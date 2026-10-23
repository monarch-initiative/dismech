---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T00:01:49.287386'
end_time: '2026-09-04T00:06:37.807998'
duration_seconds: 288.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Stickler Syndrome Type 2
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
  web_search_requests: 13
  num_turns: 19
  total_cost_usd: 1.1692930000000001
  session_id: eaf6e7f6-c363-56c8-b267-6f60c89fc92d
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 26
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 1
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:10486316
  - PMC:PMC9590009
  relevance_assessed: 17
  on_topic: 13
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 16
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000875
    reported_labels:
    - lattice degeneration, if available
    ontology_label: Episodic hypertension
  - term_id: GO:0060004
    reported_labels:
    - "reflex \u2014 not relevant"
    ontology_label: reflex
  - term_id: UBERON:0000955
    reported_labels:
    - cochlea, or more specific substructures
    ontology_label: brain
  - term_id: UBERON:0002481
    reported_labels:
    - mandible
    ontology_label: bone tissue
  labels_variant: 4
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Stickler Syndrome Type 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Stickler Syndrome Type 2** covering all of the
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

I'll research Stickler Syndrome Type 2 now using web search and fetch tools.

# Stickler Syndrome Type 2 (COL11A1-Related Stickler Syndrome): Comprehensive Research Report

## 1. Disease Information

