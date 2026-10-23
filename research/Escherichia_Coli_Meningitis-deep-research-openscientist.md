---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T21:03:58.905126'
end_time: '2026-09-29T21:20:20.742729'
duration_seconds: 981.84
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Escherichia coli meningitis
  mondo_id: MONDO:0006753
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
citation_count: 39
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 15
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:23178136
  relevance_assessed: 39
  on_topic: 27
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: UBERON:0002361
    reported_labels:
    - "Primary organ:** brain and meninges \u2014 **leptomeninges"
    ontology_label: pia mater
  - term_id: UBERON:0002360
    reported_labels:
    - Body system:** central nervous system / **meninges
    ontology_label: meninx
  - term_id: NCIT:C376
    reported_labels:
    - "Empirical:** third-generation cephalosporins \u2014 **cefotaxime"
    ontology_label: Cisplatin
  - term_id: NCIT:C1352
    reported_labels:
    - Resistant strains:** **meropenem
    ontology_label: Recombinant Brain-Derived Growth Factors
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0051092
    ontology_label: obsolete positive regulation of NF-kappaB transcription factor
      activity
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Escherichia_Coli_Meningitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Escherichia_Coli_Meningitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Escherichia coli meningitis
- **MONDO ID:** MONDO:0006753 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Escherichia coli meningitis** covering all of the
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

# Escherichia coli Meningitis — Comprehensive Disease Characteristics Report

**Disease:** *Escherichia coli* meningitis
**MONDO ID:** MONDO:0006753
**Category:** Infectious Disease
**Report type:** Disease knowledge base entry (multi-iteration autonomous literature synthesis)

---

## Summary

*Escherichia coli* meningitis is an acute bacterial infection of the meninges and cerebrospinal fluid (CSF) that is, worldwide, the **leading Gram-negative cause of neonatal bacterial meningitis**. The overwhelming majority of neonatal cases are caused by a specialized pathotype — **neonatal-meningitis *E. coli* (NMEC)** — that carries the **K1 capsular polysaccharide** and belongs predominantly to **extraintestinal pathogenic *E. coli* (ExPEC) phylogroup B2, sequence-type complex 95 (ST95)**, serotypes O18:K1, O1:K1, and O2:K1. Approximately 80% of neonatal-meningitis *E. coli* express the K1 capsule. In contemporary early-onset neonatal meningitis cohorts, *E. coli* and Group B *Streptococcus* (GBS) are co-predominant, with one 20-year cohort attributing 37.1% of blood-culture-positive cases to *E. coli* [PMID: 42661190].

The pathogenesis follows a well-defined causal chain. The K1 sialic-acid capsule confers resistance to the **alternative complement pathway**, enabling the bacterium to achieve and sustain **high-grade bacteremia**. A threshold level of bacteremia leads to **receptor-mediated transcytosis across the blood-brain barrier (BBB)** at the level of human brain microvascular endothelial cells (HBMEC), mediated by at least three independent invasin–receptor–signaling modules: **OmpA→Ecgp96(gp96)→PI3K**, **CNF1→37LRP→RhoA**, and **IbeA→vimentin/PSF→ERK–NF-κB**. Crucially, bacterial entry occurs by **transcellular transcytosis without initial disruption of endothelial tight junctions**. Downstream, invasion triggers **RIPK1/ripoptosome-dependent regulated endothelial cell death** (coordinated apoptosis, pyroptosis, and necroptosis) together with **neutrophil (PMN) transmigration** driven by IbeA/vimentin and upregulated ICAM-1/CD44, culminating in **BBB breakdown, neuroinflammation, and neuronal injury**.

Despite modern antimicrobial therapy (third-generation cephalosporins ± aminoglycoside or meropenem for resistant strains), outcomes remain poor: **mortality of 12% (term) to 18% (preterm)**, with **long-term neurosensorial sequelae in 14–17%** and **neurodevelopmental sequelae in 10–17%** of survivors. Ampicillin resistance is high (~78%), and ESBL/ST131 clones threaten empirical regimens. **No licensed vaccine exists**; the conserved surface polysaccharide **PNAG** and **OmpA** are the leading experimental candidates, both showing proof-of-concept protection in neonatal mouse models. This report organizes 14 confirmed findings across the 15 requested disease-characteristic domains.

---

## 1. Disease Information

**Overview.** *E. coli* meningitis is an acute pyogenic (purulent) bacterial meningitis caused by the Gram-negative bacillus *Escherichia coli*. It is predominantly a **disease of the neonate** (birth–28 days, extending to young infants <90 days), although it also occurs in older adults, immunocompromised hosts, and as a nosocomial/post-neurosurgical complication (e.g., ventriculoperitoneal shunts, transsphenoidal surgery). It is the leading Gram-negative bacterial cause of neonatal meningitis worldwide [PMID: 36709579].

