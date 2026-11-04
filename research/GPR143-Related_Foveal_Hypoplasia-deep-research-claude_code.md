---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-04T19:15:51.030771'
end_time: '2026-11-04T19:21:11.267090'
duration_seconds: 320.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: GPR143-Related Foveal Hypoplasia
  mondo_id: MONDO:0700230
  category: Mendelian
  causal_genes: GPR143
  omim_id: not recorded
  synonyms: GPR143-related foveal hypoplasia with or without albinism
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
  web_search_requests: 11
  num_turns: 21
  total_cost_usd: 2.4171374999999995
  session_id: 246fd892-cdbc-4d18-92cd-914aef904673
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
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
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GPR143-Related Foveal Hypoplasia
- **MONDO ID:** MONDO:0700230 (if available)
- **Causal gene(s):** GPR143
- **OMIM:** not recorded
- **Synonyms:** GPR143-related foveal hypoplasia with or without albinism
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **GPR143-Related Foveal Hypoplasia** covering all of the
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

Searching the literature now. The KB entry for this disease is only a skeleton so far.

# GPR143-Related Foveal Hypoplasia (MONDO:0700230): Research Report

**Prepared:** 2026-11-04 · **Causal gene:** *GPR143* (hgnc:20145; formerly *OA1*), Xp22.2

This report is a lead for curation, not curated content. Each PMID is marked by how it was checked:

- **[V]** The PMID and its finding were confirmed in a search result, the offline Bookshelf index, or `references_cache/`.
- **[V?]** The PMID appeared only in a URL or a secondary listing. Run `just fetch-reference` on it before quoting.
- **[no PMID]** The publication is real, but I found no PMID for it. It is cited by DOI or PMC ID.

No quoted text below has yet been checked against a cached abstract. Every snippet must be re-taken from the `references_cache/` file after fetching.

Every ontology CURIE suggested here was read from the repository's own term caches (`cache/hp`, `cl`, `go`, `uberon`, `chebi`, `ncit`) or from the stub file in this session. The sole exception is `UBERON:0001785`, the optic chiasm alternative mentioned in §7, which I did not look up and which is flagged there. A CURIE marked "not found" means it was not in the cache. It does not mean the ontology lacks a term.

---

## 1. Disease information

**Overview.** GPR143-related foveal hypoplasia is an X-linked recessive disorder of the developing eye caused by hemizygous loss-of-function variants in *GPR143*. *GPR143* encodes an intracellular G-protein-coupled receptor on the membranes of melanosomes and lysosomes in the retinal pigment epithelium (RPE) and melanocytes.

The disease runs along a spectrum:
- **Classic X-linked ocular albinism (OA1, Nettleship–Falls).** Foveal hypoplasia, infantile nystagmus, reduced visual acuity, iris translucency, a hypopigmented fundus, misrouting of optic fibres at the chiasm, and macromelanosomes in skin and RPE. Skin pigmentation is essentially normal.
- **X-linked congenital nystagmus (NYS6).** Nystagmus with foveal hypoplasia and little or no visible albinism.
- **Isolated foveal hypoplasia.** Foveal hypoplasia with neither nystagmus nor iris depigmentation (Mao et al. 2021, PMID:33785018 [V]).

The MONDO term (label "GPR143-related foveal hypoplasia"; synonym "…with or without albinism") was built as the umbrella over this spectrum. Its two MONDO descendants are listed in the dismech stub.

**Identifiers**

