---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T16:19:10.176287'
end_time: '2026-10-08T16:25:38.412545'
duration_seconds: 388.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1L
  mondo_id: MONDO:0011702
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
  web_search_requests: 4
  num_turns: 29
  total_cost_usd: 2.4262885999999995
  session_id: 5a69f01f-fef0-4a0e-afad-c755a181222a
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
citation_count: 11
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 20
  on_topic: 14
  validator_version: 0.3.0
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 6
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: DOID:0110436
    reported_labels:
    - DOID
    ontology_label: dilated cardiomyopathy 1L
  - term_id: NCBITaxon:10036
    reported_labels:
    - Mesocricetus auratus
    - Hamster BIO14.6 / TO-2
    ontology_label: Mesocricetus auratus
  - term_id: NCBITaxon:10090
    reported_labels:
    - Sgcd-null mouse
    - "\u03B1-MHC-S151A transgenic mouse"
    - S151A heterozygous knock-in mouse
    ontology_label: Mus musculus
  - term_id: NCBITaxon:9823
    reported_labels:
    - SGCD-KO pig
    ontology_label: Sus scrofa
  - term_id: NCBITaxon:7227
    reported_labels:
    - "Transgenic fly (human \u03B4-SG S151A)"
    ontology_label: Drosophila melanogaster
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1L
- **MONDO ID:** MONDO:0011702 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1L** covering all of the
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

Still gathering sources; I'm checking for cached ClinGen SGCD records in the repo now.

Cached the key SGCD papers; now reading their titles and abstracts to pull exact quotes.

Mapped all cached papers to their PMIDs; doing one last check on the hamster gene-therapy paper and the cohort studies' SGCD results.

# Dilated Cardiomyopathy 1L (CMD1L; SGCD-related autosomal dominant DCM): research report

**Target:** dilated cardiomyopathy 1L, MONDO:0011702 · **Gene:** SGCD (hgnc:10807) · **Prepared:** 2026-10-08

> **Key finding for curation.** The link between monoallelic SGCD variants and dilated cardiomyopathy is weak and contested.
> - **ClinGen** (DCM GCEP) rates SGCD → "Dilated cardiomyopathy 1L" (AD) as **Limited**, evaluated 2026-03-04. Assertion: `CGGV:assertion_59326e1b-5cc1-4dfe-8d67-3379aa305c40-2026-03-04T170000.000Z`. Human genetic evidence scored 0.25 of 12 points.
> - **Ambry Genetics** lists it on GenCC as **Disputed Evidence** (2023).
> - The founding variant, p.S151A, was found without cardiomyopathy in compound-heterozygous carriers (PMID:19259135).
> - Most of the support comes from **SGCD-null animals** (hamster, mouse, pig). Those animals model the *recessive* loss of the protein, not a heterozygous human state.
>
> An entry should state this uncertainty openly: a `gene_disease_validity` block copied from ClinGen, plus a `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH` discussion. A cleanly causal Mendelian claim would overstate the evidence.
>
> One discrepancy is unresolved. A web-search summary said ClinGen had downgraded the gene to "No Known Disease Relationship" in March 2025. The live ClinGen page and GenCC both show **Limited**, dated 2026-03-04. I treated the live record as authoritative. Re-check it when the entry is written.

---

## 1. Disease information

**Overview.** CMD1L is a proposed autosomal dominant form of isolated dilated cardiomyopathy: left ventricular dilatation with systolic dysfunction and no skeletal muscle disease. It is attributed to heterozygous variants in SGCD, which encodes δ-sarcoglycan, part of the dystrophin–glycoprotein complex (DGC). The founding report described severe childhood or young-adult disease with heart failure, transplantation and sudden death (Tsubata et al. 2000, PMID:10974018).

> "Mutations affecting the secondary structure were identified in one family and two sporadic cases, whereas immunofluorescence analysis of myocardium from one of these patients demonstrated significant reduction in delta-sarcoglycan staining. No skeletal muscle disease occurred in any of these patients." (PMID:10974018)

**Identifiers**