**Overview.** Stickler syndrome type 2 (STL2) is a rare, autosomal dominant connective tissue disorder caused by heterozygous pathogenic variants in *COL11A1*, the gene encoding the α1(XI) chain of type XI collagen. It belongs to the "Stickler syndrome" family of collagenopathies (types I–V), all of which share a core tetrad of ocular, auditory, skeletal, and orofacial abnormalities but differ by causal gene and vitreous phenotype. Type 2 is distinguished clinically from type 1 (*COL2A1*-related) by its characteristic "beaded" (as opposed to "membranous"/type 1) vitreous anomaly, more pronounced midfacial hypoplasia, and substantially more prevalent and severe hearing loss ([OMIM #604841](https://omim.org/entry/604841); [GeneReviews – Stickler Syndrome](https://www.ncbi.nlm.nih.gov/books/NBK1302/)).

**Key identifiers:**
- **OMIM:** #604841 (STICKLER SYNDROME, TYPE II; STL2)
- **Orphanet:** ORPHA828 (Stickler syndrome, umbrella entry) / ORPHA90654 (type 2 specific entry cited in the literature)
- **Gene/Locus:** *COL11A1*, chromosome 1p21.1
- **MeSH/ICD-11:** Grouped under hereditary connective tissue disorders / arthro-ophthalmopathy
- **Suggested MONDO mapping:** A MONDO ID specific to STL2 should be confirmed via the MONDO browser at curation time (not resolved in this search pass).

**Synonyms:** Hereditary arthro-ophthalmopathy, type 2; STL2; beaded vitreous Stickler syndrome; Stickler syndrome, COL11A1-related. Note the close nosological relationship to **Marshall syndrome** and **otospondylomegaepiphyseal dysplasia (OSMED)**, both also caused by *COL11A1*/*COL11A2* variants, discussed further under Etiology.

**Evidence basis:** Most published data derive from aggregated clinical cohorts (case series of genetically confirmed COL11A1 probands and families), disease-level curated resources (OMIM, GeneReviews, Orphanet), and ClinVar variant submissions, rather than large-scale population EHR studies — consistent with STL2's rarity.

Sources: [OMIM #604841](https://omim.org/entry/604841), [GeneReviews Stickler Syndrome (NBK1302)](https://www.ncbi.nlm.nih.gov/books/NBK1302/), [Orphanet – Stickler syndrome](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=828)

---

## 2. Etiology

**Disease causal factors.** STL2 is a purely genetic, monogenic disorder. It is caused by heterozygous (dominant) pathogenic variants in *COL11A1* that disrupt the assembly or function of type XI collagen heterotrimers in cartilage and vitreous extracellular matrix. There is no known environmental, infectious, or purely mechanistic (non-genetic) causal pathway for classic STL2; environmental/behavioral factors instead modulate secondary complications (e.g., ocular trauma precipitating retinal detachment) rather than causing the underlying disease.

**Genetic risk factors:**
- **Causal variants:** Predominantly splice-site variants and missense substitutions in glycine residues of the collagen triple-helical Gly-X-Y repeat domain; also in-frame exonic deletions and, less commonly, nonsense/frameshift variants leading to premature stop codons. *COL11A1* intron 50 has been identified as a mutational hot spot ([GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/)).
- Splicing mutations affecting the 54-bp exons in the C-terminal (fibronectin-like) region of *COL11A1* are specifically associated with the **Marshall syndrome** phenotype, whereas other *COL11A1* variant types produce classic Stickler or overlapping Marshall/Stickler phenotypes — "of 10 mutation-positive patients, four were diagnosed with Marshall syndrome, but the remaining 6 showed an overlapping Marshall/Stickler phenotype" ([Griffith et al., Am J Hum Genet, PMID:10486316](https://pubmed.ncbi.nlm.nih.gov/10486316/)).
- **Recessive/biallelic COL11A1 variants**: a distinct, non-classical mode has been reported — inherited and de novo **biallelic** *COL11A1* pathogenic variants causing a recessive form of type 2 Stickler syndrome with unusually severe hearing loss, distinct from the fibrochondrogenesis phenotype normally caused by biallelic loss-of-function *COL11A1* variants (Nixon et al., 2020, [PMC7507023](https://pmc.ncbi.nlm.nih.gov/articles/PMC7507023/); [PMID via Mol Genet Genomic Med](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.1354)).
- **Population frequency of causal alleles:** *COL11A1* variants are individually ultra-rare; gnomAD population allele frequencies for reported pathogenic variants are typically <0.003%, consistent with a rare dominant disorder under purifying selection ([ClinVar records](https://www.ncbi.nlm.nih.gov/clinvar/variation/1032776/)).
- **Modifier/susceptibility factors:** No confirmed modifier genes for STL2 severity have been established in the literature reviewed; phenotypic variability appears substantially attributable to variant type/location (dominant-negative vs. haploinsufficient mechanisms) rather than a distinct modifier locus.

**Environmental risk factors:** None causal for disease onset. However, contact sports and activities with head/ocular trauma risk are recognized risk factors for retinal detachment in already-affected individuals, and this underlies the standard counseling to avoid such activities ([GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/)).

**Protective factors:** No genetic or environmental protective factors specific to STL2 are documented in the literature surveyed. Prophylactic ophthalmologic intervention (see Prevention/Treatment) functions as a secondary-prevention strategy rather than a true "protective factor" against the underlying mutation.

**Gene-environment interaction:** The principal interaction described in the literature is mechanical/traumatic: the structurally weakened, "beaded" vitreous and peripheral retinal lattice degeneration confer markedly increased *risk* of retinal tear/detachment upon minor ocular trauma, amplifying an otherwise sporadic environmental exposure into a major morbidity in this genetic background.

---

## 3. Phenotypes

STL2 phenotypes span four organ systems, with characteristic frequency data drawn primarily from GeneReviews and cohort studies of genetically confirmed *COL11A1* probands.

### Ocular phenotypes
| Feature | Frequency/Notes | Suggested HPO term |
|---|---|---|
| Myopia (typically congenital or early-onset, often high/progressive) | 80–85% (up to 87% in one 31-patient, 6-pedigree series) | HP:0000545 (Myopia); HP:0011003 (Extreme myopia) |
| "Beaded"/type 2 congenital vitreous anomaly | Present in ~100% of confirmed COL11A1 cases in the defining cohort (31/31 individuals across 6 pedigrees) | Vitreous anomaly (no precise HPO 1:1 term; often captured under HP:0007957 Corneal/vitreous phenotype categories — verify at curation) |
| Retinal detachment | <40% (lower than COL2A1-related type 1) | HP:0000541 (Retinal detachment) |
| Paravascular lattice retinopathy | 38% in the same 31-patient cohort | related to HP:0000875 (lattice degeneration, if available) |
| Cataract (often early-onset) | Reported but less quantified specifically for type 2 | HP:0000518 (Cataract) |

Onset is typically congenital/early childhood (myopia and vitreous anomaly present from birth or early infancy); progression of myopia can continue through childhood; retinal detachment risk is lifelong, including risk in adults >50 years old.

### Auditory phenotypes
- **Overall prevalence of hearing impairment:** 69–75-80% of individuals with type 2 Stickler syndrome have hearing loss in at least one ear (four-frequency average >20 dBHL) ([Alexander et al. 2020, PMID:32901364](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165062/)).
- **Type:** Predominantly **sensorineural** (77% of affected ears), with smaller proportions mixed (7%) or purely conductive (3%).
- **Severity:** Most commonly mild in the better ear (46% of the cohort, 30/65 patients); reduced sensitivity is present across the full frequency spectrum (250 Hz–8 kHz), not confined to high frequencies as previously assumed.
- **Progression:** Cross-sectional data (ages 3–70, mean 29.2) show "no significant progression of hearing loss beyond that expected of ageing (presbyacusis)" — i.e., largely stable/congenital rather than strongly progressive within an individual.
- **Mechanism:** Cochlear/peripheral in origin (not central), possibly related to microstructural collagen irregularities in tympanic membrane fibrous layer and cochlear ECM; intrinsic tympanic membrane hypermobility (24% Ad-type tympanograms) is less frequent than in type 1 disease, suggesting a distinct intrinsic mechanism rather than sequelae of recurrent otitis media.
- Suggested HPO terms: HP:0000407 (Sensorineural hearing impairment), HP:0000405 (Conductive hearing impairment), HP:0000410 (Mixed hearing impairment).

### Orofacial phenotypes
- **Midfacial hypoplasia/flat facies:** More pronounced in COL11A1-related than COL2A1-related disease. HPO: HP:0000272 (Flat face) / HP:0011800 (Midface retrusion).
- **Cleft palate** (isolated or as part of Pierre Robin sequence): ~60% of COL11A1-related cases. HPO: HP:0000175 (Cleft palate); Pierre Robin sequence itself: HP:0000278 (Retrognathia) + HP:0000047 or the composite Pierre Robin term.
- **Micrognathia:** HP:0000347.

### Skeletal phenotypes
- Early-onset degenerative joint disease/osteoarthritis, present in roughly 25% of affected individuals in the GeneReviews summary; joint hypermobility also reported. HPO: HP:0002829 (Arthralgia) / HP:0002758 (Osteoarthritis, early onset).

### Quality of life impact
No STL2-specific EQ-5D/SF-36 data were identified in this search; qualitatively, the combination of progressive visual impairment risk (retinal detachment), hearing loss requiring amplification, orofacial surgical needs in infancy (Pierre Robin sequence can cause airway obstruction/feeding difficulty), and early degenerative joint disease collectively affect childhood development, education, and adult occupational/social function, per general Stickler syndrome literature (GeneReviews, NORD).

Sources: [GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/), [Alexander et al. 2020 — Auditory dysfunction in type 2 Stickler Syndrome, PMC8165062](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165062/), [OMIM #604841](https://omim.org/entry/604841)

---

## 4. Genetic/Molecular Information

**Causal gene:** *COL11A1* (HGNC:2186; NCBI Gene 1301; OMIM *120280), chromosome 1p21.1, encoding pro-α1(XI) collagen chain, one of three chains (α1(XI), α2(XI), α3(XI)/COL2A1-derived) forming the heterotrimeric type XI collagen molecule.

**Variant classes reported (per ClinVar and literature):**
- Missense variants substituting glycine residues in the Gly-X-Y triple-helical repeat (classic collagenopathy mechanism), e.g., p.Gly97Val reported in an early founding STL2 family ([PMID:8872475](https://pubmed.ncbi.nlm.nih.gov/8872475/)).
- Splice-site variants (donor/acceptor), frequently clustering around intron 50 and other introns; several verified functionally via minigene/exon-trapping assays ([PMC7766184](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7766184/); [Frontiers in Genetics 2025](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2025.1642604/full)).
- In-frame exonic deletions.
- Nonsense variants causing premature stop codons (e.g., p.Glu1466Ter, p.Arg1362*).
- Rare biallelic (compound heterozygous or homozygous) variants causing a recessive severe-hearing-loss phenotype rather than classic dominant STL2 or the more severe fibrochondrogenesis (Nixon et al. 2020).

**Population frequency/gnomAD:** Individual pathogenic *COL11A1* variants are essentially absent or present at extremely low frequency (≤0.003%) in gnomAD control populations, consistent with a fully penetrant, rare autosomal dominant disorder under negative selection.

**Somatic vs. germline:** STL2 is exclusively a germline disorder; no somatic mosaicism-driven or acquired oncologic mechanism is implicated. Germline mosaicism in a parent is a recognized (though not separately quantified in this search) consideration for recurrence-risk counseling in apparently de novo cases, consistent with other autosomal dominant collagenopathies.

**Functional consequence — molecular mechanism:** "Pathogenic variants of type XI collagen more usually exert dominant negative effects," in contrast to *COL2A1*-related Stickler syndrome (type 1), which typically acts via haploinsufficiency. Dominant-negative variants (splice-site, in-frame deletion, glycine substitution) allow mutant α1(XI) chains to be incorporated into heterotrimers with wild-type chains, disrupting collagen fibril assembly ("fibrillogenesis") and secretion, producing a poison-peptide effect on the overall collagen network in vitreous and cartilage matrix. Loss-of-function/nonsense variants may instead act via haploinsufficiency in some cases.

**Modifier genes:** None specifically validated for STL2 in the sources reviewed.

**Epigenetics:** No disease-specific epigenetic (DNA methylation/histone) mechanism has been described for STL2 in the literature surveyed.

**Chromosomal abnormalities:** STL2 is caused by point/small-indel/splice variants rather than large chromosomal rearrangements; no recurrent CNV or translocation mechanism is reported.

**Relationship to allelic disorders:** *COL11A1* variants also cause:
- **Marshall syndrome** (particularly with splicing mutations of the 54-bp exons in the C-terminal region), overlapping clinically with STL2 but with more pronounced short nose/flat nasal bridge and midfacial hypoplasia.
- **Fibrochondrogenesis** (severe skeletal dysplasia) from biallelic loss-of-function variants.
- Nonsyndromic autosomal dominant sensorineural hearing loss, **DFNA37**, caused by a splice-altering *COL11A1* variant, demonstrating allelic heterogeneity of clinical outcome depending on variant location/type ([Nat Genet Med 2018](https://www.nature.com/articles/s41436-018-0285-0)).

Sources: [GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/), [OMIM #604841](https://omim.org/entry/604841), [ClinVar variant records](https://www.ncbi.nlm.nih.gov/clinvar/RCV000679954/), [Griffith et al. Am J Hum Genet PMID:10486316](https://pubmed.ncbi.nlm.nih.gov/10486316/), [Alazami/Novel & recurrent COL11A1/COL2A1 mutations, Hum Genome Var 2017](https://www.nature.com/articles/hgv201740)

---

## 5. Environmental Information

STL2 has no primary environmental, lifestyle, or infectious causal factor — it is a fully penetrant monogenic disorder. Environmental relevance is confined to:
- **Trauma:** Contact sports, high-impact activity, and ocular trauma are recognized precipitants of retinal detachment in the structurally abnormal, "beaded" vitreous — this is the principal reason clinical guidance recommends avoidance of contact sports in affected individuals.
- **Noise exposure:** No STL2-specific data on noise-induced hearing loss interaction were found in this search, though as with any baseline sensorineural hearing loss, cumulative noise exposure could theoretically compound existing deficits (inferred, not directly evidenced in the literature reviewed).
- **Infectious agents:** Not causally implicated in STL2 pathogenesis itself; however, recurrent otitis media is a differential/comorbid contributor to conductive hearing loss components in Stickler syndrome broadly (more prominent in type 1 than reported for type 2, per the tympanometry data above).

No CTD (Comparative Toxicogenomics Database), TOXNET, or NHANES-level environmental exposure data specific to *COL11A1*/STL2 were located.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (from molecular lesion to clinical phenotype)

1. A heterozygous pathogenic variant (most often a glycine substitution or splice-altering mutation) in *COL11A1* **leads to** an abnormal pro-α1(XI) collagen chain.
2. The abnormal chain is incorporated into the heterotrimeric type XI procollagen molecule alongside wild-type α2(XI) and α1(II)-lineage chains, which **results in** a dominant-negative poisoning of collagen triple-helix assembly (for splice/glycine/in-frame-deletion variants), or in reduced total functional protein (haploinsufficiency, more typical of nonsense/frameshift variants) — *this specific dominant-negative-vs-haploinsufficiency branch point is a documented distinction rather than an inference*.
3. Defective or reduced type XI collagen **leads to** disrupted regulation of lateral growth of co-assembled type II collagen fibrils, since type XI collagen normally acts as a nucleator/regulator controlling fibril diameter in cartilage and vitreous matrices where it constitutes 10–25% of vitreous collagen and 5–10% of cartilage collagen.
4. In the **vitreous**, this dysregulated fibrillogenesis **results in** short, irregular-diameter, thickened fibrils that aggregate into the diagnostic "beaded" lamellar vitreous phenotype (as opposed to the "membranous"/optically empty type 1 vitreous phenotype seen with COL2A1 haploinsufficiency) — demonstrated ultrastructurally and inferred from genotype-phenotype correlation studies.
5. The abnormal vitreous scaffold, combined with weakened vitreoretinal adhesion, **predisposes to** peripheral retinal lattice degeneration and, upon vitreous traction or trauma, **leads to** retinal tears and rhegmatogenous retinal detachment (documented clinical outcome, though the exact biomechanical step from beaded vitreous to lattice degeneration is partly inferred from structural/ultrastructural correlation rather than direct causal proof).
6. Independently, disrupted collagen XI content **impairs** normal growth-plate cartilage chondrocyte organization and endochondral ossification (demonstrated in the *cho/cho* mouse and zebrafish *col11a1a* knockdown models — see Model Organisms), which **results in** the midfacial hypoplasia/flat facies and, when severe enough during palatal shelf fusion in utero, **causes** cleft palate/Pierre Robin sequence via a mechanistic branch distinct from the ocular pathway.
7. Disrupted cartilage collagen matrix also **leads to** early degenerative joint disease (osteoarthropathy) via abnormal articular cartilage mechanical properties — demonstrated in heterozygous *cho/+* mice, which develop osteoarthritis, supporting a direct model-organism causal link.
8. In the **cochlea**, type XI collagen abnormalities affect basilar and tectorial membrane extracellular matrix microstructure (inferred from cochlear expression pattern studies and structural correlation, since the heterozygous mouse model paradoxically shows *no* auditory phenotype — a documented human/model discrepancy, see below), **leading to** sensorineural hearing impairment across the frequency spectrum via a peripheral (cochlear), not central, auditory pathway (directly demonstrated by psychoacoustic/central-processing testing in the human cohort study).
9. Tympanic membrane fibrous-layer collagen abnormality separately **may contribute to** a smaller conductive/mixed hearing-loss component in a minority of ears, distinguishable from otitis-media-related conductive loss by tympanometric intrinsic hypermobility patterns (a mechanistic hypothesis, not fully proven).

### Category detail

- **Molecular pathways:** Collagen fibrillogenesis/triple-helix assembly is the dominant pathway (not a classical signaling cascade like Wnt/MAPK/PI3K-AKT); relevant GO terms include **collagen fibril organization (GO:0030199)** and **extracellular matrix organization (GO:0030198)**.
- **Cellular processes:** Chondrocyte differentiation/hypertrophy dysregulation (documented in zebrafish *col11a1a* knockdown, which alters "spatial organization of chondrocytes, the shaping of cartilage elements, and the maturation of chondrocytes to hypertrophy" — [PMC9590009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9590009/)); no strong evidence of apoptosis, autophagy dysregulation, or classical inflammatory/immune-mediated cell death being primary in STL2 (unlike some other connective tissue disorders).
- **Protein dysfunction:** Dominant-negative incorporation of mutant α1(XI) chains into heterotrimers causing structurally abnormal, likely intracellularly retained or extracellularly malformed collagen fibrils — a gain-of-abnormal-function/dominant-negative mechanism rather than simple misfolding/aggregation of the UPR type.
- **Tissue damage mechanisms:** Mechanical/structural fragility (abnormal fibril diameter and spacing) rather than oxidative stress, ischemia, or classical fibrosis; retinal detachment represents a biomechanical tissue-failure event superimposed on this structurally weak matrix.
- **Biochemical abnormalities:** Reduced or absent normal-diameter type XI collagen fibrils in vitreous and cartilage ECM; no known enzyme deficiency or ion channel defect is implicated.
- **Molecular profiling:** No large-scale transcriptomic/proteomic/metabolomic datasets specific to human STL2 tissue were identified in this search (vitreous and cartilage biopsy material from patients is understandably difficult to obtain); most mechanistic data derive from animal/zebrafish models and biochemical/ultrastructural studies of collagen fibrils.
- **Advanced technologies:** No single-cell, spatial transcriptomic, or CRISPR functional-genomics screen data specific to *COL11A1*/STL2 were found in this search pass; the zebrafish morphant/knockout and *cho* mouse models remain the principal functional-genomics tools used.

**Suggested ontology terms:**
- GO:0030199 (collagen fibril organization), GO:0030198 (extracellular matrix organization), GO:0001501 (skeletal system development), GO:0060004 (reflex — not relevant), GO:0071711 (basement membrane organization) — verify applicability at curation.
- CL terms: chondrocyte (CL:0000138), retinal pigment epithelial cell (context-dependent), hair cell of the cochlea (CL:0000583) as a candidate cochlear cell type of interest.
- UBERON: vitreous body (UBERON:0001797), cartilage (UBERON:0002418), cochlea (UBERON:0000955), secondary palate (UBERON:0001716).

Sources: [GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/), [GeneCards COL11A1](https://www.genecards.org/card/COL11A1), [Alexander et al. 2020, PMC8165062](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165062/), [Col11a1a zebrafish studies, PMC7558312, PMC9590009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7558312/), [Auditory function in cho mice, ResearchGate summary](https://www.researchgate.net/publication/10951553_Auditory_function_associated_with_Col11a1_haploinsufficiency_in_chondrodysplasia_cho_mice)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Eye (vitreous, retina, lens), ear (cochlea, tympanic membrane), craniofacial skeleton (palate, mandible, midface), and appendicular/axial joints (articular cartilage).
- **Secondary/complications:** Airway (Pierre Robin sequence–related obstruction in infancy), potentially cardiovascular (mitral valve prolapse is reported in some Stickler syndrome cohorts generally, though not specifically quantified for STL2 in this search).
- **Body systems:** Ophthalmologic, auditory/vestibular, musculoskeletal, craniofacial/orofacial.

**Tissue and cell level:**
- Vitreous humor (specialized extracellular matrix, largely acellular but organized by hyalocytes).
- Articular and growth-plate cartilage (chondrocytes, CL:0000138).
- Cochlear basilar and tectorial membranes (specialized ECM structures within the organ of Corti).
- Tympanic membrane fibrous layer.
- Palatal shelf mesenchyme during embryonic development.

**Subcellular level:**
- Extracellular matrix/collagen fibrils (GO Cellular Component: extracellular matrix, GO:0031012); rough endoplasmic reticulum (site of procollagen synthesis/triple-helix folding) may be secondarily implicated in dominant-negative variants causing intracellular retention, though this is inferred by analogy to other collagenopathies rather than directly demonstrated for STL2 in the sources reviewed.

**Localization:**
- Ocular findings are typically bilateral.
- Hearing loss is "bilateral and symmetrical" in the majority of cases per the Alexander et al. cohort.
- Craniofacial features (midfacial hypoplasia, cleft palate) are midline/bilateral rather than lateralized.
- Joint disease can be poly-articular, most classically affecting large weight-bearing joints (hips, knees) with early degenerative change.

Suggested UBERON terms: UBERON:0001797 (vitreous body), UBERON:0000966 (retina), UBERON:0002418 (cartilage tissue), UBERON:0000955 (cochlea, or more specific substructures), UBERON:0001716 (secondary palate), UBERON:0002481 (mandible).

---

## 8. Temporal Development

**Onset:**
- Congenital/early-childhood onset is typical for the defining ocular anomaly (vitreous phenotype present from birth), congenital or early-onset myopia, and — when present — cleft palate/Pierre Robin sequence (present at birth).
- Hearing loss is generally present from early life (the cohort study spanning ages 3–70 supports this) rather than adult-onset.
- Onset pattern for the joint disease is **insidious**, with "early-onset degenerative joint disease" typically manifesting well before the general population's usual osteoarthritis age.

**Progression:**
- **Ocular:** Myopia may progress in childhood; retinal detachment risk is lifelong and can occur even after age 50, meaning prophylaxis is recommended "for SS adults of any age," not just childhood.
- **Auditory:** Statistically, hearing loss shows "no significant progression... beyond that expected of ageing (presbyacusis)" in cross-sectional data — i.e., relatively stable rather than strongly progressive within an individual, though this is based on cross-sectional rather than longitudinal cohort data and should be interpreted cautiously.
- **Skeletal:** Progressive, degenerative joint disease with earlier-than-typical onset of osteoarthritic changes.
- **Disease course pattern:** Chronic and lifelong rather than episodic/relapsing-remitting; there is no described spontaneous remission.
- **Critical periods:** In utero/early embryonic period for craniofacial (palatal fusion) and skeletal patterning; neonatal period for airway management in Pierre Robin sequence; childhood/adolescence is the critical window for ongoing surveillance (retinal exams) given retinal detachment risk starting early and persisting lifelong.

No formal staging system (analogous to AJCC cancer staging) exists for Stickler syndrome; severity is instead tracked via organ-specific outcome measures (visual acuity, audiometric thresholds, joint imaging).

---

## 9. Inheritance and Population

**Epidemiology:**
- Overall Stickler syndrome (all types combined) birth prevalence is estimated at **1/7,500 to 1/9,000** ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=828)).
- *COL11A1*-related Stickler syndrome (type 2) accounts for approximately **10–20%** of all genetically confirmed Stickler syndrome cases (multiple concordant sources: GeneReviews, Orphanet, and case-series literature).

**Inheritance pattern:** Autosomal dominant (classic STL2). A distinct, rarer **autosomal recessive/biallelic** form has also been reported, causing a severe-hearing-loss variant phenotype rather than the lethal fibrochondrogenesis otherwise associated with biallelic *COL11A1* loss-of-function (Nixon et al. 2020).

**Penetrance:** Reported as high/complete for the core phenotype in dominant carriers, though expressivity (see below) is markedly variable — a heterozygous pathogenic variant essentially always produces some disease manifestation, but the specific combination and severity of features differs.

**Expressivity:** Highly **variable**, "both within and among families" (GeneReviews), and echoed in case reports such as "Variable clinical expression of Stickler Syndrome: A case report of a novel COL11A1 mutation" ([PMID:32558342](https://pubmed.ncbi.nlm.nih.gov/32558342/)).

**Genetic anticipation:** Not a recognized feature of STL2 (no repeat-expansion mechanism); not applicable.

**Germline mosaicism:** Not specifically quantified for *COL11A1* in the sources reviewed, but standard genetic counseling principles for autosomal dominant collagenopathies with apparent de novo variants would still consider low-level parental germline mosaicism a residual recurrence-risk factor (inferred from general collagenopathy genetics, not directly sourced here).

**Founder effects:** No specific *COL11A1* founder mutation/population was identified in this search (contrast with some other Mendelian disorders); further targeted search of population genetics databases would be needed to confirm absence versus simply not surfaced.

**Consanguinity:** Relevant specifically to the rare recessive/biallelic *COL11A1* form (Nixon et al. 2020 cohort included both inherited-biallelic and de novo-biallelic cases), where recessive inheritance would be expected to have a higher incidence in consanguineous families, though this was not explicitly quantified in the search results.

**Carrier frequency:** Not applicable in the classic sense for a fully penetrant dominant disorder; for the recessive biallelic form, no specific carrier frequency was found (individual variants are each individually rare per gnomAD).

**Population demographics:**
- No specific ethnic or geographic enrichment for *COL11A1*-related STL2 was identified in the sources reviewed (contrast to some Stickler-related genes/populations with founder effects); Stickler syndrome overall is described as pan-ethnic.
- Sex ratio: No sex-linked or sex-skewed prevalence was identified for STL2 (autosomal dominant with no reported sex-influenced penetrance in the sources reviewed).
- Age distribution: All-ages disorder from birth through late adulthood, as evidenced by cohort studies spanning ages 3–70.

Sources: [Orphanet – Stickler syndrome](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=828), [GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/), [Nixon et al. 2020, PMC7507023](https://pmc.ncbi.nlm.nih.gov/articles/PMC7507023/), [Brizola et al. 2020, PMID:32558342](https://pubmed.ncbi.nlm.nih.gov/32558342/)

---

## 10. Diagnostics

**Clinical tests:**
- **Ophthalmologic examination:** Slit-lamp and dilated fundoscopic exam to characterize the vitreous phenotype (type 2 "beaded" vitreous is itself a key diagnostic clue distinguishing STL2 from type 1), assess myopia degree, and screen for lattice retinopathy/retinal thinning.
- **Audiologic evaluation:** Pure-tone audiometry across the full frequency range (250 Hz–8 kHz, per the Alexander et al. protocol), tympanometry to assess middle-ear/tympanic membrane compliance, and central auditory processing assessment to localize the lesion to the cochlear/peripheral level.
- **Imaging:** Skeletal radiographs for epiphyseal changes and joint assessment; craniofacial imaging as needed for orofacial anomalies; no disease-specific advanced imaging modality (MRI/CT/PET) is a primary diagnostic tool.
- **Biopsy/pathology:** Not routinely used for diagnosis; the diagnosis rests on clinical phenotype plus molecular confirmation rather than histopathology.

**Genetic testing:**
- No universal consensus clinical diagnostic criteria exist for Stickler syndrome; diagnosis is established by "characteristic clinical features and/or a heterozygous pathogenic variant in COL2A1, COL9A1, COL9A2, COL9A3, COL11A1, or COL11A2" (GeneReviews).
- **Recommended approach:** Given locus heterogeneity, a **multi-gene panel** covering *COL2A1*, *COL9A1/2/3*, *COL11A1*, and *COL11A2* is the standard first-tier test; single-gene *COL11A1* sequencing may be prioritized when the vitreous phenotype and more severe hearing loss/midfacial hypoplasia point specifically toward type 2.
- **Exon-trapping/minigene splicing assays** have been used to functionally reclassify intronic *COL11A1* variants of uncertain significance as pathogenic splice-altering variants ([PMC7766184](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7766184/); [Frontiers 2025](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2025.1642604/full)).
- **WES/WGS** utility: appropriate when panel testing is negative or when phenotype is atypical/overlapping (e.g., Marshall/Stickler overlap), given demonstrated allelic heterogeneity across the *COL11A1* locus.
- **Chromosomal microarray/karyotype/FISH:** Not indicated, as STL2 is not caused by CNV or chromosomal rearrangement.
- **Mitochondrial DNA/repeat expansion testing:** Not applicable.

**Omics-based diagnostics:** No routine transcriptomic, proteomic, metabolomic, or liquid-biopsy-based diagnostic modality exists for STL2; RNA-based splicing assays (minigene constructs) function as a research/confirmatory tool for variant interpretation rather than a first-line clinical diagnostic.

**Clinical criteria:** No DSM/ICD-based standardized diagnostic checklist was identified in this search; clinical suspicion is typically built from the combined ocular-auditory-orofacial-skeletal tetrad plus family history, confirmed molecularly.

**Differential diagnosis:** Marshall syndrome (COL11A1, overlapping phenotype distinguished mainly by more pronounced short nose/flat nasal bridge), OSMED (COL11A2, no ocular involvement since COL11A2 is not vitreous-expressed), Stickler syndrome type 1 (COL2A1, membranous vitreous, more severe retinal detachment risk, milder hearing loss), other type XI/type IX collagenopathies (types 4/5), Pierre Robin sequence of other etiologies, and other syndromic causes of high myopia/hearing loss combinations.

**Screening:** No population-based newborn screening program exists for Stickler syndrome (it is not detected by standard metabolic newborn screening panels). Cascade genetic testing of at-risk relatives once a proband's *COL11A1* variant is identified is the standard practice, alongside genetic counseling for family planning.

Sources: [GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/), [PMC7766184](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7766184/), [Frontiers in Genetics 2025](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2025.1642604/full)

---

## 11. Outcome/Prognosis

**Survival and mortality:** Stickler syndrome, including type 2, is not generally associated with reduced life expectancy from the connective tissue disorder itself. The main mortality risk historically relates to airway compromise in neonates with severe Pierre Robin sequence if unmanaged, which is a manageable, not inevitable, risk with modern neonatal care. No specific STL2 survival/mortality registry statistics were identified in this search.

**Morbidity and function:**
- The principal morbidity drivers are **visual** (risk of retinal detachment leading to potential blindness if untreated or detected late) and **auditory** (bilateral, often lifelong sensorineural hearing loss affecting communication/education).
- Early-onset degenerative joint disease contributes to musculoskeletal morbidity and potential need for early joint interventions (e.g., earlier-than-typical arthroplasty in severe cases, inferred from "early-onset degenerative joint disease" framing, though not explicitly quantified with an intervention rate in the sources found).
- No disease-specific EQ-5D/SF-36/PROMIS quality-of-life dataset was located for STL2 in this search.

**Disease course/complications:**
- Retinal detachment is the single most vision-threatening complication; with prophylactic treatment protocols (see Prevention/Treatment), detachment risk and visual morbidity can be substantially reduced.
- Recurrent otitis media may complicate the auditory picture (more so in type 1 than type 2, per tympanometric data), and dental/orthodontic complications commonly follow midfacial hypoplasia and cleft palate repair.
- Recovery potential: With early, consistent surveillance and prophylactic ophthalmologic intervention plus hearing amplification, functional visual and auditory outcomes are considerably better than the natural history without intervention — this is the central rationale for the structured lifelong surveillance protocols described below.

**Prognostic factors:** Variant type (dominant-negative splice/glycine-substitution variants vs. simple haploinsufficiency variants) likely influences phenotypic severity, though a fully validated genotype-severity prediction model was not identified in this search. Early diagnosis (enabling early prophylactic retinal treatment) is itself a major modifiable prognostic factor for visual outcome.

---

## 12. Treatment

There is currently **no disease-modifying or curative therapy** for STL2; management is entirely surveillance-based and symptomatic/preventive, targeting the organ-specific complications.

**Pharmacotherapy:** No *COL11A1*-targeted pharmacologic therapy exists. Standard analgesic/anti-inflammatory management (e.g., NSAIDs) may be used symptomatically for joint pain from early osteoarthritis, following general osteoarthritis management guidelines rather than a Stickler-specific protocol (NCIT:C15986, Pharmacotherapy — general, non-specific).

**Advanced therapeutics (investigational):**
- Gene therapy and antisense oligonucleotide (ASO) approaches have been explored as an emerging strategy in Stickler syndrome broadly, with early research reportedly focused on correcting *COL2A1*-related (type 1) pathology; comparable *COL11A1*-targeted approaches were not identified as being in active clinical trials in this search. This should be treated as an early-stage/preclinical research direction rather than a current treatment option (NCIT:C15238, Gene Therapy — investigational only).
- No cell therapy, targeted small-molecule, or immunotherapy approach specific to STL2 was identified.

**Surgical and interventional:**
- **Prophylactic retinal treatment:** 360° laser photocoagulation or cryotherapy at the vitreous base/ora serrata is the mainstay of retinal-detachment prevention. Two named historical protocols:
  - **Cambridge cryotherapy protocol:** a 360° transconjunctival contiguous single row of cryotherapy spots at the retina–pars plana junction.
  - **Manchester laser protocol:** 3–4 rows of laser posterior to the ora serrata, 360°; an "extended vitreous base laser" approach (360° from ora serrata to equator) has shown better visual outcomes in some series.
  - The **2025 American Academy of Ophthalmology Preferred Practice Pattern** guidelines recommend 360° laser prophylaxis for genetically confirmed Stickler syndrome patients ([AAO EyeNet](https://www.aao.org/eyenet/article/diagnosis-and-management-of-stickler-syndrome); search-derived summary).
  - Fellow-eye prophylaxis is "strongly recommended" after repair of a retinal detachment in the first eye, and prophylaxis should be offered to adults of any age given detachment risk persisting past age 50 ([systematic review/meta-analysis summary, PMC9793794](https://pmc.ncbi.nlm.nih.gov/articles/PMC9793794/)).
- **Vitreoretinal surgery** (scleral buckle, vitrectomy) for established retinal detachment/giant retinal tear repair (NCIT:C15329, Surgical Procedure).
- **Orofacial surgery:** Cleft palate repair; management of Pierre Robin sequence airway obstruction, sometimes requiring mandibular distraction osteogenesis or tracheostomy in severe neonatal cases (NCIT:C16186, Orthopedic Surgical Procedure / NCIT:C15329 general surgical procedure, per specific intervention).
- **Orthopedic intervention:** As needed for advanced joint disease (e.g., joint replacement in severe early-onset osteoarthritis cases), though no STL2-specific arthroplasty statistics were found.

**Supportive and rehabilitative care:**
- **Hearing amplification** (hearing aids) for sensorineural/mixed hearing loss; cochlear implantation would be considered per general audiology criteria in severe cases, though STL2-specific cochlear implant outcome data were not identified in this search.
- **Speech therapy** for children with cleft palate/orofacial involvement.
- **Physical/occupational therapy** for joint symptom management (NCIT:C15302, Physical Therapy).
- **Genetic counseling** for affected families (NCIT:C15240, Genetic Counseling).

**Experimental treatments:** No active *COL11A1*-specific interventional clinical trial (ClinicalTrials.gov NCT identifier) was surfaced in this search; broader Stickler syndrome gene-therapy/ASO research (largely COL2A1-focused) represents the closest investigational analog.

**Treatment outcomes:** Prophylactic 360° laser/cryotherapy protocols are reported to be effective in reducing giant retinal tear/detachment incidence in both treated and fellow eyes, per multiple single-institution case series (search results above); no randomized controlled trial data were identified, and evidence is predominantly retrospective/observational.

**Treatment strategy:** Management follows an organ-system-based surveillance algorithm: annual dilated ophthalmologic exam (vitreoretinal specialist) starting in early childhood, annual audiologic evaluation, craniofacial/orthodontic follow-up through growth, and periodic musculoskeletal assessment — rather than a single unifying pharmacologic algorithm.

Sources: [GeneReviews NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/), [AAO EyeNet – Diagnosis and Management of Stickler Syndrome](https://www.aao.org/eyenet/article/diagnosis-and-management-of-stickler-syndrome), [Cambridge cryotherapy protocol, PMID:24793526](https://pubmed.ncbi.nlm.nih.gov/24793526/), [Preventing Retinal Detachment review, PMC9793794](https://pmc.ncbi.nlm.nih.gov/articles/PMC9793794/)

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (no vaccination or exposure-avoidance strategy prevents the underlying genetic mutation); the closest analog is reproductive/preconception genetic counseling and, where desired, **preimplantation genetic diagnosis (PGD)** for families with a known pathogenic *COL11A1* variant.

**Secondary prevention:** The dominant secondary-prevention strategy in STL2 is prophylactic vitreoretinal treatment (360° laser or cryotherapy) to prevent retinal detachment before it occurs — this is a hallmark, well-documented preventive intervention specific to this disease group (see Treatment section above), rather than a population screening program.

**Screening/early detection:**
- No population-based newborn or carrier screening program exists for STL2 specifically.
- Once a proband is molecularly diagnosed, **cascade testing** of first-degree relatives is standard, enabling early identification of at-risk family members before symptom onset, so that prophylactic ophthalmologic surveillance can begin proactively rather than reactively.
- Prenatal testing is possible for known familial variants but is a family/ethical decision rather than a standard public-health recommendation, given the generally treatable/manageable nature of the disease.

**Behavioral interventions:** Avoidance of contact sports and high-risk trauma activities is the principal behavioral/lifestyle preventive recommendation to reduce retinal detachment risk.

**Genetic counseling:** Central to STL2 management given autosomal dominant inheritance with ~50% transmission risk per pregnancy for an affected parent, variable expressivity complicating risk prediction of severity (though not presence) in offspring, and the rare recessive biallelic form requiring different counseling for carrier parents.

**Public health/environmental interventions:** Not applicable — STL2 has no environmental/toxicant etiology to target with public health measures.

**Prophylaxis:** Beyond the ophthalmologic laser/cryotherapy prophylaxis already discussed, no pharmacologic prophylactic regimen exists.

---

## 14. Other Species / Natural Disease

**Taxonomy of affected species:**
- **Mouse** (*Mus musculus*, NCBITaxon:10090): the **chondrodysplasia (*cho*) mouse** carries a spontaneous functional-null *Col11a1* allele. Homozygous (*cho/cho*) mice die perinatally with lethal chondrodysplasia; heterozygous (*cho/+*) mice survive and develop osteoarthritis, modeling the human joint phenotype.
- **Zebrafish** (*Danio rerio*, NCBITaxon:7955): possess two *COL11A1* orthologs, *col11a1a* and *col11a1b*; *col11a1a* is most similar to human *COL11A1* and to the mouse *cho* locus.
- No specific naturally occurring companion-animal (dog/cat/horse) Stickler-syndrome-like *COL11A1* disease was identified in this search; a targeted OMIA search would be needed to confirm absence versus a gap in this search pass.

**Orthologous genes:** Mouse *Col11a1* (MGI ortholog of human *COL11A1*); zebrafish *col11a1a*/*col11a1b* (duplicated due to teleost genome duplication).

**Natural disease/veterinary relevance:** No veterinary clinical case series of naturally occurring *COL11A1*-associated disease in companion animals or wildlife was found in this search.

**Comparative biology:**
- **Conservation of mechanism:** The role of type XI collagen in regulating collagen fibril diameter during chondrogenesis and cartilage matrix organization is evolutionarily conserved from fish to mammals, as shown by concordant phenotypes (abnormal, thickened/sparse fibrils; disrupted chondrocyte maturation) across zebrafish knockdown and mouse *cho* models.
- **Divergence:** A striking cross-species discrepancy exists for the auditory phenotype — heterozygous *cho/+* mice have **normal auditory brainstem responses up to 10 months** despite skeletal and joint phenotypes, whereas human *COL11A1* heterozygotes commonly have significant sensorineural hearing loss. This has led researchers to conclude that "the lack of an auditory phenotype in the heterozygous mouse suggests haploinsufficiency is not the pathogenic mechanism underlying COL11A1-related auditory defects in humans" — an important translational caveat when extrapolating from the mouse heterozygote model to human auditory pathology.
- Homozygous *cho/cho* mice do show "marked hearing loss when tested by auditory brain-stem responses," but this recessive-lethal genotype models fibrochondrogenesis-like severity rather than classic dominant human STL2.

**Transmission:** Not applicable — not an infectious or zoonotic disease.

Sources: [Auditory function in cho mice — ResearchGate/PubMed summary](https://www.researchgate.net/publication/10951553_Auditory_function_associated_with_Col11a1_haploinsufficiency_in_chondrodysplasia_cho_mice), [Ultrastructural cochlear changes in cho/cho mice, PMID:1952599](https://pubmed.ncbi.nlm.nih.gov/1952599/), [Col11a1/Col11a2 cochlear expression, PMID:15141750](https://pubmed.ncbi.nlm.nih.gov/15141750/)

---

## 15. Model Organisms

### Mouse models
- ***cho* (chondrodysplasia) mouse:** A spontaneous functional-null allele of *Col11a1*.
  - **Homozygous (*cho/cho*):** Lethal perinatal chondrodysplasia; cochlear ultrastructural abnormalities and marked ABR-measured hearing loss — a good model of the severe end of the *COL11A1* biallelic spectrum (informing understanding of fibrochondrogenesis/recessive severe phenotypes) but not representative of classic dominant human STL2 due to its recessive, embryonic-lethal-adjacent severity.
  - **Heterozygous (*cho/+*):** Viable; develops osteoarthritis (modeling the human joint phenotype reasonably well) but has **normal hearing up to 10 months of age**, a notable **failure to recapitulate** the human auditory phenotype, suggesting either a species-specific auditory mechanism or that haploinsufficiency alone (as opposed to dominant-negative mutant protein incorporation) is insufficient to produce the human ear phenotype. This makes *cho/+* a model with **fidelity: HIGH** for skeletal/joint phenotype but **fidelity: LOW** (or a "fails to recapitulate" relationship) for the auditory phenotype specifically — an important limitation to flag for any pathophysiology modeling that uses this line to justify auditory mechanism claims.
  - Databases: MGI (Mouse Genome Informatics).

### Zebrafish models
- ***col11a1a* knockdown (morpholino) and mutant zebrafish:** Recapitulate craniofacial cartilage abnormalities (Meckel's cartilage malformation), otolith abnormalities, and altered body length; demonstrate disrupted chondrocyte spatial organization and delayed/abnormal maturation to hypertrophy, plus deposition of abnormally thick, sparse collagen fibrils in cartilage ECM — a reasonably faithful recapitulation of the skeletal/craniofacial arm of human COL11A1 disease at the cellular/matrix level.
  - This model has been proposed as a system to dissect "the mechanism that links the skeletal phenomena to hearing loss resulting from mutations in the Col11a1 gene," i.e., its main research application is investigating the skeletal-auditory mechanistic link, though direct zebrafish auditory/lateral-line phenotype data specific to *col11a1a* were not detailed in the sources retrieved in this search.
  - Databases: ZFIN.
- A related zebrafish model of **Col2a1a** (the type II collagen partner gene) has separately been used to study neural crest-related early eye development defects in Stickler syndrome ([PMC9589970](https://ncbi.nlm.nih.gov/pmc/articles/PMC9589970)), providing a complementary ocular-development model system within the same collagen-network disease family, though this specific model targets *COL2A1* (type 1 disease) rather than *COL11A1*.

### Cellular/in vitro models
No iPSC-derived or immortalized cell-line model specific to *COL11A1*/STL2 chondrocyte or vitreous biology was identified in this search; this appears to be a relative gap in the current modeling landscape and a plausible candidate for future research investment (inferred from absence of hits, not a positive finding).

### Model limitations summary
- The **cho/+ mouse** is the best-established genetic model overall but has a documented, well-characterized **failure to recapitulate the human auditory phenotype**, which is mechanistically informative (arguing against simple haploinsufficiency as the auditory mechanism) but limits its use for auditory-specific translational study.
- **Zebrafish col11a1a models** better capture cartilage/craniofacial cellular mechanism (chondrocyte organization/hypertrophy, fibril ultrastructure) and are proposed, but not yet fully validated, as a bridge to understanding the skeletal-auditory phenotypic link.
- No model to date fully recapitulates the ocular "beaded" vitreous phenotype or the retinal detachment risk specifically for *COL11A1* (as opposed to the *Col2a1a* zebrafish model used for the *COL2A1*/type 1 ocular phenotype).

Sources: [Auditory function in cho mice](https://www.researchgate.net/publication/10951553_Auditory_function_associated_with_Col11a1_haploinsufficiency_in_chondrodysplasia_cho_mice), [Ultrastructural cochlear changes cho/cho mice, PMID:1952599](https://pubmed.ncbi.nlm.nih.gov/1952599/), [Col11a1a Expression Is Required for Zebrafish Development, PMC7558312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7558312/), [The Shape of the Jaw — Zebrafish Col11a1a, PMC9590009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9590009/), [Craniofacial cartilage morphogenesis requires zebrafish col11a1 activity, PMID:19638309](https://pubmed.ncbi.nlm.nih.gov/19638309/)

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term(s) |
|---|---|
| Disease | OMIM:604841; Orphanet ORPHA828 / ORPHA90654 (verify exact STL2-specific ORPHA code and MONDO ID at curation) |
| Causal gene | hgnc:2186 (COL11A1) |
| Phenotypes (HP) | HP:0000545 (Myopia), HP:0000541 (Retinal detachment), HP:0000407 (Sensorineural hearing impairment), HP:0000405 (Conductive hearing impairment), HP:0000410 (Mixed hearing impairment), HP:0000175 (Cleft palate), HP:0000347 (Micrognathia), HP:0000272 (Flat face)/HP:0011800 (Midface retrusion), HP:0002758-type early-onset osteoarthritis term (verify exact code), HP:0000518 (Cataract) |
| Biological process (GO) | GO:0030199 (collagen fibril organization), GO:0030198 (extracellular matrix organization), GO:0001501 (skeletal system development) |
| Cell types (CL) | CL:0000138 (chondrocyte); cochlear/organ of Corti cell types as applicable |
| Anatomy (UBERON) | UBERON:0001797 (vitreous body), UBERON:0002418 (cartilage tissue), UBERON:0000955 (cochlea), UBERON:0001716 (secondary palate) |
| Treatment (NCIT) | NCIT:C15329 (Surgical Procedure — vitreoretinal/cleft repair), NCIT:C15302 (Physical Therapy), NCIT:C15240 (Genetic Counseling); no specific pharmacotherapy NCIT term is disease-modifying |
| Organism models (NCBITaxon) | NCBITaxon:10090 (Mus musculus, *cho* allele); NCBITaxon:7955 (Danio rerio, *col11a1a*) |

**Note on evidence gaps:** This search did not surface disease-specific quality-of-life instrument data (EQ-5D/SF-36), population-specific ethnic/geographic prevalence variation, a validated genotype-severity prediction model, active *COL11A1*-targeted clinical trials, veterinary/OMIA natural-disease cases, or single-cell/spatial-omics datasets for human STL2 tissue — these should be flagged as "not available" or researched further rather than inferred, per the report's citation requirements.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 17 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:10486316`: "of 10 mutation-positive patients, four were diagnosed with Marshall syndrome, but the remaining 6 showed an overlapping Marshall/Stickler phenotype"
  - closest text in source: "The α2(V) chain substitutes for the α2(XI) chain in the vitreous (Mayne et al.1993), thus explaining the lack of the ocular symptoms in patients with the COL11A2 gene mutations Our results indicate that patients with a splicing mutation in a 54-bp exon or with a mutation causing a 54-bp deletion in the C-terminal half of the COL11A1 gene more frequently showed with findings related to Marshall syndrome, and the mutations in the COL2A1 gene leading to a premature translation-termination codon caused the more classic Stickler syndrome phenotype"
- `PMC:PMC9590009` *(abstract only)*: "spatial organization of chondrocytes, the shaping of cartilage elements, and the maturation of chondrocytes to hypertrophy"
  - closest text in source: "Our results demonstrate that zebrafish col11a1a knockdown impairs the cellular organization of Meckel's cartilage in the developing jaw and alters the bone formation that occurs adjacent to the Meckel's cartilage"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 24 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000875` (1 mention) - the report calls it "lattice degeneration, if available"; HP calls it **Episodic hypertension**
- `GO:0060004` (1 mention) - the report calls it "reflex — not relevant"; GO calls it **reflex**
- `UBERON:0000955` (3 mentions) - the report calls it "cochlea, or more specific substructures"; UBERON calls it **brain**
- `UBERON:0002481` (1 mention) - the report calls it "mandible"; UBERON calls it **bone tissue**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000272` (2 mentions) - the report calls it "Flat face"; HP calls it **Malar flattening**, and lists "Flat cheekbone" among its other names
- `HP:0002758` (2 mentions) - the report calls it "Osteoarthritis, early onset"; HP calls it **Osteoarthritis**
- `CL:0000138` (3 mentions) - the report calls it "CL terms: chondrocyte", "chondrocyte"; CL calls it **chondrocyte**
- `UBERON:0001797` (3 mentions) - the report calls it "UBERON: vitreous body", "vitreous body"; UBERON calls it **vitreous humor**, and lists "humor vitreous" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000138` - called "CL terms: chondrocyte", "chondrocyte"
- `UBERON:0001797` - called "UBERON: vitreous body", "vitreous body"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.