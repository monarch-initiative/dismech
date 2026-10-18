---
provider: claude_code
model: claude-fable-5-1, claude-haiku-4-5-20251001
cached: false
start_time: '2026-10-05T12:39:19.473747'
end_time: '2026-10-05T12:48:52.524098'
duration_seconds: 573.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Fetal Valproate Syndrome
  mondo_id: MONDO:0012275
  category: Environmental
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
  - claude-fable-5-1
  - claude-haiku-4-5-20251001
  num_turns: 70
  total_cost_usd: 8.613982000000004
  session_id: fb0db24c-d898-420f-810f-a9d2a6e557f5
  stop_reason: end_turn
  permission_denials: 6
  denied_tools:
  - Bash
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 72
reference_validation:
  total_references: 72
  verified: 71
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.014
  quotes_checked: 5
  quotes_valid: 5
  relevance_assessed: 71
  on_topic: 54
  unresolved_references:
  - PMID:35639399
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 86
  verified: 85
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fetal Valproate Syndrome
- **MONDO ID:** MONDO:0012275 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Fetal Valproate Syndrome** covering all of the
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

Still gathering sources: the abstract fetcher dropped the structured abstracts, so I'm re-pulling the key papers in smaller batches to get exact quotes.

Research is essentially complete; I'm doing one last lookup of ontology terms in the local caches, then writing the report.

# Fetal Valproate Syndrome (Fetal Valproate Spectrum Disorder): Research Report

**Target:** Fetal Valproate Syndrome, MONDO:0012275. **Category:** Environmental (teratogenic embryofetopathy). **Compiled:** 2026-10-05.

## How to read this report

- **Quote reliability.** Quotes come from PubMed/Europe PMC abstracts fetched through a summarising tool, so treat every quote as a lead until it is re-checked against `references_cache/` (`just fetch-reference PMID:<id>`).
  - **[V]** marks quotes from abstracts returned in full.
  - **[F]** marks fragments, which are more likely to contain small wording errors.
  - Only PMID:23613074 was read directly from the local reference cache.
- **Ontology terms.** Terms marked ✓ were read from this repository's `cache/*/terms.csv` in this session (CURIE and label confirmed). Terms listed "by label only" were not looked up and have no CURIE on purpose.
- **Sources not retrieved.**
  - The Orphanet page (ORPHA:1906) was blocked, and no `ORPHA_1906.md` exists in the local cache.
  - The abstracts for DiLiberti 1984 (PMID:6439041) and Clayton-Smith 1995 (PMID:8544193) were not returned.
  - The Clayton-Smith 2019 consensus full text was read only as a tool summary, so its figures need checking against the paper.

---

## 1. Disease information

**Overview.** Fetal valproate syndrome (FVS) is a drug-induced embryofetopathy caused by in utero exposure to valproic acid/sodium valproate (VPA). It has three components: a recognisable facial gestalt, major and minor congenital malformations, and neurodevelopmental impairment.

- MONDO defines it as "an anticonvulsant drug-related embryofetopathy that can occur when a fetus is exposed to valproic acid (VPA), characterized by distinct facial dysmorphism, congenital anomalies and developmental delay (especially in language and communication)" (via OLS).
- A 2019 European Reference Network (ERN-ITHACA) consensus proposed the name **Fetal Valproate Spectrum Disorder (FVSD)**: "we feel this better encompasses the broad range of effects seen following VPA exposure in utero" [F] (PMID:31324220).
- The same abstract describes the pattern as "major and minor congenital anomalies, facial dysmorphic features, and neurodevelopmental difficulties, including cognitive and social impairments" [F].

**Identifiers** (from the MONDO:0012275 record via OLS unless noted):

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0012275 "fetal valproate syndrome" |
| OMIM | 609442 (MONDO synonym "susceptibility to valproate embryopathy"; also cited as "fetal valproate syndrome (OMIM #609442)" in PMID:39097820) |
| Orphanet | ORPHA:1906 |
| MeSH | C536525 (supplementary concept) |
| UMLS | C0236026 |
| SNOMED CT | 17231009 |
| NCIT | C98930 |
| DOID | 0060471 |
| ICD-9 | 759.89 |
| ICD-11 | foundation ID 1055155432 |
| GARD | 5447 |
| MedDRA | 10016524 |
| ICD-10 | Not in the MONDO record; Q86.8 ("other congenital malformation syndromes due to known exogenous causes") is from memory and unverified |

**Synonyms.** FVS; fetal valproic acid syndrome; valproic acid embryopathy; valproate embryopathy; susceptibility to valproate embryopathy; fetal valproate spectrum disorder (FVSD). The condition is also a subset of "fetal anticonvulsant syndrome" (FACS).

**Data provenance.** Knowledge is aggregated at disease level. The main sources are:
- prospective pregnancy registries (EURAP, the North American AED Pregnancy Registry, the UK Epilepsy and Pregnancy Register);
- national health-register cohorts (Denmark, the Nordic SCAN-AED study, US claims data);
- EUROCAT congenital-anomaly registries;
- clinic-ascertained case series and case reports.

No EHR-derived individual patient data were used here.

---

## 2. Etiology

### Causal factor

Maternal use of valproate during pregnancy is the single necessary cause. The disease is environmental and not Mendelian.

### Risk factors (modifiers of risk given exposure)

**Dose** is the strongest and best-documented modifier.
- EURAP: major congenital malformations (MCM) in "142 (10·3%) of 1381 pregnancies" on valproate monotherapy [F], with risk rising with dose (p<0.0001 as reported by the tool). Even ≤650 mg/day carried higher risk than levetiracetam (OR 2.43, 95% CI 1.30–4.55, tool-reported) (PMID:29680205).
- Cochrane 2023: "Multiple studies found that the MCM risk is dose-dependent." [F] (PMID:37647086).
- Cochrane 2014, cognition: "A dose effect for VPA was reported in six studies, with higher doses (800 to 1000 mg daily or above) associated with a poorer cognitive outcome in the child." [F] (PMID:25354543).
- The consensus statement gives an overall malformation risk of about 11%, rising to about 24% above 1500 mg/day (tool summary of PMID:31324220).
- A narrative review states doses below 600 mg have limited teratogenic potential (tool paraphrase of PMID:38203562). EURAP shows there is no risk-free dose.

**Timing.**
- First-trimester exposure drives structural malformations (PMID:20558369).
- Exposure in the second half of pregnancy still carries autism risk: exposure was defined "from gestational week 19 until delivery" in the US cohort, where valproate remained associated (PMID:38507750) [V].

**Polytherapy.** Combined use with other antiseizure medications raises malformation rates (tool paraphrase of PMID:38203562).

**Previous affected child.**
- UK register: "For women whose first child had a congenital malformation there was a 16.8% risk of having another child with a congenital malformation, compared with 9.8% for women whose first child did not have a malformation (relative risk 1.73, 95% confidence interval [CI] 1.01-2.96)." [V] (PMID:23167802).
- The valproate-specific recurrence was 21.9% (RR 1.47, 95% CI 0.68–3.20), a trend that was not significant.
- Sibling clusters are reported in PMID:12196666, PMID:11223853 and PMID:15669094.

