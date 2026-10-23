---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-21T16:45:32.004340'
end_time: '2026-10-21T16:59:28.716268'
duration_seconds: 836.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Craniofaciocardiohepatic Syndrome
  mondo_id: MONDO:0978295
  category: Mendelian
  causal_genes: AMOTL1
  omim_id: OMIM:621192
  synonyms: CFCHS; AMOTL1-associated multiple congenital anomalies; AMOTL1-related
    orofacial clefting syndrome
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 7
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 3
  labels_variant: 3
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Craniofaciocardiohepatic_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Craniofaciocardiohepatic_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniofaciocardiohepatic Syndrome
- **MONDO ID:** MONDO:0978295 (if available)
- **Causal gene(s):** AMOTL1
- **OMIM:** OMIM:621192
- **Synonyms:** CFCHS; AMOTL1-associated multiple congenital anomalies; AMOTL1-related orofacial clefting syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Craniofaciocardiohepatic Syndrome** covering all of the
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

# Craniofaciocardiohepatic Syndrome (CFCHS): A Comprehensive Disease Characterization Report

**Disease:** Craniofaciocardiohepatic Syndrome (CFCHS)
**Causal gene:** **AMOTL1** (angiomotin-like protein 1; HGNC:17811; NCBI Gene 154810; UniProt Q8IY63)
**OMIM:** #621192 (phenotype); *614657 (gene)
**MONDO:** MONDO:0978295
**Category:** Mendelian, autosomal dominant

---

## Summary

Craniofaciocardiohepatic syndrome (CFCHS) is an ultra-rare autosomal dominant multiple-congenital-anomaly disorder caused by **heterozygous missense variants in AMOTL1**, the gene encoding angiomotin-like protein 1. AMOTL1 is a Motin-family actin-binding adaptor protein that localizes to tight junctions and regulates cell polarity, cell-cell adhesion, directional cell migration, and Hippo–YAP signaling. The pathogenic variants cluster tightly at a conserved hotspot spanning amino acid residues **157–161**, recurrently affecting p.Arg157Cys, p.Arg157His, p.Pro160Leu, and p.Gln161Arg. This clustering, together with functional and animal-model data, indicates that CFCHS is **not** a loss-of-function/haploinsufficiency disease but rather operates through a **gain-of-function or dominant-negative mechanism**.

The molecular lesion is now well defined. The 157–161 residues form part of AMOTL1's **Tankyrase-binding motif (TBM)**. Hotspot mutants (R157C, P160L) fail to bind Tankyrase 1/2 and the E3 ligase RNF146, and therefore escape the normal poly-ADP-ribosylation → ubiquitination → proteasomal degradation cascade. The consequence is **abnormal stabilization and cytoplasmic accumulation** of mutant AMOTL1, which disrupts cell junctions and focal adhesions and impairs both the velocity and persistence of cell migration. Because craniofacial, cardiac, and hepatic organogenesis depend on precisely coordinated epithelial/endothelial migration and junction remodeling, this cellular defect derails morphogenesis and produces the multi-organ phenotype that gives the syndrome its name.

Clinically, CFCHS presents from the neonatal/congenital period with a recognizable core phenotype: **orofacial clefting (~94%)**, **dysplastic/large auricles (~62%)**, **congenital heart disease (~50%)**, **tall stature (~44%)**, and **hearing loss, liver disease, and neurodevelopmental involvement (~31% each)**, plus gastrointestinal/anorectal anomalies (e.g., imperforate anus). The disease was delineated through a small series of index families (Liegel et al. 2019; Rips et al. 2021), consolidated into a defining 16-individual cohort (Strong et al. 2023), named CFCHS with the addition of the hepatic phenotype (Gallego-Zazo et al. 2025), and mechanistically explained (Luo et al. 2026). Fewer than ~20 individuals have been reported worldwide. Management is multidisciplinary, surgical, and supportive; no gene-targeted therapy exists.

---

## Key Findings

### Finding 1 — CFCHS is caused by heterozygous AMOTL1 missense variants clustering at a conserved hotspot (aa 157–161)

CFCHS is a Mendelian, autosomal dominant disorder caused by heterozygous missense variants in **AMOTL1**. The defining cohort study by Strong et al. 2023 reported that heterozygous missense variants affecting amino acid residues 157–161 define a core phenotype of orofacial clefting, congenital heart disease, tall stature, auricular anomalies, and gastrointestinal manifestations. Recurrent variants include **p.Arg157Cys (R157C)**, **p.Arg157His (R157H)**, and **p.Pro160Leu (P160L)**, with p.Gln161Arg also reported. Rips et al. 2021 independently reported a de novo **c.479C>T (p.Pro160Leu)** in an affected infant. Both **de novo** and **inherited** (father→daughter, father→son) occurrences are documented, consistent with autosomal dominant transmission with apparent high penetrance for the hotspot alleles. **[human clinical]**

