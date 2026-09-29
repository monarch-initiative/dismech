---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-12T17:37:29.204757'
end_time: '2026-09-12T17:42:20.651611'
duration_seconds: 291.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Uterine Leiomyoma
  mondo_id: MONDO:0007886
  category: Complex
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
  web_search_requests: 17
  num_turns: 19
  total_cost_usd: 1.3128661999999998
  session_id: 8a14391c-ae91-5ecd-9b2c-79a47d372ef7
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 71
reference_validation:
  total_references: 49
  verified: 49
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 49
  on_topic: 29
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 11
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0030318
    reported_labels:
    - Pelvic pain
    ontology_label: Angular cheilitis
  - term_id: HP:0030068
    reported_labels:
    - Dyspareunia
    ontology_label: Olfactory esthesioneuroblastoma
  - term_id: HP:0031801
    reported_labels:
    - Abdominal mass
    ontology_label: Vocal cord dysfunction
  - term_id: UBERON:0000459
    reported_labels:
    - endometrium
    ontology_label: uterine wall
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Uterine Leiomyoma
- **MONDO ID:** MONDO:0007886 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Uterine Leiomyoma** covering all of the
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

I have gathered comprehensive research across all major domains. I'll now compile the full report.

I now have sufficient research depth across all sections to compile the comprehensive report.

# Uterine Leiomyoma (Uterine Fibroids): Comprehensive Research Report

## 1. Disease Overview and Identifiers