| System | ID | Source checked |
|---|---|---|
| MONDO | MONDO:0011702 "dilated cardiomyopathy 1L" | `cache/mondo/terms.csv` |
| OMIM (phenotype) | 606685 | GenCC Ambry submission |
| OMIM (gene) | 601411 (SGCD) | OMIM mirror |
| HGNC | hgnc:10807 (SGCD) | `cache/hgnc/terms.csv` |
| Orphanet | ORPHA:154 Familial isolated dilated cardiomyopathy (gene-level grouping) | GenCC |
| DOID | DOID:0110436 | GlyCosmos page |
| MONDO parents | MONDO:0700335 familial isolated DCM; MONDO:0016144 qualitative or quantitative defects of delta-sarcoglycan | stub file |

**Synonyms** (from the stub): CMD1L; cardiomyopathy, dilated, 1L; dilated cardiomyopathy type 1L; SGCD familial isolated dilated cardiomyopathy; familial isolated DCM caused by mutation in SGCD.

**Data provenance.** All of the evidence is aggregated, disease-level literature: case reports, small families and cohort screens. There are no EHR-derived data.

**Allelic disorder.** Biallelic SGCD loss causes autosomal recessive limb-girdle muscular dystrophy type 2F (LGMDR6; MONDO:0011028; OMIM 601287). ClinGen rates that link **Definitive** (2024-11-14).

## 2. Etiology

- **Causal factor (proposed):** heterozygous germline SGCD missense or in-frame variants.
  - Founding variants: p.S151A (c.451T>G, exon 6) in one family, and p.ΔK238 (3-bp deletion in exon 9) in two sporadic cases (PMID:10974018).
  - Later variants: p.R71T in a Finnish family (PMID:14564412); a splice variant c.4-1G>A, functionally confirmed and reclassified as likely pathogenic (PMID:36270459).
- **Contribution to DCM is marginal.** Sylvius et al. screened 99 DCM probands and found no causal variants (PMID:12794684):
  > "we could estimate the prevalence of delta-sarcoglycan gene mutations to be less than 1% in idiopathic dilated cardiomyopathy"

  The Finnish screen of 52 patients concluded the same (PMID:14564412):
  > "We conclude that the desmin and delta-sarcoglycan genes are not predominant disease-causing genes in patients with DCM in eastern Finland."

  ClinGen's summary reports no enrichment of SGCD rare variants in a large case-control comparison (Mazzarotto et al. 2020, PMID:31983221; per ClinGen, p=0.74). That paper's abstract does not name SGCD, so cite the ClinGen record for this point.
- **Susceptibility haplotype (Chinese cohort):** a promoter 11-bp deletion plus p.Q283R haplotype was associated with DCM (OR 17.27) (PMID:26720722). This is a single association study and should be modeled as `RISK_FACTOR`, not causative.
- **Environmental risk, protective factors, G×E:** none reported specifically for CMD1L. General DCM modifiers (alcohol, cardiotoxic chemotherapy, myocarditis, pregnancy) are plausible but undocumented for SGCD.

## 3. Phenotypes

From the Tsubata families and sporadic cases (PMID:10974018), unless noted otherwise. HPO CURIEs were checked against `cache/hp/terms.csv`.

| Phenotype | HPO | Onset / course | Notes |
|---|---|---|---|
| Dilated cardiomyopathy | HP:0001644 | Childhood to young adult; progressive | Defining feature |
| Left ventricular dilatation | HP:4000141 | — | Mild in R71T carriers (PMID:14564412) |
| Reduced LV ejection fraction / systolic function | HP:0012664 / HP:0006673 | Progressive | — |
| Congestive heart failure | HP:0001635 | Early onset in the S151A family | "early-onset CHF and sudden deaths" |
| Sudden cardiac death | HP:0001645 | Young adults | S151A family; patients were "athletic until their onset of heart failure or sudden death" |
| Need for heart transplantation | (procedure; no HPO) | — | Transplanted at age 21 in the S151A family |
| Arrhythmia | HP:0011675 | — | Not well characterized |

- **Absent feature:** no skeletal muscle disease. This contrasts with LGMD2F.
- **Variable expressivity:** R71T carriers had "a relatively mild phenotype and a late onset of the disease" (PMID:14564412).
- **Frequencies:** cannot be estimated. Fewer than 40 probands are reported worldwide; ClinGen counted about 33 across 11 publications.
- **Quality of life:** there are no disease-specific data. General DCM/heart-failure QoL burden (NYHA class, KCCQ) applies.

