---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T16:19:10.166725'
end_time: '2026-10-08T16:23:14.084951'
duration_seconds: 243.92
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1M
  mondo_id: MONDO:0011840
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
  web_search_requests: 11
  num_turns: 30
  total_cost_usd: 2.3519769999999998
  session_id: 35b5c55c-a919-4bc0-9931-0926ba0b3da2
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 2
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
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 14
  on_topic: 13
  validator_version: 0.3.0
term_validation:
  total_terms: 23
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001635
    reported_labels:
    - verify
    ontology_label: Congestive heart failure
  - term_id: HP:0001706
    reported_labels:
    - verify
    ontology_label: Endocardial fibroelastosis
  - term_id: HP:0001712
    reported_labels:
    - verify
    ontology_label: Left ventricular hypertrophy
  labels_variant: 2
  unresolvable_prefixes:
  - MIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1M
- **MONDO ID:** MONDO:0011840 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1M** covering all of the
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

The local cache holds the two primary dilated-cardiomyopathy papers on CSRP3 (Knöll 2002 and Mohapatra 2003). I'm reading their abstracts now so I can quote them exactly.

# Dilated Cardiomyopathy 1M (CMD1M; MONDO:0011840): Research Report

*Prepared 2026-10-08 for the dismech entry `kb/disorders/Dilated_Cardiomyopathy_1M.yaml`.*

**Provenance and limits.**
- **Quoted text.** The abstract quotes for PMID:12507422, PMID:14567970, PMID:18505755, PMID:30681346, PMID:39132495 and PMID:38666070 come from the repository's own `references_cache/` files. They are safe to use as snippets.
- **Paraphrased text.** Claims attributed to PMID:9039266, PMID:20044516, PMID:19412328, PMID:10555147 and PMID:31406109 were paraphrased from web search results. None of these is cached yet. Run `just fetch-reference` and take the quote from the cache before using any of them as evidence.
- **ClinGen.** The ClinGen DCM curation was read from the live ClinGen website (assertion dated 2026-03-04). It is not in the local cache.
- **Ontology IDs.** The repo rule is "never write a CURIE from memory". Every ontology CURIE below is marked as either **confirmed**, meaning seen in a source during this research, or **verify**, meaning it must be checked with a lookup before binding.

---

## Executive summary: the entity is weakly supported

CMD1M is an OMIM *provisional* phenotype. It is listed as "?Cardiomyopathy, dilated, 1M" (MIM:607482) and attributed to heterozygous variants in **CSRP3**. CSRP3 encodes muscle LIM protein (MLP), on chromosome 11p15.1.

The DCM association is weak, while the same gene's association with **hypertrophic** cardiomyopathy is Definitive:

| Gene–disease pair | ClinGen classification | Expert panel / date |
|---|---|---|
| CSRP3 – dilated cardiomyopathy 1M (MONDO:0011840), AD | **Limited** | DCM GCEP. Evaluated 2020-11-06, re-evaluated under SOP v10 on 2025-05-30 with no change of tier, report dated 2026-03-04 |
| CSRP3 – hypertrophic cardiomyopathy (MONDO:0005045), **semi-dominant** | **Definitive** | Hereditary Cardiovascular Disease GCEP, 2023-08-09 (`CGGV:assertion_012b9b15-…-2023-08-09T160000.000Z`, cached) |

The ClinGen DCM curation scores **0.4 genetic points**:
- Hershberger 2008 p.Gly72Arg; Trachoo 2022 p.Glu191Lys; Zimmerman 2010 p.Ala50Thr and p.Thr179Ala, at 0.1 each.
- Mohapatra 2003 p.Lys69Arg scored 0, as a possible phenocopy.
- Case–control data from Walsh 2017 and Mazzarotto 2020 scored 0, because neither showed enrichment of CSRP3 variants in DCM cases.

It scores **3.5 experimental points**, from the MLP-knockout mouse (Arber 1997) and the T-cap interaction defect (Knöll 2002). ClinGen's conclusion is that "there is limited convincing genetic evidence that has directly implicated this gene in human disease" and that "More evidence is needed to support the relationship of CSRP3 and AD DCM."

