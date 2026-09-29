---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-27T05:54:21.697762'
end_time: '2026-09-27T06:00:00.322221'
duration_seconds: 338.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 5B
  mondo_id: MONDO:0013933
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
  num_turns: 36
  total_cost_usd: 1.8143006000000002
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 24
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 11
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 48
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 14
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0001846
    reported_labels:
    - inner ear structures, for sensorineural hearing loss
    ontology_label: internal ear
  labels_variant: 7
  unresolvable_prefixes:
  - ORPHA
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 5B
- **MONDO ID:** MONDO:0013933 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 5B** covering all of the
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

Confirmed directly against the HGNC REST API: HGNC:9717. Now I have sufficient verified material to write the full report.

---

# Peroxisome Biogenesis Disorder 5B (PBD5B) — Research Report

**Note on sourcing:** Web access to OMIM.org and PubMed's own pages was blocked by their bot-detection layers throughout this session (HTTP 403 / reCAPTCHA walls); the OMIM and PubMed content below was recovered via Europe PMC's REST API, HGNC's REST API, and web-search snippets rather than direct page reads. Where a claim rests only on a search-engine summary rather than a directly fetched primary source, that is noted. All PMIDs, the OMIM numbers, and the HGNC ID (verified directly against `rest.genenames.org`) should be independently re-verified against primary sources before being written into a curated KB record.

## 1. Disease Information

**Overview.** Peroxisome Biogenesis Disorder 5B (PBD5B) is the milder, non-lethal end of the phenotypic spectrum caused by biallelic pathogenic variants in **PEX2** (chromosome 8q21.13; formerly *PXMP3*). PEX2 disease is nosologically split by OMIM into two severity-linked phenotype entries that share one gene: **PBD5A (Zellweger syndrome)**, OMIM #614866, the classic lethal-in-infancy form, and **PBD5B**, OMIM #614867, corresponding to the milder neonatal adrenoleukodystrophy (NALD) / infantile Refsum disease (IRD) end of the Zellweger spectrum. Both are members of the broader **Zellweger Spectrum Disorders (ZSD)** / peroxisome biogenesis disorder (PBD) group, a set of ~13 genetically distinct but phenotypically overlapping autosomal recessive conditions in which peroxisomes fail to assemble or fail to import their matrix enzymes, producing combined loss of peroxisomal β-oxidation, α-oxidation, plasmalogen synthesis, and bile-acid synthesis capacity ([Klouwer et al. 2015, *Orphanet J Rare Dis*, PMID:26627182](https://pubmed.ncbi.nlm.nih.gov/26627182); GeneReviews *Zellweger Spectrum Disorder*, NBK1448).

**Key identifiers:**
- **MONDO:** MONDO:0013933
- **OMIM (phenotype):** #614867 (PBD5B); allelic to #614866 (PBD5A / Zellweger syndrome, same gene)
- **OMIM (gene):** *170993 (PEX2, formerly PXMP3)
- **HGNC:** HGNC:9717 (symbol PEX2; Entrez Gene 5828; Ensembl ENSG00000164751) — verified directly via HGNC REST API
- **Orphanet:** the umbrella "Peroxisome biogenesis disorder, Zellweger syndrome spectrum" entry is ORPHA:79189 (this search did not surface a PEX2-specific or PBD5B-specific ORPHA subcode distinct from the umbrella ZSD entry; this should be confirmed directly on orphadata rather than assumed absent)
- **Complementation group:** historically CG5 (equivalent to CG10 / CGF in older nomenclature)

**Synonyms:** Zellweger spectrum disorder, PEX2-related; Neonatal adrenoleukodystrophy (NALD), PEX2-related; Infantile Refsum disease (IRD), PEX2-related; peroxisome biogenesis disorder, complementation group 10 (CG10); peroxisome biogenesis disorder, complementation group F (CGF).

**Source type:** This report draws on aggregated disease-level resources (OMIM, GeneReviews, Orphanet-derived review literature) plus a small number of individual-patient case reports/case series (Mignarri et al. 2012, PMID:23430938; Gootjes et al. 2004, PMID:14630978) — the PEX2 literature is dominated by single- or small-N case reports rather than large cohort studies, which is itself informative about disease rarity.

## 2. Etiology

**Causal factor:** Purely monogenic/genetic. Biallelic (homozygous or compound heterozygous) loss-of-function or partial-loss-of-function variants in *PEX2* impair the PEX2–PEX10–PEX12 peroxisomal membrane retrotranslocation/ubiquitin-ligase complex, degrading peroxisomal matrix protein import. There is no known environmental, infectious, or purely mechanistic (non-genetic) causal contribution — this is a pure inborn error of organelle biogenesis.

