---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:09.930562'
end_time: '2026-10-14T15:54:19.548640'
duration_seconds: 309.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sudden cardiac failure, infantile
  mondo_id: MONDO:0014973
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
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 26
  total_cost_usd: 2.5572564
  session_id: 52e9ef20-4bcb-4150-adc1-4f01ed940151
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 6
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sudden cardiac failure, infantile
- **MONDO ID:** MONDO:0014973 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sudden cardiac failure, infantile** covering all of the
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

I'm pulling the cached PPA2 abstracts now. Next I'll search for newer papers on models and survivors, then write the report.

Pulling full abstracts for the 2023–2026 case reports and the mitochondrial-fission paper, so I can quote them exactly.

Pulling key sentences from the cached full text of the 2021 cohort paper. After that I'll write the report.

# Research report: Sudden cardiac failure, infantile (SCFI; MONDO:0014973)

**Method.** Abstracts and full texts for the key papers were read from this repository's `references_cache/`: PMID:27523597 (full text), PMID:27523598, PMID:34400813 (full text), PMID:31705601, PMID:33028643 and PMID:33826954. Case reports from 2023–2026 were found through a PubMed search on PPA2 and read through NCBI E-utilities and the Europe PMC API.

**Two kinds of citation in this report:**
- **Exact quotes from cached files.** Quotes marked *(cached)* were copied from those files and can be used as snippets.
- **Quotes from summaries of web pages.** Quotes from uncached PMIDs came through a tool that summarises pages, so some are partial. Run `just fetch-reference` on each one and re-quote it from the cache before using it as a snippet.

**Ontology IDs.** The labels shown were checked against this repository's `cache/*/terms.csv`. IDs marked **[verify]** were not in the cache. Look them up before you bind them.

**Unavailable tools.** The claude.ai PubMed and OLS connectors were not authorized in this session, so they were not used. They can be enabled in the claude.ai connector settings.

---

## 1. Disease information

**Overview.** SCFI is an autosomal recessive mitochondrial disease. It is caused by biallelic hypomorphic variants in **PPA2** (hgnc:28883), which encodes the mitochondrial inorganic pyrophosphatase. Affected children who seemed healthy die suddenly of cardiac arrest or acute heart failure, usually before age 2. Death often follows a viral illness. Guimier et al. 2016 reported "seven individuals from three families affected by sudden and unexpected cardiac arrest between 4 and 20 months of age" and found "compound heterozygous missense mutations in PPA2" *(PMID:27523598, cached)*.

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0014973, "sudden cardiac failure, infantile" |
| OMIM (disease) | #617222 (named in PMID:33028643 and PMID:33826954) |
| OMIM (gene) | PPA2 \*609988 (PMID:31705601) |
| Allelic disorder | Sudden cardiac failure, alcohol-induced (SCFAI): OMIM #617223, MONDO:0014974 |
| HGNC | hgnc:28883 (PPA2) |
| LOVD | disease #06623 ([LOVD](https://databases.lovd.nl/shared/diseases/06623)) |
| Orphanet | No dedicated ORPHA code was found; no `ORPHA_*.md` cache mentions PPA2 **[verify]** |
| ICD-10/11, MeSH | No disease-specific codes. The closest MeSH headings are *Death, Sudden, Cardiac* and *Mitochondrial Diseases* (MeSH terms on PMID:27523597) |

**Synonyms:** SCFI; PPA2 deficiency; inorganic pyrophosphatase 2 deficiency; PPA2-associated sudden cardiac death (PMID:34400813); PPA2-related mitochondriopathy (PMID:37269378).

**Source of the data.** All knowledge comes from aggregated case reports and case series. About 45 individuals in roughly 25 families had been reported by 2021, with further single reports in 2023–2026. There are no registry or EHR cohorts.

**Lump/split note.** SCFI and SCFAI are separate in both OMIM and MONDO. They are, however, one genotype–activity continuum. Guimier 2021 describes "inter- and intrafamilial phenotypic variability" *(PMID:34400813, cached)*. Kennedy's index family (p.[Glu172Lys];[Pro228Leu]) presented in the teens with alcohol sensitivity, while other genotypes caused death in infancy *(PMID:27523597)*.