One web search result (a GenCC summary) said the 2025 re-evaluation changed the tier to "no known disease relationship". **The live ClinGen report contradicts this:** it says the tier stayed Limited. Use ClinGen.

The founding variant, **W4R (p.Trp4Arg)**, is a common European polymorphism. It occurs in up to ~1% of Caucasians and in gnomAD heterozygotes, including at least one homozygote. Two studies weaken it as a cause of DCM:
- It did not segregate with DCM in the Mohapatra 2003 family (PMID:14567970).
- Geier et al. 2008 found it at similar rates in DCM cases (3/652), HCM cases (2/354) and controls (2/533) (PMID:18505755 era work, reported via OMIM and PanelApp).

Genomics England PanelApp lists CSRP3 as red (low evidence) for DCM.

**Curation implications:**
1. A `gene_disease_validity` assertion of `LIMITED`, `classified_by: CLINGEN`, AD, with the ClinGen DCM assertion ID. Run `just clingen-rebuild --id <CGGV id>` first so it can be cited.
2. Keep `relationship_type` off `CAUSATIVE`. `CAUSATIVE` means Definitive or Strong, and `just check-gene-validity` would flag it as `overstated`.
3. A `KNOWLEDGE_GAP` discussion on whether CMD1M exists as a distinct Mendelian DCM.
4. Much of the mechanistic and model literature is DCM in the *knockout mouse*, while human CSRP3 disease is mainly HCM. That is a `HUMAN_MODEL_MISMATCH`.

---

## 1. Disease information

- **Definition.** Autosomal dominant dilated cardiomyopathy attributed to heterozygous missense variants in CSRP3/MLP, a Z-disc and costamere LIM-only protein involved in sensing cardiomyocyte stretch. Clinically it is non-syndromic DCM: left ventricular dilation and systolic dysfunction leading to heart failure.
- **Identifiers:**
  - MONDO:0011840 "dilated cardiomyopathy 1M" (confirmed: existing YAML and ClinGen).
  - OMIM #607482, provisional "?" (confirmed).
  - Gene: CSRP3, OMIM *600824, **hgnc:2472** (confirmed, ClinGen).
  - Not verified: a separate Orphanet code (likely only the umbrella "familial isolated DCM"), and ICD-10 I42.0 for dilated cardiomyopathy.
- **Synonyms.** CMD1M; Cardiomyopathy, dilated, 1M; CSRP3-related dilated cardiomyopathy; MLP-related DCM.
- **Allelic disorder.** Hypertrophic cardiomyopathy 12 (CMH12, MIM:612124) is caused by CSRP3 and is better established.
- **Data basis.** Aggregated disease-level resources (OMIM, ClinGen) and small case series. There are no EHR cohorts.

## 2. Etiology

- **Causal factor.** Heterozygous germline CSRP3 missense variants. The reported variants are W4R, K69R, G72R, A50T, T179A and E191K.
- **Genetic risk and modifiers.** W4R behaves as a common, low-penetrance or benign variant in humans. In mice it causes dose-dependent cardiomyopathy (PMID:20044516). Variants in interaction partners have been proposed as modifiers or co-contributors, but this is unproven:
  - TCAP (hgnc:11610): ClinGen rates it Disputed for HCM (cached CGGV `c35abc20`).
  - ACTN2: Mohapatra reported an ACTN2 Q9R variant that disrupts MLP binding.
- **Environmental factors.** No specific exposures are documented. In mice, catecholamine stress reveals the W4R phenotype ("lost almost all contractile reserve"; PMID:20044516, paraphrased). This is a model-level gene–environment interaction, plausibly relevant to adrenergic load in humans. It is an inference, not demonstrated in humans.
- **Protective factors.** None documented in humans. In mice, removing phospholamban rescued MLP−/− DCM (PMID:10555147). That is a genetic rescue in the mouse, not a protective human variant.

## 3. Phenotypes

The human data come from roughly 10 or fewer probands, so frequencies cannot be estimated.

