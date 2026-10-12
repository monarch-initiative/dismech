---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T16:19:10.168413'
end_time: '2026-10-08T16:24:56.392432'
duration_seconds: 346.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1C
  mondo_id: MONDO:0011094
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
  web_search_requests: 5
  num_turns: 26
  total_cost_usd: 2.2760800000000003
  session_id: 5ae2e60c-9914-4702-b719-b7f4a3ac4255
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 3
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
citation_count: 10
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 31
  on_topic: 14
  off_topic: 1
  off_topic_references:
  - PMID:22992465
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 9
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: DOID:0110423
    reported_labels:
    - Disease Ontology
    ontology_label: dilated cardiomyopathy 1C
  - term_id: MONDO:0979236
    reported_labels:
    - DCM 2L
    ontology_label: cardiomyopathy, dilated, 2l
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1C
- **MONDO ID:** MONDO:0011094 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1C** covering all of the
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

Still gathering sources: checking which LDB3 papers are already cached here before searching the web.

Reading the rest of the OMIM text for CMD1C and LDB3, then searching for the mouse and functional studies.

# Research report: Dilated Cardiomyopathy 1C (CMD1C; LDB3/ZASP/Cypher)

**Date compiled:** 2026-10-08. **Target:** MONDO:0011094, dilated cardiomyopathy 1C.

**Before using this report:**
- **The gene–disease link is weak.** ClinGen's Dilated Cardiomyopathy Gene Curation Expert Panel rates LDB3 as **Limited** for dominant DCM. It rates the recessive, loss-of-function form (DCM 2L, a separate entry) as **Strong**. The 2026 ClinGen reassessment (PMID:42708185) says so, and both ClinGen records are already cached in this repository.
- **Two PMIDs are often swapped.** Vatta 2003 is **PMID:14662268**. Arimura 2004 is **PMID:14660611**.
- **Ontology IDs.** The only CURIEs below are ones I confirmed this session from the draft entry, the ClinGen ingest file or the ClinGen cache. Every other ontology term is a label only. Look each one up (runoak or `cache/*/terms.csv`) before binding it.
- **Quotes.** Abstract quotes were taken from PubMed efetch output, which a summarizing model relayed. Before using any of them as a `snippet:`, check it against the cached reference with `just fetch-reference` and `just count-verified-snippets`.
- **What is already cached.** Of the papers below, only these are in `references_cache/`: PMID:15668942, 17097056, 42708185, 27532257, 30980206, 31771441, 33802723, 39337275, the two ClinGen records, and the GeneReviews DCM overview (NBK1309). Everything else needs fetching.

---

## 1. Disease information

**Overview.** CMD1C is an autosomal dominant dilated cardiomyopathy, with or without left ventricular noncompaction (LVNC). It is attributed to heterozygous missense variants in **LDB3**, the gene for ZASP/Cypher. That protein is a PDZ–LIM scaffold at the sarcomeric Z-disc in heart and skeletal muscle.

OMIM #601493 is titled "Cardiomyopathy, dilated, 1C, with or without left ventricular noncompaction". The same OMIM entry also covers:
- **LVNC3** (left ventricular noncompaction 3)
- **CMH24** (familial hypertrophic cardiomyopathy 24)

The OMIM clinical synopsis lists:
- **Heart:** left ventricular dilation; noncompaction, hypertrophy or a sigmoid septum in some patients; congestive heart failure; ventricular arrhythmia and sudden cardiac death in some patients.
- **Biopsy:** moderate to marked myocyte hypertrophy, mild to moderate endocardial fibrosis, and focal myocyte disarray.

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0011094 (dilated cardiomyopathy 1C) |
| OMIM (phenotype) | #601493 |
| OMIM (gene) | *605906 LDB3 |
| Disease Ontology | DOID:0110423 |
| Orphanet | ORPHA:154 (familial isolated DCM), ORPHA:54260 (LVNC). These are cross-references from OMIM; there is no CMD1C-specific ORPHA code. |
| ICD-10-CM | I42.0 (dilated cardiomyopathy), via DOID |
| Gene | LDB3, hgnc:15710, 10q23.2 (GRCh38 chr10:86,666,788–86,736,072) |

