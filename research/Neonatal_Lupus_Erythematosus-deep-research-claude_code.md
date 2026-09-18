---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T23:16:20.583453'
end_time: '2026-08-27T23:19:53.324448'
duration_seconds: 212.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neonatal Lupus Erythematosus
  mondo_id: ''
  category: Autoimmune
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
  web_search_requests: 18
  num_turns: 20
  total_cost_usd: 1.1991881999999998
  session_id: 2df13fb4-9115-50fa-aa7c-75f1d91c874a
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 49
reference_validation:
  total_references: 36
  verified: 35
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC3437607
  relevance_assessed: 35
  on_topic: 26
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neonatal Lupus Erythematosus
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Neonatal Lupus Erythematosus** covering all of the
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

I'll research Neonatal Lupus Erythematosus now and compile a comprehensive report. Let me start by gathering information from primary sources.

Let me gather a few more specific details: fetuses of anti-Ro mothers overall recurrence/risk stratification, pacemaker outcomes, IVIG trials, and recent 2024-2025 review specifics.

I now have comprehensive material across all major sections. Let me do a final round on a few remaining gaps: neurological/CNS involvement, other rare manifestations, and disease course/self-limited nature confirmation.

I have sufficient information to compile a comprehensive report. Here is the full research report.

# Neonatal Lupus Erythematosus (NLE): Comprehensive Research Report

## 1. Disease Information

**Overview:** Neonatal lupus erythematosus (NLE) is a rare, *passively acquired* autoimmune syndrome of the fetus/neonate caused by transplacental transfer of maternal IgG autoantibodies — principally anti-Ro/SSA (anti-Ro52/TRIM21 and anti-Ro60) and often anti-La/SSB, with anti-U1-RNP implicated in a distinct subset. It is explicitly **not** the neonatal/infant form of systemic lupus erythematosus (SLE); rather, it is "an example of passively acquired autoimmunity in which the influx of maternal autoantibodies... transiently affects fetal and neonatal organ systems" (PMC3437607). The maternal disease may be overt SLE, Sjögren's syndrome, or entirely asymptomatic — many mothers are identified only after their infant's diagnosis.

**Key identifiers:**
- **MONDO:** MONDO:0018360
- **Orphanet:** ORPHA:398124
- **ICD-10:** M32.8 (Other forms of lupus erythematosus); **ICD-11:** KA07.0
- **OMIM:** No dedicated OMIM entry exists (NLE is acquired, not Mendelian)
- **MeSH:** Lupus Erythematosus, Systemic (neonatal lupus indexed as a related term)

**Synonyms:** Neonatal lupus syndrome (NLS); congenital lupus erythematosus; Ro/SSA-associated neonatal lupus.

**Evidence base:** Predominantly aggregated disease-level data — national/international registries (e.g., the U.S. Research Registry for Neonatal Lupus), multicenter observational cohorts, and systematic literature reviews of individual patient data — rather than single-EHR studies, reflecting the disease's rarity (Vaz de Carvalho et al., PMC7164747, *geoepidemiologic systematic review of individual patient data*).

Sources: [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK526061/), [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=398124), [PMC3437607](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3437607/), [PMC7164747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7164747/)

---

## 2. Etiology

**Primary causal mechanism:** Transplacental passage (via neonatal FcRn receptor) of maternal IgG anti-Ro/SSA (52-kDa and 60-kDa) and anti-La/SSB antibodies during the second and third trimesters, when IgG transport peaks. Anti-Ro (anti-SSA) is present in ~95% of affected infants' mothers (StatPearls). Anti-U1-RNP antibodies define a separate, generally cardiac-sparing NLE phenotype (NEJM 1987, classic description) — **"The Neonatal Lupus Syndrome Associated with U1RNP (nRNP) Antibodies."**

**Risk factors:**
- *Genetic (maternal):* HLA-A1, HLA-B8, HLA-DR3, HLA-B*15, HLA-C*02, HLA-DQ5, HLA-DR10 increase risk of cardiac NLS; HLA-DRB1*04 and HLA-Cw*05 confer susceptibility to anti-SSA/Ro-mediated congenital heart block (CHB), while **HLA-DRB1*13 and HLA-Cw*06 are protective** (J Rheumatol 2025, PMID:38825356).
- *Genetic (fetal):* HLA-DQB1*02, DRB1*03, and TNF-α promoter polymorphisms associate with milder (skin-limited) disease.
- *A recent multiethnic 2024 study found HLA-wide analyses did NOT identify robust NLE risk alleles, and broader SLE-associated genetic risk was not significantly associated with NLE outcomes* — suggesting the field's earlier HLA associations may be less generalizable than thought (Lupus Foundation of America summary of J Rheumatol 2025 findings, PMID:38825356).
- *Obstetric/exposure:* Prior affected pregnancy is the single strongest risk factor (recurrence risk 15–25% vs. <1–2% for first affected pregnancy); maternal antibody titer and epitope specificity (e.g., 52-kDa Ro/SSA epitopes preferentially recognized by mothers of CHB-affected children, PMC1526571).
- **Protective factor:** Anti-β2-glycoprotein I antibodies have been reported to associate with *reduced* risk of anti-Ro60-associated cardiac NLE in some cohorts (ResearchGate/PubMed).

