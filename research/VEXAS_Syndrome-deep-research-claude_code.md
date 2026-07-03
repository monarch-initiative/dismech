---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-29T11:05:09.973824'
end_time: '2026-06-29T11:09:58.072764'
duration_seconds: 288.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: VEXAS Syndrome
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
  web_search_requests: 6
  num_turns: 10
  total_cost_usd: 2.1377249999999997
  session_id: 646a5f71-11a0-49de-827d-67cdbcfe2859
  stop_reason: end_turn
citation_count: 10
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** VEXAS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **VEXAS Syndrome** covering all of the
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

I have enough well-sourced material to write the comprehensive report. Writing it now.

---

# Comprehensive Research Report: VEXAS Syndrome

> **Scope note:** VEXAS is a young disease — first defined in late 2020 — so essentially the entire literature is "recent." I've prioritized the landmark discovery paper, the large NIH/NHGRI cohorts, the 2023 population-prevalence study, and 2023–2025 mechanism and treatment work. Evidence-source types are tagged per the dismech convention (HUMAN_CLINICAL, IN_VITRO, MODEL_ORGANISM, COMPUTATIONAL).

---

## 1. Disease Information

**Overview.** VEXAS syndrome is a severe, adult-onset, treatment-refractory autoinflammatory disease driven by *acquired* (somatic) loss-of-function mutations in the X-linked gene **UBA1**, the apex enzyme of the ubiquitylation cascade. The mutation arises in hematopoietic stem and progenitor cells (HSPCs), so it sits at the crossroads of **autoinflammation** and **clonal hematologic disease (myelodysplastic syndrome, plasma-cell dyscrasias)**. The name is an acronym coined in the discovery paper:

> **V**acuoles, **E**1 enzyme, **X**-linked, **A**utoinflammatory, **S**omatic — *Beck DB et al., NEJM 2020* (PMID:33108101).

It is best understood as a clonal hematopoietic disorder masquerading as, and overlapping with, a host of rheumatologic syndromes (relapsing polychondritis, Sweet syndrome, polyarteritis nodosa, giant cell arteritis, undifferentiated systemic inflammation). It unified many previously "idiopathic" adult inflammatory presentations under a single molecular cause.

**Key identifiers.**
- **MONDO:** MONDO:0026777
- **OMIM:** #301054 (VEXAS SYNDROME)
- **Orphanet:** ORPHA:596753
- **GARD:** 15001
- **MeSH:** indexed under "VEXAS syndrome" (introduced ~2022)
- **ICD-10/ICD-11:** No dedicated code yet; typically coded under autoinflammatory/myelodysplastic categories (ICD-10 D89.9 / D46.x). ICD-11 has no specific stem code as of this writing — **(data gap)**.

**Synonyms / alternative names.** "UBA1-related autoinflammatory disease"; "Somatic UBA1-mutation–associated autoinflammatory syndrome"; historically subsumed under "relapsing polychondritis with myelodysplasia," "Sweet syndrome with MDS," and "idiopathic adult-onset autoinflammatory disease."

**Data derivation.** Knowledge is a mix: deep-phenotyped **disease-level cohorts** (NIH/NHGRI, French GFEV, multicenter registries) plus a landmark **genome-first / EHR-linked** population study (Geisinger MyCode, PMID:36692560) that ascertained patients from sequencing rather than clinic — an unusual and valuable "reverse" ascertainment for a rare disease.

