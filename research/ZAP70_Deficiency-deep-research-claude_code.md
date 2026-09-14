---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-09T01:45:37.727426'
end_time: '2026-09-09T01:50:27.965240'
duration_seconds: 290.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ZAP70 Deficiency
  mondo_id: MONDO:0010023
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
  web_search_requests: 12
  num_turns: 18
  total_cost_usd: 1.2673926000000002
  session_id: 26dbdeb2-df8f-5b2c-9949-47091d00d07d
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
citation_count: 19
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:8124727
  quotes_not_checkable: 1
  relevance_assessed: 18
  on_topic: 14
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0010023
    reported_labels:
    - MONDO
    ontology_label: combined immunodeficiency due to ZAP70 deficiency
  - term_id: HP:0005416
    reported_labels:
    - T lymphocytopenia
    ontology_label: Decreased circulating complement factor B concentration
  - term_id: HP:0004791
    reported_labels:
    - Increased CD4:CD8 ratio
    ontology_label: Esophageal ulceration
  - term_id: HP:0002090
    reported_labels:
    - Phenotype (recurrent pneumonia)
    ontology_label: Pneumonia
  - term_id: NCBITaxon:9606
    reported_labels:
    - Homo sapiens
    - Taxonomy of the affected species:** *Homo sapiens
    ontology_label: Homo sapiens
  labels_variant: 6
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
- **Disease Name:** ZAP70 Deficiency
- **MONDO ID:** MONDO:0010023 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ZAP70 Deficiency** covering all of the
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

I'll research ZAP70 Deficiency now using web search and fetch tools, then compile the comprehensive report.

# ZAP70 Deficiency — Comprehensive Research Report

## 1. Disease Information

**Overview.** ZAP70 deficiency (also called ZAP70-related combined immunodeficiency, "Selective T-cell defect," or historically "CD8 lymphopenia due to ZAP-70 deficiency") is a rare **autosomal recessive combined immunodeficiency (CID)** caused by biallelic loss-of-function variants in *ZAP70*, encoding the T-cell receptor (TCR)-proximal tyrosine kinase Zeta-chain-associated protein kinase 70. It was first described in 1994 in three children of Mennonite descent presenting with a SCID-like phenotype but a distinctive immunophenotype: **profoundly reduced/absent CD8+ T cells with normal or elevated CD4+ T cells** (Arpaia et al., PMID: 8124727; Elder et al.). Since then, over 80 affected individuals from >40 families have been reported worldwide (GeneReviews, NBK20221; Sharifinejad et al., 2020, PMID: 32431715).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM | 269840 (Immunodeficiency 48) |
| Gene (OMIM) | *ZAP70*, 176947 |
| MONDO | MONDO:0010023 |
| Orphanet | Combined immunodeficiency due to ZAP70 deficiency (Orphanet Expert/gene page ZAP70) |
| GARD | 387 |
| UMLS | C2931299 |
| ICD-10-CM | D81.8 (Other combined immunodeficiencies) |
| HGNC (gene) | HGNC:7535 |
| Gene location | 2q11.2 |
| GeneReviews | NBK20221 |

**Synonyms:** ZAP-70 deficiency; Selective CD8+ T-lymphocyte deficiency; ZAP70-related combined immunodeficiency; CD8 lymphopenia due to ZAP-70 deficiency; SCID due to ZAP70 deficiency (older, imprecise usage — see below); Immunodeficiency 48.

**Source of information.** Almost all published data derive from **aggregated case reports and case series** (individual patient-level clinical/immunologic/genetic data pooled into systematic reviews), not large-scale EHR/registry-based studies, reflecting the disease's rarity (Sharifinejad et al. 2020 pooled 49 patients from 33 published articles; a 2025 single-center series (PMC12507918) adds further transplant outcome data).

---

## 2. Etiology

**Disease causal factor:** Biallelic (homozygous or compound heterozygous) **loss-of-function or hypomorphic pathogenic variants in *ZAP70*** (HGNC:7535, chr2q11.2) are the sole established cause. There is no known infectious or purely environmental etiology; this is a monogenic inborn error of immunity.

**Genetic risk factors:**
- Autosomal recessive inheritance — biallelic pathogenic variants required.
- **Consanguinity** is a major risk factor: reported in 36.1% (first-degree) and 16.7% (second-degree relative) parental unions among reviewed cases (Sharifinejad et al. 2020).
- **Founder effect:** the intronic variant **c.1624-11G>A** (destabilizing splicing, p.K541_K542insLEQ) is a recurrent founder mutation identified in ~10 unrelated families, overwhelmingly of **Old Order Mennonite** descent from Canada/Pennsylvania (30.6% of the reviewed cohort). Other ethnic enrichments reported include Turkish (22.4%), and Japanese and Caucasian (6.1% each) (Sharifinejad et al. 2020).
- No genome-wide association (GWAS) susceptibility loci are described — this is a Mendelian, fully penetrant disorder rather than a polygenic-risk condition.
- Population allele-frequency databases (gnomAD) do not report an established general-population carrier frequency for ZAP70 pathogenic variants outside the Mennonite founder allele; no genome-wide carrier-frequency study specific to *ZAP70* was identified in this search.

**Environmental risk factors:** None identified as causal. Because affected infants have a profound cellular immunodeficiency, common childhood pathogen exposures (viral, opportunistic) act as **precipitants of clinical presentation** rather than causal agents — see Section 5.

**Protective factors:** None described; there is no evidence of protective alleles at the *ZAP70* locus. The partial functional compensation provided by the paralogous kinase **SYK** in some residual CD8+ T cells (see Mechanism, below) is the closest analog to an endogenous "modifier" — patients whose residual CD8 T cells retain higher SYK expression show somewhat preserved TCR signaling function (Toyabe et al., PMID: 26187144).

**Gene–environment interactions:** Not formally studied; the phenotype is driven overwhelmingly by genotype (loss vs. hypomorphic variant), with infectious/antigenic exposure determining the timing and severity of clinical presentation rather than modifying underlying risk.

---

## 3. Phenotypes