**Gene–environment interaction:** The central "interaction" is immunologic rather than classically environmental — maternal autoimmune serology (genetically influenced) combines with the *developmental window* of fetal cardiac conduction system remodeling (18–24 weeks gestation), when physiological apoptosis exposes normally intracellular Ro/La antigens on the cell surface, creating a narrow window of vulnerability to circulating maternal antibody.

Sources: [J Rheumatol 2025 — Genetics of NLE Risk](https://www.jrheum.org/content/52/1/52), [PMC1526571](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1526571/), [NEJM 1987 U1RNP](https://www.nejm.org/doi/abs/10.1056/NEJM198704303161807)

---

## 3. Phenotypes

### Cardiac (most severe manifestation)
- **Congenital (complete) heart block (CHB):** third-degree AV block is the "signature lesion" of cardiac NLE; second- and first-degree AV block also occur and may be reversible. Onset window: 18–24 weeks gestation (rarely later, and rarely postnatal, first-degree block). HP suggestion: **HP:0001680** (Atrioventricular block) / **HP:0011705** (Complete atrioventricular block).
- **Endocardial fibroelastosis, dilated cardiomyopathy:** can present neonatally or emerge late (postnatal incidence 19–29% despite normal in-utero function) — **HP:0001635** (dilated cardiomyopathy).
- **Valvular insufficiency, sinus node dysfunction, prolonged QTc.**
- Frequency: CHB occurs in 15–30% of NLE cases overall; regional variation is striking — ~70% of NLE cases in European/American cohorts present with CHB vs. only 8.9–23% in Asian cohorts, where cutaneous disease predominates (~80%) (PMC7164747, geoepidemiology review).

### Cutaneous
- **Erythematous, annular/polycyclic photosensitive plaques**, often with central scaling, classically periorbital ("raccoon-eye" appearance) and on the scalp/face — **HP:0025426** (Photosensitivity) plus HPO annular erythema terms.
- Onset: may be present at birth but frequently emerges within the first weeks of life (UV exposure–triggered); resolves over 6–12 months as maternal antibody clears, occasionally leaving telangiectasia, atrophy, or dyspigmentation.
- Sex distribution paradox: cutaneous NLE shows a reported **male predominance (2:1–3:1)** in several series, contrasting with the strong female predominance of adult SLE (though at least one 57-case registry found female predominance — literature is mixed).

### Hepatobiliary
- Occurs in ~15–25% of cases: transaminitis, cholestasis, hepatomegaly/splenomegaly, and rarely a hemochromatosis-like or lupus-hepatitis picture with portal lymphocytic infiltration. Generally transient, resolving over months. HP: **HP:0001392** (Abnormality of the liver), **HP:0001396** (Cholestasis).

### Hematologic
- Occur in ~27% of infants: neutropenia, thrombocytopenia, hemolytic or non-hemolytic anemia, thought to arise from antibody binding to fetal blood cell antigens/immune complex-mediated peripheral destruction. HP: **HP:0001873** (Thrombocytopenia), **HP:0001875** (Neutropenia).

### Neurological (underrecognized)
- Benign, usually asymptomatic **hydrocephalus/macrocephaly** — prevalence ~8.0% in one cohort of 47 NLE infants vs. 0.048–0.081% in the general population. Also reported: white-matter abnormalities, basal ganglia calcification, intracranial hemorrhage, subependymal pseudocysts, seizures, myelopathy/spastic paraparesis (rare, symptomatic subset). Typically resolves without sequelae as antibody clears. HP: **HP:0000238** (Hydrocephalus), **HP:0000256** (Macrocephaly).

### Quality of life / severity
- Cutaneous, hepatic, and hematologic NLE are self-limited (4–12 months) with generally good QoL outcomes. Cardiac NLE is the dominant driver of morbidity/mortality and lifelong pacemaker dependence, with associated psychosocial and quality-of-life burden for families, though no NLE-specific EQ-5D/SF-36 instrument was located in the literature searched.

Sources: [DermNet NZ](https://dermnetnz.org/topics/neonatal-lupus-erythematosus), [PMC7164747 geoepidemiology](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7164747/), [PubMed 17330304 — hydrocephalus/macrocephaly](https://pubmed.ncbi.nlm.nih.gov/17330304/), [Nature Reviews Rheumatology](https://www.nature.com/articles/ncprheum0490)

---

## 4. Genetic/Molecular Information

NLE has **no primary causal germline mutation** in the affected infant — it is antibody-mediated, not inherited in a Mendelian sense. Genetic contributions operate at the level of **maternal (and modestly, fetal) susceptibility**:

- **HLA associations (maternal):** HLA-A1, B8, DR3, B*15, C*02, DQ5, DR10 (cardiac NLS risk); DRB1*04/Cw*05 (susceptibility); DRB1*13/Cw*06 (protective) (J Rheumatol, PMID:38825356).
- **Fetal modifiers:** HLA-DQB1*02, DRB1*03, TNF-α promoter polymorphism — associated with milder/skin-limited disease.
- **Target autoantigens:** Ro60 (TROVE2/SSA2, hgnc:11313), Ro52/TRIM21 (hgnc:11312), La/SSB (hgnc:10646), and in the U1RNP subset, U1-70K/SNRNP70 and other spliceosomal proteins.
- **No pathogenic germline variant classification (ACMG/AMP) applies** — this is not a ClinVar-indexed Mendelian disorder. gnomAD/ClinVar searches are not informative here.
- **Epigenetics:** Not a major described mechanism for NLE itself (distinguish from adult SLE, where DNA methylation changes in T cells are well described); no NLE-specific DiseaseMeth/ENCODE data were identified.
- **Chromosomal abnormalities:** Not implicated; NLE is acquired/immune-mediated, not cytogenetic.

The 2025 *J Rheumatol* genetics paper is the most current authoritative source: broader SLE genetic-risk scores were **not** significantly associated with NLE outcome in a multiethnic mother-infant cohort, indicating the maternal antibody profile (not global SLE genetic burden) is the operative determinant.

Sources: [J Rheumatol — Genetics of NLE](https://www.jrheum.org/content/52/1/52), [Lupus Foundation summary](https://www.lupus.org/news/systemic-lupus-erythematosus-genetics-not-associated-with-neonatal-lupus-outcomes)

---

## 5. Environmental Information

- **UV light** is the principal recognized environmental trigger/exacerbant for the cutaneous phenotype — lesions are classically photo-distributed and can be precipitated or worsened by neonatal sun/phototherapy exposure.
- No infectious agent is causally implicated; NLE is autoantibody-mediated, not infectious.
- No specific maternal lifestyle factor (diet, smoking) has robust evidence as a risk/protective modifier in the literature reviewed; the dominant "environmental" exposure is the maternal autoantibody itself crossing the placenta during the critical fetal cardiac developmental window (18–24 weeks).

Source: [DermNet NZ](https://dermnetnz.org/topics/neonatal-lupus-erythematosus)

---

## 6. Mechanism / Pathophysiology

**Causal chain (cardiac NLE):**
1. **Trigger:** Maternal anti-Ro60/anti-Ro52 (± anti-La) IgG crosses the placenta via FcRn transport, concentrating in fetal circulation during 2nd–3rd trimester.
2. **Antigen exposure:** During normal physiological remodeling of the fetal cardiac conduction system (weeks 18–24), cardiomyocytes undergo apoptosis, translocating normally intracellular Ro60/Ro52/La antigens to the cell surface in apoptotic blebs — a process requiring hY3 RNA for Ro60 surface exposure (PMC3708308).
3. **Antibody binding — two complementary hypotheses:**
   - *Apoptosis hypothesis:* Surface-bound anti-Ro/La antibodies impair the normal, non-inflammatory clearance of apoptotic cardiomyocytes by healthy neighboring myocytes, diverting clearance to **macrophages**, which release pro-inflammatory/pro-fibrotic cytokines.
   - *Calcium-channel hypothesis:* Molecular mimicry between Ro antigen and cardiac **L-type and T-type (α1G) calcium channels** — anti-Ro/La antibodies directly bind fetal cardiomyocyte calcium channels, disturbing calcium homeostasis (JEM, PMC2212767) and disrupting AV/SA nodal conduction independent of inflammation.
4. **Fibrotic amplification:** Anti-Ro60 binding triggers conformational activation of the **uPA/uPAR system**, generating plasmin, which activates **TGF-β**, driving a profibrotic cascade (PMID:22013113).
5. **Downstream pathology:** Progressive macrophage/giant-cell infiltration, fibrosis, and dystrophic calcification of the AV node → irreversible replacement of conduction tissue → third-degree AV block. This explains why steroid (anti-inflammatory) treatment can sometimes reverse *early* first/second-degree block but **never reverses third-degree (complete) block**, since fibrotic replacement is structural, not inflammatory.
6. **Cutaneous/hepatic/hematologic mechanism:** Parallel but reversible antibody-mediated cell injury/immune complex formation in skin (UV-potentiated keratinocyte apoptosis with Ro/La surface exposure), liver (portal lymphocytic infiltration), and blood cells (peripheral antibody-mediated destruction) — these resolve as maternal antibody is catabolized (half-life ~3 weeks, clearing by 6–12 months).

**Suggested ontology terms:**
- GO: GO:0006915 (apoptotic process), GO:0035589 (G-protein coupled purinergic receptor... — N/A), GO:0007568 — better: GO:0030041 (actin filament...) — most relevant: **GO:0043408** (regulation of MAPK cascade) is not central; use **GO:0030512** (negative regulation of TGF-beta receptor signaling — inverse) → prefer **GO:0007179** (transforming growth factor beta receptor signaling pathway, MODIFIER: INCREASED), **GO:0006508** (proteolysis, for uPA/plasmin), **GO:0005513** (detection of calcium ion), **GO:0086012** (membrane depolarization during cardiac muscle cell action potential).
- CL: CL:0000746 (cardiac muscle cell), CL:0000235 (macrophage), CL:0002496 (cardiac neuron / conduction-system cell — or CL:1000306 nodal myocyte if available).
- UBERON: UBERON:0002018 (atrioventricular node).
- CHEBI: relevant to hydroxychloroquine (CHEBI:5801) mechanistically, not a metabolite of the disease itself.

Sources: [PMC3708308](https://pmc.ncbi.nlm.nih.gov/articles/PMC3708308/), [JEM/PMC2212767](https://pmc.ncbi.nlm.nih.gov/articles/PMC2212767/), [PMID:22013113 — uPA/TGF-β](https://pubmed.ncbi.nlm.nih.gov/22013113/), [PMC3467518](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3467518/), [PMC11120786 — Molecular Mechanisms review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11120786/)

---

## 7. Anatomical Structures Affected

- **Organ level:** Heart (primary, most severe), skin, liver/biliary tree, hematopoietic/blood, CNS (secondary). Body systems: cardiovascular, integumentary, hepatobiliary, hematologic, nervous.
- **Tissue/cell level:** Cardiac conduction system myocytes (AV node specifically — UBERON:0002018), epidermal keratinocytes, hepatic portal tract lymphocytes, macrophages (CL:0000235), megakaryocytes/platelets, neutrophils.
- **Subcellular:** Apoptotic membrane blebs (site of Ro/La surface translocation) — GO Cellular Component: GO:0097169 (nuclear membrane) is not right; more precisely the plasma membrane surface (GO:0005886) via apoptotic bleb formation.
- **Localization:** AV node (UBERON:0002018) for CHB; periorbital/scalp/facial skin for cutaneous disease; liver (UBERON:0002107); no strong lateralization pattern reported.

---

## 8. Temporal Development

- **Onset:** Cardiac manifestations onset **in utero**, virtually always between 18–24 weeks gestation (rarely as late as 30 weeks; postnatal-onset first-degree block is rare). Cutaneous/hepatic/hematologic manifestations are present at birth or emerge in the first weeks to months of postnatal life.
- **Progression:** CHB, once complete (third-degree), is permanent and non-reversible; first/second-degree block may progress to complete block or, with steroid treatment, may partially regress (second→first degree). Cutaneous/hepatic/hematologic disease is self-limited, resolving over 4–12 months.
- **Disease course:** Cardiac NLE is a **chronic, lifelong** condition once complete block is established (pacemaker-dependent); cutaneous/hepatic/hematologic NLE is **self-limited/transient**.
- **Critical window:** Weeks 16–26 gestation is the critical surveillance period (serial fetal echocardiography); this is the therapeutic window for hydroxychloroquine initiation (before 10 weeks gestation) in the PATCH trial protocol.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Not Mendelian — acquired via transplacental antibody transfer. Recurrence in subsequent pregnancies is driven by persistent maternal antibody status, not classical genetic transmission.
- **Epidemiology:**
  - Overall NLE incidence: ~1 in 20,000 US live births.
  - Among anti-SSA/anti-SSB-positive mothers: NLE incidence ~2% in a first at-risk pregnancy.
  - CHB specifically: 1–2% prevalence among anti-Ro-positive pregnant women; 15–30% of NLE cases have CHB overall (with strong regional variation: ~70% in Europe/US cohorts vs. 8.9–23% in Asian cohorts, where cutaneous disease predominates at ~80%).
  - **Recurrence risk:** <1% in mothers with a prior unaffected pregnancy; **15–25%** (some sources cite up to 18–20%) if a prior child had NLE/CHB.
- **Mortality:** Neonatal mortality for cardiac NLE is **20–30%**; a large registry reported 11.8% overall mortality with median 7-year follow-up, 79.1% pacemaker rate, and 18.8% dilated cardiomyopathy rate.
- **Sex ratio:** Overall NLE incidence shows no significant sex difference; cutaneous NLE specifically shows a reported (though inconsistently replicated) male predominance (2:1–3:1 in some series; female predominance in at least one 57-patient registry).
- **Geographic/ethnic distribution:** Notable geoepidemiologic variation — European/American cohorts skew cardiac-predominant, Asian cohorts skew cutaneous-predominant, per systematic individual-patient-data review (PMC7164747). Non-European ancestry is also a reported risk factor for late-onset dilated cardiomyopathy in CHB survivors.

Sources: [JACC — National Neonatal Lupus Registry](https://www.jacc.org/doi/10.1016/S0735-1097(98)00161-2), [PMC7164747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7164747/), [PMC11899241](https://pmc.ncbi.nlm.nih.gov/articles/PMC11899241/)

---

## 10. Diagnostics

- **Maternal serology:** Anti-Ro/SSA (52-kDa and 60-kDa) and anti-La/SSB antibody testing (ELISA/immunoblot) — the essential first-line test in any pregnancy with suspected/known maternal autoimmune disease or an affected prior pregnancy.
- **Fetal cardiac surveillance:** Serial fetal echocardiography with **mechanical PR-interval** (Doppler-derived AV time interval) measurement, weekly from 16–26 weeks gestation (some protocols 18–26 weeks) and biweekly 26–34 weeks, per PRIDE study and subsequent guidance. PR interval >150 ms = first-degree block; >140 ms triggers more frequent monitoring.
- **Postnatal:** ECG/echocardiography for confirmation and grading of AV block; skin biopsy (interface dermatitis with vacuolar degeneration, lymphocytic infiltrate — similar to subacute cutaneous LE) if cutaneous diagnosis is uncertain; direct immunofluorescence may show granular IgG deposition at the dermo-epidermal junction.
- **Laboratory:** CBC (cytopenias), liver function tests (transaminases, bilirubin), ANA/anti-Ro/anti-La titers in the infant (reflecting passive maternal transfer, not endogenous production).
- **Neuroimaging:** Cranial ultrasound recommended in at-risk infants to screen for hydrocephalus/macrocephaly.
- **Differential diagnosis:** Other causes of fetal bradycardia (structural heart disease, long QT syndrome), other neonatal photosensitive dermatoses (e.g., erythema multiforme, tinea), TORCH infections (for hepatosplenomegaly/cytopenias), other causes of cholestatic liver disease in infancy.
- **Screening:** No population-based newborn screening program exists; screening is targeted — any mother with known anti-Ro/anti-La antibodies (with or without overt SLE/Sjögren's) should have anticipatory fetal cardiac and postnatal skin surveillance.

Sources: [PRIDE study, PMID:18195175](https://pubmed.ncbi.nlm.nih.gov/18195175/), [Circulation — Utility of Cardiac Monitoring](https://www.ahajournals.org/doi/10.1161/circulationaha.107.707661), [ISUOG Congenital Heart Block](https://www.isuog.org/education/visuog/obstetrics/heart/other/congenital-heart-block.html)

---

## 11. Outcome/Prognosis

- **Non-cardiac NLE:** Excellent prognosis — cutaneous, hepatic, and hematologic manifestations are self-limited and typically resolve fully within 4–12 months without long-term sequelae (occasional residual dyspigmentation/atrophy in severe cutaneous cases).
- **Cardiac NLE:**
  - Mortality: 20–30% for infants with complete heart block, concentrated in the neonatal/fetal period (hydrops, severe bradycardia, associated endocardial fibroelastosis/cardiomyopathy).
  - With timely pacemaker implantation, long-term survival exceeds 90%, and most survivors achieve normal neurodevelopment.
  - Dilated cardiomyopathy (DCM) is a major late complication: 10-year survival is only **23.1%** for neonatally diagnosed DCM, **53.9%** for late-onset DCM, vs. **98.6%** for CHB infants without DCM.
  - Risk factors for late-onset DCM: non-European ancestry, in-utero mitral regurgitation, pacemaker implantation itself.
  - Pacemaker dependency is lifelong in nearly all complete-block survivors (79.1% pacemaker rate in a large registry).
- **Neurologic NLE:** Generally resolves without sequelae once maternal antibody clears; symptomatic cases (seizures, myelopathy) are rare.
- **Prognostic biomarkers:** Antibody titer/epitope specificity (52-kDa Ro reactivity), degree of AV block at presentation (reversible first/second-degree vs. irreversible third-degree), presence of endocardial fibroelastosis or in-utero valvular regurgitation.

Sources: [ScienceDirect — long-term cardiac dysfunction](https://www.sciencedirect.com/science/article/abs/pii/S000349672401505X), [ScienceDirect — DCM incidence/mortality](https://www.sciencedirect.com/science/article/abs/pii/S0167527317323264), [PMC5578407](https://pmc.ncbi.nlm.nih.gov/articles/PMC5578407/)

---

## 12. Treatment

**Prenatal / preventive (targeting cardiac NLE):**
- **Hydroxychloroquine (CHEBI:5801; NCIT drug class — Pharmacotherapy, NCIT:C15986):** The **PATCH trial** (PMID:32674792) — 400 mg/day started before 10 weeks gestation, continued throughout pregnancy — showed recurrent CHB in only 1 of 17 completed hydroxychloroquine-exposed pregnancies (vs. historical recurrence rate ~18%), a >50% reduction. This is now the leading evidence-based secondary-prevention strategy for anti-Ro-positive mothers with a prior affected pregnancy.
- **Fluorinated corticosteroids (dexamethasone/betamethasone):** Can reverse **first- and second-degree** block (inflammation-driven, pre-fibrotic stage) but have **no effect on established third-degree (complete) block**, since fibrotic replacement of the AV node is structurally irreversible. Carries maternal/fetal risk (growth restriction, oligohydramnios) — use is now more selective/controversial (PMID:10555029).
- **IVIG:** A multicenter prospective observational study (PMID:20131278) at 400 mg/kg found IVIG **ineffective** for CHB prevention; higher-dose (1 g/kg) regimens have shown more promise in smaller/more recent studies (JACC: Clin EP 2022), but this remains investigational, not standard of care.
- **β-agonists (e.g., terbutaline, salbutamol):** used adjunctively for severe fetal bradycardia to maintain ventricular rate in utero.

**Postnatal:**
- **Permanent pacemaker implantation (epicardial in neonates):** definitive treatment for symptomatic/high-grade complete heart block — NCIT:C15329 (Surgical Procedure) / device-based; corresponds to `therapeutic_modality: DEVICE`.
- **Topical corticosteroids and photoprotection (sun avoidance, protective clothing/sunscreen):** mainstay for cutaneous NLE, supportive/symptomatic; NCIT:C15747 (Supportive Care).
- **Supportive care for hepatic/hematologic disease:** typically self-resolving; only symptomatic/severe cytopenias require transfusion support.

**Experimental / future directions:**
- Investigation of immune checkpoint molecule dysregulation in autoimmune CHB (2024 research direction noted in search results) as a potential mechanistic/therapeutic target.
- Belimumab, rituximab, and other B-cell-targeted therapies have been explored in maternal SLE management around pregnancy but are not established NLE-preventive agents.

**NCIT term suggestions:** NCIT:C15986 (Pharmacotherapy, for hydroxychloroquine/steroids with `therapeutic_agent` CHEBI:5801 hydroxychloroquine), NCIT:C15329 (Surgical Procedure, pacemaker), NCIT:C15747 (Supportive Care).

Sources: [PATCH trial JACC](https://www.jacc.org/doi/abs/10.1016/j.jacc.2020.05.045), [PMC7394202](https://pmc.ncbi.nlm.nih.gov/articles/PMC7394202/), [Pisoni IVIG study](https://onlinelibrary.wiley.com/doi/abs/10.1002/art.27350), [JACC Clin EP 2022 — high-dose IVIG](https://www.jacc.org/doi/10.1016/j.jacep.2022.12.014)

---

## 13. Prevention

- **Primary prevention:** Pre-conception counseling/screening for anti-Ro/anti-La antibodies in women with known or suspected autoimmune disease (SLE, Sjögren's) planning pregnancy; the 2024 Bankole & Nwaonu review explicitly recommends NLS-antibody screening occur *before* pregnancy as a collaborative rheumatology-obstetrics practice.
- **Secondary prevention:** Hydroxychloroquine for anti-Ro/La-positive women, particularly those with a prior affected pregnancy (per PATCH trial protocol, started pre-10 weeks gestation).
- **Screening/early detection:** Serial fetal echocardiography (mechanical PR interval) from 16–26 weeks gestation in all anti-Ro/anti-La-positive pregnancies, enabling detection of early (reversible) AV block before progression to complete block.
- **Genetic counseling:** Not classical Mendelian counseling (no causal fetal genotype), but risk counseling on recurrence rates (15–25% after one affected pregnancy) is standard practice for affected families.
- **No vaccine or population-level public health intervention applies** (not infectious/environmental in a classical sense).

Sources: [SAGE review 2024 (Bankole & Nwaonu)](https://journals.sagepub.com/doi/10.1177/00368504241278476), [PMC6099126 — provider practice survey](https://pmc.ncbi.nlm.nih.gov/articles/PMC6099126/)

---

## 14. Other Species / Natural Disease

No robust literature was identified describing naturally occurring NLE-like disease in companion animals or wildlife (OMIA search did not surface a canine/feline analog in this research pass). This is consistent with NLE being a human-specific, antibody/placenta-mediated acquired condition tied to human IgG transplacental transport physiology (FcRn-mediated) and human Ro/La antigen epitopes.

---

## 15. Model Organisms

- **Passive-transfer murine models:** IgG purified from anti-Ro/La-positive mothers (or affinity-purified anti-Ro60/anti-Ro52 antibodies) injected into pregnant mice have been used to study antibody-mediated cardiac conduction abnormalities, supporting both the apoptosis and calcium-channel hypotheses (e.g., work underlying PMC2212767, Ro/SSA autoantibodies directly bind cardiomyocytes, JEM 2005).
- **In vitro/ex vivo models:** Cultured human fetal cardiomyocytes and keratinocytes have been central to demonstrating apoptosis-induced surface translocation of Ro60/La and the requirement for hY3 RNA (PMC3708308); isolated perfused fetal/neonatal heart preparations have been used to test T-type calcium channel (Cav3.1/α1G) blockade by anti-Ro antibodies (PMC3767782).
- **Limitations:** Mouse models lack a direct anatomic/physiologic analog of the human fetal AV nodal remodeling window and human-specific Ro52/TRIM21 antigenicity, so translational fidelity for the exact CHB timing (18–24 weeks in humans) is imperfect — an appropriate `HUMAN_MODEL_MISMATCH` candidate for dismech curation, since these models demonstrate antibody-calcium channel/apoptosis interactions but do not fully recapitulate the human developmental timing or AV-node-specific fibrotic outcome.
- **General lupus mouse models** (e.g., MRL/lpr) are relevant to maternal SLE pathogenesis broadly but are not NLE-specific models.

Sources: [PMC3708308](https://pmc.ncbi.nlm.nih.gov/articles/PMC3708308/), [Wiley — Role of Calcium Channels in CHB](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-3083.2010.02439.x), [PMC3767782](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3767782/)

---

## Summary Table: Suggested Ontology Bindings for Curation

| Concept | Suggested Term |
|---|---|
| Disease | MONDO:0018360; ORPHA:398124 |
| Complete heart block | HP:0011705 |
| First-degree AV block | HP:0011706 (or general HP:0001680) |
| Dilated cardiomyopathy | HP:0001635 |
| Photosensitive annular rash | HP:0025426 + skin lesion terms |
| Hydrocephalus | HP:0000238 |
| Macrocephaly | HP:0000256 |
| Thrombocytopenia | HP:0001873 |
| Neutropenia | HP:0001875 |
| Cholestasis | HP:0001396 |
| Ro60 antigen gene | hgnc:11313 (TROVE2) |
| Ro52/TRIM21 gene | hgnc:11312 (TRIM21) |
| La/SSB gene | hgnc:10646 (SSB) |
| AV node | UBERON:0002018 |
| Macrophage | CL:0000235 |
| Cardiac muscle cell | CL:0000746 |
| Apoptotic process | GO:0006915 |
| TGF-beta signaling | GO:0007179 (modifier: INCREASED) |
| Hydroxychloroquine | CHEBI:5801 |
| Pharmacotherapy | NCIT:C15986 |
| Surgical procedure (pacemaker) | NCIT:C15329 |

---

### Full Source List

- [An Overview of Neonatal Lupus with Anti-Ro Characteristics (PMC8431034)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8431034/)
- [Neonatal Lupus Erythematosus (PMC3437607)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3437607/)
- [Neonatal Lupus Erythematosus - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK526061/)
- [Anti-Ro antibodies and neonatal lupus - PubMed](https://pubmed.ncbi.nlm.nih.gov/2657894/)
- [Case Report: Siblings with NLE (PMC11911384)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11911384/)
- [Medscape — Neonatal and Pediatric LE](https://emedicine.medscape.com/article/1006582-overview)
- [Neonatal lupus erythematosus: an acquired autoimmune disease to be taken seriously (PMC11899241, 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11899241/)
- [Same, Taylor & Francis full text](https://www.tandfonline.com/doi/full/10.1080/07853890.2025.2476049)
- [Complete heart block in neonatal lupus (PMC8596036)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8596036/)
- [JACC — National Neonatal Lupus Registry](https://www.jacc.org/doi/10.1016/S0735-1097(98)00161-2)
- [Geoepidemiology systematic review (PMC7164747)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7164747/)
- [52-kDa Ro/SSA epitopes (PMC1526571)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1526571/)
- [UpToDate — Neonatal lupus management](https://www.uptodate.com/contents/neonatal-lupus-management-and-outcomes)
- [Orphanet — NLE](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=398124)
- [MalaCards — NLE](https://www.malacards.org/card/neonatal_lupus_erythematosus)
- [NORD — Neonatal Lupus](https://rarediseases.org/rare-diseases/neonatal-lupus/)
- [PATCH trial PubMed (PMID:32674792)](https://pubmed.ncbi.nlm.nih.gov/32674792/)
- [PATCH trial PMC (PMC7394202)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7394202/)
- [ClinicalTrials.gov NCT01379573](https://clinicaltrials.gov/study/NCT01379573)
- [DermNet NZ — NLE](https://dermnetnz.org/topics/neonatal-lupus-erythematosus)
- [A Neonate With Annular Cutaneous Lesions (PMC7417094)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7417094/)
- [Karnabi 2010 — Calcium Channels in CHB](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-3083.2010.02439.x)
- [Congenital Heart Block Maternal Sera Target α1G T-Type Calcium Channel (PMC3767782)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3767782/)
- [Liver disease in NLE — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S002234760582880X)
- [Early cholestasis in NLE (PMC3101731)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3101731/)
- [Molecular Mechanisms of Fetal and Neonatal Lupus review (PMC11120786)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11120786/)
- [A review of neonatal lupus syndrome, Bankole & Nwaonu 2024 (SAGE)](https://journals.sagepub.com/doi/10.1177/00368504241278476)
- [Same, PMC11418246](https://pmc.ncbi.nlm.nih.gov/articles/PMC11418246/)
- [Genetics of NLE Risk and Specific Manifestations — J Rheumatol 2025](https://www.jrheum.org/content/52/1/52)
- [Lupus Foundation of America — SLE genetics not associated with NLE](https://www.lupus.org/news/systemic-lupus-erythematosus-genetics-not-associated-with-neonatal-lupus-outcomes)
- [PR Interval and Dexamethasone Evaluation (PRIDE) study, PMID:18195175](https://pubmed.ncbi.nlm.nih.gov/18195175/)
- [Circulation — Utility of Cardiac Monitoring in Fetuses at Risk for CHB](https://www.ahajournals.org/doi/10.1161/circulationaha.107.707661)
- [ISUOG — Congenital Heart Block](https://www.isuog.org/education/visuog/obstetrics/heart/other/congenital-heart-block.html)
- [Factors associated with long-term cardiac dysfunction in NLE — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S000349672401505X)
- [Incidence/risk factors/mortality of DCM in cardiac NLE — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167527317323264)
- [Progress in pathogenesis/treatment of cardiac NLE (PMC5578407)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5578407/)
- [Pisoni 2010 — Failure of IVIG (PMID:20131278)](https://pubmed.ncbi.nlm.nih.gov/20131278/)
- [JACC Clin EP 2022 — High-dose IVIG scheme](https://www.jacc.org/doi/10.1016/j.jacep.2022.12.014)
- [Fluorinated glucocorticoids comparison — PMID:10555029](https://pubmed.ncbi.nlm.nih.gov/10555029/)
- [Provider practice survey (PMC6099126)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6099126/)
- [Ro60 Requires Y3 RNA for Surface Exposure (PMC3708308)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3708308/)
- [Ro/SSA autoantibodies directly bind cardiomyocytes — JEM (PMC2212767)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2212767/)
- [uPA/uPAR TGF-β activation, PMID:22013113](https://pubmed.ncbi.nlm.nih.gov/22013113/)
- [Connecting molecular dots — cardiac NLE pathogenesis (PMC3467518)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3467518/)
- [Hydrocephalus and macrocephaly in NLE, PMID:17330304](https://pubmed.ncbi.nlm.nih.gov/17330304/)
- [Nature Reviews Rheumatology — Hydrocephalus and NLE](https://www.nature.com/articles/ncprheum0490)
- [NEJM 1987 — U1RNP-associated Neonatal Lupus Syndrome](https://www.nejm.org/doi/abs/10.1056/NEJM198704303161807)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 35 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC3437607` *(abstract only)*: "an example of passively acquired autoimmunity in which the influx of maternal autoantibodies... transiently affects fetal and neonatal organ systems"
  - closest text in source: "Neonatal lupus erythematosus (NLE) refers to a clinical spectrum of cutaneous, cardiac, and systemic abnormalities observed in newborn infants whose mothers have autoantibodies against Ro/SSA and La/SSB"