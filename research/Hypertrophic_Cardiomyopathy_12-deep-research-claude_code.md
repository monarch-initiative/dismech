---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-13T14:03:28.735491'
end_time: '2026-10-13T14:06:37.251955'
duration_seconds: 188.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 12
  mondo_id: MONDO:0012804
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
  web_search_requests: 6
  num_turns: 19
  total_cost_usd: 2.0489324
  session_id: 66022e7b-6e43-4b94-b545-8f38b59a73ec
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 18
  on_topic: 15
  validator_version: 0.3.0
term_validation:
  total_terms: 40
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0005045
    reported_labels:
    - ClinGen Definitive is recorded against general HCM
    ontology_label: hypertrophic cardiomyopathy
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 12
- **MONDO ID:** MONDO:0012804 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 12** covering all of the
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

# Research report: Hypertrophic Cardiomyopathy 12 (CMH12, CSRP3-related HCM)

**Target:** MONDO:0012804 · Mendelian · prepared 2026-10-13

**How to read the evidence.** Quotes marked **[cached]** are exact text from abstracts already in this worktree's `references_cache/`, so they can be used as snippets as they stand. References marked **[not cached]** were found by web search. They need `just fetch-reference` before anything from them is used as evidence, and I have not quoted them verbatim. Ontology CURIEs marked ✔ were checked against the committed `cache/*/terms.csv`. CURIEs without ✔ are leads and must be looked up before they are bound.

---

## 1. Disease information

**Overview.** CMH12 is familial hypertrophic cardiomyopathy caused by variants in **CSRP3** (11p15.1). CSRP3 encodes **muscle LIM protein (MLP)**, a small protein with two LIM domains. MLP sits at the Z-disc and costamere and also moves into the nucleus. Unlike most HCM genes, CSRP3 is **non-sarcomeric**. Its role is mechanosensing and signalling, not generating force.

> "MLP, in contrast to the proteins encoded by the other recognised HCM disease genes, is non-sarcomeric, and has important signalling functions in cardiomyocytes." — PMID:30048712 [cached]

**Identifiers**
| System | ID |
|---|---|
| MONDO | MONDO:0012804 *hypertrophic cardiomyopathy 12* (already in the draft entry) |
| OMIM (phenotype) | 612124 (CMH12; listed as AD) |
| OMIM (gene) | *600824 CSRP3 |
| HGNC | hgnc:2472 CSRP3 (taken from the ClinGen rows below; not yet checked in `cache/hgnc`) |
| MedGen | 393755 |
| LOVD disease | 03091 |
| Orphanet | No CMH12-specific entry was found. The umbrella entry is "Familial isolated hypertrophic cardiomyopathy" (ORPHA:217569, **not verified**; check with `just fetch-reference ORPHA:…`) |
| ICD-10 / ICD-11 | Only the general HCM codes apply (I42.1 obstructive / I42.2 other HCM; ICD-11 BC43.1). Neither has been checked against the ICD10CM cache |

**Synonyms:** CMH12; cardiomyopathy, familial hypertrophic, 12; CSRP3-related hypertrophic cardiomyopathy; MLP-related HCM. Allelic disorder: dilated cardiomyopathy 1M (CMD1M, MONDO:0011840).

**Data provenance:** All of the data are disease-level aggregates (family cosegregation studies, case–control cohorts, and the ClinGen and OMIM curations). No EHR-derived data were found.

---

## 2. Etiology

**Primary cause:** Germline CSRP3 variants. Three kinds are reported:
- **Heterozygous missense variants in the LIM1 domain.** Examples are C58G, L44P, S54R/E55G, K42Q and C150Y.
- **Homozygous or biallelic variants**, including truncating variants that effectively knock the gene out. Examples are p.Arg122Ter and other truncations.
- **The W4R variant (p.Trp4Arg).** It is common (about 1% in Europeans) and now looks like a **modifier** rather than a cause of disease on its own.

