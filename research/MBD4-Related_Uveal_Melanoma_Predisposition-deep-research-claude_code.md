---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T14:22:12.788891'
end_time: '2026-10-15T14:23:14.995748'
duration_seconds: 62.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: MBD4-Related Uveal Melanoma Predisposition
  mondo_id: MONDO:0011695
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.6981005000000001
  session_id: aa4f0803-31cb-5b9b-8409-a0195ed1b485
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC9118112
  relevance_assessed: 4
  on_topic: 4
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 12
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0002863
    reported_labels:
    - MDS
    ontology_label: Myelodysplasia
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MBD4-Related Uveal Melanoma Predisposition
- **MONDO ID:** MONDO:0011695 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MBD4-Related Uveal Melanoma Predisposition** covering all of the
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

# MBD4-Related Uveal Melanoma Predisposition: Research Report

**Source and verification status.** This report comes from three standard web searches. I read search-result summaries and snippets, not full papers. I did not open the full Derrien, Palles, Sanders or Rodrigues papers, and the supplied sources do not cover several template sections (flagged "Not retrieved"). Items marked **[unverified, from background knowledge]** are lead-class model recall, not sourced. They must not go into YAML without a primary-source check. I give PMC or URL identifiers rather than PMIDs where I did not see the PMID in a result. Every CURIE below is a suggestion that needs an OAK or cache lookup before binding.

**Lump/split flag.** The entry name "MBD4-Related Uveal Melanoma Predisposition" conflates two genetic states, and the sources diverge sharply on them.
- **Biallelic germline MBD4 loss** is an autosomal recessive multi-tumor syndrome, MBD4-associated neoplasia syndrome (MANS). It is established in the sources I saw (Palles et al. 2022, PMC9118112; NCI PDQ).
- **Monoallelic germline MBD4 loss plus somatic loss of the second allele in the tumor** is the uveal melanoma (UM) predisposition described by Derrien et al. The risk estimates are large but contested. A Finnish series found germline loss-of-function (LoF) variants rare in UM, and the NCI PDQ summary, as relayed by the Haematologica review, calls the heterozygous-risk data conflicting.

I could not tell from the search results which of these MONDO:0011695 actually represents. **Check this before curation.** If the term is the UM-predisposition concept, a possible split is a MANS entry (recessive, multi-tumor) plus a UM-predisposition entry or `has_subtypes` row. Keep germline syndromes separate from the somatic tumors they predispose to (design-decisions §3a).

## 1. Disease Information

- **Overview.** MBD4 encodes a DNA glycosylase in base excision repair (BER). It removes thymine from G:T mismatches created by deamination of 5-methylcytosine. Loss produces a CpG>TpG (C>T) hypermutator phenotype. Tumors in carriers are hypermutated with a CpG>TpG excess. Source classes: primary literature (Derrien 2021, Rodrigues 2018) and the NCI PDQ summary, via search snippets.
- **Identifiers.** MONDO:0011695 comes from the template and I did not verify it. OMIM, Orphanet, ICD and MeSH identifiers: **Not retrieved.**
- **Synonyms.** "MBD4-associated neoplasia syndrome (MANS)" appears in the NCI PDQ title. "Germline MBD4 deficiency / multi-tumor predisposition syndrome" appears in the JCI Insight reference-list title.
- **Individual or aggregated data.** The evidence is individual-level: case reports, family series and consecutive UM cohorts. No aggregated disease-level resource was reviewed.

## 2. Etiology

- **Causal factor.** Germline LoF variants in MBD4.
  - Biallelic: "autosomal recessive, multi-organ tumor predisposition syndrome… five individuals with bi-allelic MBD4 variants within four families, with histories of adenomatous colorectal polyposis, acute myeloid leukemia, and uveal melanoma" (Palles et al. 2022, PMC9118112, via search snippet).
  - Monoallelic: Derrien et al. (JNCI 2021, PMC7781447 per search listing) report "8 deleterious MBD4 mutations in the consecutive UM series, a 9.15-fold (95% CI = 4.24–19.73) increased incidence compared with the general population." Tumors carrying them "were all associated with high tumor mutation burden and a CpG>TpG hypermutator phenotype."
  - A larger Curie series, per the Institut Curie listing: 23/896 UM patients carried a germline P/LP MBD4 variant, relative risk 31.44. I only saw the snippet.
- **Contrary evidence.** Repo et al. 2020 reported germline LoF MBD4 variants rare in Finnish UM patients (via Haematologica snippet). A 2024 study found UM and other tumors in 25 families with monoallelic variants (PMID:38060262, title only). Its findings were not retrieved.
- **Environmental and protective factors, gene-environment interactions.** Not retrieved. UV is not established in UM etiology, and I did not source this.
- **Modifier genes.** Not retrieved.

