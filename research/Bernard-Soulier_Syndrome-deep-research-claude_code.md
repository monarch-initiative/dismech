---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-15T08:51:22.359002'
end_time: '2026-08-15T09:14:22.687379'
duration_seconds: 1380.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bernard-Soulier Syndrome
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
  web_search_requests: 2
  num_turns: 78
  total_cost_usd: 6.199841000000001
  session_id: 9ec06ef2-7211-41ce-82d5-4b92fc600f49
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 34
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bernard-Soulier Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bernard-Soulier Syndrome** covering all of the
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

# Bernard-Soulier Syndrome — Comprehensive Research Report

*Prepared 2026-08-15 for dismech KB curation. Everything with a PMID below was pulled from the live PubMed MEDLINE record during this session; quoted strings marked **[verbatim]** were transcribed straight out of the abstract text and are safe to use as evidence snippets. Ontology IDs marked **[OLS-checked]** were resolved against EBI OLS4 in this session; the rest are high-confidence-from-memory and **must** be run through `just validate-terms` before they go in a YAML file.*

sup. so Bernard-Soulier is one of those disorders where the whole story hangs off a single receptor that turned out to be doing two completely unrelated jobs at once — a docking cleat and a piece of structural scaffolding. Break it and you get *both* a platelet that can't stick to anything *and* a platelet that got built wrong in the first place. Two failures, one gene. That double duty is the thing to keep in your head through this entire report.

---

## 1. Disease Information

### Overview

Bernard-Soulier syndrome (BSS) is an inherited bleeding disorder of the megakaryocyte/platelet lineage caused by absence, deficiency, or dysfunction of the platelet **GPIb-IX-V complex** — the receptor that grabs von Willebrand factor (VWF). The clinical triad is (1) bleeding tendency out of proportion to the platelet count, (2) abnormally large platelets, and (3) thrombocytopenia.

> **[verbatim, PMID:17109744]** "Bernard-Soulier syndrome (BSS), also known as Hemorrhagiparous thrombocytic dystrophy, is a hereditary bleeding disorder affecting the megakaryocyte/platelet lineage and characterized by bleeding tendency, giant blood platelets and low platelet counts."
> — Lanza F. *Orphanet J Rare Dis.* 2006 Nov 16;1:46. doi:10.1186/1750-1172-1-46

> **[verbatim, PMID:39191409]** "Bernard-Soulier syndrome (BSS) is an inherited platelet function disorder caused by mutations in the genes that encode the glycoprotein (GP) Ibalpha and GPIbbeta subunits, as well as the GPIX subunit in the GPIbIX complex, which is located on the platelet surface and has roles in platelet adhesion and activation."
> — Kaya Z. *Semin Thromb Hemost.* 2025 Mar;51(2):209-218. doi:10.1055/s-0044-1789184 **← the current definitive review; use this one heavily**

### Key identifiers

| Resource | ID | Status |
|---|---|---|
| MONDO | **MONDO:0009276** — Bernard-Soulier syndrome | **[OLS-checked]** |
| MONDO (subtypes) | **MONDO:1060238** GP1BA-related; **MONDO:1060239** GP1BB-related; **MONDO:1060237** GP9-related | **[OLS-checked]** |
| MONDO (dominant form) | **MONDO:0007930** — Bernard-Soulier syndrome, type A2, autosomal dominant | **[OLS-checked]** |
| MONDO (veterinary) | **MONDO:1010672** — Bernard-Soulier syndrome, GP9-related, dog | **[OLS-checked]** |
| MeSH | **D001606** — Bernard-Soulier Syndrome | **[verified via NLM `id.nlm.nih.gov/mesh` lookup]** |
| Orphanet | **ORPHA:274** | high confidence; orpha.net was behind a bot-check this session — **verify**, and prefer citing the cached `ORPHA:274` structured record via `just structured-rebuild-orphanet` |
| OMIM | **#231200** (BSS); **#153670** (BSS type A2, AD); genes **\*606672** GP1BA, **\*138720** GP1BB, **\*173515** GP9, **\*173511** GP5 | omim.org returned HTTP 403 — **all OMIM numbers unverified this pass, check before curating** |
| ICD-10 | **D69.1** Qualitative platelet defects | high confidence |
| ICD-11 | **not verified** — the WHO browser is a JS app that WebFetch can't read. Use the ICD-11 Coding Tool. |

### Genes (HGNC) — **[OLS-checked, all four]**

| Gene | HGNC | Protein | Locus |
|---|---|---|---|
| GP1BA | `hgnc:4439` | GPIbα | 17p13.2 (Lanza 2006 says 17p12 — older mapping, use 17p13.2) |
| GP1BB | `hgnc:4440` | GPIbβ | 22q11.21 |
| GP9 | `hgnc:4444` | GPIX | 3q21.3 |
| GP5 | `hgnc:4443` | GPV | 3q29 — **never implicated in BSS** |

> **[verbatim, PMID:17109744]** "Genes coding for the four subunits of the receptor, GPIBA, GPIBB, GP5 and GP9, map to chromosomes 17p12, 22q11.2, 3q29, and 3q21, respectively. Defects have been identified in GPIBA, GPIBB, and GP9 but not in GP5."

### Synonyms / alternative names

