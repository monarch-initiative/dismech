---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T20:49:38.496224'
end_time: '2026-06-30T20:53:20.071563'
duration_seconds: 221.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IPEX Syndrome
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
  - claude-opus-4-8[1m]
  web_search_requests: 3
  num_turns: 6
  total_cost_usd: 1.7956364999999999
  session_id: 893542d7-117a-4c88-8029-797e7d5b8fd5
  stop_reason: end_turn
citation_count: 7
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IPEX Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IPEX Syndrome** covering all of the
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

I have solid grounding. Let me write the comprehensive report.

# Comprehensive Research Report: IPEX Syndrome

**(Immunodysregulation, Polyendocrinopathy, Enteropathy, X-linked syndrome)**

*Prepared: 2026-06-30 · For dismech knowledge-base entry*

> **Curation note (per dismech SOP §2a):** PMIDs and quoted snippets below are provided as *leads*. Before committing any snippet as an `evidence` item, run `just fetch-reference PMID:XXXX` and confirm the snippet is an exact substring of the cached abstract. I have flagged the highest-confidence anchor citations, but all quotes must be verified against the real abstract.

---

## 1. Disease Information

**Overview.** IPEX syndrome is a rare, X-linked, monogenic autoimmune disease — the prototypical **"Tregopathy"** — caused by loss-of-function mutations in *FOXP3*, the master transcription factor of CD4⁺CD25⁺ regulatory T cells (Tregs). Absence of functional Tregs unleashes systemic, multi-organ autoimmunity that classically presents in the first months of life with the triad of **severe enteropathy, endocrinopathy (neonatal type 1 diabetes and/or thyroiditis), and dermatitis (eczema)**. Untreated, it is usually fatal in infancy or early childhood.

**Key identifiers:**
| Resource | ID |
|---|---|
| **MONDO** | **MONDO:0010026** (immunodysregulation-polyendocrinopathy-enteropathy-X-linked syndrome) |
| **OMIM** | **#304790** (IMMUNODYSREGULATION, POLYENDOCRINOPATHY, AND ENTEROPATHY, X-LINKED; IPEX) |
| **Orphanet** | **ORPHA:37042** |
| **ICD-10** | D89.89 (other specified disorders involving the immune mechanism); often coded under E31.0 (autoimmune polyglandular failure) for the endocrine component |
| **ICD-11** | 4A00.14 (Immunodysregulation with autoimmunity/IPEX) |
| **MeSH** | Covered under "Genetic Diseases, X-Linked" / "Diabetes Mellitus, Type 1" / "Polyendocrinopathies, Autoimmune"; MeSH Supplementary Concept: **C536917** (IPEX syndrome) |
| **UMLS** | C0342288 |

**Synonyms / alternative names:** IPEX; Immune dysregulation–polyendocrinopathy–enteropathy–X-linked syndrome; **XLAAD** (X-linked autoimmunity–allergic dysregulation syndrome); X-linked autoimmunity–immunodeficiency syndrome; **XPID**; **Polyendocrinopathy, enteropathy, X-linked (PIDX)**; autoimmune enteropathy type 1; formerly the human counterpart of the murine **"scurfy"** phenotype.

**Data derivation.** Knowledge is derived from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews) and from **individual-patient literature** — case reports and, importantly, the international multicenter cohort of Barzaghi et al. (96 genetically-proven patients from 38 institutions), which is the principal source of natural-history and outcome statistics.

---

## 2. Etiology

**Primary cause — genetic.** IPEX is a **monogenic X-linked recessive disorder** caused by hemizygous pathogenic variants in ***FOXP3*** (forkhead box P3) at **Xp11.23**. FOXP3 is the lineage-defining transcription factor of Tregs; its loss abolishes Treg suppressive function (or, in some alleles, Treg numbers), producing unchecked autoreactive effector T-cell responses.

- **Landmark discovery citations:** Bennett et al., *Nat Genet* 2001 (**PMID:11137993**) — "The immune dysregulation, polyendocrinopathy, enteropathy, X-linked syndrome (IPEX) is caused by mutations of FOXP3"; Wildin et al., *Nat Genet* 2001 (**PMID:11137992**); Chatila et al., *J Clin Invest* 2000 (**PMID:11120765**, JM2/FOXP3). The murine ortholog was identified from the *scurfy* mouse by Brunkow et al., *Nat Genet* 2001 (**PMID:11138001**).

