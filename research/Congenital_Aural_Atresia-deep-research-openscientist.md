---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T12:27:28.806172'
end_time: '2026-10-01T12:43:36.426092'
duration_seconds: 967.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Aural Atresia
  mondo_id: MONDO:0011921
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
citation_count: 39
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 39
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:40644931
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 27
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 10
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Aural_Atresia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Aural_Atresia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Aural Atresia
- **MONDO ID:** MONDO:0011921 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Aural Atresia** covering all of the
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

# Congenital Aural Atresia (MONDO:0011921): A Comprehensive Disease Characteristics Report

## Summary

**Congenital aural atresia (CAA)** is a congenital malformation in which the external auditory canal (EAC) fails to develop, resulting in absence or severe stenosis of the ear canal, usually accompanied by maldevelopment of the middle-ear cavity and ossicular chain and, in most cases, by microtia (malformation of the auricle). Because the defect is confined to the sound-conducting apparatus derived from the **first and second pharyngeal (branchial) arches and the first pharyngeal cleft**, while the cochlea and inner ear (otic-vesicle derived) are typically spared, CAA produces a **maximal conductive hearing loss** of approximately 60 dB (a large air–bone gap) rather than sensorineural deafness. It is a stable, non-progressive, non-fatal structural malformation present at birth, and the dominant clinical problem is hearing deprivation and its downstream impact on speech, language, and psychosocial development, together with the cosmetic and psychosocial burden of the auricular deformity.

Etiologically, CAA is **heterogeneous**. Most cases are sporadic and isolated (≈74% isolated, ≈89% unilateral in a large registry), with a male predominance and right-sided predilection, and with recognized non-genetic risk factors including maternal pregestational/gestational diabetes, Hispanic and Andean/high-altitude ancestry, moderate altitude residence, maternal retinoid exposure, and some occupational exposures. A substantial minority are **Mendelian/syndromic**, occurring within mandibulofacial dysostosis and craniofacial microsomia spectra. The validated and candidate genes — **HOXA2, TSHZ1, HMX1, TCOF1, POLR1C/POLR1D, SF3B2, EFTUD2, TWIST1** — converge mechanistically on **cranial neural-crest cell specification/patterning and on the spliceosome/ribosome-biogenesis machinery required by neural crest**, linking CAA to the broader group of neurocristopathies and ribosomopathies.

Diagnosis rests on clinical examination, audiometry (bone-conduction testing to confirm a normal cochlear reserve), and **high-resolution temporal-bone CT**, which reveals the hypoplastic middle-ear cleft, fused/hypoplastic/absent ossicles, underpneumatized mastoid, and — critically for surgery — an anteriorly displaced mastoid segment of the facial nerve. CT grading (Jahrsdoerfer 10-point scale; aMEI 16-point scale) stratifies surgical candidacy. Management is **rehabilitative, not curative**: early bone-conduction amplification (softband, then osseointegrated or transcutaneous implants) to restore auditory input during the critical window for language development; Jahrsdoerfer-selected **atresiaplasty/canaloplasty** for hearing (air–bone gap ≤30 dB achievable in ~79–90% of well-selected ears); and staged **autologous costal-cartilage (Nagata/Brent) or porous-polyethylene auricular reconstruction** for the microtia. There is no disease-modifying pharmacologic, gene, or cell therapy. Prevention is limited to maternal glycemic control, teratogen avoidance, newborn hearing screening (secondary prevention), and genetic counseling for syndromic/familial cases.

---

## 1. Disease Information

**Overview.** Congenital aural atresia is the congenital absence or incomplete formation (atresia) of the external auditory canal, typically with concurrent middle-ear hypoplasia and ossicular anomalies, and most often associated with microtia. It is the structural basis of **congenital conductive hearing loss** of the outer/middle ear. The inner ear is usually normal because it derives embryologically from the otic placode/vesicle, a separate developmental program from the branchial-arch-derived conducting apparatus.

**Key identifiers.**
- **MONDO:** MONDO:0011921
- **ICD-10:** Q16.1 (congenital absence, atresia and stricture of auditory canal, external)
- **ICD-11:** LA22 region (congenital malformations of ear causing impairment of hearing)
- **MeSH:** closest terms "Congenital Microtia," "Ear Canal/abnormalities," "Hearing Loss, Conductive"
- **Orphanet / OMIM:** indexed chiefly through syndromic entities and the microtia spectrum (e.g., microtia with meatal atresia and conductive deafness); no single isolated-CAA OMIM phenotype number captures all forms given genetic heterogeneity.

**Synonyms / alternative names.** Aural atresia; congenital atresia of the external auditory canal; congenital meatal atresia; external auditory canal atresia (EAC atresia); atresia auris congenita. Frequently co-indexed with **microtia-atresia** and **congenital aural stenosis** (a milder, partial-canal variant that behaves differently — notably a much higher cholesteatoma risk).

**Information source type.** The knowledge base entry is derived predominantly from **aggregated disease-level resources** — surgical case series, birth-defect registries (e.g., Texas Birth Defects Registry), cohort studies, imaging series, and a genetics scoping review — rather than from individual EHR-level patient records.

---

## 2. Etiology

**Primary causal factors.** CAA is fundamentally a **developmental field defect of the first and second pharyngeal arches and the first pharyngeal cleft** (Finding F004). The causal spectrum spans:
- **Multifactorial/sporadic** (the majority): disrupted branchial-arch morphogenesis of uncertain individual cause.
- **Mendelian/syndromic:** single-gene disorders affecting neural-crest patterning and the spliceosome/ribosome machinery (Findings F001, F008).
- **Teratogenic/environmental:** maternal diabetes, retinoids (isotretinoin/vitamin-A excess), mycophenolate mofetil, and other exposures.

### Risk factors

