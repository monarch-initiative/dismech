---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-31T16:35:21.898037'
end_time: '2026-10-31T16:39:21.677175'
duration_seconds: 239.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autoinflammation With Episodic Fever and Lymphadenopathy
  mondo_id: MONDO:0030018
  category: Mendelian
  causal_genes: RIPK1
  omim_id: OMIM:618852
  synonyms: AIEFL; Cleavage-Resistant Ripk1-Induced Autoinflammatory Syndrome; Cria
    Syndrome
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
  num_turns: 27
  total_cost_usd: 2.4889546
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 13
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 12
  on_topic: 8
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0030018
    reported_labels:
    - MONDO
    ontology_label: autoinflammation with episodic fever and lymphadenopathy
  - term_id: UBERON:0002372
    reported_labels:
    - Oral mucosa and tonsils
    ontology_label: tonsil
  - term_id: NCIT:C15986
    reported_labels:
    - Suggested NCIT treatment terms:** Pharmacotherapy
    ontology_label: Pharmacotherapy
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
- **Disease Name:** Autoinflammation With Episodic Fever and Lymphadenopathy
- **MONDO ID:** MONDO:0030018 (if available)
- **Causal gene(s):** RIPK1
- **OMIM:** OMIM:618852
- **Synonyms:** AIEFL; Cleavage-Resistant Ripk1-Induced Autoinflammatory Syndrome; Cria Syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autoinflammation With Episodic Fever and Lymphadenopathy** covering all of the
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

Fetching the primary abstracts verbatim so the quotes in the report are exact.

Checking the existing KB entry and its cached references, then I'll write the report.

Verifying the mouse-model papers, then writing.

I've written the full report below. The disease's existing knowledge-base entry, `kb/disorders/Autoinflammation_With_Episodic_Fever_And_Lymphadenopathy.yaml`, is a 16-line stub (name and MONDO term only), so almost all of this is new content.

Before using it:
- **Variant attribution.** The two founding *Nature* papers are easy to mix up, and the summarizing tool swapped them once during this research. Lalaoui et al. (PMID:31827281) reported D324N, D324H and D324Y in three families. Tao et al. (PMID:31827280) reported D324V and D324H in two families. That pairing is confirmed against both PubMed abstract pages.
- **Quotes.** Every quote is under 125 characters, and some come from the PMC full text (methods, figure legends) rather than the abstract. Re-check each against `references_cache/` after `just fetch-reference` before using it as a snippet.
- **Ontology IDs.** All HP, GO, CL, UBERON and HGNC identifiers are leads written from memory, not lookups. Each needs `runoak` or `just validate-terms` before binding. I deliberately left out NCIT drug codes.
- **Not reached.** I could not get the full text of the Tao et al. clinical tables (blocked by a captcha), the sirolimus case report (PDF not readable), the 2024 Indian case report, or an Orphanet record. Those details are marked as unverified in the report.

---

# Research report: Autoinflammation With Episodic Fever and Lymphadenopathy (AIEFL / CRIA syndrome)

**MONDO:0030018 · OMIM:618852 · Causal gene: *RIPK1* (receptor-interacting serine/threonine-protein kinase 1; HGNC:10019, to verify)**

## 1. Disease information

**Overview.** This disease is caused by **heterozygous, dominantly acting variants in *RIPK1*** that stop caspase-8 from cutting the RIPK1 protein. It is usually called **CRIA syndrome** (cleavage-resistant RIPK1-induced autoinflammatory syndrome). It starts in infancy or early childhood with recurrent fevers every 2–4 weeks, each lasting about 1–7 days, and severe, often painful lymph-node swelling during flares. Some patients also have an enlarged spleen or liver, mouth ulcers, abdominal pain, tonsillitis and joint pain.

Two papers described it at the same time in *Nature* in January 2020 (published online December 2019):
- **Lalaoui et al.**, PMID:31827281: "heterozygous missense mutations p.D324N, p.D324H and p.D324Y prevent caspase cleavage of RIPK1 in humans". Seven affected people in three families.
- **Tao et al.**, PMID:31827280: "we identify two families with variants in RIPK1 (D324V and D324H)".

