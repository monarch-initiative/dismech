---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T15:22:41.259453'
end_time: '2026-09-23T15:25:22.923931'
duration_seconds: 161.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ARHGDIA-Related Steroid-Resistant Nephrotic Syndrome
  mondo_id: MONDO:0014099
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
  web_search_requests: 13
  num_turns: 27
  total_cost_usd: 1.3074506000000001
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 18
  not_found: 0
  obsolete: 0
  unverifiable: 8
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 12
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  - EXT_ID
  - MIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ARHGDIA-Related Steroid-Resistant Nephrotic Syndrome
- **MONDO ID:** MONDO:0014099 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ARHGDIA-Related Steroid-Resistant Nephrotic Syndrome** covering all of the
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

I'll research this systematically using web search, prioritizing primary literature with PMIDs.

I now have sufficient primary-source material. Here is the research report.

# ARHGDIA-Related Steroid-Resistant Nephrotic Syndrome (Nephrotic Syndrome, Type 8 / NPHS8) — Research Report

**Identifiers:** OMIM #615244 (NPHS8); Gene: *ARHGDIA*, OMIM *601925, HGNC:678, UniProt P52565, chr17q25.3, GRCh38 ENSG00000141522; MONDO:0014099; Orphanet ORPHA:656 (Hereditary steroid-resistant nephrotic syndrome, parent grouping — no disease-specific ORPHA code was found for the ARHGDIA subtype specifically; it is cataloged under this broader hereditary SRNS entry and via GeneCC gene-disease submissions at thegencc.org/genes/HGNC:678); Inheritance: autosomal recessive.

---

## 1. Disease Overview

ARHGDIA-related nephrotic syndrome (NPHS8) is a genetically defined, autosomal recessive form of steroid-resistant nephrotic syndrome (SRNS) caused by biallelic loss-of-function variants in *ARHGDIA*, which encodes Rho GDP-dissociation inhibitor alpha (RhoGDIα/GDIα). It was established as a monogenic SRNS cause simultaneously by two independent groups in 2013: Gee et al. (PMID:23867502, *J Clin Invest* 123(8):3243-3253) via homozygosity mapping/whole-exome sequencing in a consanguineous family, and Gupta et al. (PMID:23434736, *J Med Genet* 50(5):330-338) via whole-exome sequencing of two affected sisters. Both groups independently converged on the same gene and the same podocyte cytoskeletal mechanism, which is unusually strong corroboration for a single-gene SRNS discovery.

Direct quote (Gee et al., abstract): *"We combined homozygosity mapping with whole-exome resequencing and identified an ARHGDIA mutation that causes SRNS... These findings identify a single-gene cause of NS and reveal that RHO GTPase signaling is a pathogenic mediator of SRNS."*

Direct quote (Gupta et al., conclusions): *"Mutations in ARHGDIA need to be considered in the aetiology of heritable forms of nephrotic syndrome."*

## 2. Etiology / Genetic Basis

**Gene function.** *ARHGDIA*'s product sequesters RHOA, RAC1, and CDC42 in their inactive, GDP-bound, cytosolic form and protects them from proteasomal degradation. Gee et al.: *"ARHGDIA is in a complex with RHO GTPases and is prominently expressed in podocytes of rat glomeruli."*

**Reported pathogenic variants (all biallelic, AR):**
| Variant | Type | Source |
|---|---|---|
| c.553_555del, p.Asp185del (ΔD185) | In-frame deletion, homozygous, two affected sisters | Gupta et al. 2013, PMID:23434736 |
| p.Arg120Ter (R120X) | Nonsense | Gee et al. 2013, PMID:23867502 |
| p.Gly173Val (G173V) | Missense | Gee et al. 2013, PMID:23867502 |
| Additional novel variant, single case | Iranian consanguineous SRNS cohort (n=30 families) | Estiar-Nejad/colleagues cohort, PMC9555279 — reports ARHGDIA among single-case genetic causes alongside NUP205, COQ6, SGPL1, NPHP1; states one ARHGDIA variant "had not previously been reported as disease-causing" (paraphrase from search synthesis — exact primary-text confirmation of this ARHGDIA-specific detail was not independently verified by direct fetch; treat as a lead pending confirmation of full text) |
| Homozygous *ARHGDIA* mutation, 11-month-old infant | Case report | PMID:35060086, *Indian J Pediatr* — abstract text could not be retrieved directly; title and indexing confirm a third clinical report of infantile-onset SRNS with a homozygous ARHGDIA variant |