| Phenotype | Suggested HPO (status) | Notes |
|---|---|---|
| Dilated cardiomyopathy | HP:0001644 Dilated cardiomyopathy (**confirmed** in existing YAML) | Core feature; adult onset in most reports |
| Congestive heart failure | HP:0001635 (verify) | Knöll 2002: "defects in the complex can lead to human DCM and associated heart failure" (PMID:12507422) |
| Reduced LV systolic function | e.g. "Abnormal left ventricular function"; check for an "ejection fraction" HP term (verify) | — |
| Endocardial fibroelastosis | HP:0001706 (verify) | One K69R patient with "DCM and EFE" (PMID:14567970) |
| Ventricular arrhythmia / sudden death | HP:0004308, HP:0001645 (verify) | Generic to DCM; not documented specifically for CMD1M |
| Mild skeletal myopathy | e.g. HP:0003198 Myopathy (verify) | Reported in CSRP3 *HCM* carriers (PMID:18505755) and W4R mice (PMID:20044516); not documented in CMD1M |
| Left ventricular hypertrophy (allelic HCM) | HP:0001712 (verify) | Belongs to CMH12, not CMD1M; bind it only if the entry spans the spectrum |

Quality of life: no CMD1M-specific data. DCM-related heart failure generally lowers NYHA class and health-related quality of life.

## 4. Genetic and molecular information

- **Gene.** CSRP3 at 11p15.1, 6 exons spanning ~20 kb (Knöll 2002, via OMIM). It encodes a 194-aa protein with two LIM domains, expressed only in striated muscle.

**Variants reported in DCM:**

| Variant | Source | Evidence | ClinGen score |
|---|---|---|---|
| p.Trp4Arg (W4R, c.10T>C) | Knöll 2002 (10 DCM patients) | Defective T-cap binding. Common in controls and gnomAD; did not segregate with DCM (PMID:14567970). | Not scored; reported in controls |
| p.Lys69Arg (K69R) | Mohapatra 2003 | "abolishes the interaction between MLP and alpha-actinin-2" (PMID:14567970) | 0 (possible phenocopy) |
| p.Gly72Arg | Hershberger 2008 (PMID:19412328) | — | 0.1 |
| p.Ala50Thr, p.Thr179Ala | Zimmerman 2010 (PMID:20474083) | — | 0.1 each |
| p.Glu191Lys | Trachoo 2022 (PMID:36166435) | — | 0.1 |

- **Classification.** ClinVar treats CSRP3 DCM variants mostly as VUS. One ClinVar record notes that "loss of function of CSRP3 has not been clearly established as a mechanism of disease".
- **Origin and mechanism.** All reported variants are germline. The functional class is unclear:
  - Partial loss of function or destabilisation: reduced MLP protein in W4R mice; HCM mutants destabilised (PMID:18505755).
  - Interaction loss: T-cap, α-actinin-2.
  - In schema terms, `PARTIAL_LOSS_OF_FUNCTION` is the most defensible category, labelled as inferred.
- **Inheritance across the CSRP3 spectrum.** Biallelic CSRP3 truncating variants cause adult HCM (6 reported cases; PMID:38666070). ClinGen accordingly curates CSRP3–HCM as semi-dominant (PMID:39132495).
- **Not reported.** Epigenetic or chromosomal mechanisms: none.

## 5. Environmental information

None reported. No infectious, toxic or lifestyle causes. Adrenergic and pressure stress unmask the phenotype in model systems only (section 2).

## 6. Mechanism and pathophysiology

**Causal chain:**

1. A heterozygous CSRP3 missense variant (e.g. W4R in the N-terminus; K69R next to LIM1) **leads to** reduced MLP abundance or stability and/or loss of binding to partners: T-cap/telethonin at the Z-disc (W4R; PMID:12507422) and α-actinin-2 (K69R; PMID:14567970). *Demonstrated in vitro and in mice. In-patient protein destabilisation has been shown only for HCM variants.*
2. The loss of the Z-disc MLP/T-cap complex **impairs** cardiomyocyte mechanical stretch sensing. Knöll 2002: "a Z disc MLP/T-cap complex is a key component of the in vivo cardiomyocyte stretch sensor machinery" (PMID:12507422; MLP−/− mice and cells).
3. Defective stretch-responsive signalling and cytoarchitecture **result in** cytoskeletal and sarcomeric disorganisation and abnormally compliant myocardium. In MLP−/− mice, newborn hearts are "abnormally soft" with "dramatic disruption of cardiomyocyte cytoarchitecture" before hypertrophy (PMID:9039266, paraphrase). Increased nuclear localisation of the mutant protein may change transcriptional co-regulation (W4R mice; PMID:20044516). *This is inferred.*
4. **Branch: calcium cycling.** Chronic phospholamban–SERCA2a inhibition in the MLP-deficient heart **drives** progressive dilation; phospholamban ablation rescues it (PMID:10555147; mouse). MLP-null human ESC-derived cardiomyocytes show abnormal Ca²⁺ handling (PMID:31406109).
5. These changes **lead to** eccentric remodelling and LV dilation with systolic dysfunction (DCM), and then heart failure. In humans, the outcome depends on genotype and context: the same pathway more often gives HCM (PMID:18505755), and W4R mice and MLP-null hESC-cardiomyocytes develop HCM-like phenotypes. *That is the central human–model mismatch.*

