---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-31T20:48:25.814220'
end_time: '2026-08-31T20:57:37.661835'
duration_seconds: 551.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chemotherapy-Induced Neutropenia
  mondo_id: ''
  category: Complex
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
  web_search_requests: 26
  num_turns: 40
  total_cost_usd: 3.7584274999999994
  session_id: 966f6369-68c0-46a4-a6e1-e71065f5c7c0
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chemotherapy-Induced Neutropenia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Chemotherapy-Induced Neutropenia** covering all of the
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

# Chemotherapy-Induced Neutropenia (CIN) — Comprehensive Research Report

*Prepared 2026-08-31 for dismech knowledge-base curation.*

**A framing note before the data:** this entry is not a disease in the "broken gene → broken protein → sick person" sense. It's an iatrogenic injury — we deliberately poison a fast-dividing tissue to kill another fast-dividing tissue, and the bone marrow is collateral. So several template sections (causal genes, inheritance, natural disease in other species) don't map cleanly, and I've said so plainly rather than manufacturing content. Where the section *does* have a real analogue — germline pharmacogenomics standing in for "causal genes," cytotoxic drug class standing in for "environmental exposure" — I've curated that instead and flagged the substitution.

**Evidence-verification status, stated up front:** PMIDs marked ✅ below were retrieved and read this session (via NCBI E-utilities or PMC). PMIDs marked ⚠️ are derived from PubMed URLs and search-result summaries and were *not* opened directly — treat every quoted string from those as a **lead, not a snippet**. Before any of these become `snippet:` values in a dismech entry, run `just fetch-reference PMID:NNNNNNNN` and match the exact substring against the cache. Ontology IDs marked ✅ were resolved live against the EBI OLS4 API this session; ones marked 🔍 need a local OAK lookup before binding.

---

## 1. Disease Information

### What it is

Chemotherapy-induced neutropenia is the drop in circulating neutrophils that follows cytotoxic anticancer therapy, because the drugs that hit dividing cancer cells also hit the dividing granulocyte precursors in marrow. The marrow is basically a factory running three shifts — stem cells, a dividing (mitotic) pool, and a maturing (post-mitotic) storage pool — and chemotherapy shuts down the middle shift. The warehouse keeps shipping for a few days, then runs dry. That lag *is* the nadir.

Its clinically dangerous form is **febrile neutropenia (FN)**: fever arriving while the neutrophil count is on the floor, which is a medical emergency because the usual sign of infection — pus, inflammation, a visible abscess — requires neutrophils to make, and there aren't any. The fever is often the *only* sign.

### Identifiers

| Resource | ID | Label | Status |
|---|---|---|---|
| MeSH | **D064146** | Chemotherapy-Induced Febrile Neutropenia | ✅ resolved via OLS |
| MedGen | **C3658261** | Febrile Neutropenia, Chemotherapy-Induced | ✅ |
| OMIT | **0028359** | Chemotherapy-Induced Febrile Neutropenia | ✅ |
| MONDO | **MONDO:0001475** | Neutropenia (parent concept) | ✅ |
| NCIT | **NCIT:C80520** | Neutropenia — "A decrease in the number of neutrophils in the peripheral blood." | ✅ |
| NCIT | **NCIT:C35665** | Febrile Neutropenia | ✅ |
| NCIT | **NCIT:C143481** | Febrile Neutropenia, CTCAE | ✅ |
| NCIT | **NCIT:C59479 / C59715 / C59951** | Grade 3 / 4 / 5 Febrile Neutropenia, CTCAE | ✅ |
| HP | **HP:0001875** | Decreased total neutrophil count | ✅ |
| HP | **HP:0410255** | Transiently decreased total neutrophil count | ✅ |
| HP | **HP:0012235** | Drug-induced agranulocytosis — "<50 granulocytes per microliter" caused by drug exposure | ✅ |
| ICD-10-CM | **D70.1** Agranulocytosis secondary to cancer chemotherapy; **D70.9** Neutropenia unspecified; **T45.1X5A** adverse effect of antineoplastic drugs | 🔍 verify in `icd10cm` adapter |
| ICD-11 | 3A20.0 / 3A20 (drug-induced neutropenia branch) | 🔍 verify |
| OMIM / Orphanet | **Not applicable** — acquired iatrogenic condition, no OMIM or ORPHA disorder entry | — |

**⚠️ MONDO gap — important curation finding.** A direct OLS query for MONDO terms matching "chemotherapy-induced neutropenia," "drug-induced neutropenia," or "febrile neutropenia" returned **nothing**. MONDO carries `MONDO:0001475` (Neutropenia) plus a long tail of *congenital* neutropenia syndromes, but no drug-induced or chemotherapy-induced child that I could resolve. Recommended handling in dismech: anchor `disease_term` on `MONDO:0001475` with a `mappings.mondo_mappings` entry using `mapping_predicate: skos:narrowMatch`, per the design-decisions rule for promoted concepts lacking their own term, and record the gap in `notes:`. Do **not** invent a MONDO ID here — my own memory note (`never guess MONDO ids`) exists precisely because guessed IDs resolve to real-but-wrong concepts.

### Synonyms

Chemotherapy-induced neutropenia; CIN; chemotherapy-induced myelosuppression (broader — includes anemia and thrombocytopenia); myelotoxicity; neutropenic fever; febrile neutropenia; FN; chemotherapy-induced febrile neutropenia; drug-induced agranulocytosis (when profound); bone marrow suppression.

Note the near-synonym trap: **"chemotherapy-induced myelosuppression" (CIM) is the multilineage parent**, of which CIN is the neutrophil lineage. Trilaciclib's label and the trilaciclib literature use CIM, not CIN. Keep the two distinguishable in the entry.

### Data provenance

Both. Individual-patient EHR/claims data drive the burden and incidence figures (Boccia et al. pooled US claims and hospital datasets ✅ PMID:35552754); aggregated trial and registry data drive the regimen-specific risk estimates and the guideline thresholds.

---

## 2. Etiology

### Primary cause

The cause is the drug. This is a dose-dependent, largely predictable, on-target-off-tissue toxicity, and the "genetic etiology" here is *host pharmacogenomics modulating exposure*, not a disease gene.

**Highest-risk agent classes** (mechanistic grouping):

| Class | Exemplars | Mechanism of marrow injury |
|---|---|---|
| Taxanes | docetaxel, paclitaxel | microtubule stabilization → mitotic arrest → apoptosis of dividing progenitors |
| Anthracyclines | doxorubicin, epirubicin | topoisomerase II poisoning + DNA intercalation + ROS |
| Alkylators | cyclophosphamide, ifosfamide, bendamustine | DNA crosslinking; hits quiescent HSC as well as cycling progenitors |
| Platinums | carboplatin (> cisplatin) | DNA adducts; carboplatin notably myelosuppressive, cisplatin comparatively not |
| Topo-I inhibitors | topotecan, irinotecan | topoisomerase I trapping → replication-fork collapse |
| Antimetabolites | 5-FU, gemcitabine, methotrexate, cytarabine | S-phase nucleotide starvation / fraudulent nucleotide incorporation |
| ADCs | sacituzumab govitecan, trastuzumab deruxtecan | payload (SN-38, DXd) released systemically reaches marrow |

High-FN-risk (>20%) regimen exemplars documented in the literature: **TAC** (docetaxel/doxorubicin/cyclophosphamide) is consistently classified >20% ⚠️; **TC** (docetaxel 75 + cyclophosphamide 600 q3w) has reported FN rates spanning **4–69%** across studies, and a meta-analysis supports G-CSF primary prophylaxis for it ⚠️ PMID:26337685; **TPF** (docetaxel/cisplatin/5-FU) for head and neck ⚠️; dose-dense AC-T; R-CHOP in older lymphoma patients; topotecan and platinum-etoposide in SCLC.

### Risk factors

**Treatment-related (dominant):**
- Regimen myelotoxicity and dose intensity — the single largest determinant
- Prior chemotherapy or radiotherapy (especially pelvic/vertebral fields — marrow reserve is a bank account you can overdraw)
- Concurrent radiotherapy
- Cycle number: FN clusters in **cycle 1** — a prospective multinational MASCC study of 364 patients across 1,601 cycles found FN in **5% of first cycles, 3% in cycles 2–3, 1% in cycles 4–6**, with **9% of patients** having ≥1 FN episode and **59% of all FN events occurring in cycle 1** ⚠️ (PMC10570161). That front-loading is why *primary* prophylaxis beats *secondary*.

**Patient-related:**
- **Age ≥65** — the most consistently replicated host risk factor
- Low baseline ANC / low pretreatment absolute lymphocyte count / low pretreatment monocyte count ⚠️ (PMC5922370)
- Poor performance status, low albumin, low BMI (or, in some analyses, obesity via dosing practice)
- Bone marrow involvement by tumor
- Renal or hepatic impairment (reduced drug clearance → higher exposure)
- Comorbidities: cardiovascular, hepatic, diabetes
- Advanced disease stage; hematologic malignancy > solid tumor
- Open wounds / active infection

