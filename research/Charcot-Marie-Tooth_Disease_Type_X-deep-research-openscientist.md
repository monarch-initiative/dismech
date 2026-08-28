---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-27T15:41:10.320367'
end_time: '2026-08-27T15:58:03.157560'
duration_seconds: 1012.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Type X
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 21
  off_topic: 2
  off_topic_references:
  - PMID:9722620
  - PMID:10586239
  needs_review: true
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Charcot-Marie-Tooth_Disease_Type_X-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Charcot-Marie-Tooth_Disease_Type_X-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Type X
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Type X** covering all of the
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

# Charcot-Marie-Tooth Disease Type X (CMTX): Comprehensive Disease Characterization Report

**Report type:** Disease knowledge-base entry — aggregated disease-level synthesis of primary literature and reference databases.
**Primary evidence base:** Human clinical cohorts and case series, mouse models, and in vitro cell studies (PMIDs cited throughout).

---

## Summary

Charcot-Marie-Tooth disease type X (**CMTX**) is an X-linked form of inherited peripheral neuropathy. Its dominant and prototypical subtype, **CMTX1**, is caused by mutations in **GJB1**, the gene encoding the gap-junction protein **connexin-32 (Cx32)**, expressed by myelinating Schwann cells peripherally and by oligodendrocytes centrally. CMTX1 is the **second most common form of CMT** overall (after CMT1A/*PMP22* duplication), accounting for roughly 7–16% of genetically diagnosed cases in most cohorts. It presents as a slowly progressive, length-dependent sensorimotor polyneuropathy with distal weakness, atrophy, sensory loss, pes cavus, and areflexia, typically beginning in the first two decades ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/), [PMID: 35383424](https://pubmed.ncbi.nlm.nih.gov/35383424/)).

Because the disorder is X-linked, **hemizygous males are affected more severely than heterozygous females**, and there is characteristically **no male-to-male transmission**—a key pedigree clue. Electrophysiology shows **"intermediate" nerve conduction velocities** (~25–45 m/s in males), distinguishing CMTX1 from uniformly slowed CMT1A and normal-velocity axonal CMT2 ([PMID: 15468313](https://pubmed.ncbi.nlm.nih.gov/15468313/), [PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)). Mechanistically, loss of Cx32 abolishes the **reflexive gap junctions** that provide a radial diffusion pathway across the myelin sheath—approximately one million times faster than the circumferential route—leading to **early axonal transport and cytoskeletal defects that precede demyelination** ([PMID: 9722620](https://pubmed.ncbi.nlm.nih.gov/9722620/), [PMID: 20720503](https://pubmed.ncbi.nlm.nih.gov/20720503/)). Because Cx32 is also expressed centrally, a minority of patients experience transient, reversible **CNS "stroke-like" episodes**, and CMTX carries an increased frequency of CNS demyelination/multiple sclerosis ([PMID: 12111842](https://pubmed.ncbi.nlm.nih.gov/12111842/), [PMID: 30196252](https://pubmed.ncbi.nlm.nih.gov/30196252/)).

Life expectancy in CMTX1 is normal, and management is presently **supportive** (physiotherapy, orthotics, foot-deformity correction, pain management). No disease-modifying therapy is approved, but **AAV9-mediated, Schwann-cell-targeted GJB1 gene replacement** rescues the *Gjb1*-null mouse both before and after symptom onset and is the leading emerging strategy; **serum neurofilament light chain (NfL)** is a promising circulating biomarker of the axonal injury underlying disability ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/), [PMID: 42017539](https://pubmed.ncbi.nlm.nih.gov/42017539/), [PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)). The term "CMTX" is genetically heterogeneous: beyond CMTX1 (*GJB1*), rarer subtypes include **CMTX4/Cowchock syndrome** (*AIFM1*), **CMTX5** (*PRPS1*), and others ([PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/)).

---

## Key Findings

### 1. CMTX1 is caused by GJB1/connexin-32 mutations and is the second most common form of CMT
Multiple large cohorts confirm *GJB1* (connexin-32) as the causal gene for the dominant X-linked subtype (CMTX1). The largest natural-history study (387 patients / 295 families) states: *"Charcot-Marie-Tooth disease (CMT) due to GJB1 variants (CMTX1) is the second most common form of CMT. It is an X-linked disorder characterized by progressive sensory and motor neuropathy with males affected more severely than females"* ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)). That study reported **154 distinct GJB1 variants**, of which **82.4% were pathogenic/likely pathogenic**.

### 2. X-linked inheritance with males more severely affected than females
Panosyan et al. (87 males mean age 41; 73 females mean age 46) found: *"Sensory-motor polyneuropathy affects both sexes, more severely in males than in females, and there was a strong correlation between age and disease burden in males but not in females"* ([PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)). Record et al. confirmed males (166/319, 52%) were more severely affected at baseline ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)).

### 3. Axonal degeneration precedes demyelination
In *Gjb1*-null mice studied at 2–4 months (minimal demyelination), *"axonal abnormalities including impaired cytoskeletal organization and defects in axonal transport precede demyelination in this mouse model of CMT1X"*—with reduced large-axon diameters, neurofilament dephosphorylation, increased β-amyloid precursor protein (an axonal-damage marker), and slowed fast axonal transport ([PMID: 20720503](https://pubmed.ncbi.nlm.nih.gov/20720503/)). This establishes the temporal causal chain: axonal dysfunction is **upstream** of demyelination.

### 4. CNS involvement and transient "stroke-like" episodes are a recognized feature
Cx32 is expressed by both Schwann cells and oligodendrocytes. CNS-phenotype mutants *"failed to reach the cell membrane and were instead retained in the endoplasmic reticulum (A39V, T55I) or Golgi apparatus (M93V, R164Q, R183H)"* ([PMID: 12111842](https://pubmed.ncbi.nlm.nih.gov/12111842/)). Multiple case reports document transient stroke-like episodes with reversible corpus-callosum-splenium DWI lesions, triggered by fever, infection, exercise, altitude, or allergen exposure, resolving within hours to days ([PMID: 30952033](https://pubmed.ncbi.nlm.nih.gov/30952033/), [PMID: 42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/)).

### 5. AAV9-mediated Schwann-cell-targeted GJB1 gene therapy rescues CMT1X in mice
Kagiava et al. delivered *GJB1*/Cx32 under the *Mpz* promoter intrathecally in *Gjb1*-null mice; a pre- and post-onset trial *"demonstrated improved motor performance and sciatic nerve conduction velocities along with improved myelination and reduced inflammation in peripheral nerve tissues,"* with *"Blood biomarker levels… also significantly ameliorated"* ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)). Current management remains supportive: *"Symptomatic management is still the only option, but many therapeutic approaches are under investigation"* ([PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)).

