---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-08T04:17:51.979124'
end_time: '2026-08-08T04:22:23.332525'
duration_seconds: 271.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thymoma
  mondo_id: ''
  category: Neoplastic
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
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 18
  total_cost_usd: 1.8089072
  session_id: 9817ea01-45d7-53de-a9c7-9530260f7472
  stop_reason: end_turn
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thymoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Thymoma** covering all of the
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

# Thymoma: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview:** Thymoma is a thymic epithelial neoplasm (TET) arising from the epithelial cells of the thymus gland, the primary lymphoid organ situated in the anterior superior mediastinum responsible for T-cell development and central immune tolerance. Thymoma is the most common tumor of the anterior mediastinum in adults and the most common form of thymic epithelial neoplasm, distinguished from thymic carcinoma (historically "type C") by retention of organotypical thymic architecture and lower-grade cytologic atypia ([Orphanet: Thymoma](https://www.orpha.net/en/disease/detail/99867); [Thymoma: An Overview, PMC10527963](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10527963/)).

**Key identifiers:**
- OMIM: 274230
- MONDO: MONDO:0006451
- Orphanet: ORPHA:99867
- ICD-10-CM: C37 (Malignant neoplasm of thymus)
- MeSH: D013945
- Related entity — Good syndrome (immunodeficiency with thymoma): a distinct paraneoplastic/associated condition

**Synonyms:** Thymic epithelial tumor (encompassing thymoma and thymic carcinoma), thymic neoplasm; historically "benign" vs "malignant" thymoma terminology has been abandoned in favor of WHO histologic typing plus staging, since even encapsulated thymomas can recur or metastasize.

**Data source note:** Information below is derived primarily from aggregated disease-level resources — population cancer registries (SEER, national cancer registries), multi-institutional genomic cohorts (TCGA, AACR GENIE, THYMOGENE trial), and case-series/case-report literature for paraneoplastic phenomenology — rather than individual EHR-level data, consistent with the rarity of the disease.

---

## 2. Etiology

**Disease Causal Factors:** Thymoma's etiology is predominantly somatic/molecular rather than classically genetic or environmentally driven. Unlike most solid tumors, thymomas have a **remarkably low overall somatic mutation burden** but a striking recurrent driver: a single hotspot missense mutation in **GTF2I** (general transcription factor IIi).

