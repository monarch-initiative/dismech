---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-26T19:10:34.523512'
end_time: '2026-11-26T19:18:21.123057'
duration_seconds: 466.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PLPBP Deficiency
  mondo_id: MONDO:0015005
  category: Mendelian
  causal_genes: PLPBP
  omim_id: OMIM:617290
  synonyms: epilepsy, early-onset, vitamin B6-dependent; EPVB6D; EPVB6D
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
  - claude-fable-5-2
  - claude-haiku-5-5
  web_search_requests: 5
  num_turns: 20
  total_cost_usd: 2.67419355
  session_id: 35948a41-7979-4d2b-848c-1d39a6da6426
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 64
  retrieval_calls: 62
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 54
  quotes_valid: 54
  relevance_assessed: 32
  on_topic: 28
  off_topic: 1
  off_topic_references:
  - PMID:10496079
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 38
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 25
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 3
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  service_unreachable: 23
  obsolescence_unchecked: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PLPBP Deficiency
- **MONDO ID:** MONDO:0015005 (if available)
- **Causal gene(s):** PLPBP
- **OMIM:** OMIM:617290
- **Synonyms:** epilepsy, early-onset, vitamin B6-dependent; EPVB6D; EPVB6D
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PLPBP Deficiency** covering all of the
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

Still researching: the PubMed and GeneReviews web pages blocked direct fetches, so I'm pulling abstracts through the NCBI E-utilities API instead, plus ClinVar, mouse-model and trial lookups.

# PLPBP Deficiency (Vitamin B6-Dependent Early-Onset Epilepsy, EPVB6D): Disease Characteristics Report

**Interpretation and scope.** This report covers MONDO:0015005 / OMIM:617290, the autosomal recessive vitamin B6-dependent epilepsy caused by biallelic variants in ***PLPBP*** (HGNC:9457, formerly *PROSC*; protein PLPHP). It does not cover the other B6-dependent epilepsies (*ALDH7A1*, *PNPO*, *ALDH4A1*, *ALPL*).

**Retrieval limits that affect this report.**
- The GeneReviews chapter body, the PubMed HTML pages, OMIM and Orphanet could not be opened (bot checks). GeneReviews content is limited to its PubMed/MedGen summary.
- Abstract quotes were retrieved through NCBI E-utilities and are exact but short (clauses of 125 characters or fewer).
- Items marked **[tool summary – verify]** came through a machine-generated summary of a truncated page, not verbatim text.
- Ontology IDs are given only where retrieved (MONDO, HGNC, HPO via Monarch, ortholog IDs). For GO, CL, UBERON, CHEBI and NCIT I give term labels only; the IDs were not retrieved and need a lookup.

---

## 1. Disease Information

