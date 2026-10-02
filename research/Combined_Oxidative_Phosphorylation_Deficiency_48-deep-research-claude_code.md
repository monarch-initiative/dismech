---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-08T07:54:37.217044'
end_time: '2026-09-08T08:00:13.861588'
duration_seconds: 336.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined oxidative phosphorylation deficiency 48
  mondo_id: MONDO:0033566
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
  web_search_requests: 9
  num_turns: 21
  total_cost_usd: 1.3192638000000003
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 40
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 15
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0003128
    reported_labels:
    - present across essentially all early-onset cases; a hallmark biochemical abnormality
    ontology_label: Lactic acidosis
  - term_id: CHEBI:5991
    reported_labels:
    - Idebenone
    ontology_label: CHEBI_5991
  labels_variant: 10
  obsolete_terms:
  - term_id: CHEBI:5991
    ontology_label: CHEBI_5991
    replaced_by: CHEBI:28638
  unresolvable_prefixes:
  - MGI
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined oxidative phosphorylation deficiency 48
- **MONDO ID:** MONDO:0033566 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined oxidative phosphorylation deficiency 48** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency 48 (COXPD48) — Research Report

## 1. Disease Information

**Overview:** COXPD48 is an autosomal recessive mitochondrial translation disorder caused by biallelic loss-of-function or hypomorphic variants in **NSUN3** (NOP2/Sun RNA methyltransferase family member 3), which encodes the enzyme that installs 5-methylcytosine (m⁵C) at the wobble position (C34) of mitochondrially-encoded tRNA-Met (mt-tRNA^Met). This methylation is the obligate first step toward 5-formylcytosine (f⁵C34) formation (catalyzed downstream by ALKBH1/ABH1), which is required for mt-tRNA^Met to decode both AUG and the non-canonical AUA codon during mitochondrial translation. Loss of this modification causes a combined (multi-complex) OXPHOS deficiency due to impaired mitochondrial protein synthesis, producing a disease that — as characterized by the founding 2016 case and subsequent reports — spans from an isolated, adult-onset optic atrophy phenotype to a severe, early-onset multisystem mitochondrial encephalomyopathy (Van Haute et al., *Nat Commun* 2016, PMID:27356879; Jurkute et al., *IOVS* 2025, PMID:40465263).

**Key identifiers:**
- **OMIM disease:** #619012 — COMBINED OXIDATIVE PHOSPHORYLATION DEFICIENCY 48; COXPD48
- **OMIM gene:** *617491 — NOP2/SUN RNA METHYLTRANSFERASE FAMILY, MEMBER 3; NSUN3
- **HGNC:** NSUN3, HGNC:26208
- **MONDO:** MONDO:0033566
- **Gene location:** 3q11.2
- **Inheritance:** Autosomal recessive
- **Category (broader MONDO grouping):** combined oxidative phosphorylation deficiency (a genetically heterogeneous group; COXPD1 through COXPD5x+, each numbered entry defined by a distinct causal gene)

**Synonyms:** "NSUN3-related mitochondrial disease," "NSUN3 deficiency," and — for the milder end of the spectrum — "NSUN3-related optic neuropathy" / "isolated optic atrophy due to NSUN3 variants" (Jurkute et al. 2025 explicitly reframe this as a phenotypic continuum rather than distinct diseases).

**Evidence base type:** The entirety of the clinical literature is **individual patient/case-series data** (case reports and small multi-family case series totaling ~10 published individuals worldwide as of 2025), not aggregated registry or EHR-derived statistics — there is no disease registry, and Orphanet/GeneReviews do not yet carry a dedicated COXPD48 entry independent of OMIM. This is an ultra-rare, essentially "n-of-few" disorder.

---

## 2. Etiology

**Disease causal factor:** Purely genetic — biallelic (homozygous or compound heterozygous) pathogenic variants in *NSUN3*. No environmental, infectious, or acquired etiology has been implicated in the primary disease process, though intercurrent infection has been reported as a **seizure trigger** in at least one severe case (norovirus infection preceding status epilepticus in a 4-year-old girl; Jurkute et al. 2025, PMID:40465263).

**Genetic risk factors:**
- Biallelic *NSUN3* variants are necessary and (to current knowledge) sufficient to cause disease; no polygenic or susceptibility-locus component has been described.
- **Variant-severity correlation is the dominant modifier identified to date:** complete loss-of-function alleles (nonsense, frameshift, canonical splice-site) are associated with the **severe, early-onset multisystem phenotype**, while missense variants retaining partial activity (particularly those outside the catalytic SAM-binding domain) are associated with the **milder, later-onset isolated optic atrophy phenotype**. Jurkute et al. state explicitly: *"Loss of function variants were associated with a more severe phenotype"* (PMID:40465263). Compare:
  - Severe: c.123-615_466+2155del (p.Glu42Valfs*11) / c.295C>T (p.Arg99*) — compound het null alleles, infantile-onset encephalomyopathy (Van Haute 2016)
  - Severe: c.150G>A (p.Trp50*) homozygous — infantile-onset (Jurkute Family 4)
  - Mild: c.812A>G (p.Glu271Gly) homozygous, downstream of the SAM domain — isolated adolescent-onset optic atrophy (Jurkute Family 1)
- **Consanguinity** is a recurrent feature: reported in the Van Haute index family, the Paramasivam case (consanguineous East Asian parents), and Jurkute Family 1 (consanguineous Pakistani parents) and Family 3, consistent with a rare AR disorder ascertained disproportionately in consanguineous pedigrees.
- One case (Jurkute Family 1, proband III-2) carried **paternal uniparental disomy of chromosome 3**, which converted a heterozygous paternal frameshift variant to apparent homozygosity — a mechanism worth flagging for any curated `genetic_context`/`variant_origin` annotation, since the mutational mechanism (UPD rather than biparental transmission of two mutant alleles) differs from ordinary autosomal recessive segregation.
- No modifier genes have been reported. One severe-phenotype individual (Jurkute Family 2, II-1) also carried an independent homozygous LOF variant in a heme-synthesis gene, invoked to explain concurrent sideroblastic anemia as a **separate, non-NSUN3 comorbidity** rather than a true genetic modifier of the mitochondrial phenotype.

