---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T12:17:53.484907'
end_time: '2026-10-08T12:24:18.741945'
duration_seconds: 385.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia 46
  mondo_id: MONDO:0033481
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
  web_search_requests: 7
  num_turns: 38
  total_cost_usd: 2.5768047
  session_id: 3e33c2f6-0f4c-4629-b1d9-fa1f071527a7
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 4
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
citation_count: 18
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 10
  verified: 8
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0080288
    reported_labels:
    - DOID
    ontology_label: spinocerebellar ataxia 46
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia 46
- **MONDO ID:** MONDO:0033481 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia 46** covering all of the
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

Reading the cached Nibbeling 2017 abstract and a 2024 review that mentions PLD3, then searching the literature on the dispute and on PLD3 biology.

Pulling verbatim abstracts for the key PMIDs so the report can quote them exactly.

Checking ClinGen's record for PLD3 and the original paper's family details, then I'll write the report.

# Spinocerebellar ataxia 46 (SCA46; PLD3): research report

**Compiled:** 2026-10-08 · **Target:** MONDO:0033481 · **Category:** Mendelian (autosomal dominant)

## Summary for curation

- **The disease rests on one family.** SCA46 is defined by a single Dutch kindred carrying the heterozygous PLD3 missense variant c.923T>C, p.Leu308Pro (Nibbeling et al. 2017, PMID:29053796). The same kindred had been described clinically in 1995 as a dominant sensory ataxic neuropathy (van Dijk et al. 1995, PMID:8595484). No second family with segregation has been published. The only other report is a single Indian patient with a different PLD3 variant and an atypical phenotype (PMID:38059248).
- **The gene–disease link is provisional and disputed.** OMIM lists the entry with a question mark (?SCA46, #617770). ClinGen has no published gene–disease validity curation for PLD3. GenCC aggregators show Limited and Supportive assertions. Gonzalez et al. (2018) reported that Pld3 knockout mice show no cerebellar degeneration or ataxia, and that PLD3 expression is lowest in the adult cerebellum (PMID:30312375). The original group replied defending the variant (PMID:30312384).
- **PLD3 is a lysosomal enzyme, not a phospholipase in the classic sense.** It is a lysosomal 5′ exonuclease that breaks down single-stranded DNA and RNA (PMID:30111894, 34620855, 33288674). Its main physiological substrate is mitochondrial DNA (PMID:37225734). It also synthesizes the lysosomal lipid S,S-BMP (PMID:39423811). The L308P protein is held in the ER, poorly processed, and has lost exonuclease activity (Gonzalez 2018 letter). How this produces cerebellar or sensory-neuron degeneration has not been shown.
- **For dismech:** the mechanism should be recorded as loss of function with an inferred downstream chain. The disputed gene–disease validity should be stated openly, for example in a `discussions` entry of kind `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH`. There is no ClinGen tier to copy into `gene_disease_validity`.

---

## 1. Disease information

**Overview.** SCA46 is a rare autosomal dominant, slowly progressive, late-onset ataxia. It mixes cerebellar ataxia with sensory axonal neuropathy in varying proportions. Dysarthria and oculomotor abnormalities are common, and cerebellar atrophy on MRI is absent or mild.

- van Dijk 1995: *"We describe a Dutch family with sensory ataxia in two generations"* (PMID:8595484).
- Sowmini 2023: *"SCA 46 is a rare autosomal dominant ataxia initially described in a Dutch family"* (PMID:38059248).

| Identifier | Value | Source |
|---|---|---|
| MONDO | MONDO:0033481 "spinocerebellar ataxia 46" | MedGen / draft entry |
| OMIM (phenotype) | #617770 (provisional, "?SCA46") | MedGen; [LOVD](https://databases.lovd.nl/shared/diseases/06427) |
| OMIM (gene) | *615698 PLD3 | [GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4540404) |
| Orphanet | ORPHA:589522 | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1624251) |
| UMLS | C4540404 | MedGen |
| DOID | DOID:0080288 | [GlyCosmos](https://glycosmos.org/diseases/DOID:0080288) |
| HGNC | hgnc:17158 (PLD3) | [ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:17158) |
| ICD-10 / ICD-11 | No specific code. It falls under the hereditary ataxia codes (ICD-10 G11.x). Not verified. | — |

**Synonyms:** SCA46; "spinocerebellar ataxia, 46, autosomal dominant, with sensory axonal neuropathy"; "spinocerebellar ataxia with sensory axonal neuropathy". PLD3 gene aliases include AD19, HU-K4 and HUK4 (GTR).

**Data provenance:** aggregated disease-level resources (OMIM, Orphanet, MedGen) built on a single published pedigree and one case report.

## 2. Etiology

- **Cause:** germline heterozygous PLD3 c.923T>C, p.Leu308Pro (chr19:40880431, hg19). The variant lies in the second phosphodiesterase (HKD) domain. SIFT, PolyPhen-2 and MutationTaster all predict it to be damaging, and it was absent from 1000 Genomes and ExAC. It segregated with disease: present in 8 affected relatives and absent in 3 unaffected relatives. One relative with mild complaints did not carry it. Screening 96 further index patients found no additional PLD3 variants (Nibbeling 2017, full text).
- **Environmental risk factors:** none reported.
- **Protective factors:** none reported.
- **Gene–environment interactions:** none reported.
- **Related PLD3 associations (separate diseases; do not merge with SCA46):**
  - Late-onset Alzheimer's disease risk. Cruchaga 2014: *"A rare variant in PLD3 (phospholipase D3; Val232Met) segregated with disease status in two independent families"* and *"doubled risk for Alzheimer's disease in seven independent case-control series"* (PMID:24336208). Later replication was inconsistent.
  - A homozygous nonsense variant, p.Y62X (c.186C>G), was reported in a consanguineous family with leukoencephalopathy, hearing and vision loss, and kidney disease. Liu 2021: *"homozygous mutation of PLD3 may result in a novel leukoencephalopathy syndrome"* (PMID:34267643).

## 3. Phenotypes

Main source: the Nibbeling 2017 family (Table 2), cross-checked against the MedGen/HPO annotation list. No penetrance or frequency figures beyond this single family exist.

| Phenotype | Type | Frequency in the family | Notes | Suggested HPO (CURIE must be verified by lookup) |
|---|---|---|---|---|
| Progressive gait ataxia (mixed sensory and cerebellar; gait affected more than limbs) | Sign | All affected | Slowly progressive | Gait ataxia; Progressive cerebellar ataxia (HP:0002073 is already in the draft) |
| Limb ataxia / dysmetria | Sign | Most | — | Limb ataxia; Dysmetria |
| Sensory axonal neuropathy | Sign / electrophysiology | Variable, mild to predominant | 1995 report: *"axonal degeneration of myelinated nerve fibres in four of five investigated siblings"* | Sensory axonal neuropathy |
| Distal loss of vibration and position sense; positive Romberg sign | Sign | Common | Large-fibre involvement | Positive Romberg sign; Distal sensory impairment |
| Dysarthria | Sign | *"absent in some, but present in most cases"* | Absent to severe | Dysarthria |
| Oculomotor abnormalities: jerky pursuit, square-wave jerks, gaze-evoked or downbeat nystagmus, slow saccades, saccadic dysmetria | Sign | *"abnormal in all but one case"* | — | Jerky ocular pursuit movements; Nystagmus; Slow saccadic eye movements |
| Cerebellar atrophy on MRI | Imaging | Absent or mild | — | Cerebellar atrophy (bind with a mild qualifier, or mark as variable) |

**Onset.** Late adult onset. The mean age was 53.5 years, with a range of 35 to almost 70 (Nibbeling 2017). The 1995 report gives *"late onset of symptoms (over the age of 40 years) and slow progression"* (PMID:8595484).

**Atypical case (PLD3 p.Ile26Thr, c.77T>C; zygosity and segregation not reported; PMID:38059248).**
- A 20-year-old woman with bilateral sensorineural hearing loss from age 13, then ataxia, dysarthria and early optic atrophy.
- She had severe sensorimotor axonal polyneuropathy with distal weakness and diffuse cerebellar atrophy, and became wheelchair-bound.
- Treat this as weak, unconfirmed evidence. Do not add hearing loss or optic atrophy as core SCA46 features without a `notes` caveat.

**Quality of life.** No published SARA, ICARS, EQ-5D or SF-36 data specific to SCA46.

## 4. Genetic and molecular information

- **Gene:** PLD3 (phospholipase D family member 3), 19q13.2, hgnc:17158, NCBI Gene 23646, UniProt Q8IV08.
- **Pathogenic variant:** NM_012268 c.923T>C, p.Leu308Pro. UniProt annotates it as of uncertain significance, with *reduced lysosomal localization; induces retention in the ER; reduction of proteolytic cleavage; loss of exonuclease activity* ([UniProt](https://uniprot.org/uniprotkb/Q8IV08/entry)). No ClinVar or ACMG classification was retrieved, and the gnomAD allele frequency was not retrieved.
- **Origin:** germline.
- **Functional class:** loss of function (LoF).
  - Nibbeling 2017 (COS-7 lysates): *"PLD3-L308P exhibited significantly reduced activity compared to PLD3-WT"*. The values were WT 2.2 ± 0.2 and L308P 1.5 ± 0.06, against a GFP mock of 1.7 ± 0.1. The L308P result is therefore close to background.
  - Nibbeling 2017 found no difference from wild type in localization, stability or ER stress.
  - Gonzalez 2018 (untagged protein): ER retention, impaired lysosomal delivery and processing, and loss of 5′ exonuclease activity (PMID:30312375).
  - A dominant-negative mechanism has not been tested. Haploinsufficiency is the default assumption, but Pld3 heterozygous and homozygous mice show no ataxia.
- **ClinGen / GenCC:** ClinGen: *"ClinGen has not yet published curations for PLD3"*. GenCC: SCA46 AD at Supportive (Orphanet) and Limited ([genebe](https://genebe.net/gene/hg38/PLD3)). Per CLAUDE.md, record only the tiers you copy directly from a GenCC or Orphanet source. Orphanet submits everything at Supportive.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported for SCA46. PLD3 hippocampal methylation changes have been reported in Alzheimer's disease (PMID:30208929), which is not relevant to SCA46.
- **Network context:** Nibbeling 2017 placed PLD3 in the *synaptic transmission* cluster with FAT2, KIF26B, PDYN, FGF14, PRKCG and CACNA1A. The abstract states: *"Our work links spinocerebellar ataxia to alterations in synaptic transmission and transcription regulation"* (PMID:29053796; cached). This is a computational, guilt-by-association result.

## 5. Environmental information

No environmental, lifestyle or infectious contributors are reported. Not applicable.

## 6. Mechanism and pathophysiology

### Ordered causal chain (★ = demonstrated; ◇ = inferred)

1. ★ A heterozygous germline PLD3 p.Leu308Pro variant in the luminal HKD catalytic domain **leads to** misfolding and retention of the mutant protein in the ER, with failed ESCRT-dependent delivery to lysosomes and failed proteolytic processing. Evidence is from overexpressing cells only (PMID:30312375; the trafficking route is described in PMID:29386126: *"PLD3 reaches lysosomes as a type II transmembrane protein"*).
2. ★ This **results in** loss of lysosomal acid 5′ exonuclease activity from the mutant allele.
   - *"PLD3 as the principal acid 5' exonuclease in HeLa cells"* (PMID:33288674).
   - *"they are 5' exonucleases, probably identical to spleen phosphodiesterase, that break down TLR9 ligands"* (PMID:30111894).
   - In heterozygotes the expected residual activity is about 50%. Whether the mutant has a dominant-negative effect is untested ◇.
3. ◇ This **leads to** slower lysosomal breakdown of single-stranded nucleic acids, especially mitochondrial DNA.
   - *"We identified mitochondrial DNA (mtDNA) as a major physiological substrate"* (PMID:37225734).
   - *"The deficiency of PLD3 leads to the slowed degradation of nucleic acids in lysosomes"* (PMID:37994783).
4. **Branch A** ◇ (shown in PLD3-deficient neurons and cells, not in SCA46 patients): mtDNA leaks from lysosomes into the cytosol and **activates** cGAS–STING, which **leads to** increased autophagy, APP-CTF and cholesterol accumulation, and lysosomal stress.
   - *"Lysosomal leakage of mtDNA to the cytosol activates cGAS-STING signaling"* (PMID:37225734).
   - Endosomal TLR7/TLR9 sensing of unbroken nucleic acids is a parallel innate-immune route (PMID:34620855, 38697119). It is mainly shown in myeloid cells.
5. **Branch B** ◇: loss of PLD3 synthase activity **reduces** lysosomal S,S-BMP, which **impairs** lysosomal lipid and ganglioside breakdown.
   - *"Deletion of PLD3 or PLD4 markedly reduced BMP levels in cells or in murine tissues"*; disease-associated PLD3 mutants have reduced activity (PMID:39423811).
   - Whether L308P was tested specifically was not confirmed from the abstract.
6. ◇ Lysosomal dysfunction in long-lived neurons (cerebellar Purkinje cells and/or large-fibre dorsal root ganglion sensory neurons) **leads to** slow neurodegeneration and axonal degeneration. This step has not been demonstrated for PLD3. Indirect support: Zfp212 knockout mice show Purkinje cell death accompanied by Pld3 downregulation, and restoring ZNF212 rescues it. *"Pld3 alone was tightly regulated by Flag-tagged ZNF212 overexpression"* (PMID:34815492).
7. ★ Clinically, sensory axonal neuropathy (large-fibre loss) plus mild cerebellar dysfunction **results in** mixed sensory–cerebellar gait ataxia, dysarthria and oculomotor signs (PMID:8595484, 29053796).

### Counter-evidence to attach to steps 6 and 7

- Pld3 knockout mice: *"These data do not reveal a major degenerative phenotype of the cerebellum in PLD3 KO mice."*
- PLD3 expression is *"lowest… in the adult cerebellum compared to all other brain regions"* (PMID:30312375).
- Encode this as `HUMAN_MODEL_MISMATCH`, not as a refutation of the variant. Mice may need a longer lifespan, a second hit, or compensation by PLD4.

### Suggested ontology anchors (leads only; resolve each CURIE before binding)

- **GO biological processes:** lysosomal DNA catabolic process / DNA catabolic process; 5′-3′ exonuclease activity (molecular function); lysosome organization; cGAS/STING signaling (positive regulation of type I interferon production); protein retention in ER lumen; lysosomal transport.
- **GO cellular components:** lysosomal lumen and lysosomal membrane; endoplasmic reticulum (mutant retention); multivesicular body.
- **CL cell types:** Purkinje cell; sensory neuron of dorsal root ganglion (large-fibre / proprioceptive); neuron.
- **Biological scale:** step 1 MOLECULAR; steps 2–5 CELLULAR; step 6 TISSUE; step 7 ORGANISM.

### Molecular profiling and advanced technologies

- No transcriptomic, proteomic, metabolomic or single-cell data exist for SCA46.
- Structures of PLD3 are available: a crystal structure (PMID:37994783, 39325669, 39517096) and cryo-EM structures with bound substrate (PMID:41381514, 38537643). These could support modelling of L308P, but none of the abstracts retrieved mention L308P.

## 7. Anatomical structures affected

- **Primary:** cerebellum (mild or absent atrophy); peripheral sensory nerves (sural nerve axonal loss); dorsal root ganglia and dorsal columns (inferred from large-fibre sensory loss).
- **Secondary:** oculomotor control pathways in the cerebellum and brainstem.
- **Subcellular:** lysosome (normal site of action); ER (where the mutant is retained).
- **Laterality:** bilateral and symmetric, distal-predominant neuropathy.
- **Suggested UBERON terms (verify):** cerebellum, sural nerve, dorsal root ganglion, peripheral nerve.

## 8. Temporal development

- **Onset:** adult or late adult, mean 53.5 years (range 35 to about 70). Insidious.
- **Course:** slowly progressive and lifelong.
- **Stages, remission, critical windows:** not described. There is no natural-history study.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (heterozygous). Penetrance appears high in the family: 8 of 8 carriers were affected. One mildly symptomatic relative was a non-carrier, which could be a phenocopy. Expressivity is variable between sensory-predominant and cerebellar-predominant forms. No anticipation, since this is not a repeat expansion.
- **Prevalence:** unknown. Only one family is confirmed (`CASES_IN_LITERATURE`). Orphanet's prevalence class was not retrieved because the page was blocked; check `just structured-rebuild-orphanet --id 589522`.
- **Population:** Dutch, with a possible additional Indian case. There is no founder data, no sex bias (both generations were affected), and no consanguinity in the dominant family.

## 10. Diagnostics

- **Clinical work-up:**
  - Nerve conduction studies show a sensory axonal neuropathy.
  - Sural nerve biopsy shows loss of myelinated fibres. 1995 report: *"Clinical, electrophysiological and sural nerve biopsy findings revealed a sensory polyneuropathy"*.
  - Brain MRI shows normal or mildly atrophic cerebellum.
  - Eye-movement examination.
- **Genetic testing:**
  - Ataxia or neuropathy NGS panels, or exome or genome sequencing (exome found the original variant).
  - GTR lists PLD3 sequence analysis (4 clinical tests), deletion/duplication analysis (4) and targeted variant analysis (1).
  - First exclude the common repeat-expansion SCAs (SCA1/2/3/6/7/17, DRPLA), RFC1 CANVAS and FGF14-GAA (SCA27B). These are relevant because the sensory-plus-cerebellar picture overlaps heavily with CANVAS.
- **Biomarkers:** none.
- **Differential diagnosis:**
  - RFC1-related CANVAS, which has sensory neuronopathy and vestibular areflexia.
  - Friedreich ataxia, which has earlier onset, GAA expansion and cardiomyopathy.
  - SCA4, which also features sensory axonal neuropathy.
  - SANDO / POLG disorders.
  - Vitamin E deficiency.
  - Acquired sensory ganglionopathies.
- **Screening:** cascade testing of relatives once a familial variant is known.

## 11. Outcome and prognosis

- No mortality or survival data. Slow progression suggests a near-normal lifespan, but this is not documented.
- Expected disability: impaired gait, possible need for walking aids, and falls. The atypical young patient became wheelchair-bound (PMID:38059248).
- No prognostic biomarkers.

## 12. Treatment

There is no disease-modifying therapy and no clinical trials (ClinicalTrials.gov not searched in depth). Management is supportive.

| Intervention | NCIT suggestion (verify) | `therapeutic_modality` |
|---|---|---|
| Physical therapy / gait and balance training | NCIT:C15302 Physical Therapy | BEHAVIORAL |
| Speech therapy for dysarthria | NCIT:C159273 (speech language therapy) | BEHAVIORAL |
| Occupational therapy | NCIT:C121351 | BEHAVIORAL |
| Rehabilitation | NCIT:C15315 Rehabilitation | BEHAVIORAL |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — |

- **Pharmacogenomics:** not applicable.
- **Experimental options:** none specific. Small-molecule modulators of PLD3/PLD4 exist as research tools (PMID:34332037, 38560090). STING inhibition normalized APP-CTF in PLD3-deficient models: *"STING inhibition largely normalizes APP-CTF levels"* (PMID:37225734). This is preclinical and not related to ataxia.

## 13. Prevention

- **Primary prevention:** not applicable.
- **Reproductive options:** genetic counseling, with prenatal or preimplantation testing available once the familial variant is known (50% recurrence risk).
- **Tertiary prevention:** fall prevention and foot care for the sensory neuropathy.

## 14. Other species and natural disease

- No naturally occurring PLD3 ataxia is listed in OMIA (not checked exhaustively).
- **Orthologs:** mouse Pld3 and zebrafish pld3 (IDs not retrieved).

## 15. Model organisms

| Model | Findings | Relevance to SCA46 |
|---|---|---|
| **Pld3⁻/⁻ mouse** (Gonzalez 2018, PMID:30312375) | No cerebellar degeneration or ataxia | `FAILS_TO_RECAPITULATE` for the cerebellar node. Possible divergences: `SPECIES_MISMATCH` and paralog (PLD4) compensation. |
| **Pld3⁻/⁻ Pld4⁻/⁻ mouse** (PMID:30111894, 34620855) | *"Pld3-/-Pld4-/- mice accumulate small ssRNAs and develop spontaneous fatal hemophagocytic lymphohistiocytosis (HLH)"* | Shows the exonuclease function in vivo. The immune phenotype is not ataxia. |
| **Pld3 knockout or overexpression in Alzheimer's mice** (Yuan 2022, PMID:36450991) | *"Pld3 deletion reduced endolysosomal vesicle and spheroid size"* | Shows neuronal lysosomal and axonal roles. Alzheimer's context only. |
| **Zfp212 knockout mouse** (PMID:34815492) | Purkinje cell degeneration and ataxia-like gait, with Pld3 downregulation | Indirect support that PLD3 matters in the cerebellum (`PARTIALLY_RECAPITULATES`, `LOW` fidelity). |
| **Cell models:** COS-7, HeLa, HEK293 overexpression; PLD3-KO HeLa; iPSC-derived neurons (PMID:37225734) | L308P activity and localization; the mtDNA–STING axis | IN_VITRO evidence. No knock-in of L308P in any system. |

**Main gap:** there is no L308P knock-in model and no patient iPSC-derived Purkinje cells or sensory neurons.

---

## Evidence quick-reference (verbatim abstract fragments)

| PMID | Evidence source | Fragment |
|---|---|---|
| 29053796 (cached) | HUMAN_CLINICAL + IN_VITRO | "we report five novel spinocerebellar ataxia genes, FAT2, PLD3, KIF26B, EP300, and FAT1" |
| 8595484 | HUMAN_CLINICAL | "late onset of symptoms (over the age of 40 years) and slow progression" |
| 8595484 | HUMAN_CLINICAL | "mild eye movement disturbances, probably due to cerebellar involvement" |
| 38059248 | HUMAN_CLINICAL | "clinically characterized by ataxia, peripheral neuropathy, cerebellar dysarthria, and varied oculomotor abnormalities." |
| 30111894 | MODEL_ORGANISM / IN_VITRO | "Mice deficient in both PLD3 and PLD4 developed lethal liver inflammation in early life" |
| 34620855 | MODEL_ORGANISM | "PLD3 and PLD4 regulate both endosomal TLR and cytoplasmic/STING nucleic acid sensing pathways" |
| 29386126 | IN_VITRO | "PLD3 is sorted into intraluminal vesicles of multivesicular endosomes" |
| 33288674 | IN_VITRO | "proteolytic processing of PLD3 is dispensable for its hydrolytic activity" |
| 37225734 | IN_VITRO / MODEL_ORGANISM | "Lysosomal leakage of mtDNA to the cytosol activates cGAS-STING signaling" |
| 39423811 | IN_VITRO / MODEL_ORGANISM | "phospholipases D3 and D4 (PLD3 and PLD4) synthesize lysosomal S,S-BMP" |
| 34815492 | MODEL_ORGANISM | "GABAergic Purkinje cell degeneration in the Cb and aberrant locomotion were observed in adult Zfp212-KO mice." |

**Caveats on this table:**
- Except for PMID:29053796, the fragments came from a web-fetch tool and not from `references_cache`. Run `just fetch-reference PMID:<id>` and re-copy each snippet from the cache before using it as evidence.
- The Gonzalez (30312375) and Ma & Verbeek (30312384) letters have no PubMed abstract. Snippets from them need full-text access.
- Full-text quotes from Nibbeling 2017 (onset 53.5 years, segregation in 8 affected, the activity values) are not in the abstract-only cache.

## Open issues to record

1. **Gene–disease validity is unresolved.** There is one family, the OMIM entry is provisional, ClinGen has no curation, and the knockout mouse is negative. Do not set `relationship_type: CAUSATIVE` without a note; consider whether the evidence supports it.
2. **Haploinsufficiency versus dominant-negative effect is untested.**
3. **The cell type is unknown.** It is not established whether the primary lesion is in Purkinje cells, sensory ganglion neurons, or both. The mixed sensory–cerebellar phenotype is consistent with both.
4. **The Indian p.Ile26Thr case** needs a segregation and zygosity check before it is counted as SCA46.

---

### Sources
- Nibbeling et al. 2017, Brain — [PMID:29053796](https://pubmed.ncbi.nlm.nih.gov/29053796/); [full text](https://academic.oup.com/brain/article/140/11/2860/4372181)
- van Dijk et al. 1995, Brain — [PMID:8595484](https://pubmed.ncbi.nlm.nih.gov/8595484/)
- Gonzalez et al. 2018, Brain letter — [PMC6202572](https://pmc.ncbi.nlm.nih.gov/articles/PMC6202572) (PMID:30312375)
- Ma & Verbeek 2018 reply — [Brain e79](https://dbpia.nl.go.kr/brain/article/141/11/e79/5127750) (PMID:30312384)
- Sowmini et al. 2023 — [J Neurosci Rural Pract](https://ruralneuropractice.com/spinocerebellar-ataxia-46-in-a-young-female/) (PMID:38059248)
- Gavin et al. 2018, Nat Immunol — [PMC6105523](https://pmc.ncbi.nlm.nih.gov/articles/PMC6105523) (PMID:30111894)
- Gavin et al. 2021, Nat Commun — [PMC8497607](https://pmc.ncbi.nlm.nih.gov/articles/PMC8497607/) (PMID:34620855)
- Van Acker et al. 2023, Nat Commun — [PMC10209153](https://pmc.ncbi.nlm.nih.gov/articles/PMC10209153) (PMID:37225734)
- Gonzalez et al. 2018 Cell Rep (PMID:29386126); Cappel et al. 2021 JBC (PMID:33288674); Singh et al. 2024 Cell (PMID:39423811); Yuan et al. 2022 Nature (PMID:36450991); Khang et al. 2021 Sci Rep (PMID:34815492); Liu et al. 2021 Front Aging Neurosci (PMID:34267643); Cruchaga et al. 2014 Nature (PMID:24336208); PLD3 structures (PMID:37994783, 39517096, 41381514)
- [MedGen 1624251](https://www.ncbi.nlm.nih.gov/medgen/1624251) · [GTR C4540404](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4540404) · [ClinGen PLD3](https://search.clinicalgenome.org/kb/genes/HGNC:17158) · [UniProt Q8IV08](https://uniprot.org/uniprotkb/Q8IV08/entry) · [LOVD SCA46](https://databases.lovd.nl/shared/diseases/06427) · [genebe PLD3 (GenCC)](https://genebe.net/gene/hg38/PLD3) · [MalaCards](https://malacards.org/card/spinocerebellar_ataxia_46) · [Frontiers Liu 2021](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2021.671296/full)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0080288` (3 mentions) - the report calls it "DOID"; DOID calls it **spinocerebellar ataxia 46**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.