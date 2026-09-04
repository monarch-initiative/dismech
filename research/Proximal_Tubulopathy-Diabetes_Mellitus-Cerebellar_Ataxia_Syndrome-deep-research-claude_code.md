---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-18T18:38:42.434576'
end_time: '2026-08-18T18:42:45.638454'
duration_seconds: 243.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Proximal tubulopathy-diabetes mellitus-cerebellar ataxia syndrome
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
  web_search_requests: 10
  num_turns: 19
  total_cost_usd: 1.7060714999999997
  session_id: 4cafed56-1dee-50a6-8700-1ce935b1df93
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 17
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Proximal tubulopathy-diabetes mellitus-cerebellar ataxia syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Proximal tubulopathy-diabetes mellitus-cerebellar ataxia syndrome** covering all of the
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

# Research Report: Proximal Tubulopathy-Diabetes Mellitus-Cerebellar Ataxia Syndrome

## Important Framing Note

This is an **ultra-rare, essentially single-family disease entity**. The entire primary literature basis for this syndrome is one 1992 case report describing two sisters (Rötig, Colonna, Bonnefont, et al., *Am J Hum Genet* 1992) [PMID:1531167]. No additional independently-reported families with this exact phenotype–genotype combination were identified in this search. Because of this, most of the "characteristics" below are drawn directly from that single report, supplemented by (a) general mechanistic knowledge of mitochondrial DNA (mtDNA) rearrangement disorders (Kearns-Sayre syndrome/Pearson syndrome spectrum, which this entity is nosologically grouped with) and (b) general pathophysiology of mitochondrial proximal renal tubulopathy, mitochondrial diabetes, and mitochondrial cerebellar degeneration, which is **extrapolated, not disease-specific evidence**. This distinction is flagged throughout.

---

## 1. Disease Information

**Overview:** Proximal tubulopathy-diabetes mellitus-cerebellar ataxia syndrome is a multisystem mitochondrial disorder presenting in infancy with a severe proximal renal tubulopathy (Fanconi-type), followed during childhood by progressive development of skin pigmentary changes, mitochondrial myopathy (ragged-red fibers), cerebellar ataxia, sensorineural hearing loss, pigmentary retinopathy/blindness, osteoporosis, and diabetes mellitus. It is caused by a **maternally inherited, heteroplasmic partial duplication of mitochondrial DNA**, and mitochondrial respiratory chain analysis has demonstrated **complex III (ubiquinol-cytochrome c reductase) deficiency** in affected tissue (skeletal muscle and lymphocytes) [PMID:1531167].

