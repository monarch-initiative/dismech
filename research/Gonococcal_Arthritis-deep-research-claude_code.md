---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-27T00:26:25.593460'
end_time: '2026-11-27T00:30:18.690276'
duration_seconds: 233.1
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Gonococcal Arthritis
  mondo_id: MONDO:0041903
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 10
  num_turns: 16
  total_cost_usd: 1.2884391
  session_id: 59c695cd-cde7-437e-acd5-4eed298e448c
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 14
  retrieval_calls: 11
  assistant_text_blocks: 2
citation_count: 29
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:11157049
  - PMC:PMC4869260
  relevance_assessed: 18
  on_topic: 11
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 30
  verified: 9
  not_found: 0
  obsolete: 0
  unverifiable: 21
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0100626
    reported_labels:
    - tenosynovitis
    ontology_label: Chronic hepatic failure
  service_unreachable: 21
  obsolescence_unchecked: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gonococcal Arthritis
- **MONDO ID:** MONDO:0041903 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Gonococcal Arthritis** covering all of the
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

Let me try PubMed E-utilities directly for PMIDs and abstracts.

I have gathered enough sourced material to write the report. A few sections (model organisms specific to DGI, detailed omics) have little disease-specific literature, which I'll flag.

---

# Disease Characteristics Research Report: Gonococcal Arthritis (Disseminated Gonococcal Infection)

