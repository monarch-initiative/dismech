---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T11:46:40.228713'
end_time: '2026-10-19T12:04:22.557006'
duration_seconds: 1062.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: KIF1A-Related Neurological Disorder
  mondo_id: MONDO:0700055
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
citation_count: 38
reference_validation:
  total_references: 38
  verified: 37
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.026
  quotes_checked: 25
  quotes_valid: 25
  relevance_assessed: 37
  on_topic: 23
  off_topic: 1
  off_topic_references:
  - PMID:42587136
  unresolved_references:
  - PMID:30778698
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 43
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 2
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: KIF1A_Related_Neurological_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KIF1A_Related_Neurological_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KIF1A-Related Neurological Disorder
- **MONDO ID:** MONDO:0700055 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KIF1A-Related Neurological Disorder** covering all of the
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

# KIF1A-Related Neurological Disorder (KAND): Comprehensive Disease Characteristics Report

**Disease:** KIF1A-Related Neurological Disorder (KAND)
**MONDO ID:** MONDO:0700055
**Category:** Mendelian (monogenic neurodevelopmental–neurodegenerative disorder)
**Gene:** *KIF1A* (HGNC:888; NCBI Gene 547; OMIM gene 601255; locus 2q37.3)

---

## Summary

KIF1A-Related Neurological Disorder (KAND) is an ultrarare, clinically highly variable, progressive neurodevelopmental and neurodegenerative Mendelian condition caused by variants in *KIF1A*, which encodes a neuron-specific kinesin-3 motor protein essential for ATP-dependent, superprocessive, microtubule-plus-end-directed anterograde axonal transport of synaptic-vesicle precursors, dense-core vesicles, and organelles. The disorder spans a single allelic continuum encompassing hereditary spastic paraplegia (SPG30), hereditary sensory and autonomic neuropathy (HSAN2C), and the severe neurodevelopmental NESCAV syndrome (neurodegeneration and spasticity with or without cerebellar atrophy or cortical visual impairment; also catalogued as intellectual developmental disorder, autosomal dominant 9 / MRD9). Most severe cases arise from **de novo heterozygous missense variants** concentrated in the motor domain, while recessive (biallelic) variants cause milder, more restricted phenotypes.

The core clinical picture is a near-universal global developmental delay (≈96%), progressive lower-limb spasticity and weakness, near-universal optic nerve atrophy (≈95%), epilepsy, cerebellar atrophy with ataxia, intellectual disability, and peripheral sensory-motor axonopathy. Motor regression is characteristic: although most patients achieve independent walking in early childhood, only a minority retain ambulation into later evaluation, reflecting the neurodegenerative course. The single recurrent variant p.Glu253Lys (E253K) produces the most severe phenotype, including risk of acute encephalopathy with multiorgan failure.

Mechanistically, pathogenic *KIF1A* variants fall into **loss-of-function, hypoactive, hyperactive, and dominant-negative** classes that differentially disrupt cargo trafficking, neurite outgrowth, synapse density, and presynaptic patterning. Because most patients are heterozygous, wild-type/mutant heterodimers are implicated in dominant pathogenesis. Downstream, a TDP-43 proteinopathy branch links KAND to the broader neurodegenerative spectrum (FTLD-TDP / motor neuron disease pathology). No cure exists and management is supportive; however, allele-specific antisense oligonucleotides (first-in-human, safe and showing preliminary benefit) and in vivo prime (gene) editing represent emerging disease-modifying therapies, marking KAND as a frontier for precision medicine in rare neurogenetic disease.

---

## Key Findings

### Finding 1 — KAND is a rare progressive neurodegenerative disorder caused by *KIF1A* variants disrupting kinesin-3 axonal transport

