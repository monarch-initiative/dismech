---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-09T00:42:51.805006'
end_time: '2026-11-09T00:47:07.122375'
duration_seconds: 255.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Nephrotic Syndrome Type 3
  mondo_id: MONDO:0012546
  category: Mendelian
  causal_genes: PLCE1
  omim_id: OMIM:610725
  synonyms: PLCE1 nephrotic syndrome; nephrotic syndrome caused by mutation in PLCE1
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
  num_turns: 15
  total_cost_usd: 2.4186071
  session_id: d93ce688-7888-4e75-b1ae-1a561a11ac9b
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 23
  validator_version: 0.5.1
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: CL:0000650
    reported_labels:
    - site of matrix expansion in DMS
    ontology_label: mesangial cell
  - term_id: GO:0004435
    reported_labels:
    - molecular function
    ontology_label: phosphatidylinositol-4,5-bisphosphate phospholipase C activity
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nephrotic Syndrome Type 3
- **MONDO ID:** MONDO:0012546 (if available)
- **Causal gene(s):** PLCE1
- **OMIM:** OMIM:610725
- **Synonyms:** PLCE1 nephrotic syndrome; nephrotic syndrome caused by mutation in PLCE1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Nephrotic Syndrome Type 3** covering all of the
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

Still working: an entry for this disease already exists in the KB, so I'm reading the abstracts it cites from the local reference cache to get exact quotes.

Still gathering abstracts — one more batch covering the PLCE1 interaction partners and the later cohort studies, then I'll write the report.

# Nephrotic Syndrome Type 3 (NPHS3; PLCE1-related nephrotic syndrome): research report

**Target:** MONDO:0012546, OMIM:610725. **Causal gene:** *PLCE1* (phospholipase C epsilon 1). Inheritance is autosomal recessive.

**How the sources were handled.**
- One reference was read in full: PMID:29058690, from the local `references_cache/`.
- For the other PubMed records, quotes come from abstracts retrieved through NCBI E-utilities. Each quote is under 125 characters. They were extracted by a summarising fetch tool, so treat them as close to exact but still run them through `just fetch-reference` and `just count-verified-snippets` before using them as KB snippets.
- None of the ontology CURIEs below was looked up in this session. Under the repository's term contract they are **leads to verify with `runoak` or `just validate-terms`**, not bindings.
- The KB already has a skeleton entry, `kb/disorders/Nephrotic_Syndrome_Type_3.yaml`. It holds only the name, MONDO term and synonyms.

---

## 1. Disease information

NPHS3 is an autosomal recessive podocytopathy. Biallelic loss-of-function variants in **PLCE1** cause early-onset nephrotic syndrome. The typical kidney histology is **diffuse mesangial sclerosis (DMS)**; a minority of patients have **focal segmental glomerulosclerosis (FSGS)**. Most patients progress to end-stage kidney disease (ESKD) in early childhood. A small number of patients have responded to steroids or calcineurin inhibitors, which made NPHS3 the first monogenic nephrotic syndrome reported as potentially reversible.

- Hinkes et al. 2006 (PMID:17086182, *Nat Genet*): "we identified mutations in the phospholipase C epsilon gene (PLCE1) as causing early-onset nephrotic syndrome"
- PMID:17086182: "the first report of a molecular cause of nephrotic syndrome that may resolve after therapy"
- PMID:18270750 (review, 2008): "NPHS3 is a severe form of isolated nephrotic syndrome with rapid progression to terminal renal failure"

**Identifiers**
- Confirmed by the task: MONDO:0012546, OMIM:610725.
- From memory, verify before use:
  - gene OMIM *608414
  - HGNC:17175, written `hgnc:17175` in this repo
  - Orphanet groups it under isolated diffuse mesangial sclerosis and genetic SRNS
  - ICD-10 N04.x, ICD-11 GB41
  - MeSH: Nephrotic Syndrome (D009404)

**Synonyms:** NPHS3; PLCE1 nephrotic syndrome; nephrotic syndrome caused by mutation in PLCE1; early-onset nephrotic syndrome with diffuse mesangial sclerosis; PLCE1-related steroid-resistant nephrotic syndrome.

**Source type:** The literature is aggregated case series and cohorts plus a few family studies. No EHR-derived data were found.