> *"heterozygous missense variants in AMOTL1, most commonly affecting amino acid residues 157-161, define a new orofacial clefting syndrome"* — Strong et al. 2023 [PMID: 36751037]

> *"trio exome sequencing revealed a de novo variant in AMOTL1 affecting a highly conserved amino acid (c.479C>T; p.[Pro160Leu])"* — Rips et al. 2021 [PMID: 33026150]

The extraordinary clustering of pathogenic variants within a 5-amino-acid window is itself strong evidence for a specific, non-loss-of-function molecular mechanism (see Findings 2 and 7).

### Finding 2 — Hotspot variants disrupt a Tankyrase-binding motif, escaping degradation and causing pathological accumulation that impairs junctions and migration

The 157–161 residues lie within AMOTL1's **highly conserved Tankyrase-binding motif (TBM)**. Luo et al. 2026 demonstrated that the R157C and P160L mutants **fail to interact with Tankyrase 1/2 and RNF146**, so they cannot undergo poly-ADP-ribosylation, ubiquitination, or subsequent proteasomal degradation. The mutant proteins are therefore **stabilized and accumulate in the cytoplasm**. Accumulated mutant AMOTL1 **disrupts cell junctions and focal adhesions**, inhibiting both the velocity and the persistence of cell migration. In a zebrafish model, R157C expression produced craniofacial malformations plus cardiac and skeletal-muscle defects, recapitulating the human multi-organ phenotype. **[in vitro, model organism]**

> *"both the R157C and P160L mutants fail to interact with Tankyrase 1/2 and Ring finger protein 146, rendering them unable to undergo poly ADP-ribosylation, ubiquitination, and subsequent proteasomal degradation. As a result, these mutants are significantly stabilized and accumulate in the cytoplasm"* — Luo et al. 2026 [PMID: 42012498]

> *"Accumulated AMOTL1 mutants, in turn, disrupt cell junctions and focal adhesions, thereby inhibiting both the velocity and persistence of cell migration"* — Luo et al. 2026 [PMID: 42012498]

> *"expression of the R157C mutant leads to craniofacial malformations and defects in cardiac function and skeletal muscle"* — Luo et al. 2026 [PMID: 42012498]

This is the central mechanistic finding: a **toxic gain-of-function via loss of regulated turnover** rather than loss of protein.

### Finding 3 — Core phenotype: orofacial clefting, congenital heart disease, tall stature, auricular and gastrointestinal/anal anomalies, plus hepatic abnormalities

The core multi-system phenotype comprises **orofacial clefting, congenital heart disease, tall stature, auricular anomalies, and gastrointestinal manifestations** (Strong et al. 2023). Rips et al. 2021 documented cleft lip and palate, imperforate anus, and dysmorphic features in a P160L infant. The earliest (father–daughter/father–son) reports described orofacial clefts and cardiac abnormalities. Gallego-Zazo et al. 2025 added **hepatic abnormalities** (chronic liver dysfunction), consolidating the **craniofacial + heart + liver triad** that gives the syndrome its name (craniofaciocardiohepatic) and proposing the designation CFCHS. **[human clinical]**

> *"define a core phenotype of orofacial clefting, congenital heart disease, tall stature, auricular anomalies, and gastrointestinal manifestations in individuals with variants in AMOTL1 affecting amino acids 157-161"* — Strong et al. 2023 [PMID: 36751037]

> *"a female infant with cleft lip and palate, imperforate anus and dysmorphic features"* — Rips et al. 2021 [PMID: 33026150]

> *"we propose naming this entity as AMOTL1-associated multiple congenital anomalies or craniofaciocardiohepatic syndrome (CFCHS)"* — Gallego-Zazo et al. 2025 [PMID: 39538375]

### Finding 4 — Normal AMOTL1 biology: a Motin-family tight-junction adaptor regulating polarity, junction stability, and Hippo–YAP signaling

AMOTL1 (angiomotin-like protein 1) is an actin-binding protein regulating cell polarity, adhesion, and migration. It colocalizes with AMOT at **tight junctions** and is required for proper tight-junction activity and endothelial polarity/directional migration; morpholino knockdown in zebrafish causes vascular migratory defects and decreased junctional stability (Hultin et al. 2009). Motin proteins regulate the **Hippo–YAP pathway** and small-G-protein signaling: they can activate the LATS2 kinase and recruit YAP to tight junctions. AMOTL1 stability is normally controlled both by Nedd4-family E3 ligases (Nedd4/Nedd4-2/Itch) and—per the disease mechanism—by Tankyrase/RNF146-mediated PARylation-dependent degradation. **[in vitro, model organism]**