**Environmental/other risk factors:** None established as causal. No described protective genetic or environmental factors (the gene is too rare for GWAS-type protective-variant discovery).

**Gene-environment interaction:** Not systematically studied; the single reported infection-triggered seizure exacerbation (norovirus) suggests that intercurrent catabolic/febrile stress may unmask or worsen the mitochondrial translation defect, as is well established for other combined OXPHOS deficiencies generally, but this has not been specifically investigated for NSUN3 disease.

---

## 3. Phenotypes

The phenotype is best organized along the severity spectrum identified by Jurkute et al. 2025 (8 patients / 5 families), integrated with the two prior single-patient reports.

### Ophthalmological (near-universal; present in 7/8 of the 2025 cohort, 87.5%)
- **Bilateral optic atrophy / optic neuropathy** — HP:0000648 (Optic atrophy)
  - Onset ranges from infancy (nystagmus/optic atrophy noted <3 months in the index Van Haute patient) to the fourth decade (age 40, Family 3 father)
  - Progressive visual acuity decline is typical; some patients show a **LHON-like acute/subacute presentation** with disc edema, telangiectatic peripapillary microangiopathy, and subsequent partial spontaneous recovery — distinct from the classically insidious optic atrophy of most mitochondrial optic neuropathies
  - **Nystagmus** (convergence nystagmus in the index case; rotatory nystagmus in the optic-neuropathy case) — HP:0000639
  - **Cataract** ("blue dot" / cerulean cataract) recurring across multiple family members — HP:0010696
  - Color vision deficits (Ishihara/D-15 panel abnormalities) — HP:0000551 (Impaired color vision)
  - Central scotomas — HP:0000618
  - OCT: reduced peripapillary RNFL and ganglion cell layer thickness
  - Electrophysiology: delayed/subnormal pattern VEP, abnormal PERG, and in the severe multisystem cases, generalized rod/cone ERG dysfunction (electronegative ERG), indicating a combined optic-nerve **and** outer/inner retinal process in the more severe end of the spectrum

### Neurological (severe/early-onset end of spectrum)
- **Global developmental delay** — HP:0001263
- **Microcephaly** (low-grade to overt) — HP:0000252
- **Muscular hypotonia** — HP:0001252
- **Muscle weakness**, proximal-accentuated — HP:0001324 / HP:0003701
- **External ophthalmoplegia** — HP:0000544
- **Seizures**, generalized, recurrent, drug-refractory (levetiracetam-resistant in one case) — HP:0001250
- **Peripheral neuropathy** (generalized axonal sensorimotor) — HP:0007002
- **Sensorineural hearing loss**, mild — HP:0000407
- **Dysarthria** — HP:0001260

### Growth/systemic
- **Failure to thrive / inadequate weight gain** — HP:0001508
- **Small for gestational age** — HP:0001518
- Growth hormone deficiency, insulin resistance, borderline thyroid dysfunction (one severe case)
- **Cardiac malformation** (bicuspid aortic valve, atrial septal defect) in one severe case — HP:0001647 / HP:0001631

### Laboratory/metabolic
- **Elevated plasma lactate / lactic acidosis** — HP:0002151 / HP:0003128 (present across essentially all early-onset cases; a hallmark biochemical abnormality)
- Hypoglycemia, hypernatremia, and severe metabolic acidosis during an acute seizure episode in one case
- **Combined OXPHOS deficiency on muscle biopsy** — reduced activity of Complex I and Complex IV predominantly (Complex II/III typically normal — consistent with the exclusively mtDNA-encoded-subunit-dependent complexes being selectively vulnerable to a translation defect)

### Muscle histopathology
- Variable: ranges from **no COX-negative fibers / no ragged-red fibers** (Family 1, milder phenotype) to **multiple COX-negative fibers with subsarcolemmal mitochondrial aggregates and swollen mitochondria with massively reduced/linearized cristae on EM** (Family 3, more severe optic-neuropathy-with-neuropathy phenotype). This heterogeneity itself is notable and should be curated per-subtype rather than as a single canonical histopathology finding.

### Onset/severity/progression summary
- **Age of onset:** ranges from neonatal/infantile (<3 months, most severe) to the fourth decade (isolated optic atrophy, mildest) — mean ~17 years (SD ±12) across the 2025 cohort, reflecting strong bimodal clustering rather than a true continuous distribution
- **Severity:** frankly variable and appears to track genotype (LOF vs. hypomorphic missense) as above
- **Progression:** Chronic/progressive for the optic neuropathy component in essentially all patients; the encephalomyopathic/seizure component in severe cases is also progressive, punctuated by infection-triggered exacerbations
- **Quality of life impact:** Not formally measured with any validated instrument (EQ-5D/SF-36) in any published report; qualitatively, severe cases show substantial functional impairment (developmental delay, refractory seizures) while the isolated optic atrophy cases retain ambulatory independence with visual impairment as the dominant burden.

---

## 4. Genetic/Molecular Information

**Causal gene:** NSUN3 (HGNC:26208; NCBI Gene ID 63899; OMIM *617491), chromosome 3q11.2. Encodes a mitochondrially-targeted member of the NOP2/Sun RNA methyltransferase family.

**Reported pathogenic/likely pathogenic variants (cDNA reference NM_022072):**

