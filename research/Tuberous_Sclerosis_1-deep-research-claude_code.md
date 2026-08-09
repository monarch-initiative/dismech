---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T23:58:38.428601'
end_time: '2026-07-31T00:04:40.046736'
duration_seconds: 361.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)
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
  - claude-sonnet-5
  web_search_requests: 14
  num_turns: 16
  total_cost_usd: 1.6733244
  session_id: aa8143d0-221a-5a14-ac50-52eb4696c6ea
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)** covering all of the
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

# Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex): Comprehensive Research Report

---

## 1. Disease Information

**Overview:** Tuberous sclerosis complex (TSC) is an autosomal dominant, multisystem genetic disorder caused by loss-of-function pathogenic variants in either of two tumor-suppressor genes, **TSC1** (hamartin, 9q34.13) or **TSC2** (tuberin, 16p13.3). Both genes encode subunits of a heterotrimeric complex (with TBC1D7) that functions as a GTPase-activating protein (GAP) for the small GTPase Rheb, and loss of either gene product causes constitutive hyperactivation of mechanistic target of rapamycin complex 1 (mTORC1) signaling. This produces hamartomas (benign but architecturally disorganized growths) in multiple organs — brain, skin, heart, kidney, lung, eyes, and teeth — together with epilepsy, developmental/neuropsychiatric impairment, and organ-specific complications such as renal angiomyolipoma-related hemorrhage and pulmonary lymphangioleiomyomatosis (LAM). **TSC1-related TSC** is the subtype caused specifically by TSC1 variants, which is clinically and genetically distinguishable from TSC2-related disease by generally milder severity and higher familial (vs. de novo) transmission rate (GeneReviews, NCBI Bookshelf NBK1220).

**Key identifiers:**
| System | Identifier |
|---|---|
| OMIM (phenotype, TSC1 locus) | **191100** — Tuberous Sclerosis-1 |
| OMIM (gene, TSC1) | **605284** — TSC Complex Subunit 1 |
| OMIM (phenotype, TSC2 locus, for contrast) | 613254 |
| OMIM (gene, TSC2) | 191092 |
| Orphanet | ORPHA:805 (Tuberous sclerosis complex) |
| ICD-10 | Q85.1 (Tuberous sclerosis) |
| ICD-11 | Foundation entity for tuberous sclerosis exists under LD2C — exact code should be verified against the current ICD-11 browser before curation |
| MeSH | D014402 (Tuberous Sclerosis) |
| MONDO | The umbrella term for TSC exists in MONDO; a TSC1-specific MONDO term (subtype/gene-specific) should be confirmed with an OAK lookup (`runoak -i sqlite:obo:mondo search "tuberous sclerosis 1"`) before citing an exact ID — do not assume a specific MONDO CURIE without verification |
| HGNC (gene) | TSC1, HGNC:12362 |
| Ensembl | ENSG00000165699 |
| UniProt (hamartin) | Q92574 |

**Synonyms:** Bourneville disease; Bourneville-Pringle disease; epiloia (an older portmanteau of "epilepsy" + "low intelligence" + "adenoma sebaceum," now considered outdated/pejorative and not recommended for clinical use); tuberous sclerosis-1; TSC1-related tuberous sclerosis complex; hamartin deficiency.

**Data provenance:** The evidence base for TSC1-TSC is a mixture of aggregated disease-level resources (OMIM, Orphanet, GeneReviews syntheses of population cohorts) and large multi-center genotype-phenotype registries (e.g., the TSC Natural History Database (TOSCA), the US TSC Alliance registry, and national mutation-analysis cohort studies from Greece, Brazil, Mexico, Denmark, and the US that specifically stratify outcomes by TSC1 vs. TSC2 genotype) — not primarily individual EHR-level data, though some more recent screening/penetrance studies (e.g., biobank-based re-analyses) draw on population EHR/genomic cohorts.

---

## 2. Etiology

### Disease Causal Factors
TSC1-related TSC is caused by heterozygous germline (or mosaic) loss-of-function pathogenic variants in **TSC1**. Mutation types include nonsense, frameshift, canonical splice-site, and large genomic deletions/duplications, most of which are predicted to produce a truncated or absent hamartin protein — consistent with a **loss-of-function, haploinsufficiency-plus-second-hit tumor-suppressor mechanism** rather than a gain-of-function or dominant-negative mechanism. Missense variants are relatively uncommon in TSC1 compared with TSC2. Across large cohorts, TSC1 variants account for roughly **15–31%** of mutation-positive TSC cases, with TSC2 accounting for the remainder (69–85%) (search results, multiple mutation-analysis cohorts; PMC5711901; PMC5481739 "The genomic landscape of tuberous sclerosis complex").

### Genetic Risk Factors
- **Causal variant:** Any pathogenic/likely pathogenic TSC1 variant (per ACMG/AMP criteria) is sufficient for diagnosis regardless of clinical findings, per the 2021 updated International TSC Consensus criteria (PMID: 34399110).
- **Somatic "second hit":** Hamartoma formation in TSC follows a **two-hit tumor-suppressor model** (Knudson-type): a germline (first-hit) TSC1 variant plus a somatic second-hit mutation or loss of heterozygosity (LOH) at the TSC1 locus in the affected tissue. LOH has been demonstrated in the majority of TSC-associated renal angiomyolipomas — **84 of 128 TSC renal angiomyolipomas (66%)** showed LOH at TSC1 or TSC2 markers in one classic series — though LOH is preferentially seen at the TSC2 locus over TSC1 in sporadic hamartomas (PMID: 8824721; PMID: 7849708, demonstrating "growth suppressor-like activity also for the TSC1 gene").
- **Mosaicism:** Germline and somatic mosaicism for TSC1/TSC2 variants are increasingly recognized causes of atypical, milder, or clinically unsuspected TSC, and lower the threshold for reporting low-level variants clinically (Human Mutation 2022, PMID search result "Mosaicism in tuberous sclerosis complex: Lowering the threshold for clinical reporting").
- No population-level susceptibility loci or common modifier SNPs for TSC1-TSC severity have been robustly established via GWAS; genotype (TSC1 vs. TSC2, variant type/location) is the dominant known genetic modifier (see Genetic/Molecular section).

### Environmental Risk Factors
TSC1-related TSC has **no known environmental, infectious, toxin, or lifestyle causal risk factors** — it is a purely monogenic disorder. There is no established gene-environment interaction literature specific to TSC1 mutation carriers; environmental factors are not implicated in disease initiation, though secondary factors (e.g., febrile illness, sleep deprivation) can precipitate breakthrough seizures in individuals who already have TSC-associated epilepsy (a disease-modifying rather than causal role).

### Protective Factors
No genetic or environmental protective factors that prevent TSC1-TSC onset are established, consistent with its fully penetrant, single-gene, tumor-suppressor loss-of-function mechanism. At the mechanistic level, retention of the wild-type TSC1 allele (i.e., absence of somatic second-hit LOH) is protective against focal hamartoma formation in a given cell/tissue, which is why lesion burden is patchy/multifocal rather than uniform.

### Gene-Environment Interactions
Not a recognized feature of this disease; TSC1-TSC penetrance and expressivity are driven overwhelmingly by genotype (variant type, second-hit stochastic events, mosaicism level) rather than by environmental exposure.

