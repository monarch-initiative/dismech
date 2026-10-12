---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T13:04:30.749004'
end_time: '2026-10-08T13:10:05.149003'
duration_seconds: 334.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia, Autosomal Recessive 26
  mondo_id: MONDO:0033116
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 10
  num_turns: 38
  total_cost_usd: 2.6579409
  session_id: 2b317df2-0007-4e17-bba4-24d430d3d807
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 4
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 12
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 11
  validator_version: 0.3.0
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0033116
    reported_labels:
    - MONDO
    ontology_label: spinocerebellar ataxia, autosomal recessive 26
  - term_id: DOID:0080260
    reported_labels:
    - Disease Ontology
    ontology_label: autosomal recessive spinocerebellar ataxia 26
  - term_id: NCIT:C121351
    reported_labels:
    - Fine motor
    ontology_label: Occupational Therapy
  - term_id: NCIT:C159273
    reported_labels:
    - Dysarthria
    ontology_label: Speech Language Therapy
  - term_id: NCIT:C15240
    reported_labels:
    - AR recurrence 25%
    ontology_label: Genetic Counseling
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0006977
    ontology_label: obsolete DNA damage response, signal transduction by p53 class
      mediator resulting in cell cycle arrest
    replaced_by: GO:0030330
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia, Autosomal Recessive 26
- **MONDO ID:** MONDO:0033116 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia, Autosomal Recessive 26** covering all of the
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

Gathering primary literature on SCAR26 (XRCC1); now reading the O'Connor 2018 patient report and recent papers.

Reading the cached zebrafish, mouse, and PARP1-mechanism papers for exact quotes.

Checking Orphanet/ClinGen identifiers and the Komulainen abstract, then writing the report.

# Spinocerebellar Ataxia, Autosomal Recessive 26 (SCAR26; XRCC1-related ataxia): Research Report

**Prepared:** 2026-10-08 · **Target:** MONDO:0033116 · **Category:** Mendelian

> **About this report.** The quotes marked "verbatim" were checked against the cache files I fetched in this session with `just fetch-reference` (`references_cache/PMID_*.md`), so they can be used as snippets. Ontology IDs marked *(verify)* came from memory. They are leads only and must be checked with `runoak` or the term caches before binding. Two 2026 case reports have no abstract in PubMed (PMIDs 41631675 and 41506093), and their publisher pages blocked retrieval. They are listed but not quoted.

---

## 1. Disease Information

**Overview.** SCAR26 is a very rare autosomal recessive cerebellar ataxia caused by biallelic variants in **XRCC1**. XRCC1 is the scaffold protein for DNA single-strand break repair (SSBR) and base excision repair (BER). The core phenotype is:
- progressive cerebellar ataxia with cerebellar atrophy
- sensorimotor, predominantly axonal, length-dependent peripheral neuropathy
- oculomotor abnormalities (ocular motor apraxia in the index case; slow saccade initiation and nystagmus in later cases)

The disease belongs to the SSBR-defective ataxia family with AOA1 (*APTX*), SCAN1 (*TDP1*) and AOA4 (*PNKP*). One 2022 Brazilian cohort paper calls it "AOA5" (PMID:35426160). I could not confirm that synonym in OMIM or Orphanet.

- Verbatim (PMID:28002403, Hoch et al., *Nature* 2017): *"Here we show that biallelic mutations in the human XRCC1 gene are associated with ocular motor apraxia, axonal neuropathy, and progressive cerebellar ataxia."*

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0033116 |
| OMIM (phenotype) | #617633 |
| OMIM (gene) | *194360 (XRCC1) |
| HGNC | hgnc:12828 (XRCC1; 19q13.31; UniProt P18887; Ensembl ENSG00000073050; MANE NM_006297.3) — from `kb/genes/ingest/hgnc.tsv` |
| Disease Ontology | DOID:0080260 |
| MedGen | C4539948 |
| Orphanet | No distinct ORPHA code found; no Orphadata cache row mentions XRCC1 |
| ICD-10/11 | No specific code; falls under G11.x hereditary ataxia (non-specific) |

**Synonyms:** SCAR26; autosomal recessive spinocerebellar ataxia 26; XRCC1-related cerebellar ataxia; "AOA5" (single source, unconfirmed).

**Source of information:** Essentially all data come from individual patient reports. At most about 4–6 published probands are known (see §9). No registry or aggregated cohort exists.

