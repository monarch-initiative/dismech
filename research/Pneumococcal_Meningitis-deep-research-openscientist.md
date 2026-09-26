---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T13:00:18.770885'
end_time: '2026-09-25T13:17:34.493128'
duration_seconds: 1035.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pneumococcal Meningitis
  mondo_id: MONDO:0006913
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
citation_count: 45
reference_validation:
  total_references: 46
  verified: 46
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 46
  on_topic: 33
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 42
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0000407
    reported_labels:
    - up to 30% of survivors
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0002181
    reported_labels:
    - ~29% (adults)
    ontology_label: Cerebral edema
  - term_id: HP:0100543
    reported_labels:
    - variable
    ontology_label: Cognitive impairment
  - term_id: UBERON:0002361
    reported_labels:
    - Primary organ/site:** meninges/leptomeninges
    ontology_label: pia mater
  - term_id: UBERON:0001844
    reported_labels:
    - Secondary:** cochlea/inner ear
    ontology_label: cochlea
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pneumococcal_Meningitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pneumococcal_Meningitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pneumococcal Meningitis
- **MONDO ID:** MONDO:0006913 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pneumococcal Meningitis** covering all of the
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

# Pneumococcal Meningitis (MONDO:0006913): A Comprehensive Disease Characteristics Report

## Summary

**Pneumococcal meningitis is an acute, life-threatening bacterial infection of the meninges and cerebrospinal fluid (CSF) caused by a single infectious agent, *Streptococcus pneumoniae* (NCBITaxon:1313).** It is not a genetic disease; rather, it is an infectious disease whose etiology is a human-restricted, encapsulated Gram-positive commensal that ordinarily colonizes the nasopharynx and occasionally invades. The pathogenesis follows a well-characterized causal chain: nasopharyngeal colonization → mucosal/epithelial invasion → bloodstream survival via complement evasion → crossing of the blood–brain barrier (BBB) → unrestricted bacterial multiplication in the CSF → a pneumolysin- and complement-driven neuroinflammatory cascade → hippocampal apoptosis, cortical necrosis, cerebral edema, and cerebrovascular injury → death or long-term neurological sequelae, most commonly sensorineural hearing loss.

Globally, *S. pneumoniae* meningitis (SPM) is a leading cause of bacterial meningitis death and disability-adjusted life years (DALYs), concentrated in children under 5 years, though the burden has fallen substantially since the introduction of pneumococcal conjugate vaccines (PCVs). The disease carries approximately 20–30% in-hospital mortality (with adults faring far worse than children) and leaves roughly 40% of survivors with neurological sequelae. Host susceptibility and outcome are modulated polygenically, concentrated in innate-immune and complement-pathway genes (MBL2, C5, CFH), rather than by Mendelian causal variants.

Management centers on emergency empiric antimicrobial therapy (third-generation cephalosporin plus vancomycin) started within one hour of presentation, plus adjunctive dexamethasone given before or with the first antibiotic dose, which reduces unfavorable outcomes from ~25% to ~15% in adults with the pneumococcal subgroup benefiting most. Prevention rests on pneumococcal conjugate and polysaccharide vaccination, correction of anatomical CSF leaks in recurrent disease, and prophylaxis/vaccination in asplenic and immunocompromised patients. A central emerging challenge is serotype replacement and antimicrobial resistance following widespread PCV use.

---

## Key Findings

### Finding 1 — Global burden: a leading cause of bacterial meningitis death and DALYs, concentrated in young children (F001)

The Global Burden of Disease (GBD) 2021 analysis established that *Streptococcus pneumoniae* meningitis caused **20,718 deaths (95% UI 14,718–29,192) and 1,823,058 DALYs (95% UI 1,301,814–2,561,107)** among people aged 0–19 in 2021, exceeding *Neisseria meningitidis* meningitis (17,389 deaths) in the same population. The burden clustered in children under 5 years. In GBD 2023, *S. pneumoniae* was the **leading pathogen** contributing to child death and DALY loss among children in G20 countries (~66,400 deaths, ages 0–14). Importantly, overall burden fell substantially from 1990 to 2021, driven by epidemiological change attributable to vaccination.

