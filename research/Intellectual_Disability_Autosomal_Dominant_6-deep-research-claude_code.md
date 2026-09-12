---
provider: claude_code
model: claude-fable-5[1m], claude-haiku-4-5-20251001
cached: false
start_time: '2026-09-04T20:39:33.213214'
end_time: '2026-09-04T20:45:12.348792'
duration_seconds: 339.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability, Autosomal Dominant 6
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
  - claude-fable-5[1m]
  - claude-haiku-4-5-20251001
  web_search_requests: 11
  num_turns: 26
  total_cost_usd: 2.942443500000001
  session_id: 2bc9652f-a6e2-402c-84b1-e6ff114deea5
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  - mcp__pubmed__get_article_metadata
  assistant_text_blocks: 8
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
citation_count: 26
reference_validation:
  total_references: 16
  verified: 15
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.062
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:8789948
  unresolved_references:
  - DOI:10.1016/j.ymgme.2023.107673
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15302
    reported_labels:
    - "Developmental/supportive care** \u2014 early-intervention programs, physical\
      \ therapy"
    ontology_label: Physical Therapy
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability, Autosomal Dominant 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability, Autosomal Dominant 6** covering all of the
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

I'll research Intellectual Disability, Autosomal Dominant 6 (MRD6/GRIN2B) using web resources, then produce the full report. First, let me load the web tools.

Now let me run several verification searches in parallel.

OMIM 613970 / GRIN2B / MONDO:0013509 confirmed. Let me load PubMed tools to pull exact abstracts for citations.

PubMed MCP isn't authorized; I'll use the local reference cache and web fetches instead.

The repo's reference cache already holds the two key papers. Let me read them and find other cached GRIN2B references.

Both key abstracts are cached locally. Now let me gather GeneReviews details, mouse-model, ClinGen, incidence, and treatment-trial facts.

One quick local check on the Orphanet and ClinGen cached records for GRIN2B, then I'll write the report.

I have everything I need. Here is the full research report.

---

# Research Report: Intellectual Disability, Autosomal Dominant 6 (MRD6)

**Prepared:** 2026-09-04 · **Category:** Mendelian · **Anchor identifiers verified this session:** OMIM #613970, MONDO:0013509, gene GRIN2B (hgnc:4586)

> **Identifier discipline note:** all ontology CURIEs below marked "(suggest)" are candidate bindings to be re-verified against OLS/OAK before curation; identifiers stated as verified were confirmed against OMIM/ClinGen/MedGen/PubMed records during this research session.

---

## 1. Disease Information

**Overview.** Intellectual Developmental Disorder, Autosomal Dominant 6, with or without seizures (MRD6) is a rare monogenic neurodevelopmental disorder caused by heterozygous, almost always **de novo**, pathogenic variants in **GRIN2B**, which encodes the GluN2B (NR2B/GluRε2) subunit of the N-methyl-D-aspartate (NMDA) glutamate receptor. It is the non-encephalopathic pole of the broader "GRIN2B-related neurodevelopmental disorder" spectrum: mild-to-profound developmental delay/intellectual disability in all affected individuals, with variable epilepsy, autism spectrum disorder/behavioral problems, muscle tone abnormalities, movement disorders, cortical visual impairment, and occasionally malformation of cortical development (GeneReviews NBK501979; PMID:28377535).

**Key identifiers (verified):**

| Resource | ID |
|---|---|
| OMIM (phenotype) | **#613970** — "Intellectual developmental disorder, autosomal dominant 6, with or without seizures; MRD6" |
| OMIM (gene) | 138252 (GRIN2B) |
| MONDO | **MONDO:0013509** — intellectual disability, autosomal dominant 6 |
| MedGen/UMLS | C3151411 |
| GARD | 12851 |
| Allelic OMIM phenotype | #616139 — Developmental and epileptic encephalopathy 27 (DEE27), same gene |
| Orphanet | No dedicated ORPHA code for MRD6; subsumed under autosomal dominant non-syndromic intellectual disability (ORPHA:178469 group); GRIN2B also listed as a gain-of-function gene for Infantile epileptic spasms syndrome (ORPHA:697160, per Orphadata gene table) |
| ICD-10 / ICD-11 | No disease-specific code; coded as disorders of intellectual development (ICD-10 F70–F79; ICD-11 6A00) ± epilepsy codes |

