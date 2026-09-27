---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-21T12:44:19.468598'
end_time: '2026-08-21T12:48:44.296315'
duration_seconds: 264.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 14B, Autosomal Recessive
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
  web_search_requests: 14
  num_turns: 21
  total_cost_usd: 1.9681664
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 15
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 14B, Autosomal Recessive
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 14B, Autosomal Recessive** covering all of the
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

I'll research this disorder now, starting by loading web search tools and querying for authoritative sources on Immunodeficiency 14B, Autosomal Recessive (PIK3CD-related).

I have gathered sufficient authoritative data (OMIM #619281, the Swan et al. 2019 Haematologica founding report, PI3K pathway biology, and related literature). I'll now compile the comprehensive research report.

I now have sufficient depth to produce the comprehensive report. Here it is.

This confirms the mutation spectrum (Q116*, I899del, V552Sfs*26, Q721* across the described families). I now have enough verified material to write the full report.

---

# Immunodeficiency 14B, Autosomal Recessive (IMD14B) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Immunodeficiency 14B, Autosomal Recessive (IMD14B) is a rare inborn error of immunity caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *PIK3CD***, the gene encoding the p110δ catalytic subunit of class IA phosphoinositide 3-kinase (PI3Kδ). It is the recessive, loss-of-function counterpart of the much more extensively characterized **autosomal dominant gain-of-function PIK3CD disorder, Activated PI3K-delta Syndrome 1 (APDS1 / IMD14A, OMIM #615513)** — the same gene, opposite direction of dysregulation, and a substantially different clinical picture. Whereas APDS1 (heterozygous activating variants) causes a combined immunodeficiency with lymphoproliferation and hyperactive PI3Kδ signaling, IMD14B (biallelic loss-of-function variants) produces **PI3Kδ deficiency/haploinsufficiency-below-threshold**, presenting mainly with humoral immunodeficiency, defective cytotoxic lymphocyte function, and autoimmune/autoinflammatory features including autoimmune thrombocytopenia and enterocolitis.

**Key identifiers:**
- **OMIM:** #619281 — "IMMUNODEFICIENCY 14B, AUTOSOMAL RECESSIVE; IMD14B" (gene-disease relationship curated at OMIM *602839, PIK3CD)
- **Related/contrasted entries:** OMIM #615513 (IMD14A, autosomal dominant, same gene, GOF); OMIM #616005 (IMD36/APDS2, PIK3R1, AD); ClinGen gene-disease validity record SGC-104693.2 (PIK3CD, autosomal recessive)
- **Gene:** *PIK3CD* (HGNC:8977), chromosome 1p36.22
- **MONDO ID:** not directly located in this search session — recommend cross-checking the MONDO term server directly before curation (candidate: a MONDO term mapping to OMIM:619281)
- **Suggested MONDO/Mondo cross-ref:** should resolve via OMIM 619281 xref
- **Inheritance:** Autosomal recessive
- **Category:** Inborn error of immunity — predominantly antibody deficiency / combined immunodeficiency with immune dysregulation (IUIS classification)

**Synonyms/alternative names:** Autosomal recessive PI3Kδ deficiency; PIK3CD deficiency (loss-of-function type); p110δ deficiency; PI3K-delta underactivation; biallelic PIK3CD deficiency. Should not be confused with "PIK3CD deficiency" used loosely in some older literature to mean APDS1 (gain-of-function).

**Evidence basis:** This entry is derived almost entirely from **aggregated case-series/case-report literature** (family and cohort reports of small numbers of patients, typically from consanguineous kindreds), not large-cohort EHR/registry data — reflecting genuine disease rarity. As of the founding 2019 report only ~9 patients from 6 families had been described with germline biallelic PI3Kδ-pathway loss-of-function; a further multi-sibling family was reported in 2025.

Sources: [OMIM #619281](https://www.omim.org/entry/619281), [OMIM #615513 (IMD14A)](https://www.omim.org/entry/615513), [ClinGen SGC-104693.2](https://thegencc.org/submissions/SGC-104693.2), [PMC6886442 (Swan et al. 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/)

---

## 2. Etiology

### Disease Causal Factors
IMD14B is a **monogenic, purely genetic** disorder. Disease requires **biallelic loss-of-function (LOF)** variants in *PIK3CD* — i.e., both alleles carry null or severely hypomorphic mutations, consistent with autosomal recessive Mendelian inheritance. This is mechanistically the inverse lesion from APDS1: APDS1 variants (e.g., E1021K, the classic "hotspot") **increase** PI3Kδ lipid-kinase activity (gain-of-function, dominant), while IMD14B variants **abolish or severely reduce** p110δ protein expression or catalytic function (loss-of-function, recessive — a single functional allele is sufficient for near-normal PI3Kδ signaling, consistent with autosomal recessive rather than dominant-negative behavior at the heterozygous carrier level).

### Genetic Risk Factors
- **Causal variants:** Biallelic (homozygous or compound heterozygous) null/hypomorphic *PIK3CD* alleles. Reported variant types across the described families include:
  - **c.703_723delinsGT** (exon 5), producing a frameshift and premature stop codon **p.Q170Vfs*41**, resulting in absent full-length p110δ protein — the index case in the Swan et al. 2019 Haematologica report (homozygous, from consanguineous parents)
  - Nonsense variants: **Q116*, Q721***
  - Frameshift: **V552Sfs*26**
  - In-frame deletion: **I899del**
  (These four — Q116*, I899del, V552Sfs*26, Q721* — represent the mutation spectrum reported across the original 6-family cohort of biallelic PI3Kδ-pathway LOF cases.)
- **Consanguinity is strongly overrepresented** among reported families, consistent with the rarity of biallelic LOF alleles at population frequency and typical of autosomal recessive Mendelian disease ascertainment.
- **Population allele frequency / constraint:** *PIK3CD* is a gene with population-level constraint against loss-of-function variation in gnomAD (constraint metrics — pLI/LOEUF — were not independently retrieved in this session and should be pulled directly from gnomAD before finalizing a KB entry, but the extreme rarity of reported biallelic-null patients is consistent with a haploinsufficient/constrained gene where homozygous null genotypes are strongly selected against or embryonic-lethal-adjacent in some genetic backgrounds).
- **Modifier/digenic context:** At least one report describes a patient with **concomitant partial defects in PIK3CD and RAB27A** (two hypomorphic genetic lesions) that together predisposed to hemophagocytic lymphohistiocytosis (HLH) upon viral challenge — illustrating that partial (hypomorphic, not fully null) PI3Kδ pathway dysfunction can act as a genetic modifier/second hit rather than causing IMD14B outright on its own (Ghosh et al., *J Exp Med* 2018, "Concomitant PIK3CD and TNFRSF9 deficiencies cause chronic active Epstein-Barr virus infection of T cells" — note: this specific title concerns TNFRSF9, and a related HLH/RAB27A digenic report was also identified in search but not independently verified in this session; treat as a lead requiring primary-source confirmation before citation).

### Environmental Risk Factors
None established as causal — this is a purely monogenic disorder. However, as with other primary antibody/cytotoxic immunodeficiencies, **infectious triggers** (particularly EBV and CMV) appear to precipitate or exacerbate the clinical phenotype in affected patients (CMV viremia and gut CMV replication were documented in the index Swan et al. case; norovirus and post-transplant HSV were also noted), consistent with the known role of PI3Kδ in cytotoxic lymphocyte (CD8+ T cell, NK cell) antiviral function.

### Protective Factors
None specifically established. By analogy to other antibody-deficiency PIDs, timely diagnosis enabling immunoglobulin replacement and prophylactic antimicrobials likely reduces infection-related morbidity, but this has not been formally studied as a "protective factor" in IMD14B specifically.

### Gene-Environment Interactions
The core biological interaction is **infection as a functional stress-test of an already-deficient cytotoxic/humoral immune system** — e.g., CMV/EBV exposure unmasking failure of PI3Kδ-dependent CD8+ T-cell and NK-cell cytotoxic effector function, and gut viral/bacterial exposure precipitating the enterocolitis phenotype in a background of PI3Kδ-dependent epithelial/mucosal immune dysregulation.

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), [PMC6082933 (CD8+ T cell PI3Kδ)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6082933/), [JEM: Concomitant PIK3CD and TNFRSF9 deficiencies](https://rupress.org/jem/article/216/12/2800/132533/)

---

## 3. Phenotypes

Reported cases converge on a triad of **recurrent infection, humoral immunodeficiency, and autoimmune/autoinflammatory gut and hematologic disease** — clinically distinct from the lymphoproliferative, herpesvirus-viremic phenotype of APDS1 (gain-of-function).

| Phenotype | Type | Onset | Severity/Course | Suggested HP term |
|---|---|---|---|---|
| Recurrent sinopulmonary/respiratory infections | Symptom/clinical sign | Early childhood | Variable; some patients had severe pneumonia | HP:0002205 (Recurrent respiratory infections) |
| Hypogammaglobulinemia | Laboratory abnormality | Childhood | Reported as IgG 2.5 g/L, IgM 0.25 g/L in the index case | HP:0004313 (Hypogammaglobulinemia) |
| Decreased/absent class-switched memory B cells | Laboratory abnormality | — | — | HP:0005361 or a B-cell subset abnormality term (candidate: HP:0010976, Decreased proportion of memory B cells) |
| Low-normal circulating B-cell numbers | Laboratory abnormality | — | — | HP:0010976 / HP:0012183 (B lymphocytopenia) — verify exact term with OAK before curating |
| Inflammatory bowel disease / enterocolitis | Clinical sign | Childhood | Can be intractable — index case had ~30% body weight loss from diarrhea; histology showed crypt epithelial apoptosis, eosinophil/neutrophil infiltration, crypt abscesses | HP:0002037 (Inflammatory abnormality of the intestine) / HP:0100280 (IBD) |
| Autoimmune (immune-mediated) thrombocytopenia | Clinical sign, hematologic | Childhood | Refractory to corticosteroids, IVIG, and splenectomy in the index case; complicated by intracranial hemorrhage requiring neurosurgical evacuation | HP:0001973 (Autoimmune thrombocytopenia) |
| Osteomyelitis | Clinical sign | Childhood | Reported in a subset of patients | HP:0002754 (Osteomyelitis) |
| Impaired cell-mediated cytotoxicity | Laboratory/functional abnormality | — | Affects NK and CD8+ T-cell killing | HP:0025387 (Impaired natural killer cell cytotoxicity) or related |
| Defective T-cell function | Laboratory abnormality | — | Normal T-cell *numbers* but functionally impaired | HP:0002647 or a T-cell dysfunction term |
| CMV/EBV susceptibility | Clinical sign, infectious | — | CMV gut viremia documented in index case | HP:0032101 or general viral-susceptibility term |
| Skewed CD8+ effector/memory T-cell compartment | Laboratory abnormality | — | Elevated TBET and perforin expression reported | (candidate GO/CL-level annotation rather than HP)

**Frequency caveat:** because the disease has been described in only a handful of families, formal frequency bands (FREQUENT/OCCASIONAL) cannot be assigned from large-cohort statistics; per dismech evidence discipline, frequency claims for this entry should either be omitted or explicitly qualified as derived from a small case series (n≈9–15 patients across all published reports as of this research).

**Quality of life impact:** Not formally studied with validated instruments (EQ-5D/SF-36) in this ultra-rare population; qualitatively, the index case required repeated hospitalizations, splenectomy, neurosurgical intervention for intracranial hemorrhage, and ultimately curative HSCT — indicating substantial morbidity in severe presentations.

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), [OMIM #619281 search summary](https://www.omim.org/entry/619281)

---

## 4. Genetic/Molecular Information

**Causal gene:** *PIK3CD* (HGNC:8977; OMIM *602839), chromosome 1p36.22, encoding **p110δ**, the catalytic subunit of class IA phosphoinositide 3-kinase delta (PI3Kδ). p110δ binds the p85 regulatory subunit (encoded by *PIK3R1*) to form the heterodimeric PI3Kδ enzyme, which phosphorylates PIP2 to PIP3 downstream of antigen and cytokine receptors, driving AKT/mTOR pathway activation.

**Pathogenic variant classes described in IMD14B (loss-of-function, biallelic):**
- Nonsense: **c.[346C>T] p.Gln116*** (Q116*); **p.Gln721*** (Q721*)
- Frameshift: **c.703_723delinsGT, p.Gln170Valfs*41** (Q170Vfs*41); **p.Val552Serfs*26** (V552Sfs*26)
- In-frame deletion: **p.Ile899del** (I899del)

All produce **complete or near-complete loss of p110δ protein expression or catalytic function** when biallelic. Zygosity in reported cases is predominantly **homozygous**, reflecting consanguinity in the ascertained families; compound heterozygosity is also biologically plausible and consistent with autosomal recessive inheritance.

**Functional consequences (mechanistic, patient-derived cell data):**
- Patient T lymphoblasts show **profoundly impaired PIP3 generation** upon T-cell receptor (TCR) engagement
- **Reduced AKT and mTOR phosphorylation**
- **Impaired glycolysis and glycolytic reserve** in activated T cells
- The functional phenotype of patient cells **parallels pharmacologic PI3Kδ inhibition** (e.g., idelalisib) in healthy donor cells — i.e., the genetic lesion phenocopies chemical PI3Kδ blockade
- Absent full-length p110δ protein on Western blot in the index frameshift case

**Contrast with APDS1 (gain-of-function, same gene):** APDS1 variants (classic hotspot E1021K, and others such as E525K) enhance membrane recruitment/kinase activity of p110δ, causing constitutively elevated PIP3/AKT/mTOR signaling, T-cell senescence, and impaired B-cell class-switching from *hyperactivity*, whereas IMD14B produces the same downstream signaling defect (impaired terminal effector output) via the opposite biochemical mechanism (absence rather than excess of activity) — both converge on defective adaptive antiviral immunity and B-cell dysfunction, but with very different accompanying phenotypes (lymphoproliferation/herpesvirus viremia in APDS1 vs. autoimmune cytopenia/enterocolitis in IMD14B).

**Variant frequency/pathogenicity resources:** ClinVar and gnomAD should be queried directly per-variant during curation; this session did not retrieve specific gnomAD allele frequency or pLI/LOEUF constraint values for *PIK3CD* and these should be sourced from gnomad.broadinstitute.org before finalizing KB entries.

**Modifier genes:** Digenic/oligogenic modulation has been reported — concomitant hypomorphic defects in a second gene (e.g., in the setting of HLH-susceptibility or chronic active EBV) appear to potentiate the phenotype of partial PI3Kδ pathway dysfunction; this should be flagged in the entry as a `MODIFIER`/`COOPERATING` relationship_type rather than curated as the primary causal mechanism.

**Epigenetic/chromosomal information:** No epigenetic mechanism or chromosomal-abnormality mechanism has been reported for IMD14B; this is a classic biallelic small-variant Mendelian disorder.

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), [OMIM *602839](https://www.omim.org/entry/602839), [Nature Immunology — activating PIK3CD variants, T-cell senescence](https://www.nature.com/articles/ni.2771)

---

## 5. Environmental Information

No non-genetic environmental, lifestyle, or occupational factors have been described as causal for IMD14B — it is a Mendelian monogenic disease. The only environmental modulators identified in the literature are **infectious triggers** (CMV, EBV, norovirus, HSV) that precipitate or exacerbate clinical episodes against the background of underlying immune deficiency, rather than acting as disease-initiating exposures.

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/)

---

## 6. Mechanism / Pathophysiology

### Causal chain (proposed for pathograph modeling)

1. **Trigger:** Biallelic loss-of-function *PIK3CD* variant (nonsense/frameshift/in-frame deletion) →
2. **Molecular:** Absent or non-functional p110δ catalytic subunit protein → failure to form functional PI3Kδ heterodimer with p85 (PIK3R1) →
3. **Molecular:** Loss of PIP2→PIP3 conversion upon antigen receptor (BCR/TCR) and cytokine receptor engagement →
4. **Molecular:** Failure of AKT and mTORC1 (and downstream S6/4E-BP1) phosphorylation cascade →
5. **Cellular:** Impaired T-cell and B-cell activation-induced metabolic reprogramming (reduced glycolysis/glycolytic reserve) →
6. **Cellular:** Defective B-cell development, survival, and class-switch recombination → hypogammaglobulinemia, reduced class-switched memory B cells →
7. **Cellular:** Defective cytotoxic effector differentiation/function in CD8+ T cells and NK cells → impaired viral clearance (CMV, EBV) →
8. **Organismal:** Recurrent infections (sinopulmonary, opportunistic) →
9. **Parallel branch — immune dysregulation:** Loss of a normally PI3Kδ-dependent regulatory/tolerogenic checkpoint (mechanism less well defined than the infection-susceptibility arm) → breakdown of peripheral tolerance → autoimmune thrombocytopenia, enterocolitis (with crypt epithelial apoptosis, eosinophil/neutrophil infiltration) →
10. **Organismal:** Multisystem disease — hematologic (bleeding, intracranial hemorrhage), gastrointestinal (malnutrition, weight loss), skeletal (osteomyelitis) complications

### Suggested ontology terms for pathograph nodes
- **Molecular function:** GO:0004430 (1-phosphatidylinositol 4-kinase activity) / more precisely the phosphatidylinositol-4,5-bisphosphate 3-kinase activity term (GO:0035005, phosphatidylinositol-4,5-bisphosphate 3-kinase activity) — verify exact GO ID/label via OAK before curating
- **Biological process:** GO:0043491 (protein kinase B signaling / AKT signaling), GO:0038202 (TORC1 signaling), GO:0050853 (B cell receptor signaling pathway), GO:0050852 (T cell receptor signaling pathway), GO:0002250 (adaptive immune response)
- **Cell types (CL):** CL:0000236 (B cell), CL:0000818 (memory B cell / class-switched memory B cell subtype), CL:0000625 (CD8-positive, alpha-beta T cell), CL:0000623 (natural killer cell), CL:0000897 (CD4-positive, alpha-beta memory T cell)
- **Protein dysfunction category:** loss of function (p110δ absent/non-functional) — use `functional_impact_category: LOSS_OF_FUNCTION` per the dismech GeneticContext slot guidance, contrasting with the `GAIN_OF_FUNCTION` classification used for the allelic APDS1 disorder

### Molecular profiling
No transcriptomic, proteomic, or single-cell atlas dataset specific to IMD14B was identified in this research session (unlike APDS1, which has been studied with bulk and single-cell approaches). Functional characterization has relied on **patient-derived primary lymphocyte assays** (PIP3 flux by flow cytometry, phospho-AKT/phospho-S6 immunoblotting, Seahorse extracellular flux glycolysis assays) rather than omics datasets.

### Tissue damage / immune dysregulation mechanisms
Gut histopathology in the index case showed **crypt epithelial apoptosis, eosinophil and neutrophil infiltration, and crypt abscess formation** — consistent with an inflammatory bowel disease-like process superimposed on immunodeficiency, analogous mechanistically to other monogenic very-early-onset IBD (VEO-IBD) syndromes with primary immunodeficiency etiology.

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), [PMC6082933](https://pmc.ncbi.nlm.nih.gov/articles/PMC6082933/), [JACI review — PI3K pathway defects](https://www.jacionline.org/article/S0091-6749(19)30421-X/fulltext)

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Immune system broadly — lymphoid organs (spleen — splenectomy performed in index case; bone marrow — site of B-cell development); gastrointestinal tract (small/large intestine — enterocolitis); respiratory tract (lungs — recurrent pneumonia); skeletal system (bone — osteomyelitis); central nervous system (secondary — intracranial hemorrhage as a complication of severe thrombocytopenia, not a primary target organ)
- **Body systems:** Hematologic/immune system (primary), digestive system, respiratory system, skeletal system, secondarily nervous system (hemorrhagic complication)
- **UBERON candidates:** UBERON:0002106 (spleen), UBERON:0002371 (bone marrow), UBERON:0002108 (small intestine), UBERON:0002106, UBERON:0002048 (lung)
- **Tissue/cell level:** Lymphoid tissue — B lymphocytes (bone marrow and peripheral development), T lymphocytes (thymic/peripheral), NK cells; intestinal crypt epithelium (site of apoptosis/damage in enterocolitis)
- **Subcellular level:** Plasma membrane (site of PI3Kδ lipid kinase activity and PIP3 generation upon receptor engagement); cytoplasm (AKT/mTOR signaling cascade) — GO Cellular Component candidates: GO:0005886 (plasma membrane), GO:0005942 (phosphatidylinositol 3-kinase complex, class IA)
- **Localization/laterality:** Not applicable — systemic/multisystem disease, not laterality-specific

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/)