## 2. Etiology

**Cause.** Biallelic PPA2 variants that partly lose function. "Biallelic hypomorphic variants in PPA2 … have been recently identified in individuals presenting with sudden cardiac death, occasionally triggered by alcohol intake or a viral infection" *(PMID:34400813, cached)*.

**Genetic risk factors**
- **Commonest variant: c.514G>A p.(Glu172Lys).** It is "the most frequent pathogenic PPA2 variant … identified in 11 of the 20 families in our cohort". It has a "gnomAD allele frequency of 0.00053, and has never been seen in the homozygous state" *(PMID:34400813, cached)*. Its absence as a homozygote suggests it is close to null and is only tolerated in trans with a milder allele.
- **Other recurrent alleles:** p.Pro228Leu (milder), p.Arg127Leu, p.Pro167Leu, p.Met94Val, p.Ser61Phe, p.Arg127Cys, p.Ser175\* (nonsense), and p.Gln327fs (frameshift).

**Environmental triggers (gene × environment)**
- **Febrile viral illness.** "Both individuals from family 3 and the affected individual from family 4 had viral infections at the time of hospital admission". Rotavirus and norovirus were confirmed in stool *(PMID:27523597, cached)*. Guimier 2021: "a viral test was positive in five cases" *(cached)*.
- **Alcohol, even small amounts.** "Four teenagers drank alcohol before sudden cardiac arrest" *(PMID:34400813, cached)*. Also reported in PMID:37249496, PMID:37269378 and PMID:38582264: "Two brothers from family 1 suffered sudden death after a small first intake of alcohol".
- **Temperature.** Mutant enzymes "were significantly decreased and sensitive to temperature" *(PMID:34400813, cached)*. This gives a plausible molecular basis for fever as a trigger: thermolabile enzyme activity falls below a critical threshold. This link is inferred, not demonstrated in patients.
- **Protective factors.** None known. Avoiding alcohol and preventing or treating fever are the only modifiable factors.

## 3. Phenotypes

**Cardiac phenotypes**

| Phenotype | HPO | Frequency / evidence | Onset and course |
|---|---|---|---|
| Sudden cardiac death | HP:0001645 Sudden cardiac death | 28/34 died; 15 by sudden arrest (PMID:34400813) | Infancy (median under 2 y); a second peak at 14–16 y |
| Cardiac arrest | HP:0001695 Cardiac arrest | Core feature | Acute |
| Acute heart failure / cardiogenic shock | HP:0001635 Congestive heart failure; HP:0030149 Cardiogenic shock | 13/28 deaths were from acute heart failure (PMID:34400813) | Acute, often with infection |
| Myocardial fibrosis | HP:0001685 Myocardial fibrosis | "myocardial fibrosis was reported in 15 cases" (PMID:34400813); "marked mid-myocardial fibrosis" on MRI (PMID:27523597) | Chronic, accumulates over time |
| Dilated cardiomyopathy | HP:0001644 Dilated cardiomyopathy | Necropsy: "dilation of the left ventricle, focal fibrosis, and inflammatory infiltrates with acute myocyte loss" (PMID:34400813) | Progressive; one prenatal case |
| Ventricular fibrillation / VT | HP:0001663 Ventricular fibrillation; HP:0004756 Ventricular tachycardia | Two children with "multiple VF arrests starting at 20 months and 18 months" (PMID:34400813) | Episodic |
| Myocarditis-like inflammatory infiltrate | HP:0012819 Myocarditis | 6/34, always with fibrosis (PMID:34400813) | — |
| Hypertrophic cardiomyopathy | HP:0001639 Hypertrophic cardiomyopathy | Listed only in aggregator summaries; no primary source found **[verify]** | — |

**Metabolic, neurological and other phenotypes**

