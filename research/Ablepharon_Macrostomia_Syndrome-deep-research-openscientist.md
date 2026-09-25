---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T13:56:41.628706'
end_time: '2026-09-25T14:44:38.020257'
duration_seconds: 2876.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ablepharon-Macrostomia Syndrome
  mondo_id: MONDO:0008693
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 25
  on_topic: 15
  off_topic: 2
  off_topic_references:
  - PMID:20980404
  - PMID:19609939
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 48
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 6
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0008693
    reported_labels:
    - MONDO
    ontology_label: ablepharon macrostomia syndrome
  - term_id: HP:0011500
    reported_labels:
    - Ablepharon
    ontology_label: Polycoria
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ablepharon_Macrostomia_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ablepharon_Macrostomia_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ablepharon-Macrostomia Syndrome
- **MONDO ID:** MONDO:0008693 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ablepharon-Macrostomia Syndrome** covering all of the
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

# Ablepharon-Macrostomia Syndrome (AMS): Comprehensive Disease Characteristics Report

**Disease:** Ablepharon-Macrostomia Syndrome
**MONDO ID:** MONDO:0008693
**OMIM:** #200110
**Category:** Mendelian (autosomal dominant, de novo)
**Causal gene:** *TWIST2* (a.k.a. *DERMO1*), HGNC:20670, chromosome 2q37.3

---

## Summary

Ablepharon-Macrostomia Syndrome (AMS) is an ultra-rare congenital ectodermal dysplasia (fewer than ~20 well-documented cases worldwide since its first description in 1977) defined by a nearly pathognomonic combination of **ablepharon** (absent or severely foreshortened eyelids with anterior-lamellar dysgenesis) and **macrostomia** (an abnormally wide, "fish-shaped" mouth), accompanied by absent eyebrows/eyelashes, external-ear malformations, malar/zygomatic hypoplasia, sparse hair/alopecia, dry ichthyotic redundant skin, rudimentary nipples, and ambiguous or abnormal genitalia. The disorder is caused by a **recurrent de novo heterozygous missense mutation in *TWIST2*, c.223G>A (p.Glu75Lys / E75K)**, located in the basic DNA-binding domain of this basic helix-loop-helix (bHLH) transcription factor ([PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/)). Remarkably, mutation of the *same* codon to glutamine or alanine (E75Q/E75A) produces the allelic **Barber-Say syndrome (BSS)** rather than AMS, one of the cleanest genotype–phenotype correlations in dysmorphology.

Mechanistically, the E75K substitution does not eliminate the protein (that would cause a different, recessive disease — Setleis syndrome); instead it **alters the DNA-binding specificity** of TWIST2, producing a dominant antimorphic/neomorphic effect that dysregulates the Wnt-downstream **TWIST2/DERMO1 mesenchymal transcriptional program** that governs dermal, craniofacial, and skin-appendage development. The result is faulty specification and differentiation of cranial-neural-crest- and mesoderm-derived mesenchymal progenitors, producing the characteristic eyelid, malar, ear, skin, and genital defects. The disorder is faithfully modeled in **zebrafish** (a base-edited *twist2* p.E78K knock-in) and in ***C. elegans*** (an allelic series engineered into the single Twist homolog *hlh-8*).

There is **no disease-modifying pharmacologic or gene therapy**. Management is multidisciplinary, supportive, and surgical: **urgent neonatal corneal protection** (intensive lubrication, masquerade flaps) to prevent exposure keratopathy and blindness, followed by **staged anterior-lamellar eyelid reconstruction** (e.g., full-thickness skin grafts over the Müller-muscle/conjunctiva complex, rib-cartilage/fat grafting, reverse hatchet flaps), plus reconstructive surgery for macrostomia, ear, skin, and genital anomalies. Cognition and lifespan are generally normal; the major morbidity is ophthalmic. Both sexes are affected, there is no known population/founder enrichment, and there is no known non-genetic (environmental, infectious, lifestyle) contribution or prevention beyond genetic counseling.

---

## 1. Disease Information