> "We found 3 different missense mutations in 3 unrelated patients with familial HCM but detected no mutation in the DCM group or the controls. All mutations predicted an amino acid exchange at highly conserved residues in the functionally important LIM1 domain" — PMID:12642359 [cached]

**Gene-disease validity: the classification moved between curations, and the mode of inheritance is disputed**
- ClinGen 2019 (Ingles et al., *Circ Genom Precis Med*) put CSRP3 in the **Moderate** group, together with TNNC1 and JPH2 [not cached; ClinGen HCM gene curation].
- The current ClinGen record is **Definitive**, with MOI recorded as **SD (semidominant)**, from the Hereditary Cardiovascular Disease GCEP, dated 2023-08-09:
  > "CSRP3 | HGNC:2472 | hypertrophic cardiomyopathy | MONDO:0005045 | SD | Definitive" — `CGGV:assertion_012b9b15-798a-46e2-8164-61a829ceeda1-2023-08-09T160000.000Z` [cached]
  - **Curation caveat:** this ClinGen assertion is for the *general* HCM term MONDO:0005045, not MONDO:0012804. Under the CLAUDE.md rule ("The assertion must be for this entry's disease"), it is copied onto CMH12's `gene_disease_validity` only if CMH12 maps to that term with `exactMatch`. Otherwise it is an `other_disease` lead.
- For the allelic DCM phenotype: "CSRP3 | HGNC:2472 | dilated cardiomyopathy 1M | MONDO:0011840 | AD | Limited" — `CGGV:assertion_beaafc90-…-2026-03-04` [cached].
- Recessive inheritance was argued early on:
  > "we suggest that the association of CSRP3 as a validated HCM-causing gene require additional studies and those CSRP3 variants could result in HCM with an autosomal recessive inheritance rather than with an autosomal dominant transmission as usually reported on HCM (OMIM 612124)." — PMID:30012424 [cached]
- Population-scale association (2026):
  > "Several definitive genes which are much less commonly affected in HCM (CSRP3, MYL3, ACTC1, TPM1, FHOD3, MYL2, and TNNC1) did not pass our Bonferroni corrected-significance threshold, but all had positively associated effect sizes with HCM." — PMID:41893039 [cached]

**Risk factors**
- *Genetic:* Biallelic state, which consanguinity makes more likely (see section 9). Co-inheritance of a sarcomeric variant, which W4R makes worse (see Modifiers).
- *Age:* Penetrance depends strongly on age (C150Y; PMID:33035702).
- *Environmental:* No CSRP3-specific environmental risk factor has been reported. General HCM modifiers such as hypertension and obesity are plausible but **unstudied for CMH12**.

**Protective factors:** None reported. Mechanistically, lowering sarcomeric crossbridge load protects iPSC tissue (PMID:35384713, see section 6), but this is a treatment effect and not a protective factor in a population.

**Gene–environment interactions:** No human data. MLP's subcellular location responds to load and contractility (PMID:19376126). This suggests mechanical load is a plausible G×E axis, but that is an **inference**.

---

## 3. Phenotypes

All of the HP CURIEs below are ✔ in `cache/hp/terms.csv`.

