---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T14:20:04.316301'
end_time: '2026-08-27T14:25:53.172887'
duration_seconds: 348.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MMADHC-related Disorder of Cobalamin Metabolism, cblD Type
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
  web_search_requests: 19
  num_turns: 36
  total_cost_usd: 1.6026110000000002
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MMADHC-related Disorder of Cobalamin Metabolism, cblD Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MMADHC-related Disorder of Cobalamin Metabolism, cblD Type** covering all of the
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

I now have comprehensive information to compile the full research report.

# MMADHC-Related Disorder of Cobalamin Metabolism, cblD Type: Comprehensive Research Report

## 1. Disease Information

### Overview

MMADHC-related disorder of cobalamin (vitamin B12) metabolism — the **cblD complementation group** — is a rare, autosomal recessive inborn error of intracellular cobalamin metabolism caused by biallelic pathogenic variants in *MMADHC* (methylmalonic aciduria and homocystinuria type D protein, formerly *C2orf25*), located at chromosome 2q23.2. The MMADHC protein acts as a trafficking chaperone that operates at a branch point in the intracellular cobalamin pathway, directing cobalamin toward mitochondrial synthesis of adenosylcobalamin (AdoCbl, the cofactor for methylmalonyl-CoA mutase) and/or cytosolic synthesis of methylcobalamin (MeCbl, the cofactor for methionine synthase) (Coelho et al., 2008, PMID:[18385497](https://pubmed.ncbi.nlm.nih.gov/18385497/)).

Because MMADHC governs both branches of the pathway, its disruption is genotypically and clinically heterogeneous, producing **three distinct biochemical/clinical phenotypes** depending on where in the gene/protein the causal variants fall:

| Designation | Biochemistry | Deficient coenzyme |
|---|---|---|
| **cblD-combined** (classic cblD; MAHCD) | Combined methylmalonic aciduria + homocystinuria | AdoCbl **and** MeCbl |
| **cblD variant 1 (cblDv1)**, "cblD-HC" | Isolated homocystinuria | MeCbl only |
| **cblD variant 2 (cblDv2)**, "cblD-MMA" | Isolated methylmalonic aciduria | AdoCbl only |

("Bäumgartner MR, Fowler B" clinic group first characterized these subtypes; Coelho et al. 2008.)

### Key Identifiers

- **Gene:** *MMADHC* (HGNC:26275), previously *C2orf25*
- **OMIM gene:** *611935 (METABOLISM OF COBALAMIN ASSOCIATED D; MMADHC)
- **OMIM phenotypes:**
  - **#277410** — Methylmalonic aciduria and homocystinuria, cblD type (MAHCD) — the combined/classic form
  - **#620952** — Homocystinuria-megaloblastic anemia, cblD type (HMAD) — corresponds to cblDv1 (recently split out as its own phenotypic entry, last major OMIM update ~September 2024)
  - **#620953** — Methylmalonic aciduria, cblD type (MACD) — corresponds to cblDv2 (also split out ~2024)
- **Orphanet:** ORPHA:79283 (Methylmalonic acidemia with homocystinuria, type cblD) — grouped under the broader Orphanet entries for methylmalonic acidemia with homocystinuria (ORPHA:26) and homocystinuria without methylmalonic aciduria
- **NCBI Entrez Gene ID:** 27249; **Ensembl:** ENSG00000168288; **UniProt:** Q9H3L0; **RefSeq mRNA:** NM_015702
- **PDB structures:** 5CUZ, 5CV0 (C-terminal domain, human CblD), 5A4R
- **UMLS:** C1848552 ("Methylmalonic aciduria and homocystinuria type cblD")

### Common Synonyms / Alternative Names

- Cobalamin D deficiency; cblD disease/defect
- MMADHC deficiency
- Methylmalonic aciduria and homocystinuria, cblD type (MAHCD)
- Combined methylmalonic aciduria and homocystinuria, cblD type
- Homocystinuria-megaloblastic anemia, cblD type (HMAD) — isolated homocystinuria subtype
- Isolated methylmalonic aciduria, cblD type (MACD) — isolated MMA subtype

### Evidence Basis

Because fewer than 20 patients have ever been reported worldwide, essentially **all available data derive from individual case reports and small case series** (patient-level clinical, biochemical, fibroblast, and molecular data) rather than aggregated registries, epidemiological surveys, or large disease-level databases. GeneReviews (NCBI Bookshelf NBK1328, "Disorders of Intracellular Cobalamin Metabolism") is the closest thing to an aggregated clinical-management resource, itself synthesized from the case literature.

---

## 2. Etiology

### Disease Causal Factors

cblD disease is **purely monogenic**: biallelic (homozygous or compound heterozygous) loss-of-function or partial loss-of-function variants in *MMADHC* are necessary and sufficient to cause disease. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause. Maternal cobalamin deficiency and other acquired B12 disorders are phenocopies, not causes of the genetic disease, and must be distinguished diagnostically.

### Genetic Risk Factors

- **Causal variants:** Missense, nonsense, frameshift, and splice-site variants across the 8 exons (18 kb genomic span) of *MMADHC*. Founder or recurrent variants are not well established given the extreme rarity and small number of reported kindreds; most published cases represent private (family-specific) variants (Coelho et al. 2008; Miousse et al. 2009, PMID:[19058814](https://pubmed.ncbi.nlm.nih.gov/19058814/)).
- **Genotype-phenotype correlation (domain mapping):** A structure-function study (Jusufi et al., 2014, *J Inherit Metab Dis*, PMID:[24722857](https://pubmed.ncbi.nlm.nih.gov/24722857/)) refined the domain boundaries governing which biochemical phenotype results:
  > "null mutations N-terminal to Met116 cause isolated methylmalonic aciduria (cblD-MMA) due to AdoCbl deficiency; ... null mutations across the C-terminus (p.Y140-R250) cause combined methylmalonic aciduria and homocystinuria (cblD-MMA/HC) due to AdoCbl and MeCbl deficiency; ... missense mutations in a conserved C-terminal region (p.D246-L259) cause isolated homocystinuria (cblD-HC) due to MeCbl deficiency."

  This is a clean example of an **allelic series** producing three phenotypes from one locus, driven by variant location/type rather than variant "severity" per se — a hypomorphic missense change in a narrow C-terminal region selectively knocks out the MeCbl-synthesis function while sparing AdoCbl synthesis, whereas a truncating variant upstream removes both.

- **Consanguinity:** Given the autosomal recessive inheritance and extreme rarity, consanguinity increases risk in affected families, as is typical of ultra-rare AR conditions, though no systematic consanguinity data specific to cblD have been published.
- **Modifier genes:** None specifically documented for cblD. In principle, variation in interacting partners (*MMACHC*, *MTR*, *MTRR*, *MUT*, *ABCD4*, *LMBRD1*) could theoretically modify severity, but this has not been studied.

### Protective Factors

None specific to cblD are documented in the literature (genetic or environmental). Adequate dietary/parenteral cobalamin supply is supportive rather than a true "protective" factor against the underlying genetic lesion, since the defect is in intracellular processing rather than absorption or intake.

### Gene-Environment Interactions

Not applicable in the classic sense (no known environmental exposure modifies penetrance). However, an important pharmacologic interaction exists: **nitrous oxide anesthesia irreversibly oxidizes cobalamin and inhibits methionine synthase**, and is specifically contraindicated in cblD (and all cobalamin-remethylation disorders) because it can precipitate acute decompensation on a background of already-reduced MeCbl availability (GeneReviews NBK1328).

---

## 3. Phenotypes

### cblD-Combined (Classic/MAHCD) — Laboratory and Clinical Features

- **Laboratory abnormalities:**
  - Elevated urinary methylmalonic acid (MMA), reported as high as >1,000 mmol/mol creatinine in some cases
  - Elevated total plasma homocysteine (tHcy), >100 µmol/L in some patients
  - Low-to-normal plasma methionine
  - Megaloblastic anemia (macrocytic red cells, hypersegmented neutrophils)
  - Serum B12 typically normal (this is a cellular processing defect, not a B12 deficiency/absorption defect)
- **Signs/symptoms:** poor feeding, failure to thrive/slow growth, hypotonia, developmental delay, encephalopathy, seizures (including infantile spasms in severe cases); GeneReviews notes "untreated infants may have multiorgan involvement, neurologic deterioration, seizures ... and encephalopathy."
- **Onset:** infancy to early childhood in most reported cases, though teenage-onset has also been described.

### cblD Variant 1 (cblDv1 / HMAD) — Isolated Homocystinuria

- **Laboratory:** elevated tHcy (>100 µmol/L in some), low-normal methionine, **normal urinary/serum MMA**, megaloblastic anemia.
- **Signs/symptoms** (per OMIM #620952 and case literature): developmental delay, impaired gross motor skills, dystonia or spastic ataxia, poor speech, nystagmus, poor eye contact, hypotonia, seizures, cerebral or cerebellar atrophy on neuroimaging. Thromboembolic complications (thrombophilia), hemolytic uremic syndrome (HUS)-like microangiopathy, and pulmonary hypertension have also been reported — mirroring the vascular/renal complications well described in the related cblC disorder.
- A detailed single-case report (Atkinson et al. 2014, *JIMD Reports*, PMID:[25155779](https://pubmed.ncbi.nlm.nih.gov/25155779/)) — described as only the **seventh documented cblD-HC case** at the time — details clinical, biochemical, and molecular findings and probable shared ancestry with other reported cases, underscoring how few patients exist worldwide.

### cblD Variant 2 (cblDv2 / MACD) — Isolated Methylmalonic Aciduria

- **Laboratory:** elevated urinary/plasma MMA, **normal tHcy and methionine**.
- **Signs/symptoms** (per OMIM #620953): may present in infancy with severe features including respiratory distress syndrome, intracranial hemorrhage, seizures, and ketotic coma/metabolic decompensation — a presentation resembling other isolated (AdoCbl-pathway) methylmalonic acidemias such as cblA/cblB.

### Phenotype Onset/Progression Characteristics

- **Age of onset:** neonatal to late childhood, with most cases in infancy/early childhood; adolescent-onset reported.
- **Severity:** highly variable, from severe neonatal metabolic decompensation to milder, later-onset neurologic presentations.
- **Progression:** progressive if untreated (neurologic deterioration, cerebral/cerebellar atrophy); stabilizes or improves substantially with early hydroxocobalamin-based treatment, though some deficits (structural CNS changes) may be irreversible if treatment is delayed.
- **Frequency of specific features:** Precise percentages are not calculable given only ~17 total published cases (see Epidemiology, Section 9), but developmental delay, megaloblastic anemia (in the Hcy-affected forms), and neurologic signs are near-universal in symptomatic patients; nystagmus, seizures, and hypotonia are variably reported.

### Quality of Life Impact

No disease-specific EQ-5D/SF-36/QOL instrument data exist for cblD given its extreme rarity; QOL burden is inferred from the underlying neurologic, hematologic, and (in cblDv2-type presentations) acute metabolic morbidity, analogous to related cobalamin remethylation/methylmalonic acidemia disorders — developmental delay, motor impairment, seizures, and (in the homocystinuria-predominant forms) risk of thromboembolic and renal/vascular complications all materially affect daily functioning.

### Suggested HPO Terms

- HP:0001513 Obesity — N/A (not relevant)
- HP:0001263 Global developmental delay
- HP:0001622 Premature birth (not typical; omit unless documented)
- HP:0002133 Status epilepticus / HP:0001250 Seizure
- HP:0000639 Nystagmus
- HP:0001272 Cerebellar atrophy
- HP:0002500 Basal ganglia lesions (per related cobalamin remethylation disorders)
- HP:0001939 Abnormality of metabolism/homeostasis (general)
- HP:0003119 Abnormal circulating homocysteine concentration → HP:0003081 Hyperhomocystinemia
- HP:0003201 Methylmalonic aciduria
- HP:0001873 Thrombocytopenia (megaloblastic-related cytopenias) / HP:0001878 Hemolytic anemia
- HP:0001999 Abnormal facial shape (nonspecific; omit unless documented)
- HP:0001252 Hypotonia
- HP:0002020 Gastroesophageal reflux (feeding difficulty proxy) / HP:0011968 Feeding difficulties
- HP:0001508 Failure to thrive
- HP:0007018 Attention deficit — omit, not documented
- HP:0100543 Cognitive impairment
- HP:0001332 Dystonia
- HP:0001251 Ataxia
- HP:0002240 Hepatomegaly — not a typical feature; omit
- HP:0001744 Splenomegaly — not typical; omit
- HP:0004431 Thrombotic microangiopathy / HP:0000822 Hypertension (pulmonary HTN: HP:0002092 Pulmonary arterial hypertension)
- HP:0001891 Thrombophilia / HP:0001895 Microangiopathic hemolytic anemia

(Curators should confirm each against the current HPO release and cite the specific case report supporting it before binding.)

---

## 4. Genetic/Molecular Information

### Causal Gene

- **Gene:** *MMADHC* (HGNC:26275); OMIM *611935
- 8 exons, ~18 kb genomic span, chromosome 2q23.2 (GRCh38: chr2:149,569,637–149,587,778 approx., per GeneCards)
- Encodes: cobalamin trafficking protein CblD (MMADHC protein), a mitochondrial and cytosolic factor

### Pathogenic Variant Classes and Domains

From Coelho et al. 2008 (PMID:18385497) and Jusufi et al. 2014 (PMID:24722857):

- **N-terminal truncating/null variants (upstream of Met116):** abolish mitochondrial targeting/AdoCbl-branch function → **isolated MMA (cblDv2)**
- **Truncating/null variants spanning p.Tyr140–Arg250 (broad C-terminal region):** abolish both branches → **combined MMA + homocystinuria (classic cblD)**
- **Missense variants restricted to a narrow conserved C-terminal segment, p.Asp246–Leu259 (later refined to a region ~p.Arg197–Asp226 as most critical for MeCbl synthesis):** selectively spare AdoCbl synthesis but abolish MeCbl synthesis → **isolated homocystinuria (cblDv1)**
- C-terminal truncations of >20 amino acids give a combined (cblD-MMA/HC)-like cellular phenotype; truncations of 10–20 amino acids give a cblD-HC-like phenotype (Jusufi et al. 2014) — i.e., the precise truncation length within the C-terminal functional domain acts as a rheostat between the combined and isolated-HC phenotypes.

**Specific documented variant:** NM_015702.3(MMADHC):c.748C>T (p.Arg250Ter) — a nonsense variant at the critical p.Arg250 boundary residue, listed in ClinVar (RCV000000803) as associated with methylmalonic aciduria and homocystinuria type cblD.

### Variant Type/Class

Missense, nonsense (frameshift-causing premature termination codons, PTCs), and splice-site variants have all been reported; large deletions/duplications have not been systematically characterized (detection rate for gene-targeted deletion/duplication analysis in *MMADHC* is reported as "unknown" per GeneReviews).

### Allele Frequency / Population Databases

No published carrier-frequency or founder-mutation data specific to *MMADHC*/cblD were identified in gnomAD-based studies (searches of recent gnomAD v4-based carrier-frequency literature did not surface *MMADHC*-specific entries), consistent with its status as one of the rarest inborn errors of cobalamin metabolism — far rarer than cblC (*MMACHC*), for which such data are available. Curators should query gnomAD directly (gene *MMADHC*) for the current allele-frequency table of loss-of-function variants when precise numbers are needed.

### Somatic vs. Germline

Germline only; this is a classic Mendelian inborn error of metabolism, not a somatic/oncologic condition.

### Functional Consequences

- **Loss of function (partial or complete)** of MMADHC's chaperone/adaptor role in cobalamin trafficking. The functional split is between the protein's **N-terminal region**, required specifically for the **mitochondrial route** (AdoCbl synthesis) but **dispensable for cytosolic trafficking**, and its **C-terminal region**, which **contributes to both routes** (per structural/functional studies, PMC4705923; Jusufi et al. 2014).
- The C-terminal globular domain (crystallized as PDB 5CUZ/5CV0) is "sufficient for its interaction with MMACHC... and for supporting the cytoplasmic cobalamin trafficking pathway," and has "an α+β fold that is structurally reminiscent of the nitro-FMN reductase superfamily."
- MMACHC and MMADHC form a **1:1 heterodimer complex**; the cob(II)alamin intermediate generated by MMACHC-mediated dealkylation is stabilized on MMACHC and forms an **inter-protein cobalt-sulfur (Co–S) coordination complex with MMADHC**, physically linking the two proteins during cofactor handoff (Structural Insights paper, PMC4705923; Froese lab work at U Nebraska-Lincoln).

### Modifier Genes

None specifically established for *MMADHC*; functionally interacting genes in the same pathway (see Section 6) are candidates but not validated modifiers.

### Epigenetic / Chromosomal Information

No disease-specific epigenetic or chromosomal-abnormality data reported; cblD is caused by sequence-level variants in a single gene, not by copy-number, translocation, or epigenetic (imprinting/methylation) mechanisms.

### Translational Readthrough — A Notable Molecular/Therapeutic Finding

A 2021 mechanistic study (PMID:[33552904](https://pubmed.ncbi.nlm.nih.gov/33552904/), PMC7847965) found that many pathogenic *MMADHC* alleles generate **premature termination codons (PTCs)**, and tested pharmacologic PTC-readthrough:

> "G418 and gentamicin reconstituted full-length MMADHC R250X expression at variable extent (11.5% and 3.5% expression, respectively, with respect to MMADHC wild type). TGA PTC codons responded more efficiently than TAG or TAA, with R54X and R250X displaying the higher PTC readthrough responses (16% and 8% expression, respectively)."

This is an *in vitro* (cell-based) proof-of-concept for a mutation-specific therapeutic strategy, not yet a clinical intervention — appropriately classified as `evidence_source: IN_VITRO` / `COMPUTATIONAL` (as applicable) for KB curation, and as `EXPERIMENTAL` under Treatment.

---

## 5. Environmental Information

- **Environmental factors:** No toxin, radiation, or pollutant exposures are known to cause or modulate cblD risk. Nitrous oxide (medical anesthesia gas) is a documented **exacerbating/precipitating agent** to be avoided (oxidizes cobalamin, inhibits methionine synthase), relevant as a `Pathophysiology.triggers` / environmental "EXACERBATES" annotation candidate bound to an ECTO term for nitrous oxide exposure.
- **Lifestyle factors:** Standard dietary protein intake should be maintained (GeneReviews explicitly advises against low-protein diets or methionine-free medical foods designed for isolated MMA, since patients with the homocystinuria component need methionine, unlike patients with isolated propionate-pathway MMA).
- **Infectious agents:** Not applicable — cblD is not infectious or infection-triggered, though intercurrent infections/catabolic stress can precipitate acute metabolic decompensation as in other IEMs (a general, non-specific IEM principle rather than a documented cblD-specific trigger in the literature reviewed).

---

## 6. Mechanism / Pathophysiology

### The Intracellular Cobalamin Trafficking Pathway (Causal Chain)

1. **Cellular uptake:** Circulating holo-transcobalamin (holo-TC, cobalamin bound to transcobalamin II) is internalized via receptor-mediated endocytosis through the transcobalamin receptor **TCblR/CD320**.
2. **Lysosomal processing:** In the lysosome, transcobalamin is degraded, freeing cobalamin, which is exported from the lysosomal lumen to the cytosol by the **ABCD4–LMBRD1** transporter complex ("LMBD1 and ABCD4 facilitate the vectorial delivery of lysosomal vitamin B12 to cytoplasmic MMACHC, preventing cofactor dilution to the cytoplasmic milieu"). Defects here cause cblF (*LMBRD1*) and cblJ (*ABCD4*).
3. **Cytosolic dealkylation:** **MMACHC (CblC)** removes the upper axial ligand from incoming cobalamin forms (methyl-, adenosyl-, cyano-, or hydroxocobalamin), generating a common cob(II)alamin intermediate. Defects cause cblC, the most common cobalamin remethylation disorder.
4. **Branch-point trafficking (cblD node):** **MMADHC (CblD)** forms a 1:1 heterodimer with MMACHC via an inter-protein cobalt-sulfur coordination bond and acts as the **branch point** directing the processed cobalamin either:
   - into the **mitochondrion**, where MMAA and MMAB (defective in cblA and cblB, respectively) complete synthesis of **adenosylcobalamin (AdoCbl)**, the cofactor for **methylmalonyl-CoA mutase (MUT)**; or
   - retained in the **cytosol**, complexing with **MTRR** and **MTR (methionine synthase)** to support synthesis of **methylcobalamin (MeCbl)**, the cofactor methionine synthase uses to remethylate homocysteine to methionine.
   
   ("MMACHC, MMADHC, MTRR ... and MTR ... form a multiprotein complex ... which may contribute to shuttle safely and efficiently cobalamin towards MTR in order to produce methionine.") MMADHC's mitochondrial-vs-cytosolic dual localization (both compartments) is structurally consistent with this branch-point role.
5. **Consequence of MMADHC loss-of-function:**
   - Failure of the mitochondrial branch → **AdoCbl deficiency → loss of methylmalonyl-CoA mutase activity → accumulation of methylmalonyl-CoA → methylmalonic acid (MMA) elevation** (methylmalonic aciduria).
   - Failure of the cytosolic branch → **MeCbl deficiency → loss of methionine synthase activity → failure to remethylate homocysteine → homocysteine accumulation (homocystinuria) and low-normal methionine**; disrupted methionine/SAM cycling also impairs downstream methylation reactions broadly (relevant to megaloblastic anemia via impaired thymidylate/purine synthesis pathways that intersect with folate-methionine cycling).
   - Because MMADHC sits at the branch **point itself**, the domain location of the causal variant determines **which branch (or both)** is disrupted — this is the direct molecular explanation for the three clinical phenotypes (Section 4).

### Cellular Processes and Downstream Consequences

- **Megaloblastic anemia** (in the Hcy-affected forms) reflects impaired one-carbon/methionine-cycle metabolism affecting DNA synthesis in erythroid precursors — the classic mechanism shared with other remethylation disorders (cblC, cblE, cblG, MTHFR deficiency).
- **Neurologic injury** (developmental delay, seizures, cerebral/cerebellar atrophy) is attributed to combined effects of homocysteine neurotoxicity, disrupted methylation (via S-adenosylmethionine, SAM) needed for myelination and neurotransmitter synthesis, and (in MMA-predominant disease) methylmalonate/propionate pathway toxicity to mitochondrial energy metabolism.
- **Thrombotic microangiopathy / HUS-like picture and pulmonary hypertension** (reported in cblDv1/HC-predominant patients) mirror the vascular endothelial injury attributed to hyperhomocysteinemia in cblC and classical homocystinuria (CBS deficiency), via endothelial dysfunction and pro-thrombotic effects of elevated homocysteine.

### Suggested GO / CL Terms

- **GO:0009235** cobalamin metabolic process
- **GO:0031419** cobalamin binding
- **GO:0004494** methylmalonyl-CoA mutase activity (downstream enzyme, MUT)
- **GO:0008705** methionine synthase activity (downstream enzyme, MTR)
- **GO:0005739** mitochondrion (subcellular localization of AdoCbl-branch machinery)
- **GO:0005737** cytoplasm/cytosol (MeCbl-branch machinery)
- **GO:0005764** lysosome (upstream trafficking step)
- **CL:0000764** erythroid lineage cell (megaloblastic anemia)
- **CL:0000115** endothelial cell (vascular/microangiopathic complications)

### Molecular Profiling / Advanced Technologies

No transcriptomic, proteomic, metabolomic, single-cell, or spatial datasets specific to cblD patient tissue were identified in this search — consistent with the disease's extreme rarity (patient-derived skin fibroblasts, studied by complementation analysis and functional rescue assays, remain the primary "omics-adjacent" experimental system used in the literature, e.g., Miousse et al. 2009 and Jusufi et al. 2014).

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary:** Central nervous system (brain — cerebral and cerebellar atrophy, developmental delay, seizures); bone marrow (megaloblastic hematopoiesis).
- **Secondary/complication-related:** Kidney (thrombotic microangiopathy/HUS-like picture in Hcy-predominant disease), cardiovascular/pulmonary vasculature (pulmonary hypertension, thromboembolism), eye (nystagmus; ophthalmologic surveillance recommended — macular changes are a hallmark of the related cblC disorder and should be actively screened for, though cblD-specific retinal data are sparse).
- **Body systems:** nervous, hematologic, cardiovascular/pulmonary, renal, ophthalmologic, and (in the acute MMA-predominant neonatal presentations) metabolic/respiratory (respiratory distress).

### Tissue/Cell Level

- Erythroid precursor cells (megaloblastic change)
- Vascular endothelial cells (microangiopathy)
- Neurons and glia (developmental and degenerative CNS changes)
- Skin fibroblasts are the standard *in vitro* diagnostic/research tissue (complementation analysis, functional rescue studies)

### Subcellular Level

- **Mitochondria** (GO:0005739) — site of AdoCbl completion (MMAA/MMAB) and its downstream target enzyme methylmalonyl-CoA mutase
- **Cytosol** (GO:0005829) — site of MeCbl-branch complex (MMACHC-MMADHC-MTRR-MTR) and methionine synthase
- **Lysosome** (GO:0005764) — upstream cobalamin export step (ABCD4/LMBRD1), relevant to the pathway context though not the primary defect site in cblD

### Localization / Laterality

Bilateral/systemic — no lateralized anatomical involvement is described; CNS findings (atrophy) are typically diffuse/bilateral on imaging.

---

## 8. Temporal Development

### Onset

- **Typical age:** infancy to early childhood; some patients present in the neonatal period with acute metabolic decompensation (especially cblDv2/isolated MMA), others present later in childhood or even adolescence with more indolent neurologic/hematologic findings (cblDv1/isolated Hcy).
- **Onset pattern:** can be acute (neonatal metabolic crisis in MMA-predominant disease) or insidious/subacute (progressive developmental delay, neurologic decline in Hcy-predominant disease).

### Progression

- Untreated: progressive neurologic deterioration, structural CNS atrophy, and (for Hcy-predominant disease) escalating thromboembolic/vascular risk.
- Treated (early hydroxocobalamin ± betaine ± folinic acid): stabilization and often marked clinical improvement; growth and developmental trajectory can normalize substantially, though pre-existing structural damage (e.g., established cerebral atrophy) may not fully reverse.
- **Disease course pattern:** chronic, lifelong metabolic disorder requiring ongoing monitoring and treatment; not typically relapsing-remitting once stabilized on therapy, though intercurrent illness/catabolic stress can precipitate acute decompensations.

### Patterns

- **Remission:** treatment-induced biochemical normalization is achievable and is the goal of hydroxocobalamin/betaine therapy; spontaneous remission does not occur (underlying genetic lesion is permanent).
- **Critical periods:** early diagnosis and treatment initiation (including consideration of prenatal maternal hydroxocobalamin therapy where prenatal diagnosis is available) appears critical for neurocognitive outcome, analogous to the well-documented critical window in cblC — GeneReviews notes prenatal OHCbl therapy "may improve neurocognitive outcome; however, the ophthalmologic manifestations are often still present" (in related cobalamin disorders; cblD-specific prenatal-treatment outcome data are limited given case numbers).

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** Orphanet lists cblD prevalence as **<1/1,000,000** — one of the rarest defects of cobalamin metabolism.
- **Total reported cases:** As of the most recent Orphanet/literature synthesis available, **17 cases of cblD have been reported in total: 6 classic (combined) cblD, 5 cblDv1 (isolated homocystinuria), and 6 cblDv2 (isolated MMA)**. GeneReviews independently corroborates that "fewer than 20 cases each" have been described for cblD (grouping it with cblF, cblJ, and cblX as similarly ultra-rare, in contrast to the much more common cblC).
- **Incidence:** Not separately established given the case-report-level ascertainment; too rare for population-based incidence estimates.

### Inheritance Pattern

- **Autosomal recessive**, consistent across all three phenotypic subtypes (classic, cblDv1, cblDv2).
- **Penetrance:** Presumed complete for biallelic pathogenic variants, though given the extremely small numbers, formal penetrance estimates are not available.
- **Expressivity:** Highly variable — indeed, the defining feature of this locus is that *which* biallelic genotype a patient carries determines an essentially qualitatively different biochemical/clinical phenotype (combined vs. isolated MMA vs. isolated Hcy), rather than a graded severity spectrum of one phenotype.
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented for *MMADHC*.
- **Founder effects:** Not established; the Atkinson et al. 2014 case report notes "likely ancestry" shared among some reported cblD-HC patients, suggestive of possible founder or IBD (identity-by-descent) relationships among a subset of cases, but this has not been formally characterized as a population founder mutation.
- **Consanguinity:** Plausibly relevant given AR inheritance and rarity, though not systematically quantified across the case series in the literature reviewed.
- **Carrier frequency:** Not established (too rare; no population screening data identified).

### Population Demographics

- **Affected populations / geographic distribution:** No specific ethnic or geographic clustering has been robustly established in the literature reviewed, beyond the possible shared-ancestry observation above; reported cases are scattered internationally (Canada, USA/other Western case reports being prominent in the literature identified).
- **Sex ratio:** No skew is expected or reported (autosomal recessive).
- **Age distribution of affected individuals in the literature:** predominantly pediatric at diagnosis (infancy through childhood), consistent with onset patterns above.

---

## 10. Diagnostics

### Clinical/Laboratory Tests

- **Urine organic acid (UOA) analysis** — elevated MMA in cblD-combined and cblDv2.
- **Serum/plasma methylmalonic acid** — elevated in MMA-affected forms; important because urinary MMA can be less sensitive than plasma/serum MMA in milder cases (a general lesson from the broader cobalamin-remethylation newborn-screening literature).
- **Total plasma homocysteine (tHcy)** — elevated in cblD-combined and cblDv1.
- **Plasma amino acids (PAA)** — low-to-normal methionine; hypomethioninemia is a key feature distinguishing remethylation-defect homocystinuria (like cblD) from classical homocystinuria due to **cystathionine β-synthase (CBS) deficiency**, in which methionine is typically elevated.
- **Serum vitamin B12** — typically normal (this is an intracellular processing defect, not a B12-absorption/transport deficiency), an important diagnostic pointer away from simple B12 deficiency.
- **Complete blood count** — macrocytic/megaloblastic anemia, hypersegmented neutrophils in Hcy-affected forms.

### Molecular Testing

- **Sequence analysis of *MMADHC*** detects missense, nonsense, and splice-site variants; this is now the primary diagnostic approach.
- **Gene-targeted deletion/duplication analysis:** detection rate "unknown" for *MMADHC* per GeneReviews — i.e., copy-number variant testing has not been well validated for this gene.
- **Complementation analysis** (cultured skin fibroblasts, cell fusion/functional rescue against reference cblC/cblD cell lines): historically the diagnostic gold standard prior to widespread molecular sequencing; still useful for equivocal molecular results or novel variants of uncertain significance, and was central to the original gene-discovery work (Coelho et al. 2008).

### Omics-Based / Screening Diagnostics

- **Newborn screening (NBS):** Standard tandem mass spectrometry NBS uses **propionylcarnitine (C3)** as the primary marker for methylmalonic-acidemia-spectrum disorders and elevated methionine as a marker for classical (CBS-deficiency) homocystinuria. Both approaches have documented limitations for cblD:
  > "C3 (propionylcarnitine) is not always sufficiently sensitive to detect methylmalonic acidemia caused by defects in the adenosylcobalamin synthesis pathway, as demonstrated in a case of cobalamin D disease (cblD) variant 2 missed in newborn screening."
  
  and more generally:
  > "Newborn screening for methylmalonic acidemia uses propionylcarnitine (C3) as a primary index, which is insufficiently sensitive at detecting methylmalonic acidemia caused by defects in the adenosylcobalamin synthesis pathway. Moreover, homocystinuria from cystathionine β-synthase deficiency is screened by detecting hypermethioninemia, but methionine levels decrease in homocystinuria caused by defects in homocysteine remethylation" — meaning cblDv1 (isolated homocystinuria via a remethylation defect) is essentially **invisible** to a screening algorithm tuned to detect hypermethioninemia.

  This is a clinically important, citable diagnostic gap for the KB — cblD (particularly cblDv1 and milder cblDv2) can be **missed on standard newborn screening**, and second-tier markers (direct plasma tHcy and MMA measurement) are increasingly recommended to close this gap (per the broader newborn-screening-for-remethylation-disorders literature, e.g., PMID:[25762406](https://pubmed.ncbi.nlm.nih.gov/25762406/), systematic review and proposed guidelines).

### Clinical Criteria / Differential Diagnosis

- **Key differential:** other cobalamin-remethylation/processing disorders — **cblC** (*MMACHC*, by far the most common and must be ruled out first given far higher prevalence), **cblE** (*MTRR*), **cblG** (*MTR*), **cblF** (*LMBRD1*), **cblJ** (*ABCD4*), **cblX** (*HCFC1*), **cblK** (*ZNF143*); isolated methylmalonic acidemias **cblA**/**cblB** (*MMAA*/*MMAB*) and mut⁰/mut⁻ (*MMUT*) for the isolated-MMA phenotype; classical homocystinuria (**CBS deficiency**) and **MTHFR deficiency** for the isolated-homocystinuria phenotype (distinguished by normal-to-low vs. elevated methionine, respectively).
- Distinguishing cblD from cblC specifically requires either molecular sequencing or complementation analysis, since the biochemical phenotype (combined MMA + Hcy) overlaps substantially.

### Screening

- **Newborn screening:** as above, imperfectly sensitive for cblD, especially cblDv1 and milder cblDv2; second-tier biochemical (direct tHcy/MMA) or genomic newborn screening approaches are increasingly proposed to improve detection.
- **Carrier/prenatal/preimplantation screening:** requires prior identification of the family's specific pathogenic *MMADHC* variants (biochemical carrier testing is not reliable, per GeneReviews); once variants are known, prenatal diagnosis and preimplantation genetic testing are technically feasible.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No cblD-specific survival statistics are available given the small case numbers; severe neonatal-onset presentations (particularly the acute metabolic-decompensation picture described for cblDv2/MACD — respiratory distress, intracranial hemorrhage, ketotic coma) carry meaningful early mortality/morbidity risk if unrecognized, analogous to other severe neonatal-onset methylmalonic acidemias.
- **Morbidity/function:** Developmental delay and other neurologic sequelae (dystonia, spastic ataxia, cerebral/cerebellar atrophy) represent the dominant chronic morbidity when treatment is delayed; vascular/renal complications (HUS-like microangiopathy, pulmonary hypertension, thromboembolism) are additional sources of morbidity, particularly in Hcy-predominant disease.
- **Treatment response / recovery potential:** Early and consistent treatment with parenteral hydroxocobalamin (± betaine, ± folinic acid) is generally reported to improve biochemical parameters and clinical status substantially; by analogy with the better-studied cblC disorder (for which detailed dose-escalation outcome data exist), earlier treatment initiation correlates with better neurocognitive outcome, while some structural changes (once established) are not fully reversible.
- **Prognostic factors:** age at diagnosis/treatment initiation, severity of the initiating metabolic phenotype (combined vs. isolated), and presence/absence of vascular complications appear to be the operative prognostic variables, by extrapolation from the cobalamin-remethylation-disorder literature broadly, though cblD-specific outcome cohorts large enough to formally establish this do not exist.

---

## 12. Treatment

### Pharmacotherapy

- **Parenteral hydroxocobalamin (OHCbl)** is the mainstay of treatment for all three cblD subtypes and should be initiated immediately when the disorder is clinically suspected, even before confirmatory testing returns. GeneReviews specifies typical dosing: infants started at **1.0 mg daily (~0.3 mg/kg/day) intramuscularly or subcutaneously**. Cyanocobalamin is explicitly **ineffective** for cblD (and other intracellular processing defects) and should not be substituted.
  - Suggested CHEBI term: hydroxocobalamin
  - Suggested NCIT treatment_term: NCIT:C15986 (Pharmacotherapy), with `therapeutic_agent` bound to hydroxocobalamin (search CHEBI/NCIT for the specific term at curation time)
- **Betaine** (starting ~250 mg/kg/day, divided doses) — for elevated tHcy, promotes homocysteine remethylation via the betaine-homocysteine methyltransferase (BHMT) pathway, bypassing the deficient methionine synthase step.
- **Folate/folinic acid supplementation** — folinic acid is preferred over folic acid because it crosses the blood-brain barrier more effectively, supporting one-carbon metabolism broadly.

### Nutritional/Dietary

- Normal-protein diet is recommended; GeneReviews specifically warns against **low-protein diets or methionine-free medical foods** designed for isolated (propionate-pathway) MMA, since cblD patients (particularly combined and cblDv1) require methionine intake to support the (deficient) remethylation pathway rather than restrict it.

### Supportive Care

- Gastrostomy tube placement may be required for feeding difficulties in severe cases.
- Standard supportive management of megaloblastic anemia, seizures (anti-epileptic therapy as needed), and developmental support (physical/occupational/speech therapy — NCIT:C15302 Physical Therapy, NCIT:C159273 Speech Therapy, NCIT:C121351 Occupational Therapy as applicable).

### Agents to Avoid

- **Nitrous oxide** — depletes cobalamin and inhibits methionine synthase; contraindicated for anesthesia in these patients.
- Prolonged fasting without dextrose-containing IV fluids (risk of catabolic decompensation).
- Dietary protein restriction below RDA, or use of methionine-free medical foods, contrary to the specific pathway biology of cblD.

### Experimental/Emerging

- **PTC-readthrough pharmacology** (gentamicin, G418): proof-of-concept *in vitro* rescue of nonsense-variant MMADHC expression (PMID:33552904) — a genotype-specific experimental approach relevant to patients with premature-termination-codon-generating variants (e.g., p.Arg250Ter, p.Arg54Ter), not yet in clinical use. Suggested classification: `therapeutic_modality: SMALL_MOLECULE` (readthrough compound), `evidence_source: IN_VITRO`.
- No gene therapy, cell therapy, or RNA-based (ASO/siRNA) therapeutic programs specific to cblD/*MMADHC* were identified in this search.

### Treatment Algorithm / Strategy

Acute suspicion → immediate parenteral hydroxocobalamin + isotonic, high-glucose-concentration IV fluid stabilization → confirmatory biochemical/molecular workup → long-term individualized combination of hydroxocobalamin, betaine (if Hcy-elevated), folinic acid, and normal-protein nutrition, with structured surveillance (below).

### Surveillance / Monitoring

- **First year of life:** monthly-to-bimonthly metabolic specialist evaluation.
- **Toddler/school-age:** at least twice yearly, to adjust medication and assess nutrition.
- **Adolescents/adults:** annual evaluation.
- **Labs monitored:** urine organic acids, serum MMA, plasma amino acids (methionine), total plasma homocysteine, complete blood count (for cytopenias).
- **Clinical assessment:** growth parameters, head circumference, feeding, developmental status, neurologic exam, echocardiography (pulmonary hypertension surveillance), and ophthalmologic evaluation.

### Clinical Trials

No disease-specific registered clinical trials (ClinicalTrials.gov / ICTRP) for cblD/*MMADHC* were identified in this search, consistent with its ultra-rare status; management guidance derives from expert consensus (the 2017 cobalamin-remethylation-disorders diagnosis/management guideline, Huemer et al., *J Inherit Metab Dis* 2017, referenced by GeneReviews and covering cblC, cblD, cblE, cblF, cblJ, and MTHFR deficiency collectively) rather than disease-specific trial data.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the sense of exposure avoidance (genetic disease); genetic counseling and carrier/prenatal testing in families with a known pathogenic variant are the operative "primary prevention" strategy for recurrence.
- **Secondary prevention (early detection):** Improved newborn screening algorithms incorporating second-tier direct plasma tHcy/MMA measurement (rather than relying solely on C3/methionine) have been proposed specifically to close the detection gap for remethylation disorders like cblD (see Section 10); expanded genomic newborn screening is an emerging strategy relevant here as well.
- **Tertiary prevention:** Ongoing surveillance and treatment adherence (Section 12) to prevent/minimize neurologic, hematologic, and vascular complications once diagnosed.
- **Genetic counseling:** Standard autosomal recessive counseling — 25% recurrence risk per pregnancy for carrier parents, 50% carrier risk, 25% unaffected/non-carrier; prenatal diagnosis and preimplantation genetic testing are feasible once the family's specific *MMADHC* variants are known.
- **Prophylaxis:** Avoidance of nitrous oxide anesthesia in known or suspected patients (see Section 12).
- **Public health / immunization / environmental interventions:** Not applicable — no population-level or environmental prevention strategies apply to this genetic disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal cblD disease (OMIA) was identified in this search — unlike some other inborn errors of metabolism, spontaneous *MMADHC*-deficient disease in domestic species does not appear to be documented in the literature reviewed.
- **Orthologous gene:** Mouse ortholog *Mmadhc* (MGI:1923786; NCBI Gene) is conserved and has been targeted for knockout/reporter allele generation by international mouse phenotyping consortia (see Section 15).
- **Comparative biology:** The cobalamin trafficking pathway (MMACHC-MMADHC-MTRR-MTR-MMAA-MMAB) is broadly conserved across mammals, underlying the validity of mouse and other model systems for studying pathway biology generally, though disease-recapitulating characterization of an *Mmadhc*-specific animal model was not found in this search (see below).
- **Zoonotic potential:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

- **Mouse:** A KOMP (Knockout Mouse Project)-derived targeted allele, **Mmadhc^tm2e(KOMP)Wtsi**, is registered at MGI (MGI:5430974) — a conditional-ready/reporter-tagged null allele generated as part of the international knockout mouse resource, available for further phenotyping (e.g., through IMPC, the International Mouse Phenotyping Consortium). Detailed, disease-recapitulating phenotypic characterization data (e.g., biochemical MMA/Hcy elevation, neurologic phenotype, mortality) specific to this *Mmadhc* allele were **not identified** in the sources reviewed here — this appears to be a gap; curators should check IMPC's phenotyping database directly (mousephenotype.org, MGI:1923786) for any released phenotype calls.
- **Related pathway models (context, not cblD-specific):** *Mmachc*-null mice are embryonic lethal — "Deletion of Mmachc in mice is embryonic lethal, which has complicated the early analysis of facial development" — illustrating that complete pathway loss upstream of the MMACHC-MMADHC complex is not viable in mice, which may be relevant context for interpreting why a complete *Mmadhc* knockout model has not yielded a well-characterized postnatal disease model, and why hypomorphic/patient-variant-specific models (or cellular systems) may be more tractable for this pathway.
- **Cellular models:** Patient-derived and immortalized **skin fibroblast lines** (including a well-characterized cblD-MMA/HC patient fibroblast line used for domain-mapping rescue experiments in Jusufi et al. 2014) are the primary experimental system for this disease — used for complementation analysis, functional (AdoCbl/MeCbl synthesis) rescue assays, and structure-function mutagenesis studies. These would be modeled in a dismech entry as `experimental_models` (IN_VITRO), not `animal_models`.
- **Zebrafish/Drosophila/C. elegans/yeast:** No cblD/*MMADHC*-specific models were identified in this search; related cobalamin-pathway zebrafish work exists for *MMACHC* (cblC syndrome; e.g., a 2023 bioRxiv zebrafish chondrocyte-intercalation study), which could be a useful comparative/HUMAN_MODEL_MISMATCH reference point but is not itself an *MMADHC* model.

**Model limitations to note for curation:** Given embryonic lethality of complete pathway knockouts upstream (*Mmachc*), a full *Mmadhc*-null mouse, if similarly lethal, would only be informative via conditional/tissue-specific alleles — the KOMP tm2e allele's conditional-ready design is consistent with this being an anticipated strategy, but confirmed postnatal phenotype data were not found in this search and should be verified directly against IMPC/MGI before citing a specific recapitulation claim.

---

## Summary Table: Suggested Ontology Bindings for KB Curation

| Concept | Suggested term |
|---|---|
| Disease (combined) | MONDO (verify current ID), OMIM:277410 |
| Disease (HMAD/cblDv1) | OMIM:620952 |
| Disease (MACD/cblDv2) | OMIM:620953 |
| Causal gene | hgnc: (verify MMADHC HGNC numeric ID; HGNC symbol MMADHC), NCBIGene:27249 |
| Enzyme (downstream, mitochondrial) | methylmalonyl-CoA mutase — GO:0004494 |
| Enzyme (downstream, cytosolic) | methionine synthase — GO:0008705 |
| Biological process | GO:0009235 cobalamin metabolic process |
| Cell type (anemia) | CL:0000764 erythroid lineage cell |
| Cell type (vascular) | CL:0000115 endothelial cell |
| Phenotype: developmental delay | HP:0001263 |
| Phenotype: nystagmus | HP:0000639 |
| Phenotype: hyperhomocysteinemia | HP:0003081 |
| Phenotype: methylmalonic aciduria | HP:0003201 |
| Phenotype: megaloblastic anemia | HP:0001923 (verify exact HPO term) |
| Treatment: hydroxocobalamin | CHEBI (verify ID), NCIT:C15986 Pharmacotherapy (treatment_term) |
| Treatment: betaine | CHEBI (verify ID) |
| Treatment: folinic acid | CHEBI (verify ID) |
| Exposure to avoid | ECTO (search "nitrous oxide exposure") |

---

## Key Citations

1. Coelho D, Suormala T, Stucki M, Lerner-Ellis JP, Rosenblatt DS, Newbold RF, Baumgartner MR, Fowler B. "Gene identification for the cblD defect of vitamin B12 metabolism." *N Engl J Med.* 2008;358(14):1454-64. PMID: [18385497](https://pubmed.ncbi.nlm.nih.gov/18385497/)
2. Miousse IR, Watkins D, Coelho D, Rupar T, Crombez EA, Vilain E, Bernstein JA, Cowan T, Lee-Messer C, Enns GM, Fowler B, Rosenblatt DS. "Clinical and molecular heterogeneity in patients with the cblD inborn error of cobalamin metabolism." *J Pediatr.* 2009;154(4):551-556. PMID: [19058814](https://pubmed.ncbi.nlm.nih.gov/19058814/)
3. Atkinson C, Miousse IR, Watkins D, Rosenblatt DS, Raiman JA. "Clinical, Biochemical, and Molecular Presentation in a Patient with the cblD-Homocystinuria Inborn Error of Cobalamin Metabolism." *JIMD Rep.* 2014:77-81. PMID: [25155779](https://pubmed.ncbi.nlm.nih.gov/25155779/), PMCID: PMC4241196
4. Jusufi J, et al. "Characterization of functional domains of the cblD (MMADHC) gene product." *J Inherit Metab Dis.* 2014;37(5):841-849. PMID: [24722857](https://pubmed.ncbi.nlm.nih.gov/24722857/)
5. "MMADHC premature termination codons in the pathogenesis of cobalamin D disorder: Potential of translational readthrough reconstitution." PMID: [33552904](https://pubmed.ncbi.nlm.nih.gov/33552904/), PMCID: PMC7847965
6. "Structural Insights into the MMACHC-MMADHC Protein Complex Involved in Vitamin B12 Trafficking." PMCID: PMC4705923
7. "Subcellular location of MMACHC and MMADHC, two human proteins central to intracellular vitamin B(12) metabolism." PMID: [23270877](https://pubmed.ncbi.nlm.nih.gov/23270877/)
8. GeneReviews: "Disorders of Intracellular Cobalamin Metabolism." NCBI Bookshelf NBK1328. https://www.ncbi.nlm.nih.gov/books/NBK1328/
9. OMIM #277410 (MAHCD), #620952 (HMAD), #620953 (MACD), *611935 (MMADHC gene). https://omim.org/entry/277410 ; https://www.omim.org/entry/620952 ; https://omim.org/entry/620953 ; https://omim.org/entry/611935
10. Orphanet ORPHA:79283, "Methylmalonic acidemia with homocystinuria, type cblD." https://www.orpha.net/en/disease/detail/79283
11. "The cblD defect causes either isolated or combined deficiency of methylcobalamin and adenosylcobalamin synthesis." PMID: [15292234](https://pubmed.ncbi.nlm.nih.gov/15292234/)
12. Newborn-screening sensitivity limitations for remethylation disorders / cblD variant 2: "Pilot Study on Neonatal Screening for Methylmalonic Acidemia Caused by Defects in the Adenosylcobalamin Synthesis Pathway and Homocystinuria Caused by Defects in Homocysteine Remethylation," PMCID: PMC8293178; and systematic review PMID: [25762406](https://pubmed.ncbi.nlm.nih.gov/25762406/).
13. MMADHC gene summary — Wikipedia / GeneCards (Entrez 27249, Ensembl ENSG00000168288, UniProt Q9H3L0). https://en.wikipedia.org/wiki/MMADHC ; https://www.genecards.org/card/MMADHC
14. MGI:5430974, *Mmadhc^tm2e(KOMP)Wtsi* targeted allele. https://www.informatics.jax.org/allele/MGI:5430974

**Note on evidence gaps for curation:** Because total published cblD cases number only ~17, several standard KB sections (precise phenotype frequencies, QOL instruments, formal survival statistics, gnomAD carrier frequency, a phenotypically characterized animal model) simply do not have primary-literature data to cite — this should be recorded explicitly as `NOT_YET_DOCUMENTED`/absence-of-evidence in the corresponding schema slots (e.g., `prevalence_class: NOT_YET_DOCUMENTED` or qualitative `ULTRA_RARE`) rather than inferred or fabricated from the better-studied cblC disorder, per the project's evidence-fabrication safeguards. Where cblC data are used only for pathway-mechanism context (not as direct cblD evidence), that distinction must be preserved in the entry's evidence items and explanations.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.