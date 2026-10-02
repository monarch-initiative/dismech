---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T02:16:43.732551'
end_time: '2026-09-04T03:14:41.528808'
duration_seconds: 3477.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 67
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 15
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 13
  relevance_assessed: 18
  on_topic: 12
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - Orphanet
  - NANDO
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_67-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_67-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 67
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 67** covering all of the
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

# Immunodeficiency 67 (IRAK-4 Deficiency): Comprehensive Disease Characterization

**Disease:** Immunodeficiency 67 (IMD67) — Autosomal Recessive Human IRAK-4 Deficiency
**MONDO ID:** MONDO:0011888 | **OMIM:** #607676 | **Orphanet:** 70592
**Category:** Mendelian (autosomal recessive inborn error of innate immunity)
**Causal gene:** *IRAK4* (12q12; HGNC:17967; NCBI Gene 51135; Ensembl ENSG00000198001; UniProt Q9NWZ3)

---

## Summary

**Immunodeficiency 67 is autosomal recessive human IRAK-4 deficiency**, a Mendelian inborn error of innate immunity caused by biallelic loss-of-function mutations in *IRAK4*, the gene encoding interleukin-1 receptor-associated kinase 4. IRAK-4 is a Ser/Thr kinase that sits at the heart of the MyD88-dependent "Myddosome" signaling platform, transducing signals from nearly all Toll-like receptors (all except TLR3) and every member of the interleukin-1 receptor family. Complete loss of IRAK-4 function abolishes activation of NF-κB and MAPK downstream of these Toll/IL-1 receptor (TIR)-domain receptors, so affected cells fail to mount inflammatory cytokine responses to purified TLR and IL-1R agonists.

Paradoxically, despite the breadth of receptors that depend on IRAK-4, the clinical phenotype is **narrow**: patients are selectively susceptible to a small set of pyogenic (pus-forming) bacteria, dominated by *Streptococcus pneumoniae*, with *Staphylococcus aureus* and *Pseudomonas aeruginosa* next in frequency. In the largest cohort (48 patients), invasive pneumococcal disease occurred in 68% of patients, the first invasive infection struck before age 2 in 88%, and mortality was high in early childhood (24 deaths). A clinical hallmark is **blunted or delayed inflammation** — patients often have no fever and weak acute-phase responses despite overwhelming invasive infection, which dangerously masks severity. Crucially, susceptibility and mortality **improve markedly with age**, presumably as adaptive immunity and anti-pneumococcal antibody develop.

Management is entirely **preventive and supportive**: continuous antibiotic prophylaxis, pneumococcal conjugate/polysaccharide vaccination, immunoglobulin replacement, caregiver vigilance, and immediate empiric broad-spectrum antibiotics at the first sign of infection. No curative pharmacotherapy exists; hematopoietic stem cell transplantation is generally not indicated because prognosis improves with age, and there is no gene or cell therapy in clinical use. Breakthrough invasive disease can still be fatal even in fully vaccinated, prophylaxed patients. An emerging extension of the phenotype is heightened susceptibility to severe COVID-19, attributed to impaired TLR7-dependent type I interferon production.

---

## Key Findings

### 1. Disease identity and genetic basis (F001, F010, F014)