**Distinct from a different RIPK1 disease.** Biallelic loss-of-function *RIPK1* variants cause **recessive RIPK1 deficiency**, also called Immunodeficiency 57 with or without autoinflammation (OMIM:618108). That is a combined immunodeficiency with early-onset inflammatory bowel disease and arthritis, and it is not this disease. A 2021 review states that "RIPK1 loss-of-function (LoF) mutations and cleavage-deficient mutations have been identified in humans" (Zhang et al., PMID:34163478). In 2026 two further RIPK1 conditions were reported that should also be kept separate:
- compound-heterozygous K377E/R390G with CD8+ T-cell death (Dai et al., PMID:41813671);
- a heterozygous kinase-domain variant (D24V) with immunodeficiency and autoimmunity (Parentelli et al., PMID:41760196).

**Identifiers**

| Source | ID |
|---|---|
| MONDO | MONDO:0030018 |
| OMIM | 618852 |
| Orphanet | Not confirmed; no ORPHA code found in search or in the local `references_cache` |
| ICD-10 / ICD-11 / MeSH | None specific. Usual umbrella: ICD-10 M04.8 / ICD-11 4A60 (autoinflammatory syndromes), to verify |

**Synonyms:** AIEFL; CRIA syndrome; cleavage-resistant RIPK1-induced autoinflammatory syndrome; RIPK1-associated autoinflammatory disease, dominant.

**Data source.** All knowledge comes from published case series and family studies: about 5 families in the founding papers, plus single families and cases since. There are no registry or EHR data.

## 2. Etiology

- **Cause:** a single germline genetic variant. Monoallelic missense changes at or next to the caspase-8 cleavage site of RIPK1 (Asp324, which is Asp325 in mouse) make the protein resistant to cleavage.
- **Genetic risk:** the D324 variants (N, H, Y, V, G) and L321R. Tapiz i Reula et al. (PMID:35716229) reported "two novel heterozygous RIPK1 variants at the caspase-8 cleavage site (p.Leu321Arg and p.Asp324Gly)". These variants "were resistant to caspase-8-mediated cleavage and induced a constitutive activation of necroptotic pathway."
- **Modifiers:** none identified. An asymptomatic carrier sibling has been reported (see section 9), which suggests modifiers or incomplete penetrance exist but are uncharacterized.
- **Environmental and protective factors:** none documented. Flares are episodic, but no specific triggers such as infection or stress are established. In the heterozygous mouse, TLR ligands (LPS, poly(I:C)) bring out excess cytokine production, which suggests infections or microbial products could trigger flares. That is an inference from mice and has not been shown in patients.
- **Gene–environment interaction:** not studied in humans.

## 3. Phenotypes

Frequencies below are from the founding cohort of 7 patients in Lalaoui et al. (PMID:31827281). The HPO IDs are suggestions to verify.

| Phenotype | HPO (verify) | Frequency | Notes |
|---|---|---|---|
| Recurrent fever | HP:0001954 | 7/7 | Starts at birth or in infancy (one at 6 months); every 2–4 weeks; lasts 1–7 days; peaks at 38.9–41 °C |
| Lymphadenopathy | HP:0002716 | 7/7 | Cervical, axillary, inguinal or periaortic; often painful during flares |
| Oral ulcers | HP:0000155 | 5/7 | |
| Splenomegaly | HP:0001744 | 4/7 | |
| Abdominal pain | HP:0002027 | 4/7 | |
| Tonsillitis | HP:0011110 | 3/7 | |
| Arthralgia | HP:0002829 | 3/7 | No arthritis |
| Hepatomegaly | HP:0002240 | 2/7 | |
| Raised CRP / ESR | HP:0011227 / HP:0003565 | Common, even between flares | e.g. ESR 50 mm/h, CRP 30.4 mg/L at baseline in one patient |
| Raised serum IL-6 | (verify) | Reported | Chougule et al., PMID:37452601 |
| Raised serum amyloid A | (verify) | Reported in one family | No kidney dysfunction |
| Steroid-responsive nephrotic syndrome | HP:0000100 | 1 case report | PMID:37452601. Whether it is part of the disease is uncertain |
| Failure to thrive; microcytic hypochromic anemia | HP:0001508; HP:0001935 | 1 case report | PMID:37452601 |
| Sweet-like neutrophilic dermatosis with shock in infancy | (verify) | 1 case report | Hernández Sánchez et al., PMID:42547316. The diagnosis of CRIA in this case is not clear from the abstract |

**Absent in the founding cohort:** rash, genital ulcers, arthritis and organ damage. Lalaoui et al. report "there were no signs of rash, arthritis, genital ulcers or end-stage organ damage" and "the condition was not life-threatening in any of the patients."

**Course:** episodic and lifelong. Severity varies within families: Chougule et al. note the family "showed variability with respect to frequency and duration of periodic fever".