## 2. Etiology

- **Cause:** Biallelic germline loss-of-function variants in *XRCC1*.
- **Genetic risk factors:**
  - **c.1293G>C (p.Lys431Asn)** is recurrent in South Asian (Pakistani and East Indian) families. It sits at the last base of exon 11 and disrupts the intron 11 donor splice site.
  - O'Connor et al. found it heterozygous in four South Asian ExAC individuals (AF 0.0002449). They wrote that it *"likely exists at a higher frequency than previously described"* (PMID:29472272).
- **Modifier genes:** None in humans. In mice, *Parp1* dosage strongly modifies the phenotype: losing one *Parp1* allele extended lifespan more than losing both (PMID:33932076).
- **Environmental, protective and gene–environment factors:** None documented. Mechanistically, endogenous oxidative single-strand breaks are the relevant "exposure". This is inferred; no human exposure data exist.

## 3. Phenotypes

The sources below are the index patient (PMID:28002403) and two homozygous c.1293G>C patients (PMID:29472272). With N≈3, every frequency is qualitative.

| Phenotype | Notes / frequency | Suggested HPO *(verify)* |
|---|---|---|
| Progressive cerebellar ataxia (gait and limb) | 3/3 | HP:0002073 Progressive cerebellar ataxia |
| Cerebellar atrophy (MRI) | 3/3; P1 in O'Connor had a normal MRI at 15 and atrophy later | HP:0001272 Cerebellar atrophy |
| Pontine / middle and superior cerebellar peduncle volume loss | 1/3 | HP:0006879 Pontocerebellar atrophy |
| Sensorimotor axonal, length-dependent neuropathy | 3/3 | HP:0003477 Peripheral axonal neuropathy; HP:0007141 Sensorimotor neuropathy |
| Ocular motor apraxia | Index case | HP:0000657 Oculomotor apraxia |
| Slow saccade initiation, hypometric saccades, jerky pursuit | O'Connor P1 | HP:0000570 Abnormality of saccadic eye movements |
| Gaze-evoked / horizontal nystagmus | 2/3 | HP:0000639 Nystagmus |
| Dysarthria | 3/3 | HP:0001260 Dysarthria |
| Dysmetria, dysdiadochokinesis | ≥2/3 | HP:0001310; HP:0002075 |
| Areflexia (lower limbs or generalized) | 2/3 | HP:0001284 Areflexia |
| Impaired vibration sense and proprioception | 1–2/3 | HP:0002495 Impaired vibratory sensation |
| Distal calf wasting, pes planus / cavus | 2/3 | HP:0003693 Distal amyotrophy; HP:0001761 Pes cavus |
| Muscle cramps | 2/3 | HP:0003394 Muscle spasm/cramps |
| Mild learning difficulties | 2/3 (childhood-onset cases) | HP:0001328 Specific learning disability |
| Extensor plantar response | 1/3 | HP:0003487 Babinski sign |
| Male infertility (hypogonadism, azoospermia) | 1/3; authors say alternative causes are not excluded | HP:0000027 Azoospermia |

**Onset**
- Adult onset in the index case: balance and gait difficulties *"first noticed at twenty-eight years"*, with diagnosis at 41 (PMID:28002403).
- Early childhood onset in O'Connor's patients: observable signs by about 3 years.
- 2026 reports describe one childhood-onset homozygous c.1293G>C patient (PMID:41631675) and one late-onset case (PMID:41506093). I could not read either.

**Course:** Slowly progressive. Secondary sources (e.g., MalaCards/OMIM synopsis) mention eventual loss of independent ambulation.

**Confounder:** O'Connor P2 also carried homozygous *CLCN1* myotonia congenita. Myotonia, calf hypertrophy and probably the cramps in that patient should not be attributed to SCAR26.

**Quality of life:** No formal QoL data exist. Expect impact on mobility and falls, fine motor function, speech, and possibly fertility.

## 4. Genetic / Molecular Information

**Gene:** *XRCC1*, X-ray repair cross-complementing 1. It is a non-enzymatic scaffold with:
- an N-terminal domain that binds POLβ
- a central BRCT1 domain that binds PAR and DNA
- a C-terminal BRCT2 domain that binds LIG3α
- a CK2-phosphorylated linker that binds PNKP, APTX and APLF

**Reported pathogenic variants**