**Synonyms:** MRD6; GRIN2B-related neurodevelopmental disorder (GRIN2B-NDD, lumping term); GRIN2B encephalopathy (used when epilepsy/encephalopathy is prominent); mental retardation, autosomal dominant 6 (legacy); GRIN2B-related syndrome.

**Data provenance.** Knowledge is derived from aggregated case series and disease-level resources (OMIM, GeneReviews, ClinVar/ClinGen, the CFERV/GRIN variant registries), not population EHR data. The largest phenotype series remains Platzer et al. 2017 (n=86 pathogenic/likely pathogenic de novo variant carriers; PMID:28377535).

## 2. Etiology

**Causal factor.** Purely genetic: heterozygous pathogenic variants in GRIN2B (missense clustering in transmembrane and ligand-binding domains, truncating/frameshift, splice-site variants, and whole-gene or exonic deletions). Endele et al. first established causation by finding GRIN2B disrupted by translocation breakpoints and then four de novo mutations (a frameshift, a missense, two splice-site) on sequencing 468 individuals with intellectual disability: *"Sequencing of GRIN2B in 468 individuals with mental retardation revealed four de novo mutations: a frameshift, a missense and two splice-site mutations."* (PMID:20890276, Nat Genet 2010).

**Genetic risk factors.** The only established risk factor is the de novo variant itself; there are no known susceptibility loci or modifier genes for MRD6. Advanced paternal age raises de novo SNV rates generically (inference from de novo mutation biology, not demonstrated for GRIN2B specifically). ClinGen has curated GRIN2B dosage sensitivity with a **haploinsufficiency score of 3 (sufficient evidence)** for intellectual disability, autosomal dominant 6 (ClinGen gene-dosage HGNC:4586).

**Environmental risk/protective factors.** None known; no gene–environment interactions are documented (CTD lists no curated GRIN2B chemical–disease interactions specific to MRD6). Environmental modulation of outcome is limited to non-specific factors (access to early intervention, seizure control).

**Protective genetic factors.** None described.

## 3. Phenotypes

Frequencies below are from the GeneReviews GRIN2B-NDD chapter (NBK501979, Platzer & Lemke) drawing on the 86-patient Platzer 2017 cohort (PMID:28377535).

| Phenotype | Frequency | Onset | Severity/course | Suggested HP term |
|---|---|---|---|---|
| Developmental delay / intellectual disability | **100%** (mild ~15%, severe–profound ~61%) | infancy | stable, non-degenerative; regression rare (~7%) | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability (suggest) |
| Muscular hypotonia | ~56% (15% of these tube-fed) | neonatal/infantile | often persistent | HP:0001252 Hypotonia (suggest) |
| Epilepsy (various types incl. infantile spasms, focal, generalized) | ~51% | birth–9 y | ~half drug-resistant | HP:0001250 Seizure; HP:0012469 Infantile spasms (suggest) |
| Autism spectrum disorder / behavioral abnormalities | ~26% | early childhood | chronic | HP:0000717 Autism; HP:0000708 Abnormal behavior (suggest) |
| Spasticity | ~23% (only in severe ID) | childhood | chronic | HP:0001257 Spasticity (suggest) |
| Microcephaly | ~18% (severe ID only) | congenital/postnatal | stable | HP:0000252 Microcephaly (suggest) |
| Malformation of cortical development (polymicrogyria-like, intermediate with tubulinopathy pattern) | ~13% (6/48 in Platzer series) | congenital | structural | HP:0002126 Polymicrogyria (suggest) |
| Movement disorder (dystonic, dyskinetic, choreiform) | ~10% | infancy/childhood | chronic | HP:0001332 Dystonia; HP:0002072 Chorea (suggest) |
| Cortical visual impairment | ~8% | infancy | chronic | HP:0100704 Cerebral visual impairment (suggest) |
| Feeding difficulties | subset of hypotonic patients | neonatal | may need gastrostomy | HP:0011968 Feeding difficulties (suggest) |
| Macrocephaly (12p13 deletion cases) | occasional | infancy | — | HP:0000256 Macrocephaly (suggest); PMID:27656287 |

