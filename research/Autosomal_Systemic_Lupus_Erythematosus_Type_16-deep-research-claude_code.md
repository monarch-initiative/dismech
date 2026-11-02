---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-29T18:37:58.825929'
end_time: '2026-10-29T18:42:37.969569'
duration_seconds: 279.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Systemic Lupus Erythematosus Type 16
  mondo_id: MONDO:0013743
  category: Mendelian
  causal_genes: DNASE1L3
  omim_id: OMIM:614420
  synonyms: systemic lupus erythematosus type 16; SLEB16; systemic lupus erythematosus
    16; systemic lupus erythematosus related to DNASE1L3
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 20
  total_cost_usd: 2.4956809999999994
  session_id: d766227f-70b4-5440-ab6b-6f5a6ed9d934
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 6
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 17
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:35670985
  - PMID:41850754
  relevance_assessed: 21
  on_topic: 21
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 53
  verified: 50
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 4
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Systemic Lupus Erythematosus Type 16
- **MONDO ID:** MONDO:0013743 (if available)
- **Causal gene(s):** DNASE1L3
- **OMIM:** OMIM:614420
- **Synonyms:** systemic lupus erythematosus type 16; SLEB16; systemic lupus erythematosus 16; systemic lupus erythematosus related to DNASE1L3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Systemic Lupus Erythematosus Type 16** covering all of the
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

I'm pulling exact abstract quotes from the cached references to ground the report, then I'll write it up.

# Autosomal Systemic Lupus Erythematosus Type 16 (SLEB16; DNASE1L3 deficiency): research report

**Target:** MONDO:0013743 · OMIM:614420 · causal gene **DNASE1L3** (hgnc:2959) · Mendelian, autosomal recessive

**About the term IDs.** Term IDs marked ✔ are already used and validated in `kb/disorders/Autosomal_Systemic_Lupus_Erythematosus_Type_16.yaml`, or appear in `cache/*/terms.csv`. Every other CURIE here is a **suggestion only**. Look each one up with `runoak` or the term cache before binding it.

**About the quotes.** Quotes come from the abstract or full-text bodies cached under `references_cache/`. Items marked *(web, not cached)* were found by web search and need `just fetch-reference` and a snippet check before anyone cites them.

---

## 1. Disease information

**Overview.** SLEB16 is a monogenic form of systemic lupus erythematosus (SLE). It is caused by **biallelic loss-of-function variants in DNASE1L3**, the gene for a secreted endonuclease (DNase γ) that digests extracellular chromatin. Al-Mayouf et al. (2011) first described it in consanguineous Arab families:

> "We identified a rare autosomal recessive form of SLE, in which autozygome analysis revealed a null mutation in the DNASE1L3 gene. The DNASE1L3-related SLE we describe was always pediatric in onset and correlated with a high frequency of lupus nephritis." — PMID:22019780 (Nat Genet 2011)

**Same gene, wider spectrum.** Hypocomplementemic urticarial vasculitis syndrome (HUVS) was later shown to be caused by the same gene (PMID:23666765). Current literature treats SLEB16 and HUVS as one spectrum, usually called **"DNASE1L3 deficiency"**:

> "DNASE1L3 deficiency was associated with a broad clinical spectrum of immune-mediated disease rather than a single clinicopathological entity." — PMID:42726335

**Identifiers.**
- MONDO:0013743 ✔ "autosomal systemic lupus erythematosus type 16"
- OMIM:614420 (SLEB16)
- Related HUVS phenotype: MONDO / OMIM (HUVS, OMIM:614420 is shared; MONDO HUVS term to verify)
- MeSH D008180 (Lupus Erythematosus, Systemic)
- ICD-10 M32.x; ICD-11 4A40.0 (SLE). There is no gene-specific ICD code.
- Orphanet: covered under monogenic SLE or HUVS. The ORPHA code needs a lookup; `ORPHA:536` is SLE.

**Synonyms.** SLEB16; systemic lupus erythematosus 16; DNASE1L3-related SLE; DNASE1L3 deficiency; DNASE1L3-associated monogenic lupus.

**Data provenance.** The information is almost entirely patient-level: case reports, family series, systematic reviews of individual cases, and one multicentre longitudinal cohort. There are no EHR-scale data.

## 2. Etiology

**Causal factor.** Biallelic loss of DNASE1L3 nuclease activity, either by null variants or by missense variants that impair secretion or activity. Penetrance is described as full:

> "DNASE1L3 deficiency is a rare, fully penetrant autosomal-recessive cause of monogenic SLE and hypocomplementaemic urticarial vasculitis syndrome, typically presenting in early childhood with treatment-refractory disease." — PMID:42716676

