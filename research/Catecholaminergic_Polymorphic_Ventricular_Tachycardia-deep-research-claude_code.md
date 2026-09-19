---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-07-30T16:27:04.308352'
end_time: '2026-07-30T16:32:25.762987'
duration_seconds: 321.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Catecholaminergic Polymorphic Ventricular Tachycardia
  mondo_id: MONDO:0017990
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
  - claude-opus-4-8[1m]
  web_search_requests: 6
  num_turns: 8
  total_cost_usd: 2.3803095
  session_id: 5c25f996-51e5-4e0c-bd1c-38bf1585daae
  stop_reason: end_turn
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Catecholaminergic Polymorphic Ventricular Tachycardia
- **MONDO ID:** MONDO:0017990 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Catecholaminergic Polymorphic Ventricular Tachycardia** covering all of the
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

I have enough verified material to write the comprehensive report. 

> **Note (branch):** You are on branch **augment-cpvt**. **Skills used:** none invoked — this is a direct research/report-writing task; the dismech curation skills (`initiate-new-disorder-creation`, `dismech-terms`, `dismech-references`, `curate`) would be the right tools when this report is actually loaded into a KB YAML entry with validated snippets.

---

# Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT): Comprehensive Research Report

**Target for:** dismech knowledge-base entry · **MONDO:0017990** · Category: Genetic (inherited cardiac ion-channel/calcium-handling disorder / "cardiac channelopathy")

A note on evidence typing throughout (per dismech `evidence_source` conventions): human cohort/registry/case data = HUMAN_CLINICAL; knock-in mouse / large-animal work = MODEL_ORGANISM; hiPSC-cardiomyocyte, lipid-bilayer, and myocyte studies = IN_VITRO; computational myocyte models = COMPUTATIONAL.

---

## 1. Disease Information

**Overview.** CPVT is a rare, potentially lethal **inherited arrhythmia syndrome (cardiac "channelopathy" of intracellular calcium handling)** characterized by **adrenergically triggered bidirectional and polymorphic ventricular tachycardia (VT)** occurring in a **structurally normal heart with a normal resting ECG**. Arrhythmia is provoked by physical exertion or acute emotion (catecholamine surge) and manifests clinically as exercise/stress-induced syncope, seizures (misdiagnosed as epilepsy), or aborted/actual sudden cardiac death (SCD), typically in children and adolescents. The pathognomonic rhythm is **bidirectional VT** — a beat-to-beat ~180° alternation of the QRS axis — although polymorphic VT and catecholamine-induced supraventricular arrhythmias also occur.

The syndrome was first defined clinically by **Coumel (1978)** and characterized in a landmark case series by **Leenhardt et al., 1995** (*Circulation* 91:1512–1519, **PMID:7867192**), which established the exercise-reproducible bidirectional VT phenotype, childhood onset, and high lethality.

**Key identifiers.**
- **MONDO:** MONDO:0017990 (catecholaminergic polymorphic ventricular tachycardia)
- **OMIM (locus/subtype series):** CPVT1 **#604772** (RYR2); CPVT2 **#611938** (CASQ2); CPVT3 **#614021** (TECRL locus / older mapping); CPVT4 **#614916** (CALM1); CPVT5 **#615441** (TRDN). Gene entries: RYR2 *180902*, CASQ2 *114251*.
- **Orphanet:** **ORPHA:3286** (Catecholaminergic polymorphic ventricular tachycardia).
- **ICD-10:** **I47.2** (Ventricular tachycardia — no CPVT-specific code). **ICD-11:** BC71.0 / arrhythmia block (no dedicated CPVT stem; coded under ventricular tachyarrhythmia + genetic modifier).
- **MeSH:** indexed under *Tachycardia, Ventricular* (D017180); CPVT exists as a MeSH Supplementary Concept Record ("Ventricular Tachycardia, Catecholaminergic Polymorphic").

**Common synonyms / alternative names:** Catecholaminergic polymorphic ventricular tachycardia; familial polymorphic ventricular tachycardia (FPVT); bidirectional tachycardia induced by catecholamines; catecholamine-induced polymorphic ventricular tachycardia; stress-induced polymorphic ventricular tachycardia; CPVT.

**Data derivation.** Information is predominantly from **aggregated disease-level resources** (GeneReviews, OMIM, Orphanet, ClinGen expert-panel curation) and **multicenter registries/cohorts** rather than EHR-derived individual-patient datasets, reflecting the disorder's rarity. Key registries: the international CPVT registries feeding Hayashi et al. 2009, van der Werf et al. 2011, and the pediatric CPVT registry (Roston et al. 2015).

---

## 2. Etiology

**Primary cause — genetic.** CPVT is a **monogenic Mendelian disorder of cardiomyocyte sarcoplasmic-reticulum (SR) calcium handling.** Pathogenic variants dysregulate diastolic SR Ca²⁺ release, so the "trigger" is not the gene alone but **catecholaminergic (β-adrenergic) stimulation acting on a genetically primed calcium-release apparatus.** There is no structural, ischemic, or inflammatory substrate.

**ClinGen-validated causal genes** (Gene–Disease Validity):
- **RYR2** (cardiac ryanodine receptor 2) — **CPVT1, autosomal dominant, gain-of-function**; ~**50–60%** of clinically definite cases.
- **CASQ2** (calsequestrin 2) — **CPVT2, classically autosomal recessive** (dominant/compound-het forms reported); ~**2–5%**.
- **TRDN** (triadin) — autosomal recessive; ~**1–2%**.
- **CALM1, CALM2, CALM3** (calmodulin) — autosomal dominant "calmodulinopathy"; ~**1%**, often severe, early-onset, overlapping with LQTS.
- **TECRL** (trans-2,3-enoyl-CoA reductase-like) — autosomal recessive; CPVT/LQTS overlap phenotype.