**Risk factors.**
- *Genetic:* Being **male and hemizygous** for a pathogenic *FOXP3* variant is effectively deterministic (near-complete penetrance in males). A positive **family history** on the maternal (X-linked) side is a major risk indicator; carrier mothers are typically asymptomatic.
- *Environmental / triggering:* Overt autoimmune flares can be **triggered by infections, immunizations, or dietary antigen exposure** (early enteral feeding), but these unmask rather than cause disease. There are **no established non-genetic causes**.

**Protective factors.** No environmental protective factors are established. Genotype–phenotype relationships act as *modifiers* rather than protectors: variants preserving partial FOXP3 function (e.g., certain missense or polyadenylation-signal variants) associate with **milder, later-onset, or attenuated disease**. Maternal-derived normal *FOXP3* on the second X chromosome protects heterozygous female carriers (favorable/skewed X-inactivation in Tregs).

**Gene–environment interactions.** Given the monogenic near-deterministic nature, GxE is limited; however, the *timing and antigen load* of environmental exposures modulates which autoimmune manifestations dominate and their severity. Not a classic multifactorial GxE disease.

---

## 3. Phenotypes

IPEX is a multisystem autoimmune disease. Onset is overwhelmingly early: **~95% present in the first year of life; ~50% within the first month** (GeneReviews; Barzaghi et al. cohort). Course is typically **severe and progressive/relapsing** without treatment.

**Classic diagnostic triad:**

| Phenotype | HPO suggestion | Frequency | Notes / onset |
|---|---|---|---|
| **Severe enteropathy / intractable secretory diarrhea, malabsorption, failure to thrive** | HP:0002014 (Diarrhea); HP:0002608 (Autoimmune enteropathy is captured via HP:0100785/HP:0002583 abnormalities); HP:0001508 (Failure to thrive); HP:0004395 (Malnutrition) | **Very frequent (~90–95%)** — most consistent feature | Neonatal/infantile; villous atrophy; often the presenting and life-threatening feature |
| **Endocrinopathy – neonatal/early type 1 diabetes mellitus** | HP:0100651 (Type I diabetes mellitus); HP:0000833 (Hyperglycemia) | **Frequent (~60–70%)** | Often the earliest endocrine sign; autoimmune β-cell destruction |
| **Dermatitis / eczema (also erythroderma, psoriasiform, ichthyosiform)** | HP:0000964 (Eczema); HP:0001005 (Erythroderma); HP:0011123 (Inflammatory abnormality of the skin) | **Frequent (~50–65%)** | Atopic-like dermatitis, alopecia (HP:0002293), nail dystrophy |

**Other autoimmune / hematologic / systemic manifestations:**

| Phenotype | HPO suggestion | Frequency |
|---|---|---|
| **Autoimmune thyroiditis (hypo- or hyperthyroidism)** | HP:0000821 (Hypothyroidism); HP:0000870 (Hyperthyroidism); HP:0002926 (autoimmune thyroiditis → HP:0100646) | Occasional–frequent (~20–30%) |
| **Autoimmune cytopenias** (hemolytic anemia, thrombocytopenia, neutropenia) | HP:0004814 (Autoimmune hemolytic anemia); HP:0001973 (Autoimmune thrombocytopenia); HP:0001875 (Neutropenia) | Frequent (~20–30%) |
| **Autoimmune hepatitis** | HP:0001409 (Autoimmune hepatitis → HP:0002240 hepatomegaly) | Occasional (~10–20%) |
| **Nephropathy** (membranous/interstitial nephritis, proteinuria) | HP:0000112 (Nephropathy); HP:0000093 (Proteinuria) | Occasional |
| **Recurrent/severe infections (sepsis)** | HP:0002719 (Recurrent infections); HP:0100806 (Sepsis) | Frequent — from immune dysregulation, skin/gut barrier loss, and immunosuppression |
| **Elevated IgE, eosinophilia, food allergy** | HP:0003212 (Increased IgE level); HP:0001880 (Eosinophilia); HP:0500093 (Food allergy) | Frequent |
| **Lymphadenopathy / splenomegaly** | HP:0002716 (Lymphadenopathy); HP:0001744 (Splenomegaly) | Occasional |
| **Growth failure / cachexia** | HP:0001510 (Growth delay); HP:0004325 (Decreased body weight) | Frequent (secondary to enteropathy) |