### 6. Core clinical phenotype: adolescent-onset distal weakness, atrophy, sensory loss, foot deformity
Yalcouyé et al. (Mali cohort): *"Neurological examination found a distal muscle weakness and atrophy, and sensory loss, skeletal deformities, decreased or absent reflexes and steppage gait"* ([PMID: 35383424](https://pubmed.ncbi.nlm.nih.gov/35383424/)). Chen et al. documented a *"median age of onset of 16.5 years (range: 13–30)"* ([PMID: 31323543](https://pubmed.ncbi.nlm.nih.gov/31323543/)). Occasional sensorineural hearing loss occurs in a variant-dependent manner ([PMID: 12542510](https://pubmed.ncbi.nlm.nih.gov/12542510/)).

### 7. Female phenotypic variability is NOT explained by skewed X-inactivation
Bekircan-Kurt et al. analyzed X-chromosome inactivation via HUMARA in archived sural-nerve biopsies from two female CMTX1 patients (previously misdiagnosed as CIDP): *"our findings suggest that XCI does not contribute to phenotypic variability in female CMTX1 patients"* ([PMID: 40759929](https://pubmed.ncbi.nlm.nih.gov/40759929/)). This refutes a long-standing hypothesis.

### 8. Intermediate conduction velocities and no male-to-male transmission are key diagnostic clues
Vondracek et al.: *"All patients having the CMT phenotype and intermediate conduction velocities who are negative for CMT1A duplication/hereditary neuropathy with liability to pressure palsies (HNPP) deletion, and whose family shows a dominant trait without male-to-male transmission, should be screened for CMTX1"* ([PMID: 15468313](https://pubmed.ncbi.nlm.nih.gov/15468313/)).

### 9. Epidemiology: CMT ~1/2,500; GJB1 ~7–16% (second most common)
Milley et al. (Hungary): *"alterations were most frequently found in PMP22 (40.5%), followed by GJB1 (9.2%)"* ([PMID: 29174527](https://pubmed.ncbi.nlm.nih.gov/29174527/)). Corroborated by Bashkortostan (13.7%) and Southern Italy cohorts ([PMID: 19062535](https://pubmed.ncbi.nlm.nih.gov/19062535/), [PMID: 25429913](https://pubmed.ncbi.nlm.nih.gov/25429913/)).

### 10. Cx32 forms reflexive gap junctions providing a ~million-fold faster radial diffusion pathway
Balice-Gordon, Bone & Scherer: *"a gap junction-mediated radial pathway may be essential for rapid diffusion between the adaxonal and perinuclear cytoplasm, since this radial pathway is approximately one million times faster than the circumferential pathway"* ([PMID: 9722620](https://pubmed.ncbi.nlm.nih.gov/9722620/)). Scherer's review confirms: *"Reflexive gap junctions, comprising connexin32 and at least one other connexin protein, form a radial pathway for the diffusion of ions and small molecules directly across the myelin sheath"* ([PMID: 10586239](https://pubmed.ncbi.nlm.nih.gov/10586239/)).

### 11. "CMTX" is genetically heterogeneous
Beyond CMTX1 (~90% of X-linked CMT), rarer subtypes exist. Rinaldi et al.: *"Cowchock syndrome (CMTX4) is a slowly progressive X-linked recessive disorder with axonal neuropathy, deafness, and cognitive impairment"* caused by *AIFM1* variants ([PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/), [PMID: 26173962](https://pubmed.ncbi.nlm.nih.gov/26173962/)). Others: CMTX5 (*PRPS1*), CMTX2/3, CMTX6 (*PDK3*).

### 12. CMTX is associated with increased CNS inflammatory demyelination / MS
Koutsis et al. (70 CMTX patients over 20 years): *"The resulting 20-year MS incidence (4.3%) differed significantly from the highest background 20-year MS incidence ever reported from Greece (p=0.00039)"*; 10/18 cases had splenium hyperintensity vs 0 controls (p=0.0002) ([PMID: 30196252](https://pubmed.ncbi.nlm.nih.gov/30196252/)).

### 13. Natural history: slow progression quantified by CMTES; c.-17G>A has a distinct milder phenotype
Record et al. used the CMT Examination Score (CMTES) for longitudinal tracking. *"Baseline measures in patients with P/LP variants and VUS showed no significant differences, and regression analysis suggested the disease groups were near identical at baseline"*, and genotype analysis *"suggested c.-17G>A produces"* a distinct milder phenotype ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)).

### 14. Serum NfL is an emerging circulating biomarker of axonal injury
In the *Gjb1*-null model, gene therapy significantly ameliorated blood NfL alongside functional/histological rescue ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)). In human CMT-spectrum carriers, *"All carriers exhibited elevated serum NfL"* ([PMID: 42017539](https://pubmed.ncbi.nlm.nih.gov/42017539/)).

---

## Mechanistic Model / Interpretation

CMTX1 is best understood as a **Schwann-cell-autonomous defect that becomes a functional axonopathy**. Loss or mistrafficking of connexin-32 removes the reflexive gap junctions that create a radial "shortcut" for ions and metabolites across the myelin sheath—a pathway ~10⁶-fold faster than diffusion around the myelin spiral ([PMID: 9722620](https://pubmed.ncbi.nlm.nih.gov/9722620/)). The immediate consequence is **failure of adaxonal homeostasis**, producing cytoskeletal disorganization and slowed axonal transport **before** myelin breaks down ([PMID: 20720503](https://pubmed.ncbi.nlm.nih.gov/20720503/)). Over years, demyelination and secondary **axonal degeneration** accumulate distally, generating the length-dependent clinical picture; serum NfL is the circulating footprint of that axonal loss.

Two features flow from Cx32's dual expression and X-linkage. First, **oligodendrocyte** Cx32 loss makes central myelin metabolically fragile, so stressors (fever, exercise, altitude, allergen exposure) can precipitate **reversible** CNS lesions, and CMTX carries excess CNS demyelination/MS ([PMID: 12111842](https://pubmed.ncbi.nlm.nih.gov/12111842/), [PMID: 30196252](https://pubmed.ncbi.nlm.nih.gov/30196252/)). Second, **X-linkage** dictates that hemizygous males are uniformly and more severely affected while heterozygous females are variable—variability that is **not** explained by skewed X-inactivation ([PMID: 40759929](https://pubmed.ncbi.nlm.nih.gov/40759929/)). The predominantly loss-of-function nature of the disease is exactly why **gene replacement** is compelling: restoring Schwann-cell Cx32 improves function, conduction, myelination, and biomarkers in vivo, both before and after onset ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)).

```
 GJB1 mutation (hemizygous male / heterozygous female)
        │
        ▼
 Loss / mistrafficking of Connexin-32
        │
        ├──────────► Oligodendrocytes (CNS): stress-triggered reversible
        │            white-matter dysfunction ("stroke-like episodes"); ↑MS risk
        ▼
 Loss of reflexive gap junctions in Schwann cells
 (Schmidt-Lanterman incisures, paranodes)
        │
        ▼
 Loss of fast radial diffusion pathway (~10^6× faster than circumferential)
        │
        ▼
 Impaired adaxonal ion/metabolite homeostasis
        │
        ▼
 EARLY: axonal cytoskeletal disorganization + slowed axonal transport
        │  (neurofilament dephosphorylation, ↑β-APP)
        ▼
 LATER: demyelination  →  secondary axonal degeneration
        │
        ▼
 Length-dependent distal weakness, atrophy, sensory loss, areflexia
```

---

# Full Disease Characterization (15 Sections)

## 1. Disease Information

**Overview.** CMTX is a group of X-linked inherited peripheral neuropathies; the most common and prototypical form is **CMTX1**, caused by pathogenic variants in **GJB1** (connexin-32/Cx32). It is a **progressive length-dependent sensorimotor polyneuropathy** with mixed demyelinating and axonal ("intermediate") features, in which **males are affected more severely than females**, and is the **second most common form of CMT overall** after CMT1A ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/), [PMID: 29174527](https://pubmed.ncbi.nlm.nih.gov/29174527/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | **302800** (CMTX1); gene *GJB1* **304040** |
| Orphanet | ORPHA:101075 (CMT, X-linked / CMTX1) |
| MONDO | **MONDO:0010674** |
| ICD-10 / ICD-11 | G60.0 / 8C20 (hereditary motor and sensory neuropathy) |
| MeSH | D002607 (Charcot-Marie-Tooth Disease) |
| HGNC / UniProt / NCBI Gene / Ensembl | HGNC:4283 / P08034 / 2705 / ENSG00000169562 |

**Synonyms.** X-linked Charcot-Marie-Tooth disease type 1; CMTX1; CMT1X; hereditary motor and sensory neuropathy, X-linked (HMSN-X / HMSN 1X); X-linked dominant CMT; connexin-32 neuropathy.

**Genetic heterogeneity of "CMTX."** CMTX1 (*GJB1*) accounts for **~90%** of X-linked CMT and is **X-linked dominant** with demyelinating/intermediate physiology. Rarer, often syndromic subtypes include **CMTX4 (AIFM1; Cowchock syndrome)**—X-linked recessive, axonal, with deafness and cognitive impairment ([PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/), [PMID: 26173962](https://pubmed.ncbi.nlm.nih.gov/26173962/))—plus **CMTX5 (PRPS1)**, **CMTX2/3**, and **CMTX6 (PDK3)** ([PMID: 41557339](https://pubmed.ncbi.nlm.nih.gov/41557339/)).

**Data provenance.** Derived from **aggregated, disease-level resources** (OMIM, Orphanet, peer-reviewed cohorts, case series, and mechanistic studies), not individual EHR data.

## 2. Etiology

**Primary cause (genetic, monogenic).** Loss-of-function / dominant-negative / trafficking-defective mutations in **GJB1/Cx32** on **Xq13.1**. Over 150 variants are reported; one large cohort documented 154 variants across 295 families ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)). Both hemizygous males and heterozygous females develop disease.

**Genetic risk factors.** Being **hemizygous male** for a pathogenic *GJB1* variant confers the highest burden. No consistent modifier loci are established; genotype–phenotype correlations are generally weak, though the promoter variant **c.-17G>A** produces a distinct milder phenotype ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)).

**Environmental / triggering factors.** CMTX1 is not environmentally caused, but **transient CNS episodes** are precipitated by **fever, infection, vigorous exercise, high altitude/hyperventilation, and allergen/pollen exposure** ([PMID: 42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/), [PMID: 30952033](https://pubmed.ncbi.nlm.nih.gov/30952033/)). **Age and male sex** are the strongest modifiers of peripheral severity ([PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)).

**Protective factors.** No validated genetic/environmental protective factors. In females, one normal *GJB1* allele generally yields milder disease—but **not** through skewed X-inactivation ([PMID: 40759929](https://pubmed.ncbi.nlm.nih.gov/40759929/)).

**Gene–environment interactions.** Metabolic/thermal stress precipitating reversible oligodendrocyte dysfunction in Cx32-mutant individuals is the main documented GxE interaction ([PMID: 42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/)).

## 3. Phenotypes

**Core peripheral neuropathy** (symmetric, length-dependent, adolescent onset):

| Phenotype | Type | HPO | Onset/severity/frequency |
|---|---|---|---|
| Distal muscle weakness (legs>hands) | Sign | HP:0002460 | Adolescent; progressive; >90% of males |
| Distal muscle atrophy | Manifestation | HP:0003693 | Progressive; common |
| Impaired distal sensation | Sign | HP:0106487 | Progressive; common |
| Paresthesia / tingling | Symptom | HP:0003401 | Frequent presenting symptom |
| Pes cavus / foot deformity | Manifestation | HP:0001761 | Childhood–adolescence; common |
| Areflexia / hyporeflexia | Sign | HP:0001265 | Common |
| Steppage gait | Sign | HP:0003376 | Chief complaint |
| Sensorineural hearing loss | Sign/lab | HP:0000407 | Occasional; variant-specific |
| Transient CNS "stroke-like" episodes | Sign (episodic) | HP:0002401 | Minority; reversible |

Yalcouyé et al.: *"The predominant starting symptom was tingling, and the chief complaint was gait difficulty. Neurological examination found a distal muscle weakness and atrophy, and sensory loss, skeletal deformities, decreased or absent reflexes and steppage gait"* ([PMID: 35383424](https://pubmed.ncbi.nlm.nih.gov/35383424/)). Median onset ~16.5 years (range 13–30) ([PMID: 31323543](https://pubmed.ncbi.nlm.nih.gov/31323543/)). Severity mild–moderate in females, moderate–severe in males, strongly age-dependent in males; high intra-/inter-familial variability.

**Quality-of-life impact.** CMT substantially reduces QoL; a survey of rare neurological conditions including CMT reported **EQ-5D index 0.2–0.44**, with frequent pain, anxiety/depression, and problems with mobility, self-care, and usual activities ([PMID: 23001492](https://pubmed.ncbi.nlm.nih.gov/23001492/)).

## 4. Genetic / Molecular Information

**Causal gene.** *GJB1* (connexin-32/Cx32), Xq13.1; a four-transmembrane gap-junction protein forming hexameric connexons.

**Pathogenic variants.**
- **Classes:** predominantly **missense** (majority), plus **nonsense, frameshift (c.423delC), splice-site, small in/dels, whole-gene deletions**, and **5′UTR/promoter (c.-17G>A)** variants ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/), [PMID: 12542510](https://pubmed.ncbi.nlm.nih.gov/12542510/)). Representative: p.Arg22Gln, p.Pro87Ala, p.Ile127Ser/Thr, p.Arg164Gln, p.Arg183Cys/His, p.Glu186Lys, p.Glu208Gly.
- **Classification (ACMG/AMP):** ~**82.4% P/LP**, remainder VUS ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)).
- **Allele frequency:** absent/ultra-rare in gnomAD.
- **Origin:** **germline**, X-linked; not somatic.
- **Functional consequence:** mixed—**loss of function** (deletions → peripheral-only disease), **dominant-negative**, and **trafficking defects** (ER/Golgi retention for CNS mutants; [PMID: 12111842](https://pubmed.ncbi.nlm.nih.gov/12111842/)).

**Genotype–phenotype.** Generally weak; deletion/null alleles cause peripheral-only disease, whereas mistrafficking mutants associate with CNS phenotypes; c.-17G>A is milder ([PMID: 12542510](https://pubmed.ncbi.nlm.nih.gov/12542510/), [PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)). VUS behave like P/LP at baseline, supporting reclassification ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)).

**Modifier genes / epigenetics / chromosomal.** No firm modifiers; female variability is **not** from skewed XCI ([PMID: 40759929](https://pubmed.ncbi.nlm.nih.gov/40759929/)). Whole-*GJB1* deletions are the largest lesions; no characteristic cytogenetic rearrangements.

## 5. Environmental Information

- **Environmental factors:** no causal toxin/pollution; physiological stressors (fever, infection, exercise, altitude, allergens) trigger transient CNS episodes ([PMID: 42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/), [PMID: 30952033](https://pubmed.ncbi.nlm.nih.gov/30952033/)).
- **Lifestyle:** no established dietary/smoking/alcohol risk; deconditioning worsens function; **avoid neurotoxic drugs (e.g., vincristine)** in any CMT.
- **Infectious agents:** none cause CMTX1; infections act only as nonspecific triggers.

## 6. Mechanism / Pathophysiology

**Normal Cx32 function.** Cx32 forms **reflexive gap junctions** in non-compact myelin (paranodes, Schmidt-Lanterman incisures), creating a **radial diffusion pathway** ~10⁶× faster than the circumferential route ([PMID: 9722620](https://pubmed.ncbi.nlm.nih.gov/9722620/), [PMID: 10586239](https://pubmed.ncbi.nlm.nih.gov/10586239/)). Partial redundancy from other connexins may contribute to variability.

**Causal chain.** Pathogenic *GJB1* variant → loss/dysfunction of Cx32 reflexive gap junctions → impaired Schwann-cell–axon radial diffusion/metabolic support → **early axonal cytoskeletal and transport defects** → demyelination and secondary axonal degeneration → length-dependent denervation → weakness/atrophy/sensory loss.

**Upstream vs downstream.** In *Gjb1*-null mice with minimal demyelination, *"axonal abnormalities… precede demyelination"* ([PMID: 20720503](https://pubmed.ncbi.nlm.nih.gov/20720503/)); electrophysiology shows *"primary demyelinating neuropathy with secondary axonal loss"* ([PMID: 15468313](https://pubmed.ncbi.nlm.nih.gov/15468313/)). This supports the "functional axonopathy" model ([PMID: 16775378](https://pubmed.ncbi.nlm.nih.gov/16775378/)).

**Protein dysfunction.** CNS-phenotype mutants (A39V, T55I → ER; M93V, R164Q, R183H → Golgi) *"failed to reach the cell membrane"* ([PMID: 12111842](https://pubmed.ncbi.nlm.nih.gov/12111842/)).

**Cells & processes (GO/CL).** Myelinating Schwann cell (CL:0002573), oligodendrocyte (CL:0000128); myelination (GO:0042552), gap-junction assembly/cell-cell signaling (GO:0007267), axonal transport (GO:0008088), connexin complex (GO:0005922); secondary neuroinflammation reduced by gene therapy ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)).

**Immune involvement.** Not autoimmune, but secondary neuroinflammation occurs; an emerging epidemiological **CMTX–MS association** (20-yr MS incidence 4.3%, p=0.00039) suggests Cx32 loss may predispose to CNS inflammatory demyelination ([PMID: 30196252](https://pubmed.ncbi.nlm.nih.gov/30196252/)).

**Biomarkers.** Blood **NfL** is elevated and tracks disease/therapy in the model ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)) and in human carriers ([PMID: 42017539](https://pubmed.ncbi.nlm.nih.gov/42017539/)).

## 7. Anatomical Structures Affected

- **Organ/system:** **Peripheral nervous system** (UBERON:0000010) primary; **CNS white matter** (UBERON:0002316) secondary/transient; musculoskeletal (distal atrophy, foot deformity).
- **Nerves:** distal > proximal—sural, peroneal/fibular, median, ulnar, radial ([PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)); sciatic (UBERON:0001322).
- **Tissue/cell:** myelinating Schwann cells (CL:0002573); oligodendrocytes (CL:0000128); secondary skeletal muscle denervation.
- **Subcellular (GO CC):** connexin complex/gap junction (GO:0005922) at non-compact myelin; mutant protein in ER (GO:0005783) and Golgi (GO:0005794); axonal neurofilaments (GO:0005882).
- **Localization/laterality:** **bilateral, symmetric, length-dependent** peripheral involvement; CNS lesions often symmetric, favoring corpus callosum splenium and centrum semiovale ([PMID: 42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/)).

## 8. Temporal Development

- **Onset:** typically **first–second decade** (median ~16.5 y; [PMID: 31323543](https://pubmed.ncbi.nlm.nih.gov/31323543/)); insidious/chronic. Transient CNS episodes can be an acute/subacute presenting event, sometimes in childhood.
- **Progression:** **slowly progressive over decades**; strong **age–severity correlation in males**, not females ([PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)).
- **Course:** peripheral neuropathy chronic-progressive, lifelong; CNS episodes episodic and reversible (hours–days).
- **Critical windows:** pre- and post-onset gene therapy both improved outcomes in mice, implying a therapeutic window extending beyond onset ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)).

## 9. Inheritance and Population

- **Inheritance:** **X-linked (dominant with intermediate female expression)**; hallmark **no male-to-male transmission** ([PMID: 15468313](https://pubmed.ncbi.nlm.nih.gov/15468313/)). Affected fathers → all daughters (carriers), no sons; carrier mothers → 50% of children.
- **Penetrance:** near-complete in hemizygous males; variable/incomplete in heterozygous females.
- **Expressivity:** highly variable, even within families ([PMID: 35383424](https://pubmed.ncbi.nlm.nih.gov/35383424/)).
- **Anticipation:** none (not a repeat expansion).
- **Founder effects:** regional alleles exist (e.g., Pro87Ala in Bashkortostan with a shared haplotype; [PMID: 19062535](https://pubmed.ncbi.nlm.nih.gov/19062535/)).
- **Consanguinity:** not relevant (X-linked).
- **Epidemiology:** overall CMT ~**1/2,500** ([PMID: 29174527](https://pubmed.ncbi.nlm.nih.gov/29174527/)); GJB1 ~9% of CMT (second most common), ~13.7% regionally → estimated CMTX1 prevalence ~1.3–6/100,000.
- **Geography:** worldwide, including a sub-Saharan African cohort (Mali; [PMID: 35383424](https://pubmed.ncbi.nlm.nih.gov/35383424/)); no strong ethnic predilection.
- **Sex ratio:** both sexes affected; **males more severely** ([PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)).

## 10. Diagnostics

- **Electrophysiology (key):** **"intermediate" motor conduction velocities** (~25–45 m/s), demyelinating + secondary axonal loss, often non-uniform slowing; females less slowed ([PMID: 15468313](https://pubmed.ncbi.nlm.nih.gov/15468313/), [PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)).
- **Clinical/pedigree criteria:** CMT phenotype + intermediate NCV + negative *PMP22* dup/HNPP deletion + dominant inheritance without male-to-male transmission → screen *GJB1* ([PMID: 15468313](https://pubmed.ncbi.nlm.nih.gov/15468313/)).
- **Genetic testing (confirmatory):** single-gene *GJB1* sequencing or NGS CMT panel / WES ([PMID: 39428786](https://pubmed.ncbi.nlm.nih.gov/39428786/)); MLPA first to exclude *PMP22* dosage changes; dosage methods for whole-gene deletions.
- **Nerve biopsy (not routine):** demyelination, remyelination, onion bulbs, axonal loss ([PMID: 12542510](https://pubmed.ncbi.nlm.nih.gov/12542510/)).
- **Imaging:** brain MRI during CNS episodes shows reversible DWI-restricted white-matter lesions (splenium, centrum semiovale); MRA/MRV normal ([PMID: 42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/), [PMID: 30196252](https://pubmed.ncbi.nlm.nih.gov/30196252/)).
- **Audiology:** when hearing loss suspected ([PMID: 41557339](https://pubmed.ncbi.nlm.nih.gov/41557339/)).
- **Biomarker:** **serum NfL** (axonal degeneration), normalized by gene therapy in model and elevated in human carriers ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/), [PMID: 42017539](https://pubmed.ncbi.nlm.nih.gov/42017539/)).
- **Differential diagnosis:** CMT1A (uniform slowing), MPZ-CMT, **CIDP** (females with conduction block often misdiagnosed; [PMID: 40759929](https://pubmed.ncbi.nlm.nih.gov/40759929/)); during CNS episodes: stroke, MELAS, ADEM, MS.
- **Screening:** cascade/carrier testing of at-risk relatives; prenatal/PGT for known variants.

## 11. Outcome / Prognosis

- **Survival/mortality:** **normal/near-normal life expectancy**; not directly life-limiting.
- **Morbidity/disability:** progressive distal weakness, foot deformity, gait impairment, hand dexterity loss, neuropathic pain, fatigue; most patients remain **ambulatory** (often with AFOs); males accrue greater disability with age ([PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)).
- **Quality of life:** substantially reduced (EQ-5D 0.2–0.44; [PMID: 23001492](https://pubmed.ncbi.nlm.nih.gov/23001492/)).
- **Complications:** falls/fractures, foot ulceration, contractures; transient CNS episodes; possible increased MS risk ([PMID: 30196252](https://pubmed.ncbi.nlm.nih.gov/30196252/)); hearing loss in a subset.
- **Prognostic factors:** male sex, older age ([PMID: 28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/)); longitudinal change captured by **CMTES** ([PMID: 37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/)); c.-17G>A predicts milder course.

## 12. Treatment

- **Disease-modifying therapy:** **none approved** — *"Symptomatic management is still the only option"* ([PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)).
- **Emerging gene therapy:** **AAV9-Mpz.GJB1** (Schwann-cell-targeted, intrathecal) rescued *Gjb1*-null mice pre- and post-onset with improved motor performance, conduction, myelination, reduced inflammation, and improved blood biomarkers ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)) (NCIT: Gene Therapy).
- **Supportive/rehabilitative (standard of care):** physical/occupational therapy, ankle-foot orthoses, stretching, exercise, assistive devices (NCIT: Physical Therapy, Occupational Therapy, Orthotic Device).
- **Symptom management:** neuropathic pain control (gabapentinoids, duloxetine, tricyclics), fatigue management, foot care.
- **Surgical:** corrective foot surgery (osteotomy, tendon transfer, arthrodesis) for disabling deformity.
- **Sensorineural hearing loss:** cochlear implantation beneficial in selected patients, best early ([PMID: 41557339](https://pubmed.ncbi.nlm.nih.gov/41557339/)).
- **Cautions:** avoid neurotoxic agents (vincristine, etc.).

## 13. Prevention

- **Primary:** not preventable (monogenic); **genetic counseling** and reproductive options (prenatal diagnosis, PGT) for known *GJB1* variants.
- **Secondary:** **cascade genetic screening** of at-risk relatives; early identification enables avoidance of neurotoxic drugs and early orthotics/PT.
- **Tertiary:** rehabilitation, orthotics, foot care, pain management to prevent falls, deformity, ulceration ([PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)).
- **Trigger avoidance:** manage fever, extreme exertion, high altitude in patients with CNS episodes ([PMID: 42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/)).
- **Counseling:** X-linked recurrence-risk education (no male-to-male transmission).
- **Immunization/public health/prophylaxis:** not applicable.

## 14. Other Species / Natural Disease

- **Taxonomy:** *Mus musculus* (NCBI Taxon 10090); *Homo sapiens* (9606).
- **Ortholog:** mouse **Gjb1/connexin-32** (NCBI Gene 14618); highly conserved.
- **Natural disease:** no well-characterized spontaneous CMTX1-equivalent connexin-32 neuropathy is catalogued in companion animals in OMIA; studied primarily via engineered rodent models.
- **Comparative biology:** Cx32 gap-junction biology and myelin architecture are conserved across mammals.
- **Zoonotic potential:** none (genetic disease).

## 15. Model Organisms

- **Principal model:** **Gjb1-null (Cx32 knockout) mouse**—recapitulates progressive demyelinating peripheral neuropathy with early axonal changes ([PMID: 20720503](https://pubmed.ncbi.nlm.nih.gov/20720503/)) and impaired conduction; used for natural-history and therapy studies ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)).
- **Model types:** knockout; human-mutation knock-in/transgenic lines; cell models (HeLa / communication-incompetent cells transfected with WT/mutant Cx32 for trafficking assays; [PMID: 12111842](https://pubmed.ncbi.nlm.nih.gov/12111842/)).
- **Phenotype recapitulation:** good for peripheral demyelination, axonal transport defects, conduction slowing, elevated NfL, neuroinflammation, and treatment response.
- **Limitations:** milder CNS involvement; does not fully model human transient stroke-like episodes or the male–female severity dichotomy.
- **Applications:** mechanistic dissection (axon vs myelin), preclinical gene therapy, biomarker development.
- **Resources:** MGI (Gjb1), IMPC/IMSR, Cellosaurus.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [37284795](https://pubmed.ncbi.nlm.nih.gov/37284795/) | *Genetic analysis and natural history of CMTX1 due to GJB1 variants* | Largest cohort; causal gene, inheritance, 2nd-most-common, CMTES natural history, VUS≈P/LP, c.-17G>A |
| [28768847](https://pubmed.ncbi.nlm.nih.gov/28768847/) | *Cross-sectional analysis of a large CMTX1 cohort* | Quantifies male>female severity; age–burden correlation |
| [20720503](https://pubmed.ncbi.nlm.nih.gov/20720503/) | *Axonal pathology precedes demyelination (mouse)* | Temporal causal chain: axonopathy upstream of demyelination |
| [9722620](https://pubmed.ncbi.nlm.nih.gov/9722620/) | *Functional gap junctions in the Schwann cell myelin sheath* | Normal Cx32 role; ~10⁶× faster radial pathway |
| [10586239](https://pubmed.ncbi.nlm.nih.gov/10586239/) | *Nodes, paranodes, and incisures* | Cx32 localization to reflexive gap junctions |
| [12111842](https://pubmed.ncbi.nlm.nih.gov/12111842/) | *Cellular mechanisms of Cx32 CNS mutations* | Mutant mistrafficking (ER/Golgi) → CNS phenotype |
| [30196252](https://pubmed.ncbi.nlm.nih.gov/30196252/) | *CMTX and multiple sclerosis* | Statistically significant MS excess; splenium hyperintensity |
| [33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/) | *AAV9 Schwann-cell GJB1 gene therapy* | Pre/post-onset rescue; NfL biomarker response |
| [15468313](https://pubmed.ncbi.nlm.nih.gov/15468313/) | *Ile127Ser GJB1 phenotype* | Intermediate CV + no male-to-male transmission = diagnostic rule |
| [40759929](https://pubmed.ncbi.nlm.nih.gov/40759929/) | *Random XCI in female CMTX1* | Refutes skewed XCI as female-variability mechanism |
| [35383424](https://pubmed.ncbi.nlm.nih.gov/35383424/) | *GJB1 variants in Mali* | Core clinical signs enumerated |
| [31323543](https://pubmed.ncbi.nlm.nih.gov/31323543/) | *Three novel mutations, Chinese patients* | Age of onset (median 16.5 y) |
| [29174527](https://pubmed.ncbi.nlm.nih.gov/29174527/) | *Hungarian CMT subtype frequencies* | Prevalence 1/2,500; GJB1 2nd (9.2%) |
| [23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/) | *Cowchock syndrome / AIFM1* | Non-GJB1 X-linked subtype (CMTX4) |
| [26173962](https://pubmed.ncbi.nlm.nih.gov/26173962/) | *Novel AIFM1 mutation* | Expands AIFM1 phenotypic spectrum |
| [42017539](https://pubmed.ncbi.nlm.nih.gov/42017539/) | *NEFL-associated CMT* | Human serum NfL elevation in CMT-spectrum carriers |
| [23001492](https://pubmed.ncbi.nlm.nih.gov/23001492/) | *HRQL in rare neurological conditions* | EQ-5D quality-of-life impact |
| [41557339](https://pubmed.ncbi.nlm.nih.gov/41557339/) | *Cochlear implantation in CMT* | Hearing-loss management incl. GJB1/CMT1X |
| [40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/) | *CMT management, 2025 review* | Supportive care remains only option |
| [16775378](https://pubmed.ncbi.nlm.nih.gov/16775378/) | *Pathomechanisms of mutant CMT proteins* | Functional-axonopathy hypothesis |
| [19062535](https://pubmed.ncbi.nlm.nih.gov/19062535/) | *GJB1 in Bashkortostan* | Founder effect (Pro87Ala); 13.7% frequency |
| [12542510](https://pubmed.ncbi.nlm.nih.gov/12542510/) | *GJB1 mutations and CNS symptoms* | Deletion → peripheral-only; gain-of-function → CNS |
| [30952033](https://pubmed.ncbi.nlm.nih.gov/30952033/) | *Stroke-like syndrome, I127T* | Transient CNS episodes with reversible MRI |
| [42477620](https://pubmed.ncbi.nlm.nih.gov/42477620/) | *Pediatric stroke-like episodes, pollen* | Triggers and reversible white-matter lesions |
| [39428786](https://pubmed.ncbi.nlm.nih.gov/39428786/) | *Novel R183C missense, WES diagnosis* | WES diagnostic utility |
| [25429913](https://pubmed.ncbi.nlm.nih.gov/25429913/) | *CMT frequencies, Southern Italy* | Epidemiology corroboration |

**Ontology term suggestions (summary).** MONDO:0010674; OMIM 302800. HPO: HP:0002460 (distal weakness), HP:0003693 (distal amyotrophy), HP:0001761 (pes cavus), HP:0106487 (impaired distal sensation), HP:0003401 (paresthesia), HP:0001265 (areflexia), HP:0003376 (steppage gait), HP:0000407 (SNHL), HP:0002401 (stroke-like episode). GO: GO:0042552 (myelination), GO:0007267 (cell-cell signaling), GO:0008088 (axonal transport), GO:0005922 (connexin complex), GO:0005783 (ER), GO:0005794 (Golgi). CL: CL:0002573 (myelinating Schwann cell), CL:0000128 (oligodendrocyte). UBERON: UBERON:0000010 (PNS), UBERON:0002316 (white matter), UBERON:0001322 (sciatic nerve). NCIT: Gene Therapy, Physical Therapy, Occupational Therapy, Orthotic Device, Cochlear Implant.

---

## Limitations and Knowledge Gaps

1. **No primary experimental dataset** was analyzed; conclusions rest on published cohorts, case reports, and mechanistic studies (evidence types: human clinical, mouse model, in vitro, computational).
2. **Prevalence estimates for CMTX1 specifically are indirect** (CMT-wide prevalence × GJB1 fraction).
3. **Human molecular profiling is sparse**—transcriptomic/proteomic/metabolomic maps of human CMTX1 nerve are limited; much mechanistic detail derives from the *Gjb1*-null mouse, which does not fully model CNS episodes, the MS-association, or intermediate CVs.
4. **Female-variability mechanism remains unexplained** after XCI was refuted ([PMID: 40759929](https://pubmed.ncbi.nlm.nih.gov/40759929/)); modifier genes/epigenetics are uncharacterized.
5. **Weak genotype–phenotype correlation** limits variant-specific prognostication (beyond c.-17G>A and CNS-mutant trafficking).
6. **CNS/stroke-like episodes and MS association derive largely from case series** (lower evidence level).
7. **No approved disease-modifying therapy**; gene-therapy evidence is preclinical, and serum NfL requires CMTX1-specific longitudinal validation as a surrogate endpoint.
8. **No well-documented naturally occurring animal counterpart** exists; comparative data are thin.

---

## Proposed Follow-up Experiments / Actions

1. **Advance AAV9-*GJB1* gene therapy toward clinical trials**, using CMTES and serum NfL as co-primary endpoints and leveraging the demonstrated pre-/post-onset efficacy window ([PMID: 33692503](https://pubmed.ncbi.nlm.nih.gov/33692503/)).
2. **Prospective longitudinal NfL study** in genotyped CMTX1 males and females to validate NfL as a progression/response biomarker and correlate with CMTES.
3. **Single-cell / spatial transcriptomics of human (or humanized-model) peripheral nerve** to map Schwann-cell and axonal molecular changes in situ and confirm upstream vs. downstream events.
4. **Search for genetic/epigenetic modifiers of female severity** now that skewed XCI is excluded—candidate modifier screens and family-based studies.
5. **Systematic genotype–phenotype cataloguing** (variant class × CNS involvement × severity) integrating trafficking assays to refine ACMG classification and reclassify VUS.
6. **Prospective natural-history and MS-surveillance cohort** to clarify the CMTX–MS relationship and define management for CNS episodes and triggers.
7. **Consolidate rare CMTX subtype registries** (*AIFM1*, *PRPS1*, *PDK3*) to distinguish them diagnostically and prognostically from CMTX1.

---

## Evidence Source Types
Human clinical cohorts/case series: PMIDs 37284795, 28768847, 31323543, 35383424, 12542510, 30952033, 42477620, 30196252, 39428786, 41557339, 23001492, 29174527, 19062535, 15468313, 40759929, 23217327, 26173962, 25429913, 42017539. Mouse in vivo: 20720503, 33692503. In vitro cell biology: 12111842, 9722620. Reviews: 16775378, 40014417, 10586239.


## Artifacts

- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Type_X-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Type_X-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 21 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:9722620` (10 mentions) - Functional gap junctions in the schwann cell myelin sheath.
  - shared terms: cx32
- `PMID:10586239` (6 mentions) - Nodes, paranodes, and incisures: from form to function.
  - shared terms: axonal

Weighed against this report's own most characteristic terms: `gjb1`, `cns`, `gene`, `female`, `cmtx1`, `male`, `episode`, `axonal`, `cmt`, `cx32`, `disease`, `therapy`, `cohort`, `variant`, `phenotype`, `loss`, `neuropathy`, `x-linked`, `patient`, `transient`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.