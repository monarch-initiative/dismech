---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T02:23:59.986822'
end_time: '2026-10-24T02:25:06.063922'
duration_seconds: 66.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Palmoplantar Keratoderma Nagashima Type
  mondo_id: MONDO:0014272
  category: Mendelian
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
  - claude-sonnet-5-5
  web_search_requests: 4
  num_turns: 8
  total_cost_usd: 0.7431091999999997
  session_id: 1cf15249-1f26-5978-9d50-1c0a311fb777
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 18
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0005737
    reported_labels:
    - 'Subcellular level: the cytoplasm'
    ontology_label: cytoplasm
  labels_variant: 3
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
- **Disease Name:** Palmoplantar Keratoderma Nagashima Type
- **MONDO ID:** MONDO:0014272 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Palmoplantar Keratoderma Nagashima Type** covering all of the
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

# Nagashima-type palmoplantar keratosis (NPPK): research report

**Causal gene (first paragraph, as requested):** NPPK is caused by biallelic loss-of-function variants in **SERPINB7**. SERPINB7 is a clade-B intracellular serine protease inhibitor, with the HGNC ID `hgnc:13902` (not retrieved in this session; look it up before binding). The identifiers below were confirmed from a GARD/NIH record found by search, but I did not open that record: MONDO:0014272, OMIM:615598, ORPHA:140966, DOID:0070555 ([GARD record](https://rarediseases.info.nih.gov/assets/singles/16967.json); [KEGG H02264](https://www.kegg.jp/entry/H02264)). The disease is autosomal recessive.

**Scope and limits.** This report rests on one full-text read (Kubo 2013) and on search-result abstracts and snippets for the rest. I could not read the full text of the 2016 Acta Dermato-Venereologica paper. Anything I could not source is marked "not retrieved". Every CURIE below is a lead to be looked up before binding, per the repo's rules.

## 1. Disease information
- NPPK is an isolated, diffuse, non-epidermolytic palmoplantar keratoderma (PPK) with transgrediens (spread beyond the palms and soles). It is the most common PPK in East Asia and very rare elsewhere ([Acta Derm Venereol 2016](https://medicaljournals.se/acta/content/html/10.2340/00015555-2391)). The characteristic picture is well-demarcated erythema with mild-to-moderate hyperkeratosis. It can extend to the backs of the hands and feet and the Achilles tendon area. Lesional skin turns whitish and spongy after water exposure.
- Identifiers: see above. Synonyms: palmoplantar keratosis/keratoderma, Nagashima type; "PPK Nagashima type"; "Nagashima-type palmoplantar keratosis with SERPINB7 mutation".
- All data are aggregated from patient case series and disease-level resources, not EHR.

## 2. Etiology
**Causal factors.** The cause is genetic. Kubo et al. found "biallelic putative loss-of-function mutations in SERPINB7" in 13 unrelated Japanese patients (PMID:24207119; [PMC3824127](https://pmc.ncbi.nlm.nih.gov/articles/PMC3824127)). Six were homozygous and seven compound heterozygous.

**Risk and protective factors.** No genetic modifiers, protective variants or gene-environment interactions are established (not retrieved). Water and mechanical friction visibly worsen the whitish, spongy change in lesional skin, but I found no formal exposure studies.

## 3. Phenotypes
Based on the clinical summaries above. Frequencies are not retrieved and should come from a case series or Orphanet.

| Phenotype | Suggested HPO lead (verify) |
|---|---|
| Palmoplantar keratoderma, diffuse | HP:0000982 |
| Palmoplantar erythema, well-demarcated | HP:0010783 (erythema) |
| Transgrediens to the dorsal hands/feet and Achilles area | no specific term (leave as a note) |
| Whitish, spongy change after water exposure (maceration) | no specific term |

- **Onset and course:** Onset is in infancy or early childhood (typical for NPPK; not confirmed from a retrieved source). Severity is mild to moderate, and the course is stable or slowly progressive.
- **Atypical presentation:** Extensive erythema and hyperkeratosis of the extremities and lumbar area has been reported ([Acta Derm Venereol 2016](https://medicaljournals.se/acta/content/html/10.2340/00015555-2391)).
- **Quality of life:** Not retrieved.

## 4. Genetic/molecular information
- **Gene:** SERPINB7 (chromosome 18q21.3). The OMIM entry for the disease is 615598.
- **Variants (Kubo 2013):**
  - The founder variant c.796C>T (p.Arg266*).
  - c.218_219del2ins12 (p.Gln73Leufs*17).
  - c.455-1G>A (p.Gly152Valfs*21).
  - c.309delT (p.Phe103Leufs*33).
  - c.336+2T>G.
- **Later reports:**
  - c.650_653delCTGT, in compound heterozygosity with c.796C>T in two brothers.
  - A homozygous c.522dupT (p.Val175Cysfs*46) in a Thai patient.
  - Novel c.530T>C and c.643A>G, from a 2022 Chinese series of eight patients that reviewed 15 pathogenic variants ([PMC9303684](https://pmc.ncbi.nlm.nih.gov/articles/PMC9303684)).
- **Consequence:** Loss of function. The reactive-site loop (residues 331–352) is predicted to be lost in all the truncating mutant proteins (PMID:24207119).
- **Population frequency:**
  - 1000 Genomes: c.796C>T was heterozygous in 2 of 89 Japanese individuals (about 0.4% allele frequency; PMID:24207119).
  - gnomAD, per ClinVar submissions: about 0.7–0.8% in East Asians (347/44,860 alleles in v4.0). I did not check gnomAD directly. The variant is 18-61471522-C-T ([ClinVar Miner](https://clinvarminer.genetics.utah.edu/submissions-by-variant/NM_003784.4%28SERPINB7%29%3Ac.796C%3ET%20%28p.Arg266Ter%29)).
- **Digenic or modifier genes, epigenetics, chromosomal abnormalities:** None reported (not retrieved).

## 5. Environmental information
No environmental or infectious causes were found. Water exposure is a clinical sign, not a cause: whitening and sponginess appeared within 10 minutes in lesional skin only (PMID:24207119).

## 6. Mechanism / pathophysiology
**Causal chain**
1. Biallelic loss-of-function SERPINB7 variants (nonsense, frameshift and splice-site) lead to loss of SERPINB7 protein. The reactive-site loop is lost, and protein signal is markedly reduced in patient skin (demonstrated; PMID:24207119).
2. This results in a complete loss of protease-inhibitory activity in the epidermis. The authors wrote of "a complete loss of the protease inhibitory activity of SERPINB7 in NPPK skin" (inferred from the predicted protein structure).
3. The proposed next step is overactive, unrestrained proteases in the stratum corneum, which weaken its structure. This is an inference and was not tested, and the target proteases are not identified (PMID:24207119).
4. Impaired barrier function follows. Transepidermal water loss was higher in lesional skin before and after water exposure (3 patients vs 3 controls; demonstrated, small sample).
5. The clinical result is erythema and hyperkeratosis of the palms and soles. These are likely reactive, because loricrin, involucrin and filaggrin staining and electron microscopy showed no major differentiation or ultrastructural defect.

**Details**
- **Localization:** SERPINB7 sits in the cytoplasm of the stratum granulosum and upper stratum corneum, with mild apical concentration. Staining was also seen in facial and abdominal epidermis. SERPINB7 was first described in kidney mesangial cells (as MEGSIN), but NPPK patients have no renal disease.
- **Cell types:** keratinocyte (CL:0000312) and granular-layer keratinocyte (verify the CURIE).
- **GO leads (verify):** serine-type endopeptidase inhibitor activity (GO:0004867); epidermis development (GO:0008544).
- **Open question:** A 2023 report suggests c.796C>T may alter SERPINB7's subcellular localization (Lyu et al., Exp Dermatol 32(6):766-776; I saw only the abstract).
- Molecular profiling, single-cell and CRISPR data: not retrieved.

## 7. Anatomical structures affected
- Palmar and plantar skin (UBERON:0001045 skin of hand; UBERON:0001046 skin of foot; verify). The disease extends onto the dorsa of the hands and feet and the Achilles area.
- Tissue and cell level: the epidermis, mainly the stratum granulosum and stratum corneum (UBERON:0000483 epithelium; UBERON:0002027 stratum corneum, verify).
- Subcellular level: the cytoplasm (GO:0005737).
- The disease is bilateral and symmetric.

## 8. Temporal development
Onset is in early life; the course is chronic and lifelong. Remission is not described. This section is mostly unsourced beyond the clinical summaries above.

## 9. Inheritance and population
- **Inheritance:** autosomal recessive (HP:0000007). Pseudodominant inheritance, from a high carrier frequency, has been reported in one Japanese family ([Fujita Health University](https://pure.fujita-hu.ac.jp/en/publications/highly-prevalent-serpinb7-founder-mutation-causes-pseudodominant-/)).
- **Prevalence (estimated by Kubo; PMID:24207119):** about 1.2 per 10,000 in Japanese, 3.1 per 10,000 in Chinese, and about 0.5 per 100,000,000 in non-Asian populations.
- **Founder effect:** c.796C>T is a founder variant in Japanese and Chinese populations. In a Chinese Han cohort of nine patients, five were homozygous for it and four were compound heterozygous ([Spandidos](https://www.spandidos-publications.com/mmr/14/5/4049)).
- **Geography:** Cases outside East Asia have been reported in France, Finland and Thailand ([PMC9303684](https://pmc.ncbi.nlm.nih.gov/articles/PMC9303684)).
- **Not retrieved:** sex ratio, penetrance and expressivity, and consanguinity role.

## 10. Diagnostics
- **Clinical:** the typical distribution, plus the whitening after water exposure.
- **Genetic:** SERPINB7 sequencing or a gene panel. Targeting c.796C>T first is efficient in East Asian patients.
- **Histology:** hyperkeratosis without a major differentiation defect.
- **Differential diagnosis:** other PPKs such as Unna-Thost and Mal de Meleda, and tinea. I did not source the distinguishing features.
- **Screening:** none established.

## 11. Outcome/prognosis
The disease is benign and non-syndromic, with no extracutaneous or renal involvement (PMID:24207119). Complications such as secondary infection and quality-of-life data are not retrieved.

## 12. Treatment
- No curative or approved disease-specific treatment was found. Standard care is topical keratolytics (urea, salicylic acid) and emollients, plus management of any superimposed infection. I did not source these, and the repo rules require a retrievable citation before any claim is curated.
- The 2023 Exp Dermatol report describes one homozygous patient who showed moderate improvement in keratinization on ixekizumab (an anti-IL-17A antibody). This is a single case and not evidence of efficacy.
- NCIT leads: Pharmacotherapy (NCIT:C15986) for any topical or systemic agent; Supportive Care (NCIT:C15747).
- Clinical trials: none found.

## 13. Prevention
Genetic counseling (NCIT:C15240) is appropriate. With a carrier rate near 0.7–0.8% in East Asians, a pseudodominant pattern in a family is possible. Other prevention items: not applicable.

## 14. Other species / natural disease
No naturally occurring analogue was found. Zebrafish homologs (serpinb1l1 and serpinb1l3) are expressed in the larval digestive tract ([ZFIN](https://www.zfin.org/ZDB-PUB-230212-44)). Mouse and other orthologs: not retrieved.

## 15. Model organisms
No mouse or other genetic model of NPPK was found. The zebrafish expression work above is descriptive only, not a disease model.

## Key references
- Kubo A, et al. Am J Hum Genet 2013;93:945–956. PMID:24207119.
- [Acta Derm Venereol 2016 (DOI 10.2340/00015555-2391)](https://medicaljournals.se/acta/content/html/10.2340/00015555-2391): PMID not retrieved.
- Lyu et al., Exp Dermatol 2023;32(6):766-776: PMID not retrieved.
- [Chinese Han cohort](https://www.spandidos-publications.com/mmr/14/5/4049); [2022 Chinese series](https://pmc.ncbi.nlm.nih.gov/articles/PMC9303684); [Fujita Health University pseudodominant report](https://pure.fujita-hu.ac.jp/en/publications/highly-prevalent-serpinb7-founder-mutation-causes-pseudodominant-/).

Sources:
- [Kubo 2013 (PMC3824127)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3824127)
- [GARD record](https://rarediseases.info.nih.gov/assets/singles/16967.json)
- [KEGG H02264](https://www.kegg.jp/entry/H02264)
- [ClinVar Miner](https://clinvarminer.genetics.utah.edu/submissions-by-variant/NM_003784.4%28SERPINB7%29%3Ac.796C%3ET%20%28p.Arg266Ter%29)
- [ZFIN](https://www.zfin.org/ZDB-PUB-230212-44)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0005737` (1 mention) - the report calls it "Subcellular level: the cytoplasm"; GO calls it **cytoplasm**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000982` (1 mention) - the report calls it "Palmoplantar keratoderma, diffuse"; HP calls it **Palmoplantar keratoderma**
- `CL:0000312` (1 mention) - the report calls it "Cell types:** keratinocyte"; CL calls it **keratinocyte**
- `NCIT:C15986` (1 mention) - the report calls it "NCIT leads: Pharmacotherapy"; NCIT calls it **Pharmacotherapy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.