| Phenotype | HP term | Frequency / characteristics | Evidence |
|---|---|---|---|
| Asymmetric septal hypertrophy | HP:0001670 ✔ | Typical pattern; all 3 original index cases | "All 3 index patients were characterized by typical asymmetrical septal hypertrophy." PMID:12642359 [cached] |
| Hypertrophic cardiomyopathy / LV hypertrophy | HP:0001639 ✔ / HP:0001712 ✔ | Defining. Mean maximal LV wall 18 ± 3 mm in C150Y carriers | PMID:33035702 [cached]; PMID:34558151 "an obvious left ventricular hypertrophy was found in the proband" [cached] |
| Late (adult) onset | onset descriptor | Mean age at diagnosis 55 ± 13 y (C150Y); "highly age-dependent penetrance" | PMID:33035702 [cached] |
| Sigmoid septal contour | none checked; candidate *Sigmoid septum* (look up) | 85% of Z-disc-variant HCM in one cohort (mixed genes) | Theis 2006, PMID:17097056 [not cached] |
| LV diastolic dysfunction | HP:0025168 ✔ | General HCM feature; seen in the KI mouse | PMID:30048712 (mouse) [cached] |
| LV systolic dysfunction / progression to dilation | HP:0025169 ✔ / HP:0001644 ✔ | Reported for biallelic or severe cases and the allelic CMD1M. Uncommon in heterozygous CMH12 | PMID:30048712 (mouse); ClinGen DCM Limited |
| LVOT obstruction | HP:0032092 ✔ | No CSRP3-specific frequency found | general HCM |
| Exertional dyspnea, chest pain, palpitations, syncope | HP:0002875 ✔, HP:0100749 ✔, HP:0001962 ✔, HP:0001279 ✔ | Usual HCM symptom set; no CMH12-specific frequencies | general HCM |
| Atrial fibrillation, ventricular tachycardia | HP:0005110 ✔, HP:0004756 ✔ | Not quantified for CMH12 | — |
| Sudden cardiac death | HP:0001645 ✔ | **Low risk in heterozygous C150Y.** "After a mean follow-up of 11 (±8) years, no adverse events were reported in any of the HCM patients." | PMID:33035702 [cached] |
| Myocardial fibrosis | HP:0001685 ✔ | Profibrotic signalling in the KI mouse; human LGE data not found | PMID:30048712 [cached] |
| Myocyte disarray (histology) | candidate HP term (look up) | Proposed mechanism | PMID:15205937 [cached] |

**Severity:** Varies with dose. The phenotype is mild, late-onset and low-risk in heterozygotes, and more severe in homozygotes:
> "Ten of the index cases were heterozygous and one was homozygous. Homozygous had a more severe phenotype." — PMID:33035702 [cached]

**Quality of life:** No CMH12-specific QoL data were found. General HCM data (e.g. KCCQ in the mavacamten trials) apply only by inference.

---

## 4. Genetic / molecular information

- **Gene:** CSRP3 (hgnc:2472; OMIM *600824; NCBI Gene 8048), 11p15.1, 194-aa protein with two LIM domains (LIM1 and LIM2), a nuclear localization signal, and a glycine-rich region.
- **Reference sequences:** NM_003476.5 / NP_003467.1 (used in PMID:34558151).

**Key variants**
| Variant | Type | Zygosity | Status / notes | Source |
|---|---|---|---|---|
| p.Cys58Gly (C58G) | missense, LIM1 zinc finger | het (familial) | The only variant rated likely pathogenic in the 2018 ACMG meta-analysis. Abolishes zinc coordination | PMID:12642359, 15205937, 30012424, 30048712 [cached] |
| p.Leu44Pro, p.Ser54Arg/Glu55Gly | missense, LIM1 | het | Cause protein depletion in cells | PMID:30048712 [cached] |
| p.Cys150Tyr | missense, LIM2 | het (10) / hom (1) | 11/6456 HCM probands vs 0 in other cardiomyopathy and control groups (p<0.0001). Late-onset, low risk | PMID:33035702 [cached] |
| p.Arg122Ter (c.364C>T) | nonsense | **hom** (Polish), **het** (Chinese family, cosegregating) | Homozygous null; the heterozygous Chinese family conflicts with recessive-only models | PMID:31919335, 34558151 [cached] |
| Homozygous truncating (2 probands) | nonsense/frameshift | hom | First homozygous CSRP3 knockouts in HCM | PMID:30012424 [cached] |
| p.Trp4Arg (W4R; rs45550635, look up) | missense, N-terminal | het, ~1% of Europeans | **Modifier, not causal on its own** | PMID:35384713 [cached]; Geier 2008 PMID:18505755 [not cached] |

> "We demonstrate that the common muscle LIM protein-W4R variant is an important modifier, exacerbating the phenotypic expression of HCM, but alone may not be a disease-causing mutation." — PMID:35384713 [cached]

