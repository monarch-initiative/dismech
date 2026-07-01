---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-07-01T08:59:20.974764'
end_time: '2026-07-01T09:05:18.971659'
duration_seconds: 358.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Granulomatous Disease
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
  web_search_requests: 8
  num_turns: 10
  total_cost_usd: 2.1881684999999993
  session_id: 3c5b68a1-9a58-424f-b8af-cec443dc7974
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Granulomatous Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chronic Granulomatous Disease** covering all of the
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

I have strong grounding now. Here is the comprehensive research report.

---

# Comprehensive Research Report: Chronic Granulomatous Disease (CGD)

> **Curation note (dismech SOP compliance):** Every PMID and quoted snippet below is a *research lead*. Before any of these enter the `Chronic_Granulomatous_Disease.yaml` entry, each must be re-fetched with `just fetch-reference PMID:XXXX` and the snippet verified as an exact substring of the cached abstract; every ontology ID (HP/GO/CL/UBERON/CHEBI/MAXO/MONDO) must be verified with `just validate-terms-file`. I flag confidence levels where relevant. CGD is a well-characterized, low-NEC-risk classic immunodeficiency (distinct gene set, unambiguous MONDO/OMIM anchors), so named-entity confusion risk is low — but the ID-validation step is still mandatory.

---

## 1. Disease Information

**Overview.** Chronic granulomatous disease (CGD) is an inherited primary immunodeficiency (inborn error of immunity) caused by defects in the phagocyte NADPH oxidase complex (NOX2 system). Because neutrophils, monocytes, macrophages, and eosinophils cannot mount a normal **respiratory burst** — the burst of superoxide and downstream reactive oxygen species (ROS) that kills ingested microbes — patients suffer recurrent, life-threatening bacterial and fungal infections and a paradoxical tendency to **granuloma formation and hyperinflammation** (e.g., inflammatory bowel disease–like colitis). It is the prototypical **defect of phagocyte killing** (IUIS classification: "congenital defects of phagocyte number or function").

Think of the neutrophil as a cell that swallows a bacterium and is supposed to detonate a tiny oxidative bomb inside the phagosome. In CGD the fuse is cut — the microbe is engulfed but survives, and the frustrated immune system walls it off in a granuloma instead.

**Key identifiers:**
- **MONDO:** MONDO:0018305 (chronic granulomatous disease, umbrella); X-linked form MONDO:0010071
- **OMIM (phenotype series):**
  - 306400 — CGD, X-linked (CYBB / gp91-phox)
  - 233690 — CGD, autosomal recessive, cytochrome b–negative (CYBA / p22-phox)
  - 233700 — CGD, autosomal recessive, cytochrome b–positive, type I (NCF1 / p47-phox)
  - 233710 — CGD, autosomal recessive, type II (NCF2 / p67-phox)
  - 613960 — CGD, autosomal recessive, type III (NCF4 / p40-phox)
  - 618935 — CGD due to CYBC1/EROS deficiency
- **Orphanet:** ORPHA:379
- **ICD-10:** D71 (Functional disorders of polymorphonuclear neutrophils); **ICD-11:** 4A00.10
- **MeSH:** D006105 ("Granulomatous Disease, Chronic")

**Synonyms / historical names:** CGD; chronic granulomatous disease of childhood; congenital dysphagocytosis; "fatal granulomatosis of childhood" (historical, pre-antibiotic era); Bridges–Good syndrome; progressive septic granulomatosis; NADPH oxidase deficiency.

**Data derivation.** The knowledge base entry should be an **aggregated disease-level** synthesis (OMIM, Orphanet, GeneReviews, national/international CGD registries), not individual-EHR-derived. Major aggregate cohorts include the U.S. national registry of 368 patients (**PMID 10844935**, Winkelstein et al., *Medicine* 2000), the European experience (van den Berg et al., *PLoS One* 2009, **PMID 19381301**), and the residual-oxidase survival cohort of 287 patients (**PMID 21190454**, Kuhns et al., *NEJM* 2010).

Recent comprehensive reviews suitable as backbone citations: Roos D, *Br Med Bull* 2016; Arnold DE & Heimall JR, "A Review of Chronic Granulomatous Disease," *Adv Ther* 2017 (**PMID ~29168050**, verify); Yu JE et al., "Considerations in the Diagnosis of CGD," *J Pediatric Infect Dis Soc* 2018 (**PMID 29746674**); and the Justiz Vaillant/StatPearls chapter (**PMID via NBK493171**).

---

## 2. Etiology

**Primary cause — genetic.** CGD is monogenic. It results from loss-of-function variants in any one of six genes encoding subunits of the phagocyte NADPH oxidase (NOX2) complex or its assembly chaperone:

