---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T15:35:09.321322'
end_time: '2026-10-15T15:37:37.914238'
duration_seconds: 148.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SPATA22-related gametogenic failure
  mondo_id: MONDO:0975843
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
  web_search_requests: 5
  num_turns: 13
  total_cost_usd: 1.8430135
  session_id: a4926378-2813-40a6-9ccc-290c3f9bf6e9
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 2
citation_count: 9
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SPATA22-related gametogenic failure
- **MONDO ID:** MONDO:0975843 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SPATA22-related gametogenic failure** covering all of the
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

I'm searching the web for more human SPATA22 case reports, because the PubMed tool wasn't permitted.

# SPATA22-related gametogenic failure (MONDO:0975843): research report

**Status:** Prepared 2026-10-15 for curating `kb/disorders/SPATA22-related_gametogenic_failure.yaml`.

**Sources:** The primary literature comes from 11 cached `references_cache/PMID_*.md` files in this worktree. All quotes below are copied from those files. Database identifiers (OMIM, LOVD, PanelApp) come from web searches. The PubMed search tool was not permitted in this session, so the literature sweep is not exhaustive.

**Ontology CURIEs:** Every HPO/GO/CL/UBERON/HGNC/NCIT identifier below is a lead only. They were written from general knowledge and not looked up. Each must be checked with `runoak`, the term cache or `just validate-terms` before it is bound.

---

## 0. Curation flags (read first)