**Zygosity/origin:** all reported cases are homozygous or compound-heterozygous germline variants, consistent with autosomal recessive, loss-of-function disease mechanism. No modifier genes, digenic interactions, or protective alleles have been reported in the literature retrieved.

**Frequency among SRNS cohorts:** ARHGDIA is a rare cause. In the largest reported consanguineous SRNS cohort search returned (30 Iranian families, PMC9555279), the dominant genes were NPHS1 (~30%), NPHS2 (~20%), and WT1 (~7%), with ARHGDIA appearing only in a single case — consistent with it being a minor contributor genome-wide, as expected for a gene identified from single/small pedigrees rather than large cohort screens.

## 3. Phenotypes

**Onset:** neonatal to early infancy in the founding reports — Gupta et al.'s sisters had congenital nephrotic syndrome; the case report literature includes an 11-month-old infant (PMID:35060086). OMIM's synopsis (per search-engine synthesis of the omim.org entry, direct fetch blocked by a bot-verification wall) describes "neonatal or early childhood onset steroid resistant renal disease."

**Core renal phenotype:**
- Severe proteinuria, nephrotic-range
- Hypoalbuminemia
- Generalized edema
- Hyperlipidemia
- Progressive renal failure to end-stage kidney disease (steroid-resistant by definition — unresponsive to corticosteroid therapy)

**Suggested HPO terms:** HP:0000100 (Nephrotic syndrome), HP:0003155 (Elevated urine protein/proteinuria — or HP:0000093 Proteinuria), HP:0003073 (Hypoalbuminemia), HP:0003077 (Hyperlipidemia), HP:0000969 (Edema), HP:0000083 (Renal insufficiency)/HP:0000822 progression to HP:0003774 (Stage 5 chronic kidney disease), HP:0012622 (Chronic kidney disease). Onset: HP:0003623 (Neonatal onset) or HP:0410280 (Infantile onset) depending on the individual case.

**Histopathology (kidney biopsy):** diffuse mesangial sclerosis — small glomeruli, hypercellularity, increased extracellular matrix, contracted/collapsed glomerular tufts surrounded by immature/abnormal podocytes. Electron microscopy: diffuse foot process effacement and thinning of the glomerular basement membrane (per search synthesis of case-report content; this histologic description should be re-verified against primary-text access to the case report(s) before use as a direct quote in curation — flagged as a lead, not independently confirmed by direct source fetch).

**Extrarenal involvement:** None consistently reported in the human literature retrieved. Note that the mouse knockout (Togawa et al. 1999, below) additionally shows reproductive organ impairment and lymphocyte trafficking defects (Ishizaki et al. 2006, *J Immunol*, GDIα/GDIβ double knockout) — these are model-organism findings and have **not** been reported as part of the human phenotype in the literature surveyed; this is a candidate `HUMAN_MODEL_MISMATCH`/undetermined-translatability point rather than an established pediatric extrarenal manifestation.

## 4. Molecular Mechanism / Pathophysiology

**Causal chain (as established by the founding papers and mechanistic follow-up):**

