---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-29T22:11:51.453988'
end_time: '2026-07-29T22:18:01.256319'
duration_seconds: 369.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Avoidant Restrictive Food Intake Disorder
  mondo_id: ''
  category: Psychiatric
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
  web_search_requests: 19
  num_turns: 29
  total_cost_usd: 2.0609357000000004
  session_id: 574ce21a-bc93-5c7c-a2f0-f74643218baf
  stop_reason: end_turn
citation_count: 11
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Avoidant Restrictive Food Intake Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Avoidant Restrictive Food Intake Disorder** covering all of the
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

# Avoidant/Restrictive Food Intake Disorder (ARFID): Comprehensive Research Report

## 1. Disease Information

**Overview:** Avoidant/Restrictive Food Intake Disorder (ARFID) is a feeding and eating disorder characterized by persistent failure to meet nutritional and/or energy needs through avoidant or restrictive food intake, **without** the body image disturbance, fear of weight gain, or drive for thinness that defines anorexia nervosa (AN) or bulimia nervosa (BN). It was introduced as a new diagnostic category in **DSM-5** (2013), replacing and substantially expanding the DSM-IV-TR diagnosis "Feeding Disorder of Infancy or Early Childhood" (previously restricted to onset before age 6) (PMID: 38849953; NBK603710).

**Key identifiers:**
- **ICD-11:** `6B83` Avoidant-restrictive food intake disorder, under "Feeding or Eating Disorders" (findacode.com/ICD-11 MMS; mrcpsych.uk)
- **DSM-5 code:** 307.59
- **MONDO:** A specific MONDO CURIE could not be independently confirmed via web search in this session — dismech curation should verify directly via `uv run runoak -i sqlite:obo:mondo search "avoidant restrictive food intake disorder"` per project convention rather than relying on this report.
- **OMIM:** Not applicable — ARFID is not modeled in OMIM as a monogenic/Mendelian disorder; it is a polygenic, multifactorial psychiatric/behavioral condition.
- **Orphanet:** Not listed as a rare disease entity (ARFID is a common psychiatric condition, not orphan-classified).
- **MeSH:** Falls under "Feeding and Eating Disorders" (MeSH D000066942 Avoidant Restrictive Food Intake Disorder was added as an indexed term after 2013 introduction).

**Synonyms/alternative names:** Selective eating disorder (older/lay term); "picky eating disorder" (lay term, imprecise); food avoidance emotional disorder (an earlier, related but not identical construct); functional dysphagia (as a fear-driven ARFID presentation); food neophobia (a component construct, not synonymous); previously "feeding disorder of infancy or early childhood" (DSM-IV, now subsumed).

**Evidence base characteristics:** The literature is derived from a mix of sources — clinical cohort studies from specialized eating-disorder and feeding programs (aggregated disease-level clinical data), population-based birth-cohort and twin registries (e.g., the Swedish Child and Adolescent Twin Study, CATSS; the Dutch Generation R Study), self-report/parent-report screening instrument validation studies, and a small but growing number of neuroimaging and genetic (GWAS) studies. There is essentially no OMIM/ClinVar-style individual-variant clinical data, since ARFID is not caused by identified single-gene mutations.

---

## 2. Etiology

### Disease Causal Factors
ARFID is **multifactorial**, arising from the interaction of genetic predisposition, neurobiological traits (sensory processing, appetite regulation, fear/threat circuitry), temperament, medical/gastrointestinal history, and environmental/psychosocial triggers (PMID: 38849953). There is no single necessary or sufficient cause; three overlapping symptom "drivers" recognized in DSM-5 map onto at least partially distinct etiological pathways:
1. **Sensory sensitivity** to taste/texture/smell/appearance of food
2. **Apparent lack of interest in eating or food** (low appetite/interoceptive drive)
3. **Fear of aversive consequences** of eating (choking, vomiting, allergic reaction, GI pain) — often following a precipitating traumatic eating event

### Genetic Risk Factors
- **Heritability:** The largest twin study to date (Dinkler et al., 2023, *JAMA Psychiatry*, PMID 36723946) analyzed 16,951 twin pairs (33,902 children, ages 6–12) from the Swedish CATSS registry; 682 children (2.0%) met a "broad ARFID phenotype." Heritability was estimated at **0.79 (95% CI, 0.70–0.85)**, with nonshared environmental factors contributing **0.21 (95% CI, 0.15–0.30)**, and shared environment contributing negligibly. This heritability estimate is comparable to or higher than other eating disorders and similar to neurodevelopmental disorders. Sensitivity analyses excluding children with autism (h² = 0.77) or medical conditions (h² = 0.79) gave similar estimates, indicating this is not solely an artifact of comorbid autism.
- **Candidate mechanism — taste receptor genetics:** Polymorphisms in **TAS2R** bitter-taste receptor genes are associated with "supertaster" phenotypes (heightened sensitivity to 6-n-propylthiouracil/PROP bitterness), proposed as a heritable substrate for the sensory-sensitivity ARFID subtype (PMID: 38849953).
- **GWAS status:** The **ARFID-GEN** study (ARFID Genes and Environment; PMID 37990202, BMC Psychiatry 2023) is the first dedicated genome-wide association study, collecting phenotypic questionnaires and saliva DNA from a cohort spanning ages 7–88 (target N=3,190+). Rationale: "High twin-based heritability recently reported for ARFID... motivated the undertaking of this genome-wide association study" — SNP-based heritability, GWAS, genetic correlations with other psychiatric/anthropometric traits, polygenic risk scores, and rare copy-number variant (CNV) analysis are planned. As of mid-2025 conference abstracts (T25, *European Neuropsychopharmacology*), preliminary meta-analyses had not yet reached genome-wide significance for individual loci, attributed to modest sample size at that stage; full ARFID-GEN results are pending.
- **Neurodevelopmental genetic overlap:** Strong genetic/phenotypic correlation with autism spectrum disorder (ASD) and ADHD — children with ARFID are **~14x more likely** to have a co-occurring ASD diagnosis and **~9x more likely** to have ADHD than children without ARFID.

