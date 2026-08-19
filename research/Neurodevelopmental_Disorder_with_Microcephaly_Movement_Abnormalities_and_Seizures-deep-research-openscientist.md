---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-18T15:06:09.190704'
end_time: '2026-08-18T15:26:42.483177'
duration_seconds: 1233.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities,
    and Seizures
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
citation_count: 6
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_with_Microcephaly_Movement_Abnormalities_and_Seizures-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_with_Microcephaly_Movement_Abnormalities_and_Seizures-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures** covering all of the
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

# Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures (NEDMIMS): A Comprehensive Disease Characterization

**Disease:** Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures (NEDMIMS)
**OMIM:** #620023 · **MONDO:** MONDO:0859282 · **UMLS:** C5774208 · **Causal gene:** *CHKA* (choline kinase alpha, 11q13.2) · **Category:** Mendelian (autosomal recessive)

> **Evidence caveat.** This is an ultra-rare, recently delineated Mendelian disorder. Almost all *disease-specific* clinical statements derive from a single primary report of six individuals from five families ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)). Mechanistic, model-organism, and pathway statements draw on broader choline-kinase / Kennedy-pathway literature. Where information does not exist, this is stated explicitly.

---

## Summary

Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures (**NEDMIMS**, OMIM **#620023**) is an ultra-rare, autosomal recessive Mendelian disorder caused by **biallelic (homozygous or compound heterozygous) loss-of-function/hypomorphic variants in *CHKA***, the gene encoding **choline kinase alpha** on chromosome 11q13.2. The disease was first delineated by Klöckner and colleagues in 2022, who reported six affected individuals from five unrelated families ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)). CHKA catalyzes the **first committed step of the CDP-choline (Kennedy) pathway** — the ATP-dependent phosphorylation of choline to phosphocholine — the rate-influencing entry point for de novo synthesis of **phosphatidylcholine (PC)**, the most abundant phospholipid of eukaryotic cell membranes. Disease variants reduce CHKA enzymatic activity, starving the developing brain of membrane phospholipid supply.

The clinical phenotype is severe and highly stereotyped: **fully penetrant microcephaly, severe-to-profound global developmental delay with absent speech, early-onset refractory epileptic encephalopathy, and a mixed movement disorder** combining spasticity/hypertonia with hyperkinetic features (dyskinesia, choreoathetosis). Additional features include hyperreflexia, inability to walk, short stature, nystagmus, aggressive and self-injurious behavior, scoliosis, and — on neuroimaging — CNS hypomyelination and thin corpus callosum. Onset is congenital-to-infantile. There is no biochemical diagnostic marker; diagnosis relies on **exome or genome sequencing**. Management is entirely **supportive** (anti-seizure medications, spasticity/movement management, physical/occupational/speech therapy, orthopedic and feeding support); no disease-specific or curative therapy exists.

Mechanistically, NEDMIMS joins a growing family of "**Kennedy-pathway disorders**" (alongside *CHKB*, *PCYT1A*, *PCYT2*, and *SELENOI* diseases). Because complete *Chka* knockout is embryonic lethal in mice, human disease alleles are necessarily **hypomorphic** (partial loss of function), not null. Functional validation in yeast complementation assays and structural modeling confirmed reduced catalytic activity of disease variants. The successful AAV-mediated gene-therapy rescue of the paralogous *Chkb* (rmd) mouse suggests phospholipid-pathway defects are therapeutically tractable in principle, offering a rationale for future disease-modifying strategies.

---

## Key Findings

### Finding 1 — Disease identity: NEDMIMS is caused by biallelic *CHKA* variants
NEDMIMS (OMIM **#620023**) was established by Klöckner et al. (2022, *Brain*), who identified **six individuals from five unrelated families** carrying bi-allelic variants in *CHKA* (gene MIM 118491; 11q13.2). Inheritance is **autosomal recessive**. The authors state: *"We identified six individuals from five families with bi-allelic variants in CHKA presenting with severe global developmental delay, epilepsy, movement disorders and microcephaly"* ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)). The four cardinal features give the disorder its name. Yeast complementation and structural modeling showed the variants *"reduce the enzymatic activity of CHKA and confer a significant impairment of the first enzymatic step of the Kennedy pathway,"* establishing a **loss-of-function mechanism**.

### Finding 2 — CHKA loss cripples the CDP-choline (Kennedy) pathway
Choline kinase (isoforms CHKα/CHKβ) catalyzes **ATP + choline → ADP + phosphocholine**, the first committed step of de novo PC synthesis; phosphocholine is converted to **CDP-choline** (PCYT1A/B) and then to **phosphatidylcholine**. Klöckner et al. note: *"The Kennedy pathways catalyse the de novo synthesis of phosphatidylcholine and phosphatidylethanolamine, the most abundant components of eukaryotic cell membranes"* ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)). This is corroborated by Chen et al.: *"Choline kinases possess enzyme activity that catalyses the conversion of choline to phosphocholine, which is further converted to cytidine diphosphate-coline (CDP-choline) in the biosynthesis of phosphatidylcholine (PC)"* ([PMID: 27769579](https://pubmed.ncbi.nlm.nih.gov/27769579/)). **Four of ten Kennedy-pathway genes** were already disease-associated before NEDMIMS: *CHKB* (megaconial muscular dystrophy), *PCYT1A* (cone-rod dystrophy/bone), *PCYT2* and *SELENOI* (spastic paraplegia).

### Finding 3 — *CHKA* is not haploinsufficient, consistent with recessive disease
gnomAD constraint for *CHKA* (ENSG00000110721): **pLI ≈ 4.3×10⁻⁶**, observed/expected LoF = **0.57 (90% CI 0.43–0.75; LOEUF 0.75)**, LoF Z = 2.86, missense Z ≈ 0. Heterozygous loss-of-function is **tolerated** in the general population (carriers unaffected); disease requires **biallelic** variants — fully consistent with autosomal recessive inheritance and the disorder's ultra-rarity/consanguinity association.

### Finding 4 — Complete Chka loss is embryonic lethal; disease alleles are hypomorphic
Wu et al.: *"Disruption of murine Chka leads to embryonic lethality, whereas a spontaneous genomic deletion in murine Chkb results in neonatal forelimb bone deformity and hindlimb muscular dystrophy"* ([PMID: 20026284](https://pubmed.ncbi.nlm.nih.gov/20026284/)). Because a null *Chka* genotype is incompatible with life in mice, viable **human disease alleles must retain residual activity (hypomorphic)**. The paralogous disorder offers a therapeutic proof-of-concept: *"Intramuscular gene therapy post-disease onset using an adeno-associated viral 6 (AAV6) vector carrying a functional copy of Chkb is also capable of rescuing the dystrophy phenotype"* ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)). Human variants were additionally validated by **yeast (S. cerevisiae) complementation**.

### Finding 5 — Full phenotype spectrum with HPO frequencies (n=6, Klöckner 2022)
Fully penetrant core features (6/6, 100%): microcephaly (HP:0000252), severe global developmental delay (HP:0011344), delayed gross motor development (HP:0002194), absent speech (HP:0001344), epileptic encephalopathy (HP:0200134), hypertonia (HP:0001276). Highly frequent: hyperreflexia (HP:0001347, 5/5), inability to walk (HP:0002540, 5/6). Common: infantile onset (HP:0003593, 4/6), short stature (HP:0004322, 4/6), nystagmus (HP:0000639, 3/6), aggressive behavior (HP:0000718, 3/6), scoliosis (HP:0002650, 3/6). Movement axis: dyskinesia (HP:0100660, 2/6), choreoathetosis (HP:0001266, 1/6), rigidity (HP:0002063, 1/6). Less frequent (1/6): self-injury (HP:0100716), sleep disturbance (HP:0002360), autistic behavior (HP:0000729), hyperactivity (HP:0000752), cerebral visual impairment (HP:0100704), feeding difficulties (HP:0011968), high palate (HP:0000218), kidney stone (HP:0000787). Neuroimaging: CNS hypomyelination (HP:0003429, 2/5), thin corpus callosum (HP:0033725, 1/5). Source: *"…severe global developmental delay, epilepsy, movement disorders and microcephaly"* ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)).

### Finding 6 — *CHKA* pathogenic variant spectrum (ClinVar; NM_001277.3)
Pathogenic/Likely-pathogenic NEDMIMS variants span classes: **c.1030G>T p.(Gly344Ter)** (nonsense); **c.14dup p.(Cys6fs)** (frameshift); **c.1021T>C p.(Phe341Leu)**, **c.580C>T p.(Pro194Ser)**, **c.421C>T p.(Arg141Trp)** (missense). Full *CHKA* ClinVar record (94 entries): **7 Pathogenic, 10 Likely pathogenic, 54 VUS, 5 Likely benign** — though many "Pathogenic" entries are large 11q contiguous-gene CNVs, not NEDMIMS-specific. Variants are **germline, biallelic**; consequence is **loss-of-function / reduced choline kinase activity (hypomorphic)**.

### Finding 7 — CHKA protein: cytosolic choline/ethanolamine kinase
CHKA (UniProt **P35790**; HGNC:1937; NCBIGene:1119; ENSG00000110721; 11q13.2). Reactions: choline + ATP → phosphocholine + ADP (**GO:0004103**) and ethanolamine + ATP → phosphoethanolamine + ADP (**GO:0004305**). Processes: PC biosynthesis (**GO:0006656**), CDP-choline pathway (**GO:0006657**), PE biosynthesis (**GO:0006646**). Localization: cytosol (**GO:0005829**), cytoplasm (**GO:0005737**), lipid droplet (**GO:0005811**). CHEBI entities: choline (CHEBI:15354), ATP (CHEBI:30616), phosphocholine (CHEBI:295975), CDP-choline (CHEBI:16436), phosphatidylcholine (CHEBI:16110), ethanolamine (CHEBI:57603).

### Finding 8 — Orthologs and pathway memberships
*CHKA* (HomoloGene 88575) orthologs: mouse *Chka* (12660), rat *Chka* (29194), zebrafish *chka* (558499), *C. elegans* (180703), plus dog/cow/chicken/chimp. Pathways: KEGG **hsa00564** (glycerophospholipid metabolism), **hsa05231** (choline metabolism in cancer); WikiPathways **WP3933** (Kennedy pathway); Reactome **R-HSA-1483191** (synthesis of PC). No naturally occurring *CHKA*-equivalent disease is catalogued in OMIA for domestic animals.

### Finding 9 — Rich experimental structural data for variant mapping
Human CHKα (457 aa) has **≥5 high-resolution PDB structures** (2IG7, 2CKQ, 2CKO, 3F2R, 2CKP). Architecture: **disordered N-terminal region (~res 1–86)** + **choline/ethanolamine kinase catalytic domain (~res 80–457)**; ATP/substrate-contacting residues include 117–123, 119–121, 146, 207–213, 308, 330. NEDMIMS missense variants (**p.Arg141Trp, p.Pro194Ser, p.Phe341Leu**) fall **within/adjacent to the catalytic domain**, structurally consistent with the measured reduction in activity ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)).

