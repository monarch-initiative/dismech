---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:25.686851'
end_time: '2026-10-14T15:52:48.824203'
duration_seconds: 203.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Female Infertility Due To Zona Pellucida Defect
  mondo_id: MONDO:0014342
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5-5
  web_search_requests: 7
  num_turns: 14
  total_cost_usd: 2.151764
  session_id: 793ebe12-bd9b-4a83-8638-aa731815b844
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Female Infertility Due To Zona Pellucida Defect
- **MONDO ID:** MONDO:0014342 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Female Infertility Due To Zona Pellucida Defect** covering all of the
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

Checking a few last details: the 2025 BJOG cohort, ZP2 and ZP3 nosology, and the identifiers. After that I'll write the report.

# Female Infertility Due to Zona Pellucida Defect (OOMD1; ZP1-related): Research Report

**Target:** MONDO:0014342 · OMIM 615774 · ORPHA:404466 · Category: Mendelian
**Report date:** 2026-10-14

**How to read the citations.** I took the direct quotes marked "abstract quote" from abstracts already cached in this repository's `references_cache/`, or from the existing draft entry `kb/disorders/Female_Infertility_Due_To_Zona_Pellucida_Defect.yaml`, which has passed snippet validation. Claims marked **[unverified]** came from web search or memory and need a PMID lookup with `just fetch-reference` before they are used as evidence. Some ontology IDs are marked "ID to look up"; I was not able to source those IDs, so I did not write them.

**Tooling note.** The PubMed, OLS and bgpt MCP connectors in this session need authorization through claude.ai connector settings, and I could not use them here. OMIM returned HTTP 403. Identifiers were confirmed through NCBI MedGen instead.

---

## 1. Disease Information

**Overview.** The disorder is an autosomal recessive form of primary female infertility, with a smaller autosomal dominant arm. It is caused mainly by pathogenic variants in **ZP1**, which encodes zona pellucida glycoprotein 1. ZP1 cross-links the filaments of the zona pellucida (ZP), the extracellular coat around the oocyte.

Affected women otherwise look reproductively normal: normal karyotype, menarche, menstrual cycles, hormone levels, ovarian reserve and tubal/uterine anatomy. The defect only shows up during ART cycles. Retrieval then yields one of three things:
- no oocytes at all (genuine empty follicle syndrome, GEFS);
- shrivelled, degenerated oocytes;
- mature MII oocytes with no ZP, or a very thin one, which fail conventional IVF.

> "Here we describe a form of infertility with an autosomal recessive mode of inheritance, characterized by abnormal eggs that lack a zona pellucida. We identified a homozygous frameshift mutation in ZP1 in six family members." — Huang et al., *NEJM* 2014, PMID:24670168 (abstract quote)

**Identifiers** (from NCBI MedGen C4014291, MedGen UID 862728):

| Resource | ID |
|---|---|
| MONDO | MONDO:0014342 |
| OMIM | 615774 (gene ZP1, OMIM 195000 **[verify]**) |
| Orphanet | ORPHA:404466 |
| MedGen | C4014291 |
| Gene locus | ZP1, 11q12.2; HGNC hgnc:13187 |
| ICD-10 / ICD-11 | No specific code. Nearest are N97.x (female infertility) and ICD-11 GA31 (female infertility) **[verify]** |
| MeSH | No specific descriptor. Nearest are "Infertility, Female" and "Zona Pellucida" |

**Synonyms:** oocyte maturation defect 1 (OOMD1); oocyte/zygote/embryo maturation arrest 1 (OZEMA1); ZP1-related empty follicle syndrome; ZP1-related zona pellucida defect; zona-free oocytes, familial.

**Nosology caveat.** OMIM 615774 and MONDO:0014342 are **ZP1-specific**. The overlapping ZP2 and ZP3 disorders have their own entries:
- ZP3: OOMD3 / OZEMA3, OMIM 617712, MONDO:0021574
- ZP2: OOMD6 / OZEMA6, OMIM 618353, MONDO:0032696

ZP4-related thin-zona infertility currently has no OMIM phenotype entry **[verify]**. A dismech entry should keep ZP1 as the defining gene and handle ZP2, ZP3 and ZP4 as differentials or a grouping, not lump them in.

**Data provenance.** All knowledge comes from aggregated case reports and small cohorts, mostly Chinese and North African. There are no registry or EHR-scale data.

