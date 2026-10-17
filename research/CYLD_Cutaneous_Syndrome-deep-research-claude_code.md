---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-13T20:44:49.809107'
end_time: '2026-10-13T20:46:04.339091'
duration_seconds: 74.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CYLD Cutaneous Syndrome
  mondo_id: MONDO:0011512
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 4
  num_turns: 7
  total_cost_usd: 0.7400011000000002
  session_id: aa4f0803-31cb-5b9b-8409-a0195ed1b485
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 12
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 5
  verified: 4
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.2
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0100677
    reported_labels:
    - Cylindroma
    ontology_label: Vulval varicose vein
  unresolved_terms:
  - HP:0100782
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CYLD Cutaneous Syndrome
- **MONDO ID:** MONDO:0011512 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CYLD Cutaneous Syndrome** covering all of the
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

# CYLD Cutaneous Syndrome (MONDO:0011512): research report

**Provenance of this report.** Web access was limited. Four standard searches returned snippets. A direct fetch of the GeneReviews chapter (NBK555820) was blocked by a browser-verification page. Items below are labelled by source class:
- **[search]**: stated in a search-result summary, with the source URL named.
- **[model]**: my own background knowledge, not checked in this session. Treat these as leads.
- **[gap]**: not found.

PMIDs are given only where the search result showed them. I have not verified any exact snippets. Nothing here is ready to copy into a KB `evidence:` block without `just fetch-reference` and snippet checks.