**Genetic susceptibility: maternal folate-pathway genotype.** Human evidence is suggestive and inconsistent.
- Dean 2007: "No effect of the child's genotype on congenital malformation, neurodevelopmental disorder or FACS was detected." [F] Mothers homozygous for MTHFR 677TT had a three- to four-fold higher risk of an affected child than 677CC mothers (PMID:17853476; earlier report PMID:10563481).
- Kini 2007: maternal MTHFR genotype was associated with malformations, but "the main teratogenic effects are mediated through other mechanisms" [F] (PMID:17951123).
- Mouse model: VPA "significantly increased the malformation rate of CT and TT heterozygote and homozygote mice, respectively, compared to that of CC mice (P < 0.05)" [V] (PMID:40645457; MODEL_ORGANISM).

**Paternal exposure** is not established as a cause. A Norway/Taiwan cohort concluded: "Paternal use of valproate within the 90 days before conception was not associated with an increased risk of NDDs in offspring after adjustment for confounding" [V] (PMID:41733407). The earlier regulatory precaution (EMA/MHRA, 2024) rested on an unpublished registry signal and was not retrieved here.

**Maternal epilepsy itself** confounds some outcomes. In Denmark, the ASD hazard ratio fell from 2.9 to 1.7 (95% CI 0.9–3.2) when the cohort was restricted to mothers with epilepsy, though childhood autism remained elevated (HR 2.9, 95% CI 1.4–6.0) (PMID:23613074) [V, local cache].

### Protective factors

**Periconceptional folic acid.** The evidence is partial.
- NEAD: higher periconceptional folate use correlated with better cognitive outcomes (tool paraphrase of PMID:23352199).
- Nordic target-trial emulation (all antiseizure medications): "Initiation of high-dose folic acid in the 12 weeks before pregnancy was associated with a reduced risk of MCA in offspring of women using ASMs while initiation in the 12 weeks after pregnancy onset was not." [V] (RR 0.55, 95% CI 0.25–0.91; PMID:41876129). This result is not valproate-specific.
- AAN/AES/SMFM guideline: "Clinicians should prescribe at least 0.4 mg of folic acid supplementation daily preconceptionally and during pregnancy to any PWECP treated with an ASM" [V] (PMID:38748979).
- Folate does not abolish valproate teratogenicity.

**Substitution or dose reduction before conception** is the only reliable prevention (see section 13).

**No protective genetic variants** have been identified in humans.

### Gene–environment interaction

The working model is exposure × maternal one-carbon-metabolism genotype (MTHFR 677C>T), supported by the mouse knock-in model (PMID:40645457) and by familial recurrence (PMID:23167802, PMID:12196666). Placental drug transporter variation has been proposed as a further modifier (PMID:17597651, review).

---

## 3. Phenotypes

Frequencies come from mixed ascertainment. Registry figures are prospective and unbiased. Clinic or support-group series (PMID:10882750, PMID:37666366) over-represent severe cases.

### Craniofacial dysmorphism

Onset is congenital and features are most recognisable in infancy and early childhood. The consensus list (tool summary of PMID:31324220) is: "flat philtrum, thin upper lip, full, everted lower lip, short anteverted nose, small mouth, epicanthic folds, neat arched eyebrows, broad nasal root", plus metopic ridging. In Aberdeen, "52% of exposed children had facial dysmorphism compared with 25% of those not exposed" (all antiepileptics; PMID:11950853) [V].

| Feature | HPO (✓ = cache-verified) |
|---|---|
| Epicanthic folds | HP:0000286 Epicanthus ✓ |
| Thin upper lip | HP:0000219 Thin upper lip vermilion ✓ |
| Full, everted lower lip | HP:0000232 Everted lower lip vermilion ✓; HP:0000179 Thick lower lip vermilion ✓ |
| Flat philtrum | HP:0000319 Smooth philtrum ✓ |
| Short anteverted nose | HP:0003196 Short nose ✓; HP:0000463 Anteverted nares ✓ |
| Broad nasal root/bridge | HP:0000431 Wide nasal bridge ✓ |
| Small mouth | HP:0000160 Narrow mouth ✓ |
| Arched eyebrows | HP:0002553 Highly arched eyebrow ✓ |
| Metopic ridge / trigonocephaly | HP:0005487 Prominent metopic ridge ✓; HP:0000243 Trigonocephaly ✓ |
| Infraorbital groove, medial eyebrow deficiency | by label only (not in cache) |

### Major congenital malformations

Overall MCM prevalence after monotherapy:
- 10.3% (EURAP, PMID:29680205);
- 9.9% (95% CI 8.5–11.5; EURAP update, PMID:38497990);
- 9.2% (31/337; North American registry, PMID:40669027);
- pooled "9.8% (95% CI 8.1 to 11.9) from cohort data" [F] (PMID:37647086).

Specific malformations, from the EUROCAT case-control study of first-trimester monotherapy versus no antiepileptic (PMID:20558369) [F, numbers as returned]:

| Malformation | Odds ratio (95% CI) | HPO |
|---|---|---|
| Spina bifida | 12.7 (7.7–20.7) | HP:0002414 Spina bifida ✓; HP:0002475 Myelomeningocele ✓; HP:0045005 Neural tube defect ✓ |
| Craniosynostosis | 6.8 (CI not returned) | HP:0001363 Craniosynostosis ✓ |
| Cleft palate | 5.2 (2.8–9.9) | HP:0000175 Cleft palate ✓ |
| Hypospadias | 4.8 (2.9–8.1) | HP:0000047 Hypospadias ✓ |
| Atrial septal defect | 2.5 (1.4–4.4) | HP:0001631 Atrial septal defect ✓ |
| Polydactyly | 2.2 (1.0–4.5) | HP:0010442 Polydactyly ✓ (pre/postaxial: HP:0100258 ✓ / HP:0100259 ✓) |

Other reported malformations:
- Radial ray defects (dose-related per the consensus; prenatal case PMID:27809899): HP:0006501 Aplasia/Hypoplasia of the radius ✓; HP:0003974 Absent radius ✓.
- Other cardiac defects: HP:0001629 Ventricular septal defect ✓.
- Renal collecting-system anomalies and hydronephrosis: HP:0000126 ✓.
- Omphalocele: HP:0001539 ✓.
- Coloboma (PMID:24263622, PMID:38411000): HP:0000589 ✓.
- Talipes: HP:0001762 ✓.
- Inguinal hernia: HP:0000023 ✓.
- Overlapping toes: HP:0001845 ✓.

In a review of 69 cases exposed to VPA alone, musculoskeletal abnormalities occurred in 62%, cardiovascular in 26%, and neural tube defects in 3% (tool paraphrase of PMID:11223853; case-literature ascertainment).

### Neurodevelopmental and behavioural phenotypes

These emerge in early childhood, are non-progressive, and are lifelong.