> "Worldwide, Escherichia coli is the leading cause of neonatal Gram-negative bacterial meningitis, but full understanding of the pathogenesis of this disease is not yet achieved." — [PMID: 36709579](https://pubmed.ncbi.nlm.nih.gov/36709579/)

**Key identifiers.**
- **MONDO:** MONDO:0006753
- **MeSH:** *Meningitis, Escherichia coli* (a subtype under *Meningitis, Bacterial* / *Central Nervous System Bacterial Infections*)
- **ICD-10:** G00.8 (Other bacterial meningitis); P36/P37 codes apply in neonatal sepsis/congenital-infection contexts
- **ICD-11:** 1D00 (Bacterial meningitis) with an *E. coli* causal extension code
- **OMIM / Orphanet:** Not a Mendelian disorder; no OMIM phenotype number. Not assigned a distinct Orphanet rare-disease number (infectious, not genetic).

**Synonyms / alternative names.** *Escherichia coli* meningitis; *E. coli* meningitis; neonatal *E. coli* meningitis; *E. coli* K1 meningitis; Gram-negative enteric bacillary meningitis (when grouped); neonatal-meningitis *E. coli* (NMEC) infection of the CNS.

**Information source type.** This knowledge base entry is derived from **aggregated disease-level resources** — population-based surveillance, retrospective cohorts, mechanistic in vitro (HBMEC) and animal-model studies, and reviews — rather than individual EHR-level patient records.

---

## 2. Etiology

**Primary cause (infectious).** The disease is caused by infection with *Escherichia coli*, chiefly the **K1-encapsulated NMEC pathotype**. K1 strains account for ~80% of neonatal-meningitis *E. coli*.

> "Escherichia coli K1 is the leading cause of neonatal gram-negative bacterial meningitis, but the pathogenesis of E coli K1 meningitis remains unclear." — [PMID: 38531686](https://pubmed.ncbi.nlm.nih.gov/38531686/)

**Risk factors (host / environmental).**
- **Prematurity** (OR 5.84, 95% CI 2.02–16.85) and **low birth weight** (OR 8.48, 95% CI 2.60–27.69) are strong independent risk factors for death in neonatal bacterial meningitis [PMID: 29384979].
- **Neonatal age** itself — an immature immune system and immature/permeable BBB.
- **Maternal genitourinary/intestinal colonization** with ExPEC (vertical transmission) driving early-onset disease; nosocomial acquisition for late-onset disease.
- **Twin/multiple gestation** — shared exposure and genetic factors increase risk; twin concordance ~35% in cohort/surveillance studies [PMID: 42497927].
- **Neurosurgical devices / procedures** in older patients (VP shunts, transsphenoidal surgery, CSF leak, diabetes) [PMID: 29191537; PMID: 34522514].
- **Immunocompromise** in adults (community-acquired *E. coli* meningoencephalitis/brain abscess) [PMID: 40809603].

**Genetic risk factors (host).** No established Mendelian human susceptibility gene is specific to *E. coli* meningitis. Host susceptibility is essentially **non-genetic**, driven by developmental immaturity. (In an animal model, loss of **Trefoil Factor 2 (Tff2)** sensitized rat pups to systemic *E. coli* K1 infection [PMID: 30833331] — a model finding, not a validated human risk locus.) The critical "genetics" of this disease reside in the **pathogen genome** (virulence-gene repertoire; see Section 4).

**Protective factors.** Specific anti-K1/anti-capsular antibody protects against complement-resistant bacteremia (the K1 capsule evades complement only *in the absence* of specific antibody) [PMID: 6196296]. In a small twin subgroup, **pre-emptive antibiotics** for a well-appearing co-twin were associated with lower disease risk (11% vs 56%, p=0.03) [PMID: 42497927]. A probiotic *Bifidobacterium* mixture prevented neonatal *E. coli* K1 translocation in a model system [PMID: 28979247].

**Gene–environment interactions.** The dominant interaction is between **pathogen virulence genotype** (K1 capsule, *ompA*, *cnf1*, *ibeA*, GimA island) and the **host developmental window** (neonatal BBB permeability, immature complement/antibody repertoire). No classical human GxE locus is defined.

---

## 3. Phenotypes

Neonatal *E. coli* meningitis presents **nonspecifically**; classic meningeal signs are frequently absent. In a UK/Ireland population-based cohort of infants <90 days (n=263 with clinical data) [PMID: 29384979]:

| Phenotype (HPO suggestion) | Frequency | Type |
|---|---|---|
| Fever (HP:0001945) | 54% | Symptom/sign |
| Seizures (HP:0001250) | 28% | Clinical sign |
| Bulging anterior fontanelle (HP:0004474 / HP:0005484) | 22% | Physical sign |
| Coma / reduced consciousness (HP:0001259) | 6% | Clinical sign |
| Nuchal rigidity / neck stiffness (HP:0031179) | 3% | Clinical sign |

> "Fever was reported in 143 (54%), seizures in 73 (28%), bulging fontanelle in 58 (22%), coma in 15 (6%) and neck stiffness in 7 (3%)." — [PMID: 29384979](https://pubmed.ncbi.nlm.nih.gov/29384979/)

Other reported features include lethargy, poor feeding/failure to suck, temperature instability, apnea, irritability, and hypotonia. **Laboratory abnormalities (CSF):** neutrophilic pleocytosis, elevated CSF protein, and **low CSF glucose (hypoglycorrhachia)** (LOINC panels for CSF cell count, protein, glucose) — e.g., a severe example with CSF protein 572 mg/dL and glucose 9.5 mg/dL with abundant PMNs [PMID: 22090305].

- **Age of onset:** neonatal (early-onset ≤72 h; late-onset >72 h to ~28 days; extends to <90 days).
- **Severity:** severe, life-threatening.
- **Progression:** acute; can be fulminant with rapid deterioration.
- **Quality-of-life impact:** survivors frequently suffer hearing loss, epilepsy, cerebral palsy, hydrocephalus, and neurodevelopmental impairment, with major lifelong QoL burden. In the UK/Ireland cohort, 23% of survivors had serious CNS complications at discharge [PMID: 29384979].

Suggested HPO terms for complications: **Hydrocephalus (HP:0000238)**, **Brain abscess (HP:0031845)**, **Ventriculitis**, **Sensorineural hearing impairment (HP:0000407)**, **Cerebral palsy (HP:0100021)**, **Global developmental delay (HP:0001263)**.

---

## 4. Genetic/Molecular Information

Because this is an **infectious**, not inherited, disease, the relevant "genetics" are **bacterial virulence genes**, not human germline variants. There are **no causal human genes, pathogenic ACMG/AMP variants, allele frequencies, modifier genes, chromosomal abnormalities, or germline/somatic classifications** applicable to disease causation. (This section is explicitly *not applicable* in the classical Mendelian sense for a bacterial infection.)

**Key bacterial virulence determinants (the effective "molecular genetics" of NMEC):**

| Gene / locus | Product | Role | Evidence |
|---|---|---|---|
| *kpsMT* / *neu* (K1 capsule) | K1 polysialic acid capsule | Complement (alternative pathway) evasion → bacteremia | [PMID: 6196296] |
| *ompA* | Outer membrane protein A | Binds Ecgp96/gp96 → PI3K → invasion | [PMID: 12860457; PMID: 24932957] |
| *cnf1* | Cytotoxic necrotizing factor-1 | Binds 37LRP → RhoA activation → BBB traversal | [PMID: 11877402; PMID: 12860457] |
| *ibeA* (GimA island) | Invasion protein IbeA | Binds vimentin/PSF → ERK–NF-κB → invasion + PMN transmigration | [PMID: 20088823; PMID: 22536447; PMID: 21083634] |
| *ibeB*, *yijP* | Invasion loci | Contribute to endothelial invasion | [PMID: 11008113] |
| *ompT* | Outer membrane protease T | Adherence/invasion; virulence (APEC/NMEC) | [PMID: 28199899] |
| *rpoE* | Sigma-E stress factor | Stress resistance, invasion, pathogenicity | [PMID: 35630325] |
| PNAG synthesis (*pga* locus) | Poly-β-(1-6)-N-acetylglucosamine | Surface polysaccharide; virulence & vaccine target | [PMID: 36709579] |

**Phylogenomic background.** NMEC belong predominantly to **phylogroup B2** and **ST complex 95**; among 28 US early-onset sepsis/meningitis isolates, B2 predominated (68%), of which 53% were K1-encapsulated, with phylogroup D also present (18%) [PMID: 26407251].

> "phylogroup B2 strains predominated (68%), of which more than half were K1-encapsulated (53%)" — [PMID: 26407251](https://pubmed.ncbi.nlm.nih.gov/26407251/)

**Epigenetic / chromosomal (host):** Not applicable.

---

## 5. Environmental Information

- **Infectious agent (NCBI Taxonomy):** *Escherichia coli* (**NCBI:txid562**); pathotype NMEC; predominant capsular type **K1**; serotypes O18:K1:H7 (prototype strain RS218), O1:K1, O2:K1.
- **Environmental / lifestyle factors:** Not a toxin- or lifestyle-driven disease. Relevant "environmental" exposures are **maternal colonization**, **perinatal transmission**, **hospital/device exposure** (VP shunts, external ventricular drains, post-neurosurgical), and **contaminated water/equipment** in nosocomial neonatal settings.
- **Reservoir / transmission:** Maternal gastrointestinal and genitourinary tract; vertical transmission perinatally; horizontal/nosocomial acquisition for late-onset disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **NMEC colonizes** the neonatal gut/mucosa and **enters the bloodstream** (vertical/perinatal acquisition). → leads to
2. **K1 sialic-acid capsule impedes activation of the alternative complement pathway** (in the absence of specific antibody), protecting the bacterium from complement-mediated killing [PMID: 6196296]. → results in
3. **High-grade, sustained bacteremia** — a threshold magnitude of bacteremia is required for CNS entry (inferred from newborn-rat models) [PMID: 6196296]. → leads to
4. **Bacterial binding to human brain microvascular endothelial cells (HBMEC)** at the BBB via multiple invasin–receptor pairs. This branches into **three independent signaling modules**:
   - **4a. OmpA → Ecgp96 (gp96, HSP90-family) → PI3K activation** (no effect on RhoA); requires GlcNAc1-4GlcNAc N-glycan epitopes on Ecgp96 [PMID: 12860457; PMID: 24932957].
   - **4b. CNF1 → 37-kDa laminin receptor (37LRP) → RhoA activation** (no effect on PI3K); required for BBB traversal in vivo [PMID: 11877402; PMID: 12860457].
   - **4c. IbeA → vimentin (primary receptor) + PSF (co-receptor) → CaMKII-mediated vimentin Ser82 phosphorylation, ERK phosphorylation, lipid-raft/caveolin-1 → NF-κB nuclear translocation** [PMID: 20088823; PMID: 22536447]. → each results in
5. **Actin cytoskeletal rearrangement and receptor-mediated endocytosis** → **transcellular transcytosis of *E. coli* across the endothelial monolayer WITHOUT initial tight-junction disruption** [PMID: 11008113]. (Ancillary node: OmpA–Ecgp96 engagement upregulates GTP-cyclohydrolase-1 (GCH1)/biopterin/NO synthesis, promoting invasion — inferred from inhibitor studies [PMID: 23100563].) → leads to
6. **Bacterial entry into the CSF/subarachnoid space** and replication, plus **IbeA/vimentin-driven neutrophil (PMN) transendothelial migration** with upregulation of ICAM-1 and CD44 [PMID: 21083634]. → results in
7. **RIPK1-kinase-dependent assembly of the ripoptosome** in brain endothelial cells, driving **coordinated apoptosis, pyroptosis, and necroptosis** [PMID: 40774959]. → leads to
8. **BBB disruption, vasogenic edema, neuroinflammation, and neuronal injury** → clinical meningitis (fever, seizures, bulging fontanelle, coma) and, downstream, **cerebral abscess, ventriculitis, hydrocephalus, and neurodevelopmental sequelae**.

> "OmpA treatment of human BMEC resulted in phosphatidylinositol 3-kinase (PI3K) activation with no effect on RhoA, while CNF1 treatment resulted in RhoA activation with no effect on PI3K..." — [PMID: 12860457](https://pubmed.ncbi.nlm.nih.gov/12860457/)

> "vimentin is a primary receptor required for IbeA+ E. coli K1-induced signalling and invasion of HBMECs" — [PMID: 20088823](https://pubmed.ncbi.nlm.nih.gov/20088823/)

> "RS218 infection promotes assembly of the Ripoptosome complex. This leads to the coordinated activation of apoptosis, pyroptosis, and necroptosis." — [PMID: 40774959](https://pubmed.ncbi.nlm.nih.gov/40774959/)

### Upstream vs downstream

- **Upstream (bacterial-side, initiating):** K1 capsule complement evasion; bacteremia magnitude.
- **Midstream (host–pathogen interface):** invasin–receptor engagement and transcytosis (OmpA/Ecgp96, CNF1/37LRP, IbeA/vimentin).
- **Downstream (host tissue injury):** ripoptosome-driven endothelial death, PMN transmigration, cytokine/NF-κB inflammation, BBB breakdown.

### Molecular pathways, processes, and ontology suggestions

- **Pathways:** PI3K–AKT (OmpA arm), RhoA/Rho-kinase (CNF1 arm), ERK–MAPK → NF-κB (IbeA arm), RIPK1/RIPK3–MLKL necroptosis and caspase-driven apoptosis/pyroptosis.
- **GO biological processes:** transcytosis (GO:0045056); regulation of Rho protein signal transduction (GO:0035023); positive regulation of NF-κB transcription factor activity (GO:0051092); necroptotic process (GO:0070266); pyroptosis (GO:0070269); leukocyte transendothelial migration (GO:0050900); inflammatory response (GO:0006954).
- **GO cellular components:** membrane raft (GO:0045121); intermediate filament / vimentin.
- **CL cell types:** brain microvascular endothelial cell (**CL:1001509**), neutrophil (**CL:0000775**), macrophage (**CL:0000235**), neuron (**CL:0000540**).

**Immune involvement:** NF-κB-driven pro-inflammatory cascade, PMN recruitment; the K1 capsule and OmpA engage innate evasion (complement; FcγRI/CD64 on macrophages [PMID: 26407066]). **Metabolic node:** GCH1/biopterin/NO (BH4 pathway) [PMID: 23100563]; CsiR→ilvB→FAK/PI3K under low-iron conditions promotes invasion [PMID: 38531686].

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Primary organ:** brain and meninges — **leptomeninges (UBERON:0002361)**, **subarachnoid space (UBERON:0002420)**, **cerebrospinal fluid (UBERON:0001359)**.
- **Body system:** central nervous system / **meninges (UBERON:0002360)**.
- **Secondary involvement:** cerebral cortex and hippocampus (microvessels show increased glycosylated Ecgp96 in infected mice [PMID: 24932957]); cerebral ventricles (**ventriculitis**), brain parenchyma (**cerebral abscess**), and systemic bloodstream (bacteremia/sepsis). Hydrocephalus and ischemo-hemorrhagic lesions are described complications [PMID: 23178136].

**Tissue / cell level.**
- **Tissue:** cerebral microvascular endothelium (nervous-system vasculature); nervous tissue.
- **Target cells:** **brain microvascular endothelial cells (HBMEC; CL:1001509)** — the principal cellular gateway; **neutrophils (CL:0000775)** (transmigration); **macrophages (CL:0000235)** (FcγRI/CD64 interaction); neurons and glia (injury, reactive gliosis).

**Subcellular level (GO cellular component).**
- Plasma-membrane **membrane rafts (GO:0045121)** and **caveolae** (caveolin-1) mediate IbeA signaling; **cytoskeleton** — actin filaments, microtubules, and **intermediate filaments (vimentin)**; **nucleus** (NF-κB translocation). Ecgp96/gp96 localizes to the ER and cell surface.

**Localization / lateralization.** Diffuse, **bilateral** leptomeningeal involvement is typical; focal complications (abscess, infarct) may be **unilateral or asymmetric**.

---

## 8. Temporal Development

- **Onset age:** neonatal — **early-onset (≤72 h)** typically vertically acquired, and **late-onset (>72 h to ~28 days, up to <90 days)** often nosocomial. Also affects older adults and post-neurosurgical patients.
- **Onset pattern:** **acute to fulminant**; can progress within hours.
- **Stages / course:** acute bacterial meningitis → potential early complications (cerebral abscess, ventriculitis, ischemo-hemorrhagic lesions) → convalescence → long-term neurological sequelae in survivors [PMID: 23178136].
- **Progression rate:** rapid; deterioration to coma predicts death (OR 31.85) [PMID: 29384979].
- **Duration:** acute illness over days–weeks with antibiotics; **sequelae are lifelong**.
- **Critical period / window of opportunity:** early empirical antibiotics are decisive — delayed/inadequate therapy increases complications [PMID: 23178136]; delayed presentation independently predicts unfavorable outcome [PMID: 41387772].

---

## 9. Inheritance and Population

**Epidemiology.**
- Neonatal *E. coli* invasive disease is **uncommon**. Population-based surveillance in the Paris area (2019–2021, ≥34 weeks gestation) recorded **early-onset neonatal sepsis incidence of 0.32 per 1000 live births (95% CI 0.26–0.38)**, of which *E. coli* meningitis is a subset; GBS was ~twice as frequent as *E. coli* in term infants [PMID: 35902218].
- Norwegian data give **neonatal bacterial meningitis incidence of 36 per 100,000 live births**, with *E. coli* responsible for 18% of childhood cases [PMID: 41273196].

> "108 EOS were recorded (annual incidence, 0.32 per 1000 live births; 95% CI 0.26 to 0.38)" — [PMID: 35902218](https://pubmed.ncbi.nlm.nih.gov/35902218/)

**Etiologic share (selected cohorts):**

| Cohort / setting | *E. coli* share | Reference |
|---|---|---|
| Early-onset neonatal meningitis, 20-yr cohort | 37.1% of blood-culture-positive (vs GBS 30.7%) | [PMID: 42661190] |
| Australian tertiary, culture-proven neonatal meningitis | 19% (4/21; tied with *S. aureus*) | [PMID: 41543078] |
| Ethiopian suspected meningitis (culture+PCR) | 45.5% (25/55) — most common | [PMID: 41387772] |
| Norwegian childhood cases | 18% | [PMID: 41273196] |

**Inheritance / penetrance / founder effects / carrier frequency / consanguinity:** **Not applicable** — infectious, non-Mendelian disease.

**Population demographics.**
- **Age:** overwhelmingly neonates/young infants; secondary peaks in older/immunocompromised adults and post-neurosurgical patients.
- **Sex ratio:** male predominance is generally reported for neonatal Gram-negative sepsis/meningitis (not precisely quantified in the reviewed sources).
- **Geographic distribution:** worldwide; higher burden and higher antimicrobial resistance in resource-limited settings [PMID: 41387772].
- **Pathogen lineage distribution:** phylogroup B2 / ST95 (O1/O2/O18:K1) globally; emerging multidrug-resistant ST131 clones.

---

## 10. Diagnostics

**Gold standard — CSF analysis plus culture.** Definitive diagnosis requires **lumbar puncture** with CSF showing **neutrophilic pleocytosis, elevated protein, and low glucose (hypoglycorrhachia)**, plus a **positive CSF and/or blood culture** growing Gram-negative rods [PMID: 22090305].

| Test | Finding in *E. coli* meningitis | Notes |
|---|---|---|
| CSF cell count/differential (LOINC) | Neutrophilic pleocytosis | Nonspecific bacterial pattern |
| CSF protein (LOINC) | Elevated (e.g., 572 mg/dL) | [PMID: 22090305] |
| CSF glucose (LOINC) | Low (hypoglycorrhachia; e.g., 9.5 mg/dL) | [PMID: 22090305] |
| CSF/blood culture | Gram-negative bacilli; *E. coli* | Gold standard; enables susceptibility testing |
| CSF Gram stain | Gram-negative rods | Rapid presumptive |
| Blood culture | Positive in high-grade bacteremia | Supports diagnosis |

**Molecular / omics adjuncts.**
- **Multiplex PCR panels** (e.g., MeltArray CNS targeting 85 meningitis pathogens) and syndromic panels detect *E. coli* directly from CSF, outperforming culture especially after antibiotics [PMID: 42623488; PMID: 41387772].
- **Targeted metagenomic next-generation sequencing (mNGS)** of CSF shows **moderate agreement (~59% positive agreement) with conventional diagnostics** and aids detection in culture-negative cases, but high unexpected-detection rates limit standalone use [PMID: 42636981].

> "Targeted mNGS shows moderate agreement with conventional diagnostics and may aid pathogen detection in selected patients with negative routine testing." — [PMID: 42636981](https://pubmed.ncbi.nlm.nih.gov/42636981/)

**Imaging.** Cranial ultrasound (neonate; ventricular dilatation), CT/MRI to detect abscess, ventriculitis, infarction, hydrocephalus.

**Genetic testing / newborn screening / host omics diagnostics:** **Not applicable** (no host genetic cause). "Screening" here refers to microbiologic detection, not carrier/germline testing.

**Differential diagnosis.** GBS meningitis (co-predominant; distinguished by Gram stain/culture), *Listeria monocytogenes*, *Klebsiella pneumoniae* and other Enterobacterales, *Citrobacter*, *S. aureus*, viral/enteroviral meningitis, and non-infectious causes.

---

## 11. Outcome / Prognosis

**Mortality.** Outcome is poor: **12% mortality in term and 18% in preterm** infants [PMID: 23178136]. Population cohorts report ~9–19% case fatality [PMID: 29384979; PMID: 41543078].

> "Outcome of early and late onset E. coli neonatal meningitis is poor with 12% (term infant) to 18% (premature infant) mortality rates." — [PMID: 23178136](https://pubmed.ncbi.nlm.nih.gov/23178136/)

**Morbidity / sequelae.** Long-term **neurosensorial sequelae 14–17%** and **neurodevelopmental sequelae 10–17%** [PMID: 23178136]. Early complications: cerebral abscess, ventriculitis, ischemo-hemorrhagic lesions, hydrocephalus. In one cohort, 23% of survivors had serious CNS complications at discharge [PMID: 29384979].

> "Long term sequelae, particularly neurosensorial [14-17%] and neurodevelopmental [10-17%] are frequent." — [PMID: 23178136](https://pubmed.ncbi.nlm.nih.gov/23178136/)

**Prognostic factors.** Independent predictors of **death**: **prematurity (OR 5.84)**, **low birth weight (OR 8.48)**, and **coma at presentation (OR 31.85)** [PMID: 29384979]. Predictors of **CNS complications**: seizures (OR 7.06), temperature instability (OR 2.99), high CSF protein (OR 2.62) [PMID: 29384979]. Additional adverse factors: hemodynamic failure, apnea, hypoglycorrhachia, abnormal EEG, and delayed/inadequate antibiotics [PMID: 23178136]. In broader cohorts, low Glasgow Coma Scale, comorbidity, and delayed presentation independently predict unfavorable outcome [PMID: 41387772].

---

## 12. Treatment

**Pharmacotherapy (mainstay).**
- **Empirical:** third-generation cephalosporins — **cefotaxime (NCIT:C376)** or **ceftriaxone (NCIT:C769)** — often combined with an **aminoglycoside (gentamicin/amikacin)** or **ampicillin (NCIT:C263)** in neonatal regimens.
- **Resistant strains:** **meropenem (NCIT:C1352)** for ESBL/AmpC producers; carbapenems for cephalosporin resistance.
- **Rationale for coverage choice:** **ampicillin resistance is high (~78%)** among NMEC, so ampicillin monotherapy is inadequate empirically [PMID: 26407251]. Contemporary ESBL-producing and ST131/CTX-M-15 clones further threaten empirical regimens [PMID: 26407251; PMID: 41820864].

> "the rate of ampicillin resistance was high (78%)" — [PMID: 26407251](https://pubmed.ncbi.nlm.nih.gov/26407251/)

**Adjunctive therapy.**
- **Corticosteroids (dexamethasone)** reduce mortality and neurological sequelae in acute bacterial meningitis overall (chiefly pneumococcal); however, **benefit in neonatal Gram-negative meningitis is not established**, and guidelines generally exclude neonates [PMID: 41675892; PMID: 42601017].
- **Supportive care:** anticonvulsants for seizures, management of raised intracranial pressure/hydrocephalus (may require CSF diversion/shunt), hemodynamic and respiratory support.

**Experimental / host-directed therapeutics (model-organism evidence).**
- **Mesenchymal stem cells (MSCs):** intraventricular human umbilical-cord-blood-derived MSC transplantation reduced CSF bacterial growth and mortality and attenuated brain injury in newborn-rat *E. coli* meningitis [PMID: 30188499].

> "Intraventricular transplantation of hUCB-MSCs significantly improved survival and attenuated the brain injury via anti-inflammatory and antibacterial effects in experimental neonatal E. coli meningitis." — [PMID: 30188499](https://pubmed.ncbi.nlm.nih.gov/30188499/)

- **MSC-derived extracellular vesicles (MSC-EVs)** similarly attenuated brain injury [PMID: 35888118].
- **Mechanism-targeted candidates (preclinical):** RIPK1 inhibitors (to block ripoptosome-driven endothelial death) [PMID: 40774959]; GCH1/biopterin inhibitor DAHP (prevented invasion and meningitis in newborn mice) [PMID: 23100563]; anti-OmpA/Ecgp96 interface blockade [PMID: 24932957].

**Pharmacogenomics / gene / cell / RNA / targeted / immuno-therapy (host):** Not applicable as disease-specific approved therapies.

---

## 13. Prevention

**Primary prevention.**
- **Maternal screening and intrapartum management** of colonization; hygiene and infection-control in neonatal units to prevent nosocomial acquisition.
- **Pre-emptive antibiotics** for well-appearing co-twins of an affected neonate reduced disease risk in a small subgroup (11% vs 56%, p=0.03) [PMID: 42497927].
- **Probiotics:** a *Bifidobacterium* mixture prevented neonatal *E. coli* K1 translocation/infection in a model [PMID: 28979247].

**Immunization (experimental — no licensed vaccine).**
- **No vaccine is currently available** against bacterial neonatal meningitis [PMID: 36709579].
- **PNAG (Poly-β-(1-6)-N-Acetyl-Glucosamine):** a TnSeq-identified conserved surface polysaccharide; **both passive and active immunization prevented/treated *E. coli* K1 meningitis in neonatal mice**, with opsonophagocytic killing and reduced BBB crossing; PNAG is also expressed by GBS, offering potential cross-protection [PMID: 36709579].

> "We showed that both passive and active immunization successfully prevented and/or treated meningitis caused by E. coli K1 in neonatal mice." — [PMID: 36709579](https://pubmed.ncbi.nlm.nih.gov/36709579/)

- **OmpA / Ecgp96 GlcNAc1-4GlcNAc interface:** a preventive target — disrupting this interaction blocks invasion [PMID: 24932957].

**Secondary/tertiary prevention.** Early lumbar puncture and prompt empirical antibiotics (secondary); management of complications (hydrocephalus, seizures, sequelae) and rehabilitation (tertiary). **Counseling / genetic screening:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogen:** *Escherichia coli* (**NCBI:txid562**).
- **Zoonotic / cross-host lineage:** Neuropathogenic *E. coli* belong to the **zoonotic-capable ExPEC/APEC phylogroup B2, ST complex 95** lineage. **Avian pathogenic *E. coli* (APEC)** and human ExPEC of serotypes O1, O2, O18 cluster in B2/ST95 with **no or minimal host specificity** [PMID: 25397580].

> "Avian pathogenic E. coli and human extraintestinal pathogenic E. coli serotypes O1, O2 and O18 strains isolated from different hosts are generally located in phylogroup B2 and ST complex 95, and they share similar genetic characteristics and pathogenicity, with no or minimal host specificity." — [PMID: 25397580](https://pubmed.ncbi.nlm.nih.gov/25397580/)

- **Molecular identity across hosts:** Representative O18 APEC and NMEC strains have **identical OmpA sequences**, survive human serum equally, use the same receptors (FcγRI-α/CD64 on macrophages; Ecgp96 on endothelium), and induce meningitis in newborn mice [PMID: 26407066].

> "The amino acid sequences of the outer membrane protein A (OmpA), an important virulence factor in the pathogenesis of meningitis, are identical within these representative APEC and NMEC strains." — [PMID: 26407066](https://pubmed.ncbi.nlm.nih.gov/26407066/)

- **Natural / veterinary disease:** APEC causes avian colibacillosis (poultry); the shared virulence repertoire underscores a **One Health / zoonotic reservoir** concern (poultry as a potential ExPEC reservoir).
- **Comparative biology:** the OmpA–Ecgp96, CNF1–37LRP, and IbeA–vimentin mechanisms are conserved between avian and human strains, supporting evolutionary conservation of the meningitis mechanism.

---

## 15. Model Organisms

- **Mammalian in vivo models:** **Newborn/neonatal rat** and **newborn mouse** models of hematogenous *E. coli* K1 meningitis are the workhorses — used to demonstrate CNF1/RhoA-dependent BBB traversal [PMID: 11877402], DAHP/biopterin-dependent meningitis prevention [PMID: 23100563], PNAG vaccine efficacy [PMID: 36709579], and MSC therapy [PMID: 30188499]. A **newborn-rat ventriculitis model without concomitant bacteremia** (intraventricular K1-negative *E. coli*) isolates CNS injury from systemic sepsis [PMID: 31846163].
- **In vitro / cellular models:** **Human brain microvascular endothelial cells (HBMEC)** are the standard BBB model for invasion/transcytosis and signaling studies [PMID: 12860457; PMID: 20088823]; mouse **bEnd.3** BMEC used for APEC studies [PMID: 28199899]; CHO-Lec1 glycosylation-mutant cells for receptor-epitope mapping [PMID: 24932957].
- **Phenotype recapitulation:** Neonatal rodent models faithfully reproduce bacteremia → BBB crossing → CSF infection → brain injury/inflammation and neurodevelopmental impairment, and respond to interventions predictably.
- **Limitations:** Rodent BBB and immune ontogeny differ from human; K1-negative ventriculitis models bypass the natural hematogenous route; in vitro HBMEC monolayers cannot fully capture in vivo neuroinflammatory dynamics.
- **Resources:** MGI (mouse), RGD (rat); strain resources for prototype NMEC (RS218, O18:K1:H7).

---

## Mechanistic Model / Interpretation

```
   NMEC (K1+, phylogroup B2 / ST95, O18/O1/O2:K1)
              │  perinatal / mucosal entry
              ▼
   [K1 sialic-acid capsule] ── impedes alternative complement pathway ─┐
              │                                                         │ (immune evasion)
              ▼                                                         │
   HIGH-GRADE, SUSTAINED BACTEREMIA  ◄──────────────────────────────────┘
              │  (threshold magnitude required)
              ▼
   BINDING TO BRAIN MICROVASCULAR ENDOTHELIUM (HBMEC) at the BBB
              │
      ┌───────┼───────────────────────┬───────────────────────────┐
      ▼       ▼                        ▼                           ▼
  OmpA→Ecgp96(gp96)        CNF1→37LRP              IbeA→vimentin + PSF
      → PI3K                   → RhoA                  → ERK → NF-κB
      │                        │                        │  (+ICAM-1/CD44)
      └──────── actin remodeling / receptor endocytosis ───────────┘
              │
              ▼
   TRANSCELLULAR TRANSCYTOSIS across endothelium
   (NO initial tight-junction disruption)
              │
              ├──► Bacterial replication in CSF / subarachnoid space
              └──► IbeA/vimentin-driven NEUTROPHIL TRANSMIGRATION
              │
              ▼
   RIPK1 / RIPOPTOSOME → apoptosis + pyroptosis + necroptosis (endothelium)
              │
              ▼
   BBB DISRUPTION + NEUROINFLAMMATION + NEURONAL INJURY
              │
              ▼
   CLINICAL MENINGITIS → fever, seizures, bulging fontanelle, coma
   COMPLICATIONS → abscess, ventriculitis, hydrocephalus, infarction
   OUTCOME → 12–18% mortality; 10–17% neurodevelopmental sequelae
```

The central interpretive insight is that **immune evasion (capsule) and endothelial invasion (three redundant invasin pathways) are the two rate-limiting, upstream nodes**, while **RIPK1-driven regulated cell death and neutrophil influx are the downstream effectors of tissue damage**. The redundancy of invasion pathways (OmpA, CNF1, IbeA each independent, with additive inhibitor effects and greater attenuation in double mutants) explains why single-target anti-virulence strategies may be insufficient and why **conserved capsular/surface antigens (PNAG, K1) and shared receptors (Ecgp96) are attractive vaccine/therapeutic targets**.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [36709579](https://pubmed.ncbi.nlm.nih.gov/36709579/) | *E. coli* leading Gram-negative neonatal meningitis cause; PNAG vaccine POC; no licensed vaccine | Review + animal model |
| [38531686](https://pubmed.ncbi.nlm.nih.gov/38531686/) | K1 leading cause; CsiR/low-iron invasion pathway | In vitro/mechanistic |
| [42661190](https://pubmed.ncbi.nlm.nih.gov/42661190/) | Modern etiologic breakdown (*E. coli* 37.1%) | Human cohort (20-yr) |
| [6196296](https://pubmed.ncbi.nlm.nih.gov/6196296/) | K1 capsule impedes alternative complement pathway | In vitro + newborn-rat |
| [12860457](https://pubmed.ncbi.nlm.nih.gov/12860457/) | OmpA→PI3K vs CNF1→RhoA independent invasion pathways | In vitro (HBMEC) |
| [11877402](https://pubmed.ncbi.nlm.nih.gov/11877402/) | CNF1/RhoA required for in vivo BBB traversal | Animal model |
| [20088823](https://pubmed.ncbi.nlm.nih.gov/20088823/) | Vimentin is primary IbeA receptor for invasion | In vitro (HBMEC) |
| [22536447](https://pubmed.ncbi.nlm.nih.gov/22536447/) | Vimentin+PSF drive NF-κB nuclear translocation | In vitro |
| [21083634](https://pubmed.ncbi.nlm.nih.gov/21083634/) | IbeA/vimentin → PMN transmigration, ICAM-1/CD44 | In vitro |
| [11008113](https://pubmed.ncbi.nlm.nih.gov/11008113/) | Transcytosis route; ompA/ibeA/ibeB/yijP gene set | Review/mechanistic |
| [40774959](https://pubmed.ncbi.nlm.nih.gov/40774959/) | RIPK1/ripoptosome-driven endothelial death & BBB disruption | In vitro/model |
| [24932957](https://pubmed.ncbi.nlm.nih.gov/24932957/) | OmpA–Ecgp96 GlcNAc epitope; preventive target | In vitro + mouse |
| [23100563](https://pubmed.ncbi.nlm.nih.gov/23100563/) | GCH1/biopterin/NO node; DAHP prevents meningitis | In vitro + newborn mice |
| [29384979](https://pubmed.ncbi.nlm.nih.gov/29384979/) | Phenotype frequencies; death/CNS-complication predictors | Population cohort (UK/Ireland) |
| [23178136](https://pubmed.ncbi.nlm.nih.gov/23178136/) | Mortality 12–18%; sequelae 10–17% | Review |
| [26407251](https://pubmed.ncbi.nlm.nih.gov/26407251/) | Phylogroup B2 68%/K1 53%; ampicillin resistance 78%; ST131/CTX-M-15 | US isolates |
| [35902218](https://pubmed.ncbi.nlm.nih.gov/35902218/) | EOS incidence 0.32/1000 live births | Population surveillance (Paris) |
| [41273196](https://pubmed.ncbi.nlm.nih.gov/41273196/) | Neonatal meningitis 36/100,000; *E. coli* 18% | National (Norway) |
| [25397580](https://pubmed.ncbi.nlm.nih.gov/25397580/) | B2/ST95 APEC–ExPEC shared lineage, minimal host specificity | Comparative genomics |
| [26407066](https://pubmed.ncbi.nlm.nih.gov/26407066/) | Identical OmpA, shared receptors APEC/NMEC | Comparative in vitro/model |
| [30188499](https://pubmed.ncbi.nlm.nih.gov/30188499/) | MSC therapy improves survival/brain injury | Newborn-rat model |
| [35888118](https://pubmed.ncbi.nlm.nih.gov/35888118/) | MSC-EVs attenuate brain injury | Model |
| [41675892](https://pubmed.ncbi.nlm.nih.gov/41675892/) | Corticosteroid adjunct benefit (mainly pneumococcal; excludes neonates) | Narrative review |
| [42636981](https://pubmed.ncbi.nlm.nih.gov/42636981/) | Targeted mNGS diagnostic role & limits | Diagnostic study |
| [42623488](https://pubmed.ncbi.nlm.nih.gov/42623488/) | Multiplex PCR (MeltArray CNS) for CSF pathogens | Diagnostic study |
| [22090305](https://pubmed.ncbi.nlm.nih.gov/22090305/) | Severe CSF profile example (protein 572, glucose 9.5) | Case report |
| [42497927](https://pubmed.ncbi.nlm.nih.gov/42497927/) | Twin concordance; pre-emptive antibiotics | Systematic review |

---

## Limitations and Knowledge Gaps

1. **Not a genetic disease.** Sections geared to Mendelian genetics (causal genes, ACMG variants, inheritance, penetrance, founder effects, genetic testing, newborn screening) are **not applicable**; the "genetics" reside in the pathogen. Host susceptibility loci for *E. coli* meningitis are essentially undefined in humans.
2. **Mechanism largely from models.** Much of the invasion/injury mechanism (OmpA/CNF1/IbeA pathways, RIPK1 ripoptosome, biopterin node) derives from **in vitro HBMEC and neonatal-rodent models**; direct human validation is limited.
3. **Epidemiologic heterogeneity.** *E. coli* share of neonatal meningitis varies widely by setting (18–46%); resource-limited settings show higher resistance and worse outcomes, complicating global generalization.
4. **No head-to-head neonatal Gram-negative corticosteroid trial.** Adjunctive steroid benefit is extrapolated from predominantly pneumococcal data and is **not established for neonatal Gram-negative meningitis**.
5. **Resistance trajectory.** ESBL/ST131/CTX-M-15 emergence data are from limited isolate collections; the true trajectory threatening empirical cephalosporin therapy needs continued surveillance.
6. **Vaccine translation gap.** PNAG and OmpA are promising but remain **preclinical**; no human efficacy data exist.
7. **Sex-ratio and QoL quantification** were not precisely resolved from the reviewed literature.

---

## Proposed Follow-up Experiments / Actions

1. **Pathogen genomic surveillance:** Systematically genotype NMEC isolates (phylogroup, ST, capsule, ESBL/carbapenemase genes) across regions to track ST131/ST95 dynamics and inform empirical regimens.
2. **RIPK1-targeted host-directed therapy:** Test RIPK1 kinase inhibitors (e.g., necrostatin-class) as adjuncts in neonatal-rodent *E. coli* meningitis to quantify reductions in BBB disruption and neurodevelopmental sequelae [building on PMID: 40774959].
3. **Multivalent conserved-antigen vaccine:** Advance PNAG (+ OmpA/Ecgp96-interface) conjugate vaccines toward safety/immunogenicity studies, leveraging cross-protection against GBS PNAG [PMID: 36709579].
4. **Combination anti-invasin strategy:** Given pathway redundancy, test simultaneous blockade of ≥2 invasion arms (PI3K + Rho-kinase + IbeA/vimentin) in vivo for additive protection [PMID: 12860457].
5. **Neonatal Gram-negative steroid/adjunct trial:** Design a dedicated trial or observational study of dexamethasone or alternative immunomodulation specifically in neonatal Gram-negative meningitis.
6. **Diagnostic validation:** Prospectively validate multiplex-PCR and targeted mNGS CSF panels against culture in neonatal cohorts to define sensitivity for culture-negative (pre-treated) cases [PMID: 42623488; PMID: 42636981].
7. **One Health investigation:** Quantify poultry/APEC B2-ST95 reservoirs and potential zoonotic transmission routes for neuropathogenic *E. coli* [PMID: 25397580].

---

*Report compiled from 14 confirmed findings and 56 reviewed papers across a 5-iteration autonomous investigation. Evidence types are labeled (human clinical, animal model, in vitro, computational/genomic) throughout. All quoted text is verbatim from cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Escherichia_Coli_Meningitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Escherichia_Coli_Meningitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 39 |
| On topic | 27 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23178136` *(abstract only)*: "Long term sequelae, particularly neurosensorial [14-17%] and neurodevelopmental [10-17%] are frequent."
  - closest text in source: "Long term sequelae, particularly neurosensorial [14-17%] and neurodevelopmental [10-17%] are frequent."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002361` (1 mention) - the report calls it "Primary organ:** brain and meninges — **leptomeninges"; UBERON calls it **pia mater**
- `UBERON:0002360` (1 mention) - the report calls it "Body system:** central nervous system / **meninges"; UBERON calls it **meninx**
- `NCIT:C376` (1 mention) - the report calls it "Empirical:** third-generation cephalosporins — **cefotaxime"; NCIT calls it **Cisplatin**
- `NCIT:C1352` (1 mention) - the report calls it "Resistant strains:** **meropenem"; NCIT calls it **Recombinant Brain-Derived Growth Factors**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051092` (obsolete positive regulation of NF-kappaB transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001259` (1 mention) - the report calls it "Coma / reduced consciousness"; HP calls it **Coma**, and lists "Unconsciousness" among its other names
- `HP:0031179` (1 mention) - the report calls it "Nuchal rigidity / neck stiffness"; HP calls it **Nuchal rigidity**
- `GO:0045056` (1 mention) - the report calls it "GO biological processes:** transcytosis"; GO calls it **transcytosis**
- `GO:0045121` (2 mentions) - the report calls it "GO cellular components:** membrane raft", "Plasma-membrane **membrane rafts"; GO calls it **membrane raft**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0045121` - called "GO cellular components:** membrane raft", "Plasma-membrane **membrane rafts"