**Functional consequence:** The pathogenic missense variants cause **loss of function through protein destabilization and proteasomal depletion**, which amounts to haploinsufficiency or hypomorphism. They do not act as gain of function (`functional_impact_category`: LOSS_OF_FUNCTION or PARTIAL_LOSS_OF_FUNCTION):
> "Intriguingly, the abundance of MLP decreased in KI/KI mice by 80% and in KI/+ mice by 50%. Protein depletion was also observed in cellular studies for two further HCM-causing CSRP3 mutations (L44P and S54R/E55G). We show that MLP depletion is caused by proteasome action." — PMID:30048712 [cached]

**Yield and frequency:** About 3% of HCM probands carry a CSRP3 variant (12/389 in the Mayo cohort; Bos 2006, PMID:16352453 [not cached]). This share should be read as an upper bound, because pathogenicity is unresolved for many of those variants. Geier 2008 reported a large linkage family plus 4 more families with segregating missense variants (PMID:18505755 [not cached]).

**Modifiers:** W4R (above). Sarcomeric co-variants such as MYH7 interact with MLP depletion (PMID:35384713).

**Epigenetic changes / chromosomal abnormalities:** None reported. CNVs involving 11p15.1 are not known as a CMH12 mechanism.

**Somatic origin:** Not applicable (germline).

---

## 5. Environmental information

There are no known environmental, lifestyle or infectious causes. Mechanical load and contractility regulate where MLP sits in the cell (PMID:19376126), which makes exercise and pressure load plausible modulators. This is **an inference, not an observation in patients**. Following CLAUDE.md, an `environmental` entry should either be left out or carry a "Left deliberately uncited." waiver.

---

## 6. Mechanism / pathophysiology

### Ordered causal chain
1. **Germline CSRP3 variant** (LIM1/LIM2 missense, or biallelic truncation) **leads to** misfolding of a zinc-finger LIM domain:
   > "this single point mutation prevents zinc coordination and proper folding of the second zinc-finger in the first LIM domain, which consequently renders the protein less stable and more susceptible to proteolysis." — PMID:15205937 [cached; IN_VITRO]
2. **Unstable MLP is degraded by the proteasome**, which **results in** MLP depletion (about 50% in heterozygous and about 80% in homozygous knock-in mice; PMID:30048712 [cached; MODEL_ORGANISM]). Truncating biallelic alleles reach the same end state, a null, directly.
   - *Branch 2b (proteotoxic):* Mutant MLP C58G binds BAG3, which **triggers** a proteotoxic, heat-shock-protein stress response (PMID:30048712).
3. **Loss of MLP binding partners at the Z-disc:** binding to α-actinin, N-RAP and telethonin (T-cap) drops:
   > "Protein-binding studies indicate that mutations in the CRP3 gene lead to a decreased binding activity of MLP to alpha-actinin." — PMID:12642359 [cached]
   W4R specifically disrupts the interaction with telethonin and its localization (Knöll 2002, *Cell* 111:943, PMID:12507422 [not cached]).
4. **The Z-disc stretch-sensing complex fails**, which **leads to** a mechanosensing defect, disinhibition of **calcineurin–NFAT signalling**, and hypertrophic gene expression. This step was shown in human iPSC engineered heart tissue, where MLP depletion was secondary to MYH7 load. Applying it to primary CSRP3 depletion is a **mechanistic inference**:
   > "Subsequent reduction in the sarcomeric muscle LIM protein level caused disinhibition of calcineurin-nuclear factor of activated T-cells signaling, which promoted cardiac hypertrophy." — PMID:35384713 [cached; IN_VITRO]
5. **Disrupted nucleocytoplasmic shuttling of MLP** impairs myofilament remodelling and stress gene expression (sarcomere disarray, BNP). This was demonstrated in rat neonatal myocytes:
   > "cyclic strain of myocytes after prior NLS treatment to remove nuclear MLP resulted in disarrayed sarcomeres" — PMID:19376126 [cached; IN_VITRO]
