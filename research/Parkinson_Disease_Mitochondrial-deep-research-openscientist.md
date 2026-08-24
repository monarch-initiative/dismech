---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-14T23:31:43.913241'
end_time: '2026-08-14T23:46:36.669605'
duration_seconds: 892.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Parkinson Disease, Mitochondrial
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
citation_count: 45
reference_validation:
  total_references: 45
  verified: 45
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Parkinson_Disease_Mitochondrial-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Parkinson_Disease_Mitochondrial-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Parkinson Disease, Mitochondrial
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Parkinson Disease, Mitochondrial** covering all of the
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

# Parkinson Disease, Mitochondrial — Comprehensive Disease Characterization Report

**Target Disease:** Parkinson Disease, Mitochondrial
**OMIM:** 556500 | **Category:** Mendelian (maternally/mitochondrially inherited)
**Suggested MONDO mapping:** MONDO term for "Parkinson disease, mitochondrial" (derived from OMIM 556500)

*Evidence types are labeled where relevant: [Human clinical], [Model organism], [In vitro], [Computational/meta-analysis]. PMIDs are given for all key claims.*

---

## Summary

**Parkinson Disease, Mitochondrial (OMIM 556500)** is a rare, maternally (mitochondrially) inherited form of parkinsonism defined molecularly by a heteroplasmic point mutation in the mitochondrially-encoded 12S ribosomal RNA gene (**m.T1095C in *MT-RNR1***). In the originally described pedigree, this variant co-segregated with a distinctive clinical triad of **levodopa-responsive parkinsonism, sensorineural (aminoglycoside-sensitive) hearing loss, and peripheral neuropathy**. The mutation disrupts a highly conserved loop of the small-subunit mitochondrial rRNA important for initiation of mitochondrial protein synthesis, producing measurable defects in oxidative phosphorylation — notably reduced cytochrome c oxidase (complex IV) activity in patient cells and, in transmitochondrial cybrids, depletion of mitochondrial glutathione, reduced complex II/III activity, and markedly increased aminoglycoside-induced apoptosis ([PMID: 11079536](https://pubmed.ncbi.nlm.nih.gov/11079536/); [PMID: 22735573](https://pubmed.ncbi.nlm.nih.gov/22735573/)).

Beyond this specific Mendelian entity, "Mitochondrial Parkinson Disease" serves as the archetype of the broader and central role of **mitochondrial dysfunction in Parkinson disease (PD)**. Converging genetic and biochemical evidence implicates: (1) **respiratory chain complex I (CI) deficiency**, which stratifies roughly one-quarter of idiopathic PD into a distinct molecular subtype; (2) **nuclear-encoded mtDNA-maintenance failure** (*POLG*, *TWNK*/C10orf2-Twinkle) causing accumulation of multiple mtDNA deletions and selective nigrostriatal degeneration; (3) **defective PINK1–Parkin mitophagy** (*PINK1*, *PRKN*) underlying autosomal-recessive early-onset PD; and (4) common **mtDNA haplogroup/variant** modulation of sporadic PD risk and progression. These insults converge on the selective loss of a molecularly-defined vulnerable dopaminergic population — the **SOX6⁺/AGTR1⁺ ventral-tier substantia nigra pars compacta (SNpc)** neurons that are specifically enriched for heritable PD risk.

Clinically, management is symptomatic (levodopa, deep brain stimulation, and support for hearing loss and neuropathy) with **no proven disease-modifying therapy**. Because the core mutation is maternally transmitted and heteroplasmic, prevention centers on **genetic counseling for maternal inheritance** and, for carriers, **avoidance of aminoglycoside antibiotics and complex I–inhibiting neurotoxins**. This report synthesizes eight confirmed findings across 86 reviewed papers and maps them to the requested disease-knowledge-base sections, with ontology term suggestions and PMID-anchored evidence throughout.

---

## Key Findings

### Finding 1 — A maternally inherited heteroplasmic 12S rRNA mutation (m.T1095C) defines the disease

Thyagarajan et al. (2000) identified a **novel heteroplasmic, maternally inherited 12S rRNA point mutation (T1095C, *MT-RNR1*)** in a pedigree presenting with maternally inherited sensorineural deafness, levodopa-responsive parkinsonism, and neuropathy. The variant was **absent in 270 ethnically diverse controls**, and respiratory chain enzyme analysis in cultured lymphocytes from the proband revealed a **significant reduction in cytochrome c oxidase (complex IV) activity**. The mutation is predicted to disrupt a highly conserved loop within the small-subunit rRNA critical for the initiation of mitochondrial protein synthesis ([PMID: 11079536](https://pubmed.ncbi.nlm.nih.gov/11079536/)). [Human clinical]

> *"A novel, heteroplasmic, maternally inherited 12SrRNA point mutation (T1095C) was found in the pedigree. Respiratory chain enzyme analysis in cultured lymphocytes from the proband revealed a significant reduction in cytochrome c oxidase activity."* — [PMID: 11079536](https://pubmed.ncbi.nlm.nih.gov/11079536/)

Functional confirmation came from cybrid studies (Muyderman et al., 2012). A transmitochondrial cybrid line derived from the proband showed **selective depletion of mitochondrial glutathione, decreases in complex II/III activity, and a ~10-fold increase in aminoglycoside (gentamicin)-induced apoptosis** ([PMID: 22735573](https://pubmed.ncbi.nlm.nih.gov/22735573/)). [In vitro] This aminoglycoside hypersensitivity is mechanistically important because m.T1095C lies in the same 12S rRNA gene (*MT-RNR1*) that harbors the classic aminoglycoside-ototoxicity/deafness variants (e.g., m.1555A>G), explaining the deafness phenotype and the pharmacogenomic contraindication.

> *"a transmitochondrial cybrid line derived from the proband of this family shows selective depletion of mitochondrial glutathione and decreases in the activity of complex II/III"* — [PMID: 22735573](https://pubmed.ncbi.nlm.nih.gov/22735573/)

**Interpretation:** m.T1095C is a **gain of dysfunction at the level of mitochondrial translation** → impaired assembly of respiratory-chain complexes → energy deficit and oxidative-stress vulnerability in high-demand, high-oxidative tissues (auditory hair cells/cochlea, peripheral nerve, and nigral dopaminergic neurons).

---

### Finding 2 — Defective mtDNA replication/maintenance (POLG, TWNK) causes selective nigrostriatal degeneration

Tzoulis et al. (2016) used dopamine-transporter (DAT) imaging in 21 patients across diverse mitochondrial disorders and found that **nigrostriatal degeneration occurred exclusively in patients with defective mtDNA replication and maintenance** (mutations in *POLG* or *C10orf2*/Twinkle). In these patients the degeneration was **progressive and at least as severe as in advanced PD**, whereas patients with primary mtDNA point mutations or single large-scale deletions showed **no nigral involvement** ([PMID: 26979109](https://pubmed.ncbi.nlm.nih.gov/26979109/)). [Human clinical]

> *"Nigrostriatal degeneration occurred exclusively in patients with defective mtDNA replication and maintenance. In these patients, nigrostriatal degeneration was progressive and at least as severe as in patients with advanced Parkinson's disease."* — [PMID: 26979109](https://pubmed.ncbi.nlm.nih.gov/26979109/)

Mechanistically, mtDNA-maintenance defects drive the **progressive accumulation of multiple mtDNA deletions in substantia nigra dopaminergic neurons**, seen in normal aging and, to a greater extent, in PD (Manini et al., 2022) ([PMID: 35114397](https://pubmed.ncbi.nlm.nih.gov/35114397/)).

> *"studies have demonstrated a progressive accumulation of multiple mtDNA deletions in dopaminergic neurons of the substantia nigra in elderly population and, to a greater extent, in Parkinson's disease patients"* — [PMID: 35114397](https://pubmed.ncbi.nlm.nih.gov/35114397/)

Clinically, *POLG*-related parkinsonism is typically **levodopa-responsive**. Sensory neuropathy accompanying levodopa-responsive dystonia/parkinsonism should prompt *POLG* testing (Qiu et al., 2021; [PMID: 34062649](https://pubmed.ncbi.nlm.nih.gov/34062649/)), and *POLG* variants can co-occur with other PD genes such as *GBA* (Chen et al., 2019; [PMID: 30941926](https://pubmed.ncbi.nlm.nih.gov/30941926/)). This finding establishes that the pathway from mitochondrial dysfunction to nigral loss is **not caused equally by all mitochondrial lesions** — it is the failure of mtDNA maintenance (and consequent somatic deletion load) that most reliably produces PD-like nigral vulnerability.

---

### Finding 3 — Neuronal complex I deficiency stratifies idiopathic PD into a distinct molecular subtype

Complex I deficiency in PD substantia nigra was first established by Schapira et al. (1993) ([PMID: 8420145](https://pubmed.ncbi.nlm.nih.gov/8420145/)). Flønes et al. (2024) advanced this to a stratification framework, showing that **idiopathic PD can be divided by the severity of neuronal respiratory complex I (CI) deficiency** into two emerging subtypes with distinct molecular and clinical profiles ([PMID: 38684731](https://pubmed.ncbi.nlm.nih.gov/38684731/)). [Human clinical]

- A **CI-deficient subtype (~25% of cases)** with anatomically widespread neuronal CI deficiency, distinct cell-type-specific gene expression, increased neuronal mtDNA deletion load, and predilection for **non-tremor-dominant** phenotypes.
- A **non-CI-deficient subtype** confined to dopaminergic SNpc, with a **tremor-dominant** predilection.

> *"iPD can be stratified according to the severity of neuronal respiratory complex I (CI) deficiency, and identify two emerging disease subtypes with distinct molecular and clinical profiles"* — [PMID: 38684731](https://pubmed.ncbi.nlm.nih.gov/38684731/)

Earlier work by the same group (Flønes et al., 2018) demonstrated that **neuronal CI deficiency occurs throughout the PD brain, including regions spared by neurodegeneration** (e.g., cerebellum), and did not correlate with mtDNA damage outside the substantia nigra ([PMID: 29270838](https://pubmed.ncbi.nlm.nih.gov/29270838/)) — indicating that CI deficiency is a widespread, partly independent feature rather than a mere consequence of local cell death.

> *"neuronal complex I deficiency occurs throughout the Parkinson's disease brain, including areas spared by the neurodegenerative process such as the cerebellum"* — [PMID: 29270838](https://pubmed.ncbi.nlm.nih.gov/29270838/)

This finding has direct **precision-medicine relevance**: it rationalizes trials of "mitochondrial enhancer" strategies in genetically/biochemically stratified subgroups (e.g., the coenzyme Q10 stratified trial concept, [PMID: 33324897](https://pubmed.ncbi.nlm.nih.gov/33324897/)).

---

### Finding 4 — mtDNA haplogroups and variants modulate PD risk and progression

A systematic review/meta-analysis (Sena-Dos-Santos et al., 2024; 13,640 PD cases, 22,588 controls) identified four mtDNA variants associated with PD and several risk-modulating macrohaplogroups ([PMID: 38917640](https://pubmed.ncbi.nlm.nih.gov/38917640/)). [Computational/meta-analysis]

> *"Four mtDNA variants were associated with PD: m.4336C (odds ratio [OR] = 2.99; 95 % confidence interval [CI] = 1.79-5.02), m.7028T (OR = 0.80; 95 % CI = 0.70-0.91), m.10398G (OR = 0.92; 95 % CI = 0.85-0.98), and m.13368A (OR = 0.74; 95 % CI = 0.56-0.98)"* — [PMID: 38917640](https://pubmed.ncbi.nlm.nih.gov/38917640/)

| mtDNA variant / haplogroup | Effect | Odds ratio (95% CI) | Direction |
|---|---|---|---|
| m.4336C (tRNA-Gln, *MT-TQ*) | Risk | 2.99 (1.79–5.02) | ↑ risk |
| m.7028T | Protective | 0.80 (0.70–0.91) | ↓ risk |
| m.10398G | Protective | 0.92 (0.85–0.98) | ↓ risk |
| m.13368A | Protective | 0.74 (0.56–0.98) | ↓ risk |
| Macrohaplogroup R | Risk | 2.25 | ↑ risk |
| Macrohaplogroup F | Risk | 1.18 | ↑ risk |
| Macrohaplogroup H | Risk | 1.12 | ↑ risk |
| Macrohaplogroup B | Protective | 0.77 | ↓ risk |

For **progression**, Liu et al. (2023) found that the haplogroup super-cluster J/T/U was associated with a **41% lower risk of cognitive progression** (P = 2.42 × 10⁻⁶) versus haplogroup H ([PMID: 36343661](https://pubmed.ncbi.nlm.nih.gov/36343661/)).

> *"patients with the super macro-haplogroup J, T, U# had a 41% lower risk of cognitive progression with P = 2.42 × 10-6 compared to those with macro-haplogroup H"* — [PMID: 36343661](https://pubmed.ncbi.nlm.nih.gov/36343661/)

Historically, the **np4336 tRNA-Gln variant** was enriched in AD+PD patients (~5.2% vs 0.7% of controls; Shoffner et al., 1993; [PMID: 8104867](https://pubmed.ncbi.nlm.nih.gov/8104867/)). Importantly, the mtDNA-association literature is **heterogeneous**: some cohorts (e.g., a familial PD study, [PMID: 20356410](https://pubmed.ncbi.nlm.nih.gov/20356410/); an East Indian cohort, [PMID: 33904476](https://pubmed.ncbi.nlm.nih.gov/33904476/)) found no maternal-inheritance bias or haplogroup association, underscoring population-specificity and methodological caveats ([PMID: 31233840](https://pubmed.ncbi.nlm.nih.gov/31233840/)).

---

### Finding 5 — Animal and cellular models recapitulate mitochondrial parkinsonism

**Toxin (complex I inhibitor) models:** MPTP (via MPP⁺), rotenone, paraquat, and 6-OHDA produce selective nigrostriatal dopaminergic degeneration and motor deficits ([PMID: 34043196](https://pubmed.ncbi.nlm.nih.gov/34043196/); [PMID: 30605763](https://pubmed.ncbi.nlm.nih.gov/30605763/)). [Model organism] MPTP more precisely reproduces nigral DA neuron loss and neuroinflammation, whereas rotenone better models CI-deficiency biochemistry and Lewy-body-like α-synuclein aggregation ([PMID: 35039876](https://pubmed.ncbi.nlm.nih.gov/35039876/)).

**Genetic mitochondrial model — MitoPark mouse:** DAT-Cre-driven deletion of the mitochondrial transcription factor *TFAM* in DA neurons produces progressive, adult-onset dopaminergic degeneration with motor decline; it is worsened by manganese (gene–environment interaction) and improved by voluntary exercise ([PMID: 28595911](https://pubmed.ncbi.nlm.nih.gov/28595911/); [PMID: 31226324](https://pubmed.ncbi.nlm.nih.gov/31226324/)).

> *"This unique PD model recapitulates key features of the disease including progressive neurobehavioral changes and neuronal degeneration"* — [PMID: 28595911](https://pubmed.ncbi.nlm.nih.gov/28595911/)

**Nuclear mtDNA-maintenance models** (Mutator, Deletor, PD-mitoPstI, TwinkPark) show nigrostriatal degeneration, mirroring the human *POLG*/*TWNK* phenotype ([PMID: 35114397](https://pubmed.ncbi.nlm.nih.gov/35114397/)).

**PINK1/Parkin models:** Loss-of-function in *Drosophila* and patient iPSC-derived dopaminergic neurons causes impaired mitophagy/mitochondrial clearance, ROS accumulation, reduced ATP, and apoptosis ([PMID: 32470327](https://pubmed.ncbi.nlm.nih.gov/32470327/); [PMID: 32138754](https://pubmed.ncbi.nlm.nih.gov/32138754/)). [In vitro / Model organism]

> *"The proposed system recapitulates the deficiency of mitochondrial clearance, ROS accumulation, and increasing apoptosis in these familial PD-derived neurons"* — [PMID: 32470327](https://pubmed.ncbi.nlm.nih.gov/32470327/)

---

### Finding 6 — A specific SNpc dopaminergic subtype (SOX6⁺/AGTR1⁺, ventral tier) is selectively vulnerable and enriched for PD heritability

Single-cell/single-nucleus profiling of 387,483 human midbrain nuclei (22,048 DA-neuron profiles) by Kamath et al. (2022) identified ten DA subtypes. A **single subtype marked by *AGTR1* (within the *SOX6* lineage), spatially confined to the ventral tier of SNpc**, was most susceptible to loss in PD, showed the strongest upregulation of TP53 and NR2F2 targets, and was **specifically enriched for heritable PD risk** ([PMID: 35513515](https://pubmed.ncbi.nlm.nih.gov/35513515/)). [Human clinical / single-cell]

> *"A single subtype, marked by the expression of the gene AGTR1 and spatially confined to the ventral tier of SNpc, was highly susceptible to loss in PD and showed the strongest upregulation of targets of TP53 and NR2F2"* — [PMID: 35513515](https://pubmed.ncbi.nlm.nih.gov/35513515/)

A complementary mouse midbrain snRNA-seq atlas (~70,000 cells) confirmed **graded vulnerability across mDA "territories"** in a 6-OHDA lesion model, framing vulnerability as a continuum rather than discrete classes ([PMID: 38587883](https://pubmed.ncbi.nlm.nih.gov/38587883/)). The *AGTR1* marker is mechanistically notable given independent zebrafish evidence that renin–angiotensin system (RAAS) inhibitors are neuroprotective via mitochondrial restoration in DA neurons ([PMID: 34550070](https://pubmed.ncbi.nlm.nih.gov/34550070/)).

---

### Finding 7 — Reduced CSF cell-free mtDNA (ccf-mtDNA) is a candidate early-PD biomarker

Pyle et al. (2015) found a **significant reduction of ccf-mtDNA in PD CSF versus controls**, proposing it as a biomarker for early PD/neurodegeneration ([PMID: 26343811](https://pubmed.ncbi.nlm.nih.gov/26343811/)). [Human clinical]

> *"identifying a significant reduction of ccf-mtDNA in PD patient cerebrospinal fluid (CSF) when compared to controls. Our data demonstrates that CSF ccf-mtDNA is not only a powerful biomarker for PD"* — [PMID: 26343811](https://pubmed.ncbi.nlm.nih.gov/26343811/)

In the Parkinson's Progression Markers Initiative (372 PD, 159 controls, two timepoints), Lowes et al. (2020) replicated the reduction and linked it to **cognitive impairment**, while noting confounders (treatment, depression, insomnia, disease duration) ([PMID: 32070373](https://pubmed.ncbi.nlm.nih.gov/32070373/)).

> *"ccf-mtDNA levels appear significantly reduced in PD cases when compared to matched controls and are associated with cognitive impairment"* — [PMID: 32070373](https://pubmed.ncbi.nlm.nih.gov/32070373/)

Mechanistically, reduced release is proposed to reflect **altered neuronal mtDNA homeostasis before overt cell death** in vulnerable brain regions ([PMID: 31143191](https://pubmed.ncbi.nlm.nih.gov/31143191/)) — a finding echoed across other neurodegenerative diseases including progressive MS ([PMID: 30098422](https://pubmed.ncbi.nlm.nih.gov/30098422/)).

---

### Finding 8 — The PINK1–Parkin phospho-ubiquitin mitophagy axis links mitochondrial damage to dopaminergic neurodegeneration

Upon mitochondrial depolarization, **PINK1 (PTEN-induced kinase 1) stabilizes on the outer mitochondrial membrane (OMM), where it phosphorylates ubiquitin and Parkin at serine 65**, activating Parkin's E3-ubiquitin-ligase activity to ubiquitinate OMM substrates and trigger selective autophagic clearance (mitophagy) of damaged mitochondria ([PMID: 42490204](https://pubmed.ncbi.nlm.nih.gov/42490204/); review [PMID: 42533617](https://pubmed.ncbi.nlm.nih.gov/42533617/)). [In vitro / review]

> *"Upon mitochondrial depolarization, PINK1 stabilizes on the outer mitochondrial membrane (OMM), where it recruits and phosphorylates Parkin at serine 65"* — [PMID: 42490204](https://pubmed.ncbi.nlm.nih.gov/42490204/)

Loss-of-function *PINK1*/*PRKN* variants impair this pathway, causing **autosomal-recessive early-onset PD** ([PMID: 42368330](https://pubmed.ncbi.nlm.nih.gov/42368330/); clinical example [PMID: 40898742](https://pubmed.ncbi.nlm.nih.gov/40898742/)). PRKN-independent (receptor-mediated, lipid-mediated) mitophagy pathways provide partial compensation ([PMID: 42533617](https://pubmed.ncbi.nlm.nih.gov/42533617/)).

> *"the best-characterized PINK1-PRKN/parkin-dependent mitophagy pathway and the expanding repertoire of PRKN-independent mechanisms"* — [PMID: 42533617](https://pubmed.ncbi.nlm.nih.gov/42533617/)

A key downstream effector is **PARIS (ZNF746)**: on PINK1/parkin deficiency, PARIS accumulates and represses **PGC-1α → NRF1/TFAM**-driven mitochondrial biogenesis, driving DA neuron loss — a phenotype reversible by PINK1, parkin, or PGC-1α overexpression ([PMID: 32138754](https://pubmed.ncbi.nlm.nih.gov/32138754/)). Additional mediators include iron-sulfur cluster loss in CISD1 downstream of PINK1 loss ([PMID: 39159312](https://pubmed.ncbi.nlm.nih.gov/39159312/)).

---

## Mechanistic Model / Interpretation

Mitochondrial Parkinson disease is best understood as **multiple upstream mitochondrial insults converging on a shared downstream cascade** that selectively kills vulnerable ventral-tier SNpc dopaminergic neurons.

```
UPSTREAM TRIGGERS (heterogeneous)
┌───────────────────────────────────────────────────────────────┐
│ (a) Primary mtDNA translation defect                          │
│     m.T1095C (MT-RNR1, 12S rRNA)  ── OMIM 556500 core lesion   │
│ (b) Nuclear mtDNA-maintenance failure                         │
│     POLG / TWNK → multiple mtDNA deletions accumulate          │
│ (c) Mitophagy failure                                         │
│     PINK1 / PRKN loss-of-function (AR early-onset PD)          │
│ (d) Environmental complex I inhibitors                        │
│     MPTP/MPP+, rotenone, paraquat                             │
│ (e) mtDNA haplogroup background (risk modifier)               │
└───────────────────────────────────────────────────────────────┘
                         │
                         ▼
   CORE BIOCHEMICAL LESION: Respiratory chain deficiency
   • Complex I deficiency (stratifies ~25% iPD)
   • ↓ Complex IV (m.T1095C) / ↓ Complex II-III (cybrids)
   • ↓ ATP, ↑ ROS, ↓ mitochondrial glutathione
                         │
                         ▼
   AMPLIFYING LOOPS
   • PARIS↑ → PGC-1α/NRF1/TFAM↓ → ↓ mitochondrial biogenesis
   • CISD1 Fe-S cluster loss, iron dyshomeostasis
   • Proteasome inhibition, ubiquitin accumulation (SN)
   • α-synuclein aggregation (context-dependent crosstalk)
                         │
                         ▼
   SELECTIVE CELL DEATH
   SOX6+/AGTR1+ ventral-tier SNpc DA neurons (TP53/NR2F2 targets↑)
                         │
                         ▼
   CLINICAL MANIFESTATION
   Levodopa-responsive parkinsonism (+ deafness + neuropathy in 556500)
```

**Upstream vs downstream:** The upstream triggers are genetically/environmentally heterogeneous, but all funnel into **respiratory-chain (especially complex I) deficiency and oxidative stress**, then into failure of **mitochondrial quality control and biogenesis**, and finally into death of a **specific, molecularly-defined neuronal population**. Notably, not every mitochondrial lesion produces PD: primary mtDNA point mutations/single deletions spare the nigra, whereas **mtDNA-maintenance defects and CI deficiency** reliably produce nigral vulnerability — a critical distinction for genotype–phenotype interpretation.

### Ontology term suggestions

| Category | Suggested terms |
|---|---|
| **Genes (HGNC)** | *MT-RNR1*, *POLG*, *TWNK*(C10orf2), *PINK1*, *PRKN*, *TFAM*, *PPARGC1A*(PGC-1α), *ZNF746*(PARIS), *CISD1*, *AGTR1*, *SOX6* |
| **GO — Biological Process** | mitochondrial translation (GO:0032543); oxidative phosphorylation (GO:0006119); mitophagy (GO:0000422); mitochondrial DNA replication (GO:0006264); mitochondrion organization (GO:0007005); response to oxidative stress (GO:0006979); dopaminergic neuron differentiation (GO:0071542) |
| **GO — Cellular Component** | mitochondrion (GO:0005739); mitochondrial inner membrane (GO:0005743); mitochondrial outer membrane (GO:0005741); respiratory chain complex I (GO:0045271); mitochondrial small ribosomal subunit (GO:0005763) |
| **CL — Cell types** | dopaminergic neuron (CL:0000700); midbrain/substantia nigra DA neuron; cochlear hair cell (CL:0000589); peripheral sensory neuron |
| **UBERON — Anatomy** | substantia nigra pars compacta (UBERON:0001965); nigrostriatal tract; striatum (UBERON:0002435); midbrain (UBERON:0001891); cochlea (UBERON:0001844); peripheral nerve |
| **CHEBI — Chemicals** | levodopa (CHEBI:15765); MPTP (CHEBI:17963); rotenone (CHEBI:28201); paraquat (CHEBI:34905); coenzyme Q10 (CHEBI:46245); glutathione (CHEBI:16856); gentamicin/aminoglycoside |
| **HPO — Phenotypes** | Parkinsonism (HP:0001300); Bradykinesia (HP:0002067); Resting tremor (HP:0002322); Rigidity (HP:0002063); Sensorineural hearing impairment (HP:0000407); Peripheral neuropathy (HP:0009830); Dopa-responsive (HP:0034332); Cognitive decline (HP:0100543) |

---

## Section-by-Section Disease Characterization

### 1. Disease Information
- **Overview:** A rare, maternally inherited parkinsonism-plus syndrome caused by a heteroplasmic 12S rRNA mtDNA mutation, embodying the broader mitochondrial pathogenesis of PD.
- **Identifiers:** OMIM **556500**; MeSH "Parkinson Disease"/"Parkinsonian Disorders"; ICD-10 G20 (parkinsonism); Orphanet — mitochondrial parkinsonism spectrum. MONDO: derived from OMIM 556500.
- **Synonyms:** Mitochondrial parkinsonism; maternally inherited parkinsonism–deafness–neuropathy; parkinsonism with deafness and neuropathy (12S rRNA T1095C).
- **Source of information:** Predominantly **aggregated disease-level resources** (OMIM, single-pedigree reports, cybrid studies, meta-analyses), not EHR-derived.

### 2. Etiology
- **Causal factors:** Genetic — heteroplasmic mtDNA m.T1095C (*MT-RNR1*) for OMIM 556500; nuclear *POLG*/*TWNK*/*PINK1*/*PRKN* for related mitochondrial PD. Environmental — complex I–inhibiting toxins.
- **Genetic risk factors:** m.4336C (tRNA-Gln, OR 2.99); macrohaplogroups R/F/H (Finding 4). Nuclear susceptibility via mtDNA-maintenance and mitophagy genes.
- **Environmental risk factors:** Pesticides (rotenone, paraquat), MPTP, heavy metals (manganese), solvents, air pollution ([PMID: 42595356](https://pubmed.ncbi.nlm.nih.gov/42595356/)); aging; aminoglycoside exposure (triggers ototoxicity/apoptosis in carriers).
- **Protective factors:** mtDNA variants m.7028T (OR 0.80), m.10398G (OR 0.92), m.13368A (OR 0.74), haplogroup B (OR 0.77); J/T/U super-cluster slows cognitive progression. Exercise delays MitoPark degeneration ([PMID: 31226324](https://pubmed.ncbi.nlm.nih.gov/31226324/)).
- **Gene–environment interaction:** Manganese exacerbates degeneration in the genetically-primed MitoPark mouse ([PMID: 28595911](https://pubmed.ncbi.nlm.nih.gov/28595911/)) — a paradigm of GxE in metal neurotoxicity.

### 3. Phenotypes
| Phenotype | HPO | Onset | Progression | Frequency (556500 pedigree/related) |
|---|---|---|---|---|
| Levodopa-responsive parkinsonism | HP:0001300 | Adult | Progressive | Core feature |
| Sensorineural hearing loss | HP:0000407 | Adult, aminoglycoside-sensitive | Progressive | Core feature |
| Peripheral (sensory) neuropathy | HP:0009830 | Adult | Progressive | Core feature |
| Bradykinesia / rigidity / resting tremor | HP:0002067/0002063/0002322 | Adult | Progressive | Common |
| Cognitive decline (mtDNA-maintenance/CI-deficient subtypes) | HP:0100543 | Variable | Progressive | Subtype-dependent |

Quality-of-life impact is substantial and progressive (motor disability plus sensory/hearing loss compounding communication and mobility deficits), though disease-specific EQ-5D/SF-36 data for this rare entity are not available.

### 4. Genetic/Molecular Information
- **Causal genes:** *MT-RNR1* (m.T1095C, heteroplasmic, maternally inherited); related: *POLG*, *TWNK*, *PINK1*, *PRKN*.
- **Variant type/class:** mtDNA point mutation (rRNA); nuclear missense/frameshift/deletion (e.g., *POLG* p.R964C, p.G737R, p.Q1102P; *PRKN* exon deletions).
- **Allele frequency:** m.T1095C absent in 270 controls (Finding 1); *MT-RNR1* variants tracked in **MITOMAP**.
- **Origin/consequence:** Germline (maternal, heteroplasmic) for mtDNA; loss of function for *POLG*/*PINK1*/*PRKN*. Somatic mtDNA deletions accumulate in nigral neurons with age/disease.
- **Modifier genes:** mtDNA haplogroup background; *GBA* co-mutation reported with *POLG* ([PMID: 30941926](https://pubmed.ncbi.nlm.nih.gov/30941926/)).
- **Epigenetics/chromosomal abnormalities:** Not characterized for this specific entity (data not available).

### 5. Environmental Information
Complex I–inhibiting toxins (rotenone, paraquat, MPTP), manganese, and broader pollution/pesticide exposures are established contributors to mitochondrial-type nigral injury ([PMID: 30605763](https://pubmed.ncbi.nlm.nih.gov/30605763/); [PMID: 42595356](https://pubmed.ncbi.nlm.nih.gov/42595356/)). Aminoglycoside antibiotics are a pharmacological trigger in *MT-RNR1* carriers. No infectious agent is implicated.

### 6. Mechanism / Pathophysiology
Detailed in the Mechanistic Model above. Core pathways: **oxidative phosphorylation / respiratory chain (complex I)**, **PINK1–Parkin mitophagy**, **PGC-1α/NRF1/TFAM mitochondrial biogenesis**. Cellular processes: mitophagy, apoptosis, oxidative stress, proteostasis failure (ubiquitin accumulation in SN, [PMID: 25446449](https://pubmed.ncbi.nlm.nih.gov/25446449/)), neuroinflammation. Metabolic changes: ATP deficit, glutathione depletion, iron dyshomeostasis. Multi-omics: CI-deficient subtype has distinct cell-type-specific transcriptomes ([PMID: 38684731](https://pubmed.ncbi.nlm.nih.gov/38684731/)); single-cell profiling defines the vulnerable SOX6⁺/AGTR1⁺ population ([PMID: 35513515](https://pubmed.ncbi.nlm.nih.gov/35513515/)).

### 7. Anatomical Structures Affected
- **Primary organ/system:** Nervous system — substantia nigra pars compacta and nigrostriatal pathway (UBERON:0001965); striatum (UBERON:0002435).
- **Secondary:** Cochlea/auditory system (UBERON:0001844); peripheral nerves.
- **Cell level:** Ventral-tier SNpc dopaminergic neurons (CL:0000700; SOX6⁺/AGTR1⁺); cochlear hair cells; peripheral sensory neurons.
- **Subcellular:** Mitochondrion (GO:0005739), inner/outer membranes, respiratory chain complex I (GO:0045271), mitochondrial ribosome.
- **Lateralization:** Parkinsonism typically begins asymmetric, becoming bilateral.

### 8. Temporal Development
Adult-onset, insidious, chronic, and progressive. mtDNA deletion load and CI deficiency accumulate over years; the CI-deficient subtype is more widespread/non-tremor-dominant. No spontaneous remission; symptomatic treatment-induced improvement only. Aging is the principal critical modifier.

### 9. Inheritance and Population
- **Inheritance:** **Mitochondrial/maternal** (OMIM 556500, heteroplasmic → variable expressivity and incomplete/tissue-dependent penetrance). Related forms: autosomal recessive (*POLG*, *PINK1*, *PRKN*).
- **Heteroplasmy** drives variable severity and complicates prediction ([PMID: 32187761](https://pubmed.ncbi.nlm.nih.gov/32187761/)).
- **Epidemiology:** OMIM 556500 is ultra-rare (single/few pedigrees). Broader mitochondrial contributions modulate PD (global prevalence ~0.3%). Haplogroup effects are population-specific (Finding 4).
- **Sex/geography:** Not specifically established for this entity; PD overall shows male predominance.

### 10. Diagnostics
- **Genetic testing:** **mtDNA sequencing** (MITOMAP/MSeqDR) for *MT-RNR1* m.T1095C with heteroplasmy quantification; nuclear gene panels/WES/WGS for *POLG*/*TWNK*/*PINK1*/*PRKN*.
- **Biochemistry:** Respiratory chain enzymology (↓ complex IV in m.T1095C; ↓ complex I in CI-deficient PD).
- **Imaging:** DAT-SPECT showing nigrostriatal deficit ([PMID: 26979109](https://pubmed.ncbi.nlm.nih.gov/26979109/)); PET.
- **Candidate biomarker:** Reduced **CSF ccf-mtDNA** (Finding 7).
- **Differential diagnosis:** Idiopathic PD; other genetic parkinsonisms; *POLG* spectrum (progressive external ophthalmoplegia, ataxia, neuropathy); consider *COA7*-related dystonia-parkinsonism ([PMID: 37750949](https://pubmed.ncbi.nlm.nih.gov/37750949/)). Distinguishing features: maternal transmission + deafness + neuropathy suggests mtDNA/*MT-RNR1*; sensory neuropathy + dystonia suggests *POLG*.

### 11. Outcome/Prognosis
Chronic, progressive disability. Levodopa responsiveness is generally preserved early but motor fluctuations and dyskinesias develop; cognitive decline marks the mtDNA-maintenance/CI-deficient course. Haplogroup J/T/U predicts slower cognitive progression ([PMID: 36343661](https://pubmed.ncbi.nlm.nih.gov/36343661/)). Reduced CSF ccf-mtDNA associates with cognitive impairment ([PMID: 32070373](https://pubmed.ncbi.nlm.nih.gov/32070373/)). No disease-specific survival statistics are available for OMIM 556500.

### 12. Treatment
- **Pharmacotherapy:** **Levodopa/carbidopa** (NCIT: Levodopa); dopamine agonists; MAO-B inhibitors. Symptomatic response is typical.
- **Surgical/interventional:** **Deep brain stimulation** (subthalamic nucleus) for motor fluctuations ([PMID: 40898742](https://pubmed.ncbi.nlm.nih.gov/40898742/)).
- **Pharmacogenomics:** **Avoid aminoglycosides** in *MT-RNR1* carriers (apoptosis hypersensitivity, [PMID: 22735573](https://pubmed.ncbi.nlm.nih.gov/22735573/)); avoid valproate in *POLG* disease (hepatotoxicity risk).
- **Investigational/mitochondrial-targeted:** Coenzyme Q10 in genetically-stratified subgroups ([PMID: 33324897](https://pubmed.ncbi.nlm.nih.gov/33324897/)); mito-metformin/PKD1-PGC-1α activation (preclinical, [PMID: 38449738](https://pubmed.ncbi.nlm.nih.gov/38449738/)); RAAS inhibitors (preclinical/epidemiological, [PMID: 34550070](https://pubmed.ncbi.nlm.nih.gov/34550070/)); hypoxia therapy (preclinical, [PMID: 40770507](https://pubmed.ncbi.nlm.nih.gov/40770507/)); MSC/cell therapy (investigational, [PMID: 41982578](https://pubmed.ncbi.nlm.nih.gov/41982578/)). No disease-modifying therapy is proven ([PMID: 26208210](https://pubmed.ncbi.nlm.nih.gov/26208210/)).
- **Supportive:** Hearing aids/cochlear support, neuropathy management, physiotherapy; **exercise** shows benefit in models.

### 13. Prevention
- **Primary:** Avoidance of complex I–inhibiting toxins and aminoglycosides in at-risk individuals; exercise.
- **Secondary:** DAT imaging / CSF ccf-mtDNA for early detection in at-risk maternal relatives (research-stage).
- **Genetic counseling:** Essential given **maternal transmission and heteroplasmy** — recurrence risk and severity are difficult to predict; mitochondrial replacement/PGD are theoretical options for maternal mtDNA disease ([PMID: 29418047](https://pubmed.ncbi.nlm.nih.gov/29418047/)).
- No immunization or infectious control applicable.

### 14. Other Species / Natural Disease
No naturally occurring homolog of this specific mtDNA disease is documented in companion animals (data not available in OMIA for m.T1095C). Orthologs of nuclear genes are highly conserved (*Pink1*, *prkn*, *Polg*, *Tfam*) across mouse, rat, zebrafish, and *Drosophila*, enabling cross-species modeling. Mitophagy mechanisms are evolutionarily conserved ([PMID: 42533617](https://pubmed.ncbi.nlm.nih.gov/42533617/)).

### 15. Model Organisms
| Model | Type | Lesion | Recapitulation | Key limitation |
|---|---|---|---|---|
| MitoPark mouse | Mammalian genetic | DAT-Cre *TFAM* KO | Progressive adult DA loss, motor decline, GxE (Mn), exercise-responsive | Not the human mtDNA lesion |
| Mutator/Deletor/PD-mitoPstI/TwinkPark | Mammalian genetic | mtDNA-maintenance | Nigrostriatal degeneration, deletion load | Variable nigral penetrance |
| MPTP / rotenone / 6-OHDA / paraquat | Toxin (mouse/rat) | Complex I inhibition | Nigral DA loss, motor deficits; rotenone → Lewy-body-like | Acute; incomplete pathology |
| *Drosophila* Pink1/parkin | Invertebrate genetic | Mitophagy/biogenesis failure | Mitochondrial defects, DA loss, motor deficits, PARIS/PGC-1α axis | Simplified nervous system |
| Patient iPSC-derived DA neurons | In vitro human | PINK1/PRKN mutation | Impaired mitochondrial clearance, ROS, apoptosis | Lacks aging/circuit context |
| Zebrafish DA-ablation | Vertebrate | Mitochondrial dysfunction | High-content neuroprotection screening | Not spontaneous PD |

Resources: MGI, RGD, ZFIN, FlyBase, IMSR, Cellosaurus.

---

## Evidence Base

| PMID | Role | Support/Challenge |
|---|---|---|
| [11079536](https://pubmed.ncbi.nlm.nih.gov/11079536/) | Defines OMIM 556500 causal mutation (m.T1095C) | **Supports** F001 (foundational) |
| [22735573](https://pubmed.ncbi.nlm.nih.gov/22735573/) | Cybrid functional confirmation | **Supports** F001 |
| [26979109](https://pubmed.ncbi.nlm.nih.gov/26979109/) | DAT imaging across mito disorders | **Supports** F002 (selective nigral vulnerability to maintenance defects) |
| [35114397](https://pubmed.ncbi.nlm.nih.gov/35114397/) | mtDNA homeostasis review | **Supports** F002/F005 |
| [34062649](https://pubmed.ncbi.nlm.nih.gov/34062649/) | POLG dystonia/neuropathy | **Supports** F002 (diagnostic clue) |
| [8420145](https://pubmed.ncbi.nlm.nih.gov/8420145/) | CI deficiency in PD SN (landmark) | **Supports** F003 |
| [38684731](https://pubmed.ncbi.nlm.nih.gov/38684731/) | CI-deficiency stratifies iPD | **Supports** F003 |
| [29270838](https://pubmed.ncbi.nlm.nih.gov/29270838/) | Widespread neuronal CI deficiency | **Supports** F003; **nuances** causality |
| [38917640](https://pubmed.ncbi.nlm.nih.gov/38917640/) | Meta-analysis of mtDNA variants | **Supports** F004 |
| [36343661](https://pubmed.ncbi.nlm.nih.gov/36343661/) | Haplogroup & cognitive progression | **Supports** F004 |
| [8104867](https://pubmed.ncbi.nlm.nih.gov/8104867/) | np4336 tRNA-Gln enrichment | **Supports** F004 |
| [20356410](https://pubmed.ncbi.nlm.nih.gov/20356410/); [33904476](https://pubmed.ncbi.nlm.nih.gov/33904476/) | Null haplogroup associations | **Challenge** F004 (population-specificity) |
| [28595911](https://pubmed.ncbi.nlm.nih.gov/28595911/) | MitoPark + manganese GxE | **Supports** F005 |
| [32470327](https://pubmed.ncbi.nlm.nih.gov/32470327/) | iPSC PINK1/Parkin model | **Supports** F005/F008 |
| [35513515](https://pubmed.ncbi.nlm.nih.gov/35513515/) | SOX6/AGTR1 vulnerable subtype | **Supports** F006 |
| [38587883](https://pubmed.ncbi.nlm.nih.gov/38587883/) | Mouse mDA vulnerability atlas | **Supports** F006 |
| [26343811](https://pubmed.ncbi.nlm.nih.gov/26343811/) | CSF ccf-mtDNA biomarker | **Supports** F007 |
| [32070373](https://pubmed.ncbi.nlm.nih.gov/32070373/) | PPMI replication of ccf-mtDNA | **Supports** F007; notes confounders |
| [42490204](https://pubmed.ncbi.nlm.nih.gov/42490204/); [42533617](https://pubmed.ncbi.nlm.nih.gov/42533617/) | PINK1-Parkin mechanism/review | **Supports** F008 |
| [32138754](https://pubmed.ncbi.nlm.nih.gov/32138754/) | PARIS/PGC-1α axis | **Supports** F008 |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity of OMIM 556500.** The core entity rests largely on a single well-characterized pedigree plus cybrid work; genotype–phenotype breadth, penetrance, sex ratio, prevalence, and survival statistics are essentially unquantified.
2. **Heteroplasmy and tissue segregation** make prediction of onset/severity and recurrence risk difficult, and complicate genetic counseling.
3. **mtDNA association heterogeneity.** Haplogroup/variant effects are population-specific and inconsistently replicated ([PMID: 20356410](https://pubmed.ncbi.nlm.nih.gov/20356410/); [PMID: 33904476](https://pubmed.ncbi.nlm.nih.gov/33904476/); [PMID: 31233840](https://pubmed.ncbi.nlm.nih.gov/31233840/)).
4. **Causality vs consequence of CI deficiency.** Widespread neuronal CI deficiency in regions spared from degeneration ([PMID: 29270838](https://pubmed.ncbi.nlm.nih.gov/29270838/)) indicates CI deficiency alone is insufficient for cell death; additional "second hits" (α-synuclein, proteostasis, cell-intrinsic vulnerability) are required.
5. **Biomarker confounders.** CSF ccf-mtDNA is influenced by treatment, comorbidity, and disease duration; not yet clinically validated.
6. **Therapeutic gap.** No disease-modifying therapy is proven; mitochondrial-enhancer trials have largely been negative or remain early-stage.
7. **No documented natural animal homolog** of the m.T1095C disease; model organisms capture pathway biology but not the exact mtDNA lesion or human aging context.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype expansion:** Query MITOMAP/MSeqDR and international mitochondrial-disease registries for additional *MT-RNR1* m.T1095C carriers to quantify penetrance, heteroplasmy thresholds, and the deafness–neuropathy–parkinsonism co-occurrence rate.
2. **Heteroplasmy–phenotype correlation:** Single-cell heteroplasmy quantification in patient-derived neurons/tissues to define the threshold for respiratory failure and DA-neuron death.
3. **Targeted iPSC modeling:** Generate m.T1095C cybrids/iPSC-derived ventral A9-like DA neurons ([PMID: 41279649](https://pubmed.ncbi.nlm.nih.gov/41279649/)) to test whether the mutation preferentially injures SOX6⁺/AGTR1⁺ neurons and whether glutathione or CoQ10 supplementation rescues them.
4. **Biomarker validation:** Prospective longitudinal CSF ccf-mtDNA measurement in defined mitochondrial-PD carriers vs idiopathic PD to establish specificity and predictive value for progression.
5. **Stratified therapeutics:** Advance mitochondrial-enhancer (CoQ10, PGC-1α activators, mito-metformin) and RAAS-inhibitor trials specifically in CI-deficient / mtDNA-defined PD subgroups.
6. **Pharmacovigilance flag:** Establish an alert to contraindicate aminoglycosides in *MT-RNR1* variant carriers and valproate in *POLG* patients.

---

## Consensus Answer

Parkinson Disease, Mitochondrial (OMIM 556500) is a rare maternally inherited parkinsonism caused by a heteroplasmic 12S rRNA point mutation (m.T1095C in *MT-RNR1*) that impairs mitochondrial protein synthesis and oxidative phosphorylation, producing levodopa-responsive parkinsonism, aminoglycoside-sensitive sensorineural deafness, and peripheral neuropathy. It exemplifies the broader central role of mitochondrial dysfunction in PD — complex I deficiency (stratifying ~25% of idiopathic cases), nuclear mtDNA-maintenance failure (*POLG*/*TWNK*), and defective PINK1–Parkin mitophagy (*PINK1*/*PRKN*) — that drives selective loss of molecularly-defined SOX6⁺/AGTR1⁺ ventral-tier substantia nigra dopaminergic neurons, with mtDNA haplogroups modulating sporadic risk and progression; management is symptomatic with no proven disease-modifying therapy.


## Artifacts

- [OpenScientist final report](Parkinson_Disease_Mitochondrial-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Parkinson_Disease_Mitochondrial-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.