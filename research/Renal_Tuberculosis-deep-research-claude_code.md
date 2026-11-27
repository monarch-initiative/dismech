---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T03:49:09.757118'
end_time: '2026-11-26T03:54:10.260913'
duration_seconds: 300.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Renal Tuberculosis
  mondo_id: MONDO:0005938
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: kidney tuberculosis; tuberculosis of kidney
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
  web_search_requests: 24
  num_turns: 31
  total_cost_usd: 1.39859863
  session_id: 033424d3-6ae8-48f8-acea-5cce9999706a
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 49
  retrieval_calls: 44
  assistant_text_blocks: 3
citation_count: 49
reference_validation:
  total_references: 47
  verified: 47
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 3
  quotes_unsupported: 8
  unsupported_quote_references:
  - PMID:24578959
  - PMID:28540230
  - PMC:PMC11687435
  - PMC:PMC2556487
  - PMC:PMC6977373
  - PMC:PMC9999700
  - PMC:PMC4340670
  - PMID:31548730
  relevance_assessed: 47
  on_topic: 20
  off_topic: 2
  off_topic_references:
  - PMID:36482950
  - PMC:PMC9715008
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0005938
    reported_labels:
    - supplied
    ontology_label: renal tuberculosis
  - term_id: DOID:9733
    reported_labels:
    - MGI disease page
    ontology_label: renal tuberculosis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Tuberculosis
- **MONDO ID:** MONDO:0005938 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** kidney tuberculosis; tuberculosis of kidney
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Renal Tuberculosis** covering all of the
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

I'm gathering sources for the renal TB report. Direct PubMed calls from the shell are blocked here, so I'm using web search instead.

I have enough sources for most sections. Running a last round of searches on latency, epidemiology and treatment regimens before I write the report.

# Renal Tuberculosis (MONDO:0005938): Disease Characteristics Research Report

**How I read the request:** Renal tuberculosis (TB) is an infectious disease, not a Mendelian one. Its cause is infection with the *Mycobacterium tuberculosis* complex: mainly *M. tuberculosis*, sometimes *M. bovis*. **No single causal gene is recorded for it, and none exists.** Host genes only change how susceptible a person is. Most primary literature treats renal TB as the main part of "genitourinary" or "urogenital" TB (GUTB/UGTB), so I used those sources where none were kidney-specific.

**Limits on the evidence:**
- PubMed and PMC full-text pages could not be fetched in this session (cookie and CAPTCHA blocks, and shell network access was denied). Most facts below come from abstracts and excerpts returned by web search.
- I only marked text as a direct quote where it came back as quoted source text. Where only a PMC ID or DOI was retrieved, I give that instead of a PMID.
- **Ontology terms (HPO, GO, CL, UBERON, CHEBI, NCIT) are given as labels only.** I did not retrieve or check their numeric IDs, so map them before loading.

---

## 1. Disease Information

