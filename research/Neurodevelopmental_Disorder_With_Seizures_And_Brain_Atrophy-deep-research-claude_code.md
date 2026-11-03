---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T15:32:04.955482'
end_time: '2026-10-15T15:36:49.433164'
duration_seconds: 284.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder With Seizures And Brain Atrophy
  mondo_id: MONDO:0033658
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 26
  total_cost_usd: 2.2327803999999993
  session_id: 78d82f81-499c-4ef4-89cf-1bf4a80dd8b5
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 4
citation_count: 7
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0033658
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with seizures and brain atrophy
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0090522
    ontology_label: obsolete vesicle tethering involved in exocytosis
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Seizures And Brain Atrophy
- **MONDO ID:** MONDO:0033658 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Seizures And Brain Atrophy** covering all of the
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

Researching EXOC7 / NEDSEBA literature now — PubMed tool was denied, so switching to web search.

Fetching the abstracts of the six EXOC7 disease papers I found.

Checking the 2023 exocyst review and OMIM for any EXOC7 patients reported after 2020, then I'll write the report.

# Neurodevelopmental Disorder With Seizures And Brain Atrophy (NEDSEBA; EXOC7-related): research report

**Scope.** The literature on this disease is very thin. One primary human study defines it: Coulter et al., *Genet Med* 2020 (PMID:32103185; PMC7272323; NIHMS1572592). I searched PubMed and Europe PMC through October 2026 and found no further published EXOC7 patient series. Everything below the "Disease information" section comes from that paper unless another source is named. Where a template section has no data, I say so rather than fill it.

**Tool limits.**
- The PubMed MCP tool was denied and the NCBI E-utilities rate-limited my requests.
- I read the abstracts and full texts through Europe PMC instead. Abstract quotes below are copied from that text but are short fragments, so check them with `just fetch-reference PMID:32103185` before using any as a `snippet:`.
- I did not look up any ontology CURIE in this session. Every term ID below is a lead to verify with `runoak` or the cache. **None is a checked binding.**

---

## 1. Disease information

**Overview.** NEDSEBA is an autosomal recessive disorder of cerebral cortical development caused by biallelic partial loss-of-function variants in **EXOC7**. EXOC7 encodes Exo70, a subunit of the octameric exocyst complex, which tethers secretory vesicles to the plasma membrane. The core features are:
- developmental delay or intellectual disability
- seizures
- progressive brain atrophy
- in severe cases, congenital microcephaly, arthrogryposis and death in infancy

MedGen's summary of OMIM describes "highly variable manifestations and severity." At the severe end, onset is in utero, with seizures at birth, poor growth, small head size, no developmental progress and marked atrophy. Milder cases have later-onset seizures, mild intellectual impairment and minimal atrophy.

**Identifiers**

| System | ID | Note |
|---|---|---|
| MONDO | MONDO:0033658 | Linked to OMIM 619072 by the DrugMap/LOVD cross-references. Confirm the xref in MONDO itself. |
| OMIM | #619072 | NEDSEBA, linked to EXOC7 ([LOVD](https://databases.lovd.nl/shared/diseases/06947)) |
| MedGen | C4749045 / UID 1748227 | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1748227) |
| Orphanet, ICD-10/11, MeSH | Not found | No disease-specific entry located. It probably falls under generic codes for epileptic encephalopathy or microcephaly. |

**Synonyms:** NEDSEBA; EXOC7-related neurodevelopmental disorder; EXOC7-related microcephaly and brain atrophy.

**Do not confuse it with OMIM #619076**, "neurodevelopmental disorder with microcephaly, seizures, and brain atrophy" (NEDMISBA). That disorder is caused by **EXOC8**, was reported in the same paper, and is a separate MONDO concept. If the dismech entry mentions EXOC8, it belongs in a differential-diagnosis note, not under `genetic:`.

**Data basis.** The disease-level descriptions are aggregated from published family reports (five families across both genes). There are no EHR data.

---

## 2. Etiology

- **Cause:** biallelic germline EXOC7 variants that reduce Exo70 function. The authors call them partial loss of function (hypomorphic).
- **Risk factors:** consanguinity (three of the four EXOC7 families). No environmental, sex or lifestyle risk factors are known.
- **Protective factors, gene–environment interactions:** none reported.
- **Modifiers:** none known. The authors propose that allele severity sets the phenotype (see §4).

---

## 3. Phenotypes

The cohort is eight affected individuals from four EXOC7 families: two infants, one child, two terminated fetuses and three siblings.