### Immunodeficiency-related (laboratory abnormalities)
| Phenotype | Frequency (Sharifinejad 2020, n=49) | Suggested HPO term |
|---|---|---|
| Decreased CD8+ T-cell count (median 75 cells/µL) | 97.9% | HP:0032219 (Decreased CD8:CD4 ratio) / HP:0005416 (T lymphocytopenia) |
| Normal/elevated CD4+ T cells (median 2,312/µL) | Near-universal | HP:0004791 (Increased CD4:CD8 ratio) |
| Reduced mitogen (PHA) proliferative response | 95% (38/40) | HP:0002846 (Abnormal T cell physiology) |
| Poor polysaccharide vaccine antibody response | 55.6% | HP:0002846 |
| Poor peptide/protein vaccine antibody response | 80% | HP:0002846 |
| Hypogammaglobulinemia / decreased IgG | 27.3% (12/44) | HP:0004315 (Decreased circulating IgG) |
| Decreased IgA | 13.3% | HP:0002720 |
| Decreased IgM | 11.1% | HP:0002850 |
| Hyper-IgM-like phenotype | 13% | HP:0010976 |
| Reduced TREC (T-cell receptor excision circles) | 50% (5/10 tested) | — |

### Clinical/infectious phenotypes
| Phenotype | Frequency | HPO term |
|---|---|---|
| Recurrent respiratory infections | 81.8% | HP:0002205 |
| Pneumonia (recurrent) | 71.4% | HP:0002090 |
| Cutaneous involvement (rash, eczema, ichthyosis, bullous lesions) | 57.9% | HP:0000988 (Skin rash), HP:0000964 (Eczema) |
| Chronic diarrhea | 50% | HP:0002014 |
| Failure to thrive | 43.6% | HP:0001508 |
| Lymphoproliferation / lymphadenopathy | 32.4% | HP:0002716 |
| Hepatomegaly | 19.4% | HP:0002240 |
| ENT infections (otitis media, sinusitis) | 19.4% | HP:0000388 |
| Enteropathy | 18.4% | HP:0002027 |
| Hematologic abnormality (cytopenias, HLH) | 16.7% | HP:0001871 |
| Splenomegaly | 13.9% | HP:0001744 |
| Neurologic abnormality (encephalitis, silent infarcts) | 13.9% | HP:0012638 |
| Autoimmunity (cytopenias, nephritis, bullous pemphigoid, adrenal insufficiency, colitis) | 19.4% | HP:0002960 |
| Malignancy (predominantly EBV-associated lymphoma) | 8.1% | HP:0002664 |

**Infectious agents identified in this cohort:** CMV (29%), Varicella (29%), EBV (12.5%), Rotavirus (4.1%); BCG-related disease (18.4%, reflecting BCG vaccination in endemic settings before diagnosis); *Candida albicans* (28.9%); *Pneumocystis jirovecii* (24.5%).

**Onset, severity, progression:**
- Median age of symptom onset: **4.0 months** (IQR 2.0–7.0); 97.3% present within the first 12 months of life.
- Median diagnostic age: 10.4 months; median diagnostic delay ~5 months.
- Severity is variable — ranging from a **SCID-like presentation in infancy** (initially misdiagnosed as SCID in 73.5% of cases) to **later-onset, milder combined immunodeficiency with prominent immune dysregulation/autoimmunity** in patients with hypomorphic ("leaky") variants.
- Course is **progressive without treatment**: infants presenting with severe infection in the first year typically do not survive past their second year without HSCT (GeneReviews NBK20221).
- Bullous pemphigoid, colitis and nephrotic-range proteinuria have been documented as a severe, uncontrollable autoimmune triad in siblings with ZAP70 deficiency (case report literature).

**Quality of life impact:** Formal EQ-5D/SF-36 data are not available for this ultra-rare disease; qualitatively, untreated disease carries high infection-related morbidity, growth failure, and (in autoimmune-predominant presentations) chronic organ-specific autoimmune disease (skin, gut, kidney) substantially impairing daily function; successful HSCT is associated with resolution of most clinical manifestations and normalization of growth and activity (GeneReviews; Sharifinejad 2020).

---

## 4. Genetic/Molecular Information

**Causal gene:** *ZAP70* (Zeta-chain-associated protein kinase 70; HGNC:7535; NCBI Gene ID 7535; UniProt **P43403**), chromosome **2q11.2**. OMIM gene entry 176947; disease entry 269840.

**Variant spectrum (Sharifinejad et al. 2020; n=49 patients, 41 families, 32 unique variants):**
- Missense: 23 (majority)
- Indel/frameshift: 5
- Splice-site: 3
- Nonsense: 1
- **77.5% homozygous**, 16.3% compound heterozygous.
- Variants occur throughout the gene with **no single dominant hotspot**, though the **majority cluster in the kinase domain**.
- **Founder variant:** c.1624-11G>A (splice-altering, resulting in p.K541_K542insLEQ), the most common single variant, found in ~10 Mennonite families.
- **Newly characterized C-terminal SH2 domain (SH2-C) variants** (Bucciol et al., 2023, PMID: 37313400, DOI:10.3389/fimmu.2023.1155883): p.R170C and p.R192W in four patients. Unlike classical loss-of-expression variants, these preserve ZAP-70 protein expression but **abolish binding of ZAP-70 to phosphorylated TCR-ζ**, causing attenuated TCR-induced ZAP-70 phosphorylation and absent TCR-induced proliferation. Patients with SH2-C variants presented with **combined immunodeficiency plus prominent autoimmunity**, expanding the phenotypic spectrum beyond "classic" kinase-domain loss-of-function disease.

**Variant classification/mechanistic categories (per Sharifinejad et al. 2020):**
1. **Classical/amorphic (36 patients):** abolish protein expression entirely.
2. **Leaky/hypomorphic (5 patients):** allow residual protein expression/function, generally associated with milder or later-onset disease.
3. **Atypical (2 patients):** combined loss-of-function/gain-of-function effects.

**Genotype–phenotype correlation:** The largest systematic review concludes there is **no significant genotype–phenotype correlation** between classical vs. leaky mutation groups or among different mutation types with respect to clinical/laboratory severity — an important caveat for prognostic counseling.

**Population frequency:** No general-population allele-frequency estimate specific to *ZAP70* pathogenic variants was retrievable from gnomAD-based studies in this search; the disease is considered ultra-rare outside the Mennonite founder-variant carrier pool, where regional carrier frequency is elevated due to the founder effect and community endogamy.

