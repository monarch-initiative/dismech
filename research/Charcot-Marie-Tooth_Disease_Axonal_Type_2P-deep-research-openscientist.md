---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-02T07:41:07.414008'
end_time: '2026-09-02T07:55:24.236991'
duration_seconds: 856.82
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Axonal Type 2P
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 20
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 17
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0013749
    reported_labels:
    - Charcot-Marie-Tooth disease, axonal, type 2P
    - Suggested MONDO
    ontology_label: ventricular septal defect 3
  - term_id: HP:0001761
    reported_labels:
    - Physical manifestation
    ontology_label: Pes cavus
  - term_id: HP:0009027
    reported_labels:
    - Clinical sign
    ontology_label: Foot dorsiflexor weakness
  - term_id: NCIT:C15224
    reported_labels:
    - pain management
    ontology_label: Nutrition Research, Fats
  - term_id: NCIT:C15633
    reported_labels:
    - genetic counseling
    ontology_label: Cancer Pain Management
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Charcot-Marie-Tooth_Disease_Axonal_Type_2P-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Charcot-Marie-Tooth_Disease_Axonal_Type_2P-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Axonal Type 2P
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Axonal Type 2P** covering all of the
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

# Charcot-Marie-Tooth Disease Axonal Type 2P (CMT2P) — Comprehensive Disease Characteristics Report

**Disease:** Charcot-Marie-Tooth Disease, Axonal, Type 2P
**OMIM:** #614436 | **Gene:** *LRSAM1* (chr9q33.3) | **Category:** Mendelian
**Suggested MONDO:** MONDO:0013749 (Charcot-Marie-Tooth disease, axonal, type 2P)

*Evidence base: literature-derived (human clinical, in vitro/biochemical, model organism, and computational). No primary datasets were provided; all claims are supported by primary literature (PMIDs) and standard disease/gene databases.*

---

## Summary

