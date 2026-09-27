---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T12:24:19.726192'
end_time: '2026-08-28T12:39:39.253210'
duration_seconds: 919.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ZMYND11-related intellectual disability, autosomal dominant 30 (MRD30)
  mondo_id: MONDO:0014486
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 13
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Disability_Autosomal_Dominant_30-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Disability_Autosomal_Dominant_30-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ZMYND11-related intellectual disability, autosomal dominant 30 (MRD30)
- **MONDO ID:** MONDO:0014486 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ZMYND11-related intellectual disability, autosomal dominant 30 (MRD30)** covering all of the
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

# ZMYND11-Related Intellectual Disability, Autosomal Dominant 30 (MRD30): A Comprehensive Disease Characterization

**Disease:** ZMYND11-related intellectual disability, autosomal dominant 30 (MRD30)
**OMIM:** #616083 · **MONDO:** MONDO:0014486 · **Gene:** *ZMYND11* (10p15.3) · **Category:** Mendelian, autosomal dominant

---

## Summary

**MRD30 is an ultra-rare, autosomal dominant neurodevelopmental disorder caused by heterozygous loss-of-function (haploinsufficiency) of *ZMYND11* at chromosome 10p15.3.** *ZMYND11* is the critical gene of the contiguous 10p15.3 microdeletion syndrome: patients with 10p15.3 deletions and patients with intragenic *ZMYND11* truncating variants share an overlapping core phenotype of hypotonia, intellectual disability/global developmental delay, facial dysmorphism, speech and motor delay, seizures, and significant behavioral problems. An intragenic deletion affecting only the 5′UTR and first two exons confirms that a single functional copy of the gene is insufficient — the mechanism is haploinsufficiency, not a dominant-negative or gain-of-function effect ([PMID: 34818214](https://pubmed.ncbi.nlm.nih.gov/34818214/); [PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/)).

Mechanistically, ZMYND11 (also called **BS69** or **BRAM1**) is a **chromatin reader** that specifically recognizes the trimethylated histone variant **H3.3 at lysine 36 (H3.3K36me3)** through its tandem PHD–Bromo–PWWP domains, and additionally carries a C-terminal MYND zinc-finger domain. Reading this histone mark, ZMYND11 fine-tunes RNA polymerase II transcription (elongation control, promoter/initiation occupancy, Pol II pausing) and couples chromatin state to pre-mRNA splicing, mainly regulating intron retention by antagonizing the U5 snRNP component EFTUD2. In the developing human cortex, ZMYND11 loss de-represses latent developmental gene programs, releases restraint on the histone methyltransferase KMT2A, and disrupts a brain-specific RNA isoform switch mediated by the splicing regulator RBFOX2 — collectively impairing cortical progenitor and neuron production ([PMID: 25263594](https://pubmed.ncbi.nlm.nih.gov/25263594/); [PMID: 41068108](https://pubmed.ncbi.nlm.nih.gov/41068108/); [PMID: 41279818](https://pubmed.ncbi.nlm.nih.gov/41279818/)).

Clinically, MRD30 is a lifelong, largely **static (non-neurodegenerative)** disorder with congenital-to-early-childhood onset. Neurodevelopmental deficits are essentially fully penetrant; dysmorphic features and epilepsy are variable, with seizure prognosis ranging from spontaneous remission to drug resistance. Most pathogenic variants arise **de novo**, but rare inherited cases from mildly affected parents demonstrate variable expressivity and incomplete penetrance. There is **no curative or gene-specific therapy**; management is symptomatic and multidisciplinary. This report synthesizes 14 confirmed findings from 28 reviewed papers into a complete disease knowledge-base entry across all 15 requested domains.

---

## 1. Disease Information

MRD30 is a Mendelian, monogenic neurodevelopmental disorder in the intellectual-disability spectrum. It is defined molecularly by haploinsufficiency of *ZMYND11* and represents the "pure gene" counterpart of the 10p15.3 microdeletion syndrome, in which *ZMYND11* is the critical dosage-sensitive gene ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/)).

**Key identifiers (F014):**

| Resource | Identifier |
|---|---|
| OMIM | #616083 (Intellectual developmental disorder, autosomal dominant 30; MRD30) |
| MONDO | MONDO:0014486 |
| Gene (HGNC) | *ZMYND11*, HGNC:29316 |
| NCBI Gene | 10778 |
| UniProt | Q15326 |
| Locus | 10p15.3 |
| Gene aliases | BS69, BRAM1 |

**Synonyms / alternative names (F014):** ZMYND11-related intellectual disability; ZMYND11-related neurodevelopmental disorder; ZMYND11-related syndromic intellectual disability; MRD30; and — for the deletion form — 10p15.3 microdeletion syndrome (of which *ZMYND11* is the critical gene).

**Information source type:** The knowledge base for MRD30 is derived from **aggregated case reports and small cohorts** plus functional/mechanistic studies (patient-derived iPSC/cortical organoid, mouse ESC/MEF, and zebrafish models), **not** from population-scale EHR datasets ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/)). Suggested ontology mapping: **MONDO:0014486**.

---

## 2. Etiology

**Disease causal factors (F014):** MRD30 etiology is **exclusively genetic**. It is caused by heterozygous loss-of-function or deleterious variants in *ZMYND11* (nonsense, frameshift, canonical splice-site, missense, whole-gene or intragenic deletions) or by 10p15.3 deletions that remove *ZMYND11*. There are **no established environmental, lifestyle, toxic, occupational, or infectious causal or risk factors**, and no known protective factors or gene–environment interactions.