**Genetic risk factors** — see §4, but in brief: `DPYD` (fluoropyrimidines), `UGT1A1` (irinotecan), `TPMT` and `NUDT15` (thiopurines), `CYP2B6` (cyclophosphamide), `CDA` (gemcitabine/capecitabine), plus GWAS hits at `SLC15A1`, `NR1I2`(PXR), `FMO3`, and platinum loci at 2q24.3 and 17p12.

**Environmental / lifestyle:** malnutrition; poor dentition and periodontal disease (a portal of entry); crowded or high-exposure living or occupational settings; no strong evidence that smoking or alcohol independently drive CIN incidence, though both correlate with comorbidity burden.

### Protective factors

- **G-CSF prophylaxis** — the dominant modifiable protective factor (§12)
- **Trilaciclib** — pharmacologic myeloprotection via transient G1 arrest of HSPCs
- Dose reduction / schedule modification — protective against FN but at the cost of relative dose intensity (§11); a genuine two-edged trade
- **Genetic:** the flip side of the pharmacogene story — normal-function `DPYD`, `UGT1A1*1/*1`, wild-type `TPMT`/`NUDT15` are effectively protective alleles for the corresponding drugs
- **Higher baseline ANC** — and this is where the Duffy story sits (§4/§9), because a *lower* baseline ANC in Duffy-null individuals is NOT a risk factor for infection, but is systematically misread as one

### Gene–environment interaction

This condition is almost the platonic case of GxE: the "environment" is a precisely dosed, precisely timed chemical exposure, and the genotype sets the exposure–response curve. A `DPYD` poor metabolizer given standard 5-FU experiences a pharmacokinetic exposure several-fold higher than intended; the same genotype with no fluoropyrimidine exposure is clinically silent. CPIC and DPWG both publish genotype-directed dose reductions, and DPYD/UGT1A1 pre-emptive genotyping is now implemented in multiple health systems ⚠️ (PMC8827955, PMC9262778).

---

## 3. Phenotypes

The defining feature of CIN's phenotype list is what's *missing*: neutropenia is largely **asymptomatic until it isn't**. Without neutrophils you cannot mount the local inflammatory response that produces the usual signs of infection, so a patient can go from "fine" to "septic" with almost no intermediate signal. Fever is often the only manifestation, and that's precisely why it's treated as an emergency.

| Phenotype | Category | HP suggestion | Onset | Severity | Course | Frequency |
|---|---|---|---|---|---|---|
| Decreased absolute neutrophil count | Laboratory | **HP:0001875** ✅ (consider `temporality: TRANSIENT`, or **HP:0410255** ✅) | Days 5–14 post-infusion | Mild→profound | Episodic, cycle-locked | Near-universal with myelosuppressive regimens; grade 3–4 in a large minority |
| Profound neutropenia / agranulocytosis (ANC <100–500/µL) | Laboratory | **HP:0012235** ✅ (drug-induced agranulocytosis) | Nadir | Severe | Episodic | Regimen-dependent |
| Fever (the FN presentation) | Sign | 🔍 look up HP "Fever" | At nadir | Severe by definition | Acute, episodic | ~9% of patients over a course in intermediate-risk regimens ⚠️ |
| Bacteremia / bloodstream infection | Sign | 🔍 | At nadir | Severe | Acute | Documented in a minority of FN episodes; most FN is culture-negative |
| Sepsis / septic shock | Sign | 🔍 | At nadir | Life-threatening | Acute | Drives most FN mortality |
| Oral mucositis / oropharyngeal ulceration | Sign | 🔍 | Days 5–10 | Mild→severe | Episodic | Common; mechanistically coupled to CIN (§6) |
| Perianal cellulitis / typhlitis (neutropenic enterocolitis) | Sign | 🔍 | At nadir | Severe | Acute | Uncommon but high-lethality |
| Invasive fungal infection | Sign | **HP:0020101** ✅ | Prolonged neutropenia (>7 days) | Severe | Acute | Risk rises steeply with duration |
| Invasive pulmonary aspergillosis | Sign | **HP:0020103** ✅ | Prolonged neutropenia | Severe | Acute | Mostly hematologic malignancy / HSCT |
| Severe Candida infection | Sign | **HP:6001283** ✅ (definition explicitly references profound chemotherapy neutropenia) | Prolonged | Severe | Acute | — |
| Concurrent anemia | Laboratory | 🔍 | Cumulative | Variable | Progressive over cycles | Multilineage CIM |
| Concurrent thrombocytopenia | Laboratory | 🔍 | Days 7–14 | Variable | Episodic | Multilineage CIM |
| Fatigue | Symptom | 🔍 | Throughout | Moderate | Fluctuating | Very common; largest QoL driver |
| Treatment delay / dose reduction | Not a phenotype — model as `clinical_burden` or `progression` | — | — | — | — | — |

**Severity grading — and a 2025 change you must not miss.**

CTCAE v5.0 "Neutrophil count decreased," ANC thresholds ⚠️:
- Grade 1: <LLN – ≥1500/µL
- Grade 2: <1500 – ≥1000/µL
- Grade 3: <1000 – ≥500/µL
- Grade 4: <500/µL

**CTCAE v6.0 (released 2025) shifted every band down one notch** ✅ PMID:41158990 (Merz LE, *HemaSphere* 2025;9(10):e70242):
- Grade 1: <1500 – 1000/µL
- Grade 2: <1000 – 500/µL
- Grade 3: <500 – 100/µL
- Grade 4: <100/µL

The paper's own framing, quoted from the article: *"It is no longer accurate or appropriate to use neutropenia severity grading from the 1980s to assess treatments from the 2020s."* Two drivers: modern agents aren't 1980s cytotoxics, and the old thresholds pathologized the normal ANC range of Duffy-null individuals. **Any dismech entry citing a "grade 3/4 neutropenia" rate must state which CTCAE version the source used** — the same patient reclassifies between v5 and v6.

Febrile neutropenia definition (IDSA/common clinical): single oral temperature ≥38.3 °C (101 °F), or ≥38.0 °C sustained over one hour, **plus** ANC <500/µL or <1000/µL with predicted decline to <500 ⚠️. Note that some sources cite ANC <1500 for the FN definition; the <500 threshold is the operational one.

**Quality of life.** Trilaciclib trials measured patient-reported outcomes alongside myeloprotection endpoints and reported improvements in fatigue and physical wellbeing domains ✅ PMID:34408488. Beyond the direct symptom burden, CIN drives hospitalization (average LOS 6–10 days ✅ PMID:35552754), social isolation during nadir periods, and the anxiety of the "call us if you have a fever" instruction that reorganizes a patient's whole month around a thermometer.

---

## 4. Genetic / Molecular Information

**Causal genes: none.** There is no germline or somatic mutation that causes CIN. What genetics contributes is **susceptibility magnitude** — how much drug exposure a given host generates from a given dose, and how readily their progenitors die from it.

### Pharmacogenes with actionable, guideline-backed evidence

| Gene | HGNC | Drug(s) | Key variants | Consequence | Effect |
|---|---|---|---|---|---|
| **DPYD** | `hgnc:3012` 🔍 | 5-FU, capecitabine | `*2A` (rs3918290), rs67376798 (D949V), `*13` (rs55886062), HapB3 (rs75017182) | Reduced/absent dihydropyrimidine dehydrogenase → impaired pyrimidine catabolism | Severe myelosuppression, mucositis; CPIC dose reduction; EMA mandates pre-treatment testing ⚠️ |
| **UGT1A1** | `hgnc:12530` 🔍 | irinotecan | `*28` (TA7 promoter repeat), `*6` (rs4148323, East Asian) | Reduced glucuronidation of active metabolite SN-38 | rs4148323 "correlated with irinotecan neutropenia"; IM and PM phenotypes were "independent risk factors for febrile neutropenia" in FOLFIRINOX ⚠️ (PMC8909027) |
| **TPMT** | `hgnc:12014` 🔍 | thiopurines (6-MP, azathioprine) | `*2`, `*3A`, `*3C` | Loss of S-methylation → accumulated thioguanine nucleotides | Severe, prolonged myelosuppression |
| **NUDT15** | `hgnc:23063` 🔍 | thiopurines | `*3` (rs116855232), `*6` | "Impaired breakdown of active thiopurine metabolites" | Leukopenia/neutropenia; particularly important in East Asian ancestry. Combined TPMT+NUDT15 "could explain up to 50% of thiopurine-related toxicities" ⚠️. Case report of severe myelosuppression with `*1/*6` ⚠️ PMID:42286409 |
| **CYP2B6** | 🔍 | cyclophosphamide | `*6` | Altered bioactivation to 4-OH-CPA | Variable exposure |
| **CDA** | 🔍 | gemcitabine, capecitabine | rs2072671, rs532545 | Cytidine deaminase activity | Reported association with severe neutropenia |
| **ABCB1 / SLCO1B1** | 🔍 | multiple / methotrexate | various | Transporter function | Exposure modulation |