**Somatic vs. germline:** ZAP70 deficiency is exclusively a **germline** condition. (Note: *ZAP70* over-expression/dysregulation is separately implicated as a somatic prognostic marker in chronic lymphocytic leukemia — a distinct, unrelated biological context not covered by this deficiency phenotype.)

**Functional consequence:** Predominantly **loss-of-function** (complete or partial loss of kinase activity or TCR-binding capacity). A biologically distinct **gain-of-function** mechanism exists at the same locus but causes a *different* clinical entity (see below) rather than classic deficiency.

**Modifier genes:** *SYK* (the ZAP70 paralog) is the principal identified functional modifier — see Mechanism section.

**Epigenetics / chromosomal abnormalities:** No disease-specific epigenetic marks or chromosomal structural abnormalities (aneuploidy, translocation) have been reported as causal; ZAP70 deficiency is a point-variant/small-indel monogenic disorder.

**Related but distinct entity — ZAP70 gain-of-function (GOF) syndrome:** Disease-associated variants (e.g., **p.R360P**) that *disrupt ZAP-70's autoinhibited conformation* produce a **gain-of-function**, hyperactive kinase that enhances TCR responses to weak/self-ligands, producing an early-onset **familial autoimmune syndrome** distinct from the CD8-lymphopenic deficiency phenotype (Ashouri et al., Immunol Rev 2022, PMID referenced via PMC8986586; Science Signaling scisignal.abc4479). This GOF entity is mechanistically and clinically separate and should not be conflated with classical ZAP70 deficiency in curation, though both illustrate that **either too little or too much ZAP-70 activity** disrupts thymic selection and immune tolerance.

---

## 5. Environmental Information

**Environmental factors:** No toxin, chemical, or radiation exposure is implicated in causing ZAP70 deficiency (it is fully genetic). Environmental/infectious exposures instead act as the **triggers that unmask** the underlying immunodeficiency:
- **BCG vaccination** in BCG-endemic countries has caused disseminated BCG disease in undiagnosed infants (18.4% of the cohort), underscoring the need to avoid live vaccines pending diagnosis.
- **CMV and other congenital/perinatal viral exposure**, including via breastfeeding from a CMV-seropositive mother, is a recognized risk for severe/fatal infection; GeneReviews management explicitly recommends withholding breastfeeding until maternal CMV status is established.
- **Non-irradiated blood products** risk transfusion-associated graft-versus-host disease in these profoundly T-cell-dysfunctional infants.
- Environmental fungal exposure (construction/soil sites) is flagged as an infection-risk in management guidance (invasive fungal disease risk).

**Lifestyle factors:** Not applicable in the classical sense (this is a pediatric-onset monogenic disease); avoidance of crowded/enclosed spaces and infection-control practices are the relevant "behavioral" mitigations pending immune reconstitution.

**Infectious agents (as disease-uncovering/complicating pathogens, not causal agents):**
- Viral: CMV, varicella-zoster virus (including VZV encephalitis), EBV (including EBV-driven lymphoproliferative disease/lymphoma), rotavirus.
- Bacterial: BCG (Mycobacterium bovis vaccine strain) causing disseminated disease.
- Fungal: *Candida albicans*.
- Protozoal/other: *Pneumocystis jirovecii* pneumonia.

These reflect the combined T-cell (CD8-predominant) and humoral functional defect rather than a specific microbial tropism for ZAP70-deficient tissue.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Biallelic pathogenic *ZAP70* variants (2q11.2) → **loss or severe reduction of ZAP-70 kinase activity**, or (for SH2-C domain variants) **loss of ZAP-70's ability to dock on phosphorylated TCR-ζ ITAMs** despite normal protein expression (Bucciol et al. 2023, PMID:37313400).
2. Following TCR engagement, LCK normally phosphorylates the ITAMs of the CD3/TCR-ζ complex; ZAP-70's tandem N- and C-terminal SH2 domains then dock onto these phospho-ITAMs, and LCK-mediated phosphorylation of ZAP-70 Tyr493 (activation loop) plus autophosphorylation activates the kinase. **Loss-of-function or ITAM-binding-defective ZAP-70 breaks this recruitment/activation step**, so downstream phosphorylation of **LAT** and **SLP-76/LCP2** fails to occur (this leads to → step 3).
3. Failure to nucleate the LAT/SLP-76 signalosome **leads to** absent downstream calcium flux, defective PLCγ1 activation, and failure of Ras-MAPK and PKCθ-NF-κB pathway engagement — demonstrated directly in patient T cells as "weak tyrosine phosphorylation signals, no calcium flux, and defective proliferation" (Arpaia et al., PMID:8124727).
4. In the thymus, this TCR-signaling failure **results in** an asymmetric, lineage-selective block: **CD4+CD8+ double-positive (DP) thymocytes fail to complete positive selection into the CD8 single-positive (SP) lineage**, while **CD4 SP maturation proceeds relatively intact** because, as shown in TetZap70-inducible mice, CD4 SP development requires a lower ZAP70 signaling threshold than CD8 SP development (temporal/quantitative threshold model; Science Signaling scisignal.2000702). This step is directly demonstrated in human thymic sections: "CD4+CD8+ cells [are present] in the cortex; however, only CD4, not CD8, single-positive cells are present in the medulla" (GeneReviews NBK20221).
5. This selective failure **leads to** the hallmark peripheral immunophenotype: **profound CD8+ T-lymphopenia with normal/elevated CD4+ T cells** (elevated CD4:CD8 ratio), while B cells and NK cells remain numerically normal (they do not depend on ZAP-70 signaling for development).
6. Residual peripheral CD8+ T cells retain **partial TCR signaling capacity in a subset of patients**, which correlates with expression of the **paralogous kinase SYK**, which can partially substitute for ZAP-70 at the TCR (Toyabe et al., PMID:26187144); this is an inferred compensatory branch rather than a fully demonstrated therapeutic mechanism, and explains inter-patient variability in residual CD8 function independent of genotype.
7. The combined T-cell signaling defect **results in** impaired T-cell help for B-cell antibody responses (poor response to protein/polysaccharide vaccines in 55.6–80% of patients) despite normal B-cell numbers, **leading to** functional (rather than purely quantitative) humoral immunodeficiency and susceptibility to encapsulated-organism and opportunistic infection.
8. Global impairment of TCR-signal-dependent processes (central tolerance during negative selection, peripheral regulatory T-cell function, and lymphocyte homeostatic proliferation) **leads to, in a parallel branch**, loss of self-tolerance and immune dysregulation — manifesting as the autoimmune phenotypes (cytopenias, enteropathy, bullous pemphigoid, nephritis) seen in ~19% of patients, particularly among those with hypomorphic/leaky or SH2-C-domain variants that permit some peripheral T-cell survival with residual but disordered signaling. This branch is *inferred* from the correlation between milder/leaky genotypes and autoimmune-predominant phenotypes rather than fully mechanistically dissected in humans.
9. Unopposed viral antigen exposure (notably EBV) in the setting of defective cytotoxic (CD8+) surveillance **leads to** EBV-driven lymphoproliferative disease and lymphoma in a subset of patients (8.1%), representing a second downstream branch of the CD8 deficiency.