**Genetic risk factors:** The only risk factor is carriage of a pathogenic *ZMYND11* variant. *ZMYND11* is a highly loss-of-function–intolerant, dosage-sensitive gene; heterozygous LoF is sufficient to cause disease, and pathogenic LoF alleles are essentially absent from population controls (gnomAD) (F013). Variants are distributed across the gene with no precise genotype–phenotype correlation, though missense and LoF classes show partially distinct phenotypic emphases (see Section 4) ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/); [PMID: 41820311](https://pubmed.ncbi.nlm.nih.gov/41820311/)).

**Environmental / lifestyle / infectious factors:** None identified or applicable (F014). No CTD/toxicogenomic, NHANES-type lifestyle, or infectious-agent associations are established for this monogenic disorder.

**Gene–environment interactions:** None reported.

---

## 3. Phenotypes

The MRD30 core phenotype is a syndromic neurodevelopmental disorder. Across cohorts, affected individuals show **hypotonia, intellectual disability/global developmental delay, facial dysmorphism, speech and motor delay, seizures, and significant behavioral problems** (including autism spectrum disorder, ADHD, and aggression) ([PMID: 34818214](https://pubmed.ncbi.nlm.nih.gov/34818214/); F003).

> *"patients harboring 10p15.3 microdeletions or pathogenic ZMYND11 truncating variants share similar clinical features including hypotonia, intellectual disability, facial dysmorphisms, speech and motor delays, seizures, and significant behavioral problems"* ([PMID: 34818214](https://pubmed.ncbi.nlm.nih.gov/34818214/))

**Epilepsy subtypes (F003).** In a cohort of ~20 individuals, ZMYND11-associated epilepsy fell into three groups:

| Epilepsy group | n | Notes |
|---|---|---|
| (i) Atypical benign partial epilepsy (ABPE) / idiopathic focal epilepsy | 8 | Centrotemporal features |
| (ii) Generalised epilepsies / infantile epileptic encephalopathy | 4 | More severe end |
| (iii) Unclassified | 8 | — |

> *"Individuals with ZMYND11 associated epilepsy fell into three groups: (i) atypical benign partial epilepsy or idiopathic focal epilepsy (n = 8); (ii) generalised epilepsies/infantile epileptic encephalopathy (n = 4); (iii) unclassified (n = 8)"* ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/))

**Phenotype characteristics.** Onset is congenital to early childhood. **"Neurodevelopmental deficits were invariable. Dysmorphic features were variable."** ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/)) — i.e., near-complete penetrance for the neurodevelopmental core, with variable expressivity of dysmorphism and epilepsy. Seizure progression ranges from spontaneous remission to drug-resistant. Individual reports additionally document **sensorineural hearing loss, ataxic gait, a happy disposition (Angelman-like), and rarer features** such as eosinophilic esophagitis and severe allergies.

> *"seizures, global developmental delay, sensorineural hearing loss, hypotonia, dysmorphic features, and other features including a happy disposition and ataxic gait similar to Angelman syndrome"* ([PMID: 27626064](https://pubmed.ncbi.nlm.nih.gov/27626064/))

**Suggested HPO terms:**

| Phenotype | HPO term | Frequency / severity |
|---|---|---|
| Intellectual disability / global developmental delay | HP:0001249 / HP:0001263 | Invariable (near-100%); mild–severe |
| Hypotonia | HP:0001252 | Common |
| Seizures | HP:0001250 | Variable subset; remission to drug-resistant |
| Delayed speech and language development | HP:0000750 | Common |
| Motor delay | HP:0001270 | Common |
| Autism spectrum disorder / behavioral abnormality | HP:0000729 / HP:0000708 | Common |
| Facial dysmorphism | HP:0001999 | Variable |
| Sensorineural hearing impairment | HP:0000407 | Reported (subset) |
| Strabismus | HP:0000486 | Enriched in missense variants |
| Ataxic gait | HP:0002066 | Reported |
| Aggressive behavior | HP:0000718 | Reported |

**Quality-of-life impact.** Disease-specific EQ-5D/SF-36 data are **not available** for this ultra-rare disorder. By clinical extrapolation, lifelong intellectual disability, communication impairment, behavioral difficulties, and (in a subset) epilepsy substantially affect daily functioning, independence, and caregiver burden.

---

## 4. Genetic / Molecular Information

**Causal gene (F001, F014):** *ZMYND11* (zinc finger MYND-type containing 11; alias BS69/BRAM1), 10p15.3; HGNC:29316; NCBI Gene 10778; UniProt Q15326; OMIM disease #616083.

**Variant spectrum and classification (F006, F008, F013).** Most reported MRD30 patients carry **loss-of-function** variants — nonsense, frameshift, canonical splice-site, and whole/partial-gene deletions. **Missense variants are rarer** (~13 reported) and their mechanistic characteristics are less defined. Variants are classified per ACMG/AMP criteria and are distributed across the gene with no precise genotype–phenotype correlation.

> *"Most previously reported patients harbor loss-of-function (LoF) variants, whereas missense variants are rare and their clinical and mechanistic characteristics remain insufficiently defined"* ([PMID: 41820311](https://pubmed.ncbi.nlm.nih.gov/41820311/))

**Missense vs. LoF genotype–phenotype (F006).** Aggregate analysis of the 13 reported missense variants (including recurrent **c.1798C>T, p.Arg600Trp**) suggests higher frequencies of **strabismus, hypotonia, and severe intellectual disability** than LoF variants, plus associations with microcephaly, broad nasal alae, short stature, cryptorchidism, and nipple anomalies.

> *"Aggregate analysis of reported 13 missense variants suggested higher frequencies of strabismus, hypotonia and severe intellectual disability compared with LoF variants"* ([PMID: 41820311](https://pubmed.ncbi.nlm.nih.gov/41820311/))

**Allele frequency / origin.** Pathogenic *ZMYND11* LoF alleles are essentially **absent from population databases (gnomAD)**, consistent with strong LoF constraint. Variants are **germline** (not somatic in the disease context) and mostly **de novo**, with rare inherited cases (F013).

**Functional consequences (F001).** The unifying mechanism is **loss of function / haploinsufficiency**. An intragenic deletion removing only the 5′UTR + first two exons produced the same phenotype, confirming that reduced dosage — rather than a dominant-negative product — drives disease.

> *"our report contributes to expand the clinical and mutational spectrum of ZMYND11 and confirms haploinsufficiency as the underlying disease mechanism"* ([PMID: 34818214](https://pubmed.ncbi.nlm.nih.gov/34818214/))

**Dosage sensitivity / chromatinopathy overlap (F006).** ZMYND11 is dosage-sensitive; its perturbation has also been linked to **Cornelia de Lange Syndrome (CdLS)-like** phenotypes, placing MRD30 within the broader family of chromatinopathies. Adult presentations may include movement disorders. Independently, *ZMYND11* LoF is an FDR-significant **schizophrenia** risk gene ([PMID: 40753099](https://pubmed.ncbi.nlm.nih.gov/40753099/)).

> *"ZMYND11, a dosage-sensitive gene, has been associated with Cornelia de Lange Syndrome (CdLS)-like phenotypes, and its haploinsufficiency is linked to 10p15.3 microdeletion syndrome"* ([PMID: 42003802](https://pubmed.ncbi.nlm.nih.gov/42003802/))

**Modifier genes.** None specifically established for pure MRD30. In the contiguous-deletion form, co-deleted neighbors (*DIP2C*, *GATA3*) modify the phenotype (Section 10).

**Epigenetic information.** ZMYND11's own function is epigenetic (H3.3K36me3 reading); no disease-specific DNA-methylation episignature has been definitively established, though its role in chromatin regulation makes an episignature plausible (a knowledge gap).

**Chromosomal abnormalities (F008, F010).** 10p15.3 deletions (detected by CMA/karyotype/FISH), ring chromosome 10, inv dup del(10p), and complex rearrangements involving 10p can remove *ZMYND11* and cause the deletion form of the disorder.

**Suggested ontology terms:** Gene product — **UniProt Q15326**; molecular function — **GO:0035064** (methylated histone binding), **GO:0003682** (chromatin binding).

---

## 5. Environmental Information

**Not applicable.** MRD30 is a monogenic disorder with no established environmental, lifestyle, or infectious contributors (F014). No toxin, radiation, pollution, occupational-exposure, dietary, or pathogen association is documented. This section is included for completeness and is explicitly negative.

---

## 6. Mechanism / Pathophysiology

### Domain architecture and histone-reader function (F002, F004)

ZMYND11/BS69 contains tandemly arranged **PHD, Bromo, and PWWP** chromatin-recognition modules plus a C-terminal **MYND** zinc-finger domain. Together these read the histone variant mark **H3.3K36me3**.

> *"BS69 (also called ZMYND11) contains tandemly arranged PHD, BROMO, and PWWP domains, which are chromatin recognition modalities. Here, we show that BS69 selectively recognizes histone variant H3.3 lysine 36 trimethylation (H3.3K36me3) via its chromatin-binding domains."* ([PMID: 25263594](https://pubmed.ncbi.nlm.nih.gov/25263594/))

ZMYND11 was originally identified as a specific reader for H3.3K36me3 and a candidate tumor suppressor; some oncogenic H3.3 mutations abrogate the H3.3K36me3/BS69 interaction, underscoring its functional importance.

> *"two recent studies identified BS69/ZMYND11, which was proposed to be a candidate tumor suppressor, as a specific reader for a modified form of H3.3 (H3.3K36me3)"* ([PMID: 25453099](https://pubmed.ncbi.nlm.nih.gov/25453099/))

The chromatin-reader function connects directly to epilepsy pathogenesis: *"ZMYND11 is one of a small group of chromatin reader genes associated in the pathogenesis of epilepsy, and specifically ABPE"* ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/)).

### Coupling chromatin to transcription and splicing (F004)

Beyond elongation control, ZMYND11 couples the H3K36me3 chromatin state to **pre-mRNA processing**, mainly regulating **intron retention (IR)** by antagonizing the U5 snRNP spliceosome component **EFTUD2**; this depends on binding H3K36me3-decorated chromatin.

> *"BS69 mainly regulates intron retention (IR)... BS69 promotes IR by antagonizing EFTUD2 through physical interactions. We further show that regulation of IR by BS69 also depends on its binding to H3K36me3-decorated chromatin."* ([PMID: 25263594](https://pubmed.ncbi.nlm.nih.gov/25263594/))

More recent data show ZMYND11 also localizes to **gene promoters** and regulates **transcription initiation**:

> *"ZMYND11 deficiency reduces the pausing index of Pol II, H3.3, and H3K36me3, indicating impaired transcription initiation"* ([PMID: 42262664](https://pubmed.ncbi.nlm.nih.gov/42262664/))

### Neurodevelopmental convergence (F005, F007)

In human cortical models, **ZMYND11 mutations impair cortical progenitor and neuron production**; ZMYND11-deficient neural stem cells **upregulate inappropriate developmental pathways**, disrupting neurogenesis, and ZMYND11 controls a **brain-specific RNA isoform switch involving RBFOX2**.

> *"mutations in ZMYND11, a newly implicated risk gene, impair human cortical progenitor and neuron production"* ([PMID: 41068108](https://pubmed.ncbi.nlm.nih.gov/41068108/))
> *"ZMYND11-deficient cortical neural stem cells upregulate inappropriate developmental pathways, leading to disrupted neurogenesis"* ([PMID: 41068108](https://pubmed.ncbi.nlm.nih.gov/41068108/))
> *"ZMYND11 regulates a brain-specific RNA isoform switch involving the splicing regulator RBFOX2"* ([PMID: 41068108](https://pubmed.ncbi.nlm.nih.gov/41068108/))

A complementary mechanistic axis: **ZMYND11 restrains the histone methyltransferase KMT2A (MLL1)** to enable a neuronal developmental program ([PMID: 41279818](https://pubmed.ncbi.nlm.nih.gov/41279818/)), linking MRD30 to the KMT2A/COMPASS chromatin-modifier network implicated in neurodevelopmental disorders.

### Causal chain (upstream → downstream)

```
ZMYND11 haploinsufficiency (heterozygous LoF / 10p15.3 deletion)
        │
        ▼
Reduced reading of H3.3K36me3 on gene bodies & promoters
        │
        ├─► Impaired Pol II elongation control + reduced Pol II pausing (initiation)
        ├─► Loss of EFTUD2 antagonism → aberrant intron retention / mis-splicing
        ├─► Disrupted RBFOX2-dependent brain-specific isoform switch
        └─► Loss of restraint on KMT2A → de-repression of latent developmental genes
        │
        ▼
Cortical neural stem cells activate inappropriate developmental programs
        │
        ▼
Impaired cortical progenitor & neuron production (disrupted corticogenesis)
        │
        ▼
Intellectual disability, developmental delay, seizures, behavioral problems
```

**Cell types & compartments:** neural stem/progenitor cells and cortical neurons (**CL:0000047** neural stem cell; **CL:0000679** glutamatergic neuron); subcellular localization is the **nucleus/chromatin** (**GO:0005634** nucleus; **GO:0000785** chromatin).

**Suggested GO biological processes:** GO:0006357 (regulation of transcription by RNA Pol II), GO:0008380 (RNA splicing), GO:0006397 (mRNA processing), GO:0021987 (cerebral cortex development), GO:0022008 (neurogenesis).

**Immune, metabolic, oxidative-stress mechanisms:** Not central to MRD30 pathophysiology. (Co-deleted *DIP2C* perturbs sphingolipid metabolism/myelination in the deletion syndrome — Section 10 — but this is not ZMYND11-intrinsic.)

---

## 7. Anatomical Structures Affected

**Primary organ / system (F005, F010):** the **brain / central nervous system** (nervous system) — specifically the developing **cerebral cortex** (**UBERON:0000955** brain; **UBERON:0000956** cerebral cortex).

**Tissue and cell level:** nervous tissue; neural stem/progenitor cells and cortical neurons (**CL:0000047**, **CL:0000679**).

**Subcellular level:** nucleus and chromatin (**GO:0005634**, **GO:0000785**).

**Secondary / contiguous-deletion involvement (F010):** In larger 10p15.3 deletions, additional organs are affected because neighboring genes are co-deleted — **heart** (congenital heart defects, via *DIP2C*), **kidney**, **parathyroid** (hypoparathyroidism, via *GATA3*/DGS2), **skeleton** (short stature, hand/foot malformation, butterfly vertebrae, scoliosis), **inner ear** (sensorineural deafness), and rarely the **GI tract** (refractory gastroparesis). Some patients show cerebellar/posterior-fossa malformations (ring chromosome 10 cases).

> *"Recurrent 10p15.3 microdeletion syndrome is a rare multisystem disorder characterized by abnormal facial features, global developmental delay (DD)/intellectual disability (ID), short stature, hand/foot malformation, and congenital heart defects (CHDs)"* ([PMID: 40915331](https://pubmed.ncbi.nlm.nih.gov/40915331/))

**Lateralization:** CNS involvement is bilateral/diffuse (a developmental, not focal-lesion, disorder), though focal epileptiform (e.g., centrotemporal) EEG features occur.

---

## 8. Temporal Development

**Onset (F011):** Congenital to early childhood — neonatal hypotonia and infantile developmental delay are typical; onset pattern is **chronic/insidious**, not acute.

**Progression (F011):** The disorder is **chronic and lifelong** and the neurodevelopmental deficit is **largely static (non-neurodegenerative)** rather than progressive. Neurodevelopmental deficits are essentially invariable (fully penetrant).

> *"Seizure prognosis ranged from spontaneous remission to drug resistant. Neurodevelopmental deficits were invariable."* ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/))

**Course patterns / adult evolution (F011):** Epilepsy course is variable (episodic/remitting to drug-resistant). A distinct subset develops or worsens a **movement disorder (dystonia/ataxia/tremor) in adulthood**, prompting adult neurological referral and underscoring the need for lifelong surveillance.

> *"displayed a movement disorder (dystonia/ataxia/tremor) which manifested for the first time, or worsened, in the adulthood"* ([PMID: 35172867](https://pubmed.ncbi.nlm.nih.gov/35172867/))

**Critical periods:** Cortical neurogenesis (fetal/early-postnatal) is the key vulnerable window, consistent with the corticogenesis defect and congenital onset (F005). Prenatal presentations are nonspecific (Section 10).

---

## 9. Inheritance and Population

**Epidemiology (F013):** MRD30 is **ultra-rare**; only on the order of dozens of individuals are reported worldwide (e.g., a 2021 study assembled 20 individuals with epilepsy). **No population prevalence or incidence estimate is established.**

**Inheritance (F008, F013):** **Autosomal dominant.** Pathogenic variants mostly arise **de novo**; rare inherited cases from mildly/variably affected parents demonstrate **incomplete penetrance and variable expressivity**.

> *"Variants were distributed across the gene and mostly de novo with no precise genotype-phenotype correlation."* ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/))
> *"Parental CMA analysis revealed that the 10p15.3 microdeletion was inherited from the father, who displayed mild language impairment"* ([PMID: 39696561](https://pubmed.ncbi.nlm.nih.gov/39696561/))

**Penetrance / expressivity:** Neurodevelopmental deficits are near-fully penetrant; dysmorphism, epilepsy, and additional features are variably expressed. Germline mosaicism is plausible for de novo cases but not specifically quantified.

**Founder effects / consanguinity / carrier frequency:** No founder effect described; consanguinity is not relevant (dominant, mostly de novo). Carrier frequency in the healthy population is effectively negligible given strong LoF constraint (gnomAD).

**Demographics (F013):** Reported in **both sexes with no clear sex predilection** and across diverse populations; no ethnic or geographic clustering is established.

---

## 10. Diagnostics

**Recommended approach (F008).** Diagnosis is **molecular**. Point/truncating *ZMYND11* variants are detected by **whole-exome or whole-genome sequencing** or by **epilepsy/intellectual-disability gene panels**, with variants classified per **ACMG/AMP** criteria. 10p15.3 deletions are detected by **chromosomal microarray analysis (CMA)**, **karyotyping**, and **FISH**; prenatally by amniocentesis + CMA.

> *"Genetic evaluation was performed using gene panels or exome sequencing; variants were classified using American College of Medical Genetics (ACMG) criteria"* ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/))

| Test | Utility in MRD30 |
|---|---|
| WES / WGS | High — detects intragenic point/truncating variants (first-line for ID/epilepsy) |
| Epilepsy/ID gene panels | High — targeted detection of *ZMYND11* variants |
| Chromosomal microarray (CMA) | Detects 10p15.3 deletions and contiguous-gene involvement |
| Karyotype / FISH | Detects ring chr10, inv dup del(10p), translocations involving 10p |
| Prenatal (amniocentesis + CMA) | Detects deletions; correlate with ultrasound |

**Prenatal / fetal features (F008).** Nonspecific: increased **nuchal translucency** (first trimester), **fetal growth restriction** (third trimester), and skeletal anomalies (butterfly vertebrae, scoliosis).

> *"Two cases were diagnosed in the first trimester because of increased nuchal translucency (NT). Three had normal routine first-trimester and second-trimester ultrasound scans, and were diagnosed because of fetal growth restriction (FGR)"* ([PMID: 42362275](https://pubmed.ncbi.nlm.nih.gov/42362275/))

**Ancillary tests.** EEG (for epilepsy classification, including centrotemporal/ABPE patterns), brain MRI (may show cerebellar/posterior-fossa anomalies in some deletion/ring-chromosome cases), and audiology/ophthalmology assessments for hearing loss and strabismus. No specific blood/urine biomarker or enzyme assay exists.

**Differential diagnosis.** Angelman syndrome (happy disposition, ataxic gait, hypotonia — overlap noted in individual reports; [PMID: 27626064](https://pubmed.ncbi.nlm.nih.gov/27626064/)), other chromatinopathies including Cornelia de Lange-like presentations ([PMID: 42003802](https://pubmed.ncbi.nlm.nih.gov/42003802/)), and — for contiguous deletions — HDR/Barakat syndrome (via *GATA3*) and DiGeorge-region disorders.

**Distinguishing pure MRD30 from the contiguous-deletion syndrome (F010).** Pure *ZMYND11* disruption (point variants or small intragenic deletions) causes the **core neurodevelopmental phenotype only**. Larger deletions add features from co-deleted neighbors: *DIP2C* (congenital heart defects, short stature, hand/foot malformation, abnormal myelination/sphingolipid metabolism) and, for larger terminal deletions, *GATA3* + DiGeorge critical region 2 (DGS2) → **hypoparathyroidism, sensorineural deafness, renal abnormalities** (HDR/Barakat-like).

> *"We identified Disco Interacting Protein 2 Homolog C (DIP2C) as a putative candidate gene underlying CHDs"* ([PMID: 40915331](https://pubmed.ncbi.nlm.nih.gov/40915331/))
> *"includes the ZMYND11 and GATA3 genes and a partial critical region of the DiGeorge syndrome 2 gene (DGS2)"* ([PMID: 34049562](https://pubmed.ncbi.nlm.nih.gov/34049562/))

**Screening / cascade testing.** Once a familial variant is identified, targeted cascade testing of at-risk relatives is appropriate given documented inherited/variably expressed cases. No population newborn screening exists.

---

## 11. Outcome / Prognosis

**Survival / mortality (F011).** MRD30 is **not associated with reduced life expectancy** in the reported literature; it is a static neurodevelopmental disorder rather than a lethal or neurodegenerative one. No disease-specific mortality rate is established.

**Morbidity / function.** The principal burden is **lifelong intellectual disability and developmental disability**, with communication impairment, behavioral difficulties (ASD/ADHD/aggression), and — in a subset — epilepsy and adult movement disorders contributing to functional impairment and caregiver dependence. Formal disability/QoL metrics (ICF, EQ-5D, PROMIS) have not been reported for this rare disorder.

**Disease course / complications.** Complications include drug-resistant epilepsy (subset), adult-onset/worsening movement disorder, sensorineural hearing loss, and — in contiguous deletions — cardiac, renal, endocrine, and GI complications. Recovery to normal cognition does not occur; developmental gains are achievable with early intervention.

**Prognostic factors (F006, F011).** Variant class appears prognostically relevant: missense variants (e.g., p.Arg600Trp) associate with **more severe intellectual disability, strabismus, and hypotonia**. Seizure severity/drug-resistance and the presence of contiguous-gene deletions also influence prognosis. No validated molecular prognostic biomarker exists.

---

## 12. Treatment

**No disease-specific or curative therapy exists (F012).** Management is **symptomatic and multidisciplinary**, following general neurodevelopmental-disorder care:

| Domain | Intervention | Suggested NCIT concept |
|---|---|---|
| Epilepsy | Antiseizure medications (ASMs); recognize drug-resistant subset | NCIT:C264 (Anticonvulsant Agent) |
| Development | Early developmental intervention | NCIT:C15275 (Rehabilitation Therapy) |
| Motor / hypotonia | Physical & occupational therapy | NCIT:C15242 / NCIT:C15226 |
| Speech / language | Speech-language therapy | NCIT:C15275 |
| Behavior (ASD/ADHD/aggression) | Behavioral & educational support | NCIT:C15319 (Behavioral Therapy) |
| Sensory | Vision (strabismus) & hearing surveillance/treatment | — |
| Contiguous deletions | Cardiac, renal, parathyroid/endocrine, skeletal evaluation & management | — |

> *"Seizure prognosis ranged from spontaneous remission to drug resistant."* ([PMID: 34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/)) — justifies individualized antiseizure management including recognition of drug-resistant epilepsy.

**Emerging / experimental directions (F012).** Cellular studies indicate that defects seen in ZMYND11-deficient and related chromatin-ASD-gene models can be **partially rescued by enhancing ZMYND11 function**, hinting at future targeted approaches — but nothing is clinically available.

> *"Similar defects are observed in other chromatin-related ASD risk genes, some of which are partially rescued by enhancing ZMYND11 function"* ([PMID: 41068108](https://pubmed.ncbi.nlm.nih.gov/41068108/))

**Pharmacogenomics / gene / cell / RNA therapy:** No approved targeted, gene-, cell-, or RNA-based therapy; no MRD30-specific pharmacogenomic guidance. There are no registered disease-specific interventional trials at the time of this review.

---

## 13. Prevention

Because MRD30 is a monogenic disorder with no environmental component, prevention is limited to **genetic risk management** (F013, F014):

- **Primary prevention:** Not applicable in the classical sense (no modifiable environmental risk). For families with a known variant, **genetic counseling, prenatal diagnosis, and preimplantation genetic testing (PGT)** can inform reproductive decisions.
- **Secondary prevention:** Early molecular diagnosis (WES/WGS/CMA) enables early developmental intervention and surveillance for epilepsy, hearing, and vision problems.
- **Tertiary prevention:** Proactive management of complications — antiseizure therapy, adult neurological surveillance for movement disorders, and organ-specific monitoring in contiguous-deletion cases.
- **Genetic counseling:** Given that most variants are de novo but inherited/variably expressed cases occur, recurrence-risk counseling should account for **variable expressivity, incomplete penetrance, and possible parental mosaicism**; cascade testing follows identification of a familial variant.

No immunization, behavioral, or public-health/environmental prevention is applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (F009):** *ZMYND11* is evolutionarily conserved; functional orthologs are studied in **mouse** (*Zmynd11*) and **zebrafish** (*bs69*/*zmynd11*). Human gene NCBI Gene 10778.
- **Natural disease in animals:** No naturally occurring companion-animal or wildlife disease is described (OMIA has no established entry for a natural ZMYND11 disorder). This is a research-modeled, not a naturally recognized veterinary, condition.
- **Comparative biology:** Disease mechanisms (H3.3K36me3 reading, transcription/splicing control, developmental-signaling regulation) are conserved. In zebrafish, **Mga modulates Bmpr1a activity by antagonizing Bs69**, providing an in-vivo developmental-signaling (BMP) context ([PMID: 30324105](https://pubmed.ncbi.nlm.nih.gov/30324105/)).
- **Transmission / zoonosis:** Not applicable (genetic disorder).

---

## 15. Model Organisms

**Available models (F009):**

| System | Model | Key finding | PMID |
|---|---|---|---|
| Human iPSC / cortical organoid | *ZMYND11*-deficient cortical NSCs | Impaired progenitor/neuron production; de-repressed latent genes; RBFOX2 splicing switch | [41068108](https://pubmed.ncbi.nlm.nih.gov/41068108/) |
| Mouse ESC / MEF | *Zmynd11* deficiency | Impaired transcription initiation; reduced Pol II pausing index | [42262664](https://pubmed.ncbi.nlm.nih.gov/42262664/) |
| Zebrafish | *bs69* (Mga–Bmpr1a axis) | In-vivo BMP developmental-signaling model | [30324105](https://pubmed.ncbi.nlm.nih.gov/30324105/) |
| Mouse (neighboring *Dip2c*) | Het/hom *Dip2c* mutants | Dosage-sensitive cognitive impairment, hyperlocomotion, abnormal sphingolipid metabolism/myelination | [41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/) |
| Zebrafish (neighboring *dip2ca*) | *dip2ca* knockdown | Craniofacial and cardiac defects | [40915331](https://pubmed.ncbi.nlm.nih.gov/40915331/) |

> *"heterozygous mutant mice displayed only mild cognitive impairment, recapitulating the dosage-sensitive phenotype observed in human 10p15.3 microdeletion syndrome"* ([PMID: 41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/)) — dosage-sensitive model for the neighboring 10p15.3 gene *DIP2C*.

**Phenotype recapitulation & limitations.** Human iPSC/cortical-organoid models faithfully reproduce the **corticogenesis defect** and molecular signatures (latent-gene de-repression, RBFOX2 splicing) and are the most disease-relevant system. Mouse ESC/MEF models capture the transcription/chromatin mechanism. **Limitations:** no published constitutive *Zmynd11* knockout mouse fully modeling the MRD30 behavioral/seizure phenotype was identified; zebrafish/mouse *Dip2c* models inform the contiguous-deletion (not pure-*ZMYND11*) phenotype. **Genetic-model types available:** cellular knockout/deficiency and organoid systems; a humanized or conditional neuronal knockout mouse would be a valuable addition.

**Applications & resources:** Cortical organoids for mechanism and drug-rescue screening; ESC/MEF for chromatin/transcription assays; zebrafish for developmental signaling. Resources: MGI (*Zmynd11*), ZFIN (*bs69*/*zmynd11*), Cellosaurus (patient iPSC lines).

---

## Mechanistic Model / Interpretation

MRD30 is best understood as a **chromatinopathy of transcriptional–splicing coupling in the developing cortex**. A single functional dose of *ZMYND11* is insufficient for normal reading of the H3.3K36me3 mark deposited on active gene bodies. The immediate consequence is dysregulated RNA Pol II behavior (elongation control plus initiation/pausing) and loss of the ZMYND11–EFTUD2 balance that governs intron retention. Layered on top, ZMYND11 normally **restrains KMT2A** and enforces a **brain-specific RBFOX2 isoform switch**. When ZMYND11 is halved, latent developmental gene programs are inappropriately activated, cortical neural stem cells fail to execute proper neurogenesis, and the mature cortex is built from too few, mis-specified neurons — producing intellectual disability, developmental delay, epilepsy, and behavioral phenotypes. Because the insult is developmental and completed early, the clinical disorder is **static rather than degenerative**, explaining its lifelong-but-stable natural history (with a distinct adult movement-disorder subset).

Two "concentric" clinical entities emerge from the same locus:

```
  ┌──────────────────────── 10p15.3 deletion (large terminal) ─────────────────────┐
  │  + GATA3/DGS2  → hypoparathyroidism, deafness, renal (HDR/Barakat-like)         │
  │  ┌──────────────── 10p15.3 microdeletion (recurrent) ─────────────────────┐     │
  │  │  + DIP2C → CHD, short stature, hand/foot malformation, myelination      │     │
  │  │  ┌──────────── Pure ZMYND11 loss = MRD30 (core) ───────────────┐        │     │
  │  │  │  ID/DD, hypotonia, seizures, dysmorphism, behavior           │        │     │
  │  │  └──────────────────────────────────────────────────────────────┘        │     │
  │  └──────────────────────────────────────────────────────────────────────────┘     │
  └──────────────────────────────────────────────────────────────────────────────────┘
```

This nested model is the single most clinically actionable synthesis: the **size and gene content of the lesion predict which additional organ systems require evaluation**, while the ZMYND11 core drives the neurodevelopmental phenotype in every case.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [34818214](https://pubmed.ncbi.nlm.nih.gov/34818214/) | Intragenic *ZMYND11* deletion / DD | **Confirms haploinsufficiency mechanism**; deletion–truncating phenotypic equivalence |
| [34216016](https://pubmed.ncbi.nlm.nih.gov/34216016/) | *ZMYND11* epilepsies + NDD (cohort ~20) | Critical-gene status; epilepsy subtypes; de novo predominance; diagnostic methods; penetrance |
| [25263594](https://pubmed.ncbi.nlm.nih.gov/25263594/) | BS69/ZMYND11 reads H3.3K36me3, regulates splicing | Domain architecture; H3.3K36me3 reader; EFTUD2/intron-retention |
| [25453099](https://pubmed.ncbi.nlm.nih.gov/25453099/) | Histone H3.3 and cancer reader connection | Reader specificity; tumor-suppressor context |
| [42262664](https://pubmed.ncbi.nlm.nih.gov/42262664/) | ZMYND11 at promoters / initiation | Transcription initiation & Pol II pausing role |
| [41068108](https://pubmed.ncbi.nlm.nih.gov/41068108/) | ZMYND11 safeguards corticogenesis | Corticogenesis defect; latent-gene de-repression; RBFOX2; partial rescue |
| [41279818](https://pubmed.ncbi.nlm.nih.gov/41279818/) | ZMYND11 restrains KMT2A | KMT2A restraint enabling neuronal program |
| [41820311](https://pubmed.ncbi.nlm.nih.gov/41820311/) | p.Arg600Trp / missense phenotype | Missense-vs-LoF genotype–phenotype |
| [42003802](https://pubmed.ncbi.nlm.nih.gov/42003802/) | 7p dup + 10p del chromatinopathy | Dosage sensitivity; CdLS-like overlap |
| [27626064](https://pubmed.ncbi.nlm.nih.gov/27626064/) | De novo missense; DD/seizures/hypotonia | Individual multisystem phenotype; Angelman-like features |
| [35172867](https://pubmed.ncbi.nlm.nih.gov/35172867/) | NDD in adulthood — movement disorder | Adult-onset/worsening movement disorder |
| [39696561](https://pubmed.ncbi.nlm.nih.gov/39696561/) | Prenatal pure 10p15.3 deletion | Inherited case, variable expressivity |
| [42362275](https://pubmed.ncbi.nlm.nih.gov/42362275/) | Prenatal 10p15.3 (5 cases) | Nonspecific prenatal features (NT, FGR) |
| [40915331](https://pubmed.ncbi.nlm.nih.gov/40915331/) | DIP2C and CHD in 10p15.3 | Attributes CHD to co-deleted *DIP2C* |
| [41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/) | *Dip2c* deficiency / sphingolipids in mice | Dosage-sensitive mouse model (neighboring gene) |
| [34049562](https://pubmed.ncbi.nlm.nih.gov/34049562/) | Large 10p15.3p13 deletion | *GATA3*/DGS2 co-deletion adds endocrine/renal/hearing features |
| [30324105](https://pubmed.ncbi.nlm.nih.gov/30324105/) | Mga–Bmpr1a–Bs69 in zebrafish | Zebrafish developmental-signaling model |
| [40753099](https://pubmed.ncbi.nlm.nih.gov/40753099/) | Schizophrenia exome risk genes | *ZMYND11* LoF as FDR-significant SCZ risk gene |

**Evidence source types:** human clinical (case reports/small cohorts), in vitro/iPSC (human cortical organoids), model organism (mouse ESC/MEF, zebrafish), and computational/genetic (exome burden). No population EHR or randomized-trial evidence exists for this ultra-rare disorder.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** All clinical knowledge derives from case reports and small cohorts (dozens of patients). No prevalence/incidence estimate, no natural-history registry, and no controlled trials exist.
2. **No population-scale or QoL data.** Formal disability, EQ-5D/SF-36/PROMIS, and long-term functional-outcome metrics are unreported.
3. **Genotype–phenotype resolution is coarse.** Missense-vs-LoF differences are suggested from aggregate analysis of only ~13 missense variants; larger, systematically phenotyped cohorts are needed.
4. **No definitive disease-specific episignature** or biomarker has been validated, despite ZMYND11's chromatin role.
5. **Model gap.** No published constitutive/conditional *Zmynd11*-knockout mouse fully recapitulating the MRD30 behavioral/seizure phenotype was identified; much mouse evidence pertains to the neighboring gene *DIP2C*.
6. **Contiguous-gene confounding.** Deletion-based literature mixes *ZMYND11* effects with those of *DIP2C*, *GATA3*, and DGS2, complicating attribution — mitigated only by pure-variant/intragenic-deletion cases.
7. **No therapeutics.** Rescue-by-enhancement is a cellular observation only, with no translational pathway yet.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble an international MRD30 registry** with standardized deep phenotyping (HPO-coded), variant-class stratification, and longitudinal follow-up to establish penetrance, expressivity, and prognostic factors quantitatively.
2. **Systematic genotype–phenotype study** contrasting LoF vs. missense (especially recurrent p.Arg600Trp) with functional assays of reader capacity, EFTUD2 antagonism, and KMT2A restraint.
3. **Test for a DNA-methylation episignature** in patient blood to enable a diagnostic biomarker and VUS reclassification.
4. **Generate a conditional neuronal *Zmynd11* mouse** (and validate against patient cortical organoids) to model behavior, seizures, and to serve as a preclinical rescue platform.
5. **Mechanistic dissection of the RBFOX2 splicing switch and KMT2A axis** in patient neurons, with multi-omics (RNA-seq intron-retention analysis, CUT&RUN for H3.3K36me3/ZMYND11, Pol II ChIP).
6. **Pursue "enhance-ZMYND11-function" or downstream-node therapeutic screens** (e.g., modulating KMT2A/COMPASS activity or splicing) in cortical organoids to identify actionable targets.
7. **Standardize clinical care pathways** distinguishing pure MRD30 from contiguous-deletion syndrome, specifying which patients need cardiac (*DIP2C*), renal/parathyroid/audiologic (*GATA3*/DGS2) evaluation, and lifelong adult neurological surveillance for movement disorders.

---

*Report compiled from 14 confirmed findings across 5 investigation iterations and 28 reviewed publications. Ontology suggestions provided for MONDO, HPO, GO, CL, UBERON, and NCIT to support knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Intellectual_Disability_Autosomal_Dominant_30-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Disability_Autosomal_Dominant_30-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.