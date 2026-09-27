---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T02:42:12.822859'
end_time: '2026-09-04T02:47:31.492150'
duration_seconds: 318.67
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: X-linked Spermatogenic Failure 1
  mondo_id: ''
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
  web_search_requests: 21
  num_turns: 21
  total_cost_usd: 1.4269299999999996
  session_id: fab9582c-86c5-587f-8c13-07e30530b023
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 28
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 17
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 22
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCBITaxon:10090
    reported_labels:
    - Mus musculus
    - Taxonomy:** Modeled primarily in **Mus musculus
    ontology_label: Mus musculus
  obsolete_terms:
  - term_id: MONDO:0010595
    ontology_label: obsolete Sertoli cell-only syndrome
    replaced_by: MONDO:0056795
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked Spermatogenic Failure 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **X-linked Spermatogenic Failure 1** covering all of the
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

I'll research X-linked Spermatogenic Failure 1 (TEX11-related) now, using web search and fetch tools.

I have enough material now to compile a comprehensive, well-cited report. Let me also check the recent M1AP/ZZS EMBO 2025 paper and the mouse model bioRxiv 2026 paper for the most current findings.

I now have sufficient material to write the comprehensive report.

---

# X-linked Spermatogenic Failure 1 (SPGFX1) — Comprehensive Research Report

## Important Nomenclature Note (read first)

Searches for "X-linked Spermatogenic Failure 1" surface **two distinct OMIM entries** that are frequently conflated in secondary sources, and this report distinguishes them explicitly:

| Entry | OMIM # | Gene | Status |
|---|---|---|---|
| **SPGFX1** — Spermatogenic Failure, X-Linked, 1 | **305700** | Not identified | Phenotype-only MIM entry, gene never mapped/cloned |
| SPGFX2 — Spermatogenic Failure, X-Linked, 2 | 309120 | **TEX11** (Xq13.1) | Molecularly defined, extensively characterized |