**Overview.** AMS is an extremely rare congenital malformation syndrome of ectoderm- and mesenchyme-derived structures. It is characterized by absent/short eyelids (ablepharon), a wide fish-shaped mouth (macrostomia), external ear abnormalities, absent eyebrows/eyelashes, and a range of skin, skeletal, and genital anomalies ([PMID: 15103726](https://pubmed.ncbi.nlm.nih.gov/15103726/)). It was first described by McCarthy and West in 1977.

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008693 |
| OMIM | #200110 (Ablepharon-Macrostomia Syndrome) |
| Orphanet | ORPHA:920 |
| MeSH | Ablepharon macrostomia syndrome (within "Ectodermal Dysplasia" tree) |
| Gene | *TWIST2* / *DERMO1*, HGNC:20670, NCBI Gene 117581 |
| ICD-10 | Q18.8 / Q10.3 (other congenital malformations of face/eyelid) — no specific code |
| ICD-11 | LD2F.1Y (other specified developmental anomalies) — no dedicated code |

**Synonyms / alternative names.** Ablepharon-macrostomia syndrome; AMS. It is closely related to (and allelic with) **Barber-Say syndrome (BSS)**, and both belong to the *TWIST2*-related craniofacial/ectodermal dysplasia spectrum.

**Data provenance.** The disease-level knowledge base for AMS is derived almost entirely from **aggregated case reports and small case series** (individual patients described in the published literature) plus functional/molecular studies, rather than from large EHR cohorts or registries. Given fewer than ~20 reported cases, all epidemiologic and clinical statements are based on this aggregated case literature.

---

## 2. Etiology

**Disease causal factors — genetic.** AMS is a monogenic Mendelian disorder. The primary and essentially sole cause is a **de novo heterozygous missense mutation in *TWIST2***, specifically **c.223G>A, p.Glu75Lys (E75K)** in the basic DNA-binding domain ([PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/); [PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/)). Inheritance is autosomal dominant; most cases are sporadic (de novo), with rare familial transmission and rare mosaic cases.

**Genetic risk factors.** The single causal variant *is* the risk factor. There are no known susceptibility loci or modifier genes established for AMS beyond the allelic-series relationship at codon 75 that determines AMS vs BSS. No GWAS/polygenic contribution applies to this Mendelian condition.

**Environmental risk factors.** **None identified.** No toxins, teratogens, infections, parental age effects, occupational exposures, diet, or lifestyle factors have been implicated. The de novo mutations arise spontaneously.

**Protective factors.** **None identified** (neither genetic protective alleles nor environmental/dietary protective exposures are described for this single-gene disorder).

**Gene–environment interactions.** **Not applicable / none reported.** AMS is a fully penetrant consequence of the causal genotype; there is no evidence of environmental modulation.

---

## 3. Phenotypes

AMS phenotypes are **congenital (present at birth)**, **non-progressive/stable** structural malformations (the ophthalmic complications, however, can progress if untreated), and highly **consistent** across reported patients for the two cardinal features. Frequencies below are qualitative given the tiny case literature.

| Phenotype | Type | HPO term (suggested) | Onset | Frequency | Notes |
|---|---|---|---|---|---|
| Ablepharon / absent or short eyelids (anterior-lamellar dysgenesis) | Physical/structural | HP:0011500 (Ablepharon) | Congenital | Cardinal (~100%; "absent" lids in ~60% of reports) | Sight-threatening; anterior lamella specifically deficient ([PMID: 34092176](https://pubmed.ncbi.nlm.nih.gov/34092176/)) |
| Macrostomia (wide fish-shaped mouth) | Physical/structural | HP:0000154 (Macrostomia) | Congenital | Cardinal (~100%) | |
| Absent eyebrows and eyelashes | Physical | HP:0002223 (Absent eyebrow); HP:0000561 (Absent eyelashes) | Congenital | Very frequent | |
| External ear abnormalities / dysplastic ears | Physical | HP:0000356 (Abnormal outer ear morphology) | Congenital | Frequent | |
| Malar/zygomatic hypoplasia; zygomatic-arch absence | Skeletal | HP:0000272 (Malar flattening) | Congenital | Frequent | Zygomatic arch absence reported ([PMID: 3293678](https://pubmed.ncbi.nlm.nih.gov/3293678/)) |
| Alopecia / sparse hair; absent lanugo | Ectodermal | HP:0001596 (Alopecia); HP:0008070 (Sparse hair) | Congenital | Frequent | |
| Dry, ichthyotic, redundant skin | Ectodermal/skin | HP:0008064 (Ichthyosis); HP:0001582 (Redundant skin) | Congenital | Frequent | |
| Rudimentary/absent nipples | Physical | HP:0002557 (Rudimentary/absent nipples) | Congenital | Reported | |
| Ambiguous / abnormal genitalia (e.g., absent prepuce) | Physical | HP:0000078 (Abnormality of the genital system) | Congenital | Frequent in both sexes | Absent prepuce reported ([PMID: 34850759](https://pubmed.ncbi.nlm.nih.gov/34850759/)) |
| Hypertelorism | Physical | HP:0000316 (Hypertelorism) | Congenital | Reported ([PMID: 33055564](https://pubmed.ncbi.nlm.nih.gov/33055564/)) | |
| Exposure keratopathy / corneal ulceration → vision loss | Ophthalmic complication (secondary) | HP:0000508 / HP:0000481 | Neonatal onset, progressive if untreated | Major morbidity | Preventable with early intervention ([PMID: 38967579](https://pubmed.ncbi.nlm.nih.gov/38967579/)) |
| Laryngo-tracheal malacia / stenosis | Visceral (rare) | HP:0001601 (Laryngomalacia) | Variable | Rare | First stenosis case: [PMID: 31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/) |

**Canonical description (F003):** *"AMS is characterized by absent or short eyelids, absent eyebrows and eyelashes, macrostomia, and external ear abnormalities. Additional features include alopecia or sparse hair, hypoplastic malar region, redundant skin, rudimentary nipples, abnormal genitalia"* ([PMID: 15103726](https://pubmed.ncbi.nlm.nih.gov/15103726/)).

**Severity/expressivity.** Variable; **mosaic *TWIST2* expression yields a milder phenotype**, with anterior-lamella abnormality remaining a common feature ([PMID: 34092176](https://pubmed.ncbi.nlm.nih.gov/34092176/)).

**Quality-of-life impact.** The dominant QoL burden is **ophthalmic** — the eyelid defect causes lagophthalmos and exposure keratopathy that, untreated, leads to corneal ulceration and blindness ([PMID: 38967579](https://pubmed.ncbi.nlm.nih.gov/38967579/)). Facial dysmorphism (macrostomia, ear, malar) carries psychosocial and functional (feeding, speech) impact requiring multidisciplinary reconstruction ([PMID: 33689605](https://pubmed.ncbi.nlm.nih.gov/33689605/)). Cognition is generally normal. A patient's-view account underscores the lived experience of AMS/BSS ([PMID: 28690482](https://pubmed.ncbi.nlm.nih.gov/28690482/)). No standardized EQ-5D/SF-36 QoL data exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***TWIST2*** (also **DERMO1**), a bHLH transcription factor gene on chromosome **2q37.3** (HGNC:20670; OMIM *607556). UniProt Q8WVJ9.

**Pathogenic variant.**
- **AMS-specific variant:** **c.223G>A, p.Glu75Lys (E75K)** — a **missense** change in the **basic DNA-binding domain** ([PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/)).
- **Classification:** Pathogenic (recurrent de novo, robust genotype–phenotype correlation, functional evidence) per ACMG/AMP criteria (PS2, PS1/PM5 at codon, PM1 in critical domain, PP3).
- **Allele frequency:** Absent from population databases (gnomAD) — de novo, not a population polymorphism.
- **Origin:** **Germline de novo** (germline/somatic mosaicism described in rare milder cases, [PMID: 34092176](https://pubmed.ncbi.nlm.nih.gov/34092176/)). Not somatic/cancer-associated.
- **Functional consequence:** **Altered DNA binding** — a **dominant antimorphic/neomorphic** effect, *not* simple loss of function or haploinsufficiency. *"All identified mutations fell in the basic domain of TWIST2 and altered the DNA-binding pattern of Flag-TWIST2 in HeLa cells"* ([PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/)); basic-domain substitutions *"exert antimorphic effects"* ([PMID: 30450715](https://pubmed.ncbi.nlm.nih.gov/30450715/)).

**The TWIST2 allelic series (F002)** — a key organizing principle:

| Variant | Residue | Disease | Inheritance | Mechanism |
|---|---|---|---|---|
| *TWIST2* p.Glu75**Lys** | E75 (basic domain) | **AMS** (this disease) | AD, de novo | Altered DNA binding (antimorph) |
| *TWIST2* p.Glu75**Gln / Ala** | E75 (basic domain) | **Barber-Say syndrome** | AD, de novo | Altered DNA binding (antimorph) |
| *TWIST2* biallelic **loss-of-function** | — | **Setleis syndrome / FFDD3** (MIM#227260) | **AR** | Loss of function |
| *TWIST1* p.Glu117 (paralogous residue) | basic domain | **Sweeney-Cox syndrome** | AD | Altered DNA binding |
| *TWIST1* **haploinsufficiency** | — | **Saethre-Chotzen syndrome** | AD | Loss of function (+ craniosynostosis) |

*"a lysine at TWIST2 residue 75 resulted in AMS, whereas a glutamine or alanine yielded BSS"* ([PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/)). *"subjects with Barber-Say and Ablepharon-Macrostomia syndromes were found to harbor heterozygous missense substitutions in the paralogous glutamic acid residue in TWIST2 (p.Glu75Ala, p.Glu75Gln and p.Glu75Lys)"* and *"This allelic series revealed that different substitutions exhibit graded severity, in terms of both gene expression and cellular phenotype"* ([PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/)). *"Setleis syndrome (SS), or focal facial dermal dysplasia type III (FFDD3, MIM #227260), is an autosomal recessive condition caused by biallelic loss-of-function variants in TWIST2"* ([PMID: 36942595](https://pubmed.ncbi.nlm.nih.gov/36942595/)).

**Modifier genes.** None established. The E→ (K vs Q/A) identity at codon 75 is itself the principal genotype-driven modifier of phenotype (AMS vs BSS).

**Epigenetic information.** No disease-specific methylation signature is described for AMS. Of note, in *cancer* cell lines the *DERMO1/TWIST2* promoter can be silenced by CpG-island hypermethylation ([PMID: 21109964](https://pubmed.ncbi.nlm.nih.gov/21109964/)) — relevant to TWIST2 biology as a tumor-suppressor context but not to AMS pathogenesis.

**Chromosomal abnormalities.** None cause AMS; karyotype/CMA are normal in AMS and serve mainly to exclude CNV mimics. (By contrast, a 1p36.23p36.22 dosage change relates to the *Setleis*/FFDD3 spectrum, [PMID: 36942595](https://pubmed.ncbi.nlm.nih.gov/36942595/).)

---

## 5. Environmental Information

- **Environmental factors:** None known. AMS is not caused or triggered by toxins, radiation, pollution, or occupational exposure.
- **Lifestyle factors:** Not applicable — no smoking/diet/alcohol association (congenital de novo genetic disorder).
- **Infectious agents:** None. AMS is not infectious in origin and has no known infectious trigger.

This section is essentially **"not applicable"** for AMS: it is a purely genetic, de novo Mendelian disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **de novo heterozygous mutation *TWIST2* c.223G>A (p.Glu75Lys)** arises in the germline, placing a lysine in the basic DNA-binding domain of the TWIST2 (DERMO1) bHLH transcription factor. → *leads to*
2. **Altered DNA-binding specificity** of the mutant TWIST2 protein (demonstrated: altered binding of Flag-TWIST2 in HeLa cells), producing a **dominant antimorphic/neomorphic** activity rather than loss of function. → *results in*
3. **Dysregulation of the TWIST2/DERMO1 transcriptional program** in mesenchymal progenitor cells. TWIST2 normally dimerizes with E-proteins, binds E-box DNA, and acts **downstream of canonical Wnt/β-catenin signaling** as a master regulator of dermal/mesenchymal lineage identity. → *leads to*
4. **Impaired specification and differentiation of cranial-neural-crest- and mesoderm-derived mesenchymal progenitors** (dermal fibroblasts, cranial mesenchyme, chondrogenic/osteogenic and adipogenic precursors). → *results in*
5. **Faulty morphogenesis of ectoderm-associated mesenchymal structures**: eyelid anterior lamella, malar/zygomatic bone, auricular cartilage, hair follicles, skin, nipples, and genitalia. → *manifests as*
6. **Clinical phenotype:** ablepharon, macrostomia, malar/zygomatic hypoplasia, ear dysplasia, sparse hair, redundant/ichthyotic skin, rudimentary nipples, ambiguous genitalia.
7. **[Downstream / inferred, secondary]** Anterior-lamella deficiency → **lagophthalmos** → **corneal exposure** → **exposure keratopathy** → **corneal ulceration** → **blindness if untreated**.

**Branch note:** Steps 1–3 are demonstrated *in vitro* and in animal models; steps 4–5 are inferred from TWIST2/DERMO1 developmental biology; step 7 is a well-documented secondary mechanical consequence.

### Supporting detail by category

- **Molecular pathways.** Canonical **Wnt/β-catenin → DERMO1/TWIST2** axis. *"Wnt signaling/β-catenin is absolutely required and sufficient for Dermo1 expression and dermal cell identity in the cranium"* ([PMID: 20980404](https://pubmed.ncbi.nlm.nih.gov/20980404/)). In zebrafish skin-appendage development, *"the expression of twist2/dermo1 and twist3 is regulated by Wnt signaling"* ([PMID: 33994357](https://pubmed.ncbi.nlm.nih.gov/33994357/)). GO suggestions: **GO:0016055** (Wnt signaling pathway), **GO:0006357** (regulation of transcription by RNA Pol II), **GO:0003700** (DNA-binding transcription factor activity).
- **Cellular processes.** Mesenchymal stem-cell self-renewal and lineage commitment; suppression of osteogenesis and promotion of adipogenesis via Id genes. *"implicate the TWIST gene family members as potential mediators of MSC self-renewal and lineage commitment in postnatal skeletal tissues"* ([PMID: 19609939](https://pubmed.ncbi.nlm.nih.gov/19609939/)). GO: **GO:0060485** (mesenchyme development), **GO:0001837** (EMT), **GO:0030154** (cell differentiation).
- **Protein dysfunction.** bHLH transcription factor with altered DNA-binding; **gain-of-abnormal-function/antimorph**, not misfolding/aggregation. Basic-domain substitutions *"exert antimorphic effects"* ([PMID: 30450715](https://pubmed.ncbi.nlm.nih.gov/30450715/)).
- **Metabolic changes / immune involvement / oxidative injury:** Not primary to AMS. (Twist2-null mice — a *loss-of-function* context distinct from AMS — show elevated proinflammatory cytokines and perinatal death, illustrating TWIST2's role restraining inflammation, but this is not the AMS mechanism.)
- **Biochemical abnormality.** Transcription-factor DNA-binding defect (no enzyme/ion-channel deficiency).
- **Molecular profiling.** Mutant TWIST2 expressed in zebrafish embryos causes **widespread transcriptome changes** and abnormal developmental phenotypes ([PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/)); the *C. elegans hlh-8* allelic series shows graded gene-expression changes ([PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/)). No human patient transcriptomic/proteomic/metabolomic datasets exist.

**Cell types (CL suggestions):** dermal fibroblast (CL:0000057), mesenchymal stem cell (CL:0000134), cranial neural crest cell (CL:0000333), chondrocyte (CL:0000138). **GO biological processes:** mesenchyme development (GO:0060485), skin development (GO:0043588), palate development, hair follicle morphogenesis (GO:0031069).

---

## 7. Anatomical Structures Affected

**Organ level (primary).**
- **Eyelids / anterior lamella** (UBERON:0000014 skin of eyelid; UBERON:0001711 eyelid) — cardinal.
- **Mouth / oral opening** (UBERON:0000165 mouth) — macrostomia.
- **External ear / auricle** (UBERON:0001757 pinna).
- **Malar/zygomatic bone** (UBERON:0001683 zygomatic bone) — hypoplasia/arch absence.
- **Skin** (UBERON:0002097) — ichthyotic, redundant.
- **Hair follicles** (UBERON:0002073) — sparse hair/alopecia.
- **Nipple/breast** (UBERON:0002030) — rudimentary nipples.
- **External genitalia** (UBERON:0000990 reproductive system) — ambiguous/abnormal.

**Secondary organ involvement.**
- **Cornea/ocular surface** (UBERON:0000964) — exposure keratopathy, ulceration (mechanical consequence of eyelid defect).
- **Larynx/trachea** (UBERON:0001737 / UBERON:0003126) — rare malacia/stenosis ([PMID: 31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/)).

**Body systems:** integumentary (skin/hair/nails), musculoskeletal (craniofacial bone/cartilage), ocular/adnexal, reproductive/genitourinary, and (rarely) respiratory.

**Tissue/cell level.** Predominantly **mesenchyme-derived connective tissue** (dermis, cranial mesenchyme, cartilage/bone precursors) and their epithelial appendages. Targeted cell populations: **dermal fibroblasts (CL:0000057), mesenchymal stem cells (CL:0000134), cranial neural crest cells (CL:0000333), chondrocytes (CL:0000138)**.

**Subcellular level.** The molecular lesion resides in the **nucleus** (GO:0005634) — a DNA-binding transcription factor acting on chromatin (GO:0003700 DNA-binding TF activity; GO:0000981).

**Localization / lateralization.** Craniofacial midline and paired bilateral structures; the eyelid, ear, and malar defects are typically **bilateral** (e.g., "bilateral absence or hypoplasia of lower eyelids," [PMID: 3293678](https://pubmed.ncbi.nlm.nih.gov/3293678/)).

---

## 8. Temporal Development

- **Onset:** **Congenital** — all structural features are present at birth; the disorder is fully developmental. Onset pattern is fixed/congenital rather than acute or progressive.
- **Progression:** The malformations themselves are **stable/non-progressive** (structural). The **ophthalmic complication is time-critical**: exposure keratopathy can develop within the first days of life and progress to corneal ulceration and permanent vision loss without intervention ([PMID: 29538102](https://pubmed.ncbi.nlm.nih.gov/29538102/); [PMID: 38967579](https://pubmed.ncbi.nlm.nih.gov/38967579/)).
- **Disease course / duration:** Chronic/lifelong structural condition; managed by staged reconstruction over childhood into adulthood. Patients survive into adulthood (reported at ages 37 and 46 years: [PMID: 31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/); [PMID: 15103726](https://pubmed.ncbi.nlm.nih.gov/15103726/)).
- **Critical periods:** The **neonatal period** is the key window of vulnerability (corneal protection) and of intervention opportunity. Staged eyelid reconstruction thereafter shows durable results at 10–15 year follow-up ([PMID: 31373987](https://pubmed.ncbi.nlm.nih.gov/31373987/)).
- **Remission:** Not applicable (structural congenital malformation); surgical correction is the only route to functional improvement.

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare.** *"Only 15 patients with AMS have been described in 12 articles"* ([PMID: 31373987](https://pubmed.ncbi.nlm.nih.gov/31373987/)); *"fewer than 20 cases being reported in the literature"* ([PMID: 33055564](https://pubmed.ncbi.nlm.nih.gov/33055564/)). Prevalence/incidence are not formally quantifiable but far below 1/1,000,000. No population-based registry data exist.

**Genetic etiology.**
- **Inheritance pattern:** **Autosomal dominant**, almost always **de novo**; rare familial transmission and rare **mosaic** cases ([PMID: 31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/); [PMID: 39792429](https://pubmed.ncbi.nlm.nih.gov/39792429/); [PMID: 34092176](https://pubmed.ncbi.nlm.nih.gov/34092176/)).
- **Penetrance:** Complete for the constitutional E75K genotype (mosaicism attenuates severity).
- **Expressivity:** Variable; **mosaic expression → milder phenotype** ([PMID: 34092176](https://pubmed.ncbi.nlm.nih.gov/34092176/)).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline/somatic mosaicism:** Reported in rare milder cases.
- **Founder effects / consanguinity:** None described; parents typically unrelated ([PMID: 34850759](https://pubmed.ncbi.nlm.nih.gov/34850759/)). (Consanguinity is relevant to the *recessive* Setleis syndrome, not AMS.)
- **Carrier frequency:** Not applicable (dominant, de novo).

**Population demographics.**
- **Affected populations:** Worldwide, no ethnic enrichment; cases reported across regions including the first West African report ([PMID: 34850759](https://pubmed.ncbi.nlm.nih.gov/34850759/)).
- **Geographic distribution:** None (sporadic, global).
- **Sex ratio:** Both sexes affected; ambiguous genitalia reported in both males and females (no strong sex bias).
- **Age distribution:** Diagnosed at birth; patients span neonates to at least the fifth decade.

---

## 10. Diagnostics

**Diagnostic approach (F008).** Diagnosis is **clinical gestalt** — the pathognomonic combination of ablepharon + macrostomia with ectodermal/craniofacial/genital features at birth — **confirmed by molecular testing**.

- **Genetic testing:**
  - **Single-gene *TWIST2* sequencing** for the recurrent **c.223G>A (p.Glu75Lys)** is the confirmatory test of choice; the specific codon-75 substitution also distinguishes AMS (E75K) from allelic BSS (E75Q/E75A) ([PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/)).
  - **Whole-exome/whole-genome sequencing** is useful when the diagnosis is uncertain or for gene discovery.
  - **Chromosomal microarray / karyotype** are typically **normal**; their role is to exclude CNV/aneuploidy mimics.
  - Mitochondrial DNA, repeat-expansion, and FISH testing are **not indicated**.
- **Clinical tests / imaging:** Skull radiography/CT can demonstrate **malar/zygomatic hypoplasia or zygomatic-arch absence** ([PMID: 3293678](https://pubmed.ncbi.nlm.nih.gov/3293678/); [PMID: 34850759](https://pubmed.ncbi.nlm.nih.gov/34850759/)). Ophthalmic slit-lamp examination assesses corneal integrity/exposure. Bronchoscopy is used if airway symptoms suggest laryngo-tracheal malacia/stenosis ([PMID: 31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/)).
- **Laboratory/biomarkers:** No specific biochemical biomarker; diagnosis is molecular. Endocrine/genital work-up may be needed for ambiguous genitalia.
- **Omics-based diagnostics:** Not used clinically for AMS.

**Clinical criteria.** No formal consensus diagnostic criteria; diagnosis rests on the characteristic phenotype + *TWIST2* variant.

**Differential diagnosis.**
| Condition | Gene/mechanism | Distinguishing feature |
|---|---|---|
| **Barber-Say syndrome** (allelic) | *TWIST2* E75Q/E75A | **Hypertrichosis** (vs sparse hair in AMS); codon-75 substitution differs ([PMID: 28680619](https://pubmed.ncbi.nlm.nih.gov/28680619/)) |
| **Saethre-Chotzen syndrome** | *TWIST1* haploinsufficiency | **Craniosynostosis** — a cardinal feature *absent* in AMS ([PMID: 30450715](https://pubmed.ncbi.nlm.nih.gov/30450715/)) |
| **Sweeney-Cox syndrome** | *TWIST1* Glu117 | Paralogous TWIST1 basic-domain substitution ([PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/)) |
| **Setleis syndrome / FFDD3** | *TWIST2* biallelic LoF (AR) | Recessive; focal facial dermal dysplasia ([PMID: 36942595](https://pubmed.ncbi.nlm.nih.gov/36942595/)) |
| **Fraser / cryptophthalmos spectrum** | *FRAS1 / FREM2 / GRIP1* | Cryptophthalmos (skin covering eye), syndactyly ([PMID: 37493047](https://pubmed.ncbi.nlm.nih.gov/37493047/)) |

*"craniosynostosis, which is a cardinal feature of Saethre-Chotzen syndrome"* — its absence is a key discriminator for AMS ([PMID: 30450715](https://pubmed.ncbi.nlm.nih.gov/30450715/)).

**Screening.** No population newborn screening exists (ultra-rare, clinically obvious at birth). Cascade/carrier screening is generally unnecessary given de novo origin, but molecular confirmation informs recurrence-risk counseling.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** Generally **normal life expectancy**; cognition typically normal. AMS is not intrinsically lethal — patients reach adulthood (documented at 37 and 46 years). Rare life-threatening events are secondary (e.g., acute airway compromise from laryngo-tracheal stenosis requiring tracheostomy, [PMID: 31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/)).
- **Morbidity / function:** Dominated by **ophthalmic morbidity** — untreated exposure keratopathy can cause permanent vision loss/blindness ([PMID: 38967579](https://pubmed.ncbi.nlm.nih.gov/38967579/); [PMID: 33055564](https://pubmed.ncbi.nlm.nih.gov/33055564/)). Facial dysmorphism affects feeding, speech, and psychosocial function.
- **Disease course / complications:** Exposure keratopathy, corneal ulceration; feeding/airway issues; psychosocial impact. Surgical reconstruction substantially improves function and appearance.
- **Recovery potential:** Structural defects are **surgically correctable** with good durability — full-thickness skin grafts over Müller muscle gave clear corneas at 10–15 year follow-up ([PMID: 31373987](https://pubmed.ncbi.nlm.nih.gov/31373987/)).
- **Prognostic factors:** **Timeliness of neonatal corneal protection** is the principal determinant of visual outcome. Mosaic cases have milder overall prognosis ([PMID: 34092176](https://pubmed.ncbi.nlm.nih.gov/34092176/)).
- **Prognostic biomarkers:** None molecular; genotype (E75K constitutional vs mosaic) predicts severity.

---

## 12. Treatment

**No disease-modifying pharmacotherapy or gene/RNA/cell therapy exists.** Management is **supportive, surgical, and multidisciplinary** (F004).

**Urgent supportive care (neonatal).** Intensive **ocular lubrication** to prevent exposure keratopathy; *"Despite intensive ocular lubrication, severe exposure keratopathy developed within the first days after birth. The eyes were closed using masquerade flaps"* ([PMID: 29538102](https://pubmed.ncbi.nlm.nih.gov/29538102/)). NCIT suggestions: ocular lubricant therapy, supportive care (NCIT:C15277).

**Surgical / interventional — eyelid (anterior-lamella) reconstruction.** The eyelids are not truly absent but foreshortened with anterior-lamellar dysgenesis; staged reconstruction is the standard:

| Technique | Evidence | Outcome |
|---|---|---|
| Full-thickness skin grafts over Müller-muscle/conjunctiva complex | [PMID: 31373987](https://pubmed.ncbi.nlm.nih.gov/31373987/) | *"all 3 cases who underwent upper eyelid lengthening with full thickness skin grafts placed over Müller muscle had clear corneas"*; durable at 10–15 yr |
| Masquerade flaps (urgent), then staged division | [PMID: 29538102](https://pubmed.ncbi.nlm.nih.gov/29538102/) | Emergency corneal protection in severe neonates |
| Autologous rib cartilage + fat grafting (lower lid) | [PMID: 33055564](https://pubmed.ncbi.nlm.nih.gov/33055564/) | First reported use for lower-lid reconstruction |
| Modified reverse hatchet flap + preputial skin graft | [PMID: 38967579](https://pubmed.ncbi.nlm.nih.gov/38967579/) | Corneal protection / lid lengthening |
| Deep skin grafts adjusting eyelid contour/position | [PMID: 39792429](https://pubmed.ncbi.nlm.nih.gov/39792429/) | Improved eyelid contour and position |

**Other reconstructive surgery.** Macrostomia repair (commissuroplasty), ear reconstruction, malar augmentation, skin and genital surgery, all coordinated multidisciplinarily ([PMID: 33689605](https://pubmed.ncbi.nlm.nih.gov/33689605/)). Airway stenosis managed by temporary tracheostomy + corticosteroids ([PMID: 31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/)). NCIT suggestions: reconstructive surgical procedure, skin graft (NCIT:C15325), tracheostomy (NCIT:C51796).

**Supportive/rehabilitative.** Feeding support, speech therapy, and psychosocial support as needed.

**Experimental / advanced therapeutics.** None; no ClinicalTrials.gov interventional trials for AMS. Pharmacogenomics, targeted therapy, and immunotherapy are **not applicable**.

**Treatment strategy.** Algorithm: (1) immediate corneal protection at birth → (2) staged anterior-lamellar eyelid reconstruction → (3) sequential correction of macrostomia, ear, malar, skin, and genital anomalies, timed to growth and function.

---

## 13. Prevention

- **Primary prevention:** None possible — de novo mutation; not preventable by risk-factor modification, vaccination, or lifestyle change.
- **Secondary prevention:** **Early recognition and immediate neonatal corneal protection** is the critical "secondary prevention" that prevents the major preventable complication (blindness) ([PMID: 29538102](https://pubmed.ncbi.nlm.nih.gov/29538102/); [PMID: 38967579](https://pubmed.ncbi.nlm.nih.gov/38967579/)).
- **Tertiary prevention:** Staged reconstruction and ongoing ophthalmic/multidisciplinary follow-up to prevent complications and disability.
- **Genetic screening / counseling:** For families with an affected child, recurrence risk is low (de novo) but non-zero due to possible **germline mosaicism**; genetic counseling and, where desired, prenatal/preimplantation testing for the known *TWIST2* variant are appropriate. Prenatal ultrasound may detect facial anomalies.
- **Immunization, public-health, environmental, behavioral, prophylactic measures:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / natural disease:** No naturally occurring AMS-equivalent disease is reported in companion animals or wildlife (OMIA has no AMS entry). AMS is a human de novo disorder; there is **no zoonotic or cross-species transmission** (not applicable).
- **Orthologous genes:** *TWIST2/DERMO1* is evolutionarily conserved — zebrafish *twist2/dermo1* (and *twist3*), *C. elegans* single Twist homolog ***hlh-8*** (residue Glu29), and mouse *Twist2/Dermo1*. The disease-critical glutamic-acid residue (human Glu75) is conserved across paralogs and orthologs ([PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/)).
- **Comparative biology:** The graded-severity allelic series across TWIST1/TWIST2 basic-domain substitutions is conserved and reproducible in *C. elegans*, demonstrating deep evolutionary conservation of the Twist-family transcription-factor mechanism ([PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/)).

---

## 15. Model Organisms

**AMS is well-modeled experimentally (F006):**

| Model | Construct | Recapitulation | Reference |
|---|---|---|---|
| **Zebrafish** (*Danio rerio*) | CRISPR base-edited **twist2 p.E78K** knock-in (paralogous to human E75K) | *"recapitulating pathological features of human ablepharon macrostomia syndrome (AMS)"* | [PMID: 33272268](https://pubmed.ncbi.nlm.nih.gov/33272268/); protocol [PMID: 30076894](https://pubmed.ncbi.nlm.nih.gov/30076894/) |
| **Zebrafish** (overexpression) | Mutant TWIST2 mRNA in embryos | Abnormal developmental phenotypes + widespread transcriptome changes | [PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/) |
| ***C. elegans*** | All five TWIST1/TWIST2 disease alleles engineered into *hlh-8* Glu29 | Graded severity of gene-expression and M-lineage/muscle cellular phenotypes | [PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/) |
| **In vitro (HeLa)** | Flag-TWIST2 mutants | Altered DNA-binding pattern | [PMID: 26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/) |
| **Mouse** (*Twist2/Dermo1*) | Knockout / Dermo1-Cre lineage tools | Developmental biology of Wnt/β-catenin–Dermo1 mesenchyme; Twist2-null → perinatal death with elevated proinflammatory cytokines | [PMID: 20980404](https://pubmed.ncbi.nlm.nih.gov/20980404/), [PMID: 18231602](https://pubmed.ncbi.nlm.nih.gov/18231602/) |

*"zAncBE4max successfully generated the Twist2 p.E78K mutation in zebrafish, recapitulating pathological features of human ablepharon macrostomia syndrome (AMS)"* ([PMID: 33272268](https://pubmed.ncbi.nlm.nih.gov/33272268/)). *"we engineered all five disease-associated alleles into the equivalent Glu29 residue encoded by hlh-8, the single Twist homolog present in Caenorhabditis elegans"* ([PMID: 28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/)).

**Applications:** These models enable study of the antimorphic DNA-binding mechanism, the allelic-series severity gradient (AMS vs BSS vs Sweeney-Cox), and downstream transcriptional dysregulation. **Limitations:** Invertebrate/fish models incompletely capture human craniofacial/ectodermal complexity; no mouse knock-in of the exact E75K antimorph is reported for full AMS phenotype recapitulation. **Resources:** ZFIN (zebrafish), WormBase (*C. elegans*), MGI (mouse *Twist2*).

---

## Mechanistic Model / Interpretation

```
            de novo TWIST2 c.223G>A (p.Glu75Lys) — basic DNA-binding domain
                                   |  [demonstrated]
                                   v
                 Altered TWIST2 DNA-binding specificity
                 (dominant ANTIMORPH — not loss of function)
                                   |  [demonstrated: HeLa; zebrafish transcriptome]
                                   v
       Wnt/beta-catenin --> DERMO1/TWIST2 transcriptional program DYSREGULATED
                                   |  [inferred from developmental biology]
                                   v
      Impaired specification/differentiation of mesenchymal progenitors
      (dermal fibroblasts, cranial NCC-derived mesenchyme, cartilage/bone)
                                   |
        +--------------+----------+-----------+-------------+-----------+
        v              v                      v             v           v
   eyelid anterior  malar/zygomatic      auricular      hair/skin   genital/
   lamella defect     hypoplasia          cartilage    (ichthyosis, nipple
        |            (arch absence)        dysplasia    alopecia)    anomalies
        v
   ABLEPHARON --> lagophthalmos --> corneal exposure --> exposure keratopathy
                                   [secondary/mechanical] --> ulceration --> BLINDNESS (if untreated)

   MACROSTOMIA (wide fish-shaped mouth) — parallel branch of oral mesenchyme defect
```

**Key interpretive points.** (1) The **allele identity at codon 75** determines the disease (K→AMS, Q/A→BSS), while the **mechanism** determines the axis (dominant antimorph → AMS/BSS; recessive LoF → Setleis) — a textbook demonstration of how different mutation *types* in one gene yield distinct diseases. (2) The mechanism is a **transcription-factor DNA-binding perturbation upstream of a broad developmental program**, explaining the pleiotropic, multi-structure phenotype. (3) The most clinically actionable step is **downstream and mechanical** (eyelid → cornea), which is why timely surgical/supportive intervention — not molecular therapy — currently drives outcomes.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/) | Landmark: recurrent basic-domain *TWIST2* mutations; E75K→AMS, E75Q/A→BSS; altered DNA binding in HeLa; zebrafish transcriptome | F001, F002, F007, F008 (core causal + mechanism) |
| [28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/) | TWIST1/TWIST2 allelic series; *C. elegans hlh-8* modeling; graded severity | F002, F006 |
| [36942595](https://pubmed.ncbi.nlm.nih.gov/36942595/) | Recessive LoF *TWIST2* → Setleis/FFDD3 (contrasts dominant AMS) | F002, F008 |
| [30450715](https://pubmed.ncbi.nlm.nih.gov/30450715/) | Antimorphic effect of basic-domain substitutions; craniosynostosis distinguishes Saethre-Chotzen from AMS | F002, F005, F007, F008 |
| [15103726](https://pubmed.ncbi.nlm.nih.gov/15103726/) | Canonical clinical feature list (46-yr-old patient) | F003 |
| [3293678](https://pubmed.ncbi.nlm.nih.gov/3293678/) | Zygomatic-arch absence; bilateral lid involvement | F003, F007 |
| [34092176](https://pubmed.ncbi.nlm.nih.gov/34092176/) | Mosaic *TWIST2* → milder phenotype; anterior-lamella hallmark | F003, F005 |
| [34850759](https://pubmed.ncbi.nlm.nih.gov/34850759/) | First West African case; absent prepuce; unrelated parents | F003, F005 |
| [31462237](https://pubmed.ncbi.nlm.nih.gov/31462237/) | Laryngo-tracheal stenosis; AD mutation; adult survival | F003, F005 |
| [38967579](https://pubmed.ncbi.nlm.nih.gov/38967579/) | Sight-threatening keratopathy; reverse hatchet flap | F003, F004 |
| [31373987](https://pubmed.ncbi.nlm.nih.gov/31373987/) | Definitive skin-graft-over-Müller technique; 10–15 yr outcomes; "only 15 patients" | F004, F005 |
| [29538102](https://pubmed.ncbi.nlm.nih.gov/29538102/) | Masquerade flap; urgent neonatal corneal protection | F004 |
| [33055564](https://pubmed.ncbi.nlm.nih.gov/33055564/) | Rib-cartilage/fat grafting; "<20 cases" | F004, F005 |
| [39792429](https://pubmed.ncbi.nlm.nih.gov/39792429/) | Deep skin grafts; AD inheritance statement | F004, F005 |
| [33689605](https://pubmed.ncbi.nlm.nih.gov/33689605/) | Multidisciplinary care | F004 |
| [33272268](https://pubmed.ncbi.nlm.nih.gov/33272268/) | Zebrafish twist2 E78K knock-in recapitulates AMS | F006 |
| [30076894](https://pubmed.ncbi.nlm.nih.gov/30076894/) | Base-editing protocol reproducing the AMS mutation in zebrafish | F006 |
| [20980404](https://pubmed.ncbi.nlm.nih.gov/20980404/) | Wnt/β-catenin required/sufficient for Dermo1 + cranial dermal identity | F007 |
| [33994357](https://pubmed.ncbi.nlm.nih.gov/33994357/) | twist2/dermo1 Wnt-regulated in skin-appendage development | F007 |
| [19609939](https://pubmed.ncbi.nlm.nih.gov/19609939/) | TWIST family mediates MSC self-renewal/lineage commitment | F007 |
| [28680619](https://pubmed.ncbi.nlm.nih.gov/28680619/) | Barber-Say (hypertrichosis) differential | F008 |
| [37493047](https://pubmed.ncbi.nlm.nih.gov/37493047/) | Cryptophthalmos/Fraser differential | F008 |
| [28690482](https://pubmed.ncbi.nlm.nih.gov/28690482/) | Patient's-view QoL perspective | Section 3 |
| [21109964](https://pubmed.ncbi.nlm.nih.gov/21109964/) | DERMO1 promoter methylation (cancer context) | Section 4 (epigenetics, non-AMS) |
| [18231602](https://pubmed.ncbi.nlm.nih.gov/18231602/) | Dermo1-Cre/β-catenin mesenchymal lineage biology | Section 6/15 |

**Evidence-type mix:** human clinical (case reports/series), in vitro (HeLa DNA-binding), and model organism (zebrafish, *C. elegans*, mouse). There are **no** large human -omics cohort datasets for AMS.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Fewer than ~20 reported patients; all clinical/epidemiologic claims rest on aggregated case reports — no registries, no prevalence/incidence figures, no controlled QoL data.
2. **Mechanism partly inferred.** Steps 1–3 (mutation → altered DNA binding → transcriptome change) are demonstrated; steps 4–5 (tissue-specific developmental failure) are inferred from TWIST2/DERMO1 biology, not directly from AMS patient tissue.
3. **No exact mammalian knock-in.** The zebrafish E78K and *C. elegans hlh-8* models are informative but phylogenetically distant; no mouse *Twist2* E75K knock-in recapitulating the full craniofacial AMS phenotype has been reported.
4. **No molecular therapy.** No pharmacologic, gene-editing, or ASO approach is in development; the antimorphic/dominant mechanism (rather than simple LoF) complicates gene-replacement strategies.
5. **Genotype–phenotype nuance unresolved.** Why lysine (E75K) specifically yields AMS while glutamine/alanine yield BSS — i.e., the precise altered DNA-binding readout — is not fully mapped at the level of target genes.
6. **Under-characterized systemic involvement.** Rare visceral features (airway, genital) are described anecdotally; their true frequency and natural history are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC / organoid models:** Generate *TWIST2* E75K iPSCs and differentiate into cranial-neural-crest and dermal mesenchyme to directly map the dysregulated transcriptional program (RNA-seq + CUT&RUN/ChIP-seq for mutant vs WT TWIST2 genome-wide binding).
2. **Precise mouse knock-in:** Create a conditional *Twist2* E75K knock-in mouse to test craniofacial/eyelid/skin phenotype recapitulation and to serve as a preclinical platform.
3. **Define the altered-binding "neo-target" set:** Comparative genome-wide binding of E75K vs E75Q/A vs WT to explain the AMS-vs-BSS divergence mechanistically.
4. **Allele-selective silencing proof-of-concept:** Given the dominant antimorph, test allele-specific ASO/siRNA or base-editing correction in the zebrafish E78K model as a therapeutic feasibility study.
5. **International registry + natural-history study:** Pool the ultra-rare cases to quantify feature frequencies, ophthalmic outcomes, and standardized QoL (validated instruments), and to formalize diagnostic/management guidelines.
6. **Standardize surgical outcome reporting:** Prospective, multi-center comparison of eyelid-reconstruction techniques (skin-graft-over-Müller vs rib-cartilage/fat vs flaps) with corneal and cosmetic endpoints at ≥10 years.

---

*Report compiled from 8 confirmed findings and 29 reviewed papers over a 5-iteration autonomous investigation. Evidence types: human clinical case literature, in vitro DNA-binding assays, and zebrafish/C. elegans/mouse model-organism studies.*


## Artifacts

- [OpenScientist final report](Ablepharon_Macrostomia_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ablepharon_Macrostomia_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 15 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:20980404` (6 mentions) - Role of canonical Wnt signaling/ß-catenin via Dermo1 in cranial dermal cell development.
  - shared terms: dermo1
- `PMID:19609939` (4 mentions) - TWIST family of basic helix-loop-helix transcription factors mediate human mesenchymal stem cell growth and commitment.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `ams`, `twist2`, `phenotype`, `skin`, `dna-binding`, `gene`, `dermo1`, `dominant`, `novo`, `corneal`, `disease`, `e75k`, `exposure`, `eyelid`, `bss`, `mutation`, `mechanism`, `macrostomia`, `patient`, `syndrome`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008693` (2 mentions) - the report calls it "MONDO"; MONDO calls it **ablepharon macrostomia syndrome**
- `HP:0011500` (1 mention) - the report calls it "Ablepharon"; HP calls it **Polycoria**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000154` (1 mention) - the report calls it "Macrostomia"; HP calls it **Wide mouth**, and lists "Macrostomia" among its other names
- `HP:0000356` (1 mention) - the report calls it "Abnormal outer ear morphology"; HP calls it **Abnormality of the outer ear**
- `HP:0002557` (1 mention) - the report calls it "Rudimentary/absent nipples"; HP calls it **Hypoplastic nipples**, and lists "Small nipples" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0002030` (1 mention) - the report calls it "Nipple/breast"; UBERON calls it **nipple**
- `UBERON:0000964` (1 mention) - the report calls it "Cornea/ocular surface"; UBERON calls it **cornea**, and lists "cornea of camera-type eye" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.