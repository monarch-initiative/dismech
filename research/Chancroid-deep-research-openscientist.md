---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T22:12:40.907093'
end_time: '2026-09-24T22:26:54.106589'
duration_seconds: 853.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chancroid
  mondo_id: MONDO:0001797
  category: Infectious Disease
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 19
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 16
  verified: 15
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0500089
    reported_labels:
    - genital ulcer
    ontology_label: Optic nerve sheath meningioma
  obsolete_terms:
  - term_id: GO:0007050
    ontology_label: GO_0007050
    replaced_by: GO:0051726
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Chancroid-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chancroid-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chancroid
- **MONDO ID:** MONDO:0001797 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chancroid** covering all of the
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

# Chancroid (MONDO:0001797): Comprehensive Disease Characteristics Report

**Disease:** Chancroid | **MONDO:** MONDO:0001797 | **ICD-10:** A57 | **ICD-11:** 1A75 | **MeSH:** D002602 | **SNOMED CT:** 3419005 | **DO:** DOID:11165 | **Category:** Infectious Disease
**Causative agent:** *Haemophilus ducreyi* (Gram-negative coccobacillus; NCBI Taxon 730)

---

## Summary

Chancroid is an acute, curable, sexually transmitted bacterial infection caused by the fastidious Gram-negative coccobacillus *Haemophilus ducreyi*. It classically presents, after a 3–5 day incubation, as one or more soft, painful, non-indurated genital ulcers with tender regional (inguinal) lymphadenitis that progresses to suppurating buboes in roughly half of affected individuals. It is a **localized infectious disease, not a heritable disorder** — there are no human causal genes, pathogenic germline variants, inheritance patterns, or Mendelian genetics associated with it. Consequently, several sections of the standard disease-characteristics template (causal genes, variant classification, host genetic models, karyotyping, etc.) are **not applicable**; the "genetics" of chancroid resides in the **pathogen genome and virulence factors**, and the "host genetics" is limited to immune-response determinants of infection outcome.

The pathophysiology is driven by a defined set of *H. ducreyi* virulence factors — HgbA-mediated heme/hemoglobin acquisition (an obligate nutritional requirement and a protective vaccine target), DsrA serum resistance, the anti-phagocytic lipoproteins LspA1/LspA2, and the genotoxic tripartite cytolethal distending toxin (CdtA/CdtB/CdtC) — acting together with the **host cutaneous and dendritic-cell immune response**, which ultimately determines whether an inoculation site resolves spontaneously or progresses to a pustule/ulcer. Diagnosis is made within the genital-ulcer-disease (GUD) syndrome by multiplex nucleic acid amplification testing (NAAT/PCR), because *H. ducreyi* culture is insensitive and no FDA-cleared commercial assay is widely available. Treatment is highly effective: single-dose azithromycin 1 g PO or ceftriaxone 250 mg IM, or multi-day ciprofloxacin or erythromycin, with buboes sometimes requiring aspiration or drainage.

Chancroid causes **no direct mortality** and is fully curable, but its dominant public-health importance is as a **cofactor for HIV transmission and acquisition** — the countries with the greatest HIV burden historically had the highest chancroid prevalence. Male circumcision and simple topical hygiene are protective, and the infection depends on high-partner-change sexual networks (commercial sex work), giving it a "precarious epidemiological niche" that makes it locally eradicable. Chancroid has declined dramatically worldwide and is now rare in high-income countries, but persists in endemic pockets (e.g., ~22% of GUD PCR-positive in Malawi, 2019–2022). Notably, over the past two decades *H. ducreyi* has **re-emerged as a major cause of non-sexually-transmitted chronic skin ulcers in children** in yaws-endemic tropical regions, where it is the leading differential diagnosis for yaws.

---

## Key Findings

### F001 — Chancroid is caused by *H. ducreyi* and presents as painful genital ulcers with buboes

