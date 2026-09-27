---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-08-24T04:45:20.459990'
end_time: '2026-08-24T04:51:10.252259'
duration_seconds: 349.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Asherman Syndrome
  mondo_id: ''
  category: Acquired
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
  - claude-opus-4-8[1m]
  web_search_requests: 6
  num_turns: 13
  total_cost_usd: 1.74471475
  session_id: 2888122b-be7b-4fb5-a001-0f26b17e9c9e
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 19
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Asherman Syndrome
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Asherman Syndrome** covering all of the
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

I'll research Asherman Syndrome comprehensively. Let me first load the web tools, then gather current literature.

Let me fetch key primary sources for detailed, citable content.

I have enough for a comprehensive report. Let me grab one more source on molecular mechanisms and animal models.

I have gathered sufficient authoritative information. Here is the comprehensive research report.

---

# Comprehensive Research Report: Asherman Syndrome

**Compiled:** August 2026 | **Category:** Acquired uterine disorder | **MONDO:** MONDO:0015299

> **Scope note:** Asherman syndrome (AS) is an *acquired* condition, not a Mendelian genetic disorder. Accordingly, sections oriented toward causal genes, inheritance, penetrance, founder effects, and germline variant classification are largely **Not Applicable**, and this is flagged explicitly where it arises. The mechanistically rich content concentrates in Etiology, Pathophysiology, Phenotypes, Diagnostics, Treatment, and Prevention.

---

## 1. Disease Information

**Overview.** Asherman syndrome is a rare, acquired gynecological disorder characterized by the formation of **intrauterine adhesions (IUA)** / synechiae — fibrous scar tissue that partially or completely obliterates the uterine cavity and/or cervical canal. It arises from damage to the **basal (regenerative) layer of the endometrium**, most often after intrauterine instrumentation, leading to non-regenerative healing in which functional endometrium is replaced by fibrous connective tissue and opposing uterine walls adhere. The clinical triad is **menstrual abnormality (hypomenorrhea/amenorrhea), infertility/recurrent pregnancy loss, and cyclic pelvic pain**. The eponym honors Joseph Asherman, who characterized the syndrome in 1948–1950.

A useful nomenclature distinction (increasingly emphasized in the literature): **"intrauterine adhesions"** is the anatomical/hysteroscopic finding, whereas **"Asherman syndrome"** is reserved for IUA *accompanied by symptoms* (menstrual disturbance, infertility, pain). In one retrospective cohort, of patients with adhesions, 76.1% were classified as IUA and 23.9% met criteria for symptomatic Asherman syndrome ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).

