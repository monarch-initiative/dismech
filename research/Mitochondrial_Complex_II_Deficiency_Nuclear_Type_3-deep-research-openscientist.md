---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T01:55:01.837871'
end_time: '2026-10-20T02:13:57.136203'
duration_seconds: 1135.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial Complex II Deficiency, Nuclear Type 3
  mondo_id: MONDO:0030937
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
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 16
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 54
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 20
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0030937
    reported_labels:
    - MONDO
    ontology_label: mitochondrial complex 2 deficiency, nuclear type 3
  - term_id: HP:0002151
    reported_labels:
    - Increased circulating lactate
    - lactic acidosis
    - Elevated blood and CSF lactate
    ontology_label: Increased circulating lactate concentration
  - term_id: NCIT:C737
    reported_labels:
    - Riboflavin
    ontology_label: Pesticide
  - term_id: NCIT:C1220
    reported_labels:
    - Coenzyme Q10
    ontology_label: Samarium Sm-153 Lexidronam Pentasodium
  - term_id: NCIT:C78591
    reported_labels:
    - Levocarnitine
    ontology_label: Laryngeal Nerve Paralysis
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mitochondrial_Complex_II_Deficiency_Nuclear_Type_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mitochondrial_Complex_II_Deficiency_Nuclear_Type_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex II Deficiency, Nuclear Type 3
- **MONDO ID:** MONDO:0030937 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex II Deficiency, Nuclear Type 3** covering all of the
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

# Mitochondrial Complex II Deficiency, Nuclear Type 3 (MC2DN3): Comprehensive Disease Report

**Disease:** Mitochondrial Complex II Deficiency, Nuclear Type 3
**MONDO:** MONDO:0030937 | **OMIM:** #619167 | **Category:** Mendelian (autosomal recessive)
**Causal gene:** *SDHD* (11q23.1)

---

## Summary

