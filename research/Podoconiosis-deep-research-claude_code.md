---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T03:27:17.844501'
end_time: '2026-09-07T03:33:39.186159'
duration_seconds: 381.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Podoconiosis
  mondo_id: MONDO:0005425
  category: Environmental Lymphatic Disease
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 28
  num_turns: 32
  total_cost_usd: 1.7512751999999998
  session_id: 4bf4a114-75db-54c3-885d-72412fe47716
  stop_reason: end_turn
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
citation_count: 43
reference_validation:
  total_references: 41
  verified: 41
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 41
  on_topic: 28
  off_topic: 1
  off_topic_references:
  - PMC:PMC1008352
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 13
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: UBERON:0002387
    reported_labels:
    - dermis
    ontology_label: pes
  - term_id: UBERON:0004357
    reported_labels:
    - dorsum of foot
    ontology_label: paired limb/fin bud
  - term_id: UBERON:0001511
    reported_labels:
    - leg structures
    ontology_label: skin of leg
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Podoconiosis
- **MONDO ID:** MONDO:0005425 (if available)
- **Category:** Environmental Lymphatic Disease

## Research Objectives

Please provide a comprehensive research report on **Podoconiosis** covering all of the
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

I'll research podoconiosis comprehensively, using web search and fetching primary sources to build out this report with proper citations.

I now have comprehensive material across all sections. Compiling the full research report.

# Podoconiosis (Endemic Non-Filarial Elephantiasis / Geochemical Lymphedema): Comprehensive Research Report

## 1. Disease Information

**Overview.** Podoconiosis (also "podoconiosis," from Greek *podos* [foot] + *konia* [dust]) is a non-infectious, geochemical lymphedema of the lower legs caused by long-term contact of bare feet with irritant, mineral-rich red clay soils derived from alkalic volcanic rock, occurring exclusively in genetically susceptible individuals. It is the second most common cause of tropical lymphedema worldwide after lymphatic filariasis and is one of the very few WHO Neglected Tropical Diseases (NTDs) that is **non-infectious** — grouped, unusually, with snakebite envenoming in the "non-infectious NTD" category of the WHO 2021–2030 NTD roadmap. It is also known by the regional lay term "mossy foot" for its hyperkeratotic, moss-like papillomatous skin lesions.

**Key identifiers:**
- **MONDO:** MONDO:0005425
- **OMIM:** 614590 — "PODOCONIOSIS, SUSCEPTIBILITY TO; PDCOS" (susceptibility locus entry, not a classic Mendelian disease entry)
- **Disease Ontology:** DOID:0050138
- **MeSH:** D062846 ("Elephantiasis, Nonfilarial" / historically indexed with "Non-Filarial Lymphedema")
- ICD-10/ICD-11: no dedicated podoconiosis-specific code was identified in this search; it is typically coded under non-filarial lymphedema/elephantiasis categories (curators should verify current ICD-11 foundation entries directly before binding).
- An Orphanet (ORPHA) code was not confirmed via this search and should be checked directly against Orphadata before citing.

**Synonyms:** endemic non-filarial elephantiasis; nonfilarial elephantiasis; tropical non-filarial elephantiasis; geochemical elephantiasis; "mossy foot" disease; podoconiosis lymphoedema.

**Data provenance:** The evidence base is overwhelmingly **aggregated, disease-level** (cross-sectional community surveys, case-control studies, disease registries such as the Ethiopian national podoconiosis mapping, and genetic-epidemiology cohorts from southern Ethiopia), rather than individual EHR-derived data — reflecting its concentration in resource-limited rural settings without electronic health infrastructure. (WHO fact sheet; Deribe et al., *PLoS NTD* "Ten Years of Podoconiosis Research in Ethiopia," 2013.)

---

## 2. Etiology

**Disease causal factors — a gene–environment disease model.** Podoconiosis is the paradigm example of a disease requiring **both** a specific environmental exposure (chronic bare-foot contact with irritant volcanic soil) **and** genetic susceptibility (HLA class II variants); neither alone is sufficient. The WHO states: "evidence suggests that podoconiosis is the result of a genetically determined abnormal inflammatory reaction to mineral particles in irritant red clay soils derived from volcanic deposits." No infectious agent has ever been identified despite extensive investigation.

**Genetic risk factors:**
- **HLA class II locus (chromosome 6p21.3):** The first genome-wide association study (GWAS) of podoconiosis (Tekola Ayele F, et al., *N Engl J Med* 2012;366:1200-8; **PMID:22455414**) genotyped 194 cases and 203 controls from southern Ethiopia and found genome-wide significant association with **rs17612858** (OR 2.19; P=3.44×10⁻⁸), an intergenic SNP between **HLA-DQA1** and **HLA-DQB1**, plus seven other genome-wide-suggestive SNPs in the HLA class II region. Together the HLA SNPs explained ~15.6% of genetic variance and conferred a 2–3-fold increase in risk.
- **Replication:** A follow-up study (*Sci Rep* 2021;11:2941; **PMID:33558538**) replicated HLA class II (DRB1, DQA1, DQB1) association across three Ethiopian ethnic groups (Wolaita, Amhara, Oromo), strengthening the causal case beyond a single population.
- **Heritability/segregation analysis:** Multi-generational family studies in the Wolaita ethnic group (1,400 individuals across 59 families) found a sibling recurrence risk ratio (λs) of **5.07** and heritability of **0.63**, with the best-fitting model being an **autosomal co-dominant major gene**, with age and footwear use as significant environmental covariates (Davey G, et al., genetic epidemiology studies referenced in *Trans R Soc Trop Med Hyg* / *PLoS NTD*, Ethiopia).
- **Mechanistic immunogenetic follow-up:** Because HLA class II presents peptide antigens to CD4+ T cells, the HLA association implicates podoconiosis as a **T-cell-mediated inflammatory disease**. A 2020 multiplexed gene-expression study (PMC7738654) and a 2024 *Nature Communications* paper ("Evidence for immune activation in pathogenesis of the HLA class II associated disease, podoconiosis," PMCID PMC10917762 — PMID not independently confirmed in this search and should be verified before citation) both report signatures of chronic immune activation consistent with an antigen-driven, T-cell-mediated response to mineral particles.

