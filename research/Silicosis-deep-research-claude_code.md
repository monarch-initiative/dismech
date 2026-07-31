---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-16T11:20:50.751711'
end_time: '2026-07-16T11:26:07.387012'
duration_seconds: 316.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Silicosis
  mondo_id: ''
  category: Environmental Lung Disease
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
  - claude-opus-4-8
  web_search_requests: 8
  num_turns: 11
  total_cost_usd: 1.5141854999999997
  session_id: 7a0e5b0b-32b7-433e-b461-5488477a2b55
  stop_reason: end_turn
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Silicosis
- **MONDO ID:**  (if available)
- **Category:** Environmental Lung Disease

## Research Objectives

Please provide a comprehensive research report on **Silicosis** covering all of the
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

I now have enough to write the comprehensive report. Here it is.

---

# Comprehensive Research Report: Silicosis

**Prepared:** July 2026 · **Category:** Environmental / Occupational Lung Disease

> Scope note: Silicosis is an *environmentally acquired* fibrotic lung disease, not a Mendelian disorder. Consequently, several template sections framed around causal genes, inheritance patterns, and variant pathogenicity (Sections 4, 9-inheritance) are largely **not applicable** — for silicosis the genetics are *susceptibility/modifier* effects layered on an obligate environmental cause (respirable crystalline silica). I have flagged these explicitly rather than fabricating Mendelian content.

---

## 1. Disease Information

**Overview.** Silicosis is a chronic, irreversible, fibrotic interstitial lung disease (a pneumoconiosis) caused by the inhalation of respirable crystalline silica (RCS, silicon dioxide, SiO₂). Inhaled silica particles are phagocytosed by alveolar macrophages, triggering a self-perpetuating cycle of macrophage death, inflammation, and progressive collagen deposition that produces the pathognomonic silicotic nodule and, in advanced disease, progressive massive fibrosis (PMF). It is one of the oldest recognized occupational diseases and is entirely preventable but incurable.

**Key identifiers:**
- **MONDO:** MONDO:0005960
- **ICD-10-CM:** J62 (Pneumoconiosis due to dust containing silica); J62.8 (other silica-containing dust); J62.0 (talc)
- **ICD-11:** CA60.0 (Silicosis)
- **MeSH:** D012829 (Silicosis)
- **OMIM:** Not applicable — no single-gene Mendelian entry; silicosis is not a Mendelian disorder
- **Orphanet:** Not a rare disease per Orphanet (common occupational disease)
- **SNOMED CT:** 40122008 (Silicosis)

**Synonyms / alternative names:** Miner's phthisis, grinder's asthma/disease, potter's rot, stonemason's disease, "the dust disease," pneumosilicosis, silicotic fibrosis. Subtype-linked terms: acute silicosis (acute silicoproteinosis/silicolipoproteinosis), accelerated silicosis, chronic (simple and complicated) silicosis, conglomerate silicosis (= PMF).

