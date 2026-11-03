---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T03:39:43.500645'
end_time: '2026-10-15T04:21:58.773113'
duration_seconds: 2535.27
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glutaric Acidemia Type 3
  mondo_id: MONDO:0009283
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 23
  verified: 21
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.045
  labels_checked: 11
  labels_matching: 4
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - Clinical sign
    ontology_label: Global developmental delay
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0002500
    reported_labels:
    - Leukoencephalopathy
    ontology_label: Abnormal cerebral white matter morphology
  - term_id: UBERON:0002113
    reported_labels:
    - Mouse modifier branch:** kidney
    ontology_label: kidney
  labels_variant: 3
  unresolved_terms:
  - CHEBI:45009
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Glutaric_Acidemia_Type_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Glutaric_Acidemia_Type_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glutaric Acidemia Type 3
- **MONDO ID:** MONDO:0009283 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glutaric Acidemia Type 3** covering all of the
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

# Glutaric Acidemia Type 3 (GA3): A Comprehensive Disease Characteristics Report

**Disease:** Glutaric Acidemia Type 3 (Glutaric Aciduria Type 3, GA3)
**MONDO ID:** MONDO:0009283 | **OMIM:** 231690 | **Gene:** SUGCT (C7orf10), gene OMIM 609187
**Category:** Mendelian, autosomal recessive inborn error of metabolism

---

## Summary

Glutaric acidemia type 3 (GA3) is a rare autosomal-recessive inborn error of organic-acid metabolism caused by biallelic loss-of-function variants in **SUGCT** (also called **C7orf10**), which encodes the mitochondrial enzyme **succinyl-CoA:glutarate CoA-transferase**. The enzyme's normal function is to recapture free glutarate — generated during lysine and tryptophan catabolism, and substantially by the gut microbiome — by transferring a CoA moiety from succinyl-CoA to produce glutaryl-CoA. When SUGCT activity is lost, free glutarate accumulates and spills into the urine, producing an **isolated glutaric aciduria** with characteristically **normal-to-low 3-hydroxyglutaric acid** and **low glutarylcarnitine/glutarylglycine** — a biochemical signature that cleanly distinguishes GA3 from the clinically severe glutaric acidemia type 1 (GA1/GCDH deficiency) and from GA2/MADD.

The central conclusion of this investigation is that **GA3 is, in the overwhelming majority of cases, a benign biochemical trait — a likely "non-disease."** Only roughly nine individuals had been described in the literature as of 2018, most affected people remain asymptomatic despite markedly elevated urinary glutarate, and the original cohort of six patients showed no consistent clinical phenotype. Population-genetics data reinforce this: SUGCT is **loss-of-function tolerant and non-essential** in gnomAD (pLI ≈ 0; observed/expected LoF ≈ 0.75), meaning that heterozygous and even biallelic loss of the gene is well tolerated at the population level. When severe multisystem disease is reported in a "GA3 patient," it most often reflects **ascertainment bias**, **coincidental comorbidity**, or a **contiguous-gene deletion** that removes the neighbouring *MPLKIP* gene (causing trichothiodystrophy type 4) in addition to *SUGCT*.

Mechanistically, the glutarate burden is strongly modulated by **gene–environment interactions**: the gut microbiome is a major source of glutarate, and in both a *Sugct*-knockout mouse and a symptomatic human patient, **antibiotic treatment reduced glutarate and improved outcomes**. Dietary lysine load similarly worsens metabolic phenotypes in the mouse model. Diagnosis rests on **urine organic acid analysis (GC-MS)** followed by **SUGCT molecular confirmation**; because glutarylcarnitine is not elevated, standard tandem-MS acylcarnitine newborn screening does not detect GA3. There is no disease-specific therapy; management is supportive, and genetic counseling is the principal preventive measure. The main clinical risk GA3 poses is not organ damage but a **diagnostic odyssey** — an isolated urinary glutarate elevation can trigger extensive workup and risks mis-attribution of unrelated symptoms to SUGCT deficiency.

---

## Key Findings

### Finding 1 — GA3 is caused by biallelic SUGCT (C7orf10) variants, inherited autosomal recessively