| Variant (NM_006297) | Effect | Zygosity / cases | Source |
|---|---|---|---|
| c.1293G>C, p.(Lys431Asn) | Last base of exon 11 / intron 11 donor. In patient LCLs (cycloheximide-treated) it causes aberrant splicing including intron 11 retention, plus reduced total XRCC1 mRNA. The missense effect lies in the BRCTa/linker region | Compound heterozygous in the index case; homozygous in 2 Pakistani consanguineous families with a shared haplotype; homozygous in the 2026 MDCP case | PMID:28002403; 29472272; 41631675 |
| c.1393C>T, p.(Gln465*) | Nonsense, predicted NMD | In trans with K431N in the index case | PMID:28002403 |

- Verbatim (PMID:28002403): *"1293G>C mutation is located at the end of exon 11 and is also part of the donor splice site for intron 11, most likely affecting splicing and inducing premature stop codons/nonsense-mediated decay and/or encoding XRCC1 with the missense mutation, K431N."*
- **Protein consequence** (PMID:28002403): XRCC1 protein is reduced in patient cells. The partner protein is also destabilized: *"Levels of DNA ligase IIIα (Lig3α) were also greatly reduced (by >80%) in patient cells"*.
- **Functional class:** Loss of function, hypomorphic. Complete XRCC1 loss is embryonic lethal in mice, so the human alleles must retain some residual function (inference).
- **Other recorded SCAR26 variants:** ClinVar lists about 13 *XRCC1* variants under SCAR26 with mixed classifications. A 2026 *Cell Death Differ* study tested three "SCAR26-associated" missense constructs: c.1196A>G (BRCT1), c.1293G>C (linker) and c.1738C>T (BRCT2). It found that one variant disrupts TADA2B binding while LIG3 binding is preserved (PMID:42399641). Their individual clinical provenance is unverified, so do not curate them as patient variants without a primary report.
- **Gene–disease validity:** A ClinGen GDV record for XRCC1–SCAR26 was not found in the local cache; check before asserting a tier. PanelApp England and Australia rate XRCC1 Green (high evidence) for hereditary ataxia in current versions; earlier versions were Amber/Red.
- **Origin:** Germline. No somatic, epigenetic or chromosomal mechanisms are described.
- **Common polymorphisms:** p.Arg399Gln and similar variants are extensively studied cancer-association SNPs, unrelated to SCAR26. Avoid confusing them with disease variants. Hoch used R399Q only as a phasing marker.

## 5. Environmental Information

There are no environmental, lifestyle or infectious factors. The relevant "lesions" are endogenous oxidative and topoisomerase-1–induced single-strand breaks. Not applicable for `environmental:`.

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic *XRCC1* variants** (splice / missense K431N, nonsense Q465*) **lead to** reduced XRCC1 mRNA and protein (human patient cells, demonstrated; PMID:28002403).
2. **Reduced XRCC1 leads to** destabilization and loss of LIG3α (>80% reduced), so the XRCC1–LIG3α–POLβ–PNKP repair complexes fail to assemble (demonstrated in patient cells; PMID:28002403).
3. **Loss of XRCC1 complexes results in** slow repair of single-strand breaks and BER intermediates (demonstrated in patient cells and XRCC1⁻/⁻ RPE-1 cells; PMID:28002403, 34102106).
   - Verbatim (PMID:28002403): *"Cells from a patient with mutations in XRCC1 exhibited not only reduced rates of single-strand break repair but also elevated levels of protein ADP-ribosylation."*
4. **Unrepaired breaks plus the missing "anti-trapper" lead to** PARP1 trapping on BER intermediates and PARP1 hyperactivation (excess poly- and mono-ADP-ribosylation).
   - Verbatim (PMID:34102106): *"As a result, PARP1 becomes "trapped" on BER intermediates in XRCC1-deficient cells in a manner similar to that induced by PARP inhibitors, including in patient fibroblasts from XRCC1-mutated disease."*
   - Also shown in mouse cerebellum: *"Strikingly, we detected elevated levels of ADP-ribose in the cerebellum of Xrcc1Nes-Cre mice…"* (PMID:28002403).
   - XRCC1 loss also amplifies mono-ADPr and RNF114 recruitment (PMID:41922367).
   - **Feedback:** trapped PARP1 blocks POLβ access and further impedes repair, which sustains step 3: *"This excessive PARP1 engagement and trapping renders BER intermediates inaccessible to enzymes such as DNA polymerase β and impedes their repair."* (PMID:34102106)
