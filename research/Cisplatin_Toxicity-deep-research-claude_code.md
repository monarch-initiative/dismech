---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-01T22:16:55.225659'
end_time: '2026-09-01T22:30:14.467535'
duration_seconds: 799.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cisplatin Toxicity
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
  - claude-opus-5
  web_search_requests: 5
  num_turns: 67
  total_cost_usd: 8.118168249999998
  session_id: a177099e-edd5-4c2c-9879-5355be8d2d56
  stop_reason: end_turn
  permission_denials: 7
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 2
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cisplatin Toxicity
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cisplatin Toxicity** covering all of the
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

I am researching cisplatin toxicity now. Report follows in this message.

# Cisplatin Toxicity — Comprehensive Research Report

**Prepared:** 2026-09-01 · **Target:** Cisplatin Toxicity · **MONDO:** MONDO:0027664 (label verified live against OLS4: `cisplatin toxicity`) · **Category:** Complex

**Provenance note, stated up front.** Every PMID, quotation, and ontology identifier below was retrieved during this session from NCBI E-utilities, the EBI Ontology Lookup Service, the HGNC REST API, or the dismech term caches in this worktree. Where I could not verify something, I say so in place rather than filling the gap. I did not verify ICD-10, ICD-11, SNOMED CT, or LOINC codes against their authorities.

---

## 1. Disease Information

### What it is

Cisplatin toxicity is not a disease of the patient's own biology. It is the injury a drug does to normal tissue while it is doing its intended work on a tumour. The initiating lesion is the same in tumour and in host: platinum bound to DNA.

The MeSH scope note for Cisplatin (`D002945`, introduced 1984, CAS registry `Q20Q21Q62J`) states the chemistry plainly:

> "An inorganic and water-soluble platinum complex. After undergoing hydrolysis, it reacts with DNA to produce both intra and interstrand crosslinks. These crosslinks appear to impair replication and transcription of DNA. The cytotoxicity of cisplatin correlates with cellular arrest in the G2 phase of the cell cycle."
> — MeSH descriptor D002945 (retrieved 2026-09-01)

Dasari & Tchounwou give the same mechanism as a pharmacological claim:

> "Its mode of action has been linked to its ability to crosslink with the purine bases on the DNA; interfering with DNA repair mechanisms, causing DNA damage, and subsequently inducing apoptosis in cancer cells."
> — PMID:25058905, *Eur J Pharmacol* 2014;740:364-78

The syndrome is a **cluster of organ-specific toxicities**, not one lesion. The 2024 comprehensive review names the dose-limiting set:

> "its clinical utility is hampered by its dose-limiting toxicities, including nephrotoxicity, ototoxicity, neurotoxicity, and myelosuppression."
> — PMID:39423903, *Eur J Pharm Sci* 2024;203:106939

A 2023 ototoxicity review adds the fuller list:

> "its clinical use is limited by severe side effects, including ototoxicity, nephrotoxicity, neurotoxicity, hepatotoxicity, gastrointestinal toxicity, and retinal toxicity."
> — PMID:38003734, *Int J Mol Sci* 2023;24(22):16545

### Identifiers

| Resource | Identifier | Verified? |
|---|---|---|
| MONDO | `MONDO:0027664` "cisplatin toxicity" | Yes — OLS4 live query |
| MeSH (drug) | `D002945` Cisplatin | Yes — NCBI E-utilities |
| MeSH (kidney outcome) | `D058186` Acute Kidney Injury | Yes |
| MeSH (nerve outcome) | `D010523` Peripheral Nervous System Diseases | Yes |
| MeSH (ear outcome) | "Ototoxicity" exists as a descriptor; its descriptor UI did not resolve in my query | **Not verified** |
| ChEBI (agent) | `CHEBI:27899` cisplatin | Yes — dismech cache |
| NCIT (agent) | `NCIT:C376` Cisplatin | Yes — dismech cache |
| ICD-10-CM | Adverse-effect coding is by T-code plus manifestation, not by a cisplatin-specific code | **Not verified against ICD authority** |
| OMIM / Orphanet | Not applicable — this is an acquired drug toxicity, not a Mendelian disorder | — |

### Synonyms

Cisplatin-induced nephrotoxicity (CIN); cisplatin-associated acute kidney injury (CP-AKI); cisplatin-induced ototoxicity (CIO); cisplatin-induced peripheral neuropathy (CIPN, when platinum-specific); platinum toxicity; cis-diamminedichloroplatinum(II) toxicity. The MeSH entry terms for the drug include *cis-Platinum*, *Platinol*, *NSC-119875*, *cis-Dichlorodiammineplatinum(II)*.

### Data derivation

Both. Much of the epidemiology below is **individual-patient EHR-derived** — the BMJ risk-score study drew on 24,717 adults across six US academic cancer centres (PMID:38538012). The pharmacogenomic and survivorship data come from **aggregated cohorts** (the Platinum Study, PanCareLIFE, Canadian Pharmacogenomics Network for Drug Safety). Mechanism is almost entirely **preclinical**, and the reviews say so.

---

## 2. Etiology

### Primary cause

One cause, and it is iatrogenic: administration of cisplatin. There is no cisplatin toxicity without cisplatin exposure. Everything else on this page is a modifier of dose, of tissue exposure, or of cellular tolerance.

The exposure is **cumulative and dose-dependent**. Ototoxicity in particular tracks cumulative dose in a way that is visible even in self-report:

> "Tinnitus was also significantly related to age at survey completion (OR = 1.79; P = 0.003) and cumulative cisplatin dose (OR = 5.17; P < 0.001)."
> — PMID:36637632, *J Cancer Surviv* 2023;17(1):27-39

### Risk factors — clinical and demographic

The BMJ 2024 derivation cohort identified an independently associated set that is worth reproducing exactly, because it is the best-powered such list available:

> "Each of the following factors were independently associated with CP-AKI in the derivation cohort: age, hypertension, diabetes mellitus, serum creatinine level, hemoglobin level, white blood cell count, platelet count, serum albumin level, serum magnesium level, and cisplatin dose."
> — PMID:38538012, *BMJ* 2024;384:e077169

Pre-existing organ impairment is the other axis:

> "The risk of developing cisplatin-induced toxicity could be related to pre-existing conditions, including kidney disease, hearing impairment, neuropathy, impaired liver function, and other comorbidities."
> — PMID:39423903

For hearing specifically, the Platinum Study found cardiovascular and familial risk factors mattered alongside dose:

> "Risk factors for hearing loss included age at survey completion (OR = 1.57; P = 0.036), hypercholesterolemia (OR = 3.45; P = 0.007), cumulative cisplatin dose (OR = 1.94; P = 0.049), and family history of hearing loss (OR = 2.87; P = 0.071)."
> — PMID:36637632

**Age is bidirectional and matters differently by organ.** Very young children are at highest ototoxicity risk; older adults are at highest AKI risk. Both directions appear in the sources above.

### Genetic risk factors

The Canadian Pharmacogenomics Network for Drug Safety 2022 update is the authoritative synthesis. It graded 40 reports across 47 independent populations and 24 genes:

> "Considering GRADE criteria, genetic variants in 2 genes were strongly (ie, odds ratios ≥3) and consistently (ie, replication in ≥3 independent populations) predictive of cisplatin-induced ototoxicity. Specifically, an ACYP2 variant has been associated with ototoxicity in both children and adults, whereas TPMT variants are relevant in children."
> — PMID:37726872, *Ther Drug Monit* 2023;45(6):714-730

Two things follow, and the second is the one curators get wrong. First, only **ACYP2** and **TPMT** clear the bar. Second, **COMT does not** — it was an early candidate and the review's own conclusion drops it to the "further research required" tier.

The Platinum Study GWAS adds signal that has not been replicated to the same standard:

> "Hearing loss and TXNRD1, which plays a key role in redox regulation, showed borderline significance (p = 4.2 × 10-6) in gene-based analysis. rs62283056 in WFS1 previously found to be significantly associated with hearing loss (n = 511), was marginally significant in an independent replication cohort (p = 0.06; n = 606). Gene-based analyses identified significant associations between tinnitus and WNT8A (p = 2.5 × 10-6)."
> — PMID:35322580, *Cancer Med* 2022;11(14):2801-2816

The Brock consensus review frames the genetic architecture as three functional classes:

> "Genes involved in drug transport, metabolism, and DNA repair regulate platinum toxicities."
> — PMID:22547603, *J Clin Oncol* 2012;30(19):2408-17

**Gene table (HGNC IDs resolved live from rest.genenames.org or the dismech cache):**