### GWAS findings

- **Biobank Japan**, 13,122 cancer patients across regimens (antimicrotubule, paclitaxel-based, docetaxel-based) — GWAS of severe neutropenia/leucopenia ⚠️ PMID:23648065 (and a follow-up, PMC7657179)
- **Platinum-based chemotherapy in NSCLC**: rs13014982 (2q24.3) and rs9909179 (17p12) associated with myelosuppression risk ⚠️ PMID:25823687
- **Docetaxel-induced myelosuppression** (Chinese Han cohort): `SLC15A1` rs2297322, `PXR`/`NR1I2` rs3732359, `FMO3` rs2266782 ⚠️
- **CALGB 90401/60404 (Alliance)** GWAS of docetaxel-induced neutropenia ⚠️

### The Duffy / ACKR1 story — and why it belongs in this entry

**`ACKR1`** (atypical chemokine receptor 1, the Duffy blood group gene) 🔍. Homozygosity for the `-67T>C` promoter variant (rs2814778) abolishes erythroid ACKR1 expression and produces the **Duffy-null associated neutrophil count (DANC)** phenotype: a genuinely lower circulating ANC with **no increased infection risk**, because the neutrophils are redistributed to tissue rather than absent. This is not a disease; it was historically mislabeled "benign ethnic neutropenia."

Numbers ✅ (from PMID:41158990 and *Blood Advances* 2023;7(3):317 ⚠️):
- Normal ANC reference range, Duffy-null adults: **1200–1540/µL**; Duffy non-null adults: **2000–7500/µL**
- **~66–67%** of Black/African American individuals in the US carry the Duffy-null phenotype
- Median ANC 2820/µL (Duffy-null) vs 5005/µL (non-null) among healthy Black adults ⚠️
- *"Duffy null patients have ~10% lower eligibility for clinical trials due to ANC criteria alone."* ✅

A 2024 Dana-Farber analysis found that **more than half of studied cancer treatments would require dose reduction, delay, or discontinuation** if a Duffy-null participant's ANC fell below a threshold that is *normal for their phenotype* ⚠️. This is a mechanism by which an ontology-adjacent measurement error becomes an undertreatment disparity, and it is the reason CTCAE v6 moved the grade boundaries.

**Curation suggestion:** model this as a `genetic:` entry with `relationship_type: MODIFIER` (or `SUSCEPTIBILITY` for the misclassification pathway), and consider a `discussions:` entry with `kind: KNOWLEDGE_GAP` on whether Duffy-null status modifies *true* CIN risk versus only its measurement.

**Epigenetics, chromosomal abnormalities, somatic variants:** not applicable to CIN itself. Relevant adjacent finding: **clonal hematopoiesis (CH)** — pre-existing `PPM1D`, `TP53`, `DNMT3A`, `TET2` clones are selected for by cytotoxic therapy, and CH-derived therapy-related myeloid neoplasms occur in up to **2.3%** of autologous-HSCT recipients at a median **2.6 years** post-transplant, with worse outcomes than non-CH-derived tMN ⚠️ (*Leukemia* 2024, PMC11147764). This belongs in §11 as a long-term complication of the same cytotoxic exposure, not as a cause of CIN.

---

## 5. Environmental Information

For CIN, "environmental factor" *is* the drug exposure, which makes this section unusually well-defined.

**Suggested `environmental:` entries with `influences_mechanisms` links** (remember: `target` here is a **bare node name**, not an entity reference — the pathograph does not use `<kind>#<name>`):

| Exposure | ECTO binding | `environmental_effect` | Target node |
|---|---|---|---|
| Systemic cytotoxic chemotherapy administration | 🔍 search ECTO for antineoplastic-agent exposure; may be genuinely unbindable — record the search in `notes:` if so | `TRIGGERS` | Cytotoxic Injury to Granulocyte Progenitors |
| Prior/concurrent ionizing radiation to marrow-bearing bone | 🔍 ECTO ionizing radiation exposure | `EXACERBATES` | Reduced Hematopoietic Reserve |
| Antibiotic exposure (prophylactic fluoroquinolone) | 🔍 | `MODULATES` | Gut Microbiota Disruption |

*A note on predicate choice*: `TRIGGERS` and `EXACERBATES` are in `qc_plugins.CAUSAL_PREDICATES` and count toward compliance scoring. Chemotherapy genuinely triggers this, so `TRIGGERS` is honest here — but antibiotic prophylaxis's net effect on outcomes is contested, so `MODULATES` is the right non-committal predicate for that one.

**Lifestyle factors:** limited independent evidence. Nutritional status and oral/dental hygiene are the two with plausible mechanistic links (barrier integrity, portal of entry).

**Infectious agents — as consequence, not cause.** The organisms that matter in FN, worth curating with NCBITaxon bindings 🔍:
- Gram-negative: *Escherichia coli*, *Klebsiella pneumoniae*, *Pseudomonas aeruginosa* (the one that kills fast)
- Gram-positive: coagulase-negative staphylococci (most common isolate, often line-related), *Staphylococcus aureus*, viridans group streptococci (mucositis-associated, can cause ARDS)
- Anaerobes: *Clostridioides difficile*
- Fungi: *Candida* spp., *Aspergillus* spp. (risk rises sharply beyond ~7 days of neutropenia)
- Viral reactivation: HSV, VZV, CMV

Critically: **most FN episodes are culture-negative.** Only a minority yield a microbiologic diagnosis, which is the empirical anchor for the "febrile mucositis" reframing in §6.

---

## 6. Mechanism / Pathophysiology

### The causal chain

1. **Cytotoxic drug is administered** and distributes systemically, reaching bone marrow — *leads to* —
2. **DNA damage / mitotic arrest / nucleotide starvation in the marrow mitotic pool.** The mitotic pool is the committed granulocytic progenitor compartment (CFU-GM, myeloblasts, promyelocytes, myelocytes) that is "sensitive to myelosuppressive chemotherapeutic drugs" ⚠️ (PMC6472781) — *leads to* —
3. **p53 stabilization → transcriptional induction of the BH3-only protein PUMA (`BBC3`) → BAX/BAK-dependent mitochondrial outer membrane permeabilization → intrinsic apoptosis of progenitors.** Evidence: *"PUMA is largely responsible for the apoptotic effect downstream of p53 in hematopoietic stem cells after irradiation"* and *"Many chemotherapeutic agents function, in part, by inducing apoptosis through p53-dependent up-regulation of proapoptotic BH3-only proteins such as PUMA"* ⚠️. `Puma`-null mice are protected from HSPC depletion ⚠️ (*Blood* 2010;115:3472 and 115:4707). **This step is inferred for most cytotoxics from irradiation and dyskeratosis-congenita models rather than demonstrated directly for each agent** — mark `directness: INDIRECT` and `evidence_source: MODEL_ORGANISM` accordingly.
4. **Branch A (acute, reversible):** progenitor apoptosis halts new granulocyte production — *results in* —
5. **Depletion of the marrow post-mitotic storage pool** over the following days as it continues releasing without resupply — *results in* —
6. **Circulating neutropenia.** The kinetics fall straight out of neutrophil biology: neutrophils have a circulating half-life of only **6–8 hours** and are produced at **5×10¹⁰–10×10¹¹ cells/day** ⚠️ (PMC2930213). A cell type with that turnover has essentially no buffer; the count follows production with only the storage-pool transit time as delay. Hence the **nadir at days 10–14 for most regimens**, with docetaxel notably earlier (median **day 7**) ⚠️ (PMC6472781) — *leads to* —
7. **Loss of innate first-line defense**, plus, in parallel:
8. **Branch B (the mucosal arm, running concurrently):** the same cytotoxic hits the gut and oral epithelium — *results in* — **mucosal barrier injury (mucositis)** — *results in* — **loss of epithelial barrier integrity plus antibiotic- and chemotherapy-driven dysbiosis of commensal microbiota**, with commensals converting to pathobionts — *results in* — **bacterial translocation into the bloodstream** and, independently, **cytokine release / inflammatory response even in the absence of proven infection** ⚠️ PMID:25196917 ✅. The authors of that paper propose *"febrile mucositis"* as a more complete frame than "febrile neutropenia," on the grounds that MBI *"creates a port-de-entrée for resident micro-organisms to cause blood stream infections and contributes directly to the occurrence of fever by disrupting highly regulated host-microbe interactions."* This is the best available explanation for why most FN is culture-negative.
9. **Branches A and B converge** — *result in* — **febrile neutropenia**, and when uncontrolled, **sepsis, organ failure, death**.
10. **Branch C (long-term):** cytotoxic exposure also drives **HSC stress-induced premature senescence** (not just apoptosis) and **bone marrow niche perturbation** — mesenchymal stromal injury, elevated intracellular ROS ⚠️ (PMC6114852) — *leads to* — **impaired self-renewal and long-term hematopoietic damage**, distinct from the acute nadir. The literature draws the distinction explicitly: *"If hematopoietic progenitor cells are induced apoptosis and depleted by chemotherapy, acute myelosuppression occurs, but if hematopoietic stem cells undergo senescence with impaired self-renewal ability, long-term damage to the hematopoietic system occurs"* ⚠️.
11. **Branch D (clinical-management feedback loop):** neutropenia → dose delay/reduction → **reduced relative dose intensity** → potentially worse cancer outcomes (§11). The toxicity loops back onto the disease being treated.
12. **Branch E (emerging, model-organism only):** neutropenia may itself be **permissive for metastasis**. ✅ PMID:37538353 (Russo et al., *Oncoimmunology* 2023): cyclophosphamide and doxorubicin — but not cisplatin — increased lung metastatic burden in mice *by inducing neutropenia*; anti-Ly6G neutrophil depletion reproduced the effect, and **G-CSF rescue prevented it**. *"CIN affected the early metastatic colonization of the lung, quite likely promoting the proliferation of tumor cells extravasated into the lung at 24–72 hours."* Strictly `evidence_source: MODEL_ORGANISM`; this is a `HUMAN_MODEL_MISMATCH` candidate, not a human claim.