## 2. Etiology

- **Cause:** Germline biallelic (homozygous or compound-heterozygous) PLCE1 variants, mostly truncating.
- **Incomplete penetrance and modifiers:** Several reports show that PLCE1 genotype alone is not always sufficient for disease.
  - Gilbert et al. 2009 (PMID:19037252, *Kidney Int*): "mutation within PLCE1 is not always sufficient to cause diffuse mesangial sclerosis". In that kindred, "All affected children were homozygous for a four-basepair deletion in exon 3", yet unaffected relatives were also homozygous.
  - Boyer et al. 2010 (PMID:20591883): "three unaffected and unrelated individuals were also found to carry the homozygous mutations". The authors proposed modifier genes or environmental factors.
- **Environmental risk:** No human exposure is documented. Mouse data point to hemodynamic stress as a second hit (Section 5).
- **Protective factors:** None described.
- **Gene–environment interaction:** In mice, *Plce1* deficiency combined with hypertension gives glomerulosclerosis (PMID:32223311). This has not been shown in humans.
- **Unrelated association:** Common PLCE1 polymorphisms are GWAS risk loci for esophageal squamous cell carcinoma and gastric cancer (Wang LD 2010 and Abnet 2010, *Nat Genet*; recalled as PMID:20729852 and 20729853, not verified). They do not cause NPHS3 and should not be merged into this entry. A small association study of PLCE1 rs7922612 with nephrotic-syndrome risk exists (PMID:39028381, *Biochem Genet* 2025); its abstract was not reviewed.

## 3. Phenotypes

Unless stated, frequencies are qualitative. Onset is infantile to early childhood: median 11 months, range 1–72 months, in the DMS cohort of PMID:18065803.

| Phenotype | Type | Frequency / course | Candidate HPO (verify) | Support |
|---|---|---|---|---|
| Nephrotic syndrome | clinical/lab | obligatory; infantile/early-childhood onset | HP:0000100 Nephrotic syndrome | PMID:17086182, 18065803 |
| Nephrotic-range proteinuria | lab | ~100% | HP:0000093 Proteinuria (or a nephrotic-range child term) | PMID:17086182 |
| Hypoalbuminemia | lab | typical | HP:0003073 Hypoalbuminemia | general NS; no PLCE1-specific quote |
| Edema | sign | typical | HP:0000969 Edema | general NS |
| Hyperlipidemia / hypercholesterolemia | lab | typical | HP:0003077 Hyperlipidemia | general NS |
| Steroid resistance | clinical | most patients | HP:0031969? (SRNS term; verify existence) | PMID:20591883 |
| Diffuse mesangial sclerosis | histopathology | most frequent lesion; 33% of DMS cases carry PLCE1 variants | HP:0001967 Diffuse mesangial sclerosis | PMID:17086182, 18065803, 20591883 |
| Focal segmental glomerulosclerosis | histopathology | minority; 8% of NPHS2-negative FSGS cases | HP:0000097 Focal segmental glomerulosclerosis | PMID:17086182, 20591883 |
| Progression to ESKD | outcome | rapid, usually in early childhood | HP:0003774 Stage 5 chronic kidney disease | PMID:18270750 |
| Podocyte foot-process effacement | ultrastructure | expected | HP term to search | — |

Key quotes:
- PMID:17086182: "Kidney histology of affected individuals showed diffuse mesangial sclerosis (DMS)."
- PMID:17086182, on a missense family: "showed histology characteristic of focal segmental glomerulosclerosis"
- PMID:20591883: "Homozygous or compound heterozygous mutations were identified in 33% (8/24) of DMS cases." and "PLCE1 mutations were found in 8% (6/78) of FSGS cases without NPHS2 mutations."
- PMID:20591883: "No clear genotype-phenotype correlation was observed"

The disease is isolated (non-syndromic), with no consistent extrarenal features; PMID:18270750 calls it "isolated nephrotic syndrome". A PYCR1 cutis laxa case with PLCE1 nephrotic syndrome (PMID:30586144) is a double recessive diagnosis in a consanguineous family, not an NPHS3 feature.

**Quality of life:** No disease-specific QoL data. The burden is that of infantile nephrotic syndrome, dialysis and transplantation.

## 4. Genetic and molecular information