KAND is defined molecularly by pathogenic variants in *KIF1A*, which encodes a kinesin-3 motor protein required for anterograde axonal transport. The authoritative 2026 review by Lin et al. states that *KIF1A* "encodes a kinesin-3 motor protein essential for anterograde axonal transport of synaptic vesicles, dense core vesicles, and organelles in neurons" and that KAND "is a rare, progressive neurodegenerative condition" ([PMID: 41310149](https://pubmed.ncbi.nlm.nih.gov/41310149/)). The disorder "comprises a broad spectrum of overlapping neurological phenotypes, including hereditary spastic paraplegia, intellectual disability, peripheral neuropathy, optic nerve atrophy, epilepsy, and progressive motor decline" ([PMID: 41310149](https://pubmed.ncbi.nlm.nih.gov/41310149/)). This establishes the gene, protein function, core mechanism, and phenotypic breadth that define the entity. Onset, severity, and progression are highly variable, and there is currently no cure—only symptom management.

### Finding 2 — Motor phenotype: near-universal developmental delay, progressive lower-limb spasticity, with E253K most severe

A cross-sectional cohort of 51 individuals (Bernardi et al. 2026) quantified the motor spectrum. Global developmental delay was present in **96.1%** and neonatal/infantile hypotonia in **62.7%**. Progressive spasticity occurred in **72.5%**, predominantly affecting the lower extremities and positively correlated with age (OR = 1.56, 95% CI 1.09–2.25, P = 0.016), while lower-extremity weakness (88.2%) was inversely related to age (OR = 0.93, P = 0.032). The neurodegenerative course is captured by motor regression: "Independent walking was achieved by 62.7% at a median age of 24 months, but only 31.4% retained independent ambulation at last evaluation" ([PMID: 42500835](https://pubmed.ncbi.nlm.nih.gov/42500835/)). Additional movement features included motor stereotypies (43.1%), cerebellar signs (37.2%), ataxia (19.6%), action tremor (15.6%), and dystonia (3.9%). Critically, "The p.Glu253Lys variant was associated with the most severe phenotype" ([PMID: 42500835](https://pubmed.ncbi.nlm.nih.gov/42500835/)), anchoring a genotype–phenotype gradient.

| Motor/movement feature | Frequency | Age relationship |
|---|---|---|
| Global developmental delay | 96.1% | — |
| Neonatal/infantile hypotonia | 62.7% | — |
| Progressive spasticity | 72.5% | Increases with age (OR 1.56) |
| Lower-extremity weakness | 88.2% | Decreases with age (OR 0.93) |
| Independent walking achieved | 62.7% (median 24 mo) | — |
| Independent walking retained | 31.4% | Regression over time |
| Motor stereotypies | 43.1% | — |
| Cerebellar signs | 37.2% | — |
| Ataxia | 19.6% | — |
| Action tremor | 15.6% | — |
| Dystonia | 3.9% | — |

**Suggested HPO terms:** Global developmental delay (HP:0001263), Neonatal hypotonia (HP:0001319), Progressive spastic paraplegia (HP:0007020), Lower limb spasticity (HP:0002061), Intellectual disability (HP:0001249), Ataxia (HP:0001251), Tremor (HP:0001337), Dystonia (HP:0001332), Stereotypy (HP:0000733).

### Finding 3 — Variants cluster in the motor domain and impair superprocessive motility and force generation

Single-molecule and structural studies localize the pathogenic burden to the motor domain. Rao & Gennerich 2022 note that "KAND mutations span the entirety of the KIF1A protein sequence, of which the majority are located within the motor domain and are thus predicted to affect the motor's motility and force-generating properties" ([PMID: 36063335](https://pubmed.ncbi.nlm.nih.gov/36063335/)). The exceptional run length (superprocessivity) of KIF1A is driven by a lysine-rich insertion in loop-12, the "K-loop": Zaniewski & Hancock 2023 report that "superprocessivity of KIF1A dimers originates from a unique structural domain, the lysine-rich insertion in loop-12 termed the 'K-loop', which enhances electrostatic interactions between the motor and the microtubule" ([PMID: 36549649](https://pubmed.ncbi.nlm.nih.gov/36549649/)), with removal of positive charge causing a ~6-fold decrease in run length. More than 100 pathogenic *KIF1A* mutations are known ([PMID: 33931448](https://pubmed.ncbi.nlm.nih.gov/33931448/)). Motility is further tuned by tubulin C-terminal tail polyglutamylation interacting with the K-loop ([PMID: 30770469](https://pubmed.ncbi.nlm.nih.gov/30770469/)).

### Finding 4 — Both de novo autosomal dominant (often dominant-negative) and autosomal recessive (SPG30) inheritance

KAND follows a dual inheritance model. Cheon et al. 2017 state that "Homozygous mutations of KIF1A have been identified in a recessive subtype of hereditary spastic paraplegia (HSP), SPG30. In addition, KIF1A mutations have been found in pure HSP with autosomal dominant inheritance" ([PMID: 28970574](https://pubmed.ncbi.nlm.nih.gov/28970574/)). The dominant mechanism is frequently dominant-negative: a heterozygous p.T258M motor-domain variant showed that "the KIF1A motor domain with p.T258M mutation has reduced motor activity and exerts a dominant negative effect on wild-type KIF1A" ([PMID: 28970574](https://pubmed.ncbi.nlm.nih.gov/28970574/)), producing complicated HSP with intellectual disability, epilepsy, optic atrophy, thin corpus callosum, and microcephaly. Most severe KAND cases arise de novo.

### Finding 5 — Missense variants reduce microtubule-stimulated ATPase activity; E253K causes severe NESCAV with acute encephalopathy risk

Biochemical assays link specific variants to catalytic impairment. Aguilera et al. 2021 report "The Novel KIF1A Missense Variant (R169T) Strongly Reduces Microtubule Stimulated ATPase Activity and Is Associated With NESCAV Syndrome" ([PMID: 34121983](https://pubmed.ncbi.nlm.nih.gov/34121983/)). NESCAVS is "the severest phenotype" among KIF1A disorders (Isobe et al. 2022; [PMID: 34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/)). That report documented a "de novo heterozygous missense variant in KIF1A (NM_001244008.1: c. 757G > A, p.E253K)" ([PMID: 34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/)) causing developmental delay, multifocal epileptic discharges, severe motor and sensory axonopathy, and acute encephalopathy with multiorgan failure (hemorrhagic shock and encephalopathy syndrome), leaving the patient bedridden and gastrostomy-dependent with dysphagia.

### Finding 6 — Variants fall into loss-of-function, hypoactive, and hyperactive classes with distinct synaptic consequences

Isogenic gene-edited human iPSC-derived neurons resolved the functional taxonomy (Aiken et al. 2026): "Null (p.C92*) and hypoactive (p.P305L) mutations delay neurite outgrowth, mislocalize synaptic cargoes, and decrease synapse density. Conversely, a hyperactive (p.R350G) mutation supports neurite outgrowth but causes aberrant motility of synaptic vesicle precursors and deficits in microtubule-dependent presynaptic patterning" ([PMID: 42704317](https://pubmed.ncbi.nlm.nih.gov/42704317/)). Because dominant KAND patients retain a wild-type allele, heterodimers matter: "Most patients are heterozygous and have both mutated and intact KIF1A alleles, suggesting that heterodimers composed of wild-type KIF1A and mutant KIF1A are likely involved in pathogenesis" (Kita et al. 2023; [PMID: 37853694](https://pubmed.ncbi.nlm.nih.gov/37853694/)). KIF1A also transports TDP-43 mRNA cargo in axons ([PMID: 42853422](https://pubmed.ncbi.nlm.nih.gov/42853422/)).

| Functional class | Example variant | Neurite outgrowth | Synaptic phenotype |
|---|---|---|---|
| Null (loss-of-function) | p.C92* | Delayed | Mislocalized cargo, ↓ synapse density |
| Hypoactive | p.P305L | Delayed | Mislocalized cargo, ↓ synapse density, delayed maturation |
| Hyperactive | p.R350G | Supported | Aberrant SVP motility, presynaptic patterning deficits, precocious activity |
| Dominant-negative | p.T258M | — | Reduced WT motor activity via heterodimers |

### Finding 7 — Optic nerve atrophy is the primary, near-universal ocular manifestation (~95%), progressive with age

The KOALA ophthalmic study (Abdelhakim et al. 2024; n = 24) found that "Ninety-five percent of participants examined had some degree of optic nerve atrophy detected by clinical examination and/or optical coherence tomography (OCT)" and concluded that "Optic nerve atrophy is the primary ocular finding in individuals with KAND and is present at higher prevalence than previously reported" ([PMID: 39009236](https://pubmed.ncbi.nlm.nih.gov/39009236/)). Approximately 40% had strabismus, with impaired color vision, visual fields, and stereopsis in most. Visual evoked potentials showed slowing/diffuseness consistent with optic neuropathy even absent overt structural change. Vision declines with age: "Adults had worse vision on average than children, suggesting possible decline in vision with age" ([PMID: 39009236](https://pubmed.ncbi.nlm.nih.gov/39009236/))—mean central acuity 20/43 in children versus 20/119 in adults.

**Suggested HPO terms:** Optic atrophy (HP:0000648), Strabismus (HP:0000486), Reduced visual acuity (HP:0007663), Abnormal visual evoked potentials (HP:0000649).

### Finding 8 — Cross-species models: *C. elegans* unc-104, Kif1a-null mice (neonatal lethal), patient iPSC neurons

KIF1A biology is deeply conserved. Yonekawa et al. 1998 established that "KIF1A, a murine homologue of unc-104 gene of Caenorhabditis elegans, is a unique monomeric neuron-specific microtubule plus end-directed motor" and that knockout mice "died mostly within a day after birth showing motor and sensory disturbances. In the nervous systems of these mutants, the transport of synaptic vesicle precursors showed a specific and significant decrease" ([PMID: 9548721](https://pubmed.ncbi.nlm.nih.gov/9548721/)), with decreased synaptic vesicle density and marked neuronal degeneration. The *C. elegans* UNC-104 is the founding kinesin-3; its processivity is regulated by SAM-4 ([PMID: 25329901](https://pubmed.ncbi.nlm.nih.gov/25329901/)), SYD-2/liprin-α ([PMID: 26354975](https://pubmed.ncbi.nlm.nih.gov/26354975/)), EBP-1/EB1 ([PMID: 37586371](https://pubmed.ncbi.nlm.nih.gov/37586371/)), and FBXB-65 ([PMID: 38477340](https://pubmed.ncbi.nlm.nih.gov/38477340/)). Human patient-derived iPSC neurons recapitulate trafficking and synaptic deficits ([PMID: 42704317](https://pubmed.ncbi.nlm.nih.gov/42704317/); [PMID: 42241928](https://pubmed.ncbi.nlm.nih.gov/42241928/)).

### Finding 9 — No cure exists; allele-specific ASOs and in vivo gene editing are emerging disease-modifying therapies

Current care is supportive only. The landmark first-in-human intervention (Ziegler et al. 2024) treated a patient with severe KAND (p.Pro305Leu) "with intrathecal injections of an allele-specific antisense oligonucleotide specifically designed to degrade the mRNA from the pathogenic allele" ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/)); it was safe over 9 months and "Most outcome measures, including severity of the spells of behavioral arrest, number of falls and quality of life, improved" ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/)). Zuccaro et al. 2026 broadened the strategy: ASOs targeting common polymorphisms in cis with pathogenic variants could in principle treat 54/56 individuals, and "antisense oligonucleotide-mediated knockdown of the pathogenic transcript rescues the dendrite neurite outgrowth phenotype in neurons from a patient with the P305L variant" ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/)). In vivo prime editing corrected a pathogenic *KIF1A* mutation in a KAND mouse brain ([PMID: 42587136](https://pubmed.ncbi.nlm.nih.gov/42587136/)). Symptomatic therapy includes antiseizure medications (e.g., cannabidiol; [PMID: 41630268](https://pubmed.ncbi.nlm.nih.gov/41630268/)) and spasticity management. ASOs are highlighted among emerging childhood movement-disorder therapies ([PMID: 42723627](https://pubmed.ncbi.nlm.nih.gov/42723627/)).

### Finding 10 — Diagnosis relies on molecular genetic testing supported by neurophysiology, OCT/VEP, and MRI

Because clinical features overlap and are non-specific, gene-level diagnosis is essential. Paprocka 2023 "underlined the difficulties in classifying particular syndromes due to non-specific and overlapping signs and symptoms, sometimes observed only temporarily" ([PMID: 37239332](https://pubmed.ncbi.nlm.nih.gov/37239332/)). Diagnosis is typically made by exome or genome sequencing or HSP/neurodevelopmental gene panels (e.g., TruSight One; [PMID: 30778698](https://pubmed.ncbi.nlm.nih.gov/30778698/)). Supportive studies: nerve conduction studies reveal severe motor/sensory axonopathy and EEG shows epileptic discharges ([PMID: 34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/)); OCT and VEP detect optic neuropathy (~95% atrophy; [PMID: 39009236](https://pubmed.ncbi.nlm.nih.gov/39009236/)); brain MRI commonly shows cerebellar atrophy/hypoplasia—KIF1A is among "The most prevalent genes were CACNA1A, ITPR1, and KIF1A" in childhood cerebellar atrophy cohorts ([PMID: 36305856](https://pubmed.ncbi.nlm.nih.gov/36305856/))—plus thin corpus callosum and microcephaly ([PMID: 28970574](https://pubmed.ncbi.nlm.nih.gov/28970574/)).

### Finding 11 — Genotype–inheritance–phenotype allelic series

Ylikallio et al. 2015 crystallized the allelic logic: "Recessive missense variants have led to spastic paraplegia, and recessive truncations to sensory and autonomic neuropathy. De novo missense variants cause developmental delay or intellectual disability, cerebellar atrophy and variable spasticity" ([PMID: 25585697](https://pubmed.ncbi.nlm.nih.gov/25585697/)). The same study reported the first dominantly inherited variant (father-to-son p.Ser69Leu motor-domain variant causing pure spastic paraplegia): "Our study reports the first dominantly inherited KIF1A variant and expands the spectrum of phenotypes caused by heterozygous KIF1A motor domain variants to include pure spastic paraplegia" ([PMID: 25585697](https://pubmed.ncbi.nlm.nih.gov/25585697/)). Associated OMIM phenotypes: **SPG30 (#610357)**, **NESCAV syndrome / MRD9 (#614255)**, **HSAN2C (#614213)**.

| Zygosity / variant type | Phenotype | OMIM |
|---|---|---|
| Recessive missense | Spastic paraplegia (SPG30) | #610357 |
| Recessive truncating | Sensory & autonomic neuropathy (HSAN2C) | #614213 |
| De novo heterozygous missense | DD/ID, cerebellar atrophy, spasticity (NESCAV/MRD9) | #614255 |
| Dominant inherited missense | Pure spastic paraplegia | — |

### Finding 12 — Epidemiology and genetics: 2q37.3, ultrarare (~1/64,000 children), mostly de novo, pediatric-onset

Ortiz-Ortigosa et al. 2023 report that KAND is "caused by mutations in the KIF1A gene (Kinesin family member 1A) located on chromosome 2q37.3" ([PMID: 37668235](https://pubmed.ncbi.nlm.nih.gov/37668235/)). In their pediatric series (4 patients, ages 1–13 y; median symptom onset 5 months), the estimated prevalence "represents an approximate prevalence of 1 per 64,000 children under 14 years of age for our pediatric population" ([PMID: 37668235](https://pubmed.ncbi.nlm.nih.gov/37668235/)). Core features: intellectual disability, axial hypotonia and spastic paraparesis (4/4), cerebellar symptoms (2/4), urinary incontinence, sensory-motor polyneuropathy, behavioral alteration, and focal epilepsy with secondary generalization. Most pathogenic variants are de novo. Gene identifiers: HGNC:888; NCBI Gene 547; OMIM gene 601255.

### Finding 13 — Long projection neurons affected, with downstream TDP-43 proteinopathy

Cellular targets inferred from phenotype and pathology include corticospinal upper motor neurons (spastic paraplegia), retinal ganglion cells/optic nerve (optic atrophy ~95%), cerebellar/Purkinje neurons (ataxia, cerebellar atrophy), peripheral sensory and motor neurons (axonopathy), and cerebral cortex (ID, epilepsy). A neurodegenerative TDP-43 branch is now documented: Homayoun et al. 2025 found that "Quantitative imaging of patient iPSC neurons identified TDP-43 mislocalization to the soma and dendritic atrophy" ([PMID: 40543705](https://pubmed.ncbi.nlm.nih.gov/40543705/)), with autopsy revealing tauopathy and TDP-43 proteinopathy in the brainstem. Saito et al. 2026 reported an autopsied childhood-onset KAND patient with FTLD-TDP43 and motor neuron disease pathology, "suggesting that HSP and FTLD-MND share a pathological continuum through a TDP-43-related pathway and expanding the clinicopathological spectrum of KAND" ([PMID: 42130092](https://pubmed.ncbi.nlm.nih.gov/42130092/)).

---

## Report by Template Section

### 1. Disease Information
KAND is a monogenic kinesin-3 motor disorder of neurons. **Identifiers:** MONDO:0700055; OMIM gene 601255; OMIM phenotypes #610357 (SPG30), #614255 (NESCAV/MRD9), #614213 (HSAN2C); Orphanet includes KIF1A-related spastic paraplegia/NESCAV entries; HGNC:888; NCBI Gene 547. **Synonyms/alternative names:** KIF1A-Associated Neurological Disorder; NESCAV syndrome; spastic paraplegia 30 (SPG30); hereditary sensory and autonomic neuropathy type 2C (HSAN2C); intellectual developmental disorder, autosomal dominant 9 (MRD9). Information is derived primarily from **aggregated disease-level resources and small clinical cohorts/case series** (e.g., 51-patient and 24-patient cohorts), not large EHR datasets, reflecting the disorder's rarity ([PMID: 41310149](https://pubmed.ncbi.nlm.nih.gov/41310149/); [PMID: 42500835](https://pubmed.ncbi.nlm.nih.gov/42500835/)).

### 2. Etiology
**Causal factor:** genetic—pathogenic variants in *KIF1A*. **Genetic risk:** the causal variant itself is the determinant; the majority of severe cases are de novo heterozygous missense variants in the motor domain, with recessive biallelic variants producing milder/restricted phenotypes ([PMID: 25585697](https://pubmed.ncbi.nlm.nih.gov/25585697/)). No established **environmental risk or protective factors**, no infectious trigger, and no documented gene–environment interactions exist for disease causation—KAND is essentially fully genetically determined. One acute encephalopathy episode (E253K) was precipitated in the context of systemic illness, implying illness/fever may act as a decompensating stressor in the most severe genotypes ([PMID: 34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/)), though this is anecdotal. Modifier genes are not yet defined; the retained wild-type allele and heterodimer composition modulate severity ([PMID: 37853694](https://pubmed.ncbi.nlm.nih.gov/37853694/)).

### 3. Phenotypes
The dominant phenotypes, types, and frequencies (from the 51-patient cohort unless noted) are summarized in Finding 2's table. Phenotype **types** span clinical signs (spasticity, hypotonia, optic atrophy), symptoms (developmental delay, visual decline), behavioral changes (stereotypies, autism features; a de novo missense variant has been linked to ASD, [PMID: 41868953](https://pubmed.ncbi.nlm.nih.gov/41868953/)), and laboratory/neurophysiologic abnormalities (axonopathy on NCS, epileptic EEG). **Onset:** predominantly neonatal/infantile to childhood; **severity:** variable (mild pure HSP to severe NESCAV); **progression:** progressive/neurodegenerative with motor regression. **Quality-of-life impact** is substantial: loss of ambulation, visual impairment, dysphagia requiring gastrostomy in severe cases ([PMID: 34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/)), and seizures. Suggested HPO terms are listed in Findings 2 and 7, plus Optic atrophy (HP:0000648), Seizure (HP:0001250), Cerebellar atrophy (HP:0001272), Peripheral axonal neuropathy (HP:0003477), Thin corpus callosum (HP:0033725), Microcephaly (HP:0000252).

### 4. Genetic/Molecular Information
**Causal gene:** *KIF1A* (2q37.3; OMIM 601255). **Variant classes:** predominantly missense (motor domain), plus truncating/nonsense (recessive HSAN2C) and splice variants; >100 pathogenic variants catalogued ([PMID: 33931448](https://pubmed.ncbi.nlm.nih.gov/33931448/)). **ACMG classification:** recurrent variants (E253K, P305L, T258M, R350G, R169T, S69L, N222H) are classified pathogenic/likely pathogenic; novel variants are interpreted per ACMG, with VUS common in milder presentations ([PMID: 41168819](https://pubmed.ncbi.nlm.nih.gov/41168819/); [PMID: 38301322](https://pubmed.ncbi.nlm.nih.gov/38301322/)). **Allele frequency:** pathogenic dominant variants are essentially absent from gnomAD (de novo). **Origin:** germline (de novo or inherited); no somatic/cancer role established. **Functional consequences:** loss-of-function, hypoactive, hyperactive, and dominant-negative ([PMID: 42704317](https://pubmed.ncbi.nlm.nih.gov/42704317/); [PMID: 28970574](https://pubmed.ncbi.nlm.nih.gov/28970574/)). **Epigenetics:** no disease-causing epigenetic mechanism; of note, *Kif1a* expression is itself epigenetically regulated (SP1–TET1-mediated promoter demethylation in a chronic migraine model; [PMID: 41723361](https://pubmed.ncbi.nlm.nih.gov/41723361/)), but this is not a KAND causal mechanism. **Chromosomal abnormalities:** not a feature—KAND is a single-gene point-variant disorder.

### 5. Environmental Information
No established environmental, lifestyle, or infectious contributors to KAND causation. The disorder is monogenic and essentially fully penetrant for severe de novo genotypes. Intercurrent systemic illness may precipitate acute encephalopathic decompensation in the most severe genotype (E253K) but is not a cause of the disorder ([PMID: 34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A germline *KIF1A* variant (most often a de novo heterozygous missense in the motor domain) **leads to** an altered kinesin-3 motor protein. *(Demonstrated.)*
2. The altered motor domain **results in** disrupted ATP hydrolysis/microtubule binding—e.g., reduced microtubule-stimulated ATPase activity (R169T), impaired ATP binding (S69L), or altered motility (loss-of-function/hypoactive/hyperactive). *(Demonstrated biochemically; [PMID: 34121983](https://pubmed.ncbi.nlm.nih.gov/34121983/); [PMID: 36063335](https://pubmed.ncbi.nlm.nih.gov/36063335/).)*
3. In heterozygotes, mutant protein **forms** WT/mutant heterodimers that **exert** dominant-negative drag on the intact motor, reducing effective transport (branch A); in nulls/hypoactive alleles, transport capacity is simply reduced (branch B); in hyperactive alleles, cargo is mis-trafficked by excessive/aberrant motility (branch C). *(Demonstrated in iPSC neurons/modeling; [PMID: 37853694](https://pubmed.ncbi.nlm.nih.gov/37853694/); [PMID: 42704317](https://pubmed.ncbi.nlm.nih.gov/42704317/).)*
4. Disrupted anterograde axonal transport **leads to** mislocalization of synaptic-vesicle precursors, dense-core vesicles, organelles, and mRNA cargo (including TDP-43 mRNA). *(Demonstrated; [PMID: 9548721](https://pubmed.ncbi.nlm.nih.gov/9548721/); [PMID: 42853422](https://pubmed.ncbi.nlm.nih.gov/42853422/).)*
5. Cargo mislocalization **results in** delayed neurite outgrowth, decreased synapse density, aberrant presynaptic patterning, and delayed synaptic maturation. *(Demonstrated; [PMID: 42704317](https://pubmed.ncbi.nlm.nih.gov/42704317/).)*
6. These synaptic/transport deficits **lead to** dysfunction and progressive degeneration of long projection neurons—corticospinal, retinal ganglion, cerebellar, and peripheral sensory/motor. *(Inferred from phenotype + mouse degeneration; [PMID: 9548721](https://pubmed.ncbi.nlm.nih.gov/9548721/).)*
7. Downstream (neurodegenerative branch), transport failure **contributes to** TDP-43 mislocalization to the soma, dendritic atrophy, and ultimately TDP-43/tau proteinopathy. *(Demonstrated in iPSC + autopsy; [PMID: 40543705](https://pubmed.ncbi.nlm.nih.gov/40543705/); [PMID: 42130092](https://pubmed.ncbi.nlm.nih.gov/42130092/).)*
8. Neuronal dysfunction/degeneration across these circuits **manifests as** developmental delay/ID, progressive spastic paraplegia, optic atrophy, epilepsy, ataxia, and peripheral neuropathy. *(Clinically demonstrated.)*

```
KIF1A motor-domain variant
          │
          ▼
Altered ATPase / microtubule binding
          │
   ┌──────┼─────────────┐
   ▼      ▼             ▼
Dominant-  LoF/       Hyperactive
negative   hypoactive  (aberrant motility)
(heterodimer)
   └──────┼─────────────┘
          ▼
Impaired anterograde axonal transport (SVPs, DCVs, mRNA/TDP-43)
          │
          ▼
↓ neurite outgrowth, ↓ synapse density, aberrant presynaptic patterning
          │
          ▼
Dysfunction/degeneration of long projection neurons
          │
          ▼  (downstream branch)
TDP-43 mislocalization → dendritic atrophy → TDP-43/tau proteinopathy
          │
          ▼
DD/ID · spastic paraplegia · optic atrophy · epilepsy · ataxia · neuropathy
```

**Molecular pathways/processes:** anterograde axonal transport (**GO:0008089**), microtubule-based transport (**GO:0099118/GO:0010970**), synaptic vesicle transport (**GO:0048489**), ATP hydrolysis-coupled motor activity. **Protein dysfunction:** loss/gain/dominant-negative motor function. **Cell types (CL):** corticospinal/upper motor neuron (CL:0000679 glutamatergic neuron / pyramidal), retinal ganglion cell (**CL:0000740**), cerebellar Purkinje cell (**CL:0000121**), peripheral sensory neuron (**CL:0000101**), motor neuron (**CL:0000100**). **Subcellular (GO CC):** axon (**GO:0030424**), microtubule (**GO:0005874**), synaptic vesicle (**GO:0008021**), kinesin complex (**GO:0005871**).

### 7. Anatomical Structures Affected
**Primary organ/system:** central and peripheral **nervous system (UBERON:0001016)**. **Specific sites:** corticospinal tracts / spinal cord (**UBERON:0002240**), optic nerve (**UBERON:0000941**) and retina (**UBERON:0000966**), cerebellum (**UBERON:0002037**), cerebral cortex (**UBERON:0000956**), corpus callosum (**UBERON:0002336**, thinning), peripheral nerves (**UBERON:0001021**). **Lateralization:** bilateral/symmetric for spasticity, optic atrophy, and neuropathy. **Tissue:** nervous tissue; **cells:** long projection neurons (see Finding 13). Secondary involvement includes bladder (neurogenic, urinary incontinence) and GI (dysphagia) via neurological impairment.

### 8. Temporal Development
**Onset:** typically congenital/neonatal to early childhood (median symptom onset ~5 months in one series; [PMID: 37668235](https://pubmed.ncbi.nlm.nih.gov/37668235/)); milder dominant/recessive HSP forms can present later, including adult-onset less severe phenotypes ([PMID: 41585230](https://pubmed.ncbi.nlm.nih.gov/41585230/)). **Onset pattern:** insidious/chronic, occasionally with acute encephalopathic decompensation in severe genotypes. **Progression:** progressive and neurodegenerative—spasticity increases with age while ambulation is often lost (independent walking retained by only 31.4%; [PMID: 42500835](https://pubmed.ncbi.nlm.nih.gov/42500835/)) and vision declines with age ([PMID: 39009236](https://pubmed.ncbi.nlm.nih.gov/39009236/)). **Course:** chronic, lifelong; no spontaneous remission. **Critical window:** early childhood (active neurodevelopment/synaptogenesis) is both the period of peak vulnerability and the proposed window of therapeutic opportunity for ASO/editing approaches.

### 9. Inheritance and Population
**Epidemiology:** ultrarare; approximate prevalence ~1 per 64,000 children under 14 in one pediatric population ([PMID: 37668235](https://pubmed.ncbi.nlm.nih.gov/37668235/)); true population incidence/prevalence not firmly established. **Inheritance:** autosomal dominant (mostly de novo; occasionally inherited) and autosomal recessive (SPG30, HSAN2C) ([PMID: 28970574](https://pubmed.ncbi.nlm.nih.gov/28970574/); [PMID: 25585697](https://pubmed.ncbi.nlm.nih.gov/25585697/)). **Penetrance:** high/complete for severe de novo missense variants; **expressivity:** highly variable. **Anticipation:** not a feature (not a repeat-expansion disorder). **Mosaicism/founder effects/consanguinity:** germline mosaicism possible but not well quantified; recessive forms more likely in consanguineous pedigrees; no major founder variants defined. **Demographics:** no strong ethnic predilection; de novo origin predicts broad geographic distribution. **Sex ratio:** no strong sex bias reported. **Age distribution:** predominantly pediatric at diagnosis.

### 10. Diagnostics
**Genetic testing is the diagnostic cornerstone** (Finding 10): exome/genome sequencing or HSP/NDD gene panels; single-gene testing confirms recurrent variants; chromosomal microarray/karyotype are not informative (point variants). **Supportive tests:** nerve conduction studies (motor/sensory axonopathy), EEG (epileptic discharges), OCT and VEP (optic neuropathy, ~95% atrophy), brain MRI (cerebellar atrophy/hypoplasia, thin corpus callosum, microcephaly). **Differential diagnosis:** other HSP subtypes (SPAST/SPG4, ATL1/SPG3, KIF5A/SPG10, SPG11), other cerebellar-atrophy genes (CACNA1A, ITPR1), and broader NDD/kinesinopathies ([PMID: 36305856](https://pubmed.ncbi.nlm.nih.gov/36305856/); [PMID: 30778698](https://pubmed.ncbi.nlm.nih.gov/30778698/); [PMID: 42651835](https://pubmed.ncbi.nlm.nih.gov/42651835/)). Clinical overlap makes molecular confirmation essential ([PMID: 37239332](https://pubmed.ncbi.nlm.nih.gov/37239332/)). **Screening:** no population newborn screening; cascade/targeted testing of family members is relevant chiefly for recessive and rare inherited dominant variants.

### 11. Outcome/Prognosis
**Survival/mortality:** variable—mild pure HSP forms are compatible with normal lifespan; severe NESCAV with acute encephalopathy and multiorgan failure carries high morbidity and mortality risk ([PMID: 34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/)). **Morbidity/disability:** substantial—progressive loss of ambulation, visual impairment, cognitive impairment, epilepsy, dysphagia/gastrostomy dependence. **Disease course:** progressive with motor and visual regression. **Prognostic factors:** variant identity/functional class is the strongest determinant—E253K predicts the most severe phenotype; motor-domain missense and dominant-negative mechanisms predict worse outcomes; recessive missense (SPG30) and some adult-onset dominant variants predict milder courses ([PMID: 42500835](https://pubmed.ncbi.nlm.nih.gov/42500835/); [PMID: 41585230](https://pubmed.ncbi.nlm.nih.gov/41585230/)). **Recovery potential:** limited spontaneously; disease-modifying therapy may alter trajectory (emerging).

### 12. Treatment
**Current standard = supportive/symptomatic** (NCIT: Supportive Care): antiseizure medications (e.g., cannabidiol; [PMID: 41630268](https://pubmed.ncbi.nlm.nih.gov/41630268/)), antispasticity agents and physical/occupational/speech therapy, nutritional support (gastrostomy in severe dysphagia), visual aids, and orthopedic/rehabilitative management. **Disease-modifying/experimental:** allele-specific antisense oligonucleotide (intrathecal, first-in-human, safe with preliminary benefit; [PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/)); polymorphism-targeted ASOs expanding eligibility to ~54/56 individuals ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/)); in vivo prime editing correcting the mutation in mouse brain ([PMID: 42587136](https://pubmed.ncbi.nlm.nih.gov/42587136/)). These are reviewed among emerging childhood movement-disorder therapies ([PMID: 42723627](https://pubmed.ncbi.nlm.nih.gov/42723627/)). **Pharmacogenomics/targeted/immuno/cell therapy:** not established. **Personalized medicine:** the allele-specific ASO paradigm makes KAND an exemplar of variant-tailored therapy. **Suggested NCIT terms:** Antisense Oligonucleotide Therapy, Gene Editing, Supportive Care, Anticonvulsant Therapy, Physical Therapy.

### 13. Prevention
**Primary prevention:** not applicable for de novo variants; **genetic counseling** is central—recurrence risk is low for de novo cases but 25% for recessive carrier couples and up to 50% for an affected dominant transmitter. **Reproductive options:** prenatal diagnosis and preimplantation genetic testing for known familial variants. **Secondary/tertiary prevention:** early multidisciplinary surveillance (vision/OCT, EEG, developmental monitoring) and complication management (seizure control, aspiration/nutrition, contracture prevention). No vaccine or public-health/environmental prevention applies.

### 14. Other Species / Natural Disease
**Orthologs:** mouse *Kif1a* (NCBI Gene 16560) and *C. elegans* unc-104 are the principal orthologs; *Kif1a*-null mice are neonatal-lethal with transport and degeneration defects ([PMID: 9548721](https://pubmed.ncbi.nlm.nih.gov/9548721/)). **Taxonomy:** *Mus musculus* (NCBITaxon:10090), *Caenorhabditis elegans* (NCBITaxon:6239). **Evolutionary conservation:** the kinesin-3 motor and its transport function are deeply conserved from nematode to human, underpinning model-organism validity. No prominent naturally occurring companion-animal/wildlife disease or zoonotic/cross-species transmission is relevant (KAND is a non-transmissible genetic disorder).

### 15. Model Organisms
- **Mouse (MGI):** *Kif1a* knockout—neonatal-lethal, synaptic-vesicle-precursor transport deficit, decreased synaptic vesicle density, neuronal degeneration ([PMID: 9548721](https://pubmed.ncbi.nlm.nih.gov/9548721/)); KAND knock-in models now used for in vivo editing ([PMID: 42587136](https://pubmed.ncbi.nlm.nih.gov/42587136/)). Recapitulates transport/degeneration but homozygous lethality limits lifespan studies.
- **C. elegans (WormBase):** unc-104 temperature-sensitive and point alleles—reduced locomotion and axonal synaptic-vesicle levels; powerful for dissecting processivity regulation (SAM-4, SYD-2, EBP-1, FBXB-65, LRK-1/AP-3) ([PMID: 25329901](https://pubmed.ncbi.nlm.nih.gov/25329901/); [PMID: 26354975](https://pubmed.ncbi.nlm.nih.gov/26354975/); [PMID: 37586371](https://pubmed.ncbi.nlm.nih.gov/37586371/); [PMID: 38477340](https://pubmed.ncbi.nlm.nih.gov/38477340/); [PMID: 38722918](https://pubmed.ncbi.nlm.nih.gov/38722918/)).
- **Human iPSC-derived neurons (Cellosaurus/iPSC):** isogenic gene-edited and patient-derived lines recapitulate neurite-outgrowth, cargo-mislocalization, synapse-density, and TDP-43 phenotypes; central to functional classification and ASO proof-of-concept ([PMID: 42704317](https://pubmed.ncbi.nlm.nih.gov/42704317/); [PMID: 42241928](https://pubmed.ncbi.nlm.nih.gov/42241928/); [PMID: 40543705](https://pubmed.ncbi.nlm.nih.gov/40543705/)).
- **In vitro single-molecule assays:** purified KIF1A motors for motility/ATPase/force measurements ([PMID: 36063335](https://pubmed.ncbi.nlm.nih.gov/36063335/); [PMID: 36549649](https://pubmed.ncbi.nlm.nih.gov/36549649/)).

---

## Mechanistic Model / Interpretation

KAND is best understood as a **single allelic continuum of an axonal-transport motor disease**. One gene, *KIF1A*, produces a graded spectrum because distinct variants perturb the motor in mechanistically distinct ways (loss-of-function, hypoactive, hyperactive, dominant-negative), and because zygosity and the retained wild-type allele set the effective transport capacity. The unifying lesion is **impaired anterograde delivery of synaptic and organellar cargo to the distal ends of the longest neurons**, which are the first to decompensate—explaining the length-dependent phenotype (corticospinal → spastic paraplegia; retinal ganglion → optic atrophy; peripheral sensory/motor → neuropathy; cerebellar circuits → ataxia). Early-childhood synaptogenesis is the window of greatest vulnerability, and the progressive, regressive course plus the emerging TDP-43 proteinopathy place KAND at the interface of **neurodevelopmental and neurodegenerative** disease. Therapeutically, because the dominant form depends on a toxic mutant allele acting through heterodimers, **allele-specific silencing (ASO) or direct correction (prime editing)** are mechanistically rational and already show early human and preclinical success.

---

## Evidence Base (Key Literature)

| PMID | Role in report | Contribution |
|---|---|---|
| [41310149](https://pubmed.ncbi.nlm.nih.gov/41310149/) | Supports F001, F009 | Defines disease, gene, mechanism, phenotype spectrum; no cure |
| [42500835](https://pubmed.ncbi.nlm.nih.gov/42500835/) | Supports F002 | 51-patient motor cohort; frequencies; E253K severity |
| [36063335](https://pubmed.ncbi.nlm.nih.gov/36063335/) | Supports F003 | Motor-domain localization; motility/force |
| [36549649](https://pubmed.ncbi.nlm.nih.gov/36549649/) | Supports F003 | K-loop basis of superprocessivity |
| [28970574](https://pubmed.ncbi.nlm.nih.gov/28970574/) | Supports F004 | Dominant-negative (T258M); SPG30 recessive/dominant |
| [34121983](https://pubmed.ncbi.nlm.nih.gov/34121983/) | Supports F005 | R169T reduces ATPase; NESCAV |
| [34916088](https://pubmed.ncbi.nlm.nih.gov/34916088/) | Supports F005 | E253K; NESCAVS severest; acute encephalopathy |
| [42704317](https://pubmed.ncbi.nlm.nih.gov/42704317/) | Supports F006 | Null/hypoactive/hyperactive functional classes |
| [37853694](https://pubmed.ncbi.nlm.nih.gov/37853694/) | Supports F006 | Heterodimer pathogenesis |
| [39009236](https://pubmed.ncbi.nlm.nih.gov/39009236/) | Supports F007 | KOALA study; ~95% optic atrophy; age decline |
| [9548721](https://pubmed.ncbi.nlm.nih.gov/9548721/) | Supports F008 | Kif1a-null mouse; unc-104 orthology |
| [39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/) | Supports F009 | First-in-human allele-specific ASO |
| [41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/) | Supports F009 | Polymorphism-targeted ASO; in vitro rescue |
| [42587136](https://pubmed.ncbi.nlm.nih.gov/42587136/) | Supports F009 | In vivo prime editing in KAND mouse |
| [37239332](https://pubmed.ncbi.nlm.nih.gov/37239332/) | Supports F010 | Clinical overlap → molecular diagnosis |
| [36305856](https://pubmed.ncbi.nlm.nih.gov/36305856/) | Supports F010 | KIF1A among top cerebellar-atrophy genes |
| [25585697](https://pubmed.ncbi.nlm.nih.gov/25585697/) | Supports F011 | Allelic series; first dominant variant |
| [37668235](https://pubmed.ncbi.nlm.nih.gov/37668235/) | Supports F012 | Locus 2q37.3; ~1/64,000 prevalence |
| [40543705](https://pubmed.ncbi.nlm.nih.gov/40543705/) | Supports F013 | TDP-43 mislocalization, dendritic atrophy |
| [42130092](https://pubmed.ncbi.nlm.nih.gov/42130092/) | Supports F013 | FTLD-TDP/MND continuum autopsy |

Supporting/contextual literature: kinesinopathy review ([PMID: 42651835](https://pubmed.ncbi.nlm.nih.gov/42651835/)), HSP NGS panels ([PMID: 30778698](https://pubmed.ncbi.nlm.nih.gov/30778698/)), TDP-43 axonal transport ([PMID: 42853422](https://pubmed.ncbi.nlm.nih.gov/42853422/)), emerging therapies review ([PMID: 42723627](https://pubmed.ncbi.nlm.nih.gov/42723627/)), adult/milder genotype–phenotype ([PMID: 41585230](https://pubmed.ncbi.nlm.nih.gov/41585230/)), ASD association ([PMID: 41868953](https://pubmed.ncbi.nlm.nih.gov/41868953/)), and C. elegans regulatory studies ([PMID: 25329901](https://pubmed.ncbi.nlm.nih.gov/25329901/); [PMID: 26354975](https://pubmed.ncbi.nlm.nih.gov/26354975/); [PMID: 37586371](https://pubmed.ncbi.nlm.nih.gov/37586371/); [PMID: 38477340](https://pubmed.ncbi.nlm.nih.gov/38477340/); [PMID: 38722918](https://pubmed.ncbi.nlm.nih.gov/38722918/)).

---

## Limitations and Knowledge Gaps

- **Epidemiology is weak:** the ~1/64,000 estimate derives from a single small pediatric series ([PMID: 37668235](https://pubmed.ncbi.nlm.nih.gov/37668235/)); true incidence, prevalence, sex ratio, and ethnic/geographic distribution are not robustly established.
- **Cohorts are small** (tens of patients), limiting statistical power for genotype–phenotype correlation beyond strong signals (E253K severity).
- **Variant-level functional annotation is incomplete:** >100 variants exist but only a handful are biochemically characterized; many remain VUS, complicating prognosis and ASO eligibility.
- **Mechanistic gaps:** how transport failure leads to TDP-43 proteinopathy (cause vs consequence) is not fully resolved; modifier genes are undefined.
- **Natural history and QoL** data are limited; standardized longitudinal outcome measures are still being developed—important for trial endpoints.
- **Therapeutic evidence is early:** the ASO result is n = 1 over 9 months; prime editing is preclinical/mouse. Durability, delivery, and broad applicability remain open.

---

## Proposed Follow-up Experiments / Actions

1. **Build a comprehensive variant–function map:** systematically assay single-molecule motility, ATPase, and iPSC-neuron synaptic phenotypes for the full catalogue of recurrent *KIF1A* variants to assign each to a functional class and enable precise prognosis and therapy selection.
2. **Natural-history registry with standardized endpoints:** prospective, multi-center longitudinal study pairing motor (ambulation), visual (OCT/VEP), cognitive, and seizure metrics with genotype to define progression rates and trial-ready biomarkers.
3. **Expand allele-specific ASO programs:** validate polymorphism-targeting ASOs across diverse genotypes and test in additional patients, with CSF/neurofilament biomarkers of target engagement.
4. **Advance in vivo gene editing** from mouse to larger models, optimizing CNS delivery and quantifying correction efficiency and phenotype rescue.
5. **Dissect the TDP-43 branch:** determine whether TDP-43 mislocalization is a driver or marker of degeneration, and whether transport-restoring therapy reverses proteinopathy—potentially linking KAND therapeutics to broader ALS/FTLD paradigms.
6. **Identify modifiers:** leverage the retained wild-type allele/heterodimer biology and C. elegans regulators (SAM-4, SYD-2, EBP-1, FBXB-65) as candidate modifier pathways and druggable targets for transport enhancement.

---

*Report compiled from 13 confirmed findings across 5 investigative iterations and 52 reviewed papers. Evidence source types span human clinical cohorts, autopsy pathology, model organisms (mouse, C. elegans), patient-derived iPSC neurons, in vitro single-molecule biophysics, and computational modeling.*


## Artifacts

- [OpenScientist final report](KIF1A_Related_Neurological_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KIF1A_Related_Neurological_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 25 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 37 |
| On topic | 23 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:30778698` (7 mentions) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42587136` (8 mentions) - Mechanistic machine learning for prediction of prime editing outcomes.
  - shared terms: disorder

Weighed against this report's own most characteristic terms: `motor`, `variant`, `kif1a`, `kand`, `phenotype`, `gene`, `dominant`, `atrophy`, `severe`, `neuron`, `novo`, `optic`, `patient`, `transport`, `recessive`, `neuropathy`, `cerebellar`, `spastic`, `sensory`, `disorder`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |

42 of 43 terms resolved to a current term; the rest could not be looked up either way.