---

## 3. Phenotypes

TSC has a multisystem hamartoma phenotype; below are core phenotype categories with characteristics and suggested HPO terms (IDs given at moderate-to-high confidence based on established TSC HPO annotations; **all IDs should be confirmed via OAK/HPO browser lookup before insertion into the KB**, per project SOP).

### Neurological / CNS
- **Cortical tubers** — cortical dysplasia; congenital, present from birth, static in number but epileptogenic focus; nearly universal (>90%) in TSC. HPO: cortical tuber (verify exact ID, candidate region under "Abnormality of the cerebral cortex," HP:0002120 lineage).
- **Subependymal nodules (SEN)** — periventricular calcified nodules; present in ~80-90%, generally asymptomatic but monitored for growth into SEGA.
- **Subependymal giant cell astrocytoma (SEGA)** — low-grade (WHO grade I) glioneuronal tumor near the foramen of Monro; develops in ~10-20% of TSC patients, typically ages 5–15; can cause obstructive hydrocephalus if untreated. HPO candidate: HP:0100836/HP:0030966 range — verify.
- **Epilepsy** — the most common and disabling neurological manifestation. Mean prevalence **64.1% in adults and 79.8% in children** across systematic review (PMC12648938). Includes infantile spasms/epileptic spasms (often the presenting sign in infancy) and focal (often multifocal) seizures. HP:0001250 (Seizure); HP:0011097 (Epileptic spasm, verify).
- **TSC-Associated Neuropsychiatric Disorders (TAND)** — a structured umbrella (behavioral, psychiatric [autism spectrum disorder, ADHD, anxiety], intellectual, academic, neuropsychological, and psychosocial domains) affecting **>90% of diagnosed TSC patients** at some point in life (TAND Checklist literature, PMID: 25532776; PMC7487732). Intellectual disability ranges from none to profound and correlates with tuber burden, infantile-spasms history, and genotype.

### Dermatologic
- **Hypomelanotic macules ("ash-leaf spots")** — present in ~90%+, often earliest sign, visible with Wood's lamp.
- **Facial angiofibromas** (previously "adenoma sebaceum") — develop in childhood/adolescence, cosmetically significant; ~75% by adulthood.
- **Shagreen patch** — connective-tissue nevus, typically lumbosacral.
- **Ungual/periungual fibromas (Koenen tumors)** — typically appear later, adolescence/adulthood.
- **"Confetti" skin lesions** — small hypopigmented macules.
- **Dental enamel pits** and **intraoral (gingival) fibromas.**

### Cardiac
- **Cardiac rhabdomyoma** — the most useful **prenatal** marker of TSC; detected by fetal echocardiography in **22.1%** of eventual TSC cases in one cohort. Typically largest in utero, regresses spontaneously postnatally in the majority of cases; can cause outflow obstruction or arrhythmia requiring intervention when large (PMC6071374; search results).

### Renal
- **Renal angiomyolipoma (AML)** — benign but vascular fat/muscle/vessel tumors, risk of spontaneous hemorrhage when >3-4 cm; develop in a majority of adults with TSC, more common/larger in TSC2.
- **Renal cysts**, polycystic-kidney-like disease (much more characteristic of TSC2, due to the contiguous PKD1 gene adjacent to TSC2 on 16p13.3 — the **TSC2/PKD1 contiguous gene syndrome** — this is a TSC2-specific, not TSC1-specific, phenomenon and should not be conflated with isolated TSC1 disease).
- Rarely, renal cell carcinoma.

### Pulmonary
- **Lymphangioleiomyomatosis (LAM)** — smooth-muscle-like cell proliferation causing progressive cystic lung destruction almost exclusively in women (though "multifocal micronodular pneumocyte hyperplasia," MMPH, occurs in both sexes and is more benign). LAM is strongly TSC2-associated but can occur with TSC1 (with generally milder/later-onset course).

### Ophthalmologic
- **Retinal astrocytic hamartoma** ("retinal phakoma") and retinal achromic patches.

### Frequency/severity/progression characteristics
- **Onset:** many manifestations are present from birth or infancy (cardiac rhabdomyoma, hypomelanotic macules, cortical tubers) while others emerge over the life course (facial angiofibromas — childhood/adolescence; renal AML, LAM, ungual fibromas — adolescence/adulthood), reflecting an age-dependent expressivity pattern important for surveillance scheduling.
- **Severity/progression:** highly variable even within families; generally milder and slower progressing in TSC1 vs. TSC2 (see Genetic section).
- **Quality of life impact:** epilepsy (particularly infantile spasms and drug-resistant epilepsy), intellectual disability, and TAND account for the majority of caregiver and patient-reported QoL burden; a validated self-report tool (TAND-SQ) was published in 2023 specifically to capture patient-level QoL burden across TAND domains (Pediatric Neurology 2023).

---

## 4. Genetic/Molecular Information

### Causal Gene
- **TSC1** (HGNC:12362; chr9q34.13; OMIM *605284; NM_000368) encodes **hamartin**, a 130 kDa, 1164-amino-acid hydrophilic protein with no strong catalytic domain of its own. Hamartin stabilizes tuberin (TSC2) against ubiquitin-proteasome degradation and mediates membrane/cytoskeletal anchoring of the TSC1-TSC2-TBC1D7 complex; the Rheb-GAP catalytic activity resides principally in TSC2's GAP domain, but hamartin is required for complex integrity and full GAP activity in vivo.

### Pathogenic Variant Spectrum
- **Variant types:** predominantly protein-truncating (nonsense, frameshift, canonical splice-site) variants and large deletions/duplications; missense variants are comparatively rare in TSC1 relative to TSC2, consistent with TSC1's role as a scaffolding/stabilizing subunit rather than an enzyme.
- **Classification:** per ACMG/AMP guidelines as adopted by the International TSC Consensus Group (PMID: 34399110); pathogenic/likely pathogenic TSC1 variant identification is **sufficient alone** for a definite TSC diagnosis regardless of clinical findings.
- **Allele frequency:** TSC1 pathogenic variants are essentially absent/extremely rare in population reference databases (gnomAD) consistent with strong purifying selection against a fully penetrant dominant disease gene; no common population-frequency pathogenic TSC1 allele exists.
- **Somatic vs. germline:** most TSC1 variants are germline; somatic/mosaic TSC1 variants (constitutional mosaicism, sometimes tissue-limited to skin/hamartoma-only) are an important and previously underappreciated cause of "no mutation identified" (NMI) TSC.
- **Functional consequence:** loss of function → failure to stabilize/complex with tuberin → loss of Rheb-GAP activity → constitutive Rheb-GTP → constitutive mTORC1 activation (gain-of-function at the pathway level, loss-of-function at the gene level).

