---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T21:59:48.223706'
end_time: '2026-10-27T22:07:37.538363'
duration_seconds: 469.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 39, Multiple Types
  mondo_id: MONDO:0014075
  category: Mendelian
  causal_genes: CRYGB
  omim_id: OMIM:615188
  synonyms: CRYGB early-onset non-syndromic cataract; CTRCT39; cataract 39, multiple
    types, autosomal dominant; early-onset non-syndromic cataract caused by mutation
    in CRYGB
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
  num_turns: 38
  total_cost_usd: 3.0293374
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 5
citation_count: 12
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 26
  on_topic: 24
  validator_version: 0.4.0
term_validation:
  total_terms: 37
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 2
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 39, Multiple Types
- **MONDO ID:** MONDO:0014075 (if available)
- **Causal gene(s):** CRYGB
- **OMIM:** OMIM:615188
- **Synonyms:** CRYGB early-onset non-syndromic cataract; CTRCT39; cataract 39, multiple types, autosomal dominant; early-onset non-syndromic cataract caused by mutation in CRYGB
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cataract 39, Multiple Types** covering all of the
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

Still researching: I found the founding CRYGB family paper (Kuwaiti family, PMID 23288985) and am now pulling its details and other CRYGB reports.

Pulling verbatim abstracts for the key CRYGB papers so the report can quote them exactly.

Checking GenCC classifications and a second mouse Crygb model (S11R, Li et al. 2008).

Checking one last source, a 2002 Indian family study that UniProt cites for a CRYGB S73I variant, before writing the report.

# Cataract 39, Multiple Types (CTRCT39; *CRYGB*): Research Report

**Target:** Cataract 39, multiple types (MONDO:0014075; OMIM:615188). **Causal gene:** *CRYGB* (γB‑crystallin; hgnc:2409; NCBI Gene 1419; UniProt P07316; OMIM gene 123670; chromosome 2q33.3, in the *CRYGA–CRYGD* γ‑crystallin cluster).
**Date:** 2026‑10‑27

---

## Bottom line

CTRCT39 is autosomal dominant congenital or early‑onset non‑syndromic cataract attributed to heterozygous variants in ***CRYGB***. The human evidence is **one Kuwaiti family** (AlFadhli et al. 2012, PMID:23288985). OMIM, PanelApp and GenCC all trace back to that report.

The evidence is thin:
- **Gene–disease validity is Limited.** GenCC holds Limited calls from Labcorp/Invitae and from G2P.
- **A 2026 ClinGen‑protocol curation also rated it Limited.** Ing et al. (PMID:42091610) scored *CRYGB* "No Known Disease Relationship" on clinical evidence alone, and reached Limited only once mouse data were added.
- **Genomics England PanelApp lists *CRYGB* as Red** (low evidence).

The mechanism comes almost entirely from two mouse *Crygb* alleles, *Crygb^nop* and *Crygb^S11R*. **Treat this as a weakly supported entity.**

**How the evidence was checked.**
- **Verbatim quotes.** Quotes marked † were copied from the repository's own `references_cache/` files. All other quotes came through Europe PMC's REST API via a summarising fetch tool. They are probably exact but must be re‑checked with `just fetch-reference` / `just count-verified-snippets` before they go into the KB.
- **Unread sources.** PubMed, PMC, ClinVar and OMIM pages returned bot‑check screens, so ClinVar variant counts and OMIM text were not read directly.
- **Sandbox limits.** This session could not run `curl` or `just fetch-reference`.

---

## 1. Disease information

**Overview.** CTRCT39 is lens opacity of congenital or early‑childhood onset, without systemic features, caused by heterozygous *CRYGB* variants. In the founding family it appeared as three morphologies: lamellar, anterior polar, and total ("complete") cataract.

UniProt (P07316) gives this disease annotation for *CRYGB*: CTRCT39 is an autosomal dominant lens opacification whose types include lamellar, anterior polar and complete cataract. The opacities "vary in location and may be static or progressive."

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0014075 "cataract 39 multiple types" (parent: MONDO:0011060 early‑onset non‑syndromic cataract) |
| OMIM | 615188 (gene: 123670 *CRYGB*) |
| MedGen / UMLS | C3808800 |
| Orphanet | No CTRCT39‑specific code found. Orphanet links *CRYGB* (GenCC "Supportive") to ORPHA:98994 total early‑onset cataract (MONDO:0021548), ORPHA:98988 early‑onset anterior polar cataract (MONDO:0020373), and ORPHA:441452 early‑onset lamellar cataract (MONDO:0018611) |
| ICD‑10 | Q12.0 congenital cataract (category level; no gene‑specific code) |
| ICD‑11 | LA12.0 congenital cataract (category level; verify) |
| MeSH | D002386 Cataract (with the "congenital" qualifier; no specific heading) |