| Symbol | HGNC | Role in cisplatin toxicity | Evidence tier |
|---|---|---|---|
| `ACYP2` | HGNC:180 | Ototoxicity susceptibility, children and adults | Strong, replicated ≥3 populations (PMID:37726872) |
| `TPMT` | hgnc:12014 | Ototoxicity susceptibility, children | Strong in children (PMID:37726872) |
| `COMT` | hgnc:2228 | Candidate ototoxicity locus; not replicated to strong tier | Inconsistent (PMID:37726872) |
| `WFS1` | hgnc:12762 | rs62283056, hearing loss | Marginal in replication (PMID:35322580) |
| `TXNRD1` | HGNC:12437 | Redox regulation; gene-based hearing-loss signal | Borderline (PMID:35322580) |
| `WNT8A` | Not verified this session | Tinnitus, gene-based | Single study (PMID:35322580) |
| `SLC31A1` (CTR1) | HGNC:11016 | Cellular uptake | Mechanistic (PMID:19144690) |
| `SLC22A2` (OCT2) | HGNC:10966 | Basolateral tubular uptake | Mechanistic (PMID:19144690, PMID:32150447) |
| `SLC47A1` (MATE1) | HGNC:25588 | Apical efflux | Mechanistic — **not directly verified this session** |
| `ERCC1` | hgnc:3433 | Nucleotide excision repair of Pt-DNA adducts | Mechanistic |
| `ERCC2` (XPD) | hgnc:3434 | Nucleotide excision repair | Mechanistic |
| `XPA` / `XPC` | hgnc:12814 / hgnc:12816 | Nucleotide excision repair | Mechanistic |
| `TP53` | hgnc:11998 | Apoptotic response to adducts | Mechanistic |
| `GSTP1` | HGNC:4638 | Glutathione conjugation / detoxification | Candidate |
| `TRPM6` | HGNC:17995 | Distal tubular magnesium reabsorption | Mechanistic candidate for hypomagnesemia — **link not directly verified this session** |

### Protective factors

Genetic protective alleles: none established. The literature frames variants as susceptibility, not protection.

Environmental and pharmacological protection is where the field actually stands:

- **Magnesium supplementation during hydration.** A 2024 systematic review with meta-analysis of 11 retrospective studies: "A meta-analysis of 11 retrospective studies that examined magnesium supplementation during hydration showed that this treatment provided significant protection against CIN (OR = 0.22, 95% CI = 0.14 to 0.35)." — PMID:37530867, *Clin Exp Nephrol* 2024;28(1):1-12
- **Dose is not the whole story for magnesium.** A 2026 meta-analysis: "Magnesium supplementation showed an inhibitory effect on cisplatin-induced renal injury. The inhibitory effect of magnesium supplementation showed no difference among the three dose groups (<10 mEq, 10-<20 mEq, and ≥20 mEq)." — PMID:42652681, *J Clin Med* 2026;15(16):6278
- **Sodium thiosulfate** for hearing, in children — see §12.

### Gene-environment interaction

The Platinum Study is the only source here with direct GxE-relevant data, and its findings are behavioural rather than molecular:

> "In addition, hearing loss was positively associated with BMIs at clinical evaluation and nonwork-related noise exposure (>5 h/week). Tinnitus was positively associated with tobacco use, hypercholesterolemia, and noise exposure. We observed positive associations between peripheral neuropathy and persistent vertigo, tobacco use, and excess alcohol consumption."
> — PMID:35322580

Noise exposure stacking on a cisplatin-damaged cochlea is the clearest GxE candidate in the corpus. The genetic half of that interaction has not been tested against the environmental half in any study I found.

---

## 3. Phenotypes

### Otologic

Cisplatin ototoxicity is bilateral, high-frequency-first, and permanent.

> "Cisplatin-induced ototoxicity manifests as irreversible, bilateral, high-frequency sensorineural hearing loss in 40-60% of adults and in up to 60% of children."
> — PMID:38003734

> "Platinum initially impairs hearing in the high frequencies and progresses to lower frequencies with increasing cumulative dose."
> — PMID:22547603

> "Cisplatin chemotherapy causes permanent hearing loss in 40-80% of treated patients."
> — PMID:29162831, *Nat Commun* 2017;8(1):1654

| Phenotype | HP term | Frequency | Onset / course | Source |
|---|---|---|---|---|
| High-frequency sensorineural hearing impairment | `HP:0001757` | 40–60% adults; up to 60% children | Begins during therapy; progresses with cumulative dose | PMID:38003734, PMID:22547603 |
| Bilateral sensorineural hearing impairment | `HP:0008619` | Essentially all affected cases are bilateral | Irreversible | PMID:38003734 |
| Progressive sensorineural hearing impairment | `HP:0000408` | — | Progresses to lower frequencies with dose | PMID:22547603 |
| Tinnitus | `HP:0000360` | 68% of testicular cancer survivors | Persistent | PMID:36637632 |
| Hearing impairment (self-reported) | `HP:0000365` | 59% of testicular cancer survivors | Late, persistent | PMID:36637632 |
| Vertigo | `HP:0002321` | Reported; frequency not quantified in sources retrieved | — | PMID:39417180 |

Composite ototoxicity in a well-characterised adult survivor cohort:

> "Of 145 TC survivors, 74% reported ototoxicity: 68% tinnitus; 59% hearing loss; and 52% reported both."
> — PMID:36637632

Quality-of-life impact is stated qualitatively in the reviews and I did not find an EQ-5D or SF-36 utility decrement specific to cisplatin ototoxicity:

> "Hearing loss can lead to social isolation, depression, and cognitive decline in adults, and speech and language developmental delays in children."
> — PMID:38003734

### Renal and electrolyte

| Phenotype | HP term | Frequency | Notes |
|---|---|---|---|
| Acute kidney injury | `HP:0001919` | Severe (≥2× creatinine): 5.2% derivation / 3.3% validation. Any-grade: "up to one third of patients" | PMID:38538012; PMID:41854743 |
| Elevated circulating creatinine concentration | `HP:0003259` | Definitional for the above | PMID:38538012 |
| Chronic kidney disease | `HP:0012622` | Long-term sequela | PMID:36229672 |
| Renal insufficiency | `HP:0000083` | — | PMID:37182407 |
| Hypomagnesemia | `HP:0002917` | Very common; a low serum magnesium is also a *predictor* of AKI | PMID:38538012, PMID:42652681 |
| Hypokalemia | `HP:0002900` | Common; hypokalaemia was the commonest non-haematological AE in ACCL0431 controls (12%) | PMID:27914822 |
| Hypocalcemia | `HP:0002901` | Secondary to Mg depletion | PMID:37182407 |
| Hyponatremia | `HP:0002902` | Salt-wasting reported | PMID:37182407 |
| Hypophosphatemia | `HP:0002148` | Tubular | PMID:37182407 |
| Renal tubular dysfunction | `HP:0000124` | The proximate lesion | PMID:37182407 |
| Renal Fanconi syndrome | `HP:0001994` | Reported, uncommon | Mechanistically consistent; frequency **not verified** |
| Hemolytic-uremic syndrome | `HP:0005575` | Rare; thrombotic microangiopathy | PMID:37182407 |
| Polyuria | `HP:0000103` | Salt-losing nephropathy | PMID:37182407 |

The nephrotoxicity spectrum is explicitly broader than AKI:

> "We also discuss the spectrum of nephrotoxicity, including acute and chronic impairment of kidney function, electrolyte disturbances, and thrombotic microangiopathy."
> — PMID:37182407, *Semin Nephrol* 2022;42(6):151341

**Note the incidence discrepancy, and do not average it away.** The BMJ figure (3–5%) is for *severe* CP-AKI defined as doubling of creatinine or dialysis within 14 days. The "up to one third" and "up to 20%" figures use looser definitions. These are different endpoints, not conflicting estimates.

### Neurologic

| Phenotype | HP term | Frequency | Source |
|---|---|---|---|
| Peripheral neuropathy | `HP:0009830` | 29.2% after EPx4; 21.4% after BEPx3 (self-reported, TC survivors) | PMID:28240972 |
| Distal sensory impairment | `HP:0002936` | Length-dependent, stocking-glove | PMID:32663120 |
| Paresthesia | `HP:0003401` | Presenting symptom | PMID:32663120 |
| Peripheral axonal neuropathy | `HP:0003477` | The pathological substrate | — |
| Sensory neuropathy | `HP:0000763` | Predominantly sensory; motor sparing is characteristic | — |
| Areflexia | `HP:0001284` | Late | — |
| Gait ataxia | `HP:0002066` | From large-fibre sensory loss | — |
| Raynaud phenomenon | `HP:0030880` | 11.6% after EPx4; 21.4% after BEPx3 | PMID:28240972 |

> "When comparing individual AHOs for EPX4 versus BEPX3, Raynaud phenomenon (11.6% v 21.4%; P < .01), peripheral neuropathy (29.2% v 21.4%; P = .02), and obesity (25.5% v 33.0%; P = .04) differed."
> — PMID:28240972, *J Clin Oncol* 2017;35(11):1211-1222

The three neurotoxicities travel together:

> "Hearing loss, tinnitus, and peripheral neuropathy, accounting for age and cisplatin dose, were interdependent. Survivors with these neurotoxicities experienced more hypertension and poorer self-reported health."
> — PMID:35322580

**Coasting** — progression of neuropathy for weeks to months after the last dose — is a recognised feature of platinum neuropathy. I did not locate a primary citation for it in this session. Curate it only with a source you have read.

### Haematologic and gastrointestinal

| Phenotype | HP term | Notes |
|---|---|---|
| Anemia | `HP:0001903` | Dose-limiting with cumulative cycles |
| Decreased total neutrophil count | `HP:0001875` | **Note the current HPO label** — OLS4 returns "Decreased total neutrophil count", not "Neutropenia". Grade 3–4 neutropenia occurred in 65% of control participant-cycles in ACCL0431 (PMID:27914822) |
| Thrombocytopenia | `HP:0001873` | Label verified current via OLS4 |
| Pancytopenia | `HP:0001876` | Severe cases |
| Nausea | `HP:0002018` | Cisplatin is the archetypal highly emetogenic agent |
| Vomiting | `HP:0002013` | Acute and delayed phases |
| Anorexia | `HP:0002039` | — |
| Diarrhea | `HP:0002014` | — |
| Weight loss | `HP:0001824` | — |
| Alopecia | `HP:0001596` | — |
| Fatigue | `HP:0012378` | — |

### Other organ systems

Retinal toxicity (`HP:0000488` Retinopathy; `HP:0000551` Color vision defect) and optic neuropathy (`HP:0001138`) are named in PMID:38003734's side-effect list. Hepatotoxicity is likewise named there. Male infertility (`HP:0003251`) and azoospermia (`HP:0000027`) follow gonadal exposure in testicular cancer survivors — a survivorship burden documented in the Platinum Study series (PMID:28240972 reports adverse health outcome counts, though I did not extract per-phenotype gonadal figures).

**Adverse health outcome burden, testicular cancer survivors, median 4.3 years post-chemotherapy:**

> "None, one to two, three to four, or five or more AHOs were reported by 20.4%, 42.0%, 25.1%, and 12.5% of TCSs, respectively."
> — PMID:28240972

---

## 4. Genetic/Molecular Information

**There is no causal gene.** The cause is a drug. Genetics here modifies susceptibility only, and the modification is real but modest outside the two strong ototoxicity loci.

- **Causal genes:** none. Do not curate `relationship_type: CAUSATIVE` for any gene on this entry.
- **Susceptibility loci:** `ACYP2` (HGNC:180) and `TPMT` (hgnc:12014), per PMID:37726872. Curate these as `SUSCEPTIBILITY`.
- **Variant classification:** these are common susceptibility SNPs, not ACMG-classifiable pathogenic variants. ClinVar/ACMG framing does not apply.
- **Somatic vs germline:** the susceptibility variants are germline. The DNA lesion driving toxicity is an acquired chemical adduct, not a variant.
- **Allele frequencies:** not retrieved this session.
- **Chromosomal abnormalities:** not applicable to the toxicity phenotype. Secondary treatment-related myeloid neoplasms after platinum/etoposide regimens do carry cytogenetic lesions, but that is a distinct downstream disease and should be a separate entry if curated.

### Epigenetics

The Nature Reviews Nephrology synthesis flags this as an emerging layer, and flags it as emerging rather than established:

> "In addition, emerging evidence suggests a contribution of epigenetic changes to cisplatin-induced acute kidney injury and chronic kidney disease. Further research is needed to determine how these pathways are integrated and to identify the cell type-specific roles of critical molecules involved in regulated necrosis, inflammation and epigenetic modifications in cisplatin nephrotoxicity."
> — PMID:36229672

Curate this as a `KNOWLEDGE_GAP` discussion, not as a mechanism node.

---

## 5. Environmental Information

- **The exposure is the drug.** Route: intravenous. Cumulative dose is the dominant determinant. In SIOPEL 6 the dose was 80 mg/m² over 6 hours per course, six courses (PMID:29924955); in ACCL0431 the trigger threshold in the FDA-approval framing was cumulative cisplatin ≥200 mg/m².
- **Infusion duration matters.** ACCL0431 restricted to individual doses infused over ≤6 hours, and initially stratified randomisation by "age and duration of cisplatin infusion" (PMID:27914822). Shorter infusions concentrate peak exposure.
- **Noise.** Non-occupational noise exposure >5 h/week associated with hearing loss in survivors (PMID:35322580). This is the clearest modifiable environmental co-exposure.
- **Tobacco and alcohol.** Tinnitus associated with tobacco use; peripheral neuropathy with tobacco use and excess alcohol (PMID:35322580).
- **Concomitant nephrotoxins.** Aminoglycosides, NSAIDs, contrast, and proton pump inhibitors are all implicated. A 2024 prospective cohort reported PPIs increasing CP-AKI risk in nasopharyngeal carcinoma (PMID:39138312 — title verified, abstract **not read this session**).
- **Cranial irradiation** compounds ototoxicity; ACCL0431 added it as a stratification variable by protocol amendment (PMID:27914822).
- **Infectious agents:** not applicable.

**ECTO binding.** I did not find a suitable ECTO exposure term for therapeutic cisplatin administration in this session. Per the dismech environmental-term convention, leaving `exposure_term.term` unbound with a `notes:` line recording the search is the correct outcome if a search confirms no term exists. Do not stretch a general "exposure to platinum" term onto a therapeutic infusion without checking it.

---

## 6. Mechanism / Pathophysiology

### The causal chain

**Branch point at step 3.** The chain is shared as far as intracellular platinum accumulation, then diverges by organ because the transporters, the repair capacity, and the cell death programs differ.

1. **Cisplatin is administered intravenously and circulates as the neutral dichloride complex in high-chloride plasma.** The low intracellular chloride concentration then drives **aquation**, converting cisplatin to a reactive positively charged aquo species. *Leads to* a DNA-reactive electrophile.
2. **Cell entry is transporter-mediated, not passive.** Copper transporter 1 (CTR1, `SLC31A1`, HGNC:11016) and organic cation transporter 2 (OCT2, `SLC22A2`, HGNC:10966) carry cisplatin into cells. *Results in* selective accumulation in tissues expressing these carriers — renal proximal and distal tubule, cochlea, dorsal root ganglion. This is why the toxicity is organ-selective rather than uniform.
   > "we demonstrate that Ctr1 is mainly expressed in both proximal and distal tubular cells in mouse kidneys. We further show that Ctr1 is mainly localized on the basolateral side of these cells, a proposed site for cisplatin uptake. Importantly, downregulation of Ctr1 by small interfering RNA or copper pretreatment results in decreased cisplatin uptake." — PMID:19144690 (**model organism / in vitro**)
   > "Cimetidine, a pharmacological inhibitor of OCT2, can also partially attenuate cisplatin uptake." — PMID:19144690
3. **Intracellular platinum binds the N7 of purine bases and forms 1,2-intrastrand and interstrand crosslinks.** *Leads to* stalled replication and transcription and G2 arrest (MeSH D002945; PMID:25058905).

**Branch A — kidney.**

4a. **Adduct burden in the tubular epithelium triggers a DNA damage response** alongside mitochondrial injury, ROS generation, and ER stress. These are concurrent, not sequential.
   > "Preclinical studies have provided insights into the cellular and molecular mechanisms of cisplatin nephrotoxicity, which involve intracellular stresses including DNA damage, mitochondrial pathology, oxidative stress and endoplasmic reticulum stress." — PMID:36229672
5a. **Those stresses activate a set of stress-response programs, several of which are cell-death programs.**
   > "Stress responses, including autophagy, cell-cycle arrest, senescence, apoptosis, programmed necrosis and inflammation have key roles in the pathogenesis of cisplatin nephrotoxicity." — PMID:36229672
6a. **Ferroptosis is now argued to be the dominant tubular death mode**, with ALOX12-driven phospholipid peroxidation as one demonstrated route. *This is a strong claim from a 2024 primary paper and should be curated as such, not as consensus.*
   > "In acute kidney injury (AKI), ferroptosis is the main mechanism of cell death in the renal tubular epithelium." — PMID:38805781, *Phytomedicine* 2024;130:155757 (**model organism + in vitro**)
   > "baicalein reduced the expression of 12-lipoxygenase (ALOX12), which inhibits phospholipid peroxidation and ferroptosis in AKI" — PMID:38805781
