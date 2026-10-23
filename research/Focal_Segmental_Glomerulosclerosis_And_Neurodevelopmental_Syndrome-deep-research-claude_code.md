---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T01:55:08.376417'
end_time: '2026-10-23T01:59:56.322673'
duration_seconds: 287.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Focal Segmental Glomerulosclerosis and Neurodevelopmental Syndrome
  mondo_id: MONDO:0100111
  category: Mendelian
  causal_genes: TRIM8
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
  - claude-opus-5-5
  web_search_requests: 7
  num_turns: 21
  total_cost_usd: 2.1936812000000003
  session_id: 8b0ae437-3d2d-418b-9fef-a8b60f475f04
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 12
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 29
  on_topic: 22
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0100111
    reported_labels:
    - MONDO
    ontology_label: focal segmental glomerulosclerosis and neurodevelopmental syndrome
  - term_id: GO:0016604
    reported_labels:
    - Subcellular:** nucleus and nuclear bodies
    ontology_label: nuclear body
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Focal Segmental Glomerulosclerosis and Neurodevelopmental Syndrome
- **MONDO ID:** MONDO:0100111 (if available)
- **Causal gene(s):** TRIM8
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

Please provide a comprehensive research report on **Focal Segmental Glomerulosclerosis and Neurodevelopmental Syndrome** covering all of the
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

I'm collecting the primary TRIM8 papers (Weng 2021, Assoum 2018, Warren 2020, and others) to confirm the PMIDs and pull exact abstract quotes.

The core literature is in hand. I'm checking whether the TRIM8 condensatopathy preprint has been formally published and what animal models it used, then I'll write the report.

# FSGS and Neurodevelopmental Syndrome (TRIM8; MONDO:0100111): Research Report

## Summary

This disorder is caused by **de novo heterozygous truncating variants in *TRIM8*** (tripartite motif-containing 8; HGNC:15579, written `hgnc:15579` in this repository; chromosome 10q24.32). TRIM8 is an E3 ubiquitin ligase. The disorder is autosomal dominant and links kidney disease (nephrotic syndrome, usually steroid-resistant, with focal segmental glomerulosclerosis) to brain disease (developmental delay with epilepsy, ranging from mild intellectual disability to early-onset epileptic encephalopathy).

All disease-causing variants found so far shorten the protein. They sit in the **last exon**, are predicted to escape nonsense-mediated decay, and therefore produce a protein missing its C-terminal intrinsically disordered region (IDR). The evidence does not support simple half-dosage of the gene (haploinsufficiency) as the mechanism. The leading model is that the truncated protein gains an abnormal function or interferes with the normal copy: it fails to form nuclear bodies (condensates), and its regulation by the proteasome and its TAK1/NF-κB signalling are disturbed.

**How the research was done.** PubMed tool access was denied in this session. Literature was found through web search, the PubMed website, and the Europe PMC REST API. The fetch tool would only return quotations under 125 characters, so the abstract quotes below are short exact excerpts. Every PMID listed was confirmed against a Europe PMC or PubMed record. **No ontology CURIE in this report was looked up during this session**, apart from MONDO:0100111 and HGNC:15579, which came from the task and the GenCC record. Look up each CURIE before binding it (see the Ontology Term Contract in CLAUDE.md).

---

## 1. Disease information

