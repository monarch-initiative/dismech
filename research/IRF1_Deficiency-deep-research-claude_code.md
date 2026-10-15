---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T01:31:52.972934'
end_time: '2026-09-04T01:36:25.046286'
duration_seconds: 272.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IRF1 Deficiency
  mondo_id: ''
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 27
  total_cost_usd: 1.3120430000000003
  session_id: 1d4c83ee-98b8-54c2-892b-3815ba752722
  stop_reason: end_turn
  assistant_text_blocks: 4
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC9907019
  relevance_assessed: 8
  on_topic: 4
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 15
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0100646
    reported_labels:
    - Abnormal lymph node morphology / lymphadenopathy
    ontology_label: Thyroiditis
  - term_id: HP:0410030
    reported_labels:
    - Impaired lymphocyte transformation / abnormal T-cell physiology
    ontology_label: Cleft lip
  - term_id: HP:0002960
    reported_labels:
    - "Autoimmunity / immune dysregulation \u2014 not reported in IRF1 deficiency\
      \ to date"
    ontology_label: Autoimmunity
  - term_id: GO:0000785
    reported_labels:
    - chromatin, where IRF1 binds ISRE elements
    ontology_label: chromatin
  - term_id: UBERON:0002370
    reported_labels:
    - thymus, relevant to T-cell development
    ontology_label: thymus
  - term_id: NCIT:C1666
    reported_labels:
    - Interferon Gamma
    ontology_label: Tyrphostin A30
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IRF1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IRF1 Deficiency** covering all of the
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

I'll research IRF1 Deficiency now, using web search and fetch tools to gather current, citable information.

I now have sufficient depth to write the comprehensive report. Let me do a couple more targeted searches to round out phenotype/HPO, mouse models, and gnomAD frequency data before compiling.

I have enough material now to compile a comprehensive, well-cited report.

I now have comprehensive, well-sourced material. Compiling the full research report.

# IRF1 Deficiency: Comprehensive Research Report

## 1. Disease Information

**Overview.** IRF1 deficiency is a recently characterized (2023) autosomal recessive inborn error of immunity caused by biallelic loss-of-function variants in *IRF1* (Interferon Regulatory Factor 1). It presents as a novel genetic etiology of **Mendelian Susceptibility to Mycobacterial Disease (MSMD)**, a heterogeneous group of inborn errors of immunity in which otherwise healthy children develop severe, disseminated disease caused by weakly virulent mycobacteria — the BCG vaccine strain (*Mycobacterium bovis* BCG) and environmental (nontuberculous) mycobacteria (EM) — and related "intramacrophagic" pathogens, in the absence of notable susceptibility to other classes of pathogens (PMC9907019, Rosain et al., *Cell*, 2023; PMID: 36736301). The defect is selective: IRF1-deficient patients show no history of severe viral disease despite documented exposure to multiple viruses, including SARS-CoV-2, distinguishing this condition mechanistically from broader antiviral interferon disorders (PMC9907019).

**Key identifiers:**
- **Gene:** *IRF1* (HGNC:6116), chromosome 5q31.1
- **OMIM gene entry:** *147575 — Interferon Regulatory Factor 1; IRF1
- **OMIM phenotype:** #620668 — Immunodeficiency 117 (IMD117)
- **Orphanet:** ORPHA:699615 — "Complete IRF1 deficiency," listed under the MSMD gene/disease group (orpha.net/en/disease/gene/IRF1)
- **Disease category:** Mendelian, primary/inborn immunodeficiency; a subtype within the MSMD spectrum (~21 known genetic etiologies)
- **Common synonyms/alternative names:** Immunodeficiency-117 (IMD117); Complete IRF1 deficiency; MSMD due to IRF1 deficiency; IRF1-related mycobacterial susceptibility

**Evidence basis.** As a disease first described in a single primary-literature report, essentially all current knowledge derives from **aggregated case-series/mechanistic study data** (two unrelated index patients studied in depth with genomics, immunophenotyping, transcriptomics, and cellular functional assays), rather than large-scale EHR/registry data. OMIM's clinical synopsis for IMD117 (#620668) is itself abstracted directly from this same primary report.

---

## 2. Etiology