### Environmental Risk Factors
- **Early neurodevelopmental problems (NDPs):** A Japanese birth-cohort study found children in the highest-risk NDP percentile had roughly **3x higher odds** of suspected ARFID; NDPs predictive of later ARFID included problems with general development, communication/language, attention/concentration, social interaction, and sleep (PMC10242837).
- **Precipitating/traumatic triggers:** In one cohort, 71.4% of ARFID patients reported an identifiable triggering event — choking, vomiting (self or witnessed), abdominal pain, bullying, bereavement, medication initiation, or a food-allergy scare (PMID: 38849953).
- **Perpetuating factors:** Parental accommodation of restricted "safe foods," parental anxiety/frustration at mealtimes, and negative reinforcement of avoidance behavior sustain the disorder once established.
- **Medical/GI comorbidity as a risk pathway:** Gastroesophageal reflux disease (GERD), eosinophilic esophagitis, inflammatory bowel disease, food allergies, and structural oropharyngeal abnormalities are recognized antecedent/contributing conditions, particularly for the fear-of-aversive-consequences subtype.
- **Sex:** Unlike AN/BN, ARFID shows a more even or even male-skewed sex ratio in pediatric clinical samples (21–50% male, vs. the strong female predominance in AN/BN).

### Protective Factors
No genetic protective variants have been reported. Environmentally, early, low-pressure, repeated exposure to food variety in infancy/toddlerhood and responsive (non-coercive) feeding practices are associated with lower risk of persistent selective eating, though formal protective-factor data (as distinct from treatment response) remain limited.

### Gene-Environment Interactions
The prevailing model is a **diathesis-stress framework**: an inherited predisposition (heightened sensory reactivity, anxious temperament, or blunted appetite drive) is unmasked or amplified by an environmental trigger (an aversive eating event, GI illness, or high-NDP-risk developmental trajectory), which is then perpetuated by feeding-environment reinforcement patterns (PMID: 38849953; PMC13050801, "Risk factors for avoidant/restrictive food intake disorder in children: A systematic review," 2026).

---

## 3. Phenotypes

ARFID phenotypes are typically organized under DSM-5's three symptom drivers, each with a partially distinct clinical/demographic profile.

### A. Sensory Sensitivity / Selective Eating
- **Type:** Behavioral/sensory-processing phenotype
- **Onset:** Often earliest, from infancy or toddlerhood
- **Characteristics:** Refusal based on texture, temperature, color, smell, or presentation of food; narrow accepted-food repertoire; frequently seen with concurrent ASD (13–50% comorbidity, PMID 38849953)
- **Frequency/demographics:** More common in boys (51.2% vs. 31.5% in girls, P=0.007) and in younger children (66.7% at ages 5–9 vs. 22.2% at ages 15–18)
- **Suggested HP terms:** `HP:0011968` Feeding difficulties; `HP:0000745` Irritability (secondary); consider `HP:0032443` Restrictive eating behavior or generic `HP:0011968`/`HP:0410030`-class feeding-behavior terms — HPO does not yet carry an ARFID-specific granular term; curators should verify current HPO subtree under "Feeding difficulties" (`HP:0011968`) for the closest fit.

### B. Apparent Lack of Interest in Eating / Low Appetite ("Inappetence")
- **Type:** Behavioral/physiological (appetite regulation) phenotype
- **Onset:** Often present from infancy
- **Characteristics:** Low interest in food, easy distractibility during meals, forgetting to eat, rapid satiety
- **Neuroendocrine correlates:** Higher fasting ghrelin, elevated postprandial peptide YY (PYY), elevated fasting cholecystokinin (CCK) versus healthy controls (PMID 38849953, citing Murray et al. 2022 and Becker et al. 2021) — though patterns differ from anorexia nervosa (see Mechanism section)
- **Suggested HP terms:** `HP:0004396` Decreased body weight, `HP:0001508` Failure to thrive, `HP:0011968` Feeding difficulties

### C. Fear of Aversive Consequences
- **Type:** Anxiety-driven behavioral phenotype
- **Onset:** Often later (school-age/adolescence), typically post-traumatic-event
- **Characteristics:** Fear of choking, vomiting, allergic reaction, or GI pain; avoidance of specific food textures/consistencies (often solids); overlaps with specific phobia and emetophobia
- **Frequency:** Associated with the highest anxiety-trait correlations among the three profiles
- **Suggested HP terms:** `HP:0000739` Anxiety, `HP:0002024` Vomiting-related avoidance (via association), consider functional dysphagia-related terms

### Secondary/Systemic Phenotypes (from chronic malnutrition — see Sections 6–7)
- Growth failure / short stature: `HP:0001508` Failure to thrive; `HP:0004322` Short stature
- Amenorrhea (primary/secondary): `HP:0000786` Secondary amenorrhea
- Anemia: `HP:0001903`
- Bradycardia: `HP:0001662`
- Osteopenia/reduced bone mineral density: `HP:0000939` Osteopenia
- Delayed puberty: `HP:0000823`

### Quality of Life Impact
Psychosocial impairment is a core diagnostic criterion (not merely a consequence): impaired ability to eat with others, social isolation at school, family mealtime conflict, and — in fear-driven presentations — significant distress/avoidance of eating-related social situations. Illness duration before diagnosis is notably long (12–33 months vs. 8–23 months for other eating disorders), prolonging cumulative QoL burden (PMID 38849953).

