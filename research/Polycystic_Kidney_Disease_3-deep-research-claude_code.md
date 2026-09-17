---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-29T00:21:04.473925'
end_time: '2026-08-29T00:32:55.718704'
duration_seconds: 711.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Polycystic Kidney Disease 3
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
  - claude-opus-5[1m]
  web_search_requests: 13
  num_turns: 45
  total_cost_usd: 3.893259500000002
  session_id: d4ba898e-a267-4dcb-80fc-796f0fe13269
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 1
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
citation_count: 23
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 27
  on_topic: 20
  validator_version: 0.2.1
term_validation:
  total_terms: 58
  verified: 56
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 27
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Polycystic Kidney Disease 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Polycystic Kidney Disease 3** covering all of the
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

# Research Report — Polycystic Kidney Disease 3 (PKD3; GANAB-related ADPKD/ADPLD)

**Prepared:** 2026-08-29 · **Target MONDO:** `MONDO:0010916` (verified present in this repo's MONDO cache, `cache/mondo/terms.csv:1662`) · **Category:** Mendelian

---

## ⚠️ Scope note — read before curating

**Two things are called "PKD3," and only one of them is this entry.**

1. **The historical, unmapped third locus.** In 1995 two groups reported ADPKD families that excluded linkage to both *PKD1* (16p13.3) and *PKD2* (4q21): Daoust et al. in a French-Canadian family (Genomics 1995;25:733–6, [PMID:7759112](https://pubmed.ncbi.nlm.nih.gov/7759112/)) and de Almeida et al. in a Portuguese family (Hum Genet 1995, [PMID:7607660](https://pubmed.ncbi.nlm.nih.gov/7607660/)). OMIM created **600666 "PKD3"** for this putative locus. It was never mapped, and several apparent "PKD3" pedigrees were later re-explained as bilineal *PKD1* + *PKD2* disease.
2. **GANAB-related ADPKD/ADPLD.** In 2016 Porath et al. identified *GANAB* (11q12.3) mutations in ADPKD- and ADPLD-affected families, and OMIM 600666 was re-purposed as **"POLYCYSTIC KIDNEY DISEASE 3 WITH OR WITHOUT POLYCYSTIC LIVER DISEASE; PKD3,"** gene *GANAB*. This is what `MONDO:0010916` denotes and is the subject of this report.

**Curation consequence:** pre-2016 literature using "PKD3" is about the unmapped locus and must **not** be cited as evidence for this entry. Additionally, the field's own preferred designation is now **"ADPKD-GANAB"** (Cornec-Le Gall, Torres & Harris, JASN 2018) rather than "PKD3" — worth recording as a synonym-with-caveat.

**Second scope decision the curator must make:** the design-decision question of whether this is a `DISEASE` entry or a `SUBTYPE` of `Autosomal_Dominant_Polycystic_Kidney_Disease` (which already exists in `kb/disorders/`, alongside `Polycystic_Kidney_Disease_2.yaml` and `Autosomal_Dominant_Polycystic_Liver_Disease.yaml`). The evidence below supports a separate entry on the grounds of a **distinct molecular mechanism** (ER glucosidase II, not the polycystin complex itself) and a **distinct clinical trajectory** (mild kidney disease, liver-dominant in many carriers), but note it straddles the ADPKD/ADPLD boundary in a way the existing three entries do not.

---

## 1. Disease Information

### Overview

PKD3 is an autosomal dominant cystic disease of the kidney and liver caused by heterozygous loss-of-function or hypomorphic variants in ***GANAB***, which encodes the **α subunit of glucosidase II (GIIα)**, a heterodimeric endoplasmic reticulum enzyme that trims glucose residues from N-linked glycans during glycoprotein quality control. GIIα is required for the maturation, surface delivery, and ciliary localization of **polycystin-1 (PC1)**. PKD3 is therefore not a polycystin gene disease but a **polycystin-biogenesis** disease: the cystogenic endpoint is the same as classical ADPKD, reached one step upstream.

The clinical presentation is bimodal and, within families, highly variable:

- a **mild polycystic kidney phenotype** — few large cysts, preserved kidney function into late life, kidney failure rare or absent — often with liver cysts; **or**
- a **severe isolated polycystic liver disease (ADPLD)** phenotype with few or no kidney cysts, occasionally requiring liver transplantation.

The same allele can produce either. Delbarba et al. reported a family in which the *p.Arg839Trp* variant caused mild ADPKD, while the same variant had previously been reported in a patient with ADPLD severe enough to require liver transplant ([PMID:34357571](https://pubmed.ncbi.nlm.nih.gov/34357571/)).

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | `MONDO:0010916` — polycystic kidney disease 3 with or without polycystic liver disease ✅ verified in repo cache |
| **OMIM (phenotype)** | 600666 — POLYCYSTIC KIDNEY DISEASE 3 WITH OR WITHOUT POLYCYSTIC LIVER DISEASE; PKD3 |
| **OMIM (gene)** | 104160 — GLUCOSIDASE, ALPHA, NEUTRAL AB; GANAB |
| **HGNC** | `hgnc:4138` (GANAB) ✅ verified via genenames.org REST |
| **UniProt** | Q14697 (GANAB_HUMAN, neutral α-glucosidase AB) |
| **NCBI Gene / Ensembl** | 23193 / ENSG00000089597 |
| **RefSeq (canonical)** | NM_198334 |
| **Cytoband** | 11q12.3 |
| **MeSH** | D016891 *Polycystic Kidney, Autosomal Dominant* (no PKD3-specific MeSH term exists) |
| **ICD-10** | Q61.2 *Polycystic kidney, autosomal dominant* (no gene-specific code) |
| **ICD-11** | GB81.0 *Autosomal dominant polycystic kidney disease* — ⚠️ **verify in the current ICD-11 browser before binding** |
| **Orphanet** | No dedicated ORPHA code for GANAB-ADPKD was found. Nearest: ORPHA:730 (ADPKD), ORPHA:2924 (isolated polycystic liver disease). ⚠️ **verify** |

### Synonyms and alternative names

- ADPKD-GANAB *(the preferred contemporary designation; Cornec-Le Gall et al. 2018)*
- GANAB-related autosomal dominant polycystic kidney disease
- Polycystic kidney disease 3 with or without polycystic liver disease
- PKD3
- GANAB-related polycystic liver disease
- Glucosidase IIα-deficiency polycystic disease *(descriptive, not standard)*

⚠️ **Do not** list "polycystic kidney disease, type III (unmapped locus)" as a synonym without the historical caveat above.

### Nature of the evidence base

**Entirely aggregated disease-level and case-level literature.** There is no EHR-derived cohort, no registry, and no natural-history study specific to GANAB. The total published experience is on the order of **~30–40 families worldwide**. The evidence base is:

- one gene-discovery study with functional validation (Porath 2016, n = 20 affected individuals / 9 families)
- one ADPLD gene-discovery study (Besse 2017)
- one targeted cohort screen (van de Laarschot 2020, 625 patients)
- a scattering of single-family and single-case reports
- one population-sequencing prevalence estimate (Lanktree 2018)

Every quantitative claim below should be read against that denominator.

---

## 2. Etiology

### Primary cause

Heterozygous germline variants in **GANAB**. The mechanism is **haploinsufficiency / partial loss of glucosidase IIα function**, with a probable requirement for a somatic or stochastic second hit at the tissue level (the standard ADPKD two-hit / dosage-threshold framework).

> "Whole-exome sequencing of six GUR ADPKD-affected families identified one with a missense mutation in GANAB, encoding glucosidase II subunit α (GIIα). Because PRKCSH encodes GIIβ, GANAB is a strong ADPKD and ADPLD candidate gene."
> — Porath et al., *Am J Hum Genet* 2016;98:1193–1207. [PMID:27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/), doi:10.1016/j.ajhg.2016.05.004

The candidate-gene logic is worth capturing in the entry: *PRKCSH*, the long-established isolated-PCLD gene (PCLD1, OMIM 174050), encodes the **β subunit** of the very same glucosidase II heterodimer. GANAB was pursued because its partner was already a cystic-disease gene.

### Genetic risk factors

- **Causal variants:** heterozygous *GANAB* truncating (nonsense, frameshift, canonical splice) and hypomorphic missense variants. See §4.
- **Trans-heterozygous / oligogenic modification:** the strongest recurring theme in the ADPKD-spectrum literature. Cornec-Le Gall et al. state:
  > "Recent data have shown that biallelic disease including at least one weak ADPKD allele is a significant cause of symptomatic, very early onset ADPKD."
  > — *J Am Soc Nephrol* 2018;29:13–23. [PMID:29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/), doi:10.1681/ASN.2017050483

  A worked instance: a 12-year-old girl with bilateral renal cysts and nephrolithiasis carrying a *GANAB* nonsense variant (`c.181C>T`, p.Arg61*) **and** a *PKD1* VUS (`c.182C>T`, p.Pro61Leu) — reported as the first pediatric case combining PKD1 and GANAB variants ([PMC6375066](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6375066/)).
- **Modifier loci:** unidentified for GANAB specifically. Lanktree et al. found substantial rare variation in candidate cyst-modifier genes at population scale (see §9), but no GANAB-specific modifier has been mapped.
- **Sex:** female sex is a well-established risk factor for **severe liver cystic disease** across all PLD genes (see §9); whether it modifies the kidney phenotype in GANAB carriers is unknown.

### Environmental risk factors

**No GANAB-specific environmental risk factor has been identified.** Extrapolating from the ADPKD literature (label these clearly as ADPKD-general if used):

- Estrogen exposure (endogenous, pregnancy, exogenous HRT/oral contraceptives) — accelerates hepatic cystogenesis; the standard clinical advice is estrogen avoidance in symptomatic PLD.
- High dietary sodium, low water intake / high circulating vasopressin — associated with faster kidney disease progression in ADPKD.
- Smoking, caffeine, obesity — variably reported ADPKD progression associations, none established for GANAB.

### Protective factors

- **Genetic:** none identified. There is no reported protective allele or modifier.
- **Environmental:** none GANAB-specific. High water intake (vasopressin suppression) and salt restriction are plausible-by-mechanism but unproven in ADPKD generally and untested in GANAB.

### Gene–environment interaction

**No data.** ⚠️ Not available for this disease. The mechanistically obvious hypothesis — that vasopressin/cAMP tone modulates the penetrance of a partial polycystin-1 deficit — is untested in GANAB carriers and should be recorded as a `KNOWLEDGE_GAP` discussion rather than asserted.

---

## 3. Phenotypes

### Kidney phenotypes

| Phenotype | HPO lead ⚠️ | Frequency / severity | Onset | Course |
|---|---|---|---|---|
| Multiple bilateral renal cysts | `HP:0005562` Multiple renal cysts | Near-universal in ADPKD-presenting families; **few, large** cysts rather than innumerable small ones | Adult; some childhood cases | Slowly progressive |
| Renal cyst | `HP:0000107` Renal cyst | — | — | — |
| Polycystic kidney dysplasia | `HP:0000113` | Atypical / Mayo class 2 morphology common for minor ADPKD genes | Adult | — |
| Hypertension | `HP:0000822` | ~40% of families in Porath 2016; onset typically 35–55 y | Adult | Chronic |
| Renal insufficiency | `HP:0000083` | **Uncommon** — the defining feature of the genotype | Late, if at all | Slow |
| Stage 5 CKD / kidney failure | `HP:0003774` | **Not reported** in the Porath cohort; ESKD is the exception, not the rule | Late | — |
| Hematuria | `HP:0000790` | Reported (Delbarba family) | Adult | Episodic |
| Nephrolithiasis | `HP:0000787` | Reported in individual cases | Variable | Episodic |
| Flank / abdominal pain | `HP:0030157` / `HP:0002027` ⚠️ | Reported | Adult | Episodic |

The kidney phenotype is the single most consistent descriptive claim in the literature:

> "The phenotype was mild PKD and variable, including severe, PLD."
> — Porath et al. 2016, [PMID:27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/)

> GANAB pathogenic variants cause "mild cystic kidney disease, usually without a decline in kidney function, with the majority of affected individuals having liver cysts."
> — *GeneReviews*, Polycystic Kidney Disease, Autosomal Dominant ([NBK1246](https://www.ncbi.nlm.nih.gov/books/NBK1246/))

**⚠️ The mildness claim is now formally contested.** A 2025 case report describes an 18-year-old with a GANAB variant and Mayo Imaging Classification **1E** — the highest-risk imaging class:

> "The GANAB gene mutation found in this patient is typically associated with mild kidney disease; however, according to the Mayo Clinic Imaging Classification (MIC) for ADPKD, our patient falls under Classification 1E, which is predictive of rapid progression to end-stage renal disease (ESRD)... This case questions the assumption that GANAB-associated ADPKD progresses in a mild manner."
> — Agrawal G, Agarwal B, Chandrasekhara Pillai A, Kuriakose K. *Cureus* 2025;17(2):e79498. [PMID:40134995](https://pubmed.ncbi.nlm.nih.gov/40134995/), doi:10.7759/cureus.79498

This is a good candidate for a `discussions` entry with `kind: KNOWLEDGE_GAP` attached to the progression/prognosis section, since n = 1 does not overturn a cohort but does bound the confidence.

### Liver phenotypes

| Phenotype | HPO lead ⚠️ | Notes |
|---|---|---|
| Hepatic cysts | `HP:0001407` | The dominant phenotype in the ADPLD-presenting families; ranges from **absent** → few → massive |
| Hepatomegaly | `HP:0002240` | Secondary to cyst burden |
| Abdominal distension / mass effect | `HP:0003270` ⚠️ | Drives most of the symptom burden in severe PLD |
| Hepatic failure | `HP:0001399` | Rare; PLD is a mass/volume disease, not a synthetic-function disease |

Severity spans the full range: some carriers have no cysts, others require **liver resection or transplantation** (Porath 2016; Delbarba 2022 cites a prior *p.Arg839Trp* carrier who was transplanted).

### Extrarenal / vascular phenotypes

⚠️ **Weakly supported for GANAB specifically.** Intracranial aneurysm is a canonical ADPKD extrarenal feature but was observed in only **one** GANAB family (M641) in the discovery cohort; the association is not established for the gene. Aortic root dilatation was reported in the Delbarba proband.

| Phenotype | HPO lead ⚠️ | Evidence status for GANAB |
|---|---|---|
| Intracranial aneurysm / cerebral artery dilatation | `HP:0004944` ⚠️ verify | Single family — **do not assert as a GANAB feature** |
| Aortic root aneurysm | `HP:0002616` | Single case report (Delbarba 2022) |
| Mitral valve prolapse | `HP:0001634` | ADPKD-general; no GANAB data |
| Pancreatic cysts | `HP:0001737` | ADPKD-general; no GANAB data |

### Laboratory abnormalities

No GANAB-specific biochemical signature. Standard ADPKD labs apply: serum creatinine/eGFR (LOINC 33914-3 eGFR; 2160-0 creatinine), urinalysis for hematuria, and liver enzymes (typically normal or mildly cholestatic in PLD — GGT and ALP may rise with large cyst burden). There is **no clinically deployed glucosidase II activity assay** for diagnosis.

### Quality-of-life impact

⚠️ **No GANAB-specific QoL data exist.** No EQ-5D, SF-36, PROMIS, or disease-specific (e.g. ADPKD-IS, PLD-Q) instrument has been applied to a GANAB cohort. From the PLD literature generally:

> "Liver cysts arise in patients with autosomal dominant PLD (ADPLD) or in co-occurrence with renal cysts... which constitute the main cause of morbidity and markedly affect the quality of life."
> — Olaizola P, Rodrigues PM, Caballero-Camino FJ, et al. *Nat Rev Gastroenterol Hepatol* 2022;19(9):585–604. [PMID:35562534](https://pubmed.ncbi.nlm.nih.gov/35562534/), doi:10.1038/s41575-022-00617-7

Because kidney function is typically preserved, **the QoL burden in GANAB disease is predominantly hepatic mass effect** — early satiety, abdominal distension, pain, dyspnea, malnutrition — rather than the dialysis-trajectory burden that dominates PKD1. This is a genuine, curatable difference from `Polycystic_Kidney_Disease_2` and from `Autosomal_Dominant_Polycystic_Kidney_Disease`.

---

## 4. Genetic / Molecular Information

### Causal gene

**GANAB** (`hgnc:4138`), glucosidase II alpha subunit, 11q12.3, OMIM 104160, UniProt Q14697, NM_198334. Aliases: *GluII, G2AN, KIAA0088, GIIA, GIIalpha*. Previous symbol: *glucosidase, alpha; neutral AB*.

### Pathogenic variants

**Variants reported in Porath et al. 2016** (⚠️ extracted from full text via automated retrieval — **re-verify each variant against Table 1 of the paper before entering into the KB**):

| Family | cDNA | Protein | Type | Family phenotype |
|---|---|---|---|---|
| M263 | c.1265G>T | p.Arg422Leu | Missense | ADPKD + severe PLD |
| M641 | c.1914_1915delAG | p.Asp640Glnfs*77 | Frameshift | ADPKD, variable PLD |
| 290100 | c.1914_1915delAG | p.Asp640Glnfs*77 | Frameshift | ADPKD, variable PLD |
| P1174 | c.1214C>G | p.Thr405Arg | Missense | ADPKD, mild PLD |
| M656 | c.2690+2_+7del | splice | Splice | ADPKD, mild PLD |
| PK20016 | c.39−1G>C | splice | Splice | ADPKD + PLD |
| PK20017 | c.2176C>T | p.Arg726* | Nonsense | ADPKD + PLD |
| P1073 | c.2515C>T | p.Arg839Trp | Missense | ADPLD (severe) |
| M472 | c.152_153delGA | p.Arg51Lysfs*21 | Frameshift | ADPLD (severe) |

Nine variants, **six truncating** — consistent with loss of function as the mechanism.

**Variants reported in van de Laarschot et al. 2020** (Orphanet J Rare Dis 2020;15:302, doi:10.1186/s13023-020-01585-4, [PMC7585303](https://pmc.ncbi.nlm.nih.gov/articles/PMC7585303/)):

| cDNA | Protein | Type |
|---|---|---|
| c.687delT | p.Asp229Glufs*60 | Frameshift |
| c.11_16delTAGCGG | p.Val4_Ala5del | In-frame deletion |
| c.1835G>C | p.Arg612Pro | Missense |
| c.2002+1G>C | — | Splice |
| c.2509C>T | p.Arg837* | Nonsense |
| c.2656C>T | p.Arg886* | Nonsense |

In-silico interpretation from that paper: *p.Arg612Pro* "was predicted to disrupt the structure of the active site of the protein"; the truncating variants are "predicted to cause abnormal binding of α- and β-subunits of glucosidase II, thus affecting its enzymatic activity."

**Structural variants.** Large *GANAB* deletions are a real and under-ascertained class — sequence-only panels will miss them:

> Wilson EM, Choi J, Torres VE, Somlo S, Besse W. **Large Deletions in GANAB and SEC63 Explain 2 Cases of Polycystic Kidney and Liver Disease.** *Kidney Int Rep* 2020;5(5):727–731. [PMID:32405593](https://pubmed.ncbi.nlm.nih.gov/32405593/), doi:10.1016/j.ekir.2020.01.009

**Non-coding variants.** At least one deep-intronic/non-coding *GANAB* variant has been reported to explain isolated PCLD in a large family ([PMC5805583](https://pmc.ncbi.nlm.nih.gov/articles/PMC5805583/)) — relevant to the diagnostic-yield discussion in §10.

⚠️ **Note the discrepancy for curators:** *GeneReviews* states no *GANAB* deletions/duplications had been documented, but Wilson et al. 2020 reported exactly that. Cite the primary paper, not the summary table.

### Variant classification, origin, and functional consequence

- **Classification (ACMG/AMP):** truncating variants are classified pathogenic on PVS1 grounds — ClinVar records e.g. `NM_198334.3(GANAB):c.490C>T (p.Arg164*)` as pathogenic, "loss-of-function is an established mechanism of disease for this gene." Missense variants require functional support (see the rescue assay in §6) and many remain VUS.
- **Origin:** **germline, heterozygous, autosomal dominant.** No somatic-origin disease is described. Somatic second hits in cyst epithelium are presumed by analogy to PKD1/PKD2 but ⚠️ **have not been demonstrated for GANAB**.
- **Functional consequence:** **loss of function / partial loss of function.** Use `functional_impact_category: LOSS_OF_FUNCTION` on the `GeneticContext`, and `modifier: DECREASED` (not `LOSS_OF_FUNCTION`) on downstream GO-bound activity nodes unless a qualitative regulatory-escape claim is being made — the CLAUDE.md `INCREASED`/`GAIN_OF_FUNCTION` discipline applies here.
- **Allele frequency:** individual pathogenic variants are absent or ultra-rare in gnomAD. ⚠️ **Specific gnomAD constraint metrics (pLI, LOEUF, o/e) for GANAB were not retrievable in this session — look them up directly at gnomad.broadinstitute.org before citing any constraint number.** Note the mouse data (§15) showing homozygous lethality, which predicts strong constraint.

### Modifier genes

None mapped for GANAB. The generic ADPKD-spectrum modifier framework applies: Lanktree et al. found "truncating mutations in ADPLD genes and genes of potential relevance as cyst modifiers were found in 20.2 cases and 103.9 cases per 10,000 sequenced, respectively" ([PMID:30135240](https://pubmed.ncbi.nlm.nih.gov/30135240/)).

### Epigenetics

⚠️ **No GANAB-specific epigenetic data.** No methylation, histone, or chromatin study has been performed on GANAB-related disease. (Epigenetic dysregulation — HDAC, bromodomain, miRNA — is an active theme in ADPKD generally, but nothing is GANAB-specific.) Record as a knowledge gap; do not import ADPKD-general epigenetics as PKD3 content.

### Chromosomal abnormalities

None associated. GANAB disease is a single-gene, small-variant + intragenic-deletion disorder. No aneuploidy, translocation, or contiguous-gene syndrome involving 11q12.3 has been linked to PKD3.

---

## 5. Environmental Information

- **Environmental factors:** ⚠️ **None identified.** No toxin, radiation, pollutant, or occupational exposure is associated with PKD3. CTD/TOXNET searching yields no GANAB-disease exposure link.
- **Lifestyle factors:** No GANAB-specific data. If any `environmental:` block is curated, the estrogen-avoidance and vasopressin/water-intake items must be labelled as ADPKD/PLD-general extrapolation, with `environmental_effect` chosen conservatively (`MODULATES`, not `TRIGGERS`).
- **Infectious agents:** ⚠️ **Not applicable.** No infectious etiology or trigger.

Given the repo's `check-environmental-evidence` gate, the honest curation here is either an empty `environmental:` section or an entry carrying the `review_notes: "Left deliberately uncited."` waiver with the searches recorded — not a manufactured citation.

---

## 6. Mechanism / Pathophysiology

This is the section with the strongest, best-cited content, and the reason PKD3 deserves its own entry.

### The causal chain

```
GANAB heterozygous LoF variant
  → reduced glucosidase IIα (GIIα) protein/activity in the ER
  → failure to trim glucose from N-glycans on nascent PC1
  → PC1 fails to complete GPS autoproteolytic cleavage / maturation; retained in ER
  → loss of mature PC1 glycoform; PC1 does not reach plasma membrane or cilium
  → PC2 ciliary localization lost (PC1-dependent trafficking)
  → loss of ciliary polycystin complex signalling
  → ↑ intracellular cAMP, ↑ epithelial proliferation, ↑ transepithelial Cl⁻/fluid secretion
  → focal tubular and biliary cyst initiation, cyst detachment, expansion
  → cystic kidney and liver disease
```

### Upstream — ER glycoprotein quality control (the GANAB-specific step)

Glucosidase II is an ER heterodimer: **GIIα (GANAB)** is catalytic, **GIIβ (PRKCSH/hepatocystin)** is the regulatory/ER-retention subunit. Together they perform the second glucose-trimming step of N-glycan processing, gating entry into and exit from the **calnexin/calreticulin folding cycle**. Both subunits are cystic-disease genes — which is the structural argument that hepatic and renal cystogenesis run through a common protein-biogenesis bottleneck.

Besse et al. generalized this to a pathway-level model:

> "Similarly to PRKCSH and SEC63, these genes encode proteins that are integral to the protein biogenesis pathway in the endoplasmic reticulum. We inactivated these candidate genes in cell line models to show that loss of function of each results in defective maturation and trafficking of polycystin-1, the central determinant of cyst pathogenesis. Despite acting in a common pathway, each PCLD gene product demonstrated distinct effects on polycystin-1 biogenesis."
> — Besse W, Dong K, Choi J, et al. **Isolated polycystic liver disease genes define effectors of polycystin-1 function.** *J Clin Invest* 2017;127(5):1772–1785. [PMID:28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/), doi:10.1172/JCI90129

That last clause matters for curation: ALG8, GANAB, SEC61B, PRKCSH, and SEC63 are **not interchangeable** in their effect on PC1 — they converge on the same node by different routes. This is a strong candidate for a shared mechanism **module** in `kb/modules/` (see the curation note at the end).

### Core functional evidence (Porath 2016, in vitro)

> "Analysis of GANAB-null cells showed an absolute requirement of GIIα for maturation and surface and ciliary localization of the ADPKD proteins (PC1 and PC2), and reduced mature PC1 was seen in GANAB(+/-) cells. PC1 surface localization in GANAB(-/-) cells was rescued by wild-type, but not mutant, GIIα. Overall, we show that GANAB mutations cause ADPKD and ADPLD and that the cystogenesis is most likely driven by defects in PC1 maturation."
> — Porath et al. 2016, [PMID:27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/)

Additional detail from the full text (⚠️ automated extraction — verify before quoting as `snippet`):

- **GANAB-null cells:** complete loss of the mature PC1 glycoform (PC1-NTR); full-length and immature PC1 accumulate; **ciliary PC2 completely absent** despite normal cilium formation; minimal effect on control glycoproteins (EGFR, E-cadherin) — i.e. the defect is **selective for PC1**, not a global glycosylation collapse.
- **GANAB^+/− cells:** ~50% reduction in PC1-NTR — **gene-dosage-proportional**, which is the cell-biological basis for haploinsufficiency as the human mechanism.
- **Rescue:** wild-type FLAG-GIIα restored PC1 surface localization; the disease missense variants **p.Thr405Arg, p.Arg422Leu, p.Arg839Trp failed to rescue**, while presumed-neutral variants did. This is a functional assay usable for ACMG PS3-level evidence.

**Curation note on `evidence_source`:** all of the above is `IN_VITRO`, not `HUMAN_CLINICAL`. The Porath abstract mixes human genetic and cell-biology claims in one paragraph — per CLAUDE.md, **split the evidence items** so each carries a single `evidence_source`.

### Downstream — shared ADPKD cystogenic machinery

Once mature PC1 is lost, the mechanism is the canonical polycystin pathway already curated in `Autosomal_Dominant_Polycystic_Kidney_Disease` and `Polycystic_Kidney_Disease_2`: loss of the ciliary polycystin-1/polycystin-2 receptor-channel complex → derepression of adenylyl cyclase → ↑cAMP → PKA-driven proliferation (B-Raf/MEK/ERK) and CFTR-mediated transepithelial chloride and fluid secretion → mTOR activation, Wnt/planar-cell-polarity disturbance, and a metabolic shift toward aerobic glycolysis in cyst epithelium. **This is `conforms_to` territory — reuse the existing nodes rather than re-deriving them, and cite the shared literature at the ADPKD entry.**

### Cellular processes, cell types, protein dysfunction

- **Protein dysfunction:** loss of enzymatic function (GIIα) → *trans*-acting maturation failure of a client glycoprotein (PC1). Note this is **not** misfolding or aggregation of the mutant protein itself; the disease protein is an enzyme whose absence strands a client. That distinction is worth stating explicitly in the entry's `description`, because it is what separates PKD3's molecular node from PKD1/PKD2.
- **Cellular processes:** ER protein quality control; N-linked glycan processing; ER-to-Golgi trafficking; ciliogenesis-independent ciliary cargo delivery; epithelial proliferation; transepithelial anion secretion.
- **Metabolic changes:** ⚠️ **No GANAB-specific metabolomic data.** The Warburg-like shift described in ADPKD cyst epithelium has not been demonstrated in GANAB disease.
- **Immune involvement:** ⚠️ **None specific.** Macrophage-driven interstitial inflammation is described in advanced ADPKD; no GANAB data.
- **Tissue damage:** cyst mass effect, compression of adjacent parenchyma, secondary interstitial fibrosis. Given preserved kidney function in most carriers, the fibrotic burden appears low — but this has not been formally studied.

### Ontology term leads for the mechanism section

⚠️ **All CURIEs below are leads. Run `just validate-terms` before binding any of them; per the `dismech-terms` rule, "no term beats a bad one."**

**GO — biological process**
| Concept | Lead CURIE |
|---|---|
| protein N-linked glycosylation | `GO:0006487` |
| protein folding in endoplasmic reticulum | `GO:0034975` ⚠️ |
| protein folding | `GO:0006457` |
| response to endoplasmic reticulum stress | `GO:0034976` |
| ERAD pathway | `GO:0036503` |
| protein localization to plasma membrane | `GO:0072659` |
| protein localization to cilium | `GO:0061512` ⚠️ |
| cilium assembly | `GO:0060271` |
| transepithelial chloride transport | `GO:0030321` ⚠️ |
| cAMP biosynthetic process | `GO:0006171` ⚠️ |
| positive regulation of cell population proliferation | `GO:0008284` |
| kidney development | `GO:0001822` |

**GO — molecular function / cellular component**
| Concept | Lead CURIE |
|---|---|
| glucosidase II complex | `GO:0017177` ⚠️ |
| endoplasmic reticulum lumen | `GO:0005788` |
| endoplasmic reticulum membrane | `GO:0005789` |
| ciliary membrane | `GO:0060170` |
| cilium | `GO:0005929` |
| α-glucosidase activity | ⚠️ **unresolved** — GANAB's EC is 3.2.1.207; confirm the exact GO MF term via OAK rather than guessing |

**CL — cell types**
| Concept | Lead CURIE |
|---|---|
| kidney epithelial cell | `CL:0002518` |
| epithelial cell of proximal tubule | `CL:0002306` |
| kidney collecting duct principal cell | `CL:1001431` ⚠️ |
| cholangiocyte | `CL:1000488` ⚠️ |

### Molecular profiling and advanced technologies

⚠️ **Essentially all absent for PKD3.** Recording this honestly is more useful than importing ADPKD-general data:

- **Transcriptomics:** no GANAB-specific GEO/ArrayExpress dataset identified.
- **Proteomics:** none GANAB-specific.
- **Metabolomics / lipidomics:** none.
- **Single-cell / spatial transcriptomics:** none. (Human kidney and liver single-cell atlases exist and would establish GANAB expression by cell type, but no GANAB-disease scRNA-seq has been published.)
- **Functional genomics screens:** GANAB appears in DepMap and genome-wide CRISPR screens as a general-essentiality/glycosylation gene, but **not in a PKD-disease-model screen**.

**Datasets caution:** per CLAUDE.md's Named Entity Confusion warning (§2b), searching GEO for "GANAB" will surface cancer and glycosylation datasets that have nothing to do with polycystic disease. Any `datasets:` block here needs manual `DIRECT`/`GENE_ONLY` triage and `just verify-datasets`.

---

## 7. Anatomical Structures Affected

### Organ level

| Level | Structure | UBERON lead ⚠️ | Notes |
|---|---|---|---|
| Primary | Kidney | `UBERON:0002113` | Bilateral, typically asymmetric/atypical (Mayo class 2) morphology |
| Primary | Liver | `UBERON:0002107` | Often the dominant organ; can be the *only* affected organ |
| Secondary | Biliary tree / intrahepatic bile ducts | `UBERON:0002394` ⚠️ | Cysts derive from biliary epithelium (peribiliary glands / von Meyenburg complexes) |
| Possible | Cerebral arteries | ⚠️ **verify** | Intracranial aneurysm in one family only |
| Possible | Aorta / aortic root | `UBERON:0001496` ⚠️ | Single case (Delbarba 2022) |
| ADPKD-general only | Pancreas | `UBERON:0001264` | No GANAB data |
| ADPKD-general only | Cardiac valves | `UBERON:0002135` (mitral valve) | No GANAB data |

**Body systems:** renal/urinary and hepatobiliary primarily; cardiovascular possibly.

### Tissue and cell level

- **Tissue type:** simple/cuboidal **epithelium** — renal tubular epithelium (distal nephron and collecting duct predominate in ADPKD) and intrahepatic biliary epithelium.
- **Cell populations:** kidney tubular epithelial cells (`CL:0002518`), collecting-duct principal cells (`CL:1001431` ⚠️), cholangiocytes (`CL:1000488` ⚠️).
- ⚠️ **No histopathology series exists for GANAB-related disease specifically.** Cyst lining morphology is presumed identical to classical ADPKD/PLD but has not been separately characterized.

### Subcellular level

This is the diagnostic subcellular signature of PKD3 and should be curated explicitly:

- **Endoplasmic reticulum** (`GO:0005783`), specifically **ER lumen** (`GO:0005788`) and **ER membrane** (`GO:0005789`) — the site of GIIα action and of the PC1 maturation block.
- **Glucosidase II complex** (`GO:0017177` ⚠️).
- **Primary cilium** (`GO:0005929`) and **ciliary membrane** (`GO:0060170`) — the compartment PC1/PC2 fail to reach.
- **Plasma membrane** (`GO:0005886`) — reduced mature PC1 at the surface.

### Localization and lateralization

**Bilateral** kidney involvement, but characteristically **asymmetric and with a small number of large cysts** rather than the diffuse symmetric enlargement of PKD1 — the "atypical" / Mayo class 2 pattern that the minor-ADPKD-gene literature emphasizes. Liver cysts are diffusely distributed through both lobes.

---

## 8. Temporal Development

### Onset

- **Typical onset:** **adult**, and often **late-onset**. Delbarba et al. explicitly title their report "late-onset ADPKD" and describe diagnosis at 45 years incidentally, during screening for hernia repair, with **elderly parents who had bilateral cystic kidneys and normal kidney function** ([PMID:34357571](https://pubmed.ncbi.nlm.nih.gov/34357571/)).
- **Pattern:** **insidious**, frequently **incidental discovery on imaging** performed for another indication.
- **Pediatric/adolescent onset is reported but exceptional** — the 18-year-old with MIC 1E disease (Cureus 2025) and the 12-year-old with a *GANAB* + *PKD1* pair ([PMC6375066](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6375066/)). In the latter case a second locus is the likely explanation.
- **Liver cysts** in PLD generally are "undetectable early in life and usually appear after the age of 40 years" (Orphanet, isolated PCLD, ORPHA:2924) — consistent with the GANAB series.

### Progression

- **Kidney:** **slow or non-progressive.** Kidney function is typically preserved; **no ESKD was reported in the Porath discovery cohort.** For the ADPKD-spectrum minor genes generally, the pattern is "a smaller number of cysts and less kidney enlargement than with PKD1 and PKD2 mutations, asymmetric distribution of cysts, and a slower decline in kidney function."
- **Liver:** **progressive and the main driver of morbidity** in the liver-dominant subset; can reach transplant-requiring severity.
- **Course:** chronic, lifelong, progressive-but-slow. Not episodic or relapsing-remitting. Symptom episodes (pain, hematuria, cyst infection/hemorrhage) punctuate an otherwise indolent course.
- **Duration:** lifelong.

### Staging

⚠️ **No PKD3-specific staging system.** Two ADPKD-general instruments are applied and are directly relevant:

- **Mayo Imaging Classification (MIC)** — htTKV-and-age-based classification into class 1A–1E (typical) and class 2 (atypical). GANAB carriers are expected to fall in **class 2** (atypical morphology); the 2025 Cureus case is notable precisely because the patient was **1E**.
- **CKD stage** (KDIGO G1–G5) for kidney function.
- **Gigot / Schnelldorfer classification** for polycystic liver severity.

### Critical periods and remission

- **No spontaneous or treatment-induced remission.** Cysts do not regress; surgical/interventional treatment debulks rather than cures.
- **Critical intervention window (ADPKD-general, unproven in GANAB):** disease-modifying therapy is most valuable early, while eGFR and kidney volume are still preserved — which is exactly why tolvaptan eligibility is tied to MIC class and eGFR ≥25 (§12). Whether that window concept applies to a genotype that rarely progresses is **an open question and a good `KNOWLEDGE_GAP`**.

---

## 9. Inheritance and Population

### Inheritance

- **Pattern:** **autosomal dominant** (`HP:0000006`). All reported disease is heterozygous.
- **Penetrance:** **incomplete and age-dependent** — strongly so. Lanktree et al.'s population-sequencing finding is the key evidence:
  > "Loss-of-function mutations in ADPLD genes are also more common than expected, suggesting the possibility of unrecognized cases and incomplete penetrance."
  > — Lanktree MB, Haghighi A, Guiard E, Iliuta IA, Song X, Harris PC, Paterson AD, Pei Y. *J Am Soc Nephrol* 2018;29(10):2593–2600. [PMID:30135240](https://pubmed.ncbi.nlm.nih.gov/30135240/), doi:10.1681/ASN.2018050493
- **Expressivity:** **highly variable, both between and within families** — the single most reproducible clinical statement about GANAB.
  > "The evidence that the GANAB variant may cause both ADPKD and ADPLD of variable severity supports that renal and hepatic cystogenesis are the result of a common defective polycystin-1 pathway."
  > — Delbarba E, Econimo L, Dordoni C, et al. *J Nephrol* 2022;35(2):645–652. [PMID:34357571](https://pubmed.ncbi.nlm.nih.gov/34357571/), doi:10.1007/s40620-021-01131-w
- **Genetic anticipation:** **not applicable** — not a repeat-expansion disorder; no anticipation reported.
- **Germline mosaicism:** ⚠️ not reported. De novo variants are presumably possible but undocumented.
- **Founder effects:** ⚠️ none identified. The recurrent `c.1914_1915delAG` in two families (M641, 290100) may represent a shared haplotype or a mutational hotspot — **unresolved in the source**.
- **Consanguinity:** **not relevant** (dominant). Note that homozygous *Ganab* loss is **embryonic lethal in mouse** (§15), so a human biallelic PKD3 phenotype is unlikely to exist.
- **Carrier frequency:** the concept does not apply to a dominant disorder; the relevant quantity is population allele frequency of pathogenic variants (see below).

### Epidemiology

**⚠️ No direct prevalence estimate for PKD3/ADPKD-GANAB exists.** What can be said:

| Quantity | Value | Source |
|---|---|---|
| GANAB as a fraction of **all** ADPKD | **~0.3%** — "∼3% of GUR ADPKD-affected families (~0.3% total ADPKD)" | Porath 2016 (full text; ⚠️ verify) |
| GANAB as a fraction of ADPKD | **<0.5%** | *GeneReviews* NBK1246 |
| Detection rate in a mixed ADPKD/ADPLD referral cohort | **~1%** — "In our study population the detection rate of bona fide pathogenic GANAB variants is ~ 1%" (8 of 625: 7 ADPLD, 1 ADPKD) | van de Laarschot 2020, [PMC7585303](https://pmc.ncbi.nlm.nih.gov/articles/PMC7585303/) |
| Genetically unresolved fraction that GANAB helped close | 7–10% of ADPKD families and ~50% of ADPLD families were GUR before 2016 | Porath 2016 abstract |
| **Derived ballpark PKD3 prevalence** | **~0.03–0.05 per 100,000** if 0.3–0.5% of an ADPKD point prevalence of 3–5/10,000 | ⚠️ **Derived, not measured — mark as an estimate** |

Anchor figures for context (label as ADPKD-general, not PKD3):
- ADPKD point prevalence **3–5 per 10,000** in recent epidemiologic studies; classic lifetime risk ~1 per 1,000 (Lanktree 2018).
- Population-sequencing lower bound for lifetime ADPKD prevalence: **9.3 cases per 10,000 sequenced** (Lanktree 2018) — *higher* than clinical ascertainment, the direct evidence for unrecognized mild disease.
- Isolated ADPLD prevalence **~1/100,000** (Orphanet ORPHA:2924).

**Prevalence curation guidance (per CLAUDE.md §8):** use `measure_type: POINT_PREVALENCE` with `prevalence_class: BELOW_1_IN_1000000` for the derived PKD3 figure, put the derivation in `notes`, and **do not** put a `rate_per_100000` that implies measurement precision the literature does not support. `CASES_IN_LITERATURE` is arguably the more honest `measure_type` here — on the order of **30–40 reported families**.

### Population demographics

- **Ethnic/geographic distribution:** reported families are of European ancestry (US Mayo/HALT/CRISP cohorts, French Genkyst, Dutch, Italian) plus scattered single cases. ⚠️ **This is ascertainment, not biology** — GANAB screening has been performed almost exclusively in European-ancestry ADPKD cohorts, so the apparent distribution is an artifact.
- **Sex ratio:** **~1:1 for inheritance.** But severe **liver** disease is female-predominant across PLD generally — "Women are predominantly affected and have a larger number of cysts than affected males" (Orphanet ORPHA:2924) — and van de Laarschot's 8 carriers were 6 female, mean age 56 (range 31–79). ⚠️ Small n; do not overstate.
- **Age distribution of affected individuals:** diagnosis clusters in the **4th–7th decades**; the Porath carriers spanned ages **9–78 years** (⚠️ full-text extraction, verify).

---

## 10. Diagnostics

### The diagnostic problem, stated plainly

PKD3 is **not diagnosable by phenotype alone**. Its imaging appearance is a mild/atypical cystic kidney with liver cysts — which overlaps with simple cysts, early PKD2, IFT140-related disease, ALG5/ALG8/ALG9 disease, ADTKD, and localized cystic disease. **The diagnosis is molecular, made by a multigene panel.**

### Imaging

- **Kidney ultrasound** — first line. The **Pei unified criteria** (Pei et al., *J Am Soc Nephrol* 2009, [PMID:19118147](https://pubmed.ncbi.nlm.nih.gov/19118147/)) apply to at-risk individuals with a positive family history: ≥3 cysts (uni- or bilateral) at ages 15–39; ≥2 cysts in each kidney at 40–59; ≥4 cysts in each kidney at ≥60. Exclusion in an at-risk individual ≥40 requires fewer than 2 cysts. ⚠️ **These criteria were derived and validated in PKD1/PKD2 families and are of uncertain sensitivity in GANAB carriers**, whose cyst counts are low by definition — a real and citable limitation.
- **MRI / CT** — required for **height-adjusted total kidney volume (htTKV)** and Mayo Imaging Classification, and for characterizing liver cyst burden and planning intervention. GANAB carriers frequently land in **MIC class 2 (atypical)**, in which the class-1 progression model does not apply.
- **RadLex/imaging:** abdominal MRI without and with contrast; T2-weighted sequences for cyst enumeration.

### Laboratory tests

Non-specific: serum creatinine and eGFR (LOINC 33914-3 / 2160-0), urinalysis, urine albumin-to-creatinine ratio, liver panel (ALP and GGT may be elevated with high cyst burden; synthetic function usually preserved), CBC. **There is no biomarker and no clinical enzyme assay for glucosidase II activity.**

### Genetic testing — the decisive modality

- **Recommended approach:** a **PKD/cystic-kidney multigene NGS panel** including *PKD1, PKD2, GANAB, DNAJB11, IFT140, ALG5, ALG8, ALG9, PRKCSH, SEC63, SEC61B, LRP5, PKHD1, HNF1B, NEK8*. *GeneReviews* recommends "a multigene panel that includes GANAB along with PKD1, PKD2, and other associated genes."
- **Sequence analysis** detects >95% of *GANAB* pathogenic variants (*GeneReviews*).
- **Deletion/duplication analysis (CNV calling) must be included** — Wilson et al. 2020 reported a large *GANAB* deletion explaining PKD/PLD ([PMID:32405593](https://pubmed.ncbi.nlm.nih.gov/32405593/)). ⚠️ *GeneReviews*' table stating no GANAB del/dups is out of date on this point.
- **WES/WGS:** WES was the discovery modality (Porath 2016; Besse 2017) and is appropriate for panel-negative cases. **WGS additionally captures non-coding variants** — at least one non-coding *GANAB* variant explains PCLD in a large family ([PMC5805583](https://pmc.ncbi.nlm.nih.gov/articles/PMC5805583/)).
- **Single-gene GANAB testing:** appropriate only for cascade testing of a known familial variant.
- **Not indicated:** chromosomal microarray, karyotype, FISH, mtDNA testing, repeat-expansion testing.
- **⚠️ PKD1 pseudogene caveat:** any panel must handle the six *PKD1* pseudogenes correctly, since excluding *PKD1* is a prerequisite for calling a *GANAB* case.

### Omics-based diagnostics

⚠️ **None validated.** RNA-seq could in principle resolve the splice variants (`c.2002+1G>C`, `c.2690+2_+7del`, `c.39−1G>C`) but no RNA-based diagnostic workflow has been published for GANAB.

### Clinical criteria and differential diagnosis

No PKD3-specific criteria exist. Diagnosis = ADPKD/ADPLD clinical-radiologic picture **+** a pathogenic *GANAB* variant. Cornec-Le Gall et al. propose the composite phenotype-plus-genotype designation:

> "We therefore propose categorization of patients with a phenotypic and genotypic descriptor that will clarify etiology, provide prognostic information, and better describe atypical cases. In genetically defined cases, the designation would include the disease and gene names... Including a genic (and allelic) descriptor with the disease name will provide outcome clues, guide treatment, and aid prevalence estimates."
> — [PMID:29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/)

**Differential diagnosis, with distinguishing features:**

| Condition | Distinguishing feature |
|---|---|
| ADPKD-PKD1 | Innumerable bilateral cysts, marked kidney enlargement, ESKD median ~54 y |
| ADPKD-PKD2 | Milder than PKD1, ESKD median ~78 y — **clinically the closest mimic**; separated only by genetics |
| ADPKD-IFT140 | Mild, ~2% of ADPKD-spectrum cases, often no family history, generally favorable prognosis |
| ADPKD-DNAJB11 | Small kidneys, interstitial fibrosis, ADTKD-like overlap |
| ALG5 / ALG8 / ALG9 disease | Same glycosylation-machinery theme; ALG9 can show early kidney enlargement |
| Isolated ADPLD (PRKCSH, SEC63, SEC61B, LRP5) | Liver-only; but GANAB **also** causes this — genetics is the only separator |
| ARPKD / PKHD1 carrier state | Heterozygous PKHD1 carriers can present with adult PCLD (Besse 2017) |
| ADTKD (UMOD, MUC1, HNF1B) | Few cysts, tubulointerstitial fibrosis, gout (UMOD), hypomagnesemia/diabetes (HNF1B) |
| Simple renal/hepatic cysts | Age-related, non-familial, ≤2–3 cysts |
| Acquired cystic kidney disease | In dialysis patients; small kidneys |
| Tuberous sclerosis / VHL | Extrarenal tumor syndromes; angiomyolipomas / hemangioblastomas |

### Screening

- **Cascade screening** of at-risk first-degree relatives — targeted testing for the known familial variant is preferred over imaging, given the low cyst counts.
- **No newborn screening.** Not appropriate: adult onset, mild course, no preventive intervention available in childhood.
- **No population carrier screening.** Not indicated for a dominant, low-penetrance, mild disorder.
- ⚠️ **Ethical note worth capturing:** predictive testing of asymptomatic minors is generally not recommended for adult-onset ADPKD; the mildness of the GANAB phenotype strengthens that position.

---

## 11. Outcome / Prognosis

### Survival and mortality

⚠️ **No survival, life-expectancy, or mortality data exist for PKD3.** No registry, no cohort, no actuarial estimate. Any number entered here would be fabricated.

What is defensible: because kidney failure is uncommon and the kidney phenotype is mild, **the ADPKD mortality model (dominated by ESKD and cardiovascular disease) is not obviously transferable**, and life expectancy in GANAB carriers with kidney-limited disease is plausibly near-normal — but this is **inference, not evidence**, and should be flagged as such.

### Morbidity and function

- **Kidney:** low morbidity. Kidney function preserved in most carriers; ESKD not reported in the discovery cohort.
- **Liver:** **the dominant morbidity**, and it can be severe — liver resection and liver transplantation are both documented in GANAB carriers. Hepatic morbidity in PLD is mass-effect morbidity: pain, early satiety, malnutrition, dyspnea, portal hypertension in advanced cases.
- **Disability outcomes / ICF:** no data.
- **Quality of life:** no GANAB-specific instrument data (see §3).

### Complications

Kidney: hypertension, hematuria, nephrolithiasis, cyst hemorrhage, cyst infection, chronic pain. Liver: cyst hemorrhage, cyst infection, rupture, compression of the inferior vena cava or portal vein, cholestasis. Vascular: intracranial aneurysm — ⚠️ **one family only; not established for the gene.**

### Prognostic factors

- **Mayo Imaging Classification** (class 1C–1E predicts rapid progression) — but note that MIC was derived in typical class-1 morphology, and GANAB disease is usually class 2, where MIC does not apply. The 2025 Cureus case is the exception that makes this worth curating explicitly.
- **Historical eGFR slope** (≥3 mL/min/1.73 m²/year decline).
- **Genotype itself:** carrying *GANAB* rather than *PKD1* is prognostically favorable — that is the substance of the "genic descriptor" proposal in Cornec-Le Gall 2018.
- **Sex** for the hepatic phenotype (female predominance in severe PLD).
- **Prognostic biomarkers:** none. The PROPKD score was derived for PKD1/PKD2 and is **not validated for GANAB**.

---

## 12. Treatment

⚠️ **There is no GANAB-specific therapy and no GANAB-specific trial. Every item below is ADPKD- or PLD-general and must be curated as such.**

### Kidney-directed pharmacotherapy

**Tolvaptan** — selective vasopressin V2 receptor antagonist; suppresses cAMP-driven cyst-cell proliferation and fluid secretion. The only disease-modifying drug approved for ADPKD.

KDIGO 2025 ([Kidney Int 2025, KDIGO ADPKD guideline](https://www.kidney-international.org/article/S0085-2538(24)00479-4/fulltext)):
> Tolvaptan is recommended in adults with ADPKD and eGFR ≥25 mL/min/1.73 m² at risk of rapidly progressive disease, with initiation criteria of Mayo Imaging Classification 1C–1E or historical eGFR decline ≥3 mL/min/1.73 m²/year.

**⚠️ The direct implication for PKD3: most GANAB carriers would not meet these criteria**, because they are neither MIC 1C–1E nor declining at ≥3 mL/min/yr. The 2025 Cureus case is precisely a report of a GANAB patient who *did*. This tension — a genotype that usually excludes itself from the only approved therapy — is the most clinically actionable thing in this entry and deserves a `mechanistic_hypotheses` or `discussions` node.

Key evidence (ADPKD-general): TEMPO 3:4 ([NCT00428948](https://clinicaltrials.gov/study/NCT00428948), Torres et al. *N Engl J Med* 2012, [PMID:23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/)) and REPRISE ([NCT02160145](https://clinicaltrials.gov/study/NCT02160145), Torres et al. *N Engl J Med* 2017, [PMID:29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/)). ⚠️ **Fetch and verify both abstracts before quoting** — I did not retrieve them in this session.

**Adverse events:** aquaresis (polyuria, nocturia, thirst) is dose-limiting; **idiosyncratic hepatotoxicity** requires monthly then quarterly LFT monitoring. ⚠️ **A specific concern in this genotype:** KDIGO lists "significant liver disease other than polycystic liver disease" as a contraindication, so a GANAB patient with severe PLD sits at an awkward intersection — worth noting.

**Supportive/adjunct:** salt restriction and thiazides reduce tolvaptan polyuria (KDIGO 2025); ACE inhibitors/ARBs for blood pressure with a target of ≤110/75 in younger patients with preserved eGFR (HALT-PKD); high water intake.

### Liver-directed therapy

- **Somatostatin analogues** — octreotide LAR, lanreotide, pasireotide. Reduce liver volume modestly (~3–6%). Olaizola et al.: "Current therapeutic strategies, mainly based on surgical procedures and/or chronic administration of somatostatin analogues, show modest benefits, with liver transplantation as the only potentially curative option" ([PMID:35562534](https://pubmed.ncbi.nlm.nih.gov/35562534/)).
- **Estrogen avoidance**; H2 blockers or PPIs for symptomatic liver cysts (*GeneReviews*).
- **Surgical/interventional:** cyst aspiration with sclerotherapy; laparoscopic fenestration; segmental hepatic resection; **liver transplantation** — the only curative option, and documented in GANAB carriers.

### Kidney replacement

Dialysis and kidney transplantation — standard, but **rarely needed in this genotype**.

### Advanced therapeutics

⚠️ **None exist.** No gene therapy, gene editing, ASO, siRNA, mRNA, cell therapy, targeted therapy, or immunotherapy for GANAB-related disease. Conceptually, an ER-proteostasis or chemical-chaperone approach aimed at rescuing PC1 maturation is the mechanistically indicated strategy — the Besse and Porath rescue experiments are its proof of concept — but **nothing has entered development.** Record as a `KNOWLEDGE_GAP` / `mechanistic_hypotheses` entry with `status: EMERGING`, not as a treatment.

### Experimental / trials

⚠️ **No trial has ever enrolled by GANAB genotype.** ADPKD-general trials that would in principle include GANAB carriers: venglustat ([NCT04705051](https://clinicaltrials.gov/study/NCT04705051), glucosylceramide synthase inhibitor — note its own glycosphingolipid mechanism), and pasireotide LAR in severe PLD ([NCT01670110](https://clinicaltrials.gov/study/NCT01670110)). ⚠️ **Verify current status via `just fetch-reference NCT…` before curating any trial.**

### NCIT treatment term leads ⚠️

| Treatment | `treatment_term` lead | `therapeutic_agent` / modality |
|---|---|---|
| Tolvaptan | `NCIT:C15986` Pharmacotherapy | agent: tolvaptan (⚠️ resolve CHEBI/NCIT via OAK); `therapeutic_modality: SMALL_MOLECULE` |
| Somatostatin analogue (octreotide/lanreotide) | `NCIT:C15986` Pharmacotherapy | agent: octreotide (⚠️ resolve); `therapeutic_modality: PEPTIDE` |
| Antihypertensive therapy (ACEi/ARB) | `NCIT:C15986` Pharmacotherapy | `SMALL_MOLECULE` |
| Liver transplantation | `NCIT:C15289` Organ Transplantation | `SURGERY` |
| Kidney transplantation | `NCIT:C15289` Organ Transplantation | `SURGERY` |
| Hepatic cyst fenestration / resection | `NCIT:C15329` Surgical Procedure | `SURGERY` |
| Genetic counseling | `NCIT:C15240` Genetic Counseling | `BEHAVIORAL` |
| Dietary sodium restriction / high water intake | `NCIT:C15447` Dietary Intervention | `BEHAVIORAL` |
| Supportive/pain management | `NCIT:C15747` Supportive Care | `BEHAVIORAL` or `OTHER` |

Verify each with `uv run runoak -i sqlite:obo:ncit info "l^…"` per the repo's term contract.

### Pharmacogenomics

⚠️ **No GANAB pharmacogenomic data.** Tolvaptan is a **CYP3A4 substrate** — strong CYP3A inhibitors are an absolute contraindication (KDIGO 2025). That is drug-level, not genotype-level, PGx. No CPIC guideline applies.

### Personalized medicine

The genotype-guided principle here is precisely Cornec-Le Gall's: knowing a patient is **ADPKD-GANAB** rather than **ADPKD-PKD1-truncating** changes surveillance interval, tolvaptan candidacy, reproductive counselling, and living-donor evaluation of relatives. That is the clinical payoff of making this diagnosis at all.

---

## 13. Prevention

**There is no primary prevention** — this is a germline dominant disorder. Prevention is reproductive and secondary/tertiary.

- **Primary prevention:** ⚠️ **Not applicable.** No vaccination, no modifiable-exposure prevention.
- **Reproductive options:** genetic counselling (50% transmission risk per pregnancy), **preimplantation genetic testing for monogenic disorders (PGT-M)**, prenatal diagnosis. ⚠️ **A real counselling difficulty specific to GANAB:** the phenotype is mild and penetrance incomplete, so the proportionality of PGT-M/prenatal testing is genuinely debatable in a way it is not for PKD1-truncating disease. Worth curating explicitly.
- **Secondary prevention:** cascade genetic testing of at-risk relatives; abdominal imaging every 1–5 years and blood-pressure monitoring (*GeneReviews* surveillance).
- **Tertiary prevention (preventing complications):** blood-pressure control; adequate hydration; avoidance of nephrotoxins and NSAIDs; treatment of UTIs; **estrogen avoidance in symptomatic PLD** (*GeneReviews*); intracranial aneurysm screening — ⚠️ **indications are ADPKD-general (family history of aneurysm or SAH, high-risk occupation); there is no evidence base for screening GANAB carriers specifically.**
- **Risk stratification:** MIC + eGFR slope, with the caveats above.
- **Behavioral interventions:** low-sodium diet, adequate water intake, smoking cessation, weight management — ADPKD-general, unproven in GANAB.
- **Public health / environmental interventions:** ⚠️ **Not applicable.**
- **Prophylaxis:** none.

---

## 14. Other Species / Natural Disease

⚠️ **No naturally occurring GANAB-related polycystic disease has been reported in any non-human species.** OMIA has no GANAB entry for polycystic kidney disease. This section is close to empty and should be curated that way.

- **Taxonomy of the human disease:** *Homo sapiens*, `NCBITaxon:9606`.
- **Orthologues:** *Ganab* is broadly conserved across metazoa — mouse *Ganab* (NCBI Gene 14376 ⚠️ verify), rat, zebrafish *ganab*, *Drosophila*, *S. cerevisiae* *GLS2/ROT2*. Glucosidase II is one of the most deeply conserved components of ER glycoprotein quality control, and that conservation is itself a mechanistic point: the enzyme is ancient, while its cystic-disease relevance is a vertebrate-specific consequence of having a polycystin client.
- **Breed (VBO):** ⚠️ **Not applicable** — no breed-associated GANAB disease.
- **Naturally occurring PKD in other species — relevant but NOT GANAB:** feline ADPKD in Persian and Persian-derived cats is caused by *PKD1* `c.10063C>A` (p.Cys3284Ter) and is the best-known animal ADPKD (OMIA 000807-9685); bull terrier hereditary nephritis and West Highland White Terrier PKD are also *PKD1*-related. **These are `Autosomal_Dominant_Polycystic_Kidney_Disease` content, not PKD3 content** — importing them here would be a Named Entity Confusion error.
- **Comparative pathology:** the mouse data (§15) show a **species divergence that matters**: mouse *Ganab* haploinsufficiency does not phenocopy human disease. This is a textbook `HUMAN_MODEL_MISMATCH` rather than a `KNOWLEDGE_GAP`.
- **Zoonotic potential / cross-species transmission:** ⚠️ **Not applicable** — non-communicable genetic disorder.

---

## 15. Model Organisms

### The headline finding — and it is a negative one

> **"Homozygous mutation of the Ganab gene in C57BL/6 mice resulted in early embryonic lethality, and there were no cysts in the kidneys or livers of Ganab +/- mice."** … "Homozygous Ganab mutations are lethal in the fetal stage, and Ganab haploinsufficiency does not cause kidney or liver cysts in mice, suggesting that it may not be the causative gene in polycystic kidney disease."
> — Geng G, Xiao Y, Zhang Y, et al. **Ganab Haploinsufficiency Does Not Cause Polycystic Kidney Disease or Polycystic Liver Disease in Mice.** *Biomed Res Int* 2020;2020:7469428. [PMID:32550232](https://pubmed.ncbi.nlm.nih.gov/32550232/), doi:10.1155/2020/7469428

The same paper reports that despite ~50% reduction in Ganab protein, "the expression of ADPKD proteins (PC1 and PC2) and acetylated tubulin was not affected" in the heterozygous mice — i.e. the mouse does not even reproduce the *cellular* intermediate that Porath demonstrated in human cells.

**How to curate this.** This is exactly the case CLAUDE.md describes for `discussions` with `kind: HUMAN_MODEL_MISMATCH` rather than `KNOWLEDGE_GAP`: evidence exists in the model, and its translational validity to human disease is the open question. Two readings are on the table and the entry should hold both:

1. **Species divergence in dosage threshold** — mouse retains enough GIIα activity at 50% to mature PC1, while human PC1 sits closer to a threshold; supported by the human GANAB^+/− cell data showing ~50% PC1-NTR reduction (a measurable deficit that mouse tissue apparently tolerates). Note also that mouse ADPKD models generally require conditional/inducible inactivation and a "third hit" to cyst; a plain heterozygote is a low bar.
2. **The authors' own reading** — that GANAB "may not be the causative gene." ⚠️ **This is a minority position** contradicted by the human genetic and rescue data across four independent cohorts (Porath, Besse, van de Laarschot, plus case reports), but it is in the literature and should be represented rather than suppressed.

For the model link itself: `relationship: FAILS_TO_RECAPITULATE`, which per CLAUDE.md **requires both `limitations` and `evidence`** — both are available here.

### Available and needed models

| Model | Status |
|---|---|
| *Ganab*^−/− mouse (CRISPR/Cas9, C57BL/6) | **Embryonic lethal** — Geng 2020 |
| *Ganab*^+/− mouse | **No renal or hepatic cysts** — Geng 2020 |
| Kidney/liver-conditional *Ganab* knockout | ⚠️ **Not reported.** The obvious next experiment, and the right content for a `proposed_experiments` block |
| Knock-in of a human missense allele (e.g. p.Arg839Trp) | ⚠️ Not reported |
| Zebrafish *ganab* | ⚠️ Not reported for cystic phenotype |
| **GANAB-null human cell lines** | ✅ **The workhorse system.** Porath 2016 (GANAB^−/− and ^+/−, PC1/PC2 maturation, ciliary localization, variant rescue); Besse 2017 (comparative PC1 biogenesis across ALG8/GANAB/SEC61B/PRKCSH/SEC63) |
| Patient-derived iPSC / kidney or liver organoids | ⚠️ **Not reported for GANAB.** A genuine and tractable gap |

### Applications and limitations

- **What the cell models establish well:** the molecular mechanism (PC1 maturation dependence on GIIα), gene-dosage proportionality, and a **functional assay for variant classification** — the rescue assay separates disease missense variants from neutral ones, which is directly usable as ACMG PS3 evidence.
- **What no model currently supports:** cystogenesis in vivo, natural history, organ-specificity (why liver > kidney in many carriers), modifier discovery, and any preclinical therapeutic testing.
- **Resources:** MGI (*Ganab*), IMPC, Alliance of Genome Resources. ⚠️ **Check IMPC for a *Ganab* allele and its viability call** — this session did not query it, and IMPC viability data would independently corroborate the Geng lethality finding.

### Suggested `modeled_mechanisms` skeleton

```yaml
animal_models:
- name: Ganab heterozygous knockout mouse (C57BL/6, CRISPR/Cas9)
  species: Mouse
  genotype: Ganab +/- (CRISPR/Cas9-targeted)
  publication: PMID:32550232
  modeled_mechanisms:
  - target: <the GANAB haploinsufficiency node>
    relationship: FAILS_TO_RECAPITULATE
    fidelity: LOW
    limitations: >-
      Ganab +/- mice develop no kidney or liver cysts and show unaltered PC1/PC2
      expression, so the model reproduces neither the human cystic phenotype nor
      the polycystin-maturation defect demonstrated in human GANAB+/- cells.
      Homozygous loss is embryonically lethal, so a constitutive null cannot be
      assessed postnatally.
    evidence:
    - reference: PMID:32550232
      supports: REFUTE
      evidence_source: MODEL_ORGANISM
      snippet: "<exact quote — fetch via just fetch-reference PMID:32550232>"
      explanation: >-
        Reports the absence of cysts in Ganab+/- mice and embryonic lethality of
        the homozygote, establishing the human/model mismatch.
```

---

## Consolidated reference list

| Citation | Identifier | Role |
|---|---|---|
| Porath B, Gainullin VG, Cornec-Le Gall E, et al. Mutations in GANAB, Encoding the Glucosidase IIα Subunit, Cause Autosomal-Dominant Polycystic Kidney and Liver Disease. *Am J Hum Genet* 2016;98(6):1193–1207 | [PMID:27259053](https://pubmed.ncbi.nlm.nih.gov/27259053/) · doi:10.1016/j.ajhg.2016.05.004 | **Landmark** — gene discovery + functional validation |
| Besse W, Dong K, Choi J, et al. Isolated polycystic liver disease genes define effectors of polycystin-1 function. *J Clin Invest* 2017;127(5):1772–1785 | [PMID:28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) · doi:10.1172/JCI90129 | **Landmark** — ER-biogenesis pathway model |
| Cornec-Le Gall E, Torres VE, Harris PC. Genetic Complexity of Autosomal Dominant Polycystic Kidney and Liver Diseases. *J Am Soc Nephrol* 2018;29(1):13–23 | [PMID:29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) · doi:10.1681/ASN.2017050483 | Nomenclature ("ADPKD-GANAB"), gene list, biallelic disease |
| Lanktree MB, Haghighi A, Guiard E, et al. Prevalence Estimates of Polycystic Kidney and Liver Disease by Population Sequencing. *J Am Soc Nephrol* 2018;29(10):2593–2600 | [PMID:30135240](https://pubmed.ncbi.nlm.nih.gov/30135240/) · doi:10.1681/ASN.2018050493 | Prevalence, penetrance |
| van de Laarschot LFM, et al. Novel GANAB variants associated with polycystic liver disease. *Orphanet J Rare Dis* 2020;15:302 | doi:10.1186/s13023-020-01585-4 · [PMC7585303](https://pmc.ncbi.nlm.nih.gov/articles/PMC7585303/) | Cohort screen, ~1% detection rate, 6 variants |
| Wilson EM, Choi J, Torres VE, Somlo S, Besse W. Large Deletions in GANAB and SEC63 Explain 2 Cases of Polycystic Kidney and Liver Disease. *Kidney Int Rep* 2020;5(5):727–731 | [PMID:32405593](https://pubmed.ncbi.nlm.nih.gov/32405593/) · doi:10.1016/j.ekir.2020.01.009 | Structural variants |
| Geng G, Xiao Y, Zhang Y, et al. Ganab Haploinsufficiency Does Not Cause Polycystic Kidney Disease or Polycystic Liver Disease in Mice. *Biomed Res Int* 2020;2020:7469428 | [PMID:32550232](https://pubmed.ncbi.nlm.nih.gov/32550232/) · doi:10.1155/2020/7469428 | **Negative model result** / HUMAN_MODEL_MISMATCH |
| Delbarba E, Econimo L, Dordoni C, et al. Expanding the variability of the ADPKD-GANAB clinical phenotype in a family of Italian ancestry. *J Nephrol* 2022;35(2):645–652 | [PMID:34357571](https://pubmed.ncbi.nlm.nih.gov/34357571/) · doi:10.1007/s40620-021-01131-w | Variable expressivity, late onset |
| Olaizola P, Rodrigues PM, Caballero-Camino FJ, et al. Genetics, pathobiology and therapeutic opportunities of polycystic liver disease. *Nat Rev Gastroenterol Hepatol* 2022;19(9):585–604 | [PMID:35562534](https://pubmed.ncbi.nlm.nih.gov/35562534/) · doi:10.1038/s41575-022-00617-7 | PLD review, therapy |
| Agrawal G, Agarwal B, Chandrasekhara Pillai A, Kuriakose K. GANAB-Associated Severe ADPKD in an 18-Year-Old Female: A Case Report. *Cureus* 2025;17(2):e79498 | [PMID:40134995](https://pubmed.ncbi.nlm.nih.gov/40134995/) · doi:10.7759/cureus.79498 | Challenges the mildness assumption |
| Daoust MC, Reynolds DM, Bichet DG, Somlo S. Evidence for a third genetic locus for autosomal dominant polycystic kidney disease. *Genomics* 1995;25(3):733–736 | [PMID:7759112](https://pubmed.ncbi.nlm.nih.gov/7759112/) | **Historical PKD3 — do not cite as GANAB evidence** |
| de Almeida S, et al. ADPKD: evidence for the existence of a third locus in a Portuguese family. *Hum Genet* 1995 | [PMID:7607660](https://pubmed.ncbi.nlm.nih.gov/7607660/) | Historical PKD3 |
| Pei Y, Obaji J, Dupuis A, et al. Unified criteria for ultrasonographic diagnosis of ADPKD. *J Am Soc Nephrol* 2009;20(1):205–212 | [PMID:19118147](https://pubmed.ncbi.nlm.nih.gov/19118147/) | ⚠️ Not independently verified this session |
| KDIGO 2025 Clinical Practice Guideline for ADPKD. *Kidney Int* 2025 | [kidney-international.org](https://www.kidney-international.org/article/S0085-2538(24)00479-4/fulltext) | Tolvaptan, MIC, management |
| Harris PC, Torres VE. Polycystic Kidney Disease, Autosomal Dominant. *GeneReviews* | [NBK1246](https://www.ncbi.nlm.nih.gov/books/NBK1246/) | Diagnosis, surveillance, GANAB frequency |
| OMIM 600666 (PKD3) / OMIM 104160 (GANAB) | omim.org | ⚠️ Both returned HTTP 403 this session — **not directly verified** |

---

## Curation notes and caveats

**Three things must be verified before any of this reaches a YAML file:**

1. **Every CURIE above is an unvalidated lead.** Nothing was run through `just validate-terms`. The `dismech-terms` rule applies in full — *no term beats a bad one*. The GO molecular-function term for glucosidase IIα activity and the "intracranial aneurysm" HPO term are the two I would flag as most likely wrong.
2. **The Porath variant table and clinical-range figures in §4 and §3 came from automated full-text extraction**, not from my own reading of the source. Re-verify each variant, each eGFR/htTKV range, and the "~0.3% of total ADPKD" denominator against the paper before entering them. Similarly, **no evidence `snippet` in this report should be pasted into YAML without first running `just fetch-reference PMID:…` and confirming the exact substring** — several quotes above are abstract text relayed through a fetch tool.
3. **OMIM was not reachable** (HTTP 403). The OMIM identifiers, the gene-phenotype assignment, and the clinical synopsis should be confirmed directly.

**Two structural recommendations for the entry:**

- **The `Autosomal_Dominant_Polycystic_Liver_Disease.yaml` entry already exists in this repo.** GANAB straddles it and `Autosomal_Dominant_Polycystic_Kidney_Disease.yaml`. Decide deliberately whether PKD3's liver-dominant presentation is curated here, cross-referenced there, or split — and record the reasoning, because a curator six months from now will ask.
- **The ER-protein-biogenesis bottleneck is a module, not a disease-specific mechanism.** PRKCSH, SEC63, GANAB, ALG8, and SEC61B all converge on defective PC1 maturation, and Besse 2017 is the paper that says so at pathway level. If no module in `kb/modules/` covers it, this is a strong candidate for `create-module` — and PKD3 would then `conforms_to` it rather than duplicating the chain. Check first: `rg -il "polycystin\|glucosidase\|protein biogenesis" kb/modules`.

**Next step:** confirm the entry-type decision (separate `DISEASE` vs `SUBTYPE` of ADPKD), then I can draft the full `Polycystic_Kidney_Disease_3.yaml` against this report — the current file is a 22-line placeholder with two stub nodes.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 27 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 58 |
| Resolved | 56 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 29 |
| Terms named correctly | 27 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003774` (1 mention) - the report calls it "Stage 5 CKD / kidney failure"; HP calls it **Stage 5 chronic kidney disease**
- `HP:0000787` (1 mention) - the report calls it "Nephrolithiasis"; HP calls it **Kidney stone**, and lists "Nephrolithiasis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

56 of 58 terms resolved to a current term; the rest could not be looked up either way.