Platzer abstract (verbatim, quotable): *"Patients presented with neurodevelopmental disorders and a spectrum of hypotonia, movement disorder, cortical visual impairment, cerebral volume loss and epilepsy."* (PMID:28377535).

**Quality of life impact.** Dominated by ID severity, drug-resistant epilepsy, non-verbal status (many severe cases have absent speech — HP:0001344, suggest), feeding dependence, and caregiver burden; no disease-specific EQ-5D/PROMIS studies exist (gap).

## 4. Genetic/Molecular Information

- **Causal gene:** GRIN2B (hgnc:4586; OMIM 138252), chromosome **12p13.1**, encoding GluN2B, one of the glutamate-binding NR2 subunits of the heterotetrameric NMDA receptor (2×GluN1 + 2×GluN2) (PMID:20890276).
- **Variant spectrum:** ~95% detectable by sequence analysis (missense, nonsense, frameshift, splice); ~5% exon/whole-gene deletions detectable by del/dup analysis or CMA (GeneReviews NBK501979). Missense variants **cluster in transmembrane segments and ligand-binding (agonist-binding) domains** (PMID:28377535). 12p13 deletions encompassing GRIN2B cause DD with macrocephaly (PMID:27656287).
- **Origin:** de novo germline in essentially all molecularly confirmed probands; somatic variants are not a recognized mechanism.
- **Functional consequence classes:** both **loss-of-function** (reduced surface expression, reduced agonist potency, reduced open probability, haploinsufficiency from truncation/deletion) and **gain-of-function** (increased glutamate/glycine potency, reduced voltage-dependent Mg²⁺ block, prolonged deactivation): *"Functional consequences of variants were diverse, revealing various potential gain-of-function and loss-of-function mechanisms and a retained sensitivity to the use-dependent blocker memantine."* (PMID:28377535). CFERV (Emory) maintains functional annotations per variant (PMID:27818011).
- **Population frequency:** pathogenic variants are absent from population databases; GRIN2B is among the most missense- and LoF-constrained genes in gnomAD (pLI ≈ 1) — consistent with dominant de novo disease (constraint claim: standard gnomAD observation; verify current v4 values before curation).
- **Modifier genes / epigenetics:** none established. No disease-defining methylation episignature reported.
- **Chromosomal abnormalities:** translocations disrupting GRIN2B were the original discovery route (PMID:20890276); 12p13.1 microdeletions are a recurrent mechanism (DECIPHER; PMID:27656287).

## 5. Environmental Information

Not applicable as etiology: no toxins, lifestyle factors, or infectious agents cause or trigger MRD6. Fever/illness may transiently worsen seizures as in other developmental epilepsies (generic inference, not GRIN2B-specific evidence).

## 6. Mechanism / Pathophysiology

**Causal chain (numbered; branch points marked):**