## 3. Phenotypes

Source for the table: Palles et al. 2022 (biallelic); Derrien 2021 (monoallelic). Frequencies, onset and quality-of-life data were not retrieved, so no percentages are given.

| Phenotype | Candidate HP term | Context |
|---|---|---|
| Uveal melanoma | HP:0007716 (uveal melanoma) **[unverified]** | Both monoallelic and biallelic |
| Colorectal adenomatous polyposis | HP:0005227 **[unverified]** | Biallelic |
| Acute myeloid leukemia | HP:0004808 **[unverified]** | Biallelic and Sanders 2018 (see below) |
| Clonal hematopoiesis / MDS | HP:0002863 (MDS) **[unverified]** | Haematologica review snippet |
| Schwannomatosis | not verified | NCI PDQ testing criteria mention it |

- **Pediatric framing.** The sources I saw do not give onset ages. Whether MANS has pediatric onset is **not established here.** The question needs the case-level ages in Palles 2022 and Sanders 2018.

## 4. Genetic/Molecular

- **Gene.** MBD4 (HGNC symbol; use the lowercase `hgnc:` form, ID not looked up).
- **Variants.** LoF (nonsense, frameshift, splice and similar), but the specific variants and ACMG classes were not retrieved. Population allele frequencies (gnomAD) were not retrieved.
- **Somatic second hit.** Heterozygous germline variants with somatic loss of the wild-type allele are reported in UM (Haematologica snippet). Rodrigues et al. 2018 (PMC5951831) describe a "germline deleterious mutation, and somatic MBD4 inactivation in the tumor" in an exceptional anti-PD-1 responder.
- **Signature.** SBS1 (clock-like CpG>TpG), seen in the colorectal adenomas of MBD4-deficient individuals (Palles 2022).
- **ClinGen validity.** Not retrieved. Do not infer a tier.
- **Epigenetics and chromosomal abnormalities.** Not retrieved.

## 6. Mechanism: causal chain

1. Germline LoF in one or both MBD4 alleles. In the monoallelic case, somatic loss of the second allele in the tumor (reported, PMC5951831) creates biallelic deficiency in that tissue.
2. MBD4 no longer removes thymine from G:T mismatches arising from deamination of 5-methylcytosine (function per Palles 2022 snippet).
3. Unrepaired mismatches are replicated, which leads to CpG>TpG substitutions and the SBS1-dominant mutator phenotype (Palles 2022; Derrien 2021).
4. The accumulating mutations probably include driver hits (inferred; the specific UM drivers were not retrieved), which leads to tumor formation in tissues at risk: uveal melanocytes, colonic epithelium, hematopoietic cells.
5. In UM, the result is a hypermutated tumor, unusual for a typically low-TMB cancer (Derrien 2021).
6. Hypermutation likely increases neoantigen load, which leads to checkpoint-inhibitor sensitivity. This is inferred and is supported only by case and cohort data (see §12).

- **Why UM specifically** is unexplained in the sources I saw. Treat that as a gap.
- **Suggested GO terms [unverified]:** base-excision repair (GO:0006284), DNA N-glycosylase activity (GO:0019104). Cell types: melanocyte (CL:0000148), hematopoietic stem cell (CL:0000037), colonic epithelial cell. Verify all by lookup.
- **Omics, single-cell, spatial and functional screens.** Not retrieved.

## 7. Anatomical structures

- **Uvea and eye:** uveal tract (UBERON:0001768 **[unverified]**). Laterality was not retrieved.
- **Colon** (adenomas) and **bone marrow** (AML, clonal hematopoiesis).
- **Subcellular:** nucleus.
- **Metastatic site:** metastatic UM is treated in the cohort below. The metastatic sites (the liver is typical for UM) were not sourced in my results.

## 8. Temporal development

- **Onset, progression, remission.** Not retrieved.
- **Critical periods.** Not retrieved. MANS onset in childhood versus adulthood is the key open question for the pediatric framing.

## 9. Inheritance and population

- **Biallelic:** autosomal recessive (Palles 2022).
- **Monoallelic UM predisposition:** autosomal dominant-like with tumor-level second hit, but penetrance is undefined.
- **Case counts.** The NCI PDQ summary cites nine reported cases, and a later Portuguese series reports 11 individuals from eight families (search-result snippets; I did not open the primary papers).
- **Prevalence and incidence, founder effects, carrier frequency, sex ratio.** Not retrieved. Derrien's 9.15-fold and the Curie RR of 31.44 are relative figures, not penetrance. They need the denominators in the papers.

## 10. Diagnostics