1. Biallelic loss-of-function *ARHGDIA* variant (R120X, G173V, ΔD185, or other) →
2. Mutant RhoGDIα protein fails to bind RHO-family GTPases (RHOA, RAC1, CDC42) — demonstrated directly by co-immunoprecipitation/binding assays in HEK293T cells (Gupta et al.) and by loss of GTPase interaction for R120X/G173V (Gee et al.) →
3. Loss of GDIα-mediated cytosolic sequestration and protection from proteasomal degradation of RHO-GTPases →
4. Hyperactivation of GTP-bound RAC1 (most consistently and prominently implicated) and CDC42, but **not** RHOA — Gee et al.: *"ARHGDIA mutations (R120X and G173V) ... increased active GTP-bound RAC1 and CDC42, but not RHOA, indicating that RAC1 and CDC42 are more relevant to the pathogenesis of this SRNS variant than RHOA."* The follow-up mechanistic paper (Gupta, *Small GTPases* 2016, PMC4905261) sharpens this further: *"Rac1 activity was markedly increased in GDIα KD podocytes"* and Rac1 showed the most pronounced, consistent hyperactivation of the three GTPases tested across all three disease mutations. Gupta et al. 2013 additionally showed hyperactivation of all three GTPases (RhoA, Rac1, Cdc42) in patient fibroblasts and GDIα-knockdown podocytes, with GDIα mislocalized to the nucleus in the ΔD185 proband's fibroblasts.
5. Rho-GTPase (chiefly RAC1) dysregulation causes derangement of the podocyte actin cytoskeleton →
6. Altered podocyte motility — mutant GDIα *enhanced* migration of cultured human podocytes, an effect reversible with RAC1 inhibitors (Gee et al.) — and impaired podocyte morphology/adhesion →
7. Foot process effacement / podocyte injury and glomerular filtration barrier breakdown →
8. Proteinuria, hypoalbuminemia, edema, hyperlipidemia (nephrotic syndrome) →
9. Progressive glomerulosclerosis (diffuse mesangial sclerosis pattern) → chronic/end-stage renal failure.

**Model-organism confirmation of the chain:** Gee et al. recapitulated the nephrotic phenotype in *arhgdia*-deficient zebrafish, and RAC1 inhibitors were "partially effective in ameliorating arhgdia-associated defects" — direct evidence that step 4→6 is causally load-bearing and pharmacologically targetable, at least in the fish model. The original constitutive mouse knockout (Togawa et al. 1999, *Oncogene* 18:5373-5380, PMID:10498891) independently established, well before the human disease-gene discovery, that *Arhgdia*−/− mice "developed massive proteinuria mimicking nephrotic syndrome, leading to death due to renal failure within a year," with additional degeneration of tubular epithelial cells and progressive reproductive-organ impairment — the mouse model that first flagged this gene as renally relevant, later mined by Gupta et al. as translational justification for pursuing *ARHGDIA* as a human candidate gene ("Mice with targeted inactivation of ARHGDIA are known to develop severe proteinuria and nephrotic syndrome, therefore this gene was pursued in functional studies").

**Molecular pathway/GO/CL suggestions:**
- GO:0005094 (Rho GDP-dissociation inhibitor activity) — ARHGDIA's own molecular function
- GO:0007266 (Rho protein signal transduction); GO:0030036 (actin cytoskeleton organization); GO:0030334 (regulation of cell migration)
- CL:0000653 (podocyte) — the principal disease-relevant cell type
- Relevant downstream GTPases as distinct entities: RAC1 (HGNC:9801), CDC42 (HGNC:1736); note RHOA (HGNC:667) is implicated in in-vitro/fibroblast assays but was explicitly **not** hyperactivated in the podocyte/patient-derived Rho-GTPase activity assays in Gee et al., a distinction worth preserving rather than lumping all three GTPases together in a pathophysiology node.

## 5. Anatomical/Cellular Localization