| Phenotype | Frequency (EXOC7 cases) | Onset / course | Candidate HPO (verify) |
|---|---|---|---|
| Seizures | 6/6 liveborn (Families I, II, IV); myoclonic in Family I | Neonatal (severe) to childhood (mild) | HP:0001250 Seizure; HP:0002123 Generalized myoclonic seizure |
| Global developmental delay or intellectual disability | All liveborn survivors evaluated (II, IV) | Infancy, static or progressive | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability |
| Cerebral atrophy (central and cortical, temporal-predominant in II-04) | Families I and II, 2/3 in IV | Progressive (implied by "atrophy") | HP:0002059 Cerebral atrophy |
| Microcephaly | Family I (congenital, −2.7 SD), II (−2.6 SD), III (fetal, mild) | Congenital or prenatal | HP:0000252 Microcephaly; HP:0011451 Primary microcephaly |
| Simplified gyral pattern and thin cortex | Family I | Congenital | HP:0009879 Simplified gyral pattern |
| Ventriculomegaly | Family I | Congenital | HP:0002119 Ventriculomegaly |
| Reduced cerebral white matter | Family I | — | HP:0002060 is *Abnormal cerebral morphology*, which is too broad; search for a "reduced cerebral white matter volume" term |
| Cerebellar hypoplasia and small brainstem | Family I; Family III (fetal autopsy) | Prenatal | HP:0001321 Cerebellar hypoplasia; HP:0002365 Hypoplasia of the brainstem |
| Arthrogryposis multiplex congenita | Family I | Congenital | HP:0002804 Arthrogryposis multiplex congenita |
| Death in infancy | Family I (both died within months) | Infancy | HP:0001522 Death in infancy |

**Not reported:** hypotonia or spasticity, dysmorphic features, systemic, renal or ocular involvement, and laboratory abnormalities. The paper gives no detailed seizure semiology, EEG findings or quality-of-life data.

---

## 4. Genetic and molecular information

**Gene:** EXOC7, chromosome 17q25.1. HGNC ID: look it up; it is not in `cache/hgnc/terms.csv`. The protein is Exo70.

| Family | Variant (hg19) | Type | Zygosity | gnomAD | Functional data |
|---|---|---|---|---|---|
| I (consanguineous, 2 affected) | c.809-2A>G, intron 6 / exon 7 acceptor (NC_000017.10:g.74087318T>C) | Splice acceptor | Homozygous | 2/251,414, heterozygous only | Minigene: loss of the normal exon 6–7–9 transcript and two out-of-frame isoforms (stops near aa 286 and 290). HAP1 knock-in: about 50% reduction of the long isoform (p=0.045). |
| II (consanguineous, 1) | p.Ser48del (g.74097928_74097930del), exon 3 | In-frame deletion | Homozygous | 2/276,426 | None. Lies in the N-terminal region that binds EXOC8 and the WAVE regulatory complex. |
| III (non-consanguineous, 2 fetuses) | c.809-2A>G + c.1212_1226del (NM_001145297.2), exon 10, removes 5 aa | Splice + in-frame deletion | Compound heterozygous | Deletion absent | Only the splice allele was tested. |
| IV (consanguineous, 3) | p.Ala523Thr (g.74081807C>T), exon 15 | Missense | Homozygous | 2/277,066 | None. LOD 2.9. |

**Discrepancy to resolve.** The Halim et al. 2023 review (PMID:37085629) writes the Family III splice allele as **c.808-2A>G**, while Coulter writes **c.809-2A>G** for both families. Check against the primary paper's supplementary table and ClinVar before encoding.

**Mechanism class.** Every allele is hypomorphic. The authors propose a severity ranking: splice > 5-aa deletion > 1-aa deletion > missense. That ranking rests on clinical correlation and functional testing of one allele only. The zebrafish and mouse data (§15) suggest complete loss of EXOC7 is lethal, which fits a disease of hypomorphs. In dismech terms: `functional_impact_category: PARTIAL_LOSS_OF_FUNCTION`, `variant_origin: GERMLINE`, `zygosity` homozygous or compound heterozygous.

