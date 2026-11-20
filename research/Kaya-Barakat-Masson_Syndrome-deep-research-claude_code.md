---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-11-03T02:42:40.893687'
end_time: '2026-11-03T02:43:43.498343'
duration_seconds: 62.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Kaya-Barakat-Masson Syndrome
  mondo_id: MONDO:0030878
  category: Mendelian
  causal_genes: YIF1B
  omim_id: OMIM:619125
  synonyms: KABAMAS
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
  num_turns: 8
  total_cost_usd: 0.8759125999999998
  session_id: 12ee386d-0540-4b57-ab7e-db306eb6e9b5
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 6
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.5.1
term_validation:
  total_terms: 25
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0030878
    reported_labels:
    - taken from the task, not checked
    ontology_label: Kaya-Barakat-Masson syndrome
  - term_id: HP:0001332
    reported_labels:
    - A mixed movement disorder including dystonia
    ontology_label: Dystonia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kaya-Barakat-Masson Syndrome
- **MONDO ID:** MONDO:0030878 (if available)
- **Causal gene(s):** YIF1B
- **OMIM:** OMIM:619125
- **Synonyms:** KABAMAS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Kaya-Barakat-Masson Syndrome** covering all of the
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

# Kaya-Barakat-Masson Syndrome (KABAMAS, YIF1B-related neurodevelopmental disorder): research report

**Scope and limits.** This report rests on a few web searches. Page fetches (OMIM, GeneReviews) were blocked by the proxy, so I worked from search-result summaries only. The GeneReviews chapter's management and MRI sections were not retrieved. Every claim below is traceable to a source I saw. I did not verify exact abstract quotes, so none are given as snippets. Items marked **[unverified]** need checking before they go into a KB entry.

## 1. Disease information

KABAMAS is a rare autosomal recessive neurodevelopmental disorder caused by biallelic loss-of-function variants in **YIF1B** (YIP1-interacting factor homolog B, a membrane-trafficking protein). The gene is OMIM *619109. It encodes a protein that supports ER-to-membrane transport and is linked to Golgi morphology.