**Genetic risk factors / genotype-severity correlation.** PBD5A vs. PBD5B is not a different gene but a different *allelic severity* at the same locus:
- **Gootjes et al. 2004** (PMID:14630978, *Pediatric Research*) sequenced four unrelated PBD patients and found four PEX2 mutations (three novel). Two patients were homozygous for mutations producing severely truncated protein (severe phenotype); of the two patients with mutations in the RING zinc-binding domain, "the patient lacking the domain had a mild phenotype, whereas the C247R patient had a severe phenotype" — i.e., a missense change within the zinc-binding RING domain can be *more* deleterious than complete loss of that domain, an unintuitive genotype–phenotype relationship attributed to residual partial function versus a poisoned/misfolded domain.
- **Mignarri et al. 2012** (PMID:23430938, *JIMD Reports*) reported a 51-year-old man with two heterozygous PEX2 mutations and an unusually mild, adult-onset, slowly progressive cerebellar ataxia phenotype with normal cognition — markedly milder than any previously reported PEX2 patient, extending the clinical spectrum toward an ataxia-predominant presentation.
- **Gomez et al. 2025** (PMID:40621817, *Disease Models & Mechanisms*) used humanized *Drosophila* PEX2/PEX16 lines to functionally test patient variants across the severity spectrum and found that "some missense mutations exhibit[ed] severity comparable to truncations," that alleles associated with the mild PBD phenotype showed partial rescue of peroxisome function, and that variants linked to an *atypical ataxia* phenotype could fully rescue function in the fly assay — direct functional evidence that PEX2 variant residual activity is a continuous, allele-specific determinant of clinical severity rather than a simple null/non-null dichotomy.

**Environmental/lifestyle risk factors:** None identified; this is not modifiable by exposure, diet, or lifestyle prior to onset.

**Protective factors:** None specific to PEX2 have been reported. No modifier genes or protective alleles are described in the literature surveyed.

**Gene-environment interaction:** Not applicable — no interaction with environmental exposure has been described for this monogenic organelle-biogenesis disorder.

**Inheritance:** Autosomal recessive (both PBD5A and PBD5B).

## 3. Phenotypes

PBD5B corresponds to the attenuated end of Zellweger spectrum, overlapping the classically named NALD and IRD phenotypes and, per the Mignarri report, extending to an adult-onset ataxia-predominant presentation. Phenotype detail below is drawn from the ZSD literature broadly (Klouwer et al. 2015, PMID:26627182) and the PEX2-specific case reports, since PEX2 is one of the rarer causal genes and PEX2-specific frequency data by phenotype are sparse.

**Neurological:**
- Developmental delay / intellectual disability — variable; the Mignarri patient had *normal cognition* at age 51, demonstrating this is not obligate in mild PBD5B (HP:0001263 Developmental delay / HP:0001249 Intellectual disability — as absent findings in the mildest reported case)
- Hypotonia — present to variable degree across the spectrum, milder in PBD5B than PBD5A (HP:0001252 Hypotonia)
- Cerebellar ataxia, progressive, childhood-onset, slowly progressive over decades — the defining feature of the Mignarri case (HP:0001251 Ataxia)
- Areflexia (HP:0001284 Areflexia)
- Axonal sensorimotor polyneuropathy, severe (HP:0007141 or HP:0003477-type peripheral neuropathy terms — specific HPO ID to be confirmed at curation time)
- Cerebellar atrophy on MRI, without white-matter involvement in the mildest case (HP:0001272 Cerebellar atrophy); by contrast, more typical NALD/IRD presentations show progressive leukodystrophy/demyelination (HP:0002415 Leukodystrophy-type terms)
- Nystagmus (HP:0000639) and strabismus (HP:0000486)
- Neuronal migration defect (neocortical dysplasia, polymicrogyria) in the more classic severe end (HP:0002269 Neuronal migration defect) — established mechanistically in the mouse model (below), reported in humans across the ZSD spectrum generally

**Ophthalmologic** (common across ZSD, variably present in PBD5B): retinal dystrophy / retinitis pigmentosa (HP:0000556 Retinal dystrophy), cataracts (HP:0000518), glaucoma (HP:0000501), progressive vision loss — described as "nearly universal" in the broader ZSD literature and a dominant feature of the milder, longer-surviving phenotypes.

**Audiologic:** Sensorineural hearing loss (HP:0000407), progressive, described as "nearly universal" in ZSD and a leading feature (with vision loss) in the milder NALD/IRD forms that patients survive long enough to manifest.

**Hepatic:** Liver dysfunction (HP:0001392 Abnormality of the liver / HP:0001410 Hepatic steatosis-type terms), elevated transaminases, coagulopathy secondary to fat-soluble vitamin K malabsorption — milder and later-onset in PBD5B than in PBD5A/classic Zellweger.

**Renal:** Renal calcium-oxalate stones — reported at "83%" prevalence in a ZSD patient cohort in the Klouwer review (this figure is for ZSD broadly, not PEX2-specific; treat as approximate).

**Endocrine:** Primary adrenal insufficiency — described in the Klouwer review as "common and probably underdiagnosed" across ZSD; annual screening is recommended (see Treatment/Prevention below).

**Skeletal/dental:** Chondrodysplasia punctata (calcific stippling, epiphyseal) in the severe end of the spectrum; enamel hypoplasia reported as near-universal across ZSD.

**Phenotype characteristics:**
- **Onset:** PBD5B spans childhood-onset (the classic NALD/IRD presentations, symptomatic in infancy/childhood) through to the Mignarri case's presentation, whose ataxia had childhood onset but diagnosis was not made until age 51 — illustrating substantial diagnostic delay possible in the mild tail of the spectrum.
- **Severity/progression:** Slowly progressive in the mild PEX2 phenotype; "moderate impairment...seems to affect predominantly neuronal cells in cerebellum" per Mignarri et al. NALD patients may reach their teens; IRD patients may reach adulthood (MalaCards/OMIM-derived summary).
- **Frequency:** No PEX2-specific phenotype-frequency table was located in this search; frequencies quoted above (e.g., the 83% renal stone figure) come from ZSD cohorts pooling multiple causal genes and should not be assumed representative of PEX2 alone without a PEX2-specific cohort study.

