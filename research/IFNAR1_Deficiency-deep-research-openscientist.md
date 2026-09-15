---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T20:52:39.091282'
end_time: '2026-09-13T21:05:52.286130'
duration_seconds: 793.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IFNAR1 Deficiency
  mondo_id: MONDO:0030970
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 20
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 8
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0030970
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 106, susceptibility to viral infections
  - term_id: HP:0002090
    reported_labels:
    - Clinical sign
    ontology_label: Pneumonia
  - term_id: HP:0002383
    reported_labels:
    - Clinical sign
    ontology_label: Infectious encephalitis
  - term_id: HP:0032251
    reported_labels:
    - Abnormal susceptibility to viral infection
    ontology_label: Abnormal immune system morphology
  - term_id: GO:0005886
    reported_labels:
    - Subcellular level:** IFNAR1 is a **plasma membrane** receptor
    ontology_label: plasma membrane
  - term_id: NCIT:C15320
    reported_labels:
    - Supportive Care
    ontology_label: Study Design
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: IFNAR1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: IFNAR1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IFNAR1 Deficiency
- **MONDO ID:** MONDO:0030970 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IFNAR1 Deficiency** covering all of the
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

# IFNAR1 Deficiency: A Comprehensive Disease Characteristics Report

**Disease:** IFNAR1 Deficiency (Autosomal Recessive)
**MONDO ID:** MONDO:0030970 · **OMIM:** #619304 (Immunodeficiency 45) · **Gene OMIM:** *IFNAR1* 107450
**Category:** Mendelian inborn error of immunity (IEI)

---

## Summary

IFNAR1 deficiency is an ultra-rare **autosomal recessive inborn error of immunity** caused by biallelic loss-of-function (LOF) variants in *IFNAR1* (chromosome 21q22.11), the gene encoding interferon-alpha/beta receptor subunit 1. IFNAR1 pairs with IFNAR2 to form the shared cell-surface receptor for **all type I interferons (IFN-α, IFN-β, and IFN-ω)**. When IFNAR1 is absent or non-functional, cells cannot respond to any type I IFN, abolishing the JAK1/TYK2–STAT1/STAT2–ISGF3 signaling cascade that drives interferon-stimulated gene (ISG) expression and intrinsic antiviral defense. The functional signature is definitive: patient fibroblasts show no response to IFN-α2, IFN-ω, or IFN-β [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/).

The clinical hallmark is a striking dissociation between baseline health and catastrophic response to specific viral challenges. Affected individuals are typically **otherwise healthy and develop normally** until they encounter a live attenuated vaccine (measles-mumps-rubella, MMR; or yellow fever 17D) or a select wild-type virus (notably SARS-CoV-2), whereupon uncontrolled viral replication produces severe, sometimes fatal disseminated disease — encephalitis, pneumonitis, hepatitis, and multiorgan involvement. This pattern illustrates an **"essential but narrow" role for type I IFN in human antiviral immunity**: unlike mice, humans display considerable redundancy in type I IFN protection under natural conditions, so the phenotype is dominated by attenuated-vaccine viruses and a handful of wild-type pathogens rather than by broad, everyday viral susceptibility.

The disease has a notable population genetics dimension: a **Polynesian founder allele, p.Glu386\* (nonsense)**, reaches a minor allele frequency above 1% in Samoa and is distributed across western Polynesia, making regional consideration essential before live vaccination. Diagnosis combines genetic testing (WES/WGS/IEI panels, with copy-number analysis for large deletions) and functional confirmation of absent type I IFN responses, while carefully excluding the **acquired phenocopy** — neutralizing autoantibodies against type I IFNs, found in 10–15% of critical COVID-19 pneumonia cases. Management is fundamentally preventive: strict avoidance of live attenuated vaccines, supportive/antiviral care during viral episodes, cascade screening of relatives, and hematopoietic stem cell transplantation (HSCT) as a rational curative option in severe disease. There is no approved disease-specific pharmacotherapy, and exogenous type I IFN is useless because the receptor is absent.

---

## 1. Disease Information