| Item | Value |
|---|---|
| Disease | KABAMAS, OMIM #619125 ([OMIM](https://omim.org/entry/619125)) |
| MONDO | MONDO:0030878 (taken from the task, not checked) |
| Gene | YIF1B (OMIM *619109) |
| Inheritance | Autosomal recessive |
| GeneReviews | "YIF1B-Related Neurodevelopmental Disorder", Medico-Salsench, Kaya, Barakat, 2024 ([NBK606999](https://www.ncbi.nlm.nih.gov/books/NBK606999/)) |
| Synonyms | KABAMAS; YIF1B-related brain disorder; YIF1B-related neurodevelopmental disorder |

The data are patient-level case reports and cohorts, aggregated in OMIM and GeneReviews.

## 2. Etiology

- **Cause:** homozygous or compound heterozygous pathogenic variants in YIF1B.
- **Case count:** OMIM reports 24 cases from 19 families. GeneReviews reports 24 of 25 individuals with biallelic variants found by exome sequencing.
- **Risk factors:** none beyond genotype are known. I found no environmental, protective or gene-environment data.
- **Modifier genes:** none reported.
- **Consanguinity:** I did not retrieve this directly. It is likely common, as in most autosomal recessive neurodevelopmental cohorts, but I have no source for it **[unverified]**.

## 3. Phenotypes

Sources: [Medico Salsench 2021, PMID:34373908](https://pubmed.ncbi.nlm.nih.gov/34373908/); [GeneReviews NBK606999](https://www.ncbi.nlm.nih.gov/books/NBK606999/). I did not retrieve per-feature frequencies, so none are given.

Core features are a progressive encephalopathy with:
- Severe-to-profound global developmental delay and intellectual disability: HP:0001263, HP:0010864
- Epilepsy: HP:0001250
- Microcephaly, present in some patients: HP:0000252
- A mixed movement disorder including dystonia (HP:0001332), with hypotonia (HP:0001252) and motor delay
- Dysphagia (HP:0002015)

Imaging features reported through MedGen/GeneReviews are corpus callosum hypoplasia (HP:0002079) and cerebellar atrophy (HP:0001272). I did not see the full MRI description **[unverified details]**.

- **Onset:** infancy or early childhood.
- **Course:** progressive encephalopathy, per the original report title.
- **Mortality:** OMIM notes some patients die in infancy or early childhood.
- **Genotype-phenotype:** biallelic truncating variants tend to give a more severe phenotype than biallelic missense variants, possibly because of residual YIF1B activity (GeneReviews, via search summary).
- **Quality-of-life data:** none found.

## 4. Genetic and molecular information

- **Variant spectrum (OMIM):** 18 of 24 cases (75%) carry truncating variants or a whole-gene deletion. 6 (25%) carry missense variants.
- **Missense variants:** all lie in or near the transmembrane domains. They are absent from gnomAD, apart from one seen once as a heterozygote.
- **Recurrent variants:** p.Ala63fs is found in 5 independent families. p.Glu200* is found in 3.
- **Other variants:**
  - Homozygous whole-gene deletion including the promoter and exons 1–7 (Medico Salsench 2021).
  - Splice variant c.297+1G>A ([Sanri et al. 2023, PMID:36948290](https://pubmed.ncbi.nlm.nih.gov/36948290/)).
  - A 2026 frameshift, c.440_441delinsA (p.Ala147Aspfs*51), in J Child Neurol ([DOI:10.1177/08830738261474029](https://doi.org/10.1177/08830738261474029)). The details came from an incomplete search snippet, so verify them.
- **Testing yield (GeneReviews):** sequence analysis accounts for about 96% of identified pathogenic variants. Deletion/duplication analysis accounts for about 4%.
- **Founder effects and carrier frequency:** the recurrent alleles suggest possible founder effects, but I found no population data.
- **Epigenetic and chromosomal data:** none.

## 5. Environmental information

No environmental, lifestyle or infectious factors are known.

## 6. Mechanism and pathophysiology

**Causal chain, with inferred steps marked:**
1. Biallelic YIF1B variants (truncating, deletion or transmembrane missense) cause loss of YIF1B protein or function.
2. This disturbs ER-to-Golgi and Golgi-to-membrane trafficking. Evidence includes accelerated VSVG anterograde traffic and impaired dendritic targeting of the 5-HT1A receptor in neurons (earlier Yif1b knockout work, per search summary). YIF1B also interacts with Rab6.
3. Golgi, ER and primary cilium alterations follow, shown in a Yif1b knockout mouse (Diaz et al.).
4. Neuronal degeneration and altered myelination follow, per the OMIM summary of the mouse work. The link from step 3 to this step is **inferred**.
5. The clinical result is the progressive encephalopathy: developmental delay, epilepsy, movement disorder and microcephaly. This step is **inferred**.

Suggested ontology terms:
- GO:0006888 (ER to Golgi vesicle-mediated transport)
- GO:0005794 (Golgi apparatus)
- GO:0005783 (endoplasmic reticulum)
- GO:0036064 (ciliary basal body), for the cilium alterations if bound
- Cell types: CL:0000540 (neuron), CL:0000128 (oligodendrocyte)

No immune, metabolic, omics or single-cell data were found. A clean molecular mechanism has not been established. The authors state that further functional studies are needed.

## 7. Anatomical structures affected

- **Organ:** brain (UBERON:0000955), including the corpus callosum (UBERON:0002336) and cerebellum (UBERON:0002037).
- **Systems:** nervous system, plus swallowing and motor function.
- **Subcellular:** Golgi apparatus, ER and primary cilium.
- **Lateralization:** bilateral, as expected for a generalized brain disorder **[inferred]**.

## 8. Temporal development

- **Onset:** infancy or early childhood.
- **Course:** progressive, with variable severity.
- **Duration:** lifelong. Early death occurs in some patients.
- No remission patterns or critical periods are described.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Prevalence:** not estimated. This is ultra-rare, with about 25 reported individuals.
- **Sex ratio and ancestry:** I did not retrieve these.
- **Consanguinity:** not retrieved (see section 2).
- **Anticipation and germline mosaicism:** not applicable and not reported.

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing, or a multigene panel, as the first-line approach. Add deletion/duplication analysis to catch whole-gene deletions, which account for about 4% of variants.
- **Imaging:** brain MRI, looking for corpus callosum hypoplasia and cerebellar atrophy.
- **EEG:** for seizure characterization.
- **Biochemical biomarkers:** none known.
- **Differential diagnosis:** other progressive developmental and epileptic encephalopathies, and other Golgi or trafficking disorders such as congenital disorders of glycosylation. I derived this from general knowledge, not from a source.
- **Screening:** no newborn screening.

## 11. Outcome and prognosis

- Severe disability and some early mortality (OMIM).
- Truncating variants appear to carry a worse prognosis than missense variants.
- No survival data or quality-of-life measures were found.

## 12. Treatment

No disease-specific therapy is known. Management is supportive, from general practice and not from a retrieved source:
- Antiseizure medication (NCIT:C15986, Pharmacotherapy)
- Movement-disorder and dystonia care
- Feeding and swallowing support (NCIT:C15747, Supportive Care)
- Physical, occupational and speech therapy (NCIT:C15302, NCIT:C121351, NCIT:C159273)
- Genetic counseling (NCIT:C15240)

I found no clinical trials and no pharmacogenomic data. The GeneReviews management section was not retrieved, so check it before curating treatments.

## 13. Prevention

- Genetic counseling, carrier testing of relatives, and prenatal or preimplantation testing once the familial variants are known (general autosomal recessive practice).
- No primary prevention exists.

## 14. Other species

No naturally occurring disease is documented. I did not check OMIA. YIF1B is conserved across vertebrates.

## 15. Model organisms

- **Yif1b knockout mouse (Diaz et al.):** shows Golgi, ER and primary cilium alterations. The authors propose that some patient features may stem from neuronal degeneration associated with these changes, and OMIM summarizes altered myelination and neuronal death. I could not retrieve the paper, its year or its PMID **[unverified]**. Its fidelity to human microcephaly and epilepsy is unknown.
- **Earlier Yif1b knockout work:**
  - Cultured hippocampal neurons showed accelerated VSVG anterograde traffic.
  - 5-HT1A receptor targeting to dendrites was impaired.
- **Patient-derived and cell models:** Medico Salsench 2021 tested the missense variants functionally. I did not retrieve the assay details.
- No zebrafish, fly or worm models were found.

## Key references

| Reference | Identifier |
|---|---|
| Medico Salsench et al. 2021, Brain, "Expanding the mutational landscape and clinical phenotype of the YIF1B related brain disorder" | [PMID:34373908](https://pubmed.ncbi.nlm.nih.gov/34373908/) |
| Sanri et al. 2023, Eur J Med Genet, "YIF1B-related Kaya-Barakat-Masson Syndrome: Report of a new patient and literature review" | [PMID:36948290](https://pubmed.ncbi.nlm.nih.gov/36948290/) (taken from a mirror URL) |
| AlMuhaizea et al., "Truncating mutations in YIF1B cause a progressive encephalopathy with various degrees of mixed movement disorder, microcephaly, and epilepsy" | PMID not retrieved |
| Diaz et al., Yif1b knockout mouse | PMID not retrieved |
| Gokalp et al. 2026, J Child Neurol, frameshift variant | [DOI:10.1177/08830738261474029](https://doi.org/10.1177/08830738261474029) |
| GeneReviews NBK606999 | PMID not retrieved |
| OMIM [#619125](https://omim.org/entry/619125), [*619109](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/619109) | n/a |

## Gaps to fill before curation

Run `just fetch-reference` on the PMIDs above, then pull these from the cached text:
- Per-feature frequencies.
- MRI findings.
- The GeneReviews management and surveillance recommendations.
- The mouse model details.
- Citable abstract quotes for the snippets.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 11 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030878` (1 mention) - the report calls it "taken from the task, not checked"; MONDO calls it **Kaya-Barakat-Masson syndrome**
- `HP:0001332` (1 mention) - the report calls it "A mixed movement disorder including dystonia"; HP calls it **Dystonia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006888` (1 mention) - the report calls it "ER to Golgi vesicle-mediated transport"; GO calls it **endoplasmic reticulum to Golgi vesicle-mediated transport**, and lists "ER to Golgi vesicle-mediated transport" among its other names
- `UBERON:0000955` (1 mention) - the report calls it "Organ:** brain"; UBERON calls it **brain**