## 4. Genetic and molecular information

- **Gene:** SGCD at 5q33. It has 8 exons spanning at least 100 kb. The protein is a 290-aa, 35-kDa sarcolemmal transmembrane glycoprotein (PMID:8842738):
  > "Its mRNA expression is abundant in striated and smooth muscles, with a main 8 kb transcript, encoding a predicted basic transmembrane glycoprotein of 290 amino acids."

**Variants**

| Variant | Type | Evidence | Status |
|---|---|---|---|
| p.S151A (c.451T>G) | Missense | Familial AD DCM (PMID:10974018) | **Contested.** Compound-heterozygous carriers with p.A131P had no cardiomyopathy (PMID:19259135). Knock-in mice showed only a mild, subclinical phenotype (PMID:23695275). ClinGen scored it 0. |
| p.ΔK238 (c.710_712del / 711_713del) | In-frame deletion | Two sporadic cases; absent from 200 controls and from unaffected parents, so presumed de novo; myocardial δ-SG reduced (PMID:10974018) | Scored 0 by ClinGen (population frequency) |
| p.R97Q (c.290G>A) | Missense | One sporadic case (PMID:10974018) | Uncertain |
| p.R71T | Missense; creates an ectopic N-glycosylation site | Finnish family, 2 carriers (PMID:14564412; PMID:26968544) | Uncertain |
| c.4-1G>A | Canonical splice | Minigene-confirmed; reclassified LP (PMID:36270459) | The only proband ClinGen scored (0.25 pts) |

- **Constraint:** gnomAD v4 pLI 0.05, LOEUF 0.88, DECIPHER %HI 4.64 (via ClinGen gene page). The gene is not constrained against loss of function, so haploinsufficiency is unlikely as the mechanism.
- **ClinGen dosage sensitivity:** not curated.
- **Functional class:** a dominant-negative mechanism is proposed (PMID:26968544; PMID:17164264). Germline origin.
- **Modifiers, epigenetics, chromosomal abnormalities:** none reported.

## 5. Environmental information

There are no documented environmental, lifestyle or infectious triggers. Report this as "not available". A `Left deliberately uncited.` waiver is appropriate if an environmental section is added.

## 6. Mechanism and pathophysiology

**Causal chain** (inferred steps are marked)

1. A heterozygous SGCD missense or in-frame variant (germline) **leads to** a structurally abnormal δ-sarcoglycan that is co-expressed with the wild-type protein.
2. The mutant protein **results in** dominant-negative disturbance of the sarcoglycan–sarcospan subcomplex of the DGC. The evidence comes from overexpression systems:
   - **2a.** R97Q/R71T traffic normally to the membrane, and the DGC still assembles, but membrane stability under strain is reduced (PMID:26968544).
   - **2b.** In transgenic mice, S151A is mislocalized to the nucleus, sequesters β/γ-SG, and mislocalizes lamin A/C and emerin (PMID:17164264).
3. This **leads to** loss of sarcolemmal mechanical integrity during contraction (GO:0042383 sarcolemma; GO:0016012 sarcoglycan complex; GO:0016010 dystrophin-associated glycoprotein complex). The evidence:
   > "Upon cyclical cell stretching, cardiac myocytes expressing mutant δ-sarcoglycan R97Q or R71T have increased cell-impermeant dye uptake and undergo contractures at greater frequencies than myocytes expressing normal δ-sarcoglycan." (PMID:26968544)
4. Membrane injury **results in** cardiomyocyte necrosis with replacement fibrosis. This step is extrapolated from null models, where focal necrosis is the histological hallmark (PMID:10481911). An additional branch, also from Sgcd-null mice: loss of the SG–SSPN complex in **vascular smooth muscle** causes coronary vasospasm and ischemic microinfarcts, and a vasodilator prevents the necrosis (PMID:10481911).
5. Progressive myocyte loss **leads to** LV dilatation and reduced systolic function (HP:0001644, HP:0012664). These in turn **result in** heart failure, arrhythmia and sudden death (HP:0001635, HP:0001645).

**Upstream vs downstream.** Steps 1–2 are molecular (the initiating lesion). Step 3 is cellular. Steps 4–5 are at the tissue and organism level.