5. **PARP1 hyperactivity then branches into three effects:**
   - **5a. Transcriptional failure.** PARP1 hyperactivity leads to excessive USP3 recruitment, loss of H2A/H2B monoubiquitination, and failed recovery of RNA polymerase I and II transcription after oxidative damage. This was shown in XRCC1 patient fibroblasts and *Xrcc1*-deficient cerebellar neurons (PMID:34811483).
     - Verbatim: *"We show that aberrant PARP1 activity suppresses transcriptional recovery during base excision repair by promoting excessive recruitment and activity of the ubiquitin protease USP3, which as a result reduces the level of monoubiquitinated histones important for normal transcriptional regulation."*
   - **5b. NAD⁺ depletion / PAR toxicity.** Proposed and supported in zebrafish discussion, but not directly measured in human SCAR26 (inferred; PMID:40379758).
   - **5c. Deregulated presynaptic Ca²⁺ signalling.** Leads to hyperexcitability and seizures in mice (PMID:33932076). Seizures have not been reported in human SCAR26.
6. **In parallel, persistent DNA damage in differentiating cerebellar interneuron progenitors leads to** p53-dependent cell-cycle arrest. This produces loss of basket, stellate and Golgi interneurons, granule-neuron apoptosis and reduced Purkinje-cell spike activity (mouse; PMID:19633665, 28002403).
   - Verbatim (PMID:19633665): *"This cell loss was linked to p53-dependent cell cycle arrest and occurred as interneuron progenitors commenced differentiation."*
   - **Upstream of this branch:** PARP1 deletion restores interneuron density about 4-fold, so PARP1 acts upstream of much of the neuron loss (PMID:28002403).
7. **Cerebellar neuron loss and dysfunction result in** cerebellar atrophy and progressive ataxia. This is direct in mice, and inferred in humans from MRI and the clinical picture.
   - PARP1 is causal: *"genetic deletion of Parp1 rescued normal cerebellar ADP-ribose levels and reduced the loss of cerebellar neurons and ataxia in Xrcc1-defective mice"* (PMID:28002403).
   - Zebrafish give the same answer: *"parp1 knockdown alone does not significantly affect neural development, and instead rescues the cerebellar defects observed in xrcc1 mutant larvae"* (PMID:40379758).
8. **Peripheral axonal neuropathy and oculomotor apraxia** presumably arise from the same SSBR/PARP1 mechanism in long peripheral axons and brainstem/cerebellar oculomotor circuits. This is **inferred**: no model has studied the peripheral nerve.

**Upstream vs downstream:** steps 1–3 form the lesion; step 4 is the pivotal hub node (PARP1 hyperactivation); steps 5–6 are cellular effectors; steps 7–8 are the organ and clinical phenotypes.

**Suggested terms** *(verify all)*

| Kind | Terms |
|---|---|
| GO | GO:0000012 single strand break repair (DECREASED); GO:0006284 base-excision repair (DECREASED); GO:0070212 protein poly-ADP-ribosylation (INCREASED); GO:0006281 DNA repair; GO:0006977 DNA damage response, signal transduction by p53 class mediator resulting in cell cycle arrest; GO:0021680 cerebellar Purkinje cell layer development or a cerebellar interneuron differentiation term; GO:0006351 DNA-templated transcription (DECREASED recovery) |
| CL | cerebellar granule cell (CL:0001031); Purkinje cell (CL:0000121); cerebellar stellate / basket / Golgi interneurons (check CL); peripheral sensory and motor neurons; fibroblast (CL:0000057) for patient-cell evidence |
| GO-CC | nucleus, nucleolus (XRCC1 is nucleolar at baseline), chromatin |
| CHEBI | NAD⁺ (CHEBI:57540); poly(ADP-ribose) |

**Molecular profiling:** No omics, single-cell or spatial datasets specific to SCAR26 were found.

## 7. Anatomical Structures