**Sources:** [NEJM 2020 (PMID:33108101)](https://pubmed.ncbi.nlm.nih.gov/33108101/) · [GeneReviews NBK614471](https://www.ncbi.nlm.nih.gov/books/NBK614471/) · [OMIM 301054](https://omim.org/entry/301054)

---

## 2. Etiology

**Primary cause (genetic, somatic).** VEXAS is caused by **somatic (post-zygotic, mosaic) mutations in UBA1** acquired in hematopoietic stem cells during adult life — it is **not inherited** and not a germline disease. The canonical mutations hit **codon 41 (p.Met41)**, which is the **alternative translation-initiation start codon for the cytoplasmic UBA1b isoform**. Loss of Met41 abolishes cytoplasmic UBA1b initiation; cells instead make a catalytically impaired, mislocalized isoform (UBA1c) from a downstream start site, crippling cytoplasmic ubiquitylation.

> "We identified 25 men who had somatic mutations in *UBA1*... The mutations were found in peripheral-blood cells... the somatic mutations affected methionine-41 (p.Met41)." — Beck DB et al., NEJM 2020 (PMID:33108101). *(HUMAN_CLINICAL)*

**Risk factors.**
- **Age:** Strongest determinant. Disease is essentially adult-only, median onset mid-60s; risk rises with age (consistent with age-related clonal hematopoiesis as the soil for acquiring the UBA1 mutation). 
- **Sex (male):** Because UBA1 is X-linked, males (one X) need only a single somatic hit to reach a pathogenic mutant allele fraction. Males ≈96% of cases.
- **Clonal hematopoiesis:** VEXAS is mechanistically a form of clonal hematopoiesis; co-occurring **DNMT3A** and **TET2** mutations are common and may precede or accompany the UBA1 clone.
- **Genetic risk in females:** Females generally require an additional event — **acquired monosomy X (loss of the wild-type X), X-inactivation skewing, or a second somatic hit** — to manifest, which explains their rarity. (PMID:33108101; GeneReviews NBK614471).

**Protective factors.** No established environmental protective factors. The closest "protective" genetic concept is the **mutation-type gradient**: p.Met41Leu (which preserves more residual UBA1b translation) carries markedly better survival than p.Met41Val. Higher residual wild-type/UBA1b activity is protective at the cellular level (PMID:35793465, *Ferrada/Beck Blood 2022*, *IN_VITRO + HUMAN_CLINICAL*).

**Gene–environment interactions.** No proven exogenous trigger. The dominant "environment" is **endogenous aging hematopoiesis** providing the clonal substrate. Infection/inflammation can precipitate flares but is not a documented cause. **(Largely a data gap for true GxE.)**

---

## 3. Phenotypes

VEXAS is multisystem. Frequencies below are pooled from GeneReviews and major cohorts (NEJM 2020, JAMA 2023, French cohort). Mark these as **HUMAN_CLINICAL**.

**Constitutional / inflammatory**
- **Recurrent fevers** — 65–90%. HPO: **HP:0001954 (Recurrent fever)** / HP:0011947. Episodic, often weekly; adult onset; recurrent.
- **Weight loss / cachexia, fatigue, malaise** — very frequent. HP:0001824 (Weight loss).

**Skin (≈80%, often the presenting feature)**
- **Neutrophilic dermatosis / Sweet-syndrome–like lesions** — dominant pattern. HPO: **HP:0200035 (Neutrophilic dermatosis)** / HP:0000962 (Hyperkeratosis – not apt); best: HP:0200035.
- **Cutaneous vasculitis, leukocytoclastic vasculitis** — HP:0011008 / HP:0025476 (Cutaneous small vessel vasculitis).
- Skin biopsy classically shows a **leukocytoclastic and neutrophilic/histiocytoid infiltrate with myeloid precursors carrying the UBA1 mutation**.

**Cartilage / musculoskeletal**
- **Relapsing chondritis (auricular and nasal)** — 36–54%. HPO: **HP:0002770 (Chondritis)** / HP:0100786 (auricular). A large fraction of "relapsing polychondritis" in older men is actually VEXAS.
- **Inflammatory arthritis / polyarthralgia** — 28–58%. HP:0001369 (Arthritis).

**Eye (30–46%)**
- **Periorbital edema, scleritis, episcleritis, uveitis, orbital inflammation** — HPO: **HP:0100534 (Scleritis)**, HP:0000554 (Uveitis), HP:0100539 (Periorbital edema).

**Lung (35–55%)**
- **Pulmonary infiltrates, organizing pneumonia, pleural effusions, neutrophilic alveolitis** — HPO: **HP:0006530 (Abnormal pulmonary interstitial morphology)** / HP:0002113 (Pulmonary infiltrates) / HP:0002202 (Pleural effusion).

**Vascular / thrombotic (23–41%)**
- **Venous thromboembolism (DVT/PE)** predominant; some arterial. HPO: **HP:0002625 (Deep venous thrombosis)**, HP:0002204 (Pulmonary embolism), HP:0001907 (Thromboembolism). Episodic/recurrent.

**Hematologic (near-universal)**
- **Macrocytic anemia** — ~97%. HPO: **HP:0001972 (Macrocytic anemia)** / HP:0001903 (Anemia). Progressive, transfusion-dependent in many.
- **Cytoplasmic vacuoles in myeloid and erythroid precursors** (bone marrow) — the pathognomonic morphologic clue. HPO: closest is HP:0011273 (Abnormal myeloid cell morphology) — **(no precise "vacuolated precursor" HP term; data gap)**.
- **Thrombocytopenia** — 10–48%. HP:0001873.
- **Myelodysplastic syndrome (MDS)** — 31–53% (mostly low/very-low risk). HP:0002863 (Myelodysplasia).
- **Plasma-cell dyscrasia (MGUS / multiple myeloma)** — 10–25%. HP:0012184 (Abnormal circulating immunoglobulin) / monoclonal gammopathy.
- **Markedly elevated CRP/ESR** — near-universal. HP:0011227 (Elevated C-reactive protein level), HP:0003565 (Elevated erythrocyte sedimentation rate).

**Other**
- Orchitis/epididymitis, aseptic meningitis, gastrointestinal inflammation, hearing loss reported less commonly.

**Onset / severity / progression / QoL.** Onset adult (median ~66 y). Course is **chronic, relapsing-remitting with progressive cumulative organ damage**; severity moderate-to-severe and frequently glucocorticoid-dependent. QoL impact is high: chronic high-dose steroid exposure, transfusion dependence, recurrent hospitalization, and substantial fatigue/pain burden. Formal EQ-5D/SF-36 data are sparse — **(QoL instrument data gap)**.

---

## 4. Genetic / Molecular Information

**Causal gene.** **UBA1** (ubiquitin-like modifier-activating enzyme 1; E1 enzyme). HGNC: **HGNC:12469** (dismech CURIE form `hgnc:12469`); NCBI Gene 7317; Xp11.23; OMIM gene 314370. Encodes the **sole or principal E1** that charges ubiquitin with ATP and hands it to E2 conjugating enzymes — the obligatory first step of essentially all cellular ubiquitylation.

**Pathogenic variants (somatic, X-linked).**
- **Canonical codon-41 variants (≈80–90% of cases):**
  - **p.Met41Thr** — c.122T>C — most common; associated with more ocular inflammation; ~83% 5-yr survival.
  - **p.Met41Val** — c.121A>G — most aggressive; less chondritis, more undifferentiated systemic inflammation, **worst survival (~60–77% 5-yr)**; lowest residual UBA1b.
  - **p.Met41Leu** — c.121A>C — frequent skin/Sweet phenotype; **best survival (~100% 5-yr)**.
- **Splice and non-Met41 variants:** e.g., **c.118-1G>C, c.118-2A>C (splice-site), p.Ser56Phe, p.Gly477Ala**, and others that also impair cytoplasmic UBA1b — these broaden the variant spectrum and are recognized in later cohorts (Poulter JA et al., Blood 2021, PMID:33690795; and subsequent series). *(HUMAN_CLINICAL / IN_VITRO)*

**Classification.** Pathogenic / likely pathogenic per functional + segregation-with-disease evidence; these are **somatic mosaic** calls, so ACMG germline rules apply imperfectly — interpretation hinges on variant allele fraction (VAF) and functional data.

**Variant origin & allele fraction.** **Somatic, not germline.** Restricted to the hematopoietic compartment (blood/marrow), **absent in skin fibroblasts** — a key diagnostic discriminator. VAF ranges ~4–95%, typically high in peripheral myeloid cells; the mutation enriches in myeloid lineage over time.

**Population frequency.** Not present in germline population databases (gnomAD) as a constitutional variant — it is an acquired somatic event, so "allele frequency" is age- and tissue-dependent rather than a fixed population number.

**Functional consequence.** **Loss of cytoplasmic UBA1b** → global reduction in cytoplasmic ubiquitylation (a partial loss-of-function with downstream gain-of-inflammatory-function at the cellular level). Met41 is the AUG start for the catalytically active cytoplasmic isoform; its loss forces use of a downstream Met67 start producing the dysfunctional UBA1c.

> "Translation of cytoplasmic UBA1 contributes to VEXAS syndrome pathogenesis... patients with p.Met41Val have... lower residual translation of the normal cytoplasmic UBA1 isoform UBA1b." — Ferrada/Beck et al., Blood 2022 (PMID:35793465). *(IN_VITRO + HUMAN_CLINICAL)*

**Modifier genes.** Co-occurring clonal mutations — **DNMT3A, TET2** (clonal hematopoiesis), and MDS-associated genes — modify hematologic trajectory and malignant risk.

**Epigenetics.** No primary epigenetic cause; however, the therapeutic efficacy of **hypomethylating agents (azacitidine)** implies DNA-methylation–sensitive clonal biology. Direct methylome studies are limited — **(data gap)**.

**Chromosomal abnormalities.** **Acquired monosomy X / loss of wild-type X** is an important mechanism enabling disease in females and can accompany clonal evolution in males.

---

## 5. Environmental Information

- **Environmental/toxic factors:** None established as causal. **(Data gap.)**
- **Lifestyle factors:** No proven dietary/smoking/alcohol contribution to onset; smoking and cardiovascular risk factors are relevant only to thrombotic-complication management.
- **Infectious agents:** No infectious cause. Infections are a **leading cause of death** in VEXAS (immunosuppression + cytopenias), and intercurrent infection can trigger flares — but VEXAS is **not** an infectious disease. NCBI Taxonomy: not applicable.

The "environmental" driver is essentially **endogenous somatic mutagenesis in aging hematopoiesis**.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Somatic UBA1 p.Met41 mutation in an HSPC** → loss of cytoplasmic UBA1b → **global reduction in cytoplasmic ubiquitylation**. *(initiating lesion; IN_VITRO + HUMAN_CLINICAL, PMID:33108101, PMID:35793465)*
2. **Impaired ubiquitin–proteasome protein quality control** → **ER stress and activation of the unfolded protein response (UPR)** and dysregulated autophagy in mutant myeloid cells.
3. **Innate immune activation:** mutant monocytes/myeloid cells show **inflammasome activation, NF-κB and type I/II interferon signatures, and elevated IL-6, IL-1β, TNF-α**. Defective Lys63/Met1 (linear) polyubiquitylation of inflammatory signaling complexes dysregulates death/inflammation checkpoints.

> "Mutant cells showed decreased ubiquitylation [activating] cellular stress responses that lead to upregulation of the unfolded-protein response... and a shared gene expression signature consistent with the activation of multiple innate immune pathways." — Beck DB et al., NEJM 2020 (PMID:33108101). *(IN_VITRO)*

4. **Myeloid bias and dysplastic hematopoiesis:** UBA1-mutant clones outcompete in the myeloid lineage; recent work shows **inflammation and myeloid bias can arise via partly independent mechanisms** downstream of UBA1 loss (Nature 2025, s41586-025-09815-0). The cytoplasmic **vacuoles** in marrow precursors are a morphologic readout of this proteostatic/autophagic stress.
5. **Aberrant regulated cell death:** Uba1-mutant macrophages undergo **RIPK1/RIPK3-linked inflammatory cell death**, amplifying sterile inflammation (biorxiv 2025; mechanistic literature). *(MODEL_ORGANISM / IN_VITRO)*
6. **Clinical output:** chronic, relapsing multi-organ neutrophilic/cytokine-driven inflammation **plus** progressive bone-marrow failure and clonal evolution to MDS/plasma-cell disease.

**Molecular pathways / GO suggestions:**
- **GO:0016567** protein ubiquitination (DECREASED) — the core lesion
- **GO:0000209** protein polyubiquitination
- **GO:0030968** endoplasmic reticulum unfolded protein response (INCREASED)
- **GO:0006914** autophagy (dysregulated)
- **GO:0032606** type I interferon production / **GO:0034340** response to type I interferon (INCREASED)
- **GO:0070423** nucleotide-binding oligomerization domain containing signaling / **GO:0140447** cytokine precursor processing (inflammasome) (INCREASED)
- **GO:0043123** positive regulation of canonical NF-κB signaling (INCREASED)
- **GO:0097190** apoptotic signaling / RIPK1-dependent necroptosis (INCREASED)

**Cell types (CL suggestions):**
- **CL:0000576** monocyte (key dysregulated effector)
- **CL:0000775** neutrophil (neutrophilic dermatosis, alveolitis)
- **CL:0000037** hematopoietic stem cell (clonal origin)
- **CL:0000839** myeloid lineage restricted progenitor cell
- **CL:0000764** erythroid lineage cell (vacuolated precursors) / **CL:0000557** granulocyte monocyte progenitor cell
- **CL:0000786** plasma cell (associated dyscrasia)

**Subcellular (GO cellular component):** GO:0005783 endoplasmic reticulum; GO:0005829 cytosol (site of lost UBA1b activity); GO:0000502 proteasome complex.

**Immune involvement:** Prototypic **autoinflammatory** (innate-driven) disease, not classic autoimmunity — though autoantibody/overlap features occur. Cytokine drivers: IL-6, IL-1β, TNF-α, type I/II IFN.

**Molecular profiling:** Transcriptomics of patient marrow/blood shows interferon + inflammatory signatures arising **early in primitive HSPCs and the myeloid lineage** (Cell Reports Med / iScience 2023; PMC12092610, S2666379123003130). Single-cell genotype–phenotype mapping links the mutant clone directly to the inflammatory program and suggests therapeutic vulnerabilities (biorxiv 2024.05.19.594376). *(IN_VITRO / COMPUTATIONAL)*

---

## 7. Anatomical Structures Affected

**Primary site:** **Bone marrow / hematopoietic system** — the origin and engine. UBERON: **UBERON:0002371 (bone marrow)**, UBERON:0000178 (blood).

**Multi-organ secondary involvement (UBERON):**
- Skin — **UBERON:0002097 (skin of body)** / UBERON:0000014 (zone of skin)
- Cartilage — auricular **UBERON:0001691 (external ear)** / nasal cartilage **UBERON:0001737 (laryngeal cartilage—approx.)**; cartilage tissue **UBERON:0002418**
- Eye — **UBERON:0000970 (eye)**; sclera UBERON:0001773; orbit UBERON:0001697
- Lung — **UBERON:0002048 (lung)**; pleura UBERON:0000175
- Blood vessels (veins) — **UBERON:0001638 (vein)**; vasculature UBERON:0002049
- Joints — **UBERON:0000465 (material anatomical entity—joint)** / UBERON:0001485 (synovial joint approx.)

**Body systems:** hematopoietic/immune, integumentary, respiratory, cardiovascular (venous), musculoskeletal, ocular/visual, occasionally nervous (aseptic meningitis) and reproductive (orchitis).

**Tissue/cell level:** myeloid and erythroid bone-marrow precursors (vacuolated); circulating monocytes and neutrophils; dermal neutrophilic/histiocytoid infiltrates; cartilage perichondrial inflammation.

**Subcellular:** ER (UPR), cytosol (ubiquitylation failure), proteasome; characteristic cytoplasmic vacuoles.

**Localization/laterality:** Generally **systemic and bilateral** (e.g., bilateral auricular chondritis, periorbital edema), though skin and pulmonary lesions can be patchy/asymmetric.

---

## 8. Temporal Development

- **Onset:** **Adult/late-onset.** Median ~66 y (IQR ~63–73); essentially never pediatric (somatic clonal acquisition with age). HPO onset: HP:0003581 (Adult onset) → HP:0003596 (Middle age onset)/late onset. Pattern usually **insidious/subacute** with episodic flares.
- **Progression / stages:** No formal staging. Conceptually: (1) early relapsing inflammatory phase often misdiagnosed as a rheumatologic syndrome → (2) glucocorticoid-dependent chronic inflammation with emerging cytopenias → (3) progressive marrow failure / transfusion dependence and clonal evolution (MDS, plasma-cell disease) → (4) end-stage cytopenias, infection, or transformation.
- **Course:** **Chronic, relapsing-remitting with cumulative organ damage**; lifelong. Spontaneous durable remission is rare; remissions are typically **treatment-induced** (steroids, JAK inhibitors, hypomethylating agents) or **curative only via allogeneic transplant**.
- **Critical window:** Earlier molecular diagnosis (recognizing VEXAS behind "relapsing polychondritis / Sweet / MDS in an older man") opens the window for clone-directed therapy and transplant evaluation before irreversible marrow failure.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Prevalence (landmark genome-first study, Geisinger MyCode, 163,096 unselected adults):** ~**1 in 4,269 men >50 y** and ~**1 in 26,238 women >50 y**; ~1 in 13,591 unrelated individuals >50 y overall.

> "...estimated prevalence of disease-associated UBA1 variants... 1 in 4269 men and 1 in 26,238 women older than 50 years." — Beck DB et al., JAMA 2023;329(4):318-324 (PMID:36692560). *(HUMAN_CLINICAL)*

- This reframed VEXAS from "ultra-rare" to a **relatively common cause of unexplained adult inflammation** in older men, almost certainly under-diagnosed. Incidence figures are not yet firmly established — **(data gap)**.

**Genetics of transmission.**
- **Inheritance pattern:** **Not inherited** — somatic/acquired. Functionally **X-linked** in the sense that the male single-X dosage explains the strong sex skew, but there is **no germline transmission to offspring** and **no recurrence risk in families**.
- **Penetrance:** Among carriers identified genome-first, penetrance of the combined inflammatory+hematologic phenotype was reported as high (approaching ~100% in symptomatic ascertainment), though milder/oligosymptomatic carriers are increasingly recognized.
- **Expressivity:** Highly variable (chondritis-predominant vs skin-predominant vs MDS-predominant), partly by genotype.
- **Anticipation / germline mosaicism / founder effects / consanguinity / carrier frequency:** Not applicable (somatic disease).

**Demographics.**
- **Sex ratio:** Strongly male; ~**96% male / ~4% female** (females usually require monosomy X or skewed XCI).
- **Age distribution:** Overwhelmingly >50 y; peak 6th–8th decades.
- **Ethnic/geographic distribution:** Reported worldwide across ancestries; no strong ethnic predilection established (the major cohorts are US and European). No endemic geography (not environmental/infectious).

---

## 10. Diagnostics

**Definitive test — molecular.**
- **UBA1 somatic mutation detection** in **peripheral blood and/or bone marrow** (myeloid-enriched fractions increase sensitivity). Methods: targeted Sanger (high-VAF), **NGS panels**, ddPCR, or WGS/WES (caution: high-VAF somatic UBA1 can be **misread as hemizygous germline** on exome — PMID:36038944). Confirm **somatic status** by absence in skin fibroblasts/non-hematopoietic tissue.

**Morphologic clue.**
- **Bone marrow aspirate:** **cytoplasmic vacuoles in myeloid and erythroid precursor cells** — the original "V." Highly suggestive but not 100% specific/sensitive.

**Laboratory.**
- Persistently **elevated CRP/ESR**; **macrocytic anemia** (high MCV), variable thrombocytopenia/leukopenia/monocytopenia; ferritin often high. LOINC: CRP (LOINC:1988-5), ESR (LOINC:4537-7), MCV (LOINC:787-2), Hemoglobin (LOINC:718-7).
- SPEP/immunofixation for monoclonal protein (plasma-cell dyscrasia screen).

**Imaging.** CT chest for pulmonary infiltrates/effusions; vascular imaging for VTE; cross-sectional imaging for large-vessel vasculitis when GCA/large-vessel overlap suspected.

**Histopathology.** Skin/marrow biopsy: neutrophilic/leukocytoclastic infiltrates, perichondrial inflammation; marrow shows myeloid hyperplasia ± dysplasia and vacuolated precursors.

**Diagnostic criteria.** **No validated formal criteria yet.** Working approach (GeneReviews; Koster/Mayo and others): adult male with relapsing multisystem inflammation (chondritis/skin/eye/lung) **+ macrocytic anemia/cytopenias ± marrow vacuoles + steroid dependence** → test UBA1. Proposed clinical screening scores exist (e.g., to prioritize who to sequence) but are not consensus-finalized — **(data gap / evolving)**.

**Differential diagnosis (to distinguish):** relapsing polychondritis, Sweet syndrome, polyarteritis nodosa, giant cell arteritis/large-vessel vasculitis, adult-onset Still disease, MDS without autoinflammation, IgG4-related disease, Behçet disease. The unifying discriminator is the **somatic UBA1 mutation + marrow vacuoles + macrocytic anemia** in an older man.

**Screening.** No population newborn/carrier screening (somatic disease). Emerging concept: **opportunistic UBA1 testing** in older men presenting with otherwise-unexplained relapsing inflammation plus macrocytosis.

---

## 11. Outcome / Prognosis

- **Mortality / survival:** High. Estimated **5-year mortality up to ~50% from symptom onset** in early cohorts; the discovery cohort reported 10/25 deaths.

> "Of the 25 patients, 10 died during the study period." — Beck DB et al., NEJM 2020 (PMID:33108101). *(HUMAN_CLINICAL)*

- **Genotype-stratified 5-yr survival:** p.Met41Leu ~100% > p.Met41Thr ~83% > p.Met41Val ~60–77% (Ferrada/Beck, Blood 2022, PMID:35793465).
- **Disease-specific mortality drivers:** progressive cytopenias/marrow failure, **infection** (compounded by immunosuppression), thromboembolism, transformation to MDS/AML or progressive plasma-cell disease.
- **Prognostic factors:** **p.Met41Val genotype** and **transfusion dependence** predict worse survival; **ear chondritis** associates with *better* prognosis; co-mutations in myeloid-malignancy genes worsen outcome; age and comorbidity matter.
- **Morbidity:** Substantial — chronic steroid toxicity (osteoporosis, diabetes, infection), transfusion dependence, recurrent thrombosis, cumulative organ damage. Most patients fail to achieve durable drug-free remission.
- **Recovery potential:** No spontaneous cure; **allogeneic HSCT is the only potentially curative option** and can eradicate the mutant clone, at the cost of significant transplant-related morbidity/mortality.

---

## 12. Treatment

> No regulatory-approved therapy and **no consensus guideline** exist; management is empirical, drawn from cohorts/case series. Two strategic arms: **(A) suppress inflammation** and **(B) target/eradicate the UBA1-mutant clone**.

**A. Anti-inflammatory / immunosuppressive**
- **Glucocorticoids** — first-line, almost universally effective but disease is **steroid-dependent**; chronic toxicity drives the need for steroid-sparing agents. MAXO: **MAXO:0000058 (pharmacotherapy)** / corticosteroid; CHEBI:50858 (corticosteroid) / CHEBI:8378 (prednisone).
- **JAK inhibitors** — **ruxolitinib** is the most effective JAK inhibitor (superior to tofacitinib/baricitinib/upadacitinib), with meaningful clinical response in roughly half of treated patients.

> "Ruxolitinib is more effective than other JAK inhibitors to treat VEXAS syndrome." — Heiblig M et al., Blood 2022 (PMID:35609174). *(HUMAN_CLINICAL)*
  CHEBI:75045 (ruxolitinib); modality SMALL_MOLECULE; target JAK1/JAK2.
- **IL-6 inhibition (tocilizumab)** — partial benefit (~26% response). CHEBI/NCIT tocilizumab; modality MONOCLONAL_ANTIBODY.
- **IL-1 inhibition (anakinra, canakinumab)** — limited efficacy (<10%); anakinra can cause severe injection-site reactions in VEXAS.
- **Conventional DMARDs (methotrexate, azathioprine), TNF inhibitors** — generally **poorly/inconsistently effective**.

**B. Clone-directed (hematologic)**
- **Hypomethylating agents — azacitidine** — clinical responses (~5/11 with concurrent MDS in GeneReviews summary) and, importantly, **occasional deep/complete molecular remission of the UBA1 clone**, sometimes permitting therapy de-escalation.

> "Two patients achieved complete molecular remission of the underlying UBA1 mutant clone... receiving treatment with the hypomethylating agent azacitidine." — *Blood / Annals of Hematology 2023–2025 reports.* *(HUMAN_CLINICAL)*
  CHEBI:2038 (azacitidine); MAXO chemotherapy/pharmacotherapy.
- **Allogeneic hematopoietic stem cell transplantation (allo-HSCT)** — the **only curative therapy**; eradicates the mutant clone. Systematic review/meta-analysis supports efficacy in selected, fit patients, balanced against transplant-related mortality (Nature BMT 2024, s41409-024-02375-3). MAXO: **MAXO:0001175/MAXO:0010039 (hematopoietic/organ transplantation)**; modality CELL_THERAPY.

**Emerging / experimental.** UBA1-targeted and clone-selective strategies, optimized HMA + JAKi combinations, and refined transplant conditioning are under active study. Recent retrospective treatment-outcome cohorts (Lancet Rheumatology 2025, PIIS2665-9913(25)00034-7) are defining comparative effectiveness. Relevant trial registries: search ClinicalTrials.gov for "VEXAS" (e.g., natural-history/genetics protocol **NCT06004349**; several interventional JAKi/HMA studies). **(Add specific NCT IDs at curation time.)**

**Supportive care.** Transfusion support, infection prophylaxis (especially under steroids/JAKi/HMA — PJP prophylaxis), anticoagulation for VTE, bone protection, vaccination. MAXO:0000950 (supportive care).

**Pharmacogenomics.** No VEXAS-specific PGx; standard JAKi/azacitidine considerations apply.

---

## 13. Prevention

- **Primary prevention:** None possible — disease arises from a random somatic mutation in aging hematopoiesis; no modifiable exposure, no vaccine. 
- **Secondary prevention (early detection):** The highest-yield "prevention" is **earlier diagnosis** — testing UBA1 in older men with unexplained relapsing inflammation + macrocytic anemia to intervene before marrow failure. Genome-first ascertainment (PMID:36692560) shows latent/under-recognized cases exist.
- **Tertiary prevention (complications):** VTE prophylaxis/anticoagulation, **infection prophylaxis** during immunosuppression, steroid-toxicity mitigation (bone, glucose), transfusion-iron management, and timely transplant referral to prevent clonal progression.
- **Genetic counseling:** Reassurance that VEXAS is **somatic and not heritable** — no offspring/sibling recurrence risk, no prenatal/carrier testing indicated. This is an important counseling point distinguishing it from germline autoinflammatory syndromes.
- **Public-health/environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (NCBITaxon:9606). No naturally occurring animal counterpart described.
- **Orthologous gene:** *Uba1* is highly conserved — mouse **Uba1** (NCBI Gene 22201), zebrafish **uba1**. Strong evolutionary conservation of the ubiquitin-activation step makes the mechanism studyable across species.
- **Natural disease in animals (OMIA/veterinary):** None reported — **(data gap / not applicable)**. There is no spontaneous companion-animal or wildlife VEXAS analog on record.
- **Comparative biology:** The disease itself is human-specific (requires the human UBA1b cytoplasmic-isoform start-codon architecture at Met41 plus age-related clonal hematopoiesis); engineered animal models (below) are the route to cross-species mechanistic study.
- **Transmission/zoonosis:** Not applicable (non-communicable, somatic).

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*):** *uba1*-perturbation models recapitulate **IRF3 accumulation, excessive type I interferon, and inflammation**, supporting the proximal-ubiquitylation→IFN mechanism. *(MODEL_ORGANISM)* — useful for innate-immune readouts and drug screening. ZFIN resource.
- **Mouse (*Mus musculus*):** Conditional/hematopoietic **Uba1-mutant or knockdown models** show **UPR activation and myeloid bias**, with recent work dissecting inflammation vs myeloid-bias as **partly independent** of RIPK3–CASP8 (Nature 2025, s41586-025-09815-0). *(MODEL_ORGANISM)* MGI resource; IMPC for *Uba1* alleles.
- **In vitro / cellular:** Patient-derived **monocytes/macrophages and CD34+ HSPCs**, iPSC-derived myeloid cells, and engineered Met41-mutant cell lines reproduce **reduced ubiquitylation, ER/UPR stress, inflammasome activation, and RIPK1-mediated death**. *(IN_VITRO)* — workhorse systems for mechanism and therapeutic-vulnerability screens (single-cell genotype–phenotype mapping, biorxiv 2024.05.19.594376).
- **Phenotype recapitulation:** Models reproduce the **molecular/inflammatory** arms well (ubiquitylation defect, UPR, IFN/inflammasome, myeloid skewing). 
- **Limitations:** No single model fully reproduces the **multi-organ relapsing clinical syndrome** (chondritis, skin, vacuolated precursors, MDS evolution) seen in patients; the **age-dependent somatic-clonal** acquisition and the human-specific UBA1b isoform context are hard to mimic. Treat model→human translation as a **HUMAN_MODEL_MISMATCH** candidate where mouse/zebrafish data inform mechanism but human-disease fidelity remains open.
- **Resources:** MGI, IMPC, ZFIN, Cellosaurus (patient/iPSC lines), GEO (patient transcriptomics).