**Genotype-negative fraction:** ~30–40% of clinically definite CPVT remains genetically unexplained after testing the known genes (locus/mechanistic heterogeneity; some carry non-coding or copy-number RYR2 variants missed by standard panels).

**Risk factors.**
- *Genetic risk (causal):* Heterozygous RYR2 gain-of-function missense variants clustered in mutational "hotspots" (N-terminal domain, central domain, C-terminal channel/pore domain); biallelic CASQ2/TRDN/TECRL; dominant CALM variants. Family history of exertional syncope or premature/unexplained SCD is a major risk marker.
- *Modifier/susceptibility loci:* variant location within RyR2 domains and specific residues modulate penetrance and severity (see §4).
- *Environmental/physiologic "risk" (triggers, not causes):* **exercise, acute emotional stress, catecholamine administration, fever** in overlap cases, and competitive/high-intensity physical activity are the principal arrhythmia precipitants. Male sex and younger age at first symptom are associated with worse arrhythmic outcome.

**Protective factors.**
- *Pharmacologic (acquired):* **β-adrenergic blockade (especially nadolol), flecainide, and left cardiac sympathetic denervation** are protective by blunting the catecholaminergic trigger / stabilizing RyR2 (see §12). **Exercise restriction** reduces trigger exposure.
- *Genetic protective:* No robust protective germline allele is established; residual RyR2 function and variant position influence a milder phenotype but are better described as reduced severity than protection.

**Gene–environment interaction.** CPVT is a paradigm of GxE: the **genetic lesion is clinically silent at rest and unmasked by adrenergic drive.** β-agonist provocation (exercise/epinephrine) is both the diagnostic maneuver and the disease trigger, and β-blockade neutralizes the environmental arm — a direct, therapeutically exploited gene–environment axis.

---

## 3. Phenotypes

CPVT phenotypes are **arrhythmic and exertion-dependent**; the heart is structurally and (at rest) electrically normal.

| Phenotype | Type | Suggested HPO | Onset / severity / frequency |
|---|---|---|---|
| **Exercise/emotion-induced syncope** | Symptom | **HP:0011675** (Syncope) / HP:0001278 (Orthostatic ... — not apt); use **HP:0001279** (Syncope) | Childhood onset; often first presentation; **up to ~80%** experience ≥1 syncopal spell if untreated |
| **Bidirectional ventricular tachycardia** | Clinical sign / ECG | **HP:0004758** (Bidirectional ventricular tachycardia) | Pathognomonic; provoked by exercise/catecholamine |
| **Polymorphic ventricular tachycardia** | Clinical sign / ECG | **HP:0031677** (Polymorphic ventricular tachycardia) / HP:0006684 | Provoked, episodic |
| **Ventricular fibrillation / cardiac arrest** | Clinical sign | **HP:0001663** (Ventricular fibrillation); **HP:0001695** (Cardiac arrest) | **~30%** have ≥1 cardiac arrest if untreated |
| **Sudden cardiac death** | Outcome | **HP:0001645** (Sudden cardiac death) | Can be first manifestation; mortality up to ~30–50% by age 30–40 untreated |
| **Exercise-induced ventricular premature complexes** | Clinical sign | **HP:0006682** (Premature ventricular contraction) / HP:0025535 | Earliest exercise-test finding; reproducible threshold heart rate |
| **Supraventricular arrhythmias (AF, atrial tachycardia)** | Clinical sign | **HP:0004755** (Paroxysmal atrial fibrillation) / HP:0011702 | Catecholamine-induced; common associated finding |
| **Sinus bradycardia / sinus node dysfunction** | Clinical sign | **HP:0001662** (Bradycardia); HP:0011702 | Reported baseline finding, esp. CASQ2/RYR2 |
| **Seizure-like episodes** (arrhythmic syncope with convulsion) | Symptom | **HP:0001250** (Seizure) | Frequent misdiagnosis as epilepsy |
| **Palpitations / dizziness on exertion** | Symptom | **HP:0025213** (Palpitations); HP:0002321 (Vertigo) | Common prodrome |
| **Normal resting ECG / structurally normal heart** | Baseline feature | (normal echocardiogram; no HP for "normal") | Diagnostic requirement |

**Phenotype characteristics.**
- **Age of onset:** typically **first/second decade**; median age at diagnosis/first symptom ~**8–12 years** (one systematic review: median onset **11 years, IQR 7–14**). A subset presents in adulthood (milder variants).
- **Severity:** **severe** — high risk of cardiac arrest/SCD; among the most malignant of inherited arrhythmia syndromes when untreated.
- **Progression:** **episodic/triggered**, not degenerative — arrhythmia burden tracks with adrenergic exposure and treatment adequacy; a **stepwise progression** from isolated PVCs → bidirectional couplets/bigeminy → non-sustained bidirectional VT → sustained polymorphic VT/VF as workload increases on exercise testing.
- **Frequency among affected:** untreated — **~80%** syncope, **~30%** cardiac arrest; cumulative arrhythmic events remain substantial even on therapy.

**Quality-of-life impact:** exercise restriction, competitive-sport disqualification, ICD-related psychosocial burden and inappropriate shocks, anxiety, and impact on schooling/employment. No CPVT-specific QoL instrument; generic tools (SF-36, PedsQL, ICD-specific measures) apply.

---

## 4. Genetic / Molecular Information

**Causal genes and variant landscape.**