| Gene | Protein | Locus | Inheritance | Approx. share of cases |
|------|---------|-------|-------------|------------------------|
| **CYBB** | gp91-phox (NOX2) | Xp21.1–p11.4 | X-linked recessive | ~65–70% (∼2/3) |
| **NCF1** | p47-phox | 7q11.23 | Autosomal recessive | ~20–25% (most common AR) |
| **NCF2** | p67-phox | 1q25 | Autosomal recessive | ~5% |
| **CYBA** | p22-phox | 16q24 | Autosomal recessive | ~5% |
| **NCF4** | p40-phox | 22q13.1 | Autosomal recessive | rare (<1%) |
| **CYBC1 (EROS/C17orf62)** | Eros chaperone | 17q25.3 | Autosomal recessive | rare, recently described |

> *"Molecular defects in any of these five genes (CYBB for gp91phox … CYBA for p22phox, NCF1 for p47phox, NCF2 for p67phox, and NCF4 for p40phox) can occur in 90% of patients"* — supported by GeneReviews and the MDPI review (verify exact wording against PMID before use).

CYBB is X-linked; the other five are autosomal recessive. In Western/outbred populations X-linked disease predominates (males ~80% of patients); in populations with high consanguinity, autosomal recessive forms rise to parity or majority.

**Environmental/infectious triggers.** No environmental exposure *causes* CGD, but infections are the clinical trigger. Catalase-positive organisms are the pathogenic linchpin (see §5). Live vaccines (notably **BCG**) can cause disseminated disease ("BCGosis") in undiagnosed infants.

**Risk factors.**
- **Genetic risk:** hemizygous CYBB variant in males; biallelic pathogenic variants in an AR gene; carrier mother of an X-linked proband. Family history is the dominant risk factor.
- **Consanguinity** markedly increases AR-form risk.
- **Sex:** male (X-linked predominance).
- No established modifiable lifestyle risk factors.

**Protective factors.** In a well-documented gene–environment/genotype–phenotype effect, **residual NADPH oxidase activity** is strongly protective: patients retaining measurable superoxide production have markedly better survival (**PMID 21190454**, Kuhns et al.). Certain "leaky" CYBB missense/splice variants (e.g., the X91⁻ and X91ᵛᵃʳⁱᵃᵇˡᵉ subtypes) confer milder disease. **X-linked carrier females** with skewed X-inactivation toward the wild-type allele (>10–20% oxidase-normal neutrophils) are usually clinically protected from infection, though they may develop lupus-like/photosensitive and inflammatory features.

**Gene–environment interactions.** The central interaction is genotype (residual ROS) × microbial exposure: the lower the residual oxidase, the more catalase-positive organisms establish infection. There is no classic toxicant GxE; the "environment" is the microbiome/pathogen load.

---

## 3. Phenotypes

CGD phenotypes fall into two arms: **(A) infectious** and **(B) inflammatory/granulomatous**. Onset is usually **infancy to early childhood** (most diagnosed at 1–3 years; milder AR/p47-phox cases may present in adolescence/adulthood). Course is **chronic-lifelong, episodic/recurrent**. Severity is **variable**, tracking residual oxidase activity.

### A. Infectious phenotypes
- **Recurrent bacterial and fungal infections** — the defining feature. Suggested HP: *Recurrent bacterial infections* (HP:0002718), *Recurrent fungal infections* (HP:0002841 — verify), *Immunodeficiency* (HP:0002721).
- **Pneumonia / recurrent pneumonia**, often *Aspergillus* — HP:0002090 (Pneumonia); *Aspergillosis* HP:0033100 (verify). Frequency: very frequent (leading cause of infection and death).
- **Suppurative/lymphadenitis and abscesses** — lymphadenitis (HP:0002716 — verify), **liver abscess** (staphylococcal, characteristically "dense/caseous") — Hepatic abscess (verify ID), **perianal/perirectal abscess**, **skin abscesses/pustular dermatitis**.
- **Osteomyelitis** (including *Serratia*, *Aspergillus*, *Burkholderia*) — HP:0002754 (verify).
- **Septicemia / sepsis** (Burkholderia, Salmonella) — Sepsis (verify).
- **Otitis, sinusitis, gingivitis/stomatitis, aphthous ulcers**.

### B. Inflammatory/granulomatous phenotypes
- **Granuloma formation** — hallmark; obstructing granulomas of GU (bladder) and GI tract. Suggested HP: *Granuloma* (HP:0032252 — verify).
- **Inflammatory bowel disease (IBD)–like colitis** — up to ~40–50% of patients, especially X-linked; diarrhea, failure to thrive, perianal disease, strictures. HP: *Colitis* (HP:0002583 — verify), *Diarrhea* (HP:0002014), *Inflammatory abnormality of the large intestine*.
  > *"…up to 50% of patients having gastrointestinal involvement meeting diagnostic criteria for inflammatory bowel disease"* (USIDNET registry, **PMID 35...**/PMC9086117 — verify).
- **Gastric outlet obstruction / antral narrowing**, esophageal/ureteral strictures.
- **Hepatosplenomegaly and lymphadenopathy** — Splenomegaly (HP:0001744), Hepatomegaly (HP:0002240), Lymphadenopathy (verify).
- **Failure to thrive / growth delay / short stature** — HP:0001508 (Failure to thrive), HP:0001510 (Growth delay).
- **Chorioretinitis / retinal lesions**; **discoid-lupus/photosensitive skin lesions** (especially in X-linked carriers).
- **Autoimmune/autoinflammatory features** (lupus-like, JIA-like, antiphospholipid).