**Suggested terms:**
- **GO processes (verify):** cellular response to mechanical stimulus (GO:0071260); sarcomere organization (GO:0045214); regulation of calcium ion transport / regulation of the force of heart contraction; cardiac muscle hypertrophy.
- **GO cellular components:** Z disc (GO:0030018, verify); costamere; nucleus.
- **Cell type:** cardiac muscle cell / cardiomyocyte (CL:0000746, verify).
- **Proteins:** MLP/CSRP3 (hgnc:2472, confirmed); T-cap/TCAP (hgnc:11610, confirmed); α-actinin-2/ACTN2 (verify); β-spectrin and zyxin are also reported partners.
- **Molecular profiling:** no CMD1M-specific transcriptomic or proteomic datasets were found. RNA-seq exists for Mlp-C58G knock-in mice, an HCM variant model (Oxford Cardioscience).

## 7. Anatomical structures

- **Primary:** heart, left ventricle (UBERON:0002084 heart left ventricle, verify), myocardium, endocardium (EFE case).
- **Secondary:** possibly skeletal muscle (mild myopathy, HCM and mouse data); systemic effects of heart failure.
- **Subcellular:** Z-disc, costamere, sarcolemma, nucleus.
- **Laterality:** bilateral or global ventricular involvement.

## 8. Temporal development

- **Onset.** Adult in most reports; one paediatric DCM/EFE case (K69R).
- **Course.** Progressive, from insidious systolic dysfunction to symptomatic heart failure. No staging or natural history specific to CMD1M exists; use DCM/heart-failure staging (ACC/AHA A–D). In mice the W4R phenotype is age- and dose-dependent.

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant, as asserted by OMIM and ClinGen (HP:0000006 Autosomal dominant inheritance, verify).
- **Penetrance.** Low or incomplete: W4R in controls and failure to segregate. Expressivity is variable across the DCM and HCM spectrum.
- **Prevalence.** Unknown, and extremely rare if the entity is real. The W4R allele is up to ~1% in Europeans, so population carrier frequency greatly exceeds disease frequency, which argues against high penetrance.
- **Not reported:** founder effects, anticipation, sex bias, consanguinity role.

## 10. Diagnostics

- **Imaging and function:** echocardiography or cardiac MRI for LV dilation and reduced EF; ECG and Holter for arrhythmia; NT-proBNP or BNP as a heart-failure biomarker.
- **Genetic testing:** DCM multigene panels or exome sequencing.
  - CSRP3 is on many DCM panels but **should not be reported diagnostically for DCM** at a Limited classification.
  - Variants should be interpreted against gnomAD frequency. W4R is too common to be causal on its own.
  - Exclude Definitive/Strong DCM genes first: TTN, LMNA, MYH7, TNNT2, RBM20, FLNC, BAG3, DSP and others (Jordan et al. 2021, Circulation).
- **Differential diagnosis:**
  - CSRP3-HCM (CMH12) progressing to a burnt-out, dilated phase.
  - Other genetic DCMs.
  - Ischemic, myocarditic, toxic (alcohol, anthracycline) and peripartum DCM.
  - Left ventricular noncompaction.
- **Screening:** cascade echocardiographic screening of first-degree relatives, as for any familial DCM.

## 11. Outcome and prognosis

There are no CMD1M-specific survival data. Expect the course of non-ischemic DCM: risk of heart failure progression, ventricular arrhythmia, sudden death and transplantation. Prognostic markers are generic: LVEF, LGE on cardiac MRI, NYHA class, natriuretic peptides.