| Variant (cDNA) | Protein | Zygosity | Type | Source |
|---|---|---|---|---|
| c.123-615_466+2155del | p.Glu42Valfs*11 | compound het | large deletion/frameshift (exon 3) | Van Haute 2016, PMID:27356879 |
| c.295C>T | p.Arg99* | compound het (with above) | nonsense | Van Haute 2016 |
| c.421G>C | p.Ala141Pro | compound het | missense (exon 3) | Paramasivam 2020, PMID:32488845 |
| c.454T>A | p.Cys152Ser | compound het (with above) | missense (exon 3) | Paramasivam 2020 |
| c.349_352dup | p.Ala118Glufs*45 | homozygous | frameshift (exon 3) | PMID:38790159 (isolated optic atrophy) |
| c.812A>G | p.Glu271Gly | homozygous | missense, downstream of SAM domain | Jurkute 2025, PMID:40465263 (VUS; mild phenotype) |
| c.424C>T | p.Pro142Ser | homozygous | missense, within SAM domain | Jurkute 2025 (likely pathogenic; severe phenotype) |
| c.930_931delAT | p.Cys311Trpfs*8 | "homozygous" via paternal UPD3 | frameshift (terminal exon) | Jurkute 2025 |
| c.150G>A | p.Trp50* | homozygous | nonsense | Jurkute 2025 (pathogenic; severe phenotype) |

**ACMG/AMP classification:** Ranges from VUS to pathogenic across the reported alleles (see table); loss-of-function alleles are more consistently classified pathogenic/likely pathogenic (PVS1-triggering), while several missense alleles remain VUS pending further functional or population data — an important curation caveat, since not every reported variant meets a confident pathogenicity bar.

**Allele frequency:** NSUN3 is not a commonly studied gene in population databases; no specific gnomAD constraint metrics (pLI/LOEUF) were retrievable in this search session, and given the rarity of reported disease alleles, population frequency data for the specific pathogenic variants is expected to be at or near absent from gnomAD — this should be verified directly against gnomAD/ClinVar at curation time rather than assumed.

**Functional consequence:** All functionally characterized alleles converge on **loss of NSun3-catalyzed m⁵C34 methylation of mt-tRNA^Met**, quantified in the 2025 cohort as tRNA^Met methylation reduced "to background levels" versus 26–33% methylation in controls — interpreted by the authors as evidence of **complete functional loss** even for some missense alleles. Downstream consequences demonstrated across the case reports:
- Absent or markedly reduced full-length NSun3 protein (patient fibroblasts, Van Haute 2016)
- Defective mitochondrial translation / protein synthesis
- Reduced steady-state levels and enzymatic activity of Complex I and Complex IV (the OXPHOS complexes with the largest mtDNA-encoded subunit content)
- Reduced basal oxygen consumption rate (OCR), reduced ATP-linked OCR, and reduced maximal (FCCP-uncoupled) respiration on Seahorse extracellular flux assay in patient fibroblasts
- Impaired growth under galactose-forcing conditions (a classic functional readout of OXPHOS-dependent, as opposed to glycolysis-dependent, cellular energy metabolism)
- Rescue of the translation defect by re-expression of wild-type NSUN3 (Van Haute 2016) — establishing causality

**Chromosomal abnormalities:** Not a feature of this disease (single-gene point/small-indel mechanism); the one structural exception is the large 3,114 bp intragenic deletion in the index patient (c.123-615_466+2155del), and the reported paternal UPD3 event, which is a mechanism of homozygosity rather than a pathogenic chromosomal rearrangement per se.

**Epigenetic information:** Not directly studied for NSUN3 disease; conceptually notable that NSUN3 itself is an RNA-modifying (epitranscriptomic) enzyme, so the entire disease mechanism is, in a sense, a defect of RNA epitranscriptomic modification rather than DNA epigenetics — worth flagging in `pathophysiology` framing but distinct from DNA methylation/chromatin biology.

---

## 5. Environmental Information