### Symptom Progression
Course is more often **chronic and stable** than episodic; a prospective 2-year outcome study found nearly half of individuals continued to meet full ARFID criteria at follow-up, with only a minority achieving full remission (PMID 38718975). Persistence at 1 year was associated with greater sensory-sensitivity and lack-of-interest severity; remission at 2 years was associated with the fear-of-aversive-consequences profile.

---

## 4. Genetic/Molecular Information

- **Causal genes:** None established — ARFID is not attributable to a single gene or chromosomal abnormality. It is modeled as a complex/polygenic behavioral-psychiatric trait, analogous in genetic architecture (per twin data) to neurodevelopmental disorders rather than to a monogenic syndrome.
- **Pathogenic variants:** Not applicable in the Mendelian sense. No ClinVar/ACMG pathogenic-variant classifications exist for ARFID as a primary diagnosis.
- **Candidate/associated genes:** TAS2R bitter-taste receptor family polymorphisms (sensory-subtype candidate, not yet GWAS-confirmed for ARFID specifically) (PMID 38849953).
- **GWAS status:** ARFID-GEN (PMID 37990202) is the first ARFID-dedicated GWAS; SNP-heritability, polygenic risk score, and genetic-correlation analyses (versus AN, ASD, ADHD, anxiety, BMI) are underway/pending as of this writing (2026); a preceding preliminary GWAS of "childhood fussy eating and ARFID" (ScienceDirect abstract, 2023) had not reached genome-wide significance in early analyses.
- **Modifier genes:** None specifically established; comorbid ASD/ADHD genetic liability likely acts as a shared/overlapping risk architecture rather than a discrete "modifier."
- **Epigenetics:** No dedicated ARFID methylation/epigenomic studies were identified in this search; this remains an open gap.
- **Chromosomal abnormalities:** None specifically implicated in idiopathic ARFID (distinguish from feeding difficulties secondary to known syndromic conditions, which are typically coded as symptoms of the underlying syndrome rather than as ARFID per se).

---

## 5. Environmental Information

- **Non-toxin environmental factors:** No specific toxin, radiation, or occupational exposure is implicated (this is not an exposure-driven disease in the toxicological sense).
- **Lifestyle/behavioral factors:** Feeding practices (parental pressure vs. accommodation), family mealtime structure, and repeated food exposure patterns strongly modulate course, though they are better characterized as perpetuating/ameliorating factors than primary causal exposures.
- **Infectious agents:** Not directly causal, though acute GI infections/illness episodes are a recognized category of precipitating traumatic eating events (e.g., vomiting illness triggering food-specific fear).
- **Medical antecedents functioning as environmental risk:** GERD, eosinophilic esophagitis, IBD, food allergy, and oropharyngeal/structural abnormalities are established antecedent medical conditions that can precipitate or maintain avoidant eating, especially in the fear-driven subtype (NBK603710).

---

## 6. Mechanism / Pathophysiology

The most current synthesis (Fonseca et al. 2024, *Journal of Eating Disorders*, PMID 38849953) proposes a **three-dimensional neurobiological model** mapping onto the three DSM-5 symptom drivers.

### Domain 1 — Sensory Perception Alterations
- **Cellular/molecular basis:** Heightened taste receptor sensitivity (TAS2R bitter-taste polymorphisms; "supertaster" phenotype linked to PROP bitterness sensitivity) produces intensified, aversive taste/texture experiences.
- **Processing mechanism:** Individuals show **sensory hyperresponsiveness** — "faster, more intense, and longer-lasting responses to sensory stimuli," attributed to impaired regulation/organization of sensory-input intensity (PMID 38849953).
- **Neural substrate:** Anterior insula implicated as the interoceptive/gustatory integration hub, though a food-cue fMRI study did not find greater insula activation in the ARFID-sensory-sensitivity subgroup versus controls (PMID 39964683), suggesting the insula's role may be more complex than a simple hyperactivation model.
- **Suggested GO terms:** `GO:0050909` sensory perception of taste; `GO:0007605` sensory perception of sound (n/a); more specifically `GO:0050916` sensory perception of sweet taste / `GO:0001580` detection of chemical stimulus involved in sensory perception of bitter taste.
- **Suggested CL terms:** `CL:0000209` taste receptor cell.

### Domain 2 — Appetite Homeostasis Dysregulation ("Inappetence")
- **Causal chain:** Altered hypothalamic-insular signaling → blunted hunger/interoceptive drive → chronic low intake → malnutrition.
- **Central structures:** Lateral hypothalamus (LH, feeding termination) and paraventricular nucleus (PVN, feeding initiation) integrate hunger/satiety; hunger increases, satiety inhibits hypothalamic activity in typical physiology, and this integration appears disrupted in the inappetence ARFID subtype.
- **Neuroimaging:** Kerem et al. (cited in PMID 38849953) found hyperactivation of orbitofrontal cortex and anterior insula (food-anticipation/reward regions) in fasted ARFID patients with overweight/obesity versus normal-weight ARFID — an unexpected reward-circuit finding requiring replication.
- **Neuroendocrine profile (distinguishing ARFID from AN):** Higher fasting ghrelin, elevated postprandial PYY, elevated fasting CCK, higher GLP-1; **but** low-weight ARFID shows *lower* total ghrelin around meals than AN and does *not* show AN's sustained post-meal PYY elevation (Becker et al. 2021, cited in PMID 38849953) — indicating a biologically distinct appetite-dysregulation signature from AN's fear/restraint-driven physiology. Aulinas et al. (2020) also found ARFID has fewer missed menses, higher total T3, and lower T4:T3 ratio versus AN.
- **Suggested GO terms:** `GO:0007631` feeding behavior; `GO:0032099` negative regulation of appetite; `GO:0032100` positive regulation of appetite.