7a. **Dying tubular cells release DAMPs and cytokines, recruiting inflammatory cells.** *Leads to* amplification of injury beyond the directly platinated cells. Pabla & Dong framed this early: "Recent research has shed significant new lights on the mechanism of cisplatin nephrotoxicity, especially on the signaling pathways leading to tubular cell death and inflammation." — PMID:18272962
8a. **Tubular loss and inflammation produce falling GFR and rising creatinine** — clinically, AKI (`HP:0001919`).
9a. **Repeated cycles convert acute injury into fibrosis and CKD.** Demonstrated directly in mice: "Repeated administration of low-dose cisplatin in mice induces fibrosis." — PMID:26739893, *Am J Physiol Renal Physiol* 2016;310(6):F560-8 (**model organism**)
10a. **In parallel, tubular injury impairs magnesium reabsorption**, producing renal magnesium wasting and hypomagnesemia. Hypomagnesemia then feeds back as a risk factor for further kidney injury — a loop, not a one-way step. Magnesium is both a predictor of CP-AKI (PMID:38538012) and a preventive intervention (PMID:37530867, PMID:42652681). **The TRPM6 step is a plausible molecular explanation for this and I did not verify it against a primary source.**

**Branch B — cochlea.**

4b. **Cisplatin enters the cochlea and is not cleared.** This is the key non-obvious step: the pharmacokinetics of the inner ear differ from every other organ.
   > "In most organs cisplatin is detected within one hour after injection, and is eliminated over the following days to weeks. In contrast, the cochlea retains cisplatin for months to years after treatment in both mice and humans." — PMID:29162831 (**human tissue + model organism**)
5b. **Accumulation concentrates in the stria vascularis**, the endolymph-maintaining tissue.
   > "Cisplatin accumulation is consistently high in the stria vascularis, the region of the cochlea that maintains the ionic composition of endolymph." — PMID:29162831
6b. **Outer hair cells die**, basal turn first, which is why loss is high-frequency first. Whether the primary hit is direct hair-cell uptake or secondary to strial injury is genuinely unsettled and the field says so.
   > "Cisplatin ototoxicity chiefly manifests through the loss of outer hair cells, possibly resulting from damages directly by cisplatin uptake or secondary effects on the stria vascularis. Both direct and indirect influences contribute to cisplatin ototoxicity, while it is still debated which path is dominant or where the primary target of cisplatin is located." — PMID:39417180, *Am J Cancer Res* 2024;14(9):4597-4632
   Curate this as a `mechanistic_hypotheses` pair with `status: EMERGING`, or as a `KNOWLEDGE_GAP` discussion. Do not pick a winner.
7b. **Four death programs converge on the hair cell**, and inflammation is upstream of several.
   > "Cisplatin causes hair cell death by forming DNA adducts, mitochondrial dysfunction, oxidative stress, and inflammation, culminating in programmed cell death by apoptosis, necroptosis, pyroptosis, or ferroptosis." — PMID:38003734
8b. **Hair cells do not regenerate in mammals.** *Results in* permanent, bilateral, high-frequency sensorineural hearing loss, progressing to speech frequencies as cumulative dose rises (PMID:22547603).

**Branch C — dorsal root ganglion.**

4c. **The DRG lies outside a tight blood-nerve barrier and accumulates platinum.** Adducts form in nuclear and mitochondrial DNA of sensory neurons. *Leads to* a sensory neuronopathy rather than a distal axonopathy — which is why the deficit is sensory, length-dependent in presentation but ganglionopathic in origin. **I did not retrieve a primary citation for the blood-nerve-barrier claim this session; treat it as textbook background pending a source.**
5c. **Sensory neuron dysfunction and axonal degeneration** produce paraesthesia, distal sensory loss, areflexia, and sensory ataxia (`HP:0003401`, `HP:0002936`, `HP:0001284`, `HP:0002066`).

**Branch D — bone marrow.**

4d. **Cycling haematopoietic progenitors arrest and die** from the same adduct burden. *Results in* anaemia, neutropenia, thrombocytopenia. This is the branch the existing stub already models, and it is correct as far as it goes.

**Branch E — area postrema and gut.**

4e. **Cisplatin provokes acute and delayed emesis** through enterochromaffin-cell serotonin release and substance P/NK1 signalling. *Results in* the highly emetogenic phenotype that defines cisplatin antiemetic prophylaxis. **I did not verify a primary citation for the enterochromaffin/substance-P step this session.** Curate the phenotype; leave the mechanism uncited or find the source first.

### Ontology bindings for mechanism nodes

All GO terms below verified present in `cache/go/terms.csv` with the labels shown.

| Mechanism step | GO term |
|---|---|
| DNA crosslink formation, repair attempt | `GO:0006281` DNA repair; `GO:0006289` nucleotide-excision repair; `GO:0036297` interstrand cross-link repair |
| DNA-damage apoptosis | `GO:0008630` intrinsic apoptotic signaling pathway in response to DNA damage; `GO:0006915` apoptotic process |
| Oxidative stress | `GO:0006979` response to oxidative stress; `GO:0034614` cellular response to reactive oxygen species |
| Mitochondrial injury | `GO:0051882` mitochondrial depolarization; `GO:0032042` mitochondrial DNA metabolic process |
| ER stress | `GO:0030968` endoplasmic reticulum unfolded protein response |
| Regulated necrosis | `GO:0070266` necroptotic process |
| Iron-dependent lipid peroxidation death | `GO:0097707` ferroptosis |
| Autophagy | `GO:0006914` autophagy |
| Senescence | `GO:0090398` cellular senescence |
| Inflammation | `GO:0006954` inflammatory response; `GO:0001816` cytokine production |
| Uptake | `GO:0006825` copper ion transport (for the CTR1 route) |

Note: pyroptosis is named in PMID:38003734 but I did not verify a GO term for it in the dismech cache. Check before binding.

### Molecular profiling

- **Proteomics / biomarker landscape in vitro.** A 2026 PRISMA systematic review of 58 human proximal-tubule in vitro studies published 2014–2024: "Kidney injury molecule-1 was the most frequently reported structural biomarker. Mechanistic endpoints, particularly oxidative stress and intracellular signaling markers, predominated over structural injury markers." — PMID:42459863, *Front Toxicol* 2026;8:1862941. The same review concludes reporting is not harmonised, which matters if you are mining these datasets.
- **Transcriptomics, metabolomics, lipidomics, single-cell, spatial:** not searched this session. The Nature Reviews Nephrology review explicitly calls for multi-omics and GWAS work, which implies it is not yet mature: "Further research using tumour-bearing animals, multi-omics and genome-wide association studies will enable a comprehensive understanding of the complex cellular and molecular mechanisms of cisplatin nephrotoxicity" — PMID:36229672.

---

## 7. Anatomical Structures Affected

All UBERON and CL terms below verified in the dismech caches or by live OLS4 query.

### Organ level

| Organ / system | UBERON | Role |
|---|---|---|
| Kidney | `UBERON:0002113` | Primary — dose-limiting AKI/CKD |
| Cochlea | `UBERON:0001844` | Primary — irreversible SNHL |
| Dorsal root ganglion | `UBERON:0000044` | Primary — sensory neuronopathy |
| Bone marrow | `UBERON:0002371` | Primary — myelosuppression |
| Peripheral nervous system | `UBERON:0000010` | System-level |
| Testis | `UBERON:0000473` | Gonadal toxicity, infertility |
| Retina | `UBERON:0000966` | Rare retinal toxicity |
| Renal medulla | `UBERON:0000362` | Corticomedullary junction injury |

### Tissue and cell level

| Cell type | CL | Involvement |
|---|---|---|
| Epithelial cell of proximal tubule | `CL:0002306` | Principal target of tubular injury |
| Kidney proximal convoluted tubule epithelial cell | `CL:1000838` | S3 segment most vulnerable |
| Kidney distal convoluted tubule epithelial cell | `CL:1000849` | Magnesium wasting; CTR1 expressed here too (PMID:19144690) |
| Kidney loop of Henle thick ascending limb epithelial cell | `CL:1001106` | Electrolyte handling |
| Kidney interstitial fibroblast | `CL:1000692` | Fibrotic conversion on repeat dosing (PMID:26739893) |
| Macrophage | `CL:0000235` | Inflammatory amplification |
| Cochlear outer hair cell | `CL:0000601` | Principal ototoxic target (PMID:39417180) |
| Cochlear inner hair cell | `CL:0000589` | Later/less affected |
| Supporting cell | `CL:0000630` | Implicated in ototoxic cascade |
| Spiral ganglion neuron | `CL:0011113` | Secondary degeneration |
| Sensory neuron of dorsal root ganglion | `CL:1001451` | CIPN substrate |
| Schwann cell | `CL:0002573` | Myelin; secondary |
| Hematopoietic stem cell | `CL:0000037` | Myelosuppression |

### Localization detail

- Spiral organ of cochlea: `UBERON:0002227` (label "spiral organ of cochlea" — verified live via OLS4; note the label is *not* "organ of Corti")
- Stria vascularis of cochlear duct: `UBERON:0002282` (verified live via OLS4) — the site of highest platinum accumulation (PMID:29162831)
- Proximal tubule: `UBERON:0004134`; nephron tubule: `UBERON:0001231`

### Lateralization

Bilateral and broadly symmetric across all organ branches. Ototoxicity is explicitly bilateral (PMID:38003734). Neuropathy is symmetric and length-dependent.

