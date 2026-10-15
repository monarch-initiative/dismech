---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-26T12:56:18.547023'
end_time: '2026-08-26T13:00:34.799828'
duration_seconds: 256.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex I Deficiency Nuclear Type 31
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 19
  total_cost_usd: 1.1401934000000002
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 16
reference_validation:
  total_references: 5
  verified: 4
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency Nuclear Type 31
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency Nuclear Type 31** covering all of the
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

# Mitochondrial Complex I Deficiency, Nuclear Type 31 (MC1DN31) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Mitochondrial Complex I Deficiency, Nuclear Type 31 (MC1DN31) is an ultra-rare, autosomal recessive, early-onset mitochondrial encephalomyopathy caused by biallelic pathogenic variants in **TIMMDC1** (Translocase of Inner Mitochondrial Membrane Domain-Containing Protein 1), a nuclear-encoded assembly chaperone for the mitochondrial NADH:ubiquinone oxidoreductase (respiratory chain Complex I). It belongs to the large genetically heterogeneous group of "mitochondrial complex I deficiency, nuclear type" (MC1DN1–MC1DNxx) disorders catalogued in OMIM, which collectively represent the most common biochemical signature of pediatric mitochondrial disease. MC1DN31 was first delineated by Kremer et al. (2017) using transcriptome (RNA-seq) sequencing to solve previously unsolved exome-negative cases, establishing TIMMDC1 as a novel disease gene (PMID: 28607462, *Nat Commun* 8:15824) [omim.org/entry/618251].

**Key identifiers:**
- **OMIM (phenotype):** #618251 — MITOCHONDRIAL COMPLEX I DEFICIENCY, NUCLEAR TYPE 31; MC1DN31
- **OMIM (gene):** *615534 — TIMMDC1 (chromosome 3q13, gene ID 51300; also known as *C3orf1*)
- **NCBI GTR / MedGen:** C4748838
- **Transcript reference:** NM_016589.4 (also cited as NM_001143988 in some reports, accounting for two equivalent HGVS numbering systems for the same intronic variant)
- **MONDO / Orphanet:** No stable, independently searchable MONDO or Orphanet-specific code could be confirmed via web search in this session — MC1DN31 is indexed primarily through the OMIM phenotypic series for nuclear Complex I deficiency and via NCBI GTR/MedGen (C4748838); this should be verified directly against a live MONDO/Orphanet lookup before use in curation, as recommended in the dismech term-binding workflow.
- **Synonyms:** "Mitochondrial complex 1 deficiency, nuclear type 31"; "TIMMDC1-related mitochondrial disease"; "TIMMDC1-related Leigh syndrome" (informal, used in some case reports)

**Data provenance.** All available characterization of MC1DN31 derives from **aggregated case-report/case-series literature** (a handful of probands across ~3–5 families reported in the literature to date) rather than large-cohort disease registries or EHR-derived data — reflecting its status as an ultra-rare, recently delineated Mendelian disorder.