- **Testing.** NCI PDQ suggests germline testing for "AML patients with high mutational burden enriched for CG>GT variants, or with a history of colonic polyposis, schwannomatosis, or uveal melanoma" (snippet, paraphrased by the search tool).
- **Tumor sequencing.** A CpG>TpG-dominant, high-TMB profile in a UM should prompt MBD4 testing (inferred from Derrien 2021 and Rodrigues 2018).
- **Everything else.** GTR panels, GeneReviews and guidelines: **Not retrieved.** Differential diagnosis and screening protocols: **Not retrieved.**

## 11. Prognosis

Not retrieved for the predisposition syndrome. The only outcome data I have are for metastatic UM treated with checkpoint inhibitors (see §12).

## 12. Treatment

- **Checkpoint inhibitors.**
  - Rodrigues et al. 2018 (PMC5951831): a single metastatic UM patient with "exceptional high sensitivity to a PD-1 inhibitor" and an outlier CpG>TpG mutation burden.
  - Saint-Ghislain et al. 2022 (Eur J Cancer), per a search summary: 300 metastatic UM patients on checkpoint inhibitors; 5 of the 131 sequenced tumors (3.8%) carried MBD4 mutations; 3 of 5 MBD4-mutant patients responded versus about 4% of wild-type; the summary gave median PFS of 4.0 months (wild-type) versus 22.3 months (mutant). The numbers rest on five patients, and I did not verify them in the full paper. The authors propose MBD4 as a tissue-agnostic biomarker.
  - Whether TMB alone explains the response is unresolved.
- **Suggested NCIT terms [unverified]:** immunotherapy (NCIT:C15262), Pharmacotherapy (NCIT:C15986, from the repo guidance). Candidate `therapeutic_agent` entries are anti-PD-1 agents such as pembrolizumab and nivolumab (look up the CHEBI or NCIT agent term). No specific drug or regimen was named in my search results, so I should not assert one.
- **Surveillance** (colonoscopy, ophthalmologic exam, hematologic monitoring): **Not retrieved**, and I will not infer guidelines.
- **Clinical trials, pharmacogenomics, advanced therapeutics:** Not retrieved.

## 13. Prevention

Not retrieved. Genetic counseling and cascade testing follow from the recessive and dominant-like inheritance, but I have no sourced guideline.

## 14–15. Other species and model organisms

Not retrieved. I know of Mbd4 knockout mice in the literature **[unverified, from background knowledge]**, but I did not search for them or their phenotypes.

## Gaps to close before curation

1. Confirm the scope of MONDO:0011695 (see the lump/split flag).
2. Pull Derrien 2021 (PMC7781447), Palles 2022 (PMC9118112) and Rodrigues 2018 (PMC5951831) in full, to get exact snippets, PMIDs, variant lists and ages.
3. Get Sanders 2018 (Blood, MBD4 and clonal hematopoiesis/AML) and Saint-Ghislain 2022. I know them only from search-result summaries.
4. Get ClinGen validity, GeneReviews and Orphanet, and a surveillance guideline, if any exists.
5. Resolve the contested heterozygous risk by reading Repo 2020 and PMID:38060262 against Derrien.

## Sources (search-result level)

- [Derrien et al. 2021, PMC7781447](https://pmc.ncbi.nlm.nih.gov/articles/PMC7781447)
- [Palles et al. 2022, PMC9118112](https://pmc.ncbi.nlm.nih.gov/articles/PMC9118112)
- [Rodrigues et al. 2018, PMC5951831](https://pmc.ncbi.nlm.nih.gov/articles/PMC5951831)
- [Familial UM in 25 families with monoallelic MBD4 variants, PMID:38060262](https://pubmed.ncbi.nlm.nih.gov/38060262/)
- [NCI PDQ, MBD4-Associated Neoplasia Syndrome](https://cancer.gov/publications/pdq/information-summaries/genetics/mbd4-hp-pdq)
- [Haematologica review](https://haematologica.org/article/view/12253/78790)
- [Institut Curie: germline MBD4 mutations and predisposition to UM](https://institut-curie.org/publications/germline-mbd4-mutations-and-predisposition-uveal-melanoma)
- [MBD4 deficiency predictive of ICI response in metastatic UM (Saint-Ghislain; listing page)](https://wordpressdev.france-genomique.org/publication/mbd4-deficiency-is-predictive-of-response-to-immune-checkpoint-inhibitors-in-metastatic-uveal-melanoma-patients/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC9118112`: "autosomal recessive, multi-organ tumor predisposition syndrome… five individuals with bi-allelic MBD4 variants within four families, with histories of adenomatous colorectal polyposis, acute myeloid leukemia, and uveal melanoma"
  - closest text in source: "We identified five individuals with bi-allelic MBD4 variants within four families and these individuals had a personal and/or family history of adenomatous colorectal polyposis, acute myeloid leukemia, and uveal melanoma"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002863` (1 mention) - the report calls it "MDS"; HP calls it **Myelodysplasia**