6. **Cardiomyocyte hypertrophy and myocyte disarray**, plus compensatory N-RAP upregulation (proposed in PMID:15205937), **lead to** asymmetric septal LV hypertrophy.
7. **Fetal gene programme, profibrotic signalling and interstitial fibrosis** **result in** diastolic dysfunction, and with biallelic or severe loss, systolic dysfunction with progression towards DCM:
   > "Transcriptome analysis by RNA-seq identified activation of pro-fibrotic signalling, induction of the fetal gene programme and activation of markers of hypertrophic signalling in these hearts." — PMID:30048712 [cached]
8. **Clinical expression** (dyspnea, arrhythmia, rarely SCD) depends on gene dose and age. Heterozygous carriers have a late-onset, low-risk course (PMID:33035702).

**Upstream vs downstream:** Steps 1–3 are molecular (MOLECULAR scale). Steps 4–5 are cellular signalling (CELLULAR). Steps 6–7 are tissue and organ (TISSUE). Step 8 is organism-level (ORGANISM).

**Suggested terms** (✔ = in cache)
- GO BP: response to muscle stretch GO:0035994 ✔; calcineurin-NFAT signaling cascade GO:0033173 ✔ (modifier INCREASED); cardiac muscle hypertrophy GO:0003300 ✔; sarcomere organization GO:0045214 ✔; cardiac myofibril assembly GO:0055003 ✔; proteasome-mediated ubiquitin-dependent protein catabolic process GO:0043161 ✔ (MLP depletion)
- GO CC: Z disc GO:0030018 ✔; costamere GO:0043173 ✔; nucleus GO:0005634 ✔
- CL: cardiac muscle cell CL:0000746 ✔; fibroblast of cardiac tissue CL:0002548 ✔ (fibrosis node)
- Module conformance candidates: run `just list-modules cardiomyopathy` and `just list-modules fibro`. `cardiomyopathy_maladaptive_remodeling` and `fibrotic_response` are named in CLAUDE.md; check them before conforming.

**Molecular profiling:** The only omics dataset found is the bulk RNA-seq of C58G knock-in mouse hearts (PMID:30048712; locate the GEO accession using `just discover-datasets`). No human single-cell, proteomic or metabolomic data specific to CSRP3 were found.

---

## 7. Anatomical structures

- **Organ:** heart UBERON:0000948 ✔; cardiovascular system.
- **Site:** interventricular septum UBERON:0002094 ✔ (asymmetric). The left ventricle term was not found in the cache; look it up.
- **Tissue:** cardiac muscle tissue UBERON:0001133 ✔.
- **Cells:** cardiomyocytes (CL:0000746 ✔); cardiac fibroblasts (secondary).
- **Subcellular:** Z-disc, costamere, nucleus and nucleolus (PMID:19376126: "The NLS of MLP also localizes to the nucleolus.").
- **Secondary organs:** None. MLP is also expressed in skeletal muscle, but no skeletal myopathy is documented in CMH12.

---

## 8. Temporal development

- **Onset:** Usually adulthood (mean 55 ± 13 y for C150Y). Biallelic cases can present in adolescence or young adulthood (PMID:30012424 MeSH lists adolescent and adult; check the full text for exact ages).
- **Pattern:** Insidious. Hypertrophy develops progressively with **age-dependent penetrance**.
- **Course:** Chronic and lifelong. Heterozygotes appear to have a stable, low-event course (no events over a mean 11 y follow-up). Homozygous and knockout states are more severe and can progress to systolic dysfunction.
- **Remission:** None.
- **Critical period:** Not defined. Serial screening of carriers into later life is warranted because of late penetrance (an inference from PMID:33035702).

---

## 9. Inheritance and population

- **Inheritance:** OMIM lists **AD** and ClinGen lists **semidominant**. The literature supports gene-dose effects: heterozygous variants have low penetrance, and homozygous variants give a more severe phenotype.
  - Suggested `inheritance` blocks: Autosomal dominant (HP:0000006) and Autosomal recessive (HP:0000007). Neither is in the cache list I checked, so look both up. Name semidominance in `description`. Look up whether HPO has a "Semidominant inheritance" term (possibly HP:0032113, **unverified**).