**Genetic risk factors.**
- **Consanguinity and autozygosity.** Nearly all reported families are consanguineous (PMID:22019780, PMID:23666765, PMID:34161863).
- **Founder alleles.** Several alleles recur in specific populations (see §9).
- **Common hypomorphic variant rs35677470 (p.Arg206Cys).** This variant is a modest-effect risk allele for *sporadic* SLE, systemic sclerosis and RA. For SLE it reduces secretion while preserving activity, with heterozygous OR ≈ 1.14 and homozygous OR ≈ 1.68. *(ARD 2021;80:782, PMID 33455918, web, not cached.)* For SSc, see PMID 36708011 *(web)*. This variant is **not** causal for SLEB16; it shows the dose-dependent biology of the gene.
- **Acquired phenocopy in sporadic SLE.** Neutralizing anti-DNASE1L3 autoantibodies reduce enzyme activity in many sporadic SLE patients, especially those with nephritis. *(Hartl et al., J Exp Med 2021, PMID 33783474, web, not cached.)*

**Modifiers.** Identical genotypes give discordant phenotypes, which suggests modifiers that have not been identified:

> "The occurrence of identical pathogenic variants across distinct phenotypic and severity states argues against a simple genotype-phenotype model and suggests that additional modifiers influence disease expression." — PMID:42726335

In m

I'll resume from where the report was cut off rather than reproduce what was already printed. Continuing the remaining sections:

## 2. Etiology (continued)

**Environmental factors.** No established environmental trigger. Sun exposure, infection and drugs are discussed for SLE generally; nothing specific to SLEB16 is documented. Disease onset is frequently in infancy, before most candidate exposures accumulate.

**Protective factors.** None documented. Heterozygous carriers are generally unaffected.

**Gene–environment interactions.** Not characterized for this disorder.

## 3. Phenotypes

Frequencies below are from two sources: the 49-patient systematic review (PMID:42726335) and the 57-patient Oman/UAE cohort (PMID:42716676).

**Phenotype distribution (PMID:42726335):** SLE-dominant 27/45 (60%), HUVS-dominant 10/45 (22.2%), overlap 8/45 (17.8%); renal involvement 30/45 (66.7%); onset by age 3 years in 20/45 (44.4%).

**Suggested HP terms** (✔ = already bound in the entry):
- Systemic lupus erythematosus HP:0002725 ✔
- Lupus nephritis HP:0033726 ✔ — 34% rising to 46% on follow-up (PMID:42716676)
- Glomerular immune-complex deposition HP:6000668 ✔
- Proteinuria HP:0000093 ✔; Microscopic hematuria HP:0002907 ✔
- Vasculitis in the skin HP:0200029 ✔ — urticarial rash is often the first sign, from as early as 15 months (PMID:34161863)
- Decreased circulating complement C3 HP:0005421 ✔ and C4 HP:0045042 ✔ — "Persistent hypocomplementemia affecting C3 and C4 was frequently reported across the spectrum" (PMID:42726335)
- Anti-dsDNA antibody positivity HP:0020151 ✔; Antinuclear antibody positivity HP:0003493 ✔ — but both can be **absent**: one compound-heterozygous adult "lacked antinuclear, anti-double-stranded DNA, and anti-Smith antibodies" (PMID:42396794), and the Quebec patient had "negative ANA and anti-dsDNA antibodies" (PMID:40880305)
- Perinuclear ANCA positivity HP:0032229 ✔ — ANCA positivity marks a poor-outcome subgroup (PMID:35670985)
- Arthritis HP:0001369 ✔; Pulmonary hemorrhage HP:0040223 ✔ (6/35 with lung lesions, PMID:35670985); Autoimmune hemolytic anemia HP:0001890 ✔; Recurrent fever HP:0001954 ✔
- Candidates to verify and add: Episcleritis (HP:0100534?), Abdominal pain (HP:0002027), Osteoporosis (HP:0000939) — 23% → 41% on follow-up, largely glucocorticoid-related (PMID:42716676); Inflammatory bowel disease-like colitis (PMID:35670985); Renal insufficiency / Stage 5 chronic kidney disease (HP:0003774 / HP:0003774 + dialysis dependence, PMID:40880305, PMID:39059688)

**Onset.** Median age at onset 24 months in the 100-patient monogenic-lupus cohort where DNASE1L3 accounted for 25% (PMID:41850754); median age at diagnosis 5 years (IQR 1.75–13) in the Oman/UAE cohort (PMID:42716676).

**Severity and course.** Treatment-refractory, relapsing, with cumulative damage. The key longitudinal finding is a dissociation between activity and damage:

> "Despite a significant reduction in disease activity (SLE Disease Activity Index scores) over the follow-up period (9 vs 4; p<0.001), this was not accompanied by clear improvement in long-term outcomes." — PMID:42716676

**Quality of life.** No EQ-5D/SF-36/PROMIS data specific to this disorder. Proxies in the literature are SLEDAI, the SLICC/ACR Damage Index, Physician/Parent Global Assessment, and a Paediatric Systemic Disease Index median of 3 (PMID:41850754). Dialysis dependence, osteoporosis and glucocorticoid burden are the documented drivers of functional impact.

## 4. Genetic / molecular information

**Gene.** DNASE1L3 (hgnc:2959 ✔), chromosome 3p14.3, OMIM *602244. Protein: DNase γ / DNase Y / LS-DNase, a secreted DNASE1-family endonuclease (UniProt Q13609).

**Reported variants** (all germline, biallelic):
- `c.643delT` (p.Val215fs) — the dominant allele in the Oman/UAE cohort: "most carrying the homozygous DNASE1L3 c.643delT loss of function variant" (PMID:42716676). This is the original Nat Genet null allele.
- `c.289_290delAC` / `c.290_291delCA` (p.Thr97Ilefs*2) — recurrent frameshift, reported in HUVS families (PMID:23666765), an Italian family (PMID:27821515), a Turkish patient (PMID:34161863), and in compound heterozygosity (PMID:42396794). Note the two cDNA spellings in the literature refer to the same allele.
- `c.320+4delAGTA` — splice variant causing exon skipping (PMID:23666765)
- `c.572A>G` (p.Asn191Ser) — recurrent missense in Emirati families; impairs secretion and activity (PMID:39947743)
- `c.179T>G` (p.Ile60Ser) — novel missense with residual activity (PMID:42396794)
- rs35677470 (p.Arg206Cys) — common hypomorph, risk allele not a cause (§2)

**Functional consequence: loss of function**, by two routes. Nulls abolish protein; missense alleles impair secretion while retaining partial catalysis:

> "The variant 191S was shown to impact the secretion and activity of DNASE1L3." — PMID:39947743

> "Functional testing showed markedly impaired DNA degradation for both variants, with residual activity in the missense mutant." — PMID:42396794

> "The detected mutations led to loss of function, via either nonsense-mediated messenger RNA decay or abolished endonuclease activity, as demonstrated by a plasmid nicking assay." — PMID:23666765

**Genotype–phenotype.** None established — the same allele spans organ-limited vasculitis through severe multisystem lupus (PMID:42726335, quoted in §2).

**Allele frequency.** Causal alleles are absent or ultra-rare in gnomAD; rs35677470 is common (minor allele frequency in the low percent range, higher in Europeans). Verify current gnomAD numbers before curating any figure.

**Epigenetics, chromosomal abnormalities.** No disease-specific findings. Not applicable.

## 5. Environmental information

No established environmental, lifestyle or infectious contributor. Worth recording as explicitly searched rather than absent: recurrent/refractory warts developed in one immunosuppressed patient (PMID:40880305), which is treatment-related infection risk rather than an etiologic exposure. The ECTO binding question therefore does not arise for this entry.

## 6. Mechanism / pathophysiology

### Causal chain