---

## 2. Etiology

**Primary cause.** Germline pathogenic ZP1 variants. Inheritance is mostly biallelic (homozygous or compound heterozygous), with a minority of heterozygous variants that appear to act in a dominant-negative way.

**Genetic risk factors:**
- **Consanguinity.** The index family was a consanguineous Chinese pedigree (PMID:24670168), and the North African founder families are also consanguineous (PMID:42060237).
- **Founder variant** ZP1 c.1097G>A p.(Arg366Gln) in North African populations (PMID:35460069, PMID:42060237).
  > "The recurrent ZP1 c.1097G > A p.(Arg366Gln) variant contributes to EFS in consanguineous North African families." — PMID:42060237 (abstract quote)
- **Paternally transmitted heterozygous variants** with sex-limited expression, for example ZP1 p.Tyr262Cys (PMID:38966008). Carrier fathers are fertile.

**Environmental risk factors:** none known. The disorder is fully genetic. Maternal age and stimulation protocol affect ART outcome but do not cause the zona defect.

**Protective factors / gene–environment interactions:** none described.

**Modifiers.** Phenotype severity (EFS vs ZP-free MII oocytes) depends on variant type and location. Truncating and splice variants lean toward EFS or degeneration. Some missense variants (for example in the ZP-N1 domain) allow retrieval of ZP-free MII oocytes (PMID:36476320; PMID:42060237). No modifier genes have been identified.

---

## 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Primary female infertility | Clinical sign | Adult (found when trying to conceive) | Obligate (100%) | HP:0008222 Female infertility |
| Absent zona pellucida (ZP-free oocytes) | Laboratory/ART finding | Found at oocyte retrieval | Common. About 20–25% of ZP1 patients yield ZP-free MII oocytes **[count from PMID:36476320 review — check text]** | "Absent zona pellucida" (term exists; listed in MedGen), ID to look up |
| Thin or irregular zona pellucida | ART finding | Retrieval | Occasional | "Abnormal zona pellucida morphology" or similar, ID to look up |
| Empty follicle syndrome (no oocytes despite normal follicle growth and hCG/E2) | ART finding | Retrieval | Most frequent ZP1 presentation (EFS plus degeneration ≈ 75%+ of reported ZP1 cases) | Look up an HPO term for empty follicle syndrome. None may exist; if so, bind to Female infertility and keep the detail in `preferred_term` |
| Degenerated, shrivelled or dark oocytes | ART finding | Retrieval | Frequent | "Oocyte degeneration"-type term, ID to look up |
| Failure of fertilization in conventional IVF | ART finding | ART | Universal when ZP-free oocytes are inseminated by IVF | "Fertilization failure"-type term, ID to look up |
| Normal menstrual cycle, hormones, AMH | Negative findings | — | Typical | — (diagnostic context) |

Key quotes:
> "All the oocytes from ZP1-associated patients appeared shriveled and dark indicating that the abnormal ZP1 protein induced oocyte death and degeneration." — PMID:35460069

> "Sixty-nine mutations of the ZP genes were reported in 87 patients with different clinical phenotypes, including empty follicle syndrome (EFS), ZP-free oocytes (ZFO), ZP-thin oocytes (ZTO), degenerated and immature oocytes. The phenotypes of patients were influenced by the types and location of the mutations." — Zhang et al. 2022 review, PMID:36476320

**Severity, progression and quality of life.** The phenotype is stable and lifelong. There are no systemic or somatic features. The burden is psychosocial: repeated failed stimulation cycles, cost, and infertility distress. No disease-specific QoL studies exist. Generic FertiQoL data on infertility apply.

---

## 4. Genetic / Molecular Information

**Causal gene:** ZP1 (hgnc:13187; 12 exons; 638-aa type I membrane glycoprotein). Its domains run from N- to C-terminus: signal peptide, ZP-N1 (the cross-linking domain), proline-rich linker, trefoil (P-type) domain, bipartite ZP module (ZP-N and ZP-C), consensus furin cleavage site, transmembrane domain and cytoplasmic tail.

**Variant spectrum.**
> "A total of 47 ZP1 mutations have been reported in 19 pieces of literature … Mutations are distributed in all 12 exons of ZP1 gene … including 13 nonsense mutations, 16 missense mutations, seven splicing mutations and 11 frameshift mutations" — PMID:36476320

Notable variants (transcript NM_207341):

