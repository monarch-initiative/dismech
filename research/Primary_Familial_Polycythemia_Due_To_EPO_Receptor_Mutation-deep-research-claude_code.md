---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T03:58:15.617475'
end_time: '2026-10-15T03:59:13.236455'
duration_seconds: 57.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Primary Familial Polycythemia Due to EPO Receptor Mutation
  mondo_id: MONDO:0007572
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
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.7919443
  session_id: 6f407ab6-10d8-510b-8a76-b165dbc02479
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 4
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Familial Polycythemia Due to EPO Receptor Mutation
- **MONDO ID:** MONDO:0007572 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primary Familial Polycythemia Due to EPO Receptor Mutation** covering all of the
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

# Primary Familial Polycythemia Due to EPO Receptor Mutation (EPOR-related ECYT1/PFCP): Research Report

**Verification status.** I ran three web searches. Only three PMIDs came back with a source I could read, and I marked those **[verified]**. Everything else is from my background knowledge and is marked **[unverified]**. Under this repository's rules, an unverified item is a lead only. Run `just fetch-reference PMID:<id>` and check the snippet before it becomes evidence. I did not read any abstract in full, so I give no direct quotes except short fragments from the search results. The MONDO ID given in the template (MONDO:0007572) and every HPO, GO, CL, UBERON and NCIT ID below also need an OAK lookup before binding. I wrote none of them from a lookup.

## 1. Disease information