- **Penetrance:** Incomplete and age-dependent (PMID:33035702).
- **Expressivity:** Variable; modified by W4R and sarcomeric co-variants.
- **Consanguinity:** Biallelic variants are enriched:
  > "variants in the minor HCM genes MYL2, MYL3, and CSRP3 more likely to present in homozygosity than the major genes, suggesting these variants are less penetrant in heterozygosity." — PMID:37431535 [cached; Egyptian cohort n=514]
- **Founder effects:** Not established. C150Y was found in a Spanish/European multicentre cohort, and R122Ter recurs in Polish and Chinese families.
- **Prevalence:** HCM overall affects about 1/500 ("estimated prevalence of 1/500", PMID:30012424 [cached]). CSRP3 accounts for a small minority of genotyped HCM: 11/6456 probands (about 0.17%) for C150Y alone, and about 3% of the Mayo cohort carried any CSRP3 variant. **No CMH12-specific prevalence exists.** Record it as `measure_type: UNKNOWN` / `prevalence_class: RARE` rather than deriving a number.
- **Sex ratio and geography:** Not reported for CMH12 specifically.
- **Germline mosaicism / anticipation:** Not reported.

---

## 10. Diagnostics

- **Imaging:** Echocardiography and cardiac MRI showing LV wall ≥15 mm (≥13 mm in relatives) without another explanation, which is the general ESC/AHA HCM criterion. MRI LGE can assess fibrosis.
- **ECG:** LVH and repolarization changes; Holter monitoring for AF and NSVT.
- **Biomarkers:** NT-proBNP and BNP (non-specific). BNP expression depends on MLP in the myocyte models (PMID:19376126).
- **Histopathology:** Myocyte hypertrophy, disarray and fibrosis (the proband biopsy in PMID:34558151).
- **Genetic testing:** A multigene HCM panel or exome. CSRP3 is on the ClinGen-curated HCM panel and is typically included (PMID:30012424: "CSRP3 is usually included on HCM gene panels used for molecular diagnosis by next-generation sequencing"). Points for interpreting results:
  - Rule out W4R as the sole explanation.
  - Look for a second allele or a sarcomeric co-variant.
  - Use ancestry-matched controls (PMID:37431535).
  - CMA, karyotype, FISH, mtDNA and repeat expansion testing are not indicated.
- **Differential diagnosis:** Sarcomeric HCM (MYBPC3 and MYH7, which account for most genotype-positive cases). Phenocopies: Fabry disease, PRKAG2, Danon disease (LAMP2), TTR amyloidosis, RASopathies, mitochondrial disease. Also athlete's heart and hypertensive LVH. TRIM63 is another recessive non-sarcomeric HCM gene.
- **Screening:** Cascade genetic testing and serial imaging of first-degree relatives. This matters particularly because of late penetrance.

---

## 11. Outcome / prognosis

- Heterozygous C150Y: favourable. "The p.(Cys150Tyr) variant in CSRP3 causes late-onset and low risk form of hype[rtrophic cardiomyopathy]" (PMID:33035702; the cached abstract is cut off there, so quote only up to the truncation).
- Homozygous / null: more severe, with risk of systolic dysfunction (human case reports plus the KI/KI mouse). There are too few cases to estimate survival.
- **No CMH12-specific survival, mortality or QoL statistics exist.** Prognostic factors follow general HCM SCD risk models (ESC HCM Risk-SCD), which have not been validated for CSRP3.

---

## 12. Treatment

No CSRP3-specific therapy exists. Management follows the general HCM guidelines (2024 AHA/ACC; 2023 ESC).