### Detection Rate and "No Mutation Identified" (NMI)
Conventional clinical genetic testing (sequencing + deletion/duplication analysis) identifies a pathogenic variant in **>85%** of clinically diagnosed TSC cases; **10–15% remain "NMI."** A landmark deep-sequencing study found that when 53 NMI TSC subjects were re-examined with more sensitive methods, mutations were found in **45/53 (85%)** — with mosaicism accounting for the majority (26/45, 58%) and intronic (deep intronic, often splice-affecting) variants in 40% (18/45); some variants were detectable only in skin tumor biopsies, not blood/saliva, at allele frequencies as low as <1% (PMID: 26540169, PLOS Genetics 2015, "Mosaic and Intronic Mutations in TSC1/TSC2 Explain the Majority of TSC Patients with No Mutation Identified by Conventional Testing"). This is directly relevant to genetic-testing recommendations (Section 10).

### Modifier Genes
No robustly validated modifier genes beyond the TSC1/TSC2 genotype itself and second-hit somatic events; variant location/type within TSC1 (truncating vs. rare missense) and mosaicism level are the principal known modifiers of expressivity.

### Epigenetic Information
mTORC1 hyperactivation downstream of TSC1 loss secondarily affects broad transcriptional/translational programs (via S6K1, 4E-BP1, and downstream effects on ribosome biogenesis and, indirectly, chromatin-modifying enzyme translation); TSC-specific primary epigenetic (DNA methylation/histone) driver mechanisms are not a major established feature of TSC1 pathogenesis per se, distinguishing it from primary epigenetic disorders.

### Chromosomal Abnormalities
TSC1 is not typically involved in a contiguous-gene deletion syndrome (unlike TSC2, which sits adjacent to PKD1 on 16p13.3, producing the well-characterized TSC2/PKD1 contiguous deletion syndrome with severe early polycystic kidney disease). Large single-gene deletions/duplications spanning TSC1 do occur and are detected by chromosomal microarray/MLPA, but no recurrent TSC1-adjacent contiguous-gene syndrome is established.

---

## 5. Environmental Information

TSC1-related TSC is a monogenic disorder with **no established environmental causal factors, lifestyle risk factors, or infectious triggers** for disease onset. This section is largely not applicable for etiology. As noted above, non-causal environmental/physiologic stressors (febrile illness, sleep deprivation, medication non-adherence) can precipitate breakthrough seizure activity in individuals with established TSC-associated epilepsy, but do not cause the underlying disease.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathway
The central mechanism is loss of hamartin-tuberin (TSC1-TSC2-TBC1D7) complex function, causing **constitutive activation of mTOR complex 1 (mTORC1)**:

1. **Normal physiology:** Growth factor/PI3K-AKT and AMPK/energy-status signaling converge on the TSC1-TSC2-TBC1D7 complex, which acts as a GTPase-activating protein (GAP) that keeps the small GTPase **Rheb** in its inactive GDP-bound state, restraining mTORC1.
2. **TSC1 loss:** Biallelic loss (germline heterozygous first hit + somatic second hit) destabilizes the complex → loss of Rheb-GAP activity → Rheb-GTP accumulates → **constitutive mTORC1 activation**, independent of normal growth-factor/nutrient cues.
3. **Downstream effectors:** Activated mTORC1 phosphorylates **S6K1** and **4E-BP1**, driving cap-dependent mRNA translation, ribosome biogenesis, lipid biosynthesis (via SREBP), and suppressing autophagy (via ULK1 inhibitory phosphorylation) and lysosomal biogenesis regulation (via TFEB).
4. **Cellular consequence:** unregulated cell growth (increased cell size), altered differentiation, and disorganized tissue architecture — producing the hallmark **hamartoma** (a benign but architecturally disordered mixture of otherwise mature cell types) rather than a frankly malignant neoplasm.

Suggested GO terms: GO:0038202 (TORC1 signaling), GO:0032008 (positive regulation of TOR signaling), GO:0006417 (regulation of translation), GO:1904262 (negative regulation of TORC1 signaling — the normal hamartin/tuberin function), GO:0004871/GO:0005096 (GTPase regulator/GAP activity).

### Cellular Processes
- **Cell growth/hypertrophy** (increased cell size, characteristic "giant cells" seen in cortical tubers and SEGA).
- **Aberrant neuronal migration and differentiation** during corticogenesis, producing dysplastic/dysmorphic "balloon cells" within cortical tubers, histologically and molecularly resembling focal cortical dysplasia type IIb.
- **Impaired autophagy** — mTORC1 hyperactivation suppresses autophagic flux; a body of literature (e.g., PMC8022228, "The paradox of autophagy in Tuberous Sclerosis Complex") explores context-dependent roles of autophagy dysregulation in TSC pathophysiology, including potential compensatory or maladaptive autophagy induction in different cell types/lesions.
- **Angiogenesis and lymphangiogenic proliferation** — relevant to renal AML (vascular component) and LAM (lymphatic-associated smooth-muscle-like cell invasion).

### Protein Dysfunction
Loss-of-function of hamartin — most commonly via nonsense-mediated decay of truncated transcripts or loss of protein stability — removes the scaffolding/stabilizing partner required for tuberin's GAP function; this is best characterized as **loss-of-function of a tumor-suppressor scaffold protein**, not misfolding/aggregation or dominant-negative gain-of-function.

### Metabolic Changes
mTORC1 hyperactivation reprograms cellular metabolism toward anabolism: increased glycolysis, increased lipid/sterol biosynthesis (SREBP-driven), increased nucleotide biosynthesis to support proliferation and hypertrophy, and suppressed catabolic autophagy/lysosomal recycling.

### Immune System Involvement
Not a primary autoimmune or immunodeficiency disease; TSC1 has been shown to play roles in T-lymphocyte development/homeostasis (PMC3954840, "Monoallelic Germline TSC1 Mutations Are Permissive for T Lymphocyte Development and Homeostasis in Tuberous Sclerosis Complex Individuals"), indicating that heterozygous TSC1 loss alone is compatible with largely normal adaptive immune development, consistent with the two-hit requirement for overt pathology.

### Tissue Damage Mechanisms
Tissue disruption in TSC arises primarily from **mass effect/architectural disorganization of hamartomatous overgrowth** (e.g., SEGA causing obstructive hydrocephalus, renal AML causing hemorrhage via abnormal vasculature, LAM causing cystic parenchymal destruction) rather than classic oxidative-stress/ischemic/fibrotic injury pathways, although secondary inflammation and fibrosis can accompany chronic lesions (e.g., pulmonary parenchymal remodeling in LAM).

### Biochemical/Genomic/Advanced Profiling
- **Genomic:** somatic second-hit LOH/point mutations are readily detectable in TSC-associated hamartoma tissue via targeted sequencing (contrast blood vs. lesion DNA) — a key diagnostic/research tool.
- **Transcriptomics/proteomics:** mTORC1 pathway activation signatures (elevated phospho-S6, phospho-4E-BP1 by immunohistochemistry) are used both in research and to confirm mechanistic diagnosis in ambiguous lesions.
- **Single-cell/model-system findings:** single-cell (mosaic) Tsc1 knockout during mouse corticogenesis generates tuber-like lesions and reduces seizure threshold, directly modeling the somatic second-hit mechanism at cellular resolution (Feliciano et al., JCI, PMID search result "Single-cell Tsc1 knockout during corticogenesis generates tuber-like lesions and reduces seizure threshold in mice").