1. Biallelic loss-of-function variants in **DNASE1L3** lead to absent or markedly reduced secreted DNASE1L3 nuclease activity in plasma (PMID:23666765, PMID:39947743, PMID:42396794).
2. Loss of that activity **results in** failure to digest chromatin on apoptotic-cell-derived microparticles — the enzyme's unique substrate: "DNASE1L3 is uniquely capable of digesting chromatin in microparticles released from apoptotic cells" (PMID:27293190).
3. Undigested chromatin **leads to** accumulation of extracellular self-DNA, measurable as altered plasma DNA fragmentation: "DNASE1L3-deficient mice and human patients have elevated DNA levels in plasma, particularly in circulating microparticles" (PMID:27293190); "patients with DNASE1L3 disease-associated gene variations showed aberrations in size and a reduction of a 'CC' end motif of plasma DNA" (PMID:33022220).
4. Microparticle-bound chromatin acts as a self-antigen, which **results in** activation of DNA-reactive B cells: "extracellular microparticle-associated chromatin is a potential self-antigen normally digested by circulating DNASE1L3" (PMID:27293190).
5. That activation **proceeds via** CD40L-dependent, germinal-center-independent **extrafollicular** differentiation into short-lived antibody-forming cells, requiring endosomal TLR9/TLR7 sensing and type I IFN from plasmacytoid dendritic cells (mouse; PMID:32454024).
6. **Branch A — autoantibody/immune-complex arm.** Class-switched anti-dsDNA antibodies form immune complexes, which **lead to** glomerular and dermal deposition, complement consumption (low C3/C4) and immune-complex glomerulonephritis (PMID:34161863, PMID:42726335, PMID:40880305).
7. **Branch B — type I IFN arm.** Nucleic-acid sensing drives interferon-stimulated gene expression and MxA protein in glomerular endothelium (PMID:39059688). Unlike the canonical interferonopathies, the signal is **transient**: "we noticed a transient increase of ISGs in blood, which returned to normal with disease remission… contrary to anomalies of intracellular DNA sensing and signaling observed in Aicardi-Goutières syndrome or STING-associated vasculitis in infancy (SAVI)" (PMID:35670985).
8. **Branch C — NET arm.** DNASE1L3 also degrades neutrophil extracellular traps; its loss **results in** increased NET burden: "Patients homozygous for 191S variant had significantly higher burden (p=0.0409) of NET structure in comparison to heterozygous and healthy control" (PMID:39947743). This branch is the rationale for NET-degrading replacement therapy (§12).
9. Sustained immune-complex deposition and inflammation **lead to** irreversible organ damage — glomerulosclerosis, interstitial fibrosis, kidney failure, alveolar hemorrhage (PMID:40880305, PMID:39059688) — which accrues even when activity scores fall (PMID:42716676).

Branch ordering: steps 1–4 are upstream and demonstrated in both human and mouse; step 5 is **mouse-only** and is an inference for human disease; branches A and B are human-demonstrated; branch C is human-demonstrated at the biomarker level, with its causal weight for organ injury still inferred.

**Protein function (review-level framing, PMID:42726335):**
> "DNASE1L3 uniquely binds and degrades chromatin as well as protein- or lipid-complexed DNA, efficiently digesting nucleosomal DNA, DNA within immune complexes, and membrane-bound DNA released during apoptosis."

The same source notes functions beyond DNA clearance — inflammasome-dependent IL-1 release and NET degradation — which have not been dissected in patients.

**Suggested terms.** Already bound ✔: GO:0033891 CC-preferring endodeoxyribonuclease activity; GO:0006308 DNA catabolic process; GO:0042113 B cell activation; GO:0032481 positive regulation of type I interferon production; GO:0002434 immune complex clearance; GO:0006958 complement activation, classical pathway. Cells ✔: CL:0000235 macrophage, CL:0000451 dendritic cell (the sources of circulating enzyme — "Circulating DNASE1L3 is produced by dendritic cells and macrophages", PMID:27293190), CL:0000236 B cell, CL:0000786 plasma cell, CL:0000784 plasmacytoid dendritic cell. Candidates to verify: neutrophil CL:0000775 (NET branch), glomerular endothelial cell CL:1001005, podocyte CL:0000653; GO terms for NET formation/disassembly, TLR9 signaling, type I interferon-mediated signaling pathway (GO:0060337).

**Molecular profiling.** Plasma **fragmentomics** is the distinctive assay: shortened mononucleosomal peak, excess long fragments, loss of CC end motifs (PMID:33022220, PMID:42396794, PMID:40880305). Blood ISG scores are the IFN readout (PMID:35670985, PMID:39059688). No disease-specific transcriptomic, proteomic, metabolomic, lipidomic or single-cell datasets were identified; for `datasets:` curation, run `just discover-datasets` rather than assuming GEO coverage.

## 7. Anatomical structures affected

- **Kidney** (UBERON:0002113) — the dominant organ: lupus nephritis across the membranous, endocapillary, extracapillary and thrombotic-microangiopathy patterns, "all belonging to the lupus nephritis (LN) spectrum" (PMID:39059688). Bilateral.
- **Skin** (UBERON:0002097) — urticarial rash with dermal vasculitis; the earliest manifestation in many patients.
- **Lung** (UBERON:0002048) — diffuse alveolar hemorrhage, ground-glass opacities (PMID:40880305, PMID:34161863).
- **Joints** (UBERON:0000982 synovial joint) — arthritis, polyarthritis.
- **Blood and immune system** — hemolytic anemia, hypocomplementemia; spleen/lymph node involvement not specifically characterized.
- **Eye** (UBERON:0000970) — episcleritis (PMID:42396794).
- **Gastrointestinal tract** (UBERON:0001555) — early-onset IBD in one patient (PMID:35670985); intestinal angioedema and recurrent abdominal pain in another (PMID:42396794).
- **Upper airway** — nasal septum ulceration in the ANCA-overlap patient (PMID:40880305).
- **Bone** — osteoporosis accruing over follow-up (PMID:42716676), largely iatrogenic.
- **Subcellular / extracellular.** The relevant compartment is **extracellular space** (GO:0005615 extracellular space / GO:0005576 extracellular region) — unusually for a monogenic lupus, the lesion is in plasma, not in a cell. Secretory pathway (ER/Golgi) matters for the secretion-impaired missense alleles.
- **Histopathology.** Immune-complex glomerulonephritis with IgG and C3 glomerular fixation, intramembranous electron-dense deposits, and on chronic biopsies advanced glomerulosclerosis with diffuse interstitial fibrosis (PMID:40880305). MxA immunostaining in glomerular endothelium (PMID:39059688).