**Key identifiers:**
- **MONDO:** MONDO:0015299
- **Orphanet:** ORPHA:137686
- **ICD-10:** N85.6 (Intrauterine synechiae)
- **ICD-11:** GA20 (Non-inflammatory disorders of the uterus) / relevant synechiae code
- **MeSH:** "Gynatresia" / "Asherman Syndrome" is indexed under MeSH term **D054882** (Gynatresia); IUA also indexed under uterine diseases
- **OMIM:** Not applicable (acquired, non-Mendelian)
- **NORD:** Listed rare disease profile ([NORD](https://rarediseases.org/rare-diseases/ashermans-syndrome/))

**Synonyms / alternative names:** Intrauterine adhesions; intrauterine synechiae; uterine synechiae; endometrial sclerosis; sclerotic endometrium; traumatic uterine atrophy; uterine/cervical atresia (older usage); Asherman's syndrome. ([NORD](https://rarediseases.org/rare-diseases/ashermans-syndrome/), [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=137686))

**Data derivation:** Disease-level knowledge is aggregated from case series, retrospective cohorts, hysteroscopy registries, and increasingly from **single-cell molecular atlases** of patient endometrium — not from a single population EHR resource. It is under-captured in administrative datasets because many cases are diagnosed only at hysteroscopy during infertility work-up.

---

## 2. Etiology

**Primary causal mechanism — endometrial basalis trauma.** The dominant cause (>90% of cases) is **iatrogenic mechanical injury to the endometrial basal layer**, typically in a hormonally hypoestrogenic, recently pregnant uterus where the endometrium is thin and vulnerable ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).

**Disease causal factors / procedures:**
- **Dilation and curettage (D&C) for miscarriage or retained products of conception (RPOC)** — the single most common cause; up to ~40% of women undergoing D&C for RPOC develop adhesions ([management review, Springer](https://link.springer.com/article/10.1186/1477-7827-11-118)).
- **Postpartum curettage** — IUA in ~22% ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Termination of pregnancy (TOP)** — first-trimester ~21.2%; second-trimester 16.2–21% ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Myomectomy** — ~9.3% incidence, especially with cavity entry ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Cesarean section**, B-Lynch compression suturing, uterine artery embolization, and other conservative postpartum-hemorrhage interventions.
- **Infectious / inflammatory causes:** genital tuberculosis (a leading cause in endemic regions, often producing severe disease), schistosomiasis, chronic endometritis, and pelvic inflammatory disease.
- **Congenital predisposition:** Müllerian anomalies — one series found 31.6% of septate uteri developed IUAs ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).

**Risk factors (environmental / clinical):**
- **Timing of curettage** is the most consistent modifiable risk factor: all women who developed IUA in one post-abortion cohort had undergone curettage **8–28 days after delivery/miscarriage, with 75% in the 14–24-day window** ([Identifying risk factors and incidence, PMID:33462894](https://pubmed.ncbi.nlm.nih.gov/33462894/)). Elevated risk persists up to ~4 weeks post-delivery/miscarriage.
- **Repeated uterine instrumentation / repeat abortions** — the principal risk factor; risk rises with number of procedures.
- **Negative uterine (suction) pressure** — extremely strong association (OR 125.61, 95% CI 67.35–183.87) ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Chronic endometritis** — present in 64.3% of severe cases ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Age >35 years** (confounded by cumulative prior procedures); **low estrogen state**.

**Genetic risk factors:** None established as causal. AS is acquired. There may be individual variation in fibrotic/wound-healing propensity (e.g., TGF-β pathway polymorphisms), but no validated susceptibility locus, GWAS signal, or ClinVar entry exists for AS. **Not Applicable / Not established.**

**Protective factors:** The strongest protective strategy is **avoiding sharp curettage** in favor of medical management (misoprostol) or **ultrasound-guided gentle suction/manual vacuum aspiration**, and avoiding the high-risk 2–4 week postpartum window ([Fertility & Sterility, uterine evacuation approach](https://www.fertstert.org/article/S0015-0282(21)00537-9/fulltext)). No genetic protective variants are known.

**Gene–environment interactions:** Not characterized for AS. Host fibrotic response to endometrial injury is the plausible interaction axis but is unproven.

---

## 3. Phenotypes

| Phenotype | Type | Suggested HPO | Frequency / notes |
|---|---|---|---|
| Amenorrhea / hypomenorrhea | Menstrual sign | HP:0000141 (Amenorrhea); HP:0011225 (Hypomenorrhea) | Amenorrhea in 34.4% of AS vs 2.0% of IUA (OR 26.19); hallmark of severe disease ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)) |
| Female infertility | Reproductive sign | HP:0008222 (Female infertility) | Very frequent; a leading cause of refractory uterine-factor infertility |
| Recurrent pregnancy loss | Reproductive sign | HP:0100615 / HP:0500110 (Recurrent spontaneous abortion) | 5–39% of women with recurrent miscarriage have IUA ([Springer review](https://link.springer.com/article/10.1186/1477-7827-11-118)) |
| Cyclic pelvic pain / dysmenorrhea | Symptom | HP:0002360 (dysmenorrhea-related); HP:0012531 (Pain) | Dysmenorrhea 43.8% in AS vs 22.5% IUA; from trapped menstrual blood (hematometra) behind cervical obstruction |
| Hematometra | Physical manifestation | HP:0030144 (Hematometra) | Occurs when outflow is obstructed by cervical/lower-segment adhesions |
| Abnormal uterine cavity / synechiae | Imaging finding | HP:0031331 (Abnormal uterine morphology) | Defining hysteroscopic finding |
| Placenta accreta spectrum (obstetric complication) | Physical manifestation | HP:0011409 (Abnormal placenta morphology) | Increased in subsequent pregnancies due to deficient decidualization |

**Characteristics:**
- **Age of onset:** Reproductive-age adult; onset is temporally linked to the inciting procedure (mean age ~33 years in cohorts; onset days-to-weeks after instrumentation) ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Severity:** Variable — graded mild/moderate/severe. AS cohorts skew severe (58.1% AFS stage III) vs IUA cohorts skewing mild (54.9% AFS stage I) ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Progression:** Chronic and, without treatment, **stable-to-progressive**; adhesions can re-form aggressively after lysis (severe cases up to 62.5% recurrence, see §11).
- **QoL impact:** Substantial — infertility, pregnancy loss, chronic cyclic pain, and psychological distress; measured with general instruments (SF-36/EQ-5D) rather than AS-specific tools.

---

## 4. Genetic / Molecular Information

**Causal genes:** **None.** Asherman syndrome is an acquired fibrotic disorder with no Mendelian gene, no pathogenic germline variant, and no OMIM entry. ClinVar/HGMD/COSMIC are **Not Applicable**.

**Molecularly dysregulated genes (acquired expression changes, not mutations)** — from single-cell and expression studies:
- **TGFB1** (TGF-β1) — up-regulated; central pro-fibrotic driver via **SMAD2/3** signaling, promoting myofibroblast differentiation ([single-cell review searches](https://www.sciencedirect.com/science/article/pii/S2352320425000732)).
- **ACTA2** (α-SMA) and **COL1A1** (collagen I) — up-regulated myofibroblast/ECM markers.
- **THBS1** (thrombospondin-1) — identified as a key pro-fibrotic factor modulating **PI3K/AKT**, and a stem-cell-reversible target ([Frontiers, THBS1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916671/)).
- **SLPI** (secretory leukocyte protease inhibitor) — marks a stressed epithelial subpopulation characteristic of AS during the implantation window ([Nat Commun single-cell atlas, PMID:37735465](https://pmc.ncbi.nlm.nih.gov/articles/PMC10514053/)).
- **WNT7A / FZD6 / LRP6** — loss of ligand–receptor communication (impaired epithelial differentiation).
- **JAG1 / NOTCH2** — decreased communication affecting glandular differentiation.
- **IGFBP3/5/6** — up-regulated anti-angiogenic factors.
- Stress-response genes **HSPA1A**, **SOCS3** co-expressed in the stressed epithelium.

**Suggested HGNC/gene annotations:** TGFB1 (hgnc:11766), ACTA2 (hgnc:130), COL1A1 (hgnc:2197), THBS1 (hgnc:11785), SLPI (hgnc:11092), WNT7A (hgnc:12786), NOTCH2 (hgnc:7882).

**Epigenetics:** Emerging evidence implicates altered DNA methylation and non-coding RNAs (various miRNAs regulating TGF-β/Smad and EMT) in endometrial fibrosis, but this remains preliminary and not part of routine characterization.

**Chromosomal abnormalities:** Not applicable.

---

## 5. Environmental Information

- **Environmental / occupational toxins:** No established chemical or radiation etiology (external pelvic radiation could theoretically damage endometrium, but is not a recognized AS cause).
- **Lifestyle factors:** No direct causal lifestyle factors; the operative risk is procedural, not behavioral.
- **Infectious agents (can trigger/cause):**
  - *Mycobacterium tuberculosis* (NCBITaxon:1773) — **genital tuberculosis** is a major cause of severe AS in endemic regions.
  - *Schistosoma* spp. — genital schistosomiasis (regional).
  - Polymicrobial **chronic endometritis** and PID organisms contribute to the inflammatory/fibrotic milieu.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Trauma to endometrial basalis** (curettage, especially on gravid/postpartum uterus) → loss of the regenerative stem/progenitor niche.
2. **Local ischemia and inflammation** → hypoxic, pro-inflammatory microenvironment (increased macrophages, B cells, dendritic cells on single-cell profiling).
3. **TGF-β1 → SMAD2/3 activation** → **fibroblast-to-myofibroblast transdifferentiation** (↑α-SMA), with contributions from CXCR4 signaling and THBS1/PI3K-AKT ([TGF-β/Smad2/3 in IUA](https://www.sciencedirect.com/science/article/pii/S2352320425000732)).
4. **Excessive ECM deposition** — collagen I, laminin, fibronectin (FN1) from stromal fibroblasts; single-cell data show **"a shift from epithelial–stromal interactions to ECM-based self-stromal signaling"** ([PMID:37735465](https://pmc.ncbi.nlm.nih.gov/articles/PMC10514053/)).
5. **Failed epithelial regeneration** — dramatic epithelial loss (**8.3% vs 51.65%** of cells) and near-absent ciliated epithelium (**0.19% vs 5.3%**), with disrupted **WNT** (loss of WNT7A–FZD6/LRP6) and **NOTCH** (↓JAG1–NOTCH2) signaling impairing differentiation ([PMID:37735465](https://pmc.ncbi.nlm.nih.gov/articles/PMC10514053/)).
6. **Anti-angiogenic environment** — up-regulated IGFBP3/5/6 → poor revascularization → perpetuates ischemia (a self-reinforcing fibrotic loop).
7. **Adhesion formation** — opposing fibrotic walls fuse; cavity/cervical obliteration.
8. **Clinical manifestation** — reduced functional endometrium → hypomenorrhea/amenorrhea, impaired implantation/decidualization → infertility, RPL, placenta accreta spectrum.

**Cellular processes / GO terms:**
- Wound healing / fibrosis: GO:0061041 (regulation of wound healing), GO:0030198 (ECM organization)
- TGF-β receptor signaling: GO:0007179
- Myofibroblast differentiation / fibroblast activation
- Inflammatory response: GO:0006954
- Epithelial cell differentiation: GO:0030855 (disrupted)
- Angiogenesis: GO:0001525 (suppressed)
- Wnt signaling: GO:0016055; Notch signaling: GO:0007219

**Cell types involved (CL terms):**
- Endometrial stromal fibroblast → **myofibroblast** (CL:0000186) — the fibrogenic effector
- Endometrial (luminal/glandular) **epithelial cell** (CL:0002586 / CL:0000066) — lost/stressed
- **Ciliated epithelial cell** (CL:0000064) — markedly depleted
- **Macrophage** (CL:0000235), **B cell** (CL:0000236), **dendritic cell** (CL:0000451) — expanded
- Vascular endothelial cell (CL:0000115) — anti-angiogenic shift

**Molecular profiling available:** Single-cell RNA-seq atlas of AS endometrium ([PMID:37735465](https://pmc.ncbi.nlm.nih.gov/articles/PMC10514053/); medRxiv preprint 2022) is the flagship dataset, defining the SLPI+ stressed epithelium and the pro-fibrotic/anti-angiogenic niche. This is the strongest candidate dataset for KB `datasets:` linkage (GEO deposition associated with the Nature Communications paper).

---

## 7. Anatomical Structures Affected

- **Primary organ:** **Uterus** (UBERON:0000995), specifically the **endometrium** (UBERON:0001295) and its **basal layer**.
- **Tissue level:** endometrial epithelium (glandular + luminal), endometrial stroma, uterine cavity; fibrous scar replacing functional mucosa.
- **Secondary sites:** **cervix / cervical canal / internal os** (UBERON:0000002) — obstruction here causes hematometra; **fallopian tube ostia** may be occluded, contributing to infertility.
- **Subcellular/GO cellular component:** ECM (extracellular region, GO:0005576); collagen-containing ECM (GO:0062023).
- **Body system:** Female reproductive system (UBERON:0000474).
- **Lateralization:** Adhesions are distributed within the cavity (may be marginal, central, or diffuse); disease is of a single midline organ — not lateralized per se.

---

## 8. Temporal Development

- **Onset:** Adult, reproductive age; **acquired, temporally linked to instrumentation** (days–weeks after the inciting procedure). Onset pattern is subacute (fibrosis develops over the healing window).
- **Progression stages:** Graded mild → moderate → severe by cavity involvement and adhesion density (see classification, §10). Severe disease features dense, cavity-obliterating adhesions and amenorrhea.
- **Course:** Chronic; without intervention, stable-to-progressive. **Post-treatment recurrence is the defining temporal problem** — reformation of adhesions after lysis, up to 62.5% in severe disease.
- **Critical intervention windows:** (a) **Prevention window** — the 2–4 week postpartum/post-miscarriage period when curettage is most dangerous; (b) **Post-adhesiolysis window** — early second-look hysteroscopy and barrier/estrogen measures to prevent reformation.

---

## 9. Inheritance and Population

- **Inheritance:** **Not applicable** — acquired, non-heritable. No penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier-frequency considerations.
- **Epidemiology:** True population prevalence is uncertain (under-diagnosed). Procedure-conditioned incidence:
  - **16–45.5%** of women develop IUA after intrauterine interventions (miscarriage management, TOP, D&C) ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
  - **Up to ~21.5%** after D&C generally; **up to ~40%** after D&C for RPOC.
  - **~1.5%** of women undergoing HSG show IUA; **5–39%** of women with recurrent miscarriage ([Springer review](https://link.springer.com/article/10.1186/1477-7827-11-118)).
  - Orphanet lists it as a rare disease.
- **Population demographics:** Affects women of reproductive age worldwide; **higher burden in regions with high rates of unsafe abortion, postpartum curettage, and genital tuberculosis** (parts of South Asia, Africa). **Sex:** exclusively female (uterine organ). Mean age in cohorts ~33 years.

---

## 10. Diagnostics

**Gold standard:** **Hysteroscopy** — direct visualization of the cavity, permitting simultaneous diagnosis and treatment ([Dovepress current perspectives, PMID:30936754](https://pubmed.ncbi.nlm.nih.gov/30936754/); [PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).

**Imaging / functional tests:**
- **3D transvaginal ultrasound (TVUS):** sensitivity 98.8%, specificity 90.8%, accuracy 91.4% ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)); useful first-line/screening; can assess endometrial thickness.
- **Saline infusion sonohysterography (SIS):** less invasive cavity assessment.
- **Hysterosalpingography (HSG):** shows filling defects but limited accuracy (~50%); also assesses tubal patency ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **MRI:** reserved for **totally obliterated cavities** where hysteroscopy cannot access the fundus.
- **Laboratory / endocrine:** used to *exclude* other causes of amenorrhea (FSH, estradiol, prolactin, TSH, hCG) — endocrine axis is typically normal in AS, distinguishing it from ovarian/hypothalamic causes.

**Classification systems:** No universally validated system; ~7 exist. Most used:
- **American Fertility Society (AFS, 1988)** scoring (extent of cavity, adhesion type, menstrual pattern) → stages I (mild), II (moderate), III (severe).
- **ESGE (European Society for Gynaecological Endoscopy)** classification.
- **Nasr et al. (2000)** clinicohysteroscopic score.

**Differential diagnosis:** Hypothalamic amenorrhea, premature ovarian insufficiency, PCOS, pregnancy, endometrial atrophy, cervical stenosis, Müllerian agenesis — distinguished by normal endocrine profile plus cavity findings on imaging/hysteroscopy.

**Genetic testing:** Not applicable.

---

## 11. Outcome / Prognosis

- **Reproductive outcomes after hysteroscopic adhesiolysis:** In a treated cohort, **cumulative pregnancy rate 81.9%** and **cumulative live birth rate 51.2%**, with outcomes stratifying by severity ([low-resource setting review, PMC10848492](https://pmc.ncbi.nlm.nih.gov/articles/PMC10848492/)). Milder disease has far better prognosis: AFS stage I ~>75% fertility prognosis; stage III often 25–50% ([PMID:40310333](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)).
- **Recurrence:** The central prognostic obstacle. Adhesion reformation correlates with baseline severity; **severe IUA recurrence up to 62.5%** ([outcomes searches](https://pmc.ncbi.nlm.nih.gov/articles/PMC10848492/)).
- **Obstetric complications in achieved pregnancies:** increased **placenta accreta spectrum**, placenta previa, preterm birth, IUGR, and miscarriage, owing to deficient decidualization over scarred segments.
- **Mortality:** AS is **not directly life-threatening**; morbidity is reproductive (infertility, pregnancy loss) and quality-of-life (chronic pain, psychological burden). Rare severe placenta accreta in subsequent pregnancy carries hemorrhage risk.
- **Prognostic factors:** severity/AFS stage, extent of residual functional endometrium, endometrial thickness/vascularity post-treatment, presence of chronic endometritis, and adhesion density.

---

## 12. Treatment

**Standard of care — hysteroscopic adhesiolysis** (NCIT:C15329 Surgical Procedure; more specifically operative hysteroscopy):
- **Cold microscissors** preferred over electrosurgery to reduce thermal injury, perforation, and recurrence ([outcomes searches](https://pmc.ncbi.nlm.nih.gov/articles/PMC10848492/)).
- Severe/obliterated cases may need ultrasound- or laparoscopy-guided dissection; often **repeated procedures**.

**Post-operative adhesion-reformation prevention** (adjuncts — the key strategy given high recurrence):
- **Physical barriers:** intrauterine balloon (Foley/Cook), IUD, **hyaluronic acid gel / auto–cross-linked HA** ([NCT02617108](https://clinicaltrials.gov/study/NCT02617108); HA outcomes [PMID:41267665](https://pubmed.ncbi.nlm.nih.gov/41267665/)).
- **Hormonal (estrogen ± progestogen) therapy** to stimulate re-epithelialization (NCIT:C15986 Pharmacotherapy; therapeutic_agent estrogen, CHEBI). **Important recent evidence caveat:** a **randomized trial (Hanstede et al., 2023, [PMID:37396823](https://pmc.ncbi.nlm.nih.gov/articles/PMC10308500/)) found hormonal support did NOT improve recurrence, menses, or endometrial thickness** — the efficacy of routine post-adhesiolysis estrogen is now questioned. Curate this as a `KNOWLEDGE_GAP` / competing-evidence point rather than settled benefit.
- **Antibiotics** where chronic endometritis is present.
- **Platelet-rich plasma (PRP)** intrauterine infusion — emerging adjunct.

**Advanced / experimental (regenerative) therapeutics** (NCIT:C15238 Gene Therapy / NCIT:C15431 stem-cell / cell therapy):
- **Menstrual blood-derived mesenchymal stem cells (MenSCs)** — attenuate TGF-β, down-regulate α-SMA and collagen I, promote proliferation; act mainly via **paracrine** signaling ([PMID:30760192](https://pubmed.ncbi.nlm.nih.gov/30760192/); [MenSC review](https://www.sciencedirect.com/science/article/pii/S2352320425000732)).
- **Bone marrow / umbilical cord MSCs**, autologous stem cell mobilization.
- **Stem-cell–derived exosomes** and **bioengineered hydrogels/scaffolds**; hESC-derived endometrial organoids + 3D Matrigel ([PMC8079828](https://pmc.ncbi.nlm.nih.gov/articles/PMC8079828/)).
- **Molecular targets under study:** THBS1 (PI3K/AKT), TGF-β1/Smad2/3 axis.
- **Assisted reproduction:** IVF ± gestational surrogacy for refractory uterine-factor infertility.

**Pharmacogenomics:** Not applicable.

---

## 13. Prevention

- **Primary prevention (most impactful):**
  - **Avoid unnecessary curettage**; prefer **medical management (misoprostol)** or expectant management for miscarriage.
  - Use **ultrasound-guided gentle suction / manual vacuum aspiration** rather than sharp curettage.
  - **Avoid the 2–4 week postpartum/post-miscarriage high-risk window** for instrumentation ([Fertility & Sterility](https://www.fertstert.org/article/S0015-0282(21)00537-9/fulltext); [PMID:33462894](https://pubmed.ncbi.nlm.nih.gov/33462894/)).
  - Limit repeat intrauterine procedures; treat genital infections (including TB) promptly.
- **Secondary prevention:** early hysteroscopic diagnosis in women with post-procedure menstrual change or infertility; treat chronic endometritis.
- **Tertiary prevention:** post-adhesiolysis barriers (balloon/HA gel), early **second-look hysteroscopy** to lyse re-forming adhesions, and endometrial-regeneration adjuncts.
- **Counseling:** reproductive/pre-conception counseling; genetic counseling **not applicable**.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (*Homo sapiens*, NCBITaxon:9606). Naturally occurring analogous intrauterine adhesion disease in other species is not well documented; endometrial fibrosis/scarring can occur in domestic animals but "Asherman syndrome" is a human clinical entity.
- **Breed / OMIA / veterinary:** No established OMIA entry (acquired, not genetic).
- **Comparative biology:** Endometrial regeneration is a conserved mammalian process; rodents serve as mechanistic surrogates rather than natural-disease models.
- **Zoonosis / transmission:** Not applicable.

---

## 15. Model Organisms

- **Rodent (mouse/rat) mechanical/chemical injury models — the workhorse:** Induced by intrauterine curettage/scraping, electrocoagulation, ethanol/trichloroacetic-acid instillation, or dual mechanical+LPS injury. These recapitulate **endometrial fibrosis, ↑TGF-β1/Smad, ↑α-SMA/collagen, thinned endometrium, and impaired fertility**, and are the standard platform for testing MSC/exosome/hydrogel therapies ([mechanisms & stem cell therapy review](https://www.discoverymedicine.com/Xuechai-Bai/2019/06/endometrial-fibrosis-and-stem-cell-therapy/)).
- **In vitro / cellular models:** primary human endometrial stromal cells with TGF-β1 stimulation (fibrosis induction); endometrial epithelial cultures; **iPSC/hESC-derived endometrial organoids** ([PMC8079828](https://pmc.ncbi.nlm.nih.gov/articles/PMC8079828/)).
- **Model characteristics / limitations:** Rodent uterine anatomy (bicornuate, rapid estrous cycling, high regenerative capacity) differs from human; models capture fibrosis and functional infertility well but imperfectly reproduce the human implantation-window epithelial phenotype and chronic recurrence dynamics. `evidence_source: MODEL_ORGANISM` for all rodent data; `IN_VITRO` for organoid/cell work.
- **Resources:** No dedicated AS model repository; models are protocol-defined and reported ad hoc in the literature.

---

## Key Ontology Term Summary (for KB population)

- **MONDO:** MONDO:0015299 (Asherman syndrome)
- **Phenotypes (HP):** HP:0000141 (Amenorrhea), HP:0011225 (Hypomenorrhea), HP:0008222 (Female infertility), HP:0500110/HP:0100615 (Recurrent spontaneous abortion), HP:0030144 (Hematometra), HP:0031331 (Abnormal uterine morphology)
- **Anatomy (UBERON):** UBERON:0001295 (endometrium), UBERON:0000995 (uterus), UBERON:0000002 (cervix), UBERON:0000474 (female reproductive system)
- **Cells (CL):** CL:0000186 (myofibroblast), CL:0000066 (epithelial cell), CL:0000064 (ciliated cell), CL:0000235 (macrophage)
- **Processes (GO):** GO:0007179 (TGF-β receptor signaling), GO:0030198 (ECM organization), GO:0061041 (regulation of wound healing), GO:0001525 (angiogenesis), GO:0016055 (Wnt signaling)
- **Treatments (NCIT):** NCIT:C15329 (Surgical Procedure — hysteroscopic adhesiolysis), NCIT:C15986 (Pharmacotherapy — estrogen), NCIT:C15238 (Gene Therapy), cell therapy (MSC)

---

## Curation Caveats / Evidence Notes

1. **Acquired disease** — do not populate causal-gene, inheritance, or germline-variant slots; explicitly mark N/A.
2. **Hormonal support efficacy is contested** — the 2023 RCT ([PMID:37396823](https://pmc.ncbi.nlm.nih.gov/articles/PMC10308500/)) is a REFUTE/PARTIAL-type evidence item against routine post-op estrogen; curate as a knowledge gap.
3. **Single-cell atlas ([PMID:37735465](https://pmc.ncbi.nlm.nih.gov/articles/PMC10514053/))** is the strongest molecular source for pathophysiology nodes and has an associated GEO dataset worth linking.
4. **Verify all PMIDs and snippets** with `just fetch-reference` before committing — PubMed abstracts were partly cookie-walled during this research; the exact-quote SOP (§Adding Evidence) must be applied to each claim.
5. This entry is a strong candidate to `conforms_to` the **`fibrotic_response`** module (tissue injury → inflammation → myofibroblast activation → excessive ECM → organ dysfunction), substituting endometrial stromal fibroblast → myofibroblast.

---

## Sources

- [Decoding the endometrial niche of Asherman's Syndrome at single-cell resolution — Nat Commun, PMID:37735465 (PMC10514053)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10514053/)
- [Intrauterine Adhesions and Asherman Syndrome: Retrospective Dive into Risk Factors, Diagnosis, Surgical Perspectives — PMID:40310333 (PMC12026105)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026105/)
- [Identifying risk factors and incidence of Asherman Syndrome in post-abortion curettage — PMID:33462894](https://pubmed.ncbi.nlm.nih.gov/33462894/)
- [Mechanistic insights into intrauterine adhesions — PMID:39613882](https://pubmed.ncbi.nlm.nih.gov/39613882/)
- [Asherman's syndrome: current perspectives on diagnosis and management — PMID:30936754 (Dovepress)](https://www.dovepress.com/ashermans-syndrome-current-perspectives-on-diagnosis-and-management-peer-reviewed-fulltext-article-IJWH)
- [The management of Asherman syndrome: a review of literature — Reprod Biol Endocrinol (Springer)](https://link.springer.com/article/10.1186/1477-7827-11-118)
- [Hormonal support in women with Asherman syndrome does not lead to better outcomes: a randomized trial — PMID:37396823 (PMC10308500)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10308500/)
- [Novel therapeutic strategies: endometrial regeneration using menstrual blood-derived stem cells — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352320425000732)
- [Endometrial Regeneration in Asherman's Syndrome: stem cell therapies — PMID:30760192](https://pubmed.ncbi.nlm.nih.gov/30760192/)
- [Stem cell therapy targets THBS1 to reverse endometrial fibrosis — Frontiers (PMC12916671)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916671/)
- [Endometrial membrane organoids from hESC + 3D Matrigel — PMC8079828](https://pmc.ncbi.nlm.nih.gov/articles/PMC8079828/)
- [Review of Asherman syndrome and hysteroscopic treatment outcomes (low-resource setting) — PMC10848492](https://pmc.ncbi.nlm.nih.gov/articles/PMC10848492/)
- [Fertility & obstetric outcomes: hyaluronic acid post-adhesiolysis — PMID:41267665](https://pubmed.ncbi.nlm.nih.gov/41267665/)
- [Avoiding Asherman's syndrome: refining uterine evacuation — Fertility and Sterility](https://www.fertstert.org/article/S0015-0282(21)00537-9/fulltext)
- [Intrauterine balloon + postoperative estrogen — NCT02617108](https://clinicaltrials.gov/study/NCT02617108)
- [NORD — Asherman's Syndrome](https://rarediseases.org/rare-diseases/ashermans-syndrome/)
- [Orphanet — Asherman syndrome (ORPHA:137686)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=137686)
- [Mechanisms of Endometrial Fibrosis and Stem Cell Therapy — Discovery Medicine](https://www.discoverymedicine.com/Xuechai-Bai/2019/06/endometrial-fibrosis-and-stem-cell-therapy/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.