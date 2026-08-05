---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-29T11:14:16.108445'
end_time: '2026-06-29T11:19:50.469889'
duration_seconds: 334.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Anti-Glomerular Basement Membrane Disease
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
  web_search_requests: 9
  num_turns: 20
  total_cost_usd: 2.650466
  session_id: 0690b46f-a3fd-43bb-a803-8736ca5e8646
  stop_reason: end_turn
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anti-Glomerular Basement Membrane Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Anti-Glomerular Basement Membrane Disease** covering all of the
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

I now have well-verified, richly sourced material. Writing the comprehensive report.

---

# Comprehensive Research Report: Anti–Glomerular Basement Membrane (Anti-GBM) Disease

**Prepared:** 2026-06-29 · **Category:** Complex (organ-specific autoimmune) · **Primary MONDO:** MONDO:0009303

> **Verification note for KB curation:** PMIDs below marked ✔ were directly confirmed against PubMed/publisher abstracts during this research. PMIDs marked ⚠ are well-known landmark papers cited from secondary search results — re-fetch with `just fetch-reference PMID:XXXX` and confirm the exact snippet before committing any of them as evidence. Per the dismech anti-hallucination SOP, no snippet below should be pasted into YAML without substring-verifying it against the freshly fetched abstract.

---

## 1. Disease Information

**Overview.** Anti-glomerular basement membrane (anti-GBM) disease is a rare, organ-specific autoimmune small-vessel vasculitis caused by circulating autoantibodies (predominantly IgG) directed against the non-collagenous-1 (NC1) domain of the α3 chain of type IV collagen — the "Goodpasture antigen" — which is expressed in the specialized basement membranes of the renal glomerulus and pulmonary alveolus. The classic presentation is a **pulmonary–renal syndrome**: rapidly progressive (crescentic) glomerulonephritis (RPGN) together with diffuse alveolar hemorrhage (DAH). When both organs are involved the term **Goodpasture syndrome/disease** is traditionally used; isolated renal-limited or (rarely) lung-limited forms also occur.

**Key identifiers.**
- **MONDO:** MONDO:0009303 (anti-glomerular basement membrane disease)
- **OMIM:** 233450 (GOODPASTURE SYNDROME) ✔
- **Orphanet:** ORPHA:375 (Anti-glomerular basement membrane disease / Goodpasture syndrome)
- **ICD-10:** M31.0 (Hypersensitivity angiitis – Goodpasture syndrome); **ICD-11:** 4A44.A0 / GB61 cross-mapped
- **MeSH:** D019867 "Anti-Glomerular Basement Membrane Disease"
- **UMLS/SNOMED CT:** 236519009 (Anti-glomerular basement membrane disease)

**Synonyms / alternative names.** Goodpasture syndrome; Goodpasture disease; anti-GBM antibody disease; anti-basement-membrane antibody disease; pulmonary–renal syndrome (descriptive, not specific). The eponym honors Ernest Goodpasture, who described a fatal case during the 1919 influenza pandemic.

**Data derivation.** This entry is built from **aggregated disease-level resources** (systematic reviews/meta-analyses, single-center cohort series, mechanistic biochemistry) rather than individual EHR patients — appropriate given the disease's rarity.

---

## 2. Etiology

### Causal mechanism
Anti-GBM disease is fundamentally an **autoantibody-mediated (Type II hypersensitivity) conformeropathy**. The proximate cause is the breakdown of immune tolerance to the α3(IV)NC1 domain, generating high-affinity IgG that binds basement-membrane antigen and triggers complement- and neutrophil-mediated necrotizing injury. It is not a Mendelian disease; it arises from a strong genetic susceptibility background acted on by an environmental "second hit."

### Genetic risk factors
- **HLA-DRB1\*15:01 (DR15 haplotype)** is the dominant susceptibility allele. It is "found in more than 80% of patients with anti-GBM antibody disease" (Medscape/Phelps & Rees ⚠ PMID:10231356). DRB1\*15:01 and DRB1\*04 are positively associated.
- **Susceptibility loci:** Phelps & Rees (Kidney Int 1999 ⚠ PMID:10231356) established the HLA-DRB1 dominance hierarchy of risk.

