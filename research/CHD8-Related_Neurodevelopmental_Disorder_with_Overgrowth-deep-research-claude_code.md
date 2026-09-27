---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T22:38:40.315518'
end_time: '2026-07-31T22:57:58.719222'
duration_seconds: 1158.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CHD8-Related Neurodevelopmental Disorder with Overgrowth
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 29
  num_turns: 78
  total_cost_usd: 6.600318750000001
  session_id: 9779c7e6-ab33-4766-8d6b-1d8fba40c923
  stop_reason: end_turn
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CHD8-Related Neurodevelopmental Disorder with Overgrowth
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CHD8-Related Neurodevelopmental Disorder with Overgrowth** covering all of the
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

# Comprehensive Research Report

# CHD8-Related Neurodevelopmental Disorder with Overgrowth (CHD8-NDD / IDDAM)

**Prepared:** 2026-07-31 · **Target MONDO:** MONDO:0014017 · **Category:** Mendelian (autosomal dominant, de novo predominant)

---

## ⚠️ Methodological Note on Evidence Quality — Read Before Curating

Three constraints on this report must be stated plainly, because they determine how the content may be used:

1. **Quoted snippets in this report are NOT validated evidence snippets.** In this sandboxed run, PubMed MCP access, the local `just fetch-reference` tooling, and direct E-utilities `curl` were all unavailable (permission-gated), and the web-fetch layer returns *model-summarized* prose rather than verbatim abstract text. Quotation marks below reproduce text as it was returned by source pages and fetch summaries. **Every snippet must be re-fetched with `just fetch-reference PMID:xxxx` and re-verified with `just validate-references` before it enters a `kb/disorders/` YAML file.** Treat this report exactly as CLAUDE.md §2a instructs for deep-research output: *leads, not ground truth*.

2. **All PMIDs cited here were independently verified** against NCBI E-utilities `esummary` (title + journal + year + first author matched). This is the one layer I was able to confirm mechanically. PMIDs are reliable; snippets are not.

3. **Ontology IDs were verified** against the repo's cached term enums (`cache/enums/*.csv`). Every HP/GO/CL/UBERON/NCIT/CHEBI ID appearing below was confirmed present in the corresponding dynamic-enum expansion. **Labels were not verifiable** (the cache files carry CURIEs only, and OAK/`runoak` was permission-blocked), so labels must still be confirmed with `just validate-terms` before use. IDs that failed the membership check have been omitted rather than guessed.