### Laboratory-abnormality phenotypes
- **Abnormal/absent neutrophil respiratory burst** (DHR-123 flow cytometry, NBT) — the central lab phenotype.
- **Anemia of chronic disease, leukocytosis, elevated ESR/CRP**, hypergammaglobulinemia, elevated IL-18/IFN-γ in inflamed tissue (PMC6813411).

**Quality-of-life impact.** Chronic infections, IBD-like colitis, frequent hospitalizations, prolonged IV antimicrobials, growth failure, and (historically) shortened lifespan substantially reduce QoL; colitis is a major driver of morbidity. Formal EQ-5D/SF-36 CGD datasets are sparse — flag as data-limited.

---

## 4. Genetic / Molecular Information

**Causal genes & products (HGNC):**
- **CYBB** (hgnc:2578) → gp91-phox / NOX2 (catalytic β-subunit of flavocytochrome b₅₅₈).
- **CYBA** (hgnc:2577) → p22-phox (α-subunit; stabilizes gp91-phox in the membrane).
- **NCF1** (hgnc:7660) → p47-phox ("organizer" cytosolic factor).
- **NCF2** (hgnc:7661) → p67-phox ("activator" cytosolic factor; binds Rac).
- **NCF4** (hgnc:7662) → p40-phox (cytosolic; phagosomal targeting via PX domain).
- **CYBC1 / EROS** (verify HGNC) → chaperone required for gp91-phox/p22-phox expression.

> Use **lowercase `hgnc:`** CURIEs per repo convention.

**Variant landscape.**
- **CYBB:** highly heterogeneous — nonsense, frameshift, splice-site, missense, large deletions/insertions across the gene. Classified by residual protein/function: **X91⁰** (absent gp91-phox, no oxidase — most severe), **X91⁻** (reduced), **X91⁺** (normal protein, non-functional). Large contiguous Xp21 deletions can produce a **contiguous gene syndrome** (CGD + McLeod/Kell phenotype ± Duchenne muscular dystrophy ± retinitis pigmentosa/ornithine transcarbamylase).
- **NCF1:** the **ΔGT dinucleotide deletion (c.75_76delGT)** at the start of exon 2 accounts for the vast majority of p47-phox alleles; it arises from recombination with adjacent NCF1 pseudogenes (ψNCF1), complicating molecular diagnosis and gnomAD frequency estimates.
- Variant **classification** (ACMG/AMP): most are pathogenic/likely pathogenic loss-of-function; consult **ClinVar** and the curated **CYBB/NCF1 mutation databases** (Roos et al.). **Somatic vs germline:** germline (X-linked hemizygous or AR biallelic); no somatic mechanism.
- **Functional consequence:** loss of function (failure to assemble/activate the oxidase). A few missense variants are hypomorphic (partial function → milder phenotype). A distinct **p40-phox (NCF4)** defect selectively impairs *intracellular/phagosomal* ROS with relatively preserved extracellular burst, giving a colitis-predominant, infection-mild phenotype.

**Modifier genes / genetic modifiers.** Residual oxidase level is the dominant severity modifier (functionally, not a separate locus). Polymorphisms in myeloperoxidase, mannose-binding lectin, FcγR, and inflammatory loci have been proposed to modify infection/inflammation risk (weaker evidence). X-inactivation skewing modifies carrier-female phenotype.

**Epigenetic information.** No established primary epigenetic mechanism; X-linked carrier phenotype is governed by **X-chromosome inactivation (lyonization)** patterns. Flag as not-a-major-feature.

**Chromosomal abnormalities.** Large **Xp21 contiguous deletions** (structural) as above; detectable by MLPA/CMA/karyotype. Otherwise CGD is a single-gene disorder.

**Allele frequency.** Individual pathogenic variants are rare; because CGD is severe, causal alleles are at very low frequency in gnomAD. The NCF1 ΔGT is confounded by pseudogene mapping — treat gnomAD NCF1 frequencies with caution.

---

## 5. Environmental Information

**Infectious agents (central to CGD).** The classic vulnerability is to **catalase-positive** organisms (catalase degrades microbial H₂O₂ that could otherwise substitute for the missing host oxidant). The "big five" CGD pathogens:
1. **Staphylococcus aureus** (catalase⁺; liver abscess, lymphadenitis, osteomyelitis) — NCBITaxon:1280
2. **Burkholderia (Pseudomonas) cepacia** complex (pneumonia, sepsis — high mortality) — NCBITaxon:87882/292
3. **Serratia marcescens** (osteomyelitis, soft-tissue) — NCBITaxon:615
4. **Nocardia** species (necrotizing pneumonia) — NCBITaxon:1817
5. **Aspergillus** species (*A. fumigatus*, *A. nidulans* — the latter almost pathognomonic; invasive pulmonary/osteo aspergillosis; **leading cause of death**) — NCBITaxon:746128 (*A. fumigatus*)