---

## 8. Temporal Development

- **Onset:** Early childhood (recurrent infections typically the presenting feature); the index HSCT case was diagnosed/treated by age 9
- **Onset pattern:** Chronic with acute exacerbations (infectious episodes, thrombocytopenic crises, IBD flares)
- **Progression:** Can be progressive and life-threatening without intervention — the index case progressed to refractory autoimmune thrombocytopenia complicated by intracranial hemorrhage requiring surgical evacuation, and intractable enterocolitis causing ~30% weight loss, ultimately requiring curative allogeneic HSCT
- **Disease course pattern:** Chronic, with episodic/relapsing autoimmune manifestations (thrombocytopenia refractory to first-line therapies) superimposed on a baseline of chronic humoral immunodeficiency
- **Duration:** Chronic/lifelong unless treated definitively (HSCT reported curative in at least one case, achieving 100% donor chimerism after a second transplant with myeloablative conditioning)
- **Remission patterns:** Spontaneous remission not described; disease was treatment (HSCT)-induced remission/cure in the reported case
- **Critical periods:** Early recognition appears critical given the severity of complications (intracranial hemorrhage) that can occur if autoimmune thrombocytopenia is not adequately controlled

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/)

---

## 9. Inheritance and Population

- **Epidemiology:** Extremely rare — as of the founding literature (Swan et al. 2019), only **9 patients from 6 families** had been reported with germline biallelic PI3Kδ-pathway loss-of-function causing this phenotype; a further family with multiple affected siblings was reported in 2025 (Journal of Clinical Immunology). No formal population prevalence/incidence estimate exists; this contrasts with APDS1/APDS2 (gain-of-function), for which >200–250 patients have been reported and an early prevalence estimate of ~1 in 1,000,000 live births was proposed (likely an underestimate given limited genetic screening) — no comparable prevalence estimate is available for the recessive LOF disorder given its still smaller reported case count.
- **Inheritance pattern:** Autosomal recessive (biallelic — homozygous or compound heterozygous)
- **Penetrance:** Appears to be high/complete in reported homozygous null cases, though the small number of reported families limits confident penetrance estimation
- **Expressivity:** Variable — reported patients range from severe multisystem disease (the index HSCT case) to milder presentations dominated by recurrent infection and hypogammaglobulinemia without necessarily manifesting the severe autoimmune/enterocolitis phenotype
- **Consanguinity:** Strongly overrepresented among reported families — most/all published pedigrees involve consanguineous unions, consistent with autosomal recessive disease requiring biallelic rare LOF alleles
- **Founder effects:** Not specifically documented; variants reported to date appear to be private/family-specific (e.g., the c.703_723delinsGT frameshift was described as a "private homozygous frameshift variant")
- **Carrier frequency:** Not established; would require gnomAD-derived allele frequency data per specific variant (not retrieved in this session)
- **Affected populations / geographic distribution:** Not systematically characterized; reported families derive from multiple, geographically dispersed consanguineous kindreds rather than a single founder population
- **Sex ratio:** Not established as skewed — autosomal recessive inheritance predicts equal sex distribution, consistent with expectation for an autosomal (non-X-linked) gene

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), [Frontiers — Activated PI3Kinase Delta Syndrome, multifaceted disease](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2021.652405/full)