---

## Key Citations (PMID-anchored)

| Claim | Reference | PMID | Evidence type |
|---|---|---|---|
| Discovery; UBA1 p.Met41 somatic mutation; vacuoles; 25 men; 10 deaths | Beck DB et al. *NEJM* 2020;383:2628-2638 | **33108101** | HUMAN_CLINICAL + IN_VITRO |
| Population prevalence (1/4269 men >50) | Beck DB et al. *JAMA* 2023;329:318-324 | **36692560** | HUMAN_CLINICAL |
| Cytoplasmic UBA1b translation; genotype–survival (Val worst) | Ferrada/Beck et al. *Blood* 2022;140:1496-1506 | **35793465** | IN_VITRO + HUMAN_CLINICAL |
| Novel/expanded UBA1 variant spectrum (splice, non-Met41) | Poulter JA et al. *Blood* 2021;137:3676-3681 | **33690795** | HUMAN_CLINICAL |
| Ruxolitinib superior among JAK inhibitors | Heiblig M et al. *Blood* 2022 | **35609174** | HUMAN_CLINICAL |
| Exome can misread high-VAF somatic UBA1 as hemizygous | (case report) | **36038944** | HUMAN_CLINICAL |
| Comprehensive clinical/genetic synthesis | GeneReviews: VEXAS Syndrome (Beck DB) | Bookshelf **NBK614471** | Review |
| Mechanism: inflammation vs myeloid bias independent | *Nature* 2025 (s41586-025-09815-0) | (PMID pending) | MODEL_ORGANISM |

