---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-01T01:24:51.341418'
end_time: '2026-10-01T01:26:02.236298'
duration_seconds: 70.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acquired Epidermolysis Bullosa
  mondo_id: MONDO:0018747
  category: Autoimmune
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
  - claude-sonnet-5-5
  web_search_requests: 1
  num_turns: 10
  total_cost_usd: 0.8641530000000002
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acquired Epidermolysis Bullosa
- **MONDO ID:** MONDO:0018747 (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Acquired Epidermolysis Bullosa** covering all of the
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

# Research Report: Epidermolysis Bullosa Acquisita (Acquired Epidermolysis Bullosa), MONDO:0018747

**Date:** 2026-10-01

## Provenance and verification

- **Verified this session.** I retrieved these two sources:
  - Perković et al., *J Clin Med* 2023, **PMID:36769788**, "Epidermolysis Bullosa Acquisita—Current and Emerging Treatments" (full text read, [PMC9917799](https://pmc.ncbi.nlm.nih.gov/articles/PMC9917799/)).
  - Kim et al., "Clinical presentation, pathogenesis, diagnosis, and treatment of epidermolysis bullosa acquisita" (**PMID:23956869**, [PMC3727188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3727188/)). Only the search-result title and PMID pairing was seen. The page itself was blocked by a captcha.
- **Not verified.** The StatPearls chapter ([NBK554512](https://www.ncbi.nlm.nih.gov/books/NBK554512/)) was blocked, so I did not read it. Nothing else below was fetched. Everything not marked "verified" is background knowledge and should be treated as a lead.
- **No PMIDs from memory.** I deliberately give no PMID for landmark papers (Woodley, Sitaru, Ludwig and others) that I could not check. Each needs `just fetch-reference` before any snippet is quoted.
- **Suggested ontology terms** (HP, GO, CL, UBERON, NCIT) are leads only. The `dismech-terms` skill requires looking up each CURIE before binding it.
- **Existing entry.** `kb/disorders/Acquired_Epidermolysis_Bullosa.yaml` already exists, with MONDO:0018747 and a short two-node pathophysiology. This report is input for enriching it, not for creating a new entry.

---

## 1. Disease Information

- **Overview.** EBA is a rare, chronic, acquired autoimmune subepidermal blistering disease. IgG autoantibodies (occasionally IgA) target type VII collagen (COL7A1 product). Type VII collagen is the main component of the anchoring fibrils that tether the epidermal basement membrane to the papillary dermis. Antibody binding causes dermal-epidermal separation below the lamina densa.
- **Identifiers.**
  - MONDO:0018747, as in the existing KB entry.
  - ICD-10: L12.3 (acquired epidermolysis bullosa).
  - MeSH: Epidermolysis Bullosa Acquisita.
  - Orphanet and OMIM codes were not checked. Look them up with `just fetch-reference ORPHA:<code>`.
- **Synonyms.** EBA; acquired epidermolysis bullosa; anti-type VII collagen disease.
- **Data level.** The sources are aggregated, disease-level literature (reviews and case series). No EHR-derived data were used.

## 2. Etiology

- **Primary cause.** Loss of tolerance to the NC1 (non-collagenous 1) and other domains of type VII collagen, producing pathogenic autoantibodies.
- **Genetic risk.**
  - HLA-DR2 association; the Perković 2023 review (PMID:36769788) notes that "people of African descent carry the HLA-DRB1 risk allele." The specific allele (reported elsewhere as HLA-DRB1*15:03) is not verified here.
  - No Mendelian cause. This is not the inherited dystrophic EB caused by COL7A1 variants.
- **Associations (risk contexts).**
  - Inflammatory bowel disease, especially Crohn's disease. The review mentions the correlation, but the frequency was not verified.
  - Lymphoma. Perković 2023 reports an association "in 8% of patients."
  - Drug-associated cases, for example after a DPP-4 inhibitor ([case report PMC12812923](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12812923/), not read).
- **Protective factors and gene-environment interactions.** None established. No data found.

## 3. Phenotypes

Phenotype frequencies were not extracted from the sources I could read. Mark each frequency as "unspecified" in the KB unless it is curated from a primary source.

| Phenotype | Notes | Suggested HPO (verify first) |
|---|---|---|
| Subepidermal blistering | Core feature | HP:0008066 Abnormal blistering of the skin (already in the KB entry) |
| Skin fragility (mechanobullous form) | Trauma-prone sites (extensor surfaces, hands, feet) | to be looked up |
| Scarring, milia, nail dystrophy | Healing of mechanobullous lesions | to be looked up |
| Inflammatory bullae, pruritus | Widespread, in traumatic and non-traumatic areas | to be looked up |
| Mucosal erosions | Oral, ocular, esophageal | to be looked up |

- **Clinical types.** Two main types are distinguished: mechanobullous and inflammatory (search-result summary of the literature).
- **Onset.** Mostly adult, but not quantified here.
- **Course.** Chronic.
- **Quality of life.** No data retrieved.

## 4. Genetic/Molecular Information

- **Autoantigen.** COL7A1 (HGNC ID not looked up; use lowercase `hgnc:` and resolve it with `runoak`).
- **Pathogenic variants.** None. The disease is autoimmune.
- **Modifier genes.** HLA class II, as above.
- **Epigenetic and chromosomal findings.** Not available.

## 5. Environmental Information

- **Drug triggers.** Case reports exist, for example DPP-4 inhibitors (unverified beyond the title).
- **Lifestyle and infectious agents.** None established.
- **Mechanical trauma.** It determines where lesions form in the mechanobullous type.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps marked *inferred* are not demonstrated in the sources I read):

1. Genetic susceptibility, including HLA class II (HLA-DR2), plus unknown triggers, leads to loss of tolerance to type VII collagen (*the trigger is inferred*).
2. Autoreactive B and T cells produce IgG anti-COL7 autoantibodies, mainly against the NC1 domain.
3. The autoantibodies bind COL7 in the anchoring fibrils at the dermal-epidermal junction.
4. Binding has two consequences. It can directly impair COL7 function and its interaction with other basement membrane components. It can also recruit complement and Fcγ-receptor-bearing cells.
5. In the inflammatory pathway, neutrophils and other myeloid cells are activated and release proteases and reactive oxygen species. In experimental EBA this involves IFN-γ ([PMC11116581](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11116581/), title only).
6. The result is damage to the lamina densa and sublamina densa and dermal-epidermal separation.
7. Clinically, this produces tense subepidermal blisters, with scarring and milia when healing follows trauma.

- **Branching.** The mechanobullous type is driven by skin fragility. The inflammatory type is driven by immune-cell infiltration.
- **Suggested terms.**
  - GO: adaptive immune response; complement activation; neutrophil activation involved in immune response.
  - CL: B cell (CL:0000236), neutrophil (CL:0000775), plasma cell (CL:0000786).

## 7. Anatomical Structures Affected

- **Primary.** Skin, at the dermal-epidermal junction (the sublamina densa, where anchoring fibrils lie).
- **Secondary.** Oral, ocular and esophageal mucosa.
- **Suggested UBERON** (verify before binding): skin of body, basement membrane of epithelium, epidermis, dermis.
- **Subcellular.** Extracellular matrix and anchoring fibrils.
- **Lateralization.** Typically bilateral and symmetric at trauma-prone sites.

## 8. Temporal Development

- **Onset.** Adult.
- **Pattern.** Chronic, with relapses.
- **Remission.** Perković 2023 states that "complete remission off-treatment in EBA is impossible since maintenance therapy is needed." Treat this as a review-level claim, not an absolute.

## 9. Inheritance and Population

- **Incidence.** Perković 2023 gives "between 0.08 and 0.5 per million," with Germany the highest at 2.8 per million. A search-result summary states an incidence of 0.2 new cases per million per year.
- **Inheritance.** Not inherited (acquired). The HLA association is a susceptibility factor only.
- **Population.** HLA-DRB1 risk allele in people of African descent.
- **Sex ratio and age distribution.** Not verified.

## 10. Diagnostics

- **Direct immunofluorescence (DIF).** Linear IgG, and sometimes C3, deposits along the basement membrane zone.
- **Salt-split skin immunofluorescence.** The deposits localize to the dermal (floor) side, and a u-serrated pattern is a key differentiating feature.
- **ELISA.** Detects serum anti-COL7 (NC1) autoantibodies.
- **Combined criteria.** Perković 2023: "Positive DIF test, and ELISA showing patients' serum autoantibodies targeting Col7" constitute ideal diagnostic criteria.
- **Histology.** Subepidermal split. Infiltrate type was not verified.
- **Differential diagnosis.**
  - Bullous pemphigoid.
  - Mucous membrane pemphigoid.
  - Dystrophic EB.
  - Bullous SLE.
  - Porphyria cutanea tarda.
  - The KB already has entries for several of these.
- **Genetic testing and screening.** Not applicable.

## 11. Outcome/Prognosis

- Chronic course that needs maintenance therapy (Perković 2023).
- Complications: scarring, mucosal strictures, and risk related to immunosuppression. Specific figures were not retrieved.
- Survival and mortality data were not found. This is a gap.

## 12. Treatment

All details are from Perković 2023 (PMID:36769788) unless stated.

- **First line (search-result summary).** Systemic corticosteroids with dapsone. Colchicine and dapsone are listed as steroid-sparing agents.
- **Rituximab.** "Complete disease remission was achieved in 10 cases using the lymphoma protocol."
- **IVIG.** "After 16 to 31 IVIG infusion therapies...clinical remission was observed."
- **Emerging.**
  - Anti-FcRn therapy.
  - Anakinra (anti-IL-1).
  - Anti-GM-CSF antibodies.
  - Biologic case series: [PMC10371012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10371012/), title only.
- **Suggested NCIT terms** (look up each CURIE first): Pharmacotherapy (NCIT:C15986, listed in CLAUDE.md), with `therapeutic_agent` for dapsone, colchicine, rituximab and immunoglobulin; `therapeutic_modality` MONOCLONAL_ANTIBODY for rituximab and anti-FcRn agents.
- **Not covered.** Clinical trials (NCT IDs), pharmacogenomics and adverse-event data were not retrieved. Run `just fetch-reference` on any NCT ID before citing it.

## 13. Prevention

No primary prevention is known. Secondary and tertiary prevention rely on early diagnosis and trauma avoidance in the mechanobullous type. This is an inference and was not sourced.

## 14. Other Species / Natural Disease

No naturally occurring animal disease was found in the sources read. OMIA was not queried.

## 15. Model Organisms

- **Mouse.** The experimental EBA models are:
  - Passive transfer of anti-COL7 antibodies.
  - Active immunization with COL7 fragments.
- **Recapitulation.** Subepidermal blistering with neutrophilic involvement. IFN-γ inhibition impairs induction of experimental EBA (title-level only: [PMC11116581](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11116581/)).
- **Limitations and resources.** Not retrieved. In the KB these models belong in `animal_models:` with `modeled_mechanisms`.

---

## Gaps for curation follow-up

1. Fetch and cache PMID:36769788 and PMID:23956869 with `just fetch-reference`, then curate exact snippets.
2. Phenotype frequencies, mortality and survival, HLA allele-level data and drug-trigger evidence are unsourced.
3. Resolve the ontology IDs (COL7A1 HGNC, HP, UBERON, NCIT) by lookup before binding.
4. Add a `history/` record for any KB edit.

**Sources:**
- [Perković et al. 2023, EBA Current and Emerging Treatments (PMC9917799)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9917799/)
- [Kim et al., EBA review (PMC3727188)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3727188/)
- [PubMed 23956869](https://pubmed.ncbi.nlm.nih.gov/23956869/)
- [StatPearls EBA (NBK554512)](https://www.ncbi.nlm.nih.gov/books/NBK554512/)
- [Experimental EBA, IFN-γ (PMC11116581)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11116581/)
- [Biologic treatment case series (PMC10371012)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10371012/)
- [DPP-4 inhibitor case report (PMC12812923)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12812923/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000236` (1 mention) - the report calls it "CL: B cell"; CL calls it **B cell**

Every term resolved, and every label the report gave matched.