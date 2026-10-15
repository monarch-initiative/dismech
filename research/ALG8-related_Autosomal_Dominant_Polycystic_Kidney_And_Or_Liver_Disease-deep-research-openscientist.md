---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-08T10:47:22.636661'
end_time: '2026-10-08T11:01:17.951713'
duration_seconds: 835.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ALG8-related Autosomal Dominant Polycystic Kidney And/Or Liver Disease
  mondo_id: MONDO:1060122
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
- provider: openai
  succeeded: false
  error_type: ProviderAuthError
  status_code: 401
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 14
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ALG8-related_Autosomal_Dominant_Polycystic_Kidney_And_Or_Liver_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ALG8-related_Autosomal_Dominant_Polycystic_Kidney_And_Or_Liver_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALG8-related Autosomal Dominant Polycystic Kidney And/Or Liver Disease
- **MONDO ID:** MONDO:1060122 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG8-related Autosomal Dominant Polycystic Kidney And/Or Liver Disease** covering all of the
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

# ALG8-related Autosomal Dominant Polycystic Kidney And/Or Liver Disease — Comprehensive Research Report

**Disease:** ALG8-related Autosomal Dominant Polycystic Kidney And/Or Liver Disease
**MONDO ID:** MONDO:1060122
**Category:** Mendelian (autosomal dominant, low-penetrance)
**Causal gene:** *ALG8* (α-1,3-glucosyltransferase; HGNC:23159; chr 11q14.1; OMIM gene *608103*)

---

## Summary

ALG8-related polycystic kidney and/or liver disease is a rare, adult-onset, **mild** autosomal dominant cystic disorder caused by heterozygous loss-of-function (LoF) variants in *ALG8*, a gene encoding an endoplasmic reticulum (ER) α-1,3-glucosyltransferase (EC 2.4.1.265) integral to dolichol-linked N-glycosylation and protein biogenesis. *ALG8* was identified as a minor polycystic liver disease (PCLD/ADPLD) gene by whole-exome sequencing in a discovery cohort of 102 PRKCSH/SEC63-negative patients, where cell-model inactivation demonstrated that *ALG8* loss impairs the maturation and trafficking of **polycystin-1 (PC1)**, the central determinant of cyst formation [PMID: 28375157]. The phenotype is predominantly **polycystic liver disease with limited bilateral kidney cysts** that, importantly, rarely progress to chronic kidney disease or kidney failure.