**Reduced IQ, especially verbal.**
- NEAD at age 6: mean IQ 97 for valproate versus 105 (carbamazepine) and 108 (lamotrigine, phenytoin). "Fetal valproate exposure has dose-dependent associations with reduced cognitive abilities across a range of domains at 6 years of age." [F] (PMID:23352199).
- Cochrane: "The IQ of children exposed to VPA (n = 76) was lower than for children born to women without epilepsy (n = 552) (MD -8.94, 95% CI -11.96 to -5.92, P < 0.00001)." [F] (PMID:25354543).
- Clinically confirmed FVS: mean full-scale IQ 19 points below expectation, IQ <70 in 26%, disproportionately low verbal comprehension in 61%, educational intervention in 74% (PMID:30453023) [F].
- HPO: HP:0001249 Intellectual disability ✓; HP:0001328 Specific learning disability ✓; HP:0002354 Memory impairment ✓.

**Language delay or impairment.** In the FACS series, "46 (81%) had speech delay" (60% of the series were exposed to valproate alone; PMID:10882750) [V]. HPO: HP:0000750 Delayed speech and language development ✓; HP:0002463 Language impairment ✓.

**Autism spectrum disorder.**
- Denmark: absolute risk 4.42% for ASD (adjusted HR 2.9, 95% CI 1.7–4.9) and 2.50% for childhood autism (adjusted HR 5.2, 95% CI 2.7–10.0) (PMID:23613074) [V].
- Nordic: 2.7% ASD and 2.4% intellectual disability; adjusted HR 2.4 (1.7–3.3) and 2.5 (1.7–3.7) (PMID:35639399) [F].
- US: cumulative ASD incidence at age 8 of 10.5% with valproate versus 4.2% unexposed among mothers with epilepsy; adjusted HR 2.67 (1.69–4.20) (PMID:38507750) [V].
- Diagnosed FVSD (clinic cohort): 62.9% ASD (PMID:37666366) [F].
- Features: "an even sex ratio, absence of regression or skill loss, and language delay in the absence of global delay" [V] (PMID:16108456).
- HPO: HP:0000717 Autism ✓; HP:0000729 Autistic behavior ✓.

**ADHD.** "Children with prenatal valproate exposure had a 48% increased risk of ADHD (adjusted hazard ratio, 1.48; 95% CI, 1.09-2.00)"; absolute 15-year risk 11.0% versus 4.6% [V] (PMID:30646190). HPO: HP:0007018 ✓.

**Any neurodevelopmental disorder by age 6.** 12.0% with valproate monotherapy versus 1.87% in controls (PMID:23370617) [F].

**Global and motor delay.** "34 (60%) had gross motor delay, and 24 (42%) had fine motor delay" (PMID:10882750) [V]. HPO: HP:0001263 Global developmental delay ✓; HP:0001270 Motor delay ✓.

**Sensory problems.** 80.6% in diagnosed FVSD (PMID:37666366) [F].

### Other medical features

From the FACS series (PMID:10882750) [V] and the consensus statement:
- Joint laxity: "40 (70%) had joint laxity involving all sizes of joints". HPO: HP:0001382 Joint hypermobility ✓.
- Glue ear in 33%. HPO: HP:0000389 Chronic otitis media ✓ / HP:0000403 Recurrent otitis media ✓ (HPO has a more specific effusion term that was not looked up).
- Myopia in 34% of those examined. HPO: HP:0000545 ✓.
- Strabismus (HP:0000486 ✓), pes planus (HP:0001763 ✓), scoliosis (HP:0002650 ✓).
- Laryngomalacia/stridor (HP:0001601 ✓) and tracheomalacia (HP:0002779 ✓).
- Poor bladder control (HP:0000805 Enuresis ✓).
- Neonatal hypotonia (HP:0001252 ✓) and neonatal withdrawal: "Neonatal withdrawal was seen in 20% of those exposed to antiepileptic drugs" [V] (PMID:11950853).

**Growth.** A large Nordic cohort found no association between valproate and small-for-gestational-age birth or microcephaly (PMID:38476755) [V]. This sits awkwardly with the AAN guideline's advice to avoid valproate to reduce small-for-gestational-age risk (PMID:38748979). Do not assert growth restriction as a core feature.

### Quality of life

A qualitative study of 13 young adults with FVSD and their parents reported lifelong physical, cognitive, emotional and social challenges and limited adult services (PMID:38335859; tool paraphrase). In the ConcePTION cohort, 77.6% required formal educational support (PMID:37666366) [F]. No EQ-5D or SF-36 data were found.

---

## 4. Genetic and molecular information

- **Causal genes, pathogenic variants, chromosomal abnormalities:** not applicable. FVS is a teratogenic phenocopy. A normal microarray and Fragile X study are *required* for diagnosis (section 10).
- **Susceptibility or modifier gene:** maternal *MTHFR* 677C>T (see section 2). Evidence is limited, and the association is with maternal genotype, not the child's. If curated, use `relationship_type: SUSCEPTIBILITY` or `MODIFIER`, never `CAUSATIVE`. The HGNC ID was not looked up.
- **Epigenetic information** is the most relevant molecular layer:
  - **Blood episignature.** "a distinct DNA methylation profile was identified in the majority of affected individuals"; the classifier "exhibited high sensitivity and specificity relative to a large reference data set of unaffected controls"; and enrichment "for terms associated with cell adhesion, including significant overrepresentation of the cadherin superfamily" [V/F] (PMID:39097820).
  - **Neonatal methylation.** Longer prenatal antiepileptic exposure was associated with "a decrease in average global methylation" in cord blood [F] (PMID:22419127; all antiepileptics, not valproate-specific).
  - **Phenotypic overlap with chromatinopathies.** "Critically examining the phenotype of FVSD and chromatinopathies, they shared several overlapping features" [F] (PMID:33959609). A case was described as a phenocopy of Kleefstra syndrome (PMID:30151876).

---

## 5. Environmental information

- **Exposure agent.** Valproic acid and its salts (sodium valproate, divalproex/valproate semisodium), taken for epilepsy, bipolar disorder or migraine prophylaxis. Cache-verified terms: CHEBI:39867 valproic acid ✓; CHEBI:60654 valproate ✓; CHEBI:9925 sodium valproate ✓; NCIT:C48029 Valproate Sodium ✓. No valproate exposure term is in the local ECTO cache, so an ECTO lookup is needed before binding.
- **Route.** Maternal oral or intravenous therapy with transplacental transfer. VPA crosses the placenta and reaches elevated fetal concentrations (tool paraphrase of PMID:38203562).
- **Lifestyle factors.** None established. Periconceptional folate status is the only nutritional modifier.
- **Infectious agents.** Not applicable.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Maternal valproate therapy during pregnancy leads to fetal exposure** by placental transfer (demonstrated in humans; PMID:38203562).
2. **VPA directly inhibits class I histone deacetylases in embryonic cells, which results in histone hyperacetylation.** "Valproic acid… acts through a distinct pathway that involves direct inhibition of histone deacetylase (IC(50) for HDAC1 = 0.4 mm)" [V] (PMID:11473107; IN_VITRO).
3. **Hyperacetylation leads to widespread ectopic or mistimed transcription in the embryo.** VPA "also activates transcription from diverse exogenous and endogenous promoters" [V] (PMID:11473107). The teratogenic link is shown in Xenopus and zebrafish: "the teratogenic effects of VPA are very likely mediated specifically by inhibition of HDACs" [V] (PMID:15901671; MODEL_ORGANISM). This step is inferred for humans.
4. **Parallel branch A: VPA impairs folate supply and one-carbon metabolism, which contributes to neural tube closure failure.**
   - "VPA serves as a noncompetitive inhibitor of the high affinity folate receptors" [F] (PMID:25066307; IN_VITRO).
   - "Repeated VPA administration reduced the placental expression of Folr1and Mtr on GD20" [F] (PMID:34293696; rat).
   - The step from reduced folate to human neural tube defects is inferred, and folate supplementation only partly mitigates it.