---

## 10. Diagnostics

### Clinical/laboratory tests
- **Immunoglobulin levels:** Quantitative IgG, IgA, IgM — hypogammaglobulinemia is a hallmark (index case IgG 2.5 g/L, IgM 0.25 g/L)
- **Lymphocyte immunophenotyping (flow cytometry):** B-cell enumeration (low-normal total B cells; markedly reduced/absent class-switched memory B cells [CD27+IgD-IgM-]); T-cell and NK-cell enumeration (typically normal numbers despite functional defects)
- **Functional PI3Kδ pathway assays (research/reference-lab level):** PIP3 generation assay upon BCR/TCR engagement; phospho-AKT and phospho-S6/phospho-mTOR flow cytometry or immunoblot following receptor stimulation — these directly demonstrate the loss-of-function biochemical defect
- **Metabolic functional assays:** Seahorse extracellular flux analysis showing impaired glycolysis/glycolytic reserve in activated lymphocytes
- **Viral load monitoring:** CMV and EBV PCR/viremia surveillance given documented susceptibility
- **Histopathology:** Intestinal biopsy in cases with enterocolitis — crypt epithelial apoptosis, eosinophil/neutrophil infiltration, crypt abscesses

### Genetic testing
- **Recommended approach:** Given the phenotypic overlap with other combined immunodeficiencies and antibody deficiencies, a **primary immunodeficiency gene panel** or **whole exome/genome sequencing** is the practical diagnostic approach, particularly given consanguinity (which favors homozygosity mapping/WES in an autosomal recessive framework)
- **Single-gene *PIK3CD* sequencing** is reasonable when the biochemical/functional phenotype (impaired PI3Kδ signaling by flow-cytometric PIP3/pAKT assay) already points to the PI3Kδ pathway
- **Chromosomal microarray/karyotype:** Not indicated as a primary diagnostic tool — this is a small-variant (not structural) disorder
- No specific mention of newborn screening applicability was identified (TREC-based SCID newborn screening would not reliably detect this humoral/cytotoxic-predominant phenotype, since T-cell numbers are typically normal)