---

## Mechanistic Model / Interpretation

### Causal chain

```
Biallelic hypomorphic CHKA variants (missense / nonsense / frameshift)
        │  (null is embryonic-lethal → alleles retain residual activity)
        ▼
Reduced choline kinase activity
        │  ATP + choline ──X──▶ phosphocholine   (first committed step)
        ▼
Impaired CDP-choline (Kennedy) pathway flux
        ▼
Deficient de novo phosphatidylcholine (± phosphatidylethanolamine) synthesis
        │  PC = most abundant membrane phospholipid
        ▼
Inadequate membrane phospholipid supply in the developing CNS
        │  (neuronal membrane biogenesis, myelination, synaptogenesis)
        ▼
┌─────────────────────────────────────────────────────────────┐
│ Microcephaly  │ Hypomyelination/thin CC │ Epileptic          │
│ (HP:0000252)  │ (HP:0003429/HP:0033725) │ encephalopathy     │
│               │                         │ (HP:0200134)       │
│ Severe global DD / absent speech (HP:0011344 / HP:0001344)   │
│ Mixed movement disorder: hypertonia + dyskinesia/chorea      │
│ (HP:0001276 / HP:0100660 / HP:0001266)                       │
└─────────────────────────────────────────────────────────────┘
```

**Upstream vs downstream.** The upstream trigger is the genetic lesion reducing CHKA catalytic output; the immediate downstream node is diminished phosphocholine production and reduced Kennedy-pathway flux to PC. Distal clinical consequences (microcephaly, hypomyelination, seizures, movement disorder) reflect the developing brain's exceptional dependence on continuous membrane phospholipid biosynthesis for neuronal proliferation, axonal/dendritic membrane expansion, and myelin production. CHKA's bifunctional ethanolamine kinase activity (GO:0004305) means PE synthesis may also be partly compromised, compounding the deficit.