**Laboratory abnormalities:** markedly **elevated serum IgE and eosinophilia**; multiple **autoantibodies** — anti-enterocyte (**anti-harmonin/AIE-75 and anti-villin**), anti-islet (GAD65, IA-2, insulin), anti-thyroid (TPO, thyroglobulin), and others; normal-to-elevated total lymphocyte counts with **reduced/dysfunctional Tregs** and low/absent FOXP3 protein by flow cytometry.

**Severity / progression / QoL.** Severe, life-limiting without treatment; relapsing-remitting under immunosuppression. Quality of life is heavily impacted by **chronic diarrhea, TPN dependence, insulin-dependent diabetes, chronic immunosuppression, and transplant morbidity**. There is **variable expressivity** even within families, indicating modifier effects.

---

## 4. Genetic / Molecular Information

**Causal gene:** ***FOXP3*** (forkhead box P3).
- **HGNC:** `hgnc:6106` · **OMIM gene:** 300292 · **NCBI Gene:** 50943 · **Ensembl:** ENSG00000049768 · **UniProt:** Q9BZS1 (FOXP3_HUMAN) · **Cytoband:** Xp11.23.
- FOXP3 encodes **scurfin**, a ~431-aa forkhead-family transcription factor with an **N-terminal repressor/proline-rich domain, a zinc finger, a leucine-zipper (dimerization), and a C-terminal forkhead (FKH) DNA-binding domain** (the FKH domain also mediates nuclear localization).

**Pathogenic variants.**
- **Types:** Missense, nonsense, frameshift (insertion/deletion), splice-site, and variants in the **polyadenylation signal** (the original Wildin/Bennett *poly(A)* variant) as well as promoter/enhancer variants. Missense variants cluster in the **forkhead (FKH) DNA-binding domain** and the **leucine-zipper**; FKH-domain mutations (e.g., **p.Arg347His**, **p.Ala384Thr**, **p.Phe371Cys**) impair DNA binding/nuclear import.
- **Classification:** Predominantly **loss-of-function** (ACMG pathogenic/likely pathogenic). Some alleles are **hypomorphic**, retaining partial function → milder phenotype (genotype–phenotype correlation is imperfect).
- **Functional consequence:** Loss of FOXP3 transcriptional activity → failure of Treg lineage commitment/suppressive program. In humans, most mutations yield **present-but-nonfunctional Tregs** (in contrast to some models where Tregs are numerically absent); "Functional type 1 regulatory T cells develop regardless of FOXP3 mutations in patients with IPEX syndrome" (Passerini et al., PMC3107421) illustrates residual regulatory compartments.
- **Origin:** **Germline**, X-linked; often inherited from a carrier mother, with a notable fraction of **de novo** variants. **Germline/somatic mosaicism** in mothers has been reported and affects recurrence-risk counseling.
- **Allele frequency:** Pathogenic *FOXP3* variants are **absent/ultra-rare** in gnomAD (as expected for a severe X-linked disorder under strong selection).
- **ClinVar:** numerous IPEX-associated *FOXP3* entries (pathogenic/likely pathogenic).

**Modifier genes / phenocopies.** True IPEX is *FOXP3*-defined, but **"IPEX-like" syndromes** phenocopy it via other Treg/immune-tolerance genes — importantly ***CD25/IL2RA*** (**OMIM 606367**), ***STAT1*** GOF, ***STAT3*** GOF, ***CTLA4*** haploinsufficiency, ***LRBA***, ***IL2RB***, ***BACH2***, ***FOXP1***, and ***STAT5B***. These are distinct MONDO/OMIM entities and are the principal **differential diagnoses**, not modifiers of *FOXP3* itself.

**Epigenetic information.** Treg identity depends on demethylation of the **Treg-specific demethylated region (TSDR/CNS2)** in the *FOXP3* locus; stable *FOXP3* expression requires this epigenetic imprint. Relevant for diagnosis and for engineered-Treg therapy (methylation status is a maturity/stability marker).