| System | ID | Notes |
|---|---|---|
| MONDO | MONDO:0700230 | GPR143-related foveal hypoplasia; parent MONDO:0044203 *foveal hypoplasia* |
| MONDO children | MONDO:0021019 *X-linked recessive ocular albinism*; MONDO:0010435 *nystagmus 6, congenital, X-linked* | From `stubs/GPR143-related_Foveal_Hypoplasia.yaml` |
| OMIM (phenotype) | 300500 (Ocular albinism type I, Nettleship–Falls); 300814 (Nystagmus 6, congenital, X-linked) | Not recorded in the stub. Confirm before adding |
| OMIM (gene) | 300808 (*GPR143*) | Allele 300808.0009 = S89F (Liu 2007, per secondary source) |
| HGNC | hgnc:20145 GPR143 | Lowercase prefix, per repo convention |
| ClinGen | `CGGV:assertion_41096b60-bbfb-469e-9695-8a23986f467c-2022-10-06T160000.000Z`: **Definitive, XL**, Retina GCEP, SOP9, 2022-10-06 | Row in `cache/clingen/gene_validity.csv`. Cite it with `gene_disease_validity`, `classified_by: CLINGEN` |
| GeneReviews | PMID:20301517 (NBK1343) "Ocular Albinism, X-Linked – **RETIRED CHAPTER**" [V]; PMID:37053367 (NBK590568) "Oculocutaneous Albinism and Ocular Albinism Overview" [V] | From `cache/bookshelf/genereviews.csv`. A retired-only tag gives `TAGGED_RETIRED`, so prefer the current Overview chapter as the baseline |
| ICD-10 / Orphanet | E70.31x ocular albinism codes; Orphanet ORPHA:54 (X-linked OA) | Not verified in this session. Confirm with `just fetch-reference ORPHA:54` |

**Data provenance.** Almost all of the evidence is aggregated disease-level material: family case series, mostly from Chinese and European pedigrees, plus reviews and mouse models. No EHR-derived cohorts exist.

## 2. Etiology

- **Cause.** Germline hemizygous *GPR143* variants in males. The disease is purely genetic, with no known environmental cause.
- **Genetic risk.** Pathogenic variants include missense, nonsense, frameshift, splice-site, and intragenic or whole-gene deletions. Large deletions are a recognised share of cases (a 2001 *Hum Genet* deletion study, PMID:11214907 [V?]). An early screen found point mutations in only about one-third of clinically diagnosed XLOA patients ("Analysis of the OA1 gene reveals mutations in only one-third of patients with X-linked ocular albinism", PMID:8634705 [V?]). That figure reflects both deletions missed by the methods of the time and clinical misdiagnosis.
- **Modifiers and digenic effects.** One family carried an *OPN1LW/OPN1MW* blue-cone monochromacy allele together with a *GPR143* variant, giving BCM plus foveal hypoplasia (PMID:34445325 [V], cached). This is co-occurrence of two X-linked disorders, not a modifier effect. No true modifier genes are established.
- **Protective factors and gene–environment interactions.** None known.

## 3. Phenotypes

The HPO terms below are all present in `cache/hp/terms.csv`.

| Phenotype | HPO | Onset / course | Frequency and notes |
|---|---|---|---|
| Foveal hypoplasia | HP:0007750 Hypoplasia of the fovea | Congenital, stationary | Essentially universal. All patients with GPR143 mutations had foveal hypoplasia in the SE-China XL-INS cohort (PMID:38222445 [V?]) and in Han 2015 (Sci Rep, PMC4498220 [no PMID]). Often grade 3–4 on OCT; grade 4 in Mao 2021 |
| Infantile nystagmus | HP:0000639 Nystagmus | Infantile onset (HP:0003593), usually in the first months | Very frequent but absent in the isolated-FH family (PMID:33785018 [V]) |
| Reduced visual acuity | HP:0007663 Reduced visual acuity / HP:0000505 Visual impairment | Congenital, largely stationary | BCVA ranged from light perception to 0.15 in a three-family series (Sci Rep 2017, PMC5314354) and 0.01–0.2 in a five-generation family (PMC3423421). One case reached 20/50–20/60 without nystagmus |
| Iris translucency / hypopigmentation | HP:0012805 Iris transillumination defect; HP:0007730 Iris hypopigmentation | Congenital | Variable. Absent in NYS6 and isolated-FH families |
| Fundus hypopigmentation / ocular albinism | HP:0001107 Ocular albinism | Congenital | Variable. Darker-pigmented individuals and Asian families often show minimal fundus hypopigmentation |
| Optic chiasm misrouting | HP:0025163 Abnormal optic chiasm morphology | Developmental | Shown on asymmetric VEP in humans and in Oa1⁻/⁻ mice (PMID:11092754 [V]) |
| Strabismus | HP:0000486 | Childhood | Common, frequency not well quantified |
| Photophobia | HP:0000613 | Childhood | Common in classic OA1 |
| Refractive error | HP:0000483 Astigmatism; HP:0000545 Myopia; HP:0000540 Hypermetropia | — | Frequent high astigmatism, as in all albinism. Not quantified |
| Cutaneous macromelanosomes | No HP term in cache | — | Histologic sign of classic OA1, seen on skin biopsy. Rarely used now |

