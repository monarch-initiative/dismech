---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-23T21:11:50.836452'
end_time: '2026-10-23T21:13:36.731958'
duration_seconds: 105.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spermatogenic Failure 68
  mondo_id: MONDO:0030721
  category: Mendelian
  causal_genes: CATSPERT
  omim_id: OMIM:619805
  synonyms: SPGF68
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
  web_search_requests: 5
  num_turns: 12
  total_cost_usd: 0.9382246999999998
  session_id: 7cf4d4d2-202c-5e35-b74d-6f65c6e8bfd8
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 6
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0034307
    reported_labels:
    - Globozoospermia
    ontology_label: Elevated left ventricular end-diastolic diameter
  unresolvable_prefixes:
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 68
- **MONDO ID:** MONDO:0030721 (if available)
- **Causal gene(s):** CATSPERT
- **OMIM:** OMIM:619805
- **Synonyms:** SPGF68
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 68** covering all of the
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

Still working: I'm looking up PMIDs for the key papers on Europe PMC, then I'll write the report.

# Spermatogenic Failure 68 (SPGF68; MONDO:0030721; OMIM:619805): CATSPERT-related globozoospermia

**Reliability.** The human evidence for this disease is a single reported patient. I verified the mouse biology from search-result abstracts and snippets. I could not open OMIM, GeneCards or PubMed directly, because the proxy refused those connections. Quotes below are paraphrases of search-result text, not verified abstract quotes. Before any quote goes into a snippet, run `just fetch-reference` and check it against the cache. I did not confirm the PMID for Oud et al. 2020. I did not verify MONDO, HGNC, HPO, GO or UBERON identifiers, so look each one up before binding it.

## 1. Disease information

SPGF68 is an autosomal recessive male infertility disorder. It is caused by a homozygous missense variant in **CATSPERT**, the gene whose older symbols are **C2CD6** and **ALS2CR11**. The gene encodes CatSperτ (tau), an auxiliary subunit of the sperm CatSper calcium channel. OMIM's gene entry is *619776 (C2CD6) ([OMIM](https://www.omim.org/entry/619776)). The phenotype entry is #619805.

