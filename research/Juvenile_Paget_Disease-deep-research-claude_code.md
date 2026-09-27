---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T14:04:44.314724'
end_time: '2026-09-04T14:11:14.330345'
duration_seconds: 390.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Juvenile Paget Disease
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 24
  num_turns: 43
  total_cost_usd: 1.8744813999999999
  session_id: 4583080c-1cc0-583c-84bf-77d0d31559d4
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Paget Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Juvenile Paget Disease** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I now have comprehensive material. Let me do a final round on genotype-phenotype correlation, treatment algorithm/monitoring, prevention/genetic counseling, and model organisms specifics, then write the report.

# Juvenile Paget Disease (Osteoprotegerin Deficiency): Comprehensive Research Report

## 1. Disease Information

**Overview.** Juvenile Paget disease (JPD) — also called idiopathic hyperphosphatasia, hereditary hyperphosphatasia, familial osteoectasia, chronic idiopathic hyperphosphatasemia, or hyperostosis corticalis deformans juvenilis — is an ultra-rare, generalized (non-focal) skeletal dysplasia of markedly accelerated bone turnover presenting in infancy or early childhood. It is fundamentally distinct from adult (classic) Paget disease of bone: adult Paget disease is focal, typically monostotic or polyostotic in older adults, and driven mainly by *SQSTM1* mutations affecting osteoclast p62/sequestosome signaling, whereas JPD is a generalized, whole-skeleton process of childhood most often caused by biallelic loss-of-function of osteoprotegerin (OPG), the natural decoy receptor that restrains osteoclastogenesis (Cundy & Mumm 2007, PMC6779132; Cundy et al., PMC10169728 — Frontiers Genet 2023, "Paget's disease: a review of the epidemiology, etiology, genetics, and treatment").