| Variant | Domain | Zygosity / inheritance | Phenotype | Source |
|---|---|---|---|---|
| c.1169_1176del, p.Ile390Thrfs*16 (I390fs404X) | ZP module | Homozygous, AR | ZP-free oocytes; the original family | PMID:24670168 |
| c.1097G>A, p.Arg366Gln | ZP-N | Homozygous; North African founder | Degenerated oocytes / EFS | PMID:35460069, PMID:42060237 |
| p.Trp83Arg | ZP-N1 | Compound heterozygous / heterozygous | Blocks ZP1-N1 homodimerization | PMID:31300655 |
| c.326G>A, p.Arg109His | ZP-N1 | Heterozygous | ZP-free oocytes; live birth after ICSI | PMID:32573113 |
| p.Tyr262Cys | Trefoil | Heterozygous, paternally inherited | Abnormal ZP formation | PMID:38966008 |
| Compound heterozygous pairs in sisters | various | AR | EFS | PMID:31292994 |
| 20 ZP1 variants (in a cohort of 35 GEFS/degeneration patients) | various | AR | GEFS / degeneration | PMID:33272616 |

**Classification and frequency.** Most variants are reported as pathogenic or likely pathogenic in the original papers. ClinVar curation is sparse and there is no ClinGen gene–disease validity curation **[verify via `just list-gene-validity`/CGGV cache]**. Variants are rare or absent in gnomAD. The Arg366Gln carrier frequency in North African populations has not been formally estimated.

**Origin and function.** All variants are germline. The functional consequence is loss of function: truncation, absent secretion, or loss of ZP1-N1 dimerization. Some heterozygous missense and frameshift alleles are proposed to act dominant-negatively, by trapping wild-type ZP2, ZP3 and ZP4 inside the cell (PMID:24670168; PMID:33272616; PMID:32573113). Strictly, heterozygous causality rests on a few families and in-vitro data, so treat it as moderate evidence.

**Related ZP genes (differential/allelic group):**
- **ZP3**, heterozygous p.Ala134Thr. Autosomal dominant EFS with paternal transmission (Chen et al., *AJHG* 2017, PMID:28886344 **[verify]**). A homozygous ZP3 EFS variant has also been reported (Front Genet 2023, PMC10613883).
- **ZP2.** Biallelic variants cause a thin ZP that cannot bind sperm (Dai et al. 2019 **[PMID to verify]**). A ZP2 loss-of-function variant has been modelled in humans and rats (PMC10244809).
- **ZP4.** Heterozygous loss-of-function variants were found in 3 of 26 women with thin, irregular ZP (about 11%); ICSI pregnancies were achieved (summarized in PMID:36476320).
- **Combined cohorts:**
  > "We identified zona pellucida (ZP) gene variants in 18 individuals, which included 20 variants in the ZP1 gene, two variants in the ZP2 gene, and one previously reported recurrent variant in the ZP3 gene. The women carrying ZP variants constituted 51.43% of the GEFS cohort." — PMID:33272616

**Epigenetics and chromosomal abnormalities:** none reported. Karyotype is normal (46,XX).

---

## 5. Environmental Information

Not applicable. No toxin, lifestyle or infectious contribution is known. Note that acquired, iatrogenic "false" EFS (for example from a faulty hCG trigger) is a non-genetic phenocopy and has to be excluded clinically (see §10).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Germline ZP1 variant**: truncating, splice, or missense in ZP-N1, trefoil or ZP module.
2. **This leads to loss of secreted ZP1.** Mutant ZP1 is misfolded or truncated and is retained in the oocyte cytoplasm / ER instead of being secreted (shown in HeLa, CHO and 293T cells, and in rat oocytes).
   > "secretion of hZP1Mut is completely abolished" — PMID:31300655 (in vitro)
3. **Branch A (mainly truncating and dominant-negative alleles).** Retained mutant ZP1 binds and co-sequesters wild-type ZP3 and ZP4, and possibly ZP2, inside the cell, so they cannot be exported.
   > "the aberrant ZP1 results in the sequestration of ZP3 in the cytoplasm, thereby preventing the formation of the zona pellucida around the oocyte." — PMID:24670168 (in vitro)

   **Branch B (ZP-N1 missense alleles).** ZP1 is secreted but cannot form the disulfide-bonded ZP1-N1 homodimer, so ZP2/ZP3/ZP4 filaments are not cross-linked. Human ZP4 cannot substitute.
   > "W83R … significantly reduces its ability to form disulphide-bonded homodimers … the mutation leads to lack of the ZP by hindering human ZP filament cross-linking." — PMID:31300655 (in vitro, structural)