### Molecular pathway/process detail (checklist coverage)
- **Molecular pathway:** TCR proximal signaling cascade (LCK → CD3ζ ITAM phosphorylation → ZAP-70 recruitment/activation → LAT/SLP-76 phosphorylation → PLCγ1/Ras-MAPK/PKCθ-NF-κB). KEGG hsa04660 (T cell receptor signaling pathway) is the relevant reference pathway.
- **Cellular processes affected:** thymocyte positive selection, T-cell activation/proliferation, cytokine production, cytoskeletal reorganization/immunological synapse formation, peripheral T-cell homeostasis.
- **Protein dysfunction:** loss of catalytic (kinase) activity (classical variants) vs. loss of substrate/receptor docking via SH2 domains despite normal expression (SH2-C variants) vs. loss of autoinhibition/gain-of-function (R360P, distinct GOF disease).
- **Immune system involvement:** combined immunodeficiency (T-cell, and secondary antibody-response defect) plus immune dysregulation/autoimmunity — this disease sits at the intersection of immunodeficiency and immune dysregulation, a recognized IUIS category ("combined immunodeficiency with associated/syndromic features" or "diseases of immune dysregulation" depending on presentation).
- **Molecular profiling:** Structural biology (X-ray crystallography) has resolved the **autoinhibited conformation of ZAP-70**, in which interdomain A and interdomain B (the SH2-kinase linker, containing regulatory tyrosines Y315/Y319) pack against the kinase domain's C-lobe to stabilize an inactive state (Deindl et al., Cell 2007, PMID referenced via S0092-8674(07)00455-2). This structural mechanism explains why R360P (in this autoinhibitory interface) causes gain-of-function, while kinase-domain or SH2-domain substitutions elsewhere typically cause loss-of-function.

### Cell types and biological processes (ontology suggestions)
- **Cell types (CL):** CD8-positive, alpha-beta T cell (CL:0000625); CD4-positive, alpha-beta T cell (CL:0000624); double-positive, alpha-beta thymocyte (CL:0000809); naive thymus-derived CD8-positive T cell.
- **Biological processes (GO):** T cell receptor signaling pathway (GO:0050852); positive thymic T cell selection (GO:0045059); positive regulation of alpha-beta T cell activation (GO:0046634); peptidyl-tyrosine phosphorylation (GO:0018108); protein tyrosine kinase activity (GO:0004713).
- **Molecular function:** non-membrane spanning protein tyrosine kinase activity (GO:0004715).

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** Immune system — specifically the **thymus** (site of the developmental block) and **peripheral lymphoid tissue** (lymph node, spleen — site of downstream functional consequences and, when involved, lymphoproliferation).
- **Secondary organ involvement:** Lung/respiratory tract (recurrent pneumonia), skin (rash, eczema, ichthyosis, bullous pemphigoid), gastrointestinal tract (enteropathy, colitis, chronic diarrhea), liver/spleen (hepatosplenomegaly), kidney (nephrotic syndrome, IgA nephropathy in autoimmune-predominant cases), central nervous system (silent infarcts, VZV encephalitis), cardiovascular system (hypertension, atrioventricular block reported in isolated cases).
- **Tissue/cell level:** thymic cortex and medulla (differential involvement — see Mechanism); T-lymphocyte lineage specifically (CD8 SP lineage most affected); epidermal/dermal junction (in bullous pemphigoid, an autoantibody-mediated blistering process).
- **Subcellular level:** the TCR/CD3 immune-synapse signalosome at the plasma membrane; cytoplasmic tyrosine-kinase signaling complex (GO Cellular Component: plasma membrane, T cell receptor complex GO:0042101).
- **Anatomical ontology suggestions (UBERON):** thymus (UBERON:0002370), lymph node (UBERON:0000029), spleen (UBERON:0002106), skin epidermis (UBERON:0001003).
- **Laterality:** Not applicable — systemic/bilateral immune process, not a laterality-defined structural anomaly.

---

## 8. Temporal Development

- **Onset:** Predominantly **infantile**, median 4.0 months of age (IQR 2.0–7.0); congenital susceptibility present from birth, but clinical manifestation is typically delayed until maternal antibody protection wanes and pathogen exposure occurs. A minority present later in childhood or with a milder, immune-dysregulation-predominant phenotype associated with hypomorphic variants.
- **Onset pattern:** Can be acute/severe (SCID-like presentation with life-threatening infection) or insidious (recurrent infections, failure to thrive, gradually apparent autoimmunity).
- **Progression:** Without treatment, disease is **progressive and generally fatal** — patients "usually do not survive past their second year without allogeneic HSCT" (GeneReviews). With HSCT, the disease process is **halted/reversed**, with immune reconstitution and resolution of most clinical manifestations.
- **Disease course pattern:** Predominantly **progressive** in the infectious/immunodeficiency domain; **relapsing-remitting or chronic** in the autoimmune-predominant subgroup (e.g., recurrent bullous pemphigoid flares, chronic enteropathy).
- **Critical period:** The **first year of life** is the critical window both for clinical deterioration (97.3% present within 12 months) and for optimal transplant outcome — post-HSCT complication rates were markedly higher in patients transplanted after 6 months of age (66% of those with complications were >6 months at transplant), arguing for earlier diagnosis/transplant.
- **Remission:** Only via curative HSCT; no spontaneous remission is described. Autoimmune manifestations may respond (partially) to corticosteroids pending definitive therapy (steroid response noted in 5/8 treated patients in the reviewed cohort).