| Phenotype | HPO | Frequency / evidence | Onset and course |
|---|---|---|---|
| Lactic acidosis | HP:0003128 Lactic acidosis | 5/34 (PMID:34400813); severe in neonates (PMID:27523597) | Neonatal or during crises |
| Seizures | HP:0001250 Seizure | In the severe neonatal and infantile forms (PMID:27523597) | Neonatal to infancy |
| Hypotonia | HP:0001252 Hypotonia | Severe forms | — |
| Vomiting / diarrhea | HP:0002013 Vomiting; HP:0002014 Diarrhea | Before decompensation (PMID:27523597) | Prodrome |
| Vocal cord paralysis | HP:0001605 Vocal cord paralysis | Single case, with hypertension (PMID:33028643) | 5 weeks |
| Peripheral axonal neuropathy, external ophthalmoplegia, ptosis | HP:0003477 Peripheral axonal neuropathy; HP:0000544 External ophthalmoplegia; HP:0000508 Ptosis | One survivor, from age 29 (PMID:34400813) | Progressive |
| Ataxia, spasticity, dysarthria | HP:0002073 Progressive cerebellar ataxia | One survivor, from about age 14 (PMID:34400813); "Progressive neurological signs were observed in 2/6 surviving individuals" | Progressive |
| Alcohol sensitivity | No precise HPO term found **[verify]** | Index family and teenagers | Lifelong |

**Quality of life.** No formal QoL studies exist. In survivors, the burden comes from a defibrillator, lifelong restrictions on alcohol and medicines, and progressive neurological disability.

## 4. Genetic and molecular information

- **Gene.** PPA2, located at 4q24 (location from aggregator sources). It is nuclear-encoded and imported into the mitochondrial matrix. Its catalytic function is inorganic diphosphatase activity: GO:0004427 **[verify label]**. The parent term GO:0016462 "pyrophosphatase activity" is cached.
- **Variant classes.** Mostly missense. LoF alleles (nonsense, frameshift) occur only in trans with a hypomorph. The authors took "the absence of common or homozygous LoF variants within gnomAD … as evidence to support LoF as a mechanism for pathogenicity" *(PMID:34400813, cached)*. Complete loss is presumed lethal, consistent with yeast *ppa2Δ* inviability.
- **Variant effects on enzyme activity (PMID:27523597, cached):**
  - p.Pro167Leu and p.Glu172Lys: "5%–10% residual activity".
  - p.Pro228Leu: "residual activity of 24%–28%".
  - Residual activity tracks severity: "Recombinant PPA2 enzymes modeling hypomorphic missense mutations had decreased activity that correlated with disease severity".
- **Germline vs somatic.** All variants are germline. A de novo missense in trans with an inherited nonsense variant was phased by long-read sequencing (PMID:33826954).
- **Population frequency.** "The cumulative heterozygous carrier frequency … is 0.0024, which would result in a calculated prevalence … of 0.58 per 100,000 (1 in 170,000)" *(PMID:27523597, cached)*.
- **ClinGen.** PPA2–dilated cardiomyopathy (MONDO:0005021) is classified **Strong, AR** by the DCM gene curation expert panel (2025-05-16). That classification is for DCM, not for SCFI itself.
- **Updated DCM gene evidence.** PPA2 is among the AR genes rated "high evidence" for DCM (Jordan et al., *Circulation* 2026, PMID:42708185).
- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

## 5. Environmental information

- **Ethanol** (CHEBI:16236 **[verify]**). A trigger at very low doses. Avoid ethanol in medicines (PMID:39882621).
- **Viral infections.** These are triggers, not causes. Rotavirus and norovirus have been documented (PMID:27523597). Fever is the likely link (see Section 2).
- **Toxins and lifestyle.** Nothing else reported. Maternal smoking was noted in one case without causal inference (PMID:31705601).

## 6. Mechanism and pathophysiology

**Causal chain**