## 12. Treatment

All treatment is standard guideline-directed DCM and heart-failure therapy. Nothing is genotype-specific.

**Pharmacotherapy.** Suggested NCIT treatment term: Pharmacotherapy NCIT:C15986, which CLAUDE.md lists. Suggested agents (CHEBI IDs must be looked up):
- β-blockers (e.g. carvedilol, metoprolol, bisoprolol)
- ACE inhibitor, ARB, or sacubitril/valsartan
- Mineralocorticoid receptor antagonists (spironolactone, eplerenone)
- SGLT2 inhibitors (dapagliflozin, empagliflozin)
- Diuretics

**Devices and surgery:**
- ICD and CRT: bind to a clinical-action term such as Surgical Procedure NCIT:C15329, with the device carried as a qualifier, per the repo's device convention.
- Heart transplantation (Organ Transplantation, NCIT:C15289).

**Other:** Genetic Counseling (NCIT:C15240).

**Experimental:** no CSRP3-targeted trials. Phospholamban/SERCA2a modulation is a preclinical concept from the MLP−/− rescue (PMID:10555147). The SERCA2a gene-therapy trials (CUPID) were not CSRP3-specific.

## 13. Prevention

- **Primary:** none.
- **Secondary:** cascade family screening and surveillance echocardiography.
- **Tertiary:** guideline-directed therapy and ICD for sudden-death prevention.
- **Counseling:** genetic counseling should state the weak gene–disease validity, and that predictive testing for CSRP3 DCM variants is not clinically actionable.

## 14. Other species and natural disease

No naturally occurring CSRP3-linked cardiomyopathy was found in OMIA during this search (OMIA not queried directly).

