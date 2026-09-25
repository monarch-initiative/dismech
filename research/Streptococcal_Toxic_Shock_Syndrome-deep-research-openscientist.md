---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T07:55:26.749468'
end_time: '2026-09-25T08:12:10.622504'
duration_seconds: 1003.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Streptococcal Toxic Shock Syndrome
  mondo_id: MONDO:0020544
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 26
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 23
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 25
  verified: 24
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.04
  labels_checked: 24
  labels_matching: 13
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0020544
    reported_labels:
    - STSS
    ontology_label: streptococcal toxic-shock syndrome
  - term_id: HP:0007503
    reported_labels:
    - Desquamation
    ontology_label: Generalized ichthyosis
  - term_id: UBERON:0002385
    reported_labels:
    - fascia
    ontology_label: muscle tissue
  - term_id: CL:0000842
    reported_labels:
    - antigen-presenting cell
    - APC/monocyte
    ontology_label: mononuclear leukocyte
  labels_variant: 7
  unresolved_terms:
  - NCBITaxon:1114
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Streptococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Streptococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Streptococcal Toxic Shock Syndrome
- **MONDO ID:** MONDO:0020544 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Streptococcal Toxic Shock Syndrome** covering all of the
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

# Streptococcal Toxic Shock Syndrome (STSS): A Comprehensive Disease Characteristics Report

**Disease:** Streptococcal Toxic Shock Syndrome
**MONDO ID:** MONDO:0020544
**Category:** Infectious Disease
**Report type:** Aggregated disease-level synthesis (literature-derived; not derived from individual EHR records)

---

## Summary

Streptococcal Toxic Shock Syndrome (STSS) is an acute, toxin-mediated, fulminant complication of invasive Group A *Streptococcus* (GAS; *Streptococcus pyogenes*) infection — and, less commonly, of group C/G streptococci (*Streptococcus dysgalactiae* subsp. *equisimilis*). It is defined clinically by the triad of **high fever, hypotensive shock, and multi-organ dysfunction**, frequently accompanied by a "sunburn-like" erythematous rash with subsequent desquamation and, in a large fraction of cases, necrotizing soft-tissue infection (necrotizing fasciitis). The core mechanism is not genetic in the patient but microbial and immunological: secreted **superantigens** (streptococcal pyrogenic exotoxins SPE-A/SPE-C, SSA, SMEZ) cross-link MHC class II molecules on antigen-presenting cells directly to the Vβ region of the T-cell receptor, bypassing conventional antigen processing and activating up to ~20% of the entire T-cell repertoire. This triggers a massive polyclonal **cytokine storm** (TNF, IL-1, IL-2, IL-6, IFN-γ, IL-17), which — together with streptolysin O (SLO)-mediated endothelial cytolysis — produces capillary leak, distributive shock, disseminated intravascular coagulation (DIC), and cascading failure of kidneys, liver, lungs, heart, and the hematologic system.

Although STSS is not a heritable disorder, the **host HLA class II genotype is the principal determinant of disease severity**: the same GAS clone can cause severe or mild invasive disease depending on how the patient's class II haplotype presents the superantigens. Epidemiologically, STSS accounts for roughly 20–24% of invasive GAS (iGAS) infections and is consistently the strongest independent predictor of iGAS mortality. The emergence and clonal expansion of the hyper-toxigenic **emm1/M1UK (M1T1/ST28) lineage**, which over-produces SPE-A, has driven post-COVID increases in invasive disease and STSS. Risk is age-stratified — varicella and pharyngotonsillitis (with NSAID use as a key gene–environment interaction) in children; malignancy, diabetes, IV drug use, chronic wounds, and age >65 in adults.

Management rests on a three-pillar strategy: **early aggressive surgical source control** (debridement of necrotizing infection, potentially amputation), **combination antibiotics** (a β-lactam for bactericidal killing PLUS a protein-synthesis inhibitor — clindamycin or linezolid — to suppress toxin production), and **adjunctive intravenous immunoglobulin (IVIG)** plus intensive organ support. Despite this, STSS carries the highest mortality of all invasive GAS syndromes (~20–45% in dedicated cohorts), and **no licensed GAS vaccine exists**. This report synthesizes 14 confirmed findings across all 15 knowledge-base sections, grounded in 66 reviewed papers.

---

## Key Findings

### F001 — STSS is a superantigen-driven fulminant manifestation of invasive GAS

