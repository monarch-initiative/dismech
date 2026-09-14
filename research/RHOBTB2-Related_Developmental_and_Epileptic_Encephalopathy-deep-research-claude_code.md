---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T12:08:21.430774'
end_time: '2026-08-20T12:13:27.390535'
duration_seconds: 305.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RHOBTB2-Related Developmental and Epileptic Encephalopathy
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
  num_turns: 29
  total_cost_usd: 2.3431266999999996
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 15
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - DOI:10.3389/fped.2024.1448793
  relevance_assessed: 10
  on_topic: 7
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RHOBTB2-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RHOBTB2-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I'll research RHOBTB2-Related Developmental and Epileptic Encephalopathy using web search and fetch, then compile a comprehensive report.

Excellent detail. Let me get a few more specifics — the ion channel mechanism paper, the recent Epilepsia clinical spectrum paper, HPO/phenotype frequencies, and MONDO ID.

I now have sufficient primary-source material to compile the comprehensive report.

# RHOBTB2-Related Developmental and Epileptic Encephalopathy (DEE64) — Comprehensive Research Report

---

## 1. Disease Information

**Overview.** RHOBTB2-related developmental and epileptic encephalopathy (also designated Developmental and Epileptic Encephalopathy 64, DEE64; formerly Early Infantile Epileptic Encephalopathy 64, EIEE64) is a rare, autosomal dominant neurodevelopmental disorder caused by heterozygous, almost always *de novo*, missense variants in *RHOBTB2* (Rho-related BTB domain-containing protein 2). It was first delineated in 2018 and is characterized by early-onset (usually first-year-of-life) seizures, moderate-to-severe intellectual disability, postnatal microcephaly, hypotonia, and a distinctive polymorphic movement disorder with paroxysmal, alternating-hemiplegia-of-childhood (AHC)-like features (dystonia, ataxia, chorea-like movements) ([Straub et al. 2018, PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/); [OMIM #618004](https://omim.org/entry/618004)). The disease spectrum has since expanded to include milder phenotypes from GTPase-domain variants and biallelic loss-of-function variants, so the field increasingly uses the umbrella term "RHOBTB2-related disorders" (RHOBTB2-RD) rather than a single DEE label ([Genetics in Medicine 2023](https://www.gimjournal.org/article/S1098-3600(23)00898-5/fulltext); [Epilepsia 2026, epi.70286](https://onlinelibrary.wiley.com/doi/abs/10.1002/epi.70286)).

**Key identifiers:**

| Database | Identifier |
|---|---|
| OMIM phenotype | #618004 — Developmental and Epileptic Encephalopathy 64 (DEE64) |
| OMIM gene | *607352 — RHOBTB2 |
| HGNC | HGNC:18756 (RHOBTB2) |
| NCBI Gene | 23221 |
| Ensembl | ENSG00000008853 |
| UniProt | Q9BYZ6 |
| Cytogenetic location | 8p21.3 (GRCh38: chr8:22,950,813–23,020,199) |
| GARD | Developmental and epileptic encephalopathy, 64 (GARD ID 13681) |
| ClinVar | Multiple RCVs, e.g. RCV000656374 for c.1465C>T (p.Arg489Trp) |
| MONDO | A MONDO term unifying DEE64 is expected to exist (mapped from OMIM:618004) but could not be independently confirmed via web search in this session — verify directly at mondo.monarchinitiative.org before curating |

**Synonyms/alternative names:** RHOBTB2-related developmental and epileptic encephalopathy; Early Infantile Epileptic Encephalopathy 64 (EIEE64) — older nomenclature; RHOBTB2-related disorders (RHOBTB2-RD, encompassing DEE64 plus the milder GTPase-domain and biallelic-variant phenotypes); the protein/gene is also known by the alias **DBC2** ("Deleted in Breast Cancer 2") and **p83**.

**Evidence basis:** Nearly all published knowledge derives from aggregated case series and case reports (patient-level clinical, EEG, MRI, and genetic data), i.e., disease-level literature rather than large-scale EHR aggregation. The largest cohort to date integrates 12 Chinese patients with 79 previously published international cases (~91 total) ([Epilepsia 2026](https://onlinelibrary.wiley.com/doi/abs/10.1002/epi.70286)); earlier landmark series include the original 10-patient description ([PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/)), a 34-patient early series, and the 11-patient AHC-spectrum expansion ([Zagaglia et al. 2021, Neurology](https://pubmed.ncbi.nlm.nih.gov/33504645/)).

---

## 2. Etiology

**Disease causal factor:** Monogenic — heterozygous, predominantly *de novo* missense variants in *RHOBTB2*, an atypical Rho GTPase family gene (8p21.3). No environmental or infectious causal factor is implicated; this is a purely genetic (Mendelian) disorder within dismech's "Mendelian" category classification.

**Genetic risk factors:**
- **Causal variants:** De novo heterozygous missense variants clustering in the two BTB (Broad-complex, Tramtrack, Bric-à-brac) domains — hotspots at **Arg483** (p.Arg483His, recurrent) and **Arg511** (p.Arg511Trp, p.Arg511Gln, p.Arg511Gly, all recurrent) account for "more than half" of reported BTB-domain variants ([PMC11744465](https://pmc.ncbi.nlm.nih.gov/articles/PMC11744465/); [Epilepsia 2026](https://onlinelibrary.wiley.com/doi/abs/10.1002/epi.70286), reporting 75% of Chinese-cohort variants in the BTB domain with p.Arg483His as a conserved hotspot). Other BTB-region variants include p.(Ala471Val), p.(Ala474Gly), p.(Arg507Cys), p.(Arg489Trp) — the latter confirmed de novo in the French Guiana case report ([Defo et al. 2022, PMC9184662](https://pmc.ncbi.nlm.nih.gov/articles/PMC9184662/)).
- A second class of variants affects the **N-terminal GTPase domain** — e.g., p.(Asp114His), p.(Arg116Cys), p.(Arg154Gln), p.(Arg154Leu) — and is mechanistically and phenotypically distinct (see §6).
- **Biallelic (recessive) variants:** Homozygous/compound-heterozygous splice-site and truncating variants (e.g., p.(Ser543Alafs*52)) have been described in 9 families, showing that complete loss of RHOBTB2 function is also pathogenic, producing "variable neurodevelopmental phenotypes" distinct from the dominant gain-of-function BTB presentation ([GIM 2023](https://www.gimjournal.org/article/S1098-3600(23)00898-5/fulltext)).
- Constraint metrics (gnomAD pLI/LOEUF/missense-Z) could not be retrieved directly in this session (page was JS-rendered); prior functional work notes ExAC-era constraint data suggested RHOBTB2 tolerates loss-of-function variants, arguing against simple haploinsufficiency as the dominant-disease mechanism ([PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/)) — consistent with the biallelic-LOF-vs-dominant-missense dichotomy above. This should be independently verified against the current gnomAD v4 browser before curation.
- **Modifier genes:** None specifically established; *CEBPA* has been proposed as an upstream transcriptional regulator of RHOBTB2 expression in a rat prenatal-malnutrition model (see §15), but this is not a human disease modifier per se.

**Environmental risk/trigger factors:** Not causal, but recognized **precipitants of acute encephalopathic/seizure exacerbation** in already-affected individuals:
- **Fever/hyperthermia** — recurring trigger for acute encephalopathy and status epilepticus episodes.
- **Head trauma (including mild)** — documented as a trigger for acute encephalopathy in RHOBTB2 patients ([Neurology Genetics, "Acute encephalopathy after head trauma in a patient with a RHOBTB2 mutation"](https://www.neurology.org/doi/10.1212/NXG.0000000000000418); [Neurología English Edition, "Mild head trauma: Acute encephalopathy trigger..."](https://www.elsevier.es/en-revista-neurologia-english-edition--495-articulo-mild-head-trauma-acute-encephalopathy-S217358082200058X)). At least five patients across the literature have had acute encephalopathy/seizures triggered by hyperthermia or head trauma, with severe EEG abnormalities and abnormal MRI (hemisphere swelling, restricted diffusion) during these episodes.

**Protective factors:** None identified in the literature reviewed.

**Gene-environment interactions:** The fever/trauma-triggered encephalopathy pattern suggests a gene-environment interaction in which the already-destabilized RHOBTB2 protein/ion-channel network has reduced tolerance for physiological stress, but no formal GxE study has been published.

---

## 3. Phenotypes

### Core clinical features (with suggested HPO terms; frequencies drawn from the literature reviewed — verify against the largest cohort, Epilepsia 2026, for precise percentages before final curation)

| Phenotype | Category | Onset/Course | Frequency (literature) | Suggested HPO term |
|---|---|---|---|---|
| Seizures (multiple types: tonic-clonic, focal clonic, myoclonic, epileptic spasms) | Symptom/clinical sign | Onset typically <12 months, some as early as 4 days postnatal | Core/near-universal feature | HP:0001250 (Seizure); HP:0002069 (Bilateral tonic-clonic seizure); HP:0002123 (Generalized myoclonic seizure) |
| Drug-resistant/refractory epilepsy | Clinical course | Chronic | Common — many patients remain seizure-prone despite polytherapy | HP:0011722 (Drug-resistant seizures, i.e., "intractable epilepsy") |
| Severe intellectual disability / developmental delay | Behavioral/cognitive | From infancy, static-to-progressive | Core feature, most patients | HP:0001249 (Intellectual disability); HP:0001263 (Global developmental delay) |
| Postnatal microcephaly | Physical/laboratory (growth) | Postnatal onset (often not present at birth; e.g., French Guiana case emerged at 9 months, -2.5 SD) | Frequent (e.g., 5 of a reported series had microcephaly, -3 to -4.5 SD) | HP:0005484 (Postnatal microcephaly) |
| Hypotonia | Physical sign | Infancy onward | Common | HP:0001252 (Hypotonia) |
| Movement disorder — dystonia | Physical sign | Variable, often paroxysmal | Common | HP:0001332 (Dystonia) |
| Movement disorder — ataxia | Physical sign | Variable | Common | HP:0001251 (Ataxia) |
| Paroxysmal chorea-like movements / choreoathetosis | Physical sign | Episodic | Characteristic | HP:0002072 (Chorea); HP:0002119 (Ventriculomegaly — not relevant, omit) |
| Alternating hemiplegia of childhood (AHC)-like episodes | Physical sign | Paroxysmal, episodic | Reported in ~84% of cases per one review; established as a distinct expanded phenotype ([Zagaglia 2021](https://pubmed.ncbi.nlm.nih.gov/33504645/)) | HP:0032794 (Alternating hemiplegia — check exact HPO term) |
| Poor/absent speech | Behavioral | Static | Common | HP:0002465 (Poor speech) or HP:0001344 (Absent speech) |
| Motor delay ranging to complete lack of head control / non-ambulation | Physical sign | Progressive spectrum | Variable severity | HP:0001270 (Motor delay) |
| Nonspecific facial dysmorphism | Physical sign | Congenital | Common but nonspecific | HP:0001999 (Abnormal facial shape) |
| Acute encephalopathy episodes (fever/trauma-triggered) | Clinical course | Episodic, triggered | Documented in ≥5 reported patients | HP:0006846 (Encephalopathy, episodic) |
| Poor postnatal growth | Physical sign | Postnatal | Common ("many patients had poor overall postnatal growth") | HP:0008897 (Postnatal growth retardation) |

**Genotype-linked phenotype severity (see also §6, §9):**
- **BTB-domain variants** → earlier seizure onset, more severe DEE, drug-resistant epilepsy, and the full AHC-like movement disorder.
- **GTPase-domain variants** → broader, generally milder spectrum: mild-to-moderate intellectual disability, learning difficulties, developmental regression in some, and — per the mechanistic study below — seizures that are typically better controlled with antiseizure medication ([HMG 2025, PMC/Oxford Academic](https://academic.oup.com/hmg/article/34/7/639/7976912); [GIM 2023](https://www.gimjournal.org/article/S1098-3600(23)00898-5/fulltext)).
- **Biallelic loss-of-function variants** → variable neurodevelopmental phenotypes distinct from the classic dominant BTB presentation.
- A milder phenotype was also correlated with a specific variant, p.(Ala474Gly), in the original ten-patient cohort ([PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/)).

**Quality of life impact:** No disease-specific EQ-5D/SF-36/PROMIS data were located. Qualitatively, the combination of drug-resistant epilepsy, severe intellectual disability, and a debilitating paroxysmal movement disorder (with episodic AHC-like crises) is described as substantially disabling, with motor function ranging "from total lack of head control and inability to walk to walking with a broad-based or unsteady gait" ([Frontiers Pediatrics 2024](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2024.1448793/full)).

---

## 4. Genetic/Molecular Information

**Causal gene:** *RHOBTB2* (HGNC:18756; NCBI Gene 23221; Ensembl ENSG00000008853; OMIM *607352). Encodes an atypical Rho GTPase with a modular architecture: N-terminal GTPase domain, proline-rich region, tandem BTB1–BTB2 domains, and a conserved C-terminal region ([Wikipedia/HGNC](https://en.wikipedia.org/wiki/RHOBTB2); RhoBTB family review).

**Pathogenic variant classification and type:**
- Predominantly **de novo heterozygous missense variants**, clustering in the BTB1/BTB2 domain region (dominant, gain-of-function-like mechanism) or the N-terminal GTPase domain (distinct, milder mechanism).
- **Recurrent/hotspot residues:** Arg483 and Arg511 (BTB domain) — collectively >50% of BTB variants.
- Documented BTB-domain variants: p.(Ala471Val), p.(Ala474Gly), p.(Arg483His), p.(Arg489Trp), p.(Arg507Cys), p.(Arg511Gly), p.(Arg511Trp), p.(Arg511Gln), p.(Ser543Alafs*52 — homozygous/biallelic).
- Documented GTPase-domain variants: p.(Asp114His), p.(Arg116Cys), p.(Arg154Gln), p.(Arg154Leu).
- **Biallelic (recessive) variants:** splice-site and truncating variants reported in 9 families (GIM 2023), establishing complete loss-of-function as a second, distinct disease mechanism.
- **ACMG/ClinVar classification:** individual variants (e.g., c.1465C>T p.(Arg489Trp), ClinVar RCV000656374) are classified case-by-case; consult ClinVar/ClinGen directly for current classifications before curation.
- **Allele frequency:** Pathogenic variants are essentially absent from population databases (gnomAD) consistent with de novo, severe, dominant disease — exact gnomAD constraint values (pLI/LOEUF) should be pulled directly from the gnomAD browser (not confirmed in this session due to a fetch limitation).
- **Somatic vs. germline:** Germline (constitutional) de novo variants for DEE64; separately, *somatic* loss-of-function/deletion events in RHOBTB2 are described in cancer (see below) — these are a biologically related but clinically distinct phenomenon.

**Functional consequence — the central genotype-mechanism finding:**
> "Mutant RHOBTB2 was more abundant than the wild-type, most likely because of impaired degradation in the proteasome" — and this effect was reversed by proteasome inhibition, "confirming proteasomal degradation impairment as the primary mechanism" for BTB-domain variants ([Straub et al. 2018, PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/)).

This is a **gain-of-function / dominant-negative-like accumulation mechanism** (increased mutant protein abundance due to impaired 26S proteasomal degradation), not simple haploinsufficiency — a genuinely unusual, notable mechanism among developmental encephalopathy genes. Co-immunoprecipitation studies found **no differential CUL3 binding** between mutant and wild-type RHOBTB2, indicating the pathogenic effect operates downstream of/independent from simple loss of CUL3 engagement ([PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/)).

By contrast, GTPase-domain variants do **not** impair proteasomal degradation — RHOBTB2 protein levels remain normal — pointing to an alternative (likely direct protein-protein-interaction or GTPase-cycle) pathogenic mechanism.

**Epigenetic information:** In cancer contexts (not DEE), *RHOBTB2* promoter CpG-island hypermethylation causes epigenetic silencing and loss of tumor-suppressor function (see §6). No epigenetic mechanism has been specifically described for the DEE64 phenotype.

**Chromosomal abnormalities:** No recurrent large-scale chromosomal rearrangement (translocation, aneuploidy) is described for DEE64; disease is driven by point/small-indel variants within *RHOBTB2*.

---

## 5. Environmental Information

- **Environmental/toxin factors:** None established as causal for RHOBTB2-RD; disease is monogenic.
- **Lifestyle factors:** Not applicable as causal factors; however, avoidance of known triggers (fever control, minimizing head trauma risk) is a practical management consideration given the documented trigger relationship (§2).
- **Infectious agents:** Not causal, but febrile illness (of any infectious etiology) is a recognized *trigger* for acute encephalopathic crises in affected individuals, not a cause of the underlying genetic disease.

---

## 6. Mechanism / Pathophysiology

### Molecular function of RHOBTB2 (baseline biology)
RHOBTB2 (a.k.a. DBC2) is a substrate-specific adaptor for a Cullin-3 (CUL3)–RBX1-based E3 ubiquitin ligase complex ([Wilkins et al., PMC2749729](https://pmc.ncbi.nlm.nih.gov/articles/PMC2749729/); [Berthold et al., "RhoBTB2 is a substrate of the mammalian Cul3 ubiquitin ligase complex"](https://www.ncbi.nlm.nih.gov/sites/ppmc/articles/PMC395845/)). Mechanism:
1. RHOBTB2's BTB domains bind CUL3's N-terminal region.
2. RHOBTB2 recruits specific substrates for ubiquitination.
3. RBX1 recruits E2 ubiquitin-conjugating enzymes, transferring ubiquitin to the CUL3/RHOBTB2-bound substrate, building a polyubiquitin chain.
4. The polyubiquitinated substrate — and RHOBTB2 itself — is degraded by the 26S proteasome.
5. An **autoregulatory mechanism** exists: the non-GTP-binding GTPase domain can fold back and interact intramolecularly with the BTB region, keeping RHOBTB2 in an inactive, degradation-protected state — a proposed "closed" conformation model.

Suggested **GO terms**: GO:0004871 (signal transducer activity — for GTPase-domain function); GO:0031624 (ubiquitin conjugating enzyme binding); GO:0031461 (cullin-RING ubiquitin ligase complex); GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process); GO:0007015 (actin filament organization); GO:0016477 (cell migration).

### Causal chain for DEE64 (BTB-domain, dominant/gain-of-function arm)
1. **Trigger:** De novo missense variant at a BTB-domain hotspot (e.g., p.Arg483His, p.Arg511Trp/Gln/Gly).
2. **Molecular lesion:** Variant impairs proteasomal recognition/degradation of RHOBTB2 without disrupting CUL3 binding → **increased steady-state abundance of mutant RHOBTB2 protein** in neurons.
3. **Downstream transcriptional/ion-channel effect:** RNA-seq in a *Drosophila* overexpression model shows enrichment for differentially expressed **ion channel genes**, including orthologs of human voltage-gated sodium channels (*paralytic* → SCN1A/SCN2A/SCN3A/SCN8A), a potassium channel (*slowpoke* → KCNMA1/BK channel), and an ionotropic glutamate receptor (*ir76a*) ([Human Molecular Genetics 2025](https://academic.oup.com/hmg/article/34/7/639/7976912)).
4. **Cellular electrophysiology (human iPSC-derived neurons):** Neurons carrying patient BTB-domain variants show **significantly altered neuronal excitability** — increased action-potential firing frequency, increased AP half-width, and decreased depolarization speed — compared to wild-type. Critically, this electrophysiological derangement was **not** seen in neurons with GTPase-domain variants or with complete RHOBTB2 knockout, mechanistically explaining the BTB-vs-GTPase genotype-phenotype divergence.
5. **Organismal phenotype (Drosophila):** Pan-neuronal *RhoBTB* overexpression causes bang-sensitivity (seizure-like paralysis after mechanical shock) and severe locomotor impairment in negative-geotaxis assays; *RhoBTB* knockdown in dendritic arborization (da) neurons causes reduced dendritic branch number — implicating RHOBTB2 dosage in both neuronal excitability and dendritic morphogenesis ([Straub et al. 2018, PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/)).
6. **Clinical manifestation:** Neuronal hyperexcitability + disrupted dendritic architecture → seizures, developmental encephalopathy, movement disorder.

Two candidate mechanistic hypotheses remain open (not yet distinguished): (a) RHOBTB2 accumulation indirectly dysregulates ion-channel gene *transcription*; (b) RHOBTB2 (or a RHOBTB2-CUL3 complex) directly ubiquitinates ion channels as substrates, and impaired turnover/mistargeting of the channels themselves drives hyperexcitability.

**Cell types/anatomical scale:** Primarily central nervous system neurons (cortical/dendritic-arborization-type neurons in the fly model; iPSC-derived cortical neurons in the human model). Suggested **CL terms**: CL:0000540 (neuron); CL:0000598 (dendritic cell — not relevant, exclude); CL:0011020 (neural progenitor cell, if precursor-stage effects are modeled); consider CL:0000679 (glutamatergic neuron) given the ionotropic glutamate receptor link.

### Cancer-associated mechanism (contrast arm — informs the "gain vs. loss" duality)
In sporadic cancers, **loss** of RHOBTB2 function — via deletions, loss-of-function variants (found in ~10% of breast cancer samples), or CpG-island promoter hypermethylation — removes its tumor-suppressor activity (failure to degrade oncogenic substrates such as Cyclin D1), promoting unchecked proliferation in breast, lung, bladder, gastric cancers, and osteosarcoma ([Frontiers Pediatrics 2024](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2024.1448793/full); Oncogene 2016, DBC2/RhoBTB2-Musashi-2 axis). This is the biological converse of the DEE64 mechanism: **precise RHOBTB2 dosage is essential — too little predisposes to malignancy, too much (via impaired degradation) is neurotoxic.**

Additional hypothesized pathway: dysregulation of an **E2F1–RHOBTB2** axis affecting apoptotic signaling has been proposed as contributing to the neurodevelopmental phenotype and was leveraged in an AI-guided drug-repurposing screen (see §12).

**Metabolic/immune involvement:** No specific metabolic pathway or immune-mediated mechanism has been reported for RHOBTB2-RD; this is a cell-intrinsic proteostasis/ion-channel-excitability disorder of the CNS.

**Molecular profiling data:** RNA-seq (Drosophila overexpression model) is the principal transcriptomic dataset reported; no human patient-derived multi-omics (proteomics, metabolomics, single-cell) datasets specific to RHOBTB2-RD were identified in this search.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (brain) — cerebral cortex (seizure generation, cognitive impairment), basal ganglia/extrapyramidal circuits (dystonia, chorea), cerebellum (ataxia).
- **Secondary:** Growth (postnatal microcephaly, poor postnatal growth) reflects secondary CNS/systemic developmental effects rather than a distinct organ-level primary lesion.
- **Body systems:** Nervous system (primary); musculoskeletal system secondarily affected via hypotonia/movement disorder.

Suggested **UBERON terms**: UBERON:0000955 (brain); UBERON:0001872 (cerebral hemisphere); UBERON:0002037 (cerebellum); UBERON:0002420 (basal ganglion).

**Tissue/cell level:** Cortical and dendritic-arborization neurons (per the Drosophila and iPSC modeling). RHOBTB2 tissue expression is reported as primarily neural, with lesser expression in fetal heart and lungs.

**Subcellular level:** Cytosol, plasma membrane, cytoskeleton (actin) per baseline RHOBTB2 biology (Wikipedia/UniProt); the ubiquitin-proteasome degradation machinery (26S proteasome) is a key subcellular locus of pathogenic mechanism. Suggested **GO Cellular Component terms**: GO:0005737 (cytoplasm); GO:0005886 (plasma membrane); GO:0015629 (actin cytoskeleton); GO:0000502 (proteasome complex).

**Localization/lateralization:** The characteristic AHC-like movement-disorder episodes are, by definition, often lateralized/alternating (hemiplegic episodes shifting sides), a distinguishing clinical feature from typical bilateral movement disorders.

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal predisposition with clinical onset typically in the **first year of life**; seizures have been documented as early as 4 days postnatal in the most severe cases. Microcephaly is typically **postnatal** in onset (normal head circumference at birth in documented cases, e.g., the French Guiana patient, with microcephaly emerging by 9 months).
- **Onset pattern:** Acute-to-subacute onset of seizures; insidious emergence of developmental delay/regression.
- **Progression:** Variable — ranges from static severe DEE with drug-resistant epilepsy and profound motor/cognitive impairment (BTB-domain variants) to a milder, more static-to-slowly-progressive course with learning difficulties (GTPase-domain variants); some patients show frank **developmental regression**.
- **Disease course pattern:** Chronic, lifelong; punctuated by **episodic/paroxysmal exacerbations** — both the intrinsic AHC-like movement episodes and acute encephalopathic crises triggered by fever or head trauma.
- **Critical periods:** Infancy/early childhood is the period of highest vulnerability for seizure onset and encephalopathic crises; avoidance of febrile illness complications and head trauma is a practically important window for intervention (see §13).

---

## 9. Inheritance and Population

**Epidemiology:** RHOBTB2-RD is an **ultra-rare** disorder. Approximately 91 cases have been aggregated in the most recent comprehensive cohort (12 Chinese + 79 international) ([Epilepsia 2026](https://onlinelibrary.wiley.com/doi/abs/10.1002/epi.70286)); earlier series reported 19–34 patients. No formal population-based prevalence or incidence estimate (per 100,000) has been published; RHOBTB2-related AHC-spectrum disease is grouped among ultra-rare neurological disorders generally estimated at 1:100,000–1:1,000,000 by analogy to related AHC etiologies, but this figure is not RHOBTB2-specific and should be treated as a rough proxy, not a citable disease-specific statistic.

**Inheritance pattern:** **Autosomal dominant** for the classic BTB-domain and GTPase-domain missense phenotypes, essentially always occurring as ***de novo*** variants (parental testing consistently negative in reported trios). A separate ***autosomal recessive*** (biallelic loss-of-function) inheritance pattern has been described in 9 families for splice-site/truncating variants (GIM 2023), producing a distinct, variable neurodevelopmental phenotype.

**Penetrance/expressivity:** Appears fully penetrant for the dominant missense variants (all reported carriers are symptomatic), with **highly variable expressivity** — phenotype severity ranges from classic severe DEE64 to milder learning-difficulty/movement-disorder-predominant presentations, correlating with variant domain location (BTB vs. GTPase) as detailed in §6.

**Genetic anticipation:** Not applicable/not reported — this is not a repeat-expansion disorder.

**Germline mosaicism:** Not specifically documented for RHOBTB2 in the sources reviewed; general possibility exists for any de novo dominant disorder but should be discussed with families as a theoretical (low) recurrence-risk consideration, not confirmed by RHOBTB2-specific mosaicism reports found here.

**Founder effects / consanguinity:** No founder-population effect reported for the dominant missense variants (occur as independent de novo events across diverse populations/ethnicities, including reports from France/French Guiana, China, UK, and elsewhere). The biallelic/recessive presentation would be expected to show increased likelihood in consanguineous families, consistent with general autosomal-recessive genetics, though this was not explicitly detailed in the sources reviewed.

**Carrier frequency:** Not applicable in the classical sense for a dominant de novo disorder (BTB/GTPase arm); for the recessive biallelic arm, population carrier frequency of individual loss-of-function alleles is expected to be very low (ultra-rare), consistent with a rare recessive disorder, but no specific carrier-frequency data were located.

**Population demographics:** Cases reported across multiple continents/ethnicities (European, Chinese, South American [French Guiana]) with no described geographic clustering or strong ethnic predisposition. Sex ratio: not clearly skewed in the sources reviewed (no strong male:female bias reported); should be checked against the largest published cohort (Epilepsia 2026) directly if precise ratios are needed for curation. Age distribution: pediatric-onset disorder by definition (first year of life), tracked through childhood in the reported literature (long-term adult natural history data are limited given the disorder's recent [2018] delineation).

---

## 10. Diagnostics

**Clinical/laboratory tests:** No RHOBTB2-specific biochemical biomarker has been identified; diagnosis is clinical + genetic. Standard metabolic/laboratory work-up is used mainly to exclude alternative etiologies of DEE.

**Imaging:**
- **Brain MRI** is frequently **normal**, particularly early in the disease course (e.g., normal at both 3 and 10 months in the French Guiana case) — an important diagnostic point, since normal neuroimaging does not exclude RHOBTB2-RD.
- During **acute encephalopathic crises** (fever/trauma-triggered), MRI can show transient abnormalities: hemisphere swelling and/or reduced diffusion in various brain regions.

**Electrophysiology:**
- **EEG** findings are variable; documented findings include slowed background electrogenesis for age (delta rhythm) and diffuse/focal polyspikes (e.g., right-hemisphere polyspikes in the French Guiana case). During acute encephalopathic episodes, severe EEG abnormalities have been documented.
- No RHOBTB2-specific EEG signature/biomarker (e.g., a pathognomonic ictal or interictal pattern) has been established.

**Genetic testing (primary diagnostic modality):**
- **Whole exome sequencing (WES) or whole genome sequencing (WGS)**, typically as a **trio** (proband + both parents) to confirm de novo status, is the standard diagnostic approach given the phenotypic heterogeneity and lack of a pathognomonic clinical sign.
- **Epilepsy/DEE gene panels** that include RHOBTB2 are also used in clinical practice (e.g., Genomics England PanelApp lists RHOBTB2 under both "Early onset or syndromic epilepsy" and "Paroxysmal central nervous system disorders" panels).
- Single-gene Sanger confirmation follows panel/WES identification of a candidate variant.
- Chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are not primary diagnostic tools for this disorder but are commonly part of a broader DEE diagnostic work-up to exclude other etiologies before/alongside RHOBTB2 sequencing.

**Clinical diagnostic criteria:** No formal consensus clinical diagnostic criteria (e.g., DSM/ICD-style) exist specifically for RHOBTB2-RD; diagnosis relies on the combination of characteristic phenotype (early-onset DEE + paroxysmal movement disorder ± AHC-like features + postnatal microcephaly) plus confirmatory molecular genetic testing.

**Differential diagnosis:** Most importantly, **ATP1A3-related alternating hemiplegia of childhood** (classic AHC), given phenotypic overlap in the paroxysmal movement-disorder domain — RHOBTB2-RD is explicitly framed in the literature as an AHC-mimicking/AHC-spectrum-expanding disorder distinct from ATP1A3-AHC ("RHOBTB2-Associated Neurological Phenotypes and Underlying Mechanisms: Alternating Hemiplegia of Childhood Beyond ATP1A3," [Diseases journal](https://doi.org/10.3390/diseases14050166)). Other DEE genes (SCN1A, SCN2A, SCN8A, STXBP1, CDKL5, etc.) should be considered in the broader differential given phenotypic overlap in early-onset DEE.

**Screening:** No population-based newborn or carrier screening program exists for this ultra-rare de novo disorder; cascade/family screening is relevant primarily for the rare biallelic/recessive presentation.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No disease-specific mortality rate or life-expectancy data were located in the sources reviewed; RHOBTB2-RD is not classically described as directly life-limiting in the literature surveyed, though acute encephalopathic crises (fever/trauma-triggered, with severe EEG changes and MRI abnormalities) represent a recognized acute risk requiring urgent management.
- **Morbidity/function:** Substantial chronic morbidity from the combination of drug-resistant epilepsy, severe intellectual disability, and the paroxysmal movement disorder. Motor function outcomes span a wide spectrum — from complete lack of head control and non-ambulation to walking with a broad-based/unsteady gait — reflecting the broad genotype-driven severity spectrum.
- **Complications:** Acute encephalopathy episodes (fever- or trauma-triggered) with transient MRI/EEG abnormalities represent the most severe recognized complication category.
- **Prognostic factors:** The clearest identified prognostic determinant is **variant location** — BTB-domain variants predict earlier onset, more severe DEE, and drug-resistant epilepsy; GTPase-domain variants predict a milder, more variable course with better anti-seizure medication responsiveness. This genotype-phenotype correlation is the primary prognostic biomarker currently available (no molecular/biochemical prognostic biomarker has been validated).

---

## 12. Treatment

**Pharmacotherapy (seizure management — current standard of care):**
Antiseizure medications are the mainstay, with the most frequently used agents being:
- **Valproic acid** (CHEBI:39867) — NCIT: Pharmacotherapy (NCIT:C15986)
- **Levetiracetam** (CHEBI:6437)
- **Topiramate** (CHEBI:9366)
- **Oxcarbazepine** (CHEBI:7824)

These were used, for example, in combination (triple therapy: topiramate + valproic acid + oxcarbazepine) in the French Guiana case, achieving partial but incomplete seizure control ([PMC9184662](https://pmc.ncbi.nlm.nih.gov/articles/PMC9184662/)). Explicitly noted limitation: **"no treatments have been identified that address the other symptoms or the underlying pathophysiological mechanisms"** — i.e., current therapy is purely symptomatic for seizures and does not target the movement disorder, cognitive impairment, or the proteasomal-degradation mechanism itself.

**Pharmacogenomics:** No RHOBTB2-specific pharmacogenomic (drug-metabolism) data were identified.

**Emerging/experimental therapeutics:**
- **AI-guided drug repurposing:** A computational screen implicated **NSAIDs** — celecoxib (CHEBI:41423), diclofenac (CHEBI:47381), indomethacin (CHEBI:5773) — as potential RHOBTB2 pathway modulators, acting via downregulation of **E2F1** (the hypothesized apoptotic-signaling axis noted in §6). This is preclinical/in-silico and not yet in clinical use ([Frontiers Pediatrics 2024](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2024.1448793/full)).
- **Antisense oligonucleotide (ASO) therapy** targeting RHOBTB2 mRNA is described as "in development" — consistent with a rational precision-medicine approach given the gain-of-function/protein-accumulation mechanism (an ASO-mediated knockdown strategy would directly counter the pathogenic mechanism of excess mutant protein). No clinical trial identifier (NCT) was located for this program in the sources reviewed — this should be verified against ClinicalTrials.gov directly before curation, as no active registered trial was confirmed.

**Surgical/interventional:** No disease-specific surgical intervention (e.g., epilepsy surgery) was described as a standard approach in the literature reviewed, though it may be considered on a case-by-case basis for focal drug-resistant epilepsy as in general DEE management.

**Supportive/rehabilitative care:** Physical therapy, occupational therapy, and speech/communication therapy are inferred standard supportive management for the motor and speech impairments, consistent with general DEE management, though not explicitly detailed with RHOBTB2-specific outcome data in the sources reviewed. NCIT: Physical Therapy (NCIT:C15302); Rehabilitation (NCIT:C15315).

**Treatment outcomes:** Explicitly **drug-resistant epilepsy** is common; the disorder is generally refractory to standard antiseizure polytherapy in the more severe (BTB-domain) cases, while GTPase-domain-variant patients show comparatively better seizure control.

---

## 13. Prevention

Because RHOBTB2-RD arises from de novo germline variants with no known environmental causal contribution, classic primary prevention (risk-factor modification) is not applicable to preventing disease occurrence.

- **Tertiary prevention (preventing complications in affected individuals):** Given the documented fever- and head-trauma-triggered acute encephalopathy phenomenon, practical management should include **prompt, aggressive fever control** and **head-injury precaution/avoidance counseling** as a tertiary-prevention strategy to reduce acute encephalopathic crisis risk — this is directly supported by the trigger literature in §2, though no formal prospective prevention trial has validated this approach.
- **Genetic counseling:** Given the essentially universal de novo occurrence for the dominant missense variants, recurrence risk for future pregnancies in a family with an affected child is low (approximating general population risk, with residual risk from theoretical parental germline mosaicism) — standard genetic counseling practice for de novo dominant disorders. For the rare biallelic/recessive presentation, standard autosomal-recessive recurrence-risk counseling (25% per pregnancy) applies once both parental carrier variants are confirmed.
- **Prenatal/preimplantation testing:** Once a familial variant is known (e.g., after an affected child), prenatal diagnosis or preimplantation genetic testing could theoretically be offered for future pregnancies, per standard practice for known de novo monogenic disorders — no RHOBTB2-specific prenatal testing program was documented in the sources reviewed.
- **Screening:** No population or newborn screening program exists or is anticipated for this ultra-rare disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring RHOBTB2-associated disease in non-human species (companion animals, livestock, wildlife) was identified in this search — no OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case report surfaced. This appears to be a human-genetics-delineated disorder without a described natural-disease veterinary correlate at this time. This gap should be explicitly noted as "not identified" rather than assumed absent, since OMIA was not directly queried in this session.

**Orthology:** The *Drosophila melanogaster* ortholog is **RhoBTB** (single fly gene corresponding to the mammalian RhoBTB1/2/3 subfamily), used extensively as the primary in vivo functional model (see §6, §15). No specific mouse, rat, zebrafish, or other vertebrate ortholog gene ID was independently retrieved in this session beyond the human/mouse Wikipedia infobox coordinates (mouse *Rhobtb2* at chromosome 14, band 14 D2).

---

## 15. Model Organisms

| Model type | System | Manipulation | Key findings |
|---|---|---|---|
| Invertebrate (fly) | *Drosophila melanogaster*, ortholog *RhoBTB* | Pan-neuronal overexpression (mimicking BTB-domain gain-of-function/protein-accumulation) | Bang-sensitivity (seizure-like paralysis/spasms post-mechanical-shock); severe locomotor impairment (negative geotaxis assay); RNA-seq shows ion-channel-gene enrichment among differentially expressed genes ([Straub 2018, PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/); [HMG 2025](https://academic.oup.com/hmg/article/34/7/639/7976912)) |
| Invertebrate (fly) | *Drosophila*, dendritic arborization (da) neurons | Pan-neuronal/tissue-specific *RhoBTB* knockdown | Significantly reduced dendritic branch number and reduced total dendrite size/length, implicating RHOBTB2 in dendritic development; complete *RhoBTB*-null flies show seizures and motor degeneration |
| Cellular/patient-derived | Human iPSC-derived neurons (patient-specific lines) | Endogenous patient variants: BTB-domain vs. GTPase-domain vs. complete knockout, studied by whole-cell patch-clamp | BTB-domain variants → significantly altered excitability (increased AP firing frequency and half-width, decreased depolarization speed); GTPase-domain variants and complete knockout → **no significant electrophysiological alteration**, directly explaining the clinical genotype-phenotype divergence ([HMG 2025](https://academic.oup.com/hmg/article/34/7/639/7976912)) |
| Cell line (biochemical) | HEK293 transfection | Overexpression of wild-type vs. mutant RHOBTB2, ± proteasome inhibitor | Confirms impaired proteasomal degradation as the proximate mechanism of BTB-variant protein accumulation ([PMC5777381](https://pmc.ncbi.nlm.nih.gov/articles/PMC5777381/)) |
| Mammalian (indirect) | Rat, prenatal-malnutrition model | Not a direct patient-variant model; used to study RHOBTB2's normal role in learning/synaptic development | Validated RHOBTB2's role in learning and synaptic development; identified *Cebpa* as a transcriptional regulator of RHOBTB2 expression |

**Explicit modeling gap:** As of the most recent review located, **"no patient-variant animal models [e.g., knock-in mouse] have been generated"** to study RHOBTB2-related neurodevelopmental disease in vivo in a mammalian system — the iPSC-neuron and Drosophila systems represent the current state of the art, with the mammalian (mouse knock-in) gap flagged as an open need in the field ([Frontiers Pediatrics 2024](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2024.1448793/full)).

**Model limitations:** The Drosophila system captures dosage-sensitive seizure/locomotor and dendritic phenotypes but cannot recapitulate human-specific cortical architecture or the AHC-like alternating-hemiplegia clinical phenomenon. iPSC-neuron patch-clamp captures single-cell excitability changes but not network-level or whole-organism seizure semiology. No model to date recapitulates the postnatal-microcephaly or the fever/trauma-triggered acute-encephalopathy phenotypes specifically.

---

## Summary of Key Curation-Relevant Ontology Term Suggestions

- **Gene/protein:** HGNC:18756 (RHOBTB2); UniProt Q9BYZ6
- **Disease:** OMIM:618004 (DEE64); OMIM:607352 (gene locus entry) — MONDO ID should be independently confirmed
- **HPO (partial):** HP:0001250 (Seizure), HP:0001249 (Intellectual disability), HP:0005484 (Postnatal microcephaly), HP:0001252 (Hypotonia), HP:0001332 (Dystonia), HP:0001251 (Ataxia), HP:0002072 (Chorea), HP:0011722 (Drug-resistant seizures), HP:0001263 (Global developmental delay), HP:0006846 (episodic encephalopathy — verify exact term)
- **GO (mechanism):** GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process), GO:0031461 (cullin-RING ubiquitin ligase complex), GO:0000502 (proteasome complex)
- **CL:** CL:0000540 (neuron)
- **UBERON:** UBERON:0000955 (brain), UBERON:0002420 (basal ganglion), UBERON:0002037 (cerebellum)
- **CHEBI (treatments):** CHEBI:39867 (valproic acid), CHEBI:6437 (levetiracetam), CHEBI:9366 (topiramate), CHEBI:7824 (oxcarbazepine)
- **NCIT (treatment action):** NCIT:C15986 (Pharmacotherapy)

---

## Notable Evidence Gaps / Caveats for Curators

1. **gnomAD constraint metrics** (pLI, LOEUF, missense-Z) could not be retrieved directly in this session — verify at gnomad.broadinstitute.org before curating population-constraint claims.
2. **MONDO ID** for DEE64 was not independently confirmed — verify at mondo.monarchinitiative.org.
3. Several full-text sources (OMIM full clinical synopsis, GIM 2023 full text, Epilepsia 2026 full text) returned HTTP 403 on direct fetch; the summaries above rely on search-engine-indexed excerpts and secondary citations (Frontiers Pediatrics 2024 review, GeneCards, Wikipedia) rather than full primary-text extraction — **snippets used for KB curation should be independently re-verified against the cached/fetched primary abstract** per dismech's evidence SOP before being committed as `evidence.snippet` values.
4. No OMIA veterinary/natural-disease entry was directly queried — treat "no natural disease in other species identified" as an evidence gap, not a confirmed negative.
5. Precise phenotype frequency percentages (e.g., % with each seizure type, exact sex ratio) should be pulled directly from the largest cohort study (Epilepsia 2026, 91 cases) once full-text access is available, as only fragmentary percentages were recoverable via search snippets in this session.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `DOI:10.3389/fped.2024.1448793` *(abstract only)*: "from total lack of head control and inability to walk to walking with a broad-based or unsteady gait"
  - Text part not found as substring: 'from total lack of head control and inability to walk to walking with a broad-based or unsteady gait' (note: only abstract available for DOI:10.3389/fped.2024.1448793, full text may contain this excerpt)