1. A de novo heterozygous GRIN2B variant (missense in TMD/ligand-binding domain, truncating/splice variant, or gene deletion) **leads to** an altered or absent GluN2B protein (PMID:20890276; PMID:28377535).
2. Altered GluN2B **results in** abnormal GluN2B-containing NMDA receptor function — **branch A (loss of function):** reduced receptor surface expression, agonist potency, or channel open probability, or pure haploinsufficiency; **branch B (gain of function):** increased agonist potency, reduced Mg²⁺ block, and/or prolonged channel activation (PMID:28377535; PMID:27818011).
3. Because GluN2B is the predominant NR2 subunit of prenatal and early postnatal forebrain (before the developmental GluN2B→GluN2A switch), either branch **disrupts** NMDAR-mediated Ca²⁺ influx and downstream signaling at developing glutamatergic synapses (PMID:20890276 — *"disturbances in the neuronal electrophysiological balance during development result in variable neurological phenotypes"*; review DOI:10.3389/fnsyn.2022.1090865).
4. Dysregulated NMDAR signaling **impairs** neuronal differentiation, dendrite morphogenesis, synaptogenesis, and synaptic plasticity (LTP/LTD): *"disease-associated GluN2B variants interfere with neuronal differentiation, dendrite morphogenesis, synaptogenesis, and synaptic plasticity"* (Sabo et al., Front Synaptic Neurosci 2023, DOI:10.3389/fnsyn.2022.1090865; largely in vitro/model-organism evidence — an **inferred** step in humans).
5. In a subset, disturbed NMDAR-dependent neuronal migration during corticogenesis **produces** malformation of cortical development (polymicrogyria-like MCD intermediate with tubulinopathies) (PMID:28377535; mechanism inferred).
6. Synaptic/network dysfunction **manifests as** excitatory–inhibitory imbalance **leading to** the clinical phenotypes — DD/ID universally; epilepsy (enriched in gain-of-function; Orphadata annotates the IESS association specifically as gain-of-function, ORPHA:697160 gene table); ASD/behavioral phenotypes; hypotonia/movement disorder; cortical visual impairment.

**Ontology anchors (suggest, verify before binding):** GO:0004972 NMDA glutamate receptor activity; GO:0035235 ionotropic glutamate receptor signaling pathway; GO:0007268 chemical synaptic transmission; GO:0060291 long-term synaptic potentiation; GO:0060292 long-term synaptic depression; GO:0048813 dendrite morphogenesis; GO:0007416 synapse assembly; GO:0070588 calcium ion transmembrane transport; GO:0014069 postsynaptic density; GO:0017146 NMDA selective glutamate receptor complex; GO:0098978 glutamatergic synapse. Cell types: CL:0000679 glutamatergic neuron; CL:0000598 pyramidal neuron; CL:0000617 GABAergic neuron (interneuron migration/maturation involvement is hypothesized).

**Molecular profiling.** No human patient transcriptomic/proteomic/metabolomic signature is established (gap). Model-system profiling exists in mouse/rat haploinsufficiency models (e.g., absence seizures and sleep abnormalities in a Grin2b⁺/⁻ rat, bioRxiv 2024 preprint DOI:10.1101/2024.02.27.582289 — preprint, weight accordingly).

## 7. Anatomical Structures Affected

- **Primary organ:** brain (UBERON:0000955, suggest), especially cerebral cortex (UBERON:0000956) and hippocampal formation (UBERON:0002421); cerebral volume loss and MCD on MRI (PMID:28377535).
- **Systems:** nervous system primarily; secondary musculoskeletal (tone, spasticity-related contractures), visual (cortical visual impairment — the lesion is cortical, eyes structurally normal), gastrointestinal/feeding (hypotonia-related).
- **Tissue/cell level:** glutamatergic synapses of cortical and hippocampal excitatory neurons; developing neurons broadly (GluN2B expression is pan-forebrain prenatally).
- **Subcellular:** postsynaptic membrane/postsynaptic density of dendritic spines (GO:0014069, suggest); receptor also signals extrasynaptically.
- **Lateralization:** bilateral; MCD when present is typically bilateral (PMID:28377535).

## 8. Temporal Development