No environmental toxins, occupational exposures, radiation, or lifestyle factors have been implicated as disease-causal — this is a monogenic mitochondrial translation disorder. The one environment-adjacent finding is **infection as a symptom trigger/exacerbant**: norovirus gastroenteritis preceded a seizure exacerbation with T2-hyperintense parieto-occipital lesions on MRI in one severe-phenotype patient (Jurkute 2025, Family 4). This is analogous to the well-documented pattern in other mitochondrial disorders where febrile/catabolic illness precipitates metabolic decompensation, but has not been mechanistically dissected for NSUN3 disease specifically. No infectious agent is causal to the underlying disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Biallelic loss-of-function or hypomorphic missense variants in *NSUN3* **lead to** absent or markedly reduced NSun3 methyltransferase enzymatic activity in mitochondria (demonstrated directly: complete loss of full-length protein for null alleles; near-complete loss of catalytic methylation activity even for some missense alleles, PMID:40465263).
2. Loss of NSun3 activity **results in** failure to install 5-methylcytosine at the wobble position C34 of mitochondrial tRNA-Met (mt-tRNA^Met) — demonstrated directly by mass-spectrometric/primer-extension quantification of tRNA modification in patient cells (Van Haute 2016; Jurkute 2025).
3. Absent m⁵C34 **prevents** the obligate downstream oxidation step, catalyzed by ALKBH1 (ABH1), that converts m⁵C34 to 5-formylcytosine (f⁵C34) — this two-step methylation→oxidation pathway was mechanistically established in parallel by Nakano et al. (*EMBO J* 2016, PMID:27497299), who showed NSUN3 and ALKBH1 act sequentially on the same wobble base.
4. Absence of f⁵C34 **abolishes** the expanded codon-recognition capacity that this modified base normally confers, so mt-tRNA^Met can no longer efficiently decode the non-canonical mitochondrial AUA (isoleucine-in-standard-code but methionine-in-mitochondrial-code) start/internal codon in addition to AUG.
5. Impaired AUA/AUG decoding by mt-tRNA^Met **causes** stalling or reduced fidelity of mitochondrial ribosomal translation of the 13 mtDNA-encoded OXPHOS subunit mRNAs (demonstrated directly: reduced de novo mitochondrial protein synthesis in patient fibroblasts, Van Haute 2016).
6. Defective synthesis of mtDNA-encoded subunits **results in** selectively reduced steady-state levels and enzymatic activity of the OXPHOS complexes that are heavily dependent on mtDNA-encoded subunits — predominantly **Complex I** (7 mtDNA-encoded subunits) and **Complex IV** (3 mtDNA-encoded subunits) — while Complex II (entirely nuclear-encoded) remains normal; this pattern is consistently reproduced across all reported muscle biopsies and fibroblast studies.
7. Combined Complex I/IV deficiency **leads to** reduced mitochondrial oxygen consumption and ATP-linked respiration (directly measured by Seahorse respirometry: reduced basal OCR, reduced ATP-production-linked OCR, and reduced maximal FCCP-uncoupled respiration in patient fibroblasts, Jurkute 2025) and **results in** compensatory reliance on glycolysis, evidenced by impaired growth specifically under galactose-forced-oxidative-metabolism culture conditions.
8. Chronic cellular energy deficit in the most metabolically demanding, post-mitotic, high-energy-dependent tissues — **retinal ganglion cells and their axons (optic nerve)**, central and peripheral neurons, and skeletal/cardiac muscle — **produces** the clinical phenotype: progressive retinal ganglion cell degeneration/optic atrophy (the near-universal manifestation), and, when the underlying molecular lesion is more severe (complete loss-of-function alleles), an additional encephalomyopathic phenotype of developmental delay, hypotonia, seizures, and lactic acidosis. This branch point — optic-nerve-only vs. multisystem involvement — is the central genotype-phenotype correlation identified in the literature (inferred correlation, not yet mechanistically dissected at the level of *why* retinal ganglion cells are so uniformly vulnerable even in hypomorphic-allele carriers who otherwise lack systemic disease).
9. In the mouse model, complete loss of Nsun3 **causes** embryonic lethality between E10.5–E12.5 (Murakami et al., *Commun Biol* 2023, PMID:36949224), establishing that some minimal threshold of mt-tRNA^Met modification/mitochondrial translation is essential for normal embryonic development — a step with no direct human correlate (no reported homozygous-null human survivors), consistent with all reported human disease alleles being hypomorphic or, when null, apparently compatible with survival only via as-yet-unexplained residual translational capacity or genetic background effects (this gap between "null alleles are viable in humans but embryonic lethal in mice" is worth flagging explicitly as a species-discordance caveat for any `HUMAN_MODEL_MISMATCH` discussion node).

### Molecular pathways
Mitochondrial translation / mitoribosome function; tRNA wobble-position modification pathway (NSUN3 → ALKBH1/ABH1 sequential C34 methylation-then-oxidation). GO: **GO:0032259** (methylation), **GO:0070901** (mitochondrial tRNA methylation), **GO:0032543** (mitochondrial translation), **GO:0070125** (mitochondrial translational elongation).

### Cellular processes
Mitochondrial protein synthesis; oxidative phosphorylation; cellular respiration; (secondarily, in severe cases) neuronal/retinal-ganglion-cell degeneration.

### Protein dysfunction
Loss-of-function (null alleles: absent protein) or partial loss-of-function (hypomorphic missense within/near the SAM-methyltransferase catalytic domain) of a mitochondrial matrix-targeted, SAM-dependent RNA methyltransferase. UniProt: **Q9H649** (NSUN3_HUMAN).

### Metabolic changes
Impaired oxidative energy metabolism with compensatory glycolytic dependence; lactic acidosis reflects a shift toward anaerobic glycolysis and/or impaired pyruvate oxidation secondary to Complex I/IV deficiency.

### Biochemical abnormalities
Reduced Complex I and Complex IV enzymatic activities in skeletal muscle (quantitatively documented, e.g., Complex I 0.078 vs. normal range 0.118–0.332; Complex IV 0.003 vs. normal 0.013–0.039 in one biopsy — units as reported, nmol/min/mg or similar respiratory-chain-assay units per the source; verify exact units against the source before curating numerically). Low tissue ubiquinone (CoQ10) also reported in one biopsy (94 pmol/mg vs. normal 140–850), of uncertain primary vs. secondary significance.

### Cell types / anatomical relevance
Retinal ganglion cells (CL:0000740) and their unmyelinated/myelinated axons in the optic nerve are the most consistently and severely affected cell population; skeletal myocytes (CL:0000188), cardiomyocytes (in the mouse heart-specific knockout and in one human case with structural cardiac defects), and central/peripheral neurons in the severe phenotype.

### Molecular profiling
No transcriptomic, proteomic, or metabolomic datasets specific to NSUN3/COXPD48 patients were identified in this search (beyond the targeted respirometry/western blot/immunocytochemistry functional assays described above). No single-cell, spatial transcriptomic, or CRISPR screen data specific to this gene/disease were found.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Optic nerve / eye (UBERON:0000970 eye; UBERON:0001780 optic nerve) — near-universal
- **Secondary/severe-phenotype:** Central nervous system (brain), peripheral nerves, skeletal muscle, heart (bicuspid aortic valve, ASD in one case), inner ear (sensorineural hearing loss), bone marrow (sideroblastic anemia, though likely a separate co-occurring gene defect in that case), skin (cerulean/blue-dot cataract — lens), retina (rod/cone ERG abnormalities in severe cases, beyond pure optic-nerve involvement)
- **Body systems:** Nervous system, visual system, musculoskeletal system, and — in the most severe cases — endocrine (growth hormone deficiency, insulin resistance, thyroid), cardiovascular, and hematopoietic systems

**Tissue/cell level:**
- Retinal ganglion cells and optic nerve axons (CL:0000740)
- Skeletal muscle fibers, particularly type I (oxidative) fibers showing subsarcolemmal mitochondrial aggregation (CL:0000188 / CL:0000189)
- Peripheral sensorimotor axons (axonal neuropathy pattern)
- Cardiomyocytes (CL:0000746) — established in the mouse heart-specific knockout, and clinically relevant given the one human case with structural congenital heart disease

