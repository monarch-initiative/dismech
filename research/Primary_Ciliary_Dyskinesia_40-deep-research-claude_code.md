---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T20:12:05.191900'
end_time: '2026-10-14T20:13:42.721771'
duration_seconds: 97.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Primary Ciliary Dyskinesia 40
  mondo_id: MONDO:0032664
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
  num_turns: 9
  total_cost_usd: 0.7897633000000001
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 22
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 19
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 3
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0031318
    reported_labels:
    - Heterotaxy / laterality defect
    ontology_label: Myofiber disarray
  - term_id: HP:0004429
    reported_labels:
    - verify
    ontology_label: Recurrent viral infections
  - term_id: HP:0002205
    reported_labels:
    - verify
    ontology_label: Recurrent respiratory infections
  - term_id: HP:0012206
    reported_labels:
    - verify
    ontology_label: Abnormal sperm motility
  - term_id: HP:0005214
    reported_labels:
    - verify
    ontology_label: Intestinal obstruction
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Ciliary Dyskinesia 40
- **MONDO ID:** MONDO:0032664 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primary Ciliary Dyskinesia 40** covering all of the
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

Status: I've confirmed PCD40 (CILD40) is caused by biallelic DNAH9 variants and have the key PMIDs. I'm now pulling the Loges and Fassad abstracts so I can quote them exactly.

# Primary Ciliary Dyskinesia 40 (CILD40, DNAH9-related)

**Method and limits.** This report rests on web searches and PubMed E-utilities lookups. I could not read OMIM, Orphanet or ClinGen directly (the MalaCards fetch returned 403). Where a statement comes from a secondary aggregator, I say so. Not every detail below was checked against a primary abstract. Items marked **[unverified]** are from my background knowledge or an aggregator and should be checked before curation. Direct quotes below are short and come from search or abstract summaries, not full-text reading. **Run `just fetch-reference PMID:<id>` and re-extract exact snippets before using any quote as evidence.** The PMIDs listed here came from the PubMed search, but I did not confirm every one against the full record.

## 1. Disease information