- **Gene:** *PLCE1*, chromosome 10q23. It encodes PLCε1, a phosphoinositide-specific phospholipase C with an N-terminal CDC25 RasGEF domain, the catalytic X/Y domains, a C2 domain and two Ras-association (RA) domains.
  - HGNC: `hgnc:17175` (verify).
  - UniProt Q9P212 (verify).
- **Variant spectrum:**
  - Truncating variants predominate: nonsense, frameshift, splice.
  - Missense variants occur and were seen in the FSGS siblings of PMID:17086182.
  - The 4-bp exon 3 deletion in a kindred with nonpenetrant homozygotes (PMID:19037252).
  - Gbadegesin et al. 2008 (PMID:18065803): "We detected truncating mutations in PLCE1 in 10/35 (28.6%) families"; "PLCE1 mutation is the most common cause of IDMS in this cohort."
  - Boyer et al. 2010 found that truncating and missense variants produced similar kidney outcomes.
- **Population frequencies:** Individual pathogenic alleles are rare in gnomAD. Not quantified here; check ClinVar and gnomAD per variant.
- **Origin:** Germline, recessive.
- **Functional consequence:** Loss of function. Evidence: truncation, cell knockdown and knockout phenocopies (Section 6), and the zebrafish morphant.
- **Genotype–age correlation:** Sadowski et al. 2015 (PMID:25349199), 1,783 SRNS families: "For PLCE1, specific mutations correlated with age of onset." Single-gene causes were found in "29.5% (526 of 1783)" of families, with yield highest when onset was in the first 3 months (69.4%).
- **Diagnostic yield in panels:** PLCE1 recurs in SRNS panel studies.
  - PMID:24742477: "Seven novel disease-causing mutations in PLCE1 (n=5), NPHS1 (n=1), and LAMB2 (n=1) were identified"
  - PMID:23349334: "variations in expected genes such as NPHS1, NPHS2, and PLCe1"
- **Negative cohorts:**
  - PMID:18975016: "PLCE1/NPHS3 mutations are not a cause of FSGS in this cohort." (69 families with FSGS)
  - PMID:24500309 found no pathogenic PLCE1 variants in sporadic adult FSGS.
  - So PLCE1 is mainly a pediatric DMS gene.
- **Modifier genes:** Proposed but none identified (PMID:19037252, 20591883). PMID:40003707 lists PLCE1 as a candidate modifier in Alport syndrome; that is a different direction of effect and was not reviewed.
- **Epigenetic or chromosomal changes:** None reported. CNV screening in SRNS cohorts (PMID:37670083) was not reviewed for PLCE1.

## 5. Environmental information

There is no known environmental, lifestyle or infectious trigger in humans. The mouse evidence is a hypertension second hit:
- Yu et al. 2020 (PMID:32223311): "global Plce1-deficient mice have histologically normal glomeruli and no albuminuria at baseline"
- Angiotensin II "led to 20-fold increased albuminuria and significantly more sclerotic glomeruli"
- Conclusion: "Plce1 deficiency in mice predisposes to glomerular damage secondary to hypertensive insults."

Evidence type: MODEL_ORGANISM. This is a candidate PREDISPOSES or EXACERBATES link to a hemodynamic-stress node. It does not establish an environmental cause of human disease.

## 6. Mechanism and pathophysiology

### Ordered causal chain
1. **Biallelic PLCE1 loss-of-function variants** (mostly truncating) **lead to** absent or nonfunctional PLCε1 protein in glomerular podocytes. PLCε1 is expressed in developing and mature podocytes. PMID:17086182: "we found PLCepsilon1 expression in developing and mature glomerular podocytes"
2. **Loss of PLCε1 catalytic activity results in** reduced hydrolysis of PIP2 to IP3 and DAG downstream of receptor tyrosine kinase, Ras and Rap signalling. EGF-induced DAG generation is one documented readout (in vitro).
   - PMID:29058690: "PLCE1 is a member of the phospholipase family of enzymes that catalyzes the hydrolysis of polyphosphoinositides to generate the second messengers ino-sitol-1,4,5 trisphosphate (IP3) and diacylglycerol (DAG)". This is a **BACKGROUND** quote; the line breaks in the cached full text need checking.