**Primary cause.** IMD117 is caused by **homozygous (biallelic) loss-of-function nonsense mutations in *IRF1***, identified in two unrelated children, each born to **consanguineous parents** (PMC9907019; OMIM #620668):
- Patient 1: homozygous c.385C>T, p.Arg129Ter (**R129X**)
- Patient 2 (girl): homozygous c.103C>T, p.Gln35Ter (**Q35X**)

Both variants were identified by whole-exome sequencing and segregated with disease in each family, consistent with **autosomal recessive** inheritance. Functional testing showed the R129X truncated protein still localizes to the nucleus and retains DNA-binding capacity but has **no transcriptional activity**; patient cells showed markedly reduced *IRF1* mRNA (consistent with nonsense-mediated decay) and **absent IRF1 protein**, confirming a complete loss-of-function/null mechanism rather than a dominant-negative one.

**Risk factors:**
- *Genetic:* Biallelic (homozygous) null variants in *IRF1* are causal and fully penetrant for the mycobacterial phenotype reported to date. **Consanguinity** was present in both reported families, consistent with the ultra-rare autosomal recessive inheritance model and elevated homozygosity risk in consanguineous unions.
- *Environmental/exposure:* **BCG vaccination** is the dominant precipitating exposure worldwide (given routinely in many countries with high TB burden), producing disseminated "BCGitis/BCGosis." Environmental (nontuberculous) mycobacteria exposure (e.g., *Mycobacterium avium* complex) is the other principal trigger.
- No modifier genes or protective variants have yet been reported for IRF1 deficiency specifically, reflecting its very recent discovery and the extremely small number of known patients (n=2 in the founding report).

**Gene-environment interaction.** The disease is a classic "genotype reveals susceptibility to an otherwise low-virulence environmental/vaccine exposure" model typical of MSMD: the germline defect is silent until the child is exposed to BCG (via routine immunization) or to ubiquitous environmental mycobacteria, at which point unchecked intramacrophagic replication produces disseminated disease.

---

## 3. Phenotypes

**Core clinical phenotype:** early-onset, recurrent, multifocal/disseminated disease due to weakly virulent mycobacteria — both **BCG** (post-vaccination) and **environmental mycobacteria** — in patients who otherwise lack a striking susceptibility to viral, fungal, or ordinary bacterial pathogens (PMC9907019; OMIM #620668).

**Phenotype characteristics:**
- **Onset:** Early childhood (infancy/early childhood), typically following BCG vaccination
- **Course:** Recurrent, life-threatening, multifocal mycobacterial disease episodes; disease persisted/recurred **despite treatment with multiple antimycobacterial drugs**, indicating a severe underlying immunologic defect rather than antimicrobial resistance
- **Severity:** Severe/life-threatening in both reported patients
- **Frequency:** Based on n=2 patients (extremely rare); disseminated mycobacterial disease is essentially fully penetrant in the biallelic null genotype reported

**Laboratory/immunologic phenotype (a distinct "laboratory abnormality" phenotype class):**
- Mildly impaired IFN-γ secretion by leukocytes
- Impaired cellular response to IFN-γ in fibroblasts and myeloid cells, with **impaired signaling downstream of STAT1**
- Deficient expression of IFN-γ-inducible genes involved in immune activation and antimicrobial effector function
- **Impaired development of T and NK cell subsets** on transcriptome analysis, with abnormal expression of NK/T developmental target genes
- **Normal responses to type I interferon (IFN-α/β)** and normal in vitro antiviral activity against several pathogens, including SARS-CoV-2 — the key finding establishing IRF1's redundancy for antiviral immunity in humans despite being essential for antimycobacterial immunity

**Quality of life impact:** Not formally studied (no EQ-5D/SF-36 data available for this ultra-rare, recently described condition); qualitatively, disease burden is high given recurrent life-threatening infection episodes in early childhood requiring prolonged multidrug antimycobacterial therapy.

**Suggested HPO terms:**
- HP:0002718 — Recurrent infections
- HP:0002090 — Pneumonia (if pulmonary involvement)
- HP:0100646 — Abnormal lymph node morphology / lymphadenopathy (BCGitis-associated)
- HP:0410030 — Impaired lymphocyte transformation / abnormal T-cell physiology (developmental impairment of T/NK cells)
- HP:0040312 — (or nearest available) susceptibility to mycobacterial infection — note: dismech curators should check for the most specific MSMD-family HPO term, as HPO's coverage of "mycobacterial disease susceptibility" is coded at varying granularity across MSMD gene entries
- HP:0002960 — Autoimmunity / immune dysregulation — not reported in IRF1 deficiency to date; include only if literature review of later case reports confirms

*(GeneCards reports IRF1 as linked to 38 HPO terms across multiple organ systems in aggregate gene-disease association databases, but the two published human IRF1-deficiency cases are specifically and narrowly characterized by mycobacterial/immune phenotypes; broader multi-system associations in aggregator databases likely reflect somatic/oncologic IRF1 biology rather than the germline immunodeficiency phenotype and should be curated cautiously.)*

---

## 4. Genetic/Molecular Information

**Causal gene:** *IRF1*, HGNC:6116, OMIM *147575, chromosome 5q31.1.

**Pathogenic variants identified to date (both from the founding report, PMC9907019 / OMIM #620668):**

| Variant (cDNA) | Protein change | Zygosity | Type | Consequence |
|---|---|---|---|---|
| c.103C>T | p.Gln35Ter (Q35X) | Homozygous | Nonsense | Loss of function, likely NMD, absent protein |
| c.385C>T | p.Arg129Ter (R129X) | Homozygous | Nonsense | Truncated protein; nuclear-localized, DNA-binding-competent but transcriptionally inactive; low mRNA (NMD) and absent protein in patient cells |

- **Variant classification:** Both variants function as **complete loss-of-function (null)** alleles based on segregation with a fully recessive Mendelian phenotype plus direct functional/biochemical confirmation (loss of transcriptional activity in reconstitution assays; absent protein in patient cells) — consistent with ACMG/AMP "pathogenic" classification, though formal ClinVar submission status was not independently confirmed in this research pass.
- **Origin:** Both are **germline** variants (not somatic); both patients born of **consanguineous** parents, consistent with homozygosity by descent.
- **Functional consequence:** Complete **loss of function** — no dominant-negative or gain-of-function mechanism identified. IRF1's role as a transcriptional activator downstream of IFN-γ/STAT1/GAF signaling is abolished.
- **Population allele frequency:** Formal gnomAD constraint statistics (pLI/LOEUF/o-e ratio) for *IRF1* were not retrievable in this pass and should be queried directly at gnomad.broadinstitute.org before curation; given IRF1's dual roles as an immune transcription factor and tumor suppressor (see below), even heterozygous LoF carriers are of interest for constraint modeling, but no disease association has been reported for heterozygous carriers of these specific null alleles.

**Modifier genes:** None reported specifically for IRF1 deficiency; not enough patients have been described to assess phenotypic variability or modifiers.

**Somatic/oncologic genetics (distinct from the germline immunodeficiency, but relevant gene biology):** *IRF1* was originally identified as a **candidate myeloid tumor-suppressor gene** at 5q31.1, one of the most frequently deleted regions in **acute myeloid leukemia (AML)** and **myelodysplastic syndrome (MDS)**, particularly del(5q)/5q− syndrome (Willman et al., *Science*, 1993; PMID: 8438156). IRF-1 was the only gene in the smallest commonly deleted region consistently lost (mono- or bi-allelically) across 13 leukemia/MDS cases with 5q31 aberrations. IRF-1 expression is lost in acute promyelocytic leukemia and a subset of AML with del(5)(q31) (Nature *Leukemia*, PMID search results). In mouse models, *Irf1* loss dramatically exacerbates tumor development in HRAS-transgenic and *p53*-null backgrounds, establishing a functional interaction between IRF1 loss and p53-pathway tumor suppression (Genes Dev., PMID search results). This tumor-suppressor biology is mechanistically separate from — but molecularly continuous with — the germline immunodeficiency phenotype, since both derive from loss of IRF1's transcriptional activator function (in one case over growth/apoptosis genes, in the other over IFN-γ-response genes).

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone modification) data for germline IRF1 deficiency were identified in this pass; IRF1 promoter hypermethylation/silencing has been studied in cancer contexts but is outside the scope of the germline immunodeficiency entry.

**Chromosomal abnormalities:** Not applicable to the germline immunodeficiency (point/nonsense variants only); large-scale 5q31 deletions encompassing *IRF1* are a somatic/oncologic finding (see above), not a germline immunodeficiency mechanism.

---

## 5. Environmental Information

- **Environmental factors:** Exposure to **environmental (nontuberculous) mycobacteria** (e.g., *Mycobacterium avium* complex, and related species such as *M. fortuitum*) is a primary environmental trigger of clinical disease in genetically susceptible individuals.
- **Iatrogenic/programmatic exposure:** **BCG vaccination**, administered routinely in many countries as part of childhood immunization against tuberculosis, is the principal identified precipitant of disease onset in both reported IRF1-deficient patients, producing disseminated "BCGitis" (localized-to-disseminated *M. bovis* BCG disease).
- **Infectious agents implicated:**
  - *Mycobacterium bovis* BCG vaccine strain (NCBI Taxonomy: relevant to *M. bovis* subsp. BCG)
  - Environmental/nontuberculous mycobacteria broadly, with *M. avium* complex specifically implicated in mechanistic literature on IRF1's role in macrophage control of mycobacteria (e.g., mBio 2021 study on TNF-α/IL-6 autocrine signaling inducing IRF1/IRG1 in *M. avium*-infected human macrophages)
- **Lifestyle factors:** Not applicable/not reported — this is a pediatric, genetically determined susceptibility rather than a lifestyle-modulated condition.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Biallelic nonsense variants in *IRF1* (e.g., Q35X, R129X) **lead to** loss of full-length IRF1 protein — via nonsense-mediated mRNA decay and/or production of a transcriptionally inert truncated protein.
2. Following exposure to BCG or environmental mycobacteria, innate immune cells (monocytes/macrophages, NK cells) and T cells mount an IL-12/IL-23-driven **IFN-γ response**, which normally engages IFNGR1/IFNGR2 → JAK1/JAK2 → STAT1 (GAF complex) signaling. This upstream IFN-γ/STAT1 axis **remains largely intact** in IRF1 deficiency (patients show only mild impairment of IFN-γ secretion).
3. Physiologically, GAF-activated STAT1 **induces IRF1 transcription and nuclear translocation**, where IRF1 binds ISRE-like motifs in target-gene promoters as the "second wave" effector of the IFN-γ response, downstream of and largely dependent on STAT1.
4. In IRF1 deficiency, this second wave **fails to occur**: IRF1 loss **abolishes transcriptional induction of roughly one-third of all IFN-γ-inducible mRNAs**, including a large fraction of genes previously shown to be essential for cell-intrinsic immunity to intracellular pathogens (PMC9907019 — "IRF1 controlled the expression of one-third of IFN-γ-inducible mRNAs, including numerous targets previously described as essential for cell-intrinsic immunity to intracellular pathogens").
5. Among the genes that **fail to be upregulated** are classical IRF1 targets encoding **antimicrobial effectors and antigen-presentation machinery**: inducible nitric oxide synthase (**NOS2/iNOS**), guanylate-binding proteins (**GBP2, GBP5**), the immunoproteasome subunits (**PSMB9/LMP2**), and the peptide transporter (**TAP1**), together with **CIITA** (the MHC class II transactivator) and components of MHC class I antigen-processing/presentation (PMC4398980; Genes & Immunity/Regulation of Tap1/Lmp2; ScienceDirect CIITA induction data).
6. Loss of these antimicrobial effectors **directly impairs the intrinsic mycobactericidal/mycobacteriostatic capacity of macrophages** — this is the proximate lesion: "**IRF1-deficient mononuclear macrophages do not control mycobacteria or related intramacrophagic pathogens normally in response to IFN-γ**" (PMC9907019).
7. In parallel, transcriptomic analysis of patient cells shows **impaired development of T and NK cell subsets** that normally secrete and respond to IFN-γ, with abnormal expression of NK/T lineage developmental target genes — recapitulating findings from *Irf1*-knockout mice (see Model Organisms, below), where IRF1 acts non-cell-autonomously via the bone-marrow stromal microenvironment (through **IL-15** induction) to support NK-cell development, and cell-autonomously to support Th1/CD8+ T-cell differentiation and IL-12-driven maturation.
8. The **net result** is a **selective collapse of the "IFN-γ circuit"** required to arm macrophages against intracellular mycobacteria, **without** compromising the largely IRF1-independent **type I interferon (IFN-α/β) antiviral circuit** — explaining the clinical pattern of severe, recurrent mycobacterial disease with preserved antiviral competence, including normal in vitro control of SARS-CoV-2.

### Molecular pathways
IFN-γ → IFNGR1/IFNGR2 → JAK1/JAK2 → STAT1 (GAF) → *IRF1* induction → IRF1 binding to ISRE/IRF-E motifs → transcription of antimicrobial and antigen-presentation genes. This sits within the broader **IL-12/IL-23–IFN-γ axis** that defines MSMD pathobiology generally (Frontiers Immunol. 2026 review, "IFN-γ-driven immunity collapse underlies heterogeneous infections"; PMC12255513 MSMD overview).
Suggested GO terms: GO:0060333 (interferon-gamma-mediated signaling pathway), GO:0071346 (cellular response to interferon-gamma), GO:0002218 (activation of innate immune response), GO:0140374 (antiviral innate immune response — for the preserved arm).

### Cellular processes
- Failure of macrophage-intrinsic antimycobacterial killing programs (nitric oxide production, GBP-mediated vacuolar disruption of intracellular pathogens)
- Impaired NK-cell and T-cell developmental programming
- Preserved apoptosis/cell-death and type I IFN antiviral programs

### Protein dysfunction
Complete **loss of function** of the IRF1 transcription factor. IRF1 possesses an N-terminal winged helix-turn-helix DNA-binding domain built from five tryptophan-rich repeats, which recognizes tandem GAAA ISRE half-site motifs (structurally defined via the 1998 IRF1-DBD/DNA crystal structure, PDB 1IF1; PMID: 9422515), and a C-terminal IRF-association domain (IAD) mediating cofactor interactions. The R129X truncation retains DNA binding but loses transactivation capacity entirely (no downstream transcription), while Q35X essentially eliminates the protein via nonsense-mediated decay — both converging on a null functional outcome.

### Immune system involvement
This is fundamentally an **immunodeficiency mechanism** (not autoimmunity): a **selective, IFN-γ-restricted intrinsic immunodeficiency** of macrophages, compounded by an NK/T-cell developmental defect, producing susceptibility specifically to intramacrophagic pathogens (mycobacteria) while leaving humoral immunity, IFN-α/β antiviral immunity, and general bacterial defenses comparatively intact.

### Tissue damage mechanisms
Disease manifests as granulomatous/suppurative disseminated mycobacterial lesions (lymphadenitis, osteomyelitis, and other classic BCGitis/disseminated-EM patterns typical of MSMD), reflecting failure to contain — rather than actively destructive autoinflammatory — pathology.

### Molecular profiling
Transcriptome (RNA-seq) analysis of patient leukocytes/fibroblasts was central to establishing the ~1/3 reduction in IFN-γ-inducible gene induction and to demonstrating the T/NK developmental gene-expression signature (PMC9907019). No single-cell, spatial, proteomic, metabolomic, or CRISPR-screen data specific to IRF1-deficient patients were identified in this research pass; the founding paper's genome-wide IRF1 chromatin-binding data in normal cells (ChIP-seq, PMC4398980, "Genome-wide Identification of IRF1 Binding Sites Reveals Extensive Occupancy at Cell Death Associated Genes") is a relevant reference dataset for target-gene identification but was performed in reference (non-patient) cells.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Reticuloendothelial/lymphoid system (lymph nodes — BCGitis lymphadenitis), and any site of disseminated mycobacterial seeding (skin/soft tissue, bone, lung, liver, spleen), consistent with typical MSMD disease distribution.
- **Secondary organ involvement:** Determined by the pattern of disseminated infection in each patient (site-specific granulomatous disease); not exhaustively itemized in available secondary sources for this research pass — primary literature (PMC9907019) should be consulted directly for patient-level organ involvement detail during curation.
- **Body systems involved:** Immune system (primary); secondarily, whichever organ systems harbor disseminated mycobacterial foci.
- **Tissue/cell level:** **Macrophages/monocytes** (the principal cell-intrinsic site of the antimycobacterial defect) and **NK cells / T lymphocytes** (developmental defect). Suggested Cell Ontology terms: CL:0000235 (macrophage), CL:0000576 (monocyte), CL:0000623 (natural killer cell), CL:0000084 (T cell).
- **Subcellular level:** Nucleus (site of IRF1 transactivation of target genes; also site of the transcriptionally-inert truncated R129X protein); GO Cellular Component: GO:0005634 (nucleus), GO:0000785 (chromatin, where IRF1 binds ISRE elements).
- **Localization/laterality:** Not applicable — systemic/disseminated pattern rather than lateralized.

Suggested UBERON terms: UBERON:0000178 (blood), UBERON:0002370 (thymus, relevant to T-cell development), UBERON:0002370/0001744 (lymph node), UBERON:0002107 (liver), UBERON:0002106 (spleen) as applicable per patient-level detail.

---

## 8. Temporal Development

- **Onset:** Early childhood; disease manifested following BCG vaccination (typically administered in infancy in BCG-endemic countries), consistent with the general MSMD onset pattern of early-childhood presentation.
- **Onset pattern:** Insidious-to-acute presentation of disseminated mycobacterial disease following exposure/vaccination.
- **Progression:** **Recurrent** — both reported patients experienced **recurrent, life-threatening episodes caused by multiple mycobacteria** (both BCG and environmental mycobacteria), **despite treatment with multiple antimycobacterial drugs**, indicating a chronic, relapsing disease course rather than a single self-limited event.
- **Disease course pattern:** Chronic/relapsing, driven by an underlying immunologic defect rather than antimicrobial resistance; unlike the classical progressive neurodegenerative or metabolic Mendelian disease pattern, MSMD/IRF1 deficiency is punctuated by **infection episodes** whose severity/frequency is a function of ongoing pathogen exposure.
- **Duration:** Chronic, lifelong immunologic susceptibility (the genetic lesion is permanent); clinical episodes may remit with antimycobacterial treatment but recur on re-exposure or reactivation given the failure of intrinsic macrophage control.
- **Critical periods:** Early childhood BCG vaccination represents a clear "critical exposure window" — in countries that do not administer BCG, or where BCG is delayed/omitted in known carriers, initial presentation may instead follow environmental mycobacterial exposure at a variable age.

No formal staging system, remission-pattern data, or natural-history/longitudinal cohort data exist yet for this ultra-rare, recently described condition (n=2 patients in the literature to date).

---

## 9. Inheritance and Population

- **Epidemiology:** IRF1 deficiency is an **ultra-rare** condition; only **two patients from two unrelated families** have been reported in the literature to date (as of the founding 2023 report), and no population-level prevalence or incidence estimates exist. MSMD broadly is itself a rare disease group (~21 known genetic causes) with substantial but incompletely quantified global prevalence, concentrated in populations with high consanguinity rates and routine BCG vaccination programs.
- **Inheritance pattern:** **Autosomal recessive** — both index cases were **homozygous** for their respective nonsense variants, each inherited from **consanguineous parents**, consistent with recessive segregation.
- **Penetrance:** Appears **complete** for the mycobacterial-susceptibility phenotype in both reported homozygous patients (both alleles are functionally null), though the extremely small sample size precludes firm penetrance/expressivity estimates.
- **Expressivity:** Not yet characterized due to small patient number; both patients shared the core disseminated-BCG/environmental-mycobacteria phenotype.
- **Genetic anticipation:** Not applicable — nonsense variants, not a repeat-expansion mechanism.
- **Germline mosaicism:** Not reported.
- **Founder effects:** Not established; the two reported variants (Q35X, R129X) arose independently in unrelated consanguineous families, with no shared haplotype reported in available sources.
- **Carrier frequency:** Not established in population databases for these specific null alleles at the time of this research pass; should be checked directly in gnomAD during curation.
- **Consanguinity role:** **Central** — both reported families were consanguineous, the expected pattern for an ultra-rare autosomal recessive null-allele disease.
- **Population demographics:** Insufficient data (n=2) to characterize ethnic/geographic distribution, sex ratio, or age distribution beyond noting both cases presented in early childhood consistent with the general MSMD pattern; one reported patient was female (Q35X carrier).

---

## 10. Diagnostics

- **Clinical suspicion:** A child presenting with disseminated or unusually severe disease due to BCG vaccine strain or environmental/nontuberculous mycobacteria, particularly with consanguineous parentage or recurrent/refractory disease despite standard antimycobacterial therapy, should prompt evaluation for an MSMD-spectrum genetic defect.
- **Genetic testing (primary diagnostic modality):**
  - **Whole-exome sequencing (WES)** was the method used to identify both reported causal *IRF1* variants and is the appropriate first-line broad genetic test given the ~21 known and expanding list of MSMD genes.
  - **Targeted MSMD/primary-immunodeficiency gene panels** including *IRF1*, alongside the more common MSMD genes (*IL12RB1*, *IFNGR1*, *IFNGR2*, *STAT1*, *IL12B*, *ISG15*, *IRF8*, *NEMO/IKBKG*, *RORC*, *JAK1*, *TYK2*, *SPPL2A*, *TBX21*, etc.), are a practical clinical option.
  - **Single-gene *IRF1* Sanger confirmation** following identification of a candidate variant, plus segregation analysis in the family.
- **Functional/immunologic testing:**
  - IFN-γ secretion assays (whole-blood or PBMC stimulation) — expect mild impairment
  - Cellular response to exogenous IFN-γ (STAT1 phosphorylation and downstream target-gene induction, e.g., in fibroblasts) — expect impaired downstream (post-STAT1) signaling with intact proximal STAT1 phosphorylation, localizing the defect to the IRF1 "second wave"
  - Immunophenotyping of NK and T-cell subsets — expect reduced/abnormal NK and T-cell development on flow cytometry, correlating with the transcriptomic findings
  - IRF1 protein expression by Western blot/immunoblot in patient-derived cells — expect **absent protein**
- **Histopathology:** Granulomatous inflammation typical of mycobacterial disease at biopsied sites (e.g., lymph node), non-specific to IRF1 deficiency per se but supportive of the overall clinical picture.
- **Differential diagnosis:** Other MSMD gene defects (*IL12RB1* — most common cause of AR MSMD; *IFNGR1*/*IFNGR2* deficiency; *STAT1* deficiency; *IRF8* deficiency; *RORC* deficiency; *JAK1* deficiency; complete or partial forms across this gene list) must be excluded/distinguished by genetic testing, as clinical presentations overlap substantially. IFNγR1/R2 deficiency in particular can mimic the phenotype but differs in whether IFN-γ therapy is beneficial.
- **Screening:** No population-based newborn screening exists for this ultra-rare condition; **genetic counseling and carrier/cascade testing** in consanguineous families with an index case is the appropriate secondary-prevention measure. Given the mechanistic importance of **BCG vaccination as a trigger**, family history of BCG-related disease in a consanguineous kindred could in principle prompt genetic testing before vaccinating at-risk relatives, though no formal screening protocol has been published specific to IRF1.

Suggested NCIT/LOINC terms: NCIT:C15709 (Genetic Testing), general WES/panel testing codes; disease-specific IRF1 diagnostic assay codes are not yet standardized.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No IRF1-deficiency-specific survival statistics exist given the tiny reported cohort (n=2); broadly, **MSMD mortality ranges from ~40% to 80% depending on the severity of the underlying genetic defect** (general MSMD literature, PMC12255513 overview), with complete/null genotypes (as in both reported IRF1 cases) generally correlating with more severe disease within the MSMD spectrum, though direct IRF1-specific mortality figures are not yet published.
- **Disease course:** Recurrent, life-threatening mycobacterial disease episodes **despite multidrug antimycobacterial therapy** in both reported patients — indicating that antimicrobial therapy alone is often insufficient to fully control disease given the underlying failure of intrinsic macrophage antimycobacterial defense.
- **Complications:** Disseminated granulomatous disease at multiple anatomic sites (as is typical across MSMD); specific organ-failure or long-term sequela data for IRF1 deficiency were not available in the sources reviewed here.
- **Recovery potential:** Because the defect is selectively restricted to the IFN-γ/macrophage antimycobacterial axis (with preserved IFN-α/β antiviral immunity), prognosis may in principle be more favorable for this arm of immunity than for MSMD defects with broader combined immunodeficiency; however, this has not been formally studied.
- **Prognostic factors:** Genotype (complete/null vs. partial loss-of-function) is the dominant prognostic determinant across the MSMD gene family generally, by analogy; both reported IRF1 variants are complete-null alleles.

---

## 12. Treatment

- **Antimycobacterial pharmacotherapy:** Standard multidrug antimycobacterial regimens (e.g., combinations from rifamycins, macrolides, ethambutol, and other antimycobacterial agents used per pathogen and susceptibility) were used in both reported patients, but disease **recurred despite this treatment**, underscoring the need for immune-directed or curative approaches in confirmed genetic MSMD (NCIT:C15632/Chemotherapy is not the correct category — use NCIT:C15986 Pharmacotherapy for antimycobacterial drug therapy in general).
- **Interferon-gamma (IFN-γ) therapy:** Recombinant human IFN-γ is used across the MSMD spectrum in patients with **impaired IFN-γ production** (as opposed to impaired IFN-γ response), and has been specifically noted as a treatment approach applied in IRF1 deficiency in general MSMD treatment literature, though its efficacy in a defect that acts downstream of/parallel to STAT1 signaling (rather than at the level of cytokine production) is mechanistically less clearly predicted to be curative than in cytokine-production defects — this nuance should be flagged for careful sourcing at the individual-patient level during curation. NCIT term: consider NCIT:C1666 (Interferon Gamma) as `therapeutic_agent`, with `treatment_term` NCIT:C15986 (Pharmacotherapy).
- **Hematopoietic stem cell transplantation (HSCT):** Across the MSMD gene family, **HSCT is the only known curative treatment**, particularly indicated when the underlying defect **abolishes response to IFN-γ** rather than merely impairing its production (general MSMD literature; PMC/Orphanet MSMD sources). Given that IRF1 deficiency acts by abolishing the transcriptional response to IFN-γ in myeloid cells (i.e., a response defect, not solely a production defect), and given the demonstrated impairment of hematopoietic/immune cell development (T/NK cells), **HSCT is mechanistically a rational candidate curative therapy**, though no published outcome data for HSCT specifically in an IRF1-deficient patient were identified in this research pass.
- **Surgical/interventional:** Surgical debridement/drainage of localized suppurative or abscessed mycobacterial lesions (e.g., BCGitis lymphadenitis) may be used adjunctively, as in MSMD generally (NCIT:C15329, Surgical Procedure).
- **Supportive care:** General infection-related supportive care as clinically indicated.
- **Experimental/investigational:** No IRF1-deficiency-specific clinical trials (NCT identifiers) were identified in this research pass; patients would likely be considered, on a compassionate/individual basis, within broader primary-immunodeficiency/MSMD HSCT protocols.
- **Treatment strategy:** As with other MSMD defects, treatment algorithms hinge on distinguishing IFN-γ **production** defects (favoring recombinant IFN-γ) from IFN-γ **response** defects (favoring HSCT), and on genotype-specific severity — IRF1 deficiency, as a downstream transcriptional response defect with combined myeloid-functional and lymphoid-developmental impairment, likely sits closer to the "response defect, consider HSCT" end of this spectrum, though direct outcome evidence in IRF1-deficient patients remains to be published.

---

## 13. Prevention

- **Primary prevention:** The most clinically actionable primary-prevention consideration is **avoidance or deferral of BCG vaccination** in infants known (by prior family genetic diagnosis) to be at risk of biallelic *IRF1* (or other MSMD-gene) null variants, given that BCG vaccination was the precipitating exposure in reported cases. This mirrors established practice for other severe combined and MSMD-spectrum immunodeficiencies in which live vaccines are contraindicated.
- **Genetic counseling:** Essential in consanguineous families with an index case, given the autosomal recessive inheritance and elevated recurrence risk (25% per pregnancy for parents who are both carriers); prenatal or preimplantation genetic testing may be offered where the familial variant is known.
- **Secondary prevention/screening:** Cascade genetic testing of siblings/relatives in an affected consanguineous kindred, prior to BCG vaccination or other live-pathogen exposures, is the principal secondary-prevention strategy, though no formal published screening protocol specific to IRF1 deficiency exists.
- **Tertiary prevention:** Prompt recognition and multidrug antimycobacterial therapy at first presentation, with early consideration of curative HSCT, to prevent recurrent/progressive disseminated disease.
- **Environmental/public health interventions:** General avoidance of high-risk environmental mycobacterial exposures is a nonspecific consideration common to all MSMD patients but has not been formally studied for IRF1 deficiency specifically.

---

## 14. Other Species / Natural Disease

No naturally occurring IRF1-deficiency disease has been reported in non-human species in the sources reviewed for this report. IRF1 orthologs are broadly conserved across mammals (see Model Organisms below), and cross-species comparative-pathology or veterinary case data specific to spontaneous *IRF1* loss-of-function disease were not identified in this research pass; if curating this section further, OMIA (Online Mendelian Inheritance in Animals) and veterinary case-report literature should be searched directly, as none surfaced here.

---

## 15. Model Organisms

**Primary model: *Irf1*-knockout (*Irf1⁻/⁻*) mouse** (JAX strain 002762), which has been extensively used to define IRF1 immune biology well before the human disease was described, and whose phenotype strongly recapitulates and mechanistically anticipates the 2023 human findings:

- **NK cell development:** *Irf1⁻/⁻* mice show **strongly reduced NK cell numbers**. Mechanistically, IRF1 acts **non-cell-autonomously**: it is required in the **radiation-resistant bone-marrow stromal microenvironment** (via induction of **IL-15**) to support NK-cell development, **not** in the NK-cell progenitors themselves — *Irf1⁻/⁻* bone-marrow cells can generate functional NK cells when cultured with exogenous IL-15 (PMID: 9490414, "Requirement for IRF-1 in the microenvironment supporting development of natural killer cells"). NK-cell cytotoxicity and IFN-γ secretion (particularly after IL-12 stimulation) are abrogated.
- **T-cell/Th1 development:** *Irf1⁻/⁻* mice show **impaired CD8+ T-cell and NK-cell maturation**, **impaired IL-12 production by macrophages**, **exclusive Th2 skewing**, and **defective Th1 differentiation**.
- **Antigen presentation:** *Irf1⁻/⁻* mice **lack expression of gene products involved in antigen presentation** (consistent with IRF1's role in inducing TAP1, LMP2/PSMB9, and CIITA), compounding the Th1/NK/CD8 defects into a broader immunodeficient phenotype.
- **Fidelity to human disease:** The mouse model **recapitulates** the key human findings — impaired NK/T development, impaired IL-12/IFN-γ axis function, and impaired antigen-presentation gene induction — providing strong mechanistic support (HIGH-to-MODERATE fidelity) for the human transcriptomic finding of impaired T/NK developmental gene expression. A notable divergence/translational caveat: the mouse literature identifies the NK-cell defect as **stromal-microenvironment-driven (via IL-15)** rather than NK-progenitor-intrinsic — whether this same non-cell-autonomous mechanism explains the T/NK developmental abnormality reported in human IRF1-deficient patients has not yet been directly tested and should be flagged as an open question (a candidate `HUMAN_MODEL_MISMATCH`-type consideration for dismech curation) rather than assumed.
- **Tumor-suppressor phenotype in mice:** *Irf1⁻/⁻* mice crossed onto HRAS-transgenic or *p53⁻/⁻* backgrounds show **markedly increased tumor susceptibility**, supporting IRF1's tumor-suppressor role independent of, but molecularly convergent with, its immune function (Genes Dev., PMID search results).

**Suggested GO/CL/NCBITaxon terms:** NCBITaxon:10090 (Mus musculus); CL:0000623 (natural killer cell); CL:0000084 (T cell); GO:0032609 (interferon-gamma production); GO:0002250 (adaptive immune response).

**Other model systems:** No zebrafish, *Drosophila*, *C. elegans*, yeast, organoid, or iPSC-derived model systems specific to IRF1 immunodeficiency were identified in this research pass; the mouse knockout remains the dominant and best-characterized model organism for IRF1 immune function.

---

## Summary of Key Evidence Sources

| Citation | Content |
|---|---|
| Rosain et al., *Cell* 2023 (PMC9907019 / PMID: 36736301) | Founding description of human IRF1 deficiency (n=2 patients); genetics, immunology, mechanism |
| OMIM #620668 (Immunodeficiency 117) | Clinical synopsis, molecular genetics summary (abstracts Rosain et al.) |
| OMIM *147575 (IRF1 gene) | Gene identifiers, historical tumor-suppressor literature |
| Orphanet ORPHA:699615 | Disease nomenclature ("Complete IRF1 deficiency") |
| PMC10023504 | Review: "Inborn errors of human transcription factors governing IFN-γ antimycobacterial immunity" — comparative context with STAT1, IRF8, RORC deficiencies |
| PMC12255513 | General MSMD overview: genetics, treatment (IFN-γ vs. HSCT), mortality range (40–80%) |
| Willman et al., *Science* 1993 (PMID: 8438156) | IRF1 as 5q31 myeloid tumor-suppressor candidate |
| PMID: 9490414 | *Irf1⁻/⁻* mouse NK-cell developmental defect, stromal IL-15 mechanism |
| PMID: 9422515 (PDB 1IF1) | IRF1 DNA-binding domain crystal structure |
| PMC4398980 | Genome-wide IRF1 ChIP-seq binding site identification |

**Data gaps flagged for curators:** (1) No published cases beyond the original two patients were identified as of this research pass — a targeted PubMed/ClinVar search closer to curation time is recommended to check for newer case reports (2024–2026). (2) gnomAD constraint metrics (pLI/LOEUF) for *IRF1* should be pulled directly from the gnomAD browser. (3) HSCT outcome data specific to IRF1-deficient patients were not found and may not yet exist in the literature — do not assert HSCT efficacy in IRF1 deficiency without a direct primary-source citation. (4) Full clinical narrative detail (exact organs involved, ages, treatment timelines, and outcomes/survival status per patient) should be extracted directly from the *Cell* 2023 full text or its supplementary materials, which could not be fully retrieved as clean text in this research pass (proxy/CAPTCHA access issues) — curators should fetch the primary PDF directly for exact abstract quotes to support `evidence` snippets.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC9907019`: "**IRF1-deficient mononuclear macrophages do not control mycobacteria or related intramacrophagic pathogens normally in response to IFN-γ**"
  - closest text in source: "Moreover, IRF1-deficient mononuclear phagocytes do not control mycobacteria and related pathogens normally when stimulated with IFN-γ"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 25 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100646` (1 mention) - the report calls it "Abnormal lymph node morphology / lymphadenopathy"; HP calls it **Thyroiditis**
- `HP:0410030` (1 mention) - the report calls it "Impaired lymphocyte transformation / abnormal T-cell physiology"; HP calls it **Cleft lip**
- `HP:0002960` (1 mention) - the report calls it "Autoimmunity / immune dysregulation — not reported in IRF1 deficiency to date"; HP calls it **Autoimmunity**
- `GO:0000785` (1 mention) - the report calls it "chromatin, where IRF1 binds ISRE elements"; GO calls it **chromatin**
- `UBERON:0002370` (2 mentions) - the report calls it "thymus, relevant to T-cell development"; UBERON calls it **thymus**
- `NCIT:C1666` (1 mention) - the report calls it "Interferon Gamma"; NCIT calls it **Tyrphostin A30**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002718` (1 mention) - the report calls it "Recurrent infections"; HP calls it **Recurrent bacterial infections**, and lists "Recurrent pyogenic infections" among its other names
- `GO:0071346` (1 mention) - the report calls it "cellular response to interferon-gamma"; GO calls it **cellular response to type II interferon**, and lists "cellular response to gamma-interferon" among its other names
- `GO:0140374` (1 mention) - the report calls it "antiviral innate immune response — for the preserved arm"; GO calls it **antiviral innate immune response**
- `GO:0032609` (1 mention) - the report calls it "interferon-gamma production"; GO calls it **type II interferon production**, and lists "interferon-gamma production" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:6116` - called "IRF1", "Gene:** *IRF1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.