---

## 9. Inheritance and Population

**Epidemiology:** ZAP70 deficiency is an **ultra-rare** disorder; over 80 patients have been reported in the literature since 1994, with no formal population-based prevalence/incidence estimate available (consistent with `prevalence_class: NOT_YET_DOCUMENTED` or an ultra-rare qualitative tier in dismech terms, pending a sourced quantitative estimate). It is one of the recognized causes of T–B+NK+ combined immunodeficiency and accounts for a small minority of SCID/CID newborn-screening referrals.

**Inheritance pattern:** **Autosomal recessive.** Parents of an affected child are obligate heterozygous carriers, typically asymptomatic. For carrier × carrier matings: 25% affected, 50% carrier, 25% unaffected/non-carrier per pregnancy (standard Mendelian AR risk, per GeneReviews).

**Penetrance/expressivity:** Full penetrance is generally assumed for biallelic loss-of-function variants, but **expressivity is highly variable** — ranging from SCID-like infantile presentation to milder, later-onset, autoimmunity-predominant disease — driven at least partly by variant "leakiness" (residual protein expression/function), though no strict genotype-phenotype correlation was established in the largest systematic review.

**Genetic anticipation / germline mosaicism:** Not reported for this disorder (not a repeat-expansion disease).

**Founder effects:** The **c.1624-11G>A** splice variant is a well-documented founder mutation concentrated in the **Old Order Mennonite population** (Pennsylvania/Ontario-derived communities), accounting for the disproportionate representation of Mennonite patients (30.6%) in the literature.

**Consanguinity:** A major contributor — present in over half of reported families (36.1% first-degree, 16.7% second-degree consanguineous unions).

**Population demographics:**
- Ethnic enrichment: Mennonite (30.6%), Turkish (22.4%), Japanese and Caucasian (6.1% each) in the pooled cohort — reflecting both founder effects and consanguinity rates rather than an intrinsic geographic restriction.
- Sex ratio: 27 males : 20 females in the pooled cohort — roughly balanced, consistent with autosomal (non-X-linked) inheritance (no significant sex skew expected or observed).
- Age distribution: Overwhelmingly diagnosed in infancy/early childhood, consistent with onset timing above.
- Family history: Positive family history of similarly affected relatives or early infant deaths reported in 61% of cases, useful as a diagnostic clue in consanguineous or founder populations.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Flow cytometric lymphocyte immunophenotyping** is the key first-line test: markedly reduced/absent CD8+ T cells with normal/elevated CD4+ T cells, normal CD19+ B cells and CD16/56+ NK cells — a distinctive pattern that should immediately raise suspicion for ZAP70 deficiency over classical SCID.
- **Mitogen (PHA) proliferation assay:** markedly reduced in ~95% of patients, reflecting the underlying TCR-signaling defect.
- **Quantitative immunoglobulins** and **specific antibody responses** to protein and polysaccharide vaccine antigens: often abnormal despite normal B-cell counts (functional antibody-response defect).
- **TREC quantification:** can be reduced but is **not a reliable screening test** for this disease (see Screening, below) — reduced in only 50% of tested patients.
- **Functional/research assays:** TCR-induced calcium flux, ZAP-70 protein expression by flow cytometry/immunoblot, and ZAP-70–TCR-ζ co-immunoprecipitation (useful to distinguish classical loss-of-expression variants from SH2-C domain variants that preserve expression but lose TCR binding).

**Genetic testing:**
- **Single-gene *ZAP70* sequencing** is appropriate when the immunophenotype (low CD8, normal CD4) is characteristic, especially in a consanguineous family or Mennonite ancestry.
- **Combined immunodeficiency/SCID gene panels** and **whole-exome/genome sequencing** are used more broadly, particularly when the phenotype is atypical (e.g., autoimmunity-predominant, as in SH2-C domain variant carriers) or family history/ethnicity does not point to *ZAP70* specifically.
- Chromosomal microarray/karyotype are not primary diagnostic tools for this single-gene disorder but may be used to exclude syndromic/chromosomal differentials.

**Screening:**
- **Newborn TREC-based SCID screening has a documented limitation for ZAP70 deficiency:** "a substantial number of infants with ZAP70 deficiency have TREC levels above the lower levels used for newborn screening... TREC screening does not sufficiently identify these patients" and "has not been frequently picked up during >10 year screening experience in the United States" (Kwan et al., PMID:24797280; Sharifinejad et al. 2020). This reflects that thymic *output* (captured by TREC) can appear relatively preserved because CD4 SP thymocyte production continues even though CD8 SP maturation fails.
- The key **early, more sensitive laboratory clue is a low absolute CD8+ T-cell count**, which precedes/parallels rather than depends on TREC decline.
- Targeted screening (flow cytometry, and/or *ZAP70* sequencing) is recommended for newborns with consanguineous parents, a positive family history of CID, or from high-prevalence founder populations (e.g., Mennonite communities), and for any infant with low CD8 counts identified incidentally.
- **Carrier/prenatal/preimplantation genetic testing** is available once a familial pathogenic variant is identified, particularly relevant for at-risk consanguineous families and Mennonite communities with the known founder allele.

**Differential diagnosis (key distinguishing features):**
| Disorder | Distinguishing feature vs. ZAP70 deficiency |
|---|---|
| X-linked SCID (IL2RG) | Affects males only; combined T AND NK cell deficiency (vs. normal NK in ZAP70 deficiency) |
| ADA deficiency | Profound T, B, AND NK lymphopenia; neurologic/skeletal findings |
| Familial/isolated CD8 deficiency (e.g., LCK deficiency) | Milder course; increased double-negative T cells; opportunistic infections and SCID-like presentation uncommon |
| MHC class I deficiency (TAP/TAPBP) | Later onset, milder respiratory presentation, low CD8 via a different (antigen-presentation) mechanism |
| RAG1/RAG2 deficiency | Low T AND B cell counts (vs. normal B cells in ZAP70 deficiency) |

---

## 11. Outcome/Prognosis

