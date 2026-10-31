---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-22T19:41:19.565466'
end_time: '2026-10-22T19:42:51.229717'
duration_seconds: 91.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spermatogenic Failure 47
  mondo_id: MONDO:0030844
  category: Mendelian
  causal_genes: DZIP1
  omim_id: not recorded
  synonyms: SPGF47; DZIP1-related asthenoteratozoospermia; DZIP1-related multiple
    morphological abnormalities of the sperm flagella
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
  num_turns: 6
  total_cost_usd: 0.7212249
  session_id: 7bbfa6a3-7297-5bea-9cda-464f8486036d
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
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 14
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0012206
    reported_labels:
    - Asthenozoospermia
    ontology_label: Abnormal sperm motility
  - term_id: UBERON:0000473
    reported_labels:
    - Suggested UBERON:** testis
    ontology_label: testis
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 47
- **MONDO ID:** MONDO:0030844 (if available)
- **Causal gene(s):** DZIP1
- **OMIM:** not recorded
- **Synonyms:** SPGF47; DZIP1-related asthenoteratozoospermia; DZIP1-related multiple morphological abnormalities of the sperm flagella
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 47** covering all of the
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

# Spermatogenic Failure 47 (SPGF47): DZIP1-related asthenoteratozoospermia with MMAF

**Scope of this report.** I ran a few targeted searches and read one primary paper in full (Lv et al. 2020). The disease rests on essentially one published study, so most template sections are marked "not available". I cite PMIDs only where I confirmed them. Other claims are cited by URL. Treat the mechanism of DZIP1 in sperm as partly inferred from non-sperm systems.

## 1. Disease information

SPGF47 is an autosomal recessive form of male infertility caused by biallelic loss-of-function or missense variants in **DZIP1** (DAZ interacting zinc finger protein 1, 13q32.1). Affected men have asthenoteratozoospermia with severe multiple morphological abnormalities of the sperm flagella (MMAF). Their sperm are immotile, and most lack flagella.