1. Biallelic hypomorphic PPA2 variants **lead to** reduced, thermolabile inorganic pyrophosphatase activity in the mitochondrial matrix (GO:0005759). Shown directly with recombinant enzymes and patient-fibroblast mitochondria (PMID:27523597, PMID:34400813).
2. Reduced PPi hydrolysis **results in** PPi accumulation and loss of the thermodynamic pull on PPi-producing matrix reactions such as mtDNA, RNA and protein synthesis and fatty-acyl-CoA activation. *Inferred* from enzymology; matrix PPi has not been measured in patients.
3. **Leads to** failure of energy transduction and inability to maintain inner-membrane potential (GO:0051881 "regulation of mitochondrial membrane potential"; GO:0005743). Shown in yeast: "pathogenic PPA2 mutations rapidly inactivate the mitochondrial energy transducing system and prevent the maintenance of a sufficient electrical potential across the inner membrane, which explains the subsequent disappearance of mitochondria" *(PMID:27523598, cached)*.
4. **Results in** reduced ATP supply (GO:0006754 "ATP biosynthetic process"; GO:0042775) in cardiomyocytes (CL:0000746 "cardiac muscle cell"). Kennedy et al. propose that hearts "were consistently deprived of adequate ATP resulting in fibrosis" *(PMID:27523597, cached)*. This is a hypothesis, not measured in human heart.
5. **Branch A (chronic):** cardiomyocyte loss **leads to** replacement fibrosis by cardiac fibroblasts (CL:0002548; GO:0030198), mainly mid-myocardial in the left ventricle (UBERON:0002084, UBERON:0002349). This **leads to** dilated cardiomyopathy and an arrhythmogenic substrate.
6. **Branch B (acute):** a stressor such as fever (thermolabile enzyme) or alcohol (unknown mechanism, perhaps extra redox or acetaldehyde load on already-limited mitochondria) **pushes** activity below a critical threshold. This **results in** acute myocyte loss, ventricular fibrillation (impaired GO:0086001 "cardiac muscle cell action potential" and GO:0060048 "cardiac muscle contraction"), cardiogenic shock and sudden death. The trigger effect is observed clinically; its molecular mechanism is inferred.
7. **Systemic branch:** the same deficit in brain, nerve and skeletal muscle **leads to** lactic acidosis, seizures and hypotonia in severe neonatal forms, and to progressive neuropathy and ataxia in long-term survivors.

**Supporting detail**
- **Mitochondrial dynamics.** PPA2 "activates mitochondrial fission signaling through MTFP1-DNM1L … leading to mitochondrial proliferation or mitophagy" (Mishra et al., *Autophagy* 2026, PMID:40873007, HeLa cells; in vitro). This could explain mitochondrial loss, but it is not shown in patient cells.
- **Proposed further roles** (from a review, PMID:31705601): "mtDNA maintenance; oxidative phosphorylation and generation of ATP; reactive oxygen species homeostasis; mitochondrial membrane potential regulation".
- **Structure.** An animal-specific "W-loop" is proposed as a site for small-molecule effectors (PMID:40513929). The yeast mitochondrial PPase crystal structure is PMID:39178581.
- **Immune involvement.** Inflammatory infiltrates are secondary. "Fibrosis may help discriminate between PPA2-related cardiomyopathy and viral myocarditis" *(PMID:34400813, cached)*.
- **Omics, single-cell and functional genomics.** No patient datasets were found.

## 7. Anatomical structures affected

- **Primary:** heart (UBERON:0000948), myocardium (UBERON:0002349), left ventricle (UBERON:0002084). Right-ventricle (UBERON:0002080) involvement has not been documented specifically.
- **Secondary:** brain (seizures), peripheral nerve, extraocular muscles, larynx (vocal cord paralysis; one case).
- **Cells:** cardiac muscle cell (CL:0000746); fibroblast of cardiac tissue (CL:0002548); patient skin fibroblasts (CL:0000057) were used for diagnosis.
- **Subcellular:** mitochondrial matrix (GO:0005759) and mitochondrial inner membrane (GO:0005743).
- **Laterality:** fibrosis is focal or patchy and mid-myocardial (PMID:27523597, PMID:40703559).

## 8. Temporal development

- **Onset.** Neonatal to about 20 months for classic SCFI. Fetal onset has been seen ("One case was diagnosed prenatally with cardiomyopathy", PMID:34400813). Milder genotypes present at school age (PMID:40486711), in adolescence (alcohol), or in adulthood:
  - acute heart failure after a viral illness at 58 years with homozygous p.Arg127Leu, "reversible" (PMID:41080696);
  - non-ischemic cardiomyopathy from age 28 needing two heart transplants (PMID:40846385).