### Causal Chain Summary (for pathophysiology modeling)
**Germline TSC1 heterozygous loss-of-function variant** → (in susceptible somatic cells) **second-hit somatic TSC1 mutation/LOH** → **loss of hamartin-tuberin-TBC1D7 complex GAP activity** → **Rheb-GTP accumulation** → **constitutive mTORC1 hyperactivation** → **dysregulated cell growth, translation, and lipid biosynthesis; impaired autophagy** → **hamartoma formation in brain (tubers, SEN, SEGA), skin, heart, kidney, lung, eye** → **organ-specific clinical manifestations** (epilepsy/TAND from cortical tubers and network hyperexcitability; obstructive hydrocephalus from SEGA; hemorrhage from renal AML; respiratory failure from LAM; outflow obstruction/arrhythmia from cardiac rhabdomyoma).

This maps cleanly onto the dismech `sustaining_proliferative_signaling`/mTOR-adjacent conceptual space but is not currently one of the enumerated hallmark-cancer conformance modules in this KB (TSC hamartomas are benign, not malignant) — a bespoke pathophysiology chain (rather than forced hallmark-module conformance) is the more accurate modeling choice, though `deregulated_cellular_energetics`-style downstream metabolic reprogramming shares conceptual overlap.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** brain (cortical tubers, SEN, SEGA), skin (angiofibromas, hypomelanotic macules, shagreen patch, ungual fibromas), heart (rhabdomyoma), kidney (angiomyolipoma, cysts), lung (LAM in a subset), eye (retinal hamartoma), teeth/oral cavity (enamel pits, gingival fibromas).
- **Secondary/complications:** liver (rare AMLs), bone (sclerotic lesions — reinstated as a 2021 minor diagnostic criterion), GI tract (rectal polyps, hamartomatous polyps).
- **Body systems:** nervous system, integumentary system, cardiovascular system, renal/urinary system, respiratory system, ocular system, skeletal system.

Suggested UBERON terms: UBERON:0000955 (brain), UBERON:0002037 (cerebellum, if relevant), UBERON:0002113 (kidney), UBERON:0000948 (heart), UBERON:0002048 (lung), UBERON:0001003 (skin epidermis), UBERON:0000970 (eye).

### Tissue and Cell Level
- **Cortical tuber:** dysplastic cortical tissue containing giant/balloon cells, dysmorphic neurons, and reactive astrocytes.
- **SEGA:** mixed glioneuronal tumor cells expressing both glial and neuronal markers.
- **Renal AML:** triphasic tissue — smooth muscle (myoid) cells, thick-walled blood vessels, and mature adipose tissue; the perivascular epithelioid cell (PEComa family member).
- **LAM lesion:** "LAM cells" — smooth-muscle-like, HMB-45-positive (melanocytic-marker-expressing) perivascular epithelioid cells infiltrating along lymphatics.
- **Facial angiofibroma:** dermal fibrous tissue with vascular proliferation.

Suggested CL terms: CL:0002608 (astrocyte of the cerebral cortex — for tuber reactive astrocytes, verify), CL:0000192 (smooth muscle cell — relevant to AML/LAM), CL:0002214 (perivascular cell, PEComa-relevant — verify closest CL term), CL:0000136 (fat cell/adipocyte — AML adipose component).

### Subcellular Level
The core molecular lesion operates primarily at the **cytoplasmic signaling complex level** (hamartin-tuberin-TBC1D7 heterotrimer, GO:0033596 TSC1-TSC2 complex), with downstream effects on **lysosome-associated mTORC1 signaling** (mTORC1 is lysosome-membrane-localized; GO:0005765 lysosomal membrane), ribosome (translation machinery), and — via autophagy suppression — the autophagosome/lysosome degradative system.

### Localization / Lateralization
Lesions are typically **multifocal and bilateral** (e.g., cortical tubers scattered across both hemispheres; bilateral renal AMLs), reflecting the stochastic, multi-hit somatic mutation mechanism rather than a single developmental field defect — unlike unilateral focal cortical dysplasia. Retinal hamartomas and rhabdomyomas can be single or multiple, unilateral or bilateral.

---

## 8. Temporal Development

### Onset
- **Congenital/prenatal:** cardiac rhabdomyoma (often first detected on routine fetal ultrasound/echocardiography, sometimes as early as the second trimester), cortical tubers (present from fetal cortical development).
- **Infancy:** hypomelanotic macules often first noted; infantile spasms (peak onset ~4-8 months) frequently the earliest neurological symptom.
- **Childhood:** facial angiofibromas typically emerge from ~2-5 years and progress through adolescence; SEGA most often diagnosed ages 5-15.
- **Adolescence/adulthood:** ungual fibromas, renal AMLs, and LAM (women, typically 20s-40s) characteristically emerge or become clinically significant later.

### Progression
- **Cortical tubers/SEN:** largely static in number once formed, though SEN can occasionally grow into SEGA.
- **SEGA:** can grow progressively, particularly in the first two decades, with risk of acute obstructive hydrocephalus if untreated; growth typically plateaus in adulthood.
- **Renal AML:** progressive growth over time, with hemorrhage risk correlating with size (>3-4 cm threshold commonly used clinically) and elastin-poor aneurysmal vasculature.
- **LAM:** slowly progressive cystic lung destruction, historically leading to respiratory failure over years-to-decades in untreated women; sirolimus/everolimus can stabilize lung function decline.
- **Cardiac rhabdomyoma:** the classic **regressive** lesion — enlarges in utero/late gestation but **usually regresses spontaneously postnatally**, with follow-up echocardiography showing shrinkage/resolution in a majority of cases by the second year of life.
- **Epilepsy:** often evolves from infantile spasms to multifocal drug-resistant epilepsy in a substantial minority; a subset achieve seizure freedom, particularly with early, aggressive, mTOR-pathway-directed and surgical management.

### Patterns
- **Remission:** cardiac rhabdomyoma spontaneous regression is the paradigmatic remission pattern in TSC; seizures can remit spontaneously in some children but drug-resistant epilepsy is common and rarely remits without intervention.
- **Critical periods:** the first 1-2 years of life represent a critical window for both (a) infantile-spasms-related neurodevelopmental injury and (b) the therapeutic opportunity being tested by "preventive"/pre-symptomatic treatment trials (see Prevention section) — reflecting the concept that early network hyperexcitability may itself drive later cognitive/behavioral impairment (the "epileptic encephalopathy" concern in TSC).

---

## 9. Inheritance and Population

### Epidemiology
- **Birth incidence:** ~1 in 6,000 live births (widely cited figure across OMIM, GeneReviews, StatPearls).
- **Population prevalence:** ~1 in 10,000 to 1 in 20,000 in various estimates; a systematic review found incidence per 100,000 live births ranging **0.153–17.24** and prevalence per 100,000 general population ranging **0.6–12.7** across countries, reflecting real variation in ascertainment, diagnostic access, and possibly true population differences (PMC results, epidemiology systematic review).
- An estimated **~2,000,000 people** are affected by TSC worldwide (Medscape/StatPearls estimate); TSC1 accounts for roughly 15-31% of these (i.e., a meaningfully smaller subset than TSC2).