4. **Both branches result in failed ZP matrix assembly or maintenance.** The ZP is absent, very thin, or fragile around growing oocytes. Human ovarian histology shows a thin, ZP1-lacking ZP in preantral follicles (PMID:31734689; one case).
5. **Branch point at the antral transition.**
   - **5a.** If the matrix is lost or unstable in antral follicles, cumulus–oocyte complex (COC) organization and transzonal oocyte–granulosa communication fail. **[Partly inferred]** Human histology supports the COC defect (PMID:31734689). The mechanism through communication loss is hypothesized (PMID:36476320). In macaques, ZP1 loss causes oxidative stress, SOD2 downregulation, mitochondrial swelling and autophagy (PMID:40923306; model organism).
   - **5a → 6a.** These changes lead to oocyte degeneration in the follicle, or to fragile oocytes that rupture during aspiration. Clinically this is **GEFS or degenerated oocytes**.
   - **5b.** If oocytes survive to MII, they lack the ZP sperm-binding matrix. ZP2-N terminus binding, the ZP-induced acrosome reaction, and the zona block to polyspermy are all missing.
   - **5b → 6b.** This leads to **fertilization failure in conventional IVF**. ICSI bypasses it (§12).
6. **Clinical endpoint:** primary female infertility (obligate).

**Upstream vs downstream.** Steps 1–3 are molecular and oocyte-intrinsic. Step 4 is extracellular matrix. Steps 5–6 are follicular and gamete-level.

**Suggested terms:**
- **GO BP** (validated in the draft YAML): extracellular matrix assembly GO:0085029; protein secretion GO:0009306; protein retention in ER lumen GO:0006621; ovarian follicle development GO:0001541; oocyte development GO:0048599; female gamete generation GO:0007292. Also worth looking up: "binding of sperm to zona pellucida", "egg coat formation", "acrosome reaction".
- **GO CC:** extracellular matrix GO:0031012; endoplasmic reticulum GO:0005783. Look up "egg coat" for the zona pellucida itself.
- **GO MF:** extracellular matrix structural constituent GO:0005201.
- **CL:** oocyte CL:0000023; primary oocyte CL:0000654; granulosa cell CL:0000501. Look up cumulus cell.
- **Biochemical:** no metabolic or immune involvement. This is a structural ECM glycoprotein defect.
- **Omics:** macaque single-oocyte transcriptomics showed disrupted granulosa–oocyte signalling (PMID:40923306). There are no human omics datasets.

---

## 7. Anatomical Structures Affected

- **Organ:** ovary, UBERON:0000992 (primary; the only organ affected). No secondary organ involvement. Body system: female reproductive.
- **Tissue:** ovarian follicle (look up the UBERON ID), cumulus oophorus, and the zona pellucida ECM.
- **Cells:** oocyte, primary oocyte, granulosa/cumulus cells.
- **Subcellular:** oocyte ER/secretory pathway (retention) and the extracellular egg coat.
- **Laterality:** bilateral (all oocytes affected).

---

## 8. Temporal Development

- **Onset:** the molecular defect is present from oocyte growth, which is fetal/prepubertal for primordial follicles and pubertal onward for growth. It is **clinically silent until adulthood**, when infertility is investigated or ART is attempted.
- **Course:** stable and lifelong. No stages and no remission.
- **Critical window:** the preantral→antral follicle transition, when the ZP must be assembled and maintained (PMID:31734689).

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007) is the main mode. A minority is autosomal dominant (HP:0000006) with **sex-limited expression**: male carriers, homozygous or heterozygous, are fertile.
  > "The ZP1 variants were inherited in an autosomal recessive pattern; the ZP2 and ZP3 variants were inherited in an autosomal dominant pattern." — PMID:33272616