- **RYR2 (hgnc:10484; OMIM 180902; chr1q43).** Encodes the ~5,000-residue cardiac ryanodine receptor, the SR Ca²⁺-release channel. **CPVT-causing variants are heterozygous, dominant, gain-of-function missense** substitutions producing a "leaky" channel. They cluster in **three hotspot domains:** N-terminal (aa ~44–466), central/FKBP-binding (aa ~2246–2534), and the C-terminal transmembrane/channel-forming/luminal domain (aa ~3778–4959). Landmark identification: **Priori et al., 2001, *Circulation* 103:196–200 (PMID:11208676)** and **Laitinen et al., 2001**. Functional consequence: **gain-of-function → lowered threshold for store-overload-induced Ca²⁺ release (SOICR) and diastolic SR Ca²⁺ leak.**
- **CASQ2 (hgnc:1513; OMIM 114251; chr1p13).** Encodes cardiac calsequestrin, the principal SR luminal Ca²⁺-buffer and RyR2 luminal regulator. **Loss-of-function, classically biallelic/recessive.** Founder discovery: **Lahat et al., 2001, *Am J Hum Genet* 69:1378–1384 (PMID:11704930)** — the **D307H missense** in consanguineous **Bedouin families in Israel** (a founder mutation). Truncating/null and dominant/compound-het variants also reported (Postma et al., 2002, *Circ Res* 91:e21–e26).
- **TRDN (hgnc:12261; chr6q22).** Triadin — anchors CASQ2 to the RyR2/junctin complex at the junctional SR. **Recessive loss-of-function**; "triadin knockout syndrome" (CPVT + LQT-like). Roux-Buisson et al., 2012, *Hum Mol Genet*.
- **CALM1/2/3 (hgnc:1442/1445/1449).** Calmodulin — Ca²⁺ sensor regulating RyR2 (and Cav1.2, KCNQ1). **Dominant, often de novo, severe early-onset** CPVT/LQTS-overlap "calmodulinopathy." Nyegaard et al., 2012, *Am J Hum Genet* 91:703–712 (**PMID:23040497**).
- **TECRL (hgnc:27365).** Recessive; CPVT/LQTS-overlap phenotype (Devalla et al., 2016, *EMBO Mol Med*, hiPSC-CM evidence).

**Variant classification & type.** Per ACMG/AMP, the great majority of pathogenic CPVT alleles are **missense**; RyR2 gain-of-function is almost exclusively missense (whole-gene deletions/exon copy-number changes cause a distinct **RyR2 loss-of-function / "Ca²⁺-release-deficiency" phenotype**, not classic CPVT). CASQ2/TRDN include nonsense, frameshift, splice, and missense null alleles. ClinGen and structure-informed Bayesian penetrance models (2024–2025) are refining VUS interpretation using RyR2 cryo-EM domain mapping.

**Allele frequency.** Pathogenic RYR2 CPVT variants are **rare/absent in gnomAD**; RYR2 is highly constrained against missense in general population data. The Bedouin CASQ2 D307H shows elevated regional carrier frequency (founder effect).

**Somatic vs germline.** **Germline** (inherited or de novo). Some severe pediatric/CALM cases are **de novo**; germline mosaicism is documented and relevant to recurrence counseling.

**Functional consequences.** **RYR2 = gain-of-function** (leaky channel, ↓SOICR threshold, ↑diastolic Ca²⁺ leak). **CASQ2/TRDN/TECRL = loss-of-function** (reduced SR Ca²⁺ buffering/regulation → functionally analogous diastolic instability). **CALM = altered Ca²⁺-dependent RyR2 regulation** (gain-of-function-like on the release apparatus). All converge on **diastolic SR Ca²⁺ leak**.

**Modifier genes / genotype–phenotype.** RyR2 **variant location and specific residue** modulate penetrance/severity; C-terminal channel-domain variants tend toward more severe arrhythmia. No large-effect trans-modifier locus is established; polygenic and background-Ca²⁺-handling modifiers are hypothesized.

**Epigenetics / chromosomal abnormalities.** No established epigenetic mechanism or recurrent chromosomal abnormality; CPVT is a point-mutation/copy-number-of-single-gene disorder. Large RYR2 exonic deletions/duplications underlie a minority (and, when whole-gene, the LOF Ca²⁺-release-deficiency variant).

Suggested gene terms (HGNC, lowercase per dismech): `hgnc:10484` RYR2, `hgnc:1513` CASQ2, `hgnc:12261` TRDN, `hgnc:1442`/`1445`/`1449` CALM1/2/3, `hgnc:27365` TECRL.

---

## 5. Environmental Information

CPVT has **no toxic, radiation, occupational, or infectious cause.** The relevant "environmental" inputs are **physiologic adrenergic triggers**, not exposures:
- **Environmental/physical triggers:** vigorous **exercise**, competitive sport, acute **emotional stress/fright**, and administration of **catecholamines/β-agonists** (including diagnostic epinephrine/isoproterenol infusion). Fever can unmask arrhythmia in some overlap variants.
- **Lifestyle factors:** high-intensity/competitive athletics increase event risk (basis for exercise-restriction advice); caffeine/stimulants and sympathomimetic drugs are relational triggers to avoid.
- **Infectious agents:** none causal. (Fever from any infection may act as a nonspecific adrenergic trigger.)

---

## 6. Mechanism / Pathophysiology

CPVT is the archetypal disorder of **triggered activity from delayed afterdepolarizations (DADs) driven by SR calcium overload/leak.** The causal chain:

**1. Trigger — β-adrenergic stimulation (upstream).** Exercise/emotion → catecholamine release → β1-adrenergic → adenylyl cyclase → **cAMP → PKA** (and CaMKII) phosphorylation of Ca²⁺-handling proteins (RyR2, phospholamban, L-type Ca²⁺ channel), increasing SR Ca²⁺ load and RyR2 open probability.

