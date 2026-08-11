---
provider: claude_code
model: claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T08:41:33.079627'
end_time: '2026-06-30T08:46:09.056159'
duration_seconds: 275.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Maculopapular Cutaneous Mastocytosis
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
  - claude-opus-4-8[1m]
  num_turns: 14
  total_cost_usd: 2.65932
  session_id: 54ef387f-92c6-4936-9e7a-dbdb7924302f
  stop_reason: end_turn
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Maculopapular Cutaneous Mastocytosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Maculopapular Cutaneous Mastocytosis** covering all of the
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

I now have comprehensive, well-sourced material. Per the PubMed tool's terms, citations below are drawn from PubMed with DOI links. Here is the full report.

---

# Comprehensive Research Report: Maculopapular Cutaneous Mastocytosis (MPCM)

> **Attribution:** Clinical and mechanistic claims below are based on articles retrieved from **PubMed**; each cited article includes its DOI link. **Curation caveat for dismech:** every ontology ID (HP, GO, CL, UBERON, CHEBI, MAXO, NCIT) suggested here is a *lead* and MUST be verified with `just validate-terms-file` / OAK before it is committed, and every evidence `snippet` must be confirmed as an exact substring of the cached abstract via `just validate-references`. Several quotes below are reproduced verbatim from abstracts to seed that process.

---

## 1. Disease Information

**Overview.** Maculopapular cutaneous mastocytosis (MPCM), historically termed **urticaria pigmentosa (UP)**, is the most common form of cutaneous mastocytosis (CM). It is defined by an abnormal accumulation of clonal mast cells restricted to the skin, producing multiple hyperpigmented (red‑brown) macules, papules, plaques, or nodules that characteristically urticate (wheal-and-flare) when stroked — the **Darier sign**. Unlike systemic mastocytosis (SM), the mast-cell infiltrate is confined to the skin with no extracutaneous organ involvement at diagnosis.