A defining feature of this disease is its **low penetrance and allelic dichotomy**. Monoallelic (heterozygous) LoF variants cause the adult-onset mild cystic phenotype, whereas **biallelic** *ALG8* variants cause a completely distinct, severe multisystem pediatric disorder — the congenital disorder of glycosylation **ALG8-CDG (CDG-Ih; OMIM #608104)** — characterized by hypotonia, protein-losing enteropathy, hepatic involvement, and failure to thrive. *ALG8* is not strongly constrained against heterozygous LoF (gnomAD pLI ≈ 0, LOEUF ≈ 0.87), and population carrier frequencies of predicted-pathogenic ADPLD-gene variants (~1:91 to 1:500) dramatically exceed the clinical prevalence of ADPLD (~9.5 per 100,000), confirming that most carriers never develop clinically significant disease.

Clinically, the disease is managed symptomatically. **Somatostatin analogues** (octreotide, lanreotide, pasireotide) reduce liver and kidney volume, with the greatest benefit in young women (≤48 years) and those with elevated baseline alkaline phosphatase; interventional and surgical options (aspiration-sclerotherapy, fenestration, resection, transplantation) are reserved for severe symptomatic polycystic liver disease. The *ALG8* ClinVar landscape is dominated by variants of uncertain significance (VUS), which complicates clinical interpretation. This report synthesizes seven confirmed findings across the full disease-characteristics template.

---

## Key Findings

### Finding 1 — *ALG8* is a minor causal gene for ADPLD/ADPKD acting via defective polycystin-1 maturation in the ER

Dominantly inherited isolated polycystic liver disease (PCLD) produces liver cysts radiologically and pathologically identical to those of ADPKD but without clinically relevant kidney cysts. Because the two most common PCLD genes (*PRKCSH* and *SEC63*) explain fewer than 40% of index cases, Besse et al. (2017) performed whole-exome sequencing in a **discovery cohort of 102 unrelated patients** who were negative for *PRKCSH*/*SEC63*, identifying heterozygous LoF variants in three additional genes: ***ALG8*, *GANAB*, and *SEC61B*** [PMID: 28375157].

> *"we have used whole exome sequencing in a discovery cohort of 102 unrelated patients who were excluded for mutations in the 2 most common PCLD genes, PRKCSH and SEC63, to identify heterozygous loss-of-function mutations in 3 additional genes, ALG8, GANAB, and SEC61B"* [PMID: 28375157]

Critically, all these genes encode proteins integral to the ER protein-biogenesis pathway. Cell-line inactivation established the mechanistic link to cystogenesis:

> *"We inactivated these candidate genes in cell line models to show that loss of function of each results in defective maturation and trafficking of polycystin-1, the central determinant of cyst pathogenesis"* [PMID: 28375157]

*ALG8* thus joins the N-glycosylation / ER quality-control module that governs PC1 biogenesis. Each gene product demonstrated distinct effects on PC1 biogenesis despite acting in a common pathway. **Evidence type:** human clinical (WES) + in vitro cell model.

### Finding 2 — Monoallelic *ALG8* variants cause a mild cystic phenotype, predominantly polycystic liver with limited kidney involvement

Two large independent cohorts quantify the mild phenotype. **Jawaid et al. (2025)** screened >3,900 families with cystic kidney and/or liver disease and identified **51 *ALG8* families (1.3%)**, a frequency ~10× greater than non-polycystic controls, establishing *ALG8* enrichment in the polycystic population [PMID: 39899384].

**Apple et al. (2023)** used the Geisinger DiscovEHR electronic-health-record cohort (174,172 patients; 236 *ALG8* protein-truncating-variant [PTV] carriers) with blinded imaging review. *ALG8* PTV carriers had increased risk of any kidney/liver cyst (OR 2.42, 95% CI 1.53–3.85), cystic kidney disease (OR 3.03, 95% CI 1.26–7.31), and nephrolithiasis (OR 1.89) [PMID: 36574950].

> *"patients with these variants were significantly at increased risk of having any kidney/liver cyst diagnosis (Odds Ratio 2.42, 95% confidence interval: 1.53-3.85), cystic kidney disease (3.03, 1.26-7.31), and nephrolithiasis (1.89, 1.96-2.97)"* [PMID: 36574950]

Blinded imaging confirmed a measurable cyst burden:

> *"ALG8 PTV heterozygotes were significantly more likely to have cystic kidney disease, defined as four or more kidney cysts (57.7% vs. 7.7%), or bilateral kidney cysts (69.2% vs. 15.4%), but not one or more liver cyst (11.5% vs. 7.7%)"* [PMID: 36574950]

Crucially, the disease does **not** progress to end-stage renal disease:

> *"ALG8 PTVs were not associated with chronic kidney disease or kidney failure"* [PMID: 36574950]

This establishes the hallmark of the disorder: bilateral kidney cysts and nephrolithiasis risk, but preserved kidney function. **Evidence type:** human clinical (EHR + blinded imaging; multicenter family screening).

| Phenotype metric | *ALG8* PTV carriers | Controls | Effect |
|---|---|---|---|
| Any kidney/liver cyst | — | — | OR 2.42 (1.53–3.85) |
| Cystic kidney disease (≥4 cysts) | 57.7% | 7.7% | OR 3.03 (1.26–7.31) |
| Bilateral kidney cysts | 69.2% | 15.4% | — |
| Nephrolithiasis | — | — | OR 1.89 |
| ≥1 liver cyst | 11.5% | 7.7% | NS |
| Chronic kidney disease / kidney failure | — | — | Not associated |

### Finding 3 — Allelic dichotomy: monoallelic LoF causes adult polycystic disease; biallelic variants cause severe multisystem ALG8-CDG

*ALG8* exhibits a striking genotype–phenotype dichotomy. **Albokhari et al. (2022)** report 26 individuals with **biallelic ALG8-CDG (CDG-Ih, OMIM #608104)** presenting with hypotonia, protein-losing enteropathy, hepatic involvement, and failure to thrive; the phenotype was expanded to include intellectual disability, autism, and ocular/cardiac/skeletal anomalies [PMID: 35716054].

> *"Individuals with ALG8-CDG commonly present with hypotonia, protein-losing enteropathy, and hepatic involvement"* [PMID: 35716054]

**Huang et al. (2025)** reported the first prenatal ALG8-CDG cases with hydrops fetalis, cataracts, echogenic kidneys, and growth restriction, with a compound heterozygous genotype [PMID: 39792033].

> *"A novel compound heterozygous mutation comprising the missense variant c.754T>C (p.Ser252Pro) and a partial exonic deletion (deletion of exons 1-2) in the ALG8 gene"* [PMID: 39792033]

By contrast, **monoallelic** *ALG8* PTVs cause adult-onset mild polycystic kidney/liver disease (Findings 1–2). This dichotomy is mechanistically coherent: partial glycosylation deficiency (one functional allele) selectively impairs the biogenesis of the large, glycosylation-dependent PC1 protein, producing a tissue-restricted cystic phenotype, whereas near-complete deficiency (biallelic) disrupts N-glycosylation globally, producing multisystem CDG. **Evidence type:** human clinical (case series + prenatal case report). The disease described by this template (MONDO:1060122) refers specifically to the **monoallelic cystic phenotype**.

### Finding 4 — Somatostatin analogues reduce liver/kidney volume, with best response in young women

Pooled individual-patient analyses (Gevers et al. 2013; n up to 153) demonstrated that somatostatin analogues (octreotide, lanreotide) reduce liver volume by ~4.5–5.9% versus placebo (overall difference 5.3%, P<.001), with the greatest benefit in young women [PMID: 23665274].

> *"Women 48 years old or younger had a greater response to therapy (a reduction in liver volume of 8.0% compared with placebo; P < .001) than older women"* [PMID: 23665274]

Elevated baseline alkaline phosphatase predicts response [PMID: 26481454]:

> *"elevated baseline alkaline phosphatase was associated with increased liver volume reduction during therapy"* [PMID: 26481454]

A network meta-analysis incorporating FDA Adverse Event Reporting System data confirmed TKV/TLV reductions with octreotide, lanreotide, and pasireotide, with differing onset times, and identified **cholelithiasis** as the most common biliary adverse event (younger patients and pasireotide users at higher risk) [PMID: 42476150]. mTOR inhibitors (everolimus) added to octreotide have not shown benefit over octreotide monotherapy (ELATE trial; no significant difference, P=0.73) [PMID: 26688394, PMID: 22104015]. **Evidence type:** human clinical (RCTs, pooled IPD, network meta-analysis).

### Finding 5 — ADPLD is rare clinically (~9.5/100,000) but LoF variants in ADPLD genes are far more common at the population level, indicating low penetrance

Suwabe et al. (2020, Olmsted County) established the clinical rarity of ADPLD [PMID: 33145487]:

> *"The incidence rate and point prevalence of combined definite and likely ADPLD were 1.01 per 100,000 person-years and 9.5 per 100,000 population, respectively"* [PMID: 33145487]

Yet population sequencing reveals a far higher molecular carrier frequency. Lanktree et al. (2018), using gnomAD/BRAVO, estimated [PMID: 30135240]:

> *"Truncating mutations in ADPLD genes and genes of potential relevance as cyst modifiers were found in 20.2 cases and 103.9 cases per 10,000 sequenced"* [PMID: 30135240]

This ~1:495 truncating-mutation frequency vastly exceeds the ~9.5/100,000 clinical prevalence. A subsequent gnomAD-based study (Varughese et al. 2026) found predicted-pathogenic ADPLD-gene variants in ~1:91 (gnomAD v2.1.1) to ~1:130 (ClinVar-assessed v4.1) people, with *LRP5* and ***ALG8*** — both associated with milder phenotypes — the most commonly affected genes; frequencies were higher in admixed American (1:91), Finnish (1:110), and African/African American (1:43) populations than European (1:187) [PMID: 42804492]. The discordance quantifies **incomplete penetrance and variable expressivity**. **Evidence type:** human clinical epidemiology + population genomics.

### Finding 6 — *ALG8* is not strongly constrained against heterozygous LoF, consistent with its low-penetrance dominant phenotype

gnomAD constraint metrics (queried via gnomAD GraphQL API, GRCh38) for *ALG8* (ENSG00000159063; chr11:78,095,244–78,139,660):

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 2.3×10⁻¹¹ (≈0) | Tolerant of heterozygous LoF |
| Observed/expected LoF (oe_lof) | 0.684 (obs 48, exp 70.2) | Modest depletion |
| LOEUF (oe_lof_upper) | 0.869 | Not strongly constrained |
| lof_z | 2.25 | Mild constraint signal |
| Missense z | 0.64 (oe_mis 0.94) | Missense-tolerant |

A pLI ≈ 0 and LOEUF ≈ 0.87 indicate that *ALG8* tolerates heterozygous LoF relatively well, with 48 LoF variants observed in gnomAD. This genomic constraint profile is fully consistent with a low-penetrance dominant phenotype in which many heterozygous LoF carriers remain clinically unaffected (Finding 5). **Evidence type:** computational / population genomics.

### Finding 7 — The *ALG8* ClinVar landscape is dominated by variants of uncertain significance

ClinVar (queried via NCBI E-utilities) for *ALG8*[gene] returned ~510 total records:

| Classification | Count |
|---|---|
| Pathogenic | 111 |
| Likely pathogenic | 59 |
| **P/LP combined** | **170** |
| Uncertain significance (VUS) | 380 |
| Benign | 261 |
| Likely benign | 257 |

VUS (380) substantially outnumber P/LP classifications (170). These counts aggregate both the biallelic ALG8-CDG and the monoallelic cystic phenotypes, because ClinVar does not cleanly partition records by condition. The VUS predominance complicates clinical interpretation and reinforces the need for functional validation and family segregation data. **Evidence type:** variant database curation.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (monoallelic cystic phenotype)

```
1. Heterozygous loss-of-function variant in ALG8 (one allele inactivated)
        │  leads to
        ▼
2. Reduced ER α-1,3-glucosyltransferase activity (EC 2.4.1.265),
   adding the third glucose to the dolichol-linked precursor
   Glc3Man9GlcNAc2-PP-dolichol  [inferred for monoallelic; demonstrated for biallelic]
        │  results in
        ▼
3. Partial deficiency of N-linked glycosylation / ER protein biogenesis
        │  results in (tissue-selective, dose-sensitive)
        ▼
4. Defective maturation and trafficking of polycystin-1 (PC1) —
   a large, heavily glycosylation-dependent membrane protein  [demonstrated in vitro, PMID: 28375157]
        │  leads to
        ▼
5. Reduced functional PC1 at the primary cilium of biliary and
   renal tubular epithelial cells
        │  results in
        ▼
6. Dysregulated cAMP / mTOR signaling, epithelial proliferation,
   and fluid secretion into expanding cysts
        │  manifests as
        ▼
7a. BILIARY BRANCH → polycystic liver disease (predominant)
7b. RENAL BRANCH   → bilateral kidney cysts + nephrolithiasis risk,
                     WITHOUT progression to kidney failure  [PMID: 36574950]
```

### Branch point: monoallelic vs biallelic genotype

```
                 ALG8 variant dosage
                        │
        ┌───────────────┴────────────────┐
   MONOALLELIC LoF                   BIALLELIC (compound het / homozygous)
   (partial deficiency)              (near-complete deficiency)
        │                                 │
   Selective PC1                     Global N-glycosylation failure
   mis-processing                         │
        │                            Multisystem ALG8-CDG (CDG-Ih)
   Adult-onset, mild                 hypotonia, protein-losing enteropathy,
   polycystic liver ± kidney         hepatic involvement, failure to thrive,
   (MONDO:1060122)                   neuro-ophthalmologic disease, hydrops fetalis
   [PMID: 28375157; 36574950]        [PMID: 35716054; 39792033]
```

### Upstream vs downstream, cells, and ontology terms

- **Upstream (initiating):** *ALG8* haploinsufficiency → impaired N-glycosylation. GO biological process: **GO:0006487** (protein N-linked glycosylation), **GO:0006488** (dolichol-linked oligosaccharide biosynthetic process). Molecular function: α-1,3-glucosyltransferase activity.
- **Intermediate (effector):** defective PC1 biogenesis and ER quality control. Cellular component: **GO:0005789** (endoplasmic reticulum membrane).
- **Downstream (clinical):** ciliary dysfunction → cystogenesis. Cell types: **CL:1000488** (cholangiocyte / biliary epithelial cell), kidney tubular epithelial cell. Subcellular: primary cilium (**GO:0005929**).
- **Anatomy (UBERON):** liver **UBERON:0002107**, intrahepatic bile duct **UBERON:0001174**, kidney **UBERON:0002113**.
- **Chemistry (CHEBI):** dolichyl phosphate, glucose (CHEBI:17234); somatostatin analogues — octreotide, lanreotide, pasireotide.

The monoallelic phenotype's tissue selectivity (liver > kidney, no renal failure) is best explained by PC1's exceptional dependence on complete glycosylation for folding/trafficking: a partial glycosylation deficit disproportionately affects this one client protein rather than causing generalized cellular failure.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | *Isolated polycystic liver disease genes define effectors of polycystin-1 function* | Landmark: discovers heterozygous LoF *ALG8* in PCLD; demonstrates PC1 mis-processing in vitro (Findings 1, 3) |
| [36574950](https://pubmed.ncbi.nlm.nih.gov/36574950/) | *Individuals heterozygous for ALG8 protein-truncating variants are at increased risk of a mild cystic kidney disease* | Quantifies cyst burden and ORs; shows no CKD/kidney-failure association (Finding 2) |
| [39899384](https://pubmed.ncbi.nlm.nih.gov/39899384/) | *Characterization of the Cystic Phenotype Associated with Monoallelic ALG8 and ALG9 Pathogenic Variants* | 51 *ALG8* families (1.3%), ~10× enrichment (Finding 2) |
| [35716054](https://pubmed.ncbi.nlm.nih.gov/35716054/) | *ALG8-CDG: Molecular and phenotypic expansion suggests clinical management guidelines* | Defines severe biallelic ALG8-CDG phenotype (Finding 3) |
| [39792033](https://pubmed.ncbi.nlm.nih.gov/39792033/) | *ALG8-CDG: advances in molecular and prenatal phenotyping* | First prenatal ALG8-CDG; biallelic genotype (Finding 3) |
| [23665274](https://pubmed.ncbi.nlm.nih.gov/23665274/) | *Young women with polycystic liver disease respond best to somatostatin analogues* | Treatment response subgroup (Finding 4) |
| [26481454](https://pubmed.ncbi.nlm.nih.gov/26481454/) | *Alkaline phosphatase predicts response in polycystic liver disease* | Predictive biomarker of treatment response (Finding 4) |
| [42476150](https://pubmed.ncbi.nlm.nih.gov/42476150/) | *Comparative Efficacy and Safety of Octreotide, Lanreotide, and Pasireotide* | Network meta-analysis; cholelithiasis adverse event (Finding 4) |
| [26688394](https://pubmed.ncbi.nlm.nih.gov/26688394/) | *Medical therapy for polycystic liver disease* | Somatostatin analogues effective; mTOR inhibitors no benefit (Finding 4) |
| [22104015](https://pubmed.ncbi.nlm.nih.gov/22104015/) | *ELATE trial protocol (everolimus + octreotide)* | Combination mTOR trial (Finding 4) |
| [33145487](https://pubmed.ncbi.nlm.nih.gov/33145487/) | *Epidemiology of ADPLD in Olmsted county* | Clinical prevalence 9.5/100,000 (Finding 5) |
| [30135240](https://pubmed.ncbi.nlm.nih.gov/30135240/) | *Prevalence Estimates of Polycystic Kidney and Liver Disease by Population Sequencing* | Truncating-mutation carrier frequency ~1:495 (Finding 5) |
| [42804492](https://pubmed.ncbi.nlm.nih.gov/42804492/) | *Population frequency of predicted pathogenic variants in ADPLD genes* | *ALG8* among commonest; 1:91–1:130; ancestry variation (Finding 5) |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | *Genetic Spectrum of Polycystic Kidney and Liver Diseases* | Context: *ALG8* a minor gene presenting as ADPKD or ADPLD |
| [38671465](https://pubmed.ncbi.nlm.nih.gov/38671465/) | *Clinical manifestation, epidemiology, genetic basis… of polycystic liver disease* | Review: ER quality-control genes impair PC1; treatment landscape |
| [38689396](https://pubmed.ncbi.nlm.nih.gov/38689396/) | *Genetic Analysis of Severe Polycystic Liver Disease in Japan* | ADPLD genes = 20% of severe PLD; female preponderance |
| [28465378](https://pubmed.ncbi.nlm.nih.gov/28465378/) | *Biliary Tract and Liver Complications in Polycystic Kidney Disease* | Biliary tract disease RR 2.24; liver complications RR 4.67 |

**Consistency assessment:** All seven findings are mutually reinforcing. The genomic constraint data (Finding 6), ClinVar VUS burden (Finding 7), and epidemiologic/population-genetic discordance (Finding 5) converge on the same conclusion — *ALG8* is a **low-penetrance, mild** dominant gene. No contradictory evidence was identified. The main interpretive caution is the allelic dichotomy (Finding 3): care must be taken not to conflate biallelic CDG literature with the monoallelic cystic disease that MONDO:1060122 denotes.

---

## Section-by-Section Disease Characteristics

**1. Disease information.** A rare adult-onset dominant cystic disorder; predominantly polycystic liver with limited kidney cysts. Identifiers: MONDO:1060122; gene *ALG8* OMIM *608103*; related biallelic disorder ALG8-CDG OMIM #608104; within the ADPLD/PCLD spectrum. Synonyms: ALG8-related ADPLD; ALG8 polycystic liver disease. Information is derived from both aggregated disease-level resources (OMIM, Orphanet) and individual-patient EHR/imaging cohorts [PMID: 36574950].

**2. Etiology.** Primary cause is genetic: heterozygous LoF variants in *ALG8*. No established environmental cause. Low penetrance implies unidentified genetic/environmental modifiers; female sex and younger age modulate liver-cyst expression and treatment response [PMID: 23665274, PMID: 38689396]. No protective factors characterized.

**3. Phenotypes.** Liver cysts (predominant; HP:0001399 hepatic cysts); bilateral renal cysts (HP:0000107; ≥4 cysts in 57.7% of carriers); nephrolithiasis (HP:0000787; OR 1.89); biliary tract disease (RR 2.24 in ADPKD context [PMID: 28465378]). Onset adult; severity mild; progression slow; kidney function preserved. QoL impact mainly from hepatomegaly-related mass effect (abdominal pain/distension) in severe PLD.

**4. Genetic/molecular.** Causal gene *ALG8* (HGNC:23159). Variant types: protein-truncating (nonsense, frameshift, splice), rare damaging missense, and structural/exon deletions. Classification: predominantly VUS (380) with 170 P/LP in ClinVar. Functional consequence: loss of function / haploinsufficiency. Germline origin. gnomAD: pLI≈0, LOEUF 0.87 (LoF-tolerant).

**5. Environmental.** No established toxic, infectious, or lifestyle cause. Disease is monogenic.

**6. Mechanism.** See causal chain above — *ALG8* haploinsufficiency → impaired N-glycosylation → defective PC1 maturation/trafficking → ciliary dysfunction → cystogenesis [PMID: 28375157].

**7. Anatomical structures.** Liver (UBERON:0002107) and intrahepatic bile ducts (UBERON:0001174) primary; kidney (UBERON:0002113) secondary. Cell types: cholangiocytes (CL:1000488), renal tubular epithelial cells. Subcellular: ER membrane (GO:0005789), primary cilium (GO:0005929). Lateralization: bilateral kidney cysts (69.2%).

**8. Temporal development.** Adult-onset, insidious, chronic, slowly progressive; no progression to kidney failure; lifelong.

**9. Inheritance/population.** Autosomal dominant, **incomplete/low penetrance**, variable expressivity. Clinical ADPLD prevalence ~9.5/100,000 [PMID: 33145487]; predicted-pathogenic carrier frequency ~1:91–1:500 [PMID: 30135240, PMID: 42804492]. Higher predicted-variant frequency in admixed American, Finnish, and African/African American populations. Female preponderance in severe PLD cohorts [PMID: 38689396].

**10. Diagnostics.** Imaging-based (ultrasound/CT/MRI cyst counts) is primary; genetic testing via NGS panels covering all PKD/ADPLD/ciliopathy genes is recommended for complex cases [PMID: 38097330]. Elevated alkaline phosphatase is a treatment-response biomarker. Differential diagnosis: ADPKD (*PKD1/PKD2*), other ADPLD genes (*PRKCSH, SEC63, GANAB, ALG9, SEC61B, LRP5*), ARPKD.

**11. Prognosis.** Favorable — kidney function preserved; main morbidity from symptomatic hepatomegaly in a minority. No excess disease-specific mortality established.

**12. Treatment.** Somatostatin analogues (octreotide, lanreotide, pasireotide) reduce TLV/TKV, best in young women [PMID: 23665274]; interventional/surgical options (aspiration-sclerotherapy, fenestration, segmental resection, liver transplantation) for severe PLD. mTOR inhibitors not beneficial [PMID: 26688394]. NCIT: octreotide (C1598), lanreotide, somatostatin analogue therapy.

**13. Prevention.** No primary prevention. Genetic counseling (incomplete penetrance, allelic dichotomy), cascade testing, and imaging surveillance of at-risk relatives. Monitor for biliary complications and cholelithiasis (somatostatin-analogue adverse event).

**14. Other species.** *ALG8* is evolutionarily conserved (yeast *ALG8*). No naturally occurring companion-animal disease established. Mechanistic conservation of N-glycosylation supports model-organism study.

**15. Model organisms.** In vitro cell-line *ALG8* inactivation models demonstrated PC1 mis-processing [PMID: 28375157]; a patient-derived iPSC line (AOUMEYi001-A) exists for ALG8-CDG [PMID: 38323760]. Dedicated mouse models of monoallelic *ALG8* cystic disease are not yet established — a knowledge gap.

---

## Limitations and Knowledge Gaps

1. **Monoallelic mechanism is inferred, not fully demonstrated.** The PC1 mis-processing mechanism was shown by full gene inactivation in cell lines [PMID: 28375157]; the quantitative glycosylation deficit produced by a single heterozygous LoF allele in human liver/kidney epithelium has not been directly measured.
2. **Low penetrance is unexplained at the modifier level.** The ~50–100-fold gap between carrier frequency and clinical prevalence (Finding 5) implies modifier genes/alleles, somatic second hits, or stochastic factors that remain uncharacterized.
3. **VUS predominance** (Finding 7) limits clinical actionability; most *ALG8* variants cannot currently be classified with confidence.
4. **ClinVar counts conflate two diseases** (biallelic CDG vs monoallelic cystic), so phenotype-specific variant interpretation is confounded.
5. **No dedicated animal model** of the monoallelic cystic phenotype exists, limiting in vivo natural-history and therapeutic study.
6. **Treatment evidence is extrapolated** from mixed ADPKD/ADPLD cohorts, not *ALG8*-specific trials; no genotype-stratified efficacy data.
7. **Epidemiology is ancestry-skewed** toward European-descent sequencing databases; true global prevalence and clinical penetrance in high-carrier-frequency populations (African/African American 1:43) are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Direct glycosylation assay in heterozygotes.** Measure dolichol-linked oligosaccharide and PC1 glycoform profiles in patient-derived cholangiocyte/tubular organoids carrying single *ALG8* LoF alleles to confirm the inferred partial-deficiency mechanism.
2. **Penetrance / modifier study.** Within biobank cohorts (UK Biobank, 100K Genomes, DiscovEHR), perform imaging-anchored penetrance estimation and modifier GWAS/burden testing in *ALG8* carriers to explain variable expressivity.
3. **Functional VUS reclassification.** Deploy a saturation-genome-editing or complementation assay for *ALG8* to systematically classify the 380 VUS by effect on glucosyltransferase activity and PC1 maturation.
4. **Animal model.** Generate a heterozygous / liver-conditional *Alg8* mouse to establish a natural-history model of the mild cystic phenotype and test somatostatin analogues genotype-specifically.
5. **Genotype-stratified treatment analysis.** Re-analyze pooled somatostatin-analogue trial data for *ALG8*-genotyped participants to test whether response differs by causal gene.
6. **Ancestry-balanced epidemiology.** Prospectively assess clinical penetrance in high-carrier-frequency populations (African/African American, Finnish, admixed American) with standardized imaging.
7. **Database curation.** Advocate for ClinVar condition-level partitioning of *ALG8* records to separate biallelic CDG from monoallelic cystic disease interpretations.

---

*Report compiled from 7 confirmed findings and 26 reviewed papers across a 5-iteration autonomous investigation. Evidence source types are annotated per finding (human clinical, in vitro, computational/population genomics).*


## Artifacts

- [OpenScientist final report](ALG8-related_Autosomal_Dominant_Polycystic_Kidney_And_Or_Liver_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ALG8-related_Autosomal_Dominant_Polycystic_Kidney_And_Or_Liver_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

13 of 14 terms resolved to a current term; the rest could not be looked up either way.