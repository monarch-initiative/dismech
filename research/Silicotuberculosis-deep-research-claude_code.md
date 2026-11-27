---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-26T15:46:03.286005'
end_time: '2026-11-26T15:50:55.944155'
duration_seconds: 292.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Silicotuberculosis
  mondo_id: MONDO:0021804
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: silicotuberculoses
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
  web_search_requests: 29
  num_turns: 35
  total_cost_usd: 1.565925
  session_id: 47027cb4-59c0-41d0-a18e-a8953d4e205c
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 33
  retrieval_calls: 31
  assistant_text_blocks: 3
citation_count: 22
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 1
  quotes_unsupported: 5
  unsupported_quote_references:
  - PMC:PMC6334662
  - PMID:34016067
  - PMC:PMC8136154
  - PMC:PMC8546409
  - PMID:39694587
  relevance_assessed: 30
  on_topic: 20
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0021804
    reported_labels:
    - MONDO
    ontology_label: silicotuberculosis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Silicotuberculosis
- **MONDO ID:** MONDO:0021804 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** silicotuberculoses
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Silicotuberculosis** covering all of the
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

I'm still collecting sources; next I'll look up PMIDs, guidelines, clinical features and burden.

# Silicotuberculosis (MONDO:0021804): research report for a disease knowledge base

**How I read the request.** Silicotuberculosis is not a genetic disease. It is active tuberculosis (TB) in a person who also has silicosis, the lung scarring caused by inhaling crystalline silica dust. **There is no causal gene** ("not recorded" in the template is correct). The causes are an exposure (respirable crystalline silica) and an infection (*Mycobacterium tuberculosis*, sometimes non-tuberculous mycobacteria). The genetic sections below cover only candidate susceptibility genes.

**Limits on what I could check.** My research tools were limited to web search. I could not query PubMed, HPO, GO, Cell Ontology or UBERON directly.
- **PMIDs:** I give a PMID only where one appeared in the retrieved search results. Where none did, I say so.
- **Ontology terms:** I give term *labels* only. Their IDs were not retrieved in this session and must be checked before entry.
- **Quotes:** Text in quotation marks is abstract or summary wording as returned by the search tool. It may be slightly paraphrased, so check against PubMed before using it as an exact abstract quote.

---

## 1. Disease information