### Domain 3 — Negative Valence System Hyperactivation (Fear of Aversive Consequences)
- **Causal chain:** Traumatic eating event (choking/vomiting/pain) → amygdala-dependent fear conditioning → hyperactivation of fear/threat circuitry → persistent conditioned avoidance of food/textures resembling the trigger.
- **Neural substrates:** Amygdala (fear processing/learning; lateral amygdala integrates multimodal sensory input for conditioned/unconditioned stimulus association), medial prefrontal cortex (fear regulation), anterior cingulate cortex (emotional processing), hippocampus (contextual memory).
- **fMRI evidence:** Youth with ARFID-fear subtype showed significantly greater amygdala activation versus healthy controls (mean difference 0.49, 95% CI 0.16–0.82, P=0.04) in response to aversive food-fear images; broader activation increases were also seen in anterior cingulate cortex, sensory association cortex, and supplementary motor cortex across ARFID groups generally (PMID 39964683).
- **Disgust as mediator:** An exploratory study of 1,644 adults found that **disgust fully mediated** the association between anxiety and ARFID symptoms, implicating disgust-processing circuitry (insula, again) as a convergence point between the fear and sensory domains (PMID 38849953).
- **Suggested GO terms:** `GO:0007613` memory (fear-related); `GO:0001662` behavioral fear response.

### Structural Neuroimaging
The first structural MRI study of ARFID (Sader et al. 2025, *J Child Psychol Psychiatry*, PMID 39623765), using 1,977 10-year-olds from the population-based Dutch Generation R cohort, found children with ARFID-like symptoms had **greater mean cortical thickness in bilateral superior frontal and frontal cortices** compared to those without symptoms — the first evidence of a distinct structural neuroanatomical correlate, independent of the functional (fMRI) findings above.

### Gut-Brain Axis
An emerging conceptual model (PMC11629072, "A Role for the Microbiota-Gut-Brain Axis in ARFID") proposes that the restricted diet characteristic of ARFID reduces gut microbial diversity, which may in turn affect homeostatic signaling, food reward, interoception, sensory sensitivity, and mood via microbial effects on inflammation, cortisol, and neurotransmitters (dopamine, serotonin) — potentially creating a **self-reinforcing cycle** in which dietary restriction itself worsens the neurobiological substrate maintaining the restriction.

### Cellular/Tissue-Level Consequences of Chronic Malnutrition
Chronic undernutrition produces secondary tissue-level pathophysiology paralleling that of anorexia nervosa: reduced cardiac mass, bone-marrow suppression (anemia/leukopenia/thrombocytopenia), reduced bone mineral density (osteoblast/osteoclast imbalance from hypogonadotropic hypogonadism), and hepatic dysfunction from starvation-associated fatty infiltration.

### Immune System Involvement
No primary autoimmune or immunodeficiency mechanism is implicated; the gut-brain-axis model above proposes a *secondary*, diet-driven inflammatory/immune modulation (via altered microbiota) rather than immune dysfunction as an initiating cause.

### Molecular Profiling
No transcriptomic, proteomic, metabolomic, or single-cell datasets specific to ARFID were identified in this search — this is a significant data gap relative to the neuroimaging and genetic literature, consistent with ARFID being a recently defined (2013) diagnostic entity.

---

## 7. Anatomical Structures Affected

### Organ/System Level
- **Primary system:** Central nervous system (hypothalamus, amygdala, insula, prefrontal/cingulate cortex) — the behavioral/regulatory locus of disease.
- **Secondary/complication-driven systems** (from chronic malnutrition, per NBK603710):
  - **Cardiovascular:** bradycardia, hypotension, arrhythmia, reduced cardiac mass, mitral valve prolapse, pericardial effusion, cardiomyopathy
  - **Gastrointestinal:** constipation, gastroparesis, GERD, dysphagia, functional dyspepsia
  - **Endocrine/reproductive:** hypothalamic amenorrhea, thyroid dysfunction, delayed puberty, osteopenia/osteoporosis
  - **Renal:** electrolyte imbalance, acute kidney injury (in severe refeeding contexts)
  - **Hematologic:** anemia, leukopenia, thrombocytopenia
  - **Musculoskeletal:** growth retardation, decreased muscle mass, rickets (severe pediatric cases)
  - **Dermatologic:** dry skin, hair loss (secondary to nutrient deficiency)

**Suggested UBERON terms:** `UBERON:0000955` brain; `UBERON:0001876` amygdala; `UBERON:0002018` insular cortex; `UBERON:0001870` frontal cortex; `UBERON:0002037` cerebellum (n/a, not specifically implicated); `UBERON:0000948` heart; `UBERON:0001007` digestive system; `UBERON:0002370` thymus (n/a).

### Tissue/Cell Level
- **Neurons:** amygdalar and hypothalamic neuronal populations implicated in fear-conditioning and appetite circuits (`CL:0000540` neuron).
- **Taste receptor cells:** `CL:0000209` taste receptor cell — sensory-subtype substrate.
- **Enteroendocrine cells:** ghrelin-, PYY-, and CCK-secreting gut enteroendocrine cells (`CL:0000164` enteroendocrine cell) — implicated in the distinct appetite-hormone profile.

### Subcellular Level
No specific subcellular/organellar pathology (e.g., mitochondrial, ER stress) has been described; this is a circuit-level, not organelle-level, disorder.

### Localization
Bilateral/symmetric neuroanatomical findings reported to date (bilateral superior frontal cortical thickening; bilateral amygdala activation) — no lateralization pattern established.

---

## 8. Temporal Development