## 8. Temporal development

- **Onset.** Pediatric, often infantile; insidious, usually beginning with urticarial rash. Median onset 24 months (PMID:41850754); onset by age 3 in 44.4% (PMID:42726335). Adult presentation occurs but is rare (PMID:42396794 — a 24-year-old with lifelong symptoms, i.e. late diagnosis rather than late onset).
- **Course.** Chronic, lifelong, relapsing–remitting with flares, and refractory to conventional therapy. Renal involvement tends to appear or worsen over time (34% → 46%), as does pulmonary involvement (3.7% → 11%) (PMID:42716676).
- **Critical period.** The intervention window implied by PMID:42716676 is before damage accrues, because falling activity scores do not stop it:
  > "reduction in clinical disease activity does not prevent progressive organ damage… apparent disease quiescence may mask ongoing subclinical injury, underscoring the need for sustained long-term surveillance and optimised transitional care strategies."
- **Remission.** Treatment-induced partial remission is achievable; ISG normalization accompanies remission (PMID:35670985). Spontaneous remission is not described.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007 ✔), fully penetrant (PMID:42716676). No anticipation, no reported germline mosaicism.
- **Expressivity.** Highly variable, including within one genotype (PMID:42726335).
- **Prevalence.** No population estimate exists. The disorder is ultra-rare; roughly 100 genetically confirmed patients are in the literature, and the cohorts overlap — 49 unique individuals in the systematic review (PMID:42726335), 57 in the Oman/UAE cohort (PMID:42716676), with probable shared families. For the `prevalence:` block, `prevalence_class: NOT_YET_DOCUMENTED` or `ULTRA_RARE` with `measure_type: CASES_IN_LITERATURE` is the honest encoding; do not derive a rate.
- **Share of monogenic lupus.** DNASE1L3 is one of the two commonest causes: "The most frequently implicated genes were C1Q (26%) and DNASE1L3 (25%)" (PMID:41850754).
- **Founder effects and geography.** Reported clusters: Arabian Peninsula (Saudi Arabia, Oman, UAE — c.643delT and p.Asn191Ser), Turkey, Italy, Syria (PMID:42601766), Slovenia/Bosnia (PMID:35670985), and a First Nations family in Quebec (PMID:40880305). "Distinct ethnic clustering of specific gene mutations was observed" (PMID:41850754). Consanguinity is the principal driver.
- **Sex ratio.** Unlike sporadic SLE, female predominance is attenuated: "monogenic lupus exhibits reduced female predominance" (PMID:41850754, a BACKGROUND-section statement — grade `quote_role: BACKGROUND`). No reliable sex ratio specific to DNASE1L3 was found.
- **Carrier frequency.** Not established; expected to be appreciable within specific consanguineous kindreds only.

## 10. Diagnostics

**Laboratory.** ANA, anti-dsDNA, ANCA/anti-MPO, C3, C4, CBC with hemolysis markers, urinalysis with protein/creatinine ratio, serum creatinine. Serum **DNase activity** is reduced — "all 3 patients had reduced serum DNAse activity" (PMID:39059688) — and is a direct functional test. LOINC codes for C3, C4, ANA, anti-dsDNA and creatinine are the candidates for `diagnosis[].measurements`; none is specific to this disease, and each must be read out of `cache/loinc/terms.csv` or seeded, never typed from memory.

**Fragmentomics as a biomarker.** This is the one assay unique to the disorder:
> "Plasma DNA fragment analysis provides a sensitive biomarker of impaired nuclease function" — PMID:42396794

**IFN signature.** Blood ISG expression, with the caveat that it is transient and normalizes in remission (PMID:35670985) — so a normal ISG score does not exclude the diagnosis.

**Biopsy.** Renal biopsy with immunofluorescence and electron microscopy establishes the immune-complex glomerulonephritis and its LN class; skin biopsy shows leukocytoclastic/dermal vasculitis.

