---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-02T16:42:56.629389'
end_time: '2026-08-02T16:48:00.892291'
duration_seconds: 304.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RYR2 CPVT
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 20
  num_turns: 23
  total_cost_usd: 1.9411572
  session_id: 94f4796d-ea94-552d-bee6-88ceab3d1e92
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RYR2 CPVT
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **RYR2 CPVT** covering all of the
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

I now have sufficient primary-source material to compose the full report.

# RYR2-Related Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT1): Comprehensive Research Report

## 1. Disease Information

**Overview.** Catecholaminergic polymorphic ventricular tachycardia (CPVT) is an inherited primary arrhythmia syndrome ("channelopathy") characterized by exercise- or emotion-induced bidirectional or polymorphic ventricular tachycardia (VT) in individuals with a structurally normal heart and a normal resting electrocardiogram. It is one of the most lethal of the inherited arrhythmia syndromes if untreated, with syncope, cardiac arrest, or sudden cardiac death (SCD) — sometimes as the first manifestation — occurring characteristically during physical exertion or acute emotional stress (GeneReviews, NBK1289, updated 2022; PMID:20301466).

**Key identifiers:**
- **OMIM (phenotype):** CPVT1, #604772 (with or without atrial dysfunction and/or dilated cardiomyopathy) — RYR2-related
- **OMIM (gene):** RYR2 *180902*
- Related OMIM subtypes: CPVT2 #611938 (CASQ2, gene *114251*); CPVT3 #614021 (TECRL, gene *617242*); CPVT4 #614916 (CALM1, gene *114180*); CPVT5 #615441 (TRDN, gene *603283*); CPVT6 #618782 (CALM3, gene *114183*)
- **Orphanet:** ORPHA3286 (Catecholaminergic polymorphic ventricular tachycardia)
- **MONDO:** MONDO:0011001 (catecholaminergic polymorphic ventricular tachycardia 1) is the RYR2-specific entity beneath the broader CPVT grouping term; MONDO integrates OMIM/Orphanet/ICD mappings for the umbrella and per-gene subtypes.
- **ICD-10:** I47.2 (Ventricular tachycardia, unspecified — CPVT has no dedicated ICD-10 code and is typically captured under this or I49.0)
- **MeSH:** Tachycardia, Ventricular (D017180); no CPVT-specific MeSH descriptor
- **HPO:** HP:0004758 (Paroxysmal ventricular tachycardia) / HP:0004756 (bidirectional ventricular tachycardia, if modeling that specific ECG pattern); HP:0001279 (Syncope); HP:0001645 (Sudden cardiac death)

**Synonyms:** CPVT; Familial polymorphic ventricular tachycardia; Bidirectional ventricular tachycardia (historical, for the classic ECG pattern); Catecholamine-induced polymorphic ventricular tachycardia; "Stress-induced polymorphic ventricular tachycardia."

**Evidence basis:** Information is derived predominantly from aggregated disease-level resources — multicenter clinical registries (e.g., the PACES CPVT registry, PMID for multi-genetic-variant analysis PMC6221297), GeneReviews expert consensus, systematic reviews/meta-analyses of published cohorts, ClinVar/gnomAD population variant databases, and mechanistic studies in iPSC-cardiomyocytes and animal models — rather than from a single large EHR-based cohort, reflecting the disease's rarity.

---

## 2. Etiology

**Disease Causal Factors.** CPVT is purely genetic/mechanistic in etiology — a primary "electrical disease" of cardiomyocyte Ca²⁺ handling, with no infectious or classic environmental causal factor. The disease is triggered (not caused) by adrenergic surges (exercise, acute emotion, occasionally auditory stimuli or fever).