## 1. Disease information
- **Overview.** CYLD cutaneous syndrome (CCS) is an autosomal dominant predisposition to multiple adnexal skin tumors: cylindromas, spiradenomas and trichoepitheliomas. It is caused by heterozygous CYLD variants at 16q12. The first tumor typically appears around puberty, and tumors accumulate with age, mostly on the scalp and face. Females often have more tumors than males. [search: GeneReviews NBK555820, Dubois and Rajan, 2020; summary only, via [GeneReviews PDF](https://https.ncbi.nlm.nih.gov/books/NBK555820/pdf/Bookshelf_NBK555820.pdf)]
- **Lump decision.** GeneReviews and MedlinePlus treat Brooke-Spiegler syndrome (BSS), familial cylindromatosis (FC) and multiple familial trichoepithelioma (MFT) as one condition. They were formerly considered distinct. [search: GeneReviews]
  - The KB file name `Brooke-Spiegler_Syndrome` therefore reflects a historical split. It is a lump/split call to surface.
  - MFT has a separate locus at 9p21, and sporadic trichoepitheliomas have been linked to PTCH. [search: GeneReviews] The CYLD-negative families are genetically heterogeneous, so a CYLD-defined entry should not claim them.
- **Identifiers.**
  - MONDO:0011512 was given in the task.
  - OMIM, Orphanet, ICD and MeSH identifiers: [gap]. I did not verify them and will not write them from memory.
  - A MedGen record exists at C1857941. [search, via [MedGen](https://ncbi.nlm.nih.gov/medgen/C1857941)]
- **Synonyms.** Brooke-Spiegler syndrome, familial cylindromatosis, multiple familial trichoepithelioma, Brooke-Spiegler/Spiegler-Brooke, "turban tumor syndrome" (the last is [model]).
- **Source level.** Aggregated disease-level resources and cohorts, not EHR-derived.

## 2. Etiology
- **Cause.** Germline heterozygous loss-of-function CYLD variants. [search: [JCI/Dermatology reviews as surfaced](https://www.ncbi.nlm.nih.gov/books/NBK555820/)]
- **Second hit.** In cylindroma cells both copies of CYLD are inactivated, and biallelic loss alone appears sufficient to drive tumorigenesis. [search: Nature Communications 2019, Rajan et al.; PMID not shown, see [IDEAS record](https://ideas.repec.org/a/nat/natcom/v10y2019i1d10.1038_s41467-019-12746-w.html)]
  - Tumor-suppressor biology is not elaborated here, as you asked.
- **Modifiers.**
  - Expression varies within and between families, so a modifier effect is suggested. [search: GeneReviews]
  - Specific modifier genes: [gap].
- **Environmental and protective factors.** [gap]. I found no evidence for either. DMBA/TPA promotes tumors in mice (section 15), but there is no human exposure evidence.
- **Gene-environment interaction.** [gap].

## 3. Phenotypes (candidate HPO terms are [model] and need lookup before binding)

| Phenotype | Candidate HPO | Frequency / onset |
|---|---|---|
| Cylindroma | HP:0100677 (Cylindroma) | Core feature; onset puberty onward [search: GeneReviews] |
| Spiradenoma | spiradenoma term (lookup needed) | Core feature |
| Trichoepithelioma | HP:0100782 (Trichoepithelioma) | Core feature |
| Salivary gland basal cell adenoma (membranous type) | lookup needed | "A minority" develop salivary tumors [search: GeneReviews] |
| Malignant transformation (e.g. spiradenocarcinoma, cylindrocarcinoma) | lookup needed | Uncommon but recognized [search: GeneReviews; [2026 case report](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1703885/full)] |

- **Pediatric framing.** The first lesion is typically at puberty, per GeneReviews. Onset before puberty is possible but I did not find data on it ([gap]). Female excess in tumor burden is reported. [search: GeneReviews]
- **Specific percentages.** I could not obtain them. Frequencies for hair loss from scalp tumors, pain, disfigurement and quality of life are [gap].
- **Tumor sites.** Mostly scalp and face, as above.

## 4. Genetic and molecular information
- **Gene.** CYLD, 16q12. Use `hgnc:` lowercase form once the ID is looked up; I have not verified the HGNC ID here.
- **Variant spectrum.**
  - A 2007 Dermatology Online Journal review counted 68 unique mutations. The count has since grown. [search: GeneReviews/MalaCards summary]
  - Variants are loss of function, and the encoded protein is truncated or inactive. [search]
  - The classic nonsense/frameshift/splice pattern is [model].
  - The founding discovery paper is Bignell et al. 2000, Nat Genet. I recall PMID 10873394 [model, unchecked]. The [CYLD mutations paper](https://scholars.mssm.edu/en/publications/cyld-mutations-underlie-brooke-spiegler-familial-cylindromatosis--2/) in the search results is the related Mount Sinai record for the lump into one syndrome.
- **Genotype-phenotype.** I found no cohort-level genotype-phenotype correlation. Phenotype varies even among carriers of the same variant. [search: GeneReviews]
- **Mosaicism.** A UK cohort of 55 patients found 2 with mosaic pathogenic CYLD variants in blood and skin. [search; source not identified; verify before citing, via [PMC8566010](https://pmc.ncbi.nlm.nih.gov/articles/PMC8566010)]
  - Consider the `somatic-mosaicism` skill if a mosaic subtype is curated.
  - Mosaicism would explain clustered or segmental tumors with negative standard testing. [search]
- **Tumor genomics.** A study of 42 tumors from 13 individuals found recurrent DNMT3A and BCOR mutations in 29% of benign tumors. [search; likely the same Nat Commun 2019 paper, unconfirmed]
- **Epigenetics, chromosomal abnormalities, population allele frequencies.** [gap].

## 5. Environmental information
No environmental, lifestyle or infectious factors were found. [gap]

## 6. Mechanism / pathophysiology

**Ordered causal chain**
1. A germline heterozygous CYLD loss-of-function variant is present in every cell. [search]
2. A somatic second hit inactivates the other allele in a skin adnexal progenitor cell. Demonstrated in cylindroma tissue (Nat Commun 2019, per search). The exact cell of origin is [model]: eccrine/apocrine or pilosebaceous adnexal lineage, unverified.
3. Loss of CYLD leaves non-K48 (principally K63) polyubiquitin chains on TRAF2 and NEMO unedited. CYLD binds both proteins and removes these chains. [search: Brummelkamp 2003, PMID 12917691; Kovalenko 2003; Courtois 2008 review]
4. IKK/NF-κB activation persists and apoptosis resistance increases. [search: Brummelkamp 2003 abstract]
5. This leads to clonal expansion and tumor formation. Intermediate steps are inferred. The 2016 JCI Insight mouse work implicates c-Myc and TRAF6. [search]
6. Rarely, cooperating mutations drive malignant transformation. [search: the Nat Commun 2019 tumor genomics; the 2026 case report involved an MSH2 VUS, which proves nothing about causation]
7. The cylindroma-to-spiradenoma-to-trichoepithelioma spectrum may reflect differing differentiation of the transformed cell. This is [model] inference and not demonstrated here.

- **Branch.** CYLD also acts in T-cell receptor signalling and mitosis, so NF-κB may not be the whole story. [search: Courtois 2008]
- **Suggested GO terms** [model, need lookup]: protein deubiquitination, K63-linked deubiquitinase activity, regulation of NF-κB signaling, negative regulation of apoptotic process.
- **Omics, single-cell, spatial and CRISPR data.** [gap], apart from the tumor exome data above.
- **Immune system involvement.** CYLD-deficient mouse immune cells show enhanced NF-κB and JNK signalling, and colitis-associated cancer risk goes up. This is mouse data (Zhang et al., JCI). [search] I found no human immune phenotype in CCS.

## 7. Anatomical structures affected
- **Organs.** Skin of scalp and face is primary. Major salivary glands (parotid) are secondary. [search for salivary; sites beyond scalp/face: model]
- **Cells and tissues.** Adnexal epithelium. CL and UBERON term selection is [gap]; look them up.
- **Subcellular.** CYLD is a cytoplasmic deubiquitinase [model]. GO CC terms were not checked.
- **Lateralization.** [gap].

## 8. Temporal development
- Onset is at puberty. Tumors accumulate with age, and their number rises through adulthood. [search: GeneReviews]
- Course is progressive and lifelong. Staging is not applicable.
- Remission patterns and critical periods: [gap].

## 9. Inheritance and population
- **Pattern.** Autosomal dominant, with variable expressivity within and between families and variable penetrance. [search: GeneReviews]
  - Specific penetrance figures: [gap]. I did not find any. Do not substitute a "near-complete" claim without a source.
- **Prevalence.** [gap]. The Orphanet value was not checked.
- Anticipation, founder effects, carrier frequency, ancestry, geography and sex ratio: [gap]. Female excess in tumor number is the only point found. [search]
- **Germline mosaicism.** Parental mosaicism has not been verified here.

## 10. Diagnostics
- **Clinical.** Multiple cylindromas, spiradenomas or trichoepitheliomas, or a single tumor with a family history. A membranous basal cell adenoma-type salivary tumor in someone with a single cylindroma, spiradenoma or trichoepithelioma also counts. [search: GeneReviews diagnostic criteria, secondhand]
- **Biopsy.** Histopathology of the adnexal tumors is diagnostic.
- **Genetic testing.** CYLD sequencing plus deletion/duplication analysis is expected [model; GeneReviews testing section not read]. A negative result in blood does not exclude mosaicism. [search]
- **Differential.** Birt-Hogg-Dubé (trichodiscomas and fibrofolliculomas), Cowden/PTEN hamartoma tumor syndrome (trichilemmomas), Gorlin/PTCH1 syndrome (BCC) [model, unchecked]. The GeneReviews differential was not read.
- **Screening.** [gap].

## 11. Outcome / prognosis
- Life expectancy and QoL: [gap].
- Complications are disfigurement from large scalp tumors (turban tumor) [model] and rare malignant transformation. [search]
- Prognostic factors: not found.

## 12. Treatment
- **Surgery** (excision, laser, electrodesiccation) is the mainstay [model]. This was not confirmed in the sources I could read.
- **Reported medical options** are limited to case-level evidence. [search: GeneReviews summary]
  - Sodium salicylate.
  - Prostaglandin A1.
  - Aspirin plus adalimumab.
  - Topical imiquimod.
  - The rationale from Brummelkamp 2003 was that aspirin derivatives block NF-κB and could reverse the effect. [search]
- A search for aspirin, salicylate or sirolimus trials returned nothing on the clinical side. I have no NCT IDs. Search ClinicalTrials.gov separately.
- Suggested NCIT terms (CURIEs not looked up): surgical procedure NCIT:C15329 and pharmacotherapy NCIT:C15986, both listed in CLAUDE.md. Neither was re-verified here.

## 13. Prevention
- Genetic counseling and cascade testing of relatives are standard for dominant conditions [model].
- A formal surveillance protocol for malignant transformation was not found. I did not read the GeneReviews surveillance section ([gap]). Sun protection has no support here.

## 14. Other species
No OMIA entry was found. [gap]

## 15. Model organisms
- **Mouse knockouts.**
  - Cyld-/- mice are more prone to DMBA/TPA skin tumors than wild type. This is linked to BCL3 nuclear translocation and cyclin D1 expression. [search: Nature Reviews Mol Cell Biol summary of a separate study]
  - Zhang et al. (JCI) reported CYLD-deficient mice with more colitis and colitis-associated cancer. [search: [JCI 28746](https://jci.org/articles/view/28746/cite)]
- **Catalytically deficient CYLD.**
  - K14-driven catalytically deficient truncated CYLD sensitizes mice to DMBA/TPA skin tumors. [search: 2011 study]
  - The 2016 JCI Insight CyldEΔ9/Δ9 model develops mostly sebaceous and basaloid tumors that resemble human CYLD-mutant tumors, versus papillomas in wild type. A topical c-Myc inhibitor induced apoptosis. [search: [JCI Insight 86548](https://insight.jci.org/articles/view/86548/figure/3)]
  - A Nature Communications 2016 paper reported sensitization to chemical carcinogen-induced intestinal and skin tumors with loss of catalytic activity. [search: [Nat Commun 12508](https://link.springer.com/article/10.1038/ncomms12508)]
- **Fidelity.** These mice do not spontaneously develop cylindromas. All models are carcinogen-promoted, so they fit `evidence_source: MODEL_ORGANISM` with `FAILS_TO_RECAPITULATE`/`PARTIALLY_RECAPITULATES` considerations for the spontaneous human tumor phenotype. That judgement is mine ([model]), based on the search summaries.

## Key follow-ups before curation
1. Read GeneReviews NBK555820 in full (it is also the mandatory baseline for a Mendelian entry). Run `just fetch-reference` for it.
2. Retrieve primary PMIDs for the 2019 tumor genomics paper, the UK mosaicism cohort, and Bignell 2000 and Kovalenko 2003 (my recalled IDs are unverified).
3. Look up CURIEs (OMIM, Orphanet, HPO, GO, CL, UBERON, hgnc) with real lookups.
4. Decide the lump/split question for the BSS/FC/MFT names.
5. Quantitative frequencies, penetrance and surveillance are all open gaps.

## Sources
- [GeneReviews PDF NBK555820](https://https.ncbi.nlm.nih.gov/books/NBK555820/pdf/Bookshelf_NBK555820.pdf) and [GeneReviews NBK555820](https://www.ncbi.nlm.nih.gov/books/NBK555820/) (summary only; page fetch blocked)
- [MedGen C1857941](https://ncbi.nlm.nih.gov/medgen/C1857941)
- [CYLD mutations underlie BSS, FC and MFT](https://scholars.mssm.edu/en/publications/cyld-mutations-underlie-brooke-spiegler-familial-cylindromatosis--2/)
- [Brummelkamp 2003, PMID 12917691](https://pubannotation.org/docs/sourcedb/PubMed/sourceid/12917691)
- [JCI 28746 (Zhang et al.)](https://jci.org/articles/view/28746/cite)
- [Nat Commun 2019 tumor genomics](https://ideas.repec.org/a/nat/natcom/v10y2019i1d10.1038_s41467-019-12746-w.html)
- [2026 Frontiers case report](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1703885/full)
- [PMC8566010](https://pmc.ncbi.nlm.nih.gov/articles/PMC8566010)
- [JCI Insight 86548](https://insight.jci.org/articles/view/86548/figure/3)
- [Nat Commun 12508](https://link.springer.com/article/10.1038/ncomms12508)
- [Nature Reviews Mol Cell Biol, nrm1977](https://www.nature.com/articles/nrm1977)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 5 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100677` (1 mention) - the report calls it "Cylindroma"; HP calls it **Vulval varicose vein**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0100782` (1 mention), reported as "Trichoepithelioma" - HP does not contain this term