**Imaging.** Chest CT for alveolar hemorrhage (PMID:40880305).

**Genetic testing.** WES is the route taken in essentially every published case (PMID:22019780 autozygosity mapping + sequencing; PMID:23666765 autozygosity mapping with WES; PMID:34161863, PMID:39947743, PMID:42396794 WES with Sanger confirmation). Single-gene DNASE1L3 testing is reasonable with a classic presentation; a monogenic-lupus gene panel is the pragmatic first line. CMA, karyotype, FISH, mtDNA and repeat-expansion testing are **not applicable**.

**When to suspect it** — the clinical trigger stated in the literature:
> "DNASE1L3 deficiency should be thought when juvenile SLE occurs with early disease-onset, pulmonary hemorrhage, glomerulonephritis, and recurrent urticarial rash along with ANCA positivity." — PMID:34161863

**Clinical criteria.** Patients are classified by the standard EULAR/ACR SLE criteria or by HUVS criteria (urticaria + hypocomplementemia + dermal vasculitis). Neither identifies the gene; and seronegative patients may fail SLE criteria altogether (PMID:42396794, PMID:40880305).

**Differential diagnosis.** Sporadic childhood-onset SLE; other monogenic lupus (C1Q, C1R/C1S, DNASE1, TREX1, ACP5, PRKCD, NRAS, SAMHD1); ANCA-associated vasculitis (the overlap is real, not just a mimic — PMID:40880305, PMID:35670985); type I interferonopathies (Aicardi-Goutières, SAVI), distinguished by the *transient* rather than sustained ISG elevation (PMID:35670985); acquired HUVS; acquired anti-DNASE1L3 autoantibody-mediated enzyme loss in sporadic SLE *(PMID 33783474, web)*.

**Screening.** Cascade genetic testing of siblings in affected consanguineous families is the only meaningful screening. No newborn or population screening exists.

## 11. Outcome / prognosis

- **Mortality.** 8.8% in pediatric follow-up rising to 13.5% after transition (p=0.125) in the largest cohort (PMID:42716676); 16% in the broader monogenic-lupus cohort (PMID:41850754).
- **Renal outcome.** The dominant driver of morbidity: refractory glomerulonephritis leading to kidney failure and dialysis dependence (PMID:39059688, PMID:40880305).
- **Damage accrual.** SLICC/ACR Damage Index rose from 0.37±0.85 to 0.72±1.17 (p=0.295) — numerically, not significantly — alongside significantly *improving* activity scores (PMID:42716676). This discordance is the single most important prognostic statement in the literature and should be curated as such.
- **Complications.** Kidney failure, alveolar hemorrhage, osteoporosis (23% → 41%), serious infection under immunosuppression, cardiopulmonary complications, refractory warts.
- **Prognostic factors.** ANCA positivity marks a poorer-outcome group: PMID:35670985 associates DNASE1L3 deficiency with "a significant risk of lupus nephritis and a poor outcome together with the presence of anti-neutrophil cytoplasmic antibodies (ANCA)." Early onset and renal involvement are the other adverse markers. No validated prognostic model exists.
- **Caveat the cohort itself states.** "the findings should be interpreted with caution in light of the small sample size in this ultra-rare disease" (PMID:42716676).

## 12. Treatment

**Conventional.** Glucocorticoids, hydroxychloroquine (CHEBI:5801 ✔), mycophenolate mofetil (CHEBI:8764 ✔), azathioprine, cyclophosphamide, rituximab, obinutuzumab, plasma exchange, hemodialysis, with renal transplantation considered (PMID:40880305). Disease is characteristically refractory: "All had persistent disease activity despite multiple conventional and biologic therapies" (PMID:42100058). NCIT:C15261 Immunosuppressive Therapy ✔.

**JAK inhibition** is the best-supported targeted approach, following from the IFN arm of the mechanism. Baricitinib (CHEBI:95341 ✔), NCIT:C15986 Pharmacotherapy ✔:
> "By six months, all patients showed improved disease activity, with SLEDAI scores decreasing from 14.2 to 4.1 by day 90 and remaining stable, PGA improving from 5.8 to 2.5 by day 180, and reduced daily GC doses." — PMID:42100058

Note the cohort mixes genotypes (C1q, DNase1L3, PRKCD, NRAS), so the DNASE1L3-specific effect is not isolated; grade the evidence accordingly. Partial response is also reported in a single DNASE1L3 patient: "The disease was refractory to multiple immunosuppressive agents but showed partial improvement with JAK inhibition" (PMID:42396794). PMID:39059688 argues the same case mechanistically — MxA in glomerular endothelium "provide[s] the rationale for IFN-I-directed therapies."