**Synonyms:** CTRCT39; cataract 39, multiple types, autosomal dominant; CRYGB early‑onset non‑syndromic cataract; early‑onset non‑syndromic cataract caused by mutation in CRYGB.

**Kind of evidence:** all of it is disease‑level and literature‑derived, from one family pedigree plus model organisms. There are no EHR or registry data.

Sources: [GenCC CRYGB](https://thegencc.org/genes/HGNC:2409); [MedGen C3808800 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C3808800/index.html); [UniProt P07316](https://rest.uniprot.org/uniprotkb/P07316.txt).

---

## 2. Etiology

**Cause.** Monogenic: heterozygous germline *CRYGB* variants, autosomal dominant.
- **Founding report.** AlFadhli et al. 2012 (Mol Vis 18:2931‑6; PMID:23288985) studied a three‑generation Kuwaiti family with seven affected members. A 250K SNP scan gave a LOD of 1.49 at 2q33‑37, spanning the *CRYG* cluster. The highest LOD, 1.5 at 2q34‑36.1 containing *CRYBA2*, yielded no *CRYBA2* variants.
- **Key quotes:**
  - "We report the linkage of ADCC to chromosome 2q33-37, which spans the CRYGB gene."
  - The study "revealed two novel heterozygous deletions and one trinucleotide polymorphism in the CRYGB gene"
  - "This study is the first to report complex heterogeneous mutations in the CRYGB gene"
- **Statistical caveat.** A LOD of about 1.5 is well short of the conventional threshold of 3 for significant linkage. The gene assignment therefore rests on finding a candidate‑gene variant inside a suggestive interval.

**Genetic risk and susceptibility**
- ***CRYGB* promoter SNP rs2289917 (c.‑47T>C) in Indian cohorts.**
  - Mehra et al. 2011 (PMID:21941057), case‑control study: "-47C allele of rs2289917 in CRYGB showed the strongest association with cataract". In silico analysis suggested altered progesterone‑receptor binding.
  - Fatima et al. 2026 (PMID:41581034) replicated it in North Indian families: "The association of rs2289917 (c.-47T>C) with inherited cataract substantiates the previous findings."
  - Kapur et al. 2009 (PMID:19384013) give baseline western‑Indian control frequencies and report that a *CRYGB* promoter variant "impacts the binding of two transcription factors".
  - **These are association signals and do not cause CTRCT39.** Model them, if at all, as SUSCEPTIBILITY, not CAUSATIVE.
- **Common benign variation.** An intronic *CRYGB* variant, rs796288, has a gnomAD allele frequency of about 0.28 and is classed benign ([genebe](https://genebe.net/variant/hg38/rs796288)). Common variants in *CRYGB* must not be read as pathogenic.

**Environmental and protective factors.** None are documented for CTRCT39. The generic risk factors for congenital cataract (intrauterine TORCH infection, galactosaemia, prematurity) are differential diagnoses, not modifiers. One relevant mouse result: raising lens gap‑junction coupling (α8Kiα3 knock‑in) fully prevented γB‑S11R nuclear cataract (PMID:20844585). That is a *genetic* protective modifier in mice.

**Gene–environment interaction:** no data.

---

## 3. Phenotypes

Source for all rows: PMID:23288985 (n = 7 affected plus 1 infant carrier). No frequencies beyond this family exist.

| Phenotype | Suggested HPO | Detail in family |
|---|---|---|
| Congenital/early‑onset bilateral cataract | HP:0000519 Congenital cataract; HP:0010696 Bilateral cataract (verify) | All affected; all except the founder (I‑1) had surgery at an early age |
| Lamellar cataract | HP:0007971 Lamellar cataract (verify label) | 4 affected (I‑2, II‑5, III‑1, III‑4), all carrying g.67delG |
| Anterior polar cataract | HP:0001133 Anterior polar cataract (verify; some HPO releases use "Anterior polar cataract" under HP:0007968) | 2 affected (I‑1, III‑2), carrying g.167delC |
| Total/complete cataract | HP:0010920 Total cataract (verify) | 1 affected (II‑3), compound heterozygous for both deletions |
| Visual impairment / amblyopia risk | HP:0000505 Visual impairment; HP:0000646 Amblyopia | Inferred: early surgery implies the opacities affected vision |

- **Onset:** congenital or infantile. Ages are not given in the paper. Infant carrier III‑3 had no opacity yet, which the authors attributed to age.
- **Severity:** mild for anterior polar, moderate to severe for lamellar, severe for total.
- **Progression:** UniProt says "static or progressive". No longitudinal data exist.
- **Quality of life:** no disease‑specific data. Paediatric cataract in general carries amblyopia and nystagmus risk and a lifelong burden of aphakia, glaucoma and visual‑axis opacification (PMID:35307324†).
- **Not reported in CTRCT39:** microphthalmia, microcornea, nystagmus or glaucoma. These are seen with *CRYGC* and *CRYGD* (e.g., PMID:19204787, PMID:35719371) and must not be carried over to *CRYGB*.

**Expected HPO inheritance term:** HP:0000006 Autosomal dominant inheritance.

---

## 4. Genetic and molecular information

**Gene and protein.** *CRYGB* encodes γB‑crystallin, 175 aa. UniProt annotates four βγ Greek‑key motifs: GK1 2–40, GK2 41–83, connecting peptide 84–88, GK3 89–129, GK4 130–172. These form two domains. Function: "the dominant structural components of the vertebrate eye lens".

**Reported variants (all germline, heterozygous)**

| Variant (as published; numbered from ATG, genomic‑style) | Location | Predicted effect | Phenotype | Notes |
|---|---|---|---|---|
| g.67delG | intron 1, 27 bp from the splice acceptor | possible splicing change (untested; no lens tissue) | lamellar | Cosegregated; absent in 50 ethnically matched controls |
| g.167delC | exon 2 | frameshift → 19 non‑native residues → truncation at 43 aa (likely LoF / NMD, or a short product) | anterior polar | Absent in controls |
| g.20‑22GGT>AAA | intron 1, by the donor site | unknown | — | Found in an unaffected member (II‑2); judged a polymorphism |

- **Missing HGVS nomenclature.** No HGVS c./p. nomenclature on a RefSeq transcript (NM_005210) was published. The variants need re‑mapping before ClinVar lookup or KB entry. Neither appeared in the population or ClinVar data this session could reach.
- **Compound heterozygosity.** One patient (II‑3) carried both deletions and had total cataract. The paper states: "Another patient with complete cataracts was a compound heterozygote with both of the above-mentioned mutations." PanelApp records that "biallelic mutations cause a more SEVERE disease form". That rests on this single person.
- **UniProt variant S73I.** UniProt lists S73I (VAR_021140) "in autosomal dominant congenital cataract", citing Santhiya et al. 2002 (J Med Genet 39:352; PMID:12011157). The full text could not be retrieved to check segregation, so treat it as **unresolved**. It may be a polymorphism found during γ‑crystallin screening. R90T (rs2241980) and I111L (rs796287) are listed as common polymorphisms.
- **Validity assessments**
  - GenCC: Limited (Labcorp/Invitae, 2023); Limited (G2P, 2025).
  - Orphanet: Supportive, for the three morphology‑specific Orphanet terms.
  - PanelApp: Red. Curator note: "not enough evidence at this time for the gene to be promoted to green."
  - Ing et al. 2026†: "four genes have Limited support (CRYBA2, CRYBA4, CRYBB3 and CRYGB)… CRYGB from No Known Disease Relationship (given absence of clinical evidence) to Limited".
  - No ClinGen CGGV record for *CRYGB* was found, so `gene_disease_validity` should only copy GenCC‑sourced tiers, with `classified_by` set accordingly.
- **Functional class:** unresolved. The exon‑2 frameshift suggests loss of function. The mouse alleles act dominantly through aggregation, a toxic gain of function or dominant‑negative mechanism (Section 6). There is no human functional study.
- **Case fraction:** *CRYGB* was absent from the solved genes in large Chinese, Australian, Swiss and US cohort screens (e.g., PMID:31523120, PMID:36161833†, PMID:23508780). It is a very rare cause.
- **Modifiers, epigenetics, chromosomal abnormalities:** none reported.

---

## 5. Environmental information

There are no environmental, lifestyle or infectious contributors. This is not applicable beyond ruling out phenocopies such as congenital rubella and galactosaemia.

---

## 6. Mechanism and pathophysiology

**Causal chain.** Human steps are largely **inferred**. Mouse steps are **demonstrated** in *Crygb^nop* and *Crygb^S11R*.

1. A heterozygous germline *CRYGB* variant (frameshift, putative splice or missense) **leads to** abnormal γB‑crystallin: truncated, misfolded, or absent from one allele.
   - Human: inferred, PMID:23288985.
   - Mouse *Crygb^nop*: an 11‑bp→4‑bp replacement in exon 3 truncates the protein at residue 144, "predicted to alter protein folding" (PMID:9782080).
2. Misfolded or truncated γB‑crystallin, which lacks the fourth Greek key, **results in** loss of solubility and amyloid‑like aggregation inside lens fibre cells. In *Crygb^nop*, "recombinant mutant γB-crystallin readily formed amyloid fibrils under physiological buffer conditions" (Sandilands et al. 2002, EMBO J; **PMID:12426373**).
3. Aggregates are **targeted to fibre‑cell nuclei**, forming Congo‑red‑positive intranuclear inclusions from E14.5. In the authors' words, "the formation of intranuclear inclusions is a key event in cataract formation" (PMID:12426373). Altered fibrillarin and CP49 nuclear entry show disrupted nuclear function and premature, abnormal denucleation. In the authors' words, "The mutant γ-crystallins initially disrupt nuclear function, but then this progresses to a full cataract phenotype".
4. **Branch (S11R missense model, PMID:18172107).** The mutant protein **leads to** raised lens Ca²⁺. That **leads to** Ca²⁺‑dependent degradation of crystallins and the cytoskeleton, disrupted inner fibre cells and dense nuclear cataract.
   - Quotes: "ICP-OES confirmed a substantial elevation of calcium concentration in mutant lenses"; "increased degradation of crystallin proteins correlated with the nuclear cataract."
   - Calpain involvement is inferred, not shown in that abstract.
   - Raising gap‑junction coupling (α8Kiα3 Cx46 knock‑in) restored calcium, actin and crystallin integrity and prevented the cataract (PMID:20844585). This indicates that **failure of lens fibre‑cell microcirculation/coupling** is a downstream amplifier.
5. Disorganised or degenerated primary (nuclear) fibre cells plus protein aggregates **result in** light scattering. That is the **lens opacity**, with morphology set by which fibre cohort is affected at what time: nuclear or lamellar opacity versus anterior polar.
   - The genotype–morphology mapping in the Kuwaiti family is observed but **mechanistically unexplained**.
   - The authors also speculated that truncated γB may interfere with α‑crystallin subunit exchange (inferred).
6. Visual‑axis opacity in infancy **leads to** form‑deprivation amblyopia (and possibly nystagmus) unless removed surgically in time. This is general paediatric cataract biology (PMID:35307324†).

**Upstream vs downstream.** The upstream steps are protein misfolding and aggregation. Nuclear inclusion formation and Ca²⁺ dysregulation are midstream. Downstream are fibre‑cell degeneration and denucleation defects, then opacity, then amblyopia.

**Analogous γ‑crystallin evidence (CRYGC, not CRYGB).** The *CRYGC* 5‑bp duplication activates the PERK–ATF4–CHOP unfolded protein response (UPR), autophagy and apoptosis (PMID:39994382†): "induces UPRer and UPRmt stress responses primarily through the PERK-dependent and Atf4/Atf5/Ddit3 pathways… inducing autophagy and apoptosis and thence congenital nuclear cataracts". Mark any UPR node in a *CRYGB* entry as hypothesis or analogy.

**Suggested ontology terms (verify every CURIE by lookup before binding)**

| Category | Terms |
|---|---|
| GO biological process | visual perception (GO:0007601); lens development in camera‑type eye (GO:0002088); lens fiber cell differentiation (GO:0070306); protein aggregation / amyloid fibril formation (GO:1990000); cellular calcium ion homeostasis (GO:0006874); lens fiber cell denucleation / nucleus organization (verify, e.g., GO:0070309); gap junction‑mediated intercellular transport (verify) |
| GO molecular function | structural constituent of eye lens (GO:0005212) |
| GO cellular component | nucleus (GO:0005634); cytoplasm (GO:0005737) |
| Cell types (CL) | lens fiber cell (CL:0011004); primary lens fiber cell (verify); lens epithelial cell (CL:0002224) |
| Chemical (CHEBI) | calcium(2+) (CHEBI:29108) |
| Molecular profiling | No CRYGB‑specific GEO, proteomic or single‑cell datasets found. Generic lens differentiation multi‑omics exist (e.g., PMID:37189439) but are not disease‑specific |

---

## 7. Anatomical structures

- **Organ:** eye, specifically the lens.
  - Suggested UBERON: lens of camera‑type eye (UBERON:0000965); lens nucleus (UBERON:0011797, verify); lens cortex; anterior lens capsule region for anterior polar cataract.
  - No secondary organ involvement. Body system: visual.
- **Tissue and cells:** lens fibre cells, primary and secondary; lens epithelium.
- **Subcellular:** cytosol and nucleus. In the mouse, intranuclear inclusions are lens‑specific (PMID:12426373).
- **Laterality:** bilateral is typical of AD congenital cataract. The paper does not state laterality explicitly, so verify before binding.

---

## 8. Temporal development

- **Onset:** congenital or infantile. In mouse, γB is first detected at E14.5 with morphological changes by E15.5 (PMID:12426373).
- **Course:** static or slowly progressive (UniProt); no natural‑history study exists.
- **Critical period:** the amblyogenic window. Visually significant bilateral infantile cataracts are classically removed within the first weeks to months (PMID:35307324†).
- **Remission:** none spontaneously; the cataract is resolved only by surgical removal.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006).
- **Penetrance:** complete for g.67delG in adult carriers (assumed in the linkage model; one infant carrier unaffected so far).
- **Expressivity:** variable, as allelic and compound‑heterozygote morphologic heterogeneity within one family.
- **Anticipation, germline mosaicism, consanguinity:** none reported.
- **Prevalence:** unknown for CTRCT39. Only one family is reported. Use `prevalence_class` with `measure_type: CASES_IN_LITERATURE`.
  - Context: congenital cataract overall is about 1–6 per 10,000 live births (PMID:28298635†, PMID:35719371†).
- **Populations:** Kuwaiti (Arab) family. Indian association studies concern a promoter SNP, not Mendelian disease. No founder effect is known.
- **Sex ratio:** not reported.

---

## 10. Diagnostics

- **Clinical:**
  - Red‑reflex screening at birth.
  - Slit‑lamp biomicroscopy to classify morphology (lamellar, anterior polar, total).
  - Dilated fundus examination.
  - B‑scan ultrasound when the opacity is dense.
  - Visual‑function assessment (fixation, preferential looking).
  - No biochemical biomarkers exist.
- **Exclusion tests for non‑genetic and syndromic causes:**
  - TORCH serology.
  - Galactosaemia testing: red‑cell GALT and galactose metabolites.
  - Plasma calcium.
  - Urine amino acids for Lowe syndrome.
- **Genetic testing:**
  - First line is a congenital cataract multigene panel or exome. PanelApp includes *CRYGB* only as Red.
  - Single‑gene testing is reasonable when 2q33 linkage is shown in a family.
  - Interpret variants carefully. Rely on segregation and population frequency, because *CRYGB* has common benign variation (rs796288 AF ≈ 0.28) and the gene's disease link is Limited.
  - Chromosomal microarray, karyotype, FISH, mtDNA and repeat expansion testing are not applicable.
- **Differential diagnosis:**
  - Other γ‑crystallin cataracts: *CRYGC* (CTRCT2), *CRYGD* (CTRCT4), *CRYGS*. These are often nuclear with microcornea.
  - β/α‑crystallins; connexins *GJA8*/*GJA3*; *MIP*, *BFSP1/2*, *HSF4*, *PITX3*.
  - Syndromic cataract: Lowe, Nance–Horan, galactosaemia, BCOR/OFCD (PMID:36261622).
  - Congenital rubella.
- **Screening:** newborn red‑reflex examination. Cascade ophthalmic and genetic testing of relatives once a familial variant is confirmed. Prenatal or preimplantation testing is technically possible but rarely used for isolated cataract.

---

## 11. Outcome and prognosis

- **Survival:** normal life expectancy; the disease is non‑lethal.
- **Morbidity** follows paediatric cataract generally (PMID:35307324†):
  - Amblyopia, strabismus and nystagmus.
  - After surgery: visual‑axis opacification and long‑term glaucoma in "about a third of patients."
  - Lifelong aphakia or pseudophakia management.
- **Prognostic factors:**
  - Morphology: anterior polar often has little visual effect; total/dense has the highest amblyopia risk.
  - Timing of surgery, bilaterality, absence of nystagmus or strabismus, and amblyopia‑therapy compliance (PMID:35307324†).
  - In the founding family, the anterior polar founder (I‑1) was the only affected member not operated on early. This is consistent with milder disease.

---

## 12. Treatment

There is no disease‑specific or molecular therapy.

| Intervention | Notes | Suggested NCIT (verify) |
|---|---|---|
| Cataract extraction (lensectomy ± anterior vitrectomy) | For visually significant opacity; early surgery in infancy | NCIT:C51677 Cataract Extraction (verify) / NCIT:C15329 Surgical Procedure; `therapeutic_modality: SURGERY` |
| Intraocular lens implantation, or aphakic contact lens/spectacles | IOL in infants <6 months gives good outcomes, but contact lenses may be preferred (PMID:35307324†) | NCIT procedure term for IOL implantation (look up); the lens itself is a device, so attach it as a qualifier (CLAUDE.md device pattern) |
| Amblyopia therapy (occlusion/patching, refractive correction) | Essential after surgery | NCIT term for occlusion therapy (look up); `BEHAVIORAL` / `DEVICE` |
| Long‑term glaucoma surveillance and treatment | Post‑surgical complication | — |
| Observation | Small anterior polar opacities | — |

- **Experimental:** no CRYGB trials.
  - Pharmacological "anti‑aggregation" approaches (e.g., lanosterol, 25‑hydroxycholesterol) have been explored for crystallin cataracts in general, but remain preclinical and are unvalidated for CRYGB.
  - In mice, gap‑junction enhancement prevented γB‑S11R cataract (PMID:20844585). That is a mechanistic proof of concept, not a therapy.
- **Pharmacogenomics:** not applicable.

---

## 13. Prevention

- **Primary:** none, apart from reproductive options (prenatal or preimplantation testing) after genetic counselling. The recurrence risk is 50% per pregnancy for a heterozygous parent.
- **Secondary:** newborn red‑reflex screening, and early examination of infants born into the family (as with infant carrier III‑3).
- **Tertiary:** timely surgery, amblyopia management, and glaucoma surveillance.
- **Counselling:** genetic counselling (NCIT:C15240) with explicit discussion of the gene's Limited validity status.

---

## 14. Other species and natural disease

- **Dog:** canine *CRYGB*, *CRYGC* and *CRYGS* were evaluated as candidates for hereditary cataract in the dachshund (Müller et al. 2007, PMID:17327821). No causal *CRYGB* variant has been reported in dogs.
- **Angolan lion:** *CRYG* candidate markers were developed for lion cataract (PMID:20423916); no causal finding.
- **OMIA:** no *CRYGB* entry identified.
- **Orthologs:** mouse *Crygb* (MGI:88522, chromosome 1 within the *Cryga–Cryge* cluster), conserved across vertebrates. The βγ‑crystallin Greek‑key fold is conserved.

---

## 15. Model organisms

| Model | Genotype | Phenotype | Fidelity / limitations | PMID |
|---|---|---|---|---|
| ***Crygb^nop*** (formerly *Cat2^nop*; strain (101/El × C3H/El)F1‑*Crygb^Nop*/Ieg, INFRAFRONTIER/EMMA) | 11 bp→4 bp replacement in exon 3, giving truncation at residue 144 (lacks GK4); dominant | Intranuclear amyloid‑like γB inclusions from E14.5; fibre‑cell swelling and small lens at E15.5; opaque nucleus at birth; disorganised primary fibres | PARTIALLY_RECAPITULATES congenital nuclear cataract. The allele differs from the human variants, and mouse γ‑crystallin abundance far exceeds human (human γB is minor in adult lens) | 9782080; 12426373; 15037589 |
| ***Crygb^S11R*** (spontaneous, JAX) | A→C missense, S11R; dominant | Homozygotes: dense nuclear cataract, raised lens Ca²⁺, crystallin degradation, inner fibre disruption | Mechanistic model of Ca²⁺‑driven degradation. Missense (not frameshift), and the severe phenotype is described in homozygotes | 18172107 |
| *Crygb^S11R* × α8Kiα3 (Cx46 knock‑in) | Genetic rescue | Homozygous knock‑in "fully prevented nuclear cataracts"; normal Ca²⁺ | RESCUES. Proof that gap‑junction coupling is a modifier | 20844585 |

- **Other model types:** no zebrafish *crygb* model specific to the human disease was found, although zebrafish crystallin models are reviewed in PMID:40206405. No iPSC lentoid or organoid studies of *CRYGB* were found.
- **Mouse alleles map to a different human gene name in places.** Older mouse literature names the *Cryg* cluster genes by mouse nomenclature, and *Cryge*/*Crygf* have no functional human orthologs (human *CRYGEP*/*CRYGFP* are pseudogenes). Do not transfer *Cryge* or *Cryga* findings to *CRYGB*.

