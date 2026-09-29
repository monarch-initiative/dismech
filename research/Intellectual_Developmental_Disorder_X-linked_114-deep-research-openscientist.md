---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T15:00:26.802510'
end_time: '2026-09-25T15:19:18.397254'
duration_seconds: 1131.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Developmental Disorder, X-Linked 114
  mondo_id: MONDO:0975828
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
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 1
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 26
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0975828
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder, X-linked 114
  - term_id: HP:0002317
    reported_labels:
    - Motor incoordination / clumsiness
    ontology_label: Unsteady gait
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_X-linked_114-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_X-linked_114-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, X-Linked 114
- **MONDO ID:** MONDO:0975828 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, X-Linked 114** covering all of the
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

# Intellectual Developmental Disorder, X-Linked 114 (XLID114): A Comprehensive Disease Characterization

**Disease:** Intellectual Developmental Disorder, X-Linked 114 (XLID114)
**MONDO ID:** MONDO:0975828 · **OMIM:** 301134 · **MedGen:** C5974891
**Causal gene:** *SRPK3* (SRSF protein kinase 3), Xq28
**Category:** Mendelian, X-linked recessive, syndromic neurodevelopmental disorder

---

## Summary

Intellectual Developmental Disorder, X-Linked 114 (XLID114) is an **ultra-rare, X-linked recessive syndromic neurodevelopmental disorder** first defined in 2024 by Roychaudhury et al. ([PMID: 39073169](https://pubmed.ncbi.nlm.nih.gov/39073169/)). It is caused by **hemizygous loss-of-function or kinase-impairing variants in *SRPK3*** (SRSF protein kinase 3), a serine/arginine (SR) protein-specific kinase located at Xq28. The disorder was delineated in **9 affected males from 5 unrelated families**, of whom the 8 postnatally ascertained cases shared a core clinical tetrad of **impaired intellectual development, agenesis of the corpus callosum, abnormal (uncontrolled) eye movements, and ataxia**, frequently accompanied by cerebellar atrophy. A ninth, prenatally ascertained case had a more complex structural brain phenotype.

The mechanism is **loss or impairment of SRPK3 kinase activity, leading to dysregulated phosphorylation of SR splicing factors and consequently aberrant pre-mRNA splicing during neurodevelopment**. This investigation triangulated the mechanism through three converging computational lines of evidence generated across five iterations: (1) all five reported disease variants localize to the single large SRPK3 protein-kinase domain; (2) *SRPK3* is markedly **cerebellum-enriched** in GTEx expression data among CNS regions, matching the cerebellar-predominant phenotype; and (3) the STRING interactome of SRPK3 is dominated by **SR splicing-factor substrates (SRSF1/4/5/6) and core spliceosome components**. Causality is further supported by a **srpk3-knockout zebrafish** that recapitulates ocular-motor deficits, cerebellar agenesis, and behavioral abnormalities.

There is **no disease-specific therapy**. Management is supportive and multidisciplinary (developmental/physical/occupational/speech therapy, ophthalmologic and neurologic care), with genetic counseling and prenatal/carrier testing offered to at-risk families. Because the disorder was described only in 2024 from a single cohort, most disease-level characteristics (precise prevalence, penetrance, natural history, prognosis) remain incompletely defined and are extrapolated from the founding cohort and from SRPK-family biology.

---

## 1. Disease Information

**Overview.** XLID114 is a Mendelian, X-linked recessive syndromic form of intellectual developmental disorder in which affected males present with cognitive impairment plus a distinctive neurodevelopmental/neuro-ophthalmologic constellation — agenesis of the corpus callosum, abnormal eye movements, and ataxia, often with cerebellar atrophy. It belongs to the large and heterogeneous group of X-linked intellectual disability (XLID) disorders and is numbered 114 in the OMIM series.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 301134 |
| MONDO | MONDO:0975828 |
| MedGen | C5974891 |
| Gene | *SRPK3* (SRSF protein kinase 3) |
| Gene OMIM (MIM) | 301002 |
| HGNC | HGNC:11402 |
| NCBI Gene | 26576 |
| Ensembl | ENSG00000184343 |
| UniProt | Q9UPE1 |
| RefSeq | NM_014370.4 / NP_055185.2 |
| Cytoband | Xq28 |

**Synonyms / alternative names.** Intellectual developmental disorder, X-linked 114; XLID114; MRX114. Gene aliases: *MSSK1* (muscle-specific serine kinase 1), *STK23* (serine/threonine kinase 23).

**Information source.** The disease-level knowledge is derived from **aggregated resources and a single primary cohort study** (OMIM, MONDO, MedGen entries anchored to Roychaudhury et al. 2024), not from population EHR data. Given the ultra-rare nature, individual-patient descriptions come from the 9 reported cases.

---

## 2. Etiology

**Primary cause — genetic.** XLID114 is a **monogenic disorder** caused by hemizygous variants in *SRPK3*. Roychaudhury et al. identified four missense variants and one truncating variant segregating with disease in affected males across five families:

> *"here we identified 4 missense variants (c.475C > G; p.H159D, c.1373C > A; p.T458N, and c.1585G > A; p.E529K, c.953C > T; p.S318L) and a putative truncating variant (c.1413_1414del; p.Y471*) in the SRPK3 gene in 9 XLID patients from 5 unrelated families"* — [PMID: 39073169](https://pubmed.ncbi.nlm.nih.gov/39073169/)

**Genetic risk factors.** The sole established genetic risk factor is **hemizygosity for a pathogenic *SRPK3* variant in males**. Because the gene is X-linked, male sex is the principal demographic risk determinant; carrier females are generally unaffected or mildly/variably affected (X-inactivation dependent). No modifier genes or susceptibility loci have been established.

**Environmental risk factors.** None identified. This is a fully penetrant-appearing Mendelian disorder in hemizygous males; no toxic, infectious, occupational, or lifestyle exposures are implicated in causation.

**Protective factors.** No genetic or environmental protective factors are described. In principle, favorable (skewed) X-inactivation could protect heterozygous female carriers, but this has not been formally documented for XLID114.

**Gene–environment interactions.** None reported; not applicable given monogenic X-linked recessive etiology.

---

## 3. Phenotypes

The core phenotype derives from the 8 postnatally ascertained patients:

> *"The 8 patients ascertained postnatally shared common clinical features including intellectual disability, agenesis of the corpus callosum, abnormal eye movement, and ataxia"* — [PMID: 39073169](https://pubmed.ncbi.nlm.nih.gov/39073169/)

| Phenotype | HPO term | Type | Onset | Frequency (cohort) | Notes |
|---|---|---|---|---|---|
| Intellectual disability | HP:0001249 | Behavioral/cognitive | Congenital/infancy | Core (8/8 postnatal) | Central feature |
| Agenesis of corpus callosum | HP:0001274 | Structural/imaging sign | Congenital | Core (8/8 postnatal) | Midline brain malformation |
| Abnormal eye movement | HP:0000496 | Clinical sign | Infancy/childhood | Core | "Uncontrolled ocular movement" |
| Ataxia | HP:0001251 | Clinical sign | Childhood | Core | Coordination deficit |
| Cerebellar atrophy | HP:0001272 | Imaging sign | Childhood | Frequent | Matches gene expression |
| Motor incoordination / clumsiness | HP:0002317 | Sign | Childhood | Reported | Modeled by zebrafish |
| Complex structural brain malformation | — | Imaging sign | Prenatal | 1/9 (prenatal case) | More severe presentation |

**Characteristics.** Onset is **congenital/early childhood**; severity is **moderate to severe** for cognition; course is **static (non-progressive)**, consistent with a neurodevelopmental rather than neurodegenerative disorder. Quality-of-life impact is substantial: the combination of intellectual disability, ataxia, and ocular-motor dysfunction impairs independent daily functioning, mobility, and communication lifelong. Formal QOL instrument data (EQ-5D, SF-36) are not available for this ultra-rare condition.

---

## 4. Genetic / Molecular Information

**Causal gene.** *SRPK3* (SRSF protein kinase 3), NCBI Gene 26576, MIM 301002, HGNC:11402, Ensembl ENSG00000184343, UniProt Q9UPE1, RefSeq NM_014370.4/NP_055185.2 (isoform 1, 567 aa). Located at **Xq28**. Mouse ortholog *Srpk3* (GeneID 56504).

**Pathogenic variants (defining cohort).**

| cDNA | Protein | Type | Domain location |
|---|---|---|---|
| c.475C>G | p.His159Asp (H159D) | Missense | Kinase domain, N-lobe |
| c.953C>T | p.Ser318Leu (S318L) | Missense | Disordered spacer insert (298–351) |
| c.1373C>A | p.Thr458Asn (T458N) | Missense | Kinase domain, C-lobe |
| c.1585G>A | p.Glu529Lys (E529K) | Missense | Kinase domain, C-lobe |
| c.1413_1414del | p.Tyr471* (Y471*) | Truncating | C-lobe (removes ~96 C-terminal residues) |

**Variant localization to the kinase domain.** Mapping onto UniProt Q9UPE1 shows SRPK3 has a single large protein-kinase domain (residues 79–565), with the catalytic active site (proton acceptor) at Asp212, a glycine-rich ATP-binding loop (aa 85–93) and ATP-binding Lys108, and disordered spacer-insert regions at aa 238–283 and 298–351. **All five variants fall within the kinase domain or its spacer insert**, providing strong structural support for a kinase-impairment mechanism (Finding F005). Specifically: p.H159D lies in the N-lobe near the ATP-binding apparatus; p.S318L within the disordered spacer insert (298–351) that interrupts the SRPK bipartite kinase domain; p.T458N and p.E529K in the C-lobe; and p.Y471* truncates the C-lobe (removing residues through 565).

**Variant classification.** Per the founding study, these were reported as disease-causing (segregating hemizygous variants). In **ClinVar (Sep 2026)**, among SRPK3 SNV/indels the classifications are **26 VUS, 1 Likely pathogenic, 3 Likely benign, 1 Benign** (large "Pathogenic" entries are multigene Xq CNVs, not point mutations). This reflects the recency of the gene–disease association and limited independent curation.

**Allele frequency / constraint.** gnomAD v2.1.1 constraint for SRPK3: observed 26 vs expected 45.3 LoF variants, **oe_lof = 0.57 (90% CI 0.42–0.80)**, lof_z = 2.44, **pLI ≈ 0.00005** — indicating **modest, incomplete LoF intolerance**. This is consistent with X-linked recessive inheritance, where the phenotypic burden falls on hemizygous males and heterozygous female LoF carriers are largely tolerated in the population.

**Functional consequence.** **Loss of function / kinase impairment.** The truncation (p.Y471*) removes C-lobe residues; missense variants cluster in catalytic/regulatory regions. The zebrafish knockout phenocopy confirms LoF as the operative mechanism.

**Modifier genes / epigenetics / chromosomal abnormalities.** None specifically established for XLID114. Large Xq28 CNVs spanning *SRPK3* exist in ClinVar but represent contiguous-gene events rather than isolated XLID114.

---

## 5. Environmental Information

**Not applicable.** XLID114 is a monogenic X-linked recessive disorder with no established environmental, lifestyle, or infectious contributors. No toxins, radiation, pollution, occupational exposures, dietary factors, or pathogens have been implicated in causation or triggering.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A hemizygous **loss-of-function or kinase-impairing variant in *SRPK3*** (missense in the kinase domain, or C-lobe truncation p.Y471*) **leads to** reduced or absent SRPK3 serine kinase activity in affected male cells.
2. Loss of SRPK3 activity **results in** deficient phosphorylation of the arginine/serine (RS) domains of **SR splicing factors** (e.g., SRSF1/ASF/SF2, SRSF4/5/6) — *inferred from SRPK-family biochemistry and the SRPK3 interactome, not yet directly demonstrated in patient neurons*.
3. Hypophosphorylation of SR proteins **leads to** impaired spliceosome assembly and altered nuclear trafficking/localization of splicing factors, **resulting in** dysregulated pre-mRNA splicing of downstream neurodevelopmental transcripts (*inferred*).
4. Aberrant splicing during CNS development **results in** defective midline and cerebellar neurodevelopment — the branch point where the phenotype diverges into (a) **agenesis of the corpus callosum**, (b) **cerebellar hypoplasia/atrophy → ataxia and ocular-motor dysfunction**, and (c) **impaired cortical/cognitive development → intellectual disability**.
5. These developmental lesions **manifest clinically as** the XLID114 tetrad (ID, ACC, abnormal eye movements, ataxia), established in infancy/childhood and static thereafter.

```
SRPK3 kinase-domain variant (LoF)
        │  leads to
        ▼
↓ SRPK3 serine-kinase activity
        │  results in
        ▼
↓ phosphorylation of SR proteins (SRSF1/4/5/6)   [inferred]
        │  results in
        ▼
impaired spliceosome assembly / SR-protein trafficking
        │  results in
        ▼
dysregulated pre-mRNA splicing in neurodevelopment
        │  branches
        ├──▶ corpus callosum agenesis
        ├──▶ cerebellar hypoplasia ──▶ ataxia + abnormal eye movements
        └──▶ cortical dysfunction ──▶ intellectual disability
```

### Molecular detail

**Molecular pathway — pre-mRNA splicing.** SRPK3 belongs to the SRPK family of SR-protein-specific kinases that phosphorylate RS domains, controlling spliceosome assembly and splicing-factor trafficking:

> *"These observations likely reflect the function of the SRPK family of kinases in spliceosome assembly and in mediating the trafficking of splicing factors in mammalian cells"* — [PMID: 9472028](https://pubmed.ncbi.nlm.nih.gov/9472028/)

Within the SRPK family, tissue-differential expression is well established — *"SRPK1 is highly expressed in pancreas, whereas SRPK2 is highly expressed in brain"* ([PMID: 9472028](https://pubmed.ncbi.nlm.nih.gov/9472028/)). The family phosphorylates RS domains processively and with high regiospecificity, as shown for the prototypical SR protein ASF/SF2 ([PMID: 14555757](https://pubmed.ncbi.nlm.nih.gov/14555757/), [PMID: 19477182](https://pubmed.ncbi.nlm.nih.gov/19477182/), [PMID: 16223727](https://pubmed.ncbi.nlm.nih.gov/16223727/)).

**Interactome confirmation.** STRING (v12) top functional partners of SRPK3 are dominated by splicing machinery: CDC5L (0.80), SRSF6 (0.74), SRSF5 (0.71), SRSF4 (0.71), U2AF2 (0.63), SRSF1 (0.62), SNRNP70/U1-70K (0.61), RBM39 (0.55), PRPF4B (0.53), SNRPA/U1A (0.51), SON (0.50), HNRNPM (0.49), SRPK1 (0.47) — i.e., **SR splicing-factor substrates, core spliceosomal proteins, splicing regulators, and paralogous kinases** (Finding F007). This triangulates the splicing mechanism independently of the biochemistry literature.

**Tissue specificity.** Within the CNS, SRPK3 is **cerebellum-enriched** (GTEx v8: cerebellum ~21 TPM, cerebellar hemisphere ~17.7 TPM vs cortex ~3.5 TPM, hippocampus 2.4, basal ganglia ~1.9) (Finding F006). This regional bias correlates with the cerebellar-predominant phenotype (ataxia, cerebellar atrophy, ocular-motor dysfunction). SRPK3 is also highly expressed in skeletal muscle (~44 TPM), consistent with its original characterization as MSSK1, a MEF2-regulated muscle kinase.

**GO / CL / UBERON suggestions.**
- Biological process: mRNA splicing via spliceosome (GO:0000398), spliceosomal complex assembly (GO:0000245), regulation of mRNA processing (GO:0050684), protein phosphorylation (GO:0006468), muscle tissue development (GO:0060537).
- Molecular function: protein serine kinase activity (GO:0106310), protein serine/threonine kinase activity (GO:0004674), ATP binding (GO:0005524).
- Cellular component: nucleus (GO:0005634), cytoplasm (GO:0005737), nuclear speck (GO:0016607).
- Cell types: cerebellar Purkinje cell (CL:0000121), granule cell (CL:0000120), neuron (CL:0000540).
- Anatomy: cerebellum (UBERON:0002037), corpus callosum (UBERON:0002336).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ affected: **brain** (CNS, UBERON:0000955), body system: **nervous system** (UBERON:0001016). Specific structures: **cerebellum** (UBERON:0002037), **corpus callosum** (UBERON:0002336, agenesis), and cerebral cortex (cognitive impairment). The **oculomotor system** is affected functionally (abnormal eye movements). Given high muscle expression, skeletal muscle is a plausible secondary site, but no myopathy is prominent in the human phenotype.

**Tissue/cell level.** Affected tissue is **nervous tissue**; likely cell populations are **cerebellar neurons** (Purkinje cells CL:0000121, granule cells CL:0000120) and cortical/callosal projection neurons. Direct histopathology in patients has not been reported.

**Subcellular level.** SRPK3 localizes to the **nucleus** (GO:0005634) and **cytoplasm** (GO:0005737); its splicing function operates in nuclear speckles (GO:0016607).

**Localization / lateralization.** Brain malformations are **midline (corpus callosum) and bilateral (cerebellum)**.

---

## 8. Temporal Development

- **Onset:** **Congenital / early childhood.** Brain malformations (ACC, cerebellar hypoplasia) are established prenatally; one case was ascertained prenatally with complex structural anomalies.
- **Onset pattern:** Chronic/insidious neurodevelopmental — deficits become apparent as developmental milestones are missed.
- **Progression:** **Static (non-progressive).** The disorder is a fixed developmental encephalopathy; cerebellar "atrophy" reflects hypoplasia/maldevelopment rather than progressive neurodegeneration.
- **Course/duration:** **Chronic, lifelong.**
- **Remission:** None; no spontaneous or treatment-induced remission.
- **Critical period:** Prenatal/early postnatal brain development is the window of vulnerability; there is no established intervention window to reverse the developmental lesion.

---

## 9. Inheritance and Population

- **Inheritance:** **X-linked recessive.** Affected individuals are hemizygous males; the founding cohort was 9 males from 5 families. Carrier mothers are typically unaffected.
- **Epidemiology:** **Ultra-rare.** No prevalence or incidence estimates exist; described in only 9 individuals worldwide as of 2024. Not listed with an Orphanet prevalence class.
- **Penetrance:** Appears **high/complete in hemizygous males** based on the reported families, though systematic penetrance data are lacking given the small cohort.
- **Expressivity:** **Variable** — from the core postnatal tetrad to a severe prenatal structural phenotype.
- **Sex ratio:** Strongly **male-predominant** (X-linked recessive); carrier females largely spared.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity / germline mosaicism:** None established. gnomAD shows no common founder LoF allele; carrier frequency is not defined but expected to be very low.
- **Population demographics / geographic distribution:** No ethnic or geographic clustering reported; the 5 families were unrelated.

---

## 10. Diagnostics

**Genetic testing is the diagnostic cornerstone.** Because XLID114 lacks a specific biochemical marker, molecular diagnosis relies on identifying a hemizygous pathogenic *SRPK3* variant.

| Modality | Utility for XLID114 |
|---|---|
| Whole-exome sequencing (WES) | **High** — primary route to diagnosis; how the founding cohort was identified |
| Whole-genome sequencing (WGS) | High — detects variants missed by WES, including non-coding/structural |
| Multigene ID/XLID panel | Useful if *SRPK3* is included (recently added) |
| Single-gene *SRPK3* testing | Appropriate for cascade testing once a familial variant is known |
| Chromosomal microarray (CMA) | Detects Xq28 CNVs involving *SRPK3*; normal in point-mutation cases |
| Karyotype / FISH | Low yield for point mutations |

**Imaging.** **Brain MRI** is central to phenotyping: demonstrates **agenesis of the corpus callosum** and **cerebellar atrophy/hypoplasia**. Ophthalmologic/neurologic exam documents abnormal eye movements and ataxia.

**Laboratory tests / biomarkers / omics.** No specific blood, urine, enzyme, metabolomic, or proteomic biomarker is available. RNA-sequencing to detect a splicing signature is a plausible future functional/diagnostic assay but is not yet validated.

**Clinical criteria / differential diagnosis.** Diagnosis is genetic; differential diagnosis includes other X-linked and autosomal causes of syndromic ID with **corpus callosum agenesis and cerebellar involvement** (e.g., other XLID genes, ACC syndromes, congenital ataxias with ocular-motor apraxia). Molecular confirmation distinguishes XLID114.

**Screening.** No newborn or population screening exists. Carrier and cascade testing within affected families is appropriate.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No survival data; the disorder is **not reported to shorten lifespan** directly, though severe cases with complex brain malformations may carry higher morbidity. Life expectancy is presumed near-normal for the milder core phenotype but is undetermined.
- **Morbidity/function:** Substantial lifelong **disability** from intellectual impairment, ataxia, and ocular-motor dysfunction — affecting mobility, communication, education, and independence.
- **Disease course:** **Static** developmental disorder; complications relate to disability (e.g., feeding, mobility, communication support needs).
- **Recovery potential:** No reversal of the neurodevelopmental lesion; supportive interventions can improve function.
- **Prognostic factors:** Severity of structural brain malformation appears to correlate with outcome (the prenatal complex-malformation case being most severe). No validated prognostic biomarkers.

---

## 12. Treatment

**No disease-specific or curative therapy exists.** Management is **supportive and multidisciplinary**:

- **Developmental/rehabilitative:** early-intervention programs, physical therapy (ataxia/gait), occupational therapy, and speech-language therapy for cognitive/communication support. (NCIT: rehabilitation therapy, physical therapy, occupational therapy, speech therapy.)
- **Neurologic/ophthalmologic care:** management of eye-movement abnormalities and any seizures; regular developmental follow-up.
- **Educational and social support:** special education and family support services.
- **Genetic counseling:** essential for the family (X-linked recessive recurrence risk).

**Pharmacotherapy:** none targeted; symptomatic only (e.g., antiepileptics if seizures occur). No pharmacogenomic considerations are specific to XLID114.

**Advanced/experimental therapeutics:** No gene, cell, or RNA-based therapies are in development. Because the defect involves a splicing kinase acting during development, and the lesion is largely established prenatally, therapeutic reversal is a formidable challenge. No registered clinical trials (ClinicalTrials.gov) target XLID114.

---

## 13. Prevention

- **Primary prevention:** Not possible for the genetic cause. **Genetic counseling** and **reproductive options** (prenatal diagnosis, preimplantation genetic testing) for families with a known *SRPK3* variant are the principal preventive measures.
- **Secondary prevention:** Early diagnosis via WES/WGS enables early intervention services to optimize developmental outcomes.
- **Tertiary prevention:** Multidisciplinary management to prevent complications of disability (contractures, aspiration, injury from ataxia).
- **Screening/counseling:** Carrier testing of at-risk female relatives; cascade testing. No population/newborn screening.
- **Immunization / public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *SRPK3* (NCBI Gene 26576) has a **mouse ortholog *Srpk3*** (GeneID 56504) and a **zebrafish ortholog *srpk3***. The SRPK family is evolutionarily conserved across metazoans and plants (Arabidopsis SRPK family, [PMID: 36273172](https://pubmed.ncbi.nlm.nih.gov/36273172/)), reflecting the deep conservation of RS-domain phosphorylation in splicing regulation.
- **Natural disease in other species:** No naturally occurring XLID114-equivalent disease is documented in companion animals or wildlife (no OMIA entry). *SRPK3* (MSSK1) in mouse was originally characterized as a MEF2-regulated muscle kinase with a role in muscle development.
- **Comparative biology:** The conservation of SRPK-mediated splicing control means mechanistic insights are transferable across species, underpinning the utility of the zebrafish model below.

---

## 15. Model Organisms

**Zebrafish (*Danio rerio*) srpk3 knockout** is the validated disease model (Roychaudhury et al. 2024):

> *"KO zebrafish exhibited severe deficits in eye movement and swim bladder inflation, mimicking uncontrolled ocular movement and physical clumsiness observed in human patients"* — [PMID: 39073169](https://pubmed.ncbi.nlm.nih.gov/39073169/)

> *"In adult KO zebrafish, cerebellar agenesis and behavioral abnormalities were observed, recapitulating human phenotypes of cerebellar atrophy and intellectual disability"* — [PMID: 39073169](https://pubmed.ncbi.nlm.nih.gov/39073169/)

| Model feature | Human counterpart | Recapitulation |
|---|---|---|
| Eye-movement deficits (larvae) | Abnormal/uncontrolled eye movements | Strong |
| Failed swim-bladder inflation | Physical clumsiness/incoordination | Analogous |
| Cerebellar agenesis (adult) | Cerebellar atrophy | Strong |
| Behavioral abnormalities (adult) | Intellectual disability | Analogous |

**Model type:** Vertebrate genetic knockout. **Strengths:** recapitulates ocular-motor, cerebellar, and behavioral domains, establishing causality. **Limitations:** zebrafish cannot fully model human corpus callosum agenesis (no corpus callosum) or the nuances of human cognition; splicing-target readouts in patient-relevant neurons remain to be defined. A **mouse *Srpk3* knockout** exists historically (muscle context) and could be re-examined for CNS phenotypes. Patient-derived iPSC neurons/cerebellar organoids are logical future models (not yet reported).

---

## Mechanistic Model / Interpretation

XLID114 is best understood as a **"splicing-kinase" neurodevelopmental disorder**. The unifying model, supported by four independent evidence streams, is:

```
GENETICS            STRUCTURE              EXPRESSION            INTERACTOME
5 variants   ──►  all in SRPK3      ──►  cerebellum-      ──►  SR proteins +
in SRPK3          kinase domain          enriched (GTEx)       spliceosome (STRING)
   │                    │                     │                     │
   └──────── converge on: loss of SRPK3 kinase activity ───────────┘
                              │
                              ▼
          dysregulated SR-protein phosphorylation & pre-mRNA splicing
                              │
                              ▼
        cerebellar + midline (callosal) + cortical maldevelopment
                              │
                              ▼
            ID + ACC + abnormal eye movements + ataxia (XLID114)
   (validated in srpk3-KO zebrafish: eye movement, cerebellar agenesis, behavior)
```

The **cerebellar enrichment of SRPK3 among CNS regions** is the most elegant genotype–phenotype link uncovered here: it provides a tissue-level explanation for why a broadly-expressed splicing kinase produces a **cerebellar-predominant** neurological syndrome (ataxia, cerebellar atrophy, ocular-motor dysfunction). The convergence of all five variants on the kinase domain, and the SR-protein/spliceosome-dominated interactome, together make the loss-of-kinase-function → aberrant-splicing mechanism the most parsimonious explanation, even though the specific mis-spliced neurodevelopmental targets have not yet been experimentally enumerated in human neurons.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [39073169](https://pubmed.ncbi.nlm.nih.gov/39073169/) | *SRPK3 Is Essential for Cognitive and Ocular Development in Humans and Zebrafish* | **Defining study** — variants, cohort phenotype, zebrafish validation |
| [9472028](https://pubmed.ncbi.nlm.nih.gov/9472028/) | *SRPK2: SR protein-specific kinase...spliceosome assembly and localization* | Establishes SRPK-family molecular function; brain-enriched paralog |
| [14555757](https://pubmed.ncbi.nlm.nih.gov/14555757/) | *Processive phosphorylation of ASF/SF2* | SRPK catalytic mechanism on SR proteins |
| [19477182](https://pubmed.ncbi.nlm.nih.gov/19477182/) | *Regiospecific phosphorylation of ASF/SF2 by SRPK1* | RS-domain phosphorylation specificity |
| [16223727](https://pubmed.ncbi.nlm.nih.gov/16223727/) | *MS/kinetic analysis of ASF/SF2 phosphorylation* | SRPK vs Clk phosphorylation of SR proteins |
| [36273172](https://pubmed.ncbi.nlm.nih.gov/36273172/) | *Arabidopsis splicing-related protein kinase families* | Evolutionary conservation of SRPK splicing role |

The founding paper (PMID 39073169) supplies the human genetics, phenotype, and animal-model validation. The SRPK-family biochemistry papers supply the mechanistic underpinning (RS-domain phosphorylation → spliceosome control) that this report extends to SRPK3 via the STRING interactome and GTEx/UniProt analyses generated during the investigation. No paper in the corpus contradicts the loss-of-function splicing mechanism.

---

## Limitations and Knowledge Gaps

1. **Single small cohort (n=9).** All human clinical data derive from one 2024 study; prevalence, penetrance, expressivity, and natural history are therefore preliminary.
2. **Mechanism partly inferred.** The step from reduced SRPK3 kinase activity to specific mis-spliced neurodevelopmental transcripts is **inferred from family biochemistry and the interactome, not directly demonstrated** in patient neurons. No patient RNA-seq splicing signature has been published.
3. **ClinVar classification lag.** Most *SRPK3* variants remain VUS; only 1 is Likely pathogenic. Independent replication cohorts are needed.
4. **Constraint is modest.** gnomAD LOEUF upper bound 0.80 / pLI≈0 indicates the gene is not strongly LoF-constrained at the population level — consistent with X-linked recessive biology but meaning LoF alone does not automatically prove pathogenicity for a given variant.
5. **Model gaps.** Zebrafish cannot model corpus callosum agenesis; no mouse CNS model or patient iPSC model has been reported.
6. **No therapeutics or trials.** Prognosis, QOL metrics, and treatment-response data are absent.

---

## Proposed Follow-up Experiments / Actions

1. **Patient/model transcriptomics:** RNA-seq of patient-derived cells or srpk3-mutant neurons to define the **aberrant splicing signature** and identify the neurodevelopmental target transcripts (validates causal chain steps 3–4).
2. **iPSC-derived cerebellar organoids** from patients to model the cerebellum-predominant phenotype and test splicing rescue.
3. **Structural/biochemical assays** of the four missense variants (H159D, S318L, T458N, E529K) to quantify residual kinase activity and confirm loss-of-function vs dominant-negative behavior.
4. **International case-finding** (GeneMatcher, DECIPHER) to expand the cohort, refine penetrance/expressivity, and reclassify VUS toward pathogenic.
5. **Female carrier studies** with X-inactivation analysis to assess carrier phenotype risk.
6. **Mouse conditional CNS knockout** to model cortical/callosal features not captured in zebrafish.
7. **Curation actions:** Submit the functional/computational evidence (kinase-domain clustering, cerebellar enrichment, SR-protein interactome) to ClinVar/ClinGen to support variant reclassification.


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_X-linked_114-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_X-linked_114-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 14 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0975828` (2 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder, X-linked 114**
- `HP:0002317` (1 mention) - the report calls it "Motor incoordination / clumsiness"; HP calls it **Unsteady gait**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0000398` (1 mention) - the report calls it "Biological process: mRNA splicing via spliceosome"; GO calls it **mRNA splicing, via spliceosome**, and lists "nuclear mRNA splicing, via spliceosome" among its other names
- `GO:0106310` (1 mention) - the report calls it "Molecular function: protein serine kinase activity"; GO calls it **protein serine kinase activity**
- `GO:0005634` (2 mentions) - the report calls it "Cellular component: nucleus", "nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `CL:0000121` (2 mentions) - the report calls it "Cell types: cerebellar Purkinje cell"; CL calls it **Purkinje cell**, and lists "cerebellar Purkinje cell" among its other names
- `UBERON:0002037` (2 mentions) - the report calls it "Anatomy: cerebellum", "cerebellum"; UBERON calls it **cerebellum**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "Cellular component: nucleus", "nucleus"
- `UBERON:0002037` - called "Anatomy: cerebellum", "cerebellum"