**Enzyme replacement — the mechanism-directed therapy.** Two threads, both needing verification before curation:
- **Preclinical gene delivery.** AAV-based Dnase1l3 transduction normalized the plasma DNA end-motif profile in deficient mice (PMID:33022220): "Adeno-associated virus-based transduction of Dnase1l3 into Dnase1l3-deficient mice restored the end motif profiles to those seen in the plasma DNA of wild-type mice." This is a biomarker correction in a mouse, not a clinical outcome.
- **NTR-441**, a recombinant DNASE1L3 analogue (Neutrolis). A phase 1 study in healthy volunteers and COVID-19 patients (NCT04941183) and a single compassionate-use case in a 16.5-year-old with DNASE1L3-deficient refractory SLE, reported as published in NEJM in July 2026, with rapid multi-organ improvement and later loss of response attributed to anti-drug antibodies. A next-generation albumin-fused analogue (NTR-1011) with planned phase 2a trials in SLE and RA is announced. **All of this is from company press releases and conference abstracts** *(web, not cached)*. Fetch the NEJM paper and NCT04941183 with `just fetch-reference` before any of it enters the KB; a press release is not a citable source here.

**Modality encoding.** For the entry: conventional agents are `SMALL_MOLECULE` or `MONOCLONAL_ANTIBODY`; baricitinib `SMALL_MOLECULE`; a recombinant DNASE1L3 analogue is `PROTEIN_REPLACEMENT`; AAV-Dnase1l3 is `GENE_THERAPY` and belongs under `animal_models`/`computational_models` framing, not as a human treatment.

**Pharmacogenomics.** Nothing disease-specific. Standard TPMT/NUDT15 genotyping applies before azathioprine, per general CPIC guidance rather than any DNASE1L3 literature.

**Adverse events.** Glucocorticoid toxicity (osteoporosis 41% at follow-up, PMID:42716676), infection risk under immunosuppression, MMF enteropathy (PMID:40880305), anti-drug antibodies to recombinant enzyme *(web)*. Baricitinib was tolerated with "no serious infections or adverse events reported" in the seven-patient series (PMID:42100058).

## 13. Prevention

- **Primary.** Not preventable. Genetic counseling for consanguineous families, carrier testing of at-risk relatives, and reproductive options (prenatal diagnosis, preimplantation genetic testing) are the only primary measures. NCIT:C15240 Genetic Counseling.
- **Secondary.** Cascade genetic testing of siblings, then surveillance of asymptomatic homozygotes for proteinuria and complement levels, to catch nephritis before damage.
- **Tertiary** — this is where the literature is most pointed. Because activity scores understate ongoing injury (PMID:42716676), the preventive intervention is sustained surveillance (urinalysis, renal function, complement, imaging for pulmonary involvement), bone protection against glucocorticoid-induced osteoporosis, infection prophylaxis and vaccination under immunosuppression, and structured transition to adult care.
- **Immunization.** No disease-specific vaccine. Standard immunosuppression-related vaccination practice applies; live vaccines are contraindicated under most of these regimens.
- **Public health / environmental.** Not applicable beyond consanguinity education where culturally appropriate.

## 14. Other species / natural disease

- **Mouse** (NCBITaxon:10090), *Dnase1l3* — the principal model; see §15.
- No naturally occurring DNASE1L3-deficiency disease is documented in companion animals or wildlife; OMIA holds no corresponding entry that I could identify. No breed association, so no VBO term.
- **Comparative biology.** The mechanism is conserved: deficient mice reproduce the human biology closely — "DNASE1L3-deficient mice rapidly develop autoantibodies to DNA and chromatin, followed by an SLE-like disease" and "DNASE1L3-deficient mice and human patients have elevated DNA levels in plasma" (PMID:27293190). The plasma-DNA fragmentation phenotype is conserved across both species (PMID:33022220).
- **Transmission / zoonosis.** Not applicable — Mendelian autoimmune disease.

## 15. Model organisms

**Dnase1l3-knockout mouse** — the workhorse model, and unusually faithful.

*Phenotype recapitulation (PMID:27293190, in vivo):* rapid anti-DNA and anti-chromatin autoantibodies, SLE-like disease, elevated plasma and microparticle DNA. The paper also establishes the inverse relationship between circulating enzyme and autoantibody: "Circulating DNASE1L3 is produced by dendritic cells and macrophages, and its levels inversely correlate with anti-DNA antibody response."