Other important agents: **Salmonella**, **Granulibacter bethesdensis**, **Chromobacterium violaceum**, **Mycobacterium** (including **BCG** vaccine strain and *M. tuberculosis*), *Candida* spp.

> *"Aspergillus species was the first cause of infection and of death in cohorts, which underscores the importance of antifungal prophylaxis with itraconazole."* (review; verify).

**Environmental/lifestyle factors.** Exposure to decaying organic matter/mulch/gardening (mold — *Aspergillus*, and **mulch pneumonitis**, an acute fulminant fungal alveolitis after heavy inhalation) is a recognized precipitant. **Live vaccines (BCG, live Salmonella typhi)** are contraindicated. Smoking/aerosolized fungal exposure worsens pulmonary risk. No dietary cause.

---

## 6. Mechanism / Pathophysiology

**Core molecular defect.** The phagocyte NADPH oxidase (NOX2 complex) normally assembles at the phagosomal/plasma membrane: the membrane **flavocytochrome b₅₅₈** (gp91-phox + p22-phox) docks the cytosolic regulatory factors **p47-phox, p67-phox, p40-phox** and the small GTPase **Rac2 (Rac1 in some cells)**. Assembly enables electron transfer from cytosolic NADPH across the membrane to molecular O₂, generating **superoxide (O₂•⁻)** — the **respiratory (oxidative) burst**. Superoxide dismutates to H₂O₂ and, with myeloperoxidase, forms hypochlorous acid and other microbicidal ROS.

> Suggested GO terms: **respiratory burst (GO:0045730)**, **superoxide anion generation (GO:0042554)**, **superoxide metabolic process (GO:0006801)**, **superoxide-generating NAD(P)H oxidase activity (GO:0016175, MF)**, **defense response to fungus (GO:0050832)**, **phagocytosis (GO:0006909)**, **inflammatory response (GO:0006954)**.

**Causal chain (upstream → downstream):**
1. **Loss-of-function variant** in a NOX2-complex gene → **failure to assemble/activate NADPH oxidase** (upstream trigger).
2. **Absent/deficient respiratory burst** → failure to generate O₂•⁻/H₂O₂/HOCl in the phagosome.
3. **Impaired oxygen-dependent microbial killing** → ingested **catalase-positive** organisms survive intracellularly (catalase-negative organisms self-supply H₂O₂ and are still killed).
4. **Recurrent/persistent infection** by the characteristic pathogens → abscesses, pneumonia, osteomyelitis, sepsis.
5. **Failure to clear organisms/antigen + defective apoptosis/efferocytosis and dysregulated inflammation** → persistent macrophage activation → **granuloma formation** and **sterile hyperinflammation** (colitis, obstructive granulomas). This is the paradox: too little killing *and* too much inflammation.

**Why the hyperinflammation? (downstream mechanisms).** ROS are not only microbicidal — they are anti-inflammatory signals. In their absence:
- **Defective NLRP3 inflammasome regulation** and **excess IL-1β / IL-18** (redox normally restrains inflammasome activity).
- **Impaired neutrophil apoptosis and macrophage efferocytosis** → prolonged inflammatory cell persistence.
- **Defective autophagy/LC3-associated phagocytosis** → failure to degrade cargo, sustained NF-κB and inflammasome signaling.
- **Reduced tryptophan→kynurenine (IDO) and impaired Nrf2 signaling**, **failure to inactivate pro-inflammatory mediators**, and **defective neutrophil extracellular trap (NET) formation** (ROS-dependent NETosis is deficient).
- **Impaired resolution of inflammation** and dysregulated Th17/IL-17 responses.

> Backbone reviews for the inflammation mechanism: *"Chronic granulomatous disease: why an inflammatory disease?"* (PMC4230281); *"Hyperinflammation in CGD and anti-inflammatory role of the phagocyte NADPH oxidase,"* Segal et al., *Semin Immunopathol* 2008; high tissue IL-18/IFN-γ (PMC6813411). Verify PMIDs.

**Cell types (CL):** neutrophil (**CL:0000775**), monocyte (**CL:0000576**), macrophage (**CL:0000235**), eosinophil (CL:0000771), granulocyte/myeloid leukocyte (CL:0000094 / CL:0000766).

**Tissue-damage mechanisms:** granulomatous/obstructive tissue remodeling, abscess/necrosis from uncontrolled infection, fibrosis (bladder/GI strictures), and inflammatory tissue injury from sustained cytokine output.