**Overview:** Uterine leiomyomas (also called uterine fibroids, myomas, or leiomyomata uteri) are benign monoclonal smooth-muscle-cell tumors of the myometrium, composed of disorganized, hypertrophic myofibroblasts embedded in an abundant, disease-defining extracellular matrix (ECM) that constitutes a substantial fraction of tumor volume ([Endocrine Reviews, 2022](https://academic.oup.com/edrv/article/43/4/678/6422392); [PMC10051203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10051203/)). They are the most common pelvic tumors in women of reproductive age, affecting an estimated ~75% of women by menopause when systematically screened, though clinically apparent (symptomatic/diagnosed) prevalence is substantially lower ([PMC12488583](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488583/); PubMed 36001050).

**Key identifiers:**
- **MONDO:** MONDO:0007886
- **OMIM:** #150699 (Leiomyoma, Uterine, Somatic) — the somatic/sporadic form; #150800 (Hereditary Leiomyomatosis and Renal Cell Cancer, HLRCC) for the germline-predisposed syndromic form
- **Orphanet:** Uterine fibroids are generally not classified as a rare disease in Orphanet given their high population prevalence, but HLRCC has an Orphanet entry as a rare hereditary tumor-predisposition syndrome
- **ICD-10-CM:** D25 (Leiomyoma of uterus), with subcodes D25.0 (submucous), D25.1 (intramural), D25.2 (subserosal), D25.9 (unspecified)
- **ICD-11:** GB50 (Leiomyoma of uterus)
- **MeSH:** D007889 (Leiomyoma), cross-referenced with D014594 (Uterine Neoplasms)

**Synonyms:** Uterine fibroid(s), myoma(s), fibromyoma, leiomyoma uteri, fibroleiomyoma.

**Evidence base:** Information derives primarily from aggregated disease-level resources — population registries (SEER-adjacent gynecologic registries, GBD, national health-linkage cohorts), large clinical trial cohorts (LIBERTY, Elaris, PRIMROSE), pathology/genomic tumor banks (TCGA-adjacent and independent whole-exome/whole-genome sequencing cohorts), and case series — rather than single-patient EHR mining, though the NIEHS Uterine Fibroid Study and Black Women's Health Study contribute large prospective individual-level cohort data.

---

## 2. Etiology

### 2a. Somatic genetic drivers (disease-causal factors)
Uterine leiomyoma pathogenesis is now understood as arising from **at least three-to-four mutually exclusive somatic driver subtypes**, together accounting for up to ~90%+ of tumors ([eLife 2018, 37110](https://elifesciences.org/articles/37110); OMIM #150699):

1. **MED12 exon 2 hotspot mutations** (~70% of tumors) — the dominant driver class. MED12 is a subunit of the Mediator transcriptional co-activator complex; mutant MED12 alters CDK8/Mediator kinase module activity and dysregulates Wnt4/β-catenin and TGF-β/EMT signaling ([Sci Rep 2024, s41598-024-84439-4](https://www.nature.com/articles/s41598-024-84439-4); [PMC13512488](https://pmc.ncbi.nlm.nih.gov/articles/PMC13512488/); ScienceDirect S2949838425000325). A 2024 mechanistic study also implicated MED12-mutant tumors in upregulating **TDO2** and activating the tryptophan→kynurenine→aryl hydrocarbon receptor (AHR) axis to drive proliferation ([PMC10561729](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10561729/)).
2. **HMGA2 overexpression/rearrangement** (via chromosome 12q14-15 rearrangements, often t(12;14)) — second most common subtype.
3. **Fumarate hydratase (FH)-deficient leiomyomas** (0.4–2.6% of tumors) — arise from biallelic FH inactivation (loss of function via missense/truncating mutation plus loss of heterozygosity), leading to fumarate accumulation, pseudohypoxia (HIF stabilization), and a distinctive "staghorn" vasculature and eosinophilic-cytoplasm histology ([bioRxiv 663609](https://www.biorxiv.org/content/10.1101/663609v1.full); [PMC10048203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10048203/)). This subtype overlaps with the hereditary HLRCC syndrome (see §9).
4. Rarer subtypes: COL4A5-COL4A6 deletions (Alport-syndrome-adjacent locus) and other minor genomic rearrangement classes.

Genome-stability genes (**TP53, ATM**) and telomere-maintenance genes (**TERT, TERC, OBFC1/STN1**) have also been implicated by GWAS as broader predisposition loci, suggesting UL risk operates through both direct smooth-muscle mitogenic pathways and genome-instability/telomere-biology pathways ([eLife 37110](https://elifesciences.org/articles/37110)).

### 2b. Risk Factors

**Genetic risk factors:**
- Family history of fibroids (first-degree relative) approximately doubles risk.
- GWAS-identified susceptibility loci near **HMGA2**, the **RGS7-FH interval on 1q43** ([PMC4526794](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4526794/)), **TP53, ATM, TERT, TERC, OBFC1**, and loci implicated in genitourinary tract development ([eLife 37110](https://elifesciences.org/articles/37110); [PMC4501220](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4501220/), NIEHS multi-ethnic replication study).
- A Mendelian randomization study found genetic liability to multiple metabolic/reproductive traits contributes causally to leiomyoma risk ([PMC10415162](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10415162/)).
- Germline **FH** pathogenic variants (autosomal dominant) cause HLRCC syndrome with early-onset, numerous, and larger uterine leiomyomas (see §9).

**Environmental/lifestyle risk factors:**
- **Age**: risk rises steeply from the mid-30s, peaking in the 40s ("Global and regional trends," [PMC11556989](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556989/); Australian linkage cohort, [PMC11373412](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11373412/)).
- **Race/ancestry**: Black women are diagnosed 2–3× more often than White women, with earlier age of onset and larger/more numerous tumors — nearly 25% of Black women aged 18-30 have fibroids vs. ~6% of White women, rising to ~60% of Black women by age 35 ([Michigan Medicine](https://www.michiganmedicine.org/health-lab/understanding-racial-disparities-women-uterine-fibroids); [AJOG](https://www.ajog.org/article/S0002-9378(24)00739-7/fulltext)). Genetic ancestry studies suggest fibroproliferative risk-allele frequency differs by African vs. European ancestry, potentially explaining up to 69% of the disparity in some models, though social/structural/environmental drivers (chronic stress, adverse childhood experiences, perceived racism, environmental contaminant exposure) are increasingly recognized as independent contributors ([PMC8463481](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8463481/); [ScienceDirect S0015028223000602](https://www.sciencedirect.com/science/article/pii/S0015028223000602)).
- **Obesity**: consistent risk factor, OR ≈1.19 (suggestive-strength evidence in umbrella review) via increased peripheral estrogen conversion ([ScienceDirect S2468784722001994](https://www.sciencedirect.com/science/article/abs/pii/S2468784722001994)).
- **Early menarche**, nulliparity, hypertension, chronic inflammation.
- **Endocrine-disrupting chemical exposure**: in-utero and adult exposure to phthalates (e.g., DEHP) and bisphenol A (BPA) is an emerging risk factor; DEHP metabolites are also associated with lower vitamin D status, suggesting compounding mechanisms ([PMC7483495](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7483495/); Eker rat DES-exposure model, [PMC7349254](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7349254/)).
- **Vitamin D deficiency**: robustly associated with fibroid presence/size; mechanistic work shows VDR knockdown in myometrial cells induces DNA double-strand breaks and impairs DNA-damage-response, implicating a calcitriol/VDR-DNA repair axis ([Endocrine Reviews 2026, edrv/8456362](https://academic.oup.com/edrv/article/47/3/329/8456362); [PMC13167191](https://pmc.ncbi.nlm.nih.gov/articles/PMC13167191/); [PMC7917888](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7917888/)).

**Protective factors:**
- **Parity**: parous women have a lower risk than nulliparous women (dose-dependent with number of births) ([Korea Nurses' Health Study, PMC10257256](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10257256/)).
- **Oral contraceptive use**: current use associated with reduced risk (RR ≈0.43 in some meta-analyses), though findings have varied by formulation and duration across studies ([PMC10056617](https://pmc.ncbi.nlm.nih.gov/articles/PMC10056617/)).
- Cigarette smoking has been reported as inversely associated in some (older) epidemiologic studies, plausibly via anti-estrogenic metabolic effects, though this is not advocated clinically given smoking's other harms.

**Gene-environment interaction:** The Eker rat model directly demonstrates a genetic (Tsc2 germline mutation) × environmental (developmental diethylstilbestrol/endocrine-disruptor exposure) interaction, in which DES exposure amplifies DNA damage specifically in myometrial stem cells of Tsc2-mutant animals, and vitamin D3 supplementation mitigates this damage — a mechanistic bridge between the genetic, environmental, and vitamin D literatures ([PMC7349254](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7349254/)).

---

## 3. Phenotypes

| Phenotype | Type | Suggested HPO term | Frequency/Notes |
|---|---|---|---|
| Heavy menstrual bleeding (menorrhagia) | Symptom | HP:0000132 (Menorrhagia) | ~30% of all patients; most common presenting symptom; a major cause of iron-deficiency anemia and elective hysterectomy ([PMC9580818](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9580818/)) |
| Iron-deficiency anemia | Lab abnormality | HP:0001891 (Iron deficiency anemia) | Secondary to chronic HMB |
| Chronic pelvic pain / pressure | Symptom | HP:0030318 (Pelvic pain) | Bulk-related; correlates with tumor size/number |
| Dysmenorrhea | Symptom | HP:0100608 (Dysmenorrhea) | Common, variable severity |
| Dyspareunia | Symptom | HP:0030068 (Dyspareunia) | Bulk-related, position-dependent |
| Urinary frequency / bladder pressure | Symptom | HP:0000103 (Polyuria) / bladder-compression related | Anterior/large fibroids compressing bladder |
| Constipation | Symptom | HP:0002019 (Constipation) | Posterior fibroids compressing rectum |
| Abdominal/pelvic mass | Physical sign | HP:0031801 (Abdominal mass) or pelvic mass equivalent | Palpable on exam when large |
| Infertility | Symptom/reproductive | HP:0000789 (Infertility) | Especially with cavity-distorting (submucosal, FIGO 0-2) fibroids |
| Recurrent pregnancy loss | Reproductive | HP:0005268 (Recurrent miscarriage) | Associated with cavity distortion |
| Acute pain (red degeneration) | Symptom (in pregnancy) | — | Painful infarction during rapid pregnancy-associated growth |

**Onset:** Typically detected in the reproductive years (30s–40s); rare before menarche; regression is expected after menopause due to estrogen/progesterone withdrawal.

**Severity/progression:** Highly variable — many fibroids are asymptomatic incidental findings; others cause severe, quality-of-life-limiting bleeding and bulk symptoms. Growth is generally slow but hormonally responsive (accelerates in pregnancy, regresses postmenopause); course is typically stable-to-slowly-progressive rather than episodic, though rapid growth raises concern for degeneration or (rarely) sarcoma.

**Frequency of symptoms among affected individuals:** More than half of women with fibroids experience heavy menstrual bleeding, pelvic pain, or infertility-related symptoms; a substantial proportion remain asymptomatic ([PMC12859363](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12859363/); AAFP rapid evidence review, 2025).

**Quality of life impact:** HMB is described as the primary driver of health-related quality-of-life deterioration in fibroid patients and the major reason for elective hysterectomy ([PMC9580818](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9580818/)). Validated instruments (UFS-QOL, a fibroid-specific tool; general EQ-5D/SF-36) are used in trials (e.g., LIBERTY, Elaris) to capture symptom severity and QOL domains (energy/mood, control, self-consciousness, sexual function).

---

## 4. Genetic/Molecular Information

**Causal genes / mutation classes:**
- **MED12** (HGNC:29305; Xq13.1) — exon 2 hotspot missense/small in-frame indel mutations in ~70% of tumors; somatic, mosaic across tumor but clonal within it.
- **HMGA2** (HGNC:5013; 12q14.3) — overexpression driven by chromosomal rearrangement/translocation (e.g., t(12;14)(q14-15;q23-24)), disrupting a 3' UTR microRNA (let-7)-binding regulatory region.
- **FH** (HGNC:3700; 1q43) — biallelic loss-of-function (germline + somatic second hit in HLRCC; purely somatic biallelic in sporadic FH-deficient subtype); loss of fumarate hydratase enzymatic activity in the TCA cycle causing fumarate accumulation, succination of proteins (2SC adduct), and HIF-1α pseudohypoxic stabilization.
- **COL4A5/COL4A6** deletion subtype (rare).
- **TSC2** — germline mutation in the Eker rat model (not a major human somatic driver but mechanistically informative).

**Variant classification (ACMG/ClinVar framework):**
- Somatic MED12/HMGA2/FH alterations are tumor-driver mutations, not germline ACMG-classified variants, and are typically reported in a cancer-genomics/somatic framework (pathogenic driver vs. passenger) rather than ClinVar pathogenicity tiers.
- Germline FH variants causing HLRCC are curated in ClinVar/ClinGen as Pathogenic/Likely Pathogenic (autosomal dominant); >200 distinct FH coding mutations have been described ([PMC9128909](https://pmc.ncbi.nlm.nih.gov/articles/PMC9128909/); [PMC10048203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10048203/), reporting c.1132G>A as one example).

**Somatic vs. germline origin:** The overwhelming majority of driver mutations (MED12, HMGA2 rearrangement, sporadic FH-deficient) are **somatic**, acquired independently in each tumor (explaining why patients frequently harbor multiple genetically distinct fibroids — a polyclonal field of monoclonal tumors). Germline FH mutation defines the syndromic HLRCC subset only.

**Functional consequences:**
- MED12 mutations: partial loss/alteration of Mediator-CDK8 kinase-module function → dysregulated Wnt/β-catenin and TGF-β/EMT transcriptional programs, plus tryptophan-kynurenine-AHR pathway activation and MMP-9-driven ECM remodeling ([ScienceDirect S002751072300026X](https://www.sciencedirect.com/science/article/abs/pii/S002751072300026X); [ScienceDirect S2949838425000325](https://www.sciencedirect.com/science/article/pii/S2949838425000325)).
- FH loss: classic loss-of-function tumor-suppressor mechanism → metabolic (pseudohypoxic) gain-of-signaling phenotype.
- HMGA2: gain-of-function overexpression via loss of 3'UTR-mediated let-7 repression.

**Epigenetics:** A 2025 study found MED12-mutation status predicts patterns of aberrant DNA methylation in leiomyomas, indicating a genetic-epigenetic interaction shaping subtype-specific gene expression programs ([PMC13512488](https://pmc.ncbi.nlm.nih.gov/articles/PMC13512488/)). Broader epigenomic dysregulation (DNA methylation, histone modification) has been documented across leiomyoma subtypes relative to adjacent myometrium (ENCODE/Roadmap-adjacent studies, cited in mechanistic reviews such as [PMC10056617](https://pmc.ncbi.nlm.nih.gov/articles/PMC10056617/)).

**Chromosomal abnormalities:** Recurrent cytogenetic rearrangements define UL molecular subclasses — t(12;14)(q14-15;q23-24) (HMGA2), del(7)(q22q32), trisomy 12, and rearrangements of 6p21 (HMGA1) — consistent with a limited set of recurrent structural drivers rather than complex genomic instability typical of malignancy.

---

## 5. Environmental Information

- **Endocrine-disrupting chemicals**: In-utero and lifetime exposure to phthalates (DEHP and metabolites) and bisphenol A are implicated as risk-modifying exposures, demonstrated mechanistically in the Eker rat DES model and epidemiologically in human cohorts ([PMC7483495](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7483495/); [PMC7349254](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7349254/)).
- **Lifestyle factors**: obesity (adiposity increases peripheral aromatization of androgens to estrogen), diet, and possibly chronic psychosocial stress (implicated as a disparities driver) ([ScienceDirect S0015028223000602](https://www.sciencedirect.com/science/article/pii/S0015028223000602)).
- **Air pollution/environmental contaminant exposure**: cited among structural/environmental drivers contributing to racial disparities in fibroid incidence and severity (Michigan Medicine/IHPI summary).
- **Infectious agents**: None established as causal for uterine leiomyoma; this is not an infection-driven disease.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from initiating lesion to clinical manifestation)

1. A myometrial smooth-muscle stem/progenitor cell acquires a somatic driver alteration — most commonly a **MED12 exon 2 mutation** (~70%), or alternatively an **HMGA2 rearrangement**, or **biallelic FH inactivation** (0.4–2.6%) — establishing a clonal population. *[Demonstrated at the molecular/genomic level, inferred as the initiating event given multiple independent clonal tumors per uterus.]*
2. The driver mutation dysregulates transcriptional programs within that clone: MED12-mutant cells show **activation of canonical Wnt4/β-catenin signaling and TGF-β/EMT signaling**, and elevated **TDO2-driven tryptophan-to-kynurenine conversion activating the aryl hydrocarbon receptor (AHR)** ([PMC10561729](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10561729/); ScienceDirect S2949838425000325). FH-deficient cells accumulate fumarate, succinate host proteins, and stabilize HIF-1α, producing a pseudohypoxic transcriptional state.
3. This leads to **clonal smooth-muscle-cell proliferation** *[demonstrated]*, forming a discrete, well-circumscribed tumor nodule distinct from surrounding normal myometrium.
4. Ovarian steroid hormones (**estrogen and progesterone**) act as the principal growth-promoting cofactors for the established clone: estrogen upregulates progesterone-receptor expression and growth-factor signaling, while progesterone is now recognized as the dominant proliferative driver in adult fibroid growth, acting through progesterone-receptor-mediated induction of pro-growth and anti-apoptotic genes. *[Demonstrated via responsiveness to GnRH agonist/antagonist and progesterone-modulator therapy, which shrink tumors by suppressing this axis — see §12.]*
5. Growth-factor cascades — **TGF-β, activin-A, platelet-derived growth factor (PDGF), and connective tissue growth factor (CTGF)** — are upregulated within the tumor and act on the surrounding myofibroblast-like tumor cells, driving both further proliferation and **excessive extracellular matrix (ECM) synthesis** ([PMC10051203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10051203/); [PMC12784659](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12784659/)).
6. The **ECM (collagen types I/III, fibronectin, versican, other proteoglycans) accumulates in disproportionate excess relative to cellular content**, acting as both structural scaffold and reservoir that binds and prolongs the activity of TGF-β and other growth factors — creating a self-reinforcing fibrotic feed-forward loop. *[Demonstrated — ECM constitutes the majority of tumor mass by volume.]*
7. **MMP-9 and other matrix metalloproteinases** are dysregulated (upregulated by mutant-MED12 signaling) and contribute to abnormal matrix remodeling and tumor expansion ([ScienceDirect S002751072300026X](https://www.sciencedirect.com/science/article/abs/pii/S002751072300026X)).
8. Concurrent **angiogenic remodeling** occurs, driven by VEGF and (in FH-deficient tumors specifically) by HIF-driven pseudohypoxic angiogenic signaling, producing the histologically distinctive "staghorn" vasculature seen in FH-deficient leiomyomas ([PMC8185197](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8185197/)).
9. As the fibrotic, hypervascular mass enlarges within the myometrium, it produces **mechanical and physiological disruption of the overlying/adjacent endometrium and myometrial contractility**: increased endometrial surface area, venule ectasia/congestion, and impaired local hemostatic factors → **heavy menstrual bleeding**, and impaired coordinated myometrial contraction contributing to bleeding and dysmenorrhea ([PMC9580818](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9580818/)).
10. Depending on **anatomical location** (see FIGO classification, §7/10), the enlarging mass produces **bulk-related manifestations**: cavity distortion → infertility/pregnancy loss (submucosal, FIGO 0–2); bladder/rectal compression → urinary frequency/constipation (large intramural/subserosal); and pregnancy-associated rapid growth can outstrip blood supply, causing **infarction ("red degeneration") and acute pain**.
11. In the rare germline-FH (HLRCC) pathway, the same FH-loss/pseudohypoxic mechanism operating in skin and kidney produces **cutaneous leiomyomas and an aggressive, early-onset papillary type 2 renal cell carcinoma**, making the uterine phenotype part of a multi-organ tumor-predisposition syndrome rather than an isolated uterine disease (see §9) — this branch is **inferred to share the core FH-loss mechanism** with sporadic FH-deficient fibroids but is **demonstrated** to differ in tissue-selective consequences (renal carcinogenesis specifically).
12. Rarely, **secondary genetic alterations** (e.g., ALK rearrangement, 14q loss) accumulate in an existing leiomyoma clone, driving **malignant transformation to leiomyosarcoma** — this remains a mechanistically distinct, low-probability branch rather than the typical fibroid trajectory ([Oncotarget 25137](https://www.oncotarget.com/article/25137/text/); [PMC6021249](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6021249/)).

### Cellular and molecular detail by category

- **Molecular pathways**: Wnt4/β-catenin, TGF-β/SMAD and non-canonical EMT signaling, tryptophan-kynurenine-AHR axis, PI3K-AKT-mTOR (growth-factor downstream), HIF-1α/pseudohypoxia (FH-deficient subtype). Suggested GO terms: GO:0016055 (Wnt signaling pathway), GO:0007179 (transforming growth factor beta receptor signaling pathway), GO:0001525 (angiogenesis).
- **Cellular processes**: smooth-muscle-cell proliferation, epithelial-to-mesenchymal-transition-like myofibroblast activation, apoptosis resistance, excessive ECM deposition/fibrosis.
- **Protein dysfunction**: MED12 Mediator-complex conformational alteration (not classic misfolding); FH enzymatic loss-of-function; HMGA2 architectural transcription-factor overexpression.
- **Metabolic changes**: TCA-cycle disruption and fumarate accumulation in FH-deficient tumors; tryptophan catabolism shift toward the kynurenine pathway in MED12-mutant tumors.
- **Tissue damage mechanisms**: fibrosis (excess ECM), localized ischemia/infarction (red degeneration, especially in pregnancy), abnormal angiogenesis.
- **Cell types involved**: uterine smooth muscle cell (relevant CL term: **CL:0002598**, myometrial smooth muscle cell, or the general **CL:0000192** smooth muscle cell), myofibroblast-like tumor cells, endothelial cells, and a minor immune infiltrate — all characterized by recent single-cell RNA-seq atlases showing substantial cellular heterogeneity within both normal myometrium and leiomyoma tissue, including diverse SMC, fibroblast, and endothelial subpopulations ([bioRxiv 2020.12.21.402313](https://www.biorxiv.org/content/10.1101/2020.12.21.402313v1.full); PubMed 36001050).
- **Cell/tumor origin**: The field's working model long postulated a **monoclonal origin** from a single dysregulated multipotent myometrial stem cell per tumor; however, newer single-cell atlases describe a **"non-monoclonal" origin of diverse and novel constituent cell types** even though each tumor's principal proliferative smooth-muscle clone remains monoclonal — the precursor/tumor-initiating cell's precise identity remains unresolved ([bioRxiv 2020.12.21.402313](https://www.biorxiv.org/content/10.1101/2020.12.21.402313v1.full); Human Reproduction 2024, O-264 tumor-initiating-cell multi-omics abstract).

---

## 7. Anatomical Structures Affected

- **Organ level**: Primary organ — uterus (myometrium). Secondary/complication-related involvement: bladder (compression → urinary symptoms), rectum/colon (compression → constipation), ureters (rare hydronephrosis with large broad-ligament fibroids), and — in HLRCC — kidney (renal cell carcinoma) and skin (cutaneous leiomyomas) as part of the syndromic phenotype. Body systems: reproductive, and secondarily urinary/GI (compression) and hematologic (anemia from HMB).
- **Anatomical/UBERON terms**: UBERON:0000995 (uterus), UBERON:0001296 (myometrium), UBERON:0000459 (endometrium), UBERON:0001255 (urinary bladder, secondary), UBERON:0002113 (kidney, HLRCC).
- **Tissue/cell level**: smooth muscle tissue (myometrium) is the tissue of origin; endometrium is secondarily affected functionally (bleeding) without itself being the tumor tissue. Cell Ontology: CL:0002598 (myometrial smooth muscle cell); tumor stroma additionally comprises fibroblast-like cells (CL:0000057) and endothelial cells (CL:0000115).
- **Subcellular level**: Mitochondria (TCA-cycle/fumarate handling in FH-deficient subtype; GO:0005739), nucleus (Mediator complex function; GO:0016592 mediator complex), extracellular matrix/extracellular space (GO:0031012).
- **Localization (FIGO anatomic classification — see §10)**: intracavitary (Type 0), submucosal (Types 1–2), intramural (Types 3–4), subserosal (Types 5–7), cervical or parasitic (Type 8), and hybrid transmural types. Lateralization is not a relevant axis (fibroids are typically multiple and distributed without lateral predilection), though location within the uterine body vs. cervix vs. broad ligament (parasitic) is clinically significant.

---

## 8. Temporal Development

- **Onset**: Reproductive age, typically detected from the mid-20s onward, with sharply rising incidence through the 30s–40s; incidence peaks around age 40–44 (5.0 cases/1000 person-years in the Australian cohort) and declines after menopause ([PMC11373412](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11373412/)). Congenital or prepubertal onset does not occur. HLRCC-associated leiomyomas present earlier (often in the 20s-30s) and more numerously.
- **Onset pattern**: Insidious — tumors grow slowly over years; most are identified incidentally or after gradual symptom accumulation rather than acute presentation (acute presentation occurs only with degeneration/torsion of a pedunculated fibroid).
- **Progression**: No formal "stage" system exists as for malignancy; the FIGO classification is anatomic/positional rather than a stage of progression. Disease course is typically **stable-to-slowly-progressive** during reproductive years, with **hormone-responsive acceleration during pregnancy** and **spontaneous regression after menopause** due to loss of ovarian estrogen/progesterone support. Course is generally not episodic/relapsing-remitting in the way autoimmune disease is, though symptom severity (particularly bleeding) can fluctuate with the menstrual cycle.
- **Remission**: Natural "remission" (shrinkage) occurs physiologically at menopause; treatment-induced regression occurs with GnRH agonists/antagonists and progesterone-receptor modulators (reversible, tumors typically regrow after cessation) or is permanent following surgical/procedural treatment.
- **Critical periods**: Reproductive years represent the principal window of clinical relevance (fertility impact, bleeding-related morbidity); pregnancy is a distinct high-risk window for both growth acceleration and degeneration/pain complications.

---

## 9. Inheritance and Population Genetics

**Epidemiology:**
- Reported incidence ranges from **217–3,745 cases per 100,000 woman-years**, and prevalence estimates range from **4.5%–68.6%**, reflecting wide variation by diagnostic method (clinical vs. systematic ultrasound screening) and population studied ([PMC12488583](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488583/); systematic review PubMed 28296146).
- Australian data-linkage cohort (2000–2022): **7.3%** cumulative diagnosis by ages 45–49; peak age-specific incidence **5.0/1000 person-years** at ages 40–44 ([PMC11373412](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11373412/)).
- Global Burden of Disease-based analyses (1990–2021/2023) document rising absolute case counts, with **further increases in both rate and total cases projected through 2050** ([PMC12488583](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488583/); [PMC13311307](https://pmc.ncbi.nlm.nih.gov/articles/PMC13311307/)).

**Inheritance pattern:** The common sporadic form is a **complex/multifactorial trait** — polygenic susceptibility (GWAS loci near HMGA2, TP53/ATM, TERT/TERC/OBFC1) combined with somatic driver mutation and environmental/hormonal exposure, not classically Mendelian. The syndromic minority form, **HLRCC (OMIM #150800)**, is **autosomal dominant**, caused by heterozygous germline pathogenic FH variants (>200 described mutations across the coding region), typically requiring a somatic "second hit" for tumor formation consistent with a classic two-hit tumor-suppressor mechanism ([OMIM #150800](https://www.omim.org/entry/150800); [PMC9128909](https://pmc.ncbi.nlm.nih.gov/articles/PMC9128909/)).
- **Penetrance**: high but incomplete for cutaneous/uterine leiomyomas in HLRCC; renal cell carcinoma penetrance is lower but the tumors that do occur tend to be aggressive.
- **Founder effects/consanguinity**: not prominently described for common UL; not specifically documented as a major factor for HLRCC beyond typical autosomal-dominant transmission.
- **Genetic anticipation, germline mosaicism**: not established features of this disease.

**Population demographics:**
- **Race/ethnicity**: Black women have markedly higher prevalence, earlier onset, and greater fibroid burden than White women (see §2b); genetic-ancestry studies estimate a substantial fraction of this disparity is attributable to differential frequency of fibroproliferative risk alleles by ancestry, alongside social/environmental contributors ([PMC8463481](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8463481/)).
- **Sex ratio**: Not applicable (uterus-specific, female-only disease).
- **Age distribution**: Concentrated in the 4th–5th decades of life, minimal before menarche or after several years post-menopause.
- **Geographic distribution**: Global disease, but burden estimates and rate-of-rise vary by region/country in GBD-based analyses ([Chinese Medical Journal, 2010–2019 worldwide database study](https://mednexus.org/doi/abs/10.1097/CM9.0000000000002971)).

---

## 10. Diagnostics

**Clinical tests:**
- **Imaging is the primary diagnostic modality.** Transvaginal (or transabdominal) **ultrasound** is first-line for detection and initial characterization; **MRI** provides superior multiplanar resolution and is preferred for surgical planning, especially with multiple/large fibroids, or to distinguish fibroids from adenomyosis or to assess for suspicious features ([PMC12553092](https://pmc.ncbi.nlm.nih.gov/articles/PMC12553092/); RadioGraphics 220161).
- **Saline-infusion sonohysterography or hysteroscopy** for submucosal (cavity-distorting) fibroids affecting fertility.
- **Laboratory**: CBC to assess for iron-deficiency anemia secondary to HMB (LOINC panels for hemoglobin/ferritin); no specific circulating biomarker is diagnostic for leiomyoma itself.
- **Biopsy/histopathology**: Not routinely needed preoperatively (fibroids are diagnosed radiologically); histology post-surgery shows whorled bundles of spindle smooth-muscle cells with abundant collagenous stroma; **FH-deficient tumors show characteristic eosinophilic cytoplasmic inclusions, prominent nucleoli with perinucleolar halos, and staghorn vasculature**, and immunohistochemistry for loss of FH protein / gain of 2SC (succinated cysteine) staining is used to screen for HLRCC ([Malacards HLRCC](https://www.malacards.org/card/hereditary_leiomyomatosis_and_renal_cell_cancer); PubMed 41808417).

**FIGO anatomic classification (Types 0–8):**
| Type | Description |
|---|---|
| 0 | Pedunculated intracavitary |
| 1 | Submucosal, <50% intramural |
| 2 | Submucosal, ≥50% intramural |
| 3 | Intramural, contacting endometrium |
| 4 | Intramural, not contacting endometrium or serosa |
| 5 | Subserosal, ≥50% intramural |
| 6 | Subserosal, <50% intramural |
| 7 | Subserosal, pedunculated |
| 8 | Cervical or other (parasitic) |
| Hybrid (e.g., "2-5") | Contacts both endometrium and serosa |

(Source: MRI-based pictorial reviews, [Springer 2020](https://link.springer.com/article/10.1007/s00261-020-02882-z), [PMC12553092](https://pmc.ncbi.nlm.nih.gov/articles/PMC12553092/)) — this classification is anatomical only and does not incorporate size, number, or vascularity.

**Genetic testing:** Not part of routine sporadic fibroid workup. Germline **FH gene sequencing** is indicated when HLRCC is clinically suspected (multiple/early-onset cutaneous leiomyomas, family history of early-onset aggressive renal cell carcinoma, or FH-deficient histology/IHC pattern on a resected uterine leiomyoma) — managed through cancer-genetics/GTR-listed panels.

**Differential diagnosis:** Adenomyosis, endometrial polyp, endometrial or uterine sarcoma (leiomyosarcoma), ovarian mass, pregnancy, adenomyoma. Distinguishing benign leiomyoma from **leiomyosarcoma preoperatively remains unreliable** — no imaging or biomarker test can definitively exclude sarcoma before histologic resection ([FDA leiomyosarcoma risk assessment](https://www.fda.gov/media/109018/download)).

**Screening:** No population-based screening program exists (unlike cervical/breast cancer screening); case-finding is via symptom-triggered pelvic exam/imaging. Cascade genetic counseling and screening for renal cell carcinoma risk is recommended for confirmed HLRCC-mutation carriers and their relatives.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Uterine leiomyoma itself is a **benign condition with essentially no direct mortality**; excess mortality risk relates only to rare complications (severe hemorrhage, surgical complications) or to the distinct entity of malignant transformation/leiomyosarcoma.

**Malignant transformation / leiomyosarcoma risk:** Leiomyosarcoma is a rare, biologically distinct uterine sarcoma, not simply an advanced fibroid. FDA's meta-analysis of 18 studies estimated the risk of occult uterine sarcoma among women undergoing surgery for presumed fibroids at **0.28%** ([FDA report](https://www.fda.gov/media/109018/download)). True malignant transformation of an existing benign leiomyoma (rather than de novo sarcomagenesis) is documented but considered rare; case reports describe secondary genetic events such as ALK rearrangement and 14q loss driving transformation to myxoid leiomyosarcoma ([Oncotarget 25137](https://www.oncotarget.com/article/25137/text/); [PMC6021249](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6021249/)). Because leiomyosarcoma cannot be reliably diagnosed preoperatively, **power morcellation carries a risk of intraperitoneal dissemination of an unsuspected sarcoma**, prompting the 2014 FDA warning against morcellation in most women undergoing myomectomy/hysterectomy for presumed fibroids and subsequent ACOG guidance (Committee Opinion 822) on patient counseling and containment techniques ([ACOG](https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2021/03/uterine-morcellation-for-presumed-leiomyomas)).

**Morbidity/functional impact:** Chronic heavy menstrual bleeding drives iron-deficiency anemia, fatigue, and substantial quality-of-life impairment; validated tools (UFS-QOL, SF-36, EQ-5D) show marked improvement with effective medical or surgical/procedural treatment.

**Reproductive/obstetric prognosis:** Fibroids — particularly cavity-distorting (submucosal) and large (≥9 cm) ones — are associated with **infertility and recurrent pregnancy loss**, and in pregnancy with increased risk of **cesarean delivery (aOR 1.57), breech presentation (1.64), malposition (1.59), preterm delivery (1.45), placenta previa (1.86), and severe postpartum hemorrhage (2.57)** ([meta-analysis, PMC11071265](https://pmc.ncbi.nlm.nih.gov/articles/PMC11071265/)). Fibroid size (not number) most strongly predicts breech presentation, postpartum hemorrhage, and placenta previa risk; fibroids ≥9 cm substantially raise antepartum/intrapartum/postpartum complication risk, sometimes prompting consideration of pre-conception myomectomy ([PMC10051105](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10051105/); PubMed 39957710). Premature rupture of membranes, chorioamnionitis, and endomyometritis are **not** significantly associated.

**Prognostic factors:** Fibroid size, number, and (most importantly for reproductive outcomes) FIGO location relative to the endometrial cavity are the principal prognostic determinants for both symptom severity and obstetric risk.

---

## 12. Treatment

Treatment is stratified by symptom severity, fertility desire, fibroid size/location, and patient preference; no single first-line therapy fits all patients.

**Pharmacotherapy:**
- **Tranexamic acid** and **NSAIDs** — symptomatic control of heavy menstrual bleeding without addressing tumor size (NCIT:C15986, Pharmacotherapy).
- **Combined oral contraceptives / progestin-only therapy / levonorgestrel-releasing IUS** — bleeding control; the LNG-IUS has been directly compared to ulipristal acetate in the UCON trial ([PMC10209678](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10209678/)).
- **GnRH agonists** (e.g., leuprolide) — induce hypoestrogenic state, shrink fibroids preoperatively; limited by menopausal side effects, generally short-term/preoperative use only.
- **Oral GnRH antagonists with hormonal add-back therapy** — a major recent therapeutic advance:
  - **Relugolix combination therapy** (relugolix 40 mg + estradiol 1 mg + norethindrone acetate 0.5 mg) — FDA-approved based on the **LIBERTY 1 and 2** Phase 3 trials (770 participants) showing significant reduction in heavy menstrual bleeding vs. placebo ([NEJM 2020, NEJMoa2008283](https://www.nejm.org/doi/full/10.1056/NEJMoa2008283)); LIBERTY EXTENSION assessed long-term efficacy/safety. A 2024 observational study also evaluated 3-month **preoperative** relugolix combination therapy for AUB associated with myomas.
  - **Elagolix combination therapy** — evaluated in the **Elaris** trials (791 participants); FDA-approved for fibroid-associated heavy bleeding.
  - **Linzagolix** — evaluated in the **PRIMROSE** trials (1,012 participants); notable for a lower-dose regimen usable without mandatory add-back therapy in some patients; approved in Europe ([PMC12327220](https://pmc.ncbi.nlm.nih.gov/articles/PMC12327220/)).
  - A 2024 clinical pharmacology review specifically addresses practical implementation considerations for these oral GnRH antagonists in fibroid management ([BJCP, bcp.15897](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/bcp.15897)).
- **Selective progesterone receptor modulators (SPRMs)** — **Ulipristal acetate** was highly effective for bleeding/size reduction but its EMA marketing authorization was suspended (initially in 2020, amid rare but serious drug-induced liver injury signals) and its use is now restricted to women who cannot undergo surgery/embolization or who have exhausted other options, with mandatory liver monitoring ([PubMed 40123751](https://pubmed.ncbi.nlm.nih.gov/40123751/); [PMC7686198, hepatotoxicity mechanism](https://pmc.ncbi.nlm.nih.gov/articles/PMC7686198/)). Mifepristone has also been studied for symptomatic/size reduction with a more favorable but less-established safety profile ([PMC11633070](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11633070/)).

**Interventional/surgical:**
- **Myomectomy** (hysteroscopic, laparoscopic, or open/abdominal) — fertility-sparing removal of fibroids; NCIT:C15329 (Surgical Procedure) with a more specific gynecologic-surgery term where available.
- **Hysterectomy** — definitive treatment for those who have completed childbearing; most common major gynecologic surgery performed for fibroids in the U.S.
- **Uterine artery embolization (UAE)** — interventional-radiology occlusion of the uterine arteries causing fibroid infarction; uterus-sparing, non-surgical alternative.
- **MRI-guided focused ultrasound surgery (MRgFUS/HIFU)** — noninvasive thermal ablation using focused ultrasound with real-time MRI thermal feedback. A 7-year follow-up study found a **33.1%** re-intervention rate over a median 6.1-year follow-up ([PMC12055703](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12055703/)); comparative literature indicates HIFU has shorter hospital stays and higher subsequent pregnancy rates than myomectomy/UAE but a higher re-intervention rate, with symptom/QOL improvement similar to myomectomy but somewhat lower than UAE ([PMC8836878](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8836878/); [PMC12081518](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12081518/)). Ongoing Phase III comparison to myomectomy (NCT03948789) and robotic-guided HIFU feasibility studies were active as of 2025.
- **Radiofrequency ablation** (laparoscopic or transcervical) — additional uterus-sparing option (not detailed in the searches above but standard in current practice guidelines).

**Precision/pharmacogenomic angle:** MED12 mutation status and CDK8 kinase-module activity have been shown to influence tumor growth trajectory and **response to GnRH agonist treatment**, suggesting a future genotype-informed treatment-selection paradigm ([PMC12773822](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12773822/)).

**Experimental/clinical trials:** Numerous registered trials on ClinicalTrials.gov for GnRH antagonist combination regimens, HIFU robotic systems, and SPRMs; representative NCT IDs include NCT03049735, NCT03103087, NCT03412890 (relugolix/LIBERTY program) and NCT03948789 (MRgFUS vs. myomectomy).

**Treatment outcomes/adverse events:** GnRH antagonist add-back regimens are generally well tolerated but require monitoring of bone mineral density with long-term use; ulipristal acetate's key adverse event of concern is rare but serious drug-induced liver injury; UAE carries risks of post-embolization syndrome and rare ovarian-reserve impact; myomectomy carries standard surgical risks plus fibroid recurrence risk; morcellation (laparoscopic or vaginal) carries the sarcoma-dissemination risk discussed in §11.

---

## 13. Prevention

- **Primary prevention**: No established primary prevention protocol exists for the general population; risk-factor modification (maintaining healthy body weight, considering hormonal contraception which has protective associations, and correcting vitamin D deficiency) is discussed in the literature as plausible but not yet incorporated into formal public-health guidelines ([PMC13167191](https://pmc.ncbi.nlm.nih.gov/articles/PMC13167191/) — vitamin D supplementation has clinical-trial evidence for reducing existing fibroid size/growth, e.g., NCT04030182, rather than pure primary prevention).
- **Secondary prevention/early detection**: No population screening program exists; early detection relies on symptom-triggered pelvic ultrasound. Given racial disparities, some equity-focused guidance advocates earlier/more proactive symptom evaluation in Black women given their higher risk and earlier onset.
- **Genetic counseling**: Recommended for suspected or confirmed HLRCC — genetic counseling and cascade testing of at-risk relatives given the autosomal-dominant inheritance and associated renal cell carcinoma risk; confirmed FH-mutation carriers undergo enhanced renal imaging surveillance protocols (per HLRCC-specific clinical management guidelines, [PMC9430984](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9430984/); [PMC11396326](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11396326/)).
- **Tertiary prevention**: Managing complications in established disease — anemia correction, pre-conception myomectomy for large/cavity-distorting fibroids to reduce obstetric complication risk, and vigilant surveillance/prompt evaluation of any rapidly enlarging mass to exclude sarcoma.
- **Prophylaxis**: Not applicable in the vaccine/antimicrobial sense; hormonal contraceptive use functions as a de facto risk-reducing intervention for those already using it for other indications.

---

## 14. Other Species / Natural Disease

- **Taxonomy**: Naturally occurring uterine leiomyoma is described in several domestic and companion species, though it is far less common than in humans; veterinary case reports exist in dogs, cats, and cattle (relevant NCBITaxon: 9615 Canis lupus familiaris, 9685 Felis catus, 9913 Bos taurus).
- **Comparative biology**: The Eker rat (a specific strain, not a naturally occurring outbred disease in the wild, but arising from a spontaneous germline Tsc2 mutation identified decades ago) represents the closest natural-genetic analog, spontaneously developing uterine leiomyoma alongside renal tumors due to loss of the Tsc2 tumor suppressor — orthologous to human TSC2 (chromosome 16p13.3), though TSC2 is not a major human sporadic UL driver, limiting direct translational relevance despite mechanistic utility ([ScienceDirect S0015028212024442](https://sciencedirect.com/science/article/pii/S0015028212024442)).
- **Zoonotic potential**: None; this is a non-infectious, hormonally-driven neoplastic process with no transmission risk.

---

## 15. Model Organisms

**In vivo genetic/spontaneous models:**
- **Eker rat**: The most widely used spontaneous animal model, carrying a germline mutation in the **Tsc2** tumor-suppressor gene, developing uterine leiomyoma (and leiomyosarcoma, renal tumors) with age; **ELT3 cells** (immortalized Eker-rat-derived leiomyoma cells) are a standard in vitro tool for mechanistic studies (e.g., the DES/vitamin D DNA-damage studies cited in §2b). However, because the driving mutation (Tsc2) does not correspond to the dominant human somatic drivers (MED12/HMGA2/FH), the model's translational fidelity to human sporadic UL is considered only **partial**, motivating alternative model development ([PMC12967960](https://pmc.ncbi.nlm.nih.gov/articles/PMC12967960/), preclinical platform review).

**Xenograft models:**
- **NOD/SCID and NSG immunodeficient mouse xenografts**: Human leiomyoma tissue or dissociated cells are implanted subcutaneously or under the kidney capsule of immunodeficient mice, often with supplemental estrogen/progesterone pellets to sustain hormone responsiveness and histological fidelity to the original tumor ([ScienceDirect S0015028214001022](https://www.sciencedirect.com/science/article/pii/S0015028214001022); [PMC5995841](https://pmc.ncbi.nlm.nih.gov/articles/PMC5995841/); Sci Rep s41598-018-27138-1). Kidney-capsule implantation in super-immunodeficient NSG mice is reported to better preserve native leiomyoma tissue characteristics than subcutaneous engraftment.
- **Patient-derived xenograft (PDX) models**: Used for predictive/preclinical drug-response studies, allowing direct testing of candidate therapeutics against patient-specific tumor genotypes ([PLOS ONE, journal.pone.0142429](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0142429)); PDX approaches have also specifically been applied to the **FH-deficient leiomyoma subtype** to study this molecular subclass in vivo (bioRxiv 2022.07.27.501688).

**Model characteristics/limitations:**
- Xenografts recapitulate hormone-responsive growth and gross/microscopic histology reasonably well but require an immunodeficient host, precluding study of immune-microenvironment contributions.
- The Eker rat captures spontaneous tumorigenesis and whole-organism biology (including gene-environment interactions) but is driven by a genetic lesion (Tsc2) not representative of the majority human molecular subtype.
- No single model currently captures the full genetic heterogeneity (MED12/HMGA2/FH subtypes) of human disease within one system; a 2024 "preclinical research platform" review explicitly frames current model selection as a construction/optimization problem requiring subtype-matched model choice depending on the research question ([PMC12967960](https://pmc.ncbi.nlm.nih.gov/articles/PMC12967960/)).

**Applications**: These models are used to study hormone-driven growth, test GnRH-antagonist/SPRM/novel small-molecule efficacy preclinically, and dissect ECM/TGF-β pathway biology and DNA-damage/vitamin-D mechanisms in a controlled genetic background.

---

## Suggested Ontology Term Summary

| Category | Term IDs |
|---|---|
| Disease/MONDO | MONDO:0007886 (uterine leiomyoma); MONDO term for HLRCC (syndromic) |
| OMIM | #150699 (sporadic UL); #150800 (HLRCC) |
| HPO (phenotypes) | HP:0000132 (Menorrhagia), HP:0030318 (Pelvic pain), HP:0100608 (Dysmenorrhea), HP:0030068 (Dyspareunia), HP:0001891 (Iron deficiency anemia), HP:0000789 (Infertility), HP:0005268 (Recurrent miscarriage) |
| Genes (HGNC) | MED12 (hgnc:29305), HMGA2 (hgnc:5013), FH (hgnc:3700), TP53, ATM, TERT, TERC |
| GO (biological process) | GO:0016055 (Wnt signaling pathway), GO:0007179 (TGF-β receptor signaling pathway), GO:0001525 (angiogenesis) |
| CL (cell types) | CL:0002598 (myometrial smooth muscle cell), CL:0000057 (fibroblast), CL:0000115 (endothelial cell) |
| UBERON (anatomy) | UBERON:0000995 (uterus), UBERON:0001296 (myometrium), UBERON:0000459 (endometrium) |
| CHEBI (chemicals) | fumarate, kynurenine (drug agents: ulipristal acetate, relugolix, elagolix, linzagolix, tranexamic acid) |
| NCIT (treatments) | NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure), NCIT:C15313 (Radiation Therapy, n/a here), device/ablation-specific terms for UAE/HIFU |

---

## Sources

- [Detection of exon2-MED12 mutations in uterine leiomyomas from Syrian patients (Sci Rep, 2024)](https://www.nature.com/articles/s41598-024-84439-4)
- [Genetic–Epigenetic Interactions in Uterine Leiomyomas: MED12 Mutations as Predictors of Aberrant DNA Methylation](https://pmc.ncbi.nlm.nih.gov/articles/PMC13512488/)
- [Variants in exon 2 of MED12 gene causes uterine leiomyoma's through over-expression of MMP-9 of ECM pathway](https://www.sciencedirect.com/science/article/abs/pii/S002751072300026X)
- [MED12 somatic mutation promotes human uterine leiomyoma's growth via Wnt4/β-catenin and TGF-β/EMT](https://www.sciencedirect.com/science/article/pii/S2949838425000325)
- [MED12 mutation activates the tryptophan/kynurenine/AHR pathway](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10561729/)
- [Impact of MED12 mutation and CDK8 activity on leiomyoma growth and GnRH agonist response](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12773822/)
- [Global and regional trends in incidence/prevalence of uterine fibroids 2010–2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556989/)
- [The epidemiology of uterine fibroids: global disease burden 1990–2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488583/)
- [Global Burden of PMS and Uterine Fibroids 1990–2023, projections to 2050](https://pmc.ncbi.nlm.nih.gov/articles/PMC13311307/)
- [First Australian estimates of incidence/prevalence of uterine fibroids 2000–2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11373412/)
- [Genetic predisposition to uterine leiomyoma (eLife, 2018)](https://elifesciences.org/articles/37110)
- [Panel Sequencing identifies Missense Mutations associated with FH-Loss](https://www.biorxiv.org/content/10.1101/663609v1.full)
- [Evaluation of GWAS candidate susceptibility loci — NIEHS uterine fibroid study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4501220/)
- [OMIM #150699 Leiomyoma, Uterine](https://www.omim.org/entry/150699)
- [Fine mapping of the uterine leiomyoma locus on 1q43 near RGS7-FH](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4526794/)
- [A Missense Mutation in FH Leads to HLRCC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10048203/)
- [Beyond VEGF and TGF-β: Growth Factor Pathways in Uterine Leiomyoma Pathophysiology](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12784659/)
- [Comprehensive Review of Uterine Fibroids (Endocrine Reviews, 2022)](https://academic.oup.com/edrv/article/43/4/678/6422392)
- [Role of TGF-β in Uterine Fibroid Biology](https://pubmed.ncbi.nlm.nih.gov/29149020/)
- [Update on Role of Extracellular Matrix in Uterine Fibroid Pathogenesis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10051203/)
- [Considerations on implementation of oral GnRH antagonists for fibroids](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/bcp.15897)
- [Linzagolix – new perspectives in uterine fibroids and endometriosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC12327220/)
- [Treatment of Uterine Fibroid Symptoms with Relugolix Combination Therapy (NEJM, 2020)](https://www.nejm.org/doi/full/10.1056/NEJMoa2008283)
- [Vitamin D and Uterine Fibroids: Pathophysiology and Therapeutic Potential](https://pmc.ncbi.nlm.nih.gov/articles/PMC13167191/)
- [Vitamin D3 Ameliorates DNA Damage from Endocrine Disruptors in Eker Rat Myometrial Stem Cells](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7349254/)
- [The Endocrine Disruption of Prenatal Phthalate Exposure](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7483495/)
- [Single Cell atlas of uterine myometrium and leiomyomas](https://www.biorxiv.org/content/10.1101/2020.12.21.402313v1.full)
- [Single-cell sequencing reveals novel cellular heterogeneity in uterine leiomyomas](https://pubmed.ncbi.nlm.nih.gov/36001050/)
- [OMIM #150800 HLRCC](https://www.omim.org/entry/150800)
- [Hereditary Leiomyomatosis and Renal Cell Cancer (PMC9128909)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9128909/)
- [HLRCC: Recognizing Patterns May Save Lives](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9430984/)
- [Long-term outcomes and re-intervention rates in MRgFUS for uterine fibroids: 7-year follow-up](https://pubmed.ncbi.nlm.nih.gov/39899259/)
- [Ultrasound-guided HIFU for symptomatic uterine fibroids: two European centers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12081518/)
- [Should HIFU Be Considered as Alternative Non-Surgical Treatment (opinion paper)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8836878/)
- [Nonobese diabetic/SCID murine xenograft model for uterine leiomyoma](https://www.sciencedirect.com/science/article/pii/S0015028214001022)
- [Establishment of a novel mouse xenograft model of human uterine leiomyoma](https://pmc.ncbi.nlm.nih.gov/articles/PMC5995841/)
- [Application of a PDX Model for Predictive Study of Uterine Fibroid Disease](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0142429)
- [Preclinical research platform for uterine leiomyoma: model selection](https://pmc.ncbi.nlm.nih.gov/articles/PMC12967960/)
- [Uterine Fibroids (Leiomyomata) and Heavy Menstrual Bleeding](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9580818/)
- [Presentation patterns and management outcomes of uterine fibroids](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12859363/)
- [FIGO classification MRI-based pictorial review](https://link.springer.com/article/10.1007/s00261-020-02882-z)
- [Diagnosis and classification of uterine fibroids](https://pmc.ncbi.nlm.nih.gov/articles/PMC12553092/)
- [Hepatic Safety Considerations in Ulipristal Acetate Use](https://pubmed.ncbi.nlm.nih.gov/40123751/)
- [Suspension of ulipristal acetate during EMA's liver injury review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7320679/)
- [Liver Injury with Ulipristal Acetate: Pharmacological Basis](https://pmc.ncbi.nlm.nih.gov/articles/PMC7686198/)
- [Malignant transformation of uterine leiomyoma to myxoid leiomyosarcoma after morcellation](https://pmc.ncbi.nlm.nih.gov/articles/PMC6021249/)
- [FDA Updated Assessment of Morcellation Risk](https://www.fda.gov/media/109018/download)
- [ACOG: Uterine Morcellation for Presumed Leiomyomas](https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2021/03/uterine-morcellation-for-presumed-leiomyomas)
- [Evidence that geographic variation in genetic ancestry associates with uterine fibroids](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8463481/)
- [Racial disparities in uterine fibroids and endometriosis: systematic review](https://www.sciencedirect.com/science/article/pii/S0015028223000602)
- [The fibroid crisis in Black women (AJOG)](https://www.ajog.org/article/S0002-9378(24)00739-7/fulltext)
- [The influence of uterine fibroids on adverse pregnancy outcomes: meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11071265/)
- [Association between leiomyoma characteristics and perinatal complications](https://pubmed.ncbi.nlm.nih.gov/39957710/)
- [Pregnancy With Uterine Fibroids: Obstetric Outcome at a Tertiary Care Hospital](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10051105/)
- [Oral contraceptive use and uterine leiomyoma risk: meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC10056617/)
- [The environmental risk factors related to uterine leiomyoma: umbrella review](https://www.sciencedirect.com/science/article/abs/pii/S2468784722001994)
- [Risk of uterine leiomyomata with menstrual/reproductive factors: Korea Nurses' Health Study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10257256/)
- [Genetic liability to multiple factors and uterine leiomyoma risk: Mendelian randomization](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10415162/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 49 |
| On topic | 29 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 21 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0030318` (2 mentions) - the report calls it "Pelvic pain"; HP calls it **Angular cheilitis**
- `HP:0030068` (2 mentions) - the report calls it "Dyspareunia"; HP calls it **Olfactory esthesioneuroblastoma**
- `HP:0031801` (1 mention) - the report calls it "Abdominal mass"; HP calls it **Vocal cord dysfunction**
- `UBERON:0000459` (2 mentions) - the report calls it "endometrium"; UBERON calls it **uterine wall**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0007886` (2 mentions) - the report calls it "uterine leiomyoma"; MONDO calls it **uterine corpus leiomyoma**, and lists "uterine leiomyoma" among its other names
- `HP:0100608` (2 mentions) - the report calls it "Dysmenorrhea"; HP calls it **Metrorrhagia**
- `HP:0005268` (2 mentions) - the report calls it "Recurrent miscarriage"; HP calls it **Miscarriage**
- `CL:0002598` (3 mentions) - the report calls it "myometrial smooth muscle cell"; CL calls it **bronchial smooth muscle cell**
- `UBERON:0001255` (1 mention) - the report calls it "urinary bladder, secondary"; UBERON calls it **urinary bladder**
- `UBERON:0002113` (1 mention) - the report calls it "kidney, HLRCC"; UBERON calls it **kidney**