### Inheritance Pattern
- **Autosomal dominant**, high penetrance (widely cited as ~95-100% by clinical exam plus imaging, though a 2026 European Journal of Human Genetics analysis specifically re-examines "apparent incomplete penetrance of TSC1/TSC2 variants" in population biobank cohorts, suggesting some historically "fully penetrant" variants may show reduced penetrance when ascertained outside clinically selected cohorts — an important nuance for newborn-screening-era genetic counseling; PMID search result, "Uncovering apparent incomplete penetrance of TSC1/TSC2 variants... implications for newborn screening").
- **De novo rate:** approximately **two-thirds of all TSC cases are de novo**; however, this splits very differently by gene — **TSC2 mutations are de novo in ~86%** of cases, while a much larger share of TSC1 cases are **familial (inherited)**, with one analysis noting that ~75% of familial TSC cases carry a TSC1 mutation, "likely due to its milder phenotype" permitting affected individuals to reproduce (search result synthesis of genotype-phenotype cohort literature). This asymmetry is one of the most clinically important genotype-driven features distinguishing TSC1 from TSC2 disease.
- **Expressivity:** highly variable, even within the same family carrying an identical TSC1 variant — consistent with the stochastic somatic second-hit model superimposed on a fixed germline genotype.
- **Genetic anticipation:** not a recognized feature of TSC1/TSC2 disease (not a repeat-expansion disorder).
- **Germline mosaicism:** recognized and clinically important for recurrence-risk counseling in apparently "sporadic" cases with unaffected parents — a mosaic parent can transmit to multiple offspring despite testing negative on standard peripheral blood sequencing.
- **Founder effects:** no major population-specific TSC1 founder variant is well established (contrast with some other Mendelian diseases); TSC1 pathogenic variants are largely private/family-specific.
- **Consanguinity:** not a relevant risk factor, since TSC is dominant rather than recessive.
- **Carrier frequency:** not applicable in the recessive-carrier sense; as a dominant fully-penetrant-ish disorder, "carriers" are themselves affected (or mosaic-affected) individuals.

### Population Demographics
- Affects **all ethnicities and both sexes equally** — no established sex ratio skew or ethnic predisposition for TSC1-TSC itself (distinct from LAM, which is markedly female-predominant as a downstream manifestation).
- **Geographic distribution:** no endemic clustering; reported incidence/prevalence variation across countries is attributed mainly to differences in healthcare access, diagnostic awareness, and ascertainment rather than population genetics per se, per the epidemiology systematic review cited above.

### Sex-Specific Note
While overall TSC1/TSC2 birth prevalence is sex-neutral, certain downstream manifestations are markedly sex-skewed: LAM is essentially restricted to females (and rare males with other conditions), reflecting a hormonally modulated (estrogen-sensitive) component of TSC-related smooth-muscle-like cell proliferation in the lung.

---

## 10. Diagnostics

### Clinical Diagnostic Criteria (2021 Update)
The **2021 Updated International Tuberous Sclerosis Complex Diagnostic Criteria** (PMID: 34399110, Pediatric Neurology) retain the 2012 major/minor clinical feature framework with two specific changes:
1. "**Multiple cortical tubers and/or radial migration lines**" replaced the more general "cortical dysplasias" as a major feature.
2. "**Sclerotic bone lesions**" were reinstated as a minor feature.

A **definite clinical diagnosis** requires 2 major features (or 1 major plus ≥2 minor features); a **possible clinical diagnosis** requires either 1 major feature or ≥2 minor features. Critically, **identification of a pathogenic (or likely pathogenic) TSC1 or TSC2 variant is independently sufficient for diagnosis, regardless of clinical findings** — because manifestations of TSC accrue with age, a young child may not yet meet clinical criteria but can be genetically confirmed.

### Genetic Testing
- **Recommended first-tier approach:** combined sequence analysis plus deletion/duplication (copy-number) analysis of TSC1 and TSC2, per GeneReviews and the 2021 consensus recommendations.
- **Sensitivity:** identifies a pathogenic variant in >85% of clinically diagnosed cases; **10-15% remain NMI** on conventional testing.
- **Next-generation/deep sequencing** for suspected mosaicism (particularly when clinical picture is atypical/mild, or when a "sporadic" case has unaffected parents) recovers pathogenic variants in the majority of previously NMI cases (85% in the Tyburczy et al. cohort), predominantly via detection of low-level mosaicism and deep intronic variants — an important practical recommendation for genetic counselors evaluating "TSC1/TSC2-negative" clinically diagnosed patients.
- **Tissue-based testing:** in rare cases a causative variant is detectable only in lesion (e.g., skin tumor) DNA, not blood/saliva — relevant when standard blood-based NGS is negative but clinical suspicion remains high.
- **Variant interpretation:** should follow ACMG/AMP standards as adopted by the TSC consensus group.
- **Prenatal/preimplantation testing:** available for families with a known pathogenic familial variant (see Prevention).

### Imaging and Organ-Specific Surveillance
- **Brain MRI:** for tubers, SEN, and SEGA surveillance, typically at diagnosis and then periodically through childhood/adolescence (per consensus recommendations, generally every 1-3 years until age 25 if asymptomatic, or as clinically indicated).
- **Fetal/neonatal echocardiography:** for cardiac rhabdomyoma — the leading prenatal clue to TSC.
- **Renal MRI (or ultrasound where MRI unavailable):** for AML and cyst surveillance, generally every 1-3 years.
- **Dermatologic exam:** annual skin survey for angiofibroma, shagreen patch, ungual fibroma progression.
- **Dilated ophthalmologic exam** for retinal hamartomas.
- **Dental exam** for enamel pits/gingival fibromas.
- **EEG:** baseline and as needed for seizure characterization; some centers use serial/video EEG or even prospective/prodromal EEG monitoring in infancy given the interest in preventive antiepileptic strategies (see below).
- **Chest HRCT:** recommended for LAM screening in women with TSC, typically once in early adulthood and repeated per pulmonary symptoms/findings.
- **Neuropsychological/TAND screening:** the TAND Checklist is recommended at every clinical visit as a rapid multi-domain screen, with more detailed neuropsychological testing at key developmental transition points (PMID: 25532776; PMC7487732).

### Differential Diagnosis
Focal cortical dysplasia (isolated, non-TSC), other PI3K-AKT-mTOR pathway "mTORopathies" (e.g., PTEN hamartoma tumor syndrome, focal cortical dysplasia type II from somatic mTOR pathway gene mutations, hemimegalencephaly), other causes of infantile spasms, other genetic syndromes with facial angiofibroma-like lesions (e.g., multiple endocrine neoplasia type 1 can show facial angiofibromas), Birt-Hogg-Dubé syndrome (renal tumors, pulmonary cysts — a differential for the AML/LAM-like phenotype but genetically and histologically distinct, FLCN gene).

### Screening
No population-based universal newborn screening program for TSC currently exists (it is not detected by standard newborn metabolic/genetic screening panels), though the growing role of genomic newborn screening pilots is prompting active discussion of TSC1/TSC2 penetrance in unselected populations (see the 2026 EJHG penetrance paper above). Cascade/family testing is recommended once a proband's familial variant is identified, given the ~1/3 (and disproportionately TSC1-driven) familial transmission rate.

---

## 11. Outcome/Prognosis