- The mutation is p.(Leu424His) [also reported as L404H/L424H depending on transcript numbering] resulting from a single T>A nucleotide change at the same genomic position on chromosome 7 in essentially all mutated tumors — "so far not detected in other tumor entities" ([GTF2I gene mutation—a driver of thymoma pathogenesis, Mediastinum](https://med.amegroups.org/article/view/3900/4668); [Primary Driver Mutations in GTF2I Specific to the Development of Thymomas, PMC7466068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/)).
- GTF2I mutation frequency is strongly histotype-dependent: **76–83% of type A and AB thymomas**, progressively less in B1/B2/B3, and only ~8% of thymic carcinomas — a molecular gradient that parallels the WHO histologic spectrum ([PMC7466068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/); [Journal of Thoracic Disease review](https://jtd.amegroups.org/article/view/35080/html)).
- Functional/mouse-model data (below) confirm GTF2I(L424H) is an **oncogenic driver**, not a passenger.

**Risk Factors:**
- *Genetic*: No established Mendelian susceptibility locus for sporadic thymoma; GTF2I mutation is somatic, not germline. No strong GWAS-identified common-variant susceptibility loci are established for thymoma (a genuine knowledge gap — rarity limits GWAS power).
- *Environmental*: A European case–control study found an association between **prior chest/medical irradiation** and thymoma risk that persisted even excluding exposures within 5 years of interview, "suggesting a possible real association or a common pathogenesis involving conditions leading to X-rays" ([Constitutional Factors and Irradiation as Risk Factors for Thymoma: A European Case–Control Study, PMC11431288](https://pmc.ncbi.nlm.nih.gov/articles/PMC11431288/)).
- *Demographic*: Age is the dominant risk correlate — incidence rises through middle age and peaks in the 7th decade (70–74 years, ~1.06/100,000) ([Frontiers Oncology epidemiology study, PMC10805269](https://pmc.ncbi.nlm.nih.gov/articles/PMC10805269/)). Racial/ethnic variation is notable: Asian/Pacific Islanders have the highest incidence, followed by Black then White populations, and thymoma arises in Black patients at a markedly younger median age (48 vs. 58 years in White patients) ([Epidemiology of Thymoma and Associated Malignancies, JTO](https://www.jto.org/article/S1556-0864(15)32613-7/fulltext)).
- **Autoimmune disease** is both a risk correlate and consequence: myasthenia gravis (MG), systemic lupus erythematosus, and rheumatoid arthritis co-occur with thymoma at rates far above the general population, likely reflecting shared/bidirectional pathophysiology (below) rather than classic exogenous risk exposure.

**Protective Factors:** No established genetic or environmental protective factors are documented in the literature for thymoma specifically — this is a notable gap given the rarity of the tumor and paucity of population-scale genetic studies.

**Gene-Environment Interactions:** No specific validated GxE interaction has been characterized for thymoma; the irradiation-association data above is the closest documented environmental modifier, but no interaction with a specific genetic susceptibility background has been demonstrated.

---

## 3. Phenotypes

Thymoma phenotypes fall into three broad classes: (a) local mass-effect/compressive symptoms, (b) systemic paraneoplastic autoimmune syndromes (the clinically dominant and best-characterized phenotype category), and (c) incidental radiographic findings.

### A. Local/compressive phenotypes
- Chest pain, cough, dyspnea from mediastinal mass effect
- Superior vena cava syndrome (in locally advanced disease)
- Suggested HPO terms: HP:0100749 (Chest pain), HP:0002094 (Dyspnea), HP:0012735 (Cough)
- **~30% of patients are asymptomatic**, with thymoma discovered incidentally on chest imaging ([Update in diagnostic imaging of the thymus, PMC6755948](https://pmc.ncbi.nlm.nih.gov/articles/PMC6755948/))

### B. Paraneoplastic autoimmune phenotypes (the defining clinical feature class)
- **Myasthenia gravis (MG)** — present in **30–50% of thymoma patients**; conversely, ~10–15% of MG patients have thymoma. Suggested HPO: HP:0003473 (Myasthenia); associated signs include ptosis (HP:0000508), diplopia (HP:0000651), dysphagia (HP:0002015), fatigable muscle weakness (HP:0003324) ([Immunological function of thymoma and pathogenesis of paraneoplastic myasthenia gravis, PMID:18401674](https://pubmed.ncbi.nlm.nih.gov/18401674/); [Paraneoplastic Autoimmunity in Thymus Tumors, PMC2276007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2276007/)).
- **Good syndrome (thymoma with immunodeficiency)** — up to 5% of thymoma patients; hypogammaglobulinemia, B-cell depletion, recurrent sinopulmonary infections, opportunistic infections (CMV, PCP, mucocutaneous candidiasis) ([When the Good Syndrome Goes Bad, PMC8185358](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8185358/)). Suggested HPO: HP:0004313 (Decreased circulating antibody level), HP:0002850 (Decreased circulating total IgG), HP:0002205 (Recurrent respiratory infections).
- **Peripheral nerve hyperexcitability** (neuromyotonia, Morvan syndrome), **dysautonomia**, **limbic/paraneoplastic encephalitis** ([Handbook of Clinical Neurology chapter](https://www.sciencedirect.com/science/chapter/handbook/abs/pii/B9780128239124000086); case report PMC6334889).
- **Pure red cell aplasia**, autoimmune cytopenias, myositis, myocarditis, systemic lupus erythematosus, cutaneous amyloidosis, nephrotic syndrome have all been reported paraneoplastic associations ([complex paraneoplastic syndrome case report, PMC9720310](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9720310/)).

### Phenotype characteristics
- **Onset:** Adult-onset overwhelmingly (median age ~59–60 years); rare in children/young adults.
- **Frequency data:** MG 30–50% of thymoma cases; Good syndrome up to 5%; asymptomatic/incidental ~30%.
- **Severity/progression:** Highly variable — paraneoplastic MG can range from mild ocular symptoms to myasthenic crisis requiring ventilatory support; symptoms may persist, improve, or (rarely) worsen post-thymectomy.
- **Quality of life impact:** MG-related fatigue and weakness substantially affect activities of daily living; Good syndrome's recurrent/opportunistic infections and its "ominous prognosis with high mortality rate secondary to recalcitrant infectious disease" represent a severe QoL and survival burden (per Good syndrome literature above). Dedicated thymoma-specific EQ-5D/SF-36 data are sparse in the literature reviewed.

---

## 4. Genetic/Molecular Information

**Causal/driver gene:**
- **GTF2I** (7q11.23; HGNC:4661) — somatic hotspot mutation p.(Leu424His) (also written L404H), a **gain-of-function/oncogenic** driver, present in the majority of type A/AB thymomas and declining in frequency through B1→B2→B3→thymic carcinoma. This is the single most important molecular lesion described for thymoma ([PMC7466068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/); [GTF2I Mutation in Thymomas: Independence From Racial-Ethnic Backgrounds, PMC8419886](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8419886/)).
- Suggested GO term for GTF2I molecular function: GO:0003713 (transcription coactivator activity).

**Variant classification/consequence:**
- Somatic, not germline; single recurrent missense hotspot (not a spectrum of LOF alleles) — functionally characterized as oncogenic gain-of-function based on mouse knock-in data (Section 6/15).
- Note for schema mapping: this would be a `functional_impact_category: GAIN_OF_FUNCTION` (qualitative, non-ontology-bound) event on `GeneticContext`, distinct from a quantitative `modifier`.

**Genomic differences by histotype/tumor type (thymic carcinoma diverges sharply):**
- Thymic carcinomas show a genuinely distinct, higher-mutation-burden genomic profile dominated by **TP53** (~27.7% mutated), **CYLD** (~17.6%), and **CDKN2A** (~12.1%), with recurrent homozygous 9p21.3 deletions encompassing CDKN2A/CDKN2B ([Genomic Landscape of Thymic Carcinoma, AACR GENIE cohort, PMC12839660](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12839660/)).
- Targeted NGS of thymic epithelial tumors found pathogenic variants in **KIT, ERBB2, KRAS, and TP53** in ~30% of thymic carcinomas, informing candidate targeted-therapy strategies ([PMC9324890](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9324890/)).
- **MTOR mutations** were enriched in local recurrences and lymph node metastases, implicating a progression-associated pathway.
- The THYMOGENE prospective trial confirms these findings in an independent prospective cohort ([Somatic Mutations of Thymic Epithelial Tumors, THYMOGENE, PMID:41405018](https://pubmed.ncbi.nlm.nih.gov/41405018/)).

**Prognostic significance of genotype:** GTF2I-mutant TETs show a markedly better clinical course than GTF2I-wildtype tumors — 10-year survival 96% vs. 70% ([GTF2I gene mutation, Mediastinum](https://med.amegroups.org/article/view/3900/4668)) — i.e., the driver mutation correlates inversely with aggressiveness, opposite to the typical oncogene paradigm and consistent with GTF2I-mutant tumors being enriched in the more indolent A/AB histotypes.

**Modifier genes:** No well-validated modifier genes distinct from co-occurring TP53/CDKN2A alterations in progression to carcinoma have been firmly established; genomic clustering analyses have identified molecular subtypes independent of WHO histologic type, suggesting additional unrecognized modifiers ([Genomic clustering analysis, PMC8202771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8202771/)).

**Epigenetic information:** Advanced/carcinoma-grade tumors show mutations in epigenetic/chromatin-remodeling regulators, though this is less well-characterized than in thymoma proper — an area flagged as needing further multi-omic study.

**Chromosomal abnormalities:** Recurrent 9p21.3 homozygous deletion (CDKN2A/CDKN2B) in thymic carcinoma; broader cytogenetic literature (6p21/HLA-region associations) was not substantively returned by current searches — worth flagging as **not confirmed by primary sources reviewed here** (a gap rather than a stated negative).

---

## 5. Environmental Information

- **Environmental factors:** Prior chest/mediastinal irradiation is the most substantiated environmental risk correlate identified in case–control data ([PMC11431288](https://pmc.ncbi.nlm.nih.gov/articles/PMC11431288/)). Suggested ECTO term: exposure to ionizing radiation (therapeutic/diagnostic).
- **Lifestyle factors:** No specific validated lifestyle risk factor (smoking, diet, alcohol) is established for thymoma in the literature surveyed — distinguishing it from most epithelial cancers where tobacco/lifestyle exposures dominate.
- **Infectious agents:** No infectious etiology is established for thymoma itself. (Contrast: Good syndrome, a thymoma-associated immunodeficiency, predisposes to secondary opportunistic infections — CMV, Pneumocystis jirovecii, mucocutaneous Candida — but these are a *consequence* of the paraneoplastic immunodeficiency, not a cause of the tumor.)

---

## 6. Mechanism / Pathophysiology

Thymoma pathophysiology operates on two largely independent but converging axes: **(A) the oncogenic transformation of thymic epithelial cells**, and **(B) the disruption of central immune tolerance that produces the paraneoplastic autoimmune phenotype.** These are mechanistically distinct — a curator building a causal chain should model them as parallel branches from the same initiating cellular context rather than a single linear pathway.

### A. Oncogenic transformation pathway
1. **Trigger:** Somatic GTF2I p.(L424H) hotspot mutation arising in thymic epithelial progenitor cells (biological_scale: MOLECULAR).
2. **Molecular consequence:** GTF2I acts as a transcription factor/coactivator (GO:0003713); the mutant form drives aberrant transcriptional programs in thymic epithelium. Knock-in mouse data show the mutation **impairs differentiation of bipotent thymic epithelial progenitors**, with medullary differentiation particularly affected ([Human thymoma-associated mutation of GTF2I impairs thymic epithelial progenitor differentiation in mice, PMID:36175547](https://pubmed.ncbi.nlm.nih.gov/36175547/); [Nature Communications Biology](https://www.nature.com/articles/s42003-022-04002-7)).
3. **Cellular consequence:** Aberrant thymic epithelial architecture, reduced thymopoietic activity, and — over time in aged mice — frank tumor formation (biological_scale: CELLULAR/TISSUE) ([A Knock-in Mouse Model of Thymoma with the GTF2I L424H Mutation, PMID:36049655 / PMC9691559](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691559/)).
4. **Progression branch (thymic carcinoma):** Acquisition of additional drivers — TP53 inactivation, CDKN2A/CDKN2B loss (9p21.3 deletion), CYLD mutation — associated with loss of organotypic architecture, higher-grade cytologic atypia, and worse prognosis (biological_scale: MOLECULAR→TISSUE).

Suggested GO biological process terms: GO:0060218 (hematopoietic stem cell differentiation, analog for epithelial progenitor context), GO:0001756 (somitogenesis-unrelated — better: GO:0060713, labyrinthine layer thymic epithelial differentiation-adjacent terms should be verified via OAK); GO:0009887 (animal organ morphogenesis) as a general placeholder pending precise term verification.

### B. Autoimmunity / central-tolerance-failure pathway (drives the paraneoplastic phenotype)
1. **Mechanistic hypothesis (well-supported):** Thymomas — particularly cortical-type/epithelial architecture-dominant subtypes — **lack a functional medulla**, the compartment where professional antigen-presenting medullary thymic epithelial cells (mTECs) normally express AIRE (autoimmune regulator) and drive **promiscuous tissue-restricted antigen expression** for negative selection of autoreactive thymocytes ([Central tolerance to self revealed by the autoimmune regulator, PMC4654700](https://pmc.ncbi.nlm.nih.gov/articles/PMC4654700/); [Update on Aire and thymic negative selection](https://onlinelibrary.wiley.com/doi/abs/10.1111/imm.12831)).
2. **Consequence:** Failure of this AIRE-dependent negative-selection checkpoint within the neoplastic thymic microenvironment allows **export of autoreactive T cells** into the periphery — "thymomas may lack the functional medulla where professional antigen-presenting cells engage in negative selection, leading thymomas to generate autoreactive T cells causing autoimmunity" ([Immunological function of thymoma and pathogenesis of paraneoplastic MG, PMID:18401674](https://pubmed.ncbi.nlm.nih.gov/18401674/)).
3. **Downstream autoantibody generation:** Autoreactive T/B cell cooperation produces autoantibodies against neuromuscular junction nicotinic acetylcholine receptor (AChR) components and against striated-muscle antigens (notably **titin**, a giant sarcomeric protein) — titin main immunogenic region antibodies detected in 97% of thymoma-associated MG sera vs. essentially absent in healthy controls ([Immunological and Structural Characterization of Titin Main Immunogenic Region, PMC9952892](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9952892/); [Anti-titin antibodies in myasthenia gravis: tight association with thymoma, PMID:11405802](https://pubmed.ncbi.nlm.nih.gov/11405802/)).
4. **Clinical manifestation:** Neuromuscular junction blockade (myasthenia gravis), or — in Good syndrome — B-cell/T-cell combined immunodeficiency with hypogammaglobulinemia, presumably reflecting a distinct (less well fully elucidated) disruption of B-cell maturation/tolerance rather than simple autoreactivity.

Suggested CL terms: CL:0002365 (medullary thymic epithelial cell), CL:0002365-adjacent cortical thymic epithelial cell term (verify exact CL ID via OAK), CL:0000542 (lymphocyte), CL:0000084 (T cell).

### Immune-checkpoint axis (relevant to treatment-toxicity mechanism)
- Thymomas frequently express high levels of **PD-L1**, making PD-1/PD-L1 blockade mechanistically rational as an anti-tumor strategy, but the same defective central-tolerance environment that causes paraneoplastic autoimmunity **markedly predisposes to severe/fatal immune-related adverse events** upon checkpoint inhibition (myocarditis, myositis, hepatitis) — "the thymus is a lymphatic system organ for the development of the immune system, which might contribute to high rates of immune-therapy related toxicity events (irAEs)" ([Fatal Toxicity Induced by anti-PD-1 ICI in Thymic Epithelial Tumor](https://www.tandfonline.com/doi/full/10.2217/imt-2021-0215); case reports of fatal multi-organ irAEs, [Clinical Lung Cancer](https://www.clinical-lung-cancer.com/article/S1525-7304(19)30282-7/abstract)). This is a directly relevant `treatment`→`target_mechanisms` and toxicity-mechanism pattern (could map to the `drug_hypersensitivity_scar`-adjacent immune-toxicity family, though mechanistically distinct — T-cell-mediated organ toxicity via checkpoint blockade rather than HLA-restricted drug hypersensitivity).

### Molecular profiling / advanced technologies
- **Transcriptomics/genomics:** TCGA and independent genomic clustering studies have defined molecular subtypes of thymic epithelial tumors that cross-cut WHO histologic classification ([PMC8202771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8202771/)).
- **Single-cell/spatial:** Not substantively returned in this search pass — likely an emerging-data gap for thymoma specifically, relative to more common cancers.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: Thymus (anterior/superior mediastinum) — suggested UBERON:0002370 (thymus).
- Secondary/complication sites: pleura (thymoma-associated pleural effusion/pleural dissemination — a characteristic pattern of thymoma spread is direct pleural seeding rather than distant hematogenous metastasis in early stage disease), pericardium, great vessels, lung (direct invasion in advanced Masaoka-Koga stage III–IV), lymph nodes and distant organs in metastatic disease.
- Body systems: primarily the **immune/lymphatic system** (as the originating organ of adaptive immunity) and secondarily **neuromuscular system** (via paraneoplastic MG) and **hematologic/hematopoietic system** (via paraneoplastic cytopenias, Good syndrome).

**Tissue/cell level:**
- Neoplastic epithelial cells: cortical- and medullary-type thymic epithelial cells depending on histologic subtype (CL:0002365 medullary TEC and cortical TEC equivalent).
- Non-neoplastic but pathologically important "background" population: intratumoral immature T-lymphocytes (thymocytes), which are typically abundant, especially in B-type thymomas, and contribute to the paraneoplastic-autoimmunity mechanism.

**Subcellular level:** Not a classical organelle-level disease; the driver lesion (GTF2I) acts at the nuclear transcription-factor level (GO cellular component: GO:0005634, nucleus).

**Localization:** Virtually always anterior mediastinal in location; bilateral/unilateral distinction is not typically applicable (thymus is a midline, though bilobed, organ) — lateralization is not a meaningful phenotype axis here, unlike in paired-organ diseases.

---

## 8. Temporal Development

- **Onset:** Adult-onset disease; median age at diagnosis ~59–60 years, rare before age 30, exceedingly rare in children (<1% of cases in the 1–18 age band per SEER-linked cohort data) ([PMC7138550](https://pmc.ncbi.nlm.nih.gov/articles/PMC7138550/)).
- **Onset pattern:** Typically insidious — many patients (~30%) are asymptomatic and diagnosed incidentally on imaging; symptomatic presentation (mass effect or paraneoplastic autoimmune symptoms) develops gradually.
- **Staging (disease "progression" framework):** The **Masaoka-Koga** system (stage I–IVb, based on capsular invasion, extension into surrounding fat/pleura/pericardium, and metastatic spread) remains the most widely applied staging system; the newer **TNM/IASLC-ITMIG** system (adopted by AJCC/UICC) is increasingly used in parallel ([Masaoka-Koga and TNM Staging System, PMC8582470](https://pmc.ncbi.nlm.nih.gov/articles/PMC8582470/)).
  - 5-/10-year overall survival by Masaoka-Koga stage: Stage I 96.4%/88.9%; Stage II 95%/89.5%; Stage III 85.4%/72.8% (stage I and II curves overlap, but stage III is clearly worse).
  - 5-/10-year survival by TNM T-stage: T1 95.5%/88.8%; T2 84.8%/70.7%; T3 88%/76.3%.
- **Progression rate:** Generally slow/indolent for type A/AB/B1 thymomas; progressively more aggressive through B2→B3→thymic carcinoma, correlating inversely with GTF2I mutation frequency.
- **Disease course pattern:** Can be stable for years post-resection in early stage; capable of late recurrence (pleural recurrence is characteristic) even after apparently complete resection, warranting long-term surveillance.
- **Critical periods:** Time-of-surgery is the major modifiable intervention window — complete (R0) resection is the single strongest determinant of outcome; presence of paraneoplastic MG can complicate perioperative anesthetic/respiratory management and requires pre-operative optimization (e.g., plasmapheresis/IVIG or pyridostigmine) in some cases.

---

## 9. Inheritance and Population

**Epidemiology:**
- Overall US incidence: variably reported ~0.13–2.2 per million/100,000 person-years depending on cohort and time window studied ([Frontiers Oncology, PMC10805269](https://pmc.ncbi.nlm.nih.gov/articles/PMC10805269/); [Trends in incidence of thymoma/thymic carcinoma/thymic NET, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0227197)).
- Thymomas represented 9,041 cases (66.3% of total thymic cancers) in the US SEER data 2001–2015.
- Orphanet cites a European annual incidence estimate of ~1/769,000.

**Inheritance pattern:** Thymoma is essentially **sporadic** — driven by a somatic (not germline) GTF2I hotspot mutation. No established Mendelian inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, or founder-effect data apply to thymoma itself as currently understood. (This contrasts with Good syndrome, which is also an acquired/sporadic adult-onset condition, not inherited.)

**Population demographics:**
- Age distribution (n=4,431 TET patients): 0.6% aged 1–18; 4.0% aged 19–30; 8.6% aged 31–40; 16.7% aged 41–50; 22.0% aged 51–60; 25.0% aged 61–70; 16.6% aged 71–80; 6.5% aged >80 ([PMC7138550](https://pmc.ncbi.nlm.nih.gov/articles/PMC7138550/)).
- Sex ratio: approximately 1:1.09 (male:female), i.e., roughly equal with a very slight female predominance.
- Race/ethnicity: highest incidence in Asian/Pacific Islanders, followed by Black, then White populations; Black patients present at a significantly younger median age (48 vs. 58 years) ([JTO epidemiology review](https://www.jto.org/article/S1556-0864(15)32613-7/fulltext)).
- Geographic distribution: No strong endemic geographic clustering reported beyond the race/ethnicity associations above; comparative US-Germany epidemiologic data (1999–2019) show broadly similar incidence trends across both countries ([PMC10805269](https://pmc.ncbi.nlm.nih.gov/articles/PMC10805269/)).

---

## 10. Diagnostics

**Imaging:**
- **CT (contrast-enhanced)** is the imaging modality of choice — evaluates mass size, location, margins (smooth/lobular vs. infiltrative), density, and relationship to adjacent structures (heart, great vessels, lung); helps distinguish thymoma from other anterior mediastinal masses (lymphoma, germ cell tumor, thyroid goiter) ([Role of Imaging in Diagnosis, Staging, Treatment of Thymoma, RadioGraphics](https://pubs.rsna.org/doi/abs/10.1148/rg.317115505); [Update in diagnostic imaging of thymus, PMC6755948](https://pmc.ncbi.nlm.nih.gov/articles/PMC6755948/)).
- MRI is used for further characterization, particularly of cystic vs. solid components.

**Biopsy/histopathology:**
- CT- or ultrasound-guided percutaneous needle biopsy, or surgical resection with histopathology, provides definitive diagnosis via WHO histologic classification.
- In classic presentations (imaging + clinical features strongly suggestive), biopsy may be deferred in favor of upfront resection, given seeding risk concerns historically associated with biopsy of encapsulated thymoma (a clinically important nuance for surgical planning).

**Serology/biomarkers (central to thymoma-associated MG workup):**
- **Anti-acetylcholine receptor (AChR) antibodies** — standard MG diagnostic test.
- **Anti-titin antibodies** — present in 56/70 (80%) of thymectomized thymoma patients vs. only 17/165 (10%) with thymic atrophy/hyperplasia; titin MIR antibodies detected in 97% of thymoma-associated MG sera. Lower sensitivity than CT/MRI for thymoma detection but higher specificity ([PMID:11405802](https://pubmed.ncbi.nlm.nih.gov/11405802/); [PMC9952892](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9952892/)).
- Additional autoantibodies reported: anti-ryanodine receptor, anti-striational antibodies.

**Genetic/molecular testing:** Not yet part of routine standard-of-care diagnostic workup (unlike many other cancers), but GTF2I mutation status (and TP53/CDKN2A in suspected thymic carcinoma) is increasingly assessed in research/clinical-trial contexts (e.g., THYMOGENE) and carries prognostic value.

**Clinical criteria/differential diagnosis:** Anterior mediastinal mass differential includes thymoma, lymphoma, germ cell tumor, thyroid goiter, thymic cyst, thymic hyperplasia, and thymic carcinoma — WHO histologic typing (A/AB/B1/B2/B3/carcinoma) is the core diagnostic classification framework ([2015 WHO Classification of Tumors of the Thymus, PMC4581965](https://pmc.ncbi.nlm.nih.gov/articles/PMC4581965/); [Histologic Classification of Thymoma, JTO](https://www.jto.org/article/S1556-0864(15)33335-9/fulltext); [StatPearls Anterior Mediastinal Mass](https://www.ncbi.nlm.nih.gov/books/NBK546608/)).

**Screening:** No population-level screening program exists for thymoma given its rarity; incidental detection on chest imaging performed for other indications, or workup triggered by new-onset MG symptoms, are the practical "screening" pathways.

---

## 11. Outcome/Prognosis

- **Survival:** Strongly stage- and histotype-dependent (see Section 8 for stage-stratified 5-/10-year OS figures). Overall, thymoma carries a substantially better prognosis than thymic carcinoma.
- **Molecular prognostic factor:** GTF2I mutation status independently associates with survival — 10-year survival 96% (GTF2I-mutant) vs. 70% (GTF2I-wildtype) ([Mediastinum review](https://med.amegroups.org/article/view/3900/4668)).
- **Complications:**
  - **Second primary malignancies (SPM)**: markedly elevated risk — a SEER analysis found second-cancer incidence of 8,224 per 100,000 thymoma patients vs. 459 per 100,000 in the general SEER population; significantly elevated risk for lung/bronchus cancer, non-basal/squamous skin cancer, urinary bladder cancer, thyroid cancer, and leukemias (ALL, AML, other acute leukemia); no significant increase for lymphoma or hepatobiliary cancers ([Epidemiology of Thymoma and Associated Malignancies, JTO](https://www.jto.org/article/S1556-0864(15)32613-7/fulltext); [JCO abstract, second primary malignancy](https://ascopubs.org/doi/10.1200/JCO.2019.37.15_suppl.8568)). This warrants **long-term multi-organ cancer surveillance** in thymoma survivors.
  - Paraneoplastic MG and Good syndrome can persist, and in some cases worsen or newly appear, even after thymectomy — thymectomy is not uniformly curative for the autoimmune phenotype.
  - Good syndrome carries a poor prognosis with substantial mortality from recurrent/opportunistic infection.
- **Recurrence pattern:** Characteristically pleural/intrathoracic seeding rather than distant hematogenous spread in earlier-stage disease, which shapes surveillance imaging strategy (serial chest CT).
- **Prognostic factors:** Masaoka-Koga/TNM stage, WHO histologic subtype, completeness of surgical resection (R0 vs. R1/R2), GTF2I mutation status, and (in thymic carcinoma) TP53/CDKN2A alteration status.

---

## 12. Treatment

**Surgery (primary modality):**
- Complete surgical resection (thymectomy, often with removal of surrounding mediastinal fat) is the cornerstone of management for resectable disease.
- Minimally invasive (thoracoscopic/robotic) approaches may be considered for clinical stage I–II disease in specialized centers, though NCCN notes these are not yet routinely recommended given limited long-term recurrence/survival data ([NCCN guidelines summary](https://www2.tri-kobe.org/nccn/guideline/lung/english/thymic.pdf)).
- Suggested NCIT term: NCIT:C15329 (Surgical Procedure) / more specific thymectomy term if available.

**Radiotherapy:**
- Adjuvant radiotherapy (conventionally fractionated, 1.8–2 Gy/day to 45–60 Gy adjuvant, 60–66 Gy definitive) is standard of care for stage II thymoma with capsular invasion after complete resection; elective nodal irradiation is not recommended ([NCCN 2.2025 guidelines](https://jnccn.org/view/journals/jnccn/23/6/article-p255.xml); [Radiotherapy for Thymic Carcinoma, PMC3887269](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3887269/)).
- Neoadjuvant radiotherapy has been explored for higher-risk B3 thymomas combined with minimally invasive surgery ([PMC10076567](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10076567/)).
- Suggested NCIT term: NCIT:C15313 (Radiation Therapy).

**Chemotherapy:**
- Platinum-based combination chemotherapy is standard of care for unresectable/metastatic or recurrent disease ([Cancer Therapy Advisor summary](https://www.cancertherapyadvisor.com/ddi/thymoma-pharmacologic-treatment/)).
- Suggested NCIT term: NCIT:C15632 (Chemotherapy).

**Targeted therapy:**
- **Sunitinib** — recommended for thymic carcinoma regardless of c-KIT mutation status; phase II data showed partial response in 6/23 (26%) chemo-refractory thymic carcinoma patients; STYLE trial showed 21.4% ORR in advanced/recurrent B3 thymoma and thymic carcinoma.
- **Everolimus** (mTOR inhibitor) — durable disease control observed in recurrent thymic epithelial tumors, but with notable risk of fatal pneumonitis — an important toxicity caveat for curation.
- These agents map to `therapeutic_agent`/CHEBI (sunitinib, everolimus) under a `treatment_term` of Targeted Therapy (NCIT:C93352) or Pharmacotherapy (NCIT:C15986).

**Immunotherapy (mechanistically important but high-risk):**
- Pembrolizumab (anti-PD-1) has shown dramatic remission in some metastatic thymoma cases given high PD-L1 expression, but **NCCN does not recommend pembrolizumab for thymoma due to the high rate of immune-related adverse events** — fatal multi-organ toxicity (myocarditis, myositis, hepatitis, endocrinopathies) has been reported, mechanistically linked to the same defective central-tolerance thymic microenvironment described in Section 6 ([Fatal adverse events in two thymoma patients treated with anti-PD-1](https://www.sciencedirect.com/science/article/abs/pii/S0169500219305082); [dramatic remission case report, PMC8082155](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8082155/)). This is a clinically critical curation point: checkpoint inhibitors are mechanistically rational but carry disproportionate risk in this specific tumor type relative to other PD-L1-high cancers.

**Supportive/paraneoplastic-directed care:**
- Pyridostigmine (acetylcholinesterase inhibitor), immunosuppression, plasmapheresis, or IVIG for paraneoplastic MG management, particularly perioperatively.
- Immunoglobulin replacement therapy for Good syndrome-associated hypogammaglobulinemia.

**Experimental:** Multiple ongoing clinical trials (e.g., NCT04577495 examining prognostic factors post-surgery; various targeted/immunotherapy combination trials) are registered on ClinicalTrials.gov for advanced/refractory thymic epithelial tumors.

**Treatment strategy:** Multidisciplinary, stage-adapted algorithm — surgery ± adjuvant radiotherapy for early stage; multimodal (chemotherapy ± radiotherapy ± surgery) for locally advanced disease; chemotherapy/targeted therapy for unresectable/metastatic disease, with immunotherapy reserved cautiously given toxicity profile.

---

## 13. Prevention

- **Primary prevention:** No established primary prevention strategy exists, given the predominantly somatic/sporadic driver-mutation etiology and lack of strong modifiable environmental risk factors beyond incidental/uncommon radiation-exposure associations.
- **Secondary prevention/early detection:** No population screening program exists (rarity precludes cost-effective screening); practical early detection occurs via incidental imaging findings or MG-symptom-triggered workup.
- **Tertiary prevention:** Long-term surveillance imaging (serial chest CT) post-resection to detect pleural recurrence; long-term multi-organ cancer surveillance given the markedly elevated second-primary-malignancy risk (Section 11); ongoing monitoring/management of paraneoplastic autoimmune phenomena (MG, Good syndrome) independent of oncologic status.
- **Genetic counseling:** Not applicable in the traditional sense given the sporadic somatic etiology — no known heritable risk to counsel relatives about.
- **Prophylaxis:** Immunoglobulin replacement in diagnosed Good syndrome to reduce opportunistic infection risk; vigilance for opportunistic pathogens (Pneumocystis, CMV) in immunodeficient thymoma patients may warrant prophylactic antimicrobial strategies analogous to other combined immunodeficiencies (extrapolated management principle; not thymoma-specific primary literature identified in this search pass).

---

## 14. Other Species / Natural Disease

**Naturally occurring veterinary disease — dogs and cats:**
- Thymoma occurs as a **naturally occurring neoplasm in dogs and cats**, with a notably parallel paraneoplastic myasthenia gravis phenotype mediated by anti-AChR antibodies, making it a genuine spontaneous comparative model rather than only an induced/engineered one ([Acquired myasthenia gravis with concurrent polymyositis and myocarditis secondary to thymoma in a dog, PMC8541714](https://pmc.ncbi.nlm.nih.gov/articles/PMC8541714/); [Metastatic thymoma and acquired generalized MG in a beagle, PMC1716736](https://pmc.ncbi.nlm.nih.gov/articles/PMC1716736/); [Canine Epithelial Thymic Tumors: Outcome in 28 Dogs Treated by Surgery, PMC8698125](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8698125/)).
- **Notable species difference in penetrance of the paraneoplastic phenotype:** In cats presenting with MG, roughly **1 in 4** has a thymic/mediastinal mass, whereas in dogs only **~3–4%** of MG cases are thymoma-associated — cats show a much tighter thymoma–MG linkage than dogs ([Merck Veterinary Manual, Neurological Paraneoplastic Syndromes in Small Animals](https://www.merckvetmanual.com/generalized-conditions/paraneoplastic-disorders-in-small-animals/neurological-paraneoplastic-syndromes-in-small-animals); [Myasthenia Gravis in Dogs and Cats, VIN](https://veterinarypartner.vin.com/default.aspx?pid=19239&id=4951980)).
- Veterinary treatment parallels human management: surgical thymectomy is the mainstay, with pyridostigmine/anticholinesterase therapy for MG symptom control.
- No OMIA (Online Mendelian Inheritance in Animals) entry or dog/cat GTF2I ortholog mutation data were identified in this search pass — veterinary thymoma appears to be studied predominantly at the clinical/phenotypic level rather than the somatic-genomic level, representing a translational research gap.

**Comparative biology:** The conserved thymoma→paraneoplastic-MG mechanism (loss of medullary negative-selection capacity → autoreactive T cells → anti-AChR antibody generation) across humans, dogs, and cats supports this as an evolutionarily conserved thymic-tolerance failure mechanism rather than a human-idiosyncratic phenomenon, strengthening confidence in the Section 6 mechanistic model.

**Zoonotic potential:** Not applicable — thymoma is a non-transmissible neoplastic disease.

---

## 15. Model Organisms

**Genetically engineered mouse model (the primary validated model):**
- A **conditional Gtf2i(L424H) knock-in mouse** (mutation targeted to Foxn1+ thymic epithelial cells) is the first genuine animal model of thymoma and directly demonstrates causality of the human hotspot mutation ([A Knock-in Mouse Model of Thymoma with the GTF2I L424H Mutation, PMID:36049655/PMC9691559](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691559/); editorial: [Now We Have the First Animal Model for Thymoma, JTO](https://www.jto.org/article/S1556-0864(22)01593-3/fulltext)).
- **Phenotype recapitulation:** In young mice, the mutation impairs thymic medulla development and mTEC maturation (mirroring the human medullary-deficiency mechanism proposed for paraneoplastic autoimmunity); in aged mice, it induces frank thymic tumor formation that **histologically mirrors human type B1 and B2 thymomas** ([PMC7466068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/); [Communications Biology, PMID:36175547](https://pubmed.ncbi.nlm.nih.gov/36175547/)).
- **Model limitations:** The mouse model most closely recapitulates B1/B2-type histology rather than the A/AB types where GTF2I mutation frequency is highest in humans (76–83%) — a partial phenotype-genotype mismatch worth flagging as a `HUMAN_MODEL_MISMATCH`-style consideration if curated into dismech, since the mutation's histologic association differs between the engineered model and the natural human tumor spectrum. This is exactly the kind of translational-validity caveat the project's schema is designed to capture explicitly rather than assume.
- **Applications:** This model enables study of the temporal sequence from mTEC differentiation defect → reduced thymopoiesis → tumorigenesis, and provides a platform for preclinical testing of GTF2I-pathway-directed therapeutics (none yet clinically available, representing a translational opportunity).

**Cell-line/in vitro models:** Not prominently returned in this search pass; thymic epithelial tumor cell lines are notoriously difficult to establish (a recognized limitation in the field, consistent with the low proliferative/mutational-burden biology of GTF2I-driven tumors), which is part of why the knock-in mouse model represented a significant advance.

**Resources:** No dedicated thymoma-specific model organism database was identified; models are documented in the primary literature (JTO, Communications Biology) rather than centralized repositories like MGI with a disease-specific portal.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease | MONDO:0006451 (thymoma); OMIM:274230 |
| Related disease | Good syndrome / immunodeficiency with thymoma |
| Gene | HGNC:4661 (GTF2I); HGNC:11998 (TP53); HGNC:1787 (CDKN2A) |
| Cell types | CL:0002365 (medullary thymic epithelial cell) and cortical TEC counterpart (verify via OAK); CL:0000084 (T cell) |
| Phenotypes | HP:0003473 (Myasthenia); HP:0004313 (Decreased circulating antibody level); HP:0000508 (Ptosis); HP:0002015 (Dysphagia) |
| Anatomy | UBERON:0002370 (thymus) |
| Treatment | NCIT:C15329 (Surgical Procedure); NCIT:C15313 (Radiation Therapy); NCIT:C15632 (Chemotherapy); NCIT:C93352 (Targeted Therapy) |
| Therapeutic agents | CHEBI (sunitinib, everolimus); NCIT:C20401-class biologics (pembrolizumab) |

*(All ontology IDs above should be run through OAK verification per dismech SOP before use in a curated entry — none have been independently re-verified against `runoak info` in this research pass and are offered as starting candidates only.)*

---

## Sources

- [Orphanet: Thymoma](https://www.orpha.net/en/disease/detail/99867)
- [Thymoma: An Overview (PMC10527963)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10527963/)
- [The 2015 WHO Classification of Tumors of the Thymus (PMC4581965)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4581965/)
- [Histologic Classification of Thymoma, JTO](https://www.jto.org/article/S1556-0864(15)33335-9/fulltext)
- [Genomic clustering analysis identifies molecular subtypes of TETs (PMC8202771)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8202771/)
- [Immunological function of thymoma and pathogenesis of paraneoplastic MG (PMID:18401674)](https://pubmed.ncbi.nlm.nih.gov/18401674/)
- [Paraneoplastic Autoimmunity in Thymus Tumors (PMC2276007)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2276007/)
- [GTF2I gene mutation—a driver of thymoma pathogenesis, Mediastinum](https://med.amegroups.org/article/view/3900/4668)
- [Primary Driver Mutations in GTF2I Specific to the Development of Thymomas (PMC7466068)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7466068/)
- [A Knock-in Mouse Model of Thymoma with the GTF2I L424H Mutation (PMC9691559)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691559/)
- [Human thymoma-associated mutation of GTF2I impairs TEC progenitor differentiation (PMID:36175547)](https://pubmed.ncbi.nlm.nih.gov/36175547/)
- [GTF2I Mutation in Thymomas: Independence From Racial-Ethnic Backgrounds (PMC8419886)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8419886/)
- [Somatic Mutations of TETs, THYMOGENE Trial (PMID:41405018)](https://pubmed.ncbi.nlm.nih.gov/41405018/)
- [Epidemiology of thymomas and thymic carcinomas in the US and Germany, 1999-2019 (PMC10805269)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10805269/)
- [Trends in the incidence of thymoma, thymic carcinoma, and thymic NET in the US (PMC6938371)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6938371/)
- [Epidemiology of thymoma and associated malignancies, JTO](https://www.jto.org/article/S1556-0864(15)32613-7/fulltext)
- [Clinical significance of age at diagnosis among TET patients (PMC7138550)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7138550/)
- [Masaoka-Koga and TNM Staging System in TETs (PMC8582470)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8582470/)
- [Evaluation of new TNM-staging system for thymic malignancies (PMC5712125)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5712125/)
- [Fatal adverse events in two thymoma patients treated with anti-PD-1 ICI](https://www.sciencedirect.com/science/article/abs/pii/S0169500219305082)
- [Immune-Therapy-Related Toxicity and Dramatic Remission After Pembrolizumab in Metastatic Thymoma (PMC8082155)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8082155/)
- [Fatal Toxicity Induced by anti-PD-1 ICI in Thymic Epithelial Tumor](https://www.tandfonline.com/doi/full/10.2217/imt-2021-0215)
- [Constitutional Factors and Irradiation as Risk Factors for Thymoma (PMC11431288)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11431288/)
- [When the Good Syndrome Goes Bad: A Systematic Literature Review (PMC8185358)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8185358/)
- [Thymoma associated with hypogammaglobulinaemia and pure red cell aplasia (PMC3797656)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3797656/)
- [Insights from a Case of Good's Syndrome (PMC10296089)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10296089/)
- [Molecular and Functional Key Features and Oncogenic Drivers in Thymic Carcinomas](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10778094/)
- [Genomic Landscape of Thymic Carcinoma, AACR GENIE Cohort (PMC12839660)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12839660/)
- [Targeted NGS of TETs: KIT, ERBB2, KRAS, TP53 in Thymic Carcinomas (PMC9324890)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9324890/)
- [Central tolerance to self revealed by the autoimmune regulator (PMC4654700)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4654700/)
- [Update on Aire and thymic negative selection](https://onlinelibrary.wiley.com/doi/abs/10.1111/imm.12831)
- [Acquired myasthenia gravis with polymyositis/myocarditis secondary to thymoma in a dog (PMC8541714)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8541714/)
- [Metastatic thymoma and acquired generalized MG in a beagle (PMC1716736)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1716736/)
- [Canine Epithelial Thymic Tumors: Outcome in 28 Dogs Treated by Surgery (PMC8698125)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8698125/)
- [Merck Veterinary Manual: Neurological Paraneoplastic Syndromes in Small Animals](https://www.merckvetmanual.com/generalized-conditions/paraneoplastic-disorders-in-small-animals/neurological-paraneoplastic-syndromes-in-small-animals)
- [Update in diagnostic imaging of the thymus and anterior mediastinal masses (PMC6755948)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6755948/)
- [Role of Imaging in Diagnosis, Staging, Treatment of Thymoma, RadioGraphics](https://pubs.rsna.org/doi/abs/10.1148/rg.317115505)
- [Anti-titin antibodies in myasthenia gravis: tight association with thymoma (PMID:11405802)](https://pubmed.ncbi.nlm.nih.gov/11405802/)
- [Immunological and Structural Characterization of Titin Main Immunogenic Region (PMC9952892)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9952892/)
- [NCCN Thymomas and Thymic Carcinomas Guidelines v2.2025](https://jnccn.org/view/journals/jnccn/23/6/article-p255.xml)
- [Thymoma and Thymic Carcinoma Treatment (PDQ), NCI](https://www.cancer.gov/types/thymus-cancer/hp/thymoma-treatment-pdq)
- [Second primary malignancy risk after thymic epithelial tumors, SEER analysis](https://jtd.amegroups.org/article/view/113290/html)
- [The risk of second primary malignancy in patients with localized thymoma, JCO abstract](https://ascopubs.org/doi/10.1200/JCO.2019.37.15_suppl.8568)