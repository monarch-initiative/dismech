---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-26T23:32:01.418709'
end_time: '2026-09-26T23:40:09.399719'
duration_seconds: 487.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ACTA1-Related Nemaline Myopathy
  mondo_id: MONDO:0008070
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
  web_search_requests: 32
  num_turns: 42
  total_cost_usd: 2.547474
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 29
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 7
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMC:PMC3447773
  - PMID:15236405
  relevance_assessed: 25
  on_topic: 23
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001319
    reported_labels:
    - Near-universal in congenital forms
    ontology_label: Neonatal hypotonia
  - term_id: HP:0003324
    reported_labels:
    - Defining feature of "typical" form
    ontology_label: Generalized muscle weakness
  - term_id: HP:0001265
    reported_labels:
    - Common
    ontology_label: Hyporeflexia
  - term_id: HP:0003701
    reported_labels:
    - 68% (pediatric systematic review, n=101, PMC10032635)
    ontology_label: Proximal muscle weakness
  labels_variant: 4
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ACTA1-Related Nemaline Myopathy
- **MONDO ID:** MONDO:0008070 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ACTA1-Related Nemaline Myopathy** covering all of the
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

I'll research ACTA1-Related Nemaline Myopathy directly and compile the full report now. Let me start by loading the web research tools and gathering data from primary sources.

# ACTA1-Related Nemaline Myopathy: Comprehensive Research Report