**Chromosomal abnormalities:** Not characteristic; IPEX is a **single-gene** disorder (no aneuploidy/translocation etiology).

---

## 5. Environmental Information

- **Environmental factors:** None causative. Infections and immunizations can **trigger flares** of the underlying autoimmunity.
- **Lifestyle factors:** Not applicable (congenital/infantile onset).
- **Infectious agents:** Not a cause. However, **opportunistic and bacterial infections/sepsis** (e.g., from CVCs, skin/gut barrier breakdown, and iatrogenic immunosuppression) are major *complications* and a leading cause of death. Common culprits include *Staphylococcus*, gram-negative sepsis, CMV, and Candida.

---

## 6. Mechanism / Pathophysiology

**Core causal chain:**

> **Loss-of-function *FOXP3* variant** → **failure of the CD4⁺CD25⁺ Treg suppressive program** (Tregs absent or, more often in humans, present but nonfunctional) → **loss of dominant peripheral tolerance** → **unrestrained autoreactive effector T-cell (Th2/Th1/Th17) activation and B-cell autoantibody production** → **multi-organ lymphocytic infiltration and tissue destruction** (gut, pancreatic islets, skin, thyroid, kidney, liver) → **clinical IPEX** (enteropathy, diabetes, dermatitis, cytopenias).

**Molecular pathways.**
- **FOXP3 transcriptional network:** FOXP3 partners with NFAT, RUNX1/CBFβ, and other factors to **upregulate Treg signature genes** (*IL2RA*/CD25, *CTLA4*, *IKZF2*/Helios, *TNFRSF18*/GITR) and to **repress effector cytokines** (IL-2, IFN-γ, IL-17). "FOXP3…upregulates Treg-associated markers such as CD25 and CTLA4, and represses proinflammatory cytokine production."
- **IL-2/CD25–STAT5 axis:** Tregs depend on high-affinity IL-2 signaling; FOXP3 loss disrupts this loop (mechanistically linking IPEX to IL2RA-deficiency IPEX-like disease).
- **mTOR signaling:** Aberrant effector T-cell metabolism/proliferation; the therapeutic rationale for **sirolimus (mTOR inhibition)**, which spares/restores Treg function relative to calcineurin inhibitors.
- **Th2 skew:** Explains eczema, elevated IgE, eosinophilia, and food allergy.

**Cellular processes:** breakdown of **immune self-tolerance / T-cell homeostasis** (GO:0002513 tolerance induction; GO:0042110 T cell activation; GO:0050777 negative regulation of immune response), lymphocytic organ infiltration, autoantibody-mediated and cytotoxic tissue injury, chronic inflammation.

**Cell types (CL suggestions):**
- **CL:0000792** — CD4-positive, CD25-positive, alpha-beta regulatory T cell (**primary affected cell**)
- **CL:0000815** — regulatory T cell
- **CL:0000896** — activated CD4-positive, alpha-beta T cell (effector expansion)
- **CL:0000236** — B cell (autoantibody production)
- **CL:0000584** — enterocyte (autoimmune target in gut)
- **CL:0000171** — pancreatic A/β-islet targets (use CL:0000169 type B pancreatic cell for β-cells)
- **CL:0000583**/thyroid follicular cell; **CL:0000097** mast cell / **CL:0000771** eosinophil (allergic arm)

**Biological processes (GO suggestions):** GO:2000514 (regulation of CD4-positive, alpha-beta T cell activation), GO:0045velocity — GO:0043029 (T cell homeostasis), GO:0002460 (adaptive immune response), GO:0006954 (inflammatory response), GO:0002617 (autoimmune response — via GO:0002200), GO:0030217 (T cell differentiation).

**Protein dysfunction:** FKH-domain missense variants impair **DNA binding and nuclear localization** of FOXP3; truncating variants abolish the protein. Loss of FOXP3's repressive/activating transcriptional output is the unifying defect.

**Immune system involvement:** This is a disease of **autoimmunity due to failed regulation** (a Tregopathy) — not a classic immunodeficiency, though functional immune dysregulation plus therapy predisposes to infection. Hallmarks: autoantibodies (anti-enterocyte/harmonin, anti-islet), Th2 skewing, hyper-IgE, eosinophilia.