**Quality of life:** no formal measures have been published. Frequent febrile flares with painful lymph nodes plausibly disrupt school and work.

## 4. Genetic and molecular information

- **Gene:** *RIPK1*, 6p25.2 (OMIM gene *603453*, to verify). The protein has an N-terminal kinase domain, an intermediate domain (which contains the D324 cleavage site and the RHIM motif) and a C-terminal death domain.

**Reported variants** (all heterozygous germline missense; all functionally shown to resist caspase-8 cleavage):

| Variant | Reference |
|---|---|
| p.Asp324Asn (D324N) | Lalaoui 2020 |
| p.Asp324His (D324H; c.970G>A per Chougule) | Lalaoui 2020; Tao 2020; Chougule 2024; Cattalini 2025 |
| p.Asp324Tyr (D324Y) | Lalaoui 2020 |
| p.Asp324Val (D324V) | Tao 2020 |
| p.Asp324Gly (D324G) | Tapiz i Reula 2022 |
| p.Leu321Arg (L321R) | Tapiz i Reula 2022 |

- **Functional consequence:** a neomorphic or gain-of-function effect. The cleavage that normally switches RIPK1 off fails, so the full-length active protein persists and drives cell death and cytokine production. This is the opposite of the loss of function in recessive RIPK1 deficiency.
- **ClinVar classification, gnomAD frequency, ClinGen validity:** not checked. The D324 variants are expected to be absent or ultra-rare in gnomAD.
- **De novo cases:** a de novo p.Asp324His case is reported (Cattalini et al., PMID:39557292; seen in a search-result snippet only, not verified in full text).
- **Epigenetic or chromosomal findings:** none.

## 5. Environmental information

No environmental, lifestyle or infectious cause is known. The flare triggers are uncharacterized (see section 2).

## 6. Mechanism and pathophysiology

**Causal chain**

1. A heterozygous *RIPK1* missense variant at Asp324 (or Leu321) **removes or disrupts the caspase-8 cleavage site**.
2. This **blocks caspase-8 (and caspase-6) cleavage of RIPK1**. In normal cells that cleavage separates the kinase domain from the intermediate and death domains, which ends RIPK1 signaling.
3. Uncleaved, kinase-competent RIPK1 **persists in TNFR1 complex II (the ripoptosome)** after TNF or TLR signaling. This **increases caspase-8 activation (apoptosis)** and **RIPK3–MLKL activation (necroptosis)**. Patient blood cells are "sensitized … to RIPK1 activation, apoptosis and necroptosis induced by TNF" (Tao et al.).
4. Myeloid cells **die more readily and release cytokines and alarmins**: TNF, IL-1β and especially **IL-6**, plus chemokines. Patient cells show "overproduction of inflammatory cytokines and chemokines". In mice, the extra cytokine production depended on RIPK3 and caspase-8, and Lalaoui et al. argue that cell death (mainly apoptosis), not altered NF-κB or MAPK signaling, drives it.
5. These cytokines **cause systemic inflammation**: fever, a raised acute-phase response (CRP, ESR, serum amyloid A) and **lymphoid hyperplasia** (lymphadenopathy, splenomegaly). The link from the cytokines to lymph-node enlargement is inferred and has not been dissected directly.
6. **Branch in fibroblasts:** patient fibroblasts had **lower RIPK1 levels** and resisted some death pathways (Tao et al.). The disease therefore looks like a problem of hematopoietic cells, and bone-marrow chimera experiments in mice transferred the hyper-responsiveness with the marrow (Lalaoui et al.).
7. **Branch in therapy response:** IL-6 sits furthest downstream and is the most clinically relevant mediator. Tocilizumab works, while TNF and IL-1 blockade mostly fail (section 12).

**Evidence from mouse genetics**
- Homozygous *Ripk1*^D325A^ mice die mid-gestation (E10.5–E11.5) with hemorrhage. Newton et al. (PMID:31511692): "mice that express RIPK1(D325A) … died mid-gestation." Lalaoui et al.: "Embryonic lethality was completely prevented by combined loss of Casp8 and Ripk3".
- Kinase-dead D138N/D325A mice survive to birth but die around weaning from RIPK3-dependent inflammation.
- Heterozygous *Ripk1*^D325A/+^ mice are viable but "hyper-responsive to inflammatory stimuli in vivo".