1. **The MONDO label does not match the entry's scope.** The draft YAML binds `MONDO:0975843` with the label "premature ovarian failure 25", which is the female phenotype only. OMIM splits the condition in two:
   - **POF25 (OMIM 621002)** for the female phenotype.
   - **Spermatogenic failure 96 (SPGF96, OMIM 621001)** for the male phenotype.

   Both are autosomal recessive and both map to SPATA22 (OMIM gene 617673) ([LOVD disease #07135](https://databases.lovd.nl/shared/diseases/07135); [Radboudumc panel](https://order.radboudumc.nl/labproduct/pdf/6393284)). The entry's name and description cover both sexes. Decide one of two options:
   - Keep `MONDO:0975843` as the primary term and add the SPGF96 MONDO term (if one exists) as a `has_subtypes` entry or a mapping.
   - Treat the male form as a subtype.

   Either way, do not leave a two-sex description on a female-only term without noting it.

2. **The inheritance evidence conflicts.** All the biallelic evidence (human and mouse) supports autosomal recessive inheritance, with heterozygous carriers fertile (mouse *repro42*, rat *tm*). A 2026 paper (PMID:42098781) reports heterozygous SPATA22 variants in a pedigree with premature ovarian insufficiency (POI) and reduced fertility in *Spata22+/−* mice. Record this as a separate, lower-confidence claim (a `RISK_FACTOR`/susceptibility row or a `KNOWLEDGE_GAP`), not as proof of dominant inheritance.

3. **The human case count is very small.** I found about three to four published families/probands:

   | Report | Variant(s) | Affected individuals |
   |---|---|---|
   | Yao 2022, PMID:35285020 | Homozygous p.R134X | 2 POI and 2 NOA in one consanguineous family |
   | Yao 2022, PMID:35285020 | Compound heterozygous c.900+1G>A / p.R11X | 1 sporadic POI |
   | PMID:34392356 (attributed via LOVD/PanelApp; citation not verified) | Homozygous c.203del, p.Leu68TrpfsTer4 | 1 NOA man |

   The details of PMID:34392356 must be fetched and checked before it is used.

---

## 1. Disease information

**Overview.** This is an autosomal recessive disorder of meiotic homologous recombination. Biallelic loss-of-function variants in *SPATA22* stop germ cells in early meiotic prophase I. The result is premature ovarian insufficiency in 46,XX individuals and non-obstructive azoospermia (NOA) from meiotic arrest in 46,XY individuals. No phenotype outside the gonads has been reported in humans or animal models.

- **PMID:35285020 (human, primary result):** "Bi-allelic SPATA22 variants cause premature ovarian insufficiency and nonobstructive azoospermia due to meiotic arrest." (title)
- **PMID:35285020:** "Thus, this is the first report identifying SPATA22 as the causative gene for human POI."

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0975843 ("premature ovarian failure 25") |
| OMIM (female phenotype) | 621002, POF25 |
| OMIM (male phenotype) | 621001, SPGF96 |
| OMIM (gene) | 617673, SPATA22 |
| LOVD disease | #07135 |
| Gene location | 17p13.3 (LOVD lists the c.203del variant at NC_000017.10:g.3366032del) |
| HGNC | to verify (candidate hgnc:30705; must be checked) |
| Orphanet, ICD-10/11, MeSH | No gene-specific code. Umbrella codes: ICD-10 E28.3 (primary ovarian failure), N46.0 (azoospermia); MeSH "Primary Ovarian Insufficiency", "Azoospermia" |

**Synonyms:** POF25; premature ovarian failure 25; spermatogenic failure 96; SPATA22-related POI/NOA; SPATA22-related meiotic arrest.

**Data provenance:** Individual-patient case reports from whole-exome sequencing (WES) of families, plus aggregated gene-curation resources (OMIM, LOVD, PanelApp Australia).

## 2. Etiology

**Cause:** Germline biallelic loss-of-function variants in *SPATA22* (nonsense, canonical splice, frameshift).

**Risk factors:**
- **Consanguinity.** The index family was consanguineous (PMID:35285020: "members of a consanguineous family with two POI and two NOA patients"), as was the c.203del proband.
- **Heterozygous variants (contested).** Possible heterozygous susceptibility to POI (PMID:42098781: "Two heterozygous pathogenic SPATA22 variants were identified in a POI pedigree with four affected infertile individuals"). This is a single report and conflicts with recessive transmission in other families.

**Environmental, protective and gene–environment factors:** None known. Oxidative stress has been proposed as a downstream mediator in granulosa cells (PMID:42098781, mouse/in vitro).

## 3. Phenotypes

| Phenotype | Candidate HPO term (verify) | Sex | Onset | Evidence |
|---|---|---|---|---|
| Premature ovarian insufficiency | HP:0008209 Premature ovarian insufficiency | F | Adolescence to young adulthood | PMID:35285020 |
| Primary or secondary amenorrhea | HP:0000786 / HP:0000869 | F | Puberty / adult | Expected with POI. Individual-level detail is in the full text, not the abstract |
| Hypergonadotropic hypogonadism (raised FSH) | HP:0000815 | Both | — | Expected from POI/NOA biochemistry. Confirm from the full text |
| Non-obstructive azoospermia | HP:0011961 Non-obstructive azoospermia (or HP:0000027 Azoospermia) | M | Adult (presents with infertility) | PMID:35285020 |
| Spermatocyte meiotic arrest (zygotene-like) on testis histology | Cellular phenotype; no exact HPO term (consider HP:0012205 globozoospermia? **No, wrong concept.** Use a free-text cellular phenotype) | M | — | PMID:35285020: "spermatogenesis was arrested at a zygotene-like stage in the proband with NOA" |
| Infertility | HP:0000789 Infertility | Both | — | PMID:35285020, PMID:42098781 |

- **Severity and course:** Complete gametogenic failure in males. In females, POI that presumably progresses to complete ovarian failure (the mouse shows oocyte loss).
- **Frequency:** No frequencies are available. With fewer than 10 patients, every listed feature is present in all reported cases of the matching sex.
- **Quality of life:** No disease-specific data. The burden is infertility, plus the consequences of estrogen deficiency in women (bone, cardiovascular, menopausal symptoms).

## 4. Genetic and molecular information

**Gene.** *SPATA22* (spermatogenesis associated 22) is vertebrate-specific and expressed mainly in germ cells.
- **PMID:22011390:** "a nonsense mutation in Spata22, a hitherto uncharacterized gene conserved among bony vertebrates. Expression of both transcript and protein is restricted predominantly to germ cells of both sexes."

**Reported variants (NM_001170698.2 per LOVD; check the transcript)**

| Variant | Type | Zygosity | Phenotype | Source |
|---|---|---|---|---|
| c.400C>T, p.(Arg134*) | Nonsense | Homozygous | 2 POI and 2 NOA, consanguineous Chinese family | PMID:35285020 |
| c.900+1G>A | Canonical splice donor (minigene-validated) | Compound heterozygous with the variant below | Sporadic POI | PMID:35285020 |
| c.31C>T, p.(Arg11*) | Nonsense | Compound heterozygous with the variant above | Sporadic POI | PMID:35285020 |
| c.203del, p.(Leu68Trpfs*4) | Frameshift | Homozygous | NOA (affected status of a homozygous brother unknown) | LOVD (pathogenic, recessive); attributed to PMID:34392356 / "Wu 2022". **Verify** |
| Two heterozygous variants (identities in the full text) | — | Heterozygous | POI pedigree | PMID:42098781 |

- **Mechanism class:** Loss of function. In mice, nonsense and splice alleles abolish the protein.
  - **PMID:22011390:** "Germ cells of repro42 mutant mice express Spata22 transcript, but not SPATA22 protein."
  - **PMID:32388826:** "leads to incorrect splicing of the Spata22 mRNA, ultimately resulting in no detectable SPATA22 protein."
- **Variant origin:** Germline. No somatic involvement.
- **Population frequency:** Not established here. Check gnomAD for loss-of-function carrier frequency.
- **ClinGen gene–disease validity:** No assertion found. PanelApp Australia rates SPATA22 high-evidence (green) on its POI and spermatogenic-failure panels ([PanelApp POI](https://panelapp-aus.org/panels/3166/gene/SPATA22/)).
- **Modifier genes, epigenetics, chromosomal abnormalities:** None reported.
- **Gene family relation:** *MEIOB* is the obligate partner. Biallelic *MEIOB* variants cause the same phenotype in both sexes (PMID:31000419), which strengthens the case for pathogenicity through the shared complex.

## 5. Environmental information

Not applicable. There are no environmental, lifestyle or infectious causes.

## 6. Mechanism and pathophysiology

**Ordered causal chain**

1. **Biallelic SPATA22 truncating or splice variants lead to absent SPATA22 protein** (nonsense-mediated decay or aberrant splicing).
   - Shown in mice (PMID:22011390, PMID:32388826). Inferred in humans from variant class and a minigene assay (PMID:35285020).
2. **Loss of SPATA22 destabilizes its obligate partner MEIOB and abolishes the MEIOB–SPATA22 heterodimer.**
   - PMID:24240703: "chromatin localization and stability of MEIOB depends on SPATA22 and vice versa."
   - PMID:28453612: "MEIOB and SPATA22 form an obligate complex."
   - In human cells, SPATA22 is also needed to bring MEIOB into the nucleus (PMID:36331299: "the NLS in the OB domain of hMEIOB and interaction with hSPATA22 are required for hMEIOB nuclear localization"). This step is in vitro.
3. **Without the complex, RPA-coated single-stranded DNA (ssDNA) at meiotic double-strand break (DSB) resection intermediates is not properly bound, compacted or processed.**
   - PMID:33812231: "MEIOB and SPATA22 interact with the preformed RPA complex... and condense RPA-coated ssDNA in vitro."
   - PMID:28453612: "MEIOB and SPATA22 are recruited to induced DNA double-strand breaks (DSBs) together but not alone."
   - PMID:40296718 (human proteins): "hSPATA22 binds to ssDNA faster and more stably and promotes ssDNA condensation."
4. **This leads to failed DSB repair and disordered recombination.** DSBs form, but DMC1 strand-exchange foci are lost early and BLM-positive foci build up abnormally.
   - PMID:32388826: "mutant cells appear to form DSBs and initiate meiotic recombination, but are unable to complete DSB repair... shani mutants show precocious loss of DMC1 foci and improper accumulation of BLM-positive recombination foci."
5. **This in turn causes failed homologous synapsis.**
   - PMID:22011390: "homologous chromosomes of mutant germ cells do not achieve normal synapsis or repair meiotic DNA double-strand breaks."
6. **This triggers prophase I arrest (zygotene-like) and apoptotic germ cell elimination** (presumed meiotic checkpoint; the checkpoint pathway was not dissected for SPATA22).
   - PMID:32388826: "leading to meiotic prophase arrest, apoptosis and sterility."
   - Human testis: arrest at a zygotene-like stage (PMID:35285020).
7. **The outcome then branches by sex:**
   - **7a (male):** No post-meiotic spermatids, leading to non-obstructive azoospermia.
   - **7b (female):** Fetal oocytes are lost in prophase I, giving a depleted primordial follicle pool and then POI with hypergonadotropic hypogonadism.
     - Oocyte loss is shown in mice (PMID:22011390: "subsequent germ cell loss in both males and females"). The human ovarian histology is inferred.
   - **7c (possible somatic branch; contested, mouse/in vitro):** SPATA22 deficiency in granulosa cells leads to DNA damage and oxidative stress, then granulosa-cell dysfunction and ovarian insufficiency (PMID:42098781). This is proposed for heterozygotes. Model it under a separate `mechanistic_hypotheses` group (status EMERGING).

**Candidate GO terms (verify)**

| Term | Use |
|---|---|
| GO:0007131 reciprocal meiotic recombination | — |
| GO:0000724 double-strand break repair via homologous recombination | — |
| GO:0007130 synaptonemal complex assembly | — |
| GO:0007129 homologous chromosome pairing at meiosis | — |
| GO:0003697 single-stranded DNA binding | Molecular function |
| GO:0051321 meiotic cell cycle | — |
| GO:0007283 spermatogenesis | — |
| GO:0048477 oogenesis | — |
| GO:0006915 apoptotic process | Downstream germ cell loss |

**Candidate CL terms (verify):**
- CL:0000017 spermatocyte (primary spermatocyte CL:0000656)
- CL:0000023 oocyte (primary oocyte CL:0000654)
- CL:0000501 granulosa cell (branch 7c)

**Pathways and other layers:**
- **Pathways:** Reactome "Meiotic recombination" (R-HSA-912446).
- **Metabolic and immune:** None.
- **Omics:** No disease-specific transcriptomic, proteomic or single-cell data found.

## 7. Anatomical structures

- **Organs (verify UBERON IDs):** Testis (UBERON:0000473), seminiferous tubule (UBERON:0001343), ovary (UBERON:0000992). Both sides are affected. No other organs are involved.
- **Subcellular compartments:**
  - Nucleus and meiotic chromosomes/chromatin: recombination foci associated with chromosome axes (PMID:24240703: "co-localize in foci that are associated with meiotic chromosomes").
  - Candidate GO cellular-component terms: GO:0005634 nucleus; GO:0000794 condensed nuclear chromosome.

## 8. Temporal development

- **Onset:** Congenital/developmental. Meiotic failure happens in the fetus (oocytes) or at puberty (spermatocytes). It shows clinically at puberty or adulthood as amenorrhea/POI or infertility.
- **Course:** Lifelong, not reversible. Natural history data are lacking.
- **Critical window:** Female fertility preservation (oocyte or ovarian-tissue cryopreservation) is possible only while follicles remain. It is not clear whether any follicles survive in null females (null mice lose oocytes early).

## 9. Inheritance and population

| Item | Finding |
|---|---|
| Inheritance | Autosomal recessive (HP:0000007; verify). OMIM, LOVD and all families with biallelic variants agree. A single report suggests heterozygous susceptibility (see flag 2) |
| Penetrance | Complete for gonadal failure in reported biallelic cases. The affected status of one homozygous brother of the c.203del proband is unknown |
| Consanguinity | Prominent |
| Founder effects | None known |
| Populations | Chinese (PMID:35285020, PMID:42098781) and one other consanguineous family (population not confirmed) |
| Prevalence | Unknown, ultra-rare. Fewer than 10 published patients |
| Prevalence class | `CASES_IN_LITERATURE` / `ULTRA_RARE` |
| Background | POI affects about 1–3% of women under 40 (quoted in PMID:31000419). SPATA22 explains only a tiny fraction: Yao et al. screened an in-house idiopathic POI WES database and found one further case. Xia et al. screened 608 POI patients and found one pedigree |
| Sex ratio | Both sexes affected equally |

## 10. Diagnostics

- **Laboratory:**
  - FSH/LH (raised), estradiol (low) and AMH (low or undetectable) in women.
  - Semen analysis (azoospermia, normal volume), raised FSH and normal karyotype in men.
- **Histology:** Testicular biopsy shows meiotic arrest at the spermatocyte (zygotene-like) stage. Spermatocyte spreads with SYCP3/γH2AX immunostaining show asynapsis (PMID:35285020).
- **Genetic testing:**
  - Rule out first: karyotype (Turner syndrome, 47,XXY), Y-chromosome AZF microdeletions, and *FMR1* premutation in women.
  - Then: WES or a POI/NOA gene panel. SPATA22 is on PanelApp Australia and Radboudumc panels.
  - Splice variants need RNA studies or a minigene assay (as for c.900+1G>A).
- **Differential diagnosis:** Other meiotic-recombination POI/NOA genes, including *MEIOB* (phenocopy, PMID:31000419), *STAG3*, *SYCE1*, *MSH4*, *MSH5*, *HFM1*, *ZSWIM7*, *SPIDR*, *DMC1*, *MCM8/9*, *TEX11* (X-linked), *MEI1* and *REC114*. Also non-genetic POI (autoimmune, iatrogenic).
- **Screening:** Cascade carrier testing and testing of siblings in consanguineous families. No newborn screening.

## 11. Outcome and prognosis

- **Survival:** Normal life expectancy is expected; no mortality is attributable to the disease.
- **Morbidity, males:** Permanent sterility. Microdissection TESE is expected to fail with complete meiotic arrest, but no SPATA22-specific sperm-retrieval data were found.
- **Morbidity, females:** Infertility, plus long-term consequences of estrogen deficiency (osteoporosis, cardiovascular risk, menopausal symptoms) without hormone replacement therapy (HRT).

## 12. Treatment

There is no disease-modifying therapy.

| Treatment | Candidate NCIT term (verify) | Notes |
|---|---|---|
| Hormone replacement therapy (estrogen/progestin) for POI | NCIT:C15986 Pharmacotherapy (+ `therapeutic_agent` estradiol, from CHEBI) | Standard POI care for bone and cardiovascular protection |
| Oocyte donation / IVF | Assisted reproductive procedure term (look up) | Only route to pregnancy for affected women |
| Donor sperm / adoption | — | Males |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — |
| N-acetylcysteine | Experimental only | Partially rescued *Spata22+/−* mouse fertility and granulosa-cell defects (PMID:42098781: "The antioxidant NAC effectively rescued GCs defects, and partially restored Spata22+/- mice fertility"). No human data. Record as preclinical evidence (`MODEL_ORGANISM`/`IN_VITRO`) |

No clinical trials were found.

## 13. Prevention

- Primary prevention is not applicable.
- Options are genetic counseling, carrier testing of relatives, and preimplantation or prenatal testing for at-risk couples (25% recurrence for carrier × carrier).
- Consider fertility preservation counseling for asymptomatic homozygous sisters identified early, though its effectiveness is unproven.

## 14. Other species and natural disease

- **Conservation:** The gene is conserved across bony vertebrates (PMID:22011390). A zebrafish ortholog is annotated in ZFIN ([ZFIN](https://www.zfin.org/ZDB-GENE-170421-1)).
- **Rodents:** The tremor rat (*tm/tm*) is a spontaneous rat mutant with sterility from a deletion that includes *Spata22*.
  - PMID:23903057: "Spata22 was identified as the gene responsible for the failure of gametogenesis to progress beyond meiosis I in tm homozygous rats by a transgenic rescue experiment."
  - Its tremor/epilepsy phenotype comes from other deleted genes.
- **Veterinary:** No naturally occurring disease known in companion animals or livestock (OMIA not checked).

## 15. Model organisms

| Model | Allele | Phenotype | Fidelity / limitations | PMID |
|---|---|---|---|---|
| Mouse *repro42* (ENU) | Nonsense; no protein | Infertility in both sexes, no other phenotype; prophase I arrest, asynapsis, unrepaired DSBs, germ cell loss | High for the gonadal phenotype | 22011390 |
| Mouse *shani* (ENU) | Exonic splicing-enhancer point mutation, mis-splicing, no protein | Phenocopies null: DSBs form but are not repaired, early DMC1 loss, BLM foci, apoptosis, sterility | High; a model for splice-class human variants | 32388826 |
| Mouse *Meiob*−/− | Partner knockout | Same sterility in both sexes; MEIOB/SPATA22 mutually dependent | Pathway phenocopy | 24240703 |
| Rat *tm/tm* | ~240 kb deletion including *Spata22* + ≥12 genes | Gonadal hypoplasia, meiosis I arrest; rescued by *Spata22* transgene | Contiguous-gene confound (tremor) | 23903057 |
| Mouse *Spata22+/−* | Heterozygous | Reported reduced ovarian function and fertility, granulosa-cell DNA damage/oxidative stress, partial NAC rescue | Single report; conflicts with fertile heterozygotes in earlier models | 42098781 |
| Cell-free / HEK293 systems | Human and mouse proteins | ssDNA binding, RPA interaction, nuclear import | `IN_VITRO`; no meiotic context | 28453612, 33812231, 36331299, 40296718 |

**Model limitations.**
- The human and rodent proteins differ in sequence. PMID:40296718: "the amino acid sequences of the two proteins are inconsistent in humans and rodents, which leads to functional differences in meiosis."
- Mouse oocyte loss is a reasonable stand-in for human POI, but human ovarian histology is not available. This is a candidate `HUMAN_MODEL_MISMATCH` discussion.

---

## Evidence summary by source type

| Source type | PMIDs |
|---|---|
| Human clinical | 35285020 (primary), 42098781 (heterozygous; contested), 34392356 (needs verifying), 31000419 (*MEIOB* phenocopy, supporting) |
| Model organism | 22011390, 32388826, 23903057, 24240703, 42098781 (mouse arm) |
| In vitro | 28453612, 33812231, 36331299, 40296718 |

## Sources (web)
- [LOVD disease #07135 – POF25, OMIM:621002](https://databases.lovd.nl/shared/diseases/07135)
- [LOVD SPATA22 c.203del variant record](https://databases.lovd.nl/shared/variants/0001017675)
- [Radboudumc ovarian insufficiency panel (POF25 621002; SPGF96 621001)](https://order.radboudumc.nl/labproduct/pdf/6393284)
- [PanelApp Australia – SPATA22 (POI panel)](https://panelapp-aus.org/panels/3166/gene/SPATA22/)
- [PanelApp Australia – SPATA22 (panel 137)](https://panelapp-aus.org/panels/137/gene/SPATA22/)
- [GeneCards – SPATA22](https://www.genecards.org/card/SPATA22)
- [ZFIN – zebrafish spata22](https://www.zfin.org/ZDB-GENE-170421-1)
- [Xia et al. 2026, Reprod Biol Endocrinol (SPATA22 heterozygous POI)](https://link.springer.com/article/10.1186/s12958-026-01547-8)
- [Frontiers in Genetics 2022 article cited in search (contents not confirmed)](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.936264/full)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000815` (1 mention) - the report calls it "Hypergonadotropic hypogonadism (raised FSH)"; HP calls it **Hypergonadotropic hypogonadism**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

31 of 32 terms resolved to a current term; the rest could not be looked up either way.