- Hemorrhagiparous thrombocytic dystrophy (the original, gorgeously archaic name)
- Congenital hemorrhagiparous thrombocytic dystrophy
- Giant platelet syndrome
- BSS
- Macrothrombocytopenia, Bernard-Soulier type
- **Gene-based subtype nomenclature** (use this, it's the modern convention):

> **[verbatim, PMID:37416759]** "According to the affected gene, we distinguish BSS type A1 (GP1BA), type B (GP1BB), or type C (GP9)."
> — Sánchez-Guiu et al. (Toledo/CIEMAT group). *Mol Ther Nucleic Acids.* 2023 Sep 12;33:75-92. doi:10.1016/j.omtn.2023.06.020

Type **A2** is reserved for the autosomal *dominant* monoallelic GP1BA form.

### Data provenance

Everything here is **aggregated disease-level knowledge** — case reports, single-center case series, and one international consortium — **not** EHR-derived. There is no population-scale BSS cohort. The single largest genotyped collection is:

> **[verbatim, PMID:24934643]** "In order to collect information on BSS patients, we established an International Consortium for the study of BSS, allowing us to enrol and genotype 132 families (56 previously unreported). With 79 additional families for which molecular data were gleaned from the literature, the 211 families characterized so far have mutations in the GP1BA (28%), GP1BB (28%), or GP9 (44%) genes."
> — Savoia A et al. "Spectrum of the mutations in Bernard-Soulier syndrome." *Hum Mutat.* 2014 Sep;35(9):1033-45. doi:10.1002/humu.22607

---

## 2. Etiology

### Primary cause: genetic, monogenic, no environmental trigger required

BSS is purely genetic. There is no toxin, no pathogen, no lifestyle exposure that causes it. What environment *does* do is decide how loudly the bleeding phenotype talks.

**Two inheritance modes, two diseases in practice:**

> **[verbatim, PMID:39191409]** "Patients with autosomal recessively inherited biallelic BSS have a homozygous or compound heterozygous expression in the GPIbalpha, GPIbbeta, and GPIX subunits of the GPIbIX complex. Patients with autosomal dominantly inherited monoallelic BSS have a heterozygous expression in only the GPIbalpha and GPIbbeta subunits of the GPIbIX complex. To date, no BSS mutations in the GP5 gene have been reported."

That last sentence is worth a dedicated evidence item — the GP5-negative finding is a real, curatable negative claim, and it's corroborated mechanistically in mouse (see §15).

**Molecular consequence classes:**

> **[verbatim, PMID:24934643]** "Most of the mutations identified in the genes encoding for the GP1BA (GPIbalpha), GP1BB (GPIbbeta), and GP9 (GPIX) subunits prevent expression of the complex at the platelet membrane or more rarely its interaction with VWF. As a consequence, platelets are unable to adhere to the vascular subendothelium and agglutinate in response to ristocetin."

So: mostly **assembly/trafficking failure** (the complex never reaches the surface), occasionally **ligand-binding failure** (the complex is there but deaf to VWF). That's a genuine two-branch mechanism worth modeling as separate pathophysiology nodes.

### Genetic risk factors

- **Biallelic pathogenic variants in GP1BA / GP1BB / GP9** — causal, not "risk."
- **Consanguinity** — the single biggest population-level risk multiplier. > **[verbatim, PMID:24934643]** "Consistent with the rarity of the disease, 85% of the probands carry homozygous mutations with evidence of founder effects in some geographical areas."
  And from a Moroccan series: > **[verbatim, PMID:40703326]** "Second-degree consanguinity was found in six cases." (of seven)
- **Founder variants** — the best-characterized is the **Bolzano** allele: > **[verbatim, PMID:21933849]** "Analyses of the geographic origin of affected pedigrees and haplotypes indicated that this mutation originated in southern Italy." and "Our study indicates that monoallelic Bolzano mutation is the most frequent cause of inherited thrombocytopenia in Italy, affecting 20% of patients recruited at our institutions during the last 10 years."
- **22q11.2 deletion syndrome** — a structural predisposing genotype. Because GP1BB sits inside the commonly deleted interval, every 22q11.2DS patient is a hemizygote: > **[verbatim, PMID:38625506]** "Patients with 22q11.2 deletion syndrome (22q11.2DS) are obligate carriers of BSS because GP1BB resides on chromosome 22q11.2." A second-hit variant on the retained allele produces full BSS.

### Environmental risk factors

None that *cause* the disease. Factors that **unmask or worsen** the bleeding phenotype:

- Antiplatelet and anti-inflammatory drugs (aspirin, other NSAIDs) — layering a second platelet hit on a platelet that already can't stick
- Trauma, surgery, dental extraction, circumcision
- Menarche and menstruation
- Pregnancy and delivery
- Anticoagulants; some antibiotics and antihistamines reported to impair platelet function
- Iron-poor diet compounding chronic mucosal blood loss

**An important acquired mimic:** anti-GPIb/IX autoantibodies produce an acquired "pseudo-BSS" phenotype. A recent Moroccan series caught one: > **[verbatim, PMID:40703326]** "constitutional BSS was established in six patients, while one case was idiopathic acquired BSS." Do **not** curate acquired BSS as the same entity — it belongs as a differential, not a subtype.

### Protective factors

- **Genetic:** none identified. No modifier alleles have been established. Notably, a *negative* result — > **[verbatim, PMID:21173099]** "Regardless of mutations identified, the patients' bleeding diathesis did not correlate with thrombocytopenia, which was always moderate, and platelet GPIbalpha expression, which was always severely impaired." — which is exactly the shape you'd expect if unknown modifiers were doing the work.
- **Environmental/behavioral:** NSAID avoidance, contact-sport avoidance, meticulous dental hygiene, hormonal menstrual suppression, iron repletion, planned peripartum prophylaxis (§12).

### Gene-environment interactions

Essentially uncharacterized as a research topic. The clinically real one is **gene-drug**: a GPIb-deficient platelet exposed to aspirin, or to dual antiplatelet therapy after a coronary stent, is a genuinely hazardous combination. There is no PharmGKB/CPIC guideline for BSS.

---

## 3. Phenotypes

BSS phenotypes fall into three tidy buckets: laboratory abnormalities (obligate), mucocutaneous bleeding (near-universal but variable), and secondary consequences (iron deficiency).

### 3a. Laboratory abnormalities — the obligate core

| Phenotype | HP term | Frequency | Notes |
|---|---|---|---|
| Macrothrombocytopenia | **HP:0040185** **[OLS-checked]** | Obligate in biallelic BSS | The defining lab finding |
| Giant platelets | **HP:0001902** **[OLS-checked]** | Very frequent / obligate | Platelets can approach lymphocyte size |
| Thrombocytopenia | HP:0001873 *(verify)* | Very frequent; typically **moderate**, ~20–100 × 10⁹/L | Savoia: "a moderate thrombocytopenia" in all 13 patients |
| Impaired ristocetin-induced platelet aggregation | **HP:0011871** **[OLS-checked]** | Obligate in biallelic; variable in monoallelic | **Not** corrected by normal plasma — the discriminator vs VWD |
| Prolonged bleeding time | **HP:0003010** **[OLS-checked]** | Very frequent | Historic test; largely superseded |
| Increased mean platelet volume | HP:0011877 *(verify)* | Very frequent | MPV >12.4 fL cited in secondary sources |
| Abnormal platelet function | HP:0011869 *(verify)* | Obligate | Parent term |

Two under-cited lab findings worth curating because they are mechanistically informative:

> **[verbatim, PMID:17109744]** "Prothrombin consumption is markedly reduced."

This one is a fingerprint of the *procoagulant* arm of GPIb function (thrombin/FXI/FXII binding), not just the adhesion arm — and it is the kind of thing that gets dropped from modern write-ups.

> **[verbatim, PMID:21173099]** "Consistent with expression levels of GPIbalpha always lower than 10% of control values, platelet aggregation was absent or severely reduced."

### 3b. Bleeding phenotypes — clinical signs and symptoms

| Phenotype | HP term | Frequency |
|---|---|---|
| Epistaxis | HP:0000421 *(verify)* | Very frequent — consistently the #1 symptom |
| Menorrhagia | **HP:0000132** **[OLS-checked]** | **All** post-menarchal females in the Indian series |
| Gingival bleeding | **HP:0000225** **[OLS-checked]** | Very frequent |
| Purpura / ecchymoses | HP:0000979 *(verify)*; Bruising susceptibility HP:0000978 *(verify)* | Very frequent |
| Petechiae | HP:0000967 *(verify)* | Frequent |
| Gastrointestinal hemorrhage | HP:0002239 *(verify)* | Frequent |
| Prolonged bleeding after surgery / dental procedures | **HP:0004846** **[OLS-checked]** | Frequent |
| Post-partum hemorrhage | **HP:0011891** **[OLS-checked]** | ~53% of reported deliveries (see below) |
| Intracranial hemorrhage | HP:0002170 *(verify)* | Occasional; the main mortality driver |
| Iron deficiency anemia | HP:0001891 *(verify)* | Frequent, esp. females |

Frequency anchors from the literature:

> **[verbatim, PMID:17109744]** "Clinical manifestations usually include purpura, epistaxis, menorrhagia, gingival and gastrointestinal bleeding."

> **[verbatim, PMID:41100648]** "Epistaxis, ecchymosis, gingival bleed, gastrointestinal bleed, and soft tissue bleed were the commonest clinical manifestations. Menorrhagia was seen in all females in the reproductive age group."
> — Natural history & QoL study, India, 76 participants (64 GT, 12 BSS). *Indian J Med Res.* 2025 Aug.

> **[verbatim, PMID:36889343]** "In the literature review, postpartum hemorrhage (PPH) was found in 52.9% (27/51) of deliveries. Late PPH occurred more frequently than early PPH (35.3 and 31.4%, respectively). 49% (25/51) of pregnancies had severe thrombocytopenia, and antepartum hemorrhage was observed in 11.8% (6/51) of those."

**Curation caution on frequency bands:** per the dismech frequency-evidence SOP, most of these percentages come from *literature reviews of published pregnancies*, which is a heavily ascertainment-biased denominator. The 52.9% PPH figure supports a `FREQUENT`/`VERY_FREQUENT` band for PPH *in reported BSS pregnancies*, not in all BSS pregnancies. Quote the sentence, and say so in the `explanation`.

### 3c. Characteristics

- **Age of onset:** Biallelic — infancy/early childhood, often neonatal. Monoallelic — later, frequently adulthood.
  > **[verbatim, PMID:39191409]** "Patients with biallelic form are usually diagnosed at a young age, typically with mucocutaneous bleeding, whereas monoallelic forms are generally identified later in life and are frequently misdiagnosed with immune thrombocytopenic purpura (ITP)."
  > **[verbatim, PMID:40703326]** "Clinically, six patients had a history of hemorrhage since early childhood, while one patient presented with non-traumatic hemarthrosis at an advanced age compatible with acquired BSS."
- **Severity:** highly variable, and — this is the striking finding — **not predicted by genotype, platelet count, or receptor expression level.**
  > **[verbatim, PMID:21173099]** "Patients all had a moderate thrombocytopenia with giant platelets and a bleeding tendency whose severity varied among individuals." and "Aware of the limitations of our cohort, we cannot define any correlations."
  This is a genuine `KNOWLEDGE_GAP` for the dismech entry, not a gap in the literature search.
- **Progression:** **Non-progressive.** The underlying defect is static from birth. What changes is exposure — menarche, surgery, pregnancy, aging vasculature. The course is **episodic** against a stable baseline, lifelong.
- **Monoallelic Bolzano-type severity:** > **[verbatim, PMID:21933849]** "Although the clinical expression was variable, patients with this mutation typically had a mild form of Bernard-Soulier syndrome with mild thrombocytopenia and bleeding tendency. The most indicative laboratory findings were enlarged platelets and reduced GPIb/IX/V platelet expression; in vitro platelet aggregation was normal in nearly all of the cases."

### 3d. Quality of life

The best available data — and it's a genuinely useful, recent, multi-instrument study:

> **[verbatim, PMID:41100648]** "Health related quality of life (HRQoL) was captured using EuroQol five-dimensional questionnaire (EQ-5D), 36-Item short form health survey (SF-36) and functional assessment of chronic illness therapy (FACIT) scales. The severity of bleeding was assessed by annual bleed rate (ABR) and International Society on Thrombosis and Haemostasis - Bleeding assessment tool (ISTH-BAT) score."

> **[verbatim, PMID:41100648]** "The relationship between quality of life scores and ISTH-BAT score was weak."

That decoupling is important: bleeding score does not equal lived burden. The burden drivers appear to be chronic anemia/fatigue, treatment access, and school/work disruption rather than event count.

---

## 4. Genetic / Molecular Information

### Causal genes

Three, and only three. GP1BA, GP1BB, GP9 (HGNC IDs in §1). GP5 is the dog that didn't bark — see §15 for the mouse data explaining why.

### Mutational spectrum

> **[verbatim, PMID:24934643]** "There is a wide spectrum of mutations with 112 different variants, including 22 novel alterations."

Gene distribution across 211 families: **GP9 44%, GP1BA 28%, GP1BB 28%.**

**Variant classes represented:** missense, nonsense, frameshift (insertions and deletions), splice-site, and larger structural deletions. Concrete, recently published examples with proper HGVS from an Iranian cohort:

> **[verbatim, PMID:42229093]** "Sequencing of the GP9 gene revealed two novel frameshift deletions: c.151_154delGCCC and c.357delT. Variants identified in the GP1BB gene consisted of one known missense mutation (c.47 T > C) and a single-nucleotide deletion (c.390delC). In the GP1BA gene, we identified three cases with a c.624_625insT mutation and one case with a novel missense substitution (c.522 C>A)."
> — *Transfus Apher Sci.* 2026 Aug.

And a structural/in-frame example tied to 22q11.2:

> **[verbatim, PMID:38625506]** "Gene panel testing revealed a novel variant in GP1BB, p.(Val169_Leu172del)."

**The named founder allele:**

> **[verbatim, PMID:21933849]** "However, some years ago it was shown that the monoallelic c.515C>T transition in the GP1BA gene (Bolzano mutation) was responsible for macrothrombocytopenia in a few Italian patients."

That's **GP1BA c.515C>T, p.Ala156Val** — southern Italian founder, autosomal dominant, mild. It matters far out of proportion to its severity because it is *common*: 20% of inherited thrombocytopenia referrals in the Pavia/Trieste catchment, across 42 families / 103 cases. And the authors flag its diaspora: > **[verbatim, PMID:21933849]** "Because many people from southern Italy have emigrated during the last century, this mutation may have spread to other countries."

### Variant classification and allele frequency

- ACMG/AMP classification: the recurrent BSS alleles are largely **Pathogenic**/**Likely pathogenic** in ClinVar; null variants in genes with established LOF mechanism get PVS1. **Verify per-variant in ClinVar/VarSome before curating any specific classification.**
- **Allele frequencies:** biallelic BSS alleles are individually ultra-rare in gnomAD. I could not find a published gnomAD-based carrier-frequency analysis for BSS in this search — a PubMed query for exactly that returned zero hits. **This is a real literature gap**, and it matters, because the Bolzano data imply heterozygous BSS alleles are collectively much commoner than the biallelic disease prevalence would suggest. Flag as `KNOWLEDGE_GAP`.
- **Origin:** germline in all inherited cases. No somatic BSS. (Acquired autoantibody pseudo-BSS is immunological, not somatic-genetic.)

### Functional consequences

- **Predominant:** loss of function via failure of complex assembly/surface expression. Because GPIbα, GPIbβ, and GPIX must assemble stoichiometrically in the ER to traffic, a null in *any one* subunit collapses surface expression of *all* of them. This is why flow cytometry shows loss of CD42a **and** CD42b together, regardless of which gene is hit — a genuinely elegant diagnostic consequence of an assembly-dependent receptor.
- **Rarer:** expressed-but-nonfunctional receptor that cannot engage VWF (Savoia 2014, quoted above).
- **Structural rationale for missense variants:** > **[verbatim, PMID:21173099]** "Homozygous mutations were identified in the GP1BA, GP1BB and GP9 genes; six were novel alterations expected to destabilize the conformation of the respective protein."
- **The mirror-image disease:** *gain-of-function* GP1BA variants that increase VWF affinity cause **platelet-type (pseudo-) von Willebrand disease**, not BSS. Same gene, opposite functional direction, different disease. Curate as a differential with an explicit `functional_impact_category` contrast (`LOSS_OF_FUNCTION` vs `GAIN_OF_FUNCTION`).
- **Dominant-negative:** the mechanism proposed for monoallelic BSS/Bolzano — a mutant subunit that incorporates into the complex and drags down its assembly/stability, giving ~50%+ reduction rather than the ~50% you'd get from simple haploinsufficiency.

### Modifier genes

None established. But there is one delightful **cis-genomic modifier** — not a classical modifier gene, but a positional artifact:

> **[verbatim, PMID:15213102]** "The SEPT5 gene resides approximately 250 nucleotides 5' to the GP Ibbeta gene and has been associated with modulating exocytosis from neurons and platelets as part of a presynaptic protein complex. Fusion mRNA transcripts present in megakaryocytes can contain both the SEPT5 and GP Ibbeta coding sequences as a result in an imperfect polyadenylation signal within the 3' end of both the human and mouse SEPT5 genes. We observed a 2- to 3-fold increase in SEPT5 protein levels in platelets from GP Ibbeta(Null) mice."

> **[verbatim, PMID:15213102]** "These results implicate SEPT5 levels in the maintenance of normal alpha-granule size and may explain the variant granules associated with human GP Ibbeta mutations and the Bernard-Soulier syndrome."

Two genes 250 bp apart sharing a leaky polyadenylation signal, so knocking out one perturbs the other. That's a plumbing accident, and it predicts a *GP1BB-specific* α-granule phenotype not shared by GP1BA or GP9 forms. Worth a dedicated pathophysiology node on the GP1BB subtype.

### Epigenetics

No BSS-specific DNA methylation, histone, or chromatin data located. Not applicable at current evidence level.

### Chromosomal abnormalities

- **22q11.2 microdeletion** (DiGeorge/velocardiofacial) removes one GP1BB copy → obligate monoallelic BSS carriage, with macrothrombocytopenia and reduced GPIbα by flow.
  > **[verbatim, PMID:38625506]** "A 15-month-old girl without bleeding symptoms had giant platelets and thrombocytopenia. Physical findings and macrothrombocytopenia suggested 22q11.2DS, which was confirmed by fluorescence in situ hybridization. Flow cytometry showed decreased GPIbalpha on the platelets." and the practice point: "This case suggests that any patient with 22q11.2DS and macrothrombocytopenia should be further tested for BSS."
- **Canine analogue:** a 2,460-bp deletion spanning most of the single coding exon of GP9 (§14).

---

## 5. Environmental Information

Short section, honestly, and that's the finding.

- **Environmental factors:** none causal. No toxin, radiation, pollutant, or occupational exposure is implicated in BSS pathogenesis. CTD/TOXNET have nothing disease-specific.
- **Lifestyle factors:** modulate *expression* of bleeding, not risk of disease. Contact sports, NSAID/aspirin use, alcohol (adds platelet inhibition + variceal risk), and dietary iron adequacy are the practical levers.
- **Infectious agents:** not applicable as cause. Relevant only as (a) transfusion-transmitted infection risk from repeated platelet exposure and (b) *H. pylori*/mucosal lesions amplifying GI bleeding.
- **Iatrogenic:** repeated platelet transfusion → HLA and anti-GPIb alloimmunization → refractoriness, and in mothers → transplacental antibody causing fetal/neonatal alloimmune thrombocytopenia. This is the single most consequential "environmental" exposure in BSS care.

---

## 6. Mechanism / Pathophysiology

Here's the part where the metaphor earns its keep. GPIb-IX-V is doing two jobs that have nothing obvious to do with each other: it's the **grappling hook** the platelet throws at a damaged vessel wall, *and* it's a **tent pole** anchoring the membrane to the internal cytoskeleton while a megakaryocyte extrudes proplatelets. Delete it and both jobs fail — hence a bleeding disorder *and* a platelet-production disorder in the same patient. Model these as two parallel downstream branches from one shared upstream node.

### The receptor

> **[verbatim, PMID:23336709]** "The glycoprotein (GP)Ib-IX-V complex is the platelet receptor for von Willebrand factor and many other molecules that are critically involved in hemostasis and thrombosis. The lack of functional GPIb-IX-V complexes on the platelet surface is the cause of Bernard-Soulier syndrome, a rare hereditary bleeding disorder that is also associated with macrothrombocytopenia."
> — Li R, Emsley J. *J Thromb Haemost.* 2013 Apr. doi:10.1111/jth.12097

**Stoichiometry:** GPIbα : GPIbβ : GPIX : GPV in a **2 : 4 : 2 : 1** ratio. GPIbα is disulfide-linked to two GPIbβ chains; GPIX associates non-covalently; GPV associates loosely and is dispensable.

**Ligands beyond VWF** (the reason BSS is worse than a pure adhesion defect): thrombin, factor XI, factor XII, high-molecular-weight kininogen, P-selectin, and leukocyte integrin Mac-1 (αMβ2). Losing this hub also degrades platelet-leukocyte crosstalk and platelet-supported coagulation — which is exactly what "prothrombin consumption is markedly reduced" is reporting.

### Causal chain — proposed dismech pathograph

```
[MOLECULAR] Biallelic LOF variant in GP1BA / GP1BB / GP9
        │
        ▼
[MOLECULAR] Failure of GPIb-IX complex assembly in the megakaryocyte ER
        │  (assembly is obligate-stoichiometric: one null subunit sinks all)
        ▼
[CELLULAR] Absent or severely reduced GPIb-IX-V at the platelet/MK surface
        │
        ├──── BRANCH A: hemostatic failure ──────────────────────────────┐
        │                                                                │
        ▼                                                                ▼
[CELLULAR] Loss of VWF-A1 capture under high shear          [MOLECULAR] Loss of GPIbα
        │  → no tethering/rolling on subendothelium           thrombin/FXI/FXII/HK
        ▼                                                     binding sites
[CELLULAR] Failure of GPIb-IX outside-in signalling                      │
        │  → no inside-out activation of αIIbβ3                          ▼
        ▼                                                    [ORGANISM] Reduced
[TISSUE] Failure of primary hemostatic plug formation         prothrombin consumption
        │
        ▼
[ORGANISM] Mucocutaneous bleeding diathesis
        │
        ▼
[ORGANISM] Chronic blood loss → iron deficiency anemia

        └──── BRANCH B: thrombopoietic failure ─────────────┐
                                                             │
                                                             ▼
[CELLULAR] Loss of GPIbα cytoplasmic-tail linkage to filamin A / 14-3-3ζ
        │  → membrane skeleton uncoupled from the cytoskeleton
        ▼
[CELLULAR] Abnormal demarcation membrane system development in MK
        │
        ▼
[CELLULAR] Impaired proplatelet formation; deranged α-tubulin /
        │  microtubule marginal-band assembly; enlarged proplatelet tips
        ▼
[CELLULAR] Release of fewer, abnormally large platelets
        │
        ▼
[ORGANISM] Macrothrombocytopenia
```

Plus a modulating side-branch: **shear-triggered receptor unfolding → platelet clearance** (below), and, for GP1BB specifically, **SEPT5 dysregulation → enlarged α-granules**.

### Branch A — adhesion and activation

Under arterial shear, VWF unfurls on exposed subendothelium and its A1 domain is the only thing fast enough to catch a platelet moving at that velocity. GPIbα is the catcher's mitt. Without it there is no capture step, so nothing downstream — αIIbβ3 activation, firm adhesion, spreading, aggregate growth — ever gets started. The clinical signature is a bleeding severity **disproportionate to the platelet count**:

> **[verbatim, PMID:10706630]** "The bleeding in patients with the Bernard-Soulier syndrome is disproportionately more severe than suggested by the reduced platelet count and is explained by a defect in primary hemostasis owing to the absence of the platelet glycoprotein (GP) Ib-IX-V membrane receptor."

The functional readout of Branch A in the lab is the **absent ristocetin response** — ristocetin artificially promotes VWF-A1/GPIbα engagement, so a platelet with no GPIbα simply cannot agglutinate no matter how much normal plasma you add. That's the whole diagnostic logic in one sentence.

### Branch B — thrombopoiesis (the part that took 50 years to work out)

> **[verbatim, PMID:10706630]** "However, the molecular basis for the giant platelet phenotype and thrombocytopenia have remained unresolved but assumed to be linked to an absent receptor complex. We have disrupted the gene encoding the alpha-subunit of mouse GP Ib-IX-V (GP Ibalpha) and describe a murine model recapitulating the hallmark characteristics of the human Bernard-Soulier syndrome. The results demonstrate a direct link between expression of a GP Ib-IX-V complex and normal megakaryocytopoiesis and platelet morphogenesis."
> — Ware J, Russell S, Ruggeri ZM. *Proc Natl Acad Sci U S A.* 2000 Mar 14;97(6):2803-8

The cell-biological detail, in mouse:

> **[verbatim, PMID:19377075]** "The number of megakaryocyte progenitors, their differentiation and progressive maturation into distinct classes and their level of endoreplication were normal in GPIbbeta(-/-) bone marrow. However, the more mature cells exhibited ultrastructural anomalies with a thicker peripheral zone and a less well developed demarcation membrane system."

> **[verbatim, PMID:19377075]** "GPIbbeta(-/-) megakaryocytes could be differentiated in culture from Lin(-) fetal liver cells in normal amounts but the proportion of cells able to extend proplatelets was decreased by 41%."

> **[verbatim, PMID:19377075]** "The marginal microtubular ring contained twice as many tubulin fibers in GPIbbeta(-/-) proplatelet buds in cultured and circulating platelets."

> **[verbatim, PMID:19377075]** "Altogether, these findings point to a role of the GPIb-V-IX complex intrinsic to megakaryocytes at the stage of proplatelet formation and suggest a functional link with the underlying microtubular cytoskeleton in platelet biogenesis."
> — Strassel C et al. *Haematologica.* 2009.

And — critically for translational validity — **the same defect is demonstrable in human megakaryocytes**, in monoallelic Bolzano patients:

> **[verbatim, PMID:19067792]** "Megakaryocyte differentiation from both cord blood (one patient) and peripheral blood (five patients) was comparable to controls. However, proplatelet formation was reduced by about 50% with respect to controls."

> **[verbatim, PMID:19067792]** "Morphological evaluation of proplatelet formation revealed an increased size of proplatelet tips, which was consistent with the increased diameters of patients' blood platelets. Moreover, alpha-tubulin distribution within proplatelets was severely deranged."

> **[verbatim, PMID:19067792]** "These results suggest that a defect of platelet formation contributes to macrothrombocytopenia associated to the Bolzano mutation, and indicate a key role for GPIb alpha in proplatelet formation."
> — Balduini A et al. *J Thromb Haemost.* 2009 Mar;7(3):478-84

That human-plus-mouse convergence is unusually strong for a rare disease and should be curated as `IN_VITRO` (human MK culture) **plus** `MODEL_ORGANISM` evidence on the same node — not one standing in for the other.

**Which part of GPIbα drives Branch B?** An elegant chimera experiment separates the extracellular and cytoplasmic contributions:

> **[verbatim, PMID:12200373]** "The characterization of these mice revealed a 2-fold increase in circulating platelet count and a 50% reduction in platelet size when compared with platelets from the mouse model of the Bernard-Soulier syndrome. Immunoprecipitation confirmed that the IL-4Ralpha/GP Ibalpha subunit interacts with filamin-1 and 14-3-3zeta, known binding proteins to the GP Ibalpha cytoplasmic tail. Mice expressing the chimeric receptor retain a severe bleeding phenotype, confirming a critical role for the GP Ibalpha extracytoplasmic domain in hemostasis."
> — Kanaji T et al. *Blood.* 2002 Sep 15

Read that carefully: replacing the *outside* of GPIbα with an unrelated domain **fixes half the macrothrombocytopenia** while leaving the bleeding phenotype intact. The cytoplasmic tail (filamin A / 14-3-3ζ) drives platelet size and count; the ectodomain drives hemostasis. Two jobs, two domains, cleanly dissociable. That's a beautiful piece of evidence for the two-branch model above.

### Mechanosensing and platelet clearance

> **[verbatim, PMID:27670775]** "Mechanisms by which blood cells sense shear stress are poorly characterized. In platelets, glycoprotein (GP)Ib-IX receptor complex has been long suggested to be a shear sensor and receptor. Recently, a relatively unstable and mechanosensitive domain in the GPIbalpha subunit of GPIb-IX was identified. Here we show that binding of its ligand, von Willebrand factor, under physiological shear stress induces unfolding of this mechanosensory domain (MSD) on the platelet surface. The unfolded MSD, particularly the juxtamembrane 'Trigger' sequence therein, leads to intracellular signalling and rapid platelet clearance."
> — Deng W et al. *Nat Commun.* 2016 Sep 27

This is the newest mechanistic layer and it's under-integrated into BSS thinking: GPIbα is a **mechanoreceptor** whose unfolding is a platelet-lifespan timer. Missense variants that destabilize the MSD could, in principle, shorten platelet survival independently of production — a plausible third contributor to thrombocytopenia. **Curate as an `EMERGING` mechanistic hypothesis, not as canonical**; the direct link from BSS-causing variants to accelerated clearance in patients has not, to my reading, been demonstrated.

### GPIbβ has its own signalling role — with a surprise

> **[verbatim, PMID:27148783]** "On the other hand, deletion of the C-flanking 159-170 segment allowed normal GPIb-IX expression, VWF-dependent responses and bleeding times, but resulted in enhanced arterial thrombosis." and "This pointed to a repressor role of GPIbbeta in thrombus formation in vivo that was not predicted in studies of heterologous cells."
> — Strassel C et al. *J Thromb Haemost.* 2016

So GPIbβ's cytoplasmic tail is partly a *brake* on thrombosis. Note the explicit heterologous-cell/in-vivo discordance — a textbook `HUMAN_MODEL_MISMATCH`-adjacent finding (here it's cell-line-vs-mouse rather than mouse-vs-human, but the epistemic shape is identical).

