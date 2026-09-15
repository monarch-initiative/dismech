---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T22:53:45.125916'
end_time: '2026-09-07T22:57:30.354438'
duration_seconds: 225.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: COA5-Related Fatal Infantile Cardioencephalomyopathy
  mondo_id: MONDO:0014667
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 10
  num_turns: 19
  total_cost_usd: 1.0607685999999998
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 23
  verified: 20
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.048
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014667
    reported_labels:
    - corresponds to MC4DN9
    ontology_label: cardioencephalomyopathy, fatal infantile, due to cytochrome c
      oxidase deficiency 3
  unresolved_terms:
  - HP:0005633
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COA5-Related Fatal Infantile Cardioencephalomyopathy
- **MONDO ID:** MONDO:0014667 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COA5-Related Fatal Infantile Cardioencephalomyopathy** covering all of the
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

I have enough primary-source material now to compile a thorough, well-cited report. Let me do a couple more targeted searches to fill gaps (HPO/phenotype terms, MGI knockout phenotype details, UniProt).

# Research Report: COA5-Related Fatal Infantile Cardioencephalomyopathy

*(Mitochondrial Complex IV Deficiency, Nuclear Type 9 / MC4DN9 / CEMCOX3)*

## 1. Disease Information

**Overview.** An autosomal recessive, neonatal/early-infantile mitochondrial disorder caused by biallelic loss-of-function variants in **COA5** (Cytochrome c Oxidase Assembly Factor 5, formerly *C2orf64*), which encodes a small CHCH-domain protein required for an early step of respiratory chain Complex IV (cytochrome *c* oxidase, COX) assembly. Disease is defined by isolated Complex IV deficiency producing rapidly fatal hypertrophic cardiomyopathy with lactic acidosis in the neonatal period; the "cardioencephalomyopathy" nosology reflects the broader OMIM disease-class naming convention for this group of nuclear COX-assembly disorders rather than a documented, prominent primary CNS lesion in the reported cases (see §3, §7).