### The counter-regulatory arm (and how the drugs exploit it)

**G-CSF / CSF3R signaling.** G-CSF (`CSF3`) is *"the major regulator of neutrophil production under basal conditions of hematopoiesis"* and is essential for **"emergency" granulopoiesis** in response to bacterial infection ⚠️. Mechanism: G-CSF binds CSF3R → conformational dimerization aligns Box1/Box2 motifs → recruitment and activation of **JAK1/JAK2/TYK2** → tyrosine phosphorylation → downstream **STAT3** (principal axis in granulocyte-monocyte progenitors), plus **MAPK/ERK, PI3K-AKT-mTOR, SRC-family kinases, NF-κB** ⚠️ PMID:41950547. STAT3 both drives myeloid differentiation and provides negative feedback via **SOCS3**. Therapeutic G-CSF shortcuts the depleted-storage-pool problem by expanding and accelerating the surviving progenitor compartment.

**CDK4/6 dependence — the trilaciclib insight.** HSPCs proliferate in a **CDK4/6-dependent** manner; many tumors (notably SCLC, which is almost universally RB1-deficient) do not. Transient pharmacologic CDK4/6 inhibition therefore *"induces reversible G1-arrest in CDK4/6-dependent cells (such as HSPCs and lymphocytes)"* ⚠️, parking the marrow safely outside S-phase for the duration of chemotherapy exposure while the RB-null tumor keeps cycling into the cytotoxic. It's a beautifully asymmetric trick — like closing the storm shutters on one house while the neighbors' windows stay open, on purpose.

### Ontology suggestions for the pathograph

**Cell types (CL)** 🔍 — verify all before binding:
- neutrophil; granulocyte monocyte progenitor cell; common myeloid progenitor; hematopoietic stem cell; promyelocyte; myeloblast; mesenchymal stem cell of bone marrow (niche); intestinal epithelial cell; oral mucosa epithelial cell

**Biological processes (GO)** 🔍:
- granulocyte differentiation; myeloid cell differentiation; neutrophil chemotaxis; intrinsic apoptotic signaling pathway in response to DNA damage by p53 class mediator; cell cycle arrest / G1/S transition of mitotic cell cycle; cellular senescence; hematopoietic stem cell proliferation; response to oxidative stress; cytokine-mediated signaling pathway; JAK-STAT cascade; innate immune response; defense response to bacterium

**Anatomy (UBERON)** 🔍: bone marrow; blood; oral mucosa; intestinal mucosa; spleen

**Chemicals (CHEBI)** 🔍: docetaxel, doxorubicin, cyclophosphamide, carboplatin, 5-fluorouracil, irinotecan, gemcitabine, topotecan

**`biological_scale` tagging suggestion:** step 2–3 nodes → `MOLECULAR`; steps 4–5 → `CELLULAR`; step 8 mucosal barrier → `TISSUE`; step 9 febrile neutropenia / sepsis → `ORGANISM`. Keep one value per node; if a node wants two, split it.

### Molecular profiling

- **Transcriptomics:** GEO holds numerous marrow and PBMC datasets under chemotherapy; also mouse 5-FU/cyclophosphamide myelosuppression series. **Run `just discover-datasets` and `just verify-datasets` before committing any accession** — and remember that verification proves existence, never relevance.
- **Microbiome:** several strong recent datasets. *"Specific gut microbiota changes heralding bloodstream infection and neutropenic fever during intensive chemotherapy"* (*Leukemia* 2019) ⚠️; gut diversity and resistome as FN outcome biomarkers in pediatric HSCT (*Sci Rep* 2024) ⚠️; AML neutropenic-fever microbiome profiles (*PLOS ONE* 2020) ⚠️.
- **Proteomics / metabolomics / lipidomics:** no established CIN-specific signature located. Record the absence rather than leaving it blank.
- **Functional genomics:** DepMap and CRISPR screens for chemosensitivity determinants exist but are tumor-focused, not marrow-focused.

---

## 7. Anatomical Structures Affected

**Primary organ:** bone marrow (UBERON 🔍) — specifically the hematopoietically active red marrow of the pelvis, sternum, vertebrae, ribs, and proximal long bones. Involvement is **bilateral, diffuse, and systemic**, not focal.

**Secondary organ involvement** (all consequences of failed defense or shared cytotoxic injury):
- Blood — the compartment where the deficit is measured
- Oral cavity and oropharynx — mucositis
- Gastrointestinal tract — mucositis, typhlitis (classically cecum/ascending colon)
- Perianal region — cellulitis
- Lung — pneumonia, invasive aspergillosis
- Skin and vascular access sites — cellulitis, line infection
- Any organ, via hematogenous seeding once bacteremia is established

**Body systems:** hematopoietic and immune (primary); gastrointestinal, integumentary, respiratory (secondary).

**Tissue level:** hematopoietic tissue; stratified squamous and columnar mucosal epithelium; marrow stroma/vasculature (the niche).

**Cell populations targeted:** the mitotic granulocytic progenitor pool preferentially; HSCs at higher/repeated doses; lymphocytes; erythroid and megakaryocytic progenitors (multilineage CIM); intestinal crypt stem cells; marrow mesenchymal stromal cells.

**Subcellular (GO Cellular Component)** 🔍: nucleus (DNA damage); mitochondrion (MOMP, intrinsic apoptosis); spindle/microtubule cytoskeleton (taxane target); specific and azurophil granules (neutrophil function).

**Lateralization:** not applicable — systemic and symmetric.

---

## 8. Temporal Development

**Onset:** acute and predictable, keyed to the infusion. No congenital or age-of-onset concept in the usual sense; the "onset" is pharmacologic. Age *distribution* mirrors who gets chemotherapy — bimodal-ish, with pediatric oncology and a large adult/geriatric mass.

**Within-cycle course (the canonical arc):**
1. Day 0: chemotherapy administered
2. Days 1–4: ANC often transiently *normal or elevated* (storage pool still shipping; steroids and stress demargination can raise it)
3. Days 5–7: descent begins
4. **Days 7–14: nadir** — most regimens days 10–14; docetaxel monotherapy median day 7 ⚠️; some regimens (gemcitabine, carboplatin) run later or biphasic
5. Days 14–21: recovery as surviving progenitors repopulate
6. Day 21: next cycle — assuming recovery is complete, which is the crux of every dose-delay decision

**Duration:** self-limited per cycle in solid-tumor chemotherapy (typically ~5–10 days of grade 3–4). In AML induction and HSCT conditioning, profound neutropenia lasts **weeks**, and duration is the dominant risk multiplier for invasive fungal disease.

**Course pattern:** **episodic and cycle-locked** — the clearest example of a recurrent, treatment-entrained disease course in oncology. Model as `temporality: RECURRENT` (or `TRANSIENT` per episode) rather than `CHRONIC`.

**Progression across cycles:** cumulative marrow injury means nadirs often deepen and recovery slows over successive cycles, especially with alkylators and carboplatin.

**Remission:** treatment-induced (G-CSF) or spontaneous with time. Complete hematologic recovery is the norm; incomplete recovery signals marrow reserve exhaustion, marrow involvement by tumor, or evolving myelodysplasia.

