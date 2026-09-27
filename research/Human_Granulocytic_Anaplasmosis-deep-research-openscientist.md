---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T02:46:33.624595'
end_time: '2026-09-25T03:02:16.125005'
duration_seconds: 942.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Human Granulocytic Anaplasmosis
  mondo_id: MONDO:0005118
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
citation_count: 20
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 20
  quotes_valid: 20
  relevance_assessed: 21
  on_topic: 13
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0016575
    ontology_label: obsolete histone deacetylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Human_Granulocytic_Anaplasmosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Human_Granulocytic_Anaplasmosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Human Granulocytic Anaplasmosis
- **MONDO ID:** MONDO:0005118 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Human Granulocytic Anaplasmosis** covering all of the
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

# Human Granulocytic Anaplasmosis (HGA): Comprehensive Disease Characterization Report

**Target Disease:** Human Granulocytic Anaplasmosis
**MONDO ID:** MONDO:0005118
**Category:** Infectious Disease (tick-borne zoonotic bacterial infection)
**Causative Agent:** *Anaplasma phagocytophilum* (human-active "Ap-ha" variant), NCBI Taxonomy ID: 948

---

## Summary

Human granulocytic anaplasmosis (HGA) is an acute, usually self-limiting tick-borne febrile illness caused by the obligate intracellular gram-negative bacterium *Anaplasma phagocytophilum*. It is transmitted principally by *Ixodes scapularis* (eastern/midwestern United States) and *Ixodes pacificus* (western United States), with small mammals — chiefly the white-footed mouse *Peromyscus leucopus* — serving as enzootic reservoirs. Only a single "human active" (Ap-ha) genetic variant of the bacterium causes human disease. HGA is fundamentally an **infectious** disease with **no human genetic etiology**: there are no causal genes, inheritance patterns, pathogenic germline variants, or vaccines. The dominant human "risk factors" are environmental and behavioral (tick exposure in endemic regions), with advanced age and immunosuppression predicting severe disease.

The pathogen has a unique biology: it is one of the few bacteria that survives and replicates inside **neutrophils**, the body's primary antibacterial effector cells. It accomplishes this through an elaborate program of subversion — entering via the PSGL-1/sialyl-Lewis^x receptor complex, then deploying Type IV secretion system (T4SS) effectors **AnkA** (which epigenetically silences the NADPH-oxidase gene *CYBB* via HDAC1 recruitment, blocking the respiratory burst) and **Ats-1** (which enters host mitochondria to block apoptosis and hijacks autophagy for nutrient acquisition). Crucially, the tissue injury and clinical severity of HGA are driven not by direct bacterial cytotoxicity — bacterial burdens are low relative to disease severity — but by the **host immune response**, specifically an IFN-γ/STAT1-driven immunopathology. In its most extreme form this dysregulation manifests as secondary hemophagocytic lymphohistiocytosis (HLH).

Clinically, HGA presents as a nonspecific febrile illness (fever in 88.5% of cases) accompanied by thrombocytopenia (71.8%), abnormal liver injury tests (66.7%), and leukopenia (49.8%). It is diagnosed by whole-blood PCR and IFA serology, with blood-smear morulae showing low sensitivity in early disease. **Doxycycline is rapidly curative first-line therapy for all ages**, with fever typically subsiding within one day; rifampin is the alternative in pregnancy. Prognosis is generally good (lethality ~3.0%, sequelae ~2.1%), though complications occur in ~40% of cases and advanced age plus immunosuppression predict severe/hospitalized disease. Prevention rests entirely on tick-bite avoidance, as no vaccine exists. The same bacterium naturally infects horses, dogs, cats, sheep, cattle, and goats, making HGA part of a broader multi-host zoonosis with important veterinary parallels.

---

## Key Findings

### Finding 1: HGA is a tick-borne infection of neutrophils presenting as a febrile illness with cytopenias