**Subcellular level:**
- **Mitochondria**, specifically the mitochondrial matrix (site of mitochondrial translation) — GO:0005759 (mitochondrial matrix), GO:0005739 (mitochondrion)
- Mitochondrial cristae — structurally abnormal (fragmented/linearized, reduced in number) on electron microscopy in both the mouse cardiac model and human muscle biopsy
- Mitochondrial ribosome / mitochondrial tRNA — GO:0005762 (mitochondrial large ribosomal subunit), GO:0032543 (mitochondrial translation)

**Localization/laterality:** Ophthalmological involvement is consistently **bilateral**; neurological/systemic involvement is not lateralized.

---

## 8. Temporal Development

**Onset:** Bimodal — either **congenital/infantile** (<3 months to ~1 year, associated with null/severe LOF alleles) or **adolescent-to-adult** (11–40 years, associated with hypomorphic missense alleles and isolated optic atrophy). No cases of purely adult-onset multisystem disease have been reported; severity of the systemic component appears fixed early by genotype rather than accumulating de novo in adulthood.

**Onset pattern:** Insidious/progressive for the optic atrophy trajectory in most patients; **subacute** in the LHON-like presentations (rapid visual decline over weeks-to-months, e.g., 6/6 to 6/24 over 13 years in one case, or 6/60 to 6/120 within 3 months in another, the latter followed by partial spontaneous/treatment-associated recovery).

**Progression:** Chronic and generally progressive for both the optic neuropathy and, where present, the encephalomyopathic components; punctuated by acute exacerbations (e.g., infection-triggered seizure/encephalopathy episode).

**Course pattern:** Predominantly progressive, though the reported spontaneous partial visual recovery in one LHON-like case (with subsequent idebenone-associated further improvement) indicates that **the disease course is not uniformly monotonically progressive** — an important nuance for any `progression`/`phase` modeling, since it departs from the classic "stable-then-declining" mitochondrial optic neuropathy pattern typical of LHON itself.

**Disease duration:** Lifelong/chronic; no spontaneous full resolution reported. Longest-followed patients are in their third-to-fourth decade of life with stable, if visually impaired, function.

**Critical periods:** Not formally established, but the striking difference between embryonic-lethal complete Nsun3 loss in mice and viable (if severely affected) human null-allele carriers suggests there may be a developmental window of particular vulnerability to complete pathway loss that current human genotypes have not fully probed (all reported human "null" genotypes retain at least some low-level residual protein/activity, or the true molecular null is not compatible with live birth and is therefore unascertained).

---

## 9. Inheritance and Population

**Epidemiology:** No prevalence or incidence estimates exist; COXPD48 is not yet listed as a standalone entry in Orphanet, and the total published literature comprises **approximately 10–11 individuals across 3 primary reports plus a 2016 mechanistic paper's index case** (Van Haute 2016 = 1 patient; Paramasivam 2020 = 1 patient; the isolated-optic-atrophy report (PMID:38790159) = 1 patient; Jurkute 2025 = 8 patients/5 families, one of which is the previously-reported Van Haute index case). This makes it one of the rarest of the numbered COXPD entries; true population prevalence is unknown and likely substantially underascertained given the milder end of the phenotypic spectrum (isolated optic atrophy) plausibly overlapping with undiagnosed "simplex" optic atrophy cases in the community.

**Inheritance pattern:** Autosomal recessive (biallelic pathogenic variants required); one case demonstrates that apparent homozygosity can arise via **uniparental disomy** rather than biparental transmission — a mechanism curators should not assume away when a proband is "homozygous" with only one carrier parent identified.

**Penetrance:** Appears high/complete for the optic neuropathy component among carriers of biallelic pathogenic variants reported to date, though ascertainment bias (case reports select for affected probands) makes true penetrance impossible to estimate from available data.

**Expressivity:** Markedly variable — the central finding of the 2025 multi-family study is a continuous phenotypic spectrum from isolated optic atrophy to severe multisystem disease, correlated with (but not perfectly predicted by) variant type/severity.

**Genetic anticipation:** Not applicable/not reported (no repeat-expansion mechanism).

**Germline mosaicism:** Not reported.

**Founder effects:** Not established; reported families are of Pakistani, Colombian, Afghan, Japanese, and unspecified East Asian ancestry, without a shared founder haplotype identified.

**Consanguinity:** A recurrent feature across multiple independent families (Van Haute index family, Paramasivam case, Jurkute Families 1 and 3), consistent with the disease's rarity and AR inheritance.

**Carrier frequency:** Unknown/not established in any population database search performed here; this should be checked directly in gnomAD at curation time.

**Population demographics:** Reported cases span Northern European (original index patient), East Asian, South Asian (Pakistani), Latin American (Colombian), Central Asian (Afghan), and Japanese ancestries — i.e., no clear geographic/ethnic restriction, consistent with a pan-ethnic ultra-rare AR disorder. **Sex ratio:** Striking male predominance in the reported cohort (7 of 8 patients in the 2025 series, plus both single-patient prior reports were male infants) — noted by the authors but unexplained mechanistically, since the gene is autosomal; this is very likely an ascertainment artifact of a tiny sample size rather than a true biological sex effect, and should be flagged as such rather than asserted as a sex-linked biological finding.

---

## 10. Diagnostics

**Laboratory tests:**
- Plasma lactate (elevated in early-onset/severe cases) — LOINC relevant to lactate assays
- Blood gas / metabolic panel during acute decompensation (documented hypoglycemia, hypernatremia, severe metabolic acidosis in one case)
- Plasma homocysteine — elevated in two adult patients with isolated optic atrophy (Jurkute Family 3), of uncertain mechanistic significance but worth noting as an associated lab finding
- Serum SAM (S-adenosylmethionine) — reported normal in one mild-phenotype family, presumably tested given NSUN3's SAM-dependent catalytic mechanism