- **Pattern.** Often silent until an acute catastrophic event: "Two healthy and asymptomatic sisters died unexpectedly at ages 12 and 10 months" *(PMID:31705601, cached)*. Fibrosis builds up chronically underneath, and survivors show progressive neurological disease.
- **Critical periods.** Infancy, during febrile illness, and adolescence, at first exposure to alcohol.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007 "Autosomal recessive inheritance"). Expressivity is variable, within and between families. Penetrance of severe genotypes appears high; long-term penetrance of mild genotypes is unknown.
- **Prevalence.** The estimate is 1 in 170,000, or 0.58 per 100,000, calculated from ExAC carrier frequencies (PMID:27523597). This is a calculated genotype prevalence, not observed disease prevalence. Use `measure_type: UNKNOWN` or record it as a carrier-frequency–derived estimate, with the cumulative carrier frequency of 0.0024.
- **Populations.** Reported in Europeans (UK, New Zealand, France, Spain), US, Chinese (PMID:33826954), Pakistani (homozygous, PMID:41743516), and a series from Queensland, Australia (PMID:41640115). No founder effect has been established.
- **Consanguinity and sex ratio.** Homozygous cases suggest consanguinity in some families. No sex bias has been reported.

## 10. Diagnostics

- **Genetic testing is the cornerstone.**
  - Exome or genome sequencing, including molecular autopsy.
  - Diagnosis after death from a newborn dried blood spot: "highlights the utility of dried blood spots for postmortem molecular diagnosis" *(PMID:33028643, cached)*.
  - PPA2 is on Genomics England PanelApp panels for sudden cardiac death, dilated/arrhythmogenic cardiomyopathy and mitochondrial disease ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/entities/PPA2)).
  - Long-read sequencing can establish phase when one variant is de novo (PMID:33826954).
- **Functional test.** Pyrophosphatase activity in fibroblast mitochondria is reduced (PMID:27523597).
- **Imaging.** Cardiac MRI shows mid-myocardial or patchy late gadolinium enhancement (PMID:27523597, PMID:40703559).
- **Laboratory.** Lactate (lactic acidosis) and troponin/BNP during crises.
- **ECG and Holter.** VT/VF.
- **Histopathology.** "Myocyte loss, disarray, or fibrosis was present in all individuals" *(PMID:27523597, cached)*.
- **Differential diagnosis:**
  - viral myocarditis (fibrosis favours PPA2);
  - channelopathies (LQTS, CPVT);
  - other mitochondrial cardiomyopathies (TAZ, AARS2, MRPL44, DNAJC19; see the cohort in PMID:30384889);
  - fatty-acid oxidation defects;
  - LPIN1 deficiency (also a cause of sudden death in young children, PMID:41640115);
  - SIDS/SUDC.
- **Screening.** Cascade testing of siblings is recommended after an index death (PMID:41743516). No newborn screening exists.

## 11. Outcome and prognosis

- **Mortality.** "Among the 34 individuals, only 6 remain alive. Twenty-three died before the age of 2 years while five died between 14 and 16 years" *(PMID:34400813, cached)*.
- **Survivors.** Some survive with a defibrillator. A 13-month-old had "excellent neurological recovery" after prolonged resuscitation (PMID:39882621). Others live into their 40s with fibrosis (PMID:27523597) or reach transplant (PMID:40846385).
- **Prognostic factors.** Residual enzyme activity, genotype, alcohol exposure, febrile illness, and the extent of fibrosis.

## 12. Treatment

There is no disease-modifying therapy.

- **Implantable cardioverter-defibrillator** for primary or secondary prevention (PMID:27523597, PMID:34400813, PMID:39882621). PMID:38582264 suggests "early defibrillator implantation might prevent lethal arrhythmias". NCIT term **[verify]**; no cached NCIT ICD term was found. Bind NCIT:C15329 "Surgical Procedure" if the specific term is not admissible, and carry the device as a qualifier per the CLAUDE.md device pattern.
- **Strict alcohol avoidance**, including alcohol in medicines (PMID:34400813, PMID:39882621). Recorded as counselling or behavioural modality.
- **Heart failure pharmacotherapy and heart transplantation.** Transplant was done twice in PMID:40846385. NCIT:C15986 "Pharmacotherapy"; NCIT:C15289 for organ transplantation (taken from CLAUDE.md; confirm in the cache).
- **Acute care.** Supportive care (NCIT:C15747 "Supportive Care"), ECMO, and correction of lactic acidosis. Aggressive treatment of fever is reasonable but unproven.
- **Genetic counselling.** NCIT:C15240 "Genetic Counseling".
- **Experimental.** No clinical trials found. Mitochondrial "cocktails" are unproven.