- **Onset:** congenital/infantile. Developmental delay evident in the first year; hypotonia often neonatal; epilepsy onset birth–9 years (GeneReviews NBK501979).
- **Course:** chronic, lifelong, generally **non-progressive** with respect to cognition (static encephalopathy); developmental regression uncommon (~7%). Epilepsy course variable; roughly half of epileptic patients are drug-resistant.
- **Critical periods:** the disorder acts during the prenatal/early-postnatal window when GluN2B-containing receptors dominate; this window is also the hypothesized therapeutic-opportunity period for mechanism-based intervention (inference; DOI:10.3389/fnsyn.2022.1090865).
- **Remission:** not applicable for core ID; some epilepsies respond to ASMs.

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant; **all reported molecularly confirmed probands with tested parents carry de novo variants** (GeneReviews NBK501979). Penetrance estimated **100%**. Expressivity is highly variable (mild ID without seizures → severe DEE).
- **Recurrence risk:** ~1% for sibs, reflecting possible parental germline mosaicism; parental somatic+inferred germline mosaicism was ~10% in a general DEE cohort study cited by GeneReviews (NBK501979).
- **No anticipation, no founder effects, no consanguinity effect** (dominant de novo mechanism); carrier frequency not applicable.
- **Epidemiology:** point prevalence unknown; fewer than ~100 fully phenotyped individuals published as of the GeneReviews update, though diagnostic-lab counts are higher. GRIN2B variants account for ~0.2% of NDD/childhood-epilepsy cohorts (NBK501979). Model-based **birth incidence estimate: ~5.91 per 100,000 live births** for GRIN2B de novo disorder (López-Rivera et al., Brain 2020, 143:1099–1105 — one of the most common single-gene NDD estimates in that catalogue).
- **Demographics:** no ethnic or geographic clustering; sexes affected roughly equally (case-series data; no formal sex-ratio study).

## 10. Diagnostics

- **Genetic testing (diagnostic gold standard):** trio exome/genome sequencing or an ID/epilepsy multigene panel containing GRIN2B is first-line; single-gene testing is not recommended. Sequence analysis detects ~95% of pathogenic variants; CMA/targeted del-dup detects the ~5% that are deletions (GeneReviews NBK501979; GTR condition C3151411). Establishing de novo status supports pathogenicity (ACMG PS2).
- **Variant interpretation:** ClinVar holds many classified variants (e.g., RCV000022580 c.411+1G>A; RCV000625193 p.Ile751Thr); functional stratification (GoF vs LoF) via CFERV electrophysiology increasingly informs both interpretation and therapy selection (PMID:27818011; PMID:28377535).
- **Neuroimaging:** brain MRI may show cerebral volume loss, thin corpus callosum, or the characteristic MCD "intermediate between tubulinopathies and polymicrogyria" (PMID:28377535).
- **EEG:** indicated when seizures suspected; hypsarrhythmia in infantile-spasm presentations.
- **Laboratory biomarkers:** none; routine metabolic work-up is normal (distinguishes from metabolic ID).
- **Differential diagnosis:** other GRIN disorders (GRIN1, GRIN2A, GRIN2D), DEE27 (allelic; distinguished by epileptic-encephalopathy severity rather than gene), other monogenic NDDs (SCN2A, STXBP1, SYNGAP1, tubulinopathies when MCD present), Angelman/Rett-like presentations.
- **Screening:** not in newborn screening; carrier screening not applicable (de novo). Cascade testing limited to parental testing for mosaicism/recurrence counseling.

## 11. Outcome/Prognosis

- **Survival:** no systematic mortality data; lifespan appears near-normal in most, but severe DEE presentations carry generic risks (SUDEP, aspiration) — stated as inference, not measured.
- **Morbidity:** driven by ID severity (61% severe–profound), drug-resistant epilepsy (~half of the epileptic subgroup), non-ambulation and absent speech in severe cases, feeding dependence.
- **Prognostic factors:** variant class and location are the main predictors — functional GoF associates with earlier, more severe epilepsy; truncating/deletion (haploinsufficiency) more often with ID/ASD without severe epilepsy; MCD predicts severe outcome (PMID:28377535; genotype–phenotype review DOI:10.1186/s13023-025-04055-x, Orphanet J Rare Dis 2025).
- **Recovery potential:** core ID is static; developmental gains occur with therapy but full recovery is not observed.