5. **Parallel branch B: VPA causes a transient oxidising shift in embryonic redox state, which contributes to neural tube defects.** "Embryos treated with VPA exhibited a transiently oxidizing GSH/GSSG Eh"; NRF2 activation reduced open neural tubes [F] (PMID:34737154; mouse).
6. **Dysregulated transcription and aberrant senescence in neuroepithelial cells result in defective neurogenesis.** "we find pronounced induction of cellular senescence in the neuroepithelial (NE) cells… we identified p19Arf as the instrumental mediator of senescence and microcephaly, but, surprisingly, not exencephaly and spinal defects" [V] (PMID:35700169; mouse and human organoids). This shows the structural and brain-growth branches are mechanistically separable.
7. **Altered neural tube cell-junction programmes lead to failed neurulation, which results in spina bifida.** Human spinal cord organoids show changes in cell-junction genes on VPA exposure, with similar defects in mouse embryos (PMID:37643760; tool paraphrase).
8. **Disturbed cranial neural crest formation and migration leads to craniofacial dysmorphism, clefting, and probably cardiac outflow and septal defects.** VPA "reduces the formation/delamination of the midbrain-R1/2 NCCs in a developmental stage-specific manner and subsequently causes the abnormal migration of R4 NCCs", with ectopic *Hoxa2* and reduced *Sox9* [V] (PMID:38403785; rat). Extension to human facial gestalt and heart defects is inferred.
9. **In post-mitotic developing neurons, HDAC and GSK-3 inhibition downregulate dendrite and synapse genes, which leads to impaired dendritic morphogenesis and synapse maturation.** VPA "caused chronic impairment of dendritic morphology and functional properties of developing neurons, but not those of mature neurons… [via] inhibition of the histone deacetylase (HDAC) and glycogen synthase kinase-3 (GSK-3) pathways, which caused transcriptional downregulation of many genes, including MARCKSL1" [V] (PMID:31155484; human IN_VITRO). This explains why exposure late in gestation still harms neurodevelopment.
10. **Region- and lineage-specific neuronal deficits follow.**
    - Loss of brainstem serotonergic differentiation via Hdac1/Notch-dependent silencing of *ascl1b* (PMID:24135485; zebrafish) [V].
    - Fewer cerebellar Purkinje cells: "significantly fewer Purkinje cells in the cerebellar vermis" [F] (PMID:10840175; rat).
    - ASD-overlapping synaptic gene dysregulation in human forebrain organoids: "CAMK4, CLCN4, DPP10, GABRB3, KCNB1, PRKCB, SCN1A, and SLC24A2" [F] (PMID:35351869).
11. **Altered circuit formation results in the clinical neurodevelopmental phenotype:** reduced verbal IQ, language impairment, ASD and ADHD. The link from cellular findings to human cognition is inferred. The human evidence is the dose-dependent epidemiology (PMID:23352199, PMID:23613074, PMID:38507750).
12. **A persistent genome-wide DNA methylation signature remains detectable in blood** (PMID:39097820). It is a biomarker of exposure effect, and its causal role is undetermined.

### Upstream versus downstream

HDAC inhibition and folate antagonism are the upstream molecular initiating events. Senescence, neural crest disruption and dendritic-gene downregulation are intermediate cellular events. Malformations and neurodevelopmental disorder are the outcomes.

### Checklist coverage

- **Molecular pathways.** HDAC/chromatin; Wnt/GSK-3 ("valproic acid activates Wnt dependent gene expression", PMID:11473107); Notch (PMID:24135485); CBP/p300 and Akt ("Cbp, p300 and Akt mRNA levels were downregulated at 1 and 3 h post-exposure in GD9 embryos" [F], PMID:32445665); folate/one-carbon/SAMe (PMID:38203562, PMID:32375098); NRF2/redox (PMID:34737154).
- **Cellular processes.** Senescence, impaired neurogenesis, altered neural crest epithelial–mesenchymal transition and migration, dendritic and synaptic maturation.
- **Protein dysfunction.** Pharmacological enzyme inhibition (HDAC1 and class I HDACs); no misfolding.
- **Immune involvement.** None established in humans.
- **Molecular profiling.** Blood methylation episignature (PMID:39097820); organoid transcriptomics (PMID:35351869, PMID:37643760). No human proteomic, metabolomic or lipidomic signatures were found.
- **Functional genomics screens.** None found.

### Suggested ontology terms

- **GO biological process (✓ cache-verified):** GO:0001843 neural tube closure; GO:0001755 neural crest cell migration; GO:0090398 cellular senescence; GO:0022008 neurogenesis; GO:0061351 neural precursor cell proliferation; GO:0048813 dendrite morphogenesis; GO:0006338 chromatin remodeling; GO:0060070 canonical Wnt signaling pathway; GO:0046655 folic acid metabolic process; GO:0006730 one-carbon metabolic process; GO:0006979 response to oxidative stress.
- **GO terms needing lookup (by label only):** histone deacetylase activity (molecular function); synapse maturation; serotonergic neuron differentiation; folate transport.
- **Cell types (✓):** CL:0002259 neuroepithelial stem cell; CL:0011012 neural crest cell; CL:0011020 neural progenitor cell; CL:0000681 radial glial cell; CL:0000850 serotonergic neuron; CL:0000121 Purkinje cell.
- **Modifier guidance.** HDAC activity is `DECREASED` (drug inhibition, quantitative). `functional_impact_category` is not applicable because there is no variant.

---

## 7. Anatomical structures affected

- **Primary organs and systems.**
  - Central nervous system: neural tube and spinal cord, forebrain, cerebellum, brainstem.
  - Craniofacial skeleton and palate.
  - Heart (septa).
  - Genitourinary tract (urethra, renal collecting system).
  - Limbs (radial ray, digits).
  - Cranial sutures (metopic).