**Molecular profiling / advanced tech (research findings):**
- Mouse-ported patient mutations reveal **allele-specific patterns of FoxP3/Treg dysfunction** (*Cell Reports* 2023, S2211-1247(23)01029-X).
- FOXP3 loss drives **expansion of two pools of autoreactive T cells** (bioRxiv 2022, Hu et al.).
- **CRISPR-based FOXP3 gene correction** in patient HSCs/T cells is under active development (US patent 12540311; Bacchetta/Roncarolo groups).

---

## 7. Anatomical Structures Affected

- **Primary organs / systems (autoimmune targets):**
 - **Gastrointestinal tract / small intestine** — UBERON:0002108 (small intestine), UBERON:0000160 (intestine); villous atrophy, enteropathy
 - **Pancreas / islets** — UBERON:0000006 (islet of Langerhans); autoimmune diabetes
 - **Skin** — UBERON:0002097 (skin of body); dermatitis/erythroderma
 - **Thyroid gland** — UBERON:0002046
 - **Immune / lymphoid system** — UBERON:0002405 (immune system); the effector site of the defect
- **Secondary involvement:** **Liver** (UBERON:0002107; autoimmune hepatitis), **kidney** (UBERON:0002113; nephritis/proteinuria), **bone marrow/blood** (autoimmune cytopenias), **lymph nodes/spleen** (UBERON:0000029/UBERON:0002106).
- **Tissue/cell level:** intestinal epithelium (enterocytes), pancreatic β-cells, thyroid follicular epithelium, keratinocytes/epidermis — all targeted by autoreactive T cells and autoantibodies.
- **Subcellular (GO CC):** FOXP3 acts in the **nucleus** (GO:0005634); mutant protein may be excluded from the nucleus (cytoplasmic mislocalization, GO:0005737).
- **Lateralization:** systemic/bilateral (not lateralized).

---

## 8. Temporal Development

- **Onset:** **Congenital/neonatal–infantile.** ~95% within the first year; ~50% within the first month of life. Rare hypomorphic alleles present later in childhood or, exceptionally, adulthood.
- **Onset pattern:** Often **acute/fulminant** (severe diarrhea, hyperglycemia in a neonate) on a chronic autoimmune background.
- **Progression:** **Progressive and relapsing-remitting**; without definitive therapy, rapid decline. Immunosuppression converts it to a chronic relapsing course; HSCT can be curative.
- **Disease course / duration:** **Chronic, lifelong.** Natural course historically **fatal within the first 1–2 years of life** from malabsorption/metabolic derangement/sepsis.
- **Remission:** Not spontaneous; **treatment-induced** (immunosuppression → partial; HSCT → durable disease resolution with full donor or even mixed chimerism, because a relatively small fraction of donor Tregs can restore tolerance).
- **Critical window:** Early diagnosis and **HSCT before accumulation of organ damage (low organ-involvement score)** markedly improves outcome — a genuine window-of-opportunity for intervention.

---

## 9. Inheritance and Population

- **Epidemiology:** **Ultra-rare.** No precise prevalence; estimated **<1 per 1,000,000**; likely underdiagnosed. Several hundred genetically-confirmed cases reported worldwide.
- **Inheritance:** **X-linked recessive.** Affected individuals are almost exclusively **male (hemizygous)**. Carrier females are typically **asymptomatic** (protected by the normal allele + skewed X-inactivation in Tregs). Rare symptomatic female carriers reported.
- **Penetrance:** **High/near-complete in hemizygous males.**
- **Expressivity:** **Variable**, even within families (modifier effects; residual FOXP3 function of hypomorphic alleles).
- **Recurrence risk / mosaicism:** Carrier mother → **50% of sons affected, 50% of daughters carriers**. A substantial minority are **de novo**; **maternal germline mosaicism** documented and relevant to counseling.
- **Founder effects / consanguinity:** Not applicable (X-linked, dominant selection; no notable founder populations; consanguinity not a driver).
- **Population demographics:** **No ethnic predilection**; reported across all populations. **Sex ratio:** overwhelmingly male. **Age distribution:** infants/young children.