**Environmental/exposure risk factors:**
- **Soil composition:** Weathering of basaltic and alkaline volcanic rock produces red clay soils rich in **smectite and kaolinite clays**, mica-group minerals, **crystalline silica (quartz)**, iron oxide, and **zirconium**; WHO also implicates **aluminium and beryllium**. A 2023 geochemical/mineralogical characterization study (PMC10611848) and a 2017 study on the **haemolytic activity of soils from areas of varying podoconiosis endemicity** (*PLoS ONE* 2017; PMC5426718) both link specific mineral/geochemical profiles to endemicity gradients.
- **Barefoot exposure duration:** Duration and age of onset of barefoot exposure are the dominant environmental determinants; **age of first shoe-wearing correlates positively with age of podoconiosis onset**.
- **Occupation:** subsistence farming with prolonged barefoot contact with cultivated volcanic soils is the classic occupational exposure.
- **Altitude:** endemic zones are characteristically **high-altitude** areas with volcanic soils (contrasting with lymphatic filariasis, which is a low-lying, mosquito-borne disease).
- **Socioeconomic status:** extreme rural poverty precluding shoe ownership is a structural risk factor.

**Protective factors:**
- **Consistent footwear use** is the principal, well-established environmental protective factor across multiple case-control studies (e.g., Rwanda: "none of the controls went barefoot… in contrast to 11.6% of controls, none of the patients wore closed shoes," Musanze District case-control study, PMC13497288). Floor covering in homes (reducing indoor soil contact) is also protective.
- **Foot hygiene** (regular washing) reduces cumulative mineral-particle penetration.
- No specific protective genetic variant/allele has yet been robustly identified (absence of the risk HLA haplotypes is implicitly protective, but no independent protective locus has been reported in the searched literature).

**Gene–environment interaction.** Podoconiosis is repeatedly cited in the literature as a "tropical model for gene–environment interactions" (Davey G, *Trans R Soc Trop Med Hyg*, 2006) — disease develops only in the intersection of (a) sustained soil exposure and (b) HLA class II susceptibility genotype; neither factor alone produces disease, and community understanding studies show that ~59% of Ethiopian youth in endemic areas already correctly conceptualize this joint causation (PMC6155534).

---

## 3. Phenotypes

Podoconiosis exhibits a well-characterized clinical progression from early reversible inflammatory changes to fixed fibrotic elephantiasis. A **de novo five-stage clinical staging system** (Tekola F, et al.) is the field standard:

| Stage | Features |
|---|---|
| 1 (early) | Itching, tingling/burning sensation on the dorsum of the foot, mild forefoot widening, intermittent swelling |
| 2 | "Water-bag" pitting, soft edema; flask-shaped leg (narrow at knee, wide at ankle); smooth, dumpy foot surface |
| 3 | Fibrotic, non-pitting edema below the knee; sclerotic hyper-/hypopigmentation on the shin; fibrotic ridge at the flexural ankle; early nodules, plantar involvement |
| 4 (advanced) | Non-pitting edema extending above the knee; skin depigmentation around the ankle |
| 5 (advanced) | Fibrotic, globular, "woody"/rubbery tumor-like swelling; ankle ankylosis; multiple nodules and scarring; band-like redundant "pillowy" skin folds |

**Symptoms/signs by category:**
- **Cutaneous:** hyperkeratotic, "mossy," papillomatous nodules (moss-like lesions present in ~77.5% of patients, often bilateral); dry, thickened, fissured skin; toe maceration; plantar/dorsal nodules; hyper- and hypopigmentation.
- **Lymphedema:** chronic, **bilateral but asymmetric**, ascending (rather than descending) leg swelling that typically **spares the groin** — a key distinguishing feature from filarial lymphedema.
- **Musculoskeletal:** ankle ankylosis and joint fixation in advanced (stage 4–5) disease, causing significant mobility impairment.
- **Systemic/complication phenotype — Acute dermatolymphangioadenitis (ADLA):** recurrent acute attacks of fever, pain, erythema, and worsening swelling, triggered by bacterial entry through fissured/cracked skin. Patients experience on average ≥5 episodes/year (up to 23.3/year reported in one Ethiopian district), totaling ~90 incapacitated days/year (PMC6638979; medRxiv 2025.05.12.25327479). Each ADLA episode drives further lymphatic damage and disease progression.
- **Laboratory/hematological:** studies from West Gojjam, Ethiopia (PMC11687886) and Musanze, Rwanda (PMC13497288) report altered hematological and immunological profiles (e.g., elevated inflammatory markers) versus controls, though these are not yet incorporated into diagnostic criteria.
- **Behavioral/psychological:** severe depression (OR ~19.8), anxiety (OR ~10.7), and stress symptoms (OR ~13.5) are markedly elevated versus unaffected neighbors (Rwanda comparative study, *PLoS NTD* 2024, PMC11309478/PMID 39116063); depressive-symptom prevalence reported at 12.6% (Ethiopia), 38.5% (Cameroon), and 68.5% (Rwanda) among patients.

**Phenotype characteristics:**
- **Onset:** insidious, typically in young adulthood — mean age at first noticing leg swelling ≈ 25 years; onset is rare before age 5–6, rises through adolescence, and can present up to the sixth decade or later.
- **Progression:** chronic, slowly progressive over years to decades if unmanaged; **early stages (1–2) are reversible** with footwear and hygiene, but stages 3–5 involve fixed fibrosis.
- **Severity/frequency:** variable; frequency of nodular/hyperkeratotic ("mossy") lesions ~77.5%; in Ethiopian endemic districts prevalence of any stage disease reaches 5–10%.
- **Quality of life impact:** significantly reduced across all four WHOQOL subdomains (physical, psychological, social, environmental) versus healthy controls (Northern Ethiopia QOL study, PMC3726315); stigma, illiteracy, comorbidity, and being unmarried are independent correlates of poor QOL.