**Cell types:** cardiac muscle cell (CL:0000746), ventricular cardiac muscle cell (CL:2000046), and vascular smooth muscle (null-model branch only).

**GO process suggestions:** plasma membrane repair (GO:0001778), cardiac muscle contraction (GO:0060048), programmed necrotic cell death (GO:0097300).

**Caveat (`HUMAN_MODEL_MISMATCH`).** Steps 4–5 are demonstrated only for complete δ-SG loss. In humans, heterozygous loss-of-function carriers (LGMD2F parents) are not known to develop DCM, and ΔK238 explant myocardium showed reduced δ-SG with preserved α/β/γ-SG. So a dominant-negative mechanism, not haploinsufficiency, has to carry the human claim, and it rests on overexpression systems.

**Omics, single-cell, CRISPR screens:** none specific to CMD1L.

## 7. Anatomical structures

- **Primary:** heart (UBERON:0000948), myocardium (UBERON:0002349), heart left ventricle (UBERON:0002084). The cardiovascular system is the only system affected.
- **Spared:** skeletal muscle tissue (UBERON:0001134). Sparing is the distinction from LGMD2F.
- **Subcellular:** sarcolemma (GO:0042383), sarcoglycan complex (GO:0016012). In the S151A transgenic mouse, the nucleus/nuclear lamina is also involved (PMID:17164264).
- **Lateralization:** global, bilateral ventricular disease, LV-predominant.

## 8. Temporal development

- **Onset:** pediatric to young adult in the founding report. That screen covered patients aged 3 days to 18 years; deaths occurred at 17–37 years and transplantation at 21 (PMID:10974018; ages as summarized in PMID:19259135). Onset is late and mild in R71T carriers.
- **Onset pattern:** insidious. Patients were asymptomatic and athletic until heart failure or sudden death.
- **Course:** chronic and progressive. There are no remission data. No formal staging exists beyond generic ACC/AHA heart-failure stages A–D.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). Penetrance is incomplete or unproven, and expressivity is variable.
- **De novo cases:** ΔK238 was absent in both unaffected parents (PMID:10974018).
- **Prevalence:** unknown and ultra-rare. Suggested record: `measure_type: CASES_IN_LITERATURE`, about 33 probands per ClinGen. SGCD accounts for less than 1% of idiopathic DCM (PMID:12794684).
- **Populations:** reports come from the USA (Tsubata), Finland (R71T), the Netherlands (c.4-1G>A) and China (risk haplotype). No founder effect is established.
- **Anticipation, mosaicism, consanguinity role, carrier frequency:** not applicable or not reported.

## 10. Diagnostics

- **Clinical tests:**
  - Echocardiography (LVEDD, LVEF)
  - Cardiac MRI with late gadolinium enhancement for fibrosis
  - ECG and Holter for arrhythmia
  - NT-proBNP
  - Creatine kinase, to exclude skeletal myopathy and sarcoglycanopathy
- **Pathology:** myocardial immunofluorescence may show reduced δ-SG with preserved α/β/γ-SG and dystrophin (PMID:10974018). This is a research test.
- **Genetic testing:** multigene DCM panel or exome sequencing. Given its Limited validity, an SGCD variant found in isolation should usually be reported as a VUS. Splice variants can be resolved with RNA or minigene assays (PMID:36270459).
- **Differential diagnosis:**
  - TTN-truncating, LMNA, DSP, RBM20 and MYH7 DCM
  - LGMD2F and other sarcoglycanopathies (elevated CK, proximal weakness)
  - Dystrophinopathy cardiomyopathy
  - Myocarditis
  - Ischemic and toxic causes
- **Screening:** cascade echocardiography and ECG for first-degree relatives, following general familial-DCM guidance. Predictive SGCD genotyping is not appropriate while validity is Limited.

## 11. Outcome and prognosis

- There are no survival statistics. The founding family showed sudden death at a young age and transplantation at 21. The Finnish carriers had a mild course.
- General DCM outcome data with genotype stratification exist (Escobar-Lopez 2021, PMID:34674813), but SGCD-specific outcomes are not reported.
- **Complications:** heart failure, ventricular arrhythmia, sudden death, thromboembolism (generic).

## 12. Treatment

There is no disease-specific therapy. Management follows guideline-directed therapy for heart failure with reduced ejection fraction. NCIT CURIEs were checked against `cache/ncit/terms.csv`.

