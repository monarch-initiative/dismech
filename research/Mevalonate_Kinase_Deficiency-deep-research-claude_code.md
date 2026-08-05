---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-29T22:11:31.296737'
end_time: '2026-06-29T22:16:14.279367'
duration_seconds: 282.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mevalonate Kinase Deficiency
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
  num_turns: 12
  total_cost_usd: 2.2670969999999997
  session_id: d1aa2bff-b1bb-4cd6-ad75-4fcc05203e23
  stop_reason: end_turn
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mevalonate Kinase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mevalonate Kinase Deficiency** covering all of the
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

I now have comprehensive data. Here is the full research report.

---

# Research Report: Mevalonate Kinase Deficiency (MKD)

**Prepared:** 2026-06-29 · **Category:** Mendelian (autosomal recessive inborn error of metabolism / monogenic autoinflammatory disorder)

A note up front on framing: MKD is best modeled as a **single-gene disease with a severity continuum**, not two diseases. Historically it was split into two clinical phenotypes — the milder **hyperimmunoglobulinemia D and periodic fever syndrome (HIDS)** and the severe **mevalonic aciduria (MVA)** — but the 1999 discovery that both arise from biallelic *MVK* variants reframed them as the two poles of one enzymatic-deficiency spectrum. The 2024 SHARE-revision consensus now prefers the terms **"mild MKD"** (formerly HIDS) and **"severe MKD"** (formerly MVA). Think of it like a dimmer switch on residual enzyme activity rather than two separate light fixtures. ([Houten et al. 2006, PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/); [Politiek & Waterham 2024 SHARE update, PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

---

## 1. Disease Information

**Overview.** MKD is an autosomal recessive disorder caused by deficient activity of **mevalonate kinase (MK)**, the first committed enzyme downstream of HMG-CoA reductase in the **mevalonate/isoprenoid biosynthesis pathway**. The block in this pathway produces a shortage of non-sterol isoprenoids (especially geranylgeranyl pyrophosphate), which impairs protein prenylation and triggers episodes of systemic hyperinflammation driven by interleukin-1β (IL-1β). Severity tracks with residual enzyme activity. ([PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/); [PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

> "Mevalonic aciduria (MVA) and hyperimmunoglobulinemia D syndrome (HIDS) represent the two ends of a clinical spectrum of disease caused by deficiency of mevalonate kinase (MVK), the first committed enzyme of cholesterol biosynthesis." ([PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/))

**Key identifiers.**
- **Gene:** *MVK*, locus **12q24.11**. OMIM gene: **251170**. HGNC: **HGNC:7530** (`hgnc:7530`).
- **OMIM phenotype — HIDS / mild MKD:** **260920** (Hyperimmunoglobulinemia D and periodic fever syndrome; "periodic fever, Dutch type"). ⚠️ *Note: some sources list 260920; verify against current OMIM.*
- **OMIM phenotype — Mevalonic aciduria / severe MKD:** **610377**.
- **Orphanet:** Mevalonate kinase deficiency (umbrella) **ORPHA:309025**; HIDS **ORPHA:343**; Mevalonic aciduria **ORPHA:29**. ⚠️ *Verify ORPHA codes against current Orphadata before committing as `ORPHA:` evidence.*
- **MONDO:** Mevalonate kinase deficiency commonly **MONDO:0018997**; mevalonic aciduria **MONDO:0009639**; HIDS **MONDO:0009358**. ⚠️ *These MONDO IDs must be verified with `runoak -i sqlite:obo:mondo info ...` before use — do not trust them as-quoted.*
- **ICD-11:** typically coded under periodic fever syndromes (4A60.2 area, "Mevalonate kinase deficiency"). ⚠️ *Verify.*
- **MeSH:** "Mevalonate Kinase Deficiency" (also indexed under hyper-IgD; D000093173 / related entries — verify).

**Synonyms / alternative names:** Mevalonate kinase deficiency (MKD); Hyper-IgD syndrome (HIDS); Hyperimmunoglobulinemia D and periodic fever syndrome; Periodic fever, Dutch type; Mevalonic aciduria (MVA); MK deficiency. ([NORD](https://rarediseases.org/rare-diseases/hyper-igd-syndrome/); [MedlinePlus](https://medlineplus.gov/genetics/condition/mevalonate-kinase-deficiency/))

**Data derivation:** Information is from **aggregated disease-level resources** (OMIM, Orphanet, the International HIDS Database, the Eurofever registry, and published cohort/natural-history studies) rather than individual EHR data.

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound heterozygous) loss-of-function/hypomorphic variants in ***MVK*** reduce mevalonate kinase activity. The disease is a **direct enzymatic deficiency**; there is no environmental cause, though environmental factors *trigger flares* (see below). ([PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/))

> "A reduced activity of MVK and pathogenic mutations in the MVK gene have been demonstrated as the common genetic basis in both disorders. The severity of the disease is linked with the residual activity of the enzyme." ([PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/))

**Genetic risk factors.** Being a carrier of two *MVK* pathogenic alleles is causal (not merely a risk factor). The dominant mild-disease allele is **p.Val377Ile (p.V377I)**; the most common second allele associated with severe disease is **p.Ile268Thr (p.I268T)**. Carrier frequency is high in people of Northern European (especially Dutch) ancestry. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/); [Frontiers SHARE 2024](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1466844/full))

**Environmental flare triggers (not disease causes).** Vaccination/immunization, infection, physical or emotional stress, surgery, and minor trauma precipitate febrile attacks. A central mechanistic insight: the mutant enzyme is **thermolabile**, so any rise in body temperature further reduces residual activity — fever begets more isoprenoid shortage in a feed-forward loop. ([PMC4855321 natural history](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/); [PMC9525117 / JCI 160929](https://pmc.ncbi.nlm.nih.gov/articles/PMC9525117/))

> "Fever episodes can be precipitated by vaccination, infection, or physical and emotional stress." In cohorts, "vaccination triggered 36–63% of attacks." ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))

> The MK enzyme is thermolabile, making "any febrile illness a potential trigger for autoinflammatory disease flares." ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Protective factors.** No established genetic protective alleles. **Female sex** and **homozygous p.V377I** genotype correlate with **spontaneous improvement / attenuation of attacks with age**. ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))

**Gene–environment interaction.** The thermolability of mutant MK is the canonical gene-by-environment node: an environmental insult that raises core temperature (infection, vaccine reaction) interacts with the temperature-sensitive mutant enzyme to acutely deepen isoprenoid depletion and precipitate the inflammatory cascade. ([PMC9525117](https://pmc.ncbi.nlm.nih.gov/articles/PMC9525117/))

---

## 3. Phenotypes

Onset is typically **in the first year of life** (78% in year 1; 92% before age 5). Attacks are **episodic/recurrent**, lasting **3–7 days (median ~5 days)**, recurring every few weeks (median ~12 attacks/year in HIDS, up to ~25 in severe MKD), with attack frequency declining through adolescence/adulthood. ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))

**Clinical features and frequencies** (International HIDS Database / cohort data; suggested HPO terms):

| Phenotype | Frequency | Type | Suggested HPO |
|---|---|---|---|
| Recurrent fever (often >40°C), episodic | ~100% (defining) | Symptom | **HP:0001954** Episodic fever / HP:0001945 Fever |
| Cervical lymphadenopathy | 84–87% | Sign | **HP:0002721**? → HP:0002716 Lymphadenopathy |
| Abdominal pain | 85–88% | Symptom | **HP:0002027** Abdominal pain |
| Diarrhea | 69–84% | Symptom | **HP:0002014** Diarrhea |
| Vomiting | 69–71% | Symptom | **HP:0002013** Vomiting |
| Arthralgia | 71–84% | Symptom | **HP:0002829** Arthralgia |
| Skin rash (maculopapular/urticarial) | 39–69% | Sign | **HP:0000988** Skin rash |
| Aphthous ulcers (oral/genital) | 43–60% | Sign | **HP:0010783**? → HP:0000155 Oral ulcer / HP:0011110 Recurrent aphthous stomatitis |
| Splenomegaly | 32–63% | Sign | **HP:0001744** Splenomegaly |
| Hepatomegaly | 22–37% | Sign | **HP:0002240** Hepatomegaly |
| Headache | 38–63% | Symptom | **HP:0002315** Headache |
| Myalgia | 22–57% | Symptom | **HP:0003326** Myalgia |
| Arthritis | variable | Sign | **HP:0001369** Arthritis |
| Elevated acute-phase reactants (CRP, SAA, leukocytosis) during flares | ~all flares | Lab | **HP:0011227** Elevated CRP; HP:0011966 Elevated SAA (verify) |
| Elevated serum IgD (and often IgA) | majority (mild MKD) | Lab | **HP:0003498**? Increased IgD (verify) |
| Elevated urinary mevalonic acid | severe MKD constant; mild MKD only during flares | Lab | — (HP for mevalonic aciduria, verify) |

**Severe-MKD (mevalonic aciduria)–specific phenotypes** (low/undetectable residual activity, <0.5%):
- Psychomotor/developmental delay — **HP:0001263** Global developmental delay
- Progressive cerebellar ataxia — **HP:0002066** Gait ataxia / HP:0001251 Ataxia; cerebellar atrophy **HP:0001272**
- Hypotonia — **HP:0001252**
- Failure to thrive / growth retardation — **HP:0001508**
- Dysmorphic features (dolichocephaly, triangular face, low-set ears, downslanting palpebral fissures) — **HP:0001999**
- Progressive visual impairment, cataracts, retinal dystrophy/uveitis — **HP:0000505 / HP:0000518**
- Seizures (~5%), cerebellar syndrome (~3%) — **HP:0001250 Seizure**, HP:0001251

> "MVA is characterized by psychomotor retardation, failure to thrive, progressive cerebellar ataxia, dysmorphic features, progressive visual impairment and recurrent febrile crises." ([PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/))

**Phenotype characteristics:** onset neonatal–infantile; severity ranges mild→severe and tracks residual enzyme activity; course is **episodic/recurrent** in mild MKD and **progressive** (neurodegenerative) in severe MKD; attack frequency declines with age in mild MKD.

**Quality-of-life impact:** Recurrent attacks cause major school/work absence and impaired health-related QoL; canakinumab treatment produced "marked improvements in HRQoL" and catch-up growth (height/weight/BMI z-scores). ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/); [CLUSTER trial, PMID 34554243](https://pubmed.ncbi.nlm.nih.gov/34554243/))

---

## 4. Genetic / Molecular Information

**Causal gene:** ***MVK*** (mevalonate kinase), 12q24.11, **HGNC:7530** (`hgnc:7530`), OMIM 251170, UniProt **Q03426**, EC **2.7.1.36**. The protein is a peroxisomal/cytosolic kinase that phosphorylates mevalonate to mevalonate-5-phosphate. ([OMIM 251170](https://omim.org/entry/251170))

**Pathogenic variants:**
- **>300 distinct *MVK* variants** documented (catalogued in the Infevers registry). ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))
- **p.Val377Ile (c.1129G>A; p.V377I)** — the dominant mild-disease allele; **~42% of alleles in Dutch patients**; **>95% of HIDS patients carry it** (usually compound heterozygous). Residual MK activity ~10–28% of wild type. Missense, likely a folding/stability defect. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/); [PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/))
- **p.Ile268Thr (p.I268T)** — second most common; associated with **more severe phenotype and protein-stability disruption**; over-represented in mevalonic aciduria. Missense. ([Chinese cohort PMC12297814](https://pmc.ncbi.nlm.nih.gov/articles/PMC12297814/))
- Other recurrent: p.His20Pro/Asn, p.Ala334Thr, p.Asn301Thr, plus nonsense, frameshift, and splice variants in severe disease. "Hotspot" conserved regions: **residues 8–35 and 234–338**. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

> "More than 95% of patients with HIDS are compound heterozygous for the V377I MVK allele, whereas a second mutant allele, I268T, is specific to patients with MA." ([PMC11590122 / search synthesis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Variant classification:** Per ACMG/AMP and curated in **ClinVar / Infevers**; p.V377I and p.I268T are classified **Pathogenic**. Pathogenicity assessment is supported by the Infevers database. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Allele frequency:** p.V377I is notably common in Northern Europeans — **~1 in 65 Dutch individuals carries a heterozygous pathogenic *MVK* variant**. Check **gnomAD** for current population frequencies. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Origin:** **Germline**, autosomal recessive. No somatic role.

**Functional consequence:** **Loss of function / reduced catalytic activity and/or reduced protein stability** (hypomorphic). The mutant enzyme is **thermolabile** — activity falls further with rising temperature, a key pathogenic feature. ([PMC9525117](https://pmc.ncbi.nlm.nih.gov/articles/PMC9525117/))

**Modifier genes:** Candidate disease modifiers have been proposed (e.g., genes affecting inflammatory tone), explaining incomplete genotype–phenotype correlation; evidence is preliminary. ([Putative modifier genes, Spandidos / MMR 2016](https://www.spandidos-publications.com/10.3892/mmr.2016.4918))

**Epigenetics / chromosomal abnormalities:** No established epigenetic mechanism or recurrent chromosomal abnormality; this is a point-mutation/small-variant Mendelian disorder.

---

## 5. Environmental Information

- **Environmental factors:** None cause the disease. Heat/fever (any cause), surgery, and trauma exacerbate it via the thermolabile enzyme.
- **Lifestyle factors:** Emotional/physical stress can trigger flares; no diet or smoking association established.
- **Infectious agents:** Infections are **flare triggers**, not etiologic agents. Intercurrent infection (and the febrile response to it or to vaccines) is the commonest precipitant. ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))

---

## 6. Mechanism / Pathophysiology

**The causal chain (upstream → downstream):**

1. **Enzymatic block.** Biallelic *MVK* variants reduce mevalonate kinase activity → mevalonate accumulates (excreted as urinary mevalonic acid) and downstream **isoprenoid pyrophosphates fall**, specifically **farnesyl-PP (FPP) and geranylgeranyl-PP (GGPP)**. GGPP shortage is the key inflammatory node. ([PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/))
2. **Defective protein prenylation.** GGPP/FPP are the lipid anchors for prenylation of small GTPases. Loss of GGPP → **impaired geranylgeranylation of RhoA** (and other Rho-family GTPases). ([PMC2946549](https://pmc.ncbi.nlm.nih.gov/articles/PMC2946549/); [Defective prenylation, PMC6702261](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6702261/))
3. **RhoA inactivation releases pyrin.** Geranylgeranylated, membrane-bound RhoA normally keeps the **pyrin inflammasome** under tonic phospho-inhibition (via RhoA→PKN1/2 phosphorylation of pyrin). Unprenylated RhoA cannot reach the membrane and cannot activate this brake → **pyrin inflammasome de-repression**. ([PMC4183811](https://pmc.ncbi.nlm.nih.gov/articles/PMC4183811/))
4. **Inflammasome → IL-1β.** De-repressed pyrin assembles an ASC/caspase-1 inflammasome → **caspase-1 cleaves pro-IL-1β → mature IL-1β secretion** → systemic autoinflammation (fever, acute-phase response). A parallel arm: unprenylated RhoA stimulates **Rac1**, which primes additional IL-1β secretion. ([PMC4183811](https://pmc.ncbi.nlm.nih.gov/articles/PMC4183811/))
5. **Clinical flare.** IL-1β (with IL-6, TNF downstream) drives recurrent fever, lymphadenopathy, serositis, rash, arthralgia, and the acute-phase rise in CRP/SAA. Sustained SAA elevation → AA amyloid deposition over years.

> "Geranylgeranylated RhoA normally inhibits the pyrin inflammasome through phospho-inactivation. Mutations of MVK lead to release of the normal, constitutive tonic inhibition of the pyrin inflammasome and excess IL-1 production… mediated at least in part by inactivation of the small GTPase RhoA and subsequent activation of pyrin, which forms an inflammasome resulting in caspase-1 mediated IL-1β release." ([PMC4183811](https://pmc.ncbi.nlm.nih.gov/articles/PMC4183811/))

**Molecular pathways:** Mevalonate/isoprenoid (cholesterol) biosynthesis pathway (KEGG hsa00900 terpenoid backbone biosynthesis; Reactome cholesterol biosynthesis); pyrin (MEFV) inflammasome; RhoA/Rac1 GTPase signaling; caspase-1/IL-1β axis.

**Cellular processes:** Innate immune activation, inflammasome assembly, pyroptosis-associated cytokine release. Also reported: increased mitochondrial dysfunction, autophagy alterations, and enhanced cell death in patient monocytes. ([PMC4959763](https://pmc.ncbi.nlm.nih.gov/articles/PMC4959763/))

**Protein dysfunction:** MK loss of catalytic activity and reduced thermostability; downstream, **GTPases fail to localize to membranes** due to absent prenyl anchors.

**Metabolic changes:** ↑ mevalonic acid (urine/plasma); ↓ non-sterol isoprenoids (GGPP, FPP, dolichol, ubiquinone/CoQ10); cholesterol is usually maintained (sterol arm is spared at the expense of isoprenoids during flares).

**Immune involvement:** This is a prototypical **monogenic autoinflammatory disorder** — innate (not autoimmune) hyperinflammation, IL-1β-centric. Elevated IgD is a biomarker, not the driver.

**Suggested GO / CL / pathway terms:**
- GO biological process: **GO:0019287** (isopentenyl diphosphate biosynthetic process, mevalonate pathway) / GO:0006695 cholesterol biosynthetic process; **GO:0018343** protein farnesylation / **GO:0018344** protein geranylgeranylation; **GO:0050702** interleukin-1 beta secretion; **GO:0072559** NLRP3/inflammasome (pyrin: GO:0140738? verify); **GO:0007266** Rho protein signal transduction.
- Cell types (CL): **CL:0000576** monocyte; **CL:0000235** macrophage; **CL:0000094** granulocyte/neutrophil; **CL:0000236** B cell (IgD); dendritic cells.

---

## 7. Anatomical Structures Affected

**Organ / system level (mild MKD):** Multisystem during flares — **immune/lymphatic** (lymph nodes: cervical, **UBERON:0000029** lymph node), **spleen** (UBERON:0002106), **liver** (UBERON:0002107), **gastrointestinal tract** (UBERON:0000160 intestine — abdominal pain, diarrhea, vomiting; serositis/peritoneal adhesions), **skin** (UBERON:0002097 — rash), **joints** (UBERON:0000019? → UBERON:0001485 joint — arthralgia/arthritis), **oral mucosa** (UBERON:0000165 mouth — aphthae).

**Severe MKD adds CNS / sensory:** **cerebellum** (UBERON:0002037 — ataxia, cerebellar atrophy), **brain** broadly (developmental delay), **eye** (UBERON:0000970 — cataract, retinal dystrophy, uveitis), skeletal/craniofacial (dysmorphism). Kidney: AA amyloidosis (UBERON:0002113 kidney) as a long-term complication; renal angiomyolipoma reported (~6%).

**Tissue / cell level:** Innate immune effector cells — **monocytes/macrophages** and **neutrophils** are the principal cytokine producers; B cells account for IgD elevation. **Subcellular:** mevalonate pathway enzymes are **peroxisomal/cytosolic** (GO:0005777 peroxisome; GO:0005829 cytosol); the prenylation defect manifests at the **plasma membrane** (failure of GTPase membrane anchoring, GO:0005886).

**Laterality:** Systemic/bilateral; lymphadenopathy often **cervical and symmetric**.

---

## 8. Temporal Development

- **Onset:** Congenital/infantile — typically **first year of life** (78% year 1; 92% by age 5); severe MKD presents neonatally/antenatally. ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))
- **Pattern:** **Episodic/recurrent (periodic fever)** in mild MKD; **chronic-progressive neurodegeneration** superimposed on attacks in severe MKD.
- **Attack architecture:** abrupt fever ± prodrome → 3–7 days (median 5) → resolution; recurs every 2–8 weeks.
- **Progression / course:** Mild MKD generally **attenuates with age** (fewer attacks in adulthood; some spontaneous improvement, especially females and p.V377I homozygotes). Severe MKD may be **fatal in early childhood**. ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))
- **Duration:** Lifelong (chronic) condition.
- **Critical windows:** Vaccination/infection in infancy commonly unmask first attacks; early diagnosis and IL-1 blockade are the intervention window to prevent growth failure and amyloidosis.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic *MVK* variants). ([OMIM](https://omim.org/entry/251170))
- **Prevalence/incidence (rare):** ~**5 per 1,000,000** general population (Netherlands) to **6.2 per 1,000,000** (Germany); pediatric incidence **0.39–1.3 per 1,000,000 person-years**. ~300 cases documented worldwide by ~2013 (≥180 HIDS, ≥30 MVA historically). ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/); [PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))
- **Carrier frequency:** **~1 in 65** in the Dutch population. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))
- **Penetrance:** Essentially complete for biallelic pathogenic genotypes, but **expressivity is highly variable** (even within genotypes/families).
- **Genotype–phenotype:** Severity correlates with **residual enzyme activity** (mild MKD ~1.8–28%; severe MKD <0.5%) more than with specific genotype; no consistent genotype correlation with attack frequency/onset. AA amyloidosis is **over-represented in p.V377I/p.I268T compound heterozygotes**. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/); [PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))
- **Founder effect:** p.V377I shows a **Northern European founder distribution** (Netherlands, France, Italy).
- **Demographics:** Higher in Northern/Western European ancestry; **roughly equal sex ratio** (female sex linked to milder/improving course); pediatric onset predominant.
- **Anticipation / mosaicism:** Not features of this disorder.

---

## 10. Diagnostics

**Laboratory:**
- **Urinary organic acids — mevalonic acid:** markedly and constantly elevated in severe MKD; in mild MKD elevated **only during flares**. (Diagnostic for MVA.) ([PMC1475558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/))
- **Acute-phase reactants:** CRP, ESR, leukocytosis, and **serum amyloid A (SAA)** rise during attacks; **SAA may be the more sensitive inflammation marker** in MKD. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))
- **Serum IgD (and often IgA):** historically elevated, but **IgD testing is now discouraged** — poor sensitivity/specificity (often normal in young children). ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))
- **Enzyme assay:** Reduced mevalonate kinase activity in leukocytes/fibroblasts (confirmatory). LOINC codes apply for organic acid and CRP/SAA assays (verify specific LOINC).

**Genetic testing (definitive):** ***MVK* sequencing** — single-gene test or autoinflammatory/periodic-fever **gene panel** (alongside *MEFV*, *TNFRSF1A*, *NLRP3*); WES/WGS in undifferentiated cases. Pathogenicity referenced against **Infevers** and ClinVar. "MVK gene testing is prioritized as the definitive diagnostic approach." ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Clinical criteria:** **2015 Eurofever/PRINTO classification** (onset <2 yr, aphthous stomatitis, painful lymph nodes, diarrhea, absence of chest pain) — **~93% sensitivity, ~89% specificity**. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Differential diagnosis:** Other hereditary periodic fevers — **FMF** (*MEFV*), **TRAPS** (*TNFRSF1A*), **CAPS** (*NLRP3*), **PFAPA syndrome**, systemic JIA, cyclic neutropenia, and infections. Distinguishing features: very early onset, vaccine-triggered attacks, prominent cervical adenopathy + GI symptoms + aphthae point to MKD.

**Imaging/neuro (severe MKD):** Brain MRI shows **cerebellar atrophy**; ophthalmologic exam for cataract/retinopathy.

**Screening:** Not part of routine newborn screening in most regions, though MVA is detectable by urinary organic-acid analysis. **Carrier/cascade screening** offered in affected families (high Dutch carrier rate); prenatal diagnosis possible by *MVK* genotyping or enzyme assay.

---

## 11. Outcome / Prognosis

- **Mild MKD (HIDS):** generally **normal life expectancy**; morbidity from recurrent attacks, growth impairment, school/work disruption; attacks tend to lessen with age. ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))
- **Severe MKD (MVA):** guarded — **can be fatal in early childhood** (e.g., 4 deaths among 11 MVA children aged 6 months–4 years in one European cohort); survivors have permanent neurodevelopmental disability. ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))
- **Key long-term complication — AA (secondary) amyloidosis:** **~3–5%**, after 20+ years of chronically elevated SAA, leading to **renal failure**; over-represented in p.V377I/p.I268T compound heterozygotes. Other complications: abdominal adhesions (~10%), joint contractures (~4%), renal angiomyolipoma (~6%), severe (e.g., pneumococcal) infections (1–6%), chronic multi-organ involvement (~55%). ([PMC4855321](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/))
- **Prognostic factors:** Residual enzyme activity (the dominant determinant), genotype (amyloidosis risk), sustained SAA control on therapy, female sex (better), age (improvement over time in mild disease).