### Suggested ontology terms

**GO biological process:**
- `GO:0030220` platelet formation **[OLS-checked]** — Branch B core, `modifier: DECREASED`
- `GO:0036344` platelet morphogenesis **[OLS-checked]** — Branch B, `modifier: ABNORMAL`/`DECREASED`
- `GO:0030168` platelet activation **[OLS-checked]** — Branch A, `DECREASED`
- `GO:0070527` platelet aggregation *(verify)* — Branch A, `DECREASED`
- `GO:0007596` blood coagulation *(verify)* — `DECREASED`
- `GO:0002576` platelet degranulation *(verify)* — relevant to the GP1BB/SEPT5 α-granule branch
- `GO:0007018` microtubule-based movement *(verify)* / microtubule cytoskeleton organization — proplatelet branch
- `GO:0051017` actin filament bundle assembly *(verify)* — filamin A linkage

**GO cellular component:**
- `GO:0005886` plasma membrane *(verify)* — where the complex should be and isn't
- `GO:0005783` endoplasmic reticulum *(verify)* — where assembly fails
- `GO:0031091` platelet alpha granule *(verify)* — GP1BB/SEPT5 branch

**GO molecular function:** the obvious one — *von Willebrand factor binding* — **does not exist in GO** (OLS query returned zero hits this session). Use `GO:0005515` protein binding or a receptor-activity term, and note the ontology gap. This is a legitimate OBO gap to surface.