- **Secondary involvement.** Joints and connective tissue (laxity), eye (myopia, strabismus, coloboma), middle ear, airway (laryngo- and tracheomalacia), abdominal wall.
- **UBERON (✓ cache-verified):** UBERON:0001049 neural tube; UBERON:0002037 cerebellum; UBERON:0001987 placenta (site of transfer and folate transport). Other sites (spinal cord, heart, secondary palate, radius, metopic suture, cerebral cortex) are suggested by label only.
- **Subcellular.** Nucleus and chromatin (histone acetylation). The GO cellular-component term was not looked up.
- **Lateralisation.** Not systematically described. Limb defects may be unilateral (right-sided radial ray defect in PMID:27809899).

---

## 8. Temporal development

- **Onset.** Congenital (prenatal). Malformations are detectable prenatally or at birth. Neurodevelopmental features declare themselves between about 18 months and school age. Mean age at autism diagnosis in the Aberdeen cohort was 5 years 4 months (PMID:16108456).
- **Critical periods.**
  - Neurulation, around days 21–28 post-conception, for neural tube defects.
  - The first trimester for other structural malformations (PMID:20558369).
  - The second half of pregnancy for neurodevelopment (PMID:38507750). Human neurons are vulnerable while immature but not when mature (PMID:31155484).
  - In rodents, a single dose at E12.5 produces the autism-like phenotype (PMID:15238991).
- **Course.** Static, non-progressive and lifelong, with no remission. Facial features become less distinctive with age (stated in the consensus literature; not directly quoted here). The burden shifts from malformation surgery in infancy to educational, behavioural and musculoskeletal needs later.
- **Suggested `progression:` phases.** Prenatal (exposure and organogenesis); neonatal (malformations, withdrawal, hypotonia); childhood (developmental and behavioural presentation); adolescence and adulthood (persistent cognitive and social disability).

---

## 9. Inheritance and population

- **Inheritance.** Not inherited. No Mendelian pattern, penetrance class, anticipation, founder effect or carrier frequency applies. Familial recurrence reflects repeated exposure plus maternal susceptibility.
- **Risk given exposure** (the practical analogue of penetrance). About 10% major malformation (PMID:37647086). The frequently cited 30–40% neurodevelopmental impairment figure comes from regulatory summaries (EMA/MHRA) and was not retrieved here. The consensus statement gives developmental delay "in the region of 30%" (tool summary of PMID:31324220).
- **Registered birth prevalence.** "Data from 15 European congenital anomaly registries identified 28 cases of valproate syndrome in 2.74 million births from 2005 to 2014. The prevalence of valproate syndrome in Europe significantly decreased from 0.22 per 10,000 births in 2005/6 to 0.03 per 10,000 births in 2013/14." [V] (PMID:29753923).
  - This converts to about 2.2 per 100,000 births, falling to 0.3 per 100,000.
  - For the knowledge base: `measure_type: BIRTH_PREVALENCE`, `rate_denominator: LIVE_BIRTHS` (the registries count births; check whether they include stillbirths and terminations).
  - This is a registered-diagnosis rate and an underestimate. With about 10% malformation risk among exposed pregnancies, true incidence tracks valproate prescribing in pregnancy.
  - One registry, Île de la Réunion, contributed 17 of the 28 cases.
- **Orphanet prevalence class.** Not retrieved.
- **Sex ratio.** ASD associated with fetal anticonvulsant exposure shows "an even sex ratio" (PMID:16108456), unlike idiopathic ASD. No overall sex bias is established.
- **Geography.** Tracks prescribing practice. Prevalent valproate use in women of childbearing age fell after 2018 in Tuscany, Spain and the UK (PMID:37294532). Case reports continue from India, Türkiye, Crimea and Japan (PMID:28003925, PMID:31831992, PMID:27809899).

---

## 10. Diagnostics

**FVS is a clinical diagnosis of exclusion.** No laboratory test is diagnostic.

**Consensus criteria** (tool summary of PMID:31324220; verify against the full text, PMC6642533). All essential criteria are required:
- confirmed VPA exposure during pregnancy;
- no other recognisable diagnosis explaining the phenotype;
- "Normal microarray-CGH and Fragile X studies";
- other overlapping teratogenic disorders excluded.

In addition, the diagnosis needs two "suggestive" criteria, or one suggestive criterion plus a supportive-feature score of at least 3. Suggestive and supportive features draw on the facial gestalt, characteristic malformations and neurodevelopmental profile; laryngomalacia/stridor is a scored supportive item.

**Genetic testing.** Chromosomal microarray and *FMR1* (Fragile X) testing are mandatory exclusions. Exome or genome sequencing is useful for the differential diagnosis, especially chromatinopathies (PMID:33959609, PMID:30151876). Genetic investigation of the mother's epilepsy is advised. Karyotype, FISH, mitochondrial and repeat-expansion testing have no specific role beyond Fragile X.

**Omics biomarker.** The peripheral-blood DNA methylation episignature (PMID:39097820) is the first candidate objective biomarker. It is not yet standard of care.

**Prenatal imaging.** Detailed ultrasound at about 13 and 20 weeks with the sonographer informed of exposure (consensus). Reported prenatal findings include radial ray defect, growth restriction and saddle nose (PMID:27809899) and nuchal oedema (PMID:12224082).

**Postnatal work-up** (consensus):
- palate and limb examination;
- one-off renal tract ultrasound and echocardiogram;
- ophthalmology within 6 months;
- hip assessment;
- hearing assessment;
- neuropsychological assessment of IQ, language, memory, attention and executive function;
- ASD screening at about 18 months;
- Beighton score for joint hypermobility.

**Differential diagnosis.**
- Fetal alcohol spectrum disorder.
- Other fetal anticonvulsant syndromes (hydantoin, carbamazepine).
- Chromatinopathies (Kleefstra syndrome and others).
- Fragile X syndrome.
- Microdeletion syndromes.
- Genetic syndromes with trigonocephaly or radial ray defects (not individually sourced here).

**Screening.** No newborn or carrier screening applies. Risk identification is by medication history.

**Diagnostic complexity.** "Establishing or Excluding a Diagnosis of Fetal Valproate Spectrum Disorder is a Multi-layered Process" (title, PMID:35863137).

---

## 11. Outcome and prognosis

- **Mortality.** Not well quantified. A historical literature review of 69 cases reported 12% infant mortality (PMID:11223853; tool paraphrase), which reflects severe case reports and is not representative. No contemporary life-expectancy data were found. Mortality relates to severe malformations.
- **Disability.** Cognitive and social disability is the main long-term burden.
  - Cochrane: "The most important finding is the reduction in IQ in the VPA exposed group, which are sufficient to affect education and occupational outcomes in later life." [F] (PMID:25354543).
  - Diagnosed FVSD (ages 7–37): "significantly higher levels of moderate (43.4%) and severe (14.4%) cognitive impairment" and "high levels of required formal educational support (77.6%)" [F] (PMID:37666366).
- **Adult outcomes.** Persisting needs with poor transition to adult services (PMID:38335859). The consensus recommends a designated GP, annual health checks, and weight, vision and hearing surveillance.
- **Prognostic factors.** Dose is the main one; higher doses give more malformations and lower IQ. Polytherapy, the presence of major malformations, and possibly periconceptional folate also matter.
- **Complications.** Sequelae of spina bifida (neurogenic bladder, hydrocephalus, mobility), surgical morbidity, mental-health comorbidity, joint pain and fatigue.
- **Recovery.** No reversal. Function improves with early educational and therapy support. No controlled outcome data exist: the consensus notes that "information regarding management is currently lacking in the medical literature" [F] (PMID:31324220).