### Clinical criteria / differential diagnosis
Differential diagnosis should include:
- **APDS1** (heterozygous gain-of-function PIK3CD) and **APDS2** (PIK3R1) — distinguished by inheritance pattern (dominant vs. recessive), lymphoproliferation/splenomegaly and chronic herpesvirus viremia (more typical of APDS), and opposite functional PI3Kδ assay results (hyperactive vs. hypoactive signaling)
- Common variable immunodeficiency (CVID) and other predominantly antibody deficiencies
- Very-early-onset inflammatory bowel disease (VEO-IBD) monogenic causes
- Other causes of autoimmune cytopenia with immunodeficiency (ALPS, CTLA4 haploinsufficiency, LRBA deficiency)

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), [JACI PI3K pathway review](https://www.jacionline.org/article/S0091-6749(19)30421-X/fulltext)

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal survival statistics exist given the extremely small reported case numbers; the index case's course (refractory thrombocytopenia, intracranial hemorrhage, severe enterocolitis with major weight loss, opportunistic infection) illustrates that the disease can be **life-threatening without definitive treatment**
- **Curative option:** **Allogeneic hematopoietic stem cell transplantation (HSCT)** was reported curative in the index case, achieving 100% donor chimerism after a second (myeloablative) transplant — directly paralleling the curative role HSCT plays in APDS1/APDS2 for patients with life-threatening complications
- **Morbidity:** Substantial in severe cases — intracranial hemorrhage requiring neurosurgical evacuation, splenectomy, malnutrition from intractable diarrhea, recurrent severe infections (pneumonia, CMV viremia, norovirus, post-transplant HSV)
- **Prognostic factors:** Severity appears to correlate with degree of p110δ loss (complete absence of protein in the frameshift/nonsense cases) and the presence of refractory autoimmune complications; earlier recognition and treatment (immunoglobulin replacement, prophylaxis, and timely consideration of HSCT for severe/refractory cases) likely improves outcomes, by analogy with APDS management paradigms

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/)