**Critical intervention windows:**
- **Before cycle 1** — because 59% of FN happens there ⚠️. Primary prophylaxis decided before the first dose is the single highest-yield intervention in this whole entry.
- **24–72 h after chemotherapy** — the pegfilgrastim/filgrastim administration window (G-CSF given too close to the cytotoxic can theoretically recruit progenitors into cycle at the worst moment).
- **First hour of fever onset** — "door-to-antibiotic time"; empiric broad-spectrum antibiotics within 60 minutes is the standard-of-care target.

---

## 9. Inheritance and Population

**Inheritance: not applicable.** CIN is acquired and iatrogenic. Do not populate an `inheritance:` block with a Mendelian mode. The heritable component is *pharmacogenomic susceptibility* — model with `genetic:` entries typed `SUSCEPTIBILITY` or `MODIFIER`, and if you want an inheritance concept at all, the honest one is polygenic/multifactorial (HP:0010982 🔍 — verify) with a `description` naming the pharmacogenes. Penetrance, anticipation, germline mosaicism, consanguinity: all not applicable.

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| Drug-induced neutropenia, US | **2.4–15.4 cases per million per year** | ✅ PMID:35552754 |
| Febrile neutropenia, US | **7.8 cases per 1,000 patients with cancer** | ✅ PMID:35552754 |
| Patients with ≥1 FN episode (intermediate-risk regimens, prospective multinational) | **9%** | ⚠️ PMC10570161 |
| FN by cycle | **5%** (cycle 1), **3%** (cycles 2–3), **1%** (cycles 4–6); **59%** of events in cycle 1 | ⚠️ PMC10570161 |
| FN risk, high-risk regimens (TAC etc.) | **>20%** by guideline definition | ⚠️ |
| ED visits for FN resulting in admission | **94%** | ✅ PMID:35552754 |
| Pediatric oncology hospitalizations due to neutropenia/FN | **10.1–22.7%** | ✅ PMID:35552754 |

**For dismech `prevalence:` records**, use the structured slots — `measure_type: ANNUAL_INCIDENCE` for the per-million and per-1,000 figures, `rate_per_100000` normalized (2.4–15.4/million → **0.24–1.54 per 100,000**; 7.8/1,000 cancer patients → **780 per 100,000 cancer patients**, and note the denominator is *cancer patients*, not general population, in `population:`). Never let a per-cycle FN rate and a per-patient FN rate sit in the same comparison.

### Population demographics

- **Sex ratio:** no strong intrinsic sex effect on CIN; observed distributions track underlying cancer epidemiology and body-composition-based dosing.
- **Age:** ≥65 is the consistently replicated high-risk group; pediatric patients have the longest hospitalizations (~8 days, up to $65,000 per admission ✅).
- **Ancestry:** **the Duffy-null issue is the dominant population-genetics finding** — ~66–67% of Black/African American individuals in the US, and high frequency in Middle Eastern populations. It affects *measured* ANC, trial eligibility (~10% lower ✅), and dose-modification decisions, without affecting infection risk. `NUDT15` variant frequencies are highest in East Asian populations; `DPYD` variant spectra differ substantially by ancestry (HapB3 is European-enriched; several African-ancestry-relevant variants are under-tested by standard panels).
- **Geography:** the burden distribution is a healthcare-access story, not a biology story — G-CSF availability and cost determine outcomes far more than any regional biological variation.

---

## 10. Diagnostics

**Diagnosis is a lab value plus a thermometer.** There's no imaging finding, no biopsy, no genetic test that makes the diagnosis.

### Core tests

- **Complete blood count with differential** → absolute neutrophil count. ANC = WBC × (% segmented neutrophils + % bands). LOINC 🔍: search "Neutrophils [#/volume] in Blood by Automated count" — resolve before binding.
- **Temperature measurement** — oral, per the FN definition.
- **Blood cultures** — at least two sets, from peripheral vein and each lumen of any central line, before antibiotics.
- Site-directed cultures: urine, stool (if diarrhea), sputum, wound, CSF if indicated.
- CMP, LFTs, lactate, CRP/procalcitonin (adjunctive, not diagnostic).
- **Chest imaging** — CXR; **high-resolution chest CT** if prolonged neutropenia or fungal concern (the halo sign in invasive aspergillosis).
- Serum galactomannan / β-D-glucan for invasive fungal surveillance in high-risk hematologic patients.
- **Bone marrow biopsy** — *not* routine for CIN. Reserved for unexplained, prolonged, or non-recovering cytopenias where marrow involvement or a therapy-related myeloid neoplasm is the question.

### Reference ranges (for a `Biochemical` entry with `interpretation_bands`)

Adult ANC, conventional: **1500–8000/µL** (LLN commonly 1500). But the Duffy-null finding means a single population-wide interval is wrong for a third of some populations. If you curate `reference_ranges`, add a **`population:`-stratified** pair:

- Duffy non-null adults: **2000–7500/µL** ✅ PMID:41158990
- Duffy-null adults: **1200–1540/µL** ✅ PMID:41158990

and then `interpretation_bands` mapping ANC <1500 / <1000 / <500 / <100 to the CTCAE tiers — **stating the version**, since v5 and v6 disagree (§3). This is exactly the graded-category case the `interpretation_bands` slot exists for, and the CKD-MBD entry is the pattern to copy.

### Genetic testing

Not diagnostic for CIN, but **predictive and increasingly standard**:
- **`DPYD` genotyping before fluoropyrimidines** — mandated pre-treatment in the EU; CPIC guideline-backed
- **`UGT1A1` before irinotecan** (especially at high dose or in FOLFIRINOX)
- **`TPMT` and `NUDT15` before thiopurines** — CPIC guideline-backed
- Pre-emptive multi-gene PGx panels ⚠️ (PMC8827955 describes implementation)
- WGS/WES/CMA/karyotype/FISH/mtDNA/repeat-expansion testing: **not applicable**
- `ACKR1` (rs2814778) genotyping or Duffy phenotyping: increasingly proposed to avoid misclassifying DANC as pathologic neutropenia ⚠️ (*Am J Hematol* 2025, "Diagnosis of Duffy Null-Associated Neutropenia During Chemotherapy")

### Clinical criteria and risk stratification

- **FN definition** (IDSA): as in §3
- **MASCC Risk Index** — 7 clinical factors at fever onset; score **<21 = high risk**. Internationally validated ⚠️
- **CISNE** (Clinical Index of Stable Febrile Neutropenia) — designed for *apparently stable* patients; in head-to-head work CISNE-I had **sensitivity 0.22 / specificity 0.91** vs MASCC low-risk **sensitivity 0.95 / specificity 0.17** ⚠️ PMID:31864874. The two are answering different questions: MASCC casts a wide net, CISNE is a stricter filter for who can genuinely go home. Validated in gynecologic oncology ⚠️ PMID:34504931. A sober JCO OP commentary is titled *"Risk-Stratifying Treatment Strategies for Febrile Neutropenia—Tools, Tools Everywhere, and Not a Single One That Works?"* ⚠️ — worth citing for honest uncertainty.
- **Lyman model** and similar multivariable models predict FN risk before cycle 1 to guide primary prophylaxis.

### Differential diagnosis

| Alternative | Distinguishing feature |
|---|---|
| Duffy-null associated neutrophil count (DANC) | Chronic, pre-treatment baseline; no infection history; `ACKR1` rs2814778 homozygous — **not a toxicity** |
| Marrow infiltration by tumor | Non-recovering counts; leukoerythroblastic film; biopsy |
| Therapy-related MDS / AML | Late, progressive, dysplastic morphology, cytogenetic/molecular abnormalities |
| Drug-induced immune agranulocytosis (non-chemo: clozapine, methimazole, ticlopidine) | Idiosyncratic, not dose-predictable, no nadir timing |
| Viral suppression (HIV, EBV, CMV, parvovirus B19) | Serology/PCR |
| Sepsis-associated neutropenia | Consumption rather than production failure |
| Autoimmune neutropenia (HP:0001904 ✅) | Anti-neutrophil antibodies |
| Nutritional (B12, folate, copper) | Macrocytosis, low levels |
| Hypersplenism | Splenomegaly, multilineage |

### Screening

- **Pre-treatment CBC and risk assessment** before every cycle — the operational screen
- **Pre-treatment pharmacogenomic screening** for `DPYD`/`UGT1A1`/`TPMT`/`NUDT15`
- No population-level screening program; not a newborn-screening or carrier-screening concept

---

## 11. Outcome / Prognosis

### Mortality ✅ (all from PMID:35552754)

| Population | In-hospital mortality (neutropenia/FN) |
|---|---|
| Pediatric oncology | **0.4–3.0%** |
| Adults, solid tumors | **2.6–7.0%** |
| Adults, hematologic malignancies | **7.4%** |