> *"In 2021, SPM caused 20,718 deaths (95% UI 14,718-29,192) and 1,823,058 disability-adjusted life years (DALYs; 95% UI 1,301,814-2,561,107), while NMM caused 17,389 deaths"* — [PMID: 42071803](https://pubmed.ncbi.nlm.nih.gov/42071803/)

> *"Streptococcus pneumoniae was the leading pathogen contributing to death and DALY loss among children in G20 countries"* — [PMID: 42752455](https://pubmed.ncbi.nlm.nih.gov/42752455/)

### Finding 2 — Pathogenesis: a causal chain from nasopharyngeal colonization to inflammatory brain injury (F002)

The mechanistic sequence of pneumococcal meningitis is well described. Infection begins with **nasopharyngeal colonization** by *S. pneumoniae*, which evades mucosal entrapment and host immunity. Invasive disease then proceeds via **epithelial adhesion → bloodstream invasion → activation of complement and coagulation → inflammatory mediators facilitating BBB crossing → free bacterial multiplication in CSF → activation of antigen-presenting and microglial cells → neutrophil recruitment and massive inflammation**, resulting in the hallmark features of bacterial meningitis: CSF pleocytosis, cochlear damage, cerebral edema, hydrocephalus, and cerebrovascular complications.

> *"The release of inflammatory mediators facilitates pneumococcal crossing of the blood-brain barrier into the brain, where the bacteria multiply freely and trigger activation of circulating antigen-presenting cells and resident microglial cells. The resulting massive inflammation leads to further neutrophil recruitment and inflammation, resulting in the well-known features of bacterial meningitis, including cerebrospinal fluid pleocytosis, cochlear damage, cerebral edema, hydrocephalus, and cerebrovascular complications"* — [PMID: 21734248](https://pubmed.ncbi.nlm.nih.gov/21734248/)

### Finding 3 — Pneumolysin: the key virulence factor driving neuronal death (F003)

**Pneumolysin (Ply)** is the principal pneumococcal neurotoxin. Multiple mechanistic studies converge on several complementary pathways:

- **Neuronal adhesion/invasion:** Via its cholesterol-binding domain 4, Ply interacts with neuronal β-actin together with the pilus-1 adhesin RrgA to promote neuronal adhesion, invasion, and death, with increased intracellular Ca²⁺ and actin cytoskeleton disassembly ([PMID: 33760879](https://pubmed.ncbi.nlm.nih.gov/33760879/)).
- **Mitochondrial apoptosis:** Ply localizes to mitochondria, alters membrane potential, and releases apoptosis-inducing factor (AIF), causing caspase-independent neuronal apoptosis ([PMID: 17562768](https://pubmed.ncbi.nlm.nih.gov/17562768/)).
- **Glutamate excitotoxicity:** Ply triggers Ca²⁺-dependent glutamate release from astrocytes, causing NMDA-receptor-dependent synaptic and dendritic damage; the NMDA antagonists MK801 and D-AP5 reduce pathology ([PMID: 23785278](https://pubmed.ncbi.nlm.nih.gov/23785278/)).
- **p38 MAPK signaling:** Ply neurotoxicity involves calcium influx and p38 MAPK activation; the inhibitor SB203580 rescues neurons ([PMID: 12586546](https://pubmed.ncbi.nlm.nih.gov/12586546/)).
- **In vivo requirement:** A pneumolysin-deficient strain showed decreased virulence and longer survival in murine meningitis ([PMID: 12379738](https://pubmed.ncbi.nlm.nih.gov/12379738/)).

> *"pneumococci interact with the cytoskeleton protein β-actin through the pilus-1 adhesin RrgA and the cytotoxin pneumolysin (Ply), thereby promoting adhesion and invasion of neurons, and neuronal death"* — [PMID: 33760879](https://pubmed.ncbi.nlm.nih.gov/33760879/)

> *"Pneumolysin colocalized with mitochondrial membranes, altered the mitochondrial membrane potential, and caused the release of apoptosis-inducing factor and cell death"* — [PMID: 17562768](https://pubmed.ncbi.nlm.nih.gov/17562768/)

### Finding 4 — Adjunctive dexamethasone improves outcomes when timed with antibiotics (F004)

The 2002 European adult trial showed that adjunctive dexamethasone **reduced unfavorable outcomes from 25% to 15%** in bacterial meningitis, with the largest benefit in the pneumococcal subgroup, provided it was given **before or with the first antibiotic dose** ([PMID: 19386456](https://pubmed.ncbi.nlm.nih.gov/19386456/)). A French national pediatric cohort (1,765 confirmed pediatric pneumococcal meningitis cases, 2005–2022) evaluated dexamethasone 0.15 mg/kg every 6 h for 4 days given within 12 h of antibiotics, using propensity-score (IPTW) analysis of 30-day all-cause death ([PMID: 40113367](https://pubmed.ncbi.nlm.nih.gov/40113367/)). The benefit is timing-dependent and attenuated if given late; notably, dexamethasone has **no proven benefit in infants and children** in some analyses (see Finding 12).

> *"This study showed that adjunctive dexamethasone therapy reduced the rate of unfavorable outcomes from 25 to 15% in adults with bacterial meningitis. In this study, adjunctive treatment with dexamethasone was given before or with the first dose of antibiotics"* — [PMID: 19386456](https://pubmed.ncbi.nlm.nih.gov/19386456/)

### Finding 5 — PCVs reduced meningitis but drove non-vaccine serotype replacement (F005)

The PSERENADE project (42 surveillance sites, 30 countries) found that **6 years after PCV10/PCV13 introduction, pneumococcal meningitis incidence declined 48–74% in children <5 y, 35–62% in ages 5–17 y, and 0–36% in adults ≥18 y** — but replacement with non-vaccine serotypes persisted throughout follow-up ([PMID: 39864526](https://pubmed.ncbi.nlm.nih.gov/39864526/)). In Mexico, PCV13-serotype meningitis fell from 77.2% (pre-PCV) to 33.3% (PCV13 era) while non-vaccine serotypes rose to 66.7%, with serotypes 19A and 15B increasing and cefotaxime resistance rising from 22.8% to 30.4% ([PMID: 41223711](https://pubmed.ncbi.nlm.nih.gov/41223711/)). Penicillin non-susceptibility under meningitis breakpoints reaches 85.7% in some settings (Taiwan), though vancomycin susceptibility is preserved ([PMID: 34219043](https://pubmed.ncbi.nlm.nih.gov/34219043/)).

> *"Six years after PCV10/PCV13 introduction, pneumococcal meningitis declined 48-74% across products and PCV7 impact strata for children <5 y, 35-62% for 5-17 y and 0-36% for ≥18 y"* — [PMID: 39864526](https://pubmed.ncbi.nlm.nih.gov/39864526/)

### Finding 6 — High mortality and frequent sequelae; adults worse than children (F006)

A Danish nationwide study (n=187) reported that **21% died in hospital (adults 27% vs children 2%, p<0.001)**, and **41% of survivors had neurological sequelae**; the most common infection focus was the ear (30%) ([PMID: 16253143](https://pubmed.ncbi.nlm.nih.gov/16253143/)). A German adult series (n=87) found in-hospital mortality of 24.1%, intracranial complications in 74.7% (diffuse brain edema 28.7%, hydrocephalus 16.1%, arterial cerebrovascular complications 21.8%), hearing loss in 25.8% of survivors, and only 48.3% with good outcome at discharge ([PMID: 12690042](https://pubmed.ncbi.nlm.nih.gov/12690042/)). In pediatric series, coma, respiratory distress, and shock predicted death or sequelae ([PMID: 8749621](https://pubmed.ncbi.nlm.nih.gov/8749621/)). **Hearing loss is the most common long-term sequela, reported in up to 30% of survivors** ([PMID: 28460251](https://pubmed.ncbi.nlm.nih.gov/28460251/)).

> *"21% of patients died during hospitalisation (adults: 27% vs. children: 2%, Fisher Exact Test, P < 0.001)"* — [PMID: 16253143](https://pubmed.ncbi.nlm.nih.gov/16253143/)

> *"Hearing loss remains the most common long-term complication of pneumococcal meningitis (PM) reported in up to 30% of survivors"* — [PMID: 28460251](https://pubmed.ncbi.nlm.nih.gov/28460251/)

### Finding 7 — Host complement-pathway genetic variation modulates susceptibility and outcome (F007)

Pneumococcal meningitis is **not a Mendelian disease**; genetic risk is polygenic/multifactorial, concentrated in innate-immune and complement genes:

- **MBL2 (mannose-binding lectin):** White individuals homozygous for the defective *MBL2* 0/0 genotype had substantially increased risk (**OR 8.21, 95% CI 1.05–64.1; p=0.017**); meta-analysis of 5 studies OR 2.33 (99% CI 1.39–3.90) ([PMID: 23741476](https://pubmed.ncbi.nlm.nih.gov/23741476/)).
- **C5 (complement component 5):** A common nonsynonymous SNP rs17611 is associated with unfavorable outcome; C5aR-deficient mice had less brain damage, and anti-C5 monoclonal antibodies prevented death in mice ([PMID: 21926466](https://pubmed.ncbi.nlm.nih.gov/21926466/)).
- **CFH (complement factor H):** The major (G) allele of rs6677604 is associated with low CSF factor H and increased mortality ([PMID: 31883521](https://pubmed.ncbi.nlm.nih.gov/31883521/)).
- **C2 deficiency:** Classical-pathway C2 deficiency predisposes to invasive pneumococcal infection ([PMID: 16785571](https://pubmed.ncbi.nlm.nih.gov/16785571/)).

> *"The risk of contracting pneumococcal meningitis was substantially increased for white individuals homozygous with the defective MBL2 0/0 genotype (odds ratio [OR] 8.21, 95% confidence interval [CI] 1.05-64.1; p = 0.017)"* — [PMID: 23741476](https://pubmed.ncbi.nlm.nih.gov/23741476/)

**Suggested HGNC gene annotations:** MBL2 (HGNC:6922), C5 (HGNC:1331), CFH (HGNC:4883), C2 (HGNC:1248).

### Finding 8 — Major predisposing/risk factors (F008)

Repeatedly identified predisposing conditions include otitis/sinusitis (ear focus 30% in the Danish cohort; otitis or sinusitis 22% in those ≥80 y), pneumonia (16%), diabetes mellitus (17%), and advanced age. In patients ≥80 y, *S. pneumoniae* caused 66% of community-acquired bacterial meningitis and case-fatality reached 50% ([PMID: 35352336](https://pubmed.ncbi.nlm.nih.gov/35352336/)). **Asplenia/functional hyposplenism** (sickle cell disease, post-splenectomy) confers markedly increased risk of overwhelming pneumococcal infection because the spleen clears encapsulated bacteria; sickle cell disease, Hodgkin's disease, transplant, myeloma, and nephrotic syndrome are documented high-risk groups ([PMID: 11577367](https://pubmed.ncbi.nlm.nih.gov/11577367/), [PMID: 3070364](https://pubmed.ncbi.nlm.nih.gov/3070364/), [PMID: 7025158](https://pubmed.ncbi.nlm.nih.gov/7025158/)). Neurosurgical procedures and CSF leaks predispose to (often nosocomial) meningitis ([PMID: 36690945](https://pubmed.ncbi.nlm.nih.gov/36690945/)).

> *"Virtually every patient without spleen has a significantly increased risk of severe postsplenectomy infection (mostly caused by Streptococcus pneumoniae)"* — [PMID: 11577367](https://pubmed.ncbi.nlm.nih.gov/11577367/)

### Finding 9 — Acute presentation; the classic triad is often incomplete (F009)

Onset is acute/fulminant. The classic triad (fever, neck stiffness, altered consciousness) is frequently incomplete: in a Danish pre-hospital study of 209 community-acquired bacterial meningitis patients, **only 3% reported all 3 triad symptoms while 85% had ≥1**; the most common symptoms were altered mental state (58%) and fever (57%), with neck stiffness less common (9%) ([PMID: 38052853](https://pubmed.ncbi.nlm.nih.gov/38052853/)). In the Danish pneumococcal meningitis cohort specifically, **fever occurred in 93%, altered mental status in 94%, back/neck rigidity in 57%, headache in 41%, and convulsion in 11%** ([PMID: 16253143](https://pubmed.ncbi.nlm.nih.gov/16253143/)).

> *"Most patients (85%) reported at least 1 of the 3 symptoms in the classical triad of meningitis, while 3% reported all 3"* — [PMID: 38052853](https://pubmed.ncbi.nlm.nih.gov/38052853/)

### Finding 10 — Rodent models recapitulate disease and confirm complement/inflammation as drivers (F010)

Primary models are mouse and rat, induced by direct intracisternal/intracerebral inoculation of *S. pneumoniae* (e.g., strain D39), plus a bacteremia-derived meningitis mouse model; rabbit models were historically important ([PMID: 6397452](https://pubmed.ncbi.nlm.nih.gov/6397452/)). These models reproduce CSF pleocytosis, cerebral edema, BBB disruption, neuronal apoptosis, and hearing loss. Mechanistic interventions: C5aR-deficient mice and anti-C5 mAb reduced CSF leukocytes, brain damage, and death ([PMID: 21926466](https://pubmed.ncbi.nlm.nih.gov/21926466/)); *Cfh* knockout worsened outcome ([PMID: 31883521](https://pubmed.ncbi.nlm.nih.gov/31883521/)); pneumolysin-deficient mutants were less virulent ([PMID: 12379738](https://pubmed.ncbi.nlm.nih.gov/12379738/)); MRP8/14 augmented inflammation via NF-κB/TNF-α/IL-6 ([PMID: 31049785](https://pubmed.ncbi.nlm.nih.gov/31049785/)); and border-associated macrophage depletion worsened disease, an effect abolished with a pneumolysin-deficient mutant ([PMID: 40988032](https://pubmed.ncbi.nlm.nih.gov/40988032/)).

> *"C5a receptor-deficient mice with pneumococcal meningitis had lower CSF wbc counts and decreased brain damage compared with WT mice. Adjuvant treatment with C5-specific monoclonal antibodies prevented death in all mice with pneumococcal meningitis"* — [PMID: 21926466](https://pubmed.ncbi.nlm.nih.gov/21926466/)

### Finding 11 — Diagnosis rests on CSF analysis; CSF lactate is highly accurate; ESCMID guideline governs management (F011)

Lumbar puncture with CSF analysis is the principal diagnostic contributor; clinical features and blood parameters have limited accuracy ([PMID: 28478238](https://pubmed.ncbi.nlm.nih.gov/28478238/)). Typical bacterial CSF shows **neutrophilic pleocytosis, elevated protein, low glucose (low CSF:serum glucose ratio), and positive Gram stain and culture**. CSF lactate differentiates bacterial from aseptic meningitis with **pooled sensitivity 0.93 (95% CI 0.89–0.96) and specificity 0.96 (95% CI 0.93–0.98)**, diagnostic OR 313, optimal cutoff ~35 mg/dL; sensitivity falls to 0.49 after antibiotic pretreatment ([PMID: 21382412](https://pubmed.ncbi.nlm.nih.gov/21382412/)). Multiplex PCR (BioFire ME panel) increases yield: among 368 culture-negative CSF specimens it detected a pathogen in 24.5%, predominantly *S. pneumoniae* ([PMID: 37784010](https://pubmed.ncbi.nlm.nih.gov/37784010/)). The **ESCMID guideline** advises starting empiric treatment within one hour of arrival, with dexamethasone as the only proven adjunct, started with antibiotics ([PMID: 28478238](https://pubmed.ncbi.nlm.nih.gov/28478238/)).

> *"The pooled test characteristics of CSF lactate were sensitivity 0.93 (95% CI: 0.89-0.96), specificity 0.96 (95% CI: 0.93-0.98), likelihood ratio positive 22.9"* — [PMID: 21382412](https://pubmed.ncbi.nlm.nih.gov/21382412/)

> *"cerebrospinal fluid analysis remains the principal contributor to the final diagnosis. The ESCMID guideline advises to start empiric treatment within one hour of arrival"* — [PMID: 28478238](https://pubmed.ncbi.nlm.nih.gov/28478238/)

### Finding 12 — Downstream brain injury: MMPs, ROS, and cytokines produce hippocampal apoptosis and cortical necrosis (F012)

The neuropathological signature of experimental pneumococcal meningitis is **apoptosis in the hippocampal dentate gyrus/subgranular zone plus ischemic necrosis in the cortex** ([PMID: 25890041](https://pubmed.ncbi.nlm.nih.gov/25890041/), [PMID: 30131074](https://pubmed.ncbi.nlm.nih.gov/30131074/)). Matrix metalloproteinases (especially **MMP-9**) mediate BBB breakdown, neutrophil infiltration, and cytokine signaling; MMP inhibitors (BB-94/batimastat, RS-130830, Trocade) reduce cortical necrosis, CSF IL-1β/IL-10, weight loss, and CSF leukocytes ([PMID: 25890041](https://pubmed.ncbi.nlm.nih.gov/25890041/), [PMID: 31172218](https://pubmed.ncbi.nlm.nih.gov/31172218/)). **Reactive oxygen species (ROS)** cause severe neuronal DNA damage and are a major cause of cell death; antioxidant adjuvants (e.g., vitamin B6 modulating APE1) reduce AIF and glutamate ([PMID: 29233148](https://pubmed.ncbi.nlm.nih.gov/29233148/)). Combined non-bacteriolytic antibiotic (daptomycin) + MMP inhibition reduced hippocampal apoptosis and cortical necrosis, lowered TNF-α/IL-1β/IL-6/IL-10, and preserved learning, memory, and hearing in infant rats — where dexamethasone has no proven benefit ([PMID: 30131074](https://pubmed.ncbi.nlm.nih.gov/30131074/)). Fluoxetine also reduced hippocampal apoptosis ([PMID: 25839149](https://pubmed.ncbi.nlm.nih.gov/25839149/)).

> *"Neuropathological correlates of these sequelae are apoptosis in the hippocampal dentate gyrus and necrosis in the cortex. Matrix metalloproteinases (MMPs) play a critical role in the pathophysiology of PM"* — [PMID: 25890041](https://pubmed.ncbi.nlm.nih.gov/25890041/)

> *"The production of reactive oxygen species (ROS) during pneumococcal meningitis (PM) leads to severe DNA damage in the neurons and is the major cause of cell death during infection"* — [PMID: 29233148](https://pubmed.ncbi.nlm.nih.gov/29233148/)

### Finding 13 — Etiology: a single human-restricted encapsulated commensal with defined virulence factors (F013)

The sole causal agent is *Streptococcus pneumoniae* (NCBITaxon:1313), a **Gram-positive, alpha-hemolytic, lancet-shaped diplococcus** that colonizes the human nasopharynx as a commensal and occasionally invades ([PMID: 18981135](https://pubmed.ncbi.nlm.nih.gov/18981135/)). Key virulence factors: the **polysaccharide capsule** (antiphagocytic; basis of >90 serotypes and of conjugate/polysaccharide vaccines), **pneumolysin** (cytolysin/neurotoxin), **neuraminidases (NanA)**, **hyaluronidase**, and **choline-binding protein A (CbpA/PspC)**, which recruits complement factor H for immune evasion. CbpA binds **human** factor H but not mouse or other tested animal FH, and deleting the FH-binding domain did not alter virulence in mice — evidence that *S. pneumoniae* is adapted specifically to the human host ([PMID: 18981135](https://pubmed.ncbi.nlm.nih.gov/18981135/)). Meningitis serotype distributions shift with vaccination (pre-PCV common types 3, 14, 19F, 23F, 6B; emerging non-vaccine types 19A, 15B, 35B, 24).

> *"CbpA binds to human FH, but not to the FH proteins of mouse and other animal species tested to date"* — [PMID: 18981135](https://pubmed.ncbi.nlm.nih.gov/18981135/)

> *"Pneumolysin, neuraminidases A and B, and hyaluronidase are virulence factors of Streptococcus pneumoniae that appear to be involved in the pathogenesis of meningitis"* — [PMID: 12379738](https://pubmed.ncbi.nlm.nih.gov/12379738/)

### Finding 14 — Modifiable risk factors and anatomical defects drive risk and recurrence; prevention combines vaccination and prophylaxis (F014)

**HIV** is a dominant modifiable risk factor: bacteremic pneumococcal disease is **~41-fold higher** in HIV-infected individuals ([PMID: 10501310](https://pubmed.ncbi.nlm.nih.gov/10501310/)); HIV also increases colonization (adjusted OR 1.6) and invasive pneumococcal pneumonia (adjusted OR 3.2) ([PMID: 24907383](https://pubmed.ncbi.nlm.nih.gov/24907383/)). Other risk factors include cigarette smoking, dementia, seizure disorders, congestive heart failure, COPD, institutionalization/crowding, and alcohol ([PMID: 10501310](https://pubmed.ncbi.nlm.nih.gov/10501310/)). Respiratory virus coinfection (influenza, adenovirus, rhinovirus) increases nasopharyngeal pneumococcal density, promoting invasion ([PMID: 24907383](https://pubmed.ncbi.nlm.nih.gov/24907383/)). **Recurrent** pneumococcal meningitis is characteristically caused by a persistent CSF leak or anatomical defect (e.g., temporal-bone/Mondini dysplasia, dural defect, cochlear implant); identifying and surgically correcting the leak prevents recurrence ([PMID: 966915](https://pubmed.ncbi.nlm.nih.gov/966915/)). Prevention: PPV23 reduced adult pneumococcal mortality especially in those ≥65 y ([PMID: 21387956](https://pubmed.ncbi.nlm.nih.gov/21387956/)); conjugate vaccines reduce meningitis and carriage ([PMID: 39864526](https://pubmed.ncbi.nlm.nih.gov/39864526/)); asplenic/immunocompromised patients receive vaccination plus antibiotic prophylaxis.

> *"The rate of pneumococcal bacteremic pneumonia is higher in blacks than in whites and 41 times higher in those with human immunodeficiency virus (HIV) infection"* — [PMID: 10501310](https://pubmed.ncbi.nlm.nih.gov/10501310/)

> *"any abnormality which predisposes a patient to a recurrence of this serious disease, must be identified and corrected"* — [PMID: 966915](https://pubmed.ncbi.nlm.nih.gov/966915/)

---

## Report by Template Section

### 1. Disease Information

**Overview.** Pneumococcal meningitis is an acute purulent (bacterial) infection of the leptomeninges and CSF caused by *Streptococcus pneumoniae* (the pneumococcus). It is the most common and most lethal cause of community-acquired bacterial meningitis in adults and a leading cause in children. The information is aggregated at the disease level from clinical cohorts, national surveillance registries, and GBD modeling — not primarily from individual-patient EHR resources, although national cohort studies (Denmark, Netherlands, France) contribute patient-level data.

**Key identifiers:**
- **MONDO:** MONDO:0006913
- **MeSH:** *Meningitis, Pneumococcal* (D008586)
- **ICD-10:** G00.1 (Pneumococcal meningitis)
- **ICD-11:** 1D01.0 (Bacterial meningitis) with *S. pneumoniae* as agent
- **SNOMED CT:** Pneumococcal meningitis (disorder)
- OMIM/Orphanet: Not a Mendelian disorder; no distinct OMIM entry (host susceptibility loci exist, e.g., complement genes).

**Synonyms:** Pneumococcal meningitis; *Streptococcus pneumoniae* meningitis; SPM; meningitis due to pneumococcus.

### 2. Etiology

**Causal factor:** A single infectious agent — *Streptococcus pneumoniae* (F013). This is fundamentally an infectious, not genetic, disease.

**Genetic risk factors (host):** Polygenic/multifactorial, concentrated in complement/innate-immune genes — *MBL2* (OR 8.21 for 0/0 genotype), *C5* (rs17611), *CFH* (rs6677604), and classical-pathway *C2* deficiency (F007).

**Environmental/modifiable risk factors (F008, F014):** extremes of age; contiguous foci (otitis media, sinusitis, mastoiditis) and distant foci (pneumonia, endocarditis); asplenia/hyposplenism; diabetes mellitus; HIV (~41× risk); smoking; alcohol; COPD; CHF; institutionalization/crowding; respiratory viral coinfection; CSF leak/skull-base defects; neurosurgery/cochlear implants.

**Protective factors:** Vaccination (PCV, PPV23); intact splenic function; the IgG2 allotype G2M(n) is protective against severe infection in C2 deficiency ([PMID: 16785571](https://pubmed.ncbi.nlm.nih.gov/16785571/)); in one influenza-SARI study, completed PCV schedule in children <5 y was associated with decreased hospitalization risk ([PMID: 27720448](https://pubmed.ncbi.nlm.nih.gov/27720448/)).

**Gene–environment interactions:** Complement-gene deficiency (MBL2/C2/CFH) combines with encapsulated-bacterium exposure and asplenia to amplify invasive risk; HIV/viral coinfection raise colonization density that intersects with host complement capacity to determine invasion.

### 3. Phenotypes

| Phenotype | Type | Frequency (PM cohorts) | Suggested HPO |
|---|---|---|---|
| Fever | Symptom/sign | 93% | HP:0001945 |
| Altered mental status | Sign | 94% | HP:0011446 / HP:0001259 (coma) |
| Neck stiffness / nuchal rigidity | Sign | 57% | HP:0031179 |
| Headache | Symptom | 41% | HP:0002315 |
| Seizure/convulsion | Sign | 11% | HP:0001250 |
| Sensorineural hearing loss (sequela) | Manifestation | up to 30% of survivors | HP:0000407 |
| Cerebral edema | Manifestation | ~29% (adults) | HP:0002181 |
| Hydrocephalus | Manifestation | ~16% | HP:0000238 |
| Cognitive/learning impairment | Sequela | variable | HP:0100543 |

Onset is **acute** (childhood peak, but all ages). Severity is **severe**. The classic triad is usually incomplete (only 3% have all three; 85% have ≥1). Quality-of-life impact is dominated by hearing loss (requiring hearing aids/cochlear implants) and cognitive/learning disability, particularly detrimental in infants and children (F006, F009, F012).

### 4. Genetic/Molecular Information

No causal (Mendelian) gene. **Host susceptibility/modifier genes** (F007): *MBL2* (HGNC:6922), *C5* (HGNC:1331; rs17611 nonsynonymous, associated with outcome), *CFH* (HGNC:4883; rs6677604), *C2* (HGNC:1248; classical-pathway deficiency). *MBL2* variants are loss-of-function for lectin-pathway activation; the *CFH* variant lowers CSF factor H. Variant origin is **germline**; these are common population polymorphisms/deficiency alleles, not somatic. No epigenetic disease-defining signature or chromosomal abnormality is established for the host. **Pathogen genetics** (capsule locus determining >90 serotypes; *ply*, *nanA*, *cbpA/pspC*) are the operative "molecular" determinants of virulence (F003, F013).

### 5. Environmental Information

**Infectious agent:** *S. pneumoniae* (NCBITaxon:1313) — the necessary and sufficient cause (F013). **Lifestyle:** smoking, alcohol, crowding/institutional living (F014). **Environmental/host exposures:** respiratory viral coinfection raising nasopharyngeal density; HIV; asplenia; anatomical CSF leak (F008, F014). No classical toxin/pollutant etiology.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1.  S. pneumoniae colonizes the human nasopharynx (capsule + adhesins)         [F002, F013]
        │  leads to
2.  Capsule/CbpA-mediated complement evasion permits mucosal + epithelial
    invasion and bloodstream survival (bacteremia)                            [F013]
        │  leads to
3.  Circulating pneumococci + inflammatory mediators disrupt the BBB and
    the bacteria CROSS into the CSF                                           [F002]
        │  leads to
4.  Bacteria multiply FREELY in CSF (complement/antibody-poor compartment)    [F002]
        │  leads to
5.  Pneumolysin release → pore formation, Ca2+ influx, mitochondrial AIF
    release, astrocytic glutamate/NMDA excitotoxicity, p38 MAPK activation    [F003]
        │  in parallel
6.  Complement (C5a/C5aR) + microglial/macrophage activation → neutrophil
    influx and massive CSF inflammation                                       [F002, F007, F010]
        │  leads to
7.  Downstream effectors: MMP-9 → BBB breakdown; ROS → neuronal DNA damage;
    cytokines TNF-α/IL-1β/IL-6                                                [F012]
        │  branches to
8a. Hippocampal dentate-gyrus APOPTOSIS      8b. Cortical ischemic NECROSIS   [F012]
    + cerebral edema, hydrocephalus, cerebrovascular (vasculitic) injury      [F002, F006]
        │  leads to
9.  Clinical manifestation: death (~20–30%) OR survival with sequelae
    (~40%), predominantly sensorineural hearing loss, cognitive/learning
    impairment, focal neurological deficits                                   [F006, F012]
```

**Molecular pathways/processes:** complement cascade (C5a–C5aR), NF-κB → TNF-α/IL-6 (MRP8/14 amplified), p38 MAPK, NMDA-receptor glutamate excitotoxicity, MMP proteolysis, ROS/oxidative DNA damage, caspase-independent (AIF) and caspase-dependent apoptosis. **Suggested GO terms:** inflammatory response (GO:0006954), complement activation (GO:0006956), neutrophil chemotaxis (GO:0030593), apoptotic process (GO:0006915), response to oxidative stress (GO:0006979), extracellular matrix disassembly (GO:0022617). **Suggested CL terms:** neuron (CL:0000540), microglial cell (CL:0000129), astrocyte (CL:0000127), neutrophil (CL:0000775), macrophage (CL:0000235), brain microvascular endothelial cell (CL:1001568). **CHEBI:** glutamate (CHEBI:14321), calcium(2+) (CHEBI:29108), reactive oxygen species (CHEBI:26523), dexamethasone (CHEBI:41879).

### 7. Anatomical Structures Affected

- **Primary organ/site:** meninges/leptomeninges (UBERON:0002361) and CSF (UBERON:0001359) of the brain (UBERON:0000955); central nervous system (UBERON:0001017).
- **Secondary:** cochlea/inner ear (UBERON:0001844) → hearing loss; cerebral cortex (UBERON:0000956) → necrosis; hippocampal dentate gyrus (UBERON:0001885) → apoptosis; cerebral ventricles → hydrocephalus; cerebral vasculature → vasculitis/infarction.
- **Body systems:** nervous system (primary); also respiratory (portal of entry/pneumonia), auditory, cardiovascular (cerebrovascular complications, endocarditis foci).
- **Tissue/cell level:** nervous tissue (neurons, astrocytes, microglia), leptomeningeal epithelium, brain microvascular endothelium; infiltrating neutrophils and macrophages.
- **Subcellular (GO CC):** mitochondrion (GO:0005739; pneumolysin target), plasma membrane (GO:0005886; pore formation), nucleus (GO:0005634; ROS DNA damage).
- **Localization/lateralization:** typically **bilateral/diffuse** meningeal involvement; focal cerebrovascular complications may be unilateral/asymmetric.

### 8. Temporal Development

**Onset:** acute to fulminant (hours to 1–2 days); can affect any age, with childhood (especially <5 y) and elderly (≥65–80 y) peaks. **Course:** rapidly progressive if untreated; a medical emergency requiring treatment within 1 hour. **Duration:** acute, self-limited if treated (10–21 days IV antibiotics), but long-term/permanent sequelae in survivors. **Critical period:** the window before/at first antibiotic dose for dexamethasone efficacy; delayed cerebral vasculopathy can appear 1–8 days after completing dexamethasone ([PMID: 32531430](https://pubmed.ncbi.nlm.nih.gov/32531430/)). **Recurrence:** episodic recurrence signals an anatomical CSF leak (F014).

### 9. Inheritance and Population

**Epidemiology:** Leading bacterial-meningitis pathogen for child mortality/DALYs; burden concentrated in <5 y; declining with PCV rollout (F001, F005). In the elderly (≥80 y), *S. pneumoniae* causes 66% of community-acquired bacterial meningitis with case-fatality up to 50% (F008). **Inheritance:** Not applicable (infectious disease); host susceptibility is **multifactorial/polygenic** (complement genes). **Penetrance/expressivity/anticipation:** not applicable. **Geographic distribution:** worldwide; highest burden in low-income, low-vaccine-coverage settings; serotype distribution varies regionally and with vaccine era. **Sex/age:** slight male predominance reported in some pediatric series; bimodal age distribution (young children + elderly).

### 10. Diagnostics

- **CSF analysis (principal):** neutrophilic pleocytosis, elevated protein, low glucose/low CSF:serum glucose ratio, positive Gram stain (Gram-positive diplococci) and culture (F011). LOINC panels apply (CSF WBC, glucose, protein, lactate, culture).
- **CSF lactate:** sensitivity 0.93 / specificity 0.96 (cutoff ~35 mg/dL); falls to 0.49 after antibiotics (F011).
- **Molecular:** multiplex PCR (BioFire ME panel) increases yield in culture-negative CSF (24.5% positivity) (F011); pneumococcal antigen detection.
- **Blood:** cultures, CBC, inflammatory markers.
- **Imaging:** CT/MRI for complications (edema, hydrocephalus, infarction, abscess) and to identify skull-base/CSF-leak defects in recurrence.
- **Clinical criteria:** ESCMID guideline — empiric treatment within 1 hour; differential diagnosis includes meningococcal, *H. influenzae*, *Listeria*, staphylococcal, tuberculous, and viral/aseptic meningitis (distinguished by CSF profile, lactate, Gram stain, PCR).
- **Genetic/omics testing:** not routine; complement function testing (CH50/AH50, MBL levels) may be indicated in recurrent/invasive disease.

### 11. Outcome/Prognosis

- **Mortality:** ~21–24% in-hospital overall; adults 27% vs children 2%; up to 50% in the very elderly (F006, F008).
- **Sequelae:** ~40% of survivors; hearing loss the most common (up to 30%); also cognitive/learning impairment, focal deficits, epilepsy, hydrocephalus (F006, F012).
- **Prognostic factors:** age (adult/elderly worse), coma, shock, respiratory distress, CSF findings (high protein, very low glucose), delayed treatment, bacterial load, complement genotype (CFH G allele → higher mortality) (F006, F007, F008).
- **Complications:** cerebral edema, hydrocephalus, cerebrovascular/delayed vasculopathy, seizures, sepsis (F006).

### 12. Treatment

- **Empiric antibiotics:** third-generation cephalosporin (ceftriaxone/cefotaxime) **plus vancomycin** (to cover penicillin/cephalosporin non-susceptibility), started within 1 hour (F005, F011). Vancomycin susceptibility is preserved even where penicillin non-susceptibility is high (F005). NCIT: Ceftriaxone (C548), Vancomycin (C1276).
- **Adjunctive dexamethasone** (NCIT: C557): 0.15 mg/kg q6h ×4 days, before/with first antibiotic; reduces unfavorable outcome 25%→15% in adults; timing-critical; unproven benefit in children (F004, F012).
- **Supportive/ICU care:** management of raised ICP, seizures, cerebral edema; hearing assessment and rehabilitation (cochlear implants).
- **Experimental/adjunctive (preclinical):** anti-C5/C5aR agents (prevented death in mice), MMP inhibitors, non-bacteriolytic antibiotics (daptomycin), antioxidants (vitamin B6/APE1), fluoxetine — several preserved cognition/hearing in infant-rat models where dexamethasone fails (F007, F010, F012). These are not yet standard clinical therapy.

### 13. Prevention

- **Primary — Immunization:** pneumococcal conjugate vaccines (PCV10/PCV13/PCV20) reduce meningitis 48–74% in <5 y and reduce carriage; PPV23 reduces adult mortality in ≥65 y (F005, F014). Ongoing serotype replacement and rising resistance motivate higher-valency vaccines (PCV20) and surveillance.
- **Secondary:** rapid recognition/treatment; complement/immune workup after invasive disease.
- **Tertiary:** correction of CSF leaks to prevent recurrence; hearing screening and rehabilitation; ESCMID recommends post-recovery pneumococcal vaccination (F011, F014).
- **Prophylaxis:** antibiotic prophylaxis (penicillin) plus vaccination in asplenic/sickle-cell/immunocompromised patients (F008, F014).
- **Public health/behavioral:** smoking cessation, HIV control/ART, reduce crowding.

### 14. Other Species / Natural Disease

*S. pneumoniae* is **human-restricted/host-adapted** (CbpA binds human but not animal factor H; deleting the FH-binding domain did not alter virulence in mice — F013). Natural pneumococcal meningitis in companion animals/wildlife is not a recognized entity; the disease is essentially human. Animal involvement is limited to experimental infection (see Section 15). Zoonotic transmission is not a feature. **NCBI Taxon:** *Streptococcus pneumoniae* 1313; host *Homo sapiens* 9606; experimental hosts *Mus musculus* 10090, *Rattus norvegicus* 10116, *Oryctolagus cuniculus* 9986.

### 15. Model Organisms

- **Mouse** (intracisternal/intracerebral or bacteremia-derived; strain D39): recapitulates pleocytosis, edema, BBB disruption, neuronal apoptosis, hearing loss; supports genetic dissection (*Cfh*⁻/⁻, *C5ar*⁻/⁻, *Bdnf* conditional KO) and anti-C5 therapy (F007, F010) — [PMID: 21926466](https://pubmed.ncbi.nlm.nih.gov/21926466/), [PMID: 31883521](https://pubmed.ncbi.nlm.nih.gov/31883521/), [PMID: 32676082](https://pubmed.ncbi.nlm.nih.gov/32676082/), [PMID: 40988032](https://pubmed.ncbi.nlm.nih.gov/40988032/).
- **Infant rat** (intracisternal): the standard model for hippocampal apoptosis + cortical necrosis and for testing adjuvant neuroprotection (MMP inhibitors, daptomycin, fluoxetine, vitamin B6) (F012) — [PMID: 30131074](https://pubmed.ncbi.nlm.nih.gov/30131074/), [PMID: 25890041](https://pubmed.ncbi.nlm.nih.gov/25890041/), [PMID: 25839149](https://pubmed.ncbi.nlm.nih.gov/25839149/).
- **Rabbit:** historically important for BBB/CSF pathophysiology (F010) — [PMID: 6397452](https://pubmed.ncbi.nlm.nih.gov/6397452/).
- **In vitro:** SH-SY5Y neuroblastoma, hippocampal organotypic cultures, organ-of-Corti explants, human brain microvascular endothelial cells (F003).

**Phenotype recapitulation:** strong for CSF inflammation, edema, the apoptosis/necrosis dichotomy, and hearing loss. **Limitations:** host restriction means mouse/rat complement (factor H) does not bind CbpA, so some human-specific evasion mechanisms are not modeled; dexamethasone's differential efficacy (adults vs infants) highlights translational gaps.

---

## Mechanistic Model / Interpretation

The disease is best understood as a **two-hit, two-arm process**. The first hit is *pathogen-intrinsic*: pneumolysin directly kills neurons (mitochondrial AIF, Ca²⁺/pore, glutamate excitotoxicity, p38 MAPK). The second, parallel arm is *host-inflammatory*: complement (C5a–C5aR) and microglial/macrophage activation recruit neutrophils, whose products (MMP-9, ROS, cytokines) break the BBB and injure brain tissue. These two arms converge on a stereotyped neuropathology — **dentate-gyrus apoptosis + cortical necrosis** — that is the substrate for the two dominant clinical outcomes (death; hearing loss/cognitive impairment).

This model explains the therapeutic landscape: antibiotics kill bacteria but, if bacteriolytic, release more pneumolysin and cell-wall inflammogens; dexamethasone dampens the host-inflammatory arm (effective in adults, timing-critical); and the most promising experimental adjuvants (anti-C5/C5aR, MMP inhibitors, antioxidants, non-bacteriolytic antibiotics) each target a specific downstream node. It also explains host genetics: complement-gene variants (MBL2/C2 upstream; C5/CFH downstream) tune both susceptibility (opsonization/clearance) and injury (C5a-driven neutrophilic inflammation).

| Arm | Key mediators | Upstream/downstream | Intervention |
|---|---|---|---|
| Pathogen-direct | Pneumolysin, Ca²⁺, glutamate, AIF | Upstream toxin | Non-bacteriolytic abx; NMDA antagonists (preclinical) |
| Host-inflammatory | C5a/C5aR, NF-κB, TNF-α/IL-1β/IL-6 | Upstream inflammation | Dexamethasone; anti-C5 (preclinical) |
| Tissue-effector | MMP-9, ROS | Downstream injury | MMP inhibitors, antioxidants (preclinical) |

---

## Evidence Base

| PMID | Contribution | Relation to findings |
|---|---|---|
| [42071803](https://pubmed.ncbi.nlm.nih.gov/42071803/) | GBD 2021 SPM burden | Supports F001 |
| [42752455](https://pubmed.ncbi.nlm.nih.gov/42752455/) | Leading child pathogen, G20 | Supports F001 |
| [21734248](https://pubmed.ncbi.nlm.nih.gov/21734248/) | Pathogenesis review | Supports F002 |
| [33760879](https://pubmed.ncbi.nlm.nih.gov/33760879/) | Ply/RrgA–β-actin | Supports F003 |
| [17562768](https://pubmed.ncbi.nlm.nih.gov/17562768/) | Ply mitochondrial apoptosis | Supports F003 |
| [23785278](https://pubmed.ncbi.nlm.nih.gov/23785278/) | Ply glutamate excitotoxicity | Supports F003 |
| [12379738](https://pubmed.ncbi.nlm.nih.gov/12379738/) | Ply-deficient avirulence; virulence factors | Supports F003, F013 |
| [19386456](https://pubmed.ncbi.nlm.nih.gov/19386456/) | Dexamethasone 25→15% | Supports F004 |
| [40113367](https://pubmed.ncbi.nlm.nih.gov/40113367/) | Pediatric dexamethasone cohort | Supports F004 |
| [39864526](https://pubmed.ncbi.nlm.nih.gov/39864526/) | PSERENADE PCV impact | Supports F005, F014 |
| [41223711](https://pubmed.ncbi.nlm.nih.gov/41223711/) | Serotype replacement Mexico | Supports F005 |
| [34219043](https://pubmed.ncbi.nlm.nih.gov/34219043/) | Penicillin non-susceptibility | Supports F005 |
| [16253143](https://pubmed.ncbi.nlm.nih.gov/16253143/) | Danish cohort mortality/symptoms | Supports F006, F009 |
| [12690042](https://pubmed.ncbi.nlm.nih.gov/12690042/) | Adult complications | Supports F006 |
| [28460251](https://pubmed.ncbi.nlm.nih.gov/28460251/) | Hearing loss leading sequela | Supports F006 |
| [23741476](https://pubmed.ncbi.nlm.nih.gov/23741476/) | MBL2 susceptibility | Supports F007 |
| [21926466](https://pubmed.ncbi.nlm.nih.gov/21926466/) | C5/C5aR outcome + therapy | Supports F007, F010 |
| [31883521](https://pubmed.ncbi.nlm.nih.gov/31883521/) | CFH mortality | Supports F007, F010 |
| [11577367](https://pubmed.ncbi.nlm.nih.gov/11577367/) | Asplenia risk | Supports F008 |
| [35352336](https://pubmed.ncbi.nlm.nih.gov/35352336/) | Elderly predisposition | Supports F008 |
| [38052853](https://pubmed.ncbi.nlm.nih.gov/38052853/) | Incomplete triad | Supports F009 |
| [40988032](https://pubmed.ncbi.nlm.nih.gov/40988032/) | BAM depletion/Ply model | Supports F010 |
| [21382412](https://pubmed.ncbi.nlm.nih.gov/21382412/) | CSF lactate accuracy | Supports F011 |
| [28478238](https://pubmed.ncbi.nlm.nih.gov/28478238/) | ESCMID guideline | Supports F011 |
| [37784010](https://pubmed.ncbi.nlm.nih.gov/37784010/) | Multiplex PCR yield | Supports F011 |
| [30131074](https://pubmed.ncbi.nlm.nih.gov/30131074/) | Daptomycin+MMPi; sequelae | Supports F012 |
| [25890041](https://pubmed.ncbi.nlm.nih.gov/25890041/) | MMP/RS-130830; apoptosis/necrosis | Supports F012 |
| [29233148](https://pubmed.ncbi.nlm.nih.gov/29233148/) | ROS/APE1/vitamin B6 | Supports F012 |
| [18981135](https://pubmed.ncbi.nlm.nih.gov/18981135/) | CbpA human-restricted FH binding | Supports F013 |
| [10501310](https://pubmed.ncbi.nlm.nih.gov/10501310/) | HIV 41× risk | Supports F014 |
| [24907383](https://pubmed.ncbi.nlm.nih.gov/24907383/) | Viral coinfection/density | Supports F014 |
| [966915](https://pubmed.ncbi.nlm.nih.gov/966915/) | CSF-leak recurrence | Supports F014 |

---

## Limitations and Knowledge Gaps

1. **Human vs model translation.** *S. pneumoniae* is human-restricted (host-specific factor H binding), so rodent models cannot fully capture complement-evasion biology; the sharpest example is dexamethasone's proven adult benefit but unproven pediatric benefit.
2. **No human clinical trials for the most promising adjuvants.** Anti-C5/C5aR, MMP inhibitors, antioxidants, and non-bacteriolytic antibiotics are supported only by animal/in-vitro data; timing of MMP inhibition is critical because MMPs also aid neuroregeneration.
3. **Host-genetics evidence is modest.** MBL2/C5/CFH associations derive from candidate-gene studies with wide confidence intervals (e.g., MBL2 OR 8.21, 95% CI 1.05–64.1); no large GWAS of pneumococcal meningitis susceptibility was identified.
4. **Serotype/resistance dynamics are moving targets.** Replacement serotypes (19A, 15B, 35B) and rising cephalosporin resistance under meningitis breakpoints threaten current empiric regimens and vaccine coverage.
5. **Sequelae quantification** relies on heterogeneous cohorts; standardized long-term (especially neurocognitive and audiologic) follow-up data are limited.
6. **Quality-of-life instruments** (EQ-5D/SF-36/PROMIS) specific to pneumococcal meningitis survivors were not identified in the reviewed literature.

---

## Proposed Follow-up Experiments / Actions

1. **Clinical translation of complement-targeted adjuvants:** design a phase 2 trial of a C5a/C5aR antagonist (sparing membrane-attack-complex to avoid increasing meningococcal susceptibility) as adjunct to standard therapy, stratified by *CFH*/*C5* genotype.
2. **Pediatric adjuvant trial:** evaluate non-bacteriolytic antibiotic (daptomycin) ± MMP inhibition in children, where dexamethasone lacks proven benefit, with hearing and neurocognition as primary endpoints.
3. **Host-genetics GWAS/meta-analysis:** pool national cohorts (Denmark, Netherlands, France) for a properly powered GWAS of susceptibility and outcome, validating MBL2/C5/CFH and discovering new loci.
4. **Surveillance integration:** couple PSERENADE-style serotype/resistance surveillance with genomic typing to guide PCV20+ formulation and empiric-therapy updates.
5. **Biomarker development:** prospectively validate CSF lactate, MMP-9, and complement activation fragments (C5a) as prognostic biomarkers for sequelae, enabling early neuroprotective intervention.
6. **Recurrence workup protocol:** standardize imaging (high-resolution temporal-bone CT/MRI) and complement/immune testing after invasive pneumococcal disease to detect correctable CSF leaks and immunodeficiency.
7. **Humanized models:** develop factor-H-humanized mice to better model CbpA-mediated complement evasion and test human-specific therapeutics.

---

## Consensus Answer

Pneumococcal meningitis is an acute, life-threatening infection of the meninges and CSF caused by the human-restricted commensal *Streptococcus pneumoniae*, in which nasopharyngeal colonization progresses through complement-evading bacteremia and blood–brain-barrier crossing to unrestricted CSF multiplication, triggering a pneumolysin- and complement-driven neuroinflammatory cascade (MMP-9, ROS, TNF-α/IL-1β/IL-6) that produces hippocampal dentate-gyrus apoptosis, cortical necrosis, cerebral edema, and cerebrovascular injury. It carries ~20–30% mortality and ~40% sequelae (most often sensorineural hearing loss), with host susceptibility being polygenic and centered on complement genes (MBL2, C5, CFH). It is managed with urgent third-generation cephalosporin plus vancomycin and adjunctive dexamethasone (lowering mortality/unfavorable outcome from ~25% to ~15% in adults) and prevented primarily by pneumococcal conjugate/polysaccharide vaccination.


## Artifacts

- [OpenScientist final report](Pneumococcal_Meningitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pneumococcal_Meningitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 46 |
| On topic | 33 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000407` (1 mention) - the report calls it "up to 30% of survivors"; HP calls it **Sensorineural hearing impairment**
- `HP:0002181` (1 mention) - the report calls it "~29% (adults)"; HP calls it **Cerebral edema**
- `HP:0100543` (1 mention) - the report calls it "variable"; HP calls it **Cognitive impairment**
- `UBERON:0002361` (1 mention) - the report calls it "Primary organ/site:** meninges/leptomeninges"; UBERON calls it **pia mater**
- `UBERON:0001844` (1 mention) - the report calls it "Secondary:** cochlea/inner ear"; UBERON calls it **cochlea**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1313` (3 mentions) - the report calls it "Streptococcus pneumoniae", "S. pneumoniae"; NCBITaxon calls it **Streptococcus pneumoniae**, and lists "Diplococcus pneumoniae" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:1313` - called "Streptococcus pneumoniae", "S. pneumoniae"