### Survival and Mortality
With modern multidisciplinary management, **life expectancy in TSC approaches that of the general population** for most individuals, though historically (and still in under-resourced settings) mortality is elevated relative to background due to:
- **SEGA-related acute obstructive hydrocephalus** if undiagnosed/untreated.
- **Renal AML hemorrhage** — a historically significant cause of TSC mortality, now substantially mitigated by surveillance and mTOR-inhibitor/embolization management.
- **Status epilepticus and SUDEP (sudden unexpected death in epilepsy)** risk in individuals with severe drug-resistant epilepsy.
- **LAM-related respiratory failure** in affected women, historically progressive to end-stage lung disease/transplant need, now substantially altered by sirolimus therapy.
TSC1-related disease, being milder on average, is generally associated with a **more favorable prognosis** than TSC2-related disease across essentially all of these axes.

### Morbidity and Function
The dominant drivers of lifelong morbidity are **epilepsy severity and TAND/intellectual disability burden**, which correlate with tuber burden, infantile-spasms history, and (again) genotype — TSC2 patients showing "more severe neurologic phenotype, including an earlier age of seizure onset, lower cognition index and more tubers" compared with TSC1 patients (search synthesis of genotype-phenotype literature). Renal and pulmonary complications drive adult morbidity; facial angiofibromas and other visible skin lesions contribute meaningfully to psychosocial/quality-of-life burden independent of organ-threatening severity.

### Disease Course / Complications
Complications include: obstructive hydrocephalus (SEGA), renal hemorrhage/chronic kidney disease (AML, cysts), pneumothorax/chylothorax and progressive respiratory failure (LAM), cardiac arrhythmia/outflow obstruction (rhabdomyoma, rare), drug-resistant epilepsy, and psychiatric/behavioral comorbidity (ASD, ADHD, anxiety, depression) under the TAND umbrella.

### Prognostic Factors
- **Genotype** (TSC1 generally milder than TSC2) is among the most consistently reported prognostic factors across multiple independent cohorts (Greek, Brazilian, Mexican, Danish, US cohorts cited above).
- **Infantile spasms history** and **early/refractory epilepsy** are strong predictors of subsequent intellectual disability/TAND severity.
- **Tuber count/burden** correlates with cognitive outcome and epilepsy severity.
- **Timing of mTOR-inhibitor initiation** is an emerging prognostic-modifying factor, with growing interest in early/preventive treatment paradigms (see below).

---

## 12. Treatment

### Pharmacotherapy — mTOR Inhibitors (Disease-Modifying, Multisystemic)
Because TSC pathophysiology is driven by constitutive mTORC1 activation, **mTOR inhibitors are the only class of therapy that addresses the underlying molecular mechanism across multiple organ systems simultaneously**, rather than treating individual manifestations symptomatically:
- **Everolimus** (oral mTORC1 inhibitor) — FDA/EMA-approved for **SEGA**, **renal AML**, and **TSC-associated refractory partial-onset seizures**. The pivotal **EXIST-1** trial (phase 3, international, double-blind, placebo-controlled) demonstrated sustained SEGA tumor-volume reduction with long-term use (PMC4924870, "Long-Term Use of Everolimus in Patients with Tuberous Sclerosis Complex: Final Results from the EXIST-1 Study"). The **EXIST-3** trial established efficacy as adjunctive therapy for TSC-associated refractory partial-onset seizures (PMID: 31335226). A 2021 study specifically documented the SEGA-shrinking effect in children (PMID: 34782838).
- **Sirolimus (rapamycin)** — the mTORC1 inhibitor of choice for **LAM** (per the NEJM MILES trial, PMID: 21525617, "Efficacy and Safety of Sirolimus in Lymphangioleiomyomatosis") and is also used off-label/in specific contexts for renal AML and other manifestations; mTOR inhibitors are now described as **"the first-choice therapy for renal angiomyolipomas secondary to tuberous sclerosis"** (PMC10726659, 2023).
- **Topical sirolimus/rapamycin gel** — approved in some jurisdictions (e.g., "Hyftor") specifically for facial angiofibroma treatment, avoiding systemic exposure for a primarily cosmetic/dermatologic indication.

MAXO term: MAXO:0000647 (chemotherapy) is not quite right for these targeted small-molecule inhibitors; a generic **NCIT:C15986 (Pharmacotherapy)** treatment_term with `therapeutic_agent` bound to CHEBI (everolimus CHEBI:68478; sirolimus/rapamycin CHEBI:9168) is the more accurate dismech pattern, consistent with the project's "generic action + therapeutic_agent" convention for targeted small molecules.

### Antiepileptic and Neurological Therapy
- **Vigabatrin** — first-line for TSC-associated infantile spasms (GABA-transaminase inhibitor); strong efficacy specifically for the infantile-spasms seizure type.
- **Cannabidiol (Epidiolex)** — FDA-approved (2020) for seizures associated with TSC in patients ≥1 year, based on the phase 3 **GWPCARE6** trial: patients who had failed a median of 4 prior antiepileptic drugs saw a **48% reduction in seizure frequency** with CBD (25 or 50 mg/kg/day) vs. **24% with placebo** (search result synthesis; NeurologyLive/Medscape coverage of FDA approval).
- Other broad-spectrum antiseizure medications, ketogenic diet, vagus nerve stimulation, and **epilepsy surgery** (tuber/epileptogenic-zone resection, corpus callosotomy in selected drug-resistant cases) round out the epilepsy treatment algorithm.
- MAXO terms: MAXO:0000004 (surgical procedure) for epilepsy surgery; MAXO:0000088 (dietary intervention) for ketogenic diet.

### Surgical/Interventional
- **SEGA resection** or, increasingly, primary everolimus therapy as a surgery-sparing alternative for growing/symptomatic SEGA.
- **Renal AML embolization** (selective arterial embolization) for actively bleeding or high-risk large AMLs; **nephron-sparing partial nephrectomy** in select cases; mTOR inhibitors have substantially reduced surgical intervention rates for AML in the modern era.
- **Cardiac surgery** rarely needed for rhabdomyoma causing hemodynamically significant outflow obstruction (most regress spontaneously and require only monitoring).

### Supportive/Rehabilitative
Multidisciplinary developmental/behavioral therapy, speech/occupational/physical therapy as indicated by TAND profile, psychiatric management of comorbid ASD/ADHD/anxiety, and structured TAND-focused psychosocial support for patients and families.

### Experimental / Emerging
- **Early/"preventive" mTOR-inhibitor or antiepileptic treatment** prior to seizure onset is an area of active trial activity (see below and Prevention section), including a head-to-head rapamycin-vs-vigabatrin prevention trial (ClinicalTrials.gov NCT04987463).
- Ongoing investigation of combination and next-generation mTOR pathway modulators, and of biomarker-guided (e.g., EEG-based) early intervention strategies to prevent epileptic-encephalopathy-related cognitive injury.