- **Penetrance:** complete in homozygous females, as far as reported. Penetrance of heterozygous alleles is uncertain.
- **Expressivity:** variable (EFS vs degeneration vs ZP-free MII), correlated with genotype.
- **Founder effect:** p.Arg366Gln in North Africa (Algeria/Tunisia/Morocco **[country breakdown to verify]**).
- **Consanguinity:** a major contributor in reported families.
- **Prevalence:** unknown in the general population; ultra-rare (ORPHA lists no estimate **[verify]**). In enriched cohorts:
  - ZP gene variants in 18/35 (51.4%) of Chinese GEFS/degeneration patients (PMID:33272616);
  - homozygous ZP1 p.Arg366Gln in 5/27 (18.5%) of North African oocyte-maturation-defect patients (PMID:35460069);
  - a 2025 *BJOG* retrospective study of 12 Chinese women with EFS or degenerated oocytes found rare ZP variants **[PMID to verify]**.
  - Underlying context: GEFS itself is reported in roughly 0.016–0.07% of IVF cycles **[verify]**.
- **Sex ratio:** female-only phenotype.

---

## 10. Diagnostics

- **Clinical and laboratory work-up:**
  - Normal FSH, LH, E2 and AMH; normal antral follicle count; normal follicular growth on ultrasound during stimulation.
  - At retrieval: no oocytes, degenerated oocytes, or ZP-free/thin-ZP oocytes, seen under light microscopy (polarized-light ZP imaging can quantify thickness).
  - **Exclude "false EFS"** by confirming adequate serum hCG or LH on trigger day.
- **Histology** (research only): ZP1 immunostaining of ovarian tissue shows a thin ZP lacking ZP1 (PMID:31734689).
- **Genetic testing (definitive).** Use whole-exome sequencing, or a female-infertility / oocyte-maturation-defect panel covering ZP1, ZP2, ZP3, ZP4, TUBB8, PATL2, WEE2, PANX1, BTG4, TLE6, NLRP family genes and others.
  > "In this cohort of North African OMD patients, whole exome sequencing permitted to diagnose 44% of the patients studied and to identify a new frequent ZP1 variant." — PMID:35460069

  Targeted testing for p.Arg366Gln is reasonable in North African patients. Microarray, karyotype, FISH, mtDNA and repeat testing are not relevant beyond confirming 46,XX.
- **Diagnostic ICSI.** A small test ICSI can reveal the embryo-development potential of ZP-free oocytes (PMID:32847637).
- **NCIT:** Genetic Testing NCIT:C15709. LOINC has no disease-specific assay.
- **Differential diagnosis:**
  - OOMD3 (ZP3; AD)
  - OOMD6 (ZP2; thin ZP with sperm-binding failure)
  - ZP4 thin zona
  - OOMD2 (TUBB8; MI arrest with an *intact* ZP; PMID:26789871)
  - PATL2 (GV arrest; PMID:35460069 contrasts it with ZP1)
  - WEE2 (fertilization failure, intact ZP)
  - iatrogenic false EFS
  - diminished ovarian reserve / POI (abnormal AMH and FSH)
- **Screening:** none at population level. Cascade testing of sisters is reasonable. Carrier screening is possible in founder populations but not established.

---

## 11. Outcome / Prognosis

- Survival, life expectancy and mortality are **not affected**. There is no systemic morbidity.
- The outcome is infertility with autologous oocytes. Prognosis depends on genotype and phenotype:
  > "Three patients with ZP1 mutations, two with ZP2 mutations, and three with ZP4 mutations had successful pregnancies through Intracytoplasmic sperm injection (ICSI) from ZFO or ZTO." — PMID:36476320

  The same review built a pregnancy-prediction model (AUC 0.898) from mutation type and location **[verify the figure in the full text]**.
- **Poor-prognosis predictors:** biallelic truncating ZP1 variants, EFS, and fully degenerated oocytes. Patients in this group usually need oocyte donation.
- **Complications:** repeated futile stimulation cycles, OHSS risk with re-stimulation, and psychological burden.

---

## 12. Treatment

There is no disease-modifying therapy. Management is reproductive.

| Intervention | Rationale / outcome | NCIT |
|---|---|---|
| **ICSI** of ZP-free/thin-ZP MII oocytes | Bypasses ZP-dependent sperm binding. Live births reported for ZP1 (PMID:32573113, PMID:32847637), ZP2 and ZP4. Requires careful handling and individual microdrop culture of zona-free embryos. | NCIT:C185482 Intracytoplasmic Sperm Injection |
| Low-pressure follicular aspiration / modified retrieval | Reduces rupture of fragile ZP-free oocytes (described in ZP4 and ZP1 reports **[verify source]**) | Surgical/retrieval procedure; ID to look up |
| Diagnostic (test) ICSI | Assesses embryo potential before a full cycle (PMID:32847637) | NCIT:C185482 |
| **Oocyte donation** | The only option for EFS or complete degeneration | Look up an NCIT oocyte-donation / ART term |
| Genetic counseling | Explains AR and sex-limited AD inheritance, sister testing, and avoiding futile cycles (PMID:42060237) | NCIT:C15240 |