**Overview.** The most recent critical review describes silicotuberculosis as "the combination of silicosis and pulmonary tuberculosis (TB)" that "remains a substantial clinical and public health problem in high TB burden countries with silica-exposed workforces." It calls the link between silica and TB "firmly established" and says TB accelerates "impairment and mortality" in people with silicosis (Ehrlich, Murray, Said-Hartley & Rees, *Eur Respir Rev* 2024;33:240168, **PMID 39694587**, https://pubmed.ncbi.nlm.nih.gov/39694587/).
- That review proposes widening the definition to include post-tuberculous lung disease (damage left after TB is cured).
- Another review describes a spectrum. At one end are "retained silica particles in the lung and TB infection without active disease." At the other is "dual disease, referred to as silicotuberculosis" (Konečný et al., *Front Immunol* 2019;9:3069, PMC6334662, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6334662/).

**Identifiers**

| System | Identifier | Source |
|---|---|---|
| MONDO | MONDO:0021804 | given in the template |
| MeSH | **D012830** "Silicotuberculosis", introduced 1966. Tree numbers include C01.748.939.669, C08.381.922.669, C08.730.939.669 and C24.800.834.752. Scope note: TB or non-tuberculous mycobacterial infection in a person with silicosis. | https://meshb.nlm.nih.gov/record/ui?ui=D012830 |
| ICD-10 | **J65** "Pneumoconiosis associated with tuberculosis". Silicotuberculosis is an inclusion term. Use with a TB code from A15.- (A15 = respiratory TB). | https://www.aapc.com/codes/icd-10-codes/J65 ; https://gesund.bund.de/en/icd-code-suche/j65 |
| ICD-11 | Not retrieved. Check icd.who.int. | — |
| OMIM / Orphanet | None. This is not a Mendelian or rare-disease entry. | — |

**Synonyms:** silico-tuberculosis, silicotuberculoses, silicosis with tuberculosis, and (as a broader term) pneumoconiosis associated with tuberculosis.

**Type of evidence:** The information comes from aggregated, disease-level sources: occupational cohorts, case-control studies, meta-analyses and randomized trials, plus some case reports. It does not come from EHR data on individual patients.

---

## 2. Etiology

**Causes.** Two things are needed:
1. Inhaled respirable crystalline silica (CHEBI label: "silicon dioxide" / quartz) causes silicosis.
2. Infection with *M. tuberculosis* complex. Non-tuberculous mycobacteria are included by the MeSH scope note.

**Environmental and occupational risk factors**
- **Silicosis and TB risk.** A meta-analysis of 8 studies gave a pooled relative risk of TB of **4.01 (95% CI 2.88–5.58)** with silicosis. The authors had high confidence in this, with "strong exposure-response gradients" and a "low severity threshold" (Ehrlich et al., *BMC Public Health* 2021, **PMID 34016067**, PMC8136154).
- **Silica exposure without radiological silicosis.** Five studies gave a pooled RR of **1.92 (1.36–2.73)**, but the authors rated confidence as low (same source).
- **Hong Kong silicosis cohort.** TB incidence after silicosis diagnosis was about **9 times** that of the age- and sex-matched local population. Independent risk factors were:
  - no anti-TB treatment before diagnosis (RR 4.51)
  - progressive massive fibrosis (RR 3.78)
  - small opacities larger than 1.5 mm (RR 2.17)
  - caisson work (RR 1.56)

  (Chang, Leung & Tam, *Int J Tuberc Lung Dis* 2001;5:177-84, **PMID 11258512**)
- **HIV.** In South African gold miners, HIV and silicosis combined *multiplicatively* in raising TB risk. TB incidence was 4.9 per 100 person-years in HIV-positive miners versus 1.1 in HIV-negative miners (Corbett et al., *AIDS* 2000;14:2759-68; PMID not retrieved; summarized in https://pmc.ncbi.nlm.nih.gov/articles/PMC2078150).
- **Higher silicosis grade and underground exposure** raised TB incidence in gold miners (Cowie, *Am J Respir Crit Care Med* 1994;150:1460-2, doi 10.1164/ajrccm.150.5.7952577; PMID not retrieved).
- **Zhejiang, China (1,659 silicosis patients).** Age, being underweight, and prior contact with a TB patient were associated with active TB. Contact gave an OR of 4.33 (95% CI 1.99–9.43) (Yang et al., *Microbiol Spectr* 2022, **PMID 36453892**, PMC9784764).
- **High-risk settings:**
  - gold mining
  - artisanal and small-scale mining (systematic review, **PMID 37733799**)
  - gemstone mining (Harris et al., *Cureus* 2025, PMC11793831)
  - engineered-stone fabrication, where latent TB has been found in affected workers (CDC MMWR, https://stacks.cdc.gov/view/cdc/231365)

**Genetic risk and protective factors (candidate-gene studies only; none replicated)**
- **FAM13A** rs2609255. The TG genotype was protective against TB in Brazilian silicosis patients: OR 0.46 (0.22–0.98), p=0.040, n=143 (Castro et al., *J Bras Pneumol* 2025;51:e20240327, PMC12401099). Variants in ACE, FAS, FASLG, IL1RN, NOS2, TGFB1 and TNF were also tested.
- **SLC11A1 (NRAMP1)** INT4 C allele. A Chinese study of silica-exposed workers (61 cases with pulmonary TB, 122 controls) found about 2.7-fold higher risk. The D543N variant showed no association (https://www.jstage.jst.go.jp/article/joh/50/6/50_L8006/_article/-char/en).
- **TNF, TGFB1, IL10, IFNG** variants showed no association in Chinese iron miners (same search results; PMID not retrieved).

**Protective factors**
- **BCG vaccination** independently lowered the risk of latent TB infection in silicosis patients: OR 0.612 (0.468–0.801) (PMID 36453892).
- **TB preventive therapy:** see Sections 12–13.
- **Lower dust exposure:** the exposure-response gradient implies this protects.

**Gene–environment interaction:** No formal studies were found. The Brazilian and Chinese candidate-gene studies were done *within* silica-exposed groups, which conditions on the exposure but does not test interaction.

---

## 3. Phenotypes

The table combines features of both diseases. Where I found no source for a feature, the table says so. HPO labels are suggestions and their IDs were not retrieved.

| Phenotype | Type | Suggested HPO label | Evidence / frequency |
|---|---|---|---|
| Cough, haemoptysis, dyspnoea, night sweats, fatigue | Symptoms | Cough; Hemoptysis; Dyspnea; Night sweats; Fatigue | Case report: 2 months of haemoptysis, dyspnoea, night sweats and fatigue (PMC11793831) |
| Weight loss / underweight | Sign | Weight loss | Underweight was associated with active TB in Zhejiang (PMID 36453892) |
| Bilateral nodules; conglomerate masses / progressive massive fibrosis | Imaging | Pulmonary nodules; Pulmonary fibrosis | PMID 11258512; PMC2929613 |
| Cavitation within a conglomerate mass | Imaging | Pulmonary cavitation | 8 of 44 silicosis patients with conglomerate masses had cavitation on HRCT; 6 of those 8 had TB. Cavitation can also come from ischaemic necrosis (PMC2929613) |
| Hypermetabolic nodules on PET/CT | Imaging | — | Can mimic cancer or sarcoidosis (D'Sa et al., *Diagnostics* 2023, **PMID 37685266**) |
| Positive sputum culture or Xpert for *M. tuberculosis* | Lab | — | Sputum smear and BAL can be negative (PMC2929613) |
| Positive IGRA or TST | Lab | — | Among silicosis patients without active TB: QFT positive in 40.5% (lower with more severe silicosis), TST positive in 57.2% (PMID 36453892) |
| Impaired lung function | Functional | Abnormal pulmonary function / restrictive or obstructive ventilatory defect | TB accelerates impairment (PMID 39694587). Specific frequencies not retrieved |

- **Onset:** adult, after years of exposure. The disease is chronic and progressive.
- **Quality of life:** No disease-specific EQ-5D or SF-36 data were retrieved. A study of Lesotho ex-miners describes "a considerable disability and care burden on families" (https://pmc.ncbi.nlm.nih.gov/articles/PMC8546409).

---

## 4. Genetic and molecular information

- **Causal genes:** none. There are no known pathogenic variants, so ClinVar, ACMG classification and gnomAD data do not apply. Germline versus somatic origin does not apply. No chromosomal abnormalities are known.
- **Susceptibility and modifier genes:** FAM13A and SLC11A1 (see Section 2). The HGNC IDs were not retrieved.
- **Epigenetics:** no studies were found that are specific to silicotuberculosis.

---

## 5. Environmental information

- **Toxicant:** respirable crystalline silica (quartz). Exposure comes from mining, quarrying, stone and engineered-stone work, pottery, caisson work and foundries (PMID 11258512; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7156992 covers mine and pottery cohorts).
- **Infectious agent:** *Mycobacterium tuberculosis* complex. The NCBI Taxon ID was not retrieved. Non-tuberculous mycobacteria are included by MeSH.
- **Co-factors:** HIV infection, undernutrition, crowded mine hostels, and migrant labour patterns. In Lesotho ex-gold miners (n=2,678), prevalences were (PMC8546409):
  - silicosis 42.5%
  - HIV 30.7%
  - silicotuberculosis 25.7%
  - active TB 6.8%
- **Smoking:** studied together with silica for mortality in Chinese cohorts (PMC7156992). No silicotuberculosis-specific estimate was retrieved.

---

## 6. Mechanism and pathophysiology

**Causal chain (evidence type in brackets)**

1. Crystalline silica is inhaled and taken up (phagocytosed) by **alveolar macrophages**. [established; reviewed in PMID 33598569 and PMC6334662]
2. Silica damages the macrophages. This **leads to** less TLR2 expression, lower anti-apoptotic Bcl-2 and Mcl-1, and higher JNK1 and ASK1. These changes prime the cells for necrotic rather than apoptotic death. [in vitro, THP-1 cells; Chávez-Galán et al., *PLoS One* 2013, **PMID 24278357**]
3. Once infected with *M. tuberculosis*, silica-exposed macrophages die by **necrosis instead of apoptosis**. This **results in** poorer control of the bacteria, more TNF-α, IL-1β and caspase-9, and release of bacteria. [in vitro, PMID 24278357. Lanzafame & Vento 2021, PMID 33598569: silica "increase[s] intracellular replication of *M. tuberculosis* and release from macrophages"]
4. In parallel, silica injury releases the cell's own **DNA into the extracellular space**. This activates the **cGAS–

Understood. I'll continue the report in a clinical/public-health register, finishing the remaining sections.

## 6. Mechanism and pathophysiology (continued)

**Causal chain, at a high level** (evidence type in brackets):

1. Inhaled silica is taken up by alveolar macrophages, which it injures. This impairs the lung's first line of antimicrobial defence. [established; reviews PMID 33598569; PMC6334662]
2. Impaired macrophages handle *M. tuberculosis* less well, so the bacteria persist more readily in the lung. [in vitro, PMID 24278357; mouse work below]
3. Silica also causes sterile tissue injury and a type-2–skewed immune environment (more Th2 and M2 macrophage responses, less type-1 immunity), which is less effective against mycobacteria. This involves the cGAS–STING / type-I-interferon axis responding to released self-DNA. [mouse model, Benmerzoug et al., *Cell Reports* 2019;27:2649-2664, **PMID 31141689**]
4. Ongoing silicotic fibrosis plus TB inflammation produces progressive scarring, conglomerate masses and progressive massive fibrosis, driving loss of lung function and higher mortality. [clinical/review, PMID 39694587]

**Supporting evidence by level**
- **Reduced TLR2** after silica exposure may partly explain higher TB susceptibility (Konečný et al., PMC6334662; consistent with PMID 24278357).
- **Mouse models:** airway delivery of silica "increases susceptibility to mycobacterial infection," with a role for repopulating macrophages (**PMID 19454707**). Transfer of alveolar macrophages from silica-exposed mice made recipient mice more susceptible, i.e. silica can convert mycobacteria-resistant mice into susceptible ones.
- **STING pathway:** cGAS-, STING- and IFNAR-deficient mice were resistant to silica-induced worsening of *M. tuberculosis* infection, implicating this pathway and suggesting it as a possible therapeutic target (PMID 31141689).
- **Rat model:** tuberculosis burden and lung-lesion severity correlated positively with silicosis (PMC12431572).

**Upstream vs downstream.** Upstream: silica uptake and macrophage dysfunction, loss of TLR2-mediated recognition, sterile inflammation. Downstream: failure to contain *M. tuberculosis*, granulomatous and fibrotic lung damage, cavitation, progressive massive fibrosis.

**Cells and processes involved (ontology labels suggested; IDs not retrieved):**
- Cell Ontology labels: alveolar macrophage, macrophage, dendritic cell, T-helper-2 cell.
- GO biological-process labels: response to inflammation, phagocytosis, macrophage apoptotic process, necrotic cell death, type I interferon signaling pathway, cellular response to silica.
- Pathway resources to confirm: cGAS-STING signaling; TLR signaling. KEGG/Reactome IDs not retrieved.

Omics, single-cell, spatial and CRISPR-screen data specific to silicotuberculosis: none retrieved.

---

## 7. Anatomical structures affected

- **Primary organ:** lung (UBERON label "lung"). Both diseases are centred here.
- **Body system:** respiratory system.
- **Secondary involvement:** hilar and mediastinal lymph nodes; pleura. The case literature also notes neck (cervical) nodes in some presentations (Radiopaedia case 66090). Systemic effects include wasting/cachexia (ICD-10 allows E88.A as an added code).
- **Tissue level:** alveolar and interstitial lung tissue; fibrotic (connective) tissue in silicotic nodules and conglomerate masses.
- **Cell populations:** alveolar macrophages are the key targeted cells (PMID 24278357; PMID 19454707).
- **Subcellular (GO cellular-component labels):** phagosome/phagolysosome; cytosol (site of DNA-sensing); mitochondria (implicated in the apoptosis/necrosis balance). IDs not retrieved.
- **Localization / lateralization:** usually bilateral, upper-zone-predominant disease; conglomerate masses are often bilateral but can be asymmetric (PMC2929613; case reports).

---

## 8. Temporal development

- **Onset:** adult, typically after years of cumulative silica exposure. TB can be the event that brings silicosis to light.
- **Pattern:** chronic and insidious, with episodes of active TB superimposed. TB may recur; relapse is a specific concern (Section 12).
- **Stages/progression:** silicosis is graded radiologically (simple nodular → progressive massive fibrosis). TB risk rises with grade (PMID 11258512; Cowie 1994). TB "accelerates impairment and mortality" (PMID 39694587).
- **Critical window:** the period around silicosis diagnosis is an intervention opportunity. Lack of prior anti-TB treatment was the strongest risk factor in the Hong Kong cohort (RR 4.51, PMID 11258512), which is the rationale for preventive therapy.
- **Duration:** silicosis is lifelong and irreversible; TB is curable but may leave post-tuberculous lung disease (PMID 39694587).

---

## 9. Inheritance and population

- **Inheritance:** not applicable (non-genetic). Penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity and carrier frequency do not apply.
- **Epidemiology:**
  - Silicosis raises TB risk ~4-fold (PMID 34016067).
  - East African estimate: silicotuberculosis prevalence 3–7% in mining communities and 0.3–2.3% in the general population (PMC11793831).
  - Lesotho ex-gold miners: silicotuberculosis 25.7% (PMC8546409).
  - Chinese hematite-miner cohort: of silicosis cases, 42% were classified as silicotuberculosis (*Scand J Work Environ Health* 1989;15:319-322, https://www.sjweh.fi/article/1844).
  - South African gold miners' TB incidence reported at ~3,000/100,000 versus ~344/100,000 in the general population (https://pmc.ncbi.nlm.nih.gov/articles/PMC1128836).
- **Geography:** concentrated in high-TB-burden countries with silica-exposed workforces, especially southern Africa and parts of Asia; rising again with engineered-stone work in higher-income countries (PMID 39694587; CDC MMWR).
- **Sex:** overwhelmingly male in the mining cohorts (trials and cohorts were in men), reflecting the workforce rather than biology (e.g. PMID 11258512; the 1991 and 1992 Hong Kong trials enrolled Chinese men).
- **Age:** working-age and older adults.

---

## 10. Diagnostics

- **Microbiology:** sputum smear, culture and Xpert MTB/RIF for *M. tuberculosis*. Caveat: smear and BAL can be negative in silicotuberculosis, so a negative smear does not exclude it (PMC2929613). No pooled Xpert sensitivity specific to silicotuberculosis was retrieved.
- **Immunological tests:** IGRA (QuantiFERON-TB Gold) and TST detect infection but may *underestimate* latent infection in silicosis; QFT positivity fell with more severe silicosis (40.5% QFT vs 57.2% TST among non-active-TB patients, PMID 36453892).
- **Imaging:** chest X-ray and HRCT. Features that raise suspicion of TB on a background of silicosis: new or rapidly changing opacities, cavitation within a conglomerate mass, and asymmetric change. Cavitation is suggestive but not specific, as it also occurs from ischaemic necrosis (PMC2929613). PET/CT shows hypermetabolic nodules that can mimic malignancy (PMID 37685266).
- **Histology:** sometimes needed when imaging is ambiguous; diagnosis in one engineered-case required histology and molecular testing of a resected mass (PMID 37685266).
- **Key clinical principle:** the two diseases overlap closely in appearance, which "continues to pose a challenge to imaging, diagnosis and pathological description" (PMID 39694587). A high index of suspicion and attention to occupational history are essential (see also PMID 41497771 on occupational history).
- **Differential diagnosis:** silicosis alone, sarcoidosis ("silicosarcoidosis" overlap, PMID 41691440), lung cancer, metastasis, and non-tuberculous mycobacterial disease.
- **Genetic/omics diagnostics:** not applicable.
- **Screening:** systematic TB testing of people with silicosis is recommended (Section 13).

Suggested coding terms: SNOMED CT and LOINC concepts apply to the component tests (sputum culture, Xpert, IGRA); specific IDs not retrieved.

---

## 11. Outcome and prognosis

- **Mortality:** silicotuberculosis is a major cause of death in silica-exposed cohorts. In the Chinese hematite-miner cohort, of underground miners who died, 42% died of silicosis/silicotuberculosis, and the silicotuberculosis standardized mortality ratio was markedly elevated (SMRN reported as 1000; *Scand J Work Environ Health* 1989, sjweh.fi/article/1844).
- TB "accelerates impairment and mortality" in silicosis (PMID 39694587).
- **Relapse:** a specific prognostic concern. With a 6-month regimen, bacteriological relapse over 3 years was 22%, versus 7% with 8 months (Hong Kong Chest Service/BMRC, *Am Rev Respir Dis* 1991;143:262-7, **PMID 1990938**). This is why longer treatment is advised.
- **Morbidity:** progressive massive fibrosis, respiratory failure, and post-tuberculous lung disease; high disability and care burden (PMC8546409).
- **Prognostic factors:** severity/grade of silicosis, HIV co-infection, presence of progressive massive fibrosis, and whether TB preventive/curative treatment was given (PMID 11258512; Corbett 2000).
- **Direct survival curves** comparing silicotuberculosis vs silicosis alone were not retrieved.

---

## 12. Treatment

**Active TB treatment**
- Standard multidrug anti-TB therapy is the backbone. A specific caveat in silicosis is a higher relapse rate with standard-duration therapy.
- The Hong Kong Chest Service/BMRC trial (240 men with silicosis + pulmonary TB) compared 6 vs 8 months of thrice-weekly streptomycin + isoniazid + rifampicin + pyrazinamide. Relapse was 22% (6 months) vs 7% (8 months), p<0.025, favouring the longer course (**PMID 1990938**). Note: retrieved copies of the abstract disagree on whether the stated conclusion is "at least 6" or "at least 8" months; the relapse data support the longer course. This should be verified against the primary source.
- NCIT clinical-intervention labels: "Isoniazid", "Rifampicin", "Pyrazinamide", "Streptomycin" (IDs not retrieved).

**TB preventive therapy (latent infection / silicosis without active TB)**
- Randomized placebo-controlled trial in 679 Chinese men with silicosis compared rifampicin 3 months, isoniazid+rifampicin 3 months, isoniazid 6 months, or placebo. Preventive therapy roughly **halved** the proportion developing TB (placebo worse at every follow-up; combined active regimens vs placebo p<0.01), though residual risk remained substantial. The three active regimens did not differ significantly; no selection of drug-resistant bacilli was seen (Girling & Chan, Hong Kong Chest Service/Tuberculosis Research Centre Madras/BMRC, *Am Rev Respir Dis* 1992;145:36-41, **PMID 1731596**).
- **Community-level caution:** mass isoniazid preventive therapy in South African gold miners (Thibela TB, 78,744 miners) reduced TB *while individuals took it* but did not improve TB control at the population level (Churchyard et al., *NEJM* 2014;370:301-310, doi 10.1056/NEJMoa1214289; PMID not retrieved).

**Experimental / mechanism-based (preclinical only)**
- Targeting the cGAS-STING/nucleic-acid axis is proposed as a future therapeutic direction (PMID 31141689).
- Diosgenin reduced mycobacterial growth and improved lung function in a rat silica model using *M. smegmatis* as a surrogate (PMC12431572). Resveratrol has been studied for silica-induced lung oxidative stress/inflammation in rats (PMID 36941929). Both are early-stage.

**Supportive/other:** management of HIV co-infection, smoking cessation, pulmonary rehabilitation, and removal from further silica exposure. Advanced silicosis may ultimately require lung transplantation (reported in engineered-stone cohorts; CDC/ESSI sources). No gene, cell or RNA therapies exist for this condition. Pharmacogenomics specific to silicotuberculosis: none retrieved.

---

## 13. Prevention

- **Primary prevention (most important):** eliminate or control silica dust exposure through engineering controls, dust suppression, respiratory protection, substitution and regulation. The South African industry's 2003 commitment aimed for no new silicosis cases by 2013 among newly unexposed miners; prevalence had not significantly declined by 2004–2009 (https://link.springer.com/10.1186/s12889-015-2566-8), showing how hard primary prevention is in practice.
- **Secondary prevention:** systematic TB testing and treatment in people with silicosis. WHO lists silicosis among the groups that "should be systematically tested and treated for LTBI" (WHO consolidated guidelines on TB, Module 1: prevention, https://tbksp.who.int/en/node/1027; updated 2nd edition https://www.who.int/publications/i/item/9789240096196). TB preventive therapy is effective (PMID 1731596).
- **Immunization:** BCG was associated with lower latent-infection risk in silicosis patients (OR 0.612, PMID 36453892), though BCG is not a silicosis-specific intervention.
- **Tertiary prevention:** early detection and full-duration treatment of active TB to prevent relapse and progressive massive fibrosis (PMID 1990938); HIV testing and antiretroviral therapy.
- **Screening/surveillance:** medical surveillance programmes for silica-exposed workers (e.g. Australian engineered-stone programmes) detect early disease (CDC/insightplus sources). Genetic screening and counselling do not apply.

---

## 14. Other species and natural disease

- **Experimental species affected:** mouse (silica + *M. tuberculosis*: PMID 31141689, PMID 19454707) and rat (silica + mycobacteria: PMC12431572). NCBI Taxon IDs not retrieved.
- **Naturally occurring disease / breeds / OMIA entry:** none retrieved. Silicosis has been described in horses and dogs from environmental silica, but no silicotuberculosis veterinary entity was found in this session.
- **Zoonotic potential / cross-species transmission:** not a defining feature of this condition (it is an exposure-plus-infection syndrome). *M. tuberculosis* itself can occasionally infect animals, but that is outside what was retrieved here.
- **Comparative biology / evolutionary conservation:** the macrophage-based mechanisms are conserved enough that mouse and rat models reproduce key features (increased mycobacterial susceptibility after silica), supporting their translational use (PMID 31141689; PMID 19454707; PMC12431572).

---

## 15. Model organisms

- **Mouse (induced, not genetic):** silica given intratracheally or intranasally before *M. tuberculosis* (e.g. H37Rv) infection.
  - Benmerzoug et al. gave silica 7 days before infection and analysed at day 28; showed increased Th2/M2 responses, reduced type-1 immunity, and a cGAS-STING/self-DNA mechanism. Knockout mice (cGAS−/−, STING−/−, IFNAR−/−) were protected (**PMID 31141689**).
  - Airway silica increased mycobacterial susceptibility, implicating repopulating macrophages; alveolar-macrophage transfer conferred susceptibility (**PMID 19454707**).
- **Rat (induced):** intratracheal crystalline silica followed by mycobacterial challenge; used to test candidate drugs (diosgenin, PMC12431572; resveratrol for silica lung injury, PMID 36941929). *M. smegmatis* is used as a lower-biosafety surrogate for *M. tuberculosis*.
- **In vitro:** human THP-1 macrophages pre-exposed to crystalline silica then infected, showing impaired control of bacterial growth and altered cell-death balance (**PMID 24278357**).
- **Genetic models (knockout):** cGAS, STING (Tmem173) and Ifnar knockout mice used to dissect mechanism (PMID 31141689).
- **Phenotype recapitulation:** models reproduce the core human feature (silica worsens mycobacterial infection/clearance) and silicotic lung pathology. **Limitations:** dose, route, timing and mycobacterial strain vary across studies; surrogate organisms (*M. smegmatis*) and short timeframes do not capture chronic human silicotuberculosis, progressive massive fibrosis over years, HIV co-infection, or human treatment relapse. No single standardized model exists.
- **Resources:** MGI for mouse alleles (not queried here).

---

## Key references (as retrieved this session)

- Ehrlich R, Murray J, Said-Hartley Q, Rees D. Silicotuberculosis: a critical narrative review. *Eur Respir Rev* 2024;33:240168. **PMID 39694587**. https://pubmed.ncbi.nlm.nih.gov/39694587/
- Ehrlich R, Akugizibwe P, Siegfried N, Rees D. The association between silica exposure, silicosis and tuberculosis: a systematic review and meta-analysis. *BMC Public Health* 2021. **PMID 34016067**. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8136154/
- Konečný P, Ehrlich R, Gulumian M, Jacobs M. Immunity to the Dual Threat of Silica Exposure and *Mycobacterium tuberculosis*. *Front Immunol* 2019;9:3069. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6334662/
- Lanzafame M, Vento S. Mini-review: silico-tuberculosis. **PMID 33598569**. https://pmc.ncbi.nlm.nih.gov/articles/PMC7868994
- Chang KC, Leung CC, Tam CM. Tuberculosis risk factors in a silicotic cohort in Hong Kong. *Int J Tuberc Lung Dis* 2001;5:177-84. **PMID 11258512**. https://pubmed.ncbi.nlm.nih.gov/11258512
- Corbett EL et al. HIV infection and silicosis. *AIDS* 2000;14:2759-68. https://pmc.ncbi.nlm.nih.gov/articles/PMC2078150 (PMID not retrieved)
- Cowie RL. Epidemiology of tuberculosis in gold miners with silicosis. *Am J Respir Crit Care Med* 1994;150:1460-2. (PMID not retrieved)
- Hong Kong Chest Service/BMRC. A controlled trial of 6 and 8 months of anti-TB chemotherapy in silicotuberculosis. *Am Rev Respir Dis* 1991;143:262-7. **PMID 1990938**.
- Girling DJ, Chan SL (Hong Kong Chest Service/TRC/BMRC). Preventive chemotherapy trial in silicosis. *Am Rev Respir Dis* 1992;145:36-41. **PMID 1731596**.
- Churchyard GJ et al. (Thibela TB). Mass isoniazid preventive therapy. *NEJM* 2014;370:301-310. (PMID not retrieved)
- Benmerzoug S et al. Sterile lung inflammation induced by silica exacerbates *M. tuberculosis* infection. *Cell Reports* 2019;27:2649-2664. **PMID 31141689**.
- Chávez-Galán L et al. Pre-exposure of *M. tuberculosis*-infected macrophages to crystalline silica. *PLoS One* 2013. **PMID 24278357**. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3838437/
- Airway delivery of silica increases susceptibility to mycobacterial infection in mice. **PMID 19454707**.
- Yang et al. *M. tuberculosis* infection among 1,659 silicosis patients in Zhejiang. *Microbiol Spectr* 2022. **PMID 36453892**. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9784764/
- Castro et al. FAM13A polymorphism and TB protection in Brazilian silica-exposed patients. *J Bras Pneumol* 2025;51:e20240327. https://pmc.ncbi.nlm.nih.gov/articles/PMC12401099
- Harris et al. Diagnosis and management of silicotuberculosis in resource-limited East Africa. *Cureus* 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11793831/
- D'Sa et al. Silicotuberculosis case report. *Diagnostics* 2023. **PMID 37685266**.
- Lesotho ex-gold-miner occupational health study. https://pmc.ncbi.nlm.nih.gov/articles/PMC8546409
- MeSH D012830. https://meshb.nlm.nih.gov/record/ui?ui=D012830
- WHO consolidated guidelines on TB, Module 1: prevention. https://tbksp.who.int/en/node/1027

---

**Caveats for the knowledge-base curator.** (1) This is a non-genetic, exposure-plus-infection disease. No causal gene, no OMIM/Orphanet entry, no inheritance pattern. (2) All ontology IDs (HPO, GO, CL, UBERON, CHEBI, NCIT, NCBI Taxon, HGNC) need to be looked up and verified; only labels are suggested here. (3) PMIDs are given only where retrieved; several papers (Corbett 2000, Cowie 1994, Thibela TB) are cited without a confirmed PMID. (4) Candidate-gene associations (FAM13A, SLC11A1) are small and unreplicated. (5) The PMID 1990938 abstract's stated conclusion appears inconsistent across mirrors and should be checked against the primary source.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 5 |
| References weighed for topical relevance | 30 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

3 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC6334662` *(abstract only)*: "dual disease, referred to as silicotuberculosis"
  - closest text in source: "In this review, we focus on the host's immunological response to both silica and Mycobacterium tuberculosis, on agents of innate and adaptive immunity, and particularly on silica-induced immunological modifications in co-exposure that influence disease pathogenesis"
- `PMID:34016067`: "low severity threshold"
  - Text part not found as substring: 'low severity threshold'
- `PMC:PMC8136154`: "low severity threshold"
  - Text part not found as substring: 'low severity threshold'
- `PMC:PMC8546409` *(abstract only)*: "a considerable disability and care burden on families"
  - closest text in source: "BACKGROUND: A legacy of the South African gold mining industry, now in decline, is a large burden of silicosis and tuberculosis among former migrant miners from rural South Africa and surrounding countries, particularly Lesotho and Mozambique"
- `PMID:39694587` *(abstract only)*: "accelerates impairment and mortality"
  - Text part not found as substring: 'accelerates impairment and mortality' (note: only abstract available for PMID:39694587, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0021804` (2 mentions) - the report calls it "MONDO"; MONDO calls it **silicotuberculosis**