- **What it is.** An autosomal dominant erythrocytosis. The red cell mass is raised because of a germline EPOR mutation, and serum erythropoietin (EPO) is low or low-normal. It is called "primary" because the defect is intrinsic to erythroid progenitors, not to oxygen sensing or EPO production.
- **Identifiers.**
  - OMIM #133100, "Erythrocytosis, familial, 1 (ECYT1)", with primary familial and congenital polycythemia (PFCP) as an alternative title ([OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/133100)).
  - Orphanet ORPHA:90042 (reached through the [PhenoDis mirror](https://iegext02.helmholtz-munich.de/phenodis/disease/show/7045)).
  - MedGen C4551637 ([MedGen](https://ncbi.nlm.nih.gov/medgen/C4551637)).
  - GARD and NORD pages exist ([GARD](https://rarediseases.org/gard-rare-disease/primary-familial-and-congenital-polycythemia/), [NORD MONDO page](https://rarediseases.org/mondo-disease/primary-familial-polycythemia-due-to-epo-receptor-mutation/)).
  - I have not checked MONDO, ICD-10/11 or MeSH.
- **Synonyms.** Primary familial and congenital polycythemia (PFCP); familial erythrocytosis type 1; familial benign erythrocytosis; EPOR-related erythrocytosis.
- **Source level.** The resources above are aggregated disease-level records. The primary papers are family and cohort reports.

## 2. Etiology

- **Cause.** Heterozygous germline EPOR mutations. "All mutations so far described lead to the truncation of the C-terminal receptor sequence that contains negative regulatory domains" (Pasquier et al. 2017, [PMID:29269524] **[verified]**). The mutations are nonsense or frameshift variants, mostly in the last exon, exon 8.
- **Example.** An EPOR G1251T change (a premature stop codon at residue 393) in one family, with a 20-fold rise in circulating endothelial precursors (PLoS ONE 2010; PMID not retrieved) **[unverified]**.
- **Frequency among cases.** One source says EPOR mutations explain roughly 12–15% of PFCP. A screen of 270 cases found EPOR mutations in only 1.1% of them. These figures conflict, probably because the cohorts were selected differently. Most erythrocytosis cases have no identified cause. Both figures are unverified.
- **Modifiers.** Kralovics et al. (J Clin Invest 1998) described an affected child with a unique EPOR mutation who did not develop polycythemia even though their erythroid progenitors were hypersensitive to EPO. The authors suggested unidentified environmental or genetic modifiers may suppress disease. The abstract was not fetched, so I did not use its wording. Penetrance of the biochemical defect is therefore not equal to penetrance of the clinical phenotype.
- **Environmental and protective factors.** None established. Carriers of a gain-of-function EPOR variant may be more sensitive to hypoxia (altitude, smoking, sleep apnea) **[unverified, inferred]**.

## 3. Phenotypes

Suggested HPO terms need lookup before binding.

| Phenotype | Notes | HPO (to verify) |
|---|---|---|
| Erythrocytosis (raised hemoglobin and hematocrit) | Core feature | HP:0001899 |
| Low or low-normal serum EPO | Key laboratory finding | not looked up |
| Normal white cell and platelet counts | Distinguishes it from polycythemia vera | not looked up |
| Hyperviscosity symptoms: headache, dizziness, plethora | Variable | not looked up |
| Thrombosis, myocardial infarction, stroke | Complication; frequency uncertain | not looked up |
| Hypertension and coronary disease | OMIM lists cardiovascular features, including myocardial infarction, coronary artery disease, hypertension and peripheral thrombosis | not looked up |

- **Onset.** Congenital or childhood, with variable penetrance. Many carriers are found by family screening.
- **Quality of life.** I found no quantitative data.
- **Frequencies.** I did not retrieve per-feature frequencies.

## 4. Genetic and molecular information

- **Gene.** EPOR, 19p13.2. The HGNC ID is not looked up; this repository writes it as lowercase `hgnc:<n>`.
- **Variant class.** Nonsense or frameshift variants that truncate the cytoplasmic C-terminus. This removes negative regulatory domains, including the binding site for SHP-1 (a phosphatase) and the residues needed for receptor internalization and degradation **[unverified, standard mechanism]**.
- **Functional consequence.** Gain of function through loss of negative regulation. Huang et al. 2010 ([PMID:20096014] **[verified]**) reviewed several lines of evidence for a causal role of the truncated receptor. They note that truncated PFCP EpoRs are not properly down-regulated upon stimulation.
- **Different variants act by different mechanisms.** Pasquier 2017 concludes that mutation types act through distinct mechanisms. A frameshift variant reported in Haematologica (PMID not retrieved) showed "a strong gain-of-function mutation, which induces major erythropoietin hypersensitivity in primary erythroid progenitors", with persistent JAK2 and STAT5 activation **[unverified]**.
- **Origin.** Germline. Population frequency, ClinVar classification and modifier genes were not checked.
- **Epigenetics and chromosomal abnormalities.** Not applicable and not researched.

## 5. Environmental information

None established. Cardiovascular risk factors such as smoking probably add to thrombotic risk **[inferred]**. No infectious agents are involved.

## 6. Mechanism and pathophysiology

**Causal chain**

1. A germline nonsense or frameshift variant in the last EPOR exon causes truncation of the cytoplasmic C-terminus. (Demonstrated.)
2. The truncated receptor lacks negative regulatory domains. These include the docking site for negative regulators (SHP-1) and the signals for internalization and degradation. (Demonstrated for some variants; the exact domain varies.)
3. The receptor is not properly down-regulated after ligand binding, so it persists on the cell surface. (Demonstrated for the G1251T variant in the PLoS ONE report.)
4. JAK2 and STAT5 activation is prolonged after EPO binding. (Demonstrated for at least one frameshift variant.)
5. Erythroid progenitors (BFU-E and CFU-E) become hypersensitive to EPO and grow with very little or no added EPO. (Demonstrated.)
6. Red cell production rises despite low EPO, and erythrocytosis results. Low EPO is the expected feedback response to the raised red cell mass. (Demonstrated.)
7. Raised hematocrit increases blood viscosity and may lead to thrombotic and cardiovascular events. (Inferred from clinical association; the strength of the effect is uncertain.)

**Branch.** Some variants may not simply be hyperactive. They may act by distinct mechanisms (Pasquier 2017), so the chain above is the common case, not a universal one.

**Candidate GO and CL terms (to verify)**
- Erythrocyte differentiation.
- Erythropoietin-mediated signaling pathway.
- JAK-STAT cascade.
- Negative regulation of receptor signaling.
- Erythroid progenitor cell (CL), erythrocyte (CL).

**Not researched.** Omics, single-cell and CRISPR screens.

## 7. Anatomical structures affected

- Bone marrow is the primary site. Blood is where the erythrocytosis shows. The vasculature is affected secondarily through hyperviscosity.
- Cell types are the erythroid progenitor and the erythrocyte. The PLoS ONE report also found raised circulating endothelial precursors **[unverified]**.
- Subcellular site: the plasma membrane receptor and its cytoplasmic domain, with downstream JAK2/STAT5 signaling in the cytoplasm and nucleus.
- No lateralization.

## 8. Temporal development

- Congenital or early onset, chronic and lifelong. Whether it progresses was not established. Complications probably accumulate with age.
- No spontaneous remission is known. I found no data on critical periods.

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant. Penetrance of the clinical phenotype is incomplete (Kralovics 1998 report of a non-polycythemic carrier child).
- **Prevalence.** Very rare. No reliable prevalence figure retrieved.
- **Founder effect.** A study titled "Benefit of phlebotomy and low-dose aspirin in the prevention of vascular events in patients with EPOR primary familial polycythemia on the island of New Caledonia" (PMID not retrieved) suggests a large regional cluster **[unverified]**. I did not read it.
- **Sex ratio, ancestry and consanguinity.** Not researched.

## 10. Diagnostics

- **Laboratory findings.** Raised hemoglobin and hematocrit, low or low-normal EPO, normal white cell and platelet counts.
- **Exclusion of other causes.** Rule out JAK2 V617F and exon 12 variants (polycythemia vera). Also rule out secondary causes: hypoxia, renal disease and EPO-secreting tumors. Check other familial erythrocytosis genes (VHL, EGLN1, EPAS1, HBB and others) **[standard practice, unverified here]**.
- **Genetic testing.** EPOR sequencing, with exon 8 as the hot spot, or an erythrocytosis gene panel. Family history and a typical pattern of dominant inheritance support the diagnosis.
- **Bone marrow culture.** Endogenous erythroid colonies and EPO hypersensitivity can be shown in vitro, but this is not routine.

## 11. Outcome and prognosis

- Survival and life expectancy data are not retrieved.
- The main risks are thrombosis and cardiovascular events, linked to hematocrit **[inferred]**.
- Cardiovascular outcomes are not uniform. Reports describe both families with early events and families with a benign course **[inferred, unverified]**.

## 12. Treatment

- **Phlebotomy.** Used periodically to relieve symptoms or keep hematocrit near normal. The target hematocrit in this disease is debated. It is not firmly established, and the polycythemia vera targets may not transfer **[unverified]**.
- **Low-dose aspirin.** The New Caledonia study above addresses phlebotomy plus aspirin for preventing vascular events. I did not retrieve its results.
- **Cytoreduction and JAK2 inhibition.** My searches did not find any evidence on ruxolitinib or hydroxyurea in EPOR-related disease. The pathway is JAK2-dependent, so a JAK2 inhibitor is a plausible hypothesis. It is not an established treatment. Do not curate it as one.
- Cardiovascular risk-factor management applies.
- NCIT terms: phlebotomy and Pharmacotherapy (`NCIT:C15986`, taken from the CLAUDE.md list); the phlebotomy ID is not looked up.
- No clinical trials were identified.

## 13. Prevention

- Genetic counseling and cascade testing of relatives.
- Tertiary prevention: control of hematocrit and of cardiovascular risk factors, and avoiding dehydration.
- No primary prevention or vaccination applies.

## 14. Other species and natural disease

No naturally occurring animal disease was identified. OMIA was not searched.

## 15. Model organisms

- **Human truncated EPOR knock-in mouse.** Divoky et al. 2001 ([PMID:11158582] **[verified]**) replaced the murine gene with the mutant human EPOR. The mice became polycythemic. A later report says the phenotype appeared at 3 to 6 weeks of age but not at birth, mirroring the human disease (J Mol Med 2015; PMID not retrieved).
- **Truncated mouse EpoR.** Mice carrying the truncated mouse receptor were not polycythemic, so the phenotype depended on the human receptor. The authors noted that erythropoiesis differs between mice and humans. This is a possible `HUMAN_MODEL_MISMATCH` discussion in the KB. The details need confirmation from the full papers.
- **Limitation.** Consequences in non-erythroid tissues were unknown in the 2001 paper.

## Gaps to close before curation

1. Fetch and verify PMIDs for Kralovics 1998, the PLoS ONE 2010 G1251T paper, the Haematologica frameshift paper, the J Mol Med 2015 mouse paper, and the New Caledonia study.
2. Confirm the GeneReviews and Orphanet content. GeneReviews did not surface in my searches.
3. Look up every MONDO, HP, GO, CL, UBERON and NCIT ID above with OAK. Check that the stub's MONDO ID matches this entity.
4. Find data on prevalence, thrombosis frequency, and treatment outcome, including ruxolitinib, if any exists.

## Sources

- [PMC Pasquier et al. (PMID:29269524), via search results](https://pmc.ncbi.nlm.nih.gov/articles/PMC5865417)
- [Huang et al. review (PMID:20096014), via search results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864346)
- [JCI Kralovics 1998 (full text PDF)](https://www.jci.org/articles/view/2886/files/pdf)
- [PLoS ONE 2010 G1251T report (DOAJ)](https://doaj.org/article/c749460bfd1e4e51998c1c626fd9cba6)
- [Haematologica 2018 (flipbook page)](https://digital.haematologica.org/wp-content/uploads/flipbook/7/files/basic-html/page36.html)
- [OMIM #133100 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/133100)
- [MedGen C4551637](https://ncbi.nlm.nih.gov/medgen/C4551637)
- [PhenoDis (Orphanet mirror)](https://iegext02.helmholtz-munich.de/phenodis/disease/show/7045)
- [GARD](https://rarediseases.org/gard-rare-disease/primary-familial-and-congenital-polycythemia/)
- [NORD MONDO page](https://rarediseases.org/mondo-disease/primary-familial-polycythemia-due-to-epo-receptor-mutation/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001899` (1 mention) - the report calls it "Core feature"; HP calls it **Increased hematocrit**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

3 of 4 terms resolved to a current term; the rest could not be looked up either way.