| Treatment | NCIT action term | Agent (look up CHEBI/NCIT) | Notes |
|---|---|---|---|
| Beta-blockers, non-dihydropyridine CCBs (verapamil, diltiazem), disopyramide | Pharmacotherapy NCIT:C15986 ✔ | e.g. metoprolol, verapamil | First line for symptoms. Note that verapamil reduces nuclear MLP in vitro (PMID:19376126), which is a mechanistic curiosity with no clinical correlate |
| Cardiac myosin inhibitors (mavacamten, aficamten) | NCIT:C15986 ✔ | mavacamten | Approved for obstructive HCM. Lowering crossbridge load rescued Z-disc/MLP stress in iPSC tissue: "By mitigating enhanced actomyosin crossbridge formation through either genetic or pharmacological means, we alleviated stress at the Z-disc, preventing the development of hypertrophy associated with sarcomeric mutations." (PMID:35384713 [cached]). Efficacy in **primary CSRP3** HCM has not been tested |
| Septal myectomy / alcohol septal ablation | Surgical Procedure NCIT:C15329 ✔ | — | For drug-refractory LVOT obstruction |
| ICD implantation | NCIT:C15329 ✔ + device qualifier pattern | — | Per SCD risk; probably rarely needed for heterozygous C150Y |
| Heart-failure therapy / transplant | NCIT:C15986 / transplantation | — | For the dilated/end-stage evolution |
| Genetic counseling | NCIT:C15240 ✔ | — | Cascade testing; recessive and dose-dependent risk in consanguineous families |

- **Gene therapy, ASO, siRNA:** None for CSRP3. A loss-of-function mechanism points towards replacement or stabilization strategies, but this is speculative. PMID:35384713 frames "mechanism-based treatments for HCM that stabilize the Z-disc MLP-mechanosensory complex."
- **Trials:** No CSRP3-specific trials were found on ClinicalTrials.gov. General HCM trials (EXPLORER-HCM NCT03470545, SEQUOIA-HCM) included unselected genotypes. Verify the NCT IDs with `just fetch-reference` before citing them.
- **Pharmacogenomics:** None specific.

---

## 13. Prevention

- **Primary:** Not possible. Preimplantation or prenatal testing is an option in families with known biallelic alleles.
- **Secondary:** Cascade genotyping. Long-term echo surveillance of heterozygous carriers, given late-onset penetrance.
- **Tertiary:** SCD risk stratification, AF anticoagulation, and activity counselling per the HCM guidelines.
- **Immunization / public health:** Not applicable.

---

## 14. Other species / natural disease

- No naturally occurring CSRP3-related disease is recorded in OMIA (I did not search directly; verify). Feline HCM is mainly MYBPC3/ALMS1, not CSRP3.
- Orthologs: mouse *Csrp3* (MGI). Look up the NCBI Gene ID; zebrafish *csrp3*.
- MLP's Z-disc mechanosensing role is conserved across vertebrates.

---

## 15. Model organisms

| Model | Phenotype recapitulation | Limitations | Source |
|---|---|---|---|
| **Csrp3 C58G knock-in mouse** (KI/KI, KI/+) | KI/KI: "robust cardiomyopathy phenotype with diastolic and systolic left ventricular dysfunction", increased heart weight, fetal genes, fibrosis. Protein depletion in KI/+ | Severe phenotype mainly when homozygous. The mixed systolic/diastolic phenotype overlaps DCM. Mouse MHC isoform differences | PMID:30048712 [cached; `RECAPITULATES`/`PARTIALLY_RECAPITULATES` LV dysfunction; `MEASURES` MLP depletion] |
| **MLP-null (Csrp3−/−) mouse** | DCM with hypertrophy and heart failure; disrupted cytoarchitecture; soft hearts at birth | Models **DCM**, not HCM, so a `FAILS_TO_RECAPITULATE`/`PARTIALLY_RECAPITULATES` candidate for the septal-HCM node | Arber et al., *Cell* 1997;88:393 (doi:10.1016/s0092-8674(00)81878-4; PMID not confirmed) [not cached] |
| **MLP-null mouse, stretch-sensing analysis**; W4R telethonin binding | Stretch-response defect | Knockout ≠ missense allele | Knöll 2002, PMID:12507422 [not cached] |
| **Neonatal rat cardiomyocytes** (NLS peptide blockade) | Shows that MLP shuttling is needed for hypertrophic remodelling | Rat, neonatal, pharmacological | PMID:19376126 [cached; IN_VITRO] |
| **Patient iPSC-CM engineered heart tissue** (MYH7 + MLP-W4R) | MLP destabilization, calcineurin–NFAT, hypertrophy; rescued by gene editing or myosin inhibition | The primary lesion is sarcomeric; CSRP3 acts as modifier. Shows **secondary** MLP depletion, not primary CMH12 | PMID:35384713 [cached; IN_VITRO] |
| **Cell binding assays** (C58G with α-actinin and N-RAP) | Reduced binding, zinc-finger misfolding | Reductionist | PMID:15205937 [cached; IN_VITRO] |