**Other genetic information:**
- *Co-segregating variants judged non-causal:* CYB5D2 p.Arg136Trp (Family I).
- *Modifiers, epigenetics, chromosomal:* none reported for this disease. 17q25.3 copy-number changes (PMID:37430334) are a different locus and should not be linked.
- *Somatic origin:* not applicable.
- *Curation status:* ClinGen gene-disease validity was not located. PanelApp Australia rates EXOC7 Green for microcephaly ([PanelApp](https://panelapp-aus.org/panels/138/gene/EXOC7/)). That is a panel rating, not a GenCC tier, so do not put it in `gene_disease_validity`.

---

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious factors are reported.

---

## 6. Mechanism and pathophysiology

**Causal chain** (I mark where each step is demonstrated or inferred):

1. **Biallelic hypomorphic EXOC7 variants** lead to reduced amount or function of Exo70.
   - *Demonstrated* for c.809-2A>G: aberrant splicing in a minigene assay and about 50% less protein in HAP1 cells.
   - *Inferred* for Ser48del, the 5-aa deletion and Ala523Thr.
2. **Reduced Exo70 impairs exocyst assembly and function**, meaning vesicle tethering and polarized exocytosis at the plasma membrane.
   - *Inferred* from Exo70's known role; this was not measured in patient cells.
   - For Ser48del, disruption of EXOC8 or WAVE-complex binding is *hypothesized*.
3. **Impaired exocyst function in neural progenitors** (ventricular-zone radial glia and outer-SVZ TBR2+ intermediate progenitors) leads to a smaller progenitor pool and apoptosis.
   - *Demonstrated in zebrafish:* a 53% drop in Sox2+ telencephalic progenitors and about 3× more TUNEL+ cells.
   - Human relevance is supported only by expression: EXOC7 is expressed in fetal VZ and oSVZ at levels similar to ASPM.
   - **Branch, ruled out:** no abnormal mitoses were seen in zebrafish, so a cytokinesis failure is not supported.
4. **Fewer progenitors and more cell death** lead to **microcephaly** and a simplified, thin cortex in the severe alleles. *Demonstrated in zebrafish:* the null has a smaller head and smaller eyes.
5. **Impaired exocyst function in post-mitotic cortical neurons** reduces neuronal survival and membrane addition, which drives **progressive cortical atrophy**.
   - *Inferred.* The authors read the atrophy as neurodegeneration.
   - EXOC7 exon 7 is preferentially included in cortical-plate transcripts (about 93% vs 47% in the VZ at GW15), which points to a neuron-specific isoform.
   - **Branch:** Exo70 knockdown in rat hippocampal neurons reduces dendritic arborization, synapse density and spine maturation (Lira et al. 2019, PMID:30374940, IN_VITRO). This suggests a synaptic or dendritic route to **seizures** and **intellectual disability**, but it is *inferred* and has not been shown in the disease.
6. **Cortical loss and abnormal connectivity** lead to **seizures, developmental delay or intellectual disability**, and in severe cases **death in infancy**.
7. **Possible branch (unconfirmed): primary cilia.** The exocyst is involved in ciliogenesis, and the zebrafish had some ciliopathy-like signs (small eyes, edema). The authors state cilia involvement needs further study. Treat it as a knowledge gap.

**Ontology leads for the pathograph** (all to verify):

| Kind | Candidate terms |
|---|---|
| GO biological process | exocytosis (GO:0006887); vesicle tethering involved in exocytosis (GO:0090522); cerebral cortex development (GO:0021987); neural precursor cell proliferation (GO:0061351); neuron apoptotic process (GO:0051402); dendrite morphogenesis (GO:0048813) |
| GO cellular component | exocyst (GO:0000145) |
| Cell types (CL) | radial glial cell (CL:0000681); neural progenitor cell (CL:0011020); cerebral cortex neuron (CL:0010012); intermediate progenitor (check for a "neuronal intermediate progenitor cell" term) |
| `biological_scale` | Steps 1–2 MOLECULAR, step 3 CELLULAR, steps 4–5 TISSUE, step 6 ORGANISM |

**Not available:** omics profiling, single-cell or spatial data, and CRISPR screens for this disease.

---

## 7. Anatomical structures

- **Organs:** brain (UBERON:0000955), mainly the cerebral cortex (UBERON:0000956), plus the cerebellum (UBERON:0002037), brainstem (UBERON:0002298) and cerebral white matter.
- **Secondary:** joints (arthrogryposis in Family I, presumably neurogenic) and eyes (small eyes in zebrafish only).
- **Developmental compartments:** ventricular zone and outer subventricular zone of the fetal cortex, and the cortical plate.
- **Subcellular:** exocyst complex at the plasma membrane.
- **Laterality:** bilateral and diffuse. One patient (II-04) had temporal-lobe-predominant atrophy.

---

## 8. Temporal development

- **Onset:** prenatal in severe cases (fetal microcephaly and cerebellar hypoplasia seen in Family III), neonatal (seizures and microcephaly in Family I), or childhood (Families II and IV).
- **Course:** neurodevelopmental, with progressive atrophy. Natural-history data are not available.
- **Critical period:** fetal corticogenesis, when progenitor proliferation and survival are at stake.
- **Remission:** none reported.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). Penetrance appears complete in the reported sibships. Expressivity is variable and correlates with the allele.
- **Consanguinity:** present in Families I, II and IV.
- **Recurrent allele:** c.809-2A>G occurs in two unrelated families (I and III). The paper does not analyze a founder haplotype; ancestry is not stated in my extraction.
- **Carrier frequency:** each allele is ≤2 heterozygotes in about 250,000–277,000 gnomAD alleles.
- **Prevalence:** unknown. Use `measure_type: CASES_IN_LITERATURE` with "8 individuals from 4 families (Coulter 2020)" and `prevalence_class: NOT_YET_DOCUMENTED` or `ULTRA_RARE`.
- **Sex ratio:** no bias evident (affected males and females).

---

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing, as in the discovery cohort. Use homozygosity mapping in consanguineous families. EXOC7 is on PanelApp Australia's microcephaly panel. CMA, karyotype, FISH, mtDNA and repeat-expansion testing are not relevant beyond excluding other diagnoses.
- **Variant interpretation:** RNA studies are useful for splice alleles. A minigene assay was decisive for c.809-2A>G.
- **Imaging:** brain MRI showing atrophy, microcephaly with simplified gyri, ventriculomegaly, and cerebellar or brainstem hypoplasia. Prenatal ultrasound or fetal autopsy can detect severe cases (Family III).
- **EEG:** recommended by default for seizures. No disease-specific EEG pattern has been reported.
- **Biomarkers or laboratory tests:** none.
- **Differential diagnosis:**
  - other exocyst disorders: EXOC8 (NEDMISBA, #619076); EXOC2 (#619306, with dysmorphism and spasticity); EXOC6B (skeletal dysplasia ± intellectual disability); EXOC4 and EXOC3L2 (Meckel–Gruber-like)
  - primary microcephalies (MCPH)
  - pontocerebellar hypoplasias
  - developmental and epileptic encephalopathies
- **Screening:** no newborn screening. Carrier and prenatal or preimplantation testing are possible once the familial variants are known.

---

## 11. Outcome and prognosis

- **Severe alleles (splice):** death within the first months of life (Family I), or pregnancy termination after prenatal diagnosis (Family III).
- **Milder alleles (missense, single-residue deletion):** survival into childhood with intellectual disability and seizures.
- **No data:** survival statistics, quality-of-life studies, or validated prognostic factors. The genotype–severity ranking is the only proposed predictor.

---

## 12. Treatment

There is no disease-specific therapy and no clinical trials. Management is symptomatic.

| Intervention | NCIT lead (verify) | Notes |
|---|---|---|
| Antiseizure medication | Pharmacotherapy NCIT:C15986 | No drug-specific evidence. Leave `therapeutic_agent` unbound unless a source names an agent. |
| Physical, occupational and speech therapy | NCIT:C15302 / C121351 / C159273 | Generic supportive care |
| Genetic counseling | NCIT:C15240 | 25% recurrence risk |
| Supportive and palliative care | NCIT:C15747 | For the severe neonatal form |

**Not applicable:** pharmacogenomics, gene therapy, ASOs and other advanced therapies.

---

## 13. Prevention

- **Primary prevention:** carrier testing in consanguineous families, and prenatal or preimplantation genetic diagnosis once the familial variants are known (Family III shows prenatal detection is feasible).
- **Tertiary prevention:** seizure control.
- **Not applicable:** vaccination and public-health measures.

---

## 14. Other species

No naturally occurring disease is known; I found no OMIA entry. The gene is conserved:
- zebrafish *exoc7* ([ZFIN ZDB-GENE-040426-2752](https://franklin.zfin.org/ZDB-GENE-040426-2752))
- mouse *Exoc7*
- yeast *EXO70*
- plants: *EXO70* paralog family

---

## 15. Model organisms

| Model | Allele | Phenotype | Fidelity | Source |
|---|---|---|---|---|
| **Zebrafish (*Danio rerio*)** | *exoc7* mh111: 1-bp frameshift in exon 5, truncation at about aa 185, presumed null (CRISPR) | Small eyes (−26% eye area), head edema, smaller head (−4%, p=6.8×10⁻⁵), body length normal, death after 5 dpf. Telencephalon: about 3× more apoptosis (p=0.0023), 53% fewer Sox2+ progenitors. Retina: 76% fewer Sox2+ cells. No abnormal mitoses. | PARTIALLY_RECAPITULATES microcephaly and progenitor loss | Coulter 2020, MODEL_ORGANISM |
| **Mouse *Exoc7* knockout** | Lexicon | Homozygous lethal | Personal communication cited in the paper, not citable as evidence | — |
| **Rat hippocampal neurons** | Lentiviral Exo70 knockdown or overexpression | Knockdown reduces dendritic arbors, synapses and spine density; overexpression increases them | IN_VITRO, supports the synaptic branch | PMID:30374940 |
| **HAP1 cells** | c.809-2A>G knock-in | About 50% less EXOC7 | IN_VITRO | Coulter 2020 |

**Limitations to record as typed divergences:**
- the zebrafish is a *null*, while the patients carry *hypomorphic* alleles (POPULATION_MISMATCH or proxy-allele caveat)
- zebrafish lack a gyrencephalic cortex and oSVZ outer radial glia (SPECIES_MISMATCH, BOUNDARY_OMISSION)
- seizures and progressive atrophy were not assessed (BOUNDARY_OMISSION)

**Candidate `HUMAN_MODEL_MISMATCH` discussion:** no mammalian hypomorph or patient-derived cortical organoid has been reported.

---

## Notes for curating the dismech entry

1. **Evidence:** PMID:32103185 is the only primary disease reference. Fetch it with `just fetch-reference PMID:32103185` and copy exact snippets from the cached abstract. The fragments quoted above, such as "four independent partial loss-of-function (LOF) variants in a recessively inherited disorder" and "the absence of exoc7 causes microcephaly", must be checked against the cache.
2. **Supporting references:**
   - PMID:37085629 (review): tag `quote_role: REVIEW_SYNTHESIS`.
   - PMID:30374940 (Exo70 in neurons): IN_VITRO, mechanism only.
   - PMID:35460391 (EXOC8): differential diagnosis only.
3. **Gaps to record as knowledge gaps:** cilia involvement; functional data for three of the four alleles; natural history and seizure semiology; and whether the splice-variant numbering is c.808 or c.809.
4. **GeneReviews:** no chapter was located. Run `just check-genereviews` to confirm.

---

## Sources

- Coulter ME et al. Regulation of human cerebral cortical development by EXOC7 and EXOC8, components of the exocyst complex, and roles in neural progenitor cell proliferation and survival. *Genet Med* 2020. PMID:32103185; [PMC7272323](https://pmc.ncbi.nlm.nih.gov/articles/PMC7272323)
- Halim DO, Munson M, Gao FB. The exocyst complex in neurological disorders. *Hum Genet* 2023. PMID:37085629; PMC10449956
- Ullah A et al. A novel nonsense variant in EXOC8 underlies a neurodevelopmental disorder. *Neurogenetics* 2022. PMID:35460391
- Lira M et al. The exocyst component Exo70 modulates dendrite arbor formation, synapse density, and spine maturation in primary hippocampal neurons. *Mol Neurobiol* 2019. PMID:30374940
- [LOVD disease #06947 (NEDSEBA, OMIM:619072)](https://databases.lovd.nl/shared/diseases/06947)
- [NCBI MedGen 1748227](https://www.ncbi.nlm.nih.gov/medgen/1748227)
- [PanelApp Australia: EXOC7, microcephaly panel](https://panelapp-aus.org/panels/138/gene/EXOC7/)
- [ZFIN *exoc7*](https://franklin.zfin.org/ZDB-GENE-040426-2752)
- [DrugMap disease DISAL3A7](https://drugmap.idrblab.net/data/disease/details/DISAL3A7) (MONDO–OMIM cross-reference)
- [GeneCards EXOC7](https://www.genecards.org/card/EXOC7)
- Europe PMC REST API (search and full text) and NCBI E-utilities esearch, accessed 2026-10-15

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0033658` (1 mention) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with seizures and brain atrophy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0090522` (obsolete vesicle tethering involved in exocytosis) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000955` (1 mention) - the report calls it "Organs:** brain"; UBERON calls it **brain**
- `NCIT:C15747` (1 mention) - the report calls it "Supportive and palliative care"; NCIT calls it **Supportive Care**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.