## 12. Treatment

**No disease-modifying therapy is approved; management is symptomatic** (GeneReviews NBK501979). Suggested NCIT bindings marked (suggest).

- **Anti-seizure pharmacotherapy** — standard ASMs chosen by seizure type; ~50% of the epilepsy is drug-resistant. (NCIT:C15986 Pharmacotherapy, suggest.)
- **Memantine (repurposed NMDAR channel blocker)** — rationale: variants retain *"sensitivity to the use-dependent blocker memantine"*, but *"an objectifiable beneficial treatment response in the respective patients still remains to be demonstrated"* (PMID:28377535, verbatim). Anecdotal use in GoF variants. (CHEBI:64312 memantine, suggest.)
- **L-serine dietary supplementation (LoF variants)** — in a patient with GluN2B(P553T), D-serine restored receptor function in vitro and 11–17 months of L-serine supplementation was *"associated with clinical improvement"* in motor/cognitive performance and communication (Soto et al., Sci Signal 2019, DOI:10.1126/scisignal.aaw0936; n = 1). Phase 2A trial NCT04646447 (L-serine in GRIN-related encephalopathy) and n-of-1 crossover protocols (PMC10746402) followed; a 2023 Mol Genet Metab study reports further supportive evidence (DOI:10.1016/j.ymgme.2023.107673 — verify exact DOI from the ScienceDirect record S1096719223001531 before citing in KB). (CHEBI:17115 L-serine, suggest; NCIT:C15447 Dietary Intervention, suggest.)
- **Radiprodil (GluN2B-selective negative allosteric modulator; GoF variants)** — in vitro, *GRIN2B gain-of-function mutations are sensitive to radiprodil* (PMID:28533163). Phase 1b **Honeycomb** trial (NCT05818943, ages 6 mo–12 y, GoF GRIN variants) reported ~86% median reduction in countable motor seizures; FDA **Breakthrough Therapy designation** granted; global Phase 3 **BeeLine** trial dosing began late 2025/2026 (industry-reported NCT07224581 — verify registry ID before KB use).
- **Developmental/supportive care** — early-intervention programs, physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), speech/feeding therapy (NCIT:C159273), ABA-based behavioral intervention for ASD, gastrostomy feeding when required, standard spasticity and movement-disorder management. (All suggest.)
- **Pharmacogenomics:** the genotype itself (GoF vs LoF) is the stratifier for mechanism-based therapy — the clearest precision-medicine axis in this disease (PMID:28377535; DOI:10.1186/s13023-025-04055-x).

## 13. Prevention

- **Primary prevention:** none possible (sporadic de novo).
- **Genetic counseling:** essential; recurrence risk ~1% (germline mosaicism); prenatal and preimplantation genetic testing may be offered for that residual risk (GeneReviews NBK501979; NCIT:C15240 Genetic Counseling, suggest).
- **Secondary/tertiary prevention:** early molecular diagnosis enables early intervention, seizure surveillance, vision assessment, and avoidance of diagnostic odyssey; aggressive seizure control to limit encephalopathic contribution (standard-of-care inference).
- Population screening, immunization, and environmental interventions: not applicable.

## 14. Other Species / Natural Disease

- **No naturally occurring GRIN2B disease** is documented in companion animals or livestock (no OMIA phene identified for GRIN2B) — engineered models only.
- **Orthologs** (Alliance of Genome Resources): mouse Grin2b (MGI:95821, suggest-verify), rat Grin2b, zebrafish grin2bb/grin2ba, Drosophila Nmdar2, C. elegans nmr-2. GluN2B function in synaptic development is deeply conserved; the developmental GluN2B→GluN2A subunit switch is conserved across mammals (review DOI:10.3389/fnsyn.2022.1090865).
- Zoonotic/transmission sections: not applicable.

## 15. Model Organisms