- **Embryo transfer:** zona-free embryos are fragile, so blastocyst-stage transfer is preferred.
- **Pharmacogenomics, gene/cell/RNA therapies:** none. No clinical trials were found on ClinicalTrials.gov for ZP1 **[search not exhaustive]**.
- **Experimental idea (not in human use):** artificial zona or ZP-substitute matrices.

---

## 13. Prevention

- **Primary:** none. The disease is genetic.
- **Secondary:** genotype-guided ART planning. Women with prior EFS, degenerated oocytes or ZP-free oocytes should be offered ZP-gene testing *before* repeat cycles. They should go straight to ICSI rather than IVF, or to donation when the genotype predicts EFS (PMID:32573113; PMID:36476320; 2025 *BJOG* study).
- **Counseling:** cascade testing of female siblings, especially in consanguineous or North African families. PGT for future generations is theoretically possible, but no one has reported it and there is little rationale because the phenotype is only infertility.
- **Vaccination / public health:** not applicable.

---

## 14. Other Species / Natural Disease

- **OMIA:** "Infertility, ZP1-related" in *Macaca fascicularis* (NCBITaxon:9541), OMIA 003005-9541. This entry records the engineered model (PMID:40923306), not natural disease.
- No naturally occurring ZP1 disease is documented in companion animals or livestock **[OMIA search for other species advised]**.
- **Comparative biology:** ZP gene composition differs across species, and this explains the phenotypes seen in models:
  - humans, macaques and rats have four ZP proteins (ZP1–4);
  - in mice, *Zp4* is a pseudogene (three proteins);
  - birds and fish have different ZP repertoires.

  The ZP1-N1 cross-linking cysteine is conserved from chicken to human (PMID:31300655).
- **Orthologs:** mouse Zp1 (MGI), rat Zp1 (RGD), macaque ZP1. Look up the NCBI Gene IDs.
- **Transmission/zoonosis:** not applicable.

---

## 15. Model Organisms

