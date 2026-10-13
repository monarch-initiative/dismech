---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-13T20:16:46.363717'
end_time: '2026-10-13T20:18:09.213797'
duration_seconds: 82.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cataract 48
  mondo_id: MONDO:0032735
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 9
  total_cost_usd: 1.5539444999999998
  session_id: 169666a9-34f2-4fce-892d-2a7275c6c574
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 2
citation_count: 13
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:14506234
  relevance_assessed: 7
  on_topic: 4
  off_topic: 1
  off_topic_references:
  - PMID:14506234
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 18
  verified: 17
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  unresolvable_prefixes:
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 48
- **MONDO ID:** MONDO:0032735 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cataract 48** covering all of the
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

Status: I've read the existing entry and its cached sources, and found OMIM 618415. Running one more search for other DNMBP cataract reports, then I'll write the report.

# Cataract 48 (CTRCT48; DNMBP-related autosomal recessive infantile cataract): research report

**Scope.** Only two publications report human DNMBP cataract: the 2018 gene-discovery paper (PMID:30290152) and one 2023 Turkish exome cohort (PMID:37592116). Web searches for 2024–2026 reports, including Chinese, Indian and Saudi pediatric cataract cohorts, found nothing new. The PubMed search tool was not authorized this session, so I checked abstracts against the local `references_cache/` files and web search. A PubMed search filtered to 2024 onward would be the next step to confirm nothing newer exists.

Quotes below are copied from the cached abstracts or full text.

---

## 1. Disease information

