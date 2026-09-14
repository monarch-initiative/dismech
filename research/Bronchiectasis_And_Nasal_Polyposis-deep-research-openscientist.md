---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T17:01:51.083518'
end_time: '2026-09-01T17:29:23.601199'
duration_seconds: 1652.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bronchiectasis and Nasal Polyposis
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
citation_count: 27
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 13
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0975835
    reported_labels:
    - MONDO
    ontology_label: bronchiectasis and nasal polyposis
  - term_id: HP:0011950
    reported_labels:
    - Laboratory/physical
    ontology_label: Unusual bronchiolitis
  labels_variant: 6
  unresolvable_prefixes:
  - OMIM
  - UMLS
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Bronchiectasis_And_Nasal_Polyposis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bronchiectasis_And_Nasal_Polyposis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bronchiectasis and Nasal Polyposis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bronchiectasis and Nasal Polyposis** covering all of the
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

# Bronchiectasis and Nasal Polyposis (BENP): A Comprehensive Disease Report

## Summary

**Bronchiectasis and Nasal Polyposis (BENP; OMIM:620984, MONDO:0975835, MedGen:1874999, UMLS:C5975469) is a distinct, recently-defined autosomal-recessive Mendelian airway disease caused by biallelic loss-of-function of *WFDC2* (WAP four-disulfide core domain 2; also known as HE4, human epididymis protein 4).** WFDC2 is a small secreted WAP-domain protease inhibitor produced by airway secretory (club) cells and submucosal glands. When both copies of the gene are non-functional, the protein is not secreted into the airway surface liquid, removing a component of innate airway defense. The clinical consequence is chronic airway infection producing severe rhinosinusitis, pronounced nasal polyposis, and bronchiectasis — while ciliary structure/function and CFTR function remain normal. The disease was molecularly defined by Dougherty et al. in 2024 ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/)), who identified biallelic pathogenic *WFDC2* variants in 11 individuals from 10 unrelated families across the United States, Europe, Asia, and Africa. A recurrent founder missense variant, p.Cys49Arg, disrupts glycosylation and blocks secretion of mature WFDC2.