---

## 12. Treatment

No disease-modifying therapy exists. Management is multidisciplinary, symptomatic and consensus-based (PMID:31324220: "affected individuals benefit from the input of a number of different health professionals" [F]).

| Intervention | Indication | NCIT (✓ = cache-verified) | Suggested modality |
|---|---|---|---|
| Surgical repair (spina bifida closure, cleft palate repair, hypospadias repair, craniosynostosis surgery, cardiac repair, limb surgery) | Structural malformations | NCIT:C15329 Surgical Procedure ✓ (more specific procedure terms need lookup) | SURGERY |
| Speech and language therapy | Language delay or impairment; refer if delayed by 2.5 years | by label only (`NCIT:C159273` is quoted in CLAUDE.md, not verified here) | BEHAVIORAL |
| Occupational therapy | Fine motor and hand function; ergonomic assessment | NCIT:C121351 Occupational Therapy ✓ | BEHAVIORAL |
| Physiotherapy, podiatry and orthotics | Joint laxity, fatigue, posture, foot deformity | NCIT:C15302 Physical Therapy ✓ | BEHAVIORAL (orthotics: DEVICE) |
| Special educational support (individualised plan, exam accommodations) | Cognitive and learning difficulties | by label only | BEHAVIORAL |
| Standard ASD and ADHD management, including stimulant medication | ASD, ADHD | NCIT:C15986 Pharmacotherapy ✓ with `therapeutic_agent` | SMALL_MOLECULE |
| Corrective lenses; grommets | Myopia; glue ear | lookup needed | DEVICE / SURGERY |
| Genetic counselling and reproductive advice for the mother | Recurrence prevention | NCIT:C15240 Genetic Counseling ✓ | BEHAVIORAL |

- **Evidence caveat.** No trial evaluates any intervention specifically in FVS; support is extrapolated from the general condition. Recording that as a `KNOWLEDGE_GAP` discussion would be accurate.
- **Advanced therapeutics** (gene, cell, RNA, targeted, immunotherapy): none.
- **Pharmacogenomics.** None applicable to the child. Maternal MTHFR genotype is a research-level risk marker only.
- **Experimental treatments.** No registered interventional trials for FVS were identified in this search, though ClinicalTrials.gov was not queried directly. Preclinical rescue studies exist only in the rodent VPA autism model, for example N-acetylcysteine (PMID:35280167) and AMPA receptor modulation (PMID:29899405). These are not candidates for human use at present.
- **Breastfeeding.** Encouraged by the consensus statement, which considers VPA compatible with nursing (also the tool paraphrase of PMID:38203562).

---

## 13. Prevention

FVS is entirely preventable by avoiding fetal exposure.

**Primary prevention: avoid valproate in people who could become pregnant.**
- AAN/AES/SMFM 2024: "Clinicians must avoid the use of valproic acid in PWECP to minimize the risk of MCMs or neural tube defects (NTDs), if clinically feasible" and "To reduce the risk of poor neurodevelopmental outcomes, including autism spectrum disorder and lower IQ, in children born to PWECP, clinicians must avoid the use of valproic acid in PWECP, if clinically feasible." [V] (PMID:38748979).
- Preferred alternatives: "Clinicians must consider using lamotrigine, levetiracetam, or oxcarbazepine in PWECP when appropriate" [V] (PMID:38748979). Their malformation rates are 2.5–3.1% versus 9.9% for valproate (PMID:38497990).
- Changes should be made before conception: "Once a PWECP is already pregnant, clinicians should exercise caution in attempting to remove or replace an ASM that is effective in controlling generalized tonic-clonic or focal-to-bilateral tonic-clonic seizures." [V] (PMID:38748979).
- If valproate is unavoidable, use the lowest effective dose (dose-response in PMID:29680205).

**Regulatory programmes.** EU doctors "are now advised not to prescribe valproate in pregnant women, in women who can become pregnant or in girls unless other treatments are ineffective or not tolerated" [V] (PMID:29753923). The effect of the 2018 EU Pregnancy Prevention Programme was partial: prevalent use declined, but contraceptive coverage stayed below 25% and "a substantial number of concurrent pregnancies during valproate exposure" persisted [F] (PMID:37294532). EUROCAT documented falling registered FVS prevalence from 2005 to 2014 (PMID:29753923).

**Folic acid.** At least 0.4 mg/day preconceptionally and during pregnancy (PMID:38748979). High-dose (4–5 mg) folic acid started in the 12 weeks before pregnancy was associated with fewer malformations across antiseizure medications (PMID:41876129). The consensus statement advises folic acid from 2–3 months before conception to 12 weeks, and does not support high doses after the first trimester. Cache-verified: CHEBI:27470 folic acid ✓; NCIT:C510 Folic Acid ✓.

**Secondary prevention.** Joint obstetric–neurology care, targeted fetal anomaly ultrasound, and structured postnatal surveillance (section 10).

**Tertiary prevention.** Early developmental intervention and regular vision, hearing and musculoskeletal review.

**Counselling.** Preconception counselling for everyone of childbearing potential on valproate. Recurrence counselling after an affected child is important: 16.8% malformation recurrence, and 50% after two affected children (PMID:23167802).

**Paternal use.** Current best evidence does not support a paternal effect (PMID:41733407). Some regulators still advise precaution.

**Immunisation.** Not applicable.

---

## 14. Other species and natural disease

- There is no naturally occurring veterinary disease. FVS is iatrogenic and human-specific in practice. Zoonosis, transmission and breed data are not applicable.
- **Cross-species susceptibility** is high and conserved. VPA is teratogenic in mouse, rat, zebrafish, Xenopus, chick and marmoset (PMID:15901671, PMID:34923091, PMID:36035018), consistent with conserved HDAC targets.
- **Taxa used experimentally** (NCBITaxon IDs by label only): *Mus musculus*, *Rattus norvegicus*, *Danio rerio*, *Xenopus laevis*, *Callithrix jacchus*.

---

## 15. Model organisms

All are induced (chemical exposure) models. No genetic model is needed, apart from susceptibility backgrounds.

