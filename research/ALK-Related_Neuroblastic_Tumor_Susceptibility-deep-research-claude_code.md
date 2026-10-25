---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-10-22T18:47:00.162642'
end_time: '2026-10-22T19:04:25.279527'
duration_seconds: 1045.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ALK-Related Neuroblastic Tumor Susceptibility
  mondo_id: MONDO:0013083
  category: ''
  causal_genes: ALK
  omim_id: OMIM:613014
  synonyms: ALK neuroblastoma; neuroblastoma caused by mutation in ALK; neuroblastoma,
    susceptibility to, type 3
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
  - claude-opus-5[1m]
  web_search_requests: 10
  num_turns: 69
  total_cost_usd: 6.783425000000002
  session_id: 72f36e43-01e2-48cc-9211-a0b8b36241c8
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 36
reference_validation:
  total_references: 61
  verified: 60
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 4
  relevance_assessed: 60
  on_topic: 31
  validator_version: 0.3.0
term_validation:
  total_terms: 105
  verified: 104
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0002107
    reported_labels:
    - Liver (stage MS/4S)
    ontology_label: liver
  labels_variant: 7
  unresolvable_prefixes:
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALK-Related Neuroblastic Tumor Susceptibility
- **MONDO ID:** MONDO:0013083 (if available)
- **Causal gene(s):** ALK
- **OMIM:** OMIM:613014
- **Synonyms:** ALK neuroblastoma; neuroblastoma caused by mutation in ALK; neuroblastoma, susceptibility to, type 3
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ALK-Related Neuroblastic Tumor Susceptibility** covering all of the
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

I'll research this now. Loading web tools and checking local ontology caches in parallel.

# ALK-Related Neuroblastic Tumor Susceptibility — Comprehensive Research Report