**Carrier females.** Heterozygous females are usually asymptomatic. They may show a mosaic fundus with alternating pigmented and hypopigmented streaks, described in PMC5314354 and consistent with Lyonization, and partial iris translucency.

**Quality of life.** There are no OA1-specific QoL instrument data. The burden is lifelong low vision affecting reading, driving eligibility, and education. Albinism-wide QoL studies apply.

## 4. Genetic and molecular information

- **Gene.** *GPR143* (hgnc:20145; OMIM 300808), about 40 kb with 9 exons. It encodes a 404-amino-acid class-A-like GPCR with seven transmembrane domains. The protein localises to the membranes of melanosomes and late endosomes or lysosomes rather than the plasma membrane.
- **Discovery.** Bassi et al. 1995, *Nat Genet* 10:13–19, doi:10.1038/ng0595-13 (PMID possibly 7647783 [V?]). The authors found "five intragenic deletions and a 2 bp insertion resulting in a premature stop codon in OA1 patients". The transcript is highly expressed in retina/RPE and melanoma.
- **Variant classes.** Missense variants cluster in the transmembrane and luminal domains, for example S89F in the large NYS6 family (Liu et al. 2007, *J Hum Genet* 52:565–70 [no PMID]). Truncating variants include W313X (c.939G>A) in isolated FH (PMID:33785018 [V]), the splice variant c.658+1G>T (Hu 2011, PMC3060156), a 37-bp deletion (2008), and a 14-bp duplication (2009, PMC2671585). Exonic and whole-gene deletions also occur, among them a large deletion in a Chinese NYS6 pedigree (PMID:27958203 [V?]). In an X-linked infantile nystagmus cohort from SE China, **11 of 98 families (11.2%)** carried *GPR143* variants (PMID:38222445 [V?]).
- **Mechanism.** Loss of function. Missense alleles commonly cause ER retention or misfolding. No gain-of-function or dominant-negative mechanism is established.
- **Genotype–phenotype.** No firm correlation. Albinism-free presentations (NYS6, isolated FH) occur with truncating as well as missense alleles, which argues against a simple hypomorph model. Pigment background is a plausible contributor but is unproven.
- **Population frequency.** Pathogenic alleles are ultra-rare in gnomAD. Hemizygous LoF is essentially absent in control males (expected for an XL recessive disease; not verified for this report).
- **Origin.** Germline. *De novo* and maternal germline mosaic cases are possible but not well documented.
- **Epigenetics and chromosomal abnormalities.** OA1 can occur within Xp22.3 contiguous-gene deletions, together with ichthyosis (*STS*), Kallmann syndrome (*ANOS1*), and chondrodysplasia punctata (*ARSL*). No disease-specific epigenetic data exist.

## 5. Environmental information