- **Age of onset:** Frequently begins in **infancy or early childhood**, especially the "lack of interest" and "sensory sensitivity" subtypes, which are often present from the earliest feeding period; the "fear of aversive consequences" subtype more often emerges later (school-age/adolescence) following a discrete traumatic eating event. Mean age at clinical presentation across studies: **11.1–14.6 years** (versus 14–16.7 years for anorexia nervosa) (PMID 38849953).
- **Onset pattern:** Can be insidious (sensory/inappetence subtypes, present from infancy) or acute/precipitated (fear subtype, tied to a specific traumatic event).
- **Progression:** Predominantly a **chronic, stable** course rather than episodic. A prospective 2-year study (PMID 38718975) found that ~half of participants persisted with full ARFID criteria at follow-up, and only 3% shifted diagnostically to anorexia nervosa. Illness duration prior to diagnosis (12–33 months) exceeds that typically seen in AN/BN (8–23 months), suggesting either slower recognition or genuinely more indolent onset.
- **Remission patterns:** A minority of cases show spontaneous or treatment-associated remission; persistence is the modal outcome without intervention. Predictors differ by symptom driver: sensory-sensitivity and lack-of-interest severity predict 1-year persistence; fear-of-aversive-consequences severity predicts 2-year remission.
- **Critical periods:** Early childhood (before age 6–7) is a key differentiation window, since normative "picky eating" is common under age 6 and typically resolves spontaneously — persistence beyond this window, combined with functional/nutritional impairment, is a key marker distinguishing ARFID from developmentally normal food selectivity (PMC12736178).
- **Course into adulthood:** ARFID is increasingly recognized to persist into or first present in adulthood; adult clinical cohorts show slower treatment progress and less favorable weight-restoration trajectories than adults with anorexia nervosa, though overall treatment completion and improvement rates are reported as good (PMC10807227).

---

## 9. Inheritance and Population

### Epidemiology
- **Community/general population prevalence:** 0.3–15.5% (wide range reflecting instrument and population heterogeneity); general child-population estimates cluster around 0.35–3.2%; a large Dutch population cohort (Generation R, n=2,862) found 6.4% met ARFID-symptom criteria; adult general-population estimates 0.3–3.1% (NBK603710; PMC10108140).
- **Clinical setting prevalence:** Specialized eating-disorder services 5–22.5%; specialized pediatric feeding clinics 32–64% (highest of any setting); general pediatric outpatient/inpatient services 3–7.2%.
- **Incidence:** 2.02 per 100,000 children/adolescents (ages 5–18) per Canadian national pediatric surveillance (Katzman et al. 2021, cited PMC10108140).

### Genetic Architecture (not classical Mendelian)
- **Inheritance pattern:** Complex/polygenic — not Mendelian (AD/AR/X-linked/mitochondrial). Twin-study heritability of **0.79** places ARFID's genetic architecture closer to neurodevelopmental disorders (ASD, ADHD) than to classic single-gene conditions (PMID 36723946).
- **Penetrance/expressivity:** Not applicable in the classical sense; expressivity is highly variable across the three symptom-driver subtypes and modified by comorbid ASD/anxiety.
- **Genetic anticipation, germline mosaicism, founder effects, consanguinity:** Not applicable/not reported — none of these classical Mendelian-genetics concepts have documented relevance to ARFID.
- **Carrier frequency:** Not applicable (polygenic trait, not a discrete carrier state).

### Population Demographics
- **Sex ratio:** More balanced than other eating disorders; clinical samples show 21–50% male (versus the strong female skew of AN/BN); some pediatric ASD-comorbid samples approach parity.
- **Age distribution:** Peak clinical presentation in later childhood/early adolescence (mean 11.1–14.6 years), though a documented developmental peak of *sub-diagnostic* selective eating exists in early childhood (ages 2–6) that is normative and distinct from clinical ARFID.
- **Geographic/ethnic variation:** Limited data; prevalence estimates vary substantially by country/instrument (e.g., Taiwan 0.3–0.5% vs. Portugal 15.5% in school samples), likely reflecting screening-tool and cultural differences rather than confirmed true prevalence differences (PMC10108140).
- **Comorbidity-driven subpopulations:** ASD populations show markedly elevated ARFID prevalence — pooled meta-analytic estimate ~16.27% ARFID prevalence among individuals with ASD, and ~11.41% ASD prevalence among individuals with ARFID (2025 meta-analysis, PMC11891632); anxiety disorder comorbidity 9.1–72% (up to ~71% in some cohorts), with generalized anxiety disorder most common.

---

## 10. Diagnostics

### Clinical Criteria (Primary Diagnostic Method)
**DSM-5 criteria** (four-part, per NBK603710):
- **Criterion A:** Eating/feeding disturbance manifest as persistent failure to meet nutritional/energy needs, evidenced by ≥1 of: significant weight loss (or failure to achieve expected growth in children); significant nutritional deficiency; dependence on enteral feeding/oral nutritional supplements; marked interference with psychosocial functioning.
- **Criterion B:** Not better explained by lack of available food or culturally sanctioned practice.
- **Criterion C:** Not occurring exclusively during AN/BN, and no evidence of disturbed body-weight/shape experience.
- **Criterion D:** Not attributable to a concurrent medical condition or better explained by another mental disorder (or, if occurring in the context of another condition, exceeds what would routinely be expected and warrants independent clinical attention).

**ICD-11 (6B83)** criteria are conceptually parallel: avoidance/restriction resulting in (1) insufficient quantity/variety to meet needs → weight loss, nutritional deficiency, supplement/tube dependence, or physical-health impact; or (2) significant functional impairment; explicitly not motivated by weight/shape concerns.