- **Mouse, Grin2b null (ε2⁻/⁻):** the foundational model — homozygous knockouts have **no suckling response and die perinatally** (rescuable briefly by hand-feeding), with impaired trigeminal barrelette formation and loss of hippocampal LTD (Kutsuwada et al., Neuron 1996;16(2):333–344, PMID:8789948). Demonstrates GluN2B's essential developmental role; homozygous lethality is why human disease is heterozygous. **Limitation:** the null homozygote does not model the human heterozygous state; fidelity for MRD6 is indirect.
- **Mouse, Grin2b heterozygous and point-mutant knock-ins** (e.g., patient-derived C456Y LoF knock-in with NMDAR hypofunction and anxiety-like/behavioral phenotypes — see Sabo 2023 review for the model survey, DOI:10.3389/fnsyn.2022.1090865): recapitulate synaptic plasticity deficits and behavioral abnormalities; partial phenotype recapitulation (no robust seizures in most LoF models).
- **Rat, Grin2b haploinsufficient:** reported absence-like seizures and sleep abnormalities (bioRxiv 2024, DOI:10.1101/2024.02.27.582289 — preprint).
- **In vitro / cellular:** heterologous electrophysiology (Xenopus oocytes/HEK) is the workhorse for GoF/LoF classification (PMID:28377535; PMID:27818011); patient-variant-expressing primary hippocampal neurons show reduced spine density and impaired NMDAR-dependent AMPA-receptor insertion for GluN2B(P553T) (DOI:10.1126/scisignal.aaw0936); patient iPSC-derived neuron models are emerging.
- **Applications:** variant functional triage (drives therapy stratification), preclinical testing of memantine/radiprodil/serine, developmental-mechanism studies. **Resources:** MGI, IMPC (Grin2b het viability data), CFERV variant database, GRIN2B Foundation & CureGRIN registries.

---

## Key primary citations (verified this session)

- **PMID:20890276** — Endele S, et al. *Mutations in GRIN2A and GRIN2B encoding regulatory subunits of NMDA receptors cause variable neurodevelopmental phenotypes.* Nat Genet 2010;42(11):1021–6. doi:10.1038/ng.677. (Gene discovery; abstract cached locally.)
- **PMID:28377535** — Platzer K, et al. *GRIN2B encephalopathy: novel findings on phenotype, variant clustering, functional consequences and treatment aspects.* J Med Genet 2017;54(7):460–470. doi:10.1136/jmedgenet-2016-104509. (Largest cohort; abstract cached locally.)
- **PMID:8789948** — Kutsuwada T, et al. *Impairment of suckling response, trigeminal neuronal pattern formation, and hippocampal LTD in NMDA receptor ε2 subunit mutant mice.* Neuron 1996;16(2):333–44.
- **PMID:27818011** — Hu C, Chen W, Myers SJ, Yuan H, Traynelis SF. *Human GRIN2B variants in neurodevelopmental disorders.* J Pharmacol Sci 2016;132(2):115–121.
- **PMID:28533163** — *GRIN2B gain of function mutations are sensitive to radiprodil, a negative allosteric modulator of GluN2B-containing NMDA receptors.*
- **PMID:27656287** — *A 12p13 GRIN2B deletion is associated with developmental delay and macrocephaly.*
- Soto D, et al. Sci Signal 2019;12(586):eaaw0936. doi:10.1126/scisignal.aaw0936 (L-serine, LoF).
- Sabo SL, Lahr JM, Sceniak MP. Front Synaptic Neurosci 2023;14:1090865. doi:10.3389/fnsyn.2022.1090865 (mechanism review; PMC9873235).
- GeneReviews: *GRIN2B-Related Neurodevelopmental Disorder* (NBK501979).
- López-Rivera JA, et al. Brain 2020;143:1099–1105 (incidence catalogue: 5.91/100,000).
- Orphanet J Rare Dis 2025, doi:10.1186/s13023-025-04055-x (genotype–phenotype/therapeutic review).
- Trials: **NCT04646447** (L-serine, Phase 2A), **NCT05818943** (radiprodil Honeycomb Phase 1b).