**Data derivation.** Information is drawn overwhelmingly from **aggregated disease-level resources** (occupational-disease registries, surveillance programs such as Australia's Queensland screening program and US state case series, and clinical/pathology literature) rather than single-patient EHR records. The engineered-stone outbreak literature draws on clinical case series and lung-transplant/autopsy cohorts.

---

## 2. Etiology

### Disease causal factor (obligate environmental cause)
The **sole necessary cause is inhalation of respirable crystalline silica** — particles generally <5–10 µm aerodynamic diameter that reach the alveoli. Crystalline polymorphs, in order of typical toxicity relevance:
- **Quartz** (most common) — CHEBI/chemical: silicon dioxide, SiO₂
- **Cristobalite** and **tridymite** — higher-temperature polymorphs, more fibrogenic; generated by heating/calcining quartz and abundant in engineered-stone processing
- Freshly fractured silica (cutting, grinding, drilling) is more toxic than aged dust because fresh surfaces carry reactive silanol/radical groups.

**Amorphous silica** (e.g., diatomaceous earth in native form) is far less fibrogenic; calcination converts it to cristobalite, raising risk.

### Risk factors — environmental / occupational (the dominant drivers)
- **High-risk occupations:** engineered/artificial "quartz" stone countertop fabrication (the current epidemic driver), hard-rock and coal mining, sandblasting (especially denim sandblasting), quarrying, tunneling, foundry work, ceramics/pottery, glass manufacture, stone masonry, construction (concrete cutting), dental laboratory work, hydraulic fracturing (sand proppant).
- **Exposure intensity and duration** determine clinical form: cumulative dose drives chronic disease; very high short-term exposure drives accelerated/acute forms.
- **Engineered ("artificial") stone** is the key modern factor: it contains **>90% crystalline silica** (vs ~30% in granite, <5% in marble), producing ultrafine (<1 µm) high-surface-area particles and dramatically shortening latency. Dry cutting without adequate wet suppression or respiratory protection is the proximate exposure.
- **Cigarette smoking:** additive/synergistic for functional decline, COPD, and markedly for lung cancer risk.
- **Sex/age:** predominantly male (occupational exposure pattern); engineered-stone cases occur in strikingly *young* men (median ~33–55 y), often immigrant/marginalized workers.

### Risk factors — genetic (susceptibility/modifier only, not causal)
Genetic factors modulate *who develops disease and how severely* among the exposed; they are neither necessary nor sufficient:
- **TNF-α promoter polymorphisms** (−308 G/A, −238 G/A): the −308A allele is associated with increased silicosis risk, especially in Asian populations; −238 promoter variants associated with severe silicosis in Black South African miners (PMID:11874815). Meta-analytic adjusted OR for −238 was reported very high (~20.9) in one cohort.
- **IL-1 receptor antagonist (IL-1RA / IL1RN) +2018 polymorphism:** associated with susceptibility and severity (OR ~4.0).
- Candidate-gene meta-analyses also implicate variants in **IL-1β, IL-6, GSTM1/GSTT1/GSTP1 (glutathione-S-transferases), and HLA class II** genes, with modest and population-dependent effects. No genome-wide-significant common causal locus is established.

### Protective factors
- **Environmental/engineering:** wet cutting/dust suppression, local exhaust ventilation, enclosed automated processing, respiratory protection (powered air-purifying respirators), and regulatory exposure limits (US OSHA PEL 50 µg/m³ 8-h TWA for RCS; Australia's 2024 **ban on engineered stone**). These are the only proven protections.
- **Genetic protective factors:** none robustly established. Some anti-inflammatory cytokine alleles (e.g., high-IL-10 producers) have been hypothesized to be protective but are not confirmed.
- **Behavioral:** smoking cessation reduces downstream lung-cancer and COPD burden but does not prevent silicosis itself.

### Gene–environment interaction
Silicosis is a paradigm of gene–environment interaction: an obligate environmental exposure whose fibrotic outcome is modulated by host inflammatory-gene polymorphisms (TNF-α, IL-1RA, GST detoxification genes). The interaction is quantitative (risk/severity modulation) rather than qualitative — no host genotype confers disease without silica exposure.

---

## 3. Phenotypes

Silicosis is often asymptomatic for years, especially in the simple chronic form. Phenotypes below are grouped by type with suggested HPO terms.

**Respiratory symptoms/signs:**
- **Dyspnea / exertional breathlessness** — HP:0002094 (Dyspnea); the dominant symptom, progressive. Frequent, especially in complicated disease.
- **Chronic cough** — HP:0031246 (Chronic cough) / HP:0012735 (Cough). Common, often productive.
- **Sputum production** — HP:0033709 (Abnormal sputum) / HP:0031508.
- **Chest pain/tightness** — HP:0100749 (Chest pain).
- **Wheezing** — HP:0030828 (Wheezing).
- **Hemoptysis** — HP:0002105 (Hemoptysis); should prompt evaluation for superimposed tuberculosis or PMF cavitation.
- **Cyanosis** — HP:0000961 (Cyanosis); late/severe.
- **Bibasilar/diffuse crackles** — HP:0030830 (Crackles); prominent in acute silicoproteinosis.
- **Digital clubbing** — HP:0001217 (Clubbing); variable, less typical than in IPF.

**Physical/systemic manifestations:**
- **Fatigue** — HP:0012378 (Fatigue).
- **Weight loss** — HP:0001824 (Weight loss); acute/advanced disease.
- **Respiratory failure** — HP:0002878 (Respiratory failure); end-stage.
- **Pulmonary hypertension / cor pulmonale** — HP:0002092 (Pulmonary arterial hypertension); complication of advanced fibrosis.
- **Pneumothorax** — HP:0002107 (Pneumothorax); complication.

**Laboratory / imaging abnormalities:**
- **Restrictive (± mixed obstructive) ventilatory defect** — HP:0002091 (Restrictive ventilatory defect); reduced FVC, reduced DLCO on pulmonary function testing.
- **Pulmonary fibrosis** — HP:0002206 (Pulmonary fibrosis).
- **Pulmonary nodules / reticulonodular opacities** — HP:0031451 (Pulmonary nodule); upper/mid-lobe predominant small rounded opacities (ILO shapes q/r).
- **Hilar/mediastinal lymphadenopathy with "eggshell" calcification** — HP:0100721 (Hilar lymphadenopathy); eggshell calcification is characteristic.
- **Elevated inflammatory/autoimmune serology** — antinuclear antibodies, rheumatoid factor, ANCA may be positive (see Section 6/complications).

**Phenotype characteristics by clinical form:**
| Form | Onset (latency) | Severity | Progression | Frequency |
|---|---|---|---|---|
| Chronic simple | 10–30+ y | Mild–moderate, often asymptomatic | Slow, may be stable | Most common historically |
| Chronic complicated (PMF) | decades | Severe | Progressive (can progress after exposure ends) | ~subset of chronic |
| Accelerated | 3–10 y | Moderate–severe | Rapid | Rising sharply (engineered stone) |
| Acute (silicoproteinosis) | weeks–<5 y | Very severe | Rapid, often fatal | Rare, very high exposure |

**Age of onset:** adult; engineered-stone accelerated silicosis strikingly presents in the 3rd–5th decade. **Progression:** can continue *after cessation of exposure*, particularly complicated/PMF forms.

**Quality-of-life impact.** Advanced silicosis produces severe exertional limitation, oxygen dependence, inability to work (major socioeconomic impact given young affected workers), and psychological burden; PMF and lung-transplant candidacy indicate profound QoL reduction. No silicosis-specific validated instrument dominates; generic tools (SF-36, EQ-5D, St George's Respiratory Questionnaire) are used.

---

## 4. Genetic / Molecular Information

**Not applicable as a Mendelian disorder.** Silicosis has **no causal gene, no pathogenic germline/somatic variant catalog, no ClinVar/HGMD pathogenic-variant set, and no chromosomal abnormality.** It is not inherited.

What exists is **susceptibility/modifier genetics** (see Section 2):
- **Modifier/susceptibility genes:** TNF (HGNC:11892; TNF-α −308/−238 promoter SNPs), IL1RN (IL-1 receptor antagonist, +2018), and candidate variants in IL1B, IL6, GSTM1/GSTT1/GSTP1, and HLA class II. Effects are small-to-moderate, population-specific, and function as risk/severity modifiers.
- **Variant classification:** These are common-population **regulatory polymorphisms**, not ACMG "pathogenic" variants — the ACMG/AMP framework does not apply to a complex environmental trait.
- **Functional consequence:** promoter variants alter cytokine expression levels (e.g., higher TNF-α transcription with −308A), amplifying the inflammatory/fibrotic response to silica.

**Epigenetics:** Silica exposure induces epigenetic reprogramming in lung cells and macrophages — DNA-methylation changes and dysregulated microRNAs are implicated in fibrogenesis (e.g., downregulation of **miR-205-5p** → ↑E2F1/SKP2 → impaired Beclin1-mediated autophagy; downregulation of **miR-503** → ↑VEGFA/FGFR1 → ERK/MAPK activation). These are acquired, exposure-driven changes, not heritable disease mutations.

---

## 5. Environmental Information

- **Environmental/occupational factor (causal):** respirable crystalline silica dust — quartz, cristobalite, tridymite. Generated by mechanical disruption of silica-containing materials (see Section 2 occupations). Engineered stone is the dominant contemporary source.
- **Chemical entity:** silicon dioxide / crystalline silica (CHEBI: silicon dioxide, CHEBI:30563; quartz-specific and crystalline-SiO₂ terms also exist). IARC **Group 1 human carcinogen** (crystalline silica inhaled from occupational sources).
- **Lifestyle factors:** cigarette smoking (synergistic for lung cancer/COPD and functional decline). Diet/alcohol not established as major modifiers.
- **Infectious agents:** silica does not *cause* infection, but silicosis is a powerful *risk multiplier for infection* — notably **Mycobacterium tuberculosis** (NCBITaxon:1773) and nontuberculous mycobacteria; also increased susceptibility to community pneumonia and fungal infections. Silica impairs macrophage bactericidal function, explaining silicotuberculosis (see Sections 6 and 11).

---

## 6. Mechanism / Pathophysiology

Silicosis pathogenesis is a well-characterized causal cascade centered on the alveolar macrophage and the **NLRP3 inflammasome**.

### Causal chain (upstream → downstream)
1. **Deposition & recognition.** Respirable silica (<5 µm) deposits in terminal bronchioles/alveoli. Alveolar macrophages (CL:0000583, alveolar macrophage) recognize and internalize particles via **scavenger receptors**, especially **MARCO** and SR-A, forming phagosomes. *(GO:0006909 phagocytosis)*
2. **Lysosomal/phagolysosomal damage.** Reactive silanol surface groups rupture the phagolysosomal membrane → **lysosomal destabilization and leakage** (cathepsin B release). *(GO:0007042 lysosomal lumen acidification / membrane permeabilization)*
3. **Oxidative stress.** Silica surface radicals and mitochondrial dysfunction generate **reactive oxygen species (ROS)**. *(GO:0006979 response to oxidative stress)*
4. **NLRP3 inflammasome assembly.** Signal 1 (priming via TLR4/MyD88 → NF-κB) plus signal 2 (lysosomal rupture + ROS + extracellular ATP acting on the **P2X7 receptor**) drive **NLRP3–ASC–caspase-1** assembly. *(GO:0072559 NLRP3 inflammasome complex; GO:0002674 regulation of acute inflammatory response)*
5. **Cytokine maturation & macrophage death.** Caspase-1 cleaves pro-IL-1β and pro-IL-18 → mature **IL-1β / IL-18**, and cleaves **gasdermin D (GSDMD)** → **pyroptosis** (inflammatory macrophage death). Released silica re-enters new macrophages, perpetuating the cycle. *(GO:0070269 pyroptosis; GO:0050830 IL-1β secretion)*
6. **Inflammatory amplification / alveolitis.** IL-1β, TNF-α, IL-6, IL-17A, and chemokines (CXCL1, CCL3/MIP-1α, CXCL2/MIP-2; CXCR4/CXCL12 axis) recruit **neutrophils** (CL:0000775) and monocytes; neutrophil extracellular traps recruit fibrocytes.
7. **Epithelial injury & aberrant regeneration.** Type II alveolar epithelial cells (CL:0002063, type II pneumocyte) are injured and undergo **epithelial–mesenchymal transition (EMT)**. *(GO:0001837 EMT)*
8. **Fibroblast/myofibroblast activation.** **TGF-β1** (master pro-fibrotic cytokine), PDGF, CTGF, and bFGF drive **fibroblast → myofibroblast differentiation** (CL:0000186, myofibroblast cell), with signaling through TGF-β/SMAD, CD44-RhoA-YAP, and 4-1BB pathways. *(GO:0007179 TGF-β receptor signaling; GO:0060312 regulation of myofibroblast differentiation)*
9. **Excess ECM deposition & fibrosis.** Myofibroblasts deposit type I/III collagen → the concentric, whorled hyalinized **silicotic nodule**; coalescence produces **progressive massive fibrosis**. *(GO:0030198 extracellular matrix organization; GO:0072538 collagen fibril organization)*
10. **Architectural destruction → organ failure.** Progressive fibrosis → restrictive physiology, ↓DLCO, pulmonary hypertension, respiratory failure.

### Cellular processes
Phagocytosis, lysosomal membrane permeabilization, NLRP3 inflammasome activation, pyroptosis and apoptosis, ROS/oxidative stress, autophagy/mitophagy dysregulation, EMT, chronic inflammation, and fibrogenesis. ER stress in alveolar macrophages contributes to fibrogenesis (unfolded protein response).

### Immune system involvement
Silica is a chronic immune adjuvant/immunotoxicant: it drives Th17/IL-17A responses, dysregulates regulatory T cells, and promotes **autoantibody production**, mechanistically linking silicosis to autoimmune disease (rheumatoid arthritis, systemic sclerosis, SLE, ANCA-associated vasculitis; Caplan syndrome = silicosis + seropositive RA with cavitating nodules). Silica-impaired macrophage function underlies the ~30-fold increased tuberculosis risk.

### Molecular profiling
Transcriptomic and proteomic studies of silica-exposed lungs/macrophages show upregulation of inflammasome, TGF-β/SMAD, ECM, and EMT gene programs; single-cell and organotypic lung stem/progenitor models have demonstrated NLRP3-mediated epithelial injury and aberrant regeneration. RAGE (receptor for advanced glycation end-products) modulates the fibrotic response in murine silica models.

### Therapeutic-target implications
NLRP3/caspase-1/IL-1β axis, P2X7 receptor, TGF-β signaling, ROS (antioxidants: N-acetylcysteine), and autophagy restoration are active preclinical/clinical targets (Section 12).

---

## 7. Anatomical Structures Affected

- **Primary organ:** lung (UBERON:0002048), especially **upper and mid lung zones / posterior upper lobes** (predilection site of silicotic nodules and PMF). Body system: respiratory system (UBERON:0001004).
- **Secondary/associated involvement:** hilar and mediastinal **lymph nodes** (UBERON:0000029) — "eggshell" calcification; **pleura** (UBERON:0000977) — pleural thickening; **pulmonary vasculature / right heart** — pulmonary hypertension and cor pulmonale (cardiovascular system, UBERON:0004535); systemic immune involvement (autoimmune sequelae).
- **Tissue level:** alveolar interstitium and parenchyma; bronchiolar walls; lymphoid tissue. Fibrotic remodeling of connective tissue.
- **Cell populations targeted/involved (CL terms):**
  - Alveolar macrophage — CL:0000583
  - Type II pneumocyte (alveolar epithelial type II) — CL:0002063
  - Type I pneumocyte — CL:0002062
  - Lung fibroblast — CL:0002553 / myofibroblast — CL:0000186
  - Neutrophil — CL:0000775
  - Fibrocyte / recruited monocyte-derived cells
- **Subcellular compartments (GO Cellular Component):** phagosome/phagolysosome and lysosome (GO:0005764), mitochondrion (GO:0005739, ROS source), endoplasmic reticulum (GO:0005783, ER stress), NLRP3 inflammasome complex (GO:0072559), extracellular matrix (GO:0031012).
- **Localization/lateralization:** bilateral, typically symmetric; upper-zone predominant. PMF masses often bilateral and may cavitate (raising TB suspicion).

---

## 8. Temporal Development

- **Onset:** adult-onset, occupationally determined. Latency is inversely proportional to exposure intensity:
  - **Chronic:** ≥10 years (often 20–40) after low-moderate exposure.
  - **Accelerated:** 3–10 years after high exposure (engineered stone).
  - **Acute (silicoproteinosis):** weeks to <5 years after extreme exposure.
- **Onset pattern:** insidious (chronic) to subacute/acute (accelerated/acute forms).
- **Stages/progression:** simple silicosis (small opacities) → complicated silicosis/PMF (coalescent masses >1 cm). Progression can occur **even after exposure ceases**, particularly complicated disease. Acute silicoproteinosis progresses rapidly, often to fatal respiratory failure.
- **Course:** chronic, lifelong, generally **irreversible and non-remitting**; no spontaneous remission of established fibrosis. Critical "window": prevention is the only effective intervention — once fibrosis is established, disease-modifying options are limited to slowing progression.

---

## 9. Inheritance and Population

### Epidemiology
- **Global burden:** Silicosis carries a high and, in some regions, rising global burden. The Global Burden of Disease Study 2021 provides incidence, mortality, and DALY estimates across 204 countries; pneumoconioses (silicosis, coal-workers', asbestosis) remain a substantial occupational-disease burden, with silicosis the largest single contributor in many analyses. Hundreds of thousands of prevalent cases worldwide; high burden in China, India, and other industrializing economies.
- **Engineered-stone outbreak (contemporary epidemic):**
  - >1,000 engineered-stone silicosis cases identified worldwide since first reports ~2010 (Spain, Israel), then Australia and the US.
  - **United States (California):** first cases 2019; **52 cases by 2023**; **219 cases by November 2024**, including **≥14 deaths and 26 lung transplantations** — young, predominantly Latino immigrant male workers.
  - **Australia (Queensland screening, since 2018):** of 1,054 stone-benchtop workers screened, **224 (21%) had silicosis** and **36 (3.6%) had PMF** (as of Aug 2024). Australia became the **first country to ban engineered stone (July 2024).**
- **Prevalence/incidence:** varies enormously by industry and region; no single "cases per 100,000" applies. Occupational cohorts (mining, stone benchtop) show double-digit prevalence percentages among the exposed.

### Inheritance
- **Not heritable.** No Mendelian inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency applies. Susceptibility is polygenic/multifactorial at most (Section 2 modifier genes) and always contingent on exposure.

### Population demographics
- **Sex:** strongly male-predominant, reflecting occupational exposure distribution (male:female ratio high; engineered-stone cohorts are almost entirely male).
- **Age:** adults; engineered-stone accelerated cases cluster in young adults (median ~33–55 y).
- **Ethnic/socioeconomic:** disproportionately affects marginalized, immigrant, and low-income workers (US engineered-stone cases predominantly Latino immigrants). Geographic clustering follows mining/stone-processing industries and lax regulatory environments.
- **Variant geography:** not applicable (no disease-defining variants).

---

## 10. Diagnostics

Diagnosis rests on the triad: **(1) exposure history, (2) characteristic imaging, (3) exclusion of alternatives** — biopsy is usually unnecessary.

**Imaging (cornerstone):**
- **Chest radiograph** classified by the **ILO International Classification of Radiographs of Pneumoconioses** — small rounded opacities (profusion, shapes typically q/r), upper-zone predominance; large opacities (A/B/C) define complicated disease/PMF; "eggshell" calcification of hilar nodes.
- **HRCT** (higher sensitivity/specificity than CXR): centrilobular and subpleural micronodules, upper/mid-lobe predominance, conglomerate masses (PMF, often with surrounding emphysema and calcification), lymphadenopathy. RadLex/DICOM-coded.

**Functional tests:**
- Spirometry/full PFTs: restrictive, mixed, or (with smoking) obstructive pattern; **reduced DLCO**; reduced 6-minute walk distance / desaturation in advanced disease.

**Laboratory / biomarkers:**
- No validated diagnostic serum biomarker in routine use; research candidates include serum SP-D, KL-6/MUC1, CC16, and inflammatory cytokines.
- Autoimmune serologies (ANA, RF, ANCA) when overlap syndromes suspected.
- **Tuberculosis screening is mandatory** (IGRA/tuberculin, sputum studies) given silicotuberculosis risk.

**Histopathology (when biopsy performed):** whorled, concentric hyalinized collagen **silicotic nodules** with birefringent particles under polarized light; acute form shows alveolar filling with PAS-positive lipoproteinaceous material (silicoproteinosis, resembling alveolar proteinosis). Mineralogical analysis (SEM-EDX) can confirm silica.

**Genetic testing:** **Not applicable for diagnosis** (no causal gene). WGS/WES/panels/karyotype/FISH/CMA have no diagnostic role. Genotyping for susceptibility SNPs is research-only.

**Clinical criteria / differential diagnosis.** No DSM/formal consensus "criteria set" beyond exposure + imaging pattern; occupational-medicine society guidance (ATS, ACOEM, ILO) applies. Differential: coal-workers' pneumoconiosis, sarcoidosis (both can give upper-zone nodules and hilar adenopathy), tuberculosis, metastatic pulmonary calcification, hypersensitivity pneumonitis, idiopathic pulmonary fibrosis, berylliosis, pulmonary Langerhans cell histiocytosis. Exposure history and mineralogy distinguish silicosis.

**Screening.** Occupational surveillance of exposed workers (periodic ILO-classified CXR/HRCT + spirometry + TB screening), as in the Queensland engineered-stone program — a secondary-prevention model. No newborn/carrier/genetic screening (non-genetic disease).

---

## 11. Outcome / Prognosis

- **No cure.** Prognosis depends on form, radiographic category, and progression to PMF. Simple chronic silicosis may remain stable and compatible with near-normal lifespan; **complicated silicosis/PMF, accelerated, and acute forms carry poor prognosis.**
- **Acute silicoproteinosis:** frequently fatal within months–few years.
- **Accelerated/engineered-stone silicosis:** poor — high rates of progression to PMF, respiratory failure, **lung transplantation**, and death in young patients; US cohort documented ≥14 deaths and 26 transplants among 219 cases.
- **Mortality:** disease-specific mortality from respiratory failure and cor pulmonale; excess mortality from tuberculosis, lung cancer, and COPD.
- **Complications (major):**
  - **Tuberculosis (silicotuberculosis):** ~**30× increased risk** in silicosis (and ~3× in silica-exposed without silicosis); NTM infections also increased.
  - **Lung cancer:** crystalline silica is an **IARC Group 1 carcinogen**; increased lung-cancer risk, synergistic with smoking.
  - **Autoimmune/connective-tissue disease:** rheumatoid arthritis (incl. **Caplan syndrome**), systemic sclerosis/scleroderma, SLE, ANCA-associated vasculitis and glomerulonephritis; **chronic kidney disease** (silica nephrotoxicity/vasculitis).
  - **COPD/emphysema, chronic bronchitis, airflow obstruction.**
  - **Pulmonary hypertension and cor pulmonale; pneumothorax; recurrent respiratory infections; respiratory failure.**
- **Morbidity/QoL:** progressive disability, oxygen dependence, loss of employment; heavy socioeconomic impact given young working-age patients.
- **Prognostic factors:** exposure intensity/duration, radiographic profusion and presence/extent of PMF, rate of radiographic progression, DLCO/FVC decline, superimposed TB or malignancy, and continued exposure.

---

## 12. Treatment

**No disease-reversing therapy exists; management is supportive, complication-directed, and increasingly antifibrotic-experimental.** Suggested MAXO terms noted.

**Foundational / supportive care (MAXO:0000950 supportive care):**
- **Exposure cessation** (remove worker from silica) — essential first step.
- **Smoking cessation** (MAXO behavioral/counseling terms).
- **Oxygen therapy** for hypoxemia (MAXO:0035008 oxygen therapy / supplemental oxygen).
- **Pulmonary rehabilitation** (MAXO:0000915 rehabilitation / physiotherapy).
- **Vaccination** — influenza, pneumococcal (± SARS-CoV-2) to reduce respiratory infections (MAXO:0001017 vaccination).
- **Prompt treatment of respiratory infections.**

**TB prevention/treatment:**
- **Screening and treatment of latent/active tuberculosis** with standard antimycobacterial regimens (isoniazid, rifampicin, etc.) — critical given silicotuberculosis risk (MAXO:0000058 pharmacotherapy / antibiotic therapy).

**Pharmacotherapy (limited evidence):**
- **Corticosteroids** — may modestly reduce inflammation/alveolitis in some accelerated/acute cases; not disease-modifying for established fibrosis.
- **Antifibrotics — pirfenidone and nintedanib:** approved for IPF, showing benefit in silicosis animal models and small clinical studies (reducing inflammation/fibrosis, pulmonary hypertension in early disease); under active clinical investigation (e.g., **NCT05118256**, pirfenidone in complicated silicosis). Not yet standard-of-care/approved for silicosis.
- **N-acetylcysteine (antioxidant)** — protective in murine silicosis models; adjunctive human use investigational.
- **Investigational/preclinical targeted agents:** NLRP3 inflammasome inhibitors, IL-1 blockade, P2X7 antagonists, TGF-β pathway inhibitors, metformin, trehalose (autophagy inducers), and nanoparticle-targeted pulmonary delivery.

**Procedural:**
- **Whole-lung lavage (WLL)** — reduces dust/inflammatory burden; most useful in early and accelerated silicosis and acute silicoproteinosis; use cautiously in advanced disease (MAXO — therapeutic bronchopulmonary lavage / therapeutic procedure).
- **Lung transplantation** — the only definitive option for end-stage PMF/respiratory failure; increasingly performed in young engineered-stone patients (MAXO:0010039 organ transplantation).

**Pharmacogenomics:** Not applicable (no genotype-guided silicosis drug therapy established).

**Treatment strategy:** stage-based — remove exposure + supportive care + TB/infection and complication management for all; antifibrotic trials/WLL for progressive early disease; transplantation for end-stage. Personalized/precision approaches are investigational.

---

## 13. Prevention

Prevention is the **only truly effective intervention** — silicosis is 100% preventable.

- **Primary prevention (eliminate/reduce exposure):**
  - **Substitution/bans:** Australia's **engineered-stone ban (July 2024)**; substituting low-silica materials.
  - **Engineering controls:** wet cutting/water suppression, local exhaust ventilation, enclosed/automated processing, dust containment.
  - **Administrative controls & PPE:** enforced exposure limits (OSHA RCS PEL 50 µg/m³), respiratory protection (fit-tested respirators/PAPRs), worker training, hygiene.
  - **Regulatory enforcement and worker education**, especially targeting small stone-fabrication shops and immigrant workforces.
- **Secondary prevention (early detection):** occupational **medical surveillance** — periodic ILO-classified chest imaging, spirometry, and TB screening of exposed workers (Queensland program model); removal from exposure at earliest signs.
- **Tertiary prevention (limit complications):** TB chemoprophylaxis/treatment, vaccination, smoking cessation, pulmonary rehab, treatment of comorbidities, and lung-cancer vigilance.
- **Public-health interventions:** dust-control legislation, industry licensing, hazard communication, and international efforts (WHO/ILO Global Programme for the Elimination of Silicosis, targeting elimination).
- **Immunization:** no vaccine against silicosis; respiratory-pathogen vaccines reduce complication burden.
- **Genetic counseling / screening:** not applicable (non-genetic disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Silicosis-like pneumoconiosis can be induced experimentally in mammals; naturally occurring silica pneumoconiosis is reported in **horses** (Equus caballus, NCBITaxon:9796) — e.g., California ranch horses exposed to silica-rich (cristobalite) soil dust develop a silicate-associated pneumoconiosis and osteoporosis syndrome. Grazing livestock and possibly other animals in silica-dusty environments may be affected.
- **Veterinary relevance:** limited but documented (equine silicosis/silicate pneumoconiosis with bone fragility); primarily an environmental veterinary concern rather than a genetic one.
- **Comparative biology:** the macrophage–inflammasome–fibrosis mechanism is evolutionarily conserved across mammals, which is why rodent models faithfully reproduce nodular fibrosis. NLRP3 inflammasome biology is conserved.
- **Zoonosis/transmission:** none — silicosis is non-infectious and non-transmissible; it is an exposure disease with no cross-species transmission.

---

## 15. Model Organisms

Silicosis is modeled by **inducing silica exposure** (not genetic engineering), making animal models highly relevant.

- **Predominant model — mouse (Mus musculus, NCBITaxon:10090):**
  - **Strain:** **C57BL/6(J)** is the standard "high-responder," most susceptible to silica- and bleomycin-induced fibrosis (vs resistant strains such as CBA/J).
  - **Induction routes:** **oropharyngeal aspiration** of crystalline silica suspension (produces a superior, more reproducible silicosis model than intratracheal instillation), intratracheal/intranasal instillation, and repeated inhalation/nose-only exposure (a model built by repeated nasal silica inhalation better mimics chronic human exposure). Silica delivery produces fibrotic nodules resembling human silicotic lesions.
- **Rat models:** used for inhalation and instillation studies of silica fibrosis and for antifibrotic drug testing.
- **Comparison with bleomycin model:** the **bleomycin** model is the classic pulmonary-fibrosis model but is typically self-limited/resolving; the **silica model produces persistent, progressive nodular fibrosis** more faithful to human silicosis chronicity. Mechanistic divergences exist (e.g., RAGE knockouts are protected in bleomycin but not asbestos/silica-type fibrosis).
- **In vitro / cellular models:** primary and immortalized **alveolar macrophages** (e.g., MH-S), **THP-1** monocyte-derived macrophages, type II epithelial lines (A549, MLE-12), and fibroblast lines exposed to crystalline silica to dissect NLRP3 activation, pyroptosis, and EMT/fibroblast activation. **Lung stem/progenitor-cell-derived organotypic (organoid) models** have demonstrated NLRP3-mediated epithelial injury and aberrant regeneration.
- **Genetic models used as tools:** knockouts of *Nlrp3, Casp1, Il1b, Il1r1, P2rx7, Tnf, Ager* (RAGE), and *Marco* on silica-exposed backgrounds dissect pathway contributions (e.g., **NLRP3 deficiency abrogates silica-induced neutrophil infiltration, damage, and fibrosis**).
- **Phenotype recapitulation:** rodent silica models reproduce alveolar macrophage activation/pyroptosis, granulomatous silicotic nodules, neutrophilic alveolitis, TGF-β-driven collagen deposition, and restrictive physiology — strong fidelity. **Limitations:** rodents do not fully reproduce human PMF conglomerate masses, the decades-long chronicity, silicotuberculosis (rodents handle *M. tuberculosis* differently), or the human autoimmune spectrum. Particle dose/delivery is non-physiologic (bolus vs chronic aerosol).
- **Model resources:** MGI, IMPC/KOMP (for knockout alleles of pathway genes), and published silica-exposure protocols (JoVE, methods papers).

---

## Evidence Source Classification Summary

- **HUMAN_CLINICAL:** epidemiology (GBD 2021, engineered-stone case series in US/Australia/Spain/Israel), clinical forms, complications (silicotuberculosis, autoimmune associations), genetic-susceptibility case-control/meta-analyses, treatment/WLL/transplant series.
- **MODEL_ORGANISM:** murine/rat silica-instillation and knockout studies; equine natural disease; N-acetylcysteine and RAGE studies.
- **IN_VITRO:** macrophage/epithelial/fibroblast silica-exposure studies, organotypic lung-progenitor models.
- **COMPUTATIONAL:** network-pharmacology/molecular-docking studies of pirfenidone in silicosis.

---

## Key Sources / Citations

Verified identifiers should be confirmed against the local MONDO/HP/CL/GO adapters before entry (per the dismech anti-hallucination SOP). Suggested key references for curation (verify PMIDs and quote exact abstract substrings with `just fetch-reference` before use):

- Sherekar et al., "Global scenario of silica-associated diseases: emerging pathophysiology of silicosis and potential therapeutic regimes," *Toxicology Reports*, 2025 — [PMC11847043](https://pmc.ncbi.nlm.nih.gov/articles/PMC11847043/) (comprehensive mechanism review).
- "The role of inflammation in silicosis," *Frontiers in Pharmacology*, 2024 — [10.3389/fphar.2024.1362509](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1362509/full).
- "NLRP3 deficiency abrogates silica-induced neutrophil infiltration, pulmonary damage and fibrosis" — [PMC11929224](https://pmc.ncbi.nlm.nih.gov/articles/PMC11929224/).
- "A review of silicosis and other silica-related diseases in the engineered stone countertop processing industry," *J Occup Med Toxicol*, 2025 — [PMC11917111](https://pmc.ncbi.nlm.nih.gov/articles/PMC11917111/).
- "Deadly Countertops: An Urgent Need to Eliminate Silicosis among Engineered Stone Workers," 2025 — [PMC12005022](https://pmc.ncbi.nlm.nih.gov/articles/PMC12005022/).
- "Burden of silicosis based on the Global Burden of Disease Study 2021…" — [PMC11898348](https://pmc.ncbi.nlm.nih.gov/articles/PMC11898348/).
- "Global burden of pneumoconiosis from 1990 to 2021…" — [PMC12055836](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12055836/).
- Corbett et al., TNF-α promoter polymorphisms and severe silicosis in Black South African miners — [PMID:11874815](https://pubmed.ncbi.nlm.nih.gov/11874815/).
- "Candidate gene polymorphisms associated with silicosis and coal workers' pneumoconiosis: systematic review/meta-analysis" — [PMC11585218](https://pmc.ncbi.nlm.nih.gov/articles/PMC11585218/).
- "TNF-α 308G/A polymorphism and silicosis susceptibility: a meta-analysis," *PLoS One* — [PMC3790741](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3790741/).
- "From Basic Research to Clinical Practice: Considerations for Treatment Drugs for Silicosis" — [PMC10179659](https://pmc.ncbi.nlm.nih.gov/articles/PMC10179659/).
- Pirfenidone in complicated silicosis trial — [NCT05118256](https://clinicaltrials.gov/study/NCT05118256).
- "N-acetylcysteine therapeutically protects against pulmonary fibrosis in a mouse model of silicosis" — [PMC6639458](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6639458/).
- "The Role of RAGE in a Murine Model of Silicosis" — [PMC2841632](https://pmc.ncbi.nlm.nih.gov/articles/PMC2841632/).
- Silicosis overview — [Merck Manual Professional](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/silicosis); [Wikipedia](https://en.wikipedia.org/wiki/Silicosis).
- Silicotuberculosis — [PMC (silicotuberculosis outbreak, LA County)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12791545/); Caplan syndrome — [PMC8136599](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8136599/).
- ER stress in alveolar macrophages / silicosis fibrosis — [PMC10734631](https://pmc.ncbi.nlm.nih.gov/articles/PMC10734631/).
- NLRP3 in lung stem/progenitor organotypic models — [IJBS v19p1875](https://www.ijbs.com/v19p1875.htm).

> **Curation caveat (dismech SOP):** Two references are already cached in this branch (`PMID_18577586`, `PMID_18604214`) — verify their content and snippets before citing. Every PMID, ontology term (MONDO:0005960, HP/CL/GO/CHEBI IDs suggested above), and snippet in this report must be independently verified with `just fetch-reference` and `just validate-terms-file` before entering the KB, per the anti-hallucination workflow. The GBD-derived numeric burden figures and engineered-stone case counts should be pinned to the specific source table and quoted exactly.

**Sources (web):**
- [PMC11847043 — Global scenario of silica-associated diseases](https://pmc.ncbi.nlm.nih.gov/articles/PMC11847043/)
- [Frontiers Pharmacology 2024 — Role of inflammation in silicosis](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1362509/full)
- [PMC11917111 — Engineered stone silicosis review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11917111/)
- [PMC12005022 — Deadly Countertops](https://pmc.ncbi.nlm.nih.gov/articles/PMC12005022/)
- [PMC11898348 — GBD 2021 silicosis burden](https://pmc.ncbi.nlm.nih.gov/articles/PMC11898348/)
- [PMC12055836 — GBD pneumoconiosis 1990–2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12055836/)
- [PMID:11874815 — TNF-α polymorphisms, South African miners](https://pubmed.ncbi.nlm.nih.gov/11874815/)
- [PMC11585218 — Candidate gene polymorphism meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11585218/)
- [PMC10179659 — Treatment drugs for silicosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC10179659/)
- [NCT05118256 — Pirfenidone in complicated silicosis](https://clinicaltrials.gov/study/NCT05118256)
- [Merck Manual — Silicosis](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/silicosis)
- [Wikipedia — Silicosis](https://en.wikipedia.org/wiki/Silicosis)
- [MalaCards — Silicosis (identifiers)](https://www.malacards.org/card/silicosis)
- [ICD-10 J62](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J60-J70/J62-)