### Structured Diagnostic Instruments
- **PARDI (Pica, ARFID, and Rumination Disorder Interview):** Clinician-administered semi-structured interview; subscale internal consistency: sensory sensitivity α=0.77, lack of interest α=0.89, fear of aversive consequences α=0.79, overall severity α=0.89; diagnostic Cohen's κ=0.75 (PMID 38849953).
- **PARDI-AR-Q (self/parent-report questionnaire version):** Correctly identified ~90% of ARFID cases against DSM-5 criteria regardless of subtype profile; includes a severity-of-impact scale and diagnostic algorithm, distinguishing it from NIAS.
- **NIAS (Nine-Item ARFID Screen):** Brief adult self-report; three 3-item subscales ("picky eating," "fear," "low appetite"); total scale α=0.84, ω=0.90; useful as a symptom-severity estimator but **not validated as a standalone diagnostic tool against clinical interview**.
- **EDA-5 (Eating Disorder Assessment for DSM-5)** and **SCID-5**: General structured clinical interviews with ARFID modules.
- **EDE-ARFID module:** 22-item, 7-point Likert; α=0.81–0.94.
- **EDY-Q:** 14-item self-report for ages 8–13, 12 ARFID-relevant items, α=0.62 (lower reliability, pediatric self-report).

### Laboratory/Ancillary Workup (supportive, not diagnostic)
CBC, comprehensive metabolic panel with LFTs, thyroid function, vitamin/mineral panel (notably B12, vitamin K, iron, zinc, folate — often deficient given reduced animal-protein/vegetable intake), celiac screening, and (in females) LH/FSH/estradiol for amenorrhea workup; ECG for bradycardia/arrhythmia risk in malnourished patients.

### Genetic Testing
No genetic test is diagnostic or clinically indicated for idiopathic ARFID; genetic/genomic evaluation is relevant only when ARFID occurs secondary to an identifiable syndromic condition (e.g., ruling out conditions with known feeding-difficulty phenotypes) — this is a differential-diagnosis exclusion exercise rather than an ARFID-confirmatory test.

### Differential Diagnosis (per NBM603710)
Anorexia nervosa, bulimia nervosa, GERD, eosinophilic esophagitis, IBD, food allergy, celiac disease, autism spectrum disorder, anxiety disorders/OCD, major depressive disorder, PTSD, ADHD, pica, rumination disorder, endocrine disorders (Addison disease, hypothyroidism), and structural oropharyngeal abnormalities.

### Screening
No population-level newborn or universal screening program exists. The key clinical screening challenge is distinguishing pathological ARFID from developmentally normative early-childhood "picky eating," which is common under age 6–7 and typically resolves without intervention (PMC12736178).

---

## 11. Outcome/Prognosis

- **Mortality:** Not separately quantified in the literature reviewed here; medical complications of severe malnutrition (cardiac arrhythmia, refeeding syndrome) carry recognized mortality risk analogous to severe anorexia nervosa, but ARFID-specific mortality/case-fatality statistics were not identified in this search and should be treated as a data gap.
- **Persistence/course:** A prospective 2-year longitudinal study (PMID 38718975) found ARFID is **not a transient developmental phase** — nearly half of patients continued to meet full diagnostic criteria at 2-year follow-up, with only a minority achieving full remission; 3% showed diagnostic shift to anorexia nervosa over the same period.
- **Predictors of persistence vs. remission:** Greater sensory-sensitivity and lack-of-interest severity predicted persistence at year 1; greater fear-of-aversive-consequences severity predicted remission at year 2 — the three symptom drivers thus carry distinct prognostic implications and may warrant differentiated treatment planning.
- **Adult treatment outcomes:** Adults with ARFID at a tertiary eating-disorders program progressed through inpatient treatment **more slowly** and achieved **less favorable weight outcomes at discharge** than matched anorexia-nervosa patients, though completion rates and functional-impairment improvement were reported as good overall, with significant BMI improvement among those admitted underweight (PMC10807227).
- **Bone health:** A narrative review (PMC10031860) documents compromised bone mineral density as a recognized long-term morbidity, paralleling AN-associated osteopenia/osteoporosis risk.
- **Course-shift risk:** A minority of ARFID cases develop overvaluation of shape/weight over time, effectively transitioning toward an AN-like clinical picture (PMC11067077) — an important longitudinal monitoring consideration.
- **Quality of life:** Chronic course, longer pre-diagnosis illness duration, and high anxiety/social-impairment comorbidity together produce sustained functional and psychosocial burden; standardized disease-specific QoL instrument data (e.g., EQ-5D) specific to ARFID were not identified in this search.

---

## 12. Treatment

### Pharmacotherapy (all off-label; **no FDA-approved medication exists for ARFID**)
- **Mirtazapine:** H1-histaminergic antagonism drives an orexigenic (appetite-stimulating) and anxiolytic effect; also addresses visceral hypersensitivity/nausea. Gray et al. (retrospective study, 14 patients) found a statistically significant increase in weekly BMI-change rate after starting mirtazapine (0.10 → 0.23 BMI-units/week) (PMID 38849953). MAXO/NCIT: Pharmacotherapy (`NCIT:C15986`); therapeutic_agent mirtazapine (`CHEBI:6980`, verify exact ID at curation time).
- **Cyproheptadine:** Antihistamine/serotonin antagonist used off-label as an appetite stimulant, primarily in case series.
- **Olanzapine:** Second-generation antipsychotic; blocks histaminergic/serotonergic receptors in the lateral hypothalamus, reducing cognitive rigidity about food and stimulating appetite/weight gain; case-series evidence also suggests benefit for associated anxiety/depressive symptoms.
- **Buspirone:** Anxiolytic used specifically for fear-of-aversive-consequences (e.g., choking-phobia) presentations; case-report-level evidence.
- **D-cycloserine:** NMDA partial agonist studied as an exposure-therapy augmentation agent for food aversions.
- **Explicit evidence gap:** "There are no randomized, double-blind, placebo-controlled trials of any psychopharmacological agent for ARFID" (multiple sources concur); all pharmacological evidence is case-series/retrospective-cohort level.