**NEC preflight (CLAUDE.md §2b):** This report passes the Named Entity Confusion check. The queried entity, the MONDO term (MONDO:0014017), the OMIM entry (#615032, IDDAM), and the GeneReviews chapter (PMID:36302072) all resolve to the **same causal gene, CHD8 (HGNC:20153, 14q11.2)**, and CHD8 is the gene named overwhelmingly throughout the retrieved literature. No competing eponym or numbered-series collision was found. The one nomenclature caution is historical rather than confusional: OMIM #615032 was originally designated **AUTS18** ("autism, susceptibility to, 18") before being renamed IDDAM; both names index the same entity.

**Existing repo state:** `kb/disorders/CHD8-Related_Neurodevelopmental_Disorder_with_Overgrowth.yaml` currently exists as a 57-line stub with a single pathophysiology node, one phenotype, one gene, and one PMID (PMID:36302072). This report is scoped to support substantial expansion of that stub.

---

## 1. Disease Information

### 1.1 Overview

CHD8-related neurodevelopmental disorder with overgrowth (CHD8-NDD) is an autosomal dominant, de novo–predominant neurodevelopmental syndrome caused by heterozygous loss-of-function variants in *CHD8*, which encodes chromodomain-helicase-DNA-binding protein 8, an ATP-dependent chromatin remodeler of the SNF2 superfamily. The disorder is defined by the co-occurrence of **generalized somatic and cranial overgrowth** with **neurodevelopmental impairment**, distinguishing it from the many non-overgrowth autism/ID syndromes.

The GeneReviews chapter (PMID:36302072) characterizes the condition as follows:

> "CHD8-related neurodevelopmental disorder with overgrowth (CHD8-NDD) is characterized by generalized overgrowth, developmental delay / intellectual disability (DD/ID), autism spectrum disorder (ASD), neuropsychiatric issues, neurologic problems, sleep disturbance, and gastrointestinal issues. The most common findings are the development of macrocephaly (most often during infancy) and tall stature (most typically during puberty)."

CHD8 occupies an unusual position in autism genetics: it is among the highest-confidence — arguably *the* highest-confidence — ASD risk gene, and it was the first gene for which a **genetically defined ASD subtype** with a recognizable somatic phenotype was demonstrated (Bernier et al., Cell 2014; PMID:24998929). That paper is the historical anchor of the entity.

### 1.2 Key Identifiers

| Resource | Identifier | Label / Note |
|---|---|---|
| **MONDO** | `MONDO:0014017` | intellectual developmental disorder with autism and macrocephaly (already used in the repo stub) |
| **OMIM** | **#615032** | INTELLECTUAL DEVELOPMENTAL DISORDER WITH AUTISM AND MACROCEPHALY; IDDAM (formerly AUTS18) |
| **OMIM gene** | ***610528*** | CHD8 |
| **HGNC** | `hgnc:20153` | CHD8 (lowercase prefix per repo convention) |
| **NCBI Gene** | 57680 | CHD8 |
| **UniProt** | Q9HCK8 | Chromodomain-helicase-DNA-binding protein 8 |
| **Cytoband** | 14q11.2 | |
| **UMLS / GTR** | C3554373 | Intellectual developmental disorder with autism and macrocephaly |
| **Orphanet** | ORPHA:642675 *(needs verification)* | Retrieved via search only; the Orphanet site blocked direct fetch. **Verify before use** — do not enter unverified. Note ORPHA:210548 ("macrocephaly-intellectual disability-autism syndrome") is a *different, non-CHD8* entity and must not be conflated. |
| **SFARI Gene** | CHD8 | Category 1 (high confidence) |
| **ICD-10** | No specific code. Closest: F84.0 (childhood autism) + Q87.3 (congenital malformation syndromes involving early overgrowth) | Combination coding required |
| **ICD-11** | No specific code. Closest: 6A02 (autism spectrum disorder) + LD2F (overgrowth syndromes) | Combination coding required |
| **MeSH** | No specific descriptor. Related: D000067877 (Autism Spectrum Disorder), D058627 (Megalencephaly) | |

**Curation note:** the absence of dedicated ICD-10/ICD-11/MeSH codes is itself a fact worth recording — CHD8-NDD is coded only by composition in administrative terminologies, which limits EHR-based case finding and argues for genotype-first ascertainment (relevant to any future `PHENOTYPE_ALGORITHM` definition).

### 1.3 Synonyms

- Intellectual developmental disorder with autism and macrocephaly (IDDAM) — the OMIM-preferred name
- CHD8 overgrowth syndrome (Ostrowski et al. 2019, PMID:31721432)
- CHD8-related syndrome (Simons Searchlight usage)
- CHD8 haploinsufficiency syndrome
- Autism, susceptibility to, 18 (AUTS18) — historical OMIM designation
- CHD8-NDD

The repo stub already carries all five principal synonyms correctly.

### 1.4 Provenance of Information

The evidence base is **aggregated disease-level** rather than EHR/individual-patient. It comprises: (a) gene-first resequencing cohorts (Bernier 2014); (b) clinician-reported case series aggregated across centers (Ostrowski 2019, n=27; Douzgou 2019, n=25; Dingemans 2022, n=106); (c) a genotype-first deep-phenotyping research cohort (University of Washington / Eichler-Bernier, feeding Beighley 2020 and the Simons Searchlight registry, NCT01238250); and (d) the GeneReviews synthesis (PMID:36302072, n=115). No population-based registry data exist. Because ascertainment in (a) is autism-biased and in (b) overgrowth/dysmorphology-biased, **feature frequencies differ systematically by cohort** — see §3.2.

---

## 2. Etiology

### 2.1 Disease Causal Factors

CHD8-NDD is a **monogenic, primarily de novo, autosomal dominant** disorder. The causal mechanism is **haploinsufficiency** of *CHD8* — a ~50% reduction in functional CHD8 protein during a developmental window in which the gene is most highly expressed.

Bernier et al. (PMID:24998929) established causality by a case-control design of unusual cleanliness for a neurodevelopmental gene:

> Researchers "resequenced the ASD-associated gene CHD8 in 3,730 children with developmental delay or ASD and identified 15 independent mutations; no truncating events were identified in 8,792 controls, including 2,289 unaffected siblings."

The complete absence of truncating events in 8,792 controls — including 2,289 unaffected siblings, which controls for family-level confounding — is the single strongest piece of human genetic evidence for the entity, and is the citation to use for the causal claim.

The gene-level constraint metrics corroborate this:
- **gnomAD pLI = 1.00** (maximal loss-of-function intolerance)
- **gnomAD LOEUF = 0.15** (extreme constraint; LOEUF < 0.35 is the conventional threshold)
- **ClinGen Dosage Sensitivity: Haploinsufficiency score 3** ("sufficient evidence for haploinsufficiency"); **Triplosensitivity score 0**
- **DECIPHER HI index = 11.24** (top ~11% most haploinsufficiency-likely genes)

> **Curation opportunity:** ClinGen dosage records are ingestable as `CGDS:` structured references in this repo. A `CGDS:HGNC_20153` cache entry would let a curator cite the ClinGen haploinsufficiency-3 row as a snippet-validated evidence item for the mechanism node. Build with `just clingen-dosage-rebuild --id CGDS:HGNC_20153`. Similarly, a ClinGen Gene-Disease Validity assertion (`CGGV:`) for CHD8-IDDAM should be checked for with `just clingen-list`.

### 2.2 Genetic Risk Factors

**Causal variants.** Heterozygous *CHD8* protein-truncating variants (nonsense, frameshift, canonical splice-site) constitute the large majority of pathogenic alleles. Dingemans et al. 2022 (PMID:36182950) catalogued across 106 individuals: **29 unique nonsense, 25 frameshift, 24 missense, 12 splice-site variants, plus 2 in-frame deletions, 1 multi-exon deletion (exons 26–28), and 1 translocation.**

**Susceptibility loci / common variation.** CHD8 is not a common-variant GWAS locus for ASD at genome-wide significance. Its contribution is entirely through rare, high-penetrance, mostly de novo alleles. A small literature on *CHD8* polymorphic variants and ASD clinical phenotype exists but should be treated as preliminary and not curated as a risk factor.

**Modifier genes — genetic background is a demonstrated modifier.** This is one of the better-established modifier findings for any ASD gene, and it comes from a deliberately designed experiment rather than post-hoc observation. Tabbaa, Knoll & Levitt (Neuron 2023; PMID:36738737) crossed a *Chd8* mutation across a mouse genetic reference panel:

> The study measured "clinically relevant phenotypes in >1,000 mice from 33 strains, including brain and body weights and cognition, activity, anxiety, and social behaviors." "Trait disruptions mimicked those seen clinically, with robust strain and sex differences, with some strains exhibiting large effect-size trait disruptions, sometimes in opposite directions, and others expressing resilience."

The finding that identical *Chd8* lesions produce **opposite-direction effects** on different genetic backgrounds — and frank resilience on some — is mechanistically important: it means the marked clinical variability in human CHD8-NDD (§9.3) is plausibly *modifier-driven* rather than purely stochastic. No specific human modifier locus has been identified. `evidence_source: MODEL_ORGANISM`.

**Mutation dosage as a modifier of sex effects.** A homozygous *Chd8* mouse model (Mol Psychiatry, May 2026; DOI 10.1038/s41380-026-03646-9) carrying the human CHD8-Asn2373LysfsX2 allele showed that "compared to heterozygous mice, the homozygous mice showed more robust phenotypes, including increased ASD-related behaviors and brain volume, decreased cerebral blood volume/flow, brain rhythms, and synaptic transmission." Critically: "while heterozygous mice on a pure background predominantly displayed behavioral deficits in males, the homozygous mutants in the hybrid background exhibited more pronounced female phenotypes, suggesting the interaction of genetic background and mutation dosage." This bears on the female-protective-effect hypothesis (§9.3). No human homozygotes are known; this is a model-organism finding only.

**Sex as a risk factor.** Male sex is a robust risk factor for ascertainment and possibly for severity. GeneReviews: *"Of the 103 individuals for whom sex is known, 69 (67%) are male."* Ostrowski 2019 reported 21:6 (3.5:1); Douzgou 2019 reported 2.7:1; Dingemans 2022 reported 76 male / 30 female (2.5:1). See §9.3 for the important counterpoint that Dingemans found no *severity* difference by sex.

**Parental age.** No CHD8-specific analysis exists. The general paternal-age effect on de novo point mutations applies but should not be curated as a CHD8-specific risk factor without direct evidence.

### 2.3 Protective Factors

**No genetic or environmental protective factors are established in humans.** This is a genuine information gap, not an omission.

Two adjacent findings should be recorded as *leads only*:
- **Resilient mouse strains** (Tabbaa 2023) demonstrate that background-encoded resilience to *Chd8* haploinsufficiency exists in principle; the responsible loci are unmapped.
- **Female protective effect.** The male excess is consistent with the general female protective effect in ASD, but the Mol Psychiatry 2026 homozygous data suggest that protection is *overridden* at high mutational dose, and Dingemans 2022 found no sex difference in severity among affected individuals (p = 0.93). The honest statement is that a female protective effect operates on *liability/ascertainment* but is not demonstrated to operate on *severity given diagnosis*.

### 2.4 Gene-Environment Interactions

**No CHD8-specific gene-environment interaction has been demonstrated.** No CTD, PheGenI, or GxE-database entry links CHD8 to an environmental exposure in the context of this disorder.

One indirect and speculative thread worth noting but not curating as a disease mechanism: *Chd8* has been reported to modulate outcomes after traumatic brain injury via Wnt signaling in rodents (PMID:32034634) — an unrelated experimental context that does not bear on CHD8-NDD pathogenesis.

---

## 3. Phenotypes

### 3.1 Core Phenotype Table — GeneReviews Synthesis (n = 115)

GeneReviews (PMID:36302072) Table 2 gives the reference frequencies for clinical use. GeneReviews states: *"To date, 115 individuals have been identified with a pathogenic heterozygous sequence variant in CHD8 for whom some phenotypic information is reported."*

| Feature | Frequency | Suggested HP term (ID verified) | Onset | Course |
|---|---|---|---|---|
| Macrocephaly | **80%** | `HP:0000256` | Infancy | Stable/progressive percentile crossing |
| Tall stature | **80%** | `HP:0000098` | Puberty (most typical) | Stable |
| Autism spectrum disorder | **75–80%** | `HP:0000717` | Toddler/preschool | Chronic, lifelong |
| DD / intellectual disability | **75–80%** | `HP:0001263` (DD) / `HP:0001249` (ID) | Infancy | Static encephalopathy |
| Sleep disturbance | **67%** | `HP:0002360` | Childhood | Chronic, often persistent |
| Gastrointestinal problems | **63%** | `HP:0011024`* / `HP:0002019` (constipation) | Infancy/childhood | Chronic, fluctuating |
| ADHD | **50%** | `HP:0007018` | School age | Chronic |
| Anxiety | **29%** | `HP:0000739` | School age → adolescence | **Worsens with age** |
| Hypotonia | **27%** | `HP:0001252`; neonatal `HP:0001319` | Neonatal/infancy | Often improves |
| Seizures | **12%** | `HP:0001250` | Variable | Variable |
| Developmental regression | "up to half" | `HP:0002376` | Infancy/early childhood | Episodic |
| Motor delay | 90% (when reported) | `HP:0001270` | Infancy | Static |
| Dystonia | Rare (4 individuals) | `HP:0001332` | Childhood → adult | **Progressive** |
| Chiari I malformation | Rare (3 individuals) | `HP:0002308` | Variable | May require decompression |

\* `HP:0011024` was not present in the cached phenotype enum and must be checked; `HP:0002019` (constipation), `HP:0002014` (diarrhea) were verified.

GeneReviews on regression and severity:
> "Developmental regression of social, speech, and/or motor skills in infancy and early childhood is reported in up to half of affected individuals."
> "The severity ranges from mild to severe, although most individuals show cognitive impairment in the mild-to-moderate range."
> "The average severity of autism symptoms is within the moderate range."

### 3.2 The Largest Cohort — Dingemans et al. 2022 (n = 106) and the Frequency Discrepancy

Dingemans et al. (Transl Psychiatry 2022; PMID:36182950) assembled the largest series and, importantly, coded features in HPO:

> "We collected and reviewed 106 individuals with IDDAM, including 36 individuals not previously published, thus enabling thorough genotype–phenotype analyses, involving the CHD8 mutation spectrum, characterization of the CHD8 DNA methylation episignature, and the systematic analysis of phenotypes collected in Human Phenotype Ontology (HPO)."

Cohort: 106 individuals (76 male, 30 female); median age 7 years (range 1–57); 70 from 17 published reports plus 36 novel.

| Feature | n/N | % | HP term |
|---|---|---|---|
| Behavioral problems | 84/95 | 88% | `HP:0000708` |
| Autism spectrum disorder | 71/94 | 76% | `HP:0000717` |
| Intellectual disability | 55/81 | 68% | `HP:0001249` |
| Macrocephaly (at examination) | 46/88 | 52% | `HP:0000256` |
| Macrocephaly (at birth) | 8/15 | 53% | `HP:0000256` |
| Tall stature | 39/78 | 50% | `HP:0000098` |
| Overweight/obesity | 24/71 | 34% | `HP:0001513` |
| Hypotonia | 22/75 | 29% | `HP:0001252` |
| Seizures | 13/75 | 17% | `HP:0001250` |
| Motor delay | 16/53 | 30% | `HP:0001270` |
| Speech delay | 11/61 | 18% | `HP:0000750` |
| Short attention span | 30/94 | 32% | `HP:0007018` (approx.) |
| Sleep disturbance | 27/94 | 29% | `HP:0002360` |
| Insomnia | 19/95 | 20% | `HP:0100785` |
| Stereotypy | 20/94 | 21% | `HP:0000733` |
| Aggressive/impulsive behavior | 16/94 | 17% | `HP:0000718` |
| Repetitive/compulsive behavior | 13/94 | 14% | `HP:0000733` (approx.) |
| GI abnormalities (any) | 35/66 | 53% | — |
| Constipation | 22/66 | 33% | `HP:0002019` |
| Diarrhea | 10/66 | 15% | `HP:0002014` |
| Musculoskeletal abnormality (any) | 49/62 | 79% | — |
| Abnormal foot morphology | 17/62 | 27% | `HP:0001763` (pes planus) |
| Eye abnormality (any) | 30/63 | 48% | — |
| Hypertelorism | 17/63 | 27% | `HP:0000316` |
| Ear abnormality | 19/61 | 31% | `HP:0000358` (post. rotated) |
| Nose abnormality | 18/60 | 30% | `HP:0000431` (wide nasal bridge) |
| Genitourinary abnormality | 10/55 | 18% | — |
| Cardiac abnormality | 3/51 | 6% | — |
| Hyperbilirubinemia | 6/53 | 11% | `HP:0002904` |
| Neoplasia | 6/54 | 11% | `HP:0002664` — **see §11.4 caution** |

ID severity distribution among those with severity specified: **mild 48%, moderate 24%, severe 28%.**

**The frequency discrepancy is real and must be curated honestly.** GeneReviews reports macrocephaly at 80% and tall stature at 80%; Dingemans reports 52% and 50%. These are not reconcilable by rounding. The most likely explanation is **ascertainment**: Ostrowski's cohort (PMID:31721432) was recruited *through overgrowth clinics*, Bernier's *through autism cohorts*, and Dingemans' by literature aggregation across both — so the pooled Dingemans figure regresses toward a lower, probably less biased estimate, while GeneReviews' higher figure reflects the overgrowth-enriched series that defined the syndrome.

**Curation guidance:** when populating `frequency:` on phenotype records, use the enum band that is defensible across both sources rather than picking the higher figure. For macrocephaly and tall stature, `FREQUENT` (spanning ~50–80%) is honest; `VERY_FREQUENT` is not supportable given Dingemans. Per `docs/frequency-evidence-guidelines.md`, each frequency band needs its own evidence item quoting the quantitative statement — the association snippet alone will not do.

### 3.3 Overgrowth Phenotype — Ostrowski 2019 (n = 27)

Ostrowski et al. (Am J Med Genet C 2019; PMID:31721432) is the deepest overgrowth characterization: 27 unrelated patients (25 null variants, 2 missense), M:F 21:6.

- **All 27 had intellectual disability; 85% mild or moderate.**
- **23/27 (85%) met formal overgrowth criteria** — "height and/or head circumference at least 2 standard deviations above the mean."
- Behavioral problems 78%; ASD diagnosis or autistic traits 56%.
- Neonatal hypotonia 9/27 (33%); seizures 4; pes planus 4; scoliosis 2; glabellar hemangioma 2; fifth-finger clinodactyly and umbilical hernia each ≤15%.

The overgrowth is **postnatal and generalized** — height *and* OFC — rather than isolated macrocephaly. This is the discriminating feature versus most other ASD-with-macrocephaly conditions (notably PTEN, where macrocephaly is disproportionate to height). Consider `HP:0005616` (accelerated skeletal maturation) and `HP:0001520` (large for gestational age) as candidate additional terms; both IDs verified, both need frequency evidence before use.

### 3.4 Dysmorphic Features

GeneReviews:
> "Prominent supraorbital ridge, broad forehead with increased occipitofrontal circumference, widely spaced eyes, downslanted palpebral fissures, pointed chin, and large and/or posteriorly rotated ears."

Bernier 2014 described the same gestalt: "increased occipitofrontal circumference (OFC), pronounced supraorbital brow ridges, wide-set eyes with down-slanted palpebral fissures, broad nose with full nasal tip, and pointed chin."

Verified HP candidates: `HP:0000336` (prominent supraorbital ridges), `HP:0000337` (broad forehead), `HP:0002007` (frontal bossing), `HP:0000316` (hypertelorism), `HP:0000494` (downslanted palpebral fissures), `HP:0000307` (pointed chin), `HP:0000358` (posteriorly rotated ears), `HP:0000431` (wide nasal bridge), `HP:0000276` (long face), `HP:0000322` (short philtrum — verified ID, relevance unconfirmed).

Note Dingemans found **forehead abnormality in 17/18 (94%)** and **dental abnormality in 10/11 (91%)** — both with very small denominators, indicating these were only assessed when a dysmorphologist examined the patient. Do not curate 94%/91% as population frequencies; the denominators make them uninterpretable as such. This is exactly the situation `docs/frequency-evidence-guidelines.md` says calls for omitting `frequency:`.

### 3.5 Neuropsychiatric Phenotype

The best-quantified psychiatric data come from the genotype-first study reported in J Neurodev Disord 2024 (16:15; PMC11017562), comparing ADNP, CHD8, and DYRK1A (N=65 total, **n=18 CHD8**, mean age 8.7 y, 40% female), using the **Child Behavior Checklist (CBCL) DSM-5-oriented scales**:

> "Patterns of mental health features varied by group, with anxiety most prominent for CHD8, oppositional features overrepresented among ADNP, and attentional and depressive features most prominent for DYRK1A."
> "For the full sample, age was positively associated with anxiety features, such that elevations in anxiety relative to same-age and same-sex peers may worsen with increasing age."
> "Predictive utility of early developmental milestones was limited, with evidence of early language delays predicting greater difficulties across behavioral domains only for the CHD8 group."

CHD8 group CBCL T-scores (mean, SD, range):
- Anxiety Problems: 64.6 (9.9), 50–82
- Depressive Problems: 66.4 (8.7), 52–82
- ADHD: 61.4 (7.7), 50–80
- Oppositional: 56.4 (7.3), 50–71

> "Within the CHD8 group, a contrasting pattern emerged in which oppositional features were significantly lower than anxiety, depression, and ADHD, all of which had group means approaching clinical thresholds."

Two clinically actionable points emerge: **anxiety is the signature psychiatric feature of CHD8 relative to other ASD genes**, and it **worsens with age** — which makes it a surveillance target, not just a descriptive finding. Note the small n (18) limits precision.

A separate finding worth curating as a cross-domain association: **self-injurious behavior is associated with abdominal pain** in ASD-associated disruptive-mutation carriers (Kurtz-Nelson et al., J Autism Dev Disord 2021; PMID:33175317) — i.e., some challenging behavior in this population is plausibly a pain signal from the GI phenotype rather than a primary behavioral phenotype. `HP:0100716` (self-injurious behavior) verified.

An adult-onset compulsive-behavior presentation has recently been described (Lan et al., Clin Genet 2026, DOI 10.1111/cge.70117), extending the psychiatric spectrum into adulthood.

### 3.6 Movement Disorder Phenotype (Emerging, Female-Skewed)

Dystonia was not part of the original syndrome description and represents a genuine phenotypic expansion. Doummar et al. (Ann Clin Transl Neurol 2021; PMID:34415117) reported childhood-onset progressive dystonia with truncating *CHD8* variants; Sorrentino et al. (J Neurol 2024; PMID:38441608) added three unrelated females:

> Three individuals "presented with young-onset dystonia, with remarkably heterogeneous manifestations ranging from focal, exercise-dependent, apparently isolated forms to generalized permanent phenotypes accompanied by spasticity and tremor. Neurocognitive impairment and autistic behaviors, typical of CHD8-related disorders, were virtually absent or at the mild end of the spectrum."

| Pt | Age/Sex | Variant | Dystonia | Onset | Cognition | Treatment |
|---|---|---|---|---|---|---|
| 1 | 53 F | c.3524_3525insC, p.(Leu1175Phefs*3) | Generalized + cervical, tremor, spasticity | Early childhood | Moderate impairment | Tizanidine, botulinum toxin |
| 2 | 25 F | c.3832dup, p.(Asp1278Glyfs*2) | Focal action-induced (writer's cramp) | 22 y | Cognitively intact | Levodopa ineffective |
| 3 | 7 F | c.1172dup, p.(Gln392Thrfs*29) | Exercise-induced, lower→upper limb | 3 y | Mild impairment | Levodopa partial response |

> "All dystonic CHD8 patients from our case series and the one from Doummar et al. happened to be females" — contrasting with the male predominance of the ASD presentation.

This is a striking and under-appreciated observation: **the two ends of the CHD8 phenotypic spectrum appear to have opposite sex skews.** With n=4 it is not established, but it is a well-defined hypothesis and a candidate `KNOWLEDGE_GAP` discussion entry. Relevant HP terms (verified): `HP:0001332` (dystonia), `HP:0001337` (tremor), `HP:0001257` (spasticity).

### 3.7 Quality-of-Life Impact

No CHD8-specific EQ-5D, SF-36, or PROMIS data exist. QoL impact must be inferred from the constituent phenotypes and stated as such:

- **DD/ID + ASD** — the dominant driver; determines educational placement, supported-living needs, and lifelong caregiver burden. Adaptive outcome is better than in many comparator ASD genes: Beighley 2020 (PMID:31526516) found CHD8 carriers had "less severe adaptive deficits in communication skills, similar functional language... and lower seizure prevalence relative to the other gene group."
- **Sleep disturbance (67%)** — high family-burden feature; disrupts caregiver sleep as well as patient functioning, and is a common driver of clinical presentation.
- **GI problems (53–63%)** — chronic constipation with painful cycling; per PMID:33175317, plausibly a hidden driver of self-injury, meaning its QoL cost is systematically underestimated.
- **Anxiety** — age-progressive, so QoL impact increases through adolescence into adulthood.
- **Dystonia** — where present, dominant motor disability; DBS-responsive (§12).

---

## 4. Genetic / Molecular Information

### 4.1 Causal Gene

**CHD8** — chromodomain helicase DNA-binding protein 8.
- HGNC: `hgnc:20153` · NCBI Gene 57680 · Ensembl ENSG00000100888 · OMIM *610528
- Locus: **14q11.2**
- UniProt: **Q9HCK8**
- Protein family: SNF2/CHD (chromodomain-helicase-DNA-binding) superfamily of ATP-dependent chromatin remodelers, subfamily III
- Domains: tandem N-terminal **chromodomains**, central **SNF2-like ATPase/helicase** domain, BRK domains; "brahma and kismet domains" per NCBI Gene
- **Isoforms:** CHD8L (full length, ~280 kDa) and **CHD8S / Duplin** (~110 kDa, N-terminal chromodomain region, alternative splicing). The existence of a short isoform is mechanistically relevant — variant position relative to the CHD8S stop determines which isoforms are affected, and is an unexplored genotype-phenotype axis.

**Expression:** "Its expression peaks in the early prenatal period of human brain development but continues to be widely expressed throughout the adult brain." Localization: nucleus/nucleoplasm, with reported ciliary-tip localization. High RNA expression in brain, skin, female reproductive tissue. The prenatal expression peak is the basis for the "critical period" framing in §8.3.

### 4.2 Pathogenic Variants

**Variant classes** (Dingemans 2022, PMID:36182950): 29 nonsense, 25 frameshift, 24 missense, 12 splice-site, 2 in-frame deletions, 1 exon 26–28 deletion, 1 translocation across 106 individuals. Truncating variants (nonsense + frameshift + splice ≈ 66 of 94 unique) dominate.

**ACMG/AMP classification.** Truncating variants in *CHD8* meet PVS1 (null variant in a gene where LoF is the established mechanism; ClinGen HI score 3 supports PVS1 application) and, when de novo with confirmed parentage in a phenotype-consistent proband, PS2 — typically yielding Pathogenic. **Missense variants are the interpretation problem.** Dingemans' cohort included 5 individuals with VUS.

**Missense variants are not uniformly pathogenic — this is the single most important variant-interpretation finding.** Shiraishi et al. (Mol Psychiatry 2024; PMID:38438524) tested ASD-patient missense alleles functionally across biochemical activity, ESC neural differentiation, and mouse behavior:

> "Only mutations with high prediction scores gave rise to ASD-like phenotypes in mice, suggesting that not all CHD8 missense mutations detected in ASD patients are directly responsible for the development of ASD."
> Mutations with high scores "cause ASD by mechanisms either dependent on or independent of loss of chromatin-remodeling function."

Two consequences for curation: (i) a *CHD8* missense variant should not be assumed pathogenic without in silico support and ideally functional or episignature data; (ii) **not all pathogenic missense alleles act through loss of remodeling activity** — some operate by a remodeling-independent mechanism, which means "haploinsufficiency" is an incomplete description of the disorder's molecular etiology and the pathophysiology graph should not force every variant through a single node.

**Allele frequency.** Pathogenic *CHD8* variants are absent from population databases: pLI 1.00, LOEUF 0.15, and Bernier's zero truncating events in 8,792 controls. Any *CHD8* truncating variant present at appreciable frequency in gnomAD should prompt re-examination of the annotation.

**Somatic vs germline.** The disease-causing variants are **germline** (overwhelmingly de novo). Somatic *CHD8* alterations occur in cancer (§4.6) but are a **biologically separate phenomenon** and must not be curated as part of this disorder's etiology.

**Functional consequence: loss of function / haploinsufficiency**, with the missense caveat above and a gain-of-function exception noted in the episignature data (§4.5).

### 4.3 Copy-Number and Dosage — Both Directions Matter

*CHD8* is dosage-sensitive in **both** directions, which is unusual and worth explicit curation:

- **Deletion/haploinsufficiency** → CHD8-NDD (this entity).
- **Duplication** → Smol et al. (Neurogenetics 2020; PMID:31823155) described 14q11.2 microduplications involving *CHD8* and *SUPT16H* producing a neurodevelopmental phenotype, concluding this shows "the importance of a tight control of at least CHD8 gene-dosage for a normal development." Corroborated experimentally: *Chd8* duplication in mice causes "behavioral hyperactivity and neurodevelopmental defects" (Nat Commun 2025, DOI 10.1038/s41467-025-59853-5).

Note the tension with ClinGen's **Triplosensitivity score of 0** — the duplication phenotype involves *SUPT16H* as well, so single-gene triplosensitivity is not established. **The 14q11.2 duplication phenotype is a distinct entity and should be a separate KB entry or a `has_subtypes` branch, not folded into CHD8-NDD.**

### 4.4 Modifier Genes

See §2.2. Genetic background is a demonstrated modifier in mouse (PMID:36738737); no human modifier locus is mapped. No `MODIFIER`-typed gene records are yet justifiable for the `genetic:` section.

### 4.5 Epigenetic Information — A Validated Episignature Exists

This is a distinguishing feature of CHD8-NDD relative to most ASD genes and has direct diagnostic utility. Dingemans 2022 (PMID:36182950) characterized a **CHD8/IDDAM DNA methylation episignature** in peripheral blood:

> "11 of the 13 individuals (85%) were classified as positive for IDDAM with high confidence."

Of the remaining two: one inconclusive, and — notably — **one showed a possible gain-of-function signature rather than the expected haploinsufficiency signature.** That single observation is the strongest human-side hint that a non-haploinsufficiency mechanism exists in a subset, converging with Shiraishi 2024's remodeling-independent missense mechanism.

The episignature has since been applied clinically: Furuta et al. (Mol Genet Genomic Med 2025; PMID:41407309) used EpiSign on a proband and father with a *CHD8* missense variant, reporting that "hierarchical clustering and multidimensional scaling plots indicate the proband and father have a DNA methylation profile similar to subjects with a confirmed IDDAM episignature and distinct from controls." That paper simultaneously documents **paternal inheritance with marked phenotypic variability** (§9.2).

**Curation note:** the episignature is a *diagnostic biomarker* (§10) and also a *molecular phenotype*. It is a strong candidate for a `category: Cellular`/molecular phenotype record with `evidence_source: HUMAN_CLINICAL`.

Beyond the episignature, the mechanistic epigenetics are the disease: CHD8 is itself a chromatin remodeler, and heterozygous *CHD8* deletion causes "widespread changes in gene expression and chromatin compaction" (Am J Hum Genet 2023, DOI 10.1016/j.ajhg.2023.10.009).

### 4.6 Somatic CHD8 Alterations in Cancer — Adjacent, Not Part of This Disorder

Recorded here for completeness and to prevent mis-curation:
- Kim et al. (Histopathology 2011; PMID:21447119): *CHD8* mutations found in 10 gastric/colorectal cancers, "detected in microsatellite instability-high (MSI-H) cancers, but not in MSI-L/MSS cancers"; loss of CHD8 expression in **35.7% of gastric** and **28.6% of colorectal** cancers.
- Sawada et al. (Oncol Rep 2013; PMID:23835524): CHD8 expression is an independent prognostic factor in gastric cancer; "loss of CHD8 expression may be a novel indicator for biological aggressiveness."

**These are somatic events in sporadic tumors.** There is **no established germline tumor-predisposition** in CHD8-NDD. Dingemans reported neoplasia in 6/54 (11%), but the report does not establish tumor type, causality, or an excess over baseline — see §11.4.

---

## 5. Environmental Information

- **Environmental factors:** None established. CHD8-NDD is a fully penetrant-by-genotype Mendelian condition; no toxin, radiation, pollutant, or occupational exposure has been implicated in causation or modification. No CTD/TOXNET entry links an exposure to this disorder.
- **Lifestyle factors:** None established as causal. Lifestyle is relevant only to *management* — dietary fiber/hydration for constipation, sleep hygiene, weight management given the 34% overweight rate.
- **Infectious agents:** **Not applicable.**

An honest "no evidence" is the correct content for this section; do not populate speculative environmental factors.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal Chain Overview (proposed pathograph)

```
[MOLECULAR]  Heterozygous CHD8 LoF variant
                 → ~50% reduction in CHD8 protein
                 → impaired ATP-dependent chromatin remodeling at CHD8-bound promoters
                     ├─→ dysregulated Wnt/β-catenin target transcription
                     ├─→ derepression of REST target genes
                     ├─→ derepression of cell-cycle genes (cyclin E2, MAPK pathway)
                     └─→ altered co-regulation of OTHER ASD risk genes
[CELLULAR]       → shortened G1 → neural progenitor over-proliferation / self-renewal
                 → altered excitatory vs inhibitory neuron production timing
                 → increased gliogenesis (primate-specific emphasis)
                 → impaired axon development and neuronal migration
                 → (parallel arm) impaired vagal neural crest → enteric neuron deficit
[TISSUE]         → megalencephaly / increased cortical + white matter volume
                 → altered striatal and cortical circuit function
                 → hypoganglionic / hyposerotonergic gut
[ORGANISM]       → macrocephaly, tall stature, ASD, DD/ID, sleep disturbance,
                   GI dysmotility/constipation, anxiety
```

### 6.2 Molecular Pathways

**Wnt/β-catenin — the founding pathway, with a direction-of-effect complication.** Thompson et al. (Mol Cell Biol 2008; PMID:18378692) established that "CHD8 is an ATP-dependent chromatin remodeling factor that regulates beta-catenin target genes," interacting directly with β-catenin and being recruited to β-catenin-responsive promoters. But the sign of the effect is **cell-type dependent**: CHD8 inhibits β-catenin/Wnt signaling in general, yet "Chd8 is a positive regulator of Wnt signaling in cells of neural lineage both in vivo and in vitro" (Durak et al., Nat Neurosci 2016; PMID:27694995). This is not a contradiction in the literature to be resolved away — it is a genuine context-dependency and should be curated as such, with the neural-lineage direction being the disease-relevant one.

GO candidates (verified): `GO:0016055` (Wnt signaling pathway), `GO:0060070` (canonical Wnt signaling pathway), `GO:0090090` (negative regulation of canonical Wnt signaling pathway).

**Cell cycle / G1 control.** The clearest mechanistic route from chromatin to macrocephaly. "Loss-of-function of a single CHD8 allele shortens the G1 phase of the cell cycle in neural stem cells by relieving transcriptional repression of the MAPK pathway and cyclins E, causing overproliferation of cortical progenitors by accelerating the cell cycle and promoting self-renewing divisions at the expense of neurogenic ones" (Biology Open 2022, 11:bio058941). Consistent with Rodríguez-Paredes et al. (Nucleic Acids Res 2009; PMID:19255092): "The chromatin remodeling factor CHD8 interacts with elongating RNA polymerase II and controls expression of the cyclin E2 gene." GO: `GO:0051726` (regulation of cell cycle), `GO:0008284` (positive regulation of cell population proliferation), `GO:0000122` (negative regulation of transcription by RNA Pol II).

**REST-mediated repression.** Katayama et al. (Nature 2016; PMID:27602517): "Expression of RE-1 silencing transcription factor (REST) target genes was reduced in embryonic brains of Chd8 mutant mice as well as in the brains of humans with ASD, and CHD8 was found to physically interact with REST in mouse brain tissue." The convergence of the mouse result with idiopathic human ASD brain is what makes this arm translationally credible.

**p53 axis.** Nishiyama et al. (Nat Cell Biol 2009; PMID:19151705): "CHD8 suppresses p53-mediated apoptosis through histone H1 recruitment during early embryogenesis." CHD8 loss → ATM activation → increased p53 phosphorylation and decreased p53 ubiquitination → apoptosis. This explains the embryonic lethality of homozygous *Chd8* null in mouse and is the reason viable homozygous models required specific alleles/backgrounds.

**ERK-MAPK / ELK1 recruitment.** CHD8 recruitment to promoters is serum- and ERK-ELK-dependent; "the autism risk factor CHD8 is a chromatin activator in human neurons and functionally dependent on the ERK-MAPK pathway effector ELK1" (PMC9794786). This positions CHD8 downstream of a signaling pathway, not merely as a constitutive remodeler.

**Co-regulation of other ASD risk genes — the "hub" property.** Cotney et al. (Nat Commun 2015; PMID:25752243), "The autism-associated chromatin modifier CHD8 regulates other autism risk genes during human neurodevelopment," and Sugathan et al. (PNAS 2014; PMID:25294932) established that CHD8 binds and regulates a large set of independently-identified ASD genes. Sugathan: suppression of CHD8 in neural progenitors "caused altered expression of 1,756 genes, 64.9% of which were up-regulated" — the up-regulation bias is consistent with a predominantly repressive role at these targets. Wilkinson et al. (Transl Psychiatry 2015; PMID:25989142) extended this to noncoding RNAs.

**Adipogenesis (off-axis but possibly relevant to overweight).** "The Autism-Related Protein CHD8 Cooperates with C/EBPβ to Regulate Adipogenesis" (Cell Rep 2018; PMID:29768199) — a plausible but unproven mechanistic link to the 34% overweight rate. Curate as a hypothesis, not an established chain.

### 6.3 Cellular Processes

**Neural progenitor over-proliferation** is the central cellular event. Villa et al. (Cell Rep 2022; PMID:35385734) resolved the developmental timing with unusual precision:

> CHD8 haploinsufficiency "disrupts neurodevelopmental trajectories by promoting an accelerated generation of inhibitory neurons and a delayed production of excitatory neurons with a temporally restricted cell-type-specific effect on proliferation of radial glial cells."

The word doing the work is **"transient"** (in the paper's title: "transient alterations in excitatory and inhibitory trajectories"). The E/I imbalance is a *timing* defect during a bounded window, not a permanent cell-fate defect — which is precisely why the critical-period framing in §8.3 matters therapeutically.

**Gliogenesis — the primate-specific arm.** Li et al. (Cell Discov 2023; PMID:36878905) used CRISPR/Cas9 in cynomolgus monkey embryos:
- Mutant monkeys showed brain weight 57.8 g vs control 45 ± 2.8 g — **~28% larger**
- "Disrupting CHD8 in the fetal monkey brain prior to gliogenesis increased the number of glial cells in newborn monkeys"
- Knockdown in organotypic newborn-monkey brain slices also enhanced glial proliferation
- Enlarged **white matter** near the lateral ventricle

This matters because rodent models gave "inconsistent findings about the mechanisms for CHD8 deficiency-mediated autism symptoms and macrocephaly." The primate data suggest **glial expansion, not neuronal excess, is the dominant driver of megalencephaly in primates** — and this is directly corroborated in mouse by the finding of "increased cortical volume without increased neuron number in heterozygous Chd8 mutant mouse cortex" (bioRxiv 2021). GO: `GO:0042063` (gliogenesis), `GO:0022008` (neurogenesis), `GO:0021895`; UBERON: `UBERON:0002316` (white matter).

**Axon development and migration.** "Autism-associated CHD8 deficiency impairs axon development and migration of cortical neurons" (Mol Autism 2018; PMID:30574290). GO: `GO:0016477` (cell migration), `GO:0031175` (neuron projection development).

**Oligodendrocyte-autonomous effects.** "Chd8 mutation in oligodendrocytes alters microstructure and functional connectivity in the mouse brain" (Mol Brain 2020; PMID:33228730) — the white-matter phenotype is at least partly oligodendrocyte-intrinsic, not purely secondary. CL: `CL:0000128`.

**Microglial effects.** "CHD8 adulthood microglial knockdown in C57BL6 mice induces behavioral, morphological, and transcriptional changes in a sex-dependent manner" (Transl Psychiatry 2025) — notable because it is an **adult** manipulation producing behavioral change, arguing against a purely developmental model. CL: `CL:0000129`.

**Adult neurogenesis.** "Conserved and Distinct Functions of the Autism-Related Chromatin Remodeler CHD8 in Embryonic and Adult Forebrain Neurogenesis" (J Neurosci 2022; PMID:36127134).

**Protein homeostasis.** "Chd8 haploinsufficiency impairs early brain development and protein homeostasis later in life" (Mol Autism 2020; PMID:33023670) — a two-phase model: developmental defect plus a distinct later-life proteostasis phenotype.

**Persistent adult dysfunction.** "Persistent cortical excitatory neuron dysregulation in adult Chd8 haploinsufficient mice" (2025; PMID:40501938) — the phenotype does not fully normalize after development.

### 6.4 The Enteric / Gut Arm — A Genuinely Distinct Mechanistic Branch

The GI phenotype is not a nonspecific comorbidity; it has a demonstrated developmental mechanism, and its discovery in the founding paper is part of what makes CHD8 a *syndrome* rather than a behavioral phenotype. Bernier 2014 (PMID:24998929) showed zebrafish *chd8* disruption "recapitulates features of the human phenotype, including increased head size" and impaired GI motility due to reduced enteric neurons.

Subsequent work (Life Sci Alliance 2023, PMC9664244; bioRxiv 2021) refined this:
- "Loss of chd8 leads to a reduced number of vagal neural crest cells (NCCs), enteric neural and glial progenitors emigrating from the neural tube, with altered early migration capability."
- Colonization eventually completes, but "decreased numbers of both serotonin-producing enterochromaffin cells and neural crest-derived serotonergic neurons were observed, suggesting intestinal hyposerotonemia in the absence of chd8."
- Reported GI burden in CHD8 cases: "80% of CHD8 cases presenting gastrointestinal complaints, including 60% with recurring periods of considerable constipation followed by loose stool or diarrhea."

The **alternating constipation/loose-stool pattern** is clinically distinctive and consistent with a dysmotility rather than an obstructive mechanism. GO: `GO:0014033` (neural crest cell differentiation), `GO:0048484` (enteric nervous system development). CL: `CL:0000333` (migratory neural crest cell), `CL:0007011` (enteric neuron). UBERON: `UBERON:0002005` (enteric nervous system), `UBERON:0000160` (intestine), `UBERON:0005409` (gastrointestinal system).

### 6.5 The Sleep Arm — Glial, Serotonergic, and Reversible

Coll-Tané et al. (Sci Adv 2021; PMID:34088660), "The CHD8/CHD7/Kismet family links blood-brain barrier glia and serotonin to ASD-associated sleep defects," is the most mechanistically complete account of any single CHD8 phenotype:

- Individuals with *CHD8* or *CHD7* mutations "suffer from disturbed sleep maintenance," recapitulated in *Drosophila kismet* mutants (the sole CHD8/CHD7 ortholog).
- "Kismet is required in glia for early developmental and adult sleep architecture, with this role localizing to subperineurial glia constituting the blood-brain barrier."
- "The Kismet-related sleep disturbances are caused by high serotonin during development, paralleling a well-established but genetically unsolved autism endophenotype."
- **"Despite their developmental origin, Kismet's sleep architecture defects can be reversed in adulthood by a behavioral regime resembling human sleep restriction therapy."**

The last point is the most clinically consequential statement in the entire CHD8 mechanism literature: a *developmentally originated* phenotype was **reversed by a behavioral intervention in adults**. It provides a mechanistic rationale for behavioral sleep intervention in CHD8-NDD (which GeneReviews already recommends empirically) and is a strong candidate for a `MECHANISTIC_HYPOTHESIS`-grounded entry. Note the serotonin direction: *high* serotonin developmentally in fly, versus *hyposerotonemia* in the zebrafish gut — these are different compartments and should not be collapsed.

Rodent corroboration: *Chd8* knockout mice show "reduced wakefulness and increased rapid eye movement (REM) sleep duration during the dark phase, along with disruption of normal daily REM sleep fluctuations" (PMC12713839).

CHEBI: `CHEBI:28790` (serotonin, verified).

### 6.6 Protein Dysfunction

Haploinsufficiency — reduced quantity of a structurally normal protein — is the principal mechanism for truncating alleles (NMD-mediated transcript degradation). No misfolding or aggregation mechanism is described. For missense alleles the picture is more complex (§4.2): some act via loss of remodeling activity, others via a **remodeling-independent** mechanism (Shiraishi 2024, PMID:38438524), and at least one human case shows a **gain-of-function-like episignature** (Dingemans 2022). Verified GO MF terms: `GO:0003682` (chromatin binding), `GO:0016887` (ATP hydrolysis activity). Verified GO CC terms: `GO:0005634` (nucleus), `GO:0000785` (chromatin), `GO:0005654` (nucleoplasm).

CHD8 also participates in a defined protein complex: "NSD3-Short Is an Adaptor Protein that Couples BRD4 to the CHD8 Chromatin Remodeler" (Mol Cell 2015; PMID:26626481) — a BRD4-NSD3-CHD8 module.

### 6.7 Metabolic, Immune, and Tissue-Damage Mechanisms

- **Metabolic:** No inborn-error-type metabolic defect. Peripheral relevance: the CHD8-C/EBPβ adipogenesis link (PMID:29768199) and the "protein homeostasis later in life" finding (PMID:33023670). The homozygous mouse implicated "mitochondrial activity" pathways transcriptomically. None is an established human metabolic abnormality.
- **Immune:** No autoimmunity, immunodeficiency, or chronic inflammation is part of the phenotype. Microglia are involved as a *neural* cell type (PMID: Transl Psychiatry 2025), not as an immune-dysfunction mechanism. **Do not curate an immune arm.**
- **Tissue damage:** CHD8-NDD is a **developmental/dysgenetic** disorder, not a degenerative one — there is no oxidative-stress, ischemia, fibrosis, or necrosis mechanism. The one qualification is the progressive dystonia subgroup (§3.6) and the "persistent adult dysregulation" findings, which raise but do not establish a progressive component.

### 6.8 Molecular Profiling

- **Transcriptomics:** Extensive. Sugathan 2014 (PMID:25294932, human NPCs, 1,756 DEGs); Cotney 2015 (PMID:25752243); Katayama 2016 (PMID:27602517, mouse brain); Gompers 2017 (PMID:28671691, "Germline Chd8 haploinsufficiency alters brain development in mouse," reporting a developmental RNA-splicing phenotype); Wang 2017 (CHD8+/− cerebral organoids, DLX/GABAergic dysregulation, WNT/β-catenin pathway enrichment, overlap with idiopathic ASD DEGs); "Common CHD8 Genomic Targets Contrast With Model-Specific Transcriptional Impacts of CHD8 Haploinsufficiency" (PMC6339895) — **the binding targets are shared across models while the transcriptional consequences are model-specific**, an important caution for cross-model inference. First whole-transcriptome RNA-seq on a CHD8-haploinsufficient *patient* plus cross-model meta-analysis: PMC7710346.
- **Epigenomics:** the IDDAM blood episignature (§4.5); genome-wide chromatin compaction changes (AJHG 2023).
- **Proteomics / metabolomics / lipidomics:** No disease-specific human datasets identified. **Genuine gap.**
- **Single-cell:** Villa 2022 (PMID:35385734) provides the cell-type-resolved developmental trajectory data.
- **Functional genomics screens:** CRISPR/Cas9 heterozygous knockout with transcriptional network characterization (Mol Autism 2015; PMID:26491539). Enhancer-targeted CRISPR-activation rescue (§12.3).

---

## 7. Anatomical Structures Affected

### 7.1 Organ Level

**Primary:** Central nervous system — `UBERON:0001017` (central nervous system), `UBERON:0000955` (brain), `UBERON:0001890` (forebrain), `UBERON:0000956` (cerebral cortex), `UBERON:0002435` (striatum), `UBERON:0002316` (white matter). All IDs verified.

Striatal involvement is specifically evidenced: "Chd8 Mutation Leads to Autistic-like Behaviors and Impaired Striatal Circuits" (Platt et al., Cell Rep 2017; PMID:28402856). Cortical over-connectivity: "Altered Neocortical Gene Expression, Brain Overgrowth and Functional Over-Connectivity in Chd8 Haploinsufficient Mice" (Suetterlin et al., Cereb Cortex 2018).

**Second primary system — enteric/GI:** `UBERON:0005409` (gastrointestinal system), `UBERON:0000160` (intestine), `UBERON:0002005` (enteric nervous system). This is a *primary* rather than secondary involvement, since the mechanism is developmental (vagal neural crest, `UBERON:0001049` neural tube) rather than a downstream consequence of CNS disease.

**Skeletal/growth:** generalized overgrowth affects the skeleton (tall stature, accelerated maturation) and the cranium.

**Secondary/less frequent:** genitourinary (18%), cardiac (6%, `UBERON:0000948`), hepatic (hyperbilirubinemia 11%), ophthalmologic (48% any eye abnormality).

**Body systems:** nervous (primary), digestive (primary), musculoskeletal (79% any abnormality), endocrine/growth, integumentary (glabellar hemangioma).

### 7.2 Tissue and Cell Level

| Cell population | CL term (verified) | Involvement |
|---|---|---|
| Neural stem/progenitor cell | `CL:0000047` | Over-proliferation, shortened G1 — the central lesion |
| Neural cell (general) | `CL:0002319` | |
| Neuron | `CL:0000540` | Delayed maturation, axon/migration defects |
| Glutamatergic (excitatory) neuron | `CL:0000679` | **Delayed** production (Villa 2022) |
| GABAergic (inhibitory) neuron | `CL:0000617` | **Accelerated** production (Villa 2022) |
| Glial cell | `CL:0000125` | Expanded — primate driver of megalencephaly |
| Astrocyte | `CL:0000127` | |
| Oligodendrocyte | `CL:0000128` | Cell-autonomous white-matter microstructure effects |
| Microglial cell | `CL:0000129` | Adult knockdown → behavioral/morphological change |
| Migratory neural crest cell | `CL:0000333` | Vagal NCC deficit → enteric hypoganglionosis |
| Enteric neuron | `CL:0007011` | Reduced number → dysmotility |

Radial glia are specifically implicated (Villa 2022) but a suitable CL ID was not confirmed against the cached enum; verify before use.

Note also *Drosophila* subperineurial glia constituting the blood-brain barrier (Coll-Tané 2021) — no direct human CL/UBERON equivalent to assert.

### 7.3 Subcellular Level

`GO:0005634` (nucleus), `GO:0000785` (chromatin), `GO:0005654` (nucleoplasm) — all verified. CHD8 is a nuclear chromatin-associated protein; the reported ciliary-tip localization is intriguing (given ciliopathy overlap in brain overgrowth) but is a Human Protein Atlas annotation, not a disease-mechanism finding, and should not be curated as pathophysiology.

### 7.4 Localization and Lateralization

Involvement is **bilateral and symmetric** — expected for a germline chromatin-remodeling defect acting on global developmental programs. Macrocephaly is symmetric; there is no reported asymmetry, focal malformation, or lateralized lesion. The exception is Chiari I malformation (3 individuals), a midline posterior-fossa finding.

---

## 8. Temporal Development

### 8.1 Onset

**Molecular onset is prenatal** — *CHD8* expression peaks in early prenatal brain development, and the primate data show the critical gliogenic effect occurs *in utero* ("prior to gliogenesis").

**Clinical onset is staged, and the staging is diagnostically useful:**

| Period | Manifestation |
|---|---|
| Prenatal/birth | Macrocephaly present at birth in ~53% (8/15, Dingemans); large for gestational age in some |
| Neonatal | Hypotonia (27–33%); feeding issues |
| Infancy | Macrocephaly becomes apparent in most ("most often during infancy"); motor and speech delay; GI problems begin |
| Early childhood | ASD diagnosis; **developmental regression in up to half**; sleep disturbance |
| School age | ADHD; anxiety emerges |
| **Puberty** | **Tall stature "most typically during puberty"** |
| Adolescence/adult | Anxiety worsens with age; adult-onset compulsive behaviors (Lan 2026); dystonia in rare cases (onset 3 y to 22 y) |

The **onset pattern is chronic/insidious**, not acute — with the exception of the regression episodes, which are subacute, and seizures, which are episodic.

### 8.2 Progression

- **Course:** Predominantly **static encephalopathy with age-dependent phenotypic evolution** — the neurodevelopmental deficit itself does not progress, but new features emerge on a developmental schedule (tall stature at puberty, anxiety through adolescence).
- **Formal staging:** None exists. No AJCC/WHO-type staging is applicable.
- **Progression rate:** Not applicable for the core phenotype. Where dystonia occurs it is explicitly **progressive** ("childhood-onset progressive dystonia," PMID:34415117).
- **Duration:** Chronic, lifelong. Median age in the largest cohort was 7 years with range to **57 years**, confirming survival into later adulthood.
- **Regression:** Reported in up to half in infancy/early childhood, affecting social, speech, and/or motor skills. Whether recovery from regression is complete is not documented — a real gap.

### 8.3 Critical Periods

Two well-defined windows of vulnerability, both experimentally supported:

1. **Midfetal ventral progenitor window.** A 2026 Nat Commun study (DOI 10.1038/s41467-026-73416-2) found that "*Chd8* mutation during the midfetal period — in particular, in ventral progenitor cells — contributes to the development of autistic-like behavior," and, critically, that **"restoration of Chd8 expression in ventral progenitor cells ameliorates both the behavioral phenotypes and aberrant ventral differentiation in Chd8 mutant mice."** This defines both a vulnerability window and a therapeutic-target window.
2. **Pre-gliogenic fetal window** (primate; PMID:36878905) — disruption before gliogenesis is what produces the glial excess and macrocephaly.

**Counterbalancing this, three findings argue that developmental origin does not equal developmental irreversibility:**
- Fly sleep architecture defects "can be reversed in adulthood by a behavioral regime resembling human sleep restriction therapy" (PMID:34088660).
- Adult microglial *Chd8* knockdown alone produces behavioral change (Transl Psychiatry 2025) — implying ongoing adult CHD8 function.
- CRISPR-activation rescue of over-proliferation persists "for several months post-treatment" in human organoids (§12.3).

The window for intervention is therefore probably **wider than the developmental-origin framing implies** — an important, and appropriately hedged, statement for the KB.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**No population prevalence estimate exists.** Every available figure is a *yield within an ascertained cohort*, and must be labeled as such — conflating these with population prevalence is the most likely curation error in this section.

| Estimate | Denominator | Source |
|---|---|---|
| 9 de novo LoF | 2,446 individuals with ASD (~0.37%) | GeneReviews |
| 8 de novo LoF | 3,730 individuals with NDD (~0.21%) | GeneReviews / Bernier |
| "as high as one in 500" (0.2%) | population of individuals with ASD | GeneReviews, citing one study |
| **1.7%** | individuals with **both overgrowth and ID** | GeneReviews |
| **~2%** | 366 macrocephalic SSC probands (OFC z > 2.0) | Simons Simplex Collection |
| 0.21% | of ASD individuals overall | commonly cited figure |

The gradient is informative: yield rises from ~0.2% in unselected ASD to **~2% when macrocephaly is required** and 1.7% with overgrowth+ID — a ten-fold enrichment that directly justifies phenotype-targeted testing (§10.4).

**For the `prevalence:` slot,** structure these as:
- `measure_type: UNKNOWN` or a diagnostic-yield note — *not* `POINT_PREVALENCE`, since these are cohort yields.
- `prevalence_class: ULTRA_RARE` or `UNKNOWN` for the population figure.
- Put the cohort denominator in `population:` and the verbatim phrasing in `notes:`.
- Do **not** invent a `rate_per_100000`. A crude derivation (ASD prevalence ~1–2% × 0.2% CHD8 yield ≈ 2–4 per 100,000) is arithmetically available but rests on assumptions the sources do not make; if recorded at all it belongs in `notes:` as an explicit derivation, not as a sourced rate.

**Incidence:** no estimate available.

### 9.2 Inheritance

**Mode:** Autosomal dominant. GeneReviews: *"Autosomal dominant disorder; the majority of affected individuals have a de novo pathogenic variant."* Suggested inheritance term: HP:0000006 (Autosomal dominant inheritance) — **verify ID before use**, it was not in the batch I checked.

**De novo rate:** *"Most probands (85%–90%) reported to date whose parents have undergone molecular genetic testing have the disorder as the result of a de novo CHD8 pathogenic variant."*

**Inherited cases occur.** The 10–15% inherited fraction is clinically important and is where the counseling complexity lies. Furuta et al. 2025 (PMID:41407309) documented **paternal transmission of a *CHD8* missense variant with marked phenotypic variability**, confirmed in both father and proband by EpiSign — a case that simultaneously demonstrates (a) inheritance from a mildly affected/unrecognized parent, (b) the utility of episignature testing for missense variants, and (c) the reality of intrafamilial variability. Sorrentino's dystonic patients (ages 25, 53) with minimal cognitive involvement (PMID:38441608) similarly show that mildly affected adult carriers exist and can go undiagnosed.

**Recurrence risk:**
- Affected parent: **50%** per pregnancy.
- Apparently de novo with unaffected, tested parents: *"estimated to be 1% because of the theoretic possibility of parental germline mosaicism."*

**Germline mosaicism:** theoretically possible; drives the 1% empiric figure. No confirmed CHD8 germline-mosaicism case was identified.

**Penetrance:** High but **not demonstrably complete**, and the field has not resolved this. The paternal-transmission case and the cognitively-intact dystonic carriers show that carriers can be mild enough to escape ascertainment. Curate as **high, incompletely characterized penetrance with markedly variable expressivity** — and avoid the common overstatement of "complete penetrance," which the inherited cases do not support.

**Expressivity:** Highly variable. Dingemans: median De Vries score 3.0 for non-missense, 1.0 for missense (p=0.046); ID severity mild 48% / moderate 24% / severe 28%; and phenotypes ranging from severe ID+ASD to isolated adult focal dystonia in a cognitively intact individual.

**Anticipation:** Not applicable — not a repeat-expansion disorder. No evidence of anticipation.

**Founder effects / consanguinity / carrier frequency:** None. Not applicable to a de novo-predominant AD disorder. Carrier screening is not applicable.

### 9.3 Genotype-Phenotype Correlations

GeneReviews states flatly: **"No genotype-phenotype correlations have been identified."**

Dingemans 2022 (PMID:36182950) found one, modest and worth recording:
> "Individuals with a missense variant were less severely affected than individuals with other variants (median De Vries score 1.0 vs. 3.0; p = 0.046)."

At p = 0.046 with 24 missense in a 106-person cohort this is a borderline finding that has not been replicated; it is also confounded by the fact — established by Shiraishi 2024 (PMID:38438524) — that some *CHD8* missense variants in ASD patients **are not causal at all**. Milder average severity in the missense group may partly reflect inclusion of non-causal variants rather than a true attenuated allele effect. Curate the correlation with that caveat attached.

**Sex and severity:** Dingemans found **"No statistically significant differences were observed between males and females (p = 0.93)"** for severity. Combined with the 2.5–3.5:1 male ascertainment ratio, the coherent interpretation is that **sex affects liability/ascertainment, not severity given diagnosis** — with the possible exception of the dystonic subgroup, which is female-skewed (§3.6).

### 9.4 Population Demographics

- **Affected populations:** No ethnic or geographic enrichment. De novo mutation is population-independent. Cases are reported worldwide (European, North American, Japanese, Korean — e.g., PMID:36731504, a Korean boy with overgrowth, ID, and autism).
- **Geographic distribution:** Global; no endemic areas; no population-specific founder variants.
- **Sex ratio:** 67% male (69/103, GeneReviews); 2.5:1 (Dingemans), 2.7:1 (Douzgou), 3.5:1 (Ostrowski). Overall ~2.5–3.5:1 M:F. **Note the inversion in the dystonia subgroup (4/4 female).**
- **Age distribution:** Ascertainment is pediatric-skewed (Dingemans median 7 y), but range extends to 57 y. The adult population is almost certainly under-ascertained, given that genome-wide testing became routine only recently and mildly affected adults exist.

---

## 10. Diagnostics

### 10.1 Establishing the Diagnosis

GeneReviews:
> "The diagnosis of CHD8-NDD is established in a proband by identification of a heterozygous pathogenic (or likely pathogenic) variant in CHD8 by molecular genetic testing."

Diagnosis is **molecular, not clinical.** There are no consensus clinical diagnostic criteria — a fact worth recording explicitly, since it distinguishes CHD8-NDD from syndromes like Sotos or Beckwith-Wiedemann that have scoring systems.

**Suggestive clinical findings** (prompting testing):
- DD and/or ID, most often mild-to-moderate
- Neuropsychiatric disorders including ASD
- Generalized overgrowth (tall stature, macrocephaly)
- Sleep disturbance
- GI problems, especially constipation

The combination of **overgrowth + ID/ASD** is the highest-yield trigger (1.7% yield; ~2% in macrocephalic ASD probands).

### 10.2 Genetic Testing Approach

| Modality | Utility for CHD8-NDD |
|---|---|
| **Exome sequencing (WES)** | **First-line.** Highest practical yield; the modality through which most cases have been found. |
| **Genome sequencing (WGS)** | Equivalent or better; adds structural/non-coding detection. Reasonable first-line where available. |
| **Multigene panels** | Effective if the panel includes CHD8 — verify. Overgrowth-with-ID panels and ASD/ID panels typically include it. |
| **Single-gene *CHD8* sequencing** | Reasonable only when the gestalt is highly specific (overgrowth + ASD + characteristic facies). Generally superseded by WES. |
| **Chromosomal microarray (CMA)** | Detects the minority of cases from 14q11.2 deletions/duplications; will **miss** the ~95%+ of cases that are sequence-level. Often performed first in practice; a normal CMA does **not** exclude CHD8-NDD. |
| **Karyotype** | Low yield; would detect only the rare translocation (1 in 106). |
| **FISH** | Not indicated absent a specific CNV hypothesis. |
| **mtDNA testing** | **Not applicable.** |
| **Repeat expansion testing** | **Not applicable.** |

**Trio testing is strongly preferred** — de novo status is both a major ACMG evidence line (PS2) and directly determines recurrence risk (50% vs 1%).

### 10.3 Omics-Based Diagnostics — Episignature Testing

**This is the distinctive diagnostic asset for CHD8-NDD** and directly addresses its main interpretive weakness (missense VUS).

- A validated **IDDAM/CHD8 DNA methylation episignature** exists in peripheral blood (Dingemans 2022, PMID:36182950): "11 of the 13 individuals (85%) were classified as positive for IDDAM with high confidence."
- Available clinically via **EpiSign**; classification uses hierarchical clustering, MDS, and an **MVP (multi-class supervised) score**.
- Blood is the appropriate tissue: "Blood presents itself as the ideal tissue type for episignature development as it is a common clinical sample type and is easily accessible... episignatures represent a fundamental defect in NDDs caused by genetic variation in the germline [so] DNAm changes will be present in all subsequent tissues."
- **Applied use case:** Furuta 2025 (PMID:41407309) resolved a *CHD8* missense VUS segregating from a mildly affected father.
- **Caveat:** 85% sensitivity means a negative episignature does not exclude the diagnosis; and one individual in Dingemans' series showed an unexpected possible gain-of-function pattern.

Other omics (RNA-seq, proteomics, metabolomics, liquid biopsy) have **no established diagnostic role**. A patient-derived whole-transcriptome study exists (PMC7710346) but is research-grade.

### 10.4 Clinical Tests, Biomarkers, and Imaging

- **Laboratory tests:** No specific biochemical abnormality. Hyperbilirubinemia was noted in 6/53 (11%) — unexplained and not a diagnostic marker. There is no enzyme assay or metabolite marker.
- **Biomarkers:** The **DNA methylation episignature is the only validated biomarker.** OFC and height z-scores function as clinical (not molecular) biomarkers of the overgrowth phenotype.
- **Anthropometry:** Serial OFC and height, plotted on standard curves, are the core longitudinal measurements. GeneReviews surveillance: *"Measurement of growth parameters including head circumference at each visit."*
- **Imaging:** Brain MRI is **not diagnostic** but is indicated when there are neurologic signs — to detect **Chiari I malformation** (3 reported individuals; potentially surgical) and ventriculomegaly (`HP:0002119`). GeneReviews advises assessing for "signs/symptoms of CSF obstruction" and considering "serial imaging for asymptomatic Chiari I malformation." No pathognomonic MRI signature is described in humans; the white-matter expansion documented in primates has not been systematically characterized in human carriers — **a notable imaging gap.**
- **Electrophysiology:** EEG when seizures are suspected (12–17% seizure rate); not a screening test. No characteristic EEG signature.
- **Functional tests:** Formal developmental/cognitive assessment, standardized autism diagnostic assessment (ADOS/ADI-R), and adaptive functioning (Vineland). Polysomnography where sleep disturbance is severe or apnea is suspected.
- **Biopsy/pathology:** **No role.** No tissue diagnosis; no characteristic histopathology.

### 10.5 Differential Diagnosis

GeneReviews lists overgrowth-with-ID conditions:

| Condition | Gene/mechanism | Discriminating features |
|---|---|---|
| **Sotos syndrome** | NSD1 | Characteristic facial gestalt (long face, frontal bossing, downslanting fissures — overlapping), advanced bone age, prior learning profile; distinct episignature |
| **Weaver syndrome** | EZH2 | Camptodactyly, hoarse cry, distinct facies; distinct episignature |
| **Tatton-Brown-Rahman syndrome** | DNMT3A | Overgrowth + ID; distinct episignature |
| **Beckwith-Wiedemann syndrome** | 11p15 imprinting | Asymmetric/lateralized overgrowth, omphalocele, macroglossia, hypoglycemia, **embryonal tumor risk** — very different natural history |
| **PTEN hamartoma tumor syndrome** | PTEN | Macrocephaly *disproportionate to height*, hamartomas, **defined cancer risk** — the most important not-to-miss alternative |
| **Fragile X syndrome** | FMR1 CGG expansion | Macroorchidism, characteristic behavior, X-linked inheritance |
| Malan, Luscan-Lumish, other overgrowth-ID syndromes | NFIX, SETD2, etc. | |

**Practical point:** several of these differentials (Sotos, Weaver, TBRS, BWS, and CHD8 itself) have **distinct DNA methylation episignatures**, so a single EpiSign array can discriminate among much of this differential simultaneously. This is a strong argument for episignature testing in the overgrowth-plus-ID phenotype, and is worth curating as a diagnostic strategy rather than merely listing differentials.

The CHD8-specific discriminators are: **generalized** (height *and* OFC) rather than disproportionate overgrowth; prominent **GI dysmotility**; prominent **sleep disturbance**; and the specific facial gestalt (prominent supraorbital ridge, pointed chin).

### 10.6 Screening

- **Newborn screening:** Not performed and not appropriate (no presymptomatic intervention alters outcome).
- **Carrier screening:** Not applicable (de novo-predominant AD).
- **Cascade testing:** **Indicated.** Because 10–15% of cases are inherited, and because mildly affected parents exist (PMID:41407309, PMID:38441608), parental testing after a proband diagnosis is essential — it changes recurrence risk from 1% to 50% and may diagnose an undiagnosed parent.
- **Prenatal/PGT:** Available where a familial variant is known (§13).

---

## 11. Outcome / Prognosis

### 11.1 Survival and Mortality

**No excess mortality has been reported.** There is no life-expectancy study, no survival curve, and no disease-specific mortality figure — and this is because the condition is not known to be life-limiting, not because the data are merely missing. The strongest available evidence is indirect: the Dingemans cohort included individuals up to **57 years of age** (PMID:36182950), and Sorrentino reported a 53-year-old (PMID:38441608).

**Curate as:** normal or near-normal life expectancy, inferred from documented survival into the sixth decade; no mortality data available. Do not assert a survival rate.

### 11.2 Morbidity and Function

The burden is **developmental and behavioral, lifelong, and non-progressive** for the core phenotype:
- **Cognitive:** ID in 68–80%; mild 48% / moderate 24% / severe 28%. Most function in the mild-to-moderate range.
- **Adaptive:** Comparatively favorable. Beighley 2020 (PMID:31526516) found CHD8 carriers had "less severe adaptive deficits in communication skills, similar functional language, more social motivation challenges in those with ASD, larger head circumference, higher weight, and lower seizure prevalence relative to the other gene group." **Preserved functional language and lower seizure burden are prognostically favorable** relative to comparator ASD-gene groups — a genuinely useful counseling point.
- **Psychiatric:** Anxiety approaching clinical thresholds and **worsening with age** (CBCL anxiety T = 64.6; depression T = 66.4). This is the domain most likely to drive adult morbidity.
- **Motor:** Usually mild; the rare dystonic subgroup is the exception and can be severely disabling.
- **GI:** Chronic constipation/dysmotility in ~half to two-thirds; a persistent, under-treated source of morbidity plausibly driving self-injury (PMID:33175317).
- **Sleep:** 67% — a chronic burden on patient and family.

**No CHD8-specific QoL instrument data exist** (no EQ-5D, SF-36, PROMIS). This is a real gap and a reasonable `KNOWLEDGE_GAP` discussion entry.

### 11.3 Disease Course and Complications

- Static encephalopathy with age-dependent emergence of features (§8).
- Complications: seizures (12–17%), Chiari I with possible CSF obstruction (rare, potentially surgical), progressive dystonia (rare), obesity (34%), chronic constipation, psychiatric decompensation in adolescence/adulthood.
- **Recovery potential:** No recovery from the core neurodevelopmental phenotype. Developmental therapies improve function without altering the underlying condition. The reversibility findings (§8.3) are preclinical.

### 11.4 The Neoplasia Question — Handle With Care

Dingemans reported **neoplasia in 6/54 (11%)**. This figure should **not** be curated as an established cancer risk, for several reasons: the tumor types are not specified in the available data; there is no comparison to population baseline; "neoplasia" as an HPO-coded term in a retrospective aggregation may include benign lesions; and GeneReviews — which would be expected to flag a tumor risk — does **not** recommend tumor surveillance. Meanwhile the *somatic* CHD8-cancer literature (§4.6) concerns sporadic MSI-H gastric/colorectal tumors, a mechanistically separate phenomenon that must not be used to infer germline risk.

**Recommended curation:** record the 11% observation as a finding with `HP:0002664`, explicitly annotated as **not established as an excess risk**, and open a `KNOWLEDGE_GAP` discussion. Do not add tumor surveillance to management. Note the contrast with PTEN and Beckwith-Wiedemann in the differential (§10.5) — both of which *do* carry defined tumor risk, which is exactly why conflating them here would be harmful.

### 11.5 Prognostic Factors

- **ID severity** — the dominant determinant of long-term functional outcome.
- **Functional language** — Beighley 2020 indicates relatively preserved communication; early language delay predicts broader behavioral difficulty **specifically in the CHD8 group** (J Neurodev Disord 2024).
- **Age** — anxiety worsens with age; independent of baseline severity.
- **Variant type** — missense associated with lower De Vries scores (p=0.046), with the caveats in §9.3.
- **Genetic background** — a demonstrated modifier in mouse; unmeasurable clinically at present, but it is the best current explanation for why sibling-like genotypes give unlike phenotypes.
- **No prognostic molecular biomarker exists.**

---

## 12. Treatment

### 12.1 Overall Strategy

GeneReviews is unambiguous:
> "There is no cure for CHD8-NDD. Supportive care to improve quality of life, maximize function, and reduce complications is recommended."

Management is **symptom-directed and multidisciplinary**. There is no disease-modifying therapy, no targeted therapy, no approved drug for the condition itself, and no pharmacogenomic guidance specific to CHD8.

### 12.2 Symptom-Directed Management

| Domain | Intervention | NCIT (verified) | CHEBI / agent (verified) | Modality |
|---|---|---|---|---|
| DD/ID | Early intervention, IEP, developmental therapies | `NCIT:C15747` (supportive care) | — | `BEHAVIORAL` |
| Motor delay/hypotonia | Physical therapy | `NCIT:C15302` | — | `BEHAVIORAL` |
| Speech delay | Speech therapy | `NCIT:C159273` | — | `BEHAVIORAL` |
| ADL/fine motor | Occupational therapy | `NCIT:C121351` | — | `BEHAVIORAL` |
| ASD behaviors | Behavioral intervention | `NCIT:C181743` | — | `BEHAVIORAL` |
| **Sleep disturbance** | "behavioral and/or pharmacologic treatment" | `NCIT:C15986` | melatonin `CHEBI:16796` | `SMALL_MOLECULE` / `BEHAVIORAL` |
| Anxiety | Behavioral + pharmacotherapy | `NCIT:C15986` | — | `SMALL_MOLECULE` |
| ADHD | Stimulant pharmacotherapy | `NCIT:C15986` | methylphenidate `CHEBI:6887` | `SMALL_MOLECULE` |
| Aggression/irritability | Atypical antipsychotic | `NCIT:C15986` | risperidone `CHEBI:8871`, aripiprazole `CHEBI:31236` | `SMALL_MOLECULE` |
| **Seizures** | "standardized anti-seizure medications" | `NCIT:C15986` | — | `SMALL_MOLECULE` |
| **Constipation** | Laxatives, dietary fiber, hydration | `NCIT:C15986` / `NCIT:C15447` | — | `SMALL_MOLECULE` / `BEHAVIORAL` |
| **Dystonia** | Trihexyphenidyl / levodopa trial / baclofen / botulinum toxin / tizanidine | `NCIT:C15986` | trihexyphenidyl `CHEBI:9720`, levodopa `CHEBI:15765`, baclofen `CHEBI:2972` | `SMALL_MOLECULE` |
| **Dystonia (refractory)** | **Deep brain stimulation** | `NCIT:C15329` (surgical procedure) | — | `DEVICE` |
| **Chiari I (symptomatic)** | Surgical decompression | `NCIT:C15329` | — | `SURGERY` |
| Family | Genetic counseling | `NCIT:C15240` | — | `BEHAVIORAL` |

**Important note on drug terms:** melatonin, methylphenidate, risperidone, aripiprazole, trihexyphenidyl, levodopa, and baclofen are listed here as the pharmacologic classes GeneReviews and the dystonia literature indicate; **CHEBI IDs are verified as valid enum members but the specific agents beyond levodopa/tizanidine/botulinum (which are explicitly named in the dystonia papers) are inferred from standard practice, not from CHD8-specific evidence.** Do not curate an inferred agent as if the source named it. Tizanidine and botulinum toxin *are* explicitly documented (PMID:38441608, Patient 1); levodopa is documented as ineffective in one patient and partially effective in another.

**Deep brain stimulation is the single best-evidenced targeted intervention in this disorder.** GeneReviews: *"2 affected persons with childhood-onset progressive dystonia... experienced improvement with deep brain stimulation."* Corroborated: "deep brain stimulation led to clinical improvement in both cases of children with CHD8-related progressive dystonia" (PMID:34415117). Two cases is a small evidence base, but for a rare phenotype within a rare disorder it is meaningful and actionable.

### 12.3 Experimental and Advanced Therapeutics

**None in human clinical trials.** No gene therapy, ASO, siRNA, mRNA, cell therapy, targeted therapy, or immunotherapy exists for CHD8-NDD. There is no interventional NCT for this condition.

Three preclinical directions are worth recording as `EMERGING` mechanistic hypotheses:

1. **Enhancer-targeted CRISPR-activation (CRISPR-A).** In hPSC-derived excitatory neurons and cerebral forebrain organoids, researchers mapped *CHD8* enhancers and used CRISPR-A to correct haploinsufficiency: "core phenotypes, including over-proliferation in CHD8+/−, are rescued by CRISPR-A for several months post-treatment," and "the overabundant progenitor phenotype caused by CHD8 haploinsufficiency is rescued by enhancer-targeted CRISPR-A" (bioRxiv 2024.03.13.584921). Enhancer targeting rather than CDS overexpression is the deliberate design choice — it permits "more nuanced control of gene expression and avoid[s] cell toxicity effects from gene overexpression," which matters given that *CHD8* **duplication is itself pathogenic** (§4.3). This is a well-reasoned therapeutic strategy for a dosage-sensitive gene. Preprint; `evidence_source: IN_VITRO`.
2. **Developmental-window Chd8 restoration.** "Restoration of Chd8 expression in ventral progenitor cells ameliorates both the behavioral phenotypes and aberrant ventral differentiation in Chd8 mutant mice" (Nat Commun 2026). `evidence_source: MODEL_ORGANISM`.
3. **Behavioral sleep-restriction therapy.** Fly sleep architecture defects of developmental origin were "reversed in adulthood by a behavioral regime resembling human sleep restriction therapy" (PMID:34088660). This is the most immediately translatable of the three — it proposes an existing, low-risk human behavioral therapy with a specific mechanistic rationale. `evidence_source: MODEL_ORGANISM`.

**Observational research:** Simons Searchlight (**NCT01238250**) — recruiting, observational, online/international registry that includes *CHD8*. This is the appropriate `clinical_trials:` entry for the KB (with `evidence: reference: clinicaltrials:NCT01238250` after `just fetch-reference NCT01238250`).

### 12.4 Surveillance

GeneReviews Table 6 recommendations, all appropriate for KB capture:
- Growth parameters **including head circumference at every visit**
- Developmental progress and educational needs
- Screen for **anxiety, psychosis, ADHD, aggressive or self-injurious behavior**
- "Assess for new manifestations such as seizures; changes in tone/movement disorders; and signs/symptoms of CSF obstruction"
- Screen for **sleep disturbance at each visit**
- Monitor constipation and feeding issues
- Consider serial imaging for asymptomatic Chiari I malformation

Two of these are notable for being disorder-specific rather than generic: surveillance for **new movement disorder** (reflecting the emerging dystonia spectrum) and for **psychosis** (reflecting adult psychiatric risk). Tumor surveillance is **not** recommended — see §11.4.

### 12.5 Pharmacogenomics and Treatment Outcomes

- **Pharmacogenomics:** No CHD8-specific PGx. No PharmGKB/CPIC guidance. Standard CYP-based PGx for psychotropics applies as it would for any patient.
- **Response rates:** No CHD8-specific efficacy data for any intervention. All pharmacotherapy is extrapolated from general ASD/ID/ADHD/epilepsy practice.
- **Adverse events:** No CHD8-specific signals. Note the general caution around weight gain with atypical antipsychotics given the 34% baseline overweight rate — a sensible, if inferential, clinical point.

---

## 13. Prevention

### 13.1 Primary Prevention

**Not possible.** CHD8-NDD arises from de novo germline mutation; there is no modifiable exposure, no vaccine, and no risk-factor intervention. Any content asserting otherwise would be wrong.

The only true primary-prevention avenue is reproductive:
- **Preimplantation genetic testing (PGT-M)** — available when a familial pathogenic variant is known (i.e., the 10–15% inherited cases, or a couple with a prior affected child accepting the ~1% germline-mosaicism risk).
- **Prenatal diagnosis** — available for known familial variants.

### 13.2 Secondary Prevention (Early Detection)

- **No population screening program exists or is warranted.**
- **Targeted diagnostic testing is the practical form of early detection:** genome/exome sequencing in any child with DD/ID/ASD, and particularly with **macrocephaly or generalized overgrowth**, where yield rises to ~2%.
- **Cascade testing of parents and at-risk relatives** — the most concrete secondary-prevention action, given that 10–15% are inherited and mildly affected carriers exist undiagnosed.
- **Early developmental identification** enables early intervention, which improves function without altering the disorder.

### 13.3 Tertiary Prevention (Preventing Complications)

This is where prevention genuinely applies, and it maps directly onto the surveillance schedule:
- Aggressive **constipation management** to prevent impaction, chronic pain, and pain-driven self-injury (PMID:33175317).
- **Sleep intervention** to reduce behavioral dysregulation and caregiver burden.
- **Anxiety screening and early treatment**, given documented age-related worsening.
- **Neurologic surveillance** for new seizures, movement disorder, or CSF-obstruction signs → timely EEG/MRI.
- **Weight management** given 34% overweight, compounded by psychotropic-associated weight gain.
- **Early referral for DBS evaluation** in progressive dystonia.

### 13.4 Immunization

Standard childhood immunization per routine schedule. **No disease-specific vaccine strategy, no contraindication, and no altered schedule.** Not applicable as a disease-specific prevention measure.

### 13.5 Genetic Counseling

Essential. Content: autosomal dominant inheritance; 85–90% de novo; recurrence 50% if a parent carries the variant, ~1% if de novo (germline mosaicism); parental testing strongly recommended; PGT-M and prenatal diagnosis available for known familial variants; **counsel on marked variable expressivity** — an identified relative carrying the same variant may be substantially more or less affected, as directly demonstrated by the paternal-transmission case (PMID:41407309) and the cognitively-intact dystonic carriers (PMID:38441608). NCIT: `NCIT:C15240`.

### 13.6 Public Health and Environmental Interventions

**Not applicable.** No sanitation, vector-control, health-education, or environmental-remediation measure is relevant to a de novo Mendelian disorder.

### 13.7 Prophylaxis

No prophylactic medication or procedure. Bowel-regimen prophylaxis for constipation is the closest analogue and is better classified as tertiary prevention.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and Orthologs

| Species | NCBI Taxon | Gene | Note |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | CHD8 (57680) | |
| *Mus musculus* | NCBITaxon:10090 | Chd8 | Principal model |
| *Macaca fascicularis* (cynomolgus monkey) | NCBITaxon:9541 | CHD8 | CRISPR model, PMID:36878905 |
| *Danio rerio* | NCBITaxon:7955 | chd8 | **Sole ortholog** in zebrafish |
| *Drosophila melanogaster* | NCBITaxon:7227 | *kismet* (kis) | **Sole CHD8/CHD7 ortholog** — models both genes at once |
| *Rattus norvegicus* | NCBITaxon:10116 | Chd8 | Limited use |

Verify all NCBI Taxon IDs against `cache/enums/organismterm_*.csv` before curating.

### 14.2 Natural Disease in Other Species

**No naturally occurring CHD8-related disease has been reported in any non-human species.** There is no OMIA entry, no canine/feline/equine breed-associated CHD8 disorder, and no wildlife disease. **No VBO breed identifier is applicable.** All animal disease models are engineered.

This is an honest and complete answer for this section — CHD8-NDD is a laboratory-modeled, not a naturally-occurring-in-animals, condition.

### 14.3 Comparative Biology and Evolutionary Conservation

CHD8 is deeply conserved across bilaterians, with the *Drosophila* ortholog *kismet* representing the ancestral CHD7/CHD8 gene prior to the vertebrate duplication. Conservation extends to function, not just sequence: **sleep-maintenance disruption is conserved from fly to human** (PMID:34088660), which is a striking degree of functional conservation for a complex behavioral phenotype and is what licenses fly work as a model here.

The most important comparative finding is a **divergence**, not a conservation: the primate work (PMID:36878905) indicates that **gliogenesis is the dominant driver of CHD8-related brain enlargement in primates**, whereas rodent studies "showed inconsistent findings about the mechanisms for CHD8 deficiency-mediated autism symptoms and macrocephaly." Given that primate brains have a far greater glial complement and a protracted gliogenic period, this is a plausible species difference rather than a technical discrepancy — and it is a caution against over-weighting rodent mechanism data for the human macrocephaly phenotype. This is a textbook candidate for a `HUMAN_MODEL_MISMATCH` discussion entry (per CLAUDE.md: evidence exists in a model, but translational validity is the open question) rather than a generic `KNOWLEDGE_GAP`.

### 14.4 Transmission

**Not applicable.** No zoonotic potential, no cross-species transmission — this is a germline genetic disorder.

---

## 15. Model Organisms

### 15.1 Mouse — Multiple Independent Lines, Convergent Core, Divergent Behavior

Mouse is the workhorse. Homozygous *Chd8* null is **embryonic lethal** (via p53-mediated apoptosis; PMID:19151705), so heterozygotes are used.

**Principal published lines:**

| Study | PMID | Key finding |
|---|---|---|
| Katayama 2016, *Nature* | 27602517 | Autistic-like behaviors; REST target derepression; delayed neuronal development; macrocephaly, craniofacial abnormalities |
| Gompers 2017, *Nat Neurosci* | 28671691 | Germline haploinsufficiency alters brain development; developmental RNA-splicing phenotype |
| Platt 2017, *Cell Rep* | 28402856 | Autistic-like behaviors + **impaired striatal circuits** |
| Durak 2016, *Nat Neurosci* | 27694995 | Cortical neurogenesis via cell cycle + Wnt; in utero knockdown reduces progenitor proliferation |
| Suetterlin 2018, *Cereb Cortex* | — | Brain overgrowth + **functional over-connectivity** |
| Kawamura 2020, *Mol Autism* | 33023670 | Early brain development + later-life proteostasis impairment |
| Kawamura 2020, *Mol Brain* | 33228730 | **Oligodendrocyte-specific** mutation alters microstructure/connectivity |
| Tabbaa 2023, *Neuron* | 36738737 | **>1,000 mice, 33 strains** — genetic background phenocopies human heterogeneity |
| Mol Psychiatry 2026 | DOI 10.1038/s41380-026-03646-9 | **Viable homozygous** (CHD8-Asn2373LysfsX2, hybrid background); dose-dependent severity; sex-effect reversal |
| 2025 | 40501938 | Persistent cortical excitatory neuron dysregulation in **adults** |

**Model types available:** germline heterozygous knockout (multiple alleles, several recapitulating specific human variants such as S62X and N2373Kfs*2), conditional/cell-type-specific (oligodendrocyte, microglia, ventral progenitor), in utero knockdown, and duplication models.

### 15.2 Phenotype Recapitulation and Limitations

**Robustly recapitulated across every line — the core convergent phenotype:**
> "Megalencephaly, subtle but wide-spread transcriptional changes and behavioral anomalies were found in all the Chd8+/− mouse lines."

Also: craniofacial abnormalities; cognitive deficits.

**Not reliably recapitulated:**
- **Behavioral divergence is the central limitation.** "There have been conflicting reports of previous lines of Chd8 mice in their spontaneous motor activity in the open field, with some groups reporting hypoactivity (Jung et al., Platt et al., Suetterlin et al.) whereas others reported no changes in activity (Gompers et al., Katayama et al.)."
- Some lines "display signatures of human CHD8 haploinsufficiency, such as macrocephaly and cognitive deficits, but not ASD-related behavioral impairments, confirming difficulties in modeling autism spectrum disorders in mice."
- **Mechanism of macrocephaly may not translate:** "increased cortical volume without increased neuron number" in mouse, versus primate glial expansion.
- **Transcriptional consequences are model-specific even where binding is conserved:** "Common CHD8 Genomic Targets Contrast With Model-Specific Transcriptional Impacts of CHD8 Haploinsufficiency" (PMC6339895).
- Human features not modeled: tall stature/puberty-timed overgrowth, the specific facial gestalt, GI constipation in mouse (better in zebrafish), anxiety trajectory.

Tabbaa 2023 (PMID:36738737) reframes the divergence: it is not noise but **genetic-background–dependent biology**, and single-inbred-strain designs "fail to capture the genetic diversity and symptom heterogeneity common clinically." This is the most important methodological statement in the CHD8 model literature and should inform how any mouse-derived evidence item is weighted.

### 15.3 Non-Human Primate

Cynomolgus monkey, CRISPR/Cas9 embryo editing (Li et al., Cell Discov 2023; PMID:36878905). Recapitulates **macrocephaly** with a mechanistically distinct explanation: increased gliogenesis, enlarged white matter near the lateral ventricle, brain weight 57.8 g vs 45 ± 2.8 g (**~28% larger**). Supported by organotypic slice knockdown. Uniquely valuable precisely because it resolves a question rodents could not. Limitations: very small n, cost, ethical constraints, limited behavioral phenotyping, mosaic founders.

### 15.4 Zebrafish

*chd8* is the sole ortholog. Two model types: transient morpholino knockdown (Bernier 2014, PMID:24998929) and stable constitutive mutants (Life Sci Alliance 2023, PMC9664244).

Recapitulates: **increased head size** and — uniquely — the **GI phenotype**: reduced enteric neurons, perturbed GI motility, reduced vagal neural crest emigration with altered migration, and decreased serotonin-producing enterochromaffin cells and NC-derived serotonergic neurons. **Zebrafish is the best model for the CHD8 gut phenotype** and is the only system in which the human GI complaint has a demonstrated developmental mechanism. Limitations: no mammalian cortex, limited behavioral relevance to ASD.

### 15.5 Drosophila

*kismet* — sole CHD8/CHD7 ortholog. Coll-Tané 2021 (PMID:34088660) recapitulated **disturbed sleep maintenance** and localized the requirement to **subperineurial glia forming the blood-brain barrier**, with high developmental serotonin as the mediator, and demonstrated adult behavioral reversibility. Also: "Kismet/CHD7/CHD8 affects gut biomechanics, the gut microbiome, and gut-brain axis in *Drosophila melanogaster*." Limitation: *kismet* models CHD7 and CHD8 jointly, so gene-specific attribution requires care.

### 15.6 Cellular and In Vitro Models

- **Human iPSC-derived NPCs:** Sugathan 2014 (PMID:25294932) — 1,756 DEGs, 64.9% up-regulated.
- **CRISPR/Cas9 isogenic heterozygous KO iPSC lines:** PMID:26491539.
- **Cerebral/forebrain organoids:** Wang 2017 (CHD8+/− vs isogenic control; DLX/GABAergic dysregulation; WNT/β-catenin; DEG overlap with idiopathic ASD) and Villa 2022 (PMID:35385734) — the cell-type-resolved E/I trajectory work. **Organoids are currently the best human-relevant system** for the neural progenitor phenotype and are the platform on which CRISPR-A rescue was demonstrated.
- **hPSC-derived excitatory neurons:** CRISPR-A rescue platform.
- **Mouse ESC neural differentiation:** used for functional missense-variant testing (PMID:38438524) — the model system that established that not all patient missense alleles are causal.

### 15.7 Model Resources

- **MGI** (Mouse Genome Informatics) — *Chd8* alleles and phenotypes; **IMSR** / **MMRRC** / **KOMP-IMPC** for strain availability
- **ZFIN** — *chd8* zebrafish alleles
- **FlyBase** — *kismet* alleles
- **Alliance of Genome Resources** — cross-species ortholog/phenotype integration
- **SFARI Gene** — CHD8 human gene + animal model catalogue (gene.sfari.org)
- **Simons Searchlight** — human registry (NCT01238250)
- **Cellosaurus / ATCC** — iPSC lines

---

## Appendix A — Verified PMID Reference List

All PMIDs below were confirmed via NCBI E-utilities `esummary` (title, journal, year, first author matched).

**Human clinical / cohort**
| PMID | Citation |
|---|---|
| 24998929 | Bernier R et al. Disruptive CHD8 mutations define a subtype of autism early in development. *Cell* 2014;158(2):263-276 |
| 36302072 | CHD8-Related Neurodevelopmental Disorder with Overgrowth. *GeneReviews* 2022 |
| 36182950 | Dingemans AJM et al. The phenotypic spectrum and genotype-phenotype correlations in 106 patients with variants in major autism gene CHD8. *Transl Psychiatry* 2022 |
| 31721432 | Ostrowski PJ et al. The CHD8 overgrowth syndrome. *Am J Med Genet C* 2019;181(4):557-564 |
| 31001818 | Douzgou S et al. The clinical presentation caused by truncating CHD8 variants. *Clin Genet* 2019 |
| 31526516 | Beighley JS et al. Clinical Phenotypes of Carriers of Mutations in CHD8 or Its Conserved Target Genes. *Biol Psychiatry* 2020;87:123-131 |
| 31823155 | Smol T et al. Neurodevelopmental phenotype associated with CHD8-SUPT16H duplication. *Neurogenetics* 2020 |
| 38441608 | Sorrentino U et al. CHD8-related disorders redefined: an expanding spectrum of dystonic phenotypes. *J Neurol* 2024 |
| 34415117 | Doummar D et al. Childhood-onset progressive dystonia associated with pathogenic truncating variants in CHD8. *Ann Clin Transl Neurol* 2021 |
| 41407309 | Furuta Y et al. Phenotypic Variability and Paternal Inheritance of a CHD8 Variant... *Mol Genet Genomic Med* 2025 |
| 33175317 | Kurtz-Nelson E et al. Brief Report: Associations Between Self-injurious Behaviors and Abdominal Pain... *J Autism Dev Disord* 2021 |
| 36731504 | A Korean boy with a CHD8 mutation who presented with overgrowth, intellectual disability, and autism |

**Mechanism — molecular / in vitro**
| PMID | Citation |
|---|---|
| 18378692 | Thompson BA et al. CHD8 is an ATP-dependent chromatin remodeling factor that regulates beta-catenin target genes. *Mol Cell Biol* 2008 |
| 19151705 | Nishiyama M et al. CHD8 suppresses p53-mediated apoptosis through histone H1 recruitment during early embryogenesis. *Nat Cell Biol* 2009 |
| 19255092 | Rodríguez-Paredes M et al. The chromatin remodeling factor CHD8 interacts with elongating RNA polymerase II and controls expression of the cyclin E2 gene. *Nucleic Acids Res* 2009 |
| 20085832 | Regulation of HOXA2 gene expression by the ATP-dependent chromatin remodeling enzyme CHD8. *FEBS Lett* 2010 |
| 25294932 | Sugathan A et al. CHD8 regulates neurodevelopmental pathways associated with autism spectrum disorder in neural progenitors. *PNAS* 2014 |
| 25752243 | Cotney J et al. The autism-associated chromatin modifier CHD8 regulates other autism risk genes during human neurodevelopment. *Nat Commun* 2015 |
| 25989142 | Wilkinson B et al. ...CHD8 regulates noncoding RNAs and autism-related genes. *Transl Psychiatry* 2015 |
| 26491539 | CRISPR/Cas9-mediated heterozygous knockout of the autism gene CHD8... *Mol Autism* 2015 |
| 26626481 | NSD3-Short Is an Adaptor Protein that Couples BRD4 to the CHD8 Chromatin Remodeler. *Mol Cell* 2015 |
| 29768199 | The Autism-Related Protein CHD8 Cooperates with C/EBPβ to Regulate Adipogenesis. *Cell Rep* 2018 |
| 35385734 | Villa CE et al. CHD8 haploinsufficiency links autism to transient alterations in excitatory and inhibitory trajectories. *Cell Rep* 2022 |
| 38438524 | Shiraishi Y et al. The complex etiology of autism spectrum disorder due to missense mutations of CHD8. *Mol Psychiatry* 2024;29:2145-2160 |

**Model organisms**
| PMID | Citation |
|---|---|
| 27602517 | Katayama Y et al. CHD8 haploinsufficiency results in autistic-like phenotypes in mice. *Nature* 2016;537:675-679 |
| 27694995 | Durak O et al. Chd8 mediates cortical neurogenesis via transcriptional regulation of cell cycle and Wnt signaling. *Nat Neurosci* 2016 |
| 28402856 | Platt RJ et al. Chd8 Mutation Leads to Autistic-like Behaviors and Impaired Striatal Circuits. *Cell Rep* 2017 |
| 28671691 | Gompers AL et al. Germline Chd8 haploinsufficiency alters brain development in mouse. *Nat Neurosci* 2017 |
| 30574290 | Autism-associated CHD8 deficiency impairs axon development and migration of cortical neurons. *Mol Autism* 2018 |
| 33023670 | Chd8 haploinsufficiency impairs early brain development and protein homeostasis later in life. *Mol Autism* 2020 |
| 33228730 | Chd8 mutation in oligodendrocytes alters microstructure and functional connectivity in the mouse brain. *Mol Brain* 2020 |
| 34088660 | Coll-Tané M et al. The CHD8/CHD7/Kismet family links blood-brain barrier glia and serotonin to ASD-associated sleep defects. *Sci Adv* 2021 |
| 36127134 | Conserved and Distinct Functions of the Autism-Related Chromatin Remodeler CHD8 in Embryonic and Adult Forebrain Neurogenesis. *J Neurosci* 2022 |
| 36738737 | Tabbaa M, Knoll A, Levitt P. Mouse population genetics phenocopies heterogeneity of human Chd8 haploinsufficiency. *Neuron* 2023;111:539-556 |
| 36878905 | Li Z et al. CHD8 mutations increase gliogenesis to enlarge brain size in the nonhuman primate. *Cell Discov* 2023 |
| 40501938 | Persistent cortical excitatory neuron dysregulation in adult Chd8 haploinsufficient mice. 2025 |

**Cancer (somatic — adjacent, not this disorder)**
| PMID | Citation |
|---|---|
| 21447119 | Kim MS et al. Genetic and expressional alterations of CHD genes in gastric and colorectal cancers. *Histopathology* 2011 |
| 23835524 | Sawada G et al. CHD8 is an independent prognostic indicator that regulates Wnt/β-catenin signaling and the cell cycle in gastric cancer. *Oncol Rep* 2013 |

**Reviews**
| PMID | Citation |
|---|---|
| 26733790 | Mutations and Modeling of the Chromatin Remodeler CHD8 Define an Emerging Autism Etiology. *Front Neurosci* 2015 |
| 34440307 | The Mechanisms of CHD8 in Neurodevelopment and Autism Spectrum Disorders. *Genes (Basel)* 2021 |
| — | Neurodevelopmental functions of CHD8: new insights and questions. *Biochem Soc Trans* 2024;52(1):15 |

**Not-yet-PMID-verified (DOI only — verify before citing):** Nat Commun 2026 midfetal ventral neurogenesis (10.1038/s41467-026-73416-2); Mol Psychiatry 2026 homozygous CHD8 (10.1038/s41380-026-03646-9); Nat Commun 2025 Chd8 duplication (10.1038/s41467-025-59853-5); Transl Psychiatry 2025 adult microglial knockdown (10.1038/s41398-025-03468-3); AJHG 2023 chromatin compaction (10.1016/j.ajhg.2023.10.009); J Neurodev Disord 2024;16:15 (PMC11017562); Clin Genet 2026 Lan et al. (10.1111/cge.70117); bioRxiv 2024.03.13.584921 (CRISPR-A, **preprint**).

---

## Appendix B — Verified Ontology Term IDs

All IDs below were confirmed present in the corresponding `cache/enums/*.csv` dynamic-enum expansion. **Labels still require `just validate-terms` confirmation.**

**HPO (phenotype):** HP:0000098, HP:0000256, HP:0000276, HP:0000307, HP:0000316, HP:0000322, HP:0000336, HP:0000337, HP:0000358, HP:0000431, HP:0000486, HP:0000494, HP:0000708, HP:0000717, HP:0000718, HP:0000733, HP:0000739, HP:0000750, HP:0001249, HP:0001250, HP:0001252, HP:0001257, HP:0001263, HP:0001270, HP:0001319, HP:0001332, HP:0001337, HP:0001513, HP:0001520, HP:0001763, HP:0002007, HP:0002014, HP:0002019, HP:0002119, HP:0002308, HP:0002360, HP:0002376, HP:0002650, HP:0002664, HP:0002904, HP:0005616, HP:0007018, HP:0012758, HP:0100716, HP:0100785

**GO biological process:** GO:0000122, GO:0006281, GO:0006338, GO:0006355, GO:0006357, GO:0007399, GO:0007416, GO:0008284, GO:0010467, GO:0014033, GO:0016055, GO:0016477, GO:0021895, GO:0022008, GO:0031175, GO:0042063, GO:0045893, GO:0048484, GO:0051726, GO:0060070, GO:0090090

**GO molecular function:** GO:0003682, GO:0016887

**GO cellular component:** GO:0000785, GO:0005634, GO:0005654

**Cell Ontology:** CL:0000047, CL:0000125, CL:0000127, CL:0000128, CL:0000129, CL:0000333, CL:0000540, CL:0000617, CL:0000679, CL:0002319, CL:0007011

**UBERON:** UBERON:0000160, UBERON:0000948, UBERON:0000955, UBERON:0000956, UBERON:0001017, UBERON:0001049, UBERON:0001890, UBERON:0002005, UBERON:0002240, UBERON:0002316, UBERON:0002435, UBERON:0005409

**NCIT (treatment action):** NCIT:C121351, NCIT:C15240, NCIT:C15302, NCIT:C15313, NCIT:C15329, NCIT:C15447, NCIT:C15747, NCIT:C159273, NCIT:C15986, NCIT:C16186, NCIT:C181743, NCIT:C49236

**CHEBI:** CHEBI:2972, CHEBI:6801, CHEBI:6887, CHEBI:8871, CHEBI:9720, CHEBI:15355, CHEBI:15765, CHEBI:16796, CHEBI:28790, CHEBI:31236, CHEBI:31859, CHEBI:64317

**MONDO:** MONDO:0014017 · **HGNC:** hgnc:20153

**Rejected — failed enum membership check, do NOT use:** GO:0016568, GO:0021846, GO:0048699, GO:0007050, GO:0043524, GO:0072091, GO:0030111, GO:0004386, GO:0140658, GO:0008094, GO:0005524, GO:0003713, GO:0008013, GO:0003677, GO:0005694, GO:0005730, CL:0000031, UBERON:0000033, UBERON:0002028, UBERON:0001893, UBERON:0004734, CHEBI:6710, CHEBI:38571, CHEBI:46793, CHEBI:63661, CHEBI:4880, NCIT:C94358, NCIT:C15632-adjacent (untested). `HP:0011024` and `HP:0000006` were not tested and must be checked before use.

---

## Appendix C — Recommended Next Steps for Curation

1. **Re-fetch and validate every snippet.** `just fetch-reference PMID:<id>` for each of the ~40 PMIDs above, then `just validate-references`. No snippet in this report is validated.
2. **Verify all labels** with `just validate-terms kb/disorders/CHD8-Related_Neurodevelopmental_Disorder_with_Overgrowth.yaml`.
3. **Confirm the Orphanet code** (ORPHA:642675) before entering it; the Orphanet site blocked direct fetch here.
4. **Build structured-source cache entries:** `just clingen-dosage-rebuild --id CGDS:HGNC_20153` (haploinsufficiency score 3) and check `just clingen-list` for a CHD8-IDDAM `CGGV:` validity assertion. Both give snippet-validatable evidence rows for the core mechanism claim.
5. **Consider module conformance.** No existing `kb/modules/` module is an obvious fit — CHD8-NDD is not fibrotic, senescent, oncologic, or lysosomal. If a `neurodevelopmental_chromatinopathy` module is ever created (CHD8, CHD2, ADNP, DYRK1A, KMT2D, SETD5, ARID1B all share the chromatin-regulator → progenitor-dynamics → NDD chain), this entry is a strong flagship conformer. Note the repo already has CHD2- and SETD5-related entries, so the grouping case is real.
6. **Candidate `Grouping`:** a "Chromatin Remodeling Neurodevelopmental Disorders" or "Overgrowth-with-Intellectual-Disability Syndromes" grouping would give the §10.5 differential an auditable structure with `SHARED_MECHANISM` / `SHARED_PHENOTYPE` basis.
7. **Open discussion entries:** (a) `HUMAN_MODEL_MISMATCH` for the rodent-vs-primate macrocephaly mechanism divergence; (b) `KNOWLEDGE_GAP` for the unexplained 11% neoplasia observation; (c) `KNOWLEDGE_GAP` for the female-skewed dystonia subgroup; (d) `KNOWLEDGE_GAP` for absent QoL instrument data.
8. **Add a history record:** `just new-history --kind disorder --slug CHD8-Related_Neurodevelopmental_Disorder_with_Overgrowth --event UPDATE ...` per CLAUDE.md.

---

## Sources

- [CHD8-Related Neurodevelopmental Disorder with Overgrowth — GeneReviews (NBK585456)](https://www.ncbi.nlm.nih.gov/books/NBK585456/)
- [Disruptive CHD8 Mutations Define a Subtype of Autism Early in Development — Cell](https://www.cell.com/fulltext/S0092-8674(14)00749-1)
- [The phenotypic spectrum and genotype-phenotype correlations in 106 patients with variants in major autism gene CHD8 — PMC9526704](https://pmc.ncbi.nlm.nih.gov/articles/PMC9526704/)
- [The CHD8 overgrowth syndrome: a detailed evaluation in 27 patients — Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.c.31749)
- [CHD8-related disorders redefined: an expanding spectrum of dystonic phenotypes — PMC11055771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11055771/)
- [Shared and divergent mental health characteristics of ADNP-, CHD8- and DYRK1A-related conditions — PMC11017562](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11017562/)
- [Clinical Phenotypes of Carriers of Mutations in CHD8 or Its Conserved Target Genes — PubMed 31526516](https://pubmed.ncbi.nlm.nih.gov/31526516/)
- [CHD8 haploinsufficiency results in autistic-like phenotypes in mice — Nature](https://www.nature.com/articles/nature19357)
- [Germline Chd8 haploinsufficiency alters brain development in mouse — Nat Neurosci](https://www.nature.com/articles/nn.4592)
- [Mouse population genetics phenocopies heterogeneity of human Chd8 haploinsufficiency — Neuron](https://www.cell.com/neuron/fulltext/S0896-6273(23)00033-8)
- [CHD8 mutations increase gliogenesis to enlarge brain size in the nonhuman primate — Cell Discovery](https://www.nature.com/articles/s41421-023-00525-3)
- [CHD8 haploinsufficiency links autism to transient alterations in excitatory and inhibitory trajectories — Cell Reports](https://www.cell.com/cell-reports/fulltext/S2211-1247(22)00363-1)
- [CHD8 regulates neurodevelopmental pathways associated with ASD in neural progenitors — PNAS](https://www.pnas.org/doi/full/10.1073/pnas.1405266111)
- [The autism-associated chromatin modifier CHD8 regulates other autism risk genes — Nat Commun](https://www.nature.com/articles/ncomms7404)
- [CHD8 is an ATP-dependent chromatin remodeling factor that regulates beta-catenin target genes — PubMed 18378692](https://pubmed.ncbi.nlm.nih.gov/18378692/)
- [Chd8 mediates cortical neurogenesis via transcriptional regulation of cell cycle and Wnt signaling — PMC5386887](https://ncbi.nlm.nih.gov/pmc/articles/PMC5386887)
- [The complex etiology of autism spectrum disorder due to missense mutations of CHD8 — Mol Psychiatry](https://www.nature.com/articles/s41380-024-02491-y)
- [The CHD8/CHD7/Kismet family links blood-brain barrier glia and serotonin to ASD-associated sleep defects — Science Advances](https://www.science.org/doi/10.1126/sciadv.abe2626)
- [Loss of autism-candidate CHD8 perturbs neural crest development and intestinal homeostatic balance — PMC9664244](https://pmc.ncbi.nlm.nih.gov/articles/PMC9664244/)
- [Defective ventral neurogenesis due to midfetal Chd8 mutation drives autistic-like behavior in mice — Nat Commun](https://www.nature.com/articles/s41467-026-73416-2)
- [Homozygous CHD8 mutation intensifies ASD phenotypes and attenuates sex differences — Mol Psychiatry](https://www.nature.com/articles/s41380-026-03646-9)
- [Duplication of the autism-related gene Chd8 leads to behavioral hyperactivity — Nat Commun](https://www.nature.com/articles/s41467-025-59853-5)
- [Enhancer-targeted CRISPR-Activation Rescues Haploinsufficient Autism Susceptibility Genes — bioRxiv](https://www.biorxiv.org/content/10.1101/2024.03.13.584921v1.full)
- [Phenotypic Variability and Paternal Inheritance of a CHD8 Variant... — PMC12711360](https://pmc.ncbi.nlm.nih.gov/articles/PMC12711360/)
- [CHD8 curation results for Dosage Sensitivity — ClinGen](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:20153)
- [Neurodevelopmental functions of CHD8: new insights and questions — Biochem Soc Trans](https://portlandpress.com/biochemsoctrans/article/52/1/15/233993/Neurodevelopmental-functions-of-CHD8-new-insights)
- [Genetic and expressional alterations of CHD genes in gastric and colorectal cancers — PubMed 21447119](https://pubmed.ncbi.nlm.nih.gov/21447119/)
- [CHD8 is an independent prognostic indicator... in gastric cancer — PubMed 23835524](https://pubmed.ncbi.nlm.nih.gov/23835524/)
- [Simons Searchlight — CHD8](https://www.simonssearchlight.org/gene-guide/chd8/)
- [OMIM #615032 IDDAM](https://omim.org/entry/615032)
- [Intellectual developmental disorder with autism and macrocephaly — NIH GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3554373/)