---

## 12. Treatment

### Pharmacotherapy
- **Immunoglobulin replacement therapy (IVIG/SCIG):** Standard supportive treatment for the hypogammaglobulinemia component, as used across PI3Kδ pathway disorders — NCIT candidate term: NCIT:C15986 (Pharmacotherapy) with therapeutic_agent bound to immunoglobulin product classes
- **Antibiotic/antimicrobial prophylaxis:** Standard supportive measure for recurrent infection risk
- **Immunosuppressive therapy:** Used for autoimmune thrombocytopenia (corticosteroids reported, though refractory in the index case) — NCIT:C15986 with an appropriate corticosteroid therapeutic_agent
- Note: unlike APDS1 (gain-of-function), where **sirolimus/rapamycin (mTOR inhibition)** and selective PI3Kδ **inhibitors** (e.g., leniolisib) are mechanistically rational targeted therapies, these agents would be **mechanistically inappropriate or contraindicated** in the loss-of-function IMD14B disorder, since further inhibiting an already-deficient pathway would be expected to worsen, not improve, the immunodeficiency. This is an important curation distinction — do not apply APDS1/APDS2 targeted-therapy `target_mechanisms` patterns to IMD14B entries.

### Surgical/Interventional
- **Splenectomy** — was attempted (unsuccessfully) for refractory autoimmune thrombocytopenia in the index case — NCIT:C15329 (Surgical Procedure) / a more specific splenectomy term if available
- **Neurosurgical evacuation of intracranial hemorrhage** — performed as an emergency intervention for the thrombocytopenia-related bleeding complication