**Cell Ontology:**
- `CL:0000556` megakaryocyte **[OLS-checked]**
- `CL:0000233` platelet *(verify)*
- `CL:0000553` megakaryocyte progenitor cell **[OLS-checked]**

**CHEBI:** `CHEBI:85129` ristocetin **[OLS-checked]** (note: `CHEBI:201477` Ristocetin sulfate, `CHEBI:201735` Ristocetin A sulfate also exist — pick the aglycone-free base for the reagent)

### Molecular profiling

- **Transcriptomics:** no BSS-specific published transcriptomic signature located. GP9-KO and patient-derived iPSC megakaryocyte systems now exist (PMID:37416759) and are the obvious substrate for one. **Gap.**
- **Proteomics:** no BSS-specific proteomic dataset located. The SEPT5 finding (PMID:15213102) is a targeted immunoblot result, not discovery proteomics.
- **Metabolomics / lipidomics:** none identified. Not applicable at present.
- **Single-cell / spatial:** none BSS-specific identified. Bone-marrow megakaryocyte scRNA-seq atlases exist generally but no BSS cohort.
- **Functional genomics screens:** no BSS-focused CRISPR/RNAi screen located; the gene-editing work in PMID:37416759 is targeted KO generation, not a screen.

For dismech `datasets:` — **do not fabricate accessions.** Run `just discover-datasets Bernard-Soulier_Syndrome` and triage relevance manually; note the short-gene-symbol NEC hazard applies hard here (`GP5`, `GP9` will collide with unrelated titles constantly).

---

## 7. Anatomical Structures Affected

BSS is a **blood and bone marrow** disease whose *symptoms* appear at mucosal surfaces. Nothing is structurally diseased in the vessel wall, the liver, or anywhere else.

### Organ level

**Primary:**
- Bone marrow — `UBERON:0002371` *(verify)* — site of the defective thrombopoiesis
- Blood / circulating platelet pool — `UBERON:0000178` blood *(verify)*