Orthologs: mouse Csrp3 (MGI:1330824, from OMIM's links) and zebrafish csrp3 (ZFIN ZDB-GENE-041010-119). MLP is conserved across vertebrates as a muscle LIM protein.

## 15. Model organisms

| Model | Phenotype | Fidelity / limitations | PMID |
|---|---|---|---|
| Csrp3−/− (MLP-knockout) mouse | Postnatal DCM with hypertrophy and heart failure; disrupted cytoarchitecture. Described as reproducing "the morphological and clinical picture of dilated cardiomyopathy" | Complete null, whereas human DCM is heterozygous missense; homozygous human LoF gives HCM (PMID:38666070). Use `PARTIALLY_RECAPITULATES` and `divergences: SPECIES_MISMATCH` / `SUPRAPHYSIOLOGICAL` dose. | 9039266 |
| MLP−/− × Pln−/− mouse | Rescue of DCM | Mechanistic rescue model (RESCUES) | 10555147 |
| Mlp W4R/+ and W4R/W4R knock-in mouse | Age- and dose-dependent **HCM** and heart failure; loss of contractile reserve under catecholamines; reduced MLP; nuclear localisation of the mutant | Phenotype is HCM, not DCM, and W4R is benign in humans (FAILS_TO_RECAPITULATE for DCM) | 20044516 |
| MLP-null human ESC-cardiomyocytes (CRISPR, H9) | HCM features (enlarged cells, multinucleation, sarcomere disarray), then heart-failure phenotypes, with abnormal Ca²⁺ handling | Human cells, but not patient variants; HCM rather than DCM | 31406109 |
| Mlp-C58G knock-in mouse | Cardiomyopathy (HCM variant) studied by RNA-seq | HCM model | (Oxford; PMID not confirmed) |
| Cell culture (K69R, W4R overexpression) | Lost α-actinin or T-cap interaction; MLP mislocalised | In vitro | 14567970, 12507422 |

---

## Key quotable abstract snippets (verified in `references_cache/`)

- **PMID:12507422** (Knöll 2002, MODEL_ORGANISM/IN_VITRO, with a human variant):
  - "a human MLP mutation (W4R) associated with dilated cardiomyopathy (DCM) results in a marked defect in T-cap interaction/localization"
  - "We propose that a Z disc MLP/T-cap complex is a key component of the in vivo cardiomyocyte stretch sensor machinery, and that defects in the complex can lead to human DCM and associated heart failure."
- **PMID:14567970** (Mohapatra 2003):
  - "We identified a patient with DCM and EFE, having a mutation in MLP with the residue lysine 69 substituted by arginine (K69R)." (HUMAN_CLINICAL)
  - "the mutation abolishes the interaction between MLP and alpha-actinin-2 and the cellular localization of MLP was altered" (IN_VITRO)
  - **REFUTE** for W4R causality: "In another individual with DCM, a W4R mutation was identified. However, this mutation did not segregate with disease in this family."
  - Background quote: "An MLP-deficient mouse has been described; these mice develop dilated cardiomyopathy and heart failure."
- **PMID:18505755** (Geier 2008): "Previous studies have shown an association between CSRP3 missense mutations and either dilated cardiomyopathy (DCM) or HCM, but all these studies were unable to provide comprehensive genetic evidence for a causative role of CSRP3 mutations."
- **PMID:39132495** (ClinGen HCM reappraisal): "CSRP3 was curated for a semi-dominant mode of inheritance (definitive)."
- **PMID:38666070**: "biallelic PTVs in CSRP3 are seemingly associated with HCM in adults (based on six reported cases)"

## Sources

- [ClinGen CSRP3 gene page](https://search.clinicalgenome.org/kb/genes/HGNC:2472) and the [CSRP3–DCM 1M Limited report (2026-03-04)](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_beaafc90-20ef-4c81-ad8f-cfcf69d269ca-2026-03-04T170000.000Z)
- Local cache: `references_cache/CGGV_assertion_012b9b15…` (CSRP3–HCM Definitive), `CGGV_assertion_c35abc20…` (TCAP–HCM Disputed), PMID_12507422, PMID_14567970, PMID_18505755, PMID_30681346, PMID_39132495, PMID_38666070, PMID_27532257
- [OMIM *600824 CSRP3 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/omim/600824)
- [GenCC CSRP3 submission](https://search.thegencc.org/submissions/GENCC_000102-HGNC_2472-MONDO_0005021-HP_0000006-GENCC_100008); its "no known relationship" claim conflicts with ClinGen
- [PanelApp Australia – CSRP3, DCM panel](https://panelapp-aus.org/panels/95/gene/CSRP3/)
- [Knöll 2010, A Common MLP Variant Is Associated With Cardiomyopathy (PMID:20044516)](https://publications.goettingen-research-online.de/ID-414)
- [Arber 1997 MLP-knockout mouse (PMID:9039266), MGI record](https://metadb.riken.jp/metadb/db/mgi_rdf/http://rdf.ncbi.nlm.nih.gov/pubmed/9039266)
- [Minamisawa 1999 phospholamban rescue (PMID:10555147)](https://www.wikigenes.org/e/ref/e/10555147.html)
- [Hershberger 2008 (PMID:19412328)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/bd92c530490f55ed2fd68cfd16ea8c327904c65c/pubmed.ncbi.nlm.nih.gov/19412328/index.html)
- [Li 2019 MLP-deficient hESC-cardiomyocytes (PMID:31406109)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6690906)
- [Indian DCM cohort, CSRP3 preprint (medRxiv 2021)](https://www.medrxiv.org/content/10.1101/2021.11.05.21265852.full.pdf)
- [Mlp-C58G knock-in RNA-seq (Oxford)](https://www.cardioscience.ox.ac.uk/publications/1136363/modal)
- [Jordan et al. 2021 ClinGen DCM gene assessment (UCL Discovery)](https://discovery-pp.ucl.ac.uk/id/eprint/10127451)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001635` (1 mention) - the report calls it "verify"; HP calls it **Congestive heart failure**
- `HP:0001706` (1 mention) - the report calls it "verify"; HP calls it **Endocardial fibroelastosis**
- `HP:0001712` (1 mention) - the report calls it "verify"; HP calls it **Left ventricular hypertrophy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0011840` (3 mentions) - the report calls it "CSRP3 – dilated cardiomyopathy 1M"; MONDO calls it **dilated cardiomyopathy 1M**
- `MONDO:0005045` (1 mention) - the report calls it "CSRP3 – hypertrophic cardiomyopathy"; MONDO calls it **hypertrophic cardiomyopathy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MIM`, `MGI`.