**Molecular profiling.** Transcriptomic/proteomic studies show heightened inflammatory-gene and inflammasome signatures in CGD phagocytes; single-cell and functional (CRISPR) work on NOX2 assembly exists but is not central to the clinical entry — flag as supplementary. Diagnostic "profiling" is functional (DHR flow), not omics.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Lung** (UBERON:0002048) — pneumonia, invasive aspergillosis, mulch pneumonitis, fibrosis.
- **Lymph nodes** (UBERON:0000029) — suppurative lymphadenitis.
- **Liver** (UBERON:0002107) — hepatic abscess (often staphylococcal), hepatomegaly, nodular regenerative hyperplasia/portal hypertension.
- **Spleen** (UBERON:0002106) — splenomegaly, abscess.
- **Skin/soft tissue** (UBERON:0002097) — abscesses, pustular/eczematoid dermatitis, granulomatous lesions.
- **Gastrointestinal tract** — colon (UBERON:0001155) and small intestine (UBERON:0002108): IBD-like colitis, granulomas, strictures; **stomach/gastric antrum** (outlet obstruction).
- **Bone** — osteomyelitis (small bones, ribs, vertebrae).
- **Genitourinary tract** — bladder granulomas, ureteral obstruction.
- **Bone marrow** (UBERON:0002371) — site of the defective myeloid progenitors and target of curative HSCT/gene therapy.
- **Eye** — chorioretinal lesions.

**Body systems:** immune/hematopoietic (primary), respiratory, digestive, integumentary, musculoskeletal, genitourinary, hepatobiliary.

**Cell/tissue level:** myeloid phagocytes (neutrophils, monocytes/macrophages, eosinophils); granuloma = epithelioid macrophages ± multinucleated giant cells and lymphocytes; characteristic **pigment-laden (lipofuscin) macrophages** on histology.

**Subcellular level (GO cellular component):** **phagocytic vesicle / phagosome membrane (GO:0045335)**, **plasma membrane / specific (secondary) granule membrane**, and the **NADPH oxidase complex (GO:0043020, NADPH oxidase complex)** localized to phagosome and plasma membrane. Flavocytochrome b₅₅₈ resides in secretory vesicles/specific granule and plasma membranes.

**Localization/lateralization:** multifocal and **bilateral/systemic** — infections and granulomas occur wherever phagocytes confront organisms; no consistent lateralization.

---

## 8. Temporal Development

**Onset.** Typically **infancy/early childhood** — most X-linked patients present and are diagnosed within the first 1–3 years of life; AR forms (especially p47-phox) skew later, with some diagnosed in adolescence or adulthood. Onset pattern is **chronic with acute infectious exacerbations** superimposed.

**Progression.** **Chronic, lifelong**, punctuated by recurrent infections and inflammatory flares (**episodic/relapsing**). Without curative therapy, cumulative organ damage (pulmonary fibrosis, GI strictures, hepatic disease) accrues. Inflammatory complications (colitis) often persist or worsen independent of infection control.

**Stages / natural history:** no formal staging. Historically, mortality was highest in the first decade; modern prophylaxis has shifted major morbidity/mortality into adolescence and adulthood, where **Aspergillus** and **Burkholderia** infections and progressive inflammatory/GI disease dominate.

**Critical windows:** infancy (BCG avoidance; early diagnosis prevents catastrophic first infections); pre-adolescence is the recommended window for HSCT in severe (low-residual-oxidase) patients while organ damage is limited (**PMID 21190454** rationale). Remission of infections is **treatment-induced** (prophylaxis, curative HSCT/gene therapy); spontaneous remission does not occur.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Incidence/prevalence:** ~**1 in 200,000–250,000 live births** in the U.S. (Winkelstein registry, **PMID 10844935**); worldwide estimates ~1/100,000–1/250,000 depending on consanguinity. Approx. 20 new U.S. cases/year historically.
  > *"A registry of United States residents with CGD was established in 1993 … 368 patients were registered; 259 had the X-linked recessive form … and 81 had one of the autosomal recessive forms."* (PMID 10844935).
- **Sex ratio:** ~**80% male** (X-linked predominance) in outbred populations.
- **Age distribution:** diagnosis concentrated in early childhood; survival now often into 4th–5th decades and beyond.

**Inheritance genetics.**
- **Pattern:** X-linked recessive (CYBB) + autosomal recessive (CYBA, NCF1, NCF2, NCF4, CYBC1).
- **Penetrance:** essentially **complete** in affected males (X-linked) and biallelic AR individuals; **expressivity is variable** (residual-oxidase-dependent).
- **Carrier females (X-linked):** mosaic neutrophil populations; usually asymptomatic for infection but may have **discoid-lupus/photosensitive** and autoimmune features; risk of symptomatic infection rises when wild-type neutrophils fall below ~10–20%.
- **Consanguinity:** raises AR-form frequency; in high-consanguinity regions AR forms equal or exceed X-linked.
- **Founder effects:** NCF1 ΔGT (pseudogene-mediated) is a recurrent, quasi-"founder" allele; regional founder variants reported (e.g., specific NCF2/CYBA alleles in Middle Eastern and Israeli Arab/Jewish populations).
- **Germline mosaicism / anticipation:** not a feature (no repeat expansion). New (de novo) CYBB variants occur in a minority of X-linked cases.
- **Carrier frequency:** low; population-specific for AR alleles.

**Geographic distribution.** Worldwide; relative gene-form distribution varies with consanguinity. No endemic clustering beyond that driven by founder alleles.

---

## 10. Diagnostics