This report distinguishes the molecularly-defined Mendelian entity **BENP (WFDC2 deficiency)** from the historically-described, clinically-overlapping **Woakes' syndrome** — a rare hereditary chronic rhinosinusitis with nasal polyposis (CRSwNP) variant defined by a clinical pentad (recurrent nasal polyposis, nasal broadening, frontal sinus aplasia, bronchiectasis, and dyscrinia). Woakes' syndrome, first delineated in 1979 ([PMID: 553887](https://pubmed.ncbi.nlm.nih.gov/553887/)), has never been assigned a molecular cause and has no OMIM/MONDO/Orphanet ID; it likely represents a clinically-recognized subset of the broader phenotypic spectrum that BENP now molecularly explains for a proportion of cases. Both entities share the core "unified airway" pathology linking upper-airway polyposis to lower-airway bronchiectasis via impaired mucociliary clearance and chronic infection.

Because WFDC2 (HE4) is undetectable in the serum of affected individuals, a **blood HE4 test combined with *WFDC2* genetic testing enables diagnosis** — a rare instance of a simple, accessible biomarker for a genetic airway disease. Management combines endoscopic sinus surgery (universal in reported Woakes' cases), type-2-targeted biologics for the polyp component (dupilumab is the leading agent), and standard bronchiectasis care (airway clearance, anti-inflammatory DPP-1 inhibition, and infection control).

---

## Disease Information

### Overview
BENP is an **autosomal recessive airway disease characterized by chronic infection of the airways resulting in rhinosinusitis and pronounced nasal polyposis** (MedGen definition, after Dougherty et al., 2024). The disease spans the entire respiratory tract: upper airway (chronic rhinosinusitis, nasal polyposis, frequently with nasal broadening and frontal sinus abnormalities) and lower airway (bronchiectasis with chronic productive cough, recurrent infections, and progressive bronchial dilatation).

### Key Identifiers
| Resource | Identifier |
|----------|-----------|
| OMIM | 620984 |
| MONDO | MONDO:0975835 |
| MedGen | 1874999 |
| UMLS | C5975469 |
| Causal gene (NCBI Gene) | *WFDC2*, Gene ID 10406 |
| Cytogenetic locus | 20q13.12 |
| HGNC | HGNC:15466 |
| Gene alias | HE4; the *WFDC2* alias list literally includes "BENP" |
| Related historical entity | Woakes' syndrome (no OMIM/MONDO/Orphanet ID; closest MedGen concept "Polypoid sinus degeneration", UMLS C0155822) |

### Synonyms and Alternative Names
- Bronchiectasis and nasal polyposis (BENP)
- Recessively inherited WFDC2 (HE4) deficiency
- (Clinically overlapping) Woakes' syndrome — synonyms: necrotic ethmoiditis with nasal polyposis; Woakes' ethmoiditis

### Source of Information
Information is derived from **aggregated disease-level resources** (OMIM, MONDO, MedGen) and from **primary clinical genetics literature** (a multi-family international case series, Dougherty et al., 2024). Epidemiologic descriptors of the overlapping Woakes' phenotype come from a PRISMA systematic review of published individual cases ([PMID: 41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/)).

---

## Etiology

### Disease Causal Factors
**BENP is a monogenic (Mendelian) disease.** The primary and sufficient cause is **biallelic (homozygous or compound heterozygous) loss-of-function of *WFDC2***. As stated by Dougherty et al.: *"We identified biallelic pathogenic variants in WAP four-disulfide core domain 2 (WFDC2) in 11 individuals from 10 unrelated families originating from the United States, Europe, Asia, and Africa"* and *"WFDC2 dysfunction defines a novel molecular etiology of bronchiectasis characterized by the deficiency of a secreted component of the airways"* ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/)).

A secondary infectious/mechanistic contribution is inherent: loss of the WFDC2 airway-defense protein permits **chronic bacterial colonization and infection**, which drives the inflammatory and structural airway damage.

### Risk Factors

**Genetic risk factors**
- Causal variants: biallelic pathogenic *WFDC2* variants. The recurrent founder missense variant **p.Cys49Arg** is the best-characterized; computer simulations and deglycosylation assays indicate it *"structurally"* disrupts glycosylation and blocks secretion of the mature protein ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/)).
- Susceptibility for the broader (non-Mendelian) nasal-polyp phenotype: CRSwNP has a strong heritable component. A Utah genealogical study (1,638 CRSwNP probands) found first-degree relatives had a **4.1-fold increased risk** (p < 10⁻³) and second-degree relatives a 3.3-fold risk of the same diagnosis, with **no increased risk in spouses**: *"First-degree relatives (1stDRs) of CRSwNP patients demonstrated a 4.1-fold increased risk (p < 10(-3)) of carrying the same diagnosis, whereas second-degree relatives (2ndDRs) demonstrated a 3.3-fold increased risk"* and *"No increased risk was observed in spouses of CRSwNP patients"* ([PMID: 25677865](https://pubmed.ncbi.nlm.nih.gov/25677865/)).

**Environmental risk factors**
- For BENP specifically, environment is not a primary driver, but chronic airway infection (opportunistic bacterial colonization) perpetuates disease. In the reported Woakes' aggregate, disease was **male-predominant (65%)** with childhood-through-adult onset ([PMID: 41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/)).
- Consanguinity increases the likelihood of recessive disease (relevant to a recessive disorder like BENP); in pediatric non-CF bronchiectasis cohorts consanguinity was positive in 59.4% ([PMID: 29605210](https://pubmed.ncbi.nlm.nih.gov/29605210/)).

### Protective Factors
No specific genetic or dietary protective factors are established for BENP. Heterozygous carriers of a single pathogenic *WFDC2* allele are unaffected (recessive inheritance), implying one functional allele is protective/sufficient.

### Gene–Environment Interactions
The core interaction is **genotype (WFDC2 loss) × airway microbial exposure**: absent WFDC2-mediated innate defense, ordinary airway microbial exposure produces chronic infection and the self-sustaining "vicious vortex" of bronchiectasis. This is inferred from the protein's antibacterial function and the infection-dominated phenotype rather than directly demonstrated with GxE modeling.

---

## Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Severity/Course | Frequency |
|-----------|------|----------------|-------|-----------------|-----------|
| Nasal polyposis (recurrent, severe) | Clinical sign / physical manifestation | HP:0100582 (Nasal polyposis) | Childhood (classically early) to adult | Severe, recurrent/relapsing | Defining feature; universal |
| Bronchiectasis | Clinical sign / imaging | HP:0002110 (Bronchiectasis) | Childhood–adult | Progressive, chronic | Defining feature |
| Chronic rhinosinusitis | Symptom/sign | HP:0000246 (Sinusitis) | Childhood–adult | Chronic, relapsing | Very frequent |
| Chronic productive cough / sputum | Symptom | HP:0031245 (Productive cough) | With bronchiectasis onset | Chronic | Frequent |
| Recurrent respiratory infections | Symptom | HP:0002205 (Recurrent respiratory infections) | Childhood | Recurrent | Frequent |
| Nasal broadening | Physical manifestation | HP:0000414 (Broad nasal tip) | Childhood | Progressive with polyp mass | Woakes' feature |
| Frontal sinus aplasia | Physical/imaging | HP:0002688 (Aplasia of the frontal sinus) | Congenital/developmental | Stable | Woakes' feature |
| Dyscrinia (highly viscous mucus) | Laboratory/physical | HP:0011950 | Early | Chronic | Woakes' feature |
| Anosmia/hyposmia | Symptom | HP:0000458 (Anosmia) | With polyp burden | Fluctuating | Frequent in CRSwNP |

**Clinical characteristics.** The Woakes' pentad — *"recurrent nasal polyposis with broadening of the nose, frontal sinus aplasia, bronchiectasis, and dyscrinia (production of highly viscous mucus)"* ([PMID: 553887](https://pubmed.ncbi.nlm.nih.gov/553887/)) — captures the phenotype. A modern series reiterates *"severe recurrent nasal polyps in early childhood with broadening of the nose, nasal dyscrinia, frontal sinus aplasia and bronchiectasis"* ([PMID: 27143164](https://pubmed.ncbi.nlm.nih.gov/27143164/)). Age of onset is variable — the systematic review of Woakes' cases found mean age 39.5 years (range 5–81), with both paediatric- and adult-onset cases ([PMID: 41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/)).

**Quality-of-life impact.** Substantial. The nasal-polyp component causes nasal obstruction, anosmia, and rhinorrhea (measured by SNOT-22); the bronchiectasis component causes chronic cough, sputum, dyspnea, and recurrent exacerbations. Endoscopic sinus surgery improves symptoms and QoL, but *"recurrences are common and multiple surgeries are often required"* ([PMID: 41261359](https://pubmed.ncbi.nlm.nih.gov/41261359/)).

---

## Genetic / Molecular Information

### Causal Gene
***WFDC2*** (WAP four-disulfide core domain 2 / HE4 / human epididymis protein 4); **NCBI Gene 10406**; **HGNC:15466**; UniProt Q14508; chromosome **20q13.12**. OMIM phenotype 620984.

### Pathogenic Variants
- **Variant type/class:** predominantly **missense** (recurrent founder **p.Cys49Arg**), consistent with disruption of a disulfide-bonded WAP-domain cysteine. Other biallelic pathogenic/likely-pathogenic variants were identified across the 10 families.
- **Classification (ACMG/AMP):** pathogenic/likely-pathogenic biallelic variants in affected individuals.
- **Functional consequence:** **loss of function via loss of secretion.** *"Computer simulations and deglycosylation assays indicate that the disease-causing founder variant p.Cys49Arg structurall[y]"* alters the protein such that mature, glycosylated WFDC2 is not secreted ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/)). The net effect is **deficiency of a secreted airway component**.
- **Origin:** **germline**, biallelic (recessive).
- **Allele frequency:** pathogenic alleles are rare; the founder p.Cys49Arg suggests population-specific recurrence. (Exact gnomAD frequencies not extracted in this investigation.)

### Modifier Genes
Not established for BENP. For the shared CRSwNP/AERD phenotype, arachidonic-acid-pathway and type-2 immune loci modulate severity (see Mechanism).

### Epigenetic Information
Not established for BENP. Of note, in cystic fibrosis airway epithelium, *WFDC2*/HE4 mRNA is upregulated with decreased miR-140-5p, indicating HE4 expression is under microRNA regulation ([PMID: 27105680](https://pubmed.ncbi.nlm.nih.gov/27105680/)) — relevant to WFDC2 biology though not to BENP pathogenesis per se.

### Chromosomal Abnormalities
None reported; BENP is a single-gene disorder, not a structural/aneuploidy syndrome.

---

## Environmental Information

- **Environmental factors:** Not primary. Chronic airway microbial exposure is the permissive environmental substrate on which the genetic defect acts.
- **Lifestyle factors:** No established BENP-specific lifestyle drivers. General bronchiectasis worsens with smoking and environmental exposures (extrapolated).
- **Infectious agents:** Chronic bacterial airway infection is central to the downstream pathology. In bronchiectasis broadly, microbiome dysbiosis with increased pathogenic bacteria correlates with severity ([PMID: 42051198](https://pubmed.ncbi.nlm.nih.gov/42051198/)); older/advanced bronchiectasis shows a shift toward *Pseudomonas aeruginosa* and Enterobacteriaceae ([PMID: 42474633](https://pubmed.ncbi.nlm.nih.gov/42474633/)). *Staphylococcus aureus* enterotoxins can amplify type-2 airway inflammation along the nasobronchial axis ([PMID: 42646747](https://pubmed.ncbi.nlm.nih.gov/42646747/)).

---

## Mechanism / Pathophysiology

### Ordered Causal Chain

```
1. Biallelic loss-of-function WFDC2 variant (e.g., p.Cys49Arg)          [demonstrated]
        │  leads to
2. Misglycosylation and blocked secretion of mature WFDC2 protein        [demonstrated]
        │  results in
3. Deficiency of secreted WFDC2 in airway surface liquid                 [demonstrated]
   (undetectable in serum)
        │  removes
4. A protease-inhibitor / antibacterial innate-defense component          [demonstrated/known]
   of the airway
        │  permits
5. Chronic bacterial airway infection and microbiome dysbiosis            [inferred/known]
        │  triggers
6. Persistent airway inflammation (neutrophilic ± type-2/eosinophilic)    [inferred/known]
        │  branches:
        ├──(UPPER AIRWAY)── epithelial injury + type-2 inflammation → mucus
        │    hypersecretion (dyscrinia) + tissue remodeling → recurrent NASAL
        │    POLYPOSIS, rhinosinusitis, nasal broadening                   [observed]
        │
        └──(LOWER AIRWAY)── impaired mucociliary clearance + neutrophil
             elastase / DPP-1-driven inflammation → "vicious vortex" →
             irreversible bronchial wall damage → BRONCHIECTASIS           [observed]
```

Steps 1–4 are **demonstrated** by the primary genetic/biochemical study ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/)). Steps 5–7 integrate established airway-disease mechanisms and are partly **inferred** for BENP specifically from the known biology of nasal polyposis and bronchiectasis.

### Molecular Pathways and Cellular Processes
- **Upstream — loss of airway defense.** WFDC2/HE4 is a secreted serine-protease inhibitor. Curated GO annotations for WFDC2 (Gene 10406) include **serine-type endopeptidase inhibitor activity (GO:0004867)**, **peptidase inhibitor activity (GO:0030414)**, **negative regulation of endopeptidase activity (GO:0010951)**, **antibacterial humoral response (GO:0019731)**, **innate immune response (GO:0045087)**, **club cell differentiation (GO:0060486)**, and **positive regulation of lung ciliated cell differentiation (GO:1901248)**. Localization: **extracellular region (GO:0005576)** and **extracellular exosome (GO:0070062)** — consistent with a secreted protein. Loss of this protease-inhibitory/antibacterial shield underlies the "loss-of-airway-defense" mechanism.
- **Downstream (upper airway) — type-2 inflammation and remodeling.** Epithelial alarmins (IL-25, IL-33, TSLP) activate ILC2/Th2 cells → IL-4/IL-5/IL-13 → eosinophilia, local IgE, mast-cell activation: *"initial allergen exposure disrupts epithelial integrity, triggering local inflammation via alarmins including IL-25, IL-33, and TSLP, which activate type 2 innate lymphoid cells as well as other immune cells to secrete type 2 cytokines IL-4, IL-5 and IL-13, promoting Th2 cell development and eosinophil recruitment"* ([PMID: 39158477](https://pubmed.ncbi.nlm.nih.gov/39158477/)). Eosinophil–epithelial interactions drive mucin and profibrotic cytokine secretion: *"Eosinophil-epithelial interactions significantly stimulated the secretion of MUC5AC, PDGF-AB, VEGF, TGF-beta1, and IL-8 in culture supernatants"* ([PMID: 24717945](https://pubmed.ncbi.nlm.nih.gov/24717945/)) — the molecular basis of mucus hypersecretion (dyscrinia) and polyp remodeling.
- **Downstream (lower airway) — vicious vortex.** *"Bronchiectasis is a chronic respiratory disease characterised by irreversible bronchial dilatation, persistent airway inflammation and recurrent infections"* ([PMID: 42342265](https://pubmed.ncbi.nlm.nih.gov/42342265/)). Neutrophil-driven inflammation via DPP-1/neutrophil elastase perpetuates airway damage; targeting DPP-1 (brensocatib) reduces exacerbations ([PMID: 42048140](https://pubmed.ncbi.nlm.nih.gov/42048140/)).

### Immune System Involvement
Combined **innate immunodeficiency** (loss of secreted WFDC2 antibacterial defense; GO:0045087) plus **chronic mixed inflammation** — type-2/eosinophilic in the polyp compartment and neutrophilic in the bronchiectatic compartment. A subset overlaps with AERD/Samter's triad, driven by dysregulated arachidonic-acid metabolism: *"Alterations in arachidonic acid metabolism may induce an imbalance between pro-inflammatory and anti-inflammatory substances, expressed as an overproduction of cysteinyl leukotrienes and an underproduction of prostaglandin E2"* ([PMID: 29414455](https://pubmed.ncbi.nlm.nih.gov/29414455/)). Samter's triad was the most common comorbidity in reported Woakes' cases (7/39) ([PMID: 41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/)).

### Cell Types and Tissues
- **Airway secretory/club cells (CL:0000158)** and **submucosal gland cells** — normal source of WFDC2.
- **Respiratory epithelial cells (CL:0002633)** and **ciliated cells (CL:0005012)** — mucociliary interface.
- **Eosinophils (CL:0000771)**, **mast cells (CL:0000097)**, **type-2 innate lymphoid cells / Th2 cells (CL:0000899)** — polyp inflammation.
- **Neutrophils (CL:0000775)** — bronchiectasis inflammation.

**GO biological processes:** GO:0019731 (antibacterial humoral response), GO:0045087 (innate immune response), GO:0002376 (immune system process), GO:0060486 (club cell differentiation), GO:1901248 (positive regulation of lung ciliated cell differentiation).

### Molecular Profiling
WFDC2/HE4 is measurable in serum and airway. In BENP it is **undetectable in serum**, enabling diagnosis. By contrast, in cystic fibrosis, serum HE4 is *elevated* and correlates with disease severity — median 99.5 pmol/L in children with CF vs 36.3 pmol/L in controls (P < .0001) ([PMID: 27105680](https://pubmed.ncbi.nlm.nih.gov/27105680/)) — illustrating that HE4 is dynamically regulated in airway disease and that its *absence* is the specific BENP signature.

---

## Anatomical Structures Affected

### Organ Level
- **Primary organs:** paranasal sinuses and nasal cavity (UBERON:0001707 nasal cavity; UBERON:0001825 paranasal sinus; frontal sinus UBERON:0002264) and the lungs/bronchi (UBERON:0002185 bronchus; UBERON:0002048 lung).
- **Secondary involvement:** middle ear (eosinophilic otitis media reported with Woakes', [PMID: 27143164](https://pubmed.ncbi.nlm.nih.gov/27143164/)); nasal external framework (nasal broadening).
- **Body system:** **respiratory system** (UBERON:0001004), upper and lower airways ("unified airway").

### Tissue and Cell Level
- **Airway epithelium** (respiratory epithelium), **submucosal glands**, and inflammatory infiltrate.
- Cell populations: club/secretory cells, ciliated cells, eosinophils, neutrophils, mast cells (CL terms above).

### Subcellular Level
- **Extracellular region / airway surface liquid** (GO:0005576) — site of WFDC2 deficiency.
- **Secretory pathway / ER–Golgi glycosylation machinery** — where the p.Cys49Arg defect blocks maturation and secretion.

### Localization / Lateralization
- Sinonasal disease is typically **bilateral**. Bronchiectasis in comparable pediatric cohorts preferentially involves **lower lobes** (left-lower 53.9–71%, right-lower 47–59%) ([PMID: 30961955](https://pubmed.ncbi.nlm.nih.gov/30961955/), [PMID: 29605210](https://pubmed.ncbi.nlm.nih.gov/29605210/)).

---

## Temporal Development

- **Onset:** variable — classically **early childhood** for the nasal-polyp component (Woakes'), but the systematic review documents onset from age 5 to adulthood (mean age at report 39.5 years) ([PMID: 41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/)). Onset pattern is **chronic/insidious**.
- **Progression:** chronic and **progressive** for bronchiectasis (irreversible bronchial dilatation) and **relapsing/recurrent** for nasal polyposis. Bronchiectasis follows a self-perpetuating "vicious vortex" ([PMID: 42474633](https://pubmed.ncbi.nlm.nih.gov/42474633/)).
- **Duration:** **chronic, lifelong.**
- **Remission patterns:** treatment-induced partial remission (surgery, biologics) is common but polyps frequently recur; spontaneous remission is not characteristic.
- **Critical periods:** childhood diagnosis offers a window to institute airway-clearance and infection-control measures before irreversible bronchiectatic damage accrues.

---

## Inheritance and Population

- **Inheritance pattern:** **autosomal recessive** (biallelic *WFDC2* loss-of-function).
- **Penetrance:** presumed high/complete for biallelic loss-of-function, though variable expressivity of individual phenotype components is expected.
- **Founder effects:** the recurrent **p.Cys49Arg** variant indicates a founder allele; affected families span the US, Europe, Asia, and Africa ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/)).
- **Consanguinity:** relevant for a recessive disorder; high consanguinity rates characterize pediatric non-CF bronchiectasis cohorts generally (59.4%, [PMID: 29605210](https://pubmed.ncbi.nlm.nih.gov/29605210/)).
- **Carrier frequency:** not precisely established; expected rare.

### Epidemiology
BENP is **ultra-rare**: the defining series comprised 11 individuals from 10 families. The clinically overlapping Woakes' phenotype is similarly rare — a PRISMA systematic review identified only **39 unique patients across 23 studies** (*"Twenty-three studies met the inclusion criteria, comprising 39 unique patients (mean age 39.5 years; range 5-81; 65% male)"*, [PMID: 41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/)). Precise prevalence/incidence figures are not available.

### Population Demographics
- **Sex ratio:** male-predominant in the Woakes' aggregate (65% male).
- **Geographic distribution:** multi-ancestry (worldwide) with a founder allele. In a Vietnamese sinopulmonary cohort, *WFDC2* abnormalities were specifically screened but **not identified**, underscoring rarity and possible population variation ([PMID: 41094464](https://pubmed.ncbi.nlm.nih.gov/41094464/)).

---

## Diagnostics

### Clinical Tests
- **Serum HE4 (WFDC2) assay:** the key BENP-specific test — **WFDC2 is undetectable in serum** of affected individuals (contrast: elevated in CF). Combined with genetic testing, this enables diagnosis ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/), [PMID: 27105680](https://pubmed.ncbi.nlm.nih.gov/27105680/)).
- **Imaging:** chest **HRCT** documents bronchiectasis (broncho-arterial ratio >1, lack of tapering, bronchial wall thickening, mucus plugging, tree-in-bud) ([PMID: 31508157](https://pubmed.ncbi.nlm.nih.gov/31508157/)); sinus **CT** scored by Lund-Mackay; nasal endoscopy scored by Lund-Kennedy.
- **Biopsy/pathology:** nasal polyp histology shows eosinophilic mucosa with MUC5AC-rich mucus hypersecretion and remodeling.

### Genetic Testing
- **Recommended approach:** targeted single-gene *WFDC2* sequencing, or a **sinopulmonary/bronchiectasis gene panel** (should include *CFTR*, PCD genes *DNAI1/DNAH5/DNAH11*, and *WFDC2*), or **WES/WGS** for undiagnosed sinopulmonary disease. Vietnamese sinopulmonary genetic screening explicitly incorporated *WFDC2* alongside CF and PCD genes ([PMID: 41094464](https://pubmed.ncbi.nlm.nih.gov/41094464/)).

### Clinical Criteria and Differential Diagnosis
BENP/Woakes' diagnosis is partly **exclusionary**: childhood nasal polyposis is classically caused by CF or Kartagener/PCD — *"Usually, nasal polyposis in early childhood (children aged less than 5 years) is caused by cystic fibrosis of Kartagener's syndrome"* ([PMID: 553887](https://pubmed.ncbi.nlm.nih.gov/553887/)) — which must be excluded.

| Differential | Gene(s) | Inheritance | Distinguishing tests |
|--------------|---------|-------------|----------------------|
| **Cystic fibrosis** | *CFTR* | AR | Sweat chloride ≥60 mmol/L; two pathogenic CFTR variants; **elevated** serum HE4 ([PMID: 41919747](https://pubmed.ncbi.nlm.nih.gov/41919747/), [PMID: 27105680](https://pubmed.ncbi.nlm.nih.gov/27105680/)) |
| **PCD / Kartagener** | *DNAI1, DNAH5, DNAH11* | AR | Low nasal nitric oxide; ciliary EM; ± situs inversus ([PMID: 16203616](https://pubmed.ncbi.nlm.nih.gov/16203616/), [PMID: 34391405](https://pubmed.ncbi.nlm.nih.gov/34391405/)) |
| **AERD / Samter's triad** | polygenic | — | NSAID hypersensitivity; aspirin challenge ([PMID: 29414455](https://pubmed.ncbi.nlm.nih.gov/29414455/)) |
| **BENP** | *WFDC2* | AR | **Undetectable** serum HE4; biallelic WFDC2 variants; **normal** cilia and CFTR |

For PCD exclusion: *"As a screening test nasal nitric oxide (NO) measurement is widely used. Establishment of diagnosis currently relies on electron microscopy, direct evaluation of ciliary beat by light microscopy"* ([PMID: 16203616](https://pubmed.ncbi.nlm.nih.gov/16203616/)). The **absence** of serum HE4 (vs its elevation in CF) plus normal cilia distinguishes BENP.

### Screening
Cascade genetic testing of at-risk relatives once a proband's biallelic *WFDC2* variants are identified; carrier testing for reproductive partners.

---

## Outcome / Prognosis

- **Survival/mortality:** BENP is **not directly lethal**, but the bronchiectasis component drives long-term morbidity and mortality. In the European Bronchiectasis Registry (EMBARC, n=13,484), *"Sputum colour is a simple marker of disease severity and future risk of exacerbations, severe exacerbations and mortality in patients with bronchiectasis"* ([PMID: 38609095](https://pubmed.ncbi.nlm.nih.gov/38609095/)).
- **Morbidity/QoL:** substantial — chronic nasal obstruction, anosmia, rhinorrhea (SNOT-22) plus chronic cough, sputum, dyspnea, and recurrent exacerbations.
- **Disease course:** chronic-relapsing. Sinus surgery relieves symptoms but *"endoscopic sinus surgery offers relief of symptoms and improvement of quality of life, recurrences are common and multiple surgeries are often required"* ([PMID: 41261359](https://pubmed.ncbi.nlm.nih.gov/41261359/)).
- **Complications:** recurrent respiratory infections, progressive airflow obstruction, and (in overlap syndromes) eosinophilic otitis media.
- **Prognostic factors:** sputum purulence, *Pseudomonas* colonization, exacerbation frequency, and lung-function decline predict worse bronchiectasis outcomes ([PMID: 38609095](https://pubmed.ncbi.nlm.nih.gov/38609095/), [PMID: 42474633](https://pubmed.ncbi.nlm.nih.gov/42474633/)).

---

## Treatment

### Surgical / Interventional
**Functional endoscopic sinus surgery (FESS)** is universal in reported cases — *"All patients underwent surgical treatment, most commonly functional endoscopic sinus surgery, with adjunctive procedures including digital nasal bone compression (six cases) and formal rhinoplasty or septorhinoplasty (seven cases)"* ([PMID: 41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/)). NCIT: Endoscopic Sinus Surgery.

### Pharmacotherapy — Type-2-Targeted Biologics (for the polyp component)
Network meta-analyses of RCTs establish biologics as effective for the CRSwNP component:

| Biologic | Target | Effect on Nasal Polyp Score (WMD vs placebo) | Source |
|----------|--------|----------------------------------------------|--------|
| **Dupilumab** | IL-4Rα (IL-4/IL-13) | **−2.16 (95% CI −2.44 to −1.89)** | [PMID: 41178615](https://pubmed.ncbi.nlm.nih.gov/41178615/) |
| Tezepelumab | TSLP | −1.50 | [PMID: 41178615](https://pubmed.ncbi.nlm.nih.gov/41178615/) |
| Mepolizumab | IL-5 | ~ −0.9 to −1.25 | [PMID: 41178615](https://pubmed.ncbi.nlm.nih.gov/41178615/) |
| Omalizumab | IgE | ~ −0.9 | [PMID: 41178615](https://pubmed.ncbi.nlm.nih.gov/41178615/) |

*"NPS was significantly improved by dupilumab (WMD: -2.16, 95% CI [-2.44, -1.89])"* ([PMID: 41178615](https://pubmed.ncbi.nlm.nih.gov/41178615/)). Larger NMAs (3,642 patients, 7 biologics) rank **dupilumab, stapokibart, and tezepelumab** in the top efficacy tier ([PMID: 42398863](https://pubmed.ncbi.nlm.nih.gov/42398863/)). A real-world cohort (n=360) achieved good-to-excellent response in **51%** ([PMID: 41989130](https://pubmed.ncbi.nlm.nih.gov/41989130/)). NCIT: Dupilumab, Mepolizumab, Omalizumab.

### Pharmacotherapy — Bronchiectasis Component
- **Airway clearance / mucoactive agents** (hypertonic saline, mannitol, carbocisteine); evidence is mixed — a meta-analysis did not show a significant reduction in exacerbations ([PMID: 42342264](https://pubmed.ncbi.nlm.nih.gov/42342264/)).
- **Anti-inflammatory DPP-1 inhibition:** **brensocatib** (recently approved) reduces neutrophil-driven inflammation and exacerbations — *"the inhibition of dipeptidyl peptidase-1 (DPP-1) which can reduce neutrophil-driven airway inflammation and, consequently, exacerbations"* ([PMID: 42048140](https://pubmed.ncbi.nlm.nih.gov/42048140/)). NCIT: Brensocatib.
- **Macrolides** (azithromycin) and targeted antibiotics for infection control.

### Advanced / Experimental (Rational, Not Yet Available)
Because BENP is a **deficiency of a secreted protein**, it is conceptually amenable to **protein-replacement or gene-directed therapy** (inhaled/topical recombinant WFDC2, or *WFDC2* gene therapy) — analogous in spirit to CFTR modulation for CF. This is a proposed, not established, strategy.

### Personalized Medicine
Genotype-guided care: confirmed *WFDC2* biallelic loss identifies patients for whom future WFDC2-directed therapy would apply and rationalizes aggressive combined upper/lower-airway management.

---

## Prevention

- **Primary prevention:** not possible for a germline recessive disorder; **genetic counseling** and **carrier/cascade screening** in affected families are the key preventive tools.
- **Secondary prevention:** early diagnosis (serum HE4 + genetics) to institute airway-clearance and infection control **before** irreversible bronchiectasis develops (critical-period concept).
- **Tertiary prevention:** minimize exacerbations and structural progression via airway clearance, prompt antibiotics, DPP-1 inhibition, and polyp control (biologics/surgery).
- **Immunization:** routine respiratory immunizations (influenza, pneumococcal) are advisable to reduce infective exacerbations (standard bronchiectasis practice).
- **Counseling:** genetic counseling for autosomal-recessive recurrence risk (25% per pregnancy for carrier couples); prenatal/preimplantation options where variants are known.

---

## Other Species / Natural Disease

- **Taxonomy / orthologs:** *WFDC2* is highly conserved with 1:1 mammalian orthologs — **mouse *Wfdc2* (Gene 67701), rat (286888), dog (403919), cow (618044), macaque (710469), chimpanzee (458283)**. NCBI Taxon: *Homo sapiens* (9606); *Mus musculus* (10090); *Rattus norvegicus* (10116).
- **Natural disease:** no naturally-occurring animal BENP homolog has been reported (OMIA search not positive in this investigation).
- **Evolutionary conservation:** strong ortholog conservation supports the feasibility of murine models and cross-species mechanistic study.

---

## Model Organisms

- **Recommended primary model:** **mouse** *Wfdc2* knockout (Gene 67701) — the conserved 1:1 ortholog makes a targeted knockout the logical model to test whether WFDC2 loss recapitulates rhinosinusitis/nasal polyposis and bronchiectasis-like airway pathology with chronic infection.
- **Complementary in-vitro models:** **air–liquid interface (ALI) cultures** of human nasal/bronchial epithelium (used widely in CRS and CF research, e.g., [PMID: 40683569](https://pubmed.ncbi.nlm.nih.gov/40683569/), [PMID: 27105680](https://pubmed.ncbi.nlm.nih.gov/27105680/)) with *WFDC2* knockdown/knockout to assay secretion, antibacterial activity, and mucin production; **patient-derived iPSC airway organoids**.
- **Model types available/needed:** knockout, conditional (airway-secretory-cell-specific), knock-in of p.Cys49Arg (to model the founder secretion defect), and humanized lines.
- **Phenotype recapitulation / limitations:** to be established — a key uncertainty is whether mice reproduce the human nasal-polyp phenotype (rodents rarely form true nasal polyps), which may limit face validity for the upper-airway component.
- **Resources:** MGI, IMPC/KOMP (for *Wfdc2* alleles), Cellosaurus/ATCC (epithelial lines).

---

## Mechanistic Model / Interpretation

BENP is best understood as a **"loss-of-airway-defense" Mendelian disease**. A single secreted protein, WFDC2/HE4 — a WAP-domain protease inhibitor with antibacterial and protease-regulatory functions made by airway club cells and submucosal glands — is a non-redundant component of airway surface liquid. Biallelic loss (often via the p.Cys49Arg secretion-blocking founder variant) removes this defense, licensing chronic airway infection. The infection/inflammation then plays out along the **unified airway**: in the sinonasal compartment it drives type-2/eosinophilic inflammation, MUC5AC hypersecretion (dyscrinia), and remodeling → recurrent polyposis; in the bronchial compartment it drives the neutrophilic "vicious vortex" → irreversible bronchiectasis.

This model elegantly explains why BENP mimics CF and PCD (all three cause combined upper+lower airway suppurative disease) yet is molecularly distinct: **cilia are structurally normal (unlike PCD) and CFTR/chloride transport is normal (unlike CF)**. The serum HE4 test provides an unusually clean diagnostic discriminator — **absent in BENP, elevated in CF** — turning a rare genetic diagnosis into a two-step (blood biomarker → confirmatory sequencing) workflow.

```
        UPSTREAM (genetic/molecular)          DOWNSTREAM (clinical)
   WFDC2 biallelic LoF ──► no secreted    ──► chronic infection ──► ┬─► NASAL POLYPOSIS
   (p.Cys49Arg etc.)      WFDC2 in ASL         + inflammation        └─► BRONCHIECTASIS
   [demonstrated]         [demonstrated]       [inferred/known]          [observed]
```

---

## Evidence Base

| PMID | Contribution | Weight |
|------|--------------|--------|
| [38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/) | **Defining paper** — biallelic WFDC2 LoF causes BENP; founder p.Cys49Arg blocks secretion; serum HE4 undetectable | Landmark (human clinical + in vitro/computational) |
| [27105680](https://pubmed.ncbi.nlm.nih.gov/27105680/) | HE4 biology in airway disease; elevated in CF (contrast with BENP); miR-140-5p regulation | Supporting |
| [553887](https://pubmed.ncbi.nlm.nih.gov/553887/) | Original Woakes' pentad; CF/PCD as differentials; hereditary basis | Historical/clinical |
| [41416018](https://pubmed.ncbi.nlm.nih.gov/41416018/) | Systematic review — epidemiology (39 patients, 65% male), universal surgery, comorbidities | Aggregate clinical |
| [25677865](https://pubmed.ncbi.nlm.nih.gov/25677865/) | Strong heritability of CRSwNP (4.1× first-degree relative risk; no spousal risk) | Supporting genetic basis |
| [24717945](https://pubmed.ncbi.nlm.nih.gov/24717945/) | Eosinophil–epithelial MUC5AC/profibrotic mechanism (dyscrinia + remodeling) | Mechanism |
| [39158477](https://pubmed.ncbi.nlm.nih.gov/39158477/) | Type-2 alarmin–cytokine cascade (upstream polyp inflammation) | Mechanism |
| [42342265](https://pubmed.ncbi.nlm.nih.gov/42342265/), [42048140](https://pubmed.ncbi.nlm.nih.gov/42048140/), [42474633](https://pubmed.ncbi.nlm.nih.gov/42474633/) | Bronchiectasis "vicious vortex"; DPP-1 inhibition (brensocatib) | Mechanism/treatment |
| [41178615](https://pubmed.ncbi.nlm.nih.gov/41178615/), [42398863](https://pubmed.ncbi.nlm.nih.gov/42398863/), [41989130](https://pubmed.ncbi.nlm.nih.gov/41989130/) | Biologic efficacy for CRSwNP (dupilumab leading) | Treatment |
| [29414455](https://pubmed.ncbi.nlm.nih.gov/29414455/) | AERD/Samter's triad leukotriene mechanism (overlap endotype) | Mechanism |
| [16203616](https://pubmed.ncbi.nlm.nih.gov/16203616/), [34391405](https://pubmed.ncbi.nlm.nih.gov/34391405/), [41919747](https://pubmed.ncbi.nlm.nih.gov/41919747/) | PCD and CF differential diagnosis | Diagnostics |
| [38609095](https://pubmed.ncbi.nlm.nih.gov/38609095/) | Bronchiectasis prognosis (EMBARC registry) | Prognosis |
| [29605210](https://pubmed.ncbi.nlm.nih.gov/29605210/), [30961955](https://pubmed.ncbi.nlm.nih.gov/30961955/), [40832796](https://pubmed.ncbi.nlm.nih.gov/40832796/) | Pediatric bronchiectasis etiology/lobar distribution | Context |
| [41094464](https://pubmed.ncbi.nlm.nih.gov/41094464/) | WFDC2 screening in a sinopulmonary cohort (not identified — rarity) | Epidemiology |

---

## Limitations and Knowledge Gaps

1. **Small defining cohort.** BENP is molecularly established from only 11 individuals in 10 families ([PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/)); penetrance, expressivity, full variant spectrum, and natural history remain to be characterized in larger cohorts.
2. **Prevalence/carrier frequency undefined.** Precise gnomAD allele frequencies for pathogenic *WFDC2* variants and population carrier rates were not extracted here.
3. **Woakes'–BENP relationship not fully resolved.** How many historical Woakes' cases carry *WFDC2* variants is unknown; some Woakes'/CRSwNP-bronchiectasis cases are likely genetically heterogeneous (AERD, other loci). A Vietnamese cohort screened for *WFDC2* and found none ([PMID: 41094464](https://pubmed.ncbi.nlm.nih.gov/41094464/)).
4. **Mechanistic steps 5–7 are partly inferred.** The infection→inflammation→structural-damage chain in BENP specifically is extrapolated from general airway-disease biology, not yet demonstrated in a BENP-specific model.
5. **No validated animal model** of BENP is yet reported; rodent nasal-polyp face-validity is a concern.
6. **Citation-integrity note.** Some citation snippets for the defining paper (PMID 38626355) were flagged as "mismatch" during automated validation; the quoted content is consistent with the paper's established conclusions but exact abstract wording should be re-verified before database ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm/curate ontology mappings** (OMIM:620984 ≡ MONDO:0975835 ≡ MedGen:1874999) and re-verify the exact abstract quotes from [PMID: 38626355](https://pubmed.ncbi.nlm.nih.gov/38626355/) to resolve the "mismatch"-flagged snippets before knowledge-base entry.
2. **Assemble a larger BENP case series** via GeneMatcher/international collaboration to define penetrance, expressivity, age-of-onset distribution, and the full *WFDC2* variant spectrum with gnomAD frequencies.
3. **Validate the two-step diagnostic algorithm** (serum HE4 → *WFDC2* sequencing) prospectively in unexplained combined rhinosinusitis-plus-bronchiectasis cohorts, quantifying sensitivity/specificity against CF and PCD.
4. **Generate a *Wfdc2*-knockout (and p.Cys49Arg knock-in) mouse** and *WFDC2*-null human ALI/organoid cultures; assay airway antibacterial activity, secretion, mucin production, and infection susceptibility to test causal steps 4–7.
5. **Assess WFDC2 protein-replacement or gene therapy** conceptually (recombinant WFDC2 in ALI/organoid rescue experiments) as a rational disease-modifying strategy.
6. **Retrospectively genotype archived Woakes'-syndrome cases** for *WFDC2* to quantify the molecular overlap between the historical clinical entity and the new Mendelian disease.

---

*Report compiled from 12 confirmed findings across 5 investigation iterations and 60 reviewed papers. Evidence types are noted throughout as human clinical, in vitro, computational, or inferred/extrapolated.*


## Artifacts

- [OpenScientist final report](Bronchiectasis_And_Nasal_Polyposis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bronchiectasis_And_Nasal_Polyposis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 21 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0975835` (3 mentions) - the report calls it "MONDO"; MONDO calls it **bronchiectasis and nasal polyposis**
- `HP:0011950` (1 mention) - the report calls it "Laboratory/physical"; HP calls it **Unusual bronchiolitis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000414` (1 mention) - the report calls it "Broad nasal tip"; HP calls it **Bulbous nose**, and lists "Bulbous nasal tip" among its other names
- `HP:0002688` (1 mention) - the report calls it "Aplasia of the frontal sinus"; HP calls it **Absent frontal sinuses**, and lists "Aplasia of frontal sinus" among its other names
- `GO:0005576` (2 mentions) - the report calls it "Extracellular region / airway surface liquid"; GO calls it **extracellular region**
- `CL:0000158` (1 mention) - the report calls it "Airway secretory/club cells"; CL calls it **club cell**
- `CL:0002633` (1 mention) - the report calls it "Respiratory epithelial cells"; CL calls it **respiratory basal cell**
- `UBERON:0001004` (1 mention) - the report calls it "respiratory system", "Body system:** **respiratory system"; UBERON calls it **respiratory system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001004` - called "respiratory system", "Body system:** **respiratory system"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UMLS`.