Immunodeficiency 67 is the OMIM designation (#607676) for autosomal recessive human IRAK-4 deficiency. It is caused by **biallelic loss-of-function mutations in *IRAK4*** (interleukin-1 receptor-associated kinase 4; gene OMIM 606883; HGNC:17967; NCBI Gene 51135; Ensembl ENSG00000198001; UniProt Q9NWZ3), located at chromosome **12q12**. IRAK4 is essential for signaling downstream of most Toll-like receptors (all except TLR3) and all IL-1 receptor family members via the MyD88-dependent Myddosome complex, culminating in activation of NF-κB and MAPK. As a review states, "*interleukin-1 receptor-associated kinase 4 (IRAK4) plays a vital role in the TLR signaling cascade*" and "*Human IRAK4 deficiency is an autosomal recessive inborn error of immunity that classically presents with blunted or delayed inflammatory response to infection and susceptibility to a narrow spectrum of pyogenic bacteria*" [PMID: 32532880](https://pubmed.ncbi.nlm.nih.gov/32532880/).

**Complete identifier set (from MONDO:0011888):** OMIM:607676; Orphanet:70592; MeSH C563662 & C564352; UMLS C1843256; MedGen 375137; GARD 0010311; NANDO:1200361/2200762. **Synonyms/alternative names:** IRAK-4 deficiency; IRAK4 deficiency; IRAK4D; immunodeficiency due to interleukin-1 receptor-associated kinase-4 deficiency; and the phenotype-based synonym **"recurrent isolated invasive pneumococcal disease, type 1" (IPD1)**. **ICD-11** maps to the category 4A00.1 (immunodeficiencies due to defects in innate immunity / Toll-like receptor signaling pathway defects); **ICD-10** maps to D84.8/D84.9 (other/unspecified immunodeficiency).

Information for this entry is derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, HPO) and from published case series and case reports rather than individual EHR data.

### 2. Molecular mechanism: total loss of TIR-receptor signaling (F003, F008)