### Morbidity and burden ✅

- Average hospital LOS: **~6 days (elderly), ~8 days (children), up to 10 days (adults)**
- Per-hospitalization cost: **up to $15,000 (elderly), $40,000 (adults), $65,000 (children)**
- Total annual US cost (2012): **>$2 billion for adults, up to $880 million for children**
- **94%** of FN emergency-department visits end in admission

### Complications

Bacteremia and sepsis; septic shock; invasive fungal disease; typhlitis; ARDS (notably viridans streptococcal); prolonged hospitalization; central line loss; C. difficile colitis; and the treatment-level complication — **dose delay and dose reduction**.

### Recovery

Complete hematologic recovery is the rule for a single cycle. The prognostically important question is whether it recovers *in time* for the next cycle.

### The dose-intensity paradox — the most important prognostic content in this entry

Two findings sit in tension and both are real:

**(a) Reduced relative dose intensity (RDI) is associated with worse cancer survival.** RDI **≥85%** is the conventional threshold for early breast cancer ⚠️; a systematic review and meta-analysis found RDI associated with survival in advanced solid tumors ⚠️ PMID:33973301; the early-breast-cancer/aggressive-lymphoma analysis is ⚠️ PMID:20227889. Older age, obesity, and FN itself are associated with reduced RDI ⚠️.

**(b) Experiencing neutropenia is associated with *better* survival.** A meta-analysis of **13 trials, 9,528 patients** found a hazard ratio of death of **0.69 (95% CI 0.64–0.75)** for patients with higher-grade neutropenia/leukopenia versus lower-grade or none ⚠️ PMID:20960191. Grade ≥3 neutropenia on **day 8 of cycle 1** in mCRPC docetaxel: 1-year OS **81% vs 68%** ⚠️.

These reconcile if you read neutropenia as a **pharmacodynamic dosimeter** — a readout that the patient actually received a biologically active exposure. As one gastric-cancer analysis puts it, *"the absence of such toxicity indicates that the dosages of drugs are not pharmacologically adequate"* ⚠️. But the inference has an obvious confounding hazard (patients who survive long enough to have cycle-1 toxicity, patients with better organ function, immortal-time bias in some designs). **Curate this as `SUPPORT` + `directness: INDIRECT`, and put a `discussions:` entry with `kind: KNOWLEDGE_GAP` on whether the association is causal or a marker of exposure.** Do not let the entry imply that inducing neutropenia is therapeutic.

### Long-term

**Therapy-related myeloid neoplasms:** up to **2.3%** of autologous-HSCT recipients at median **2.6 years**; risk factors age ≥60, male sex, radiotherapy, ≥3 prior lines, graft cellularity; post-aHSCT tMN enriched for `PPM1D` and `TP53` lesions with shorter latency and worse OS; CH-derived tMN does worse than non-CH-derived ⚠️ (*Leukemia* 2024, PMC11147764).

### Prognostic factors

MASCC and CISNE scores; ANC nadir depth; **duration of neutropenia** (the strongest predictor of invasive fungal disease); documented bacteremia; hemodynamic instability; comorbidity burden; age; hematologic vs solid malignancy; time-to-antibiotic.

---

## 12. Treatment

### Prophylaxis — the main event

**Colony-stimulating factors (G-CSF).** The current authority is ✅ **PMID:41740078 — "WBC Growth Factors: ASCO Guideline Update," *J Clin Oncol* 2026**, which replaces the 2015 version following a systematic review of RCTs and meta-analyses published **September 2014 – August 2025**. Core recommendation, quoted: *"Prophylactic use of CSFs to reduce the risk of febrile neutropenia is warranted when the risk...is approximately 20% or higher."* For regimens with **<20%** risk, primary prophylaxis may still be warranted based on **age, medical history, or disease characteristics** ⚠️. Named acceptable agents: **filgrastim, pegfilgrastim, eflapegrastim, and biosimilars** ✅.

Agents and suggested NCIT bindings:

| Agent | `therapeutic_modality` | `treatment_term` | `therapeutic_agent` NCIT/CHEBI |
|---|---|---|---|
| Filgrastim (short-acting G-CSF) | `PROTEIN_REPLACEMENT` or `PEPTIDE` (judgement call; it's a recombinant cytokine) | NCIT:C15986 Pharmacotherapy | 🔍 NCIT filgrastim |
| Pegfilgrastim | as above | NCIT:C15986 | **NCIT:C123927** ✅ (Pegfilgrastim Anti-neutropenic Factor) or 🔍 the base pegfilgrastim term |
| Pegfilgrastim biosimilars | — | NCIT:C15986 | **NCIT:C104005** ✅ (LA-EP2006); others 🔍 |
| **Eflapegrastim** (Rolvedon, FDA 2022) | — | NCIT:C15986 | **NCIT:C103856** ✅ |
| **Efbemalenograstim alfa** (Ryzneuta, FDA **22 Nov 2023**; China 6 May 2023) | — | NCIT:C15986 | 🔍 — a *dimeric G-CSF-Fc fusion without PEGylation or polysorbate 80* ⚠️ PMID:37368138 |
| Lipegfilgrastim | — | NCIT:C15986 | **NCIT:C101778** ✅ |
| Pegteograstim / Empegfilgrastim / Mecapegfilgrastim | — | NCIT:C15986 | **NCIT:C128891 / C134829 / C170155** ✅ |
| **Trilaciclib** (Cosela, FDA **12 Feb 2021**) | `SMALL_MOLECULE` | NCIT:C15986 or NCIT:C93352 Targeted Therapy | 🔍 NCIT trilaciclib |

Eflapegrastim efficacy signal: severe neutropenia in cycle 1 **15.8% vs 24.3%** for pegfilgrastim ⚠️.

**Trilaciclib.** First-in-class CDK4/6 inhibitor given **before** chemotherapy for myeloprotection in ES-SCLC. Pivotal evidence: ✅ PMID:31504118 (*Ann Oncol* 2019, phase Ib/randomized II, 94 patients, trilaciclib + etoposide/carboplatin) — grade ≥3 AEs **50% vs 83.8%**, improvements across neutrophil, RBC, and lymphocyte measures, comparable antitumor efficacy, no trilaciclib-related grade ≥3 AEs. Pooled phase 2 analysis ✅ PMID:34408488 (123 trilaciclib vs 119 placebo; NCT02499770, NCT03041311, NCT02514447) — myeloprotection across age groups, greater in patients **≥65**, with improved QoL and on-schedule chemotherapy delivery. `target_mechanisms` should point at the progenitor-apoptosis node with a `MODULATES`/preventive framing.

**Plinabulin** (investigational). PROTECTIVE-2 phase 3 (n=221, TAC q21d, plinabulin 40 mg day 1 + pegfilgrastim 6 mg day 2 vs pegfilgrastim alone): grade 4 CIN prevention in cycle 1 **31.5% vs 13.6%, P = .0015** ⚠️. FDA breakthrough designation Sept 2020 ⚠️. **Not FDA-approved** — curate as investigational and do not imply availability.

**Antimicrobial prophylaxis.** Fluoroquinolone prophylaxis is considered for high-risk patients with expected prolonged profound neutropenia (classically ANC <100/µL for >7 days), balanced against resistance selection and C. difficile risk. Antifungal (posaconazole) and anti-PJP (TMP-SMX) prophylaxis per risk group. This area is genuinely contested — use `MODULATES`-style hedging, not causal predicates.

### Treatment of established febrile neutropenia

- **Empiric broad-spectrum IV antibiotics within 60 minutes**, after cultures. IDSA monotherapy options: an antipseudomonal β-lactam (**cefepime**), a **carbapenem** (meropenem, imipenem-cilastatin), or **piperacillin-tazobactam** ⚠️ (IDSA 2010 update, *Clin Infect Dis* 2011;52:e56).
- Add vancomycin, aminoglycoside, and/or fluoroquinolone for hypotension, pneumonia, suspected line infection, or known resistance ⚠️.
- Continue *"until ANC recovery is imminent"* or until a specific infection dictates otherwise ⚠️.
- Empiric antifungal therapy for persistent fever beyond 4–7 days in high-risk patients.
- **Outpatient oral management** (ciprofloxacin + amoxicillin-clavulanate) for carefully selected low-risk patients — ASCO/IDSA outpatient guideline ⚠️ (*JCO OP* 2018).
- **Therapeutic G-CSF** in established FN: guidelines generally do not recommend routine addition, reserving it for high-risk features. In AML induction specifically, a JSCO systematic review found G-CSF *"significantly shortened the duration of neutropenia"* but *"did not correlate with infection-related mortality and did not affect disease progression/recurrence or overall survival"* ⚠️ (PMC11043120). That's an important negative and belongs in the entry.
- **Granulocyte transfusion** — salvage only; evidence weak.
- Supportive care: NCIT:C15747 Supportive Care; hydration, antipyretics, source control, line removal.

### Treatment-strategy content

- Dose reduction / cycle delay — effective at reducing FN but see the RDI paradox (§11)
- Regimen substitution to a lower-myelotoxicity option
- Genotype-guided dosing: CPIC `DPYD`, `UGT1A1`, `TPMT`/`NUDT15` — the personalized-medicine arm of this entry
- Duffy-informed ANC thresholds so that DANC patients are not needlessly dose-reduced ⚠️

### Adverse effects of the treatments

G-CSF: bone pain (very common), splenic rupture (rare), ARDS (rare), capillary leak; theoretical concern about stimulating CSF3R-expressing myeloid malignancies. Trilaciclib: fatigue, hypocalcemia, hypokalemia, headache, injection-site reactions. Broad-spectrum antibiotics: C. difficile, resistance selection, microbiome collapse (which loops back to §6, branch B — the treatment feeds the mechanism).

---

## 13. Prevention

**Primary prevention** (stop the neutropenia happening):
- FN risk assessment **before cycle 1**, using regimen risk + patient factors (Lyman-type model)
- **G-CSF primary prophylaxis at the ≥20% threshold** ✅ PMID:41740078
- Trilaciclib in ES-SCLC receiving platinum/etoposide or topotecan
- Regimen selection favoring lower myelotoxicity where efficacy-equivalent
- Pre-emptive pharmacogenomic dosing (`DPYD`, `UGT1A1`, `TPMT`, `NUDT15`)
- Dental evaluation and source control before starting therapy

**Secondary prevention** (stop the neutropenia becoming a catastrophe):
- CBC monitoring around the expected nadir
- **Secondary G-CSF prophylaxis** after a prior FN episode or dose-limiting neutropenia
- Patient education: the thermometer protocol — take a temperature for any chills or malaise, call at ≥38 °C, do not take antipyretics that mask it
- Antimicrobial prophylaxis in the high-risk subset

**Tertiary prevention:**
- Door-to-antibiotic ≤60 minutes
- Risk-stratified admission via MASCC/CISNE
- Central line care bundles
- Antifungal surveillance in prolonged neutropenia

**Immunization:** inactivated influenza and COVID-19 vaccines are recommended in chemotherapy patients (ideally timed away from nadir); pneumococcal per risk. **Live vaccines contraindicated.** These prevent *infection*, not neutropenia — keep the distinction in the entry.

**Behavioral / public health:** hand hygiene; food-safety precautions; avoiding sick contacts and crowds during nadir; the "neutropenic diet" is **not** supported by evidence and has been de-implemented in most centers — worth curating explicitly as a refuted intervention with `supports: REFUTE` if a suitable citation is obtained.

**Genetic counseling:** not applicable in the reproductive sense; pharmacogenomic counseling is the analogue.

---

## 14. Other Species / Natural Disease

**There is no natural disease here** — CIN cannot occur without an anthropogenic exposure. But there are two genuine cross-species angles:

**Veterinary iatrogenic CIN.** Dogs (**NCBITaxon:9615** 🔍) and cats (**NCBITaxon:9685** 🔍) receiving veterinary chemotherapy (doxorubicin, vincristine, cyclophosphamide, lomustine, carboplatin) develop dose-limiting neutropenia with nadir timing that differs by agent — lomustine and carboplatin notably later. Canine lymphoma CHOP protocols are the highest-volume setting. This is a real clinical entity in veterinary oncology and evidence from it grades as `evidence_source: MODEL_ORGANISM` per dismech rules (veterinary observations in non-human mammals). **Breed effects are real and mechanistically interesting**: `ABCB1` (MDR1) nt230(del4) in Collies and related herding breeds (VBO 🔍) causes profound sensitivity to P-glycoprotein substrates including vincristine and doxorubicin — a genuine veterinary pharmacogenomic parallel to the human `DPYD` story, and worth a `genetic:` or comparative note. Search **OMIA** for the `ABCB1` entry to get a citable identifier.

**Evolutionary conservation.** Granulopoiesis, CSF3/CSF3R signaling, and p53/PUMA-mediated progenitor apoptosis are conserved across vertebrates, which is why the mouse models in §15 work at all. Orthologs: `Csf3r`, `Trp53`, `Bbc3` (mouse); `csf3r`, `tp53` (zebrafish) — NCBI Gene IDs 🔍.

**Zoonotic potential / cross-species transmission:** not applicable.

---

## 15. Model Organisms

Because the initiating lesion is a drug, CIN is **unusually easy to model** — you give the animal the drug. That makes it one of the better-supported iatrogenic conditions for `animal_models:` curation.

### Mammalian induced models

| Model | Induction | Phenotype recapitulation | Limitations |
|---|---|---|---|
| **Mouse, 5-FU myeloablation** | Single **150 mg/kg** 5-FU i.p. → *"severe neutropenia lasting from days 3 to 11 post-injection; 5-FU-treated mice achieve normal ANC levels by days 12 to 14"* ⚠️ | Recapitulates nadir–recovery arc with quantitatively similar kinetics; workhorse for G-CSF and myeloprotectant testing | Single-dose, not cyclic; murine neutrophil biology differs (mice are lymphocyte-predominant, humans neutrophil-predominant); no tumor in most designs |
| **Mouse, cyclophosphamide** | e.g. 200 mg/kg i.p. ✅ PMID:37538353 | Neutropenia + the metastasis-permissive phenotype | **Strain-dependent susceptibility** — *"there are differences in susceptibility to neutropenia after cyclophosphamide treatment between inbred strains"* ⚠️, which is both a limitation and a genetic-mapping opportunity |
| **Mouse, doxorubicin** | 10 mg/kg i.v. ✅ PMID:37538353 | Neutropenia; increased artificial lung metastasis | — |
| **Mouse, cisplatin (negative control)** | 10 mg/kg i.v. ✅ | **Does NOT** produce the effect — a built-in specificity control | Its value *is* the negative result |
| **Anti-Ly6G antibody depletion** | Immunologic, not cytotoxic | Isolates the neutropenia variable from all other chemotherapy effects ✅ PMID:37538353 | Depletes mature neutrophils only; does not model progenitor loss or marrow injury |
| **Mouse, cytarabine** | — | Used in BB-10010 (MIP-1α analog) chemoprotection studies ⚠️ | — |
| ***Puma*-null / *Trp53*-null mice** | Genetic | Protected from HSPC apoptosis after irradiation/genotoxic stress ⚠️ | Establishes the mechanism (§6 step 3) but is a *protection* model, not a disease model |

**The exemplar link to curate** — Russo et al. ✅ PMID:37538353 is the strongest single `animal_models` entry available here, because it has all four `ModelMechanismLink` components in one paper:

```
animal_models:
- name: Cyclophosphamide-induced neutropenia in Renca/LLC-bearing mice
  species: Mouse
  publication: PMID:37538353
  modeled_mechanisms:
  - target: <your neutropenia node's bare name>
    relationship: RECAPITULATES
    fidelity: MODERATE
    limitations: >-
      Single high-dose administration rather than cyclic human dosing; murine
      neutrophil biology and marrow reserve differ from human; the metastasis
      readout has no confirmed human counterpart.
    readouts:
    - name: Circulating neutrophil count
      target: <same bare name>
      direction: DECREASED
      ...
```

Note the anti-Ly6G arm and the **G-CSF rescue arm** (which *prevented* the metastasis phenotype) are natural `PERTURBS` and `RESCUES` links respectively — a rare chance to use three relationship values from one paper.

### Other systems

- **Zebrafish** — transparent larvae with fluorescent neutrophil reporters (`mpx:GFP`, `lyz:DsRed`) allow live imaging of granulopoiesis and chemotoxic depletion. Useful for screening; poor for marrow-niche biology (no long-bone marrow).
- **In vitro:** human CD34+ HSPC colony-forming assays (CFU-GM) are the classic myelotoxicity readout; ex vivo bone marrow cultures; iPSC-derived hematopoietic differentiation. **These are `experimental_models:` (non-animal), not `animal_models:`.**
- **Bone-marrow-on-a-chip** — emerging NAM (new approach methodology) for chemotherapy myelotoxicity prediction; a good `experimental_models` candidate with `experimental_model_type` set appropriately.
- **Computational:** semi-mechanistic PK-PD models of the neutrophil lifecycle (Friberg-type myelosuppression models, with proliferation, transit compartments, and feedback) are widely used for dose optimization and are strong `computational_models:` candidates with `modeled_mechanisms` links to the progenitor and storage-pool nodes.

**Model databases:** MGI, IMPC, KOMP, IMSR, MMRRC (mouse); ZFIN (zebrafish); Cellosaurus/ATCC (lines); OMIA (veterinary).

---

## Curation notes for the dismech entry

A few things I'd flag before anyone starts writing YAML:

1. **The MONDO gap is the first decision.** No MONDO term for chemotherapy-induced neutropenia resolved via OLS. Anchor on `MONDO:0001475` with `skos:narrowMatch`, record the gap, and consider whether this is better modeled as a `kb/modules/` **mechanism module** than a disease entry — "cytotoxic myelosuppression" recurs across every myelosuppressive drug toxicity entry the KB will ever have, and the treatment-toxicity module family already exists for exactly this shape of thing. Run `just list-modules` and grep `kb/modules` for "myelosuppression" and "neutropenia" before deciding; a module here would let anthracycline, taxane, and platinum toxicity entries all `conforms_to` one chain instead of re-deriving it.
2. **Every "grade 3/4 neutropenia" number needs a CTCAE version stamp.** v6 (2025) moved all four boundaries. A rate quoted from a 2019 trial and one from a 2026 trial are not the same measurement.
3. **The dose-intensity paradox needs a `discussions:` entry**, not a confident causal claim in either direction.
4. **The Russo metastasis finding is `MODEL_ORGANISM` only** and is a textbook `HUMAN_MODEL_MISMATCH` candidate.
5. **Verify every ⚠️ PMID with `just fetch-reference`** before quoting. The exact-substring rule is unforgiving, and several of the quotes above came from search-result summaries that may have paraphrased. My own memory file on this (`preverify-snippets-before-writing-yaml`) exists because a blocked Write is a silent no-op.
6. **Duffy/`ACKR1` deserves its own curated thread** through `genetic:`, `reference_ranges` (population-stratified), and probably a `notes:` line in diagnostics. It's the most consequential recent development in this space and it's an equity finding as much as a biology one.

---

## Sources

- [Chemotherapy-Induced Neutropenia and Febrile Neutropenia in the US: A Beast of Burden That Needs to Be Tamed? — *The Oncologist* 2022 (PMID:35552754)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9355811/)
- [WBC Growth Factors: ASCO Guideline Update — *JCO* 2026 (PMID:41740078)](https://ascopubs.org/doi/10.1200/JCO-25-02938)
- [A paradigm shift in neutrophil adverse event grading: Why now? — *HemaSphere* 2025 (PMID:41158990)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12558435/)
- [Chemotherapy-induced neutropenia elicits metastasis formation in mice — *Oncoimmunology* 2023 (PMID:37538353)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10395252/)
- [Mucosal barrier injury, fever and infection in neutropenic patients with cancer: introducing the paradigm febrile mucositis — *Br J Haematol* 2014 (PMID:25196917)](https://pubmed.ncbi.nlm.nih.gov/25196917/)
- [Myelopreservation with the CDK4/6 inhibitor trilaciclib — *Ann Oncol* 2019 (PMID:31504118)](https://pubmed.ncbi.nlm.nih.gov/31504118/)
- [Myeloprotective Effects of Trilaciclib, pooled phase 2 — *Cancer Manag Res* 2021 (PMID:34408488)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8363477/)
- [Chemotherapy-induced neutropenia and emerging agents for prevention and treatment — *Cancer Treat Rev* 2022](https://www.cancertreatmentreviews.com/article/S0305-7372(22)00091-3/fulltext)
- [Early neutropenia on day 8 with docetaxel: mechanisms within the neutrophil pool system](https://pmc.ncbi.nlm.nih.gov/articles/PMC6472781/)
- [Neutrophil kinetics in health and disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2930213/)
- [A prospective, real-world, multinational MASCC study of febrile neutropenia occurrence](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10570161/)
- [Meta-analysis of neutropenia or leukopenia as a prognostic factor (PMID:20960191)](https://pubmed.ncbi.nlm.nih.gov/20960191/)
- [Relative Dose Intensity and Survival in Advanced Solid Tumors: Systematic Review and Meta-Analysis (PMID:33973301)](https://pubmed.ncbi.nlm.nih.gov/33973301/)
- [CISNE versus MASCC: Identifying low risk febrile neutropenic patients (PMID:31864874)](https://pubmed.ncbi.nlm.nih.gov/31864874/)
- [Risk-Stratifying Treatment Strategies for Febrile Neutropenia — *JCO OP*](https://ascopubs.org/doi/10.1200/OP.21.00148)
- [IDSA Clinical Practice Guideline for Antimicrobial Agents in Neutropenic Patients with Cancer: 2010 Update](https://academic.oup.com/cid/article/52/4/e56/382256)
- [Outpatient Management of Fever and Neutropenia in Adults — ASCO/IDSA Guideline Update](https://ascopubs.org/doi/10.1200/JOP.18.00016)
- [Efbemalenograstim Alfa: First Approval — *Drugs* 2023 (PMID:37368138)](https://pubmed.ncbi.nlm.nih.gov/37368138/)
- [FDA Approves Trilaciclib to Reduce Chemotherapy-Induced Myelosuppression (Feb 2021)](https://www.ons.org/publications-research/voice/news-views/02-2021/fda-approves-trilaciclib-reduce-chemotherapy-induced)
- [PROTECTIVE-2 meets primary endpoint of preventing grade 4 neutropenia (plinabulin)](https://www.cancernetwork.com/view/protective-2-study-meets-primary-end-point-of-preventing-grade-4-neutropenia)
- [Absolute neutrophil count by Duffy status among healthy Black and African American adults — *Blood Advances* 2023](https://ashpublications.org/bloodadvances/article/7/3/317/486360/Absolute-neutrophil-count-by-Duffy-status-among)
- [Diagnosis of Duffy Null-Associated Neutropenia During Chemotherapy — *Am J Hematol*](https://onlinelibrary.wiley.com/doi/10.1002/ajh.27679)
- [Dana-Farber: cancer trial criteria disadvantage patients of African and Middle Eastern ancestry (2024)](https://www.dana-farber.org/newsroom/news-releases/2024/criteria-for-cancer-clinical-trials-and-treatment-regimens-place-patients-of-african-and-middle-eastern-ancestry-at-a-disadvantage-due-to-natural-blood-test-variability-study-finds)
- [Duffy-null Associated Neutrophil Count (DANC) — ASH](https://www.hematology.org/education/danc)
- [GWAS of chemotherapeutic agent-induced severe neutropenia/leucopenia, Biobank Japan (PMID:23648065)](https://pubmed.ncbi.nlm.nih.gov/23648065/)
- [GWAS of myelosuppression in NSCLC with platinum-based chemotherapy (PMID:25823687)](https://pubmed.ncbi.nlm.nih.gov/25823687/)
- [Impact of UGT1A1 Polymorphisms on Febrile Neutropenia in FOLFIRINOX](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8909027/)
- [Modern Developments in Germline Pharmacogenomics for Oncology Prescribing](https://pmc.ncbi.nlm.nih.gov/articles/PMC9262778/)
- [Deletion of Puma protects hematopoietic stem cells — *Blood* 2010](https://ashpublications.org/blood/article/115/17/3472/27128/Deletion-of-Puma-protects-hematopoietic-stem-cells)
- [Chemotherapy-induced niche perturbs hematopoietic reconstitution](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6114852/)
- [CSF3R signalling beyond granulopoiesis (PMID:41950547)](https://pubmed.ncbi.nlm.nih.gov/41950547/)
- [G-CSF and its receptor in myeloid malignancy — *Blood*](https://ashpublications.org/blood/article/115/25/5131/27070/G-CSF-and-its-receptor-in-myeloid-malignancy)
- [Specific gut microbiota changes heralding bloodstream infection and neutropenic fever — *Leukemia* 2019](https://www.nature.com/articles/s41375-019-0547-0)
- [Gut diversity and resistome as biomarkers of febrile neutropenia outcome — *Sci Rep* 2024](https://www.nature.com/articles/s41598-024-56242-8)
- [Clonal hematopoiesis-derived therapy-related myeloid neoplasms after autologous HSCT — *Leukemia* 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11147764/)
- [Primary prophylaxis with G-CSF after AML induction: JSCO systematic review and meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11043120/)
- [Risk of febrile neutropenia with docetaxel/cyclophosphamide: meta-analysis (PMID:26337685)](https://pubmed.ncbi.nlm.nih.gov/26337685/)
- [Protective effects of BB-10010 on chemotherapy-induced neutropenia in mice — *Exp Hematol*](https://www.exphem.org/article/S0301-472X(98)00052-6/fulltext)
- [Febrile Neutropenia — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK541102/)
- [EBI Ontology Lookup Service (OLS4) — used for all ✅-marked term resolutions](https://www.ebi.ac.uk/ols4/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 15 |
| References weighed for topical relevance | 22 |
| On topic | 10 |
| Off topic | 0 |

22 of 37 references resolved; the rest could not be looked up either way.