- **Primary:** cerebellum (UBERON:0002037), with vermis and hemispheres; peripheral nerves (UBERON:0001021).
- **Secondary:** pons and middle/superior cerebellar peduncles (O'Connor P1); oculomotor control circuits.
- **Possible:** testis/gonad (one patient, unconfirmed).
- **Cells:** cerebellar interneurons, granule and Purkinje cells; peripheral sensory and motor axons.
- **Subcellular:** nucleus, nucleolus, chromatin at single-strand break sites.
- **Distribution:** bilateral and symmetric; length-dependent neuropathy.

## 8. Temporal Development

- **Onset:** ranges from early childhood (~3 y; homozygous c.1293G>C) to adult (28 y; compound heterozygote) to late onset (PMID:41506093, unread).
- **Onset pattern:** insidious.
- **Course:** chronic, slowly progressive. Cerebellar atrophy can develop after a normal adolescent MRI (O'Connor P1).
- **Remission and staging:** no remission; no formal staging.
- **Critical period (mouse, inferred):** XRCC1 is most needed as cerebellar interneuron progenitors differentiate around birth (PMID:19633665).

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007). LOVD labels it "digenic". That looks erroneous because all cases are biallelic at one locus.
- **Penetrance:** apparently complete in reported biallelic individuals; an unaffected heterozygous sibling was reported.
- **Expressivity:** variable, with age of onset from ~3 to ~28 years or more. No anticipation.
- **Consanguinity and founder effect:** consanguinity was present in both Pakistani families. They share a chromosome 19 haplotype around c.1293G>C, which suggests a South Asian founder allele. The index patient was of East Indian descent with non-consanguineous parents.
- **Carrier frequency:** c.1293G>C AF about 2.4×10⁻⁴ overall in ExAC, enriched in South Asians. Re-check gnomAD v4 before quoting.
- **Prevalence:** unknown. Fewer than 10 published patients. Suggested `prevalence_class`: `CASES_IN_LITERATURE` + ULTRA_RARE.
- **Negative cohort data:** a Brazilian ataxia-with-oculomotor-apraxia cohort found no *XRCC1* variants (PMID:35426160).
- **Sex ratio:** reported cases are 1 female (index) and 2 males (O'Connor).

## 10. Diagnostics

- **Genetic testing:** the mainstay. Use a hereditary ataxia multigene panel (XRCC1 is on PanelApp hereditary ataxia panels) or exome/genome sequencing. RNA studies can help confirm splice variants such as c.1293G>C. Single-variant testing is reasonable in South Asian probands with a consistent phenotype.
- **Imaging:** brain MRI showing cerebellar (± pontine) atrophy.
- **Electrophysiology:** NCS/EMG showing length-dependent sensorimotor axonal neuropathy.
- **Biomarkers:** No validated clinical biomarker. Research-level elevated ADP-ribose / PARP1 activity in patient fibroblasts was proposed as a *"biomarker of PARP1 hyperactivity"* (PMID:28002403). Labs such as AFP, albumin and cholesterol (useful in AOA1/2/4) are not reported for SCAR26.
- **Differential diagnosis:**
  - AOA1 (*APTX*): hypoalbuminemia, hypercholesterolemia
  - AOA2 (*SETX*): elevated AFP
  - AOA4 (*PNKP*): plus microcephaly and seizures
  - SCAN1 (*TDP1*)
  - ataxia-telangiectasia (*ATM*)
  - Friedreich ataxia
  - ARCA with neuropathy (*SYNE1*, *POLG*, *RFC1*/CANVAS)
- **Screening:** no newborn screening. Cascade carrier testing is possible in affected families.

## 11. Outcome / Prognosis

- No survival or mortality data exist. Patients surveyed were alive at ages 22–47.
- Morbidity comes from progressive gait and limb ataxia, falls, dysarthria, distal weakness and sensory loss. Secondary sources mention possible loss of independent ambulation.
- No prognostic biomarkers. Earlier onset appears to go with the homozygous splice genotype (N too small to conclude).
- The mouse *Xrcc1*^Nes-Cre^ median lifespan of 3–4 weeks (seizures) is far more severe than the human disease. Do not extrapolate it to human prognosis.

## 12. Treatment

**No disease-modifying therapy and no clinical trials.** Management is supportive.

| Intervention | Notes | NCIT *(verify)* |
|---|---|---|
| Physical therapy / rehabilitation for ataxia, falls and gait aids | Standard ARCA care | NCIT:C15302 Physical Therapy; NCIT:C15315 Rehabilitation |
| Occupational therapy | Fine motor | NCIT:C121351 |
| Speech-language therapy | Dysarthria | NCIT:C159273 |
| Orthotics for foot deformity, distal weakness | Neuropathy | — |
| Genetic counseling | AR recurrence 25% | NCIT:C15240 |

**Experimental and preclinical directions**
- **PARP1 suppression** is the leading therapeutic hypothesis. Genetic deletion rescues the mouse ataxia and interneuron loss (PMID:28002403), the zebrafish cerebellar hypotrophy (PMID:40379758), and the mouse seizures and lifespan (PMID:33932076).
- **Caution:** current clinical PARP inhibitors trap PARP1 and *"do not mimic PARP1 genetic deletion"* (PMID:28002403). Non-trapping PARP1 inhibitors are suggested instead. Note also that in mice, losing one *Parp1* allele beat losing both, so dosage matters.
- **USP3** is a second candidate target (PMID:34811483). NAD⁺ repletion is hypothesized (an inference from the NAD⁺-depletion model; the ALS NAD⁺–PARP1–XRCC1 review PMID:42086408 is not SCAR26-specific).
- **Pharmacogenomics:** none.

## 13. Prevention

- **Primary:** none.
- **Secondary:** cascade carrier testing and prenatal or preimplantation diagnosis once familial variants are known. Consider c.1293G>C in carrier screening for consanguineous South Asian families.
- **Tertiary:** fall prevention and neuropathy foot care.
- No vaccines, prophylaxis or public-health measures apply.

## 14. Other Species / Natural Disease

- No naturally occurring XRCC1 ataxia was found (OMIA not checked in detail).
- Orthologs: mouse *Xrcc1* and zebrafish *xrcc1*. XRCC1 recruitment strategies vary by species (PMID:35026705).
- Not zoonotic.

## 15. Model Organisms

| Model | Phenotype recapitulation | Rescue / limitations | PMID |
|---|---|---|---|
| **Mouse *Xrcc1*^loxP/loxP^;Nestin-Cre** (neural-specific KO) | Progressive ataxia with episodic spasms; loss of cerebellar basket, stellate and Golgi interneurons; p53-dependent arrest; ~4-fold more strand breaks in neurons; hippocampal dysfunction; elevated cerebellar ADP-ribose; reduced Purkinje spike activity | p53⁻/⁻ rescues interneurons. Parp1⁻/⁻ rescues ADP-ribose, interneuron density (~4-fold) and rotarod time (>30-fold). Limitations: complete neural null vs human hypomorph; developmental rather than adult onset; lethal seizures (median lifespan 3–4 weeks) not seen in humans; no peripheral neuropathy modeled | 19633665; 28002403; 33932076 |
| **Zebrafish *xrcc1* crispants** (F0 CRISPR) | Hypotrophy of the lateral cerebellar plate, involving granule-cell markers | *parp1* co-deletion restores cerebellar plate volume. Limitations: F0 mosaic, larval stage only, no behavioral ataxia readout | 40379758 |
| **Human cells:** XRCC1 patient fibroblasts and LCLs; XRCC1⁻/⁻, PARP1⁻/⁻ and double KO RPE-1 and U2OS cells | Reduced SSBR; PARP1-dependent elevated ADP-ribose; PARP1 trapping; failed transcription recovery | PARP1 deletion or PARPi restores transcription recovery and BER (PARPi does not restore SSBR rate). Limitations: non-neuronal cells | 28002403; 34102106; 34811483; 41922367 |

**Possible model divergences to type when curating** (per CLAUDE.md taxonomy):
- `SPECIES_MISMATCH`
- `BOUNDARY_OMISSION`: no peripheral nerve in any model
- `INCOMPLETE_PHENOTYPE`: zebrafish has no ataxia readout
- a severity mismatch: the mouse null is far more severe than the human disease

---

## Evidence gaps and curation notes

1. **Very small case base**: about 3 well-described patients plus 2 unread 2026 case reports. Retry fetching PMID:41631675 and PMID:41506093 later. Both are currently cached with `content_type: unavailable` and must not be quoted.
2. **No quotable gene–disease validity tier**: no ClinGen GDV, Orphanet or GeneReviews chapter was found. Run `just check-genereviews` on the entry.
3. **No human data** on NAD⁺ depletion, seizures, or the peripheral nerve mechanism. These are candidate `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH` discussions.
4. **Repository housekeeping from this session:**
   - I cached `PMID_28002403`, `29472272`, `41631675`, `41506093`, `40379758`, `19633665`, `34811483`, `34102106`, `41922367` and `33932076` in `references_cache/`.
   - I also fetched **`PMID_33779029.md`** by mistake. It is an unrelated FXR2P seizure paper and **should be deleted**; my `rm` was blocked by permissions.
   - Prune any of the others the entry does not end up citing.

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 28002403 | Hoch NC et al. *Nature* 2017;541:87–91. XRCC1 mutation is associated with PARP1 hyperactivation and cerebellar ataxia | Human clinical + IN_VITRO + MODEL_ORGANISM; split items |
| 29472272 | O'Connor E et al. *J Neurol Neurosurg Psychiatry* 2018;89:1230–1232. Mutations in XRCC1 cause cerebellar ataxia and peripheral neuropathy | Human clinical |
| 41631675 | Ribeiro G et al. *Mov Disord Clin Pract* 2026;13:1776–1778 | Human clinical; no text available |
| 41506093 | Mahale R, Mailankody P. *Parkinsonism Relat Disord* 2026;144:108184 | Human clinical; no text available |
| 19633665 | Lee Y et al. *Nat Neurosci* 2009;12:973–980 | Model organism |
| 33932076 | Komulainen E et al. *EMBO Rep* 2021;22:e51851 | Model organism |
| 40379758 | Semenova SA et al. *Sci Rep* 2025;15:17043 | Model organism (zebrafish) |
| 34102106 | Demin AA et al. *Mol Cell* 2021;81:3018 | In vitro |
| 34811483 | Adamowicz M et al. *Nat Cell Biol* 2021;23:1287 | In vitro + mouse neurons |
| 41922367 | Dauben H et al. *Nat Commun* 2026;17:3216 | In vitro |
| 42399641 | Kim K et al. *Cell Death Differ* 2026 (SCAR26 variants vs TADA2B/LIG3) | In vitro; abstract not cached |
| 31324530 | Caldecott KW. *DNA Repair* 2019;81:102664. XRCC1 protein; form and function | Review |
| 35426160 | Brazilian AOA cohort, 2022 (no XRCC1 variants found) | Human clinical (negative) |

**Web sources:**
- [PubMed 28002403](https://pubmed.ncbi.nlm.nih.gov/28002403/)
- [PMC6227798 (O'Connor 2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6227798/)
- [Komulainen 2021, PMC8097344](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8097344/)
- [OMIM 617633](https://omim.org/entry/617633)
- [MedGen C4539948](https://www.ncbi.nlm.nih.gov/medgen/1617917)
- [Disease Ontology DOID:0080260](https://disease-ontology.org/term/DOID:0080260)
- [LOVD disease 06425](https://databases.lovd.nl/shared/diseases/06425)
- [PanelApp England XRCC1](https://panelapp.genomicsengland.co.uk/panels/20/gene/XRCC1/)
- [PanelApp Australia XRCC1](https://panelapp-aus.org/panels/271/gene/XRCC1/)
- [MalaCards SCAR26](https://www.malacards.org/card/spinocerebellar_ataxia_autosomal_recessive_26)
- [Brazilian AOA cohort, PubMed 35426160](https://pubmed.ncbi.nlm.nih.gov/35426160)
- [Kim 2026, PubMed 42399641](https://pubmed.ncbi.nlm.nih.gov/42399641/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0033116` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spinocerebellar ataxia, autosomal recessive 26**
- `DOID:0080260` (4 mentions) - the report calls it "Disease Ontology"; DOID calls it **autosomal recessive spinocerebellar ataxia 26**
- `NCIT:C121351` (1 mention) - the report calls it "Fine motor"; NCIT calls it **Occupational Therapy**
- `NCIT:C159273` (1 mention) - the report calls it "Dysarthria"; NCIT calls it **Speech Language Therapy**
- `NCIT:C15240` (1 mention) - the report calls it "AR recurrence 25%"; NCIT calls it **Genetic Counseling**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006977` (obsolete DNA damage response, signal transduction by p53 class mediator resulting in cell cycle arrest) (1 mention) - replaced by `GO:0030330`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:57540` (1 mention) - the report calls it "NAD⁺"; CHEBI calls it **NAD(1-)**, and lists "NAD(+)" among its other names
- `UBERON:0002037` (1 mention) - the report calls it "Primary:** cerebellum"; UBERON calls it **cerebellum**