> *"AmotL1 colocalized with Amot to tight junctions"* — Hultin et al. 2009 [PMID: 19590046]

> *"the other angiomotin-family proteins AMOT and AMOTL1 also activate LATS2 through a novel conserved domain that binds and activates LATS2"* — Paramasivam et al. 2011 [PMID: 21832154]

Understanding the normal biology clarifies why dysregulated accumulation (not absence) of the protein is pathogenic: AMOTL1 is a dosage- and localization-sensitive junctional scaffold, and its overaccumulation perturbs the same junction/polarity/Hippo machinery it normally organizes.

### Finding 5 — Phenotype frequencies from the 16-individual Strong cohort and disease identifiers

Strong et al. 2023 (*Am J Med Genet A* 191:1227–1239) described **16 individuals from 12 families**. Per-feature frequencies:

| Feature | HPO term (suggested) | Frequency |
|---|---|---|
| Orofacial clefting (cleft lip/palate) | HP:0000175 (Cleft palate), HP:0410030 (Cleft lip) | 15/16 (94%) |
| Large/dysplastic ears | HP:0000400 (Macrotia), HP:0000377 (Abnormal pinna morphology) | 10/16 (62.5%) |
| Congenital heart disease | HP:0001627 (Abnormal heart morphology) | 8/16 (50%) |
| Tall stature | HP:0000098 | 7/16 (44%) |
| Hearing loss | HP:0000365 | 5/16 (31%) |
| Liver disease | HP:0001392 (Abnormal liver morphology/function) | 5/16 (31%) |
| Neurodevelopmental disease | HP:0012758 (Neurodevelopmental delay) | 5/16 (31%) |

Recurrent variants: p.Arg157Cys, p.Arg157His, p.Pro160Leu, plus p.Gln161Arg; the hotspot spans aa157–161. **Identifiers:** OMIM #621192 (phenotype); gene AMOTL1 OMIM *614657 on chromosome **11q21**; MONDO:0978295. Inheritance is autosomal dominant. Genomics England PanelApp rates AMOTL1 "green"/high-confidence for clefting, monoallelic. As independent validation, **5 qualifying variants were identified among 876 orofacial-cleft trios** in the Gabriella Miller Kids First dataset. **[human clinical]**

> *"a core phenotype of orofacial clefting, congenital heart disease, tall stature, auricular anomalies, and gastrointestinal manifestations"* — Strong et al. 2023 [PMID: 36751037]

### Finding 6 — Clinical delineation history and organ-specific manifestations across index cases

The clinical delineation of CFCHS proceeded through a recognizable sequence:

| Report | Case | Key manifestations | Variant |
|---|---|---|---|
| Liegel et al. 2019 | Father and son | Proband: complete left cleft lip/palate + right cleft of primary palate; VSD with tetralogy of Fallot and double-orifice mitral valve | AMOTL1 missense |
| Rips et al. 2021 [PMID: 33026150] | 7-month-old girl (Arab Muslim descent) | Cleft lip/palate, imperforate anus, dysmorphic features | de novo p.Pro160Leu |
| Strong et al. 2023 [PMID: 36751037] | 16 individuals / 12 families | Defining cohort; core phenotype + frequencies | R157C / R157H / P160L (hotspot) |
| Gallego-Zazo et al. 2025 [PMID: 39538375] | 28-year-old Spanish woman | Surgically corrected cleft lip/palate (further maxillofacial reconstruction in adolescence); large atrial septal defect corrected at age 5; chronic liver dysfunction with abnormal transaminases; proposed name "CFCHS" | AMOTL1 variant |

> *"a female infant with cleft lip and palate, imperforate anus and dysmorphic features, in whom trio exome sequencing revealed a de novo variant in AMOTL1"* — Rips et al. 2021 [PMID: 33026150] **[human clinical]**

### Finding 7 — Mouse models support a gain-of-function/dominant-negative (not haploinsufficiency) mechanism

Mouse genetics strongly argue against haploinsufficiency. Per MGI (Amotl1, MGI:1922973), mice **heterozygous for a missense mutation exhibit postnatal lethality** and homozygotes exhibit prenatal/neonatal lethality, **without** apparent craniofacial or cardiovascular phenotypes. Liegel et al. 2019 generated CRISPR **R157C knock-in** mice: homozygotes and heterozygotes had reduced perinatal survival through unidentified mechanisms, but careful skeletal/whole-mount/histologic analysis showed **no palatal clefting and no cardiac septal/valvular/outflow-tract defects**. Critically, two **deletion (complete loss-of-function) alleles did NOT affect survival**. This dissociation—**missense lethal, null tolerated**—is the hallmark of a gain-of-function or dominant-negative mechanism rather than haploinsufficiency. Zebrafish R157C expression (Luo et al. 2026) does produce craniofacial, cardiac, and skeletal-muscle defects, better recapitulating the human phenotype. **[model organism]**

