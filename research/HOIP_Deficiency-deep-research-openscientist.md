---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T20:37:56.272944'
end_time: '2026-09-29T21:09:04.351089'
duration_seconds: 1868.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: HOIP Deficiency
  mondo_id: MONDO:0957981
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
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 11
  relevance_assessed: 15
  on_topic: 10
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 41
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 13
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0957981
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 115 with autoinflammation
  - term_id: NCIT:C2551
    reported_labels:
    - Interleukin-1 Receptor Antagonist
    ontology_label: CP-609,754
  - term_id: NCIT:C29799
    reported_labels:
    - IVIG
    ontology_label: 3-Nitrobenzo[a]pyrene trans-7,8-Dihydrodiol
  labels_variant: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: HOIP_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: HOIP_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HOIP Deficiency
- **MONDO ID:** MONDO:0957981 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **HOIP Deficiency** covering all of the
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

# HOIP Deficiency (Immunodeficiency-115 with Autoinflammation): A Comprehensive Disease Characteristics Report

**Target disease:** HOIP Deficiency · **MONDO:** MONDO:0957981 · **Gene:** *RNF31* (HOIP) · **Category:** Mendelian, autosomal recessive inborn error of immunity

---

## Summary

**HOIP deficiency** is an ultra-rare, autosomal-recessive inborn error of immunity caused by biallelic loss-of-function or severely hypomorphic mutations in **RNF31**, the gene encoding **HOIP** (HOIL-1-interacting protein), the catalytic RING-IBR-RING (RBR) E3 ubiquitin-ligase subunit of the **Linear Ubiquitin chain Assembly Complex (LUBAC)**. LUBAC (HOIP + HOIL-1/RBCK1 + SHARPIN) is the sole cellular machinery that builds Met1-linked ("linear") polyubiquitin chains. Because HOIP is the enzymatic engine of the complex, its loss collapses LUBAC and abolishes linear ubiquitination. This single molecular lesion produces a strikingly paradoxical, bifurcated clinical picture: **combined immunodeficiency** on one hand and **multiorgan autoinflammation** on the other, accompanied by **subclinical amylopectinosis** (polyglucosan storage) and **systemic/intestinal lymphangiectasia** (Boisson et al. 2015, [PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)).

The mechanistic unifying concept is that LUBAC acts as a **survival brake** and a **signaling amplifier**. Loss of linear ubiquitination simultaneously (A) impairs canonical NF-κB activation — producing immunodeficiency, defective germinal-center B-cell development, and impaired antiviral (TLR3) immunity — and (B) de-represses TNFR1-, TLR3-, and inflammasome-driven programmed cell death executed through RIPK1/RIPK3/MLKL (necroptosis), caspase-8 (apoptosis), and caspase-1 (pyroptosis). The resulting cell death (particularly of endothelium and epithelium) and the release of damage- and cytokine-driven inflammation constitute the autoinflammatory arm of disease. This model is directly supported by human cellular studies, biochemical reconstitution, and multiple mouse models in which removal of TNFR1 rescues embryonic lethality and inflammation.

Because TNF-superfamily signaling drives the lethal cell-death branch, **anti-TNF therapy** is the mechanism-aligned treatment; in a patient with the sister disorder SHARPIN deficiency (same LUBAC-deficiency group), anti-TNF produced complete clinical and transcriptomic resolution of autoinflammation (Oda et al. 2024, [PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)). However, no treatment is curative: hematopoietic stem cell transplantation could correct the hematopoietic immunodeficiency but would not restore LUBAC function in non-hematopoietic cells (endothelium, fibroblasts, muscle) that drive lymphangiectasia and amylopectinosis. The disease is exceedingly rare — only a handful of patients have been reported worldwide since 2015 — and prevention is limited to genetic counseling.

---

## 1. Disease Information