Resources: MGI (Csrp3 alleles), IMPC, ZFIN.

---

## Key uncertainties for curators

1. **Mode of inheritance.** OMIM says AD, ClinGen says SD, and Janin 2018 and Lipari 2020 argue for AR. A heterozygous truncation cosegregates in a Chinese family (PMID:34558151), which conflicts with a purely recessive model. Encode multiple inheritance blocks, each with its own evidence.
2. **ClinGen Definitive is recorded against general HCM (MONDO:0005045).** Check mapping scope before copying it onto CMH12.
3. **W4R should not be modelled as causal.** Put it in `genetic` as `relationship_type: MODIFIER`.
4. **Several canonical papers are not cached:** Arber 1997, Knöll 2002, Bos 2006, Geier 2008, Ingles 2019 and Theis 2006. Fetch them before citing; the Arber PMID in particular was not confirmed.
5. **No GeneReviews chapter specific to CMH12** is expected. Confirm with `just check-genereviews`; the general "Hypertrophic Cardiomyopathy Overview" chapter probably applies.

---

### Sources
- Cached in this worktree: PMID:12642359, 15205937, 15781201 (letter; no abstract text), 19376126, 30012424, 30048712, 31919335, 33035702, 34558151, 35384713, 37431535, 41893039; ClinGen CGGV assertions 012b9b15 (HCM, Definitive) and beaafc90 (DCM 1M, Limited).
- Web: [Arber 1997 (JCI reference list)](https://www.jci.org/references/scholar/26611/B1) · [edoc.unibas.ch](https://edoc.unibas.ch/3220) · [Knöll 2002 abstract (Arizona)](https://experts.arizona.edu/en/publications/the-cardiac-mechanical-stretch-sensor-machinery-involves-a-z-disc/) · [Mount Sinai abstract page](https://scholars.mssm.edu/en/publications/the-cardiac-mechanical-stretch-sensor-machinery-involves-a-z-disc/) · [WikiGenes 12507422](https://www.wikigenes.org/e/ref/e/12507422.html) · [LOVD CMH12](https://databases.lovd.nl/shared/diseases/03091) · [MedGen 393755](https://ncbi.nlm.nih.gov/medgen/393755) · [OMIM 600824 mirror](https://https.ncbi.nlm.nih.gov/omim/600824) · [GenCC CSRP3](https://search.thegencc.org/genes/HGNC:2472/submitters) · [PanelApp CSRP3](https://nhsgms-panelapp.genomicsengland.co.uk/entities/CSRP3) · [Ingles 2019 (PMC6410971)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6410971) · [medRxiv ClinGen re-curation](https://medrxiv.org/node/844787) · [Geier 2008 (ORA Oxford)](https://ora.ox.ac.uk/objects/uuid:329fc1f5-bd84-44ef-9587-0e9f305a3368) · [MDC edoc](https://edoc.mdc-berlin.de/id/eprint/9738/) · [Bos 2006 (PMC2756511)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2756511) · [Theis 2006 (dkNET)](https://dknet.org/literature/pmid:17097056?rpKey=on) · [OMIM 607487 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/607487)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005045` (3 mentions) - the report calls it "ClinGen Definitive is recorded against general HCM"; MONDO calls it **hypertrophic cardiomyopathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000006` (1 mention) - the report calls it "Suggested `inheritance` blocks: Autosomal dominant"; HP calls it **Autosomal dominant inheritance**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.