**Functional screening/confirmation (the core test):**
- **Dihydrorhodamine-123 (DHR) flow cytometry** — current gold-standard functional assay; measures the neutrophil oxidative burst after PMA stimulation. Quantifies **residual oxidase** and reveals the bimodal pattern of X-linked **carriers**. (LOINC-codable oxidative-burst assay — verify LOINC.)
- **Nitroblue tetrazolium (NBT) slide test** — older qualitative assay, largely superseded by DHR.
- Both detect the defining lab abnormality: absent/reduced respiratory burst.

**Confirmatory protein/biochemical tests:** immunoblot/flow for gp91-phox and p22-phox (cytochrome b₅₅₈ "positive/negative" typing); cytochrome b spectral assay; NADPH oxidase activity assays.

**Genetic testing (definitive subtype/carrier assignment):**
- **Targeted single-gene sequencing** guided by DHR pattern + protein typing (e.g., CYBB in males with X-linked pattern).
- **CGD/primary-immunodeficiency NGS gene panels** or **WES/WGS** when the pattern is ambiguous. WGS/CMA/MLPA needed for **large deletions/contiguous Xp21 syndromes** and to resolve **NCF1 pseudogene** complexity (NCF1 requires specialized assays — gene-specific PCR/pyrosequencing for the ΔGT and pseudogene ratio).
- **Carrier testing / prenatal diagnosis** available once the familial variant is known.

**Imaging & supportive tests:** CT chest (pneumonia, fungal nodules, "halo" sign of aspergillosis), abdominal imaging/CT for liver abscess and bowel disease, endoscopy/biopsy for colitis. Histopathology: non-caseating granulomas, **pigmented lipofuscin-laden macrophages**, abscesses (SNOMED/pathology-codable).

**Differential diagnosis:** other phagocyte disorders (leukocyte adhesion deficiency, myeloperoxidase deficiency, Chédiak–Higashi, glucose-6-phosphate dehydrogenase deficiency with severe deficit — can mimic oxidase failure), hyper-IgE syndrome, Mendelian susceptibility to mycobacterial disease, Crohn disease (for the colitis phenotype), and other IEIs with granulomas. **Key distinguisher:** the abnormal DHR/NBT respiratory-burst assay.

**Screening:** not part of standard newborn screening (TREC-based SCID screening does not detect CGD). **Cascade/carrier screening** of at-risk relatives once a proband variant is identified is standard.

---

## 11. Outcome / Prognosis

**Survival / mortality.**
- Prognosis has improved dramatically. Historically fatal in childhood; with modern prophylaxis, many patients survive into the **4th–5th decade**. Contemporary mortality is ~**1.5–3% per year** in registry cohorts.
- **X-linked disease carries worse prognosis than AR** (lower residual oxidase), and **residual oxidase strongly predicts survival** — patients in the lowest superoxide quartile have the highest mortality, with divergence after age ~20 (**PMID 21190454**, Kuhns et al.).
  > *"…patients with the least residual … reactive oxygen intermediate production had the lowest survival."* (Kuhns 2010 — verify exact wording).
- **Leading causes of death:** invasive **fungal (Aspergillus)** infection and **Burkholderia** sepsis/pneumonia.

**Morbidity / complications.** Recurrent pneumonia and pulmonary fibrosis, hepatic abscess and portal hypertension/nodular regenerative hyperplasia, **IBD-like colitis** (major morbidity), GU/GI obstructive granulomas, growth failure, and inflammatory/autoimmune disease. Frequent hospitalizations and long antimicrobial courses.

**Curative-therapy outcomes.** Allogeneic **HSCT** now yields **~90% overall survival** in modern series (matched-sibling and matched-unrelated donors), with best results in younger patients with matched donors and controlled infection at transplant.
- 712-patient international HSCT study (Chiesa et al., *Blood* 2020, **PMID ~32202630** — verify): low graft failure and mortality across ages.
- Single-center late-survival cohort: OS ~**90% at 2 years and ~81% at 5 years** (JACI 2022).
- Reduced-intensity conditioning HSCT: Güngör et al., *Lancet* 2014 (**PMID 24161820**) — 2-year survival ~96% in a prospective series.

**Prognostic factors:** residual oxidase activity (dominant), genotype/inheritance (X-linked worse), age and organ damage at HSCT, donor match, active infection at transplant, severity of inflammatory/GI disease.

---

## 12. Treatment

### A. Lifelong prophylaxis (standard of care)
- **Antibacterial:** **trimethoprim–sulfamethoxazole (co-trimoxazole)** (CHEBI: trimethoprim 45924; sulfamethoxazole 9332) — reduces bacterial infections. MAXO: *antibiotic therapy* / *pharmacotherapy* (verify MAXO ID).
- **Antifungal:** **itraconazole** (CHEBI:6076) — landmark placebo-controlled prophylaxis trial (Gallin et al., *NEJM* 2003, **PMID 12802026** — verify) significantly reduced serious fungal infections; posaconazole (CHEBI:64355)/voriconazole (CHEBI:10023) used for treatment/breakthrough.
  > *"Itraconazole … was effective in preventing fungal infections in patients with chronic granulomatous disease."* (NEJMoa021931 — verify).
