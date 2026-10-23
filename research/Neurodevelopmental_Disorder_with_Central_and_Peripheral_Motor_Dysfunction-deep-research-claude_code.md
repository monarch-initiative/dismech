---
provider: claude_code
model: claude-fable-5-1, claude-haiku-5-5
cached: false
start_time: '2026-10-15T11:40:09.004770'
end_time: '2026-10-15T11:51:02.839238'
duration_seconds: 653.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder with Central and Peripheral Motor Dysfunction
  mondo_id: MONDO:0032698
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
  - claude-fable-5-1
  - claude-haiku-5-5
  web_search_requests: 5
  num_turns: 67
  total_cost_usd: 8.071843499999998
  session_id: 8ca6b661-a362-48d9-b9c8-002d2d4c606e
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 32
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 5
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35172135
  quotes_not_checkable: 2
  relevance_assessed: 19
  on_topic: 7
  off_topic: 3
  off_topic_references:
  - PMID:31761670
  - PMID:27616481
  - PMID:35172135
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 122
  verified: 117
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 15
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001276
    reported_labels:
    - Hypertonia (generalized, upper limb)
    ontology_label: Hypertonia
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Central and Peripheral Motor Dysfunction
- **MONDO ID:** MONDO:0032698 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Central and Peripheral Motor Dysfunction** covering all of the
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

I'll research NFASC-related neurodevelopmental disorder with central and peripheral motor dysfunction (NEDCPMD), starting from the references already cached in this worktree and then searching the literature.

Next I need abstracts for the newer PubMed hits (2020 to 2026), the two earlier cohort papers (Farwell Hagman 2017, Anazi 2017), the key mouse papers, the Brain commentary, and the Orphanet record.

I have what I need: the five cached primary papers, the OMIM-derived MedGen and HPO annotation sets, GenCC/PanelApp/ClinGen status, gnomAD constraint, the mouse and zebrafish model literature, a PubMed sweep through October 2026 showing no newer genetic case reports, and the local ontology caches for term suggestions. Writing the report now.

# Research Report: Neurodevelopmental Disorder with Central and Peripheral Motor Dysfunction (NEDCPMD)

**Target:** MONDO:0032698 | OMIM #618356 | Gene: *NFASC* (neurofascin), HGNC:29866 | Category: Mendelian, autosomal recessive
**Report date:** 2026-10-15

**Evidence base at a glance.** The entire published human literature is about 16 affected individuals from roughly 10 families, reported between 2017 and 2020. A PubMed sweep of every title containing "NFASC" or "neurofascin" published 2020 to October 2026 (83 records) found no additional genetic case reports: all are anti-neurofascin autoimmune nodopathy papers or basic biology. The mechanistic understanding rests on patient skin-biopsy immunofluorescence, patient-derived iPSC neurons, heterologous-cell assays, and a deep mouse and zebrafish literature on neurofascin isoforms at the node of Ranvier and axon initial segment.

---

## 1. Disease Information

**Overview.** NEDCPMD is an autosomal recessive disorder caused by biallelic variants in *NFASC*, the gene encoding neurofascin, an L1-family immunoglobulin-superfamily cell adhesion molecule that exists as a glial isoform (Nfasc155, at the paranodal axoglial junction of myelinating oligodendrocytes and Schwann cells) and neuronal isoforms (Nfasc186 and Nfasc140, at the node of Ranvier and axon initial segment). The phenotype is highly variable and tracks the isoform affected: variants abolishing Nfasc155 produce a severe neonatal picture (congenital hypotonia, areflexia, respiratory and feeding failure, demyelinating neuropathy, central white matter loss, profound developmental impairment), whereas variants restricted to Nfasc186 produce a later-onset progressive cerebellar ataxia with milder cognition and little or no peripheral neuropathy.