**Survival/mortality (pooled cohort, Sharifinejad et al. 2020, n=49):**
- Overall mortality: **23.9%** (11/49); overall survival at time of report: 76.1%.
- **HSCT recipients:** 88–91.7% survival (22/25 alive at median 36-month follow-up in the pooled review); a separate long-term single-center study (Journal of Clinical Immunology, PMID:27438785) reported **8/8 (100%) alive at a median 13.5-year follow-up**, and a 2025 single-center series (PMC12507918) reported 8/11 (73%) alive at median 7-year follow-up.
- **Non-transplanted patients:** substantially worse survival — 59.1% (13/22) alive at median 18-month follow-up.
- **Statistical comparison:** Kaplan-Meier analysis showed HSCT significantly reduced mortality (p<0.001).
- **Causes of death:** acute respiratory distress, CMV pneumonitis, multiorgan failure from hemophagocytic lymphohistiocytosis, disseminated intravascular coagulation, recurrent apnea/breathing arrest, and cardiac atrioventricular block.

**Morbidity/complications:**
- Post-HSCT graft-versus-host disease: 36% (9 patients).
- Post-HSCT infections: 16% (4 patients).
- Age at transplant is a key prognostic factor: complications were concentrated (66%) in patients transplanted after 6 months of age, supporting early diagnosis and transplantation.
- Second HSCT required in a subset (3 patients in the pooled cohort) for graft failure.

**Quality-of-life/functional outcome:** Successful HSCT is associated with excellent long-term immune reconstitution and resolution of infectious and (generally) autoimmune manifestations; no dedicated validated QoL instrument data (EQ-5D/SF-36/PedsQL) specific to ZAP70 deficiency were identified in this search.

**Prognostic factors:** HSCT status (curative vs. not) is the dominant prognostic determinant; age at transplantation (<6 months preferred); myeloablative conditioning is associated with more robust, durable immune reconstitution than reduced-intensity/unconditioned approaches, though the latter remain life-saving options in critically ill patients. **No reliable genotype-based prognostic marker exists** (no genotype-phenotype correlation established).

---

## 12. Treatment

**Curative therapy:**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** is the only curative treatment (NCIT:C15431, Hematopoietic Stem Cell Transplantation). Successful outcomes have been reported with:
  - **Donor sources:** HLA-matched sibling donors (61.9% of transplanted patients in the pooled review), matched unrelated donors (38.1%), and, per GeneReviews, haploidentical donors and unrelated umbilical cord blood.
  - **Stem cell sources:** bone marrow (68%), peripheral blood stem cells (20%), cord blood (12%).
  - **Conditioning regimens reported as successful:** busulfan/cyclophosphamide; busulfan/fludarabine/anti-thymocyte globulin; melphalan/fludarabine/anti-thymocyte globulin; myeloablative regimens are associated with more robust and durable engraftment, while reduced-intensity or unconditioned transplant (e.g., matched sibling donor without conditioning) is a viable life-saving option in critically ill infants with active infection/end-organ damage.

**Investigational/advanced therapeutics:**
- **Gene therapy** (NCIT:C15238) has not reached clinical application for ZAP70 deficiency but has strong preclinical proof-of-concept: retroviral transduction of primary ZAP-70-deficient human T cells restores a selective growth/functional advantage to gene-corrected cells (Nature Gene Therapy, "Retrovirus-mediated transduction..."), and **direct intrathymic injection of a T-cell-specific lentiviral vector encoding ZAP70** achieved long-term differentiation of mature TCR-αβ+ thymocytes with a partially diversified receptor repertoire in a mouse model, even without conditioning (JCI, "In vivo correction of ZAP-70 immunodeficiency by intrathymic gene transfer"). These approaches are proposed as a potentially safer alternative to ex vivo gene-modified HSCT but remain preclinical.

**Pharmacotherapy and supportive care:**
- **Immunoglobulin replacement therapy (IVIG)** (NCIT:C15986, Pharmacotherapy) — used even in patients with normal quantitative immunoglobulin levels, given the demonstrated functional antibody-response defect; used in 36.7% of the HSCT-treated subgroup in the pooled cohort as peri-transplant supportive care.
- **Anti-infective prophylaxis:** antibacterial, antifungal, antiviral, and anti-*Pneumocystis jirovecii* prophylaxis (NCIT:C15747, Supportive Care).
- **Corticosteroids** (NCIT:C2977, Corticosteroid) for autoimmune manifestations — used in 32% (8/25) of the HSCT-treated subgroup, with clinical response documented in 5 patients.
- **Blood product precautions:** only irradiated, leukoreduced, CMV-safe blood products, given risk of transfusion-associated GVHD in profoundly T-cell-dysfunctional hosts.
- **Vaccination precautions:** avoidance of live viral vaccines (for the patient and household contacts) until immune reconstitution is confirmed post-HSCT.

**Treatment strategy/algorithm:** Early recognition (low CD8 flow cytometry pattern) → confirmatory genetic testing → supportive care (IVIG, anti-infective prophylaxis, avoidance of live vaccines/non-irradiated blood/unpasteurized breast milk of CMV+ status unknown) → expedited HSCT, ideally before 6 months of age and before onset of significant end-organ damage or refractory autoimmune disease → post-transplant surveillance every 6–12 months for engraftment, immune reconstitution, growth, and resolution of organ involvement.

**Experimental treatments:** No registered ClinicalTrials.gov interventional trials specific to ZAP70 deficiency gene therapy were identified in this search; management is currently guided by HSCT case series and expert consensus (GeneReviews) rather than randomized trial data, consistent with the disease's rarity.

**Personalized/genotype-guided approaches:** Not currently established, given the absence of genotype-phenotype correlation; treatment decisions are guided by clinical severity and immunophenotype rather than specific variant class.

---

## 13. Prevention