---

## 12. Treatment

The therapeutic logic follows the mechanism: block **IL-1β**.

**Pharmacotherapy — IL-1 blockade (first-line biologics):**
- **Canakinumab** (anti-IL-1β monoclonal antibody) — **only agent with regulatory approval/RCT evidence** for MKD. In the **Phase 3 CLUSTER trial (NCT02059291)**: **35% complete response at week 16 vs 6% placebo**; over the 72-week extension, **64% of patients had no flares** and **>90% reported minimal/no disease activity** (vs median 12 flares/year at baseline). Often needs **higher doses** (150–300 mg q4–8 wk) than for CAPS. ([CLUSTER, PMID 34554243](https://pubmed.ncbi.nlm.nih.gov/34554243/); [PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/)) — MAXO: pharmacotherapy / **NCIT:C15986** + therapeutic agent canakinumab (NCIT).
- **Anakinra** (recombinant IL-1 receptor antagonist) — effective for on-demand or continuous therapy; "rational alternative" when canakinumab unavailable; high response in pediatric HIDS. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Second-line / alternative biologics:**
- **Tocilizumab** (anti-IL-6R) — option for IL-1-inhibitor-refractory cases (limited evidence). ([Tocilizumab, PMC6129367](https://pmc.ncbi.nlm.nih.gov/articles/PMC6129367/))
- **Etanercept / TNF inhibitors** — partial/variable benefit; second-line.

**Acute flare management:** NSAIDs and **short-course corticosteroids** for symptom control. MAXO: supportive care / pharmacotherapy.

**Not recommended:** **Statins and bisphosphonates are not recommended** — statins (HMG-CoA reductase inhibitors) may *worsen* isoprenoid depletion; earlier simvastatin reports were not borne out. ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/))

**Curative / advanced:** **Allogeneic hematopoietic stem cell transplantation (HSCT)** for severe, biologic-refractory MKD — in a multicenter series, **7/9 achieved complete remission** but **2 died of transplant-related complications**; reserved for severe cases. MAXO: **MAXO:0010039** organ/cell transplantation (HSCT). ([PMC11590122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/)) **Liver transplantation** has been used in select severe MVA cases.

**Experimental:** **Geranylgeraniol (GGOH) supplementation** — replenishes the depleted isoprenoid; a 2024 study reported "improvement in inflammatory parameters and reversal of the disease-specific protein signature in patients with hyper-IgD syndrome." ([medRxiv 2024](https://www.medrxiv.org/content/10.1101/2024.07.17.24309492.full.pdf))

**Pharmacogenomics:** No established PGx guidance; therapy is genotype-informed mainly via severity (residual activity) rather than drug metabolism.

**Supportive/preventive within treatment:** judicious vaccination (benefits outweigh transient flare risk; consider IL-1 cover), antipyretics, growth monitoring, SAA monitoring to pre-empt amyloidosis.

---

## 13. Prevention

- **Primary prevention:** Not possible (Mendelian). **Genetic counseling** (autosomal recessive; 25% recurrence risk) and **carrier/cascade screening** in families — especially relevant given the high Dutch carrier frequency. **Preimplantation/prenatal genetic diagnosis** available. MAXO: **MAXO:0000079** genetic counseling.
- **Secondary prevention:** Early *MVK* genetic diagnosis to start IL-1 blockade promptly, preventing growth failure and chronic inflammation.
- **Tertiary prevention:** **SAA/CRP monitoring** and sustained IL-1 inhibition to prevent **AA amyloidosis** and renal failure; manage triggers; consider prophylactic IL-1 cover around vaccinations/surgery.
- **Trigger avoidance:** managing infections promptly and minimizing avoidable febrile/stress triggers (with the caveat that vaccines remain recommended).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (**NCBITaxon:9606**). The *MVK* gene and mevalonate pathway are **deeply evolutionarily conserved** (yeast→plants→mammals), as is protein prenylation.
- **Orthologs:** *Mvk* in mouse (**NCBI Gene mouse Mvk**), rat, zebrafish; ERG12 in *S. cerevisiae*. (Check Alliance of Genome Resources / HomoloGene for IDs.)
- **Natural disease in animals:** No well-described spontaneous naturally occurring MKD in companion animals/wildlife (OMIA — verify); the disease is essentially studied via engineered models.
- **Comparative biology:** The RhoA-prenylation → pyrin-inflammasome axis is conserved in mammals, supporting cross-species mechanistic study.
- **Zoonosis:** Not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

- **Mouse — complete knockout is embryonic lethal** (mevalonate pathway is essential), limiting full-null models. **Heterozygous *Mvk*+/− mice** have reduced MK activity and immune dysfunction (↑ serum IgD, ↑ TNF-α). ([search synthesis; PMC4959763](https://pmc.ncbi.nlm.nih.gov/articles/PMC4959763/))
- **"Mouse avatar" / knock-in & temperature studies:** Models recapitulating patient genotypes show that **increased core body temperature exacerbates the protein-prenylation defect** — directly modeling the thermolabile-enzyme/fever-trigger mechanism. ([JCI 160929 / PMC9525117](https://pmc.ncbi.nlm.nih.gov/articles/PMC9525117/); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2022.02.28.480959.full.pdf))
- **Pharmacologic models:** Mevalonate-pathway blockade with **statins, bisphosphonates (aminobisphosphonates), and prenyltransferase inhibitors** in cells/animals reproduces the prenylation defect and IL-1β hypersecretion. ([PMC4183811](https://pmc.ncbi.nlm.nih.gov/articles/PMC4183811/))
- **In vitro / cellular models:** Patient PBMCs/monocytes, fibroblasts, and **PBMC + statin/inhibitor systems** demonstrate the **RhoA→pyrin→caspase-1→IL-1β** cascade and Rac1 priming. ([PMC4183811](https://pmc.ncbi.nlm.nih.gov/articles/PMC4183811/); [PMC2946549](https://pmc.ncbi.nlm.nih.gov/articles/PMC2946549/))
- **Model strengths:** Heterozygous and pharmacologic models reproduce inflammatory cytokine phenotype and the temperature-dependence; **limitation:** no single model fully captures the severe neurodegenerative MVA phenotype, and full-null lethality precludes a true KO. Zebrafish *mvk* models are referenced but less characterized (verify).
- **Resources:** MGI/IMPC (mouse), ZFIN (zebrafish), Alliance of Genome Resources.

---

## Key Evidence Citations (for KB population)

| PMID / source | Use |
|---|---|
| **PMC1475558** (Houten et al., 2006, *Orphanet J Rare Dis*) | Disease overview, spectrum, biochemistry, diagnosis |
| **PMC11590122 / PMID 39600705** (2024 SHARE revision, *Front Immunol*) | Terminology, epidemiology, diagnostics, treatment recs, amyloidosis |
| **PMC4855321** (Natural history review, 2016, *Pediatr Rheumatol*) | Phenotype frequencies, onset, triggers, complications |
| **PMC4183811 / JBC 2014** | RhoA/Rac1 → pyrin inflammasome → IL-1β mechanism |
| **PMC2946549** | Compromised RhoA/Rac1 geranylgeranylation in MKD |
| **PMID 34554243** (CLUSTER trial, *Rheumatology* 2022) | Canakinumab long-term efficacy/safety; NCT02059291 |
| **PMC9525117 / JCI 160929 (2022)** | Temperature exacerbates prenylation defect (mouse models) |
| **PMC6702261** | Defective protein prenylation across MKD severity spectrum |
| **OMIM 251170 / 260920 / 610377** | Gene + phenotype identifiers, inheritance |
| **medRxiv 2024.07.17.24309492** | Geranylgeraniol supplementation (experimental) |

---

## ⚠️ Curation cautions (per dismech anti-hallucination SOP)

Before committing any of this to a KB entry:
1. **Verify all ontology IDs** — the MONDO/ORPHA/ICD-11/HPO/GO/CL/UBERON IDs above are *suggestions*; several (especially MONDO IDs, the SAA/IgD HPO terms, and lymphadenopathy HP) are flagged and **must be confirmed with OAK** (`runoak ... info <ID>`) and `just validate-terms-file`.
2. **All evidence snippets must be exact abstract substrings** — the quoted sentences here are drawn from WebFetch summaries of PMC pages, *not* verified against the real PubMed abstract. Run `just fetch-reference PMID:XXXX` and `just validate-references` for each before use.
3. **Confirm OMIM 260920 vs alternative HIDS OMIM coding** and the exact ORPHA umbrella code (309025) against current Orphadata — given the NEC risk in spectrum disorders with multiple historical names (HIDS vs MVA vs MKD).

**Sources:**
- [Houten et al., Orphanet J Rare Dis 2006 (PMC1475558)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1475558/)
- [Politiek & Waterham, SHARE revision, Front Immunol 2024 (PMC11590122)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590122/)
- [Natural history of MKD, Pediatr Rheumatol 2016 (PMC4855321)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4855321/)
- [Unprenylated RhoA & IL-1β, JBC 2014 (PMC4183811)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4183811/)
- [Compromised RhoA/Rac1 geranylgeranylation (PMC2946549)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2946549/)
- [CLUSTER trial, PMID 34554243](https://pubmed.ncbi.nlm.nih.gov/34554243/)
- [Temperature & prenylation, JCI 2022 (PMC9525117)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9525117/)
- [Defective prenylation spectrum (PMC6702261)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6702261/)
- [MKD current perspectives (PMC4959763)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4959763/)
- [OMIM 251170 (MVK)](https://omim.org/entry/251170)
- [MedlinePlus Genetics: MKD](https://medlineplus.gov/genetics/condition/mevalonate-kinase-deficiency/)
- [NORD: Hyper-IgD/MKD](https://rarediseases.org/rare-diseases/hyper-igd-syndrome/)
- [Geranylgeraniol supplementation, medRxiv 2024](https://www.medrxiv.org/content/10.1101/2024.07.17.24309492.full.pdf)