### Genetic protective factors
- **HLA-DRB1\*07:01** (and DRB1\*01) confer **dominant protection**: "individuals inheriting DRB1\*1501 and DRB1\*0701 have no higher risk of disease than does the general population" (Medscape synthesis of Phelps & Rees ⚠).

### Environmental / acquired risk factors ("second hits" that expose the cryptic antigen)
- **Cigarette smoking** — strongly associated, especially with the pulmonary-hemorrhage phenotype.
- **Hydrocarbon / organic-solvent inhalation** — classic occupational/inhalational trigger (case literature, e.g., Egyptian J Bronchol 2026).
- **Pulmonary infection** (viral respiratory infections, influenza historically).
- **Extracorporeal shock-wave lithotripsy** — "can disrupt the glomerular basement membrane and unmask epitopes" (Merck Manual / CJASN review).
- **Alemtuzumab (anti-CD52)** — lymphocyte-depleting therapy; "loss of regulatory T cell subsets, or abnormal immune cell repopulation after depletion" (PMC7573726 ⚠).
- **Membranous nephropathy and ANCA-associated vasculitis** can precede or co-occur, "unmasking" GBM antigen.
- **Age/sex:** bimodal age peaks (young men 20–30; older adults 60–70, more women).

**Gene–environment interaction.** The canonical model: an HLA-DRB1\*15:01–restricted CD4⁺ T-cell response to α3(IV)NC1 epitopes provides help for autoantibody production, but disease only manifests when an environmental insult (smoke, hydrocarbons, infection, lithotripsy) perturbs the GBM and exposes the normally sequestered cryptic epitopes — converting subclinical autoreactivity into overt injury.

---

## 3. Phenotypes

| Phenotype | Type | HPO suggestion | Frequency | Notes |
|---|---|---|---|---|
| Rapidly progressive (crescentic) glomerulonephritis | Lab/clinical sign | **HP:0000099** Glomerulonephritis; **HP:0012622** Chronic kidney disease | ~Most renal cases | Acute, often dialysis-requiring |
| Diffuse alveolar / pulmonary hemorrhage | Clinical sign | **HP:0040223** Pulmonary hemorrhage; **HP:0002105** Hemoptysis | **32.6%** (meta-analysis ✔ PMID:38493958) | Smoking-associated |
| Hematuria | Lab abnormality | **HP:0000790** Hematuria | Very frequent | Glomerular (dysmorphic RBC, casts) |
| Proteinuria (usually sub-nephrotic) | Lab abnormality | **HP:0000093** Proteinuria | Frequent | |
| Acute kidney injury / oliguria | Clinical sign | **HP:0001919** Acute kidney injury; **HP:0100518** Dysuria/oliguria (use HP:0100626 Oliguria) | Frequent | Strong prognostic marker |
| Elevated serum creatinine / azotemia | Lab abnormality | **HP:0003259** Elevated circulating creatinine | Frequent | Baseline value is key prognosticator |
| Dyspnea / respiratory failure | Symptom | **HP:0002094** Dyspnea | Common in pulmonary cases | |
| Iron-deficiency / hemorrhagic anemia | Lab abnormality | **HP:0001891** Iron deficiency anemia; **HP:0001903** Anemia | Common | From alveolar bleeding |
| Hypertension | Clinical sign | **HP:0000822** Hypertension | Variable | Less prominent than in other GN |
| Constitutional (malaise, fatigue, weight loss, fever) | Symptoms | **HP:0012378** Fatigue; **HP:0001824** Weight loss | Common prodrome | |

**Characteristics.** Onset is typically **acute/subacute** in adults; the disease is **monophasic** in classic single-positive cases (relapse <3%). Severity is **severe** and often organ-threatening at presentation. Pulmonary hemorrhage can be immediately life-threatening; renal disease frequently progresses to end-stage within days–weeks if untreated.

**Quality-of-life impact.** Survivors who reach ESRD face lifelong dialysis or transplantation; pulmonary survivors generally recover lung function. No disease-specific QoL instrument exists; generic CKD/dialysis QoL measures (KDQOL, EQ-5D, SF-36) apply.

---

## 4. Genetic / Molecular Information

**This is NOT a monogenic disease** — there are no causal germline mutations. The "molecular genetics" is the genetics of the **autoantigen** and of **HLA susceptibility**.