- **Phenotype:** normal sperm count but globozoospermia. The sperm are round-headed and lack an acrosome. Some patients have a mix of acrosomeless sperm and sperm with a small or detached acrosome (acrosomal hypoplasia) ([MalaCards](https://malacards.org/card/spermatogenic_failure_68), [GeneCards](https://www.genecards.org/card/CATSPERT)).
- **Evidence base:** OMIM and the Disease Ontology rest this entry on one Moroccan man. The Disease Ontology notes only one patient as of 2024. A 2025 Tunisian globozoospermia study lists C2CD6 only as a candidate gene needing functional confirmation ([Springer](https://link.springer.com/article/10.1186/s43043-025-00235-8)).
- **Synonym:** SPGF68. A related GeneCards disease label is "male infertility due to globozoospermia".
- **Data source:** this is aggregated disease-level information. It does not come from EHR data.
- **Naming trap:** the SPGF serial number does not say which gene is involved, and this gene is not one of the other CATSPER genes. CATSPER1 and CATSPER2 variants cause different entries, such as CATSPER1-related nonsyndromic male infertility and the deafness-infertility syndrome from a CATSPER2–STRC deletion. They are not SPGF68 ([MedlinePlus](https://medlineplus.gov/genetics/condition/catsper1-related-nonsyndromic-male-infertility)). Also keep it apart from the CATSPERθ (CATSPERTHETA) work ([PNAS 2023, PMID 37725640](https://www.pnas.org/doi/10.1073/pnas.2304409120)).

## 2. Etiology

- **Cause:** a homozygous germline variant in CATSPERT/C2CD6 (human genomic location 2q33.1).
- **Genetic risk and protective factors, and gene–environment interaction:** none reported.
- **Environmental factors:** none reported for this entry.

## 3. Phenotypes

The report rests on one patient, so there are no frequencies. HPO suggestions (look each up before binding):

| Phenotype | Type | Suggested HPO term |
|---|---|---|
| Male infertility | Clinical | Male infertility (HP:0003251) |
| Globozoospermia (round-headed, acrosomeless sperm) | Laboratory (semen analysis) | Globozoospermia (HP:0034307) |
| Acrosomal hypoplasia in some sperm | Laboratory | Look up |
| Normal sperm count | Laboratory | Not applicable (a normal finding) |

- **Onset and course:** onset is adult, at the age of attempted conception. Severity is infertility. The disorder is not progressive. No syndromic features are reported.
- **Quality of life:** not reported.

## 4. Genetic and molecular information

- **Gene:** CATSPERT (HGNC lowercase form in the KB; look up the ID). Old symbols are C2CD6 and ALS2CR11.
- **Variant:** NM_001168221.2:c.338A>G, p.His113Arg (H113R). It is homozygous and missense. ClinVar variation ID 1345025 ([ClinVar](https://ncbi.nlm.nih.gov/clinvar/variation/1345025/?new_evidence=true)).
- **Site and frequency:** the histidine is conserved, in the C2 domain. The variant is absent from gnomAD.
- **Discovery:** exome sequencing of a globozoospermia cohort (Oud et al., Hum Reprod 2020; 35(1):240–252, [OUP](https://academic.oup.com/humrep/article/35/1/240/5715929)).
- **Segregation:** not reported.
- **Origin:** germline.
- **Mechanism class:** presumed loss of function. This is an inference from the mouse knockout, not demonstrated for H113R. No functional study of H113R is known to me.
- **Modifier genes, epigenetic changes, chromosomal abnormalities:** none reported.

## 5. Environmental information

None reported. There are no infectious agents and no lifestyle factors.

## 6. Mechanism and pathophysiology

**Causal chain** (steps 3 to 6 come from mouse data, and step 2 is inferred):

1. A homozygous CATSPERT c.338A>G (p.His113Arg) variant changes a conserved residue in the C2 domain of CatSperτ.
2. This presumably impairs CatSperτ function or stability. This is not demonstrated for H113R.
3. In mouse, CatSperτ is a membrane-associating C2-domain protein that reaches the flagellum on its own. It targets the CatSper channel into the quadrilinear Ca²⁺-signaling nanodomains of the sperm flagellar membrane. It is not needed for the channel to assemble ([Hwang et al., Cell Rep 2022, PMID 34998468](https://www.cell.com/cell-reports/pdf/S2211-1247(21)01730-7.pdf)).
4. Without CatSperτ, the knockout sperm form a functional CatSper channel only at significantly reduced levels. The sperm conduct Ca²⁺ but fail to hyperactivate ([bioRxiv](https://www.biorxiv.org/content/10.1101/2021.08.16.456347v1.full)). A separate preprint reports C2CD6 as essential for CatSper complex assembly ([Yang et al., bioRxiv](https://www.biorxiv.org/content/10.1101/2021.07.06.451342.full.pdf)). The two groups differ on whether the channel assembles.
5. Failed hyperactivation leads to failed fertilization in vitro and in vivo, so the male is infertile.
6. The mouse knockouts have no reported acrosome defect, but the human patient has globozoospermia. This is an unresolved mismatch.

**Terms to consider** (verify before binding):
- GO: sperm flagellum, cation channel complex, sperm hyperactivation, calcium ion transmembrane transport.
- CL: spermatozoon, spermatid.
- UBERON: testis, sperm flagellum principal piece.
- CatSper is a principal piece protein complex.

**Immune, metabolic and omics findings:** none reported.

## 7. Anatomical structures affected

- **Organ:** testis (spermatogenesis and sperm morphology).
- **Cells:** spermatids and spermatozoa.
- **Subcellular:** acrosome, sperm head and flagellar membrane.
- **Lateralization:** not applicable.
- **Other organs:** none. No syndromic features are reported.

## 8. Temporal development

The disease is congenital as a genetic condition but is detected in adulthood, through male factor infertility. It is stable and lifelong. No remission is reported.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive. The one patient was homozygous.
- **Population:** one Moroccan man. Consanguinity, founder effect, penetrance, expressivity, prevalence and carrier frequency are not reported.
- **Sex and age:** male only. Adults.

## 10. Diagnostics

- **Semen analysis:** normal sperm count with globozoospermia. Acrosomeless sperm can be confirmed by Papanicolaou staining or acrosome-marker staining, and by electron microscopy.
- **Genetic testing:** exome sequencing or a globozoospermia or male-infertility gene panel. Panel inclusion of CATSPERT varies, so check with the laboratory.
- **Differential diagnosis:** DPY19L2-related globozoospermia is the main genetic cause. Others include GGN and further candidate genes ([Celse et al., Hum Genet 2021, PMID 33108537](https://www.researchgate.net/publication/344914303_Genetic_analyses_of_a_large_cohort_of_infertile_patients_with_globozoospermia_DPY19L2_still_the_main_actor_GGN_confirmed_as_a_guest_player)). Also exclude other CatSper-gene disorders.
- **Functional tests:** CatSper function can be assessed in patient sperm. One preprint argues that defective CatSper function is a frequent cause of unexplained infertility ([medRxiv 2023](https://www.medrxiv.org/content/10.1101/2023.03.23.23286813.full.pdf)), but it is not peer-reviewed.

## 11. Prognosis

Natural fertility is unlikely. Other health is not reported to be affected. Prognosis for conception depends on assisted reproduction, below.

## 12. Treatment

No treatment is specific to SPGF68. No clinical trials are known to me.

- **Standard care for globozoospermia:** intracytoplasmic sperm injection (ICSI), sometimes with assisted oocyte activation. For this gene there is no outcome data. For globozoospermia in general, ICSI results are often poor because of fertilization failure. Check the systematic review ([Crafa et al., World J Mens Health 2023, PMID 36047070](https://pubmed.ncbi.nlm.nih.gov/36047070/)) before citing.
- **Mouse rescue:** OMIM's gene entry says sterility was transiently rescued with a calcium ionophore, starvation, or both. I did not verify this directly.
- **Counseling:** genetic counseling.
- **NCIT terms:** look up the terms for intracytoplasmic sperm injection and genetic counseling. The CLAUDE.md lists `NCIT:C15240` for genetic counseling.

## 13. Prevention

- **Prevention levels:** primary and secondary prevention do not apply, since the disease is recessive and congenital.
- **Screening:** carrier screening is not established.
- **Reproductive options:** genetic counseling and family testing if the variant is known.

## 14. Other species and natural disease

No natural disease is documented. The mouse ortholog is Catspert (MGI:1920713 per search results; verify), with NCBI Taxon 10090 for mouse. OMIA coverage was not checked.

## 15. Model organisms

- **Mouse knockouts:** male C2cd6/Catspert knockout mice are sterile. They show defective hyperactivation and fail fertilization in vitro and in vivo. OMIM attributes this to two groups, Yang et al. and Hwang et al. ([Cell Rep 2022, PMID 34998468](https://www.cell.com/cell-reports/pdf/S2211-1247(21)01730-7.pdf); [Yang et al. bioRxiv](https://www.biorxiv.org/content/10.1101/2021.07.06.451342.full.pdf)). I did not find a published journal version of the Yang paper.
- **Evidence type:** `MODEL_ORGANISM`.
- **Fidelity:** male infertility is reproduced. Globozoospermia (the human hallmark) was not described in the mouse results I saw. Suggest a `HUMAN_MODEL_MISMATCH` discussion, with `PARTIALLY_RECAPITULATES`.
- **Related CatSper knockouts:** Catsper1, Catsper2, Catsper3 and Catsper4 knockouts also cause infertility with impaired hyperactivation ([PubMed 14657366](https://pubmed.ncbi.nlm.nih.gov/14657366/); [Biol Reprod 2007](https://bioone.org/journals/biology-of-reproduction/volume-77/issue-1/biolreprod.107.060186.full)). Reviews: [Hwang & Chung, Physiology 2023, PMID 36512352](https://pubmed.ncbi.nlm.nih.gov/36512352/).

## Gaps to resolve before curating

1. Fetch Oud et al. 2020, find its PMID, and quote the CATSPERT/C2CD6 patient description (genotype, semen findings, ICSI history).
2. Confirm the gene symbol and HGNC ID, and check whether OMIM #619805 now cites more patients.
3. Resolve why a human acrosome defect appears with a mouse hyperactivation defect, and look for any functional data on H113R.
4. Check the GeneReviews and ClinGen baselines. I did not search either, and I did not find a GeneReviews chapter.

## Sources

- [OMIM 619776 (C2CD6)](https://www.omim.org/entry/619776)
- [MalaCards SPGF68](https://malacards.org/card/spermatogenic_failure_68)
- [GeneCards CATSPERT](https://www.genecards.org/card/CATSPERT)
- [Oud et al., Hum Reprod 2020](https://academic.oup.com/humrep/article/35/1/240/5715929)
- [ClinVar 1345025](https://ncbi.nlm.nih.gov/clinvar/variation/1345025/?new_evidence=true)
- [Hwang et al., Cell Rep 2022](https://www.cell.com/cell-reports/pdf/S2211-1247(21)01730-7.pdf)
- [Yang et al., bioRxiv 2021](https://www.biorxiv.org/content/10.1101/2021.07.06.451342.full.pdf)
- [Celse et al., Hum Genet 2021](https://www.researchgate.net/publication/344914303_Genetic_analyses_of_a_large_cohort_of_infertile_patients_with_globozoospermia_DPY19L2_still_the_main_actor_GGN_confirmed_as_a_guest_player)
- [Crafa et al., World J Mens Health 2023](https://pubmed.ncbi.nlm.nih.gov/36047070/)
- [Hwang & Chung, Physiology 2023](https://pubmed.ncbi.nlm.nih.gov/36512352/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0034307` (1 mention) - the report calls it "Globozoospermia"; HP calls it **Elevated left ventricular end-diastolic diameter**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.