In the founding report (Picard et al., *Science* 2003), blood and fibroblasts from IRAK-4-deficient children "*did not activate nuclear factor kappaB and mitogen-activated protein kinase (MAPK) and failed to induce downstream cytokines in response to any of the known ligands of TIR-bearing receptors*" [PMID: 12637671](https://pubmed.ncbi.nlm.nih.gov/12637671/). Because the children were otherwise healthy except for pyogenic bacterial infections, the authors concluded that "*the TIR-IRAK signaling pathway is crucial for protective immunity against specific bacteria but is redundant against most other microorganisms*" [PMID: 12637671](https://pubmed.ncbi.nlm.nih.gov/12637671/). This defines both the mechanism (a complete block of TIR-receptor → NF-κB/MAPK signaling) and the reason for the surprisingly narrow infection susceptibility (redundancy against viruses, fungi, parasites, and most bacteria).

**Protein architecture:** IRAK4 (UniProt Q9NWZ3, 460 aa) has an **N-terminal death domain** that mediates recruitment to the MyD88-nucleated Myddosome, and a **C-terminal Ser/Thr kinase domain**. "*Upon ligand binding and via its N-terminal death domain, IRAK4 is recruited to an oligomeric receptor that is proximal to the Myddosome signaling complex, inducing IRAK4 kinase domain dimerization, autophosphorylation, and activation*" [PMID: 30679311](https://pubmed.ncbi.nlm.nih.gov/30679311/). Pathogenic variants span nonsense, frameshift, and splice-site alleles (LoF; the most common class — e.g., p.Gln293*/c.877C>T; splice c.942-1G>A) as well as missense variants in the kinase domain — all abrogating kinase activity or protein expression.

### 3. Clinical spectrum and outcome (F002, F011)

The largest cohort (Picard et al. 2010; 48 IRAK-4-deficient patients from 37 kindreds in 15 countries) established the natural history:

| Feature | Value |
|---|---|
| Invasive pneumococcal disease | 41/48 patients (68%); 52.2% of all invasive infections |
| Invasive *P. aeruginosa* / *S. aureus* | ~16–17% each |
| First invasive infection before age 2 | 88.3% |
| First invasive infection in neonatal period | 32.7% |
| Systemic inflammatory signs | Usually weak or delayed |
| Deaths | 24 |
| Recurrent invasive infection in survivors | 36/50 (72%) |

Key quotes: "*The leading threat was invasive pneumococcal disease, documented in 41 patients (68%) and causing 72 documented invasive infections (52.2%)*"; "*The first invasive infection occurred before the age of 2 years in 53 (88.3%) and in the neonatal period in 19 (32.7%) patients*"; "*Systemic signs of inflammation were usually weak or delayed*"; "*Multiple or recurrent invasive infections were observed in most survivors (n = 36/50, 72%)*"; and "*Clinical outcome was poor, with 24 deaths*" [PMID: 21057262](https://pubmed.ncbi.nlm.nih.gov/21057262/). Deaths clustered around the first invasive episode and around invasive pneumococcal disease, but invasive infections and deaths became rare after childhood — an **age-dependent improvement** in outcome.

**Phenotype/HPO annotations:** recurrent invasive bacterial infection (HP:0002719 Recurrent infections; HP:0002718 Recurrent bacterial infections), invasive pneumococcal disease with sepsis (HP:0100806) and meningitis (HP:0001287), cutaneous/skin abscesses mainly from *S. aureus* (HP:0100658; HP:0032243), upper respiratory tract infection (HP:0002788), septic arthritis (HP:0001369) and osteomyelitis (HP:0002754), and lymphadenitis (HP:0002840). Laboratory hallmarks: **absent/blunted fever** (HP:0001945 often ABSENT), weak acute-phase response with low or paradoxically normal CRP, and transient neutropenia during sepsis (HP:0001875). Immunoglobulins and lymphocyte subsets are typically normal. Severity is greatest in infancy and improves with age; the course is episodic/recurrent.

### 4. Population genetics: recessive, LoF-tolerant gene (F004, F013)

gnomAD constraint metrics for *IRAK4* confirm the gene is **not** haploinsufficient: pLI ≈ 2.5×10⁻¹³ (essentially 0), observed/expected LoF ratio (oe_lof) = 0.85 (90% CI 0.67–1.09; LOEUF ~1.09), with 44 observed vs 51.8 expected LoF variants. This LoF tolerance is fully consistent with **autosomal recessive inheritance and asymptomatic heterozygous carriers**.

Inheritance is autosomal recessive with **complete penetrance** for the immunodeficiency but **highly variable expressivity** (age of first infection, organ site, survival). Estimated prevalence is **<1/1,000,000** (Orphanet:70592; ultra-rare); total published cases number in the low hundreds. Sex ratio ~1:1 (autosomal). Both consanguineous (homozygous) and non-consanguineous (compound heterozygous) kindreds are reported across many ethnicities — "*48 patients with IRAK-4 deficiency and 12 patients with MyD88 deficiency, from 37 kindreds in 15 countries*" [PMID: 21057262](https://pubmed.ncbi.nlm.nih.gov/21057262/). There is no genetic anticipation, mitochondrial inheritance, or recurrent large chromosomal abnormality. No single founder mutation dominates, though recurrent alleles (e.g., c.877C>T p.Gln293*) recur across unrelated families.

### 5. Extended phenotype: severe COVID-19 (F005)

An important recent extension of the phenotype: in a 22-patient series of AR MyD88 or IRAK-4 deficiency (mean age 10.9 yr) infected with SARS-CoV-2, 16/22 were hospitalized (6 moderate, 4 severe, 6 critical pneumonia, 1 death). "*The risk of invasive mechanical ventilation was also much greater than in age-matched controls from the general population (OR: 74.7, 95% CI: 26.8-207.8, P < 0.001)*" [PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/). The mechanism: "*The patients' susceptibility to SARS-CoV-2 can be attributed to impaired TLR7-dependent type I IFN production by pDCs*" [PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/). This links IRAK-4 to antiviral defense via the TLR7/plasmacytoid dendritic cell/type I interferon axis — a susceptibility not fully appreciated from the classic bacterial-only picture.

### 6. Human vs. mouse: a striking phenotypic contrast (F006)

Mouse *Myd88*/*Irak4* knockouts are broadly susceptible to many pathogens, whereas humans have a narrow phenotype. von Bernuth et al. note "*MyD88 deficiency in mice leads to susceptibility to a broad range of pathogens in experimental settings of infection*," whereas human AR MyD88-deficient children suffered a narrow range of pyogenic bacterial infections and "*these patients were otherwise healthy, with normal resistance to other microbes. Their clinical status improved with age*" [PMID: 18669862](https://pubmed.ncbi.nlm.nih.gov/18669862/). The same contrast applies to *Irak4*-knockout mice versus human IRAK-4 deficiency. This has major implications for model-organism interpretation (see Section 15).

### 7. Diagnosis and management (F007, F009, F012)

**Diagnosis** rests on demonstrating **absent cellular responses to TLR/IL-1R (TIR) agonists** — no NF-κB/MAPK activation and no cytokine (IL-6, TNF) induction in blood/fibroblasts [PMID: 12637671](https://pubmed.ncbi.nlm.nih.gov/12637671/) — confirmed by biallelic *IRAK4* mutation on sequencing (WES or gene panel). Rapid functional assays include flow-cytometric measurement of IκB-α degradation after TLR stimulation (Frans et al. 2024, [PMID: 37929815](https://pubmed.ncbi.nlm.nih.gov/37929815/)) and NF-κB reporter assays in IRAK4-null HEK293T cells: "*We established a novel NF-κB reporter assay using IRAK4-null HEK293T, which enabled the precise evaluation of IRAK4 mutations*" [PMID: 33083971](https://pubmed.ncbi.nlm.nih.gov/33083971/). A critical diagnostic clue is severe invasive infection with characteristically **low or delayed inflammatory signs** — patients often lack fever and have blunted acute-phase responses (though CRP can sometimes be elevated).

**Anatomical structures affected** (because IRAK4 is ubiquitously expressed, disease occurs wherever pyogenic bacteria invade): bloodstream (UBERON:0000178; sepsis/bacteremia), meninges/CNS (UBERON:0002360; meningitis, brain abscess), lungs (UBERON:0002048; pneumonia/empyema), skin and soft tissue (UBERON:0002097; abscesses, cellulitis), bone and joints (UBERON:0002481; osteomyelitis, septic arthritis), lymph nodes (UBERON:0000029; lymphadenitis), and upper respiratory tract (UBERON:0001557). The Picard cohort noted infection "*with a high incidence of infections of the upper respiratory tract and the skin*" [PMID: 21057262](https://pubmed.ncbi.nlm.nih.gov/21057262/). Key cell types with defective TLR/IL-1R signaling: monocytes/macrophages (CL:0000576/CL:0000235), neutrophils (CL:0000775), dendritic cells including plasmacytoid DCs (CL:0000784), and non-hematopoietic cells such as fibroblasts and epithelial cells. Subcellular: the cytoplasmic Myddosome platform and endosomal TLR compartment (GO:0035325 Toll-like receptor binding; GO:0007249 canonical NF-κB signal transduction).

**Management** is preventive: continuous antimicrobial prophylaxis (e.g., penicillin V or trimethoprim-sulfamethoxazole), pneumococcal conjugate/polysaccharide vaccination (PCV13, PPSV23), often immunoglobulin replacement, caregiver vigilance, and immediate empiric broad-spectrum antibiotics at the first sign of infection. Yet breakthrough disease occurs: a vaccinated, prophylaxed girl "*was managed with antibiotic prophylaxis (sulfa/trimethoprim/PenV, then - due to neutropenia - Cefprozil), pneumococcal vaccination (PCV-7, Pneumovax23, PCV-13) and vigilance*" but died of pneumococcal (serotype 6C) meningitis at age 7 [PMID: 24596024](https://pubmed.ncbi.nlm.nih.gov/24596024/). That report emphasizes that "*IRAK-4 deficiency causes IL-1R and TLR signaling failure, resulting in minimal clinical features despite invasive bacterial infection*" [PMID: 24596024](https://pubmed.ncbi.nlm.nih.gov/24596024/) — the central reason vigilance and empiric treatment are essential.

---

## Mechanistic Model / Causal Chain

**Ordered causal chain from mutation to clinical manifestation:**

1. **Biallelic loss-of-function mutation in *IRAK4*** (12q12) **leads to** absent or non-functional IRAK-4 kinase protein.
2. Absence of functional IRAK-4 **results in** failure to assemble/activate the MyD88-nucleated **Myddosome** — IRAK-4 can no longer be recruited via its death domain, dimerize, autophosphorylate, and activate downstream IRAK1/IRAK2 [PMID: 30679311](https://pubmed.ncbi.nlm.nih.gov/30679311/).
3. Myddosome failure **abolishes** signal transduction from all TIR-domain receptors that use MyD88 — **all TLRs except TLR3** and **all IL-1R family receptors** (IL-1R, IL-18R, IL-33R).
4. This **results in** failure to activate **NF-κB and MAPK**, so cells "*failed to induce downstream cytokines in response to any of the known ligands of TIR-bearing receptors*" [PMID: 12637671](https://pubmed.ncbi.nlm.nih.gov/12637671/).
5. Loss of pro-inflammatory cytokine induction (IL-6, TNF, IL-1β) **leads to** a **blunted/absent acute-phase response and fever** — invasive infection proceeds with "minimal clinical features."
6. **Branch A (dominant — bacterial):** Impaired early innate sensing of pyogenic bacteria (especially encapsulated *S. pneumoniae*) **leads to** failure to contain infection at mucosal/entry sites → invasive bacteremia, meningitis, pneumonia, abscesses. This is worst in infancy, before protective anti-pneumococcal antibody develops, and **improves with age** as adaptive immunity matures.
7. **Branch B (viral, inferred/emerging):** Loss of **TLR7-dependent type I IFN production by plasmacytoid dendritic cells** **results in** susceptibility to severe SARS-CoV-2 pneumonia [PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/).

```
IRAK4 biallelic LoF
        │
        ▼
No functional IRAK-4 kinase
        │
        ▼
Myddosome cannot assemble/activate  ◄── death-domain recruitment + kinase dimerization lost
        │
        ▼
All MyD88-dependent TIR receptors silenced
 (TLR1/2/4/5/6/7/8/9  +  IL-1R/IL-18R/IL-33R;  NOT TLR3)
        │
        ▼
No NF-κB / MAPK activation → no inflammatory cytokines
        │
        ├─────────────► Blunted fever & acute-phase response (masks infection)
        │
        ├── Branch A ──► Failure vs pyogenic bacteria
        │                (S. pneumoniae 68%, S. aureus, P. aeruginosa)
        │                → sepsis, meningitis, abscess; severe in infancy,
        │                  improves with age
        │
        └── Branch B ──► Impaired TLR7/pDC type I IFN
                         → severe COVID-19 (OR 74.7 for mechanical ventilation)
```

**Upstream vs downstream:** the *IRAK4* mutation and Myddosome failure are the most upstream lesion; NF-κB/MAPK silencing is the proximal molecular consequence; blunted inflammation and impaired bacterial/viral containment are the downstream clinical manifestations. **GO terms:** GO:0007249 (canonical NF-κB signal transduction), GO:0002224 (Toll-like receptor signaling pathway), GO:0035325 (Toll-like receptor binding), GO:0070498 (interleukin-1-mediated signaling), GO:0045087 (innate immune response), GO:0032496 (response to lipopolysaccharide). **Relevant CHEBI:** lipopolysaccharide, lipopeptide, CpG oligodeoxynucleotide (TLR agonists whose signaling is lost).

---

## Evidence Base

| PMID | Title (abbreviated) | Evidence type | How it supports findings |
|---|---|---|---|
| [12637671](https://pubmed.ncbi.nlm.nih.gov/12637671/) | *Pyogenic bacterial infections in humans with IRAK-4 deficiency* | Human clinical + in vitro | **Founding report.** Establishes the total TIR-signaling defect (no NF-κB/MAPK, no cytokines) and the narrow-but-crucial role of the pathway. |
| [21057262](https://pubmed.ncbi.nlm.nih.gov/21057262/) | *Clinical features and outcome of patients with IRAK-4 and MyD88 deficiency* | Human clinical (n=48) | **Largest cohort.** Natural history: 68% pneumococcal, onset <2 yr in 88%, 24 deaths, weak inflammation, age-dependent improvement. |
| [32532880](https://pubmed.ncbi.nlm.nih.gov/32532880/) | *Clinical IRAK4 deficiency…* | Review + case | Defines disease as AR inborn error with blunted inflammation and narrow pyogenic susceptibility; IRAK4's vital TLR role. |
| [36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/) | *Humans with inherited MyD88 and IRAK-4 deficiencies predisposed to hypoxemic COVID-19* | Human clinical (n=22) | Extends phenotype to severe COVID-19 (OR 74.7 for ventilation) via impaired TLR7/pDC type I IFN. |
| [18669862](https://pubmed.ncbi.nlm.nih.gov/18669862/) | *Pyogenic bacterial infections in humans with MyD88 deficiency* | Human clinical + comparative | Documents the human-vs-mouse contrast: broad murine susceptibility vs narrow human phenotype improving with age. |
| [30679311](https://pubmed.ncbi.nlm.nih.gov/30679311/) | *Conformational flexibility and inhibitor binding to unphosphorylated IRAK4* | Structural | Death-domain recruitment + kinase-domain dimerization/autophosphorylation mechanism; basis for how LoF variants disrupt function. |
| [33083971](https://pubmed.ncbi.nlm.nih.gov/33083971/) | *IRAK4 Deficiency Presenting with Anti-NMDAR Encephalitis and HHV6 Reactivation* | In vitro assay + case | NF-κB reporter assay in IRAK4-null HEK293T for precise variant evaluation (functional confirmation). |
| [24596024](https://pubmed.ncbi.nlm.nih.gov/24596024/) | *Fatal pneumococcal meningitis in a 7-year-old… despite prophylaxis* | Human case | Documents standard prophylactic regimen and breakthrough fatal disease; blunted inflammation despite invasive infection. |
| [37929815](https://pubmed.ncbi.nlm.nih.gov/37929815/) | *Diagnosis of IRAK-4-deficiency by flow cytometric IκB-α degradation* | Diagnostic method | Rapid functional diagnostic assay. |
| [42103176](https://pubmed.ncbi.nlm.nih.gov/42103176/) | *Compound het IRAK4 variants: bacterial infections, brain calcification, epilepsy* | Human case + functional | Expands variant/phenotype spectrum (frameshift c.123dupA + missense c.543T>G); persistently elevated CRP variant; reduced protein and impaired TLR signaling. |
| [26472314](https://pubmed.ncbi.nlm.nih.gov/26472314/) | *IRAK-4 deficiency misdiagnosed as AD Hyper-IgE syndrome* | Human case | Illustrates diagnostic pitfalls (recurrent *S. aureus* skin infections, elevated IgE); homozygous c.877C>T p.Gln293*. |
| [38838930](https://pubmed.ncbi.nlm.nih.gov/38838930/) | *Two novel compound het LoF mutations, fatal P. aeruginosa sepsis* | Human case + functional | Splice/frameshift variants (c.942-1G>A) confirmed by minigene assay; fatal neonatal Pseudomonas sepsis. |

Additional supporting case reports document the anatomical/clinical breadth: transcranial abscess management [PMID: 25569407](https://pubmed.ncbi.nlm.nih.gov/25569407/), anti-NMDAR encephalitis with HHV6 reactivation [PMID: 33083971](https://pubmed.ncbi.nlm.nih.gov/33083971/), CNS pseudomonal vasculopathy [PMID: 39846126](https://pubmed.ncbi.nlm.nih.gov/39846126/), *Salmonella* osteomyelitis [PMID: 38857180](https://pubmed.ncbi.nlm.nih.gov/38857180/), adult fatal meningitis [PMID: 37103729](https://pubmed.ncbi.nlm.nih.gov/37103729/), and delayed adult presentation [PMID: 38758474](https://pubmed.ncbi.nlm.nih.gov/38758474/). The systems-immunology study [PMID: 25344726](https://pubmed.ncbi.nlm.nih.gov/25344726/) showed that responses to purified agonists are globally abolished but "*variable residual responses were present following exposure to whole pathogens*," identifying "*a narrow repertoire of transcriptional programs affected*" — the molecular correlate of the narrow clinical phenotype.

---

## Section-by-Section Data Compilation

### Etiology
Purely **genetic**: biallelic (homozygous or compound heterozygous) LoF mutations in *IRAK4*. No environmental cause. **Risk factor** for expression: consanguinity (increases homozygosity). Infectious exposure to encapsulated pyogenic bacteria is the trigger for clinical events but not a cause of the underlying condition. Heterozygous carriers are unaffected (gnomAD LoF tolerance). No known protective genetic modifiers are characterized; the strongest **protective factor** is increasing age (maturation of adaptive/antibody immunity). Gene-environment interaction: the genetic defect determines susceptibility, while environmental pathogen exposure and vaccination status determine timing/severity of clinical events.

### Environmental Information
No toxins, radiation, or occupational exposures are implicated. The relevant **infectious agents** are the pathogens that exploit the immune defect: *Streptococcus pneumoniae* (dominant), *Staphylococcus aureus*, *Pseudomonas aeruginosa*, *Salmonella* (osteomyelitis case), and SARS-CoV-2 (severe COVID-19). These are downstream complications, not causes.

### Temporal Development
**Onset:** congenital genetic defect; first invasive infection typically in infancy — before age 2 in 88.3%, neonatal in 32.7%. **Pattern:** episodic/recurrent invasive infections. **Progression:** highest morbidity and mortality in early childhood, with **age-dependent improvement**; invasive infections and deaths become rare after childhood. **Critical period:** the first few years of life (before protective anti-pneumococcal antibody develops) is the window of greatest vulnerability and the key window for prophylactic intervention.

### Outcome / Prognosis
Poor in infancy — 24 deaths in the 48-patient cohort, most during the first invasive episode or from invasive pneumococcal disease. Survivors have recurrent invasive infection (72%) but progressively improving prognosis with age. No formal 5-/10-year survival figures beyond cohort mortality; life expectancy approaches normal in patients who survive childhood with good prophylaxis. **Prognostic factors:** age (younger = worse), pathogen (pneumococcal worst), and access to prophylaxis/vaccination/vigilant empiric therapy.

### Treatment (NCIT-relevant interventions)
- **Antibiotic prophylaxis** — penicillin V, trimethoprim-sulfamethoxazole (NCIT: Antibiotic Therapy).
- **Immunoglobulin replacement therapy** (IVIG/SCIG; NCIT: Intravenous Immunoglobulin Therapy).
- **Pneumococcal vaccination** — PCV13 conjugate, PPSV23 polysaccharide (NCIT: Vaccine Therapy); antibody responses can be satisfactory but short-lived, requiring boosting.
- **Immediate empiric broad-spectrum antibiotics** at first sign of infection (essential given blunted signs).
- **Surgical drainage** of abscesses (e.g., transcranial abscess, [PMID: 25569407](https://pubmed.ncbi.nlm.nih.gov/25569407/)).
- **No curative pharmacotherapy; HSCT generally not indicated** (prognosis improves with age); no gene/cell therapy in clinical use.

### Prevention
**Primary:** carrier screening/genetic counseling in affected families; vaccination; prophylactic antibiotics. **Secondary:** cascade genetic testing of siblings, early diagnosis, vigilant monitoring. **Tertiary:** aggressive early treatment of infections to prevent complications. **Counseling:** autosomal recessive — 25% recurrence risk for siblings of a proband; asymptomatic carriers; prenatal/preimplantation testing feasible where the familial variants are known.

### Other Species / Model Organisms
- **Taxonomy:** disease as such is human (NCBI Taxon 9606). Orthologs: *Irak4* in mouse (NCBI Taxon 10090; Gene 266632) and rat.
- **Model organisms:** *Irak4* and *Myd88* knockout **mice** are the principal models. **Critical limitation:** murine knockouts show **broad** pathogen susceptibility, poorly recapitulating the **narrow** human phenotype [PMID: 18669862](https://pubmed.ncbi.nlm.nih.gov/18669862/) — human disease is far more restricted and improves with age. **In vitro models:** patient fibroblasts/blood cells (loss of NF-κB/MAPK response) and IRAK4-null HEK293T reporter lines for variant functional testing [PMID: 33083971](https://pubmed.ncbi.nlm.nih.gov/33083971/). This species discordance is itself a key scientific finding: it demonstrates greater redundancy of the TIR-IRAK4 pathway in humans than in mice.

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** With a prevalence <1/1,000,000 and only low-hundreds of published cases, prevalence/incidence estimates are imprecise and demographic/geographic patterns are anecdotal. No population-based registries provide robust survival curves.
2. **The narrow-phenotype paradox is incompletely explained.** Why loss of a pathway serving nearly all TLRs and IL-1R members produces such restricted susceptibility (chiefly *S. pneumoniae*) remains only partly understood; residual whole-pathogen responses [PMID: 25344726](https://pubmed.ncbi.nlm.nih.gov/25344726/) and redundancy with TLR3/TRIF and other pathways are implicated but not fully mapped.
3. **Age-dependent improvement mechanism is inferred, not proven.** The favorable evolution with age is attributed to maturing adaptive immunity/antibody, but the precise immunological switch has not been directly demonstrated.
4. **Viral susceptibility scope is still emerging.** The COVID-19 association [PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/) and scattered viral reports (HHV6 reactivation, [PMID: 33083971](https://pubmed.ncbi.nlm.nih.gov/33083971/)) suggest the antiviral phenotype (TLR7/pDC/type I IFN) is broader than the classic bacterial picture, but its full extent is undefined.
5. **No curative therapy or genotype-phenotype map.** There is no gene/cell therapy, and correlation between specific *IRAK4* alleles and severity is not established (variable expressivity noted but not systematically modeled).
6. **Model-organism discordance** limits translational research — mouse models over-predict susceptibility breadth.

---

## Proposed Follow-up Experiments / Actions

1. **Build a systematic *IRAK4* variant–function database.** Use the IRAK4-null HEK293T NF-κB reporter [PMID: 33083971](https://pubmed.ncbi.nlm.nih.gov/33083971/) and IκB-α degradation flow assay [PMID: 37929815](https://pubmed.ncbi.nlm.nih.gov/37929815/) to functionally classify all reported alleles, establishing a genotype-phenotype/severity map and ACMG-grade functional evidence.
2. **Define the antiviral phenotype prospectively.** Given the COVID-19 finding, systematically assess TLR7/pDC type I IFN responses and viral infection history across the patient population to determine whether antiviral prophylaxis/vaccination guidance should change.
3. **Dissect the narrow-phenotype paradox.** Use single-cell transcriptomics of patient immune cells challenged with whole *S. pneumoniae* vs. other pathogens to identify the MyD88-independent (e.g., TLR3/TRIF, inflammasome, complement) compensatory circuits that spare non-pneumococcal defense.
4. **Characterize the age-dependent improvement.** Longitudinal profiling of anti-pneumococcal antibody repertoire and memory B/T cell maturation in surviving patients to test whether adaptive antibody accrual explains the falling infection rate — informing when prophylaxis may be safely de-escalated.
5. **Improve model systems.** Develop humanized or organoid/iPSC-derived myeloid models that better recapitulate the human narrow phenotype than mouse knockouts, for preclinical testing of interventions.
6. **Newborn/cascade screening feasibility.** Evaluate whether a TLR-agonist functional screen or targeted sequencing of *IRAK4*/*MYD88* is cost-effective in high-consanguinity populations or in siblings of probands, given the very high early-childhood mortality that early prophylaxis could prevent.

---

## Conclusion

Immunodeficiency 67 is autosomal recessive human IRAK-4 deficiency: biallelic loss-of-function *IRAK4* mutations abolish MyD88/Myddosome-dependent TLR (all except TLR3) and IL-1-receptor-family signaling to NF-κB and MAPK, producing a narrow but life-threatening susceptibility to pyogenic bacteria — above all invasive pneumococcal disease — with characteristically blunted inflammation, early-childhood onset and high early mortality that improves markedly with age, plus an emerging risk of severe viral disease (COVID-19). Management is entirely preventive (antibiotic prophylaxis, pneumococcal/conjugate vaccination, immunoglobulin, and immediate empiric antibiotics), as no curative therapy exists.


## Artifacts

- [OpenScientist final report](Immunodeficiency_67-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_67-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007249` (2 mentions) - the report calls it "canonical NF-κB signal transduction"; GO calls it **canonical NF-kappaB signal transduction**
- `GO:0070498` (1 mention) - the report calls it "interleukin-1-mediated signaling"; GO calls it **interleukin-1-mediated signaling pathway**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Orphanet`, `NANDO`.

30 of 34 terms resolved to a current term; the rest could not be looked up either way.