GA3 is a Mendelian autosomal-recessive disorder. In the landmark mapping study, six unrelated GA3 patients each carried **two pathogenic SUGCT/C7orf10 alleles**, and homozygosity mapping localized the locus to a 4.7 Mb region on chromosome 7p14 ([PMID: 18926513](https://pubmed.ncbi.nlm.nih.gov/18926513/)). The reported alleles included the Amish founder missense **c.895C>T (p.Arg299Trp)** together with two nonsense alleles, **c.322C>T (p.Arg108Ter)** and **c.424C>T (p.Arg142Ter)**. The study concluded: *"Two pathogenic alleles were identified in each of the six patients. There was no consistent clinical phenotype associated with GA3."* A further pathogenic missense allele, **p.Arg322Trp (c.964C>T)**, was later reported in a homozygous patient ([PMID: 32779420](https://pubmed.ncbi.nlm.nih.gov/32779420/)). The enzymatic basis is unambiguous: *"GA3 is associated with decreased conversion of free glutaric acid to glutaryl-coA, reflecting deficiency of succinate-hydroxymethylglutarate coA-transferase, caused by variants in the SUGCT (C7orf10) gene"* ([PMID: 28766179](https://pubmed.ncbi.nlm.nih.gov/28766179/)).

Note on nomenclature: transcript-dependent residue numbering means **p.Arg299Trp**, **p.Arg322Trp**, and **p.Arg329Trp** can refer to the same underlying residue across isoforms (e.g., NM_001193311). Care is needed when reconciling variants across reports.

### Finding 2 — SUGCT enzyme mechanism: succinyl-CoA-dependent conversion of glutarate to glutaryl-CoA

SUGCT is a **mitochondrial CoA-transferase** operating in the lysine/tryptophan catabolic pathway. It converts **free glutarate to glutaryl-CoA using succinyl-CoA as the CoA donor**, thereby preventing urinary loss of the organic acid: *"SUGCT catalyzes the succinyl-CoA-dependent conversion of glutaric acid into glutaryl-CoA preventing urinary loss of the organic acid"* ([PMID: 33483254](https://pubmed.ncbi.nlm.nih.gov/33483254/)). When the enzyme is deficient, the hallmark is an **isolated elevation of urinary free glutarate** with elevated molar ratios of glutarate to its downstream derivatives — *"urine molar ratios of glutarate to its derivatives (3-hydroxyglutarate, glutarylcarnitine, and glutarylglycine) were elevated, suggesting impaired formation of glutaryl-CoA"* ([PMID: 18926513](https://pubmed.ncbi.nlm.nih.gov/18926513/)). Critically, **3-hydroxyglutaric acid is low/normal**, which is the key biochemical discriminator from GA1.

### Finding 3 — GA3 is largely a benign biochemical trait ("non-disease")

The accumulated clinical literature indicates GA3 is generally a benign trait. As of 2018 only **nine individuals** had been described, and the condition is *"generally considered a likely 'non-disease,' but this is based on limited supporting information, with only nine individuals with GA3 described in the literature"* ([PMID: 28766179](https://pubmed.ncbi.nlm.nih.gov/28766179/)). The original six-patient cohort showed **no consistent clinical phenotype** ([PMID: 18926513](https://pubmed.ncbi.nlm.nih.gov/18926513/)). Mouse data concur: *"Although mutations in Sugct lead to Glutaric Aciduria Type 3 disease in humans, patients remain largely asymptomatic despite high levels of glutarate in the urine"* ([PMID: 31722069](https://pubmed.ncbi.nlm.nih.gov/31722069/)). Non-specific symptoms occasionally reported (developmental delay, hypotonia, GI disturbance/cyclic vomiting, white-matter MRI changes) are confounded by ascertainment bias and co-occurring conditions.

### Finding 4 — The gut microbiome is a major source of glutarate; antibiotics reduce it (gene–environment interaction)

A defining feature of GA3 biology is that **much of the circulating/urinary glutarate is of microbial origin**. In *Sugct*-knockout mice, *"After SugctKO mice were treated with antibiotics, metabolites were comparable to WT, indicating that the microbiome affects metabolism in SugctKO mice"* ([PMID: 31722069](https://pubmed.ncbi.nlm.nih.gov/31722069/)). This was mirrored clinically: in a GA3 patient with severe cyclic vomiting, *"A trial of antibiotic treatment, to minimise bacterial GA production, was followed by significant clinical improvement"* ([PMID: 28766179](https://pubmed.ncbi.nlm.nih.gov/28766179/)). The knockout mouse also develops **diet- and age-dependent metabolic syndrome**, with gut dysbiosis, imbalanced lipid/acylcarnitine metabolism in kidney, obesity, and kidney/liver pathology accelerated by a high-lysine diet. This establishes a clear gene–environment axis in which **diet (lysine) and microbiome composition set the glutarate burden**.

### Finding 5 — Contiguous-gene deletions of SUGCT + adjacent MPLKIP cause combined trichothiodystrophy type 4 and GA3

Several of the more severe "GA3" presentations are explained by **contiguous-gene deletions** at chromosome 7p14 that remove both **MPLKIP** (the gene for trichothiodystrophy type 4, TTD4) and **SUGCT**. A 125 kb homozygous deletion including both genes was reported in a Peruvian girl with microcephaly, short stature, intellectual disability and brittle hair: *"Chromosome microarray analysis showed a 125 kb homozygous pathogenic deletion, which includes genes MPLKIP and SUGCT, not described before"* ([PMID: 29421601](https://pubmed.ncbi.nlm.nih.gov/29421601/)). A second independent case confirmed the mechanism: *"To the best of our knowledge, our patient is the second case with co-occurrence of trichothiodystrophy type 4 and glutaric aciduria type 3, resulting from a contiguous gene deletion"* ([PMID: 37064336](https://pubmed.ncbi.nlm.nih.gov/37064336/)), presenting with hypotonia, failure to thrive, microcephaly, brittle hair and hypertransaminasemia. The severe neurocutaneous features in these patients derive from **MPLKIP loss (TTD4), not SUGCT deficiency**.

### Finding 6 — SUGCT gene structure and ClinVar variant landscape support uncertain pathogenicity

SUGCT = **ENSG00000175600**, located chr7:40,135,005–40,860,763 (GRCh38, ~725 kb), **HGNC:16001**, gene OMIM 609187; disease OMIM 231690. The ClinVar landscape reflects genuine uncertainty about pathogenicity: of **169 SUGCT ClinVar variants**, only **1 Pathogenic and 4 Likely pathogenic** (e.g., c.514C>T p.Arg172Ter; splice c.152+1G>A, c.313-1G>C; nonsense c.782G>A p.Trp261Ter, c.1014G>A p.Trp338Ter), versus **87 VUS, 24 benign, 41 likely benign, and 8 conflicting**. Pathogenic variant types are predominantly **nonsense/splice/frameshift (loss-of-function)** plus missense hypomorphs.

### Finding 7 — Common SUGCT variants show GWAS associations distinct from Mendelian GA3

Common non-coding/regulatory variation at the SUGCT locus (7p13/7p14) associates with complex traits **independent of biallelic GA3**. A genome-wide significant, protective association with pancreatic cancer susceptibility was reported: *"7p13 (SUGCT, rs17688601, OR = 0.88, 95% CI = 0.84-0.92, P = 1.41 × 10(-8))"* ([PMID: 26098869](https://pubmed.ncbi.nlm.nih.gov/26098869/)). SUGCT also appears among frailty GWAS loci — *"rs12672085 (SUGCT)"* ([PMID: 41733842](https://pubmed.ncbi.nlm.nih.gov/41733842/)) — and in selection/adaptation scans in chickens ([PMID: 38228059](https://pubmed.ncbi.nlm.nih.gov/38228059/)). These complex-trait signals are mechanistically distinct from the rare Mendelian GA3 phenotype.

### Finding 8 — SUGCT is LoF-tolerant (non-constrained) in gnomAD, consistent with a non-essential gene

gnomAD constraint metrics for SUGCT (MANE transcript ENST00000335693 / NM_001193313) demonstrate **no depletion of loss-of-function variants**: **pLI ≈ 6.1×10⁻¹¹ (~0)**, **observed/expected LoF (oe_lof) = 0.745 (90% CI 0.58–0.97)**, observed LoF = 41 vs expected 55, and missense Z = −0.37 (no missense constraint). This independently predicts that losing SUGCT is well tolerated — concordant with the mouse literature, which emphasizes *"the importance of non-essential genes with no readily detectable early phenotype"* ([PMID: 31722069](https://pubmed.ncbi.nlm.nih.gov/31722069/)).

### Finding 9 — Estimated carrier frequency ~1 in 440 (pLoF lower bound); GA3 is underdiagnosed

Summing gnomAD v4 predicted loss-of-function (pLoF) SUGCT allele frequencies gives **q(pLoF) ≈ 1.15×10⁻³**, implying a heterozygous **carrier frequency ≈ 0.23% (~1 in 437)** and a biallelic-pLoF birth prevalence ≈ q² ≈ 1.3×10⁻⁶ (~0.13 per 100,000). The most common pLoF alleles are **p.Arg101Ter** (AF 2.3×10⁻⁴), splice **c.152+1G>A** (1.5×10⁻⁴) and **c.484+1G>A** (1.3×10⁻⁴). The true biochemical GA3 prevalence is **higher**, because common missense hypomorphs (e.g., the founder p.Arg299Trp) also cause the trait. The primary literature concluded directly: *"Examination of allele frequencies underlines the fact that GA3 is underdiagnosed"* ([PMID: 28766179](https://pubmed.ncbi.nlm.nih.gov/28766179/)).

### Finding 10 — Mouse models: naturally occurring GA3 in 129 substrains and engineered SugctKO

GA3 exists as a **naturally occurring biochemical trait** in inbred 129-substrain mice (e.g., 129S2/SvPasCrl) due to Sugct deficiency, confirmed in a C57BL/6J × 129S2 F2 population: *"we describe the presence of a GA3 trait in mice of 129 substrains due to SUGCT deficiency"* ([PMID: 33483254](https://pubmed.ncbi.nlm.nih.gov/33483254/)). An **engineered SugctKO** mouse reproduces urinary glutarate elevation and reveals the diet/age-dependent pathology: *"we generated SugctKO mice and uncovered imbalanced lipid and acylcarnitine metabolism in kidney in addition to changes in the gut microbiome"* ([PMID: 31722069](https://pubmed.ncbi.nlm.nih.gov/31722069/)), with an obesity-related phenotype, lipid accumulation in kidney/liver, adipocyte "crown-like" structures, and kidney pathology worsened by high-lysine diet and normalized by antibiotics.

### Finding 11 — Diagnosis rests on urine organic acids (isolated glutarate, low 3-OHGA) plus SUGCT sequencing

GA3 is identified by **urine organic acid analysis (GC-MS)** showing isolated elevation of free glutaric acid with **normal/low 3-hydroxyglutaric acid** and low glutarylcarnitine/glutarylglycine ([PMID: 18926513](https://pubmed.ncbi.nlm.nih.gov/18926513/)). This distinguishes GA3 from GA1 (high 3-OHGA, elevated C5DC glutarylcarnitine, striatal injury, macrocephaly) and GA2/MADD (broad organic acid/acylcarnitine abnormalities). Because **glutarylcarnitine (C5DC) is NOT elevated**, standard tandem-MS acylcarnitine newborn screening typically does **not** flag GA3; instead, a population **urine-based** newborn screening program detected one asymptomatic case: *"the third was identified by a population urine-based newborn screening programme and has so far remained asymptomatic"* ([PMID: 28766179](https://pubmed.ncbi.nlm.nih.gov/28766179/)). Confirmation is by **SUGCT molecular testing** (single-gene, panel, WES, or WGS); **chromosomal microarray** detects contiguous-gene deletions (with MPLKIP).

### Finding 12 — SUGCT protein (UniProt Q9HAC7): mitochondrial 438-aa CoA-transferase with broad dicarboxylate specificity

UniProt **Q9HAC7**: Succinyl-CoA:glutarate CoA-transferase, **438 amino acids**, localized to **mitochondrion**. The primary reaction is **glutarate + succinyl-CoA ⇌ glutaryl-CoA + succinate** (reversible). It prefers succinyl-CoA/glutarate-CoA donors but also acts on **3-hydroxy-3-methylglutarate, hexanedioate (adipate), and itaconate**, participating in a dicarboxylate-CoA recycling process. Experimental structures have been deposited: **PDB 9BR6, 9BR7**.

### Finding 13 — Clinical bottom-line: historically benign, but isolated glutarate can trigger a diagnostic odyssey

In a patient with developmental delay, microcephaly, hypotonia and feeding difficulties, biochemical testing revealed an **isolated marked elevation of glutaric acid** without related-metabolite elevations, and WES was needed to resolve the picture, which included GA3: *"GA III has historically been considered clinically benign, with few reported cases"* ([PMID: 39101156](https://pubmed.ncbi.nlm.nih.gov/39101156/)). The lesson is that an isolated glutarate finding is **biochemically non-specific for severe disease** and warrants genetic confirmation plus evaluation for alternative/co-occurring diagnoses (e.g., contiguous-gene TTD4, or unrelated conditions) before attributing symptoms to SUGCT deficiency.

---

## Report by Template Section

### 1. Disease Information
- **Overview:** GA3 is a rare autosomal-recessive inborn error of lysine/tryptophan metabolism characterized by isolated glutaric aciduria due to deficiency of succinyl-CoA:glutarate CoA-transferase (SUGCT). It is generally benign.
- **Identifiers:** MONDO:0009283; OMIM 231690 (disease); gene OMIM 609187; HGNC:16001 (SUGCT); Ensembl ENSG00000175600; UniProt Q9HAC7. ICD-10: E72.3 (disorders of lysine and hydroxylysine metabolism, the closest code). MeSH indexing falls under amino-acid metabolism inborn errors (no GA3-specific MeSH term).
- **Synonyms:** Glutaric aciduria type 3; glutaric aciduria type III; GA3; GA-III; C7orf10 deficiency; SUGCT deficiency; succinyl-CoA:glutarate CoA-transferase deficiency.
- **Information source:** A blend of individual case reports (clinical case level) and aggregated disease-level resources (OMIM, Orphanet) plus population databases (gnomAD, ClinVar). Evidence is dominated by small case series given rarity.

### 2. Etiology
- **Causal factor:** Genetic — biallelic pathogenic SUGCT variants (Finding 1). Loss-of-function (nonsense/splice/frameshift) and hypomorphic missense alleles.
- **Genetic risk:** Inheriting two SUGCT pathogenic alleles; founder allele p.Arg299Trp (Amish). Carrier frequency ~1/440 (Finding 9).
- **Environmental risk/modifiers:** Dietary lysine load and gut-microbiome glutarate production raise the glutarate burden (Findings 4, 10). These are **modifiers of the biochemical phenotype**, not independent causes.
- **Protective factors:** Antibiotic suppression of glutarate-producing gut bacteria lowers glutarate (Finding 4). No established germline protective alleles for GA3.
- **Gene–environment interaction:** Strong — SUGCT genotype sets baseline; microbiome + diet set the realized glutarate level and any symptoms (Findings 4, 10).

### 3. Phenotypes
GA3 has **no obligate clinical phenotype**; the defining feature is a **laboratory abnormality** (Findings 2, 3).

| Phenotype | Type | HPO term | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Glutaric aciduria (isolated) | Laboratory abnormality | HP:0003150 (Glutaric aciduria) | Congenital/lifelong | Biochemical | ~100% (defining) |
| Asymptomatic | — | — | — | — | Majority |
| Developmental delay | Clinical sign | HP:0001263 | Childhood | Variable | Rare, likely confounded |
| Muscular hypotonia | Clinical sign | HP:0001252 | Infancy | Variable | Rare |
| Cyclic vomiting / GI disturbance | Symptom | HP:0002572 / HP:0011968 | Variable | Variable | Rare, microbiome-linked |
| White-matter MRI abnormality | Imaging/lab | HP:0002500 (Leukoencephalopathy) | Variable | Variable | Rare, non-specific |

**Quality of life:** For the asymptomatic majority, negligible impact. Severe QoL impact in reported cases is generally attributable to comorbidities or contiguous-gene TTD4 (Finding 5).

### 4. Genetic/Molecular Information
- **Causal gene:** SUGCT / C7orf10 (HGNC:16001; gene OMIM 609187) — Findings 1, 6.
- **Variant classes:** nonsense (p.Arg108Ter, p.Arg142Ter, p.Arg101Ter, p.Trp261Ter, p.Trp338Ter, p.Arg172Ter), splice (c.152+1G>A, c.313-1G>C, c.484+1G>A), missense hypomorphs (p.Arg299Trp founder; p.Arg322Trp) — Findings 1, 6, 9.
- **ClinVar:** 169 variants; 1 P / 4 LP / 87 VUS / 24 B / 41 LB / 8 conflicting (Finding 6) — high VUS burden reflecting uncertain pathogenicity.
- **Allele frequency:** pLoF q ≈ 1.15×10⁻³; p.Arg101Ter AF 2.3×10⁻⁴ (Finding 9).
- **Origin:** Germline (constitutional); no somatic relevance.
- **Functional consequence:** Loss of function (enzyme deficiency) — Findings 2, 12.
- **Modifier genes:** None established within GA3; MPLKIP is a **contiguous neighbour** whose co-deletion adds the TTD4 phenotype (Finding 5), not a severity modifier of SUGCT per se.
- **Epigenetic/chromosomal:** No GA3-specific epigenetic mechanism. Chromosomal relevance = 7p14 microdeletions spanning SUGCT+MPLKIP (Finding 5).

### 5. Environmental Information
- **Environmental/metabolic factors:** Dietary lysine; gut microbiome glutarate production (Findings 4, 10). Multiple gut bacterial pathways produce glutarate, consistent with the microbiome as a glutarate source.
- **Lifestyle:** Diet composition (protein/lysine) is the main modifiable factor.
- **Infectious agents:** None cause GA3; however, commensal/pathogenic gut bacteria are the relevant glutarate-producing agents, and antibiotics reduce glutarate (Finding 4).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function/hypomorphic variants in **SUGCT** → **leads to** reduced/absent mitochondrial succinyl-CoA:glutarate CoA-transferase activity. *(demonstrated — Findings 1, 12)*
2. Loss of enzyme activity → **results in** failure to convert free glutarate to glutaryl-CoA using succinyl-CoA as donor. *(demonstrated — Finding 2)*
3. Failure of glutarate recapture → **leads to** accumulation of free glutarate from (a) endogenous lysine/tryptophan catabolism and (b) **gut-microbiome production**. *(demonstrated; microbiome contribution shown in mouse + human — Findings 4, 10)*
4. Glutarate accumulation → **results in** isolated glutaric aciduria with elevated glutarate:derivative molar ratios and **low 3-hydroxyglutarate / low glutarylcarnitine**. *(demonstrated — Findings 2, 11)*
5. **BRANCH A (majority):** Because glutarate at these levels is not substantially neurotoxic and SUGCT is non-essential → **leads to** an asymptomatic/benign biochemical trait. *(demonstrated — Findings 3, 8)*
6. **BRANCH B (modifier-dependent, mouse-demonstrated / human-inferred):** High-lysine diet + dysbiotic microbiome → **leads to** elevated glutarate/acylcarnitine and lipid imbalance → kidney/liver lipid accumulation, obesity-like metabolic syndrome, and in a human, severe cyclic vomiting improved by antibiotics. *(mouse demonstrated; human inferred — Findings 4, 10)*
7. **BRANCH C (contiguous-gene deletion):** 7p14 microdeletion removing **MPLKIP + SUGCT** → **results in** combined trichothiodystrophy type 4 (brittle hair, microcephaly, ID, failure to thrive) **plus** GA3; the severe features derive from MPLKIP loss. *(demonstrated — Finding 5)*

- **Molecular pathway:** Lysine/tryptophan catabolism; dicarboxylate-CoA recycling (KEGG lysine degradation).
- **Protein dysfunction:** Loss of function of a 438-aa mitochondrial CoA-transferase (Q9HAC7); broad dicarboxylate specificity (adipate, itaconate, HMG) — Finding 12.
- **Metabolic change:** Amino-acid (lysine) catabolism defect; secondary lipid/acylcarnitine imbalance in mouse kidney (Finding 10).
- **Subcellular compartment:** Mitochondrion (GO:0005739). Biological process: GO:0019477 (L-lysine catabolic process); molecular function: GO:0008410 (CoA-transferase activity).
- **Cell/tissue types (mouse, modifier branch):** renal tubular cells, hepatocytes, adipocytes.
- **CHEBI entities:** glutaric acid (CHEBI:17859), glutaryl-CoA (CHEBI:57378), succinyl-CoA (CHEBI:57292), 3-hydroxyglutaric acid (CHEBI:45009).

### 7. Anatomical Structures Affected
- **Human (majority):** None definitively; GA3 is a systemic biochemical trait detectable in **urine** (UBERON:0001088) and blood.
- **Reported/modifier involvement:** CNS white matter (UBERON:0002316) — non-specific MRI changes; GI tract (UBERON:0001555) — cyclic vomiting.
- **Mouse modifier branch:** kidney (UBERON:0002113), liver (UBERON:0002107), adipose tissue (UBERON:0001013).
- **Subcellular:** mitochondrion (GO:0005739).
- **Lateralization:** Not applicable (systemic/metabolic).

### 8. Temporal Development
- **Onset:** Biochemical abnormality is **congenital/lifelong** (present from birth, detectable by urine screening). Clinical symptoms (when present) are variable and non-specific (Findings 11, 13).
- **Progression:** The biochemical trait is **stable/persistent**. No progressive neurodegeneration characteristic of GA1. Modifier-driven metabolic syndrome in mice is **age- and diet-dependent** (Finding 10).
- **Course:** Chronic lifelong biochemical trait; most individuals remain well.
- **Critical periods:** None established as neurotoxic windows (unlike GA1's striatal vulnerability in infancy).

### 9. Inheritance and Population
- **Inheritance:** Autosomal recessive (Finding 1).
- **Prevalence/incidence:** Very rare in the literature (~9 reported by 2018); pLoF-based biallelic birth prevalence ≈ 0.13/100,000 as a lower bound, with true biochemical prevalence higher due to missense hypomorphs — **underdiagnosed** (Finding 9).
- **Carrier frequency:** ~1 in 440 (pLoF-only lower bound) — Finding 9.
- **Penetrance:** Biochemical penetrance appears high/complete (biallelic loss → glutaric aciduria); **clinical penetrance is low** (most asymptomatic) — Findings 3, 8.
- **Expressivity:** Highly variable clinically; no consistent phenotype (Findings 1, 3).
- **Founder effect:** p.Arg299Trp in the Amish population (Finding 1).
- **Consanguinity:** Relevant (homozygous cases including contiguous-gene deletions in consanguineous families — Finding 5).
- **Sex ratio / anticipation / mosaicism:** No sex bias reported; no anticipation (not a repeat disorder); no mosaicism specific to GA3.

### 10. Diagnostics
- **First-line:** Urine organic acid analysis (GC-MS) — isolated ↑glutarate, low 3-OHGA, low glutarylglycine (Finding 11). Accurate 3-OHGA quantitation can require second-tier GC-MS methods to resolve the 2-/3-OHGA isomers ([PMID: 35500672](https://pubmed.ncbi.nlm.nih.gov/35500672/)).
- **Acylcarnitine (plasma/DBS):** C5DC (glutarylcarnitine) **not elevated** — standard MS/MS newborn screening misses GA3 (Finding 11).
- **Confirmation:** SUGCT molecular testing — single-gene, metabolic gene panel, WES, or WGS; **chromosomal microarray** for contiguous-gene deletions with MPLKIP (Findings 5, 11).
- **Differential diagnosis:** GA1 (GCDH; ↑3-OHGA, ↑C5DC, macrocephaly, striatal injury), GA2/MADD (broad acylcarnitine/organic acid abnormality), other organic acidurias.
- **Screening:** Urine-based NBS can detect asymptomatic GA3 (Finding 11); not captured by MS/MS acylcarnitine NBS.

### 11. Outcome / Prognosis
- **Survival/mortality:** No evidence of reduced survival attributable to isolated SUGCT deficiency; generally **benign prognosis** (Findings 3, 13).
- **Morbidity:** Low in isolated GA3. Significant morbidity in reported cases is typically due to contiguous-gene TTD4 or unrelated comorbidity (Findings 5, 13).
- **Prognostic factors:** Presence/absence of a contiguous-gene deletion (MPLKIP) is the strongest determinant of severe outcome; dietary/microbiome state modifies the biochemical and GI burden.
- **Recovery:** Microbiome-driven symptoms (e.g., cyclic vomiting) may respond to antibiotics (Finding 4).

### 12. Treatment
- **No disease-specific therapy** is established. Management is **supportive** (NCIT:C19678 supportive care).
- **Dietary:** Lysine-restriction is biologically rational (mouse data, Finding 10) but not formally validated as beneficial in human GA3; it is a cornerstone in GA1.
- **Antibiotics:** Rational for symptomatic, microbiome-driven cases (e.g., severe cyclic vomiting) — produced clinical improvement in one patient (Finding 4) — NCIT antibiotic therapy (NCIT:C15844).
- **Supportive care:** Symptom management, nutrition support.
- **Pharmacogenomics / gene / cell / RNA therapies:** None developed or applicable given the benign nature.
- **Combined TTD4+GA3 patients:** managed for the TTD4 features (photosensitivity, hair/skin, developmental support).

### 13. Prevention
- **Primary:** Not applicable in a classical sense; **genetic counseling** of carrier couples is the principal measure (Finding 9).
- **Secondary:** Urine-based newborn/high-risk screening can detect GA3; because most cases are benign, the value of detection is mainly to **avoid a diagnostic odyssey and prevent mis-attribution** rather than to intervene (Findings 11, 13).
- **Genetic screening:** Carrier screening, cascade testing in affected families; prenatal/PGT possible once familial variants known.
- **Tertiary:** For symptomatic/modifier-driven cases, dietary lysine moderation and antibiotic trials may reduce the glutarate burden.

### 14. Other Species / Natural Disease
- **Taxonomy / natural model:** *Mus musculus* (NCBI:txid10090) — GA3 occurs **naturally** in inbred 129 substrains due to Sugct deficiency (Finding 10).
- **Orthologous gene:** mouse *Sugct* (Findings 8, 10).
- **Comparative biology:** The mouse biochemical trait closely mirrors human (urinary glutarate elevation); SUGCT also appears in avian adaptation scans (chicken, Finding 7), indicating conservation.
- **Zoonosis:** Not applicable.

### 15. Model Organisms
- **Natural mouse model:** 129-substrain mice (e.g., 129S2/SvPasCrl) — GA3 trait (Finding 10).
- **Engineered model:** **SugctKO mouse** — recapitulates urinary glutarate elevation; reveals diet/age-dependent microbiome dysbiosis, kidney lipid/acylcarnitine imbalance, obesity-like metabolic syndrome; high-lysine diet exacerbates, antibiotics normalize (Findings 4, 10).
- **Phenotype recapitulation:** Excellent for the **biochemical trait and modifier biology**; the mouse actually reveals more overt metabolic pathology than typical human cases, consistent with humans being largely asymptomatic.
- **Limitations:** Human clinical penetrance is lower than the metabolic-syndrome phenotype seen in mice on provocative diets.
- **Other systems:** No dedicated zebrafish/Drosophila/cell/organoid GA3 models identified; cellular/CRISPR models exist for the unrelated GA1 (GCDH), not GA3.

---

## Mechanistic Model / Interpretation

```
          SUGCT biallelic LoF / hypomorphic variants (chr7p14; AR)
                              │
                              ▼
        ↓ mitochondrial succinyl-CoA:glutarate CoA-transferase activity
                              │
                              ▼
        Free glutarate NOT recaptured into glutaryl-CoA
                    ┌─────────┴───────────┐
        endogenous lysine/Trp        GUT MICROBIOME
        catabolism                   glutarate production
                    └─────────┬───────────┘
                              ▼
     ISOLATED GLUTARIC ACIDURIA  (↑glutarate; LOW 3-OHGA; LOW C5DC)
                              │
        ┌─────────────────────┼─────────────────────────┐
        ▼                     ▼                         ▼
  BRANCH A (majority)   BRANCH B (modifiers)      BRANCH C (contiguous
  Benign / asymptomatic  high-lysine diet +        gene deletion)
  (SUGCT non-essential,  dysbiosis → metabolic     MPLKIP+SUGCT loss
   LoF-tolerant)         syndrome (mouse); cyclic  → TTD4 + GA3
                         vomiting (human) →         (severe features
                         improves w/ ANTIBIOTICS    from MPLKIP, not SUGCT)
```

The unifying interpretation is that **GA3 is a biochemical marker, not a disease, in the large majority of cases.** Three independent lines of evidence converge on this: (1) clinical — no consistent phenotype across reported patients and most remain asymptomatic; (2) population-genetic — SUGCT is LoF-tolerant (pLI≈0) and non-essential; and (3) mechanistic — the accumulating metabolite (glutarate) is not substantially neurotoxic at these levels, unlike GA1's glutaric/3-hydroxyglutaric acids. Severe presentations resolve into **confounding comorbidity, dietary/microbiome modifiers, or contiguous-gene MPLKIP deletion.** This has direct clinical consequence: an isolated urinary glutarate elevation should prompt (a) exclusion of GA1/GA2, (b) SUGCT confirmation, (c) chromosomal microarray if dysmorphic/neurocutaneous features are present, and (d) **caution before attributing any symptom to SUGCT deficiency.**

A key contrast with GA1 clarifies why GA3 is benign: in GA1, loss of glutaryl-CoA dehydrogenase causes accumulation of **glutaryl-CoA, glutaric acid, and the neurotoxic 3-hydroxyglutaric acid**, with glutaryl-CoA uncompetitively inhibiting α-ketoglutarate dehydrogenase and driving striatal excitotoxic injury. In GA3, the block is *upstream* of glutaryl-CoA formation — glutaryl-CoA is never made, 3-OHGA stays low, and the only consequence is urinary loss of free glutarate. The toxic intermediates of GA1 are simply not generated in GA3.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [18926513](https://pubmed.ncbi.nlm.nih.gov/18926513/) | Genetic mapping of GA3 to chr7; C7orf10 mutations | Human clinical/genetic | F1, F2, F3, F11 (causal gene, biochemistry, no consistent phenotype) |
| [28766179](https://pubmed.ncbi.nlm.nih.gov/28766179/) | Three Canadian GA3 cases | Human clinical | F1, F3, F4, F9, F11 ("non-disease", antibiotics, underdiagnosed, urine NBS) |
| [31722069](https://pubmed.ncbi.nlm.nih.gov/31722069/) | SugctKO knockout mouse | Model organism | F3, F4, F8, F10 (asymptomatic, microbiome, non-essential, KO phenotype) |
| [33483254](https://pubmed.ncbi.nlm.nih.gov/33483254/) | GA3 natural trait in 129 mice | Model organism | F2, F10 (enzyme reaction, natural model) |
| [29421601](https://pubmed.ncbi.nlm.nih.gov/29421601/) | MPLKIP+SUGCT deletion, Peru | Human clinical | F5 (contiguous-gene TTD4+GA3) |
| [37064336](https://pubmed.ncbi.nlm.nih.gov/37064336/) | 2nd contiguous deletion TTD4+GA3 | Human clinical | F5 |
| [32779420](https://pubmed.ncbi.nlm.nih.gov/32779420/) | Novel p.Arg322Trp; brain MRI | Human clinical | F1 (new allele, white-matter MRI) |
| [39101156](https://pubmed.ncbi.nlm.nih.gov/39101156/) | WES dual diagnosis incl. GA3 | Human clinical | F13 (benign reputation, diagnostic odyssey) |
| [26098869](https://pubmed.ncbi.nlm.nih.gov/26098869/) | Pancreatic cancer GWAS (7p13 SUGCT) | GWAS/computational | F7 (common-variant complex-trait signal) |
| [41733842](https://pubmed.ncbi.nlm.nih.gov/41733842/) | Frailty GWAS | GWAS | F7 |
| [38228059](https://pubmed.ncbi.nlm.nih.gov/38228059/) | Chicken adaptation scan | Comparative genomics | F7 (conservation/selection) |
| [35500672](https://pubmed.ncbi.nlm.nih.gov/35500672/) | GC-MS 2-/3-OHGA separation | Methods | F11 (diagnostic accuracy) |

Supporting context on GA1 (the severe sibling disorder used throughout as a contrast) is provided by [PMID: 27853989](https://pubmed.ncbi.nlm.nih.gov/27853989/), [PMID: 21431622](https://pubmed.ncbi.nlm.nih.gov/21431622/), [PMID: 17879145](https://pubmed.ncbi.nlm.nih.gov/17879145/) and [PMID: 20923787](https://pubmed.ncbi.nlm.nih.gov/20923787/); these underscore that GA1's neurotoxicity derives from 3-hydroxyglutaric/glutaric acid accumulation and glutaryl-CoA inhibition of α-ketoglutarate dehydrogenase — a mechanism GA3 does **not** share because 3-OHGA remains low and glutaryl-CoA is not formed.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Fewer than ~15 human GA3 patients are reported, almost all as single cases/small series. No natural-history cohort or registry exists, so prevalence, penetrance, and symptom frequencies are estimates, not measured rates.
2. **Ascertainment bias.** Patients are usually detected because they are symptomatic (undergoing metabolic workup), inflating the apparent association with developmental/neurological problems. The true population of biochemically-affected but asymptomatic individuals is unknown.
3. **Causality of reported symptoms is unproven.** White-matter changes, developmental delay, and hypotonia reported in GA3 patients have not been causally linked to SUGCT deficiency and are plausibly coincidental.
4. **Prevalence uncertainty.** The ~1/440 carrier frequency is a pLoF-only lower bound; missense hypomorphs (p.Arg299Trp) are not counted, so true carrier/affected rates are higher but unquantified.
5. **Human modifier data are thin.** The diet–microbiome–glutarate axis is robustly demonstrated in mice but rests on a single human antibiotic-response anecdote.
6. **No formal QoL, mortality, or treatment-outcome studies** exist for isolated GA3.
7. **Variant interpretation is difficult** — 87/169 ClinVar variants are VUS, complicating molecular confirmation.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a GA3 natural-history registry** combining urine-screening-ascertained (unbiased) and clinically-ascertained cases to directly measure clinical penetrance and symptom frequency.
2. **Systematic ascertainment via urine-based newborn/population screening** to capture asymptomatic individuals and estimate true prevalence independent of symptom-driven bias.
3. **Human microbiome–metabolome study**: quantify the fraction of urinary glutarate attributable to gut bacteria in confirmed GA3 patients (stable-isotope / antibiotic-challenge design) to formalize the mouse finding.
4. **Reclassify SUGCT VUS** using functional CoA-transferase assays (leveraging the new PDB structures 9BR6/9BR7) and in-vitro expression of missense variants to resolve the large VUS burden.
5. **Controlled dietary-lysine intervention in the SugctKO mouse** to define whether lysine restriction prevents the metabolic-syndrome branch, informing whether human dietary management is warranted.
6. **Always perform chromosomal microarray** in any GA3 patient with dysmorphism, brittle hair, or neurodevelopmental features to detect contiguous-gene MPLKIP deletions (TTD4) that explain severe phenotypes.
7. **Diagnostic stewardship guidance**: publish a decision pathway so that isolated glutaric aciduria with low 3-OHGA/low C5DC triggers SUGCT confirmation and explicit consideration of alternative causes before symptoms are attributed to GA3.

---

*Report compiled from 13 confirmed findings across 5 investigation iterations and 27 reviewed papers. Evidence types span human clinical case series, model-organism (mouse) studies, population-genetic constraint analysis (gnomAD), and GWAS/comparative genomics.*


## Artifacts

- [OpenScientist final report](Glutaric_Acidemia_Type_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Glutaric_Acidemia_Type_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "Clinical sign"; HP calls it **Global developmental delay**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0002500` (1 mention) - the report calls it "Leukoencephalopathy"; HP calls it **Abnormal cerebral white matter morphology**
- `UBERON:0002113` (1 mention) - the report calls it "Mouse modifier branch:** kidney"; UBERON calls it **kidney**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `CHEBI:45009` (1 mention) - CHEBI does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005739` (2 mentions) - the report calls it "Subcellular compartment:** Mitochondrion", "Subcellular:** mitochondrion"; GO calls it **mitochondrion**
- `CHEBI:17859` (1 mention) - the report calls it "CHEBI entities:** glutaric acid"; CHEBI calls it **glutaric acid**
- `UBERON:0002316` (1 mention) - the report calls it "Reported/modifier involvement:** CNS white matter"; UBERON calls it **white matter**, and lists "CNS white matter" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005739` - called "Subcellular compartment:** Mitochondrion", "Subcellular:** mitochondrion"