**Quality of life:** Not separately quantified for PBD5B/PEX2 in the literature surveyed; broadly, progressive sensorineural hearing loss and retinal dystrophy are the major determinants of functional impact in patients who survive past infancy.

## 4. Genetic / Molecular Information

**Causal gene:** PEX2 (HGNC:9717; chromosome 8q21.13; 4 exons spanning ~17.5 kb; the entire coding sequence lies within a single 1,275-bp exon 4, per [genomic-organization report, PMID:10891359](https://pubmed.ncbi.nlm.nih.gov/10891359/)).

**Pathogenic variant classes reported:**
- Homozygous truncating mutations producing severely truncated protein — associated with severe phenotype (Gootjes et al., PMID:14630978)
- Missense mutations within the C3HC4 zinc-binding RING domain — variable severity depending on exact residue (C247R → severe; a variant causing complete loss of the domain → paradoxically milder, per the same report)
- Compound heterozygous missense combinations — the genotype underlying the Mignarri mild-ataxia adult case (exact variant nomenclature not recovered in this search; should be pulled from the primary paper/ClinVar at curation time)
- The Drosophila humanization study (Gomez et al. 2025, PMID:40621817) functionally tested a panel of patient PEX2/PEX16 missense alleles and found a continuum from truncation-like severity through partial rescue (mild PBD) to full rescue (atypical-ataxia alleles), providing a variant-effect map that could support ACMG functional-evidence codes (PS3/BS3) for specific PEX2 missense variants.

**Allele frequency / population data:** Not specifically retrieved for PEX2 in this search; gnomAD constraint metrics (pLI/LOEUF) for PEX2 were not obtainable via the search tools used in this session and should be pulled directly from the gnomAD browser at curation time rather than asserted here.

**Somatic vs. germline:** Exclusively germline; no somatic PEX2 disease association is known.

**Functional consequence:** Loss-of-function (complete or partial) of a peroxisomal membrane RING-type E3 ubiquitin ligase — see Mechanism section below.

**Modifier genes:** None specifically identified for PEX2/PBD5B in this search.

**Epigenetic information:** No PEX2-specific epigenetic mechanism identified.

**Chromosomal abnormalities:** Not a contiguous-gene/structural-variant disorder; disease arises from sequence-level PEX2 variants, not gross chromosomal rearrangement.

## 5. Environmental Information

No environmental toxin, occupational exposure, lifestyle factor, or infectious agent has been implicated as a cause, trigger, or modifier of PBD5B in the literature surveyed. This is consistent with its being a pure monogenic organelle-biogenesis disorder.

## 6. Mechanism / Pathophysiology

**Causal chain (ordered):**

1. Biallelic pathogenic *PEX2* variants → reduced or absent function of the PEX2 protein, a 35-kDa integral peroxisomal membrane protein with two transmembrane domains and a cytosolically-exposed C3HC4 zinc RING-finger domain (demonstrated structurally; [PMID:10891359](https://pubmed.ncbi.nlm.nih.gov/10891359/); UniProt/Wikipedia-derived domain architecture).
2. PEX2, together with PEX10 and PEX12, normally coassembles into a peroxisomal-membrane **retrotranslocation channel** (an ~10 Å pore) whose cytosolically-positioned RING zinc-fingers monoubiquitinate the PTS1 import receptor **PEX5** at a conserved cysteine (Cys-11), after PEX5 has delivered its PTS1-tagged cargo into the peroxisomal matrix ([Nature 2022 structural paper, PMID/PMC reference PMC9279156](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279156/); this is inferred/established mechanism from a non-disease-specific structural/biochemical study, not a PBD5B clinical paper). Loss of PEX2 RING ligase activity → **leads to** failure of PEX5 monoubiquitination and retrotranslocation.
3. Failure of PEX5 recycling → **results in** depletion of the cytosolic pool of functional PEX5 receptor and, downstream, failure of continued PTS1-mediated (and, secondarily, PTS2-mediated, since PEX5L also escorts PEX7/PTS2 cargo) import of nascent peroxisomal matrix enzymes.
4. Failure of matrix enzyme import → **leads to** combined deficiency of the peroxisomal enzymes for: very-long-chain fatty acid (VLCFA) β-oxidation, phytanic/pristanic acid α/β-oxidation, plasmalogen (ether-phospholipid) biosynthesis, bile-acid side-chain oxidation (C27 → C24 bile acids), and pipecolic acid catabolism.
5. Loss of these enzymatic functions → **results in** the characteristic biochemical signature: elevated plasma VLCFA, phytanic acid, pristanic acid, pipecolic acid, and C27 bile-acid intermediates (THCA/DHCA), together with **decreased** erythrocyte plasmalogens (GeneReviews NBK1448; Klouwer et al. PMID:26627182).
6. Accumulated toxic bile-acid intermediates → **leads to** hepatocyte injury, cholestasis, coagulopathy (via fat-soluble vitamin K malabsorption), and progressive hepatic fibrosis.
7. VLCFA/phytanic-acid accumulation plus loss of plasmalogens (essential myelin lipid components) in the CNS → **leads to** disrupted lipid/cholesterol homeostasis in white matter. The 2026 mouse study (Eberhart et al., PMID:41815956, *Front Mol Neurosci*) directly demonstrates that postnatal *Pex2*-knockout mice develop "severe hypomyelination and dysregulation of cholesterol and fatty acid metabolism in the CNS," with **elevated desmosterol** (a cholesterol-synthesis intermediate) indicating a block distal in the cholesterol synthesis pathway, and altered sphingolipid metabolism accompanying diminished myelination markers — this **results in** the leukodystrophy/demyelination seen on brain MRI in more severe ZSD patients.
8. Independently of (and upstream of, developmentally) the biochemical/myelin axis, loss of peroxisomal function during neurogenesis **leads to** a neuronal migration defect: the original *Pex2*-knockout mouse (Faust & Hatten 1997, PMID:9382874, *J Cell Biol*) showed delayed neuronal migration in the developing cerebral cortex (using a mitotic marker to track precursor cells), abnormal Purkinje cell development with an altered cerebellar folial pattern, malformation of the inferior olivary complex, and extensive neuronal apoptosis — this branch of the causal chain **results in** the neocortical dysplasia/polymicrogyria and cerebellar structural abnormality (in the mild PEX2 human phenotype, manifesting as isolated cerebellar atrophy without migration defect, per Mignarri et al.) seen across the spectrum, with cerebellar/Purkinje-cell vulnerability plausibly explaining why *ataxia* specifically is the presenting feature of the mildest human PEX2 allelic tier.
9. In the retina, disrupted lipid metabolism and loss of peroxisomal function in photoreceptors and RPE → **leads to** progressive retinal dystrophy (mechanism established generally for ZSD via PEX1 mouse-model RPE lipidomic studies referenced in the search results; PEX2-specific retinal mechanistic data were not separately recovered in this session).
10. In the liver specifically, the *Pex2*-knockout mouse also shows **decreased total and HDL cholesterol** in plasma and a 40% reduction of hepatic cholesterol content relative to wild-type (Mol Cell Biol 2004, PMID:14673138) — demonstrating that peroxisomal dysfunction disturbs whole-body cholesterol homeostasis via a mechanism distinct from, and additional to, the bile-acid-intermediate toxicity described in step 6.

**Molecular pathways:** Peroxisomal matrix protein import (PTS1/PTS2 pathway); the PEX2-PEX10-PEX12 RING-finger ubiquitin-ligase retrotranslocation channel; PEX5/PEX7 receptor cycling; downstream, VLCFA β-oxidation, phytanic-acid α-oxidation, plasmalogen (ether-lipid) biosynthesis, and bile-acid synthesis pathways (KEGG/Reactome peroxisome pathway maps).

**Cellular processes:** Protein ubiquitination (monoubiquitination, not degradative polyubiquitination, in this context), organelle (peroxisome) biogenesis, receptor retrotranslocation/recycling, apoptosis (neuronal), pexophagy (PEX2 is also reported as the E3 ligase required for pexophagy during starvation — a second, ubiquitination-dependent but import-independent PEX2 function).

**Protein dysfunction:** Loss-of-function (complete, from truncating alleles) or partial loss-of-function (from RING-domain missense alleles, with a demonstrated non-monotonic severity relationship to domain integrity).

**Suggested GO terms:** GO:0016558 (protein import into peroxisome matrix), GO:0007031 (peroxisome organization), GO:0004842 (ubiquitin-protein transferase/ligase activity), GO:0016558-adjacent PEX5 retrotranslocation process terms, GO:0006635 (fatty acid beta-oxidation), GO:0097009 (energy homeostasis — less specific), GO:0034389 (lipid droplet organization — if relevant to lipidomic phenotype), GO:0034635 (glutathione transport — not relevant here, omit).

**Suggested CL terms:** CL:0000182 (hepatocyte), CL:0000540 (neuron), CL:0000121 (Purkinje cell), CL:0000128 (oligodendrocyte, for the myelination phenotype), CL:0011020 (neural progenitor cell, for the migration-defect mechanism), CL:0000210 (photoreceptor cell, for retinal dystrophy).

**Suggested UBERON terms:** UBERON:0002107 (liver), UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0002113 (kidney), UBERON:0000966 (retina), UBERON:0002369 (adrenal gland), UBERON:0001846 (inner ear structures, for sensorineural hearing loss).

**Molecular profiling / advanced technologies:** No single-cell, spatial-transcriptomic, or multi-omics dataset specific to PBD5B/PEX2 was located in this search. The 2026 mouse hypomyelination paper (PMID:41815956) reports bulk lipidomic (sterol, sphingolipid) profiling of CNS tissue in the *Pex2*-knockout model — this is the most relevant recent molecular-profiling dataset identified.

## 7. Anatomical Structures Affected

- **Primary organs:** Brain (cerebrum, cerebellum), liver, eye (retina, lens), inner ear, adrenal gland, kidney.
- **Secondary/complication-driven:** Skeletal system (epiphyses — chondrodysplasia punctata in severe end), teeth (enamel hypoplasia), coagulation system (secondary to hepatic vitamin K malabsorption).
- **Body systems:** Nervous, hepatic, renal, endocrine, sensory (visual and auditory), skeletal, dental.
- **Tissue/cell level:** Neurons (cortical migrating neurons, Purkinje cells, inferior olivary neurons), oligodendrocytes/myelin, hepatocytes, retinal photoreceptors/RPE, cochlear/vestibular sensory cells, adrenal cortex.
- **Subcellular level (GO Cellular Component):** Peroxisomal membrane (site of PEX2 RING-ligase complex) and peroxisomal matrix (site of enzymatic consequence); secondarily, myelin/white matter lipid compartments and mitochondria are metabolically coupled to peroxisomal lipid handling.
- **Lateralization:** Not applicable — this is a symmetric, systemic metabolic disorder without lateralized findings.

## 8. Temporal Development

- **Onset:** Spans a wide range within PBD5B itself — classic NALD/IRD onset is in infancy/early childhood; the mildest reported PEX2 phenotype (Mignarri et al.) had childhood-onset ataxia not diagnosed until age 51, illustrating that PBD5B onset can be insidious and diagnosis markedly delayed.
- **Progression:** Slowly progressive in the mild tail of the spectrum ("slowly progressive course" — Mignarri et al.); more classically NALD/IRD patients show progressive hearing and vision loss with age, and hepatic/neurologic findings that plateau or worsen depending on individual allele combination.
- **Course pattern:** Chronic and progressive rather than relapsing-remitting or episodic; no described remission.
- **Duration/life expectancy:** NALD patients may reach their teens; IRD patients may reach adulthood; the mildest PEX2 ataxia phenotype is compatible with survival past age 50. This contrasts sharply with the allelic severe form (PBD5A/Zellweger syndrome), where death typically occurs within the first year of life — underscoring that "PBD5B" as a label spans a genotype-defined but clinically broad severity band.
- **Critical periods:** Neuronal migration occurs prenatally, so the migration-defect component of the mechanism (where present) is fixed by birth and not modifiable postnatally; by contrast, the ongoing biochemical toxicity (VLCFA, bile-acid intermediates) and progressive hearing/vision loss represent a postnatal, potentially interventable window, which is the rationale for cholic-acid and DHA supplementation trials (see Treatment).

## 9. Inheritance and Population

- **Epidemiology:** Zellweger spectrum disorders overall have an estimated incidence of about 1 in 50,000 live births in the United States, with regional variation (as high as ~1 in 12,000 in parts of Quebec; as low as ~1 in 500,000 in Japan) (search-engine-derived summary; primary citation not independently confirmed in this session — treat as approximate). A 2025 population-genetics modeling study specifically for **PEX1**-mediated ZSD (the most common causal gene) estimated incidence at roughly 1 in 245,000 (conservative) to 1 in 114,000 (expanded model) births in the US (PMID referenced in search only as "40519747" per search snippet; not independently verified). **No PEX2-specific incidence figure was located in this search** — PEX2 is repeatedly described in the literature as "less common" than PEX1, PEX6, or PEX26 among ZSD-causing genes, consistent with PBD5B being a rare subset of an already rare disease group.
- **Inheritance pattern:** Autosomal recessive.
- **Penetrance:** Presumed complete for biallelic loss-of-function genotypes (based on case-report ascertainment); no explicit incomplete-penetrance data found.
- **Expressivity:** Markedly variable — the central genotype-phenotype finding across the PEX2 literature (Gootjes et al.; Mignarri et al.; the Drosophila functional-severity map) is that expressivity varies continuously with the specific missense/truncating allele combination, from lethal-infantile (PBD5A) through classic NALD/IRD to adult-onset isolated ataxia.
- **Genetic anticipation:** Not described; not expected for this mechanism (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported for PEX2 in this search.
- **Founder effects:** Not identified for PEX2 specifically in this search (contrast with some other PBD genes, e.g., PEX26, which have population-specific founder variants reported in isolated case reports found in this search).
- **Consanguinity:** Homozygous mutations reported in the Gootjes et al. series are consistent with consanguineous or founder-population ascertainment in at least some of the four patients, though this was not explicitly stated in the recovered abstract.
- **Carrier frequency:** Not specifically obtained for PEX2 in this search; should be pulled from gnomAD directly.
- **Population demographics / geographic distribution:** No PEX2-specific ethnic or geographic enrichment was identified in this search.
- **Sex ratio:** No sex-differential reported; autosomal recessive disorders are not expected to show a sex skew (barring ascertainment bias).

## 10. Diagnostics

**Biochemical testing (the primary/first-line diagnostic route, not PEX2-specific but applicable to PBD5B):**
- Plasma VLCFA panel (elevated C26:0, elevated C24:0/C22:0 and C26:0/C22:0 ratios)
- Plasma phytanic acid and pristanic acid (elevated)
- Plasma pipecolic acid (elevated; described as an adjunct rather than primary biomarker)
- Plasma bile-acid intermediates (THCA, DHCA — elevated)
- Erythrocyte plasmalogen levels (reduced)
- (GeneReviews NBK1448, per search-engine-derived summary)

**Genetic testing:** Confirmatory diagnosis requires identification of biallelic pathogenic/likely-pathogenic PEX2 variants by single-gene sequencing, a PEX-gene multi-gene panel, or exome/genome sequencing (GTR test listings exist for PEX2 full-gene sequencing as part of ZSD panels).

**Imaging:** Brain MRI — neocortical dysplasia, decreased/delayed white matter myelination in classic presentations; isolated cerebellar atrophy without white-matter involvement in the mildest reported PEX2 case (Mignarri et al.).

**Other functional testing:** Nerve conduction studies (documented severe axonal sensorimotor polyneuropathy in the Mignarri case); audiometry (sensorineural hearing loss); ophthalmologic exam including electroretinography (retinal dystrophy).

**Newborn screening:** ZSD is **not** currently included in any US state newborn-screening panel as a primary target, but may be incidentally identified via newborn screening for X-linked adrenoleukodystrophy (X-ALD), since both disorders can show elevated VLCFA; this raises the possibility that mild PBD5B cases could be identified presymptomatically via X-ALD NBS follow-up (GeneReviews-derived summary).

**Differential diagnosis:** Other PEX-gene-caused ZSD forms (PEX1, PEX6, PEX10, PEX12, PEX26, etc. — clinically indistinguishable without biochemical/genetic testing); X-linked adrenoleukodystrophy; other autosomal recessive ataxias (relevant specifically for the mild/adult-onset PEX2 presentation, per Mignarri et al.'s explicit recommendation that "genetic screening of PEX2 is warranted in children and adults with otherwise unexplained autosomal recessive ataxia").

**Prenatal diagnosis:** Not specifically detailed for PEX2 in this search, though fetal MRI-based prenatal diagnosis of Zellweger syndrome generally has been reported in the ZSD literature (search snippet reference only).

## 11. Outcome / Prognosis

- **Survival:** Highly allele-dependent. PBD5A (severe/Zellweger) patients typically die within the first year of life. Within PBD5B, NALD patients "may reach their teens," IRD patients "may reach adulthood," and the mildest reported PEX2 genotype (Mignarri et al.) is compatible with survival to at least age 51 with slow neurological progression and normal cognition.
- **Morbidity:** Progressive sensorineural hearing loss and retinal dystrophy/vision loss are the dominant long-term morbidities in patients who survive infancy; hepatic dysfunction and coagulopathy are ongoing management concerns; in the mildest phenotype, progressive ataxia and severe polyneuropathy are the dominant functional morbidities.
- **Complications:** Adrenal insufficiency (probably underdiagnosed), renal calcium-oxalate stones, coagulopathy from fat-soluble vitamin deficiency, dental enamel defects.
- **Prognostic factors:** The single strongest prognostic factor identified across the literature is the specific PEX2 allele combination and its residual protein function (truncating vs. missense; RING-domain-disrupting vs. domain-preserving) — directly demonstrated functionally in the 2025 Drosophila humanization study (PMID:40621817).
- **Quality-of-life tools:** No PEX2- or PBD5B-specific QOL instrument data (EQ-5D, SF-36) were located in this search.

## 12. Treatment

There is **no curative treatment** for PBD5B; management is supportive/symptomatic, per the Klouwer et al. 2015 clinical-management review (PMID:26627182):

- **Endocrine:** Cortisone/hydrocortisone replacement for confirmed adrenal insufficiency (screen annually). Suggested NCIT term: NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` CHEBI hydrocortisone.
- **Neurological:** Standard antiepileptic drugs for seizures where present (NCIT:C15986 Pharmacotherapy).
- **Hematologic:** Vitamin K supplementation for coagulopathy; vitamins A, D, E supplementation for fat-soluble vitamin deficiency (NCIT:C15433 Nutritional Support / specific CHEBI vitamin terms).
- **Bile-acid-directed pharmacotherapy — cholic acid (Cholbam®):** Oral cholic acid inhibits endogenous (toxic C27) bile-acid synthesis via physiologic feedback inhibition on the bile-acid synthesis pathway, and multiple case series/open-label studies (Heubi, Bove & Setchell 2018, PMID:28968290, *J Pediatr Gastroenterol Nutr*; additional long-term case reports identified in search) report it as "efficacious and well tolerated" for reducing hepatotoxic bile-acid intermediates in ZSD, with an FDA-approved indication; a formal post-marketing registry (REPLACE, NCT03115086) and an open-label clinical study (NCT01438411, following an earlier compassionate-use program NCT00007020) have been conducted. Clinical benefit beyond biochemical normalization is still described as incompletely established. Suggested NCIT term: NCIT:C15986 Pharmacotherapy; `therapeutic_agent` CHEBI cholic acid.
- **DHA (docosahexaenoic acid) supplementation:** Randomized controlled trials (search-identified, not individually pulled) raised plasma DHA levels but showed "no improvement of visual function and growth" in ZSD; still used adjunctively in some centers, including combined with cholic acid in infantile Refsum disease (case report, PMID:34664020).
- **Plasmalogen precursor supplementation:** Limited case-report evidence of symptomatic improvement; explicitly "never studied systematically" per the Klouwer review.
- **Dietary:** Phytanic-acid-restricted diet when plasma phytanic acid is markedly elevated (NCIT:C15447 Dietary Intervention).
- **Renal:** Oral citrate and increased fluid intake to prevent calcium-oxalate stone formation/hyperoxaluria.
- **Sensory/supportive:** Hearing aids or cochlear implants (NCIT device/procedure terms per the dismech device-binding convention — action term NCIT:C15329 Surgical Procedure for cochlear implantation, with the device itself as a qualifier); cataract surgery and corrective lenses; gastrostomy tube placement for caloric support (NCIT:C15329 Surgical Procedure); dental follow-up for enamel hypoplasia; physical/occupational therapy for hypotonia and ataxia (NCIT:C15302 Physical Therapy).
- **Investigational/experimental:** Small-molecule compounds intended to stimulate residual peroxisomal biogenesis are under investigation, with the greatest theoretical benefit anticipated for temperature-sensitive or partial-function mutations — a category that plausibly includes some PEX2 missense alleles given the Drosophila functional-rescue data above. In a mechanistically related but gene-distinct 2026 paper, in vivo base editing of the common PEX1-p.G843D allele rescued liver pathophysiology and peroxisome function in a PEX1 mouse model (PMID:41981313) — illustrating a gene-editing therapeutic strategy that is conceptually extensible to a defined recurrent PEX2 allele, though no PEX2-specific gene-editing study was identified in this search.
- **Clinical trials:** A prospective natural-history study of ZSD retinopathy is actively recruiting (NCT06190626, "ZSDvision").

## 13. Prevention

- **Primary prevention:** Not applicable at the population level (no modifiable risk factor); the only primary-prevention lever is reproductive: carrier screening and genetic counseling for at-risk couples (e.g., known familial PEX2 variant, or in a population with an identified founder allele, though none is established for PEX2 specifically per this search).
- **Secondary prevention / screening:** Prenatal diagnosis via biochemical (amniotic fluid VLCFA/plasmalogen) or molecular testing in at-risk pregnancies (a known familial genotype); preimplantation genetic diagnosis is an option once a familial variant is characterized. Postnatally, incidental identification via X-ALD newborn screening (VLCFA-based) is possible but PBD5B is not a primary NBS target anywhere identified in this search.
- **Tertiary prevention:** The annual surveillance protocol described under Diagnostics/Treatment above (adrenal function, seizures, fat-soluble vitamins, coagulation, phytanic acid, hearing, vision) functions as tertiary prevention — catching and treating complications (adrenal crisis, vitamin-K-deficiency bleeding, renal stones) before they cause additional morbidity.
- **Genetic counseling:** Standard autosomal-recessive recurrence-risk counseling (25% recurrence risk per pregnancy for carrier couples); counseling should explicitly discuss the wide expressivity range demonstrated for PEX2 (a family history of a severe PBD5A-affected sibling does not reliably predict the severity of a subsequent affected child if the underlying genotype differs, though a specific known familial genotype narrows this considerably).
- **Public health / immunization / prophylaxis:** Not applicable — no infectious or environmental component to prevent.

## 14. Other Species / Natural Disease

No naturally-occurring PEX2-associated disease in a non-human species (companion animal, livestock, or wildlife) was identified in this search — unlike some other inherited metabolic disorders, no OMIA entry or veterinary case series for PEX2-related peroxisomal disease was found. This appears to be a disorder studied in animals exclusively through engineered (knockout) models rather than through naturally occurring disease.

## 15. Model Organisms

**Mouse (primary model, genetic knockout):**
- **Original *Pex2*-null mouse** (Faust & Hatten 1997, PMID:9382874, *J Cell Biol*): Targeted deletion of *Pex2*. Homozygous-null pups are growth-retarded, severely hypotonic, do not feed, and die 6–24 hours after birth (i.e., this null-allele mouse models the **lethal, severe PBD5A end** of the spectrum, not the milder PBD5B phenotype covered by this report). Demonstrated: delayed neuronal migration in the developing cerebral cortex (tracked via a mitotic marker), abnormal Purkinje cell development with altered cerebellar folial pattern, malformed inferior olivary complex, and extensive neuronal apoptosis. This is the mechanistic basis for classifying Zellweger syndrome as a **neuronal migration disorder**.
- **Cholesterol homeostasis follow-up** (PMID:14673138, *Mol Cell Biol* 2004): the same/related *Pex2*-knockout model shows decreased plasma total and HDL cholesterol, with hepatic cholesterol content reduced ~40% versus wild-type despite normal cholesterol content in most other tissues — demonstrating organ-selective disruption of cholesterol handling.
- **Postnatal survival / hypomyelination model** (Eberhart et al., PMID:41815956, *Front Mol Neurosci*, 2026): a model that survives to the **postnatal** period (details of how postnatal survival was achieved — e.g., a hypomorphic or conditional allele rather than the original perinatal-lethal null — were not fully recovered in this search and should be checked against the primary paper) shows severe hypomyelination, dysregulated CNS cholesterol and fatty-acid metabolism, elevated desmosterol (cholesterol-synthesis-pathway block), altered sphingolipid metabolism, and reduced myelination markers. This model is the closest available rodent proxy for the **surviving, milder PBD5B phenotype** covered by this report, since the original perinatal-lethal null cannot model longer-term neurological progression.

**Drosophila (humanized functional-variant model):**
- Gomez et al. 2025 (PMID:40621817, *Disease Models & Mechanisms*): humanized fly lines expressing human PEX2 or PEX16 patient variants in place of the fly ortholog, used to functionally stratify variant severity (truncation-like vs. partial-rescue "mild PBD" vs. full-rescue "atypical ataxia" alleles). This is explicitly framed by the authors as a scalable platform for genotype-phenotype/variant-classification work across the PEX2 allelic series, directly relevant to interpreting novel PBD5B-associated missense variants (e.g., for ACMG PS3/BS3 functional evidence).

**Phenotype recapitulation and limitations:** The classic *Pex2*-null mouse recapitulates the severe, lethal end of the spectrum (PBD5A) well, including the neuronal migration defect that is a hallmark of human Zellweger syndrome, but by dying within a day of birth it cannot model the *slowly progressive, decades-long* course that defines PBD5B in humans (e.g., the Mignarri case's presentation over 50 years). The newer postnatal-surviving mouse model and the Drosophila variant-rescue platform are the two model systems in the literature best positioned to inform the milder PBD5B phenotype specifically, but neither directly reproduces the human adult-onset isolated-ataxia presentation described by Mignarri et al. No iPSC-derived or organoid model specific to PEX2/PBD5B was identified in this search.

**Databases:** MGI (Mouse Genome Informatics) for the *Pex2* knockout allele records; FlyBase for the Drosophila *Pex2* ortholog (Dmel\Pex2, FBgn0035876) used in the humanization study.

---

Sources:
- [Entry - #614867 - PEROXISOME BIOGENESIS DISORDER 5B; PBD5B - OMIM](https://www.omim.org/entry/614867)
- [Entry - #614866 - PEROXISOME BIOGENESIS DISORDER 5A (ZELLWEGER); PBD5A - OMIM](https://omim.org/entry/614866)
- [Entry - *170993 - PEROXISOME BIOGENESIS FACTOR 2; PEX2 - OMIM](https://omim.org/entry/170993)
- [Peroxisome Biogenesis Disorder 5b - MalaCards](https://www.malacards.org/card/peroxisome_biogenesis_disorder_5b)
- [Curate peroxisome biogenesis disorder 5B (MONDO:0013933) · Issue #12952 · monarch-initiative/dismech](https://github.com/monarch-initiative/dismech/issues/12952)
- [Zellweger Spectrum Disorder - GeneReviews® - NCBI Bookshelf (NBK1448)](https://www.ncbi.nlm.nih.gov/books/NBK1448/)
- [Zellweger spectrum disorders: clinical overview and management approach — Klouwer et al. 2015, PMID:26627182](https://pubmed.ncbi.nlm.nih.gov/26627182) (full text: [PMC4666198](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666198/))
- [Zellweger Spectrum Disorder with Mild Phenotype Caused by PEX2 Gene Mutations — Mignarri et al. 2012, PMID:23430938](https://pubmed.ncbi.nlm.nih.gov/23430938)
- [Novel mutations in the PEX2 gene of four unrelated patients with a peroxisome biogenesis disorder — Gootjes et al. 2004, PMID:14630978](https://pubmed.ncbi.nlm.nih.gov/14630978/)
- [Distinguishing PEX2 and PEX16 gene variant severity for mild, severe and atypical peroxisome biogenesis disorders — Gomez et al. 2025, PMID:40621817](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40621817)
- [Dysregulated lipid metabolism and hypomyelination in postnatal peroxisome-deficient Pex2 knockout Zellweger mice — Eberhart et al. 2026, PMID:41815956](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971716/)
- [Targeted deletion of the PEX2 peroxisome assembly gene in mice provides a model for Zellweger syndrome — Faust & Hatten 1997, PMID:9382874](https://pubmed.ncbi.nlm.nih.gov/9382874/)
- [Disturbed Cholesterol Homeostasis in a Peroxisome-Deficient PEX2 Knockout Mouse Model — PMID:14673138](https://pubmed.ncbi.nlm.nih.gov/14673138)
- [Genomic organization and characterization of human PEX2 encoding a 35-kDa peroxisomal membrane protein — PMID:10891359](https://pubmed.ncbi.nlm.nih.gov/10891359/)
- [A peroxisomal ubiquitin ligase complex forms a retrotranslocation channel — Nature 2022 (PMC9279156)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279156/)
- [Oral Cholic Acid Is Efficacious and Well Tolerated in Patients With Bile Acid Synthesis and Zellweger Spectrum Disorders — Heubi, Bove, Setchell 2018, PMID:28968290](https://pubmed.ncbi.nlm.nih.gov/28968290/)
- [Estimation of PEX1-mediated Zellweger spectrum disorder births and population prevalence by population genetics modeling — 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12166394/)
- [In vivo base editing rescues liver pathophysiology and peroxisome dysfunction in a mouse model of Zellweger spectrum disorder — PMID:41981313](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41981313)
- [HUGO Gene Nomenclature Committee — REST API record for PEX2 (HGNC:9717)](https://rest.genenames.org/fetch/symbol/PEX2)
- [Orphanet: Peroxisome biogenesis disorder (ORPHA:79189)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=79189)
- [Ophthalmic Diagnosis and Novel Management of Infantile Refsum Disease with Combination DHA and Cholic Acid — PMID:34664020](https://pubmed.ncbi.nlm.nih.gov/34664020)
- [ClinicalTrials.gov — REPLACE Registry for Cholbam® (NCT03115086)](https://clinicaltrials.ucsf.edu/trial/NCT03115086)
- [ClinicalTrials.gov — Longitudinal Prospective Natural History Study of Retinopathy in Zellweger Spectrum Disorder (NCT06190626)](https://clinicaltrials.gov/study/NCT06190626)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 22 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001846` (1 mention) - the report calls it "inner ear structures, for sensorineural hearing loss"; UBERON calls it **internal ear**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004842` (1 mention) - the report calls it "ubiquitin-protein transferase/ligase activity"; GO calls it **ubiquitin-protein transferase activity**
- `GO:0097009` (1 mention) - the report calls it "energy homeostasis — less specific"; GO calls it **energy homeostasis**
- `GO:0034389` (1 mention) - the report calls it "lipid droplet organization — if relevant to lipidomic phenotype"; GO calls it **lipid droplet organization**
- `GO:0034635` (1 mention) - the report calls it "glutathione transport — not relevant here, omit"; GO calls it **glutathione transport**
- `CL:0000128` (1 mention) - the report calls it "oligodendrocyte, for the myelination phenotype"; CL calls it **oligodendrocyte**
- `CL:0011020` (1 mention) - the report calls it "neural progenitor cell, for the migration-defect mechanism"; CL calls it **neural progenitor cell**
- `CL:0000210` (1 mention) - the report calls it "photoreceptor cell, for retinal dystrophy"; CL calls it **photoreceptor cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `EXT_ID`.