Charcot-Marie-Tooth disease axonal type 2P (**CMT2P**; OMIM #614436) is a rare, genetically defined form of hereditary axonal sensorimotor peripheral neuropathy caused by pathogenic variants in ***LRSAM1***, a gene on chromosome 9q33.3 encoding a **RING-type E3 ubiquitin-protein ligase**. It is a member of the large, clinically and genetically heterogeneous Charcot-Marie-Tooth (CMT) family — the most common inherited neuromuscular disorder, affecting roughly 1 in 2,500 people worldwide — but CMT2P itself is one of the rarer axonal (type 2) subtypes. The disease is distinguished by a **late/adult onset** (typically second to fifth decade), **slow progression**, **lower-limb predominance**, frequent **neuropathic pain**, and marked **phenotypic variability** that includes asymptomatic mutation carriers.

The molecular pathology centers on **loss of LRSAM1 ubiquitin ligase activity**. Pathogenic variants cluster in the C-terminal RING domain that mediates the essential E2–E3 interaction required for transferring ubiquitin to substrate proteins (the best-validated target being TSG101, a component of the ESCRT endosomal-trafficking machinery). CMT2P displays a distinctive **dual inheritance pattern**: recessive alleles that trigger complete loss of protein (e.g., via nonsense-mediated decay, NMD) versus dominant alleles that escape NMD and produce a truncated protein exerting a **dominant-negative** effect on the RING domain. Whether a 3′-located premature-termination variant escapes or triggers NMD effectively determines whether disease is dominant or recessive — a rare and instructive example of a single gene where variant position dictates inheritance mode.

There is **no curative therapy**; management is entirely symptomatic and supportive (ankle-foot orthoses, physical/occupational therapy, foot-deformity surgery, neuropathic pain control, and genetic counseling), and **life expectancy is normal**. An emerging and biologically intriguing finding is that LRSAM1 disease may extend beyond the peripheral nervous system: within the original dominant kindred, several affected members developed **late-onset parkinsonism**, and additional cases pair CMT2P with parkinsonian features — linking this peripheral neuropathy to a central nervous system phenotype and to ubiquitin-proteostasis themes shared with neurodegeneration.

---

## 1. Disease Information

**Overview.** CMT2P is an axonal (as opposed to demyelinating) hereditary motor and sensory neuropathy. Clinically it presents as a length-dependent, distal, symmetric sensorimotor polyneuropathy with distal weakness and atrophy (legs > arms), distal sensory loss, reduced/absent tendon reflexes, foot deformity (pes cavus), and gait impairment — the classic CMT phenotype — but with a characteristically **mild, late-onset, slowly progressive** course.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #614436 (Charcot-Marie-Tooth disease, axonal, type 2P) |
| OMIM (gene) | *LRSAM1* 610933 |
| Gene / HGNC | *LRSAM1*, HGNC:25135 |
| NCBI Gene | 90678 |
| UniProt | Q6UWE0 |
| Suggested MONDO | MONDO:0013749 |
| ICD-10 | G60.0 (Hereditary motor and sensory neuropathy) |
| ICD-11 | 8C20 (Hereditary motor and sensory neuropathy) |
| MeSH | Charcot-Marie-Tooth Disease (D002607) |

**Synonyms / alternative names:** CMT2P; Charcot-Marie-Tooth disease, axonal, type 2P; CMT2G (a historically separate entity now **reclassified as CMT2P** after identification of the *LRSAM1* p.Cys694Tyr mutation — [PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)); LRSAM1-related Charcot-Marie-Tooth disease.

**Information source type.** The knowledge base for CMT2P is derived overwhelmingly from **aggregated disease-level resources** — OMIM, published family/pedigree studies, and case reports — rather than large EHR cohorts, reflecting its rarity.

---

## 2. Etiology

**Primary cause — genetic.** CMT2P is a monogenic Mendelian disorder caused by pathogenic variants in ***LRSAM1***. The first description came from **Guernsey et al. (2010)** who used homozygosity mapping in a large recessive eastern Canadian kindred (locus chr9:122–129 Mb) and identified a homozygous intronic splice-acceptor variant (AG→AA) producing a frameshift/truncation and complete loss of protein ([PMID: 20865121](https://pubmed.ncbi.nlm.nih.gov/20865121/)). **Weterman et al. (2012)** then identified a dominant frameshift, **p.Leu708Argfs\*28**, in the C-terminal RING domain in a three-generation family with a strong LOD score of 5.12 ([PMID: 22012984](https://pubmed.ncbi.nlm.nih.gov/22012984/)).

> "A homozygous pathogenic variant was identified in the gene encoding leucine rich repeat and sterile alpha motif 1 (LRSAM1) by direct DNA sequencing" — Guernsey et al., [PMID: 20865121](https://pubmed.ncbi.nlm.nih.gov/20865121/)

> "This frameshift mutation (p.Leu708Argfx28) is located in the C-terminal RING finger motif of the encoded protein." — Weterman et al., [PMID: 22012984](https://pubmed.ncbi.nlm.nih.gov/22012984/)

**Genetic risk factors.** The causal variants themselves are the risk factors; no additional susceptibility loci are established. **Modifier considerations:** in a family co-segregating a *RAB7A* (CMT2B) mutation and a novel *LRSAM1* variant, gender and possible *RAB7A/LRSAM1* gene interactions were proposed to explain marked variability in age of onset ([PMID: 27462242](https://pubmed.ncbi.nlm.nih.gov/27462242/)).

**Environmental risk / protective factors.** No environmental risk or protective factors are established for CMT2P in humans. However, an important **gene–environment interaction** was demonstrated in the mouse model: *Lrsam1* mutant mice are hypersensitive to the axonal neurotoxin **acrylamide**, indicating that loss of LRSAM1 lowers the axonal threshold for degeneration under toxic stress ([PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)). This suggests that, mechanistically, neurotoxic exposures could plausibly aggravate an LRSAM1-compromised nervous system, though this has not been shown clinically.

**Genetic protective factors.** None specifically identified. Incomplete penetrance/asymptomatic carriers imply the existence of unknown modifiers, but none have been mapped.

---

## 3. Phenotypes

CMT2P phenotypes are those of a distal, length-dependent axonal sensorimotor polyneuropathy. Onset is typically **adult/late (2nd–5th decade)**, severity is **mild to moderate**, progression is **slow and progressive**, and there is **variable expressivity** including asymptomatic carriers ([PMID: 33568173](https://pubmed.ncbi.nlm.nih.gov/33568173/), [PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)).

> "dominant CMT2P is usually characterized by relatively mild, slowly progressive axonal neuropathy, mainly involving lower limbs, with age of onset between the second and fifth decades of life" — Palaima et al., [PMID: 33568173](https://pubmed.ncbi.nlm.nih.gov/33568173/)

> "CMT2P is a rare, but nevertheless relevant cause of adult-onset axonal and painful neuropathy" — Reilich et al., [PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)

| Phenotype | Type | HPO term (suggested) | Onset / severity / progression | Notes |
|---|---|---|---|---|
| Distal lower-limb muscle weakness | Clinical sign | HP:0009053 / HP:0002460 | Adult; mild-moderate; progressive | Legs affected before/more than arms |
| Distal sensory loss | Symptom/sign | HP:0002936 (distal sensory impairment) | Adult; variable | Length-dependent |
| Neuropathic / painful neuropathy | Symptom | HP:0009830 (peripheral neuropathy), HP:0012531 (pain) | Adult; variable | Notable feature of CMT2P |
| Pes cavus (high-arched foot) | Physical manifestation | HP:0001761 | Insidious | Classic CMT deformity |
| Gait instability / disturbance | Clinical sign | HP:0002317 (unsteady gait), HP:0001288 | Progressive | Major functional impact |
| Reduced/absent deep tendon reflexes | Clinical sign | HP:0001265 (areflexia) / HP:0001315 | Early | Distal predominance |
| Foot drop | Clinical sign | HP:0009027 | Adult | From distal weakness |
| Fatty atrophy of lower-limb muscle (MRI) | Laboratory/imaging | HP:0003693 (distal amyotrophy) | Subclinical detectable | Detects subclinical carriers ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)) |
| Parkinsonism (emerging) | Clinical sign | HP:0001300 (parkinsonism) | Late (5th–7th decade) | CNS extension ([PMID: 26900582](https://pubmed.ncbi.nlm.nih.gov/26900582/), [PMID: 40721190](https://pubmed.ncbi.nlm.nih.gov/40721190/)) |

**Quality-of-life impact.** As with CMT broadly, the dominant burden is on **mobility and gait**, with foot deformity, falls risk, and — distinctively for CMT2P — **chronic neuropathic pain**. Supportive care (orthotics, rehabilitation) improves quality of life ([PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/), [PMID: 40636623](https://pubmed.ncbi.nlm.nih.gov/40636623/)). Formal EQ-5D/SF-36/PROMIS data specific to CMT2P are not available.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***LRSAM1*** (Leucine Rich Repeat And Sterile Alpha Motif containing 1; also called **Tal**), HGNC:25135, gene OMIM 610933, NCBI Gene 90678, UniProt Q6UWE0, on **chromosome 9q33.3**. It encodes a universally expressed **RING-type E3 ubiquitin-protein ligase** with domain architecture **LRR – coiled-coil – SAM – PDZ-binding – RING** ([PMID: 33568173](https://pubmed.ncbi.nlm.nih.gov/33568173/), [PMID: 23245322](https://pubmed.ncbi.nlm.nih.gov/23245322/)).

**Pathogenic variants** cluster in the **3′-prime exons encoding the C-terminal RING domain**. Reilich et al. (2021) reported 14 patients from 12 families harboring 10 different *LRSAM1* variants (7 novel), predominantly dominant ([PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)).

| Variant | Type | Inheritance | Source |
|---|---|---|---|
| Intronic splice-acceptor AG→AA (frameshift/truncation, complete LOF) | Splice-site | Recessive (homozygous) | [PMID: 20865121](https://pubmed.ncbi.nlm.nih.gov/20865121/) |
| p.Leu708Argfs\*28 | Frameshift (RING domain) | Dominant | [PMID: 22012984](https://pubmed.ncbi.nlm.nih.gov/22012984/) |
| p.Pro707Leu | Missense (RING) | Dominant | [PMID: 28335037](https://pubmed.ncbi.nlm.nih.gov/28335037/) |
| p.Cys694Tyr | Missense (RING) | Dominant (reclassified CMT2G→CMT2P) | [PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/) |

**Variant classification (ACMG/AMP).** Interpretation is challenging precisely because pathogenic variants cluster at the 3′ end where premature-termination codons **may or may not escape NMD**; careful application of PVS1 and related criteria is required depending on exact position and predicted NMD outcome ([PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)).

> "Variants at the 3`end may or may not escape from nonsense-mediated decay, thereby defining the pattern of inheritance" — Reilich et al., [PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)

> "clustering of pathogenic variants in 3´-prime exons, interpretation of genetic variants in LRSAM1 is challenging" — Reilich et al., [PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)

**Functional consequences.**
- **Recessive** variants → complete loss of LRSAM1 protein → **loss of function**.
- **Dominant** variants → truncated RING-domain protein escaping NMD → **dominant-negative** effect on ligase activity ([PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)).

> "the C-terminal RING domain, which exerts a dominant-negative effect on protein function, whenever affected by an altered or truncated protein" — Reilich et al., [PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)

**Allele frequency / somatic vs germline.** All disease variants are **germline** and rare (not established as recurrent population polymorphisms); LRSAM1 mutations are considered rare even within CMT2 ([PMID: 28335037](https://pubmed.ncbi.nlm.nih.gov/28335037/)). No somatic (COSMIC/cancer) role is relevant.

**Modifier genes / epigenetics / chromosomal abnormalities.** Possible *RAB7A × LRSAM1* interaction and a gender effect were proposed as phenotype modifiers ([PMID: 27462242](https://pubmed.ncbi.nlm.nih.gov/27462242/)). No epigenetic mechanisms or large chromosomal abnormalities are implicated; transcriptomic changes (upregulation of *NEDD4L* and *TNFRSF21*) were seen with the p.Cys694Tyr mutation ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious agents cause CMT2P — it is a purely genetic disorder. The only mechanistically relevant environmental link is experimental: LRSAM1-deficient mouse axons are **more sensitive to the neurotoxin acrylamide** ([PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)), raising the theoretical possibility that neurotoxic exposures could exacerbate axonal vulnerability. Of interest to the protein's normal biology, LRSAM1 participates in **anti-bacterial autophagy (xenophagy)** of intracellular *Salmonella* Typhimurium ([PMID: 23245322](https://pubmed.ncbi.nlm.nih.gov/23245322/)), but there is no evidence infection triggers the neuropathy.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A germline pathogenic variant arises in ***LRSAM1***, clustered in the 3′ exons encoding the **C-terminal RING domain**.
2. Depending on variant position and NMD, this **leads to** one of two states:
   - **(Recessive branch)** biallelic loss → NMD/complete absence of LRSAM1 protein → total **loss of E3 ligase function**; **or**
   - **(Dominant branch)** a truncated protein that escapes NMD → a **dominant-negative** RING-domain protein that poisons residual ligase activity.
3. Either state **results in** disrupted **E2–E3 interaction**, the essential step for transferring ubiquitin from the E2 conjugating enzyme to substrates — thereby **abrogating LRSAM1-mediated ubiquitylation** ([PMID: 28335037](https://pubmed.ncbi.nlm.nih.gov/28335037/)).
4. Loss of ubiquitylation of the validated target **TSG101** (an ESCRT-I component) **impairs** endosomal sorting / multivesicular-body (MVB) trafficking and receptor endocytosis ([PMID: 15256501](https://pubmed.ncbi.nlm.nih.gov/15256501/)) — *inferred* to perturb membrane/protein homeostasis in neurons.
5. Impaired proteostasis and trafficking **lowers the threshold** for **length-dependent distal axonal degeneration** — demonstrated indirectly by heightened axonal vulnerability to neurotoxic stress in the mouse model ([PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)).
6. Degeneration of the longest peripheral motor and sensory axons **produces** distal muscle weakness/atrophy, distal sensory loss, neuropathic pain, areflexia, pes cavus, and gait impairment — the CMT2P phenotype.
7. **(Branch — CNS extension, inferred)** In some individuals the same ligase dysfunction **is associated with** later degeneration affecting the substantia nigra, **manifesting as** late-onset parkinsonism ([PMID: 26900582](https://pubmed.ncbi.nlm.nih.gov/26900582/), [PMID: 40721190](https://pubmed.ncbi.nlm.nih.gov/40721190/)); the mechanism connecting LRSAM1 to nigral neurons remains undefined.

### Causal chain diagram

```
        LRSAM1 pathogenic variant (3' RING-encoding exons, chr9q33.3)
                              |
         ┌────────────────────┴────────────────────┐
   (recessive)                                (dominant)
 biallelic, NMD →                       PTC escapes NMD →
 complete loss of LRSAM1               truncated RING protein
        |                                        |
        └───────────────┬────────────────────────┘
                        v
        Disrupted E2–E3 interaction  →  loss of ubiquitylation activity
                        v
     ↓ Ubiquitination of TSG101 (ESCRT-I)  →  impaired endosomal/MVB trafficking
                        v
     Perturbed neuronal proteostasis & membrane homeostasis (inferred)
                        v
     ↑ Vulnerability to length-dependent DISTAL AXON DEGENERATION
       (mouse: unmasked by neurotoxic stress; ↑TNFRSF21)
                        v
   ┌────────────────────┴──────────────────────────┐
   v                                                v
 PNS phenotype:                          CNS extension (some patients):
 distal weakness, sensory loss,          late-onset parkinsonism
 neuropathic pain, pes cavus,            (substantia nigra; mechanism unknown)
 areflexia, gait impairment
```

### Supporting detail

- **Molecular pathway / biochemical defect.** The core lesion is in the **ubiquitin–proteasome / ubiquitin-conjugation pathway**. LRSAM1 is a RING E3 ligase; RING-domain variants cause "*loss of the E2-E3 interaction that is an essential prerequisite for supporting ubiquitylation of target substrates*" ([PMID: 28335037](https://pubmed.ncbi.nlm.nih.gov/28335037/)).
- **Protein function.** Two functional modules: the **LRR domain targets** substrates (e.g., cytosolic bacteria) and the **RING domain catalyzes** ubiquitin transfer — "*these functions require LRSAM1's leucine-rich repeat and RING domains, respectively*" ([PMID: 23245322](https://pubmed.ncbi.nlm.nih.gov/23245322/)).
- **Cellular processes.** Endosomal/ESCRT trafficking, MVB and retrovirus budding (via TSG101 monoubiquitination, [PMID: 15256501](https://pubmed.ncbi.nlm.nih.gov/15256501/)); autophagy/xenophagy; and, downstream, **axon degeneration**. Transcriptomic profiling of patient cells implicated *TNFRSF21* (a regulator of axonal degeneration) and pathways shared with ALS and Alzheimer disease ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)).
- **Subcellular localization.** In transfected cells LRSAM1 localizes to a **perinuclear compartment just beyond the Golgi** ([PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)).

**Upstream vs downstream:** the mutation and lost ubiquitylation are **upstream**; trafficking/proteostasis defects are **intermediate**; distal axonal degeneration and clinical signs are **downstream**.

**Suggested ontology terms.** GO:0016567 (protein ubiquitination), GO:0004842 (ubiquitin-protein transferase activity), GO:0061630 (ubiquitin protein ligase activity), GO:0007032 (endosome organization), GO:0098930 (axonal transport), GO:0006914 (autophagy). **Cell types (CL):** CL:0000101 (sensory neuron), CL:0000100 (motor neuron), CL:0002573 (Schwann cell). **Cellular components:** GO:0005768 (endosome), GO:0000813 (ESCRT-I complex), GO:0005794 (Golgi apparatus).

---

## 7. Anatomical Structures Affected

**Organ / system level.** The **peripheral nervous system** is primary (UBERON:0000010). Body system: nervous system (UBERON:0001016). Secondary/musculoskeletal involvement includes distal limb muscles and the **foot/skeleton** (pes cavus, foot deformity); CMT patients also show an under-recognized rate of **hip acetabular dysplasia** (21% of imaged CMT patients in one series — [PMID: 40432997](https://pubmed.ncbi.nlm.nih.gov/40432997/)). The emerging CNS extension implicates the **substantia nigra / basal ganglia** ([PMID: 26900582](https://pubmed.ncbi.nlm.nih.gov/26900582/)).

**Tissue / cell level.** Nervous tissue — **peripheral motor and sensory axons**; LRSAM1 is abundantly expressed in PNS motor and sensory neurons ([PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)). Affected cells: **motor neurons (CL:0000100)** and **sensory neurons (CL:0000101)**; skeletal muscle secondarily denervated (CL:0000188).

**Subcellular level.** Endosome/MVB (GO:0005768), ESCRT-I complex (GO:0000813), Golgi-adjacent perinuclear compartment (GO:0005794).

**Localization.** Distal, length-dependent, **bilateral and symmetric**, lower limbs > upper limbs. Suggested UBERON: UBERON:0001322 (sciatic nerve) and distal peroneal/tibial nerve territory; spinal cord and CNS not primarily affected in the classic peripheral phenotype.

---

## 8. Temporal Development

- **Onset:** adult/late, typically **2nd to 5th decade**; **insidious/chronic** ([PMID: 33568173](https://pubmed.ncbi.nlm.nih.gov/33568173/)). A rare **early-onset autosomal dominant** family has been reported ([PMID: 38330802](https://pubmed.ncbi.nlm.nih.gov/38330802/)).
- **Progression:** **slow and progressive**; generally mild ("quiescent") axonal neuropathy ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)).
- **Course pattern:** chronic, lifelong, non-remitting, non-episodic.
- **Critical periods / CNS window:** late-onset parkinsonism appears **years after** neuropathy onset (ages ~50–65) in some patients ([PMID: 26900582](https://pubmed.ncbi.nlm.nih.gov/26900582/)).

---

## 9. Inheritance and Population

**Epidemiology.** CMT overall affects ~**1:2,500** worldwide with >100 known genetic causes ([PMID: 40219666](https://pubmed.ncbi.nlm.nih.gov/40219666/)). CMT2P is a **rare** subtype; *LRSAM1* mutations are uncommon even within CMT2 ([PMID: 28335037](https://pubmed.ncbi.nlm.nih.gov/28335037/)). Precise CMT2P prevalence/incidence are not established.

> "Affecting about ~1:2,500 people worldwide, CMT has over 100 known genetic causes, leading to different subtypes with varying disease severity and progression." — Stavrou et al., [PMID: 40219666](https://pubmed.ncbi.nlm.nih.gov/40219666/)

**Inheritance.** **Both autosomal dominant (predominant) and autosomal recessive**, determined by variant location and NMD outcome (see Section 4). Dominant = dominant-negative RING variants escaping NMD; recessive = biallelic complete loss ([PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)).

**Penetrance / expressivity.** **Incomplete penetrance** and **variable expressivity**, including asymptomatic carriers detectable only by lower-limb muscle MRI ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/), [PMID: 33568173](https://pubmed.ncbi.nlm.nih.gov/33568173/)).

**Founder effects / consanguinity.** The original recessive kindred was a large **consanguineous eastern Canadian** family (homozygous founder-type splice variant) ([PMID: 20865121](https://pubmed.ncbi.nlm.nih.gov/20865121/)). Carrier status for the recessive LRSAM1 allele has been incidentally detected in idiopathic neuropathy cohorts ([PMID: 39290488](https://pubmed.ncbi.nlm.nih.gov/39290488/)).

**Demographics.** No strong ethnic predilection; reported families span Canada, the Netherlands, and others. Sex ratio not clearly skewed, though gender was proposed as a modifier in one family ([PMID: 27462242](https://pubmed.ncbi.nlm.nih.gov/27462242/)). Genetic anticipation and germline mosaicism are not established.

---

## 10. Diagnostics

**Clinical / electrophysiology.** Diagnosis rests on **nerve conduction studies / EMG** demonstrating an **axonal** (rather than demyelinating) sensorimotor neuropathy: reduced amplitudes with relatively preserved conduction velocities ([PMID: 40721190](https://pubmed.ncbi.nlm.nih.gov/40721190/)). Clinical exam shows distal weakness, sensory loss, areflexia, pes cavus.

**Imaging.** **MRI of lower-limb musculature** systematically reveals **fatty atrophy** in both clinical and subclinical carriers and is useful to detect minimal/subclinical disease ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)).

**Genetic testing (definitive).** Diagnosis is confirmed by identifying a pathogenic *LRSAM1* variant. Recommended approach: **multigene neuropathy/CMT panel or exome sequencing**, given the >100 CMT genes; targeted *LRSAM1* analysis when phenotype/family history suggests it. LRSAM1 is included on inherited neuromuscular gene panels ([PMID: 39290488](https://pubmed.ncbi.nlm.nih.gov/39290488/)). Careful ACMG interpretation of 3′ PTC variants (NMD escape) is essential ([PMID: 33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/)). Chromosomal microarray, karyotyping, FISH, mitochondrial and repeat-expansion testing are **not** relevant to CMT2P.

**Omics diagnostics.** Not standard; research transcriptome profiling of patient lymphoblasts has shown disease-associated expression changes ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)).

**Differential diagnosis.** Other axonal CMT2 subtypes (CMT2A/*MFN2*, CMT2B/*RAB7A*, CMT2K/*GDAP1*, etc.), hereditary transthyretin (ATTRv) amyloidosis (important treatable mimic — [PMID: 39290488](https://pubmed.ncbi.nlm.nih.gov/39290488/)), CMT1 (demyelinating; *PMP22*), acquired/idiopathic axonal polyneuropathies, and ALS5/SPG11 overlap syndromes ([PMID: 26556829](https://pubmed.ncbi.nlm.nih.gov/26556829/)).

**Screening.** Cascade genetic testing of at-risk relatives once a familial variant is known; no population newborn screening.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy: normal.** CMT2P is not life-limiting; by analogy to other CMT the disease "*reflects a process of normal ageing*" with **normal life expectancy** ([PMID: 24646194](https://pubmed.ncbi.nlm.nih.gov/24646194/)).
- **Morbidity / disability.** Chronic, slowly progressive **mobility impairment**, foot deformity, falls risk, and **neuropathic pain** dominate; wheelchair dependence is uncommon given the mild course.
- **Complications.** Foot deformities requiring surgery; possible hip acetabular dysplasia in CMT broadly ([PMID: 40432997](https://pubmed.ncbi.nlm.nih.gov/40432997/)); **late-onset parkinsonism** as a distinct CNS complication in some LRSAM1 patients ([PMID: 26900582](https://pubmed.ncbi.nlm.nih.gov/26900582/)).
- **Prognostic factors.** Variant type/inheritance (dominant-negative vs LOF), and modifiers such as gender/second-gene interaction ([PMID: 27462242](https://pubmed.ncbi.nlm.nih.gov/27462242/)). No validated molecular prognostic biomarkers.

---

## 12. Treatment

**No curative therapy exists; management is symptomatic and supportive.**

> "Currently, no curative treatment exists for CMT. Management focuses on symptomatic interventions, including orthotic support, surgical procedures, and physical therapy." — Kikuchi, [PMID: 40636623](https://pubmed.ncbi.nlm.nih.gov/40636623/)

| Modality | Intervention | Suggested NCIT |
|---|---|---|
| Orthotics | Ankle-foot orthoses (AFOs) for foot drop | NCIT:C50008 (orthotic device) |
| Rehabilitation | Physical therapy, occupational therapy | NCIT:C15327 (physical therapy) |
| Surgical | Correction of pes cavus / foot deformity | NCIT:C15329 (surgery) |
| Pharmacologic (supportive) | Neuropathic pain control (gabapentinoids, duloxetine, TCAs) | NCIT:C15224 (pain management) |
| Genetic counseling | Family risk assessment | NCIT:C15633 (genetic counseling) |

**Experimental / disease-modifying (CMT broadly, not LRSAM1-specific).** No approved disease-modifying drug for CMT2P. Across CMT, **gene therapy** (silencing/replacement/editing via AAV vectors) is under active preclinical/early-clinical development but faces blood–nerve/brain-barrier delivery, immunogenicity, and scalability challenges ([PMID: 40219666](https://pubmed.ncbi.nlm.nih.gov/40219666/)). Other emerging approaches include **PMP22 silencers** (for CMT1A), **HDAC6 inhibitors**, and **govorestat** (aldose reductase inhibitor, CMT-SORD trial) — none specific to LRSAM1 ([PMID: 40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/)).

> "Currently, there are no approved treatments and care focuses on managing symptoms." — Stavrou et al., [PMID: 40219666](https://pubmed.ncbi.nlm.nih.gov/40219666/)

**Pharmacogenomics / personalized medicine.** No LRSAM1-specific pharmacogenomic guidance. The dual LOF-vs-dominant-negative mechanism implies **different rational strategies** (gene replacement for recessive LOF; allele-specific silencing for dominant-negative alleles) — currently conceptual.

---

## 13. Prevention

CMT2P cannot be prevented (genetic). Prevention is limited to **reproductive/genetic risk management** and **complication avoidance**:

- **Primary:** Genetic counseling, carrier/cascade testing, and reproductive options (prenatal testing, preimplantation genetic diagnosis) for known familial variants (general CMT precedent — [PMID: 24646194](https://pubmed.ncbi.nlm.nih.gov/24646194/)).
- **Secondary:** Early detection of subclinical carriers via lower-limb muscle MRI ([PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)); early physiotherapy/orthotics.
- **Tertiary:** Prevent complications — orthotic support to prevent falls/deformity progression, monitoring for hip dysplasia and, given the emerging link, parkinsonian features.
- **Behavioral:** Theoretical avoidance of neurotoxic exposures (extrapolated from acrylamide sensitivity in the mouse model, [PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)) — not a clinical guideline.

No immunization, public-health, or infectious-control measures apply.

---

## 14. Other Species / Natural Disease

- **Model species:** *Mus musculus* (NCBI Taxon 10090) — the *Lrsam1* mutant mouse ([PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)).
- **Orthologous gene:** mouse *Lrsam1*, abundantly expressed in PNS motor and sensory neurons.
- **Natural disease in companion animals/wildlife:** No naturally occurring LRSAM1/CMT2P disease documented in other species (OMIA); the LRR–RING E3-ligase function is **evolutionarily conserved**, and the protein's ubiquitin-dependent xenophagy role is conserved across mammalian cells ([PMID: 23245322](https://pubmed.ncbi.nlm.nih.gov/23245322/)).
- **Zoonotic potential:** None (non-infectious genetic disease).

---

## 15. Model Organisms

**Mouse (*Lrsam1* mutant).** The principal model ([PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)):

- **Phenotype recapitulation (partial):** Both homozygous and heterozygous mice have **largely normal neuromuscular performance and only very mild age-related neuropathy** — milder than the human disease.
- **Key finding — sensitized axons:** mutant axons are hypersensitive to axonal neurotoxin challenge.

> "Lrsam1 mutant mice are more sensitive to challenge with acrylamide, a neurotoxic agent that causes axon degeneration, indicating that the axons in the mutant mice are indeed compromised" — Bogdanik et al., [PMID: 23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/)

- **Localization insight:** LRSAM1 localizes to a **perinuclear post-Golgi compartment**, with little colocalization with endosome-to-lysosome trafficking machinery.
- **Limitations:** Mild phenotype limits modeling of overt human neuropathy; does not capture dominant-negative human biology or the parkinsonism extension.
- **Cellular / in vitro models:** Patient lymphoblasts/fibroblasts for ubiquitylation assays and transcriptomics ([PMID: 28335037](https://pubmed.ncbi.nlm.nih.gov/28335037/), [PMID: 27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/)); in vitro ubiquitylation reconstitution to test E2–E3 interaction defects.
- **Resources:** MGI (mouse) and standard CMT model repositories.

---

## Mechanistic Model / Interpretation

The unifying theme is **failure of a RING E3 ubiquitin ligase**, converging on impaired proteostasis and endosomal trafficking in neurons. CMT2P is mechanistically distinctive within CMT2 for two reasons: (a) its **position-dependent dual inheritance**, in which NMD escape/triggering of a 3′ premature-termination codon decides whether disease is dominant (dominant-negative) or recessive (complete loss of function); and (b) a **dominant-negative** mode operating for most disease alleles. The recurrent link to parkinsonism situates LRSAM1 within broader **ubiquitin-proteostasis neurodegeneration** biology — echoed by patient-cell transcriptomes sharing pathways with ALS and Alzheimer disease — and suggests the same ligase defect can, over decades, extend from the longest peripheral axons to vulnerable central (nigral) neurons.

---

## Evidence Base

| PMID | Study | Contribution |
|---|---|---|
| [20865121](https://pubmed.ncbi.nlm.nih.gov/20865121/) | Guernsey et al. 2010 | First identified *LRSAM1* as causal (recessive splice variant, complete LOF) |
| [22012984](https://pubmed.ncbi.nlm.nih.gov/22012984/) | Weterman et al. 2012 | Dominant RING frameshift p.Leu708Argfs\*28 (LOD 5.12) |
| [28335037](https://pubmed.ncbi.nlm.nih.gov/28335037/) | Hakonen et al. 2017 | Biochemical defect: RING variants disrupt E2–E3 interaction, abrogate ubiquitylation |
| [33414056](https://pubmed.ncbi.nlm.nih.gov/33414056/) | Reilich et al. 2021 | Genotype–phenotype: 3′ clustering, NMD determines inheritance, dominant-negative RING |
| [33568173](https://pubmed.ncbi.nlm.nih.gov/33568173/) | Palaima et al. 2021 (review) | Clinical spectrum; TSG101 as main substrate; domain architecture |
| [27686364](https://pubmed.ncbi.nlm.nih.gov/27686364/) | 2016 | CMT2G reclassified as CMT2P (p.Cys694Tyr); MRI subclinical detection; transcriptome |
| [23519028](https://pubmed.ncbi.nlm.nih.gov/23519028/) | Bogdanik et al. 2013 | Mouse model: mild phenotype, acrylamide sensitization, localization |
| [15256501](https://pubmed.ncbi.nlm.nih.gov/15256501/) | Amit et al. 2004 | LRSAM1/Tal ubiquitinates TSG101; ESCRT/MVB & retrovirus budding |
| [23245322](https://pubmed.ncbi.nlm.nih.gov/23245322/) | Huett et al. 2012 | LRR (targeting) + RING (catalytic) domains; anti-bacterial xenophagy |
| [26900582](https://pubmed.ncbi.nlm.nih.gov/26900582/) | Aerts et al. 2016 | Parkinsonism in 3/5 affected family members — CNS extension |
| [40721190](https://pubmed.ncbi.nlm.nih.gov/40721190/) | Ducatel et al. 2025 | CMT2P with parkinsonism case — corroborates CNS link |
| [40219666](https://pubmed.ncbi.nlm.nih.gov/40219666/) | Stavrou et al. 2025 | CMT prevalence (1:2,500); no approved treatments; gene-therapy status |
| [40636623](https://pubmed.ncbi.nlm.nih.gov/40636623/) | Kikuchi 2025 | Symptomatic management (orthotics, PT, surgery) |
| [40014417](https://pubmed.ncbi.nlm.nih.gov/40014417/) | De Grado et al. 2025 | Current CMT therapeutics landscape / trials |
| [38330802](https://pubmed.ncbi.nlm.nih.gov/38330802/) | 2024 | Early-onset autosomal dominant CMT2P family |
| [27462242](https://pubmed.ncbi.nlm.nih.gov/27462242/) | 2016 | Gender & *RAB7A/LRSAM1* interaction as phenotype modifiers |
| [39290488](https://pubmed.ncbi.nlm.nih.gov/39290488/) | 2024 | LRSAM1 carrier detected on neuropathy gene panel |
| [24646194](https://pubmed.ncbi.nlm.nih.gov/24646194/) | 2014 | CMT precedent: normal life expectancy, symptomatic care |
| [40432997](https://pubmed.ncbi.nlm.nih.gov/40432997/) | 2025 | Hip acetabular dysplasia in CMT (21%) |
| [26556829](https://pubmed.ncbi.nlm.nih.gov/26556829/) | 2015 | ALS5/SPG11 overlap — differential diagnosis context |

**Evidence source types:** human clinical/genetic (family & cohort studies, reviews), model organism (mouse), and in vitro/biochemical (ubiquitylation assays, cell transfection).

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** No reliable prevalence/incidence, sex ratio, or natural-history quantitation specific to CMT2P; most data come from individual pedigrees and case reports.
2. **Substrate biology is incomplete.** TSG101 is the only well-validated LRSAM1 ubiquitylation target relevant to disease; how impaired TSG101/ESCRT function specifically drives *axonal* degeneration is inferred, not demonstrated.
3. **Genotype–phenotype uncertainty.** NMD escape/dominant-negative predictions for 3′ PTC variants are not always experimentally verified, complicating ACMG classification.
4. **Mouse model is mild.** The *Lrsam1* mouse under-recapitulates overt human neuropathy and does not model the dominant-negative or parkinsonism aspects.
5. **The parkinsonism link is preliminary.** Based on one family plus isolated cases; causality, penetrance, and mechanism (LRSAM1 in substantia nigra) are unknown.
6. **No disease-specific therapy or biomarkers.** All treatments are symptomatic; no validated prognostic molecular markers.

---

## Proposed Follow-up Experiments / Actions

1. **Functional NMD/dominant-negative assays** for each reported 3′ *LRSAM1* PTC variant (patient RNA + minigene assays) to firm up ACMG calls and inheritance prediction.
2. **iPSC-derived motor/sensory neurons** carrying dominant-negative vs LOF *LRSAM1* alleles to test axonal degeneration, ESCRT/TSG101 trafficking, and stress vulnerability — bridging the mild mouse-model gap.
3. **Expand substrate mapping** (ubiquitylation proteomics) in neurons to identify axon-relevant LRSAM1 targets beyond TSG101.
4. **Systematic ascertainment of parkinsonism/CNS features** across LRSAM1 cohorts (DAT-SPECT imaging, longitudinal follow-up) to establish frequency, penetrance, and mechanism of the CNS extension.
5. **Allele-specific silencing (dominant alleles) and gene replacement (recessive LOF)** proof-of-concept in cellular/mouse models, leveraging the AAV gene-therapy platforms being developed for CMT broadly.
6. **Registry-based natural history study** to define CMT2P prevalence, progression rate, and disability trajectory, enabling future trial readiness.
7. **Test neurotoxic-exposure interaction** clinically/epidemiologically, motivated by acrylamide hypersensitivity in the mouse model.

---

*Report compiled from an autonomous multi-iteration literature investigation (8 confirmed findings, 21 papers reviewed). Evidence is predominantly human genetic/clinical and model-organism; CMT2P remains a rare, symptomatically managed axonal neuropathy with an emerging CNS dimension.*


## Artifacts

- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Axonal_Type_2P-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Axonal_Type_2P-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 20 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013749` (2 mentions) - the report calls it "Charcot-Marie-Tooth disease, axonal, type 2P", "Suggested MONDO"; MONDO calls it **ventricular septal defect 3**
- `HP:0001761` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Pes cavus**
- `HP:0009027` (1 mention) - the report calls it "Clinical sign"; HP calls it **Foot dorsiflexor weakness**
- `NCIT:C15224` (1 mention) - the report calls it "pain management"; NCIT calls it **Nutrition Research, Fats**
- `NCIT:C15633` (1 mention) - the report calls it "genetic counseling"; NCIT calls it **Cancer Pain Management**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C50008` (1 mention) - the report calls it "orthotic device"; NCIT calls it **Interface Device**
- `NCIT:C15327` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Lumbar Puncture**, and lists "Spinal Tap" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0013749` - called "Charcot-Marie-Tooth disease, axonal, type 2P", "Suggested MONDO"