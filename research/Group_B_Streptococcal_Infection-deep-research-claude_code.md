---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-26T15:46:16.561016'
end_time: '2026-11-26T15:51:37.169769'
duration_seconds: 320.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Group B Streptococcal Infection
  mondo_id: MONDO:0700218
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Group B streptococcal disease; Streptococcus agalactiae infection
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 16
  num_turns: 25
  total_cost_usd: 1.7035741
  session_id: 7dd6a614-1823-4b76-bcfd-3f404dcc5bee
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  tool_calls: 23
  retrieval_calls: 17
  assistant_text_blocks: 4
citation_count: 28
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 25
  validator_version: 0.8.0
term_validation:
  total_terms: 25
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0000996
    reported_labels:
    - Maternal/reproductive:** vagina
    ontology_label: vagina
  labels_variant: 3
  service_unreachable: 3
  obsolescence_unchecked: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Group B Streptococcal Infection
- **MONDO ID:** MONDO:0700218 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Group B streptococcal disease; Streptococcus agalactiae infection
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Group B Streptococcal Infection** covering all of the
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

I'm looking up Group B strep sources in PubMed. My first script was blocked, so I'm querying the database directly.

I have strong sourcing already. Let me gather a few remaining pieces (vaccine, adult disease, treatment/penicillin, animal models) and then write the report.

I have strong coverage. Two final searches for the mechanism and model-organism sections, then I'll write the report.

**Interpretation note:** This report covers **Group B Streptococcal (GBS) infection** (MONDO:0700218), i.e., invasive and mucosal disease caused by the Gram-positive bacterium ***Streptococcus agalactiae***. This is an **infectious disease, not a Mendelian genetic disorder** — the template field "Causal gene(s): not recorded" is correct because the disease has no human causal gene. The relevant "genetics" are therefore (a) the *pathogen's* virulence genes and (b) *host susceptibility/response* factors. I have mapped the template's gene-centric sections onto those two axes where applicable and marked sections "Not applicable" where the template assumes a monogenic human disease. Every specific claim below was retrieved via web search in this session; where I could not retrieve adequate support, I say so in that section rather than filling from memory. Some identifiers (ICD codes, several PMIDs) are widely used but were **not** independently verified against their primary registry this session — these are explicitly flagged.

---

## 1. Disease Information