- Organ: kidney (glomerulus) — primary and essentially sole clinically established site of disease.
- Tissue: glomerular filtration barrier / mesangium.
- Cell type: podocyte (CL:0000653), the cell type in which ARHGDIA is "prominently expressed" per both founding papers, in rat and mouse glomeruli.
- Subcellular: cytoplasm (GDIα's normal sequestering compartment for inactive GTPases) vs. pathological nuclear mislocalization of mutant GDIα reported in ΔD185 patient fibroblasts (Gupta et al.) — a notable subcellular mislocalization finding suggesting disruption of normal cytoplasmic tethering as part of the loss-of-function mechanism.

## 6. Diagnostics

- Clinical presentation: infantile/early-childhood nephrotic syndrome that fails to respond to corticosteroid therapy (defining "steroid-resistant" status), prompting genetic workup.
- Genetic testing: targeted single-gene sequencing or inclusion in SRNS/congenital nephrotic syndrome gene panels (alongside NPHS1, NPHS2, WT1, PLCE1, LAMB2, and others); whole-exome sequencing was the discovery method in both founding cohorts and remains the practical diagnostic route for a gene this rare (not typically first-tier on narrow panels given its low prevalence in cohorts).
- Renal biopsy: diffuse mesangial sclerosis pattern; EM shows foot process effacement — supportive but non-specific; overlaps histologically with WT1- and PLCE1-related DMS, so histology alone cannot discriminate genotype.
- No specific biomarker or functional assay for ARHGDIA deficiency is reported in a clinically validated form; functional confirmation (GTPase activity assays, fibroblast Rho-GTPase pulldown) has so far been used only in the research setting (Gupta et al.'s proband fibroblast studies), not as a routine diagnostic.

## 7. Treatment / Prognosis

- No disease-specific approved therapy exists. Standard nephrotic-syndrome supportive management applies (ACE inhibitor/ARB for proteinuria reduction, management of edema/hyperlipidemia, and ultimately renal replacement therapy/transplantation for progression to ESKD), consistent with general SRNS management principles; the literature retrieved contains no ARHGDIA-specific clinical trial or approved pharmacotherapy.
- **Experimental/mechanistic therapeutic signal:** RAC1 inhibition. Gee et al. showed pharmacological RAC1 inhibition reversed the enhanced podocyte migration phenotype in vitro and was "partially effective in ameliorating arhgdia-associated defects" in the zebrafish model — this is model-system evidence for a targeted mechanism-based therapeutic strategy, not a clinically validated treatment; would map to a `HUMAN_MODEL_MISMATCH`/emerging hypothesis framing rather than an established treatment entry.
- Renal transplantation: general literature confirms recurrent nephrotic syndrome/FSGS after transplant is a recognized risk in genetic SRNS broadly (~30–40% depending on native histology), but no ARHGDIA-specific post-transplant recurrence case was identified in the searches performed; this should be recorded as a gap rather than inferred from the general SRNS transplant-recurrence literature.

## 8. Animal/Model Organism Summary

| Model | Genotype | Phenotype | Source |
|---|---|---|---|
| Mouse | *Arhgdia*−/− (constitutive KO) | Massive proteinuria mimicking nephrotic syndrome, death from renal failure within ~1 year; tubular epithelial degeneration; progressive reproductive organ impairment | Togawa et al. 1999, *Oncogene* 18:5373-5380, PMID:10498891 |
| Mouse | *Arhgdia*/*Arhgdib* double KO | Defective chemokine-directed lymphocyte migration/development | Ishizaki et al. 2006, *J Immunol* (lymphocyte/immune phenotype, not renal-focused; relevance to the human kidney disease is indirect) |
| Zebrafish | *arhgdia*-deficient (morpholino/genetic) | Recapitulated nephrotic phenotype; partially rescued by RAC1 inhibitor | Gee et al. 2013, PMID:23867502 |
| Cultured human podocytes | GDIα knockdown ± reconstitution with R120X/G173V/ΔD185 mutant constructs | RAC1 (and CDC42/RHOA in some assays) hyperactivation, impaired/enhanced motility phenotypes reversible by RAC1 inhibition, impaired actin polymerization | Gee et al. 2013; Gupta et al. *Small GTPases* 2016 (PMC4905261) |
| HEK293T cells | Transfected WT vs. mutant RhoGDIα | Mutant protein fails to bind RhoA/Rac1/Cdc42 | Gupta et al. 2013, PMID:23434736 |

The mouse constitutive knockout is notably the **oldest** piece of evidence in this entire causal chain (1999) — it identified the renal phenotype 14 years before the gene was linked to human disease, making it an unusually direct instance of animal-model-first gene discovery being retrospectively validated in humans. Model fidelity is high for the core proteinuria/glomerular phenotype but the mouse model's additional reproductive and immune phenotypes have no reported human correlate and should not be imported into the human pathograph without qualification.

## 9. Notable Gaps / Items Requiring Further Verification Before KB Entry

- Full-text confirmation of the Iranian cohort paper's (PMC9555279) specific ARHGDIA variant, zygosity, and patient-level clinical detail — direct fetch was blocked (reCAPTCHA); only search-engine synthesis was obtained, which per this repository's evidence standards is not an exact quotable snippet and must be re-fetched (e.g., via `just fetch-reference`) before citation.
- PMID:35060086 (Indian J Pediatr case report) abstract text could not be retrieved directly (fetch attempts returned only citation metadata or server errors); title/indexing confirm its existence and relevance but no quotable snippet was obtained.
- OMIM #615244's full clinical synopsis could not be directly fetched (bot-verification wall on omim.org); the clinical description used above is a search-engine paraphrase of the OMIM entry and should be re-verified against the primary OMIM text (or GeneReviews, if one exists — none was identified in these searches) before use as a cited snippet.
- No dedicated Orphanet disease-specific code (distinct from the broader ORPHA:656 "Hereditary steroid-resistant nephrotic syndrome" grouping) was confirmed for the ARHGDIA subtype specifically.
- Prevalence/incidence figures specific to NPHS8 were not found in any source; it appears only as single-case/single-family reports (three independent pedigrees/cases identified: the original consanguineous family, two sisters, the Iranian single case, and the Indian infant case report), consistent with an ultra-rare designation, but no formal prevalence class (Orphanet-style) was located.

---

## Sources

- [Entry - #615244 - NEPHROTIC SYNDROME, TYPE 8; NPHS8 - OMIM](https://www.omim.org/entry/615244)
- [Entry - *601925 - RHO GDP-DISSOCIATION INHIBITOR ALPHA; ARHGDIA - OMIM](https://omim.org/entry/601925)
- [ARHGDIA: a novel gene implicated in nephrotic syndrome - PubMed (PMID:23434736)](https://pubmed.ncbi.nlm.nih.gov/23434736/)
- [ARHGDIA mutations cause nephrotic syndrome via defective RHO GTPase signaling - PubMed (PMID:23867502)](https://pubmed.ncbi.nlm.nih.gov/23867502/)
- [JCI - ARHGDIA mutations cause nephrotic syndrome via defective RHO GTPase signaling (full text)](https://www.jci.org/articles/view/69134)
- [Disease-causing mutations of RhoGDIα induce Rac1 hyperactivation in podocytes - PMC (PMC4905261)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4905261/)
- [Europe PMC record for PMID:23867502 (abstract)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23867502&format=json&resultType=core)
- [Europe PMC record for PMID:23434736 (abstract)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23434736&format=json&resultType=core)
- [Homozygous ARHGDIA Gene Mutation in an 11-Month-Old Infant with Steroid-Resistant Nephrotic Syndrome - PubMed (PMID:35060086)](https://pubmed.ncbi.nlm.nih.gov/35060086/)
- [High detection rate for disease-causing variants in a cohort of 30 Iranian pediatric steroid resistant nephrotic syndrome cases - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9555279/)
- [Progressive impairment of kidneys and reproductive organs in mice lacking Rho GDIalpha - PubMed (PMID:10498891)](https://pubmed.ncbi.nlm.nih.gov/10498891/)
- [ARHGDIA gene with submissions organized by classifications - GenCC](https://thegencc.org/genes/HGNC:678)
- [ARHGDIA gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ARHGDIA)
- [Orphanet: ARHGDIA - Rho GDP dissociation inhibitor alpha](https://www.orpha.net/en/disease/gene/ARHGDIA)
- [Gene: ARHGDIA (ENSG00000141522) - Ensembl](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141522)
- [pharos.nih.gov MIM:615244](https://pharos.nih.gov/idg/diseases/MIM:615244)
- [Gene–disease relationships for glomerular phenotypes: expert recommendations from ClinGen - Nature Reviews Nephrology](https://www.nature.com/articles/s41581-026-01087-9)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 8 |
| Terms whose name was checked | 14 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0410280` (1 mention) - the report calls it "Infantile onset"; HP calls it **Pediatric onset**
- `CL:0000653` (2 mentions) - the report calls it "podocyte", "Cell type: podocyte"; CL calls it **podocyte**, and lists "renal podocyte" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000653` - called "podocyte", "Cell type: podocyte"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `EXT_ID`, `MIM`.

18 of 26 terms resolved to a current term; the rest could not be looked up either way.