Multiple authoritative reviews (2017–2026) converge on the definition of chancroid as a sexually acquired genital ulcerative disease caused by the fastidious Gram-negative coccobacillus *H. ducreyi*, characterized by one or more soft, painful genital ulcers and regional lymphadenitis that may develop into buboes. The 2017 European guideline states: *"Chancroid is a sexually acquired infection caused by Haemophilus ducreyi. The infection is characterized by one or more genital ulcers, which are soft and painful, and regional lymphadenitis, which may develop into buboes"* ([PMID: 28081686](https://pubmed.ncbi.nlm.nih.gov/28081686/)). A 2026 review reaffirms: *"Chancroid, caused by Haemophilus ducreyi, is a sexually transmitted genital ulcerative condition associated with inguinal bubo formation"* ([PMID: 41046959](https://pubmed.ncbi.nlm.nih.gov/41046959/)). Key identifiers: **ICD-10 A57**, **MeSH D002602**, **MONDO:0001797**. This information derives from aggregated disease-level resources (guidelines, reviews) and controlled human infection studies, not individual EHR records.

### F005 — Clinical natural history: 3–5 day incubation, soft painful ulcer, ~50% bubo suppuration

The incubation period is 3–5 days. The typical lesion is a soft, non-indurated ulcer with a dirty exudate at the base that is painful and exquisitely tender to palpation — a presentation that contrasts sharply with the painless, indurated chancre of primary syphilis. Bubo (regional lymphadenitis) formation is common, and about half of buboes suppurate: *"The incubation period is 3-5 days and the typical lesion is a soft nonindurated ulcer with a dirty exudate at the base, which is painful and exquisitely tender to palpation. Bubo formation is common and about half suppurate"* ([PMID: 6687703](https://pubmed.ncbi.nlm.nih.gov/6687703/)). Lesions are usually obvious in males but may go undetected in women. Disease is localized rather than systemic.

**Suggested ontology terms (phenotypes):** genital ulcer (HPO region HP:0500089), inguinal lymphadenopathy, painful skin lesion. **Anatomical (UBERON):** penis (UBERON:0000989), prepuce, labia, inguinal lymph node (UBERON:0002450).

### F003 — CDT and anti-phagocytic Lsp proteins are key virulence factors

*H. ducreyi* cytolethal distending toxin (CDT) is a tripartite toxin (CdtA, CdtB, CdtC). CdtB possesses DNase-I-like activity that produces DNA double-strand breaks, triggering G2/M cell-cycle arrest, cellular distension, and death of epithelial cells, keratinocytes, and immune cells: *"Once inside the cell, CdtB enters the nucleus and exhibits a DNase I-like activity that results in DNA double-strand breaks. The eukaryotic cell responds ... by initiating a regulatory cascade that results in cell cycle arrest, cellular distension, and cell death"* ([PMID: 17123907](https://pubmed.ncbi.nlm.nih.gov/17123907/)).

In the controlled human challenge model, the LspA1/LspA2 proteins (which inhibit phagocytosis) are required to initiate disease. An *lspA1 lspA2* double mutant produced significantly smaller papules and no pustules: *"The pustule formation rates were 44% (95% CI, 5.8 to 77.6%) at parent sites and 0% (95% CI, 0 to 39.4%) at mutant sites (P = 0.009)"* ([PMID: 15271912](https://pubmed.ncbi.nlm.nih.gov/15271912/)). Papule size was 24.8 vs 39.1 mm² (P=0.0002). **Suggested GO terms:** DNA catabolic process/deoxyribonuclease activity (CdtB), negative regulation of phagocytosis (LspA1/A2), cell cycle arrest.

### F007 — Heme acquisition via HgbA is obligate and a protective vaccine target

*H. ducreyi* has an **obligate requirement for heme**, which it acquires from the human host via TonB-dependent transporters. Of three such receptors, only the hemoglobin receptor **HgbA** is required to establish infection in the early human challenge model. Active immunization with native HgbA (nHgbA) confers complete protection in the experimental swine model: *"only the hemoglobin receptor, HgbA, is required to establish infection during the early stages of the experimental human model of chancroid. Active immunization with a native preparation of HgbA (nHgbA) confers complete protection in the experimental swine model of chancroid"* ([PMID: 21646451](https://pubmed.ncbi.nlm.nih.gov/21646451/)). Passive transfer of anti-nHgbA serum protects against homologous (but not heterologous) challenge by blocking hemoglobin binding. HgbA surface loops 4, 5, and 7 are immunogenic; loops 5 and 7 are essential for hemoglobin binding.

### F008 — Infection outcome is determined by the host cutaneous/dendritic-cell immune profile

In experimentally infected human volunteers, the cutaneous response to *H. ducreyi* is orchestrated by serum, polymorphonuclear leukocytes (neutrophils), macrophages, T cells, and myeloid dendritic cells. This response either resolves spontaneously or progresses to pustule formation: *"This response either leads to spontaneous resolution of infection or progresses to pustule formation, which is associated with the failure of phagocytes to ingest the organism and the presence of Th1 and regulatory T cells"* ([PMID: 17893130](https://pubmed.ncbi.nlm.nih.gov/17893130/)). Volunteers reproducibly segregate into **pustule-formers (PP)** and **resolvers (RR)**: RR sites show transcripts of effective immune function, while PP sites show a hyperinflammatory, dysregulated response, with differential dendritic-cell polarization (DC1 vs regulatory DC). This is the closest thing to a **host-immunological susceptibility determinant** for chancroid. **Suggested CL terms:** neutrophil (CL:0000775), macrophage (CL:0000235), myeloid dendritic cell (CL:0000782), T-helper 1 cell, regulatory T cell.

### F004 — Treatment: single-dose azithromycin or ceftriaxone; multi-day ciprofloxacin/erythromycin

Recommended first-line therapies are azithromycin 1 g PO once, ceftriaxone 250 mg IM once, or erythromycin 500 mg PO 4×/day for 7 days; ciprofloxacin 500 mg twice daily for 3 days is an effective alternative: *"The recommended therapies--with azithromycin (1 g orally, once), ceftriaxone (250 mg intramuscularly, once), or erythromycin (500 mg orally, four times a day for 7 days)--appear highly effective in the United States"* ([PMID: 10028106](https://pubmed.ncbi.nlm.nih.gov/10028106/)). HIV-infected and uncircumcised men respond less well, and single-dose regimens may fail in HIV co-infection, requiring follow-up. Suppurative buboes may require drainage: *"Buboes may need additional treatment with either aspiration or excision and drainage"* ([PMID: 41046959](https://pubmed.ncbi.nlm.nih.gov/41046959/)). A Cochrane review of 7 RCTs (875 participants) found no statistically significant difference between macrolides and comparators, supporting single-dose azithromycin as a convenient first-line choice ([PMID: 29226307](https://pubmed.ncbi.nlm.nih.gov/29226307/)).

**NCIT terms:** Azithromycin (C1052), Ceftriaxone (C377), Ciprofloxacin (C376), Erythromycin (C480). **CHEBI:** azithromycin (CHEBI:2955), ceftriaxone (CHEBI:29007).

### F002 — Chancroid is an important cofactor for HIV transmission and acquisition

Chancroid remains an important cofactor in both transmission and acquisition of HIV-1, and countries with the greatest HIV burden historically had the highest chancroid prevalence: *"Chancroid, formerly a major cause of the genital ulcer disease syndrome, remains an important cofactor in both the transmission and acquisition of HIV-1 infection. Those countries with the greatest burden of HIV also have some of the highest prevalence rates of chancroid worldwide"* ([PMID: 15918786](https://pubmed.ncbi.nlm.nih.gov/15918786/)). Quantitatively: *"Chancroid is a common cause of genital ulcer in all 18 countries where adult HIV prevalence surpasses 8% and is rare in countries with low-level HIV epidemics"* ([PMID: 11584729](https://pubmed.ncbi.nlm.nih.gov/11584729/)). This synergy — ulcer disruption of the epithelial barrier plus recruitment of HIV-target immune cells — is the principal reason chancroid control was promoted as an HIV-prevention strategy.

### F006 — Male circumcision and hygiene are protective; commercial sex networks drive risk

A systematic review/meta-analysis found circumcised men at lower risk of chancroid in six of seven studies (individual RRs 0.12 to 1.11): *"Circumcised men were at lower risk of chancroid in six of seven studies (individual study RRs: 0.12 to 1.11)"* ([PMID: 16581731](https://pubmed.ncbi.nlm.nih.gov/16581731/)). Both circumcision and simple topical hygiene greatly reduce infection risk: *"Both simple, topical hygiene and male circumcision greatly reduce risk of infection"* ([PMID: 11584729](https://pubmed.ncbi.nlm.nih.gov/11584729/)). *H. ducreyi* depends on sexual networks with high partner-change rates (commercial sex work, male mobility); eliminating infection from these core groups causes chancroid to disappear from the wider community. **Risk factors:** commercial sex work, multiple/casual partners, poor genital hygiene, uncircumcised status, low socioeconomic status, and HIV co-infection.

### F011 — Diagnosis relies on multiplex NAAT/PCR; culture is insensitive; no FDA-cleared test

Chancroid is diagnosed within the GUD workup alongside HSV-1/2 and *Treponema pallidum*. Multiplex real-time PCR reliably detects all three from ulcer swabs and outperforms culture and serology: *"Real-time PCR technology can provide sensitive, rapid and reproducible evaluation of GUD aetiology in a resource-limited setting"* ([PMID: 19066198](https://pubmed.ncbi.nlm.nih.gov/19066198/)). *H. ducreyi* is fastidious and hard to culture (special media, ~75% maximum sensitivity). Etiology of GUD varies geographically; multiplex PCR in Pune, India detected *H. ducreyi* in 23% of GUD: *"The etiology of GUD as determined by M-PCR was HSV (26%), H. ducreyi (23%), T. pallidum (10%), and multiple infections (7%)"* ([PMID: 9918324](https://pubmed.ncbi.nlm.nih.gov/9918324/)). CDC **probable-case clinical criteria**: painful genital ulcer(s); no evidence of *T. pallidum* by darkfield/NAAT/serology ≥7 days after onset; typical presentation with regional lymphadenopathy; negative HSV test.

### F009 — Research models: temperature-dependent rabbit, experimental swine, and human challenge

Three complementary models exist: (1) the **temperature-dependent rabbit model** for virulence/vaccine studies ([PMID: 22100216](https://pubmed.ncbi.nlm.nih.gov/22100216/)); (2) the **experimental swine (pig) model**, in which nHgbA vaccination confers complete protection; and (3) the **human challenge model**, in which volunteers are inoculated on the upper arm with *H. ducreyi* 35000HP: *"We developed a human infection model for Haemophilus ducreyi in which human volunteers are inoculated on the upper arm. After inoculation, papules form and either spontaneously resolve or progress to pustules"* ([PMID: 26374122](https://pubmed.ncbi.nlm.nih.gov/26374122/)). The human model has defined which virulence factors are required (LspA1/LspA2 required; CpxR **not** required — [PMID: 21606544](https://pubmed.ncbi.nlm.nih.gov/21606544/)) and links the skin microbiome to outcome. There is no established natural animal-reservoir disease; *H. ducreyi* is considered an obligate human pathogen, though Class I strains circulate in non-human primates in some regions.

### F010 — *H. ducreyi* has re-emerged as a cause of non-sexual chronic skin ulcers in children

Over the past two decades the recognized epidemiological spectrum of *H. ducreyi* expanded to include non-sexually-transmitted cutaneous ulcers in children in tropical regions (Western Pacific, sub-Saharan Africa), where it is the most common differential diagnosis for yaws: *"the recognized epidemiological spectrum of H. ducreyi has expanded to include nonsexually transmitted cutaneous ulcers in children in tropical regions. Genomic and microbiological studies have clarified its population structure, revealing two major lineages with limited divergence between genital and cutaneous isolates"* ([PMID: 41318902](https://pubmed.ncbi.nlm.nih.gov/41318902/)). Genomics reveals two major lineages (Class I, Class II); in Papua New Guinea, *"Class II HD infections were more often represented by longer-lasting ulcers than Class I HD infections"* ([PMID: 39146379](https://pubmed.ncbi.nlm.nih.gov/39146379/)). PCR-confirmed *H. ducreyi* skin-ulcer prevalence reached 4.3% in Ghana (vs 2.3% yaws) and 5.3% in Tanzanian children with skin ulcers.

### F012 — Curable, non-fatal, globally declining but persistent; main burden is HIV facilitation

Chancroid causes no direct mortality and is fully curable, so survival/life-expectancy metrics are not applicable. It declined markedly worldwide over the 20th–21st centuries — now rare in high-income countries — but persists in endemic pockets. Its causative organism *"is biologically vulnerable and occupies a precarious epidemiological niche"* ([PMID: 11584729](https://pubmed.ncbi.nlm.nih.gov/11584729/)), explaining why targeted control of core transmission groups can eliminate it locally. Current persistence: 22% of GUD PCR-positive in Malawi — *"Among 618 participants with GUD, 137 (22%) tested positive for"* ([PMID: 41646416](https://pubmed.ncbi.nlm.nih.gov/41646416/)) — while in Australia *"No H. ducreyi has been detected ... since 1998"* ([PMID: 16619156](https://pubmed.ncbi.nlm.nih.gov/16619156/)). Untreated complications include phagedenic ulcers, phimosis, and suppurative/fistulizing buboes; the dominant public-health impact is increased HIV acquisition/transmission.

---

## Section-by-Section Report

### 1. Disease Information
Chancroid is an acute, curable, sexually transmitted bacterial genital ulcer disease caused by *H. ducreyi* (F001). **Identifiers:** MONDO:0001797; ICD-10 **A57** ("Chancroid"); ICD-11 1A75; MeSH **D002602**; SNOMED CT 3419005; DO DOID:11165. There is no OMIM entry (non-genetic disease); Orphanet does not list it as a rare genetic disorder (it is a common infectious disease). **Synonyms:** soft chancre, ulcus molle, soft sore, chancre mou, *Haemophilus ducreyi* infection. Information is derived from aggregated disease-level resources (clinical guidelines, reviews) and controlled human infection studies rather than EHR-level individual patient data.

### 2. Etiology
**Causal factor:** infectious — the Gram-negative coccobacillus *H. ducreyi* (F001). This is **not a genetic disease**; there are no human causal variants, susceptibility loci defined by GWAS, or modifier genes. The only host-genetic dimension is immunological: individuals reproducibly differ in whether they resolve or form pustules, driven by their cutaneous/dendritic-cell immune profile (F008), but no specific human risk allele has been mapped. **Environmental/behavioral risk factors:** commercial sex work, multiple or casual sexual partners, poor genital hygiene, uncircumcised status, low socioeconomic status, and HIV co-infection (F006, F002). **Protective factors:** male circumcision (RRs 0.12–1.11 across studies) and simple topical hygiene (F006). **Gene–environment interactions:** not applicable in the classical (human-heritable) sense; the analogous "pathogen genotype–host environment" interaction is that Class I vs Class II *H. ducreyi* strains cause ulcers of differing duration (F010).

### 3. Phenotypes
| Phenotype | Type | Characteristics | Frequency | Suggested HPO |
|---|---|---|---|---|
| Painful genital ulcer(s), soft/non-indurated | Clinical sign | Adult onset; 3–5 d incubation; moderate–severe; self-limited if treated | Defining (~100%) | HP:0500089 (genital ulcer) |
| Tender inguinal lymphadenitis (bubo) | Clinical sign | Unilateral or bilateral; can suppurate/fistulize | ~50% develop buboes; ~half suppurate | inguinal lymphadenopathy |
| Exquisite ulcer tenderness | Symptom | Pain on palpation (distinguishes from syphilis) | High | painful skin lesion |
| Phimosis / phagedenic ulceration | Complication | Untreated/advanced cases | Minority | — |

Quality-of-life impact is significant but transient given curability: pain, genital disfigurement risk, sexual dysfunction, and psychosocial distress; no chronic disability in treated disease (F005, F012). Formal EQ-5D/SF-36 data specific to chancroid are not available.

### 4. Genetic/Molecular Information
**Not applicable to human host genetics** — no causal genes, pathogenic germline/somatic variants, allele frequencies, modifier genes, epigenetic marks, or chromosomal abnormalities are associated with chancroid susceptibility in humans. The relevant molecular information resides in the **pathogen genome**: key virulence loci include *hgbA* (hemoglobin receptor), *lspA1*/*lspA2* (anti-phagocytic large supernatant proteins), *dsrA* (serum resistance), and the *cdtABC* operon (cytolethal distending toxin) (F003, F007). Population genomics defines two major *H. ducreyi* lineages, **Class I and Class II**, with limited divergence between genital and cutaneous isolates (F010).

### 5. Environmental Information
**Infectious agent:** *Haemophilus ducreyi* (NCBI Taxonomy ID 730), an obligate human pathogen. **Lifestyle/behavioral factors:** high-partner-change sexual networks, commercial sex work, lack of circumcision, poor hygiene (F006). No chemical toxins, radiation, or occupational exposures are implicated. In the pediatric cutaneous-ulcer setting, transmission appears to be skin-to-skin/non-sexual, possibly facilitated by insect vectors and environmental contact, though this remains under study (F010).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating infection → clinical ulcer):**

1. *H. ducreyi* is inoculated into skin/mucosa through a **microabrasion during sexual contact**, which **leads to** entry into the dermis.
2. The organism must obtain iron/heme; it expresses the TonB-dependent hemoglobin receptor **HgbA**, which **results in** heme acquisition from host hemoglobin — an *obligate* nutritional step required to establish infection (demonstrated in the human challenge model) (F007).
3. To survive host defenses, *H. ducreyi* expresses **DsrA** (serum resistance) and the anti-phagocytic lipoproteins **LspA1/LspA2**, which **lead to** evasion of complement-mediated killing and inhibition of phagocytosis by neutrophils/macrophages (demonstrated: *lspA1 lspA2* mutant is avirulent) (F003).
4. Failure of phagocytes to ingest the organism **results in** the bacterium persisting extracellularly within a forming abscess (inferred from PP-vs-RR immune data) (F008).
5. Secreted **cytolethal distending toxin (CdtB)** enters host epithelial cells/keratinocytes/immune cells, where its DNase-I-like activity **causes** DNA double-strand breaks → **G2/M cell-cycle arrest → cellular distension → apoptosis/necrosis** (F003).
6. The host mounts a cutaneous immune response (neutrophils, macrophages, T cells, myeloid dendritic cells). **The branch point:** an effective/regulated response **leads to** spontaneous resolution (RR phenotype); a dysregulated, hyperinflammatory Th1/Treg-skewed response **leads to** pustule/ulcer formation (PP phenotype) (F008).
7. Combined tissue toxicity and inflammation **result in** the soft, painful, non-indurated ulcer with a purulent base; lymphatic spread **leads to** regional lymphadenitis and, in ~50%, suppurating buboes (F005).
8. The open ulcer disrupts the epithelial barrier and recruits HIV-target cells, which **facilitates** HIV acquisition/transmission (downstream cofactor effect) (F002).

**Upstream** events: bacterial entry, heme acquisition, immune evasion. **Downstream** events: CDT-mediated genotoxicity, host inflammatory branch, ulceration, bubo formation, HIV facilitation.

**Cell types (CL):** keratinocyte (CL:0000312), epithelial cell, neutrophil (CL:0000775), macrophage (CL:0000235), myeloid dendritic cell (CL:0000782), T-helper 1 cell, regulatory T cell. **Biological processes (GO):** DNA double-strand break (GO:0006302), cell cycle arrest (GO:0007050), negative regulation of phagocytosis (GO:0050765), inflammatory response (GO:0006954), heme transport (GO:0015886). **Subcellular:** host cell nucleus (CdtB target); bacterial outer membrane (HgbA, DsrA).

### 7. Anatomical Structures Affected
**Primary organs:** external genitalia — penis (UBERON:0000989), prepuce/foreskin, coronal sulcus, glans; in females: labia, fourchette, vaginal introitus, cervix. **Secondary:** inguinal lymph nodes (UBERON:0002450) → buboes. **Body system:** reproductive/integumentary and lymphatic. **Tissue level:** stratified squamous epithelium, dermis; **cells:** keratinocytes and infiltrating immune cells. **Localization:** genital and inguinal regions; laterality of buboes is typically unilateral but may be bilateral. In the emerging pediatric syndrome, ulcers occur on the **limbs** (non-genital skin) (F010).

### 8. Temporal Development
**Onset:** acute; incubation 3–5 days after exposure (F005). Adult-onset in the classical STI form; childhood in the cutaneous-ulcer form (F010). **Progression:** papule → pustule → painful ulcer over days; buboes develop subsequently. **Course:** self-limited to a few weeks with treatment; untreated ulcers may persist/enlarge (phagedenic) for months. **Duration:** short/curable — not chronic or lifelong. **Remission:** treatment-induced cure is the norm; spontaneous resolution occurs in a subset (the RR immunophenotype in the human model) (F008). **Critical intervention window:** early antibiotic treatment prevents bubo suppuration and complications.

### 9. Inheritance and Population
**Inheritance:** none — infectious, non-heritable; penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency are all **not applicable**. **Epidemiology:** globally declined; rare in high-income countries (no *H. ducreyi* in Australia since 1998; ~0.9% of GUD in Amsterdam and Rakai, Uganda) but persistent in endemic pockets (22% of GUD PCR-positive in Malawi 2019–2022; 23% in Pune, India) (F011, F012). **Demographics:** historically concentrated in tropical, resource-limited regions and in sexual-network core groups; male predominance in clinic series (ulcers more visible/symptomatic in men). Geographic strain distribution: Class I and Class II lineages, with Class II associated with longer-lasting ulcers in Papua New Guinea (F010).

### 10. Diagnostics
**Gold-standard practical test:** multiplex real-time NAAT/PCR of ulcer swabs detecting *H. ducreyi*, *T. pallidum*, and HSV-1/2 simultaneously; superior to culture and serology (F011). **Culture:** fastidious, requires special enriched media, ~75% maximum sensitivity, not routinely available. **No FDA-cleared commercial *H. ducreyi* PCR** in many settings. **Gram stain** of ulcer exudate may show "school-of-fish"/"railroad-track" coccobacilli but is insensitive/nonspecific. **CDC probable-case clinical criteria:** painful ulcer(s); negative *T. pallidum* darkfield/NAAT/serology ≥7 days; typical appearance with regional lymphadenopathy; negative HSV. **Differential diagnosis:** primary syphilis (painless, indurated chancre), genital herpes (grouped vesicles, recurrent), lymphogranuloma venereum, granuloma inguinale (donovanosis), and — in children in the tropics — yaws (F010, F011). **Genetic/omics testing:** not applicable to host diagnosis.

### 11. Outcome / Prognosis
**Excellent** — chancroid is fully curable and causes no direct mortality (survival metrics not applicable) (F012). **Complications (untreated):** phagedenic/destructive ulceration, phimosis, suppurative and fistulizing buboes, superinfection. **Recovery:** complete with appropriate antibiotics; ulcers heal, though large ulcers may scar. **Prognostic factors:** HIV co-infection and lack of circumcision predict slower healing and possible single-dose treatment failure (F004). **Dominant morbidity driver:** facilitation of HIV acquisition/transmission (F002).

### 12. Treatment
**First-line pharmacotherapy** (F004): azithromycin 1 g PO single dose (NCIT C1052; CHEBI:2955), ceftriaxone 250 mg IM single dose (NCIT C377; CHEBI:29007), erythromycin 500 mg PO QID × 7 days (NCIT C480), or ciprofloxacin 500 mg PO BID × 3 days (NCIT C376). Drug classes: macrolide, third-generation cephalosporin, fluoroquinolone. **HIV-coinfected/uncircumcised** patients may need multi-dose regimens and follow-up. **Surgical/interventional:** needle aspiration or incision and drainage of fluctuant buboes. **Supportive:** analgesia, local wound care, partner treatment. **Response rates** are high across regimens (Cochrane: no significant difference between macrolides and comparators; [PMID: 29226307](https://pubmed.ncbi.nlm.nih.gov/29226307/)). No gene, cell, or RNA-based therapies apply. Pharmacogenomics: not disease-specific.

### 13. Prevention
**Primary prevention:** condom use, reduction of partner numbers, male circumcision, genital hygiene, and treatment of sexual partners (F006). No licensed vaccine exists, but **HgbA is a validated protective vaccine antigen** in the swine model (F007), the leading vaccine candidate. **Secondary prevention:** syndromic GUD management and prompt treatment in high-prevalence settings; screening/treatment of commercial sex workers interrupts transmission (F006, F012). **Public health:** targeted control of sexual-network core groups can locally eradicate chancroid because of its "precarious epidemiological niche" (F012). In yaws-endemic areas, azithromycin mass drug administration also reduces *H. ducreyi* cutaneous ulcers (F010).

### 14. Other Species / Natural Disease
*H. ducreyi* (NCBI Taxon 730) is essentially an **obligate human pathogen**; there is no established natural companion-animal or wildlife reservoir disease (F009). Notably, Class I strains have been detected circulating in **non-human primates** in some African regions, raising questions of zoonotic potential in the cutaneous-ulcer setting (F009, F010). No VBO breeds, orthologous host disease genes, or OMIA entries apply. Experimental infection is achievable in rabbits and swine (models, below).

### 15. Model Organisms
Three complementary **infection** models (not genetic host-disease models) (F009):
| Model | Type | Use | Key result |
|---|---|---|---|
| Temperature-dependent rabbit | Mammalian in vivo | Virulence, vaccine testing | Oral HgbA-*Salmonella* vaccine; LspA attenuation ([PMID: 22100216](https://pubmed.ncbi.nlm.nih.gov/22100216/)) |
| Experimental swine (pig) | Mammalian in vivo | Vaccine efficacy | nHgbA vaccination = complete protection ([PMID: 21646451](https://pubmed.ncbi.nlm.nih.gov/21646451/)) |
| Human challenge (35000HP, upper arm) | Human controlled infection | Virulence factor & host-susceptibility mapping | Papule→resolve or →pustule; LspA1/A2 required, CpxR not ([PMID: 26374122](https://pubmed.ncbi.nlm.nih.gov/26374122/), [PMID: 15271912](https://pubmed.ncbi.nlm.nih.gov/15271912/), [PMID: 21606544](https://pubmed.ncbi.nlm.nih.gov/21606544/)) |

**Phenotype recapitulation:** the human challenge model faithfully reproduces the papule-to-pustule natural history but is limited to an early, self-resolving arm-skin lesion (ethical necessity) and does not model buboes or genital-site disease. Rabbit/swine models capture ulcer formation and vaccine protection but differ in temperature dependence and immunology from humans.

---

## Mechanistic Model / Interpretation

```
   SEXUAL CONTACT (microabrasion)
              │ inoculation
              ▼
   H. ducreyi in dermis
              │  HgbA → heme/Hb acquisition  (OBLIGATE; F007)
              ▼
   Nutritional establishment
              │  DsrA (serum resistance) + LspA1/LspA2 (anti-phagocytic)  (F003)
              ▼
   Immune evasion — phagocytes fail to ingest organism
              │  CdtB DNase activity → DNA DSBs → G2/M arrest → cell death (F003)
              ▼
   Local tissue damage + inflammation
              │
      ┌───────┴─────────┐   HOST IMMUNE BRANCH (F008)
      ▼                 ▼
 Regulated response   Dysregulated/hyperinflammatory
 (RR: resolves)       (PP: pustule/ulcer)
                          │
                          ▼
               Soft painful ulcer + inguinal bubo (~50% suppurate; F005)
                          │
                          ▼
               Epithelial barrier breach → HIV cofactor (F002)
```

The unifying insight is that chancroid pathology is a **two-party outcome**: the pathogen supplies the tools (heme acquisition, serum resistance, anti-phagocytic proteins, genotoxin), but the *decision* between resolution and ulceration is made by the host's cutaneous/dendritic-cell immune program. This explains both the reproducible PP/RR dichotomy in the human model and the therapeutic/prophylactic leverage points: HgbA (nutritional bottleneck → vaccine), circumcision/hygiene (reduce inoculation), and antibiotics (eliminate the organism before the inflammatory branch matures).

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [28081686](https://pubmed.ncbi.nlm.nih.gov/28081686/) | European guideline definition of disease and cardinal features | F001 |
| [41046959](https://pubmed.ncbi.nlm.nih.gov/41046959/) | 2026 review; etiology, buboes, drainage | F001, F004 |
| [6687703](https://pubmed.ncbi.nlm.nih.gov/6687703/) | Incubation, ulcer morphology, bubo suppuration | F005 |
| [17123907](https://pubmed.ncbi.nlm.nih.gov/17123907/) | CDT/CdtB molecular mechanism | F003 |
| [15271912](https://pubmed.ncbi.nlm.nih.gov/15271912/) | Human challenge: LspA1/A2 required for virulence | F003, F009 |
| [21646451](https://pubmed.ncbi.nlm.nih.gov/21646451/) | HgbA obligate for infection; protective vaccine (swine) | F007 |
| [17893130](https://pubmed.ncbi.nlm.nih.gov/17893130/) | Host immune branch (PP vs RR) determines outcome | F008 |
| [10028106](https://pubmed.ncbi.nlm.nih.gov/10028106/) | First-line antibiotic regimens | F004 |
| [29226307](https://pubmed.ncbi.nlm.nih.gov/29226307/) | Cochrane review of macrolide efficacy | F004 |
| [15918786](https://pubmed.ncbi.nlm.nih.gov/15918786/) | Chancroid as HIV cofactor | F002 |
| [11584729](https://pubmed.ncbi.nlm.nih.gov/11584729/) | HIV correlation; hygiene/circumcision protective; eradicability | F002, F006, F012 |
| [16581731](https://pubmed.ncbi.nlm.nih.gov/16581731/) | Meta-analysis: circumcision protective | F006 |
| [26374122](https://pubmed.ncbi.nlm.nih.gov/26374122/) | Human challenge model design; skin microbiome | F009 |
| [22100216](https://pubmed.ncbi.nlm.nih.gov/22100216/) | Rabbit model; oral HgbA vaccine | F007, F009 |
| [21606544](https://pubmed.ncbi.nlm.nih.gov/21606544/) | CpxR mutant remains virulent | F009 |
| [19066198](https://pubmed.ncbi.nlm.nih.gov/19066198/) | Multiplex real-time PCR for GUD | F011 |
| [9918324](https://pubmed.ncbi.nlm.nih.gov/9918324/) | Multiplex PCR; H. ducreyi 23% of GUD in Pune | F011 |
| [41318902](https://pubmed.ncbi.nlm.nih.gov/41318902/) | Emerging pediatric cutaneous ulcers; two lineages | F010 |
| [39146379](https://pubmed.ncbi.nlm.nih.gov/39146379/) | Class I vs II ulcer duration | F010 |
| [41646416](https://pubmed.ncbi.nlm.nih.gov/41646416/) | Current persistence in Malawi (22% GUD) | F012 |
| [16619156](https://pubmed.ncbi.nlm.nih.gov/16619156/) | Near-elimination in Australia | F012 |

**Evidence-type mix:** human clinical/epidemiological (guidelines, GUD PCR surveys, meta-analyses), controlled human infection (challenge model), model organism (rabbit, swine), and in vitro (CDT biochemistry).

---

## Limitations and Knowledge Gaps

- **Template mismatch:** Chancroid is a non-genetic infectious disease, so all human genetics sections (causal genes, ACMG variant classification, inheritance, penetrance, carrier frequency, chromosomal/epigenetic host changes, gene therapy) are **not applicable**. This should be recorded as a definitive "N/A," not a data gap.
- **Host susceptibility genetics undefined:** The reproducible PP/RR dichotomy strongly implies host-genetic control of outcome, but no specific human HLA/immune alleles have been mapped.
- **Diagnostic accessibility:** No FDA-cleared commercial *H. ducreyi* NAAT exists in many settings; surveillance likely underestimates true burden, especially in women and in the emerging pediatric cutaneous form.
- **No licensed vaccine:** HgbA protection is homologous-strain-specific in animal models; heterologous protection and human efficacy remain unproven.
- **Emerging cutaneous form:** Transmission routes, reservoirs (including possible non-human-primate zoonosis), and long-term impact of azithromycin MDA on strain dynamics are incompletely understood.
- **Quality-of-life data:** No chancroid-specific EQ-5D/SF-36/PROMIS datasets were identified.

---

## Proposed Follow-up Experiments / Actions

1. **Map host-genetic determinants of the PP/RR phenotype** via HLA typing and immune-gene GWAS/transcriptomics in human-challenge volunteers, to define who resolves vs ulcerates.
2. **Advance a cross-protective HgbA (or multivalent HgbA + LspA + DsrA) vaccine** toward heterologous-strain protection and early-phase human trials, prioritizing HIV-endemic and yaws-endemic populations.
3. **Develop and validate a point-of-care multiplex NAAT** (TPHD-LAMP-type) meeting WHO target product profiles for both GUD and pediatric cutaneous ulcers.
4. **Characterize the transmission ecology of the pediatric cutaneous form** — reservoirs, vectors, and zoonotic potential of Class I strains from non-human primates.
5. **Longitudinal surveillance of strain dynamics under azithromycin MDA** to detect resurgence and emerging macrolide resistance.
6. **Formal quality-of-life and HIV-cofactor modeling** to quantify the population-level benefit of chancroid control on HIV incidence.

---

*Report compiled from 12 cited findings and 48 reviewed papers across 5 investigation iterations. Evidence quotes are verbatim from indexed PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Chancroid-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chancroid-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0500089` (2 mentions) - the report calls it "genital ulcer"; HP calls it **Optic nerve sheath meningioma**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007050` (GO_0007050) (1 mention) - replaced by `GO:0051726`