- **Definition.** A non-syndromic, autosomal recessive cataract with bilateral lens opacity starting in infancy. It is caused by biallelic loss-of-function variants in *DNMBP* on chromosome 10q24. OMIM-derived records describe it as "characterized by infantile or early-childhood cataracts and visual impairment" ([MGI disease page, OMIM:618415](https://informatics.jax.org/disease/OMIM:618415)).
- **Identifiers.**
  - MONDO:0032735 (cataract 48)
  - OMIM 618415
  - Gene: DNMBP, `hgnc:30373`
  - Orphanet: no DNMBP-specific record found. It falls under Orphanet's general early-onset non-syndromic cataract grouping.
  - ICD-10: Q12.0 (congenital cataract)
  - MeSH: Cataract / Cataract, congenital
- **Synonyms.** CTRCT48; DNMBP-related cataract; autosomal recessive infantile cataract, DNMBP-related.
- **Data source.** Everything known comes from individual families: 12 affected people in 3 Pakistani families, plus 1 Turkish proband. There is no registry or EHR data.

## 2. Etiology

- **Cause.** Homozygous truncating *DNMBP* variants. "We therefore conclude that DNMBP loss-of-function variants cause infantile-onset cataracts in humans" (PMID:30290152).
- **Genetic risk factor.** Consanguinity. Every confirmed homozygous family was consanguineous; the Turkish Family 6 proband was the child of a first-cousin marriage.
- **Environmental, protective and gene–environment factors.** None reported. Not applicable to a fully penetrant Mendelian lens defect as far as the literature shows.

## 3. Phenotypes

| Phenotype | Suggested HPO | Onset | Frequency | Source |
|---|---|---|---|---|
| Bilateral infantile cataract | HP:0000519 Developmental cataract (or HP:0000518 Cataract; laterality via HP:0012832 Bilateral) | Infancy | 12/12 Pakistani; 1/1 Turkish | PMID:30290152 ("The phenotypes of all affected individuals include infantile-onset cataracts."); PMID:37592116 |
| Lamellar cataract | HP:0007971 Lamellar cataract | Diagnosed at 5 months | 1/1 homozygous Turkish proband | PMID:37592116 ("…received the diagnosis of bilateral lamellar…") |
| Visual impairment | HP:0000505 Visual impairment | Infancy | Not quantified | OMIM-derived summary only |

- **Gaps.**
  - The Pakistani abstract does not state the cataract morphology.
  - No reports of nystagmus, amblyopia or aphakic glaucoma, and no extra-ocular features. The disease is reported as non-syndromic.
- **Quality of life.** No disease-specific data. The general burden is that of infantile cataract: risk of deprivation amblyopia and lifelong optical correction after surgery.

## 4. Genetics and molecular information

**Gene.** *DNMBP* encodes Tuba (dynamin-binding protein). It is a multi-SH3 scaffold with a central Dbl homology (DH) domain and a BAR domain (PMID:14506234).

**Reported alleles.** All are homozygous unless noted.

| Variant | Type | Family / population | Classification |
|---|---|---|---|
| c.811C>T p.(Arg271*) | Nonsense | F385, Pakistani, 9 affected, LOD 5.18 at θ=0 | Pathogenic (segregation) |
| c.2947_2948del p.(Asp983*) | Frameshift → stop | F372, Pakistani, 2 affected | Pathogenic / likely pathogenic |
| c.2852_2855del p.(Thr951Metfs*41) | Frameshift | F3, Pakistani, 1 affected | Likely pathogenic |
| c.1918C>T p.(Arg640*) (NM_015221.4) | Nonsense | Turkish Family 6 | Novel; reported as LoF ("the second study in the literature that reports bi-allelic loss-of-function") |
| c.395G>A p.(Gly132Glu) + c.960G>T p.(Gln320His) (NM_001318326.2) | Compound heterozygous missense | Non-consanguineous Turkish child with lamellar cataract | VUS; should not count as confirmed CTRCT48 |

- **Variant origin.** Germline. Parents were heterozygous carriers.
- **Functional consequence.** Loss of function. The truncations remove the DH (Cdc42 GEF) domain and the C-terminal domains.
- **Not reported.** Modifier genes, epigenetic findings, chromosomal abnormalities and population allele frequencies for these specific variants (check gnomAD per variant).
- **ClinGen.** No gene-disease validity classification was found in the local cache.

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious contribution has been reported.

## 6. Mechanism and pathophysiology

**Causal chain.** Steps 4 and 5 are inferred, not shown in a lens.

1. Biallelic truncating *DNMBP* variants **lead to** loss of Tuba protein, or of its DH domain at least. *Inferred from variant class; no patient protein studies.*
2. Loss of Tuba **removes** a Cdc42-specific guanine nucleotide exchange factor.
   - "A Dbl homology domain present in the middle of Tuba … activates Cdc42, but not Rac and Rho" (PMID:14506234, in vitro).
3. Reduced local Cdc42 / N-WASP activity at the apical junction **results in** disordered junctional F-actin and E-cadherin assembly, with "curved and slack" junctions.
   - "At the subcellular level, Tuba inactivation modified the assembly pattern of junctional F-actin and E-cadherin."
   - "Suppression of Cdc42 activity or depletion of N-WASP … mimicked the effects of Tuba depletion."
   - Source: PMID:17015620, cultured non-lens epithelial cells.
4. In the eye, junction disorganization **affects** the cells that build the lens.
   - Fly evidence: knockdown of the ortholog *sif* "affects the development of these cells as well as the localization of E-cadherin, alters the distribution of septate junctions in adjacent cone cells," and cuts ERG amplitude by about 50% (PMID:30290152, *Drosophila*).
   - *Extrapolation to vertebrate lens epithelium is untested.*
5. Disrupted E-cadherin-dependent lens development **is proposed to cause** loss of lens transparency.
   - "E-cadherin has an important role in lens vesicle separation and lens epithelial cell survival in humans" (PMID:30290152).
   - This is the authors' background rationale, not an experimental result.
6. Loss of lens transparency **produces** bilateral infantile, sometimes lamellar, cataract and visual impairment.

**Ontology suggestions.**

| Category | Suggested terms |
|---|---|
| GO | GO:0005085 guanyl-nucleotide exchange factor activity (Cdc42-specific); GO:0034332 adherens junction organization; GO:0120193 tight junction organization; GO:0036438 maintenance of lens transparency; GO:0002088 lens development in camera-type eye |
| CL | CL:0002224 lens epithelial cell; CL:0011004 lens fiber cell |
| GO cellular component | apical junction complex; adherens junction; tight junction; actin cortex |

**Profiling.** There are no transcriptomic, proteomic, metabolomic or single-cell studies of DNMBP cataract.

## 7. Anatomy

| Level | Affected structures |
|---|---|
| Organ / tissue | Lens: UBERON:0000965 lens of camera-type eye; lens epithelium; lens fibers |
| Subcellular | Cell–cell junctions: adherens and tight junctions |
| Laterality | Bilateral in all reported cases |

There is no secondary organ involvement.

## 8. Temporal development

- **Onset.** Infantile. The Turkish proband was diagnosed at 5 months and had surgery at 11 months.
- **Progression.** Natural history is not described. As with other developmental cataracts, the opacity is presumed to be stable or slowly progressive.
- **Critical period.** The amblyopia window in the first months of life is when surgery and optical rehabilitation matter most. This is general infantile-cataract knowledge, not DNMBP-specific.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007), with complete penetrance in the families reported.
- **Prevalence.** Unknown. There are 4 confirmed families: 3 Pakistani and 1 Turkish.
- **Founder effect, carrier frequency and sex ratio.** Not reported. Sexes are not separately described in the abstract.
- **Population pattern.** Concentrated in consanguineous populations.

## 10. Diagnostics

- **Clinical exam.** Slit-lamp examination and red-reflex testing. CTRCT48 cannot be clinically distinguished from other infantile cataracts.
- **Genetic testing.** Exome sequencing or a congenital-cataract gene panel. Confirm DNMBP is included, since it is a rarely tested gene. Follow with segregation analysis.
  - Suggested NCIT term: NCIT:C101295 Whole Exome Sequencing.
  - In the Turkish cohort, exome sequencing found a pathogenic or likely pathogenic variant in 7 of 12 families (58%) (PMID:37592116).
- **Biomarkers.** None.
- **Differential diagnosis.** Other autosomal recessive infantile cataracts (e.g., *LSS*, *FYCO1*, *CRYBB1*, *GCNT2*); dominant crystallin and connexin cataracts; and syndromic or metabolic cataracts, such as galactosemia, which should be excluded biochemically.

## 11. Outcome and prognosis

- Life expectancy is expected to be normal. There are no systemic features.
- Visual outcome depends on timely surgery and amblyopia management. No DNMBP-specific outcome data exist.

## 12. Treatment

- **Surgery.** Lensectomy or cataract extraction (NCIT:C157809 Cataract Surgery), followed by aphakic or IOL optical correction. Both Turkish DNMBP probands had surgery at 11 months.
- **Rehabilitation.** Amblyopia therapy, such as occlusion.
- **Other therapies.** There is no pharmacological, gene-targeted or other DNMBP-specific therapy, and no clinical trials.

## 13. Prevention

- Genetic counseling for consanguineous families, with a 25% recurrence risk for parents who are both carriers.
- Carrier testing and prenatal or preimplantation testing are possible once the familial variant is known.
- Early detection through newborn red-reflex screening.

## 14. Other species

- No naturally occurring DNMBP cataract is recorded in OMIA from this search.
- *Drosophila* ortholog: *still life* (*sif*).

## 15. Model organisms

- **Drosophila *sif* RNAi** (PMID:30290152). Knockdown disrupts development of the lens-secreting cells, E-cadherin localization and septate-junction distribution, and roughly halves ERG amplitude in young flies.
  - Limitation: the insect corneal lens is a secreted cuticular structure, not a crystallin-filled cellular lens. The model shows a junctional defect, not opacity.
- **Vertebrate models.** No vertebrate (mouse or zebrafish) lens model of DNMBP loss has been described. This is the main gap in the evidence for the mechanism.
- **In vitro.** Tuba knockdown in simple epithelial cell lines (PMID:17015620) is the main mechanistic system.

---

## Key evidence gaps

1. Only 4 confirmed families have been reported.
2. Cataract morphology in the Pakistani families is not in the abstract.
3. No vertebrate lens model exists.
4. There is no ClinGen classification.
5. Whether the Turkish compound-heterozygous missense variants are pathogenic is unresolved.

## Note on the existing knowledge base entry

`kb/disorders/Cataract_48.yaml` already covers this material: the same 4 alleles, the causal chain marked as inferred, Drosophila model caveats, and surgery evidence. This report found no new primary literature that would change the entry.

**Sources**
- PMID:30290152, Ansar et al., *Am J Hum Genet* 2018, [doi:10.1016/j.ajhg.2018.09.004](https://doi.org/10.1016/j.ajhg.2018.09.004); [PMC6174361](https://pmc.ncbi.nlm.nih.gov/articles/PMC6174361)
- PMID:37592116, Türkyılmaz et al., *Int Ophthalmol* 2023, [doi:10.1007/s10792-023-02857-1](https://doi.org/10.1007/s10792-023-02857-1)
- PMID:14506234 (Tuba, Cdc42-specific DH domain); PMID:17015620 (Tuba regulates junction configuration)
- [MGI disease page, OMIM:618415](https://informatics.jax.org/disease/OMIM:618415)
- [FlyBase FBrf0240231](https://flybase.org/reports/FBrf0240231)
- [Texas Children's news release](https://www.texaschildrens.org/content/news-release/research-reveals-novel-link-between-congenital-cataracts-and-dynamin-binding)
- [KTU AVESIS record of the Turkish study](https://avesis.ktu.edu.tr/yayin/26936448-0fa9-4d40-9213-8c3883ac67a9/identification-of-novel-variants-in-turkish-families-with-non-syndromic-congenital-cataracts-using-whole-exome-sequencing)
- [GeneBe DNMBP](https://genebe.net/gene/hg38/DNMBP)
- [Houston Methodist scholars page](https://scholars.houstonmethodist.org/en/publications/bi-allelic-loss-of-function-variants-in-dnmbp-cause-infantile-cat/)
- [EyeSmart](https://eyesmart.com.au/newsarticle/5617-dynamin-binding-protein-linked-to-congenital-cataracts), [Medical Dialogues](https://speciality.medicaldialogues.in/dynamin-binding-protein-linked-to-congenital-cataract), [CRST Europe](https://crstodayeurope.com/news/dynamin-binding-protein-linked-to-congenital-cataracts/2479813/), [NZ Optics](https://nzoptics.co.nz/live-articles/fly-eyes-link-dnmbp-to-congenital-cataracts)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:14506234` *(abstract only)*: "A Dbl homology domain present in the middle of Tuba … activates Cdc42, but not Rac and Rho"
  - closest text in source: "A Dbl homology domain present in the middle of Tuba upstream of a Bin/amphiphysin/Rvs (BAR) domain activates Cdc42, but not Rac and Rho, and may thus cooperate with the C terminus of the protein in regulating actin assembly"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:14506234` (3 mentions) - Tuba, a novel protein containing bin/amphiphysin/Rvs and Dbl homology domains, links dynamin to regulation of the actin cytoskeleton.
  - shared terms: tuba

Weighed against this report's own most characteristic terms: `cataract`, `dnmbp`, `turkish`, `variant`, `lens`, `infantile`, `found`, `familie`, `pakistani`, `surgery`, `proband`, `tuba`, `affected`, `bilateral`, `gene`, `abstract`, `amblyopia`, `autosomal`, `recessive`, `visual`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

17 of 18 terms resolved to a current term; the rest could not be looked up either way.