- **Primary prevention:** Not possible in the traditional sense (monogenic AR disease); the closest analog is **carrier screening and genetic counseling** in high-risk populations (e.g., Mennonite communities carrying the c.1624-11G>A founder allele) and in consanguineous unions, enabling informed reproductive decision-making.
- **Secondary prevention (early detection):** Population/targeted **newborn screening** — with the important caveat that standard TREC-based SCID newborn screening has documented sensitivity limitations for ZAP70 deficiency; **targeted lymphocyte immunophenotyping (CD8 count) or gene-panel testing** is more sensitive in high-risk families/populations. Early diagnosis materially improves outcomes by enabling HSCT before 6 months of age.
- **Tertiary prevention (avoiding complications in affected individuals):** Anti-infective prophylaxis, avoidance of live vaccines, use of irradiated/CMV-safe blood products, and avoidance of high fungal-spore-exposure environments (construction/soil) — all aimed at preventing infectious complications while awaiting or after HSCT.
- **Immunization:** Live vaccines (e.g., BCG, MMR, varicella, oral polio) are contraindicated pre-transplant in affected infants and in household contacts of undiagnosed at-risk infants in endemic/founder communities; **BCG-endemic country vaccination practices are a recognized real-world hazard**, given the 18.4% rate of BCG-related disease in the reviewed cohort.
- **Genetic counseling:** Recommended for all families with an affected child or a known carrier, discussing autosomal recessive inheritance, 25% recurrence risk, and availability of prenatal/preimplantation genetic diagnosis once the familial variant is known.
- **Public health/screening program considerations:** Because of the TREC-screening blind spot, public health newborn-screening programs in populations with elevated ZAP70 deficiency prevalence (e.g., Mennonite communities) may warrant supplementary CD8-lymphocyte-based or gene-panel screening strategies — a recommendation made explicitly in the primary literature (Kwan et al., PMID:24797280).

---

## 14. Other Species / Natural Disease

- **Taxonomy of the affected species:** *Homo sapiens* (NCBITaxon:9606) is the only species in which naturally-occurring ZAP70 deficiency disease has been reported; no naturally occurring veterinary/companion-animal ZAP70-deficiency disease was identified in this search (no OMIA entry found).
- **Orthologous gene:** *Zap70* is highly conserved; mouse ortholog **Zap70** (MGI:99613, NCBI Gene ID 22637) is the primary basis for engineered (not naturally occurring) animal models — see Model Organisms below.
- **Comparative biology:** The TCR-proximal signaling role of ZAP-70/Syk-family kinases is evolutionarily conserved across jawed vertebrates; mouse studies of *Zap70*-null and hypomorphic alleles closely recapitulate the human developmental block, although with species-specific quantitative differences in the CD4/CD8 selection threshold (see Mechanism/Model organisms sections) — illustrating strong mechanistic conservation but imperfect one-to-one phenotype transfer.
- **Zoonotic potential/transmission:** Not applicable — this is a non-infectious, monogenic disorder.

---

## 15. Model Organisms

**Genetic mouse models** (Alliance of Genome Resources; MGI):
- **Zap70 knockout (Zap70−/−) mice:** T-cell development is arrested at the **CD4+CD8+ double-positive (DP) thymocyte stage**, with a complete absence of mature T cells in peripheral lymphoid organs and blood — closely paralleling (though more completely blocking than) the human phenotype, in which some CD4 SP maturation does occur.
- **TetZap70 (tetracycline-inducible Zap70) mice:** Allow controlled re-induction of Zap70 expression in a null background, revealing that CD4 SP thymocytes develop faster and require a **lower ZAP70 signaling threshold** than CD8 SP thymocytes — the key mechanistic model explaining the human selective CD8 lymphopenia (Science Signaling, scisignal.2000702).
- **Zap70/Syk double-knockout mice:** T-cell development is blocked even earlier, at the double-negative (DN) to DP transition — demonstrating that **Syk provides partial redundant function** sufficient to permit progression past the DN stage in Zap70-single-knockout mice (Cheng et al., PMID:9324357; restoration of thymocyte development by ectopic Syk expression in zap-70−/− mice).
- **Point-mutant "knock-in" mice** at regulatory tyrosines (Y292, Y315) recapitulate specific aspects of altered TCR signaling and thymocyte selection, informing structure-function understanding of interdomain B autoinhibition (J Exp Med, rupress.org/jem/article/194/4/491).
- **Hypomorphic ZAP70 mouse models (e.g., "SKG" strain carrying a W163C hypomorphic mutation)** reveal a distinct threshold effect: partial ZAP70 loss-of-function can produce **spontaneous autoimmune arthritis** rather than immunodeficiency, by skewing thymic selection toward an arthritogenic self-reactive TCR repertoire and impairing Treg development/function (PMC2768860) — directly relevant to understanding the human hypomorphic/leaky variant autoimmune-predominant phenotype.
- **R360P gain-of-function knock-in models** recapitulate the distinct autoimmune (rather than immunodeficient) phenotype produced by disrupted ZAP-70 autoinhibition, altering thymic negative selection and Treg development (Ashouri et al. 2022; Science Signaling scisignal.abc4479).

**Model characteristics — phenotype recapitulation and limitations:**
- Mouse Zap70-null models **faithfully recapitulate the DP-stage block and T-cell signaling failure**, and the TetZap70 system specifically **explains the human CD4-vs-CD8 selective vulnerability**, making mouse models highly informative for mechanism.
- **Limitation:** complete Zap70-null mice show a more absolute block (no peripheral T cells at all) than most human patients, who typically retain low but present peripheral CD8 T cells and largely intact CD4 T-cell compartments — likely reflecting species differences in the stringency of the CD4/CD8 selection threshold and/or Syk compensation dynamics, and underscoring that mouse models better model the "complete loss" end of the human variant spectrum than the hypomorphic/leaky end (which is better modeled by hypomorphic knock-in strains such as SKG).
- **Applications:** mouse models have been used to study thymocyte selection thresholds, test intrathymic lentiviral gene-therapy correction strategies (with restoration of a diversified, alloantigen-responsive T-cell repertoire), and dissect the distinct GOF-driven autoimmune-arthritis pathway.

**Resources:** MGI (Mouse Genome Informatics) Zap70 gene page; Alliance of Genome Resources; IMPC/KOMP for conditional/humanized allele availability.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease | MONDO:0010023; OMIM:269840 |
| Gene | hgnc:7535 (ZAP70) |
| Phenotype (CD8 lymphopenia) | HP:0005416 (T lymphocytopenia) / consider CD8-specific descriptor |
| Phenotype (recurrent pneumonia) | HP:0002090 |
| Phenotype (bullous pemphigoid) | relevant HP/NCIT term for autoimmune blistering skin disease |
| Phenotype (failure to thrive) | HP:0001508 |
| Biological process | GO:0050852 (T cell receptor signaling pathway); GO:0045059 (positive thymic T cell selection) |
| Molecular function | GO:0004713 / GO:0004715 (protein tyrosine kinase activity) |
| Cell types | CL:0000625 (CD8+ alpha-beta T cell); CL:0000624 (CD4+ alpha-beta T cell); CL:0000809 (DP thymocyte) |
| Anatomy | UBERON:0002370 (thymus) |
| Treatment (HSCT) | NCIT:C15431 |
| Treatment (IVIG) | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent (immunoglobulin) |
| Treatment (gene therapy, investigational) | NCIT:C15238 |