| Model | Genotype | Recapitulation | Ref |
|---|---|---|---|
| **Rat** (*Rattus norvegicus*, Sprague-Dawley) | Homozygous Zp1 knock-in of human I390fs404X | High. Complete ZP absence, cytoplasmic ZP1, 1–2 vs ~21 eggs ovulated, IVF failure, sterility. | PMID:33624742 |
| **Cynomolgus macaque** | CRISPR ZP1 loss-of-function (#ZP1-2) | High (primate, 4-ZP). ZP-deficient oocytes, low IVM and blastocyst rates, disrupted folliculogenesis, mitochondrial swelling, SOD2 down. Single animal. | PMID:40923306 |
| **Mouse** | Zp1-null (Zp1 tm/tm) | Partial. Loose, porous ZP2/ZP3 zona; ectopic granulosa cells; *subfertile*, with smaller litters from early embryo loss. | PMID:10433913 |
| Mouse Zp2-null / Zp3-null | Knockout | No ZP, sterile; models the ZP2/ZP3 differentials | Rankin et al. 1996/2001 **[PMIDs to look up]** |
| Rat Zp2 model | Loss-of-function variant | ZP2 differential | PMC10244809 |
| **Cell lines** (HeLa, CHO, HEK293T) | Co-transfected WT/mutant ZP1 ± ZP2/3/4 | Moderate. Retention, co-sequestration, dimerization and secretion assays. | PMID:24670168, 31300655, 33272616, 32573113 |

- **Human–model mismatch.** The mouse knockout is milder because mice lack ZP4, and a null allele (unlike a retained truncated protein) does not trap partner ZPs. The rat and macaque are the preferred models. This fits a `HUMAN_MODEL_MISMATCH` discussion, which the draft YAML already carries.
- **Resources:** MGI, RGD, IMPC (check for a Zp1 line), OMIA.

---

## Key gaps and cautions for curation

1. **Population prevalence:** none exists. Record it as unknown and use only cohort-enriched frequencies.
2. **Heterozygous ZP1 causality** rests on very few families. Mark the AD claim with moderate confidence.
3. **The step from ZP loss to degeneration** (oocyte–cumulus communication, oxidative stress) is supported only by human hypothesis and one macaque model. Edges for it should carry `directness: INDIRECT` or MODEL_ORGANISM evidence.
4. **HPO IDs** for "Absent zona pellucida", empty follicle syndrome and oocyte degeneration need lookup. Do not write them from memory.
5. **[unverified] PMIDs** for Chen 2017 *AJHG* (ZP3), Dai 2019 (ZP2), the 2025 *BJOG* cohort, and Rankin's Zp2/Zp3 knockouts need confirmation with `just fetch-reference`.
6. **Draft YAML check:** the existing YAML uses the deprecated `percentage` prevalence field and `updated_date`. Migrate both to structured prevalence (`measure_type: UNKNOWN` / cohort fraction) before PR.

---

### Sources
- Huang HL et al. *NEJM* 2014, PMID:24670168
- Sun L et al. 2021, PMID:33272616
- Zhang Z et al. 2022 review, PMID:36476320 — [PMC9730648](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9730648/)
- Loeuillet C et al. 2022, PMID:35460069; North African ZP1 follow-up, PMID:42060237
- Nishio S et al. 2019 (ZP1 cross-linking), PMID:31300655
- Sun Y et al. 2019 (compound heterozygous sisters), PMID:31292994
- Cao Q et al. 2020 (ZP1/ZP3 heterozygous), PMID:32573113
- Dai C et al. 2019 / Zhou Z et al. 2019, PMID:30810869
- Case report, ovarian histology, PMID:31734689
- Diagnostic ICSI case report, PMID:32847637
- ZP1-Y262C, PMID:38966008 — [Frontiers Genet 2024](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1407202/epub)
- Rat Zp1 knock-in, PMID:33624742; macaque ZP1, PMID:40923306 — [Zool Res PDF](https://www.zoores.ac.cn/en/article/pdf/preview/10.24272/j.issn.2095-8137.2024.415.pdf), [OMIA 003005-9541](https://omia.org/OMIA003005/9541/)
- Rankin T et al. 1999 (Zp1-null mouse), PMID:10433913
- Feng R et al. 2016 (TUBB8), PMID:26789871
- [NCBI MedGen C4014291](https://www.ncbi.nlm.nih.gov/medgen/C4014291)
- [NORD entry](https://rarediseases.org/?p=269989)
- [ZP3 homozygous EFS case, Front Genet 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10613883/)
- [ZP2 loss of function in humans and rats](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10244809/)
- [BJOG 2025 ZP variant study (EBSCO record)](https://www.ebsco.com/articles/consumer-health/69a12748-795d-5bf3-b0ff-8e762861e656/association-of-zona-pellucida-gene-variants-with-female-infertility-a-retrospective-genetic-analysis/)
- [AlphaGalileo summary](https://www.alphagalileo.org/en-gb/Item-Display/ItemId/277784)
- [News-Medical, 2026-09-08](https://www.news-medical.net/news/20260908/Study-identifies-14-egg-layer-gene-variants-linked-to-female-infertility.aspx)
- Other search results consulted: [PMC7822995](https://pmc.ncbi.nlm.nih.gov/articles/PMC7822995), [PMC9107549](https://pmc.ncbi.nlm.nih.gov/articles/PMC9107549), [PMC7642144](https://pmc.ncbi.nlm.nih.gov/articles/PMC7642144), [PMC7412702](https://pmc.ncbi.nlm.nih.gov/articles/PMC7412702), [PMC7336750](https://pmc.ncbi.nlm.nih.gov/articles/PMC7336750), [J Assist Reprod Genet 2022](https://www.doi.org/10.1007/s10815-022-02466-4), [J Ovarian Res 2025](https://biomedcentral-ovarianresearch.publicaciones.saludcastillayleon.es/articles/10.1186/s13048-025-01674-7), [PMC7492330](https://pmc.ncbi.nlm.nih.gov/articles/PMC7492330), [eLife ZP](https://elifesciences.org/articles/48904.pdf), [ZP2 IVF failure](https://www.medchemexpress.com/publications/29895852.html), [GTR ZP1](https://https.ncbi.nlm.nih.gov/gtr/genes/22917)
