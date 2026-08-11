---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-29T11:04:57.711032'
end_time: '2026-06-29T11:09:45.145543'
duration_seconds: 287.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lymphangioleiomyomatosis
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8[1m]
  web_search_requests: 10
  num_turns: 12
  total_cost_usd: 2.207513
  session_id: f68515d5-0aa0-4075-bf9a-44c8e65be8f3
  stop_reason: end_turn
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymphangioleiomyomatosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Lymphangioleiomyomatosis** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Comprehensive Research Report: Lymphangioleiomyomatosis (LAM)

> **Scope note for the knowledge-base curator:** Citations below give PMIDs/PMC IDs and source URLs gathered from current literature. Per the dismech evidence SOP, every PMID and snippet must be re-fetched with `just fetch-reference` and substring-verified against the real abstract before it is committed as an `EvidenceItem`. Where I quote abstract text it is marked as a direct quote, but treat all quotes as *leads to verify*, not pre-validated snippets. Several PMIDs are flagged "verify" where I am reconstructing them from memory rather than from the search payload.

---

## 1. Disease Information

**Overview.** Lymphangioleiomyomatosis (LAM) is a rare, slowly progressive, low-grade neoplastic (metastasizing) disease that almost exclusively affects women, typically in their reproductive years. It is characterized by diffuse cystic destruction of the lung parenchyma, abnormal proliferation of immature smooth-muscle-like "LAM cells" along lymphatics, airways, and blood vessels, and a strong association with renal angiomyolipomas (AMLs) and chylous (lymphatic) effusions. It is now understood as a **member of the PEComa family (perivascular epithelioid cell tumors)** and behaves like a low-grade, hormonally responsive, metastasizing neoplasm — a "benign metastasizing" tumor of the lung ("a wolf in sheep's clothing," JCI 2012, https://www.jci.org/articles/view/58709).

Two clinical contexts exist:
- **Sporadic LAM (S-LAM):** arises from somatic *TSC2* mutations; not inherited.
- **TSC-LAM:** occurs in patients with the germline disorder Tuberous Sclerosis Complex (TSC); affects up to 30–40% of adult women with TSC (and is detectable on CT in a substantial fraction of men with TSC, though usually asymptomatic).

**Key identifiers:**
- **MONDO:** MONDO:0011705 (https://monarchinitiative.org/MONDO:0011705)
- **OMIM:** #606690 — "LYMPHANGIOLEIOMYOMATOSIS; LAM" (https://omim.org/entry/606690)
- **Orphanet:** ORPHA:538
- **MedGen:** C0751674
- **ICD-10:** J84.81 (Lymphangioleiomyomatosis); **ICD-11:** CB04.1 / under interstitial lung diseases (also coded among rare cystic lung diseases)
- **MeSH:** D018192 "Lymphangioleiomyomatosis"
- **NCIT:** C3725 (Lymphangioleiomyomatosis)
- **Related upstream gene disorders:** TSC1 (OMIM 605284), TSC2 (OMIM 191092); Tuberous Sclerosis (OMIM 191100/613254)

**Synonyms / alternative names:** Lymphangiomyomatosis; LAM; pulmonary lymphangioleiomyomatosis; lymphangiomyoma; sporadic lymphangioleiomyomatosis (S-LAM); tuberous-sclerosis–associated LAM (TSC-LAM). (Note: "lymphangiomyomatosis" is the legacy OMIM/ClinVar spelling.)

**Data derivation:** Disease-level resource (aggregated). LAM knowledge derives from disease-level registries and natural-history cohorts (NHLBI LAM Registry, the LAM Foundation registry, Japanese national insurance-claims database, ERS/ATS guideline cohorts) rather than single-patient EHR records.

Sources: OMIM 606690 (https://omim.org/entry/606690); Monarch MONDO:0011705; StatPearls (https://www.ncbi.nlm.nih.gov/books/NBK534231/); clinical review, *Breathe* 2020 (https://publications.ersnet.org/content/breathe/16/2/200007); PMC7714539 (https://pmc.ncbi.nlm.nih.gov/articles/PMC7714539/).

---

## 2. Etiology

**Primary cause — genetic/mechanistic.** LAM is caused by **biallelic inactivation of the tumor-suppressor genes *TSC1* (9q34, encoding hamartin) or, far more commonly, *TSC2* (16p13.3, encoding tuberin)**. Loss of the TSC1–TSC2–TBC1D7 complex (a GTPase-activating complex for the small GTPase RHEB) leads to **constitutive activation of mTOR complex 1 (mTORC1)**, driving inappropriate cell growth, proliferation, survival, and lymphangiogenesis.

- In **sporadic LAM**, LAM cells carry **somatic** *TSC2* mutations plus loss of heterozygosity (LOH) at the second allele (two-hit Knudson mechanism). LOH at chromosome 16p13 (the *TSC2* locus) is detectable in pulmonary LAM cells, lymph-node LAM cells, and angiomyolipoma cells (Carsillo, Astrinidis & Henske, *PNAS* 2000 — PMID:10737804, *verify*; "Angiomyolipoma cells and pulmonary LAM cells from sporadic LAM patients contain inactivating mutations in the *TSC2* gene that arose somatically").
- In **TSC-LAM**, one *TSC1/TSC2* allele is mutated in the germline; a somatic second hit occurs in the LAM cell.
- A **metastatic ("benign metastasis") model** is strongly supported: identical *TSC2* mutations are found across spatially separate lesions, and recurrent LAM in transplanted donor lungs has been shown by genetic analysis to derive from **recipient** cells (Karbowniczek et al., *Am J Respir Crit Care Med* 2003, https://www.atsjournals.org/doi/full/10.1164/rccm.200208-969OC — "cells in recurrent LAM lesions in donor lungs … derive from the recipient rather than from the allografts").

**Risk factors:**
- **Female sex** — overwhelmingly the dominant risk factor; near-exclusive female predominance.
- **Reproductive-age / hormonal status** — onset and progression cluster in the premenopausal period; estrogen is a key disease driver (see §5).
- **Germline *TSC1/TSC2* mutation (Tuberous Sclerosis Complex)** — strongest *genetic* risk factor; TSC raises LAM risk dramatically.
- **Family history** — only relevant via TSC (sporadic LAM is not heritable).
- **Pregnancy and exogenous estrogen** — associated with accelerated progression and pneumothorax risk in observational data; estrogen-containing contraceptives are generally cautioned against.

**Protective factors:**
- **Menopause / estrogen withdrawal** is associated with slower decline; lung-function decline tends to attenuate after menopause.
- No validated *genetic* protective variants are established. Anti-estrogen states (oophorectomy historically attempted) were proposed as protective but lack robust trial support.

**Gene–environment interaction.** The central interaction is **TSC2 loss × estrogen signaling**: tuberin-deficient cells are hormonally responsive; estrogen promotes LAM-cell survival (via inhibition of anoikis), migration, MEK–ERK signaling, and pulmonary metastasis in preclinical models (see §6 and §15). This explains why a constitutive genetic lesion produces a sex- and reproductive-stage-restricted disease.

Sources: OMIM 606690; PMC7714539; *AJP Cell Physiol* 2022 (https://journals.physiology.org/doi/full/10.1152/ajpcell.00202.2022); Karbowniczek 2003.

---

## 3. Phenotypes

LAM is a multisystem disease dominated by pulmonary, lymphatic, and renal manifestations. Approximate frequencies below are drawn from registry/cohort literature (NHLBI LAM Registry; ATS/JRS guideline; Orphanet).

| Phenotype | Type | Suggested HPO | Approx. frequency | Notes / characteristics |
|---|---|---|---|---|
| Progressive exertional dyspnea | Symptom | HP:0002875 (Exertional dyspnea) / HP:0002094 (Dyspnea) | Very frequent (~70–80%) | Adult-onset; progressive; the dominant presenting symptom |
| Spontaneous pneumothorax | Clinical sign/event | HP:0002107 (Pneumothorax) | ~50–70% over disease course; recurrent | Often the presenting event; recurrence rate very high (~70% without pleurodesis) |
| Diffuse pulmonary cysts (thin-walled, bilateral) | Imaging/physical | HP:0009789 (Pulmonary cyst) / HP:0032967 (Cystic lung disease, verify) | ~Universal (defining) | Bilateral, diffuse, round, thin-walled; uniform distribution |
| Chylothorax | Clinical sign | HP:0030758 (Chylothorax, verify) / HP:0010310 (Chylous pleural effusion) | ~10–30% | Due to lymphatic obstruction; can be recurrent/large |
| Chylous ascites / chyluria | Clinical sign | HP:0030245 (Chylous ascites, verify) | Less common | Lymphatic involvement of abdomen |
| Renal angiomyolipoma | Tumor/sign | HP:0006772 (Renal angiomyolipoma, verify) / HP:0009592 (Angiomyolipoma) | ~30–50% (S-LAM); up to ~80–90% (TSC-LAM) | Risk of hemorrhage if >4 cm or aneurysm >5 mm |
| Lymphangioleiomyoma (cystic lymphatic mass) | Tumor/sign | HP:0100763 (Lymphangioma, verify) | ~16–40% | Retroperitoneal/pelvic; may fluctuate in size diurnally |
| Hemoptysis | Symptom | HP:0002105 (Hemoptysis) | Occasional | Usually mild |
| Cough | Symptom | HP:0012735 (Cough) | Frequent | |
| Airflow obstruction (↓FEV₁, ↓FEV₁/FVC) | Lab/PFT | HP:0006510 (Chronic pulmonary obstruction, verify) / HP:0030877 (Reduced FEV1, verify) | Frequent, progressive | Obstructive pattern; reduced DLCO is common and often early |
| Reduced DLCO | Lab/PFT | HP:0045051 (Abnormal DLCO, verify) | Frequent | Sensitive early marker |
| Chronic respiratory failure / hypoxemia | Sign | HP:0002878 (Respiratory failure) / HP:0012418 (Hypoxemia) | Advanced disease | End-stage |
| Elevated serum VEGF-D | Lab abnormality | (no specific HP) | Frequent (diagnostic) | >800 pg/mL is diagnostic in correct context (see §10) |
| Fatigue / reduced exercise capacity | Symptom | HP:0012378 (Fatigue) | Frequent | Reduced 6-minute-walk distance |

**Quality-of-life impact:** Progressive dyspnea, oxygen dependence, recurrent pneumothorax/effusions, and the emotional burden of a rare progressive disease substantially reduce HRQoL. Lung-function decline and 6-minute-walk distance correlate with QoL and mortality (Determinants of Progression and Mortality, *Chest* 2023, https://www.sciencedirect.com/science/article/pii/S0012369223002726).

Sources: ATS/JRS guideline PMID:27628078; Orphanet ORPHA:538; *Breathe* 2020 review; StatPearls.

---

## 4. Genetic / Molecular Information

**Causal genes:**
- ***TSC2*** — 16p13.3, encodes **tuberin**; HGNC:12363; OMIM 191092. The dominant gene in sporadic LAM.
- ***TSC1*** — 9q34, encodes **hamartin**; HGNC:12362; OMIM 605284. Rarely implicated in sporadic LAM; more in TSC.

The TSC1–TSC2–TBC1D7 complex is the GAP for **RHEB-GTP**; loss → RHEB-GTP accumulation → mTORC1 hyperactivation.

**Pathogenic variants:**
- **Variant types:** the full spectrum of loss-of-function lesions — **nonsense, frameshift (indels), splice-site, missense, large deletions/structural rearrangements**, plus second-hit **LOH** at 16p13. ClinVar examples include TSC2 c.501G>A (p.Trp167Ter) nonsense and TSC2 c.5160+4A>C splice variants annotated to "Lymphangiomyomatosis" (https://www.ncbi.nlm.nih.gov/clinvar/RCV001195824/, RCV001196213/).
- **Classification:** Per ACMG/AMP, truncating LoF variants in *TSC2* are typically Pathogenic/Likely Pathogenic; many missense are VUS.
- **Somatic vs germline:** **Somatic** in S-LAM (with LOH); **germline + somatic second hit** in TSC-LAM. **Somatic mosaicism** for *TSC2* has been documented even in isolated/"sporadic" LAM, including rare male cases (PMC10849871; PMC7340110 "Generalised mosaicism for TSC2 mutation in isolated lymphangioleiomyomatosis").
- **Functional consequence:** **Loss of function** of tuberin (a tumor suppressor) → mTORC1 gain of activity (a "two-hit," recessive-at-cellular-level mechanism).
- **Allele frequency:** Causal somatic mutations are private/not in population databases; germline TSC variants in gnomAD are exceedingly rare.

**Modifier genes / interacting loci:** Estrogen-receptor-α (*ESR1*) signaling, Wnt/β-catenin, and downstream effectors modulate phenotype; no formal Mendelian modifier gene is established. mTORC1 hyperactivation cross-talks with ERα, Wnt, FGF, SHH, and TGFβ signaling to produce the cystic phenotype (PMC7714539; *AJP Cell Physiol* 2022).

**Epigenetics:** A 3D drug-screen study implicated **HDAC** dependency in mTORC1-driven LAM, nominating HDAC inhibitors (bioRxiv 2021, https://www.biorxiv.org/content/10.1101/2021.07.03.451004). Epigenetic regulation is an emerging but not yet clinically actionable area.

**Chromosomal abnormalities:** No recurrent karyotypic aberration beyond locus-specific **LOH at 16p13 (TSC2)** detected in microdissected LAM cells.

Sources: OMIM 606690/191092; ClinVar TSC2 records; PMC10849871; PMC7340110; Carsillo/Henske *PNAS* 2000 (PMID:10737804, verify).

---

## 5. Environmental Information

- **Environmental/occupational toxins:** No established environmental cause. LAM is genetically driven.
- **Hormonal "environment" (key modifiable factor):** **Estrogen** (endogenous and exogenous). Pregnancy, estrogen-containing oral contraceptives, and hormone-replacement therapy are associated with disease acceleration/complications; clinicians generally advise avoiding supplemental estrogen.
- **Lifestyle:** **Smoking** is not causal but worsens obstructive lung disease and should be avoided. **Air travel** carries a modest pneumothorax risk in patients with cysts (PMC6293523, "Air travel and incidence of pneumothorax in lymphangioleiomyomatosis").
- **Infectious agents:** None — LAM is **not** infectious.

Sources: PMC6293523; ATS/JRS guideline; Endocrinology minireview (https://academic.oup.com/endo/article/157/9/3374/2422360).

---

## 6. Mechanism / Pathophysiology

**Central causal chain (upstream → downstream):**

1. **Biallelic *TSC2* (or *TSC1*) loss** in a LAM cell → loss of TSC1–TSC2–TBC1D7 GAP activity.
2. **RHEB-GTP accumulation → constitutive mTORC1 activation** ("mTORC1, a key controller of cell growth and metabolism, is inappropriately activated"; PMC7714539).
3. **mTORC1 drives anabolic output** chiefly via **S6K1→ribosomal protein S6** and **4E-BP1→eIF4E**, boosting cap-dependent mRNA translation, ribosome biogenesis, lipid/nucleotide synthesis, and HIF/VEGF programs.
4. **VEGF-D (and VEGF-C) overproduction → lymphangiogenesis** and lymphatic spread; VEGF-D is the serum biomarker correlate.
5. **Estrogen (ERα) synergy:** mTORC1 activation synergizes with ERα; estrogen promotes **survival (anoikis resistance), migration, MEK1/2–ERK1/2 signaling**, and **pulmonary metastasis** of TSC2-deficient cells (PMC4992946; Discover Oncology 2014).
6. **Wnt/β-catenin, FGF, SHH, TGFβ up-regulation** → the **cystic remodeling** phenotype (PMC7714539).
7. **Matrix destruction:** LAM cells and recruited cells produce **matrix metalloproteinases (MMP-2, MMP-9)** and cathepsin-K, degrading elastin/ECM → progressive **airspace cyst formation and lung destruction** (rationale for doxycycline as an anti-MMP agent — modest/uncertain benefit).
8. **Lymphatic dissemination & "benign metastasis":** LAM cells circulate, seed the lung, proliferate around lymphatics/airways/vessels → cysts, lymphatic obstruction (chylous effusions), and lymphangioleiomyomas.

**Cellular processes:** dysregulated cell growth/proliferation, evasion of anoikis/apoptosis, autophagy modulation (mTORC1 suppresses autophagy — basis for the sirolimus + autophagy-inhibition trials, PMC6026235), metabolic reprogramming, lymphangiogenesis, ECM proteolysis. The proapoptotic protein **Bim** mediates anoikis that estrogen overcomes (PMC5111508). Estradiol also augments **tumor-induced neutrophil production** to promote metastasis (PMC10164661).

**Cell of origin:** Uncertain but converging on a **uterine/neural-crest-related smooth-muscle lineage**. Uterine-specific *Tsc2* deletion in mice produces myometrial tumors that spontaneously metastasize to lung (PMC3753421; "Identification of the lymphangioleiomyomatosis cell and its uterine origin," bioRxiv). LAM cells **co-express melanocytic (HMB-45, gp100, Melan-A, MITF) and smooth-muscle (SMA, desmin) markers**, plus ERα/PgR, consistent with a neural-crest–related, PEComa lineage (Frontiers 2014, PMC4243694).

**Suggested ontology terms (mechanism):**
- GO: GO:0032008 (positive regulation of TOR signaling), GO:0031929 (TOR signaling), GO:0001525 (angiogenesis), GO:0001946 (lymphangiogenesis), GO:0030198 (extracellular matrix organization), GO:0043066 (negative regulation of apoptotic process), GO:0006914 (autophagy).
- CL: CL:0000192 (smooth muscle cell), CL:0000669 (pericyte, verify), CL:0000148 (melanocyte, partial-marker analogy), CL:0002138 (endothelial cell of lymphatic vessel).
- CHEBI: CHEBI:9168 (sirolimus), CHEBI:16469 (17β-estradiol), CHEBI:50845 (doxycycline), CHEBI:68481 (everolimus, verify), CHEBI:42261 (rapamycin synonym).

Sources: PMC7714539; PMC10523142; *AJP Cell Physiol* 2022; PMC4992946; PMC5111508; PMC10164661; PMC3753421; PMC4243694; PMC6026235.

---

## 7. Anatomical Structures Affected

- **Primary organ:** **Lung** (UBERON:0002048) — diffuse bilateral cystic destruction of parenchyma; involvement of bronchioles, pulmonary vessels, and lymphatics.
- **Lymphatic system** (UBERON:0006558 lymphatic vessel; thoracic duct UBERON:0001473) — lymphangioleiomyomas, chylous effusions, axial lymphatic involvement (mediastinum, retroperitoneum, pelvis).
- **Kidney** (UBERON:0002113) — **angiomyolipomas** (fat-/muscle-/vessel-containing benign tumors).
- **Pleura** (UBERON:0000977) — pneumothorax, chylothorax.
- **Uterus / myometrium** (UBERON:0001295) — proposed origin; myometrial smooth-muscle involvement.
- **Mediastinum / retroperitoneum / abdomen** — nodal masses, chylous ascites.

**Tissue/cell level:**
- Affected tissue: smooth muscle / mesenchymal connective tissue, lymphatic and pulmonary epithelium (secondary).
- Target cell: the **LAM cell** — a perivascular epithelioid cell with **spindle (smooth-muscle-like, SMA/desmin+)** and **epithelioid (HMB-45/Melan-A+)** morphologies; ERα/PgR positive. CL: CL:0000192 (smooth muscle cell); melanocytic differentiation (CL:0000148 melanocyte) as marker analogy.

**Subcellular:** mTORC1 signaling node at the **lysosomal membrane** (GO:0005765); cytoplasmic translational machinery (ribosome, GO:0005840); nucleus (ERα transcriptional program, GO:0005634).

**Localization / laterality:** Pulmonary disease is **bilateral and diffuse/symmetric**; pneumothorax may be unilateral at presentation; angiomyolipomas often **bilateral**.

Sources: ATS/JRS guideline; StatPearls; Molecular Pathology of LAM/PEComa (https://meridian.allenpress.com/aplm/article/134/1/33/460876).

---

## 8. Temporal Development

- **Onset:** Adult-onset; typical diagnosis in the **third to fourth decade** (premenopausal). TSC-LAM may be detected earlier via TSC surveillance. Congenital/pediatric onset is essentially not seen.
- **Onset pattern:** Insidious (progressive dyspnea) or **acute** when presenting as spontaneous pneumothorax or chylothorax.
- **Progression:** Chronic, generally **slowly progressive** but variable. Disease progression is operationally defined as a **≥10% absolute decline in FEV₁**. Untreated, mean FEV₁ decline is on the order of **~75–120 mL/year** (placebo arm of MILES showed FEV₁ slope ≈ **−12 mL/month**, i.e., ~−134 mL/yr in moderately impaired patients; PMID:21410393). Rate is faster in patients with higher baseline VEGF-D and worse histology score.
- **Course pattern:** Progressive, occasionally punctuated by acute events (pneumothorax, effusion). **Menopause tends to slow** decline.
- **Disease stages:** Early (preserved PFTs, incidental cysts) → intermediate (obstructive PFTs, symptomatic) → advanced/end-stage (respiratory failure, oxygen dependence, transplant candidacy).
- **Remission:** No spontaneous remission; **treatment-induced stabilization** (not cure) with mTOR inhibitors. Disease typically **resumes progression upon drug cessation** (PMC10523142).
- **Critical intervention window:** Initiate sirolimus at/early after a decline of FEV₁ (e.g., FEV₁ <70% predicted or rapid decline) to preserve function.

Sources: MILES PMID:21410393; Predicting Individualized Progression, *Chest* 2023 (PMC10258438); Natural History (PMC2883494); Long-term outcomes PMID:35717210.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence (S-LAM):** ~**3–8 per million women**; commonly cited ~**1 in 400,000 adult women**. Japanese national-database data (2019): **prevalence ~28.7 per million women**, **incidence ~3 per million women-years** (ScienceDirect, *J Investig Med?/ ERJ Open?*, https://www.sciencedirect.com/science/article/abs/pii/S2212534524000522).
- **Men:** incidence <0.2/million-yr, prevalence ~0.8/million (essentially only in TSC).
- **TSC-LAM:** cystic lung changes occur in ~**30–40% of adult women with TSC** (higher with age).

**Inheritance pattern:**
- **Sporadic LAM: NOT inherited** (somatic two-hit, like a tumor).
- **TSC-LAM:** Tuberous Sclerosis is **autosomal dominant** (TSC1/TSC2), with high spontaneous-mutation rate (~⅔ de novo); LAM then arises via somatic second hit. **Penetrance** of LAM within TSC is **incomplete and sex-biased** (clinically penetrant mainly in women). **Variable expressivity** is the rule.
- **Germline/somatic mosaicism:** documented (relevant to rare apparent-sporadic and male cases).
- **Anticipation, founder effects, consanguinity, carrier frequency:** Not applicable to sporadic LAM; standard TSC genetics apply to TSC-LAM.

**Demographics:**
- **Sex ratio:** Overwhelmingly **female** (sporadic LAM essentially female-only; very rare male cases reported, usually with TSC or mosaicism).
- **Age:** Predominantly **reproductive-age women (20s–40s)** at diagnosis.
- **Ethnic/geographic:** No strong ethnic predilection; reported worldwide. Apparent regional differences largely reflect ascertainment.

Sources: Japan national database study (S2212534524000522); Orphanet ORPHA:538; Medscape (https://emedicine.medscape.com/article/299545-overview); StatPearls.

---

## 10. Diagnostics

**Imaging (cornerstone):**
- **HRCT chest:** numerous, **bilateral, diffuse, thin-walled round cysts** with normal intervening parenchyma — characteristic and often diagnostic in the right clinical context (RadLex; ATS/JRS guideline). Abdominal CT/MRI for AMLs and lymphangioleiomyomas.

**Biomarker:**
- **Serum VEGF-D** — the key non-invasive diagnostic test. **≥800 pg/mL** in a woman with characteristic cystic HRCT is **diagnostic** of LAM (avoids biopsy); a cut-off ~645 pg/mL is sensitive, ~800 pg/mL is specific (PLOS One, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0212776; Young et al., *Respir Res* 2012, PMID:22513045 — "combining ERS criteria and serum VEGF-D reduc[es] the need for lung biopsy"). VEGF-D also **tracks treatment response** (falls on sirolimus) and correlates with lymphatic involvement.

**Other supportive tests:**
- **PFTs:** obstructive pattern (↓FEV₁, ↓FEV₁/FVC), **reduced DLCO**; air trapping. Used for staging and monitoring.
- **6-minute walk test, pulse oximetry** for functional staging.
- **Pleural fluid analysis:** chylous (triglyceride-rich) effusion.

**Histopathology / biopsy (when imaging+biomarker inconclusive):**
- **Transbronchial lung biopsy** (often diagnostic; 2017 ATS/JRS addendum supports it, PMC5694834) or surgical biopsy.
- **Microscopy:** nodular/diffuse proliferation of spindle and epithelioid smooth-muscle-like cells around cysts, lymphatics, and vessels.
- **Immunohistochemistry:** **HMB-45 positive** (~most sensitive melanocytic marker for LAM cells), **SMA/desmin positive**, **ERα and PgR positive**; Melan-A, MITF, cathepsin-K may be positive. (Molecular Pathology of LAM/PEComa, Allenpress 2010.)

**Genetic testing:**
- Indicated to evaluate for **TSC** (germline *TSC1/TSC2* panel/sequencing + deletion/duplication analysis) when TSC features are present or in younger/multifocal disease. Sporadic LAM is diagnosed clinically (HRCT + VEGF-D ± biopsy); somatic *TSC2* testing of lesional tissue is research-oriented.

**Diagnostic criteria:** ATS/JRS 2016 and ERS 2010 criteria integrate characteristic HRCT + at least one of: AML, chylous effusion, lymphangioleiomyoma, TSC, or serum VEGF-D ≥800 pg/mL (or confirmatory biopsy).

**Differential diagnosis:** Birt-Hogg-Dubé syndrome (basilar cysts, FLCN), pulmonary Langerhans cell histiocytosis (smoking, upper-lobe nodules/cysts), emphysema/COPD, Sjögren-associated LIP/cystic disease, amyloidosis, light-chain deposition disease, follicular bronchiolitis. VEGF-D and cyst morphology distinguish LAM.

**Suggested MAXO/diagnostic terms:** MAXO:0000455 (chest CT, verify); biomarker assay; histopathology examination (MAXO:0000823, verify).

Sources: ATS/JRS 2016 (PMID:27628078); 2017 addendum (PMC5694834); Summary for Clinicians (PMC5566288); VEGF-D PLOS One 2019; Young 2012 (PMID:22513045).

---

## 11. Outcome / Prognosis

- **Survival:** Generally favorable with modern care. Recent cohorts report **5-year ~90–93%** and **10-year ~85–91%** survival (Long-term outcomes, *Respir Res* 2022, PMID:35717210). Historically (pre-sirolimus, transplant-era cohorts) median survival/transplant-free survival was lower; outcomes have improved markedly.
- **Prognostic factors (independent predictors of mortality):** older age, **lower FEV₁ and DLCO**, **shorter 6-minute-walk distance**, higher **LAM histology score (LHS-3 worst: ~52% survival at 156 months)**, and higher baseline/rising VEGF-D (Determinants of Progression and Mortality, *Chest* 2023).
- **Disease course / morbidity:** recurrent pneumothorax, chylous effusions, AML hemorrhage, progressive exertional limitation, oxygen dependence; significant QoL burden.
- **Recovery potential:** No cure; mTOR inhibitors **stabilize but do not reverse** lung destruction and must be continued; benefit wanes on discontinuation.
- **End-stage:** Respiratory failure → **lung transplantation** (good outcomes; FEV₁ ~48–49% predicted at 6–12 months post-transplant per NEJM 1996 series). **Recurrence of LAM in the allograft** can occur (recipient-derived), reinforcing the metastatic model — but is usually clinically indolent.
- **Prognostic biomarker:** serum **VEGF-D** (diagnostic + monitoring).

Sources: PMID:35717210; *Chest* 2023 (S0012369223002726); MILES PMID:21410393; Lung Transplantation NEJM 1996 (https://www.nejm.org/doi/full/10.1056/NEJM199610243351704).

---

## 12. Treatment

**Pharmacotherapy (disease-modifying):**
- **Sirolimus (rapamycin)** — allosteric **mTORC1 inhibitor**; **first-line, evidence-based** therapy. The pivotal **MILES trial** (RCT, n=89, NEJM 2011, **PMID:21410393**) showed sirolimus **stabilized FEV₁** (slope +1 vs −12 mL/month placebo), reduced VEGF-D, and improved symptoms/QoL — *"sirolimus stabilized lung function, reduced serum VEGF-D levels, and was associated with a reduction in symptoms and improvement in quality of life."* Benefit reverses on cessation. Indicated for **FEV₁ <70% predicted, rapid decline, or problematic chylous effusions/AML**. MAXO: pharmacotherapy; CHEBI:9168 (sirolimus); therapeutic_modality: SMALL_MOLECULE.
- **Everolimus** — second mTORC1 inhibitor; used especially for **renal angiomyolipoma** (EXIST-2 trial established AML shrinkage with everolimus; FDA-approved for TSC-associated AML) and as a sirolimus alternative. CHEBI:68481 (verify).
- **Doxycycline** — anti-MMP rationale; trials (e.g., the UK doxycycline trial) showed **no clear lung-function benefit**; not routinely recommended (ATS/JRS: do not use to improve lung function).
- **Hormonal manipulation (anti-estrogen, progesterone, GnRH analogs, oophorectomy):** historically used; **not recommended** by ATS/JRS due to lack of efficacy and harms; avoid exogenous estrogen.

**Pharmacogenomics:** No validated pharmacogenomic dosing for sirolimus in LAM beyond therapeutic drug monitoring (target trough ~5–15 ng/mL, often lower in LAM ~5–10).

**Experimental / advanced therapeutics (clinical trials):**
- **Sirolimus + autophagy inhibition (hydroxychloroquine)** — SAIL phase I (PMC6026235, NCT01687179).
- **Resveratrol + sirolimus** — RESET trial (NCT03253913).
- **Aromatase inhibitors (letrozole)** — TRAIL trial in postmenopausal LAM.
- **HDAC inhibitors** — preclinical lead (bioRxiv 2021).
- Other mTOR/autophagy/anti-estrogen combinations and inhaled sirolimus are under study.

**Supportive / interventional:**
- **Pleurodesis** (chemical or surgical) for recurrent pneumothorax/chylothorax; **pleurodesis is preferred even after a first pneumothorax** given high recurrence (ATS/JRS).
- **Embolization or nephron-sparing surgery** for large/bleeding renal AML (>4 cm or aneurysm >5 mm).
- **Supplemental oxygen, pulmonary rehabilitation, bronchodilators** (some have reversible obstruction), **vaccinations**, dietary management of chylous effusions (low-fat/MCT diet).
- **Lung transplantation** for end-stage disease (MAXO:0010039 organ transplantation).

**Treatment outcomes:** Sirolimus stabilizes FEV₁ and reduces VEGF-D in the majority; common adverse events: mucositis/stomatitis, acne-like rash, hyperlipidemia, edema, cytopenias, infections, diarrhea. Real-world data confirm durable stabilization with continued therapy (PMC10713282, "mTOR inhibitors in real world").

**Suggested MAXO terms:** MAXO:0000058 (pharmacotherapy/therapeutic, verify; or NCIT:C15986 Pharmacotherapy), MAXO:0010039 (organ transplantation), MAXO:0000950 (supportive care), MAXO:0000004/NCIT:C15329 (surgical procedure for pleurodesis/AML), MAXO:0000506 (oxygen therapy, verify).

Sources: MILES PMID:21410393; ATS/JRS 2016 PMID:27628078; PMC10713282; PMC6026235; clinicaltrials.gov NCT03253913, NCT01687179.

---

## 13. Prevention

- **Primary prevention:** Not possible (genetic/somatic disease). Practical measures: **avoid exogenous estrogen** (estrogen-containing contraceptives/HRT) in known/at-risk patients; smoking cessation.
- **Secondary prevention / early detection:** **Surveillance of women with TSC** for LAM (baseline HRCT, periodic PFTs) per TSC guidelines enables earlier detection. Consider LAM in any woman with spontaneous pneumothorax, unexplained dyspnea, chylous effusion, or renal AML — serum VEGF-D screening can identify cases non-invasively (PMC10327335, probability of LAM in women with spontaneous pneumothorax).
- **Tertiary prevention (complication avoidance):** **early/first-episode pleurodesis** to prevent recurrent pneumothorax; **AML embolization/surveillance** to prevent hemorrhage; **mTOR inhibition** to slow functional decline; oxygen and rehab to limit disability; **caution with air travel** and counseling on pneumothorax symptoms.
- **Counseling:** **Genetic counseling for TSC-LAM** families (autosomal-dominant TSC); reassurance that **sporadic LAM is not heritable**. Reproductive counseling regarding pregnancy-associated risk.
- **Immunization / public-health / environmental measures:** standard respiratory vaccinations (influenza, pneumococcal, COVID-19); no infectious-disease or environmental prevention applies.

Sources: ATS/JRS guideline; PMC10327335; TSC surveillance consensus.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease — *Homo sapiens* (NCBITaxon:9606). Naturally occurring LAM is essentially human-specific.
- **Orthologous genes:** *Tsc1*/*Tsc2* are highly conserved — mouse *Tsc2* (NCBI Gene 22084), rat *Tsc2* (Gene 24855); the **Eker rat** carries a germline *Tsc2* mutation (a spontaneous animal model of *Tsc2* tumor predisposition).
- **Natural disease in animals:** No well-recognized spontaneous LAM/PEComa epidemic in companion animals analogous to human LAM; the **Eker rat** develops *Tsc2*-driven uterine leiomyomas and renal tumors (the disease analog, not lung LAM per se). OMIA: TSC-related tumor predisposition in rat.
- **Comparative biology:** The TSC–mTORC1 axis is deeply conserved (yeast TOR → mammalian mTOR), enabling cross-species mechanistic study; the **female/estrogen dependence and lung tropism** of human LAM are only partially recapitulated in models.
- **Zoonotic potential:** None.

Sources: Eker-rat literature; OMIA; PMC4992946.

---

## 15. Model Organisms

**Mouse models:**
- **Uterine-specific *Tsc2* knockout** (conditional, e.g., *Amhr2-Cre* or progesterone-receptor-Cre driven): produces **estrogen-dependent myometrial tumors with smooth-muscle and neural-crest features that spontaneously metastasize to lung** in ~50% of animals — the best genetic recapitulation of LAM's hormone dependence and lung tropism (PMC3753421; Molecular Endocrinology 2013). Strong support for the uterine-origin/metastasis hypothesis.
- ***Tsc1/Tsc2* heterozygous mice** develop renal and hepatic tumors (TSC-like) but **do not faithfully reproduce pulmonary LAM** — a key limitation.

**Rat model:**
- **Eker rat** (germline *Tsc2* mutation) — source of the widely used **ELT3 (Eker leiomyoma–derived) cell line**, TSC2-null smooth-muscle cells expressing ERα/PgR.

**Cell-line / xenograft models:**
- **ELT3 cells** and **TSC2-null/patient-derived AML cells** used in xenograft "pseudo-LAM" lung-metastasis assays. **Estrogen strongly enhances pulmonary metastasis of ELT3 cells**, via **MEK1/2–ERK1/2** signaling, anoikis resistance (Bim suppression), and estradiol-driven neutrophil expansion (Discover Oncology 2014; PMC5111508; PMC10164661).
- **Patient-derived LAM cells / iPSC and 3D/organoid drug-screen systems** — used for therapeutic screening (HDAC inhibitor lead, bioRxiv 2021).

**Genetic-model types available:** knockout (constitutive *Tsc1/Tsc2* het), **conditional/tissue-specific knockout** (uterine *Tsc2*), spontaneous-mutant (Eker rat), and xenograft/induced metastasis models.

**Phenotype recapitulation:** Uterine-*Tsc2*-KO mouse captures **hormone dependence, smooth-muscle/melanocytic marker profile, and spontaneous lung metastasis**; ELT3 xenografts capture **estrogen-driven metastasis and mTORC1 biology** and **respond to rapamycin**. **Limitations:** no model fully reproduces human **cystic lung destruction**, the chronic indolent clinical course, or the exclusively female human epidemiology; lung "metastases" are myometrial-tumor deposits rather than authentic cyst-forming LAM lesions.

**Applications:** dissecting mTORC1 signaling, estrogen/ERα–mTOR crosstalk, anoikis/metastasis biology, and **preclinical drug testing** (rapamycin/everolimus, anti-estrogens, autophagy and HDAC inhibitors).

**Resources/databases:** MGI (mouse *Tsc1/Tsc2*), RGD (rat *Tsc2*, Eker), Cellosaurus (ELT3), ATCC; Alliance of Genome Resources.

Sources: PMC3753421; Discover Oncology 2014 (https://link.springer.com/article/10.1007/s12672-014-0192-z); PMC4992946; PMC5111508; PMC10164661; bioRxiv 2021.

---

## Consolidated Key Citations (verify PMIDs before KB commit)

- McCormack FX et al. **Efficacy and safety of sirolimus in lymphangioleiomyomatosis (MILES).** *N Engl J Med* 2011;364:1595-1606. **PMID:21410393** (https://pubmed.ncbi.nlm.nih.gov/21410393/). *Direct quote:* "In patients with LAM, sirolimus stabilized lung function, reduced serum VEGF-D levels, and was associated with a reduction in symptoms and improvement in quality of life."
- McCormack FX et al. **Official ATS/JRS Clinical Practice Guidelines: LAM Diagnosis and Management.** *Am J Respir Crit Care Med* 2016;194(6):748-761. **PMID:27628078** (https://pubmed.ncbi.nlm.nih.gov/27628078/).
- Gupta N et al. **2017 ATS/JRS addendum (HRCT, transbronchial biopsy, pleural disease).** PMC5694834.
- Young L et al. **Clinical utility of diagnostic guidelines and putative biomarkers in LAM (VEGF-D).** *Respir Res* 2012;13:34. **PMID:22513045** (https://pubmed.ncbi.nlm.nih.gov/22513045/).
- **Serum VEGF-D as diagnostic/therapeutic biomarker for LAM.** *PLOS One* 2019 (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0212776).
- Carsillo T, Astrinidis A, Henske EP. **Mutations in TSC2 and LOH in sporadic LAM.** *PNAS* 2000. PMID:10737804 (verify).
- Karbowniczek M et al. **Recurrent LAM after transplantation: metastatic mechanism.** *Am J Respir Crit Care Med* 2003 (https://www.atsjournals.org/doi/full/10.1164/rccm.200208-969OC).
- **Long-term clinical course and outcomes in LAM.** *Respir Res* 2022. **PMID:35717210** (https://pubmed.ncbi.nlm.nih.gov/35717210/).
- **Determinants of Progression and Mortality in LAM.** *Chest* 2023 (https://www.sciencedirect.com/science/article/pii/S0012369223002726).
- **LAM clinical review.** *Breathe* 2020;16:200007 (https://publications.ersnet.org/content/breathe/16/2/200007); PMC7714539.
- **Uterine-specific loss of Tsc2 → myometrial tumors in uterus and lungs.** *Mol Endocrinol* 2013. PMC3753421.
- Henske EP, McCormack FX. **LAM — a wolf in sheep's clothing.** *J Clin Invest* 2012 (https://www.jci.org/articles/view/58709).
- OMIM #606690 (https://omim.org/entry/606690); MONDO:0011705 (https://monarchinitiative.org/MONDO:0011705); StatPearls NBK534231 (https://www.ncbi.nlm.nih.gov/books/NBK534231/).

---

**Sources (search-derived URLs):**
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7714539/
- https://journals.physiology.org/doi/full/10.1152/ajpcell.00202.2022
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10523142/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10713282/
- https://pubmed.ncbi.nlm.nih.gov/21410393/
- https://www.nejm.org/doi/full/10.1056/NEJMoa1100391
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6026235/
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0212776
- https://pubmed.ncbi.nlm.nih.gov/22513045/
- https://www.sciencedirect.com/science/article/abs/pii/S2212534524000522
- https://emedicine.medscape.com/article/299545-overview
- https://www.ncbi.nlm.nih.gov/books/NBK534231/
- https://publications.ersnet.org/content/breathe/16/2/200007
- https://meridian.allenpress.com/aplm/article/134/1/33/460876
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10258438/
- https://www.nejm.org/doi/full/10.1056/NEJM199610243351704
- https://pubmed.ncbi.nlm.nih.gov/35717210/
- https://www.sciencedirect.com/science/article/pii/S0012369223002726
- https://www.jci.org/articles/view/58709
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4992946/
- https://academic.oup.com/endo/article/157/9/3374/2422360
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5111508/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10164661/
- https://link.springer.com/article/10.1007/s12672-014-0192-z
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3753421/
- https://www.atsjournals.org/doi/full/10.1164/rccm.200208-969OC
- https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2014.00069/full
- https://omim.org/entry/606690
- https://monarchinitiative.org/MONDO:0011705
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5694834/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5566288/
- https://www.biorxiv.org/content/10.1101/2021.07.03.451004
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10849871/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7340110/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10327335/

---

**Curator handoff note:** This is the worktree branch `add-lymphangioleiomyomatosis` with an untracked `kb/disorders/Lymphangioleiomyomatosis.yaml`. The highest-value, well-anchored evidence items for the KB entry are: (1) MILES/sirolimus (PMID:21410393), (2) ATS/JRS guideline + VEGF-D 800 pg/mL threshold (PMID:27628078; PMID:22513045), (3) TSC2/mTORC1 LOH mechanism (PMID:10737804), (4) metastatic/recurrence-after-transplant model (Karbowniczek 2003), and (5) uterine-*Tsc2*-KO mouse model (PMC3753421). Before committing any of these as snippets, run `just fetch-reference PMID:XXXX` and verify each quote is an exact substring of the fetched abstract.