Sources:
- [OMIM Entry #613970 — MRD6](https://omim.org/entry/613970)
- [ClinGen condition MONDO:0013509](https://search.clinicalgenome.org/kb/conditions/MONDO:0013509)
- [ClinGen GRIN2B dosage sensitivity (HGNC:4586)](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:4586)
- [GeneReviews: GRIN2B-Related Neurodevelopmental Disorder (NBK501979)](https://www.ncbi.nlm.nih.gov/books/NBK501979/)
- [GARD 12851 — Intellectual disability, autosomal dominant 6](https://rarediseases.info.nih.gov/diseases/12851/intellectual-disability-autosomal-dominant-6)
- [MedGen C3151411](https://www.ncbi.nlm.nih.gov/medgen/462761)
- [Platzer 2017, PMID 28377535](https://pubmed.ncbi.nlm.nih.gov/28377535/)
- [Endele 2010, Nat Genet](https://www.nature.com/articles/ng.677)
- [Kutsuwada 1996, PMID 8789948](https://pubmed.ncbi.nlm.nih.gov/8789948/)
- [Hu 2016, PMID 27818011](https://pubmed.ncbi.nlm.nih.gov/27818011/)
- [Radiprodil in vitro, PMID 28533163](https://pubmed.ncbi.nlm.nih.gov/28533163/)
- [12p13 GRIN2B deletion, PMID 27656287](https://pubmed.ncbi.nlm.nih.gov/27656287/)
- [Soto 2019, Science Signaling](https://www.science.org/doi/10.1126/scisignal.aaw0936)
- [Sabo 2023 mechanism review, Front Synaptic Neurosci](https://www.frontiersin.org/journals/synaptic-neuroscience/articles/10.3389/fnsyn.2022.1090865/full)
- [López-Rivera 2020 incidence catalogue, Brain](https://academic.oup.com/brain/article/143/4/1099/5803191)
- [OJRD 2025 genotype–phenotype review](https://link.springer.com/article/10.1186/s13023-025-04055-x)
- [L-serine trial NCT04646447](https://clinicaltrials.gov/study/NCT04646447)
- [Radiprodil Breakthrough Therapy designation](https://practicalneurology.com/news/radiprodil-designated-a-breakthrough-therapy-for-grin-related-neurodevelopmental-disorder/2473793/)
- [Phase 3 BeeLine trial announcement](https://www.prnewswire.com/news-releases/grin-therapeutics-announces-first-patient-dosed-in-global-phase-3-beeline-trial-of-investigational-radiprodil-for-grin-related-neurodevelopmental-disorder-302656999.html)
- [Grin2b rat model preprint, bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.02.27.582289v1.full)
- [ClinVar RCV000022580](https://www.ncbi.nlm.nih.gov/clinvar/RCV000022580/) · [RCV000625193](https://www.ncbi.nlm.nih.gov/clinvar/RCV000625193/)
- [GTR condition C3151411](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3151411/)
- [MRD6 case report, Cureus 2023 (PMC10623208)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10623208/)
- [L-serine n-of-1 protocol (PMC10746402)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10746402/)
- [MedlinePlus GRIN2B gene](https://medlineplus.gov/genetics/gene/grin2b/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1016/j.ymgme.2023.107673` (1 mention) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:8789948` (5 mentions) - Impairment of suckling response, trigeminal neuronal pattern formation, and hippocampal LTD in NMDA receptor epsilon 2 subunit mutant mice.
  - shared terms: receptor

Weighed against this report's own most characteristic terms: `grin2b`, `variant`, `developmental`, `seizure`, `nbk501979`, `disorder`, `novo`, `gene`, `epilepsy`, `glun2b`, `receptor`, `dominant`, `mrd6`, `deletion`, `phenotype`, `intellectual`, `autosomal`, `disability`, `disease`, `therapy`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15302` (1 mention) - the report calls it "Developmental/supportive care** — early-intervention programs, physical therapy"; NCIT calls it **Physical Therapy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.