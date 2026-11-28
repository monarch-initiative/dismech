---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-28T01:03:01.755521'
end_time: '2026-11-28T01:08:36.799654'
duration_seconds: 335.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spinal Tuberculosis
  mondo_id: MONDO:0043836
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: tuberculosis of vertebral column; pott disease; pott's disease
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
  web_search_requests: 4
  num_turns: 15
  total_cost_usd: 0.9813739749999999
  session_id: 1046ff12-2285-4358-917f-b494060a1d6a
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 53
  retrieval_calls: 49
  assistant_text_blocks: 4
citation_count: 10
reference_validation:
  total_references: 56
  verified: 56
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 19
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:41232750
  - PMID:37304201
  - PMC:PMC9955044
  relevance_assessed: 56
  on_topic: 42
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0043836
    reported_labels:
    - research report for a disease knowledge base
    ontology_label: tuberculosis, spinal
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinal Tuberculosis
- **MONDO ID:** MONDO:0043836 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** tuberculosis of vertebral column; pott disease; pott's disease
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spinal Tuberculosis** covering all of the
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

I'm collecting sources, PubMed IDs (PMIDs) and abstract quotes. Next I'll fetch PubMed records to check them.

PubMed's web pages are blocked, so I'm switching to Europe PMC's API to get the abstracts.

I have most sections covered. One more round to fill gaps: clinical-feature frequencies, MRI features, and identifiers.

# Spinal tuberculosis (Pott disease), MONDO:0043836: research report for a disease knowledge base

**Scope.** This report covers MONDO:0043836, "tuberculosis, spinal", described in MONDO as "Tuberculosis of the vertebrae." **Causal gene:** none. This is an infectious disease caused by the *Mycobacterium tuberculosis* complex, and no human Mendelian causal gene is recorded. The template's gene and variant sections are answered as "not applicable", and host susceptibility polymorphisms are reported in their place.

**Sources and their limits.**
- PubMed's web interface and E-utilities could not be reached from this environment. Abstracts were taken from the Europe PMC REST API, and identifiers from MeSH and EBI OLS.
- Quotes are verbatim abstract fragments as returned. Some were shortened by the retrieval tool, and they should be re-checked against PubMed before deposit.
- Ontology IDs other than MONDO:0043836 and MeSH D014399 were **not retrieved** in this session. Terms are therefore given as labels only, and their IDs need to be looked up.

---

## 1. Disease Information

**Overview.** Spinal TB is "a destructive form of tuberculosis" that "accounts for approximately half of all cases of musculoskeletal tuberculosis" (Garg & Somvanshi 2011, PMID 22118251). "The spinal column is involved in less than 1% of all cases of tuberculosis (TB)." It is "a very dangerous type of skeletal TB as it can be associated with neurologic deficit" (Rasouli et al. 2012, PMID 23275816).

**Identifiers retrieved**