**2. Molecular lesion — leaky RyR2 / defective SR Ca²⁺ buffering.**
- *RYR2 gain-of-function:* the channel's threshold for **store-overload-induced Ca²⁺ release (SOICR)** is lowered, so RyR2 opens spontaneously in **diastole** as the SR refills — a **diastolic SR Ca²⁺ leak.** Two mechanistic frameworks (complementary, sometimes debated): (a) **FKBP12.6/calstabin2 destabilization** — PKA hyperphosphorylation dissociates the stabilizing subunit, "unzipping"/hyperactivating the channel (**Wehrens et al., 2003, *Cell* 113:829–840, PMID:12809615**); (b) **defective SOICR/luminal Ca²⁺ regulation** — mutation lowers the luminal Ca²⁺ threshold for spontaneous opening (**Jiang et al., 2004, *PNAS* 101:13062–13067**, S.R.W. Chen lab). Post-translational **oxidation** and CaMKII phosphorylation further sensitize the channel.
- *CASQ2/TRDN loss-of-function:* reduced luminal Ca²⁺ buffering and impaired luminal RyR2 regulation destabilize the closed state — **same end effect** (diastolic Ca²⁺ leak, reduced SR content, premature release).

**3. Cellular event — DADs and triggered activity (core).** Diastolic cytosolic Ca²⁺ rise activates the electrogenic **Na⁺/Ca²⁺ exchanger (NCX1/SLC8A1)**, which extrudes 1 Ca²⁺ for 3 Na⁺ influx, generating a net **inward transient (I_ti)** → membrane **delayed afterdepolarization.** When a DAD reaches threshold it fires a **triggered action potential → premature ventricular beat.**

**4. Tissue-level — bidirectional/polymorphic VT (downstream).** Spatially heterogeneous DAD-triggered ectopy from **Purkinje/fascicular and ventricular myocardium** with alternating beat-to-beat origins produces the hallmark **bidirectional VT (≈180° QRS-axis alternans)**, degenerating into polymorphic VT and **ventricular fibrillation → syncope / sudden cardiac death.** The Purkinje network is implicated as a key source of triggered beats. Recent optical/computational work shows **subthreshold DADs disrupt ventricular activation** (RyR2-R420Q models, 2024–2025).

**Molecular pathways / GO & cell/anatomy terms.**
- Biological processes (GO): **GO:0055117** regulation of cardiac muscle contraction; **GO:0051209 / GO:0014808** release of sequestered Ca²⁺ into cytosol (SR); **GO:0060314** regulation of ryanodine-sensitive Ca²⁺-release channel activity; **GO:0051924** regulation of Ca²⁺ transport; **GO:0086002/GO:0086005** cardiac muscle cell action potential / ventricular cardiac muscle cell action potential; **GO:0006816** calcium ion transport.
- Molecular functions (GO): **GO:0005219** ryanodine-sensitive Ca²⁺-release channel activity; **GO:0005509** calcium ion binding; **GO:0015085** calcium ion transmembrane transporter activity (NCX).
- Cellular components (GO): **GO:0033017** sarcoplasmic reticulum membrane; **GO:0016529** sarcoplasmic reticulum; **GO:0014701** junctional SR membrane; **GO:0030315** T-tubule.
- Cell types (CL): **CL:0000746** cardiac muscle cell (cardiomyocyte); **CL:0002098** regular ventricular cardiac myocyte; **CL:0002068** Purkinje myocyte (cardiac conduction).
- Anatomy (UBERON): **UBERON:0002349** myocardium; **UBERON:0002084** heart left ventricle; **UBERON:0002094** interventricular septum; **UBERON:0002351** Purkinje fiber network; **UBERON:0000948** heart; **UBERON:0002061** sinoatrial node (bradycardia arm).
- Chemicals (CHEBI): **CHEBI:29108** calcium(2+); **CHEBI:17489** cyclic AMP; **CHEBI:29101** sodium(1+); catecholamines **CHEBI:33569** noradrenaline / **CHEBI:28918** adrenaline.

**Metabolic/immune involvement:** none — CPVT is **not** metabolic, inflammatory, or autoimmune. No energy-metabolism or immune mechanism; "tissue damage" is functional/electrical, not necrotic/fibrotic (heart is structurally normal).

**-omics.** hiPSC-derived cardiomyocytes from CPVT patients robustly recapitulate DADs/spontaneous Ca²⁺ release and are a primary IN_VITRO platform (e.g., patient-specific RyR2 lines; TECRL Devalla 2016). Single-cell Ca²⁺-imaging and computational myocyte models (Guinea-pig/human) quantify SOICR thresholds and pacing-dependent arrhythmogenesis.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **heart** (UBERON:0000948) — specifically **ventricular myocardium** (UBERON:0002349) and the **cardiac conduction/Purkinje system** (UBERON:0002351); **left ventricle** (UBERON:0002084). Structurally normal by imaging; the defect is functional/electrical.
- **Secondary/system involvement:** **cardiovascular system**; secondary **CNS** effects (syncope, hypoxic seizure) are consequences of transient arrhythmic cerebral hypoperfusion, not primary CNS disease. **Autonomic nervous system** (sympathetic cardiac innervation) is the trigger pathway and the target of sympathetic denervation therapy.
- **Tissue/cell level:** **cardiac muscle tissue**; affected cell populations = **ventricular cardiomyocytes (CL:0002098)** and **Purkinje myocytes (CL:0002068)**; atrial myocytes/SA-node cells account for supraventricular arrhythmia and bradycardia components.
- **Subcellular level (GO cellular component):** **sarcoplasmic reticulum (GO:0016529)** and **junctional SR membrane (GO:0014701)**; **T-tubule (GO:0030315)**; **dyadic cleft** RyR2–L-type-channel couplon; **sarcolemma/plasma membrane** (NCX, β-receptor).
- **Localization/lateralization:** biventricular/global myocardial process (not lateralized); therapeutically, the **left** stellate/thoracic sympathetic chain is targeted (left cardiac sympathetic denervation), reflecting left-dominant sympathetic influence on ventricular arrhythmogenesis.