A systematic review of HGA cases established the core clinical and laboratory phenotype. HGA "primarily presents as an unspecific febrile illness (88.5% of the cases) often accompanied by thrombocytopenia (71.8% of the cases), abnormal liver injury tests (66.7% of the cases), and leukopenia (49.8% of the cases)" ([PMID: 39102427](https://pubmed.ncbi.nlm.nih.gov/39102427/)). Complications occurred in 40.5% of cases (acute renal failure 9.8%, multi-organ failure 7.5%, ARDS 6.3%), while "sequelae are rare (2.1% of the cases) and lethality is low (3.0% of the cases)."

This phenotypic signature — fever plus the triad of thrombocytopenia, transaminitis, and leukopenia — is the diagnostic fingerprint of HGA and reflects the pathogen's tropism for hematopoietic and granulocytic lineages. The nonspecific nature of the presentation is a central clinical challenge, since it overlaps with many other acute febrile illnesses and other tick-borne diseases (Lyme disease, babesiosis, ehrlichiosis).

**Suggested HPO terms:** Fever (HP:0001945), Thrombocytopenia (HP:0001873), Elevated hepatic transaminase (HP:0002910), Leukopenia (HP:0001882), Myalgia (HP:0003326), Headache (HP:0002315), Acute kidney injury (HP:0001919).

### Finding 2: *A. phagocytophilum* survives in neutrophils by subverting bactericidal functions and delaying apoptosis

The paradox of HGA is that the pathogen thrives inside the very cell type designed to destroy it. The bacterium "infects and actively grows in neutrophils by employing an array of mechanisms to subvert their bactericidal activity. These include its ability to inhibit phagosome-lysosome fusion, to suppress respiratory burst and to delay the apoptotic death of neutrophils" ([PMID: 17275372](https://pubmed.ncbi.nlm.nih.gov/17275372/)).

An Affymetrix microarray study of infected human polymorphonuclear leukocytes (PMNs) demonstrated the apoptosis-evasion mechanism directly: "ingestion of *A. phagocytophilum* failed to trigger the neutrophil apoptosis differentiation program that typically follows phagocytosis and ROS production" ([PMID: 15879137](https://pubmed.ncbi.nlm.nih.gov/15879137/)). Normally, neutrophils undergo a programmed apoptotic death shortly after phagocytosis; by suppressing this program, the bacterium extends the lifespan of its intracellular niche, buying time for replication.

**Suggested GO terms:** negative regulation of apoptotic process (GO:0043066), negative regulation of respiratory burst (GO:0060264), phagosome-lysosome fusion (GO:0090385). **Suggested CL term:** neutrophil (CL:0000775).

### Finding 3: Type IV secretion effectors AnkA and Ats-1 drive intracellular subversion

The molecular machinery of subversion is the T4SS and its two best-characterized effectors. **AnkA** (Ankyrin A) "enters the granulocyte nucleus, binds stretches of AT-rich DNA and alters transcription of antimicrobial defence genes, including down-regulation of *CYBB*" ([PMID: 25996657](https://pubmed.ncbi.nlm.nih.gov/25996657/)). AnkA recruits histone deacetylase 1 (HDAC1) to the *CYBB* (gp91phox/NADPH oxidase) promoter, causing histone H3 deacetylation and epigenetic silencing — directly disabling the enzyme responsible for the neutrophil respiratory burst. This is a striking example of a bacterial effector functioning as a host transcriptional/epigenetic regulator.

**Ats-1** (Anaplasma translocated substrate 1) operates at the mitochondria: it "inhibited etoposide-induced cytochrome c release from mitochondria, PARP cleavage, and apoptosis in mammalian cells" ([PMID: 20174550](https://pubmed.ncbi.nlm.nih.gov/20174550/)). Ats-1 additionally hijacks autophagy: it "binds Beclin 1, a subunit of the class III PI3K and Atg14L, and it nucleates autophagosomes" ([PMID: 23197835](https://pubmed.ncbi.nlm.nih.gov/23197835/)), redirecting autophagosomal cargo to feed the bacterium. Multi-omics work further shows Ats-1 up-regulates respiratory-chain subunits (NDUFB5, NDUFB3, NDUFS7, COX6C, SLC25A5), enhancing host ATP production and inhibiting apoptosis to support bacterial replication.

**Suggested GO terms:** modulation by symbiont of host process (GO:0044003), negative regulation of host apoptotic process, autophagosome assembly (GO:0000045), histone deacetylation (GO:0016575).

### Finding 4: Doxycycline is highly effective; advanced age and immunosuppression predict severe disease

"Treatment with doxycycline shows a rapid response, with the fever subsiding in the majority of patients within one day of starting treatment" ([PMID: 39102427](https://pubmed.ncbi.nlm.nih.gov/39102427/)). This rapid defervescence is so characteristic that a prompt response to empiric doxycycline supports the diagnosis.

Prognostic stratification comes from a 465-case Mayo Clinic cohort (2011–2021), in which 33% of patients were hospitalized. "Hospitalized patients (n = 153, 33%) were more likely to be older (median age of 71 vs 61; P ≤ .001) and immunocompromised (17% vs 7%; P ≤ .001)" ([PMID: 40176262](https://pubmed.ncbi.nlm.nih.gov/40176262/)). Additional risk factors for hospitalization included altered mental status, higher absolute neutrophil count, and comorbidities. Notably, coinfection (e.g., with *Borrelia burgdorferi* or *Babesia microti*) did not impact mortality or hospitalization in this cohort.

**Suggested NCIT term:** Doxycycline (NCIT:C731).

### Finding 5: Entry via PSGL-1/sialyl-Lewis^x and persistence via msp2(p44) antigenic variation

The molecular entry mechanism is well defined: "P-selectin glycoprotein ligand-1 (PSGL-1) and the tetrasaccharide sialyl Lewis x (sLe(x)), which caps the PSGL-1 N-terminus, are confirmed *A. phagocytophilum* receptors" ([PMID: 18485118](https://pubmed.ncbi.nlm.nih.gov/18485118/)). PSGL-1 N-terminus-mediated entry is Syk-dependent and promotes optimal delivery of the AnkA effector, linking receptor engagement to the downstream subversion program.

Persistence and immune evasion are achieved through antigenic variation of the immunodominant major surface protein: "*A. phagocytophilum* utilizes gene conversion to shuffle approximately 100 functional pseudogenes into a single expression cassette of the msp2(p44) gene, which encodes the major surface antigen, major surface protein 2 (Msp2)" ([PMID: 22859615](https://pubmed.ncbi.nlm.nih.gov/22859615/)). In chronically infected reservoir woodrats, 60 unique expression-site variants emerged over the course of infection — a continuously moving antigenic target that frustrates the antibody response.

### Finding 6: HGA is an emerging *Ixodes*-borne zoonosis; only the Ap-ha variant is human-pathogenic

HGA is transmitted primarily by *Ixodes scapularis* (eastern/midwestern US) and *I. pacificus* (western US), with reservoirs in small mammals, chiefly *Peromyscus leucopus* (white-footed mouse) and eastern chipmunks. Critically, only one variant infects humans: studies reference "the zoonotic variant Ap-ha (human active) of the bacterium *Anaplasma phagocytophilum*" ([PMID: 41016325](https://pubmed.ncbi.nlm.nih.gov/41016325/)). Approximately 90–100% of infected reservoir small mammals in southeastern Canada carried Ap-ha.

The disease burden is substantial and rising. US hospitalization data show that "Lyme disease was the most common cause, accounting for 65% of hospitalizations (171,328 admissions), followed by ehrlichiosis/anaplasmosis (46,446)" over 2002–2021 ([PMID: 41003548](https://pubmed.ncbi.nlm.nih.gov/41003548/)), with tick-borne disease hospitalizations increasing 2.5-fold. The burden concentrates in the Northeast (52.9% of TBD hospitalizations), peaks in July, and affects males slightly more (53.9%). Rare non-tick transmission occurs: "Although usually transmitted via tick bite, HGA may rarely also be acquired through transfusion" ([PMID: 25385549](https://pubmed.ncbi.nlm.nih.gov/25385549/)) — and leukoreduction does not reliably prevent transfusion transmission — as well as perinatally.

### Finding 7: HGA tissue injury is immunopathologic, driven by IFN-γ/STAT1 signaling

A defining and mechanistically important feature of HGA is that disease severity is disproportionate to bacterial burden, pointing to an immune-mediated pathology. "IFN-γ, is necessary for innate immunity and plays an important role in the induction of severe histopathology in *A. phagocytophilum*-infected mice, horses and humans" ([PMID: 23278812](https://pubmed.ncbi.nlm.nih.gov/23278812/)). The downstream signaling node is STAT1: an "increase in phosphorylated Stat1 (pStat1) correlated significantly with IFN-γ production and inflammatory tissue injury," with phosphorylated STAT1 markedly increased by day 7 post-infection in infected mice.

This immunopathologic model reframes HGA: the pathogen sets off a host inflammatory cascade (via TLR2/NF-κB and IFN-γ/STAT1) that produces the observed organ injury. It is reinforced by the observation, in CNS involvement, that "CSF abnormalities did not correlate with neurologic severity, suggesting a cytokine-mediated process rather than direct central nervous system infection" ([PMID: 42230277](https://pubmed.ncbi.nlm.nih.gov/42230277/)).

**Suggested GO terms:** interferon-gamma-mediated signaling pathway (GO:0060333), inflammatory response (GO:0006954), response to interferon-gamma (GO:0034341).

### Finding 8: Diagnosis relies on PCR and serology; blood-smear morulae have low early sensitivity

"The laboratory diagnosis is most frequently serological—evidence of antibody by indirect immunofluorescence assay (IFA) and detection of DNA by polymerase chain reaction (PCR), or microscopy evidence—Giemsa stain of blood smears (morulae in granulocytes or monocytes)" ([PMID: 20077398](https://pubmed.ncbi.nlm.nih.gov/20077398/)). Morulae are intracytoplasmic microcolonies of the bacterium — the pathognomonic but insensitive microscopic finding.

A Korean hospital cohort quantified this insensitivity: "Of the 18 patients who underwent peripheral blood (PB) smear test, only one (5.6%) had morulae" ([PMID: 34035378](https://pubmed.ncbi.nlm.nih.gov/34035378/)). Because both morulae detection and IFA (which requires seroconversion) are insensitive in early disease, whole-blood PCR is the primary early diagnostic tool, and empiric doxycycline should not await confirmation.

### Finding 9: Doxycycline is first-line for all ages; rifampin is the alternative in pregnancy

In a case series of six pregnant women with HGA, disease was non-fulminant and "all treated patients had excellent responses to rifampin or doxycycline therapy. Perinatal transmission was documented in 1 neonate, who responded well to treatment" ([PMID: 17682993](https://pubmed.ncbi.nlm.nih.gov/17682993/)), with no long-term sequelae in offspring at a mean follow-up of 21 months. A transfusion-associated case in a pregnant patient was successfully treated with rifampin ([PMID: 25385549](https://pubmed.ncbi.nlm.nih.gov/25385549/)). Doxycycline remains the drug of choice across all systematic reviews and all age groups; rifampin is reserved for pregnancy and doxycycline intolerance.

**Suggested NCIT terms:** Doxycycline (NCIT:C731), Rifampin (NCIT:C692).

### Finding 10: *A. phagocytophilum* is a multi-host zoonotic pathogen (granulocytic anaplasmosis / tick-borne fever)

The same bacterium causes disease across many mammalian species. Genetic typing (ankA, groEL, MLST) shows "the *A. phagocytophilum* strains found infecting cats are the same as those that cause disease in humans, dogs and horses" ([PMID: 37803346](https://pubmed.ncbi.nlm.nih.gov/37803346/)). In naturally PCR-positive horses, hematological abnormalities occurred in 95%, dominated by thrombocytopenia (86%) and anemia (52%) — paralleling the human thrombocytopenia phenotype ([PMID: 36436292](https://pubmed.ncbi.nlm.nih.gov/36436292/)). In ruminants the disease is called tick-borne fever (TBF): "By itself TBF does not cause high mortality rates but infected animals are more susceptible to other secondary infections, pregnant animals may abort and there is a severe reduction in milk yield in dairy cattle" ([PMID: 17275372](https://pubmed.ncbi.nlm.nih.gov/17275372/)).

**Suggested NCBI Taxonomy identifiers for affected species:** *Homo sapiens* (9606), *Equus caballus* (9796), *Canis lupus familiaris* (9615), *Felis catus* (9685), *Ovis aries* (9940), *Bos taurus* (9913), *Capra hircus* (9925), *Peromyscus leucopus* (10041).

### Finding 11: Severe anaplasmosis can trigger secondary HLH, a treatable immune-dysregulation complication

The immunopathologic model reaches its extreme in secondary HLH. Case reports "present two cases of severe anaplasmosis that progressed to secondary hemophagocytic lymphohistiocytosis (HLH). This severe immune dysregulation syndrome has an extremely high mortality, but anaplasmosis represents one of the few treatable underlying etiologies" ([PMID: 32723647](https://pubmed.ncbi.nlm.nih.gov/32723647/)). One "anaplasmosis-induced HLH successfully treated with a combination of doxycycline, steroids, and anakinra (an IL-1 receptor antagonist)" — demonstrating that this primarily immune-mediated complication responds to both antimicrobial therapy and immunosuppression, and reinforcing the cytokine-driven mechanism.

**Suggested NCIT terms:** Anakinra (NCIT:C1594), Corticosteroid therapy. **Suggested HPO term:** Hemophagocytosis (HP:0012156).

### Finding 12: Integrated model — pathogen-driven neutrophil subversion produces host IFN-γ/STAT1 immunopathology, reversible with doxycycline

Synthesizing all findings, HGA follows a coherent causal chain from tick inoculation of the Ap-ha variant to a febrile cytopenic illness that is fully reversible with doxycycline. The upstream arm is pathogen-driven (receptor entry → T4SS effectors → neutrophil subversion); the downstream arm is host-driven (IFN-γ/STAT1 immunopathology → clinical disease, and in extreme cases HLH). Clinically this yields fever (88.5%), thrombocytopenia (71.8%), transaminitis (66.7%), and leukopenia (49.8%) with low lethality (3.0%), and doxycycline produces defervescence within ~1 day. There is no human causal gene, inheritance pattern, or vaccine; prevention is tick-bite avoidance. The two anchoring facts of this synthesis are the clinical output ([PMID: 39102427](https://pubmed.ncbi.nlm.nih.gov/39102427/)) and the immunopathology driver ([PMID: 23278812](https://pubmed.ncbi.nlm.nih.gov/23278812/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating exposure → clinical manifestation)

1. An *Ixodes scapularis* or *I. pacificus* tick carrying the **Ap-ha (human-active)** variant of *A. phagocytophilum* bites a human and inoculates the bacterium. *(demonstrated — vector/variant epidemiology)*
2. Circulating bacteria bind **PSGL-1** capped by **sialyl-Lewis^x** on neutrophils and myeloid precursors, **leading to** Syk-dependent internalization into a host-derived vacuole. *(demonstrated in vitro)*
3. Internalization **results in** assembly of the Type IV secretion system and translocation of effectors into the host cell. *(demonstrated)*
4. **AnkA** traffics to the nucleus, binds AT-rich DNA at the *CYBB* promoter, and recruits **HDAC1**, **causing** histone H3 deacetylation and epigenetic silencing of *CYBB* (gp91phox) — this **blocks the NADPH-oxidase respiratory burst**. *(demonstrated)*
5. In parallel, **Ats-1** enters host **mitochondria** and inhibits cytochrome c release and PARP cleavage, **blocking apoptosis**; it also binds **Beclin 1/Atg14L** to nucleate autophagosomes and divert nutrients to the bacterium. *(demonstrated in vitro/cell models)*
6. Suppressed oxidative killing + delayed apoptosis + nutrient acquisition **result in** unchecked intracellular bacterial replication and formation of morulae. *(demonstrated)*
7. **Branch — immune sensing:** bacterial ligands engage **TLR2 → NF-κB** and drive **IFN-γ** production; IFN-γ signaling **leads to** STAT1 phosphorylation (pSTAT1). *(demonstrated in mouse/comparative models; inferred in humans)*
8. Elevated **IFN-γ/pSTAT1** **causes** inflammatory, immunopathologic tissue injury that is **disproportionate to bacterial burden** — producing fever, hepatic transaminitis, and organ dysfunction. *(demonstrated in animal models; strongly inferred in humans)*
9. Consumption/sequestration and marrow effects **result in** **thrombocytopenia and leukopenia**; the febrile cytopenic syndrome is the clinical readout. *(demonstrated clinically; mechanism partly inferred)*
10. **Extreme branch:** in a subset (older/immunocompromised), unchecked cytokine activation **leads to** secondary **HLH**. *(demonstrated in case reports)*
11. **Doxycycline** halts bacterial protein synthesis, **collapsing** the effector-driven subversion and interrupting the cytokine cascade, **resulting in** defervescence within ~1 day and full recovery in the great majority. *(demonstrated clinically)*

### Schematic

```
   Ixodes tick (Ap-ha variant)
              │  inoculation
              ▼
   PSGL-1 / sialyl-Lewis^x  ──Syk──►  neutrophil entry
              │
              ▼
       T4SS effector translocation
        ├── AnkA → nucleus → HDAC1 at CYBB → ✗ respiratory burst
        └── Ats-1 → mitochondria → ✗ apoptosis; Beclin1 → autophagy nutrient theft
              │
              ▼
   Intracellular replication (morulae), low total burden
              │
     ┌────────┴─────────────┐
     ▼ (pathogen arm)        ▼ (host arm)
  neutrophil dysfunction   TLR2/NF-κB + IFN-γ → pSTAT1
                              │
                              ▼
                   IMMUNOPATHOLOGY (severity ≫ burden)
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   fever (88.5%)     thrombocytopenia (71.8%)   transaminitis (66.7%)
                     leukopenia (49.8%)          → extreme: HLH
                              │
                    doxycycline (≤1 day defervescence) → recovery
```

### Upstream vs downstream

| Layer | Mechanism | Direction | Evidence type |
|---|---|---|---|
| Vector/variant | *Ixodes* transmission of Ap-ha | Most upstream | Epidemiology (human) |
| Entry | PSGL-1/sLe^x/Syk | Upstream | In vitro |
| Subversion | AnkA (CYBB silencing), Ats-1 (anti-apoptosis, autophagy) | Upstream | In vitro / cell models |
| Immune sensing | TLR2/NF-κB, IFN-γ/STAT1 | Midstream | Mouse/comparative; inferred in human |
| Immunopathology | Cytokine-driven tissue injury | Downstream | Animal + clinical inference |
| Clinical | Fever, cytopenias, transaminitis, HLH | Most downstream | Human clinical |

**Cell types involved (CL):** neutrophil (CL:0000775), granulocyte (CL:0000094), monocyte (CL:0000576), macrophage (CL:0000235). **Anatomical structures (UBERON):** blood (UBERON:0000178), bone marrow (UBERON:0002371), liver (UBERON:0002107), spleen (UBERON:0002106), lung (UBERON:0002048), kidney (UBERON:0002113). **Subcellular (GO CC):** nucleus (GO:0005634), mitochondrion (GO:0005739), autophagosome (GO:0005776).

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding | Evidence type |
|---|---|---|---|
| [39102427](https://pubmed.ncbi.nlm.nih.gov/39102427/) | *HGA — systematic review* | F1, F4, F12 (clinical phenotype, doxycycline, prognosis) | Human clinical (systematic review) |
| [17275372](https://pubmed.ncbi.nlm.nih.gov/17275372/) | *Immune evasion & immunosuppression by A. phagocytophilum* | F2, F10 (neutrophil subversion; ruminant TBF) | Review / in vitro |
| [15879137](https://pubmed.ncbi.nlm.nih.gov/15879137/) | *Fails to induce apoptosis in human neutrophils* | F2 (apoptosis delay) | In vitro (human PMN microarray) |
| [25996657](https://pubmed.ncbi.nlm.nih.gov/25996657/) | *Chromatin-bound AnkA recruits HDAC1* | F3 (AnkA epigenetic silencing) | In vitro / molecular |
| [20174550](https://pubmed.ncbi.nlm.nih.gov/20174550/) | *Ats-1 imported into mitochondria, blocks apoptosis* | F3 (Ats-1 anti-apoptosis) | In vitro |
| [23197835](https://pubmed.ncbi.nlm.nih.gov/23197835/) | *Autophagosomes induced by bacterial Beclin 1-binding protein* | F3 (Ats-1 autophagy hijack) | In vitro |
| [40176262](https://pubmed.ncbi.nlm.nih.gov/40176262/) | *Trends in anaplasmosis over the past decade* | F4 (prognostic risk factors) | Human clinical (465-case cohort) |
| [18485118](https://pubmed.ncbi.nlm.nih.gov/18485118/) | *PSGL-1-independent infection, Syk, AnkA delivery* | F5 (entry receptors) | In vitro |
| [22859615](https://pubmed.ncbi.nlm.nih.gov/22859615/) | *Antigen variability during chronic reservoir infection* | F5 (msp2/p44 antigenic variation) | In vivo (reservoir host) |
| [41016325](https://pubmed.ncbi.nlm.nih.gov/41016325/) | *Small mammal hosts of zoonotic A. phagocytophilum, Canada* | F6 (Ap-ha variant, reservoirs) | Field epidemiology |
| [41003548](https://pubmed.ncbi.nlm.nih.gov/41003548/) | *Hospitalizations for TBDs in the US 2002–2021* | F6 (US burden) | Epidemiology (registry) |
| [25385549](https://pubmed.ncbi.nlm.nih.gov/25385549/) | *Transfusion-associated infection in pregnancy* | F6, F9 (non-vector transmission; rifampin) | Case report |
| [23278812](https://pubmed.ncbi.nlm.nih.gov/23278812/) | *IFN-γ production and Stat1 signaling* | F7, F12 (immunopathology) | Model organism + comparative |
| [42230277](https://pubmed.ncbi.nlm.nih.gov/42230277/) | *CSF findings in CNS anaplasmosis* | F7 (cytokine-mediated, not direct CNS infection) | Human clinical |
| [15122530](https://pubmed.ncbi.nlm.nih.gov/15122530/) | *TLR2 activation of NF-κB by A. phagocytophilum* | F7/F12 (innate sensing branch) | In vitro |
| [20077398](https://pubmed.ncbi.nlm.nih.gov/20077398/) | *Ehrlichiosis/Anaplasmosis* | F8 (diagnostic modalities) | Review |
| [34035378](https://pubmed.ncbi.nlm.nih.gov/34035378/) | *HGA in a single Korean university hospital* | F8 (morulae low sensitivity) | Human clinical cohort |
| [17682993](https://pubmed.ncbi.nlm.nih.gov/17682993/) | *HGA during pregnancy: case series* | F9 (rifampin/doxycycline in pregnancy) | Case series |
| [37803346](https://pubmed.ncbi.nlm.nih.gov/37803346/) | *Feline granulocytic anaplasmosis, strain typing* | F10 (cross-species strains) | Veterinary/molecular |
| [36436292](https://pubmed.ncbi.nlm.nih.gov/36436292/) | *A. phagocytophilum in German horses* | F10 (equine hematologic parallels) | Veterinary retrospective |
| [32723647](https://pubmed.ncbi.nlm.nih.gov/32723647/) | *Severe anaplasmosis as treatable cause of HLH* | F11 (HLH complication) | Case reports + review |

Across the evidence base, the **clinical phenotype and treatment findings** rest on human systematic reviews and cohorts (strong for descriptive epidemiology); the **molecular subversion mechanisms** rest on robust in vitro and cell-model data; and the **immunopathology model** is strongest in mouse and comparative (horse) systems and is inferred — though well-supported — in humans by the dissociation between low bacterial burden and disease severity, and by cytokine-mediated CSF findings.

---

## Section-by-Section Knowledge Base Content

**1. Disease Information.** HGA is an acute tick-borne bacterial infection of neutrophils. Identifiers: MONDO:0005118; MeSH "Anaplasmosis"/"Ehrlichiosis, Human, Granulocytic"; ICD-10 A79.82 (Anaplasmosis); ICD-11 ~1C30.2. No OMIM/Orphanet genetic entry (not a Mendelian disease). Synonyms: human granulocytic ehrlichiosis (HGE, historical), granulocytic anaplasmosis. Information is derived from aggregated disease-level clinical and epidemiological resources, not germline genetics.

**2. Etiology.** Causal factor is **infectious** — the Ap-ha variant of *A. phagocytophilum*. Risk factors are environmental/behavioral: residence or activity in *Ixodes*-endemic regions (Northeast/Upper Midwest/Pacific US), outdoor exposure in tick season (peak July), advanced age, and immunosuppression (severity). **No genetic risk, protective, or gene-environment factors are established** in humans.

**3. Phenotypes.** Fever (88.5%; HP:0001945), thrombocytopenia (71.8%; HP:0001873), transaminitis (66.7%; HP:0002910), leukopenia (49.8%; HP:0001882); myalgia, headache, chills, arthralgia common; complications include acute renal failure (9.8%), multi-organ failure (7.5%), ARDS (6.3%). Rare: subdural hematoma/CNS involvement, pulmonary embolism, HLH. Onset acute; severity mild-to-severe/variable; course self-limited with treatment.

**4. Genetic/Molecular Information.** **Not applicable at the human host level** — no causal genes, pathogenic variants, modifier genes, or chromosomal abnormalities. The relevant molecular biology is the *pathogen's* virulence genes (ankA, ats-1, msp2/p44, T4SS/virB-virD4) and the *host* genes they target (CYBB/gp91phox silencing; mitochondrial respiratory-chain subunits NDUFB5/NDUFB3/NDUFS7/COX6C/SLC25A5 up-regulated).

**5. Environmental Information.** Infectious agent: *A. phagocytophilum* (NCBI Taxon 948). Vectors: *Ixodes scapularis*, *I. pacificus* (also *I. ricinus* in Europe). Reservoirs: *Peromyscus leucopus*, chipmunks, other small mammals. Transmission mainly by tick bite; rare via blood transfusion and perinatally.

**6. Mechanism/Pathophysiology.** See the ordered causal chain and schematic above. Molecular pathways: TLR2/NF-κB, IFN-γ/JAK-STAT1; host NADPH-oxidase pathway (silenced); mitochondrial apoptosis and autophagy (subverted). Immune involvement is central and immunopathologic.

**7. Anatomical Structures Affected.** Primary: blood/hematopoietic system (neutrophils; UBERON:0000178, bone marrow UBERON:0002371). Secondary: liver (UBERON:0002107), spleen, kidney, lung, occasionally CNS. Subcellular: host cytoplasmic vacuole, nucleus (AnkA target; GO:0005634), mitochondria (Ats-1 target; GO:0005739), autophagosome (GO:0005776).

**8. Temporal Development.** Onset acute, ~5–14 days post-tick bite; disease is typically self-limited and resolves rapidly with doxycycline (fever ≤1 day). Untreated disease can progress to complications; chronic human infection is not established (unlike persistent reservoir-host infection).

**9. Inheritance and Population.** No inheritance (infectious). Epidemiology: rising US incidence; concentrated in Northeast/Upper Midwest; seasonal July peak; slight male predominance (53.9%); older adults over-represented among hospitalized. Not a genetic disease — penetrance/expressivity/founder effects N/A.

**10. Diagnostics.** Whole-blood **PCR** (primary, sensitive early), **IFA serology** (paired acute/convalescent; insensitive early), Giemsa **blood smear morulae** (specific but ~5.6% sensitive early). Supportive labs: CBC (thrombocytopenia, leukopenia), elevated transaminases, elevated CRP. Differential: ehrlichiosis, Lyme disease, babesiosis, other acute febrile illnesses.

**11. Outcome/Prognosis.** Good: lethality ~3.0%, sequelae ~2.1%. Complications in ~40.5%. Prognostic factors: advanced age, immunosuppression, altered mental status, comorbidities. Rapid recovery with timely doxycycline.

**12. Treatment.** **Doxycycline** first-line, all ages (NCIT:C731); **rifampin** in pregnancy/intolerance (NCIT:C692). Severe/HLH cases: doxycycline + corticosteroids ± anakinra (IL-1RA). No gene/cell/RNA therapies applicable.

**13. Prevention.** No vaccine. Primary prevention = tick-bite avoidance (permethrin-treated clothing, DEET/IR3535 repellents, tick checks, landscape/rodent-targeted interventions). Secondary prevention = early empiric treatment. Public health: vector/reservoir control, health education.

**14. Other Species / Natural Disease.** Natural disease in horses (equine granulocytic anaplasmosis), dogs, cats, and ruminants (tick-borne fever with abortion, reduced milk yield, immunosuppression). Shared strains across humans/dogs/horses/cats confirm zoonotic cross-species susceptibility.

**15. Model Organisms.** Mouse models (used to establish IFN-γ/STAT1 immunopathology); naturally infected horses, sheep/lambs (msp2/p44 persistence studies), and reservoir woodrats/*Peromyscus* (antigenic variation). In vitro: HL-60 promyelocytic cells, human PMNs, HEK293T (effector studies). These recapitulate neutrophil infection, cytopenias, and immunopathology; they do not fully capture human clinical heterogeneity.

---

## Limitations and Knowledge Gaps

- **Immunopathology in humans is inferred, not directly demonstrated.** The IFN-γ/STAT1 model is strongest in mouse and horse systems; direct human tissue-level causal evidence is limited, resting on the burden–severity dissociation and cytokine-mediated CSF findings.
- **Host genetic determinants of human severity are unknown.** Why some patients (beyond age/immunosuppression) develop severe disease or HLH is not defined; no human susceptibility loci have been mapped.
- **Mechanistic link from subversion to specific cytopenias is incomplete.** The pathways producing thrombocytopenia and leukopenia (marrow suppression vs peripheral consumption/sequestration) are not fully resolved.
- **Effector biology gaps.** Only 3 of ≥6 T4SS effectors are functionally characterized; the full effector repertoire and its integration with host signaling remain open.
- **Diagnostic performance data are heterogeneous.** Sensitivity/specificity of PCR vs serology across disease stages come from varied, sometimes small cohorts.
- **No controlled trial data** exist for HLH-directed immunomodulation in anaplasmosis; evidence is anecdotal (case reports).
- **Publication/case-report bias** likely inflates the apparent frequency of rare severe manifestations (CNS, HLH, thromboembolism) relative to the true population.

---

## Proposed Follow-up Experiments / Actions

1. **Human immunophenotyping study:** longitudinal serum cytokine profiling (IFN-γ, IL-1, IL-6, IL-18, ferritin) and pSTAT1 in circulating leukocytes in HGA patients stratified by severity, to directly test the immunopathology model and identify HLH-risk biomarkers.
2. **Host-genetics of severity:** targeted or exome sequencing of severe/HLH HGA cases (e.g., PRF1, UNC13D, STXBP2 HLH genes) to test whether occult HLH predisposition underlies severe outcomes.
3. **Effector–pathway mapping:** complete the functional characterization of the remaining T4SS effectors and their host targets using proximity labeling/interactomics in primary human neutrophils.
4. **Mechanistic dissection of cytopenias:** bone marrow and platelet-kinetic studies (or murine models) to determine whether thrombocytopenia/leukopenia are marrow-suppressive or consumptive.
5. **Diagnostics benchmarking:** prospective multicenter head-to-head evaluation of PCR vs IFA vs smear vs emerging antigen/metagenomic assays across defined time-since-onset windows.
6. **Immunomodulation registry:** structured case registry (or adaptive platform) for anaplasmosis-associated HLH to evaluate doxycycline ± corticosteroids ± anakinra outcomes.
7. **Prevention translation:** field evaluation of rodent-targeted acaricide/vaccine interventions specifically on Ap-ha (human-active) variant prevalence, not just total *A. phagocytophilum*.

---

## Consensus Answer

Human granulocytic anaplasmosis (HGA; MONDO:0005118) is an acute, usually self-limiting tick-borne febrile illness caused by the obligate intracellular bacterium *Anaplasma phagocytophilum* (human-active "Ap-ha" variant), transmitted mainly by *Ixodes* ticks and characterized by fever with thrombocytopenia, transaminitis, and leukopenia. The pathogen uniquely infects neutrophils — entering via PSGL-1/sialyl-Lewis^x and surviving via Type IV secretion effectors AnkA (HDAC1-mediated epigenetic silencing of the NADPH-oxidase gene *CYBB*) and Ats-1 (mitochondrial anti-apoptosis and autophagy hijacking) — while tissue injury is driven by an IFN-γ/STAT1 immunopathologic host response rather than direct bacterial damage. HGA has no human genetic etiology or vaccine; diagnosis is by whole-blood PCR and IFA serology, doxycycline is rapidly curative first-line therapy (rifampin in pregnancy), and prognosis is good (lethality ~3%), with advanced age and immunosuppression predicting severe disease.


## Artifacts

- [OpenScientist final report](Human_Granulocytic_Anaplasmosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Human_Granulocytic_Anaplasmosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016575` (obsolete histone deacetylation) (1 mention)

33 of 34 terms resolved to a current term; the rest could not be looked up either way.