## 13. Prevention

- **Primary prevention.** Carrier and cascade testing, and prenatal or preimplantation diagnosis for known familial variants.
- **Secondary prevention.** Genetic screening of siblings, cardiac MRI and Holter, and an ICD for at-risk biallelic relatives.
- **Tertiary prevention.** Lifelong avoidance of alcohol, fever management, and vaccination to limit viral triggers (a reasonable inference; no data).

## 14. Other species

No naturally occurring PPA2 disease in animals was found; OMIA was not searched directly **[verify]**. Mitochondrial pyrophosphatases are conserved from yeast (*S. cerevisiae* PPA2) to human: "Yeast PPA2 gene encodes a mitochondrial inorganic pyrophosphatase that is essential for mitochondrial function" (PMID:1648084).

## 15. Model organisms

- **Yeast (*S. cerevisiae*, NCBITaxon:4932 [verify]).**
  - *ppa2Δ* "compromises cell viability due to the loss of mitochondria". Human wild-type PPA2 rescues it; patient alleles do not (PMID:27523598, cached).
  - This recapitulates the molecular and organelle defect but has no cardiac readout. Relationship to the mechanism nodes: RECAPITULATES the membrane-potential and energy-transduction nodes; FAILS_TO_RECAPITULATE fibrosis and arrhythmia.
  - Ageing context: PMID:31082499.
- **Recombinant enzyme assays** (in vitro). Show thermolability and residual activity (PMID:27523597, PMID:34400813, PMID:40513929).
- **Patient fibroblasts** (in vitro). Show reduced activity (PMID:27523597).
- **HeLa knockdown** (in vitro). Fission and mitophagy signalling (PMID:40873007).
- **Mouse, zebrafish, iPSC-cardiomyocytes.** No published PPA2 disease model was found. This is a knowledge gap and a strong candidate for a `HUMAN_MODEL_MISMATCH` / `KNOWLEDGE_GAP` discussion. A zebrafish search result concerned PP2Cm, an unrelated phosphatase, and should not be used.

---

## Key sources

**Cached, quotable:**

| PMID | Paper |
|---|---|
| 27523597 | Kennedy et al., *AJHG* 2016 |
| 27523598 | Guimier et al., *AJHG* 2016 |
| 34400813 | Guimier et al., *Genet Med* 2021 (PMID:35394429 is a duplicate record of the same title) |
| 31705601 | Phoon et al. 2020 |
| 33028643 | Sanford et al. 2020 |
| 33826954 | Zhao et al. 2021 |

**Uncached; fetch before citing:** 37249496, 37269378, 37869221, 38582264, 39882621, 40486711, 40703559, 40846385, 41080696, 41743516, 41640115, 40873007, 40513929, 42708185, 30384889, 1648084, 16300924. PMID:16300924 is negative: no PPA2 mutations were found in mtDNA depletion syndrome patients.

**Web sources:**
- [Kennedy et al. 2016 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5011043/)
- [PubMed search: PPA2](https://pubmed.ncbi.nlm.nih.gov/?term=PPA2%5Btiab%5D+AND+%28cardiac+OR+sudden+OR+mitochondrial%29&size=50&sort=date)
- [LOVD disease #06623](https://databases.lovd.nl/shared/diseases/06623)
- [GenCC PPA2](https://search.thegencc.org/genes/HGNC:28883)
- [PanelApp PPA2](https://panelapp.genomicsengland.co.uk/panels/entities/PPA2)
- [MalaCards SCFI](https://www.malacards.org/card/sudden_cardiac_failure_infantile)