| Model | Protocol and findings | Recapitulates | Limitations | PMID |
|---|---|---|---|---|
| Rat, prenatal VPA (autism model) | Single dose around E12.5; reduced social behaviour, stereotypy, sensory changes, delayed maturation | Behavioural and neurodevelopmental phenotype | Single high bolus (600 mg/kg) versus chronic human dosing; used mainly as an idiopathic autism model | PMID:15238991 [V]; PMID:28472621; PMID:37873949 |
| Rat cerebellum | "significantly fewer Purkinje cells in the cerebellar vermis" after 600 mg/kg at E12.5 | Neuroanatomical correlate | Human correlate is from autism, not FVS, neuropathology | PMID:10840175 |
| Mouse neural tube defect model (CD-1 and others) | Exencephaly after exposure around E7.5–E9; redox shift, Cbp/p300/Akt changes; NRF2 rescue | Neural tube defect | Mouse gets exencephaly, human gets lumbosacral spina bifida, so the affected axial level differs | PMID:34737154; PMID:32445665 |
| Mouse and human organoid senescence model | p19Arf-dependent neuroepithelial senescence leading to microcephaly | Reduced brain growth and neurogenesis | Microcephaly is not a consistent human feature (PMID:38476755) | PMID:35700169 |
| *Mthfr* 677C>T knock-in mouse | Higher VPA malformation rate in CT and TT animals | Gene–environment susceptibility | Single 400 mg/kg intraperitoneal dose | PMID:40645457 |
| Rat cranial neural crest | Reduced crest formation, ectopic *Hoxa2*, abnormal migration | Craniofacial dysmorphism mechanism | Short-term embryonic readouts only | PMID:38403785 |
| Zebrafish | Hdac1/Notch-dependent *ascl1b* silencing and loss of serotonergic neurons; HDAC-inhibitor-like malformations | Molecular mechanism; morphology and behaviour in one assay | Non-mammalian; waterborne exposure | PMID:24135485 [V]; PMID:15901671 |
| *Xenopus laevis* (R-FETAX) | Window-specific neural tube, facial and tail defects plus swimming deficits at therapeutic concentrations | Both malformation and behavioural arms | Amphibian development | PMID:34923091 [V] |
| Marmoset | Prenatal VPA; ASD-like behaviour, brain pathology, raised cortisol | Primate social behaviour and HPA axis | Few animals; costly | PMID:36035018 [V] |
| Human forebrain organoids | VPA alters synaptic and neurodevelopmental genes overlapping ASD brain signatures | Human transcriptional response | No circuit or behavioural readout | PMID:35351869 |
| Human spinal cord organoids | Neural-tube-like morphogenesis defects; cell-junction gene changes | Human neurulation | In vitro | PMID:37643760 |
| Human induced neurons | Stage-restricted dendritic and synaptic impairment via HDAC/GSK-3 and *MARCKSL1* | Late-gestation neuronal vulnerability | Reductionist | PMID:31155484 [V] |

**Curation notes.**
- Animal models belong in `animal_models:`. Organoids and induced neurons belong in `experimental_models:`.
- The rodent "VPA autism model" literature is mostly designed to study idiopathic autism. Link it with `PARTIALLY_RECAPITULATES` and a `limitations` note on the dosing mismatch.
- The mouse exencephaly versus human spina bifida difference is a candidate `HUMAN_MODEL_MISMATCH` discussion.
- A transgenerational effect was reported in mice (PMID:27819277) and discussed in human reports (PMID:34866359). This is unconfirmed in humans.

---

## Evidence-source summary for key citations

| PMID | Study | `evidence_source` |
|---|---|---|
| 31324220 | ERN-ITHACA consensus statement | OTHER (consensus/review; `quote_role: REVIEW_SYNTHESIS`) |
| 29680205, 38497990, 40669027, 23167802 | Pregnancy registries | HUMAN_CLINICAL |
| 20558369, 29753923 | EUROCAT studies | HUMAN_CLINICAL |
| 23613074, 30646190, 35639399, 38507750, 41733407, 41876129, 38476755 | Population cohorts | HUMAN_CLINICAL |
| 23352199, 23370617, 10882750, 11950853, 16108456, 30453023, 37666366, 38335859 | Clinical cohorts and series | HUMAN_CLINICAL |
| 37647086, 25354543 | Cochrane reviews | HUMAN_CLINICAL (meta-analysis) |
| 38748979 | AAN/AES/SMFM guideline | OTHER |
| 39097820, 22419127, 17853476, 17951123, 10563481 | Human molecular and genetic studies | HUMAN_CLINICAL |
| 11473107, 25066307, 31155484, 35351869, 37643760 | Cell and organoid studies | IN_VITRO |
| 15901671, 35700169, 34737154, 32445665, 40645457, 38403785, 24135485, 34923091, 36035018, 15238991, 10840175, 34293696 | Animal studies (35700169 also includes organoids; split items) | MODEL_ORGANISM |
| 38203562, 33959609, 32375098, 28472621, 37873949 | Narrative reviews | OTHER / REVIEW_SYNTHESIS |

## Gaps and items to verify before curation

1. **Orphanet (ORPHA:1906).** Definition, prevalence class and HPO frequency table were not retrieved. Build with `just structured-rebuild-orphanet --id 1906`.
2. **Foundational descriptions.** DiLiberti 1984 (PMID:6439041) and Clayton-Smith 1995 (PMID:8544193) returned no abstract text.
3. **Rodier 1996 thalidomide/VPA brainstem paper.** PMID not confirmed, so it is not cited.
4. **Regulatory neurodevelopmental figure and paternal-exposure warning.** The 30–40% figure and the 2024 EMA/MHRA paternal warning need a primary citation.
5. **Preflight.** Run `just preflight-dr <report> MONDO:0012275` and the reference validation before using any content from this report.
6. **Conflicting evidence to keep separate.** Fetal growth restriction (PMID:38476755 versus PMID:38748979); the child's versus the mother's MTHFR genotype; whether microcephaly is a feature.

## Sources