- **Overview.** PCD40, or CILD40, is an autosomal recessive form of primary ciliary dyskinesia. It is caused by homozygous or compound heterozygous variants in *DNAH9* on chromosome 17p12. DNAH9 encodes an outer dynein arm (ODA) heavy chain. The distinguishing feature is a mild respiratory phenotype with prominent laterality defects. ([MalaCards](https://malacards.org/card/ciliary_dyskinesia_primary_40); [MedGen via NCBI mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/medgen/C4749028/index.html))
- **Identifiers.** MONDO:0032664; OMIM #618300; MedGen C4749028 (per the MedGen mirror URL; "1648365" in one search summary is probably a mis-transcription, so check it); gene *DNAH9* (HGNC symbol; the KB form is lowercase `hgnc:<n>`, and I did not look up the number). ([DrugMap](https://drugmap.idrblab.net/data/disease/details/DISJWDP0); [NORD/MONDO](https://rarediseases.org/mondo-disease/ciliary-dyskinesia-primary-40))
- **Synonyms.** CILD40; "Ciliary dyskinesia, primary, 40, with or without situs inversus"; PCD40.
- **Data source.** This is an aggregated, disease-level description built from case series. It is not EHR-derived.
- **Parent and relatives.** This is one of the genetically defined PCD subtypes, each of which has its own MONDO ID (MONDO:0014910 is another PCD subtype that appeared in the GenCC results, not this one).

## 2. Etiology

- **Cause.** Biallelic loss-of-function (LoF) variants in *DNAH9*. Loges et al. reported "loss-of-function mutations in DNAH9 in five independent families" ([PMID:30471718](https://pubmed.ncbi.nlm.nih.gov/30471718/)). Fassad et al. identified *DNAH9* mutations in PCD-clinic individuals with situs inversus and, in one case, male infertility ([PMID:30471717](https://pubmed.ncbi.nlm.nih.gov/30471717/)).
- **Risk and protective factors.** None are established for this recessive monogenic condition. A common-variant study reported an interaction between *DNAH9* and early-life smoke exposure for bronchial hyperresponsiveness ([PMID:26797031](https://pubmed.ncbi.nlm.nih.gov/26797031/)), but that concerns asthma-type traits in the general population, not CILD40.
- **Gene–environment.** Tobacco smoke and airway infections plausibly worsen respiratory disease in any PCD. I found no CILD40-specific data **[unverified]**.

## 3. Phenotypes

| Phenotype | Suggested HPO | Frequency / note |
|---|---|---|
| Situs inversus totalis | HP:0001696 | Reported in all CILD40 patients in the MalaCards/OMIM summary. Caution: a single family in Fassad had an affected sibling pair, both with situs inversus. |
| Heterotaxy / laterality defect | HP:0031318 | Several patients with severe congenital heart disease ([PMID:35050399](https://pubmed.ncbi.nlm.nih.gov/35050399/); [PMID:40376972](https://pubmed.ncbi.nlm.nih.gov/40376972/)) |
| Congenital heart defect | HP:0001627 | Cilia-related CHD in Chinese cohort (Chen 2022) |
| Chronic rhinosinusitis | HP:0004429 (verify) | Reported in the Somali sibling pair |
| Recurrent respiratory infections / productive cough | HP:0002205 (verify) | Pediatric productive cough ([PMID:33452233](https://pubmed.ncbi.nlm.nih.gov/33452233/)) |
| Bronchiectasis | HP:0002110 | Not well documented in the sources I found; typically late and mild if present **[unverified]** |
| Male infertility / asthenozoospermia | HP:0012206 (verify) | Fassad (one case); [PMID:33610189](https://pubmed.ncbi.nlm.nih.gov/33610189/); [PMID:39523437](https://pubmed.ncbi.nlm.nih.gov/39523437/) |
| Jejunal atresia | HP:0005214 (verify) | Single Bahraini child ([PMID:36712782](https://pubmed.ncbi.nlm.nih.gov/36712782/)); a single report, so treat as an anecdotal association |

- **Respiratory course.** MalaCards says "compared with other CILDs the respiratory phenotype is relatively mild and patients typically do not develop serious lung disease." Symptoms typically begin in childhood as mild upper respiratory infections.
- **Normal screening tests.** One conference abstract reports normal nasal nitric oxide, normal ciliary beat frequency and preserved mucociliary clearance in three patients ([ERJ abstract](https://publications.ersnet.org/content/erj/52/suppl62/pa4667)). This conflicts with Fassad, who found a reduced beat frequency in the distal cilia (see below). Likely explanation: the defect is subtle and regional, so results vary by method.
- **Quality of life.** No CILD40-specific data found.

## 4. Genetic / molecular information

- **Gene.** *DNAH9*, 17p12, dynein axonemal heavy chain 9, with ~70 exons **[unverified]**. The original gene description is Bartoloni et al. ([PMID:11247663](https://pubmed.ncbi.nlm.nih.gov/11247663/)).
- **Variants.** Biallelic LoF (nonsense, frameshift, splice) and some missense variants have been reported across the case series above. I did not extract specific variant nomenclature or ClinVar classifications.
- **Variant origin.** Germline.
- **Allele frequency / founder effects.** Not checked. Check gnomAD and ClinVar before curation.
- **Modifiers and epigenetics.** None known.
- **Chromosomal abnormalities.** Not applicable.
- **Gene-disease validity.** The DrugMap/GenCC data list the DNAH9 association as strong; I could not read the ClinGen record. If a ClinGen assertion exists, cache it as `CGGV:` rather than recording a tier from memory.

## 5. Environmental information

No specific environmental or infectious causes. Secondary respiratory pathogens (e.g., *Haemophilus influenzae*, *Pseudomonas aeruginosa*) are expected as in other PCD forms **[unverified for CILD40]**.

## 6. Mechanism / pathophysiology

**Causal chain**

1. Biallelic germline *DNAH9* LoF variants lead to absent or truncated DNAH9 protein. (Demonstrated: Loges 2018, Fassad 2018.)
2. Loss of DNAH9 results in loss of DNAH9/DNAH5-containing type 2 ODAs, which is restricted to the distal region of the cilium. Fassad et al.: "DNAH9 and its partner heavy chain DNAH5 localize to type 2 ODAs of the distal cilium... a loss of DNAH9/DNAH5-containing type 2 ODAs that was restricted to the distal cilia region." Electron tomography confirmed regional loss of whole or partial ODAs. Loges et al. found that DNAH9-deficient cilia also lack other ODA components in the distal axoneme, and that DNAH9 interacts with DNAH5, DNAI2 and CCDC114. (Demonstrated, in human cells.)
3. Loss of distal type 2 ODAs leads to a reduced beat frequency with a subtle beat-pattern defect in the distal cilium portion. (Demonstrated, Fassad.) Proximal ODAs, which contain DNAH11 and DNAH5, are preserved, which explains the milder, sometimes near-normal, standard tests.
4. In motile monocilia of the embryonic node, impaired motility leads to defective leftward flow and randomized left-right axis determination. This is **inferred** from the genotype–phenotype pattern and from the general model of ODA-related laterality defects; I did not verify a DNAH9-specific node study.
5. Randomized laterality results in situs inversus and, in some cases, heterotaxy with congenital heart disease. (Observed in patients.)
6. In the airway, partially preserved ciliary function results in milder mucociliary clearance impairment, with childhood-onset cough and upper-airway infections. (Observed.)
7. In the male reproductive tract, impaired sperm flagellar motility results in asthenozoospermia and infertility. (Observed in a subset.)

**Suggested ontology terms** (check each with a lookup before binding): GO "outer dynein arm assembly" (GO:0036158, verify), "cilium movement" (GO:0003341, verify), "determination of left/right symmetry" (GO:0007368, verify); CL ciliated columnar epithelial cell of the airway, sperm (CL:0000019), embryonic node monocilia cells; GO:CC "outer dynein arm" (GO:0005858, verify).

**Immune, metabolic and omics findings.** None established for CILD40 in the humans reported. A mouse study (below) describes mucin accumulation and immune cell infiltration.

## 7. Anatomical structures affected

- **Primary:** motile cilia of the respiratory tract (nose, paranasal sinuses, bronchi), the embryonic left-right organizer (node), and sperm flagella.
- **Secondary:** heart (laterality-related CHD), middle ear (in other PCD forms; not verified here), gut (single jejunal atresia report).
- **Subcellular:** distal ciliary axoneme, outer dynein arms.
- **Lateralization:** the laterality phenotype is a mirror image, not an asymmetric loss.

## 8. Temporal development

- **Onset:** congenital, because laterality defects are present at birth. Respiratory symptoms appear in childhood.
- **Progression:** generally mild and slowly progressive or stable. Long-term data are lacking **[unverified]**.
- **Critical period:** embryonic left-right patterning. This cannot be reversed postnatally.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007).
- **Prevalence:** CILD40 prevalence is not established. Overall PCD prevalence is roughly 1 in 10,000–20,000 **[unverified for this report; check Orphanet]**. DNAH9 variants appear to be a rare cause among PCD cases.
- **Case series origins:** European, Somali-British, Japanese, Chinese, and Bahraini patients have been reported, which suggests no single population is dominant. See Fassad, Loges, [PMID:35050399](https://pubmed.ncbi.nlm.nih.gov/35050399/), [PMID:34008076](https://pubmed.ncbi.nlm.nih.gov/34008076/) (Japanese fetus), [PMID:39115416](https://pubmed.ncbi.nlm.nih.gov/39115416/).
- **Carrier frequency, penetrance, consanguinity:** not examined.

## 10. Diagnostics

- **Hallmark findings.** Situs abnormality in a child with chronic respiratory symptoms should prompt PCD evaluation.
- **Why standard tests can mislead.** Because the defect is restricted to distal cilia, nasal NO, high-speed video analysis and routine transmission electron microscopy can look normal or near-normal. Loges et al. and Fassad et al. both describe this. The conference abstract reports normal nasal NO and ciliary beat frequency. So **a normal screen does not rule out CILD40**.
- **More informative tests.** Immunofluorescence for DNAH9 and DNAH5 along the cilium (showing a distal-only pattern), electron tomography, and genetic testing.
- **Genetic testing.** PCD multigene panel or exome sequencing including *DNAH9*; several of the cited cases were found by exome sequencing ([PMID:34008076](https://pubmed.ncbi.nlm.nih.gov/34008076/), [PMID:33452233](https://pubmed.ncbi.nlm.nih.gov/33452233/)).
- **Differential:** other ODA defects (DNAH5, DNAI1, DNAH11), other laterality disorders (heterotaxy from *ZIC3*, *MMP21*, *PKD1L1*, *GDF1*; see [PMID:42630107](https://pubmed.ncbi.nlm.nih.gov/42630107/)), and CF.
- **Guideline.** The [practical guide for PCD diagnosis and management](https://www.sciencedirect.com/science/article/pii/S0385814624000166) is a general PCD reference.

## 11. Prognosis

The lung disease is expected to be milder than other PCD forms. I found no CILD40-specific survival data. Prognosis in patients with complex CHD depends mainly on the cardiac lesion.

## 12. Treatment

No CILD40-specific trials were found. Management follows general PCD care: airway clearance physiotherapy (NCIT: verify), prompt antibiotic treatment of infections (NCIT:C15986 Pharmacotherapy; agents vary), vaccination (NCIT:C15346), management of sinus and ear disease, and surgical or medical care of CHD where present. Assisted reproduction is an option for infertile men. Mucolytics, long-term macrolides and inhaled antibiotics are used in other PCD forms **[unverified for this subtype]**. Experimental: a mouse/organoid study screened mitochondria-targeting drugs that partly improved cilia beating (see below); this is preclinical only. Gene therapy is not available.

## 13. Prevention

Genetic counseling for a recessive condition (25% recurrence risk per pregnancy, NCIT:C15240); carrier testing for relatives; prenatal or preimplantation testing where the familial variants are known. Early diagnosis is useful so that respiratory care can start even when screening tests look normal.

## 14. Other species / natural disease

Not checked (OMIA was not searched). Dynein arm defects cause PCD-like disease in dogs and other species, but I have no DNAH9-specific entries **[unverified]**.

## 15. Model organisms

- **Mouse, *Dnah9* knockdown, plus airway organoids.** Zheng et al. studied a patient with compound *DNAH9* mutation. Per the summary I retrieved, the knockdown mice "recapitulated the patient phenotypes", with low lung function, mucin accumulation and immune cell infiltration; airway organoids were used to screen drugs, with mitochondria-targeting compounds partly improving cilia beating ([PMID:35729109](https://pubmed.ncbi.nlm.nih.gov/35729109/)). Evidence source: model organism / in vitro. Limitation: this is a knockdown, not a null, and the cited patient's phenotype is what is "recapitulated", so fidelity to the laterality phenotype is not established here.
- **Earlier work.** Mislocalization of DNAH5 and DNAH9 in PCD respiratory cells ([PMID:15750039](https://pubmed.ncbi.nlm.nih.gov/15750039/)), human cell evidence.
- Zebrafish, *Chlamydomonas* and other models: not searched.

## Gaps to close before curation

1. Pull OMIM #618300 text, ClinVar/ClinGen entries and the Orphanet record through the repo's structured-source routes.
2. Read the Loges and Fassad full texts for variant nomenclature, cohort sizes and quotable snippets.
3. Check whether an HP term is appropriate for "distal ODA loss" or whether to leave it unbound.
4. Verify each HPO, GO and CL ID marked "verify" with a lookup. I did not run any term lookup, so no CURIE here is checked.
5. Resolve the conflict between normal ciliary beat frequency (conference abstract) and reduced frequency (Fassad).

## Sources

- [MalaCards, CILD40](https://malacards.org/card/ciliary_dyskinesia_primary_40)
- [NORD/MONDO, ciliary dyskinesia, primary, 40](https://rarediseases.org/mondo-disease/ciliary-dyskinesia-primary-40)
- [DrugMap disease DISJWDP0](https://drugmap.idrblab.net/data/disease/details/DISJWDP0)
- [MedGen C4749028 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/medgen/C4749028/index.html)
- [Fassad et al. 2018, AJHG](https://www.cell.com/ajhg/fulltext/S0002-9297(18)30368-9), PMID:30471717
- Loges et al. 2018, AJHG, PMID:30471718
- [ERJ 2018 conference abstract on DNAH9 cilia](https://publications.ersnet.org/content/erj/52/suppl62/pa4667)
- PubMed E-utilities lookups for the other PMIDs cited above

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 9 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031318` (1 mention) - the report calls it "Heterotaxy / laterality defect"; HP calls it **Myofiber disarray**
- `HP:0004429` (1 mention) - the report calls it "verify"; HP calls it **Recurrent viral infections**
- `HP:0002205` (1 mention) - the report calls it "verify"; HP calls it **Recurrent respiratory infections**
- `HP:0012206` (1 mention) - the report calls it "verify"; HP calls it **Abnormal sperm motility**
- `HP:0005214` (1 mention) - the report calls it "verify"; HP calls it **Intestinal obstruction**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001627` (1 mention) - the report calls it "Congenital heart defect"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names