**Suggested HPO terms** (leads only — must be verified against the current HPO release before curation, per dismech's anti-hallucination policy):
- Lower-limb lymphedema / lymphedema (general lymphedema term)
- Hyperkeratosis (HP:0000962 general hyperkeratosis concept)
- Skin ulcer / skin fissuring
- Ankle contracture / joint ankylosis
- Depression, Anxiety (as secondary/behavioral phenotypes)
- Recurrent skin infections (as the substrate of ADLA)

---

## 4. Genetic/Molecular Information

**Causal/susceptibility genes:** Podoconiosis is **not** a single-gene Mendelian disorder; it is modeled as a **complex, HLA class II-associated susceptibility trait** (OMIM 614590, "PODOCONIOSIS, SUSCEPTIBILITY TO"). No monogenic causal mutation has been described.

**Implicated loci/genes (HGNC where applicable):**
- **HLA-DQA1** / **HLA-DQB1** (intergenic SNP rs17612858 between them) — Tekola Ayele et al., PMID:22455414.
- **HLA-DRB1** — implicated in replication study (PMID:33558538) alongside DQA1/DQB1.

**Variant classification:** These are common-variant (population-frequency) susceptibility alleles identified by GWAS, not rare pathogenic Mendelian variants — so ACMG/AMP pathogenicity tiers do not directly apply. Effect sizes are modest (OR ~2.19 for the lead SNP), consistent with a polygenic/complex-trait architecture layered on an obligate environmental exposure.

**Allele frequency:** Population-level allele frequencies for the implicated HLA class II haplotypes in Ethiopian populations were reported in the original GWAS and replication studies but specific frequency values were not retrieved in this search; gnomAD/1000 Genomes do not have curated podoconiosis-specific frequency annotations (this is an HLA-region association, so standard biallelic-variant frequency databases are of limited direct use — HLA imputation/typing panels are more appropriate).

**Somatic vs. germline:** Exclusively germline susceptibility (host genetic background), acting in combination with an acquired environmental exposure — not a somatic disease.

**Functional consequences:** The HLA class II susceptibility association is interpreted as conferring an altered antigen-presentation profile that predisposes CD4+ T cells to mount a chronic, maladaptive inflammatory response to mineral particles absorbed through the skin — i.e., **gain-of-function of a pathological adaptive immune response**, not a loss-of-function protein defect.

**Modifier genes:** None specifically named beyond the co-dominant "major gene" inferred by segregation analysis; the field considers additional minor loci and environmental covariates (age, footwear) likely but not yet mapped.

**Epigenetic information / chromosomal abnormalities:** No epigenetic (DNA methylation, histone modification) studies or chromosomal-abnormality data specific to podoconiosis were identified in this search — this appears to be an open research gap.

**Molecular/immunological profiling:**
- A 2020 multiplexed gene-expression (NanoString-type) study of PBMCs from HLA class II-genotyped cases/controls (PMC7738654) found evidence of **chronic immune activation** transcriptional signatures.
- A 2024 *Nature Communications* study (PMC10917762) extended this, reporting immune-activation evidence directly tied to the HLA-associated disease mechanism.
- A cytokine-stimulation study (PMC11598685) measured **TNF-α, IL-1β, and IFN-γ** by ELISA in PBMCs from cases vs. endemic healthy controls, at baseline and after in vitro stimulation with **kaolinite, chlorite, and beryllium sulfate**. Key finding: baseline (unstimulated) TNF-α and IL-1β were **significantly higher in patients** than controls, but after mineral stimulation, healthy controls showed a **paradoxically greater increase** in IL-1β (2–3-fold higher with kaolinite/chlorite) than patients — suggesting patients' cells may already be in a chronically activated/exhausted state at baseline. No significant difference in cytokine gene mRNA expression was found, though slight increases in IL-1β and TGF-β were noted.

---

## 5. Environmental Information

**Environmental factors:** The central environmental agent is chronic transdermal (plantar) exposure to **irritant, alkalic-volcanic-derived red clay soil**. Implicated mineral/chemical constituents (from soil geochemistry studies, PMC10611848 and PMC5426718):
- Smectite and kaolinite clays (phyllosilicates)
- Mica-group minerals
- Crystalline silica/quartz (colloid-sized alumino-silicate particles)
- Iron oxide
- Zirconium
- Aluminium and beryllium (per WHO)

Soils from higher-endemicity areas show measurably different mineralogical/geochemical and hemolytic-activity profiles compared to soils from lower-endemicity areas of the same region, supporting a soil-composition dose-response relationship.

**Lifestyle factors:** Habitual bare-footedness (occupational and cultural norm in affected rural communities); lack of floor coverings in homes; poverty precluding shoe purchase/replacement.

**Infectious agents:** None causally implicated in the primary disease process (podoconiosis is explicitly non-infectious). However, **secondary bacterial infection** through fissured, hyperkeratotic skin is the proximate trigger for **ADLA** attacks, which drive disease exacerbation; a 2023 study (*Sci Rep* 2023, "Tropical leg lymphedema caused by podoconiosis is associated with increased colonisation by anaerobic bacteria") found increased anaerobic bacterial colonization of affected limbs, implicating a polymicrobial (largely anaerobic) skin/soft-tissue flora in the acute-attack pathophysiology.

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, with inference status noted)