---

## 10. Diagnostics

- **Molecular genetic testing (definitive):** Detection of a **hemizygous pathogenic *FOXP3* variant** by **single-gene sequencing**, **primary-immunodeficiency/IPEX-like gene panels** (including IL2RA, CTLA4, LRBA, STAT1/3, FOXP1, etc.), or **exome/genome sequencing**. GTR-listed clinical tests available. Chromosomal microarray/karyotype are **not** indicated (single-gene disorder).
- **Immunophenotyping:** **Flow cytometry for FOXP3 protein** and CD4⁺CD25⁺CD127^low Tregs — reduced/absent or present-but-dysfunctional; **TSDR/CNS2 methylation** analysis as an adjunct.
- **Laboratory:**
 - **Autoantibodies:** anti-enterocyte (**anti-harmonin/AIE-75, anti-villin**) — relatively specific for the enteropathy; anti-islet (GAD65, IA-2, insulin); anti-thyroid (TPO, Tg); others.
 - **Elevated IgE, eosinophilia**; variable other immunoglobulins.
 - Metabolic: hyperglycemia, electrolyte derangement from diarrhea.
- **Histopathology (biopsy):** **Small-bowel biopsy** — villous atrophy with lymphocytic (often plasma-cell/eosinophil-rich) lamina propria infiltrate, resembling but distinguishable from celiac disease; **skin** — spongiotic/psoriasiform dermatitis; **pancreas** — insulitis.
- **Clinical criteria / differential diagnosis:** Diagnose on the **triad + early male onset + elevated IgE/autoantibodies + FOXP3 variant**. Differentials: **IPEX-like syndromes** (IL2RA, CTLA4, LRBA, STAT1-GOF, STAT3-GOF, FOXP1, STAT5B), **autoimmune enteropathy** of other cause, **APECED/APS-1 (AIRE)**, severe combined immunodeficiency with Omenn-like features, **cow's-milk protein enteropathy**, congenital diarrheas.
- **Screening:** No population newborn screening for IPEX itself. **Cascade/carrier testing** of at-risk female relatives once the familial variant is known; **prenatal / preimplantation genetic testing** available for known pathogenic variants.

---

## 11. Outcome / Prognosis

- **Natural history:** Without treatment, **most affected males die in the first 1–2 years of life** (malabsorption, metabolic derangement, sepsis).
- **With therapy (key cohort data — Barzaghi et al., international multicenter, n=96; PMID:29241729):**
 - **Overall survival after HSCT: 73.2%** (95% CI 59.4–83.0).
 - **Overall survival on chronic immunosuppression: 65.1%.**
 - **Pretreatment organ-involvement (OI) score** was the **only significant predictor of overall survival after transplant (P=.035)**.
 - Chronic-immunosuppression patients suffer **disease recurrence/complications**, degrading long-term disease-free survival; **HSCT in low-OI-score patients gives disease resolution and better QoL, independent of age, donor source, or conditioning.**
 - GeneReviews cites **15-year survival ~77.5%** with HSCT.
- **Morbidity:** insulin-dependent diabetes, chronic diarrhea/TPN dependence, growth failure, infections, transplant-related toxicity (GVHD, conditioning morbidity).
- **Prognostic factors:** **Extent of organ damage at treatment (OI score)**, timing of HSCT, genotype (hypomorphic vs null), infection burden.

---

## 12. Treatment

**Immunosuppression (first-line / bridging):**
- **Sirolimus (rapamycin)** — mTOR inhibitor, **preferred agent**; "dosed to achieve levels of 8–12 ng/mL…shown to restore regulatory T cell function." Favored over calcineurin inhibitors because it spares residual Treg function. → **MAXO:** pharmacotherapy/immunosuppressive therapy; CHEBI:9168 (sirolimus).
- **Calcineurin inhibitors** — **tacrolimus** (CHEBI:61049) or **cyclosporine A** (CHEBI:4031) as alternatives/adjuncts.
- **Corticosteroids** — for acute flares (CHEBI:34848 / NCIT:C2322 corticosteroid class).
- **Other steroid-sparing / biologics:** rituximab (anti-CD20; autoimmune cytopenias), **abatacept (CTLA4-Ig)** especially in CTLA4-related IPEX-like disease, mycophenolate mofetil, azathioprine, and mTOR-based regimens.