IFNAR1 deficiency is a Mendelian inborn error of immunity characterized by selective vulnerability to certain viruses and live attenuated viral vaccines, with intact immunity to most other pathogens. It was first described in 2019 in otherwise healthy patients who suffered life-threatening disease after MMR and yellow fever vaccination [PMID: 31270247](https://pubmed.ncbi.nlm.nih.gov/31270247/).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0030970 |
| OMIM (phenotype) | #619304 (Immunodeficiency 45) |
| OMIM (gene) | *IFNAR1* 107450 |
| Gene (HGNC) | *IFNAR1* (HGNC:5432) |
| Cytogenetic locus | 21q22.11 |
| Inheritance | Autosomal recessive |

**Synonyms / alternative names:** Immunodeficiency 45 (IMD45); autosomal recessive IFNAR1 deficiency; interferon alpha/beta receptor 1 deficiency; type I interferon receptor 1 deficiency.

**Information source:** The disease-level knowledge derives primarily from **aggregated case series and functional immunology studies** (Hernandez et al. 2019; Bastard et al. 2022; Abolhassani et al. 2022; Azamor et al. 2026), not from EHR/population-scale data, reflecting the ultra-rare nature of the condition.

> *"Globally, autosomal recessive IFNAR1 deficiency is a rare inborn error of immunity underlying susceptibility to live attenuated vaccine and wild-type viruses."* — [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/)

---

## 2. Etiology

**Disease causal factor (genetic):** The sole cause is **biallelic loss-of-function variants in *IFNAR1***. This is a monogenic, molecularly fully penetrant defect. Cellular responses to all type I IFNs are abolished [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/).

**Genetic risk factors:** The disease *is* the genotype — homozygous or compound heterozygous LOF *IFNAR1* variants. No additional susceptibility loci are required. The most important population-specific genetic risk factor is the **Polynesian founder allele p.Glu386\***, enriched in individuals of Polynesian (especially Samoan) ancestry.

**Environmental "risk factors" (disease-precipitating triggers):** Because baseline health is preserved, disease manifestation is triggered by specific environmental exposures:
- **Live attenuated vaccines:** MMR, yellow fever 17D (YF-17D).
- **Wild-type viruses:** SARS-CoV-2 (critical COVID-19 pneumonia), and other viruses in individual reports.

**Protective factors:** The principal "protective" measure is behavioral/medical — **avoidance of live attenuated vaccines**. No genetic protective modifier alleles have been established for this disease.

**Gene–environment interaction:** This disease is a paradigmatic **monogenic gene × environment interaction** — an inherited receptor defect that is clinically silent until an environmental viral trigger (vaccine or wild-type virus) unmasks it, producing life-threatening disease.

---

## 3. Phenotypes

The phenotype is dominated by **infectious/post-vaccination events** rather than constitutional features. Between triggers, patients are typically asymptomatic and grow normally.

| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Adverse reaction to live attenuated vaccine (MMR, YF) | Clinical event | HP:0002090 (Pneumonia), HP:0002383 (Encephalitis) | Childhood (post-vaccination) | Severe/life-threatening | Presenting feature in index cases |
| Viral encephalitis | Clinical sign | HP:0002383 | Variable | Severe | Reported |
| Severe/critical viral pneumonia (incl. COVID-19) | Clinical sign | HP:0002090 | Any age | Severe | Reported |
| Disseminated viral infection / viral hepatitis | Clinical sign | HP:0006562 (Viral hepatitis) | Variable | Severe | Reported |
| Susceptibility to viral infection | Lab/clinical | HP:0032251 (Abnormal susceptibility to viral infection) | Variable | Variable | Core |
| Otherwise normal immunity/health between triggers | — | — | — | — | Characteristic |

**Onset:** Typically childhood, coincident with the routine live-vaccine schedule; can also present in adulthood upon wild-type viral challenge (e.g., adult critical COVID-19).

**Severity/progression:** Episodic and trigger-dependent. Individual episodes can be fulminant and fatal, but there is no constitutive, progressive organ degeneration between events.

**Quality-of-life impact:** Between episodes, QoL is generally normal. The dominant burden is the risk of catastrophic disease upon exposure and the lifelong requirement to avoid live vaccines and manage viral exposures. No disease-specific EQ-5D/SF-36 data are available (reflecting rarity).

> *"Vaccination against measles, mumps, and rubella (MMR) and yellow fever (YF) with live attenuated viruses can rarely cause life-threatening disease."* — [PMID: 31270247](https://pubmed.ncbi.nlm.nih.gov/31270247/)

---

## 4. Genetic / Molecular Information

**Causal gene:** *IFNAR1* (interferon alpha and beta receptor subunit 1), HGNC:5432, located at chromosome **21q22.11**. Gene OMIM 107450; disease phenotype OMIM #619304.

**Pathogenic variants (spectrum):**

| Variant | Type | Population | Consequence | Reference |
|---|---|---|---|---|
| p.Glu386\* (nonsense) | Truncating LOF | Polynesian founder (MAF >1% in Samoa) | Truncated protein absent from cell surface | [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/) |
| Large homozygous deletion | Structural / CNV | Individual case | Complete LOF | [PMID: 35091979](https://pubmed.ncbi.nlm.nih.gov/35091979/) |
| CNV Δ3-4-5 (homozygous) | Structural / CNV | Brazilian family | Receptor dysfunction; fatal YF vaccine adverse event | [PMID: 42097348](https://pubmed.ncbi.nlm.nih.gov/42097348/) |

**Variant classification:** Reported disease-causing variants are **pathogenic** (nonsense, large deletions, CNVs) per ACMG/AMP, all producing loss of function.

**Functional consequence:** **Loss of function** — abolished expression or surface localization of IFNAR1, eliminating the type I IFN receptor complex. The founder allele encodes a **truncated protein absent from the cell surface**.

**Allele frequency:** The founder p.Glu386\* allele is >1% MAF in Samoa but is extremely rare or absent in non-Polynesian populations. Other variants are private/ultra-rare.

**Somatic vs germline:** **Germline.** (Somatic *IFNAR1* down-regulation by viruses — e.g., SARS-CoV-2-induced IFNAR1 ubiquitination [PMID: 34260266](https://pubmed.ncbi.nlm.nih.gov/34260266/) — is a distinct immune-evasion phenomenon, not the inherited disease.)

**Modifier genes / epigenetics / large chromosomal abnormalities:** No established disease modifiers, epigenetic drivers, or aneuploidy associations specific to this monogenic disorder.

> *"All the patients are homozygous for the same nonsense IFNAR1 variant (p.Glu386\*). This allele encodes a truncated protein that is absent from the cell surface and is loss-of-function."* — [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/)

---

## 5. Environmental Information

**Environmental/infectious triggers (the operative "environmental" dimension):**
- **Live attenuated vaccines:** measles-mumps-rubella (MMR), yellow fever 17D.
- **Wild-type viruses:** SARS-CoV-2 (critical COVID-19 pneumonia); other viruses in individual reports.

**Toxins/pollution/occupational exposures:** Not implicated. **Lifestyle factors (smoking, diet, alcohol):** Not relevant to disease causation.

**Infectious agents:** The relevant "pathogens" are the **vaccine strains themselves** (attenuated measles, mumps, rubella, YF-17D) and specific wild-type viruses that normally depend on type I IFN for host containment.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic LOF variant in *IFNAR1*** (nonsense p.Glu386\*, deletion, or CNV) → **leads to** absent or non-functional IFNAR1 protein at the cell surface.
2. Absent IFNAR1 → **prevents** assembly of the type I IFN receptor (IFNAR1 + IFNAR2) → **results in** no ternary receptor complex upon IFN-α/β/ω binding.
3. No ternary complex → **fails to** juxtapose the receptor-associated kinases **JAK1 and TYK2** → they cannot cross-phosphorylate.
4. No JAK/TYK activation → **abolishes** phosphorylation of **STAT1/STAT2** → the **ISGF3 (STAT1–STAT2–IRF9)** complex does not form.
5. No ISGF3 → **eliminates** induction of **interferon-stimulated genes (ISGs)** → cells lose the type I IFN-driven antiviral state.
6. Loss of the antiviral state → **permits** uncontrolled replication of attenuated-vaccine viruses and select wild-type viruses in infected/target cells (e.g., fibroblasts highly vulnerable to SARS-CoV-2).
7. Uncontrolled viral replication → **causes** disseminated viral disease (encephalitis, pneumonitis, hepatitis, multiorgan involvement), which may be fatal.
   - *Branch (inferred):* In some contexts, aberrant innate/inflammasome activation upon viral trigger contributes to immunopathology (e.g., inflammasome-driven innate-cell activation upon YFV-17D exposure in a CNV case [PMID: 42097348](https://pubmed.ncbi.nlm.nih.gov/42097348/)).

### Detail by category

**Molecular pathway:** The **type I IFN → JAK-STAT (ISGF3) → ISG** axis (KEGG hsa04630 Jak-STAT signaling; Reactome "Interferon alpha/beta signaling"). Type I IFNs bind a receptor formed by IFNAR1 and IFNAR2, forming a ternary complex that brings JAK1 and TYK2 into proximity; they cross-phosphorylate each other, the receptor chains, and STATs, which then activate ISGs [PMID: 38608537](https://pubmed.ncbi.nlm.nih.gov/38608537/).

> *"Common to both are two distinct receptor chains (IFNAR1/IFNAR2 and IFNLR1/IL10R2), which form ternary complexes upon binding their respective ligands. This results in close proximity of the intracellularly associated kinases JAK1 and TYK2, which cross phosphorylate each other, the associated receptor chains, and signal transducer and activator of transcriptions, with the latter activating IFN-stimulated genes."* — [PMID: 38608537](https://pubmed.ncbi.nlm.nih.gov/38608537/)

**Cellular processes:** Loss of the cell-intrinsic antiviral state (impaired restriction of viral replication); GO:0060337 (type I interferon signaling pathway), GO:0051607 (defense response to virus).

**Protein dysfunction:** Loss of function of IFNAR1 — either the protein is truncated and fails to reach the plasma membrane (p.Glu386\*) or is deleted entirely.

**Immune system involvement:** This is an **immunodeficiency** (impaired intrinsic antiviral immunity), not primarily an autoimmune or autoinflammatory disease — though excessive innate/inflammasome activation can accompany a viral trigger. Notably, the *opposite* pole of IFN biology (excessive IFN-I signaling) causes type I interferonopathies, underscoring the pathway's dose-sensitivity.

**Species contrast (why the human phenotype is narrow):** In mice, type I IFN is essential against a broad range of viruses; in humans there is far more redundancy under natural conditions [PMID: 33729549](https://pubmed.ncbi.nlm.nih.gov/33729549/).

> *"A picture is emerging of greater redundancy of human type I IFNs for protective immunity to viruses in natural conditions than was initially anticipated."* — [PMID: 33729549](https://pubmed.ncbi.nlm.nih.gov/33729549/)

**Molecular profiling / functional readout:** IFNAR1-deficient fibroblasts show **no ISG induction** to IFN-α2/-β/-ω and are **highly vulnerable to SARS-CoV-2** (P = 1.2×10⁻¹¹ vs benign controls) [PMID: 35708626](https://pubmed.ncbi.nlm.nih.gov/35708626/).

> *"Fibroblasts deficient for IFNAR1, STAT2, or TYK2 are highly vulnerable to SARS-CoV-2."* — [PMID: 35708626](https://pubmed.ncbi.nlm.nih.gov/35708626/)

**Cell types / GO / CL suggestions:** Broadly acting because IFNAR1 is ubiquitously expressed — fibroblasts (CL:0000057), epithelial cells (CL:0000066), leukocytes/monocytes (CL:0000576), and other nucleated cells. GO terms: GO:0060337 (type I interferon signaling pathway), GO:0034340 (response to type I interferon), GO:0051607 (defense response to virus).

---

## 7. Anatomical Structures Affected

Because IFNAR1 is expressed on virtually all nucleated cells, the disease has **no fixed anatomical target**; rather, the organ affected is dictated by the tropism of the triggering virus.

- **Organ level:** Variable and virus-dependent — **lung** (viral/COVID-19 pneumonia; UBERON:0002048), **brain/CNS** (encephalitis; UBERON:0000955), **liver** (viral hepatitis; UBERON:0002107), with potential multiorgan dissemination.
- **Body systems:** Immune system (primary defect), with secondary respiratory, nervous, and hepatobiliary involvement during infectious episodes.
- **Tissue/cell level:** Any infected cell type; fibroblasts and epithelial cells are demonstrably permissive in vitro. CL terms: CL:0000057 (fibroblast), CL:0000066 (epithelial cell), CL:0000576 (monocyte).
- **Subcellular level:** IFNAR1 is a **plasma membrane** receptor (GO:0005886); signaling proceeds via cytoplasmic kinases/STATs to the **nucleus** (GO:0005634) for ISG transcription.
- **Localization / lateralization:** Determined by viral tropism; typically bilateral/systemic in disseminated disease.

---

## 8. Temporal Development

**Onset:** Congenital genetic defect, but **clinically silent until a triggering exposure**. Classic presentation is in **childhood** at the time of routine live-vaccine administration; adult presentation occurs with wild-type viral challenge (e.g., adult critical COVID-19).

**Onset pattern:** **Acute** — fulminant illness following vaccination or infection.

**Progression / course:** **Episodic**, trigger-dependent. There is no constitutive progressive degeneration; between episodes patients are typically well. Individual episodes can progress rapidly to severe/fatal disease.

**Disease duration:** The underlying genetic condition is **lifelong**; the risk persists indefinitely and requires lifelong avoidance of live vaccines.

**Remission:** Recovery from a viral episode is possible with supportive care and viral clearance; there is no "remission" of the underlying genetic defect.

**Critical periods:** The **peri-vaccination window** (routine childhood immunization schedule) is the key period of vulnerability and the main opportunity for prevention (withholding live vaccines).

---

## 9. Inheritance and Population

**Inheritance pattern:** **Autosomal recessive.** Recurrence risk for siblings of an affected proband is **25%**.

**Penetrance/expressivity:** At the molecular level, biallelic LOF fully abolishes type I IFN responses; **clinical** penetrance is **trigger-dependent** (an individual may remain well if never exposed to a triggering live vaccine or virus). Expressivity is variable, driven by which virus is encountered.

**Epidemiology:** Ultra-rare globally. Prevalence has not been formally established; knowledge is based on case reports and small series.

**Founder effect / affected populations:** A strong **Polynesian founder effect** — the p.Glu386\* allele has MAF >1% in Samoa and is also present in the Cook, Society, Marquesas, and Austral islands, and Fiji; it is extremely rare or absent elsewhere. Seven children from five unrelated western Polynesian kindreds were homozygous for this variant [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/).

**Consanguinity:** Contributes to homozygosity in some families (as typical for AR IEIs), and to the appearance of private homozygous deletions/CNVs.

**Sex ratio:** No sex predilection (autosomal).

> *"All the patients are homozygous for the same nonsense IFNAR1 variant (p.Glu386\*)... this IFNAR1 variant has a minor allele frequency >1% in Samoa."* — [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/)

---

## 10. Diagnostics

**Diagnostic approach combines genetics + function:**

1. **Genetic testing:** Whole-exome (WES) or whole-genome (WGS) sequencing, or targeted **inborn errors of immunity (IEI) gene panels**, to identify biallelic *IFNAR1* LOF variants. **Copy-number/CNV analysis is essential** because large deletions and structural CNVs (e.g., the homozygous deletion and CNV Δ3-4-5) are recurrent mechanisms [PMID: 35091979](https://pubmed.ncbi.nlm.nih.gov/35091979/); [PMID: 42097348](https://pubmed.ncbi.nlm.nih.gov/42097348/).
2. **Functional confirmation:** Demonstrate **absent cellular responses to type I IFNs** (IFN-α2, IFN-β, IFN-ω) using fibroblast or whole-blood ISG-induction assays. A sensitive whole-blood assay (e.g., IP-10/CXCL10 readout) can detect both inborn errors and the autoantibody phenocopy [PMID: 39312669](https://pubmed.ncbi.nlm.nih.gov/39312669/).

**Differential diagnosis — critical:** The key acquired phenocopy is **neutralizing autoantibodies against type I IFNs**, present in ~10–15% of critical COVID-19 pneumonia cases; these must be excluded [PMID: 42524028](https://pubmed.ncbi.nlm.nih.gov/42524028/). Other differentials include IFNAR2, STAT1, STAT2, TYK2, IRF9 deficiencies and other IEIs of type I IFN immunity.

**Screening:** Not part of routine newborn screening; **cascade genetic screening** of relatives of affected individuals is recommended, particularly in high-prevalence Polynesian populations, prior to live vaccination.

> *"Human inborn errors of the type I IFN response pathway and auto-Abs neutralizing IFN-α, -β, and/or -ω can underlie severe viral illnesses. We report a simple assay for the detection of both types of condition."* — [PMID: 39312669](https://pubmed.ncbi.nlm.nih.gov/39312669/)

> *"Autoantibodies neutralizing type I interferon (AAN-I-IFN) have been found in at least 10-15% of critical COVID-19 pneumonia cases."* — [PMID: 42524028](https://pubmed.ncbi.nlm.nih.gov/42524028/)

---

## 11. Outcome / Prognosis

**Mortality:** Individual triggering episodes can be **fatal**. Documented fatalities include a child with concurrent critical COVID-19 pneumonia and MIS-C who died on day 56 [PMID: 35091979](https://pubmed.ncbi.nlm.nih.gov/35091979/), and two deceased siblings following yellow fever vaccination in a Brazilian family with a homozygous *IFNAR1* CNV [PMID: 42097348](https://pubmed.ncbi.nlm.nih.gov/42097348/).

**Between-episode outlook:** Generally good — patients are otherwise healthy with normal growth and development, and can survive to adulthood if triggers are avoided.

**Complications:** Encephalitis, viral pneumonia/ARDS, hepatitis, disseminated viral infection, and — in the COVID-19 setting — co-occurring MIS-C.

**Prognostic factors:** The nature of the trigger (fulminant vaccine-strain disease vs manageable wild-type infection), timeliness of recognition/supportive care, and avoidance of further live-vaccine exposure. With appropriate prevention (no live vaccines) and prompt management of infections, long-term prognosis can be favorable.

---

## 12. Treatment

**There is no approved disease-specific pharmacotherapy.** Critically, **exogenous type I IFN is ineffective** because the receptor is absent — this is a mechanistic dead-end for IFN-replacement strategies.

| Modality | Role in IFNAR1 deficiency | NCIT suggestion |
|---|---|---|
| Supportive/intensive care | Mainstay during viral episodes (organ support, ICU) | NCIT:C15320 (Supportive Care) |
| Antiviral therapy | Directed against the triggering virus where available | NCIT:C258 (Antiviral Agent) |
| Hematopoietic stem cell transplantation (HSCT) | Rational **curative** option in severe cases (restores IFNAR1-competent immune cells) | NCIT:C15431 (Hematopoietic Stem Cell Transplantation) |
| Exogenous type I IFN | **Not applicable** — receptor absent | — |

**Pharmacogenomics / advanced therapeutics:** No established gene therapy, RNA therapy, or targeted small-molecule therapy exists for this disease as of this report. HSCT is the only potentially curative intervention and is considered on a case-by-case basis in severe presentations.

**Treatment strategy:** Prevention-first (avoid live vaccines) + aggressive supportive/antiviral management of breakthrough viral illness + consideration of HSCT for severe/recurrent disease.

---

## 13. Prevention

Prevention is the cornerstone of management.

- **Primary prevention:** **Strict avoidance of live attenuated vaccines** (MMR, yellow fever, and other live vaccines) in affected individuals. Use inactivated/subunit alternatives where available and appropriate.
- **Secondary prevention:** **Cascade genetic screening** of at-risk relatives; and — importantly — **pre-vaccination screening** for type I IFN inborn errors and autoantibodies in relatives of individuals with adverse events following yellow fever vaccination [PMID: 42097348](https://pubmed.ncbi.nlm.nih.gov/42097348/).
- **Population-targeted consideration:** Inherited IFNAR1 deficiency should be **considered in individuals of Polynesian ancestry with severe viral illnesses**, and consideration given before live vaccination in that population [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/).
- **Genetic counseling:** AR inheritance with 25% sibling recurrence risk; counsel families accordingly, including reproductive options.
- **Tertiary prevention:** Prompt recognition and supportive/antiviral care to limit complications during viral episodes.

> *"Our findings advocate for precision vaccinology by screening relatives of AEFI-YF cases for type I IFN EIIs and auto-antibodies prior to live-attenuated vaccination."* — [PMID: 42097348](https://pubmed.ncbi.nlm.nih.gov/42097348/)

> *"Inherited IFNAR1 deficiency should be considered in individuals of Polynesian ancestry with severe viral illnesses."* — [PMID: 35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/)

---

## 14. Other Species / Natural Disease

- **Orthologous gene:** Mouse *Ifnar1* (NCBI Gene ID 15975); human *IFNAR1* (NCBI Gene ID 3454). The type I IFN receptor architecture and JAK-STAT signaling are **evolutionarily conserved** across vertebrates, including teleost fish [PMID: 35906001](https://pubmed.ncbi.nlm.nih.gov/35906001/).
- **Natural disease in other species:** No well-characterized naturally occurring **IFNAR1-deficiency disease** in companion animals or wildlife is established; the condition is defined in humans. Viral immune-evasion strategies that *degrade or block* IFNAR1 are, however, widespread across animal pathogens (e.g., African swine fever virus p22 promoting TAX1BP1-mediated IFNAR1 degradation [PMID: 40668839](https://pubmed.ncbi.nlm.nih.gov/40668839/); lumpy skin disease virus LSDV122 disrupting IFNAR1/IFNAR2 assembly [PMID: 41525414](https://pubmed.ncbi.nlm.nih.gov/41525414/)), underscoring the conserved centrality of this receptor to antiviral defense.
- **Evolutionary conservation of mechanism:** High — the requirement for type I IFN/JAK-STAT signaling in antiviral immunity is conserved, though with a **species difference in breadth**: mouse type I IFN is essential against a broad range of viruses, whereas human type I IFN shows greater redundancy [PMID: 33729549](https://pubmed.ncbi.nlm.nih.gov/33729549/).

---

## 15. Model Organisms

The principal model is the **Ifnar1-knockout (IFNAR1 KO) mouse** (mammalian, germline knockout), one of the most widely used tools in viral pathogenesis and vaccine research.

| Feature | IFNAR1 KO mouse | Human IFNAR1 deficiency |
|---|---|---|
| Type I IFN response | Abolished | Abolished |
| Viral susceptibility breadth | **Broad** — uniformly lethal to many viruses | **Narrow** — mainly live vaccines + select wild-type viruses |
| Utility | Pathogenesis + vaccine-efficacy studies | — |

**Phenotype recapitulation:** The KO faithfully reproduces the **loss of type I IFN signaling** and its consequence (viral susceptibility). It is used as a **uniformly lethal infection model** across diverse viruses — Nipah [PMID: 42623407](https://pubmed.ncbi.nlm.nih.gov/42623407/); [PMID: 42035922](https://pubmed.ncbi.nlm.nih.gov/42035922/), Akabane [PMID: 40209629](https://pubmed.ncbi.nlm.nih.gov/40209629/), Zika [PMID: 41754520](https://pubmed.ncbi.nlm.nih.gov/41754520/), dengue [PMID: 42149728](https://pubmed.ncbi.nlm.nih.gov/42149728/), Bourbon [PMID: 40910687](https://pubmed.ncbi.nlm.nih.gov/40910687/), and other bunyaviruses — and for vaccine-efficacy testing.

**Model limitation:** The KO **overstates the human phenotype**. Because human type I IFN is more redundant than mouse type I IFN, KO mice are broadly and lethally susceptible to viruses that cause little or no everyday illness in IFNAR1-deficient humans [PMID: 33729549](https://pubmed.ncbi.nlm.nih.gov/33729549/). Related multi-deficiency models (e.g., triple IFNAR/IFNGR/IFNLR "AGL" mice [PMID: 42463654](https://pubmed.ncbi.nlm.nih.gov/42463654/)) extend susceptibility further and reveal type III IFN as a backup layer.

> *"Mouse type I IFNs are essential for protection against a broad range of viruses in experimental conditions."* — [PMID: 33729549](https://pubmed.ncbi.nlm.nih.gov/33729549/)

**Resources:** MGI (*Ifnar1*), IMPC/IMSR for knockout lines; patient-derived fibroblasts and iPSCs for in vitro functional assays.

---

## Mechanistic Model / Interpretation

```
  IFNAR1 biallelic LOF (p.Glu386*, deletion, CNV)
                 │
                 ▼
  No functional IFNAR1 at cell surface
                 │
                 ▼
  IFN-α/β/ω cannot form IFNAR1+IFNAR2 ternary complex
                 │
                 ▼
  JAK1 / TYK2 not juxtaposed → no cross-phosphorylation
                 │
                 ▼
  STAT1 / STAT2 not phosphorylated → no ISGF3 (STAT1-STAT2-IRF9)
                 │
                 ▼
  No ISG induction → loss of cell-intrinsic antiviral state
                 │
        ┌────────┴─────────┐
        ▼                  ▼
  TRIGGER: live vaccine   TRIGGER: select wild-type
  (MMR, YF-17D)           virus (e.g., SARS-CoV-2)
        │                  │
        ▼                  ▼
  Uncontrolled viral replication in permissive cells
        │
        ▼
  Disseminated disease: encephalitis / pneumonitis /
  hepatitis / multiorgan; may be fatal
        │
        └─(inferred branch)─► aberrant innate/inflammasome
                              activation on viral trigger
```

The unifying interpretation is that IFNAR1 deficiency **removes a single, non-redundant node** (the obligate IFNAR1 chain) of the type I IFN receptor, collapsing the entire IFN-α/β/ω arm of antiviral immunity. In humans, this arm turns out to be **essential but narrow** — dispensable for containment of most everyday viruses (thanks to redundancy with type II/III IFN and other pathways), but indispensable for controlling attenuated-vaccine viruses and a limited set of wild-type viruses. This explains the paradox of an "otherwise healthy" patient who nonetheless suffers catastrophic vaccine or COVID-19 disease. The parallel with **IFNAR2 deficiency** (fatal encephalitis after MMR, yet no prior heightened respiratory-virus susceptibility [PMID: 26424569](https://pubmed.ncbi.nlm.nih.gov/26424569/)) confirms the pattern applies to the whole IFNAR receptor.

> *"Despite the severe outcome of systemic live vaccine challenge, the proband had previously shown no evidence of heightened susceptibility to respiratory viral pathogens... supports an essential but narrow role for IFN-α/β in human antiviral immunity."* — [PMID: 26424569](https://pubmed.ncbi.nlm.nih.gov/26424569/)

---

## Evidence Base

| PMID | Study | Contribution | Source type |
|---|---|---|---|
| [35442418](https://pubmed.ncbi.nlm.nih.gov/35442418/) | Bastard et al. 2022 | Defines AR IFNAR1 deficiency; Polynesian founder p.Glu386\* (MAF >1% Samoa); abolished IFN responses | Human clinical + functional |
| [31270247](https://pubmed.ncbi.nlm.nih.gov/31270247/) | Hernandez et al. 2019 | First description; MMR/YF live-vaccine adverse reactions in otherwise healthy patients | Human clinical |
| [42097348](https://pubmed.ncbi.nlm.nih.gov/42097348/) | Azamor et al. 2026 | Homozygous CNV Δ3-4-5; fatal YF vaccine AEs; advocates pre-vaccination screening | Human clinical + functional |
| [35091979](https://pubmed.ncbi.nlm.nih.gov/35091979/) | Abolhassani et al. 2022 | Homozygous LOF deletion; critical COVID-19 + MIS-C; fatal | Human clinical |
| [35708626](https://pubmed.ncbi.nlm.nih.gov/35708626/) | Zhang et al. 2022 | Recessive type I IFN IEIs in ~10.7% of pediatric COVID pneumonia; IFNAR1-deficient fibroblasts vulnerable to SARS-CoV-2 | Human clinical + in vitro |
| [38608537](https://pubmed.ncbi.nlm.nih.gov/38608537/) | de Weerd et al. 2024 | Structure–function of type I/III IFN receptor signaling (ternary complex, JAK/TYK/STAT) | Review / structural |
| [33729549](https://pubmed.ncbi.nlm.nih.gov/33729549/) | Meyts & Casanova 2021 | Human vs mouse type I IFN redundancy; explains narrow human phenotype | Review |
| [26424569](https://pubmed.ncbi.nlm.nih.gov/26424569/) | Duncan et al. 2015 | IFNAR2 deficiency; "essential but narrow" role; otherwise-healthy phenotype | Human clinical |
| [39312669](https://pubmed.ncbi.nlm.nih.gov/39312669/) | Gervais et al. 2024 | Whole-blood assay detecting both inborn errors and autoantibody phenocopies | Methods |
| [42524028](https://pubmed.ncbi.nlm.nih.gov/42524028/) | Kholaiq et al. 2026 | Anti–type I IFN autoantibodies in 10–15% of critical COVID-19 (acquired phenocopy) | Human clinical |

Consistency across independent kindreds and continents (Polynesia, Brazil, Iran, and pediatric COVID cohorts) reinforces the core disease definition. The mouse-model literature (Nipah, Akabane, Zika, dengue, Bourbon) both supports the mechanistic centrality of type I IFN and, by its broad lethality, **usefully contrasts** with the narrower human phenotype.

---

## Limitations and Knowledge Gaps

- **Ultra-rarity:** Total reported cases number in the low dozens; there are no formal prevalence/incidence estimates, no QoL instruments, and no natural-history cohorts. Epidemiology outside Polynesia is essentially unknown.
- **Variant spectrum incompletely mapped:** Beyond the founder nonsense allele and a few deletions/CNVs, the full mutational landscape (missense, splice, regulatory) and genotype–phenotype correlations are undefined.
- **Trigger–outcome uncertainty:** It is not fully resolved which wild-type viruses cause severe disease in IFNAR1-deficient humans versus which are contained by redundancy. The role of inflammasome/innate hyperactivation as a driver of immunopathology is inferred, not proven.
- **Therapeutics:** No disease-specific therapy or gene therapy exists; HSCT experience is anecdotal, with outcomes not systematically reported.
- **Modifiers:** No genetic/epigenetic modifiers of severity have been identified.
- **Model translation gap:** IFNAR1-KO mice overstate susceptibility, complicating direct translation of preclinical antiviral/vaccine findings.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for IFNAR1 (and broader type I IFN pathway) deficiency to capture prevalence, natural history, triggers, outcomes, and HSCT results.
2. **Population screening in Polynesia:** Systematic carrier screening for p.Glu386\* and integration into pre-vaccination protocols; quantify carrier frequency and true regional prevalence.
3. **Genotype–phenotype cataloging:** Curate all *IFNAR1* variants (with CNV detection) in ClinVar/IEI databases and correlate variant class with clinical severity and triggering virus.
4. **Standardized functional diagnostics:** Broaden validation and deployment of whole-blood ISG-induction assays (IP-10/CXCL10) that simultaneously flag inborn errors and neutralizing autoantibodies, enabling rapid differential diagnosis in severe viral illness.
5. **Prospective evaluation of HSCT** as curative therapy in severe cases; and preclinical exploration of *IFNAR1* gene-addition/editing in patient iPSC-derived immune cells.
6. **Precision vaccinology guidelines:** Formalize recommendations to withhold/replace live vaccines and to screen relatives of individuals with severe adverse events following live-attenuated (especially yellow fever) vaccination.
7. **Refine model systems:** Complement IFNAR1-KO mice with humanized or conditional models, and patient-derived organoids/iPSCs, to better recapitulate the narrow human antiviral phenotype for therapeutic testing.

---

*Report compiled from 9 confirmed findings across 5 investigation iterations, drawing on 38 reviewed papers. Evidence types are annotated as human clinical, model organism, in vitro, or review throughout.*


## Artifacts

- [OpenScientist final report](IFNAR1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](IFNAR1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030970` (2 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 106, susceptibility to viral infections**
- `HP:0002090` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Pneumonia**
- `HP:0002383` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Infectious encephalitis**
- `HP:0032251` (1 mention) - the report calls it "Abnormal susceptibility to viral infection"; HP calls it **Abnormal immune system morphology**
- `GO:0005886` (1 mention) - the report calls it "Subcellular level:** IFNAR1 is a **plasma membrane** receptor"; GO calls it **plasma membrane**
- `NCIT:C15320` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Study Design**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0060337` (2 mentions) - the report calls it "type I interferon signaling pathway"; GO calls it **type I interferon-mediated signaling pathway**, and lists "type I interferon signaling pathway" among its other names
- `NCIT:C258` (1 mention) - the report calls it "Antiviral Agent"; NCIT calls it **Antibiotic**, and lists "Antimicrobial Agent" among its other names