---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T20:31:19.087741'
end_time: '2026-10-14T20:32:27.798745'
duration_seconds: 68.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 39
  mondo_id: MONDO:0032845
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
  web_search_requests: 4
  num_turns: 6
  total_cost_usd: 0.7268404
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 14
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0032845
    reported_labels:
    - MONDO
    ontology_label: spermatogenic failure 39
  - term_id: HP:0012206
    reported_labels:
    - Asthenozoospermia
    ontology_label: Abnormal sperm motility
  - term_id: HP:0012864
    reported_labels:
    - check
    ontology_label: Abnormal sperm morphology
  - term_id: HP:0012862
    reported_labels:
    - check
    ontology_label: Abnormal germ cell morphology
  - term_id: NCIT:C15240
    reported_labels:
    - listed in CLAUDE.md
    ontology_label: Genetic Counseling
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 39
- **MONDO ID:** MONDO:0032845 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 39** covering all of the
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

# Research Report: Spermatogenic Failure 39 (SPGF39)

**Method note.** I ran four web searches and opened no primary source in full. Most of the content below comes from search-result summaries and database mirrors. Journal citations come from result titles and reference lists. I have not verified any PMID against PubMed, so I list none as confirmed. Run `just fetch-reference` on each PMID or DOI before any of this goes into evidence snippets, and don't write snippets from this report. Anything not in the search results is marked "not retrieved". Gene-level mechanism beyond what the sources say is inference, and I label it as such.

---

## 1. Disease Information