| Resource | ID / label | Source |
|---|---|---|
| MONDO | MONDO:0043836 "tuberculosis, spinal" | EBI OLS (https://www.ebi.ac.uk/ols4) |
| MeSH | D014399 "Tuberculosis, Spinal" | https://meshb.nlm.nih.gov/record/ui?ui=D014399 |

- **MeSH tree numbers:** C01.150.252.410.040.552.846.617.525.722; C01.160.886.722; C05.116.165.886.722; C05.116.900.853.850.
- **MeSH scope note:** "Osteitis or caries of the vertebrae, usually occurring as a complication of tuberculosis of the lungs."
- **MeSH entry terms:** Pott Disease; Pott's Disease. Pott's Paraplegia is a narrower concept.
- **MeSH annotation:** do not confuse Pott disease with Pott Puffy Tumor (D059369).
- **Not retrieved:** OMIM (there is no OMIM disease entry for this infection), Orphanet, ICD-10 and ICD-11 codes. These must be added from the source databases.

**Synonyms.** MONDO exact synonyms are tuberculosis of vertebral column, pott disease and pott's disease. MONDO related synonyms are Potts disease, pott's paraplegia and spinal tuberculosis. Clinical literature also uses tuberculous spondylitis (PMIDs 42550235, 41081173) and the abbreviation STB.

**Data provenance.** The evidence comes from aggregated disease-level literature: reviews, cohort series, randomised trials and meta-analyses. None of it is individual EHR data.

## 2. Etiology

### Causal factors
- **Infection by the *M. tuberculosis* complex.** In one genotyped series from south-central China, "Of the 56, cases, 53 involved M. tuberculosis and 3 involved M. bovis" (Liu et al. 2020, PMID 32076625).
- **Iatrogenic *M. bovis* BCG.** Vertebral osteomyelitis can follow intravesical BCG therapy for bladder cancer (Mackel et al. 2016, PMID 27158574).
- **Spread from a primary focus.** MeSH describes the disease as "usually occurring as a complication of tuberculosis of the lungs." A 2025 series found that parenchymal spinal TB "is more frequently associated with haematogenous pulmonary dissemination" (Shan et al. 2025, PMID 40211169).

### Risk factors
**Host genetic susceptibility.** All of these are case-control studies in Chinese Han populations and none has been replicated:

| Gene / variant | Finding | PMID |
|---|---|---|
| *SLC11A1* (NRAMP1) rs17235409 | 227 STB patients vs 516 controls. "the presence of the A allele increases the risk of developing STB" | 34990850 |
| *MBL2* −221G>C, *CD14* −159C>T, *TNF* −857 | 240 patients. These "are risk factors" | 29298876 |
| *MMP1* −1607 1G/2G | OR 2.084 (95% CI 1.401–3.100) for 1G/1G+1G/2G vs 2G/2G | 28129430 |
| *VDR* FokI | OR 2.176 (95% CI 1.236–3.832); ff genotype 46.36% | 20430254 |

The *MMP1* and *VDR* figures come from a summary of the record, not a verbatim quote. Other studies were seen by title only and not read: *P2X7* (PMID 29158203) and *IL17A* rs2275913 (PMID 41794165).

**Clinical and environmental risk factors.**
- A review states that "Research has implicated the risk factors for the susceptibility and severity of Pott's disease" (Glassman et al. 2023, PMID 36826156). Its specific factors were not retrieved.
- HIV co-infection is studied in South Africa. Spinal biopsies show *Mtb*–HIV-1 co-localisation and "reciprocal expansion" (Waters et al. 2026, PMID 41232750), and a separate series covered HIV in 52 spinal TB patients (Scherer et al. 2024, PMID 39514752; title only).
- Quantitative data on diabetes, age and other host factors for spinal TB specifically were not retrieved.

### Protective factors
No spinal-TB-specific protective genetic or environmental factors were retrieved.

### Gene–environment interactions
No studies were retrieved. The polymorphisms above act only in the presence of *Mtb* exposure, but this has not been formally tested for spinal TB.

## 3. Phenotypes

The retrieved abstracts give few pooled frequencies. Values below are from individual series.

| Phenotype | HPO label (ID not retrieved) | Frequency / notes | Source |
|---|---|---|---|
| Back pain (often chronic, insidious) | Back pain; Low back pain | Common presenting feature | PMID 37304201; case series PMID 42488243 |
| Constitutional symptoms (fever, weight loss) | Fever; Weight loss | "Constitutional symptoms" listed as common | Reviews: https://pmc.ncbi.nlm.nih.gov/articles/3184481 |
| Spinal tenderness | — | Common | same |
| Paraparesis / paraplegia ("Pott's paraplegia") | Paraparesis; Paraplegia | 45.6% (52 cases) in a 10-year Central India series; tetraplegia 1.7% | DOAJ eda1dcccd90b411683025dcf0ad4ffb2 |
| Neurological deficit at presentation | — | 200/312 (≈64%) in Sharma et al., Spinal Cord 2016 | https://www.nature.com/articles/sc201685 |
| Sensory deficit | — | 10.5% | Central India series |
| Bowel/bladder dysfunction | Urinary incontinence; Neurogenic bladder | 4.4% | Central India series |
| Kyphotic deformity (gibbus) | Kyphosis; Angular kyphosis | Major sequela; surgical correction of angle from 66.6° to 34.5° in revision cases | PMID 37083590; PMID 38632071 |
| Paravertebral / psoas / epidural abscess | Abscess | 2 of 6 in a lumbosacral series | PMID 42488243 |
| Radiculopathy | Radiculopathy | Lumbosacral disease | PMID 42488243 |
| Vertebral body destruction and collapse | Vertebral collapse | An independent MRI discriminator vs pyogenic infection (OR 3.713) | PMID 42477203 |

- **Onset:** insidious. "Substantial delay in diagnosis continues to be common" (PMID 32154388).
- **Severity:** variable, ranging from mild symptoms to complete paraplegia.
- **Progression:** progressive without treatment.
- **Quality of life:** the main effects come from pain, neurological deficit and deformity. No validated spinal-TB QoL instrument data (EQ-5D or SF-36) were retrieved. One case report stresses the role of physical and rehabilitation medicine in elderly patients (PMID 36817719).

## 4. Genetic/Molecular Information

- **Causal genes, pathogenic variants (ACMG), allele frequencies, somatic origin, chromosomal abnormalities:** not applicable to this infectious disease.
- **Host susceptibility loci:** see §2. HGNC symbols are SLC11A1, MBL2, CD14, TNF, MMP1, VDR, P2RX7 and IL17A. Their HGNC IDs were not retrieved.
- **Pathogen genomics:**
  - Beijing-lineage strains: "the resistance rate of the Beijing type was higher than that of the nonBeijing type" (PMID 32076625).
  - Whole-genome sequencing: "We could not confirm any genomic difference between pulmonary and spinal TB strains" (Ngcelwane et al. 2023, PMID 37194130).
- **Epigenetics:** no data retrieved.

## 5. Environmental Information

- **Infectious agents:** *Mycobacterium tuberculosis* (most cases), *M. bovis* (minority; PMID 32076625), and *M. bovis* BCG (iatrogenic; PMID 27158574). NCBI Taxon IDs were not retrieved.
- **Drug resistance:**
  - A 6.5% drug-resistance rate, "showing annual escalation", was reported among 893 patients in East China (Cao et al. 2025, PMID 40890663).
  - A review of drug-resistant spinal TB exists (PMID 32904104; title only).
- **Lifestyle, toxins, occupation:** no spinal-specific data retrieved.

## 6. Mechanism / Pathophysiology

**Causal chain.** Steps 1–2 and 5–8 rest on the retrieved sources. Step 3 is inferred from general TB biology and was not retrieved here, and step 4 is supported only by early single-cell data.

1. Inhaled *M. tuberculosis* (or another complex member) establishes a primary focus, usually pulmonary. This **leads to** haematogenous dissemination. *Supported by the MeSH scope note and PMID 40211169.*
2. Bacilli seed the vertebral body, which **results in** vertebral osteomyelitis. Biopsy "from the affected site in the center of the vertebral body" is the diagnostic standard (PMID 22118251).
3. Infection of macrophages **leads to** granulomatous inflammation with caseous necrosis. *Inferred; the step was not retrieved for the spine specifically.*
4. Local immune programmes form in the lesion.
   - Single-cell RNA-seq of lesion tissue "yielded 67,274 high-quality cells and identified nine major cell types." Spinal TB and brucellar spondylitis "exhibit distinct local immunopathological programs," including foamy macrophages (Liu et al. 2026, PMID 42698543).
   - T-cell circuits "converge on a common osteo-immune pathway" (Yang et al. 2026, PMID 42239541).
5. Matrix degradation by host proteases (MMP-1 "plays a curial role in extracellular matrix degradation during the progression of tuberculosis", PMID 28129430), together with osteo-immune bone resorption, **results in** endplate and vertebral body destruction.
6. Destruction progresses along two branches:
   - **(6a)** Vertebral collapse **leads to** angular kyphosis (gibbus) (PMIDs 42477203, 38632071).
   - **(6b)** Caseous material spreads beneath the ligaments and into soft tissue, which **results in** paravertebral, psoas or epidural cold abscesses (PMID 42488243).
7. Abscess, sequestrum or kyphotic deformity compresses the cord, which **leads to** neurological deficit (Pott's paraplegia). MRI compression stage predicts recovery after surgery (OR 2.87). Even so, "severe MRI compression does not necessarily indicate irreversible spinal cord injury" (PMID 42431540).
8. **Modifier branch:** HIV-1 co-infection is associated with "reciprocal relationships" between *Mtb* and HIV-1 abundance in spinal tissue (PMIDs 41232750, PPR1035753).

**Suggested terms (labels only; IDs not retrieved)**
- **GO:** granuloma formation; inflammatory response; bone resorption; extracellular matrix disassembly; T cell activation; macrophage activation.
- **CL:** macrophage; foam cell; T cell; osteoclast.

**Not retrieved:** proteomics, metabolomics, spatial transcriptomics and CRISPR screen data specific to spinal TB.

## 7. Anatomical Structures Affected

UBERON labels are given; IDs were not retrieved.

- **Primary site:** vertebral column and vertebral body, with secondary involvement of the intervertebral disc. Marked disc involvement favours pyogenic infection, OR 0.209 for TB (PMID 42477203).
- **Distribution by region:**
  - Reviews often cite the thoracic or thoracolumbar spine as most common.
  - Large Chinese series find the lumbar spine most common: 47.30% lumbar vs 40.95% thoracic in a Guizhou series of 597 patients, and 43.53% vs 32.55% in Guangxi (via https://pmc.ncbi.nlm.nih.gov/articles/PMC8683179, https://pmc.ncbi.nlm.nih.gov/articles/PMC7019620).
  - Multisegmental and skip lesions occur (PMIDs 40046928, 41081173).
- **Secondary structures:**
  - Spinal cord, through compressive myelopathy.
  - Spinal meninges, in the meningeal form (PMID 40211169).
  - Psoas muscle (abscess).
  - Lung (concurrent pulmonary TB).
- **Body systems:** musculoskeletal, nervous and respiratory.
- **Tissue and cell level:** bone tissue, bone marrow and epidural soft tissue; macrophages, foam cells and T cells (PMID 42698543).
- **Subcellular level:** no disease-specific data retrieved. The phagosome of infected macrophages is the presumed niche, but this was not retrieved here.
- **Lateralization:** midline. Abscesses may be unilateral or bilateral; bilateral psoas abscess has been reported in a preprint, PPR1133032.

## 8. Temporal Development

- **Onset:** occurs from childhood to old age. A paediatric series had a mean age of 8.5 years (PMID 33327790). An East China series of 893 patients had a median age of 56 (PMID 40890663). Onset is insidious or chronic, and diagnostic delay is common (PMID 32154388; PMC9955044).
- **Progression:**
  - Untreated disease progresses from vertebral osteomyelitis to collapse, abscess, deformity and neurological deficit.
  - MRI compression stages have been proposed for thoracic disease (PMID 42431540).
- **Remission:** treatment-induced. With treatment, "clinical results… are generally quite good with adequate and prompt care" (PMID 37304201).
- **Recurrence:** occurs, including after surgery and with emerging drug resistance in HIV infection (PMID 38162320; PMID 37083590).
- **Critical period:** early diagnosis. "A delay in diagnosis is the factor that most contributes to a worse prognosis" (PMC9955044).

## 9. Inheritance and Population

- **Frequency:**
  - Less than 1% of all TB (PMID 23275816).
  - About half of musculoskeletal TB (PMID 22118251; Jia 2024, PMID 39033332: "spinal tuberculosis accounting for approximately 50%").
  - Patient.info gives about 15% of extrapulmonary TB (https://patient.info/doctor/spinal-tuberculosis).
  - Population incidence and prevalence per 100,000 were **not retrieved**.
- **Inheritance:** not Mendelian. Risk is multifactorial, with host susceptibility loci (§2).
- **Not applicable:** penetrance, anticipation, mosaicism, founder effects and carrier frequency.
- **Sex ratio:** male:female 1.4:1 (PMID 40890663).
- **Geography:** endemic in high-TB-burden regions. The retrieved cohorts come from China, India, South Africa and Pakistan.

## 10. Diagnostics

**Gold standard.** "Neuroimaging-guided needle biopsy from the affected site in the center of the vertebral body is the gold standard technique for early histopathological diagnosis" (PMID 22118251).

**Imaging.**
- "MRI is most common imaging modality used," and "PET CT is recently evaluated for response assessment with promising results" (Kubihal 2022, PMID 34956831).
- MRI "is more sensitive imaging technique than x-ray and more specific than computed tomography" (PMID 22118251).
- **Telling tuberculous from pyogenic spondylitis on MRI:**
  - Signal-intensity ratio scores reached AUC 0.888 and 0.870. A cut-off of EAS ≥0.400 gave 93.1% sensitivity and 85.3% specificity (PMID 42550235).
  - Vertebral collapse (OR 3.713) favours TB (PMID 42477203).
  - Features that differ significantly across pyogenic, tuberculous, brucellar and fungal spondylitis include skip lesions, intraosseous abscess and the extent of destruction (PMID 41081173).
- **Machine-learning differentiation:**
  - Five-centre multimodal model for TB, pyogenic and brucellar spondylitis (PMID 42819251).
  - Radiomics vs spinal metastasis, AUC 0.971 (PMID 43033258).
  - Nomogram vs pyogenic infection, AUC 0.770 (PMID 42025441).

**Molecular and microbiological tests.**

| Test | Performance | Source |
|---|---|---|
| Xpert MTB/RIF Ultra on spinal biopsy | Sensitivity 94.7% (95% CI 75.3–99.7%). "Xpert Ultra detected more STB cases than culture for CT-guided biopsy samples." Culture specificity on CT-guided samples was only 43%. | Waters et al. 2024, PMID 38173845 |
| Xpert MTB/RIF in osteoarticular TB (pooled, 19 studies) | Sensitivity 81%, specificity 99% vs composite reference | Cited in https://pmc.ncbi.nlm.nih.gov/articles/PMC10583401 |
| Xpert MTB/RIF in musculoskeletal TB (2017 meta-analysis) | AUC >0.9 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5627758 |
| Xpert MTB/RIF in bone and joint TB (PLoS One 2019 meta-analysis) | "good diagnostic accuracy… not related to the type of specimen" | https://pmc.ncbi.nlm.nih.gov/articles/PMC6705841 |
| Digital droplet PCR | Detected MTBC DNA in 10/10 culture-confirmed biopsies | PMID 41232750 |
| mNGS / tNGS | Detection 97.47% (mNGS) and 100% (tNGS); preprint | PPR1249986 |
| Urinary LAM, HIV-negative patients | Sensitivity 37.3%, specificity 92.3% | Das et al. 2026, PMID 43033803 |
| Histopathology | Granulomatous inflammation; foamy macrophage features distinguish TB from brucellosis | PMID 42698543 |

- **Genetic testing of the host:** not indicated.
- **Genetic testing of the pathogen:** used for drug resistance, through Xpert rifampicin-resistance detection, tNGS and WGS (PMID 37194130).
- **Differential diagnosis:**
  - Pyogenic spondylodiscitis and brucellar spondylitis.
  - Fungal spondylitis.
  - Spinal metastasis.
  - Spondyloarthritis (PMID 42638134).
  - Neuroschistosomiasis (PMID 42756785).
- **Screening:** there is no population screening. Suspicion is raised in patients with back pain who come from endemic settings or have TB risk factors.

## 11. Outcome/Prognosis

- **Mortality and survival:** spinal-TB-specific figures were not retrieved.
- **Outcome on treatment:** generally good (PMID 37304201). In the Madras MRC trial, 10-year favourable status was 90% after radical surgery, 94% after 6 months of ambulant chemotherapy and 99% after 9 months (PMID 10872368; figures from a summary of the record).
- **Neurological recovery:**
  - In Sharma et al. 2016, 128 of 200 patients with deficit (64%) recovered completely on the AIS scale. The level of vertebral involvement, AIS grade at presentation, and bladder or bowel involvement affected recovery (https://www.nature.com/articles/sc201685).
  - Children can recover from long-standing deficits lasting 6–24 months (PMID 33327790).
- **Complications:**
  - Kyphotic deformity.
  - Permanent paraplegia.
  - Recurrence.
  - Drug resistance (PMIDs 38162320, 40890663).
- **Prognostic factors:**
  - Diagnostic delay (PMC9955044).
  - AIS grade and duration of deficit.
  - MRI compression stage (PMID 42431540).
  - HIV status.
  - Drug resistance.

## 12. Treatment

NCIT labels are given; IDs were not retrieved.

**Pharmacotherapy.** "Combination multidrug antitubercular therapy is the basis of treatment" (PMID 37304201). Standard regimens use isoniazid, rifampicin, pyrazinamide and ethambutol. The Madras trial used isoniazid plus rifampicin for 6 or 9 months (PMID 10422019).

- **Duration of treatment:**
  - A meta-analysis found 6 months of antitubercular therapy healed 375/414 patients (90.58%). "Overall, the healed status of spinal TB was equivalent in patients in both groups" (RR 0.98, 95% CI 0.92–1.04) (Aryal 2022, PMID 34784702).
  - In surgically treated Chinese patients, "short-course chemotherapy could be equivalent to the standard chemotherapy in terms of efficacy" (PMID 33781290).
  - Guidance is largely "extrapolated from trials on pulmonary disease," and there have been few good-quality studies since the BMRC trials of the 1970s (PMID 32154388).
- **Landmark trials** (British Medical Research Council Working Party on Tuberculosis of the Spine):
  - Korea, 265 patients followed for 3 years (PMID 8444944).
  - 15-year assessment from Korea and Hong Kong (PMID 9619936).
  - 5-year assessment of 6-, 9- and 18-month regimens (PMID 10422019).
  - Ambulant chemotherapy vs radical surgery in Madras (PMID 10872368).
- **Drug-resistant disease:** managed with regimens guided by resistance testing (review PMID 32904104).
- **Pharmacogenomics:** no spinal-TB-specific data retrieved.

**Surgery.**
- **Indications:** "Patients who come with significant kyphosis or neurological impairments are the only ones who require surgical care" (PMID 37304201).
- **Procedures:**
  - Debridement and decompression.
  - Bone grafting. A network meta-analysis of 517 patients favoured autograft for safety (PMID 37202780).
  - Instrumented fusion.
  - Posterior revision and kyphosis correction (PMIDs 37083590, 38632071).
  - Oblique lateral interbody fusion (OLIF) vs open surgery in lumbar disease: shorter operative time and less blood loss in a 617-patient systematic review (preprint PPR1243934).
  - Gardner-Wells traction for paediatric kyphosis (PMID 39631124).

**Supportive and rehabilitative care.** Physical and rehabilitation medicine, nutrition, and vitamin D supplementation (case series PMID 39033700).

**Advanced therapeutics.** Gene, cell, RNA, targeted and checkpoint therapies are not applicable. No spinal-TB NCT trials were retrieved.

**Suggested NCIT labels:** antitubercular agent; isoniazid; rifampin; pyrazinamide; ethambutol; spinal fusion; surgical debridement; laminectomy/decompression; bone graft; physical therapy.

## 13. Prevention

- **Primary prevention:** control of pulmonary TB transmission, and BCG vaccination in endemic settings. No spinal-specific vaccine efficacy data were retrieved.
- **Secondary prevention:** early detection of infection and molecular diagnosis. "Novel molecular diagnostic methods are effective and timely choices" (PMID 36826156).
- **Tertiary prevention:** complete antitubercular therapy, timely decompression, deformity correction, and surveillance for relapse and resistance.
- **Genetic counselling:** not applicable.
- **Prophylaxis:** treatment of latent TB infection in high-risk groups, such as people with HIV. Spinal-specific data were not retrieved.

## 14. Other Species / Natural Disease

- Lesions consistent with tuberculous spondylitis have been found at abattoir inspection of domestic pigs and in hunted wild swine. They have been proposed as a model for human Pott disease (Amato et al. 2019, PMID 29846908).
- **Zoonotic potential:** human *M. bovis* spinal TB occurs (3/56 cases, PMID 32076625), which implies an animal reservoir.
- OMIA, VBO and ortholog data are not applicable or were not retrieved.

## 15. Model Organisms

- **Rabbit, the principal model.**
  - Review: "New Zealand rabbits, possessing a comparable anatomical structure to humans" (Jia 2024, PMID 39033332).
  - Model establishment (Geng 2015, PMID 25325713).
  - Direct infusion of *M. tuberculosis* H37Rv into the disc space through a posterolateral approach (Yue 2022, PMID 35896778).
  - Lumbar vertebral model: "M. tuberculosis was cultured in 67% of the abscesses" (Liu 2015, PMID 25420665).
- **What the models reproduce:** local vertebral destruction and abscess formation.
- **Limitations:** these are mainly direct local inoculation models, not haematogenous spread from a pulmonary focus. They bypass the natural disease course and are used for surgical, biomaterial and drug-delivery research.
- **Swine:** a possible natural model (PMID 29846908).
- **Not retrieved:** spinal-TB-specific mouse, zebrafish or organoid models, and model database entries (MGI and others).

---

## Gaps to fill from the primary databases
1. ICD-10, ICD-11 and Orphanet identifiers.
2. Population incidence and prevalence per 100,000.
3. Pooled frequencies for each symptom.
4. Mortality.
5. WHO guidance on treatment duration for spinal TB.
6. Verified IDs for all HPO, GO, CL, UBERON, CHEBI and NCIT terms.
7. NCBI Taxon IDs for the pathogens.
8. PMIDs for the sources cited by URL only: Sharma 2016, the Central India series, Glassman 2023 (PMID 36826156 was found later and should be checked against PMC9955044), and the two Xpert meta-analyses.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 56 |
| Resolved | 56 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 56 |
| On topic | 42 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41232750` *(abstract only)*: "reciprocal expansion"
  - Text part not found as substring: 'reciprocal expansion' (note: only abstract available for PMID:41232750, full text may contain this excerpt)
- `PMID:37304201` *(abstract only)*: "clinical results… are generally quite good with adequate and prompt care"
  - closest text in source: "Clinical results for the treatment of spinal TB are generally quite good with adequate and prompt care."
- `PMC:PMC9955044` *(abstract only)*: "A delay in diagnosis is the factor that most contributes to a worse prognosis"
  - closest text in source: "While the current literature shows that timely diagnosis is crucial to reduce the morbidity and mortality from Pott's disease, there is a lack of specific clinical diagnostic criteria for Pott's disease, and the symptoms may be very non-specific"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0043836` (4 mentions) - the report calls it "research report for a disease knowledge base"; MONDO calls it **tuberculosis, spinal**