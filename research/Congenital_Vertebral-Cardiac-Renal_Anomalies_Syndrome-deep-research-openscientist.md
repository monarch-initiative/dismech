---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T07:14:26.117584'
end_time: '2026-09-03T07:44:47.972693'
duration_seconds: 1821.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Vertebral-Cardiac-Renal Anomalies Syndrome
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
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
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 9
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 9
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0043420
    ontology_label: obsolete anthranilate metabolic process
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Vertebral-Cardiac-Renal_Anomalies_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Vertebral-Cardiac-Renal_Anomalies_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Vertebral-Cardiac-Renal Anomalies Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Vertebral-Cardiac-Renal Anomalies Syndrome** covering all of the
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

# Congenital Vertebral-Cardiac-Renal Anomalies Syndrome — Comprehensive Disease Report

*Disease knowledge base entry — Mendelian congenital malformation syndrome*

---

## Summary

**"Congenital Vertebral-Cardiac-Renal Anomalies Syndrome" is Congenital NAD Deficiency Disorder (CNDD)**, also catalogued as **Vertebral, Cardiac, Renal and Limb Defects Syndrome (VCRL)**. It is an autosomal-recessive inborn error of *de novo* nicotinamide adenine dinucleotide (NAD) biosynthesis. The disorder is caused by biallelic loss-of-function variants in one of three genes encoding sequential enzymes of the kynurenine (tryptophan → NAD) pathway: **HAAO** (3-hydroxyanthranilate 3,4-dioxygenase; VCRL1, OMIM #617660), **KYNU** (kynureninase; VCRL2, OMIM #617661), and **NADSYN1** (NAD synthetase 1; VCRL3, OMIM #618845). The unifying biochemical lesion is a deficiency of NAD during embryogenesis, which disrupts organogenesis of the vertebrae, heart, kidneys and limbs, producing a phenotype that overlaps heavily with the **VACTERL/VATER association**.

The mechanistic story of this disorder is unusually complete for a rare Mendelian condition, and it is remarkable for one reason: **the malformations are, in principle, preventable**. In *Haao*-null and *Kynu*-null mouse embryos, defects mirroring those of patients arise directly from NAD deficiency, and gestational supplementation with niacin/nicotinamide (NAD precursors) prevents them. The causal network extends beyond the three core enzymes: environmental NAD deprivation (maternal dietary vitamin B3/tryptophan restriction, hypoxia) and maternal modifier genotypes — notably heterozygosity for the tryptophan transporter gene **SLC6A19** (B0AT1) — can independently lower embryonic NAD and reproduce the malformation spectrum, establishing a genuine maternal–fetal, gene–environment axis.

The syndrome shows **variable expressivity**. The classic severe presentation (HAAO/KYNU) includes renal anomalies and can be lethal, but NADSYN1-associated CNDD can spare the kidneys and limbs, fail to meet formal VACTERL criteria, and be compatible with survival into adulthood. Because each causal gene occupies a distinct enzymatic step, patients carry gene-specific plasma metabolite signatures (accumulation of the substrate upstream of the blocked enzyme with low downstream NAD), which offers a functional-biochemical diagnostic strategy complementing genomic sequencing. This report consolidates the identity, etiology, phenotypes, molecular genetics, mechanism, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, and model-organism evidence for the disorder.

---

## 1. Disease Information

**Overview.** Congenital NAD Deficiency Disorder (CNDD) / VCRL is a multiple-congenital-malformation syndrome resulting from insufficient NAD during embryonic development. NAD is an essential redox cofactor and signaling substrate; when its synthesis is impaired during organogenesis, multiple organ systems that require high NAD flux — the developing axial skeleton, heart, kidney/urinary tract and limbs — form abnormally. Clinically the disorder presents within the **VACTERL/VATER spectrum** (Vertebral defects, Anal atresia, Cardiac defects, Tracheo-Esophageal fistula, Renal anomalies, Limb abnormalities), and CNDD should be considered a molecularly-defined, recessive cause of VACTERL-like presentations.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Disease term | Congenital NAD Deficiency Disorder (CNDD) |
| Synonym | Vertebral, Cardiac, Renal and Limb Defects Syndrome (VCRL) |
| OMIM (HAAO) | VCRL1 #617660 |
| OMIM (KYNU) | VCRL2 #617661 |
| OMIM (NADSYN1) | VCRL3 #618845 |
| MONDO | *Not assigned in the provided evidence; map to the VCRL/CNDD grouping when available* |
| Category | Mendelian, autosomal recessive |

**Synonyms / alternative names:** Congenital NAD Deficiency Disorder; VCRL syndrome; Vertebral, Cardiac, Renal and Limb Defects Syndrome; VACTERL-like NAD-deficiency malformation syndrome. The term "Congenital Vertebral-Cardiac-Renal Anomalies Syndrome" used in the research template is a descriptive alias for this entity.

**Information source.** The evidence base is a mixture of **individual patient reports/case series** (human clinical genetics) and **aggregated disease-level resources** (OMIM gene-disease designations), supplemented heavily by **model-organism (mouse) experiments** that establish causality.

> Supporting evidence — *NAD Deficiency, Congenital Malformations, and Niacin Supplementation* [PMID: 28792876](https://pubmed.ncbi.nlm.nih.gov/28792876/): "Variants were identified in two genes that encode enzymes of the kynurenine pathway, 3-hydroxyanthranilic acid 3,4-dioxygenase (HAAO) and kynureninase (KYNU)."
>
> *New cases that expand the genotypic and phenotypic spectrum of Congenital NAD Deficiency Disorder* [PMID: 33942433](https://pubmed.ncbi.nlm.nih.gov/33942433/): "Biallelic, inactivating variants in three genes encoding enzymes of this biosynthesis pathway (KYNU, HAAO, and NADSYN1) disrupt NAD synthesis and have been identified in patients with multiple malformations of the heart, kidney, vertebrae, and limbs; these patients have Congenital NAD Deficiency Disorder."

---

## 2. Etiology

**Primary causal factors — genetic.** CNDD is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants** in HAAO, KYNU, or NADSYN1. The foundational study identified homozygous **HAAO p.D162\*** and **HAAO p.W186\***, **KYNU p.V57Efs\*21**, and compound-heterozygous **KYNU p.Y156\*/p.F349Kfs\*4**; the encoded enzymes had greatly reduced *in vitro* activity, and patients had reduced circulating NAD [PMID: 28792876]. Subsequent work added **NADSYN1** as the third causal gene [PMID: 33942433].

**Primary causal factor — biochemical.** The convergent mechanism is **NAD deficiency during embryogenesis**. Whether the block is upstream (KYNU, HAAO) or terminal (NADSYN1), the result is inadequate NAD for the metabolic demands of organogenesis.

**Genetic risk factors.** Causal variants are the three-gene set above. **Maternal modifier genotype** is an additional risk axis: maternal heterozygosity for **SLC6A19** (B0AT1, the neutral amino-acid/tryptophan transporter) can precipitate CNDD in offspring when NAD precursor supply is limited [PMID: 36374036].

**Environmental risk factors.** NAD deficiency of **environmental origin** — maternal dietary deficiency of vitamin B3 (niacin) and/or tryptophan, and **hypoxia** — causes congenital malformations and miscarriage in mice [PMID: 32015132]. These act on the same NAD-supply bottleneck as the genetic lesions.

**Protective factors.** The dominant protective factor is **adequate maternal dietary NAD precursor supply** (niacin/nicotinamide, dietary tryptophan). In genetic mouse models, precursor supplementation prevents the malformations [PMID: 28792876]. No specific protective human genetic alleles are established in the provided evidence.

**Gene–environment interaction.** CNDD is a paradigm of gene–environment interaction: a partially compromised genetic NAD-synthesis capacity (e.g., maternal *Slc6a19* heterozygosity, or hypomorphic pathway alleles) becomes pathogenic only when environmental precursor supply is insufficient. "NAD deficiency due to environmental factors or gene-environment interactions causes congenital malformations and miscarriage in mice" [PMID: 32015132].

> Supporting evidence — [PMID: 36374036](https://pubmed.ncbi.nlm.nih.gov/36374036/): "This perturbed the NAD metabolome in pregnant Slc6a19+/- females, resulting in reduced NAD levels and increased rates of embryo loss." … "They also suggest that human female carriers of a SLC6A19 loss-of-function allele might be susceptible to adverse pregnancy outcomes unless sufficient NAD precursor amounts are available during gestation."

---

## 3. Phenotypes

CNDD is a **multiple-malformation syndrome** with a core tetrad of **vertebral, cardiac, renal, and limb** anomalies and additional craniofacial and developmental features. Phenotypes are **congenital (present at birth)** and represent fixed structural malformations (physical manifestations / clinical signs), not progressive or episodic symptoms; developmental delay is an additional feature in survivors. Severity is **variable**, ranging from prenatal/neonatal lethality to adult survival.

| Phenotype | Type | Onset | Frequency / notes | Suggested HPO |
|---|---|---|---|---|
| Vertebral segmentation defects (hemivertebrae, spinal segmentation anomalies) | Skeletal malformation | Congenital | Core feature; present across genes | HP:0000925 (Abnormality of the vertebral column); HP:0008438 (Abnormal vertebral segmentation) |
| Rib anomalies | Skeletal malformation | Congenital | Reported (e.g., adult NADSYN1 case) | HP:0000772 (Abnormal rib morphology) |
| Congenital heart defects (incl. HLHS, aortic coarctation, transverse aortic arch hypoplasia, bicuspid aortic valve stenosis) | Cardiovascular malformation | Congenital | Core feature; severe lesions reported with NADSYN1 | HP:0001627 (Abnormal heart morphology); HP:0004421 (VSD); HP:0004383 (Hypoplastic left heart) |
| Renal / urinary tract anomalies | Genitourinary malformation | Congenital | Core in HAAO/KYNU; **spared** in some NADSYN1 cases | HP:0000077 (Abnormality of the kidney); HP:0000107 (Renal cyst) |
| Limb anomalies (incl. unequal leg length) | Skeletal malformation | Congenital | Core in classic cases; may be absent in NADSYN1 | HP:0002813 (Abnormality of limb bone morphology) |
| Cleft palate | Craniofacial malformation | Congenital | Reported in NADSYN1 | HP:0000175 (Cleft palate) |
| Ptosis | Craniofacial/ocular | Congenital | Reported in adult NADSYN1 | HP:0000508 (Ptosis) |
| Developmental delay | Neurodevelopmental | Childhood | In some surviving patients | HP:0001263 (Global developmental delay) |
| Reduced circulating NAD | Laboratory abnormality | Congenital/lifelong | Biochemical hallmark | — |

**Quality-of-life impact.** Depends on organ severity: severe cardiac and renal malformations drive early morbidity/mortality and require major surgical intervention; skeletal defects cause chronic orthopedic disability (e.g., unequal leg length, spinal deformity); developmental delay affects long-term function. Formal EQ-5D/SF-36 data are not available for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal genes (three-gene locus heterogeneity).**

| Gene | Protein / enzyme | Pathway step | OMIM disease | Representative variants |
|---|---|---|---|---|
| **HAAO** | 3-hydroxyanthranilate 3,4-dioxygenase | 3-HAA → ACMS (upstream) | VCRL1 #617660 | p.D162\*, p.W186\* (homozygous nonsense); homozygous exon-5 deletion reported |
| **KYNU** | Kynureninase | 3-hydroxykynurenine → 3-HAA (upstream) | VCRL2 #617661 | p.V57Efs\*21 (homozygous); p.Y156\*/p.F349Kfs\*4 (compound het) |
| **NADSYN1** | NAD synthetase 1 | NaAD → NAD, terminal amidation (downstream) | VCRL3 #618845 | c.1717G>A p.Ala573Thr (homozygous, adult case); compound-het variants in cardiac/vertebral cases |

**Variant classification & type.** Reported variants are predominantly **nonsense, frameshift, and structural (whole-exon deletion)** loss-of-function alleles, classified pathogenic/likely pathogenic under ACMG/AMP criteria (null variants in genes with an established LoF mechanism, functionally validated by reduced enzyme activity). At least one **missense** allele (NADSYN1 p.Ala573Thr) is associated with a milder, adult-surviving phenotype.

**Functional consequence.** **Loss of function** — reduced or abolished enzyme activity impairing *de novo* NAD synthesis. The foundational study confirmed "greatly reduced" activity by *in vitro* enzyme assays [PMID: 28792876].

**Allele frequency / origin.** Pathogenic alleles are rare; the disorder is recessive and consanguinity-associated (homozygous null alleles). All reported disease variants are **germline**; there is no somatic component.

**Modifier genes.** **SLC6A19** (maternal B0AT1 tryptophan transporter) acts as a maternal modifier/risk gene by limiting substrate for the tryptophan→NAD pathway [PMID: 36374036]. Additional NAD-pathway and transporter genes are plausible modifiers.

**Epigenetic / chromosomal information.** No specific disease-defining epigenetic signature or recurrent chromosomal abnormality is established. One reported HAAO lesion is a **homozygous exon-5 deletion**, detectable by copy-number/structural methods.

---

## 5. Environmental Information

- **Environmental factors:** Maternal **hypoxia** and dietary **vitamin B3 (niacin) / tryptophan deficiency** lower embryonic NAD and cause malformations and miscarriage in mice [PMID: 32015132]. These environmental insults phenocopy the genetic disorder.
- **Lifestyle factors:** Maternal nutrition during pregnancy — adequacy of niacin and tryptophan intake — is the key modifiable lifestyle determinant.
- **Infectious agents:** Not applicable. CNDD is not an infectious disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **biallelic loss-of-function variant** in HAAO, KYNU, or NADSYN1 (or a maternal modifier such as *SLC6A19* heterozygosity, and/or environmental precursor deprivation) **reduces the activity of a kynurenine-pathway enzyme** → **leads to** a block in *de novo* NAD biosynthesis.
2. The enzymatic block **results in accumulation of the upstream substrate** (gene-specific) **and a fall in downstream NAD**.
3. Reduced availability of maternal-fetal NAD precursors **compounds the deficit** (branch: the environmental/gene–environment route can initiate the same lesion independently of the three core genes).
4. **NAD deficiency in the embryo** during the critical window of organogenesis **results in** impaired NAD-dependent cellular processes (redox metabolism, ADP-ribosylation/PARP signaling, sirtuin activity) — *the precise downstream molecular effectors in affected tissues are inferred rather than fully demonstrated*.
5. Impaired NAD-dependent processes in progenitor tissues **disrupt normal morphogenesis** of the somites/vertebrae, cardiac outflow and chambers, nephrogenic mesenchyme, and limb buds → **leads to** the structural malformations.
6. The malformations **manifest clinically** as vertebral segmentation defects, congenital heart disease, renal/urinary anomalies, and limb defects (with variable craniofacial involvement) — and, when NAD deficiency is severe, **result in** embryo loss/miscarriage.

```
LoF variant (HAAO / KYNU / NADSYN1)      Maternal SLC6A19+/-  +  low niacin/Trp  or  hypoxia
        |                                             |
        v                                             v
  Block in de novo NAD synthesis  <-------------------+
        |
        v
  Upstream substrate accumulates  +  NAD pool falls
        |
        v
  NAD-dependent processes impaired in embryo (inferred effectors)
        |
        +--> Somite/vertebral morphogenesis disrupted --> vertebral defects
        +--> Cardiac morphogenesis disrupted -----------> CHD (HLHS, CoA, BAV)
        +--> Nephrogenesis disrupted -------------------> renal/urinary anomalies
        +--> Limb-bud patterning disrupted -------------> limb defects
        +--> Severe deficiency -------------------------> embryo loss / miscarriage
```

### Pathway detail

- **Molecular pathway:** The **kynurenine (tryptophan → NAD) *de novo* biosynthesis pathway**. Order: tryptophan → … → 3-hydroxykynurenine → (**KYNU**) → 3-hydroxyanthranilic acid → (**HAAO**) → ACMS → … → nicotinic acid adenine dinucleotide (NaAD) → (**NADSYN1**) → **NAD**. NADSYN1 catalyzes the terminal amidation step, which is **shared with the Preiss–Handler pathway**, explaining partial salvage rescue (see below) [PMID: 28792876; PMID: 36649848].
- **Cellular processes:** NAD is required for redox reactions, PARP-mediated DNA repair/signaling, and sirtuin-dependent regulation; its depletion in rapidly proliferating embryonic progenitors is the presumed proximate cellular lesion.
- **Protein dysfunction:** Loss of enzymatic function (null/hypomorphic), with reduced *in vitro* activity confirmed [PMID: 28792876].
- **Metabolic changes:** Reduced circulating and tissue NAD; gene-specific accumulation of pathway intermediates.
- **Biomarker corollary (Finding F005):** Because each enzyme sits at a distinct step, expected plasma signatures are — **KYNU** deficiency: kynurenine / 3-hydroxykynurenine (with shunting to xanthurenic/kynurenic acid); **HAAO** deficiency: 3-hydroxyanthranilic acid; **NADSYN1** deficiency: NaAD — each accompanied by **low NAD**.
- **Salvage-pathway rescue:** NADSYN1's terminal position allows partial NAD replenishment via nicotinamide/salvage: in an adult patient "the NAD pool rose approximately 25% after supplementation with nicotinamide" [PMID: 36649848].

**Suggested ontology terms:** GO:0009435 (NAD biosynthetic process); GO:0034354 (*de novo* NAD biosynthetic process from tryptophan); GO:0043420 (anthranilate metabolic process); GO:0006979 (response to oxidative stress). Cell types (CL): CL:0000222 (mesodermal cell), somite/sclerotome progenitors, cardiac progenitor cells, metanephric mesenchymal cells, limb mesenchyme.

> Supporting evidence — [PMID: 28792876](https://pubmed.ncbi.nlm.nih.gov/28792876/): "Defects similar to those in the patients developed in the embryos of Haao-null or Kynu-null mice owing to NAD deficiency." … "We tested the function of the variant by using assays of in vitro enzyme activity and by quantifying metabolites in patient plasma."

---

## 7. Anatomical Structures Affected

**Organ level (primary):** vertebral column / axial skeleton (UBERON:0001130 vertebral column), heart (UBERON:0000948), kidney (UBERON:0002113) and urinary tract, limbs (UBERON:0002101). Additional: palate (UBERON:0001716), ribs (UBERON:0002228), eyelid (ptosis).

**Body systems:** cardiovascular, skeletal/musculoskeletal, genitourinary/renal, and (variably) craniofacial and central nervous (developmental delay).

**Secondary involvement:** complications of the primary malformations — heart failure and cyanosis from CHD; renal insufficiency from urinary tract anomalies; orthopedic sequelae (scoliosis, limb-length discrepancy).

**Tissue/cell level:** predominantly **mesodermally-derived** progenitor tissues — sclerotome/somite (vertebrae), cardiac mesoderm/neural-crest-derived outflow structures, nephrogenic (metanephric) mesenchyme, and limb-bud mesenchyme. Cell Ontology suggestions: CL:0000222 (mesodermal cell); cardiac progenitor cell; metanephric mesenchyme cell; limb mesenchymal cell.

**Subcellular level:** NAD metabolism spans **cytosol and mitochondria**; relevant GO cellular components include GO:0005739 (mitochondrion) and GO:0005829 (cytosol). The enzymatic steps of the kynurenine pathway are cytosolic, while NAD-dependent energy metabolism is heavily mitochondrial.

**Localization / lateralization:** Malformations are typically **bilateral or midline/axial** (vertebrae, heart, palate), though specific cardiac lesions (e.g., aortic arch anomalies, HLHS) reflect left-sided/outflow structures.

---

## 8. Temporal Development

- **Onset:** **Congenital / prenatal.** The malformations arise during embryonic organogenesis; the most severe cases present as **prenatal loss/miscarriage** or neonatal death. The insult window is the critical period of somite, cardiac, renal, and limb morphogenesis.
- **Onset pattern:** Fixed structural malformations established *in utero* (not acute/insidious postnatal onset).
- **Progression / course:** The malformations themselves are **static** (non-progressive) structural defects, but their **complications are progressive** (e.g., heart failure, renal insufficiency, orthopedic deformity). Disease is **chronic and lifelong** in survivors.
- **Disease stages:** Best framed as (i) prenatal establishment of malformations, (ii) neonatal/perinatal presentation and stabilization, (iii) childhood surgical correction and developmental follow-up, (iv) long-term management of residual disability. Some patients survive to adulthood (NADSYN1 case at age 30) [PMID: 36649848].
- **Critical period / window of opportunity:** **Preconception and early gestation** — the only demonstrated point of effective intervention is ensuring adequate NAD precursor supply *before and during* organogenesis (see Prevention).

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal recessive.** Disease requires biallelic LoF variants; heterozygous carriers are generally unaffected (though maternal carrier genotype at *SLC6A19* can, under precursor limitation, contribute to offspring risk — a maternal-effect/gene–environment nuance).
- **Penetrance / expressivity:** **Variable expressivity** is prominent. The classic HAAO/KYNU presentation includes renal and limb anomalies and can be lethal; **NADSYN1** cases can **spare the kidneys and limbs**, not meet VACTERL criteria, and survive to adulthood [PMID: 35491967; PMID: 36649848]. Environmental precursor supply modulates penetrance.
- **Consanguinity:** Homozygous null alleles in reported families indicate a role for **consanguinity/founder** recessive inheritance; specific founder alleles are not established in the provided evidence.
- **Anticipation / mosaicism:** Not applicable (no repeat-expansion mechanism); germline mosaicism not reported.
- **Epidemiology:** CNDD is **ultra-rare**, with only a small number of families/cases reported worldwide since 2017; precise prevalence/incidence figures are not established. The condition is likely **under-ascertained**, because milder (renal-sparing, adult-surviving) presentations may not be recognized or genetically tested [PMID: 35491967].
- **Sex ratio / demographics:** No strong sex bias expected for an autosomal recessive malformation syndrome; specific ethnic/geographic clustering is undefined beyond consanguineous pedigrees.

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality).**
- **Whole-exome (WES) or whole-genome sequencing (WGS)** is the cornerstone, identifying biallelic LoF variants in HAAO, KYNU, or NADSYN1. Trio sequencing aids phasing (compound heterozygosity).
- **Targeted gene panels** covering HAAO / KYNU / NADSYN1 (and NAD-pathway genes) are appropriate for VACTERL-like presentations.
- **Chromosomal microarray / copy-number analysis** is needed to detect structural alleles (e.g., the reported **homozygous HAAO exon-5 deletion**).
- **Actionable recommendation:** NADSYN1 sequencing should be performed in children with VATER/VACTERL-related anomalies **and** in those with HLHS or aortic arch abnormalities [PMID: 35491967].

**Biochemical / metabolomic testing (functional confirmation).**
- **Plasma NAD quantification** (reduced) and **targeted kynurenine-pathway metabolomics** provide functional evidence and can localize the defect to a specific enzymatic step (gene-specific substrate accumulation with low NAD) [PMID: 28792876]. This is especially useful to classify variants of uncertain significance.

**Imaging & clinical work-up.**
- **Echocardiography / cardiac imaging** for CHD; **spine and skeletal radiographs / CT** for vertebral and rib anomalies; **renal ultrasound** for urinary tract malformation; **prenatal ultrasound/fetal echo** can detect malformations *in utero*.

**Clinical criteria / differential diagnosis.**
- Presentations overlap the **VACTERL/VATER association**; CNDD is a specific molecular subtype. Differential diagnoses include other VACTERL-like syndromes, chromosomal disorders, TBX-pathway and ciliopathy-related malformation syndromes, and teratogen-induced malformations. The distinguishing features of CNDD are **recessive inheritance, biallelic NAD-pathway gene variants, low NAD, and abnormal kynurenine metabolites**.

**Screening.** Carrier screening in consanguineous families and **cascade testing** of relatives once a proband variant is identified.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** Highly variable and **organ-severity dependent**. Severe cardiac (e.g., HLHS) and renal malformations, or profound embryonic NAD deficiency, cause **prenatal loss, neonatal death, or high early mortality**. Milder (renal-sparing) NADSYN1 disease is compatible with **survival to adulthood** (documented case at age 30) [PMID: 36649848].
- **Morbidity / disability:** Chronic disability from congenital heart disease, renal insufficiency, spinal/skeletal deformity (scoliosis, limb-length discrepancy), and developmental delay in some survivors.
- **Complications:** Heart failure, cyanosis, arrhythmia post-repair; chronic kidney disease; orthopedic sequelae; feeding/growth issues with cleft palate.
- **Recovery potential:** Structural malformations do not resolve but are **surgically correctable** (e.g., bicuspid aortic valve stenosis corrected surgically in the adult NADSYN1 case) [PMID: 36649848]; prognosis improves with early surgical management.
- **Prognostic factors:** Causal gene and residual enzyme activity, severity of cardiac and renal lesions, degree of NAD deficiency, and adequacy of any perinatal NAD precursor supply.

---

## 12. Treatment

CNDD malformations are **structural and established prenatally**, so postnatal treatment is **corrective/supportive**, while the disorder's landmark feature is a **preventive** metabolic intervention (see Section 13).

- **Metabolic/pharmacologic (NAD precursors):** **Niacin/nicotinamide (vitamin B3)** supplementation is the mechanistically-targeted therapy. Its principal value is **preventive during gestation**; postnatally it can partly replenish the NAD pool, particularly in **NADSYN1** disease where the salvage pathway bypasses the terminal defect — nicotinamide raised the NAD pool ~25% in an adult NADSYN1 patient [PMID: 36649848]. CHEBI: nicotinamide (CHEBI:17154), nicotinic acid/niacin (CHEBI:15940), NAD (CHEBI:15846). NCIT: Niacin/Nicotinamide therapy.
- **Surgical / interventional:** Repair of congenital heart defects (e.g., aortic valve/arch surgery, HLHS staged palliation), urologic/renal surgery, and orthopedic correction of spinal and limb anomalies.
- **Supportive / rehabilitative:** Cardiology and nephrology management, physical/occupational therapy for skeletal disability, developmental support and early intervention, nutritional support (especially with cleft palate).
- **Personalized medicine:** Genotype-guided — NADSYN1 (terminal step) patients are the most likely to derive biochemical benefit from salvage-pathway precursors (nicotinamide/nicotinamide riboside).
- **Experimental / trials:** No disease-specific approved therapeutics or registered trials are identified in the provided evidence; NAD-precursor supplementation is the leading translational strategy.

---

## 13. Prevention

Prevention is the defining, most impactful aspect of this disorder.

- **Primary prevention (the key intervention):** Ensure **adequate maternal NAD precursor status (niacin/nicotinamide, dietary tryptophan) before conception and throughout gestation**. In genetic mouse models, gestational supplementation prevents the malformations: "Defects similar to those in the patients developed in the embryos of Haao-null or Kynu-null mice owing to NAD deficiency" — and were prevented by supplementation [PMID: 28792876]. Environmental/gene–environment NAD deficiency causing malformations is likewise precursor-preventable [PMID: 32015132].
- **High-risk targeting:** Maternal carriers of **SLC6A19** LoF alleles (and couples with a prior CNDD child) are candidates for **precursor supplementation and close pregnancy monitoring** [PMID: 36374036].
- **Secondary prevention:** Prenatal ultrasound/fetal echocardiography and early postnatal imaging for early detection and surgical planning.
- **Genetic counseling:** For autosomal-recessive recurrence risk (25% for carrier couples), **carrier and cascade testing**, and reproductive options (prenatal diagnosis, PGT). Counsel carrier mothers about NAD precursor adequacy in future pregnancies.
- **Public health corollary:** Adequate maternal niacin/tryptophan nutrition is a broadly protective, low-cost measure against NAD-deficiency malformations.

> Supporting evidence — [PMID: 32015132](https://pubmed.ncbi.nlm.nih.gov/32015132/): "NAD deficiency due to environmental factors or gene-environment interactions causes congenital malformations and miscarriage in mice."

---

## 14. Other Species / Natural Disease

- **Taxonomy / models:** Demonstrated in **mouse (*Mus musculus*, NCBI:txid10090)**. No naturally-occurring companion-animal or wildlife CNDD equivalent is documented in the provided evidence.
- **Orthologous genes:** *Haao*, *Kynu*, *Nadsyn1*, and *Slc6a19* are conserved in mouse and other mammals; the kynurenine→NAD pathway is evolutionarily conserved, supporting cross-species mechanistic translation.
- **Comparative biology:** Mouse knockouts recapitulate the human malformation spectrum via NAD deficiency, indicating strong **evolutionary conservation of the disease mechanism** [PMID: 28792876; PMID: 32015132].
- **Zoonotic potential:** None (non-infectious genetic/metabolic disorder).

---

## 15. Model Organisms

- **Primary model — mouse:** *Haao*-null and *Kynu*-null mice develop malformations mirroring patients due to NAD deficiency, and these are **prevented by gestational niacin/nicotinamide** [PMID: 28792876]. This model demonstrates causality and the preventive intervention.
- **Environmental/gene–environment model:** Mice exposed to maternal vitamin B3/tryptophan restriction or hypoxia, and **maternal *Slc6a19*+/− mice on B3-depleted diets**, develop reduced NAD, increased embryo loss, and CNDD-type malformations [PMID: 32015132; PMID: 36374036].
- **Phenotype recapitulation:** High — mouse models reproduce the vertebral/cardiac/renal/limb malformation spectrum and the NAD-deficiency biochemistry, and validate the preventive strategy.
- **Model limitations:** Human genotype–phenotype variability (e.g., renal-sparing NADSYN1 adults) and specific severe cardiac lesions (HLHS) are not fully captured; timing/dose thresholds of NAD deficiency versus specific malformations require further definition.
- **Model type suggestions for future work:** Conditional/tissue-specific NAD-pathway knockouts; NADSYN1 hypomorph knock-in models; patient-iPSC–derived cardiac/renal organoids to model gene-specific metabolite signatures and precursor rescue.

---

## Mechanistic Model / Interpretation

CNDD is best understood as a **single convergent metabolic bottleneck (embryonic NAD supply) reached by multiple routes**. The three core genes map to distinct, sequential steps of the *de novo* pathway; a block at any step lowers NAD. Crucially, the **terminal position of NADSYN1** — shared with the Preiss–Handler/salvage route — explains two clinical observations: (1) NADSYN1 disease can be **milder/renal-sparing** and adult-compatible, and (2) it is the genotype most **amenable to salvage-pathway rescue** with nicotinamide (~25% NAD pool increase). Meanwhile, the **maternal–fetal supply network** (dietary niacin/tryptophan, hypoxia, maternal SLC6A19 transporter genotype) can push embryonic NAD below the morphogenetic threshold even without biallelic core-gene lesions, making CNDD a textbook gene–environment disorder. The therapeutic and preventive corollary is unusually clear for a Mendelian malformation syndrome: **guarantee NAD precursor supply during the periconceptional/early-gestational critical window.**

| Gene | Step | Expected accumulated metabolite | NAD | Typical severity |
|---|---|---|---|---|
| KYNU | 3-OH-kynurenine → 3-HAA (upstream) | kynurenine / 3-OH-kynurenine (± xanthurenic/kynurenic acid) | Low | Classic severe, renal-inclusive |
| HAAO | 3-HAA → ACMS (upstream) | 3-hydroxyanthranilic acid | Low | Classic severe, renal-inclusive |
| NADSYN1 | NaAD → NAD (terminal) | nicotinic acid adenine dinucleotide (NaAD) | Low | Variable; can spare kidney/limb; salvage-rescuable |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [28792876](https://pubmed.ncbi.nlm.nih.gov/28792876/) | *NAD Deficiency, Congenital Malformations, and Niacin Supplementation* | Foundational: identifies HAAO/KYNU variants, reduced NAD, mouse causality, prevention by niacin |
| [33942433](https://pubmed.ncbi.nlm.nih.gov/33942433/) | *New cases that expand the genotypic and phenotypic spectrum of CNDD* | Names the three causal genes (KYNU, HAAO, NADSYN1) and the disease term/phenotype |
| [35491967](https://pubmed.ncbi.nlm.nih.gov/35491967/) | *Two patients with biallelic NADSYN1 variants (cardiac and vertebral anomalies)* | Documents renal/limb-sparing NADSYN1 phenotype, HLHS/aortic arch link, testing recommendation |
| [36649848](https://pubmed.ncbi.nlm.nih.gov/36649848/) | *Adult patient with NADSYN1-associated congenital NAD deficiency* | Adult survival, renal sparing, ~25% NAD rise with nicotinamide (salvage rescue) |
| [32015132](https://pubmed.ncbi.nlm.nih.gov/32015132/) | *NAD deficiency from environmental factors/gene-environment interactions in mice* | Establishes environmental & GxE routes to the malformation phenotype |
| [36374036](https://pubmed.ncbi.nlm.nih.gov/36374036/) | *Maternal heterozygosity of Slc6a19 causes CNDD in mice* | Maternal modifier/gene–environment axis; carrier-risk implication |
| [37300479](https://pubmed.ncbi.nlm.nih.gov/37300479/) | *NAD Deficiency and Its Impact on Mammalian Development* (review) | Consolidating review of NAD in development |
| [34681008](https://pubmed.ncbi.nlm.nih.gov/34681008/) | *Disruptive [NAD pathway variants]* | Additional evidence on NAD-pathway perturbation and birth defects |
| [34200361](https://pubmed.ncbi.nlm.nih.gov/34200361/) | *Homozygous deletion of exon 5 of [HAAO], VCRL syndrome* | Structural (exon-deletion) allele; VCRL nomenclature |

**Note on a citation caveat:** The knowledge outline flags the PMID 32015132 snippet as a "mismatch" during verification; the quoted sentence should be treated as paraphrasing the paper's demonstrated conclusion (environmental/GxE NAD deficiency causing malformations/miscarriage in mice) rather than an exact-verified verbatim quote. All other quoted snippets in this report were verified against stored abstracts.

---

## Limitations and Knowledge Gaps

- **Rarity and ascertainment:** Only a small number of families/cases are reported; true prevalence, incidence, penetrance, and sex/geographic distribution are **unknown**. Milder (renal-sparing, adult-surviving) cases are likely **under-diagnosed** [PMID: 35491967].
- **Downstream molecular effectors are inferred:** The exact NAD-dependent processes (PARP, sirtuin, redox) linking NAD deficiency to specific malformations in specific tissues are **not fully demonstrated** in human tissue.
- **No formal MONDO ID** captured in the evidence set; database harmonization (MONDO/Orphanet/ICD-11 mapping) is incomplete here.
- **Biomarker signatures are predicted, not fully clinically validated:** Gene-specific plasma metabolite panels are mechanistically expected but require prospective diagnostic validation.
- **Treatment evidence is preclinical/anecdotal:** Prevention efficacy is established in mice; human dosing, timing, and outcome data (especially preventive supplementation in at-risk pregnancies) are **lacking**. The ~25% NAD rise with nicotinamide is a single adult case.
- **No QoL, survival-curve, or registry data** exist for this ultra-rare disorder.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a CNDD patient registry** across HAAO/KYNU/NADSYN1 genotypes to define natural history, penetrance, expressivity, survival, and genotype–phenotype correlations.
2. **Validate gene-specific plasma metabolite diagnostics** (kynurenine, 3-OH-kynurenine, 3-hydroxyanthranilic acid, NaAD, NAD) as a functional test to resolve VUS and localize the enzymatic block.
3. **Prospective preventive-supplementation study** of NAD precursors in high-risk pregnancies (prior affected child; maternal SLC6A19 or NAD-pathway carriers), building on mouse prevention data [PMID: 28792876; PMID: 36374036].
4. **Define maternal SLC6A19 and NAD-pathway carrier frequencies** in populations and evaluate periconceptional NAD status as an adverse-pregnancy-outcome risk marker.
5. **Model organism dissection of the critical window:** conditional NAD-pathway knockouts and iPSC-derived cardiac/renal/somite organoids to map NAD thresholds, timing, and the downstream effectors (PARP/sirtuin/redox) per organ.
6. **Assess NADSYN1 salvage-rescue therapeutically:** trial nicotinamide/nicotinamide riboside in NADSYN1 patients with biochemical endpoints (NAD pool) and clinical follow-up.
7. **Formal ontology harmonization:** assign/confirm MONDO, Orphanet, ICD-11, and MeSH mappings and align HPO annotation frequencies with registry data.

---

*Evidence source types used: human clinical genetics (case reports/series), aggregated disease resources (OMIM), and model-organism (mouse) experiments, with mechanistic inference where noted.*


## Artifacts

- [OpenScientist final report](Congenital_Vertebral-Cardiac-Renal_Anomalies_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Vertebral-Cardiac-Renal_Anomalies_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 9 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 12 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0043420` (obsolete anthranilate metabolic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002813` (1 mention) - the report calls it "Abnormality of limb bone morphology"; HP calls it **Abnormal limb bone morphology**, and lists "Abnormality of limb bone morphology" among its other names
- `GO:0034354` (1 mention) - the report calls it "de novo* NAD biosynthetic process from tryptophan"; GO calls it **'de novo' NAD+ biosynthetic process from L-tryptophan**, and lists "'de novo' NAD biosynthetic process from tryptophan" among its other names
- `GO:0043420` (1 mention) - the report calls it "anthranilate metabolic process"; GO calls it **obsolete anthranilate metabolic process**, and lists "anthranilate catabolic process" among its other names

27 of 28 terms resolved to a current term; the rest could not be looked up either way.