---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T13:10:55.103200'
end_time: '2026-10-15T13:14:55.741591'
duration_seconds: 240.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hackmann-Di Donato Syndrome
  mondo_id: MONDO:0026733
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
  num_turns: 42
  total_cost_usd: 2.6801260000000005
  session_id: 1d239467-146e-43ea-931e-0e26ec9ff5a9
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 6
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 20
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 64
  verified: 64
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15986
    reported_labels:
    - Antiseizure medication when epilepsy is present
    ontology_label: Pharmacotherapy
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hackmann-Di Donato Syndrome
- **MONDO ID:** MONDO:0026733 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hackmann-Di Donato Syndrome** covering all of the
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

Reading the files directly instead.

I've read the 18 cached references and the MedGen record. Next I'm getting the full cohort phenotype table from the 2019 AJHG paper.

# Hackmann-Di Donato Syndrome (NKAP-related X-linked syndromic intellectual disability): Research Report

**Prepared:** 2026-10-15 · **Target:** MONDO:0026733 · **Category:** Mendelian

**Sources and how far to trust them.** Most of this report rests on the 18 references already cached in this worktree's `references_cache/`. Quotes from those are marked *(abstract)* or *(full text)* and can be copied as snippets. I also used two web sources:
- the PMC full text of Fiordaliso et al. 2019 ([PMC6848994](https://pmc.ncbi.nlm.nih.gov/articles/PMC6848994)), which supplies the per-feature counts;
- the NCBI MedGen record ([C5393302](https://ncbi.nlm.nih.gov/medgen/C5393302)).

The per-feature counts came through a WebFetch summary, not a cached file. **Check every number and quote taken from that source against the PDF before using it as a snippet.**

Ontology CURIEs below come from MedGen, the stub, or the draft entry, or are leads I wrote from memory. Marked ⚠ means not yet looked up. Per the repository's term contract, run `runoak` or `just validate-terms` on each before binding.

---

## 1. Disease Information

**Overview.** Hackmann-Di Donato syndrome (HDDS; OMIM-style symbol MRXSHD) is an X-linked recessive neurodevelopmental disorder. It is caused by hemizygous missense variants in **NKAP** (Xq24), which encodes the NF-κB activating protein. NKAP is a nuclear-speckle and spliceosome-associated protein that also acts as a transcriptional corepressor with HDAC3.

The defining publication is Fiordaliso et al. 2019 (PMID:31587868, *Am J Hum Genet*). It reported 10 affected males from 8 families with:
- developmental delay or intellectual disability;
- hypotonia;
- Marfanoid habitus with tall stature;
- joint laxity, arachnodactyly and scoliosis;
- behavioral abnormalities;
- a recognizable long-face gestalt.

> "we report a disorder of transcriptional regulation due to missense mutations in the X chromosome gene, NKAP. These mutations are clustered in the C-terminal region of NKAP where NKAP interacts with HDAC3 and post-catalytic spliceosomal complex proteins." — PMID:31587868 (abstract)

> "The clinical features of affected individuals are highly conserved and include developmental delay, hypotonia, joint contractures, behavioral abnormalities, Marfanoid habitus, and scoliosis." — PMID:31587868 (abstract)

**Eponym.** The syndrome is named after Karl Hackmann and Nataliya Di Donato. Their 2016 re-examination of patients clinically diagnosed with Lujan-Fryns syndrome found an NKAP variant in one individual:

> "X-exome sequencing of four individuals revealed private or non-recurrent mutations in NKAP and LAS1L in one patient each." — PMID:26358559 (abstract)

**Identifiers**

| System | ID | Source |
|---|---|---|
| MONDO | MONDO:0026733 "intellectual developmental disorder, X-linked, syndromic, Hackmann-Di Donato type" | stub, MedGen |
| OMIM (phenotype) | 301039 | MedGen; PMID:38647244 ("MRXSHD, MIM: #301039") |
| OMIM (gene) | 300766 (NKAP) | MedGen |
| MedGen | C5393302 | MedGen |
| NCBI Gene | 79576 (NKAP) | MedGen |
| HGNC | hgnc:29873 (NKAP) | stub, draft |
| Orphanet | **Not found.** No Orphanet record turned up in search; do not cite an ORPHA code until one is located. | — |
| ICD-10/ICD-11, MeSH | No disease-specific code found. Parent concepts only (X-linked ID). | — |
| MONDO parent | MONDO:0020119 "X-linked syndromic intellectual disability" | stub |

**Synonyms**
- Hackmann-Di Donato syndrome; also spelled Hackman-Di Donato (PMID:41917976 uses the single-n form)
- Intellectual developmental disorder, X-linked, syndromic, Hackmann-Di Donato type (MRXSHD)
- Mental retardation, X-linked, with Marfanoid habitus, 2 (MedGen)
- NKAP-related syndrome / NKAP mutation-related disorder (PMID:36929417, PMID:38647244)

**Data provenance.** Everything here comes from published case series and case reports (aggregated, disease-level). No EHR or registry data exist.

**Reported individuals to date (about 14):**
- 10 males in Fiordaliso 2019;
- 2 male fetuses in Xu 2024 (PMID:38647244);
- 1 boy with an exon-4 variant of uncertain significance in Semyachkina 2026 (PMID:41917976);
- 1 or more members of a family in Gérard 2026 (PMID:42481913), including "the oldest known patient".

Gérard 2026 states: "Only 12 individuals harboring pathogenic NKAP variants have been reported in the literature."

---

## 2. Etiology

**Primary cause.** Germline hemizygous missense variants in NKAP. Every variant classified pathogenic or likely pathogenic falls in exons 8–9, which encode the C-terminal (DUF926) region.

> "All pathogenic nucleotide variants were located in exons 8 and 9, encoding the C-terminal part of NKAP." — PMID:41917976 (full text)

**Genetic risk factors**
- **Variant hotspots** at p.Arg330 and p.Arg333 (see §4).
- **Unaffected or mildly affected carrier mothers.** Three affected males in Fiordaliso 2019 inherited the variant from such mothers. Xu 2024 found carrier grandmothers and aunts in a multigenerational family.
- **Maternal germline mosaicism** in one sibship. Two brothers carried an apparently de novo variant (PMID:41917976 full text: "In one pedigree, two siblings appeared to have inherited the mutation due to maternal germline mosaicism.").
- **Modifier genes:** none identified.

**Environmental risk factors.** None reported. In Xu 2024 the mother of the CHD fetuses reported "no history of illness, medication usage or exposure to either radiation or harmful substances during her pregnancy" (PMID:38647244 full text).

**Protective factors and gene–environment interactions.** None reported.

**Sex-specific protection in females.** The plausible explanation is skewed X-inactivation, but it is only partly demonstrated:
- **Mouse:** heterozygous females with a deleterious Nkap allele showed 83–97% inactivation of the mutant X, explained as secondary selection against cells expressing the mutant allele (PMID:41828556).
- **Human:** one report of a nonsense NKAP variant in a hemophilia A carrier with extreme skewing. It is cited as ref. 10 in PMID:41828556, but its PMID is not cached; fetch it before citing.
- **Not measured in HDDS carrier mothers.** Fiordaliso 2019 reports none: "Mothers carrying NKAP mutations were unaffected or much less severely affected." This is a curatable knowledge gap.

---

## 3. Phenotypes

Frequencies are from Fiordaliso 2019 Table 1 (n=10 males, ages 4–21 years). Verify them against the PDF before encoding. Suggested HPO terms come from MedGen's HPO list where available; ⚠ marks a term to look up.

### Core neurodevelopmental features

| Phenotype | Freq. | HPO (suggested) | Notes |
|---|---|---|---|
| Global developmental delay / intellectual disability | 10/10 | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Onset in infancy. Speech delay is prominent and walking is mildly delayed (OMIM/MedGen summary). Severity ranges from borderline intelligence (PMID:41917976) to ID. |
| Hypotonia | 10/10 | HP:0001252 Hypotonia (MedGen lists "Hypotonia") | Congenital/infantile. A mouse correlate exists: reduced grip strength (PMID:41828556). |
| Behavioral abnormality (ADHD and/or aggression) | 5/10 | HP:0007018 ADHD ⚠; HP:0000718 Aggressive behavior ⚠ | Childhood onset. |
| Delayed speech | common (OMIM summary) | HP:0000750 Delayed speech and language development ⚠ | |
| Seizures (absence epilepsy) | 1 case (VUS case) | HP:0002121 Absence seizure ⚠ | PMID:41917976 only. The genotype is a VUS, so do not generalize. |
| White matter lesions on MRI (stable) | 1 family | HP:0002500 Abnormality of the cerebral white matter ⚠ | PMID:42481913: "Brain MRI revealed stable white matter lesions." Not systematically assessed in other cases. |

### Growth and habitus

| Phenotype | Freq. | HPO | Notes |
|---|---|---|---|
| Tall stature / Marfanoid habitus | 10/10 | HP:0001519 Disproportionate tall stature (MedGen); HP:0001166 Arachnodactyly | The draft entry uses HP:0001519 with preferred_term "Marfanoid habitus", which matches MedGen. |
| Central/abdominal obesity | 5/10 | HP:0012743 Abdominal obesity ⚠ (MedGen lists the label) | |

### Musculoskeletal

| Phenotype | Freq. | HPO |
|---|---|---|
| Joint laxity/hypermobility | 9/10 | HP:0001382 Joint hypermobility ⚠ |
| Arachnodactyly | 8/10 | HP:0001166 ⚠ |
| Scoliosis | 6/10 | HP:0002650 ⚠ |
| Pectus carinatum or excavatum | 5/10 | HP:0000768 / HP:0000767 ⚠ |
| Camptodactyly | 4/10 | HP:0012385 ⚠ |
| Joint contractures | stated in the abstract; no separate count | HP:0001371 Flexion contracture ⚠ |
| Talipes equinovarus | 1/10 | HP:0001762 ⚠ |
| Recurrent shoulder dislocation, dolichostenomelia, pes planovalgus | VUS case | PMID:41917976 |

### Craniofacial

| Phenotype | Freq. | HPO |
|---|---|---|
| Long face | 8/10 | HP:0000276 ⚠ |
| Prominent/protruding ears | 8/10 | HP:0000411 ⚠ |
| Open mouth appearance | 7/10 | HP:0000194 ⚠ |
| Midface retrusion | 7/10 | HP:0011800 ⚠ |
| Short philtrum | 7/10 | HP:0000322 ⚠ |

### Cardiovascular

Fiordaliso 2019 reports roughly 6/10 with a cardiac finding. Xu 2024 counts 8/12 across all reported cases, including the two fetuses (PMID:38647244 Table 3).

| Phenotype | Freq. | HPO |
|---|---|---|
| Mitral regurgitation / mitral valve prolapse | 3/10 | HP:0001653 ⚠; HP:0001634 ⚠ |
| Atrial septal defect | 1/10 | HP:0001631 ⚠ |
| Ventricular septal defect | 1/10 postnatal; 2/2 fetuses | HP:0001629 ⚠ |
| Patent ductus arteriosus | 1/10 postnatal + 1 fetus | HP:0001643 ⚠ |
| Aortic root dilatation | 1/10 | HP:0002616 Aortic root aneurysm (MedGen) ⚠ |
| Pulmonary stenosis, overriding aorta (tetralogy of Fallot-like) | 1 fetus | HP:0001642 ⚠; HP:0002623 ⚠ |

Genotype–phenotype note:

> "Particularly, all four individuals carrying mutation at p.R330 had cardiac defects, strongly suggesting a correlation between NKAP p.R330 mutation and cardiac development." — PMID:38647244 (full text)

### Genitourinary

| Phenotype | Freq. | HPO |
|---|---|---|
| Cryptorchidism | 4/10 | HP:0000028 ⚠ |

### Prenatal findings (PMID:38647244)

- Increased nuchal translucency of 3.0 mm at 12 weeks (HP:0010880 ⚠).
- Mild lateral ventriculomegaly.
- Choroid plexus cysts (HP:0002190 ⚠).
- Fetal tachycardia.

> "These prenatal anomalies include cardiac defect and thickened NT, which could be observed as early as 12 weeks gestation" — PMID:38647244 (full text)

### Phenotype the draft entry includes but the sources do not support

**Macrocephaly** is in the draft YAML `description`. It does **not** appear in Fiordaliso 2019 (per the full-text read), MedGen's HPO list, or any cached reference. Remove it from the description unless a source turns up.

### Quality of life

No QoL instrument data exist (no EQ-5D, SF-36 or PROMIS). The main inferred burden is lifelong ID with behavioral problems, connective-tissue complications (scoliosis, joint instability), and cardiac follow-up.

---

## 4. Genetic / Molecular Information

**Causal gene:** NKAP (hgnc:29873; NCBI Gene 79576; OMIM 300766; Xq24). The transcript is NM_024528.4, encoding a 415-amino-acid protein of about 47 kDa. Its domains are:
- an N-terminal RS (arginine/serine-rich) domain that mediates nuclear localization;
- a central basic region;
- a C-terminal DUF926 domain that binds HDAC3 and spliceosomal proteins. Shapiro 2019 (PMID:30804042) places the minimal HDAC3-binding site around F347/Y352.

**Variants reported**

| Variant (NM_024528.4) | Protein | Families / individuals | Origin | Classification | Source |
|---|---|---|---|---|---|
| c.988C>T | p.Arg330Cys | 1 male (de novo) + 2 fetuses (maternal) | de novo; maternal | Likely pathogenic (PS2+PM2_Sup+PM5_Sup+PP1_Sup per Xu); ClinVar VCV 827654 listed as VUS at the time | PMID:31587868; PMID:38647244 |
| c.989G>A | p.Arg330His | 1 male | de novo | LP | PMID:31587868 |
| c.998G>A | p.Arg333Gln | 6 males / 4 families (recurrent hotspot) | maternal; germline mosaic sibs; unknown | P/LP | PMID:31587868 |
| c.1010T>C | p.Ile337Thr | 1 male | de novo | LP | PMID:31587868 |
| c.1082G>A | p.Arg361Gln | 1 male | unknown | LP | PMID:31587868 |
| c.612A>C | p.Arg204Ser (exon 4) | 1 boy | not stated in abstract | **VUS** | PMID:41917976 |
| familial inherited variant (not stated in abstract) | — | 1 family | maternal | pathogenic | PMID:42481913 |

Xu 2024 Table 3 prints c.988G>A for p.R333Q in some rows. Fiordaliso's own text gives c.998G>A, which is the correct HGVS. Use c.998G>A.

- **Variant type:** all are missense. No truncating, splice or copy-number variant has been reported in an affected male. This is consistent with complete loss of NKAP being lethal (see the model data below).
- **Population frequency:** the hotspot alleles are absent from gnomAD (PM2 cited in PMID:38647244).
- **Origin:** germline. There is no somatic role in HDDS. Somatic NKAP loss in sarcoma (PMID:27694884) is a separate cancer-biology observation and not part of this disease.

**Functional consequence.** This is best described as **partial or altered loss of function confined to the C-terminal interaction domain**, not null:
- NKAP mRNA and protein levels were normal in patient lymphoblastoid cell lines (LCLs), and HDAC3 levels and distribution were unchanged (Fiordaliso, full text).
- p.R330C reduced NKAP–HDAC3 co-IP from 44.9% to 16.7% and shifted NKAP to the nuclear periphery in HEK293T/HeLa overexpression experiments (PMID:38647244).
- In mice, complete Nkap deletion in hematopoietic cells is lethal (PMID:20610818). In zebrafish, a C-terminal truncation is lethal by 4 dpf (PMID:31587868).

Suggested `functional_impact_category`: `PARTIAL_LOSS_OF_FUNCTION`, or leave it unset with a note. Dominant-negative and gain-of-function have not been tested; do not assert either.

**Genotype–phenotype.** p.Arg330 variants are associated with congenital heart disease (4/4 carriers). No other correlation is established.

**Epigenetics.** No disease-specific methylation signature (episignature) has been reported. Skewed X-inactivation in carrier females has been shown only in the mouse (PMID:41828556).

**Chromosomal abnormalities.** None. This is a point-mutation disorder, and karyotype and chromosomal microarray were normal in the fetal proband (PMID:38647244).

**ClinGen.** No gene–disease validity curation for NKAP–HDDS was found. Leave `gene_disease_validity` absent.

---

## 5. Environmental Information

There are no environmental, lifestyle or infectious contributors. The `environmental:` section should stay empty.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Germline hemizygous missense variant in the NKAP C-terminal (DUF926) domain** (exons 8–9; hotspots R330, R333). *Demonstrated in patients* (PMID:31587868).
2. **The variant alters NKAP protein interactions without lowering NKAP abundance.**
   - Patient LCLs: NKAP mRNA and protein are normal (PMID:31587868 full text).
   - **2a. Reduced NKAP–HDAC3 association.** *Demonstrated in vitro for p.R330C only* (PMID:38647244). Inferred for other variants, which sit in the HDAC3-binding region. The importance of this interaction is supported by the Y352A HDAC3-binding-null mouse (PMID:30804042, PMID:31387873).
   - **2b. Possible perturbation of NKAP's role in the post-catalytic spliceosome (C*/P complex, exon ligation).** *Inferred* from the structural location of the variants (PMID:30705154: "CACTIN, SDE2, and NKAP-factors implicated in alternative splicing-further stabilize the catalytic conformation of the spliceosome during exon ligation").
   - **2c. Altered intranuclear (nuclear speckle) distribution.** *In vitro, p.R330C only* (PMID:38647244). The nuclear-speckle framing is from the review PMID:36929417.
3. **Transcriptional dysregulation.** Loss of NKAP–HDAC3 corepressor activity, including on Notch targets, leads to a distinctive transcriptome signature.
   - Patient LCLs show 455 upregulated and 721 downregulated genes, with HES1 and JAG1 up (PMID:31587868 full text).
   - **3a. Long genes with many exons are selectively downregulated.** *Demonstrated in patient LCLs* (PMID:31587868 abstract: "transcriptome signature, which is characterized by the downregulation of long genes with higher exon numbers").
   - **3b. Notch target genes are de-repressed.** *Demonstrated in mouse T cells* (PMID:19409814: Hes1, Deltex1 8–20-fold higher with NKAP loss). Patient LCLs show HES1/JAG1 changes. That this occurs in neural or mesenchymal tissue is *inferred*.
   - Splicing changes in patient cells were modest: only 39 events, with some increase in intron retention. This is *weak evidence* that mis-splicing is the main driver.
4. **Branching tissue consequences** (all *inferred*; none shown in human tissue):
   - **4a. Brain:** disrupted neurodevelopmental gene programs lead to ID/DD, hypotonia and behavioral abnormality. Supporting context: NKAP is highly expressed in neural progenitors and migrating neuroblasts (mouse SVZ/RMS, PMID:24583034), and long, exon-rich genes are enriched among neuronal and synaptic genes. That second point is my inference, not a statement from the cited sources.
   - **4b. Connective tissue / skeleton:** dysregulated extracellular-matrix gene expression (ECM terms enriched in the LCL differentially expressed genes) leads to Marfanoid habitus, joint laxity, arachnodactyly and scoliosis. *Inferred*; the mechanism is unknown.
   - **4c. Heart:** altered expression of cardiac morphogenesis genes (JAG1 and DNAH11 up, DHRS3 down with p.R330C in HEK293T) leads to septal defects, outflow-tract and valve anomalies (PMID:38647244). *In vitro inference.* The authors themselves note that the direction of change for DHRS3 conflicts with the LCL data.
5. **Clinical syndrome:** ID, hypotonia, Marfanoid habitus, connective-tissue features and variable CHD.

### Parallel branch to model as a hypothesis, not a demonstrated disease mechanism

**Genome-stability functions of NKAP:**
- SUMOylated NKAP anchors CENP-E at kinetochores for chromosome alignment (PMID:27694884).
- NKAP–HDAC3 prevents R-loop accumulation and DNA damage (PMID:37322264).
- Mutant NKAP mouse embryonic fibroblasts proliferate 3.4-fold less, become senescent, and upregulate p27/p57, IL-1β and IL-6 (PMID:41828556).

None of these has been tested with HDDS patient variants. Their relevance to HDDS is a **knowledge gap**. The SUMOylation sites lie in amino acids 277–415, which overlaps the patient-variant region and makes this a reasonable hypothesis.

### NKAP biology by category

- **Molecular pathways:**
  - Notch signaling (NKAP is a corepressor with CIR/HDAC3): PMID:19409814, PMID:24583034.
  - NF-κB activation (original description, overexpression in 293 cells): PMID:14550261.
  - Pre-mRNA splicing at exon ligation: PMID:30705154.
- **Cellular processes:** transcriptional repression; mitotic chromosome alignment; R-loop suppression and genome stability; hematopoietic stem cell maintenance (PMID:20610818, PMID:30804042); T/iNKT/Treg maturation (PMID:21624937, PMID:23481390, PMID:31387873). The immune and hematopoietic phenotypes are mouse conditional-knockout findings with **no reported human HDDS counterpart**. Do not add immune phenotypes.
- **Protein dysfunction:** altered binding (HDAC3) and altered localization. Not misfolding or aggregation.
- **Metabolic and immune involvement:** none reported in patients.
- **Molecular profiling:** LCL RNA-seq in Fiordaliso 2019. No GEO accession is quoted in the summary I have; check the paper's data availability statement before running `just discover-datasets`.

### Suggested ontology terms (⚠ verify all)

**GO, biological processes**
- GO:0000122 negative regulation of transcription by RNA polymerase II
- GO:0045746 negative regulation of Notch signaling pathway
- GO:0000398 mRNA splicing, via spliceosome
- GO:0051310 metaphase chromosome alignment
- GO:0007399 nervous system development
- GO:0007507 heart development
- GO:0030198 extracellular matrix organization

**GO, cellular components**
- GO:0016607 nuclear speck
- GO:0071013 catalytic step 2 spliceosome
- GO:0000776 kinetochore

**CL, cell types**
- CL:0000540 neuron
- CL:0011020 neural progenitor cell
- CL:0000057 fibroblast
- CL:0000746 cardiac muscle cell (for the CHD branch)
- CL:0000037 hematopoietic stem cell (model-only context)

**Interacting gene:** HDAC3 (HGNC ID ⚠ — look it up; do not write it from memory).

---

## 7. Anatomical Structures Affected

**Primary systems**
- Central nervous system: brain, UBERON:0000955 ⚠.
- Musculoskeletal and connective tissue: vertebral column UBERON:0001130 ⚠ (scoliosis); joints; digits.
- Heart: UBERON:0000948 ⚠. Specifically the interventricular and interatrial septa, mitral valve and aortic root.

**Secondary systems**
- Testis / cryptorchidism (urogenital).
- Cerebral white matter (one family).

**Subcellular:** nucleus, nuclear speckles, spliceosome, and kinetochores during mitosis.

**Lateralization:** systemic and bilateral. Scoliosis is asymmetric by nature.

---

## 8. Temporal Development

- **Onset:** congenital or prenatal.
  - Cardiac defects and increased nuchal translucency are detectable from 12 weeks' gestation (PMID:38647244).
  - Hypotonia and developmental delay appear in infancy.
- **Course:** a static neurodevelopmental disorder, with no regression reported.
  - Skeletal features such as scoliosis and Marfanoid proportions become more evident during childhood growth.
  - The white matter lesions in the Gérard family were "stable".
- **Duration:** lifelong.
- **Ages reported:** 4–21 years in the original cohort. Gérard 2026 reports the oldest known patient; the exact age is not in the abstract.
- **Stages, remission, critical periods:** not defined. Early intervention during infancy and childhood is the main window for developmental therapies (general principle; not disease-specific evidence).

---

## 9. Inheritance and Population

- **Inheritance:** X-linked recessive. HP:0001419 is used in the draft; the OMIM/MedGen designation agrees.
- **Penetrance in hemizygous males:** apparently complete for C-terminal variants, with variable expressivity, especially for cardiac involvement.
- **Heterozygous females:**
  - Carrier mothers were "unaffected or much less severely affected".
  - In Xu 2024, female carriers (mother, aunt, grandmother) were healthy.
  - An uncle in that family had developmental delay and spinal instability and died at age 1; he was not genotyped.
- **De novo rate:** 6/10 in the original cohort, as stated by Xu 2024 (Fiordaliso reports 4 apparently de novo individuals plus 2 brothers from germline mosaicism).
- **Germline mosaicism:** yes, one maternal case.
- **Anticipation, founder effects, consanguinity:** none.
- **Epidemiology:**
  - Prevalence is unknown.
  - About 14 individuals have been reported worldwide.
  - Populations: European (German, Czech, Italian, UK), US, Japanese, Korean, Chinese (fetuses) and Russian/Slavic.
  - Suggested `prevalence` record: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED`, citing PMID:42481913 ("Only 12 individuals …").
- **Sex ratio:** affected individuals are male.

---

## 10. Diagnostics

**Genetic testing (the main route)**
- Exome or genome sequencing, ideally trio, is the diagnostic test. Trio exome was used in PMID:38647244 and PMID:42481913, and genome sequencing in PMID:41917976.
- NKAP is on the Genomics England PanelApp intellectual disability panel ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/285/gene/NKAP/)).
- X-exome sequencing first detected it in a Lujan-Fryns-like patient (PMID:26358559).
- Chromosomal microarray and karyotype are normal; they are useful only for excluding differentials.

**Supporting work-up**
- Echocardiography for septal, valve and aortic-root disease.
- Spine radiographs for scoliosis.
- Brain MRI: white matter lesions in one family. Gérard 2026 suggests systematic neuroimaging.
- EEG if seizures occur.
- Prenatal: nuchal translucency and fetal echocardiography, with prenatal exome sequencing in an at-risk family.

**Biomarkers:** none validated. The patient-LCL transcriptome signature (downregulated long, exon-rich genes) is research-only.

**Clinical criteria:** none formalized. Hackmann 2016 argues that "the combination of ID and marfanoid habitus in a male patient is not sufficient for the diagnosis of LFS" (PMID:26358559).

**Differential diagnosis** (all Marfanoid habitus with ID):
- **Lujan-Fryns syndrome** (MED12; also UPF3B, ZDHHC9): nasal speech and specific facies.
- **Marfan syndrome** (FBN1): ectopia lentis and aortic dilatation, with normal intellect.
- **Loeys-Dietz syndrome.**
- **Homocystinuria:** run plasma homocysteine.
- **Stickler syndrome.**
- **Other nuclear-speckleopathies** (ZTTK/SON) (PMID:36929417).

---

## 11. Outcome / Prognosis

- **Survival:** no data. Postnatal patients have been followed into adulthood (21 years in the original cohort; older in the Gérard family).
- **Pregnancy outcomes:** both p.R330C fetuses were terminated after a CHD diagnosis.
- **Morbidity:** lifelong intellectual disability; behavioral problems; risk of scoliosis and joint dislocation; cardiac valve and septal disease, plus potential aortic-root dilatation needing surveillance.
- **Prognostic factors:** p.Arg330 variants predict CHD (based on 4/4 carriers). Nothing else is known.
- **QoL measures:** none published.

---

## 12. Treatment

There is no disease-specific or disease-modifying therapy, and no clinical trials. ClinicalTrials.gov and ICTRP searches are not indicated; none was found. Management is supportive and follows standard care for ID and connective-tissue disorders. These recommendations are by analogy; no HDDS-specific guideline exists.

| Intervention | NCIT (from the CLAUDE.md list; verify) | `therapeutic_modality` |
|---|---|---|
| Early developmental, speech and occupational therapy | NCIT:C15315 Rehabilitation; NCIT:C15302 Physical Therapy | BEHAVIORAL |
| Behavioral management (ADHD/aggression); stimulant or other pharmacotherapy as indicated | NCIT:C15986 Pharmacotherapy (+ `therapeutic_agent` only if a source names a drug) | — |
| Cardiology surveillance; surgical repair of significant CHD | NCIT:C15329 Surgical Procedure | SURGERY |
| Orthopedic management of scoliosis (bracing or spinal fusion) | NCIT:C16186 Orthopedic Surgical Procedure | SURGERY |
| Antiseizure medication when epilepsy is present | NCIT:C15986 | SMALL_MOLECULE |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — |
| Supportive care | NCIT:C15747 Supportive Care | — |

**Evidence gap.** No cached reference describes treatment outcomes. Any treatment rows will need evidence: cite the case reports' management descriptions, or record each row as a general-care recommendation with a `notes:` explanation.

---

## 13. Prevention

- **Primary prevention:** not applicable.
- **Genetic counseling:**
  - A carrier mother has a 50% risk of an affected son with each male pregnancy.
  - An apparently de novo case still carries recurrence risk because of possible germline mosaicism, which has been documented.
- **Testing options in a known family:** carrier testing of female relatives, prenatal diagnosis (shown in PMID:38647244), and preimplantation genetic testing.
- **Secondary prevention:** cardiac and spinal surveillance after diagnosis.
- **Newborn screening:** not applicable.

---

## 14. Other Species / Natural Disease

- No naturally occurring animal disease is known, and nothing is listed in OMIA (not searched exhaustively).
- **Orthologs:**
  - Mouse *Nkap* (on the X chromosome).
  - Zebrafish *nkap*.
  - Rat to human conservation of the C-terminal lysines (PMID:27694884).
  - R330 is "highly conserved among various species" (PMID:38647244).
- NCBI Gene IDs for the orthologs were not retrieved; look them up before encoding.

---

## 15. Model Organisms

| Model | Genotype | Phenotype recapitulation | Limitations | Source |
|---|---|---|---|---|
| **Zebrafish** (*Danio rerio*, NCBITaxon:7955) | nkap c.859delA (exon 8), p.Arg298GlufsTer6, a C-terminal truncation that escapes NMD; also the nkap^hi1477Tg insertion line | Homozygotes: eye, intestinal and cardiac edema; notochord curvature; CNS necrosis from 2 dpf; no heartbeat and 100% lethality by 4 dpf. Heterozygotes are normal. | Truncation, not a patient missense allele. Too severe and lethal to model ID or habitus. | PMID:31587868 |
| **Mouse, germline** (NCBITaxon:10090) | Nkap Δ123bp in-frame N-terminal (RS-domain) deletion, hemizygous males | Reduced forelimb grip strength and altered gait (shorter stride, longer duty cycle), consistent with hypotonia. Normal survival to 18 months, normal size, normal bone length on X-ray. **Does not recapitulate Marfanoid habitus.** | The allele is in the N-terminus, not the C-terminal hotspot. Females show skewed XCI. A frameshift allele (Δ70bp) could not be transmitted. | PMID:41828556 |
| **Mouse, conditional knockouts** | Mx1-cre / Vav-cre; Lck-cre; CD4-cre; Y352A knock-in (HDAC3-binding-null) | Hematopoietic stem cell failure and perinatal lethality; blocked αβ T-cell, iNKT and Treg maturation; lethal autoimmunity with Y352A in Tregs | Hematopoietic and immune only, with no human HDDS correlate. Shows that NKAP–HDAC3 binding is essential in vivo. | PMID:20610818, PMID:19409814, PMID:21624937, PMID:23481390, PMID:30804042, PMID:31387873 |
| **Mouse embryonic fibroblasts** | Δ123bp | 3.4-fold lower proliferation; senescence (SA-β-gal positive; p27/p57, IL-1β, IL-6 up) | In vitro, N-terminal allele | PMID:41828556 |
| **Patient LCLs** (human, in vitro) | p.R333Q, p.R361Q | Transcriptome signature (long-gene downregulation, HES1/JAG1 changes) | Non-neural cell type | PMID:31587868 |
| **HEK293T / HeLa overexpression** | p.R330C | Reduced HDAC3 binding, perinuclear mislocalization, altered JAG1/DNAH11/DHRS3 expression | Overexpression system | PMID:38647244 |

**Suggested model links** (`modeled_mechanisms`):
- Zebrafish → "Dysregulated Transcription": `PARTIALLY_RECAPITULATES`, `fidelity: LOW`.
- Mouse Δ123bp → the hypotonia phenotype: `PARTIALLY_RECAPITULATES`, `fidelity: LOW`. Add a `BOUNDARY_OMISSION` divergence (no Marfanoid habitus) and a `PROXY_QUANTITY` divergence (grip strength standing in for hypotonia).

**Knowledge gap worth recording** (`HUMAN_MODEL_MISMATCH`): no model carries a patient C-terminal missense allele, and no iPSC-derived neuron or organoid model exists.

---

## Notes for curating `kb/disorders/Hackmann-Di_Donato_Syndrome.yaml`

1. **File name.** The stub's `proposed_name` is `Intellectual_Developmental_Disorder_X-linked_Syndromic_Hackmann-Di_Donato_Type`, but the draft uses `Hackmann-Di_Donato_Syndrome`. Either is fine. Delete `stubs/Intellectual_Developmental_Disorder_X-linked_Syndromic_Hackmann-Di_Donato_Type.yaml` in the PR.
2. **Remove "macrocephaly"** from the draft `description`; no source supports it. "Joint hypermobility" (9/10 joint laxity) and "scoliosis" are supported.
3. **Build out the pathograph.** Add the HDAC3-binding and intranuclear-localization nodes, split "Dysregulated Transcription" into its Notch-target and long-gene branches, and wire edges to the neurodevelopmental, connective-tissue and cardiac phenotypes. Without these the phenotypes stay disconnected (`just list-disconnected-phenotypes`).
4. **Discussions.** Record XCI in carrier mothers and the genome-stability functions as `KNOWLEDGE_GAP` discussions.
5. **Exon-4 variant.** Keep p.Arg204Ser out of the causative variant list or mark it VUS (`clinical_significance`), citing PMID:41917976.
6. **No GeneReviews chapter is expected.** Confirm with `just check-genereviews`.
7. **Every snippet** quoted above from an "(abstract)" or cached "(full text)" source should be checked with `just count-verified-snippets`. Numbers from the PMC6848994 WebFetch summary are not in the local cache: that file (PMID_31587868.md) is abstract-only, so quote only its abstract.

---

## Sources

**Cached references**
- PMID:31587868 · PMID:26358559 · PMID:38647244 · PMID:41917976 · PMID:42481913
- PMID:41828556 · PMID:36929417 · PMID:30705154 · PMID:19409814 · PMID:20610818
- PMID:21624937 · PMID:23481390 · PMID:30804042 · PMID:31387873 · PMID:27694884
- PMID:37322264 · PMID:24583034 · PMID:14550261

**Web sources**
- [Fiordaliso et al. 2019, PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6848994)
- [MedGen C5393302](https://ncbi.nlm.nih.gov/medgen/C5393302)
- [Xu et al. 2024, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11034370/)
- [Genomics England PanelApp – NKAP](https://panelapp.genomicsengland.co.uk/panels/285/gene/NKAP/)
- [CHOP news release, 2019](https://chop.edu/news/genetics-researchers-find-new-neurodevelopmental-syndrome)
- [ZFIN publication ZDB-PUB-191008-1](https://zfin.org/ZDB-PUB-191008-1)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 20 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 64 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15986` (2 mentions) - the report calls it "Antiseizure medication when epilepsy is present"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:10090` (1 mention) - the report calls it "Mouse, germline"; NCBITaxon calls it **Mus musculus**, and lists "mouse" among its other names