**Secondary (bleeding sites, not diseased tissue):**
- Nasal cavity / nasal mucosa — epistaxis — `UBERON:0001707` nasal cavity *(verify)*
- Gingiva / oral mucosa — `UBERON:0001828` gingiva *(verify)*
- Gastrointestinal tract mucosa — `UBERON:0001555` digestive tract *(verify)*
- Endometrium / uterus — menorrhagia, PPH — `UBERON:0001295` endometrium *(verify)*
- Skin — purpura, ecchymoses, petechiae — `UBERON:0002097` skin of body *(verify)*
- Brain — intracranial hemorrhage (rare, high-lethality) — `UBERON:0000955` brain *(verify)*
- Joints — hemarthrosis is *atypical* for BSS (it's a coagulation-factor pattern), and its appearance should prompt a rethink — note the Moroccan acquired case presented that way

**Body systems:** hematologic/hematopoietic (primary); cardiovascular (as the compartment); integumentary, digestive, respiratory (upper), reproductive (as bleeding sites).

### Tissue and cell level

- **Megakaryocyte** (`CL:0000556` **[OLS-checked]**) — the cell where the disease is actually *made*. Progenitor number, differentiation, and endoreplication are **normal**; the defect is at the terminal proplatelet-extrusion step (PMID:19377075). That's an important negative — don't model it as a proliferation defect.
- **Platelet** (`CL:0000233`) — the cell that carries the defect out into circulation. Abnormally large but, notably, **still discoid**: > **[verbatim, PMID:19377075]** "GPIbbeta(-/-) released platelets were larger but retained a typical discoid shape."
- **Vascular endothelium / subendothelium** — the *partner* tissue. Not diseased; it's the substrate the platelet fails to engage.
- Blood vessel — `UBERON:0001981` *(verify)*

### Subcellular level

- **Plasma membrane** (`GO:0005886`) — where the receptor is absent
- **Endoplasmic reticulum** (`GO:0005783`) — where subunit assembly fails and misassembled subunits are retained/degraded
- **Demarcation membrane system** — the megakaryocyte's internal membrane reservoir; poorly developed in GPIbβ-null MK. **No clean GO term** for DMS that I could confirm — another ontology gap worth flagging.
- **Marginal microtubule band / α-tubulin cytoskeleton** — doubled fiber count in mutant proplatelet buds
- **α-granule** (`GO:0031091`) — enlarged in the GP1BB/SEPT5 branch
- **Membrane skeleton** — filamin A / 14-3-3ζ linkage

### Localization and laterality

**Systemic and bilateral by nature** — this is a circulating-cell disorder, so there is no laterality. Bleeding sites are wherever mucosa meets mechanical stress. No focal or asymmetric anatomical pattern.

---

## 8. Temporal Development

### Onset

- **Pattern:** congenital genotype, **insidious-to-early** clinical onset. The receptor has been missing since fetal megakaryopoiesis; it just takes a hemostatic challenge to reveal it.
- **Biallelic BSS:** neonatal to early childhood. Classic revealing events — bleeding at circumcision, prolonged umbilical-stump or venipuncture oozing, easy bruising as the child becomes mobile, epistaxis in the toddler years.
- **Monoallelic BSS:** adolescence to adulthood, often incidentally on a CBC, or after a "refractory ITP" odyssey.
- **Diagnostic delay is the norm.** Mean age at diagnosis around 16 years is cited in secondary sources (StatPearls, NBK557671 — **secondary, verify against primary**); the Moroccan series had a mean age of 21 years despite childhood-onset symptoms in 6/7.

### Progression

- **Rate:** non-progressive. The underlying lesion does not worsen.
- **Course pattern:** **episodic** on a stable baseline. Bleeding events cluster around hemostatic challenges rather than accumulating.
- **Duration:** chronic, lifelong.
- **Stages:** BSS has no formal staging system. If you need an axis, use **ISTH-BAT bleeding score** and **annual bleed rate (ABR)** — both were applied to BSS in PMID:41100648 — rather than inventing stages.

### Patterns

- **Remission:** none spontaneous. Treatment-induced remission of *bleeding* (not of the disorder) is achievable — most durably in the eltrombopag long-term arm: > **[verbatim, PMID:31273088]** "Four patients with clinically significant spontaneous bleeding entered a program of long-term eltrombopag administration (16 additional weeks): all of them obtained remission of mucosal hemorrhages, with the remission persisting throughout the treatment period."
- **A false remission worth naming:** splenectomy performed under a mistaken ITP diagnosis produces temporary improvement, which then reinforces the wrong diagnosis. > **[verbatim, PMID:41853404]** "She was misdiagnosed and treated for ITP, and due to refractory symptoms, she underwent splenectomy and experienced temporary symptom improvement. However, the symptoms returned, and further workup with ristocetin and flow cytometry confirmed her diagnosis of BSS." That's an iatrogenic-harm pathway worth curating explicitly.

### Critical periods (windows of vulnerability / intervention)

1. **Neonatal period** — circumcision, heel-stick, and the ICH window; plus FNAIT risk if the mother is alloimmunized
2. **Menarche** — frequently the presenting crisis in females; a planned hormonal + antifibrinolytic strategy *before* menarche is the highest-yield preventive intervention in BSS
3. **Any surgical or dental procedure** — plan, don't react
4. **Pregnancy and the peripartum window** — including the **late** PPH window, which in BSS is *more* common than early PPH (35.3% vs 31.4%, PMID:36889343). Post-discharge is not safe territory.
5. **First transfusion** — the alloimmunization clock starts here; HLA-typing and leukoreduction decisions made at diagnosis determine options a decade later

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence: <1 per 1,000,000** for classical biallelic BSS.

> **[verbatim, PMID:34878196]** "Bernard-Soulier syndrome (BSS) is an inherited bleeding disorder characterized by macroplatelets and thrombocytopenia, prolonged bleeding time, and a prevalence of less than 1 in 1,000,000."

Orphanet-style class: `BELOW_1_IN_1000000`; `rate_per_100000` ≈ **0.1** (upper bound). Note this figure is very likely an **underestimate** — every review says so, and the two independent reasons are (a) monoallelic BSS masquerading as ITP and (b) undiagnosis in low-resource settings.

**Cumulative reported cases:**
> **[verbatim, PMID:17109744]** "This syndrome is extremely rare as only approximately 100 cases have been reported in the literature." (2006)
> **[verbatim, PMID:40703326]** "Bernard-Soulier syndrome (BSS) is a rare thrombopathy with only a few hundred cases reported in the medical literature." (2025)

**Genotyped families:** 211 (Savoia 2014 consortium).

**Incidence:** no published incidence rate located. **Gap.**

### Regional variation

- **Consanguineous populations are markedly enriched.** > **[verbatim, PMID:40703326]** "BSS is a thrombopathy that can be either constitutional or acquired, with a relatively high prevalence in Morocco, and should not be underestimated." Seven BSS-compatible profiles out of 268 platelet-aggregation tests over four years at one Rabat center.
- **Italy** — the Bolzano allele makes *monoallelic* BSS the commonest inherited thrombocytopenia in the country (20% of referrals), with southern Italian origin and probable diaspora spread.
- **Founder effects generally:** > **[verbatim, PMID:24934643]** "...85% of the probands carry homozygous mutations with evidence of founder effects in some geographical areas."
- **Iran, Turkey, North Africa, South Asia, Middle East** — repeatedly represented in the case-series literature, consistent with consanguinity structure.

### Inheritance

- **Autosomal recessive** for classical biallelic BSS (types A1, B, C)
- **Autosomal dominant** for monoallelic BSS (type A2; GP1BA and GP1BB only, never GP9 in the dominant form per Kaya 2025)
- **Penetrance:** essentially complete for the *laboratory* phenotype (macrothrombocytopenia) in biallelic disease. Incomplete/variable for clinically significant bleeding — and even for detection in the monoallelic form, where a 15-month-old carried the full lab picture "without bleeding symptoms" (PMID:38625506).
- **Expressivity: highly variable, uncorrelated with genotype.** This is the single most robustly replicated negative finding in BSS genetics (PMID:21173099).
- **Anticipation:** not applicable — no repeat expansion mechanism.
- **Germline mosaicism:** not reported.
- **Consanguinity:** major driver (above).
- **Carrier frequency:** heterozygous carriers of classical recessive alleles are generally **asymptomatic with normal or near-normal platelets** — with one important exception:
  > **[verbatim, PMID:21173099]** "Except for obligate carriers of a GP9 mutation with a reduced GPIb/IX/V expression and defective aggregation, all the other carriers had no obvious anomalies."
  > and: "Obligate carriers had features similar to controls though their GPIb/IX/V expression showed discrepancies."
  So: some GP9 heterozygotes are *not* silent. Curate carrier status as `variable`, not `unaffected`.
  No gnomAD-based carrier-frequency estimate for BSS alleles was located. **Gap.**

### Demographics

- **Sex ratio:** ~1:1 expected (autosomal). Reported series deviate on small numbers — the Moroccan series reported a sex ratio of 2.5 (n=7), which is noise, not signal. **Females carry disproportionate morbidity** (menorrhagia, iron deficiency, pregnancy risk) even at equal prevalence — that's a burden asymmetry, not an incidence asymmetry, and the distinction matters for how you curate it.
- **Age distribution:** all ages; biallelic patients are ascertained in childhood, monoallelic in adulthood. Median age 14 in the Indian GT/BSS cohort; mean 21 in the Moroccan BSS series.
- **Ethnic groups:** no ethnicity is intrinsically predisposed; the enrichment tracks **consanguinity rates and founder history**, which is a different claim and should be curated as such.

---

## 10. Diagnostics

### The diagnostic logic in one paragraph

Macrothrombocytopenia + mucocutaneous bleeding + **absent ristocetin-induced aggregation that normal plasma does not fix** + **flow-cytometric loss of CD42a/CD42b** = BSS. Genetics confirms and subtypes. Everything else is ruling out the mimics.

### The definitive modern statement of the biallelic-vs-monoallelic diagnostic split

> **[verbatim, PMID:39191409]** "In biallelic BSS, giant platelets in the peripheral blood smear, absence of ristocetin-induced platelet aggregation (RIPA) using light transmission aggregometry (LTA), and complete loss of GPIbIX complex in flow cytometry are observed, whereas in monoallelic forms, genetic diagnosis is recommended due to the presence of large platelets in the peripheral blood smear, decreased or normal RIPA response in LTA, and partial loss or normal GPIbIX complex in flow cytometry."

That single sentence should anchor the whole `definitions` block. Note the operational consequence: **in monoallelic BSS the functional tests can be normal, so genetics is not confirmatory-optional, it's primary.**

### Laboratory tests

| Test | Finding in BSS | Notes |
|---|---|---|
| CBC + MPV | Thrombocytopenia (typically 20–100 × 10⁹/L), MPV elevated (>12.4 fL cited) | **Automated counters undercount giant platelets** by sizing them as leukocytes — always confirm on smear |
| Peripheral blood smear | Giant platelets, reduced number | Cheap, fast, and the most under-used test in this disease |
| Light transmission aggregometry (LTA) | **Absent/severely reduced RIPA; normal response to ADP, collagen, arachidonic acid, epinephrine**; occasional thrombin hyporesponsiveness | The isolated ristocetin defect is the signature |
| RIPA + normal plasma mixing | **No correction** | Discriminates BSS (receptor absent) from VWD (ligand absent) |
| Flow cytometry | ↓↓ **CD42a (GPIX)**, ↓↓ **CD42b (GPIbα)**; also CD42c (GPIbβ), CD42d (GPV) | Confirmatory; works in neonates and on tiny samples |
| Bleeding time | Markedly prolonged | Historic; largely abandoned |
| PFA-100 closure time | Prolonged (collagen/ADP and collagen/epinephrine) | Screening only |
| Prothrombin consumption | **Markedly reduced** (PMID:17109744) | Classic, informative, nearly forgotten |
| Iron studies / ferritin | Microcytic hypochromic anemia in 4/7 Moroccan cases | Monitor, don't just treat once |
| ISTH-BAT | Quantifies bleeding phenotype | Validated and used in BSS (PMID:41100648) |

> **[verbatim, PMID:40703326]** "Platelet aggregation showed a normal response to all inducers except ristocetin."

### Biomarkers

There is no soluble biomarker for BSS. The "biomarker" is the receptor itself, measured on the cell — surface CD42b/CD42a density by flow, expressed as % of control. Savoia's cohort anchors the biallelic threshold: **GPIbα <10% of control** (PMID:21173099).

**LOINC:** platelet count, MPV, and platelet-aggregation panels have LOINC codes; CD42b flow does too. Look these up — I did not resolve specific LOINC IDs this session, and per the dismech `reference_ranges` guidance, an interval needs a citable source, not a guessed code.

### Imaging, functional, electrophysiology, biopsy

- **Imaging:** no diagnostic role. Used only to characterize a bleed (CT head for suspected ICH, ultrasound/CT for internal hemorrhage).
- **Functional / electrophysiology:** not applicable.
- **Bone marrow biopsy:** **not required and not recommended for diagnosis.** If done (usually during an ITP workup), megakaryocytes are present in normal-to-increased number with abnormal ultrastructure — which is the point: the marrow looks *unhelpfully normal* on light microscopy, and that reassures people toward the wrong diagnosis.
- **Electron microscopy:** research-grade; shows the DMS and α-granule abnormalities.

### Genetic testing

**Recommended approach:** targeted **inherited-platelet-disorder / inherited-thrombocytopenia gene panel** covering GP1BA, GP1BB, GP9 alongside MYH9, ACTN1, TUBB1, FLNA, ITGA2B, ITGB3, RUNX1, ANKRD26, ETV6, WAS, etc. Panel-first is right because the clinical differential is genetically broad and phenotypically overlapping.

- **Gene panel:** first-line. Worked in PMID:38625506 ("Gene panel testing revealed a novel variant in GP1BB").
- **Single-gene / Sanger:** appropriate when a founder allele is suspected (Bolzano c.515C>T in an Italian-ancestry patient; a known familial variant for cascade testing). PMID:42229093 used PCR + Sanger across all three genes successfully.
- **WES:** reasonable when the panel is negative and the phenotype is syndromic.
- **WGS:** catches the structural and deep-intronic variants panels miss — this is exactly how the canine 2,460-bp GP9 deletion was found (PMID:31484196), and the same logic applies in humans.
- **FISH / chromosomal microarray:** **mandatory if 22q11.2DS is suspected**, and the reverse rule from PMID:38625506: any 22q11.2DS patient with macrothrombocytopenia should be tested for BSS.
- **Karyotype:** low yield except for 22q11.2 context.
- **mtDNA testing / repeat expansion testing:** not applicable.

### Omics-based diagnostics

Not established for BSS. RNA-seq could in principle resolve splice variants of uncertain significance; no published BSS diagnostic RNA-seq protocol located. Proteomics, metabolomics, epigenomics, liquid biopsy: **not applicable.**

### Clinical criteria

No formal consensus diagnostic criteria (no DSM/ICD-style checklist). The operative criteria are the ISTH SSC guidance on diagnosis of inherited platelet disorders plus the phenotype-test combination above. Kaya 2025 provides the most usable modern criteria set.

### Differential diagnosis

| Condition | Distinguishing feature |
|---|---|
| **Immune thrombocytopenia (ITP)** | Acquired, no family history, **platelets normal-sized**, responds to steroids/IVIG, normal RIPA and normal CD42b. **The single most consequential misdiagnosis** — leads to steroids, IVIG, and splenectomy |
| **Type 2B VWD** | **Increased**, not decreased, RIPA at low-dose ristocetin; VWF multimer abnormality |
| **Platelet-type (pseudo-) VWD** | *Gain-of-function* GP1BA; also enhanced low-dose RIPA; corrected by plasma-vs-platelet mixing studies |
| **MYH9-related disease** (May-Hegglin, Sebastian, Fechtner, Epstein) | Leukocyte Döhle-like inclusions; nephropathy, deafness, cataract; normal RIPA and CD42b |
| **Gray platelet syndrome (NBEAL2)** | Pale, agranular platelets; absent α-granules; myelofibrosis |
| **Paris-Trousseau / Jacobsen (11q del, FLI1)** | Giant α-granules; 11q deletion; dysmorphism |
| **22q11.2DS / DiGeorge** | Macrothrombocytopenia *plus* cardiac, palatal, immune, endocrine features — and the GP1BB mechanistic link |
| **ACTN1, TUBB1, FLNA-related macrothrombocytopenia** | Normal GPIb-IX-V by flow |
| **ITGA2B/ITGB3-related macrothrombocytopenia** | Reduced CD41/CD61, not CD42 |
| **Mediterranean macrothrombocytopenia** | Often the mild monoallelic BSS end of the spectrum in disguise |
| **Acquired / pseudo-BSS** | Anti-GPIb autoantibody; adult onset without family history; may present atypically (the Moroccan hemarthrosis case) |
| **Glanzmann thrombasthenia** | **Normal** platelet count and size; absent aggregation to *all* agonists **except** ristocetin — the exact mirror image of BSS |

That last row is the mnemonic that actually sticks: **Glanzmann fails everything but ristocetin; Bernard-Soulier fails only ristocetin.** Normal-sized platelets vs giant. Opposite in every way except that both bleed.

### Screening

- **Newborn screening:** not performed, not proposed.
- **Cascade screening:** yes — first-degree relatives of a proband, especially in consanguineous kindreds and in dominant (Bolzano/type A2) families.
- **Carrier screening:** targeted in founder populations; not population-wide.
- **Preconception/prenatal:** available where the familial variant is known (§13).

---

## 11. Outcome / Prognosis

### The headline

> **[verbatim, PMID:17109744]** "The prognosis is usually good with adequate supportive care but severe bleeding episodes can occur with menses, trauma and surgical procedures."

That's the honest summary: **BSS is compatible with a normal lifespan — conditional on access to care.** Which is precisely where the recent data get uncomfortable.

### Survival and mortality

- **Life expectancy:** approaching normal with adequate management. No formal actuarial data exist.
- **Disease-specific mortality — the access-dependent reality:**
  > **[verbatim, PMID:41100648]** "Between 2000 and 2025, 13 deaths were reported due to bleeding mainly due to inaccessibility to treatment or treatment products."
  In a 76-patient GT+BSS cohort. Read that again: the deaths were attributed principally to **inaccessibility**, not to intractable biology. That reframes prognosis from a property of the disease to a property of the health system.
- A frequently cited figure of **~16% fatal bleeding** appears in secondary sources (StatPearls NBK557671). **I could not trace it to a primary source in this pass — do not curate it without finding the original.**
- **5-/10-year survival:** not applicable (not a malignancy; no staged survival data).

### Morbidity and function

- Chronic iron-deficiency anemia with fatigue and lost work/school time
- Menorrhagia-driven disability in females of reproductive age
- Transfusion dependence in severe cases, and the downstream alloimmunization spiral
- Procedural and dental care restricted or deferred (PMID:34878196 documents how thin the evidence base for even routine oral surgery is — an integrative review found only **five** relevant articles: one letter and four case reports)
- **Quality of life:** measured with EQ-5D, SF-36, and FACIT in PMID:41100648, with the key finding being weak correlation with ISTH-BAT — i.e. bleeding severity scores are a poor proxy for how people are actually doing.

### Complications

1. **Iron-deficiency anemia** — the most common
2. **Platelet alloimmunization → refractoriness** — the most consequential; it converts the first-line therapy into a dead end
3. **Anti-GPIb alloantibodies crossing the placenta → FNAIT** in the neonate of a previously transfused mother; monitoring is advised for weeks postpartum
4. **Transfusion-transmitted infection** — low but non-zero
5. **Postpartum hemorrhage**, disproportionately *late* PPH
6. **Iatrogenic harm from ITP misdiagnosis** — steroids, IVIG, and unnecessary splenectomy (PMID:41853404)
7. **Antithrombotic dilemma** — patients who develop coronary disease and need stents face an unresolvable risk trade-off
8. **Intracranial hemorrhage** — rare, and the dominant cause of catastrophic outcome

### Prognostic factors

- **Access to platelet products and rFVIIa** — the strongest determinant in the only cohort that measured mortality
- **Biallelic vs monoallelic genotype** — monoallelic is milder (PMID:21933849)
- **Alloimmunization status** — the key branch point in the treatment tree
- **Female reproductive-age status** — higher cumulative morbidity
- **Early correct diagnosis** — avoids the splenectomy detour
- **NOT prognostic:** platelet count and GPIbα expression level. This deserves emphasis because it's counterintuitive: > **[verbatim, PMID:21173099]** "...the patients' bleeding diathesis did not correlate with thrombocytopenia, which was always moderate, and platelet GPIbalpha expression, which was always severely impaired."

**There are no validated prognostic biomarkers in BSS.** Flag as a gap.

---

## 12. Treatment

### 12a. Overall strategy

> **[verbatim, PMID:39191409]** "Platelet transfusion is the main therapy but recombinant factor VIIa is advised in alloimmunized patients, and allogeneic stem cell transplantation is suggested in refractory cases. Antifibrinolytics and oral contraceptives are utilized as supplementary treatments."

That's the whole algorithm in one sentence, and it's the best single citation for a `treatments:` block. The escalation ladder:

```
Local measures + antifibrinolytics
        ↓ (inadequate)
Platelet transfusion (HLA-matched, leukoreduced, apheresis-preferred)
        ↓ (alloimmunized / refractory / access-limited)
Recombinant activated factor VIIa
        ↓ (severe, refractory, transfusion-dependent)
Allogeneic HSCT
        ↓ (experimental)
Autologous lentiviral gene therapy
```

### 12b. Pharmacotherapy

**Antifibrinolytics — tranexamic acid, ε-aminocaproic acid**
- First-line for mucocutaneous bleeding and menorrhagia; oral, topical (mouthwash), or IV
- **Contraindicated in upper urinary tract bleeding** (clot obstruction) and generally avoided in pulmonary hemorrhage
- Used peripartum in the obstetric case: "Single donor platelet transfusions and oral tranexamic acid were administered as prophylaxis at the peripartum period" **[verbatim, PMID:36889343]**
- Suggested annotation: `treatment_term` NCIT:C15986 Pharmacotherapy + `therapeutic_agent` **CHEBI:48669 tranexamic acid** *(verify CHEBI ID)*; `therapeutic_modality: SMALL_MOLECULE`

**Hormonal control of menorrhagia**
- Combined oral contraceptives, levonorgestrel-releasing IUD, progestins, GnRH agonists
- Named explicitly by Kaya 2025 as supplementary therapy
- `therapeutic_modality: SMALL_MOLECULE`

**Recombinant activated factor VIIa (rFVIIa, NovoSeven)**
- Licensed for **Glanzmann thrombasthenia**, not BSS. Use in BSS is **off-label** but guideline-endorsed (UKHCDO/BSH) for severe bleeding, especially in alloimmunized/refractory patients.
- Mechanism: bypasses the GPIb-dependent adhesion step by driving thrombin generation on the platelet surface directly
- **Newest evidence — prophylactic, not just on-demand:**
  > **[verbatim, PMID:41259294]** "Both were initiated on prophylactic rFVIIa (4.5 mg IV and 4 mg IV, respectively) on a weekly basis. Following initiation of prophylaxis, both patients experienced a marked reduction in the frequency and severity of bleeding episodes."
  > and: "Prophylactic administration of rFVIIa was effective in reducing bleeding episodes in both siblings with severe BSS. This case highlights the potential role of rFVIIa as a viable alternative to platelet transfusions in patients with recurrent bleeding. Further studies are needed to establish standardized protocols for prophylactic rFVIIa use in BSS."
  — n=2, so `supports: PARTIAL` at best, and say "case report" in the explanation.
- A parallel access story from Japan: > **[verbatim, PMID:42419992]** "rFVIIa has conventionally been used in GT patients refractory to platelet transfusion due to alloantibody production, but is now available in Japan regardless of alloantibody status or platelet transfusion refractoriness. rFVIIa should be considered especially in patients at risk of alloantibody production due to platelet transfusion."
- Real-world access gap: > **[verbatim, PMID:41100648]** "Platelet transfusion was the main mode of treatment; none of the patients in the present series were on activated recombinant factor VII (rFVIIa) therapy."
- `therapeutic_modality: PROTEIN_REPLACEMENT` (or `OTHER` — it's a recombinant zymogen-activated factor; PROTEIN_REPLACEMENT is the closest honest fit)

**Desmopressin (DDAVP)**
- **Largely ineffective in BSS** — it works by mobilizing VWF, and BSS platelets have no receptor to receive it. Support is anecdotal only. Risks: hyponatremia, seizures with repeat dosing.
- Worth curating as a **negative/limited-efficacy** treatment with `treatment_effect` reflecting that. Negative treatment claims are as useful as positive ones here.

**Eltrombopag (thrombopoietin-receptor agonist)** — the most interesting off-label option
> **[verbatim, PMID:31273088]** "We enrolled 24 patients affected by MYH9-related disease, ANKRD26-related thrombocytopenia, X-linked thrombocytopenia/ Wiskott-Aldrich syndrome, monoallelic Bernard-Soulier syndrome, or ITGB3-related thrombocytopenia."
> **[verbatim, PMID:31273088]** "Of 23 patients evaluable for response, 11 (47.8%) achieved a major response (platelet count >100 x10(9)/L), ten (43.5%) had a minor response (platelet count at least twice the baseline value), and two patients (8.7%) did not respond. The average increase of platelet count compared to baseline was 64.5 x10(9)/L (P<0.001)."
> **[verbatim, PMID:31273088]** "Despite these encouraging results, caution is recommended when using thrombopoietinmimetics in inherited thrombocytopenias predisposing to leukemia."
- **NCT02422394** — Phase II, Zaninetti/Pecci, *Haematologica* 2020
- **Critical scope caveat for curation:** the trial included **monoallelic** BSS, and only as part of a mixed cohort. Do **not** curate this as evidence for eltrombopag efficacy in biallelic BSS. Also note the mechanistic asymmetry — raising the *count* of platelets that still can't bind VWF addresses only half the disease.
- `therapeutic_modality: SMALL_MOLECULE`; `therapeutic_agent` CHEBI/NCIT eltrombopag *(verify ID)*

**Iron supplementation** — routine, and under-prescribed. `therapeutic_modality: SMALL_MOLECULE`.

**Drugs to avoid:** aspirin, other NSAIDs, and (per secondary sources) certain antihistamines and antibiotics with antiplatelet effects. Curate as a contraindication note.

### 12c. Pharmacogenomics

None established. No PharmGKB or CPIC guideline for BSS. **Gap.** The relevant "pharmacogenomic" fact is structural rather than metabolic: a GP1BA/GP1BB/GP9-null genotype makes DDAVP mechanistically futile and antiplatelet drugs disproportionately dangerous.

### 12d. Advanced therapeutics

**Gene therapy — the most active research front, and it now spans all three genes**

*Type A1 / GP1BA, mouse, proof of concept:*
> **[verbatim, PMID:22044935]** "GPIbalpha(null) hematopoietic stem cells (HSC) transduced with 2bIbalpha LV were transplanted into lethally irradiated GPIbalpha(null) littermates. Therapeutic levels of hGPIbalpha expression were achieved that corrected the tail bleeding time and improved the macrothrombocytopenia."
> and: "These results demonstrate that lentivirus-mediated gene transfer can provide sustained phenotypic correction of murine BSS, indicating that this approach may be a promising strategy for gene therapy of BSS patients."
> — Kanaji S et al. *Mol Ther.* 2012 Mar;20(3):625-32

Note the vector design: human GP1BA under the **platelet-specific integrin αIIb promoter** — lineage-restricted expression, which is the right architecture for a megakaryocyte-autonomous disease.

*Making the conditioning clinically tolerable:*
> **[verbatim, PMID:25066812]** "Transplantation of 10-20% hGPIbalpha(tg+/+) BM HSCs mixed with GPIbalpha(null) BM HSCs into irradiated GPIbalpha(null) mice was sufficient to correct bleeding time (n = 5)."
> and: "A combination of busulfan plus ATG conditioning successfully prevented antibody development and significantly increased therapeutic engraftment."
> and: "A conditioning regimen of busulfan in combination with ATG could potentially be used in non-myeloablative autologous gene therapy in human BSS."
> — Kanaji S et al. *J Thromb Haemost.* 2014 Oct

That **10–20% corrected-HSC threshold** is a genuinely important translational number: you don't need full chimerism, which is what makes non-myeloablative conditioning viable.

*Type B / GP1BB, and a structure-function bonus:*
> **[verbatim, PMID:27148783]** "hGPIbbeta transplanted into the bone marrow of GPIbbeta(null) mice rescued GPIb-IX expression in 97% of circulating platelets. These platelets efficiently bound von Willebrand factor (VWF) and extended filopodia on a VWF matrix, demonstrating the restoration of GPIb-dependent adhesive and signaling properties. These mice exhibited less severe macrothrombocytopenia and had normal tail bleeding times as compared with GPIbbeta(null) mice."
> — Strassel C et al. *J Thromb Haemost.* 2016

*Type C / GP9 — and this one reaches patient cells:*
> **[verbatim, PMID:37416759]** "Using gene-editing tools, we generated knockout (KO) human cellular models that helped us to better understand GPIb-V-IX complex assembly. Furthermore, we developed novel lentiviral vectors capable of correcting GPIX expression, localization, and functionality in human GP9-KO megakaryoblastic cell lines. Generated GP9-KO induced pluripotent stem cells produced platelets that recapitulated the BSS phenotype: absence of GPIX on the membrane surface and large size. Importantly, gene therapy tools reverted both characteristics. Finally, hematopoietic stem cells from two unrelated BSS type C patients were transduced with the gene therapy vectors and differentiated to produce GPIX-expressing megakaryocytes and platelets with a reduced size. These results demonstrate the potential of lentiviral-based gene therapy to rescue BSS type C."
> — *Mol Ther Nucleic Acids.* 2023 Sep 12;33:75-92 (a corrigendum/companion record exists at PMID:37621411, same title, *Mol Ther Nucleic Acids* 33:749)

**This is the most advanced human-cell evidence in BSS** and belongs on the entry as `IN_VITRO` evidence for a `GENE_THERAPY` treatment with `target_mechanisms` pointing at the receptor-assembly node. Still preclinical — **no BSS gene therapy has entered a clinical trial**, and the entry should say so plainly.

**Cell therapy — allogeneic HSCT**
- The only *curative* therapy currently available to actual patients
- Reserved for severe, refractory, transfusion-dependent, alloimmunized disease
- Evidence base is case reports/small series; endorsed by Kaya 2025 for refractory cases
- `treatment_term` NCIT:C15431 hematopoietic cell transplantation *(verify)*; `therapeutic_modality: CELL_THERAPY`

**RNA-based therapies, targeted therapies, immunotherapies:** none applicable to BSS.

### 12e. Surgical and interventional

- **Splenectomy: not indicated.** It is a marker of misdiagnosis. (PMID:41853404)
- Surgery of any kind requires pre-procedural planning: HLA-matched platelets on standby, antifibrinolytic cover, and hematology co-management.
- **Dental/oral surgery** is disproportionately represented in BSS bleeding events and disproportionately under-evidenced: > **[verbatim, PMID:34878196]** "As a result, only five articles with the main theme were included: one letter to the editor and four case reports" and "We conclude with this review the need for adequate knowledge of surgeons regarding coagulation disorders and the need to discuss and plan procedures with the hematology team."

### 12f. Obstetric management

> **[verbatim, PMID:36889343]** "64.7% (33/51) of the patients were delivered via cesarean section. PPH and late PPH were found to be more common in those who delivered vaginally compared to those who delivered by caesarean section. It was observed that PPH was less common in women who were given prophylaxis in the peripartum period."

> **[verbatim, PMID:36889343]** "BSS is an inherited macro-thrombocytopathy that may cause adverse maternal and neonatal outcomes. The optimal mode and timing of delivery remain unclear. A multidisciplinary approach with prophylaxis at the peripartum period should be applied."

Practical points: **neuraxial anesthesia is contraindicated**; uterotonics, HLA-matched platelets, and tranexamic acid are the toolkit; monitor the neonate for FNAIT for weeks postpartum if the mother has been transfused. Note the observational-design caveat before curating the cesarean/vaginal comparison — the mode of delivery was not randomized and confounding by indication is severe.

### 12g. Supportive care and prevention-of-harm

Patient education, medical alert bracelet/card, registration with a 24-hour hemophilia treatment center, contact-sport avoidance, meticulous dental hygiene, **HLA typing at diagnosis** (so matched products are obtainable later), iron repletion, and hepatitis B vaccination before transfusion exposure.

### 12h. Suggested NCIT annotations

I did **not** resolve NCIT IDs against OAK in this session, so treat these as *candidates to verify*, not as verified terms:
- `NCIT:C15986` Pharmacotherapy — antifibrinolytics, hormonal therapy, eltrombopag, rFVIIa
- `NCIT:C15431` Hematopoietic Cell Transplantation — allogeneic HSCT
- `NCIT:C15238` Gene Therapy — experimental LV gene therapy
- `NCIT:C15747` Supportive Care — the education/avoidance bundle
- `NCIT:C15240` Genetic Counseling
- `NCIT:C15329` Surgical Procedure — procedural planning context
- **Platelet transfusion** — NCIT has a term; look it up with `uv run runoak -i sqlite:obo:ncit info "l^Platelet Transfusion"` rather than guessing the ID

Remember the dismech gotcha: NCIT drug terms frequently fail `therapeutic_agent` validation — prefer CHEBI for the small molecules (tranexamic acid, eltrombopag) and reserve NCIT for classes and for biologics with no CHEBI entry.

---

## 13. Prevention

### Primary prevention

**You cannot prevent the genotype.** What you *can* prevent is its transmission and its complications.

- **Genetic counseling** — the core intervention. For AR families: 25% recurrence risk per pregnancy, carrier testing for relatives. For AD/Bolzano families: 50% transmission, but with the honest caveat that clinical expression is mild and variable.
- **Carrier and cascade screening** — targeted at families and at consanguineous communities with founder alleles. Not population-wide screening; the prevalence doesn't justify it.
- **Preimplantation genetic testing (PGT-M)** and **prenatal diagnosis** (CVS/amniocentesis) — technically available whenever the familial variant is known. Lanza 2006 and Orphanet both note antenatal diagnosis is feasible.
- **Consanguinity counseling** — the single highest-yield population-level lever in the regions where BSS actually clusters, and also the most socially delicate. Frame it as informed choice and carrier testing, not as prohibition.
- **Immunization:** no vaccine prevents BSS. But **hepatitis B vaccination before first transfusion exposure** is genuine primary prevention of a transfusion-associated harm and belongs here.

### Secondary prevention (early detection)

- **No newborn screening program** exists or is proposed.
- The real secondary-prevention target is **diagnostic delay**. Two rules with published support:
  1. Any patient with "refractory ITP" + macrothrombocytopenia + family history → run ristocetin aggregometry and CD42 flow **before** considering splenectomy. > **[verbatim, PMID:39191409]** "Thus, BSS should be kept in mind in the presence of individuals with chronic persistent thrombocytopenia, positive family history, unresponsive ITP treatment, macrothrombocytopenia, and absence of RIPA response."
  2. Any 22q11.2DS patient with macrothrombocytopenia → test for BSS (PMID:38625506).
- **Risk stratification:** ISTH-BAT score + genotype (biallelic vs monoallelic) + alloimmunization status.

### Tertiary prevention (preventing complications in diagnosed patients)

This is where nearly all the achievable benefit sits:

1. **Prevent alloimmunization** — leukoreduced, HLA-matched, apheresis-derived (single-donor) platelets; minimize transfusion episodes by using antifibrinolytics and rFVIIa where they'll do the job; **HLA-type at diagnosis**
2. **Prevent iron deficiency** — proactive ferritin monitoring and repletion, not reactive
3. **Prevent menstrual morbidity** — a hormonal + tranexamic acid plan established *before* menarche in known-affected girls
4. **Prevent procedural bleeding** — pre-procedure hematology consultation for every dental extraction and surgery; the oral-surgery review (PMID:34878196) exists precisely because this keeps failing
5. **Prevent peripartum hemorrhage** — planned multidisciplinary delivery with peripartum prophylaxis; prophylaxis was associated with less PPH (PMID:36889343)
6. **Prevent FNAIT** — identify maternal anti-GPIb antibodies; monitor the neonate's platelet count for weeks after delivery
7. **Prevent iatrogenic harm** — no splenectomy, no steroids, no IVIG for what is not ITP; no NSAIDs; no IM injections; no neuraxial anesthesia in labor
8. **Prevent trauma** — activity counseling, helmets, contact-sport avoidance, medical alert identification

### Behavioral interventions and public health

- Patient/family education is repeatedly identified as the highest-value single intervention
- **Public health / systems intervention:** the Indian mortality data make the case bluntly — 13 bleeding deaths attributed mainly to inaccessibility of treatment products. **Supply-chain and access policy is a prevention intervention for this disease**, on par with anything clinical. > **[verbatim, PMID:41100648]** "The need for optimal treatment strategies to improve QoL and providing timely access to specific treatment products to prevent mortality is underscored."
- **Environmental interventions:** not applicable.

### Prophylaxis

- **Peripartum:** platelet transfusion + tranexamic acid (PMID:36889343)
- **Pre-procedural:** HLA-matched platelets + antifibrinolytic
- **Long-term regular prophylaxis** — this is genuinely new and worth flagging as an emerging practice rather than a standard: weekly rFVIIa in two severely affected brothers (PMID:41259294), and 16-week continuous eltrombopag maintaining mucosal-hemorrhage remission (PMID:31273088)

---

## 14. Other Species / Natural Disease

### Taxonomy

- **Dog** — *Canis lupus familiaris*, **NCBITaxon:9615** *(verify)* — the only species with a well-characterized naturally occurring BSS
- **Mouse** — *Mus musculus*, **NCBITaxon:10090** *(verify)* — engineered only, no natural BSS (§15)
- Human — *Homo sapiens*, **NCBITaxon:9606**

### Breed

**Cocker Spaniel** — VBO term exists for the breed; **I did not resolve the VBO ID this session — look it up before curating.**

### Orthologous genes

Canine **GP9**, located on **dog chromosome 20**, single coding exon (as in human). NCBI Gene IDs for canine GP1BA/GP1BB/GP9 exist — **not resolved this session.**

### Natural disease in dogs — the flagship finding

> **[verbatim, PMID:31484196]** "Four cases of a mild to severe bleeding disorder in Cocker Spaniel dogs are herein presented. The affected dogs showed a platelet adhesion defect characterized by macrothrombocytopenia with variable platelet counts resembling human Bernard-Soulier syndrome (BSS). Furthermore, the lack of functional GPIb-IX-V was demonstrated by immunocytochemistry."

> **[verbatim, PMID:31484196]** "Whole genome sequencing of one affected dog and visual inspection of the candidate genes identified a deletion in the glycoprotein IX platelet (GP9) gene."

> **[verbatim, PMID:31484196]** "The deletion spanned 2460 bp, and included a significant part of the single coding exon of the canine GP9 gene on dog chromosome 20. The variant results in a frameshift and premature stop codon which is predicted to truncate almost two-thirds of the encoded protein. PCR-based genotyping confirmed recessive inheritance. The homozygous variant genotype seen in affected dogs did not occur in 98 control Cocker Spaniels."

> **[verbatim, PMID:31484196]** "Thus, it was concluded that the structural variant identified in the GP9 gene was most likely causative for the BSS-phenotype in the dogs examined. These findings provide the first large animal GP9 model for this group of inherited platelet disorders and greatly facilitate the diagnosis and identification of affected and/or normal carriers in Cocker Spaniels."
> — *PLoS One.* 2019

Beautiful parallelism: same gene, same recessive mode, same macrothrombocytopenia + adhesion defect, same "variable platelet counts," and a structural variant that a gene panel would have missed. MONDO already carries it as **MONDO:1010672** "Bernard-Soulier syndrome, GP9-related, dog" **[OLS-checked]**.

### Veterinary relevance

> **[verbatim, PMID:31484196]** "Inherited bleeding disorders including abnormalities of platelet number and function rarely occur in a variety of dog breeds, but are probably underdiagnosed. Genetically characterized canine forms of platelet disorders provide valuable large animal models for understanding similar platelet disorders in people. Breed-specific disease associated genetic variants in only eight different genes are known to cause intrinsic platelet disorders in dogs."

Practical veterinary value: a PCR genotyping assay now exists for Cocker Spaniel breeding programs. **OMIA** carries the entry — look up the OMIA ID rather than guessing it.

### Comparative biology

- **Conservation:** the GPIb-IX-V complex and its VWF-binding function are conserved across mammals. The dog and mouse both reproduce the core macrothrombocytopenia + adhesion-defect phenotype from orthologous lesions — strong evidence that the mechanism is not human-specific.
- **The GPV exception is the most informative comparative finding.** In mouse, deleting GPV changes essentially nothing about megakaryocyte biology:
  > **[verbatim, PMID:10959706]** "Our study extends previous results and reports that electron microscopy of bone marrow from the GPV knockout mice revealed a normal MK ultrastructure and development of the demarcation membrane system (DMS)."
  > and: "Thus GPV is not crucial to MK development and platelet production, consistent with the fact that no mutation in the GPV gene has as yet been described in BSS."
  > — Poujol C et al. *Thromb Haemost.* 2000 Aug;84(2):312-8

  A mouse knockout independently predicting the *absence* of a human disease gene, and being right for twenty-six years running. That's about as good as cross-species validation gets, and it's the strongest available evidence for curating "GP5 is not a BSS gene" as a positive claim rather than a null result.

### Transmission

- **Zoonotic potential:** none. Genetic, non-transmissible.
- **Cross-species susceptibility:** not applicable.

---

## 15. Model Organisms

### 15a. Mouse models — the workhorse

| Model | Genotype | Key phenotype | PMID |
|---|---|---|---|
| **GPIbα-null** | *Gp1ba* targeted disruption | Full BSS phenocopy: macrothrombocytopenia + severe bleeding; the founding model | **10706630** |
| **GPIbβ-null** | *Gp1bb* targeted disruption | Macrothrombocytopenia + severe bleeding **+ enlarged α-granules** (SEPT5 effect) | **15213102** |
| **GPIbβ-null, MK biology** | same | Normal progenitor number/endoreplication; DMS underdeveloped; proplatelet formation ↓41%; doubled tubulin fibers | **19377075** |
| **GPV-null** | *Gp5* targeted disruption | **Normal** MK ultrastructure, DMS, GPIb-IX expression, adhesion — *fails to phenocopy BSS*, and correctly so | **10959706** |
| **hGPIbα transgenic rescue** | GPIbα-null + human GP1BA transgene | Phenotype rescued — the in vivo humanized platform | **10706630** |
| **IL-4Rα/GPIbα chimera** | GPIbα-null + chimeric receptor transgene | **Dissociates the two branches**: 2× platelet count, 50% smaller platelets, bleeding *unchanged* | **12200373** |
| **LV gene-therapy recipients** | GPIbα-null + 2bIbα lentivirus in HSC | Corrected bleeding time, improved macrothrombocytopenia, sustained through serial BMT | **22044935** |
| **Non-myeloablative conditioning** | GPIbα-null + busulfan ± ATG | 10–20% corrected HSC sufficient; ATG prevents anti-hGPIbα antibody | **25066812** |
| **GPIbβ LV rescue + tail deletions** | GPIbβ-null + hGPIbβ variants | 97% platelet rescue; Δ150-160 ↓ expression 43% and ↑ bleeding; Δ159-170 ↑ thrombosis | **27148783** |

**Foundational quote for the model-organism block:**
> **[verbatim, PMID:10706630]** "Thus, an in vivo model is defined for analysis of the human GP Ib-IX-V receptor and its role in the processes performed exclusively by megakaryocytes and platelets."

**For the dismech `animal_models:` block with `modeled_mechanisms`:**
- GPIbα-null mouse → `RECAPITULATES` "Macrothrombocytopenia" and "Failure of primary hemostasis", `fidelity: HIGH`
- GPIbβ-null mouse → `RECAPITULATES` "Impaired proplatelet formation", `fidelity: HIGH`; readouts: proplatelet-forming MK fraction (`DECREASED`), marginal-band tubulin fiber count (`INCREASED`), platelet diameter (`INCREASED`)
- **GPV-null mouse → `FAILS_TO_RECAPITULATE`** the BSS phenotype — and this is the textbook case for that relationship value, because the failure is *informative*, not a limitation. Requires `limitations` + `evidence`, both of which PMID:10959706 supplies.
- IL-4Rα/GPIbα chimera → `PARTIALLY_RECAPITULATES` / `RESCUES` — partial rescue of the size/count branch with the bleeding branch untouched

**Limitations to record honestly:**
- Baseline mouse platelets are smaller and far more numerous than human platelets, so "macrothrombocytopenia" is scaled differently
- Tail-bleeding time is a crude, high-variance surrogate for human mucocutaneous bleeding
- Mouse models are homozygous nulls; they say little about the **monoallelic/dominant-negative** human forms, which is where the Bolzano human-megakaryocyte work (PMID:19067792) is irreplaceable
- Transgenic rescue expresses *human* GPIbα in a mouse complex — an interspecies chimera by construction

### 15b. Human cellular and in vitro models (NAMs)

These belong in `experimental_models:`, not `animal_models:`.

- **Patient-derived megakaryocyte cultures** from CD34+ cord blood and CD45+ peripheral blood — the Bolzano proplatelet study (PMID:19067792). Directly human, directly on the mechanism, six patients. Highest translational fidelity available.
- **GP9-KO human megakaryoblastic cell lines** — gene-edited, used to dissect complex assembly (PMID:37416759)
- **GP9-KO iPSC → megakaryocyte → platelet** — > **[verbatim, PMID:37416759]** "Generated GP9-KO induced pluripotent stem cells produced platelets that recapitulated the BSS phenotype: absence of GPIX on the membrane surface and large size. Importantly, gene therapy tools reverted both characteristics."
- **Patient HSC-derived megakaryocytes** from two unrelated BSS type C patients, transduced and differentiated (PMID:37416759) — the closest thing to a human-in-a-dish trial
- **CHO heterologous expression** — used for complex-assembly stoichiometry (PMID:12200373). **Caveat with teeth:** heterologous cells *mispredicted* GPIbβ's in vivo role (PMID:27148783 explicitly: "a repressor role of GPIbbeta in thrombus formation in vivo that was not predicted in studies of heterologous cells"). Record as a `limitations` field, and consider a `HUMAN_MODEL_MISMATCH`-style discussion.

### 15c. Large-animal model

**Cocker Spaniel GP9-deletion dog** (PMID:31484196) — "the first large animal GP9 model for this group of inherited platelet disorders." Naturally occurring, outbred, human-scale physiology, spontaneous bleeding phenotype. Ideal for testing transfusion alternatives and, eventually, gene-therapy dosing at realistic body size.

### 15d. What does *not* exist

- **No zebrafish, Drosophila, or C. elegans BSS model** located. Invertebrates lack platelets entirely; zebrafish thrombocytes are nucleated and the GPIb-IX-V orthology is imperfect.
- **No BSS organoid or organ-chip model.** A bone-marrow-on-chip with BSS iPSC-derived megakaryocytes under physiological shear is the obvious missing NAM — it would let you interrogate both branches (proplatelet extrusion and shear-dependent adhesion) in one human system. **Flag as a `proposed_experiment`.**
- **No functional genomics screen** (CRISPR/RNAi) targeting the BSS pathway.

### 15e. Resources

MGI (mouse alleles for *Gp1ba*, *Gp1bb*, *Gp5*, *Gp9*), IMPC, Alliance of Genome Resources, IMSR (strain availability), **OMIA** (canine BSS), Cellosaurus (the GP9-KO megakaryoblastic lines and iPSC lines from PMID:37416759 — request accessions from the authors if not deposited).

---

## Synthesis: what to build first in the KB entry

If I were laying out the pathograph, I'd anchor on the two-branch structure, because that's the thing about BSS that nothing else in the inherited-platelet-disorder space does as cleanly. One receptor, two jobs, and a chimera experiment (PMID:12200373) that surgically separates them. That's the spine.

Then:
- **`conforms_to` candidates:** none of the existing dismech modules fit well. `thrombogenesis` is the *inverse* (failure to form a thrombus, not formation of one) — do **not** wire BSS to it as a conformer; the module models pathological thrombus formation, and BSS is its mirror. If anything, BSS is a candidate *trigger* for a future "primary hemostatic failure" module, which does not yet exist.
- **`differentials`:** ITP, Glanzmann thrombasthenia, type 2B VWD, platelet-type VWD, MYH9-RD, gray platelet syndrome, 22q11.2DS. Grep the sibling entries for their MONDO IDs — do not guess them.
- **Grouping candidate:** BSS belongs in an "Inherited macrothrombocytopenias" or "Inherited platelet function disorders" grouping alongside Glanzmann thrombasthenia and MYH9-RD, with `grouping_basis: SHARED_MECHANISM` + `SHARED_PHENOTYPE`. Check whether one already exists before creating.
- **`discussions` / `KNOWLEDGE_GAP` items** worth curating explicitly:
  1. No genotype-phenotype correlation for bleeding severity (PMID:21173099) — replicated, mechanistically unexplained
  2. No gnomAD-derived carrier-frequency estimate; monoallelic BSS prevalence is unknown and probably substantially underestimated
  3. Whether GPIbα mechanosensor-domain destabilization shortens platelet survival in patients (PMID:27670775) — `EMERGING`, not canonical
  4. No prognostic biomarker; no validated severity model
  5. The ~16% fatal-bleeding figure circulating in secondary sources has no traceable primary citation
  6. No BSS gene-therapy clinical trial despite strong preclinical data across all three genes

**Before writing YAML:** run `just preflight-dr` if you generate any DR report for this disease. BSS is moderate NEC risk — the eponym is shared with nothing obvious, but the *subtype letters* (A1/A2/B/C) are exactly the numbered-series pattern that trips DR tools, and "Bernard" collides with several unrelated eponyms. Also verify every OMIM number, every NCIT ID, and the ICD-11 code, all of which I could not confirm in this pass.

---

## Sources

- [Kaya Z. Bernard-Soulier Syndrome: A Review of Epidemiology, Molecular Pathology, Clinical Features, Laboratory Diagnosis, and Therapeutic Management. *Semin Thromb Hemost.* 2025;51(2):209-218. PMID:39191409](https://pubmed.ncbi.nlm.nih.gov/39191409/)
- [Lanza F. Bernard-Soulier syndrome (hemorrhagiparous thrombocytic dystrophy). *Orphanet J Rare Dis.* 2006;1:46. PMID:17109744](https://pubmed.ncbi.nlm.nih.gov/17109744/)
- [Savoia A et al. Spectrum of the mutations in Bernard-Soulier syndrome. *Hum Mutat.* 2014;35(9):1033-45. PMID:24934643](https://pubmed.ncbi.nlm.nih.gov/24934643/)
- [Savoia A et al. Clinical and genetic aspects of Bernard-Soulier syndrome: searching for genotype/phenotype correlations. *Haematologica.* 2011;96(3):417-23. PMID:21173099](https://pubmed.ncbi.nlm.nih.gov/21173099/)
- [Noris P et al. Clinical and laboratory features of 103 patients from 42 Italian families with inherited thrombocytopenia derived from the monoallelic Ala156Val mutation of GPIbα (Bolzano mutation). *Haematologica.* 2012;97(1):82-8. PMID:21933849](https://pubmed.ncbi.nlm.nih.gov/21933849/)
- [Balduini A et al. Proplatelet formation in heterozygous Bernard-Soulier syndrome type Bolzano. *J Thromb Haemost.* 2009;7(3):478-84. PMID:19067792](https://pubmed.ncbi.nlm.nih.gov/19067792/)
- [Ware J, Russell S, Ruggeri ZM. Generation and rescue of a murine model of platelet dysfunction: the Bernard-Soulier syndrome. *PNAS.* 2000;97(6):2803-8. PMID:10706630](https://pubmed.ncbi.nlm.nih.gov/10706630/)
- [Kanaji T et al. Amelioration of the macrothrombocytopenia associated with the murine Bernard-Soulier syndrome. *Blood.* 2002. PMID:12200373](https://pubmed.ncbi.nlm.nih.gov/12200373/)
- [Kato K et al. Genetic deletion of mouse platelet glycoprotein Ibβ produces a Bernard-Soulier phenotype with increased alpha-granule size. *Blood.* 2004. PMID:15213102](https://pubmed.ncbi.nlm.nih.gov/15213102/)
- [Strassel C et al. Intrinsic impaired proplatelet formation and microtubule coil assembly of megakaryocytes in a mouse model of Bernard-Soulier syndrome. *Haematologica.* 2009. PMID:19377075](https://pubmed.ncbi.nlm.nih.gov/19377075/)
- [Strassel C et al. Lentiviral gene rescue of a Bernard-Soulier mouse model to study platelet glycoprotein Ibβ function. *J Thromb Haemost.* 2016. PMID:27148783](https://pubmed.ncbi.nlm.nih.gov/27148783/)
- [Poujol C et al. Ultrastructural analysis of megakaryocytes in GPV knockout mice. *Thromb Haemost.* 2000;84(2):312-8. PMID:10959706](https://pubmed.ncbi.nlm.nih.gov/10959706/)
- [Kanaji S et al. Correction of murine Bernard-Soulier syndrome by lentivirus-mediated gene therapy. *Mol Ther.* 2012;20(3):625-32. PMID:22044935](https://pubmed.ncbi.nlm.nih.gov/22044935/)
- [Kanaji S et al. Non-myeloablative conditioning with busulfan before HSCT leads to phenotypic correction of murine Bernard-Soulier syndrome. *J Thromb Haemost.* 2014. PMID:25066812](https://pubmed.ncbi.nlm.nih.gov/25066812/)
- [Lentiviral gene therapy reverts GPIX expression and phenotype in Bernard-Soulier syndrome type C. *Mol Ther Nucleic Acids.* 2023;33:75-92. PMID:37416759](https://pubmed.ncbi.nlm.nih.gov/37416759/) (companion record [PMID:37621411](https://pubmed.ncbi.nlm.nih.gov/37621411/))
- [Zaninetti C et al. Eltrombopag for the treatment of inherited thrombocytopenias: a phase II clinical trial. *Haematologica.* 2020;105(3):820-828. NCT02422394. PMID:31273088](https://pubmed.ncbi.nlm.nih.gov/31273088/)
- [Deng W et al. Platelet clearance via shear-induced unfolding of a membrane mechanoreceptor. *Nat Commun.* 2016. PMID:27670775](https://pubmed.ncbi.nlm.nih.gov/27670775/)
- [Li R, Emsley J. The organizing principle of the platelet glycoprotein Ib-IX-V complex. *J Thromb Haemost.* 2013. PMID:23336709](https://pubmed.ncbi.nlm.nih.gov/23336709/)
- [Bernard-Soulier syndrome caused by a novel GP1BB variant and 22q11.2 deletion. *Int J Hematol.* 2024;120(1):142-145. PMID:38625506](https://pubmed.ncbi.nlm.nih.gov/38625506/)
- [Molecular genetic diagnosis of Bernard-Soulier syndrome in Iranian patients: reporting three novel mutations. *Transfus Apher Sci.* 2026. PMID:42229093](https://pubmed.ncbi.nlm.nih.gov/42229093/)
- [Natural history & quality of life in Glanzmann thrombasthenia & Bernard Soulier syndrome: An observational study from India. *Indian J Med Res.* 2025. PMID:41100648](https://pubmed.ncbi.nlm.nih.gov/41100648/)
- [Recombinant Factor VIIa Prophylaxis in 2 Brothers with Bernard-Soulier Syndrome. *Am J Case Rep.* 2025. PMID:41259294](https://pubmed.ncbi.nlm.nih.gov/41259294/)
- [Bernard-Soulier Syndrome: Case Studies From Morocco. *Cureus.* 2025. PMID:40703326](https://pubmed.ncbi.nlm.nih.gov/40703326/)
- [Bernard Soulier Syndrome Misdiagnosed and Treated as Immune Thrombocytopenia Purpura: A Case Report. *Cureus.* 2026. PMID:41853404](https://pubmed.ncbi.nlm.nih.gov/41853404/)
- [Bernard-Soulier Syndrome from the Perspective of the Obstetrician: A Case Report with a Review of the Literature. *Z Geburtshilfe Neonatol.* 2023. PMID:36889343](https://pubmed.ncbi.nlm.nih.gov/36889343/)
- [Invasive procedures in the oral cavity of individuals with Bernard-Soulier syndrome: An integrative review. *Spec Care Dentist.* 2022. PMID:34878196](https://pubmed.ncbi.nlm.nih.gov/34878196/)
- [Current diagnosis and treatment of congenital platelet function disorders: focus on Glanzmann thrombasthenia and Bernard-Soulier syndrome. *Rinsho Ketsueki.* 2026. PMID:42419992](https://pubmed.ncbi.nlm.nih.gov/42419992/)
- [A large deletion in the GP9 gene in Cocker Spaniel dogs with Bernard-Soulier syndrome. *PLoS One.* 2019. PMID:31484196](https://pubmed.ncbi.nlm.nih.gov/31484196/)
- [Bernard-Soulier Syndrome. StatPearls, NCBI Bookshelf NBK557671](https://www.ncbi.nlm.nih.gov/books/NBK557671/) — secondary source; several figures cited above (mean diagnosis age 16, ~16% fatal bleeding, MPV >12.4 fL) trace only to here and need primary confirmation
- [OMIM entry #231200 — Bernard-Soulier syndrome](https://omim.org/entry/231200) — returned HTTP 403 this session; OMIM identifiers above are unverified
- [Orphanet — Bernard-Soulier syndrome (ORPHA:274)](https://www.orpha.net/en/disease/detail/274) — bot-challenge this session; prefer the cached structured `ORPHA:274` record
- [EBI OLS4](https://www.ebi.ac.uk/ols4) — used to resolve the MONDO, HP, GO, CL, CHEBI, and HGNC identifiers marked **[OLS-checked]**
- [NLM MeSH lookup service](https://id.nlm.nih.gov/mesh/lookup/descriptor?label=Bernard-Soulier%20Syndrome&match=exact) — D001606

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |

All extracted references resolved successfully.