**Genetic risk factors.** A 2024 scoping review of nonsyndromic microtia/CAA genetics (30 studies) identified **40 unique genes plus one susceptibility locus (4p15.32–4p16.2)**; the most-cited microtia genes were **HOXA2, MUC6, GSC**, and **TSHZ1 was identified as the candidate gene for nonsyndromic CAA alone** (Finding F001; [PMID: 39624921](https://pubmed.ncbi.nlm.nih.gov/39624921/)). The review states: *"Thirty studies met inclusion criteria, describing 40 unique genes and one susceptibility gene locus (4p15.32-4p16.2) ... A single article describing nonsyndromic CAA alone identified the TSHZ1 as a candidate gene."* **HOXA2** homeodomain missense (p.Q186K) causes autosomal-recessive bilateral microtia with mixed hearing loss and cleft palate in a consanguineous Iranian family (LOD 4.17; [PMID: 18394579](https://pubmed.ncbi.nlm.nih.gov/18394579/)). **HMX1** downstream-enhancer duplications cause isolated bilateral concha-type microtia ([PMID: 32552830](https://pubmed.ncbi.nlm.nih.gov/32552830/)).

**Environmental/demographic risk factors** (Finding F002):

| Risk factor | Effect estimate | Source |
|---|---|---|
| Male sex | PR 1.3 (95% CI 1.2–1.4); M:F up to 3.53:1 | [PMID: 36398384](https://pubmed.ncbi.nlm.nih.gov/36398384/), [PMID: 40984631](https://pubmed.ncbi.nlm.nih.gov/40984631/) |
| Maternal diabetes | PR 2.0 (1.6–2.4); bilateral PR 5.0 (3.3–7.7) | [PMID: 36398384](https://pubmed.ncbi.nlm.nih.gov/36398384/) |
| Maternal diabetes (VACTERL hearing loss) | OR 3.71 (1.5–7.3) | [PMID: 37649433](https://pubmed.ncbi.nlm.nih.gov/37649433/) |
| Hispanic ancestry | PR 2.9 (2.5–3.4) | [PMID: 36398384](https://pubmed.ncbi.nlm.nih.gov/36398384/) |
| Advanced maternal age (30–39; ≥35) | PR 1.2 | [PMID: 36398384](https://pubmed.ncbi.nlm.nih.gov/36398384/), [PMID: 39487910](https://pubmed.ncbi.nlm.nih.gov/39487910/) |
| Moderate altitude (1500–2500 m) | aOR 1.60 for microtia | [PMID: 39056527](https://pubmed.ncbi.nlm.nih.gov/39056527/) |
| Maternal cleaning occupation | Elevated OR for anotia/microtia | [PMID: 41266119](https://pubmed.ncbi.nlm.nih.gov/41266119/) |
| Mycophenolate mofetil (in-utero) | Pattern of malformation incl. microtia | [PMID: 18368705](https://pubmed.ncbi.nlm.nih.gov/18368705/) |

**Protective factors.** No validated genetic protective variant or modifier allele is established for CAA. Folic acid intake and TORCH vaccination were examined as candidate protective factors in the Indonesian case-control study ([PMID: 40984631](https://pubmed.ncbi.nlm.nih.gov/40984631/)) but no robust protective effect specific to CAA has been confirmed. The clearest *modifiable* preventive lever is **maternal glycemic control**, given the strong, dose-dependent diabetes association (bilateral PR 5.0).

**Gene–environment interactions.** Direct GxE evidence for CAA is sparse. The biologically coherent model is that **maternal hyperglycemia and retinoid signaling perturbations act on a susceptible neural-crest/branchial-arch developmental program** — the same program disrupted by HOXA2/neural-crest genes — such that environmental insults and genetic susceptibility converge on the same morphogenetic window (weeks 3–8 of gestation). This remains inferred rather than demonstrated at the molecular level in humans.

---

## 3. Phenotypes

The core phenotype is **congenital conductive hearing loss** due to a mechanically absent/obstructed sound-conduction path, layered with **structural/physical malformations** of the ear and, in syndromic cases, broader craniofacial and systemic features.

| Phenotype | Type | HPO term (suggested) | Characteristics | Frequency |
|---|---|---|---|---|
| Aural atresia (absent EAC) | Physical malformation | HP:0000413 (Atresia of the external auditory canal) | Congenital; stable; unilateral ~89% | Defining feature |
| Microtia | Physical malformation | HP:0008551 (Microtia) | Congenital; right-predominant | Co-occurs in vast majority |
| Conductive hearing loss | Clinical sign / lab (audiometric) | HP:0000405 (Conductive hearing impairment) | Neonatal onset; severe (~60 dB air–bone gap); non-progressive | Universal in complete atresia |
| Ossicular malformation/fusion | Physical malformation | HP:0011453 (Abnormality of the middle ear ossicles) | Congenital | ~89% of atretic ears (25/28 in CT series) |
| Middle-ear hypoplasia | Physical malformation | HP:0011452 (Hypoplasia of the middle ear) | Congenital | Typical |
| Aberrant facial nerve course | Physical malformation | HP:0010827 (Abnormal facial nerve morphology) | Congenital | Anterior/round-window position in 57/70 atretic ears |
| Cholesteatoma (stenosis variant) | Complication | HP:0009797 (Cholesteatoma) | Acquired; progressive | 1.7% in complete CAA vs 43% in stenosis |

**Age of onset:** congenital (neonatal) for all structural and conductive-loss features. **Severity:** hearing loss is severe and maximal for a conductive deficit (~60 dB) but, crucially, rehabilitatable because cochlear reserve is normal. **Progression:** the malformation itself is stable and non-progressive; cholesteatoma (mainly in the stenosis variant) is a progressive acquired complication. **Frequency among affected individuals:** unilateral ~89%, bilateral ~11%; bilateral disease disproportionately associated with maternal diabetes.

**Quality-of-life impact.** Bilateral CAA threatens speech and language acquisition and is a developmental emergency for auditory input. Even unilateral CAA carries measurable burden: in congenital unilateral hearing loss, **early language input strongly improves language outcomes** at age 3 ([PMID: 41616317](https://pubmed.ncbi.nlm.nih.gov/41616317/)). Bone-conduction rehabilitation yields positive QoL benefit (median **Glasgow Children's Benefit Inventory +14.6; 89% improved**; [PMID: 36649663](https://pubmed.ncbi.nlm.nih.gov/36649663/)). The auricular deformity additionally generates appearance-related distress addressed in reconstruction decisions.

---

## 4. Genetic / Molecular Information

**Causal and candidate genes (Findings F001, F008).**

| Gene (HGNC) | Locus | Role / disorder | Inheritance | Evidence |
|---|---|---|---|---|
| **HOXA2** | 7p15.2 | Homeobox; PA2 neural-crest patterning; principal validated nonsyndromic microtia/CAA gene | AR (p.Q186K) | [PMID: 18394579](https://pubmed.ncbi.nlm.nih.gov/18394579/), [PMID: 37277355](https://pubmed.ncbi.nlm.nih.gov/37277355/) |
| **TSHZ1** | 18q22.3 | Candidate for *isolated* CAA; middle-ear development | — | [PMID: 39624921](https://pubmed.ncbi.nlm.nih.gov/39624921/) |
| **HMX1** | 4p16.1 | Craniofacial homeobox; enhancer (ECR) CNV | AD (enhancer duplication) | [PMID: 32552830](https://pubmed.ncbi.nlm.nih.gov/32552830/) |
| **TCOF1** | 5q32–q33.1 | Treacher Collins (ribosome biogenesis/treacle) | AD | [PMID: 39583227](https://pubmed.ncbi.nlm.nih.gov/39583227/), [PMID: 16981466](https://pubmed.ncbi.nlm.nih.gov/16981466/) |
| **POLR1C / POLR1D** | — | Treacher Collins (RNA Pol I/III) | AR / AD | [PMID: 39583227](https://pubmed.ncbi.nlm.nih.gov/39583227/) |
| **SF3B2** | 11q13.2 | Craniofacial microsomia; spliceosome | — (truncating: p.Gln60*, p.Lys507*) | [PMID: 42608604](https://pubmed.ncbi.nlm.nih.gov/42608604/) |
| **EFTUD2** | 17q21.31 | Mandibulofacial dysostosis with microcephaly; spliceosome | AD (c.698dupA p.V235Gfs*27) | [PMID: 41918385](https://pubmed.ncbi.nlm.nih.gov/41918385/) |
| **TWIST1** | 7p21.1 | Syndromic craniosynostosis with microtia/aural atresia | AD (c.423C>G p.Asp141Glu) | [PMID: 42104108](https://pubmed.ncbi.nlm.nih.gov/42104108/) |

**Variant classification and type.** Reported pathogenic variants span **missense** (HOXA2 p.Q186K; TWIST1 p.Asp141Glu), **nonsense/truncating** (SF3B2 p.Gln60*, p.Lys507*), **frameshift** (EFTUD2 p.V235Gfs*27), and **structural/CNV** (HMX1 enhancer duplications; the 4p15.32–4p16.2 susceptibility locus). A scoping review across 194 subjects in 18 Mendelian manuscripts found **49% autosomal dominant, 4% autosomal recessive, 5% X-linked recessive, and 42% no reported inheritance pattern** ([PMID: 39624921](https://pubmed.ncbi.nlm.nih.gov/39624921/)). All reported variants are germline; no somatic origin is implicated for this developmental disorder.

**Functional consequences.** The dominant mechanism is **loss of function / haploinsufficiency** of transcription factors (HOXA2, TWIST1) and of spliceosome/ribosome-biogenesis components (SF3B2, EFTUD2, TCOF1, POLR1C/D), which impairs the specification, survival, and patterning of cranial neural-crest cells feeding the pharyngeal arches. HMX1 CNVs act via **enhancer dosage** on a transcription factor; notably, luciferase assays show **HOXA2 increases HMX1 enhancer activity**, placing these genes in a shared regulatory network ([PMID: 32552830](https://pubmed.ncbi.nlm.nih.gov/32552830/)).

**Modifier genes, epigenetics, chromosomal abnormalities.** No specific modifier gene is established for isolated CAA. Epigenetic contributions are plausible given enhancer/CNV involvement (HMX1) but not directly characterized. Large-scale chromosomal lesions appear chiefly in syndromic/contiguous-gene contexts; the 4p15.32–4p16.2 locus is the one reported nonsyndromic susceptibility region.

---

## 5. Environmental Information

- **Environmental/toxicant factors:** maternal retinoid exposure (isotretinoin, vitamin-A excess) is a classic ear-teratogen pathway; mycophenolate mofetil in-utero produces a malformation pattern including microtia ([PMID: 18368705](https://pubmed.ncbi.nlm.nih.gov/18368705/)); maternal occupational cleaning exposure is associated with anotia/microtia ([PMID: 41266119](https://pubmed.ncbi.nlm.nih.gov/41266119/)); moderate altitude (hypoxia proxy) raises microtia risk (aOR 1.60; [PMID: 39056527](https://pubmed.ncbi.nlm.nih.gov/39056527/)).
- **Lifestyle/metabolic factors:** **maternal diabetes** is the strongest modifiable factor (PR 2.0 overall; PR 5.0 bilateral). Smoking and folic-acid status were examined without a confirmed CAA-specific effect ([PMID: 40984631](https://pubmed.ncbi.nlm.nih.gov/40984631/)).
- **Infectious agents:** Not an established cause of isolated CAA. (TORCH infections classically cause sensorineural, not conductive outer/middle-ear, deafness; TORCH vaccination was examined as a candidate variable but no CAA-specific infectious etiology is confirmed.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A **genetic lesion** (e.g., *HOXA2* LOF, *SF3B2/EFTUD2/TCOF1* spliceosome/ribosome-biogenesis haploinsufficiency, *TWIST1* LOF) **or** an **environmental insult** (maternal hyperglycemia, retinoid excess, hypoxia) perturbs the embryo during pharyngeal-arch morphogenesis (weeks 3–8). → *leads to*
2. **Impaired specification, survival, migration, or patterning of cranial neural-crest cells** populating the **first and second pharyngeal arches** (demonstrated for *Hoxa2* in PA2 neural crest; inferred for the spliceosome/ribosomopathy genes via neural-crest sensitivity). → *results in*
3. **Dysmorphogenesis of first/second-arch and first-cleft derivatives** — the auricle (hillocks of His), the external auditory meatus (from the first pharyngeal cleft/EAM), the tympanic membrane, and the middle-ear cavity/ossicles (malleus, incus from arch 1; part of stapes from arch 2). → *branches into*
   - **3a.** Failure of the **first pharyngeal cleft/EAM to canalize** → **aural atresia/stenosis** (no patent ear canal).
   - **3b.** Arrested auricular hillock development → **microtia**.
   - **3c.** Hypoplasia/fusion/absence of **ossicles** and a **small, underpneumatized middle-ear cleft**; secondary **aberrant anterior course of the facial nerve**. → *together these cause*
4. **Interruption of the air-conduction sound path** (no canal to deliver sound; no/abnormal ossicular lever to transmit it to the oval window). → *produces*
5. **Maximal conductive hearing loss (~60 dB air–bone gap)** with a **preserved cochlea/inner ear** (otic-placode lineage unaffected). → *if bilateral and untreated, leads to*
6. **Auditory deprivation during the critical period for language**, threatening **speech, language, and psychosocial development** — the principal source of morbidity.

### Mechanistic detail

- **Molecular pathways / cellular processes (GO suggestions):** cranial **neural crest cell development** (GO:0014032), **pharyngeal system / branchial-arch morphogenesis** (GO:0060037), **ear morphogenesis** (GO:0042471), **middle ear morphogenesis** (GO:0042474), and **inner ear morphogenesis** (GO:0042472, spared here). In the spliceosome/ribosomopathy genes, **mRNA splicing via spliceosome** (GO:0000398) and **ribosome biogenesis** (GO:0042254) are the upstream defective processes; neural crest is unusually sensitive to their disruption (nucleolar stress → p53-dependent apoptosis, as established for TCOF1/treacle).
- **Super-enhancer control (demonstrated):** In PA2 neural crest, a super-enhancer region (**HIRE1/HIRE2**) establishes inter-TAD interactions with **Hoxa2**, which is required for external and middle-ear structures; **HIRE2 deletion on a Hoxa2-haploinsufficient background yields microtia**, and **HIRE1 deletion phenocopies the full Hoxa2 knockout** ([PMID: 37277355](https://pubmed.ncbi.nlm.nih.gov/37277355/)).
- **Protein dysfunction:** loss-of-function/haploinsufficiency of transcription factors and spliceosome/Pol-I components (upstream); mechanical loss of the ossicular lever system (downstream, the proximate cause of the conductive deficit).
- **Cell types (CL suggestions):** cranial **neural crest cell** (CL:0000333), chondrocytes and osteoblasts of the ossicles and auricular cartilage, **epithelial cells** of the EAM.
- **Upstream vs downstream:** upstream = gene/enhancer lesion → neural-crest defect; downstream = arch-derivative dysmorphogenesis → interrupted conduction path → conductive hearing loss → developmental sequelae.

**Molecular profiling.** No human transcriptomic/proteomic/metabolomic signature specific to isolated CAA tissue is established; mechanistic evidence comes from mouse/zebrafish models (below) and human imaging/genetics.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** external auditory canal (**UBERON:0001352**, external acoustic meatus), auricle/pinna (**UBERON:0001757**), middle ear (**UBERON:0001756**) with ossicles — malleus (**UBERON:0002355**), incus (**UBERON:0002356**), stapes (**UBERON:0001687**) — tympanic membrane (**UBERON:0002364**), mastoid/temporal bone (**UBERON:0001678**). Facial nerve (**UBERON:0001647**) is anatomically displaced.
- **Secondary/system involvement:** in syndromic forms, the craniofacial skeleton (mandible, maxilla, zygoma), palate, eyes, vertebrae, heart, and limbs (craniofacial microsomia / Treacher Collins / VACTERL / craniosynostosis spectra).
- **Tissue/cell level:** neural-crest-derived cartilage and bone (ossicles, auricle), EAM epithelium; the sensorineural cochlea is spared.
- **Subcellular (GO Cellular Component):** for the molecular lesions, **spliceosomal complex** (GO:0005681), **nucleolus** (GO:0005730, ribosome biogenesis), and **nucleus/chromatin** (transcription-factor and enhancer function).
- **Localization / lateralization:** predominantly **unilateral (~89%)** with a right-sided predilection; bilateral in ~11% and over-represented in maternal diabetes. The imaging hallmark is an **anteriorly/inferiorly displaced mastoid facial nerve** near the round window (57/70 atretic ears; [PMID: 23793597](https://pubmed.ncbi.nlm.nih.gov/23793597/)).

---

## 8. Temporal Development

- **Onset:** congenital; the malformation is fully formed at birth (completed during weeks 3–8 of gestation).
- **Onset pattern:** structural and chronic from birth; hearing loss is present and detectable from the neonatal period (newborn hearing screening).
- **Progression:** the atresia/microtia is **stable and non-progressive** across life. The notable acquired, progressive complication is **cholesteatoma**, which is rare in complete CAA (**1.7%**) but common in congenital EAC stenosis (**43%**) — a key reason the stenosis variant requires surveillance/earlier surgery ([PMID: 35439089](https://pubmed.ncbi.nlm.nih.gov/35439089/)).
- **Disease course / duration:** chronic, lifelong.
- **Critical periods:** the decisive window is **postnatal auditory development** — early auditory input/language stimulation (first years of life) determines language outcomes, independent of the device per se ([PMID: 41616317](https://pubmed.ncbi.nlm.nih.gov/41616317/)). This makes early amplification an intervention of time-sensitive opportunity rather than structural reversal.

---

## 9. Inheritance and Population

**Epidemiology.** Anotia/microtia (the entity under which CAA is registered) birth prevalence is on the order of ~1–3 per 10,000 births, rising in some registries (China 2007–2021; [PMID: 39487910](https://pubmed.ncbi.nlm.nih.gov/39487910/)). In the Texas Birth Defects Registry (1999–2014, n=1,322): **74.3% isolated, 88.9% unilateral** ([PMID: 36398384](https://pubmed.ncbi.nlm.nih.gov/36398384/)).

**Inheritance (genetic forms).** Across 18 Mendelian microtia/CAA manuscripts (194 subjects): **49% AD, 4% AR, 5% X-linked recessive, 42% unspecified** ([PMID: 39624921](https://pubmed.ncbi.nlm.nih.gov/39624921/)). HOXA2 microtia/CAA can be autosomal recessive (p.Q186K, consanguineous family; [PMID: 18394579](https://pubmed.ncbi.nlm.nih.gov/18394579/)); syndromic genes (TCOF1, EFTUD2, TWIST1) are typically autosomal dominant. **Penetrance is incomplete and expressivity highly variable** — the Hfm mouse model is explicitly described as autosomal dominant with reduced penetrance ([PMID: 11772174](https://pubmed.ncbi.nlm.nih.gov/11772174/)), mirroring human variability. Consanguinity contributes to recessive forms (Iranian HOXA2 family). Founder effects, germline mosaicism, genetic anticipation, and defined carrier frequencies are **not established** for isolated CAA.

**Population demographics.**
- **Sex ratio:** male-predominant (M:F ≈ 1.3:1 to 3.53:1).
- **Ethnic/geographic:** higher prevalence in **Hispanic** (PR 2.9) and **Andean/high-altitude** populations; moderate-altitude residence is an independent risk factor (aOR 1.60).
- **Laterality distribution:** right > left; unilateral ≫ bilateral.
- **Maternal age:** increased with advanced maternal age (≥35).

---

## 10. Diagnostics

**Clinical tests.**
- **Audiometry / electrophysiology:** pure-tone and bone-conduction audiometry confirm a **conductive** loss with normal cochlear reserve; in infants, ABR/BAER and otoacoustic-emission-based newborn screening flag the deficit. A ~60 dB air–bone gap is characteristic.
- **Imaging — the cornerstone (Finding F006):** **high-resolution temporal-bone CT** demonstrates: reduced middle-ear sectional area (**mean 19.3 mm² vs 47.4 mm²** in controls), **hypoplastic ossicles** (mean ossicular area 8.3 mm² vs 11 mm²), diminished mastoid aeration ([PMID: 17178446](https://pubmed.ncbi.nlm.nih.gov/17178446/)); ossicular deformity in **25/28 ears** (malleus-incus hypoplasia 19, stapes abnormality 11, absent ossicles 3, oval-window atresia 1; [PMID: 17580714](https://pubmed.ncbi.nlm.nih.gov/17580714/)); and an **anteriorly displaced mastoid facial nerve** near the round window in **57/70** atretic ears ([PMID: 23793597](https://pubmed.ncbi.nlm.nih.gov/23793597/)). Körner's septum anatomy is also assessed preoperatively ([PMID: 16108317](https://pubmed.ncbi.nlm.nih.gov/16108317/)).
- **CT-based grading:** the **Jahrsdoerfer 10-point scale** and the **16-point aMEI score** stratify surgical candidacy and predict outcome ([PMID: 23604757](https://pubmed.ncbi.nlm.nih.gov/23604757/)). CT/MRI is not always required to exclude cholesteatoma in complete-atresia follow-up ([PMID: 31374385](https://pubmed.ncbi.nlm.nih.gov/31374385/)).

**Genetic testing.** Indicated when syndromic features are present or for familial/bilateral/recessive-pattern cases: **targeted single-gene testing** (HOXA2, TCOF1, SF3B2, EFTUD2, TWIST1), **craniofacial gene panels**, **chromosomal microarray** (for CNVs, e.g., HMX1 enhancer region; 4p susceptibility locus), and **WES/WGS** for undiagnosed syndromic presentations. Isolated unilateral CAA with a normal contralateral ear generally has low diagnostic yield for monogenic testing.

**Clinical criteria / differential diagnosis.** Diagnosis is clinical + radiologic. Differential includes **congenital EAC stenosis** (higher cholesteatoma risk), **acquired atresia**, **first branchial cleft anomaly** (can co-occur; [PMID: 31137094](https://pubmed.ncbi.nlm.nih.gov/31137094/)), and distinguishing isolated from **syndromic** forms (Treacher Collins, Goldenhar/OAV, Nager, Miller, craniofacial microsomia, MFDM).

**Screening.** Universal **newborn hearing screening** captures the conductive deficit; **cascade/genetic counseling** applies to syndromic/familial cases.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** CAA is **non-fatal**; isolated CAA does not reduce life expectancy. Mortality, where present, relates to syndromic comorbidities (airway, cardiac).
- **Morbidity/function:** the dominant morbidity is **hearing disability** and its developmental consequences. Outcomes hinge on **timely auditory input**. Bone-conduction rehabilitation significantly improves pure-tone average and speech-in-noise (p<0.001) with positive QoL (GCBI +14.6; [PMID: 36649663](https://pubmed.ncbi.nlm.nih.gov/36649663/)).
- **Recovery potential:** hearing is **rehabilitatable** (normal cochlea). Atresiaplasty achieves an **air–bone gap of 0–30 dB in ~79–90%** of well-selected ears ([PMID: 25625335](https://pubmed.ncbi.nlm.nih.gov/25625335/)).
- **Complications:** canal restenosis, tympanic-membrane lateralization, recurrent infection, and (rarely in complete CAA) cholesteatoma; facial-nerve injury risk from the aberrant nerve course.
- **Prognostic factors:** **Jahrsdoerfer/aMEI CT score** is the principal predictor of surgical hearing outcome; microtia grade, hemifacial microsomia, and prior canalplasty predict auricular-reconstruction outcomes ([PMID: 29595733](https://pubmed.ncbi.nlm.nih.gov/29595733/)); shorter PORP prosthesis length predicts better long-term hearing ([PMID: 29664866](https://pubmed.ncbi.nlm.nih.gov/29664866/)).

---

## 12. Treatment

Management is **rehabilitative and reconstructive**; there is **no disease-modifying pharmacologic, gene, cell, or RNA therapy** (Finding F009).

**Hearing rehabilitation (prioritized in infancy).**
- **Bone-conduction devices** (NCIT: Bone-Conduction Hearing Device): softband BCD in infancy, then **osseointegrated (percutaneous BAHA)** or **transcutaneous (Baha Attract, Sophono)** implants. Most common initial treatment (**75.6%** of patients receive a nonsurgical BCHD; earlier fitting improves compliance; [PMID: 33338703](https://pubmed.ncbi.nlm.nih.gov/33338703/)). Transcutaneous osseointegrated implants improve PTA (63.7→9.6 dB) and speech-in-noise in children ([PMID: 29978214](https://pubmed.ncbi.nlm.nih.gov/29978214/)).
- **Atresiaplasty / canaloplasty** (NCIT: surgical reconstruction of ear canal): for Jahrsdoerfer-selected candidates (score ≥6–7), achieving ABG ≤30 dB in ~79–90% ([PMID: 25625335](https://pubmed.ncbi.nlm.nih.gov/25625335/)); often combined with ossicular reconstruction (PORP; [PMID: 29664866](https://pubmed.ncbi.nlm.nih.gov/29664866/)) and tragal/flap techniques ([PMID: 19172604](https://pubmed.ncbi.nlm.nih.gov/19172604/), [PMID: 27011544](https://pubmed.ncbi.nlm.nih.gov/27011544/)).
- **Active middle-ear implants** for selected malformed ears (aMEI score; [PMID: 23604757](https://pubmed.ncbi.nlm.nih.gov/23604757/)).

**Auricular (microtia) reconstruction.**
- **Autologous costal-cartilage** frameworks — **Nagata two-stage** and **Brent** techniques — or **porous polyethylene (MEDPOR)** implants, typically begun around school age (~6–10 yr) ([PMID: 29595733](https://pubmed.ncbi.nlm.nih.gov/29595733/), [PMID: 40644931](https://pubmed.ncbi.nlm.nih.gov/40644931/)). Hemifacial microsomia and prior canalplasty predict unfavorable auricular projection (22.3% unfavorable; [PMID: 29595733](https://pubmed.ncbi.nlm.nih.gov/29595733/)).
- Adjuncts: **ear molding** in the neonatal period for milder auricular deformities (RCT; [PMID: 32791720](https://pubmed.ncbi.nlm.nih.gov/32791720/)); laser hair removal of low hairlines after reconstruction ([PMID: 40644931](https://pubmed.ncbi.nlm.nih.gov/40644931/)).

**Treatment strategy / sequencing.** Auditory rehabilitation first (infancy), then coordinated planning of auricular reconstruction and any canalplasty — the two must be sequenced because canalplasty and hemifacial microsomia affect reconstruction outcomes. No combination pharmacotherapy or personalized-medicine (genotype-guided) regimen exists.

---

## 13. Prevention

- **Primary prevention:** limited but real — **maternal glycemic control** (given diabetes PR 2.0 overall, 5.0 bilateral), **avoidance of teratogens** (retinoids, mycophenolate), and counseling regarding modifiable exposures.
- **Secondary prevention:** **universal newborn hearing screening** for early detection and timely amplification during the language-critical window.
- **Tertiary prevention:** surveillance for cholesteatoma (especially in the stenosis variant), prevention of restenosis/infection after surgery, and ongoing audiologic/developmental support.
- **Genetic counseling:** indicated for syndromic and familial/recessive forms; prenatal diagnosis is feasible for known syndromic variants (e.g., EFTUD2; [PMID: 41918385](https://pubmed.ncbi.nlm.nih.gov/41918385/)) and Treacher Collins ([PMID: 16981466](https://pubmed.ncbi.nlm.nih.gov/16981466/)).
- **Immunization / prophylaxis / public-health vector measures:** not applicable (non-infectious).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** the causal genes are deeply conserved — *Hoxa2* (mouse, NCBI Taxon 10090), *sf3b2* (zebrafish, *Danio rerio*, Taxon 7955), *Tcof1/Treacle*, *Twist1*, *Hmx1*. Human–mouse–zebrafish conservation of the branchial-arch/neural-crest program underlies the use of these models.
- **Natural disease in animals:** HMX1 enhancer CNVs cause ear (and eye) malformations in other animals naturally, and were described in animals before humans ([PMID: 32552830](https://pubmed.ncbi.nlm.nih.gov/32552830/)) — a comparative-biology link. Formal OMIA cataloguing of naturally occurring aural atresia in companion animals was not specifically retrieved in this investigation.
- **Evolutionary conservation of mechanism:** the first/second-arch contribution to the middle and external ear and tympanic membrane is conserved across amniotes (mouse and chick comparison; [PMID: 28807901](https://pubmed.ncbi.nlm.nih.gov/28807901/)).
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Type | Genetic manipulation | Phenotype recapitulation | Source |
|---|---|---|---|---|
| **Mouse — Hoxa2 / HIRE enhancer** | Mammalian, in vivo | Enhancer deletion (HIRE1/HIRE2), haploinsufficiency | HIRE2 deletion on Hoxa2-haploinsufficient background → **microtia**; HIRE1 deletion phenocopies full Hoxa2 KO; external/middle-ear defects | [PMID: 37277355](https://pubmed.ncbi.nlm.nih.gov/37277355/) |
| **Mouse — Hfm transgenic** | Mammalian, in vivo | Transgenic (AD, reduced penetrance) | Microtia + external auditory meatus, middle-ear, cranial-base, maxilla, pharyngeal anomalies — models hemifacial microsomia/microtia-atresia spectrum | [PMID: 11772174](https://pubmed.ncbi.nlm.nih.gov/11772174/) |
| **Mouse / chick — pharyngeal arch** | Mammalian / avian | Developmental/lineage analysis | First arch crucial for tympanic-membrane formation; distinct PA1/PA2 contributions | [PMID: 28807901](https://pubmed.ncbi.nlm.nih.gov/28807901/) |
| **Zebrafish — sf3b2 knockout** | Vertebrate, in vivo | CRISPR/Cas9 KO | **25.33% malformation rate**, shortened Meckel's/palatoquadrate cartilage, reduced head-to-body ratio — recapitulates human craniofacial microsomia features | [PMID: 42608604](https://pubmed.ncbi.nlm.nih.gov/42608604/) |

**Applications:** these models dissect neural-crest patterning (Hoxa2), enhancer-level gene regulation (HIRE), spliceosome sensitivity of neural crest (sf3b2), and the developmental origin of tympanic-membrane/middle-ear structures. **Limitations:** rodent ear anatomy differs from human; models capture microtia/arch dysmorphology better than the human-specific **external auditory canal atresia** and the clinically pivotal **aberrant facial-nerve course**; no model fully reproduces the human conductive-hearing-loss rehabilitation problem.

---

## Mechanistic Model / Interpretation

```
   GENETIC LESION                         ENVIRONMENTAL INSULT
   HOXA2, TSHZ1, HMX1,                    maternal diabetes,
   TCOF1/POLR1C/D, SF3B2,                 retinoids, hypoxia/altitude,
   EFTUD2, TWIST1 (LOF/                   mycophenolate
   haploinsufficiency/CNV)                      |
        |                                        |
        v                                        v
   +----------------------------------------------------------+
   |  Perturbed CRANIAL NEURAL-CREST CELL program             |
   |  (specification / survival / patterning) in              |
   |  PHARYNGEAL ARCHES 1 & 2  (weeks 3-8)                     |
   |  [spliceosome/ribosome-biogenesis genes act here via     |
   |   nucleolar/splicing stress; TFs via patterning]         |
   +----------------------------------------------------------+
        |
        v
   Dysmorphogenesis of 1st/2nd-arch & 1st-cleft derivatives
        |                 |                     |
        v                 v                     v
  EAM fails to      Auricular hillock     Ossicle hypoplasia/
  canalize          arrest                fusion/absence +
  = AURAL ATRESIA   = MICROTIA            small middle ear +
                                          anterior facial nerve
        \_________________|_____________________/
                          v
        Interrupted AIR-CONDUCTION sound path
        (cochlea / inner ear SPARED)
                          v
        MAXIMAL CONDUCTIVE HEARING LOSS (~60 dB)
                          v
   (if bilateral & untreated) AUDITORY DEPRIVATION in the
   language-critical window -> speech/language/psychosocial morbidity
                          v
        Rehabilitation: bone-conduction input + atresiaplasty
        + auricular reconstruction  (NOT structural cure)
```

The unifying interpretation is that CAA is a **neurocristopathy of the pharyngeal arches**: diverse upstream lesions (transcription-factor LOF, spliceosome/ribosome-biogenesis haploinsufficiency, enhancer CNVs, or teratogenic metabolic/retinoid stress) converge on the same vulnerable cranial-neural-crest population, yielding the same downstream anatomical triad (atresia + microtia + ossicular/middle-ear hypoplasia) and the same functional endpoint (conductive hearing loss with a normal cochlea). This convergence explains both the **phenotypic overlap** among Treacher Collins, Goldenhar/OAV, Nager, Miller, and craniofacial-microsomia spectra and the **genetic heterogeneity** (TCOF1 excluded in Goldenhar and in familial microtia-meatal atresia; [PMID: 15770127](https://pubmed.ncbi.nlm.nih.gov/15770127/)). It also frames why treatment is rehabilitative: the lesion is a completed developmental event by birth, so therapy targets the functional consequence (restoring auditory input) rather than the cause. A notable clinical gradient supports the model — in the oculo-auriculo-vertebral spectrum, EAC atresia, ossicular anomaly, and aberrant facial-nerve frequency all rise with craniofacial severity (EAC 48.4%→82.8%; ossicles 40.3%→82.8%; [PMID: 41289623](https://pubmed.ncbi.nlm.nih.gov/41289623/)), indicating a dose-like relationship between the severity of arch disruption and the ear phenotype.

---

## Evidence Base

| PMID | Contribution | Supports / Challenges |
|---|---|---|
| [39624921](https://pubmed.ncbi.nlm.nih.gov/39624921/) | Scoping review: 40 genes + 4p15.32–4p16.2 locus; HOXA2/MUC6/GSC top; TSHZ1 for isolated CAA; inheritance breakdown | Supports genetic landscape (F001) |
| [18394579](https://pubmed.ncbi.nlm.nih.gov/18394579/) | HOXA2 p.Q186K AR microtia/CAA, LOD 4.17 | Supports HOXA2 causality (F001) |
| [32552830](https://pubmed.ncbi.nlm.nih.gov/32552830/) | HMX1 enhancer duplications → concha-type microtia; HOXA2 boosts HMX1 enhancer | Supports regulatory network (F001) |
| [36398384](https://pubmed.ncbi.nlm.nih.gov/36398384/) | Texas registry: isolated 74.3%, unilateral 88.9%, male/diabetes/Hispanic risk | Supports epidemiology (F002) |
| [37649433](https://pubmed.ncbi.nlm.nih.gov/37649433/) | Maternal diabetes OR 3.71 for hearing loss in VACTERL | Supports diabetes risk (F002) |
| [36649663](https://pubmed.ncbi.nlm.nih.gov/36649663/) | Transcutaneous BCI: PTA/speech improve p<0.001; GCBI +14.6 | Supports treatment/QoL (F003) |
| [25625335](https://pubmed.ncbi.nlm.nih.gov/25625335/) | Atresiaplasty ABG 0–30 dB in 79–90%; complications | Supports surgical outcomes (F003) |
| [33338703](https://pubmed.ncbi.nlm.nih.gov/33338703/) | 75.6% receive nonsurgical BCHD; earlier fitting → compliance | Supports treatment pathway (F003) |
| [39583227](https://pubmed.ncbi.nlm.nih.gov/39583227/) | Treacher Collins (TCOF1) → atresia + middle-ear hypoplasia via arch 1&2 | Supports branchial-arch mechanism (F004) |
| [15770127](https://pubmed.ncbi.nlm.nih.gov/15770127/) | Phenotypic overlap of 1st/2nd-arch disorders; TCOF1 excluded in Goldenhar/familial microtia | Supports shared origin + heterogeneity (F004) |
| [37277355](https://pubmed.ncbi.nlm.nih.gov/37277355/) | HIRE super-enhancer controls Hoxa2 in PA2 crest; deletions → microtia | Supports mechanism + mouse model (F005) |
| [11772174](https://pubmed.ncbi.nlm.nih.gov/11772174/) | Hfm mouse recapitulates microtia + EAM/middle-ear anomalies | Supports model organism (F005) |
| [17178446](https://pubmed.ncbi.nlm.nih.gov/17178446/) | CT: middle-ear 19.3 vs 47.4 mm²; ossicles hypoplastic | Supports diagnostics (F006) |
| [23793597](https://pubmed.ncbi.nlm.nih.gov/23793597/) | Aberrant facial-nerve position in 57/70 atretic ears | Supports diagnostics/surgery (F006) |
| [35439089](https://pubmed.ncbi.nlm.nih.gov/35439089/) | Cholesteatoma 1.7% CAA vs 43% stenosis | Supports prognosis/complications (F006) |
| [41616317](https://pubmed.ncbi.nlm.nih.gov/41616317/) | RCT: early language input (not device alone) drives outcomes | Supports prognosis/critical period (F007) |
| [39487910](https://pubmed.ncbi.nlm.nih.gov/39487910/) | Rising microtia/anotia prevalence; maternal age | Supports epidemiology (F007) |
| [42608604](https://pubmed.ncbi.nlm.nih.gov/42608604/) | SF3B2 truncating variants + zebrafish KO recapitulate CFM | Supports syndromic genes/model (F008) |
| [41289623](https://pubmed.ncbi.nlm.nih.gov/41289623/) | OAV: atresia/ossicular/facial-nerve anomalies scale with severity | Supports syndromic spectrum (F008) |
| [29595733](https://pubmed.ncbi.nlm.nih.gov/29595733/) | Nagata reconstruction; canalplasty/HFM predict unfavorable projection | Supports reconstruction (F009) |

---

## Limitations and Knowledge Gaps

1. **No disease-specific molecular profiling in humans.** There is no transcriptomic, proteomic, metabolomic, or epigenomic signature of isolated human CAA tissue; mechanism is inferred from model organisms and genetics.
2. **Large unexplained genetic fraction.** 42% of Mendelian cases lack a reported inheritance pattern and most isolated unilateral CAA has no identified monogenic cause — the "missing heritability" and the role of the 4p susceptibility locus are unresolved.
3. **GxE interactions are inferred, not demonstrated.** The convergence of maternal diabetes/retinoid signaling onto the neural-crest program is biologically plausible but not mechanistically proven in humans.
4. **Penetrance/expressivity are poorly quantified** for isolated CAA; carrier frequencies and founder effects are undefined.
5. **TSHZ1** is a candidate (single-article) gene for isolated CAA and needs replication and functional validation.
6. **Model gap:** no animal model fully reproduces the human EAC atresia + aberrant facial nerve + conductive rehabilitation problem.
7. **Outcome data heterogeneity:** surgical hearing and reconstruction outcomes come largely from single-surgeon retrospective series; standardized, long-term, multi-center QoL and developmental outcome data are limited.

---

## Proposed Follow-up Experiments / Actions

1. **Functional validation of TSHZ1 and the 4p15.32–4p16.2 locus** in isolated CAA via targeted sequencing/CNV analysis in large microtia-atresia cohorts, plus zebrafish/mouse perturbation.
2. **GxE mechanistic study:** model maternal hyperglycemia and retinoid exposure in neural-crest/arch explants or organoids carrying HOXA2/SF3B2 hypomorphic backgrounds to test convergence on crest survival/patterning.
3. **Single-cell transcriptomics of developing pharyngeal arches** (human embryonic references + models) to map the crest subpopulations most sensitive to spliceosome/ribosome-biogenesis haploinsufficiency.
4. **Prospective multi-center natural-history and developmental-outcome registry** linking laterality, Jahrsdoerfer/aMEI grade, device timing, and standardized language/QoL measures (EQ-5D/PROMIS, GCBI) to refine prognostic models.
5. **Comparative-biology search (OMIA/VetCompass)** for naturally occurring aural atresia/microtia in companion animals to leverage HMX1/Hoxa2 conservation.
6. **Trial of standardized early-amplification protocols** (softband BCD timing) powered on language outcomes, building on the RCT evidence that early input — not the device per se — drives development.
7. **Explore enhancer/epigenetic contributions** (HMX1-type CNVs, HIRE-analogous regulatory elements) by CMA + regulatory-region sequencing in CNV-negative, exome-negative patients.

---

*Evidence source types represented: human clinical (registries, cohorts, imaging, surgical series, RCTs), model organism (mouse, zebrafish, chick), and in-vitro/functional (luciferase enhancer assays, CRISPR knockout). PMIDs are provided for all mechanistic and clinical claims.*


## Artifacts

- [OpenScientist final report](Congenital_Aural_Atresia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Aural_Atresia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 39 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:40644931` (5 mentions) - Alexandrite laser hair removal for pediatric microtia patients undergoing autologous rib cartilage auricular reconstruction: A retrospective analysis.
  - shared terms: microtia

Weighed against this report's own most characteristic terms: `microtia`, `caa`, `atresia`, `hearing`, `genetic`, `gene`, `maternal`, `middle-ear`, `hoxa2`, `ear`, `isolated`, `syndromic`, `loss`, `developmental`, `auditory`, `neural-crest`, `model`, `enhancer`, `conductive`, `diabete`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 15 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 5 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011453` (1 mention) - the report calls it "Abnormality of the middle ear ossicles"; HP calls it **Abnormal incus morphology**, and lists "Abnormality of the incus" among its other names
- `HP:0011452` (1 mention) - the report calls it "Hypoplasia of the middle ear"; HP calls it **Functional abnormality of the middle ear**
- `HP:0010827` (1 mention) - the report calls it "Abnormal facial nerve morphology"; HP calls it **Abnormal seventh cranial physiology**, and lists "Abnormality of the facial nerve" among its other names
- `GO:0060037` (1 mention) - the report calls it "pharyngeal system / branchial-arch morphogenesis"; GO calls it **pharyngeal system development**
- `CL:0000333` (1 mention) - the report calls it "neural crest cell"; CL calls it **migratory neural crest cell**

Every term resolved, and every label the report gave matched.