**Overview.** HOIP deficiency is a Mendelian, autosomal-recessive systemic disorder combining features of primary immunodeficiency and autoinflammation, first defined in humans in 2015. It is the "index" LUBAC-deficiency disorder involving the catalytic subunit of LUBAC. The cardinal presentation is **multiorgan autoinflammation, combined immunodeficiency, subclinical amylopectinosis, and systemic lymphangiectasia** (Boisson et al. 2015, [PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0957981 |
| Disease (OMIM phenotype) | Immunodeficiency-115 with autoinflammation (**IMD115**) |
| Gene symbol | **RNF31** (aliases: HOIP, IMD115, ZIBRA, Paul) |
| NCBI Gene ID | 55072 |
| HGNC | HGNC:16031 |
| Gene OMIM | 612487 |
| Ensembl | ENSG00000092098 |
| UniProt | Q96EP0 (RNF31_HUMAN, 1072 aa) |
| Cytogenetic locus | 14q12 |

(Identifier set from MyGene.info; see Finding F004.)

**Synonyms / alternative names.** HOIP deficiency; LUBAC deficiency (HOIP subtype); RNF31 deficiency; Immunodeficiency 115 with autoinflammation (IMD115). LUBAC deficiency as a category encompasses HOIP, HOIL-1/RBCK1, and SHARPIN deficiencies.

**Nature of information.** Evidence is derived from **individual patients** (a very small number of case reports and their in-depth cellular immunology) supplemented by mechanistic model-organism and in-vitro work — not from aggregated disease-level or EHR datasets, given the disorder's rarity.

---

## 2. Etiology

**Primary cause (genetic).** HOIP deficiency is caused by **biallelic (homozygous) loss-of-function or severely hypomorphic mutations in RNF31**. Two molecular classes are documented:

1. A **PUB-domain missense allele, L72P**, in the first reported patient — "at least severely hypomorphic, as it impairs HOIP expression and destabilizes the whole LUBAC complex," abolishing linear ubiquitination (Boisson et al. 2015, [PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)).
2. A **C-terminal frameshift null allele** generating a premature termination codon and "a C-terminal truncated HOIP mutant, that is, the loss of the linear ubiquitin chain-specific catalytic domain" (Wang et al. 2024, [PMID: 39009172](https://pubmed.ncbi.nlm.nih.gov/39009172/)).

**Genetic risk factors.** The disease is monogenic; the causal variants themselves are the risk factor. **Consanguinity / founder background** is the principal predisposing context, as all reported patients are homozygous. RNF31 is relatively loss-of-function-constrained in gnomAD, so biallelic disease is vanishingly rare.

**Environmental risk factors.** None established as causal. Infections (bacterial, viral) act as **triggers/complications** because of the immunodeficiency and can precipitate autoinflammatory flares, but are downstream of the genetic lesion.

**Protective factors.** None identified. No protective alleles or environmental protective factors are described for this monogenic disorder.

**Gene-environment interactions.** MyD88-dependent innate signaling (downstream of IL-1 and TLR pathways sensing microbial/endogenous ligands) is **required** for the autoinflammatory phenotype in HOIP deficiency (Wu et al. 2021, [PMID: 34253576](https://pubmed.ncbi.nlm.nih.gov/34253576/)) — implying that microbial/inflammatory environmental input interacts with the genetic lesion to shape the inflammatory phenotype.

---

## 3. Phenotypes

Synthesized from the two index HOIP-deficient patients and the overlapping HOIL-1/RBCK1 disorder (Boisson et al. 2015, [PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/); Oda et al. 2019, [PMID: 30936877](https://pubmed.ncbi.nlm.nih.gov/30936877/); Boisson et al. 2012, [PMID: 23104095](https://pubmed.ncbi.nlm.nih.gov/23104095/)). Onset is in **infancy/early childhood**, with a **chronic/relapsing** course.

| Phenotype | Type | HPO term(s) | Onset / severity / frequency |
|---|---|---|---|
| Multiorgan autoinflammation, recurrent fever | Clinical sign / symptom | HP:0001954 (Recurrent fever), HP:0002960 (Autoimmunity/autoinflammation) | Infancy; moderate–severe; core feature |
| Elevated inflammatory markers (CRP/ESR) | Lab abnormality | HP:0011227 (Elevated CRP) | Present during flares; frequent |
| Combined immunodeficiency, recurrent/invasive infections | Clinical sign | HP:0005387 (Combined immunodeficiency), HP:0002719 (Recurrent infections) | Infancy; severe; core feature |
| Impaired antibody responses (defective CD40-driven B-cell activation) | Lab abnormality | HP:0004313 (Decreased circulating antibody level) | Early; variable |
| Systemic / intestinal lymphangiectasia (± protein-losing enteropathy) | Physical manifestation | HP:0100767 (Lymphangiectasis), HP:0002593 (Intestinal lymphangiectasia) | Early; variable; core feature |
| Amylopectinosis (polyglucosan storage, often subclinical, muscle) | Pathologic manifestation | related to HP:0003198 (Myopathy) | Subclinical; storage |
| Hepatosplenomegaly | Clinical sign | HP:0001433 (Hepatosplenomegaly), HP:0001744 (Splenomegaly) | Variable |
| Failure to thrive / chronic diarrhea | Clinical sign | HP:0001508 (Failure to thrive), HP:0002028 (Chronic diarrhea) | Infancy; variable |

**Progression:** chronic, relapsing autoinflammation punctuated by infection-triggered flares. **Quality-of-life impact:** substantial — recurrent invasive infections, chronic inflammation, and protein-losing enteropathy impair growth, nutrition, and daily functioning; formal QoL instruments (EQ-5D/SF-36/PROMIS) have not been applied given rarity.

**Cellular signature underpinning the paradox:** patient fibroblasts show impaired NF-κB activation to IL-1β/TNF, whereas monocytes are **hyper-responsive** to IL-1β, and B-cell activation/differentiation to CD40 is impaired — "the patient's monocytes respond to IL-1β more vigorously than control monocytes. However, the activation and differentiation of the patient's B cells are impaired in response to CD40 engagement" ([PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)).

---

## 4. Genetic / Molecular Information

**Causal gene:** **RNF31** (HOIP), OMIM 612487, HGNC:16031, NCBI Gene 55072, Ensembl ENSG00000092098, UniProt Q96EP0, locus 14q12. HOIP is the catalytic RBR E3 ligase subunit of LUBAC (HOIP + HOIL-1/RBCK1 + SHARPIN).

**Pathogenic variants (documented):**

| Variant | Type | Domain / consequence | Classification | Reference |
|---|---|---|---|---|
| L72P | Missense | PUB domain; impairs HOIP expression, destabilizes LUBAC (severely hypomorphic) | Pathogenic | [PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/) |
| C-terminal frameshift | Frameshift/null | Premature stop; deletes linear-ubiquitin catalytic (RBR-LDD) domain | Pathogenic (LOF) | [PMID: 39009172](https://pubmed.ncbi.nlm.nih.gov/39009172/) |

**Functional consequence:** **loss of function** — abolition of Met1/linear ubiquitination and destabilization of the LUBAC holocomplex. **Allele frequency:** extremely low; RNF31 is LoF-constrained in gnomAD, so carrier frequency is very low. **Origin:** germline (autosomal recessive); no somatic disease association is described.

**Modifier genes / interactors.** MyD88 is required for the autoinflammatory phenotype ([PMID: 34253576](https://pubmed.ncbi.nlm.nih.gov/34253576/)). TNFR1 (TNFRSF1A) is the dominant genetic modifier in models — its removal rescues lethality/inflammation ([PMID: 25284787](https://pubmed.ncbi.nlm.nih.gov/25284787/), [PMID: 25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/)). OTULIN and A20 (TNFAIP3) counter-regulate the same linear-ubiquitin/NF-κB axis. **Epigenetic** contributions and **chromosomal abnormalities** are not implicated in this monogenic disorder.

---

## 5. Environmental Information

- **Environmental factors / toxins:** none causal.
- **Lifestyle factors:** not applicable (monogenic, pediatric-onset).
- **Infectious agents:** bacteria and viruses act as **triggers and complications** of the underlying combined immunodeficiency (invasive bacterial infections are prominent in the sister HOIL-1 disorder — "invasive bacterial infections," [PMID: 23104095](https://pubmed.ncbi.nlm.nih.gov/23104095/)). LUBAC is required for TLR3-dependent immunity to influenza A virus, so viral susceptibility is expected ([PMID: 27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/)). Microbial/inflammatory input feeding MyD88 signaling drives autoinflammation ([PMID: 34253576](https://pubmed.ncbi.nlm.nih.gov/34253576/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic RNF31 (HOIP) LOF/hypomorphic mutation** → **leads to** reduced HOIP protein and **destabilization/collapse of the LUBAC complex** (demonstrated: [PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)).
2. LUBAC collapse → **results in loss of Met1-linked (linear) polyubiquitination** of substrates (NEMO, RIPK1, etc.), because HOIP's RBR + unique LDD extension is the sole activity specifying linear chains (demonstrated: [PMID: 22863777](https://pubmed.ncbi.nlm.nih.gov/22863777/)).
3. Loss of linear ubiquitination **branches** into two signaling outputs plus a storage/vascular arm:

   **Branch A — Impaired canonical NF-κB signaling (→ immunodeficiency):**
   - 4A. Reduced linear ubiquitination of NEMO → **leads to** defective canonical NF-κB activation in fibroblasts and lymphocytes ([PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/); [PMID: 39009172](https://pubmed.ncbi.nlm.nih.gov/39009172/)).
   - 5A. Impaired NF-κB → **results in** defective CD40-driven B-cell activation/differentiation and **substantial reduction of germinal-center B-cell development** ([PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/); [PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)) and impaired TLR3 antiviral immunity ([PMID: 27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/)) → **combined immunodeficiency**.

   **Branch B — De-repression of TNFR1/TLR3/inflammasome cell death (→ autoinflammation):**
   - 4B. Without linear ubiquitin scaffolding, TNFR1 stimulation **leads to** aberrant cytosolic **complex-II** formation ([PMID: 25284787](https://pubmed.ncbi.nlm.nih.gov/25284787/)).
   - 5B. Complex-II engages **RIPK1 → caspase-8/BID (apoptosis)** and **RIPK3/MLKL (necroptosis)** ([PMID: 25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/)); LUBAC loss also heightens **caspase-1 activation and pyroptosis** upon inflammasome engagement ([PMID: 32122970](https://pubmed.ncbi.nlm.nih.gov/32122970/)) and increases a **TLR3-induced death-inducing complex** ([PMID: 27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/)).
   - 6B. Excess programmed death of **endothelial and epithelial/keratinocyte** cells **results in** tissue injury, release of inflammatory mediators, and (MyD88-dependent) **multiorgan autoinflammation** ([PMID: 34253576](https://pubmed.ncbi.nlm.nih.gov/34253576/)).

   **Branch C — Storage / vascular pathology (mechanism partly inferred):**
   - 4C. LUBAC-subunit loss is associated with accumulation of amylopectin-like **polyglucosan (amylopectinosis)**, paralleling RBCK1/HOIL-1 polyglucosan body myopathy ([PMID: 23995275](https://pubmed.ncbi.nlm.nih.gov/23995275/)) — the precise link between linear-ubiquitin loss and polyglucosan storage remains **inferred**.
   - 5C. Endothelial dysfunction/death contributes to **systemic and intestinal lymphangiectasia** (mechanism inferred from the endothelial-survival role of HOIP; [PMID: 25284787](https://pubmed.ncbi.nlm.nih.gov/25284787/)).

### Detail by category

- **Molecular pathways:** TNFR1/TNF-superfamily signaling, canonical NF-κB (IKK/NEMO), TLR3/TRIF, inflammasome/caspase-1, MyD88/IL-1R. LUBAC-generated linear ubiquitin is the upstream node.
- **Cellular processes:** apoptosis, necroptosis, pyroptosis (all de-repressed); inflammation; impaired lymphocyte activation. **Upstream:** loss of linear ubiquitination. **Downstream:** RIPK1/RIPK3/MLKL/caspase-8/caspase-1 effectors and cytokine release.
- **Protein dysfunction:** loss of function and complex destabilization; HOIP L72P impairs expression, frameshift deletes the catalytic domain — "both LUBAC catalytic activity and LUBAC specificity for linear ubiquitin chain formation are embedded within the RING-IBR-RING (RBR) ubiquitin ligase subunit HOIP" ([PMID: 22863777](https://pubmed.ncbi.nlm.nih.gov/22863777/)).
- **Immune involvement:** both immunodeficiency (NF-κB↓, GC B-cell↓, TLR3 antiviral↓) and autoinflammation (death-driven, monocyte IL-1β hyperresponse).
- **Tissue damage:** endothelial and epithelial programmed cell death; polyglucosan storage.
- **GO / CL suggestions:** GO:0071797 (LUBAC complex), GO:0006954 (inflammatory response), GO:0043123 (positive regulation of canonical NF-κB), GO:0097527 (necroptotic signaling), GO:0006915 (apoptotic process), GO:0043069 (negative regulation of programmed cell death), GO:1990592 (protein linear polyubiquitination), GO:0005829 (cytosol). Cell types: CL:0000115 (endothelial cell), CL:0000576 (monocyte), CL:0000236 (B cell), CL:0000312 (keratinocyte), CL:0000057 (fibroblast), CL:0000815 (regulatory T cell).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** skin (UBERON:0002097), lymphatic vessels (UBERON:0001473), liver (UBERON:0002107), spleen (UBERON:0002106), intestine (UBERON:0000160), skeletal muscle (UBERON:0001134), vascular endothelium (UBERON:0001981).
- **Secondary/system involvement:** immune/lymphoreticular system (secondary lymphoid germinal centers), gastrointestinal system (protein-losing enteropathy), cardiovascular/vascular system.
- **Tissue and cell level:** vascular endothelial cells (CL:0000115), keratinocytes (CL:0000312), monocytes (CL:0000576), B cells (CL:0000236), fibroblasts (CL:0000057), regulatory T cells (CL:0000815).
- **Subcellular (GO-CC):** cytosol (GO:0005829), LUBAC complex (GO:0071797).
- **Localization/lateralization:** systemic and typically bilateral/generalized (multiorgan); no consistent lateralization.

---

## 8. Temporal Development

- **Onset:** congenital/pediatric — manifests in **infancy/early childhood**; pattern chronic/insidious with acute infection- or inflammation-triggered flares.
- **Progression:** chronic, relapsing–remitting inflammatory course; lifelong; storage (amylopectinosis) is slowly accumulating and often subclinical.
- **Disease course:** severe multisystem; potentially life-threatening (the complete HOIL-1 counterpart was originally a "fatal human inherited disorder," [PMID: 23104095](https://pubmed.ncbi.nlm.nih.gov/23104095/)).
- **Remission patterns:** treatment-induced (anti-TNF produced complete remission of autoinflammation in a LUBAC-group patient, [PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)); no reliable spontaneous remission.
- **Critical periods:** early infancy (infection vulnerability) is the key window for diagnosis and intervention.

---

## 9. Inheritance and Population

- **Epidemiology:** exceedingly rare; only a small number of patients reported worldwide since the 2015 first description. No established prevalence/incidence (Orphanet-level "unknown"; ORPHA not firmly assigned).
- **Inheritance:** **autosomal recessive** — all patients homozygous for biallelic RNF31 LOF/hypomorphic alleles ([PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)); consistent with consanguineous/founder backgrounds.
- **Penetrance:** complete in reported homozygotes; **expressivity** severe.
- **Anticipation / germline mosaicism:** not applicable/not reported.
- **Founder effects / carrier frequency:** very low carrier frequency (RNF31 LoF-constrained in gnomAD); biallelic disease vanishingly rare.
- **Sex ratio:** no predilection (AR). **Age distribution:** pediatric onset.

---

## 10. Diagnostics

**Recommended approach:** molecular genetics plus functional confirmation.

- **Genetic testing:** identification of biallelic **RNF31** pathogenic variants by **whole-exome (WES)** or **whole-genome (WGS)** sequencing, or via **inborn-errors-of-immunity / autoinflammatory gene panels** including RNF31/HOIP; confirm with single-gene/Sanger testing and family segregation (AR). CMA/karyotype/FISH/mtDNA/repeat-expansion testing are not indicated as first-line.
- **Functional confirmation (established in original reports):** reduced HOIP expression and destabilized LUBAC on immunoblot; impaired Met1/linear ubiquitination; **defective NF-κB activation in patient fibroblasts to IL-1β/TNF with paradoxical monocyte IL-1β hyper-responsiveness**; impaired CD40-induced B-cell activation — "Linear ubiquitination and NF-κB activation are impaired in the patient's fibroblasts stimulated by IL-1β or TNF. In contrast, the patient's monocytes respond to IL-1β more vigorously than control monocytes" ([PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)).
- **Supportive labs/pathology:** elevated CRP/ESR and proinflammatory cytokines; immunologic workup showing combined immunodeficiency (antibody defect); **PAS-positive, diastase-resistant polyglucosan/amylopectin inclusions** on muscle/tissue biopsy (amylopectinosis); imaging/endoscopy showing lymphangiectasia and protein-losing enteropathy.
- **Differential diagnosis:** HOIL-1/RBCK1 deficiency and SHARPIN deficiency (sister LUBAC disorders), OTULIN deficiency (ORAS/otulipenia), A20 haploinsufficiency (HA20), other combined immunodeficiencies/CVID, and glycogen storage disease type IV / polyglucosan body disorders. OTULIN- and A20-deficient cells show **excess** Met1/K63 chains and constitutive NF-κB — the mirror image of LUBAC deficiency: "OTULIN or A20-deficient cells have an excess of Met1 or K63 Ub chains on NEMO, RIPK1, and other target substrates, which lead to constitutive activation of the NF-kB pathway" ([PMID: 28469620](https://pubmed.ncbi.nlm.nih.gov/28469620/)).
- **Screening:** carrier/cascade testing in affected families; prenatal / preimplantation genetic testing available; not a newborn-screening target.

---

## 11. Outcome / Prognosis

- **Severity/mortality:** severe, potentially life-threatening multisystem disease; the analogous complete HOIL-1 deficiency was a "fatal human inherited disorder characterized by chronic autoinflammation, invasive bacterial infections and muscular amylopectinosis" ([PMID: 23104095](https://pubmed.ncbi.nlm.nih.gov/23104095/)). Morbidity/mortality are driven by recurrent invasive infections and organ-damaging autoinflammation.
- **Morbidity/function:** chronic inflammation, protein-losing enteropathy, growth failure, and infection burden impair function and quality of life.
- **Complications:** invasive bacterial/viral infections, organ inflammation (liver, spleen, gut), lymphangiectasia-related protein loss, storage pathology.
- **Prognostic factors:** variant severity (hypomorphic vs null), infection control, and access to anti-cytokine therapy. Formal survival statistics are not established due to rarity.

---

## 12. Treatment

**No curative therapy exists.** Management combines targeted anti-cytokine therapy, immune support, and supportive care.

| Modality | Rationale / evidence | NCIT suggestion |
|---|---|---|
| **Anti-TNF therapy** (etanercept, infliximab, adalimumab) | TNF-superfamily drives the lethal cell-death branch; anti-TNF gave **complete clinical and transcriptomic resolution** of autoinflammation in a SHARPIN-deficient (LUBAC-group) patient ([PMID: 38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/)) | NCIT:C2536 (TNF antagonist) |
| **IL-1 blockade** (anakinra, canakinumab) | Monocyte IL-1β hyperresponse; inflammasomopathy treatment "often aimed at interleukin-1 (IL-1) blockade" ([PMID: 37821203](https://pubmed.ncbi.nlm.nih.gov/37821203/)) | NCIT:C2551 (Interleukin-1 Receptor Antagonist) |
| **JAK inhibition** (ruxolitinib, baricitinib) | Rational for NF-κB/inflammasome-driven inflammation and interferon signatures ([PMID: 37821203](https://pubmed.ncbi.nlm.nih.gov/37821203/)) | NCIT:C129824 (JAK inhibitor) |
| **Immunoglobulin replacement + antimicrobial prophylaxis** | Corrects/mitigates combined immunodeficiency; avoid live vaccines | NCIT:C29799 (IVIG) |
| **Supportive care** for lymphangiectasia/enteropathy (nutrition, albumin) | Manages protein-losing enteropathy | — |
| **HSCT (theoretical)** | Could correct hematopoietic immunodeficiency but **would NOT** correct LUBAC loss in non-hematopoietic cells (endothelium, fibroblasts, muscle) driving lymphangiectasia and amylopectinosis | NCIT:C15431 (Hematopoietic Stem Cell Transplantation) |

**Pharmacogenomics / personalized medicine:** treatment is genotype-driven at the level of pathway (TNF/IL-1/JAK blockade selected by mechanism). **Experimental:** LUBAC-targeting small molecules (HOIPINs) exist as research tools but are inhibitors, not activators, and are not therapeutic here.

---

## 13. Prevention

- **Primary prevention:** not possible (monogenic, germline). Prevention is limited to reproductive/genetic strategies.
- **Genetic counseling:** 25% recurrence risk for carrier couples; **cascade carrier testing**; options for **prenatal diagnosis** and **preimplantation genetic testing (PGT)**.
- **Secondary/tertiary prevention:** early diagnosis and initiation of anti-cytokine therapy; antimicrobial prophylaxis and immunoglobulin replacement to prevent infections; avoidance of live vaccines given combined immunodeficiency; nutritional support to prevent complications of enteropathy.
- **Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** mouse *Rnf31* (Hoip), NCBI Taxon 10090. HOIP/LUBAC is evolutionarily conserved across mammals.
- **Natural disease in other species:** no naturally occurring companion-animal or wildlife HOIP-deficiency disease is documented (OMIA); disease knowledge is from engineered laboratory models. RBCK1/HOIL-1 links to polyglucosan storage provide comparative-pathology parallels ([PMID: 23995275](https://pubmed.ncbi.nlm.nih.gov/23995275/)).
- **Evolutionary conservation of mechanism:** the TNFR1-driven death sensitivity and NF-κB dependence on linear ubiquitination are conserved between human and mouse (rescue of murine lethality by Tnfr1 ablation mirrors human TNF-driven pathology).
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

**Mouse** (*Mus musculus*, Taxon 10090) is the principal model system.

| Model | Phenotype | Key finding | Reference |
|---|---|---|---|
| Constitutive *Hoip* KO; Tie2-Cre endothelial *Hoip* deletion | **Embryonic lethal ~E10.5** from aberrant TNFR1-mediated endothelial death, defective vascularization | "**Ablation of tumor necrosis factor receptor 1 (TNFR1) prevents cell death, vascularization defects, and death at midgestation**" | [PMID: 25284787](https://pubmed.ncbi.nlm.nih.gov/25284787/) |
| *Sharpin*-null **cpdm** mouse (spontaneous) | Chronic proliferative dermatitis, liver inflammation, splenomegaly, loss of Peyer's patches | "**TNF-dependent multi-organ inflammation**"; RIPK3/MLKL + caspase-8 effectors | [PMID: 25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/) |
| cpdm variants (Tlr3 co-ablation) | Dermatitis ameliorated | Excess **TLR3-induced** cell death contributes to disease | [PMID: 27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/) |
| Treg-specific *Sharpin* ± *Hoip* disruption | cpdm-like → **T-cell-predominant autoimmune** lesions | "**additional disruption of the Hoip locus... converts cpdm-like dermatitis to T cell-predominant autoimmune lesions**" | [PMID: 31462647](https://pubmed.ncbi.nlm.nih.gov/31462647/) |

**Model types available:** knockout (constitutive and conditional/tissue-specific via Cre), spontaneous mutant (cpdm). **Phenotype recapitulation:** models faithfully reproduce the **TNF-driven cell-death and inflammation** arm and its genetic rescue, providing strong mechanistic validation. **Limitations:** complete Hoip/Hoil-1 knockouts are **embryonic lethal** — "their genetic ablation is embryonically lethal in mice" ([PMID: 32122970](https://pubmed.ncbi.nlm.nih.gov/32122970/)) — so viable models rely on Sharpin-null cpdm or conditional deletions; the human hypomorphic (partial-function) state and full multisystem human phenotype (amylopectinosis, lymphangiectasia) are incompletely captured. **Resources:** MGI, IMPC/IMSR for Rnf31 alleles.

---

## Mechanistic Model / Interpretation

**Capstone synthesis (Finding F013).** HOIP deficiency is best understood as a **LUBAC "survival-brake" disorder**. A single molecular lesion — loss of Met1/linear ubiquitination — produces a bifurcated signaling output plus storage/vascular pathology:

```
   Biallelic RNF31 (HOIP) LOF / hypomorphic mutation
                 │
                 ▼
     LUBAC complex collapse  (HOIP + HOIL-1 + SHARPIN)
                 │
                 ▼
   Loss of Met1-linked (linear) polyubiquitination
        (NEMO, RIPK1, caspase-1 CARD, ...)
                 │
      ┌──────────┴───────────────┬─────────────────────┐
      ▼                          ▼                     ▼
 (A) Impaired canonical     (B) De-repressed         (C) Storage /
     NF-κB signaling            programmed cell           vascular
      │                          death (TNFR1          pathology
      ▼                          complex-II,             │
 - Defective CD40 B-cell         TLR3, inflammasome)    ▼
   activation                    │                   - Amylopectinosis
 - ↓ Germinal-center         RIPK1→caspase-8         (polyglucosan)
   B cells                    (apoptosis)            - Systemic /
 - Impaired TLR3               RIPK3/MLKL              intestinal
   antiviral immunity         (necroptosis)           lymphangiectasia
      │                       caspase-1               (endothelial
      ▼                       (pyroptosis)             death; inferred)
 COMBINED                        │
 IMMUNODEFICIENCY                ▼  (MyD88-dependent)
                            MULTIORGAN AUTOINFLAMMATION
                                 │
                                 ▼
                    Anti-TNF / IL-1 / JAK blockade
                    resolves the inflammatory branch
```

The elegance — and the paradox — of the disease is that the **same** enzymatic defect that **weakens** activating signaling (NF-κB → immunodeficiency) simultaneously **removes a checkpoint** that normally restrains death-inducing complexes (→ autoinflammation). The two arms are not contradictory but two faces of one lost function: linear ubiquitin is both a **signaling amplifier** for NF-κB and a **survival scaffold** that keeps TNFR1/TLR3/inflammasome signaling from tipping into cell death. This places HOIP deficiency firmly within the ubiquitin/NF-κB-dysregulation class of autoinflammatory diseases, alongside OTULIN deficiency (ORAS) and A20 haploinsufficiency (HA20) — but on the opposite side of the ubiquitin balance: LUBAC deficiency **removes** linear chains, whereas OTULIN/A20 loss leaves **excess** chains and constitutive NF-κB. As Boisson et al. concluded, "human HOIP is essential for the assembly and function of LUBAC and for various processes governing inflammation and immunity in both hematopoietic and nonhematopoietic cells" ([PMID: 26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/)) — explaining why HSCT (a hematopoietic fix) cannot cure the non-hematopoietic (vascular, muscle, epithelial) manifestations.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [26008899](https://pubmed.ncbi.nlm.nih.gov/26008899/) | *Human HOIP and LUBAC deficiency underlies autoinflammation, immunodeficiency, amylopectinosis, and lymphangiectasia* | **Index case**; defines cardinal phenotype, L72P allele, LUBAC destabilization, and the fibroblast-NF-κB↓/monocyte-IL-1β↑ signature |
| [39009172](https://pubmed.ncbi.nlm.nih.gov/39009172/) | *A novel HOIP frameshift variant alleviates NF-κB signalling and sensitizes cells to TNF-induced death* | Second molecular class (frameshift null); confirms NF-κB suppression + TNF-induced death in human cells |
| [30936877](https://pubmed.ncbi.nlm.nih.gov/30936877/) | *Second Case of HOIP Deficiency…* | Expands clinical features; defines LUBAC-regulated inflammatory transcriptome |
| [22863777](https://pubmed.ncbi.nlm.nih.gov/22863777/) | *E3 ligase HOIP specifies linear ubiquitin chain assembly…* | Biochemical basis: HOIP RBR+LDD is the catalytic engine for linear chains |
| [25284787](https://pubmed.ncbi.nlm.nih.gov/25284787/) | *HOIP deficiency causes embryonic lethality by aberrant TNFR1-mediated endothelial cell death* | Mouse model; TNFR1-driven death branch, rescued by TNFR1 ablation |
| [25443632](https://pubmed.ncbi.nlm.nih.gov/25443632/) | *TNFR1-dependent cell death drives inflammation in Sharpin-deficient mice* | cpdm model; RIPK3/MLKL + caspase-8 effectors |
| [27810922](https://pubmed.ncbi.nlm.nih.gov/27810922/) | *LUBAC deficiency perturbs TLR3 signaling…* | TLR3 antiviral gating; TLR3-induced death complex |
| [32122970](https://pubmed.ncbi.nlm.nih.gov/32122970/) | *Cross-regulation between LUBAC and caspase-1…* | Inflammasome/pyroptosis branch; embryonic lethality of KO |
| [34253576](https://pubmed.ncbi.nlm.nih.gov/34253576/) | *MyD88-Dependent Signaling Is Required for HOIP Deficiency-Induced Autoinflammation* | MyD88 as required node for the autoinflammatory arm |
| [31462647](https://pubmed.ncbi.nlm.nih.gov/31462647/) | *Modulation of autoimmune pathogenesis by T cell-triggered inflammatory cell death* | Conditional Hoip mouse; T-cell autoimmune lesions |
| [38609546](https://pubmed.ncbi.nlm.nih.gov/38609546/) | *Biallelic human SHARPIN loss of function…* | Completes LUBAC trio; shared GC-B-cell defect; **anti-TNF resolves autoinflammation** |
| [28469620](https://pubmed.ncbi.nlm.nih.gov/28469620/) | *NF-κB Pathway in Autoinflammatory Diseases… Ubiquitin* | Nosology: LUBAC vs OTULIN vs A20; shared cellular signature |
| [23104095](https://pubmed.ncbi.nlm.nih.gov/23104095/) | *Immunodeficiency, autoinflammation and amylopectinosis… HOIL-1 and LUBAC deficiency* | Sister disorder; overlapping fatal phenotype |
| [23995275](https://pubmed.ncbi.nlm.nih.gov/23995275/) | *New insights in muscle glycogenoses* | RBCK1/polyglucosan storage link (amylopectinosis) |
| [37821203](https://pubmed.ncbi.nlm.nih.gov/37821203/) | *Targeted Treatment of Diseases of Immune Dysregulation* | IL-1 blockade / JAK inhibition rationale |

**Evidence source types:** human clinical/cellular (26008899, 39009172, 30936877, 38609546, 23104095), biochemical/in-vitro (22863777, 32122970), and model-organism (25284787, 25443632, 27810922, 31462647, 34253576).

---

## Limitations and Knowledge Gaps

1. **Extreme rarity / very small n.** Only a handful of HOIP-deficient patients are described; phenotype frequencies, natural history, penetrance nuances, and survival statistics are not robustly quantified. Much of the clinical spectrum is extrapolated from the sister LUBAC disorders (HOIL-1, SHARPIN).
2. **No HOIP-specific treatment trials.** The strongest therapeutic evidence (complete anti-TNF remission) comes from a **SHARPIN-deficient** patient; direct HOIP-deficiency treatment outcomes are anecdotal.
3. **Model limitations.** Complete Hoip knockout is embryonic lethal, so viable mechanistic modeling depends on conditional deletions and the Sharpin cpdm mouse; the human **hypomorphic** state and the full multisystem human phenotype (amylopectinosis, lymphangiectasia) are incompletely recapitulated.
4. **Mechanism of storage and lymphangiectasia is inferred.** The causal link from linear-ubiquitin loss to polyglucosan storage and to lymphatic pathology is not fully demonstrated.
5. **No disease-specific population genetics.** RNF31 constraint is inferred from gnomAD; no formal carrier-screening or founder studies exist.
6. **Incomplete ontology mapping.** ORPHA assignment and some HPO frequency annotations remain incomplete for this newly delineated entity.

---

## Proposed Follow-up Experiments / Actions

1. **Patient registry / natural-history study** pooling all reported HOIP (and LUBAC-trio) cases to quantify phenotype frequencies, onset, penetrance, and survival, and to standardize HPO annotation.
2. **Genotype–phenotype correlation:** systematically compare hypomorphic missense (L72P-type) vs null (frameshift) alleles for severity, storage burden, and treatment response.
3. **Prospective anti-cytokine therapy evaluation** in confirmed HOIP-deficiency patients (anti-TNF first-line; IL-1 and JAK inhibition as alternatives) with transcriptomic monitoring, mirroring the SHARPIN case.
4. **Patient-derived iPSC / organoid and endothelial models** to dissect the amylopectinosis and lymphangiectasia mechanisms that mouse models miss, and to test whether death-pathway inhibitors (RIPK1/RIPK3/MLKL/caspase inhibitors) protect endothelium.
5. **HSCT outcome documentation** to empirically test the prediction that transplantation corrects immunodeficiency but not the non-hematopoietic (vascular/storage) pathology.
6. **Functional variant curation** in ClinVar/ClinGen for RNF31 to support ACMG classification and cascade/prenatal testing.

---

*Report compiled from 13 confirmed findings and 29 reviewed papers across a 5-iteration autonomous investigation. Ontology suggestions (HPO, GO, CL, UBERON, NCIT, MONDO) are provided throughout for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](HOIP_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](HOIP_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 23 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957981` (2 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 115 with autoinflammation**
- `NCIT:C2551` (1 mention) - the report calls it "Interleukin-1 Receptor Antagonist"; NCIT calls it **CP-609,754**
- `NCIT:C29799` (1 mention) - the report calls it "IVIG"; NCIT calls it **3-Nitrobenzo[a]pyrene trans-7,8-Dihydrodiol**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011227` (1 mention) - the report calls it "Elevated CRP"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated CRP" among its other names
- `GO:0043123` (1 mention) - the report calls it "positive regulation of canonical NF-κB"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**
- `GO:0097527` (1 mention) - the report calls it "necroptotic signaling"; GO calls it **necroptotic signaling pathway**, and lists "necroptosis signaling" among its other names
- `GO:1990592` (1 mention) - the report calls it "protein linear polyubiquitination"; GO calls it **protein K69-linked ufmylation**
- `CL:0000115` (2 mentions) - the report calls it "endothelial cell", "Tissue and cell level:** vascular endothelial cells"; CL calls it **endothelial cell**
- `NCIT:C2536` (1 mention) - the report calls it "TNF antagonist"; NCIT calls it **Canarypox Antigen**, and lists "Canarypox Antigens" among its other names
- `NCIT:C129824` (1 mention) - the report calls it "JAK inhibitor"; NCIT calls it **Antineoplastic Protein Inhibitor**, and lists "Anti-cancer Protein Inhibitor" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000115` - called "endothelial cell", "Tissue and cell level:** vascular endothelial cells"