**Overview.** SPGF39 is an autosomal recessive form of male infertility caused by biallelic variants in *DNAH17*. A disease-ontology description gives the phenotype as a spermatogenic failure "characterized by multiple morphologic anomalies of the sperm flagellum, lack of the outer dynein arms in the flagella, and asthenozoospermia" ([drugmap disease page](https://drugmap.idrblab.net/data/disease/details/DISWTPU4)). It is isolated: the sources describe infertility without a syndromic or ciliary phenotype.

**Identifiers**
| Resource | ID |
|---|---|
| MONDO | MONDO:0032845 |
| OMIM | #618643 (SPGF39) |
| Gene | *DNAH17* (OMIM 610063), 17q25.3 |
| MedGen | C5231438 |
| LOVD disease entry | #06384 ([LOVD](https://databases.lovd.nl/shared/diseases/06384)) |
| Orphanet, ICD-10/11, MeSH | not retrieved |

**Synonyms.** Spermatogenic failure 39; SPGF39; *DNAH17*-related MMAF or asthenozoospermia. This is the MMAF (multiple morphological abnormalities of the sperm flagella) / asthenoteratozoospermia spectrum.

**Source type.** The disease-level resources (OMIM, MONDO) aggregate the case literature. The primary papers are small patient series with sperm and genetic analysis.

## 2. Etiology

- **Causal factor:** homozygous or compound heterozygous *DNAH17* variants. OMIM lists autosomal recessive inheritance with a phenotype-mapping key of 3, meaning the molecular basis is known ([MedGen/OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C5231438/index.html?cmd=HTOn)).
- **Gene-disease validity:** one gene-target database lists the association as "Definitive" ([drugmap](https://drugmap.idrblab.net/data/disease/details/DISWTPU4)). Per the dismech rule, I did not use this as a ClinGen tier. It is not a CGGV record. Check the cached ClinGen data with `just check-gene-validity` before recording any tier.
- **Risk, protective and gene-environment factors:** none found. No environmental, lifestyle, modifier-gene or protective-variant data turned up for this monogenic disorder. These are gaps, not negatives.

## 3. Phenotypes

All items are male-limited. Frequencies were not retrieved. Suggested HPO terms are leads that need lookup and validation.

| Phenotype | Suggested HPO lead | Notes |
|---|---|---|
| Male infertility | HP:0003251 | Presenting feature |
| Asthenozoospermia | HP:0012206 | Core feature; sperm motility is severely reduced |
| Abnormal sperm flagellum morphology (MMAF: short, absent, coiled, irregular tails) | HP:0012864 (check) | Per MedGen summary |
| Abnormal sperm head and midpiece morphology | HP:0012862 (check) | Reported in some men |
| Teratozoospermia / asthenoteratozoospermia | HP:0012864 (check) | Used in the 2025 AJA title |
| Oligozoospermia | HP:0000798 | Listed in a mouse-phenotype mirror; unconfirmed in humans |
| Absent outer dynein arms on EM | no HPO term likely | Ultrastructural finding |

- **Onset and course:** onset is at reproductive age, when infertility is noticed. The condition is lifelong and non-progressive in the reports seen, which is inferred.
- **Quality of life:** not retrieved.

## 4. Genetic / Molecular Information

- **Gene:** *DNAH17*, axonemal dynein heavy chain 17, a sperm-specific outer dynein arm heavy chain. HGNC id: look up in cache. dismech uses lowercase `hgnc:` CURIEs.
- **Variant types:** the literature includes loss-of-function variants (nonsense, frameshift, splice) and missense variants.
  - **Whitfield et al. 2019** (Am J Hum Genet 105(1):198–212) is the foundational paper, "Mutations in DNAH17, encoding a sperm-specific axonemal outer dynein arm heavy chain, cause isolated male infertility due to asthenozoospermia".
  - **Zhang et al. 2020** (J Exp Med 217(2):e20182365) reports a *DNAH17* missense variant causing flagella destabilization and asthenozoospermia ([JEM](https://rupress.org/jem/article/217/2/e20182365/132579/A-DNAH17-missense-variant-causes-flagella)).
  - **Sha et al. 2020** (Ann Hum Genet 84:271–9) reports biallelic variants in a patient with severe asthenozoospermia and MMAF, with *DNAH17* protein nearly undetectable in sperm ([Wiley](https://onlinelibrary.wiley.com/doi/10.1111/ahg.12369)).
  - **Zhang et al. 2021** (Clin Genet 99:176–86) reports novel loss-of-function variants causing MMAF in humans and mice ([Mount Sinai record](https://scholars.mssm.edu/en/publications/novel-loss-of-function-variants-in-dnah17-cause-multiple-morpholo/)).
  - **Newer reports** include a 2023 J Assist Reprod Genet paper ([Springer](https://link.springer.com/article/10.1007/s10815-023-02897-7)), a 2025 Reprod Sci paper on splice-site variants truncating the AAA6 domain ([Springer](https://link.springer.com/article/10.1007/s43032-025-02002-6)) and a recent Asian J Androl paper ([PubMed 41549443](https://pubmed.ncbi.nlm.nih.gov/41549443/)).
- **Cohort size:** the 2023 paper says that, with its five new cases, the literature held 21 patients with *DNAH17* mutations.
- **Allele frequency, ACMG classifications, ClinVar counts, founder variants, modifier genes, epigenetics, chromosomal abnormalities:** not retrieved.
- **Functional consequence:** loss of function, with loss of the outer dynein arms and of *DNAH17* protein in sperm (Sha 2020).

## 5. Environmental Information

None found. There are no known toxin, lifestyle or infectious contributors for this monogenic form. Leave `environmental:` empty.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps 1–3 and 5 follow the sources; step 4 is inferred from the DNAH17 and dynein-arm biology rather than shown directly):

1. Biallelic *DNAH17* variants (loss of function, or destabilizing missense) are inherited from both parents.
2. These lead to loss or severe reduction of *DNAH17* protein in sperm (Sha 2020).
3. This results in absent outer dynein arms in the sperm axoneme, seen by electron microscopy ([MedGen mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C5231438/index.html?cmd=HTOn)).
4. *(Inferred)* Without outer-arm dynein force generation, the flagellum cannot beat normally. This causes asthenozoospermia.
5. *(Branch)* In many men, flagellar assembly also fails and the tail becomes short, absent, coiled or irregular (MMAF). In the mouse, disorganized microtubules and outer dense fibers appear in developing spermatids (impaired flagellar assembly).
6. Sperm cannot reach or fertilize the oocyte, so the man is infertile.

**Cell types and processes (suggested terms, to be looked up):**
- Cell types: spermatid (CL:0000018), spermatozoon (CL:0000019).
- Processes: sperm flagellum assembly and axoneme assembly (GO:0007288), outer dynein arm assembly (GO:0036158, check), sperm motility (GO:0097722).
- Compartments: motile cilium or sperm flagellum, axoneme.
- Anatomy: testis (UBERON:0000473), seminiferous tubule, sperm flagellum.
- Protein: a dynein heavy chain with ATPase (AAA) domains. The 2025 paper reports splice variants that truncate the AAA6 domain. Further structure-function detail was not retrieved.

Omics, single-cell and immune data were not retrieved. None are expected for this disorder.

## 7. Anatomical Structures Affected

The primary site is the testis, specifically the post-meiotic germ cells (spermatids) and the sperm flagellum. No extragonadal involvement is reported, in contrast to primary ciliary dyskinesia. That absence is inferred from the isolated-infertility framing, so confirm it in Whitfield 2019. Lateralization is not applicable.

## 8. Temporal Development

Onset is at reproductive age. Course is stable and lifelong, which is inferred. No natural-history or remission data were found.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (OMIM). HPO term HP:0000007.
- **Sex:** males only are affected.
- **Prevalence, carrier frequency, penetrance, founder effects and consanguinity:** not retrieved. Many MMAF cohorts include consanguineous families, but I did not confirm that here.
- **Populations:** cases were reported from several cohorts, including Chinese, North African and Middle Eastern ones. I did not verify this, so check each paper.

## 10. Diagnostics

- **Semen analysis:** severe asthenozoospermia, often with MMAF sperm morphology.
- **Electron microscopy:** absent outer dynein arms and a disorganized axoneme.
- **Immunofluorescence:** reduced or absent *DNAH17* staining in sperm (Sha 2020).
- **Genetic testing:** whole-exome or gene-panel sequencing for *DNAH17* and other MMAF genes (*DNAH1*, *CFAP43*, *CFAP44* and others). Single-gene testing is feasible once the pattern is known. Panel contents were not retrieved.
- **Differential diagnosis:** other causes of asthenozoospermia and MMAF, and primary ciliary dyskinesia.
- **Screening and clinical criteria:** none.

## 11. Outcome / Prognosis

The disorder is not life-limiting. Fertility is the main outcome.
- A pooled 2023 analysis reported worse pregnancy outcomes after ICSI in men with MMAF-type *DNAH17* mutations. Only three men achieved a clinical pregnancy, with ICSI plus assisted oocyte activation (AOA) ([Springer](https://link.springer.com/article/10.1007/s10815-023-02897-7)).
- A newer report of two probands who had ICSI with AOA reported fertilization rates of 90.9–100.0% and blastocyst rates of 66.7–85.7% ([PMC13423380](https://pmc.ncbi.nlm.nih.gov/articles/PMC13423380/)). Its authors recommend ICSI with AOA over conventional IVF. Treat this as a small, conflicting data point, not a settled result.

## 12. Treatment

- **No curative therapy.**
- **Assisted reproduction:** ICSI, possibly with AOA, as above. Suggested NCIT leads, not verified: intracytoplasmic sperm injection and assisted reproductive technology. Look up the IDs before binding them. Per dismech rules, omit the `term:` if no suitable NCIT clinical-intervention term exists.
- **Genetic counseling:** NCIT:C15240 (listed in CLAUDE.md).
- **Pharmacotherapy, gene therapy, trials (NCT):** none found.

## 13. Prevention

Genetic counseling and carrier testing of partners in affected families. Preimplantation or prenatal testing is possible in principle, but I found no source on it. No primary-prevention measures exist.

## 14. Other Species / Natural Disease

No natural disease in other species was found. OMIA and breed data were not checked.

## 15. Model Organisms

- **Mouse:** *Dnah17*−/− mice showed an MMAF phenotype with completely disorganized axonemal structures, and disorganized microtubules and outer dense fibers in spermatids (Zhang et al. 2021, [Mount Sinai record](https://scholars.mssm.edu/en/publications/novel-loss-of-function-variants-in-dnah17-cause-multiple-morpholo/)). The mouse phenocopies the human sperm phenotype. This is MODEL_ORGANISM evidence.
- **ICSI in knockout mice:** a ResearchGate summary says ICSI was performed in patients and KO mice with offspring monitored. I could not retrieve the results.
- **Resources:** an MGI/IMPC page for *Dnah17* appeared in an earlier search, but I did not confirm the gene symbol mapping.
- **Limitations:** not retrieved.

---

## Gaps for Curators

1. Fetch Whitfield 2019, Zhang 2020 (JEM), Sha 2020 and Zhang 2021 with `just fetch-reference` to get PMIDs and abstracts, then quote exact snippets from those.
2. Check GeneReviews and Orphanet for a baseline, using `just check-genereviews`.
3. Look up every HP, GO, CL, UBERON, NCIT and `hgnc:` identifier above in the same step you write it. The ones I gave are leads, not bindings.
4. Frequencies, prevalence, variant spectrum and the ICSI evidence need primary-source reading.

**Sources:**
- [OMIM-derived gene table search results](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C5231438/index.html?cmd=HTOn)
- [DrugMap SPGF39 page](https://drugmap.idrblab.net/data/disease/details/DISWTPU4)
- [LOVD disease #06384](https://databases.lovd.nl/shared/diseases/06384)
- [Sha et al. 2020, Ann Hum Genet](https://onlinelibrary.wiley.com/doi/10.1111/ahg.12369)
- [Zhang et al., JEM](https://rupress.org/jem/article/217/2/e20182365/132579/A-DNAH17-missense-variant-causes-flagella)
- [Zhang et al. 2021, Clin Genet (Mount Sinai record)](https://scholars.mssm.edu/en/publications/novel-loss-of-function-variants-in-dnah17-cause-multiple-morpholo/)
- [J Assist Reprod Genet 2023](https://link.springer.com/article/10.1007/s10815-023-02897-7)
- [Reprod Sci 2025](https://link.springer.com/article/10.1007/s43032-025-02002-6)
- [Asian J Androl, PubMed 41549443](https://pubmed.ncbi.nlm.nih.gov/41549443/)
- [PMC13423380](https://pmc.ncbi.nlm.nih.gov/articles/PMC13423380/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032845` (1 mention) - the report calls it "MONDO"; MONDO calls it **spermatogenic failure 39**
- `HP:0012206` (1 mention) - the report calls it "Asthenozoospermia"; HP calls it **Abnormal sperm motility**
- `HP:0012864` (2 mentions) - the report calls it "check"; HP calls it **Abnormal sperm morphology**
- `HP:0012862` (1 mention) - the report calls it "check"; HP calls it **Abnormal germ cell morphology**
- `NCIT:C15240` (1 mention) - the report calls it "listed in CLAUDE.md"; NCIT calls it **Genetic Counseling**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000018` (1 mention) - the report calls it "Cell types: spermatid"; CL calls it **spermatid**
- `GO:0007288` (1 mention) - the report calls it "Processes: sperm flagellum assembly and axoneme assembly"; GO calls it **sperm axoneme assembly**
- `UBERON:0000473` (1 mention) - the report calls it "Anatomy: testis"; UBERON calls it **testis**