### Treatment Outcomes / Trial Evidence Summary
| Trial | Drug | Population | Key Result | Reference |
|---|---|---|---|---|
| EXIST-1 | Everolimus | TSC with SEGA | Sustained SEGA volume reduction, long-term durable response | PMC4924870 |
| EXIST-3 | Everolimus | TSC refractory focal seizures | Adjunctive efficacy for seizure reduction | PMID:31335226 |
| MILES | Sirolimus | LAM | Stabilized lung function decline | PMID:21525617 |
| GWPCARE6 | Cannabidiol | TSC seizures | 48% vs 24% (placebo) seizure-frequency reduction | FDA approval coverage, 2020 |
| EPISTOP | Preventive vigabatrin | TSC infants pre-seizure-onset | Seizures at 2y: 52% (VGB) vs 84% (conventional); delayed/prevented infantile spasms | Search result synthesis |
| PREVeNT | Preventive vigabatrin | TSC infants pre-seizure-onset (US) | Delayed/reduced infantile spasms but did **not** improve 2-year neurocognitive outcomes; no broad protection against focal seizures | Search result synthesis; Annals of Neurology commentary 2024 |

### Treatment Strategy
Modern TSC management follows a genotype-informed, surveillance-driven, multidisciplinary algorithm (per the 2021 consensus recommendations companion to the diagnostic criteria) with **mTOR inhibitors positioned as the multisystemic disease-modifying backbone**, layered with organ-specific symptomatic/interventional therapy and increasing interest in **early/preventive intervention during the infantile window** to reduce cumulative neurodevelopmental injury from uncontrolled early seizures.

---

## 13. Prevention