**Biomarkers:** No validated circulating biomarker specific to NSUN3 disease; muscle-tissue Complex I/IV enzymatic activity and CoQ10 level function as tissue-level (not circulating) biomarkers in the reported cases.

**Imaging:**
- Optic nerve/orbital MRI: typically shows slender/atrophic optic nerves; occasionally T2 hyperintensity
- Brain MRI: usually unremarkable in the isolated-optic-atrophy phenotype; in the most severe case, T2-hyperintense edematous lesions in parietal/occipital lobes during an acute seizure episode
- OCT (optical coherence tomography): reduced peripapillary RNFL and ganglion cell layer thickness — the most sensitive structural biomarker of the optic neuropathy component

**Functional/electrophysiological tests:**
- Pattern and full-field visual evoked potentials (VEP) — delayed/subnormal
- Pattern ERG (PERG) — reduced/abnormal P50, consistent with retinal ganglion cell dysfunction
- Full-field ERG — abnormal (electronegative waveform, delayed b-waves) in the severe multisystem phenotype, indicating additional outer/inner retinal (not purely optic-nerve) involvement
- EEG — performed in seizure cases; can be unremarkable interictally

**Biopsy/histopathology:**
- Skeletal muscle biopsy with histochemistry (COX/SDH staining), Western blot for OXPHOS subunits (reduced COX II/Complex IV and NDUFB8/Complex I), and electron microscopy (abnormal mitochondrial size/cristae) — the diagnostic gold standard historically used before genetic confirmation, still valuable for functional characterization
- Skin biopsy → dermal fibroblast culture for confirmatory functional studies (immunocytochemistry, Seahorse respirometry, tRNA methylation assay)