### Advanced/curative therapeutics
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — curative in the reported index case (myeloablative conditioning, second transplant needed to achieve full donor chimerism) — NCIT:C15289 (Organ Transplantation) is the closest general term; a more specific HSCT-mapped NCIT code should be verified (candidate: NCIT:C15431, Hematopoietic Cell Transplantation)

### Supportive care
- Nutritional support given severe diarrhea/weight loss (~30% body weight loss documented) — NCIT:C15433/C15447-family terms as appropriate
- Antiviral management for CMV/EBV/HSV reactivation/infection

### Experimental / investigational
No disease-specific clinical trials (NCT-registered) for IMD14B were identified in this research session — reflecting the extreme rarity of the condition. Management is extrapolated largely from broader primary immunodeficiency and APDS-family treatment paradigms, adjusted for the opposite direction of the underlying molecular lesion.

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), [Frontiers — Activated PI3Kδ syndrome, diagnosis/treatment review](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1208567/full)

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic recessive disease) — the relevant preventive intervention is **genetic counseling and carrier/prenatal testing** for consanguineous families with a known proband, given the autosomal recessive inheritance pattern and demonstrated overrepresentation of consanguinity
- **Secondary prevention:** Early diagnosis via genetic testing in symptomatic infants/children with recurrent infection plus hypogammaglobulinemia, particularly from consanguineous unions, to enable early initiation of immunoglobulin replacement and infection prophylaxis before severe autoimmune/enterocolitis complications develop
- **Genetic counseling:** Recommended for families with an identified proband — recurrence risk 25% for future pregnancies in carrier x carrier matings, consistent with standard autosomal recessive counseling
- **Screening:** No population-level newborn screening protocol identified as applicable (TREC-based SCID screening would not detect this phenotype); targeted carrier screening would only be relevant in populations/families with a known pathogenic allele
- **Prophylaxis:** Antimicrobial and immunoglobulin prophylaxis, as discussed under Treatment, functions as tertiary/ongoing prevention of infectious complications once diagnosed

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/)

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/animal disease analog of biallelic PIK3CD loss-of-function was identified in this research session. This appears to be a human-specific reported condition to date (in contrast to some PIDs with described veterinary correlates).