| Treatment | NCIT action term | Notes |
|---|---|---|
| GDMT: ACEi/ARB/ARNI, β-blocker, MRA, SGLT2i | NCIT:C15986 Pharmacotherapy (+ `therapeutic_agent` CHEBI) | Not studied in CMD1L specifically |
| ICD for sudden-death prevention | — (device; see the CLAUDE.md device pattern) | Relevant given the SCD history |
| Heart transplantation | NCIT:C15289 Organ Transplantation | Performed in the founding family |
| Genetic counseling | NCIT:C15240 Genetic Counseling | Must convey uncertain validity |
| Supportive care | NCIT:C15747 Supportive Care | — |
| Gene therapy (preclinical only) | NCIT:C15238 Gene Therapy | AAV-δ-SG rescues Sgcd-null mice (PMID:19218289) and TO-2 hamsters (Kawada et al., PNAS 2002;99:901–906, doi:10.1073/pnas.022641799; PMID not verified) |

From the mouse rescue study (PMID:19218289): "The aim of our study was to develop an approach for preventing cardiomyopathy in Sgcd-deficient mice by cardiac expression of the intact cDNA upon systemic delivery of adeno-associated viral (AAV) vectors."

In Sgcd-null mice, a vascular smooth-muscle relaxant (verapamil) prevented necrosis (PMID:10481911). This has not been tested in humans.

No clinical trials or pharmacogenomic data specific to CMD1L were identified.

## 13. Prevention

- **Primary prevention:** none.
- **Secondary prevention:** cascade cardiac screening of relatives.
- **Tertiary prevention:** GDMT and ICD to prevent heart-failure progression and sudden death.
- **Counseling:** 50% transmission risk if the variant is truly causal. Counseling must convey the Limited/Disputed validity.
- **Reproductive options:** PGD or prenatal testing is not advisable without a pathogenic-classified variant.
- **Vaccination and public-health measures:** not applicable.

## 14. Other species and natural disease

- **Syrian (cardiomyopathic) hamster**, *Mesocricetus auratus* (NCBITaxon:10036), strains BIO14.6 (HCM-like) and TO-2 (DCM-like). These carry a naturally occurring **homozygous** deletion of Sgcd exon 1 and its promoter (PMID:9391120):
  > "Herein we show that both HCM and DCM hamsters share a common defect in a gene for delta-sarcoglycan (delta-SG)"
- **Inheritance mismatch:** the hamster disease is recessive (null), unlike the proposed human AD disease.
- **Companion animals:** no naturally occurring SGCD-DCM was found in OMIA searches as reported in the literature I reviewed.
- **Zoonotic potential:** none.

## 15. Model organisms

NCBITaxon CURIEs were checked against the cache.

| Model | Taxon | Genotype | Recapitulation | Ref |
|---|---|---|---|---|
| Sgcd-null mouse | NCBITaxon:10090 | Homozygous KO | Cardiomyopathy and muscular dystrophy; focal necrosis; coronary vascular irregularities. Partial match: recessive and with skeletal disease. | PMID:10481911 |
| α-MHC-S151A transgenic mouse | NCBITaxon:10090 | Overexpressed S151A | DCM at a young age, increased lethality, nuclear δ-SG, lamin A/C and emerin mislocalized | PMID:17164264 |
| S151A heterozygous knock-in mouse | NCBITaxon:10090 | Physiological dosage | Only mild cardiac enlargement at 1 year; function preserved; no histopathology. This argues against strong pathogenicity. | PMID:23695275 |
| SGCD-KO pig | NCBITaxon:9823 | Homozygous KO | Systolic dysfunction, myocardial degeneration, sudden death; loss of α/β/γ-SG | PMID:32060408 |
| Hamster BIO14.6 / TO-2 | NCBITaxon:10036 | Natural null | HCM and DCM sublines; rescued by AAV-δ-SG | PMID:9391120 |
| Transgenic fly (human δ-SG S151A) | NCBITaxon:7227 | Inducible overexpression | Enlarged chambers, impaired systolic function (OCT) | PMID:16432241 |
| Adult rat cardiomyocytes (in vitro) | — | Adenoviral R97Q/R71T | Stretch-induced membrane fragility (dominant negative) | PMID:26968544 |