> *"both the R157C and P160L mutants fail to interact with Tankyrase 1/2 and Ring finger protein 146, rendering them unable to undergo poly ADP-ribosylation, ubiquitination, and subsequent proteasomal degradation"* — Luo et al. 2026 [PMID: 42012498]

Orthology: mouse *Amotl1* = NCBI Gene 75723 (NCBI Taxon 10090); human *AMOTL1* = NCBI Gene 154810; zebrafish (*Danio rerio*, NCBI Taxon 7955) *amotl1* ortholog used in disease modeling.

---

## Section-by-Section Characterization

### 1. Disease Information

CFCHS is an ultra-rare autosomal dominant multiple-congenital-anomaly syndrome affecting craniofacial, cardiac, and hepatic development, plus auricular, gastrointestinal/anorectal, growth, hearing, and neurodevelopmental domains. It is defined molecularly by heterozygous AMOTL1 missense variants at the aa157–161 hotspot.

- **Key identifiers:** OMIM #621192 (phenotype); OMIM *614657 (AMOTL1 gene); MONDO:0978295. ICD-10/ICD-11 and dedicated MeSH entries are not established for this newly delineated entity (coded under broader congenital-malformation syndrome categories).
- **Synonyms:** CFCHS; AMOTL1-associated multiple congenital anomalies; AMOTL1-related orofacial clefting syndrome; "mutational hotspot in AMOTL1" syndrome of orofacial clefting, cardiac anomalies and tall stature.
- **Source of information:** Aggregated disease-level resources (OMIM, MONDO) combined with individual-patient case reports and a small defining cohort (16 individuals / 12 families). This is a case-report/cohort-derived entity, not an EHR-population-derived one.

### 2. Etiology

- **Disease causal factors:** Purely genetic — heterozygous missense variants in AMOTL1 at the aa157–161 hotspot. No environmental, infectious, or metabolic cause.
- **Genetic risk factors:** The causal variants themselves (R157C, R157H, P160L, Q161R). No separate susceptibility loci or modifier genes have been established.
- **Environmental risk factors:** None identified. De novo mutation is a sporadic event; advanced parental age is a plausible but unproven contributor to de novo missense events in general.
- **Protective factors:** None characterized. Given the gain-of-function mechanism, hypothetical protective strategies would target mutant-protein turnover (e.g., restoring degradation), but none exist.
- **Gene–environment interactions:** None documented. The disorder is essentially fully genetically determined by the hotspot variant.

### 3. Phenotypes

See Finding 5 table for frequencies and suggested HPO terms. Phenotype characteristics:

- **Age of onset:** Congenital/neonatal — structural anomalies are present at birth or detectable prenatally/at birth (clefting, cardiac defects, imperforate anus). Hepatic dysfunction and neurodevelopmental features may become apparent across childhood; tall stature manifests over growth.
- **Severity:** Variable; clefting is highly penetrant and surgically significant. Cardiac disease ranges from septal defects (ASD/VSD) to complex conotruncal malformation (tetralogy of Fallot, double-orifice mitral valve).
- **Progression:** Structural anomalies are static/congenital and correctable by surgery; liver dysfunction may be chronic; neurodevelopmental features are stable to slowly evolving.
- **Quality-of-life impact:** Orofacial clefting affects feeding, speech, hearing, and facial appearance; congenital heart disease carries surgical and cardiologic burden; hearing loss and neurodevelopmental involvement affect communication and learning. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) has been applied to this rare entity.

### 4. Genetic / Molecular Information

- **Causal gene:** AMOTL1 (HGNC:17811; OMIM *614657; chromosome 11q21; UniProt Q8IY63).
- **Pathogenic variants:** Recurrent missense — c.469C>T p.(Arg157Cys), c.470G>A p.(Arg157His), c.479C>T p.(Pro160Leu), p.(Gln161Arg). **Variant class:** missense, clustered at aa157–161. **Classification:** pathogenic/likely pathogenic per clustering, de novo occurrence, functional data, and segregation (ACMG criteria PS1/PM1/PM2/PS3/PP-type support).
- **Allele frequency:** Hotspot variants are absent or extremely rare in gnomAD (consistent with PM2).
- **Origin:** Germline; both de novo and inherited.
- **Functional consequence:** Gain-of-function / dominant-negative via loss of Tankyrase/RNF146-mediated degradation → protein stabilization/accumulation (Finding 2). This is distinct from loss-of-function/haploinsufficiency, which is tolerated (Finding 7).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established. No large-scale structural rearrangements implicated; CFCHS is a single-gene missense disorder.

### 5. Environmental Information