**Overview.** PLPBP deficiency is a treatable vitamin B6-dependent early-onset epileptic encephalopathy caused by biallelic pathogenic variants in *PLPBP*, which encodes the pyridoxal 5'-phosphate homeostasis protein (PLPHP).
- GeneReviews: "PLPBP deficiency is a treatable form of vitamin B6-dependent early-onset epileptic encephalopathy." (PMID 36795901; https://www.ncbi.nlm.nih.gov/books/NBK589231/, posted 2023-02-16)
- Seizures are "unresponsive to (or only partly responsive to) anti-seizure medications (ASMs)" "but typically show an immediate positive response to vitamin B6," (PMID 36795901).
- The disease was defined in 2016 (Darin et al., PMID 27912044) and confirmed in 2017 (Plecko et al., PMID 28391250).

**Identifiers** (Monarch entity record, https://api.monarchinitiative.org/v3/api/entity/MONDO:0015005; HGNC, https://rest.genenames.org/fetch/symbol/PLPBP):

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0015005, "epilepsy, early-onset, vitamin B6-dependent" |
| MONDO parents | MONDO:0009945 (pyridoxine-dependent epilepsy); MONDO:0957599 (epilepsy, early-onset) |
| OMIM phenotype / gene | 617290 / 604436 |
| MedGen / UMLS | 934599 / C4310632 |
| GARD | 0025048 |
| DOID | DOID:0080769 |
| Gene | *PLPBP*, HGNC:9457, NCBI Gene 11212, ENSG00000147471, UniProt O94903, 8p11.23 |
| GeneReviews | NBK589231 (PMID 36795901) |
| Orphanet, ICD-10/11, MeSH | Not retrieved; MONDO lists no ICD or NCIT cross-reference |

**Synonyms.** EPVB6D; PLPHP deficiency; PROSC deficiency; pyridoxal 5'-phosphate homeostasis protein deficiency; PLPBP-related vitamin B6-dependent epilepsy. UniProt labels the disease "Epilepsy, early-onset, 1, vitamin B6-dependent (EPEO1)" (https://rest.uniprot.org/uniprotkb/O94903.json).

**Source type.** All information is aggregated disease-level data from published case reports, case series, systematic reviews and curated resources. No EHR-derived data were used.

---

## 2. Etiology

**Causal factor.** The disease is monogenic: germline biallelic loss-of-function or hypomorphic *PLPBP* variants.
- Darin 2016: a "homozygous nonsense mutation in proline synthetase co-transcribed homolog (bacterial), PROSC" was found in two sibs. Sequencing of 29 further individuals with pyridoxine-responsive epilepsy "identified four additional children with biallelic PROSC mutations." (PMID 27912044)

**Genetic risk and severity factors.**
- Genotype class is the main determinant of severity: "biallelic truncating variants and homozygous variants were linked to severe phenotypes and/or early mortality." (PMID 41671913)
- Parental consanguinity was present in most families in one series (PMID 30668673, full text).
- A French-Canadian founder allele exists (section 9).
- No modifier genes or susceptibility loci have been reported.

**Environmental risk factors.** None cause the disease. Factors that worsen expression:
- Withdrawal of or delay in B6 treatment: "Two patients underwent a controlled pyridoxine withdrawal with signs of encephalopathy within a couple of days." (PMID 28391250)
- Intercurrent viral illness, which preceded an episodic crisis in one child (PMID 42563912).
- Some anti-seizure medications: "Several ASMs (such as carbamazepine, valproate, phenytoin, and phenobarbitone) can cause a low plasma concentration of PLP." (PMID 36795901)

**Protective factors.**
- Genetic: missense and compound heterozygous genotypes are associated "with an attenuated phenotype," (PMID 41671913).
- Environmental: early supraphysiological B6. In the founder-variant families, "both patients, who are alive, had a history of prenatal supplements taken by their mothers as antiemetic medication" "with high doses of pyridoxine." (PMID 33977028). This is an observational association from a handful of patients.

**Gene–environment interaction.** The phenotype depends on B6 supply. Patients have "a lifelong dependency on supraphysiological vitamin B6 supply." (PMID 30671974). In cell models, B6 vitamer imbalance scaled with the pyridoxine or pyridoxamine concentration in the medium (PMID 37451483).

---

## 3. Phenotypes

Frequencies come from three pooled sources, which overlap in the patients they count:
- **A** = systematic review plus multicentre series, n=54 (Alsini 2026, PMID 41671913).
- **B** = review of 54 individuals (Alsubhi 2022, PMID 36324377, Table 1).
- **C** = HPO annotations from the 7 original patients (Monarch, citing PMID 27912044).

| Phenotype | Suggested HPO term | Type | Onset | Frequency | Notes |
|---|---|---|---|---|---|
| Neonatal seizures, drug-resistant, B6-responsive | Neonatal seizure; Vitamin B6-responsive seizures (IDs not retrieved) | Sign | Neonatal | A: onset in first 24 h 55.5%, first week 76%. B: neonatal onset 49/54 (91%), infantile 3/54 (6%) | Severe; episodic; breakthrough with fever or missed doses |
| Tonic seizure | HP:0032792 | Sign | Neonatal | C: 4/4 **[tool summary – verify]** | — |
| Bilateral tonic-clonic seizure | HP:0002069 | Sign | Neonatal–infantile | C: 5/7 **[tool summary – verify]**; "Generalized tonic-clonic seizures were commonly noted." (PMID 30525118) | — |
| Myoclonic seizure / myoclonus | HP:0032794 / HP:0001336 | Sign | Neonatal | C: 3/7 | — |
| Clonic seizure | HP:0020221 | Sign | Neonatal | C: 1/7 **[tool summary – verify]** | — |
| Epileptic (infantile) spasms | Infantile spasms (ID not retrieved) | Sign | Infancy | 4/12 in one series (PMID 30668673) | Can occur without hypsarrhythmia (PMID 36577449) |
| EEG burst suppression | HP:0010851 | EEG | Neonatal | B: 21/54 (39%); 6/11 (PMID 30668673) | Interictal EEG can be near normal (PMID 36577449) |
| Suspected fetal seizures / abnormal fetal movements | Fetal distress HP:0025116; abnormal fetal movement (ID not retrieved) | Prenatal sign | Prenatal | B: 9/54 (17%); fetal distress C: 4/7 | — |
| Prematurity | Premature birth (ID not retrieved) | Sign | Perinatal | Listed among "Common clinical features" (PMID 41671913) | Proposed diagnostic clue (PMID 33728241) |
| Microcephaly | Secondary microcephaly HP:0005484; congenital microcephaly also reported (PMID 36308585) | Sign | Congenital/postnatal | B: 20/54 (37%) | Absent in milder cohort: "All four patients were normocephalic" (PMID 28391250) |
| Global developmental delay / intellectual disability / autism | HP:0001263, HP:0001249 | Developmental | Infancy onward | B: 30/46 (65%); GeneReviews: "more than 50%" | Mild to severe; main driver of long-term disability |
| Delayed or absent speech | HP:0000750, HP:0002465 | Developmental | Childhood | C: 5/6 | — |
| Motor delay | HP:0001270 | Developmental | Infancy | C: 4/6 | — |
| Hypotonia / hypertonia | HP:0001252 / HP:0001276 | Sign | Neonatal | C: 1/7 and 3/7; "most commonly mild hypotonia" (PMID 36795901) | — |
| Irritability / encephalopathy | HP:0000737 | Sign | Neonatal | C: 3/4 **[tool summary – verify]** | — |
| Respiratory insufficiency / apnea | HP:0002093 / HP:0002104 | Sign | Neonatal | C: 3/7 and 1/7; 3/12 (PMID 30668673) | Cause of early death |
| Movement disorder (dystonic/hyperkinetic paroxysms, opsoclonus-myoclonus-like, tremor) | Paroxysmal dyskinesia; Opsoclonus (IDs not retrieved) | Sign | Infancy–childhood | B: 4/54 (7%) | PMIDs 36324377, 42563912, 30668673 |
| Anxiety states, behavioural change | Anxiety (ID not retrieved) | Behavioural | Adolescence | Single reports | PMIDs 31687261, 42563912 |
| Lactic acidaemia / metabolic acidosis | HP:0002151 / HP:0001942 | Lab | Neonatal | C: 4/6 and 5/7; 21/54 (39%) **[tool summary – verify]** | Mimics mitochondrial disease |
| Hyperglycinaemia | Hyperglycinemia (ID not retrieved) | Lab | Neonatal | 13/54 (24%) **[tool summary – verify]** | Mimics glycine encephalopathy |
| Low CSF PLP and pyridoxal | No specific HPO term retrieved | Lab | Pre-treatment | "Pre-treatment cerebrospinal fluid samples showed low PLP concentrations" (PMID 27912044) | — |
| Brain MRI abnormality | — | Imaging | Neonatal | A: 65% | Detailed below |
| White matter abnormality / delayed myelination | Abnormal cerebral white matter morphology (ID not retrieved) | Imaging | — | A: 54% | — |
| Periventricular or temporal cysts | Periventricular cysts (ID not retrieved) | Imaging | — | A: 27% | Marker of the founder variant |
| Simplified gyral pattern / broad gyri, shallow sulci | Simplified gyral pattern (ID not retrieved) | Imaging | — | A: 44% | — |
| Corpus callosum anomaly | Thin corpus callosum (ID not retrieved) | Imaging | — | A: 15.4% | — |
| Brain atrophy / ventriculomegaly | HP:0012444 / HP:0002119 | Imaging | — | C: 1/7 (atrophy) | — |
| Minor facial dysmorphism | HP:0000219, HP:0000343, HP:0000582, HP:0000629 | Sign | — | C: 1–2 of 4 each | Non-specific |
| Esodeviation | HP:0020045 | Sign | — | C: 1/4 | — |

**Quality of life.** No study using a standardised instrument (EQ-5D, SF-36, PROMIS) was retrieved. Impact is inferred from the developmental burden, the need for adjunct ASMs in "almost 60%" (PMID 36795901), and lifelong daily treatment.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PLPBP* (HGNC:9457; previous symbol *PROSC*, "proline synthetase co-transcribed (bacterial homolog)"), at 8p11.23. Reference transcript NM_007198.4. The protein has 275 residues, with PLP bound at Lys47 as a Schiff base (UniProt O94903). The human and mouse genes were cloned in 1999 (PMID 10496079).

**Variant spectrum.**
- "The most common type of variant was missense variants (48%)," "with the variant c.370-373del being the most frequently reported (18.5%)." (PMID 41671913)
- Truncating variants: p.Ser78Ter, p.Gln71Ter, c.207+1G>A, c.320-2A>G, c.370_373del (p.Asp124Lysfs*2) (PMIDs 27912044, 30668673).
- Missense variants: p.Pro40Leu, p.Arg41Gln, p.Glu67Lys, p.Tyr69Cys, p.Pro87Leu, p.Ile94Phe, p.Thr116Ile, p.Leu175Pro, p.Arg205Gln, p.Gly224Ala, p.Arg241Gln (PMIDs 27912044, 28391250, 30668673).
- More recent: p.Ala232Val (PMID 36308585); p.His92Arg and p.Ala107Thr (PMID 40976369); p.Val235Gly (PMID 36324377); c.596dup (PMID 42307184); a CA-duplication frameshift (PMID 33425341).

**ClinVar** (E-utilities query, November 2026): 372 records for *PLPBP*; 78 flagged pathogenic, most of which are large multi-gene copy-number variants spanning 8p; 118 VUS. The likely-pathogenic count could not be retrieved. Examples of gene-specific pathogenic entries: NM_007198.4:c.47_48dup (p.Leu17fs) and an intragenic deletion (VCV 3245576).

**Population frequency and constraint.**
- gnomAD (GRCh38): pLI ≈ 0.00002, LOEUF 0.97, missense o/e 0.87 (https://gnomad.broadinstitute.org). The gene tolerates heterozygous loss of function, as expected for a recessive disorder.
- Per-variant allele frequencies were not retrieved.

**Origin and consequence.**
- All reported variants are germline and inherited; no somatic or mosaic cases were retrieved.
- The functional mechanism is loss of function. p.Ser78Ter and p.Leu175Pro gave undetectable protein in patient fibroblasts (UniProt, citing PMID 27912044).
- Recombinant mutant studies: "The p.Leu175Pro mutation grossly misfolded PLPHP." "PLPHP stability was decreased in p.Arg241Gln, p.Pro40Leu, and p.Arg205Gln mutants (thermofluor assays)." "The p.Arg241Gln and p.Tyr69Cys mutants respectively lacked PLP or had a decreased amount of this cofactor." (PMID 29689137)

**Modifier genes, epigenetics, chromosomal abnormalities.** None reported. The large 8p copy-number variants in ClinVar are contiguous-gene events, not the cause of this recessive disease.

---

## 5. Environmental Information

- **Environmental toxins and infectious agents:** not applicable as causes. Febrile or viral illness triggers breakthrough seizures or crises (PMIDs 28391250, 42563912).
- **Lifestyle and nutrition:** the disease is a dependency on pharmacological B6, not a dietary deficiency. Adherence is the critical factor.
- **Drugs:** enzyme-inducing ASMs and valproate can lower plasma PLP (PMID 36795901).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic germline *PLPBP* variants** result in absent, misfolded, unstable or PLP-binding-deficient PLPHP. *Demonstrated in vitro and in patient fibroblasts* (PMIDs 29689137, 27912044).
2. **Loss of PLPHP leads to disturbed intracellular B6 vitamer homeostasis.** PLP falls, and pyridoxine 5'-phosphate (PNP) and pyridoxamine 5'-phosphate (PMP) accumulate. *Demonstrated in patient fibroblasts, HEK293 knockouts and zebrafish* (PMIDs 30668673, 37451483). The original report found the opposite PLP direction: "cultured fibroblasts showed excessive PLP accumulation." (PMID 27912044); the discrepancy is unresolved.
3. **Two proximate causes of the PLP deficit:**
   - 3a. Reduced PNPO flux: tracer experiments "confirmed lower pyridox(am)ine 5'-phosphate oxidase activity" (PMID 37451483). *Demonstrated in cells.*
   - 3b. Increased PLP hydrolysis: "indicating increased PLP hydrolysis to pyridoxal in PLPHP-deficient cells." "This effect could be partly counteracted by inactivation of pyridoxal phosphatase." (PMID 37451483). This fits the proposed role of PLPHP in "supplying this cofactor to apoenzymes while minimizing any toxic side reactions." (PMID 27912044). *The carrier/chaperone function itself is inferred.*
4. **PLP shortage leads to reduced activity of PLP-dependent enzymes in brain**: "evidence of reduced activity of PLP-dependent enzymes." in pre-treatment CSF (PMID 27912044). The mechanism then branches:
   - **Branch A, neurotransmitters.** Impaired glutamate decarboxylase and aromatic L-amino acid decarboxylase (AADC) results in reduced GABA and altered monoamine synthesis. Zebrafish "had disruptions in amino acid metabolism as well as GABA and catecholamine biosynthesis," (PMID 30668673). In humans, AADC-like metabolites were found in one patient (PMID 30668673) and raised 3-O-methyldopa and 5-hydroxytryptophan in some (PMID 32980745). This leads to neuronal hyperexcitability, seizures, burst suppression and movement disorder. *The GABA link is demonstrated in zebrafish and inferred in humans.*
   - **Branch B, glycine.** Impaired glycine cleavage (a PLP-dependent system) results in hyperglycinaemia. *Inferred in humans.* In *E. coli*, PNP inhibits the glycine cleavage system (PMID 31677193, title only).
   - **Branch C, mitochondria.** PLPHP is partly mitochondrial. Its loss has "a distinct effect on mitochondrial PLP and PMP," "suggesting impaired activity of mitochondrial transaminases." (PMID 37451483). This leads to "Lactate and pyruvate accumulation along with the decrease of tricarboxylic acid cycle intermediates" (PMID 37451483), and clinically to lactic acidaemia and a mitochondrial-encephalopathy-like picture. *Demonstrated in HEK293 cells and yeast; inferred as the cause of patient lactate elevation.*
5. **Prenatal and early postnatal PLP shortage in developing brain** leads to under-development: simplified gyri, white-matter abnormality, cysts and microcephaly. *Inferred from imaging* (PMIDs 41671913, 33977028).
6. **Uncontrolled seizures plus the structural deficit** result in developmental delay and intellectual disability, and in the most severe genotypes respiratory failure and early death (PMID 30668673).
7. **Pharmacological pyridoxine or PLP** partly restores PLP supply to apoenzymes, which results in seizure control. Rescue is incomplete where prenatal injury has occurred or residual protein is absent (PMIDs 33977028, 30525118).

### Supporting detail

- **Protein structure.** A (β/α)8 TIM-barrel fold with PLP bound to Lys47, shown by homology modelling (PMID 30668673). "Normal PLPHP is largely a monomer with PLP bound through a Schiff-base linkage." (PMID 29689137). Cross-linking mass spectrometry found "an unexpected dimeric assembly of PLPBP." (PMID 31825581).
- **Localisation.** Cytosolic and mitochondrial: "the first empirical evidence that PLPHP is localized in mitochondria" (PMID 30668673).
- **Proteomics.** A PLPBP-knockout cell line showed "upregulation of several cytoskeleton- and cell division-associated proteins." (PMID 31825581).
- **Possible additional function.** RNA binding, conserved between bacterial YggS and the human protein: "it is also observed with human PLP-BP." (PMID 39604152). Disease relevance is unknown.
- **Metabolomics.** B6 vitamer profiling by mass spectrometry in fibroblasts, HEK293 cells and zebrafish (PMIDs 30668673, 37451483). No specific patient biomarker has emerged.
- **Not reported:** immune involvement, epigenetic changes, patient transcriptomics, single-cell or spatial studies, lipidomics, CRISPR screens.

**Suggested ontology terms (labels; IDs to be verified).**
- GO biological process: pyridoxal phosphate metabolic process; vitamin B6 metabolic process; gamma-aminobutyric acid biosynthetic process; catecholamine biosynthetic process; glycine catabolic process; tricarboxylic acid cycle.
- GO molecular function: pyridoxal phosphate binding.
- GO cellular component: cytosol; mitochondrion.
- CL: neuron; GABAergic neuron; fibroblast (experimental cell type).
- CHEBI: pyridoxal 5'-phosphate; pyridoxine; pyridoxine 5'-phosphate; pyridoxamine 5'-phosphate; pyridoxal; 4-pyridoxic acid; glycine; lactate; GABA.

---

## 7. Anatomical Structures Affected

- **Primary organ:** brain (central nervous system). Cerebral cortex (gyral simplification, atrophy), cerebral white matter (delayed myelination), periventricular and temporal regions (cysts), corpus callosum (PMIDs 41671913, 33977028).
- **Laterality:** imaging findings are described as diffuse or bilateral. No lateralisation data were retrieved.
- **Secondary:** respiratory failure in severe neonatal cases (PMID 30668673); systemic metabolic acidosis.
- **Other tissues:** a transfection study suggested a role "in cell division" "as well as proper muscle function." (PMID 31825581). This is in vitro only, with no clinical myopathy described.
- **Cell and subcellular level:** neurons (inferred); cytosol and mitochondria (PMID 30668673).
- **Suggested UBERON labels (IDs not retrieved):** brain; cerebral cortex; white matter of cerebral hemisphere; corpus callosum; temporal lobe.

---

## 8. Temporal Development

- **Onset.** Prenatal in a minority (suspected fetal seizures in 17%, PMID 36324377). Otherwise acute and neonatal: "the majority occurring within the first 24 h of life (55.5%) or the first week of life (76%)." (PMID 41671913).
- **Late onset.** Rare. Onset at 3 months (PMID 30525118), and at 8 months with diagnosis at 10 years (PMID 40976369). One patient was untreated until 16 years, with "only mild cognitive impairment and an early-onset, well-controlled epilepsy." (PMID 31687261).
- **Course.** Chronic and lifelong. Seizures are episodic with treatment-induced remission and relapse on withdrawal or with illness. Neurodevelopmental impairment is largely static rather than neurodegenerative. No formal staging exists.
- **Critical window.** Prenatal and early neonatal: "treatment with pyridoxine and/or Pyridoxal-5-phophate has to be started immediately" (PMID 33977028). Even so, "Even with early appropriate treatment, neurological outcome of our patient is still poor." in the founder genotype (PMID 33977028).

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007). Sibs have "a 25% chance of being affected," (PMID 36795901).
- **Penetrance:** apparently complete for biallelic pathogenic genotypes; no unaffected biallelic individuals were retrieved.
- **Expressivity:** highly variable. "PLPBP mutations cause variable phenotypes of developmental and epileptic encephalopathy." (PMID 30525118).
- **Anticipation, germline mosaicism:** not reported.
- **Prevalence and incidence:** unknown and ultra-rare. Published cases: about 30 by 2020 (PMID 33425341), 54 by 2022 (PMID 36324377), 54 in the 2026 systematic set (PMID 41671913). No population estimate was retrieved.
- **Diagnostic yield:** 4 of 700 patients in a developmental and epileptic encephalopathy cohort (PMID 30525118); 4 of 29 with unexplained pyridoxine-responsive epilepsy (PMID 27912044).
- **Founder effect:** c.370_373del (p.Asp124Lysfs*2) in the Saguenay–Lac-St-Jean region of Quebec. "Haplotype analysis showed a single shared profile for the affected persons and their parents," (PMID 33977028).
- **Consanguinity:** frequent in reported families (PMIDs 27912044, 30668673, 33425341).
- **Carrier frequency:** not established.
- **Geography and ancestry:** pan-ethnic. Reports come from Europe, Canada, Japan, China, Pakistan, India, Turkey, Saudi Arabia/Oman and Iran (PMIDs 30668673, 30525118, 31737911, 33425341, 34316313, 36308585, 31831980, 42307184).
- **Sex ratio:** 6 males to 6 females in one series (PMID 30668673); no sex bias is expected.

---

## 10. Diagnostics

**No specific biomarker exists.** "Unlike other causes of vitamin B6-dependent epilepsies; however, a specific biomarker for this disorder has yet to be identified." (PMID 33728241)

**Laboratory findings.**
- Pre-treatment CSF PLP is low (PMID 27912044). CSF pyridoxal may be more specific: "Low cerebrospinal fluid pyridoxal concentrations may be a better indicator of pyridoxal 5'-phosphate deficiency" (PMID 32980745).
- Plasma B6 vitamers on treatment are not discriminating: "Vitamin B6 plasma profiles on pyridoxine did not enable the differentiation of patients with PROSC mutations." (PMID 28391250). One untreated patient had plasma PLP of 1.1 nM against a reference above 20.5 (PMID 30668673, full text).
- Lactate and glycine are often raised: "Hyperglycinemia and hyperlactatemia are the most consistently observed biochemical abnormalities" (PMID 31741821).
- Negative markers help exclude other causes: urinary α-aminoadipic semialdehyde is normal, which distinguishes it from *ALDH7A1* deficiency (PMID 36577449).

**EEG.** Burst suppression, focal or multifocal discharges, or diffuse slowing (PMID 30525118). The EEG can be near normal.

**MRI.** Abnormal in about 65% (section 3). Magnetic resonance spectroscopy showed a lactate doublet in 2 patients (PMID 30668673). Temporal cysts are a marker of the founder genotype (PMID 33977028).

**Genetic testing.**
- The diagnosis is established by "biallelic pathogenic variants in PLPBP identified by molecular genetic testing." (PMID 36795901).
- Recommended approach: an epilepsy or metabolic gene panel that includes *PLPBP*, or exome/genome sequencing. Older panels may omit the gene: a child with a "previous nondiagnostic epilepsy gene panel" was diagnosed by exome (PMID 42563912). "PLPHP should be included systematically in NGS epilepsy gene panels." (PMID 36577449).
- Copy-number analysis is relevant because an intragenic deletion is recorded in ClinVar.
- Karyotype, FISH, mitochondrial DNA and repeat-expansion testing are not indicated.

**Therapeutic trial.** Clinical and EEG response to pyridoxine or PLP supports the diagnosis, but the response may be partial.

**Clinical criteria.** None exist; this is consistent with GeneReviews (per search summary of NBK589231).

**Differential diagnosis.**
- *ALDH7A1* and *PNPO* deficiency: the phenotype "was indistinguishable" "from ALDH7A1 and PNPO deficiency." (PMID 28391250).
- Mitochondrial encephalopathy (lactate), glycine encephalopathy (glycine), AADC deficiency, folinic acid-responsive seizures, hypoxic-ischaemic encephalopathy, opsoclonus-myoclonus-ataxia syndrome (PMIDs 31741821, 30668673, 42563912).

**Screening.**
- No biochemical newborn screening exists.
- Pyridoxine-dependent epilepsy as a group is included in genomic newborn-screening studies (NCT05687474 Baby Detect; NCT03655223 Early Check); whether *PLPBP* itself is on those panels was not verified.
- Cascade testing of sibs and prenatal diagnosis are available (PMID 36795901).

---

## 11. Outcome / Prognosis

- **Mortality.** 8 of 54 (15%) died, at ages from 2 weeks to 16 months (PMID 36324377, Table 1). Deaths cluster in truncating genotypes with a mitochondrial-like neonatal presentation and respiratory failure (PMID 30668673). No survival curves or life-expectancy data exist; the oldest described patients are adults aged 30 and 35 (PMIDs 28391250, 36324377).
- **Seizure outcome.** Seizure-free on maintenance treatment in 31 of 45 (69%) (PMID 36324377). "almost 60% of individuals require adjunct ASMs" (PMID 36795901).
- **Neurodevelopment.** Developmental delay, intellectual disability or autism in 30 of 46 (65%) (PMID 36324377). "more than two thirds of patients were classified as having moderate to severe disease." (PMID 41671913). Normal outcome is possible: "Three had favourable outcome with normal intellectual properties at age 12.5, 15.5 and 30 years, respectively," (PMID 28391250).
- **Prognostic factors.** Genotype (truncating or homozygous is worse; missense or compound heterozygous is milder), brain malformation on MRI, prenatal onset, and treatment delay (PMIDs 41671913, 30668673, 33977028). Early treatment does not guarantee a normal outcome (PMID 30525118).
- **Prognostic biomarkers.** None: "metabolic biomarkers for early detection and prognosis of PLPBP deficiency are currently still lacking." (PMID 31741821).
- **Quality-of-life measures.** None published.

---

## 12. Treatment

**Pharmacotherapy (targeted).**
- **Pyridoxine (PN)** or **pyridoxal 5'-phosphate (PLP)**, lifelong: "Targeted therapy is lifelong pharmacologic treatment with either PN or PLP, and often with additional ASMs." (PMID 36795901).
- **Doses in practice.** PN 4.7–23 mg/kg/day and PLP 30–58 mg/kg/day in one series (PMID 30668673, Table 1). Across all B6-dependent epilepsies, "Pyridoxine dosage ranged between 1 and 55 mg/kg/die." (PMID 36980111). GeneReviews dosing recommendations could not be retrieved.
- **Response.** A first B6 trial gave complete seizure resolution in 36 of 44 (82%) (PMID 36324377, Table 1).
- **PN versus PLP.** Evidence is mixed. "PLP has been advocated as the treatment of choice for PLPBP defect," "but oral PN has also demonstrated good seizure control in some patients, including ours." (PMID 33425341). Switching between them helps some patients and not others (PMID 30668673).
- **Folinic acid.** Added in individual partial responders with benefit (PMID 30668673). Evidence is anecdotal.
- **Adjunct ASMs.** Oxcarbazepine, lamotrigine, clobazam, phenobarbital, valproate (PMIDs 30668673, 28391250). ASMs that lower PLP should be used with awareness (PMID 36795901).

**Adverse effects.** High-dose pyridoxine carries a concern of sensory neuropathy, which prompted dose reduction in one adult on 1,200 mg/day (PMID 36324377). No systematic adverse-event data specific to this disease were retrieved.

**Treatment algorithm (synthesised from the sources above).**
1. Give a B6 trial to any neonate or infant with drug-resistant seizures. One group suggests "the introduction of pyridoxine in all infants when two ASMs have failed." (PMID 42516410).
2. Continue until genetic results return (PMID 33977028).
3. If the response is partial, trial PLP and/or folinic acid and add ASMs.
4. Do not withdraw B6 once the diagnosis is confirmed.

**Not applicable or not available.**
- Gene therapy, cell therapy, RNA therapies, immunotherapy, surgery: none reported.
- Pharmacochaperones: proposed only on in vitro grounds for destabilising missense variants, "suggesting the potential of pharmacochaperone-based therapeutic approaches." (PMID 29689137).
- Lysine-restricted diet and arginine: relevant to *ALDH7A1* deficiency, not to PLPBP deficiency.
- Pharmacogenomics: no data.

**Supportive care.** Neurology, developmental paediatrics, speech-language, physical and occupational therapy (PMID 36795901 summary).

**Clinical trials.** No interventional trial specific to PLPBP deficiency was found on ClinicalTrials.gov. The related entries (NCT01795170, NCT04672226, NCT06054347) concern pyridoxine-dependent epilepsy in general or *ALDH7A1* deficiency.

**Suggested NCIT labels (IDs not retrieved).** Pyridoxine; Pyridoxal Phosphate; Leucovorin (folinic acid); Anticonvulsant Agent; Physical Therapy; Speech Therapy; Occupational Therapy; Genetic Counseling.

---

## 13. Prevention

- **Primary:** genetic counselling for an autosomal recessive condition, carrier testing of relatives once familial variants are known, and prenatal or preimplantation testing. "prenatal molecular genetic testing may be performed via amniocentesis or chorionic villus sampling" (PMID 36795901).
- **Secondary:** in at-risk newborns awaiting results, either treat with PN or PLP from birth, or monitor clinically and by EEG and treat at the first sign of seizures or encephalopathy (PMID 36795901 summary). Use an early B6 trial in unexplained neonatal seizures.
- **Maternal prenatal pyridoxine:** survival was associated with maternal high-dose pyridoxine in the founder families (PMID 33977028). No formal prenatal treatment protocol was retrieved.
- **Tertiary:** strict lifelong adherence, a plan for breakthrough seizures during febrile illness, awareness of PLP-lowering ASMs, and developmental therapies.
- **Immunisation, behavioural, public-health or environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Natural disease.** No naturally occurring animal disease attributed to a *PLPBP* ortholog was retrieved (OMIA was not searched successfully). There is no zoonotic or transmission relevance.
- **Orthologs** (Alliance of Genome Resources):

| Species | Gene | ID |
|---|---|---|
| *Mus musculus* | Plpbp | MGI:1891207 |
| *Rattus norvegicus* | Plpbp | RGD:1308962 |
| *Danio rerio* | plpbp | ZFIN:ZDB-GENE-030131-1378 |
| *Xenopus tropicalis* | plpbp | Xenbase:XB-GENE-950135 |
| *Drosophila melanogaster* | CG1983 | FBgn0039751 |
| *Caenorhabditis elegans* | F09E5.8 | WBGene00017286 |
| *Saccharomyces cerevisiae* | YBL036C | SGD:S000000132 |

- **Conservation.** The family is "found in living organisms from all kingdoms." (PMID 39604152), including bacterial YggS, cyanobacterial PipY (PMID 28914444) and two plant homologs (PMID 38954500). Loss of the homolog disturbs the B6 pool across species: "Accumulation of PNP is a characteristic phenotype of PLPBP deficiency" (PMID 34978460).

---

## 15. Model Organisms

| Model | Type | Recapitulation | Reference |
|---|---|---|---|
| Zebrafish *plpbp* ot101/ot102 (ZFIN:ZDB-FISH-220728-15) | CRISPR/Cas9 exon 1 frameshift alleles, compound heterozygous, no protein | Strong. Seizures "by 10 days post-fertilization" "and early death by 16 days post-fertilization."; low PLP and pyridoxal; altered GABA, catecholamines and amino acids. "Treatment with pyridoxine significantly improved the epileptic phenotype and extended lifespan" | PMID 30668673 |
| Mouse Plpbp em1(IMPC)Bay, C57BL/6N | CRISPR knockout, homozygous | Preweaning lethality with incomplete penetrance (MP:0011110). No significant nervous-system or behavioural call in the standard pipeline; no seizure characterisation published | IMPC (https://www.mousephenotype.org), Baylor centre |
| HEK293 PLPHP knockout | Human cell line | Low PLP, high PNP and PMP, lactate accumulation, reduced TCA intermediates | PMIDs 30668673, 37451483 |
| Patient skin fibroblasts | Primary cells | B6 vitamer imbalance; raised lactate-to-pyruvate ratio; reduced spare respiratory capacity | PMIDs 27912044, 30668673, 37451483 |
| Yeast ybl036cΔ | Knockout | Normal growth on glucose, impaired on respiratory carbon sources, partly rescued by human PLPHP; PLP depletion "only with carbon sources requiring mitochondrial metabolism" | PMIDs 30668673, 37451483 |
| *E. coli* ΔyggS | Knockout | Pyridoxine sensitivity; complementation assay for human variants ("complementation with human PROSC restored growth") | PMIDs 27912044, 34978460 |
| *Salmonella*, cyanobacteria (PipY), *Arabidopsis* | Knockouts | Conserved B6 and amino acid homeostasis defects | PMIDs 42045118, 28914444, 38954500 |

**Limitations.**
- Zebrafish die as larvae, so they do not model long-term cognition; PLP was less effective than pyridoxine in fish **[tool summary – verify]**.
- The mouse knockout has not been characterised neurologically.
- Cell models give conflicting PLP directions between studies (PMID 27912044 versus PMIDs 30668673 and 37451483).
- No iPSC-derived neuronal or organoid model was retrieved.

**Applications.** Variant pathogenicity testing by complementation (bacteria, yeast), B6 vitamer flux studies, and treatment testing in zebrafish.

**Resources.** ZFIN (ZDB-PUB-190123-4), IMPC/MGI (MGI:1891207), SGD (YBL036C), Alliance of Genome Resources.

---

## Key References

| PMID | Citation | Evidence type |
|---|---|---|
| 27912044 | Darin N et al. Am J Hum Genet 2016. Mutations in PROSC disrupt cellular pyridoxal phosphate homeostasis and cause vitamin-B6-dependent epilepsy | Human clinical; in vitro; bacterial |
| 28391250 | Plecko B et al. J Med Genet 2017. Confirmation of mutations in PROSC as a novel cause of vitamin B6-dependent epilepsy | Human clinical |
| 29689137 | Tremiño L et al. Hum Mutat 2018. Insight into vitamin B6-dependent epilepsy due to PLPBP missense mutations | In vitro protein |
| 30525118 | Shiraku H et al. Epilepsia Open 2018. PLPBP mutations cause variable phenotypes of developmental and epileptic encephalopathy | Human clinical |
| 30668673 | Johnstone DL et al. Brain 2019. PLPHP deficiency: clinical, genetic, biochemical, and mechanistic insights (https://pmc.ncbi.nlm.nih.gov/articles/PMC6391652/) | Human clinical; zebrafish; yeast; cells |
| 31741821 | Jensen KV et al. JIMD Rep 2019. Diagnostic pitfalls in vitamin B6-dependent epilepsy caused by mutations in the PLPBP gene | Human clinical |
| 31825581 | Fux A et al. ACS Chem Biol 2020. Biochemical and proteomic studies of human PLPBP | In vitro; proteomics |
| 32980745 | Akiyama T et al. Pediatr Neurol 2020. CSF pyridoxal as an indicator of vitamin B6-dependent epilepsy | Human biomarker |
| 33728241 | Heath O et al. JIMD Rep 2021. Premature infant with pathogenic PLPBP variants; literature review | Human clinical |
| 33977028 | Pal M et al. JIMD Rep 2021. Founder mutation in PLPBP in Saguenay–Lac-St-Jean families | Human clinical; haplotype |
| 36324377 | Alsubhi S et al. Front Neurol 2022. Three novel individuals and review of 51 cases (https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2022.913652/full) | Human clinical; review |
| 36795901 | Al-Shekaili H et al. GeneReviews 2023. PLPBP Deficiency (NBK589231) | Curated review |
| 36980111 | Mastrangelo M et al. Children 2023. Epilepsy phenotypes of vitamin B6-dependent diseases: systematic review | Systematic review |
| 37451483 | Ciapaite J et al. J Biol Chem 2023. Maintenance of cellular vitamin B6 levels and mitochondrial oxidative function depend on PLPHP | Cells; yeast |
| 39604152 | Graziani C et al. Protein Sci 2024. PLP-binding protein is also an RNA-binding protein | In vitro |
| 40976369 | Nakamura S et al. Eur J Med Genet 2025. Late-onset vitamin B6-dependent epilepsy with compound heterozygous PLPBP variants | Human clinical |
| 42563912 | Takle M et al. Ann Child Neurol Soc 2025. PLPBP deficiency mimicking opsoclonus-myoclonus-ataxia syndrome | Human clinical |
| 41671913 | Alsini H et al. Mol Genet Metab 2026. Multicentre case series and systematic review of PLPBP deficiency | Human clinical; systematic review |
| 42516410 | Kravljanac R et al. Front Neurol 2026. Pyridoxine-dependent and other pyridoxine-responsive epilepsies | Human clinical |

**Gaps to fill before curation.**
- GeneReviews dosing, surveillance and frequency tables.
- Orphanet, ICD and MeSH codes.
- Ontology IDs for the GO, CL, UBERON, CHEBI, NCIT and remaining HPO labels.
- Full-text verification of the items marked **[tool summary – verify]**.
- The complete ClinVar variant list with classifications.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 54 |
| Quoted claims found in source | 54 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 28 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:10496079` (1 mention) - Cloning and characterization of human and mouse PROSC (proline synthetase co-transcribed) genes.
  - shared terms: gene, protein

Weighed against this report's own most characteristic terms: `plpbp`, `patient`, `variant`, `plp`, `disease`, `seizure`, `deficiency`, `epilepsy`, `pyridoxine`, `pyridoxal`, `plphp`, `treatment`, `cause`, `phenotype`, `vitamin`, `cell`, `gene`, `protein`, `prenatal`, `developmental`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 25 |
| Terms whose name was checked | 4 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010851` (1 mention) - the report calls it "EEG burst suppression"; HP calls it **EEG with burst suppression**

### Terms the ontology service could not be reached for

23 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0009945` (1 mention)
- `MONDO:0957599` (1 mention)
- `HP:0032794` (1 mention)
- `HP:0001270` (1 mention)
- `HP:0001252` (1 mention)
- `HP:0001276` (1 mention)
- `HP:0000737` (1 mention)
- `HP:0002093` (1 mention)
- `HP:0002104` (1 mention)
- `HP:0002151` (1 mention)
- `HP:0001942` (1 mention)
- `HP:0012444` (1 mention)
- `HP:0002119` (1 mention)
- `HP:0000219` (1 mention)
- `HP:0000343` (1 mention)
- `HP:0000582` (1 mention)
- `HP:0000629` (1 mention)
- `HP:0020045` (1 mention)
- `HP:0000007` (1 mention)
- `MGI:1891207` (2 mentions)
- `RGD:1308962` (1 mention)
- `SGD:S000000132` (1 mention)
- `MP:0011110` (1 mention)

### Terms whose obsolescence could not be checked

4 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `MONDO:0015005` (4 mentions)
- `DOID:0080769` (1 mention)
- `HP:0032792` (1 mention)
- `HP:0002069` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

13 of 38 terms resolved to a current term; the rest could not be looked up either way.