- **Identifiers:** MONDO:0030844 (as given). OMIM 619102 per [MGI's disease page](https://informatics.jax.org/disease/OMIM:619102) and [search results](https://glycosmos.org/diseases/DOID:0112175). Gene OMIM 608671. Orphanet, ICD-10 and MeSH were not checked.
- **Synonyms:** SPGF47; DZIP1-related MMAF; DZIP1-related asthenoteratozoospermia.
- **Data source:** The disease-level description comes from one case report of two individuals. Gene-disease evidence is described as limited (Molecular Interaction Atlas curation label, per search results; this is not an explicit OMIM statement).
- **Unrelated association at the same locus:** OMIM lists a questionable autosomal dominant entry, mitral valve prolapse 3 (610840), for DZIP1. It is a separate phenotype and should not be merged with SPGF47.

## 2. Etiology

- **Causal factor:** Genetic. Homozygous DZIP1 variants were found in two men from consanguineous families (PMID:32051257).
- **Risk and protective factors:** No environmental, lifestyle, modifier or protective factors have been reported. Heterozygous carriers (the parents of one proband) were not reported as affected, and heterozygous knockout mice were fertile like wild type.
- **Gene-environment interactions:** None reported.

## 3. Phenotypes

Source for all rows below: PMID:32051257 (n = 2, ages 27 and 28).

| Phenotype | Finding | Suggested HPO |
|---|---|---|
| Male infertility | Both probands | HP:0003251 (Male infertility) |
| Asthenozoospermia | Total motility 0–2.1%, progressive motility 0% (WHO reference above 32% total and 40% progressive) | HP:0012206 (Asthenozoospermia) |
| Teratozoospermia, MMAF | Absent flagella in 92.4–99.0% of sperm and short flagella in 1.0–7.6%. No normal flagella. TEM showed absent or very short axonemes. | HP:0012864 (Abnormal sperm flagellum morphology) and HP:0012207 (Teratozoospermia) |
| Reduced sperm count | Concentration 0.7–5.3 ×10⁶/mL (reference above 15) | HP:0000798 (Oligospermia) |
| Abnormal sperm centriole | Abnormal centrin1 dot numbers in sperm | No specific HPO term identified |

- **Severity and onset:** Severe, with a presumed congenital basis. The ages at which infertility was recognised were not reported.
- **Frequency:** In the MMAF cohort of 65 unrelated Han Chinese men, 2 carried DZIP1 variants (3.1%).
- **Other findings:** Normal 46,XY karyotype, no large Y-chromosome deletions, and no other ciliopathy signs were found in the two men. Semen volume was normal. I did not check whether the paper reports hormone levels or testis volume.
- **Quality of life:** Not reported.

## 4. Genetic and molecular information

- **Gene:** DZIP1 (hgnc: not verified here; look it up before binding). It has zinc-finger and coiled-coil domains.
- **Variants** (PMID:32051257):
  - c.188G>A, p.Arg63Gln. This is a homozygous missense variant at a conserved residue, predicted deleterious by SIFT, PolyPhen-2 and MutationTaster.
  - c.690T>G, p.Tyr230\*. This is a homozygous stop-gain, with both parents heterozygous. It lies at the start of the first coiled-coil domain, so all three coiled-coil domains are lost.
  - Neither variant appears in 1000 Genomes, ExAC or gnomAD, or in Han Chinese controls.
  - The paper's Methods give the stop-gain as p.Tyr23\* while the Results and Figure 1 give p.Tyr230\*. Curators should record the discrepancy and use p.Tyr230\*.
- **Origin and function:** Germline. The variants are described as loss of function. Per the paper, the variant constructs in HEK293T cells gave reduced or truncated protein.
- **ClinVar and ClinGen classification:** Not checked.
- **Modifier, epigenetic and chromosomal data:** None reported.

## 5. Environmental information

None reported. There are no known toxin, lifestyle or infectious contributors.

## 6. Mechanism and pathophysiology

**Causal chain** (steps 1–4 are demonstrated in patients or knockout mice; step 5 is inferred from other systems):

1. Biallelic DZIP1 variants (p.Arg63Gln, or truncation at Tyr230) lead to loss of DZIP1 protein. Patient sperm showed absent DZIP1 signal.
2. DZIP1 loss results in abnormal centrioles in sperm (abnormal centrin1 dot counts, in about half or more of sperm in one proband).
3. Abnormal centrioles lead to weak, misplaced or absent IFT88 and IFT140 signals. This is correlative in patient sperm.
4. Failed axoneme assembly results in absent or short flagella (MMAF) and immotile sperm, hence asthenoteratozoospermia and male infertility. Knockout mice reproduce this endpoint with infertile males, few and immotile sperm, and mostly absent flagella.
5. **Inferred:** In other systems DZIP1 acts at the basal body and centriolar satellites. It forms a BBSome–DZIP1–PCM1 complex and promotes ciliary Rab8 activation via GDI2 ([GSK3β–Dzip1–Rab8 study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4393111/)). A Drosophila study reports a role for Dzip1 in basal body docking during spermatogenesis (per search summary). The Lv et al. discussion cites these ideas. This work did not test whether those same steps are the mechanism in human sperm.

- **Suggested GO terms** (verify before use): cilium assembly (GO:0060271), sperm flagellum assembly or axoneme assembly, and centriolar satellite as a cellular component.
- **Cell types:** spermatid (CL:0000018) and spermatozoon (CL:0000019). DZIP1 is expressed mainly in testis, especially elongating spermatids in mouse.
- **Omics, immune and metabolic changes:** None reported.

## 7. Anatomical structures affected

- **Organs:** testis and epididymis, with a reproductive-system phenotype only in the reported patients.
- **Cells and subcellular:** elongating spermatids; the sperm centriole/basal body and the flagellar axoneme. In human sperm DZIP1 localizes to the head and neck.
- **Laterality:** Not applicable. Findings are in semen.
- **Suggested UBERON:** testis (UBERON:0000473) and epididymis (UBERON:0001301).

## 8. Temporal development

Presumed congenital. Infertility becomes apparent in adulthood on semen analysis. No data exist on progression, remission or critical periods.

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive (HP:0000007). Both families were consanguineous.
- **Population:** Both families were Han Chinese. Founder effects, carrier frequency, prevalence and geographic variant distribution are unknown.
- **Sex:** Affected phenotype is male. Whether female carriers have any phenotype was not reported.
- **Penetrance and expressivity:** Not established, since only two individuals are reported.

## 10. Diagnostics

- **Semen analysis:** Low motility with a high proportion of absent or short flagella.
- **Electron microscopy:** Absent or very short axonemes.
- **Immunofluorescence:** Absent DZIP1 and weak or misplaced IFT88 and IFT140 in sperm. This is a research method.
- **Genetic testing:** Exome sequencing found both variants. A reasonable approach is to include DZIP1 on MMAF or male infertility gene panels. The paper does not give formal testing recommendations.
- **Differential diagnosis:** Other MMAF genes. The paper names DNAH1, CEP135, CATSPER2 and SUN5 as related asthenoteratospermia genes ([search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC7361034)), and known genes explain only about half of cases. Primary ciliary dyskinesia should also be considered, although the two probands had no other ciliopathy features.

## 11. Outcome and prognosis

No survival, life-expectancy or quality-of-life data. The phenotype appears limited to infertility, with no systemic complications reported in the two men.

## 12. Treatment

- **ICSI or other assisted reproduction outcomes:** Not reported in the paper. The authors say the probands will be followed up.
- **Other therapies:** No gene therapy, drug or clinical trial was identified (no search of ClinicalTrials.gov was run).
- **Reasoning only:** Because nearly all sperm lack flagella and are immotile, outcomes of assisted reproduction cannot be predicted from the available data.

## 13. Prevention

Genetic counselling for consanguineous couples. Recurrence risk is 25% per pregnancy when both parents are carriers, which follows from autosomal recessive inheritance. No screening programs or environmental measures apply.

## 14. Other species and natural disease

No naturally occurring disease in other species was identified (OMIA was not searched).

## 15. Model organisms

- **Mouse knockout** (PMID:32051257): CRISPR-Cas9 frameshift allele c.102_132del (p.Ala35Serfs\*13), with DZIP1 protein absent.
  - All homozygous males were infertile.
  - Very few epididymal sperm were recovered, none motile.
  - Most sperm were severely malformed, mainly with absent flagella, plus cytoplasmic residue and abnormal heads.
  - Heterozygous males did not differ from wild type.
  - The mouse study did not directly assess centrioles or IFT.
  - The mouse phenotype closely matches the human MMAF phenotype.
- **Other systems:** Zebrafish (iguana) and mouse embryonic fibroblasts support a role in ciliogenesis ([GSK3β–Dzip1–Rab8](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4393111/); also an unreviewed Hedgehog-signalling paper at [pure.psu.edu](https://pure.psu.edu/en/publications/centrosomal-protein-dzip1-regulates-hedgehog-signaling-by-promoti/)). A Drosophila study reports a role in basal body docking in spermatogenesis. I did not verify these models independently.
- **Limitations:** Mouse centriole and IFT phenotypes were not tested, and the human data come from two individuals.

## Gaps and cautions for curators

- **Single report.** All patient-level evidence comes from PMID:32051257. I did not find a second family or case series.
- **Unverified identifiers.** I did not verify HGNC, GO, CL, UBERON or HPO CURIEs. Look each one up before binding.
- **Quotes.** I read the paper through a summarising tool and did not extract exact abstract quotes. Fetch the cached reference with `just fetch-reference PMID:32051257` and copy snippets from it.
- **Unread part of the paper.** The last ~2,500 characters of the PMC page were not read.

## Sources

- [Lv et al. 2020, J Med Genet 57:445–453, PMID:32051257 (PMC7361034)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7361034)
- [J Med Genet article page](https://jmg.bmj.com/content/57/7/445)
- [MGI disease page, OMIM:619102](https://informatics.jax.org/disease/OMIM:619102)
- [GlyCosmos entry for SPGF47](https://glycosmos.org/diseases/DOID:0112175)
- [GSK3β–Dzip1–Rab8 cascade and ciliogenesis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4393111/)
- [Dzip1 and Hedgehog signalling](https://pure.psu.edu/en/publications/centrosomal-protein-dzip1-regulates-hedgehog-signaling-by-promoti/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012206` (1 mention) - the report calls it "Asthenozoospermia"; HP calls it **Abnormal sperm motility**
- `UBERON:0000473` (1 mention) - the report calls it "Suggested UBERON:** testis"; UBERON calls it **testis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000798` (1 mention) - the report calls it "Oligospermia"; HP calls it **Oligozoospermia**, and lists "Oligospermia" among its other names
- `CL:0000018` (1 mention) - the report calls it "Cell types:** spermatid"; CL calls it **spermatid**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.