**Target entity:** ALK-Related Neuroblastic Tumor Susceptibility
**MONDO:** MONDO:0013083 — *neuroblastoma, susceptibility to, 3* (CURIE and label verified against the repository's local MONDO term cache, `cache/mondo/terms.csv`, 2026-10-22)
**OMIM phenotype:** 613014 (NBLST3) · **OMIM gene:** 105590 (*ALK*)
**Causal gene:** ***ALK*** (anaplastic lymphoma kinase receptor tyrosine kinase), HGNC `hgnc:427` (verified in `cache/hgnc/terms.csv`)
**Report date:** 22 October 2026

> **Gene-identity check.** This report is about germline activating variants in the ***ALK*** receptor tyrosine kinase gene at chromosome 2p23. The serial-numbered synonym "neuroblastoma, susceptibility to, 3" (NBLST3) is easy to confuse with the sibling OMIM loci NBLST1 (2p, non-*ALK*) and **NBLST2 (OMIM 613013, *PHOX2B*)**, which is a different gene and a different predisposition syndrome (associated with Hirschsprung disease and congenital central hypoventilation syndrome). Everything below is anchored on *ALK* / MONDO:0013083 / OMIM 613014.

> **Citation and CURIE discipline.** Ontology identifiers in this report fall into two classes, and they are labelled: **[verified]** = resolved during this session against the repository's committed term caches or the EBI OLS4 API; **[lead]** = named from the literature or recall and **not** resolved — these must be looked up before being written into any KB record. Abstract quotations marked "verbatim" were retrieved through the Europe PMC REST API in this session. PubMed's own pages and the NCBI Bookshelf were not retrievable (cookie wall / reCAPTCHA), so where I rely on GeneReviews chapter body text rather than its retrieved summary, I say so explicitly.

---

## 1. Disease Information

### 1.1 Overview

ALK-related neuroblastic tumor susceptibility is an autosomal dominant, incompletely penetrant cancer predisposition syndrome caused by heterozygous **germline gain-of-function missense variants in the tyrosine kinase domain of *ALK***. It is the principal genetic cause of **familial neuroblastoma**. Carriers are at increased risk of the full spectrum of **neuroblastic tumours** — neuroblastoma, ganglioneuroblastoma and ganglioneuroma — with risk concentrated in infancy and early childhood and a strong tendency to **multifocal and bilateral primary tumours**.

The authoritative clinical description is the GeneReviews chapter *ALK-Related Neuroblastic Tumor Susceptibility* (Greengard EG, Perrino MR, Park JR; GeneReviews®, University of Washington, Seattle; **PMID:20301782**, Bookshelf ID **NBK24599**). Retrieved verbatim:

> "ALK-related neuroblastic tumor susceptibility is characterized by increased risk for neuroblastic tumors including neuroblastomas, ganglioneuroblastomas, and ganglioneuromas. Neuroblastomas are a more malignant tumor and ganglioneuromas a more benign tumor. Depending on the histologic findings, ganglioneuroblastomas can behave in a more aggressive fashion, like neuroblastomas, or in a benign fashion, like ganglioneuromas. The overall penetrance of a germline ALK pathogenic variant is approximately 50%, with the risk for neuroblastic tumor development highest in infancy and decreasing by late childhood." (PMID:20301782)

A critical conceptual point for knowledge-base modelling: **this entity is a *susceptibility* state, not the tumour itself.** The germline variant is necessary but not sufficient; tumour formation requires cooperating somatic events, most prominently *MYCN* amplification (see §6).

### 1.2 Key identifiers

| Resource | Identifier | Status |
|---|---|---|
| Mondo | MONDO:0013083 — *neuroblastoma, susceptibility to, 3* | **[verified]** local cache |
| OMIM (phenotype) | 613014 — NEUROBLASTOMA, SUSCEPTIBILITY TO, 3; NBLST3 | as supplied in the brief |
| OMIM (gene) | 105590 — *ALK* RECEPTOR TYROSINE KINASE | **[lead]** |
| HGNC | `hgnc:427` — *ALK* | **[verified]** local cache |
| MedGen | C2751681 — "Neuroblastoma, susceptibility to, 3" | **[lead]**, from NCBI MedGen search result |
| GeneReviews | NBK24599 / PMID:20301782 | **[verified]** via Europe PMC |
| UniProt | Q9UM73 (ALK_HUMAN) | **[lead]**, not re-resolved this session |
| ICD-10 | Neuroblastoma is coded by site (e.g. C74.9 adrenal, C47.x peripheral nerves/autonomic); **no code exists for the predisposition state** | **[lead]** — the repository's `cache/icd10cm/terms.csv` contains no neuroblastoma row |
| ICD-O-3 morphology | 9500/3 neuroblastoma NOS; 9490/3 ganglioneuroblastoma; 9490/0 ganglioneuroma | **[lead]**, must be verified before use |
| MeSH | Neuroblastoma D009447; Anaplastic Lymphoma Kinase D000071436 | **[lead]** |

### 1.3 Synonyms

ALK neuroblastoma; neuroblastoma caused by mutation in ALK; neuroblastoma, susceptibility to, type 3 (NBLST3); hereditary neuroblastoma (when *ALK*-driven); familial neuroblastoma, *ALK*-related; ALK-related neuroblastic tumour predisposition.

### 1.4 Nature of the evidence base

Essentially all information is **aggregated disease-level** — pedigree-based linkage and segregation studies, cooperative-group tumour-sequencing cohorts (COG/TARGET, SIOPEN, the French *Société Française de Cancérologie de l'Enfant* series), clinical-trial cohorts, and registry/consensus guideline documents. Individual-patient EHR-derived evidence is confined to small case series and single-family reports (e.g. the mother-and-daughter kindred in PMID:40294355). There is **no** population-based registry of germline *ALK* carriers, which is the main reason penetrance estimates remain coarse.

---

## 2. Etiology

### 2.1 Primary causal factor

A **heterozygous germline activating missense variant in the *ALK* tyrosine kinase domain**, inherited from a (often unaffected) parent or arising de novo. The founding observation, Mossé et al., *Nature* 2008 (PMID:18724359), abstract verbatim:

> "Here we show that germline mutations in the anaplastic lymphoma kinase (ALK) gene explain most hereditary neuroblastomas, and that activating mutations can also be somatically acquired. We first identified a significant linkage signal at chromosome bands 2p23-24 using a whole-genome scan in neuroblastoma pedigrees. Resequencing of regional candidate genes identified three separate germline missense mutations in the tyrosine kinase domain of ALK that segregated with the disease in eight separate families."

and:

> "Our results demonstrate that heritable mutations of ALK are the main cause of familial neuroblastoma, and that germline or acquired activation of this cell-surface kinase is a tractable therapeutic target for this lethal paediatric malignancy." (PMID:18724359)

Independently and concurrently, Janoueix-Lerosey et al., *Nature* 2008 (PMID:18923523) verbatim: *"Germline mutations were observed in two neuroblastoma families, indicating that ALK is a neuroblastoma predisposition gene."*

### 2.2 Genetic risk factors

**(a) The causal germline variants.** Three variants were identified in the original eight linked pedigrees — **G1128A, R1192P and R1275Q** — all in the kinase domain. A fourth, **T1151M**, was described in the same body of work. Bourdeaut et al., *Eur J Hum Genet* 2012 (PMID:22071890), found three germline *ALK* variants in a selected French series, verbatim:

> "We found three ALK germline mutations, all in a context of multifocal tumours. Two mutations (T1151R and R1192P) were inherited and shared by several unaffected patients, thus illustrating an incomplete penetrance. Younger age at tumour onset did not seem to offer a relevant selection criterion for ALK analyses. Conversely, multifocal tumours might be the most to benefit from the genetic screening." (PMID:22071890)

**(b) Cooperating somatic lesions** — the dominant modifier of whether a carrier develops a tumour (see §4.3 and §6): ***MYCN* amplification** (`hgnc:7559` **[verified]**), 17q gain, 1p36 and 11q loss, and *ALK* copy-number gain/amplification in cis.

**(c) Common polygenic susceptibility alleles**, which act on the same developmental programme and plausibly modify penetrance in a carrier. The best-characterised is the *LMO1* super-enhancer polymorphism **rs2168101 G>T** (Oldridge et al., *Nature* 2015, PMID:26560027; verbatim: *"SNP rs2168101 G>T is the most highly associated variant (combined P = 7.47 × 10(-29), odds ratio 0.65, 95% confidence interval 0.60-0.70), and resides in a super-enhancer defined by extensive acetylation of histone H3 lysine 27 within the first intron of LMO1"*). Weichert-Leahey et al., *J Clin Invest* 2023 (PMID:37183825) showed mechanistically that the protective TATA allele *"reduced the penetrance of MYCN-driven tumors, which were restricted to the mesenchymal cell state."*

**(d) Other germline cancer-predisposition genes** are enriched in unselected neuroblastoma, chiefly ***BARD1*** (`hgnc:952` **[verified]**). Kim et al., *JNCI* 2024 (PMID:37688579), verbatim: *"We observed 116 pathogenic or likely pathogenic variants involving 13.9% (109 of 786) of neuroblastoma patients, representing a statistically significant excess burden compared with cancer-free participants (odds ratio [OR] = 1.60, 95% confidence interval [CI] = 1.27 to 2.00). BARD1 harbored the most statistically significant enrichment of pathogenic or likely pathogenic variants (OR = 32.30, 95% CI = 6.44 to 310.35)."* These are **separate predisposition mechanisms**, not modifiers of *ALK* per se, but they matter for differential diagnosis and for panel design.

### 2.3 Environmental risk factors

**No established environmental risk factor modifies risk in *ALK* carriers.** Neuroblastoma in general has no reproducible environmental cause; candidate exposures studied in sporadic disease (parental occupational exposures, maternal medication use, assisted reproduction) have not produced consistent associations, and none has been studied in a germline-*ALK* population. Non-genetic risk determinants that *are* established are demographic rather than environmental: **age** (risk is highest in infancy and falls through childhood — GeneReviews, PMID:20301782) and **family history**.

**Explicit gap:** I found no study of environmental modifiers of penetrance in *ALK* carriers. Any environmental claim in a KB entry would be unsupported.

### 2.4 Protective factors

- **Genetic:** the *LMO1* intron-1 **TATA (T) allele** at rs2168101 is protective for neuroblastoma generally (OR 0.65; PMID:26560027) and reduces tumour penetrance in a *MYCN*-driven zebrafish model (PMID:37183825). Whether it modifies penetrance specifically in germline-*ALK* carriers has **not** been tested.
- **Environmental:** none identified.
- A mechanistically interesting case is the germline *ALK* **I1250T** variant, reported to be a **kinase-dead** allele rather than an activating one — i.e. not all germline *ALK* kinase-domain substitutions are oncogenic. **[lead — attributed to Schönherr et al., *Biochem J* 2011; not retrieved or verified this session.]**

### 2.5 Gene–environment interactions

No documented gene–environment interaction. The interaction that governs this disease is **gene–gene**: germline *ALK* activation × somatic *MYCN* amplification (§6.3). This is the single most important "two-factor" statement the KB entry should carry, and it is well evidenced in three independent animal systems (PMID:22789543, PMID:22439933, PMID:22764207).

---

## 3. Phenotypes

The phenotype of the *susceptibility state* is tumour occurrence plus, rarely, a developmental neurological phenotype. There is **no constitutional dysmorphic or syndromic phenotype** in the typical case — unaffected obligate carriers are clinically normal.

### 3.1 Core tumour phenotypes

| Phenotype | HPO term | Status | Type | Onset | Frequency / notes |
|---|---|---|---|---|---|
| Neuroblastoma | **HP:0003006** *Neuroblastoma* | **[verified]** cache | Neoplasm | Congenital–early childhood | The dominant manifestation; overall penetrance of any neuroblastic tumour ≈50% (PMID:20301782) |
| Ganglioneuroblastoma | **HP:0006747** *Ganglioneuroblastoma* | **[verified]** OLS4 | Neoplasm | Childhood | Intermediate behaviour; "can behave in a more aggressive fashion, like neuroblastomas, or in a benign fashion, like ganglioneuromas" (PMID:20301782) |
| Ganglioneuroma | **HP:0003005** *Ganglioneuroma* | **[verified]** cache | Neoplasm | Childhood–adult | Benign; "typically removed by surgical resection and require no further therapy" (PMID:20301782) |
| Neuroblastic tumour (umbrella) | **HP:0004376** *Neuroblastic tumor* | **[verified]** OLS4 | Neoplasm | — | Useful as the parent node for the tumour spectrum |

**Multifocality and bilaterality are the clinical hallmark that should raise suspicion of germline *ALK*.** Bourdeaut et al. found all three germline variants in multifocal cases and concluded *"multifocal tumours might be the most to benefit from the genetic screening"* (PMID:22071890). The 2024 AACR workshop update quantifies the background rate: *"3% to 4% of cases present with bilateral or multifocal primary tumors"* (Kamihara et al., *Clin Cancer Res* 2024, PMID:38860978, verbatim). There is no single HPO term for "multifocal primary neuroblastoma"; in a KB entry this is best carried as a `description`/qualifier on the neuroblastoma phenotype rather than bound to an invented term.

### 3.2 Tumour-derived clinical signs and symptoms (site-dependent)

These are the manifestations of the neuroblastic tumour itself, not of the germline state, and their presence depends entirely on primary site and stage.

| Manifestation | HPO term | Status |
|---|---|---|
| Abdominal mass (commonest presentation; adrenal/retroperitoneal primary) | **HP:0031500** *Abdominal mass* | **[verified]** |
| Hepatomegaly (stage MS/4S liver infiltration in infants) | **HP:0002240** *Hepatomegaly* | **[verified]** |
| Spinal cord compression ("dumbbell" paraspinal tumour through neural foramina) | **HP:0002176** *Spinal cord compression* | **[verified]** |
| Paraplegia | **HP:0010550** *Paraplegia* | **[verified]** |
| Horner syndrome (cervical/apical thoracic primary) | **HP:0002277** *Horner syndrome* | **[verified]** |
| Hypertension (catecholamine secretion / renovascular compression) | **HP:0000822** *Hypertension* | **[verified]** |
| Proptosis and periorbital ecchymosis ("raccoon eyes", orbital metastasis) | **HP:0000520** *Proptosis*; periorbital ecchymosis **[lead]** | partial |
| Bone pain (cortical bone metastasis) | **HP:0002653** *Bone pain* | **[verified]** |
| Anaemia; thrombocytopenia (marrow infiltration) | **HP:0001903**; **HP:0001873** | **[verified]** |
| Failure to thrive | **HP:0001508** *Failure to thrive* | **[verified]** |
| Secretory diarrhoea (VIP-secreting tumours, typically ganglioneuroblastoma/ganglioneuroma) | **HP:0002014** *Diarrhea* | **[verified]** |
| Opsoclonus–myoclonus (paraneoplastic) | **HP:0010543** *Opsoclonus*; **HP:0001336** *Myoclonus*; **HP:0001251** *Ataxia* | **[verified]** |
| Scoliosis (late effect / paraspinal mass) | **HP:0002650** *Scoliosis* | **[verified]** |

### 3.3 Laboratory abnormalities

| Finding | HPO term | Status | Note |
|---|---|---|---|
| Elevated urinary homovanillic acid (HVA) | **HP:0011977** | **[verified]** | The screening analyte pair named in the GeneReviews surveillance protocol |
| Elevated urinary vanillylmandelic acid (VMA) | **HP:0011978** | **[verified]** | idem |

LOINC codes for urine HVA and VMA exist but were **not** resolved this session; per repository policy a LOINC code must be read from an authority in the same step it is written, so none is offered here.

### 3.4 The rare severe developmental phenotype (germline-specific)

A distinct and important observation: a **small number of de novo germline *ALK* variants produce a severe congenital neurological syndrome** in addition to neuroblastoma. de Pontual et al., *Hum Mutat* 2011 (PMID:21681106 is a different paper; the correct identifier is **PMID:21972109**), abstract verbatim:

> "Here we report a novel syndromic presentation associating congenital NB with severe encephalopathy and abnormal shape of the brainstem on brain MRI in two unrelated sporadic cases harboring de novo, germline, heterozygous ALK gene mutations. Both mutations are gain-of-function mutations that have been reported in NB and NB cell lines. These observations further illustrate the role of oncogenes in both tumour predisposition and normal development, and shed light on the pleiotropic and activity-dependent role of ALK in humans. More generally, missing germline mutations relative to the spectrum of somatic mutations reported for a given oncogene may be a reflection of severe effects during embryonic development, and may prompt mutation screening in patients with extreme phenotypes." (PMID:21972109)

A commentary accompanies it: Wilkie AOM, "New germline syndrome with brainstem abnormalities and neuroblastoma, caused by ALK mutation," *Hum Mutat* 2011;32(3):v (**PMID:21972113**; no abstract).

Associated HPO terms: **HP:0001298** *Encephalopathy* **[verified]**, **HP:0012747** *Abnormal brainstem MRI signal intensity* **[verified]**, **HP:0002791** *Hypoventilation* **[verified]**, **HP:0002871** *Central apnea* **[verified]**, **HP:0002104** *Apnea* **[verified]**.

> **Caution on the specific residues.** The two variants in de Pontual et al. are widely cited as **F1174V** and **F1245V**, but the retrieved abstract does not name them and I did not obtain the full text. Treat the residue assignment as **[lead]** until the paper's own text is read. The *concept* the abstract does support — that the strongest activating alleles are under-represented in the germline because they are developmentally deleterious — is itself a substantive and citable claim.

Note also that **congenital central hypoventilation syndrome (CCHS) is classically a *PHOX2B* phenotype, not an *ALK* phenotype**. The 2024 AACR update is explicit that *PHOX2B* germline variants underlie CCHS-with-NB predisposition (PMID:38860978). Do not attribute CCHS to *ALK* without the brainstem-syndrome caveat above.

### 3.5 Severity, progression and quality of life

- **Severity: highly variable, bimodal.** The same germline variant can produce a spontaneously regressing infant tumour in one carrier, high-risk metastatic disease in another, and nothing at all in a third. The strongest within-family illustration is kindred FNB56 (Mossé 2008), in which R1275Q was inherited from an **unaffected father**, with discordant twins and multiple unaffected carriers. **[lead — from a secondary summary of the paper, not from retrieved primary text.]**
- **Progression:** neuroblastoma specifically is one of the few human cancers with a well-documented capacity for **spontaneous regression and maturation** in infancy (Matthay et al., *Nat Rev Dis Primers* 2016, PMID:27830764, verbatim: *"the tendency for spontaneous regression of tumours in infancy"*). Ganglioneuroma is stable/benign; high-risk neuroblastoma is rapidly progressive.
- **Quality-of-life impact:** no *ALK*-specific QoL data exist. The burden in carriers who develop high-risk disease is driven by multimodal therapy late effects — ototoxicity (platinum), endocrine and growth sequelae, neurocognitive effects, second malignancy — plus, for carriers specifically, the **psychosocial burden of lifelong surveillance** and, under the GeneReviews protocol, three-monthly testing from birth to age six. I found **no** published EQ-5D, PROMIS or SF-36 data for this population. This is a genuine gap, not an omission.

---

## 4. Genetic / Molecular Information

### 4.1 The gene and protein

***ALK*** (`hgnc:427` **[verified]**) encodes anaplastic lymphoma kinase, a single-pass **receptor tyrosine kinase of the insulin-receptor superfamily**, located at chromosome **2p23** — immediately centromeric to *MYCN* at 2p24, a genomic adjacency with direct pathogenic consequences (Chen et al., PMID:18923524, verbatim: *"the ALK locus, centromeric to the MYCN locus, was identified as a recurrent target of copy number gain and gene amplification"*).

Domain architecture, from Reshetnyak et al., *Nature* 2021 (PMID:34819673) verbatim: *"ALK is composed of an extracellular region (ECR), a single transmembrane helix and an intracellular tyrosine kinase domain. ALK is activated by the binding of ALKAL1 and ALKAL2 ligands to its ECR."* The same paper establishes the activation mechanism: *"Our data reveal a mechanism of RTK activation that allows dimerization by either dimeric (ALKAL2) or monomeric (ALKAL1) ligands... The ALK-ECR undergoes a pronounced ligand-induced rearrangement and adopts an orientation parallel to the membrane surface."*

Protein length 1620 aa, UniProt **Q9UM73** — **[lead]**, not re-verified this session.

A therapeutically decisive property: *ALK* expression is **developmentally restricted and largely absent from healthy postnatal tissue**. Trigg & Turner, *Cancers* 2018 (PMID:29642598) verbatim: *ALK* "represents an ideal therapeutic target given its low or absent expression in healthy tissue postnatally."

### 4.2 Pathogenic variants

**Variant class.** All disease-associated germline variants reported to date are **heterozygous missense substitutions within the kinase domain** (GENO:0000135 *heterozygous* **[verified]**). No germline truncating, frameshift, splice or whole-gene deletion variant causes this syndrome — the mechanism is **gain of function**, so loss-of-function alleles are not causal.

**Germline variants reported in neuroblastoma families:**

| Variant (protein) | Context | Evidence |
|---|---|---|
| **p.Arg1275Gln (R1275Q)** | The most frequent germline allele; also the most frequent *somatic* hotspot after F1174 | PMID:18724359; PMID:18923525; PMID:40294355 |
| **p.Gly1128Ala (G1128A)** | Segregating family variant; weakly activating; **lower penetrance** | PMID:18724359 |
| **p.Arg1192Pro (R1192P)** | Segregating family variant; also inherited by unaffected carriers in the French series | PMID:18724359; PMID:22071890 |
| **p.Thr1151Met (T1151M)** / **p.Thr1151Arg (T1151R)** | T1151M in the original linkage work; T1151R inherited and shared with unaffected relatives | PMID:18724359; PMID:22071890 |
| **p.Phe1174Val (F1174V)**, **p.Phe1245Val (F1245V)** | De novo, with congenital NB + encephalopathy + brainstem malformation | PMID:21972109 — **residues [lead]** |
| **p.Ile1250Thr (I1250T)** | Reported kinase-**dead**; cautionary against assuming any kinase-domain germline substitution is activating | **[lead]** |

**Variant classification.** ClinVar (queried via MyVariant.info this session) records **NM_004304.5(ALK):c.3824G>A (p.Arg1275Gln)**, chr2:g.29432664C>T (GRCh38), rs113994087, as **Pathogenic**, germline origin, under the conditions *"Neuroblastoma, susceptibility to, 3"* (6 submitters), *"Hereditary cancer-predisposing syndrome"* (1 submitter) and "not provided" (1 submitter).

**Allele frequency.** The MyVariant query returned **no gnomAD exome or genome allele-frequency field** for this variant in the fields requested. That is an absence of a returned field, **not** evidence that the variant is absent from gnomAD — do not report it as "absent from gnomAD" without a direct gnomAD query. All reported germline *ALK* neuroblastoma alleles are expected to be ultra-rare; a direct gnomAD lookup is required before any frequency statement.

**Somatic versus germline.** The same hotspots recur somatically at far higher frequency. Headline somatic figures from four independent cohorts:

| Study | Cohort | Somatic *ALK* mutation frequency (verbatim) |
|---|---|---|
| Mossé 2008, PMID:18724359 | 194 high-risk | *"somatically acquired mutations in the tyrosine kinase domain in 12.4% of samples"* |
| George 2008, PMID:18923525 | primary NB | *"previously unknown mutations in the ALK gene... in 8% of primary neuroblastomas"* |
| Chen 2008, PMID:18923524 | 215 primary; 24 cell lines | *"eight novel missense mutations in 13 out of 215 (6.1%) fresh tumours and 8 out of 24 (33%) neuroblastoma-derived cell lines"* |
| Bresler 2014, PMID:25517749 | 1,596 diagnostic samples | *"ALK tyrosine kinase domain mutations occurred in 8% of samples—at three hot spots and 13 minor sites—and correlated significantly with poorer survival in high- and intermediate-risk neuroblastoma"* |
| Pugh 2013, PMID:23334666 | 240 high-risk (TARGET) | *ALK* mutated in *"9.2% of cases"*; also *"Rare, potentially pathogenic germline variants were significantly enriched in ALK, CHEK2, PINK1 and BARD1"* |
| Rosswog 2023, PMID:36807339 | 943 patients | *"At diagnosis, ALK point mutations occurred in 10.5% of all cases, with highest frequencies in stage 4 patients <18 months."* |

**Subclonality at diagnosis** is a practically important finding — Bellini et al., *Clin Cancer Res* 2015 (PMID:26059187) used targeted deep sequencing of 276 diagnostic samples and found F1174 mutations at mutated-allele fractions from 0.562% to 40.409% and R1275 from 0.811% to 73.001%, with *subclonal events below 20% allele fraction in over half of ALK-mutated cases*. A germline variant, by contrast, is present at ~50% allele fraction in every cell — which is itself a useful discriminator on tumour-only sequencing.

**Evolution over time** — Rosswog 2023 verbatim: *"At relapse, ALK alteration frequency increased by 70%, both in high-risk and non-high-risk cases. The increase was most likely due to de novo mutations, frequently leading to R1275Q substitutions, which are sensitive to pharmacological ALK inhibition. By contrast, the frequency of ALK amplifications did not change over the course of the disease. ALK amplifications, but not mutations, were associated with poor patient outcome."* (PMID:36807339)

**Functional consequence: constitutive, ligand-independent kinase activation.** Converging verbatim evidence:
- *"Mutations resulted in constitutive phosphorylation"* (PMID:18724359)
- *"Mutated ALK proteins were overexpressed, hyperphosphorylated and showed constitutive kinase activity"* (PMID:18923523)
- *"The mutated kinases were autophosphorylated and displayed increased kinase activity compared with the wild-type kinase. They were able to transform NIH3T3 fibroblasts as shown by their colony formation ability in soft agar and their capacity to form tumours in nude mice"* (PMID:18923524)
- *"ALK complementary DNAs encoding the F1174L and R1275Q variants, but not the wild-type ALK cDNA, transformed interleukin-3-dependent murine haematopoietic Ba/F3 cells to cytokine-independent growth"* (PMID:18923525)

**Not all variants are equal.** This is the single most therapeutically consequential molecular fact. Bresler et al., *Cancer Cell* 2014 (PMID:25517749) verbatim: *"Biochemical and computational studies distinguished oncogenic (constitutively activating) from nononcogenic mutations and allowed robust computational prediction of their effects. The mutated variants also showed differential in vitro crizotinib sensitivities. Our studies identify ALK genomic status as a clinically important therapeutic stratification tool in neuroblastoma and will allow tailoring of ALK-targeted therapy to specific mutations."*

Canonically: **R1275Q is crizotinib-sensitive; F1174L is intrinsically crizotinib-resistant** and co-segregates with *MYCN* amplification (Berry et al., PMID:22789543, verbatim: *"The ALK(F1174L) mutation is associated with intrinsic and acquired resistance to crizotinib and cosegregates with MYCN in neuroblastoma."*).

### 4.3 Modifier genes

- ***MYCN*** (`hgnc:7559` **[verified]**) — the dominant cooperating oncogene; amplification converts a permissive germline state into a tumour (§6.3).
- ***LMO1*** — common regulatory polymorphism modulating the adrenergic cell state and tumour initiation rate (PMID:26560027; PMID:37183825). `hgnc` ID **[lead]**.
- ***RET*** (`hgnc:9967` **[verified]**) — a *downstream* effector upregulated by activated Alk, and a tractable second target (Cazes et al., *Oncotarget* 2014: activated ALK *"triggers RET upregulation in mouse sympathetic ganglia at birth as well as in murine and human neuroblastoma,"* and RET inhibition with vandetanib *"strongly impairs tumor growth in vivo"* in both MYCN/Alk^R1279Q and MYCN/Alk^F1178L mice — **[quotes from a search-engine summary of PMC4058037, not from retrieved primary text; verify before use]**).
- Bypass-pathway genes that modify *response* rather than risk: **BRAF fusions, MET amplification, NF1 mutations** at acquired lorlatinib resistance (Xie et al., *NPJ Precis Oncol* 2026, PMID:42151367).

### 4.4 Epigenetic information

No *ALK*-predisposition-specific methylation or chromatin signature has been described. The relevant epigenetic biology is of the tumour, not the germline state: neuroblastoma identity is governed by **core regulatory circuitries (CRCs)** — super-enhancer-driven autoregulatory transcription-factor loops defining an **adrenergic (ADRN)** versus **mesenchymal (MES)** cell state (PMID:37183825, verbatim: *"These cell states are governed by autoregulatory transcriptional loops called core regulatory circuitries (CRCs), which drive the early development of sympathetic neuronal progenitors from migratory neural crest cells during embryogenesis"*). The *LMO1* risk allele acts by altering GATA3 binding within an H3K27ac-marked super-enhancer (PMID:26560027).

### 4.5 Chromosomal abnormalities

In the **germline**: none — this is a single-nucleotide missense syndrome. Large 2p23 germline rearrangements are not an established mechanism.

In the **tumour**: *MYCN* amplification (2p24), *ALK* copy gain and focal amplification (2p23), 17q gain, 1p36 loss, 11q loss, and whole-chromosome ploidy changes. Janoueix-Lerosey 2008 (PMID:18923523) verbatim: *"One particularly informative case presented a high-level gene amplification that was strictly limited to ALK, indicating that this gene may contribute on its own to neuroblastoma development."* The murine model recapitulates the cytogenetics — Heukamp 2012 (PMID:22764207) verbatim: *"Chromosomal aberrations were syntenic to those in human neuroblastoma, including 17q gain and MYCN oncogene amplification."*

---

## 5. Environmental Information

- **Environmental factors:** none established, in carriers or in sporadic neuroblastoma. No ECTO exposure term should be bound to this entry.
- **Lifestyle factors:** not applicable — this is a predisposition manifesting in infancy and early childhood.
- **Infectious agents:** not applicable. No pathogen has any role; no NCBITaxon infectious-agent binding is appropriate.

This section is a genuine negative and should be recorded as such rather than left blank.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain

Steps are numbered from the initiating lesion to clinical manifestation. **Demonstrated** = supported by direct experimental or human evidence cited at the step; **inferred** = a plausible linking step not directly demonstrated for the germline state.

1. **A heterozygous germline missense variant in the *ALK* kinase domain is present in every cell of the embryo from conception.** *(Demonstrated — PMID:18724359, PMID:18923523.)*
2. **The variant destabilises the kinase's autoinhibited conformation, producing ligand-independent dimerisation-equivalent activation**, which **leads to** constitutive autophosphorylation of the receptor. *(Demonstrated — "Mutated ALK proteins were overexpressed, hyperphosphorylated and showed constitutive kinase activity," PMID:18923523; "The mutated kinases were autophosphorylated," PMID:18923524. The wild-type activation mechanism it subverts is the ALKAL1/ALKAL2-driven ECR rearrangement of PMID:34819673.)* — GO:0046777 *protein autophosphorylation* **[verified]**; GO:0004714 *transmembrane receptor protein tyrosine kinase activity* **[verified]**; GO:0018108 *peptidyl-tyrosine phosphorylation* **[verified]**; GO:0005886 *plasma membrane* **[verified]**.
3. **Constitutive ALK activity results in sustained signalling through RAS–MAPK, PI3K–AKT–mTOR and STAT3**, in the absence of any physiological ligand cue. *(Demonstrated for MAPK and PI3K/AKT/mTOR in vivo — "ALK(F1174L)-induced activation of the PI3K/AKT/mTOR and MAPK pathways," PMID:22789543. Demonstrated for STAT3/ERK in ALK-mutant NB cells — "Alectinib suppressed PD-L1 expression by inhibiting ALK downstream pathways, including STAT3 and ERK1/2 phosphorylation," PMID:41866626.)* — GO:0000165 *MAPK cascade*, GO:0007265 *Ras protein signal transduction*, GO:0043491 *phosphatidylinositol 3-kinase/protein kinase B signal transduction*, GO:0031929 *TOR signaling* — all **[verified]**.
4. **In the developing sympathoadrenal lineage, this drives excess proliferation and delayed/blocked differentiation of sympathetic neuroblasts**, which **results in** hyperplasia of sympathetic ganglia and a persistent pool of undifferentiated progenitors beyond the normal developmental window. *(Demonstrated in knock-in mice: enlargement of superior cervical and stellate ganglia from E12.5 persisting into adulthood, with increased sympathetic neuron proliferation at birth — Cazes et al., Oncotarget 2014 — **[from a secondary summary of PMC4058037; verify against primary text]**. Also demonstrated as "prolonged neurogenesis" in the same system.)* — GO:0048485 *sympathetic nervous system development* **[verified, OLS4]**; GO:0030182 *neuron differentiation*, GO:0050767 *regulation of neurogenesis*, GO:0008284 *positive regulation of cell population proliferation* — **[verified]**.
5. **Branch point — this expanded progenitor pool is a permissive, not a sufficient, state.** Most carriers' progenitor pools involute normally and no tumour forms. *(Demonstrated by the ~50% penetrance and the existence of unaffected obligate carriers — PMID:20301782, PMID:22071890.)*
   - **5a. Branch A — no second hit → no tumour** (≈50% of carriers), or a tumour that spontaneously regresses or matures into ganglioneuroma in infancy. *(Demonstrated for spontaneous regression as a general NB property — PMID:27830764.)*
   - **5b. Branch B — a cooperating somatic lesion is acquired**, most often ***MYCN* amplification**, which **leads to** transformation (step 6).
6. **MYCN overexpression in an ALK-activated neuroblast blocks the developmentally timed apoptotic cull that normally eliminates hyperplastic sympathoadrenal cells.** *(Demonstrated — Zhu et al., PMID:22439933 verbatim: "MYCN overexpression induces adrenal sympathetic neuroblast hyperplasia, blocks chromaffin cell differentiation, and ultimately triggers a developmentally-timed apoptotic response in the hyperplastic sympathoadrenal cells. Coexpression of activated ALK with MYCN provides prosurvival signals that block this apoptotic response and allow continued expansion and oncogenic transformation of hyperplastic neuroblasts, thus promoting progression to neuroblastoma.")* — GO:0043066 *negative regulation of apoptotic process* **[verified]**.
7. **Reciprocally, activated ALK increases MYCN protein dosage** via PI3K/AKT/mTOR-dependent stabilisation and suppresses MYCN's pro-apoptotic arm, closing a feed-forward loop. *(Demonstrated — PMID:22789543 verbatim: "ALK(F1174L)/MYCN tumors exhibited increased MYCN dosage due to ALK(F1174L)-induced activation of the PI3K/AKT/mTOR and MAPK pathways, coupled with suppression of MYCN pro-apoptotic effects.")*
8. **Activated ALK upregulates RET in sympathetic ganglia**, contributing a parallel pro-tumourigenic effector arm. *(Demonstrated in mouse and detected in human NB — Cazes 2014 — **[verify primary text]**.)*
9. **The transformed clone proliferates, acquires the stereotyped segmental copy-number landscape of neuroblastoma (17q gain, 1p/11q loss), invades and metastasises**, which **results in** the clinical tumour at an adrenal, paraspinal, cervical, thoracic or pelvic site. *(Demonstrated — PMID:22764207 for syntenic aberrations in the model; PMID:27830764 for the human clinical picture. The ECM-remodelling/invasion contribution of R1275Q specifically is reported in Cazes et al., Oncogene 2016, "ALK^R1275Q perturbs extracellular matrix, enhances cell invasion" — **[lead, title only]**.)* — GO:0016477 *cell migration*, GO:0001755 *neural crest cell migration* **[verified]**.
10. **Tumour mass and catecholamine secretion produce the clinical phenotype** — abdominal mass, cord compression, Horner syndrome, hypertension, elevated urinary HVA/VMA (§3.2–3.3). *(Demonstrated clinically.)*
11. **Branch C — germline-specific developmental toxicity.** Where the germline allele is one of the strongest activators, constitutive ALK signalling during CNS development **results in** encephalopathy and brainstem malformation alongside congenital neuroblastoma. *(Demonstrated in two de novo cases — PMID:21972109.)* This branch also explains why the strongest somatic alleles are under-represented in the germline: *"missing germline mutations relative to the spectrum of somatic mutations reported for a given oncogene may be a reflection of severe effects during embryonic development"* (PMID:21972109).
12. **Branch D — lifelong, not childhood-limited, risk.** In at least one kindred, an adult carrier developed bilateral adrenal neuroblastoma at age 36 during pregnancy, after being asymptomatic throughout childhood *(Demonstrated — PMID:40294355)*. The mechanism of the adult-onset branch is **not established**; the pregnancy association is a single observation and should not be presented as a mechanism.

### 6.2 Cells, tissues and compartments

| Entity | Term | Status |
|---|---|---|
| Neural crest cell (origin of the lineage) | **CL:0011012** *neural crest cell* | **[verified]** |
| Migratory neural crest cell | **CL:0000333** *migratory neural crest cell* | **[verified]** |
| Neural crest derived neuroblast | **CL:0002676** | **[verified]** |
| Neuroblast | **CL:0000031** *neuroblast (sensu Vertebrata)* | **[verified]** |
| Sympathetic neuron | **CL:0011103** | **[verified]** |
| Chromaffin cell | **CL:0000166** | **[verified]** |
| Adrenal medulla chromaffin cell | **CL:0000336** | **[verified]** |
| Schwann cell precursor (candidate contributor to the sympathoadrenal pool) | **CL:0002375** | **[verified]** |
| Plasma membrane (receptor location) | **GO:0005886** | **[verified]** |

**On the cell of origin.** Single-cell studies of human adrenal medulla development place neuroblastoma's origin in the **sympathoadrenal/noradrenergic progenitor compartment**, with debate over the relative contribution of **Schwann cell precursors (SCPs)** versus committed sympathoblasts. A 2026 preprint directly implicates the predisposition allele in this process: *"ALK R1275Q mutation drives expansion of SCP-like cells during sympathoadrenal commitment and primes neuroblastoma initiation"* (bioRxiv, posted 27 January 2026, doi 10.64898/2026.01.27.701690). **I was rate-limited fetching the abstract and have verified only the title, venue and date — treat its content as unread.** If confirmed, it would place the mechanism's step 4 precisely at SCP-like cells and is directly relevant to this entry.

A complementary human-cell system: Shi et al., *Genes Cells* 2026 (PMID:41560679) showed MYCN+ALK coexpression in **cranial** neural-crest cells derived from human iPSCs induced NB-like tumours in mice, with *"loss of NF1 and gain of 17q chromosome"* — extending the cooperation model to a human-cell context.

### 6.3 Protein dysfunction

Gain of function by conformational destabilisation of the autoinhibited kinase, not misfolding, aggregation or loss of function. The kinase remains catalytically competent — indeed hyperactive — which is why it is druggable by ATP-competitive inhibitors. Structural basis for *normal* activation: PMID:34819673. Structure-informed classification of which substitutions are oncogenic: PMID:25517749.

### 6.4 Metabolic changes

Nothing specific to the germline syndrome. The relevant "metabolic" phenotype is **catecholamine biosynthesis and secretion by the tumour**, producing the HVA/VMA elevation that underpins both diagnosis and surveillance. CHEBI terms for homovanillic acid and vanillylmandelic acid were **not** resolved this session — **[lead]**.

### 6.5 Immune system involvement

Not a mechanism of predisposition, but therapeutically important in two ways: (i) **GD2 is the immunotherapeutic target** in high-risk neuroblastoma, and (ii) ALK signalling modulates immune evasion — Sugitatsu et al., *Br J Cancer* 2026 (PMID:41866626) verbatim: *"Alectinib suppressed PD-L1 expression by inhibiting ALK downstream pathways, including STAT3 and ERK1/2 phosphorylation,"* with the combination of alectinib and GD2 CAR-T cells reducing tumour growth and extending survival in an ALK-mutant xenograft model.

### 6.6 Tissue damage mechanisms

Not inflammatory, ischaemic or fibrotic. Tissue injury is **mass effect plus infiltration**: neural foraminal extension causing cord compression, marrow replacement causing cytopenias, hepatic infiltration in stage MS, and bone destruction at metastatic sites.

### 6.7 Molecular profiling

- **Transcriptomics:** ALK-mutant tumours sit predominantly in the **adrenergic (ADRN)** CRC state (PMID:37183825). Transcriptomic evidence of increased sympathetic neuron proliferation at birth in knock-in mutants (Cazes 2014, **[verify]**).
- **Genomics:** TARGET WGS/WES/RNA-seq of 240 high-risk cases (PMID:23334666); 1,596-sample mutation survey (PMID:25517749); 943-patient longitudinal diagnosis/relapse series (PMID:36807339).
- **Proteomics / metabolomics / lipidomics:** **no** *ALK*-predisposition-specific dataset identified. Reported as absent.
- **Functional genomics:** RNAi knockdown establishes ALK dependency — *"targeted knockdown of ALK messenger RNA resulted in profound inhibition of growth in all cell lines harbouring mutant or amplified ALK, as well as in two out of six wild-type cell lines for ALK"* (PMID:18724359); *"The knockdown of ALK expression in ALK-mutated cells, but also in cell lines overexpressing a wild-type ALK, led to a marked decrease of cell proliferation"* (PMID:18923523). The DepMap CRISPR dependency portal is the obvious systematic resource; **not queried this session**.
- **Datasets:** no GEO/dbGaP accessions were resolved this session. TARGET-NBL is the obvious starting point for a `datasets:` block, but every accession must be verified with the repository's own tooling before being written.

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level

**Primary system: the peripheral sympathetic nervous system** (UBERON:0000010 *peripheral nervous system* **[verified]**). Matthay 2016 (PMID:27830764) frames neuroblastoma as a neuroendocrine tumour of the developing sympathetic nervous system; Janoueix-Lerosey (PMID:18923523) as *"a tumour derived from the peripheral sympathetic nervous system."*

Primary tumour sites, in approximate order of frequency:

| Site | UBERON | Status |
|---|---|---|
| Adrenal gland (commonest primary) | **UBERON:0002369** *adrenal gland* | **[verified]** |
| Adrenal medulla (the specific compartment) | **UBERON:0001236** *adrenal medulla* | **[verified]** |
| Sympathetic ganglion | **UBERON:0001806** | **[verified]** OLS4 |
| Paravertebral ganglion (paraspinal chain) | **UBERON:0001807** | **[verified]** OLS4 |
| Superior cervical ganglion (enlarged in knock-in mice) | **UBERON:0001989** | **[verified]** OLS4 |
| Posterior mediastinum / thoracic cavity | **UBERON:0003728** *mediastinum*; **UBERON:0002224** *thoracic cavity* | **[verified]** |
| Neck (cervical primary) | **UBERON:0000974** *neck* | **[verified]** |
| Pelvis (organ of Zuckerkandl) | **[lead]** | not resolved |
| Retroperitoneal space | **[lead]** | not resolved |

Secondary / metastatic involvement:

| Site | UBERON | Status |
|---|---|---|
| Bone marrow | **UBERON:0002371** | **[verified]** |
| Liver (stage MS/4S) | **UBERON:0002107** | **[verified]** |
| Lymph node | **UBERON:0000029** | **[verified]** |
| Skin (blueberry-muffin nodules in infants) | **UBERON:0002097** *skin of body* | **[verified]** |
| Spinal cord (compression, not invasion) | **UBERON:0002240** | **[verified]** |
| Bone / cortical bone | **[lead]** | not resolved |
| Orbit | **[lead]** | not resolved |

In the rare germline developmental branch (§3.4), the **brainstem** (UBERON:0002298 **[verified]**) is structurally abnormal.

### 7.2 Subcellular

ALK is a **plasma-membrane** receptor (GO:0005886 **[verified]**). Its downstream effectors act in cytosol and nucleus (GO:0045944 *positive regulation of transcription by RNA polymerase II* **[verified]**). No organelle-specific pathology (no mitochondrial, lysosomal or ER component).

### 7.3 Lateralisation

**This is a diagnostically load-bearing feature.** Germline *ALK* disease is disproportionately **bilateral and/or multifocal** — bilateral adrenal tumours in both the infant and the adult of the kindred in PMID:40294355, and all three germline variants in the Bourdeaut series arising *"in a context of multifocal tumours"* (PMID:22071890). Sporadic neuroblastoma is characteristically unilateral and unifocal; bilaterality or multifocality is the trigger for germline testing.

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** congenital to early childhood, with risk *"highest in infancy and decreasing by late childhood"* (PMID:20301782). Familial cases present earlier than sporadic ones. For context, sporadic neuroblastoma has a median age at diagnosis of ~17 months with ~90% diagnosed before age 5 **[lead — from secondary sources, see §9.1]**.
- **Pattern:** typically insidious — an incidentally found mass, or symptoms from mass effect. Acute presentations occur with cord compression or massive hepatomegaly.
- **The upper age boundary is genuinely contested.** GeneReviews states *"Screening beyond age ten years is not indicated"* (PMID:20301782). Against this, Mossé et al., *JCO Precision Oncology* 2025 (PMID:40294355) report a carrier who developed **bilateral adrenal neuroblastoma at age 36**, and argue that *"patients with germline ALK mutations have a lifelong risk of developing new neuroblastic tumors and thus require surveillance through adulthood."* A KB entry should record **both** positions and attribute each.

### 8.2 Progression

- **Staging:** the **INRG (International Neuroblastoma Risk Group)** pretreatment staging system (L1, L2, M, MS) and the **INSS** post-surgical system; risk stratification integrates age, stage, *MYCN* status, histology (Shimada/INPC), ploidy and segmental chromosomal alterations. There is **no** *ALK*-predisposition-specific staging system — carriers are staged and risk-stratified identically to all other patients.
- **Rate:** bimodal and extreme. Low-risk infant disease may regress without treatment; high-risk disease is *"rapidly progressive; even with intensive myeloablative chemotherapy, relapse is common and almost uniformly fatal"* (PMID:18923525).
- **Course in the carrier:** the predisposition itself is lifelong and static; the clinical course is punctuated by discrete tumour events, which may recur metachronously at new sites (PMID:40294355).
- **Duration:** the susceptibility is lifelong. An individual tumour episode may be self-limited (regression), curable, or fatal.

### 8.3 Patterns

- **Spontaneous regression** is a genuine and well-documented phenomenon in infant neuroblastoma (PMID:27830764). Maturation to ganglioneuroma is the differentiation counterpart.
- **Treatment-induced remission** is achievable and can be durable on targeted therapy alone — PMID:40294355 reports an infant who achieved *"an early complete response"* on crizotinib, took it for 5 years, and *"remains in remission now 8 years off-therapy."*
- **Critical window for intervention:** birth to ~6 years, which is why the GeneReviews surveillance protocol is at its most intensive there (three-monthly). The rationale for surveillance is stage-shift — detecting tumours before they become high-risk or cause end-organ damage.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**Of the predisposition:** no prevalence estimate exists. It is a rare syndrome of unknown population frequency.

**Of the underlying tumour and its familial fraction** (2024 AACR consensus, PMID:38860978, verbatim): *"Genetic predisposition to neuroblastoma (NB) is relatively rare. Only 1% to 2% of patients have a family history of NB, 3% to 4% of cases present with bilateral or multifocal primary tumors, and occasional patients have syndromes that are associated with increased NB risk."* And: *"several groups determined that activating GPVs in ALK accounted for a substantial number of familial NB."*

2017 AACR consensus (PMID:28674118, verbatim): *"Prior studies suggest that about 2% of patients with NB have an underlying genetic predisposition that may have contributed to the development of NB. Germline mutations in ALK and PHOX2B account for most familial NB cases."*

**Neuroblastoma incidence (background rates — all [lead], from secondary sources only):** approximately **8.3–9.5 cases per million children under 15 per year**, with **>650 new cases annually in the United States**; ~15% of paediatric cancer deaths (PMID:18923525 verbatim: *"accounts for approximately 15% of all deaths due to childhood cancer"*; PMID:28674118: *"accounts for 15% of pediatric cancer deaths"*). These incidence figures came from a web-search summary of StatPearls/ACS/NCI and should be replaced by a directly cited SEER or registry source before use.

**Arithmetic implication, offered as a derived estimate rather than a cited figure:** if 1–2% of NB is familial and *ALK* explains most of it, germline *ALK* accounts for roughly 1% of all neuroblastoma — on the order of **a handful of new index cases per year in the United States**. Searches for a directly measured germline-*ALK* prevalence in an unselected cohort did not return one. One secondary source stated that *"in families with two or more first-degree relatives with neuroblastoma, the incidence of germline ALK pathogenic variants is 80%"* — **[lead; source not identified, do not cite without finding it]**.

### 9.2 Inheritance characteristics

From GeneReviews (PMID:20301782), verbatim:

> "ALK-related neuroblastic tumor susceptibility is inherited in an autosomal dominant manner. Some individuals diagnosed with ALK-related neuroblastic susceptibility inherited a pathogenic variant from a heterozygous parent. Because of reduced penetrance, a parent may have a germline ALK activating pathogenic variant without having developed a neuroblastic tumor. Some individuals diagnosed with ALK-related neuroblastic tumor susceptibility have the disorder as the result of a de novo germline activating pathogenic variant; the proportion of probands who have a de novo pathogenic variant is unknown. Each child of an individual with ALK-related neuroblastic tumor susceptibility has a 50% chance of inheriting the ALK pathogenic variant. The likelihood that a child who inherits the pathogenic variant will develop a neuroblastic tumor is unknown, though the penetrance is estimated to be around 50%."

| Parameter | Value | Source |
|---|---|---|
| Mode of inheritance | **Autosomal dominant** (HPO *Autosomal dominant inheritance* **[lead]** — CURIE not resolved this session) | PMID:20301782 |
| Zygosity | Heterozygous — GENO:0000135 **[verified]** | PMID:18724359 |
| Overall penetrance | **≈50%**, age-dependent, highest in infancy | PMID:20301782 |
| Variant-specific penetrance | **R1275Q > G1128A.** One secondary source attributes to GeneReviews: *"The pathogenic variant p.Gly1128Ala appeared to have lower penetrance: 40% of heterozygotes developed neuroblastoma during childhood."* | **[lead — search-engine rendering of GeneReviews body text; the chapter itself was not retrievable, so this figure is NOT verified]** |
| Expressivity | **Highly variable** — tumour type (neuroblastoma vs ganglioneuroma), site, number of foci, stage and outcome all vary within a single family | PMID:20301782; PMID:40294355 |
| De novo rate | **Unknown** — explicitly stated as unknown | PMID:20301782 |
| Genetic anticipation | **Not described.** Not a repeat-expansion disorder; no mechanism for anticipation | — |
| Germline mosaicism | **Not reported.** No published instance identified | — |
| Founder effects | **None described** | — |
| Consanguinity | **Not relevant** — dominant, gain-of-function | — |
| Carrier frequency | **Not established**; expected ultra-rare. gnomAD not directly queried (§4.2) | — |

### 9.3 Population demographics

- **Affected populations:** no ethnic or ancestral predilection reported for germline *ALK*. Families have been described in North American, European (French, Italian, Belgian, UK) and Asian cohorts. No HANCESTRO term is warranted.
- **Geographic distribution:** none — case ascertainment follows where paediatric-oncology genomics is practised, which is an ascertainment artefact rather than a biological distribution.
- **Variant geography:** no population-specific germline allele reported.
- **Sex ratio:** not established for the predisposition. Sporadic neuroblastoma shows a slight male excess (~1.1–1.2:1) **[lead]**.
- **Age distribution:** strongly skewed to infancy and early childhood, with a documented adult tail (PMID:40294355).

---

## 10. Diagnostics

### 10.1 Establishing the diagnosis of the predisposition

GeneReviews, verbatim: *"ALK-related neuroblastic tumor susceptibility is established by identification of a heterozygous germline ALK activating pathogenic variant in the tyrosine kinase domain that is known or suspected to cause altered kinase function by molecular genetic testing."* (PMID:20301782)

**Two components are required**, and the second is what makes this diagnosis harder than most: a germline *ALK* kinase-domain variant **plus** evidence (functional or predictive) that it is **activating**. Bresler et al. (PMID:25517749) provide the biochemical and computational framework that distinguishes *"oncogenic (constitutively activating) from nononcogenic mutations."* A VUS in the *ALK* kinase domain is not a diagnosis.

### 10.2 Who should be tested

Derived from Bourdeaut (PMID:22071890) and the AACR consensus documents (PMID:28674118, PMID:38860978):

- **Any patient with bilateral or multifocal primary neuroblastic tumours** — the highest-yield indication. *"Conversely, multifocal tumours might be the most to benefit from the genetic screening."*
- **Any family history of neuroblastic tumour** in a first- or second-degree relative.
- **Congenital neuroblastoma with encephalopathy or brainstem malformation** (PMID:21972109).
- **A somatic *ALK* mutation at ~50% allele fraction** on tumour sequencing, which should prompt germline confirmation.
- Note that **young age alone is not a useful selection criterion** — Bourdeaut, verbatim: *"Younger age at tumour onset did not seem to offer a relevant selection criterion for ALK analyses."*
- Kim et al. (PMID:37688579) argue more broadly, verbatim: *"As centers move toward paired tumor-normal sequencing at diagnosis, efforts should be made to centralize data and provide an infrastructure to support cooperative longitudinal prospective studies of germline pathogenic variation."*

### 10.3 Genetic testing modalities

| Modality | Utility |
|---|---|
| **Single-gene *ALK* sequencing** (kinase domain, or full coding sequence) | The targeted first-line test when the indication is specific; also the test for at-risk relatives once the familial variant is known |
| **Multigene cancer-predisposition panel** | Preferred first-line in practice — must include ***ALK*, *PHOX2B*, *BARD1***, and the syndromic genes in the differential (*TP53*, *PTPN11* and the RASopathy genes, *NF1*) |
| **WES / WGS (germline, paired with tumour)** | Appropriate where panel is negative and suspicion remains; also the route by which the *BARD1* and other enrichments were found (PMID:23334666, PMID:37688579) |
| **Chromosomal microarray / karyotype / FISH** | **Not indicated for this diagnosis.** No germline CNV mechanism. (CMA has a role in the tumour, and *MYCN* FISH is standard tumour work-up) |
| **mtDNA / repeat-expansion testing** | **Not applicable** |

NCIT:C15709 *Genetic Testing* **[verified]**.

### 10.4 Tumour diagnosis and work-up (for the tumour event, not the predisposition)

- **Urinary catecholamine metabolites — HVA and VMA** (HP:0011977, HP:0011978 **[verified]**). These are both the diagnostic biochemical test and the surveillance analyte.
- **Imaging:** abdominal ultrasound (NCIT:C17230 *Ultrasound Imaging* **[verified]**) as the surveillance modality; CT or MRI (NCIT:C16809 *Magnetic Resonance Imaging* **[verified]**) for staging; **¹²³I-MIBG scintigraphy** for disease extent and response — note PMID:37012551 uses *"¹²³I-metaiodobenzylguanidine (MIBG) response"* as a trial endpoint, and PMID:40294355 reports a bilateral case in which *"The left mass was MIBG-avid; the right was not"*, a reminder that MIBG-negative neuroblastic tumours occur.
- **Bone marrow aspirate and trephine biopsy** (bilateral) for metastatic staging.
- **Histopathology:** INPC/Shimada classification — degree of neuroblastic differentiation, Schwannian stromal content, mitosis–karyorrhexis index. This is what distinguishes neuroblastoma from ganglioneuroblastoma from ganglioneuroma, and is therefore what determines which of the three HPO terms applies.
- **Immunohistochemistry:** PHOX2B, synaptophysin, chromogranin A, tyrosine hydroxylase, GD2; ALK IHC is **not** a reliable surrogate for *ALK* mutation status in neuroblastoma (unlike in ALK-fusion lung cancer) and must not be used in its place.
- **Tumour molecular profiling:** *MYCN* amplification status (FISH or ddPCR) is mandatory for risk stratification; segmental chromosomal alterations; *ALK* mutation status by **deep sequencing** — essential, because over half of *ALK*-mutated cases at diagnosis are subclonal below 20% allele fraction and would be missed by standard-depth sequencing (PMID:26059187).

### 10.5 Liquid biopsy

**An active and plausibly imminent change in practice.** Mossé et al. (PMID:40294355) recommend surveillance with *"ctDNA and whole-body MRIs"*. Circulating tumour DNA is well suited to this disease because the target is a recurrent point mutation at a known hotspot, present in the germline at 50% in leukocytes — which means **ctDNA assays in a germline carrier must be designed to detect allele-fraction *excess* over the germline 50%, or to track tumour-specific co-occurring lesions**, not merely the presence of the variant. I found no validated ctDNA surveillance protocol for germline-*ALK* carriers; this is a stated recommendation, not an established method.

### 10.6 Clinical criteria and differential diagnosis

There are no formal consensus diagnostic criteria for the predisposition beyond the molecular definition. The differential for a child with a neuroblastic tumour and a suspected predisposition:

| Alternative | Distinguishing features |
|---|---|
| ***PHOX2B*-related NB predisposition (NBLST2, OMIM 613013)** | Congenital central hypoventilation syndrome and/or Hirschsprung disease; *PHOX2B* polyalanine expansion or non-PARM variant. PMID:38860978: *"a germline pathogenic variant (GPV) in PHOX2B was associated with Hirschsprung disease and congenital central hypoventilation syndrome"* |
| **Li-Fraumeni syndrome (*TP53*)** | Broad multi-tumour spectrum; neuroblastoma is an uncommon component (PMID:28674118) |
| **RASopathies (Noonan/CFC; *PTPN11*, others)** | Characteristic facies, cardiac defects, short stature; neuroblastoma is rare (PMID:28674118) |
| ***BARD1*-associated predisposition** | No syndromic features; DNA-repair deficiency mechanism; enriched in unselected NB (PMID:37688579, PMID:37688570) |
| **Beckwith-Wiedemann spectrum** | Overgrowth, macroglossia, hemihypertrophy; embryonal-tumour risk including NB **[lead]** |
| **Neurofibromatosis type 1** | Café-au-lait macules, neurofibromas; NB association weak **[lead]** |
| **Sporadic neuroblastoma with a somatic *ALK* mutation** | **The most important and most often confused alternative.** Unifocal, no family history, mutation at a subclonal or non-50% allele fraction, absent from leukocyte DNA |

### 10.7 Screening of asymptomatic individuals

GeneReviews, verbatim: *"It is appropriate to test relatives at risk (e.g., sibs age <10 years at the time of diagnosis of the proband, as well as sibs born subsequently) for the ALK pathogenic variant found in the proband to identify those for whom early detection of neuroblastomas and initiation of therapy would likely improve quality of life and possibly affect outcome (if therapy is started prior to end organ damage)."* (PMID:20301782)

Note that **population-based newborn screening for neuroblastoma by urinary catecholamines was trialled at scale in Japan, Germany and Quebec and abandoned** — it detected an excess of biologically favourable tumours that would have regressed, without reducing mortality. This history is the reason surveillance here is targeted at known carriers only, and a KB entry should not present catecholamine screening as a population measure. **[lead — well established in the literature but not re-cited this session.]**

---

## 11. Outcome / Prognosis

### 11.1 Prognosis of the carrier state versus the tumour

These must not be conflated. **Being a carrier is not a disease state** — roughly half of carriers never develop a tumour, and those who do may have a tumour that regresses. Prognosis is determined by the tumour event, risk-stratified exactly as for any neuroblastoma.

### 11.2 Survival

- **All neuroblastoma:** 5-year overall survival for high-risk disease has improved to *"50%"* with intensive multimodal therapy (PMID:27830764, verbatim: *"these have improved 5-year overall survival to 50%"*). Trigg & Turner (PMID:29642598) put it at *"40-50%"* with *"over half of patients relapse."*
- **Effect of *ALK* mutation on outcome:** Bresler 2014 — *ALK* kinase-domain mutations *"correlated significantly with poorer survival in high- and intermediate-risk neuroblastoma"* (PMID:25517749). Bellini 2015 — *"ALK mutations correlated with reduced five-year overall survival (75% vs. 57%, P = 0.0212)"* (PMID:26059187).
- **Mutation versus amplification:** Rosswog 2023 found that *"ALK amplifications, but not mutations, were associated with poor patient outcome"* (PMID:36807339). This apparent conflict with Bresler/Bellini is real and should be recorded as such rather than smoothed over — the cohorts, eras and covariate adjustments differ.
- **Any germline predisposition variant worsens outcome:** Kim 2024 — *"Patients harboring a germline pathogenic or likely pathogenic variant had a worse overall survival compared with those without (P = 8.6 x 10-3)"*, and *"The presence of any germline pathogenic or likely pathogenic variant in a cancer predisposition gene was independently predictive of worse overall survival"* (PMID:37688579). This is across all predisposition genes, not *ALK* specifically.
- **No published survival estimate exists for germline-*ALK* carriers as a group.**

### 11.3 Morbidity, disability and quality of life

Driven by therapy rather than by the germline state: platinum ototoxicity (ANBL1531 reported contemporary ototoxicity rates), growth and endocrine late effects, nephrotoxicity, neurocognitive effects, infertility, second malignancy, and — for paraspinal tumours — permanent neurological deficit from cord compression. For carriers specifically, add the burden of surveillance and the reproductive and psychological consequences of a dominant predisposition in the family. **No disease-specific QoL instrument data identified.**

### 11.4 Complications

Cord compression with permanent deficit; metachronous new primaries at new anatomical sites (PMID:40294355); relapse with acquired resistance; treatment-related late effects; and, for the rare developmental branch, fixed neurological disability from the brainstem malformation (PMID:21972109).

### 11.5 Recovery potential

Genuinely good in several scenarios: ganglioneuroma is cured by excision; low-risk infant disease may need observation only; and targeted therapy can produce durable off-treatment remission — PMID:40294355 reports *"an early complete response"* to crizotinib in an infant with germline R1275Q, who *"remains in remission now 8 years off-therapy"*, and an adult who *"continued ALK inhibition with alectinib for 28 months"* and maintains *"complete remission."*

### 11.6 Prognostic factors and biomarkers

Standard INRG factors — age at diagnosis, INRG stage, *MYCN* amplification, INPC histology, DNA ploidy, segmental chromosomal alterations (1p, 11q loss; 17q gain). *ALK*-specific: mutation presence and **which** hotspot (F1174 co-segregates with *MYCN* amplification and with crizotinib resistance — PMID:22789543, PMID:25517749); *ALK* amplification (adverse — PMID:36807339); allele fraction/clonality (PMID:26059187). Response biomarkers on ALK inhibition: MIBG response (PMID:37012551), and molecular profile — Xie 2026 verbatim: *"patients with ALK hotspot mutations alone achieved an ORR of 100%, whereas those with concurrent MYCN amplification, rare ALK mutations, or ALK amplification demonstrated significantly reduced efficacy (ORR 25.0%, p = 0.006)"* (PMID:42151367).

---

## 12. Treatment

### 12.1 The governing principle

GeneReviews, verbatim: *"Children who develop neuroblastic tumors should be evaluated and treated by a pediatric oncologist at a pediatric cancer center. Treatment for individuals with neuroblastomas and ganglioneuroblastomas who have a germline ALK activating pathogenic variant is the same standard risk-stratified therapy used to treat all neuroblastoma. Ganglioneuromas are typically removed by surgical resection and require no further therapy."* (PMID:20301782)

**This is contested at the leading edge.** Mossé et al. 2025 propose a germline-specific departure — *"ALK inhibition therapy as the primary treatment modality, perhaps even as monotherapy"* for germline-*ALK* patients (PMID:40294355). A KB entry should record the standard-of-care position as current guidance and this as an emerging, case-report-level proposal.

### 12.2 Targeted therapy — ALK inhibitors

NCIT:C93352 *Targeted Therapy* **[verified]**; NCIT:C15986 *Pharmacotherapy* **[verified]**.

| Agent | Generation | CHEBI | NCIT | Evidence in neuroblastoma |
|---|---|---|---|---|
| **Crizotinib** | 1st | **CHEBI:64310** **[verified]** | **NCIT:C74061** **[verified]** OLS4 | COG ADVL0912 phase 1 (PMID:23598171): RP2D 280 mg/m² BID; but *"one of 11"* neuroblastoma patients responded — activity was concentrated in ALCL and IMT. Durable responses do occur in germline R1275Q (PMID:40294355) |
| **Lorlatinib** | 3rd | **CHEBI:143117** **[verified]** | **NCIT:C113655** **[verified]** OLS4 | The current standard ALK inhibitor for this disease — see below |
| **Ceritinib** | 2nd | **CHEBI:78432** **[verified]** | **[lead]** | Paediatric phase 1 (NCT01742286) |
| **Alectinib** | 2nd | **CHEBI:90936** **[verified]** | **[lead]** | Used for 28 months with sustained CR in an adult germline-R1275Q carrier (PMID:40294355); enhances GD2 CAR-T efficacy preclinically (PMID:41866626) |
| **Entrectinib** | — | **CHEBI:195558** **[verified]** | **NCIT:C114984** **[verified]** | ALK/ROS1/NTRK inhibitor; paediatric development |
| **Ensartinib, brigatinib, repotrectinib** | 2nd/3rd | **[lead]** | **[lead]** | Investigational in this setting |

**Why lorlatinib displaced crizotinib.** Goldsmith et al., *Nat Med* 2023 (PMID:37012551), abstract verbatim:

> "Neuroblastomas harbor ALK aberrations clinically resistant to crizotinib yet sensitive pre-clinically to the third-generation ALK inhibitor lorlatinib. We conducted a first-in-child study evaluating lorlatinib with and without chemotherapy in children and adults with relapsed or refractory ALK-driven neuroblastoma... The RP2D of lorlatinib with and without chemotherapy in children was 115 mg/m². The single-agent adult RP2D was 150 mg. The single-agent response rate (complete/partial/minor) for <18 years was 30%; for ≥18 years, 67%; and for chemotherapy combination in <18 years, 63%; and 13 of 27 (48%) responders achieved MIBG complete responses, supporting lorlatinib's rapid translation into active phase 3 trials for patients with newly diagnosed high-risk, ALK-driven neuroblastoma. ClinicalTrials.gov registration: NCT03107988."

Toxicity profile from the same trial, verbatim: *"Common adverse events (AEs) were hypertriglyceridemia (90%), hypercholesterolemia (79%) and weight gain (87%). Neurobehavioral AEs occurred mainly in adults and resolved with dose hold/reduction."*

**Resistance.** Intrinsic resistance of F1174L to crizotinib is the paradigm case (PMID:22789543; PMID:25517749). Acquired resistance to lorlatinib involves bypass pathways — Xie 2026, verbatim: *"Acquired resistance was associated with potential bypass pathway alterations, including BRAF fusions, MET amplification, and NF1 mutations; however, functional validation of these mechanisms is still required."* (PMID:42151367). Trigg & Turner anticipated exactly this: *"It is anticipated that long-term use of these compounds will require combinatorial targeting of pathways downstream of ALK, functionally-related 'bypass' mechanisms and concomitant oncogenic pathways."* (PMID:29642598)

**Rational combinations with direct preclinical support:**
- **mTOR inhibition** to overcome F1174L/MYCN resistance — *"Combined treatment with the ATP-competitive mTOR inhibitor Torin2 overcame the resistance of ALK(F1174L)/MYCN tumors to crizotinib"* (PMID:22789543).
- **RET inhibition (vandetanib)** in MYCN/Alk-mutant mice (Cazes 2014, **[verify primary text]**).
- **ALK inhibitor + GD2 CAR-T** — alectinib relieves PD-L1-mediated immune evasion (PMID:41866626).
- **ALK inhibitor + induction chemotherapy** — the ANBL1531 Arm E design, and PMID:42151367: *"All six newly diagnosed high-risk patients who received lorlatinib in combination with induction chemotherapy achieved an objective response."* With a safety caveat from the same paper: *"Pulmonary toxicity was observed in patients receiving lorlatinib combined with anti-GD2 immunotherapy or chemotherapy."*

### 12.3 Standard risk-stratified neuroblastoma therapy

| Component | NCIT | CHEBI (agents) |
|---|---|---|
| Surgery (resection of primary; resection of ganglioneuroma) | **NCIT:C15329** *Surgical Procedure* **[verified]** | — |
| Induction chemotherapy | **NCIT:C15632** *Chemotherapy* **[verified]** | **CHEBI:4027** cyclophosphamide, **CHEBI:63632** topotecan, **CHEBI:27899** cisplatin, **CHEBI:4911** etoposide, **CHEBI:28445** vincristine, **CHEBI:28748** doxorubicin, **CHEBI:31355** carboplatin — all **[verified]** |
| Myeloablative consolidation with autologous stem-cell rescue | **NCIT:C15431** *Hematopoietic Cell Transplantation* **[verified]** | — |
| Radiotherapy to the primary site | **NCIT:C15313** *Radiation Therapy* **[verified]** | — |
| ¹³¹I-MIBG therapy | **[lead]** | — |
| Anti-GD2 immunotherapy (dinutuximab ± GM-CSF/IL-2) | **NCIT:C15262** *Immunotherapy* **[verified]**; **NCIT:C1570** *Dinutuximab* **[verified]** OLS4 | — |
| Differentiation therapy (13-*cis*-retinoic acid) | **NCIT:C603** *Isotretinoin* **[verified]** | **CHEBI:6067** isotretinoin **[verified]** |
| Observation only (low-risk infant disease) | **[lead]** | — |
| Supportive care | **NCIT:C15747** *Supportive Care* **[verified]** | — |
| Genetic counselling | **NCIT:C15240** *Genetic Counseling* **[verified]** | — |

### 12.4 Pharmacogenomics

- **The germline *ALK* genotype is itself the pharmacogenomic determinant** — which hotspot a carrier has predicts ALK-inhibitor sensitivity (PMID:25517749). This is an unusual case where the predisposition allele and the drug-response allele are the same variant.
- **Cisplatin ototoxicity pharmacogenomics** (*TPMT*, *COMT*, *ACYP2* variants) is relevant to anyone receiving platinum-based induction but is not *ALK*-specific. **[lead]**
- No CPIC guideline exists for ALK inhibitors.

### 12.5 Advanced therapeutics

- **Gene therapy / gene editing:** none in development. Mechanistically unattractive — the target is a dominant gain-of-function allele in a tissue that cannot be reached; small-molecule inhibition already achieves the same end.
- **Cell therapy:** GD2-directed CAR-T, with ALK inhibitor combination support (PMID:41866626). Also anti-GD2 antibody-drug conjugates in early development (NCIT:C212045 *Anti-GD2 Antibody-drug Conjugate M3554* **[verified]** OLS4).
- **RNA-based therapy:** no ASO or siRNA programme for *ALK* in neuroblastoma identified. Noted as absent.

### 12.6 Clinical trials

| Trial | NCT | Description |
|---|---|---|
| ADVL0912 | **NCT00939770** | COG phase 1 crizotinib in paediatric refractory solid tumours and ALCL (PMID:23598171) |
| NANT 2015-02 | **NCT03107988** | First-in-child lorlatinib ± chemotherapy in ALK-driven relapsed/refractory neuroblastoma (PMID:37012551) |
| ANBL1531 | **NCT03126916** | COG phase 3, newly diagnosed high-risk neuroblastoma, testing addition of ¹³¹I-MIBG **or lorlatinib (Arm E)** to intensive therapy. Opened May 2018 at 163 COG institutions; closed to accrual except Arm E in September 2023 **[lead — from secondary sources; Arm E outcome data not located]** |
| LDK378 (ceritinib) paediatric | **NCT01742286** | Phase 1 in paediatric malignancies with ALK alteration |
| Lorlatinib real-world data | **NCT04753658** | Observational collection in paediatric neuroblastoma treated with lorlatinib |

**NCT identifiers above are transcribed from retrieved search results and the Goldsmith abstract; each should be re-fetched and cached before being written into a KB entry.**

### 12.7 Treatment algorithm for a germline-*ALK* carrier

1. Risk-stratify the tumour by INRG criteria exactly as for any neuroblastoma.
2. Determine the **specific *ALK* allele** and its predicted inhibitor sensitivity (PMID:25517749), plus *MYCN* status.
3. Low-risk/infant disease: observation or surgery alone; do not escalate on the basis of the germline finding alone.
4. Intermediate/high-risk: standard multimodal therapy, with **lorlatinib added for ALK-driven disease** where a trial or access route permits (PMID:37012551; ANBL1531 Arm E).
5. Relapsed/refractory ALK-driven disease: lorlatinib ± chemotherapy (PMID:37012551).
6. Ganglioneuroma: resection alone (PMID:20301782).
7. Throughout: genetic counselling, cascade testing of at-risk relatives, and entry into the surveillance protocol (§13).
8. **Open question** — whether ALK inhibition should be first-line, possibly as monotherapy, in germline carriers (PMID:40294355). Not current standard of care.

---

## 13. Prevention

### 13.1 Primary prevention

**None exists.** The germline variant cannot be removed, and no modifiable risk factor has been identified. The only true primary-prevention option is **reproductive**: preimplantation or prenatal genetic testing. GeneReviews, verbatim: *"Once the germline ALK activating pathogenic variant has been identified in an affected family member, genetic testing of at-risk asymptomatic relatives and prenatal/preimplantation genetic testing are possible."* (PMID:20301782) Given ~50% penetrance, variable expressivity and the curability of much neuroblastoma, this is a genuinely value-laden decision requiring counselling rather than a recommendation.

### 13.2 Secondary prevention — the surveillance protocol

This is the core actionable content of the entry. GeneReviews, verbatim (PMID:20301782):

> "In asymptomatic children and after successful treatment of neuroblastic tumors: abdominal ultrasound and urine catecholamine metabolite levels (homovanillic acid and vanillylmandelic acid) every three months and physical examination and chest radiograph every six months between birth and age six years; physical examination, abdominal ultrasound, and measurement of urine catecholamine metabolite levels every six months and chest radiograph every six to 12 months between ages six and ten years. Screening beyond age ten years is not indicated."

| Age | Abdominal ultrasound | Urine HVA/VMA | Physical examination | Chest radiograph |
|---|---|---|---|---|
| **Birth – 6 y** | every 3 months | every 3 months | every 6 months | every 6 months |
| **6 – 10 y** | every 6 months | every 6 months | every 6 months | every 6–12 months |
| **>10 y** | *"Screening beyond age ten years is not indicated"* | — | — | — |

**The 2024 AACR workshop reviewed and retained this framework**, describing *"minor updates to surveillance recommendations that were published previously in 2017"* (PMID:38860978). The specific text of those minor updates sits in the article body, which I could not retrieve; the abstract alone does not say what changed.

**Dissenting position on the age-10 cut-off.** Mossé et al. 2025 argue the cut-off is unsafe given a carrier who presented at 36, recommending *"annual"* surveillance *"through adulthood"* using *"ctDNA and whole-body MRIs"* (PMID:40294355). Record both.

### 13.3 Tertiary prevention

Surveillance continues *"after successful treatment of neuroblastic tumors"* (PMID:20301782) — a carrier who is cured of one tumour remains at risk of a metachronous new primary, which is exactly what the kindred in PMID:40294355 demonstrates.

### 13.4 Risk stratification, counselling and public health

- **Risk stratification** within the carrier population is currently crude: allele identity (R1275Q > G1128A) and age are the only usable axes, and the quantitative penetrance-by-allele figures are weakly sourced (§9.2).
- **Genetic counselling** (NCIT:C15240 **[verified]**) must cover: autosomal dominant inheritance with 50% transmission risk; ~50% penetrance so that a carrier child may never develop a tumour; the possibility of an unaffected transmitting parent; variable expressivity; and the surveillance burden.
- **Cascade testing** of sibs under 10 and subsequently born sibs is explicitly recommended (PMID:20301782).
- **Immunisation, behavioural intervention, environmental intervention, prophylactic medication or surgery: none applicable.** There is no chemoprevention, and prophylactic adrenalectomy has no role — tumours arise along the entire sympathetic chain, not only in the adrenal.

---

## 14. Other Species / Natural Disease

- **Taxonomy of species with a described *Alk*/ALK role:** *Mus musculus* NCBITaxon:10090 **[verified]**; *Danio rerio* NCBITaxon:7955 **[verified]**; *Drosophila melanogaster* NCBITaxon:7227 **[verified]**; *Caenorhabditis elegans* NCBITaxon:6239 **[verified]**; *Homo sapiens* NCBITaxon:9606 **[verified]**.
- **Breed:** not applicable — no VBO term warranted.
- **Orthologous genes:** mouse *Alk* (the knock-in residues are numbered **F1178L** and **R1279Q**, corresponding to human **F1174L** and **R1275Q** — a numbering offset curators must not collapse); zebrafish *alk*; *Drosophila* **Alk**, whose ligand **Jelly belly (Jeb)** patterns visceral muscle founder cells. NCBI Gene IDs **[lead]**, not resolved this session.
- **Naturally occurring disease in other species:** **none identified.** I found no OMIA entry or veterinary case series describing spontaneous *ALK*-driven neuroblastic tumours in companion animals or wildlife. Every animal model discussed in §15 is engineered. This is a real negative and should be recorded rather than left blank.
- **Comparative pathology:** the engineered mouse tumours are a close phenocopy — Heukamp 2012, verbatim: *"Tumors resembled human neuroblastomas in morphology, metastasis pattern, gene expression, and the presence of neurosecretory vesicles as well as synaptic structures."* (PMID:22764207)
- **Evolutionary conservation:** the ALK–MYCN cooperation and the developmental programme it subverts are conserved from zebrafish to human (PMID:22439933). The *LMO1* regulatory mechanism is conserved *"over 400 million years of evolution, separating zebrafish and humans"* (PMID:37183825).
- **Transmission / zoonosis:** not applicable.

---

## 15. Model Organisms

### 15.1 Mouse

| Model | Type | Key finding | Reference |
|---|---|---|---|
| **TH-*ALK*^F1174L transgenic** (neural-crest/tyrosine-hydroxylase-targeted) | Transgenic | *"targeted expression of the most frequent and aggressive variant, ALK(F1174L), is tumorigenic in mice"*; tumours phenocopy human NB in morphology, metastasis, expression and ultrastructure; syntenic 17q gain and *MYCN* amplification; *"Treatment of ALK(F1174L) transgenic mice with the ALK inhibitor TAE-684 induced complete tumor regression"* | Heukamp 2012, PMID:22764207 |
| ***ALK*^F1174L + *MYCN*** (neural-crest overexpression) | Compound transgenic | *"co-expression of these two oncogenes led to the development of neuroblastomas with earlier onset, higher penetrance, and enhanced lethality"*; MYCN dosage increased via PI3K/AKT/mTOR; Torin2 overcomes crizotinib resistance | Berry 2012, PMID:22789543 |
| ***Alk*^F1178L knock-in** (≡ human F1174L) | Knock-in, endogenous locus | Enlarged superior cervical and stellate ganglia from E12.5; hyperactivation causes neonatal lethality in the homozygote; cooperates with *MYCN*, shorter latency than R1279Q | Cazes 2014, *Oncotarget* — **[lead; abstracts not retrieved]** |
| ***Alk*^R1279Q knock-in** (≡ human **R1275Q**, the principal germline allele) | Knock-in, endogenous locus | **The most faithful genetic model of this syndrome.** Enlarged sympathetic ganglia; increased sympathetic neuron proliferation at birth; first in vivo demonstration that R1279Q cooperates with *MYCN*; RET upregulation; vandetanib impairs tumour growth | Cazes 2014, *Oncotarget* (PMC4058037) — **[lead; verify primary text]** |
| ***Alk* kinase-domain knockout** | Knockout | Homozygotes **viable**, with *"an age-dependent increase in basal hippocampal progenitor proliferation"*, altered behaviour, and *"an increase in basal dopaminergic signalling selectively within the frontal cortex"* — establishing that ALK is dispensable for viability, which is the safety rationale for pharmacological inhibition | Bilsland 2008, *Neuropsychopharmacology*, PMID:17487225 |

### 15.2 Zebrafish

**MYCN transgenic ± activated ALK** (Zhu et al., *Cancer Cell* 2012, PMID:22439933). The mechanistically richest model, and the one that best explains the incomplete penetrance of the human syndrome, verbatim: *"Coexpression of activated ALK with MYCN in this model triples the disease penetrance and markedly accelerates tumor onset... Coexpression of activated ALK with MYCN provides prosurvival signals that block this apoptotic response and allow continued expansion and oncogenic transformation of hyperplastic neuroblasts."* The companion *LMO1* knock-in zebrafish (PMID:37183825) models a penetrance modifier.

### 15.3 Human cellular and organoid systems

- **Neuroblastoma cell lines** with endogenous *ALK* lesions — KELLY and SH-SY5Y (F1174L), CLB-GA (R1275Q), NB-1 (*ALK*-amplified), IMR-5 (used as the isogenic background in the *BARD1* work, PMID:37688570). Line identities are **[lead]** pending Cellosaurus verification.
- **Ba/F3 transformation assay** — the standard functional test for whether an *ALK* variant is activating (PMID:18923525), and therefore directly relevant to classifying a novel germline VUS.
- **NIH3T3 transformation / soft-agar / nude-mouse xenograft** (PMID:18923524).
- **hiPSC-derived neural crest** — Shi et al. 2026 (PMID:41560679) generated NB-like tumours from MYCN+ALK-expressing **cranial** NCCs, acquiring NF1 loss and 17q gain; *"This model provides a valuable platform for studying the biological mechanisms driving ALK and MYCN amplification in NB derived from cNCCs."*
- **hPSC sympathoadrenal differentiation** is the system in which the 2026 R1275Q/SCP-like-cell preprint works (unread; §6.2).

### 15.4 Phenotype recapitulation and limitations

**What the models reproduce well:** tumour histology, anatomical site, metastatic pattern, the cytogenetic landscape, ALK dependency and inhibitor response, the ALK×MYCN synergy, and — in the knock-in lines — the *pre-neoplastic* sympathetic ganglion hyperplasia that is arguably the true phenotype of the human germline state.

**What they do not reproduce, and what a curated model record must say:**
1. **Penetrance is engineered away.** The compound *MYCN*/*Alk* models approach complete penetrance; the human syndrome is ~50% penetrant. The models therefore model *tumour formation given a second hit*, not *risk*.
2. **Transgenic overexpression is not a germline allele.** The TH-*ALK*^F1174L and *MYCN* models use supraphysiological, promoter-driven expression; only the **knock-in** lines carry one mutant allele at the endogenous locus at physiological dosage, which is what the human carrier has.
3. **Residue numbering differs** (mouse F1178L/R1279Q vs human F1174L/R1275Q) — a trap for automated cross-species annotation.
4. **Human-specific developmental biology is absent.** The adrenal-medulla developmental programme, including the contribution of Schwann cell precursors and the human-specific timing of sympathoadrenal commitment, is not reproduced in zebrafish and is incompletely reproduced in mouse. This is a candidate `HUMAN_MODEL_MISMATCH` rather than a plain knowledge gap.
5. **The germline CNS/brainstem phenotype** (PMID:21972109) has no reported animal counterpart, and the *Alk*-knockout behavioural phenotype (PMID:17487225) is a loss-of-function phenotype that cannot speak to it.
6. **No model of the adult-onset branch** (PMID:40294355) exists.

### 15.5 Resources

MGI (mouse), ZFIN (zebrafish), IMSR/EMMA/MMRRC (strain repositories), Cellosaurus and ATCC (cell lines), Alliance of Genome Resources (orthology), DepMap (dependency). None queried this session; all accession-level claims must be verified before use.

---

## Summary of evidence quality and explicit gaps

**Strongest evidence (multiple independent human studies + animal corroboration):**
- *ALK* germline activating variants cause familial neuroblastoma (4 independent 2008 *Nature* papers; PMID:18724359, 18923523, 18923524, 18923525)
- Constitutive kinase activation is the mechanism (same four, plus PMID:34819673 for the wild-type baseline)
- ALK × MYCN cooperation (3 independent animal systems: PMID:22789543, 22439933, 22764207)
- Variant-specific inhibitor sensitivity (PMID:25517749)
- Lorlatinib activity in ALK-driven neuroblastoma (PMID:37012551, corroborated PMID:42151367, PMID:42499277)
- The surveillance protocol as consensus guidance (PMID:20301782, PMID:28674118, PMID:38860978)

**Weak or single-source claims that must be labelled as such:**
- Variant-specific penetrance figures (the "G1128A ≈40%" number is **unverified** — it reached me only through a search-engine rendering of GeneReviews body text)
- De novo rate — explicitly **unknown** (PMID:20301782)
- Adult-onset risk and the case for lifelong surveillance — a **single kindred** (PMID:40294355)
- The residue assignment (F1174V/F1245V) in the germline encephalopathy cases
- RET upregulation as a therapeutic axis — the quotes I have are from a secondary summary, not retrieved primary text
- All incidence figures in §9.1

**Genuine absences, which should be recorded as negatives rather than omitted:**
environmental risk and protective factors; gene–environment interaction; QoL data; proteomic, metabolomic and lipidomic profiles; naturally occurring disease in other species; carrier frequency; germline mosaicism; founder effects; survival data for carriers as a group; an *ALK*-specific staging or risk system.

**Flag for the curator on scope and granularity:** MONDO:0013083 is a *susceptibility* concept, and dismech's stub vocabulary has an `OUT_OF_SCOPE` value for "a phenotype, susceptibility term, or category too abstract to carry a mechanism." That judgement does **not** apply here — this entity carries a complete, well-evidenced causal chain from a specific germline lesion through a defined developmental cell population to a tumour, including a branch point that explains its own incomplete penetrance. It should be curated as a `DISEASE`, kept distinct from any somatic neuroblastoma entry, and wired so the germline node is upstream of the shared ALK-activation mechanism. Note also the repository's own rule that germline predisposition syndromes follow the plain Mendelian lump/split rules and stay separate from the somatic cancer entries they predispose to.

---

## Sources

- [Mossé YP et al. Identification of ALK as a major familial neuroblastoma predisposition gene. Nature 2008 (PMID:18724359)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18724359&resultType=core&format=json)
- [Janoueix-Lerosey I et al. Somatic and germline activating mutations of the ALK kinase receptor in neuroblastoma. Nature 2008 (PMID:18923523)](https://doi.org/10.1038/nature07398)
- [Chen Y et al. Oncogenic mutations of ALK kinase in neuroblastoma. Nature 2008 (PMID:18923524)](https://doi.org/10.1038/nature07399)
- [George RE et al. Activating mutations in ALK provide a therapeutic target in neuroblastoma. Nature 2008 (PMID:18923525)](https://doi.org/10.1038/nature07397)
- [Greengard EG, Perrino MR, Park JR. ALK-Related Neuroblastic Tumor Susceptibility. GeneReviews® (PMID:20301782, NBK24599)](https://www.ncbi.nlm.nih.gov/books/NBK24599/)
- [de Pontual L et al. Germline gain-of-function mutations of ALK disrupt central nervous system development. Hum Mutat 2011 (PMID:21972109)](https://onlinelibrary.wiley.com/doi/10.1002/humu.21442)
- [Wilkie AOM. New germline syndrome with brainstem abnormalities and neuroblastoma, caused by ALK mutation. Hum Mutat 2011 (PMID:21972113)](https://pubmed.ncbi.nlm.nih.gov/21972113/)
- [Bourdeaut F et al. ALK germline mutations in patients with neuroblastoma: a rare and weakly penetrant syndrome. Eur J Hum Genet 2012 (PMID:22071890)](https://www.nature.com/articles/ejhg2011195)
- [Berry T et al. The ALK(F1174L) mutation potentiates the oncogenic activity of MYCN in neuroblastoma. Cancer Cell 2012 (PMID:22789543)](https://doi.org/10.1016/j.ccr.2012.06.001)
- [Zhu S et al. Activated ALK collaborates with MYCN in neuroblastoma pathogenesis. Cancer Cell 2012 (PMID:22439933)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3315700/)
- [Heukamp LC et al. Targeted expression of mutated ALK induces neuroblastoma in transgenic mice. Sci Transl Med 2012 (PMID:22764207)](https://doi.org/10.1126/scitranslmed.3003967)
- [Mossé YP et al. Safety and activity of crizotinib... Lancet Oncol 2013 (PMID:23598171)](https://doi.org/10.1016/s1470-2045(13)70095-0)
- [Pugh TJ et al. The genetic landscape of high-risk neuroblastoma. Nat Genet 2013 (PMID:23334666)](https://doi.org/10.1038/ng.2529)
- [Bresler SC et al. ALK mutations confer differential oncogenic activation and sensitivity to ALK inhibition therapy in neuroblastoma. Cancer Cell 2014 (PMID:25517749)](https://doi.org/10.1016/j.ccell.2014.09.019)
- [Cazes A et al. Activated Alk triggers prolonged neurogenesis and Ret upregulation... Oncotarget 2014 (PMC4058037)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4058037/)
- [Bellini A et al. Deep Sequencing Reveals Occurrence of Subclonal ALK Mutations in Neuroblastoma at Diagnosis. Clin Cancer Res 2015 (PMID:26059187)](https://doi.org/10.1158/1078-0432.CCR-15-0423)
- [Oldridge DA et al. Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism. Nature 2015 (PMID:26560027)](https://doi.org/10.1038/nature15540)
- [Matthay KK et al. Neuroblastoma. Nat Rev Dis Primers 2016 (PMID:27830764)](https://www.nature.com/articles/nrdp201678)
- [Kamihara J et al. Retinoblastoma and Neuroblastoma Predisposition and Surveillance. Clin Cancer Res 2017 (PMID:28674118)](https://doi.org/10.1158/1078-0432.CCR-17-0652)
- [Trigg RM, Turner SD. ALK in Neuroblastoma: Biological and Therapeutic Implications. Cancers 2018 (PMID:29642598)](https://doi.org/10.3390/cancers10040113)
- [Barr EK, Applebaum MA. Genetic Predisposition to Neuroblastoma. Children 2018 (PMID:30200332)](https://www.mdpi.com/2227-9067/5/9/119)
- [Reshetnyak AV et al. Mechanism for the activation of the anaplastic lymphoma kinase receptor. Nature 2021 (PMID:34819673)](https://doi.org/10.1038/s41586-021-04140-8)
- [Goldsmith KC et al. Lorlatinib with or without chemotherapy in ALK-driven refractory/relapsed neuroblastoma. Nat Med 2023 (PMID:37012551)](https://doi.org/10.1038/s41591-023-02297-5)
- [Rosswog C et al. Genomic ALK alterations in primary and relapsed neuroblastoma. Br J Cancer 2023 (PMID:36807339)](https://www.nature.com/articles/s41416-023-02208-y)
- [Weichert-Leahey N et al. Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state. J Clin Invest 2023 (PMID:37183825)](https://doi.org/10.1172/jci166919)
- [Kim J et al. Germline pathogenic variants in neuroblastoma patients are enriched in BARD1 and predict worse survival. JNCI 2024 (PMID:37688579)](https://doi.org/10.1093/jnci/djad183)
- [Randall MP et al. BARD1 germline variants induce haploinsufficiency and DNA repair defects in neuroblastoma. JNCI 2024 (PMID:37688570)](https://doi.org/10.1093/jnci/djad182)
- [Kamihara J et al. Neuroblastoma Predisposition and Surveillance—An Update from the 2023 AACR Childhood Cancer Predisposition Workshop. Clin Cancer Res 2024 (PMID:38860978)](https://aacrjournals.org/clincancerres/article/30/15/3137/746580/Neuroblastoma-Predisposition-and-Surveillance-An)
- [Mossé YP et al. Anaplastic Lymphoma Kinase Inhibition Therapy for Hereditary Neuroblastoma. JCO Precis Oncol 2025 (PMID:40294355)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12039971/)
- [Xie W et al. Lorlatinib monotherapy or combination therapy in ALK-driven high-risk neuroblastoma. NPJ Precis Oncol 2026 (PMID:42151367)](https://www.nature.com/articles/s41698-026-01487-x)
- [Shi T et al. Coexpression of MYCN and ALK Induces Neuroblastoma-Like Tumors From Human iPS Cell-Derived Cranial Neural Crest Cells. Genes Cells 2026 (PMID:41560679)](https://doi.org/10.1111/gtc.70083)
- [Sugitatsu Y et al. Alectinib boosts anti-tumor efficacy of GD2 CAR-T cells in ALK-mutated neuroblastoma. Br J Cancer 2026 (PMID:41866626)](https://doi.org/10.1038/s41416-026-03363-8)
- [Imazu T et al. Feasibility and Efficacy of Lorlatinib in Japanese Patients With Relapsed/Refractory ALK-Aberrant Neuroblastoma. Pediatr Blood Cancer 2026 (PMID:42499277)](https://doi.org/10.1002/1545-5017.70511)
- [Bilsland JG et al. Behavioral and neurochemical alterations in mice deficient in anaplastic lymphoma kinase. Neuropsychopharmacology 2008 (PMID:17487225)](https://doi.org/10.1038/sj.npp.1301446)
- [ALK R1275Q mutation drives expansion of SCP-like cells during sympathoadrenal commitment (bioRxiv preprint, 27 Jan 2026) — title/date only, content unread](https://www.biorxiv.org/content/10.64898/2026.01.27.701690v1.full)
- [NCT03126916 — ANBL1531, 131I-MIBG or lorlatinib added to intensive therapy for newly diagnosed high-risk neuroblastoma](https://clinicaltrials.gov/study/NCT03126916)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 61 |
| Resolved | 60 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 60 |
| On topic | 31 |
| Off topic | 0 |

60 of 61 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 105 |
| Resolved | 104 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002107` (1 mention) - the report calls it "Liver (stage MS/4S)"; UBERON calls it **liver**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011977` (2 mentions) - the report calls it "Elevated urinary homovanillic acid (HVA)"; HP calls it **Elevated urinary homovanillic acid**
- `HP:0011978` (2 mentions) - the report calls it "Elevated urinary vanillylmandelic acid (VMA)"; HP calls it **Elevated urinary vanillylmandelic acid**
- `GO:0005886` (3 mentions) - the report calls it "Plasma membrane (receptor location)"; GO calls it **plasma membrane**
- `CL:0002375` (1 mention) - the report calls it "Schwann cell precursor (candidate contributor to the sympathoadrenal pool)"; CL calls it **Schwann cell precursor**, and lists "Schwann cell precursor cell" among its other names
- `UBERON:0001807` (1 mention) - the report calls it "Paravertebral ganglion (paraspinal chain)"; UBERON calls it **paravertebral ganglion**
- `UBERON:0001989` (1 mention) - the report calls it "Superior cervical ganglion (enlarged in knock-in mice)"; UBERON calls it **superior cervical ganglion**
- `UBERON:0002240` (1 mention) - the report calls it "Spinal cord (compression, not invasion)"; UBERON calls it **spinal cord**, and lists "spinal cord structure" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `EXT_ID`.