- [PMID:31324220 Clayton-Smith 2019, FVSD consensus (Orphanet J Rare Dis; PMC6642533)](https://pubmed.ncbi.nlm.nih.gov/31324220/)
- [PMID:6439041 DiLiberti 1984](https://pubmed.ncbi.nlm.nih.gov/6439041/) · [PMID:8544193 Clayton-Smith 1995](https://pubmed.ncbi.nlm.nih.gov/8544193/)
- [PMID:10882750 Moore 2000](https://pubmed.ncbi.nlm.nih.gov/10882750/) · [PMID:11950853 Dean 2002](https://pubmed.ncbi.nlm.nih.gov/11950853/) · [PMID:16108456 Rasalam 2005](https://pubmed.ncbi.nlm.nih.gov/16108456/)
- [PMID:11223853 Kozma 2001](https://pubmed.ncbi.nlm.nih.gov/11223853/) · [PMID:12196666 Malm 2002](https://pubmed.ncbi.nlm.nih.gov/12196666/) · [PMID:15669094 Schorry 2005](https://pubmed.ncbi.nlm.nih.gov/15669094/)
- [PMID:20558369 Jentink 2010, NEJM](https://pubmed.ncbi.nlm.nih.gov/20558369/) · [PMID:29680205 Tomson 2018, EURAP](https://pubmed.ncbi.nlm.nih.gov/29680205/) · [PMID:38497990 Battino 2024](https://pubmed.ncbi.nlm.nih.gov/38497990/) · [PMID:40669027 Hernandez-Diaz 2025](https://pubmed.ncbi.nlm.nih.gov/40669027/)
- [PMID:37647086 Bromley 2023, Cochrane](https://pubmed.ncbi.nlm.nih.gov/37647086/) · [PMID:25354543 Bromley 2014, Cochrane](https://pubmed.ncbi.nlm.nih.gov/25354543/)
- [PMID:23352199 Meador 2013, NEAD](https://pubmed.ncbi.nlm.nih.gov/23352199/) · [PMID:23370617 Bromley 2013](https://pubmed.ncbi.nlm.nih.gov/23370617/) · [PMID:23613074 Christensen 2013, JAMA](https://pubmed.ncbi.nlm.nih.gov/23613074/)
- [PMID:30646190 Christensen 2019](https://pubmed.ncbi.nlm.nih.gov/30646190/) · [PMID:35639399 Bjørk 2022](https://pubmed.ncbi.nlm.nih.gov/35639399/) · [PMID:38507750 Hernández-Díaz 2024, NEJM](https://pubmed.ncbi.nlm.nih.gov/38507750/)
- [PMID:30453023 Bromley 2019](https://pubmed.ncbi.nlm.nih.gov/30453023/) · [PMID:37666366 Bluett-Duncan 2023](https://pubmed.ncbi.nlm.nih.gov/37666366/) · [PMID:38335859 Khanom 2024](https://pubmed.ncbi.nlm.nih.gov/38335859/)
- [PMID:38476755 Christensen 2024, fetal growth](https://pubmed.ncbi.nlm.nih.gov/38476755/) · [PMID:38748979 Pack 2024, AAN/AES/SMFM guideline](https://pubmed.ncbi.nlm.nih.gov/38748979/)
- [PMID:41876129 Sun 2026, folic acid](https://pubmed.ncbi.nlm.nih.gov/41876129/) · [PMID:41733407 Meng 2026, paternal valproate](https://pubmed.ncbi.nlm.nih.gov/41733407/)
- [PMID:29753923 Morris 2018, EUROCAT prevalence](https://pubmed.ncbi.nlm.nih.gov/29753923/) · [PMID:23167802 Campbell 2013, recurrence](https://pubmed.ncbi.nlm.nih.gov/23167802/) · [PMID:37294532 Abtahi 2023, pregnancy prevention programme](https://pubmed.ncbi.nlm.nih.gov/37294532/)
- [PMID:17853476 Dean 2007](https://pubmed.ncbi.nlm.nih.gov/17853476/) · [PMID:17951123 Kini 2007](https://pubmed.ncbi.nlm.nih.gov/17951123/) · [PMID:10563481 Dean 1999](https://pubmed.ncbi.nlm.nih.gov/10563481/) · [PMID:17597651 Atkinson 2007](https://pubmed.ncbi.nlm.nih.gov/17597651/) · [PMID:40645457 Yang 2025](https://pubmed.ncbi.nlm.nih.gov/40645457/)
- [PMID:39097820 Haghshenas 2024, episignature](https://pubmed.ncbi.nlm.nih.gov/39097820/) · [PMID:22419127 Smith 2012](https://pubmed.ncbi.nlm.nih.gov/22419127/) · [PMID:33959609 Parodi 2021](https://pubmed.ncbi.nlm.nih.gov/33959609/) · [PMID:30151876 Arora 2018](https://pubmed.ncbi.nlm.nih.gov/30151876/)
- [PMID:11473107 Phiel 2001](https://pubmed.ncbi.nlm.nih.gov/11473107/) · [PMID:15901671 Gurvich 2005](https://pubmed.ncbi.nlm.nih.gov/15901671/) · [PMID:35700169 Rhinn 2022](https://pubmed.ncbi.nlm.nih.gov/35700169/) · [PMID:31155484 Chanda 2019](https://pubmed.ncbi.nlm.nih.gov/31155484/)
- [PMID:25066307 Fathe 2014](https://pubmed.ncbi.nlm.nih.gov/25066307/) · [PMID:34293696 Furugen 2021](https://pubmed.ncbi.nlm.nih.gov/34293696/) · [PMID:32375098 Reynolds 2020](https://pubmed.ncbi.nlm.nih.gov/32375098/) · [PMID:34737154 Piorczynski 2022](https://pubmed.ncbi.nlm.nih.gov/34737154/) · [PMID:32445665 Shafique 2020](https://pubmed.ncbi.nlm.nih.gov/32445665/)
- [PMID:38403785 Suzuki 2024](https://pubmed.ncbi.nlm.nih.gov/38403785/) · [PMID:35351869 Meng 2022](https://pubmed.ncbi.nlm.nih.gov/35351869/) · [PMID:37643760 Lee 2023](https://pubmed.ncbi.nlm.nih.gov/37643760/) · [PMID:38203562 Ornoy 2023](https://pubmed.ncbi.nlm.nih.gov/38203562/)
- [PMID:15238991 Schneider 2005](https://pubmed.ncbi.nlm.nih.gov/15238991/) · [PMID:10840175 Ingram 2000](https://pubmed.ncbi.nlm.nih.gov/10840175/) · [PMID:28472621 Nicolini 2018](https://pubmed.ncbi.nlm.nih.gov/28472621/) · [PMID:37873949 Zarate-Lopez 2024](https://pubmed.ncbi.nlm.nih.gov/37873949/)
- [PMID:24135485 Jacob 2014](https://pubmed.ncbi.nlm.nih.gov/24135485/) · [PMID:34923091 Battistoni 2022](https://pubmed.ncbi.nlm.nih.gov/34923091/) · [PMID:36035018 Nakamura 2022](https://pubmed.ncbi.nlm.nih.gov/36035018/) · [PMID:27819277 Choi 2016](https://pubmed.ncbi.nlm.nih.gov/27819277/) · [PMID:34866359 Martin 2022](https://pubmed.ncbi.nlm.nih.gov/34866359/)
- [PMID:27809899 Kikuchi 2016](https://pubmed.ncbi.nlm.nih.gov/27809899/) · [PMID:12224082 Witters 2002](https://pubmed.ncbi.nlm.nih.gov/12224082/) · [PMID:35863137 Kalim 2021](https://pubmed.ncbi.nlm.nih.gov/35863137/) · [PMID:24263622 Shah 2014](https://pubmed.ncbi.nlm.nih.gov/24263622/) · [PMID:38411000 Moutafi 2024](https://pubmed.ncbi.nlm.nih.gov/38411000/)
- [PMID:28003925 Goyal 2016](https://pubmed.ncbi.nlm.nih.gov/28003925/) · [PMID:31831992 Rybalko 2019](https://pubmed.ncbi.nlm.nih.gov/31831992/) · [PMID:35280167 Schiavi 2022](https://pubmed.ncbi.nlm.nih.gov/35280167/) · [PMID:29899405 Kim 2019](https://pubmed.ncbi.nlm.nih.gov/29899405/)
- [MONDO:0012275 record (EBI OLS)](https://www.ebi.ac.uk/ols4/api/terms?obo_id=MONDO:0012275&ontology=mondo)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 72 |
| Resolved | 71 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 71 |
| On topic | 54 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:35639399` (4 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 86 |
| Resolved | 85 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

85 of 86 terms resolved to a current term; the rest could not be looked up either way.