### Placement within the Kennedy-pathway disorder family

| Gene | Enzyme / step | Associated disorder | Relationship to NEDMIMS |
|------|---------------|---------------------|-------------------------|
| **CHKA** | Choline kinase α (step 1, choline branch) | **NEDMIMS (OMIM #620023)** | Index disorder |
| *CHKB* | Choline kinase β (step 1, muscle-predominant) | Megaconial congenital muscular dystrophy | Shares ID/DD/behavioral features; muscle-predominant, megaconial mitochondria ([PMID: 23945283](https://pubmed.ncbi.nlm.nih.gov/23945283/)) |
| *PCYT1A* | CTP:phosphocholine cytidylyltransferase (step 2) | Cone-rod dystrophy, skeletal disease | Downstream, same pathway |
| *PCYT2* | Ethanolamine-branch cytidylyltransferase | Hereditary spastic paraplegia | Spasticity overlap |
| *SELENOI* | Ethanolaminephosphotransferase | Hereditary spastic paraplegia | Spasticity overlap |

The **tissue-specific expression of the two paralogs** (Wu et al., [PMID: 20026284](https://pubmed.ncbi.nlm.nih.gov/20026284/)) explains why α-isoform loss manifests as a neurodevelopmental (rather than myopathic) disease. Cell types: **neurons (CL:0000540)**, **oligodendrocytes (CL:0000128**; hypomyelination), and neural progenitors (microcephaly). Subcellular convergence: cytosolic phosphorylation (GO:0005829) → ER-based PC assembly → deficient plasma-membrane / myelin phospholipid.

---

## Section-by-Section Disease Characterization

### 1. Disease Information
- **Overview:** ultra-rare autosomal recessive Mendelian neurodevelopmental disorder defined by microcephaly, severe global developmental delay, epileptic encephalopathy, and a mixed movement disorder, caused by biallelic *CHKA* variants that impair phosphatidylcholine biosynthesis.
- **Identifiers:** OMIM **#620023**; gene OMIM 118491; MONDO **:0859282**; UMLS **C5774208**; MedGen linked; HGNC:1937; NCBIGene:1119; Ensembl ENSG00000110721; UniProt P35790. **No dedicated Orphanet, ICD-10/ICD-11, or MeSH code** was identified (maps to broad categories: ICD-10 Q02 microcephaly / G40 epilepsy / F79 intellectual disability).
- **Synonyms:** NEDMIMS; CHKA-related neurodevelopmental disorder; CHKA-related developmental and epileptic encephalopathy with microcephaly; choline kinase alpha deficiency (neurodevelopmental form).
- **Source type:** aggregated disease-level knowledge from an individual-patient case series (n=6), not EHR/registry data.

### 2. Etiology
- **Causal factor:** purely **genetic** — biallelic hypomorphic loss-of-function variants in *CHKA*; no environmental/infectious cause. Klöckner et al. showed variants *"reduce the enzymatic activity of CHKA"* ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)).
- **Genetic risk factors:** inheriting two damaging *CHKA* alleles; **consanguinity/founder homozygosity** is the dominant risk context. *CHKA* is not haploinsufficient (pLI≈0), so carriers are unaffected. No proven modifier genes (paralog *CHKB* and downstream *PCYT1A/PCYT2/SELENOI/CHPT1/CEPT1* are plausible but unproven modifiers).
- **Environmental/protective factors:** none established. **Dietary choline** is a theoretical (untested) substrate-supply modifier.
- **Gene–environment interactions:** none documented.

### 3. Phenotypes
See Finding 5 for the HPO-annotated frequency profile. Phenotype types span clinical signs (microcephaly, hypertonia, hyperreflexia), developmental deficits (global DD, absent speech, inability to walk), behavioral changes (aggression, self-injury, autistic behavior, hyperactivity, sleep disturbance), and neuroimaging abnormalities (hypomyelination, thin corpus callosum). **Onset:** infantile (4/6) to childhood (2/6). **Severity:** severe-to-profound. **Progression:** developmental delay static-to-slowly-progressive; microcephaly progressive/postnatal; epilepsy often refractory. **Laboratory:** no diagnostic biochemical marker. **QoL impact:** profound — non-verbal, non-ambulatory in most, lifelong dependent care; no disease-specific QoL instrument data.

### 4. Genetic / Molecular Information
- **Causal gene:** *CHKA* (HGNC:1937; MIM 118491; 11q13.2; NM_001277.3 / NP_001268.1). See Finding 6 for variants.
- **Classification landscape:** 94 ClinVar records (7 P, 10 LP, 54 VUS, 5 LB); ACMG/AMP-based, supported by functional data + rarity + recessive segregation.
- **Allele frequency:** ultra-rare/absent in gnomAD; heterozygous LoF tolerated.
- **Origin:** germline, biallelic (CHKA somatic overactivity is a *cancer* phenomenon, not relevant here).
- **Functional consequence:** loss-of-function/hypomorphic; not gain-of-function or dominant-negative.
- **Modifier/epigenetic/chromosomal:** none NEDMIMS-specific; large 11q13 CNVs cause distinct contiguous-gene phenotypes.

### 5. Environmental Information
Not applicable — no toxic, lifestyle, or infectious contributors. (Diagnostic pitfall: intracranial calcifications in the broader spectrum can mimic congenital TORCH infection.)

### 6. Mechanism / Pathophysiology
Detailed above. Pathway: **CDP-choline / Kennedy pathway** (WP3933; KEGG hsa00564; Reactome R-HSA-1483191). Core defect: reduced **choline kinase activity (GO:0004103)** → impaired **PC biosynthesis (GO:0006656)**. Protein dysfunction: hypomorphic activity reduction with disease missense residues mapping to the catalytic domain (PDB 2IG7, 2CKQ, etc.). CHKA also has a non-catalytic scaffolding role (binds c-Src SH3 via its poly-proline region, [PMID: 31745227](https://pubmed.ncbi.nlm.nih.gov/31745227/)); relevance to NEDMIMS unproven. No immune, infectious, or storage component. **No patient-level omics** (transcriptomic/proteomic/lipidomic) published; predicted lipidomic signature = reduced PC species.

### 7. Anatomical Structures Affected
- **Organ/system:** brain/CNS (UBERON:0000955, UBERON:0001017) — cortex (UBERON:0000956), white matter (UBERON:0002316), corpus callosum (UBERON:0002336); secondary skeletal (scoliosis; UBERON:0001130), growth, occasional renal.
- **Tissue/cell:** nervous tissue — neurons (CL:0000540), oligodendrocytes (CL:0000128; hypomyelination); no primary muscle pathology (contrast *CHKB*).
- **Subcellular:** cytosol (GO:0005829), lipid droplet (GO:0005811); pathology converges on cellular membranes (ER GO:0005783, plasma/myelin membrane).
- **Localization:** bilateral, symmetric, diffuse; not focal.

### 8. Temporal Development
- **Onset:** congenital-to-infantile (HP:0003593 4/6; childhood HP:0011463 2/6); chronic/insidious-developmental, with epilepsy sometimes acute in presentation.
- **Progression:** static-to-slowly-progressive developmental deficits; progressive microcephaly; often refractory epileptic encephalopathy; no discrete stages.
- **Course/duration:** chronic, lifelong, non-remitting; no spontaneous remission of core disability.
- **Critical period:** prenatal–early-postnatal brain growth/myelination window — the theoretical window for metabolic intervention.

### 9. Inheritance and Population
- **Inheritance:** autosomal recessive (HP:0000007); biallelic (homozygous or compound heterozygous).
- **Penetrance:** complete for the core tetrad in reported biallelic cases (small denominator). **Expressivity:** variable for secondary features.
- **Anticipation/mosaicism:** not applicable (not a repeat disorder).
- **Founder/consanguinity:** consanguinity central; likely private/founder alleles per family rather than one global founder.
- **Carrier frequency:** not formally estimated; expected very low.
- **Epidemiology:** ultra-rare; prevalence/incidence not established (<~10 individuals reported; 6 in the defining paper). **Demographics:** reported families of Middle Eastern/North African/South Asian background (ascertainment via homozygosity); no sex bias expected (autosomal); pediatric diagnosis.

### 10. Diagnostics
- **Genetic testing is definitive:** trio **WES/WGS** or a neurodevelopmental/epilepsy/microcephaly gene panel including *CHKA*; confirm biallelic status + segregation. **GeneMatcher** enabled cohort assembly. CMA/karyotype/FISH help exclude 11q CNVs but are typically **normal** in NEDMIMS. mtDNA/repeat testing not indicated.
- **No biochemical biomarker;** routine metabolic screens unrevealing.
- **Imaging:** brain MRI may be normal or show hypomyelination/leukoencephalopathy, thin corpus callosum, ventriculomegaly, cortical abnormalities (± calcifications on CT). **EEG:** epileptiform/encephalopathic patterns. Serial head-circumference documents progressive microcephaly.
- **Differential diagnosis:** other Kennedy-pathway disorders (*CHKB* megaconial dystrophy — muscle-predominant, megaconial mitochondria; *PCYT2/SELENOI* HSP; *PCYT1A* retinal/skeletal), *PPFIBP1*-related disorder (microcephaly + periventricular calcifications), primary microcephaly (MCPH) genes, congenital TORCH infections, other early-infantile DEEs, hypomyelinating leukodystrophies.
- **Screening:** not part of newborn screening; carrier/cascade and prenatal/PGT-M feasible for known biallelic families.

### 11. Outcome / Prognosis
- **Function:** severe-to-profound; most non-ambulatory (inability to walk 5/6) and non-verbal (absent speech 6/6) with refractory epilepsy → lifelong dependence (ICF: severe limitations in mobility, communication, self-care).
- **Survival/mortality:** not systematically quantified; early-onset refractory epileptic encephalopathy carries elevated risk (including generic SUDEP risk). Long-term life expectancy undetermined.
- **Complications:** refractory seizures, aspiration/feeding difficulties, failure to thrive/short stature, scoliosis, contractures, behavioral/self-injury and sleep problems, cerebral visual impairment, rare nephrolithiasis.
- **Recovery potential:** none for core deficit (irreversible developmental involvement).
- **Prognostic factors:** presumed correlation of residual CHKA activity (allele severity) and seizure control with outcome — plausible, not statistically established. No validated prognostic biomarker.

### 12. Treatment
**No disease-specific or curative therapy.** Management is symptomatic, supportive, multidisciplinary.
- **Pharmacotherapy:** anti-seizure medications (NCIT: Anticonvulsant Agent); spasticity/movement agents (baclofen, trihexyphenidyl, focal botulinum toxin); behavioral/sleep management. No CHKA-specific pharmacogenomics.
- **Advanced/experimental (conceptual only):** **choline/CDP-choline (citicoline)** substrate supplementation — precedent in the paralogous *CHKB* disorder (Chen et al. propose CDP-choline supplementation may be beneficial, [PMID: 27769579](https://pubmed.ncbi.nlm.nih.gov/27769579/)) — efficacy in CHKA **unproven**. **Gene replacement** — AAV6-*Chkb* rescued the rmd mouse ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)), a template for future CHKA work (CNS delivery/timing are hurdles). CHKA **inhibitor** trials exist but are oncology programs (opposite direction — irrelevant to this LoF disorder).
- **Surgical/interventional:** epilepsy surgery generally not applicable (diffuse/genetic); orthopedic scoliosis/contracture management; gastrostomy as needed.
- **Supportive/rehabilitative (mainstay):** physical, occupational, and speech/communication therapy; nutrition; vision/orthopedic care; caregiver support (NCIT: Rehabilitation Therapy).

### 13. Prevention
- **Primary:** reproductive genetics only — **genetic counseling** for consanguineous/at-risk couples, **carrier screening**, and, for couples with a prior affected child, **prenatal diagnosis** or **PGT-M**.
- **Secondary:** early molecular diagnosis → early seizure control and early developmental/rehabilitation intervention within the critical window.
- **Tertiary:** complication prevention (seizure management, aspiration precautions/nutrition, scoliosis/contracture prevention, behavioral/sleep support).
- **Immunization/public-health/environmental/prophylaxis:** not applicable (non-infectious, non-environmental).

### 14. Other Species / Natural Disease
- **Affected species (natural):** human (*Homo sapiens*, NCBI:txid9606) only. **No naturally occurring CHKA-equivalent disease in OMIA** for companion animals/livestock. (The spontaneous *Chkb* rmd mouse is the paralog.)
- **Orthologs:** mouse *Chka* (12660, txid10090), rat (29194, txid10116), zebrafish (558499, txid7955), *C. elegans* (180703, txid6239), plus dog/cattle/chicken/chimp (HomoloGene 88575). Deeply conserved (metazoa → yeast CKI1).
- **Comparative biology:** Kennedy pathway deeply conserved; yeast complementation of human variants demonstrates conserved catalytic function ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)). No zoonotic/veterinary relevance (genetic disorder).

### 15. Model Organisms
- **Mouse (MGI):** homozygous *Chka* KO is **embryonic lethal** ([PMID: 20026284](https://pubmed.ncbi.nlm.nih.gov/20026284/)) → CHKA essentiality; a **conditional/hypomorphic or humanized knock-in** model is needed to recapitulate NEDMIMS. The *Chkb* rmd mouse models the paralogous disease and is **AAV-rescuable** ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)).
- **Yeast (SGD):** cell-based complementation validated reduced activity of patient variants ([PMID: 35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/)).
- **C. elegans (WormBase)** and **zebrafish (ZFIN):** orthologs available; no published NEDMIMS-specific model (zebrafish is a tractable CNS/microcephaly option).
- **Cellular/iPSC/organoid:** none published; **patient iPSC cortical neurons/organoids with lipidomics** is the clear next step.
- **Recapitulation:** no model fully reproduces the human CNS phenotype; existing systems establish loss of enzymatic function/essentiality and enable variant functional testing and therapeutic proof-of-concept.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [35202461](https://pubmed.ncbi.nlm.nih.gov/35202461/) | *Bi-allelic variants in CHKA cause a neurodevelopmental disorder with epilepsy and microcephaly* | **Defining paper.** Gene, inheritance, n=6 cohort, phenotype, LoF/Kennedy mechanism (yeast + structural). Supports Findings 1, 2, 5, 9. |
| [27769579](https://pubmed.ncbi.nlm.nih.gov/27769579/) | *Molecular structure and differential function of choline kinases CHKα and CHKβ* | Defines choline→phosphocholine→CDP-choline→PC chain; citicoline rationale. Supports Findings 2, 12. |
| [20026284](https://pubmed.ncbi.nlm.nih.gov/20026284/) | *Differential expression of choline kinase isoforms in skeletal muscle (rmd mouse)* | Murine *Chka* disruption embryonic lethal vs *Chkb* dystrophy; supports hypomorphic-allele inference and tissue specificity. Supports Findings 4, 8, 15. |
| [31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/) | *Functional rescue in a mouse model of megaconial muscular dystrophy* | AAV6-*Chkb* gene therapy rescues paralogous disease — therapeutic proof-of-concept. Supports Finding 4; treatment outlook. |
| [23945283](https://pubmed.ncbi.nlm.nih.gov/23945283/) | *Megaconial CMD due to loss-of-function in choline kinase β* | Characterizes paralogous *CHKB* disorder; contextualizes disease family and differential diagnosis. |
| [31745227](https://pubmed.ncbi.nlm.nih.gov/31745227/) | *CHKA–c-Src SH3 interaction* | Non-catalytic scaffolding role of CHKA; possible additional mechanism (unproven in NEDMIMS). |
| [27705917](https://pubmed.ncbi.nlm.nih.gov/27705917/) / [27206796](https://pubmed.ncbi.nlm.nih.gov/27206796/) / [34416377](https://pubmed.ncbi.nlm.nih.gov/34416377/) | CHKA in cancer "cholinic phenotype" / inhibitor development | Provide enzymatic/structural context; illustrate that cancer biology is the mirror image (gain) of this LoF disorder. |

Peripheral literature (PPFIBP1-, ACBD6-, RBL2-, BORCS5-, tubulin-, GABRB2-related disorders) was reviewed to establish the **differential-diagnostic landscape** of monogenic microcephaly–DD–epilepsy–movement-disorder syndromes; these overlap clinically but are mechanistically distinct from CHKA/Kennedy-pathway disease.

---

## Limitations and Knowledge Gaps

1. **Extremely small evidence base.** The clinical definition rests on **one case series (n=6, 5 families)**. Prevalence, penetrance detail, natural history, survival, and genotype–phenotype correlations are essentially uncharacterized; phenotype frequencies (Finding 5) will shift as cases accrue.
2. **No patient-level molecular profiling.** No transcriptomic/proteomic/lipidomic/metabolomic patient datasets; no validated biomarker. Direct demonstration of reduced brain PC in patients is lacking (mechanism inferred from enzymology + models).
3. **No dedicated in-vivo NEDMIMS model.** Complete *Chka* KO is embryonic lethal, so a hypomorphic/conditional CNS model recapitulating the human disease is not yet available; yeast validates activity loss but cannot model neurodevelopment.
4. **Ontology/identifier gaps.** No Orphanet, ICD-10/ICD-11, or MeSH-specific code located; classification relies on OMIM/MONDO/UMLS.
5. **Therapeutics unproven.** Choline/CDP-choline supplementation and gene replacement are only theoretically motivated (by paralog biology); no experimental or clinical data in NEDMIMS.

---

## Proposed Follow-up Experiments / Actions

1. **International case ascertainment (GeneMatcher / Matchmaker Exchange):** expand the cohort to refine phenotype frequencies, penetrance, expressivity, natural history, and genotype–phenotype correlations.
2. **Patient lipidomics/metabolomics:** measure phosphocholine, CDP-choline, and PC species in patient fibroblasts, plasma, and neural cells to establish a candidate biomarker and confirm the membrane-lipid deficit in vivo.
3. **Faithful neuronal disease model:** generate patient-derived iPSC cortical neurons/organoids or a **conditional/hypomorphic *Chka* mouse** (bypassing embryonic lethality) to test whether reduced activity causes microcephaly, hypomyelination, and hyperexcitability, and to define the developmental critical window.
4. **Structure–function mapping:** dock disease missense variants (p.Arg141Trp, p.Pro194Ser, p.Phe341Leu) onto CHKα structures (PDB 2IG7/2CKQ) and correlate predicted destabilization/active-site perturbation with residual activity, to build a variant-effect framework for reclassifying the 54 current VUS.
5. **Therapeutic proof-of-concept:** test **choline/CDP-choline (citicoline) supplementation** and **AAV-CHKA gene delivery** in patient iPSC neurons and any hypomorphic mouse model, leveraging the AAV6-*Chkb* rmd-mouse rescue precedent ([PMID: 31216357](https://pubmed.ncbi.nlm.nih.gov/31216357/)).
6. **Registry and counseling infrastructure:** establish a NEDMIMS/CHKA registry, standardized genetic-counseling/prenatal-testing pathways for affected (often consanguineous) families, and pursue Orphanet/ICD-11 cataloguing with carrier-frequency estimation.

---

*Report compiled from 9 confirmed findings and 32 reviewed papers across 5 investigation iterations. Evidence source types: predominantly **human clinical** (defining case series), supported by **model organism** (mouse, yeast, C. elegans), **in vitro** (enzyme/structural), and **computational** (gnomAD constraint, structural modeling) data.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_with_Microcephaly_Movement_Abnormalities_and_Seizures-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_with_Microcephaly_Movement_Abnormalities_and_Seizures-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.