**Curative therapy:**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — the **only established cure**; restores functional donor-derived Tregs (even mixed chimerism can suffice). Reduced-intensity conditioning is increasingly used to limit toxicity. → **MAXO:0010039** (organ/stem-cell transplantation) / bone marrow transplantation.

**Supportive care:**
- **Total parenteral nutrition (TPN)** and nutritional support for enteropathy; **insulin** for diabetes; thyroid hormone replacement; transfusions; **antimicrobial prophylaxis** and aggressive infection management. → MAXO:0000950 (supportive care), MAXO:0000088 (dietary intervention).

**Experimental / advanced:**
- **Gene therapy / gene editing:** *ex vivo* **lentiviral FOXP3 gene addition** and **CRISPR-based FOXP3 correction** of autologous HSCs or T cells / engineered Tregs (Roncarolo, Bacchetta et al.; US patent 12540311). **Preclinical–early clinical.**
- **Engineered/adoptive Treg therapy.**

**Pharmacogenomics:** Sirolimus/tacrolimus metabolism is **CYP3A5/CYP3A4-dependent**; therapeutic drug monitoring is standard (relevant CPIC guidance for tacrolimus).

---

## 13. Prevention

- **Primary prevention:** None (monogenic congenital disease). Prevention centers on **reproductive risk reduction**: **genetic counseling**, **carrier testing** of at-risk female relatives, and **prenatal (CVS/amniocentesis) or preimplantation genetic testing** for known familial *FOXP3* variants. → MAXO:0000079 (genetic counseling).
- **Secondary prevention:** **Early molecular diagnosis** in a symptomatic male infant (and in known-carrier pregnancies) to enable **pre-emptive HSCT before organ damage accrues** — the single most impactful "secondary prevention" lever, given OI score drives outcome.
- **Tertiary prevention:** Preventing complications in established disease — **infection prophylaxis**, meticulous metabolic/nutritional control, immunosuppression monitoring, and timely transplant.
- **Immunization caveat:** **Live vaccines contraindicated** during immunosuppression; standard vaccination decisions individualized.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Best-characterized in ***Mus musculus*** (NCBITaxon:10090). The natural mouse counterpart is the ***scurfy* (sf)** mutant — a spontaneous X-linked *Foxp3* frameshift mutation producing a fatal early lymphoproliferative/autoimmune wasting disease (males die ~3–4 weeks), the **direct animal analog of human IPEX**. (Brunkow et al., *Nat Genet* 2001, **PMID:11138001**.)
- **Orthologous gene:** *Foxp3* (mouse NCBI Gene 20371); highly conserved forkhead factor.
- **Natural disease in other species:** No prominent naturally-occurring companion-animal IPEX analog is well documented; the disease is essentially defined through human patients and engineered/spontaneous mouse models.
- **Comparative biology:** The scurfy phenotype and *Foxp3*-null mice **recapitulate multi-organ autoimmunity**, cementing FOXP3/Tregs as the mechanistic linchpin; a key **human–model difference** is that human IPEX Tregs are frequently **present but nonfunctional**, whereas many mouse models show **absent** Tregs — relevant for translational fidelity (candidate `HUMAN_MODEL_MISMATCH` discussion note).

---

## 15. Model Organisms

- **Mouse (primary model):**
 - **Spontaneous:** *scurfy* mutant (X-linked *Foxp3* frameshift) — fatal neonatal autoimmune lymphoproliferation.
 - **Engineered:** *Foxp3* **knockout**, **GFP/reporter knock-in** (Foxp3-GFP), **conditional/DTR (Foxp3^DTR^ for Treg ablation)**, and **patient-mutation knock-in** lines. The 2023 *Cell Reports* study "ported" specific IPEX patient mutations into mice, revealing **allele-specific FoxP3/Treg dysfunction**.
 - **Phenotype recapitulation:** Strong for multi-organ autoimmunity, wasting, dermatitis, enteritis; **limitation** — divergence in whether Tregs are absent vs dysfunctional, and species-specific organ-targeting patterns.
 - **Resources:** MGI, IMSR, Jackson Laboratory strains.