**Key identifiers:**
- **OMIM:** #560000 — "RENAL TUBULOPATHY, DIABETES MELLITUS, AND CEREBELLAR ATAXIA" (https://omim.org/entry/560000)
- **Orphanet:** ORPHA:3390 (https://www.orpha.net/en/disease/detail/3390)
- **MONDO:** MONDO:0010798
- **MedGen/UMLS:** UID 463309 / CUI C3151959 (https://www.ncbi.nlm.nih.gov/medgen/463309)
- **ICD-10/11:** No dedicated code identified; would fall under mitochondrial disease / E88.4x-adjacent or N-codes for tubulopathy depending on coding system used (not independently confirmed in this search).

**Synonyms:** Renal tubulopathy, diabetes mellitus, and cerebellar ataxia; RTDMCA (informal).

**Source of information:** This entry is derived from a single aggregated case report of two affected siblings (not EHR-derived, not a registry) — i.e., **disease-level literature description of an individual pedigree**, not population-level epidemiology.

---

## 2. Etiology

**Disease causal factor:** A **heteroplasmic, maternally transmitted partial duplication of the mitochondrial genome** (~26 kb), consisting of one full-length mitochondrial genome plus one partially deleted genome, joined at a single abnormal junction located between the genes encoding **ATP synthase subunit 6 (MT-ATP6)** and **cytochrome b (MT-CYB)** [PMID:1531167]. Southern blot analysis demonstrated this rearrangement in the proband tissues; PCR of maternal lymphocyte DNA detected trace amounts of the same duplicated species, establishing **maternal transmission** — this was reported as "the first example of a maternally inherited duplication of the mitochondrial genome in man" [PMID:1531167].

**Genetic risk factors:**
- Maternal carriage of the heteroplasmic mtDNA duplication (even at very low, PCR-detectable heteroplasmy levels in blood) is the sole documented risk factor.
- As with other heteroplasmic mtDNA rearrangement disorders, the degree of heteroplasmy and its tissue distribution (mitotic segregation) likely determines phenotypic severity and tissue involvement, though this was not directly quantified across tissues in the original report.
- No nuclear modifier genes have been described for this specific entity.

**Environmental risk factors:** None specifically reported for this syndrome. By extrapolation from mitochondrial disease biology generally, catabolic stress (intercurrent illness, fasting, dehydration) can precipitate metabolic decompensation in patients with underlying OXPHOS defects — consistent with the fact that both sisters in the index family had life-threatening deteriorations during episodes of diarrhea/vomiting/dehydration [PMID:1531167].

**Protective factors:** None identified in the literature search.

**Gene-environment interactions:** Not established for this entity specifically.

---

## 3. Phenotypes

The following phenotype list synthesizes the OMIM/MedGen/Orphanet-curated description, all traceable to the original 2-sibling report [PMID:1531167].

### Renal / Metabolic (earliest-onset)
| Phenotype | HPO suggestion | Onset | Notes |
|---|---|---|---|
| Proximal (Fanconi-type) renal tubulopathy | HP:0000114 (Proximal tubulopathy) | First year of life | Polyuria with renal loss of potassium, sodium, calcium, and chloride |
| Polyuria | HP:0000103 | Infancy | Secondary to tubular wasting |
| Failure to thrive | HP:0001508 | Infancy | Presenting feature |
| Dehydration (recurrent, severe) | HP:0001944 | Childhood | Precipitated by intercurrent GI illness; fatal in the older sister at age 5 |
| Diarrhea / vomiting | HP:0002014 / HP:0002013 | Childhood | Triggered acute decompensation episodes |
| Hepatomegaly | HP:0002240 | Variable | Listed in MedGen-derived HPO set |
| Rickets / Osteoporosis | HP:0002748 / HP:0000939 | Childhood | Bone disease developing with disease progression |

### Endocrine
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Diabetes mellitus (insulin-dependent pattern reported) | HP:0000857 (Genetic diabetes mellitus) / HP:0100651 (Type I diabetes mellitus, as tagged in MedGen) | Developed later in disease course as part of the multisystem progression |

### Neurological
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Cerebellar ataxia | HP:0001251 | Progressive; developed during childhood |
| Hypotonia | HP:0001252 | Associated finding |
| Myoclonus | HP:0001336 | Listed in curated HPO set |
| Developmental regression | HP:0002376 | Listed in curated HPO set |
| Extraocular muscle palsy / ophthalmoparesis | HP:0000602 | Second sister developed this in later course |
| Ptosis | HP:0000508 | Second sister; also present in the mother (heteroplasmic carrier) |

### Ophthalmologic
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Pigmentary retinopathy | HP:0000580 | Second sister |
| Extinguished/undetectable electroretinogram | HP:0000512-adjacent (abnormal ERG) | Objective correlate of retinal degeneration |
| Blindness | HP:0000618 | End-stage visual loss |

### Dermatologic
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Mottled pigmentation of photo-exposed skin (erythrocyanosis, abnormal pigmentation) | HP:0007441 (Mottled pigmentation) or HP:0000953 (Hyperpigmentation) | Progressive skin finding |

### Musculoskeletal / Neuromuscular
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Mitochondrial myopathy with ragged-red fibers | HP:0003200 (Ragged-red muscle fibers) | Documented on muscle biopsy |

### Auditory
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Sensorineural hearing loss / deafness | HP:0000407 | Listed among the progressive multisystem features |

### Maternal carrier phenotype
The unaffected/mildly affected mother, who carried trace heteroplasmic levels of the duplication, exhibited **ptosis, ophthalmoplegia, and muscle weakness** [PMID:1531167] — a mild PEO-like phenotype consistent with low mutant load.

**Severity/progression:** Markedly severe and progressive; the older sister died of an acute dehydration episode at age 5, and the younger sister survived an early severe episode at age 3 but went on to accumulate ophthalmologic, retinal, and neurologic deficits. **This indicates a severe, life-limiting, progressive multisystem course with a narrow window of survival through early decompensation events.**

**Quality of life impact:** Not formally studied (no QOL instrument data identified); qualitatively, the disease is severely disabling and historically fatal in early-to-mid childhood based on the index cases.

---

## 4. Genetic/Molecular Information

**Causal genetic lesion:** Heteroplasmic **mtDNA duplication** (~26 kb), not a point mutation or single-gene nuclear variant. This is fundamentally different from most Mendelian dismech-style entries: the "gene" involved is the mitochondrial genome itself, with a single abnormal recombination/junction breakpoint located between **MT-ATP6** (ATP synthase F0 subunit 6) and **MT-CYB** (cytochrome b, complex III core catalytic subunit) [PMID:1531167].

- **Affected loci:** MT-ATP6 (mitochondrially encoded, part of Complex V) and MT-CYB (mitochondrially encoded, catalytic core subunit of Complex III) flank the duplication junction. The duplication itself spans most of the mitochondrial genome (one full-length copy plus a partially-deleted copy).
- **Variant classification:** Not applicable in ACMG/AMP terms (structural mtDNA rearrangement, not a SNV); functionally analogous to a large structural mtDNA variant.
- **Heteroplasmy:** The duplication is heteroplasmic — present at high levels in affected tissue (muscle, presumably kidney) and at very low, PCR-only-detectable levels in maternal lymphocytes, consistent with mitotic/tissue segregation of heteroplasmy typical of mtDNA rearrangement disorders.
- **Allele frequency in population databases:** Not applicable — this is a private, family-specific structural mtDNA rearrangement, not a population polymorphism; not expected to appear in gnomAD/mtDNA reference sets.
- **Somatic vs. germline origin:** Germline (maternally transmitted), demonstrated by detection of the duplicated species in the mother's lymphocyte DNA — but note that mtDNA duplications/deletions can also arise **de novo** in oocytogenesis in many other reported cases of mtDNA rearrangement syndromes (general mtDNA-disease knowledge, not specific to this pedigree).
- **Functional consequence:** The duplication is associated with **complex III (ubiquinol–cytochrome c oxidoreductase) deficiency**, documented biochemically in skeletal muscle and lymphocytes from the second sister [PMID:1531167]. This represents impaired oxidative phosphorylation (OXPHOS) capacity.

**Modifier genes/factors:** None specifically described. General mtDNA-disease principle: heteroplasmy level and tissue-specific segregation are the major modifiers of phenotype in mtDNA rearrangement disorders (extrapolated, not shown directly for this family beyond the mother/daughters difference).

**Epigenetic information:** Not reported/applicable for this entity.

**Chromosomal abnormalities:** Not applicable (mitochondrial genome rearrangement, not nuclear chromosomal).

**Relationship to other mtDNA rearrangement syndromes:** This entity is nosologically related to the broader family of **single large-scale mtDNA rearrangement syndromes** (Kearns-Sayre syndrome, Pearson marrow-pancreas syndrome, chronic progressive external ophthalmoplegia/CPEO) — see GeneReviews "Single Large-Scale Mitochondrial DNA Deletion Syndromes" (NCBI Bookshelf NBK1203, last updated 2023). While *deletions* are the classic and usually sporadic lesion in that spectrum, **duplications** are less common, can be **maternally inherited** (unlike most single deletions, which are typically sporadic de novo events), and have been reported to co-occur with deletions in some patients. Renal tubulopathy, cerebellar ataxia, diabetes mellitus, and PEO/deafness are all recognized phenotypes across this broader mtDNA rearrangement spectrum (general mtDNA-rearrangement literature, e.g., Poulton et al., "Duplications of mitochondrial DNA: implications for pathogenesis," *J Inherit Metab Dis* 1992).

---

## 5. Environmental Information

No disease-specific environmental, occupational, or toxin exposures were identified as causal or modifying for this syndrome. **Infectious/GI illness as a precipitant of acute decompensation** is documented directly in the index cases (both sisters had severe deteriorations in the setting of diarrhea/vomiting/dehydration) [PMID:1531167] — this is best framed as a **catabolic-stress trigger for acute metabolic crisis** rather than a causal environmental factor, analogous to the general principle in mitochondrial and metabolic disease that intercurrent illness unmasks/worsens the underlying bioenergetic defect.

No infectious agents are causally implicated in the underlying disease process itself.

---

## 6. Mechanism / Pathophysiology

**Causal chain (as supported by direct and extrapolated evidence):**

1. **Trigger/initiating lesion:** Heteroplasmic mtDNA duplication (MT-ATP6/MT-CYB junction) inherited maternally or arising in oogenesis [PMID:1531167].
2. **Molecular consequence:** Disrupted assembly/function of the mitochondrial respiratory chain — specifically documented **Complex III (ubiquinol-cytochrome c reductase) deficiency** in muscle and lymphocytes [PMID:1531167]. (GO: mitochondrial respiratory chain complex III assembly, GO:0017062; GO: mitochondrial electron transport, ubiquinol to cytochrome c, GO:0006122)
3. **Cellular consequence:** Impaired oxidative phosphorylation → reduced ATP generation, particularly in tissues with high energetic demand and reliance on aerobic metabolism.
4. **Tissue-level consequences (organ-specific downstream effects):**
   - **Proximal renal tubule (S3 segment):** The proximal tubule performs highly energy-intensive active reabsorption of glucose, amino acids, low-molecular-weight proteins, and electrolytes; the S3 segment in particular cannot rely on anaerobic glycolysis due to relative paucity of glycolytic enzymes, making it exquisitely vulnerable to OXPHOS failure. This produces a **generalized Fanconi-type proximal tubulopathy** (glucosuria, aminoaciduria, phosphaturia, bicarbonaturia/acidosis, low-molecular-weight proteinuria, and, in this syndrome, wasting of potassium, sodium, calcium, and chloride). This mechanism is well established for mitochondrial cytopathies broadly (e.g., BCS1L-related complex III deficiency causing Fanconi syndrome, *J Hum Genet* 2021; complex I-related Fanconi syndrome, *PMC3872385*) and is consistent with, though not separately biochemically dissected at the renal tissue level in, the original report.
   - **Pancreatic islet β-cells:** High ATP-dependence for glucose-stimulated insulin secretion (via ATP-sensitive K+ channel closure) makes β-cells vulnerable to OXPHOS defects, producing progressive insulin-secretory failure and **mitochondrial diabetes mellitus**. This is the general mechanism invoked for mtDNA-related diabetes (e.g., m.3243A>G MIDD) and is extrapolated to this entity given the shared bioenergetic defect; not independently proven in this pedigree.
   - **Cerebellum (Purkinje cells):** Purkinje neurons show disproportionate vulnerability to OXPHOS/complex deficiency in primary mitochondrial disease, with selective Purkinje cell loss and OXPHOS protein deficiency documented in post-mortem mitochondrial-disease cerebellar tissue exceeding that in granule cells or dentate neurons (PMC12125081, 2025). This provides a plausible mechanistic basis for the **progressive cerebellar ataxia** in this syndrome, though again this is general mitochondrial-cerebellar-disease mechanism rather than tissue-specific data from the index family.
   - **Retina (photoreceptors/RPE):** High mitochondrial density and metabolic demand of photoreceptors underlies the pigmentary retinopathy and extinguished ERG.
   - **Skeletal muscle:** Ragged-red fibers on biopsy reflect subsarcolemmal mitochondrial proliferation, a classic histopathological marker of mtDNA rearrangement disease.
   - **Skin:** Pigmentary changes in photo-exposed areas — mechanism not detailed in the literature reviewed; possibly reflects generalized bioenergetic/oxidative stress effects on melanocytes, by analogy with other mitochondrial cytopathy skin phenotypes (*J Am Acad Dermatol* mtDNA syndromes review).
   - **Bone:** Osteoporosis/rickets likely multifactorial — secondary renal phosphate/calcium wasting (renal osteodystrophy-like mechanism) compounding any direct bioenergetic bone effect.

5. **Systemic decompensation:** Superimposed catabolic stress (GI illness, dehydration) in a patient with chronically compromised renal and systemic energy reserve precipitates acute, life-threatening metabolic crises — the proximate cause of death in the index family's older sibling.

**Suggested ontology terms:**
- GO biological process: GO:0006122 (mitochondrial electron transport, ubiquinol to cytochrome c); GO:0042775 (mitochondrial ATP synthesis coupled electron transport); GO:0090207 (regulation of triglyceride metabolic process — n/a); more relevantly GO:0032543 (mitochondrial translation, if duplication affects gene dosage/translation).
- Cell types (CL): CL:1000838 (kidney proximal straight tubule epithelial cell), CL:0000169 (type B pancreatic cell), CL:0000121 (Purkinje cell), CL:0000210 (photoreceptor cell), CL:0000187 (myocyte).
- UBERON: UBERON:0004134 (renal proximal convoluted tubule)/UBERON:0004203 (proximal straight tubule), UBERON:0000006 (islet of Langerhans), UBERON:0002037 (cerebellum), UBERON:0000966 (retina).
- GO cellular component: GO:0005750 (mitochondrial respiratory chain complex III), GO:0005743 (mitochondrial inner membrane).

**Advanced/omics data:** No transcriptomic, proteomic, metabolomic, single-cell, or spatial data specific to this syndrome were identified — consistent with its status as a single historically-reported family predating the omics era (report published 1992).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Kidney (proximal tubule), pancreas (endocrine), cerebellum, skeletal muscle, retina/eye, inner ear, skin, bone.
- **Body systems:** Renal, endocrine, nervous (central — cerebellum; also cranial nerve/extraocular muscle involvement), musculoskeletal, integumentary, sensory (visual, auditory).

**Tissue/cell level:**
- Renal proximal tubular epithelium (S1–S3 segments)
- Pancreatic islet β-cells (endocrine)
- Cerebellar Purkinje cells and associated cerebellar cortical neurons
- Skeletal myofibers (ragged-red fiber pathology reflects subsarcolemmal mitochondrial accumulation)
- Retinal photoreceptors/pigment epithelium
- Cochlear/inner ear sensory epithelium (for hearing loss)
- Epidermal melanocytes/keratinocytes (photo-exposed skin pigmentation)

**Subcellular level:**
- Mitochondrial inner membrane respiratory chain complex III (GO:0005750) — primary biochemical lesion site
- Mitochondrial matrix/genome (site of the duplication itself)

**Localization/laterality:** Systemic/bilateral, non-lateralized — consistent with a maternally-inherited mtDNA lesion affecting multiple organs simultaneously rather than a focal structural process.

---

## 8. Temporal Development

- **Onset:** Congenital/early infantile. Proximal tubulopathy manifests **in the first year of life** [PMID:1531167] — the earliest and defining presenting feature.
- **Onset pattern:** Insidious renal onset (failure to thrive, polyuria) followed by an accumulating, progressive multisystem course through childhood.
- **Progression:** Progressive and severe. Skin changes, cerebellar ataxia, myopathy, deafness, retinopathy, and diabetes mellitus accrue sequentially "during childhood" per the OMIM/MedGen synthesis.
- **Disease course pattern:** Chronic-progressive with **acute, potentially fatal decompensation episodes** superimposed (triggered by intercurrent GI illness/dehydration) — the older sister died during such an episode at age 5; the younger sister survived a similar episode at age 3 but continued to accrue chronic multisystem deficits afterward.
- **Critical periods:** Infancy (first year of life) represents the critical window for renal disease onset; early childhood (ages 3–5) represents a period of high mortality risk from acute metabolic/dehydration crises.
- **Remission:** No spontaneous or treatment-induced remission described; this is a progressive, non-remitting mitochondrial disease.

---

## 9. Inheritance and Population

**Epidemiology:** No formal prevalence or incidence estimates exist. This is described in the literature as based on a **single reported family (two affected sisters)**, making it one of the rarest entities in the mitochondrial-disease nosology — effectively a "cases in literature" count of 2 (plus a mildly-affected obligate carrier mother). Orphanet classifies it as an ultra-rare disorder.

**Inheritance pattern:** **Maternal (mitochondrial) inheritance**, heteroplasmic — the duplication was detectable at trace levels in the unaffected/mildly-affected mother's lymphocyte DNA by PCR, establishing maternal transmission of the lesion [PMID:1531167]. This is distinct from the *typical* single mtDNA deletion syndrome pattern (Kearns-Sayre/Pearson), where deletions are usually **sporadic, de novo** events not transmitted from an affected mother; duplications, by contrast, have a documented capacity for maternal transmission (Poulton et al., 1992; general mtDNA rearrangement literature).

**Penetrance/expressivity:** Markedly variable expressivity is evident even within this single family — the mother, carrying very low-level heteroplasmy, manifested only a mild PEO-like phenotype (ptosis, ophthalmoplegia, muscle weakness), while her daughters (presumably with much higher heteroplasmic mutant load in affected tissues due to mitotic segregation during development) manifested the full severe multisystem syndrome. This is consistent with the general mitochondrial genetics principle of a **heteroplasmy threshold effect** for phenotypic expression.

**Genetic anticipation:** Not established, though the pattern of a mildly-affected mother and severely-affected offspring is at least superficially consistent with increasing heteroplasmic load through the maternal germline — this is not proven mechanistically in the report and should not be over-interpreted as "anticipation" in the classical repeat-expansion sense.

**Germline mosaicism:** The mother's low-level heteroplasmy detected only by PCR (not Southern blot) in lymphocytes is itself an example of germline/somatic mosaicism for the mtDNA rearrangement.

**Founder effects / consanguinity / carrier frequency:** Not applicable/not reported — as a private familial mtDNA rearrangement, there is no population carrier frequency, and consanguinity is not relevant to mitochondrial (non-Mendelian nuclear) inheritance.

**Population demographics:** No data on affected ethnic/geographic groups, sex ratio (both reported cases are female, consistent with maternal transmission being observed in daughters, though sons can also inherit maternal mtDNA), or age distribution beyond the index family (onset in first year of life; death/major morbidity by age 3–5 years in the reported cases).

---

## 10. Diagnostics

**Laboratory tests:**
- Renal tubular function panel: serum and urine electrolytes (Na, K, Cl, Ca), evaluation for generalized Fanconi-type proximal tubulopathy (glucosuria, aminoaciduria, phosphaturia, bicarbonate wasting/acidosis, low-molecular-weight proteinuria) — LOINC panels for comprehensive metabolic panel and urine amino acid/protein screening apply generally (not disease-specific LOINC identified).
- Blood glucose / HbA1c for diabetes mellitus monitoring.
- Serum/CSF lactate and lactate:pyruvate ratio — a standard mitochondrial-disease screening test (not explicitly reported as measured in the original paper per the available excerpts, but standard of care for suspected mitochondrial cytopathy).

**Biomarkers:** No specific circulating biomarker beyond standard mitochondrial disease panel (lactate, pyruvate) was identified for this syndrome specifically.

**Muscle biopsy / histopathology:** Modified Gomori trichrome stain demonstrating **ragged-red fibers** — the classic morphological hallmark of mtDNA rearrangement disease, documented in this family [PMID:1531167].

**Biochemical (enzymatic) testing:** Mitochondrial respiratory chain enzyme assay on skeletal muscle and lymphocyte homogenates demonstrating **isolated/predominant Complex III deficiency** [PMID:1531167]. This is the key biochemical diagnostic finding.

**Genetic testing:**
- **Southern blot analysis of muscle mtDNA** — the method used to first identify the ~26 kb heteroplasmic partial duplication with the ATP6/CYB junction [PMID:1531167]. This remains the gold-standard method for detecting large-scale mtDNA duplications/deletions (as opposed to standard long-range PCR, which can sometimes miss duplications or misinterpret them as deletions).
- **PCR amplification** of the specific junction fragment — used to detect trace-level heteroplasmy in maternal lymphocyte DNA, establishing maternal transmission [PMID:1531167].
- Modern equivalent: whole mitochondrial genome sequencing with long-read or targeted long-range PCR approaches, capable of resolving duplication vs. deletion topology, would be the contemporary diagnostic approach (general mtDNA-diagnostics knowledge; not applied in the original 1992 report which pre-dates these methods).
- Because mtDNA rearrangements can be tissue-restricted and heteroplasmy level–dependent, **testing of an affected/high-heteroplasmy tissue (muscle) is preferred over blood** for diagnostic sensitivity — consistent with GeneReviews guidance for single large-scale mtDNA deletion/duplication syndromes generally (NBK1203).

**Ophthalmologic evaluation:** Electroretinogram (documented as extinguished in the second sister) and fundoscopic exam for pigmentary retinopathy.

**Audiology:** Formal audiometric testing for sensorineural hearing loss.

**Differential diagnosis:** Other single large-scale mtDNA deletion/duplication syndromes (Kearns-Sayre syndrome, Pearson marrow-pancreas syndrome, CPEO/CPEO-plus); other primary mitochondrial disorders causing Fanconi syndrome (e.g., BCS1L-related complex III deficiency with Fanconi syndrome and GRACILE-spectrum disease, EHHADH- and GATM-related isolated renal Fanconi syndromes, RRM2B-related mtDNA depletion syndrome with encephalomyopathy and renal tubulopathy); other syndromic causes of diabetes + deafness + neurodegeneration (e.g., Wolfram syndrome, though that is autosomal recessive nuclear disease with diabetes insipidus rather than tubulopathy); mitochondrial diabetes and deafness (MIDD, typically m.3243A>G point mutation) as a distinguishing comparator — MIDD lacks the severe infantile Fanconi tubulopathy that defines this entity.

**Screening:** No population screening program exists for this ultra-rare entity; family-based cascade testing (maternal lineage) would be the logical approach given the demonstrated maternal transmission in the index pedigree.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Severe. In the only reported family, the **older sister died at age 5 of an acute episode of diarrhea, vomiting, and dehydration** [PMID:1531167] — i.e., the disease was fatal in early childhood in this case. The **younger sister survived a comparable severe dehydration episode at age 3** but continued to develop progressive multisystem disease (ophthalmoplegia, ptosis, retinal degeneration with extinguished ERG) thereafter. No formal survival statistics (5-year/10-year rates) exist given the extremely small reported case number.

**Morbidity:** Severe and multi-domain — progressive renal, neurological (cerebellar and cranial-nerve/extraocular), visual, auditory, endocrine (diabetes), musculoskeletal, and dermatological morbidity accrue over the disease course.

**Complications:** Acute life-threatening dehydration/electrolyte crises (directly tied to the severe renal salt-wasting tubulopathy) represent the dominant acute complication and cause of mortality in the index family. Chronic complications include blindness (from pigmentary retinopathy), deafness, cerebellar ataxia-related disability, osteoporosis/fracture risk, and the long-term complications of diabetes mellitus if the patient survives long enough to accrue them.

**Prognostic factors:** By analogy with other heteroplasmic mtDNA disorders, tissue-specific heteroplasmy level is likely the principal driver of phenotypic severity and prognosis (illustrated by the marked difference between the mildly-affected carrier mother and her severely-affected daughters), though this was not directly quantified across tissues in the report.

---

## 12. Treatment

There is **no disease-specific treatment or cure** described for this syndrome in the literature identified; management is supportive and follows general principles for mitochondrial cytopathies and their organ-specific complications, extrapolated from broader mitochondrial-disease and mtDNA-rearrangement-syndrome management guidance (GeneReviews NBK1203; mitochondrial diabetes reviews):

- **Renal tubulopathy / Fanconi syndrome:** Electrolyte and fluid replacement (sodium, potassium, bicarbonate, calcium, phosphate supplementation as needed), close monitoring and aggressive management of intercurrent illness to prevent life-threatening dehydration (the documented cause of death/near-death in the index family). NCIT: Fluid/electrolyte therapy — NCIT:C15747 (Supportive Care) as a general category.
- **Diabetes mellitus:** Insulin therapy is typically required as mitochondrial diabetes tends to progress more rapidly to insulin-dependence than typical type 2 diabetes; **metformin is generally avoided** because of the risk of precipitating or worsening lactic acidosis in the setting of underlying OXPHOS impairment. SGLT2 inhibitors have been proposed as a preferred oral option in mitochondrial diabetes in more recent general reviews (*Clinical Diabetes*, 2019; general mitochondrial-diabetes management literature — not specific trial data for this entity). NCIT:C15986 (Pharmacotherapy) with therapeutic_agent insulin (CHEBI or NCIT term) and, if used, SGLT2 inhibitor class.
- **Mitochondrial "cocktail" / cofactor therapies:** Coenzyme Q10, riboflavin, L-carnitine, and other mitochondrial cofactor supplements are used empirically in mitochondrial disease broadly, though efficacy remains unproven/experimental and no data exist specific to this syndrome. NCIT:C15433 (Nutritional Support) is the closest general term but per project convention should be scrutinized rather than mechanically applied.
- **Ophthalmologic/audiological support:** Low-vision aids, hearing aids/cochlear implant evaluation as needed for progressive sensory loss.
- **Neurological/rehabilitative support:** Physical/occupational therapy for cerebellar ataxia-related motor impairment (NCIT:C15302 Physical Therapy).
- **Bone health:** Vitamin D/calcium supplementation and monitoring for osteoporosis/rickets, particularly given renal phosphate/calcium wasting.
- **Genetic counseling:** Given demonstrated maternal transmission, genetic counseling of maternal relatives regarding recurrence risk (heteroplasmy-dependent and unpredictable, as for other heteroplasmic mtDNA disorders) is indicated. NCIT:C15240 (Genetic Counseling).

**Experimental treatments:** No clinical trials specific to this syndrome were identified on searches; general mitochondrial disease trials (e.g., of elamipretide, idebenone, or other mitochondrial-targeted agents) would not have specific evidence in this ultra-rare entity.

---

## 13. Prevention

No disease-specific primary prevention exists, given the sporadic/private nature of the causal mtDNA rearrangement (arising either de novo in oogenesis or, as shown here, transmitted at low heteroplasmy from a mildly-affected mother).

- **Secondary prevention:** Early recognition of infantile proximal tubulopathy with prompt electrolyte correction and aggressive management of intercurrent GI illness/dehydration could plausibly reduce acute mortality risk, based directly on the fatal decompensation event in the index case.
- **Reproductive/genetic counseling:** For families with a documented maternal mtDNA rearrangement, reproductive options analogous to those used for other heteroplasmic mtDNA disorders (prenatal testing, though heteroplasmy-based recurrence risk prediction is notoriously difficult for mtDNA disorders due to the mitotic bottleneck; mitochondrial replacement therapy in principle, though not reported as applied to this specific entity) would be the theoretical prevention avenues, extrapolated from general mitochondrial-genetics counseling practice (GeneReviews NBK1203 discusses this for the broader mtDNA rearrangement syndrome category).
- No vaccination, screening program, or public-health intervention is applicable to this private familial mtDNA disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring animal model or veterinary case of this specific mtDNA duplication/phenotype combination was identified in this search. Mitochondrial DNA rearrangement disorders in general are not well-modeled by natural disease in other species (mtDNA rearrangements are typically studied via patient-derived cybrid/transmitochondrial cell lines rather than whole-animal natural disease models), and no OMIA entry or comparable veterinary literature was found for this entity.

---

## 15. Model Organisms

No dedicated animal or cellular model (transgenic mouse, cybrid cell line, iPSC-derived model) specific to this mtDNA duplication was identified in the literature searched. General mtDNA rearrangement research has used **transmitochondrial cybrid cell lines** (patient-derived mitochondria fused into mtDNA-depleted (ρ0) recipient cells) to study duplicated/rearranged mtDNA maintenance and segregation (Molecular Biology of the Cell, 2000, "Maintenance of Human Rearranged Mitochondrial DNAs in Long-Term Cultured Transmitochondrial Cell Lines") — this is a general methodology applicable to, but not specifically reported for, this syndrome's causal duplication. No knockout/knock-in mouse model, zebrafish model, or other organism-based model of this specific ATP6/CYB-junction duplication was identified.

---

## Summary of Key Evidentiary Gaps

1. **Single-family disease:** All specific clinical/genetic findings trace to one 1992 report of two sisters and their mother [PMID:1531167]. No independent replication or additional families have been published in the searched literature.
2. **No modern molecular characterization:** The causal lesion was characterized by Southern blot and PCR in 1992; no subsequent whole-mtDNA sequencing, long-read confirmation, or updated molecular nomenclature (e.g., formal MITOMAP entry) was located.
3. **No tissue-specific pathophysiology data:** Kidney, pancreatic, and cerebellar tissue-level respiratory chain/heteroplasmy data were not directly reported (only muscle and lymphocyte); organ-specific mechanism discussion above is extrapolated from general mitochondrial-disease biology, not this entity specifically.
4. **No treatment outcome data:** No treatment trial, cohort, or even a second case report describing therapeutic approach/response was identified.

**Recommendation for KB curation:** Given the extreme rarity and single-source nature of this entry, evidence items should be conservatively scoped to what is directly stated in PMID:1531167 (and the OMIM/Orphanet/MedGen curated summaries derived from it), with any mechanism-level extrapolation (e.g., proximal tubule bioenergetics, β-cell ATP-dependent insulin secretion, Purkinje cell vulnerability) clearly flagged via appropriate `evidence_source` classification (e.g., citing general mitochondrial-disease mechanism papers separately from the disease-specific case report) rather than implied as directly demonstrated in this pedigree.

---

## Sources

- [Maternally inherited duplication of the mitochondrial genome in a syndrome of proximal tubulopathy, diabetes mellitus, and cerebellar ataxia - PMC (PMID:1531167)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1682469/)
- [Maternally inherited duplication... - PubMed](https://pubmed.ncbi.nlm.nih.gov/1531167/)
- [OMIM #560000 - RENAL TUBULOPATHY, DIABETES MELLITUS, AND CEREBELLAR ATAXIA](https://omim.org/entry/560000)
- [Orphanet: Proximal tubulopathy-diabetes mellitus-cerebellar ataxia syndrome (ORPHA:3390)](https://www.orpha.net/en/disease/detail/3390)
- [Proximal tubulopathy-diabetes mellitus-cerebellar ataxia syndrome - MedGen - NCBI (C3151959)](https://www.ncbi.nlm.nih.gov/medgen/463309)
- [Renal tubulopathy-diabetes mellitus-cerebellar ataxia - wikidoc](https://www.wikidoc.org/index.php/Renal_tubulopathy-diabetes_mellitus-cerebellar_ataxia)
- [About: Proximal tubulopathy-diabetes mellitus-cerebellar ataxia syndrome - NCSU rare diseases](https://rarediseases.oscar.ncsu.edu/disease/proximal-tubulopathy-diabetes-mellitus-cerebellar-ataxia-syndrome/about/)
- [Single Large-Scale Mitochondrial DNA Deletion Syndromes - GeneReviews (NBK1203)](https://www.ncbi.nlm.nih.gov/books/NBK1203/)
- [Duplications of mitochondrial DNA: Implications for pathogenesis - Poulton, J Inherit Metab Dis 1992](https://onlinelibrary.wiley.com/doi/10.1007/BF01799607)
- [BCS1L mutations produce Fanconi syndrome with developmental disability - J Hum Genet 2021](https://www.nature.com/articles/s10038-021-00984-0)
- [Distinct Mitochondrial Pathologies Caused by Mutations of the Proximal Tubular Enzymes EHHADH and GATM - PMC8326905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8326905/)
- [Renal Fanconi Syndrome Is Caused by a Mistargeting-Based Mitochondriopathy - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2211124716304648)
- [Mitochondrial Diabetes: More Than Just Hyperglycemia - Clinical Diabetes, ADA](https://diabetesjournals.org/clinical/article/37/3/298/32909/Mitochondrial-Diabetes-More-Than-Just)
- [Management of mitochondrial diabetes in the era of novel therapies - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1056872720303366)
- [Delineating the mechanisms of cerebellar degeneration in paediatric and adult primary mitochondrial disease - PMC12125081](https://pmc.ncbi.nlm.nih.gov/articles/PMC12125081/)
- [RRM2B-related mitochondrial DNA depletion syndrome, encephalomyopathic form with renal tubulopathy - MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/rrm2b-related-mitochondrial-dna-depletion-syndrome-encephalomyopathic-form-with-renal-tubulopathy/)
- [Mitochondrial DNA deletion and duplication in Kearns–Sayre Syndrome with initial presentation as Pearson Marrow-Pancreas Syndrome - PMC7667363](https://pmc.ncbi.nlm.nih.gov/articles/PMC7667363/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |

All extracted references resolved successfully.