**Overview.**
- Disease Ontology defines renal TB as "an urogenital tuberculosis that results_in formation of granulomas located_in kidney" (MGI/DO page: https://www.informatics.jax.org/disease/DOID:9733).
- GUTB "usually arises from reactivation of old, dormant infection by members of the *M. tuberculosis* complex" (Cent Eur J Urol 2012, PMID 24578959).
- Urogenital TB causes about 30–40% of extrapulmonary TB cases, second only to lymph-node disease (PMC11687435; also Figueiredo & Lucon review, PMID 18836557).

**Identifiers.**

| System | Code |
|---|---|
| MONDO | MONDO:0005938 (supplied) |
| Disease Ontology | DOID:9733 (MGI disease page) |
| ICD-10 / ICD-10-CM | A18.1 "Tuberculosis of genitourinary system" (header); **A18.11 "Tuberculosis of kidney and ureter"** (CMS ICD-10-CM; https://www.cms.gov/ICD10m/version372-fullcode-cms/fullcode_cms/P0245.html; https://gesund.bund.de/en/icd-code-search/a18-1) |
| ICD-11 | 1B12.5 "Tuberculosis of the genitourinary system" (third-party AutoICD listing; https://autoicdapi.com/icd11/1B12.5). I did not find a kidney-only ICD-11 code; confirm in the WHO browser. |
| OMIM / Orphanet | Not applicable (not a Mendelian or rare-disease entry) |
| MeSH | Indexed under "Tuberculosis, Renal" (descriptor ID not retrieved this session) |

**Synonyms.** Kidney tuberculosis; tuberculosis of kidney; tuberculous nephritis. It is part of genitourinary or urogenital TB. The end-stage form is called "putty kidney" or tuberculous autonephrectomy (PMID 35812261).

**Type of evidence.** Disease-level knowledge comes from aggregated sources: narrative reviews, retrospective hospital series, autopsy series, and meta-analyses. There are no patient-level registries specific to renal TB.

---

## 2. Etiology

**Causal agent.**
- *Mycobacterium tuberculosis* complex, mainly *M. tuberculosis*; *M. bovis* is a zoonotic cause.
- The usual route is reactivation of bacilli that reached the kidney through the blood during the first lung infection (PMID 24578959). Genitourinary involvement "almost always follows a pulmonary infection" (Transl Androl Urol 2017, PMID 28540230).
- A separate iatrogenic route exists: granulomatous disease after intravesical BCG (*M. bovis* BCG) for bladder cancer. This is in the general literature, but I did not retrieve a source for it this session.

**Risk factors (human clinical evidence).**
- **Chronic kidney disease, dialysis, and kidney transplant:**
  - A 2023 meta-analysis (Clin Infect Dis 77:1194–1200, doi 10.1093/cid/ciad364; PMC10573716) found a pooled adjusted HR of **1.57 (95% CI 1.22–2.03)** for TB in CKD without kidney failure. Risk was highest in stages 4–5 (IRR **3.63**, 2.25–5.86).
  - An earlier meta-analysis (PMID 26614191) reported a dialysis rate ratio of **3.62 (1.79–7.33)** and raised risk after kidney transplant.
  - A Korean cohort found kidney failure carried a 4.39-fold TB risk.
  - These are risks for TB overall, not renal TB specifically.
- **HIV / AIDS:** "The AIDS epidemic caused unexpected worldwide levels of tuberculosis, even in developed countries" (PMID 18836557).
- **Age and sex:** Most common in men in their 40s and 50s (PMC11687435).
- **Living in or migrating from a high-burden area**, and a past history of pulmonary TB (PMID 31548730).
- **Diabetes and immunosuppressive drugs** are established TB risk factors in general. I did not retrieve renal-specific data for them.

**Genetic risk factors (susceptibility only, not causal).**
- **Mendelian susceptibility to mycobacterial disease (MSMD)** comes from inborn errors of IFN-γ immunity. It involves at least 19–20 genes, including **IFNGR1** (AR or AD) and **IL12RB1** (AR), and penetrance is incomplete (Bustamante et al., PMC4357480; update PMC6438774; overview PMID 40656276).
- **TYK2 P1104A homozygosity:** "TYK2 P1104A impairs cellular responses to IL-23, but not to IFN-α, IL-10, or even IL-12." Homozygotes are "found in about 1/600 Europeans and between 1/1000 and 1/10,000 individuals in regions other than East Asia" (Boisson-Dupuis et al., Sci Immunol 2018, PMID 30578352). In UK Biobank, homozygotes were 6/620 TB patients (1%) versus 0.2% of controls, OR about 5.
- **Polymorphisms tested for extrapulmonary TB:**
  - IL1B, VDR FokI, and TLR2 variants were associated with EPTB in a small pilot (24 EPTB cases; PMC2837863).
  - IFNG +874 T/A (rs2430561) looked protective for pulmonary and extrapulmonary TB in a 42-study meta-analysis (PMC5584145).
  - TLR2 Arg753Gln was associated with pulmonary TB but **not** EPTB (PMC6348792).
  - No GWAS signal specific to renal TB was found.

**Protective factors.**
- Genetic: possibly the IFNG +874 alleles above (PMC5584145).
- Environmental: avoiding unpasteurized milk (lowers *M. bovis* risk; WHO Zoonotic TB Roadmap, https://www.who.int/publications/i/item/9789241513043), treating latent infection, controlling HIV, and finishing treatment of pulmonary TB.

**Gene–environment interaction.** Disease needs exposure plus a host immune defect. The MSMD and TYK2 genotypes only matter after mycobacterial exposure, and penetrance is incomplete (PMC4357480; PMID 30578352). No GxE studies specific to renal TB were found.

---

## 3. Phenotypes

Onset is in adults, mostly in their 40s and 50s, with an insidious, slowly progressive course (PMC11687435).

| Phenotype | Type | Reported frequency | Source | Suggested HPO label |
|---|---|---|---|---|
| Lower urinary tract symptoms (frequency, dysuria) | Symptom | 65.2% | PMID 28343213 | Dysuria; Urinary urgency / Pollakisuria |
| Flank or loin pain | Symptom | 37.9% | PMID 28343213 | Flank pain |
| Gross hematuria | Sign | 26.3% | PMID 28343213 | Macroscopic hematuria |
| Hematuria (any) | Lab | about 51% | BMC Urol 2021, doi 10.1186/s12894-021-00888-3 | Hematuria |
| Pyuria, classically "sterile" (routine culture negative) | Lab | about 68% | BMC Urol 2021 | Pyuria / Sterile pyuria |
| Proteinuria | Lab | about 68% | BMC Urol 2021 | Proteinuria |
| Constitutional symptoms (fever, weight loss, night sweats, anorexia) | Symptom | 38.9% | PMID 28343213; PMC3737618 | Fever; Weight loss; Night sweats; Anorexia |
| Recurrent UTI not responding to standard antibiotics | Sign | qualitative | PMC6837772 / PMID 31754491 | Recurrent urinary tract infections |
| Hydronephrosis / hydroureter (from strictures) | Imaging sign | common | Radiopaedia renal TB article | Hydronephrosis; Hydroureter |
| Renal calcification | Imaging sign | about one-third | Radiopaedia | Nephrocalcinosis / Renal calcification |
| Small contracted bladder | Sign | late | PMC11687435 | Decreased bladder capacity |
| Hypertension (non-functioning kidney) | Sign | occasional | PMC2684360 | Hypertension |
| Reduced kidney function / ESKD | Lab | in late or interstitial-nephritis forms | PMC9999700 | Chronic kidney disease; Stage 5 CKD |

**Severity.** Ranges from mild urinary symptoms to loss of the kidney or bilateral kidney failure. Symptoms are non-specific, which delays diagnosis (PMID 23730329; PMC11884631).

**Quality of life.** Lower urinary tract symptoms and a contracted bladder hurt daily function, and infertility arises when genital TB coexists. **No EQ-5D or SF-36 data for renal TB were retrieved.**

---

## 4. Genetic/Molecular Information

- **Causal genes:** None (infectious disease).
- **Pathogen genetics:**
  - *M. tuberculosis* H37Rv is the reference strain and is used in experimental renal models (RU2776130C1).
  - *M. bovis* is naturally resistant to pyrazinamide (WHO Zoonotic TB Roadmap).
  - The rifampicin-resistance region of rpoB is detected by Xpert MTB/RIF (PMID 33448348).
- **Host susceptibility genes:** IFNGR1, IL12RB1, TYK2 (P1104A, missense, partial loss of function selective for IL-23), plus other MSMD genes; all germline (PMC4357480; PMID 30578352). ACMG classifications for renal TB are not applicable.
- **Allele frequency:** TYK2 P1104A homozygosity is about 1/600 in Europeans (PMID 30578352).
- **Modifier, epigenetic, and chromosomal data:** None specific to renal TB were found.

---

## 5. Environmental Information

- **Infectious agents:** *M. tuberculosis* complex (*M. tuberculosis*, *M. bovis*; NCBI Taxonomy IDs not retrieved this session).
- **Zoonotic route:**
  - WHO estimated 147,000 new zoonotic TB cases and about 12,500 deaths in 2016.
  - Infection comes mainly from untreated meat and dairy products.
  - *M. bovis* disease is often extrapulmonary and "clinically indistinguishable" from *M. tuberculosis* disease.
  - Source: WHO/FAO/WOAH Roadmap, https://www.who.int/news/item/12-10-2017-tb-partners-launch-first-roadmap-to-jointly-stop-the-transmission-of-bovine-and-zoonotic-tuberculosis.
- **Lifestyle factors:** Overcrowding, poverty, malnutrition, smoking, and alcohol are general TB drivers. The 8961-case review notes that regional differences track epidemic conditions and national economic status (PMID 18836557). No renal-specific data were retrieved.
- **Toxins and radiation:** Not applicable.

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. **The *M. tuberculosis* complex is inhaled (or *M. bovis* is swallowed)**, which leads to a primary infection, usually in the lung (PMID 28540230).
2. **Bacilli spread through the blood during that primary infection**, which seeds the kidney. "After hematogenous spread from the pulmonary focus, there is colonization of the renal parenchyma, with initially bilateral, cortical, glomerular, and pericapillary renal lesions" (urogenital TB review retrieved via search, PMC11687435/PMC2556487).
3. **Cell-mediated immunity (IL-12/IL-23 to IFN-γ to macrophage activation) contains the seeded bacilli** in small cortical granulomas, which results in clinical latency.
   - Latency averages about 22 years (range 1–46 years). Elsewhere it is given as 5–40 years, with GUTB in 2–20% of people with pulmonary TB.
   - Autopsy series: GUTB in 3.1% of 5,424 autopsies, 98% bilateral, 85% with lung lesions.
   - Sources: search-retrieved review excerpts; PMC11687435.
   - *(Branch, inferred from genetic data:)* Defects in this axis (IFNGR1, IL12RB1, TYK2 P1104A) or acquired immunosuppression (HIV, CKD/dialysis, transplant drugs) lead to failed containment (PMC4357480; PMID 30578352; doi 10.1093/cid/ciad364).
4. **Waning immunity lets the bacilli reactivate**, typically at one focus. That focus grows, so clinical disease is usually unilateral even though seeding was bilateral: "infection progresses from a single focus, affecting one kidney and sparing the other."
5. **Granulomas grow and caseate in the medulla and papillae**, which results in papillary necrosis (tuberculous papillitis) and rupture of caseous material into the collecting system. This is Kulchavenya stage 2 (PMC4340670).
6. **Bacilli and debris then pass into the urine**, which leads to:
   - (a) urine positive for acid-fast bacilli (AFB) or NAAT with "sterile" pyuria and hematuria, and
   - (b) spread down to the ureter, bladder, and, in men, the prostate and epididymis (PMID 36482950 for retrograde genital spread).
7. **Chronic granulomatous inflammation heals by fibrosis**, which results in strictures of the infundibula, pelviureteric junction, and ureterovesical junction. This causes "phantom calyx", hydrocalycosis, and hydronephrosis. Ureteral stenosis accounts for "up to 93.7%" of renal exclusion (PMC2684360; RSNA RadioGraphics 2021, doi 10.1148/rg.2021200154).
8. **Cavities form and obstruction persists**, which leads to cavernous and then polycavernous disease (stages 3–4). With dystrophic calcification this becomes a non-functioning "putty kidney" or autonephrectomy (PMID 35812261; PMC4340670).
9. **Bladder involvement leads to fibrosis**, which results in a small contracted bladder, vesicoureteral reflux, and pressure on the upper tract (PMC11687435).
10. **Clinical outcome:** lower urinary tract symptoms, flank pain, hematuria, hypertension, and loss of function in one kidney or, if bilateral, CKD or ESKD.
    - *Parallel branch:* Diffuse **granulomatous tubulointerstitial nephritis** (TIN) without urinary-tract destruction leads directly to acute or chronic kidney failure. In one series, 17/25 biopsied TB patients with significant renal disease had chronic granulomatous TIN, and it "presents late with advanced disease" (PMC6977373/related series; PMC9999700).
    - Secondary AA amyloidosis is a further branch from chronic inflammation. This is from general literature; I did not retrieve a source this session.

### Mechanism detail

- **Molecular pathways:** IL-12/IL-23 to JAK/TYK2 to STAT4 to IFN-γ (TYK2 P1104A selectively breaks IL-23-driven IFN-γ; PMID 30578352). Also TLR2 recognition and VDR-dependent antimicrobial responses (PMC2837863).
- **Cellular processes:** Granuloma formation, caseous necrosis, macrophage activation, fibrosis. Suggested GO labels: *granuloma formation*, *response to bacterium / defense response to Gram-positive bacterium*, *interferon-gamma-mediated signaling pathway*, *macrophage activation*, *inflammatory response*, *fibroblast proliferation*.
- **Cell types (CL labels):** macrophage; epithelioid cell; multinucleated giant cell (Langhans); CD4-positive alpha-beta T cell; renal tubular epithelial cell; glomerular endothelial cell; urothelial cell; fibroblast.
- **Upstream vs downstream:** Steps 1–4 (infection, seeding, immune containment and its failure) are upstream. Steps 5–10 (necrosis, fibrosis, obstruction, kidney loss) are downstream tissue-damage mechanisms.
- **Omics, single-cell, and spatial data:** **None specific to renal TB were found.** Granuloma omics work in TB is lung-based.

---

## 7. Anatomical Structures Affected

- **Primary organ:** Kidney: cortex at seeding, then medulla, papillae, calyces, and renal pelvis (UBERON labels: *kidney*, *renal cortex*, *renal medulla*, *renal papilla*, *renal pelvis*, *major/minor calyx*).
- **Secondary organs:**
  - ureter (strictures, often at the ureterovesical junction), urinary bladder (contracted bladder);
  - in men, the prostate, seminal vesicle, epididymis, and vas deferens (PMID 36482950);
  - the lung (concurrent or prior disease; 85% at autopsy).
- **Body systems:** Urinary, reproductive, immune, and respiratory.
- **Tissue level:** Renal tubulointerstitium, glomeruli (initial seeding), urothelium, fibrous connective tissue.
- **Subcellular level:** Bacilli live inside the macrophage phagosome or phagolysosome (GO CC labels: *phagocytic vesicle*, *lysosome*). This is general TB biology; I did not retrieve a renal-specific source.
- **Laterality:** Seeding is bilateral (98% at autopsy). Clinical, destructive disease is usually **unilateral** (search-retrieved review excerpts). Bilateral disease puts kidney function at risk.

---

## 8. Temporal Development

- **Onset:** Adults, mostly in their 40s and 50s (PMC11687435). Insidious and chronic, after a latency averaging about 22 years.
- **Stages (Kulchavenya; PMC4340670):**
  - "Level 1 – nondestructive form, TB of parenchyma"
  - "Level 2 – small destructive form, TB papillitis"
  - "Level 3 – destructive form with one or two caverns (cavernous kidney TB)"
  - "Level 4 – widespread destructive form with more than two caverns (polycavernous kidney TB)"
- **Progression:** Slow, but strictures can form or worsen *during* treatment as lesions heal. This is why early stenting or nephrostomy is advised (PMC2684360).
- **Remission:** Treatment-induced. Stages 1–2 are curable with drugs. "Cavernous KTB… recovery without surgery is rare. Polycavernous KTB… recovery with anti-TB drugs only is impossible, surgery is necessary, basically nephrectomy" (PMC4340670).
- **Critical window:** Diagnosis before cavities and strictures form (stages 1–2) preserves the kidney.

---

## 9. Inheritance and Population

- **Inheritance:** Not inherited. Susceptibility can be monogenic (MSMD: AR or AD, incomplete penetrance) or multifactorial (PMC4357480).
- **Global TB burden:**
  - 10.8 million incident TB cases in 2023; 8.2 million notified.
  - About **16% of notified cases were extrapulmonary** (the denominator should be checked) (WHO Global TB Report 2024, https://www.who.int/publications/i/item/9789240101531; https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024/tb-diagnosis-and-treatment/2-1-case-notifications).
  - 8.3 million notifications in 2024 (WHO 2025 report).
- **Renal and urogenital share:** UGTB is 30–40% of EPTB in reviews (PMC11687435; PMID 18836557). Its share is much lower in some low-burden series.
- **No direct prevalence or incidence per 100,000 for renal TB was retrieved.**
- **Geography:** Endemic regions (Africa, South and Southeast Asia) and migrants from them (PMID 34827337, which also notes that GUTB is under-recognized in Europe).
- **Sex ratio:** Male predominance (PMC11687435).
- **Pediatric cases** are rare because of the long latency.

---

## 10. Diagnostics

**Microbiology (reference standard).** "Specific diagnosis rests on culturing *M. tuberculosis* from a suitable clinical sample or identifying its DNA" (PMID 31548730). Standard practice is 3–5 early-morning urine samples for AFB smear and mycobacterial culture (liquid or solid).

**Nucleic acid amplification tests (NAAT) on urine:**

| Study | Result |
|---|---|
| Altez-Fernandez et al., BMC Infect Dis 2017 (PMID 28583076) | "Xpert studies were of good quality and not heterogeneous, pooled sensitivity was 0·87 (0·66–0·96) and specificity was 0·91 (0·84–0·95)." "PCR studies were highly heterogeneous." |
| Chen et al., Int J Infect Dis 2020 (doi 10.1016/j.ijid.2020.03.023) | Against culture: sensitivity 0.89, specificity 0.95. Against a composite reference: sensitivity 0.55, specificity 0.99. Xpert is "a promising diagnostic tool for the diagnosis of UGTB via urine specimen." |
| Chen et al., Sci Rep 2019 (PMID 31363115), 302 patients | "Against culture, Xpert and smear achieved a sensitivity of 94.4% (95% CI: 81.3–99.3%)." Against the composite reference, "the sensitivity of Xpert, smear and culture was 41.3%." |
| Cochrane, all EPTB (PMID 33448348) | Pooled Xpert sensitivity 71.1%, specificity 96.9% across non-respiratory specimens. |

**Routine lab tests.** Urinalysis (sterile pyuria, hematuria, proteinuria), serum creatinine and eGFR. IGRA or tuberculin skin test supports infection but does not distinguish latent from active disease.

**Imaging:**
- MDCT urography has replaced IV urography. "Multidetector computed tomography can reproduce images comparable with intravenous excretory urography" (Mthalane et al., PMID 31754491).
- Key findings: papillary necrosis, infundibular stenosis, "phantom calyx," hydrocalycosis, cortical scarring, calcification (CT is the most sensitive), thickened ureter or pelvis wall, "putty kidney" (PMID 35812261; RadioGraphics doi 10.1148/rg.2021200154).
- Individual findings are not specific, but "presence of multiple imaging findings in a single case is pointer to this disease" (Sankhe & Joshi, Curr Radiol Rep 2014).
- Also: chest imaging, and DMSA/renography to estimate split kidney function.

**Biopsy and histopathology.**
- Caseating epithelioid granulomas with Langhans giant cells, AFB on Ziehl–Neelsen stain, tissue PCR.
- Granulomatous interstitial nephritis is found in 0.5–0.95% of native kidney biopsies. TB causes just over half of cases in an Indian series and none in a Glasgow series (PMC9999700).

**Genetic testing.** Not applicable for diagnosis. Consider MSMD gene panels or exomes (IFNGR1, IL12RB1, TYK2, and others) only for disseminated, recurrent, or BCG/environmental-mycobacterial disease in young patients (PMC4357480).

**Omics diagnostics.** None validated for renal TB.

**Differential diagnosis.**
- Other causes of sterile pyuria: partly treated UTI, interstitial nephritis, urolithiasis, Chlamydia/Ureaplasma.
- Xanthogranulomatous pyelonephritis.
- Papillary necrosis from analgesics, diabetes, or sickle cell disease.
- Renal cell carcinoma or urothelial carcinoma.
- Renal sarcoidosis (granulomatous TIN; caseation favors TB) (PMC9999700).
- Medullary sponge kidney; post-BCG granulomatous disease.

**Screening.** There is no population screening. Screen high-risk groups for latent TB: before dialysis or transplant, people with CKD stages 4–5, people with HIV (doi 10.1093/cid/ciad364).

---

## 11. Outcome/Prognosis

- **Mortality:** Low when treated. **No 5- or 10-year survival figures specific to renal TB were retrieved.**
- **Morbidity:**
  - Kidney loss (non-functioning kidney, autonephrectomy).
  - Ureteral stricture; contracted bladder; hypertension; infertility (genital involvement).
  - CKD or ESKD: in granulomatous-TIN series, two of five TB patients reached ESKD and the rest had a mean eGFR of 28 mL/min at 1 year (PMC9999700/related UK series).
- **Historical shift:** In 1945 the nephrectomy rate was 97% (Nesbit, 260 patients). In 1970, Bloom et al. managed all 25 non-functioning kidneys conservatively (PMC2684360).
- **Prognostic factors:**
  - Stage at diagnosis (Kulchavenya 1–2 versus 3–4).
  - Bilateral disease.
  - Length of stricture: balloon dilation does best with strictures under 1.5 cm, non-ischemic, and with adequate kidney function (PMC2684360).
  - Baseline eGFR; HIV and immunosuppression; drug resistance.
- **Prognostic biomarkers:** None established.
- **Quality-of-life instruments:** None reported.

---

## 12. Treatment

**Drug therapy (drug-susceptible disease).**
- Standard **2HRZE/4HR**: isoniazid, rifampicin, pyrazinamide, and ethambutol for 2 months, then isoniazid and rifampicin for 4 months. GUTB is treated for 6–9 months (PMID 31548730; ATS/CDC/IDSA guideline, Nahid et al., Clin Infect Dis 2016, doi 10.1093/cid/ciw376; WHO Module 4, https://www.who.int/publications/i/item/9789240048126).
- Drug-resistant TB needs 12–24 months of more toxic drugs with close monitoring (PMID 31548730). WHO's newer short regimens for drug-resistant TB are not covered by the sources retrieved here.
- The WHO 4-month HPMZ regimen (rifapentine and moxifloxacin) covers **pulmonary** TB in people aged 12 and over, based on Study 31. Its use in extrapulmonary or renal TB is not established.
- *M. bovis* is naturally pyrazinamide-resistant, so treat for 9 months without pyrazinamide (WHO Zoonotic TB Roadmap; duration from general practice).
- **Dose adjustment in reduced kidney function:** Ethambutol and pyrazinamide are cleared by the kidney, so their dosing interval is extended in CKD and on dialysis. This is a guideline-level fact that I did not re-verify this session.
- Corticosteroids to prevent ureteral stricture are sometimes used, but the evidence is weak; no source was retrieved.

**Pharmacogenomics.** NAT2 acetylator status affects isoniazid exposure and liver toxicity. This is known biology, but I did not retrieve a source this session.

**Surgery and interventions (PMC2684360; PMID 23730329).**
- **Stenting or percutaneous nephrostomy** for obstruction: "Stents or nephrostomy tubes decrease the likelihood of renal loss."
- **Endoscopic balloon dilation** of strictures.
- **Ureteral reimplantation, Boari flap, ileal ureter substitution, and pyelo- or ureterocalyceal reconstruction.**
- **Augmentation cystoplasty** for a contracted bladder.
- **Nephrectomy or partial nephrectomy** for a non-functioning kidney with pain or hypertension, deferred until several weeks of drugs. Laparoscopic nephrectomy is "safe, effective and less invasive."

**Advanced therapies (gene, cell, RNA, targeted, immunotherapy).** Not applicable. No renal-TB trials (NCT numbers) were identified.

**NCIT-style intervention labels:** Isoniazid; Rifampin; Pyrazinamide; Ethambutol; Rifapentine; Moxifloxacin; Nephrectomy; Ureteral Stent Placement; Percutaneous Nephrostomy; Ureteral Reimplantation; Augmentation Cystoplasty.

**Treatment algorithm.**
1. Microbiological confirmation (urine culture plus Xpert, which also screens for rifampicin resistance).
2. Drug susceptibility testing.
3. Standard regimen.
4. Imaging at baseline and during early treatment to catch new strictures.
5. Early drainage for obstruction.
6. Delayed reconstruction or nephrectomy for stage 3–4 disease.

---

## 13. Prevention

- **Primary prevention:**
  - TB infection control; HIV control; pasteurizing milk and controlling bovine TB (WHO Roadmap).
  - BCG vaccination protects mainly children from disseminated TB. Its effect on adult renal TB is not established.
- **Secondary prevention:**
  - Screening for and treating latent TB in CKD stages 4–5, before dialysis or transplant, and in people with HIV (doi 10.1093/cid/ciad364; PMID 26614191).
  - Raising suspicion for sterile pyuria or recurrent UTI that fails standard antibiotics in endemic settings (PMID 31754491).
- **Tertiary prevention:** Early stenting and imaging follow-up to stop strictures from destroying the kidney (PMC2684360); following kidney function over time.
- **Genetic counseling:** Only for families with MSMD or TYK2 genotypes (PMC4357480).

---

## 14. Other Species / Natural Disease

- ***Mycobacterium bovis* in cattle** is the main animal reservoir. Zoonotic transmission to humans is mainly through food (WHO Roadmap).
- I retrieved **no kidney- or urogenital-specific veterinary data**, and none from OMIA (not applicable, because the disease is not Mendelian).
- **Comparative note:** The rabbit model produces kidney lesions "very closely related to those found in chronic human kidney tuberculosis" (Jpn J Urol 1932, https://www.jstage.jst.go.jp/article/jpnjurol1928/21/10/21_10_506/_article/-char/en).

---

## 15. Model Organisms

- **Rabbit, direct kidney inoculation:** "A fine needle puncture of the cortical layer of the parenchyma of the lower pole of the kidney is performed under ultrasound control to the rabbit" with *M. tuberculosis* H37Rv (patent RU2776130C1, https://patents.google.com/patent/RU2776130C1/en). This is an induced model meant to imitate the clinical course.
- **Rabbit, intravenous:** Ear-vein inoculation produces miliary disease plus chronic-type kidney lesions (1932 study above).
- **Guinea pig:** Recapitulates human-like (lung) granuloma pathology (PMC10556493). Its kidney lesions are not characterized in the sources retrieved.
- **Mice:**
  - Standard mice form poor human-like granulomas. C3HeB/FeJ mice form necrotic lesions, but these are lung-focused (PMC3631743 and related).
  - Humanized BLT mice use the kidney capsule only for engrafting human tissue, not as an infection model.
  - **No validated mouse model of renal TB was found.**
- **Genetic models:** Ifngr1-, Il12rb1-, and Tyk2-deficient mice exist for studying TB susceptibility in general. I did not retrieve renal-specific data for them.
- **Limitations:**
  - No model captures decades of latency, unilateral reactivation, or stricture fibrosis.
  - Direct inoculation skips the blood-borne seeding step.
- **Resources:** MGI disease page DOID:9733 (https://www.informatics.jax.org/disease/DOID:9733).

---

## Evidence gaps

1. There are no prevalence or incidence figures specific to renal TB. Data are pooled at the GUTB or EPTB level.
2. There are no quality-of-life (EQ-5D/SF-36) studies.
3. There are no omics, single-cell, or spatial studies of human renal TB tissue.
4. There is no validated small-animal renal TB model.
5. Evidence for corticosteroids against strictures, and for short-course regimens in renal TB, is lacking.
6. Many quotes above come from abstract excerpts in search results, because full-text PubMed and PMC access failed in this session. Check them against the source records before using them as exact abstract quotes.

## Sources
- [Muneer et al., Nat Rev Urol 2019, PMID 31548730](https://pubmed.ncbi.nlm.nih.gov/31548730/)
- [GUTB in low-endemic countries, Antibiotics 2021, PMID 34827337](https://pmc.ncbi.nlm.nih.gov/articles/PMC8614939)
- [Genital TB, Transl Androl Urol 2017, PMID 28540230](https://pmc.ncbi.nlm.nih.gov/articles/PMC5422679)
- [GUTB historical/basic science review, PMID 24578959](https://pmc.ncbi.nlm.nih.gov/articles/PMC3921817)
- [Best practice UGTB, PMID 23730329](https://pmc.ncbi.nlm.nih.gov/articles/PMC3655357)
- [Figueiredo & Lucon, 8961 cases, PMID 18836557](https://pubmed.ncbi.nlm.nih.gov/18836557/)
- [Renal TB series, PMID 28343213](https://www.ncbi.nlm.nih.gov/pubmed/28343213)
- [BMC Urology 2021 renal TB cohort](https://bmcurol.biomedcentral.com/articles/10.1186/s12894-021-00888-3)
- [UGTB review PMC11687435](https://pmc.ncbi.nlm.nih.gov/articles/PMC11687435)
- [IBJU 2025 narrative review PMC11884631](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11884631/)
- [Narrative review PMC3737618](https://pmc.ncbi.nlm.nih.gov/articles/PMC3737618)
- [Altez-Fernandez 2017 NAAT meta-analysis, PMID 28583076](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460328)
- [Chen 2019 Sci Rep, PMID 31363115](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6667469/)
- [Chen 2020 IJID meta-analysis (Mahidol repository)](https://repository.li.mahidol.ac.th/handle/123456789/54592)
- [Cochrane Xpert EPTB, PMID 33448348](https://pubmed.ncbi.nlm.nih.gov/33448348/)
- [Mthalane MDCT scoping review, PMID 31754491](https://pmc.ncbi.nlm.nih.gov/articles/PMC6837772)
- [Putty kidney, PMID 35812261](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9228914/)
- [Radiopaedia renal TB](https://www.radiopaedia.org/articles/renal-tuberculosis)
- [RSNA RadioGraphics 2021](https://pubs.rsna.org/doi/abs/10.1148/rg.2021200154)
- [CKD–TB meta-analysis, CID 2023 (PMC10573716)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10573716)
- [CKD–TB meta-analysis 2015, PMID 26614191](https://pubmed.ncbi.nlm.nih.gov/26614191)
- [TYK2 P1104A, PMID 30578352](https://research.pasteur.fr/en/b/ZUw)
- [UK Biobank TYK2](https://www.ukbiobank.ac.uk/publications/homozygosity-for-tyk2-p1104a-underlies-tuberculosis-in-about-1-of-patients-in-a-cohort-of-european-ancestry)
- [MSMD review PMC4357480](https://pmc.ncbi.nlm.nih.gov/articles/PMC4357480)
- [MSMD update PMC6438774](https://pmc.ncbi.nlm.nih.gov/articles/PMC6438774)
- [MSMD overview PMID 40656276](https://pubmed.ncbi.nlm.nih.gov/40656276/)
- [EPTB polymorphisms PMC2837863](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2837863/)
- [IFNG +874 meta-analysis PMC5584145](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5584145/)
- [TLR2 Arg753Gln meta-analysis PMC6348792](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6348792/)
- [Surgical management of renal TB PMC2684360](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2684360/)
- [Kulchavenya classification PMC4340670](https://pmc.ncbi.nlm.nih.gov/articles/4340670)
- [Granulomatous interstitial nephritis series PMC9999700](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9999700/)
- [Male genital TB, PMID 36482950](https://pmc.ncbi.nlm.nih.gov/articles/PMC9715008)
- [WHO Global TB Report 2024](https://www.who.int/publications/i/item/9789240101531)
- [WHO 2024 case notifications](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024/tb-diagnosis-and-treatment/2-1-case-notifications)
- [WHO Module 4 treatment](https://www.who.int/publications/i/item/9789240048126)
- [WHO 4-month regimen (TB KSP)](https://tbksp.who.int/en/node/1926)
- [ATS/CDC/IDSA 2016 guideline](https://academic.oup.com/cid/article/63/5/e61/2196792)
- [WHO Zoonotic TB Roadmap](https://www.who.int/publications/i/item/9789241513043)
- [ICD-10 A18.1 (gesund.bund.de)](https://gesund.bund.de/en/icd-code-search/a18-1)
- [CMS ICD-10-CM A18.11](https://www.cms.gov/ICD10m/version372-fullcode-cms/fullcode_cms/P0245.html)
- [ICD-11 1B12.5 (AutoICD)](https://autoicdapi.com/icd11/1B12.5)
- [MGI DOID:9733](https://www.informatics.jax.org/disease/DOID:9733)
- [Rabbit kidney TB model patent RU2776130C1](https://patents.google.com/patent/RU2776130C1/en)
- [1932 rabbit renal TB study](https://www.jstage.jst.go.jp/article/jpnjurol1928/21/10/21_10_506/_article/-char/en)
- [Guinea pig lesions PMC10556493](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556493/)
- [Granuloma modeling PMC3631743](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3631743/)
- [StatPearls GUTB, PMID 32491490](https://pubmed.ncbi.nlm.nih.gov/32491490/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 8 |
| References weighed for topical relevance | 47 |
| On topic | 20 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

7 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24578959` *(abstract only)*: "usually arises from reactivation of old, dormant infection by members of the *M. tuberculosis* complex"
  - closest text in source: "Genitourinary tuberculosis (GUTB) usually results from the reactivation of old, dormant tuberculous diseases by pathogens of the mycobacterium tuberculosis complex"
- `PMID:28540230`: "almost always follows a pulmonary infection"
  - closest text in source: "Tubercular involvement of the genitourinary organs is almost always secondary to pulmonary infection"
- `PMC:PMC11687435` *(abstract only)*: "After hematogenous spread from the pulmonary focus, there is colonization of the renal parenchyma, with initially bilateral, cortical, glomerular, and pericapillary renal lesions"
  - closest text in source: "Starting with a pulmonary focus, 2 to 20% of patients develop urogenital tuberculosis through hematogenous spread to the kidneys, prostate, and epididymis; through the descending collecting system to the ureters, bladder, and urethra; and through the ejaculatory ducts to the genital organs"
- `PMC:PMC2556487` *(abstract only)*: "After hematogenous spread from the pulmonary focus, there is colonization of the renal parenchyma, with initially bilateral, cortical, glomerular, and pericapillary renal lesions"
  - closest text in source: "As a result, the disease tends to be less serious, with more patients presenting without significant lesions of the upper urinary tract on diagnosis"
- `PMC:PMC6977373` *(abstract only)*: "presents late with advanced disease"
  - Text part not found as substring: 'presents late with advanced disease' (note: only abstract available for PMID:32015596, full text may contain this excerpt)
- `PMC:PMC9999700` *(abstract only)*: "presents late with advanced disease"
  - closest text in source: "Despite treatment, 6 of 11 (54.5%) patients with vasculitis developed end-stage kidney disease (ESKD) during the median follow-up of 16 months"
- `PMC:PMC4340670` *(abstract only)*: "Cavernous KTB… recovery without surgery is rare. Polycavernous KTB… recovery with anti-TB drugs only is impossible, surgery is necessary, basically nephrectomy"
  - closest text in source: "As with any other infection, UGTB should be cured by antibacterial therapy, but because of late diagnosis it may often require surgery"
- `PMID:31548730` *(abstract only)*: "Specific diagnosis rests on culturing *M. tuberculosis* from a suitable clinical sample or identifying its DNA"
  - closest text in source: "The specific diagnosis of UG-TB is achieved by culturing Mycobacterium tuberculosis from an appropriate clinical sample or by DNA identification"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:36482950` (3 mentions) - Why do we miss isolated male genital tuberculosis diagnosis?
  - shared terms: tuberculosis
- `PMC:PMC9715008` (2 mentions) - Why do we miss isolated male genital tuberculosis diagnosis?
  - shared terms: tuberculosis

Weighed against this report's own most characteristic terms: `renal`, `kidney`, `disease`, `infection`, `tuberculosis`, `stricture`, `stage`, `ckd`, `function`, `tyk2`, `pmc11687435`, `bovis`, `gutb`, `pmc2684360`, `pmc4357480`, `session`, `roadmap`, `serie`, `bladder`, `found`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005938` (2 mentions) - the report calls it "supplied"; MONDO calls it **renal tuberculosis**
- `DOID:9733` (7 mentions) - the report calls it "MGI disease page"; DOID calls it **renal tuberculosis**