---

## Sources

- [Clinical, Immunological, and Genetic Features in 49 Patients With ZAP-70 Deficiency: A Systematic Review (PMC7214800)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7214800/) — Sharifinejad et al., Front Immunol 2020;11:831, PMID: 32431715
- [ZAP70 Deficiency / ZAP70-Related Combined Immunodeficiency — GeneReviews (NBK20221)](https://www.ncbi.nlm.nih.gov/books/NBK20221/)
- [Combined immunodeficiency caused by pathogenic variants in the ZAP70 C-terminal SH2 domain (PMC10258307)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10258307/) — Bucciol et al., Front Immunol 2023, PMID: 37313400
- [Clinical, immunological, molecular characteristics and outcomes of stem cell transplantation in ZAP70 deficiency: a single-center experience (PMC12507918)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507918/), PMID: 41080547
- [Long-Term Outcomes of Hematopoietic Stem Cell Transplantation for ZAP70 Deficiency — J Clin Immunol](https://link.springer.com/article/10.1007/s10875-016-0316-z), PMID: 27438785
- [Defective T cell receptor signaling and CD8+ thymic selection in humans lacking zap-70 kinase — PubMed](https://pubmed.ncbi.nlm.nih.gov/8124727/) (Arpaia et al., 1994)
- [SYK expression endows human ZAP70-deficient CD8 T cells with residual TCR signaling — PubMed](https://pubmed.ncbi.nlm.nih.gov/26187144/) (Toyabe et al.)
- [Restoration of thymocyte development and function in zap-70-/- mice by the Syk protein tyrosine kinase — PubMed](https://pubmed.ncbi.nlm.nih.gov/9324357/)
- [Regulation of Zap70 Expression During Thymocyte Development Enables Temporal Separation of CD4 and CD8 Repertoire Selection — Science Signaling](https://www.science.org/doi/abs/10.1126/scisignal.2000702)
- [A hypomorphic allele of ZAP-70 reveals a distinct thymic threshold for autoimmune disease versus autoimmune reactivity (PMC2768860)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2768860/), PMID: 19841086
- [ZAP70, too little, too much can lead to autoimmunity — Immunological Reviews (PMC8986586)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8986586/)
- [A disease-associated mutation that weakens ZAP70 autoinhibition enhances responses to weak and self-ligands — Science Signaling](https://www.science.org/doi/10.1126/scisignal.abc4479)
- [Structural Basis for the Inhibition of Tyrosine Kinase Activity of ZAP-70 — Cell](https://www.cell.com/fulltext/S0092-8674(07)00455-2)
- [Limitation of TREC-based newborn screening for ZAP70 Severe Combined Immunodeficiency — PubMed](https://pubmed.ncbi.nlm.nih.gov/24797280/) (Kwan et al.)
- [In vivo correction of ZAP-70 immunodeficiency by intrathymic gene transfer — JCI](https://www.jci.org/articles/view/23966)
- [Retrovirus-mediated transduction of primary ZAP-70-deficient human T cells... — Gene Therapy (Nature)](https://www.nature.com/articles/3301249)
- [ZAP70 Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ZAP70)
- [Orphanet: Combined immunodeficiency due to ZAP70 deficiency](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=911&lng=EN)
- [ZAP-70 deficiency — Immune Deficiency Foundation](https://primaryimmune.org/understanding-primary-immunodeficiency/types-of-pi/zap-70-deficiency)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 18 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:8124727` *(abstract only)*: "weak tyrosine phosphorylation signals, no calcium flux, and defective proliferation"
  - closest text in source: "Peripheral CD4+ T cells from the zap-70-/- patients exhibit markedly reduced tyrosine phosphorylation, fail to produce interleukin-2, and do not proliferate in response to T cell receptor stimulation by mitogens or antigens"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:24797280`: "has not been frequently picked up during >10 year screening experience in the United States"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 13 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010023` (2 mentions) - the report calls it "MONDO"; MONDO calls it **combined immunodeficiency due to ZAP70 deficiency**
- `HP:0005416` (2 mentions) - the report calls it "T lymphocytopenia"; HP calls it **Decreased circulating complement factor B concentration**
- `HP:0004791` (1 mention) - the report calls it "Increased CD4:CD8 ratio"; HP calls it **Esophageal ulceration**
- `HP:0002090` (2 mentions) - the report calls it "Phenotype (recurrent pneumonia)"; HP calls it **Pneumonia**
- `NCBITaxon:9606` (1 mention) - the report calls it "Homo sapiens", "Taxonomy of the affected species:** *Homo sapiens"; NCBITaxon calls it **Homo sapiens**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002846` (3 mentions) - the report calls it "Abnormal T cell physiology"; HP calls it **Abnormal B cell morphology**
- `HP:0004315` (1 mention) - the report calls it "Decreased circulating IgG"; HP calls it **Decreased circulating IgG concentration**, and lists "Decreased circulating IgG level" among its other names
- `HP:0001508` (2 mentions) - the report calls it "Phenotype (failure to thrive)"; HP calls it **Failure to thrive**, and lists "Postnatal failure to thrive" among its other names
- `GO:0004715` (2 mentions) - the report calls it "Molecular function:** non-membrane spanning protein tyrosine kinase activity"; GO calls it **non-membrane spanning protein tyrosine kinase activity**
- `NCIT:C15431` (2 mentions) - the report calls it "Treatment (HSCT)"; NCIT calls it **Hematopoietic Cell Transplantation**, and lists "HSCT" among its other names
- `NCIT:C15238` (2 mentions) - the report calls it "Gene therapy", "Treatment (gene therapy, investigational)"; NCIT calls it **Gene Therapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15238` - called "Gene therapy", "Treatment (gene therapy, investigational)"
- `NCBITaxon:9606` - called "Homo sapiens", "Taxonomy of the affected species:** *Homo sapiens"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `OMIM`.