**Synonyms:** CMD1C; dilated cardiomyopathy 1C with or without LVNC; LDB3-related (ZASP-related, Cypher-related) dilated cardiomyopathy; zaspopathy (cardiac form).

**Source type.** All of this information comes from published families and cohorts and from disease-level resources (OMIM, ClinGen). No EHR or registry-derived data exist.

Sources: [OMIM 601493 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/601493); [Disease Ontology DOID:0110423](https://disease-ontology.org/term/DOID:0110423/).

## 2. Etiology

**Causal factor.** Heterozygous germline missense variants in LDB3 (OMIM .0004–.0006, .0009) are the cause.

Vatta et al. 2003 (PMID:14662268) screened 100 probands with left ventricular dysfunction and found five missense mutations in six of them. None of the mutations was present in 200 controls. Their quoted result: *"Five mutations in six probands (6% of cases) were identified in patients with familial or sporadic DCM or INLVM."* Their conclusion: *"These data suggest that mutated Cypher/ZASP can cause DCM and INLVM and identify a mechanistic basis."*
- OMIM summarizes the carriers as 2 with DCM alone and 4 with DCM plus LVNC. One secondary source describes the cohort differently, so confirm the split against the full text.

**How strong is the gene–disease evidence?**

| Disease | Inheritance | ClinGen class | Record |
|---|---|---|---|
| DCM 1C (MONDO:0011094) / DCM (MONDO:0005021) | AD | **Limited** | CGGV:assertion_7756e3c0-… (cached) |
| DCM 2L (MONDO:0979236) | AR | **Strong** | CGGV:assertion_c9d89b2d-… (cached) |
| Hypertrophic cardiomyopathy (MONDO:0005045) | AD | Disputed | CGGV:assertion_1089e729-… (2026-01-27) |
| ARVC (MONDO:0016587) | AD | Disputed | CGGV:assertion_8ebdc3e8-… (2019) |

The 2026 ClinGen reassessment (PMID:42708185, cached) states: *"Four previously evaluated genes were curated for both AD and AR MOIs: JPH2 (AD-Strong, AR-Limited), LDB3 (AD-Limited, AR-Strong), MYBPC3 (AD-Limited, AR-Limited), and TNNI3 (AD- and AR- Strong)."*

**Variants that have been questioned.**
- **D117N** (OMIM .0007) did not segregate with disease in Bedouin families and is common in the population (Levitas 2016, PMID:26419279). The quoted conclusion: *"our data support the notion that the p.(D117N) variant in Cypher/ZASP is not a causative mutation"*.
- The population-scale reassessment of cardiomyopathy genes (Walsh 2017, PMID:27532257, cached) is the expected source for the absence of a case excess for LDB3. I have not checked its full text for an LDB3-specific figure.

**Risk and modifier factors.**
- LDB3 polymorphisms have been studied as modifiers of clinical presentation and ICD outcomes (Wang 2019, PMID:31379146). This is association data only.
- **Oligogenic cases.** One young-onset DCM case with sudden cardiac death carried LDB3 p.M456R together with MYH6 and SYNE1 variants (Zhao 2021, PMID:33949037). Separately, one Barth syndrome family carried a TAZ variant and an LDB3 variant together (Marziliano 2007, PMID:17394203).
- **Environmental risk factors.** None are documented.
- **Protective factors.** None are documented.
- **Gene–environment interactions.** None are documented. One case report describes subtle cardiac involvement in LDB3-related myopathy that was unmasked after COVID-19 (Gadaleta 2025, PMID:40626683). This is anecdotal.

## 3. Phenotypes

The evidence comes from small family series, so frequencies are only qualitative ("some patients", per OMIM).

| Phenotype | HPO label (verify ID) | Notes |
|---|---|---|
| Dilated cardiomyopathy | Dilated cardiomyopathy (HP:0001644, confirmed in draft) | Core feature; onset ranges from adolescence to late adulthood (D626N was late-onset, PMID:14660611) |
| LV dilation | Left ventricular dilatation | OMIM synopsis |
| LV noncompaction | Left ventricular noncompaction | Present in some probands (PMID:14662268; D626N in a Japanese LVNC family, PMID:16427346) |
| Congestive heart failure | Congestive heart failure | OMIM |
| Reduced ejection fraction | Reduced left ventricular ejection fraction / systolic dysfunction | Vatta cohort definition |
| Ventricular arrhythmia | Ventricular arrhythmia | Some patients |
| Sudden cardiac death | Sudden cardiac death | Some patients |
| Conduction defect / AV block | Atrioventricular block | Seen in the S196L mouse (PMID:20852297). Human data are sparse. |
| LV hypertrophy, sigmoid septum | Left ventricular hypertrophy; asymmetric septal hypertrophy | Belongs to the CMH24 allelic form. Z-disc HCM "is associated preferentially with sigmoidal morphology" (PMID:17097056, cached). |
| Myocardial fibrosis, myocyte hypertrophy, disarray | Endocardial fibrosis; myocardial fibrosis | Biopsy findings |
| Skeletal myopathy | Distal muscle weakness; myofibrillar myopathy | Belongs to the allelic MFM4 form. Cardiac involvement occurred in 3 of 11 MFM4 patients (PMID:15668942, cached). Whether CMD1C patients have subclinical myopathy is unresolved (Finsterer letter, PMID:15337232). |

**Quality of life.** No LDB3-specific data exist. Burden follows the usual course of DCM: heart failure symptoms (NYHA class), arrhythmia, ICD shocks and transplantation.

## 4. Genetic and molecular information

**Gene.** LDB3, also called ZASP, CYPHER or KIAA0613; hgnc:15710; OMIM 605906.
- The protein has an N-terminal PDZ domain, an internal ZASP-like motif (ZM, which binds actin) and three C-terminal LIM domains (which bind PKC).
- Alternative splicing produces short isoforms without LIM domains and long isoforms with them, in cardiac-specific and skeletal-specific classes (Huang 2003, PMID:12499364).

**Variants.** HGVS numbering differs between OMIM and RefSeq: OMIM's S196L is p.Ser189Leu on NM_007078, and T213I is Thr206Ile.

| OMIM | Protein change | Phenotype | Reference |
|---|---|---|---|
| .0004 | I352M | CMD1C, AD family | PMID:14662268 |
| .0005 | S196L (p.S189L) | CMD1C with LVNC; also CMH24 | PMID:14662268; PMID:17097056 |
| .0006 | T213I (p.T206I) | CMD1C with LVNC | PMID:14662268 |
| .0007 | D117N | Doubtful pathogenicity | PMID:26419279 |
| .0009 | D626N | Late-onset DCM in Japan; LVNC family | PMID:14660611; PMID:16427346 |
| — | c.1051A>G | ARVC family | PMID:25041374 (ClinGen: Disputed) |
| .0001–.0003 | A147T, A165V, R268C | MFM4 (skeletal; sometimes cardiac) | PMID:15668942 |

- **Variant type:** missense, germline.
- **Proposed effect:** gain of function or altered binding (D626N increases PKC affinity), not haploinsufficiency. Heterozygous parents of the biallelic loss-of-function cases appear unaffected (PMID:36253531; PanelApp Australia), which argues against haploinsufficiency as the dominant mechanism.
- **ClinVar.** Classifications are mostly VUS or conflicting; p.Ser189Leu has 13 submissions ([ClinVarMiner](https://clinvarminer.genetics.utah.edu/submissions-by-variant/NM_007078.3%28LDB3%29%3Ac.566C%3ET%20%28p.Ser189Leu%29)).
- **Not established:** gnomAD frequencies for each variant (I did not retrieve them), epigenetic contributions, and any chromosomal abnormality.

## 5. Environmental information

There are no known environmental, lifestyle or infectious causes. The general DCM cofactors (alcohol, cardiotoxic chemotherapy, myocarditis, pregnancy) would plausibly unmask disease, but no LDB3-specific study supports this. If the entry needs an `environmental:` block, mark it uncited.

## 6. Mechanism and pathophysiology

**Causal chain** (each step marked demonstrated or inferred):

1. A heterozygous LDB3 missense variant changes ZASP/Cypher in the PDZ region, the exon 4 region (S189L, T206I) or the LIM region (D626N). *(Human genetics, PMID:14662268.)*
2. This **alters ZASP's protein interactions**:
   - (2a) D626N **increases LIM-domain affinity for PKC**. Quote: *"the D626N mutation of Cypher/ZASP increased the affinity of the LIM domain for protein kinase C"* (PMID:14660611, in vitro).
   - (2b) S189L and T206I **reduce binding of PGM1**. Quote: *"ZASP/Cypher anchors PGM1 to Z-disc under conditions of stress"* (PMID:19377068, in vitro).
   - (2c) ZASP is an **A-kinase anchoring protein (AKAP)** that is phosphorylated by PKA at Ser265 and Ser296 (PMID:23996002). DCM variants may disturb PKA signalling (phosphoproteomics, PMID:34966794).
3. This leads to **Z-disc and cytoskeletal disorganization**. Transfected mutant ZASP produced cytoskeletal disarray (PMID:14662268, in vitro). Knockout mice show fragmented Z-lines: Cypher *"functions as a linker-strut to maintain cytoskeletal structure during contraction"* (PMID:11696561, mouse).
4. This leads to **impaired force transmission and maladaptive stress signalling** in cardiomyocytes. Cardiac knockouts show increased ERK and Stat3 activity (PMID:19028670). Loss of the long isoforms disturbs calcineurin–NFAT and PKC signalling (PMID:21303826). Cypher deficiency destabilizes F-actin and impairs MRTFA–SRF-driven cardiomyocyte maturation (PMID:39113806). Knockdown causes apoptosis through Akt/p38 MAPK (PMID:32922198, in vitro). *These are mostly loss-of-function models; applying them to dominant missense variants is an inference.*
5. **Branch, electrical:** ZASP sits in a complex with cardiac ion channels. S196L knock-in mice develop *"cardiac conduction defects and atrioventricular block"* (PMID:20852297), which leads to arrhythmia and sudden death.
6. **Branch, developmental (inferred):** abnormal compaction of the ventricular myocardium leads to LVNC. Cypher and its homolog ENH are needed for cardiac development (PMID:25944877, mouse).
7. Cardiomyocyte loss, hypertrophy and fibrosis lead to **LV dilation and systolic dysfunction (DCM)**, which leads to heart failure.

**Suggested terms (labels only; verify IDs).**
- **GO:** sarcomere organization; Z disc (cellular component); actin filament organization; protein kinase C binding; protein kinase A binding; cardiac muscle contraction; regulation of cardiac conduction.
- **CL:** cardiac muscle cell (cardiomyocyte); skeletal muscle fiber, for MFM4.
- **Molecular profiling:** no CMD1C omics datasets were found. One forensic RNA-seq study reported abnormal LDB3 splicing in sudden cardiac death (PMID:31419596).

## 7. Anatomy

- **Primary site:** heart, specifically the left ventricular myocardium and the interventricular septum.
- **Secondary site:** skeletal muscle in the allelic spectrum.
- **Tissue and cell level:** cardiac muscle tissue and cardiomyocytes.
- **Subcellular level:** Z disc, I band, costamere.
- **Distribution:** cardiac involvement is global, biventricular or left-dominant. Myopathy in MFM4 is bilateral and distal-predominant.

## 8. Timing

- **Onset:** variable, from childhood to late adulthood. D626N was a late-onset familial case (PMID:14660611).
- **Course:** insidious onset, chronic, and progressive into heart failure.
- **Remission:** no spontaneous remission. Remodelling may partly reverse on guideline-directed medical therapy (GDMT); there are no LDB3-specific data.
- **Contrast with the recessive form:** biallelic loss of function (DCM 2L) causes severe disease in infancy and childhood, sometimes in the fetus, and is often lethal (PMID:36253531).

## 9. Inheritance and population

- **Inheritance:** autosomal dominant with incomplete, age-dependent penetrance and variable expression (DCM, LVNC or HCM within the same allelic group).
- **Prevalence:** unknown. LDB3 is a rare contributor to DCM. The 6% yield in Vatta's cohort was not replicated in later large studies, which is reflected in the Limited classification.
- **Founder effects:** the founder haplotype reported for LDB3 belongs to the A165V distal myopathy (PMID:17337483), not to CMD1C.
- **Population data:** probands have been reported from US, Japanese, Chinese and Bedouin populations. No sex ratio data exist.

## 10. Diagnostics

**Clinical workup**
- Echocardiography and cardiac MRI (LV dilation, LVEF, noncompaction ratio, late gadolinium enhancement)
- ECG and Holter monitoring (conduction disease, ventricular arrhythmia)
- NT-proBNP
- Creatine kinase (CK) and neurological examination to screen for myopathy
- Endomyocardial biopsy is rarely needed

**Genetic testing**
- Use a multigene DCM panel or exome sequencing. LDB3 is on most panels but is rated amber for DCM on Genomics England PanelApp ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/238/gene/LDB3)).
- Report heterozygous LDB3 missense variants cautiously. Most are VUS, and the dominant gene–disease link is Limited.

**Differential diagnosis**
- Other dilated cardiomyopathies (TTN, LMNA, RBM20, FLNC, BAG3)
- Isolated LVNC (MYH7, MIB1)
- ACTN2- and MYPN-related Z-disc cardiomyopathies
- Myofibrillar myopathies (DES, CRYAB, MYOT, FLNC)
- Barth syndrome

**Screening:** cascade screening of relatives with imaging and ECG, and genotyping only when the variant is classified actionable. GeneReviews' DCM overview (NBK1309, cached) is the general baseline.

## 11. Outcome and prognosis

There are no LDB3-specific survival data. Risks are those of DCM in general: progressive heart failure, ventricular arrhythmia, sudden cardiac death and transplantation. Severe early cases with sudden death have been reported (PMID:33949037). Without an LDB3-specific series, prognostic factors default to general DCM markers: LVEF, LGE scar and non-sustained VT.

## 12. Treatment

Care follows standard heart failure guidelines. There is no LDB3-targeted therapy. NCIT labels below are to be verified.

| Treatment | NCIT action term (verify) | Agents |
|---|---|---|
| GDMT for heart failure | Pharmacotherapy | ACE inhibitor/ARB/ARNI (sacubitril–valsartan), β-blocker, MRA, SGLT2 inhibitor |
| Anticoagulation in LVNC with thrombus or AF | Pharmacotherapy | Warfarin or DOAC |
| ICD / cardiac resynchronization | No NCIT device action term; use Surgical Procedure plus a device qualifier | — |
| Heart transplantation | Organ Transplantation | — |
| Genetic counselling | Genetic Counseling | — |

- **Gene, RNA and cell therapies:** none.
- **Clinical trials:** none specific to LDB3.
- **Pharmacogenomics:** none specific to LDB3.

## 13. Prevention

- **Primary prevention:** not applicable beyond preimplantation or prenatal options, which are rarely justified given the Limited evidence.
- **Secondary prevention:** cascade clinical surveillance of first-degree relatives.
- **Tertiary prevention:** GDMT, ICD to prevent sudden death, and avoidance of cardiotoxins and excess alcohol (general DCM advice).

## 14. Other species

- No naturally occurring LDB3 cardiomyopathy appears in the material I reviewed. I did not search OMIA.
- **Orthologs:** mouse *Ldb3* (Cypher); zebrafish *ldb3a/b* (not reviewed); Drosophila *Zasp52* (knockdown work, PMID:19603185; Zasp regulates integrin activation, PMID:22992465).

## 15. Model organisms

| Model | Phenotype | How well it models the human disease | PMID |
|---|---|---|---|
| Global *Cypher*⁻/⁻ mouse | Death by postnatal day 5; congenital myopathy; ventricular dilatation; fragmented Z-lines | Resembles recessive DCM 2L, not dominant CMD1C | 11696561 |
| Isoform knock-in rescue | A single short or long skeletal isoform rescues lethality, but muscle pathology remains | Isoform biology | 12499364 |
| Cardiac-specific and inducible adult knockouts | Severe DCM and death before 23 weeks; ERK and Stat3 increased | DCM mechanism (loss of function) | 19028670 |
| Long-isoform-specific deletion | Late-onset DCM, growth retardation, NFAT and PKC changes; deleting the short isoforms has no effect | Partially matches the late-onset course | 21303826 |
| *Cypher*/*ENH* double knockout | Embryonic lethal; cardiac development defects | Relevant to LVNC (inferred) | 25944877 |
| **S196L knock-in or transgenic mouse** | Cytoskeletal abnormalities, conduction defects and AV block at 3 months | The **only CMD1C-allele model**; reproduces the arrhythmic phenotype | 20852297 |
| A165V knock-in mouse | Filamin C aggregation; PKCα and TSC2–mTOR changes; Z-disc disassembly | MFM4, not CMD1C | 33742095 |
| Cypher-deficient hPSC cardiomyocytes | F-actin destabilization; impaired maturation through MRTFA–SRF | Human in vitro model of loss of function | 39113806 |

**Main limitation.** Almost all models remove the gene, which matches the recessive DCM 2L disorder. Only the S196L mouse tests a dominant CMD1C missense allele, and no iPSC model of a CMD1C allele has been published. This is a natural `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion for the entry.

---

## Implications for the dismech entry

1. **Draft description.** The current text, "associated with heterozygous LDB3 variants", should state the ClinGen **Limited (AD)** classification. Copy it into `gene_disease_validity` from the cached CGGV record; don't assign it yourself.
   - The cached record (`CGGV:assertion_7756e3c0-…-2025-03-21T040000.000Z`) is mapped to the generic DCM term MONDO:0005021.
   - The ingest file instead shows a 2026-03-04 record mapped to **MONDO:0011094**, this entry's own disease term.
   - Fetch or rebuild that newer record before citing it.
2. **Scope.** Keep DCM 2L (biallelic loss of function) out of this entry or link it as a separate disease. HCM (CMH24) and LVNC3 are the same OMIM entry. A `has_subtypes` block, or notes covering the allelic spectrum, would fit.
3. **References to fetch:** PMID:14662268, 14660611, 19377068, 20852297, 11696561, 19028670, 21303826, 26419279, 16427346, 23996002, 39113806, 36253531.

---

## Sources

- Vatta et al. 2003, JACC, PMID:14662268 — [UMN record](https://experts.umn.edu/en/publications/mutations-in-cypherzasp-in-patients-with-dilated-cardiomyopathy-a/)
- [OMIM #601493 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/601493); [OMIM *605906 LDB3 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/605906)
- [Disease Ontology DOID:0110423](https://disease-ontology.org/term/DOID:0110423/)
- [GenCC submission](https://thegencc.org/submissions/SGC-117357.1)
- ClinGen DCM GCEP 2026 reassessment, Circulation, PMID:42708185 (cached)
- [Koopmann et al., biallelic LDB3 loss (PMC9823012)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9823012/), PMID:36253531
- [PanelApp Australia, LDB3](https://panelapp-aus.org/panels/3270/gene/LDB3/); [Genomics England PanelApp, LDB3](https://panelapp.genomicsengland.co.uk/panels/238/gene/LDB3)
- [ClinVarMiner, p.Ser189Leu](https://clinvarminer.genetics.utah.edu/submissions-by-variant/NM_007078.3%28LDB3%29%3Ac.566C%3ET%20%28p.Ser189Leu%29)
- [bioRxiv 2025 preprint, LDB3 in an Indian DCM cohort](https://www.biorxiv.org/content/10.1101/2025.10.21.683814.full.pdf) (not peer-reviewed)
- PubMed abstracts retrieved through NCBI E-utilities, cited by PMID throughout.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 31 |
| On topic | 14 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:22992465` (1 mention) - Zasp regulates integrin activation.
  - shared terms: zasp

Weighed against this report's own most characteristic terms: `dcm`, `ldb3`, `cardiac`, `disease`, `lvnc`, `ventricular`, `cmd1c`, `cached`, `cypher`, `gene`, `heart`, `death`, `dominant`, `variant`, `zasp`, `clingen`, `failure`, `sudden`, `missense`, `myopathy`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 9 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0110423` (6 mentions) - the report calls it "Disease Ontology"; DOID calls it **dilated cardiomyopathy 1C**
- `MONDO:0979236` (1 mention) - the report calls it "DCM 2L"; MONDO calls it **cardiomyopathy, dilated, 2l**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0016587` (1 mention) - the report calls it "ARVC"; MONDO calls it **arrhythmogenic right ventricular cardiomyopathy**, and lists "ARVD" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.