**Suggested `modeled_mechanisms` fidelity.** Null models should be PARTIALLY_RECAPITULATES (LOW–MODERATE fidelity). Record a `POPULATION_MISMATCH` or genotype divergence because the models are recessive null while the human disease is heterozygous dominant. The S151A knock-in arguably FAILS_TO_RECAPITULATE severe DCM.

**Resources:** MGI (Sgcd), IMSR, ZFIN (sgcd).

---

## Notes for the curator

- **References cached.** I fetched 18 references into `references_cache/` with `just fetch-reference`; they are currently untracked:
  - Human genetics: 10974018, 14564412, 12794684, 19259135, 26720722, 36270459, 31983221, 33662488, 27532257
  - Gene identification and models: 8842738, 9391120, 10481911, 16432241, 17164264, 19218289, 23695275, 32060408, 26968544

  Every quote above is copied from those cache files. Commit the ones the entry cites. Escobar-Lopez (PMID:34674813) and the Kawada hamster paper are not cached.
- **Not cached:** the ClinGen CGGV record. Run `just clingen-rebuild --id CGGV:assertion_59326e1b-5cc1-4dfe-8d67-3379aa305c40-2026-03-04T170000.000Z` before citing it in `gene_disease_validity`. The local ClinGen pin may predate the 2026-03-04 assertion; repin if so.
- **No GeneReviews chapter** is specific to CMD1L. The generic "Dilated Cardiomyopathy Overview" (NBK1309) is cached as a URL reference.
- **Lump/split.** The ClinGen and Ambry verdicts bear on whether this should be a standalone DISEASE entry. An alternative is a subtype or `notes` on a familial-DCM entry; the current draft already exists, but surface the choice to the user.

### Sources
- [Tsubata 2000, JCI](https://www.jci.org/articles/view/9224) · [PMC381284](https://pmc.ncbi.nlm.nih.gov/articles/PMC381284)
- [ClinGen SGCD gene page](https://search.clinicalgenome.org/kb/genes/HGNC:10807) · [ClinGen CMD1L assertion](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_59326e1b-5cc1-4dfe-8d67-3379aa305c40-2026-03-04T170000.000Z)
- [GenCC SGCD](https://thegencc.org/genes/HGNC:10807) · [GenCC submission](https://thegencc.org/submissions/SGC-106255.2)
- [PanelApp DCM – SGCD](https://panelapp.genomicsengland.co.uk/panels/652/gene/SGCD/)
- [Bauer 2009 EJHG](https://www.nature.com/articles/ejhg200917)
- [Kawada 2002 PNAS (PMC117403)](https://pmc.ncbi.nlm.nih.gov/articles/PMC117403)
- [OMIM 601411 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/601411)
- [GlyCosmos DOID:0110436](https://alpha.glycosmos.org/diseases/DOID:0110436)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 20 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0110436` (4 mentions) - the report calls it "DOID"; DOID calls it **dilated cardiomyopathy 1L**
- `NCBITaxon:10036` (2 mentions) - the report calls it "Mesocricetus auratus", "Hamster BIO14.6 / TO-2"; NCBITaxon calls it **Mesocricetus auratus**
- `NCBITaxon:10090` (3 mentions) - the report calls it "Sgcd-null mouse", "α-MHC-S151A transgenic mouse", "S151A heterozygous knock-in mouse"; NCBITaxon calls it **Mus musculus**
- `NCBITaxon:9823` (1 mention) - the report calls it "SGCD-KO pig"; NCBITaxon calls it **Sus scrofa**
- `NCBITaxon:7227` (1 mention) - the report calls it "Transgenic fly (human δ-SG S151A)"; NCBITaxon calls it **Drosophila melanogaster**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0042383` (2 mentions) - the report calls it "Subcellular:** sarcolemma"; GO calls it **sarcolemma**
- `UBERON:0000948` (1 mention) - the report calls it "Primary:** heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "Spared:** skeletal muscle tissue"; UBERON calls it **skeletal muscle tissue**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:10036` - called "Mesocricetus auratus", "Hamster BIO14.6 / TO-2"
- `NCBITaxon:10090` - called "Sgcd-null mouse", "α-MHC-S151A transgenic mouse", "S151A heterozygous knock-in mouse"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.