---

## 8. Temporal Development

- **Onset:** typically **childhood/adolescence** (first/second decade); median first symptom/diagnosis ~**8–12 years** (systematic-review median 11 y). Rare congenital/infantile presentations (CALM, severe RYR2). Adult-onset milder forms exist. Onset pattern of *symptoms* is **acute/episodic** (event-driven), on a lifelong genetic substrate.
- **Progression / course:** **lifelong, episodic/triggered**, not neurodegenerative-style progressive. Within an exercise test, arrhythmia shows a **reproducible, graded escalation** (isolated PVCs → bigeminy/couplets → non-sustained → sustained bidirectional/polymorphic VT) above a threshold heart rate (~110–130 bpm). Untreated natural history is **malignant** (early cardiac arrest/SCD).
- **Patterns:** no spontaneous remission; **treatment-induced control** (β-blockade/flecainide/LCSD) is the goal. **Critical intervention window:** early diagnosis (often after a first syncope/aborted arrest or via family cascade screening) before a fatal event — the strongest determinant of outcome. Untreated cumulative mortality reaches ~30–50% by the third–fourth decade.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Prevalence:** estimated **~1 in 10,000** (Orphanet/GeneReviews). True prevalence likely underestimated (sudden death may be the first event; normal resting ECG defies routine screening).
- **Incidence:** not precisely established (rare disease); CPVT is a recognized cause of **autopsy-negative sudden unexplained death in the young / SIDS-adjacent cases** and drives a share of "idiopathic" exercise-related SCD.

**Genetic parameters.**
- **Inheritance pattern:** **autosomal dominant** — RYR2, CALM1/2/3, KCNJ2-associated (Andersen–Tawil overlap); **autosomal recessive** — CASQ2 (classic), TRDN, TECRL (dominant/compound-het CASQ2 also occur). De novo variants common in severe pediatric/CALM cases.
- **Penetrance:** overall clinical penetrance **~70–80%** (range reported 25–100%); **RYR2 mean penetrance ~83%**; **biallelic CASQ2 essentially 100% penetrant** in reported individuals. Structure-informed Bayesian models (2024–2025) show penetrance varies continuously by RyR2 domain/residue.
- **Expressivity:** **variable** — from asymptomatic exercise-test-positive carriers to childhood cardiac arrest, even within a family.
- **Anticipation:** not a feature (no repeat expansion).
- **Germline mosaicism:** documented; relevant to recurrence risk when a proband appears "de novo."
- **Founder effects:** **CASQ2 D307H** founder mutation in **Bedouin Israeli families** (Lahat 2001); other regional CASQ2/RYR2 founder alleles reported.
- **Consanguinity:** relevant for recessive CASQ2/TRDN/TECRL (consanguineous pedigrees).
- **Carrier frequency:** low; elevated regionally for founder alleles.

**Population demographics.**
- **Affected populations:** panethnic; recessive founder clusters in consanguineous populations (Bedouin, other Middle Eastern/North African).
- **Sex ratio:** roughly balanced overall; some cohorts show **female predominance** in ascertained series (systematic review 351 M / 463 F), but **male sex is associated with worse arrhythmic outcome/earlier events**. Gender-related inheritance-mode differences in RYR2 transmission have been reported.
- **Age distribution:** skewed young (index events predominantly in children/adolescents/young adults).

---

## 10. Diagnostics

**Core diagnostic approach:** demonstrate **reproducible exercise/catecholamine-induced ventricular ectopy/bidirectional or polymorphic VT** in the setting of a **normal resting ECG and structurally normal heart**, plus **genetic confirmation** and family history.

- **Resting ECG:** typically **normal** (sometimes sinus bradycardia, prominent U waves); QT normal (distinguishes from LQTS).
- **Exercise stress testing (cornerstone):** graded treadmill/bicycle test reproducibly provokes, above a threshold HR, **PVCs → ventricular bigeminy/couplets → non-sustained → bidirectional/polymorphic VT.** Highly reproducible; used for diagnosis and treatment monitoring. LOINC: standard exercise stress ECG panels.
- **Ambulatory (Holter) / event / implantable loop monitoring:** captures exertion-related ectopy and supraventricular arrhythmias.
- **Epinephrine or isoproterenol provocation:** pharmacologic catecholamine challenge when exercise testing is not feasible (lower sensitivity/specificity than exercise).
- **Echocardiography / cardiac MRI:** to confirm **structural normality** and exclude ARVC, myocarditis, ischemia, sarcoid.
- **Electrophysiology:** programmed stimulation is generally **not** useful (does not reliably induce CPVT VT — a distinguishing feature).
- **Biomarkers/labs:** none diagnostic; used to exclude ischemia/electrolyte causes.

**Genetic testing.**
- **Recommended approach:** targeted **CPVT/arrhythmia multigene panel** covering **RYR2, CASQ2, TRDN, CALM1/2/3, TECRL** (± KCNJ2), with **RYR2 as the highest-yield single gene (~50–60%).** WES/WGS reserved for panel-negative cases; **CNV/exon-level analysis of RYR2** is important (missed by some panels).
- **Cascade family screening:** predictive testing of first-degree relatives for a known familial variant is central to management; clinically-driven (exercise testing) screening for genotype-negative families.
- Not applicable: karyotype/FISH/CMA (single-gene disorder), mitochondrial DNA, repeat-expansion testing.