**Overview.** Group B Streptococcal infection is disease caused by *Streptococcus agalactiae* (Lancefield group B *Streptococcus*, GBS), a beta-hemolytic, encapsulated, Gram-positive coccus that colonizes the human gastrointestinal and genitourinary tracts as a commensal and can become an invasive pathogen. It is **the leading cause of neonatal sepsis and meningitis** and an increasingly important cause of invasive disease in non-pregnant adults; it also causes maternal infection, stillbirth, and preterm birth ([Seale 2017, *Clin Infect Dis*](https://pubmed.ncbi.nlm.nih.gov/29117326/); [Gonçalves 2022, *Lancet Glob Health*](https://pesquisa.bvsalud.org/bvsvs/resource/pt/mdl-35490693)). *S. agalactiae* is also a major pathogen of cattle (mastitis) and farmed fish.

**Clinical syndromes** are conventionally divided into:
- **Early-onset disease (EOD):** day 0–6 of life, acquired vertically around birth; presents as respiratory distress progressing to septicemia/pneumonia, less often meningitis.
- **Late-onset disease (LOD):** day 7–89; presents as sepsis, more often progressing to meningitis ([Frontiers in Microbiology 2022 review, PMC-hosted](https://www.frontiersin.org/articles/10.3389/fmicb.2022.820365/full); ["Neonatal Group B Streptococcus Disease," PMID 38296778](https://pubmed.ncbi.nlm.nih.gov/38296778/)).
- **Maternal/pregnancy-associated disease:** colonization, chorioamnionitis, bacteremia, UTI, endometritis, and associated stillbirth/preterm birth.
- **Adult non-pregnancy-associated invasive disease:** bacteremia, skin/soft-tissue infection, osteomyelitis/septic arthritis, pneumonia, endocarditis — predominantly in older adults and those with diabetes/obesity ([Francois Watkins 2019, *JAMA Intern Med*, PMC6450309](https://pmc.ncbi.nlm.nih.gov/articles/PMC6450309)).

**Key identifiers:**
- **MONDO:** MONDO:0700218 (as supplied in the template; not independently re-verified this session).
- **ICD-10 / ICD-11:** No single dedicated GBS "disease" code. GBS is commonly captured with **B95.1** ("Streptococcus, group B, as the cause of diseases classified elsewhere") and **P36.0** ("Sepsis of newborn due to streptococcus, group B"). *Not verified against the ICD browser this session — treat as provisional.*
- **MeSH:** "Streptococcus agalactiae" (organism) and "Streptococcal Infections" (disease). *MeSH tree numbers not retrieved this session.*
- **OMIM / Orphanet:** Not applicable as a disease entry (OMIM catalogs Mendelian human genes/phenotypes; GBS is infectious). Not retrieved.

**Synonyms:** Group B streptococcal disease; *Streptococcus agalactiae* infection; GBS infection; group B strep.

**Data source type:** The quantitative content below is drawn from **aggregated disease-level resources** — population-based surveillance (CDC Active Bacterial Core surveillance/ABCs), systematic reviews/meta-analyses, and modeled global burden estimates — not from individual EHR-level patient records.

---

## 2. Etiology

**Primary cause (infectious).** The sole necessary cause is infection with *Streptococcus agalactiae*. NCBI Taxonomy ID for the organism is **txid1311** (*S. agalactiae*); *not re-verified against NCBI Taxonomy this session.* Disease arises when the commensal organism breaches mucosal barriers — vertically (ascending from maternal vaginal colonization, or during passage through the birth canal) in neonates, or via mucosal/skin translocation in adults.

**Risk factors — host/environmental:**
- **Maternal GBS colonization** is the principal upstream risk factor for EOD; worldwide maternal rectovaginal colonization is ~**18%** (95% CI 17–19%), with regional range 11–35% ([Russell 2017, *Clin Infect Dis* Suppl, PMC5848259](https://pmc.ncbi.nlm.nih.gov/articles/PMC5848259)).
- **Neonatal:** preterm birth/low birth weight, prolonged rupture of membranes, intrapartum fever/chorioamnionitis, heavy maternal colonization, prior infant with GBS disease, young maternal age, Black race (higher incidence in US surveillance).
- **Adult:** **diabetes mellitus** and **obesity** are the dominant comorbidities — among US non-pregnant adult cases, obesity (53.9%) and diabetes (53.4%) were most common; a VA cohort found ~4-fold higher incidence with poor glycemic control vs good control ([Francois Watkins 2019, *JAMA Intern Med*](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2724392)). Advanced age, cirrhosis, malignancy, and immunosuppression also raise risk.

**Genetic (host) susceptibility factors.** Host genetic susceptibility to GBS is biologically plausible (e.g., maternal antibody levels, innate-immune receptor variation) but I did **not** retrieve primary GWAS/ClinVar evidence for specific human susceptibility loci this session. **This subsection is unverified/not available** and should not be populated from memory.

**Pathogen genetic factors** (the operative "genetics" here): serotype (capsular polysaccharide type), clonal complex/sequence type (notably **hypervirulent CC17/ST-17**), and specific virulence genes (see Section 4).

**Protective factors:**
- **Maternal type-specific anti-capsular IgG** transferred transplacentally protects the newborn — the biological basis of maternal vaccination ([Madhi 2023, *NEJM* GBS6 trial, PMID 37467497](https://www.pubmed.gov/37467497/)).
- **Intrapartum antibiotic prophylaxis (IAP)** and universal antenatal screening are the proven preventive interventions for EOD (see Sections 12–13) ([CDC 2010 MMWR guidelines](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5910a1.htm)).
- No validated human *genetic* protective variant was retrieved.

**Gene–environment interactions.** A notable host-flora interaction: in a murine model, GBS alone did not establish vaginal colonization/ascending infection, but **co-inoculation with *Gardnerella vaginalis*** was required — implicating the vaginal microbiome as a modifier of GBS pathogenesis ([PMC8555936](https://pmc.ncbi.nlm.nih.gov/articles/PMC8555936)). Human GxE data not retrieved.

---

## 3. Phenotypes

Phenotypes are clinical manifestations of infection (not heritable traits). Frequencies below are from a neonatal case series and reviews.

**Neonatal GBS disease — syndrome distribution** (one series): septicemia 62%, meningitis 22%, bacteremic pneumonia 5%, focal infection <1%; meningitis more common in LOD (29%) than EOD (11%) ([Frontiers Microbiol 2022 review](https://www.frontiersin.org/articles/10.3389/fmicb.2022.820365/full)).

| Phenotype | Type | Onset | Severity/course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Neonatal sepsis / bacteremia | clinical sign / lab | neonatal (EOD d0–6; LOD d7–89) | severe, acute | most common syndrome (~62%) | HP:0100806 (Sepsis), HP:0031864? (neonatal sepsis — verify) |
| Respiratory distress / pneumonia | symptom/sign | EOD, hours after birth | severe, acute | predominant EOD presentation | HP:0002094 (Dyspnea), HP:0002090 (Pneumonia) |
| Meningitis | clinical sign | LOD > EOD | severe; risk of permanent sequelae | ~22% overall; 29% LOD | HP:0001287 (Meningitis) |
| Fever | symptom | neonatal/adult | variable | common | HP:0001945 (Fever) |
| Osteomyelitis / septic arthritis | clinical sign | LOD; adults | subacute | less common | HP:0002754 (Osteomyelitis), HP:0000768? (verify) |
| Neurodevelopmental impairment (sequela of meningitis) | behavioral/developmental | post-infection, childhood | moderate–severe, often permanent | ~37,100 of iGBS survivors developed moderate/severe NDI (2020 model) | HP:0012758 (Neurodevelopmental delay) |
| Stillbirth / preterm birth (maternal/fetal) | outcome | antenatal/perinatal | fatal/severe | 46,200 GBS stillbirths (2020 model) | — |

*HPO IDs above are suggested mappings; several (neonatal sepsis, septic arthritis) should be verified in the HPO browser before ingestion.*

**Quality-of-life impact.** Survivors of GBS meningitis carry substantial long-term burden through neurodevelopmental impairment (cerebral palsy, hearing/vision loss, cognitive and motor deficits). The 2020 global model estimated **~37,100 children recovering from invasive GBS went on to develop moderate or severe NDI** (range 14,600–96,200) ([Gonçalves 2022, *Lancet Glob Health*](https://pesquisa.bvsalud.org/bvsvs/resource/pt/mdl-35490693)). Formal EQ-5D/SF-36/PROMIS instrument data specific to GBS were **not retrieved** this session.

---

## 4. Genetic / Molecular Information

**Human causal genes: Not applicable** (infectious disease; no human causal gene — consistent with template "not recorded").

**Pathogen genetic/molecular determinants (the operative content):**

- **Capsular polysaccharide (CPS) serotypes.** Ten serotypes (Ia, Ib, II–IX); **serotypes I–V account for ~98%** of colonizing isolates, and **serotype III accounts for ~25%** of colonizing isolates and is disproportionately associated with invasive disease ([Russell 2017, PMC5848259](https://pmc.ncbi.nlm.nih.gov/articles/PMC5848259)). In US late-onset disease, **serotype III was most common (56.2%)** and rising ([Nanduri 2019, *JAMA Pediatr*, PMID 30640366](https://pmc.ncbi.nlm.nih.gov/articles/PMC6439883)). Six serotypes caused 99.3% of EOD and 99.7% of LOD (ibid.). The CPS is synthesized by the *cps* gene cluster.

- **Hypervirulent clone CC17/ST-17** carries the surface adhesin **HvgA** (hypervirulent GBS adhesin), present **only in ST-17**; ST-17 accounted for **>80% of neonatal meningitis** isolates in a French collection. HvgA mediates binding to intestinal, choroid plexus, and blood–brain-barrier endothelial cells and is required for gut colonization and meningeal crossing in neonatal mice ([Tazi 2010, *J Exp Med*, PMID 20956545](https://pmc.ncbi.nlm.nih.gov/articles/PMC2964583)).

- **β-hemolysin/cytolysin = granadaene pigment.** The hemolytic/cytolytic activity is due to the **ornithine-rhamnolipid pigment granadaene**, produced by the ***cyl* operon (cylX–K)**, not a protein pore-forming toxin; it enables penetration of human placenta ([Whidbey 2013, *J Exp Med*, PMID 23712433](https://pmc.ncbi.nlm.nih.gov/articles/PMC3674703)).

- **Sialylated capsule / molecular mimicry.** The CPS terminal **Siaα2-3Galβ1-4GlcNAc** mimics host sialoglycans and engages neutrophil **Siglec-9** to dampen oxidative burst, protease release, and NET formation ([Carlin 2009, *Blood*, PMC2665898](https://pmc.ncbi.nlm.nih.gov/articles/PMC2665898)).

- **Other virulence genes retrieved:** **β protein** engages Siglec-5 (Sia-independent) ([related 2009 *J Exp Med*, PMC2722167](https://pmc.ncbi.nlm.nih.gov/articles/PMC2722167)); **hyaluronidase** promotes ascending infection/preterm birth; **npx** is required for invading reproductive tissue and driving PPROM/preterm birth in mice ([PMID 36409087, PMC9765263](https://pmc.ncbi.nlm.nih.gov/articles/PMC9765263/)).

- **Antimicrobial-resistance determinants (pathogen):** reduced β-lactam susceptibility is associated with **PBP2x point mutations** (e.g., V405A, Q557E), with additional PBP2b/PBP1a substitutions at higher MICs ([US surveillance 1998–2018, PMID 33553474](https://pubmed.ncbi.nlm.nih.gov/33553474/)). Macrolide/lincosamide resistance is conferred by ***erm*** (MLS_B phenotype, constitutive or inducible) and ***mef*** (M phenotype, macrolide-only) ([four-state ABCs surveillance; West Virginia 2025 genomic study, PMC12698558](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12698558/)).

**Human epigenetics / chromosomal abnormalities:** Not applicable / not retrieved.

---

## 5. Environmental Information

- **Infectious agent (CHEBI/organism):** *Streptococcus agalactiae*, NCBI Taxon txid1311 (provisional, not re-verified). It is the obligatory etiologic agent.
- **Environmental/behavioral factors:** Maternal colonization status is the key perinatal "exposure." Adult disease is driven by host metabolic comorbidity (diabetes, obesity) rather than toxins/occupational exposures ([Francois Watkins 2019](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2724392)). No toxin/radiation/pollution associations retrieved (not expected for this disease).
- **Vaginal microbiome:** *Gardnerella vaginalis* co-colonization facilitated GBS vaginal colonization and ascension in a mouse model ([PMC8555936](https://pmc.ncbi.nlm.nih.gov/articles/PMC8555936)).

---

## 6. Mechanism / Pathophysiology

### Causal chain (neonatal early-onset disease)

1. Maternal rectovaginal **colonization** by *S. agalactiae* (commensal state; ~18% of pregnant women) → **leads to** a reservoir for vertical transmission ([Russell 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5848259)).
2. **Ascending infection** and/or intrapartum exposure: GBS ascends the genital tract (facilitated by **hyaluronidase** and the **granadaene/β-H/C** toxin; *npx* required for tissue invasion) → **results in** invasion of amniotic/placental tissue and fetal exposure ([Whidbey 2013, PMID 23712433](https://pmc.ncbi.nlm.nih.gov/articles/PMC3674703); [Randis ascending model, PMID 24474814](https://pmc.ncbi.nlm.nih.gov/articles/PMC4092248); [npx PMID 36409087](https://pmc.ncbi.nlm.nih.gov/articles/PMC9765263/)).
3. **Granadaene-mediated cytolysis** of placental and epithelial barriers → **allows** bacterial penetration of the human placenta and fetal membranes (branch point: can cause PPROM, preterm birth, stillbirth) ([Whidbey 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3674703)).
4. Neonatal **mucosal colonization** (aspiration of infected vaginal secretions seeds respiratory/GI mucosa) → **leads to** mucosal translocation into the bloodstream ([Frontiers 2022 review](https://www.frontiersin.org/articles/10.3389/fmicb.2022.820365/full)).
5. **Immune evasion in blood:** sialylated capsule engages **Siglec-9/-5**, blunting neutrophil oxidative burst, degranulation, and NETs → **permits** bacterial survival and **bacteremia/sepsis** ([Carlin 2009, PMC2665898](https://pmc.ncbi.nlm.nih.gov/articles/PMC2665898)).
6. **Branch — meningeal tropism (esp. CC17/ST-17):** **HvgA** mediates adhesion to blood–brain-barrier endothelium and choroid plexus → **enables** BBB crossing and **meningitis** ([Tazi 2010, PMID 20956545](https://pmc.ncbi.nlm.nih.gov/articles/PMC2964583)).
7. Meningeal/systemic inflammation and tissue injury → **results in** neuronal injury → **neurodevelopmental impairment** in survivors (inferred causal link from epidemiologic association; mechanistic detail of neuronal injury not fully retrieved) ([Gonçalves 2022](https://pesquisa.bvsalud.org/bvsvs/resource/pt/mdl-35490693)).

### Checklist coverage
- **Molecular pathways / protein dysfunction:** granadaene (ornithine-rhamnolipid, *cyl* operon) causes membrane lysis; HvgA (surface adhesin) mediates cell adhesion; CPS sialic acid engages host Siglec lectin receptors. *Specific KEGG/Reactome pathway IDs not retrieved.*
- **Cellular processes:** cytolysis, neutrophil suppression (reduced ROS burst, impaired NETosis), epithelial/endothelial barrier breach, inflammation.
- **Immune involvement:** innate immune evasion via molecular mimicry (Siglec-9/-5); host protection via type-specific anti-CPS IgG.
- **Tissue damage mechanisms:** direct cytolysis (granadaene), BBB disruption, inflammatory injury.

**Upstream vs downstream:** colonization → ascension/invasion (upstream) → immune evasion/bacteremia → organ seeding (meninges, lung) → inflammation/sequelae (downstream).

**Suggested ontology terms:** GO:0019836 (hemolysis in another organism), GO:0044179 (hemolysis in other organism — verify), GO:0052572 (response to host immune response — verify); **CL:** CL:0000775 (neutrophil), CL:0000115 (endothelial cell), CL:0002319 (neural cell); **UBERON:** see Section 7. *All suggested terms require verification in their browsers.*

---

## 7. Anatomical Structures Affected

- **Primary organs/systems (neonatal):** bloodstream (bacteremia/sepsis), **lungs** (pneumonia — UBERON:0002048), **meninges/CNS** (meningitis — UBERON:0002360 meninges; UBERON:0000955 brain). 
- **Maternal/reproductive:** vagina (UBERON:0000996), placenta (UBERON:0001987), fetal membranes/amnion, uterus/endometrium.
- **Adult:** bloodstream, skin and soft tissue, **bone/joint** (osteomyelitis/septic arthritis — UBERON:0001474 bone; UBERON:0000955 joint — verify), lung, heart (endocarditis — UBERON:0002165 endocardium — verify).
- **Tissue/cell level:** vaginal/placental **epithelium**, **vascular endothelium** (incl. BBB microvascular endothelium — CL:0002139/CL:0000115), choroid plexus epithelium, **neutrophils** (CL:0000775) as the key suppressed effector cell.
- **Subcellular:** host cell **plasma membrane** (granadaene target — GO:0005886); bacterial **cell surface/capsule**.
- **Localization/lateralization:** meningitis and sepsis are systemic/not lateralized; pneumonia may be bi- or unilateral (not specifically retrieved).

*UBERON/CL/GO IDs are suggested and require verification.*

---

## 8. Temporal Development

- **Onset / age windows:**
  - **EOD:** 0–6 days of life (acute, often within hours of birth) ([Nanduri 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6439883)).
  - **LOD:** 7–89 days.
  - "Very-late-onset": >90 days (mainly in preterm/immunocompromised infants — not quantified here).
  - **Adults:** median older age; rising with comorbidity ([Francois Watkins 2019](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2724392)).
- **Onset pattern:** acute to fulminant (sepsis); meningitis subacute-to-acute.
- **Course / duration:** acute infection; self-limited with prompt antibiotics in most, but meningitis can leave **chronic, lifelong neurodevelopmental sequelae**. Fatal in a proportion (see Section 11).
- **Critical period for intervention:** **intrapartum** (IAP during labor) is the key window for EOD prevention ([CDC 2010](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5910a1.htm)). IAP does **not** prevent LOD, which has remained stable despite EOD decline ([Nanduri 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6439883)).

---

## 9. Inheritance and Population

**Inheritance:** Not applicable (infectious; no Mendelian inheritance, penetrance, anticipation, founder effects, or carrier frequency in the human-genetic sense). "Carriage" here refers to *bacterial colonization* (~18% of pregnant women), not genetic carrier status.

**Epidemiology:**
- **Maternal colonization:** ~18% worldwide (95% CI 17–19%; regional 11–35%) ([Russell 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5848259)).
- **Global burden (2015 model):** ≥409,000 maternal/fetal/infant cases and 147,000 stillbirths + infant deaths annually; Africa bore 54% of cases and 65% of fetal/infant deaths ([Seale 2017, *Clin Infect Dis*](https://openaccess.sgul.ac.uk/109347/1/cix664.pdf)).
- **Global burden (2020 model):** ~19.7 million pregnant women colonized; 231,800 early-onset and 162,200 late-onset infant invasive cases; 46,200 GBS-attributed stillbirths; 40,500 maternal invasive cases; ~37,100 survivors with moderate/severe NDI ([Gonçalves 2022, *Lancet Glob Health*](https://pesquisa.bvsalud.org/bvsvs/resource/pt/mdl-35490693)).
- **US infant incidence (ABCs, 2006–2015):** EOD declined from **0.37 → 0.23 per 1,000 live births** (P<.001); LOD stable (mean **0.31 per 1,000**); in 2015, ~840 EOD and ~1,265 LOD cases nationally; LOD now exceeds EOD ([Nanduri 2019, PMID 30640366](https://pmc.ncbi.nlm.nih.gov/articles/PMC6439883)).
- **US non-pregnant adults (2008–2016):** incidence rose from **8.1 → 10.9 per 100,000** ([Francois Watkins 2019](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2724392)).
- **Demographics:** higher incidence historically in Black infants (US); regionally highest burden in Africa. Adult disease skews older with diabetes/obesity.

---

## 10. Diagnostics

- **Microbiology (gold standard):** culture of *S. agalactiae* from a normally sterile site (blood, CSF) for invasive disease; **CSF analysis** for meningitis. For maternal screening, **culture of combined vaginal-rectal swab at 36 0/7–37 6/7 weeks** (updated from 35–37 weeks in CDC 2010) ([CDC 2010 MMWR](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5910a1.htm)).
- **Rapid molecular:** intrapartum **NAAT/PCR** for GBS (used when colonization status unknown at labor) — *specific assay performance not retrieved this session.*
- **Serotyping / genotyping:** CPS serotyping and MLST (e.g., ST-17 identification) for epidemiology; **HvgA detection** proposed as a marker for the hypervirulent clone ([Tazi 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2964583)).
- **Susceptibility testing:** penicillin remains predictably active, but routine disk diffusion may miss **low-level reduced β-lactam susceptibility** (PBP2x mutants); erythromycin/clindamycin testing (including **D-test for inducible clindamycin resistance**) is needed for penicillin-allergic patients ([PMID 33553474](https://pubmed.ncbi.nlm.nih.gov/33553474/); macrolide-resistance surveillance above).
- **Omics/liquid biopsy / imaging / EEG etc.:** Not disease-defining; **not retrieved** and generally not applicable to routine GBS diagnosis.
- **Human genetic testing:** Not applicable.
- **Differential diagnosis:** other neonatal sepsis pathogens (*E. coli*, *Listeria monocytogenes*), other causes of neonatal respiratory distress and meningitis; in adults, other streptococcal/staphylococcal invasive infections. *Distinguishing-feature detail not specifically retrieved.*

---

## 11. Outcome / Prognosis

- **Neonatal case fatality:** GBS remains a leading cause of neonatal sepsis/meningitis mortality; specific CFR figures were **not precisely retrieved** this session (the 2015/2020 global models report large absolute death counts — 147,000 stillbirths+infant deaths in 2015 — rather than per-case CFR) ([Seale 2017](https://openaccess.sgul.ac.uk/109347/1/cix664.pdf)).
- **Morbidity / long-term sequelae:** Meningitis survivors are at high risk of **moderate-to-severe neurodevelopmental impairment** (cerebral palsy, hearing/vision loss, cognitive/motor deficits); ~37,100 survivors developed moderate/severe NDI in the 2020 model ([Gonçalves 2022](https://pesquisa.bvsalud.org/bvsvs/resource/pt/mdl-35490693)).
- **Prognostic factors:** prematurity, meningitis (vs bacteremia-only), delay to effective antibiotics, serotype III/CC17 (meningitis tropism), and in adults, severity of underlying diabetes/comorbidity.
- **Adult outcomes:** higher morbidity/mortality with age and comorbidity; quantitative CFR not retrieved.
- Formal **QoL instrument data (EQ-5D/SF-36/PROMIS)** specific to GBS: **not available** from this session's retrieval.

---

## 12. Treatment

**Antimicrobial therapy (NCIT suggestions in brackets):**
- **Penicillin G** is the drug of choice; **ampicillin** is an acceptable alternative — for both treatment and intrapartum prophylaxis ([CDC 2010 MMWR](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5910a1.htm); [AAFP summary](https://www.aafp.org/pubs/afp/issues/2011/0501/p1106.html)). *(NCIT: Penicillin G; Ampicillin.)*
- **Meningitis:** typically ampicillin/penicillin, often combined with an aminoglycoside empirically pending cultures (combination synergy) — *specific regimen detail not fully retrieved.*
- **Penicillin-allergic patients (prophylaxis):** **cefazolin** if not at high risk of anaphylaxis; for high-risk allergy, **clindamycin only if susceptibility (incl. D-test) confirmed**, otherwise **vancomycin**. **Erythromycin is no longer acceptable** ([CDC 2010](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5910a1.htm)). *(NCIT: Cefazolin; Clindamycin; Vancomycin.)*
- **Resistance considerations:** penicillin resistance is not established clinically, but **reduced β-lactam susceptibility (PBP2x mutants)** is emerging and may be missed on routine testing ([PMID 33553474](https://pubmed.ncbi.nlm.nih.gov/33553474/)); macrolide/clindamycin resistance (*erm*/*mef*) is substantial and rising (erythromycin rose 15.8%→32.8%, clindamycin 10.5%→15.0% in one surveillance period) ([four-state surveillance; West Virginia 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12698558/)).

**Supportive care:** neonatal/adult sepsis and meningitis management — respiratory support, hemodynamic support, fluids; neurorehabilitation for survivors with sequelae. *(General; specific GBS protocols not separately retrieved.)*

**Advanced/experimental therapeutics:** No gene/cell/RNA therapy applies. The principal investigational product is a **maternal vaccine** (see Section 13), not a therapeutic.

**Pharmacogenomics / targeted / immunotherapy / surgery:** Not applicable beyond source control (e.g., drainage of septic joint/abscess) — surgical detail not retrieved.

---

## 13. Prevention

- **Primary prevention (current standard):** **universal antenatal GBS screening** (vaginal-rectal culture at 36 0/7–37 6/7 weeks) + **intrapartum antibiotic prophylaxis (IAP)** with penicillin G (ampicillin alternative) for colonized women and those with risk factors. This strategy has driven the marked EOD decline but does **not** prevent LOD ([CDC 2010 MMWR RR-59(10)](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5910a1.htm); [Nanduri 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6439883)). *(Note: ACOG later assumed stewardship of the US guideline; the ACOG 2020 document was not retrieved this session.)*
- **Immunization (investigational):** **GBS6**, a hexavalent (serotypes Ia, Ib, II, III, IV, V) CPS–conjugate **maternal vaccine**, elicited anti-CPS IgG in pregnant women that transferred to infants at levels associated with reduced invasive-disease risk, with no vaccine-associated safety signal (phase 2) ([Madhi 2023, *NEJM* 389:215–227, PMID 37467497](https://www.pubmed.gov/37467497/)). A trivalent conjugate also showed protection against colonization, ascending infection, and neonatal transmission in rodent models ([PMID 29416049, PMC5803199](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5803199/)). No licensed GBS vaccine exists as of the retrieved sources.
- **Secondary/tertiary prevention:** early recognition and treatment of neonatal/adult infection; management of comorbidity (glycemic control) to reduce adult risk ([Francois Watkins 2019](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2724392)).
- **Genetic counseling / carrier screening / public-health sanitation measures:** Not applicable in the usual senses (this is not a heritable or environmentally transmitted disease).

---

## 14. Other Species / Natural Disease

*S. agalactiae* is a genuine multi-host pathogen ([2024 host-adaptation study, PMID 39133742](https://pmc.ncbi.nlm.nih.gov/articles/pmid/39133742)):

- **Cattle (bovine mastitis):** *S. agalactiae* is a classic agent of contagious bovine mastitis; clonal complex **CC67** is essentially bovine-associated. Genomic adaptation includes acquisition of **lactose-metabolism** capacity and **lateral gene transfer** from other mastitis streptococci (*S. uberis*, *S. dysgalactiae*) ([BMC Genomics 2013, 14:252](https://link.springer.com/content/pdf/10.1186/1471-2164-14-252.pdf); [transcriptomic/genomic bovine adaptation, PMC3890567](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3890567/)).
- **Fish (farmed tilapia):** causes streptococcosis/meningoencephalitis in tilapia; Chinese tilapia isolates are genomically close to the human strain A909 but carry a distinct ~10-kb genomic island; serotype Ib fish strains show **reductive evolution** (10–25% genome loss) ([PMID 24215651](https://pmc.ncbi.nlm.nih.gov/articles/PMC3831827); host-adaptation review above).
- **Humans:** the hypervirulent **ST-17** clone is mainly human-associated ([2024 host-adaptation study](https://pmc.ncbi.nlm.nih.gov/articles/pmid/39133742)).

**Taxonomy:** *Streptococcus agalactiae* (NCBI txid1311, provisional). **Zoonotic potential:** cross-species transmission and shared lineages exist (notably fish-to-human foodborne invasive disease has been described in the literature); specific zoonosis quantification **not retrieved** this session. **Orthologous host genes / VBO breed IDs / OMIA entries:** not retrieved.

---

## 15. Model Organisms

Primary models are **murine**, reproducing distinct stages:

- **Ascending vaginal infection in pregnant mice:** models colonization → ascension → fetal infection; used to show roles of **β-hemolysin/cytolysin (granadaene)**, **hyaluronidase**, and **npx** in PPROM/preterm birth/fetal demise ([Randis, PMID 24474814](https://pmc.ncbi.nlm.nih.gov/articles/PMC4092248); [npx, PMID 36409087](https://pmc.ncbi.nlm.nih.gov/articles/PMC9765263/); hyaluronidase, [PMC4937215](https://pmc.ncbi.nlm.nih.gov/articles/PMC4937215)).
- **Neonatal transmission/meningitis model:** pups acquire GBS from vaginally colonized dams, reproducing the **natural route** of infection and neonatal meningitis ([Nat Commun 2018, PMC6081475, doi:10.1038/s41467-018-05492-y](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6081475/)).
- **Vaccine efficacy models:** rodent colonization/ascending-infection models demonstrated maternal-vaccine protection of offspring ([PMID 29416049](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5803199/)).
- **Host–microbiome interaction model:** GBS + *Gardnerella vaginalis* co-inoculation needed for vaginal colonization/ascension ([PMC8555936](https://pmc.ncbi.nlm.nih.gov/articles/PMC8555936)).

**Model characteristics:** these systems recapitulate vertical transmission, ascending infection, preterm birth, and neonatal meningitis. **Limitations** (noted across the literature but not exhaustively retrieved): mouse–human differences in gestation, placentation, and immune/Siglec repertoire limit translation of immune-evasion findings; and GBS alone colonizes mice poorly without microbiome manipulation. **Cellular/in-vitro models** (e.g., human BBB endothelial cell adhesion assays used in the HvgA work — [Tazi 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2964583)) complement the animal models. Specific MGI/IMPC/Cellosaurus resource entries were **not retrieved** this session.

---

## Evidence summary table (key sources)

| Claim domain | Source | ID |
|---|---|---|
| Global burden 2015 | Seale et al., *Clin Infect Dis* 2017;65(S2):S200–S219 | [link](https://openaccess.sgul.ac.uk/109347/1/cix664.pdf); companion Madrid PMID 29117326 |
| Global burden 2020 | Gonçalves et al., *Lancet Glob Health* 2022;10:e807–e819 | PMID 35490693 |
| Maternal colonization 18% / serotypes | Russell et al., *Clin Infect Dis* 2017;65(S2):S100–S111 | PMC5848259 |
| US infant incidence (EOD/LOD) | Nanduri et al., *JAMA Pediatr* 2019;173(3):224–233 | PMID 30640366 / PMC6439883 |
| Granadaene/placental penetration | Whidbey et al., *J Exp Med* 2013;210(6):1265–1281 | PMID 23712433 |
| HvgA / ST-17 meningeal tropism | Tazi et al., *J Exp Med* 2010;207(11):2313–2322 | PMID 20956545 |
| Siglec-9 immune evasion | Carlin et al., *Blood* 2009;113(14):3333–3336 | PMC2665898 |
| Maternal vaccine GBS6 | Madhi et al., *NEJM* 2023;389(3):215–227 | PMID 37467497 |
| Adult non-pregnant disease | Francois Watkins et al., *JAMA Intern Med* 2019 | PMC6450309 |
| Reduced β-lactam susceptibility | US surveillance 1998–2018 | PMID 33553474 |
| Prevention guideline (IAP/screening) | CDC 2010 MMWR RR-59(10) | [link](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5910a1.htm) |
| Ascending-infection mouse model | Randis et al. | PMID 24474814 |

**Explicit gaps (not retrieved / not applicable this session):** human host-susceptibility loci (GWAS/ClinVar); precise neonatal/adult case-fatality rates; GBS-specific validated QoL instrument scores; verified ICD-10/11 and MeSH tree identifiers; OMIA/VBO/MGI resource IDs; ACOG 2020 guideline text. All ontology term IDs (HPO/GO/CL/UBERON) are **suggestions requiring browser verification** before knowledge-base ingestion.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000996` (1 mention) - the report calls it "Maternal/reproductive:** vagina"; UBERON calls it **vagina**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0700218` (2 mentions) - the report calls it "Group B Streptococcal (GBS) infection"; MONDO calls it **group B streptococcal infection**
- `GO:0044179` (1 mention) - the report calls it "hemolysis in other organism — verify"; GO calls it **hemolysis in another organism**, and lists "hemolysis in other organism" among its other names
- `GO:0052572` (1 mention) - the report calls it "response to host immune response — verify"; GO calls it **response to host immune response**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000775` - called "neutrophil", "neutrophils"

### Terms the ontology service could not be reached for

3 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0002094` (1 mention)
- `UBERON:0002048` (1 mention)
- `CL:0002139` (1 mention)

### Terms whose obsolescence could not be checked

7 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0002090` (1 mention)
- `HP:0012758` (1 mention)
- `GO:0019836` (1 mention)
- `CL:0000115` (2 mentions)
- `CL:0002319` (1 mention)
- `UBERON:0000955` (2 mentions)
- `GO:0005886` (1 mention)