**Ontology suggestions (all to verify)**
- GO biological processes: necroptotic process GO:0070266; extrinsic apoptotic signaling pathway GO:0097191; tumor necrosis factor-mediated signaling pathway GO:0033209; inflammatory response GO:0006954; interleukin-6 production GO:0032635.
- GO cellular components: ripoptosome GO:0097342; cytosol.
- CL cell types: monocyte CL:0000576; macrophage CL:0000235; PBMC (no single CL term, so use monocyte or lymphocyte); fibroblast CL:0000057 (the branch with reduced RIPK1).

**Omics:** no transcriptomic, single-cell or other omics datasets specific to this disease were found.

## 7. Anatomical structures affected

- Lymph nodes (UBERON:0000029) and spleen (UBERON:0002106); liver (UBERON:0002107) in some patients.
- Oral mucosa and tonsils (UBERON:0002372); joints (pain only).
- Systems: immune and hematopoietic. Kidney is involved in one case only (nephrotic syndrome).
- Main cells involved: myeloid cells derived from the bone marrow.

## 8. Temporal development

- **Onset:** neonatal to infant (from birth to about 6 months); one onset at 5 months (Chougule et al.).
- **Course:** episodic and lifelong. Patients have been documented from 10 to 82 years of age at evaluation.
- **Remission:** no spontaneous remission is reported. Disease control comes from treatment, mainly IL-6 blockade.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). De novo cases occur.
- **Penetrance:** probably incomplete (HP:0003829, to verify). Chougule et al. report "P1's asymptomatic younger brother had the same mutation." Expressivity is variable.
- **Prevalence:** unknown. It is ultra-rare, with roughly a dozen families or fewer published.
- **Families reported so far:** Australia/UK/US (Lalaoui), China (Tao), Spain (Tapiz i Reula), India (Chougule 2024; Gangadharan 2024, a D324N case), Italy (Cattalini 2025) and Spain (Hernández Sánchez 2026).
- **Sex ratio:** no sex bias is expected.
- **Founder effects:** none known.

## 10. Diagnostics

- **Genetic testing is diagnostic.** Use an autoinflammatory/periodic-fever gene panel that includes *RIPK1*, or exome or genome sequencing. Look for a heterozygous variant at codons 321–324.
- **Functional confirmation for a new variant:** test whether the protein resists caspase-8 cleavage in vitro, and whether patient cells are more sensitive to TNF-induced death or show raised pRIPK1/pMLKL (as in Tapiz i Reula et al.).
- **Laboratory tests:** CRP, ESR, serum amyloid A and IL-6, which can be raised even between flares.
- **Imaging and biopsy:** ultrasound or CT shows lymphadenopathy and splenomegaly. Lymph-node biopsy is mainly used to exclude lymphoma; reactive hyperplasia is expected (not formally described).
- **Differential diagnosis:**
  - PFAPA, which is not familial and in which ulcers and pharyngitis dominate;
  - HIDS/mevalonate kinase deficiency (MVK; lymphadenopathy, urinary mevalonate);
  - TRAPS (TNFRSF1A);
  - FMF (MEFV);
  - recessive RIPK1 deficiency (immunodeficiency plus IBD);
  - autoimmune lymphoproliferative syndrome (ALPS);
  - Castleman disease;
  - lymphoma.
- **Screening:** cascade testing of relatives. There is no newborn screening.

## 11. Outcome and prognosis

- Not life-threatening in the founding cohort, and no organ damage reported. Life expectancy appears normal: one patient was evaluated at 82.
- The theoretical long-term risk is AA amyloidosis, given chronically raised serum amyloid A. It has not been reported.
- Morbidity comes from frequent flares and the side effects of corticosteroids.

## 12. Treatment

Responses below are from Lalaoui et al. unless another source is named.

| Agent | Response |
|---|---|
| Glucocorticoids (prednisone) | Acute relief, but flares are not prevented |
| Colchicine | No response in 1 patient (Lalaoui); fever intensity reduced but not eliminated in 2 patients (Chougule, PMID:37452601) |
| Anakinra (IL-1 receptor antagonist) | No response (Lalaoui); early improvement then relapse in an infant (Hernández Sánchez, PMID:42547316) |
| Etanercept (TNF blocker) | Mostly no response; partial in 1 patient |
| **Tocilizumab (IL-6 receptor antagonist)** | **Best evidence.** "responded to the IL-6 inhibitor tocilizumab but failed to respond to TNF inhibitors" (Lalaoui); sustained control in the 2026 case. Two patients stopped because of side effects (worse oral ulcers, hand pain) |
| Sirolimus | Proposed as a possible treatment in a case report (Cattalini, PMID:39557292); details not verified |
| RIPK1 kinase inhibitors | A logical mechanism-based option, but no clinical trial in CRIA was found |