**Clinical diagnostic criteria.** Per **HRS/EHRA/APHRS 2013 expert consensus** (Priori et al.) and **ESC 2022 Guidelines on ventricular arrhythmias/SCD** (Zeppenfeld et al., *Eur Heart J* 2022): CPVT is diagnosed by (i) structurally normal heart + normal ECG + exercise/emotion-induced bidirectional/polymorphic VT in a person <40 y; or (ii) a pathogenic variant in a CPVT gene; or (iii) exercise-induced bidirectional/polymorphic VT in a family member of a CPVT proband.

**Differential diagnosis:** Long QT syndrome (esp. LQT1/LQT7 Andersen–Tawil, LQT with catecholamine sensitivity), Andersen–Tawil syndrome (KCNJ2), ARVC, idiopathic VF, digoxin toxicity (bidirectional VT), Timothy syndrome, and structural/ischemic VT.

---

## 11. Outcome / Prognosis

- **Untreated natural history is malignant:** ~**80%** syncope, ~**30%** cardiac arrest, and substantial early mortality (cumulative death/aborted-arrest reaching ~**30–50% by age 30–40**); SCD may be the sentinel event.
- **With treatment:** high-dose non-selective β-blockade (nadolol) markedly reduces mortality; addition of **flecainide** and/or **LCSD** further lowers arrhythmic events, though a **residual life-threatening arrhythmia burden persists** in a minority even on optimal therapy — hence ICD for refractory/high-risk patients.
- **Prognostic factors (worse outcome):** younger age at first symptom, cardiac arrest as presenting event, male sex, absence of/poor adherence to β-blockade, arrhythmia inducibility despite therapy on exercise testing, and specific RYR2 variant classes/locations. Persistent exercise-test-inducible complex ectopy on therapy is a key risk marker; suppression is a treatment goal.
- **Morbidity:** exercise restriction, ICD-related complications (inappropriate shocks — β-blockers reduce these), anxiety/psychosocial burden, and risk of arrhythmic syncope-related injury.
- **Recovery potential:** the substrate is lifelong; "recovery" = durable arrhythmia suppression, not cure (gene therapy aims to change this — §12).

---

## 12. Treatment

**Pharmacotherapy.**
- **β-blockers (first-line, all symptomatic and most genotype-positive patients).** **Non-selective β-blockers are superior**; **nadolol is the preferred agent** (long half-life, best evidence): **nadolol ~1–2.5 mg/kg/day**; propranolol ~2–4 mg/kg/day as alternative. MAXO: **MAXO:0000058** (pharmacotherapy) / drug class NCIT beta-adrenergic antagonist; agent CHEBI nadolol (**CHEBI:7439**), propranolol (**CHEBI:8499**). Mechanism: blunts the catecholaminergic trigger.
- **Flecainide (second-line add-on / and increasingly early combination).** Directly **inhibits RyR2 Ca²⁺ release** and blocks Na⁺ current, suppressing DAD-triggered beats. Efficacy shown in mice and humans: **Watanabe et al., 2009, *Nat Med* 15:380–383 (PMID:19330009)** and **van der Werf et al., 2011, *J Am Coll Cardiol* 57:2244–2254 (PMID:21616285)**. Add for breakthrough arrhythmia on β-blockade or up front in high-risk patients. CHEBI flecainide **CHEBI:4956**. (Mexiletine is an alternative Na⁺-channel adjunct in some overlap cases.)
- **Pharmacogenomics:** treatment is **genotype-informed** at the syndrome level (RYR2-leak biology → flecainide rationale); no established CYP-based dosing mandate, though flecainide is CYP2D6-metabolized (relevant to levels).

**Device / interventional / surgical.**
- **Left cardiac sympathetic denervation (LCSD)** — removal/ablation of the left stellate ganglion (lower half) + T2–T4 thoracic ganglia; **antiadrenergic** adjunct for patients with breakthrough events on medical therapy or ICD-shock storms (**Wilde et al., 2008, *N Engl J Med* 358:2024–2029, PMID:18463378**). Bilateral/right-sided denervation reported in refractory cases. MAXO: **MAXO:0000004** (surgical procedure).
- **Implantable cardioverter-defibrillator (ICD)** — for aborted cardiac arrest / refractory arrhythmia despite optimal drug therapy ± LCSD (secondary prevention; selective primary prevention). **Caveat:** ICD shocks can be **proarrhythmic** in CPVT (shock-induced catecholamine surge → arrhythmic storm), so **must be combined with maximal β-blockade**, programmed with long delays, and is not a substitute for pharmacotherapy. MAXO: implantation of cardioverter-defibrillator.
- **Catheter ablation** of a triggering PVC focus (e.g., Purkinje) is investigational/adjunctive in selected refractory cases.

**Lifestyle / supportive.** **Restriction of competitive and high-intensity exercise**, avoidance of sympathomimetic drugs/stimulants, treatment of triggers, and genetic counseling/family cascade screening are integral. MAXO: behavioral/lifestyle intervention.

**Experimental / advanced therapeutics (RNA & gene therapy — active 2023–2025 pipeline).**
- **AAV-CASQ2 gene replacement (SGT-501, Solid Biosciences; originating from the Priori/ICS Maugeri Pavia lab).** Delivers a codon-optimized full-length **CASQ2** to cardiomyocytes; increased calsequestrin improves SR Ca²⁺ buffering and stabilizes RyR2. Preclinical CASQ2-knock-in mice showed durable, potentially curative rescue with single systemic AAV delivery. **FDA Fast Track designation; first-in-human Phase 1b initiated ~2024–2025.** (MODEL_ORGANISM preclinical → early HUMAN_CLINICAL.)
- **RYR2-targeted approaches:** allele-specific silencing/CRISPR editing and RyR2-stabilizing small molecules (e.g., dantrolene, S107/"rycals" targeting FKBP12.6 binding) under preclinical/early investigation.
- Suggested treatment/modality tags (dismech): `therapeutic_modality: GENE_THERAPY` (AAV-CASQ2), `SMALL_MOLECULE` (nadolol, flecainide), `SURGERY` (LCSD), `DEVICE` (ICD), `BEHAVIORAL` (exercise restriction).