- **Immunomodulatory:** **Interferon-γ (IFN-γ, 1b)** three-times-weekly SC — the International CGD Cooperative Study (*NEJM* 1991, **PMID 1846940** — verify) showed ~70% reduction in serious infections.
  > *"…interferon gamma reduced the frequency of serious infections in patients with chronic granulomatous disease."* (verify exact quote).

### B. Acute infection management
Aggressive, culture-directed IV antibacterials/antifungals; often prolonged courses. **Granulocyte transfusions** for severe refractory infection (adjunct). Surgical drainage of abscesses.

### C. Management of inflammatory/granulomatous disease
Corticosteroids for obstructive granulomas and colitis; steroid-sparing agents; anti-inflammatory/immunosuppressive therapy for IBD-like colitis. **Caution:** anti-TNF biologics increase severe infection risk in CGD (case reports of fatal fungal infection) — use judiciously.

### D. Curative therapy
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — the established cure; replaces defective myeloid lineage. MAXO: *hematopoietic stem cell transplantation* (verify MAXO ID; MAXO:0010039 organ transplantation is too generic). Reduced-intensity conditioning improves outcomes (Güngör 2014).
- **Autologous ex vivo lentiviral gene therapy** (X-linked/gp91-phox) — corrects CD34⁺ HSPCs with a myeloid-specific promoter-driven gp91-phox vector.
  > **Kohn DB et al., *Nat Med* 2020 (PMID 31988463):** nine X-CGD patients treated; *"…six of the seven surviving patients demonstrated stable vector copy numbers (0.4–1.8 copies per neutrophil)"* and stable oxidase-positive neutrophils sufficient for clinical benefit (verify exact wording). Modality: **GENE_THERAPY**; earlier retroviral trials were complicated by insertional myelodysplasia/clonal expansion, motivating self-inactivating lentiviral designs.
- Investigational: gene-corrected p47-phox lentiviral vectors (preclinical, PMC8575060); CRISPR/base-editing approaches (preclinical).

**Pharmacogenomics:** azole levels vary widely (CYP3A4/itraconazole absorption); therapeutic drug monitoring recommended. No specific germline PGx gating beyond the disease genotype.

**Supportive care:** avoidance of mulch/decaying vegetation and live vaccines; dental/skin hygiene; nutritional support for colitis-related growth failure; genetic counseling.

---

## 13. Prevention

- **Primary prevention:** the disease itself cannot be prevented (monogenic), but **infection prevention** is central — lifelong co-trimoxazole + itraconazole ± IFN-γ; avoidance of environmental mold exposure and **contraindication of live vaccines (BCG, oral typhoid)**.
- **Secondary prevention:** early diagnosis via family history and DHR testing of at-risk newborns; prompt cascade/carrier screening.
- **Tertiary prevention:** aggressive early treatment of infections; surveillance for colitis, liver, and pulmonary complications; timely referral for HSCT/gene therapy before irreversible organ damage.
- **Genetic counseling & reproductive options:** carrier testing, **prenatal diagnosis**, and **preimplantation genetic diagnosis** once the familial variant is known.
- **Prophylaxis (medication):** co-trimoxazole (antibacterial), itraconazole (antifungal), IFN-γ (immunomodulatory) — see §12.

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected species:** primarily **human (NCBITaxon:9606)**. Naturally occurring CGD-like NADPH-oxidase disease is documented in **dogs** (NCBITaxon:9615) and described in cattle.
- **Natural animal disease / OMIA:** canine CGD-type leukocyte oxidase defects and, notably, **Bovine Leukocyte Adhesion Deficiency** is a *distinct* phagocyte disorder (do not conflate); search **OMIA** for "granulomatous"/NADPH oxidase entries in dog/cattle for veterinary orthologs.
- **Orthologous genes:** CYBB/NCF1/NCF2/CYBA/NCF4 are conserved across mammals (mouse *Cybb*, *Ncf1*, *Ncf2*, *Cyba*, *Ncf4* — NCBI Gene). Deep evolutionary conservation of the NOX2 phagocyte-oxidase system.
- **Comparative biology:** knockout mice recapitulate the killing defect and granuloma/hyperinflammation, validating the anti-inflammatory role of NOX2-derived ROS across species.
- **Transmission:** none — non-infectious, non-zoonotic (it is a germline genetic disorder).

---

## 15. Model Organisms

- **Mouse (Mus musculus, NCBITaxon:10090) — primary model.**
  - **Cybb (gp91-phox) knockout** and **Ncf1 (p47-phox) knockout** mice are the workhorse models. They reproduce (a) **defective respiratory burst and increased susceptibility** to *Aspergillus*, *Burkholderia*, *Staphylococcus*, *Salmonella*, and (b) **exaggerated/granulomatous inflammation** and sterile hyperinflammation — directly demonstrating that NOX2-derived ROS restrain inflammation. Models: knockout, conditional, and **humanized/gene-corrected** lines used in gene-therapy preclinical work (MGI, IMSR).
  - Used to model prophylaxis, HSCT, and lentiviral gene-therapy correction (e.g., p47-phox lentiviral rescue restoring anti-*Salmonella* function, *Gene Ther* 2020).