## Identifiers
- **Gene:** ACTA1 (actin alpha 1, skeletal muscle) — HGNC:129, NCBI Gene ID: 58, chromosome 1q42.13 ([Atlas Genet Cytogenet Oncol Haematol](https://atlasgeneticsoncology.org/Genes/GC_ACTA1.html); [PMID:10072583](https://pubmed.ncbi.nlm.nih.gov/10072583/))
- **OMIM gene:** *102610* — ACTIN, ALPHA-1, SKELETAL MUSCLE; ACTA1 ([omim.org/entry/102610](https://omim.org/entry/102610))
- **OMIM phenotypes (phenotypic series, current nosology):**
  - *#161800* — Congenital myopathy 2A, typical, autosomal dominant (CMYO2A; historically "Nemaline myopathy 3," NEM3)
  - *#620265* — Congenital myopathy 2B, severe infantile, autosomal recessive (CMYO2B)
  - *#620278* — Congenital myopathy 2C, severe infantile, autosomal dominant (CMYO2C)
  - Additional allelic entities discussed below: actin-accumulation myopathy, intranuclear rod myopathy, cap myopathy, congenital fiber-type disproportion (CFTD), and an emerging dilated-cardiomyopathy/distal-myopathy spectrum
- **MONDO:** MONDO:0008070; **MedGen:** C3711389
- **UniProt:** P68133 (skeletal muscle α-actin, ACTS_HUMAN); **MGI (mouse ortholog):** MGI:87902 (Acta1)
- Orphanet lists nemaline myopathy generically with ACTA1 as a causal gene; I was not able to retrieve a confirmed disease-specific ORPHA code for the ACTA1 subtype from the sources fetched in this session — flagged as a gap rather than guessed.

Most of what follows is aggregated disease-level knowledge (literature cohorts, structured databases, model-organism studies) rather than a single-patient EHR source.

---

## 1. Disease Overview

Nemaline myopathy (NM) is a clinically and genetically heterogeneous group of congenital skeletal-muscle disorders defined by the presence of rod-like ("nemaline") inclusions in myofibers on biopsy, together with hypotonia and weakness of variable severity. **ACTA1**, encoding skeletal muscle α-actin — the core building block of the sarcomeric thin filament — is the second most common causal gene after **NEB** (nebulin) for NM overall, but **the single most common cause of the severe subset**: "ACTA1 accounts for more than half of the severe NM cases" ([PMC9271256](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271256/); Acta Neuropathol Commun 2022, doi:10.1186/s40478-022-01400-0). Population-level estimates place ACTA1 at roughly 20–41% of genetically solved NM cohorts depending on severity mix, and ACTA1 variants overall account for **~15–25% of all congenital myopathy** diagnoses (search synthesis of multiple reviews; [PMID:22825594](https://pubmed.ncbi.nlm.nih.gov/22825594/) Nowak, Ravenscroft & Laing, *Acta Neuropathol* 2013).

Common synonyms/related terms: nemaline myopathy 3 (NEM3, legacy name), actin-accumulation myopathy, congenital myopathy with excess of thin filaments, intranuclear rod myopathy, cap myopathy (specific to the p.Met47Val variant), and — increasingly recognized as distinct, non-NM phenotypes from the same gene — congenital fiber-type disproportion (CFTD), ACTA1-related dilated cardiomyopathy, and an emerging ACTA1-related distal myopathy.

---

## 2. Etiology

**Disease causal factor.** ACTA1-related myopathy is a purely monogenic structural-protein disorder — no environmental, infectious, or multifactorial contribution to primary causation has been established. All causation is genetic, arising through two distinct molecular routes (detailed in §4/§6):

- **Dominant, usually de novo, missense mutation** — a mutant actin monomer is incorporated into the thin filament alongside wild-type actin, producing a *dominant-negative/poison-subunit* effect rather than haploinsufficiency. This explains **93.3% (365/391)** of pathogenic/likely-pathogenic (P/LP) ACTA1 variants in the most recent curated update, of which **88% are confirmed de novo** ([PMC11918651](https://pmc.ncbi.nlm.nih.gov/articles/PMC11918651/), Clayton et al., *Hum Mutat* 2024/2025 variant-database update).
- **Biallelic (homozygous/compound-heterozygous) loss-of-function** (frameshift/nonsense) — complete absence of skeletal α-actin protein, accounting for **6.6% (26/391)** of P/LP variants, and producing severe, often lethal disease ([PMID:25182138](https://pubmed.ncbi.nlm.nih.gov/25182138/), *Eur J Hum Genet* 2015, "Recessive ACTA1 variant causes congenital muscular dystrophy with rigid spine").

**Genetic risk factors.** The gene itself is the risk factor; there is no described common susceptibility-locus or polygenic contribution. gnomAD constraint data are informative for interpreting variant pathogenicity: ACTA1 is markedly missense-constrained (only ~21% of expected missense variants observed genome-wide-length-adjusted; ranked 164th of 19,704 genes for missense intolerance) but **tolerant of loss-of-function heterozygosity** (pLI 0; o/e 0.74, 11 observed/14.9 expected) — consistent with the mechanism above: a null allele is silent in the heterozygous state, and disease from LoF variants requires biallelic loss ([PMC11918651](https://pmc.ncbi.nlm.nih.gov/articles/PMC11918651/)).

**Environmental risk factors:** none identified.

**Protective factors.** A partial biological "rescue" mechanism has been demonstrated in the recessive-null state: cardiac (fetal) α-actin (ACTC1) is normally co-expressed in developing skeletal muscle and down-regulated postnatally; in Acta1-null mice, sustained/elevated ACTC1 expression is sufficient to functionally substitute for absent skeletal α-actin and rescue lethality — "ACTC is sufficiently similar to ACTA1 to produce adequate function in postnatal skeletal muscle" ([PMID:19468071](https://pubmed.ncbi.nlm.nih.gov/19468071/), Nowak et al., *J Cell Biol* 2009). This is the leading candidate explanation for why some biallelic-null human patients survive rather than uniformly dying perinatally, and it has been explicitly pursued as a therapeutic strategy for *dominant* ACTA1 disease as well (cardiac α-actin over-expression therapy; [PMID:23736297](https://pubmed.ncbi.nlm.nih.gov/23736297/)) — see §12.

**Gene-environment interactions:** none reported; this is not a gene-environment-interaction disease model.

---

## 3. Phenotypes

Phenotype data below are drawn from aggregated multi-patient literature cohorts (case-series/systematic reviews), not from a single registry with formal frequency validation — treat percentages as literature-derived estimates from the specific cohorts cited, which differ in inclusion criteria (severity-enriched vs. unselected).

**Core/near-universal features**
| Phenotype | Onset/pattern | Frequency (source cohort) | Suggested HPO |
|---|---|---|---|
| Neonatal hypotonia | Congenital | Near-universal in congenital forms | HP:0001319 |
| Generalized muscle weakness, neck-flexor and respiratory predominance | Congenital–childhood | Defining feature of "typical" form | HP:0003324 |
| Respiratory insufficiency/failure | Neonatal–progressive | 75/143 significant first-year respiratory disease ([PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/), Ryan et al., *Ann Neurol* 2001); dyspnea in 55% of a pediatric cohort (n=101) | HP:0002093 / HP:0004879 |
| Feeding difficulty/dysphagia | Neonatal onward | 79/143 (Ryan et al.); 47% dysphagia in pediatric cohort | HP:0002015 / HP:0011968 |
| Hypo-/areflexia | Congenital | Common | HP:0001265 |
| Axial (truncal) weakness | Variable | 68% (pediatric systematic review, n=101, [PMC10032635](https://pmc.ncbi.nlm.nih.gov/articles/PMC10032635/)) | HP:0003701 |

**Musculoskeletal/structural**
- Arthrogryposis multiplex congenita (HP:0002804) — a strong early-mortality predictor
- High-arched palate (HP:0002705), facial weakness/myopathic facies
- Kyphoscoliosis/scoliosis (HP:0002650) — a major progressive complication in survivors
- Pectus excavatum (HP:0000767), clubfoot/pes planus (HP:0001762)
- Fractures, joint contractures, skull enlargement (pediatric systematic review, [PMC10032635](https://pmc.ncbi.nlm.nih.gov/articles/PMC10032635/))

**Atypical/emerging phenotypes** (from the largest recent cohort, n=275): ophthalmoplegia, unusual weakness distribution, cardiomyopathy, and intranuclear rods as "atypical" ACTA1 presentations ([PMID:40661861](https://pubmed.ncbi.nlm.nih.gov/40661861/), *Neurol Genet* 2025).

**Prenatal (severe end of spectrum)**
- Fetal akinesia/reduced fetal movement (HP:0001989), polyhydramnios (HP:0001561, from impaired fetal swallowing, appearing from ~28 weeks), intrauterine growth restriction, pulmonary hypoplasia — the fetal akinesia deformation sequence (FADS), of which ACTA1 is a recognized cause via de novo or somatic mosaic variants (search synthesis; general FADS population incidence ~1:15,000 in a Danish study, not ACTA1-specific).

**Laboratory**
- Creatine kinase typically normal to mildly elevated (reported means ~107 IU/L, range 25–369) — a distinguishing feature from dystrophic myopathies (search synthesis of case reports).

**Quality of life.** No ACTA1-specific EQ-5D/SF-36 data were located; qualitatively, respiratory failure, feeding dependence, and progressive scoliosis are the dominant drivers of morbidity and caregiver burden, and these tend to **diminish with age in survivors** while chronic weakness and orthopedic sequelae persist ([PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/)).

---

## 4. Genetic/Molecular Information

**Variant landscape** (most current source: Clayton et al. curated update, [PMC11918651](https://pmc.ncbi.nlm.nih.gov/articles/PMC11918651/)):
- 607 total reported variants across HGMD/LOVD/ClinVar; after ACMG/AMP reclassification, **447 pathogenic/likely pathogenic, 13 VUS, 147 benign/likely benign**.
- Type distribution among 391 analyzed P/LP variants: **missense 340 (87.0%)**, frameshift 18 (4.6%), nonsense 13 (3.3%), splicing 9 (2.3%), in-frame indel 6 (1.5%), stop-loss 3 (0.8%), start-loss 2 (0.5%).
- Inheritance: **dominant 365/391 (93.3%)** (88% of these confirmed de novo), **recessive 26/391 (6.6%)**.
- Missense P/LP variants affect **154/377 (40.8%)** of ACTA1 residues; across all six human actin isoforms, disease-associated missense variants collectively involve 345/377 (91.5%) residues — reflecting near-total intolerance of the actin fold to substitution.
- Phenotype distribution among P/LP variants: **nemaline myopathy 74%**, congenital fiber-type disproportion 7.2%, intranuclear rod myopathy 4.3%, cardiomyopathies 5.3% (dilated most common), fetal abnormalities 5.3%, and an emerging distal myopathy phenotype (4 reported families) — 20 distinct clinical presentations recorded in total.

**Structural mechanism.** Skeletal α-actin folds into two lobes each with two subdomains (SD1–SD4); a cleft between SD2 and SD4 binds ATP/ADP·Mg²⁺, clamped by phosphate-binding loops P1 (residues 11–16) and P2 (residues 154–161), while a separate cleft between SD1 and SD3 mediates binding of most actin-binding proteins, including myosin and tropomyosin (search synthesis of structural biology literature). Disease variants cluster at:
- The **ATP-binding cleft**, disrupting nucleotide binding and polymerization competence;
- The **actin-actin (longitudinal/lateral filament) interface**, impairing thin-filament assembly;
- The **actin-myosin/tropomyosin interaction surface**, directly impairing cross-bridge cycling — demonstrated for p.Asp286Gly, which "prevents proper strong myosin binding and triggers muscle weakness" ([PMC3447773](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447773/), PLOS One).

**Dominant-negative evidence.** Direct biochemical/cellular evidence for a dominant-negative mechanism (abnormal folding, aggregation, and altered polymerization of mutant actin isoforms) is reported in [PMID:15198992](https://pubmed.ncbi.nlm.nih.gov/15198992/). Genotype-phenotype heterogeneity is substantial even for the same or similar residues — "the marked variability in clinical phenotype among patients with different mutations in ACTA1 suggested that both the site of the mutation and the nature of the amino acid change have differential effects on thin-filament formation and protein-protein interactions" (search synthesis; corroborated by [PMID:15236405](https://pubmed.ncbi.nlm.nih.gov/15236405/), "Heterogeneity of nemaline myopathy cases with skeletal muscle alpha-actin gene mutations").

**Recessive/null mechanism.** Biallelic frameshift/nonsense variants abolish ACTA1 protein expression entirely. "Previously reported patients with biallelic ACTA1 mutations had functional 'null' variants and made no ACTA1 protein... All recessive variants reported to date have resulted in loss of skeletal α-actin expression from muscle and severe weakness from birth," with reported deaths at 5 and 19 days of age in the most severe reported cases (search synthesis of case literature; [PMID:25182138](https://pubmed.ncbi.nlm.nih.gov/25182138/)). Postnatal compensatory upregulation of cardiac (fetal) α-actin (ACTC1) in skeletal muscle is proposed to explain the variable survival seen in some null-recessive patients (mechanistically validated in mice, [PMID:19468071](https://pubmed.ncbi.nlm.nih.gov/19468071/)).

**Cardiomyopathy variants.** A distinct, non-skeletal-muscle-predominant phenotype has been reported: p.Arg256His causes dilated cardiomyopathy via disruption of actin structure/function and cardiomyocyte hypocontractility ([PMID:38559046](https://pubmed.ncbi.nlm.nih.gov/38559046/), 2024) — evidence that the same gene can produce organ-selective disease depending on variant biochemistry and which sarcomeric isoform environment is affected.

**Modifier genes:** none formally established for ACTA1 specifically; comparative cohort data show that genotype (ACTA1 vs. NEB) itself modifies early feeding/ventilation needs (§9/§11), but no discrete modifier locus has been identified.

**Epigenetic information / chromosomal abnormalities:** not applicable/not reported — ACTA1 disease is driven by point mutations and small indels in a single, small (6-exon) protein-coding gene; no epigenetic mechanism or large chromosomal rearrangement has been implicated.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious causal factor has been established for ACTA1-related myopathy — it is fully accounted for by the genetic mechanisms above. Infections (particularly respiratory) are a major **secondary** driver of morbidity and mortality (aspiration, pneumonia) rather than a cause, consistent with the respiratory-muscle weakness and impaired airway clearance intrinsic to the disease (§3, §11).

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, with explicit branch points)

1. A **heterozygous, typically de novo, missense mutation** in ACTA1 alters the amino-acid sequence of skeletal muscle α-actin at a site critical to the ATP-binding cleft, the actin-actin polymerization interface, or the actin-myosin/tropomyosin binding surface — **OR**, alternatively, **biallelic frameshift/nonsense mutation** abolishes ACTA1 protein expression entirely (branch established at step 1; downstream consequences diverge, see step 9).
2. For dominant missense variants: the mutant actin monomer is co-synthesized with wild-type actin and **incorporates into growing thin filaments as a "poison subunit"** (dominant-negative mechanism), demonstrated directly by abnormal folding, aggregation, and altered polymerization kinetics of mutant actin isoforms ([PMID:15198992](https://pubmed.ncbi.nlm.nih.gov/15198992/)).
3. This **leads to** defective actin polymerization — patient-derived fibroblasts show markedly shortened, unstructured actin filaments, with only ~7% of mutant cells achieving correct polymerization versus near-100% of controls ([PMC10740811](https://pmc.ncbi.nlm.nih.gov/articles/PMC10740811/), in vitro, patient fibroblasts).
4. Depending on mutation site, misfolded/mutant actin **results in** aggregation into rod-like inclusions (classic nemaline/rod bodies, structurally continuous with Z-disks and containing α-actinin, myotilin, and sarcomeric actin), or into intranuclear rods, cytoplasmic bodies, cores, or caps — a branch point in the cascade that determines histopathological subtype rather than clinical severity per se ([PMID:22825594](https://pubmed.ncbi.nlm.nih.gov/22825594/); [PMC9271256](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271256/), which additionally reports mislocalization of lamin A/C, Nesprin-1, and Nesprin-2 — nuclear lamina/LINC-complex components — in the severe intranuclear-rod subtype, implicating nuclear envelope dysfunction as a further downstream consequence).
5. Independently of aggregate formation, malformed/incorporated mutant actin **impairs sarcomeric cross-bridge cycling**: p.Asp286Gly directly prevents proper strong myosin binding, and functional studies confirm that "dysfunctional sarcomere contractility contributes to muscle weakness in ACTA1-related nemaline myopathy" ([PMID:29328520](https://pubmed.ncbi.nlm.nih.gov/29328520/)).
6. In parallel, actin polymerization failure **triggers compensatory RhoA/ROCK1 pathway overactivation** (increased active RhoA and phosphorylated ROCK1 in patient fibroblasts) and disrupts actin-dependent regulation of mitochondrial dynamics, **leading to** mitochondrial network fragmentation (increased DRP1, decreased OPA1), reduced basal/maximal/spare respiration, decreased ATP generation, downregulated OXPHOS complex I–V subunits, and elevated mitochondrial ROS — reproduced independently in ACTA1(H40Y) patient-iPSC-derived skeletal myocytes ([PMID:36796746](https://pubmed.ncbi.nlm.nih.gov/36796746/); [PMC10740811](https://pmc.ncbi.nlm.nih.gov/articles/PMC10740811/)). This bioenergetic branch is *reversible in vitro*: 7-day supplementation with linoleic acid and L-carnitine restored actin polymerization and normalized mitochondrial parameters in the fibroblast model.
7. Sarcomeric dysfunction (step 5) plus bioenergetic failure (step 6) **jointly reduce contractile force generation**, manifesting clinically as generalized hypotonia and weakness, with a predilection for neck-flexor and respiratory muscles.
8. In the most severe prenatal cases, profound failure of fetal muscle contraction **causes** fetal akinesia/hypokinesia, which in turn **produces** arthrogryposis multiplex congenita, pulmonary hypoplasia (from lack of fetal breathing movements), and polyhydramnios (from impaired fetal swallowing) — culminating in stillbirth or early neonatal death from respiratory failure in the severest subset.
9. **Recessive-null branch:** complete absence of ACTA1 protein removes the primary thin-filament structural component entirely; disease severity in this branch is modulated by the degree of postnatal compensatory upregulation of cardiac (fetal) α-actin (ACTC1) in skeletal muscle, which can partially substitute for the missing protein and is sufficient to rescue lethality in Acta1-null mice when sufficiently expressed ([PMID:19468071](https://pubmed.ncbi.nlm.nih.gov/19468071/)) — this is an *inferred* mechanism in humans, extrapolated from the mouse rescue experiment rather than directly demonstrated in patient tissue.
10. Postnatally, chronic weakness of paraspinal/postural and respiratory muscles **drives** a feed-forward cycle: progressive kyphoscoliosis and joint contractures further compromise respiratory mechanics, compounding the primary respiratory-muscle weakness and accounting for most of the long-term morbidity/mortality burden (§11).
11. **Divergent-outcome branch:** variants affecting the actin-myosin/tropomyosin interface preferentially, without prominent aggregation, instead produce isolated congenital fiber-type disproportion (type 1 fiber hypotrophy without rods) ([PMID:17387733](https://pubmed.ncbi.nlm.nih.gov/17387733/), Clarke et al., "The pathogenesis of ACTA1-related congenital fiber type disproportion," *Ann Neurol* 2007); variants disrupting cardiac-relevant actin-myosin interactions instead cause dilated cardiomyopathy with cardiomyocyte hypocontractility ([PMID:38559046](https://pubmed.ncbi.nlm.nih.gov/38559046/)); and a small number of families show a distal-predominant weakness pattern — an emerging phenotype not yet mechanistically dissected.

### Molecular pathways / GO terms
- Actin filament polymerization (GO:0030041); actomyosin structure organization / sarcomere organization (GO:0045214); striated muscle contraction (GO:0006941); positive regulation of Rho protein signal transduction (GO:0035025, downstream compensatory signaling); mitochondrial fission (GO:0000266) / mitochondrial fusion (GO:0007005); ATP metabolic process (GO:0046034, downstream bioenergetic failure).

### Cell types (CL terms)
- Skeletal muscle fiber (CL:0000188); type I (slow) skeletal muscle fiber (CL:0002586, selectively hypotrophic in CFTD); type II (fast) skeletal muscle fiber (CL:0002617); fibroblast (CL:0000057, the in vitro disease model used for the mitochondrial mechanism work); induced pluripotent stem cell-derived skeletal myocyte (used for H40Y iPSC model).

### Advanced/omics data
No transcriptomic, proteomic, single-cell, or spatial-transcriptomic dataset specific to ACTA1-related myopathy patient muscle was identified in this search — a data gap relative to better-resourced neuromuscular diseases. The mechanistic omics-adjacent data available is limited to targeted Western blot/qPCR (fibroblast/iPSC studies above) and classical histopathology/electron microscopy; no GEO/ArrayExpress dataset was located for this specific gene-disease pair.

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: skeletal muscle (generalized, with axial/neck-flexor/respiratory predominance in the typical form; distal predominance in the emerging distal phenotype). Secondary: respiratory system (restrictive failure secondary to muscle weakness and scoliosis); cardiac muscle (in the emerging cardiomyopathy phenotype, [PMID:38559046](https://pubmed.ncbi.nlm.nih.gov/38559046/)); gastrointestinal/oropharyngeal (dysphagia from bulbar/pharyngeal muscle weakness); skeletal system (secondary structural deformity — scoliosis, contractures, pectus excavatum — from chronic weakness rather than a primary skeletal defect).

**Tissue/cell level.** Skeletal myofibers, particularly type 1 (slow-twitch) fibers in the CFTD phenotype; cardiomyocytes in the cardiomyopathy phenotype.

**Subcellular level.** Sarcomeric thin filament and Z-disk (GO:0030018, Z disc — the structural origin of nemaline rods); sarcoplasm (site of cytoplasmic bodies/actin aggregates); nucleus and nuclear envelope/lamina (intranuclear rods; mislocalized lamin A/C, Nesprin-1/2 — LINC complex — in the severe subtype, [PMC9271256](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271256/)); mitochondria (fragmented network, reduced OXPHOS complex expression).

**Localization/laterality.** Bilateral, symmetric, generalized muscle involvement is typical; no lateralization is described.

---

## 8. Temporal Development

**Onset and course** (from the landmark 143-patient cohort, [PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/), Ryan et al., *Ann Neurol* 2001 — the most cited natural-history stratification, applicable to NM broadly and reflected in ACTA1-specific cohorts):

| Subtype | n (of 143) | Onset | Course |
|---|---|---|---|
| Severe congenital | 23 | Prenatal/birth | Often fatal in infancy from respiratory failure |
| Intermediate congenital | 29 | Birth | Significant weakness, ventilator-dependence common |
| Typical congenital | 66 (most common) | Birth–infancy | Neonatal hypotonia, delayed motor milestones, static-to-slowly-progressive |
| Childhood-onset | 19 | Childhood | Milder, slower progression |
| Adult-onset | 6 | Adulthood | Rare, mildest end of spectrum |

ACTA1-specific data (275-patient cohort, [PMID:40661861](https://pubmed.ncbi.nlm.nih.gov/40661861/)) show that ACTA1-NM patients are **more likely than NEB-NM patients to require feeding tubes and invasive ventilation in the first year of life**, though this difference narrows after the first year — consistent with ACTA1 being enriched for the severe end of the clinical spectrum.

**Progression pattern.** Generally static-to-slowly-progressive in survivors of the congenital forms; a minority develop progressive distal weakness over time. Morbidity from respiratory infections and feeding difficulties characteristically **diminishes with age** in survivors, while orthopedic complications (scoliosis) tend to **worsen** during growth/adolescence — a divergent temporal pattern across organ systems.

**Critical periods.** The neonatal period is the critical window for respiratory/feeding crisis and early mortality; adolescence is the critical window for scoliosis progression and associated respiratory compromise.

---

## 9. Inheritance and Population

**Epidemiology.** Overall nemaline myopathy prevalence is estimated at **~1:50,000 live births** worldwide, consistent with a Finnish birth-prevalence estimate of 0.02 per 1,000 live births (search synthesis of multiple reviews). ACTA1 causes an estimated 15–25% of all congenital myopathies and a substantial (cohort-dependent, roughly 20–40%) share of genetically solved NM, rising to **>50% of the severe NM subset** ([PMC9271256](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271256/)).

**Inheritance pattern.** Autosomal dominant (93.3% of P/LP variants, 88% de novo) or autosomal recessive (6.6%, biallelic null variants) ([PMC11918651](https://pmc.ncbi.nlm.nih.gov/articles/PMC11918651/)).

**Penetrance/expressivity.** Dominant missense disease is essentially fully penetrant but shows **marked variable expressivity** even for identical or neighboring residue substitutions, attributed to differential effects of mutation site/biochemistry on thin-filament assembly ([PMID:15236405](https://pubmed.ncbi.nlm.nih.gov/15236405/)).

**Germline mosaicism.** Not specifically quantified for ACTA1 in the literature retrieved; general empirical recurrence-risk figures for de novo dominant conditions (~1–5%, occasionally much higher with parental gonadal mosaicism) apply generically but are **not gene-specific data** — a recognized gap. Somatic/germline mosaicism has, however, been specifically implicated as a mechanism for ACTA1-related fetal akinesia in de novo cases (search synthesis).

**Founder effects/consanguinity.** No founder mutations are described; recessive (biallelic null) cases would be expected to be enriched by consanguinity, consistent with general Mendelian recessive-disease principles, though no ACTA1-specific consanguinity registry data were retrieved.

**Sex ratio/geographic distribution.** No sex predilection is reported (autosomal gene, both dominant and recessive mechanisms). No geographic clustering or endemic distribution has been described; cases have been reported worldwide (the pediatric systematic review sampled 101 patients from 23 countries, [PMC10032635](https://pmc.ncbi.nlm.nih.gov/articles/PMC10032635/)).

---

## 10. Diagnostics

**Muscle biopsy** remains the histopathological gold standard: modified Gömöri trichrome stain reveals red-staining rod/granular sarcoplasmic inclusions (nemaline bodies); electron microscopy confirms sarcoplasmic rods often continuous with Z-disks, and — in the severe ACTA1 subtype specifically — **intranuclear rods, cytoplasmic bodies, and enlarged perinuclear space** are characteristic distinguishing features from other NM genotypes ([PMC9271256](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271256/)). A single biopsy may show multiple co-occurring pathologies (rods, cores, caps, fiber-type disproportion) ([PMID:22825594](https://pubmed.ncbi.nlm.nih.gov/22825594/)).

**Laboratory.** Serum creatine kinase is typically normal to only mildly elevated — a useful negative discriminator against dystrophic processes.

**Genetic testing.** First-line is typically a targeted congenital-myopathy/nemaline-myopathy multigene panel (ACTA1, NEB, TPM2, TPM3, TNNT1, CFL2, KBTBD13, KLHL40, KLHL41, LMOD3, MYPN, MYO18B, ADSSL1) or exome/genome sequencing, given the genetic heterogeneity of NM; single-gene ACTA1 sequencing is reasonable when the clinical/histopathological picture (especially intranuclear rods or a severe congenital presentation) points specifically to ACTA1. Recessive cases require deliberate assessment of biallelic status (zygosity, potential compound heterozygosity), since dominant de novo missense is the default prior.

**Imaging.** Muscle MRI fatty-infiltration patterns are used adjunctively to help distinguish congenital myopathy subtypes, though no ACTA1-specific validated MRI signature was retrieved in this search.

**Prenatal diagnosis.** Ultrasound findings suggestive of the severe end of the spectrum include reduced fetal movement, multiple joint contractures/arthrogryposis, and polyhydramnios (typically apparent from ~28 weeks); genetic confirmation is by CVS/amniocentesis testing for a known familial variant, or by prenatal exome sequencing in undiagnosed severe fetal akinesia (search synthesis).

**Differential diagnosis.** Other congenital myopathies presenting with neonatal hypotonia must be distinguished, particularly: central core disease/multiminicore disease (RYR1) — important because of a *different* malignant hyperthermia risk profile (see §12); centronuclear/myotubular myopathy (MTM1, DNM2, BIN1); congenital muscular dystrophies; spinal muscular atrophy; congenital myasthenic syndromes; and the other nemaline-myopathy genes listed above.

---

## 11. Outcome/Prognosis

**Mortality.** In the landmark 143-patient cohort, 30 patients (~21%) died, the majority within the first 12 months of life, with **all deaths attributable to respiratory insufficiency**, which was "frequently underrecognized in older patients" ([PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/)). A more recent, severity-enriched pediatric systematic review (n=101) reported 36% mortality, with causes of death including sepsis, respiratory insufficiency, cardiopulmonary arrest, infection, or hypoxic-ischemic brain injury ([PMC10032635](https://pmc.ncbi.nlm.nih.gov/articles/PMC10032635/)) — the higher figure likely reflects a case-report-based sampling bias toward more severe/unusual presentations rather than a true increase in population mortality; both figures are reported here rather than reconciled, per the source cohorts' differing methodology.

**Predictors of early mortality:** arthrogryposis, neonatal respiratory failure, and failure to achieve early motor milestones ([PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/)).

**Genotype-specific survival.** In the largest cohort to date (n=275), survival differed by molecular diagnosis: NEB-NM patients had **higher survival** than patients with no molecular diagnosis, and ACTA1-NM patients required feeding tubes and invasive ventilation more often than NEB-NM patients in the first year of life ([PMID:40661861](https://pubmed.ncbi.nlm.nih.gov/40661861/)).

**Morbidity in survivors.** Respiratory-tract-infection and feeding-difficulty morbidity characteristically diminish with age, while chronic weakness, progressive scoliosis, and joint contractures persist as the dominant drivers of long-term disability. "Aggressive early management is warranted in most cases of congenital nemaline myopathy" ([PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/)).

**Functional outcome** ranges widely by subtype — from ventilator-dependent, non-ambulatory survivors (severe/intermediate congenital forms) to independently ambulatory adults with mild residual weakness (typical congenital, childhood-, and adult-onset forms) — but no formal ACTA1-specific ambulation/PROMIS/EQ-5D outcome dataset was located.

---

## 12. Treatment

There is **no approved disease-modifying or curative therapy**; management is entirely supportive and multidisciplinary.

**Respiratory:** surveillance for nocturnal hypoventilation; noninvasive ventilation (BiPAP) is an important therapeutic option in patients with chronic respiratory failure, progressing to invasive ventilation/tracheostomy in the most severe cases (search synthesis; [PMC6945071](https://pmc.ncbi.nlm.nih.gov/articles/PMC6945071/)). NCIT: C15747 (Supportive Care).

**Nutrition/feeding:** nasogastric feeding in the neonatal period, frequently progressing to percutaneous gastrostomy; dysphagia rehabilitation/speech-language and oral-motor therapy has shown potential to improve swallowing function even in children with severe oral-motor dysfunction (search synthesis of case series). NCIT: C15433 (Nutritional Support).

**Orthopedic/rehabilitative:** physical and occupational therapy for contracture management and functional mobility (NCIT:C15302 Physical Therapy; NCIT:C15315 Rehabilitation); scoliosis surveillance with **spinal fusion surgery** when indicated (NCIT:C15329 Surgical Procedure), requiring specific **anesthetic precautions** — avoidance of succinylcholine and other depolarizing/triggering agents given the risk of anesthesia-induced rhabdomyolysis and life-threatening hyperkalemia in structural myopathies broadly; note that **isolated ACTA1/nemaline myopathy is not itself considered malignant-hyperthermia-susceptible** in the way RYR1-related core myopathies are, an important distinction for anesthetic risk-stratification (search synthesis of orphananesthesia/anesthesia-literature guidance).

**Pharmacotherapy.** No approved drug. **L-tyrosine** has been trialed empirically in small open-label case series (250–3000 mg/day, 2 months to 5 years) with subjectively reported short-term improvements in strength/energy, but "due to various limitations (no placebo group, large age variability, and variable disease mutations), no firm conclusions could be made as to efficacy" — and subsequent **preclinical zebrafish and ACTA1(D286G) mouse studies found L-tyrosine treatment does NOT improve skeletal muscle performance**, directly contradicting the earlier anecdotal reports (search synthesis; biorxiv preprint on L-tyrosine in zebrafish/mouse NM models). This is a useful illustration of a therapy that looked promising in case reports but failed a more rigorous preclinical test.

**Investigational/gene-directed approaches (all preclinical):**
- **Cardiac α-actin (ACTC1) over-expression therapy** for dominant ACTA1 disease — leveraging the same rescue biology described in §2/§6 — has been directly tested as a therapeutic strategy in a mouse model of dominant ACTA1 disease ([PMID:23736297](https://pubmed.ncbi.nlm.nih.gov/23736297/), "Cardiac α-actin over-expression therapy in dominant ACTA1 disease").
- A **"Knockdown-and-Replace" (KDAR)** strategy — allele-nonspecific silencing of the mutant/dominant-negative ACTA1 transcript combined with replacement — is in early preclinical development (Rashnonejad et al., Foundation Building Strength-funded program), reflecting the field's recognition that simple gene-addition therapy cannot work against a dominant-negative poison-subunit mechanism (search synthesis; buildingstrength.org).
- AAV-based gene-therapy programs for nemaline myopathy more broadly (Z-disc fragment expression, microRNA-mediated knockdown) have so far been directed at **NEB and TNNT1**, not ACTA1 specifically, and remain in early preclinical stages without demonstrated functional benefit to date ([PMID:34561123](https://pubmed.ncbi.nlm.nih.gov/34561123/), "Recent advances in nemaline myopathy," *Neuromuscul Disord* 2021).
- No ACTA1-specific interventional clinical trial (with an NCT identifier) was identified in this search. Several **natural history studies** are actively recruiting or planned (UK: NCT06670378; Belgium: NCT07201636; Spain: NCT07488806), reflecting trial-readiness-building efforts rather than a therapeutic intervention.

**Treatment outcomes/adverse events:** no systematic pharmacovigilance (FAERS) data specific to ACTA1-directed therapy exist, since none is approved.

---

## 13. Prevention

**Primary prevention** is not possible for de novo dominant disease. For families with an identified dominant or recessive (carrier) pathogenic variant, **genetic counseling** regarding recurrence risk is the principal preventive intervention; empirical de novo recurrence-risk figures (generic, not ACTA1-specific) of ~1–5% (higher with documented parental mosaicism) should be communicated per standard genetic-counseling practice for de novo dominant conditions.

**Secondary prevention/screening:** prenatal diagnosis (CVS/amniocentesis) is available once a familial variant is known; preimplantation genetic testing (PGT-M) is an option for families with an identified pathogenic variant. Population/carrier screening is not standard, given that the great majority of pathogenic variants are private/de novo rather than population-recurrent; carrier screening would only be relevant in known recessive families or high-consanguinity settings.

**Tertiary prevention:** early, proactive multidisciplinary surveillance (respiratory function monitoring, nutritional assessment, scoliosis screening) is explicitly recommended to prevent secondary complications (aspiration pneumonia, malnutrition, progressive respiratory compromise from untreated scoliosis) — "aggressive early management is warranted in most cases" ([PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/)).

**Immunization/public health/prophylaxis:** no disease-specific measures beyond standard pediatric immunization (particularly respiratory pathogens, given the disproportionate respiratory mortality burden) were identified; this is inferred rather than explicitly sourced.

---

## 14. Other Species / Natural Disease

No well-documented, naturally occurring ACTA1-orthologous disease in companion animals, livestock, or wildlife was identified in this search (in contrast to some other neuromuscular genes with recognized veterinary counterparts) — this is flagged as a genuine data gap rather than an assumed absence, since OMIA was not directly queried in this session.

**Orthologs:** mouse *Acta1* (MGI:87902, chromosome 8); zebrafish *acta1a*/*acta1b* (the predominant actin isoforms in fast myofibers). Cross-species conservation of the actin fold is extremely high (skeletal, cardiac, and smooth-muscle actin isoforms are >90% identical), which is itself mechanistically relevant (§2, §6) — cardiac α-actin can substitute functionally for skeletal α-actin in mouse skeletal muscle.

---

## 15. Model Organisms

**Mouse models** — the best-characterized animal system for ACTA1 disease:
- **KI.Acta1(H40Y) knock-in mouse:** heterozygous mice recapitulate the severe human H40Y phenotype with high fidelity — premature lethality, severe muscle weakness, reduced mobility, nemaline rods, and muscle fiber atrophy — mirroring the human patient with this variant, who died at 2 months of age (search synthesis; [PMC10548277](https://pmc.ncbi.nlm.nih.gov/articles/PMC10548277/)).
- **Tg.ACTA1(D286G) transgenic mouse:** overexpresses mutant protein to ~20% of total actin; produces only mild nemaline pathology with minimal behavioral weakness and a normal lifespan, in contrast to the corresponding human patient (who died at 9 months) — an explicit **model-fidelity limitation**: the transgenic overexpression approach under-recapitulates severity relative to the human disease, and the original report is titled as a "cautionary note on muscle transgene expression" for this reason (search synthesis; [PMC3235150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3235150/)).
- Both models have been characterized by in vivo MRI/³¹P-MRS, showing impaired muscle function and altered energy metabolism consistent with the bioenergetic mechanism in §6 ([PMC3629063](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3629063/); [PMC3748127](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3748127/)).
- **Acta1-null (complete knockout) mice** die by 9 days after birth — a very severe phenotype directly analogous to human recessive-null disease — and are rescuable to normal-lifespan survival with no gross skeletal-muscle pathology by transgenic overexpression of cardiac α-actin (ACTC1), providing the mechanistic basis for the compensation hypothesis discussed in §2/§6 ([PMID:19468071](https://pubmed.ncbi.nlm.nih.gov/19468071/)).

**Zebrafish models:** transgenic lines expressing disease-linked dominant mutations (e.g., p.Val165Met) on the endogenous zebrafish *acta1a* fast-fiber actin transcript reproduce myopathic phenotypes — delayed hatching, curved body, reduced touch-evoked escape-response motility by 5 days post-fertilization — with severity correlating to the corresponding human mutation's severity; phalloidin staining confirms actin aggregates, and electron microscopy shows Z-line thickening and myofibrillar disorganization (search synthesis). This model was used to test — and refute — L-tyrosine efficacy (§12).

**Cellular/iPSC models:** ACTA1(H40Y) patient-derived iPSC-differentiated skeletal myocytes display mitochondrial defects, an independent line of evidence supporting the bioenergetic-failure branch of the mechanism ([PMID:36796746](https://pubmed.ncbi.nlm.nih.gov/36796746/)); patient dermal fibroblasts (non-muscle cell type, used as an accessible surrogate) were used to dissect the full actin-polymerization → RhoA/ROCK → mitochondrial-dysfunction chain, including pharmacological reversal with linoleic acid/L-carnitine ([PMC10740811](https://pmc.ncbi.nlm.nih.gov/articles/PMC10740811/)).

**Model limitations, generally:** the D286G transgenic-overexpression mouse under-recapitulates human severity, cautioning against transgene-dosage artifacts; conversely, patient fibroblasts (used for the mitochondrial mechanism) are a non-muscle surrogate cell type, so extrapolation of the RhoA/ROCK/mitochondrial findings to differentiated skeletal myofibers in situ, while independently supported by iPSC-myocyte data, still carries residual translational uncertainty.

No Drosophila or C. elegans ACTA1-orthologous disease model was identified in this search — a data gap, though invertebrate actin structure-function work (e.g., on the unrelated Drosophila indirect-flight-muscle actin gene *Act88F*) exists as a general precedent for actin-mutation biomechanics rather than as a disease model of this gene.

---

## Summary of Key Data Gaps (flagged rather than filled)
- No confirmed Orphanet ORPHA code for the ACTA1-specific NM subtype was retrieved (vs. the general nemaline myopathy entry).
- No ACTA1-specific germline-mosaicism recurrence-risk quantification exists; generic de novo figures were used as a proxy.
- No transcriptomic/proteomic/spatial-omics dataset on ACTA1 patient muscle was located.
- No formal quality-of-life instrument (EQ-5D/SF-36/PROMIS) data specific to this gene were found.
- No documented naturally occurring veterinary/companion-animal ACTA1 disease was found (absence not confirmed against OMIA directly in this session).
- No ACTA1-specific interventional (NCT) clinical trial was identified; only natural-history studies.

---

## Sources
- [OMIM #161800 — Congenital Myopathy 2A](https://omim.org/entry/161800) / [OMIM *102610 — ACTA1](https://omim.org/entry/102610)
- [Severe ACTA1-related nemaline myopathy: intranuclear rods, cytoplasmic bodies, and enlarged perinuclear space (PMC9271256)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271256/)
- [An Update on Reported Variants in the Skeletal Muscle α-Actin (ACTA1) Gene (PMC11918651)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11918651/)
- [Actin Polymerization Defects Induce Mitochondrial Dysfunction in Cellular Models of Nemaline Myopathies (PMC10740811)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10740811/)
- [ACTA1 H40Y mutant iPSC-derived skeletal myocytes — PMID:36796746](https://pubmed.ncbi.nlm.nih.gov/36796746/)
- [Nemaline myopathy: a clinical study of 143 cases — PMID:11558787](https://pubmed.ncbi.nlm.nih.gov/11558787/)
- [Pediatric Nemaline Myopathy: A Systematic Review Using Individual Patient Data (PMC10032635)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10032635/)
- [Retrospective Cohort Analysis of 275 Patients With Nemaline Myopathy — PMID:40661861](https://pubmed.ncbi.nlm.nih.gov/40661861/)
- [Skeletal muscle α-actin diseases (actinopathies): pathology and mechanisms — PMID:22825594](https://pubmed.ncbi.nlm.nih.gov/22825594/)
- [The pathogenesis of ACTA1-related congenital fiber type disproportion — PMID:17387733](https://pubmed.ncbi.nlm.nih.gov/17387733/)
- [Dysfunctional sarcomere contractility in ACTA1-related NEM3 — PMID:29328520](https://pubmed.ncbi.nlm.nih.gov/29328520/)
- [Recessive ACTA1 variant causes congenital muscular dystrophy with rigid spine — PMID:25182138](https://pubmed.ncbi.nlm.nih.gov/25182138/)
- [Rescue of skeletal muscle α-actin–null mice by cardiac (fetal) α-actin — PMID:19468071](https://pubmed.ncbi.nlm.nih.gov/19468071/)
- [Cardiac α-actin over-expression therapy in dominant ACTA1 disease — PMID:23736297](https://pubmed.ncbi.nlm.nih.gov/23736297/)
- [Evidence for a dominant-negative effect in ACTA1 nemaline myopathy — PMID:15198992](https://pubmed.ncbi.nlm.nih.gov/15198992/)
- [Heterogeneity of nemaline myopathy cases with ACTA1 mutations — PMID:15236405](https://pubmed.ncbi.nlm.nih.gov/15236405/)
- [Dilated cardiomyopathy-associated ACTA1 R256H mutation — PMID:38559046](https://pubmed.ncbi.nlm.nih.gov/38559046/)
- [Recent advances in nemaline myopathy — PMID:34561123](https://pubmed.ncbi.nlm.nih.gov/34561123/)
- [Different Mouse Models of Nemaline Myopathy Harboring Acta1 Mutations (PMC10548277)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10548277/)
- [Actin Nemaline Myopathy Mouse Reproduces Disease... (PMC3235150)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3235150/)
- [Nemaline Myopathy-Related ACTA1 D286G Prevents Proper Strong Myosin Binding (PMC3447773)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447773/)
- [Nemaline Myopathy — NORD](https://rarediseases.org/rare-diseases/nemaline-myopathy/)
- [ACTA1 gene — MedlinePlus](https://medlineplus.gov/genetics/gene/acta1)
- [ACTA1 gene assignment to chromosome 1q42.13 — PMID:10072583](https://pubmed.ncbi.nlm.nih.gov/10072583/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 25 |
| On topic | 23 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC3447773` *(abstract only)*: "prevents proper strong myosin binding and triggers muscle weakness"
  - closest text in source: "This phenomenon is likely to prevent proper myosin cross-bridge binding, limiting the fraction of actomyosin interactions in the strong binding state"
- `PMID:15236405` *(abstract only)*: "the marked variability in clinical phenotype among patients with different mutations in ACTA1 suggested that both the site of the mutation and the nature of the amino acid change have differential effects on thin-filament formation and protein-protein interactions"
  - closest text in source: "The skeletal muscle alpha-actin gene (ACTA1) is one of five genes for thin filament proteins identified so far as responsible for different forms of NM"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 11 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001319` (1 mention) - the report calls it "Near-universal in congenital forms"; HP calls it **Neonatal hypotonia**
- `HP:0003324` (1 mention) - the report calls it "Defining feature of "typical" form"; HP calls it **Generalized muscle weakness**
- `HP:0001265` (1 mention) - the report calls it "Common"; HP calls it **Hyporeflexia**
- `HP:0003701` (1 mention) - the report calls it "68% (pediatric systematic review, n=101, PMC10032635)"; HP calls it **Proximal muscle weakness**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002705` (1 mention) - the report calls it "High-arched palate"; HP calls it **High, narrow palate**, and lists "Narrow, high-arched palate" among its other names
- `HP:0002650` (1 mention) - the report calls it "Kyphoscoliosis/scoliosis"; HP calls it **Scoliosis**
- `HP:0001989` (1 mention) - the report calls it "Fetal akinesia/reduced fetal movement"; HP calls it **Fetal akinesia sequence**
- `CL:0000188` (1 mention) - the report calls it "Skeletal muscle fiber"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.