*Mechanistic dissection the model enabled (PMID:32454024, in vivo + in vitro):* the extrafollicular pathway, its CD40L dependence, pDC/IFN-I requirement, and redundant TLR9/TLR7 sensing — "anti-DNA responses in Dnase1l3-/- mice require CD40L-mediated T cell help, but proceed independently of germinal center formation via short-lived antibody-forming cells (AFCs) localized to extrafollicular regions."

*Correction experiments (PMID:33022220):* AAV-Dnase1l3 restored wild-type plasma DNA end-motif profiles, establishing that the fragmentation defect is cell-extrinsic and reversible — "DNASE1L3 is an important player in the fragmentation of plasma DNA, which appears to act in a cell-extrinsic manner."

*Limitations to record in `modeled_mechanisms[].limitations`:* the mouse does not reproduce the human urticarial-vasculitis/HUVS arm or ANCA positivity; the human ISG elevation is transient whereas mouse IFN dependence is studied under sustained conditions; alveolar hemorrhage, IBD and the renal histologic diversity of human disease are not captured; and the AAV result is a biomarker correction, not a disease-outcome rescue. For `model_scale`, the fragmentomics and autoantibody readouts are `MOLECULAR`, so links to tissue-level nodes (glomerulonephritis, alveolar hemorrhage) are upward extrapolations and need a caveat.

**Cellular / in vitro systems.** HEK293 transfection assays for variant secretion and activity (PMID:39947743); enzymatic assays on cell lysates and supernatants plus plasma cfDNA fragmentation (PMID:42396794); plasmid nicking assay (PMID:23666765); plasma smear NET assay in patients and relatives (PMID:39947743). These are `experimental_models` with `IN_VITRO` evidence, and they are the standard route to variant pathogenicity for this gene.

**Resources.** MGI (*Dnase1l3*, MGI symbol to look up), IMPC, IMSR for available knockout lines. No zebrafish, Drosophila or C. elegans model of this disorder was identified — the gene family and the extracellular-chromatin biology make those poor fits.

---

## Notes for whoever curates from this

Three things in this report need handling before they reach YAML:

1. **The NTR-441 / NEJM material is press-release sourced.** It is the most interesting therapeutic development for this disease and it is also the least verified thing here. Fetch the NEJM paper and NCT04941183 first; if the paper does not resolve, leave it out rather than citing a company announcement.
2. **Three PMIDs cited above are web-only** — 33783474 (Hartl, anti-DNASE1L3 autoantibodies), 33455918 (ARD rs35677470), 36708011 (SSc R206C). Each needs `just fetch-reference` and a snippet check. I have not verified the identifier-to-title binding for any of them against the cache.
3. **The cohort figures overlap.** PMID:42726335 (49 patients) and PMID:42716676 (57 patients) share families, and PMID:35670985's systematic review feeds both. Do not add their denominators together, and say which source any frequency came from.

Sources for the web-only items: [Hartl et al., J Exp Med 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8020718), [ARD 2021;80:782](https://ard.bmj.com/content/80/6/782), [Neutrolis NEJM announcement](https://www.biospace.com/press-releases/neutrolis-announces-new-england-journal-of-medicine-publication-demonstrating-first-clinical-evidence-for-net-degrading-therapy-in-severe-treatment-refractory-systemic-lupus-erythematosus-sle-caused-by-dnase1l3-deficiency), [Neutrolis ACR 2025 data](https://www.biospace.com/press-releases/neutrolis-presented-first-in-human-proof-of-concept-data-validating-dnase1l3-mediated-neutrophil-extracellular-trap-net-clearance-as-a-therapeutic-approach-in-autoimmunity-at-american-college-of-rheumatology-convergence-2025), [ACR abstract](https://acrabstracts.org/?p=46409), [SNPedia rs35677470](https://www.snpedia.com/index.php/Rs35677470).

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 21 |
| On topic | 21 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35670985` *(abstract only)*: "we noticed a transient increase of ISGs in blood, which returned to normal with disease remission… contrary to anomalies of intracellular DNA sensing and signaling observed in Aicardi-Goutières syndrome or STING-associated vasculitis in infancy (SAVI)"
  - closest text in source: "This report shows that interferon production is transient contrary to anomalies of intracellular DNA sensing and signaling observed in Aicardi-Goutières syndrome or STING-associated vasculitis in infancy (SAVI)."
- `PMID:41850754`: "monogenic lupus exhibits reduced female predominance"
  - closest text in source: "A total of 100 patients with genetically confirmed monogenic lupus were included; 63% were female"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000775` (1 mention) - the report calls it "NET branch"; CL calls it **neutrophil**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0001555` (1 mention) - the report calls it "Gastrointestinal tract"; UBERON calls it **digestive tract**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.

50 of 53 terms resolved to a current term; the rest could not be looked up either way.