- **Cellular/in vitro models:** patient **CD34⁺ HSPCs**, **iPSC-derived neutrophils/macrophages** (for gene-editing/gene-therapy testing), immortalized myeloid lines (e.g., PLB-985 gp91-phox knockouts) — key IN_VITRO systems for oxidase-assembly studies and CRISPR correction.
- **Model characteristics / limitations:** mouse models recapitulate the killing defect and hyperinflammation well but differ in **pathogen spectrum and colitis phenotype severity**; the human **NCF1 pseudogene** architecture has no direct murine counterpart, limiting modeling of the common human p47-phox ΔGT allele. Flag as **HUMAN_MODEL_MISMATCH** candidates where mouse inflammation/colitis does not fully mirror human IBD-like disease.
- **Resources:** MGI (mouse), IMPC/KOMP (knockouts), Cellosaurus (PLB-985 and derivatives), Alliance of Genome Resources (orthology).

---

## Suggested dismech Entry Scaffolding (quick reference)

- **MONDO:** MONDO:0018305 (umbrella); consider modeling X-linked (MONDO:0010071) and AR forms as subtypes (`has_subtypes`: *X-linked / CYBB*, *AR p47-phox / NCF1*, *AR p67-phox / NCF2*, *AR p22-phox / CYBA*, *AR p40-phox / NCF4*, *AR CYBC1/EROS*).
- **Causal genes (hgnc):** CYBB (hgnc:2578), CYBA (hgnc:2577), NCF1 (hgnc:7660), NCF2 (hgnc:7661), NCF4 (hgnc:7662), CYBC1 (verify).
- **Core GO/CL/UBERON/CHEBI/MAXO terms** as listed in §§6–7, 12 — **all require OAK validation**.
- **Pathophysiology causal chain:** NOX2-complex LoF variant → failed oxidase assembly → absent respiratory burst → impaired killing of catalase-positive microbes → recurrent infection **and** (parallel arm) impaired ROS-dependent inflammation control → granuloma/colitis/hyperinflammation.
- **Priority evidence PMIDs to fetch & verify:** 10844935 (registry/epidemiology), 21190454 (residual oxidase/survival), 12802026 (itraconazole prophylaxis — verify), 1846940 (IFN-γ trial — verify), 31988463 (lentiviral gene therapy), 24161820 (RIC-HSCT — verify), plus the *Blood* 2020 712-patient HSCT study and the USIDNET IBD/CGD paper (verify PMIDs).

---

### Sources (web-verified during this research)
- [GeneReviews: Chronic Granulomatous Disease (NBK99496)](https://www.ncbi.nlm.nih.gov/books/NBK99496/)
- [StatPearls: Chronic Granulomatous Disease (NBK493171)](https://www.ncbi.nlm.nih.gov/books/NBK493171/)
- [CGD: Epidemiology, Pathophysiology, and Genetic Basis (J Pediatric Infect Dis Soc, PMC5946813)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5946813/)
- [Winkelstein et al. 2000, national registry of 368 patients (PMID 10844935)](https://pubmed.ncbi.nlm.nih.gov/10844935/)
- [Kuhns et al. 2010, Residual NADPH Oxidase and Survival (NEJM; PMID 21190454)](https://pubmed.ncbi.nlm.nih.gov/21190454/)
- [Kohn et al. 2020, Lentiviral gene therapy for X-linked CGD (Nat Med)](https://www.nature.com/articles/s41591-019-0735-5)
- [Gallin et al., Itraconazole prophylaxis (NEJM)](https://www.nejm.org/doi/full/10.1056/NEJMoa021931)
- [CGD: why an inflammatory disease? (PMC4230281)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4230281/)
- [CGD with IBD — USIDNET Registry (PMC9086117)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9086117/)
- [Hematopoietic cell transplantation in CGD: 712 children and adults (Blood 2020)](https://ashpublications.org/blood/article/136/10/1201/461262/)
- [Orphanet: Chronic granulomatous disease (ORPHA:379)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=379)
- [CGD: Commonly Associated Pathogens, Diagnosis and Treatment (PMC10534792)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10534792/)
- [MedlinePlus Genetics: Chronic granulomatous disease](https://medlineplus.gov/genetics/condition/chronic-granulomatous-disease/)

---

**Bottom line:** CGD is a monogenic phagocyte NADPH-oxidase defect — the cell can swallow the bug but can't light the oxidative match — producing the twin signatures of *recurrent catalase-positive infections* and *paradoxical granulomatous hyperinflammation*. It's genetically well-mapped (six genes, X-linked CYBB dominant), functionally diagnosable (DHR flow), medically manageable (co-trimoxazole + itraconazole + IFN-γ), and increasingly curable (HSCT ~90% survival; lentiviral gene therapy maturing). Residual oxidase activity is the master dial for severity and survival. Remember: **fetch and validate every PMID snippet and ontology ID before writing them into the YAML.**