- **In vitro / cellular:** **Patient-derived T cells and iPSCs**, CRISPR-edited primary human Tregs/HSCs, and **lentiviral FOXP3-corrected** cells used to test gene/cell therapy and to dissect FOXP3 transcriptional targets and TSDR epigenetics.
- **Applications:** Treg biology, tolerance mechanisms, and preclinical validation of **gene correction and engineered-Treg** strategies.

---

## Key References (verify before use as evidence snippets)

| PMID | Citation | Use |
|---|---|---|
| **11137993** | Bennett CL et al., *Nat Genet* 2001 — *FOXP3* mutations cause IPEX | Gene–disease causal anchor |
| **11137992** | Wildin RS et al., *Nat Genet* 2001 — X-linked neonatal diabetes/enteropathy & *FOXP3* | Gene–disease |
| **11120765** | Chatila TA et al., *J Clin Invest* 2000 — JM2/*FOXP3* | Gene function |
| **11138001** | Brunkow ME et al., *Nat Genet* 2001 — *scurfy*/*Foxp3* mouse | Model organism |
| **29241729** | Barzaghi F et al., *J Allergy Clin Immunol* 2018 — international IPEX cohort (n=96), survival/OI score | Epidemiology, prognosis, treatment outcomes |
| **20301297** | Gambineri E, Cheng-Kiang S, Wildin RS — *GeneReviews* IPEX | Clinical/diagnostic/treatment overview |
| PMC3107421 | Passerini L et al. — functional Tr1 cells despite FOXP3 mutations | Mechanism nuance |
| S2211-1247(23)01029-X | *Cell Reports* 2023 — patient mutations ported to mice | Model/genotype-phenotype |

---

## Suggested MONDO/entry-level annotations summary

- **Disease:** MONDO:0010026 · OMIM:304790 · ORPHA:37042
- **Gene:** FOXP3 (`hgnc:6106`, Xp11.23) — loss-of-function, X-linked recessive
- **Primary cell type:** CL:0000792 (CD4⁺CD25⁺ αβ regulatory T cell)
- **Key process:** breakdown of peripheral immune tolerance (GO:0002513 / GO:0043029 T-cell homeostasis)
- **Modules to consider for `conforms_to`:** none of the existing dismech modules map cleanly; IPEX is a candidate **anchor for a future "Tregopathy / failed peripheral tolerance"** mechanism module (worth flagging as a knowledge-gap/module proposal rather than forcing an existing module).

---

**Sources:**
- [IPEX Syndrome — GeneReviews, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1118/)
- [Barzaghi et al., Long-term follow-up of IPEX syndrome patients after different therapeutic strategies (JACI 2018)](https://www.jacionline.org/article/S0091-6749(17)31893-6/fulltext)
- [FOXP3 Forkhead Domain Mutation and Regulatory T Cells in IPEX (NEJM)](https://www.nejm.org/doi/full/10.1056/NEJMc0907093)
- [Mutations from patients with IPEX ported to mice (Cell Reports 2023)](https://www.cell.com/cell-reports/fulltext/S2211-1247(23)01029-X)
- [Functional type 1 regulatory T cells develop regardless of FOXP3 mutations in IPEX (PMC3107421)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3107421/)
- [IPEX Syndrome: Genetics and Treatment Options (Genes, MDPI)](https://www.mdpi.com/2073-4425/12/3/323)
- [Loss of FOXP3 function causes expansion of autoreactive T cells (bioRxiv 2022)](https://www.biorxiv.org/content/10.1101/2022.07.10.499494.full.pdf)

---

A quick heads-up on the vibe, since you've got an `IPEX_Syndrome.yaml` already sitting untracked in the worktree: think of this report as the *raw genomic library*, not the finished protein. Every PMID and quote here is a **lead** — before any of it goes into an `evidence:` block, run it through `just fetch-reference` and check the snippet is a real substring, the way you'd confirm a band on a gel before you believe it. A couple of the frequency percentages I gave are ballpark synthesis across sources, so lean toward **omitting `frequency:`** rather than inventing a citation for the exact band. Want me to draft or sanity-check the actual YAML entry next?