---

## Curation notes for the KB entry

1. **Record validity honestly.** Keep `relationship_type: CAUSATIVE` only if justified, since the KB schema defines it as Definitive or Strong. Record the GenCC Limited tiers with their true `classified_by`. Consider a `KNOWLEDGE_GAP` discussion: "single family, sub‑threshold LOD, untested splice variant."
2. **Modelling the mechanism.** Pathophysiology nodes resting on *Crygb^nop* / *S11R* evidence should carry `evidence_source: MODEL_ORGANISM`. Any UPR node borrowed from *CRYGC* should be marked as a hypothesis.
3. **Variant nomenclature.** The founding variants need HGVS re‑mapping, and the S73I report (PMID:12011157) needs its full text checked.
4. **Uncached references.** These PMIDs are not yet in `references_cache/` and must be fetched: 23288985, 12426373, 9782080, 18172107, 20844585, 21941057, 41581034, 19384013, 15037589, 17327821.

---

## Sources

- AlFadhli S et al. Mol Vis 2012;18:2931‑6. PMID:23288985. [PMC3533929](https://pmc.ncbi.nlm.nih.gov/articles/PMC3533929/)
- Sandilands A et al. EMBO J 2002;21:6005‑14. PMID:12426373. [PMC137201](https://pmc.ncbi.nlm.nih.gov/articles/PMC137201/)
- Klopp N et al. Genomics 1998. PMID:9782080. [PubMed](https://pubmed.ncbi.nlm.nih.gov/9782080/)
- Graw J et al. IOVS 2004. PMID:15037589. [PubMed](https://pubmed.ncbi.nlm.nih.gov/15037589/)
- Li L et al. IOVS 2008;49:304‑9. PMID:18172107
- Li L et al. PLoS One 2010. PMID:20844585
- Ing A et al. Ophthalmic Genet 2026. PMID:42091610†
- Mehra S et al. J Postgrad Med 2011. PMID:21941057
- Fatima AE et al. Indian J Ophthalmol 2026. PMID:41581034
- Kapur S et al. Indian J Ophthalmol 2009. PMID:19384013
- Santhiya ST et al. J Med Genet 2002. PMID:12011157 (not verified)
- Lenhart PD, Lambert SR. Surv Ophthalmol 2022. PMID:35307324†
- Shah MH et al. Sci Rep 2025. PMID:39994382† (CRYGC analogy)
- Müller C et al. Mol Vis 2007. PMID:17327821
- [GenCC CRYGB](https://thegencc.org/genes/HGNC:2409)
- [PanelApp CRYGB](https://panelapp.genomicsengland.co.uk/panels/230/gene/CRYGB)
- [UniProt P07316](https://rest.uniprot.org/uniprotkb/P07316.txt)
- [OMIM 615188](https://www.ncbi.nlm.nih.gov/omim/615188)
- [INFRAFRONTIER Crygb^Nop](https://infrafrontier.eu/strain-search/straindetails/?q=12559)
- [genebe rs796288](https://genebe.net/variant/hg38/rs796288)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 26 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000965` (1 mention) - the report calls it "Suggested UBERON: lens of camera‑type eye"; UBERON calls it **lens of camera-type eye**
- `NCIT:C15240` (1 mention) - the report calls it "Counselling:** genetic counselling"; NCIT calls it **Genetic Counseling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.

31 of 37 terms resolved to a current term; the rest could not be looked up either way.