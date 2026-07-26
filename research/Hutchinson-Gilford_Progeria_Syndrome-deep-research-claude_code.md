---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-26T13:16:53.345064'
end_time: '2026-07-26T13:22:20.858703'
duration_seconds: 327.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hutchinson-Gilford Progeria Syndrome
  mondo_id: MONDO:0008310
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
  web_search_requests: 17
  num_turns: 18
  total_cost_usd: 1.7204288
  session_id: f9a4f8a6-559e-5875-b202-2cc5a4e70210
  stop_reason: end_turn
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hutchinson-Gilford Progeria Syndrome
- **MONDO ID:** MONDO:0008310 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hutchinson-Gilford Progeria Syndrome** covering all of the
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

# Hutchinson-Gilford Progeria Syndrome (HGPS): Comprehensive Research Report

## 1. Disease Information

**Overview.** Hutchinson-Gilford Progeria Syndrome (HGPS) is an ultra-rare, sporadic, autosomal dominant segmental premature-aging (progeroid) disorder of childhood caused by mutations in *LMNA*, the gene encoding nuclear lamins A and C. Affected children appear normal at birth but by 6–18 months of age begin to show growth failure, alopecia, joint contractures, sclerotic skin changes, and a strikingly aged facial appearance. Death occurs in the early teens (median ~14.6 years), almost always from myocardial infarction or stroke caused by accelerated, generalized atherosclerosis. HGPS is the prototypical human "laminopathy" and has become a major model for understanding both accelerated and normal cellular aging.

**Key identifiers:**
- **MONDO:** MONDO:0008310
- **OMIM:** #176670 (phenotype); *150330 (LMNA gene)
- **Orphanet:** ORPHA:740
- **MeSH:** D058495 (Progeria)
- **ICD-10-CM:** E34.8 (other specified endocrine disorders — no dedicated code exists; often also cross-referenced informally to segmental progeroid syndromes)
- **ICD-11:** listed under rare progeroid syndromes (LD24-group skin/connective tissue rare disease entries; no universally standardized single code — verify locally before use)
- **Gene:** *LMNA* — HGNC:6636, chromosome 1q22, Ensembl ENSG00000160789

**Common synonyms:** Progeria; Progeria syndrome; Hutchinson-Gilford syndrome; HGPS; "Progeria of childhood."

**Evidence source note:** HGPS knowledge derives predominantly from (1) aggregated disease-level clinical registries and cohort natural-history studies (The Progeria Research Foundation International Registry; the NIH-sponsored longitudinal cohort of Gordon, Merideth, and colleagues), (2) individual case reports/series (especially from the original 2003 discovery cohort), and (3) extensive mouse-model (*Lmna^G609G/G609G^*, *Zmpste24^-/-^*) and cell-based mechanistic studies. Unlike common diseases, there is essentially no large-scale EHR-derived epidemiology because the total living patient population is estimated at only ~150–400 individuals worldwide.