**Key identifiers:**
- **OMIM gene:** *613920 — COA5* (Huigsloot et al. 2011)
- **OMIM phenotype:** #616500 — Mitochondrial Complex IV Deficiency, Nuclear Type 9 (MC4DN9); also referenced in the literature as CEMCOX3 (Cardioencephalomyopathy, Fatal Infantile, due to Cytochrome c Oxidase Deficiency 3) ([omim.org/entry/616500](https://omim.org/entry/616500))
- **MONDO:** MONDO:0014667 (corresponds to MC4DN9)
- **Gene location:** 2q11.2; NCBI Gene ID 493753; RefSeq NM_001008215.3; also historically NCOA5-adjacent nomenclature confusion should be avoided — **COA5 ≠ NCOA5** (nuclear receptor coactivator 5), a distinct, unrelated gene that surfaces in naive searches
- **Orphanet:** ORPHA:1561 — Fatal infantile cytochrome C oxidase deficiency (the broader COX-deficiency umbrella term Orphanet uses; COA5 is one of several causal genes grouped here) ([orpha.net/en/disease/detail/1561](https://www.orpha.net/en/disease/detail/1561))
- **Yeast ortholog:** PET191

**Synonyms:** Cytochrome c oxidase assembly factor 5 deficiency; C2ORF64-related mitochondrial disease; MC4DN9; CEMCOX3.

**Evidence base.** This is an extremely narrowly-documented Mendelian entity: the primary clinical source is a single index report of **one consanguineous Turkish family (2 affected sibs)** (Huigsloot et al. 2011, PMID:21457908), corroborated by **one additional, unrelated family carrying the identical variant**, reported in a 2024–2025 mechanistic follow-up (Stroud lab / Life Science Alliance, PMID:39779219). All published human genotype-phenotype data currently trace to these two families and the single recurrent variant p.Ala53Pro — this is aggregated disease-level literature (case reports), not an EHR/registry-derived dataset.

Sources: [OMIM #616500](https://omim.org/entry/616500) · [OMIM *613920](https://omim.org/entry/613920) · [Orphanet ORPHA:1561](https://www.orpha.net/en/disease/detail/1561) · [NCBI Gene 493753](https://www.ncbi.nlm.nih.gov/gene/493753)

---

## 2. Etiology

**Disease causal factor:** Purely monogenic/genetic — biallelic (homozygous, in both reported families) pathogenic variants in **COA5** (hgnc gene; lowercase-`hgnc:` CURIE per local convention would be `hgnc:24704`, ENSG00000183513). No environmental, infectious, or multifactorial contribution has been reported or is biologically plausible for this class of nuclear mitochondrial assembly-factor disorder.

**Genetic risk factor / founder variant:** The **only variant reported in humans to date** is c.157G>C (p.Ala53Pro, NM_001008215.3), identified in homozygosity in **both** unrelated reported families, both of **Turkish ethnicity** — strongly suggestive of a Turkish founder allele, though a formal haplotype/founder-effect study has not been published (this is an inference from the recurrence pattern, not an established finding). PMID:21457908 originally identified the variant in a consanguineous Turkish pedigree; the second, independently ascertained Turkish family carrying the same allele was reported in the 2024/2025 functional-mechanism paper (PMID:39779219), which itself functions as a form of independent case confirmation.

- Population allele frequency: gnomAD frequency data specific to c.157G>C were not retrieved in this search pass; given its apparent restriction to Turkish founder chromosomes and the ultra-rare disease phenotype, expect it to be present at very low frequency or absent from gnomAD's predominantly non-Turkish-enriched reference panels — **this should be confirmed directly in gnomAD before KB entry**, as it was not independently verified here.
- **No modifier genes, susceptibility loci, or protective variants have been reported** for this disorder — there is no literature to draw on for §2's "Protective Factors" or "Gene-Environment Interactions" subsections; state this as a genuine gap rather than inferring an absence.

**Consanguinity:** Explicitly documented in the index family ("consanguineous Turkish parents," PMID:21457908), consistent with autosomal recessive transmission of a rare founder allele.

Sources: [OMIM *613920](https://omim.org/entry/613920) · Huigsloot et al. 2011, PMID:21457908 · PMC11711468/PMID:39779219

---

## 3. Phenotypes

Phenotype data derive entirely from the two reported Turkish families (Huigsloot 2011 index sibs, died at 8 and 10 days of age per the OMIM/NORD abstraction, though one search summary reported "3 months" — **this discrepancy should be resolved against the primary PMID:21457908 full text before curation**, since GARD/OMIM abstractions and AI-search summaries of the same paper conflicted on exact age at death).

| Phenotype | Type | Onset | Notes / suggested HP term |
|---|---|---|---|
| Hypertrophic cardiomyopathy (biventricular, septal hypertrophy, non-compaction appearance) | Clinical sign | Neonatal | **HP:0001639** (Hypertrophic cardiomyopathy); consider **HP:0005633** (Ventricular septal hypertrophy) and **HP:0000006** context terms as applicable |
| Elevated blood lactate (2.5–11 mmol/L reported range) | Laboratory abnormality | Neonatal | **HP:0002151** (Increased serum lactate) |
| Elevated urinary lactate | Laboratory abnormality | Neonatal | Consider **HP:0003128** (Lactic acidosis) at the systemic level |
| Elevated urinary ethylmalonic acid | Laboratory abnormality | Neonatal | Organic aciduria pattern consistent with respiratory chain dysfunction; no dedicated HP term confirmed in this pass |
| Respiratory distress / respiratory insufficiency requiring intubation | Clinical sign | Neonatal | **HP:0002093** (Respiratory insufficiency) |
| Hypotonia | Clinical sign | Neonatal (per NORD/GTR abstraction) | **HP:0001252** (Hypotonia) |
| Abnormal liver function tests | Laboratory abnormality | Neonatal | **HP:0001410** (Decreased liver function) or specific transaminase terms |
| Isolated Complex IV (COX) enzymatic deficiency in fibroblasts and heart muscle | Laboratory/biochemical | — | **HP:0011927** (Reduced cytochrome C oxidase activity) — verify exact HP CURIE before binding |
| Death in infancy | Outcome | 8–10 days to ~3 months (source-discrepant, see above) | Fatal course; **HP:0031307** or comparable "sudden death"/"fatal in infancy" outcome framing |

**Severity/progression:** Uniformly severe and rapidly fatal in both reported families; no surviving patients, no reported milder allelic series, and therefore **no data exist on variable severity, later-onset presentations, or long-term natural history** — unlike many other MC4DN subtypes (e.g., *SURF1*-Leigh syndrome), which have a phenotypic spectrum, COA5-disease as currently documented is a single, severe, lethal-in-infancy phenotype defined by n=2 families.

**CNS/encephalopathy phenotype specifically:** The disease-class name ("cardioencephalomyopathy") implies CNS involvement, but the retrieved abstracts and summaries emphasize the **cardiac and biochemical** phenotype far more than a distinct, well-characterized encephalopathic phenotype (e.g., no MRI/neuroimaging findings, no seizure phenotype, and no dedicated neurological exam findings were surfaced in this search). **This is a gap that should be resolved by reading the PMID:21457908 full text directly** — the CNS component of the phenotype may be present in the primary paper but was not captured by the search summaries used here, or the "cardioencephalomyopathy" label may be inherited from the broader disease-class nomenclature (OMIM's naming convention for this class of COX-deficiency disorders) rather than from a specific encephalopathy documented in these two families. Flag this explicitly rather than asserting a CNS phenotype without primary-source confirmation.

**Quality of life impact:** Not applicable/not reported — given uniform neonatal/early-infantile lethality, no QOL instrument data (EQ-5D, SF-36) exist or would be expected.

Sources: PMID:21457908 (Huigsloot et al. 2011, *Am J Hum Genet* 88:488–493) · [NORD/MONDO abstraction](https://rarediseases.org/mondo-disease/cardioencephalomyopathy-fatal-infantile-due-to-cytochrome-c-oxidase-deficiency-3/) · [GTR test record](https://www.ncbi.nlm.nih.gov/gtr/tests/586086/) · PMID:39779219

---

## 4. Genetic/Molecular Information

**Causal gene:** COA5 (OMIM *613920; NCBI Gene 493753; chr2q11.2; NM_001008215.3). Historical alias: *C2orf64*.

**Reported pathogenic variant:**
- **c.157G>C, p.(Ala53Pro)** — the sole variant reported in humans across both families.
- **Variant type:** Missense, homozygous (biallelic) in both reported pedigrees.
- **ACMG classification:** Not independently retrieved from ClinVar in this pass — should be pulled directly from ClinVar before KB curation, but functional data (below) strongly support a damaging/loss-of-function-type mechanism.
- **Location:** Falls within a conserved motif of the COA5/PET191 protein predicted to be important for protein folding/structure (per PMID:21457908's original functional characterization).
- **Population frequency:** Not independently confirmed here (see §2) — recommend a direct gnomAD/ClinVar pull.
- **Origin:** Germline (both reported cases), consistent with autosomal recessive constitutional disease; not a somatic/cancer-associated gene.

**Protein and functional consequence:**
- COA5 is a small mitochondrial intermembrane-space protein containing a **CHCH domain with twin CX9C motifs** — a structural class that depends on the MIA40/CHCHD4 disulfide-relay import pathway for mitochondrial localization (general class-level inference; not explicitly confirmed for COA5 in the sources retrieved here, so should be flagged as inferred-from-domain-architecture rather than COA5-specific experimental confirmation).
- Ortholog of **yeast Pet191**, a subunit of an oligomeric inner-membrane-associated complex required for COX assembly; early yeast Pet191 studies suggested a role in COX assembly without direct impact on mitochondrial translation or copper metalation of COX subunits.
- **Functional impact category:** Best characterized as **loss-of-function / partial loss-of-function** — p.Ala53Pro patient fibroblasts show:
  - Isolated Complex IV enzymatic deficiency (both fibroblasts and patient heart muscle)
  - Accumulation of Complex IV assembly **intermediates/subcomplexes** rather than mature holocomplex
  - Subcomplexes lacking COX1 (MT-CO1), COX2 (MT-CO2), COX4 (COX4I1), and COX5A subunits (PMID:21457908)
  - The 2024/2025 mechanistic paper (PMID:39779219) refined this: complexome profiling in a **CRISPR/Cas9 COA5-knockout U2OS cell line** (7-bp frameshift deletion) showed COA5 acts specifically **between MT-CO1 maturation and the incorporation of MT-CO2** into the earliest CIV assembly intermediate — i.e., COA5 loss blocks a discrete, early step, with accumulation of MT-CO1-containing subcomplexes (100–300 kDa) that cannot progress to a functional holocomplex.
- **No modifier genes** have been reported.
- **No epigenetic data** (methylation, histone modification) have been reported for this gene/disease — genuine gap, not to be inferred.
- **No chromosomal-abnormality (CNV, translocation, aneuploidy) mechanism** has been reported; disease is driven by a point missense variant only.

Suggested ontology bindings: **hgnc** gene term for COA5 (verify exact HGNC ID before binding — do not guess the numeric CURIE without an OAK/HGNC lookup); **GO:0033617** (mitochondrial respiratory chain complex IV assembly) as the key biological-process term; molecular function terms around CHCH-domain/protein-folding chaperone activity should be verified against UniProt/GO rather than asserted from this search pass.

Sources: PMID:21457908 · PMID:39779219 (PMC11711468) · [OMIM *613920](https://omim.org/entry/613920) · [NCBI Gene 493753](https://www.ncbi.nlm.nih.gov/gene/493753)

---

## 5. Environmental Information

**No environmental, lifestyle, or infectious causal/risk factors have been reported** for this disorder, consistent with its status as a fully penetrant, biallelic monogenic mitochondrial assembly-factor disease presenting at birth/neonatally. This is a genuine "not applicable" rather than an unresearched gap — nuclear-encoded COX-assembly-factor disorders of this class are not known to have environmental modifiers of onset or severity in the pediatric mitochondrial disease literature generally, though a disease-specific search for gene-environment interaction data specific to COA5 returned nothing to cite.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from molecular lesion to clinical phenotype):**

1. Biallelic **COA5 c.157G>C (p.Ala53Pro)** variant → destabilizes a conserved motif of the COA5/PET191-family CHCH-domain protein, impairing its folding/structural integrity (PMID:21457908; mechanism of destabilization is inferred from conservation and structural prediction in the original paper, not from a solved crystal structure).
2. Loss of functional COA5 protein → **arrest of Complex IV (cytochrome c oxidase) assembly at an early, discrete step** — specifically between maturation of the mitochondrially-encoded COX1 (MT-CO1) subunit and its combination with COX2 (MT-CO2) to form the earliest CIV assembly intermediate (PMID:39779219, complexome profiling in the COA5-knockout cellular model). This step is **directly demonstrated** in the CRISPR-knockout cell system; its equivalence to the patient p.A53P mechanism is supported by concordant biochemical findings in patient fibroblasts (accumulating the same class of subcomplexes) but the knockout and missense mechanisms are not proven identical at the structural level — this is a reasonable inference, not a demonstrated one-to-one mechanistic match.
3. Failure to progress past this intermediate → **accumulation of stalled MT-CO1-containing subcomplexes (~100–300 kDa)** that cannot mature into the CIV holocomplex; these appear to be routed toward a **prohibitin-complex-associated pathway**, consistent with a degradative/quality-control fate for unassembled respiratory-chain subunits (PMID:39779219 — described as "colocalisation with prohibitin complexes," suggestive of degradation but not directly proven to be degradation via a specific proteolytic mechanism in the retrieved summary).
4. Net loss of mature Complex IV holocomplex → **markedly reduced Complex IV enzymatic activity and abundance**, while Complexes I, II, III, and V remain relatively unaffected (isolated CIV deficiency) — directly demonstrated in both patient fibroblasts/heart muscle (PMID:21457908) and the knockout cell model (PMID:39779219).
5. Loss of CIV activity → **secondary loss of respiratory supercomplex assembly**, specifically **loss of the III₂+IV supercomplex** and a compensatory increase in the CI+III₂ "S0" supercomplex (PMID:39779219) — this represents a downstream structural reorganization of the respiratory chain rather than a separate causal branch.
6. Combined loss of CIV activity and supercomplex disruption → **impaired oxidative phosphorylation capacity**, particularly in high-energy-demand tissues (cardiac and skeletal muscle, and — per the disease-class "cardioencephalomyopathy" designation — potentially CNS, though the CNS mechanistic link is not directly documented in the sources retrieved here; flag as an assumed-by-nosology rather than demonstrated link) → **compensatory anaerobic glycolysis**, producing the observed **lactic acidosis** (elevated blood and urinary lactate) and **elevated urinary ethylmalonic acid** (a marker of disrupted mitochondrial fatty-acid/energy metabolism).
7. Chronic energy failure in cardiomyocytes → **hypertrophic cardiomyopathy** with septal hypertrophy and non-compaction features, the dominant clinical phenotype in both reported families.
8. Combined cardiac pump failure, respiratory insufficiency (from concurrent skeletal/respiratory muscle energy failure and possible CNS respiratory drive involvement — again, the CNS component is asserted by disease-class nomenclature more than by a directly cited mechanistic finding in this search pass), and multisystem metabolic decompensation → **death in early infancy**.

**Molecular pathway:** Mitochondrial respiratory chain Complex IV (cytochrome c oxidase) biogenesis pathway; **GO:0033617** (mitochondrial respiratory chain complex IV assembly) is the key suggested GO term. No involvement of canonical signaling cascades (Wnt/MAPK/mTOR/PI3K-AKT) — this is a structural/metabolic assembly-factor disorder, not a signaling disorder.

**Cellular process:** Impaired oxidative phosphorylation; compensatory glycolytic shift; likely proteostatic/degradative handling of stalled assembly intermediates via prohibitin-associated pathways (PMID:39779219).

**Protein dysfunction:** Loss-of-function/misfolding of a small CHCH-domain chaperone-like assembly factor (COA5), leading to failure of a specific protein-protein assembly step (MT-CO1 + MT-CO2 incorporation) rather than a defect in COX catalytic chemistry itself.

**Tissue damage mechanism:** Energy-failure-driven cardiomyocyte dysfunction/hypertrophy; no evidence retrieved here for oxidative-stress, fibrotic, or necrotic mechanisms specifically documented in COA5 disease (though these are plausible extrapolations from mitochondrial cardiomyopathy biology generally — do not assert them as COA5-specific findings).

**Cell types/anatomical involvement (see also §7):** Cardiomyocytes (primary, best-documented); skeletal muscle/fibroblasts (biochemically characterized, PMID:21457908); U2OS (human osteosarcoma) cell line used as the mechanistic knockout model (PMID:39779219) — note this is an experimental/heterologous cell model, not a disease-relevant tissue, and should be labeled accordingly in any `experimental_models` entry.

**Omics/advanced technologies:** **Complexome profiling** (a specialized proteomic/native-PAGE-based technique resolving native protein complex composition across a molecular-weight gradient) was the key advanced technology used in PMID:39779219 to map the precise assembly stage at which COA5 acts. No transcriptomic (RNA-seq/GEO), standard proteomic (PRIDE), metabolomic, lipidomic, single-cell, or spatial transcriptomic datasets specific to COA5 disease were identified in this search — a genuine gap, not to be inferred as absent from all databases without a direct GEO/PRIDE query.

Suggested GO terms: **GO:0033617** (mitochondrial respiratory chain complex IV assembly). Suggested CL terms: **CL:0000746** (cardiac muscle cell) for the primary affected cell type; **CL:0000057** (fibroblast) for the biochemically characterized cell type.

Sources: PMID:21457908 · PMID:39779219 (Life Science Alliance / PMC11711468)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart (hypertrophic cardiomyopathy — the dominant, best-documented organ manifestation in both families)
- **Secondary/systemic:** Liver (abnormal LFTs reported); respiratory system (respiratory insufficiency, though this may be secondary to cardiac failure and/or generalized hypotonia/muscle weakness rather than a distinct primary respiratory-organ lesion)
- **Body systems:** Cardiovascular (primary); metabolic/endocrine (lactic acidosis, organic aciduria); neuromuscular (hypotonia); the "encephalo-" component of the disease-class name implies CNS involvement, but a specific CNS lesion (imaging finding, defined encephalopathy phenotype) was **not** identified in the sources retrieved in this pass and should be confirmed from the PMID:21457908 full text before being curated as a distinct phenotype/organ node.

**Tissue and cell level:** Cardiac muscle tissue (myocardium — septal hypertrophy, non-compaction pattern) is the most specifically documented; skeletal muscle biopsy tissue was studied in at least the second reported family (per the 2024/2025 paper's mention of "skeletal muscle biopsies"); dermal fibroblasts were the primary cultured cell type used for biochemical/functional characterization in both the original and follow-up studies.

**Subcellular level:** **Mitochondrial inner membrane / intermembrane space** — COA5 is an intermembrane-space CHCH-domain protein associated with the assembly machinery on the matrix side of the inner membrane where nascent Complex IV subcomplexes form. Suggested GO Cellular Component term: **GO:0005758** (mitochondrial intermembrane space) — verify against UniProt subcellular-location annotation before binding, as the exact sub-compartment (inner membrane vs. IMS-soluble vs. IMS-membrane-associated) was not confirmed to UniProt-level precision in this search pass.

**Localization/laterality:** Not applicable — this is a systemic/biventricular process (biventricular hypertrophic cardiomyopathy reported), not a lateralized or focal anatomical process.

Suggested UBERON terms: **UBERON:0000948** (heart); **UBERON:0002349** (myocardium); **UBERON:0001133** (cardiac ventricle) for biventricular involvement — verify specificity against the primary source before binding.

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal — both reported families presented at birth or within the first days of life (hypotonia and respiratory insufficiency at birth per one abstraction; cardiomyopathy identified in the neonatal period in both families).
- **Onset pattern:** Acute-to-subacute, rapidly progressive.
- **Disease course:** Uniformly progressive to death — **no stable, relapsing-remitting, or spontaneously-improving course has been documented**. This is a monophasic, rapidly fatal natural history as currently reported.
- **Duration/outcome:** Death reported at **8 and 10 days of age** in the index sibs per the OMIM/NORD-derived abstraction; one search-tool summary of the same paper stated "fatal outcome at 3 months of age" — **this is a direct conflict in secondary sources that must be resolved against the PMID:21457908 primary text before any age-at-death value is entered into the KB.** Do not average or guess between these two conflicting figures.
- **Stages:** No formal staging system exists for this ultra-rare, uniformly fatal infantile disorder.
- **Critical periods:** The entire disease course occurs within a critical early-infantile window; no data exist on any therapeutic window or intervention timing given the absence of reported surviving/treated patients.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (biallelic), confirmed in both reported families, including documented parental consanguinity in the index pedigree.
- **Penetrance:** Appears fully penetrant in the (very small, n=2-family) reported cohort — both affected sibs in the index family were symptomatic and died; no asymptomatic or mildly-affected biallelic carriers have been reported. Given the extremely small sample size, a formal penetrance estimate cannot be responsibly asserted beyond "apparently complete in the cases reported."
- **Expressivity:** Cannot be meaningfully assessed — only a single recurrent variant (p.Ala53Pro) has been reported in humans, in two families with a grossly concordant, severe, lethal phenotype; there is no allelic series to demonstrate variable expressivity.
- **Genetic anticipation, germline mosaicism:** Not applicable/not reported — no repeat-expansion mechanism, and no mosaicism data reported.
- **Founder effect:** Strongly suspected (see §2) — both reported unrelated families are Turkish, and the identical c.157G>C variant was found in both, but a formal founder-haplotype study has not been published in the sources retrieved here.
- **Carrier frequency:** Not established/not reported.
- **Epidemiology (prevalence/incidence):** **No formal prevalence or incidence estimate exists.** This is one of the rarest entries in the MC4DN (mitochondrial Complex IV deficiency, nuclear type) disease group, with only two published families worldwide. Orphanet's ORPHA:1561 entry covers the broader "fatal infantile cytochrome C oxidase deficiency" umbrella (multiple causal genes), not a COA5-specific prevalence figure — do not conflate the umbrella-term prevalence with a COA5-specific number, as none exists.
- **Population demographics:** Both reported families of **Turkish ethnicity**; no data on prevalence or geographic distribution beyond this. Sex ratio: not distinctively reported (mitochondrial nuclear-gene AR disorders generally show no sex bias, consistent with autosomal — not X-linked or mitochondrial-DNA — transmission here).

---

## 10. Diagnostics

**Laboratory tests:**
- Blood lactate (elevated, 2.5–11 mmol/L reported range)
- Urinary lactate and ethylmalonic acid (elevated)
- Liver function tests (abnormal)
- Muscle/fibroblast Complex IV (cytochrome c oxidase) enzymatic activity assay — **the key confirmatory biochemical test**, showing isolated, severe CIV deficiency with normal activity of Complexes I, II, III, V

**Imaging:** Echocardiography — demonstrated biventricular hypertrophic cardiomyopathy with septal hypertrophy and a non-compaction myocardial appearance in the reported cases; no further imaging modality detail (cardiac MRI, brain MRI) was retrieved in this search pass.

**Genetic testing:** Clinically available as a **targeted sequence-analysis test for all coding COA5 exons** (postnatal), listed in NCBI's Genetic Testing Registry under the CEMCOX3/MC4DN9 indication ([GTR test 586086](https://www.ncbi.nlm.nih.gov/gtr/tests/586086/)); would also be captured on any **mitochondrial Complex IV deficiency gene panel** and on **exome/genome sequencing** given the nonspecific, phenotypically-overlapping presentation shared across the MC4DN gene group (COA5, COA6, COA7, SURF1, SCO1/2, COX10/15, PET100, NDUFA4, etc.).

**Confirmatory functional/research-level testing:** Complexome profiling and immunoblotting for COX assembly intermediates (as performed in PMID:39779219) — this is a research-level rather than routine clinical diagnostic tool at present.

**Differential diagnosis:** Other nuclear-encoded Complex IV assembly-factor disorders presenting with neonatal hypertrophic cardiomyopathy and lactic acidosis — notably **SCO2**-related fatal infantile cardioencephalomyopathy (a classic, better-characterized member of this disease class and likely the original prototype for the "cardioencephalomyopathy" naming convention), **COX15**, **COA6**, and other MC4DN subtypes; also mitochondrial DNA-encoded COX-subunit defects and other primary mitochondrial cardiomyopathies (e.g., *MTO1*, *TAZ*/Barth syndrome, and other respiratory-chain-complex disorders) should be considered and excluded biochemically/genetically.

**Screening:** No population or newborn-screening program specifically targets COA5-related disease; given its rarity this would not be expected to appear on standard newborn metabolic screening panels (which target treatable inborn errors of metabolism, and this disorder currently has no disease-modifying treatment — see §12).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** **Uniformly fatal in early infancy** in all reported cases (8–10 days per one source; "3 months" per a conflicting secondary summary — resolve against primary text, see §8). No long-term survivors have been reported in the literature retrieved here.
- **Life expectancy:** Days to at most a few months, based on the two reported families; this is among the most rapidly fatal entries in the mitochondrial Complex IV deficiency disease group as currently documented.
- **Morbidity/complications:** Respiratory insufficiency requiring intubation, hepatic dysfunction, and progressive cardiac failure were the reported proximate complications leading to death.
- **Recovery potential:** None reported/expected given the uniformly fatal course and absence of any reported disease-modifying intervention.
- **Prognostic factors/biomarkers:** No prognostic stratification exists — the extremely small reported cohort (n=2 families) with concordant severe outcomes precludes any meaningful biomarker-based prognostic modeling at this time.

---

## 12. Treatment

**No disease-specific, disease-modifying, or FDA-approved treatment exists for COA5-related disease.** No pharmacotherapy, gene therapy, cell therapy, or targeted molecular therapy trial was identified for this specific gene/disease in this search pass, and none would be expected given its ultra-rarity (two published families) and the absence of any registered clinical trial.

What can be stated, by extrapolation from general mitochondrial disease management (and should be clearly labeled in any KB entry as **general supportive-care extrapolation, not COA5-specific evidence**):
- **Supportive care** for hypertrophic cardiomyopathy and respiratory insufficiency (e.g., **NCIT:C15747** Supportive Care; **NCIT:C15986** Pharmacotherapy for symptomatic cardiac management such as diuretics/beta-blockers, though no COA5-specific citation supports their use)
- Standard "mitochondrial cocktail" supplementation (CoQ10, riboflavin, carnitine, thiamine) is commonly used empirically across the broader mitochondrial respiratory chain disease group, but **no COA5-specific evidence of efficacy was found** in this search — do not curate this as evidence-supported for this specific gene without a direct citation.
- No gene therapy, RNA-based therapy, or targeted precision-medicine approach has been reported or is in development specifically for COA5 disease.

**Clinical trials:** No registered ClinicalTrials.gov entry specific to COA5-related disease was identified in this search pass.

This is a genuine and clinically important gap to flag explicitly in the KB entry: **treatment content for this disorder should be limited to general supportive-care framing, clearly distinguished from disease-specific evidence**, consistent with the two-family, no-survivor natural history described above.

---

## 13. Prevention

- **Primary prevention:** **Genetic counseling** for consanguineous families/carrier couples, particularly relevant given the documented consanguinity in the index family and the apparent Turkish founder-variant pattern (see §2, §9). Suggested NCIT term: **NCIT:C15240** (Genetic Counseling).
- **Secondary prevention/screening:** **Carrier screening and prenatal/preimplantation genetic testing** are reasonable extrapolated recommendations for families with a known COA5 pathogenic variant (standard practice for any severe, early-lethal autosomal recessive disorder with an identified causal variant), but **no COA5-specific carrier-screening program, prenatal-testing case report, or PGD case has been published** in the sources retrieved here — this should be flagged as inferred-by-analogy rather than directly evidenced.
- **Tertiary prevention:** Not applicable given the absence of any reported surviving/treated patients in whom complication-prevention strategies could be documented.
- No population-level, public-health, immunization, or environmental-intervention prevention strategy is applicable to this purely monogenic disorder.

---

## 14. Other Species / Natural Disease

**No naturally-occurring COA5-related disease has been reported in any non-human species** (companion animal, livestock, or wildlife) in the sources retrieved here — a search of veterinary/OMIA-type sources specific to COA5 did not surface any hits, and this should be treated as a genuine absence rather than an unresearched gap, consistent with COA5 disease being an ultra-rare human founder-variant condition rather than a naturally recurring animal phenotype.

**Orthology:** COA5 is conserved from yeast (**Pet191**) through mouse (**Coa5**, MGI:1923428) to human, consistent with its fundamental, evolutionarily conserved role in Complex IV biogenesis (see §15 for mouse-specific data).

---

## 15. Model Organisms

- **Yeast (*Saccharomyces cerevisiae*):** *PET191* — the original ortholog studied; early yeast work established a role in COX assembly without a demonstrated direct effect on mitochondrial translation or copper metalation of COX subunits (per the mechanistic background cited in PMID:39779219's discussion). This represents indirect/orthology-based model support rather than a disease-recapitulating model.
- **Mouse:** *Coa5* (MGI:1923428) has multiple targeted, gene-trapped, and chemically-induced alleles catalogued (9 total alleles; 7 strains available via IMSR), with phenotype annotations spanning behavioral/neurological, embryonic development, endocrine, growth, integument, mortality/aging, and reproductive categories per the MGI summary retrieved. **However, the specific phenotypic details, zygosity (heterozygous vs. homozygous), and whether homozygous null is embryonic lethal were not resolved in this search pass** — this is an important gap: if *Coa5*-null mice are embryonic lethal, that would be a directly relevant "does the null model recapitulate/exceed the human phenotype" finding (bearing on human-model-fidelity assessment) and should be pulled from MGI's detailed phenotype allele pages before KB curation, rather than asserted here without direct confirmation.
- **Human cellular model (heterologous):** **CRISPR/Cas9-engineered COA5-knockout U2OS (human osteosarcoma) cell line** (7-bp frameshift deletion) — this is the best-characterized functional model, directly recapitulating **isolated Complex IV enzymatic deficiency** and the same class of stalled MT-CO1-containing assembly subcomplexes seen in patient fibroblasts (PMID:39779219). Because U2OS is a non-cardiac, non-physiological cell line, this model has **high fidelity for the core biochemical/assembly mechanism** but **cannot recapitulate the cardiomyopathy or organismal lethality phenotype** — an important `model_scale` distinction (cellular/molecular readout only; no tissue- or organism-level readout) if curated into a `modeled_mechanisms` link.
- **Patient-derived primary cells:** Dermal fibroblasts (both families) and skeletal muscle biopsy tissue (second family) served as **primary, disease-relevant (non-heterologous) models**, directly showing isolated CIV deficiency and assembly-intermediate accumulation — these are patient material rather than "model organisms" per se but are the most disease-relevant functional evidence available.
- **No zebrafish, *Drosophila*, or *C. elegans* COA5/Pet191-ortholog disease model was identified** in this search pass, despite orthologs likely existing (COA5 is described elsewhere as having stringent mouse/zebrafish orthology per one GeneCards-derived summary) — flag as an unexploited/unreported model-organism gap rather than an established negative finding.

---

## Summary of Notable Gaps for KB Curation

1. **Age-at-death discrepancy** (8–10 days vs. "3 months" from different secondary abstractions of PMID:21457908) — must be resolved against the primary paper.
2. **CNS/encephalopathy phenotype** is implied by the disease-class name but not directly documented in the sources retrieved here — verify in the primary text before curating a distinct CNS pathophysiology node.
3. **gnomAD/ClinVar-level variant frequency and classification** for c.157G>C were not independently pulled and should be confirmed directly.
4. **Exact HGNC ID, GO molecular-function terms, and UniProt subcellular-localization detail** for COA5 should be verified via OAK/UniProt lookup rather than taken from this search pass.
5. **Mouse *Coa5*-null phenotype detail** (viability, whether embryonic lethal) should be pulled directly from MGI's allele-specific phenotype pages.
6. No treatment, prevention, or model-organism-disease-recapitulation content beyond general extrapolation currently has direct COA5-specific citation support — this scarcity is itself the most important characteristic of this ultra-rare entry (two published families total) and should be represented honestly in the KB rather than padded with generic mitochondrial-disease boilerplate presented as disease-specific evidence.

## Primary Sources / Citations

- Huigsloot M, et al. "A mutation in C2orf64 causes impaired cytochrome c oxidase assembly and mitochondrial cardiomyopathy." *Am J Hum Genet.* 2011;88(4):488–493. **PMID:21457908**
- [COA5 has an essential role in the early stage of mitochondrial complex IV assembly](https://pmc.ncbi.nlm.nih.gov/articles/PMC11711468/) — *Life Science Alliance* 2025 (preprint: medRxiv 2024.08.27.24312374). **PMID:39779219**
- [OMIM #616500 — Mitochondrial Complex IV Deficiency, Nuclear Type 9](https://omim.org/entry/616500)
- [OMIM *613920 — COA5](https://omim.org/entry/613920)
- [Orphanet ORPHA:1561 — Fatal infantile cytochrome C oxidase deficiency](https://www.orpha.net/en/disease/detail/1561)
- [NCBI Gene 493753 — COA5](https://www.ncbi.nlm.nih.gov/gene/493753)
- [GTR Test 586086 — CEMCOX3/COA5 sequence analysis](https://www.ncbi.nlm.nih.gov/gtr/tests/586086/)
- [MGI:1923428 — Coa5 mouse gene detail](https://www.informatics.jax.org/marker/MGI:1923428)
- [NORD/MONDO disease abstraction](https://rarediseases.org/mondo-disease/cardioencephalomyopathy-fatal-infantile-due-to-cytochrome-c-oxidase-deficiency-3/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

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
| Terms checked | 23 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014667` (1 mention) - the report calls it "corresponds to MC4DN9"; MONDO calls it **cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency 3**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0005633` (1 mention) - HP does not contain this term

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1923428` - called "Coa5", "Mouse:** *Coa5", "Coa5 mouse gene detail"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.