**Genetic testing:**
- **Recommended approach:** given the phenotypic overlap with other mitochondrial optic neuropathies (LHON, dominant optic atrophy/*OPA1*) and other combined OXPHOS deficiencies, whole exome sequencing (WES) or a targeted mitochondrial-disease/optic-atrophy gene panel including *NSUN3* is the most efficient diagnostic strategy, particularly for the milder isolated-optic-atrophy presentation where clinical suspicion of "combined OXPHOS deficiency" may not be raised
- mtDNA testing is relevant primarily to **exclude** primary mtDNA disorders (e.g., LHON mtDNA point mutations) as the alternative explanation for a LHON-like presentation, since NSUN3 disease can mimic classic LHON clinically
- No specific NSUN3 gene panel or GTR-listed clinical test was identified as a named commercial product in this search; it would typically be captured within broader "mitochondrial disease" or "inherited optic neuropathy" NGS panels

**Differential diagnosis:** Leber hereditary optic neuropathy (LHON, mtDNA-encoded), autosomal dominant optic atrophy (*OPA1*), other combined OXPHOS deficiency genes (particularly other mt-tRNA-modification enzymes such as *TRMT5*, *MTO1*, *TRIT1*, or aminoacyl-tRNA synthetases), and other causes of infantile lactic acidosis with developmental delay.

**Screening:** No newborn screening, carrier screening, or population screening program exists for this ultra-rare gene; not part of any standard expanded carrier screening panel identified in this search.

---

## 11. Outcome/Prognosis

No survival curves, formal mortality statistics, or standardized quality-of-life measures have been published — the entire evidence base is descriptive case-report follow-up. Qualitatively:
- Patients with the **milder, isolated optic atrophy phenotype** (adolescent/adult onset, missense hypomorphic alleles) are reported alive and functioning into their third-to-fourth decade, with visual impairment as the dominant but not life-limiting morbidity.
- Patients with the **severe, early-onset multisystem phenotype** show substantial morbidity (refractory seizures, developmental delay, multisystem involvement); the 2025 report notes one individual with "possible limited life expectancy" in its abstract summary, though no explicit mortality outcome/age-at-death is detailed in the extracted text for any reported patient — this should be treated as a qualitative severity signal, not a quantified prognosis statistic, when curating.
- **Complications** in severe cases include drug-refractory epilepsy, growth failure, endocrinopathy, structural cardiac disease, and infection-triggered acute metabolic/neurological decompensation.
- **Prognostic factors:** genotype (LOF vs. hypomorphic missense) is the strongest prognostic correlate identified; there is no established prognostic biomarker beyond variant classification itself.

---

## 12. Treatment

No disease-specific, FDA-approved, or gene-targeted therapy exists for COXPD48/NSUN3 deficiency. Management is supportive, following general mitochondrial-disease principles, with one notable specific finding:

- **Idebenone** (a synthetic short-chain quinone/CoQ10 analog, CHEBI:5991; NCIT treatment terms would map to Pharmacotherapy NCIT:C15986 with `therapeutic_agent` idebenone) was used in one patient (Jurkute Family 3, III-2) with an acute LHON-like presentation and was **temporally associated with visual acuity restoration from 6/120 to 6/6 bilaterally over 4 months**, alongside spontaneous-recovery confounding (the paper reports "spontaneous improvement beginning at 12 months" and idebenone was given during this window) — this should be curated as a **single anecdotal treatment-response observation**, not established efficacy evidence, given the absence of a controlled trial and the confound of concurrent spontaneous recovery. Idebenone is notably the only medication with regulatory approval (EU) specifically for a mitochondrial optic neuropathy (LHON), lending biological plausibility to its use here by extension.
- **Anticonvulsant therapy:** levetiracetam was used for seizure control in one severe case but described as only partially effective ("refractory," seizures recurring approximately every 6 months) — NCIT:C15986 Pharmacotherapy / therapeutic_agent levetiracetam (CHEBI:6437).
- **Supportive care:** management of failure to thrive/nutritional support (NCIT:C15447 Dietary Intervention), physical/occupational/speech therapy for developmental delay and hypotonia (NCIT:C15302 Physical Therapy), low-vision rehabilitation and optical aids for the optic atrophy component, endocrine replacement (growth hormone) where deficiency is documented, and standard cardiology follow-up for structural cardiac anomalies.
- **General mitochondrial-disease supportive measures** (CoQ10/ubiquinone supplementation, B-vitamin cocktails, avoidance of mitochondrial-toxic drugs, aggressive treatment of intercurrent infection to avoid metabolic decompensation) are standard-of-care extrapolations from broader mitochondrial disease management guidelines rather than NSUN3-specific evidence.
- **No gene therapy, RNA-based therapy, or clinical trial** specific to NSUN3/COXPD48 was identified in ClinicalTrials.gov searches performed in this session; none should be assumed to exist without direct verification at curation time.

---

## 13. Prevention

No primary prevention exists beyond **genetic counseling and reproductive options** for families with a known biallelic *NSUN3* genotype: carrier testing of at-risk relatives, prenatal diagnosis, and preimplantation genetic diagnosis are the standard options for any confirmed AR mitochondrial-translation disorder, though no report of their specific use for NSUN3 disease was found in this search. Given the phenotypic overlap with LHON-like presentations, **avoidance of putative mitochondrial-toxic exposures** (tobacco smoke, excess alcohol — the classic environmental modifiers invoked in LHON management, though not specifically studied for NSUN3 disease) would be a reasonable extrapolated counseling point, but this is an inference from the broader mitochondrial-optic-neuropathy literature, not direct NSUN3 evidence, and should be labeled as such. No newborn screening or population carrier-screening program exists for this gene.

---

## 14. Other Species / Natural Disease

No naturally occurring NSUN3-associated disease has been reported in any non-human species (companion animals, livestock, or wildlife); no OMIA entry was identified. NSUN3 orthologs are broadly conserved across vertebrates (essential mitochondrial housekeeping function), consistent with mouse ortholog *Nsun3* (MGI:2146565) being required for embryonic viability (see below), but no spontaneous veterinary disease phenotype has been documented.

---

## 15. Model Organisms

**Mouse (*Mus musculus*, NCBITaxon:10090):** The only reported animal model.
- **Whole-body constitutive knockout:** Homozygous *Nsun3*-null mice are **embryonic lethal**, with embryos becoming progressively smaller and dying between **E10.5 and E12.5** (Murakami et al., *Commun Biol* 2023, PMID:36949224). This establishes an essential, non-redundant developmental requirement for NSUN3-dependent mt-tRNA modification that human patients — all carrying at least partially hypomorphic genotypes — do not display, an important **species-discordance caveat**: the complete-null mouse phenotype (embryonic lethality) has no directly comparable human counterpart, since no reported human patient carries a fully null biallelic genotype that survived to term; this gap should be modeled as a `HUMAN_MODEL_MISMATCH`-type consideration if curated into a `modeled_mechanisms` link, given that fidelity to the "severe end" of human phenotype is unclear (the mouse model recapitulates lethality of complete loss but cannot inform the milder end of the human spectrum, which arises from partial loss-of-function alleles the constitutive-null model does not model).
- **Conditional, heart-specific knockout (*Nsun3*^HKO, using a cardiac-specific Cre driver):** Viable to adulthood, permitting study of postnatal/adult consequences:
  - Enlarged, structurally abnormal cardiac mitochondria with **fragmented cristae** (1.5× larger at 14 weeks, 1.7× larger at 50 weeks vs. controls)
  - **Enhanced heart contraction** and mild, age-associated cardiac hypertrophy (increased left ventricular wall thickness during systole in older animals)
  - Mitochondrial mRNAs encoding respiratory subunits were **not transcriptionally downregulated**, but **enzymatic activity of the respiratory complexes was reduced**, especially Complex IV, with additional Complex I decline in older animals — directly paralleling the human muscle-biopsy finding of post-transcriptional (translational) rather than transcriptional OXPHOS impairment, and supporting **high fidelity of this tissue-specific model to the underlying translational mechanism**, though not to the optic-nerve phenotype (no eye/optic-nerve-specific conditional model has been reported).
- **Applications:** The heart-specific model is well suited to studying the cellular/mitochondrial-structural and bioenergetic consequences of NSUN3 loss in a postnatally viable tissue; no optic-nerve/retinal-ganglion-cell-specific conditional model has yet been generated, which is a notable gap given that the optic nerve is the most consistently affected human tissue.
- **Cellular models:** Patient-derived dermal fibroblasts (multiple studies) are the principal human cellular model, used for immunocytochemistry (COX I staining), Western blot (COX II, NDUFB8), Seahorse mitochondrial stress test respirometry, and mt-tRNA methylation quantification — these functional/omics assays in patient fibroblasts, rather than any animal disease model, currently provide the most direct mechanistic validation of pathogenicity for novel NSUN3 variants.
- **Resources:** MGI:2146565 (*Nsun3* mouse gene record); no IMPC/KOMP standardized knockout-mouse phenotyping data specific to constitutive *Nsun3* knockout beyond the Murakami et al. study was identified in this search (the constitutive knockout is embryonic lethal, so it would not appear in adult IMPC phenotyping pipelines in any case).

---

## Summary of Suggested Ontology Term Bindings

| Concept | Suggested term |
|---|---|
| Disease | MONDO:0033566 (COXPD48); OMIM:619012 |
| Gene | hgnc:26208 (NSUN3) |
| Optic atrophy | HP:0000648 |
| Nystagmus | HP:0000639 |
| Cataract | HP:0010696 |
| Global developmental delay | HP:0001263 |
| Microcephaly | HP:0000252 |
| Muscular hypotonia | HP:0001252 |
| External ophthalmoplegia | HP:0000544 |
| Seizures | HP:0001250 |
| Elevated lactate | HP:0002151 |
| Failure to thrive | HP:0001508 |
| Sensorineural hearing loss | HP:0000407 |
| Peripheral axonal neuropathy | HP:0007002 |
| Mitochondrial translation | GO:0032543 |
| Mitochondrial tRNA methylation | GO:0070901 |
| Mitochondrion / matrix | GO:0005739 / GO:0005759 |
| Retinal ganglion cell | CL:0000740 |
| Skeletal muscle fiber | CL:0000188 |
| Cardiomyocyte | CL:0000746 |
| Optic nerve | UBERON:0001780 |
| Eye | UBERON:0000970 |
| Idebenone | CHEBI:5991 |
| Levetiracetam | CHEBI:6437 |
| Pharmacotherapy (treatment action) | NCIT:C15986 |

---

## Key Gaps for Curation

1. **No formal prevalence/incidence data** — likely severely underascertained given the milder phenotype's overlap with idiopathic optic atrophy.
2. **No controlled treatment-efficacy evidence** — the idebenone observation is a single confounded case.
3. **No mortality/survival statistics**, only qualitative severity descriptions.
4. **Species discordance** between the embryonic-lethal complete mouse knockout and the (partial-loss-of-function-only) surviving human genotypes — flag explicitly if modeling this as a `modeled_mechanisms` link.
5. **Variable variant classification** — several reported NSUN3 alleles remain VUS; do not treat every published variant as unambiguously pathogenic without independent ClinVar/ACMG verification at curation time.
6. gnomAD constraint metrics (pLI/LOEUF) for NSUN3 were not retrievable in this session and should be pulled directly from gnomAD before citing numerically.

**Sources:**
- [OMIM #619012 — COMBINED OXIDATIVE PHOSPHORYLATION DEFICIENCY 48; COXPD48](https://omim.org/entry/619012)
- [OMIM *617491 — NSUN3](https://omim.org/entry/617491)
- [Van Haute L, et al. Deficient methylation and formylation of mt-tRNA^Met wobble cytosine in a patient carrying mutations in NSUN3. Nat Commun. 2016. PMID:27356879](https://pmc.ncbi.nlm.nih.gov/articles/PMC4931328/)
- [Nakano S, et al. NSUN3 and ABH1 modify the wobble position of mt-tRNA^Met to expand codon recognition in mitochondrial translation. EMBO J. 2016. PMID:27497299](https://pubmed.ncbi.nlm.nih.gov/27497299/)
- [Paramasivam A, et al. Novel Biallelic NSUN3 Variants Cause Early-Onset Mitochondrial Encephalomyopathy and Seizures. J Mol Neurosci. 2020. PMID:32488845](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7658056/)
- [Mutations in NSUN3, a Mitochondrial Methyl Transferase Gene, Cause Inherited Optic Neuropathy. PMID:38790159](https://pmc.ncbi.nlm.nih.gov/articles/PMC11121614/)
- [Jurkute N, et al. Biallelic NSUN3 Variants Cause Diverse Phenotypic Spectrum Disease: From Isolated Optic Atrophy to Severe Early-Onset Mitochondrial Disorder. Invest Ophthalmol Vis Sci. 2025;66(6):17. PMID:40465263](https://pmc.ncbi.nlm.nih.gov/articles/PMC12147050/)
- [Murakami Y, et al. NSUN3-mediated mitochondrial tRNA 5-formylcytidine modification is essential for embryonic development and respiratory complexes in mice. Commun Biol. 2023. PMID:36949224](https://pmc.ncbi.nlm.nih.gov/articles/PMC10033821/)
- [MGI:2146565 — Nsun3 mouse gene detail](https://www.informatics.jax.org/marker/MGI:2146565)
- [NSUN3 — GeneCards](https://www.genecards.org/card/NSUN3)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 27 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003128` (1 mention) - the report calls it "present across essentially all early-onset cases; a hallmark biochemical abnormality"; HP calls it **Lactic acidosis**
- `CHEBI:5991` (2 mentions) - the report calls it "Idebenone"; CHEBI calls it **CHEBI_5991**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CHEBI:5991` (CHEBI_5991) (2 mentions) - replaced by `CHEBI:28638`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010696` (2 mentions) - the report calls it "Cataract"; HP calls it **Polar cataract**
- `HP:0000551` (1 mention) - the report calls it "Impaired color vision"; HP calls it **Color vision defect**, and lists "Disturbed color vision" among its other names
- `HP:0001252` (2 mentions) - the report calls it "Muscular hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names
- `HP:0007002` (2 mentions) - the report calls it "Peripheral axonal neuropathy"; HP calls it **Motor axonal neuropathy**
- `HP:0002151` (2 mentions) - the report calls it "Elevated lactate"; HP calls it **Increased circulating lactate concentration**, and lists "Increased serum lactate" among its other names
- `CL:0000740` (3 mentions) - the report calls it "Retinal ganglion cells and optic nerve axons", "Retinal ganglion cell"; CL calls it **retinal ganglion cell**
- `CL:0000188` (3 mentions) - the report calls it "Skeletal muscle fiber"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0001780` (2 mentions) - the report calls it "Optic nerve"; UBERON calls it **spinal nerve**, and lists "spine nerve" among its other names
- `CL:0000746` (2 mentions) - the report calls it "Cardiomyocytes", "Cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `NCIT:C15986` (3 mentions) - the report calls it "Pharmacotherapy (treatment action)"; NCIT calls it **Pharmacotherapy**, and lists "Pharmacological Treatment" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0032543` - called "mitochondrial translation", "Mitochondrial translation"
- `CL:0000740` - called "Retinal ganglion cells and optic nerve axons", "Retinal ganglion cell"
- `CL:0000746` - called "Cardiomyocytes", "Cardiomyocyte"
- `MGI:2146565` - called "Nsun3", "Nsun3* mouse gene record", "Nsun3 mouse gene detail"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `OMIM`.