**Genetic Risk Factors:**
- **RYR2** (autosomal dominant, gain-of-function): causal in **~50–65% of clinically diagnosed CPVT** (estimates range 50–70% across cohorts) (GeneReviews NBK1289; PMID:38542006).
- **CASQ2** (autosomal recessive, loss-of-function): ~2–5% of cases (CPVT2, OMIM #611938).
- **TRDN** (autosomal recessive): <1–5% of cases (CPVT5).
- **CALM1/CALM2/CALM3** ("calmodulinopathy," predominantly de novo, autosomal dominant): <1–2% combined; produce a mixed LQTS/CPVT/overlap phenotype (PMID review, Tandfonline 2023).
- **TECRL** (autosomal recessive): CPVT3, rare, combined CPVT/QT-prolongation phenotype.
- **KCNJ2**: rare, associated with some CPVT-like presentations distinct from classic Andersen-Tawil syndrome.
- Roughly **~25% of clinically diagnosed CPVT patients remain genetically unsolved** after comprehensive panel testing (GeneReviews NBK1289).
- De novo RYR2 variants account for an estimated 30–40% of RYR2-CPVT cases (no prior family history) (GeneReviews).

**Environmental/Demographic Risk Factors:**
- Age: mean onset **7–12 years** (childhood/adolescent onset is typical, though cases up to age 40 are reported).
- Sex: **male sex is a risk factor for earlier symptom onset and syncope/cardiac events** in RYR2-CPVT — relative risk of syncope ~4.2 in men vs. women in some cohort analyses.
- Physical exertion and competitive sports are the principal environmental precipitants; emotional stress is a secondary trigger.
- Digitalis/digoxin is a specific pharmacologic risk factor — it favors DAD-mediated triggered arrhythmia and is explicitly listed as an agent to avoid.

**Protective Factors:**
- No specific protective genetic variants are established; some RYR2 missense variants show markedly incomplete penetrance (a recent Bayesian penetrance-modeling study — medRxiv 2025.03.20.25324327 / PMC13108506 — reclassified variant risk using structural + population data), implying that certain domains/positions confer lower phenotypic risk even when "pathogenic" by ACMG criteria.
- Nonselective beta-blockade (nadolol) is the major modifiable protective intervention (pharmacologic, not innate).
- CYP2D6 pharmacogenetic variation affects propranolol clearance/efficacy (sex-dimorphic; testosterone upregulates CYP2D6, causing faster clearance/lower efficacy in men, partially explaining sex-based outcome differences).

**Gene-Environment Interactions:** The central GxE axis in CPVT is genotype (RyR2 leak threshold) × sympathetic/adrenergic state (exercise, emotion, occasionally fever). Beta-adrenergic stimulation via PKA/CaMKII phosphorylation of RyR2 lowers the store-overload-induced Ca²⁺ release (SOICR) threshold in already-destabilized mutant channels, converting a subclinical molecular lesion into life-threatening arrhythmia only under catecholamine surge — i.e., the genetic lesion is necessary but adrenergic environmental triggering is required for clinical events. A recent biorxiv 2025 preprint on CaMKII phosphorylation of RYR2 (2025.09.15.676430) reinforces CaMKII-dependent phosphorylation as "essential for arrhythmia in CPVT," a specific molecular GxE node.

---

## 3. Phenotypes

| Phenotype | Type | Onset/Course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Exercise/emotion-induced syncope | Symptom | Childhood–young adult; episodic/paroxysmal | Up to 80% of symptomatic patients (untreated) | HP:0001279 (Syncope) |
| Bidirectional ventricular tachycardia | Clinical sign (ECG) | Elicited by exercise stress test or epinephrine challenge | Classic but not universal finding | HP:0004756 (Bidirectional ventricular tachycardia) |
| Polymorphic ventricular tachycardia | Clinical sign (ECG) | Exercise-induced, progressive with workload | Common | HP:0004758 (Paroxysmal ventricular tachycardia) |
| Cardiac arrest / sudden cardiac death | Clinical outcome | Any age; may be first manifestation | ~30% experience cardiac arrest untreated; up to 30–50% mortality by age 30–35 untreated | HP:0001645 (Sudden cardiac death) |
| Palpitations, dizziness, chest pain | Minor symptoms | Variable | Common but nonspecific | HP:0001962 (Palpitations); HP:0002315 (Dizziness) |
| Normal resting ECG / structurally normal heart | Baseline finding | Persistent (diagnostic prerequisite) | By definition | HP:0001677 (Structural heart abnormality — absent) |
| Sinus bradycardia (RYR2 carriers) | Laboratory/ECG abnormality | Present at baseline in some carriers | Reported subset in pediatric RYR2-CPVT (Frontiers Pediatrics 2026 cohort) | HP:0001688 (Sinus bradycardia) |
| Supraventricular arrhythmias (atrial fibrillation/flutter, atrial standstill) | Clinical sign | Can co-occur, esp. with certain RYR2 variants ("CPVT1 with atrial dysfunction") | Subset | HP:0005110 (Atrial fibrillation) |
| Intellectual disability / neurodevelopmental delay | Behavioral/cognitive | Present from early childhood in a subset | ~8% of 421 CPVT1 patients in one cohort (95% CI 6–11%) (Circ Arrhythm Electrophysiol 2024, PMID underlying CIRCEP.124.013437) | HP:0001249 (Intellectual disability) |
| Autism spectrum features | Behavioral | Reported in rare RYR2-carrier case series linking calcium leak in neurons to ASD (medRxiv 2025.07.26.25332119) | Rare, emerging association | HP:0000717 (Autism) |
| Skeletal myopathy (mild) | Physical/laboratory | TRDN-related subtype | Rare, TRDN-specific | HP:0003198 (Myopathy) |
| QT prolongation | Laboratory/ECG | Calmodulinopathy (CALM1-3) and TECRL/TRDN "atypical CPVT" | Subset, gene-specific | HP:0001657 (Long QT interval) |

**Age of onset:** Mean 7–12 years; documented range from infancy (occasionally presenting as unexplained SIDS-associated RYR2 variants) to age 40.
**Severity/progression:** Highly variable expressivity — some RYR2 carriers remain asymptomatic lifelong (~50% of mutation carriers per some series, reflecting incomplete penetrance), while others present with SCD as the sentinel event. Course is typically stable-to-episodic under treatment; without treatment, risk of events accumulates with age and continued exposure to exertional/emotional triggers, described as "80% cumulative cardiac events by age 40 if untreated" in some series.
**Quality of life:** Activity restriction (competitive-sports contraindication) is the dominant QoL burden in children/adolescents; psychological burden of living with SCD risk and, in the neurodevelopmental subgroup, cognitive/behavioral impact are documented but not yet formally quantified with SF-36/EQ-5D instruments in the literature reviewed.

---

## 4. Genetic/Molecular Information

**Causal gene:** RYR2 (HGNC:10484; chromosome 1q43), encoding cardiac ryanodine receptor 2 (RyR2), the principal Ca²⁺-release channel of the sarcoplasmic reticulum (SR) in cardiomyocytes.

**Variant landscape:**
- CPVT-causing RYR2 variants are overwhelmingly **missense**, clustering in defined "hotspot" domains: **N-terminal domain (~aa 77–466), central domain (~aa 2246–2534), and the C-terminal channel/transmembrane and RyR/IP3R-homology-associated domains (~aa 3949–4332 and 4867–4967)** (Nature/J Hum Genet PMID underlying s10038-020-0738-6; recent structural-penetrance paper PMC13108506/medRxiv 2025.03.20.25324327).
- A large aggregation study identified **1,014 affected heterozygotes carrying 468 unique RYR2 missense variants** among 622,575 total heterozygotes/5,181 unique variants pooled from literature and gnomAD, underscoring the scale of variant heterogeneity (medRxiv 2025.03.20.25324327).
- Population frequency: pathogenic RYR2 CPVT variants are individually very rare in gnomAD (example cited frequency ~3/249,018 chromosomes, ~0.0012%), consistent with a highly penetrant Mendelian disease-gene model, though ACMG reclassification efforts have found meaningful false-positive rates — one systematic re-review of 326 RYR2 missense variants reclassified **55 (16.9%)** of previously disease-associated variants as benign/likely benign using 2015 ACMG/AMP criteria.
- **Functional consequence:** The dominant mechanism is **gain-of-function** — mutant RyR2 channels show increased open probability and heightened sensitivity to luminal/cytosolic Ca²⁺ activation, lowering the threshold for store-overload-induced Ca²⁺ release (SOICR) and producing diastolic SR Ca²⁺ leak. Rare **loss-of-function RYR2 variants** have also been described, producing a distinct phenotype of exertional syncope/ventricular fibrillation without inducible bidirectional VT on stress testing (Circ Arrhythm Electrophysiol, PMID for "Human RyR2 Loss-of-Function Mutations," CIRCEP.121.010013).
- **Germline, not somatic:** CPVT is a germline Mendelian channelopathy; there is no COSMIC/somatic association.
- **Modifier genes:** No robustly established modifier genes beyond the disease genes themselves; CaMKII-mediated phosphorylation status of RyR2 is a key post-translational/regulatory modifier of arrhythmic risk (biorxiv 2025.09.15.676430).

**Recessive/other subtype genes:**
- **CASQ2** (HGNC:1512; calsequestrin-2): loss-of-function, reduced Ca²⁺-buffering capacity and destabilized RyR2 macromolecular complex; **100% penetrant when biallelic**; compound heterozygous CASQ2 variants reported with variable long-term course (PMID:29178653).
- **TRDN** (HGNC:12261; triadin): recessive, reduces CASQ2 levels and impairs coupled Ca²⁺ release; may present with mild skeletal myopathy and T-wave inversions/QT prolongation (atypical CPVT).
- **CALM1/2/3** (calmodulin, HGNC:1442/1848/1849): identical protein product from 3 genes; reduced Ca²⁺-binding affinity impairs regulatory interactions with both CaV1.2 (→ LQTS phenotype) and RyR2 (→ CPVT-like phenotype). CALM-variant carriers present with LQTS (49%), CPVT (28%), overlap LQTS/CPVT (4%), or idiopathic VF/SUD in the remainder (Tandfonline 2023 review).
- **TECRL** (trans-2,3-enoyl-CoA reductase-like): recessive, elevated diastolic Ca²⁺ and impaired mitochondrial function, combined CPVT+QT-prolongation phenotype (CPVT3, OMIM #614021).

**Epigenetic information:** No disease-defining epigenetic mechanism has been established for CPVT; the disorder is a classical monogenic ion-handling channelopathy.

**Chromosomal abnormalities:** Not applicable — CPVT is caused by point/small indel variants, not large structural/chromosomal rearrangements.

---

## 5. Environmental Information

- **Environmental/toxic factors:** No toxin, pollutant, or occupational exposure is implicated as causal; digitalis/digoxin is the principal pharmacologic environmental risk modifier (arrhythmia-promoting via DAD mechanism) and is explicitly listed as an agent to avoid.
- **Lifestyle factors:** Competitive/strenuous exercise and intense emotional stress are the dominant modifiable triggers — activity restriction is a cornerstone of management, not merely correlative.
- **Infectious agents:** None established as causal; some cohorts note fever as an occasional non-adrenergic trigger context, but this is not a primary infectious mechanism.

---

## 6. Mechanism / Pathophysiology

**Causal chain (RYR2 gain-of-function, CPVT1):**

1. **Trigger:** Sympathetic/adrenergic activation (exercise, emotion) → PKA and CaMKII phosphorylation of RyR2 and associated Ca²⁺-handling machinery.
2. **Molecular lesion:** Gain-of-function RYR2 missense variant destabilizes the closed-state conformation of the channel (disrupted N-terminal/central-domain interdomain interactions), lowering the SR luminal Ca²⁺ threshold required for spontaneous store-overload-induced Ca²⁺ release (SOICR) (PMC10311407 — "RYR2-ryanodinopathies: from calcium overload to calcium deficiency," EP Europace 2023).
3. **Cellular consequence:** Diastolic SR Ca²⁺ leak generates spontaneous, propagating intracellular Ca²⁺ waves in cardiomyocytes.
4. **Electrophysiological consequence:** Leaked cytosolic Ca²⁺ is extruded via the electrogenic Na⁺/Ca²⁺ exchanger (NCX, 3 Na⁺ in : 1 Ca²⁺ out), generating a net inward depolarizing current that manifests as a **delayed afterdepolarization (DAD)**.
5. **Arrhythmia trigger:** When DAD amplitude reaches action-potential threshold, it triggers an ectopic beat; when this occurs from distinct/alternating ventricular foci (often Purkinje-adjacent) under ongoing adrenergic drive, the result is the classic **bidirectional or polymorphic ventricular tachycardia**, which can degenerate into ventricular fibrillation and sudden cardiac death (PMC6928245, PMC2704947).
6. A recent 2025 study specifically demonstrates that subthreshold DADs can still **disrupt ventricular activation patterns** even without reaching full AP threshold, broadening the arrhythmogenic mechanism beyond simple triggered-beat generation (PMC12221671, RyR2-R420Q model).

**Cell types involved:** Ventricular and Purkinje-fiber cardiomyocytes (primary); a growing body of evidence also implicates **hippocampal/neocortical neurons**, since RyR2 is the dominant RyR isoform in brain and its dysregulation is mechanistically linked to a neurodevelopmental/neurocognitive phenotype in a subset of RYR2-CPVT patients (Nature Communications Biology PMC/s42003-022-03124-2; Circ Arrhythm Electrophysiol 2024 CIRCEP.124.013437 reporting ~8% ID prevalence in 421 CPVT1 patients; medRxiv 2025.07.26.25332119 linking RyR2 calcium leak in patient-derived neurons to autism spectrum features). This has prompted a proposed reframing of CPVT as a "neurocardiac" condition in recent literature (biorxiv 2025.01.27.635037).

**Suggested GO terms:**
- GO:0014808 (release of sequestered calcium ion into cytosol by sarcoplasmic reticulum)
- GO:0086005 (ventricular cardiac muscle cell action potential)
- GO:0086027 (SR-sarcolemma junction organization/ calcium release channel activity)
- GO:0005219 (ryanodine-sensitive calcium-release channel activity)
- GO:0002026 (regulation of the force of heart contraction)

**Suggested CL terms:**
- CL:0002131 (cardiac ventricle myocyte)
- CL:0002355 (cardiac Purkinje myocyte)
- CL:0000540 (neuron) — for the emerging neurocardiac arm

**Protein dysfunction:** Gain-of-function conformational destabilization (not aggregation/misfolding in the classic proteotoxic sense) — mutant RyR2 favors a "leaky," hyperactive closed-to-open transition, well characterized by cryo-EM structural studies of specific CPVT mutants (e.g., R2474S) showing altered channel-gate conformations.

**Metabolic changes:** RyR2 is also expressed in pancreatic beta cells; altered glucose metabolism has been reported in some RYR2 carriers (GeneReviews NBK1289), an emerging but non-cardiac metabolic association.

**Biochemical abnormality:** The core lesion is an ion-channel (Ca²⁺ release channel) gating defect — a "channelopathy" in the strict sense, not an enzyme deficiency.

**Advanced/omics findings:** iPSC-cardiomyocyte disease modeling is the dominant functional-genomics platform for RYR2-CPVT (used extensively for drug screening — e.g., EL20 RyR2 inhibitor, PMC8366453). Structural cryo-EM reconstructions of mutant RyR2 channels (e.g., R2474S) directly visualize altered channel-gate conformations relative to wild-type.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Heart — specifically ventricular myocardium and the cardiac conduction/Purkinje system; the heart is structurally normal by imaging (echocardiography/MRI), the defect being purely electrical.
- **Secondary organ involvement:** Brain (neurodevelopmental/cognitive phenotype in a subset of RYR2 patients); pancreas (beta-cell RyR2 expression, glucose-handling changes in some carriers); skeletal muscle (mild myopathy reported in TRDN-related CPVT).
- **Body systems:** Cardiovascular (primary); nervous system (emerging secondary/neurocardiac axis); endocrine/metabolic (minor, glucose handling).
- **Tissue/cell level:** Cardiac muscle tissue — ventricular cardiomyocytes and Purkinje fibers are the principal arrhythmogenic substrate (CL:0002131, CL:0002355); hippocampal and neocortical neurons for the neurologic phenotype.
- **Subcellular level:** Sarcoplasmic reticulum (GO:0005791/0033017 — SR membrane and junctional SR), specifically the RyR2 Ca²⁺-release channel complex at the SR-sarcolemma dyad/triad junction, and its regulatory partners FKBP12.6 (calstabin2), calsequestrin-2, triadin, and junctin.
- **UBERON terms:** UBERON:0002082 (cardiac ventricle); UBERON:0002080 (heart); UBERON:0001884 (Purkinje fiber); UBERON:0002421 (hippocampal formation).
- **Lateralization:** Not applicable — disease is a diffuse/bilateral electrical/molecular process affecting the whole ventricular myocardium, not a focal/lateralized lesion. (LCSD, notably, is performed unilaterally — usually left-sided — as a therapeutic intervention rather than reflecting disease lateralization.)

---

## 8. Temporal Development

- **Onset:** Typically pediatric/adolescent — mean age 7–12 years; documented range from infancy (occult RYR2 variants implicated in some SIDS cases) through age 40. Onset pattern is typically **acute/paroxysmal** (a syncopal or cardiac-arrest event), rather than insidious.
- **Progression:** Disease "stage" is not formally classified (unlike cancer staging), but clinical severity is tracked longitudinally via serial exercise stress testing and Holter monitoring; a 2025 medRxiv study specifically examined **long-term serial exercise stress testing in CPVT patients on beta-blocker + flecainide therapy**, showing the disease course and arrhythmia burden can be tracked and is modifiable by combination pharmacotherapy over years of follow-up.
- **Progression rate/course:** Without treatment, risk of life-threatening events accumulates with continued exposure to triggers (cumulative event rates reported as high as ~80% by age 40 in some untreated series); with beta-blocker ± flecainide therapy, the disease course is typically **stabilized**, though breakthrough events can still occur, particularly around puberty (dose titration to weight is emphasized) and with poor treatment adherence.
- **Duration:** Chronic, lifelong condition — there is no spontaneous resolution; the risk persists across the lifespan though relative event rates are highest in childhood/adolescence and young adulthood.
- **Remission patterns:** No spontaneous remission is described; symptomatic "remission" (arrhythmia suppression) is treatment-induced via beta-blockade, flecainide, LCSD, or combinations — assessed by serial provocative stress testing.
- **Critical periods:** Puberty is repeatedly flagged in the literature as a critical vulnerability window requiring more frequent surveillance and dose re-titration owing to rapid weight/body-composition change affecting drug dosing.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Estimated at approximately **1 in 10,000** individuals (frequently cited range 1:10,000–1:15,000), though true prevalence is likely underestimated because patients have normal resting ECG and normal cardiac imaging, making ascertainment difficult except after a sentinel arrhythmic event or targeted family cascade screening.
- **Incidence data:** No robust population-based incidence rate is established given underdiagnosis; the disease is best characterized via registry-based prevalence and familial-cascade detection.

**Inheritance patterns:**
- **Autosomal dominant:** RYR2, CALM1, CALM2, CALM3, KCNJ2 — each affected parent transmits with 50% risk per offspring.
- **Autosomal recessive:** CASQ2, TRDN, TECRL — 25% recurrence risk per sibling, 50% carrier risk.
- De novo RYR2 variants explain an estimated 30–40% of RYR2-CPVT cases lacking family history.

**Penetrance:**
- **RYR2:** Mean penetrance estimated at ~83% in some series, but with wide variant-to-variant heterogeneity; approximately **50% of mutation carriers may remain entirely asymptomatic**, reflecting substantial incomplete/variable penetrance — a 2025 Bayesian structural-modeling paper specifically develops continuous, variant-level penetrance estimates for RYR2-CPVT missense variants rather than a single point estimate (PMC13108506/medRxiv 2025.03.20.25324327).
- **CASQ2 (biallelic):** ~100% penetrant.
- Heterozygous CASQ2 carriers may show a mild/subclinical phenotype.
- Insufficient case numbers exist to derive robust penetrance estimates for CALM, KCNJ2, TRDN, and TECRL variants (GeneReviews NBK1289).

**Expressivity:** Variable — even within families carrying the identical RYR2 variant, phenotype severity ranges from asymptomatic to sudden death, and there is documented sex-based expressivity divergence (see below).

**Genetic anticipation:** Not a recognized feature of CPVT (not a repeat-expansion disorder).

**Founder effects:** The best-documented founder mutation is the Finnish **RyR2-P2328S** variant, traced by genealogical analysis to a common ancestor couple in central Finland in the 17th–18th century (PMC7735638). Other population-specific variant clusters have been reported (e.g., in Kazakh and Chinese cohorts) though without formal founder-effect confirmation in the sources reviewed.

**Consanguinity:** Relevant specifically for the recessive subtypes (CASQ2, TRDN, TECRL), where consanguineous unions increase biallelic-variant risk, consistent with general autosomal recessive disease principles.

**Carrier frequency:** Population carrier frequency of any single pathogenic RYR2 variant is very low (individual variant frequencies on the order of 0.001–0.01% in gnomAD), consistent with high aggregate genetic heterogeneity (>460 unique disease-associated missense variants described) rather than one or a few common alleles.

**Population demographics:**
- No strong ethnic-specific prevalence enrichment is described beyond the Finnish founder cluster; the disease has been reported across European, East Asian (Chinese systematic review, PMC9330865), Central Asian (Kazakh cohort), and other populations.
- **Sex ratio:** Not markedly skewed in genetic prevalence, but clinical expressivity is sex-dimorphic — males show earlier symptom onset and higher relative risk of syncope/cardiac events (RR ~4.2 in some analyses), partly attributable to CYP2D6-mediated sex differences in beta-blocker (propranolol) pharmacokinetics (testosterone-driven CYP2D6 upregulation → faster clearance/lower drug exposure in males).
- **Age distribution:** Predominantly diagnosed in childhood/adolescence/young adulthood; a minority present later (up to age 40).

---

## 10. Diagnostics

**Clinical diagnostic criteria** (GeneReviews NBK1289; consensus HRS/EHRA/APHRS and ESC criteria): CPVT is diagnosed when there is (a) a structurally normal heart on imaging, (b) a normal resting ECG, and (c) exercise- or emotion-induced bidirectional or polymorphic VT; OR when a heterozygous pathogenic variant is found in RYR2/CALM1/CALM2/CALM3/CASQ2/KCNJ2, or biallelic variants in CASQ2/TECRL/TRDN.

**Exercise stress testing:** The primary provocative test — arrhythmia (PVCs progressing to bigeminy, couplets, then sustained bidirectional/polymorphic VT) typically emerges at a heart rate threshold of **90–120 bpm**, with progressively increasing complexity as workload increases; positive in up to ~80% of symptomatic patients.

**Epinephrine (catecholamine) challenge:** Used when exercise testing is not feasible (young children) or symptoms are emotion-triggered. Standard protocol: incremental epinephrine infusion starting at 0.05–0.1 mcg/kg/min, increasing by 0.05 mcg/kg/min increments to a maximum of 0.20 mcg/kg/min; test is positive with induction of sustained/non-sustained polymorphic VT (>10 PVCs/min) or new T-wave alternans. Compared to exercise testing, epinephrine challenge has **low sensitivity (~28%) but high specificity (~98%)**.

**Holter monitoring:** Alternative/complementary method, particularly for very young patients or emotion-triggered (non-exertional) presentations.

**Genetic testing:** Multigene panel (RYR2, CASQ2, CALM1-3, TRDN, TECRL, KCNJ2) or exome/genome sequencing is recommended as first-tier molecular testing; sequence-analysis detection sensitivity approaches 99–100% for most genes, though ~25% of clinically diagnosed patients remain molecularly unsolved. ACMG/AMP-based reclassification efforts have found meaningful rates of prior misclassification (16.9% of previously "disease-associated" RYR2 missense variants reclassified benign in one study), underscoring the importance of rigorous variant curation (ClinVar cross-checking, structural/functional evidence, penetrance modeling).

**Imaging:** Echocardiography and cardiac MRI are used primarily to exclude structural heart disease (e.g., ARVC, cardiomyopathy) rather than to positively diagnose CPVT; performed at baseline and roughly every 2 years during surveillance.

**Differential diagnosis:**
- **Short-coupled Torsade de Pointes (SC-TdP):** polymorphic VT not clearly adrenergically triggered and lacking the bidirectional pattern; no established effective CPVT-type therapy.
- **Long QT syndrome type 1 (LQT1):** exercise-triggered syncope overlaps clinically, but LQT1 shows a prolonged QT interval and does not reproduce inducible bidirectional VT on graded exercise testing (unless overlap calmodulinopathy).
- **Arrhythmogenic right ventricular cardiomyopathy (ARVC):** shows structural myocardial abnormality on imaging, distinguishing it from CPVT's structurally normal heart.
- **Idiopathic ventricular fibrillation:** relevant differential for RYR2 loss-of-function variant carriers, who may present with VF without the classic inducible bidirectional VT pattern.

**Screening:** Cascade family screening (clinical + genetic) is standard once a proband is identified, given up to 50% first-degree-relative transmission risk (dominant genes) and family history present in ~30% of probands.

---

## 11. Outcome/Prognosis

- **Untreated mortality:** Historically cited untreated mortality figures range widely across sources — approximately **30–50% by age 30–35**, with some series reporting cardiac event rates as high as **80% by age 40** if untreated; approximately 30% experience cardiac arrest and up to 80% experience syncope if untreated (GeneReviews NBK1289).
- **With treatment:** Beta-blocker therapy (particularly nadolol) substantially reduces mortality and arrhythmic events; combination therapy (beta-blocker + flecainide ± LCSD/ICD) further reduces breakthrough events, as demonstrated in long-term serial-stress-testing follow-up cohorts (medRxiv 2025.04.08.25325493).
- **Morbidity:** Beyond mortality, morbidity includes recurrent syncope, ICD-related complications (inappropriate/ineffective shocks, which can paradoxically worsen VT storm via further adrenergic surge), and — in the RYR2-neurodevelopmental subgroup — intellectual disability and behavioral impact.
- **Prognostic factors:** Genotype (RYR2 vs. CASQ2 vs. calmodulinopathy), specific variant/domain location and structural severity (informing the new Bayesian penetrance models), sex (male sex worse), age at first event, and treatment adherence/response on serial exercise testing are the principal prognostic determinants identified in the literature. No single validated prognostic biomarker (analogous to a cancer biomarker) exists; risk stratification instead relies on genotype, clinical/family history, and provocative testing response.
- **ICD-specific risk:** ICDs are a double-edged prognostic tool in CPVT — while indicated in drug-refractory, highly symptomatic disease, inappropriate or even appropriate shocks can trigger further catecholamine release, precipitating an electrical storm; this is a well-recognized complication specific to this disease's adrenergic-arrhythmia mechanism.

---

## 12. Treatment

**Pharmacotherapy (first-line):**
- **Beta-blockers** — nonselective agents preferred over cardioselective ones. **Nadolol** (1–2.5 mg/kg/day) is considered possibly superior; **propranolol** (2–4 mg/kg/day, divided) is a common alternative. NCIT: Pharmacotherapy (NCIT:C15986); therapeutic agent nadolol/propranolol (beta-adrenergic antagonists).
- **Flecainide** (Class IC antiarrhythmic; 100–300 mg/day in adults) — added when beta-blockade alone is insufficient; reported effective in suppressing exercise-induced ventricular arrhythmia in ~75% of patients, with effect appearing largely independent of underlying genotype. NCIT: Chemotherapy is not applicable; use NCIT:C15986 Pharmacotherapy with therapeutic_agent flecainide (CHEBI).

**Advanced/emerging therapeutics:**
- **RyR2-targeted small molecules ("Rycals" and related stabilizers):** JTV519 (K201) and S107 stabilize FKBP12.6 (calstabin2) binding to RyR2, reducing diastolic Ca²⁺ leak; dantrolene (a hydantoin derivative, historically a malignant-hyperthermia drug) has been repurposed and shown in iPSC-cardiomyocyte studies to reduce ectopic beats in a **mutation/domain-dependent manner** — more effective for N-terminal and central-domain RyR2 mutations than transmembrane-domain mutations, consistent with its proposed mechanism of stabilizing the N-terminal/central-domain interaction. Newer tetracaine-derivative RyR2 inhibitors (EL9, EL20) have shown efficacy in patient-derived iPSC-cardiomyocyte models (PMC8366453). A novel RyR2-selective stabilizer preventing stress-induced arrhythmia was reported in a 2024/2025 preprint (biorxiv 2024.11.26.625386).
- **Gene therapy:** Solid Biosciences' AAV-based gene therapy candidate **SGT-501** for CPVT began its first-in-human Phase 1b study in **May 2024**, an open-label trial enrolling approximately 43 patients aged 4–11 years — the first gene-therapy clinical trial specifically for CPVT (CGTlive, 2024). NCIT: Gene Therapy (NCIT:C15238).

**Surgical/interventional:**
- **Left cardiac sympathetic denervation (LCSD):** Recommended as an adjunct in young patients not fully protected by beta-blockade, or when patients fail combination beta-blocker + flecainide therapy; also used to reduce ICD shock burden. Side effects include Horner-type ptosis and facial/arm anhidrosis. NCIT: Surgical Procedure (NCIT:C15329) or a sympathectomy-specific NCIT code if available.
- **Implantable cardioverter-defibrillator (ICD):** Indicated in drug-refractory, highly symptomatic disease; use requires caution given the risk that shocks (appropriate or inappropriate) can provoke further catecholamine release and precipitate electrical storm, a distinctive management challenge in this specific arrhythmia syndrome. NCIT: Device (implantable cardioverter-defibrillator implantation).

**Supportive/behavioral:**
- Absolute avoidance of competitive sports and strenuous exercise; activity restriction counseling. NCIT:C181743 (Behavioral Counseling) / therapeutic_modality: BEHAVIORAL.
- Avoidance of digitalis/digoxin (arrhythmia-promoting).
- Atropine has been studied experimentally in CPVT (registered trial NCT02927223) though it is not standard therapy and its precise role remains investigational.

**Genetic counseling:** Family cascade testing and counseling given 50% (dominant) or 25% (recessive) transmission risk; recommended given the potential for sudden death as first manifestation in unrecognized carriers.

**Treatment algorithm (stepwise):** (1) Beta-blocker (nadolol preferred) for all clinically affected individuals and asymptomatic pathogenic-variant carriers → (2) add flecainide if breakthrough arrhythmia on stress testing/symptoms → (3) LCSD and/or ICD if still refractory, with LCSD often favored first given the risk of ICD-triggered arrhythmic storms → (4) gene therapy (SGT-501) and novel RyR2 stabilizers under active clinical investigation as of 2024–2025.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (no modifiable non-genetic cause to prevent onset), but pre-symptomatic beta-blocker initiation in genotype-positive, phenotype-negative relatives identified through cascade screening functions as a primary preventive strategy against the first (potentially fatal) event.
- **Secondary prevention:** Family cascade genetic screening after proband identification; periodic exercise stress testing surveillance (every 6–12 months, more frequent during puberty) to detect breakthrough arrhythmia before a clinical event.
- **Tertiary prevention:** ICD implantation and LCSD in patients with established, drug-refractory disease to prevent recurrent/fatal events; combination pharmacotherapy adjustment based on serial stress-test results.
- **Screening:** No population-based newborn screening exists (CPVT is not detectable on a resting ECG); screening is instead cascade/family-based following proband diagnosis, using multigene panel testing.
- **Genetic counseling:** Central to prevention — informing reproductive decisions and triggering early beta-blocker initiation in asymptomatic carriers.
- **Behavioral/public health intervention:** Activity restriction guidance (avoidance of competitive sports) issued through cardiology/sports-cardiology clinical guidelines is the principal behavioral prevention lever.
- **Prophylaxis:** Prophylactic beta-blockade in all genotype-positive individuals regardless of symptom status is explicitly recommended in GeneReviews given the risk of sudden death as the first manifestation.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** RYR2 orthologs are highly conserved across vertebrates (NCBI Taxon 9606 human; conserved in Mus musculus NCBITaxon:10090, Danio rerio NCBITaxon:7955, Sus scrofa NCBITaxon:9823, Ovis aries NCBITaxon:9940).
- **Gene orthologs:** Mouse Ryr2 (NCBI Gene: 20191); highly conserved functional domains across species enable cross-species modeling.
- **Naturally occurring disease in other species:** No well-established naturally occurring CPVT/RYR2 disease model was identified in dogs via OMIA in this search (the related but mechanistically distinct Boxer-dog arrhythmogenic right ventricular cardiomyopathy is caused by a **STRN** variant, not RYR2, and was historically — and now understood to be incorrectly — attributed in part to calstabin2/FKBP12.6 deficiency in earlier literature). No confirmed naturally occurring veterinary CPVT phenotype driven by spontaneous RYR2 variants was found in the searched sources.
- **Comparative biology:** The RyR2-mediated Ca²⁺-leak/DAD arrhythmia mechanism is evolutionarily conserved and reproducible across engineered animal models (mouse, zebrafish, pig, sheep), supporting strong translational validity of the induced (non-natural) models described below.
- **Zoonotic potential:** Not applicable — CPVT is a non-infectious, purely genetic disease with no transmission risk.

---

## 15. Model Organisms

**Mouse models (most extensively characterized):**
- **RyR2-R4496C knock-in mouse** (corresponding to human R4497C): generated by homologous recombination in a fully penetrant human CPVT family variant; considered "the first RyR2 transgenic mouse model that recapitulates the main aspects of human CPVT" — mice show stress/catecholamine-induced ventricular arrhythmia and sudden death, with cellular studies showing enhanced SR Ca²⁺ release and DAD generation, and structural destabilization favoring a closed-to-open channel transition (leaky channel).
- **RyR2-P2328S knock-in mouse:** models the Finnish founder mutation; shown to downregulate Nav1.5, producing an additional arrhythmic substrate in ventricular tissue (PMC4792352) — illustrating a secondary ion-channel remodeling mechanism beyond the primary RyR2 Ca²⁺-leak defect.
- **RyR2+/− (haploinsufficient) mouse:** exhibits arrhythmogenic phenotypes resembling CPVT, used to model loss-of-function-associated arrhythmia.
- Additional knock-in efforts (e.g., attempted Q3924E Ca²⁺-binding-site mutant mice, PMC11674951) illustrate ongoing efforts to model specific structural domains, though not all attempted knock-ins produce viable/faithful models.
- **Exon-3-deletion RyR2 mouse:** models a specific human CPVT-associated exon-skipping/deletion variant (PMC3990712).

**Zebrafish models:** Used to study CALM-mutation-associated CPVT via overexpression approaches, successfully demonstrating cardiac arrhythmia phenotypes; zebrafish offer high-throughput in vivo screening advantages for CPVT drug discovery given transparent embryos and amenability to genetic manipulation.

**Large animal models:** Pigs and sheep are increasingly used as large-animal ventricular-arrhythmia models given closer anatomical/physiological resemblance to the human heart than rodents (more ethically/economically favorable than dog models); RYR2-specific engineered large-animal CPVT models are less mature than the mouse literature but are an active area per recent reviews (Biology 2026, 15040343).

**Cellular/iPSC models:** Patient-derived induced pluripotent stem cell-cardiomyocytes (iPSC-CMs) are now the dominant translational platform for RYR2/CASQ2-CPVT — used to validate calcium-handling defects, screen RyR2-stabilizing compounds (dantrolene, EL20, S107/JTV519 analogs), and, in a 2025 study, to link RyR2 calcium leak in patient-derived **neurons** to autism-spectrum features, directly bridging the cardiac and emerging neurodevelopmental phenotype (medRxiv 2025.07.26.25332119).

**Model limitations:** Mouse cardiac electrophysiology differs substantially from human (heart rate, ion channel repertoire), so while Ca²⁺-leak/DAD mechanisms are well recapitulated, absolute arrhythmia thresholds and some pharmacologic responses may not translate directly; iPSC-CM models lack full three-dimensional tissue architecture and autonomic innervation context, limiting their ability to model the whole-organism adrenergic trigger.

**Applications:** These models have been essential for (1) establishing the core Ca²⁺-leak/DAD mechanistic paradigm, (2) genotype-specific drug screening (e.g., domain-dependent dantrolene efficacy), (3) preclinical validation of RyR2-stabilizer and gene-therapy (AAV-CASQ2/RYR2) approaches prior to human trials such as SGT-501.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested term |
|---|---|
| Disease | MONDO:0011001 (CPVT1); OMIM:604772; ORPHA:3286 |
| Gene | HGNC:10484 (RYR2); HGNC:1512 (CASQ2); HGNC:12261 (TRDN); HGNC:1442/1848/1849 (CALM1/2/3) |
| Phenotype | HP:0004756 (bidirectional VT); HP:0004758 (paroxysmal VT); HP:0001279 (syncope); HP:0001645 (sudden cardiac death); HP:0001249 (intellectual disability) |
| GO (process) | GO:0014808 (SR calcium release); GO:0086005 (ventricular cardiomyocyte action potential); GO:0005219 (ryanodine-sensitive Ca²⁺-release channel activity) |
| Cell type | CL:0002131 (cardiac ventricular myocyte); CL:0002355 (Purkinje myocyte) |
| Anatomy | UBERON:0002082 (cardiac ventricle); UBERON:0001884 (Purkinje fiber) |
| Chemical | CHEBI (nadolol, propranolol, flecainide, dantrolene) |
| Treatment | NCIT:C15986 (Pharmacotherapy); NCIT:C15329 (Surgical Procedure — LCSD); NCIT:C15238 (Gene Therapy) |

---

## Sources

- [GeneReviews: Catecholaminergic Polymorphic Ventricular Tachycardia](https://www.ncbi.nlm.nih.gov/books/NBK1289/)
- [Clinical and Molecular Characterization of Patients With CPVT (Priori et al., Circulation 2002)](https://www.ahajournals.org/doi/10.1161/01.cir.0000020013.73106.d8)
- [RYR2 Variants in CPVT Patients: Insights From Protein Structure and Clinical Data (Circ Arrhythm Electrophysiol 2025)](https://pubmed.ncbi.nlm.nih.gov/40875405/)
- [RYR2-ryanodinopathies: from calcium overload to calcium deficiency (EP Europace 2023)](https://academic.oup.com/europace/article/25/6/euad156/7210777)
- [Disruption of ventricular activation by subthreshold DADs in RyR2-R420Q CPVT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12221671/)
- [Therapeutic approach for CPVT patients (EP Europace 2012)](https://academic.oup.com/europace/article/14/2/175/448785)
- [Left cardiac sympathetic denervation for CPVT and LQTS](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536998/)
- [Catecholaminergic Polymorphic Ventricular Tachycardia: Clinical Characteristics, Diagnostic Evaluation and Therapeutic Strategies (J Clin Med 2024)](https://www.mdpi.com/2077-0383/13/6/1781)
- [CPVT: Advancing From Molecular Insights to Preclinical Models (JAHA 2024)](https://www.ahajournals.org/doi/full/10.1161/JAHA.124.038308)
- [PACES CPVT Registry: multiple genetic variants](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6221297/)
- [International Multicenter Evaluation of CASQ2-CPVT (Circulation 2021)](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.045723)
- [Long-term Serial Exercise Stress Testing in CPVT (medRxiv 2025)](https://www.medrxiv.org/content/10.1101/2025.04.08.25325493v1.full.pdf)
- [Structural Evaluation of RYR2-CPVT Missense Variants and Bayesian Penetrance Estimates (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13108506/)
- [Classification and correlation of RYR2 missense variants (J Hum Genet)](https://www.nature.com/articles/s10038-020-0738-6.pdf)
- [Efficacy of RyR2 inhibitor EL20 in iPSC-CMs from a CPVT patient](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8366453/)
- [Solid Biosciences' CPVT Gene Therapy SGT-501 Phase 1b (CGTlive, 2024)](https://www.cgtlive.com/view/solid-biosciences-cpvt-gene-therapy-sgt-501-cleared-phase-1b-trial)
- [Genealogy and clinical course of CPVT caused by RyR2 P2328S (Finnish founder mutation)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7735638/)
- [The RyR2-P2328S mutation downregulates Nav1.5](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792352/)
- [Calmodulin Mutations in Human Disease (2023 review)](https://www.tandfonline.com/doi/full/10.1080/19336950.2023.2165278)
- [Intellectual and Neurodevelopmental Delays in Pediatric CPVT (Circ Arrhythm Electrophysiol 2024)](https://www.ahajournals.org/doi/10.1161/CIRCEP.124.013437)
- [Linking the heart and the brain: Neurodevelopmental disorders in CPVT (Mayo Clinic)](https://pubmed.ncbi.nlm.nih.gov/30170228/)
- [Patient-derived cells: mutated RyR2 calcium leak underlies ASD and inherited arrhythmias (medRxiv 2025)](https://www.medrxiv.org/content/10.1101/2025.07.26.25332119.full.pdf)
- [OMIM #604772 — CPVT1](https://omim.org/entry/604772)
- [OMIM #611938 — CPVT2 (CASQ2)](https://omim.org/entry/611938)
- [Human RyR2 Loss-of-Function Mutations (Circ Arrhythm Electrophysiol)](https://www.ahajournals.org/doi/10.1161/CIRCEP.121.010013)
- [Selected Large-Animal Models of Ventricular Arrhythmias (Biology, 2026)](https://doi.org/10.3390/biology15040343)
- [Arrhythmogenic right ventricular cardiomyopathy in Boxer dogs and calstabin2 deficiency](https://www.sciencedirect.com/science/article/abs/pii/S176027340800012X)
- [CaMKII Phosphorylation of RYR2 is Essential for Arrhythmia in CPVT (bioRxiv 2025)](https://www.biorxiv.org/content/10.1101/2025.09.15.676430.full.pdf)