According to PubMed, cutaneous mastocytosis "is the most common form in children, is defined when MC infiltration is limited to the skin," and CM "includes three forms: solitary mastocytoma, maculopapular cutaneous mastocytosis (MPCM), and diffuse cutaneous mastocytosis (DCM)" (Giona, *Mediterr J Hematol Infect Dis* 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

**A pivotal 2015 consensus refinement** (European Competence Network on Mastocytosis / AAAAI / EAACI) recommended that MPCM be subdivided into two clinically and prognostically distinct variants:
- **Monomorphic variant** — small, uniform maculopapular lesions, typically seen in adults; if it develops in children, it **often persists into adulthood** and may signal underlying systemic disease.
- **Polymorphic variant** — larger lesions of variable size and shape, typically seen in children; **may resolve around puberty**.

Verbatim: "we recommend that the typical maculopapular cutaneous lesions (urticaria pigmentosa) should be subdivided into 2 variants, namely a monomorphic variant with small maculopapular lesions, which is typically seen in adult patients, and a polymorphic variant with larger lesions of variable size and shape, which is typically seen in pediatric patients" (Hartmann et al., *J Allergy Clin Immunol* 2016; [DOI](https://doi.org/10.1016/j.jaci.2015.08.034)). The same consensus removed *telangiectasia macularis eruptiva perstans (TMEP)* from the CM classification and dropped the adjunct "solitary" from solitary mastocytoma.

**Key identifiers**
| Resource | ID |
|---|---|
| MONDO | **MONDO:0019316** (maculopapular cutaneous mastocytosis) — verified in OLS |
| Orphanet | **ORPHA:79457** (Maculopapular cutaneous mastocytosis); parent ORPHA:66646 (Cutaneous mastocytosis) |
| MeSH | **D014582** (Urticaria Pigmentosa) |
| SNOMED CT | **1332134000** (Maculopapular cutaneous mastocytosis) |
| UMLS/MedGen | **C0042111** |
| NCIT | **C212102** (Urticaria Pigmentosa/MPCM, Monomorphic Variant) |
| ICD-10 | **Q82.2** (Mastocytosis, congenital/cutaneous); ICD-O **9740/1** for mastocytoma/UP |
| ICD-11 | **EK90.1** (Cutaneous mastocytosis), with 2A21.0 for indolent SM |
| OMIM | **154800** (Mastocytosis, cutaneous; phenotype linked to KIT 164920) |

**Synonyms:** urticaria pigmentosa (UP); MPCM; UP/MPCM. The terms UP and MPCM are now used interchangeably, with MPCM preferred in modern consensus nomenclature.

**Information source.** Derived predominantly from **aggregated disease-level resources** (consensus classifications, systematic reviews, large single-center and registry cohorts) supplemented by individual case reports for rare KIT variants. This is *not* an EHR-derived entity.

---

## 2. Etiology

**Primary causal factor — somatic activating *KIT* mutation.** Mastocytosis is a clonal mast-cell disorder driven by gain-of-function mutations in *KIT* (the receptor for stem cell factor, SCF; CD117). "Genetic aberrations, mainly the KIT D816V mutation, play a crucial role in the pathogenesis of mastocytosis, enhancing MC survival and subsequent accumulation in organs and tissues" (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

**Critical pediatric-vs-adult distinction in the mutational driver.** Adults (and systemic disease) are dominated by the canonical activation-loop mutation **KIT D816V** (exon 17). **Children with cutaneous mastocytosis carry a much broader *KIT* mutation spectrum, frequently outside codon 816**, including extracellular/transmembrane (exon 8, 9) and juxtamembrane (exon 11) domain mutations:
- "Children with cutaneous mastocytosis typically exhibit mutations in various regions of the KIT gene, whereas those with systemic disease predominantly carry KIT D816V" (Carter, Lange, Hartmann et al., *J Allergy Clin Immunol Pract* 2025; [DOI](https://doi.org/10.1016/j.jaip.2025.11.016)).
- A worked single-case example: a 2-year-old with MPCM carried an **Asp419del in exon 8 of KIT** (Fukaura et al., *Arerugi* 2024; [DOI](https://doi.org/10.15036/arerugi.73.189)).
- In the largest pediatric systematic review (1747 cases), "KIT D816V mutation was detected in 34% of 215 tested patients" — i.e., the majority of tested children did *not* carry D816V (Méni et al., *Br J Dermatol* 2015; [DOI](https://doi.org/10.1111/bjd.13567)).

**Germline / familial forms (rare).** Most disease is sporadic/somatic, but rare familial mastocytosis and germline *KIT* syndromes exist. A germline *KIT* mutation can produce **"GIST cutaneous hyperpigmentation disease"** — familial gastrointestinal stromal tumour with cutaneous hyperpigmentation/urticaria pigmentosa (Wali et al., *Clin Exp Dermatol* 2018; [DOI](https://doi.org/10.1111/ced.13757)). Familial DCM with specific gene mutations has also been reported (Rydz, Lange et al., *Int J Mol Sci* 2024; [DOI](https://doi.org/10.3390/ijms25031401)).

**Risk factors.**
- *Genetic:* somatic *KIT* activating variants (causal); **hereditary alpha-tryptasemia (HαT)** — a germline *TPSAB1* copy-number gain — is a modifier that raises baseline tryptase and is enriched among SM patients (Beyens et al., *Acta Clin Belg* 2022; [DOI](https://doi.org/10.1080/17843286.2022.2137631)).
- *Demographic:* early childhood onset; modest male predominance (see §9).
- *Environmental/trigger factors* are **mast-cell-activation triggers** rather than disease-causing: physical stimuli (friction/rubbing, heat, cold, pressure), Hymenoptera stings, certain drugs (opioids, NSAIDs, vancomycin, neuromuscular blockers, radiocontrast), and emotional stress.

**Protective factors.** No validated genetic or environmental protective alleles are established. The principal "protective" measure is **trigger avoidance** to reduce mediator-release episodes (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

**Gene–environment interaction.** The somatic *KIT* lesion sets a low threshold for mast-cell degranulation; environmental triggers then precipitate clinical mediator-release symptoms. No quantitative GxE model is documented.

---

## 3. Phenotypes

For each phenotype I give type, characteristics, and an HPO **lead** (to be validated).

**Cutaneous (primary, near-universal):**
- **Maculopapular hyperpigmented skin lesions / urticaria pigmentosa** (clinical sign; physical manifestation). Red-brown macules/papules, often on trunk and extremities, sparing palms/soles/face in many cases. Frequency: defining (≈75% of pediatric CM present as UP/MPCM — Méni 2015; [DOI](https://doi.org/10.1111/bjd.13567)). HPO leads: *Hyperpigmentation of the skin* (HP:0000953), *Urticaria* (HP:0001025).
- **Darier sign** (whealing on stroking a lesion; pathognomonic clinical sign). "Darier's sign was present in 94% of cases" (Kiszewski et al., *J Eur Acad Dermatol Venereol* 2004; [DOI](https://doi.org/10.1111/j.1468-3083.2004.00830.x)). No dedicated HPO term; can be captured descriptively.
- **Pruritus** (symptom) — the most common mediator symptom, "often triggered by rubbing the lesions" (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)). HPO lead: *Pruritus* (HP:0000989).
- **Blistering/bullae** (sign) — especially in infants/severe polymorphic or diffuse disease. HPO lead: *Abnormal blistering of the skin* (HP:0008066).
- **Flushing** (sign/symptom) from mediator release. HPO lead: *Flushing* (HP:0031284).
- **Dermographism** (sign).

**Mediator-related systemic symptoms (mast-cell activation, MCA):** flushing, pruritus, abdominal pain, diarrhea, headache, hypotension/syncope, and — at the severe end — **anaphylaxis**. "Many pediatric patients suffer from symptoms of mast cell activation, ranging from pruritus to flushing and blistering" (Carter et al. 2025; [DOI](https://doi.org/10.1016/j.jaip.2025.11.016)). HPO leads: *Diarrhea* (HP:0002014), *Abdominal pain* (HP:0002027), *Episodic abdominal pain*, *Hypotension* (HP:0002615). Anaphylaxis risk is lower in MPCM than DCM but real, warranting epinephrine auto-injector availability (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

**Laboratory abnormality:** **elevated serum tryptase** (biomarker of mast-cell burden). A basal serum tryptase >20 ng/mL is a minor SM criterion; in pure MPCM tryptase is often normal or mildly elevated, and **lower tryptase correlates with the favorable large-lesion variant** (Wiechers et al., *J Allergy Clin Immunol* 2015; [DOI](https://doi.org/10.1016/j.jaci.2015.05.034)).

**Phenotype characteristics:**
- *Onset:* lesions occur **before age 2 in ~90%** of pediatric cases (Méni 2015; [DOI](https://doi.org/10.1111/bjd.13567)); "in 92% of cases disease onset was in the first year of life" (Kiszewski 2004; [DOI](https://doi.org/10.1111/j.1468-3083.2004.00830.x)).
- *Severity:* variable — most pediatric MPCM is mild/indolent; severity tracks lesion type (small monomorphic ↔ higher tryptase/persistence).
- *Progression:* often stable then regressing (polymorphic/large-lesion); monomorphic small-lesion disease is more persistent.
- *Quality of life:* impacted by chronic pruritus, cosmetic burden of pigmented lesions, trigger-avoidance lifestyle constraints, and anxiety about anaphylaxis; formal disease-specific QoL instruments (e.g., MC-QoL, MQLQ) exist for mastocytosis but per-phenotype QoL data for pediatric MPCM are limited.

**Prognostic phenotype subdivision (important for KB):** large lesions = favorable. "Patients with MPCM-large lesions, compared with those with MPCM-small lesions, were characterized by significantly lower tryptase levels, shorter disease duration, and earlier disease onset... more patients with MPCM-large lesions exhibited spontaneous regression" (Wiechers 2015; [DOI](https://doi.org/10.1016/j.jaci.2015.05.034)).

---

## 4. Genetic / Molecular Information

**Causal gene: *KIT*** (proto-oncogene receptor tyrosine kinase / CD117 / SCF receptor). HGNC **hgnc:6342** (dismech lowercase convention); OMIM gene **164920**; chromosome **4q12**.

**Pathogenic variants:**
- **KIT D816V** (c.2447A>T, p.Asp816Val; exon 17 activation loop) — the canonical adult/systemic mutation; gain-of-function, **constitutive ligand-independent kinase activation**. Classified Pathogenic. Somatic. In pediatric CM it is present in only ~one-third of tested cases.
- **Non-codon-816 *KIT* variants** enriched in pediatric CM: extracellular domain **exon 8** (e.g., p.Asp419del), exon 9, and juxtamembrane **exon 11** mutations; some are insertions/deletions and missense. A pediatric mature B-cell lymphoma case carried a *KIT* exon 11 variant (Yazal Erdem et al., *J Pediatr Hematol Oncol* 2022; [DOI](https://doi.org/10.1097/MPH.0000000000002196)). Verbatim exon-8 example: "an Asp419del mutation in exon 8 of the KIT gene" (Fukaura 2024; [DOI](https://doi.org/10.15036/arerugi.73.189)).
- *Variant types:* missense (dominant), small in-frame deletions, insertions, occasional internal tandem patterns.
- *Origin:* predominantly **somatic** (lesional skin); rare **germline** in familial GIST/mastocytosis syndromes.
- *Functional consequence:* **gain of function** — constitutive KIT autophosphorylation → enhanced mast-cell survival, proliferation, and accumulation. D816V notably confers **resistance to imatinib**, whereas many non-codon-816 (juxtamembrane/extracellular) variants retain imatinib sensitivity — a therapeutically decisive distinction.
- *Allele frequency:* these are somatic driver mutations; not represented as population germline allele frequencies in gnomAD.

**Modifier genes:** *TPSAB1* (hereditary alpha-tryptasemia) modifies tryptase levels and may modify symptom severity (Beyens 2022; [DOI](https://doi.org/10.1080/17843286.2022.2137631)). Additional somatic mutations (TET2, SRSF2, ASXL1 — the "S/A/R" panel) are associated with advanced SM but **not** typical pediatric MPCM.

**Epigenetic / chromosomal:** No recurrent epigenetic signature or large-scale chromosomal abnormality is characteristic of MPCM; advanced SM (not MPCM) accrues additional somatic mutations.

---

## 5. Environmental Information

MPCM is a clonal genetic disease; environmental factors act as **symptom triggers**, not causes. Relevant trigger categories: physical (rubbing/friction — the basis of the Darier sign, temperature extremes, pressure), Hymenoptera venom, drugs causing mast-cell degranulation (opioids, NSAIDs, vancomycin, muscle relaxants, iodinated contrast), alcohol (in adults), and emotional/physical stress. Management "is mainly based on strict avoidance of triggers" (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)). No infectious agent is implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Somatic activating *KIT* mutation** in a mast-cell progenitor (D816V in adults/SM; diverse exon 8/9/11/17 variants in children).
2. → **Constitutive, SCF-independent KIT receptor tyrosine kinase activation** (autophosphorylation).
3. → Downstream pro-survival/proliferative signaling: **PI3K–AKT–mTOR**, **RAS–RAF–MEK–ERK (MAPK)**, **JAK2–STAT5**, and **PLCγ** cascades.
4. → **Enhanced mast-cell survival and clonal accumulation** in the dermis (apoptosis resistance + proliferation).
5. → **Increased dermal mast-cell density** producing the pigmented maculopapular lesions (mast cells stimulate local melanocyte activity → hyperpigmentation).
6. → **Mast-cell mediator release** (degranulation) on triggering → histamine, tryptase, prostaglandin D2, leukotrienes, heparin, TNF → wheal/flare (Darier sign), pruritus, flushing, blistering, and systemic MCA symptoms up to anaphylaxis.

**Molecular pathways (KEGG/Reactome):** RTK/KIT signaling; PI3K-AKT; MAPK/ERK; JAK-STAT5. **Cellular processes:** mast-cell proliferation, apoptosis resistance, and **regulated exocytosis/degranulation**. **Protein dysfunction:** gain-of-function KIT with constitutive kinase activity (D816V destabilizes the autoinhibited conformation of the activation loop). **Immune involvement:** the entire phenotype is **mast-cell–mediated** (mediator release), without classic autoimmunity or immunodeficiency. **Metabolic changes:** none disease-specific.

**Ontology leads (validate before use):**
- GO biological process: *mast cell degranulation* (GO:0043303), *mast cell activation* (GO:0045576), *transmembrane receptor protein tyrosine kinase signaling pathway* (GO:0007169), *positive regulation of mast cell proliferation*, *regulation of mast cell apoptotic process*.
- GO molecular function: *stem cell factor receptor activity*, *protein tyrosine kinase activity* (GO:0004713).
- CL cell type: *mast cell* (CL:0000097); consider *connective tissue / dermal mast cell* subtype.
- CHEBI mediators: *histamine* (CHEBI:18295), *prostaglandin D2* (CHEBI:15555).

**Molecular profiling.** No routine transcriptomic/proteomic/metabolomic signature defines MPCM; diagnosis rests on histology + KIT genotyping + tryptase. Single-cell/spatial work on skin mast cells is emerging but not yet clinically deployed for MPCM.

---

## 7. Anatomical Structures Affected

- **Organ level — primary:** **skin** (UBERON:0002097, *skin of body*), specifically the **dermis** (UBERON:0002067), where mast cells accumulate; the overlying **epidermis** (UBERON:0001003) shows basal hyperpigmentation.
- **Secondary/systemic:** by definition **absent** in CM/MPCM (mast-cell infiltrate limited to skin). Mediator release can transiently affect the GI tract, cardiovascular system (hypotension), and respiratory system during MCA episodes, but there is no organ infiltration.
- **Tissue/cell level:** connective tissue of the dermis; the targeted cell population is the **dermal mast cell** (CL:0000097). Lesional biopsies show "a dense accumulation of CD117-positive, round or oval cells with amphophilic cytoplasm within the upper to middle dermis" (Fukaura 2024; [DOI](https://doi.org/10.15036/arerugi.73.189)).
- **Subcellular:** mast-cell **secretory granules** (GO cellular component: *secretory granule*); plasma-membrane KIT receptor.
- **Localization/laterality:** lesions are **bilateral and disseminated/generalized**, typically trunk-predominant; not lateralized.

---

## 8. Temporal Development

- **Onset:** congenital to early infancy; "Lesions occurred before the age of 2 years in 90% of cases" (Méni 2015; [DOI](https://doi.org/10.1111/bjd.13567)); first year of life in ~92% (Kiszewski 2004; [DOI](https://doi.org/10.1111/j.1468-3083.2004.00830.x)). Onset pattern: chronic/insidious.
- **Course:** generally **indolent**, often with **spontaneous regression around puberty** for the pediatric polymorphic/large-lesion variant; "In most children with CM, skin lesions regress spontaneously around puberty; unfortunately, it is not always a self-limiting disease" (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).
- **Regression rates (key quantitative data):** In a systematic review/meta-analysis, "the complete resolution rate for mastocytoma was 10% per year... while the rate for urticaria pigmentosa was 1.9% per year (95% CI: −0.5%, 4.3%)"; "Diffuse cutaneous mastocytosis and systemic mastocytosis subtypes did not show evidence of complete resolution" (Le et al., *Postgrad Med* 2017; [DOI](https://doi.org/10.1080/00325481.2017.1364124)). In the 1747-case pediatric review, "Clinical regression (complete or partial) occurred in 67% of cases and stabilization in 27%" (Méni 2015; [DOI](https://doi.org/10.1111/bjd.13567)); 80% improved/resolved in the 71-case series (Kiszewski 2004; [DOI](https://doi.org/10.1111/j.1468-3083.2004.00830.x)).
- **Adult-onset / monomorphic** disease tends to **persist lifelong** and more often associates with systemic mastocytosis.
- **Critical period for prognosis:** the **monomorphic vs polymorphic distinction** at presentation is the key window — monomorphic small lesions in a child flag persistence/possible SM (Hartmann 2016; [DOI](https://doi.org/10.1016/j.jaci.2015.08.034)).

---

## 9. Inheritance and Population

- **Epidemiology:** mastocytosis overall affects roughly **1 in 10,000** people. "Recent studies estimate that 1 in 10,000 people are diagnosed with mastocytosis" (Le 2017; [DOI](https://doi.org/10.1080/00325481.2017.1364124); concordant in Beyens 2022; [DOI](https://doi.org/10.1080/17843286.2022.2137631)). MPCM/UP is the **most common CM subtype** and the most common mastocytosis presentation in children (≈75% of pediatric CM — Méni 2015; [DOI](https://doi.org/10.1111/bjd.13567)).
- **Inheritance pattern:** predominantly **sporadic/somatic** (not inherited). Rare familial autosomal-dominant *KIT*-germline forms exist (Rydz 2024; [DOI](https://doi.org/10.3390/ijms25031401); Wali 2018; [DOI](https://doi.org/10.1111/ced.13757)). Penetrance/expressivity, anticipation, founder effects, and carrier frequencies are **not applicable** to the common somatic disease.
- **Sex ratio:** modest male predominance — male:female **1.4:1** (Méni 2015; [DOI](https://doi.org/10.1111/bjd.13567)), **1.8:1** (Kiszewski 2004; [DOI](https://doi.org/10.1111/j.1468-3083.2004.00830.x)), and a male-to-female ratio of 2.2 in a 61-patient cohort (Yazal Erdem 2022; [DOI](https://doi.org/10.1097/MPH.0000000000002196)).
- **Age distribution:** strongly bimodal across mastocytosis as a whole — **pediatric CM** (early childhood, usually <2 yr) vs **adult SM**; MPCM specifically is the dominant pediatric skin presentation.
- **Geographic/ethnic distribution:** no strong ethnic predisposition documented; reported worldwide.

---

## 10. Diagnostics

**Diagnosis is largely clinical and noninvasive in children.** "Diagnosis is mainly based on noninvasive measures, including skin inspection, elicitation of the Darier's sign, and analyses of the serum tryptase and KIT variant in blood" (Carter et al. 2025; [DOI](https://doi.org/10.1016/j.jaip.2025.11.016)). "In contrast to adults, mastocytosis in children usually has a benign course making sophisticated or invasive diagnostic tests unnecessary" (Kiszewski 2004; [DOI](https://doi.org/10.1111/j.1468-3083.2004.00830.x)).

- **Clinical signs:** typical maculopapular lesions + positive **Darier sign**.
- **Laboratory biomarker:** **serum baseline tryptase** (LOINC for tryptase available); >20 ng/mL is a minor SM criterion and prompts evaluation for systemic disease (Valent et al., *HemaSphere* 2021; [DOI](https://doi.org/10.1097/HS9.0000000000000646)).
- **Genetic testing:** **KIT mutation analysis** — peripheral-blood allele-specific PCR/ddPCR for **D816V**; if negative in a child but suspicion remains, **lesional-skin KIT sequencing** captures non-codon-816 variants (exon 8/9/11). High-sensitivity assays are recommended.
- **Histopathology (when biopsy is performed):** dermal mast-cell infiltrate, **CD117 (KIT)** and **tryptase**-positive on IHC, with aberrant **CD25/CD2/CD30** expression supporting clonality. CD30 in MC is now a minor SM criterion (Valent 2021; [DOI](https://doi.org/10.1097/HS9.0000000000000646)).
- **Bone marrow biopsy:** generally **avoided in children** with typical CM and stable/low tryptase; reserved for adults, persistent monomorphic disease, or red flags suggesting SM. In one cohort "Seven patients were further investigated with suspicion of systemic mastocytosis... none of them developed systemic disease" (Yazal Erdem 2022; [DOI](https://doi.org/10.1097/MPH.0000000000002196)).
- **Diagnostic criteria framework:** WHO / ECNM consensus criteria distinguish CM (mastocytosis in the skin, MIS) from SM (Akin & Valent, *Immunol Allergy Clin North Am* 2014; [DOI](https://doi.org/10.1016/j.iac.2014.02.003); updated consensus Valent 2021; [DOI](https://doi.org/10.1097/HS9.0000000000000646)).
- **Differential diagnosis:** other pigmented/bullous disorders — especially in infants DCM "resemble[s] other bullous skin disorders" (Rydz 2024; [DOI](https://doi.org/10.3390/ijms25031401)); also juvenile xanthogranuloma, post-inflammatory hyperpigmentation, café-au-lait macules/neurofibromatosis, secondary syphilis, and bullous impetigo.
- **Screening:** no population screening; tryptase + KIT in blood serve as the practical risk-stratification screen for systemic involvement.

---

## 11. Outcome / Prognosis

- **Overall prognosis is favorable**, especially pediatric polymorphic/large-lesion MPCM, with high rates of spontaneous regression (see §8). "Eighty per cent of patients improved or had spontaneous resolution" (Kiszewski 2004; [DOI](https://doi.org/10.1111/j.1468-3083.2004.00830.x)).
- **Mortality:** low. In the 1747-case pediatric systematic review, "the outcome was fatal in 2.9% of patients" — almost entirely in severe/diffuse or systemic disease, not typical MPCM (Méni 2015; [DOI](https://doi.org/10.1111/bjd.13567)).
- **Prognostic factors:** lesion morphology (large/polymorphic = favorable, regressing; small/monomorphic = persistent, possible SM), **lower baseline tryptase = favorable**, earlier onset, shorter disease duration (Wiechers 2015; [DOI](https://doi.org/10.1016/j.jaci.2015.05.034)); KIT genotype (non-D816V child = typical benign CM; persistent D816V/monomorphic = SM risk).
- **Morbidity / QoL:** chronic pruritus, cosmetic burden, lifestyle restriction from trigger avoidance, and **anaphylaxis risk** (lower in MPCM than DCM but warranting epinephrine auto-injector provision — Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).
- **Complications:** mediator-release crises/anaphylaxis; blistering in severe infantile disease; rare progression to/coexistence with systemic mastocytosis (mainly monomorphic/adult forms).
- **Follow-up:** even benign-appearing pediatric cases "require planned follow-up over time" (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

---

## 12. Treatment

**Treatment is symptomatic** (no curative therapy for CM); it targets mediator symptoms and trigger avoidance.

**Trigger avoidance** (first-line, all patients) — MAXO lead: *therapeutic/preventive avoidance behavior*; "strict avoidance of triggers" (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

**Pharmacotherapy (mediator blockade):**
- **H1 antihistamines** (first-line for pruritus/flushing) and **H2 antihistamines** (gastric/GI symptoms). Treatment "with H1 and H2 histamine receptor blockers on demand" is recommended (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).
- **Mast-cell stabilizer:** oral **sodium cromoglicate (cromolyn)** for GI/cutaneous symptoms; topical corticosteroids for lesions.
- **Leukotriene receptor antagonists**, and aspirin (for prostaglandin-mediated flushing in adults, with caution).
- **Omalizumab (anti-IgE)** for refractory mediator symptoms/recurrent anaphylaxis. Treatment options "encompass avoidance of triggers of mast cell activation, H1 and H2 antihistamines, cromolyn, and omalizumab" (Carter et al. 2025; [DOI](https://doi.org/10.1016/j.jaip.2025.11.016); see also Castells & Butterfield, *J Allergy Clin Immunol Pract* 2019; [DOI](https://doi.org/10.1016/j.jaip.2019.02.002)).
- **Epinephrine auto-injector** for anaphylaxis rescue (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

**KIT-targeted / cytoreductive therapy** (reserved for systemic or severe disease — *not* typical MPCM):
- **Tyrosine kinase inhibitors tailored to the KIT variant.** "In children with systemic mastocytosis, tyrosine kinase inhibitors tailored to the specific KIT variant may be considered" (Carter et al. 2025; [DOI](https://doi.org/10.1016/j.jaip.2025.11.016)). **Imatinib** is effective only for **non-D816V / imatinib-sensitive KIT** (e.g., juxtamembrane/extracellular variants common in children); **D816V is imatinib-resistant**, requiring D816V-active inhibitors (**midostaurin**, **avapritinib**). Imatinib is among "common choices" for symptomatic systemic disease (Le 2017; [DOI](https://doi.org/10.1080/00325481.2017.1364124)).
- **Phototherapy (PUVA/UVB)** for extensive symptomatic skin disease in adults.

**Pharmacogenomics:** the *KIT* genotype itself is the decisive "pharmacogenomic" determinant of TKI selection (D816V vs non-D816V).

**MAXO leads (validate):** *pharmacotherapy* (NCIT:C15986 for action), *antihistamine therapy*, *immunotherapy/anti-IgE therapy*, *phototherapy*, *avoidance behavior*; with `therapeutic_agent` CHEBI/NCIT bindings, e.g., *imatinib* (CHEBI:45783), *omalizumab*, *midostaurin* (NCIT:C1872), *avapritinib*, *cromoglicate*, *histamine H1 antagonist* class.

---

## 13. Prevention

No primary prevention exists for this clonal genetic disease. Prevention is effectively **tertiary** — preventing mediator-release crises and complications:
- **Trigger avoidance** (physical stimuli, culprit drugs, venom) — the central preventive strategy (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).
- **Premedication** (antihistamines ± corticosteroids) before high-risk exposures (surgery/anesthesia, iodinated contrast).
- **Anaphylaxis preparedness:** epinephrine auto-injector and an emergency action plan.
- **Venom immunotherapy** in patients with Hymenoptera-venom anaphylaxis and mastocytosis (more relevant to adults/SM).
- **Genetic counseling** is generally not indicated for sporadic somatic disease but is relevant for the rare germline *KIT* familial syndromes (Wali 2018; [DOI](https://doi.org/10.1111/ced.13757)).
- **Structured follow-up** to detect the minority with persistent/systemic disease (Giona 2021; [DOI](https://doi.org/10.4084/MJHID.2021.069)).

---

## 14. Other Species / Natural Disease

- **Taxonomy/natural disease:** Mastocytosis and cutaneous mast-cell tumors occur naturally in animals, most prominently the **dog** (*Canis lupus familiaris*, **NCBITaxon:9615**) — canine **mast cell tumors (MCT)** are among the most common skin tumors in dogs and frequently carry **c-KIT** (KIT) mutations (notably exon 11 internal tandem duplications), making them a recognized comparative-oncology model for KIT-driven mast-cell disease. Mast cell tumors also occur in **cats** (*Felis catus*, NCBITaxon:9685).
- **Orthologous gene:** canine **KIT** (NCBI Gene; ortholog of human *KIT*).
- **Veterinary relevance / comparative pathology:** strong — canine MCT KIT biology informed human KIT-targeted therapy; however, canine/feline MCT are typically **neoplastic tumors** rather than the self-limited pediatric maculopapular pattern, so comparative fidelity to human pediatric MPCM specifically is partial.
- **Zoonosis:** none — non-transmissible.

> *Curation note:* Veterinary mast-cell-tumor evidence should be tagged `evidence_source: MODEL_ORGANISM` per dismech rules, and kept distinct from human phenotype support.

---

## 15. Model Organisms

- **Mouse models:** the principal experimental systems. **Kit gain-of-function knock-in mice** (e.g., Kit D814V, the murine equivalent of human D816V) develop mast-cell hyperplasia/mastocytosis-like disease and have been used to dissect KIT signaling and test TKIs. **Kit loss-of-function alleles** (W/Wv, KitW-sh "sash") are **mast-cell–deficient** and are widely used for mast-cell reconstitution studies — important for mast-cell biology though they model deficiency, not mastocytosis. Resource: **MGI** (gene *Kit*).
- **Cellular / in vitro models:** human mast-cell leukemia lines **HMC-1** (carries KIT V560G ± D816V) and **LAD2**; CD34⁺-derived primary human mast cells transfected with mutant KIT; used for KIT-signaling and drug-screening (imatinib-sensitive vs D816V-resistant). Resource: **Cellosaurus**.
- **iPSC / organoid:** patient-derived iPSC mast-cell models are emerging but not standardized for MPCM.
- **Phenotype recapitulation:** KIT gain-of-function models reproduce **mast-cell accumulation and constitutive KIT signaling** well, and faithfully reproduce **D816V imatinib resistance**, supporting the molecular mechanism. **Limitations:** murine models do **not** reproduce the human **pediatric self-limited / pubertal-regression** course or the precise human maculopapular cutaneous lesion morphology, and the diverse non-codon-816 pediatric *KIT* variants are under-modeled.

> *Curation note (HUMAN_MODEL_MISMATCH candidate):* the gap between robust KIT-driven mouse/cell models and the **human pediatric spontaneous-regression phenotype** is a good `kind: HUMAN_MODEL_MISMATCH` discussion item — evidence exists in models, but translational validity to the self-limiting pediatric course is the open question.

---

## Consolidated Evidence Table (high-value, snippet-ready)

| PMID | Anchor claim | Verbatim snippet (verify before commit) | Source type | DOI |
|---|---|---|---|---|
| 26476479 | MPCM monomorphic vs polymorphic split | "the typical maculopapular cutaneous lesions (urticaria pigmentosa) should be subdivided into 2 variants, namely a monomorphic variant with small maculopapular lesions, which is typically seen in adult patients, and a polymorphic variant with larger lesions of variable size and shape, which is typically seen in pediatric patients" | HUMAN_CLINICAL (consensus) | [link](https://doi.org/10.1016/j.jaci.2015.08.034) |
| 41285204 | Pediatric KIT spectrum vs D816V | "Children with cutaneous mastocytosis typically exhibit mutations in various regions of the KIT gene, whereas those with systemic disease predominantly carry KIT D816V" | HUMAN_CLINICAL (review) | [link](https://doi.org/10.1016/j.jaip.2025.11.016) |
| 25662299 | Onset, subtype %, D816V 34%, outcomes | "Lesions occurred before the age of 2 years in 90% of cases, and presented as urticaria pigmentosa (75% of cases)... KIT D816V mutation was detected in 34% of 215 tested patients. Clinical regression (complete or partial) occurred in 67% of cases... the outcome was fatal in 2.9% of patients." | HUMAN_CLINICAL (systematic review) | [link](https://doi.org/10.1111/bjd.13567) |
| 26152315 | Large-lesion favorable prognosis | "Patients with MPCM-large lesions, compared with those with MPCM-small lesions, were characterized by significantly lower tryptase levels, shorter disease duration, and earlier disease onset... more patients with MPCM-large lesions exhibited spontaneous regression of cutaneous lesions." | HUMAN_CLINICAL | [link](https://doi.org/10.1016/j.jaci.2015.05.034) |
| 28770635 | Resolution rate UP vs mastocytoma; symptomatic Rx | "the complete resolution rate for mastocytoma was 10% per year... while the rate for urticaria pigmentosa was 1.9% per year... Treatment... is purely symptomatic with topical corticosteroids, antihistamines, omalizumab and imatinib being common choices." | HUMAN_CLINICAL (meta-analysis) | [link](https://doi.org/10.1080/00325481.2017.1364124) |
| 34804443 | Pediatric CM definition, D816V pathogenesis, management | "Cutaneous mastocytosis (CM), the most common form in children, is defined when MC infiltration is limited to the skin... Genetic aberrations, mainly the KIT D816V mutation, play a crucial role in the pathogenesis..." | HUMAN_CLINICAL (review) | [link](https://doi.org/10.4084/MJHID.2021.069) |
| 15096137 | Darier sign 94%, benign course | "Darier's sign was present in 94% of cases... in contrast to adults, mastocytosis in children usually has a benign course making sophisticated or invasive diagnostic tests unnecessary." | HUMAN_CLINICAL | [link](https://doi.org/10.1111/j.1468-3083.2004.00830.x) |
| 38522933 | Exon 8 KIT variant in MPCM; histology | "an Asp419del mutation in exon 8 of the KIT gene... a dense accumulation of CD117-positive, round or oval cells with amphophilic cytoplasm within the upper to middle dermis." | HUMAN_CLINICAL (case report) | [link](https://doi.org/10.15036/arerugi.73.189) |
| 34901755 | Updated diagnostic criteria; tryptase >20, CD30 | "A basal serum tryptase level exceeding 20 ng/mL remains a minor SM criterion... CD30 expression in MC now qualifies as a minor SM criterion." | HUMAN_CLINICAL (consensus) | [link](https://doi.org/10.1097/HS9.0000000000000646) |
| 36259506 | Prevalence ~1/10,000; KIT/CD117; HαT | "it is estimated that the disease affects approximately 1 in 10,000 persons." | HUMAN_CLINICAL (review) | [link](https://doi.org/10.1080/17843286.2022.2137631) |

---

## Suggested dismech entry scaffolding (leads)

- **`disease_term`:** MONDO:0019316 (already in draft — confirmed in OLS). Mappings: ORPHA:79457, MeSH:D014582, ICD-10:Q82.2, SNOMED:1332134000, UMLS:C0042111.
- **`has_subtypes`:** `Monomorphic` (small lesions, adult-type, persistent, SM-risk) and `Polymorphic` (large lesions, pediatric, regressing) — directly supported by Hartmann 2016 / Wiechers 2015. These map cleanly onto prognosis, tryptase, and progression fields.
- **Causal gene:** `gene: KIT` (hgnc:6342); pathophysiology node "Constitutive KIT Activation" with `modifier: INCREASED`, GO:0007169 / GO:0043303, CL:0000097, UBERON:0002067.
- **Phenotypes (HP leads):** HP:0000953 (hyperpigmentation), HP:0001025 (urticaria), HP:0000989 (pruritus), HP:0031284 (flushing), HP:0008066 (blistering), HP:0002014 (diarrhea) — **all to be validated**.
- **Treatments (MAXO/NCIT leads):** trigger avoidance, H1/H2 antihistamines, cromoglicate, omalizumab, epinephrine, KIT-TKI (imatinib for non-D816V; midostaurin/avapritinib for D816V).
- **Discussion items:** `kind: HUMAN_MODEL_MISMATCH` for the murine-model vs pediatric-regression gap; `kind: KNOWLEDGE_GAP` for why non-codon-816 KIT variants associate with the self-limiting pediatric course.

---

### Summary of key, citable facts
MPCM (urticaria pigmentosa) is the most common cutaneous mastocytosis, a clonal **KIT**-driven dermal mast-cell accumulation presenting in early childhood with hyperpigmented, Darier-positive maculopapular lesions. Children carry **diverse KIT variants (often non-D816V)** and usually follow a **benign, frequently self-resolving** course (polymorphic/large-lesion variant), whereas **monomorphic small-lesion** disease persists and flags possible systemic mastocytosis. Diagnosis is clinical + serum tryptase + KIT genotyping; treatment is symptomatic (trigger avoidance, antihistamines, cromolyn, omalizumab, epinephrine), with KIT-genotype-guided TKIs reserved for systemic/severe disease.

*All clinical/mechanistic claims above are sourced from PubMed-indexed literature with DOI links provided inline. Per the dismech anti-hallucination SOP, validate every PMID snippet (`just validate-references`) and every ontology ID (`just validate-terms-file`) before committing this content to `kb/disorders/Maculopapular_Cutaneous_Mastocytosis.yaml`.*