---

## 15. Model Organisms

- **Mouse models:** *Pik3cd*-knockout and kinase-dead knock-in mice have been used extensively to study p110δ loss-of-function biology (largely in the context of dissecting normal PI3Kδ physiology and, separately, APDS-related gain-of-function models). Search results retrieved in this session confirmed active mouse-model literature on p110δ's role in B-cell development, survival, and germinal center reactions (e.g., B-cell-specific PIK3CD gain-of-function mouse models — Mb1-aPIK3CD — and p110δ-selective inhibitor studies in murine B cells), but a specific, disease-matched **loss-of-function *Pik3cd* knockout mouse phenocopying IMD14B** was not independently retrieved with full phenotypic detail in this session and should be sourced directly from MGI (Mouse Genome Informatics) before citing in a KB entry — historically, *Pik3cd* germline-null mice are known (from foundational PI3Kδ immunology literature predating this specific human disease description) to show **B-cell developmental block, reduced serum immunoglobulin, and impaired T-cell-dependent and -independent antibody responses**, consistent with a translatable phenotype, but this claim requires direct primary-source (PMID) verification before curation into a dismech entry (do not curate from this summary without confirming the source).
- **Functional cellular models:** Patient-derived primary T lymphoblasts and B cells (ex vivo, human) constitute the principal "model system" used to demonstrate the molecular loss-of-function phenotype (PIP3 generation assays, phospho-flow, Seahorse metabolic assays) — these are IN_VITRO human primary cell studies, not animal models, and should be tagged `evidence_source: IN_VITRO` accordingly if reused for the KB.
- **Resources for follow-up:** MGI (Mouse Genome Informatics) for *Pik3cd* allele records; IMPC (International Mouse Phenotyping Consortium) for any systematic *Pik3cd*-null phenotyping data.