### Subcellular

Nucleus (DNA adducts), mitochondrion (mitochondrial DNA adducts, depolarization, permeability transition), endoplasmic reticulum (unfolded protein response). I did not verify GO Cellular Component identifiers this session.

---

## 8. Temporal Development

### Onset

- **Acute emesis:** hours after infusion.
- **AKI:** the BMJ study defines the outcome window as "within 14 days of a first dose of intravenous cisplatin" (PMID:38538012). Peak creatinine typically 7–10 days.
- **Myelosuppression:** nadir around 10–14 days per cycle.
- **Hypomagnesemia:** develops over cycles and is often persistent.
- **Ototoxicity:** may be detectable after a single course; ACCL0431's primary endpoint was hearing loss "4 weeks after final cisplatin dose" (PMID:27914822), while SIOPEL 6 assessed at "a minimum age of 3.5 years" (PMID:29924955) — which tells you the deficit is stable enough to measure years later.
- **CIPN:** typically emerges after several cycles; may progress after cessation.

### Progression and course

| Toxicity | Course | Reversible? |
|---|---|---|
| Emesis | Episodic, per cycle | Yes |
| Myelosuppression | Cyclic, cumulative | Largely yes |
| AKI | Acute; may repeat each cycle | Partly — repeated injury converts to CKD (PMID:26739893, PMID:36229672) |
| Hypomagnesemia | Chronic, cumulative | Often persists post-treatment |
| Ototoxicity | Progressive with cumulative dose; then stable | **No** — "irreversible" (PMID:38003734) |
| CIPN | Progressive during and shortly after treatment; partial recovery over years | Partial |

The dose-frequency relationship for hearing is stated directly: "Platinum initially impairs hearing in the high frequencies and progresses to lower frequencies with increasing cumulative dose." (PMID:22547603)

### Critical windows

- **The 6-hour window after cisplatin.** Both randomised otoprotection trials gave sodium thiosulfate exactly 6 hours after the cisplatin infusion ended — SIOPEL 6: "20 g per square meter, administered intravenously over a 15-minute period, 6 hours after the discontinuation of cisplatin"; ACCL0431: "sodium thiosulfate 16 g/m2 intravenously 6 h after each cisplatin dose". The delay is the whole design. Give it earlier and it may quench the drug's antitumour effect. Brock's consensus review names this: "Route of administration and optimal timing relative to platinum therapy are critical issues." (PMID:22547603)
- **The cumulative-dose threshold.** Ototoxicity risk rises steeply; ACCL0431's FDA-relevant framing used cumulative cisplatin ≥200 mg/m².
- **Early childhood.** Hearing loss during speech acquisition causes developmental language delay (PMID:38003734), which is why the paediatric otoprotection trials exist.

---

## 9. Inheritance and Population

### Epidemiology

This is an iatrogenic condition, so "prevalence" is prevalence-among-the-exposed, not population prevalence. Curate it that way — the dismech `Prevalence.population` slot should name the treated cohort, not a geography.

| Measure | Value | Population | Source |
|---|---|---|---|
| Candidate treated population | ~500,000/year in the US | Patients with germ cell, lung, bladder, ovarian, head and neck cancer | PMID:36921239 |
| Ototoxicity, adults | 40–60% | Cisplatin-treated adults | PMID:38003734 |
| Ototoxicity, children | up to 60%; "at least 60%" | Paediatric cisplatin recipients | PMID:38003734; PMID:22547603 |
| Permanent hearing loss | 40–80% | All treated | PMID:29162831 |
| Any ototoxicity, self-reported | 74% | 145 testicular cancer survivors | PMID:36637632 |
| Chemotherapy ototoxicity, all agents | >50% incidence, ~4 million people/year worldwide | All chemo recipients | PMID:39417180 |
| Severe CP-AKI (≥2× creatinine or KRT within 14 d) | 5.2% derivation / 3.3% validation | 24,717 adults, 6 US centres | PMID:38538012 |
| Nephrotoxicity, any grade | "up to 20%" | Cisplatin recipients | PMID:37530867 |
| Nephrotoxicity, any grade | "up to one third of patients" | Cisplatin recipients | PMID:41854743 |

> "Ototoxicity is an often-underestimated sequela for cancer patients undergoing chemotherapy, with an incidence rate exceeding 50%, affecting approximately 4 million individuals worldwide each year."
> — PMID:39417180

> "Approximately 500,000 patients diagnosed annually with these cancer types in the United States could be candidates for treatment with cisplatin. There is a 5-fold increase in the risk of hearing impairment or ototoxicity with cisplatin"
> — PMID:36921239

### Inheritance

Not a heritable disease. **Susceptibility** is polygenic and modestly penetrant. If curating an `Inheritance` block at all, `HP:0010982` polygenic inheritance with `relationship_type: SUSCEPTIBILITY` gene typing is the honest binding — but consider whether the entry needs one. There is no penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency to report, because there is no Mendelian disease.

### Demographics

- **Sex ratio:** determined entirely by the cancer indication, not by the toxicity. Testicular cancer cohorts are male by construction; cervical and ovarian cohorts female.
- **Age:** bimodal by indication — paediatric solid tumours (neuroblastoma, osteosarcoma, hepatoblastoma, medulloblastoma) and adult carcinomas.
- **Geography:** wherever cisplatin is used, which is globally. Cohort studies retrieved include the US (PMID:38538012), South Africa (PMID:37014872, title only), and Zimbabwe (PMID:39056302, title only). Those last two suggest the burden in cervical-cancer treatment in sub-Saharan Africa is being characterised now; I did not read either abstract.
- **Ancestry:** the pharmacogenomic literature is dominated by European-ancestry cohorts. PMID:37726872 explicitly calls for "replication studies considering diverse pediatric and adult patient populations". Treat any ancestry-specific effect size as unreplicated.

---

## 10. Diagnostics

Cisplatin toxicity is diagnosed by **monitoring during and after a known exposure**, not by a diagnostic test applied to an undifferentiated patient.

### Laboratory

| Test | Purpose |
|---|---|
| Serum creatinine, eGFR | The defining AKI measurement (PMID:38538012) |
| Serum magnesium | Both a toxicity marker and an AKI predictor (PMID:38538012) |
| Serum potassium, calcium, sodium, phosphate | Tubular wasting |
| Complete blood count | Myelosuppression nadir monitoring |
| Urinalysis, urine protein | Tubular injury |

### Biomarkers

Kidney injury molecule-1 (KIM-1, gene `HAVCR1`) is the most-used structural biomarker in the experimental literature:

> "Fifty-eight studies met inclusion criteria. Kidney injury molecule-1 was the most frequently reported structural biomarker."
> — PMID:42459863

Urinary TIMP-2×IGFBP-7 has been evaluated in children receiving cisplatin (PMID:37365422, *Pediatr Nephrol* — title verified, abstract **not read**). Neither KIM-1 nor TIMP-2×IGFBP-7 is standard of care for this indication.

### Audiology

This is the one place cisplatin toxicity has a purpose-built diagnostic standard.

- **Pure-tone audiometry** including extended high frequencies, at baseline and serially. SIOPEL 6's primary endpoint was "the absolute hearing threshold, as measured by pure-tone audiometry" (PMID:29924955).
- **Grading scales:** the **SIOP Boston Ototoxicity Scale** was created specifically for this (PMID:22547603). The **Brock grade** (0–4) is the older paediatric scale used as SIOPEL 6's endpoint: "Hearing loss was assessed according to the Brock grade (on a scale from 0 to 4, with higher grades indicating greater hearing loss)." ACCL0431 used **ASHA criteria** with masked central audiologist review.
- Otoacoustic emissions detect outer-hair-cell loss early. **Not verified against a source this session.**

**The gap is in adults, and it is a real one:**

> "Our review of the literature showed a lack of standardized guidelines for monitoring and treatment of cisplatin-induced ototoxicity, especially in the adult cancer patient population. Our survey of practicing oncologists mirrored the findings from the published literature with a heterogeneity of practice, which highlights the need for standardization."
> — PMID:36921239

### Neurologic

Clinical sensory examination, vibration and proprioception testing, patient-reported outcome instruments. Nerve conduction studies show a sensory axonal/neuronopathic pattern. **NCS pattern not verified against a source this session.**

### Genetic testing

`ACYP2` and `TPMT` genotyping is the only pharmacogenomic testing with a defensible evidence base (PMID:37726872), and even that review stops short of recommending clinical implementation, calling instead for further replication. **There is no CPIC guideline for cisplatin ototoxicity that I could confirm in this session.** Do not curate one.

WGS, WES, gene panels, CMA, karyotype, FISH, mtDNA testing, and repeat-expansion testing: not applicable.

### Differential diagnosis