Sources: [OMIM #176670](https://www.omim.org/entry/176670); [GeneReviews: Hutchinson-Gilford Progeria Syndrome](https://www.ncbi.nlm.nih.gov/books/NBK1121/); [Orphanet ORPHA:740](https://www.ebi.ac.uk/ols4/ontologies/ordo/terms?iri=http://www.orpha.net/ORDO/Orphanet_740)

---

## 2. Etiology

**Disease causal factor:** HGPS is a monogenic disorder caused, in ~90% of classic cases, by a recurrent *de novo* heterozygous silent point mutation in *LMNA* exon 11: **c.1824C>T (p.Gly608Gly, "G608G")**. This synonymous substitution does not change the encoded amino acid but activates a cryptic splice donor site, causing an internal in-frame deletion of 150 nucleotides (50 amino acids) near the C-terminus of prelamin A. The truncated protein product, **progerin**, retains a permanently farnesylated CAAX-motif cysteine that in wild-type prelamin A is normally removed by ZMPSTE24-mediated proteolytic processing (Eriksson et al., *Nature* 2003, PMID:12714972; De Sandre-Giovannoli et al., *Science* 2003, independently identified the same mutation). A minority of atypical/variant HGPS cases carry other *LMNA* exon 11 mutations that likewise increase use of the cryptic splice site (e.g., c.1968+1G>A and other splice-region variants).

> "18 out of 20 classical cases of HGPS harboured an identical de novo single-base substitution, G608G (GGC>GGT), within exon 11 of the *lamin A* (*LMNA*) gene." (Eriksson et al., 2003)

**Genetic risk factors:**
- The causal variant is essentially always *de novo*; there is no known population-level susceptibility allele.
- **Advanced paternal age** at conception is a documented risk factor for the de novo germline mutation, consistent with the general paternal-age effect seen for other recurrent single-base substitutions arising in spermatogonial mitoses.
- No sex or ethnic predilection has been observed for classic HGPS.

**Environmental risk factors:** None established — HGPS is a purely genetic, non-environmentally modified disorder, though secondary environmental exposures (UV, mechanical stress on stiffened skin/joints) may exacerbate specific phenotypic features rather than cause the disease.

**Protective factors:**
- No genetic protective/modifier variants have been robustly established in humans.
- In mouse models, genetic reduction of mTOR signaling, rapamycin/everolimus treatment, and pharmacologic inhibition of progerin farnesylation (farnesyltransferase inhibitors) partially rescue phenotypes and extend survival — these represent pharmacologic rather than heritable protective factors (Cabral et al., *Aging Cell* 2021, mTOR reduction extends lifespan in HGPS mouse model).

**Gene-environment interactions:** Because progerin production and its farnesylation status are biochemically fixed by the mutation, there is little evidence for meaningful gene-environment interaction modulating penetrance; the near-complete penetrance and stereotyped course argue against major environmental modifiers.

Sources: [Eriksson et al. Nature 2003](https://www.nature.com/articles/nature01629); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1121/); [Cabral et al. Aging Cell 2021](https://onlinelibrary.wiley.com/doi/10.1111/acel.13457)

---

## 3. Phenotypes

HGPS phenotypes span nearly every organ system. Below, phenotypes are grouped by type with onset, severity/progression, frequency, and suggested HPO terms.

### Growth / General
| Phenotype | Onset | Course | Frequency | HPO |
|---|---|---|---|---|
| Postnatal growth retardation / failure to thrive | ~6–12 months | Progressive | Nearly universal | HP:0001510 (Growth delay) / HP:0001518 (Small for gestational age, if congenital) |
| Low weight-for-height, generalized lipodystrophy | Infancy onward | Progressive | Nearly universal | HP:0009125 (Lipoatrophy) |
| Short stature | Childhood | Progressive | Very frequent | HP:0004322 |

### Dermatologic
| Phenotype | Onset | Course | Frequency | HPO |
|---|---|---|---|---|
| Total/near-total alopecia (scalp, eyebrows, eyelashes) | 6–18 months | Progressive | Very frequent (>90%) | HP:0007530 (Total alopecia) / HP:0002293 (Alopecia) |
| Sclerodermatous, tight, aged-appearing skin ("scleroderma-like") | Infancy | Progressive | Very frequent | HP:0100678 (Scleroderma) |
| Prominent cutaneous vasculature | Infancy | Progressive | Frequent | HP:0011276 |
| Mottled hyperpigmentation/dyspigmentation | Childhood | Progressive | Frequent | HP:0001000 (Abnormality of skin pigmentation) |
| Nail dystrophy/hypoplasia | Infancy | Progressive | Very frequent | HP:0008404 (Nail dystrophy) |

### Craniofacial
| Phenotype | Onset | Course | Frequency | HPO |
|---|---|---|---|---|
| Disproportionately large head for face (pseudo-macrocephaly) | Infancy | Stable/progressive | Very frequent | HP:0000256 |
| Prominent scalp veins | Infancy | Progressive | Frequent | HP:0011277 |
| Micrognathia/retrognathia | Infancy | Progressive | Very frequent | HP:0000347 |
| Thin nose with narrow tip ("beaked nose") | Childhood | Progressive | Very frequent | HP:0000426 |
| Delayed/absent tooth eruption, dental crowding | Toddlerhood | Progressive | Very frequent | HP:0000684 / HP:0000691 |
| Prominent eyes / lagophthalmos | Infancy | Progressive | Frequent | HP:0000653 / HP:0000527 |

### Musculoskeletal
| Phenotype | Onset | Course | Frequency | HPO |
|---|---|---|---|---|
| Progressive joint contractures (esp. hips, knees) | Toddlerhood onward | Progressive | Very frequent | HP:0034392 / HP:0001371 |
| Coxa valga, hip dislocation | Childhood | Progressive | Frequent | HP:0002673 |
| Osteolysis (acral, clavicular) | Childhood | Progressive | Frequent | HP:0002797 |
| Osteoporosis / low bone mineral density | Childhood | Progressive | Very frequent | HP:0000939 (conforms to the `osteoporosis_bone_resorption` dismech module) |
| "Horse-riding stance" gait | Toddlerhood | Progressive | Frequent | HP:0033391 (Abnormal gait, broadly) |
| Narrow thorax | Childhood | Progressive | Frequent | HP:0005257 |

### Cardiovascular (dominant cause of mortality)
| Phenotype | Onset | Course | Frequency | HPO |
|---|---|---|---|---|
| Accelerated generalized atherosclerosis | Early childhood (subclinical) | Progressive | Universal by adolescence | HP:0002621 (conforms to `atherogenesis`) |
| Myocardial infarction / coronary artery disease | Adolescence | Terminal event | Leading cause of death | HP:0001677 |
| Stroke / cerebrovascular disease | Adolescence | Terminal event | Common cause of death | HP:0001297 |
| Arterial stiffness, hypertension | Childhood | Progressive | Very frequent | HP:0011106 / HP:0000822 |
| Reduced ejection fraction / diastolic dysfunction | Childhood | Progressive | Frequent | HP:0012664 |

### Other
- **High-pitched voice** — HP:0001620
- **Low-frequency conductive hearing loss** — HP:0000405
- **Dry eyes / exposure keratitis** — HP:0100530
- **Normal cognitive/motor development** — a critical distinguishing negative feature; intelligence is preserved (HP:0000750 explicitly absent — this is a key differential point).

**Progression/course:** Phenotype is progressive and cumulative rather than static, with near-complete penetrance of the core phenotypic gestalt. Severity is broadly stereotyped across patients (low inter-individual variance compared with most Mendelian disorders), though atypical/variant *LMNA* mutations produce milder, later-onset, or asymmetric ("mosaic") phenotypes.

**Quality of life impact:** Joint contractures and hip disease progressively limit mobility; dental crowding/delayed eruption complicates feeding and oral hygiene; skin fragility and lipodystrophy predispose to pressure injury; hearing loss and dry eyes affect communication/comfort. Cognitive and emotional development is normal, so QoL burden is heavily weighted toward physical disability and the psychosocial impact of visible difference and a foreshortened, medically intensive life course; dedicated EQ-5D/SF-36 HGPS-specific QoL instruments are not established in the literature (an evidence gap).

Sources: [Merideth et al., NEJM 2008 "Phenotype and Course of Hutchinson-Gilford Progeria Syndrome"](https://www.nejm.org/doi/full/10.1056/NEJMoa0706898); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1121/); [OMIM Clinical Synopsis #176670](https://omim.org/clinicalSynopsis/176670)

---

## 4. Genetic/Molecular Information

**Causal gene:** *LMNA* (HGNC:6636; OMIM *150330), chr1q22, encoding lamin A and lamin C via alternative splicing of a shared pre-mRNA.

**Pathogenic variant (classic HGPS):**
- **c.1824C>T; p.Gly608Gly** (silent at the protein level for full-length lamin A but pathogenic via cryptic splicing) — accounts for ~90% of clinically diagnosed HGPS.
- Additional/atypical variants: other exon-11 substitutions and splice-region variants (e.g., c.1968+1G>A) that likewise activate/strengthen the same or a nearby cryptic 5′ splice site, producing progerin or progerin-like transcripts, sometimes with different truncation lengths (associated with atypical, often milder, later-onset phenotypes — sometimes termed "atypical Werner syndrome" or "atypical progeroid syndrome" when overlapping with Werner-like features).
- **Variant classification:** Pathogenic per ACMG/AMP criteria (recurrent de novo, functional splicing data, gain-of-toxic-function mechanism); listed in ClinVar under *LMNA*-related progeria.
- **Population frequency:** Effectively absent from gnomAD/1000 Genomes/ExAC/TOPMed reference populations (consistent with near-complete de novo origin and lethality before reproduction — no evolutionary/selective persistence).
- **Origin:** Germline de novo in ~98% of cases; ~2% arise from unaffected parental **germline (gonadal) mosaicism**, raising empiric sibling recurrence risk to roughly 1 in 500 (vs. the population birth incidence of ~1 in 4–8 million) once one affected mosaic-transmitting parent is identified.
- **Functional consequence:** Dominant-negative/toxic gain-of-function — progerin is not merely loss of lamin A function but an actively toxic, permanently farnesylated, membrane-anchored aberrant protein that structurally disrupts the nuclear lamina meshwork (dominant-negative interference with normal lamin A/C and B-type lamin network assembly).

**Modifier genes:** No confirmed human genetic modifiers of HGPS severity have been established; the karyotypically stereotyped phenotype across patients argues for limited modifier-gene effect, though the ratio of progerin:normal lamin A/C transcript (influenced by splicing efficiency) modifies severity, as seen in "neonatal progeria" cases with an unusually high progerin:lamin-A ratio causing a fulminant perinatal-onset phenotype (Reddy & Comai, *EJHG* 2012).

**Epigenetic information:** HGPS cells show global heterochromatin loss — reduced trimethylation of H3K9 (H3K9me3) and H3K27me3, loss of heterochromatin protein 1 (HP1), altered DNA methylation patterns, and a distorted "epigenetic clock" (accelerated Horvath/Hannum methylation age). Phosphorylated Lamin A/C mislocalizes to the nuclear interior and binds active enhancers, driving abnormal transcriptional programs (bioRxiv preprint, Nature-affiliated work on progeria enhancer binding).

**Chromosomal abnormalities:** None — HGPS is a single-nucleotide-variant disorder, not a copy-number/structural chromosomal condition.

**Related genes for the broader laminopathy spectrum (for differential diagnosis/module cross-reference):** *ZMPSTE24* (HGNC:16063, OMIM *606480) — encodes the zinc metalloprotease responsible for the second proteolytic cleavage step maturing prelamin A to lamin A; biallelic loss-of-function mutations cause **Restrictive Dermopathy** (lethal) and **Mandibuloacral Dysplasia type B**, both "secondary laminopathies" mechanistically related to HGPS via farnesylated-prelamin-A accumulation, though — importantly — mouse data show farnesyl-prelamin-A (Zmpste24-null) and progerin (Lmna-G609G) differ in their capacity to cause vascular smooth muscle cell (VSMC) loss, with progerin being uniquely and progressively pathogenic to the vasculature (see Section 6).

**GO/HGNC term suggestions:**
- Gene: hgnc:6636 (LMNA)
- GO:0005637 (nuclear inner membrane), GO:0005652 (nuclear lamina), GO:0016233 (telomere capping), GO:0006357 (regulation of transcription by RNA Pol II)

Sources: [Eriksson et al. Nature 2003, PMID:12714972](https://pubmed.ncbi.nlm.nih.gov/12714972/); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1121/); [Reddy & Comai, EJHG 2012 "Neonatal progeria"](https://www.nature.com/articles/ejhg201236)

---

## 5. Environmental Information

HGPS has **no known environmental, infectious, lifestyle, or toxin-based causal contribution** — it is a purely genetic disorder driven by a recurrent de novo germline point mutation. There is no infectious agent, occupational exposure, dietary factor, or teratogen implicated in disease causation. The only quasi-"environmental" association identified in the literature is **advanced paternal age**, which increases the background rate of de novo germline point mutations generally (including this one), operating through normal spermatogonial mutation accumulation rather than an exogenous exposure.

Secondary environmental modifiers affect symptom management rather than etiology: skin fragility increases vulnerability to pressure injury/trauma; joint contractures and reduced subcutaneous fat increase risk of cold intolerance and skin breakdown; and reduced bone density increases fracture risk with minor trauma.

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:**

1. **Molecular trigger:** *LMNA* c.1824C>T activates a cryptic splice donor in exon 11 → internally truncated prelamin A transcript lacking 150 nt (50 aa), including the second endoproteolytic (ZMPSTE24) cleavage site.
2. **Protein consequence:** The translated protein, **progerin**, undergoes the first (farnesylation) but not the second (defarnesylating cleavage) post-translational maturation step, so it remains **permanently farnesylated** and constitutively membrane-anchored (GO:0018343 protein farnesylation).
3. **Nuclear lamina disruption:** Progerin incorporates into and disrupts the nuclear lamina meshwork (a dominant-negative effect on normal lamin A/C and lamin B networks) → abnormal, "blebbed"/lobulated nuclear morphology, altered nuclear stiffness and mechanotransduction, and nuclear envelope rupture under mechanical stress.
4. **Downstream nuclear consequences:**
   - Loss of peripheral heterochromatin (reduced H3K9me3, H3K27me3, HP1) and altered spatial genome organization (disrupted lamina-associated domains, LADs)
   - Accumulation of unrepaired DNA damage and impaired DNA-damage-response signaling (reduced 53BP1/ATM recruitment efficiency)
   - Telomere dysfunction/shortening and replicative senescence
   - Mislocalization of phosphorylated lamin A/C to active enhancers, driving aberrant transcriptional output
   - Impaired nucleocytoplasmic transport and mitotic defects
5. **Cellular consequences:** Premature cellular senescence (this module overlaps mechanistically with the dismech `cellular_senescence` module — p16INK4a/p21 arrest pathways are activated in HGPS fibroblasts and vascular cells), increased apoptosis under mechanical/oxidative stress, impaired proliferative capacity, and stem/progenitor cell exhaustion.
6. **Tissue/organ consequences — cardiovascular (dominant mortality driver):** In vascular smooth muscle cells (VSMCs), progressive age-dependent progerin accumulation (unlike static farnesyl-prelamin-A in the related Zmpste24-null model) causes **massive VSMC loss** in the aortic media, triggering compensatory but maladaptive remodeling: adventitial fibrosis, extracellular matrix deposition, arterial stiffening, and accelerated atherosclerotic plaque formation — clinically culminating in myocardial infarction and stroke (this pathway conceptually parallels the dismech `atherogenesis` module, substituting progerin-driven VSMC depletion for the classical LDL-retention/foam-cell trigger, and also intersects `thrombogenesis` at the plaque-rupture endpoint).
7. **Other organ systems:** Osteoblast/osteoclast dysregulation and growth-plate abnormalities → osteoporosis/osteolysis (parallels `osteoporosis_bone_resorption`); adipocyte progenitor dysfunction → severe lipodystrophy; dermal fibroblast senescence → sclerodermatous skin change and alopecia via hair-follicle stem cell/dermal papilla dysfunction.

**Molecular pathways (KEGG/Reactome/GO):**
- Nuclear lamina organization: GO:0007084 (mitotic nuclear envelope reassembly), GO:0034399 (nuclear periphery), GO:0000785 (chromatin)
- DNA damage response: GO:0006281 (DNA repair), GO:0000077 (DNA damage checkpoint)
- Farnesylation/isoprenoid pathway (mevalonate pathway) — CHEBI:44468 (farnesyl group), CHEBI:15339 (farnesyl-PP), relevant to farnesyltransferase-inhibitor mechanism (see Treatment)
- mTOR signaling (GO:0031929, TOR signaling) — implicated via autophagy impairment; genetic/pharmacologic mTOR reduction (rapamycin/everolimus) improves autophagic clearance of progerin and extends mouse lifespan.

**Cell types involved (CL terms):**
- CL:0000186 (myofibroblast)/dermal fibroblast (CL:0002620) — sclerodermatous skin
- CL:0000359 (vascular smooth muscle cell, CL:0000359) — progressive loss, central to cardiovascular pathology
- CL:0000058 (chondrocyte) and osteoblast (CL:0000062)/osteoclast (CL:0000092) — skeletal disease
- CL:0000138 (chondrocyte, growth plate) — growth-plate morphology abnormalities
- Endothelial cells (CL:0000115) — impaired mechanoresponse to shear stress, contributing to vascular pathology

**Anatomical/tissue involvement:** See Section 7.

**Single-cell/omics findings:** Single-cell and bulk transcriptomic studies of HGPS fibroblasts and iPSC-derived VSMCs consistently show senescence-associated secretory phenotype (SASP) gene upregulation, dysregulated cell-cycle genes, extracellular matrix remodeling genes, and inflammatory signaling (NF-κB pathway activation) — organ-specific inflammatory/fibrotic transcriptomic signatures have been characterized in the *Lmna^G609G^* mouse across multiple organs (2024 "Inflammation and Fibrosis in Progeria" study).

**Model-organism mechanistic evidence caveat (HUMAN_MODEL_MISMATCH-relevant):** The *Zmpste24^-/-^* mouse (which accumulates farnesylated full-length prelamin A rather than progerin) does **not** reproduce the VSMC-loss/vascular phenotype seen in the *Lmna^G609G^* progerin-expressing model or in human HGPS, despite equivalent nuclear-lamina disruption at the cellular level — indicating that progerin's *specific*, progressively accumulating molecular identity (not merely permanent farnesylation generically) drives the clinically dominant cardiovascular phenotype. This is a mechanistically important human-model fidelity nuance for any pathophysiology curation.

Sources: [Kang et al./Villa-Bellosta lab, "Vascular smooth muscle cell loss underpins accelerated atherosclerosis," PMC6527384](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6527384/); ["The accumulation of progerin underlies the loss of aortic smooth muscle cells," Cell Death & Disease 2025, PMID:40707465](https://pubmed.ncbi.nlm.nih.gov/40707465/); [Frontiers, "Are There Common Mechanisms Between HGPS and Natural Aging?", PMC6529819](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6529819/); [Cabral et al., Aging Cell 2021](https://onlinelibrary.wiley.com/doi/10.1111/acel.13457)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skin/subcutaneous tissue (UBERON:0002097 skin), skeletal system (UBERON:0001434 bone), cardiovascular system (UBERON:0001981 blood vessel; UBERON:0000948 heart), adipose tissue (UBERON:0001013)
- **Secondary/complications:** Central nervous system (stroke secondary to cerebrovascular atherosclerosis — UBERON:0001017 CNS), inner/middle ear (conductive hearing loss — UBERON:0001846 middle ear), eye (lagophthalmos, dry eye — UBERON:0000970 eye), dentition (UBERON:0001091 tooth)
- **Body systems:** Integumentary, musculoskeletal, cardiovascular, and — secondarily — auditory and ophthalmologic systems. Endocrine/metabolic involvement includes lipodystrophy-associated insulin resistance in some patients.

**Tissue/cell level:**
- Dermis and subcutis: dermal fibroblasts, adipocytes (progressive loss)
- Arterial wall (tunica media): vascular smooth muscle cells (progressive depletion), adventitial fibroblasts (compensatory fibrosis)
- Bone: osteoblasts, osteoclasts, growth-plate chondrocytes
- Hair follicle: follicular stem cells/dermal papilla (alopecia)
- Cardiac tissue: cardiomyocytes (secondary structural/functional changes from chronic pressure/ischemia)

**Subcellular level (GO Cellular Component):**
- GO:0005638 (lamin filament) / GO:0005652 (nuclear lamina) — primary site of the molecular lesion
- GO:0005637 (nuclear inner membrane) — progerin's farnesyl-anchored membrane association
- GO:0000785 (chromatin) — heterochromatin loss
- GO:0005657 (replication fork) — replication stress

**Localization:** Systemic/generalized rather than focal — vascular disease is diffuse (coronary, cerebral, and peripheral arteries all affected), skin change is generalized (though most pronounced over the abdomen and extremities), and skeletal disease affects multiple joints (hips, clavicles, distal phalanges) rather than a single site. No meaningful lateralization is reported — the disease is symmetric/bilateral throughout.

---

## 8. Temporal Development

**Onset:** Congenital genetic lesion, but clinically silent at birth; the first recognizable features (growth deceleration, localized scleroderma-like skin change, subtle alopecia) emerge between **6 and 18 months of age** (median age at clinical diagnosis ~19 months, per Orphanet). Onset pattern is **insidious and progressive**, not acute.

**Progression:** Disease has no formal staged classification (unlike, e.g., cancer staging), but natural-history literature describes a continuously progressive course:
- **Early stage (infancy–early childhood):** Growth failure, alopecia onset, early skin changes, subclinical vascular disease begins.
- **Intermediate stage (childhood):** Joint contractures, osteoporosis/osteolysis, characteristic facial gestalt fully established, progressive arterial stiffening and early atherosclerotic changes become detectable by imaging.
- **Advanced/end-stage (adolescence):** Severe generalized atherosclerosis, cardiac dysfunction, and terminal cardiovascular events (myocardial infarction, stroke).

**Progression rate:** Rapid relative to normal human aging — HGPS compresses cardiovascular aging that normally unfolds over 70–80 years into roughly 12–15 years, giving the disease its "accelerated aging" designation, though it is important to note HGPS is a **segmental** progeroid syndrome (not all aging phenotypes are recapitulated — e.g., cognition, cataracts, and cancer risk are largely spared).

**Disease course pattern:** Progressive, non-remitting, non-episodic; there is no spontaneous remission.

**Disease duration:** Chronic and lifelong from clinical onset; median survival is approximately 13–14.6 years (Orphanet cites median life expectancy 13 years; more recent registry data from the treatment era report mean age at death of 14.6 years).

**Critical periods:** Early childhood represents a key intervention window — farnesyltransferase inhibitor therapy is now recommended to begin as early as possible after diagnosis, since vascular disease begins accumulating (subclinically) from early childhood; the base-editing gene-correction mouse work likewise showed maximal benefit when treatment (AAV9-ABE) was given at postnatal day 14, well before overt phenotype onset — suggesting an analogous "early therapeutic window" hypothesis in humans (not yet clinically validated — a `HUMAN_MODEL_MISMATCH`-flaggable translational gap).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Birth incidence:** ~1 in 4 million births (some sources cite 1 in 8 million live births — estimates vary by registry methodology)
- **Point prevalence:** <1 per 1,000,000 (worldwide); ~1 in 20 million living individuals
- **Total known living patients worldwide:** ~150–400 (estimates vary by year/registry ascertainment)

**Inheritance pattern:** Autosomal dominant (HP:0000006), but **de novo** in ~98% of cases — sporadic occurrence, not typically transmitted from an affected parent (survival to reproductive age is essentially never observed without treatment given the severe pre-teen mortality).

**Penetrance:** Complete/high penetrance for the classic phenotype once the pathogenic variant is present.

**Expressivity:** Relatively consistent for the classic G608G mutation; variable and generally milder for atypical splice-site variants (variable expressivity across the LMNA-associated progeroid spectrum).

**Genetic anticipation:** Not applicable — this is not a repeat-expansion disorder.

**Germline mosaicism:** Documented in a small number of families; recurrence risk for parents of an affected child is empirically estimated at up to ~1 in 500 (vs. baseline population risk of ~1 in 4–8 million), reflecting rare parental gonadal/somatic mosaicism for the mutation.

**Founder effects:** None reported — the mutation arises recurrently and independently (a true recurrent de novo mutation hotspot at a CpG-adjacent site), not through a shared ancestral founder haplotype.

**Consanguinity:** Not a relevant risk factor for classic (dominant, de novo) HGPS; may be relevant for the *recessive* related laminopathies (Restrictive Dermopathy, Mandibuloacral Dysplasia type B via ZMPSTE24) which do show consanguinity-associated enrichment.

**Carrier frequency:** Not applicable in the traditional sense (dominant, de novo, non-carrier-screened condition); population allele frequency is essentially zero in reference databases (gnomAD).

**Population demographics:**
- **Affected populations:** Reported across all continents and ethnic groups with no clear predilection; the Progeria Research Foundation registry includes patients from >40 countries.
- **Geographic distribution:** No endemic clustering; cases are sporadic and globally distributed (consistent with recurrent de novo mutation rather than an inherited founder allele).
- **Sex ratio:** Approximately equal (no significant male:female skew reported in large series).
- **Age distribution:** By definition, a pediatric/adolescent disease — nearly all living patients are children, adolescents, or rarely young adults (survival into the third decade is exceptional even with treatment).

Sources: [Orphanet ORPHA:740](https://www.ebi.ac.uk/ols4/ontologies/ordo/terms?iri=http://www.orpha.net/ORDO/Orphanet_740); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1121/)

---

## 10. Diagnostics

**Clinical diagnosis:** HGPS is primarily a **clinical diagnosis** based on the recognizable gestalt (growth failure + alopecia + sclerodermatous skin + characteristic facies + joint contractures), **confirmed by molecular genetic testing**.

**Laboratory tests / biomarkers:**
- Lipid panel (often shows dyslipidemia contributing to atherogenesis)
- Elevated urinary hyaluronic acid has historically been reported as a nonspecific biomarker of connective tissue turnover in some progeroid syndromes (older literature; low specificity)
- No FDA-qualified circulating biomarker of progerin burden is in routine clinical use, though research assays quantifying progerin mRNA/protein in skin fibroblasts or PBMCs are used investigationally as pharmacodynamic trial endpoints.

**Imaging studies:**
- Echocardiography — annual assessment of cardiac function, valve status (aortic stenosis has been specifically reported as a complication requiring intervention), and structural changes.
- Carotid/vascular ultrasound and MRA of head/neck vessels — annual surveillance for arterial narrowing/stroke risk.
- Skeletal radiographs — for osteolysis (acral, clavicular), coxa valga, hip dislocation.
- Cardiac MRI — for detailed structural/functional assessment in specialized centers.
- Dual-energy X-ray absorptiometry (DEXA) — bone mineral density monitoring for osteoporosis.

**Functional tests:**
- Electrocardiogram (annual) — for conduction abnormalities/prolonged QRS.
- Pulse-wave velocity / arterial stiffness measures — increasingly used as a research and clinical surveillance tool for vascular disease progression.

**Genetic testing:**
- **Single-gene sequencing of *LMNA* exon 11** (targeted Sanger sequencing) is the standard confirmatory test, given the recurrent, highly specific c.1824C>T mutation accounting for ~90% of cases.
- Broader **laminopathy/progeroid gene panels** (including *LMNA*, *ZMPSTE24*, *BANF1*, *POLD1*, *WRN*) are used when the phenotype is atypical or when classic HGPS testing is negative.
- **Whole-exome/genome sequencing** is appropriate for atypical presentations without a clear clinical HGPS gestalt, or when panel testing is unrevealing.
- Chromosomal microarray/karyotype are **not** informative for HGPS (single-nucleotide-level lesion) but may be used to exclude alternative differential diagnoses.
- Prenatal/preimplantation genetic testing is available once the familial variant is known (relevant chiefly for families with documented germline mosaicism).

**Clinical diagnostic criteria:** No single validated formal consensus scoring system analogous to Ghent (Marfan) exists in wide clinical use, though the classic gestalt (Merideth et al. 2008; GeneReviews) functions as an informal diagnostic framework: growth failure + alopecia + skin changes + characteristic facies + joint disease, with genetic confirmation required to establish diagnostic certainty and rule out phenocopies.

**Differential diagnosis:** Other progeroid syndromes — Néstor-Guillermo progeria syndrome (*BANF1*), Werner syndrome (*WRN*, adult-onset), Cockayne syndrome, Mandibuloacral Dysplasia, Restrictive Dermopathy, Wiedemann-Rautenstrauch (neonatal progeroid) syndrome, and acrogeria; distinguishing features include age of onset, presence/absence of intellectual disability, and specific skeletal/skin findings.

**Screening:** No population-based newborn screening exists (extreme rarity, no treatable pre-symptomatic window currently validated at scale), though early recognition of the classic gestalt in infancy prompts urgent genetic confirmation given the availability of disease-modifying therapy (lonafarnib).

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1121/); ["Intervention for critical aortic stenosis in HGPS," PMC11079313](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11079313/)

---

## 11. Outcome/Prognosis

**Survival/mortality:**
- **Untreated median survival:** ~13 years (Orphanet); mean age at death historically cited around 13 years, more recent registry cohorts (which include treated patients) report mean age at death of **14.6 years**.
- **Cause of death:** Overwhelmingly cardiovascular — myocardial infarction and stroke secondary to accelerated, generalized atherosclerosis are the leading causes in >75% of deaths.
- **Lonafarnib treatment effect on survival:** In the pivotal JAMA 2018 analysis (Gordon et al., comparing treated vs. untreated cohorts with up to 11 years follow-up), lonafarnib treatment was associated with a **survival benefit of approximately 2.5 years** relative to untreated historical controls.

**Morbidity/functional outcomes:**
- Progressive joint contractures and hip disease cause increasing mobility limitation over the disease course, often necessitating assistive devices, bracing, or surgery.
- Growth failure results in very short stature and low weight persisting throughout life.
- Hearing loss (conductive) and dental crowding/malocclusion contribute to communication and nutritional challenges.
- Cognitive/intellectual development remains normal throughout — a key prognostic distinguishing feature from many other progeroid/neurodevelopmental syndromes.

**Disease course / complications:**
- Aortic/mitral valve calcification and stenosis have been reported as a later complication requiring surgical or transcatheter intervention in some cases.
- Progressive osteolysis (clavicular, acral) and osteoporosis increase fracture risk.
- Recurrent minor infections are not a prominent feature (immune function is largely preserved), distinguishing HGPS from progeroid syndromes with immunodeficiency components.

**Prognostic factors:** Earlier initiation and longer duration of farnesyltransferase-inhibitor therapy correlate with greater survival benefit in registry analyses; degree of baseline vascular stiffness/carotid-femoral pulse-wave velocity at treatment initiation has been explored as a prognostic/pharmacodynamic marker in clinical trials.

Sources: [Gordon LB et al., JAMA 2018 "Association of Lonafarnib Treatment vs No Treatment With Mortality Rate"](https://jamanetwork.com/journals/jama/fullarticle/2679278); [Orphanet ORPHA:740](https://www.ebi.ac.uk/ols4/ontologies/ordo/terms?iri=http://www.orpha.net/ORDO/Orphanet_740)

---

## 12. Treatment

### Pharmacotherapy — Approved
**Lonafarnib (Zokinvy®)** — a **farnesyltransferase inhibitor (FTI)**, FDA-approved **November 2020** — is the only approved disease-modifying therapy, indicated for HGPS and certain processing-deficient progeroid laminopathies in patients ≥1 year old.
- **Mechanism:** Inhibits farnesyltransferase, thereby blocking the initial farnesylation step of prelamin A/progerin maturation, reducing progerin's membrane anchoring and its disruptive incorporation into the nuclear lamina.
- **Efficacy:** Registry-based comparison (Gordon et al., JAMA 2018) showed a ~2.5-year survival benefit with up to 11 years follow-up; earlier trial data (Gordon et al., Circulation 2016 triple-therapy trial, PMID:27400896) established cardiovascular/bone benefit signals.
- **Adverse events:** Nausea, vomiting, diarrhea, increased appetite, fatigue (generally manageable/tolerable in pediatric populations).
- **MAXO/NCIT terms:** treatment_term NCIT:C15986 (Pharmacotherapy); therapeutic_agent CHEBI or NCIT term for lonafarnib (NCIT:C71892 Lonafarnib, if available in local ontology — verify via OAK).

### Pharmacotherapy — Combination trials (historical)
- **Triple therapy (lonafarnib + pravastatin + zoledronic acid):** NCT00879034/NCT00916747 (Gordon et al., Circulation 2016, PMID:27400896) — showed additional bone mineral density benefit from adding pravastatin/zoledronic acid, but **no added cardiovascular benefit** beyond lonafarnib monotherapy, suggesting lonafarnib is the principal survival-driving agent.
- **Lonafarnib + everolimus (rapamycin analog):** Phase 1 (completed 2017) / Phase 2 (completed 2022), 60 children from 27 countries — targets autophagic clearance of progerin as an adjunct mechanism to farnesylation inhibition.

### Advanced/Experimental Therapeutics
- **Gene editing (adenine base editing):** In vivo adenine base editor (ABE) delivered via AAV9 corrected the pathogenic *Lmna* mutation in a mouse model, rescuing vascular pathology and extending median lifespan from 215 to 510 days after a single postnatal-day-14 injection (Koblan/Levy/Liu et al., *Nature* 2021, PMID:33408413) — proof-of-concept for a potential one-time curative gene-correction approach, not yet in human trials.
- **Antisense oligonucleotide (ASO) approaches:** Morpholino ASOs targeting the aberrant exon-11 cryptic splice site have shown preclinical efficacy in reducing progerin production (splice-modulation mechanism analogous to the dismech `antisense_oligonucleotide_therapy` module's splice-redirection paradigm) — preclinical stage.
- **Progerinin:** A small molecule optimized to inhibit progerin-lamin A binding; extended mouse lifespan by 10–14 weeks (more effective than lonafarnib in that model); FDA authorized Phase 2a trial enrollment at Boston Children's Hospital (announced October 2024) — an active experimental therapeutic as of the current reporting window.
- **Isoprenylcysteine carboxylmethyltransferase (ICMT) inhibition:** An alternative post-translational-processing target explored preclinically as a farnesylation-pathway-adjacent strategy.
- **Senolytics (dasatinib, quercetin, fisetin):** Explored in *Zmpste24^-/-^* progeria mouse models; fisetin specifically showed efficacy in attenuating bone degeneration — preclinical, not yet in HGPS human trials.

### Supportive/Rehabilitative Care
- Multidisciplinary management (pediatrics, cardiology, orthopedics, dermatology, dentistry, physical/occupational therapy, nutrition, audiology, ophthalmology).
- **Cardiology surveillance:** Annual echocardiogram, ECG, blood pressure, lipid panel; annual brain MRI/MRA for cerebrovascular narrowing.
- **Physical/occupational therapy:** For joint contractures; bracing or reconstructive hip surgery for hip dislocation (MAXO:0000011 physical therapy; NCIT:C15302).
- **Nutritional support:** High-calorie, nutrient-dense diet given growth failure and lipodystrophy (MAXO:0000088 dietary intervention).
- **Dental care:** Ongoing management of delayed/crowded dentition.
- **Cardiac/vascular intervention:** Case reports describe surgical or transcatheter intervention for critical aortic stenosis when it develops.

### Treatment strategy
Current standard of care is lonafarnib initiated as early as possible after diagnosis, combined with lifelong multidisciplinary supportive/surveillance care; combination and gene-correction/ASO/small-molecule strategies represent the active experimental frontier (registered on ClinicalTrials.gov and via the Progeria Research Foundation's clinical trials program).

Sources: [FDA approval summary, Genetics in Medicine 2022](https://www.gimjournal.org/article/S1098-3600(22)01003-6/fulltext); [Gordon et al., Circulation 2016, PMID:27400896](https://pubmed.ncbi.nlm.nih.gov/27400896/); [Koblan et al., Nature 2021, PMID:33408413](https://pubmed.ncbi.nlm.nih.gov/33408413/); [Progerinin, Communications Biology 2020](https://www.nature.com/articles/s42003-020-01540-w); [BioSpace, Progerinin Phase 2a authorization](https://www.biospace.com/fda/us-fda-authorizes-launch-of-clinical-trial-to-support-new-treatment-development-for-progeria)

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable environmental/lifestyle cause); the only "primary prevention" lever is avoidance of transmission in the rare setting of known parental germline mosaicism, via reproductive options below.

**Secondary prevention (early detection):** Early clinical recognition of the HGPS gestalt in infancy, prompting rapid genetic confirmation, is the key "secondary prevention" strategy — enabling earlier initiation of lonafarnib, which registry data associate with greater survival benefit.

**Tertiary prevention:** Structured multidisciplinary surveillance (annual cardiology, vascular imaging, DEXA, dental, audiology, ophthalmology assessments — see Section 12) aims to prevent/delay complications (stroke, critical valve stenosis, fracture) rather than the underlying disease process.

**Genetic counseling:** Central to family management — given the ~98% de novo origin, recurrence risk for parents of an affected child is population-level low, but the possibility of germline mosaicism (empiric recurrence risk up to ~1 in 500) warrants offering **prenatal diagnosis or preimplantation genetic testing (PGT)** once the familial *LMNA* variant is confirmed, particularly for future pregnancies in families with an affected child.

**Screening programs:** No newborn or population genetic screening program exists for HGPS given its extreme rarity and current lack of a presymptomatic-detection-driven early-intervention protocol validated at a population level.

**Immunization:** Not disease-specific; standard pediatric immunization schedules apply (immune competence is preserved in HGPS).

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring HGPS-equivalent disease has been documented in non-human species (NCBI Taxon Homo sapiens: NCBITaxon:9606). Unlike some Mendelian disorders with veterinary natural-disease counterparts (e.g., in dogs), HGPS is not known to occur spontaneously in companion animals or wildlife.

**Orthologous gene:** *Lmna* is highly conserved across mammals (mouse *Lmna*: MGI:96799; NCBI Gene). The equivalent murine mutation (c.1827C>T; p.Gly609Gly, "G609G") has been engineered as a knock-in model (see Section 15) rather than arising naturally.

**Comparative biology:** The lamin A processing pathway (farnesylation → ZMPSTE24 cleavage → mature lamin A) is conserved from mammals broadly; the fundamental biology of progerin toxicity (nuclear lamina disruption, heterochromatin loss, senescence induction) is evolutionarily conserved and recapitulated across engineered mouse, and to a lesser degree engineered zebrafish/*C. elegans*, systems — though no species has a naturally occurring/spontaneous equivalent.

**Zoonotic potential:** Not applicable — HGPS is a non-transmissible genetic disorder.

---

## 15. Model Organisms

**Mouse models (the dominant HGPS model system):**

1. **Lmna^G609G^ knock-in mouse** (equivalent to human c.1824C>T/G608G) — the flagship, most widely used HGPS model.
   - **Heterozygous (Lmna^G609G/+^):** Normal until ~24 weeks, then progressive progeroid phenotype, death at a mean age of ~35 weeks — models a milder/slower disease course.
   - **Homozygous (Lmna^G609G/G609G^):** More severe/earlier phenotype — osteoporosis, loss of fat depots, VSMC depletion, aberrant hormonal profiles (hypoglycemia), death at 14–15 weeks.
   - **Cardiovascular recapitulation:** Prolonged QRS intervals, progressive VSMC loss, arterial stiffening, reduced ejection fraction/fractional shortening, diastolic dysfunction — closely mirrors the dominant human cardiovascular mortality driver.
   - **Musculoskeletal recapitulation:** Decreased isometric tetanic torque, muscle atrophy, fibrosis; altered growth-plate morphology (though normal bone matrix mineralization has been specifically noted as a point of partial non-recapitulation in some sub-analyses — a nuance for translational fidelity assessment).

2. **G608G BAC transgenic mouse** — expresses the human mutant *LMNA* transgene; shows cardiac and skeletal muscle manifestations analogous to human disease (Hong et al., Aging Cell 2024).

3. **Zmpste24^-/-^ knockout mouse** — models the related "secondary laminopathy" mechanism (farnesyl-prelamin-A accumulation from failure of the second processing cleavage, rather than progerin production per se). Useful for isolating the farnesylation/lamina-disruption mechanism from progerin-specific pathology; notably this model does **not** reproduce the VSMC-loss/vascular phenotype to the same degree as the progerin-expressing G609G model even at later ages, an important **model-fidelity distinction** (a candidate `HUMAN_MODEL_MISMATCH` flag if used to model human HGPS vascular disease specifically).

4. **Genetic/pharmacologic intervention models:** mTOR-reduction (genetic or rapamycin/everolimus) crosses with the G609G model extend lifespan (Cabral et al., Aging Cell 2021); AAV9-delivered adenine base editor treatment of G609G-model mice (Koblan et al., Nature 2021) achieved the most dramatic lifespan extension reported to date (215→510 days median).

**Cellular/in vitro models:**
- Patient-derived dermal fibroblasts (the original and still most widely used HGPS cellular model) — recapitulate dysmorphic nuclei, heat-stress hypersensitivity, senescence markers.
- iPSC-derived vascular smooth muscle cells and endothelial cells from HGPS patients — used to study progerin's cell-autonomous effects on vascular mechanobiology (e.g., impaired adaptation to shear stress).
- CRISPR-engineered isogenic cell lines carrying the G608G mutation — used for mechanistic dissection and drug-screening.

**Applications:** Mouse and cellular models have been essential for (a) establishing the vascular smooth muscle cell loss mechanism, (b) preclinical testing of farnesyltransferase inhibitors, mTOR inhibitors, progerinin, ASOs, and base-editing gene correction, and (c) exploring the progerin/normal-aging mechanistic overlap hypothesis.

**Limitations:** Mouse models generally show a compressed but qualitatively similar disease course; some human-specific features (e.g., precise skeletal dysplasia patterns, dental phenotype) are imperfectly or only partially recapitulated, and — as above — the specific choice between progerin-expressing (G609G) vs. farnesyl-prelamin-A-accumulating (Zmpste24-null) models materially changes which phenotypes (especially vascular) are captured, an important caveat for interpreting any single model's translational relevance.

**Resources:** MGI (Mouse Genome Informatics) records for *Lmna*; the Progeria Research Foundation maintains a Cell and Tissue Bank distributing patient-derived fibroblast lines to researchers.

Sources: ["Long term breeding of the Lmna G609G progeric mouse," PMID:31794853](https://pubmed.ncbi.nlm.nih.gov/31794853/); [Hong et al., Aging Cell 2024](https://onlinelibrary.wiley.com/doi/10.1111/acel.14259); ["Vascular smooth muscle cell loss underpins accelerated atherosclerosis in HGPS," PMC6527384](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6527384/); [Cabral et al., Aging Cell 2021](https://onlinelibrary.wiley.com/doi/10.1111/acel.13457)

---

## Summary Ontology Term Quick-Reference

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0008310; OMIM:176670; ORPHA:740 |
| Gene | hgnc:6636 (LMNA); hgnc:16063 (ZMPSTE24, related laminopathies) |
| Key phenotypes (HP) | HP:0007530 (alopecia), HP:0100678 (scleroderma), HP:0009125 (lipoatrophy), HP:0002621 (atherosclerosis), HP:0000939 (osteoporosis), HP:0008404 (nail dystrophy), HP:0000256 (macrocephaly relative to face), HP:0000347 (micrognathia) |
| Biological processes (GO) | GO:0018343 (protein farnesylation), GO:0007084 (mitotic nuclear envelope reassembly), GO:0006281 (DNA repair) |
| Cellular component (GO:CC) | GO:0005652 (nuclear lamina), GO:0005637 (nuclear inner membrane) |
| Cell types (CL) | CL:0000359 (vascular smooth muscle cell), CL:0002620 (dermal fibroblast), CL:0000062 (osteoblast) |
| Anatomy (UBERON) | UBERON:0001981 (blood vessel), UBERON:0002097 (skin), UBERON:0001434 (bone) |
| Chemical (CHEBI) | CHEBI:44468 (farnesyl group) |
| Treatment (MAXO/NCIT) | NCIT:C15986 (Pharmacotherapy; lonafarnib); MAXO:0000011 (physical therapy); MAXO:0000088 (dietary intervention) |
| Module cross-references (dismech) | `atherogenesis`, `osteoporosis_bone_resorption`, `cellular_senescence`, `antisense_oligonucleotide_therapy` (for the ASO experimental therapeutic arm) |

---

## Key Evidence Citations (PMID/DOI)

- Eriksson M, et al. "Recurrent de novo point mutations in lamin A cause Hutchinson–Gilford progeria syndrome." *Nature* 2003;423:293–298. PMID:12714972
- Merideth MA, et al. "Phenotype and Course of Hutchinson–Gilford Progeria Syndrome." *N Engl J Med* 2008;358:592–604.
- Gordon LB, et al. "Clinical Trial of the Protein Farnesylation Inhibitors Lonafarnib, Pravastatin, and Zoledronic Acid in Children With Hutchinson-Gilford Progeria Syndrome." *Circulation* 2016. PMID:27400896
- Gordon LB, et al. "Association of Lonafarnib Treatment vs No Treatment With Mortality Rate in Patients With Hutchinson-Gilford Progeria Syndrome." *JAMA* 2018;319(16):1687–1695.
- Koblan LW, et al. "In vivo base editing rescues Hutchinson–Gilford progeria syndrome in mice." *Nature* 2021;589:608–614. PMID:33408413
- Cabral WA, et al. "Genetic reduction of mTOR extends lifespan in a mouse model of Hutchinson-Gilford Progeria syndrome." *Aging Cell* 2021. PMID:34519171 (verify)
- "The accumulation of progerin underlies the loss of aortic smooth muscle cells in Hutchinson-Gilford progeria syndrome." *Cell Death & Disease* 2025. PMID:40707465
- Reddy S, Comai L. "Neonatal progeria: increased ratio of progerin to lamin A leads to progeria of the newborn." *Eur J Hum Genet* 2012.

---

## Sources

- [OMIM #176670 — Hutchinson-Gilford Progeria Syndrome](https://www.omim.org/entry/176670)
- [OMIM Clinical Synopsis #176670](https://omim.org/clinicalSynopsis/176670)
- [GeneReviews: Hutchinson-Gilford Progeria Syndrome](https://www.ncbi.nlm.nih.gov/books/NBK1121/)
- [Orphanet ORPHA:740](https://www.ebi.ac.uk/ols4/ontologies/ordo/terms?iri=http://www.orpha.net/ORDO/Orphanet_740)
- [Eriksson et al., Nature 2003](https://www.nature.com/articles/nature01629) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/12714972/)
- [Merideth et al., NEJM 2008](https://www.nejm.org/doi/full/10.1056/NEJMoa0706898)
- [Gordon et al., Circulation 2016](https://www.ahajournals.org/doi/10.1161/circulationaha.116.022188) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/27400896/)
- [Gordon et al., JAMA 2018 (full article)](https://jamanetwork.com/journals/jama/fullarticle/2679278)
- [FDA approval summary for lonafarnib (Zokinvy), Genetics in Medicine 2022](https://www.gimjournal.org/article/S1098-3600(22)01003-6/fulltext)
- [Koblan et al., Nature 2021 (base editing)](https://www.nature.com/articles/s41586-020-03086-7) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/33408413/)
- [Vascular smooth muscle cell loss underpins accelerated atherosclerosis in HGPS, PMC6527384](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6527384/)
- [The accumulation of progerin underlies loss of aortic smooth muscle cells, PMC12290114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12290114/)
- [Are There Common Mechanisms Between HGPS and Natural Aging?, PMC6529819](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6529819/)
- [Cabral et al., Aging Cell 2021 (mTOR reduction)](https://onlinelibrary.wiley.com/doi/10.1111/acel.13457)
- [Hong et al., Aging Cell 2024 (G608G mouse cardiac/skeletal muscle)](https://onlinelibrary.wiley.com/doi/10.1111/acel.14259)
- [Long term breeding of the Lmna G609G progeric mouse, PubMed](https://pubmed.ncbi.nlm.nih.gov/31794853/?dopt=Abstract)
- [Progerinin, Communications Biology 2020](https://www.nature.com/articles/s42003-020-01540-w)
- [BioSpace: FDA authorizes Progerinin Phase 2a trial](https://www.biospace.com/fda/us-fda-authorizes-launch-of-clinical-trial-to-support-new-treatment-development-for-progeria)
- [Reddy & Comai, Neonatal progeria, EJHG 2012](https://www.nature.com/articles/ejhg201236)
- [Intervention for critical aortic stenosis in HGPS, PMC11079313](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11079313/)
- [Progeroid laminopathy with restrictive dermopathy-like features (LMNA p.R435C), PMC3824411](https://pmc.ncbi.nlm.nih.gov/articles/PMC3824411/)
- [National survey of HGPS and progeroid laminopathy in Japan, PMC12339027](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12339027/)

*Note: A small number of PMIDs above (marked "verify") are best-effort citations from general literature knowledge rather than confirmed via this session's searches; before using any specific PMID/snippet in a dismech KB entry, follow the project's mandatory verification workflow (`just fetch-reference PMID:XXXX` + `just validate-references`) rather than relying on this report's citations directly.*