- **Primary prevention:** not possible in the classic sense (monogenic dominant disorder); the closest analog is **reproductive/preconception genetic counseling and reproductive options** (see below) for families with a known pathogenic TSC1 variant.
- **Secondary prevention (early detection):** prenatal detection via fetal echocardiography (cardiac rhabdomyoma) prompts early postnatal diagnosis and surveillance; the **preventive antiepileptic treatment paradigm** (EPISTOP/PREVeNT trials, above) represents a secondary-prevention strategy aimed at intercepting epileptogenesis before clinical seizure onset in genetically/EEG-identified high-risk infants — with EPISTOP showing benefit for delaying/reducing infantile spasms specifically, but PREVeNT showing no improvement in broader 2-year neurocognitive outcomes, an important nuance requiring individualized counseling (2024 Annals of Neurology commentary on both trials).
- **Tertiary prevention:** the entire organ-surveillance program (serial brain/renal/pulmonary imaging, dermatologic/ophthalmologic/dental exams) exists specifically to detect and intervene on complications (SEGA growth, AML enlargement, LAM progression) before they cause irreversible organ damage or acute crises (hydrocephalus, hemorrhage, respiratory failure).
- **Genetic counseling:** central to TSC1-TSC management given its ~1/3 familial transmission rate (disproportionately TSC1) — includes discussion of recurrence risk (50% for each child of an affected parent; low but non-zero recurrence risk for "sporadic" cases due to germline mosaicism), and reproductive options.
- **Reproductive/prenatal options:** preimplantation genetic testing (PGT-M) and prenatal diagnosis (chorionic villus sampling/amniocentesis) are available once the familial pathogenic TSC1 variant is known.
- **Screening programs:** no population-wide newborn screening program exists for TSC at present; screening is currently family/cascade-based following proband identification, though genomic newborn screening pilots are prompting reassessment of TSC1/TSC2 penetrance assumptions in unselected populations (2026 EJHG paper cited above).
- **Immunization:** not applicable (non-infectious disease).
- **Behavioral/public health/prophylactic medication:** not applicable beyond the epilepsy-prevention paradigm discussed above; no chemoprophylaxis exists outside the investigational early-mTOR-inhibitor/antiepileptic trial context.

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected species:** Naturally occurring TSC1-driven disease in non-human species is **not well characterized**; TSC is predominantly studied in humans, with disease models almost entirely **engineered** (genetically modified) rather than spontaneous/natural.
- **Related natural/spontaneous models (not TSC1-specific):** the classic **Eker rat** carries a **spontaneous germline Tsc2 (not Tsc1) mutation** and develops hereditary renal cell carcinoma — historically important for tuberin/mTOR pathway discovery but is a **TSC2**, not TSC1, natural disease model, and should not be miscited as a TSC1 model.
- **Veterinary relevance:** No well-established naturally occurring TSC1-orthologous disease has been characterized in companion animals (dogs, cats) or livestock in the literature surveyed; this differs from some other hamartoma-syndrome genes (e.g., FLCN/Birt-Hogg-Dubé-like renal cystadenocarcinoma and nodular dermatofibrosis reported in German Shepherd dogs, which is a distinct gene/pathway).
- **Comparative biology / evolutionary conservation:** the TSC1-TSC2-Rheb-mTOR axis is **highly evolutionarily conserved**, having been foundationally characterized in **Drosophila melanogaster** (the *Tsc1*/*gigas* and *Tsc2* orthologs, whose loss-of-function phenotypes — organ/cell overgrowth — were instrumental in first linking TSC genes mechanistically to Rheb-mTOR signaling in the early 2000s) and in *C. elegans*; this cross-species conservation underlies why fly and worm genetics were pivotal in originally solving the TSC1/TSC2-mTOR mechanism, even though neither organism develops a "natural" TSC-like disease per se.
- **Orthologous genes:** Drosophila Tsc1 (gene ID varies by build; FlyBase), *C. elegans* tsc-1, zebrafish tsc1a/tsc1b (duplicated paralogs), rat Tsc1 (RGD), mouse Tsc1 (MGI:1202879).
- **Transmission/zoonotic potential:** not applicable — TSC is a purely genetic, non-transmissible, non-zoonotic disorder.

---

## 15. Model Organisms

### Mouse (primary mammalian model)
- **Germline heterozygous Tsc1+/- mice:** model the "first hit" state; largely healthy at baseline (consistent with the human two-hit requirement) but develop renal cystic/tumor lesions over time even **without evidence of mTOR activation in early lesions**, per one study ("Tsc1 Haploinsufficiency without Mammalian Target of Rapamycin Activation Is Sufficient for Renal Cyst Formation in Tsc1+/− Mice," AACR Cancer Research) — an important nuance suggesting non-canonical, mTOR-independent contributions of Tsc1 haploinsufficiency to early lesion formation.
- **Conditional/tissue-specific Tsc1 knockouts:** used extensively to dissect organ-specific mechanisms — e.g., neural-progenitor/radial-glial Tsc1 deletion produces cortical dysplasia-like and hippocampal abnormalities reminiscent of human tubers; eye-progenitor-specific Tsc1 ablation disrupts visual-pathway development with classic TSC neuropathological hallmarks (Disease Models & Mechanisms, PMC4728318); pan-neuronal Tsc1 knockout mice show reduced surface GABA-receptor-subunit expression, mechanistically linking Tsc1 loss to network hyperexcitability.
- **Single-cell (mosaic) Tsc1 knockout via in utero electroporation:** directly models the somatic second-hit mechanism, generating focal **tuber-like lesions and reducing seizure threshold** — arguably the most mechanistically faithful rodent recapitulation of human tuber pathogenesis to date (Feliciano et al., JCI, search result "Single-cell Tsc1 knockout during corticogenesis generates tuber-like lesions and reduces seizure threshold in mice").
- **Mosaic Tsc1-knockout renal model:** recapitulates human perivascular epithelioid cell tumors (PEComas)/AML-like renal lesions.
- **Timing-of-activation studies:** demonstrate that the developmental timing of mTOR pathway activation (i.e., when during corticogenesis Tsc1 is lost) materially affects the resulting neuropathology, informing critical-period concepts relevant to human preventive-treatment trial design (PMC3759338, "Timing of mTOR activation affects tuberous sclerosis complex neuropathology in mouse models").
- **Model limitations:** rodent models generally do not spontaneously develop the full multisystem human phenotype (e.g., robust SEGA-equivalent tumors, facial angiofibroma-equivalent skin lesions, or LAM-equivalent lung disease are inconsistently or only partially recapitulated), and cortical lamination/gyrification differences between mouse and human brains limit direct translational mapping of cortical tuber biology — a caveat particularly relevant to any `HUMAN_MODEL_MISMATCH`-flagged claims in a dismech entry.

### Other Model Systems
- **Drosophila melanogaster:** the founding genetic model for the Tsc1/Tsc2-Rheb-TOR pathway; loss-of-function Tsc1 or Tsc2 mutants show characteristic tissue/organ overgrowth phenotypes that were used to establish the core epistatic pathway (Tsc1/Tsc2 → Rheb → TOR) prior to its confirmation in mammalian systems.
- **Zebrafish (tsc1a/tsc1b):** used for developmental and pharmacological (drug-screening) studies given rapid development and optical transparency, useful for visualizing organ-specific hamartoma-like phenotypes and testing candidate compounds.
- **C. elegans:** used for basic pathway/genetic-interaction studies of tsc-1 within the conserved TOR signaling network.
- **iPSC-derived and organoid models:** patient-derived iPSC and cortical/cerebral organoid models carrying TSC1 or TSC2 mutations are an emerging platform for studying human-specific aspects of tuber/balloon-cell formation and network hyperexcitability, addressing some of the cross-species translational gaps noted above (relevant to a `HUMAN_MODEL_MISMATCH` framing for any organoid-only findings not yet confirmed in patient tissue).

### Research Applications
Mouse and Drosophila models have been used to dissect: (1) the core Rheb-mTORC1 signaling mechanism; (2) the two-hit somatic mutation model of hamartoma formation; (3) developmental-timing dependence of neuropathology; (4) mTOR-inhibitor pharmacodynamics and dose-response (preclinical basis for everolimus/sirolimus trials); (5) network hyperexcitability mechanisms (GABA receptor trafficking) underlying TSC epilepsy; and (6) renal/PEComa-like tumorigenesis.

### Resources
MGI (Mouse Genome Informatics) for Tsc1 mouse alleles/phenotypes; RGD (Rat Genome Database) for Eker rat Tsc2 model; ZFIN for zebrafish tsc1a/tsc1b; FlyBase for Drosophila Tsc1; IMSR for locating specific engineered mouse strains.

---

## Summary Table: Suggested Ontology Term Anchors for KB Curation

| Domain | Suggested term(s) | Confidence / verification needed |
|---|---|---|
| Disease | MONDO (TSC1-specific), ORPHA:805, OMIM:191100 | MONDO ID needs OAK verification |
| Gene | hgnc:12362 (TSC1) | High confidence |
| Molecular function/process | GO:0038202 (TORC1 signaling); GO term for TSC1-TSC2 complex GAP activity | Verify exact IDs via OAK |
| Cell types | CL term for cortical astrocyte/dysplastic neuron; CL:0000192 (smooth muscle cell, for AML/LAM) | Verify via OAK |
| Anatomy | UBERON:0000955 (brain), UBERON:0002113 (kidney), UBERON:0000948 (heart), UBERON:0002048 (lung), UBERON:0000970 (eye) | Moderate-high confidence, standard terms |
| Phenotypes | Seizure (HP:0001250), Cardiac rhabdomyoma, Renal angiomyolipoma, SEGA, Facial angiofibroma, Hypomelanotic macule, Shagreen patch, Ungual fibroma | Verify exact HP IDs via OAK before entry |
| Treatment | Everolimus (CHEBI:68478), Sirolimus/rapamycin (CHEBI:9168), Vigabatrin, Cannabidiol; treatment_term NCIT:C15986 (Pharmacotherapy) | Verify CHEBI IDs via OAK |

---

## Key Citations (PMID/DOI where available)

1. GeneReviews — *Tuberous Sclerosis Complex*, NCBI Bookshelf NBK1220.
2. Northrup H, et al. Updated International Tuberous Sclerosis Complex Diagnostic Criteria and Surveillance and Management Recommendations. *Pediatr Neurol.* 2021. **PMID: 34399110**.
3. Tyburczy ME, et al. Mosaic and Intronic Mutations in TSC1/TSC2 Explain the Majority of TSC Patients with No Mutation Identified by Conventional Testing. *PLoS Genet.* 2015. **PMID: 26540169**.
4. Au KS, et al. (LOH in TSC hamartomas) **PMID: 8824721**; Green AJ, et al. 9q34 LOH in TSC1-associated astrocytoma. **PMID: 7849708**.
5. Franz DN, et al. Long-Term Use of Everolimus in TSC: Final Results from EXIST-1. *PLoS One.* 2016. **PMC4924870**.
6. French JA, et al. Adjunctive everolimus therapy for TSC-associated refractory partial-onset seizures (EXIST-3). **PMID: 31335226**.
7. McCormack FX, et al. Efficacy and Safety of Sirolimus in Lymphangioleiomyomatosis (MILES trial). *N Engl J Med.* 2011. **PMID: 21525617**.
8. de Vries PJ, et al. TAND and the TAND Checklist. **PMID: 25532776**.
9. Feliciano DM, et al. Single-cell Tsc1 knockout during corticogenesis generates tuber-like lesions and reduces seizure threshold in mice. *J Clin Invest.* (JCI article, search-identified).
10. Prohl AK, et al. / Jóźwiak S, et al. — Commentary/analysis of PREVeNT and EPISTOP preventive vigabatrin trials. *Ann Neurol.* 2024.
11. Monoallelic Germline TSC1 Mutations Are Permissive for T Lymphocyte Development and Homeostasis. **PMC3954840**.
12. mTOR inhibitors are the first-choice therapy for renal angiomyolipomas secondary to tuberous sclerosis. 2023. **PMC10726659**.
13. Burden of illness in TSC-associated epilepsy: systematic literature review. **PMC12648938**.
14. Uncovering apparent incomplete penetrance of TSC1/TSC2 variants: implications for newborn screening. *Eur J Hum Genet.* 2026 (search-identified).

**Note on evidence quality:** All facts above are drawn from search-verified secondary/tertiary sources (PubMed/PMC abstracts, GeneReviews, OMIM, published trial summaries) rather than primary full-text extraction in every case. Per this KB's own anti-hallucination SOP, **every PMID and snippet listed here must be independently re-fetched and exact-quote-verified** (`just fetch-reference PMID:XXXX` → `just validate-references`) before being committed as an `EvidenceItem` in a disorder YAML file, and **every ontology term ID must be OAK-verified** before use — this report should be treated as a curation *lead*, not as pre-validated evidence.