**Key identifiers:**
- **OMIM (phenotype):** #239000, *Paget Disease of Bone 5, Juvenile-Onset; PDB5* (https://www.omim.org/entry/239000)
- **OMIM (gene):** *602643, TNFRSF11B (Tumor Necrosis Factor Receptor Superfamily, Member 11B)*, chromosome 8q24.12
- **Orphanet:** ORPHA:2801, *Juvenile Paget disease* (https://www.orpha.net/en/disease/detail/2801)
- **Coding cross-references** (as indexed by Orphanet/aggregator terminologies; treat as leads to confirm against the primary ICD/MeSH releases rather than authoritative in themselves): ICD-10 M88.x (Paget disease of bone) category with a hyperphosphatasia designation sometimes carried under Q78.8; ICD-11 FB85.0; MeSH supplementary concept C537701.
- **HGNC:** TNFRSF11B, HGNC:11909; gene product osteoprotegerin (OPG)/osteoclastogenesis inhibitory factor (OCIF)

**Synonyms:** Idiopathic hyperphosphatasia; hereditary hyperphosphatasia; familial hyperphosphatasemia; familial osteoectasia; hyperostosis corticalis deformans juvenilis; chronic congenital idiopathic hyperphosphatasemia; osteoectasia with hyperphosphatasia; osteoprotegerin-deficiency juvenile Paget disease (NORD, https://rarediseases.org/rare-diseases/hereditary-hyperphosphatasia/; MedlinePlus, https://medlineplus.gov/download/genetics/condition/juvenile-paget-disease.pdf).

**Evidence base:** Information for this ultra-rare disease derives almost entirely from **individual case reports and small case series** (single patients, sib pairs, or small kindreds) rather than large aggregated cohorts or registries — fewer than 100 published cases exist worldwide across nearly 70 years of literature. This has direct implications for confidence in prevalence, natural-history, and treatment-response claims below, which should be treated as case-series-level evidence, not population-based epidemiology.

---

## 2. Etiology

### Disease causal factors — genetic, and now genetically heterogeneous

JPD is monogenic. Three genetically distinct causes have now been described, with strongly differing modes of inheritance and mechanism:

1. **TNFRSF11B (OPG) biallelic loss-of-function — the predominant cause (~two-thirds to the great majority of published cases).** Autosomal recessive; homozygous or compound heterozygous null/hypomorphic variants in the gene encoding osteoprotegerin abolish or severely reduce the decoy-receptor brake on RANK–RANKL signaling (Whyte et al., NEJM 2002, PMID:12124406, "Osteoprotegerin Deficiency and Juvenile Paget's Disease"; NORD, https://rarediseases.org/rare-diseases/hereditary-hyperphosphatasia/).
2. **TNFRSF11A (RANK) heterozygous activating duplication — one reported case.** A 13-year-old girl with no TNFRSF11B mutation carried a heterozygous 15-bp in-frame tandem duplication (87dup15) in exon 1 of TNFRSF11A, predicting the same pentapeptide extension of RANK's signal peptide seen in familial expansile osteolysis/expansile skeletal hyperphosphatasia (which is caused by the homologous 84dup15 duplication) — i.e., a gain-of-function RANK signaling lesion phenocopying OPG loss (PMID:25063546, PMC4189967, "Juvenile Paget's disease with heterozygous duplication within TNFRSF11A encoding RANK").
3. **SP7/Osterix de novo heterozygous neomorphic mutation — a third, distinct genetic cause.** A de novo heterozygous missense variant (c.926C>G; p.Ser309Trp) in SP7, encoding the osteoblast master transcription factor Osterix, was reported to cause a high-bone-turnover JPD-like phenotype through an altered/neomorphic DNA-binding specificity rather than simple haploinsufficiency (ScienceDirect/Bone, S8756328220301447; Nat Commun 2022, "A neomorphic variant in SP7 alters sequence specificity and causes a high-turnover bone disorder"). Note SP7 is genetically pleiotropic: separate homozygous loss-of-function SP7 variants cause osteogenesis imperfecta type XII (a *low*-turnover phenotype), underscoring that variant type/mechanism — not just the gene — determines whether SP7 dysfunction produces high- or low-turnover bone disease.

A JPD-focused targeted next-generation sequencing panel (Papapoulos group, PMC4410173) has additionally screened *TM7SF4* (DC-STAMP), *SQSTM1*, *TNFRSF11A*, *TNFRSF11B*, *OPTN*, *CSF1*, and *VCP* as candidate/modifier loci for atypical or mild presentations, reflecting that the RANK–RANKL–OPG axis and its regulators are the relevant candidate-gene space even when TNFRSF11B itself is normal.

### Risk factors
- **Genetic:** biallelic TNFRSF11B pathogenic variants (recessive); consanguinity substantially raises risk given the AR inheritance of the dominant genetic cause. **Founder mutations** are documented in two populations:
  - **Navajo:** a homozygous genomic deletion of TNFRSF11B, with an estimated **carrier frequency of ~1 in 100 Navajos** — a population-specific founder effect (Whyte et al. 2002, PMID:12124406; Whyte & Mumm review, PMC6779132).
  - **"Balkan" mutation** (966_969delTGACinsCTT): a small deletion/insertion reported in multiple unrelated patients of Balkan/Southeast European ancestry, notably associated with paradoxically *elevated* circulating immunoreactive (but non-functional) OPG protein (Whyte et al., J Bone Miner Res 2007, "Juvenile Paget's Disease: The Second Reported, Oldest Patient Is Homozygous for the TNFRSF11B 'Balkan' Mutation"; also the basis of the two adult siblings in the long-term denosumab study, PMC11994531).
- **Population/demographic:** more prevalent wherever consanguineous marriage is practiced, consistent with autosomal-recessive transmission (Frontiers Genet review, PMC10169728).
- **Sex:** no sex predilection reported; case series suggest roughly equal male:female distribution (individual case reports rather than a systematic sex-ratio study).

### Protective factors
No genetic or environmental protective factors have been established in the literature reviewed. This is expected for an essentially fully penetrant, biallelic loss-of-function Mendelian disorder — protective modifier alleles have not been systematically studied given the extreme rarity of the disease.

### Gene–environment interactions
None established or reported; JPD's causal mechanism is intrinsic (a structural bone-remodeling signaling defect) rather than exposure-modulated. Documented modifiers of clinical course are treatment-related (bisphosphonate/denosumab exposure ameliorating turnover; see Treatment) rather than classical gene-environment risk interactions.

---

## 3. Phenotypes

### Skeletal phenotypes (signs/physical findings)

| Phenotype | Onset/characteristics | Suggested HP term |
|---|---|---|
| Progressive long-bone deformity (bowing) | Childhood onset, progressive, worsens through the adolescent growth spurt if untreated | HP:0006419 (Bowing of the legs) / HP:0002980 (Femoral bowing) |
| Macrocephaly / skull enlargement | Progressive; head circumference reported up to +2.6 SD in a Czech case (OJRD 2025, PMC12333066) | HP:0000256 (Macrocephaly) |
| Short stature | Common; progressive with disease severity | HP:0004322 (Short stature) |
| Fractures (recurrent, long bone) | Onset from infancy/early childhood; recurrent, sometimes with minimal trauma | HP:0002757 (Recurrent fractures) |
| Vertebral collapse | "Sandwich vertebrae" (dense end plates) may be seen radiographically in young children and can resolve later | HP:0002944 (Kyphosis)/HP:0003468 (Compression fractures of the vertebrae) |
| Kyphoscoliosis | Progressive spinal curvature | HP:0002751 (Kyphoscoliosis) |
| Skull hyperostosis / cranial nerve entrapment risk | Diploic thickening, basilar/orbital-roof/sphenoid sclerosis | HP:0004437 (Hyperostosis cranii) |
| Bone pain | Common, correlates with turnover activity; markedly reduced with effective anti-resorptive treatment (denosumab pain scores fell from 9/10 and 7/10 pretreatment to 0–5/10 postinjection; PMC11994531) | HP:0002653 (Bone pain) |
| Muscular weakness | Reported feature | HP:0001324 (Muscle weakness) |
| Auricular (pinna) ossification | **Newly recognized feature** — a case series of 4 unrelated JPD patients found 3 (75%) had ossification of the elastic auricular cartilage, sometimes painful and occasionally involving the auditory canal (Whyte et al., PMC5111855, "Auricular Ossification: A Newly Recognized Feature of Osteoprotegerin-Deficiency Juvenile Paget Disease") | HP:0000377 (Abnormality of the pinna) |

### Extraskeletal phenotypes

- **Sensorineural and conductive hearing loss/deafness** — very common, progressive. Mechanism is dual: (1) conductive loss from deformity/ossicular abnormality of middle-ear bones, and (2) primary sensorineural loss from OPG deficiency causing demyelination and degeneration of the cochlear/acoustic nerve and increased apoptosis of spiral ganglion cells (ScienceDirect, S0969996113001228, "Loss of osteoprotegerin expression in the inner ear causes degeneration of the cochlear nerve and sensorineural hearing loss"). In the TNFRSF11A-duplication case, deafness involved missing ossicles and eroded cochleas (PMC4189967). Suggested term: HP:0000407 (Sensorineural hearing impairment) plus HP:0000405 (Conductive hearing impairment).
- **Progressive retinopathy / angioid streaks** — a distinctive ocular phenotype. Findings include retinal pigment epithelium mottling, peripapillary atrophy, angioid streaks, and choroidal neovascularization that can progress to disciform scarring and vision loss (PubMed 20547946, "Ocular Manifestations of Juvenile Paget Disease"). OPG/RANKL signaling is hypothesized to participate in Bruch membrane calcification, and retinopathy may reflect a more generalized vasculopathy; notably, in the long-term denosumab cohort, retinopathy **progressed despite adequate skeletal disease control**, with one subject developing sudden vision loss from macular edema, subretinal fluid, and choroidal neovascularization at age 46 requiring anti-VEGF therapy (bevacizumab, then aflibercept) — "long-term denosumab administration…may not prevent the emergence of retinopathy" (PMC11994531). Suggested HP terms: HP:0000531 (Angioid streaks — verify exact HPO term string before binding), HP:0000608 (Macular degeneration).
- **Vascular calcification and aneurysm formation** — internal carotid artery (bilateral cavernous/giant aneurysms reported in a child, PMID:20934158/AJNR 29:7 and ScienceDirect S1878875010000239), iliac artery aneurysms (ScienceDirect S2772687822000290), and generalized vascular calcification. Suggested HP term: HP:0004944 (Abnormal vascular physiology) or more specific vascular/aneurysm terms as applicable.
- **Dental abnormalities** — root resorption, tooth loss/breakage reported in the TNFRSF11A RANK-duplication case (PMC4189967).
- **Transient immunodeficiency** — the 2025 Czech case report describes "transient immunodeficiency requiring temporary immunoglobulin replacement" in a JPD patient (PMC12333066). This is mechanistically plausible given OPG's role as a decoy receptor also expressed by dendritic cells/B lymphocytes that dampens RANK–RANKL signaling on immune cells, but should be treated as an emerging/case-level observation, not an established core feature — it has not been systematically characterized across the JPD cohort, and should not be conflated with the RANK-pathway immunodeficiency described for TNFRSF11A-osteopetrosis (a different, more severe phenotype with absent lymph nodes; ScienceDirect S0002929708003637).

### Laboratory abnormalities
- **Serum alkaline phosphatase (ALP): markedly elevated**, often >10–15× the upper limit of normal (e.g., 75.75 µkat/L at age 4 in the Czech case, ~15× normal; PMC12333066). ALP is the best-characterized and most widely used marker of disease extent/activity.
- **Urinary hydroxyproline and pyridinoline/deoxypyridinoline cross-links**: elevated, reflecting collagen breakdown; urinary pyridinoline is now generally preferred to hydroxyproline as a more accurate activity marker.
- Additional turnover markers reported in treated patients: P1NP, β-CrossLaps, BAP (bone-specific ALP), osteocalcin, TRAP5b, N-telopeptide (NTx) — all elevated at baseline and used to titrate anti-resorptive therapy (PMC8039828; NEJM 2005, PMID:16135836).
- Serum calcium/phosphate are typically normal at baseline but calcium requires close monitoring once anti-resorptive treatment (especially denosumab) is started, given risk of profound hypocalcemia from abrupt osteoclast inhibition against a background of very high pretreatment turnover (see Treatment).

### Frequency/severity/progression
Frequency data for individual phenotypes across the JPD population are not systematically quantified (no registry-level denominator exists); the figures above (e.g., 75% auricular ossification in a 4-patient series) come from small case series and should be read as such. Progression is characteristically **worsening through the adolescent growth spurt**, and untreated disease is reported to render **the majority of affected children wheelchair-bound by age 15** (patient.info/Doctor summary; corroborated qualitatively by the treated-vs-untreated contrast in case reports).

### Quality of life impact
Direct QOL instrument data (EQ-5D, SF-36) for JPD were not identified in available literature — expected for a disease with <100 published cases. Functional impact is documented qualitatively: motor developmental delay in infancy, progression to wheelchair dependence if untreated, and striking functional recovery with effective anti-resorptive treatment — e.g., one patient in PMC8039828 progressed from delayed sitting at 18 months to independent walking by age 3 after pamidronate initiation. Bone pain scores (9/10, 7/10 pretreatment) documented in the denosumab study (PMC11994531) are the closest quantitative QOL-adjacent metric available.

---

## 4. Genetic/Molecular Information

### Causal genes
| Gene | HGNC | OMIM gene | Protein | Mechanism | Inheritance |
|---|---|---|---|---|---|
| **TNFRSF11B** | HGNC:11909 | *602643 | Osteoprotegerin (OPG) | Loss of function (decoy receptor deficiency) | Autosomal recessive |
| **TNFRSF11A** | HGNC:11908 | *603499 | RANK | Gain of function (activating duplication) | Reported as heterozygous (single case) |
| **SP7** | HGNC:11642 | *606633 | Osterix/SP7 | Neomorphic altered DNA-binding specificity | De novo heterozygous |

### Pathogenic variants (TNFRSF11B)
- **Variant types reported**: homozygous whole-gene/multi-exon deletions, splice-site variants (e.g., c.30+5G>A), missense variants (e.g., c.329G>T p.Gly110Val; cysteine-residue missense variants in the ligand-binding domain), and small deletion/insertion variants (e.g., 966_969delTGACinsCTT "Balkan" mutation).
- **Compound heterozygosity is rare**: as of the 2025 Orphanet Journal of Rare Diseases case report, "previous literature documented only two prior compound heterozygous TNFRSF11B cases," with homozygosity being the predominant genetic pattern (PMC12333066).
- **Variant burden**: per HGMD Professional (2024.2) as cited in that same 2025 report, approximately **twenty JPD-causing variants have been described in TNFRSF11B** to date — consistent with the disease's extreme rarity.
- **Population frequency**: a TNFRSF11B pathogenic variant was noted in gnomAD v2.1.1 at extremely low allele frequency (~0.003%) in one ClinVar-linked search result — this is a single-variant data point, not a locus-wide statement, and should be re-verified per-variant via gnomAD/ClinVar directly before use in curation (VCV000840923, VCV000006971, https://www.ncbi.nlm.nih.gov/clinvar/variation/840923/).
- **Founder variants**: Navajo homozygous deletion (carrier frequency ~1/100); Balkan 966_969delTGACinsCTT (multiple unrelated reported patients; paradoxically elevated but non-functional circulating OPG immunoreactivity, JBMR 2007).

### Genotype–phenotype correlation
A JPD-genotype/phenotype study (PMID:22638612, "Genotype-phenotype correlation in juvenile Paget disease: role of molecular alterations of the TNFRSF11B gene") reports a graded severity relationship:
- **Most severe**: large gene deletions removing multiple exons (including the whole ligand-binding domain), and missense mutations affecting **cysteine residues** in the ligand-binding domain — deformity manifest before 18 months of age with major disability.
- **Intermediate**: non-cysteine missense mutations in the ligand-binding domain — deformity recognized around age 5, with increased long-bone fracture rate.
- **Mildest**: an exon 5 insertion/deletion variant.

This genotype-severity gradient is directly relevant to prognostic counseling and to anticipating age at needed treatment initiation.

### Functional consequences
Loss-of-function (TNFRSF11B) → failure of decoy-receptor sequestration of RANKL → unchecked RANK–RANKL engagement on osteoclast precursors → excessive osteoclastogenesis and osteoclast activity. Gain-of-function (TNFRSF11A duplication) → constitutively active RANK signaling, phenocopying OPG loss via the same downstream pathway. SP7 mechanism is distinct — a transcription-factor DNA-binding specificity alteration in osteoblasts rather than direct RANK–RANKL pathway disruption, but converging on a high-bone-turnover phenotype.

### Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic mechanisms, or chromosomal-level abnormalities (aneuploidy, translocation) are established for JPD in the literature surveyed; the NGS candidate-gene panel work (TM7SF4/DC-STAMP, SQSTM1, OPTN, CSF1, VCP; PMC4410173) represents candidate-modifier screening in atypical/mild cases rather than confirmed modifier loci.

---

## 5. Environmental Information

No environmental toxin, occupational exposure, infectious trigger, or lifestyle factor has been implicated in JPD causation or exacerbation in the literature reviewed — consistent with its status as a purely monogenic disorder. This differs from **adult** Paget disease of bone, where a viral (paramyxovirus) etiologic hypothesis has historically been proposed for SQSTM1-associated disease; that hypothesis is specific to the adult/SQSTM1 form and should not be extrapolated to JPD.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered)

1. **Biallelic TNFRSF11B loss-of-function variants** (homozygous deletion, splice, missense, or compound heterozygous combinations) **lead to** absent or non-functional osteoprotegerin protein, or — alternatively — a heterozygous activating TNFRSF11A duplication **leads to** constitutively active RANK, or a de novo neomorphic SP7 variant **leads to** altered osteoblast transcriptional output favoring high bone turnover. [Established for TNFRSF11B mechanism — demonstrated genetically and biochemically, Whyte et al. NEJM 2002, PMID:12124406; inferred by structural homology for the TNFRSF11A duplication case, PMC4189967; established by *in vitro* DNA-binding assay for the SP7 neomorph, Nat Commun 2022]
2. Loss of the OPG decoy receptor (or gain of RANK activity) **results in** unopposed RANKL–RANK engagement on osteoclast precursors and mature osteoclasts. [Directly demonstrated — OPG's canonical function as a soluble RANKL-neutralizing decoy receptor is well established, PMC2684955 "RANK, RANKL and osteoprotegerin in bone biology and disease"]
3. Unopposed RANK signaling **drives** markedly increased osteoclast differentiation, number, and resorptive activity — reproduced directly in Tnfrsf11b-knockout mice, which show numerous osteoclasts and rapidly remodeling **woven** bone (rather than mature lamellar bone) recapitulating the human JPD phenotype. [Demonstrated in the mouse model — MODEL_ORGANISM evidence]
4. Excess osteoclastic resorption **triggers** a compensatory but disorganized coupled increase in osteoblastic bone formation, producing rapidly remodeled, structurally disorganized **woven bone** in place of normal lamellar bone throughout the entire skeleton (a generalized rather than focal process, distinguishing JPD from adult Paget disease). [Demonstrated — histology in case reports, e.g. PMC8039828 femoral biopsy showing "parallel trabecular-like structures with coexisting lamellar and woven bone" and abnormal multilayered osteoblasts]
5. Woven, poorly mineralized, disorganized bone **results in** reduced mechanical strength → skeletal deformity (bowing), osteopenia, and pathologic/recurrent fracture, concentrated in weight-bearing long bones and progressing with growth-plate activity — hence marked worsening during the adolescent growth spurt. [Demonstrated clinically/radiographically across essentially all case reports]
6. Ongoing high-turnover skull/cranial-base remodeling **causes** progressive calvarial and skull-base hyperostosis (diploic thickening, orbital-roof/sphenoid sclerosis, enlarged clivus), which **can compress** cranial nerves/otic structures. [Demonstrated radiographically]
7. In parallel, OPG deficiency acting **directly** in the inner ear (independent of ossicular/skull deformity) **causes** demyelination and apoptotic degeneration of the cochlear (spiral ganglion) nerve, **producing** progressive sensorineural hearing loss that compounds the conductive loss from ossicular/temporal-bone deformity. [Demonstrated in mouse model — Tnfrsf11b-knockout mice show both conductive loss from ossicle abnormality and sensorineural loss; ScienceDirect S0969996113001228]
8. OPG/RANKL pathway dysfunction is hypothesized to **contribute to** ectopic calcification of Bruch membrane in the eye, **producing** angioid streaks that can be **complicated by** choroidal neovascularization and disciform scarring/vision loss; retinopathy may reflect a **broader generalized vasculopathy**. [Inferred/hypothesized — the Bruch-membrane-calcification mechanism is proposed rather than directly demonstrated at the mechanistic level; the clinical association (angioid streaks, choroidal neovascularization) is well documented]
9. The same generalized vasculopathy is hypothesized to **underlie** vascular wall calcification and **predispose to** aneurysm formation (internal carotid, iliac), representing OPG's less-characterized vascular role outside bone. [Inferred — case-report-level association; OPG's vascular-protective role is independently supported in the cardiovascular literature but the causal chain to aneurysm in JPD specifically remains inferential]
10. Untreated, the cumulative burden of skeletal deformity, fracture, and disability **culminates in** progressive loss of ambulation (wheelchair dependence reported in the majority of untreated children by age 15) and variable but potentially reduced life expectancy, while extraskeletal complications (deafness, vision loss, vascular events) **compound** overall morbidity independent of skeletal disease control — notably, effective anti-resorptive treatment of the skeletal axis (bisphosphonates/denosumab) does **not** reliably prevent retinopathy progression, indicating the ocular/vascular arm may be at least partially **uncoupled** from the RANK–RANKL–osteoclast axis that anti-resorptives target. [Demonstrated — PMC11994531 documents retinopathy progression despite good skeletal control]

### Molecular pathway
RANK–RANKL–OPG axis (TNF receptor superfamily signaling); NF-κB and NFATc1 downstream in osteoclast precursors upon RANK engagement (canonical osteoclastogenesis pathway; not independently re-verified here but standard pathway biology — see KEGG osteoclast differentiation pathway, Reactome).

### Cellular processes
Osteoclast differentiation/hyperactivation (increased osteoclast number and resorptive activity); compensatory/coupled osteoblast activity producing disorganized woven-bone formation; cochlear spiral ganglion neuronal apoptosis; possible vascular smooth muscle/Bruch-membrane ectopic calcification.

### Protein dysfunction
Absent/non-functional secreted OPG (loss-of-function truncation, deletion, or ligand-binding-domain missense disruption) vs. constitutively active RANK receptor (gain-of-function duplication) vs. altered DNA-binding specificity of the Osterix/SP7 transcription factor (neomorphic mechanism).

### Cell types involved
- **Osteoclast** (CL:0000092) — hyperactivated effector cell
- **Osteoblast** (CL:0000062) — site of OPG production (normally) and compensatory bone formation; site of SP7 transcriptional activity
- **Spiral ganglion neuron** (relevant CL term for cochlear nerve) — site of OPG-deficiency-related apoptosis/demyelination
- **Dendritic cell / B lymphocyte** — reported sources of OPG relevant to the (emerging) immune phenotype
- **Vascular smooth muscle cell** — candidate site for vascular calcification, not directly demonstrated

### Suggested GO terms
- GO:0030316 (osteoclast differentiation)
- GO:0045453 (bone resorption)
- GO:0002062 (chondrocyte differentiation) — if relevant to growth plate involvement
- GO:0038149 (RANKL-mediated signaling pathway) if precise term exists — verify exact GO ID before binding
- GO:0043123 (positive regulation of canonical NF-kappaB signal transduction) — downstream of RANK activation

### Molecular profiling / advanced technologies
No transcriptomic, proteomic, metabolomic, single-cell, or spatial-omics studies specific to human JPD tissue were identified in this search — expected given the extreme rarity and the reliance on individual case reports; most molecular characterization to date has been at the level of Sanger/targeted NGS variant calling plus serum biomarker (ALP, turnover marker) measurement, plus one mouse-model transcriptional/functional study (Tnfrsf11b-knockout).

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: skeletal system — generalized, affecting long bones (especially lower-limb weight-bearing bones), skull/calvaria, vertebrae, pelvis
- Secondary: auditory system (cochlea, ossicles), visual system (retina, choroid, Bruch membrane), cardiovascular system (carotid and iliac arteries), external ear (auricular cartilage), dentition, and (emerging) immune system

**Tissue/cell level:** bone (woven vs. lamellar), cochlear nerve/spiral ganglion, retinal pigment epithelium and choroid, vascular wall, elastic cartilage of the pinna.

**Subcellular:** not specifically characterized for JPD beyond standard osteoclast/osteoblast secretory biology.

**Suggested UBERON terms:** UBERON:0002481 (bone tissue), UBERON:0003128 (calvaria), UBERON:0001690 (ear), UBERON:0000966 (retina), UBERON:0001981 (blood vessel), UBERON:0001917 (pinna).

**Localization/laterality:** Generalized/bilateral — this is a defining distinction from adult Paget disease, which is characteristically focal/asymmetric.

---

## 8. Temporal Development

- **Onset:** infancy to early childhood, typically reported "between 2 and 3 years of age" (NORD); insidious onset with progressive deformity.
- **Progression:** progressive and worsens markedly during the adolescent growth spurt if untreated; radiographic vertebral "sandwich" changes can be present early and resolve later. Disease is lifelong (chronic); no spontaneous remission is described. Rate and severity are genotype-dependent (see §4 genotype-phenotype correlation) — cysteine-domain missense and large-deletion genotypes present earlier (before 18 months) and more severely than exon-5 indel or non-cysteine missense genotypes (~age 5 onset).
- **Patterns:** No spontaneous remission reported; treatment-induced biochemical remission (near-normalization of ALP/turnover markers) is achievable with sustained anti-resorptive therapy but **relapses on discontinuation** of bisphosphonates (Frontiers Genet review, PMC10169728).
- **Critical periods:** Childhood/adolescent growth is the critical window for treatment — "Bisphosphonates…can ameliorate the skeletal phenotype, if started early enough in childhood and continued at least until growth is complete" (patient.info/Doctor summary; corroborated by outcome data in PMC8039828 and the OJRD 2025 case, where alendronate/ibandronate started at age 5 prevented further deformity/fracture through adulthood).

---

## 9. Inheritance and Population

### Epidemiology
- **~80–100 cases reported worldwide since the disease was first described in 1956**, yielding an estimated prevalence of **less than 1 in 10 million** (Frontiers Genet review, PMC10169728, explicitly modeling for underreporting: "Making the assumption that one fourth of the patients may have been reported, the prevalence of JPD may be estimated to be less than 1 in 10 million").
- No formal incidence, birth-prevalence, or registry-based figures exist; all estimates are literature-count-derived, not population/registry-derived — a substantially weaker evidence class than typical Orphanet epidemiology rows, and should be flagged as such in curation (`prevalence_class: NOT_YET_DOCUMENTED` or `ULTRA_RARE` qualitative tier rather than a numeric Orphanet band).

### Inheritance pattern
- **TNFRSF11B-related JPD:** autosomal recessive (the predominant/default form)
- **TNFRSF11A-duplication JPD:** reported as a heterozygous variant in a single case (mechanism analogous to the dominantly inherited familial expansile osteolysis caused by the homologous duplication) — this would functionally behave as autosomal dominant, though only one case is published
- **SP7-related JPD:** de novo heterozygous (autosomal dominant, de novo)

This is a case for explicit multi-locus/genetic-heterogeneity modeling in curation — JPD is not inheritance-uniform across its causal genes, unlike most single-gene AR disorders.

### Penetrance/expressivity
Reported cases suggest high penetrance for biallelic TNFRSF11B null genotypes, with **variable expressivity strongly correlated to specific variant class** (genotype-phenotype correlation, §4) rather than to stochastic/environmental variability.

### Founder effects / consanguinity
- Navajo founder deletion, carrier frequency ~1/100 (Whyte et al. 2002)
- Balkan founder indel (966_969delTGACinsCTT), reported in multiple unrelated Balkan-region patients
- Consanguinity is repeatedly noted as a risk-elevating factor for AR TNFRSF11B-JPD, consistent with its recessive transmission

### Carrier frequency / prenatal diagnosis
"Detection of carriers and prenatal diagnosis of juvenile Paget's disease…are possible," with particular relevance in founder populations such as the Navajo (search synthesis referencing Whyte et al.). No dedicated carrier-screening program or clinical guideline was identified.

### Population demographics
No systematic sex-ratio or geographic-distribution dataset exists beyond the founder-population observations above; case reports span multiple continents/ethnicities (Navajo, Balkan/Southeast European, Bolivian [TNFRSF11A case], Czech, Iranian, etc.), consistent with panethnic occurrence outside the two founder clusters.

---

## 10. Diagnostics

### Clinical/laboratory tests
- **Serum alkaline phosphatase** — the primary, best-characterized screening/monitoring biomarker; grossly elevated (multiples of ULN) at diagnosis.
- **Urinary pyridinoline/deoxypyridinoline cross-links** — now preferred over hydroxyproline as the activity/extent marker; hydroxyproline "is no longer considered an accurate marker."
- Additional turnover markers used for monitoring: P1NP, BAP, β-CrossLaps, osteocalcin, TRAP5b, NTx.
- **Skeletal survey/radiographs**: generalized osteopenic, widened long bones with coarse trabeculation and indistinct corticomedullary junction; marked cortical thickening (hyperostosis); widened phalanges; calvarial/diploic thickening with basilar sclerosis (orbital roofs, sphenoid), enlarged clivus; "sandwich vertebrae" in young children.
- **Bone histology/biopsy** (when performed): woven bone with coexisting lamellar architecture, abnormal multilayered osteoblasts, and quantitative backscattered electron imaging showing increased heterogeneity of mineralization (PMC8039828).
- **Audiometry** — for hearing-loss surveillance (both conductive and sensorineural components).
- **Ophthalmologic exam / fundus imaging** — for angioid streaks, RPE mottling, choroidal neovascularization surveillance; recommended as ongoing surveillance given that skeletal treatment does not reliably prevent ocular progression.
- **Vascular imaging** (as clinically indicated) — for carotid/iliac aneurysm screening given documented case reports.

### Genetic testing
- **First-tier**: targeted sequencing/single-gene testing of **TNFRSF11B** (the majority-cause gene), including deletion/duplication (copy-number) analysis given the founder deletions.
- **Expanded panel**: TNFRSF11A, SP7, plus candidate/modifier genes TM7SF4 (DC-STAMP), SQSTM1, OPTN, CSF1, VCP for atypical/mild or TNFRSF11B-negative presentations (PMC4410173 NGS panel design).
- Genetic Testing Registry entries exist for OMIM 602643 (https://www.ncbi.nlm.nih.gov/gtr/all/tests/?term=602643%5Bmim%5D).
- No WGS/WES-specific yield data for JPD were identified beyond the general recommendation that panel/targeted sequencing is the practical first approach given known causal genes.

### Clinical criteria / differential diagnosis
No formal consensus diagnostic criteria (e.g., DSM/ICD-style) were identified; diagnosis is made by the combination of clinical phenotype (infantile/childhood-onset generalized skeletal deformity), grossly elevated ALP with elevated urinary collagen cross-links, characteristic generalized (not focal) radiographic findings, and confirmatory molecular genetic testing.

**Key differential diagnoses** (search-derived, general differential-diagnosis discussion rather than a JPD-specific comparative study):
- **Adult/classic Paget disease of bone** — focal not generalized; SQSTM1-associated; older-onset
- **Camurati-Engelmann disease** (progressive diaphyseal dysplasia, TGFB1) — diaphyseal hyperostosis but different distribution/mechanism; GeneReviews available (https://www.ncbi.nlm.nih.gov/books/NBK1156/)
- **Craniodiaphyseal dysplasia**
- **Hypophosphatasia** — importantly the *inverse* biochemical picture (low, not high, ALP) despite a superficially similar name ("hyperphosphatasia" vs. "hypophosphatasia"); a naming trap worth flagging explicitly
- **Osteogenesis imperfecta** (including SP7-related OI type XII, which is *low*-turnover, unlike SP7-related JPD, which is high-turnover — same gene, opposite mechanism)
- **Familial expansile osteolysis / expansile skeletal hyperphosphatasia** (TNFRSF11A dup, dominant) — mechanistically the closest relative to the TNFRSF11A-JPD case, differing mainly in the pattern/distribution of expansile lesions
- **Polyostotic fibrous dysplasia**
- Hereditary hyperphosphatasia itself is distinguished from these radiographically by generalized rather than focal/mosaic change and by much earlier (infantile) onset.

### Screening
No population/newborn screening program exists (expected given ultra-rarity); cascade/carrier testing in founder populations (Navajo, Balkan) is the relevant targeted-screening context.

---

## 11. Outcome/Prognosis

- **Untreated natural history**: progressive skeletal deformity and disability; per patient.info's clinical summary, the majority of untreated affected children become wheelchair-bound by age 15.
- **Variable severity/mortality**: "Without curative treatment options, severe forms of juvenile Paget disease are a debilitating disease with high morbidity and increased mortality. However, the severity of disease is variable…and some patients will survive beyond the age of 50 years" (search synthesis of multiple sources; consistent with the genotype-phenotype gradient in §4). No formal survival curves or life-expectancy statistics were identified — again reflecting the case-report evidence base.
- **Treated outcomes**: substantial and durable improvement in bone turnover markers, prevention of new fractures, and preserved/restored mobility with early, sustained anti-resorptive therapy (bisphosphonates or denosumab); e.g., the Czech patient treated from age 5 remained fracture-free and "physically active throughout adulthood without significant quality-of-life limitations" by age 19 (PMC12333066); the two-adult denosumab cohort saw ALP "steadily normalized" and pain scores fall from 7–9/10 to 0–5/10 with no new fractures over 12–13.5 years (PMC11994531).
- **Persistent extraskeletal risk despite skeletal control**: retinopathy can still progress (including a case of sudden severe vision loss at age 46 despite 11+ years of denosumab) — an important prognostic caveat that skeletal disease control is not equivalent to complete disease control.
- **Complications driving morbidity**: fractures, progressive deafness, vision loss from retinopathy/choroidal neovascularization, vascular aneurysm (carotid, iliac) with attendant rupture/bleeding risk, and (rarely) death from unrelated intercurrent illness in a JPD patient (one child in PMC8039828 died of pneumococcal meningitis, unrelated to JPD itself, at age 5.6 after 4.5 years of treatment).
- **Prognostic factors**: TNFRSF11B genotype class (cysteine-domain/large-deletion vs. milder variant classes) is the clearest prognostic biomarker identified; age at treatment initiation is a major modifiable prognostic factor.

---

## 12. Treatment

### Pharmacotherapy — anti-resorptive therapy is the mainstay

**Bisphosphonates** (first-line, most experience):
- Suppress the pathologically accelerated bone turnover; demonstrated to normalize/near-normalize ALP and other turnover markers, prevent new fractures, halt deformity progression, and produce striking motor-developmental recovery when started early in childhood and continued through growth completion.
- **Agents used**: pamidronate (IV, individually titrated dosing — e.g., 9 mg/kg/year in 3 cycles, later adjusted to 0.75 mg/kg every 4–5 weeks for pain control, or up to 5.6–9.2 mg/kg/year; PMC8039828), zoledronic acid (IV, e.g., 0.025 mg/kg with extended dosing intervals), alendronate and ibandronate (oral, in the Czech case achieving 73–80% reductions in P1NP/ALP/BAP and 41% reduction in β-CrossLaps by age 19; PMC12333066).
- **Caveat**: turnover-marker suppression **relapses if bisphosphonate treatment is discontinued** — treatment is not curative and requires long-term/indefinite administration through growth.
- Suggested NCIT term: NCIT:C15986 (Pharmacotherapy), or more specifically bisphosphonate class terms; therapeutic_agent candidates include CHEBI terms for pamidronate, zoledronic acid, alendronate, ibandronate.

**Denosumab** (RANKL-neutralizing monoclonal antibody — mechanistically the most direct pharmacologic mimic of the missing OPG protein):
- In a girl with JPD, denosumab produced better disease control than bisphosphonate — ALP normalized and bone pain was more effectively controlled — but **severe hypocalcemia occurred with the first injection, requiring hospitalization and IV calcium** (PMID:23788687).
- In the long-term adult cohort (two Balkan-mutation homozygous siblings, treated 12–13.5 years), individualized low, frequent dosing (30 mg every 2.5–3 months, i.e., 0.35–0.58 mg/kg — lower than standard osteoporosis dosing but more frequent) achieved sustained ALP normalization and pain control with no new fractures; asymptomatic hypocalcemia occurred after each injection in one subject during the first 2 years, then resolved (PMC11994531).
- **Explicit pediatric caution**: "caution is needed if denosumab is given to children with JPD who have very high rates of bone turnover" — a cautionary pediatric case in the literature describes severe hungry bone syndrome with rebound hypercalcemia after denosumab initiation in a child (PMC11994531).
- Denosumab does **not** reliably prevent retinopathy progression even with excellent skeletal control (see §11).
- Suggested treatment_term: NCIT:C15986 (Pharmacotherapy); therapeutic_agent NCIT:C2477 (Denosumab, if this is the correct current NCIT code — verify).

**Calcitonin**: historically used before bisphosphonates became standard; "treatment with inhibitors of bone resorption (calcitonin or bisphosphonates) showed remarkable clinical and radiographic improvement" (early literature synthesis) — now largely superseded by bisphosphonates/denosumab.

**Recombinant osteoprotegerin (investigational, proof-of-concept)**: Cundy et al., NEJM 2005 (PMID:16135836, "Recombinant Osteoprotegerin for Juvenile Paget's Disease") treated two adult siblings with once-weekly subcutaneous recombinant OPG (0.3–0.4 mg/kg); after 15 months, radial bone mass increased 9% and 30% respectively, skeletal bisphosphonate retention (a resorption surrogate) fell 37% and 55%, with radiographic improvement and only mild hypocalcemia/hypophosphatemia as adverse effects. This is proof-of-mechanism for direct OPG replacement but was never developed into an approved product; denosumab has since become the practical RANKL-pathway-targeted therapeutic.

### Advanced/targeted therapeutics
No gene therapy, cell therapy, RNA-based therapy, or approved targeted biologic beyond denosumab was identified for JPD specifically.

### Surgical/interventional
Not systematically detailed in the sources reviewed beyond fracture management; orthopedic correction of deformity may be considered per general pediatric orthopedic principles (not JPD-specific evidence identified). Vascular aneurysms have required neurointerventional/surgical management in individual case reports (carotid, iliac aneurysm cases).

### Supportive/rehabilitative
- Hearing aids/cochlear management for progressive hearing loss
- Ophthalmologic surveillance and anti-VEGF intravitreal therapy (bevacizumab, aflibercept) for choroidal neovascularization complicating retinopathy — demonstrated effective ("almost full recovery of vision" in PMC11994531)
- Physical therapy/motor rehabilitation, particularly around treatment initiation in infants with motor delay

### Experimental
An investigational angiotensin-II type 1 receptor blockade approach was studied in the **mouse model** of JPD, improving bone mineral density and left ventricular contractility (ScienceDirect S0014299919304716) — a MODEL_ORGANISM-level finding relevant to the cardiovascular arm of the disease, not yet translated to human JPD treatment. No registered human clinical trials specific to JPD were identified in this search (contrast with the unrelated hypophosphatasia trial NCT00894075 that surfaced due to name similarity — a naming-confusion trap to avoid).

### Treatment strategy
The practical algorithm emerging from the case literature: **early diagnosis → early initiation of anti-resorptive therapy (bisphosphonate first-line; denosumab as an alternative/escalation with careful calcium monitoring) → continue through completion of growth → lifelong surveillance for extraskeletal complications (audiometry, ophthalmologic exam, vascular imaging) that may progress independent of skeletal control.**

---

## 13. Prevention

- **Primary prevention**: none possible for the genetic lesion itself; the only primary-prevention-adjacent measure is genetic counseling and carrier testing in founder populations (Navajo, Balkan) to inform reproductive decision-making, plus stated feasibility of prenatal diagnosis where a familial variant is known.
- **Secondary prevention**: early biochemical/clinical recognition (elevated ALP in an infant/toddler with skeletal deformity) followed by prompt anti-resorptive treatment is repeatedly framed in the literature as the single most important prognosis-modifying intervention — "Early diagnosis and antiresorption treatment prevent further fractures and deformity progression, and improve the patient's quality of life" (search synthesis referencing PMC12333066 and related sources).
- **Tertiary prevention**: ongoing multidisciplinary surveillance (audiology, ophthalmology, vascular imaging as indicated) to catch and treat extraskeletal complications (hearing loss interventions, anti-VEGF therapy for choroidal neovascularization, vascular aneurysm monitoring/intervention) that may progress independent of skeletal disease control.
- **Genetic counseling**: recommended for families of affected individuals given autosomal recessive inheritance (TNFRSF11B form) and documented founder effects; carrier frequency data exist for the Navajo population specifically (~1/100).
- **Screening programs**: no population-based newborn or carrier screening program for JPD was identified; targeted carrier screening in known founder populations is the closest analog described in the literature.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal JPD analog (OMIA entry) was identified in this search. The relevant cross-species biology is the **engineered mouse knockout model** (below) rather than a spontaneously occurring animal disease.

**Orthologous gene**: Tnfrsf11b (mouse ortholog of human TNFRSF11B); NCBI Gene ID for mouse Tnfrsf11b not independently verified here — confirm before curation.

---

## 15. Model Organisms

### Tnfrsf11b (OPG) knockout mouse — the primary and best-validated model
- **Phenotype recapitulation**: "Mice that lack osteoprotegerin owing to the knockout of Tnfrsf11b have numerous osteoclasts and rapidly remodeling woven bone rather than…lamellar bone. These mice manifest juvenile Paget's disease" — i.e., a high-fidelity recapitulation of the core skeletal phenotype (osteoclast excess, woven-bone remodeling), directly analogous to loss-of-function human TNFRSF11B disease.
- **Extraskeletal recapitulation**: Tnfrsf11b-knockout mice also develop **both** conductive hearing loss (from abnormal middle-ear ossicles) **and** sensorineural hearing loss (from cochlear nerve demyelination/degeneration and spiral ganglion apoptosis) — closely mirroring the dual-mechanism deafness seen in human JPD (ScienceDirect S0969996113001228).
- **Cardiovascular extension**: the same/related OPG-deficient mouse model has been used to study cardiovascular consequences, where angiotensin II type 1 receptor blockade improved bone mineral density and left ventricular contractility — extending the model beyond skeletal phenotyping into the vascular/cardiac domain relevant to JPD's aneurysm/vasculopathy phenotype (ScienceDirect S0014299919304716).
- **Limitations**: specific reported limitations of the mouse model versus human JPD (e.g., whether retinopathy/angioid streaks are reproduced) were not identified in this search and should be checked directly in the primary Tnfrsf11b-knockout characterization papers (Bucay et al. 1998, Genes Dev, and Simonet et al. 1997, Cell — foundational OPG-knockout papers; PMIDs not independently re-verified in this pass and should be confirmed before citation).

No other model organism (zebrafish, Drosophila, C. elegans, iPSC/organoid) system for JPD was identified in this search.

---

## Summary of Notable Gaps and Curation Flags

- **Evidence tier**: virtually the entire evidence base is individual case reports/small series (<100 total published patients); prevalence and natural-history statistics are literature-count estimates, not registry data — grade accordingly.
- **Genetic heterogeneity**: JPD is not TNFRSF11B-exclusive. TNFRSF11A (RANK, gain-of-function duplication, single case) and SP7 (Osterix, de novo neomorphic, distinct mechanism) are documented alternate causal genes with different inheritance patterns — this needs explicit multi-gene/multi-inheritance modeling if curated, not a single AR TNFRSF11B block.
- **A same-gene, opposite-mechanism trap**: SP7 loss-of-function causes low-turnover osteogenesis imperfecta type XII, while a distinct SP7 neomorphic gain-of-function variant causes high-turnover JPD — do not conflate.
- **A name trap**: "hyperphosphatasia" (JPD) vs. "hypophosphatasia" (a biochemically opposite, ALPL-related disorder) — verify no cross-contamination in any automated/AI-assisted literature search given the near-identical names.
- **Retinopathy is not fully treatment-coupled**: skeletal disease control (bisphosphonate or denosumab) does not guarantee prevention of progressive retinopathy — an important point for any treatment-target-mechanism modeling.
- Several claims above were drawn from AI-generated search-result syntheses rather than directly fetched primary-source text (multiple PMC/NEJM/Wiley full-text fetches were blocked by CAPTCHA/paywall/403 during this research pass, including OMIM 239000 direct fetch, the PMC6779132 review, the NEJM Whyte 2002 full text, and Orphanet's page). Where a claim is load-bearing for curation (exact quotes, specific numeric values, PMID linkage), the primary source should be independently re-fetched and the snippet verified against it before it is entered into any evidence-graded knowledge base record, per this repository's zero-tolerance policy on unverified snippets.

---

## Sources

- [OMIM #239000 – Paget Disease of Bone 5, Juvenile-Onset (PDB5)](https://www.omim.org/entry/239000)
- [OMIM *602643 – TNFRSF11B](https://www.omim.org/entry/602643)
- [Orphanet: Juvenile Paget disease (ORPHA:2801)](https://www.orpha.net/en/disease/detail/2801)
- [MedlinePlus: Juvenile Paget disease](https://medlineplus.gov/download/genetics/condition/juvenile-paget-disease.pdf)
- [NORD: Hereditary Hyperphosphatasia](https://rarediseases.org/rare-diseases/hereditary-hyperphosphatasia/)
- [Whyte et al., NEJM 2002 — Osteoprotegerin Deficiency and Juvenile Paget's Disease (PMID:12124406)](https://pubmed.ncbi.nlm.nih.gov/12124406/)
- [Cundy et al., NEJM 2005 — Recombinant Osteoprotegerin for Juvenile Paget's Disease (PMID:16135836)](https://pubmed.ncbi.nlm.nih.gov/16135836/)
- [Whyte et al., JBMR 2007 — Balkan TNFRSF11B mutation](https://onlinelibrary.wiley.com/doi/full/10.1359/jbmr.070307)
- [Middleton-Hardie et al. / PMC4189967 — Juvenile Paget's disease with heterozygous duplication within TNFRSF11A encoding RANK](https://pmc.ncbi.nlm.nih.gov/articles/PMC4189967/)
- [Whyte et al. — Auricular Ossification: A Newly Recognized Feature of Osteoprotegerin-Deficiency JPD (PMC5111855)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5111855/)
- [2025 Orphanet J Rare Dis — Juvenile Paget disease with unique compound heterozygous TNFRSF11B variants (PMC12333066)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12333066/)
- [Long-Term Denosumab Treatment in Adults with Juvenile Paget Disease (PMC11994531)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11994531/)
- [Clinical course in two children with JPD during long-term IV bisphosphonate treatment (PMC8039828)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8039828/)
- [Effects of denosumab on bone turnover markers in a girl with JPD (PMID:23788687)](https://pubmed.ncbi.nlm.nih.gov/23788687/)
- [Ocular Manifestations of Juvenile Paget Disease (PMID:20547946)](https://pubmed.ncbi.nlm.nih.gov/20547946/)
- [Loss of osteoprotegerin expression in the inner ear causes cochlear nerve degeneration and sensorineural hearing loss](https://www.sciencedirect.com/science/article/abs/pii/S0969996113001228)
- [Paget's disease: a review of the epidemiology, etiology, genetics, and treatment (PMC10169728)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10169728/)
- [Genotype-phenotype correlation in juvenile Paget disease (PMID:22638612)](https://pubmed.ncbi.nlm.nih.gov/22638612/)
- [Juvenile Paget's Disease From Heterozygous Mutation of SP7 Encoding Osterix](https://www.sciencedirect.com/science/article/abs/pii/S8756328220301447)
- [A neomorphic variant in SP7 alters sequence specificity and causes a high-turnover bone disorder, Nat Commun 2022](https://www.nature.com/articles/s41467-022-28318-4)
- [Bilateral cavernous internal carotid aneurysms in a child with JPD and OPG deficiency (PMID:17947367 / AJNR 29:7)](https://www.ajnr.org/content/29/1/7)
- [Osteoprotegerin deficiency and aneurysm formation: iliac artery aneurysms in JPD](https://www.sciencedirect.com/science/article/pii/S2772687822000290)
- [Polymorphisms of CSF1 and TM7SF4 in a case of mild JPD using NGS (PMC4410173)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4410173/)
- [Blockade of the angiotensin II type 1 receptor increases BMD and LV contractility in a mouse model of JPD](https://www.sciencedirect.com/science/article/abs/pii/S0014299919304716)
- [Camurati-Engelmann Disease – GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1156/)
- [ClinVar VCV000840923](https://www.ncbi.nlm.nih.gov/clinvar/variation/840923/) / [ClinVar VCV000006971](https://www.ncbi.nlm.nih.gov/clinvar/variation/6971/)