**Interpretation note:** This report covers **MONDO:0041903**, labeled *"gonococcal infection of joint" / gonococcal arthritis*, the articular manifestation of **disseminated gonococcal infection (DGI)**. This is an **infectious disease**, not a Mendelian disorder: it has **no human causal gene**. The "causal gene" field is correctly recorded as "not recorded." The causative agent is the Gram-negative diplococcus ***Neisseria gonorrhoeae***. Where host genetics matter, they are *susceptibility* factors (notably terminal complement component genes *C5–C9*), not causal genes, and bacterial virulence genes (notably the porin gene *porB*, allele *porB1A*/*Por1A*) drive dissemination. I treat gonococcal arthritis and DGI together, since the arthritis is one of two overlapping DGI syndromes, and much literature does not separate them.

---

## 1. Disease Information

**Overview.** Gonococcal arthritis is the joint manifestation of disseminated gonococcal infection — bacteremic spread of *N. gonorrhoeae* from a usually asymptomatic mucosal (urogenital, pharyngeal, or rectal) site. DGI classically presents as one of two overlapping syndromes: (1) an **arthritis–dermatitis syndrome** (the triad of tenosynovitis, dermatitis/skin lesions, and migratory polyarthralgia, typically with negative joint-fluid cultures but occasionally positive blood cultures), and (2) a **localized purulent/septic arthritis** (usually mono- or oligoarticular, with positive synovial-fluid cultures and usually negative blood cultures) ([StatPearls, NBK470439](https://www.ncbi.nlm.nih.gov/books/NBK470439/); [PMID 16297736](https://pubmed.ncbi.nlm.nih.gov/16297736/)). The two are often described as a continuum rather than discrete entities.

**Key identifiers** (verify against primary ontology browsers before database loading):
- **MONDO:** MONDO:0041903 ("gonococcal infection of joint") ([SAIL Concept Library/MONDO node](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0041903/)).
- **ICD-10 (WHO):** M01.3* "Arthritis in other bacterial diseases classified elsewhere," with the underlying gonococcal infection dagger-coded **A54.4†** ([NHS ICD-10 M00–M03 block](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-m00-m03.htm)).
- **ICD-10-CM:** **A54.42** "Gonococcal arthritis" (more specific than the WHO parent) ([search result mapping](https://www.ncbi.nlm.nih.gov/books/NBK470439/)).
- **GARD:** 0027964 (cross-referenced from the MONDO node).
- **MeSH:** No dedicated gonococcal-arthritis heading; PubMed indexes these records under *Arthritis, Infectious/etiology* and *Gonorrhea/complications* ([PMID 12787521](https://pubmed.ncbi.nlm.nih.gov/12787521/)). The broader septic-arthritis heading is MeSH D001170.
- **Orphanet:** An Orphanet:100642 cross-reference appears on the MONDO node, but could not be confirmed as the gonococcal-arthritis term; DGI is generally not an Orphanet rare-disease entry. *Not confirmed.*

**Synonyms / alternative names:** disseminated gonococcal infection (DGI); gonococcal arthritis-dermatitis syndrome; arthritis-dermatitis syndrome; gonococcal septic arthritis; gonococcemia; "gonococcal infection of joint."

**Information source type.** Disease-level, aggregated resources (clinical reviews, case series, surveillance reports) rather than a single EHR cohort; recent surveillance (e.g., Alaska) is drawn from case-based public-health records ([MMWR 75(27), 2025](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm)).

---

## 2. Etiology

**Primary cause — infectious.** The obligate cause is infection with ***Neisseria gonorrhoeae*** (NCBI Taxonomy ID 485). DGI follows hematogenous dissemination from a mucosal focus, which is frequently asymptomatic — a key reason DGI is often diagnosed without a recognized preceding genital infection ([PMC2213355](https://pmc.ncbi.nlm.nih.gov/articles/PMC2213355); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470439/)).

**Bacterial (pathogen-side) determinants.** Dissemination is strongly associated with gonococcal strains showing **stable serum (complement) resistance**, historically typed as **Por1A (PorB1A) porin serovars**, which are also often penicillin-sensitive, AHU auxotrophs ([PMID 11157049](https://pmc.ncbi.nlm.nih.gov/articles/pmid/11157049); [PMC2213355](https://pmc.ncbi.nlm.nih.gov/articles/PMC2213355)). "Disseminated gonococcal infection often occurs without local genital inflammation, and it is mostly caused by strains that resist normal human serum without relying on sialylation... Por1A strains are the ones most often linked to disseminated disease" ([PMID 11157049](https://pmc.ncbi.nlm.nih.gov/articles/pmid/11157049)).

**Host risk factors — genetic:**
- **Terminal complement component deficiencies (C5, C6, C7, C8, and C9; and properdin for the alternative pathway).** These impair formation of the membrane attack complex (MAC), which is the principal defense against *Neisseria*, and markedly raise risk of disseminated/recurrent neisserial disease ([Terminal complement pathway deficiency overview](https://pmc.ncbi.nlm.nih.gov/articles/PMC4869260); [PMC8793329](https://pmc.ncbi.nlm.nih.gov/articles/PMC8793329)). Candidate susceptibility genes: *C5, C6, C7, C8A/C8B/C8G, C9, CFP* (properdin, X-linked).
- Deficiencies "raise susceptibility mainly to Neisseria species, while heterozygous carriers are generally not affected" ([PMC4869260](https://pmc.ncbi.nlm.nih.gov/articles/PMC4869260)).

**Host risk factors — environmental / demographic:**
- **Female sex** and **menstruation/pregnancy/postpartum** (hormonal and complement changes increase dissemination risk) ([CID 2019 case series, PMID 30418536](https://pubmed.ncbi.nlm.nih.gov/30418536/)).
- **Complement-inhibitor therapy:** eculizumab (and by mechanism, other terminal C5 inhibitors) — an iatrogenic phenocopy of terminal complement deficiency (see §5, §12).
- Multiple sex partners / high community gonorrhea prevalence; **injection drug and methamphetamine use and housing instability** in recent US clusters ([MMWR Alaska 2025](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm); [MMWR Michigan 2019, PMID 32214085](https://pubmed.ncbi.nlm.nih.gov/32214085/)); untreated mucosal gonorrhea.

**Protective factors.** Intact terminal complement pathway and prompt treatment of mucosal gonorrhea. No validated protective genetic variant or dietary factor is established for DGI; I found no specific literature, so this is reported as **not established**.

**Gene–environment interactions.** The clearest interaction is between **host MAC capability and bacterial serum resistance**: dissemination requires either a serum-resistant strain (bacterial genotype) *or* a host with impaired MAC (complement-deficient or on a C5 inhibitor). Terminal C5 blockade converts even relatively serum-sensitive strains into disseminators, as shown by the eculizumab case series ([PMID 30418536](https://pubmed.ncbi.nlm.nih.gov/30418536/)).

---

## 3. Phenotypes

Frequencies vary widely by series and by which DGI syndrome predominates; figures below are from a 20-year Thai cohort (n≈41) and other series ([Thailand cohort, PMC11338079](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11338079/); [NT Australia, PMID 31392956](https://pubmed.ncbi.nlm.nih.gov/31392956/); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470439/)).

| Phenotype | Type | Frequency (illustrative) | HPO suggestion |
|---|---|---|---|
| Arthralgia / polyarthralgia (often migratory) | symptom | very common | HP:0002829 Arthralgia |
| Arthritis (purulent/septic, mono- or oligoarticular) | clinical sign | 88.7–92.7% in some cohorts | HP:0005059 Septic arthritis / HP:0001369 Arthritis |
| Tenosynovitis | clinical sign | ~63% (Thailand) | HP:0100626 Tenosynovitis |
| Dermatitis / skin lesions (pustular, vesiculopustular, hemorrhagic) | physical manifestation | variable; part of triad | HP:0011123 Inflammatory abnormality of the skin; HP:0200037 Papulosquamous eruption |
| Fever | symptom | ~90% | HP:0001945 Fever |
| Genitourinary symptoms (often absent) | symptom | ~29% | HP:0000124 Renal/urogenital abnormality (nonspecific) |
| Endocarditis (rare, severe) | complication | ~1–3% | HP:0100584 Endocarditis |
| Meningitis (rare) | complication | rare | HP:0001287 Meningitis |
| Perihepatitis (Fitz-Hugh–Curtis) | complication | occasional | — |

The "classic triad" of tenosynovitis + dermatitis + polyarthralgia is now often **incomplete or rare** in practice — the NT Australia series reported it as uncommon, with purulent arthritis predominating (88.7%) ([PMID 31392956](https://pubmed.ncbi.nlm.nih.gov/31392956/)).

**Characteristics:** Onset is **acute to subacute** in otherwise healthy, usually young sexually active adults (not congenital). Severity ranges mild (self-limited arthralgia/dermatitis) to severe (purulent arthritis with joint destruction; rarely endocarditis/meningitis). Course is typically **monophasic and treatment-responsive**, but untreated purulent arthritis can cause **permanent joint damage** ([AFP 1992 review](https://www.ccjm.org/content/52/2/161)).

**Quality-of-life impact.** Persistent articular symptoms are common: in a 58-case series, **60% had persistent articular symptoms at discharge** ([gonococcal arthritis case series, PMID 35590115](https://pubmed.ncbi.nlm.nih.gov/35590115/)). No DGI-specific EQ-5D/SF-36 data were retrieved.

---

## 4. Genetic / Molecular Information

**Human causal genes: none.** Gonococcal arthritis is infectious; there is no human pathogenic variant that causes it.

**Host susceptibility genes (not causal):** Terminal complement components — ***C5, C6, C7, C8A, C8B, C8G, C9***, and ***CFP*** (properdin, X-linked). Loss-of-function variants cause MAC deficiency and predispose to disseminated neisserial infection; carriers (heterozygotes) are generally unaffected ([PMC4869260](https://pmc.ncbi.nlm.nih.gov/articles/PMC4869260)). Inheritance of these deficiencies is mostly autosomal recessive (properdin X-linked). These are susceptibility loci, not DGI-causing mutations; full ClinVar/gnomAD allele-frequency annotation would be at the complement-deficiency disease level, not under MONDO:0041903.

**Bacterial virulence genetics (the operative "molecular" story):**
- ***porB*** allele **porB1A (Por1A)** — porin that binds host complement regulator **factor H** at surface **loop 5**, conferring stable serum resistance and dissemination ([JCI/J Immunol references, PMID 18292569](https://pubmed.ncbi.nlm.nih.gov/18292569/)). "Factor H binding was localized to surface loop 5 of Por1A, and peptides from that loop inhibited binding" ([insight.jci.org references](https://insight.jci.org/references/scholar/2136/B39)).
- **LOS sialylation** (via *lst* sialyltransferase using host CMP-NANA) — a *separate*, unstable route to serum resistance that recruits factor H; many stable disseminating strains lack the LOS acceptor and do not rely on it ([PMC3536161](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536161); [PMC2213355](https://pmc.ncbi.nlm.nih.gov/articles/PMC2213355)).
- **NspA** contributes to serum resistance when LOS is truncated; **lipid A phosphoethanolamine** modulates C4BP/factor H binding ([PMC6346132](https://pmc.ncbi.nlm.nih.gov/articles/PMC6346132); [PMC3536161](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536161)).

**Epigenetics / chromosomal abnormalities:** Not applicable to this infectious disease (no human epigenetic or cytogenetic lesion). Bacterial antigenic/phase variation (pilin, Opa) is a gonococcal genome feature but not a human chromosomal change.

---

## 5. Environmental Information

**Infectious agent.** *Neisseria gonorrhoeae* (NCBI Taxon 485), a Gram-negative, oxidase-positive diplococcus; humans are the only natural host. Transmission is sexual (urogenital, anorectal, pharyngeal) and vertical (perinatal) — DGI arises when an organism from such a site enters the bloodstream.

**Environmental/iatrogenic factors.** **Terminal complement inhibitors (eculizumab; mechanistically ravulizumab and other anti-C5 agents)** are a documented environmental risk: the FDA safety-report series found 9 gonorrhea cases on eculizumab, **8/9 (89%) disseminated**, 8 hospitalized, 7 with positive blood cultures ([PMID 30418536](https://pubmed.ncbi.nlm.nih.gov/30418536/)). No DGI-specific ravulizumab case counts were retrieved.

**Lifestyle factors.** High-risk sexual behavior and untreated mucosal gonorrhea; **methamphetamine/injection drug use and housing instability** featured in recent US outbreak clusters ([MMWR Alaska 2025](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm); [MMWR Michigan 2019](https://www.cdc.gov/mmwr/volumes/69/wr/mm6912a5.htm)). No chemical-toxin (CTD-type) etiology applies.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating event → clinical manifestation):**

1. *N. gonorrhoeae* colonizes a mucosal surface (urogenital/pharyngeal/rectal), often **asymptomatically** → establishes a reservoir for invasion. (demonstrated)
2. A strain with **stable serum resistance** (Por1A phenotype) **binds host factor H via PorB loop 5** and/or sialylates LOS → **evades alternative-pathway complement and MAC killing** in blood. *This leads to* survival in serum ([PMID 18292569](https://pubmed.ncbi.nlm.nih.gov/18292569/); [PMC2213355](https://pmc.ncbi.nlm.nih.gov/articles/PMC2213355)). (demonstrated in vitro)
3. Serum-resistant organisms **enter the bloodstream → bacteremia (gonococcemia)**. *Branch point:* host MAC deficiency or C5-inhibitor therapy permits dissemination even by less serum-resistant strains ([PMID 30418536](https://pubmed.ncbi.nlm.nih.gov/30418536/)). (inferred from epidemiology + mechanism)
4. Circulating gonococci and their products (LOS/endotoxin, peptidoglycan) **deposit in synovium, tenosynovium, and dermal vessels** and **trigger innate immune activation** (complement C5a, TLR4/LOS signaling, cytokine release) → local inflammation. (partly inferred)
5. **Branch A — arthritis–dermatitis syndrome:** immune-complex/complement-mediated and embolic small-vessel injury *results in* **migratory polyarthralgia, tenosynovitis, and pustular/hemorrhagic skin lesions**; synovial fluid is often sterile while blood cultures may be positive. (mechanism partly inferred; phenotype demonstrated)
6. **Branch B — purulent/septic arthritis:** viable organisms seed and proliferate within a joint → **neutrophilic purulent arthritis** with positive synovial-fluid culture; blood cultures usually negative. (demonstrated)
7. Sustained intra-articular infection/inflammation → **cartilage and joint damage**; rare hematogenous seeding of endocardium or meninges → **endocarditis/meningitis**. (demonstrated clinically)

**Molecular/cellular detail:** Key pathways are **complement (alternative and terminal/MAC)** regulation and evasion (factor H, C4BP recruitment); innate sensing of **LOS via TLR4/MD-2**; neutrophil recruitment and degranulation driving purulent arthritis. Suggested **GO terms:** complement activation, alternative pathway (GO:0006957); regulation of complement activation (GO:0030449); inflammatory response (GO:0006954); neutrophil chemotaxis (GO:0030593). Suggested **CL terms:** neutrophil (CL:0000775), synovial fibroblast (CL:0000210), macrophage (CL:0000235), endothelial cell (CL:0000115). Suggested **CHEBI:** N-acetylneuraminic acid/sialic acid (CHEBI:28853) for LOS sialylation.

**Omics/single-cell/CRISPR:** No DGI-specific transcriptomic, proteomic, metabolomic, single-cell, or functional-genomics screens were retrieved — reported as **not available** at the disease level.

---

## 7. Anatomical Structures Affected

- **Primary organs/systems:** **Joints** (synovium) and **tendon sheaths** — musculoskeletal system; **skin** (dermis/epidermis); **bloodstream** (bacteremia). UBERON suggestions: synovial joint (UBERON:0002217), synovial membrane (UBERON:0002018), tendon sheath (UBERON:0007844), skin (UBERON:0002097), blood (UBERON:0000178).
- **Secondary/complication organs:** heart valves/endocardium (UBERON:0002165) in endocarditis; meninges (UBERON:0002360) in meningitis; liver capsule/peritoneum (perihepatitis).
- **Joint distribution:** typically **knees, wrists, ankles, and small hand joints**; often **asymmetric, migratory (polyarthralgia)** or **mono-/oligoarticular (purulent form)**; lateralization is variable (HP: often asymmetric).
- **Tissue/cell level:** synovial lining cells, dermal vascular endothelium, infiltrating neutrophils (CL:0000775) and macrophages (CL:0000235).
- **Subcellular:** gonococci are typically extracellular/intraphagosomal; no human organelle lesion. GO cellular component of note: external side of plasma membrane / cell surface (complement regulator binding).

---

## 8. Temporal Development

- **Onset:** **Adult-onset**, acute to subacute, in young sexually active people (not congenital/pediatric except perinatal gonorrhea, which is a different presentation). Symptoms in the eculizumab setting appeared ~days after exposure/triggering (one report ~8 days) ([PMC8216817](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8216817/)).
- **Progression/course:** Usually **monophasic and self-limited to treatment-responsive**; the arthritis–dermatitis phase can evolve into localized purulent arthritis. With appropriate antibiotics, systemic features resolve quickly; untreated or delayed purulent arthritis can progress to **joint destruction**.
- **Duration:** Acute illness over days–weeks; **~60% have residual/persistent articular symptoms at discharge** in one series ([PMID 35590115](https://pubmed.ncbi.nlm.nih.gov/35590115/)). It is not a chronic lifelong disease once treated, though recurrent DGI occurs in complement-deficient or complement-blocked hosts.
- **Critical window:** Early antibiotic therapy and prompt joint drainage are the intervention window preventing permanent joint damage ([AFP/CCJM review](https://www.ccjm.org/content/52/2/161)).

---

## 9. Inheritance and Population

- **Epidemiology:** DGI historically develops in **~0.5–3% of gonococcal infections** ([AFP 1992 review](https://www.ccjm.org/content/52/2/161)). It is a complication of gonorrhea, which is extremely common (hundreds of thousands to millions of US infections annually), so DGI incidence tracks gonorrhea incidence and local serovar distribution. No stable population prevalence per 100,000 is well defined; it is uncommon but rising in recent US clusters.
- **Recent surveillance signal:** Alaska reported **35 DGI cases in 2023–2024 vs. 3 in 2022** (median age 36 years, IQR 15; ~49–51% male) ([MMWR 75(27) 2025](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm)); Southwest Michigan reported a 2019 cluster of 13 confirmed + 3 probable cases, several in people experiencing homelessness ([MMWR 69(12) 2020, PMID 32214085](https://pubmed.ncbi.nlm.nih.gov/32214085/)).
- **Inheritance:** Not a heritable disease. Relevant **host susceptibility** (terminal complement deficiency) is mostly **autosomal recessive** (properdin X-linked); penetrance for neisserial disease is incomplete; carrier frequency and founder effects pertain to the complement-deficiency disorders, not to gonococcal arthritis itself.
- **Sex ratio:** Classically **female-predominant** (menstruation, pregnancy, and asymptomatic carriage favoring dissemination), though recent clusters show near-equal or male-leaning sex distribution ([MMWR Alaska](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm)).
- **Age:** Predominantly young to middle-aged sexually active adults.

---

## 10. Diagnostics

- **Cultures / microbiology:**
  - **Blood cultures** positive in **<~1/3 of cases**, more often in the arthritis–dermatitis form; reported positivity ranges ~4–70% across series ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470439/)).
  - **Synovial fluid** culture/NAAT: more often positive in the **purulent arthritis** form; synovial fluid is typically inflammatory (elevated WBC, neutrophil-predominant).
  - **Mucosal screening (urogenital, pharyngeal, rectal) NAAT** is essential because the primary site is often asymptomatic and more frequently positive than blood/joint ([CDC STI app, DGI page](https://www.cdc.gov/stiapp/gonorrhea_dgi.html)).
  - Skin lesion Gram stain/culture may show organisms.
- **Lab markers:** elevated inflammatory markers (CRP/ESR), leukocytosis — nonspecific. LOINC-type gonococcal NAAT and culture results apply.
- **Imaging:** joint ultrasound/MRI/radiography to assess effusion, tenosynovitis, and joint damage (supportive, nonspecific).
- **Host workup:** In recurrent or unexplained disseminated neisserial infection, test **complement function (CH50/AH50, then individual terminal components)** — low CH50 with normal C3/C4 suggests terminal pathway deficiency ([Terminal complement pathway deficiency overview](https://pmc.ncbi.nlm.nih.gov/articles/PMC4869260)); review medication list for C5 inhibitors.
- **Diagnostic criteria / differential:** Clinical diagnosis supported by compatible syndrome + positive gonococcal testing at any site. Differentials: other **septic (staph/strep) arthritis**, reactive arthritis, crystal arthropathy (gout/pseudogout), Lyme and other bacterial arthritides, meningococcemia (disseminated *N. meningitidis*), and rheumatologic disease. Antimicrobial susceptibility testing on any cultured isolate is important given resistance trends.
- **Genetic/omics testing:** Not used to diagnose the arthritis itself. Host complement-gene sequencing is reserved for suspected inherited terminal-complement deficiency. Omics-based diagnostics: **not applicable**.
- **Screening:** Screen and treat mucosal gonorrhea; screen sexual partners; consider complement evaluation after an unexplained or recurrent episode.

---

## 11. Outcome / Prognosis

- **Generally favorable with prompt treatment.** Systemic illness and arthritis–dermatitis features usually resolve with antibiotics; mortality is low in uncomplicated DGI.
- **Morbidity:** **Persistent articular symptoms in ~60% at discharge** in one series ([PMID 35590115](https://pubmed.ncbi.nlm.nih.gov/35590115/)); untreated/delayed purulent arthritis can cause **permanent joint damage** ([CCJM/AFP review](https://www.ccjm.org/content/52/2/161)).
- **Severe complications (high morbidity/mortality):** **endocarditis** and **meningitis** are rare but historically carry substantial risk; recent Alaska surveillance documented severe outcomes including gonococcal endocarditis and at least one fatal case ([MMWR Alaska 2025](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm); [Alaska endocarditis abstract](https://cdc.gov/eis-conference/php/abstracts/gonococcal-endocarditis.html)).
- **Prognostic factors:** promptness of therapy, presence of purulent arthritis vs. arthritis–dermatitis, endocardial/CNS involvement, antimicrobial resistance of the isolate, and host complement status/immunosuppression.

---

## 12. Treatment

- **First-line antibiotic (DGI/arthritis):** **Ceftriaxone 1 g IM/IV every 24 hours** (CDC 2021 STI guidelines list ceftriaxone 1 g q24h, with a 1–2 g IV q24h option for more severe disease such as endocarditis/meningitis), continued for ≥7 days (longer for endocarditis/meningitis), with transition guided by susceptibility and clinical response ([CDC STI app DGI page](https://www.cdc.gov/stiapp/gonorrhea_dgi.html); [CDC gonorrhea treatment guidelines](https://www.cdc.gov/std/treatment-guidelines/gonorrhea-adults.htm)). **Add doxycycline 100 mg BID ×7 days if chlamydia not excluded.** NCIT suggestions: Ceftriaxone (NCIT:C47704), Doxycycline (NCIT:C736).
- **Note on dosing:** DGI uses a higher/longer ceftriaxone regimen than uncomplicated gonorrhea (which is a single 500 mg IM dose per the 2020 update) ([MMWR mm6950a6, 2020](https://www.cdc.gov/mmwr/volumes/69/wr/mm6950a6.htm)). Do not conflate the two.
- **Source control:** **drainage/arthrocentesis** of purulent joints (repeat aspiration or arthroscopic lavage) as needed. NCIT: Joint Aspiration/Arthrocentesis.
- **Resistance considerations:** empiric ceftriaxone reflects current gonococcal resistance to penicillins, tetracyclines, and fluoroquinolones; susceptibility testing of isolates is advised.
- **Host-directed / special populations:** In patients on **eculizumab or other terminal C5 inhibitors**, clinicians are advised to counsel about gonococcal risk and consider antimicrobial prophylaxis per local resistance patterns, in addition to meningococcal vaccination ([PMID 30418536](https://pubmed.ncbi.nlm.nih.gov/30418536/); [Risk of DGI with terminal complement blockade, PMID 33560079](https://pubmed.ncbi.nlm.nih.gov/33560079/)).
- **Pharmacogenomics / gene / cell / RNA / targeted / immunotherapy:** Not applicable to this bacterial infection (beta-lactam allergy history guides alternatives). No DGI-specific experimental trial agents were retrieved.

---

## 13. Prevention

- **Primary:** prevent and promptly treat mucosal gonorrhea — condom use, partner reduction, routine STI screening of at-risk populations; **expedited partner therapy / partner notification** to interrupt transmission ([CDC STI guidelines](https://www.cdc.gov/std/treatment-guidelines/gonorrhea-adults.htm)).
- **Secondary:** screening asymptomatic high-risk individuals (and screening/treating partners) to prevent progression to DGI; outbreak investigation and partner-network tracing (as done in Alaska/Michigan clusters) ([MMWR Michigan](https://www.cdc.gov/mmwr/volumes/69/wr/mm6912a5.htm); [MMWR Alaska](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm)).
- **Tertiary:** timely antibiotics + joint drainage to prevent joint destruction, endocarditis, and meningitis.
- **Special-population prophylaxis:** For patients starting **complement C5 inhibitors**, counsel on gonococcal risk and consider antibacterial prophylaxis per local resistance data ([PMID 30418536](https://pubmed.ncbi.nlm.nih.gov/30418536/)).
- **Immunization:** No licensed gonococcus vaccine; some evidence that serogroup B meningococcal (4CMenB/OMV) vaccines may offer partial cross-protection against gonorrhea is under study, but this is **not an established DGI-prevention measure** (not confirmed from retrieved sources here). Meningococcal vaccination is separately required for complement-inhibitor recipients.
- **Counseling:** genetic counseling applies only to inherited terminal-complement deficiency, not to the infection itself.

---

## 14. Other Species / Natural Disease

*N. gonorrhoeae* is a **human-restricted pathogen** (NCBI Taxon 485); there is **no natural animal reservoir or naturally occurring gonococcal arthritis in other species**. Host restriction arises partly from the organism's specificity for human factors — e.g., **human factor H binds gonococci species-specifically**, and human CEACAMs/transferrin are required ([PMID 18292569](https://pubmed.ncbi.nlm.nih.gov/18292569/)). There is no OMIA veterinary counterpart, no zoonotic transmission, and no cross-species susceptibility of clinical relevance.

---

## 15. Model Organisms

- **Primary model:** the **17β-estradiol-treated female mouse model** of *N. gonorrhoeae* genital tract infection — "the only small-animal model of gonococcal genital tract infection," requiring estradiol (and antibiotics to suppress competing flora) to maintain an estrus-like, colonizable state ([Front Microbiol 2011 review](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2011.00107/full); [PMC3129519](https://pmc.ncbi.nlm.nih.gov/articles/PMC3129519)).
- **Humanized models:** transgenic mice expressing **human CEACAMs** (supporting Opa-mediated attachment) and supplementation/transgenesis with **human factor H / complement factors** to overcome host restriction ([Front Microbiol 2011](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2011.00107/full); [PMID 18292569](https://pubmed.ncbi.nlm.nih.gov/18292569/)).
- **Limitations / phenotype recapitulation:** These models reproduce **mucosal (genital) colonization and local infection**, not the **disseminated/arthritic** phenotype; murine complement and receptor differences limit modeling of human serum resistance and dissemination. No established animal model specifically recapitulates **gonococcal arthritis/DGI** was retrieved — reported as **not available**.
- **In vitro:** normal-human-serum bactericidal assays with isogenic Por1A/Por1B strains and factor-H-binding assays are the main experimental systems for the dissemination/serum-resistance mechanism ([PMC2213355](https://pmc.ncbi.nlm.nih.gov/articles/PMC2213355); [PMID 18292569](https://pubmed.ncbi.nlm.nih.gov/18292569/)).

---

## Summary of Key Ontology Suggestions
- **Disease:** MONDO:0041903; ICD-10-CM A54.42; ICD-10 M01.3*/A54.4†.
- **HPO:** HP:0005059 (septic arthritis), HP:0002829 (arthralgia), HP:0100626 (tenosynovitis), HP:0001945 (fever), HP:0100584 (endocarditis), HP:0001287 (meningitis).
- **GO:** GO:0006957 (alternative complement activation), GO:0030449 (regulation of complement activation), GO:0006954 (inflammatory response), GO:0030593 (neutrophil chemotaxis).
- **CL:** CL:0000775 (neutrophil), CL:0000210 (synovial fibroblast), CL:0000235 (macrophage), CL:0000115 (endothelial cell).
- **UBERON:** UBERON:0002217 (synovial joint), UBERON:0002018 (synovial membrane), UBERON:0002097 (skin), UBERON:0000178 (blood), UBERON:0002165 (endocardium).
- **CHEBI:** CHEBI:28853 (N-acetylneuraminic acid).
- **NCIT:** Ceftriaxone (NCIT:C47704), Doxycycline (NCIT:C736).
- **NCBI Taxon:** 485 (*Neisseria gonorrhoeae*).

## Evidence Gaps (not retrievable this session)
- A confirmed Orphanet/MeSH dedicated identifier for gonococcal arthritis.
- DGI-specific omics (transcriptomic/proteomic/metabolomic), single-cell, and CRISPR data.
- A validated animal model of the disseminated/arthritic phenotype (vs. mucosal infection).
- DGI-specific ravulizumab case counts and formal QoL (EQ-5D/SF-36) data.
- The original Ellison 1983 complement-deficiency primary source (confirmed only via secondary reviews).

**Primary sources cited:** [StatPearls NBK470439](https://www.ncbi.nlm.nih.gov/books/NBK470439/) · [PMID 16297736](https://pubmed.ncbi.nlm.nih.gov/16297736/) · [PMID 12787521](https://pubmed.ncbi.nlm.nih.gov/12787521/) · [PMID 18292569](https://pubmed.ncbi.nlm.nih.gov/18292569/) · [PMC2213355](https://pmc.ncbi.nlm.nih.gov/articles/PMC2213355) · [PMID 11157049](https://pmc.ncbi.nlm.nih.gov/articles/pmid/11157049) · [PMC3536161](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536161) · [PMC6346132](https://pmc.ncbi.nlm.nih.gov/articles/PMC6346132) · [PMID 30418536](https://pubmed.ncbi.nlm.nih.gov/30418536/) · [PMID 33560079](https://pubmed.ncbi.nlm.nih.gov/33560079/) · [PMC8216817](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8216817/) · [PMC4869260](https://pmc.ncbi.nlm.nih.gov/articles/PMC4869260) · [PMC8793329](https://pmc.ncbi.nlm.nih.gov/articles/PMC8793329) · [PMID 31392956](https://pubmed.ncbi.nlm.nih.gov/31392956/) · [PMID 35590115](https://pubmed.ncbi.nlm.nih.gov/35590115/) · [PMC11338079](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11338079/) · [MMWR Alaska 2025](https://www.cdc.gov/mmwr/volumes/75/wr/mm7527a2.htm) · [MMWR Michigan 2020, PMID 32214085](https://pubmed.ncbi.nlm.nih.gov/32214085/) · [MMWR mm6950a6 2020](https://www.cdc.gov/mmwr/volumes/69/wr/mm6950a6.htm) · [CDC STI guidelines](https://www.cdc.gov/std/treatment-guidelines/gonorrhea-adults.htm) · [CDC STI app DGI](https://www.cdc.gov/stiapp/gonorrhea_dgi.html) · [CCJM/AFP review](https://www.ccjm.org/content/52/2/161) · [Front Microbiol 2011 mouse model review](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2011.00107/full) · [MONDO node](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0041903/).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 18 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:11157049` *(abstract only)*: "Disseminated gonococcal infection often occurs without local genital inflammation, and it is mostly caused by strains that resist normal human serum without relying on sialylation... Por1A strains are the ones most often linked to disseminated disease"
  - closest text in source: "We screened 29 strains of Neisseria gonorrhoeae and found 16/21 strains that resisted killing by normal human serum and 0/8 serum sensitive strains that bound the complement regulator, C4b-binding protein (C4bp)"
- `PMC:PMC4869260` *(abstract only)*: "raise susceptibility mainly to Neisseria species, while heterozygous carriers are generally not affected"
  - closest text in source: "BACKGROUND: Deficiency of the eighth component of complement (C8) is a very rare primary immunodeficiency, associated with invasive, recurrent infections mainly caused by Neisseria species"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 21 |
| Terms whose name was checked | 5 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100626` (2 mentions) - the report calls it "tenosynovitis"; HP calls it **Chronic hepatic failure**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002165` - called "Secondary/complication organs:** heart valves/endocardium", "endocardium"

### Terms the ontology service could not be reached for

21 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `Orphanet:100642` (1 mention)
- `HP:0002829` (2 mentions)
- `HP:0001369` (1 mention)
- `HP:0001287` (2 mentions)
- `GO:0006957` (2 mentions)
- `GO:0030449` (2 mentions)
- `GO:0030593` (2 mentions)
- `CL:0000775` (3 mentions)
- `CL:0000210` (2 mentions)
- `CL:0000235` (3 mentions)
- `CL:0000115` (2 mentions)
- `CHEBI:28853` (2 mentions)
- `UBERON:0002217` (2 mentions)
- `UBERON:0002018` (2 mentions)
- `UBERON:0007844` (1 mention)
- `UBERON:0002097` (2 mentions)
- `UBERON:0000178` (2 mentions)
- `UBERON:0002165` (2 mentions)
- `UBERON:0002360` (1 mention)
- `NCIT:C47704` (2 mentions)
- `NCIT:C736` (2 mentions)

### Terms whose obsolescence could not be checked

3 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0005059` (2 mentions)
- `HP:0200037` (1 mention)
- `GO:0006954` (2 mentions)