1. **Chronic barefoot contact** with alkalic-volcanic-derived red clay soil exposes plantar/dorsal foot skin to colloid-sized alumino-silicate mineral particles (kaolinite, smectite, quartz/silica, zirconium, aluminium, beryllium) over years. *(Demonstrated — epidemiological and geochemical studies.)*
2. This exposure **leads to** transdermal/transcutaneous penetration of ultrafine mineral particles into the dermis and subcutaneous lymphatics — inferred from post-mortem/biopsy microanalysis showing intralysosomal silicon and aluminium in macrophages of affected lymphatics and lymph nodes (Price-era histochemical studies; *Trans R Soc Trop Med Hyg* 1985 lymph node/vessel silica study). *(Demonstrated in human tissue and supported by animal intralymphatic-silica injection experiments — see below.)*
3. In **HLA class II-susceptible individuals** (particularly those carrying risk alleles/haplotypes at HLA-DQA1/DQB1/DRB1), this **leads to** an aberrant, sustained CD4+ T-cell-mediated adaptive immune response against the mineral particles/particle-associated antigens, rather than normal clearance. *(Inferred from GWAS + immune-activation transcriptomic studies; the precise antigenic mechanism by which minerals engage HLA class II presentation is not directly demonstrated and remains a key open question.)*
4. Mineral particles are phagocytosed by **macrophages** in the dermal lymphatics and regional lymph nodes; intralysosomal accumulation **results in** lysosomal membrane rupture, macrophage destruction/activation, and release of pro-fibrotic and pro-inflammatory mediators. *(Demonstrated — histopathology and the classic silica-macrophage cytotoxicity model, analogous to silicosis pathogenesis.)*
5. Chronic macrophage activation and cytokine release (elevated baseline TNF-α, IL-1β; likely TGF-β involvement) **drive** endolymphangitis — inflammation of the lymphatic vessel wall — with recruitment of mast cells, lymphocytes, and plasma cells (biopsy series: 94% mast-cell infiltration, 71% plasma-cell infiltration, plus papillary/reticular dermal lymphocytic infiltrate). *(Demonstrated by histopathology, PMID:35604949.)*
6. Persistent endolymphangitis **causes** progressive collagen deposition and fibrosis within lymphatic vessel walls and surrounding dermis (thickened, vertically arranged papillary-dermal collagen bundles; horizontally arranged reticular-dermal bundles; media-sclerosis of blood vessels in later stages). *(Demonstrated.)*
7. Fibrotic thickening and scarring of the lymphatic wall **result in** obliteration of the lymphatic lumen and mechanical obstruction to lymph flow — the direct structural lesion producing lymphedema. *(Demonstrated — lymphographic and histologic evidence; note early Price-era experiments found silica's obstructive effect on lymph vessels themselves exceeded its effect via lymph nodes.)*
8. Lymphatic obstruction **leads to** chronic interstitial fluid accumulation in the foot/lower leg (clinical edema, initially reversible/pitting — clinical stages 1–2). *(Demonstrated.)*
9. Ongoing lymph stasis and tissue hypoxia **drive** progressive dermal/subcutaneous fibrosis, hyperkeratosis, and papillomatosis, producing the fixed, non-pitting, "mossy," nodular elephantiasis of advanced stages 3–5, including ankle ankylosis from peri-articular fibrosis. *(Demonstrated clinically/histologically; the precise molecular fibrogenic pathway — e.g., specific TGF-β/fibroblast activation signaling — is inferred by analogy to other fibrotic lymphedemas rather than directly dissected in podoconiosis-specific mechanistic studies.)*
10. **Branch — acute exacerbation loop:** Chronic skin fissuring/hyperkeratosis (from step 9) creates portals of entry for skin flora (including anaerobic bacteria); bacterial invasion **triggers** recurrent ADLA attacks (fever, erythema, acute swelling), each of which **further damages** lymphatic architecture and **accelerates** progression back into step 6–9, creating a self-reinforcing cycle of episodic acute inflammation superimposed on chronic fibrosis. *(Demonstrated epidemiologically and microbiologically; the precise host-microbe interaction is inferred.)*

### Detail by mechanism category

- **Molecular pathways:** No podoconiosis-specific signaling pathway (e.g., a defined Wnt/MAPK/PI3K-AKT cascade) has been directly dissected; the field relies on general models of particulate-induced macrophage activation (analogous to silicosis) and T-cell/HLA antigen-presentation biology. Candidate GO terms: **positive regulation of NF-kappaB transcription factor activity**, **T cell receptor signaling pathway**, **inflammatory response**.
- **Cellular processes:** macrophage phagocytosis and lysosomal rupture; T-cell activation; mast-cell and plasma-cell infiltration; fibroblast activation/collagen synthesis; endothelial injury to lymphatic vessel walls.
- **Protein dysfunction:** No specific misfolded/aggregating protein is implicated; the "dysfunction" is at the level of an aberrant HLA class II-restricted immune recognition event rather than an intrinsic protein structural defect.
- **Metabolic changes:** Not specifically characterized in the literature reviewed.
- **Immune system involvement:** Central — chronic, HLA class II-restricted, T-cell-mediated inflammatory/autoinflammatory-like response; elevated baseline pro-inflammatory cytokines (TNF-α, IL-1β); mast cell and plasma cell tissue infiltration; blunted mineral-specific cytokine response in patients relative to healthy exposed controls, suggesting immune exhaustion/dysregulation rather than simple hyperreactivity.
- **Tissue damage mechanisms:** silica/mineral-induced macrophage cytotoxicity, chronic lymphangitis, fibrosis, and secondary infection-driven acute tissue injury (ADLA).
- **Biochemical abnormalities:** No specific enzyme deficiency or ion-channel defect; the defect is immunogenetic (HLA-restricted antigen presentation) rather than a classical inborn-error biochemical lesion.
- **Epigenetic changes:** Not characterized in the literature surveyed — an open research gap.
- **Molecular profiling:** Transcriptomic (gene-expression) data exist (PMC7738654, PMC10917762) showing immune-activation signatures; no proteomics, metabolomics, or lipidomics datasets specific to podoconiosis were identified.
- **Advanced technologies:** No single-cell, spatial transcriptomic, multi-omics, or CRISPR/RNAi functional-genomics studies of podoconiosis were found in this search — likely reflecting the disease's neglected status and resource-limited research settings.

**Suggested GO terms (leads, to be verified):** GO:0006955 (immune response), GO:0002250 (adaptive immune response), GO:0030198 (extracellular matrix organization), GO:0042060 (wound healing), GO:0002437 (inflammatory response to antigenic stimulus).
**Suggested CL terms (leads):** CL:0000235 (macrophage), CL:0000097 (mast cell), CL:0000542 (lymphocyte), CL:0000084 (T cell), CL:0000786 (plasma cell), CL:0000057 (fibroblast), CL:0002138 (endothelial cell of lymphatic vessel).

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary target is the **lymphatic vasculature of the lower limb** (dermal and subcutaneous lymphatics of the foot and leg below the knee, extending above the knee in advanced disease). Regional lymph nodes (inguinal typically spared/less involved than in filariasis) may show reactive/fibrotic change. Skin and subcutaneous tissue of the foot/leg are secondarily and prominently affected (integumentary system). No visceral organ involvement is described — this contrasts with filarial disease, which can involve genital/scrotal lymphatics.
- **Body systems involved:** lymphatic system (primary); integumentary system (skin — hyperkeratosis, fibrosis, nodules); musculoskeletal system (secondary — ankle joint ankylosis in advanced stages); immune system (T-cell/HLA-mediated pathogenesis).
- **Tissue/cell level:** dermal papillary and reticular connective tissue (fibrosis); lymphatic endothelium; macrophages, mast cells, lymphocytes, and plasma cells within the dermis and perilymphatic tissue; eccrine sweat gland hyperplasia has also been described in advanced-stage biopsies.
- **Subcellular level:** macrophage **lysosomes/phagolysosomes** are the key subcellular compartment — intralysosomal accumulation of silicon/aluminium mineral particles, lysosomal membrane rupture, and consequent release of pro-fibrotic mediators (candidate GO Cellular Component term: GO:0005764 lysosome).
- **Localization:** bilateral but **asymmetric**, **ascending** distribution beginning at the foot/ankle and progressing proximally; characteristically **spares the groin/genitalia** (unlike filarial lymphedema). Suggested UBERON terms: UBERON:0002387 (dermis), UBERON:0004357 (dorsum of foot) or UBERON:0002387/UBERON:0001511 (leg structures), UBERON:0001473 (lymphatic vessel), UBERON:0002391 (lymph node).

---

## 8. Temporal Development

- **Onset:** insidious/chronic onset (not acute), typically in adolescence to young adulthood; mean age at first noticing swelling ≈25 years; can present from childhood through the sixth decade of life depending on exposure duration.
- **Progression:** Five clinical stages (see Section 3) representing a continuum from early reversible pitting edema (stages 1–2) to fixed fibrotic elephantiasis with joint ankylosis (stages 4–5). Progression rate is variable and strongly modifiable by intervention — footwear/hygiene adoption can halt or reverse early-stage disease, while established fibrosis (stage 3+) is largely irreversible.
- **Disease course pattern:** chronic and progressive at baseline, but punctuated by **recurrent acute exacerbations (ADLA)** that produce an episodic/relapsing component superimposed on the underlying progressive fibrotic course; disease is **lifelong** without effective self-care.
- **Remission:** partial "remission" (reduction in edema/symptom burden) is achievable with sustained conservative management (foot hygiene, compression, elevation, footwear) especially in early stages; spontaneous remission does not occur.
- **Critical periods:** early childhood is a critical window for **prevention** (early and consistent shoe adoption is strongly associated with delayed or prevented onset); once fibrosis is established, the window for reversal closes, making early intervention the key modifiable period.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Global burden:** ~4 million people affected worldwide, with disease potential in 32 countries (18 in Africa, 3 in Asia, 11 in Latin America); the WHO fact sheet cites ~17 countries with confirmed cases (12 African, 3 Latin American, 2 Asian) — reflecting the gap between "potentially endemic" and "confirmed endemic" counts. Podoconiosis is **not yet incorporated into the Global Burden of Disease (GBD) study**, a recognized evidence gap, and most quantitative prevalence data originate from Ethiopia specifically.
- **Ethiopia:** bears an estimated ~25% of the global burden; >35 million people at risk across 345 endemic districts; >1.5 million people (some sources: 1.6 million) living with the disease. Ethiopia-specific pooled prevalence (meta-analysis) = **4.52%** (95% CI 3.92–5.16%); in specific endemic districts, prevalence reaches **5–10%**.
- **Burden metrics:** 172,073 DALYs annually in Ethiopia (182 per 100,000 population, 2017 estimate); total annual economic burden in Ethiopia estimated at **US$213.2 million**, of which 91.1% is productivity loss; an older (2004) estimate cited ~US$200 million annual productivity loss.
- **Mortality:** a standardized mortality ratio of ~6 has been reported among affected populations (WHO), though podoconiosis itself is not directly fatal — excess mortality likely reflects ADLA sepsis risk, disability-associated comorbidity, and reduced healthcare access.

**Inheritance pattern:** best-fit segregation model is **autosomal co-dominant major-gene inheritance** with significant environmental covariates (age, footwear) — i.e., a complex trait with a strong single-locus (HLA class II region) contribution layered on an obligate environmental exposure, rather than classic simple Mendelian inheritance.

**Penetrance:** incomplete and **exposure-dependent** — genetic susceptibility (HLA risk genotype) is necessary but not sufficient; penetrance requires the environmental exposure (chronic barefoot soil contact), making this a gene-by-environment-dependent penetrance model.

**Heritability:** h² = 0.63 (Wolaita family study); sibling recurrence risk ratio λs = 5.07.

**Genetic anticipation, germline mosaicism, founder effects:** not described/applicable — this is a common-variant, complex-trait susceptibility disease, not a repeat-expansion or classic single-gene disorder.

**Consanguinity role:** not specifically implicated as a risk modifier in the literature surveyed (contrasts with classic autosomal recessive disorders).

**Carrier frequency:** not meaningfully defined for a complex-trait/HLA-association disease in the way it is for a recessive Mendelian disorder.

**Population demographics:**
- **Affected populations:** predominantly rural, subsistence-farming communities in East African highlands (Ethiopia, Uganda, Tanzania, Kenya, Rwanda, Burundi, Sudan/South Sudan, Cameroon) plus described foci in Central America and northern India.
- **Geographic distribution:** endemic to **high-altitude volcanic soil regions** — a striking contrast to the low-lying, mosquito-vector-dependent distribution of lymphatic filariasis.
- **Sex ratio:** conflicting across studies — a meta-analysis found women ~1.15× more likely affected than men; some single-site studies report much stronger female predominance (up to 3.2:1 in some regions), while a Wolaita, Ethiopia survey found near-parity (M:F ≈ 1:0.98), likely reflecting differing occupational/exposure patterns by locality.
- **Age distribution:** most cases (~64%) occur in the economically productive 16–45-year age range; rare before age 5–6; some studies report highest prevalence after age 45–55, consistent with cumulative lifetime soil exposure.

---

## 10. Diagnostics

**Diagnostic approach:** Podoconiosis is fundamentally a **diagnosis of clinical exclusion**, based on history (barefoot residence in an endemic volcanic-soil area), physical examination (bilateral, asymmetric, ascending, groin-sparing lymphedema with characteristic mossy/nodular skin changes), and targeted tests to exclude the principal differential diagnoses.

**Key differentiation from lymphatic filariasis** (the most important differential):

| Feature | Podoconiosis | Lymphatic filariasis |
|---|---|---|
| Laterality | Bilateral, asymmetric | Typically unilateral |
| Progression direction | Ascending | Descending |
| Groin/genital involvement | Very rare | Frequent (hydrocele common) |
| Geography | High-altitude volcanic soil | Low-lying, mosquito-endemic |
| Systemic febrile inflammatory episodes | ADLA (secondary bacterial) | Filarial adenolymphangitis |
| Filarial antigen test (ICT card) | **Negative** | **Positive** |
| Night blood smear microfilariae | Absent | Present (nocturnal periodicity in most regions) |

**Clinical/laboratory tests:**
- **Filarial antigen rapid tests** (e.g., ICT card test for circulating filarial antigen) and **night blood smears** for microfilariae are the standard exclusionary tests — negative in podoconiosis.
- **Ultrasound** can detect the pathognomonic "filarial dance sign" of live adult worms in lymphatics in filariasis; its absence supports podoconiosis, though ultrasound is not itself diagnostic of podoconiosis.
- **Skin biopsy/histopathology** (as in the PMC9166354/PMID:35604949 study) can support diagnosis by showing the characteristic papillary dermal lymphocytic infiltrate, mast-cell/plasma-cell infiltration, and collagen bundle changes, though this is a research rather than routine clinical tool.
- No podoconiosis-specific serum biomarker or genetic test is in clinical use; the HLA class II association is a research finding, not (yet) a diagnostic test.

**Differential diagnosis (beyond filariasis):** lepromatous leprosy (distinguished by sensory loss, thickened peripheral nerves, trophic ulcers — absent in podoconiosis), Kaposi sarcoma, mycetoma pedis, elephantiasis nostras verrucosa (chronic venous/lymphatic disease from other causes), and systemic causes of lower-limb edema (e.g., cardiac, renal, hepatic).

**Genetic testing:** No clinical genetic test panel exists for podoconiosis; genetic/HLA typing remains a research tool (e.g., ClinicalTrials.gov NCT01939431, "Genetic and Other Aspects of Podoconiosis").

**Screening:** No formal population screening program beyond community-based case-finding/mapping surveys (e.g., Ethiopia's national integrated LF/podoconiosis morbidity mapping, PMC6044548) used to define endemic districts for targeted intervention.

---

## 11. Outcome/Prognosis

- **Mortality:** Podoconiosis is not itself directly lethal, but a standardized mortality ratio of ~6 has been reported in affected populations (WHO), likely reflecting ADLA-related sepsis, disability-associated vulnerability, and healthcare-access disparities; formal disease-specific mortality/survival statistics (5-/10-year survival) are not established the way they are for cancers.
- **Morbidity/disability:** Substantial — advanced-stage disease causes major functional impairment (mobility limitation from ankle ankylosis and massive limb swelling), lost productivity (91% of Ethiopia's US$213.2M annual economic burden is productivity loss), and profound social/psychological morbidity (severe depression OR ~19.8, anxiety OR ~10.7 versus unaffected neighbors).
- **Quality of life:** significantly reduced across physical, psychological, social, and environmental WHOQOL domains; stigma (social exclusion from schools, churches, mosques, and marriage prospects) is a major independent driver of poor QOL, distinct from the physical disease burden itself.
- **Complications:** recurrent ADLA (the dominant complication, causing ~90 incapacitated days/year in affected individuals in some cohorts); secondary bacterial/anaerobic infection; chronic wounds; joint ankylosis; disfiguring nodules.
- **Recovery potential:** early-stage (1–2) disease is substantially reversible with consistent conservative management (footwear, hygiene, compression, elevation); stages 3–5 fibrotic/ankylotic changes are largely irreversible, though ADLA frequency and QOL can still be improved by treatment (nodulectomy, compression, hygiene) even in advanced disease.
- **Prognostic factors:** stage at initiation of treatment, consistency of self-care/footwear adherence, frequency of ADLA episodes, and presence of stigma/psychosocial comorbidity all predict functional and QOL outcomes. No molecular/biomarker-based prognostic tool has been validated.

---

## 12. Treatment

There is **no curative pharmacotherapy or disease-modifying drug** for podoconiosis; management is centered on **lymphedema self-care and, where needed, surgery** — analogous to management of other chronic lymphedemas.

**Supportive/conservative care (mainstay, evidence-based via RCT):**
- **Foot hygiene:** daily washing with soap, water, and antiseptic.
- **Emollients:** regular application to reduce skin fissuring (a key ADLA-prevention measure).
- **Compression bandaging/garments** and **limb elevation** at night.
- **Exercise** and **consistent use of socks and shoes.**
- This bundled regimen was tested in the **GoLBeT trial** ("Gojjam Lymphoedema Best Practice Trial," a pragmatic RCT in northern Ethiopia; protocol PMC4504163, results PMC6562300) — a community-based package delivered via lay "Community Podoconiosis Agents," designed specifically to **reduce the frequency of ADLA episodes**. An earlier one-year follow-up study of a simplified lymphedema treatment regimen in southern Ethiopia (*PLoS NTD* 2010, PMC2994920) demonstrated effectiveness of this basic self-care package.
- Cost-effectiveness/social-outcome analysis of community-based treatment in East Gojjam (PMC6808421) supports scaling this model.

**Surgical/interventional:**
- **Nodulectomy (surgical debulking of fibrotic nodules):** performed under local anesthesia, wounds left to heal by secondary intention with compression bandaging. A study of surgical debulking in Ethiopia (*PLoS NTD* 2021; **PMID:33481805**) found nodulectomy produced significant DLQI (Dermatology Life Quality Index) improvement with no serious complications, supporting its use as a standard resource-appropriate procedure. Suggested NCIT term: **NCIT:C15329** (Surgical Procedure); the treatment could also carry `therapeutic_modality: SURGERY`.

**Pharmacotherapy:** No specific disease-modifying drugs exist; **antibiotic therapy** is used for acute ADLA episodes (targeting the secondary bacterial/anaerobic skin infection) — suggested NCIT term **NCIT:C258** (Antibiotic) or a specific agent-level CHEBI/NCIT binding once a specific regimen is identified from local guidelines.

**Rehabilitation/psychosocial:** psychosocial support and community reintegration efforts (addressing stigma) are increasingly recognized as necessary treatment-adjacent components given the disproportionate mental-health burden; NCIT candidate: **NCIT:C15747** (Supportive Care).

**Advanced therapeutics (gene therapy, cell therapy, RNA-based, immunotherapy):** none reported or applicable — podoconiosis management remains entirely in the domain of lymphedema self-care and surgery; there is no oncologic/immunotherapeutic analog in the literature reviewed.

**Experimental treatments:** GoLBeT (RCT, completed, community lymphedema-management package) is the key trial identified; ClinicalTrials.gov NCT01939431 ("Genetic and Other Aspects of Podoconiosis") is a genetic/observational study rather than an interventional trial. No NCT-registered pharmacologic trials were identified in this search.

**Treatment algorithms:** Stage-based — early (1–2) disease emphasizes prevention/reversal via footwear+hygiene; established fibrotic disease (3–5) combines ongoing lymphedema self-care with nodulectomy for symptomatic nodules and ADLA-prevention bundles to arrest further deterioration.

---

## 13. Prevention

Prevention is the single most impactful intervention category for podoconiosis, given the absence of curative treatment.

- **Primary prevention:** the cornerstone — **consistent footwear use from early childhood**, **daily foot hygiene** (washing), and **floor covering** in homes to reduce indoor soil contact. Multiple case-control studies (Rwanda, Ethiopia) confirm shoe-wearing as the dominant modifiable protective factor. Rwanda has implemented a national public **barefoot-walking ban** as an explicit public-health prevention policy (also targeting other soil-borne diseases).
- **Secondary prevention:** early case detection (community mapping surveys) and early initiation of self-care before fibrotic (stage 3+) changes become established.
- **Tertiary prevention:** ADLA-prevention bundles (hygiene, emollients, compression) to prevent complications/further disease progression in those already affected — this is the GoLBeT trial's explicit target outcome.
- **Immunization:** not applicable — no infectious/vaccine-preventable component.
- **Screening programs:** population-based community mapping (integrated with lymphatic filariasis morbidity mapping in Ethiopia, PMC6044548) is used to define endemic districts for targeted resource allocation, rather than individual diagnostic screening.
- **Genetic screening/counseling:** not currently part of clinical practice; research studies (e.g., NCT01939431) note that **genetic research itself faces stigma-related informed-consent challenges** in affected communities (BMC Medical Ethics qualitative study, cited in search results), a notable ethical/implementation consideration for any future genetic counseling program.
- **Behavioral interventions:** community health education (e.g., the Mossy Foot Treatment and Prevention Association's model of training patients as community health agents) to promote footwear adoption and hygiene, and to reduce stigma.
- **Public health interventions:** the WHO 2021–2030 NTD roadmap includes podoconiosis as a non-infectious NTD target for national program integration; Ethiopia's Federal Ministry of Health has prioritized podoconiosis elimination given the country's disproportionate global burden. No specific WHO 2030 numeric elimination target for podoconiosis alone was identified in this search (the overarching NTD roadmap targets — 90% reduction in people requiring NTD treatment, 75% reduction in NTD-related DALYs, ≥100 countries eliminating ≥1 NTD — apply at the aggregate NTD-portfolio level).
- **Environmental interventions:** community-level floor covering/soil-contact reduction programs in schools and homes in endemic districts.

---

## 14. Other Species / Natural Disease

Podoconiosis, as an environmentally-and-genetically determined human disease dependent on a specific human HLA class II susceptibility architecture and human bipedal barefoot behavior, has **no described naturally occurring veterinary or wildlife counterpart** in the literature surveyed. No OMIA (Online Mendelian Inheritance in Animals) entry, comparative veterinary case series, or cross-species susceptibility data were identified — this is expected, since livestock/companion animals do not share the same plantar skin exposure pattern, gait, or HLA architecture, and no zoonotic or cross-species transmission mechanism exists (the disease is non-infectious). This is a notable gap relative to many other NTDs but is mechanistically expected given the disease's human-specific gene-environment etiology.

---

## 15. Model Organisms

There is **no validated whole-animal model that specifically recapitulates podoconiosis** as a disease entity (unlike, e.g., filarial lymphedema, which has established animal infection models). However, related experimental and model-organism work is directly relevant to its mechanistic underpinnings:

- **Historical intralymphatic silica-injection experiments** (foundational to the Price-era pathogenesis model; described in the *Trans R Soc Trop Med Hyg* 1985 silica/lymph-node/vessel study): direct **intralymphatic injection of fine silica particles** in experimental animals produced an "immediate and intense macrophage reaction with later fibrosis both within lymph vessels and to a lesser extent within lymph nodes," with lymphography showing that the resulting obstruction was driven more by vessel-wall than lymph-node effects — this is the closest thing to a mechanistic animal model of podoconiosis pathogenesis and directly supports the silica/mineral-macrophage-fibrosis causal chain (step 2–7 above). Species and exact citation detail were not fully resolved in this search and should be confirmed against the primary Trans R Soc Trop Med Hyg article before citation as a formal "animal model" record.
- **General lymphedema models** (not podoconiosis-specific, but mechanistically analogous for the downstream lymphatic-obstruction/fibrosis phenotype): the **murine tail lymphedema model** (surgical ablation of tail lymphatics) and the **murine hindlimb secondary lymphedema model** (surgical/radiation-based) reproduce the distal-limb swelling and fibrosis phenotype seen in podoconiosis, though they model post-surgical/radiation lymphedema rather than particulate-mineral-induced disease.
- **Genetic lymphatic-dysfunction model:** the **Chy mouse** (missense VEGFR3/*Flt4* mutation) develops congenital chylous ascites and progressive peripheral lymphedema — useful for studying lymphatic vessel biology generally but not etiologically related to podoconiosis's acquired, particulate/immune-mediated mechanism.
- **Silicosis models** (rat intratracheal silica instillation, PMC1008352) are the closest analogous **organ-system** model for silica-macrophage-fibrosis biology, informing (by analogy to the lung) how crystalline silica engages macrophage phagolysosomal rupture and downstream fibrogenesis in the lymphatic/dermal context of podoconiosis.

**Overall assessment:** podoconiosis-specific model-organism research is minimal-to-absent in the modern literature; the mechanistic evidence base rests primarily on **human tissue/biopsy studies**, **human genetic-epidemiology (GWAS/family) studies**, and **historical animal silica-injection experiments** from the 1970s–80s, representing a significant translational research gap (no modern in vivo model exists to test candidate interventions before human trials).

---

## Summary of Key Evidence Gaps (for curation awareness)

1. No modern podoconiosis-specific animal model exists to mechanistically validate the HLA–mineral–macrophage–fibrosis causal chain in vivo.
2. Epigenetic, proteomic, metabolomic, single-cell, and spatial transcriptomic data are entirely absent from the literature surveyed.
3. Global burden data outside Ethiopia are sparse; podoconiosis is not yet included in the GBD framework.
4. The precise antigen/mechanism by which mineral particles engage HLA class II-restricted T-cell activation remains undefined (cytokine-stimulation data are inconsistent/paradoxical, PMC11598685).
5. No podoconiosis-specific ICD-11/Orphanet code was confirmed in this search and should be verified directly before ontology binding.

---

## Sources

- [Podoconiosis, Susceptibility to (PDCOS) - OMIM 614590](https://www.omim.org/entry/614590)
- [Podoconiosis - non-filarial geochemical elephantiasis - PubMed](https://pubmed.ncbi.nlm.nih.gov/20096054/)
- [Podoconiosis: endemic nonfilarial elephantiasis - PubMed](https://pubmed.ncbi.nlm.nih.gov/15735414/)
- [HLA Class II Locus and Susceptibility to Podoconiosis - NEJM (PMID:22455414)](https://www.nejm.org/doi/full/10.1056/NEJMoa1108448)
- [Replication of HLA class II locus association with susceptibility to podoconiosis in three Ethiopian ethnic groups - PMC (PMID:33558538)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7870958/)
- [Evidence for immune activation in pathogenesis of the HLA class II associated disease, podoconiosis - Nature Communications](https://www.nature.com/articles/s41467-024-46347-z)
- [Multiplexed gene expression analysis of HLA class II-associated podoconiosis implicates chronic immune activation in its pathogenesis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7738654/)
- [Differences in Cytokine Expression at Baseline and in Response to Mineral Stimulation by PBMCs from Podoconiosis Cases and Healthy Controls - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11598685/)
- [The effects of silica on lymph nodes and vessels—a possible mechanism in the pathogenesis of non-filarial endemic elephantiasis - Trans R Soc Trop Med Hyg](https://academic.oup.com/trstmh/article/79/5/645/1944163)
- [Podoconiosis pathogenesis: renewed use of an historical archive - PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC7034335)
- [Podoconiosis – From known to unknown: Obstacles to tackle - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0001706X21000978)
- [A geochemical and mineralogical characterization of soils associated with podoconiosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10611848/)
- [Haemolytic activity of soil from areas of varying podoconiosis endemicity in Ethiopia - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0177219)
- [The health and economic burden of podoconiosis in East Africa: systematic review and meta-analysis - PMC (PMID:42308246)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13340807/)
- [The health and economic burden of podoconiosis in Ethiopia - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7139123/)
- [Prevalence of podoconiosis and its associated factors in Gamo zone, Southern Ethiopia, 2021 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8830091/)
- [Podoconiosis (non-filarial lymphoedema) - WHO Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/podoconiosis-(non-filarial-lymphoedema))
- [Podoconiosis: a comprehensive clinical review and strategies for control and elimination - PubMed (PMID:40898820)](https://pubmed.ncbi.nlm.nih.gov/40898820/)
- [Genetic, Immunological, and Public Health Perspectives on Podoconiosis - Journal of Tropical Medicine (PMID:41341693)](https://onlinelibrary.wiley.com/doi/10.1155/jotm/9961827)
- [Podoconiosis: Clinical spectrum and microscopic presentations - PLOS NTD (PMID:35604949)](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0010057)
- [Tropical leg lymphedema caused by podoconiosis is associated with increased colonisation by anaerobic bacteria - Scientific Reports](https://www.nature.com/articles/s41598-023-40765-7)
- [The impact of acute adenolymphangitis in podoconiosis on caregivers - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6638979/)
- [Surgical debulking of podoconiosis nodules and its impact on quality of life in Ethiopia - PubMed (PMID:33481805)](https://pubmed.ncbi.nlm.nih.gov/33481805/)
- [Lymphoedema management to prevent acute dermatolymphangioadenitis in podoconiosis in northern Ethiopia (GoLBeT): a pragmatic RCT - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6562300/)
- [Podoconiosis treatment in northern Ethiopia (GoLBet): study protocol - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4504163/)
- [Effectiveness of a Simple Lymphoedema Treatment Regimen in Podoconiosis Management in Southern Ethiopia: One Year Follow-Up - PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0000902)
- [Cost-effectiveness and social outcomes of a community-based treatment for podoconiosis lymphoedema, East Gojjam, Ethiopia - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6808421/)
- [The impact of podoconiosis on quality of life in Northern Ethiopia - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3726315/)
- [Bearing the burden: Podoconiosis and mental health—Rwanda comparative study - PLOS NTD (PMID:39116063)](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0012346)
- [The impact of podoconiosis, lymphatic filariasis, and leprosy on disability and mental well-being: systematic review - PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0009492)
- [Frontiers: Stigma related to podoconiosis in Ethiopia: a systematic review](https://www.frontiersin.org/journals/tropical-diseases/articles/10.3389/fitd.2024.1483407/full)
- [Integrated morbidity mapping of lymphatic filariasis and podoconiosis cases in 20 co-endemic districts of Ethiopia - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6044548/)
- [Podoconiosis in Uganda: prevalence, geographical distribution and risk factors - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11637681/)
- [Podoconiosis - Wikipedia](https://en.wikipedia.org/wiki/Podoconiosis)
- [Epidemiology and sex differences of podoconiosis in Ethiopia: A systemic review and meta-analysis - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405844020322891)
- [Rural youths' understanding of gene x environmental contributors to heritable health conditions: podoconiosis in Ethiopia - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6155534/)
- [Hematological profiles and preventive-practice characteristics among patients with podoconiosis: a case-control study in Musanze District, Rwanda - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13497288/)
- [Individual Correlates of Podoconiosis in Areas of Varying Endemicity: A Case-Control Study - PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0002554)
- [Determinants of Podoconiosis in Bensa District, Sidama Region, Ethiopia: A case control study - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10464951/)
- [Genetic and Other Aspects of Podoconiosis - ClinicalTrials.gov NCT01939431](https://clinicaltrials.gov/study/NCT01939431)
- [Podoconiosis: key priorities for research and implementation - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7738650/)
- [The feasibility of eliminating podoconiosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4645432/)
- [Ten Years of Podoconiosis Research in Ethiopia - PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0002301)

**Note on downstream use:** All ontology-term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT) in this report are research leads only, per dismech's anti-hallucination curation policy — each must be independently verified (label match, dynamic-enum reachability) via OAK/`just validate-terms` before being bound in a KB entry. Several PMIDs above were extracted from search-engine snippets rather than direct PubMed fetches (which were blocked by cookie/CAPTCHA walls during this session); curators should re-verify each PMID against PubMed directly, and re-derive exact-quote snippets from the primary source before use as `evidence:` blocks, per the `dismech-references` skill.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 41 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 41 |
| On topic | 28 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC1008352` (1 mention) - Intratracheal injection into rats of size-graded silica particles.
  - shared terms: none

Weighed against this report's own most characteristic terms: `podoconiosis`, `disease`, `chronic`, `lymphatic`, `ethiopia`, `lymphedema`, `hla`, `class`, `skin`, `endemic`, `adla`, `model`, `directly`, `genetic`, `soil`, `environmental`, `secondary`, `foot`, `footwear`, `mechanism`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002387` (2 mentions) - the report calls it "dermis"; UBERON calls it **pes**
- `UBERON:0004357` (1 mention) - the report calls it "dorsum of foot"; UBERON calls it **paired limb/fin bud**
- `UBERON:0001511` (1 mention) - the report calls it "leg structures"; UBERON calls it **skin of leg**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002391` (1 mention) - the report calls it "lymph node"; UBERON calls it **lymph**