**SPGFX1 (305700)** is a legacy OMIM phenotypic entry describing familial (pedigree-based) evidence for an X-linked pattern of **Sertoli cell-only (SCO) syndrome / germ cell aplasia** causing male infertility. Critically, **no causal gene has ever been mapped or cloned for this specific entry** — it remains a "phenotype description, X-linked" MIM number based on clinical pedigrees showing affected males and obligate/presumed carrier relationships, not a gene-based diagnosis [omim.org/entry/305700](https://omim.org/entry/305700). This is a common and important gap in the X-linked spermatogenic failure series: OMIM has assigned numbers SPGFX1 through SPGFX9 (305700, 309120, 301059, 301077, 301099, 301101, 301106, 301119, 301137), but only a subset (notably SPGFX2/TEX11) have a confirmed molecular basis; several others in the series remain phenotype-only or map to genes such as **TEX15, MAGEB4/USP26-linked regions, ZNF711,** and other Xq loci depending on the specific number, reflecting the deep genetic heterogeneity of X-linked non-obstructive azoospermia (NOA).

Because SPGFX1 itself has **no established molecular/mechanistic literature to report** — precisely the situation dismech's curation stub queue and design-decisions register would flag as "OUT_OF_SCOPE or awaiting a causal gene" — the bulk of this report addresses the **molecularly and mechanistically characterized X-linked spermatogenic-failure disorder that is almost certainly the intended curation target**, **SPGFX2/TEX11 (OMIM 309120)**, while explicitly flagging where content is specific to the gene-mapped entry versus the unmapped SPGFX1 phenotype. This distinction should be verified against the current OMIM/MONDO record before knowledge-base curation, since OMIM numbering and "SPGFX-N" labels have shifted historically as genes were identified.

---

## 1. Disease Information

**Overview.** X-linked spermatogenic failure comprises a genetically heterogeneous group of Mendelian, X-linked causes of isolated male infertility due to **azoospermia** (absence of sperm in ejaculate) or severe **oligozoospermia**, without other syndromic features, ambiguous genitalia, or disorders of sex development. Affected men are phenotypically normal males (46,XY) with normal secondary sexual characteristics and normal androgenization; the defect is restricted to spermatogenesis.

- **SPGFX1 (305700):** Clinically defined as **Sertoli cell-only syndrome (germ cell aplasia)** — seminiferous tubules lined solely by Sertoli cells, with no germ cells (SCO type I) or germ cells present in only a minority of tubules with subsequent degeneration (SCO type II). Men present with infertility, normal androgenization, moderately small testes (10–20 mL), normal testosterone/LH, and selectively **elevated FSH**. Diagnosis requires testicular biopsy. Etiology is hypothesized to involve failure of gonocyte migration/colonization of the gonad in some cases, versus germ-cell loss during/after puberty in others (MalaCards summary of OMIM 305700).
- **SPGFX2/TEX11 (309120):** Clinically defined by **azoospermia or severe oligozoospermia due to meiotic arrest**, with testicular histology showing **mixed testicular atrophy** (tubules ranging from meiotic arrest to Sertoli-cell-only) rather than uniform SCO.

**Key identifiers:**
- OMIM: 305700 (SPGFX1, phenotype only); 309120 (SPGFX2, TEX11); gene locus *300311 (TEX11)
- Gene: TEX11 (HGNC:11733), Xq13.1
- MONDO: MONDO:0010595 has been associated with X-linked SCO/germ cell aplasia in cross-referenced sources; the TEX11-specific disorder maps to its own MONDO term (verify current MONDO cross-reference at curation time — do not hand-assign without OAK/MONDO lookup, per this repository's ontology-term policy)
- ICD-10-CM: **N46.0** Azoospermia (with subcodes N46.01 Organic azoospermia, N46.02x by extratesticular cause); no dedicated ICD-10 code exists for the specific genetic subtype
- MeSH: Azoospermia (D053917); Meiosis; Spermatogenesis
- Synonyms: SPGFX1 — "germinal cell aplasia, X-linked," "Sertoli-cell-only syndrome, X-linked," "Del Castillo syndrome" (used loosely/non-specifically in older literature for SCO in general, not X-linked-specific); SPGFX2/TEX11 — "meiotic arrest, TEX11-related," "azoospermia due to TEX11 mutation"

**Evidence basis:** Predominantly aggregated disease-level literature (case series, cohort screens of NOA patients, family/pedigree reports) rather than large-scale EHR data, reflecting the rare, specialist-diagnosed nature of the condition (diagnosis requires testicular biopsy and/or genetic testing in an infertility clinic setting).

---

## 2. Etiology

**Disease causal factors.** Purely genetic/Mendelian — an X-linked recessive defect in spermatogenesis-specific gene function. No environmental, infectious, or acquired cause defines this entry (as distinct from acquired/idiopathic NOA).

**Genetic risk factors:**
- **TEX11** hemizygous loss-of-function variants (nonsense, frameshift, splice-site, and select missense/in-frame deletions) are the principal identified cause for SPGFX2. A landmark 2015 NEJM study (Yatsenko et al., PMID not directly retrieved but corresponding EMBO Mol Med companion paper PMID:26136358) screened 240 men with azoospermia due to meiotic arrest and found **TEX11 mutations in ~1% of unselected azoospermic men and up to 2.4% of men with meiotic-arrest histology** — the largest-known single-gene cause of meiotic-arrest azoospermia at the time.
- Subsequent cohort sequencing (Yang et al., cited via PMC10140331) found a "significantly high prevalence of singleton variants in azoospermic men (7.3%)" in a screen of 246 azoospermic men, though the same study cautioned that many singleton missense variants found in fertile controls are not causally linked — underscoring that **variant classification (pathogenic vs. VUS) is critical** and TEX11 sequence variation must be interpreted against control-cohort background rates.
- A copy-number deletion, **exons 10–12 (c.652del237bp / "607del237bp")**, removing 79 amino acids from the meiosis-specific SPO22/TEX11-domain, was among the first pathogenic TEX11 lesions described via array-CGH (Yatsenko et al. 2015) and remains a recurrent, well-studied allele — most recently re-examined by *in vitro* and *in silico* functional study (Genes, 2025; PMC12652577) questioning/confirming its pathogenicity mechanism.
- **ZZS-complex paralog genes** — **SHOC1** and **SPO16** (TEX11's obligate complex partners) — and the interacting autosomal gene **M1AP** cause phenotypically similar or distinguishable meiotic-arrest NOA; a 2025 Andrology study (Ma et al., DOI 10.1111/andr.70291) and a 2025 EMBO Molecular Medicine study (DOI 10.1038/s44321-025-00244-0) directly compared genotype-phenotype relationships across **TEX11/SHOC1/SPO16 ("ZZS deficiency")** versus **M1AP** loss-of-function, finding ZZS-deficient men show **early meiotic arrest**, while M1AP-deficient men show a **later metaphase I arrest** with occasional haploid spermatid production — an important differential-diagnostic and prognostic distinction for sperm-retrieval counseling.
- Overall, TEX11 is one of dozens of genes implicated in monogenic NOA (others include **MEIOB, HFM1, MSH5, REC114, DMRT1, SYCP2, STAG3, TEX15**), reflecting extreme locus heterogeneity in meiotic-arrest azoospermia.

**Genetic risk factor — inheritance mode.** X-linked recessive. Affected males are hemizygous for the causal TEX11 allele; because they are typically infertile without medical intervention, **de novo mutation or maternal carrier transmission** are the expected origins, and the condition is not usually observed to segregate across multiple generations of a pedigree in the classic sense (unlike autosomal-dominant conditions) — although reported multiplex families (e.g., infertile brothers, BMC Med Genet 2018, PMC5902858) demonstrate maternal transmission to more than one son.

**Environmental/lifestyle risk factors:** Not applicable to the TEX11/genetic subtype specifically — these are separate contributors to the broader idiopathic-NOA differential (heat exposure, gonadotoxins, varicocele, cryptorchidism, chemotherapy/radiation, endocrine disruptors) but are not causal for the monogenic disorder itself; a genetic diagnosis by definition excludes/supersedes these as the operative cause in a given patient, though co-occurrence is possible and not systematically studied.

**Protective factors:** None specific to this monogenic cause is established in the literature; there is no known genetic modifier that rescues TEX11-null spermatogenesis in humans.

**Gene-environment interactions:** Not established for TEX11; largely unstudied given the rarity of confirmed cases and difficulty separating genetic from environmental contributions in azoospermia cohorts.

---

## 3. Phenotypes

| Phenotype | Type | Onset/Frequency | Suggested HPO term |
|---|---|---|---|
| Azoospermia | Laboratory/clinical sign | Adult (ascertained at infertility workup); universal in confirmed cases | **HP:0000027** Azoospermia |
| Severe oligozoospermia (in less-severe allelic variants) | Laboratory | Adult; variable, minority of cases | **HP:0000798** Oligospermia |
| Meiotic arrest (spermatocyte arrest, typically pachytene/early-to-mid meiosis I for ZZS genes) | Histopathologic/laboratory | Adult; characteristic of TEX11/ZZS-related disease | Related to **HP:0010461** Oligospermia / meiotic-arrest terms are not finely subdivided in current HPO — best available: **HP:0000798**; consider free-text/GO-linked annotation for "meiotic arrest" |
| Mixed testicular atrophy (histology: tubules ranging from meiotic arrest to Sertoli-cell-only, ± hypospermatogenesis) | Histopathologic sign | Adult | **HP:0008734** Small testis (associated finding); histology itself is not directly HPO-coded |
| Sertoli-cell-only pattern (SPGFX1, and a subset of TEX11 cases) | Histopathologic sign | Adult | **HP:0000798**/testicular biopsy finding; no precise dedicated HPO term for SCO pattern specifically |
| Small/moderately reduced testicular volume (10–20 mL) | Physical/clinical sign | Adult | **HP:0008734** Small testis |
| Elevated serum FSH | Laboratory abnormality | Adult | **HP:0008730** Abnormal circulating follicle stimulating hormone level (elevated) |
| Normal testosterone and LH | Laboratory (normal) | — | N/A (normal finding, documents intact Leydig-cell/HPG axis function) |
| Normal secondary sexual characteristics / normal androgenization | Physical | — | Absence of virilization defect; distinguishes from Klinefelter and other DSDs |
| Normal karyotype (46,XY) | Cytogenetic | — | Distinguishes from Klinefelter syndrome (47,XXY), which is the leading cytogenetic differential |

**Severity and progression:** The phenotype is stable and non-progressive in the sense that it is a congenital, lifelong meiotic defect rather than a degenerative process; however, testicular histology across tubules within one testis is often mosaic ("mixed testicular atrophy"), meaning some tubules retain rare foci of more advanced spermatogenesis, which is directly relevant to sperm-retrieval prognosis (see Treatment/Diagnostics sections).

**Quality of life impact:** Primary impact is **psychosocial and reproductive** — infertility distress, and for many patients, dependence on assisted reproduction or third-party reproduction (donor sperm) for biological parenthood. No direct impact on general health, life expectancy, sexual function, or somatic development has been reported; this is an isolated reproductive-tract phenotype.

---

## 4. Genetic/Molecular Information

**Causal gene (SPGFX2):** **TEX11** ("testis expressed 11"), HGNC:11733, Xq13.1, gene OMIM *300311. Encodes a 947-amino-acid, testis-restricted meiotic protein.

**Protein function and domain structure.** TEX11 is the mammalian ortholog of the budding-yeast ZMM protein **Zip4**. It contains a **meiosis-specific sporulation domain (SPO22-like)**. TEX11 forms discrete immunocytochemical foci on synapsed meiotic chromosomes and is a physical constituent of recombination/meiotic nodules.

**Variant spectrum (SPGFX2/TEX11):**
- Nonsense and frameshift mutations → protein truncation, associated with defective SPO22/meiosis-specific domain — generally the most clearly pathogenic class, correlating with complete meiotic arrest in both human and CRISPR mouse models.
- Splice-site mutations.
- Missense mutations — pathogenicity more variable/uncertain; population screening finds missense TEX11 variants in fertile controls as well, so **ACMG/AMP-style classification per variant is essential** rather than assuming all TEX11 missense changes are causal (Yang et al., cited above).
- In-frame exonic deletion: **c.652del237bp** (loss of exons 10–12, 79-aa deletion within the SPO22 domain) — first described by array-CGH (Yatsenko 2015); its pathogenic mechanism was re-examined by a 2025 *in vitro*/*in silico* functional study.
- Estimated contribution: **TEX11 mutations account for ~1–2.4% of nonobstructive azoospermia with meiotic arrest**, and roughly **1% of unselected NOA cohorts** overall, making it one of the most frequent single-gene causes identified to date for this histologic subtype.

**Functional consequence:** Predominantly **loss of function**. TEX11 is required as part of the trimeric **"ZZS" complex** (TEX11–SHOC1–SPO16, orthologous to yeast Zip4–Zip2–Spo16) that couples **synaptonemal complex assembly to Class-I crossover formation** during meiotic prophase I. Loss of TEX11 causes **chromosomal asynapsis and reduced crossover formation**, triggering meiotic checkpoint-mediated elimination of spermatocytes at **pachytene and metaphase/anaphase I** — this is the direct molecular-to-cellular mechanistic link between the gene defect and the azoospermia phenotype.

**Modifier genes / interacting loci:** **SHOC1** and **SPO16** (ZZS complex partners) and **M1AP** (an interacting autosomal protein that promotes Class-I crossover formation alongside the ZZS complex) — pathogenic variants in any of these genes produce a related but genotype-distinguishable meiotic-arrest phenotype (early arrest for ZZS-gene defects vs. later metaphase-I arrest with rare haploid cells for M1AP defects), per the 2025 EMBO Molecular Medicine genotype-phenotype study.

**Population/allele frequency:** TEX11 pathogenic loss-of-function alleles are, as expected for a fertility-limiting X-linked recessive trait, rare/absent in general population reference databases such as gnomAD (consistent with strong purifying/reproductive selection against transmission, since affected hemizygous males are naturally infertile). Systematic gnomAD constraint metrics were not retrieved in this pass and should be checked directly in gnomAD/ClinVar at curation time.

**Epigenetics/chromosomal abnormalities:** No specific DNA-methylation or histone-modification signature has been reported as causal for TEX11-related disease; the defect is a primary loss-of-function protein/meiotic-machinery lesion rather than an epigenetic disorder. No recurrent chromosomal rearrangement (aside from the exon 10–12 deletion noted above) is described.

**SPGFX1 (305700) molecular information:** **None available** — no gene has been mapped for this OMIM entry; it remains defined purely by clinical/pedigree phenotype (X-linked pattern of SCO-syndrome infertility). This is a genuine, reportable knowledge gap rather than an omission in this research pass.

---

## 5. Environmental Information

Not applicable as a cause of the monogenic disorder itself. General environmental/lifestyle contributors to non-obstructive azoospermia as a category (heat, gonadotoxic chemotherapy/radiation, endocrine-disrupting chemicals, smoking, obesity) are documented in the broader NOA literature but are not specifically implicated in TEX11-mutation-positive or SPGFX1 cases, and no gene-environment interaction study for TEX11 was identified in this search.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (TEX11/SPGFX2 — the molecularly defined disorder):**

1. Hemizygous **TEX11 loss-of-function variant** (nonsense/frameshift/splice/exonic deletion) → **absence or non-functional TEX11 protein** in spermatocytes. *(Directly demonstrated: immunostaining shows TEX11 protein absent in patient testis tissue with truncating mutations, PMC8491544.)*
2. Loss of functional TEX11 **disrupts assembly of the ZZS complex** (TEX11–SHOC1–SPO16), which normally localizes to recombination intermediates on meiotic chromosome axes. *(Demonstrated in mouse and yeast homolog studies; inferred as the mechanism in human cells based on cross-species conservation.)*
3. ZZS-complex failure → **impaired coupling of synaptonemal-complex assembly to Class-I crossover formation**, and TEX11 loss additionally **delays repair of programmed meiotic double-strand breaks (DSBs)**. *(Demonstrated in Tex11-knockout mice, PMID:26136358.)*
4. This produces **chromosomal asynapsis** (failure of homologous chromosome pairing) and a **genome-wide reduction in crossover/chiasma frequency**. *(Demonstrated in mouse; strongly inferred in human based on the shared molecular mechanism and observed cytogenetic/histologic parallels.)*
5. Unrepaired DSBs and unsynapsed/achiasmate chromosomes **trigger the meiotic pachytene checkpoint**, leading to **apoptotic elimination of spermatocytes**, predominantly at the **pachytene and metaphase/anaphase I stages** of meiosis I. *(Demonstrated — this is the direct cytological finding in both human testis biopsy and mouse models.)*
6. Loss of the spermatocyte population at these stages → **failure of progression to secondary spermatocytes, spermatids, and mature spermatozoa**, producing histologic **meiotic arrest**, often admixed across tubules with **Sertoli-cell-only** tubules (where germ cells are entirely absent) — the "**mixed testicular atrophy**" pattern characteristic of TEX11 disease. *(Demonstrated on testis biopsy.)*
7. Absence of mature spermatozoa in the ejaculate → clinical **azoospermia**, with compensatory **elevated FSH** (loss of germ-cell-derived inhibin B feedback on the pituitary) and **preserved testosterone/LH** (Leydig cell/steroidogenic axis unaffected, since the lesion is germ-cell-intrinsic). *(Demonstrated — routine clinical/hormonal finding.)*

**Branch point — genotype-dependent severity:** Loss-of-function TEX11 variants (frameshift/nonsense) produce **complete, early meiotic arrest and full infertility** in both mouse models and men; certain missense or partial in-frame-deletion alleles may permit **partial/leaky spermatogenesis** with rare mature sperm production, which is clinically important for sperm-retrieval prognosis (see Treatment, below). The 2025 EMBO Mol Med study further demonstrates a mechanistic branch by paralog: **ZZS-gene defects (TEX11/SHOC1/SPO16) → early meiotic arrest**, whereas **M1AP defects → later, metaphase-I arrest with occasional haploid spermatid output** — i.e., the same general recombination-failure pathway but with a distinguishable "how far cells get" phenotype depending on which node of the pathway is disrupted.

**Molecular pathways:** Meiotic homologous recombination / Class-I (interference-sensitive) crossover pathway; synaptonemal complex assembly (SYCP1/SYCP2/SYCP3/SYCE-family proteins); TEX11 physically interacts with **SYCP2** in vivo, providing a proposed molecular link between chromosomal synapsis and recombination machinery.

**Cellular processes:** Meiotic prophase I progression (leptotene→zygotene→pachytene→diplotene), homologous chromosome synapsis, DNA double-strand break formation and repair (via SPO11-initiated DSBs, RAD51/DMC1-mediated strand invasion), crossover/chiasma formation, and **meiotic checkpoint-triggered apoptosis** of defective spermatocytes.

**Protein dysfunction:** Loss of function of a meiosis-specific recombination-complex scaffold protein (TEX11), rather than misfolding/aggregation or a gain-of-function mechanism.

**Suggested ontology terms:**
- GO (biological process): **GO:0007129** synapsis; **GO:0000724** double-strand break repair via homologous recombination; **GO:0007140** male meiotic nuclear division; **GO:0007140/GO:0051321** meiotic cell cycle; crossover formation processes.
- GO (cellular component): synaptonemal complex (**GO:0000795**).
- CL (cell types): **CL:0000017** spermatocyte (and more specific: primary spermatocyte, pachytene spermatocyte if a finer term is required); **CL:0000020** spermatogonium (upstream, unaffected population); **CL:0000216** Sertoli cell.
- UBERON: **UBERON:0000473** testis; **UBERON:0001301** seminiferous tubule.
- HGNC: TEX11 (HGNC:11733), SHOC1 (HGNC:29403 — verify), SPO16, M1AP.

**Single-cell/omics context:** Human testis single-cell RNA-seq atlases (Human Cell Atlas testis datasets) have characterized normal spermatogenic-lineage trajectories and are the appropriate reference for interpreting TEX11-deficient testis transcriptomic/spatial data, though a TEX11-specific single-cell study of patient tissue was not retrieved in this search pass and should be checked directly in GEO/CELLxGENE at curation time.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Testis** (bilateral) — the sole primary site of pathology. No other organ system is affected; this is an isolated reproductive-tract/gonadal phenotype.
- **Organ level (secondary):** None directly damaged; downstream/secondary consequences are functional (infertility) rather than additional organ pathology. The **epididymis** is anatomically normal but functionally irrelevant to sperm output given the absence of testicular sperm production (obstructive causes are explicitly excluded in this differential).
- **Body systems:** Male reproductive system only; endocrine (hypothalamic-pituitary-gonadal axis) is secondarily perturbed only at the hormonal level (elevated FSH) without primary pathology in the hypothalamus/pituitary.
- **Tissue/cell level:** Seminiferous tubule epithelium — specifically the germ-cell lineage (spermatogonia → spermatocytes) is lost/arrested; the somatic **Sertoli cells** persist and structurally support the (empty or arrested) tubules; **Leydig cells** in the interstitium remain functionally intact (normal testosterone).
- **Cell populations (CL terms):** Primary spermatocyte (**CL:0000018**/pachytene spermatocyte), spermatogonium (**CL:0000020**), Sertoli cell (**CL:0000216**), Leydig cell (**CL:0000178**).
- **Subcellular level:** Meiotic chromosome axis / synaptonemal complex (nuclear, **GO:0000795**); the causal lesion operates at chromatin/nuclear structures during meiotic prophase I, not in cytoplasmic organelles.
- **Localization:** Bilateral, generally symmetric testicular involvement; no lateralization pattern reported. Within each testis, involvement is characteristically **mosaic/heterogeneous** across seminiferous tubules ("mixed testicular atrophy").

---

## 8. Temporal Development

- **Onset:** The molecular/meiotic lesion is present from puberty onward (spermatogenesis, and thus meiosis, does not occur before puberty), but clinically the condition is **ascertained in adulthood**, typically during a couple's infertility workup (commonly late 20s–40s). It is not congenital in the sense of being present/detectable at birth (karyotype and genitalia are normal), though the causal genetic variant is present from conception.
- **Progression:** The underlying meiotic block is a **fixed, non-progressive developmental defect** rather than a degenerative disease course — it does not worsen over the patient's reproductive lifespan in the way an acquired or age-related condition would, though clinicians should note some non-genetic causes of NOA (e.g., varicocele) can be progressive; the monogenic TEX11 defect itself is not known to be progressive.
- **Disease course pattern:** Stable/lifelong; not episodic, relapsing-remitting, or fluctuating.
- **Duration:** Lifelong (permanent infertility via natural conception) unless circumvented by assisted reproductive technology using surgically retrieved sperm.
- **Remission:** No spontaneous or treatment-induced remission of the underlying meiotic defect is described; management targets sperm retrieval/assisted reproduction rather than restoring endogenous fertility.
- **Critical periods:** None identified for intervention/prevention, since this is a germline genetic lesion rather than a modifiable exposure-driven process; the only "intervention window" of practical relevance is the timing of surgical sperm retrieval and cryopreservation relative to a couple's reproductive planning.

---

## 9. Inheritance and Population

- **Epidemiology:** Non-obstructive azoospermia (NOA) as a category affects **~1% of all men** and **~10–15% of infertile men** (obstructive azoospermia accounts for ~40% of azoospermia cases, NOA for ~60%). Within NOA cohorts specifically ascertained for **meiotic-arrest histology**, **TEX11 mutations account for roughly 1–2.4%**, and TEX11 variants overall are found in up to ~1% of unselected azoospermic men — making it one of the more frequent single monogenic causes identified for this phenotype, though still individually rare in absolute population terms.
- **Inheritance pattern:** **X-linked recessive** for SPGFX2/TEX11 (and presumed X-linked for SPGFX1, based on pedigree evidence, though no gene is mapped). Affected males are hemizygous.
- **Penetrance:** Reported as high/complete for clearly loss-of-function (truncating) alleles based on mouse and human correlation, but genotype-phenotype studies show variable expressivity for missense and certain in-frame variants (some producing partial spermatogenesis rather than complete arrest) — formal penetrance estimates are not established with population-level precision given the rarity and ascertainment bias (nearly all reported cases come from infertility clinics).
- **Expressivity:** Variable — histologic severity ranges from complete Sertoli-cell-only pattern to mixed testicular atrophy with rare mature sperm, correlating loosely with variant type (truncating vs. missense/in-frame).
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented for TEX11, though theoretically possible as for any X-linked condition; multiplex-brother families (e.g., PMC5902858) are explained by inheritance from a heterozygous carrier mother rather than mosaicism.
- **Founder effects:** No specific population founder allele reported; variants described across Chinese Han, Iranian, and other cohorts appear largely independent/private (many are "singleton" variants per cohort screening studies), consistent with ongoing new-mutation input given that affected males rarely reproduce without ART.
- **Carrier frequency:** Not established in population screening databases; because carrier mothers are typically fertile and asymptomatic (X-inactivation mosaicism in somatic/ovarian tissue), population carrier frequency is unknown and not routinely tested outside of an affected male's family.
- **Consanguinity role:** Not specifically emphasized for this X-linked (as opposed to autosomal-recessive) disorder in the retrieved literature, since a single maternal X-linked allele is sufficient for male disease — consanguinity is more relevant to the many *autosomal*-recessive meiotic-arrest NOA genes (e.g., HFM1, MSH5, MEIOB) than to TEX11.
- **Population demographics:** Cases have been reported across diverse populations, including Chinese Han (PMC8491544), Iranian (PMC8897944), and other cohorts; no specific ethnic enrichment or geographic endemicity is established — this reflects broadly distributed private mutations rather than a population-specific founder variant.
- **Sex ratio:** By definition, this is a **male-only** phenotype (X-linked recessive with male-restricted clinical manifestation as azoospermia); female carriers are not reported to have a reproductive or other phenotype.
- **Age distribution:** Clinical ascertainment occurs in reproductive-age adult men (typically 20s–40s) presenting for infertility evaluation.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Semen analysis** (repeated, per WHO criteria) confirming azoospermia (or severe oligozoospermia).
- **Hormonal panel:** elevated FSH with normal LH and testosterone — a pattern indicating primary (testicular) rather than obstructive or hypothalamic-pituitary cause; LOINC codes exist for FSH (e.g., LOINC 2731-3 Follicle stimulating hormone [Units/volume] in Serum or Plasma) and are directly applicable.
- **Karyotype:** essential first-line test — must be **normal 46,XY** to distinguish this monogenic disorder from **Klinefelter syndrome (47,XXY)**, the most common chromosomal cause of NOA, and from other sex-chromosome aneuploidies.
- **Y-chromosome microdeletion (AZFa/AZFb/AZFc) testing:** essential to exclude the classic Y-linked/AZF causes of NOA, which are far more commonly tested clinically than single-gene X-linked panels; a normal AZF result supports proceeding to autosomal/X-linked gene panel testing.
- **Testicular biopsy/histopathology:** the definitive diagnostic step distinguishing SCO-only (SPGFX1-type) from **meiotic arrest with mixed testicular atrophy** (TEX11/SPGFX2-type) — histologic pattern is also directly prognostic for sperm-retrieval success (see below).

**Genetic testing:**
- **Targeted TEX11 sequencing** (all coding exons) is commercially available as a clinical genetic test (e.g., GTR test ID 579471, "TEX11 gene Sequence Analysis-All Coding Exons," postnatal).
- **Exome-based male-infertility gene panels** including AR, DMRT1, M1AP, TEX11, NR5A1, and others report a **diagnostic yield of ~8.5%** in previously genetically unexplained azoospermia cases (per a cited exome-panel study).
- **Whole-exome sequencing (WES)** is increasingly used in the NOA diagnostic workup and has identified TEX11 along with CFTR and DMRT1 as clinically informative findings that may also help predict sperm-retrieval success; a 2025 systematic review/meta-analysis (PLOS ONE) formally evaluated the **diagnostic yield of exome sequencing in NOA**.
- **Array-CGH/CNV analysis** was the original method by which the TEX11 exon 10–12 deletion was discovered and remains relevant for detecting exonic copy-number lesions not caught by standard exon sequencing.
- Chromosomal microarray, mitochondrial DNA testing, and repeat-expansion testing are not specifically indicated for this disorder.

**Differential diagnosis:**
- **Klinefelter syndrome (47,XXY)** — most common chromosomal cause of NOA; excluded by karyotype.
- **Y-chromosome AZF microdeletions** — excluded by Y-microdeletion PCR panel.
- Other monogenic meiotic-arrest genes (autosomal): **HFM1, MSH5, MEIOB, REC114, STAG3, SYCE1**, etc. — clinically indistinguishable without gene-panel/exome testing; histology alone (meiotic arrest pattern) cannot pinpoint the specific gene.
- **SHOC1, SPO16, M1AP** — genetically and mechanistically related ZZS-pathway/interacting genes producing a similar-but-distinguishable (per 2025 genotype-phenotype study) meiotic-arrest phenotype.
- Acquired/idiopathic NOA (varicocele, cryptorchidism history, gonadotoxin exposure, post-infectious) — excluded by history and by absence of an identified pathogenic variant.
- Obstructive azoospermia — excluded by normal FSH/testicular volume and clinical exam (though genetic and obstructive causes are formally distinguished by biopsy/hormonal profile, as reviewed in a 2025 Asian Journal of Andrology paper on "Differentiation between nonobstructive azoospermia and obstructive azoospermia: then and now").

**Screening:** No population or newborn screening applies (adult-onset ascertainment, isolated reproductive phenotype). Once a proband is identified, **cascade genetic counseling** for maternal relatives (assessing carrier status in the mother and any sisters, for their own future reproductive/family-planning counseling, since carrier daughters could transmit the allele to sons) is the relevant "screening" context, though this was not directly documented with formal guideline citations in this search pass.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No excess mortality or reduced life expectancy is associated with this disorder — it is not a systemic disease. Not applicable.
- **Morbidity:** Morbidity is confined to infertility and its psychosocial sequelae; no physical disability or organ dysfunction outside the reproductive axis.
- **Quality of life:** Impact is specifically on reproductive well-being/family-building; general health-related quality of life is not otherwise impaired. No disease-specific validated QoL instrument for this condition was identified in this search; general infertility-distress instruments would be the applicable proxy.
- **Complications:** None directly attributable to the genetic lesion itself; complications relevant to management relate instead to surgical sperm-retrieval procedures (standard microTESE risks: bleeding, hematoma, transient testosterone reduction) rather than to the underlying disease process.
- **Recovery potential:** Endogenous fertility does not recover; "recovery" in practical terms means successful surgical sperm retrieval enabling assisted reproduction.
- **Prognostic factors for sperm retrieval (micro-TESE):** **Testicular histology is the dominant prognostic factor.** Reported micro-TESE sperm-retrieval success rates by histologic pattern (from cited 2025 review, PMC12055743):
  - Hypospermatogenesis: **~100%** retrieval success
  - Testicular degeneration/atrophy: **~36.4%**
  - Post-meiotic arrest: **~33.3%**
  - Pre-meiotic arrest: **~16.7%**
  - Sertoli-cell-only syndrome: **~8.3%**
  - Meiotic arrest: **~8.7%**
  
  Because TEX11-related disease characteristically produces **meiotic arrest and/or Sertoli-cell-only histology**, retrieval success is generally **low (roughly 8–9%)**, and men carrying pathogenic variants in genes essential for meiosis are "theoretically unlikely to yield viable sperm through TESE" (per cited 2025 review) — although mosaic "mixed testicular atrophy" foci mean retrieval is not impossible, and **TEX11 genotype has been proposed as a prognostic biomarker** to help set patient expectations before pursuing micro-TESE.
- **Prognostic biomarkers:** Confirmed TEX11 (or ZZS/M1AP) pathogenic genotype itself functions as a prognostic marker for micro-TESE outcome counseling, per multiple cited sources.

---

## 12. Treatment

There is **no treatment that restores or induces endogenous spermatogenesis** for this genetic disorder — management is entirely oriented toward assisted reproduction using surgically retrieved sperm (where possible) or third-party reproduction/adoption.

- **Surgical/interventional:** **Microdissection testicular sperm extraction (micro-TESE)** is the standard-of-care intervention to identify and retrieve any focal areas of sperm production for use in **intracytoplasmic sperm injection (ICSI)**. NCIT term: **NCIT:C15329** (Surgical Procedure); more specific device/procedure-coded terms for TESE specifically should be confirmed in NCIT at curation time.
- **Assisted reproductive technology:** **ICSI** following successful sperm retrieval is the definitive fertility-restoring intervention when any mature sperm can be found. NCIT: consider **NCIT:C15746**/relevant ART procedure term (verify exact code via OAK search at curation time; not independently confirmed in this pass).
- **Pharmacotherapy:** No disease-modifying or spermatogenesis-inducing drug therapy exists for this monogenic cause; empiric hormonal therapies used in some NOA contexts (e.g., clomiphene, aromatase inhibitors, gonadotropins) are generally directed at hypogonadotropic or secondary causes and are **not expected to be effective** when the defect is a primary, cell-intrinsic meiotic-recombination failure, though this was not directly documented as formally studied/excluded for TEX11 specifically in this search pass.
- **Third-party reproduction:** **Donor sperm** insemination/IVF, or adoption, are standard alternative family-building options when sperm retrieval fails (a substantial proportion of TEX11/meiotic-arrest cases, given the ~8–9% retrieval rate cited above).
- **Genetic counseling:** **NCIT:C15240** (Genetic Counseling) is directly applicable and clinically essential — particularly because ICSI with retrieved sperm can, for the first time in an affected man's lineage, transmit the pathogenic X-linked allele to **all daughters (obligate carriers)**, while sons (who receive the father's Y chromosome, not his X) are not at risk of inheriting the paternal X-linked variant. This transmission-risk counseling point is a standard consideration in ART for men with identified monogenic infertility causes, though a TEX11-specific formal counseling guideline was not directly retrieved in this search pass and should be verified against current ASRM/ESHRE guidance at curation time.
- **Experimental/investigational:** No gene-therapy, gene-editing, or in-vitro gametogenesis approach has reached clinical application for this disorder; **in vitro spermatogenesis / testicular organoid research** is an active general research area relevant to future management of meiotic-arrest infertility but was not identified as TEX11-disease-specific in this search pass.
- **Treatment outcomes/prognosis by genotype:** As above (Section 11) — retrieval success is histology/genotype-dependent, and the ZZS-vs-M1AP genotype distinction (2025 EMBO Mol Med study) is now proposed as a basis for differentiated pre-TESE counseling, since M1AP-deficient men may retain a slightly higher chance of haploid spermatid recovery than early-arrest ZZS-gene-deficient men.

---

## 13. Prevention

- **Primary prevention:** Not applicable — this is a germline genetic condition with no modifiable environmental trigger to prevent onset.
- **Secondary prevention (early detection):** Early referral of men presenting with infertility/azoospermia for karyotype, Y-microdeletion, and (where indicated) expanded gene-panel/exome testing enables earlier, more accurate counseling and avoids unnecessary or lower-yield interventions.
- **Tertiary prevention:** Timely semen cryopreservation is not applicable (azoospermic), but **cryopreservation of any sperm successfully retrieved via micro-TESE** is standard practice to preserve reproductive options and avoid repeat surgical procedures.
- **Genetic/reproductive counseling and screening:** **Preimplantation genetic testing (PGT)** could theoretically be used to select female (carrier or non-carrier) versus male embryos, or specifically to test for the TEX11 variant in female embryos, when ICSI is used with retrieved paternal sperm — a decision to be made through formal genetic counseling given that carrier daughters themselves would not be expected to have a fertility phenotype (X-linked recessive, male-restricted expression) but could transmit the allele in the next generation.
- **Public health/behavioral/immunization:** Not applicable to this monogenic disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Modeled primarily in **Mus musculus** (NCBITaxon:10090); TEX11 orthologs are broadly conserved across vertebrates and even show mechanistic conservation back to budding yeast (*Saccharomyces cerevisiae*, NCBITaxon:4932) via the Zip4 ortholog relationship.
- **Gene orthology:** Mouse *Tex11* (MGI:1933237) is the direct ortholog of human TEX11; yeast **Zip4** is the deep evolutionary ortholog establishing the conserved ZZS-complex mechanism (Zip2/Zip4/Spo16 in yeast ↔ SHOC1/TEX11/SPO16 in mammals).
- **Natural disease in other species:** No naturally occurring TEX11-associated infertility syndrome in companion animals or wildlife was identified in this search — essentially all animal data derive from **engineered (knockout/CRISPR) mouse models** rather than spontaneously occurring veterinary cases; this is not a documented OMIA (Online Mendelian Inheritance in Animals) entry as far as this search could determine.
- **Comparative pathology:** The meiotic-recombination-failure mechanism (impaired crossover formation, asynapsis, pachytene/metaphase-I checkpoint-triggered germ cell loss) is **highly conserved** between mouse and human, which is precisely why mouse Tex11-knockout/knock-in models are considered strong mechanistic proxies for the human disease (see Model Organisms, below) — though translational fidelity for milder/missense human alleles is less well validated (see model limitations below).
- **Zoonotic potential/transmission:** Not applicable — this is a non-communicable, germline-genetic reproductive disorder.

---

## 15. Model Organisms

- **Primary model:** **Mouse (*Mus musculus*)**, via targeted knockout and, more recently, **CRISPR/Cas9-engineered patient-variant-mimicking alleles**.
- **Foundational knockout model:** *Tex11*-null mice show **abnormal male meiosis, delayed DSB repair, decreased crossover formation, and non-obstructive azoospermia**, closely paralleling the human phenotype and establishing the core causal mechanism (Yatsenko/EMBO Mol Med 2015 mouse data, PMID:26136358).
- **Recent variant-specific CRISPR mouse models (2026 preprint, bioRxiv, "Tex11 Mutant Mouse Models of Human Azoospermia"):**
  - **Tex11D** (frameshift, modeling a human truncating allele): severely reduced testis weight (28.3 mg vs. 144.2 mg wild-type), **no epididymal sperm**, infertile, **maturation-arrest** histology — closely recapitulating severe human truncating-variant disease.
  - **Tex11A** (missense): **no spermatogenesis or fertility defect observed** — demonstrating that not all TEX11 missense changes are functionally deleterious, directly relevant to human variant-classification caution noted in Section 4.
  - **Tex11L**: reduced testis weight (87.5 mg) and reduced epididymal sperm counts (0.33 million/cauda epididymis), but only **incompletely penetrant infertility** (~1/3 of mice infertile) — modeling the "leaky"/partial phenotype seen with some human hypomorphic alleles.
  - A separate PLOS One study additionally found that "a partial deletion within the meiosis-specific sporulation domain SPO22 of Tex11 is **not** associated with infertility in mice" (PMC11373865) — an important **negative/discordant finding** showing that not every exonic lesion in this domain is sufficient to cause disease, reinforcing the need for functional validation rather than domain-location alone when classifying human variants.
- **Model characteristics/limitations:** Mouse models recapitulate the core cytological mechanism (crossover failure, meiotic arrest, azoospermia) with high fidelity for clearly truncating alleles, but **phenotype severity is allele-specific** — meaning a given human missense or in-frame variant cannot be assumed pathogenic by analogy alone, and each variant class ideally needs its own mouse (or in vitro) functional validation, as the discordant SPO22-deletion and Tex11A missense results directly demonstrate.
- **Applications:** Mouse models are used to (1) establish causality and mechanism for candidate human variants, (2) study the ZZS complex's cell-biological function (chromosome axis localization, crossover formation) in vivo, and (3) potentially inform future variant-classification pipelines (functional stratification of VUS TEX11 alleles found in human NOA cohorts).
- **In vitro/functional models:** The 2025 Genes journal study on the c.652del237bp variant used **in vitro (cell-based) and in silico (computational/structural modeling)** approaches — complementing whole-animal models for variant-level functional characterization, particularly useful for triaging variants before committing to a full mouse-model study.
- **Resources:** Mouse Genome Informatics (**MGI:1933237**, Tex11) is the authoritative model-organism database entry; International Mouse Phenotyping Consortium (IMPC)/KOMP repositories are the standard sources for additional Tex11 allele resources, though specific IMPC phenotyping-center data for Tex11 was not independently retrieved in this search pass.

---

## Summary of Key Gaps and Curation Cautions

1. **Verify which OMIM/MONDO entry is actually intended** — SPGFX1 (305700, no gene) vs. SPGFX2 (309120, TEX11) — before building a pathophysiology-driven KB entry, since SPGFX1 itself has no mechanistic literature to curate against.
2. **TEX11 variant pathogenicity is allele-dependent**, not a simple "any TEX11 hit = disease" rule — population screening finds TEX11 sequence variants (including some missense changes) in fertile controls, and mouse functional data show at least one missense allele (Tex11A) and one exonic in-frame deletion (SPO22-domain partial deletion, PMC11373865) with **no functional consequence** — cite specific variant-level evidence, not gene-level association, for any pathophysiology claim.
3. Distinguish the **ZZS-complex genes (TEX11, SHOC1, SPO16)** from the **interacting autosomal gene M1AP** — related but genotype-distinguishable mechanism and prognosis per the 2025 EMBO Molecular Medicine study.
4. Sperm-retrieval prognosis (micro-TESE success) is **histology-driven** and should be modeled/cited as a distinct claim from the underlying causal mechanism.

## Sources

- [Entry - *300311 - TESTIS-EXPRESSED GENE 11; TEX11 - OMIM](https://omim.org/entry/300311)
- [Entry - #309120 - SPERMATOGENIC FAILURE, X-LINKED, 2; SPGFX2 - OMIM](https://www.omim.org/entry/309120)
- [Entry - 305700 - SPERMATOGENIC FAILURE, X-LINKED, 1; SPGFX1 - OMIM](https://omim.org/entry/305700)
- [Spermatogenic Failure, X-Linked, 1 - MalaCards](https://www.malacards.org/card/spermatogenic_failure_x_linked_1)
- [TEX11 gene Testis Expressed 11 - GeneCards](https://www.genecards.org/card/TEX11)
- [TEX11 - Wikipedia](https://en.wikipedia.org/wiki/TEX11)
- [X-Linked TEX11 Mutations, Meiotic Arrest, and Azoospermia in Infertile Men - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1406192)
- [TEX11 is mutated in infertile men with azoospermia and regulates genome-wide recombination rates in mouse - PubMed (PMID:26136358)](https://pubmed.ncbi.nlm.nih.gov/26136358/)
- [Novel Hemizygous Mutations of TEX11 Cause Meiotic Arrest and Non-obstructive Azoospermia in Chinese Han Population - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8491544/)
- [A new TEX11 mutation causes azoospermia and testicular meiotic arrest - PubMed](https://pubmed.ncbi.nlm.nih.gov/33762476/)
- [Is the TEX11-.652del237bp Exonic In-Frame Deletion Variant Associated with Azoospermia? In Vitro and In Silico Study - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12652577/)
- [Novel mutations of TEX11 are associated with non-obstructive azoospermia - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10140331/)
- [Variants in ZZS Complex-Associated Genes TEX11 and M1AP Are Responsible for Male Infertility and Nonobstructive Azoospermia - Andrology (Wiley)](https://onlinelibrary.wiley.com/doi/10.1111/andr.70291)
- [Genotype-specific differences in infertile men due to loss-of-function variants in M1AP or ZZS genes - EMBO Molecular Medicine](https://www.embopress.org/doi/full/10.1038/s44321-025-00244-0)
- [M1AP interacts with the mammalian ZZS complex and promotes male meiotic recombination - EMBO Reports](https://www.embopress.org/doi/full/10.15252/embr.202255778)
- [Tex11 Mutant Mouse Models of Human Azoospermia - bioRxiv](https://www.biorxiv.org/content/10.64898/2026.02.17.706385v1)
- [A partial deletion within the meiosis-specific sporulation domain SPO22 of Tex11 is not associated with infertility in mice - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11373865/)
- [A novel TEX11 mutation induces azoospermia: a case report of infertile brothers and literature review - BMC Medical Genetics](https://link.springer.com/article/10.1186/s12881-018-0570-4)
- [Association of CATSPER1, SPATA16 and TEX11 genes polymorphism with idiopathic azoospermia and oligospermia risk in Iranian population - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8897944/)
- [Genetic insights into non-obstructive azoospermia: Implications for diagnosis and TESE outcomes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12055743/)
- [Diagnostic yield of exome sequencing in nonobstructive azoospermia (NOA): A systematic review and meta-analysis - PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0338892)
- [Differentiation between nonobstructive azoospermia and obstructive azoospermia: then and now - Asian Journal of Andrology / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12112924/)
- [Emerging trends in the management of non-obstructive azoospermia - UroPrecision (Wiley, 2025)](https://onlinelibrary.wiley.com/doi/10.1002/uro2.70002)
- [Full article: Genetic variants underlying spermatogenic arrests in men with non-obstructive azoospermia](https://www.tandfonline.com/doi/full/10.1080/15384101.2023.2171544)
- [TEX11 gene with submissions organized by classifications - GenCC](https://thegencc.org/genes/HGNC:11733)
- [Spermatogenic failure, X-linked, 2 (TEX11) - Clinical Genetic Test - GTR/NCBI](https://www.ncbi.nlm.nih.gov/gtr/tests/579471/)
- [2026 ICD-10-CM Diagnosis Code N46.0: Azoospermia](https://www.icd10data.com/ICD10CM/Codes/N00-N99/N40-N53/N46-/N46.0)
- [Tex11 MGI Mouse Gene Detail - MGI:1933237](https://www.informatics.jax.org/marker/MGI:1933237)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCBITaxon:10090` (1 mention) - the report calls it "Mus musculus", "Taxonomy:** Modeled primarily in **Mus musculus"; NCBITaxon calls it **Mus musculus**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `MONDO:0010595` (obsolete Sertoli cell-only syndrome) (1 mention) - replaced by `MONDO:0056795`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:11733` - called "Gene: TEX11", "HGNC: TEX11"
- `NCBITaxon:10090` - called "Mus musculus", "Taxonomy:** Modeled primarily in **Mus musculus"
- `MGI:1933237` - called "Tex11", "Gene orthology:** Mouse *Tex11"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.