### Psychotherapy / Behavioral Interventions
- **CBT-AR (Cognitive-Behavioral Therapy for Avoidant/Restrictive Food Intake Disorder):** Developed for ages 10+; centers on **repeated food exposure under inhibitory-learning principles** rather than the body-image/weight-cognition focus used in CBT for AN/BN. Open-trial evidence (Dumont et al. 2019; Thomas et al. 2020, 2021) shows significant reductions in PARDI severity scores, increased dietary variety, and weight gain in underweight patients; tube feeding was discontinued in 6/11 patients in one pilot. Notably, "daily exposure to the visual, olfactory, and harmless consequences of consuming food alone does not appear to reduce avoidant behaviour" as robustly as in classic anxiety-disorder exposure therapy — suggesting ARFID-specific exposure protocols require adaptation, not direct transplantation from anxiety-disorder CBT.
- **FBT-ARFID (Family-Based Treatment, adapted from FBT for AN/BN):** Trains parents/caregivers as agents of behavioral change; pilot data (Lock et al. 2018 case series; ongoing RCT randomizing ~100 children ages 6–12 to FBT-ARFID vs. Psychoeducation/Motivation Therapy, PMID 36460266) suggest efficacy, with improved parental self-efficacy proposed as the treatment mechanism.
- **SPACE (Supportive Parenting for Anxious Childhood Emotions):** Caregiver-focused intervention targeting reduction of parental accommodation behaviors that perpetuate avoidance.

### Nutritional Rehabilitation
Core and often first-line: gradual expansion of accepted-food range, regular meal structure, close growth monitoring (pediatric), and — more frequently than in AN — enteral/nasogastric tube feeding or oral nutritional supplementation in severe malnutrition, with careful titration to avoid iatrogenic reinforcement of oral-food avoidance and monitoring for refeeding syndrome.

### Hospitalization Criteria (APA)
BMI <75% of median for age/sex; dehydration; abnormal electrolytes; ECG abnormalities; bradycardia (<50 bpm daytime/<45 bpm nocturnal); hypotension (<90/45 mmHg); hypothermia (<96°F); orthostatic pulse increase (>30 bpm adults/>40 bpm adolescents); growth impairment; failed outpatient treatment; concurrent psychiatric/medical complications.

### Experimental/Ongoing Trials
- NCT (protocol PMID 36460266): FBT-ARFID vs. Psychoeducational Motivation Therapy RCT, ages 6–12.
- Weighted-blanket intervention trial for food-related anxiety in pediatric ARFID (NCT06420232) — a novel sensory/behavioral adjunct approach.
- CBT-AR open trial at Massachusetts General Hospital.

### Suggested MAXO/treatment-ontology mappings for a dismech entry
- `MAXO:0000950` supportive care (nutritional rehabilitation/monitoring)
- `NCIT:C15986` Pharmacotherapy (mirtazapine, cyproheptadine, olanzapine, buspirone — each via `therapeutic_agent`)
- Behavioral/psychotherapy treatment_term candidates: CBT-AR and FBT-ARFID would map to a psychotherapy/behavioral-counseling MAXO term (verify exact MAXO ID at curation time, e.g., analogous to `MAXO:0000077` behavioral counseling) with `therapeutic_modality: BEHAVIORAL`.

---

## 13. Prevention

- **Primary prevention:** No established primary-prevention strategy exists; the literature explicitly states, "There's no known way to prevent avoidant/restrictive food intake disorder" (Cleveland Clinic, corroborated by systematic risk-factor review PMC13050801). Given the ~79% heritability estimate, primary prevention in the vaccine/exposure-avoidance sense is not conceptually applicable to this behavioral/neurodevelopmental-spectrum condition.
- **Risk-informed monitoring (quasi-secondary prevention):** Because early neurodevelopmental problems (general development, communication/language, attention, social interaction, sleep) predict later ARFID with ~3x elevated odds in the highest-risk percentile, targeted developmental surveillance in high-NDP-risk children is a plausible early-detection strategy, though not yet formalized into guideline-level screening programs.
- **Distinguishing normative from pathological selective eating:** Since typical "picky eating" affects a large proportion of children under 6–7 and usually resolves spontaneously, the practical secondary-prevention/early-intervention priority is accurate differentiation (via growth monitoring, nutritional-adequacy assessment, and psychosocial-impairment screening) rather than treating all selective eating as pre-ARFID.
- **Behavioral/feeding-practice interventions:** Responsive, low-pressure feeding practices and repeated non-coercive food exposure in toddlerhood are associated with better food-variety outcomes and are the closest analog to a modifiable environmental protective strategy, though rigorous trial evidence for true ARFID-incidence prevention (versus symptom management) is limited.
- **Genetic counseling:** Not clinically applicable given the polygenic, non-Mendelian architecture — no risk-percentage counseling framework analogous to single-gene disorders exists.
- **Tertiary prevention:** Early diagnosis and treatment initiation (before chronic malnutrition/growth impairment develops) is emphasized throughout the clinical literature as the most actionable "prevention" lever — i.e., preventing progression to severe medical complications (refeeding syndrome, growth failure, osteopenia) rather than preventing the underlying disorder itself.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring ARFID-equivalent disease entity has been characterized in non-human species in the veterinary/OMIA literature identified here. Feeding selectivity/food neophobia occurs across many species as a normal behavioral trait (evolutionarily conserved anti-poisoning strategy) but is not modeled as a spontaneous "disease" analog to human ARFID.
- **Breed-specific:** Not applicable — no VBO-catalogued breed-specific ARFID-like condition was identified.
- **Comparative biology:** Food neophobia (reluctance to eat novel foods) is a well-studied, evolutionarily conserved behavior in rodents and birds, studied largely in the context of pest-control/bait-avoidance research rather than as a disease model, but conceptually informs the human ARFID sensory/neophobia construct (ResearchGate: "Exploitable characteristics of neophobia and food aversions for improvements in rodent and bird control").
- **Zoonotic potential:** Not applicable — ARFID is not an infectious or transmissible condition.