- **Suggested NCIT treatment terms:** Pharmacotherapy (NCIT:C15986) with the drug in `therapeutic_agent`. Tocilizumab is a monoclonal antibody (`therapeutic_modality: MONOCLONAL_ANTIBODY`). Verify the NCIT and CHEBI codes before binding.
- **Gene, cell or RNA therapy:** none.
- **Clinical trials:** no NCT trials specific to CRIA were found.

## 13. Prevention

- No primary prevention.
- Genetic counseling: each child of an affected parent has a 50% risk of inheriting the variant.
- Cascade testing of relatives. Prenatal or preimplantation testing is technically feasible.
- Monitor serum amyloid A and urinary protein to catch amyloidosis early (by analogy with other periodic fever syndromes).

## 14. Other species

No naturally occurring disease is recorded in OMIA. The cleavage site is conserved: human Asp324 corresponds to mouse Asp325 (mouse *Ripk1* is NCBI Gene 19766, to verify).

## 15. Model organisms

| Model | Phenotype | Relevance |
|---|---|---|
| Mouse *Ripk1*^D325A/D325A^ | Dies at about E10.5 with hemorrhage; rescued by *Casp8*^−/−^ plus *Ripk3*^−/−^ | Shows that cleavage is essential (PMID:31511692, 31827281) |
| Mouse *Ripk1*^D325A/+^ (Lalaoui) | Viable; raised serum TNF and IL-1β after LPS or poly(I:C); BMDMs over-respond; the trait transfers with bone marrow | **Best model of the heterozygous human disease**, but the mice have no spontaneous fevers or lymphadenopathy (partial recapitulation) |
| Mouse *Ripk1*^D138N/D325A^ | Dies around weaning from RIPK3-dependent inflammation | Shows the disease needs RIPK1 kinase activity |
| MEFs carrying D325V or D325H (Tao) | More apoptosis and necroptosis; induce IL-6 and TNF | In vitro model |
| Patient PBMCs and fibroblasts | PBMCs are sensitized to death; fibroblasts have reduced RIPK1 | Human ex vivo model |

**Limitations:** the mice do not reproduce periodic fever, and the human IL-6-dominant response is not modeled well.

---

**Sources**
- [Lalaoui 2020, PMID:31827281](https://pubmed.ncbi.nlm.nih.gov/31827281/) · [PMC6930849](https://pmc.ncbi.nlm.nih.gov/articles/PMC6930849)
- [Tao 2020, PMID:31827280](https://pubmed.ncbi.nlm.nih.gov/31827280/)
- [Tapiz i Reula 2022, PMID:35716229](https://pubmed.ncbi.nlm.nih.gov/35716229/)
- [Chougule 2024, PMID:37452601](https://pubmed.ncbi.nlm.nih.gov/37452601/)
- [Cattalini 2025, PMID:39557292](https://pubmed.ncbi.nlm.nih.gov/39557292/)
- [Hernández Sánchez 2026, PMID:42547316](https://pubmed.ncbi.nlm.nih.gov/42547316/)
- [Dai 2026, PMID:41813671](https://pubmed.ncbi.nlm.nih.gov/41813671/)
- [Parentelli 2026, PMID:41760196](https://pubmed.ncbi.nlm.nih.gov/41760196/)
- [Zhang 2021, PMID:34163478](https://pubmed.ncbi.nlm.nih.gov/34163478/)
- [Newton 2019, PMID:31511692](https://pubmed.ncbi.nlm.nih.gov/31511692/)
- [Gangadharan 2024, Indian J Pediatr](https://link.springer.com/article/10.1007/s12098-023-04831-2)
- [Altmeyer CRIA overview](https://www.altmeyers.org/en/internal-medicine/cria-syndrome-161640)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030018` (2 mentions) - the report calls it "MONDO"; MONDO calls it **autoinflammation with episodic fever and lymphadenopathy**
- `UBERON:0002372` (1 mention) - the report calls it "Oral mucosa and tonsils"; UBERON calls it **tonsil**
- `NCIT:C15986` (1 mention) - the report calls it "Suggested NCIT treatment terms:** Pharmacotherapy"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011110` (1 mention) - the report calls it "Tonsillitis"; HP calls it **Recurrent tonsillitis**
- `HP:0000100` (1 mention) - the report calls it "Steroid-responsive nephrotic syndrome"; HP calls it **Nephrotic syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.