Sources: [OMIM #618251](https://www.omim.org/entry/618251), [OMIM *615534](https://omim.org/entry/615534), [NCBI GTR C4748838](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4748838/)

---

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic — biallelic (homozygous or compound heterozygous) loss-of-function variants in **TIMMDC1**, causing loss of Complex I assembly-chaperone function and resultant isolated Complex I deficiency.

**Genetic risk factors:**
- Homozygosity or compound heterozygosity for pathogenic TIMMDC1 alleles. The recurrent, best-characterized allele is a **deep intronic variant**, reported under two equivalent numbering conventions: **c.596+2146A>G** (intron 5, NM_001143988 numbering, Kremer et al. 2017) and **c.597-1340A>G** (NM_016589.4 numbering, later reports). This variant creates a novel intronic splice-donor motif, causing insertion of an ~80-bp "poison" pseudoexon between exons 5 and 6, a frameshift, and a premature stop codon (predicted p.Gly199_Thr200ins5*) (PMID: 28607462; PMID: 35091571).
- A second reported pathogenic allele is the nonsense variant **c.673C>T (p.Arg225Ter)**, found in ClinVar in association with Leigh syndrome/complex I deficiency (RCV000735814).
- Because the recurrent deep-intronic variant lies outside standard exome-capture regions, **exome sequencing alone frequently fails to detect it**, and diagnosis has historically required RNA-sequencing or targeted intronic/genome sequencing (a major diagnostic-odyssey theme in the literature) (PMID: 33278652, "Deep intronic TIMMDC1 variant delays diagnosis of rapidly progressive complex I deficiency").
- Population allele frequency data (gnomAD): the c.597-1340A>G deep-intronic allele has been reported at a population frequency around **AF ≈ 0.0001946** (≈1 in 5,000 alleles) in gnomAD, consistent with an ultra-rare recessive founder-type allele but not with common polymorphism; a second, distinct missense variant, c.410G>A (p.Arg137His), is present in gnomAD at AF ≈ 0.00002015 with no reported homozygotes.

**Environmental risk factors:** None established; this is a purely Mendelian genetic disorder with no known environmental, infectious, toxin, or lifestyle contribution to primary disease causation.

**Protective factors:** None identified in the literature (genetic or environmental). No modifier alleles have been reported.

**Gene-environment interactions:** None documented. As with other primary mitochondrial respiratory-chain disorders, intercurrent illness/metabolic stress (e.g., febrile infection) may precipitate clinical decompensation in affected individuals, but this is inferred from the general mitochondrial-disease literature rather than TIMMDC1-specific data.

---

## 3. Phenotypes

Phenotype data are drawn from the original Kremer et al. (2017) description of three unrelated MC1DN31 families and subsequent case reports (Bris et al., 2021, PMID 33278652; Bhatt et al., 2022, PMID 35091571; a dual-diagnosis Leigh-syndrome case, PMID 30981218).

| Phenotype | Type | Onset | Frequency/notes | Suggested HP term |
|---|---|---|---|---|
| Hypotonia | Sign | Infantile (neonatal/early postnatal) | Core, near-universal feature | HP:0001252 (Hypotonia) |
| Failure to thrive / poor feeding | Sign | Infantile, early postnatal | Core feature; reported in multiple families | HP:0001508 (Failure to thrive); HP:0011968 (Feeding difficulties) |
| Developmental delay / minimal or absent psychomotor development | Sign | Infantile, progressive | Core, often profound | HP:0001263 (Global developmental delay) |
| Developmental regression | Sign | Infantile-childhood | Reported in progressive cases | HP:0002376 (Developmental regression) |
| Sensorineural hearing loss | Sign | Variable | Reported in a subset | HP:0000407 (Sensorineural hearing impairment) |
| Dysmetria | Sign | Variable | Cerebellar feature | HP:0001310 (Dysmetria) |
| Dyskinetic/dystonic movements | Sign | Variable | Reported in a subset | HP:0100660 (Dyskinesia) / HP:0001332 (Dystonia) |
| Peripheral neuropathy | Sign | Variable | Reported in multiple patients | HP:0009830 (Peripheral neuropathy) |
| Nystagmus | Sign | Variable | Reported in a subset | HP:0000639 (Nystagmus) |
| Drug-resistant / refractory seizures | Sign | Infantile-childhood | Reported in a subset; drives rapid decline in severe cases | HP:0011168 (Refractory seizures) |
| Leigh-syndrome-pattern brain MRI (bilateral T2 hyperintensities, basal ganglia and/or brainstem) | Imaging/sign | Infantile-childhood | Reported in a subset of patients | HP:0002490 (Increased CSF lactate) is not imaging-specific; use HP:0007074 (Bilateral basal ganglia lesions) / HP:0002490 for biochemical correlate; Leigh-syndrome pattern itself is best captured via disease-level MONDO cross-reference rather than a single HP term |
| Muscle wasting | Sign | Progressive | Reported | HP:0003202 (Skeletal muscle atrophy) |
| Isolated Complex I enzymatic deficiency (muscle) | Laboratory abnormality | At biopsy | ~15% of control activity in reported muscle biopsies | HP:0003688 (Mitochondrial respiratory chain complex I deficiency) |

**Characteristics:**
- **Age of onset:** Infantile (neonatal to first months of life) in essentially all reported cases.
- **Severity/course:** Severe and, in reported deep-intronic-variant cases, **rapidly progressive and often fatal** ("severe, inevitably fatal neurodegenerative disorder affecting both central and peripheral nervous systems," per the ASO-correction study, PMID 35091571). Some individuals show a Leigh-syndrome-like course; others present with a more static severe encephalopathy or refractory epilepsy-dominant course.
- **Frequency among affected individuals:** Because the total reported cohort is small (a handful of probands across a few families), frequency percentages for individual features are not statistically robust; features above are described qualitatively as "core" (hypotonia, failure to thrive, developmental delay) versus "variable" (deafness, dysmetria, dyskinesia, neuropathy, nystagmus, seizures) per OMIM's synopsis of the Kremer et al. cohort.
- **Quality of life impact:** Not formally studied with standardized instruments (EQ-5D, SF-36) for this specific gene; qualitatively, the disorder is severely disabling and life-limiting given profound neurodevelopmental impairment and, in the more aggressive presentations, early mortality.

---

## 4. Genetic/Molecular Information

**Causal gene:** TIMMDC1 (HGNC gene symbol TIMMDC1; OMIM *615534; Gene ID 51300; also historically named C3orf1), located on chromosome 3q13.

**Pathogenic variants reported:**

| Variant (HGVS) | Type | Effect | Source |
|---|---|---|---|
| c.596+2146A>G (≡ c.597-1340A>G in alternate transcript numbering) | Deep intronic, splice-enhancer-creating | Inserts an ~80-bp pseudoexon ("poison exon") between exons 5–6 → frameshift → premature stop (p.Gly199_Thr200ins5*); near-complete loss of TIMMDC1 protein | Kremer et al. 2017 (PMID 28607462); Bris et al. 2021 (PMID 33278652); Bhatt et al. 2022 (PMID 35091571) |
| c.673C>T (p.Arg225Ter) | Nonsense | Premature truncation | ClinVar RCV000735814 (Leigh syndrome) |
| c.410G>A (p.Arg137His) | Missense | Present in gnomAD (AF ≈ 0.00002, no homozygotes); pathogenicity less firmly established | population database |

- **Variant classification:** The recurrent deep-intronic allele is classified pathogenic/likely pathogenic in ClinVar for "Mitochondrial complex I deficiency, nuclear type 31" (RCV000493542, NM_016589.4:c.597-1340A>G).
- **Allele frequency:** c.597-1340A>G reported at gnomAD AF ≈ 0.0001946; consistent with a rare recessive allele capable of biallelic disease in homozygotes or compound heterozygotes but not itself common.
- **Somatic vs. germline:** Germline only; no somatic mosaicism reported.
- **Functional consequence:** Loss of function — near-complete absence of TIMMDC1 protein in patient fibroblasts/muscle, with downstream failure of Complex I membrane-arm assembly.
- **Modifier genes:** None established.
- **Epigenetic information:** Not reported for this gene/disease.
- **Chromosomal abnormalities:** None reported; disease is caused by point/intronic sequence variants, not structural chromosomal rearrangements.

**Molecular/functional detail on TIMMDC1:**
- TIMMDC1 encodes a **four-transmembrane-domain inner mitochondrial membrane protein** that functions as an assembly chaperone specifically for the **membrane arm of Complex I**.
- It is a component of, or closely interacts with, the **mitochondrial Complex I assembly (MCIA) complex** (which includes NDUFAF1, ECSIT, ACAD9, TMEM126B), consistent with its role in Complex I biogenesis rather than catalysis itself.
- In patient tissue (fibroblasts, skeletal muscle), loss of TIMMDC1 causes **reduced expression of multiple Complex I structural subunits**, notably **NDUFA9, NDUFB8, and NDUFA13**, and impaired incorporation of both membrane-embedded and soluble arms of the holoenzyme (quantitative proteomics data cited in OMIM #618251 and PMID 28607462).
- Functional rescue: expression of wild-type TIMMDC1 cDNA in patient fibroblasts partially restores Complex I assembly, confirming causality (Kremer et al. 2017).
- **Complex I enzymatic activity** in patient skeletal muscle biopsies was reported at **~15% of control levels**, indicating severe isolated Complex I deficiency without involvement of other respiratory chain complexes.

Ontology suggestions: **HGNC:** TIMMDC1; **GO (molecular function/process):** GO:0032981 (mitochondrial respiratory chain complex I assembly); **GO (cellular component):** GO:0005743 (mitochondrial inner membrane), GO:0045271 (respiratory chain complex I).

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated in the etiology of MC1DN31 — it is a fully penetrant recessive Mendelian disorder. As is generic to mitochondrial disease broadly, febrile illness or metabolic stress may be an exacerbating (not causal) factor for acute clinical decompensation, but no TIMMDC1-specific data document this.

---

## 6. Mechanism / Pathophysiology

**Causal chain:**
1. Biallelic pathogenic TIMMDC1 variants (most commonly the deep-intronic splice-enhancer variant) → aberrant pre-mRNA splicing with pseudoexon inclusion → frameshift/premature termination codon → **near-complete loss of TIMMDC1 protein**.
2. Loss of TIMMDC1 (an inner-mitochondrial-membrane, four-transmembrane-domain assembly chaperone that interacts with the MCIA assembly complex) → **failure of proper assembly of the membrane arm of Complex I** (NADH:ubiquinone oxidoreductase), with downregulation of structural subunits including NDUFA9, NDUFB8, and NDUFA13.
3. Resulting **isolated, severe Complex I enzymatic deficiency** (~15% of normal activity in patient muscle) → impaired oxidative phosphorylation and ATP generation, particularly in high-energy-demand tissues (central and peripheral nervous system, skeletal muscle).
4. Downstream tissue consequences: neuronal energy failure manifesting as hypotonia, developmental delay/regression, cerebellar and extrapyramidal signs (dysmetria, dyskinesia), sensorineural hearing loss, peripheral neuropathy, and, in the classic Leigh-syndrome-pattern subset, symmetric necrotizing lesions of the basal ganglia and brainstem visible on MRI.

**Molecular pathway:** Oxidative phosphorylation / mitochondrial respiratory chain assembly pathway (KEGG: Oxidative phosphorylation, hsa00190; Reactome: "Complex I biogenesis").

**Cellular process:** Mitochondrial respiratory complex I assembly (GO:0032981); impaired oxidative phosphorylation (GO:0006119); secondary mitochondrial dysfunction/energy failure in postmitotic, high-energy-demand cell types (neurons, myocytes).

**Protein dysfunction:** Loss of TIMMDC1 chaperone activity leads to failed/incomplete assembly (not misfolding/aggregation of TIMMDC1 itself, since the recurrent variant essentially abolishes protein expression via nonsense-mediated decay of the aberrantly spliced transcript / loss of the transcript product).

**Metabolic changes:** Consistent with other Complex I deficiencies — impaired NADH oxidation, reduced ATP synthesis, potential for elevated lactate/lactate:pyruvate ratio (a standard biochemical hallmark of primary mitochondrial disease, though TIMMDC1-specific lactate data were not confirmed in the sources retrieved in this session).

**Immune system involvement:** None reported; this is not an immune-mediated disorder.

**Tissue damage mechanism:** Bioenergetic failure/oxidative stress in postmitotic neurons and skeletal muscle from chronic ATP deficit, consistent with the general Leigh-syndrome-spectrum mechanism (necrotizing microvascular proliferation and neuronal loss in basal ganglia/brainstem in MRI-positive cases).

**Biochemical abnormality:** Isolated Complex I (NADH:ubiquinone oxidoreductase) enzymatic deficiency, confirmed in skeletal muscle biopsy (~15% of control activity).

**Molecular profiling:** RNA-sequencing (transcriptomics) was the key diagnostic and mechanistic tool that established TIMMDC1 causality — detecting the aberrant pseudoexon-containing transcript and reduced TIMMDC1 RNA/protein expression in patient fibroblasts (Kremer et al. 2017, PMID 28607462). Quantitative proteomics on patient cells demonstrated reduced abundance of multiple Complex I subunits and confirmed a role for TIMMDC1 in assembling both membrane-embedded and soluble arms of the complex.

**Advanced technologies:** No single-cell, spatial transcriptomic, or CRISPR functional-screen data specific to TIMMDC1/MC1DN31 were identified in this search session. RNA-seq-based "aberrant expression/splicing event" detection (as implemented in tools such as OUTRIDER/FRASER, developed alongside the Kremer et al. work) remains the signature methodological advance associated with this gene's disease discovery.

Ontology suggestions: **GO:BP** GO:0032981 (mitochondrial respiratory chain complex I assembly); **GO:CC** GO:0005743 (mitochondrial inner membrane), GO:0030964 (NADH dehydrogenase complex); **CL** CL:0000540 (neuron), CL:0000187 (muscle cell).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (brain — basal ganglia, brainstem, cerebellum), peripheral nervous system, skeletal muscle, and (in a subset) the inner ear (cochlea, for sensorineural hearing loss).
- **Secondary:** Growth/nutritional axis (failure to thrive is a systemic secondary consequence of severe energy deficit and feeding difficulty).
- **Body systems:** Nervous system (primary), neuromuscular system, auditory system.

**Tissue/cell level:**
- Neurons (particularly basal ganglia and brainstem neurons in Leigh-pattern cases), cerebellar neurons/Purkinje-adjacent circuitry (dysmetria), peripheral nerve axons (neuropathy), skeletal muscle fibers (biopsy-documented Complex I deficiency and muscle wasting).
- Suggested Cell Ontology terms: CL:0000540 (neuron), CL:0000206 (peripheral neuron / relevant subtype), CL:0000187 (muscle cell), CL:0002496 (cortical GABAergic cell — not specifically documented, listed only as illustrative example; do not curate without direct source support).

**Subcellular level:**
- **Mitochondria**, specifically the **mitochondrial inner membrane** (GO:0005743) — TIMMDC1's site of action and the physical site of Complex I assembly.

**Localization / UBERON terms:**
- Basal ganglia (UBERON:0002420), brainstem (UBERON:0002298), cerebellum (UBERON:0002037), peripheral nerve (UBERON:0000010), skeletal muscle tissue (UBERON:0001134), cochlea (UBERON:0001844).
- **Lateralization:** Bilateral/symmetric, consistent with the classic Leigh-syndrome MRI pattern reported in a subset of patients (bilateral basal ganglia and/or brainstem T2 hyperintensities).

---

## 8. Temporal Development

- **Onset:** Infantile — typically neonatal to first months of life (hypotonia, poor feeding, failure to thrive as presenting features).
- **Onset pattern:** Insidious-to-subacute in most reported cases, though the deep-intronic-variant cases described by Bris et al. (2021) were explicitly characterized as **"rapidly progressive."**
- **Progression:** Progressive neurodegenerative course; developmental regression, worsening movement disorder, and (in severe cases) refractory seizures over the first months to years of life.
- **Disease course pattern:** Progressive, not relapsing-remitting; some patients described with a Leigh-syndrome-like subacute necrotizing encephalomyelopathy course (episodic decompensations superimposed on chronic decline are typical of the broader Leigh-syndrome spectrum, though not explicitly itemized for TIMMDC1 cases in the sources reviewed).
- **Disease duration:** Chronic, lifelong for survivors; the most severe (deep-intronic-variant) reported cases were described as **"inevitably fatal"** in early life.
- **Remission:** None reported — no spontaneous or treatment-induced remission described.
- **Critical periods:** Infancy represents the critical window for both symptom onset and (per the investigational ASO work) the theoretical window for intervention before irreversible neurodegeneration, paralleling other severe infantile mitochondrial encephalopathies.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (AR).
- **Prevalence/incidence:** No disease-specific prevalence or incidence figures are available for MC1DN31 given its very recent delineation (2017) and the small number of reported families (on the order of single digits of unrelated pedigrees across the literature reviewed: 3 families in Kremer et al. 2017, plus additional single-family reports in 2019–2022). For context, **mitochondrial Complex I deficiency as a biochemical category** (all genetic causes combined) is estimated to affect roughly **1 in 5,000–10,000 live births**, but this is not a MC1DN31-specific figure.
- **Penetrance:** Presumed complete/high penetrance in homozygotes/compound heterozygotes for the recurrent pathogenic allele, based on consistent, severe phenotypes across reported families; formal penetrance estimates are not available.
- **Expressivity:** Variable — while core features (hypotonia, failure to thrive, developmental delay) are consistent, the additional neurological features (deafness, dysmetria, dyskinesia, neuropathy, nystagmus, seizures, Leigh-pattern MRI) are variably present across reported individuals, and overall disease severity/tempo (e.g., the "rapidly progressive, fatal" subset) also varies.
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** The recurrence of the identical deep-intronic variant (c.596+2146A>G / c.597-1340A>G) across multiple unrelated families raises the possibility of a founder or recurrent mutational hotspot allele, though a formal founder-haplotype study was not identified in this search.
- **Consanguinity:** Given the autosomal recessive inheritance and presentation as homozygosity in reported probands, consanguinity is plausible in some families, though this was not confirmed with specific pedigree data in the sources retrieved.
- **Carrier frequency:** Based on the gnomAD allele frequency of the recurrent deep-intronic variant (~0.0002), the carrier frequency for that specific allele is on the order of 1 in ~2,500 in the general population sampled by gnomAD, though this must be treated cautiously since gnomAD allele-frequency estimates for deep-intronic/functionally cryptic variants can be affected by ascertainment and annotation limitations.
- **Population demographics:** No specific ethnic or geographic enrichment has been established in the literature reviewed; reported families appear to derive from mixed/unspecified ancestries in the original case series.
- **Sex ratio / age distribution:** No sex predilection expected (autosomal, not X-linked); affected individuals are, by definition of the phenotype, presenting in infancy.

---

## 10. Diagnostics

**Laboratory/biochemical tests:**
- Skeletal muscle biopsy with **respiratory chain enzyme activity assay** demonstrating isolated Complex I deficiency (~15% of control activity in reported cases), with normal activity of Complexes II–V — the classic biochemical signature guiding a nuclear Complex I gene search.
- Plasma/CSF lactate (commonly elevated in Leigh-spectrum disease generally; not explicitly quantified for TIMMDC1 cases in sources reviewed here).

**Biomarkers:** Complex I activity level is the principal disease-specific functional biomarker; no circulating protein or metabolite biomarker specific to TIMMDC1 deficiency has been established.

**Imaging:** Brain MRI — bilateral, symmetric T2/FLAIR hyperintensities in the basal ganglia and/or brainstem, consistent with a Leigh-syndrome pattern, reported in a subset of MC1DN31 patients.

**Genetic testing:**
- **Whole exome sequencing (WES):** Often **non-diagnostic** for the recurrent deep-intronic TIMMDC1 variant because it lies outside standard coding-exon capture regions — a key diagnostic pitfall documented in this disease (PMID 33278652 specifically reports diagnostic delay from this cause).
- **RNA sequencing (transcriptomics):** The methodology that originally established and continues to be the most reliable route to detecting the pathogenic aberrant-splicing event in TIMMDC1 (pseudoexon inclusion, reduced RNA/protein expression) — pioneered by Kremer et al. (2017) as a genome-wide RNA-seq-based diagnostic strategy for exome-negative mitochondrial disease.
- **Whole genome sequencing (WGS):** Would in principle detect the deep-intronic variant (unlike WES) but requires either a priori knowledge of the variant/gene or an RNA-seq-informed re-analysis to interpret its pathogenicity.
- **Gene panels:** Primary mitochondrial disease/nuclear-encoded Complex I panels that include TIMMDC1 and specifically extend coverage into relevant deep-intronic regions would be required; standard panels limited to coding exons ± short flanking intron may miss the recurrent allele.
- **Single-gene testing:** Targeted TIMMDC1 sequencing (including the specific deep-intronic region) is possible once a laboratory is aware of the recurrent pathogenic allele.
- **Mitochondrial DNA testing:** Not informative for this nuclear-encoded gene disorder but is a standard part of the differential work-up for isolated Complex I deficiency to exclude primary mtDNA (e.g., MT-ND) causes.

**Clinical criteria:** No TIMMDC1/MC1DN31-specific consensus diagnostic criteria exist; diagnosis follows the general framework for genetically confirmed primary mitochondrial disease/Leigh syndrome spectrum (clinical phenotype + biochemical Complex I deficiency + molecular confirmation).

**Differential diagnosis:** Other nuclear (MC1DN1–MC1DN30+, e.g., NDUFS/NDUFA/NDUFB/NDUFAF-related) and mitochondrial-DNA-encoded (MT-ND1–6) causes of isolated Complex I deficiency and Leigh syndrome; other complex I assembly-factor disorders (e.g., NDUFAF1, NDUFAF2, ACAD9, ECSIT, TMEM126B-related disease, given TIMMDC1's association with the MCIA assembly complex); PDHX-related pyruvate dehydrogenase deficiency (documented as a genuine dual-diagnosis confounder in one reported TIMMDC1 case, PMID 30981218).

**Screening:** No population or newborn screening program exists for this ultra-rare condition; cascade/carrier testing in families with an identified proband is the applicable model, per standard AR-disease genetic counseling practice.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Prognosis is poor. The best-characterized recurrent-variant cases were explicitly described in the literature as causing a **"severe, inevitably fatal neurodegenerative disorder"** with a **"rapidly progressive"** course in at least one reported sibling pair (PMID 33278652; PMID 35091571). No formal actuarial survival curves or 5-/10-year survival statistics are available given the rarity of the condition.
- **Morbidity/function:** Profound, essentially universal neurodevelopmental impairment (severe global developmental delay, often with regression), motor impairment (hypotonia progressing to dystonia/dyskinesia), sensory impairment (hearing loss, peripheral neuropathy), and in a subset, drug-resistant epilepsy.
- **Quality of life:** Not formally measured with standardized instruments for this gene; qualitatively severe based on the clinical description (profound disability, feeding difficulty, seizures).
- **Complications:** Failure to thrive/malnutrition, aspiration risk from feeding difficulties (inferred from hypotonia/feeding difficulty, not explicitly documented), status epilepticus risk in refractory-epilepsy cases, progressive muscle wasting.
- **Recovery potential:** No evidence of spontaneous recovery; disease is progressive. Investigational antisense-oligonucleotide (ASO) splice correction has shown proof-of-concept restoration of TIMMDC1 protein and Complex I function **in patient-derived fibroblasts** (PMID 35091571) but has not yet translated to a clinical therapy with documented patient outcomes.
- **Prognostic factors:** Presence/absence of the specific deep-intronic allele versus other variant types, degree of residual Complex I activity, and presence of refractory epilepsy or a Leigh-syndrome MRI pattern may correlate with more severe/rapid courses, though formal genotype-phenotype correlation studies are not available given cohort size.

---

## 12. Treatment

**No disease-modifying or curative therapy is FDA-approved or established in clinical practice for MC1DN31.** Management is supportive/symptomatic, following general standard-of-care principles for primary mitochondrial (Complex I) disease and Leigh-syndrome-spectrum disorders:

- **Supportive care / symptom management:**
  - Nutritional support / feeding intervention for failure to thrive and feeding difficulties (NCIT:C15433 Nutritional Support; NCIT:C15747 Supportive Care).
  - Antiepileptic pharmacotherapy for refractory seizures (NCIT:C15986 Pharmacotherapy).
  - Physical therapy / occupational therapy / rehabilitative care for hypotonia and motor impairment (NCIT:C15302 Physical Therapy; NCIT:C121351 Occupational Therapy).
  - Hearing amplification/audiological management for sensorineural hearing loss (no dedicated NCIT device term is available per the dismech term-binding conventions; this would typically be modeled with a free-text `preferred_term` and no bound `term:`).
  - Genetic counseling for families given autosomal recessive inheritance and recurrence risk (NCIT:C15240 Genetic Counseling).
  - General "mitochondrial cocktail" supportive supplementation (e.g., coenzyme Q10, riboflavin, carnitine) is standard empiric practice across primary mitochondrial disease broadly, though no TIMMDC1/MC1DN31-specific efficacy data were identified in this search — this should not be curated as disease-specific evidence without a direct primary source.

- **Experimental/investigational therapeutics:**
  - **Splice-switching antisense oligonucleotide (ASO) therapy:** Bhatt et al. (2022, PMID 35091571, *npj Genomic Medicine*) designed two splice-switching oligonucleotides (SSO1, SSO2) targeting the pathogenic deep-intronic splice-enhancer sequence in TIMMDC1 patient-derived fibroblasts. Treatment produced "complete disappearance" of the aberrant (pseudoexon-containing) transcript, restoration of TIMMDC1 protein to near-normal levels, restoration of Complex I subunit abundance (quantitative proteomics), and significantly increased oxygen consumption rate, ATP production, and maximal mitochondrial respiration. This is a **preclinical (cell-based), personalized-medicine (n-of-few "milasen"-style) proof-of-concept**, not a clinically deployed therapy — therapeutic_modality would be curated as `ANTISENSE_OLIGONUCLEOTIDE` (mechanism: `SPLICE_MODULATION_EXON_SKIPPING` — the ASO suppresses inclusion of the aberrant pseudoexon rather than promoting skipping of a natural exon, so the precise `aso_mechanism` enum value should be selected carefully against the schema's available options at curation time).

- **Gene therapy / cell therapy / organ transplantation / surgery:** None reported or applicable for this disorder in the literature reviewed.

- **Clinical trials:** No disease-specific registered clinical trials (NCT identifiers) for MC1DN31/TIMMDC1 were identified in this search session.

---

## 13. Prevention

- **Primary prevention:** None available beyond genetic counseling and reproductive options (carrier testing, prenatal diagnosis, preimplantation genetic testing) in families with a known proband/pathogenic allele — standard practice for a defined autosomal recessive Mendelian disorder, though no TIMMDC1-specific prenatal/PGT program was documented in sources reviewed.
- **Secondary prevention:** Early recognition via expanded diagnostic use of RNA-sequencing in exome-negative suspected mitochondrial disease may shorten the diagnostic odyssey documented in this condition (per PMID 33278652), enabling earlier supportive management, though this does not alter the underlying disease course based on currently available data.
- **Screening:** No population-level newborn or carrier screening program specifically targets TIMMDC1; cascade testing within affected families is the applicable model.
- **Immunization:** Not applicable — no infectious etiology.
- **Public health / environmental interventions:** Not applicable, as this is a purely genetic disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring TIMMDC1-deficient disease has been reported in non-human species (companion animals, livestock, or wildlife) in the sources reviewed.
- **Orthologous gene:** TIMMDC1 orthologs exist across vertebrates and even in *Drosophila melanogaster* (FlyBase gene FBgn0010340, *Dmel\Timmdc1*), reflecting deep evolutionary conservation of Complex I assembly machinery, but no disease-relevant comparative pathology data were found.
- **Comparative biology:** Not documented for this specific gene beyond the noted orthology.
- **Transmission:** Not applicable (not an infectious or zoonotic condition).

---

## 15. Model Organisms

- **Mouse:** According to IMPC (International Mouse Phenotyping Consortium) phenotype data referenced in web search results, ***Timmdc1* knockout is embryonic lethal in mice** (consistent with the essential, non-redundant role of TIMMDC1 in Complex I assembly and with the severe, often fatal human phenotype). This is analogous to embryonic lethality reported for other core Complex I assembly-factor knockouts in mice (e.g., *Ndufs4*, *Nubpl*), underscoring that a complete/near-complete loss-of-function TIMMDC1 mouse model likely cannot recapitulate postnatal human disease progression without a hypomorphic allele strategy — no hypomorphic or conditional *Timmdc1* mouse model with reported neurological phenotyping was identified in this search.
- **Zebrafish, Drosophila, C. elegans, iPSC/organoid models:** No TIMMDC1-specific disease models in these systems were identified in the sources reviewed in this session.
- **Patient-derived cellular models:** The most informative "model system" reported to date is **patient-derived dermal fibroblasts**, used across the Kremer et al. (2017) discovery study and the Bhatt et al. (2022) ASO-correction study to demonstrate (a) loss of TIMMDC1 protein and impaired Complex I assembly, (b) partial functional rescue by wild-type TIMMDC1 cDNA re-expression, and (c) splice correction and functional (oxygen consumption/ATP) rescue by antisense oligonucleotide treatment. These represent high-fidelity, patient-genotype-matched in vitro models directly recapitulating the molecular lesion (RECAPITULATES-type evidence for the pathophysiology node "Complex I assembly failure"), though as an in vitro/cell-culture system they cannot address whole-organism phenotypic features (e.g., seizures, hearing loss, cerebellar signs).
- **Model database resources:** MGI (Mouse Genome Informatics) entry MGI:1922139 (*Timmdc1*) is the relevant mouse-gene record for further phenotype-data retrieval; IMPC (International Mouse Phenotyping Consortium) holds the embryonic-lethality phenotype data referenced above.

---

## Curation Notes for dismech Entry Construction

- **Evidence strength caveat:** This is an ultra-rare, very recently described (2017 onward) disorder with a total literature base on the order of a handful of case reports/series. Every quantitative claim above (e.g., "~15% of control Complex I activity," gnomAD allele frequencies, the embryonic-lethal mouse phenotype) should be **re-verified against the primary source with an exact quoted snippet** before being entered as `evidence:` per dismech's non-negotiable snippet-fidelity rule — several figures here were extracted via search-summary tooling rather than direct primary-text reading, and PubMed abstract text could not be retrieved verbatim in this session (cookie-wall block on PMID 33278652).
- **Primary references to fetch and cache** (`just fetch-reference`): PMID:28607462 (Kremer et al. 2017, gene discovery), PMID:33278652 (Bris et al., deep intronic variant/diagnostic delay), PMID:35091571 (Bhatt et al., ASO correction — candidate for an `experimental_models` IN_VITRO fibroblast entry with `modeled_mechanisms`), PMID:30981218 (dual PDHX/TIMMDC1 diagnosis case, useful for differential-diagnosis/Named-Entity-Confusion awareness), and the underlying ClinVar records RCV000493542 and RCV000735814 for variant-level evidence.
- **MONDO ID** could not be confirmed directly in this session and must be resolved through the dismech-terms workflow (or a direct Monarch/MONDO ontology browser lookup) rather than asserted from the OMIM ID alone.

---

### Sources

- [OMIM #618251 — MITOCHONDRIAL COMPLEX I DEFICIENCY, NUCLEAR TYPE 31; MC1DN31](https://www.omim.org/entry/618251)
- [OMIM *615534 — TIMMDC1](https://omim.org/entry/615534)
- [NCBI GTR — Mitochondrial complex I deficiency, nuclear type 31 (C4748838)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4748838/)
- [ClinVar RCV000493542 — TIMMDC1 c.597-1340A>G and MC1DN31](https://www.ncbi.nlm.nih.gov/clinvar/RCV000493542/)
- [ClinVar RCV000735814 — TIMMDC1 c.673C>T (p.Arg225Ter) and Leigh syndrome](https://www.ncbi.nlm.nih.gov/clinvar/RCV000735814/)
- [Kremer LS et al., "Genetic diagnosis of Mendelian disorders via RNA sequencing," Nat Commun 8:15824 (2017), PMID 28607462](https://www.nature.com/articles/ncomms15824)
- [Bris C et al., "Deep intronic TIMMDC1 variant delays diagnosis of rapidly progressive complex I deficiency," PMID 33278652](https://pubmed.ncbi.nlm.nih.gov/33278652/) / [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1769721220308302)
- [Bhatt DK et al., "Oligonucleotide correction of an intronic TIMMDC1 variant in cells of patients with severe neurodegenerative disorder," npj Genomic Medicine, PMID 35091571](https://www.nature.com/articles/s41525-021-00277-7) / [PMC8799713](https://pmc.ncbi.nlm.nih.gov/articles/PMC8799713/)
- ["A patient with homozygous nonsense variants in two Leigh syndrome disease genes," PMID 30981218](https://pubmed.ncbi.nlm.nih.gov/30981218/)
- [TIMMDC1 Gene — GeneCards](https://www.genecards.org/card/TIMMDC1)
- [Orphanet — TIMMDC1](https://www.orpha.net/en/disease/gene/TIMMDC1)
- [MedlinePlus Genetics — Mitochondrial complex I deficiency](https://medlineplus.gov/genetics/condition/mitochondrial-complex-i-deficiency/)
- [Timmdc1 MGI Mouse Gene Detail — MGI:1922139](https://www.informatics.jax.org/marker/MGI:1922139)
- [FlyBase Gene Report — Dmel\Timmdc1](https://flybase.org/reports/FBgn0010340)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

4 of 5 references resolved; the rest could not be looked up either way.