3. **Reduced PLCε1 signalling leads to** two parallel branches in podocytes:
   - **3a. Defective actin and Rho-GTPase regulation.** Less GTP-bound Rac1 and Cdc42 means fewer lamellipodia and lower migration.
     - PMID:32238860: "Knockdown or knockout of PLCE1 in podocytes resulted in decreased levels of GTP-bound Rac1 and Cdc42" and "PLCE1 regulates Rho GTPase activity and cell migration through interacting with NCK2".
     - Upstream of PLCε1, advillin (AVIL) recruits it to ARP2/3-rich lamellipodia. PMID:29058690 abstract: knockdown of AVIL "prevented recruitment of PLCE1 to the ARP3-rich lamellipodia, blocked EGF-induced generation of diacylglycerol (DAG) by PLCE1, and attenuated the podocyte migration rate (PMR)", and "ARP-dependent lamellipodia formation occurs downstream of AVIL and PLCE1 function."
     - BRAF is an interacting partner (PMID:17942568: "we show that BRAF interacts with PLCepsilon1"; "both proteins are coexpressed and colocalize in developing and mature glomerular podocytes"). The functional consequence is not established.
   - **3b. Impaired proliferation, differentiation and maturation signalling.**
     - PMID:32238860: "Knockout of PLCE1 reduced the EGF-induced activation of ERK and cell proliferation in podocytes", with "decreased expression of podocyte markers, including NEPH1, NPHS1, WT1, and SYNPO".
     - Patient-derived podocytes (PMID:42129791, 2026) show "reduced epithelial features, altered actin cytoskeleton and significantly lower levels of the epithelial marker ZO-1". They also show "functionally impaired TGF-β1 responses with an altered SMAD2/SMAD3 ratio", and the authors conclude "disease-causing mutations in PLCΕ1 result in podocyte dedifferentiation".
4. **Steps 3a and 3b result in** arrested or abnormal glomerular podocyte development. This is the proposed basis of DMS; it is **inferred**, not directly shown in human tissue time courses.
   - Hinkes 2006 interpreted DMS as developmental arrest.
   - PMID:18270750: "NPHS3 is caused by a developmental rather than structural podocyte dysfunction"
5. **Podocyte dysfunction leads to** foot-process effacement and failure of the glomerular filtration barrier, which **results in** nephrotic-range proteinuria, then hypoalbuminemia, edema and hyperlipidemia.
   - Zebrafish *plce1* morphants develop nephrotic edema (PMID:17086182). Morpholino specificity in zebrafish nephrotic models has since been questioned (PMID:29058690 discussion).
6. **Sustained barrier failure plus mesangial matrix expansion** (DMS) or segmental sclerosis (FSGS) **leads to** progressive glomerulosclerosis and nephron loss, which **results in** ESKD in early childhood.
   - **Branch:** mouse data suggest hemodynamic stress (hypertension or hyperfiltration) accelerates sclerosis in PLCε1-deficient glomeruli (PMID:32223311, MODEL_ORGANISM). Whether this explains the human nonpenetrance is **inferred**.

### Cell types, processes and compartments (all CURIEs to verify)
- **Cell types:** podocyte, CL:0000653 "glomerular visceral epithelial cell"; mesangial cell, CL:0000650 (site of matrix expansion in DMS).
- **Biological processes:**
  - phosphatidylinositol phospholipase C activity, GO:0004435 (molecular function)
  - phosphatidylinositol-mediated signaling, GO:0048015
  - glomerular visceral epithelial cell development or differentiation, GO:0072015 or GO:0072112
  - lamellipodium assembly, GO:0030032
  - regulation of Rac and Cdc42 GTPase activity
  - epidermal growth factor receptor signaling pathway, GO:0007173
  - ERK1/ERK2 cascade, GO:0070371
  - transforming growth factor beta receptor signaling, GO:0007179
  - glomerular filtration, GO:0003094
- **Cellular components:** lamellipodium, GO:0030027; cytoplasm and plasma membrane.
- **Chemical entities:** diacylglycerol, inositol 1,4,5-trisphosphate, phosphatidylinositol 4,5-bisphosphate (CHEBI lookups needed).