Sources: [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/), search results on Mb1-aPIK3CD and p110δ B-cell biology (not independently fetched in full)

---

## Curation Notes and Flags for the dismech Entry

1. **Primary anchor reference:** Swan DJ, Aschenbrenner D, Lamb CA, et al. "Immunodeficiency, autoimmune thrombocytopenia and enterocolitis caused by autosomal recessive deficiency of PIK3CD-encoded phosphoinositide 3-kinase δ." *Haematologica* 2019. Full text at [PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/) — **fetch this via `just fetch-reference` and extract the exact PMID before writing any evidence snippet**; this report only had indirect access to the PMC full text and did not independently confirm the PMID number, which must be verified directly (e.g., via PubMed search for the exact title) rather than assumed.
2. **NEC risk:** This disease sits in a **numbered-series / gene-shared-eponym risk class** per the dismech NEC guidance — "Immunodeficiency 14A" (dominant, same gene, OMIM #615513) and "Immunodeficiency 14B" (recessive, same gene, OMIM #619281) are adjacent entries in the same phenotypic series, and **APDS1/APDS2/IMD36 literature vastly outnumbers IMD14B literature** in any generic "PIK3CD immunodeficiency" search. Run `just preflight-dr` against MONDO's causal-gene record for the correct MONDO ID once identified, and manually confirm any DR-tool output actually discusses **biallelic/homozygous loss-of-function** variants and **recessive** inheritance, not the far more common heterozygous gain-of-function APDS1 literature, before curating.
3. **MONDO ID not confirmed in this session** — must be resolved via MONDO/OMIM xref lookup (OMIM:619281) before curation.
4. Several claims flagged above ("should be verified," "not independently retrieved," "requires primary-source confirmation") are explicitly marked as **leads, not verified facts** — per the dismech evidence SOP, these must not be curated into `evidence:` blocks without independent PMID fetch and snippet verification via `just fetch-reference` / `just count-verified-snippets`.

---

## Sources

- [OMIM Entry #619281 — IMMUNODEFICIENCY 14B, AUTOSOMAL RECESSIVE](https://www.omim.org/entry/619281)
- [OMIM Entry #615513 — IMMUNODEFICIENCY 14A WITH LYMPHOPROLIFERATION, AUTOSOMAL DOMINANT](https://www.omim.org/entry/615513)
- [OMIM Entry *602839 — PIK3CD](https://www.omim.org/entry/602839)
- [ClinGen/GenCC submission SGC-104693.2 — PIK3CD, immunodeficiency 14b, autosomal recessive](https://thegencc.org/submissions/SGC-104693.2)
- [Swan et al., "Immunodeficiency, autoimmune thrombocytopenia and enterocolitis caused by autosomal recessive deficiency of PIK3CD-encoded phosphoinositide 3-kinase δ," Haematologica 2019 — PMC6886442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886442/)
- [Haematologica article page](https://haematologica.org/article/view/9105)
- [PI3K pathway defects leading to immunodeficiency and immune dysregulation, JACI 2019](https://www.jacionline.org/article/S0091-6749(19)30421-X/fulltext)
- [Genetic Defects in Phosphoinositide 3-Kinase δ Influence CD8+ T Cell Survival, Differentiation, and Function — PMC6082933](https://pmc.ncbi.nlm.nih.gov/articles/PMC6082933/)
- [Homozygous Loss of Function PIK3CD Mutation in Multiple Siblings Leading To B Cell Dysregulation and Autoimmunity, J Clin Immunol 2025](https://link.springer.com/article/10.1007/s10875-025-01938-3)
- [Concomitant PIK3CD and TNFRSF9 deficiencies cause chronic active Epstein-Barr virus infection of T cells, JEM 2019](https://rupress.org/jem/article/216/12/2800/132533/)
- [PIK3CD Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=PIK3CD)
- [Activated PI3Kδ syndrome – reviewing challenges in diagnosis and treatment, Frontiers 2023](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1208567/full)
- [Dominant-activating germline mutations in PIK3CD result in T cell senescence, Nat Immunol](https://www.nature.com/articles/ni.2771)
- [Orphanet: PIK3CD gene page](https://www.orpha.net/en/disease/gene/PIK3CD)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.