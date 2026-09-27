---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T22:02:00.249369'
end_time: '2026-09-07T22:23:22.871147'
duration_seconds: 1282.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability Autosomal Recessive 65
  mondo_id: MONDO:0020850
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
citation_count: 6
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 9
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 15
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - NCBIGene
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Disability_Autosomal_Recessive_65-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Disability_Autosomal_Recessive_65-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability Autosomal Recessive 65
- **MONDO ID:** MONDO:0020850 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability Autosomal Recessive 65** covering all of the
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

# Intellectual Disability, Autosomal Recessive 65 (MRT65): A Comprehensive Disease Report

**Disease:** Intellectual disability, autosomal recessive 65 (MRT65)
**MONDO ID:** MONDO:0020850 · **OMIM:** #618109 · **Causal gene:** *KDM5B* (1q32.1)
**Category:** Mendelian, autosomal recessive neurodevelopmental disorder ("chromatinopathy")

---

## Summary

**Intellectual disability, autosomal recessive 65 (MRT65)** is an ultra-rare, autosomal-recessive neurodevelopmental disorder caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *KDM5B***, a gene on chromosome 1q32.1 encoding a histone H3K4 (tri-/di-/mono-methyl) demethylase. Because *KDM5B* is a chromatin-modifying enzyme, MRT65 belongs to the growing family of "chromatinopathies" — Mendelian disorders of the epigenetic machinery that disrupt developmental and activity-dependent gene transcription in the brain. The disorder was first delineated by Faundes and colleagues in 2018, who described "a recessive histone lysine-methylation defect caused by homozygous or compound heterozygous *KDM5B* variants and resulting in a recognizable syndrome with developmental delay, facial dysmorphism, and camptodactyly" ([PMID: 29276005](https://pubmed.ncbi.nlm.nih.gov/29276005/)).

The core clinical picture combines **global developmental delay and moderate intellectual disability**, **delayed speech and motor milestones**, **behavioral/autistic features**, **craniofacial dysmorphism** (square face, smooth philtrum, thin vermilion border, prominent nasal bridge, bulbous nose), **finger camptodactyly** (contractures of the 4th/5th proximal interphalangeal joints), and structural brain abnormalities, most notably **corpus callosum hypoplasia/partial agenesis**. Onset is neonatal to infantile. Importantly, the same gene shows a striking dosage relationship: *KDM5B* is **loss-of-function–tolerant in the general population** (gnomAD pLI ≈ 0, LOEUF 0.855), which mechanistically explains why a single pathogenic allele is generally insufficient for the full syndrome and why disease requires biallelic hits — although heterozygous protein-truncating variants are associated with modestly reduced population-level cognition.

MRT65 is **ultra-rare**: from gnomAD v4 we estimate a pathogenic-carrier frequency of roughly **1 in 570** and a theoretical random-mating birth incidence near **1 in 1.3 million** (higher in consanguineous populations). There is **no disease-specific or curative therapy**; management is entirely supportive (early developmental intervention, physical/occupational/speech therapy, and management of dysmorphism-related and systemic complications). Mouse models recapitulate cognitive and autism-like deficits and implicate dysregulation of NMDA-receptor and immediate-early/activity-dependent gene expression, providing the mechanistic bridge from H3K4-demethylase loss to the neurobehavioral phenotype.

---

## Key Findings

### Finding 1 — MRT65 is caused by biallelic loss-of-function variants in *KDM5B*

MONDO:0020850 maps unambiguously to **OMIM:618109**, DOID:0081226, and MedGen C4748219. The NCBI MedGen→Gene link resolves to **Gene ID 10765 = *KDM5B*** (lysine demethylase 5B; aliases *JARID1B*, *PLU1*, and — reflecting this disorder — "MRT65"), **HGNC:18039**, Ensembl **ENSG00000117139**, located at **chr1q32.1** (GRCh38 chr1:202,724,495–202,808,487). The disorder was first described by **Faundes et al. 2018 (Am J Hum Genet)**, who reported "a recessive histone lysine-methylation defect caused by homozygous or compound heterozygous *KDM5B* variants and resulting in a recognizable syndrome with developmental delay, facial dysmorphism, and camptodactyly" ([PMID: 29276005](https://pubmed.ncbi.nlm.nih.gov/29276005/)). A subsequent genotype/phenotype study explicitly confirmed that "bi-allelic disruptive variants (nonsense, frameshift, and splicing variants) in *KDM5B* have been identified as causative for autosomal recessive intellectual developmental disorder type 65" ([PMID: 39202393](https://pubmed.ncbi.nlm.nih.gov/39202393/)).

*KDM5B* encodes a **JmjC-domain histone H3K4 demethylase** that removes tri-, di-, and mono-methyl marks from lysine 4 of histone H3 — a key activating mark at promoters and enhancers. Its loss therefore perturbs the epigenetic control of gene transcription. **Suggested annotations:** HGNC:18039 (*KDM5B*); GO:0032453 (histone H3-K4 demethylation); GO:0006325 (chromatin organization); MONDO:0020850.

### Finding 2 — *KDM5B* is not haploinsufficient, consistent with the recessive mechanism

Population constraint data explain the recessive inheritance. gnomAD constraint for *KDM5B* (ENSG00000117139) shows **pLI ≈ 0** (7.9×10⁻³⁶), an **observed/expected LoF ratio of 0.74** (90% CI 0.65–0.86; **LOEUF 0.855**), and **missense Z = 0.53**. These metrics indicate that *KDM5B* **tolerates heterozygous loss-of-function** in the general population. A single pathogenic allele is therefore generally insufficient to cause disease, and the fully penetrant MRT65 syndrome requires **biallelic (homozygous or compound-heterozygous) LoF**. This is a clean genotype–constraint–phenotype concordance: a LoF-tolerant gene produces a recessive, not dominant, Mendelian disorder. Notably, heterozygous protein-truncating *KDM5B* variants are nonetheless associated with **modestly reduced population-level cognitive function**, indicating a subtle dosage effect below the threshold for the full syndrome.

### Finding 3 — Mouse models recapitulate cognitive/autism-like deficits and implicate NMDAR/immediate-early gene dysregulation

Two independent mouse studies bridge the molecular lesion to neurobehavior. **Kdm5b^ΔARID/ΔARID** mice (lacking demethylase activity) show **hyperactivity and hippocampus-dependent long-term memory deficits**, with **downregulated baseline and hyperactivated post-learning immediate-early/activity-dependent gene expression** (Pérez-Sisqués et al., *J Neurosci* 2024, [PMID: 38575342](https://pubmed.ncbi.nlm.nih.gov/38575342/)). This paper confirms that "the histone lysine demethylase KDM5B is implicated in recessive intellectual" disability and directly probes hippocampal memory function. A companion study reports that **KDM5B-deficient mice display autism-like phenotypes with increased NMDAR2D (Grin3b/GRIN2D) expression** (Pérez-Sisqués et al., *Sci Adv* 2026, PMID 42160407). Together these provide a mechanistic link from **H3K4me3 demethylase loss → impaired transcriptional control of synaptic/learning ("plasticity") genes → cognitive and autism-like deficits**.

**Suggested annotations:** GO:0007613 (memory); GO:0007611 (learning or memory); GO:0050804 (modulation of chemical synaptic transmission); NMDA receptor complex components (GRIN2D/GRIN3B).

### Finding 4 — ClinVar documents a predominantly truncating biallelic variant spectrum (NM_006618.5)

ClinVar (accessed 2026) contains **590 total *KDM5B* variant records**, of which **219 are classified pathogenic/likely-pathogenic** and **98 are explicitly linked to "Intellectual disability, autosomal recessive 65."** The pathogenic spectrum is dominated by **protein-truncating variants**. Representative pathogenic/likely-pathogenic alleles (reference transcript **NM_006618.5**) include:

| Variant (cDNA) | Protein consequence | Class |
|---|---|---|
| c.394C>T | p.(Gln132Ter) | Nonsense |
| c.1457G>A | p.(Trp486Ter) | Nonsense |
| c.2345T>G | p.(Leu782Ter) | Nonsense |
| c.4198C>T | p.(Arg1400Ter) | Nonsense |
| c.2049_2050insA | p.(Leu684fs) | Frameshift |
| c.3151del | p.(Val1051fs) | Frameshift |
| c.2401_2405del | p.(Arg801fs) | Frameshift |
| c.1612G>C | p.(Ala538Pro) | Missense (typically VUS) |

Most pathogenic alleles are **nonsense, frameshift, or splice-site** (predicted to trigger nonsense-mediated decay or produce non-functional protein). **Missense variants are generally classified as variants of uncertain significance (VUS)** under ACMG/AMP criteria, reflecting the loss-of-function mechanism where truncation is more confidently deleterious than single amino-acid substitutions.

### Finding 5 — *Kdm5b*-null mice show lethality/growth/neurological phenotypes; no MRT65-specific trials exist

IMPC genotype–phenotype data for mouse *Kdm5b* (NCBI Gene 75605) homozygous nulls show **preweaning lethality with incomplete penetrance**, **decreased body length** (growth/size phenotype), and **absent pinna reflex** (neurological/behavioral phenotype) — a constellation consistent with an essential developmental regulator. A ClinicalTrials.gov API query (2026) returned **no interventional trials for MRT65/KDM5B intellectual disability**; *KDM5B* appears only in observational autism/genetics registries (e.g., Simons SPARK, NCT01238250). Small-molecule **KDM5B inhibitors exist but only in oncology contexts** (e.g., PMID 42324589) and are **mechanistically inappropriate** for a loss-of-function disorder — inhibiting an already-lost enzyme cannot restore function. Consequently, MRT65 management remains **entirely supportive**.

### Finding 6 — HPO annotations define the full, frequency-tagged phenotype spectrum

The HPO disease annotation for **OMIM:618109** (gene *KDM5B*/NCBIGene:10765; autosomal recessive; source PMID:29276005) comprises **37 terms**, with frequencies expressed as *n*/3 biallelic individuals from the original cohort. The phenotype spectrum:

| Domain | Phenotype (HPO term) | Frequency (original cohort) |
|---|---|---|
| Neurodevelopment | Intellectual disability, moderate (HP:0002342) | Core feature |
| | Global developmental delay (HP:0001263) | Moderate 2/3, severe 1/3 |
| | Delayed speech and language development (HP:0000750) | Frequent |
| | Delayed ability to walk (HP:0031936) | Frequent |
| | Gait ataxia / unsteady gait (HP:0002066) | Present |
| | Aggressive behavior (HP:0000718) | 1/3 |
| Brain MRI | Hypoplasia of the corpus callosum (HP:0002079) | Present |
| | Partial agenesis of the corpus callosum (HP:0001338) | 1/3 |
| Craniofacial | Square face (HP:0000321) | 2/3 |
| | Smooth philtrum, thin vermilion border, prominent nasal bridge, bulbous nose, downslanted palpebral fissures, dolichocephaly, prominent metopic ridge | Variable |
| Digits | Camptodactyly of 4th/5th fingers, PIP-joint contractures (HP:0009276 / HP:0009185) | Characteristic |
| Eyes | Myopia (HP:0000545) | 2/3 |
| | Astigmatism, ptosis, strabismus | Variable |
| Other | Feeding difficulties (HP:0011968) | 2/3 |
| | Cryptorchidism, hypospadias, inguinal hernia, supernumerary nipple, secundum atrial septal defect, abnormal pinna | Individual cases |

**Onset:** neonatal in 2/3 and infantile in 1/3.

### Finding 7 — Carrier frequency ~1 in 570; theoretical birth incidence ~1 in 1.3 million

Using gnomAD v4 (8,525 *KDM5B* variants), high-confidence (**LOFTEE HC**) rare (allele frequency <0.1%) predicted loss-of-function alleles across **411 sites** sum to a pathogenic allele frequency **q ≈ 8.8×10⁻⁴**. This gives:

- **Carrier frequency 2q ≈ 0.0018 (≈ 1 in 567)**
- **Theoretical random-mating homozygous/compound-heterozygous birth incidence q² ≈ 7.8×10⁻⁷ (≈ 1 in 1.3 million)**

A methodological caveat surfaced during this estimate: the single common "LoF"-annotated allele (a frameshift at AF 0.185) is **LOFTEE low-confidence (LC)** — i.e., not a true LoF. Its naive inclusion inflated the estimate ~100-fold, underscoring the necessity of **LOFTEE/quality filtering** for constraint- and incidence-based calculations. The true incidence will be **substantially higher in consanguineous populations**, where autosomal-recessive disorders are enriched.

---

## Mechanistic Model / Interpretation

MRT65 is best understood as a **transcriptional/epigenetic disorder of neurodevelopment**. The causal chain runs from an epigenetic enzyme defect to dysregulated activity-dependent gene programs to the clinical phenotype:

```
1.  Biallelic LoF variants in KDM5B (nonsense / frameshift / splice)
        │  leads to
        ▼
2.  Nonsense-mediated decay / truncated non-functional protein
        │  results in
        ▼
3.  Loss of H3K4me3/me2/me1 demethylase activity (JmjC + ARID domains)
        │  leads to
        ▼
4.  Aberrant H3K4-methylation landscape at promoters/enhancers
        │  results in
        ▼
5.  Dysregulated developmental + activity-dependent transcription
        │  (immediate-early genes down at baseline, hyperactivated post-learning;
        │   NMDAR subunit GRIN2D/GRIN3B up — shown in mouse)   [model organism]
        ├─────────────► Brain: impaired synaptic plasticity / hippocampal memory
        │                        └► intellectual disability, developmental delay,
        │                           autistic/behavioral features, gait ataxia
        ├─────────────► Neuroanatomy: corpus callosum hypoplasia / partial agenesis
        ├─────────────► Craniofacial morphogenesis → dysmorphism
        └─────────────► Limb/digit development → camptodactyly (4th/5th PIP contractures)
```

**Upstream vs downstream.** The **upstream initiating lesion** is the *KDM5B* biallelic LoF genotype; the **proximate molecular consequence** is loss of H3K4 demethylase activity and a shifted chromatin state; the **downstream** manifestations are the transcriptional dysregulation of neuronal plasticity and developmental genes and the multi-organ developmental phenotype. The mouse data (Finding 3) provide the strongest mechanistic evidence for the neuronal branch — linking demethylase loss to **immediate-early gene** and **NMDA-receptor** dysregulation and hippocampus-dependent memory deficits — but the craniofacial, callosal, and digit branches are currently inferred from human phenotype–genotype correlation rather than demonstrated mechanistically.

**Cell types and processes.** The affected biological processes center on **chromatin organization (GO:0006325)**, **histone H3-K4 demethylation (GO:0032453)**, and **learning/memory (GO:0007611, GO:0007613)**. Implicated cell types are principally **neurons (CL:0000540)**, including **hippocampal/glutamatergic neurons**, with subcellular localization in the **nucleus (GO:0005634)** and **chromatin (GO:0000785)**, consistent with a nuclear chromatin-modifying enzyme.

**Why recessive.** Finding 2 ties the genetics together: because *KDM5B* is LoF-tolerant (pLI ≈ 0, LOEUF 0.855), one functional allele suffices for near-normal development, so only biallelic loss crosses the disease threshold — a textbook example of constraint metrics predicting inheritance mode.

---

## Section-by-Section Detail

### 1. Disease Information
MRT65 is an ultra-rare autosomal-recessive neurodevelopmental chromatinopathy. **Identifiers:** MONDO:0020850; OMIM #618109; DOID:0081226; MedGen C4748219. **Synonyms:** "Intellectual developmental disorder, autosomal recessive 65"; "MRT65." Dedicated ICD-10/ICD-11 and MeSH codes are not specifically assigned; it falls under generic intellectual-disability rubrics. Information is derived from **aggregated disease-level resources** (OMIM, HPO, ClinVar) and **small published patient cohorts** (originally 3 families/biallelic individuals), not from large EHR datasets.

### 2. Etiology
**Primary cause:** genetic — biallelic loss-of-function variants in *KDM5B*. **Genetic risk factors:** homozygous or compound-heterozygous LoF alleles; **consanguinity** substantially increases risk (as for all AR disorders). No established **environmental risk or protective factors** and no infectious etiology. **Genetic protective/modifier factors:** none specifically characterized; the residual function of hypomorphic (e.g., some missense) alleles may modulate severity, and heterozygous carriers show only subclinical cognitive effects. **Gene–environment interactions:** none documented.

### 3. Phenotypes
See Finding 6 table. Phenotype **types** span clinical signs (dysmorphism, camptodactyly), neurodevelopmental/behavioral changes (ID, autism features, aggression), and structural findings (corpus callosum anomalies on MRI). **Onset** is neonatal-to-infantile; **severity** is typically moderate for ID with variable expressivity; **course** is stable/non-progressive (a developmental, not neurodegenerative, disorder). **Quality-of-life impact** is dominated by lifelong intellectual disability, communication limitations, and dependency in daily functioning; formal QoL instrument data specific to MRT65 are not available.

### 4. Genetic / Molecular Information
**Causal gene:** *KDM5B* (HGNC:18039; gene MIM *605393; Ensembl ENSG00000117139). **Variant classes:** predominantly nonsense, frameshift, and splice-site (pathogenic/likely-pathogenic); missense generally VUS (Finding 4). **Reference transcript:** NM_006618.5. **Population frequency:** pathogenic LoF alleles are individually rare (AF <0.1%). **Origin:** germline (no somatic disease role). **Functional consequence:** loss of function (haploinsufficiency tolerated; disease requires biallelic loss). **Epigenetic dimension:** the disorder is itself an epigenetic-machinery defect — loss of a histone H3K4 demethylase alters the genome-wide methylation landscape rather than acting through a single-locus methylation change. **Chromosomal abnormalities:** none characteristic; diagnosis is at the sequence-variant level.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are implicated. MRT65 is a monogenic Mendelian disorder.

### 6. Mechanism / Pathophysiology
See the causal-chain diagram above and Findings 1–3. Molecular pathway: **chromatin/H3K4-methylation regulation**; downstream, **NMDAR signaling and immediate-early gene programs** (model-organism evidence). No metabolic, immune, or classic tissue-injury (oxidative/ischemic/fibrotic) mechanisms are involved; the pathology is developmental/transcriptional.

### 7. Anatomical Structures Affected
**Primary organ/system:** central nervous system (**brain**, UBERON:0000955; nervous system, UBERON:0001016), with **corpus callosum** (UBERON:0002336) hypoplasia/partial agenesis. **Secondary/associated:** craniofacial skeleton (dysmorphism), digits/hands (camptodactyly), eyes (myopia, astigmatism, ptosis, strabismus), genitourinary (cryptorchidism, hypospadias, inguinal hernia), and heart (secundum atrial septal defect) in individual cases. **Cell type:** neurons (CL:0000540). **Subcellular:** nucleus/chromatin (GO:0005634 / GO:0000785). **Lateralization:** brain findings are midline (callosal); other features generally bilateral.

### 8. Temporal Development
**Onset:** congenital/neonatal (2/3) to infantile (1/3). **Pattern:** chronic, static developmental disorder — non-progressive and lifelong. There are no remission patterns; the **critical window** for intervention is early childhood developmental support.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** high/complete for biallelic LoF (based on limited cohorts). **Expressivity:** variable (severity and non-neurological features differ between individuals). **Carrier frequency:** ≈ 1 in 570; **theoretical birth incidence:** ≈ 1 in 1.3 million under random mating (Finding 7), higher with consanguinity. No anticipation (not a repeat-expansion disorder). **Founder effects/geographic clustering:** none established, though consanguineous populations are enriched. **Sex ratio:** no strong skew expected (autosomal); some reported features (cryptorchidism/hypospadias) are male-specific.

### 10. Diagnostics
**Genetic testing is diagnostic.** Recommended approach: **exome or genome sequencing** (often as an intellectual-disability/neurodevelopmental gene panel of 1,000+ genes), which detects the causative biallelic SNV/indels. Long-read genome sequencing can add value for phasing biallelic variants in autosomal-recessive genes and resolving structural/complex variants ([PMID: 41514368](https://pubmed.ncbi.nlm.nih.gov/41514368/)). **Confirmation:** ClinVar-referenced pathogenic classification and parental segregation (trans configuration for compound heterozygotes). **Supportive workup:** brain MRI (corpus callosum assessment), ophthalmologic exam, developmental/cognitive assessment. **No specific biochemical biomarker** exists. **Differential diagnosis:** other chromatinopathies and ID syndromes — notably *KDM4B*-related disorders (autosomal dominant IDD from heterozygous *KDM4B* LoF, and a reported biallelic *KDM4B* case) which share developmental delay, brain anomalies, and digital findings ([PMID: 37526414](https://pubmed.ncbi.nlm.nih.gov/37526414/)); metabolic ID mimics should be excluded when biochemical clues are present.

### 11. Outcome / Prognosis
MRT65 is a **non-lethal, non-progressive** developmental disorder in humans (contrast with murine preweaning lethality, Finding 5). **Life expectancy** is not established but is not intrinsically shortened by the neurodevelopmental phenotype; systemic malformations (e.g., cardiac septal defect) may modify individual prognosis. **Morbidity** is dominated by lifelong intellectual disability and dependency. No prognostic biomarkers are defined; residual gene function (hypomorphic alleles) is the plausible principal modifier of severity.

### 12. Treatment
**No disease-specific or curative therapy exists** (Finding 5). Management is **supportive and rehabilitative**: early developmental intervention, special education, **physical, occupational, and speech therapy**, management of behavioral features, ophthalmologic correction (refractive error), orthopedic/hand management of camptodactyly, and surgical correction of associated malformations (cryptorchidism, hernia, ASD) as indicated. **KDM5B small-molecule inhibitors** developed for oncology are **contraindicated in concept** for a loss-of-function disorder. No pharmacogenomic or gene/RNA-based therapies are available. Suggested NCIT-type intervention categories: rehabilitation therapy, occupational therapy, speech/language therapy, supportive care.

### 13. Prevention
No primary prevention beyond **genetic counseling** and **reproductive options** for at-risk (e.g., consanguineous or carrier) couples: **carrier testing, prenatal diagnosis, and preimplantation genetic testing** are applicable once familial variants are known. There is no vaccine, no environmental intervention, and no population newborn-screening test for MRT65. **Cascade carrier testing** in families is appropriate after a proband is identified.

### 14. Other Species / Natural Disease
**Orthologue:** mouse *Kdm5b* (NCBI Gene 75605). No naturally occurring companion-animal/wildlife disease is catalogued for *KDM5B* (no OMIA entry noted). The gene and its H3K4-demethylase function are **evolutionarily conserved**, supporting cross-species mechanistic study. No zoonotic dimension (non-infectious disorder).

### 15. Model Organisms
The principal model is the **mouse**. Informative genetic models: (1) **Kdm5b^ΔARID/ΔARID** (demethylase-dead) mice recapitulate hyperactivity, hippocampal memory deficits, and activity-dependent/immediate-early gene dysregulation ([PMID: 38575342](https://pubmed.ncbi.nlm.nih.gov/38575342/)); (2) **KDM5B-deficient mice** with autism-like phenotypes and increased NMDAR (GRIN2D/GRIN3B) expression (*Sci Adv* 2026, PMID 42160407); and (3) **IMPC Kdm5b-null** mice with preweaning lethality (incomplete penetrance), reduced body length, and absent pinna reflex (Finding 5). **Phenotype recapitulation:** strong for the cognitive/behavioral axis. **Limitations:** homozygous-null lethality in mice exceeds the human phenotype, so demethylase-dead/conditional models better model the viable human disorder. Resources: MGI, IMPC.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [29276005](https://pubmed.ncbi.nlm.nih.gov/29276005/) | Recessive H3K4-methylation defect / KDM5B syndrome (Faundes et al., 2018) | Human clinical | **Foundational** — defines MRT65 and its causal biallelic KDM5B mechanism and core triad (DD, dysmorphism, camptodactyly); source of HPO annotations |
| [39202393](https://pubmed.ncbi.nlm.nih.gov/39202393/) | Genotype/phenotype study of KDM5B | Human clinical | Confirms biallelic disruptive (nonsense/frameshift/splice) KDM5B variants cause AR IDD type 65 |
| [38575342](https://pubmed.ncbi.nlm.nih.gov/38575342/) | Kdm5b and hippocampal memory (Pérez-Sisqués et al., J Neurosci 2024) | Model organism (mouse) | Links demethylase loss to memory deficits and immediate-early/activity-dependent gene dysregulation |
| PMID 42160407 | KDM5B-deficient mice, autism-like, NMDAR2D up (Sci Adv 2026) | Model organism (mouse) | Extends mechanism to NMDAR (GRIN2D/GRIN3B) and autism-like phenotype |
| [37526414](https://pubmed.ncbi.nlm.nih.gov/37526414/) | Biallelic KDM4B frameshift phenotype | Human clinical | **Differential diagnosis** — related histone-demethylase (KDM4B) chromatinopathy; distinguishes from KDM5B |
| [41514368](https://pubmed.ncbi.nlm.nih.gov/41514368/) | Long-read GS in pediatric neurological disorders | Human diagnostics | Supports genome sequencing (incl. phasing biallelic AR variants) as first-line diagnostic |
| [40088508](https://pubmed.ncbi.nlm.nih.gov/40088508/) | Genetic epilepsies, consanguinity, India | Human epidemiology | Contextual — AR disorders enriched under consanguinity; WES diagnostic yield |

Data resources underpinning the quantitative findings: **OMIM/MONDO/MedGen** (identifier mapping), **ClinVar** (variant spectrum, Finding 4), **gnomAD v4** (constraint and carrier/incidence, Findings 2 & 7), **HPO** (phenotype annotation, Finding 6), **IMPC** and **ClinicalTrials.gov API** (mouse phenotypes and trial landscape, Finding 5).

---

## Limitations and Knowledge Gaps

1. **Small human cohort.** The HPO frequencies derive from only **3 biallelic individuals** in the original report; frequencies (n/3) are imprecise and the full phenotypic range is likely broader than currently annotated. The 2024 genotype/phenotype study (PMID 39202393) expands this, but MRT65 remains defined by tens, not hundreds, of patients.
2. **Mechanistic branches inferred, not proven.** The neuronal branch (memory, NMDAR, immediate-early genes) is supported by mouse data; the **craniofacial, corpus callosum, and digit** branches remain **genotype–phenotype correlations** without direct mechanistic demonstration.
3. **Genotype–phenotype correlation.** It is not yet clear whether missense/hypomorphic alleles produce milder disease than complete truncation; missense variants are largely VUS.
4. **Incidence estimate is theoretical.** The 1-in-1.3-million figure assumes random mating and complete penetrance; real incidence is unknown and higher in consanguineous populations. No formal prevalence study exists.
5. **Model organism discordance.** Mouse homozygous nulls are preweaning-lethal, unlike viable human patients — limiting the null model and favoring demethylase-dead/conditional models.
6. **No natural-history, QoL, or long-term outcome data**, and **no biomarker** for diagnosis or prognosis.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate a larger patient registry** (GeneMatcher/MatchmakerExchange) to refine phenotype frequencies, expressivity, and genotype–phenotype correlations (truncating vs missense).
2. **Functional characterization of missense VUS** — demethylase activity assays and H3K4me3 ChIP in patient/edited cells to reclassify VUS under ACMG PS3/BS3 evidence.
3. **Patient-derived iPSC neurons/organoids** to test whether human neurons reproduce the murine immediate-early/NMDAR transcriptional dysregulation and to map the affected gene programs (analogous iPSC modeling has proven informative in other AR neuro disorders, e.g., [PMID: 39617394](https://pubmed.ncbi.nlm.nih.gov/39617394/)).
4. **Conditional/demethylase-dead brain-region-specific mouse models** with staged (developmental vs adult) inactivation to define critical windows and test reversibility.
5. **Epigenomic profiling (H3K4me3 CUT&RUN/ChIP-seq, RNA-seq)** across neuronal, craniofacial, and limb-bud lineages to test the non-neuronal mechanistic branches.
6. **Refine carrier-frequency and incidence estimates** using targeted, LOFTEE-filtered analyses across ancestrally diverse and consanguineous cohorts.
7. **Standardize supportive-care guidance** (developmental intervention, ophthalmology, orthopedics, cardiology) into a GeneReviews-style clinical management outline.

---

*Report compiled from a 5-iteration autonomous investigation integrating OMIM/MONDO/MedGen mapping, ClinVar, gnomAD v4, HPO, IMPC, ClinicalTrials.gov, and primary literature. Evidence types are labeled human clinical, model organism, or computational throughout.*


## Artifacts

- [OpenScientist final report](Intellectual_Disability_Autosomal_Recessive_65-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Disability_Autosomal_Recessive_65-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 17 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0032453` (2 mentions) - the report calls it "histone H3-K4 demethylation"; GO calls it **histone H3K4 demethylase activity**, and lists "histone H3-K4 demethylase activity" among its other names
- `HP:0002066` (1 mention) - the report calls it "Gait ataxia / unsteady gait"; HP calls it **Gait ataxia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `NCBIGene`.

26 of 29 terms resolved to a current term; the rest could not be looked up either way.