### Molecular profiling
- No NPHS3-specific transcriptomic, proteomic or metabolomic datasets were found.
- PMID:32223311 reports podocyte expression of PLCE1 in human single-cell data. Discover GEO candidates with `just discover-datasets`.

## 7. Anatomical structures

- **Primary organ:** kidney (UBERON:0002113).
- **Sites:** renal glomerulus (UBERON:0000074), glomerular filtration barrier, and the glomerular mesangium (DMS).
- **Laterality:** bilateral.
- **Secondary effects:** systemic consequences of nephrotic syndrome and ESKD, such as edema, infection and thrombosis risk. These are general to nephrotic syndrome and not PLCE1-specific.

## 8. Temporal development

- **Onset:** infantile to early childhood, occasionally congenital. Median 11 months, range 1–72 months, in the IDMS cohort (PMID:18065803).
- **Course:** progressive and steroid-resistant, with rapid progression to ESKD (PMID:18270750).
- **Remission:** treatment-induced remission is reported in a few patients.
  - PMID:17086182 describes two patients who responded to therapy.
  - PMID:18065803: "one child with truncating mutation in PLCE1 responded to cyclosporine therapy".
- **Critical period:** podocyte maturation, if the developmental-arrest model is right.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007, verify).
- **Penetrance:** incomplete. Unaffected homozygotes are documented (PMID:19037252, 20591883).
- **Expressivity:** variable, ranging from DMS with infantile ESKD to later-onset FSGS. Siblings can differ.
- **Consanguinity:** frequent. Many families come from consanguineous populations: Turkey, the Middle East, North Africa, South Asia (e.g., PMID:41612037 for Algeria; PMID:37204080 for Oman).
- **Prevalence:** not established; ultra-rare. Proportions of genetic cases:
  - about one third of DMS cases (8/24, PMID:20591883)
  - 28.6% of IDMS families (PMID:18065803)
  - 8% of NPHS2-negative FSGS (PMID:20591883)
  - a small share of large SRNS cohorts (PMID:25349199; the overall PLCE1 share is not in the abstract and needs the full text)
- **Founder effects and carrier frequency:** not documented.
- **Sex ratio:** no bias expected.

## 10. Diagnostics

- **Laboratory tests:**
  - urine protein/creatinine ratio
  - serum albumin
  - lipid profile
  - creatinine and eGFR
- **Biopsy:**
  - Light microscopy shows DMS: mesangial matrix expansion, small glomeruli, podocyte hypertrophy. A minority show FSGS.
  - Electron microscopy shows foot-process effacement.
- **Genetic testing:** an SRNS multigene panel or exome sequencing is first line in infantile or early-childhood SRNS. Typical panels cover NPHS1, NPHS2, WT1, LAMB2, PLCE1 and others (PMID:21415313, 23349334, 24742477).
  - A recent WGS study reports monogenic disease in 56.1% of early-onset families (PMID:40402239, not reviewed).
  - Yield falls with age at onset (PMID:25349199).
- **Differential diagnosis:**
  - WT1-related DMS (Denys-Drash/Frasier; check karyotype and genitalia)
  - LAMB2 (Pierson syndrome; ocular microcoria)
  - NPHS1 (Finnish type; congenital onset)
  - NPHS2 (FSGS; later onset)
  - other podocytopathies (AVIL, ARHGDIA, COQ genes), several of which already have KB entries
  - secondary causes such as congenital infections
- **Screening:** no newborn screening. Cascade testing of siblings is reasonable, but interpret it carefully because of the nonpenetrance.

## 11. Outcome and prognosis

- **Kidney survival:** most patients reach ESKD in early childhood (PMID:18270750). Boyer 2010 found similar kidney outcomes for truncating and missense variants.
- **Transplantation:** recurrence after transplantation is not expected in monogenic SRNS. No PLCE1-specific recurrence data were found.
- **Mortality, survival and QoL:** no PLCE1-specific figures.
- **Prognostic factors:** histology (DMS is more severe than FSGS) and variant-specific age of onset (PMID:25349199).

## 12. Treatment

- **Immunosuppression:** usually ineffective in genetic SRNS, but PLCE1 is the exception with occasional calcineurin-inhibitor or steroid responses.
  - PMID:17086182 (therapy-responsive cases)
  - PMID:18065803 (cyclosporine). The authors suggest "mutations in PLCE1 may serve as a biomarker for selecting patients with IDMS who may benefit from treatment."
  - A CsA-responsive congenital nephrotic syndrome with single heterozygous NPHS1, NPHS2 and PLCE1 variants (PMID:29663071) is not proof of NPHS3.