| Alternative | Distinguishing feature |
|---|---|
| Prerenal azotemia / volume depletion | Responds to fluids; bland sediment; FENa low |
| Contrast-associated AKI | Temporal relation to contrast, not to cisplatin |
| Aminoglycoside nephrotoxicity | Concurrent drug; also causes ototoxicity — confounds attribution directly |
| Tumour lysis syndrome | Uric acid, phosphate, potassium rise; timing at treatment initiation |
| Age-related or noise-induced hearing loss | Pre-treatment audiogram is the discriminator — which is why baseline audiometry matters |
| Paraneoplastic sensory neuronopathy | Anti-Hu; may precede chemotherapy |
| Diabetic or B12-deficiency neuropathy | Pre-existing; separate workup |

### Screening

Baseline audiometry before the first dose, and baseline creatinine and magnesium. There is no population screening, because there is no population at risk that is not already identified by the prescription.

---

## 11. Outcome/Prognosis

### Mortality

Severe CP-AKI is not a nuisance toxicity. It tracks with death:

> "Greater severity of CP-AKI was monotonically associated with shorter 90 day survival (adjusted hazard ratio 4.63 (95% CI 3.56 to 6.02) for stage 3 CP-AKI versus no CP-AKI)."
> — PMID:38538012

> "This study found that a simple risk score based on readily available variables from patients receiving intravenous cisplatin could predict the risk of severe CP-AKI, the occurrence of which is strongly associated with death."
> — PMID:38538012

**Read that association carefully.** It is not established that the AKI causes the deaths; sicker patients get both. The paper reports association, and so should the KB entry.

### Morbidity and recovery

| Outcome | Recovery |
|---|---|
| Hearing loss | None. Irreversible (PMID:38003734). Hearing aids do not repair the cochlea: "Contemporary medical interventions for cisplatin ototoxicity are limited to prosthetic devices, such as hearing aids, but these have significant limitations because the cochlea remains damaged." (PMID:38003734) |
| AKI | Partial; repeated cycles drive fibrosis and CKD (PMID:26739893, PMID:36229672) |
| CIPN | Partial over years; often incomplete |
| Myelosuppression | Full between cycles |
| Hypomagnesemia | Often persistent |

Long-term burden in survivors, median 4.3 years out: 37.6% of testicular cancer survivors reported three or more adverse health outcomes, and 12.5% reported five or more (PMID:28240972).

### Prognostic factors

Age, cumulative cisplatin dose, baseline renal function, baseline magnesium, hypertension, diabetes, and infusion schedule. The BMJ nine-covariate risk score is the best-validated instrument:

> "Compared with patients in the lowest risk category, those in the highest risk category showed a 24.00-fold (95% confidence interval (CI) 13.49-fold to 42.78-fold) higher odds of CP-AKI in the derivation cohort and a 17.87-fold (10.56-fold to 29.60-fold) higher odds in the validation cohort. The primary model had a C statistic of 0.75 and showed better discrimination for CP-AKI than previously published models, the C statistics for which ranged from 0.60 to 0.68."
> — PMID:38538012

A C statistic of 0.75 is useful and is not a decision rule. It discriminates better than everything before it and still misclassifies plenty.

### Quality of life

No cisplatin-toxicity-specific EQ-5D, SF-36, or PROMIS utility values were retrieved. The reviews describe QoL impact narratively (PMID:36921239: "with major impact on patients' health-related quality of life"; PMID:38003734 on social isolation and developmental delay). If a QoL number is needed for the entry, it has not been found yet.

---

## 12. Treatment

### Sodium thiosulfate — the only approved otoprotectant

Two randomised phase 3 trials, both giving the drug 6 hours after cisplatin.