**Sources (web):**
- [Beck et al. NEJM 2020 — PMID:33108101](https://pubmed.ncbi.nlm.nih.gov/33108101/)
- [Beck et al. JAMA 2023 — PMID:36692560](https://pubmed.ncbi.nlm.nih.gov/36692560/)
- [GeneReviews: VEXAS Syndrome — NBK614471](https://www.ncbi.nlm.nih.gov/books/NBK614471/)
- [OMIM #301054](https://omim.org/entry/301054)
- [Ferrada/Beck Blood 2022 — Translation of cytoplasmic UBA1 (PMC9523373)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9523373/)
- [Heiblig et al. Blood 2022 — Ruxolitinib (PMID:35609174)](https://pubmed.ncbi.nlm.nih.gov/35609174/)
- [Nature 2025 — Independent mechanisms of inflammation and myeloid bias](https://www.nature.com/articles/s41586-025-09815-0)
- [NCI/DCEG genome-first prevalence summary](https://dceg.cancer.gov/news-events/news/2023/vexas-uba1)
- [Bone Marrow Transplantation 2024 — allo-HSCT meta-analysis](https://www.nature.com/articles/s41409-024-02375-3)
- [Lancet Rheumatology 2025 — treatment outcomes cohort](https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(25)00034-7/fulltext)

---

## Curation notes for the dismech entry (`kb/disorders/VEXAS_Syndrome.yaml`)

- **Category:** Complex — clean fit; this is a clonal-hematopoietic **autoinflammatory** disorder bridging rheumatology and hematology.
- **MONDO:** MONDO:0026777 · **Gene:** `hgnc:12469` (UBA1) · note **somatic** origin in the genetic block (GENO somatic mutation, not germline inheritance).
- **Pathophysiology causal chain** to encode: UBA1b loss → ↓cytoplasmic ubiquitylation (GO:0016567 DECREASED) → ER/UPR stress (GO:0030968 INCREASED) → inflammasome/NF-κB/type-I-IFN (GO:0034340, GO:0043123 INCREASED) → myeloid-biased dysplastic hematopoiesis + multi-organ neutrophilic inflammation.
- **Module conformance candidates:** This is a natural fit for an autoinflammation / innate-immune-dysregulation pattern; if a "clonal hematopoiesis" or "type-I-interferonopathy"-adjacent module exists or is created, link it. (No exact existing module from the CLAUDE.md list maps cleanly — flag as a possible new-module opportunity rather than forcing a fit.)
- **Before committing evidence:** every PMID above must be `just fetch-reference`'d and every `snippet:` verified as an **exact substring** of the real abstract (the quotes here are paraphrase-adjacent search excerpts and must be replaced with verified verbatim text). Run `just validate`, `just validate-references`, and `just validate-terms-file` on the file.
- **Data gaps flagged:** ICD-11 code; precise incidence; QoL instrument data; epigenome studies; animal natural-disease (OMIA); finalized formal diagnostic criteria. Consider `discussions` with `kind: KNOWLEDGE_GAP` for these, and `kind: HUMAN_MODEL_MISMATCH` for the model-organism translational gap.