The OMIM-derived summary (via MedGen) reads: NEDCPMD is "an autosomal recessive neurologic disorder with a highly variable phenotype." At the severe end "patients may have hypotonia apparent from birth, necessitating mechanical respiration and tube-feeding, and global developmental delay"; at the milder end "patients may present with infantile-onset progressive ataxia and demyelinating peripheral neuropathy" ([MedGen 1674767](https://www.ncbi.nlm.nih.gov/medgen/1674767)).

The defining cohort paper states: "We identified 10 individuals from six unrelated families, exhibiting a neurodevelopmental disorder characterized with a spectrum of central (intellectual disability, developmental delay, motor impairment, speech difficulties) and peripheral (early onset demyelinating neuropathy) neurological involvement, who were found by exome or genome sequencing to carry one frameshift and four different homozygous non-synonymous variants in NFASC" (Efthymiou et al., Brain 2019, [PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/)).

**Identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032698 (label: neurodevelopmental disorder with central and peripheral motor dysfunction; related synonym NEDCPMD) ([OLS](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0032698)) |
| OMIM | #618356 (phenotype); *609145 (NFASC gene) |
| MedGen / UMLS | 1674767 / C5193049 |
| Orphanet | **No ORPHA entry found.** An ORDO search for "neurofascin" returns only the autoimmune entities ORPHA:730233 (Anti-NF155 nodopathy) and ORPHA:730238 (Anti-pan-neurofascin nodopathy); a search on the disease name returns nothing. Do not cite an `ORPHA:` reference for this disease. |
| KEGG DISEASE | H02990 |
| ICD-10/ICD-11 | No specific code; would fall under G60.8/G60.9 (other/unspecified hereditary neuropathy) or F8x/G93 developmental codes. Not disease-specific. |
| HGNC | NFASC = HGNC:29866 (repository form `hgnc:29866`; not yet in `cache/hgnc/terms.csv`, so `just validate-terms` must populate it) |
| NCBI Gene | 23114 |
| UniProt | O94856 |

**Synonyms.** NEDCPMD; NFASC-related neurodevelopmental disorder; "autosomal recessive ataxia with demyelinating neuropathy" (Monfrini 2019 framing); "hereditary nodo-paranodopathy" (Karakaya & Wirth 2019 framing, [PMID:31560060](https://pubmed.ncbi.nlm.nih.gov/31560060/)). PanelApp England originally listed the gene under "Cerebellar ataxia, Demyelinating neuropathy" before renaming to the OMIM phenotype ([PanelApp Hereditary ataxia panel 20](https://panelapp.genomicsengland.co.uk/panels/20/gene/NFASC/)).

**Source type.** All information is from individual-patient case reports and small family series, aggregated by OMIM/MedGen/HPO. There are no EHR cohorts, registries, or natural-history studies.

---

## 2. Etiology

**Causal factor.** Biallelic (homozygous in every reported family) pathogenic variants in *NFASC*. Monogenic; no environmental, infectious, or multifactorial component is described.

**Genetic risk factors.** Consanguinity is the dominant risk context. Of the reported families, Moroccan, Iraqi, Israeli, Saudi Arabian, Algerian, Italian, and Pakistani families were consanguineous. The Polish proband's parents denied consanguinity, but runs-of-homozygosity analysis found the variant "within a relatively long (>3 Mb) ROH together with high (∼90 percentile) summed length of ROHs," and three great-grandparents came from the same village, which the authors read as "a low but distinct degree of parental consanguinity" (Smigiel et al. 2018, [PMID:30124836](https://pubmed.ncbi.nlm.nih.gov/30124836/)). The American sibling pair was born to nonconsanguineous parents yet carried a homozygous frameshift (Harper et al. 2020, [PMID:31945734](https://pubmed.ncbi.nlm.nih.gov/31945734/)).

**Heterozygote constraint.** gnomAD scores *NFASC* as strongly intolerant of heterozygous loss of function: pLI ≈ 1.00, observed/expected LoF 0.29 (43 observed vs 147 expected), LOEUF 0.376, o/e missense 0.78 ([gnomAD API, GRCh38](https://gnomad.broadinstitute.org/gene/ENSG00000163531)). This sits awkwardly beside a strictly recessive disease and is worth recording as a knowledge gap: GenCC carries one "Limited" autosomal-dominant submission (Ambry, 2018) with no published dominant phenotype ([GenCC HGNC:29866](https://thegencc.org/genes/HGNC:29866)). Heterozygous parents in every report were healthy.

**Modifier genes.** None identified. Efthymiou et al. caution that "Given the history of consanguineous marriages in these families, other recessive variants may also have contributed to the clinical phenotype, as in Proband 8 from Family 5 who died prematurely" ([PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/)).

**Protective factors, gene-environment interactions.** None reported; not applicable at the current evidence level.

---

## 3. Phenotypes

Frequencies below are counts out of the ~16 reported individuals where the feature was assessed, drawn from Table 2 of Efthymiou 2019 (which also tabulates the Smigiel and Monfrini cases), the Kvarnung siblings, and the Harper siblings. Official HPO annotations for OMIM:618356 (37 terms) are at [HPO annotation API](https://ontology.jax.org/api/network/annotation/OMIM:618356); HPO IDs below were checked against the repository's `cache/hp/terms.csv`.

### 3a. Core neurodevelopmental and central features

| Phenotype | HPO | Onset / frequency / notes |
|---|---|---|
| Global developmental delay | HP:0001263 | All 13 tabulated cases. "In all patients, psychomotor development was severely delayed (except Patients 5 and 6) in all domains." (Efthymiou) |
| Severe global developmental delay | HP:0011344 | NF155-affecting and both-isoform cases |
| Intellectual disability | HP:0001249 | 11/13 tabulated; "Moderate to severe intellectual disability was documented in all cases" of the Efthymiou cohort. Mild in NF186-only cases: Kvarnung sister full-scale IQ 79–86; brother "within the normal span". |
| Absent speech | HP:0001344 | Efthymiou cohort: "None of the affected individuals attained intelligible speech." |
| Dysarthria | HP:0001260 | NF186-only ataxic cases (Kvarnung: "dysarthria has been present from early age") |
| Hypotonia / generalized hypotonia | HP:0001252 / HP:0001290 | Neonatal or first 6 months in all NF155-affecting cases: "Hypotonia was present from neonatal age in all cases." Mild general hypotonia in Kvarnung siblings. |
| Delayed ability to walk; no independent ambulation | HP:0031936 | Efthymiou: "none achieved purposeful hand movements or independent ambulation." Kvarnung: independent walking at 2 y (brother) and 4 y (sister). |
| Ataxia / gait ataxia | HP:0001251 / HP:0002066 | NF186-only cases (Monfrini siblings; Kvarnung siblings; Efthymiou patient 10 "Hypotonia/ataxia started at 15–16 months") |
| Dysmetria, dysdiadochokinesis, intention tremor | HP:0001310, HP:0002075, HP:0002080 | OMIM synopsis (Monfrini family) |
| Nystagmus | HP:0000639 | Kvarnung sister: abnormal vertical OKN; nystagmus on fixation |
| Vertigo | HP:0002321 | Kvarnung siblings: "disabling vertigo, nausea, and headache" |
| Spasticity, hyperreflexia, Babinski sign | HP:0001257, HP:0001347, HP:0003487 | Monfrini sister: "Spastic limb hypertonia, hyperreflexia"; Kvarnung: mild patellar hyperreflexia |
| Hypertonia (generalized, upper limb) | HP:0001276 | Saudi patient 8 |
| Myoclonus | HP:0001336 | Monfrini sister: "myoclonic jerks" |
| Seizure | HP:0001250 | Smigiel proband only (onset 4 months, valproate). Efthymiou: "affected individuals had no history of seizures." Rare. |
| Impaired social interaction / autistic features; motor stereotypy | HP:0000717, HP:0000733 | Efthymiou: "Impaired social interaction and only brief and occasional visual contact ... Several patients developed restricted patterns of interests and repetitive behaviours and frequently exhibited hand or head stereotypies." |
| Anxiety; aggressive behavior | HP:0000739, HP:0000718 | Monfrini brother: "Episodes of aggression, intense anxiety" |
| Absent response to touch/pain, no pupillary light response | (no precise HP; consider HP:0007328 Impaired pain sensation) | Smigiel proband: "no reaction to touch or pain, narrow, symmetric pupils, no response to light" |

### 3b. Peripheral nerve features

| Phenotype | HPO | Notes |
|---|---|---|
| Demyelinating peripheral neuropathy | HP:0007108 | Efthymiou: NCS "showed a severe reduction in peripheral nerve conduction velocities in all cases" tested (families 1, 2, 4, 6); "Patients from Families 1 and 2 exhibited the most profound phenotype with severe demyelinating and axonal neuropathy". Monfrini: "demyelinating neuropathy". **Absent** in NF186-only Kvarnung siblings (normal ENeG at 9 and 14 y) and Efthymiou family 6. |
| Decreased (motor) nerve conduction velocity | HP:0000762 / HP:0003431 | As above |
| EMG: neuropathic changes | HP:0003445 | Patient 3 "Acute and chronic denervation, PSW"; patients 9–10 "Chronic denervation-reinnervation" |
| Areflexia / hyporeflexia | HP:0001284 / HP:0001265 | Smigiel: "areflexia"; Efthymiou patients 1–2 "absent reflex" |
| Muscle weakness | HP:0001324 (not verified in cache; HP:0003324 Generalized muscle weakness also exists) | All cases. Kvarnung 5-/5 proximal and distal |
| Auditory neuropathy spectrum disorder / sensorineural hearing loss | HP:0000365; HP:0008527 | Harper 2020: two siblings "presented with hypotonia, respiratory insufficiency, and auditory neuropathy spectrum disorder (ANSD)"; Efthymiou: "The two American children ... developed profound sensorineural hearing loss". These are very likely the same family (same NM_015090 c.2771delC / p.P924fs allele, both American sibling pairs with SNHL); treat as one family, not two. |

### 3c. Neonatal, respiratory, feeding, craniofacial, skeletal

| Phenotype | HPO | Notes |
|---|---|---|
| Decreased fetal movement; polyhydramnios | HP:0001558 | Smigiel: "The pregnancy was affected by polyhydramnios and weak fetal movements." |
| Neonatal respiratory distress; respiratory insufficiency; respiratory failure requiring ventilation | HP:0002643, HP:0002093, HP:0002878 | Smigiel: intubation, later tracheostomy. Harper siblings: respiratory insufficiency. |
| Feeding difficulties; dysphagia | HP:0011968, HP:0002015 | Smigiel: PEG; American children "feeding difficulties requiring gastrostomy"; Monfrini sister dysphagia |
| Congenital contractures / flexion contracture of finger | HP:0002803 / HP:0012785 | Smigiel: "contractures of finger in hands and feet" |
| Facial hypomimia (amimia) | (consider HP:0000338 Hypomimic face; not cache-verified) | Smigiel "amimia"; Efthymiou "note the facial hypomimia present in all cases" (families 1–2) |
| Narrow forehead (bitemporal narrowing), wide/prominent nasal bridge, micrognathia, glossoptosis, high palate, cleft palate, hypertelorism | HP:0000341, HP:0000431, HP:0000426, HP:0000347, HP:0000162, HP:0000218, HP:0000175, HP:0000316 | Efthymiou: "several craniofacial dysmorphisms including bi-temporal narrowing, high and wide nasal bridge, micrognathia, glossoptosis and highly arched palate". Kvarnung siblings: no dysmorphology. |
| Microcephaly; small anterior fontanelle | HP:0000252, HP:0000237 | OMIM synopsis (rare) |
| 11 pairs of ribs; chest deformity | HP:0000878 | Saudi patient 8 "skeletal chest deformities" |
| Hyperextensibility of finger joints | HP:0001187 | OMIM synopsis (Anazi family) |
| Failure to thrive | HP:0001508 | OMIM synopsis |
| Recurrent respiratory infections | HP:0002205 | Kvarnung siblings in infancy |

### 3d. Imaging phenotypes

| Phenotype | HPO | Notes |
|---|---|---|
| Abnormal cerebral white matter / white matter loss | HP:0002500, HP:0012447 | Efthymiou: "MRI studies of Patients 1–3, 7, 9 and 10 showed loss of cerebral white matter ... also associated with atrophic changes mainly involving the corpus callosum and the brainstem" |
| Hyperintensity of cerebral white matter on MRI | HP:0030890 | Patient 7 "Diffuse white matter T2 hyperintensity"; Monfrini siblings "mild diffuse white matter T2 hyperintensity" |
| Hypoplasia / atrophy of corpus callosum | HP:0002079 | Patients 2–3 "thin corpus callosum" |
| Ventriculomegaly | HP:0002119 | Patient 1 "enlarged lateral ventricles ... indicative of cortical volume loss" |
| Cerebellar atrophy; cerebellar vermis atrophy | HP:0001272; (HP:0001320 is hypoplasia; use with care) | NF186-only cases: patients 9–10 "Cerebellar atrophy"; Monfrini "Mild cerebellar atrophy"; Kvarnung sister "mild vermian atrophy" |
| Normal MRI | — | Efthymiou patients 5–6 (Israeli, S820P) and Kvarnung brother |

**Quality of life.** No instrument-based QoL data exist. Functional outcome is severe: non-ambulatory and non-verbal in most, gastrostomy/tracheostomy dependence in the severe tier, wheelchair dependence by adolescence in the ataxic tier (Kvarnung sister "wheelchair-bound at the age 12 years").

---

## 4. Genetic/Molecular Information

**Causal gene.** *NFASC* (HGNC:29866; OMIM *609145; 1q32.1; NCBI Gene 23114; UniProt O94856). Protein: neurofascin, 1,347-aa precursor, single-pass type I membrane protein with 6 Ig-like C2 domains (aa 41–603) and 5 fibronectin type III domains (aa 630–1206); 13 annotated UniProt isoforms, with the paper literature focusing on Nfasc186 (NM_001005388, 1241 aa; neuronal, nodal/AIS) and Nfasc155 (NM_001160331, 1165 aa; glial, paranodal) ([UniProt O94856](https://rest.uniprot.org/uniprotkb/O94856.txt)). Kvarnung notes the pre-mRNA "undergoes extensive alternative splicing and results in more than 50 different isoforms such as 186, 180, 166, and 155 kDa" ([PMID:31608123](https://pubmed.ncbi.nlm.nih.gov/31608123/)).

**Gene-disease validity.** GenCC: Strong AR (Labcorp Genetics, evaluated 2021-04-16; PanelApp Australia, evaluated 2025-01-17), Moderate AR (Ambry, 2019), Limited AD (Ambry, 2018) ([GenCC](https://thegencc.org/genes/HGNC:29866)). ClinGen: no gene-disease validity, dosage, or actionability curation ([ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:29866)); the repository's `cache/clingen/gene_validity.csv` likewise has no NFASC row, so no `CGGV:` evidence can be cited. PanelApp England: Green on the Hereditary ataxia panel, biallelic, citing PMIDs 30850329, 31608123, 31501903 ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/20/gene/NFASC/)). ClinVar: 30 pathogenic/likely-pathogenic records for *NFASC* (ClinVar E-utilities query, 2026-10-15).

**Reported pathogenic variants (all homozygous).** Nomenclature as given in the source papers; GRCh37 coordinates from Efthymiou Table 1.

| Family (origin) | Variant (Nfasc186 NM_001005388 / Nfasc155 NM_001160331) | Domain | Isoform(s) hit | Functional evidence | Phenotype tier | Source |
|---|---|---|---|---|---|---|
| Smigiel (Polish) | NM_015090.3 c.2491C>T p.Arg831Ter; = NM_001160331 c.2536C>T p.Arg846Ter; intronic in NM_001005388 (c.2470+2039C>T); rs755160624; chr1:204953187C>T | 3rd FNIII repeat of Nfasc155-specific exon | Nfasc155 only | Patient skin biopsy: Nfasc155 absent at paranodes, Caspr lost, nodal isoforms intact | Severe neonatal; epilepsy | [PMID:30124836](https://pubmed.ncbi.nlm.nih.gov/30124836/) |
| Efthymiou F2 (American; = Harper 2020 siblings) | NM_001160331 c.2816delC p.Pro939Ter (NM_015090.3 c.2771delC p.Pro924Ter; Harper: p.P924RfsX35); chr1:204986105delC | C-terminal to FNIII, before TM | Nfasc155 (and transcript 3) | HEK: no surface or intracellular protein; abolished CNTN1/CASPR1 binding; patient 3 skin: "CASPR1 immunoreactivity was completely absent in the paranodal regions" | Most severe: SNHL/ANSD, gastrostomy, respiratory failure, severe NCV slowing, white matter loss | [PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/), [PMID:31945734](https://pubmed.ncbi.nlm.nih.gov/31945734/) |
| Efthymiou F1 (Moroccan) | c.2080C>A p.Pro694Thr / c.2113C>A p.Pro705Thr; chr1:204948591C>A | FNIII | Both | Reduced Nfasc155 protein; abolished CNTN1/CASPR1 aggregation; skin: severe loss of myelinated fibres, partial Nfasc155 loss | Severe; demyelinating + axonal neuropathy | [PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/) |
| Efthymiou F3 (Arab Iraqi) | c.388A>G p.Asn130Asp / c.298A>G p.Asn124Asp; chr1:204923488A>G | Ig-like | Both | Normal surface expression and protein level; MD simulation suggests altered H-bond network | Neonatal hypotonia, severe DD | [PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/) |
| Efthymiou F4 (Israeli, 2 sibs) | c.2458T>C p.Ser820Pro / c.2491T>C p.Ser831Pro; chr1:204951136T>C | FNIII | Both | Reduced Nfasc155 protein; reduced aggregation | Infantile hypotonia, no walk, normal MRI; relatively milder | [PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/) |
| Efthymiou F5 (Saudi, 2 sibs; = Anazi 2017) | c.1076G>C p.Arg359Pro / c.1109G>C p.Arg370Pro; chr1:204939816G>C | Ig-like | Both | Normal protein level; reduced CNTN1/CASPR1 aggregation | Infantile hypotonia; one died at 4 months | [PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/); [PMID:28940097](https://pubmed.ncbi.nlm.nih.gov/28940097/) |
| Efthymiou F6 (Algerian, 2 sibs) | c.3230T>C p.Val1077Ala (NM_001005388 only); chr1:204971817T>C | NF186-specific region | Nfasc186 only | Not functionally tested | Later onset (15–16 months), ataxia, cerebellar atrophy, normal NCS | [PMID:31501903](https://pubmed.ncbi.nlm.nih.gov/31501903/) |
| Monfrini (Italian, 2 sibs) | c.3365T>A p.Val1122Glu (NM_001005388) | Transmembrane domain ("highly conserved hydrophobic transmembrane domain residue") | Numbered on Nfasc186; TM domain is shared | "led to significant loss of Neurofascin protein in the iPSC-derived neurons of affected siblings" | Early-onset cerebellar ataxia + demyelinating neuropathy; spasticity; ID in brother | [PMID:30850329](https://pubmed.ncbi.nlm.nih.gov/30850329/) |
| Kvarnung (Pakistani, 2 sibs) | c.3020-1G>A (NM_001005388), splice acceptor intron 25 → in-frame skipping of exon 26 | NF186-specific exon | Full-length Nfasc186 lost; Nfasc155 non-significant trend down | Fibroblast RT-PCR/qPCR; iPSC neurons: no NF186, reduced ankyrin-G, fewer/shorter neurites, altered Na+ currents | Progressive ataxia, mild weakness, mild cognitive impairment, normal NCS | [PMID:31608123](https://pubmed.ncbi.nlm.nih.gov/31608123/) |
| Farwell Hagman 2017 | Homozygous splice-site variant (details in supplementary data of a diagnostic-lab paper) | — | — | — | "neurodevelopmental impairment, hypotonia and areflexia" (as cited by Efthymiou) | [PMID:28106320](https://pubmed.ncbi.nlm.nih.gov/28106320/) (NFASC not in abstract) |

**Variant classes.** Nonsense (1), frameshift (1), splice-acceptor with in-frame exon skip (2 reported: Kvarnung; Farwell Hagman), missense (6). Germline in all; no somatic or mosaic cases. ACMG classifications in ClinVar: the Smigiel, Efthymiou, and Kvarnung alleles are deposited as pathogenic/likely pathogenic; the full list of 30 P/LP records has not been reviewed allele by allele here.

**Allele frequency.** rs755160624 (Smigiel allele) in gnomAD v2.1: exomes 2/251,448 (AF ≈ 8 × 10⁻⁶), genomes 2/31,386, no homozygotes ([gnomAD](https://gnomad.broadinstitute.org/variant/1-204953187-C-T?dataset=gnomad_r2_1)); Smigiel reported four heterozygotes, "European population frequency of 1 in 21114 subjects". The Efthymiou alleles were absent from 1000G, ESP6500, ExAC and gnomAD (Table 1); the Kvarnung allele "was not present in gnomAD (v2.1)".

**Functional consequence.** Loss of function in every case, with isoform specificity as the discriminating axis. Efthymiou: "Only the p.P939Ter variant strikingly affected the expression of Nfasc155"; "The protein levels of p.P705T, p.S807P and p.P939Ter mutants were found importantly decreased compared to wild-type Nfasc155"; "Both p.P705T and p.P939Ter variants abolished the interaction between Nfasc155 and CNTN1/CASPR1". Nfasc186 surface expression and gliomedin binding were unaffected by any missense variant. Karakaya & Wirth summarise: "Only variants in the fibronectin type III domain significantly reduced protein levels" ([PMID:31560060](https://pubmed.ncbi.nlm.nih.gov/31560060/)). For dismech: `functional_impact_category: LOSS_OF_FUNCTION` (complete, for the NF155-abolishing frameshift and nonsense alleles) or `PARTIAL_LOSS_OF_FUNCTION` (FNIII missense with reduced protein and binding); the Ig-domain missense alleles (N130D, R359P) with normal expression but reduced partner binding are best described as loss of adhesive function rather than reduced abundance.

**Modifier genes, epigenetics, chromosomal abnormalities.** None reported. No *NFASC* deletions/CNVs reported in patients; no methylation data. Not applicable.

---

## 5. Environmental Information

Not applicable. No environmental, lifestyle, or infectious contributors are described. The only acquired "neurofascinopathy" is immune-mediated (IgG4 anti-Nfasc155 / anti-Nfasc186 / pan-neurofascin autoimmune nodopathy), which is a distinct disease with overlapping paranodal pathology (see Section 10, differential diagnosis).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *NFASC* loss-of-function variant** → absent, reduced, or adhesion-dead neurofascin protein. The branch taken depends on which exon is hit (demonstrated: Smigiel, Efthymiou, Kvarnung).

**Branch A: glial Nfasc155 loss (neonatal-onset tier)**

2A. Loss or truncation of Nfasc155 in oligodendrocytes and Schwann cells → **failure of the paranodal ternary complex Nfasc155–CNTN1–CASPR1**. Demonstrated in patients: "Caspr was absent from the paranodes of the proband confirming the disruption of the paranodal junction" (Smigiel); "CASPR1 immunoreactivity was completely absent in the paranodal regions" (Efthymiou patient 3). Demonstrated in vitro: FNIII-domain variants and the frameshift "abolished the interaction between Nfasc155 and CNTN1/CASPR1".
3A. Loss of the paranodal septate-like junction → **loss of axonal domain segregation**: juxtaparanodal Kv1 channels encroach toward the node, nodal Nav clusters loosen. *Inferred from mice* (Pillai 2009: "paranodal axoglial junctions fail to form, axonal domains fail to segregate", [PMID:19185024](https://pubmed.ncbi.nlm.nih.gov/19185024/)); the patient skin biopsy showed "several nodes that appeared larger, however less compacted than in the control skin" and "a granular distribution of Nav ... along the axonal profiles of large fibres devoid of myelin" (Efthymiou).
4A. Domain disorganization → **severely reduced conduction velocity and prolonged latencies** (demonstrated in patients by NCS; mice show ~50% reduction: "we would predict a further 50% reduction in conduction velocities in these peripheral nerves", Smigiel).
5A. Unstable paranodes → **length-dependent loss of large myelinated fibres with preserved unmyelinated fibres** (demonstrated in patient skin: "a severe loss of myelinated fibres with a preservation of the unmyelinated ones"; "a severe effect on myelination and/or maintenance of myelin and survival of large fibres, which appears to be length-dependent"). This is the demyelinating-plus-axonal neuropathy on EMG/NCS.
6A. Peripheral conduction failure and fibre loss → **hypotonia, weakness, areflexia, reduced nociception, auditory neuropathy, bulbar and respiratory failure** (demonstrated clinically; the auditory-nerve link is inferred from the ANSD phenotype in the Harper/Efthymiou F2 siblings).
7A. In parallel, loss of oligodendrocyte Nfasc155 → **impaired CNS myelin targeting and sheath growth** (*inferred from zebrafish/mouse*: "loss of oligodendrocyte Neurofascin leads to mistargeting of myelin to cell bodies", Klingseisen 2019, [PMID:31761670](https://pubmed.ncbi.nlm.nih.gov/31761670/)) → **cerebral white matter loss, thin corpus callosum, brainstem atrophy** (demonstrated on MRI) → contributes to global developmental delay, intellectual disability, absent speech, and in some patients spasticity/hyperreflexia (the clinical link is plausible but not mechanistically demonstrated in humans).

**Branch B: neuronal Nfasc186 loss (later-onset ataxic tier)**

2B. Absence of full-length Nfasc186 → **reduced ankyrin-G and failure of axon initial segment (AIS) assembly/maintenance** (demonstrated in patient iPSC neurons: "a significant reduction of ankyrin-G in patient neurons"; mice: adult Purkinje Nfasc inactivation "causes rapid loss of Nfasc186 from the AIS but not from nodes of Ranvier" with AIS disintegration, Zonta 2011, [PMID:21382554](https://pubmed.ncbi.nlm.nih.gov/21382554/)).
3B. AIS failure → **altered neuronal excitability**: patient neurons showed Na⁺ currents "activated at about 10-mV more negative membrane potentials" with lower peak current density (Kvarnung); mouse Purkinje cells lose "the spontaneous tonic discharge typical of Purkinje cells" (Zonta).
4B. Loss of Nfasc186 during neurogenesis → **impaired neurite outgrowth and delayed neuronal maturation** (demonstrated in patient iPSC neurons: "fewer and shorter neurites"; SLIT3 upregulated; DCX/MAP2 under-induced). Contributes to cognitive impairment (inferred).
5B. In cerebellum, Nfasc186 loss in Purkinje and basket cells → **pinceau synapse disorganization, Purkinje degeneration** (*mouse*: Buttermore 2012, [PMID:22492029](https://pubmed.ncbi.nlm.nih.gov/22492029/); Shi 2026, [PMID:42052621](https://pubmed.ncbi.nlm.nih.gov/42052621/), where "Purkinje cell-specific loss of NF186 predominantly activated immune-inflammatory pathways") → **progressive cerebellar ataxia with cerebellar/vermian atrophy** (demonstrated clinically and on MRI in NF186-only patients).
6B. Postnatal Nfasc186 loss at nodes → **progressive nodal destabilization and axonal degeneration** (*mouse*: Taylor 2017, [PMID:28217083](https://pubmed.ncbi.nlm.nih.gov/28217083/)); peripheral nerves were clinically normal in the Kvarnung siblings at 9 and 14 y, so this step is a predicted late risk rather than an observed one ("we cannot exclude subclinical affection of the PNS or the emergence of peripheral symptoms with time").

**Branch C: both isoforms (missense in shared Ig/FNIII exons)** → both A and B operate, with severity scaled by how much protein/binding is lost; Efthymiou's cohort is largely this branch.

### Mechanistic detail by category

- **Protein dysfunction.** Reduced abundance (FNIII missense, frameshift), loss of surface expression (frameshift), or loss of heterophilic adhesion to CNTN1/CASPR1 with normal abundance (Ig-domain missense). Molecular dynamics: "p.N130D results in a slightly compressed mutant" (Efthymiou; COMPUTATIONAL).
- **Cellular processes.** Paranodal junction assembly (GO:0033010), clustering of voltage-gated sodium channels (GO:0045162), protein localization to juxtaparanode (GO:0071205), myelination (GO:0042552; CNS GO:0022010; PNS GO:0022011), myelin maintenance (GO:0043217, PNS GO:0032287), neuronal action potential (GO:0019228), neuron projection development (GO:0031175), axonogenesis (GO:0007409), synapse assembly (GO:0007416), cerebellar Purkinje cell layer development (GO:0021680), neuron apoptotic process (GO:0051402, Purkinje degeneration), cell-cell adhesion (GO:0098609). All verified current in QuickGO and present in `cache/go/terms.csv`.
- **Cellular components.** Node of Ranvier (GO:0033268), paranodal junction (GO:0033010), axon initial segment (GO:0043194), axon (GO:0030424).
- **Cell types.** Oligodendrocyte (CL:0000128), oligodendrocyte precursor cell (CL:0002453; NFASC expression "highest in newly formed oligodendrocytes"), Schwann cell (CL:0002573), neuron (CL:0000540), Purkinje cell (CL:0000121), basket cell (CL:0000118), motor neuron (CL:0000100), sensory neuron (CL:0000101). All in `cache/cl/terms.csv`.
- **Metabolic, immune, epigenetic.** No primary metabolic defect (Smigiel: tandem MS, GC-MS, amino acids, lactate, CK, ammonia all normal). No immune involvement in the genetic disease. Mouse RNA-seq after Purkinje NF186 loss shows secondary immune-inflammatory transcriptional activation (Shi 2026) — a lead, not a human finding.
- **Transcriptomics / expression context.** Efthymiou (GTEx co-expression; COMPUTATIONAL): "NFASC was most highly expressed in oligodendrocytes"; in anterior cingulate cortex NFASC sits in a module "enriched for genes involved in synaptic transmission (GO:0099536 ...)" and "enriched for genes known to be associated with monogenic forms of intellectual disability". No patient transcriptomic, proteomic, metabolomic, single-cell or spatial datasets exist; no GEO accession is specific to this disease.
- **Molecular pathways.** No canonical signalling cascade; this is a structural cell-adhesion / axoglial-junction disorder. KEGG H02990 lists it under nervous-system diseases without a pathway map.

---

## 7. Anatomical Structures Affected

- **Organ/system level.** Nervous system (UBERON:0001016): central nervous system (UBERON:0001017) and peripheral nervous system (UBERON:0000010) both primary. Secondary: respiratory system (respiratory failure, aspiration), gastrointestinal (feeding), auditory system (internal ear/auditory nerve; UBERON:0001846 internal ear is the closest cached term, though the lesion is neural, not cochlear), musculoskeletal (contractures, chest deformity).
- **Regional CNS.** Cerebral hemisphere white matter (UBERON:0002437; white matter UBERON:0002316), corpus callosum (UBERON:0002336), brainstem (UBERON:0002298), cerebellum (UBERON:0002037), cerebellar vermis (UBERON:0004720).
- **PNS.** Peripheral nerve (UBERON:0001021); large myelinated fibres selectively lost, small somatic and autonomic fibres spared (Efthymiou: "small fibres, both somatic and autonomic appeared less affected"). Involvement is bilateral, symmetric, and length-dependent (distal leg worse than thigh and fingertip in patient 3).
- **Cell and subcellular level.** Myelinating glia (oligodendrocyte, Schwann cell) and neurons; paranodal junction, node of Ranvier, axon initial segment, plasma membrane (GO:0005886).

---

## 8. Temporal Development

- **Onset.** Prenatal signs in the most severe case (reduced fetal movements, polyhydramnios; born at 34 weeks). Neonatal or first 6 months in all Nfasc155-affecting and both-isoform cases ("Hypotonia was present from neonatal age in all cases"). Later onset (15–16 months; early childhood) in Nfasc186-only cases. Karakaya & Wirth: "Variants affecting NFASC155 were associated with onset at birth or within 6 months. Variants affecting only NFASC186 were associated with later onset."
- **Course.** Chronic, lifelong, non-remitting. Severe tier: static-to-progressive with early death risk. Ataxic tier: slowly progressive ("progressive motor problems due to a combination of limb weakness ... ataxia, and balance problems"; wheelchair by 12 y). Smigiel describes "severe and progressive neurological disease". Patient 3 MRI: "progressive loss of cerebral white and grey matter".
- **Stages.** None defined. A practical two-phase description for `progression:`: (1) neonatal/infantile hypotonic-respiratory phase; (2) established neurodevelopmental disability with demyelinating neuropathy; and, for the NF186 tier, (1) delayed motor milestones, (2) progressive ataxia with loss of ambulation.
- **Critical periods.** Mouse data place the vulnerable window at the postnatal transition to saltatory conduction (Nfasc-null death at P7; Nfasc155-cKO death at P16–17). No human intervention window is defined.

---

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007); every reported patient homozygous; heterozygous parents unaffected. No compound heterozygotes published.
- **Penetrance / expressivity.** Complete penetrance in homozygotes; marked inter-family variable expressivity explained largely by isoform; intra-family concordance good (sibling pairs in 5 families), with some within-family variation (Saudi sibs: one died at 4 months, one alive at 2.5 y).
- **Anticipation, germline mosaicism, founder effects.** None reported. No recurrent allele across unrelated families.
- **Consanguinity.** Present or cryptic in 8 of ~10 families.
- **Carrier frequency.** Not established; individual alleles are at ≤10⁻⁵ in gnomAD.
- **Prevalence/incidence.** Unknown; about 16 reported patients worldwide as of October 2026. For dismech: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`, with the count in `notes`. No Orphanet epidemiology row exists.
- **Demographics.** Reported from Poland, Morocco, USA, Iraq, Israel, Saudi Arabia, Algeria, Italy, Pakistan, Sweden (Pakistani origin). Sex: roughly 9 male, 7 female; no sex effect. Age range at report: 3 months to 22 years.

---

## 10. Diagnostics

- **Genetic testing (definitive).** Exome or genome sequencing is how every case was diagnosed; a neuromuscular, hereditary ataxia, hypomyelinating leukodystrophy, or hereditary neuropathy panel including *NFASC* is appropriate (NFASC is Green on PanelApp Hereditary ataxia). Splice variants need RNA studies: Kvarnung showed exon 26 skipping by fibroblast RT-PCR and qPCR. No role for CMA, karyotype, FISH, mtDNA, or repeat testing beyond initial exclusion. SMN1/SMN2 MLPA was done first in the Smigiel proband because "proximal spinal muscular atrophy (SMA) was initially suspected".
- **Electrophysiology.** NCS: severely reduced motor and sensory conduction velocities with prolonged motor latencies in the Nfasc155-affecting tier (LOINC codes for NCS exist but none is cached; bind only via `just loinc-seed-cache`). EMG: acute/chronic denervation. Normal NCS does not exclude the NF186 tier. EEG: non-specific slowing without seizures in most. ABR/OAE: auditory neuropathy pattern (Harper 2020).
- **Imaging.** Brain MRI: cerebral white matter loss, thin corpus callosum, brainstem atrophy (NF155 tier); cerebellar/vermian atrophy (NF186 tier); may be normal.
- **Tissue.** Skin punch biopsy with immunofluorescence for pan-neurofascin, Nfasc155, Nfasc186, CASPR1, MBP, and Nav channels is a research-grade confirmatory test: absent paranodal Nfasc155/CASPR with preserved nodal Nfasc186 (Smigiel; Efthymiou). Nerve biopsy not reported.
- **Laboratory.** No biomarker. CK, lactate, ammonia, acylcarnitines, amino acids, CSF amino acids, immunoglobulins all normal (Smigiel). Anti-neurofascin antibody testing is negative by definition but is relevant to the differential.
- **Clinical criteria.** None published. OMIM/HPO synopsis is the de facto reference.
- **Differential diagnosis.** (1) Spinal muscular atrophy — Smigiel: "a lack of response to light and epilepsy indicating involvement of the CNS was not typical for SMA". (2) *CNTNAP1*-related congenital hypomyelinating neuropathy (CHN3) and lethal arthrogryposis — same paranodal complex; Efthymiou: "these patients have a similar phenotype to patients with CNTNAP1/CASPR1 mutations; however, without any epilepsy". The repository entry `Congenital_Hypomyelinating_Neuropathy` already carries a "Paranodal Axo-Glial Junction Failure" node naming NF155. (3) *GLDN* (gliomedin) lethal arthrogryposis (Maluenda 2016, [PMID:27616481](https://pubmed.ncbi.nlm.nih.gov/27616481/)), the nodal partner of Nfasc186. (4) Hypomyelinating leukodystrophies and CMT4/CHN (entries exist in `kb/disorders/`). (5) Autoimmune anti-Nfasc155/pan-neurofascin nodopathy — acquired, antibody-positive, treatable; shares paranodal pathology and, in up to 8% of anti-Nfasc155 CIDP, CNS demyelination. (6) Recessive early-onset ataxias (for the NF186 tier).
- **Screening.** None. Carrier testing and prenatal/preimplantation diagnosis are possible once a familial variant is known.

---

## 11. Outcome / Prognosis

- **Mortality.** Two early deaths reported: Saudi patient 8 "died at the age of 4 months, presumably due to aspiration defects"; the Polish proband was in palliative care at 3 months (outcome not reported). Survival into the third decade occurs in the ataxic tier (Monfrini sister 22 y; Efthymiou patient 9, 21 y). No survival statistics exist.
- **Morbidity and disability.** Severe tier: tracheostomy/ventilation, gastrostomy, no ambulation, no speech, hearing loss. Both-isoform missense tier: non-ambulatory, non-verbal, moderate-severe ID. NF186 tier: ambulant in early childhood, progressive loss of ambulation, dysarthria, mild cognitive impairment, disabling vertigo.
- **Prognostic factors.** Isoform affected and variant class are the only identified predictors: "affected individuals from Family 2 carrying the p.P939Ter frameshift deletion exhibited the more severe phenotype"; FNIII-domain variants reduce protein and are more severe than Ig-domain variants with preserved expression. Residual paranodal Nfasc155 ("the absence of Nfasc155 in the paranodal region was only partial in Patient 1") may predict milder disease.
- **Complications.** Aspiration, respiratory infections, feeding failure, contractures, scoliosis (not reported but expected in non-ambulatory patients; do not assert without a source), hearing loss, seizures (rare).
- **Quality of life instruments.** None applied.

---

## 12. Treatment

There is no disease-modifying therapy. All management is supportive and extrapolated from the individual case reports; no treatment has been formally evaluated.

| Intervention | Reported in | Suggested NCIT term (cached) |
|---|---|---|
| Mechanical ventilation, intubation, tracheostomy | Smigiel 2018; Harper 2020 | Supportive Care NCIT:C15747; Surgical Procedure NCIT:C15329 (tracheostomy, with `preferred_term` carrying the specificity) |
| Percutaneous endoscopic gastrostomy / tube feeding | Smigiel 2018; Efthymiou 2019 (American children) | Nutritional Support NCIT:C15433 (review modality by hand; see CLAUDE.md caution) and Surgical Procedure NCIT:C15329 |
| Antiseizure medication (valproate) | Smigiel 2018: "epilepsy appeared and was treated with valproate" | Pharmacotherapy NCIT:C15986 + `therapeutic_agent` valproic acid CHEBI:39867 (cached) |
| Physiotherapy, occupational therapy, speech therapy, mobility aids (walker, wheelchair) | Kvarnung 2019 (walker/wheelchair); general | Physical Therapy NCIT:C15302; Occupational Therapy NCIT:C121351; Speech Language Therapy NCIT:C159273; Rehabilitation NCIT:C15315 |
| Hearing habilitation for ANSD (amplification, cochlear implant candidacy, early language intervention) | Harper 2020: delays "can impact patient's language acquisition and spoken language skills" | Rehabilitation NCIT:C15315; for a device, follow the cochlear-implant qualifier pattern in CLAUDE.md |
| Palliative care | Smigiel 2018 | Supportive Care NCIT:C15747 |
| Genetic counselling, carrier testing | All families | Genetic Counseling NCIT:C15240 |

**Pharmacogenomics, gene/cell/RNA therapy, targeted or immunotherapy.** None exist or are in development for the genetic disease. Immunotherapies (rituximab, IVIG) apply only to the autoimmune nodopathies and must not be imported.

**Clinical trials.** ClinicalTrials.gov search for "NFASC OR neurofascin" (2026-10-15) returns only four CIDP/combined central-peripheral demyelination studies (NCT04480450, NCT06325943, NCT05877040, NCT04664647); none concerns the genetic disorder.

**Treatment outcomes.** Not reported beyond survival on support.

---

## 13. Prevention

- **Primary.** Genetic counselling in consanguineous families; carrier testing of relatives once a familial variant is known; preimplantation or prenatal diagnosis. No population carrier screening.
- **Secondary.** Early exome sequencing in neonates with hypotonia, areflexia and respiratory failure once SMA is excluded; early audiological assessment (ANSD) to protect language acquisition (Harper 2020).
- **Tertiary.** Respiratory and nutritional support to prevent aspiration death; contracture management; seizure control; hearing habilitation.
- **Immunization, behavioural, public-health, prophylaxis.** Not applicable beyond routine care.

---

## 14. Other Species / Natural Disease

- **Orthologues.** Mouse *Nfasc* (MGI:104753; NCBI Gene 269116), zebrafish *nfasca* and *nfascb*, *Drosophila* *Neuroglian* (*Nrg*, the single L1-family orthologue). NCBITaxon: *Mus musculus* 10090; *Danio rerio* 7955; *Drosophila melanogaster* 7227.
- **Natural disease in animals.** None recorded; OMIA has no NFASC entry to my knowledge, and no veterinary neurofascinopathy was found. No breed, zoonotic, or cross-species transmission aspect applies.
- **Comparative biology.** The paranodal Nfasc155–Caspr–contactin complex and nodal Nfasc186–ankyrin-G–Nav organisation are conserved across jawed vertebrates; Efthymiou notes "the complete conservation down to invertebrates of the amino acid residues affected by the substitutions". Zebrafish nfasca clusters "prefigure the position of a subset of nodes" (Vagionitis 2022, [PMID:35172135](https://pubmed.ncbi.nlm.nih.gov/35172135/)).

---

## 15. Model Organisms

| Model | Isoform(s) lost | Key phenotypes | Fidelity to NEDCPMD | Source |
|---|---|---|---|---|
| *Nfasc*-null mouse | All | Die ~P7 at onset of saltatory conduction; "neither paranodal adhesion junctions nor nodal complexes are formed"; "sodium channels remain diffusely distributed along the axon"; glial Nfasc155 transgene restores paranodes but not nodes | Models the combined-isoform severe tier; lethality precludes neurodevelopmental readouts | Sherman 2005, [PMID:16337912](https://pubmed.ncbi.nlm.nih.gov/16337912/) |
| Nfasc-null + neuronal Nfasc186 or Nfasc140 transgene | Nfasc155 only (effectively) | Survive to adulthood, ataxic, PNS conduction velocity ~50% of normal | Models Nfasc155-only loss with neuronal compensation | Sherman 2005; Zonta 2008 (cited in Smigiel) |
| Glia-specific Nfasc155 cKO (Cnp-Cre / P0-Cre) | Nfasc155 | "severe ataxia, motor paresis, and death before the third postnatal week" (P16–17); conduction velocity roughly halved; transverse bands absent; Caspr/contactin fail to localise; Kv1.1 mislocalised; Purkinje axon swellings | High for Branch A; Smigiel: "the phenotype of our proband reflects the severity of the murine phenotype" | Pillai 2009, [PMID:19185024](https://pubmed.ncbi.nlm.nih.gov/19185024/) |
| Adult-onset Nfasc155 ablation (Plp-CreER) | Nfasc155 | Gradual paranode disorganisation over 60–90 days; CV modestly reduced; Kv1.1 migrates toward node | Models maintenance role; relevant to progression | Pillai 2009 |
| Neuron-specific Nfasc186 cKO | Nfasc186 | Nodes disrupted; "the paranodal domains invade the nodal space"; reduced nodal Nav and ankyrin-G | Branch B nodal component | Thaxton 2011, [PMID:21262464](https://pubmed.ncbi.nlm.nih.gov/21262464/) |
| Postnatal Nfasc186 ± Nfasc155 ablation | Nfasc186; both | "progressive nodal destabilization and axonal degeneration"; Nfasc155 loss alone "does not disrupt nodes"; double loss accelerates | Predicts late PNS involvement in NF186 tier | Taylor 2017, [PMID:28217083](https://pubmed.ncbi.nlm.nih.gov/28217083/) |
| Adult Purkinje-cell Nfasc inactivation | Nfasc186 (AIS) | "rapid loss of Nfasc186 from the AIS but not from nodes of Ranvier"; AIS disintegrates; motor-learning impairment; tonic Purkinje firing abolished; "basic motor abilities remain intact" | Branch B cerebellar component (milder than human) | Zonta 2011, [PMID:21382554](https://pubmed.ncbi.nlm.nih.gov/21382554/) |
| Developmental Purkinje ± basket cell Nfasc cKO | Nfasc186 | AIS maturation blocked; pinceau disorganisation; "Purkinje neuron degeneration, and severe ataxia" | High for the ataxic tier | Buttermore 2012, [PMID:22492029](https://pubmed.ncbi.nlm.nih.gov/22492029/) |
| Purkinje-specific NF186 / AnkG / double cKO | Nfasc186 | AIS cytoskeleton disrupted; Nav/Kv mislocalised P10–30; Purkinje degeneration and cerebellar dysfunction by 2 months; NF186 loss "predominantly activated immune-inflammatory pathways" | Newest cerebellar model | Shi 2026, [PMID:42052621](https://pubmed.ncbi.nlm.nih.gov/42052621/) |
| Zebrafish nfasca mutants / oligodendrocyte Nfasc loss | Glial and neuronal | Myelin mistargeted to cell bodies, reduced sheath growth; longer and irregular internodes | CNS myelination component of Branch A | Klingseisen 2019, [PMID:31761670](https://pubmed.ncbi.nlm.nih.gov/31761670/); Vagionitis 2022, [PMID:35172135](https://pubmed.ncbi.nlm.nih.gov/35172135/) |
| Patient iPSC-derived neurons (c.3020-1G>A) | Nfasc186 | No NF186 mRNA/protein; ankyrin-G reduced; neurites fewer (8 vs 12) and shorter (123 vs 270 µm); SLIT3 up; DCX/MAP2 under-induced; Na⁺ current activates ~10 mV more negative with lower density | Human, IN_VITRO; directly links NF186 loss to neurogenesis and excitability | Kvarnung 2019, [PMID:31608123](https://pubmed.ncbi.nlm.nih.gov/31608123/) |
| Patient iPSC-derived neurons (p.V1122E) | Transmembrane | "significant loss of Neurofascin protein" | Human, IN_VITRO | Monfrini 2019, [PMID:30850329](https://pubmed.ncbi.nlm.nih.gov/30850329/) |
| HEK293 / N2A heterologous assays | Nfasc155, Nfasc186 variants | Surface expression, immunoblot abundance, CNTN1/CASPR1 aggregation, gliomedin binding | IN_VITRO variant functional grading | Efthymiou 2019 |
| 500 ns molecular dynamics of mutant ectodomains (PDB 3P3Y template) | — | p.N130D "slightly compressed"; p.R370P disrupts β-strand H-bond network | COMPUTATIONAL | Efthymiou 2019 |

**Limitations.** No mouse model carries a patient allele; all are null or conditional. Mouse Nfasc155 cKO lethality at P17 is more severe than the human NF155-only phenotype permits study of; adult Purkinje ablation is milder than the human ataxia. None reproduces the human cortical white-matter loss or intellectual disability directly. A `HUMAN_MODEL_MISMATCH` discussion is warranted for the CNS cognitive phenotype.

**Resources.** MGI lists 22 Nfasc alleles (7 targeted, 7 gene-trap, 3 transgenic, 2 endonuclease, 2 chemically induced, 1 radiation) and 24 phenotype annotations ([MGI:104753](https://www.informatics.jax.org/marker/MGI:104753)).

---

## Notes for curation

- **Lump/split.** One `DISEASE` entry anchored to MONDO:0032698 is right; the two tiers are best handled as `has_subtypes` (for example "NF155-deficient" and "NF186-deficient") stratifying onset, neuropathy, MRI pattern, and prognosis, rather than as separate entries. OMIM, MONDO, GenCC and PanelApp all treat it as one disease.
- **Module leads.** `schwann_cell_myelin_maintenance#Nerve Conduction Slowing and Conduction Block` and `#Secondary Axonal Loss and Length-Dependent Deficit` fit Branch A; `cns_myelin_failure#Deficient or Unstable CNS Myelin Sheath` and `#Axonal Degeneration and Progressive White Matter Dysfunction` fit the central white-matter arm; `cerebellar_purkinje_degeneration#Purkinje Neuron Degeneration` → `#Cerebellar Ataxia` fits Branch B. `Congenital_Hypomyelinating_Neuropathy` already has a "Paranodal Axo-Glial Junction Failure" node that is the natural cross-reference for the CNTNAP1 sibling disease.
- **Reference caches present in the worktree:** PMID:30124836, 30850329, 31501903, 31608123, 31945734. Still to fetch if cited: PMID:31560060 (Karakaya & Wirth commentary), 28940097 (Anazi 2017), 19185024, 16337912, 21382554, 22492029, 28217083, 21262464, 31761670, 35172135, 42052621, 27616481.
- **Do not cite:** any `ORPHA:` record (none exists), any `CGGV:` record (ClinGen has not curated NFASC), or trial NCT identifiers (none are relevant).

**Sources consulted (primary):** [Smigiel 2018, Hum Mol Genet](https://pubmed.ncbi.nlm.nih.gov/30124836/) · [Monfrini 2019, Parkinsonism Relat Disord](https://pubmed.ncbi.nlm.nih.gov/30850329/) · [Efthymiou 2019, Brain](https://pubmed.ncbi.nlm.nih.gov/31501903/) · [Karakaya & Wirth 2019, Brain commentary](https://academic.oup.com/brain/article/142/10/2895/5574767) · [Kvarnung 2019, Front Genet](https://pubmed.ncbi.nlm.nih.gov/31608123/) · [Harper 2020, Int J Pediatr Otorhinolaryngol](https://pubmed.ncbi.nlm.nih.gov/31945734/) · [Anazi 2017, Hum Genet](https://pubmed.ncbi.nlm.nih.gov/28940097/) · [Sherman 2005, Neuron](https://pubmed.ncbi.nlm.nih.gov/16337912/) · [Pillai 2009, J Neurosci Res](https://pmc.ncbi.nlm.nih.gov/articles/PMC2837286/) · [Thaxton 2011, Neuron](https://pubmed.ncbi.nlm.nih.gov/21262464/) · [Zonta 2011, Neuron](https://pubmed.ncbi.nlm.nih.gov/21382554/) · [Buttermore 2012, J Neurosci](https://pubmed.ncbi.nlm.nih.gov/22492029/) · [Taylor 2017, Front Cell Neurosci](https://pubmed.ncbi.nlm.nih.gov/28217083/) · [Klingseisen 2019, Dev Cell](https://pubmed.ncbi.nlm.nih.gov/31761670/) · [Vagionitis 2022, Cell Rep](https://pubmed.ncbi.nlm.nih.gov/35172135/) · [Shi 2026, Front Cell Neurosci](https://pubmed.ncbi.nlm.nih.gov/42052621/) · [Maluenda 2016, AJHG](https://pubmed.ncbi.nlm.nih.gov/27616481/) · [MedGen 1674767](https://www.ncbi.nlm.nih.gov/medgen/1674767) · [HPO annotations OMIM:618356](https://ontology.jax.org/api/network/annotation/OMIM:618356) · [GenCC NFASC](https://thegencc.org/genes/HGNC:29866) · [ClinGen NFASC](https://search.clinicalgenome.org/kb/genes/HGNC:29866) · [PanelApp Hereditary ataxia](https://panelapp.genomicsengland.co.uk/panels/20/gene/NFASC/) · [gnomAD NFASC](https://gnomad.broadinstitute.org/gene/ENSG00000163531) · [UniProt O94856](https://www.uniprot.org/uniprotkb/O94856) · [MGI Nfasc](https://www.informatics.jax.org/marker/MGI:104753) · [KEGG H02990](https://www.kegg.jp/entry/H02990)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 1 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 19 |
| On topic | 7 |
| Off topic | 3 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35172135` *(abstract only)*: "prefigure the position of a subset of nodes"
  - closest text in source: "While some of these clusters are pushed into future node position by extending myelin sheaths, others are not and thus prefigure the position of where a mature node forms"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:31761670` (6 mentions) - Oligodendrocyte Neurofascin Independently Regulates Both Myelin Targeting and Sheath Growth in the CNS.
  - shared terms: loss
- `PMID:27616481` (4 mentions) - Mutations in GLDN, Encoding Gliomedin, a Critical Component of the Nodes of Ranvier, Are Responsible for Lethal Arthrogryposis.
  - shared terms: disease, node
- `PMID:35172135` (6 mentions) - Clusters of neuronal neurofascin prefigure the position of a subset of nodes of Ranvier along individual central nervous system axons in vivo.
  - shared terms: node

Weighed against this report's own most characteristic terms: `efthymiou`, `patient`, `smigiel`, `loss`, `nfasc`, `kvarnung`, `paranodal`, `phenotype`, `sibling`, `variant`, `monfrini`, `severe`, `harper`, `nfasc155`, `disease`, `node`, `failure`, `motor`, `ataxia`, `tier`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:31560060`: "hereditary nodo-paranodopathy"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:31560060`: "Only variants in the fibronectin type III domain significantly reduced protein levels"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 122 |
| Resolved | 117 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 21 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001276` (1 mention) - the report calls it "Hypertonia (generalized, upper limb)"; HP calls it **Hypertonia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0031936` (1 mention) - the report calls it "Delayed ability to walk; no independent ambulation"; HP calls it **Delayed ability to walk**
- `HP:0001558` (1 mention) - the report calls it "Decreased fetal movement; polyhydramnios"; HP calls it **Decreased fetal movement**, and lists "Decreased fetal movements" among its other names
- `HP:0000878` (1 mention) - the report calls it "11 pairs of ribs; chest deformity"; HP calls it **11 pairs of ribs**
- `HP:0001187` (1 mention) - the report calls it "Hyperextensibility of finger joints"; HP calls it **Hyperextensibility of the finger joints**
- `HP:0002079` (1 mention) - the report calls it "Hypoplasia / atrophy of corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplasia of corpus callosum" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `MGI`.