**ACCL0431** (Children's Oncology Group, 38 sites, NCT00716976):

> "Participants received sodium thiosulfate 16 g/m2 intravenously 6 h after each cisplatin dose or observation."
> "Hearing loss was identified in 14 (28·6%; 95% CI 16·6-43·3) participants in the sodium thiosulfate group compared with 31 (56·4%; 42·3-69·7) in the control group (p=0·00022). Adjusted for stratification variables, the likelihood of hearing loss was significantly lower in the sodium thiosulfate group compared with the control group (odds ratio 0·31, 95% CI 0·13-0·73; p=0·0036)."
> — PMID:27914822, *Lancet Oncol* 2017;18(1):63-74

**SIOPEL 6** (standard-risk hepatoblastoma, NCT00652132):

> "Hearing loss of grade 1 or higher occurred in 18 of 55 children (33%) in the cisplatin-sodium thiosulfate group, as compared with 29 of 46 (63%) in the cisplatin-alone group, indicating a 48% lower incidence of hearing loss in the cisplatin-sodium thiosulfate group (relative risk, 0.52; 95% confidence interval [CI], 0.33 to 0.81; P=0.002)."
> "At a median of 52 months of follow-up, the 3-year rates of event-free survival were 82% (95% CI, 69 to 90) in the cisplatin-sodium thiosulfate group and 79% (95% CI, 65 to 88) in the cisplatin-alone group, and the 3-year rates of overall survival were 98% (95% CI, 88 to 100) and 92% (95% CI, 81 to 97), respectively."
> — PMID:29924955, *N Engl J Med* 2018;378(25):2376-2385

**Regulatory status.** The FDA approved sodium thiosulfate (Pedmark, Fennec Pharmaceuticals) on 2022-09-20 to reduce the risk of ototoxicity in patients aged 1 month to 18 years with localised, non-metastatic solid tumours. The 2023 review states it as fact: "Recently, the U.S. Food and Drug Administration (FDA) approved the first therapy, sodium thiosulfate, to prevent cisplatin-induced hearing loss in pediatric patients with localized, non-metastatic solid tumors." (PMID:38003734). **The approval date and sponsor come from a web search summary in this session and were not confirmed against an FDA primary document.**

**The efficacy caveat that matters.** Otoprotection is a trade against tumour kill, and the field says so: "Otoprotection is a strategy being explored to decrease hearing loss while maintaining dose intensity or allowing dose escalation, but it has the potential to interfere with tumoricidal effects." (PMID:22547603). This is why the label is restricted to localised, non-metastatic disease.

### Nephroprotection

- **Intravenous hydration** is the backbone and is not in dispute.
- **Magnesium supplementation** during hydration: OR 0.22 (95% CI 0.14–0.35) against CIN in a meta-analysis of 11 retrospective studies (PMID:37530867), and a 2026 meta-analysis found no dose-response across <10 mEq, 10–<20 mEq, and ≥20 mEq groups (PMID:42652681).
- **Nothing else is established.** The 2026 Kidney360 review states the position bluntly: "its dose-limiting nephrotoxicity affects up to one third of patients and has no effective pharmacologic prevention beyond hydration and magnesium supplementation." (PMID:41854743)
- **Mannitol** addition to hydration has been studied ambispectively (PMID:35413808, title verified, abstract **not read**). Evidence is not strong.
- **Amifostine** (`NCIT:C488`) is the classic cytoprotectant. I did not retrieve a current guideline recommendation for it in cisplatin nephroprotection this session. Do not curate an ASCO recommendation for it without reading the guideline.

**Emerging: SGLT2 inhibitors.** Preclinical only, and the review is honest that it is preclinical only:

> "Across these models, SGLT2 inhibitors consistently attenuated kidney injury through complementary mechanisms such as suppression of inflammatory, oxidative, and apoptotic pathways; activation of AMP-activated protein kinase-dependent autophagy; reduction of kidney platinum accumulation; and, uniquely, correction of cisplatin-induced hypomagnesemia, a clinically significant complication. Protective effects occurred without compromising cisplatin's antitumor efficacy in vitro. ... Although prospective clinical application remains untested, the strong biologic rationale, reproducibility across models, and established safety of SGLT2 inhibitors in other populations underscore the urgency of translation."
> — PMID:41854743, *Kidney360* 2026;7(5):1150-1159 (seven non-diabetic rodent studies; **MODEL_ORGANISM**)

### CIPN

The ASCO 2020 guideline update is unambiguous and mostly negative:

> "The identified data reconfirmed that no agents are recommended for the prevention of CIPN. The use of acetyl-l-carnitine for the prevention of CIPN in patients with cancer should be discouraged. Furthermore, clinicians should assess the appropriateness of dose delaying, dose reduction, substitutions, or stopping chemotherapy in patients who develop intolerable neuropathy and/or functional impairment. Duloxetine is the only agent that has appropriate evidence to support its use for patients with established painful CIPN. Nonetheless, the amount of benefit from duloxetine is limited."
> — PMID:32663120, *J Clin Oncol* 2020;38(28):3325-3348

Duloxetine binds to `CHEBI:36796`.

### Antiemesis

Cisplatin is the reference highly emetogenic agent. Standard prophylaxis is a four-drug regimen: NK1 receptor antagonist, 5-HT3 antagonist, dexamethasone (`CHEBI:41879`), and olanzapine (`CHEBI:7735`). **I could not retrieve the current ASCO antiemetic guideline PMID in this session.** Curate the regimen only with a guideline citation you have read.

### Dose modification and supportive care

Dose reduction, delay, or substitution (usually to carboplatin) remains the primary management for established toxicity — ASCO says so for neuropathy above, and the same logic drives renal and otologic dose decisions. Supportive care includes transfusion, growth factors, magnesium and potassium repletion, hearing aids or cochlear implantation for severe loss, and dialysis for severe AKI.

### NCIT bindings

All verified against the dismech `cache/ncit/terms.csv` or live OLS4.

| Treatment | `treatment_term` (clinical action) | `therapeutic_agent` |
|---|---|---|
| Sodium thiosulfate otoprotection | `NCIT:C15986` Pharmacotherapy | `NCIT:C1230` Sodium Thiosulfate |
| Amifostine cytoprotection | `NCIT:C15986` Pharmacotherapy | `NCIT:C488` Amifostine |
| Magnesium supplementation | `NCIT:C15986` Pharmacotherapy | Term not resolved this session |
| Intravenous hydration | `NCIT:C15747` Supportive Care | — |
| Duloxetine for painful CIPN | `NCIT:C15986` Pharmacotherapy | `CHEBI:36796` duloxetine |
| Antiemetic prophylaxis | `NCIT:C15986` Pharmacotherapy | `CHEBI:7773` Ondansetron; `CHEBI:41879` dexamethasone; `CHEBI:7735` olanzapine |
| Hemodialysis for severe AKI | `NCIT:C15248` Hemodialysis | — |
| Transfusion support | `NCIT:C15192` Blood Transfusion | — |
| Hearing rehabilitation | `NCIT:C15302` Physical Therapy is **wrong** here; use `NCIT:C15315` Rehabilitation or `NCIT:C15329` Surgical Procedure for implantation, per the device convention in CLAUDE.md | Device term as a `qualifiers` pair |
| Dose reduction / discontinuation | `NCIT:C49236` Therapeutic Procedure | — |

**`NCIT:C1230` and `NCIT:C488` are agent terms, not clinical-action terms.** They are not reachable from `NCIT:C25218` and will fail `TreatmentTerm` validation if put in the `treatment_term.term` slot. They belong in `therapeutic_agent`. I did not confirm their reachability either way; check before binding.

---

## 13. Prevention

### Primary prevention

The only complete primary prevention is not giving cisplatin. That is a real clinical option — carboplatin substitution trades ototoxicity and nephrotoxicity for myelosuppression, at some cost in efficacy for certain tumours.

Everything else is risk reduction:

| Intervention | Level | Evidence |
|---|---|---|
| IV hydration | Primary | Standard of care; PMID:41854743 |
| Magnesium supplementation | Primary | OR 0.22 vs CIN (PMID:37530867); dose-independent (PMID:42652681) |
| Sodium thiosulfate, 6 h post-infusion | Primary (hearing, children) | RR 0.52 (PMID:29924955); OR 0.31 (PMID:27914822) |
| Prolonged infusion (>6 h) rather than bolus | Primary | Implied by ACCL0431 eligibility and stratification (PMID:27914822); direct comparative evidence **not verified** |
| Avoiding concurrent nephrotoxins | Primary | Consistent with PMID:38538012 risk factors |
| Noise avoidance during and after treatment | Primary (hearing) | Association only (PMID:35322580) |
| Risk stratification with the BMJ nine-covariate score | Primary | C statistic 0.75, externally validated (PMID:38538012) |

### Secondary prevention

Baseline and serial audiometry, so hearing loss is caught at the high frequencies before it reaches speech frequencies and a dose decision can still be made. Serial creatinine and magnesium for the same reason. The adult monitoring gap identified in PMID:36921239 is precisely a secondary-prevention failure.

### Tertiary prevention

Dose reduction, delay, or discontinuation after toxicity appears — the ASCO CIPN guideline's explicit recommendation (PMID:32663120). Hearing aids and cochlear implantation. CKD management after repeated AKI.

### Not applicable

Immunisation. Genetic screening (no clinically actionable genotype-directed protocol exists — see §10). Prenatal or carrier testing. Public health or environmental interventions. Genetic counselling.

---

## 14. Other Species / Natural Disease

**There is no natural disease here.** Cisplatin toxicity in animals is induced, always. There is no wildlife or companion-animal population that acquires it spontaneously, and OMIA has nothing to record.

- **Species used and affected experimentally:** *Mus musculus* (`NCBITaxon:10090`), *Rattus norvegicus* (`NCBITaxon:10116`), *Danio rerio* (`NCBITaxon:7955`), *Homo sapiens* (`NCBITaxon:9606`). **NCBITaxon identifiers written from knowledge; not verified this session.**
- **Veterinary relevance.** Cisplatin is used therapeutically in dogs, chiefly for osteosarcoma, and produces the same nephrotoxicity requiring saline diuresis. Cisplatin is **contraindicated in cats**, in which it causes fatal pulmonary oedema. Both statements are well established in veterinary oncology. **I searched PubMed for a primary citation in this session and found none** — the searches returned zero results. Do not curate either claim without a source you have read. The cat contraindication is important enough that it is worth finding one.
- **Comparative pathology.** The cochlear retention finding is directly comparative and was measured in both species: "the cochlea retains cisplatin for months to years after treatment in both mice and humans" (PMID:29162831). That cross-species agreement is what makes the mouse cochlea a credible model.
- **Evolutionary conservation.** CTR1 is a copper transporter; the platinum uptake it mediates is an off-target consequence of a deeply conserved metal-handling system. The DNA adduct chemistry is species-independent.
- **Zoonotic potential:** none. Not transmissible.

---

## 15. Model Organisms

### Whole-animal models

| Model | System | What it recapitulates | Limitations |
|---|---|---|---|
| Single high-dose cisplatin mouse (typically 20–30 mg/kg IP) | Mouse | Rapid, severe AKI with tubular necrosis | Not the clinical regimen; lethality confounds; does not model CKD conversion |
| **Repeated low-dose cisplatin mouse** | Mouse | Fibrosis and CKD — "Repeated administration of low-dose cisplatin in mice induces fibrosis." (PMID:26739893) | Longer, more expensive; still not tumour-bearing |
| Mouse cochlear ototoxicity model | Mouse | Outer hair cell loss; platinum retention in cochlea matching human (PMID:29162831) | Frequency range and cochlear anatomy differ from human |
| Rat CIPN model | Rat | DRG platinum accumulation, sensory deficits | Behavioural readouts are indirect |
| Zebrafish lateral-line neuromast | Zebrafish | Hair-cell death; high-throughput otoprotectant screening (PMID:29381431 — title from search, **abstract not read**) | Neuromast hair cells are not cochlear hair cells; no cochlea |

**The single most important limitation, stated by the field itself.** Almost all mechanistic work is done in tumour-free animals, which cannot answer whether a renoprotectant also protects the tumour:

> "Importantly, it is unclear whether these approaches would limit the anticancer effects of cisplatin in tumors. Examination of tumor-bearing animals and identification of novel renoprotective strategies that do not diminish the anticancer efficacy of cisplatin are essential to the development of clinically applicable interventions."
> — PMID:18272962, *Kidney Int* 2008;73(9):994-1007

Restated fifteen years later, still open:

> "However, the effects of renoprotective strategies on the efficacy of cisplatin chemotherapy needs to be thoroughly evaluated. Further research using tumour-bearing animals, multi-omics and genome-wide association studies will enable a comprehensive understanding..."
> — PMID:36229672

That is a `HUMAN_MODEL_MISMATCH` in the dismech sense, and it is the one worth curating.

### Non-animal models (dismech `experimental_models:`)

| Model | What it shows | Limitation — verbatim where available |
|---|---|---|
| **iPSC-derived human kidney organoid** | Injury response, AKI biomarker secretion, inflammatory cytokines | "DNA damage was not specific to the proximal tubule but also affected the distal tubule and interstitial cell populations. This lack of specificity correlated with low expression of proximal tubule-specific SLC22A2/organic cation transporter 2 (OCT2) for cisplatin." — PMID:32150447. **This is the key limitation: the organoid underexpresses the transporter that gives the human kidney its selectivity.** |
| Organoid, repeated low-dose protocol | Better viability, robust injury | "we developed a repeated low-dose regimen of 4 × 5 µM cisplatin over 7 days and found this caused less toxicity while still inducing a robust injury response that included secretion of known AKI biomarkers and inflammatory cytokines" — PMID:32150447 |
| HK-2 and other human proximal tubule cell lines | Mechanistic dissection; the workhorse of the field (58 studies, 2014–2024) | Reporting is unharmonised: "Co-reporting analysis revealed recurrent pathway-oriented groupings, suggesting hypothesis-driven panel selection rather than standardized implementation across studies." — PMID:42459863 |
| Organotypic cochlear explant culture | Hair-cell death, otoprotectant screening | Loses the stria vascularis contribution and systemic pharmacokinetics — which PMID:29162831 and PMID:39417180 both argue may be where the primary lesion is |

If curating `modeled_mechanisms` links, the organoid model against a proximal-tubule injury node should be `PARTIALLY_RECAPITULATES` with `fidelity: MODERATE` and the OCT2 underexpression written into `limitations`. The mouse cochlear model against a cochlear platinum-retention node can carry `RECAPITULATES` with `fidelity: HIGH`, since PMID:29162831 measured the same phenomenon in both species.

### Resources

MGI, RGD, ZFIN, IMPC, Cellosaurus, ATCC. Not queried this session.

---

## Curation notes for the dismech entry

Six things worth flagging before this becomes a KB entry.

1. **The current stub models one branch of five.** `kb/disorders/Cisplatin_Toxicity.yaml` has Platinum-DNA Adduct Formation → Bone Marrow Hematopoietic Suppression. That edge is correct. It is also the least clinically important of the five branches. The renal, cochlear, and neural branches all hang off the same trigger node and are missing.
2. **Pathograph targets are bare names.** The stub's `downstream[].target: Bone Marrow Hematopoietic Suppression` is right. Keep every new target bare — no `pathophysiology#` prefix — per the causal-target rule in CLAUDE.md.
3. **`conforms_to` candidates beyond myelosuppression.** The peripheral axonal degeneration module is the natural target for the CIPN branch, and CLAUDE.md names it explicitly as a toxicity conformance target. Check `just list-modules` for an AKI or tubular-injury module before inventing one.
4. **Genes are `SUSCEPTIBILITY`, never `CAUSATIVE`.** `ACYP2` and `TPMT` only. `COMT` did not replicate and should not be curated as established.
5. **Do not average the AKI incidence figures.** 3–5% (severe, BMJ), up to 20% (PMID:37530867), and up to one third (PMID:41854743) use three different endpoint definitions. Curate each as its own `Prevalence` record with the definition in `notes`.
6. **The `HP:0001875` label is now "Decreased total neutrophil count".** OLS4 returns that, not "Neutropenia". The dismech HP cache does not contain the term, so nothing local will catch a stale label.

---

## Sources

- [Cisplatin nephrotoxicity: new insights and therapeutic implications — Nat Rev Nephrol 2023, PMID:36229672](https://pubmed.ncbi.nlm.nih.gov/36229672/)
- [Advances in understanding cisplatin-induced toxicity — Eur J Pharm Sci 2024, PMID:39423903](https://pubmed.ncbi.nlm.nih.gov/39423903/)
- [Molecular Characteristics of Cisplatin-Induced Ototoxicity — Int J Mol Sci 2023, PMID:38003734](https://pubmed.ncbi.nlm.nih.gov/38003734/)
- [Canadian Pharmacogenomics Network for Drug Safety 2022 Update — Ther Drug Monit 2023, PMID:37726872](https://pubmed.ncbi.nlm.nih.gov/37726872/)
- [Derivation and external validation of a risk score for severe CP-AKI — BMJ 2024, PMID:38538012](https://pubmed.ncbi.nlm.nih.gov/38538012/)
- [Cisplatin Nephrotoxicity: Novel Insights — Semin Nephrol 2022, PMID:37182407](https://pubmed.ncbi.nlm.nih.gov/37182407/)
- [Prevalence and risk factors for ototoxicity after cisplatin-based chemotherapy — J Cancer Surviv 2023, PMID:36637632](https://pubmed.ncbi.nlm.nih.gov/36637632/)
- [Cisplatin-Induced Ototoxicity: Burden, Prevention, Interception — JCO Oncol Pract 2023, PMID:36921239](https://pubmed.ncbi.nlm.nih.gov/36921239/)
- [Hearing loss during chemotherapy — Am J Cancer Res 2024, PMID:39417180](https://pubmed.ncbi.nlm.nih.gov/39417180/)
- [Cisplatin is retained in the cochlea indefinitely — Nat Commun 2017, PMID:29162831](https://pubmed.ncbi.nlm.nih.gov/29162831/)
- [SIOP Boston ototoxicity scale consensus review — J Clin Oncol 2012, PMID:22547603](https://pubmed.ncbi.nlm.nih.gov/22547603/)
- [Sodium Thiosulfate for Protection from Cisplatin-Induced Hearing Loss (SIOPEL 6) — NEJM 2018, PMID:29924955](https://pubmed.ncbi.nlm.nih.gov/29924955/)
- [Sodium thiosulfate versus observation (ACCL0431) — Lancet Oncol 2017, PMID:27914822](https://pubmed.ncbi.nlm.nih.gov/27914822/)
- [Adverse Health Outcomes Among North American Testicular Cancer Survivors — J Clin Oncol 2017, PMID:28240972](https://pubmed.ncbi.nlm.nih.gov/28240972/)
- [Pharmacogenomics of cisplatin-induced neurotoxicities — Cancer Med 2022, PMID:35322580](https://pubmed.ncbi.nlm.nih.gov/35322580/)
- [The copper transporter Ctr1 contributes to cisplatin uptake — Am J Physiol Renal Physiol 2009, PMID:19144690](https://pubmed.ncbi.nlm.nih.gov/19144690/)
- [Cisplatin nephrotoxicity: mechanisms and renoprotective strategies — Kidney Int 2008, PMID:18272962](https://pubmed.ncbi.nlm.nih.gov/18272962/)
- [Cisplatin in cancer therapy: molecular mechanisms of action — Eur J Pharmacol 2014, PMID:25058905](https://pubmed.ncbi.nlm.nih.gov/25058905/)
- [Repeated administration of low-dose cisplatin in mice induces fibrosis — Am J Physiol Renal Physiol 2016, PMID:26739893](https://pubmed.ncbi.nlm.nih.gov/26739893/)
- [Evaluation of cisplatin-induced injury in human kidney organoids — Am J Physiol Renal Physiol 2020, PMID:32150447](https://pubmed.ncbi.nlm.nih.gov/32150447/)
- [Hydration protocols and magnesium supplementation meta-analysis — Clin Exp Nephrol 2024, PMID:37530867](https://pubmed.ncbi.nlm.nih.gov/37530867/)
- [Prophylactic Magnesium Therapy meta-analysis — J Clin Med 2026, PMID:42652681](https://pubmed.ncbi.nlm.nih.gov/42652681/)
- [SGLT2 Inhibitors in Cisplatin Nephrotoxicity: A Mechanistic Review — Kidney360 2026, PMID:41854743](https://pubmed.ncbi.nlm.nih.gov/41854743/)
- [Biomarker selection in human proximal tubular in vitro models — Front Toxicol 2026, PMID:42459863](https://pubmed.ncbi.nlm.nih.gov/42459863/)
- [Baicalein alleviates cisplatin-induced AKI by inhibiting ALOX12-dependent ferroptosis — Phytomedicine 2024, PMID:38805781](https://pubmed.ncbi.nlm.nih.gov/38805781/)
- [Prevention and Management of CIPN: ASCO Guideline Update — J Clin Oncol 2020, PMID:32663120](https://pubmed.ncbi.nlm.nih.gov/32663120/)
- [MeSH descriptor D002945, Cisplatin — NCBI](https://www.ncbi.nlm.nih.gov/mesh/68002945)
- [MONDO:0027664 cisplatin toxicity — EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0027664)
- [FDA approves sodium thiosulfate — NCI Cancer Currents](https://www.cancer.gov/news-events/cancer-currents-blog/2022/fda-sodium-thiosulfate-cisplatin-hearing-loss-children)

---

## What I did not verify

Stated plainly so nothing here gets curated on my word alone.

- ICD-10, ICD-11, SNOMED CT, LOINC, and RxNorm identifiers. None checked against their authorities.
- The MeSH descriptor UI for "Ototoxicity". My query for `D000079761` returned no summary.
- NCBITaxon identifiers for mouse, rat, and zebrafish. Written from memory.
- Whether `NCIT:C1230` and `NCIT:C488` are reachable from `NCIT:C25218`. They are agent terms and probably are not.
- The FDA approval date and sponsor for Pedmark. Taken from a web search summary, not an FDA document.
- The cat contraindication and the dog osteosarcoma indication. **PubMed returned zero results for my searches.** Find a source before curating either.
- Coasting in platinum neuropathy. No primary citation retrieved.
- The blood-nerve-barrier explanation for DRG selectivity. Textbook background, uncited here.
- The enterochromaffin-cell/substance-P emesis mechanism. No citation retrieved.
- The TRPM6 link to cisplatin hypomagnesemia. A PubMed search for it returned no items.
- The current ASCO antiemetic guideline. Not located.
- Allele frequencies for `ACYP2` and `TPMT` variants. Not retrieved.
- Any CPIC guideline for cisplatin. I do not believe one exists; I did not confirm its absence.
- Transcriptomic, metabolomic, lipidomic, single-cell, and spatial datasets. Not searched.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.
