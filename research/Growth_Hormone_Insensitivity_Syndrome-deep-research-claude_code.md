---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T08:42:29.883201'
end_time: '2026-06-30T08:46:50.776104'
duration_seconds: 260.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Growth Hormone Insensitivity Syndrome
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
  num_turns: 9
  total_cost_usd: 2.181071
  session_id: 5f426858-f04e-4719-98bb-d4a179fd42cb
  stop_reason: end_turn
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Growth Hormone Insensitivity Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Growth Hormone Insensitivity Syndrome** covering all of the
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

# Comprehensive Research Report: Growth Hormone Insensitivity Syndrome (Laron Syndrome)

> **Scope note:** "Growth Hormone Insensitivity Syndrome" (GHIS) is used both narrowly — as a synonym for classic **Laron syndrome** (primary GH receptor deficiency, OMIM #262500) — and broadly, as an umbrella for the genetic disorders of the GH–IGF-1 axis that share the biochemical signature of low IGF-1 with normal/elevated GH. This report treats **Laron syndrome / GHR deficiency as the prototype** and addresses the broader GHI spectrum (STAT5B, IGFALS, IGF1, IGF1R, PAPPA2) where relevant, since the dismech entry will most plausibly be anchored on the classic Mendelian disorder.

---

## 1. Disease Information

**Overview.** Growth Hormone Insensitivity Syndrome (Laron syndrome) is an autosomal recessive disorder of severe postnatal growth failure caused by the inability to generate insulin-like growth factor-1 (IGF-1) in response to growth hormone (GH). The defining biochemical hallmark is **high or normal circulating GH with low serum IGF-1** that fails to rise on GH stimulation — i.e., the pituitary is intact but peripheral tissues are "deaf" to GH. It was first described by the Israeli pediatric endocrinologist **Zvi Laron** in 1966 in a series of consanguineous Yemenite Jewish families.

**Key identifiers:**
- **OMIM:** #262500 (Laron syndrome / GH insensitivity, classic GHR-deficiency form); related loci/forms: GHR gene *600946; STAT5B GHI with immune dysregulation #245590 (GHISID1); IGFALS deficiency (ACLSD) #615961; IGF1 deficiency #608747; IGF1R resistance #270450.
- **MONDO:** MONDO:0008638 (Laron syndrome).
- **Orphanet:** ORPHA:633 (Growth hormone insensitivity syndrome / Laron syndrome).
- **ICD-10:** E34.3 (Short stature due to endocrine disorder); **ICD-11:** 5A60.1 (Growth hormone insensitivity).
- **MeSH:** D046150 "Laron Syndrome."
- **UMLS/SNOMED CT:** Laron-type dwarfism (e.g., SNOMED 237689005).

**Synonyms / alternative names:** Laron-type dwarfism; primary growth hormone insensitivity (GHI); growth hormone receptor deficiency (GHRD); Laron-type pituitary dwarfism; severe primary IGF-1 deficiency (SPIGFD — the regulatory/therapeutic term used in the mecasermin label); somatomedin deficiency.

**Data derivation.** The knowledge is aggregated from **disease-level resources** (OMIM, Orphanet, GeneReviews) and from a small number of deeply phenotyped **cohorts of individual patients** — principally the **Israeli cohort** (assembled by Zvi Laron from 1958; ~64 patients by 2009) and the **southern Ecuadorian cohort** (~100 individuals, studied by Jaime Guevara-Aguirre). It is *not* primarily an EHR-derived entity given its rarity.

*Sources:* [OMIM #262500](https://omim.org/entry/262500); [OMIM *600946 GHR](https://omim.org/entry/600946); [MedlinePlus: Laron syndrome](https://medlineplus.gov/genetics/condition/laron-syndrome/); [NORD: Growth Hormone Insensitivity](https://rarediseases.org/rare-diseases/growth-hormone-insensitivity/).

---

## 2. Etiology

**Primary cause (genetic).** Classic Laron syndrome results from **biallelic (homozygous or compound heterozygous) loss-of-function mutations in *GHR*** (growth hormone receptor gene, 5p13–p12). Over 70–100 distinct *GHR* mutations have been catalogued — deletions, nonsense, missense, and splice-site variants — predominantly affecting the **extracellular hormone-binding domain**, abolishing GH binding or receptor dimerization. Post-receptor and downstream defects (STAT5B, etc.) cause clinically overlapping GHI.

> *"Laron syndrome is caused by homozygous or compound heterozygous mutation in the growth hormone receptor gene (GHR; 600946)… Over 70 mutations of the GHR gene have been identified including deletions, missense and nonsense point mutations and splice site mutations."* — OMIM #262500.

**Genetic risk factors.**
- **Causal variants:** biallelic *GHR* LoF (most common). The canonical Ecuadorian founder allele is **E180splice** (exon 6 splice mutation, c.594A>G); the Israeli/Mediterranean cohorts carry other recurrent alleles.
- **Other causal genes (broader GHI spectrum):** *STAT5B* (recessive and dominant-negative forms — GHI **with immune dysregulation**); *IGFALS* (acid-labile subunit deficiency — milder); *IGF1* (IGF-1 deficiency with intrauterine growth restriction, microcephaly, deafness, intellectual disability); *IGF1R* (IGF-1 resistance); *PAPPA2* (impaired IGF-1 bioavailability). A **continuum** of genetic, biochemical, and phenotypic severity exists across these genes (PMID:21525302).
- **Modifier loci:** variation in *IGFBP3*, *ALS*, and the *IGF1R* axis modulate residual growth.

**Environmental risk factors.** No environmental *cause* — the disorder is monogenic. The dominant non-genetic risk factor is **consanguinity / population isolation**, which raises homozygosity for the recessive allele. Nutrition and intercurrent illness modify the severity of hypoglycemia and growth, not disease occurrence.

**Protective factors.** Not applicable to disease causation. Notably, the *disease state itself* is associated with downstream **protection against cancer and type 2 diabetes** (see §6/§11) — a "protective phenotype," not a protective factor against the disorder.

**Gene–environment interactions.** Caloric intake and recurrent fasting interact with the impaired counter-regulatory capacity (low IGF-1, enhanced insulin sensitivity) to provoke **fasting/ketotic hypoglycemia**, especially in infancy.

*Sources:* [OMIM #262500](https://omim.org/entry/262500); [Genetic causes of GHI beyond GHR (PMC7979432)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7979432/); [Genetic defects in the GH–IGF-I axis (PMC3356141)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3356141/); [Continuum of GHI abnormalities, PMID:21525302](https://pubmed.ncbi.nlm.nih.gov/21525302/).

---

## 3. Phenotypes

Phenotypes cluster into (a) severe proportionate short stature, (b) characteristic craniofacial/somatic features, (c) metabolic abnormalities, and (d) the biochemical signature.

| Phenotype | Type | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Severe proportionate short stature (often −4 to −10 SDS; adult height ~95–124 cm) | Physical/growth | Postnatal (birth length near-normal, then failure) | Severe, lifelong | Obligate (~100%) | **HP:0004322 Short stature**; HP:0008897 Postnatal growth retardation |
| Low/undetectable serum IGF-1, unresponsive to GH | Lab | Congenital | Severe, stable | ~100% | HP:0003575 (GH excess); HP:0008258 (decreased serum IGF-1) |
| Elevated/normal basal GH | Lab | Congenital | — | ~100% | HP:0000824-related |
| Frontal bossing / saddle nose / "doll-like" facies, sparse hair | Clinical sign | Childhood | Stable | Frequent | HP:0002007 Frontal bossing; HP:0000414 Bulbous nose |
| Hypoglycemia (fasting/ketotic), neonatal | Lab/clinical | Neonatal–infancy | Episodic, can be severe | Frequent | HP:0001943 Hypoglycemia; HP:0001998 Neonatal hypoglycemia |
| Truncal/central obesity, increased body fat, reduced lean mass | Physical | Childhood→adult | Progressive | Frequent | HP:0001513 Obesity; HP:0003712 (abnormal muscle) |
| Micropenis / small genitalia, delayed puberty | Physical | Childhood/adolescence | Variable | Frequent (males) | HP:0000054 Micropenis; HP:0000823 Delayed puberty |
| High-pitched voice, hypoplastic larynx | Sign | Childhood | Stable | Frequent | HP:0001620 High-pitched voice |
| Small hands/feet (acromicria), thin skin, limited elbow extension | Physical | Childhood | Stable | Frequent | HP:0001167 Abnormal finger morphology; HP:0001238 (acromicria) |
| Delayed bone age, osteopenia, thin cortical bone | Radiologic | Childhood | Progressive | Frequent | HP:0002750 Delayed skeletal maturation; HP:0000938 Osteopenia |
| Reduced muscle strength / hypotonia (infancy), motor delay | Sign | Infancy | Improves with growth | Variable | HP:0001324 Muscle weakness |
| Blue sclerae, hip degeneration, sparse/thin hair | Sign | Variable | Stable/progressive | Occasional | HP:0000592 Blue sclerae |
| **STAT5B subtype only:** eczema, pulmonary disease, recurrent infection (immune dysregulation) | Clinical | Childhood | Progressive | Subtype-defining | HP:0002721 Immunodeficiency; HP:0000964 Eczema |

**Onset/severity/progression generalities:** Birth size is near-normal (IGF-1 prenatally is only partly GH-dependent), with **dramatic postnatal growth failure**. Short stature is **non-progressive but permanent**; metabolic features (obesity, insulin sensitivity) evolve over the lifespan.

**Quality-of-life impact.** Marked short stature affects psychosocial functioning, education/employment, and (structurally) injury risk from falls; obesity and skeletal fragility add morbidity. Cognition is generally **normal** in classic GHR-deficiency Laron syndrome (in contrast to IGF1-gene defects, which cause intellectual disability and deafness).

*Sources:* [OMIM #262500](https://omim.org/entry/262500); [Laron syndrome review, In Vivo 2016](https://iv.iiarjournals.org/content/30/4/375); [Brazilian Laron series, PMC7197995](https://pmc.ncbi.nlm.nih.gov/articles/PMC7197995/).

---

## 4. Genetic / Molecular Information

**Causal gene — *GHR* (HGNC:4263; OMIM *600946; chromosome 5p13–p12).** Encodes a 620-aa single-pass transmembrane cytokine-receptor-superfamily protein with an extracellular GH-binding domain (the proteolytically shed portion forms serum **GH-binding protein, GHBP**), a transmembrane domain, and an intracellular domain coupling to JAK2/STAT5.

**Pathogenic variants:**
- **Type/class:** the full mutational spectrum — large/partial **gene deletions**, **nonsense**, **missense** (esp. extracellular domain, e.g., disrupting disulfide bonds or dimerization), **splice-site** (the Ecuadorian **E180 splice** founder allele), and **intronic/pseudoexon** variants. Dominant-negative *GHR* variants in the transmembrane/intracellular region cause milder dominant GHI.
- **Classification (ACMG/AMP):** recurrent founder alleles are classified Pathogenic in ClinVar; many private missense variants are Likely Pathogenic/VUS pending functional data.
- **Allele frequency:** individually **ultra-rare** in gnomAD; enriched only in founder populations (southern Ecuador, Mediterranean/Middle Eastern consanguineous groups).
- **Origin:** **germline**, biallelic (recessive). No somatic role.
- **Functional consequence:** **loss of function** — failure of GH binding, receptor dimerization, or JAK2/STAT5 signal transduction → no IGF-1 transcription. **GHBP is low/absent** when the defect is in the extracellular domain (a useful biochemical discriminator) but **normal/high** in transmembrane/intracellular and post-receptor (STAT5B) defects.

**Downstream-axis genes (broader GHI):** *STAT5B* (HGNC:11367) — recessive LoF and dominant-negative; *IGFALS* (HGNC:5466); *IGF1* (HGNC:5464); *IGF1R* (HGNC:5465); *PAPPA2* (HGNC:8602). Mechanistic split: **IGF-1 deficiency** (GHR, STAT5B, IGF1), **IGF-1 bioavailability** (IGFALS, PAPPA2), **IGF-1 resistance** (IGF1R).

> *"Mutations in a number of components along this axis result in GHI and IGF deficiency (STAT5B, IGF1), IGF bioavailability (IGFALS, PAPPA2) or IGF resistance (IGF1R)."* — Genetic causes of GHI beyond GHR (PMC7979432).

**Modifier genes.** Polymorphisms/variants in *IGFBP3*, *IGFALS*, and the *IGF1R* pathway modulate residual linear growth and treatment response.

**Epigenetics.** No established primary epigenetic mechanism in classic Laron syndrome. Of note, **genome-wide profiling of Laron patients identified novel cancer-protection transcriptional/methylation pathways** (e.g., differential expression of genes regulating apoptosis, DNA repair, and metabolism) — relevant to the protective phenotype rather than disease causation.

**Chromosomal abnormalities.** Large multi-exon/whole-*GHR* **deletions** occur; otherwise no recurrent aneuploidy or translocation.

*Sources:* [OMIM *600946](https://omim.org/entry/600946); [GHI beyond GHR (PMC7979432)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7979432/); [Dominant-negative STAT5B (PMC5974024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5974024/); [Genome-wide profiling of Laron patients (PMC6627189)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627189/).

---

## 5. Environmental Information

- **Environmental factors:** none causal. The disorder is fully penetrant monogenic.
- **Lifestyle factors:** diet and fasting interact with the metabolic phenotype (hypoglycemia risk in infancy; obesity in later life), but do not cause or prevent the disorder.
- **Infectious agents:** not applicable to classic GHR-deficiency. (In the **STAT5B subtype**, recurrent infections are a *consequence* of immune dysregulation, not a trigger.)

*Source:* [MedlinePlus: Laron syndrome](https://medlineplus.gov/genetics/condition/laron-syndrome/).

---

## 6. Mechanism / Pathophysiology

**Core causal chain (upstream → downstream):**

1. **Biallelic *GHR* loss of function** (upstream trigger) → GH cannot bind/signal at target cells (chiefly **hepatocytes**).
2. **Failure of JAK2–STAT5B signal transduction.** Normally, GH binding induces GHR dimerization → JAK2 activation → STAT5B tyrosine phosphorylation, homodimerization, nuclear translocation, and transcription of *IGF1*, *IGFBP3*, and *IGFALS*.
   > *"Recruited STAT5B is tyrosine phosphorylated by JAK2, homodimerizes, and translocate[s] to the nucleus, where it binds DNA, regulating production of circulating IGF-I, IGFBP-3 and ALS."* — PMC7979432.
3. **Hepatic IGF-1 (and IGFBP-3, ALS) production collapses** → low circulating IGF-1; the ternary complex (IGF-1/IGFBP-3/ALS) that stabilizes serum IGF-1 is depleted.
4. **Loss of negative feedback** — IGF-1 normally restrains pituitary GH secretion; its absence causes **GH hypersecretion** (the paradoxical "high GH, low IGF-1" signature).
5. **Downstream phenotype:** loss of IGF-1–driven **chondrocyte proliferation at the growth plate** → severe postnatal linear growth failure; reduced anabolic signaling → altered body composition; impaired counter-regulation → hypoglycemia.

**Molecular pathways:** GH/GHR → **JAK2–STAT5B** (canonical), with secondary involvement of **PI3K–AKT–mTOR** and **RAS–MAPK** downstream of IGF-1/IGF1R. The disorder is fundamentally a **JAK-STAT signaling defect** (KEGG/Reactome: GH receptor signaling; JAK-STAT pathway; IGF-1 receptor signaling).

**Cellular processes:** reduced **chondrocyte and osteoblast proliferation** (growth plate); altered adipocyte and myocyte anabolism (obesity, sarcopenia); in the protective phenotype, **reduced pro-aging signaling**, increased apoptosis of damaged cells, and reduced oxidative DNA damage.

> *"Serum from subjects with GHR deficiency reduced DNA breaks but increased apoptosis in human mammary epithelial cells treated with hydrogen peroxide… [GHRD subjects had] only one nonlethal malignancy and no cases of diabetes, in contrast to a prevalence of 17% for cancer and 5% for diabetes in control[s]."* — Guevara-Aguirre et al., *Sci Transl Med* 2011 (PMID:21325617).

**Protein dysfunction:** loss of function of the GH receptor (or, in subtypes, of STAT5B as a transcription factor). Extracellular-domain mutants fail to bind GH and reduce serum GHBP; transmembrane/intracellular mutants may bind GH but fail to signal.

**Metabolic changes:** markedly **enhanced insulin sensitivity** (low IGF-1 → reduced lipolytic/diabetogenic GH-axis output relative to IGF-1 feedback) despite obesity; tendency to **fasting hypoglycemia** in infancy; reduced IGF-1–mediated lipid handling.

**Immune involvement:** none in classic GHR deficiency; **central to the STAT5B subtype** (STAT5B is also required for regulatory T-cell and NK function → eczema, lymphocytic interstitial pneumonitis, autoimmunity, recurrent infection).

**Tissue damage mechanisms:** primarily developmental/anabolic deficit rather than active tissue destruction; skeletal fragility (osteopenia) is a downstream consequence.

**Molecular profiling:** transcriptomic/genome-wide profiling of Laron patient cells shows differential regulation of cancer-, apoptosis-, and metabolism-related genes underpinning the cancer-protective phenotype (PMC6627189).

**Suggested ontology terms:**
- **GO biological process:** GO:0060396 growth hormone receptor signaling pathway; GO:0007259 receptor signaling pathway via JAK-STAT; GO:0048009 IGF receptor signaling pathway; GO:0040007 growth; GO:0035556 intracellular signal transduction.
- **CL cell types:** CL:0000182 hepatocyte; CL:0000138 chondrocyte; CL:0000062 osteoblast; CL:0000136 adipocyte; CL:0000084 T cell (STAT5B subtype).
- **CHEBI:** CHEBI:37845 (somatotropin/GH); IGF-1 (peptide hormone); CHEBI for mecasermin/IGF-1 therapeutic.

*Sources:* [Guevara-Aguirre 2011, PMID:21325617](https://pubmed.ncbi.nlm.nih.gov/21325617/); [GHI beyond GHR (PMC7979432)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7979432/); [Genome-wide profiling (PMC6627189)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627189/).

---

## 7. Anatomical Structures Affected

- **Organ/system level:**
  - **Endocrine system** (primary) — GH–IGF-1 (somatotropic) axis; pituitary (GH hypersecretion), **liver** (principal failed IGF-1 source).
  - **Musculoskeletal system** — **growth plate / long bones** (UBERON:0006255 growth plate; UBERON:0002481 bone tissue), reduced bone mass, small hands/feet, limited joint extension, hip degeneration.
  - **Reproductive** — small genitalia/micropenis, delayed puberty.
  - **Integumentary** — thin skin, sparse hair.
  - **Body composition** — increased adipose tissue, reduced skeletal muscle.
  - **STAT5B subtype:** lungs (interstitial disease), immune organs.
- **Tissue/cell level:** growth-plate **chondrocytes** (CL:0000138), **osteoblasts** (CL:0000062), **hepatocytes** (CL:0000182), **adipocytes** (CL:0000136).
- **Subcellular level:** plasma membrane (GHR; GO:0005886); cytoplasm/JAK2 docking; nucleus (STAT5B-mediated transcription; GO:0005634).
- **Localization / lateralization:** systemic and **bilateral/symmetric** (a generalized endocrine signaling defect, not focal).

**Suggested UBERON terms:** UBERON:0006255 (growth plate); UBERON:0002107 (liver); UBERON:0000007 (pituitary gland); UBERON:0002481 (bone tissue); UBERON:0001013 (adipose tissue).

---

## 8. Temporal Development

- **Onset:** **congenital** (genetic) with **postnatal** clinical emergence. Birth length is near-normal; growth failure becomes evident within the **first 1–2 years**. Neonatal **hypoglycemia** and micropenis can present in the newborn period.
- **Onset pattern:** chronic/insidious for growth; episodic for hypoglycemia.
- **Progression / stages:** infancy (hypoglycemia, growth failure, hypotonia) → childhood (established severe short stature, characteristic facies) → adolescence (delayed puberty, eventual spontaneous but delayed sexual maturation) → adulthood (final short stature, central obesity, insulin sensitivity, osteopenia). Short stature is **permanent and non-progressive** once growth ceases; metabolic features evolve.
- **Course:** **chronic, lifelong, stable** (not relapsing-remitting). No spontaneous remission.
- **Critical window for intervention:** **early childhood**, before growth-plate fusion — rhIGF-1 therapy started young yields the greatest height benefit; benefit falls sharply after puberty/epiphyseal closure.

*Sources:* [OMIM #262500](https://omim.org/entry/262500); [Near-adult height IGFD registry, PMID:40626687](https://pubmed.ncbi.nlm.nih.gov/40626687/).

---

## 9. Inheritance and Population

**Epidemiology.**
- **Prevalence:** ultra-rare, estimated **~1–9 per 1,000,000**. Roughly **350 patients** described worldwide (with substantial under-diagnosis likely).
- **Geographic clustering:** two large founder cohorts — **southern Ecuador (~100 individuals, the world's largest cluster)** and **Israel/Mediterranean (~64–69 individuals)**; additional cases in Brazil, Chile, Mexico, and the broader Middle East. Genetic evidence links several New World/Mediterranean cohorts to a **common ancestral (likely Sephardic *converso*) origin**.

**Genetic transmission (classic GHR deficiency):**
- **Inheritance:** **autosomal recessive** (dominant GHI exists with dominant-negative *GHR* or *STAT5B* variants but is milder).
- **Penetrance:** essentially **complete** for biallelic LoF.
- **Expressivity:** **variable** (final height spans roughly −4 to −10 SDS depending on allele/genetic background).
- **Anticipation:** none (not a repeat-expansion disorder).
- **Germline mosaicism:** not a recognized feature.
- **Founder effects:** prominent — the Ecuadorian **E180 splice** allele and Mediterranean recurrent alleles.
- **Consanguinity:** a major driver of homozygosity and regional clustering.
- **Carrier frequency:** elevated only within founder/consanguineous populations; negligible in the general population.

**Demographics:**
- **Affected populations:** enriched in southern Ecuadorian, Sephardic/Mediterranean Jewish, Middle Eastern, and other consanguineous communities.
- **Sex ratio:** roughly **equal (1:1)** — autosomal; males are more clinically conspicuous (micropenis).
- **Age distribution:** diagnosed in **infancy/early childhood**; cohorts now include long-surviving adults.

*Sources:* [OMIM #262500](https://omim.org/entry/262500); [MedlinePlus](https://medlineplus.gov/genetics/condition/laron-syndrome/); [In Vivo 2016 clinical/molecular review](https://iv.iiarjournals.org/content/30/4/375); [Zvi Laron / cohort history (Healio)](https://www.healio.com/news/endocrinology/20120325/zvi-laron-md-the-man-behind-laron-syndrome).

---

## 10. Diagnostics

**Biochemical (the cornerstone):**
- **Low serum IGF-1** (often undetectable) with **normal or elevated basal GH** (LOINC: IGF-1 [e.g., 2484-4]; GH).
- **Failure of IGF-1 to rise on IGF-1 generation test** (GH stimulation) — the functional confirmatory test distinguishing GHI from GH deficiency.
- **Low IGFBP-3 and low ALS** (acid-labile subunit).
- **Low/absent GHBP** (growth hormone–binding protein) — supports an extracellular-domain *GHR* defect; **normal GHBP** points to transmembrane/intracellular or post-receptor (STAT5B) causes.
- Ancillary: fasting **hypoglycemia**, low fasting glucose with relatively high insulin sensitivity; elevated cholesterol in some.

**Imaging / functional:**
- **Bone-age radiograph** (delayed); skeletal survey shows thin cortices, small facial bones.
- DXA — osteopenia/low bone mass.
- Pituitary MRI typically **normal** (distinguishes from organic GH deficiency).

**Genetic testing (confirmatory):**
- **Single-gene *GHR* sequencing** (first-line when the phenotype/biochemistry is classic) including deletion/duplication analysis (MLPA) for whole/partial-gene deletions.
- **Targeted GHI/short-stature gene panel** (*GHR*, *STAT5B*, *IGFALS*, *IGF1*, *IGF1R*, *PAPPA2*) when GHBP is normal or features (immune dysregulation, microcephaly/deafness) suggest a downstream cause.
- **WES/WGS** for atypical/unsolved cases.
- Chromosomal microarray to exclude deletions overlapping *GHR*.

**Clinical criteria (Laron/consensus, simplified):** severe short stature (height ≤ −3 SDS) + low IGF-1 + normal/high GH + subnormal IGF-1 response to GH, with supportive low IGFBP-3/ALS/GHBP.

**Differential diagnosis:**
- **GH deficiency** (low GH *and* low IGF-1; responds to GH — opposite GH pattern).
- **Malnutrition / chronic illness / poorly controlled diabetes / hepatic disease** (acquired low IGF-1).
- **GH gene/biologically inactive GH** variants.
- **IGF-1 / IGF1R / IGFALS / PAPPA2 defects** (distinguished by panel + GHBP, IGFBP-3/ALS, IGF-1 levels — IGF1R defects show *high* IGF-1).
- **Secondary (acquired) GH insensitivity** — antibodies, systemic disease.

**Screening:** no population newborn screening; **cascade carrier testing** and prenatal/preimplantation genetic testing are offered in known founder families via genetic counseling.

*Sources:* [GHI beyond GHR (PMC7979432)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7979432/); [OMIM #262500](https://omim.org/entry/262500); [Brazilian series, PMC7197995](https://pmc.ncbi.nlm.nih.gov/articles/PMC7197995/).

---

## 11. Outcome / Prognosis

**Survival / mortality.** **Life expectancy is generally near-normal.** In the Ecuadorian cohort, lifespan is comparable to unaffected relatives; **accidents and alcohol-related deaths** (with structural vulnerability to falls) are leading causes — *not* cancer or cardiovascular disease.

> *"The individuals with GHR deficiency exhibited only one nonlethal malignancy and no cases of diabetes, in contrast to a prevalence of 17% for cancer and 5% for diabetes in control subjects."* — Guevara-Aguirre 2011 (PMID:21325617).

**Morbidity / function.** Untreated: severe short stature with attendant functional/psychosocial impact; obesity; osteopenia/fractures; hip degeneration. Cognition is **normal** in classic GHR deficiency. A striking feature is the **protective metabolic phenotype** — near-absence of type 2 diabetes and very low cancer incidence, attributed to lifelong low IGF-1/reduced pro-aging signaling; some data also suggest cognitive/memory advantages.

**Disease course / complications.** Hypoglycemia (infancy), obesity-related metabolic features (despite preserved insulin sensitivity), skeletal fragility; for the **STAT5B subtype**, immune complications (interstitial lung disease, recurrent infection, autoimmunity) can be life-threatening.

**Prognostic factors for growth outcome.** **Age at rhIGF-1 initiation** (earlier = better), baseline height SDS, genotype/residual signaling, treatment adherence, and pubertal status.

*Sources:* [Guevara-Aguirre 2011, PMID:21325617](https://pubmed.ncbi.nlm.nih.gov/21325617/); [Scientific American summary](https://www.scientificamerican.com/article/defective-growth-gene-in-dwarfism/); [USC memory study](https://gero.usc.edu/2017/01/25/people-with-growth-stunting-gene-have-a-sharper-memory/).

---

## 12. Treatment

**Pharmacotherapy — the mainstay: recombinant human IGF-1 (rhIGF-1, mecasermin / Increlex).**
- **Mechanism:** bypasses the receptor/signaling block by directly supplying IGF-1, restoring growth-plate signaling. **GH itself is ineffective** (the defect is GH resistance).
- **Regulatory status:** **FDA-approved** (2005) and EMA-approved for long-term treatment of growth failure in **severe primary IGF-1 deficiency (SPIGFD)**, including Laron syndrome. A combination product (mecasermin rinfabate, IGF-1 + IGFBP-3) was previously available.
- **Dosing:** twice-daily subcutaneous injection, titrated; **administer with meals** to avoid hypoglycemia.

> *"Mecasermin, recombinant human IGF-1, is … FDA-approved for the long-term treatment of growth failure in children with severe primary IGF-I deficiency (Laron syndrome)."* — NCBI/CADTH review.

- **Efficacy:** height velocity rises markedly in the first year (early trials: ~7.8–8.4 cm/yr in the first 6 months, PMID:8334752); real-world IGFD registry data confirm **improved near-adult height**, though gains are **less than in GH-treated GH-deficient children** and are blunted by late start (PMID:40626687). A 22-year Saudi cohort confirms long-term height benefit and safety.
- **Adverse events:** **hypoglycemia** (most important — dose with food), **lipohypertrophy** at injection sites, **tonsillar/adenoid hypertrophy**, intracranial hypertension, slipped capital femoral epiphysis, and theoretical long-term **neoplasia/IGF-1–driven** concerns (monitored). In trials, ~83% had ≥1 adverse event.

**Supportive / adjunctive care.**
- Treat/prevent **hypoglycemia** (frequent feeds in infancy).
- Manage **obesity and metabolic** features; monitor bone health.
- **Endocrine management** of puberty as needed.
- **STAT5B subtype:** management of immune dysregulation/interstitial lung disease (immunomodulation, infection prophylaxis).

**Surgical/interventional:** none disease-specific (orthopedic/hip management as needed).

**Experimental / future:** gene-axis–directed approaches and improved IGF-1 formulations are areas of interest; no gene therapy is established. (Search ClinicalTrials.gov for active SPIGFD/mecasermin studies.)

**Pharmacogenomics / personalized medicine:** genotype (GHR vs downstream gene) and GHBP status guide whether IGF-1 replacement (vs other approaches) is rational; IGF1R-defect patients respond poorly to IGF-1 (resistance, not deficiency).

**Suggested MAXO terms:** MAXO:0000058-type pharmacotherapy / hormone replacement therapy; MAXO:0000088 dietary intervention (hypoglycemia prevention); MAXO:0000079 genetic counseling; MAXO:0000950 supportive care. (Verify exact MAXO IDs with OAK before curation.) **CHEBI/therapeutic agent:** mecasermin (recombinant IGF-1) — bind via NCIT (e.g., NCIT mecasermin) if no CHEBI term.

*Sources:* [Mecasermin clinical/pharmacoeconomic reviews (NCBI Bookshelf NBK596664/NBK596662)](https://www.ncbi.nlm.nih.gov/books/NBK596664/); [Early rhIGF-1 trial, PMID:8334752](https://pubmed.ncbi.nlm.nih.gov/8334752/); [Near-adult height IGFD registry, PMID:40626687](https://pubmed.ncbi.nlm.nih.gov/40626687/); [22-year Saudi cohort (Karger, 2025)](https://karger.com/hrp/article/doi/10.1159/000543047/917874/Long-Term-Treatment-for-Laron-Syndrome-with-IGF-1); [NHS England mecasermin policy](https://www.england.nhs.uk/wp-content/uploads/2018/07/Mecasermin-for-treatment-of-growth-failure.pdf).

---

## 13. Prevention

- **Primary prevention:** not preventable (monogenic). **Genetic counseling** for at-risk/consanguineous families and known founder communities is the principal preventive measure; **carrier and cascade testing** identify at-risk couples.
- **Reproductive options:** **prenatal diagnosis** and **preimplantation genetic testing (PGT)** where the familial variant is known.
- **Secondary prevention (early detection):** prompt biochemical workup (IGF-1, GH, GHBP) in infants with early growth failure + hypoglycemia enables early diagnosis and timely rhIGF-1 initiation within the critical growth window.
- **Tertiary prevention (complication prevention):** dosing rhIGF-1 with meals to prevent hypoglycemia; metabolic/bone monitoring; for STAT5B subtype, infection prophylaxis and pulmonary surveillance.
- **Immunization / public health / environmental:** not applicable (no infectious or environmental etiology).

*Sources:* [MedlinePlus](https://medlineplus.gov/genetics/condition/laron-syndrome/); [GeneReviews/Orphanet genetic-counseling guidance].

---

## 14. Other Species / Natural Disease

- **Taxonomy:** humans (**NCBITaxon:9606**). The *GHR* gene and GH–IGF-1 axis are deeply conserved across vertebrates.
- **Orthologous genes:** *Ghr* in mouse (**NCBI Gene 14600**), rat, and other mammals; orthologs in zebrafish, chicken, cattle, etc.
- **Naturally occurring / engineered animal disease:**
  - **Mouse:** the **GHR-knockout ("Laron mouse," Ghr⁻/⁻)** is the canonical model — dwarfism, low IGF-1, high GH, obesity, **enhanced insulin sensitivity, reduced cancer, and extended lifespan** (one of the longest-lived laboratory mouse lines).
  - **Cattle/poultry:** GHR variants underlie growth/dwarf phenotypes (e.g., **sex-linked dwarfism in chickens** maps to *GHR*; bovine GHR polymorphisms affect stature/milk).
  - **Dogs/companion animals:** GH-axis growth disorders are recognized in veterinary endocrinology (OMIA catalogues GH/IGF-axis traits across species).
- **Comparative biology:** the conserved GH→JAK2/STAT5→IGF-1 cascade means model phenotypes (dwarfism + metabolic protection + longevity) **closely mirror human Laron syndrome**, making it a leading model for **aging and cancer-protection research** (the GH/IGF-1 longevity axis).
- **Transmission / zoonosis:** none (genetic, non-communicable).

**Suggested terms:** NCBITaxon:9606 (human), NCBITaxon:10090 (mouse); OMIA for veterinary GHR phenotypes; VBO for affected breeds (e.g., chicken dwarf lines).

*Sources:* [Guevara-Aguirre 2011, PMID:21325617 (links human to long-lived Ghr−/− mouse)](https://pubmed.ncbi.nlm.nih.gov/21325617/); comparative GH/IGF-1 longevity literature (e.g., Bartke/Coschigano Ghr-KO studies).

---

## 15. Model Organisms

- **Model types:** mammalian (mouse, rat), with cellular/in-vitro systems from patient-derived material; zebrafish and cattle/poultry for comparative growth genetics.
- **Flagship genetic model — the GHR-knockout / "Laron mouse" (Ghr⁻/⁻):**
  - **Types available:** global knockout, plus tissue-specific/conditional (e.g., **liver-specific** *Ghr* knockout to dissect hepatic IGF-1's role) and humanized/knock-in lines.
  - **Phenotype recapitulation (excellent):** proportionate dwarfism, **very low IGF-1, elevated GH**, increased adiposity, **enhanced insulin sensitivity**, **reduced cancer incidence**, and **markedly extended lifespan** — faithfully mirroring the human metabolic/longevity/cancer-protection phenotype.
  - **Limitations:** murine craniofacial/skeletal proportions and the human-specific psychosocial dimension are not captured; the dramatic murine **lifespan extension** is more pronounced than the (near-normal) human lifespan, so longevity translation must be made cautiously.
- **Patient-derived in vitro models:** Laron-serum and patient-cell assays demonstrated **reduced oxidative DNA damage and increased apoptosis** of stressed cells, and genome-wide profiling identified candidate cancer-protection pathways (PMC6627189) — key for the protective-phenotype mechanism.
- **Applications:** dissecting GH–IGF-1 signaling, **aging/longevity biology**, cancer chemoprevention, insulin sensitivity/diabetes, and rhIGF-1 pharmacology.
- **Resources/databases:** **MGI / IMPC / KOMP** (mouse *Ghr* alleles), **Alliance of Genome Resources**, **OMIA** (cross-species GHR phenotypes), Cellosaurus (patient cell lines).

*Sources:* [Guevara-Aguirre 2011, PMID:21325617](https://pubmed.ncbi.nlm.nih.gov/21325617/); [Genome-wide profiling of Laron patients (PMC6627189)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627189/); Bartke/Coschigano Ghr-KO longevity literature (MGI).

---

## Summary of Key Curation Anchors (for the dismech entry)

- **MONDO:** MONDO:0008638 · **OMIM:** #262500 · **Orphanet:** ORPHA:633 · **Category:** Mendelian (autosomal recessive).
- **Causal gene:** *GHR* (HGNC:4263); broader axis: *STAT5B, IGFALS, IGF1, IGF1R, PAPPA2*.
- **Central mechanism:** biallelic *GHR* LoF → failed **JAK2–STAT5B** signaling → **hepatic IGF-1 deficiency** with loss of GH negative feedback (high GH, low IGF-1) → growth-plate chondrocyte failure → severe postnatal short stature; plus a **protective metabolic phenotype** (low cancer/diabetes).
- **Biochemical signature for definitions block:** low IGF-1 + normal/high GH + subnormal IGF-1-generation response + low IGFBP-3/ALS ± low GHBP.
- **Treatment:** **rhIGF-1 (mecasermin)** replacement (MAXO pharmacotherapy / hormone replacement); GH is ineffective.
- **Landmark evidence PMIDs:** 21325617 (cancer/diabetes protection, *Sci Transl Med*), 8334752 (early rhIGF-1 efficacy), 40626687 (near-adult height registry), 21525302 (GHI continuum), plus STAT5B (PMC5974024) and cancer-protection pathways (PMC6627189).

---

### Sources
- [OMIM #262500 — Laron Syndrome](https://omim.org/entry/262500) · [OMIM *600946 — GHR](https://omim.org/entry/600946) · [OMIM #245590 — GHISID1 (STAT5B)](https://omim.org/entry/245590)
- [MedlinePlus Genetics: Laron syndrome](https://medlineplus.gov/genetics/condition/laron-syndrome/) · [NORD: Growth Hormone Insensitivity](https://rarediseases.org/rare-diseases/growth-hormone-insensitivity/)
- [Guevara-Aguirre et al., *Sci Transl Med* 2011 — PMID:21325617](https://pubmed.ncbi.nlm.nih.gov/21325617/)
- [Genetic Causes of GHI beyond GHR — PMC7979432](https://pmc.ncbi.nlm.nih.gov/articles/PMC7979432/) · [Genetic defects in the GH–IGF-I axis — PMC3356141](https://pmc.ncbi.nlm.nih.gov/articles/PMC3356141/)
- [Continuum of GHI abnormalities — PMID:21525302](https://pubmed.ncbi.nlm.nih.gov/21525302/) · [Dominant-negative STAT5B — PMC5974024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5974024/)
- [Genome-wide profiling of Laron patients — PMC6627189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627189/)
- [Early rhIGF-1 (Laron) trial — PMID:8334752](https://pubmed.ncbi.nlm.nih.gov/8334752/) · [Near-adult height IGFD registry — PMID:40626687](https://pubmed.ncbi.nlm.nih.gov/40626687/) · [22-year Saudi Laron cohort (Karger 2025)](https://karger.com/hrp/article/doi/10.1159/000543047/917874/Long-Term-Treatment-for-Laron-Syndrome-with-IGF-1)
- [Mecasermin clinical review — NCBI NBK596664](https://www.ncbi.nlm.nih.gov/books/NBK596664/) · [NHS England mecasermin policy](https://www.england.nhs.uk/wp-content/uploads/2018/07/Mecasermin-for-treatment-of-growth-failure.pdf)
- [Clinical & molecular features of Laron syndrome — In Vivo 2016](https://iv.iiarjournals.org/content/30/4/375) · [Brazilian Laron series — PMC7197995](https://pmc.ncbi.nlm.nih.gov/articles/PMC7197995/)
- [Zvi Laron / cohort history — Healio](https://www.healio.com/news/endocrinology/20120325/zvi-laron-md-the-man-behind-laron-syndrome) · [USC: memory advantage study](https://gero.usc.edu/2017/01/25/people-with-growth-stunting-gene-have-a-sharper-memory/) · [Scientific American](https://www.scientificamerican.com/article/defective-growth-gene-in-dwarfism/)

> **Curation caveats for dismech:** Per the project SOP, every PMID and snippet above must be re-verified with `just fetch-reference` and `just validate-references` before entry — treat this report as **leads, not ground truth**. In particular, confirm exact HPO/GO/CL/UBERON/MAXO/CHEBI IDs with OAK (`runoak ... info`), and run the **NEC preflight** against MONDO:0008638 (causal gene = *GHR*; OMIM 262500) given the GHI/Laron name-and-synonym overlap with the downstream-gene GHI subtypes. Frequency bands (Frequent/Occasional) are qualitative estimates here and need their own quantitative evidence before being committed with a `frequency:` value.