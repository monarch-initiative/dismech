---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T12:24:19.886490'
end_time: '2026-08-28T12:43:11.561846'
duration_seconds: 1131.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Polycystic Kidney Disease 2
  mondo_id: MONDO:0013131
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
citation_count: 47
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Polycystic_Kidney_Disease_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Polycystic_Kidney_Disease_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Polycystic Kidney Disease 2
- **MONDO ID:** MONDO:0013131 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Polycystic Kidney Disease 2** covering all of the
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

# Polycystic Kidney Disease 2 (PKD2 / PKD2-type ADPKD): Comprehensive Disease Characterization Report

**Target disease:** Polycystic Kidney Disease 2
**MONDO ID:** MONDO:0013131 · **OMIM:** #613095 (PKD2 phenotype); *173910 (PKD2 gene) · **HGNC:** 9009 · **UniProt:** Q13563 (polycystin-2/TRPP2)
**Category:** Mendelian (autosomal dominant)

---

## Summary

Polycystic Kidney Disease 2 (PKD2) is the genetically defined, clinically milder form of **autosomal dominant polycystic kidney disease (ADPKD)**, caused by heterozygous, predominantly loss-of-function variants in **PKD2**, the gene encoding **polycystin-2 (PC2 / TRPP2)**. It accounts for approximately **15% of genetically resolved ADPKD**, with the remaining ~85% attributable to *PKD1* (polycystin-1) ([PMID: 27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/)). Polycystin-2 is a ~110 kDa, six-transmembrane, non-selective cation channel of the transient receptor potential (TRP) family that localizes to the primary cilium and co-assembles with polycystin-1 to form a mechano-/chemosensory complex governing intracellular Ca²⁺ and cyclic AMP (cAMP) signaling ([PMID: 17217069](https://pubmed.ncbi.nlm.nih.gov/17217069/); [PMID: 32251715](https://pubmed.ncbi.nlm.nih.gov/32251715/)).

Cystogenesis follows a **cellular-recessive "two-hit" mechanism**: on a germline-heterozygous background, individual tubular epithelial cells acquire a somatic "second hit" inactivating the wild-type allele, then clonally expand into fluid-filled cysts. Downstream, dysregulated **cAMP/vasopressin-V2-receptor, MAPK, mTOR and Rho/planar-cell-polarity (PCP)** signaling drives epithelial proliferation and transepithelial chloride/fluid secretion, so that hundreds-to-thousands of cysts accumulate over decades and progressively destroy renal architecture ([PMID: 11286938](https://pubmed.ncbi.nlm.nih.gov/11286938/); [PMID: 26113401](https://pubmed.ncbi.nlm.nih.gov/26113401/); [PMID: 41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/)).

Compared with PKD1, PKD2 produces fewer, later-developing cysts and substantially delayed kidney failure — **median age at death or end-stage renal disease (ESRD) ~69 years for PKD2 versus ~53 years for PKD1** — with less hypertension, urinary-tract infection and hematuria, and a distinctive female survival advantage. Nonetheless, PKD2 measurably shortens life expectancy and "cannot be regarded as a benign disorder" ([PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)). It is diagnosed by unified age-dependent ultrasound criteria supplemented by gene-panel/genome sequencing, and the vasopressin-V2-receptor antagonist **tolvaptan** is the approved disease-modifying therapy, slowing both eGFR decline and total-kidney-volume (TKV) growth ([PMID: 18945943](https://pubmed.ncbi.nlm.nih.gov/18945943/); [PMID: 37250503](https://pubmed.ncbi.nlm.nih.gov/37250503/)). This report consolidates 12 confirmed findings across 56 reviewed papers into a knowledge-base-ready characterization spanning etiology, phenotypes, molecular mechanism, anatomy, natural history, epidemiology, diagnostics, prognosis, treatment, prevention, and comparative/model-organism biology. Evidence types are indicated throughout as **[human clinical]**, **[model organism]**, **[in vitro/structural]**, **[organoid/single-cell]**, **[computational]**, or **[veterinary]**.

---

## 1. Disease Information

**Overview.** PKD2 is a subtype of ADPKD — the most common life-threatening monogenic kidney disease — characterized by progressive, bilateral development of fluid-filled renal cysts that enlarge over decades, distort renal parenchyma, and cause chronic kidney disease that may progress to ESRD. It is a systemic ciliopathy, with extrarenal cyst formation (liver, pancreas) and vascular manifestations (intracranial aneurysms, cardiovascular disease). PKD2 specifically denotes ADPKD caused by variants in the *PKD2* gene, which is clinically milder and later-onset than *PKD1*-associated disease ([PMID: 20807608](https://pubmed.ncbi.nlm.nih.gov/20807608/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013131 |
| OMIM (phenotype) | #613095 (Polycystic kidney disease 2) |
| OMIM (gene) | *173910 (PKD2) |
| HGNC (gene) | 9009 (PKD2) |
| UniProt | Q13563 (polycystin-2 / TRPP2) |
| Orphanet | ORPHA:730 (ADPKD; PKD2 as molecular subtype) |
| ICD-10 | Q61.2 (Polycystic kidney, autosomal dominant) |
| ICD-11 | GB61 / LB33 (polycystic kidney disease, autosomal dominant) |
| MeSH | D016891 (Polycystic Kidney, Autosomal Dominant) |

**Synonyms / alternative names:** ADPKD type 2; PKD2-type autosomal dominant polycystic kidney disease; polycystic kidney disease 2 (adult); PC2/TRPP2-related polycystic kidney disease.

**Data provenance:** The information in this report is derived predominantly from **aggregated disease-level resources** — OMIM, Orphanet, cohort/registry studies (e.g., the European PKD1-PKD2 Study Group, the Genkyst cohort), and mechanistic literature — rather than from individual-patient EHR data.

---

## 2. Etiology

**Primary cause (genetic).** PKD2 is a **monogenic autosomal dominant** disorder caused by germline heterozygous variants in *PKD2*. Mutations in *PKD1* or *PKD2* are the known causes of ADPKD, accounting for ~85% and ~15% of genetically resolved cases respectively: *"Mutations in PKD1 or PKD2 (∼85% and ∼15% of resolved cases, respectively) are the known causes of ADPKD"* ([PMID: 27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/)) **[human clinical]**. Cyst formation, however, is **cellular-recessive**: a germline first hit alone is insufficient, and a somatic second-hit inactivation of the wild-type allele within an individual epithelial cell is required to initiate a clonal cyst ([PMID: 11286938](https://pubmed.ncbi.nlm.nih.gov/11286938/)).

**Genetic risk factors.**
- *Causal gene:* **PKD2** (germline heterozygous variant) — the necessary and defining risk factor.
- *Genotype as modifier of severity:* In the validated **PROPKD score**, a PKD2 mutation contributes **0 points** (lowest risk): *"being male: 1 point; hypertension before 35 years of age: 2 points; first urologic event before 35 years of age: 2 points; PKD2 mutation: 0 points; nontruncating PKD1 mutation: 2 points; and truncating PKD1 mutation: 4 points"* ([PMID: 26150605](https://pubmed.ncbi.nlm.nih.gov/26150605/)) **[human clinical]**. Median age at ESRD by PROPKD risk stratum: 70.6 (low), 56.9 (intermediate), 49 years (high).
- *Somatic second hit:* A stochastic, acquired inactivation of the remaining wild-type allele triggers each cyst ([PMID: 11286938](https://pubmed.ncbi.nlm.nih.gov/11286938/); [PMID: 42436404](https://pubmed.ncbi.nlm.nih.gov/42436404/)).

**Environmental / demographic risk factors.**
- **Sex:** Male sex confers 1 PROPKD point and worse outcomes; in PKD2 specifically, women survive longer than men (71.0 vs 67.3 years), a sex effect not seen in PKD1 ([PMID: 26150605](https://pubmed.ncbi.nlm.nih.gov/26150605/); [PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)).
- **Hypertension before age 35 and early urologic events** are prognostic risk factors (2 points each in PROPKD) ([PMID: 26150605](https://pubmed.ncbi.nlm.nih.gov/26150605/)).
- **Family history of intracranial aneurysm / subarachnoid hemorrhage** raises neurovascular risk.
- Age is the principal cumulative driver — cyst burden accumulates over decades and penetrance is age-dependent.

**Protective factors.** No validated genetic protective variant is established for PKD2. The strongest relative "protective" determinant is simply carrying a *PKD2* rather than *PKD1* mutation (later onset, milder course). Female sex is associated with a survival advantage in PKD2 ([PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)). Therapeutically, hydration/vasopressin suppression and V2R antagonism slow (not prevent) progression.

**Gene–environment interactions.** A conceptual framework proposes that intrinsic sequence-dependent mutational susceptibility (guanine-rich tracts at the *PKD1* locus) interacts with a local **inflammatory microenvironment of oxidative stress and epithelial proliferation** to promote recurrent somatic second hits ([PMID: 42436404](https://pubmed.ncbi.nlm.nih.gov/42436404/)) **[computational]**. Renal injury accelerates cyst formation in animal models, indicating environmental "third-hit" stressors modulate penetrance ([PMID: 25137562](https://pubmed.ncbi.nlm.nih.gov/25137562/)) **[model organism]**.

---

## 3. Phenotypes

PKD2 shares the full clinical spectrum of ADPKD but with reduced severity and later onset. Key phenotypes, characteristics, and suggested HPO terms:

| Phenotype | HPO term | Type | Onset / severity / frequency | QoL impact |
|---|---|---|---|---|
| Multiple bilateral renal cysts | HP:0000803 / HP:0000113 | Physical/imaging | Adult-onset; progressive; near-universal in penetrant carriers | Core disease driver |
| Progressive renal insufficiency → ESRD | HP:0000083 / HP:0003774 | Lab/clinical | Late; progressive; ~50% of ADPKD reach ESRD by ~60 (later in PKD2, median ~69–74 y) | High (dialysis/transplant) |
| Hypertension | HP:0000822 | Clinical sign | Adult; less frequent in PKD2 (OR 0.25 vs PKD1) | Moderate–high |
| Hematuria | HP:0000790 | Sign/lab | Episodic; less frequent in PKD2 (OR 0.59) | Moderate |
| Urinary tract infections | HP:0000010 | Clinical | Recurrent; less frequent in PKD2 (OR 0.50) | Moderate |
| Flank/abdominal pain | HP:0030157 / HP:0011340 | Symptom | Chronic/episodic | Moderate–high |
| Nephrolithiasis | HP:0000787 | Clinical | Adult | Moderate |
| Polycystic liver disease | HP:0006557 | Physical | Adult; progressive | Variable |
| Intracranial (berry) aneurysm | HP:0004944 | Vascular | Adult; ~4–11.5% general ADPKD | Potentially catastrophic |
| Cardiac valvular abnormality / LVH | HP:0001654 / HP:0001712 | Clinical | Adult | Variable |

**Frequency data.** PKD2 patients are markedly **less likely** than PKD1 patients to have hypertension (OR 0.25), UTI history (OR 0.50), or hematuria (OR 0.59) ([PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)) **[human clinical]**. Cardiovascular manifestations — *"hypertension, left ventricular hypertrophy, cardiac valvular abnormalities, and intracranial aneurysms"* — occur in a high percentage of ADPKD patients ([PMID: 28682033](https://pubmed.ncbi.nlm.nih.gov/28682033/)). Intracranial aneurysm prevalence in general ADPKD populations is **4%–11.5%** ([PMID: 39973757](https://pubmed.ncbi.nlm.nih.gov/39973757/)).

**Age of onset / progression:** adult-onset, insidious, chronic and progressive over decades. **Severity:** mild-to-moderate relative to PKD1, but variable within and between families.

**Quality-of-life impact:** dominated by chronic pain, hypertension management, progression to dialysis/transplantation, and anxiety related to aneurysm risk. Per-phenotype standardized QoL (EQ-5D/SF-36) data specific to PKD2 were not identified and represent a knowledge gap.

---

## 4. Genetic / Molecular Information

**Causal gene.** **PKD2** (HGNC:9009; chromosome 4q22.1), encoding **polycystin-2 (PC2 / TRPP2)**, OMIM gene *173910; phenotype OMIM #613095. PKD2 accounts for ~15% of resolved ADPKD ([PMID: 27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/)).

**Protein product.** *"Polycystin-2 has a calculated molecular mass of 110 kDa, and according to structural predictions it contains six membrane-spanning domains and a pore-forming region between the 5th and 6th membrane-spanning domain"* ([PMID: 17217069](https://pubmed.ncbi.nlm.nih.gov/17217069/)) **[in vitro/structural]**. It functions as a TRPP2 non-selective cation channel in primary cilia ([PMID: 17204494](https://pubmed.ncbi.nlm.nih.gov/17204494/)).

**Variant classification and type.** Most pathogenic PKD2 variants are **truncating (loss-of-function)** — nonsense, frameshift, splice-site — but numerous **missense/point mutations** also cause disease with dramatic functional consequences ([PMID: 37028763](https://pubmed.ncbi.nlm.nih.gov/37028763/)). Comprehensive Sanger + MLPA screening of a large Italian ADPKD cohort found diagnostic variants on PKD2 in 17 of 173 mutation-positive families, including novel variants and large rearrangements ([PMID: 37231942](https://pubmed.ncbi.nlm.nih.gov/37231942/)) **[human clinical]**. Variants are classified per ACMG/AMP (pathogenic / likely pathogenic / VUS) in ClinVar.

**Functional consequences — structure-resolved.** Cryo-EM (2.7–3.2 Å) of ADPKD pore-helix variants reveals **distinct mechanisms**: *"Variant C632R reduces protein thermal stability, resulting in impaired channel assembly and abolishes primary cilia trafficking. In contrast, variants F629S and R638C retain native cilia trafficking, but exhibit gating defects"* ([PMID: 39314384](https://pubmed.ncbi.nlm.nih.gov/39314384/)) **[in vitro/structural]**. Systematic testing of 31 point mutations (in a gain-of-function PC2_F604P background) shows mutations in transmembrane, pore, and much of the extracellular "tetragonal opening for polycystins" domain are critical for channel function, whereas many C-terminal-tail mutations are mild ([PMID: 37028763](https://pubmed.ncbi.nlm.nih.gov/37028763/)). The dominant molecular mechanism is **loss of function** (channel/trafficking defect); the germline heterozygous state plus somatic second hit produces cellular loss of function.

**Origin.** Germline (inherited or de novo). Cyst-initiating second hits are **somatic** ([PMID: 11286938](https://pubmed.ncbi.nlm.nih.gov/11286938/)). Deep-intronic/pseudoexon and complex rearrangements can underlie otherwise unsolved cases ([PMID: 42502691](https://pubmed.ncbi.nlm.nih.gov/42502691/); [PMID: 37231942](https://pubmed.ncbi.nlm.nih.gov/37231942/)).

**Modifier genes / loci.** Marked within-family disease variability implies strong modifier effects: *"marked within-family renal disease variability is well documented in ADPKD and suggests a strong modifier effect from as yet unknown genetic and environmental factors"* ([PMID: 21071968](https://pubmed.ncbi.nlm.nih.gov/21071968/)). Atypical/phenocopy genes include **GANAB** (glucosidase IIα; PC1 maturation) and **DNAJB11** (ER co-chaperone), which impair polycystin-1 processing/cleavage ([PMID: 27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/); [PMID: 39530576](https://pubmed.ncbi.nlm.nih.gov/39530576/)). Sex acts as a major non-genic modifier (§5, §15).

**Epigenetic / chromosomal.** No recurrent large chromosomal abnormality defines PKD2; disease arises at the single-gene level. Metabolic reprogramming secondary to polycystin loss can alter acetyl-CoA and histone acetylation, an indirect epigenetic consequence ([PMID: 31488901](https://pubmed.ncbi.nlm.nih.gov/31488901/)). Complex genomic rearrangements at PKD loci are occasionally causal ([PMID: 37231942](https://pubmed.ncbi.nlm.nih.gov/37231942/)).

**Suggested annotations:** HGNC:9009 (PKD2); GO:0005262 (calcium channel activity); GO:0005929 (cilium); GO:0072659 (protein localization to membrane). CHEBI: cAMP (CHEBI:17489), calcium(2+) (CHEBI:29108).

---

## 5. Environmental Information

**Environmental factors.** No classical exogenous toxin, radiation, or occupational exposure is established as causal — PKD2 is fundamentally genetic. The relevant "environmental" contributor is the **local renal microenvironment**: oxidative stress and epithelial proliferation within an inflammatory milieu are proposed to promote somatic second-hit mutations, and renal injury accelerates cyst formation in models ([PMID: 42436404](https://pubmed.ncbi.nlm.nih.gov/42436404/); [PMID: 25137562](https://pubmed.ncbi.nlm.nih.gov/25137562/)).

**Lifestyle factors.** High vasopressin tone (dehydration, high salt/protein intake) drives cAMP-mediated cystogenesis; conversely, hydration and V2R suppression are protective in principle. Hypertension control modifies renal and cardiovascular outcomes. Metformin, tested as an AMPK activator, did **not** significantly slow kidney-function decline in non-diabetic ADPKD ([PMID: 41254555](https://pubmed.ncbi.nlm.nih.gov/41254555/)).

**Infectious agents.** Not applicable as a cause. Secondary complications include cyst and urinary-tract infections, but no pathogen initiates PKD2.

---

## 6. Mechanism / Pathophysiology

### Causal chain

```
Germline heterozygous PKD2 LOF variant (all cells)
        │
        ▼
Somatic "second hit" inactivating wild-type PKD2 allele in a tubular epithelial cell
   (favored by oxidative/inflammatory renal microenvironment)
        │
        ▼
Loss of functional polycystin-2 (TRPP2) channel / PC1–PC2 complex in that cell
        │
        ▼
Disrupted ciliary Ca²⁺ signaling → ↑ intracellular cAMP (vasopressin-V2R driven)
   + dysregulated mTOR, MAPK/ERK, Rho GTPase/PCP, metabolic reprogramming
        │
        ▼
Clonal epithelial proliferation + transepithelial Cl⁻/fluid secretion
        │
        ▼
Focal cyst formation → progressive enlargement (hundreds–thousands of cysts)
        │
        ▼
Distortion of parenchyma, interstitial fibrosis, inflammation
        │
        ▼
Declining GFR → chronic kidney disease → ESRD (median ~69 y in PKD2)
```

**Upstream events** are the genetic two-hit inactivation and loss of ciliary polycystin channel signaling; **downstream events** are cAMP/mTOR/MAPK/Rho-driven proliferation, fluid secretion, fibrosis and GFR loss.

**Molecular pathways.** Dysregulated **cAMP** (via vasopressin V2R), **mTOR**, **MAPK/ERK**, **Hedgehog**, and **Rho GTPase / planar-cell-polarity (PCP)** signaling ([PMID: 26113401](https://pubmed.ncbi.nlm.nih.gov/26113401/); [PMID: 33308138](https://pubmed.ncbi.nlm.nih.gov/33308138/); [PMID: 41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/)). *"Alteration of these multiple signal transduction pathways leads to cystogenesis accompanied by dysregulated planar cell polarity, excessive cell proliferation and fluid secretion"* ([PMID: 26113401](https://pubmed.ncbi.nlm.nih.gov/26113401/)).

**Cellular processes.** Excess proliferation, apoptosis dysregulation, impaired autophagy, altered planar cell polarity, and abnormal fluid secretion; primary-cilium dysfunction is central ([PMID: 34009558](https://pubmed.ncbi.nlm.nih.gov/34009558/)). Patient-derived organoids show **elongated primary cilia, polarity disruption, and elevated Rho/PCP signaling** ([PMID: 41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/)).

**Protein dysfunction.** Loss-of-function of the PC2 channel via defective assembly/trafficking (C632R) or defective gating (F629S, R638C) ([PMID: 39314384](https://pubmed.ncbi.nlm.nih.gov/39314384/)). PC1–PC2 co-assembly is required for a functional ciliary channel: *"Polycystin-1 has both ion channel and adhesion G-protein coupled receptor (GPCR) features-but its role in forming a channel complex or as a channel subunit chaperone is undetermined"* ([PMID: 32251715](https://pubmed.ncbi.nlm.nih.gov/32251715/)) **[in vitro/structural]**.

**Metabolic changes.** ADPKD cells undergo **metabolic reprogramming**; polycystins may affect metabolism through direct effects on **mitochondrial function**, altering redox state and acetyl-CoA, thereby influencing histone acetylation and gene expression ([PMID: 31488901](https://pubmed.ncbi.nlm.nih.gov/31488901/)). AMPK/mTOR is a therapeutically relevant node.

**Immune involvement / tissue damage.** A renal inflammatory microenvironment with oxidative stress promotes somatic mutation and cyst progression; interstitial **fibrosis** and inflammation are downstream tissue-damage mechanisms ([PMID: 42436404](https://pubmed.ncbi.nlm.nih.gov/42436404/); [PMID: 39530576](https://pubmed.ncbi.nlm.nih.gov/39530576/)).

**Molecular profiling.** RNA-seq of Pkd2 conditional mice shows differential expression of metabolism, cell-proliferation and immune-response genes, and sex-dependent transcriptional differences ([PMID: 41077129](https://pubmed.ncbi.nlm.nih.gov/41077129/)) **[model organism]**. *"Single-cell transcriptomics of PKD1/PKD2-mutant organoids revealed genotype-specific alterations. Genetic ablation of IFT88 disrupted cilia and selectively attenuated Rho/PCP activity in mutant backgrounds, supporting a cilia-dependent cyst-activating (CDCA) mechanism in cystogenesis"* ([PMID: 41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/)) **[organoid/single-cell]**. Single-cell multiomic methods have detected rare pathological glomerular subgroups in PKD organoids ([PMID: 42469013](https://pubmed.ncbi.nlm.nih.gov/42469013/)).

**Suggested annotations:** GO:0060271 (cilium assembly), GO:0003351 (epithelial cilium movement), GO:0007204 (positive regulation of cytosolic Ca²⁺), GO:0030036 (actin cytoskeleton organization), GO:0006874 (cellular Ca²⁺ homeostasis); CL:0002518 (kidney epithelial cell), CL:1000454 (kidney collecting duct epithelial cell), CL:1000838 (kidney proximal convoluted tubule epithelial cell).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Kidneys (UBERON:0002113) — bilateral cystic transformation of tubular epithelium. Lateralization: **bilateral**, generally symmetric.
- **Secondary organs:** Liver (UBERON:0002107) — polycystic liver disease; pancreas; occasionally spleen, ovaries, arachnoid, seminal vesicles.
- **Vascular / cardiac:** Cerebral arteries (intracranial/berry aneurysms), heart (LVH, valvular abnormalities) ([PMID: 28682033](https://pubmed.ncbi.nlm.nih.gov/28682033/)).
- **Body systems:** Renal/urinary, hepatobiliary, cardiovascular, cerebrovascular.

**Tissue / cell level.** **Renal tubular epithelial cells** are the cyst-lining cells of origin; classical ADPKD cysts arise throughout the nephron, whereas some atypical forms (DNAJB11) originate predominantly from the **proximal tubule** ([PMID: 39530576](https://pubmed.ncbi.nlm.nih.gov/39530576/)). Collecting-duct epithelium is a key site of vasopressin-V2R/cAMP-driven fluid secretion.

**Subcellular level.** The **primary cilium** (GO:0005929) is the central organelle; the **ciliary membrane**, **endoplasmic reticulum** (PC2 also resides in the ER; GO:0005783), **apical plasma membrane**, and **mitochondria** (GO:0005739) are involved.

**Suggested annotations:** UBERON:0002113 (kidney), UBERON:0001232 (collecting duct), UBERON:0004134 (proximal tubule), UBERON:0002107 (liver); CL:0002518 (renal epithelial cell).

---

## 8. Temporal Development

**Onset.** Adult-onset, **insidious and chronic**. Cysts are typically detectable in adulthood; PKD2 presents later than PKD1. Age at presentation with kidney failure is **74.0 years for PKD2 vs 54.3 years for PKD1** ([PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)).

**Progression.** Slow, **progressive**, lifelong. Cyst number and total kidney volume increase roughly exponentially with age; age-adjusted HtTKV growth rate is significantly higher in PKD1 than PKD2 carriers ([PMID: 30097754](https://pubmed.ncbi.nlm.nih.gov/30097754/)). Stages parallel CKD staging (G1→G5). Course is progressive rather than relapsing-remitting; duration is chronic/lifelong.

**Developmental switch.** *"There is a similar developmental switch in Pkd2 conditional mice with delayed cyst formation after Pkd2 inactivation at or beyond postnatal day 14"* ([PMID: 41077129](https://pubmed.ncbi.nlm.nih.gov/41077129/)) **[model organism]**. Inactivation before ~P14 causes rapid cystogenesis — implying a critical early-life window of maximal cystogenicity.

**Critical periods for intervention.** Earlier therapeutic intervention (tolvaptan in early-stage CKD) yields greater lifetime benefit ([PMID: 31014270](https://pubmed.ncbi.nlm.nih.gov/31014270/)).

---

## 9. Inheritance and Population

**Epidemiology.** ADPKD overall affects an estimated **~1 in 1,000 people** (prevalence 1:1,000–1:2,500); PKD2 constitutes ~15% of resolved cases ([PMID: 31488901](https://pubmed.ncbi.nlm.nih.gov/31488901/); [PMID: 27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/)). ADPKD accounts for ~5% of ESRD in developed countries ([PMID: 20807608](https://pubmed.ncbi.nlm.nih.gov/20807608/)).

**Inheritance & genetics.**
- **Pattern:** Autosomal dominant (germline heterozygous PKD2 variant); cyst formation requires a somatic second hit (cellular-recessive) ([PMID: 11286938](https://pubmed.ncbi.nlm.nih.gov/11286938/)).
- **Penetrance:** Age-dependent, approaching complete by later adulthood.
- **Expressivity:** Highly variable inter- and intra-familially, implying strong modifier effects ([PMID: 21071968](https://pubmed.ncbi.nlm.nih.gov/21071968/)).
- **Anticipation:** Not a feature (PKD2 is not a repeat-expansion disorder).
- **De novo / mosaicism / cryptic variants:** De novo variants occur; complex/cryptic variants can be missed by standard testing ([PMID: 42502691](https://pubmed.ncbi.nlm.nih.gov/42502691/)).

**Population demographics.**
- **Sex ratio:** Both sexes affected (AD). In PKD2, women survive longer than men (71.0 vs 67.3 y); no such sex effect in PKD1 ([PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)).
- **Geographic/ethnic distribution:** ADPKD is pan-ethnic and worldwide; no strong PKD2-specific founder effect is emphasized in the reviewed literature, though novel and population-specific variants are continually catalogued ([PMID: 37231942](https://pubmed.ncbi.nlm.nih.gov/37231942/); [PMID: 36186434](https://pubmed.ncbi.nlm.nih.gov/36186434/)).

**Natural history — PKD2 vs PKD1 (European PKD1-PKD2 Study Group; 333 PKD1, 291 PKD2, 398 controls):**

| Metric | PKD1 | PKD2 | Controls |
|---|---|---|---|
| Median age at death or ESRD (y) | 53.0 (95% CI 51.2–54.8) | **69.1 (66.9–71.3)** | 78.0 (73.8–82.2) |
| Age at presentation with kidney failure (y) | 54.3 | **74.0** | — |
| Hypertension (PKD2 vs PKD1) | ref | OR 0.25 | — |
| UTI history | ref | OR 0.50 | — |
| Hematuria | ref | OR 0.59 | — |

*"Median age at death or onset of end-stage renal disease was 53.0 years (95% CI 51.2-54.8) in individuals with PKD1, 69.1 years (66.9-71.3) in those with PKD2, and 78.0 years (73.8-82.2) in controls"* and *"Although PKD2 is clinically milder than PKD1, it has a deleterious impact on overall life expectancy and cannot be regarded as a benign disorder"* ([PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)) **[human clinical]**. PKD2 reaches ESRD roughly **16 years later** than PKD1 but still shortens life expectancy.

---

## 10. Diagnostics

**Imaging (first-line).** Renal ultrasonography is the mainstay. **Unified age-dependent ultrasound criteria** (derived to accommodate the milder PKD2) for individuals of unknown genotype: *"the presence of three or more (unilateral or bilateral) renal cysts is sufficient for establishing the diagnosis in individuals aged 15 to 39 y, two or more cysts in each kidney is sufficient for individuals aged 40 to 59 y, and four or more cysts in each kidney is required for individuals > or = 60 yr"* ([PMID: 18945943](https://pubmed.ncbi.nlm.nih.gov/18945943/)) **[human clinical]**.

| Age (y) | Diagnostic threshold | Exclusion |
|---|---|---|
| 15–39 | ≥3 renal cysts (unilateral or bilateral) | — |
| 40–59 | ≥2 cysts in **each** kidney | — |
| ≥60 | ≥4 cysts in **each** kidney | <2 cysts excludes disease at ≥40 |

Standard PKD1 criteria under-perform in PKD2 due to reduced sensitivity ([PMID: 18945943](https://pubmed.ncbi.nlm.nih.gov/18945943/); [PMID: 20219617](https://pubmed.ncbi.nlm.nih.gov/20219617/)). CT and **MRI** provide total-kidney-volume measurement (Mayo Imaging Classification; prognostic HtTKV growth rate) ([PMID: 30097754](https://pubmed.ncbi.nlm.nih.gov/30097754/)).

**Genetic testing.** Molecular testing resolves equivocal imaging, negative/indeterminate family history, and evaluation of young at-risk potential living kidney donors ([PMID: 20807608](https://pubmed.ncbi.nlm.nih.gov/20807608/)). Approaches:
- **Gene panels / targeted NGS** covering PKD1, PKD2 (and GANAB, DNAJB11, PKHD1, etc.), with **MLPA** for large rearrangements ([PMID: 37231942](https://pubmed.ncbi.nlm.nih.gov/37231942/); [PMID: 36186434](https://pubmed.ncbi.nlm.nih.gov/36186434/)).
- **Whole genome sequencing paired with transcriptome (RNA) sequencing** resolves cryptic deep-intronic/pseudoexon variants missed by exome testing: *"Genome sequencing was paired with transcriptome sequencing to evaluate the dinucleotide variant"* — a de novo deep-intronic SNV forming a dinucleotide variant with an adjacent common variant created a novel splice donor activating a 114-bp pseudoexon with an in-frame PTC ([PMID: 42502691](https://pubmed.ncbi.nlm.nih.gov/42502691/)) **[computational]**.

**Biomarkers.** Height-adjusted TKV and eGFR trajectory are the principal prognostic biomarkers; serum **endothelin-1** independently predicts hypertension and associates with renal/overall survival in ADPKD ([PMID: 30022320](https://pubmed.ncbi.nlm.nih.gov/30022320/)).

**Clinical criteria & differential diagnosis.** Diagnosis integrates family history + imaging ± genetics. Differentials: autosomal recessive PKD (PKHD1), atypical ADPKD (GANAB, DNAJB11), nephronophthisis, tuberous sclerosis, von Hippel–Lindau, acquired cystic disease, simple cysts.

**Screening.** Cascade imaging/genetic screening of at-risk relatives; presymptomatic testing and living-donor evaluation. Intracranial aneurysm screening (MRA) is targeted to those with family history of aneurysm/SAH; patients without aneurysms on initial imaging are at relatively low risk of de novo aneurysm ([PMID: 40934139](https://pubmed.ncbi.nlm.nih.gov/40934139/)).

---

## 11. Outcome / Prognosis

**Survival / mortality.** Median age at death or ESRD is **~69 years in PKD2** vs ~53 in PKD1 and ~78 in controls ([PMID: 10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/)). About **half of ADPKD patients reach ESRD by ~60**, later in PKD2. PKD2 shortens overall life expectancy despite its milder course.

**Morbidity.** Hypertension, chronic pain, nephrolithiasis, cyst/urinary infections, polycystic liver disease, and cardiovascular/cerebrovascular complications. Intracranial aneurysm rupture is a low-frequency but high-severity outcome.

**Prognostic factors.** Genotype (PKD2 = lowest PROPKD risk, 0 points), sex (male worse; female advantage specific to PKD2), early hypertension, early urologic events, and TKV/HtTKV growth rate ([PMID: 26150605](https://pubmed.ncbi.nlm.nih.gov/26150605/); [PMID: 30097754](https://pubmed.ncbi.nlm.nih.gov/30097754/)). Endothelin-1 is a prognostic vascular biomarker ([PMID: 30022320](https://pubmed.ncbi.nlm.nih.gov/30022320/)).

**Recovery.** No cure; ESRD is managed by dialysis and kidney transplantation (excellent post-transplant outcomes). Disease-modifying therapy slows but does not halt progression.

---

## 12. Treatment

**Disease-modifying pharmacotherapy — tolvaptan (vasopressin V2-receptor antagonist).** Tolvaptan slows both **TKV growth and renal-function decline** over 3 years (TEMPO 3:4, NCT00428948), confirmed in the TEMPO extension and REPRISE (NCT02160145) trials ([PMID: 33471240](https://pubmed.ncbi.nlm.nih.gov/33471240/); [PMID: 30689194](https://pubmed.ncbi.nlm.nih.gov/30689194/)). A pooled analysis in older patients (>55 y, CKD G3/G4; 95 matched pairs) showed *"The eGFR annual decline rate was significantly reduced by 1.66 mL/min/1.73"* vs standard of care ([PMID: 37250503](https://pubmed.ncbi.nlm.nih.gov/37250503/)) **[human clinical]**. Benefit on eGFR occurs **regardless of TKV response** ([PMID: 33471240](https://pubmed.ncbi.nlm.nih.gov/33471240/)). Modeling predicts ESRD delay of ~5 years (up to 6.6 y in early CKD) ([PMID: 31014270](https://pubmed.ncbi.nlm.nih.gov/31014270/)). *"Tolvaptan has demonstrated efficacy in slowing kidney enlargement and preserving eGFR in high-risk patients. Its use requires careful monitoring of liver enzymes and management of aquaretic side-effects"* ([PMID: 41815030](https://pubmed.ncbi.nlm.nih.gov/41815030/)). It is safe in combination with statins ([PMID: 32241780](https://pubmed.ncbi.nlm.nih.gov/32241780/)). *Mechanism:* V2R blockade lowers collecting-duct cAMP, reducing proliferation and fluid secretion. **NCIT:** C61895 (Tolvaptan).

**Other pharmacotherapy.**
- **Octreotide-LAR** (somatostatin analog) — approved in some settings; reduces cyst growth ([PMID: 34009558](https://pubmed.ncbi.nlm.nih.gov/34009558/)).
- **Antihypertensives:** ACE inhibitors / ARBs are agents of choice ([PMID: 28682033](https://pubmed.ncbi.nlm.nih.gov/28682033/)). NCIT: C61627 (ACE inhibitor).
- **Metformin (AMPK activator):** meta-analysis of 4 RCTs (213 non-diabetic ADPKD patients) found **no significant effect** on eGFR decline (SMD 0.19; 95% CI −0.08 to 0.46; p=0.17) or htTKV (p=0.53), with more GI adverse events (RR 2.93) ([PMID: 41254555](https://pubmed.ncbi.nlm.nih.gov/41254555/)).
- **Pioglitazone (PPARγ agonist):** preclinical promise, under clinical evaluation ([PMID: 33308138](https://pubmed.ncbi.nlm.nih.gov/33308138/)).
- **Probenecid (adjunct):** ABCG2 inhibition attenuated tolvaptan-induced polyuria while preserving efficacy in a preclinical ADPKD model and reduced urine volume/nocturia in a phase II trial ([PMID: 42298327](https://pubmed.ncbi.nlm.nih.gov/42298327/)).

**Experimental / emerging targets.** EGFR, AMPK, KEAP1-Nrf2, sphingolipids, MAPK, and cell therapy are under investigation ([PMID: 34009558](https://pubmed.ncbi.nlm.nih.gov/34009558/)). Patient-derived organoid HTS nominates **Rho GTPase inhibitors (e.g., ML141)** as cyst-reducing across PKD1/PKD2 genotypes ([PMID: 41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/)); **valosin-containing protein (VCP)** is a novel ciliary-morphology target ([PMID: 40662578](https://pubmed.ncbi.nlm.nih.gov/40662578/)).

**Surgical / interventional.** Cyst aspiration/fenestration for pain, nephrectomy (space/infection/pre-transplant), and — for ESRD — **dialysis and kidney transplantation** (NCIT: C15366). Aneurysm clipping/coiling where indicated.

**Supportive care.** Pain control, hydration, blood-pressure control, treatment of infections and stones, statins for cardiovascular risk.

**Personalized medicine.** Genotype (PKD2 vs PKD1, truncating vs non-truncating) and TKV-based Mayo class guide risk stratification and tolvaptan candidacy ([PMID: 26150605](https://pubmed.ncbi.nlm.nih.gov/26150605/); [PMID: 30097754](https://pubmed.ncbi.nlm.nih.gov/30097754/)).

---

## 13. Prevention

- **Primary prevention:** Not possible for a monogenic germline disease. Risk-factor modification (blood-pressure control, hydration/vasopressin suppression, avoidance of nephrotoxins) mitigates progression.
- **Secondary prevention:** Early diagnosis via cascade imaging/genetic screening; early tolvaptan in rapid progressors; targeted MRA aneurysm screening for those with family history ([PMID: 40934139](https://pubmed.ncbi.nlm.nih.gov/40934139/)).
- **Tertiary prevention:** Manage hypertension, CKD, infections, aneurysms; timely transplant planning.
- **Reproductive / genetic prevention:** *"preimplantation genetic testing (PGT) for polycystic kidney disease"* is validated and applied clinically, including for PKD2 couples ([PMID: 30927425](https://pubmed.ncbi.nlm.nih.gov/30927425/)) **[human clinical]**. Prenatal testing and genetic counseling (risk assessment, family planning) are standard.
- **Immunization / public health:** Not applicable (non-infectious, non-environmental etiology).

---

## 14. Other Species / Natural Disease

**Key finding:** Naturally occurring ADPKD in companion animals is **PKD1-orthologous, not PKD2**. *"Autosomal dominant polycystic kidney disease (ADPKD) is a common inherited disease in cats"* ([PMID: 37489504](https://pubmed.ncbi.nlm.nih.gov/37489504/)) **[veterinary]**, and it is *"associated with a mutation from C to A at position 10063 in exon 29 of the feline PKD1 gene"* ([PMID: 31155548](https://pubmed.ncbi.nlm.nih.gov/31155548/)) **[veterinary]** — i.e., the polycystin-1 ortholog. Feline ADPKD is common in Persian/Persian-related and Scottish Fold cats; in a University of Tokyo referral cohort (n=1,281), 1.8% carried the conventional PKD1 variant; concurrent renal+hepatic cysts occur (~12.6%, up to 31% in Persians), and Budd-Chiari-like complications are described ([PMID: 32687010](https://pubmed.ncbi.nlm.nih.gov/32687010/); [PMID: 41669239](https://pubmed.ncbi.nlm.nih.gov/41669239/)).

**Implication:** No established naturally occurring **PKD2-orthologous** polycystic kidney disease exists in companion animals; PKD2 disease biology depends on **engineered rodent models**.

**Taxonomy / orthologs (suggested):** NCBI Taxon 9606 (human), 10090 (mouse), 10116 (rat), 9685 (cat), 7955 (zebrafish). Orthologous gene: mouse Pkd2 (NCBI Gene 18764); human PKD2 (NCBI Gene 5311). The cilia-polycystin axis is broadly conserved across vertebrates.

---

## 15. Model Organisms

**Requirement for conditional models.** Germline **Pkd2 (and Pkd1) knockout is embryonic-lethal**, so conditional/inducible models are required ([PMID: 41077129](https://pubmed.ncbi.nlm.nih.gov/41077129/); [PMID: 25137562](https://pubmed.ncbi.nlm.nih.gov/25137562/)).

**Mouse (primary model).** Kidney-specific conditional *Pkd2* knockouts recapitulate cystogenesis and reveal:
- A **developmental switch** — *"delayed cyst formation after Pkd2 inactivation at or beyond postnatal day 14"* ([PMID: 41077129](https://pubmed.ncbi.nlm.nih.gov/41077129/)) **[model organism]**.
- **Sex as a major disease modifier:** *"We confirm that sex is a key modifier of ADPKD progression with differences in disease severity occurring in the context of significant transcriptional differences between males and females that are independent of the Pkd2 genotype"* ([PMID: 41077129](https://pubmed.ncbi.nlm.nih.gov/41077129/)) **[model organism]**.
- Genetic-interaction studies: ablating ciliary adenylyl-cyclase trafficking (**ANKMY2**) or adenylyl-cyclase-to-cilia targeting suppresses cystogenesis in Pkd1 models, and IFT88 ablation confirms cilia-dependent cystogenesis ([PMID: 41474822](https://pubmed.ncbi.nlm.nih.gov/41474822/); [PMID: 40501923](https://pubmed.ncbi.nlm.nih.gov/40501923/)).

**Non-mammalian / in vitro.** *Xenopus* oocytes for PC2 channel electrophysiology ([PMID: 37028763](https://pubmed.ncbi.nlm.nih.gov/37028763/)); cryo-EM structural biology of PC2 variants ([PMID: 39314384](https://pubmed.ncbi.nlm.nih.gov/39314384/)); **patient-derived multi-lineage adult renal organoids (MAROs)** that recapitulate elongated cilia, polarity disruption, elevated Rho/PCP signaling, and enable single-cell transcriptomics and HTS drug screening across PKD1/PKD2 genotypes ([PMID: 41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/); [PMID: 42469013](https://pubmed.ncbi.nlm.nih.gov/42469013/)).

**Model types available:** knockout, conditional/inducible knockout, gain-of-function point-mutant channels (e.g., PC2_F604P). **Phenotype recapitulation:** strong for renal cystogenesis, cilia biology, and signaling. **Limitations:** embryonic lethality of full knockouts; rodent Pkd2/Pkd1 escape the recurrent somatic mutagenesis seen at the human locus (guanine-rich architecture), limiting spontaneous two-hit modeling ([PMID: 42436404](https://pubmed.ncbi.nlm.nih.gov/42436404/)); standardized QoL/extrarenal features incompletely captured.

**Resources:** MGI (mouse), RGD (rat), ZFIN (zebrafish), IMPC/KOMP, Cellosaurus (organoid/cell lines).

---

## Mechanistic Model / Interpretation

PKD2 is best understood as a **ciliary channelopathy operating through a two-hit, dosage-sensitive mechanism**. The germline PKD2 loss-of-function variant sets a permissive background; a stochastic somatic second hit — favored by an oxidative, proliferative, inflammatory renal microenvironment — extinguishes functional polycystin-2 in a single tubular cell. Because PC2 (with PC1) tunes ciliary Ca²⁺ and restrains cAMP, its loss unleashes a proliferative-secretory program (cAMP↑, mTOR, MAPK, Rho/PCP), converting the affected clone into an expanding cyst. Multiplied across a lifetime and across thousands of nephrons, this produces the macroscopic bilateral cystic kidneys and progressive GFR loss.

The comparatively mild PKD2 phenotype — 0 PROPKD points, ~16-year-later ESRD, less hypertension/hematuria/UTI — reflects **residual/less-disruptive polycystin complex function and slower cyst kinetics** relative to PKD1, not a different mechanism. This unifies the clinical, structural, and model-organism data: cryo-EM shows variant-specific trafficking-vs-gating defects; conditional mice show a postnatal developmental switch and sex modification; organoids show genotype-specific but mechanistically convergent Rho/PCP-driven, cilia-dependent cystogenesis. Therapeutically, everything downstream of cAMP is the tractable target — hence tolvaptan's efficacy, probenecid's aquaretic-sparing adjunct role, and the emerging Rho-inhibitor and adenylyl-cyclase-trafficking strategies.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [10023895](https://pubmed.ncbi.nlm.nih.gov/10023895/) | Definitive PKD2 vs PKD1 natural history (median ESRD/death 69.1 vs 53.0 y); milder but not benign; female survival advantage | Human clinical |
| [27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/) | PKD2 ≈15% of resolved ADPKD; GANAB as atypical gene | Human clinical |
| [26150605](https://pubmed.ncbi.nlm.nih.gov/26150605/) | PROPKD score — PKD2 = 0 points (lowest risk) | Human clinical |
| [17217069](https://pubmed.ncbi.nlm.nih.gov/17217069/) | PC2/TRPP2 = 110 kDa, 6-TM, pore between TM5–TM6 | In vitro/structural |
| [39314384](https://pubmed.ncbi.nlm.nih.gov/39314384/) | Cryo-EM: C632R trafficking defect; F629S/R638C gating defects | In vitro/structural |
| [11286938](https://pubmed.ncbi.nlm.nih.gov/11286938/) | Two-hit cellular-recessive clonal cystogenesis model | Model/conceptual |
| [26113401](https://pubmed.ncbi.nlm.nih.gov/26113401/) | Multi-pathway cystogenesis: PCP, proliferation, fluid secretion | Review |
| [41077129](https://pubmed.ncbi.nlm.nih.gov/41077129/) | Conditional Pkd2 developmental switch; sex as major modifier | Model organism |
| [28682033](https://pubmed.ncbi.nlm.nih.gov/28682033/) | Cardiovascular/neurovascular extrarenal manifestations | Review |
| [39973757](https://pubmed.ncbi.nlm.nih.gov/39973757/) | ICA prevalence 4–11.5% in general ADPKD | Human clinical |
| [37250503](https://pubmed.ncbi.nlm.nih.gov/37250503/) | Tolvaptan reduces annual eGFR decline by ~1.66 mL/min/1.73 m² | Human clinical |
| [41815030](https://pubmed.ncbi.nlm.nih.gov/41815030/) | Tolvaptan efficacy + monitoring requirements | Review |
| [18945943](https://pubmed.ncbi.nlm.nih.gov/18945943/) | Unified age-dependent ultrasound diagnostic criteria | Human clinical |
| [32251715](https://pubmed.ncbi.nlm.nih.gov/32251715/) | PC1 co-assembly/chaperone role with PC2 channel in cilia | In vitro/structural |
| [21071968](https://pubmed.ncbi.nlm.nih.gov/21071968/) | Variable expressivity / modifier effects | Review |
| [30927425](https://pubmed.ncbi.nlm.nih.gov/30927425/) | PGT applied clinically for PKD | Human clinical |
| [41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/) | Patient organoids: genotype-specific cystogenesis; Rho/PCP inhibitors (CDCA) | Organoid/single-cell |
| [42502691](https://pubmed.ncbi.nlm.nih.gov/42502691/) | Genome+RNA-seq resolves cryptic pseudoexon variants | Computational |
| [31155548](https://pubmed.ncbi.nlm.nih.gov/31155548/) / [37489504](https://pubmed.ncbi.nlm.nih.gov/37489504/) | Natural feline ADPKD is PKD1-orthologous, not PKD2 | Veterinary |
| [41254555](https://pubmed.ncbi.nlm.nih.gov/41254555/) | Metformin: no significant benefit in non-diabetic ADPKD | Human clinical (meta-analysis) |
| [42298327](https://pubmed.ncbi.nlm.nih.gov/42298327/) | Probenecid mitigates tolvaptan aquaresis while preserving efficacy | Model + phase II |

---

## Limitations and Knowledge Gaps

1. **No primary experimental dataset** was analyzed; conclusions rest on literature synthesis of aggregated disease-level resources, not de novo statistical analysis of patient-level data.
2. **PKD2-specific QoL** (EQ-5D/SF-36/PROMIS) data are sparse; most QoL and cardiovascular figures derive from mixed ADPKD (PKD1+PKD2) cohorts.
3. **Modifier genes** driving PKD2's marked intra-familial variability remain largely unidentified ([PMID: 21071968](https://pubmed.ncbi.nlm.nih.gov/21071968/)).
4. **Founder effects / geographic variant distribution** specific to PKD2 were not well characterized in the reviewed literature.
5. **No natural PKD2 animal model** exists; mechanistic inferences transfer from PKD1 models and engineered Pkd2 mice, which may not capture human-specific somatic-mutation dynamics ([PMID: 42436404](https://pubmed.ncbi.nlm.nih.gov/42436404/)).
6. **Therapeutic evidence** is dominated by mixed-genotype ADPKD trials; PKD2-subgroup-specific efficacy of tolvaptan and emerging agents is under-reported.

---

## Proposed Follow-up Experiments / Actions

1. **PKD2-stratified re-analysis** of tolvaptan trial data (TEMPO/REPRISE) to quantify genotype-specific eGFR/TKV effect sizes and number-needed-to-treat.
2. **Modifier-locus GWAS/burden analysis** within PKD2 families to explain the female survival advantage and intra-familial variability.
3. **Prospective PKD2 organoid biobank** with single-cell multi-omics to map genotype-specific cystogenic trajectories and validate Rho/PCP and adenylyl-cyclase-trafficking (ANKMY2) targets as PKD2-effective ([PMID: 41946363](https://pubmed.ncbi.nlm.nih.gov/41946363/); [PMID: 41474822](https://pubmed.ncbi.nlm.nih.gov/41474822/)).
4. **Structure-guided variant functional classification** — extend cryo-EM/electrophysiology to reclassify PKD2 VUS as trafficking- vs gating-defective, informing ACMG calls ([PMID: 39314384](https://pubmed.ncbi.nlm.nih.gov/39314384/)).
5. **Clinical trial of probenecid–tolvaptan co-therapy** in PKD2 to improve tolerability/adherence ([PMID: 42298327](https://pubmed.ncbi.nlm.nih.gov/42298327/)).
6. **Routine genome+RNA-seq** for ultrasound-positive but molecularly unsolved ADPKD to capture cryptic PKD2 pseudoexon/deep-intronic variants ([PMID: 42502691](https://pubmed.ncbi.nlm.nih.gov/42502691/)).
7. **PKD2-specific QoL cohort study** using EQ-5D/PROMIS to fill the quality-of-life evidence gap.

---

*Report compiled from 12 confirmed findings across 56 reviewed papers over 5 investigative iterations. Evidence source types are distinguished throughout (human clinical, model organism, in vitro/structural, organoid/single-cell, computational, veterinary). All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Polycystic_Kidney_Disease_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Polycystic_Kidney_Disease_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 47 |
| On topic | 46 |
| Off topic | 0 |

All extracted references resolved successfully.