**Treatment strategy / algorithm (ESC 2022 / HRS 2013 consensus):** (1) β-blocker (nadolol) for all symptomatic and most genotype-positive patients + exercise restriction; (2) add **flecainide** for breakthrough arrhythmia (or up front in high-risk); (3) **LCSD** for persistent events / ICD-shock burden; (4) **ICD** for aborted arrest/refractory disease, always on maximal β-blockade; (5) cascade family screening; (6) emerging **gene therapy** for genetically defined (CASQ2) disease.

---

## 13. Prevention

- **Primary prevention:** not preventable at the population level (genetic). Prevention = **pre-symptomatic identification via family cascade genetic/exercise screening** of relatives of a proband, then prophylactic β-blockade + exercise restriction in genotype-positive individuals. **Avoidance of adrenergic triggers** (competitive sport, sympathomimetics).
- **Secondary prevention:** early diagnosis after a first syncope/aborted arrest; **exercise stress testing** as the key detection tool; treat before a fatal event.
- **Tertiary prevention:** escalate therapy (flecainide, LCSD, ICD) to prevent recurrent arrhythmia/SCD; adherence support; ICD shock-storm avoidance via β-blockade.
- **Genetic counseling:** autosomal-dominant (RYR2/CALM) vs recessive (CASQ2/TRDN/TECRL) recurrence risk; de novo/mosaicism counseling; predictive testing of minors is justified (early treatment prevents death). **Reproductive options:** prenatal testing and **preimplantation genetic testing (PGT)** available for known familial variants.
- **Public/behavioral:** athlete pre-participation awareness, family SCD history taking, AED access, CPR training for families; no immunization/environmental measures apply.

---

## 14. Other Species / Natural Disease

- **Taxonomy of models/natural disease:** primarily studied in **Mus musculus (NCBITaxon:10090)**; naturally occurring analogues reported in domestic species.
- **Orthologous genes:** *Ryr2*, *Casq2*, *Trdn*, *Calm1/2/3*, *Tecrl* are conserved across mammals (NCBI Gene orthologs in mouse/rat/dog).
- **Natural disease:** **German Shepherd dogs** exhibit an inherited ventricular-arrhythmia/SCD syndrome with catecholaminergic features studied as a large-animal model of ventricular arrhythmia; exercise/catecholamine-triggered ventricular arrhythmias occur in veterinary cardiology. (OMIA is the resource for animal Mendelian correlates.)
- **Comparative biology:** RyR2/CASQ2 Ca²⁺-handling and DAD/SOICR mechanisms are **evolutionarily conserved**, making cross-species models highly translational; species differences in heart rate and Ca²⁺-handling kinetics require caution when extrapolating triggering thresholds.
- **Transmission:** not applicable (non-communicable, no zoonotic potential).

---

## 15. Model Organisms

**Mouse (principal model).**
- **RYR2 knock-in models:** **RyR2-R4496C** (Cerrone et al., 2005) — the classic CPVT1 mouse; exercise/catecholamine-inducible bidirectional VT, DADs, faithful phenotype recapitulation. Other knock-ins: R2474S, R176Q, R420Q (used in recent activation-mapping/optical studies).
- **CASQ2 models:** **Casq2-null / Casq2-D307H knock-in** mice reproduce CPVT2 with catecholamine-induced VT — the platform for **AAV-CASQ2 gene-therapy** rescue studies (durable, near-curative correction).
- **Triadin/TECRL/CALM** knockout/knock-in models reproduce respective phenotypes.

**Model characteristics.** Mouse knock-ins **strongly recapitulate** the human phenotype (structurally normal heart, catecholamine/exercise-inducible bidirectional/polymorphic VT, cardiomyocyte DADs, spontaneous SR Ca²⁺ release) — hence high validity. **Limitations:** murine heart rate/electrophysiology differ from human; bidirectional VT morphology is less consistent; sudden-death rates and drug pharmacokinetics require careful translation.

**Cellular / in vitro models (IN_VITRO).**
- **Patient-specific hiPSC-derived cardiomyocytes** (RYR2, CASQ2, TECRL) reliably show DADs and abnormal diastolic Ca²⁺ release upon catecholamine challenge — used for mechanism, variant functional classification, and drug screening (e.g., flecainide response; Devalla 2016 TECRL).
- **Heterologous expression** (HEK293/lipid bilayer) of mutant RyR2 for single-channel SOICR/gating studies.
- **Isolated cardiomyocyte Ca²⁺ imaging** and **computational myocyte models** (guinea-pig/human ventricular) quantifying SOICR thresholds and pacing-dependent DAD/triggered activity.

**Applications.** Mechanistic dissection (SOICR vs FKBP12.6), preclinical testing of β-blockers/flecainide/rycals, and **AAV gene-therapy proof-of-concept** (CASQ2 rescue) that seeded the current clinical program. **Resources:** MGI/IMSR (mouse strains), Cellosaurus (hiPSC lines), Alliance of Genome Resources (orthology), OMIA (animal correlates).

---

## Key Citations (verify each PMID against the abstract before quoting in a KB YAML `snippet:`)