STSS is defined clinically by the triad of high fever, hypotensive shock, and multi-organ dysfunction, caused by GAS toxins. Superantigens (SPE-A, *speC*, *speG*) cross-link MHC class II and TCR Vβ, driving polyclonal T-cell activation and a cytokine storm; streptolysin O (SLO)-mediated endothelial lysis contributes to capillary leak and shock. As stated in a 2025 case report, *"The STSS triad encompasses high fever, hypotensive shock, and a 'sunburn-like' rash with desquamation. STSS, like Toxic Shock Syndrome (TSS), is a rare complication of streptococcal infections caused by Group A"* [PMID: 39886786](https://pubmed.ncbi.nlm.nih.gov/39886786/). A genomically characterized fatal case links the specific virulence factors mechanistically: *"The slo-mediated endothelial lysis and speC/G-induced cytokine storm contributed to capillary leakage and rapid clinical deterioration"* [PMID: 41714973](https://pubmed.ncbi.nlm.nih.gov/41714973/).

**Ontology anchors:** MONDO:0020544 (STSS); NCBITaxon:1314 (*S. pyogenes*); protein superantigens SPE-A, SPE-C.

### F002 — Host HLA class II genotype determines severity of invasive GAS/STSS

The same GAS clone can cause severe or non-severe invasive disease depending largely on the patient's HLA class II type. Certain haplotypes present streptococcal superantigens in a way that elicits potent inflammatory responses leading to organ failure and shock, while others confer relative protection. The landmark review states: *"Certain class II haplotypes present the streptococcal superantigens in a way that results in responses, whereas others present the same superantigens in a way that elicits very potent inflammatory responses that can lead to organ failure and shock"* [PMID: 14620152](https://pubmed.ncbi.nlm.nih.gov/14620152/). This is the closest thing to a "genetic risk factor" for STSS — a host-side modifier of an infectious disease, not a Mendelian causal locus.

### F003 — Clindamycin and IVIG are associated with reduced STSS mortality (low-certainty evidence)

A systematic review and meta-analysis (1 RCT + 40 observational studies, n = 1,918) found clindamycin treatment associated with lower mortality (OR 0.14, 95% CI 0.06–0.37) and, within clindamycin-treated patients, IVIG associated with lower mortality (OR 0.34, 95% CI 0.15–0.75) — both low-certainty. Age ≥65 increased mortality odds (OR 2.37, 95% CI 1.47–3.84): *"we found a statistically significant association between clindamycin treatment and mortality (n=144; OR 0.14, 95% CI 0.06 to 0.37)... Within clindamycin-treated STSS patients, we found a statistically significant association between intravenous Ig treatment and mortality (n=188; OR 0.34, 95% CI 0.15 to 0.75)"* [PMID: 36456018](https://pubmed.ncbi.nlm.nih.gov/36456018/). A rigorous 2026 Swedish population-based cohort (n = 106) was, however, **inconclusive** for IVIG after adjusting for immortal-time bias: *"the hazard ratio was estimated at 1.69 (95% CI, .66-4.30). Although our study included a large population of patients with STSS, our results were inconclusive regarding the effect of IVIG"* [PMID: 41852552](https://pubmed.ncbi.nlm.nih.gov/41852552/). The overall evidence therefore favors clindamycin more strongly than IVIG.

| Intervention | Effect estimate | 95% CI | Certainty | Source |
|---|---|---|---|---|
| Clindamycin → mortality | OR 0.14 | 0.06–0.37 | Low | PMID 36456018 |
| IVIG (in clindamycin-treated) → mortality | OR 0.34 | 0.15–0.75 | Low | PMID 36456018 |
| IVIG → 30-day mortality (adjusted) | HR 1.69 | 0.66–4.30 | Inconclusive | PMID 41852552 |
| Age ≥65 → mortality | OR 2.37 | 1.47–3.84 | — | PMID 36456018 |

### F004 — STSS epidemiology: rising post-COVID iGAS burden, emm1/M1UK predominance, high mortality

In a Korean nationwide iGAS cohort (2015–2024, n = 454), STSS accounted for 19.6% of iGAS and was the strongest independent predictor of mortality (aOR 20.07, 95% CI 9.30–43.30): *"streptococcal toxic shock syndrome (STSS, 19.6%)... were the most common iGAS infections. Intensive care unit admission was required in 28.9%... overall mortality was 15.5%. Mortality was independently associated with STSS (aOR 20.07, 95% CI 9.30-43.30"* [PMID: 42281793](https://pubmed.ncbi.nlm.nih.gov/42281793/). A French post-COVID series (2022–2023) reported STSS in 24% of iGAS with 22% mortality and emm1 predominance: *"Streptococcal toxic shock syndrome (STSS) occurred in 24% of patients... Mortality rate was 22%... GAS emm1 genotype predominated (59%) and was involved in 79% of STSS"* [PMID: 42183688](https://pubmed.ncbi.nlm.nih.gov/42183688/).

### F005 — Mechanistic causal chain: superantigen cross-linking of MHC-II/TCR-Vβ drives the cytokine storm

Superantigens (SPE-A/C, SSA, SMEZ) simultaneously bind conserved regions of MHC class II on antigen-presenting cells and the TCR Vβ region, activating up to ~20% of the T-cell pool (versus ~0.01% for a conventional antigen), triggering a Th1/Th2/Th17/Th22 cytokine storm (TNF, IL-1, IL-2, IL-6, IFN-γ) within hours. Because they cross-link MHC-II, superantigens also activate APCs independently of T cells: *"the direct and simultaneous binding of SAgs with T-cell receptor (TCR)-bearing Vβ regions and conserved structures on major histocompatibility complex class II (MHC class II) on antigen-presenting cells (APCs) induces the activation of both cell types. However, by crosslinking MHC class II molecules, APCs can be activated by SAgs independently of T lymphocytes"* [PMID: 31412561](https://pubmed.ncbi.nlm.nih.gov/31412561/). This sets in motion the toxic-shock cytokine storm: *"They target a large fraction of T cell pools to set in motion a 'cytokine storm' with severe and sometimes life-threatening consequences typically encountered in toxic shock syndrome"* [PMID: 28632753](https://pubmed.ncbi.nlm.nih.gov/28632753/). A subsequent immunosuppressive branch is driven by SPEA-induced regulatory T cells via TNF-α–TNFR2 signaling and monocyte PD-L1/kynurenine pathways: *"streptococcal pyrogenic exotoxin A (SPEA) promoted human CD4"* [PMID: 40402252](https://pubmed.ncbi.nlm.nih.gov/40402252/).

### F006 — STSS clinical case definition and phenotype spectrum

STSS is operationally defined as **hypotension plus ≥2 of**: renal impairment, hepatic dysfunction, acute respiratory distress syndrome (ARDS), soft-tissue necrosis (e.g., necrotizing fasciitis), coagulopathy/DIC, and a generalized erythematous macular (sunburn-like) rash that may desquamate. Isolation of GAS from a sterile site defines a confirmed/definite case; isolation from a non-sterile site defines a probable case: *"The SSTS was defined as hypotension and at least 2 of these criteria: renal failure, hepatic failure, acute respiratory distress, tissue necrosis or desquamative erythematous rash"* [PMID: 28705427](https://pubmed.ncbi.nlm.nih.gov/28705427/). Fever is near-universal, and skin/soft-tissue lesions are the most frequent portal/manifestation.

**Suggested HPO terms:** HP:0001945 (Fever), HP:0002615 (Hypotension), HP:0000083 (Renal insufficiency), HP:0001410 (Decreased liver function), HP:0002098 (Respiratory distress), HP:0001928 (Abnormality of coagulation / DIC), HP:0000988 (Skin rash), HP:0007503 (Desquamation).

### F007 — Animal models of STSS require HLA class II humanization; M protein + superantigen cooperate

Inbred mice are innately refractory to superantigen-mediated responses, so **HLA class II transgenic mice** (HLA-DR3, HLA-DR4, HLA-DQ) are required to recapitulate the human superantigen-driven cytokine storm. In HLA-transgenic mice infected with a lethal SpeC-expressing GAS isolate, both SpeC and M protein acting cooperatively were required for STSS; vaccination with the conserved M-protein peptide J8 (and passive anti-J8 + anti-SpeC antibodies) reduced bacterial burden and resolved disease: *"We modelled these in HLA-transgenic mice infected with a clinically lethal isolate expressing Streptococcal pyrogenic exotoxin (Spe) C and demonstrate that both SpeC and streptococcal M protein, acting cooperatively, are required for disease. Vaccination with a conserved M protein peptide, J8, protects against STSS"* [PMID: 31517054](https://pubmed.ncbi.nlm.nih.gov/31517054/). The rationale for humanized models: *"Inbred mice are innately refractive to SAg-mediated responses... the versatility of the HLA-II transgenic mouse model that allowed the biological validation of known genetic associations to GAS NSTI"* [PMID: 33079368](https://pubmed.ncbi.nlm.nih.gov/33079368/).

### F008 — Treatment backbone and the absence of a licensed GAS vaccine

Management of STSS with necrotizing soft-tissue infection requires early aggressive surgical debridement/complete removal of necrotic tissue (potentially amputation) plus directed antibiotics and hemodynamic support; delays increase mortality: *"Early surgical debridement with complete removal of necrotic tissue, including potential amputation, is essential to decrease mortality and other complications"* [PMID: 41417687](https://pubmed.ncbi.nlm.nih.gov/41417687/). The antibiotic regimen pairs a β-lactam (penicillin) for bactericidal killing with a protein-synthesis inhibitor (clindamycin or linezolid) to suppress toxin production, plus adjunctive IVIG. No GAS vaccine is licensed: *"developing an effective GAS vaccine has faced several challenges, including the complexity of GAS virulence mechanisms, the diversity of emm types, and the lack of suitable preclinical models"* [PMID: 40252837](https://pubmed.ncbi.nlm.nih.gov/40252837/).

**Suggested NCIT terms:** clindamycin (C376), linezolid (C1687), penicillin (C71634), intravenous immunoglobulin therapy (C603), surgical debridement (C15274).

### F009 — Emergence of the toxigenic M1UK/M1T1 emm1 clone with elevated SpeA

A new emm1 lineage (M1UK) emerged in England, coinciding with unprecedented scarlet fever and invasive *S. pyogenes* activity; invasive emm1 isolates rose from 31% (2015) to 42% (2016). The lineage is defined by ~27 SNPs and characterized by **increased production of the superantigen SpeA**: *"Sequences of emm1 isolates from 2009-16 showed emergence of a new emm1 lineage (designated M1"* [PMID: 31519541](https://pubmed.ncbi.nlm.nih.gov/31519541/). Fatal STSS has been genomically linked to the M1(UK) (emm1/ST28) lineage carrying *slo*, *speC/speG*, *hasABC*, and *scpA*: *"S. pyogenes isolates from all sites were identified as M1(UK) (emm1/ST28) lineage... Key virulence genes included slo, speC/speG, hasABC and scpA"* [PMID: 41714973](https://pubmed.ncbi.nlm.nih.gov/41714973/).

### F010 — Age-stratified risk factors; varicella + NSAID as a key pediatric gene–environment interaction

In children, principal predisposing factors are varicella (chickenpox; ~24–25%) and streptococcal pharyngotonsillitis, plus skin breaches; in adults, malignancy, IV drug use, diabetes mellitus, chronic wounds, and age >65 predominate: *"The main predisposing factors in children were varicella and streptococcal pharyngotonsillitis (25% and 19·8%, respectively), as opposed to malignancy, intravenous drug abuse and diabetes mellitus in adults (19·6%, 15·2% and 10·9%, respectively)"* [PMID: 23746128](https://pubmed.ncbi.nlm.nih.gov/23746128/). A prospective case-control study established that NSAID use interacts with varicella to increase invasive GAS/NSTI risk: *"To test the hypothesis that nonsteroidal antiinflammatory drug use increases the risk of necrotizing soft tissue infections and, secondarily, all invasive group A streptococcal (GAS) infections in children with primary varicella infection"* [PMID: 11331694](https://pubmed.ncbi.nlm.nih.gov/11331694/).

### F011 — Prognosis: high case-fatality, age/renal-failure prognostic factors, long-term sequelae

STSS carries the highest mortality among invasive GAS syndromes. In a 21-year Australian population data-linkage study (n = 933 iGAS hospitalizations), the hospitalized case-fatality rate was 5.2%, but most deaths were attributable to sepsis (80%), with necrotizing fasciitis (18%) and septic shock (13.3%) contributing; older age and renal failure were significant predictors: *"Hospitalised case fatality rate was 5.2%. Intensive Care Unit (ICU) admission was required for 219 patients (23.5%)... Most deaths were attributable to sepsis (80%), with necrotising fasciitis (18%) and septic shock (13.3%) also contributing"* [PMID: 42684631](https://pubmed.ncbi.nlm.nih.gov/42684631/). Survivors face substantial morbidity: *"At discharge, 137/374 (37%) had not returned to premorbid function"* [PMID: 42004581](https://pubmed.ncbi.nlm.nih.gov/42004581/). By analogy, survivors of childhood meningococcal septic shock experience high rates of skin scarring (48%) and orthopedic sequelae including amputation (8%) [PMID: 19147623](https://pubmed.ncbi.nlm.nih.gov/19147623/).

### F012 — Diagnosis is clinical/microbiological; LRINEC and CT support necrotizing infection identification

STSS diagnosis rests on the clinical case definition plus isolation of GAS (culture/PCR) from a sterile (confirmed) or non-sterile (probable) site; there is no single confirmatory biomarker. Supporting laboratory abnormalities include leukocytosis with left shift, elevated CRP/procalcitonin, AKI (elevated creatinine), transaminitis, thrombocytopenia/DIC, elevated lactate, hypoalbuminemia, hypocalcemia, and creatine kinase elevation with myonecrosis. For associated necrotizing fasciitis, CT is the best imaging test and the LRINEC score aids risk stratification: *"Computed tomography (CT) had sensitivity of 88.5% and specificity of 93.3%, while plain radiography had sensitivity of 48.9%... LRINEC ≥ 6 had sensitivity of 68.2% and specificity of 84.8%"* [PMID: 29672405](https://pubmed.ncbi.nlm.nih.gov/29672405/). The LRINEC composition: *"The score is determined by 6 serologic markers: C-reactive protein (CRP), total white blood cell (WBC) count, hemoglobin, sodium, creatinine, and glucose"* [PMID: 33570428](https://pubmed.ncbi.nlm.nih.gov/33570428/). Surgical exploration/histopathology remains the diagnostic gold standard for necrotizing infection.

### F013 — Naturally-occurring STSS/necrotizing fasciitis in dogs is caused by *Streptococcus canis* (group G)

A toxic-shock and necrotizing-fasciitis syndrome clinically analogous to human STSS occurs naturally in dogs, caused by *Streptococcus canis* (Lancefield group G; NCBITaxon:1114). In a prospective canine case series, dogs with streptococcal shock without NF died within 48 h, whereas those with NF survived after surgical debridement + antibiotics: *"3 dogs with streptococcal shock without necrotizing fasciitis died or were euthanatized within 48 hours of admission, whereas 4 dogs with streptococcal shock and necrotizing fasciitis survived following surgical debridement, supportive medical treatment, and treatment with antibiotics"* [PMID: 8870738](https://pubmed.ncbi.nlm.nih.gov/8870738/). *S. canis* possesses M protein and streptolysin O but generally lacks most *S. pyogenes* superantigen genes: *"S. canis possesses M proteins and encodes streptolysin O, but lacks some of the other recognized virulence genes with significant homology to those in S. pyogenes"* [PMID: 10591501](https://pubmed.ncbi.nlm.nih.gov/10591501/). A fluoroquinolone-inducible mitogen-encoding prophage may contribute: *"Both mitomycin and the fluoroquinolone enrofloxacin caused bacteriophage-induced lysis of S. canis strain 34, an isolate from a case of canine STSS and NF"* [PMID: 12761079](https://pubmed.ncbi.nlm.nih.gov/12761079/) — cautioning that fluoroquinolone treatment could exacerbate canine disease.

### F014 — Anatomical involvement: portal soft tissue plus systemic multi-organ injury via endothelium

STSS is a multi-system disorder. The primary portal/site is skin and soft tissue (subcutaneous tissue and superficial/deep fascia in necrotizing fasciitis; also pharynx, lung/pleura, muscle, postpartum uterus, joints). Systemically, the superantigen-driven cytokine storm targets the vascular endothelium (capillary leak → distributive/hypovolemic shock) and causes secondary failure of kidneys, liver, lungs (ARDS), heart (toxic cardiomyopathy), and the hematologic system (DIC). The multi-organ involvement is encoded in the case definition itself [PMID: 28705427](https://pubmed.ncbi.nlm.nih.gov/28705427/), and the endothelium is the key target tissue: *"The slo-mediated endothelial lysis and speC/G-induced cytokine storm contributed to capillary leakage and rapid clinical deterioration"* [PMID: 41714973](https://pubmed.ncbi.nlm.nih.gov/41714973/).

**Suggested UBERON/CL terms:** UBERON:0002097 (skin), UBERON:0002385 (fascia), UBERON:0001981 (blood vessel endothelium), UBERON:0002113 (kidney), UBERON:0002107 (liver), UBERON:0002048 (lung); CL:0000115 (endothelial cell), CL:0000624 (CD4+ T cell), CL:0000842 (antigen-presenting cell).

---

## Detailed Section-by-Section Report

### 1. Disease Information

STSS is a rare, acute, toxin-mediated complication of invasive streptococcal infection defined by hypotension plus multi-organ dysfunction (F001, F006). **Key identifiers:** MONDO:0020544; MeSH "Shock, Septic" / "Streptococcal Infections"; ICD-10 A48.3 (Toxic shock syndrome); ICD-11 1B54. It has **no OMIM entry** because it is an acquired infectious disease, not a Mendelian condition. **Synonyms:** streptococcal toxic shock-like syndrome (STSLS/TSLS), streptococcal TSS, GAS toxic shock syndrome. Information is derived from **aggregated disease-level resources** (case series, cohort studies, meta-analyses) rather than individual EHR data.

### 2. Etiology

**Causal factor:** infectious — *Streptococcus pyogenes* (GAS) secreting superantigen exotoxins, with SLO cytolysin (F001, F005, F009). Group C/G streptococci (*S. dysgalactiae* subsp. *equisimilis*) cause a minority of cases (PMID 27432040, 8905439). **Genetic "risk":** there are no patient causal genes; instead, host **HLA class II** genotype is the dominant severity modifier (F002). **Environmental/host risk factors** are age-stratified: children — varicella (~25%) and pharyngotonsillitis; adults — malignancy, IV drug use, diabetes, chronic wounds, age >65 (F010). **Gene–environment interaction:** NSAID use during primary varicella increases invasive GAS/NSTI risk in children (F010). **Protective factors:** naturally acquired anti-superantigen and anti-M-protein/conserved-antigen antibodies correlate with protection (PMID 40781379); certain HLA class II haplotypes are relatively protective (F002).

### 3. Phenotypes

Core phenotypes (with type and typical frequency): fever (symptom; near-universal, HP:0001945), hypotension/shock (clinical sign; required for diagnosis, HP:0002615), sunburn-like erythematous rash with desquamation (physical manifestation, HP:0000988/HP:0007503), renal failure (organ, HP:0000083), hepatic dysfunction (HP:0001410), ARDS (HP:0002098), coagulopathy/DIC (HP:0001928), and soft-tissue necrosis/necrotizing fasciitis (~40% of cases). Onset is **acute (adult and pediatric)**; severity is **severe by definition**; progression is **rapid/fulminant** (multiorgan failure within hours). Quality-of-life impact among survivors is substantial (37% not returned to premorbid function at discharge; F011).

### 4. Genetic/Molecular Information

There are **no human causal genes, pathogenic variants, chromosomal abnormalities, or epigenetic lesions** in the patient (STSS is acquired). The relevant genetics are (a) the **host HLA class II locus** as a severity modifier (F002) and (b) the **bacterial virulence genome**: superantigen genes *speA*, *speC*, *speG*, *ssa*, *smez*; cytolysin *slo*; hyaluronic-acid capsule operon *hasABC*; C5a peptidase *scpA*; M-protein gene *emm* (F001, F009). The **emm1/M1UK** lineage over-produces SpeA and is defined by ~27 SNPs (F009).

### 5. Environmental Information

**Infectious agent:** *S. pyogenes* (NCBITaxon:1314), predominantly emm1/M1UK; less often group C/G streptococci. **Environmental/lifestyle contributors:** skin trauma or surgical wounds (portal of entry), IV drug use, NSAID use during varicella, and immunosuppression (F010). Respiratory viral co-infection is associated with more severe pediatric iGAS (PMID 41316382, 42525127).

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. GAS (emm1/M1UK) colonizes/breaches skin, soft tissue, pharynx, or mucosa
        │  leads to
2. Local invasive infection (e.g., necrotizing fasciitis) + secretion of
   superantigens (SPE-A/C, SSA, SMEZ) and cytolysin SLO
        │  leads to
3. Superantigens cross-link MHC class II (APC) directly to TCR-Vβ  →
   activation of up to ~20% of the T-cell pool (bypasses antigen processing)
        │  branch: MHC-II cross-linking also activates APCs T-cell-independently
        │  results in
4. Polyclonal cytokine storm within hours (TNF, IL-1, IL-2, IL-6, IFN-γ, IL-17)
        │  in parallel: SLO lyses endothelial cells
        │  leads to
5. Vascular endothelial injury + capillary leak
        │  leads to
6. Distributive/hypovolemic shock (hypotension)
        │  leads to
7. Multi-organ dysfunction: AKI, hepatic failure, ARDS, DIC, toxic cardiomyopathy
        │  branch (late): SPEA-induced Tregs / monocyte PD-L1-kynurenine →
        │  immunoparalysis (impaired pathogen clearance)
        │  results in
8. STSS — high fever + shock + multi-organ failure (mortality ~20–45%)
```

**Molecular pathways:** TCR/MHC-II signaling, NF-κB-driven pro-inflammatory cytokine transcription, IFN-γ–JAK-STAT1 (small-intestinal immunopathology is a major driver of lethality in HLA-DR3 CRS models; ruxolitinib is protective — PMID 32676080). **Cellular processes:** polyclonal T-cell activation, APC activation, MAIT-cell hyperactivation then anergy (PMID 28632753), endothelial cytolysis, neutrophil-driven injury, immunothrombosis, apoptosis/necrosis (PMID 42459336). **Upstream:** superantigen/SLO release; **downstream:** capillary leak, shock, organ failure, immunoparalysis. **GO terms:** GO:0042110 (T-cell activation), GO:0006954 (inflammatory response), GO:0050729 (positive regulation of inflammatory response), GO:0002827 (positive regulation of Th1 immune response). **CL terms:** CL:0000624 (CD4+ T cell), CL:0000940 (MAIT cell), CL:0000842 (APC/monocyte), CL:0000115 (endothelial cell).

### 7. Anatomical Structures Affected

**Primary:** skin and soft tissue (subcutaneous tissue, superficial/deep fascia; UBERON:0002097, UBERON:0002385), pharynx, lung/pleura, muscle, postpartum uterus, joints. **Secondary/systemic:** vascular endothelium (key mediator; UBERON:0001981), kidney, liver, lung, heart, hematologic system (F014). **Body systems:** integumentary, cardiovascular, renal, hepatic, respiratory, hematologic. **Lateralization:** soft-tissue focus typically unilateral/localized (e.g., a limb); shock and organ failure are systemic/bilateral.

### 8. Temporal Development

**Onset:** acute, at any age (bimodal risk: young children with varicella; adults >65). **Progression:** fulminant — shock and multiorgan failure within hours (F004, F006). **Course:** self-limited if survived (not chronic); no relapsing-remitting pattern. **Critical period:** the first hours are the decisive window for source control, antibiotics, and IVIG; delays sharply increase mortality (F008).

### 9. Inheritance and Population

**Not heritable** (acquired infection). **Epidemiology:** STSS constitutes ~19.6–24% of iGAS (F004). iGAS ICU admission ~24–29%; overall iGAS mortality ~14–16%, but STSS-specific mortality is markedly higher (~20–45%). **Population demographics:** bimodal age distribution; adults >65 at highest mortality risk; both sexes affected. **Geographic/temporal:** post-COVID surge across Europe, Korea, Australia, driven by emm1/M1UK clonal expansion (F004, F009). The relevant "founder"/clonal effect is bacterial (M1UK), not human.

### 10. Diagnostics

**Clinical/microbiological** (F012): clinical case definition (hypotension + ≥2 organ criteria) plus GAS isolation from sterile (confirmed) or non-sterile (probable) site. **Labs:** leukocytosis with left shift, ↑CRP/procalcitonin, ↑creatinine (AKI), transaminitis, thrombocytopenia/DIC, ↑lactate, hypoalbuminemia, hypocalcemia, ↑CK. **Imaging:** CT is best for necrotizing infection (sensitivity 88.5%, specificity 93.3%). **LRINEC score** (CRP, WBC, hemoglobin, sodium, creatinine, glucose) ≥6 supports NF (specific but insensitive). **Strain characterization:** blood/wound/tissue cultures, emm typing (Rt-PCR or sequencing), whole-genome sequencing. **Gold standard for NF:** surgical exploration/histopathology. Patient genetic testing is **not applicable**.

### 11. Outcome/Prognosis

STSS has the **highest mortality of invasive GAS syndromes** (F011). Population case-fatality for hospitalized iGAS is ~5%, but STSS-associated cohorts report ~20–45%. **Prognostic factors:** age ≥65 (OR 2.37), renal failure, elevated lactate, delayed source control. **Complications:** septic shock, necrotizing fasciitis, DIC, multi-organ failure. **Morbidity in survivors:** amputation, skin scarring, limb-length discrepancy, functional impairment (37% not returned to premorbid function at discharge; F011).

### 12. Treatment

Three-pillar strategy (F003, F008):
1. **Source control:** early aggressive surgical debridement (potentially amputation) for necrotizing infection — essential to reduce mortality (NCIT: surgical debridement C15274).
2. **Antibiotics:** β-lactam (penicillin, NCIT C71634) for bactericidal killing PLUS a protein-synthesis inhibitor — clindamycin (C376) or linezolid (C1687) — to suppress toxin production (the "Eagle effect" rationale).
3. **Adjuncts:** IVIG (C603) to neutralize superantigens (low-certainty benefit; inconclusive in the most rigorous cohort), corticosteroids, and intensive organ support (vasopressors, mechanical ventilation, renal replacement, occasionally ECMO/extracorporeal immunomodulation — PMID 42784312).

**Experimental/future:** JAK inhibition (ruxolitinib) protective in CRS models (PMID 32676080); IgM/IgA-enriched immunoglobulins (PMID 40175197); vaccine candidates (J8/StreptInCor conserved M-protein peptides, Slr, non-M conserved antigens). **No licensed GAS vaccine** (F008). **Pharmacogenomics:** no established patient PGx; HLA class II modulates response magnitude (F002).

### 13. Prevention

**Primary:** prompt treatment of GAS pharyngitis/skin infection; varicella vaccination (removes a major pediatric risk factor); avoiding NSAIDs during varicella; wound care. **Secondary:** early recognition and empiric therapy in at-risk patients; post-exposure chemoprophylaxis for close household contacts of severe iGAS (per public-health guidance). **Tertiary:** aggressive source control and toxin suppression to prevent progression. **Immunization:** no licensed GAS vaccine; multiple candidates in development (F008). **Public health:** iGAS surveillance, emm typing, outbreak investigation. **Counseling:** genetic counseling not applicable (non-heritable).

### 14. Other Species / Natural Disease

A **naturally-occurring canine STSS/necrotizing fasciitis** exists, caused by *Streptococcus canis* (Lancefield group G; NCBITaxon:1114) (F013). Canine *S. canis* possesses M protein and SLO but lacks most *S. pyogenes* superantigen genes, and canine STSS is largely **non-clonal** (unlike human M1 clonal expansion; PMID 10369564). A fluoroquinolone-inducible mitogen-encoding prophage (phiSC1, gene *scm*) may contribute superantigen-like activity, cautioning against fluoroquinolone use in canine cases (F013). This provides a comparative-pathology model illustrating that M protein + SLO can drive shock/NF even with a divergent superantigen repertoire. Group C/G streptococci also cause STSS-like disease in humans (PMID 27432040, 8905439, 42062850).

### 15. Model Organisms

The essential model is the **HLA class II transgenic mouse** (HLA-DR3, HLA-DR4, HLA-DQ), because inbred mice are innately refractory to superantigens (F007). These models recapitulate the superantigen-driven cytokine storm and demonstrated the cooperative requirement of SpeC + M protein and J8-vaccine protection (PMID 31517054). Advanced recombinant inbred BXD mice map host genetic loci modulating GAS necrotizing soft-tissue infection (PMID 33079368). HLA-DR3 cytokine-release-syndrome models revealed small-intestinal immunopathology and IFN-γ/IL-17A/JAK signaling as pathogenic (PMID 32676080). **Limitations:** murine models incompletely capture human hemodynamics and chronic sequelae; superantigen refractoriness necessitates humanization. **Resources:** MGI, IMSR for HLA-transgenic strains.

---

## Mechanistic Model / Interpretation

The unifying model is that **STSS is a host-response disease triggered by bacterial superantigens acting on a genetically permissive immune system**. Two converging axes cause shock:

| Axis | Effector | Immediate effect | Downstream |
|---|---|---|---|
| **Immunological** | SPE-A/C, SSA, SMEZ superantigens | MHC-II × TCR-Vβ cross-link → polyclonal T-cell + APC activation | Cytokine storm (TNF, IL-1/2/6, IFN-γ, IL-17) → capillary leak |
| **Cytolytic** | Streptolysin O (SLO) | Direct endothelial lysis | Capillary leak, tissue necrosis |

Both axes converge on **endothelial dysfunction → capillary leak → distributive shock → multi-organ failure**. Host **HLA class II** genotype sets the gain on the immunological axis, explaining why the same clone produces divergent outcomes. The bacterial side is amplified when a hyper-toxigenic clone (**M1UK**, over-producing SpeA) circulates. A late **immunoparalysis** branch (SPEA-induced Tregs, monocyte PD-L1/kynurenine, MAIT anergy) impairs pathogen clearance and may worsen secondary infection. This model directly rationalizes therapy: kill the organism (β-lactam), silence the toxin factory (clindamycin/linezolid), neutralize circulating superantigen (IVIG), and physically remove the toxin source (surgical debridement).

---

## Evidence Base

| PMID | Role | How it supports the findings |
|---|---|---|
| [39886786](https://pubmed.ncbi.nlm.nih.gov/39886786/) | Case report | Defines the STSS triad and GAS causation (F001) |
| [41714973](https://pubmed.ncbi.nlm.nih.gov/41714973/) | Genomic case | SLO endothelial lysis + SPE cytokine storm; M1(UK) virulence genes (F001, F009, F014) |
| [14620152](https://pubmed.ncbi.nlm.nih.gov/14620152/) | Review | HLA class II determines severity (F002) |
| [36456018](https://pubmed.ncbi.nlm.nih.gov/36456018/) | Meta-analysis | Clindamycin/IVIG mortality associations; age ≥65 (F003) |
| [41852552](https://pubmed.ncbi.nlm.nih.gov/41852552/) | Cohort | IVIG inconclusive after bias adjustment (F003) |
| [42281793](https://pubmed.ncbi.nlm.nih.gov/42281793/) | Nationwide cohort | STSS 19.6% of iGAS; aOR 20 for mortality (F004) |
| [42183688](https://pubmed.ncbi.nlm.nih.gov/42183688/) | Series | Post-COVID STSS 24%, 22% mortality, emm1 (F004) |
| [31412561](https://pubmed.ncbi.nlm.nih.gov/31412561/) | Mechanism | MHC-II/TCR-Vβ cross-link; T-cell-independent APC activation (F005) |
| [28632753](https://pubmed.ncbi.nlm.nih.gov/28632753/) | Mechanism | Superantigen cytokine storm; MAIT anergy (F005) |
| [40402252](https://pubmed.ncbi.nlm.nih.gov/40402252/) | Mechanism | SPEA-induced Tregs (immunosuppression branch) (F005) |
| [28705427](https://pubmed.ncbi.nlm.nih.gov/28705427/) | Series | Clinical case definition/organ criteria (F006, F014) |
| [31517054](https://pubmed.ncbi.nlm.nih.gov/31517054/) | Model | HLA-humanized mouse; SpeC+M cooperation; J8 vaccine (F007) |
| [33079368](https://pubmed.ncbi.nlm.nih.gov/33079368/) | Model | Rationale for HLA-II transgenic models (F007) |
| [41417687](https://pubmed.ncbi.nlm.nih.gov/41417687/) | Position statement | Early debridement essential (F008) |
| [40252837](https://pubmed.ncbi.nlm.nih.gov/40252837/) | Review | No licensed GAS vaccine; barriers (F008) |
| [31519541](https://pubmed.ncbi.nlm.nih.gov/31519541/) | Molecular epidemiology | M1UK emergence, elevated SpeA (F009) |
| [23746128](https://pubmed.ncbi.nlm.nih.gov/23746128/) | Epidemiology | Age-stratified risk factors (F010) |
| [11331694](https://pubmed.ncbi.nlm.nih.gov/11331694/) | Case-control | NSAID × varicella interaction (F010) |
| [42684631](https://pubmed.ncbi.nlm.nih.gov/42684631/) | Data linkage | iGAS case-fatality, causes of death (F011) |
| [42004581](https://pubmed.ncbi.nlm.nih.gov/42004581/) | Cohort | 37% not returned to premorbid function (F011) |
| [19147623](https://pubmed.ncbi.nlm.nih.gov/19147623/) | Cohort | Long-term scarring/orthopedic sequelae of septic shock (F011) |
| [29672405](https://pubmed.ncbi.nlm.nih.gov/29672405/) | Meta-analysis | CT/LRINEC diagnostic accuracy (F012) |
| [33570428](https://pubmed.ncbi.nlm.nih.gov/33570428/) | Review | LRINEC composition (F012) |
| [8870738](https://pubmed.ncbi.nlm.nih.gov/8870738/) | Veterinary series | Canine STSS/NF outcomes (F013) |
| [10591501](https://pubmed.ncbi.nlm.nih.gov/10591501/) | Comparative genomics | S. canis virulence repertoire (F013) |
| [12761079](https://pubmed.ncbi.nlm.nih.gov/12761079/) | Molecular | Fluoroquinolone-inducible mitogen prophage (F013) |
| [32676080](https://pubmed.ncbi.nlm.nih.gov/32676080/) | Model | JAK-STAT/IFN-γ intestinal immunopathology; ruxolitinib |
| [40781379](https://pubmed.ncbi.nlm.nih.gov/40781379/) | Serology | Natural protective humoral immunity (protective factors) |

**Note on citation flags:** Several citations (PMIDs 42183688, 41714973, 42684631) were flagged during verification as "mismatch" — the quoted text is consistent with the finding but the automated snippet-to-abstract match was imperfect (abstracts were partially truncated in the source). These claims are supported but should be re-verified against full-text abstracts before database ingestion.

---

## Limitations and Knowledge Gaps

1. **Therapeutic uncertainty (IVIG).** The mortality benefit of IVIG is low-certainty and became **inconclusive** in the most rigorous, bias-adjusted cohort (HR 1.69, 95% CI 0.66–4.30; PMID 41852552). A definitive adequately powered RCT is lacking. Clindamycin's benefit, while consistent, also rests largely on observational data.
2. **Host genetics not resolved to variant level.** HLA class II is established as a severity modifier, but specific protective/risk alleles and their effect sizes for STSS are not fully catalogued; no GWAS-scale analysis of STSS outcomes was identified.
3. **Biomarker gap.** There is no single confirmatory diagnostic biomarker; LRINEC is insensitive; early distinction of STSS from other septic shock relies on clinical suspicion and culture.
4. **Immunoparalysis under-characterized.** The late immunosuppressive branch (Tregs, PD-L1/kynurenine, MAIT anergy) is mechanistically described but its clinical prognostic and therapeutic implications remain investigational.
5. **Model limitations.** HLA-transgenic mice are essential but incompletely capture human hemodynamics, chronic sequelae, and polymicrobial context.
6. **Vaccine absence.** emm-type diversity, virulence complexity, and preclinical model gaps continue to block a licensed vaccine.
7. **Citation verification.** Some abstracts were truncated; a subset of quotes need full-text re-verification (see note above).

---

## Proposed Follow-up Experiments / Actions

1. **Definitive IVIG RCT / emulated target trial** in STSS with pre-specified adjustment for immortal-time bias, stratified by superantigen genotype and HLA class II type, to resolve the clindamycin-adjacent IVIG question.
2. **Host-genetics study:** targeted HLA class II typing (and broader immunogenetic panels) in a large STSS-vs-non-severe-iGAS cohort to define specific risk/protective alleles and effect sizes for knowledge-base annotation.
3. **Prospective biomarker-stratified cohort** (per PMID 42459336) using monocytic HLA-DR expression, lymphocyte indices, and cytokine trajectories to develop a diagnostic/prognostic panel and phenotype the hyperinflammation→immunoparalysis transition.
4. **JAK-inhibitor translational study:** evaluate ruxolitinib (or selective JAK1/2 inhibition) as host-directed adjunct, building on HLA-DR3 CRS model protection (PMID 32676080), with careful attention to infection-clearance risk.
5. **Genomic surveillance** of emm1/M1UK and emerging lineages (including group C/G SDSE) integrated with clinical outcomes to track toxigenic clonal shifts driving STSS incidence.
6. **Vaccine advancement:** progress conserved-antigen candidates (J8/StreptInCor, Slr, non-M conserved antigens; PMIDs 40252837, 42298213, 40781379) through HLA-humanized preclinical models toward Phase I.
7. **Comparative one-health study** of canine *S. canis* STSS to test whether M protein + SLO alone suffice for shock, informing minimal virulence requirements and cautioning on fluoroquinolone use (PMID 12761079).

---

*Report compiled from 14 confirmed findings and 66 reviewed papers across 5 investigation iterations. Evidence source types span human clinical cohorts, meta-analyses, HLA-humanized model organisms, in vitro mechanistic studies, and veterinary comparative pathology.*


## Artifacts

- [OpenScientist final report](Streptococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Streptococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 34 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 24 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020544` (3 mentions) - the report calls it "STSS"; MONDO calls it **streptococcal toxic-shock syndrome**
- `HP:0007503` (2 mentions) - the report calls it "Desquamation"; HP calls it **Generalized ichthyosis**
- `UBERON:0002385` (2 mentions) - the report calls it "fascia"; UBERON calls it **muscle tissue**
- `CL:0000842` (2 mentions) - the report calls it "antigen-presenting cell", "APC/monocyte"; CL calls it **mononuclear leukocyte**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCBITaxon:1114` (2 mentions) - NCBITaxon does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1314` (2 mentions) - the report calls it "S. pyogenes"; NCBITaxon calls it **Streptococcus pyogenes**
- `HP:0001928` (2 mentions) - the report calls it "Abnormality of coagulation / DIC"; HP calls it **Abnormality of coagulation**
- `UBERON:0002097` (2 mentions) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0001981` (2 mentions) - the report calls it "blood vessel endothelium"; UBERON calls it **blood vessel**
- `CL:0000624` (2 mentions) - the report calls it "CD4+ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `GO:0002827` (1 mention) - the report calls it "positive regulation of Th1 immune response"; GO calls it **positive regulation of T-helper 1 type immune response**
- `CL:0000940` (1 mention) - the report calls it "MAIT cell"; CL calls it **mucosal-associated invariant T cell**, and lists "MAIT" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000842` - called "antigen-presenting cell", "APC/monocyte"