- **Autoantigen gene:** **COL4A3** (HGNC:2204; chromosome 2q36.3), encoding the α3 chain of type IV collagen. Its C-terminal **NC1 domain (α3(IV)NC1)** is the Goodpasture antigen. The collateral chains **COL4A4** (HGNC:2205) and **COL4A5** (HGNC:2207, Xq22.3) form the α3α4α5(IV) network.
- **Susceptibility "gene":** HLA class II — **HLA-DRB1** (HGNC:4948), allele DRB1\*15:01.
- **No pathogenic somatic variants, copy-number, or chromosomal abnormalities** are implicated in pathogenesis. (Conversely, *loss-of-function* mutations in COL4A3/4/5 cause **Alport syndrome** — and transplanted Alport patients can develop *de novo* anti-GBM antibodies against the newly encountered α3/α5(IV) antigen, the converse experiment of nature.)
- **Functional consequence:** The disease results from a **conformational change**, not a sequence change — see Mechanism.

**Epigenetics / molecular profiling.** No established disease-specific methylation/histone signature. Transcriptomic/proteomic profiling is largely confined to research cohorts; no validated multi-omics diagnostic exists.

---

## 5. Environmental Information

- **Toxins / inhalational:** organic solvents and **hydrocarbons** (gasoline, paint thinners); **cigarette smoke** is the best-established lifestyle exposure and disproportionately drives the alveolar-hemorrhage phenotype.
- **Mechanical:** extracorporeal shock-wave **lithotripsy** (GBM disruption).
- **Iatrogenic:** **alemtuzumab** and other lymphocyte-depleting agents.
- **Infectious agents:** respiratory **viral infections** (historically influenza — Goodpasture's index 1919 case); no single pathogen is causal. Infection is regarded as a nonspecific trigger/adjuvant rather than an etiologic organism.

---

## 6. Mechanism / Pathophysiology

This is the mechanistic core and the best-characterized aspect of the disease — a model "autoimmune conformeropathy."

### Step 1 — The sequestered/cryptic autoantigen and its "immune privilege"
The Goodpasture antigen is the **C-terminal NC1 domain of α3(IV) collagen**, identified by Saus, Hudson and colleagues as the common target of anti-basement-membrane antibodies (✔ PMID:8589284):
> *"Reactivity to alpha 3(IV) NC1 domains is both sufficient and necessary for the expression of autoimmune disease directed to the NC1 domain of Type IV collagen."*

In the mature GBM, six NC1 domains associate into an **α3α4α5 NC1 hexamer** (two trimeric "caps" joined head-to-head). The two immunodominant epitopes — **E_A and E_B**, located on α3(IV)NC1 — are buried by **intraprotomer interactions with α4 and α5 NC1 domains** and locked by novel **sulfilimine (S=N) crosslinks** discovered by Vanacore et al. (Science 2009 ⚠ PMID:19729652). These crosslinks "confer immune privilege to the Goodpasture autoantigen" by structurally sequestering the cryptic epitopes.

### Step 2 — Conformational unmasking (the "conformeropathy")
Pedchenko et al. (NEJM 2010 ⚠ PMID:20660402, *Molecular Architecture of the Goodpasture Autoantigen in Anti-GBM Nephritis*) showed that:
> *"the autoantibodies bind neoepitopes formed on α3 and α5 NC1 subunits upon disruption of the quaternary structure of the native α345NC1 hexamer, and hexamer disruption is concomitant with conformational changes that transition subunits into immunogens."*

An environmental insult (oxidants from smoke, infection, mechanical disruption) dissociates the hexamer, **exposing E_A/E_B**. Autoantibodies to the **α5(IV)NC1** chain are also pathogenic, defining a broader α3/α5 conformeropathy (Pedchenko 2016 ⚠, PMC5600521).

### Step 3 — Loss of tolerance and antibody production
An **HLA-DRB1\*15:01–restricted CD4⁺ T-cell response** to α3(IV)NC1 peptides drives B-cell help; **B cells (CL:0000236)** differentiate into plasma cells producing high-affinity, complement-fixing **IgG1/IgG3** anti-GBM antibodies. The autoantibody titer correlates with disease activity.

### Step 4 — Antibody binding, complement activation, effector recruitment
Circulating IgG binds the exposed α3(IV)NC1 along the GBM in a **linear, ribbon-like** immunofluorescence pattern. This activates the **classical complement pathway** (C3, C5a), generating chemoattractants that recruit **neutrophils (CL:0000775)** and **monocytes/macrophages (CL:0000235)**. Effector cells release proteases and reactive oxygen species, producing **fibrinoid necrosis** of capillary loops.

### Step 5 — Crescent formation and tissue destruction
GBM rupture permits fibrin and inflammatory cells into Bowman's space, triggering **parietal epithelial and podocyte proliferation → cellular crescents → crescentic (extracapillary) glomerulonephritis**. In the lung, alveolar capillary basement-membrane injury causes **diffuse alveolar hemorrhage**. Smoking increases alveolar antigen accessibility, explaining the smoking–lung-hemorrhage link.

### Causal chain (upstream → downstream)
HLA-DRB1\*15:01 susceptibility + environmental insult → hexamer dissociation/oxidation → exposure of cryptic E_A/E_B on α3/α5(IV)NC1 → T-cell-dependent anti-GBM IgG production → linear GBM antibody deposition → classical complement activation + neutrophil recruitment → capillary fibrinoid necrosis → crescentic GN (kidney) and alveolar hemorrhage (lung) → RPGN/ESRD and respiratory failure.

### Ontology suggestions
- **Biological processes (GO):** GO:0006956 complement activation; GO:0006958 complement activation, classical pathway; GO:0002455 humoral immune response mediated by circulating immunoglobulin; GO:0050900 leukocyte migration; GO:0006954 inflammatory response; GO:0002544 chronic inflammation; GO:0030198 extracellular matrix organization.
- **Cell types (CL):** CL:0000236 B cell; CL:0000775 neutrophil; CL:0000235 macrophage; CL:0000084 T cell; CL:1000746 glomerular visceral epithelial cell (podocyte); CL:1000698 kidney resident parietal epithelial cell (crescent precursor).
- **Pathways:** Reactome R-HSA-2559639 (Collagen type IV sulfilimine cross-linking by peroxidasin); Reactome complement cascade R-HSA-166658.
- **Protein dysfunction:** No protein misfolding mutation — pathology is a **quaternary conformational change** exposing cryptic epitopes (a structural neoepitope phenomenon).

---

## 7. Anatomical Structures Affected

- **Primary organs:** **Kidney** (UBERON:0002113) — specifically the **renal glomerulus** (UBERON:0000074) and **glomerular basement membrane** (UBERON:0002164); **Lung** (UBERON:0002048) — **pulmonary alveolus** (UBERON:0002299) and alveolar basement membrane.
- **Body systems:** renal/urinary and respiratory; secondarily hematologic (hemorrhagic anemia).
- **Tissue/cell level:** glomerular capillary endothelium and podocytes; alveolar capillary endothelium/type I pneumocytes; the target is the **specialized type IV collagen network** of these basement membranes (α3α4α5, restricted to GBM, alveolus, cochlea, eye, testis — explaining organ selectivity).
- **Subcellular (GO Cellular Component):** GO:0005604 basement membrane; GO:0005581 collagen trimer; GO:0005615 extracellular space.
- **Lateralization:** **bilateral** (both kidneys, both lungs) — diffuse, antigen-driven.

---

## 8. Temporal Development

- **Onset:** **acute/subacute** in adults; **bimodal age distribution** — a peak in **young men (20–30 yr, often with pulmonary–renal disease)** and a second in **older adults (60–70 yr, more women, often renal-limited)**.
- **Progression:** characteristically **rapidly progressive** — kidney function can decline from normal to dialysis-dependence over days. Untreated, prognosis is dismal.
- **Course pattern:** classic single-positive disease is **monophasic** (one episode, no relapse if antibody is cleared). Relapse is **<3%** (NDT treatment-standard review ✔). **Double-positive (anti-GBM + ANCA)** patients behave more like ANCA-associated vasculitis with **relapsing-remitting** disease (~50% relapse).
- **Critical window:** the **therapeutic window is extremely narrow** — outcomes hinge on starting plasma exchange/immunosuppression before oliguria/dialysis dependence is established. Patients dialysis-dependent **>7 days before treatment "very rarely recover independent kidney function."**

---

## 9. Inheritance and Population

### Epidemiology (✔ systematic review/meta-analysis, PMID:38493958 — 47 studies, 2,830 patients)
- **Incidence:** *"The overall incidence of anti-GBM disease ranged from 0.60 to 1.79 per million population per annum."* (≈0.5–1 case/million/year is the commonly quoted figure.)
- Anti-GBM accounts for **~8.0%** of rapidly progressive GN and **~12.8%** of crescentic GN cases (pooled).
- **Anti-GBM antibody positivity:** 88.8%; **ANCA co-positivity (double-positive):** 27.4%; **pulmonary hemorrhage:** 32.6%.

### Inheritance
- **Not Mendelian** — complex/multifactorial with strong HLA association. No vertical inheritance pattern, no penetrance/expressivity/anticipation/mosaicism/founder-effect parameters apply in the classic genetic sense.
- Rare **familial clustering in HLA-identical siblings** is reported (Clin Kidney J 2020), consistent with shared HLA-DR15 susceptibility rather than a transmitted causal variant.

### Demographics
- **Sex:** historically male predominance (~3:2) overall, but the older renal-limited peak skews female.
- **Ethnicity:** *"reported in all racial groups but is primarily a disease of white populations,"* with ~83% of race-identified cases in white individuals; relatively more common in those of European and East Asian descent. HLA-DRB1\*15:01 frequency shapes geographic risk.
- **Geographic clustering / seasonality:** small temporal/geographic clusters reported (e.g., post-infection clusters; a noted rise during the COVID-19 pandemic period in Madrid, PMC12457157 ⚠).

---

## 10. Diagnostics

### Serology (cornerstone)
- **Circulating anti-GBM antibodies** by **ELISA** (anti-α3(IV)NC1) — high sensitivity/specificity; titer tracks activity. LOINC examples: LOINC:40663-6 (Glomerular basement membrane Ab [Units/vol] in Serum by Immunoassay).
- **ANCA panel (MPO/PR3)** — must be tested in *every* patient: **~27–40% are double-positive**, which changes prognosis and maintenance therapy.

### Histopathology (definitive)
- **Renal biopsy:** diffuse **crescentic glomerulonephritis** on light microscopy; the pathognomonic finding is **linear (ribbon-like) IgG deposition along the GBM** on **direct immunofluorescence** (often with linear C3). Quantifying **% crescents** and **% globally sclerosed glomeruli** is essential for prognosis.
- **Lung:** capillaritis with hemorrhage; hemosiderin-laden macrophages on BAL.

### Supporting laboratory / functional
- Urinalysis: dysmorphic hematuria, RBC casts, sub-nephrotic proteinuria; rising creatinine/falling GFR.
- Anemia (hemorrhagic/iron-deficiency).
- **Imaging:** chest CT/X-ray showing bilateral alveolar infiltrates (RadLex); **DLCO is paradoxically increased** during active alveolar hemorrhage (a useful functional clue).
- **Genetic testing:** **not diagnostic** (no causal gene). HLA typing is research/risk-stratification only.

### Differential diagnosis
ANCA-associated vasculitis (GPA/MPA), lupus nephritis, other causes of pulmonary–renal syndrome, IgA/IgA-vasculitis nephritis, thrombotic microangiopathy, and (importantly) **double-positive anti-GBM/ANCA disease**. Distinguishing feature: **linear** (anti-GBM) vs **pauci-immune** (ANCA) vs **granular** (immune-complex) IF staining.

---

## 11. Outcome / Prognosis

### Survival (✔ meta-analysis PMID:38493958)
- **1-year patient survival: 76.2%**; **1-year kidney survival: 30.2%.**

### Landmark prognostic cohort (Levy et al., Ann Intern Med 2001 ⚠ PMID:11712875; n=71, plasma exchange + prednisolone + cyclophosphamide)
- Patients presenting with **creatinine <500 µmol/L (<5.7 mg/dL):** ~**100% patient and 95% renal survival at 1 year** (84%/74% longer-term).
- Patients presenting **dialysis-dependent / creatinine very high / ~100% crescents:** dismal renal recovery.

### Strongest prognostic factors
1. **Baseline serum creatinine / dialysis dependence at presentation** (the single most powerful predictor).
2. **Oliguria.**
3. **Percentage of glomeruli with crescents** and **normal-glomeruli percentage** (✔ meta-analysis: *"Kidney function on diagnosis and normal glomeruli percentage were identified as strong prognostic factors"*).
4. Time from symptom onset to treatment.

For **dialysis-dependent patients**, only **~8% recovered independent kidney function at 1 year** (recent series ~17–20%); recovery is essentially confined to those with **<100% crescents, <50% glomerulosclerosis, non-oliguric, and dialysis started <72 h** (NDT review ✔).

### Disease course / complications
- Pulmonary hemorrhage: high remission with treatment (**90–100%**) but acutely life-threatening.
- Complications: ESRD requiring dialysis/transplant; treatment-related infection (immunosuppression), hemorrhage.
- **Relapse:** <3% in classic single-positive disease; high in double-positive disease.

---

## 12. Treatment

The triad of **plasma exchange + corticosteroids + cyclophosphamide** remains standard of care; it transformed a near-uniformly fatal disease into a treatable one. Specifics below are from the 2026 NDT treatment-standard review (✔).

### Standard induction
- **Plasma exchange (PLEX) — MAXO:0000548 (therapeutic plasmapheresis) / NCIT:C15304 (Plasmapheresis):** *"Daily 40–60 mL/kg exchange for 5% human albumin solution"* until antibody fully suppressed, *"typically 14 days."* Removes circulating pathogenic IgG. (Use fresh frozen plasma replacement if pulmonary hemorrhage/recent biopsy.)
- **Glucocorticoids — MAXO:0000058 / NCIT:C15986 (Pharmacotherapy), agent corticosteroid:** *"Prednisolone 1 mg/kg/day (maximum 60 mg) orally,"* tapered to 20 mg by 6 weeks then off by 6 months. Suppresses inflammation.
- **Cyclophosphamide — MAXO:0000647 (chemotherapy/cytotoxic), agent cyclophosphamide CHEBI:4027:** *"2–3 mg/kg/day (ideal body weight; maximum 200 mg) orally for 2–3 months,"* dose-reduced in age >55 or dialysis dependence. Suppresses new autoantibody production.

### Emerging / alternative agents
- **Rituximab (anti-CD20, B-cell depletion; NCIT:C1702):** *"2× 1 g at day 0 and 14 OR 375 mg/m² weekly ×4"*; used when cyclophosphamide is contraindicated or in refractory disease. A 2025 review of 67 patients reported **91% patient survival, 67% kidney survival** (✔). Evidence base remains limited.
- **Imlifidase (IdeS, IgG-degrading enzyme of *S. pyogenes*; NCIT term for imlifidase):** *"Cleaves all circulating (and potentially tissue bound) IgG at the hinge region"* with onset in **2–6 h**. Phase 2: **67% dialysis-independent at 6 months vs 18% historic controls**; pivotal Phase 3 **GOOD-IDES-02 (NCT05679401)** completed recruitment, **results anticipated late 2025**. Dose 0.25–0.5 mg/kg single dose. *Potential paradigm shift for rapid antibody clearance.*

### Treatment-decision rules
- **Treat pulmonary hemorrhage aggressively regardless of renal status:** *"Treatment is always recommended when alveolar haemorrhage is present, regardless of the presence or severity of kidney disease."*
- **Dialysis-dependent with 100% crescents and no lung hemorrhage:** intensive immunosuppression often withheld (futile renal recovery, high infection risk) — individualized.

### Supportive / prophylactic care
*Pneumocystis jirovecii* prophylaxis, antifungal and peptic-ulcer prophylaxis, osteoporosis prevention during high-dose steroids/cyclophosphamide. **MAXO:0000950** (supportive care).

### Maintenance & transplantation
- **Classic single-positive disease:** maintenance immunosuppression **not routinely required** (monophasic).
- **Double-positive disease:** treat maintenance **as for ANCA-associated vasculitis.**
- **Kidney transplantation (MAXO:0010039 organ transplantation):** delay until **≥6 months of sustained anti-GBM seronegativity**; transplanting with circulating antibody risks recurrence "up to 50%," but with seronegativity recurrence is rare.

### Pharmacogenomics
No validated PGx markers specific to anti-GBM; standard cyclophosphamide considerations (gonadal toxicity, fertility preservation counseling) apply.

---

## 13. Prevention

- **Primary prevention:** no vaccine/screening (rare, sporadic). Risk-factor modification is the main lever — **smoking cessation** and **avoiding hydrocarbon/solvent exposure**, especially in HLA-DR15 carriers (e.g., after lithotripsy or in Alport transplant recipients).
- **Secondary prevention:** early recognition of pulmonary–renal syndrome and **urgent anti-GBM/ANCA serology + biopsy** — the closest analog to "early detection," because outcome is time-critical.
- **Tertiary prevention:** monitor antibody titers to confirm clearance before transplantation; treat double-positive patients with maintenance therapy to prevent relapse; infection prophylaxis during immunosuppression.
- **Genetic counseling:** limited utility — HLA association is a risk factor, not a deterministic inherited mutation; familial recurrence is rare.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** primarily a **human** disease (NCBITaxon:9606).
- **Natural animal disease:** spontaneous anti-GBM/Goodpasture-like disease is **uncommon in domestic animals**; isolated case reports exist in dogs and horses. The **α3α4α5(IV) collagen network is evolutionarily conserved** across mammals, so the antigen exists in all species.
- **Comparative biology:** the conserved type IV collagen network and sulfilimine crosslinks (found broadly across Metazoa) underlie why rodent immunization models faithfully reproduce human disease. **Orthologs:** mouse *Col4a3*, *Col4a4*, *Col4a5*.
- **Zoonosis:** none — autoimmune, not transmissible.

---

## 15. Model Organisms

- **Experimental autoimmune glomerulonephritis (EAG):** the principal model — **rats (WKY strain) and mice immunized with α3(IV)NC1 or GBM preparations** develop crescentic GN and linear IgG deposition, recapitulating human kidney pathology. Used to define T-cell epitopes and HLA-restricted responses.
- **Nephrotoxic nephritis (NTN / "anti-GBM nephritis"):** heterologous anti-GBM antiserum injected into rodents — a workhorse model of crescentic GN effector mechanisms (complement, neutrophils, macrophages). *Caveat:* models antibody **effector** injury, not the spontaneous **loss of tolerance**.
- **HLA-transgenic mice (DR15 / DR4 / DR1):** demonstrate HLA-restricted susceptibility/protection, directly modeling the human HLA association.
- **Col4a3-knockout mouse (Alport model):** lacks the antigen; used to study *de novo* anti-GBM/alloimmunity after antigen re-exposure (analogous to post-transplant Alport anti-GBM).
- **Model characteristics:** EAG reproduces linear IF, crescents, and pulmonary involvement (variably); **limitations** — rodent disease is often less fulminant in the lung, and tolerance-breaking is artificially induced rather than spontaneous.
- **Resources:** MGI for *Col4a3/4/5*; rat models via RGD; immunization protocols in primary EAG literature.

---

## Key References (verify PMIDs before KB ingestion)

1. ✔ Hellmark/Saus/Hudson et al. *Identification of the α3 chain of type IV collagen as the common autoantigen in anti-basement-membrane disease and Goodpasture syndrome.* **PMID:8589284.** — *"Reactivity to alpha 3(IV) NC1 domains is both sufficient and necessary…"*
2. ⚠ Pedchenko V, et al. *Molecular Architecture of the Goodpasture Autoantigen in Anti-GBM Nephritis.* N Engl J Med 2010;363:343–354. **PMID:20660402.** — conformeropathy / neoepitope mechanism.
3. ⚠ Vanacore R, et al. *A sulfilimine bond identified in collagen IV.* Science 2009;325:1230–1234. **PMID:19729652.** — immune-privilege crosslink (PMC2876822).
4. ✔ Systematic review & meta-analysis (47 studies, 2,830 patients). **PMID:38493958.** — incidence 0.60–1.79/million/yr; 1-yr patient survival 76.2%, kidney survival 30.2%; pulmonary hemorrhage 32.6%; ANCA 27.4%.
5. ⚠ Levy JB, et al. *Long-term outcome of anti-GBM antibody disease treated with plasma exchange and immunosuppression.* Ann Intern Med 2001;134:1033. **PMID:11712875.** — creatinine-stratified prognosis.
6. ✔ Levy JB, et al. *Clinical features and outcome of patients with both ANCA and anti-GBM antibodies.* Kidney Int 2004. **PMID:15458448.**
7. ✔ McAdoo SP, et al. *Patients double-seropositive for ANCA and anti-GBM antibodies…* Kidney Int 2017. **PMID:28506760.**
8. ⚠ McAdoo SP, Pusey CD. *Anti-Glomerular Basement Membrane Disease.* Clin J Am Soc Nephrol 2017;12:1162. **PMID:28515156** (review).
9. ⚠ Phelps RG, Rees AJ. *The HLA complex in Goodpasture's disease.* Kidney Int 1999. **PMID:10231356** — DRB1\*15:01 risk, DRB1\*07:01 protection.
10. ⚠ Anti-GBM disease — treatment standard. Nephrol Dial Transplant 2026;41:42. — regimen, rituximab, imlifidase/GOOD-IDES-02 (NCT05679401).

**Sources (URLs):**
- [PubMed 8589284 — α3(IV) autoantigen](https://pubmed.ncbi.nlm.nih.gov/8589284/)
- [NEJM — Molecular Architecture of the Goodpasture Autoantigen (Pedchenko 2010)](https://www.nejm.org/doi/full/10.1056/NEJMoa0910500)
- [Antibodies to α5(IV) are pathogenic — PMC5600521](https://pmc.ncbi.nlm.nih.gov/articles/PMC5600521/)
- [PubMed 38493958 — Epidemiology/outcomes systematic review & meta-analysis](https://pubmed.ncbi.nlm.nih.gov/38493958/)
- [Levy 2001 — Ann Intern Med long-term outcome](https://www.acpjournals.org/doi/10.7326/0003-4819-134-11-200106050-00009)
- [PubMed 15458448 — ANCA + anti-GBM double-positive (Levy 2004)](https://pubmed.ncbi.nlm.nih.gov/15458448/)
- [PubMed 28506760 — double-seropositive renal survival/relapse (McAdoo 2017)](https://pubmed.ncbi.nlm.nih.gov/28506760/)
- [CJASN 2017 — McAdoo & Pusey review](https://journals.lww.com/CJASN/pages/articleviewer.aspx?year=2017&issue=07000&article=00018&type=Fulltext)
- [NDT 2026 — Anti-GBM disease treatment standard](https://academic.oup.com/ndt/article/41/1/42/8257581)
- [HLA-DRB1 susceptibility — ScienceDirect/Kidney Int](https://www.sciencedirect.com/science/article/pii/S0085253815598591)
- [Medscape — Anti-GBM Antibody Disease (HLA, demographics)](https://emedicine.medscape.com/article/981258-overview)
- [Merck Manual — Anti-GBM Disease (triggers)](https://www.merckmanuals.com/professional/pulmonary-disorders/diffuse-alveolar-hemorrhage-and-pulmonary-renal-syndrome/anti-glomerular-basement-membrane-anti-gbm-disease)
- [Vanacore 2009 Science — sulfilimine bond (PMC2876822)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2876822/)
- [Goodpasture conformeropathy review — PMC6482832](https://pmc.ncbi.nlm.nih.gov/articles/PMC6482832/)
- [Alemtuzumab-related anti-GBM — PMC7573726](https://pmc.ncbi.nlm.nih.gov/articles/PMC7573726/)
- [OMIM 233450 — Goodpasture syndrome](https://www.omim.org/entry/233450)

---

### Summary for KB population
The existing `kb/disorders/Anti-GBM_Disease.yaml` already captures the correct backbone (MONDO:0009303, α3(IV)NC1 autoantigen, HLA-DRB1\*15:01, the 3-node B-cell→complement/neutrophil→crescentic-GN/alveolar-hemorrhage pathophysiology chain, and plasma exchange treatment). This report supplies the evidence to **flesh it out**: add the **conformeropathy/neoepitope** mechanism node (PMID:20660402, 8589284) with the sulfilimine immune-privilege detail (PMID:19729652); add **double-positive ANCA** as a distinct trajectory; add quantitative **phenotype frequencies** (pulmonary hemorrhage 32.6%) and **outcomes** (1-yr survival 76.2%/30.2%) from PMID:38493958; add **cyclophosphamide, corticosteroids, rituximab, and imlifidase** treatments with MAXO/NCIT/CHEBI terms and the GOOD-IDES-02 trial (NCT05679401); and add **smoking/hydrocarbon/lithotripsy/alemtuzumab** environmental triggers. Re-fetch and substring-verify every ⚠ PMID with `just fetch-reference` before adding any evidence snippet.