**Landmark / mechanistic**
- Leenhardt A, et al. *Circulation* 1995;91:1512–1519 — original clinical CPVT series. **PMID:7867192**
- Priori SG, et al. *Circulation* 2001;103:196–200 — RYR2 mutations cause CPVT1. **PMID:11208676**
- Lahat H, et al. *Am J Hum Genet* 2001;69:1378–1384 — CASQ2 D307H founder (Bedouin), CPVT2. **PMID:11704930**
- Priori SG, et al. *Circulation* 2002;106:69–74 — RYR2 clinical–genetic characterization. **PMID:12093772**
- Wehrens XHT, et al. *Cell* 2003;113:829–840 — FKBP12.6/calstabin2 destabilization mechanism. **PMID:12809615**
- Nyegaard M, et al. *Am J Hum Genet* 2012;91:703–712 — CALM1 in CPVT. **PMID:23040497**

**Treatment / outcome**
- Wilde AAM, et al. *N Engl J Med* 2008;358:2024–2029 — LCSD in CPVT. **PMID:18463378**
- Hayashi M, et al. *Circulation* 2009;119:2426–2434 — natural history/outcomes. **PMID:19398665**
- Watanabe H, et al. *Nat Med* 2009;15:380–383 — flecainide blocks RyR2, suppresses CPVT (mouse + human). **PMID:19330009**
- van der Werf C, et al. *J Am Coll Cardiol* 2011;57:2244–2254 — flecainide clinical efficacy. **PMID:21616285**

**Guidelines / consensus / recent**
- Zeppenfeld K, et al. 2022 ESC Guidelines for ventricular arrhythmias and prevention of SCD, *Eur Heart J* 2022.
- Priori SG, et al. HRS/EHRA/APHRS Expert Consensus on inherited primary arrhythmia syndromes, 2013.
- GeneReviews — *Catecholaminergic Polymorphic Ventricular Tachycardia* (Napolitano, Mazzanti, Priori et al.), NCBI Bookshelf **NBK1289** (gene fractions, penetrance, prevalence).
- Recent reviews (2023–2025): RYR2-ryanodinopathies (*Europace* 2023, euad156); JAHA 2024 "Molecular Insights to Preclinical Models" (JAHA.124.038308); *J Clin Med* 2024;13(6):1781; *Circ Arrhythm Electrophysiol* 2024–2025 RYR2 structure–penetrance studies.

---

**Sources (web-verified during this research):**
- [MDPI J Clin Med 2024 — CPVT clinical/diagnostic/therapeutic review](https://www.mdpi.com/2077-0383/13/6/1781)
- [Precision medicine in CPVT (PMC11135882)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11135882/)
- [JAHA 2024 — CPVT: Molecular Insights to Preclinical Models](https://www.ahajournals.org/doi/full/10.1161/JAHA.124.038308)
- [GeneReviews — CPVT (NBK1289)](https://www.ncbi.nlm.nih.gov/books/NBK1289/)
- [ClinGen Actionability summary — CPVT](https://actionability.clinicalgenome.org/ac/ui/Adult/ui/stg2SummaryRpt/AC042)
- [CPVT: an update (PMC6931575)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6931575/)
- [RYR2-ryanodinopathies: calcium overload to deficiency (Europace, PMC10311407)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10311407/)
- [Frontiers 2022 — Molecular changes in RyR2 with CPVT (PMC8867003)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8867003/)
- [Lahat et al. 2001 — CASQ2 Bedouin founder (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S000292970761266X)
- [OMIM 114251 — CASQ2](https://omim.org/entry/114251)
- [Solid Biosciences SGT-501 AAV-CASQ2 gene therapy — Phase 1b](https://www.cgtlive.com/view/solid-biosciences-cpvt-gene-therapy-sgt-501-cleared-phase-1b-trial)
- [FDA Fast Track for SGT-501 (Contemporary Pediatrics)](https://www.contemporarypediatrics.com/view/fda-grants-fast-track-designation-to-sgt-501-gene-therapy-for-cpvt)
- [Gene Therapy for CPVT (PMC5902314)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5902314/)
- [Heart Rhythm 2024 — Top stories on CPVT 2022–2024](https://www.heartrhythmjournal.com/article/S1547-5271(24)02566-9/fulltext)
- [RYR2 variants: protein structure & clinical data (Circ AE; PubMed 40875405)](https://pubmed.ncbi.nlm.nih.gov/40875405/)
- [Structural evaluation of RYR2-CPVT variants & Bayesian penetrance (PMC11957170)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11957170/)

---

### Curation handoff notes (dismech-specific)
When loading this into `kb/disorders/Catecholaminergic_Polymorphic_Ventricular_Tachycardia.yaml`:
1. This entry is a strong **conformer to the existing `cardiac_ion_channel_repolarization` module** — specifically the `#Arrhythmogenic Substrate and Triggered Activity` node (declare `conforms_to`), and it is a listed candidate/member of the **`Inherited_Arrhythmia_Syndromes` grouping**. Note the module's framing is "structurally normal hearts… RYR2-CPVT" — CPVT fits its calcium-handling/triggered-activity arm.
2. **Every snippet must be an exact abstract substring** — run `just fetch-reference PMID:XXXX` then `just validate-references` before commit; do not paste the paraphrased search-summary text above as snippets.
3. **Verify all ontology terms** (`just validate-terms-file`) — I've suggested HP/GO/CL/UBERON/CHEBI IDs from memory; confirm labels via OAK (e.g., HP:0004758 bidirectional VT, HP:0031677 polymorphic VT) before binding.
4. Model MOI explicitly per gene (AD RYR2/CALM vs AR CASQ2/TRDN/TECRL); the digenic pattern does not apply here, but multi-gene locus heterogeneity does.
5. Tag AAV-CASQ2 as `therapeutic_modality: GENE_THERAPY` and add the SGT-501 trial as a `clinical_trials` entry (fetch the NCT ID and validate against ClinicalTrials.gov).