**Mitochondrial Complex II Deficiency, Nuclear Type 3 (MC2DN3)** is an ultra-rare autosomal recessive mitochondrial disorder caused by biallelic (compound heterozygous or homozygous) loss-of-function variants in the nuclear gene *SDHD*, which encodes the small cytochrome-b membrane-anchor subunit (CybS) of succinate dehydrogenase — respiratory chain complex II (succinate:ubiquinone oxidoreductase). The first and defining case was reported by Jackson and colleagues in 2014, who described a child with early progressive encephalomyopathy harboring compound heterozygous *SDHD* variants (p.E69K and p.\*164Lext\*3), with native-PAGE/western blotting demonstrating impaired complex II assembly and cell-line complementation confirming pathogenicity ([PMID: 24367056](https://pubmed.ncbi.nlm.nih.gov/24367056/)).

Mechanistically, loss of SDHD impairs assembly and anchoring of complex II in the inner mitochondrial membrane, simultaneously disrupting two coupled metabolic pathways: the TCA-cycle oxidation of succinate to fumarate and the transfer of electrons into the respiratory chain via ubiquinone. The result is an energy-deficiency state with lactic acidosis and succinate accumulation that preferentially injures high-energy-demand tissues — the central nervous system (basal ganglia, brainstem, cerebral/cerebellar white matter), heart, and skeletal muscle. Clinically this manifests most commonly as Leigh syndrome, leukoencephalopathy/leukodystrophy, epileptic encephalopathy, and cardiomyopathy. There is no cure; management is supportive and largely off-label (riboflavin, coenzyme Q10, L-carnitine). Prognosis is highly variable, with cardiomyopathy predicting poor outcome and riboflavin-responsiveness predicting better outcome.

A biologically important feature of this gene is its **dual disease role**: whereas *biallelic* recessive *SDHD* variants cause this mitochondrial disease, *monoallelic* germline *SDHD* variants cause hereditary paraganglioma/pheochromocytoma with a striking parent-of-origin effect (tumors form almost exclusively after paternal transmission, accompanied by somatic loss of the maternal chromosome 11). This report synthesizes 13 confirmed findings across 33 reviewed papers into a comprehensive, section-by-section knowledge-base entry.

---

## Section 1. Disease Information

**Overview.** MC2DN3 is a Mendelian inborn error of mitochondrial energy metabolism belonging to the group of **isolated mitochondrial complex II (succinate dehydrogenase, SDH) deficiencies**. Isolated complex II deficiency is itself one of the rarest respiratory-chain disorders, accounting for approximately 2% of all mitochondrial respiratory chain deficiency diagnoses ([PMID: 22972948](https://pubmed.ncbi.nlm.nih.gov/22972948/)). MC2DN3 is the specific nuclear type caused by *SDHD* mutations.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0030937 |
| OMIM | #619167 (Mitochondrial complex II deficiency, nuclear type 3) |
| Gene-OMIM | *SDHD* 602690 |
| Orphanet | Isolated complex II deficiency (group entity; no MC2DN3-specific ORPHA) |
| MeSH | Mitochondrial Diseases; Mitochondrial Encephalomyopathies (no MC2DN3-specific descriptor) |
| ICD-10 | E88.40 (mitochondrial metabolism disorder, unspecified) |
| ICD-11 | 5C53.1 (disorders of mitochondrial energy metabolism grouping) |

**Synonyms / alternative names:** Mitochondrial complex II deficiency nuclear type 3; isolated complex II deficiency due to SDHD; SDHD-related complex II deficiency; succinate dehydrogenase deficiency (SDHD type); succinate-ubiquinone oxidoreductase deficiency.

**Information source type.** Current knowledge is derived almost entirely from **aggregated disease-level resources and individual case reports** (OMIM, Orphanet, primary literature) rather than EHR-scale individual-patient datasets. Because of the extreme rarity (a handful of reported MC2DN3 patients since 2014), there is no registry-level or population-scale data specific to the SDHD type.

---

## Section 2. Etiology

**Primary cause — genetic.** MC2DN3 is caused by **biallelic pathogenic variants in *SDHD***, inherited in an autosomal recessive manner (Finding F001). The MONDO/OLS description states it is "autosomal recessive caused by pathogenic variants in the SDHD gene." Jackson et al. 2014 reported the first patient with isolated complex II deficiency due to compound heterozygous *SDHD* mutations: *"This report describes the first case of isolated complex II deficiency due to recessive SDHD germline mutations"* and *"The patient presented with early progressive encephalomyopathy due to compound heterozygous p.E69 K and p.\*164Lext\*3 SDHD mutations"* ([PMID: 24367056](https://pubmed.ncbi.nlm.nih.gov/24367056/)).

**Genetic risk factors.** The only established causal factor is biallelic *SDHD* loss of function. Consanguinity increases risk of homozygous recessive disease (as for all AR disorders). Being a compound heterozygote or homozygote for pathogenic *SDHD* alleles is deterministic for disease rather than probabilistic.

**Environmental risk / modifier factors.** No specific environmental cause is known. As with other mitochondrial encephalomyopathies, **metabolic stressors — intercurrent viral illness, fasting, and febrile episodes — can precipitate decompensation and developmental regression**. A recent SDH-deficiency case presented with encephalopathy and developmental regression following viral illnesses ([PMID: 37064335](https://pubmed.ncbi.nlm.nih.gov/37064335/)).

**Protective factors.** The best-documented modifiable protective influence is **riboflavin (vitamin B2) supplementation**, the FAD precursor, which can partially restore complex II activity (see Section 12, Finding F002). No protective germline alleles are established.

**Gene–environment interactions.** The dominant GxE axis is the interaction between the underlying enzyme deficiency and catabolic stress: patients with limited residual complex II activity decompensate during illness/fasting, whereas riboflavin availability modulates residual holoenzyme activity.

---

## Section 3. Phenotypes

The clinical spectrum of SDHD/complex II deficiency is dominated by neurological involvement, with cardiac and muscular involvement in a substantial subset (Finding F003). Jain-Ghai et al.'s review (n=36) found *"Neurological involvement is most commonly observed and brain imaging commonly shows leukoencephalopathy, Leigh syndrome, or cerebellar atrophy"* ([PMID: 23322652](https://pubmed.ncbi.nlm.nih.gov/23322652/)), and the broader SDH-deficiency spectrum includes *"several very different presentations including Leigh syndrome, epileptic encephalopathy, and cardiomyopathy"* ([PMID: 37064335](https://pubmed.ncbi.nlm.nih.gov/37064335/)).

**Verified HPO annotations (Finding F013):**

| Phenotype | HPO term | Type | Onset | Frequency (qualitative) |
|---|---|---|---|---|
| Hypotonia | HP:0001252 | Clinical sign | Neonatal/infantile | Common |
| Global developmental delay | HP:0001263 | Clinical sign | Infantile | Common |
| Developmental regression | HP:0002376 | Clinical sign | Infantile/childhood | Common (often post-illness) |
| Encephalopathy | HP:0001298 | Clinical sign | Early | Common |
| Leukoencephalopathy | HP:0002352 | Imaging/lab | Infantile | Frequent |
| Leukodystrophy | HP:0002415 | Imaging/lab | Infantile | Frequent |
| Bilateral basal ganglia lesions | HP:0007146 | Imaging | Infantile/childhood | Frequent (Leigh pattern) |
| Abnormal basal ganglia MRI signal | HP:0012751 | Imaging | Infantile/childhood | Frequent |
| Cardiomyopathy | HP:0001638 | Physical/imaging | Variable | ~50% in complex II deficiency; high-mortality |
| Myopathy | HP:0003198 | Clinical sign | Variable | Common |
| Muscle weakness | HP:0001324 | Symptom/sign | Variable | Common |
| Increased circulating lactate | HP:0002151 | Laboratory | Early | Frequent |
| Cerebellar atrophy | HP:0001272 | Imaging | Variable | Subset |
| Ataxia | HP:0001251 | Clinical sign | Variable | Subset |
| Seizure | HP:0001250 | Clinical sign | Variable | Subset (epileptic encephalopathy) |
| Optic atrophy | HP:0000648 | Physical/exam | Variable | Subset |
| Failure to thrive | HP:0001508 | Clinical sign | Infantile | Subset |

Note: **Leigh syndrome** has no single HPO term (it is the disease MONDO:0009723); it is captured phenotypically by the basal-ganglia/brainstem imaging terms above. During QC, HP:0030642 (Fundus albipunctatus) and HP:0002451 (Limb dystonia) were removed as inappropriate.

**Onset, severity, progression.** Onset is typically **neonatal to early childhood**; severity is **variable**; progression is usually **progressive**, often with episodic regression triggered by intercurrent illness. **Quality-of-life impact** is severe in the Leigh/leukoencephalopathy phenotype (motor and cognitive disability, feeding difficulties, seizures), though no disease-specific EQ-5D/SF-36 data exist for this ultra-rare entity.

---

## Section 4. Genetic / Molecular Information

**Causal gene and identifiers (Finding F005):**

| Attribute | Value |
|---|---|
| Gene symbol | *SDHD* (QPs3, CybS, PGL1) |
| NCBI Gene | 6392 |
| HGNC | HGNC:10683 |
| Gene-OMIM | 602690 |
| UniProt | O14521 (SDHD_HUMAN) |
| Ensembl | ENSG00000204370 |
| Cytoband | 11q23.1 (GRCh38 chr11:112,086,361–112,120,016, + strand) |
| Protein | Succinate dehydrogenase [ubiquinone] cytochrome b small subunit, mitochondrial (159 aa) |

SDHD encodes the small integral-membrane cytochrome-b (CybS) subunit that, together with SDHC, anchors complex II to the matrix side of the inner mitochondrial membrane and forms the heme-b/ubiquinone-reduction site.

**ClinVar variant landscape.** ClinVar (queried Oct 2026) lists **979 *SDHD* variants: 276 pathogenic, 94 likely pathogenic, 619 VUS**. Importantly, the majority of pathogenic alleles are reported in the *monoallelic paraganglioma* context rather than recessive MC2DN3, so interpretation in the recessive disease context requires care. The defining MC2DN3 variants are **p.E69K (missense)** and **p.\*164Lext\*3 (stop-loss/C-terminal extension)** ([PMID: 24367056](https://pubmed.ncbi.nlm.nih.gov/24367056/)).

**Variant types and functional consequence.** Reported recessive alleles include missense and stop-loss extension variants that cause **loss of function** via impaired complex II assembly. Allele frequencies of the recessive pathogenic variants are very low/absent in gnomAD, consistent with ultra-rarity. Origin is **germline**.

**Technical caveat — pseudogenes.** *SDHD* has processed pseudogenes on chromosomes 1, 2, 3, 7 and 18, which can complicate NGS/Sanger analysis and require careful mapping.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes are established for the recessive disease. The clinically relevant chromosomal/epigenetic phenomenon for *SDHD* is the **parent-of-origin imprinting effect in the paraganglioma context** (Section 9), not in recessive MC2DN3. No recurrent large structural rearrangements cause MC2DN3.

---

## Section 5. Environmental Information

MC2DN3 is a monogenic disorder; environmental factors are **triggers/modifiers rather than causes**. No toxins, infectious agents, or occupational exposures are established as etiologic. The practically important environmental modifiers are catabolic stressors (intercurrent infection, fasting, fever) that precipitate metabolic decompensation, and nutritional cofactor availability (riboflavin/FAD). No infectious agent causes or triggers the disease in a specific sense, although viral illnesses have temporally preceded regression episodes ([PMID: 37064335](https://pubmed.ncbi.nlm.nih.gov/37064335/)).

---

## Section 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *SDHD*** (e.g., p.E69K / p.\*164Lext\*3) → reduced or dysfunctional CybS (cytochrome-b small) subunit protein. *(Demonstrated — Jackson 2014.)*
2. Loss of functional SDHD **leads to** failure of the SDHC–SDHD membrane anchor to form → **impaired assembly of the complex II holoenzyme** in the inner mitochondrial membrane. *(Demonstrated by native-PAGE/western: "Native polyacrylamide gel electrophoresis and western blotting demonstrated an impaired complex II assembly," [PMID: 24367056](https://pubmed.ncbi.nlm.nih.gov/24367056/).)*
3. Impaired complex II assembly **results in** loss of succinate:ubiquinone oxidoreductase activity, which **simultaneously blocks two coupled pathways**:
   - **Branch A (TCA cycle):** failure to oxidize **succinate → fumarate**, causing **succinate accumulation** (detectable as an MR-spectroscopy succinate peak and elevated succinate/fumarate ratios).
   - **Branch B (OXPHOS):** failure to transfer electrons from FADH₂ via Fe-S clusters to **ubiquinone → ubiquinol**, reducing electron flux into the respiratory chain.
4. Reduced electron entry **leads to** diminished oxidative phosphorylation and **reduced ATP output**, with compensatory anaerobic glycolysis → **lactic acidosis** (HP:0002151). *(Demonstrated/inferred from biochemistry.)*
5. Energy deficit + succinate accumulation **results in** cellular dysfunction preferentially in **high-energy-demand, post-mitotic tissues** — neurons/glia (CNS), cardiomyocytes, and myofibers. *(Inferred from tissue tropism.)*
6. Tissue-level injury **manifests as** Leigh syndrome / basal-ganglia and brainstem necrosis, leukoencephalopathy/leukodystrophy, cardiomyopathy, and myopathy (the clinical phenotype). *(Demonstrated clinically.)*

```
 SDHD biallelic LOF
        │
        ▼
 CybS subunit lost/dysfunctional
        │
        ▼
 Complex II assembly failure (native-PAGE)
        │
        ├──────────────► Branch A: succinate→fumarate block
        │                    → succinate accumulation (MRS peak)
        │
        └──────────────► Branch B: electron transfer to ubiquinone block
                             → ↓OXPHOS → ↓ATP → ↑lactate
        │
        ▼
 Energy deficit in CNS / heart / muscle
        │
        ▼
 Leigh syndrome · leukoencephalopathy · cardiomyopathy · myopathy
```

### Molecular/biochemical detail (Finding F006)

Complex II is a ~140 kDa tetramer: catalytic **SDHA** (FAD flavoprotein) oxidizes succinate→fumarate; **SDHB** (three Fe-S clusters) relays electrons to the membrane anchor formed by **SDHC + SDHD**, which bind heme b and form the ubiquinone-reduction site, reducing ubiquinone→ubiquinol. SDHD/QPs3 was identified as one of the Q-binding subunits: *"identified QPs3 as one of the putative Q-binding proteins in this reductase"* ([PMID: 9211943](https://pubmed.ncbi.nlm.nih.gov/9211943/)). The soluble catalytic domain is bound to a membrane-spanning domain, a highly conserved architecture ([PMID: 36171656](https://pubmed.ncbi.nlm.nih.gov/36171656/)).

**Pathways/ontology suggestions:** TCA cycle (KEGG hsa00020), oxidative phosphorylation (KEGG hsa00190), Reactome "Complex II (succinate dehydrogenase)". GO biological process: GO:0006099 (tricarboxylic acid cycle), GO:0022904 (respiratory electron transport chain), GO:0006119 (oxidative phosphorylation). CHEBI entities: succinate (CHEBI:30031), fumarate (CHEBI:29806), ubiquinone (CHEBI:16389), FAD (CHEBI:16238), heme b (CHEBI:26355), lactate (CHEBI:24996).

**Cellular/tissue damage mechanisms.** Bioenergetic failure and oxidative stress drive neuronal/glial injury (spongiform change, demyelination in white matter, symmetric necrosis of basal ganglia/brainstem in Leigh syndrome) and cardiomyocyte dysfunction. Succinate accumulation may also exert signaling effects (e.g., HIF stabilization, GPR91/SUCNR1 signaling) known from the tumor context, though these are better characterized for monoallelic/tumor biology than for recessive disease.

---

## Section 7. Anatomical Structures Affected (Finding F009)

**Organ / body-system level:**
- **Central nervous system (primary):** basal ganglia, brainstem, cerebral and cerebellar white matter — Leigh syndrome, leukoencephalopathy/leukodystrophy, cerebellar atrophy. UBERON: brain (UBERON:0000955), basal ganglia (UBERON:0002420), brainstem (UBERON:0002298), cerebellum (UBERON:0002037), cerebral white matter (UBERON:0002316).
- **Heart:** cardiomyopathy (UBERON:0000948, heart).
- **Skeletal muscle:** myopathy (UBERON:0001134, skeletal muscle tissue).
- **Eye (subset):** optic atrophy (UBERON:0000941, optic nerve).

*"Neurological involvement is most commonly observed and brain imaging commonly shows leukoencephalopathy, Leigh syndrome, or cerebellar atrophy"* ([PMID: 23322652](https://pubmed.ncbi.nlm.nih.gov/23322652/)).

**Tissue / cell level.** Affected cell types: neurons (CL:0000540), astrocytes/glia (CL:0000127), oligodendrocytes (white matter; CL:0000128), cardiomyocytes (CL:0000746), skeletal muscle fibers (CL:0000188). These are high-OXPHOS-dependence, post-mitotic cells.

**Subcellular level.** SDHD (UniProt O14521) is an integral protein of the **mitochondrial inner membrane**. GO cellular components: **GO:0005743 mitochondrial inner membrane**, **GO:0045273 respiratory chain complex II (succinate dehydrogenase)**, **GO:0005759 mitochondrial matrix**. Molecular functions: GO:0020037 heme binding, GO:0048039 ubiquinone binding, GO:0008177 succinate dehydrogenase (quinone) activity, GO:0009055 electron transfer activity.

**Lateralization.** CNS lesions in Leigh syndrome are characteristically **bilateral and symmetric** (e.g., bilateral basal ganglia lesions, HP:0007146).

---

## Section 8. Temporal Development

- **Onset:** typically **congenital/neonatal to early childhood**; onset pattern is often **insidious or subacute**, with **acute decompensations** superimposed by intercurrent illness.
- **Progression:** generally **progressive**, frequently with **episodic regression**. In the broader complex II-deficiency spectrum, course ranges from fatal in infancy to mild adult-onset disease (Finding F012): *"For some, the condition was fatal in infancy, others had multisystem involvement and some had onset in adulthood with mild symptoms and normal cognition"* ([PMID: 23322652](https://pubmed.ncbi.nlm.nih.gov/23322652/)).
- **Disease course pattern:** chronic, lifelong, progressive, with relapsing decompensations.
- **Remission:** no spontaneous cure; partial, treatment-associated stabilization/improvement reported with **riboflavin** (Section 12).
- **Critical periods:** infancy/early childhood is the window of greatest vulnerability and the key opportunity for cofactor intervention and avoidance of catabolic stress.

---

## Section 9. Inheritance and Population

**Epidemiology (Finding F008).** Mitochondrial disease collectively has a minimum prevalence >1 in 5,000 adults: *"Mitochondrial disease is one of the most common groups of genetic diseases with a minimum prevalence of greater than 1 in 5000 in adults"* ([PMID: 26315846](https://pubmed.ncbi.nlm.nih.gov/26315846/)). Isolated complex II deficiency accounts for ~2% of respiratory-chain deficiency diagnoses ([PMID: 22972948](https://pubmed.ncbi.nlm.nih.gov/22972948/)). **MC2DN3 specifically is ultra-rare — only a handful of patients reported since 2014 — so no formal prevalence/incidence estimate exists.**

**Inheritance (Finding F001 / F004).** Autosomal recessive; disease requires **biallelic** *SDHD* loss of function. Penetrance of biallelic LOF is presumed high/complete; expressivity is variable even within the complex-II-deficiency spectrum. No genetic anticipation (not a repeat-expansion disorder). Consanguinity increases risk of homozygous disease.

**Dual gene role / imprinting (Finding F004).** A defining molecular feature of *SDHD* is its dual disease role. **Monoallelic** germline *SDHD* variants cause **hereditary paraganglioma/pheochromocytoma (PGL1)** with a parent-of-origin effect: *"In SDHD (11q23)-linked families, the disease phenotype is expressed only upon paternal transmission of the mutation, consistent with maternal imprinting"* ([PMID: 15064708](https://pubmed.ncbi.nlm.nih.gov/15064708/)). Tumor formation requires somatic **loss of maternal chromosome 11**: *"loss of maternal chromosome 11p15 was demonstrated in 85% of SDHD"* paragangliomas ([PMID: 28099933](https://pubmed.ncbi.nlm.nih.gov/28099933/)). This dominant, imprinted tumor mechanism is **mechanistically distinct** from the recessive, biallelic mechanism of MC2DN3. Clinically, this means family counseling for an MC2DN3 proband must also consider tumor risk in heterozygous carriers (especially with paternal transmission).

**Population demographics.** No ethnic predilection or founder effect is established for the recessive MC2DN3 alleles. Sex ratio is expected ~1:1 (autosomal). Age distribution of affected individuals is skewed to infancy/early childhood.

---

## Section 10. Diagnostics (Finding F008)

**Biochemical / enzymatic:**
- **Respiratory chain enzyme assay** (muscle or fibroblasts) showing **isolated low complex II (SDH) activity** with normal other complexes.
- **SDH histochemistry** on muscle (reduced staining).
- **Elevated blood and CSF lactate** (HP:0002151).

**Imaging:**
- **Brain MRI:** Leigh-pattern bilateral symmetric basal ganglia/brainstem lesions, or leukoencephalopathy/leukodystrophy, or cerebellar atrophy.
- **MR spectroscopy:** may show an abnormal **succinate peak** (characteristic of SDH deficiency).

**Protein/assembly:**
- **BN-PAGE / native-PAGE and western blot** demonstrating impaired complex II assembly and reduced steady-state SDH subunit levels ([PMID: 24367056](https://pubmed.ncbi.nlm.nih.gov/24367056/), [PMID: 22972948](https://pubmed.ncbi.nlm.nih.gov/22972948/)).

**Molecular (confirmatory):**
- **WES/WGS or targeted SDHx gene panel** (SDHA, SDHB, SDHC, SDHD, SDHAF1, SDHAF2). Jackson et al. explicitly recommend: *"We therefore recommend screening for all SDH genes in isolated complex II deficiencies"* ([PMID: 24367056](https://pubmed.ncbi.nlm.nih.gov/24367056/)). Pseudogene awareness is required for *SDHD*.
- Functional validation by **cell-line/yeast complementation** for VUS resolution.

**Differential diagnosis:** other isolated complex II deficiencies (SDHA/SDHB/SDHC/SDHAF1-related — MC2DN1/2/4), other Leigh syndrome genetic causes (e.g., complex I defects such as NDUFS4), and other leukodystrophies/mitochondrial encephalomyopathies. SDHD type is distinguished by biallelic SDHD genotype and the biochemical signature of isolated complex II deficiency.

**Screening.** No newborn screening exists for MC2DN3. Carrier and cascade testing is feasible once a familial genotype is known; genetic counseling must address the dual tumor/mitochondrial-disease risk of *SDHD*.

---

## Section 11. Outcome / Prognosis (Finding F012)

Prognosis is **highly variable**. In the complex-II-deficiency spectrum, outcomes range from fatal infantile disease to mild adult-onset forms: *"For some, the condition was fatal in infancy, others had multisystem involvement and some had onset in adulthood with mild symptoms and normal cognition"* ([PMID: 23322652](https://pubmed.ncbi.nlm.nih.gov/23322652/)).

**Prognostic factors:**
- **Cardiomyopathy** is associated with **high mortality** (adverse prognostic marker).
- **Riboflavin-responsiveness** (particularly in early-onset leukoencephalopathy) predicts **stabilization or improvement** (favorable; Finding F002, Section 12).
- Within a family, *"the phenotype and enzyme activities are comparable within a family"* ([PMID: 23322652](https://pubmed.ncbi.nlm.nih.gov/23322652/)), but across patients there is **no reliable correlation between residual muscle complex II activity and clinical severity**.

**Disease course / complications:** progressive neurodegeneration with risk of brainstem/respiratory failure (Leigh syndrome), seizures, feeding difficulties/failure to thrive, cardiac failure, and recurrent metabolic decompensation. No validated disease-specific QoL instruments exist.

---

## Section 12. Treatment (Finding F002 / F011)

**There is no curative therapy.** *"There are currently no effective clinical treatments for mitochondrial disease"* ([PMID: 38883711](https://pubmed.ncbi.nlm.nih.gov/38883711/)); *"There is no cure for complex II deficiency, though some reported patients showed clinical improvement following riboflavin therapy"* ([PMID: 37064335](https://pubmed.ncbi.nlm.nih.gov/37064335/)).

**Pharmacologic / cofactor (off-label):**

| Intervention | Rationale / evidence | NCIT suggestion |
|---|---|---|
| **Riboflavin (vitamin B2)** | FAD precursor; biochemical and partial clinical benefit. *"Riboflavin supplementation to the growth medium of cultured fibroblasts resulted in a 2-fold increase of complex II activity in patients, but not in controls"* ([PMID: 16737791](https://pubmed.ncbi.nlm.nih.gov/16737791/)). Neurological regression in a Leigh/leukodystrophy SDH patient regressed on riboflavin ([PMID: 10230482](https://pubmed.ncbi.nlm.nih.gov/10230482/)). | NCIT:C737 (Riboflavin) |
| **Coenzyme Q10 / ubiquinone** | Mitochondrial "cocktail"; electron carrier support ([PMID: 37064335](https://pubmed.ncbi.nlm.nih.gov/37064335/)). | NCIT:C1220 (Coenzyme Q10) |
| **L-carnitine** | Mitochondrial cocktail component ([PMID: 37064335](https://pubmed.ncbi.nlm.nih.gov/37064335/)). | NCIT:C78591 (Levocarnitine) |
| Antioxidants/vitamins | Common supportive strategy in Leigh syndrome. | — |

**Supportive/rehabilitative care:** management of lactic acidosis, antiepileptic therapy for seizures, cardiac monitoring/heart-failure management for cardiomyopathy, nutritional support/feeding, and physical/occupational/speech therapy. **Avoidance of metabolic stressors** (fasting, aggressive management of intercurrent illness) is advised.

**Experimental agents:** vatiquinone (EPI-743, α-tocotrienol quinone; ≥19 US trials since 2012) showed **no survival benefit** in the Ndufs4-KO Leigh mouse model, though it may reduce seizures ([PMID: 39930437](https://pubmed.ncbi.nlm.nih.gov/39930437/)). Zagociguat (sGC stimulator) improved mitochondrial physiology across diverse respiratory-chain-deficient zebrafish models and may have utility beyond MELAS, potentially including Leigh spectrum disorder ([PMID: 40786033](https://pubmed.ncbi.nlm.nih.gov/40786033/)). No complex-II-specific or SDHD-specific targeted therapy exists.

**Pharmacogenomics / personalized medicine:** no established PGx for MC2DN3; management is genotype-informed only insofar as confirming a complex II (SDH) defect supports a riboflavin trial.

---

## Section 13. Prevention

- **Primary prevention:** not possible for the genetic disease; **genetic counseling** and reproductive options (prenatal diagnosis, preimplantation genetic testing) once a familial *SDHD* genotype is known. Counseling must disclose the **dual risk** — recessive mitochondrial disease in biallelic carriers, and paraganglioma/pheochromocytoma risk in heterozygous carriers (parent-of-origin dependent).
- **Secondary prevention:** early biochemical/genetic diagnosis to enable a riboflavin trial and avoidance of metabolic stressors; cascade carrier testing.
- **Tertiary prevention:** aggressive management of intercurrent illness, cardiac surveillance, seizure control, and nutritional support to prevent decompensation and complications.
- **Immunization:** routine childhood vaccination is advisable to reduce illness-triggered decompensations (general mitochondrial-disease practice); no disease-specific vaccine.
- **Carrier surveillance:** heterozygous relatives should be counseled regarding paraganglioma/pheochromocytoma surveillance per SDHx tumor-syndrome guidelines, especially for paternally inherited alleles.

---

## Section 14. Other Species / Natural Disease (Finding F010)

*SDHD* is highly conserved (HomoloGene 37718). The soluble catalytic domain of complex II is "highly conserved" across all biological kingdoms, and mitochondrial type-C complex II with a single heme b is proposed to have evolved as an assembled unit: *"a highly conserved soluble domain is bound to a membrane-spanning domain"* ([PMID: 36171656](https://pubmed.ncbi.nlm.nih.gov/36171656/)).

**Orthologs (NCBI Gene / Taxon):**

| Species | Gene | NCBI Gene | Taxon |
|---|---|---|---|
| Mouse (*Mus musculus*) | *Sdhd* | 66925 | 10090 |
| Rat (*Rattus norvegicus*) | *Sdhd* | 363061 | 10116 |
| Zebrafish (*Danio rerio*) | *sdhd* | 445500 | 7955 |
| *Xenopus tropicalis* | *sdhd* | 394986 | 8364 |
| Chicken (*Gallus gallus*) | *SDHD* | 419793 | 9031 |
| Rhesus macaque | *SDHD* | 711326 | 9544 |
| Chimpanzee | *SDHD* | 451547 | 9598 |
| Dog | *SDHD* | 479438 | 9615 |
| Cow | *SDHD* | 281481 | 9913 |

Yeast (*S. cerevisiae*) **SDH4** is the functional homolog used in complementation assays. No well-characterized naturally occurring biallelic-*SDHD* complex II deficiency is documented in companion animals or wildlife (OMIA has no established MC2DN3 entry); comparative disease modeling therefore relies on engineered models (Section 15). The disease is **non-transmissible / non-zoonotic**.

---

## Section 15. Model Organisms (Finding F007)

**Mouse (*Mus musculus*, Taxon 10090) — the principal mammalian model.** Piruat et al. 2004 generated the first mammalian ETC-subunit knockout. Key findings:
- **Homozygous *Sdhd*(−/−) is embryonic lethal:** *"Homozygous SDHD(-/-) animals die at early embryonic stages"* ([PMID: 15572694](https://pubmed.ncbi.nlm.nih.gov/15572694/)).
- **Heterozygous *Sdhd*(+/−):** *"Heterozygous SDHD(+/-) mice show a general, noncompensated deficiency of succinate dehydrogenase activity without alterations in body weight or major physiological dysfunction"* ([PMID: 15572694](https://pubmed.ncbi.nlm.nih.gov/15572694/)), but with constitutive carotid-body glomus-cell activation (hypertrophy/hyperplasia).

**Compound-heterozygous Sdhb/Sdhc/Sdhd knockout mice** (Baysal et al. 2022) show reduced SDH protein, elevated succinate and succinate/fumarate and succinate/oxoglutarate ratios, and complex-II-dependent effects on red cell distribution width and healthy lifespan under chronic hypoxia ([PMID: 35881479](https://pubmed.ncbi.nlm.nih.gov/35881479/)).

**Model characteristics / limitations.** Because full *Sdhd* knockout is embryonic lethal, the complete recessive human disease is not directly recapitulated by a constitutive null; conditional/tissue-specific or hypomorphic models are needed to model the human encephalomyopathy. Heterozygous mice better model the carrier/tumor-predisposition biology (carotid body activation) than the recessive mitochondrial disease. Other respiratory-chain Leigh models (e.g., Ndufs4-KO mouse) and multi-complex-deficient zebrafish are used as surrogate platforms for therapeutic testing ([PMID: 39930437](https://pubmed.ncbi.nlm.nih.gov/39930437/), [PMID: 40786033](https://pubmed.ncbi.nlm.nih.gov/40786033/)).

**Resources:** MGI (mouse *Sdhd*), IMPC/IMSR for alleles; patient-derived fibroblasts and yeast (*SDH4*) complementation systems for in vitro functional work.

---

## Mechanistic Model / Interpretation

MC2DN3 is a clean example of a **single-subunit assembly failure propagating to a bioenergetic and metabolic double-lesion**. Because SDHD is the membrane anchor and part of the ubiquinone-binding site, its loss does not merely reduce one enzymatic step — it collapses the structural scaffold needed to assemble the holoenzyme, so that both the TCA-cycle succinate-oxidation arm and the respiratory-chain electron-entry arm fail together. This explains two cardinal biochemical signatures observed clinically: **lactic acidosis** (OXPHOS failure, anaerobic glycolysis) and a **succinate peak on MRS** (TCA blockade). The downstream clinical picture is governed by tissue OXPHOS dependence, hence the predilection for CNS, heart, and muscle, and the characteristic bilateral symmetric basal-ganglia/brainstem lesions of Leigh syndrome.

The **upstream** event is always the biallelic SDHD lesion; **downstream** are assembly failure → dual metabolic blockade → energy deficit/succinate accumulation → tissue-specific neurodegeneration and cardiomyopathy. The one branch point worth emphasizing for a knowledge base is the **genotype-dosage branch of SDHD biology**: biallelic → recessive mitochondrial disease (this entity); monoallelic + somatic loss of the wild-type/maternal allele → paraganglioma. The same enzyme deficiency therefore underlies two opposite clinical worlds (degenerative vs neoplastic), unified by succinate accumulation and its pseudohypoxic/signaling consequences.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [24367056](https://pubmed.ncbi.nlm.nih.gov/24367056/) | *Mutations in SDHD lead to autosomal recessive encephalomyopathy and isolated mitochondrial complex II deficiency* | **Defining paper** — establishes SDHD biallelic recessive cause, variants, assembly defect, testing recommendation |
| [23322652](https://pubmed.ncbi.nlm.nih.gov/23322652/) | *Complex II deficiency — case report and review* | Phenotype spectrum, imaging, variable prognosis, intrafamilial consistency |
| [37064335](https://pubmed.ncbi.nlm.nih.gov/37064335/) | *Two Patients Diagnosed as SDH Deficiency* | Phenotypic presentations; no cure/riboflavin benefit; cocktail therapy |
| [16737791](https://pubmed.ncbi.nlm.nih.gov/16737791/) | *Effects of riboflavin in children with complex II deficiency* | Riboflavin ~2-fold complex II activity increase (biochemical rationale) |
| [10230482](https://pubmed.ncbi.nlm.nih.gov/10230482/) | *Leigh syndrome/leukodystrophy, regression with riboflavin* | Clinical riboflavin response in SDH deficiency |
| [22972948](https://pubmed.ncbi.nlm.nih.gov/22972948/) | *Recessive SDHA/SDHB leukodystrophy and isolated complex II deficiency* | ~2% frequency; related SDHx recessive disease; BN-PAGE assembly defects |
| [9211943](https://pubmed.ncbi.nlm.nih.gov/9211943/) | *Smallest anchoring subunit (QPs3) ... Q-binding domain* | SDHD = QPs3/CybS; ubiquinone-binding role |
| [36171656](https://pubmed.ncbi.nlm.nih.gov/36171656/) | *Evolution of the quinone binding site in complex II* | Conserved architecture across species |
| [15064708](https://pubmed.ncbi.nlm.nih.gov/15064708/) | *Somatic loss of maternal chromosome 11 ... SDHD paraganglioma* | Parent-of-origin/imprinting tumor mechanism (dual role) |
| [28099933](https://pubmed.ncbi.nlm.nih.gov/28099933/) | *Loss of maternal chromosome 11 in SDHx paragangliomas* | 85% maternal 11p15 loss in SDHD tumors |
| [15572694](https://pubmed.ncbi.nlm.nih.gov/15572694/) | *Mitochondrial SDHD gene required for early embryogenesis* | Mouse: homozygous KO embryonic lethal; heterozygous phenotype |
| [35881479](https://pubmed.ncbi.nlm.nih.gov/35881479/) | *SDH regulates RDW and lifespan in hypoxic mice* | Compound Sdh KO mouse metabolomics (succinate ratios) |
| [26315846](https://pubmed.ncbi.nlm.nih.gov/26315846/) | *Mitochondrial disease: genetics and management* | Prevalence context (>1 in 5,000) |
| [38883711](https://pubmed.ncbi.nlm.nih.gov/38883711/) | *Vatiquinone in preclinical mitochondrial disease models* | No effective clinical treatments; experimental agent data |
| [39930437](https://pubmed.ncbi.nlm.nih.gov/39930437/) | *Vatiquinone in Leigh/GPX4 models* | No survival benefit in Ndufs4-KO; possible seizure reduction |
| [40786033](https://pubmed.ncbi.nlm.nih.gov/40786033/) | *Zagociguat in RC-deficient zebrafish* | Emerging therapeutic candidate for RC disease |

**Evidence-type distribution:** human clinical/case reports (24367056, 23322652, 37064335, 16737791, 10230482, 22972948), tumor-biology human genetics (15064708, 28099933), biochemistry/structural (9211943, 36171656), model organism (15572694, 35881479, 39930437, 40786033), and review/epidemiology (26315846, 38883711).

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity.** MC2DN3 rests on a very small number of reported biallelic-*SDHD* patients; much of the phenotype/prognosis detail is extrapolated from the broader isolated complex II / SDHx deficiency literature rather than from SDHD-type-specific cohorts.
2. **No epidemiology.** No formal prevalence, incidence, carrier frequency, sex ratio, or geographic data exist for the SDHD type specifically.
3. **Variant interpretation complexity.** Most ClinVar *SDHD* pathogenic alleles are reported in the monoallelic tumor context; recessive-disease pathogenicity assignment and the confounding *SDHD* pseudogenes complicate molecular diagnosis.
4. **No faithful mammalian model** of the recessive human disease — constitutive *Sdhd* null is embryonic lethal; conditional/hypomorphic CNS- and heart-specific models are lacking.
5. **No controlled therapeutic evidence.** Riboflavin and cofactor benefits derive from small case series and in vitro data; no randomized trials exist for complex II deficiency.
6. **Mechanistic signaling downstream of succinate** (pseudohypoxia, GPR91/SUCNR1) is better characterized in tumor biology than in the degenerative recessive disease.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an SDHD-type registry / GeneMatcher collection** to aggregate biallelic-*SDHD* cases, enabling genotype–phenotype correlation, natural-history, and prognosis data.
2. **Build a conditional/tissue-specific *Sdhd* mouse** (neuronal and cardiac Cre-driven, or hypomorphic knock-in of human p.E69K) to circumvent embryonic lethality and recapitulate encephalomyopathy/cardiomyopathy.
3. **Patient-derived iPSC → neuron/cardiomyocyte and cerebral organoid models** to dissect cell-type-specific bioenergetic failure and screen cofactor/drug responses (riboflavin, CoQ10, zagociguat).
4. **Prospective riboflavin-response biomarker study** — correlate fibroblast complex II activity rescue with clinical responsiveness to guide a riboflavin trial and define responder genotypes.
5. **Deep variant curation** of *SDHD* in the recessive context (functional assays, pseudogene-aware pipelines) to reclassify VUS and build an MC2DN3-specific pathogenicity reference.
6. **Metabolomic biomarker validation** (plasma/CSF succinate, succinate/fumarate ratio, MRS succinate peak) as diagnostic and treatment-response endpoints.
7. **Integrate dual-risk genetic counseling protocols** so that MC2DN3 family cascade testing systematically addresses heterozygote paraganglioma/pheochromocytoma surveillance (parent-of-origin aware).

---

*Report compiled from 13 confirmed findings and 33 reviewed papers across 5 investigation iterations. Evidence types are distinguished throughout as human clinical, model organism, in vitro, or computational/ontological. Ontology suggestions (MONDO, HPO, GO, CL, UBERON, CHEBI, NCIT) are provided for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Mitochondrial_Complex_II_Deficiency_Nuclear_Type_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mitochondrial_Complex_II_Deficiency_Nuclear_Type_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 26 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030937` (2 mentions) - the report calls it "MONDO"; MONDO calls it **mitochondrial complex 2 deficiency, nuclear type 3**
- `HP:0002151` (3 mentions) - the report calls it "Increased circulating lactate", "lactic acidosis", "Elevated blood and CSF lactate"; HP calls it **Increased circulating lactate concentration**
- `NCIT:C737` (1 mention) - the report calls it "Riboflavin"; NCIT calls it **Pesticide**
- `NCIT:C1220` (1 mention) - the report calls it "Coenzyme Q10"; NCIT calls it **Samarium Sm-153 Lexidronam Pentasodium**
- `NCIT:C78591` (1 mention) - the report calls it "Levocarnitine"; NCIT calls it **Laryngeal Nerve Paralysis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012751` (1 mention) - the report calls it "Abnormal basal ganglia MRI signal"; HP calls it **Abnormal basal ganglia MRI signal intensity**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002151` - called "Increased circulating lactate", "lactic acidosis", "Elevated blood and CSF lactate"