---

## 15. Model Organisms

- **No dedicated, validated ARFID animal model exists** as of this literature search — this is an explicit and acknowledged gap in the field.
- **Closest available model — Conditioned Taste Aversion (CTA) in rodents:** A systematic review (ScienceDirect, 2023) proposes rodent CTA paradigms as "a potential animal model of pediatric feeding disorder and ARFID," reasoning that CTA — in which an animal learns to avoid a taste/food previously paired with illness — parallels the fear-of-aversive-consequences ARFID subtype. The review notes CTA "has been observed in humans and parallels many of the characteristics of rodent CTA," and evaluates pharmacological agents shown to reduce CTA in rodents as candidate translational treatments.
- **Applications:** CTA models are proposed to probe neural mechanisms maintaining food-specific fear/avoidance and to screen candidate pharmacological interventions (e.g., agents that reduce learned aversion), but they model only the fear-driven subtype, not the sensory-sensitivity or inappetence subtypes.
- **Limitations:** No rodent, zebrafish, Drosophila, C. elegans, or iPSC/organoid model captures the full multi-subtype human ARFID phenotype (sensory hyperresponsiveness + appetite dysregulation + fear conditioning + the psychosocial/functional-impairment criterion); given the polygenic, non-Mendelian genetic architecture, no knockout/transgenic genetic model is currently justified by a specific causal gene.
- **Resources:** No MGI, RGD, ZFIN, or IMPC entries specific to "ARFID" exist; relevant rodent feeding-behavior/appetite genetic models (e.g., ghrelin, leptin, hypothalamic circuit knockouts) are general appetite-regulation models, not ARFID-specific, and any use for dismech curation purposes should draw the distinction between "informative appetite-circuit model" and "ARFID disease model" carefully.

---

## Summary of Key Ontology Term Recommendations for KB Curation

| Category | Term suggestions (verify via OAK before use) |
|---|---|
| MONDO | Not confirmed in this search — verify via `runoak -i sqlite:obo:mondo search` |
| HP (phenotypes) | `HP:0011968` Feeding difficulties; `HP:0001508` Failure to thrive; `HP:0004322` Short stature; `HP:0000786` Secondary amenorrhea; `HP:0001903` Anemia; `HP:0001662` Bradycardia; `HP:0000939` Osteopenia; `HP:0000823` Delayed puberty; `HP:0000739` Anxiety |
| GO (biological processes) | `GO:0007631` feeding behavior; `GO:0050909` sensory perception of taste; `GO:0032099`/`GO:0032100` regulation of appetite; `GO:0001662` behavioral fear response |
| CL (cell types) | `CL:0000209` taste receptor cell; `CL:0000164` enteroendocrine cell; `CL:0000540` neuron |
| UBERON | `UBERON:0001876` amygdala; `UBERON:0002018` insular cortex; `UBERON:0001870` frontal cortex; `UBERON:0000955` brain |
| MAXO/NCIT (treatments) | `NCIT:C15986` Pharmacotherapy (+ therapeutic_agent: mirtazapine, cyproheptadine, olanzapine, buspirone); behavioral-counseling term for CBT-AR/FBT-ARFID; `MAXO:0000950` supportive care |

---

## Key Citations

- Dinkler L, et al. Etiology of the Broad Avoidant Restrictive Food Intake Disorder Phenotype in Swedish Twins Aged 6 to 12 Years. *JAMA Psychiatry.* 2023;80(3):260-269. PMID: [36723946](https://pubmed.ncbi.nlm.nih.gov/36723946/)
- Fonseca NK, et al. Avoidant restrictive food intake disorder: recent advances in neurobiology and treatment. *J Eat Disord.* 2024;12:74. PMID: [38849953](https://pmc.ncbi.nlm.nih.gov/articles/PMC11157884/)
- Bourne L, et al. What do we know about the epidemiology of avoidant/restrictive food intake disorder in children and adolescents? A systematic review. PMID: [36527163](https://pmc.ncbi.nlm.nih.gov/articles/PMC10108140/)
- Neural Response to Food Cues in Avoidant/Restrictive Food Intake Disorder. PMID: [39964683](https://pubmed.ncbi.nlm.nih.gov/39964683/)
- Sader M, et al. Neural correlates of children with avoidant restrictive food intake disorder symptoms: large-scale neuroanatomical analysis. *J Child Psychol Psychiatry.* PMID: [39623765](https://pubmed.ncbi.nlm.nih.gov/39623765/)
- Prospective 2-Year Course and Predictors of Outcome in ARFID. PMID: [38718975](https://pubmed.ncbi.nlm.nih.gov/38718975/)
- ARFID Genes and Environment (ARFID-GEN): study protocol. *BMC Psychiatry.* PMID: [37990202](https://pmc.ncbi.nlm.nih.gov/articles/PMC10664384/)
- NBK603710 — Avoidant Restrictive Food Intake Disorder, StatPearls (NCBI Bookshelf)
- Sader M, et al. The Co-Occurrence of Autism and ARFID: A Prevalence-Based Meta-Analysis. *Int J Eat Disord.* [PMC11891632](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891632/)
- ICD-11 6B83 Avoidant-restrictive food intake disorder — [findacode.com](https://www.findacode.com/icd-11/code-1242188600.html)
- Risk factors for avoidant/restrictive food intake disorder in children: A systematic review. *J Pediatr Gastroenterol Nutr.* 2026. [PMC13050801](https://pmc.ncbi.nlm.nih.gov/articles/PMC13050801/)
- Systematic review of pharmacological treatments that reduce conditioned taste aversions in rodents: A potential animal model of pediatric feeding disorder and ARFID. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S019566632302634X)