- **Antiproteinuric RAAS blockade:** ACE inhibitor or ARB. This is general SRNS supportive care, and the mouse hypertension model gives it a rationale.
- **Supportive care:** albumin infusion, diuretics, nutrition, lipid and thrombosis management.
- **Kidney replacement:** dialysis and kidney transplantation.
- **Experimental therapy:** none specific. No NCT trials target PLCE1.
- **NCIT suggestions** (codes per the CLAUDE.md list; verify the agent terms):
  - Pharmacotherapy NCIT:C15986, with therapeutic agents cyclosporine and tacrolimus (CHEBI lookups needed)
  - ACE-inhibitor class
  - Supportive Care NCIT:C15747
  - Organ Transplantation NCIT:C15289
  - Genetic Counseling NCIT:C15240
  - for dialysis, search NCIT

## 13. Prevention

- **Primary prevention:** not applicable.
- **Reproductive options:** genetic counseling for 25% recurrence risk, carrier testing, and prenatal or preimplantation testing in known families.
- **Secondary and tertiary prevention:**
  - early genetic diagnosis to avoid prolonged ineffective immunosuppression while still considering a CNI trial
  - blood-pressure control (inferred from the mouse second-hit data)
  - transplant planning

## 14. Other species

No naturally occurring PLCE1 nephropathy was found (OMIA not checked). Orthologues to verify via NCBI Gene and Alliance:
- mouse *Plce1*
- rat *Plce1*
- zebrafish *plce1*

## 15. Model organisms

| Model | Phenotype | Fidelity / limitations | Source |
|---|---|---|---|
| Zebrafish *plce1* morpholino knockdown | nephrotic edema | morpholino specificity questioned; not reproduced in stable mutants for related genes | PMID:17086182; caveat PMID:29058690 |
| *Plce1*-deficient mouse (global) | normal glomeruli, no albuminuria at baseline; albuminuria, sclerosis, "diffuse mesangial expansion, podocyte loss, and focal podocyte foot process effacement" after angiotensin II, DOCA-salt or norepinephrine hypertension | fails to recapitulate the spontaneous infantile disease; usable as a second-hit model | PMID:32223311 |
| Human podocyte lines, knockdown or knockout | ↓Rac1/Cdc42-GTP, ↓migration, ↓ERK and proliferation, ↓differentiation markers | in vitro | PMID:32238860 |
| Patient-derived immortalized podocytes (nonsense PLCE1, DMS) | dedifferentiation, ↓ZO-1, altered TGF-β1/SMAD2:SMAD3 | in vitro, single patient line | PMID:42129791 |
| AVIL–PLCE1 axis in podocytes | lamellipodia, DAG and migration defects | in vitro | PMID:29058690 |

The mouse model's normal baseline is a candidate `HUMAN_MODEL_MISMATCH` discussion: there is model evidence, but it does not reproduce the human spontaneous phenotype.

---

## Gaps and verification checklist
- Every CURIE above (HP, GO, CL, UBERON, CHEBI, NCIT, HGNC, Orphanet) must be looked up before binding.
- Quotes should be confirmed against cached abstracts. Run `just fetch-reference` for PMID:17086182, 18065803, 20591883, 19037252, 32223311, 32238860, 42129791, 17942568, 25349199, 18270750, 18975016 and 24742477.
- The PLCE1-specific proportion in PMID:25349199, the exact counts of therapy responders in PMID:17086182, and any GeneReviews coverage (`just check-genereviews`) still need to be checked.
- The esophageal-cancer GWAS PMIDs were recalled from memory and are unverified. They concern a separate phenotype.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000650` (1 mention) - the report calls it "site of matrix expansion in DMS"; CL calls it **mesangial cell**
- `GO:0004435` (1 mention) - the report calls it "molecular function"; GO calls it **phosphatidylinositol-4,5-bisphosphate phospholipase C activity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `UBERON:0000074` (1 mention) - the report calls it "Sites:** renal glomerulus"; UBERON calls it **renal glomerulus**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.