| Item | Value | Source |
|---|---|---|
| Name | Focal segmental glomerulosclerosis and neurodevelopmental syndrome | OMIM / MedGen |
| Abbreviation | FSGSNEDS | MedGen / [MalaCards](https://malacards.org/card/focal_segmental_glomerulosclerosis_and_neurodevelopmental_syndrome) |
| MONDO | MONDO:0100111 | Task input; [GenCC](https://search.thegencc.org/submissions/GENCC_000102-HGNC_15579-MONDO_0100111-HP_0000006-GENCC_100001) |
| OMIM (phenotype) | #619428 | [MedGen C5561938](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/bd92c530490f55ed2fd68cfd16ea8c327904c65c/www.ncbi.nlm.nih.gov/medgen/C5561938/index.html) |
| MedGen | C5561938 | same |
| Gene | *TRIM8* (HGNC:15579). Older alias GERP, used by Toniato 2002 | GenCC |
| Gene–disease validity | **Definitive, autosomal dominant** (GenCC) | [GenCC SGC-104565.2](https://thegencc.org/submissions/SGC-104565.2) |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code was found. Classify under the FSGS / SRNS parent terms | — |

**Synonyms in the literature:** TRIM8-related neuro-renal syndrome (NRS); TRIM8-associated nephrotic syndrome; TRIM8 epileptic encephalopathy. The epilepsy-first reports used the last name.

**What the evidence is made of:** individual patient case reports and case series, combined with one large case–control study (Weng 2021). There are no registry or EHR-level data.

**Key references (all PMIDs confirmed):**
- **Sakai 2016** (PMID:27346735, *Ann Hum Genet*, doi:10.1111/ahg.12157): "De Novo Truncating Mutation of TRIM8 Causes Early-Onset Epileptic Encephalopathy." A 10-year-old boy with severe developmental delay and early-onset epilepsy. TRIM8 is expressed in the postnatal mouse brain.
- **Assoum 2018** (PMID:30244534, *Am J Med Genet A*, doi:10.1002/ajmg.a.40357): "Further delineation of the clinical spectrum of de novo TRIM8 truncating mutations." Four patients with epileptic encephalopathy; one had nephrotic syndrome. All variants fall in the conserved C-terminus.
- **Warren 2020** (PMID:32193649, *Pediatr Nephrol*, doi:10.1007/s00467-020-04525-3): de novo nonsense variant with childhood-onset FSGS, developmental delay and seizures.
- **McClatchey 2020** (PMID:32531461, *Eur J Med Genet*, doi:10.1016/j.ejmg.2020.103972): FSGS with mild intellectual disability and well-controlled epilepsy.
- **Weng 2021** (PMID:33508234, *Am J Hum Genet*, doi:10.1016/j.ajhg.2021.01.008; [PMC7895901](https://pmc.ncbi.nlm.nih.gov/articles/PMC7895901)): the defining case–control study and functional work.
- **Shirai 2021** (PMID:34930159, *BMC Nephrol*, doi:10.1186/s12882-021-02626-1): FSGS **without** epileptic encephalopathy.
- **Li X 2022** (PMID:35903163, *Front Pediatr*); **Li W 2023** (PMID:37061734, *Ital J Pediatr*); **Sun 2023** (PMID:37643965, in Chinese); **Badeńska 2024** (PMID:38674071, *Int J Mol Sci*); **Lv 2024** (PMID:39416667, *Front Neurol*, review of 27 cases); **Luo 2024** (PMID:39669799); **Rahman 2025** (PMID:39708126); **Leventoğlu 2025** (PMID:41219125).

---

## 2. Etiology

- **Cause:** a germline de novo heterozygous truncating variant in the last exon of *TRIM8*. Weng 2021, quoted exactly:
  - "detecting eight heterozygous TRIM8 truncating variants in affected subjects but none in control subjects" (p = 3.28 × 10⁻¹¹)
  - "In all six cases with available parental DNA, we demonstrated de novo inheritance" (p = 2.21 × 10⁻¹⁵)
  - The cohort was "2,501 pediatric FSGS/SRNS-affected individuals", compared with 48,556 controls.
- **Genetic risk factors:** none beyond the causal variant. No modifier genes or GWAS loci are reported.
- **Environmental risk factors, protective factors, gene–environment interactions:** none reported. Not applicable.
- **Recurrence risk:** low for parents of a de novo case. Germline mosaicism has not been reported but cannot be excluded (standard counselling caveat). An affected individual's child would have a 50% risk.

## 3. Phenotypes

Frequencies are from Weng 2021 (n = 12 families) unless noted. Lv 2024 reviewed 27 patients.

| Phenotype | Frequency / features | Suggested HPO term (**verify before binding**) |
|---|---|---|
| Nephrotic-range proteinuria / nephrotic syndrome | 12/12. Onset from birth to 13.7 years, usually after the neurological signs | Nephrotic syndrome HP:0000100; Proteinuria HP:0000093 |
| Steroid resistance | "SRNS developed in 8 of 12 subjects" | Steroid-resistant nephrotic syndrome (search HPO) |
| FSGS on biopsy | 10/12 biopsies | Focal segmental glomerulosclerosis HP:0000097 |
| Diffuse mesangial sclerosis | 2/12 | Diffuse mesangial sclerosis HP:0001967 |
| Podocyte foot process effacement; GBM thinning, lamellation and blebbing on EM | Index case: "extensive foot process effacement and distinctive alterations of the glomerular basement membrane." Rahman 2025 reports a biopsy that mimicked a collagenopathy | Search HPO for "foot process effacement" and "glomerular basement membrane" |
| CKD progressing to kidney failure | Common. Kidney failure from about 1 to 20 years; 5/12 transplanted | Chronic kidney disease HP:0012622; Stage 5 CKD HP:0003774 |
| Developmental delay | Essentially universal (Weng: "neurodevelopmental disease in all eight families"). Onset under 1 year to 2.5 years | Global developmental delay HP:0001263 |
| Intellectual disability | Mild (McClatchey 2020) to severe | Intellectual disability HP:0001249 |
| Epilepsy / epileptic encephalopathy | 11/12. Onset under 1 year to 4.5 years; often drug-resistant in the epilepsy-first series (Assoum 2018: onset 2 months to 3.5 years) | Seizure HP:0001250; Epileptic encephalopathy HP:0200134 |
| Developmental regression | Reported (Assoum 2018) | Developmental regression HP:0002376 |
| Brain atrophy | "Brain atrophy was observed in six of eight individuals with available imaging" | Cerebral atrophy (search HPO) |
| Thin corpus callosum, posterior fossa dilatation, mesial temporal sclerosis | Single cases | search HPO |
| Hypotonia, autism, secondary microcephaly, spastic-dystonic quadriplegia | Single cases | Hypotonia HP:0001252; Autistic behavior HP:0000729; Secondary microcephaly HP:0005484 |
| Recurrent infections | One case (Assoum 2018) | Recurrent infections HP:0002719 |
| Neurogenic bladder | Li W 2023; Luo 2024 | Neurogenic bladder HP:0000011 |
| Medullary sponge kidney–like features | Single case (Leventoğlu 2025) | search HPO |

**Effect on quality of life:** severe, from refractory epilepsy, intellectual disability and the burden of dialysis or transplantation. No formal quality-of-life studies exist.

**How the phenotype relates to variant position** (Lv 2024, PMID:39416667, exact quotes):
- "Two patients with TRIM8 variants closer to the N-terminal had neurological diseases without renal damage."
- "Five patients with TRIM8 variants closer to the C-terminal had no severe neurological diseases."
- "Seven patients had Gln459* variant which is the most common variant (7/27, 25.9%)."
- "Neurological and renal phenotype with the same variant locus differed in their severity."

Li W 2023 (PMID:37061734): "as the TRIM8 variant became closer to the C-terminal, the renal lesions became more prominent".

## 4. Genetic and molecular information

- **Gene:** *TRIM8*, NM_030912 / NP_112174.2, 551 amino acids. Domains: RING, B-box and coiled-coil, followed by a C-terminal IDR. The OMIM gene number was not checked in this session.
- **Variant class:** nonsense or frameshift, all in the last exon. Weng 2021: "All TRIM8 variants cause protein truncation clustering within the last exon between residues 390 and 487". The transcripts "are predicted to escape nonsense-mediated decay".
- **Reported variants** (Weng 2021): c.1163delT p.(Phe388Serfs\*2); c.1201_1202delinsTA p.(Gly401\*); c.1231C>T p.(Gln411\*); c.1240C>T p.(Gln414\*); c.1267C>T p.(Gln423\*); c.1333C>T p.(Gln445\*); **c.1375C>T p.(Gln459\*)** (recurrent hotspot); c.1380T>A or T>G p.(Tyr460\*); c.1461C>G p.(Tyr487\*). Shirai 2021 reports c.1461C>A p.(Tyr487\*).
- **Origin:** germline, de novo. No somatic or mosaic cases have been reported.
- **Population frequency:** absent from gnomAD. gnomAD carries **earlier (N-terminal) truncating** variants in people without the syndrome, which argues against haploinsufficiency (Weng 2021).
- **Functional effect:** the truncated protein lacking its C-terminus is expected to be stable. A gain of function, toxic effect or dominant-negative effect is favoured over loss of function (see §6).
- **ClinVar / ACMG:** most published variants are de novo truncations absent from controls and are classifiable as pathogenic. Individual ClinVar records were not retrieved in this session.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported.

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious factors are reported.

## 6. Mechanism and pathophysiology

### Causal chain

1. **A de novo truncating variant in the last *TRIM8* exon** escapes nonsense-mediated decay, so a C-terminally truncated TRIM8 protein is made. This step is inferred from the variant position and NMD rules, not demonstrated in patient tissue.
2. **Loss of the C-terminal IDR stops TRIM8 forming nuclear bodies (condensates).** Weng 2021: "Wild-type TRIM8 overexpressed in immortalized human podocytes and neuronal cells localized to nuclear bodies", whereas "constructs harboring patient-specific variants mislocalized diffusely to the nucleoplasm". This is in vitro evidence. In the same study, wild-type TRIM8 was in nuclear bodies in 94% of cells, and Gemini and Cajal bodies often sat next to the TRIM8 bodies.
3. **The mislocalized truncated protein disturbs proteasomal turnover and TAK1/NF-κB signalling.** The Singh/Majmundar/Hyman preprint (bioRxiv doi:10.1101/2025.01.02.630836, **not peer reviewed**, PMID:40034645) states that "disease-causing truncations of the TRIM8 C-terminal IDR result in a condensatopathy" marked by "disrupted condensation, proteasomal regulation, and TAK1/NFκB signaling."
   - A separate abstract from the same lab (Rubin et al., Boston University; not peer reviewed) reports that the variant proteins do not accumulate after the proteasome inhibitor MG132 the way wild-type TRIM8 does, and that they co-immunoprecipitate with wild-type TRIM8. This fits a dominant-negative or gain-of-function effect.
   - Background on normal TRIM8 function: it drives TNFα- and IL-1β-triggered NF-κB activation by adding K63-linked polyubiquitin to TAK1 (Li 2011, PMID:22084099). It binds SOCS1 (Toniato 2002, PMID:12163497). It binds p53 and stops MDM2 binding it: "TRIM8 physically interacted with p53, impairing its interaction with MDM2" (Caratozzolo 2012, PMID:22262183).
4. **Branch A, kidney:** TRIM8 is "predominantly expressed in podocytes" by single-cell RNA-seq (Weng 2021). Disturbed TRIM8 signalling leads to podocyte dysfunction and "impaired response to injury" (preprint; cell and animal models). This produces foot process effacement and GBM changes, then nephrotic-range proteinuria (usually steroid-resistant), then FSGS or diffuse mesangial sclerosis, then progressive CKD and kidney failure.
   - Shirai 2021 and Warren 2020 found little TRIM8 and strong SOCS1 staining in patient kidney. This hints that SOCS1 builds up when TRIM8 fails, but the evidence is correlational only.
5. **Branch B, brain:** TRIM8 is expressed in neurons (postnatal mouse brain, Sakai 2016; neuronal cells, Weng 2021). Its disruption there is **inferred** to cause developmental delay, epilepsy and brain atrophy. No neuronal mechanism has been demonstrated.

**Evidence against haploinsufficiency:**
- gnomAD carriers of N-terminal truncations are unaffected.
- Knocking down both zebrafish paralogs (*trim8a* and *trim8b*) produced no kidney phenotype (Weng 2021).

**Suggested ontology terms (verify each before binding):**
- GO: nuclear body GO:0016604; protein K63-linked ubiquitination GO:0070534; positive regulation of canonical NF-κB signal transduction GO:0043123; ubiquitin-protein transferase activity GO:0004842. Search GO for a membraneless-organelle-assembly term.
- CL: podocyte CL:0000653; neuron CL:0000540.

**Molecular profiling:** no patient transcriptomic, proteomic, metabolomic or single-cell disease datasets were found. The podocyte enrichment comes from normal-kidney single-cell data.

## 7. Anatomical structures

- **Primary organs:** kidney glomerulus (UBERON:0000074), specifically the visceral epithelium (podocytes) and the glomerular basement membrane; brain (UBERON:0000955), including cerebral cortex, corpus callosum and mesial temporal structures.
- **Secondary:** bladder (neurogenic bladder).
- **Subcellular:** nucleus and nuclear bodies (GO:0016604). Some nuclear foci also appear in proximal tubular epithelium.
- **Laterality:** bilateral and systemic.

## 8. Temporal development

- **Onset:** neurological features first, from infancy to 4.5 years. Kidney disease is diagnosed later or at the same time: Weng 2021, "All subjects were diagnosed with renal disease after (10/12) or at the time of (2/12)" the neurological disease. Proteinuria appears from birth to adolescence; one patient was diagnosed at 17 (Badeńska 2024).
- **Course:** chronic and progressive. Kidney function often declines to kidney failure (reported from about 1 to 20 years). Some patients have only transient or stable proteinuria.
- **Remission:** steroid-induced remission is uncommon.
- **Window for intervention:** screening children with TRIM8 epileptic encephalopathy for proteinuria (McClatchey 2020) allows earlier renoprotective treatment.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant, almost always de novo. A curation entry would bind autosomal dominant inheritance (HP:0000006, the term in the GenCC record).
- **Penetrance and expressivity:** apparently complete for some neurological involvement in C-terminal truncations, with **variable expressivity**. Some patients are kidney-predominant (Shirai 2021, Li W 2023); patients with variants nearer the N-terminus may have neurological disease only.
- **Recurrent variant:** p.Gln459\* is the hotspot (7/27 patients) and is found across unrelated ancestries.
- **Epidemiology:** ultra-rare. About 27 patients were published by 2024 (Lv 2024), and GenCC cites 20 or more. TRIM8 variants accounted for 8 of 2,501 (about 0.3%) of a pediatric FSGS/SRNS cohort. No prevalence figure exists; the measure is cases in the literature.
- **Sex ratio, founder effects, consanguinity:** no sex bias is apparent. No founder effects. Consanguinity plays no role.

## 10. Diagnostics

- **Laboratory tests:** urine protein-to-creatinine ratio, serum albumin, creatinine and eGFR.
- **Kidney biopsy:** FSGS or diffuse mesangial sclerosis. EM shows foot process effacement and GBM thinning or lamellation, which can mimic a type IV collagen disease (Rahman 2025).
- **Neurology:** EEG (variable epileptiform patterns) and brain MRI (atrophy, thin corpus callosum).
- **Genetic testing:** exome or genome sequencing, or an SRNS or epilepsy gene panel that includes *TRIM8*. Warren 2020 recommends TRIM8 testing in children with FSGS and CNS abnormalities. Li X 2022 recommends genetic testing in children with steroid-resistant significant proteinuria.
- **Differential diagnosis:**
  - Galloway-Mowat syndrome (WDR73, the KEOPS complex genes, NUP genes): usually congenital microcephaly.
  - Action myoclonus-renal failure syndrome (SCARB2).
  - Mitochondrial and COQ10-biosynthesis nephropathies.
  - Alport syndrome and other collagen IV nephropathies (similar GBM changes).
  - Other monogenic SRNS genes (NPHS1, NPHS2, WT1).
- **Screening:** no newborn or carrier screening applies. Prenatal or preimplantation testing is available only for recurrence concerns.

## 11. Outcome and prognosis

- About 40% (5/12) needed kidney transplantation. **FSGS did not recur after transplant** in any of them, with follow-up of up to 24 years (Weng 2021); one patient had rejection.
- The neurological outlook depends on how severe the epilepsy is. Assoum 2018 noted that the variation between patients "appeared related to the severity of the epilepsy".
- No survival or mortality data are available.
- Prognostic factors: variant position (C-terminal variants are more kidney-predominant) and whether steroid resistance develops.

## 12. Treatment

There is no disease-specific therapy. Treatment is supportive.

| Treatment | Notes | Suggested NCIT / CHEBI (verify) |
|---|---|---|
| Kidney transplantation | Effective, with no recurrence (Weng 2021) | Organ Transplantation NCIT:C15289 |
| Dialysis | For kidney failure | search NCIT "Dialysis" |
| Renoprotective RAAS blockade (ACE inhibitor or ARB) | Standard SRNS supportive care. No TRIM8-specific evidence | Pharmacotherapy NCIT:C15986 + agent |
| Corticosteroids and calcineurin inhibitors | Most patients are steroid-resistant, so giving immunosuppression to a patient with a genetic diagnosis may expose them to toxicity with little chance of benefit | Pharmacotherapy NCIT:C15986 |
| Antiseizure medications | Often drug-resistant | Pharmacotherapy NCIT:C15986; anticonvulsant (search CHEBI) |
| Developmental, physical and speech therapy | Supportive | Physical Therapy NCIT:C15302; Rehabilitation NCIT:C15315 |
| Genetic counselling | De novo recurrence counselling | Genetic Counseling NCIT:C15240 |

- **Experimental options:** no clinical trials were found. The condensate and TAK1/NF-κB findings suggest targets, but these are only hypotheses.
- **Pharmacogenomics:** not applicable.

## 13. Prevention

- **Primary prevention:** not applicable. Variants arise de novo.
- **Secondary prevention:** proteinuria screening in children with TRIM8 neurodevelopmental disease. An early genetic diagnosis avoids prolonged immunosuppression.
- **Tertiary prevention:** renoprotection, seizure control and transplant planning.
- **Counselling:** recurrence risk is low (germline mosaicism caveat); an affected individual's child has a 50% risk.

## 14. Other species

No naturally occurring disease has been reported (no OMIA entry found). TRIM8 is conserved in vertebrates: mouse *Trim8*, and the zebrafish paralogs *trim8a* and *trim8b*. A fish TRIM8 study describes antiviral and inflammatory roles (Huang 2016, PMID:27150052); this is not a disease model.

## 15. Model organisms

- **Zebrafish:** knocking down both *trim8a* and *trim8b* with morpholinos caused **no kidney phenotype** (Weng 2021). This is a negative result that argues against haploinsufficiency. Morpholino knockdown does not model a truncation that gains a function, so the model does **not** reproduce the human disease mechanism. A curation entry would record this as a model that fails to recapitulate the disease or as a human–model mismatch.
- **Cell models:** immortalized human podocytes and neuronal cells overexpressing wild-type or truncated TRIM8 (Weng 2021; Singh 2025 preprint). These reproduce the nuclear-body mislocalization.
- **Animal models in the 2025 preprint:** the abstract says only "cellular and animal models" and does not name the species.
- **No knock-in mouse** carrying a patient-like C-terminal truncation has been published. This is the main gap in modelling the disease.

---

## Key gaps

1. How truncated TRIM8 causes disease *in vivo* (gain of function or dominant negative) has not been settled in peer-reviewed work. The condensatopathy data are a preprint.
2. No neuronal mechanism for the epilepsy has been described.
3. The SOCS1, p53 and NF-κB links in patient tissue are correlational.
4. There is no knock-in animal model and no natural-history cohort.

## Sources

- Weng et al. 2021, PMID:33508234: [PMC7895901](https://pmc.ncbi.nlm.nih.gov/articles/PMC7895901)
- [GenCC SGC-104565.2](https://thegencc.org/submissions/SGC-104565.2); [GenCC MONDO:0100111 record](https://search.thegencc.org/submissions/GENCC_000102-HGNC_15579-MONDO_0100111-HP_0000006-GENCC_100001)
- Assoum 2018, PMID:30244534: [HAL](https://hal-univ-bourgogne.archives-ouvertes.fr/hal-01990608)
- Li X 2022, PMID:35903163: [Frontiers in Pediatrics](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2022.918373/full)
- Shirai 2021, PMID:34930159: [PMC8686241](https://pmc.ncbi.nlm.nih.gov/articles/PMC8686241)
- Singh et al. 2025 preprint: [bioRxiv 10.1101/2025.01.02.630836](https://www.biorxiv.org/content/10.1101/2025.01.02.630836v1)
- Boston University abstracts, not peer reviewed: [Dissecting disease pathways of TRIM8-associated nephrotic syndrome](https://open.bu.edu/items/1dbb0eca-05f6-49c8-9f70-647f95559609); [Rubin et al.](https://open.bu.edu/items/71e13d17-7617-448e-8267-ed727b3ffd92); [Modeling the impact of variants in TRIM8](https://open.bu.edu/items/a2852940-dfb5-482f-898c-6a029f995afe)
- [MedGen C5561938 / OMIM 619428](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/bd92c530490f55ed2fd68cfd16ea8c327904c65c/www.ncbi.nlm.nih.gov/medgen/C5561938/index.html); [MalaCards](https://malacards.org/card/focal_segmental_glomerulosclerosis_and_neurodevelopmental_syndrome)
- PubMed records via Europe PMC: 27346735, 32193649, 32531461, 37061734, 39416667, 38674071, 39669799, 39708126, 41219125, 22084099, 12163497, 22262183, 27150052

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 29 |
| On topic | 22 |
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
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100111` (4 mentions) - the report calls it "MONDO"; MONDO calls it **focal segmental glomerulosclerosis and neurodevelopmental syndrome**
- `GO:0016604` (2 mentions) - the report calls it "Subcellular:** nucleus and nuclear bodies"; GO calls it **nuclear body**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000074` (1 mention) - the report calls it "Primary organs:** kidney glomerulus"; UBERON calls it **renal glomerulus**, and lists "Malphigian glomerulus" among its other names