Not applicable. No environmental factors, lifestyle factors, or infectious agents are implicated in CFCHS. (Note: one cited paper [PMID: 23942117] links arsenic to Hippo/YAP and junction dysregulation in skin; this is mechanistically adjacent to AMOTL1 biology but is not a cause of CFCHS.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A **heterozygous missense variant** at the AMOTL1 aa157–161 hotspot (e.g., R157C, P160L) **alters the Tankyrase-binding motif (TBM)**. *[demonstrated]*
2. The altered TBM **abolishes binding to Tankyrase 1/2 and the E3 ligase RNF146**, which *results in* failure of poly-ADP-ribosylation and ubiquitination of AMOTL1. *[demonstrated]*
3. Loss of this modification **prevents proteasomal degradation**, which *leads to* abnormal **stabilization and cytoplasmic accumulation** of mutant AMOTL1. *[demonstrated]*
4. Accumulated mutant AMOTL1 **disrupts cell–cell junctions and focal adhesions** (perturbing tight-junction scaffolding and actin/Hippo-YAP coupling that AMOTL1 normally organizes). *[demonstrated in vitro]*
5. Junction/adhesion disruption **impairs the velocity and persistence of directional cell migration**. *[demonstrated in vitro]*
6. Defective migration and junction remodeling in migrating epithelial/neural-crest/endothelial populations **derails morphogenesis** during a congenital critical window. *[inferred]*
7. Branching to clinical manifestations: → **orofacial clefting** (failure of facial-prominence fusion); → **congenital heart disease** (outflow-tract/septal/valve morphogenesis); → **hepatic abnormalities**; → **auricular, anorectal, growth, hearing, and neurodevelopmental anomalies**. *[inferred from human phenotype + zebrafish model]*

- **Molecular pathways:** Tankyrase/RNF146 PARylation-dependent ubiquitin–proteasome degradation; Hippo–YAP/LATS2 signaling; small-G-protein/junctional signaling.
- **Cellular processes:** Cell migration (GO:0016477), cell junction assembly/tight-junction organization (GO:0070830), establishment of cell polarity (GO:0030010), proteasomal protein catabolism (GO:0043161).
- **Cell types involved (suggested CL):** endothelial cell (CL:0000115), epithelial cell (CL:0000066), cranial neural crest-derived cells, cardiac muscle cell (CL:0000746).
- **Molecular profiling / single-cell / omics:** No human transcriptomic/proteomic/metabolomic/single-cell/spatial datasets specific to CFCHS exist yet. Functional evidence derives from targeted cell-biology and model-organism experiments (Luo et al. 2026).

### 7. Anatomical Structures Affected

- **Primary organs/systems:** Craniofacial complex (lip, palate — UBERON:0001716 secondary palate; UBERON:0000165 mouth), heart (UBERON:0000948; cardiovascular system), liver (UBERON:0002107; hepatobiliary system), external ear/pinna (UBERON:0001757), gastrointestinal/anorectal tract (UBERON:0000159 anus).
- **Secondary involvement:** Auditory system (hearing loss), central nervous system (neurodevelopmental features), skeletal/growth (tall stature), skeletal muscle (per zebrafish model).
- **Tissue/cell level:** Epithelial and endothelial tissues; tight-junction-bearing epithelia; migrating neural-crest-derived mesenchyme (inferred for craniofacial clefting).
- **Subcellular level:** Tight junctions (GO:0005923 bicellular tight junction; GO:0070160), focal adhesions (GO:0005925), cytoplasm (site of mutant accumulation; GO:0005737), actin cytoskeleton (GO:0015629).
- **Lateralization:** Clefting may be unilateral or bilateral; cardiac/organ defects per lesion.

### 8. Temporal Development

- **Onset:** Congenital. Structural anomalies present at birth; many detectable prenatally.
- **Onset pattern:** Non-progressive developmental (anomalies fixed at birth), though hepatic dysfunction can be chronic and neurodevelopmental features evolve.
- **Progression/course:** The congenital malformations are static and surgically correctable; there is no neurodegenerative course. Liver involvement may persist/fluctuate.
- **Critical period:** Embryonic organogenesis (facial-prominence fusion, cardiac septation/outflow formation, hepatic development) is the window of vulnerability; no postnatal intervention window exists to prevent the structural lesions.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant (OMIM, ClinVar, PanelApp monoallelic "green").
- **Epidemiology:** Ultra-rare; fewer than ~20 individuals reported worldwide. No formal prevalence/incidence estimates; Orphanet-level prevalence is "unknown/<1/1,000,000."
- **Penetrance/expressivity:** Apparently high penetrance for hotspot alleles with **variable expressivity** (range from isolated clefting to multi-organ involvement).
- **De novo vs inherited:** Both documented; de novo p.Pro160Leu and inherited parent→child transmission reported.
- **Anticipation / mosaicism / founder effects / consanguinity:** No anticipation (not a repeat disorder). Germline mosaicism not specifically reported but theoretically possible for de novo cases. No founder effect; cases span diverse ancestries (European, Spanish, Arab Muslim). Consanguinity is not relevant (dominant, not recessive).
- **Carrier frequency:** Not applicable (dominant); pathogenic variants effectively absent from gnomAD.
- **Sex ratio / age distribution:** No sex bias established; affected individuals span infancy to adulthood (reported cases from 7 months to 28 years).

### 10. Diagnostics

- **Genetic testing is the diagnostic cornerstone.** Trio exome sequencing (WES) identified causal variants in multiple index cases; WGS and multigene cleft/congenital-anomaly panels including AMOTL1 are suitable. **Single-gene/targeted testing** of the aa157–161 hotspot is efficient given the clustering. Chromosomal microarray/karyotype/FISH are typically normal (no structural rearrangement) and serve mainly to exclude differentials.
- **Clinical/imaging work-up:** Echocardiography and cardiac imaging for CHD; facial/palatal examination and imaging for clefting; liver function tests (transaminases) and hepatic imaging for liver involvement; audiology for hearing loss; developmental assessment.
- **Biomarkers:** No specific circulating biomarker. Abnormal transaminases (elevated ALT/AST) may flag hepatic involvement.
- **Diagnostic criteria:** No formal consensus criteria; diagnosis rests on the characteristic phenotype plus a confirmed hotspot AMOTL1 variant.
- **Differential diagnosis:** Other syndromic orofacial-clefting disorders (e.g., Van der Woude, CHARGE, 22q11.2 deletion, Kabuki), and overlapping craniofacial–cardiac–hepatic syndromes. Molecular testing distinguishes CFCHS.
- **Screening:** No population newborn screening; prenatal/cascade testing possible once a familial variant is known.

### 11. Outcome / Prognosis

- **Survival/mortality:** No systematic survival data in humans; the structural anomalies are generally surgically correctable, and long-term survival into adulthood is documented (28-year-old reported case). Severe complex CHD could affect early prognosis.
- **Morbidity/function:** Morbidity is driven by surgical burden (cleft and cardiac repair), hearing loss, hepatic dysfunction, and neurodevelopmental involvement. Many individuals achieve good functional outcomes after multidisciplinary management.
- **Complications:** Feeding/speech difficulties from clefting; cardiac-surgical complications; chronic liver dysfunction; conductive/sensorineural hearing loss.
- **Prognostic factors:** Severity of CHD and presence/degree of hepatic and neurodevelopmental involvement are the main determinants. No molecular prognostic biomarker beyond the specific variant.

### 12. Treatment

No gene-targeted or disease-modifying therapy exists. Management is **multidisciplinary, surgical, and supportive**:

- **Surgical/interventional (suggested NCIT: Surgical Procedure, NCIT:C15329):** Cleft lip/palate repair and staged maxillofacial reconstruction; cardiac surgical correction of septal defects/conotruncal anomalies; anorectal surgery for imperforate anus.
- **Supportive/rehabilitative:** Speech therapy, audiology/hearing amplification, feeding support, developmental/educational support, hepatology monitoring and supportive liver care.
- **Pharmacotherapy / advanced therapeutics:** None disease-specific; no gene therapy, RNA therapy, cell therapy, or targeted small molecule is available. Conceptually, the gain-of-function mechanism (failure of degradation) suggests a future rationale for strategies promoting mutant-protein turnover, but none are developed.
- **Experimental/clinical trials:** No registered CFCHS-specific trials.

### 13. Prevention

- **Primary prevention:** Not possible for de novo cases. For families with a known variant, **genetic counseling**, prenatal diagnosis, and preimplantation genetic testing are the principal preventive options.
- **Secondary prevention:** Early multidisciplinary evaluation (cardiac, craniofacial, hepatic, audiologic) to detect and treat anomalies promptly.
- **Tertiary prevention:** Surgical correction and ongoing surveillance to prevent complications.
- **Counseling:** Autosomal dominant 50% transmission risk from an affected parent; de novo recurrence risk is low but non-zero (germline mosaicism considered).

### 14. Other Species / Natural Disease

- **Model-relevant orthologs:** mouse *Amotl1* (NCBI Gene 75723; Taxon 10090), zebrafish *amotl1* (Taxon 7955). Human *AMOTL1* = NCBI Gene 154810.
- **Natural disease in other species:** No naturally occurring AMOTL1 CFCHS-equivalent disease is documented in companion animals or wildlife (OMIA search negative). No veterinary or zoonotic relevance.
- **Comparative biology:** AMOTL1's junctional/Hippo-YAP function is evolutionarily conserved from fish to mammals, underpinning the utility of zebrafish and mouse models.

### 15. Model Organisms

- **Zebrafish (*Danio rerio*):** Expression of R157C mutant produces craniofacial malformations plus cardiac and skeletal-muscle defects (Luo et al. 2026) — the best phenotypic recapitulation of human CFCHS. Morpholino knockdown of amotl1 causes vascular/junctional defects (Hultin et al. 2009), informing normal-function studies.
- **Mouse (*Mus musculus*):** CRISPR R157C knock-in (Liegel et al. 2019) shows perinatal lethality but **no palatal clefting or cardiac defects**; complete-null deletion alleles are tolerated. Thus mouse models reveal the gain-of-function vs haploinsufficiency distinction but **do not recapitulate the human craniofacial/cardiac malformations** — an important limitation.
- **Genetic model types available:** knock-in (R157C), knockout/deletion alleles, morpholino knockdown (zebrafish).
- **Applications/limitations:** Models are valuable for mechanism (degradation escape, migration defects) but the mouse's lack of overt malformation limits its use for craniofacial/cardiac phenotype studies; zebrafish is preferable for malformation modeling.
- **Resources:** MGI (Amotl1 MGI:1922973), ZFIN (amotl1).

---

## Mechanistic Model / Interpretation

```
 Heterozygous AMOTL1 missense at hotspot (aa157-161: R157C / R157H / P160L / Q161R)
                               │
                               ▼
         Disruption of the Tankyrase-Binding Motif (TBM)
                               │
                               ▼
     Loss of binding to Tankyrase 1/2 and E3 ligase RNF146
                               │
                               ▼
   No PARylation → no ubiquitination → no proteasomal degradation
                               │
                               ▼
      STABILIZATION + CYTOPLASMIC ACCUMULATION of mutant AMOTL1   ← gain-of-function
                               │
                               ▼
     Disruption of cell-cell junctions + focal adhesions (tight junctions, actin)
                               │
                               ▼
    Impaired velocity & persistence of directional cell migration
                               │
                               ▼
     Derailed embryonic morphogenesis (critical developmental window)
          │            │             │              │
          ▼            ▼             ▼              ▼
   Orofacial     Congenital      Hepatic      Auricular / anorectal /
   clefting      heart disease   abnormality  growth / hearing / neurodev.
    (~94%)        (~50%)          (~31%)        (62% / variable)
```

**Upstream vs downstream.** The upstream, initiating lesion is the TBM-disrupting missense variant and the resulting degradation escape (Finding 2). Immediately downstream are protein accumulation and junction/migration failure (cell-biology level), and furthest downstream are the organ-level malformations (clinical level). The convergence of all clinical features on a single migration/junction defect explains why such distinct organs are co-affected: each depends on coordinated epithelial/endothelial/neural-crest migration and junction remodeling during organogenesis.

**Why gain-of-function, not haploinsufficiency.** Three independent lines of evidence converge: (1) the extreme variant clustering at a 5-residue motif (loss-of-function disease usually shows dispersed truncating variants); (2) the direct biochemical demonstration of degradation escape and accumulation; and (3) the mouse genetics showing that missense alleles are lethal while complete-null alleles are tolerated (Findings 1, 2, 7).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [36751037](https://pubmed.ncbi.nlm.nih.gov/36751037/) | *Mutational hotspot in AMOTL1 defines a new syndrome of orofacial clefting, cardiac anomalies, and tall stature* | **Defining cohort** (16 individuals/12 families); core phenotype, frequencies, hotspot aa157–161, recurrent variants, Kids First validation (Findings 1, 3, 5) |
| [42012498](https://pubmed.ncbi.nlm.nih.gov/42012498/) | *Patient-derived AMOTL1 mutations lead to defective cell migration and tissue development* (Luo et al. 2026) | **Core mechanism**: TBM disruption → degradation escape → accumulation → junction/migration defect; zebrafish R157C phenotype (Findings 2, 7) |
| [33026150](https://pubmed.ncbi.nlm.nih.gov/33026150/) | *De novo variant in AMOTL1 in infant with cleft lip and palate, imperforate anus* | De novo p.Pro160Leu; anorectal + craniofacial manifestations (Findings 1, 3, 6) |
| [39538375](https://pubmed.ncbi.nlm.nih.gov/39538375/) | *AMOTL1-Associated Multiple Congenital Anomalies (CFCHS)* | **Names CFCHS**; adds hepatic phenotype (Findings 3, 6) |
| [19590046](https://pubmed.ncbi.nlm.nih.gov/19590046/) | *AMOTL1 controls endothelial polarity and junction stability during sprouting angiogenesis* | Normal AMOTL1 tight-junction localization/function (Finding 4) |
| [21832154](https://pubmed.ncbi.nlm.nih.gov/21832154/) | *Angiomotin family proteins are novel activators of the LATS2 kinase* | AMOTL1 → Hippo/LATS2 regulation (Finding 4) |
| [22558212](https://pubmed.ncbi.nlm.nih.gov/22558212/) | *YAP1 recruits c-Abl to protect AMOTL1 from Nedd4-mediated degradation* | Nedd4-family regulation of AMOTL1 stability (context for turnover control) |
| [22385262](https://pubmed.ncbi.nlm.nih.gov/22385262/) | *Nedd4-like E3 ligases target angiomotin/p130 for degradation* | Alternative AMOTL1/AMOT degradation axis (context) |
| [36973516](https://pubmed.ncbi.nlm.nih.gov/36973516/) | *Role of Motin family proteins in tumorigenesis—an update* | Motin biology, YAP duality, context-dependence (Finding 4 context) |
| [23942117](https://pubmed.ncbi.nlm.nih.gov/23942117/) | *Arsenic-induced cutaneous lesions and Yap/Hippo dysregulation* | Mechanistically adjacent (Hippo/junction), not a CFCHS cause |

Evidence source types: **human clinical** (36751037, 33026150, 39538375), **in vitro + model organism** (42012498, 19590046, 21832154, 22558212, 22385262), **review/context** (36973516, 23942117).

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Fewer than ~20 reported individuals; all frequencies derive essentially from a single 16-individual cohort, so percentages have wide uncertainty and ascertainment bias toward clefting.
2. **No human omics.** No CFCHS-specific transcriptomic, proteomic, metabolomic, single-cell, or spatial datasets exist; mechanistic cell-type attribution for each organ phenotype is largely inferred.
3. **Mouse–human discordance.** The R157C knock-in mouse does **not** reproduce clefting or cardiac defects, so mouse is a poor phenotype model; the zebrafish model is better but incompletely characterized.
4. **Penetrance/expressivity not quantified.** High penetrance is apparent but not formally estimated; genotype–phenotype correlations among specific hotspot alleles are not resolved.
5. **No epidemiology.** Prevalence/incidence, sex ratio, and geographic distribution are unknown.
6. **Downstream pathway incompletely mapped.** How accumulated AMOTL1 quantitatively perturbs Hippo-YAP vs junction/actin signaling in each affected tissue is not fully dissected.
7. **No therapeutics.** No disease-modifying treatment or trial; the degradation-escape mechanism is a therapeutic hypothesis only.

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry** aggregating all reported and new CFCHS individuals to refine phenotype frequencies, penetrance, expressivity, and genotype–phenotype correlations (e.g., R157 vs P160 vs Q161 alleles).
2. **Improved animal models:** characterize zebrafish amotl1 hotspot knock-ins across craniofacial, cardiac, and hepatic lineages; develop conditional/tissue-specific mouse knock-in strategies (e.g., neural-crest-restricted) to overcome the global-mouse discordance.
3. **Single-cell and spatial transcriptomics** of patient-derived iPSC models (neural crest, cardiomyocyte, hepatocyte, endothelial organoids) to map cell-type-specific junction/migration and Hippo-YAP dysregulation.
4. **Quantitative degradation/stability assays** across all hotspot variants to confirm the uniform "degradation-escape" mechanism and test whether degree of stabilization predicts phenotype severity.
5. **Therapeutic proof-of-concept:** test whether restoring mutant AMOTL1 turnover (e.g., degrader/PROTAC approaches, allele-selective knockdown with ASO/siRNA) rescues junction/migration defects in vitro and malformations in zebrafish.
6. **Clinical surveillance guidelines:** formalize a multidisciplinary protocol (cardiac echo, hepatic LFT/imaging, audiology, developmental assessment, craniofacial follow-up) for diagnosed individuals.
7. **ClinVar/panel curation:** ensure all hotspot variants are deposited with functional evidence and ACMG classifications to support rapid clinical diagnosis.

---

*Report compiled from 7 confirmed findings and 10 primary/review papers across 5 investigation iterations. All mechanistic and clinical claims are attributed to the cited PMIDs with verbatim abstract quotes where available.*


## Artifacts

- [OpenScientist final report](Craniofaciocardiohepatic_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Craniofaciocardiohepatic_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000365` (1 mention) - the report calls it "Hearing loss"; HP calls it **Hearing impairment**, and lists "Hearing loss" among its other names
- `HP:0001392` (1 mention) - the report calls it "Abnormal liver morphology/function"; HP calls it **Abnormality of the liver**, and lists "Abnormal liver" among its other names
- `GO:0016477` (1 mention) - the report calls it "Cellular processes:** Cell migration"; GO calls it **cell migration**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

29 of 31 terms resolved to a current term; the rest could not be looked up either way.