None is relevant. There are no environmental, lifestyle, or infectious factors. UV protection is a supportive measure, not an etiological one.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Hemizygous loss-of-function *GPR143* variant** leads to absent, misfolded, or ER-retained GPR143 protein in RPE and melanocytes. *[Human genetics, demonstrated]*
2. **Loss of GPR143 signalling at the melanosome membrane** results in failure of a receptor-controlled checkpoint on melanosome maturation. The proposed endogenous ligand is **L-DOPA**, the first tyrosinase product (Lopez et al. 2008, PMID:18828673 [V]: "the ligand for OA1 is L-DOPA, thus removing OA1 from orphan G-protein coupled receptor status"). On this model, GPR143 senses melanogenic activity within the organelle. *[In vitro. The ligand identity and the receptor's constitutive activity are disputed; see below]*
3. **Defective coupling to Gαi3** leads to dysregulated melanosome biogenesis. Gαi3 is the only Gαi subunit that binds Oa1. Gαi3⁻/⁻ mice phenocopy Oa1⁻/⁻ macromelanosomes, and Gαi3 protein is "barely detectable in the Oa1-/- RPE" (Young et al. 2011, PLoS ONE, PMID:21931697 [V?]; PMC3169599). *[Model organism + in vitro]*
4. **Abnormal melanosome growth** results in **macromelanosomes** and a reduced number of melanosomes in RPE and skin melanocytes. In Oa1 knockout mice these "may form by abnormal growth of single melanosomes, rather than the fusion of several" (Incerti 2000, PMID:11092754 [V]). Total melanin content is only modestly reduced, which explains the near-normal skin colour. *[Mouse, human histology]*
5. **Altered RPE signalling during eye development.** The pathway runs RPE → developing neural retina and RPE → optic stalk/chiasm. *[Inferred; the molecular intermediates are unknown]* This step branches:
   - 5a. **Arrested foveal development** leads to **foveal hypoplasia**: no foveal pit, persistent inner retinal layers, and poorly lengthened cone outer segments. *[Human OCT, demonstrated phenotype; the mechanistic link is inferred]* The common albinism hypothesis is that L-DOPA/melanogenic signalling from the RPE regulates retinal neurogenesis timing. GPR143 may be the RPE's receptor for that signal, but this is not demonstrated in humans.
   - 5b. **Excess decussation of temporal retinal ganglion cell axons** at the optic chiasm leads to a reduced uncrossed (ipsilateral) projection (Incerti 2000, PMID:11092754 [V]: "a reduction in the size of the uncrossed pathway, demonstrating a misrouting of the optic fibres at the chiasm"). The same misrouting occurs in Gαi3⁻/⁻ mice (common Oa1–Gαi3 pathway, PMC2881626). *[Mouse, demonstrated; human VEP asymmetry]*
6. **Foveal hypoplasia (5a)** leads to reduced peak cone density and acuity limited by the foveal grade. Together with **misrouting (5b)** this disrupts binocular fixation and stereopsis, which leads to **infantile nystagmus** and **strabismus**. *[Clinical correlation; nystagmus is not obligatory (isolated-FH family)]*
7. **Iris and fundus hypopigmentation** (from step 4) result in **iris transillumination** and **photophobia**. This branch is variable and can be absent.

**Controversy to record as a hypothesis or knowledge gap.** The L-DOPA ligand claim (Lopez 2008) is contested. Other groups report very high constitutive GPR143 activity, much weaker L-DOPA affinity, and Ca²⁺ responses only in RPE-derived cells. A 2019 review calls L-DOPA's role "under debate" (Front Pharmacol 2019, doi:10.3389/fphar.2019.01119 [no PMID]). The G-protein partner is also disputed (Gαi3 vs Gq/Gαo). Suggested modelling: `mechanistic_hypotheses` with an `EMERGING` L-DOPA-ligand group, and the Gαi3 coupling edge as the better-supported step.

### Ontology suggestions (all present in the repo caches)

- **GO biological process:**
  - GO:0032438 *melanosome organization* (DECREASED/abnormal)
  - GO:0042438 *melanin biosynthetic process*
  - GO:0007186 *G protein-coupled receptor signaling pathway*
  - GO:0031290 *retinal ganglion cell axon guidance*
  - GO:0007411 *axon guidance*
  - GO:0043473 *pigmentation*
- **GO cellular component:**
  - GO:0033162 *melanosome membrane*
  - GO:0042470 *melanosome*
  - GO:0005765 *lysosomal membrane*
- **CL:**
  - CL:0002586 *retinal pigment epithelial cell*
  - CL:0000148 *melanocyte*
  - CL:0000740 *retinal ganglion cell*
- **CHEBI:**
  - CHEBI:15765 *L-dopa* (proposed ligand)
  - CHEBI:18243 *dopamine* (proposed antagonist, Lopez 2008)
  - CHEBI:17895 *L-tyrosine*
- **No cached term found:** a foveal-development process term and a cone cell CL term were not in the cache. Look these up with `runoak` rather than writing them from memory.

**Molecular profiling, single-cell, and functional screens.** No disease-specific transcriptomic, proteomic, or metabolomic datasets were identified. Run `just discover-datasets` before asserting absence.

## 7. Anatomical structures affected

- **Primary:**
  - Eye: UBERON:0001786 *fovea centralis*, UBERON:0000053 *macula lutea*, UBERON:0000966 *retina*, UBERON:0001782 *pigmented layer of retina*, UBERON:0001769 *iris*
  - Visual pathway: UBERON:0000959 *optic chiasma*; UBERON:0002436 *primary visual cortex* (VEP asymmetry)
  - The optic chiasm has two UBERON candidates: UBERON:0000959 *optic chiasma* is in the cache, while UBERON:0001785 is unconfirmed. Use the cached one.
- **Secondary:** skin melanocytes, which carry macromelanosomes but are clinically silent.
- **Subcellular:** melanosome and lysosome membranes (GO above).
- **Lateralization:** bilateral and symmetric in males. In carriers the fundus pattern is mosaic and can be asymmetric.

## 8. Temporal development

- **Onset:** congenital (HP:0003577). Nystagmus appears in early infancy (HP:0003593).
- **Course:** non-progressive and stationary. Nystagmus often dampens and acuity improves modestly through childhood. There are no disease stages.
- **Critical period:** prenatal foveal and chiasmal development. Early refractive correction and amblyopia treatment in infancy and childhood optimise visual outcome.
- **Remission:** none. The condition is lifelong.

## 9. Inheritance and population

- **Inheritance:** X-linked recessive (HP:0001419). Affected males are hemizygous. Carrier females are usually unaffected or have mild fundus or iris mosaicism. Rare manifesting females arise from skewed X-inactivation.
- **Penetrance:** complete for foveal hypoplasia in hemizygous males. **Expressivity is highly variable**, ranging from classic OA1 to nystagmus without albinism to isolated FH, sometimes within one family.
- **Anticipation:** none.
- **Prevalence:**
  - Birth prevalence of about **1/50,000** for XLOA (cited in Sci Rep 2017, PMC5314354, secondary).
  - About 1/60,000 males (Genes 2025 review, MDPI 16(8):911, PMC12385408 [no PMID]).
  - These are cited estimates without a primary population study. Record them as `BIRTH_PREVALENCE` / `POINT_PREVALENCE` with `prevalence_class: BAND_1_9_PER_100000` only after quoting the source.
- **Sex ratio:** almost exclusively male.
- **Populations:** worldwide. There is a large literature from Chinese families, many with minimal albinism. This may be a reporting artefact of pigment background (minimal visible hypopigmentation in more darkly pigmented eyes) rather than a population-specific effect. No founder variants are documented.
- **Carrier frequency:** not established.

## 10. Diagnostics

- **OCT:** the key test. It grades foveal hypoplasia on the Thomas scale (grade 1–4; atypical forms) (NCIT:C20828 *Optical Coherence Tomography*, in cache).
- **Visual evoked potentials:** a crossed asymmetry on multichannel VEP shows chiasmal misrouting. There is no cached NCIT term; look one up.
- **Slit lamp and fundus examination:** iris transillumination, fundus hypopigmentation, and carrier mosaic fundus streaks.
- **Skin biopsy:** macromelanosomes. Historical and now largely replaced by genetic testing.
- **ERG:** generally normal. It helps exclude cone dystrophies and congenital stationary night blindness.
- **Genetic testing:** an inherited retinal disease, albinism, or nystagmus panel including *GPR143* (with CNV calling), or exome or genome sequencing. Deletion detection by MLPA or array/CNV analysis is essential because large deletions are common. Consider an Xp22.3 contiguous-gene deletion when ichthyosis or anosmia is also present.
- **Differential diagnosis:**
  - Oculocutaneous albinism: *TYR*, *OCA2*, *TYRP1*, *SLC45A2*, and others; distinguished by skin and hair involvement and AR inheritance
  - *SLC38A8* FHONDA (AR)
  - *PAX6* foveal hypoplasia (AD; iris anomalies)
  - *FRMD7* X-linked idiopathic infantile nystagmus (normal fovea, no misrouting)
  - *CACNA1F* Åland Island eye disease (XL; abnormal ERG; PMID:33513752 cached)
  - Achromatopsia; blue-cone monochromacy
  - Hermansky–Pudlak and Chédiak–Higashi syndromes (systemic features)
- **Screening:** no newborn screening. Carrier testing of at-risk females and cascade testing are appropriate.

## 11. Outcome and prognosis

- **Survival:** normal life expectancy, with no disease-specific mortality.
- **Morbidity:** lifelong reduced acuity, often in the 20/60–20/200 range, though anywhere from near-normal to legally blind. Additional morbidity comes from nystagmus, strabismus, absent or reduced stereopsis, photophobia, and amblyopia.
- **Prognostic factor:** foveal hypoplasia grade on OCT is the best predictor of acuity across albinism and FH, and higher grades give worse acuity. No molecular biomarkers are prognostic.

## 12. Treatment

There is no disease-modifying therapy. Management is supportive:

| Intervention | NCIT (cached) | Notes |
|---|---|---|
| Refractive correction, tinted or photochromic lenses | NCIT:C15747 Supportive Care | Eyeglass or contact-lens NCIT terms not in cache; treat as devices, not `TreatmentTerm`s |
| Low-vision aids and rehabilitation | NCIT:C15315 Rehabilitation | `therapeutic_modality: DEVICE` / `BEHAVIORAL` |
| Amblyopia therapy (occlusion) | NCIT:C15747 | Childhood |
| Strabismus surgery; nystagmus surgery (Kestenbaum/Anderson for a null-point head turn) | NCIT:C15329 Surgical Procedure | `therapeutic_modality: SURGERY` |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — |
| **Levodopa (experimental)** | NCIT:C15986 Pharmacotherapy + CHEBI:15765 L-dopa as `therapeutic_agent` | Rationale: GPR143 as the L-DOPA receptor. A University of Minnesota RCT (45 subjects with mixed albinism genotypes; levodopa/carbidopa 0.76 or 0.51 mg/kg vs placebo, 20 weeks) found **no statistically significant improvement in BCVA** (Summers et al. 2014, *Clin Exp Ophthalmol*, doi:10.1111/ceo.12325; PMID possibly 24641678 [V?]; trial probably NCT01176435, matched by sponsor and topic). Not OA1-specific |

- **Gene therapy:** AAV-mediated Oa1 transfer partly rescued retinal function and morphology in Oa1⁻/⁻ mice (Surace and colleagues, Univ. Modena/TIGEM; IRIS record [no PMID]). No human trials were identified.

## 13. Prevention

- **Primary prevention:** carrier testing, prenatal diagnosis, and PGT for families with a known variant.
- **Secondary prevention:** early diagnosis in infants with nystagmus (OCT plus a gene panel), which allows early refraction and amblyopia management.
- **Tertiary prevention:** UV and glare protection, management of strabismus and amblyopia, educational and low-vision support.
- **Not applicable:** vaccines and public-health measures.

## 14. Other species and natural disease

- **Orthologs:** mouse *Gpr143* (MGI), zebrafish *gpr143*, and *GPR143* in other mammals.
- **Naturally occurring disease:** no OMIA entry for a naturally occurring *GPR143* disease was identified in this search. Check OMIA before asserting absence.
- **Conservation:** the receptor–Gαi3–melanosome axis is conserved in mouse.

## 15. Model organisms

| Model | Phenotype recapitulation | Limitations | Ref |
|---|---|---|---|
| **Oa1 (Gpr143) knockout mouse** | RPE macromelanosomes; reduced uncrossed retinofugal projection (chiasmal misrouting); males viable and otherwise normal | Mice have no fovea, so the defining human phenotype cannot be modelled (`FAILS_TO_RECAPITULATE` for foveal hypoplasia → a `HUMAN_MODEL_MISMATCH` discussion) | Incerti 2000, PMID:11092754 [V] |
| **Gnai3 knockout mouse** | Phenocopies Oa1⁻/⁻ macromelanosomes and optic misrouting | Pathway model, not a disease-gene model | PMC2881626; Young 2011, PMID:21931697 [V?] |
| Oa1⁻/⁻ × Gnai3⁻/⁻ and Gαi1/Gαi3 double knockouts | Show the Gαi3 specificity (Gαi1⁻/⁻ and Gαi2⁻/⁻ have no macromelanosomes) | — | PMC3169599 |
| AAV-Oa1 gene transfer in Oa1⁻/⁻ mouse | Partial rescue of retinal function and morphology | No fovea | IRIS Unimore record [no PMID] |
| Cell systems (melanocytes, RPE lines, heterologous GPR143 expression) | Ligand and G-protein studies | Disputed results that depend on the cell line and medium (tyrosine in commercial media) | Lopez 2008, PMID:18828673 [V] |

---

## Curation notes for the dismech entry

1. **Naming and scope.** The current skeleton `kb/disorders/GPR143-Related_Foveal_Hypoplasia.yaml` lists "X-linked ocular albinism / OA1" as synonyms. Under the umbrella MONDO term these are better represented as `has_subtypes`: *X-linked ocular albinism* (MONDO:0021019), *NYS6* (MONDO:0010435), and *isolated foveal hypoplasia*. The name follows the `<GENE>-Related <Phenotype>` convention, consistent with the MONDO label.
2. **Gene validity.** Copy the ClinGen Definitive XL assertion verbatim from the cached CGGV row.
3. **Before quoting anything,** run `just fetch-reference` for PMIDs 33785018, 11092754, 18828673, 21931697, 27958203, 38222445, 8634705, 11214907, 37053367, 20301517, and the levodopa-trial PMID. Confirm each [V?] PMID matches the intended paper.
4. **Mechanism.** Model the L-DOPA ligand step as an `EMERGING` hypothesis. Wire foveal hypoplasia, nystagmus, and misrouting as phenotypes downstream of the melanosome and RPE-signalling nodes, so they do not float disconnected.

## Sources
- [Liu et al., GPR143 deletion in X-linked congenital nystagmus (PMC5200982)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5200982)
- [GPR143 mutations in an X-linked INS cohort, SE China (PubMed 38222445)](https://ncbi.nlm.nih.gov/pubmed/38222445)
- [Han et al. 2015, Sci Rep (PMC4498220)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4498220)
- [Hu et al. 2011, GPR143 splicing mutation (PMC3060156)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3060156/)
- [Novel GPR143 duplication in XL congenital nystagmus (PMC2671585)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2671585/)
- [Mao et al. 2021, isolated foveal hypoplasia (PMC8011130)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8011130/)
- [Sci Rep 2017 three-family study (PMC5314354)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5314354)
- [Five-generation family (PMC3423421)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3423421/)
- [Incerti et al. 2000, Oa1 knock-out (PubMed 11092754)](https://pubmed.ncbi.nlm.nih.gov/11092754/)
- [Young et al. 2011, Gαi3–Oa1 (PMC3169599)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3169599/)
- [Gαi3/Oa1 optic chiasm study (PMC2881626)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2881626)
- [Lopez et al. 2008, L-DOPA is an endogenous ligand for OA1 (PMC2553842)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2553842)
- [Front Pharmacol 2019 GPR143 review](https://www.frontiersin.org/articles/10.3389/fphar.2019.01119/full)
- [Bassi et al. 1995, Nat Genet](https://www.nature.com/articles/ng0595-13.pdf)
- [OA1 gene mutations in one-third of XLOA patients](https://api-pubmed-ncbi.laibokeji.com/8634705)
- [GPR143-associated OA in a Hispanic family, review (PMC12385408)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12385408/)
- [MedlinePlus Genetics: ocular albinism](https://medlineplus.gov/genetics/condition/ocular-albinism)
- [Summers et al., levodopa RCT in albinism](https://experts.arizona.edu/en/publications/does-levodopa-improve-vision-in-albinism-results-of-a-randomized-/)
- [NCT01176435 trial listing](https://www.syfrah.com/trial/NCT01176435)
- [AAV gene transfer in OA1 mouse (IRIS Unimore)](https://iris.unimo.it/retrieve/78334a7a-8b68-43ed-97a3-c51f318222a6/VOR_Amelioration%20of%20both%20Functional%20and%20Morphological%20Abnormalities%20in%20the%20Retina%20of%20a%20Mouse%20Model%20of%20Ocular%20Albinism%20Following%20AAV-Mediated%20Gene%20Transfer.pdf)
- [Nystagmus 6, congenital, X-linked (Arizona eye disorders)](https://disorders.eyes.arizona.edu/node/2374)
- [Foveal hypoplasia and ocular albinism atlas](https://atlas.codexdigital.com.au/view-the-atlas/chapter-outlines/macular-disease/foveal-hypoplasia-and-ocular-albinism)
- Local repo sources: `stubs/GPR143-related_Foveal_Hypoplasia.yaml`, `cache/clingen/gene_validity.csv`, `cache/bookshelf/genereviews.csv`, `references_cache/PMID_34445325.md`, `references_cache/PMID_33513752.md`, and the `cache/{hp,cl,go,uberon,chebi,ncit}/terms.csv` term caches.