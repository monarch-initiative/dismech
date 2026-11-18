---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-11-17T03:07:45.226080'
end_time: '2026-11-17T03:14:47.855594'
duration_seconds: 422.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: VPS35-Related Parkinson Disease
  mondo_id: MONDO:0013625
  category: Mendelian
  causal_genes: VPS35
  omim_id: OMIM:614203
  synonyms: Parkinson disease type 17; Parkinson disease caused by mutation in VPS35;
    VPS35 Parkinson disease
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
  web_search_requests: 7
  num_turns: 33
  total_cost_usd: 3.58797145
  session_id: f19fbfd2-1be1-41bd-b369-807862407d91
  stop_reason: end_turn
  permission_denials: 7
  denied_tools:
  - Bash
  tool_calls: 31
  retrieval_calls: 24
  assistant_text_blocks: 3
citation_count: 31
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 25
  on_topic: 23
  validator_version: 0.6.0
term_validation:
  total_terms: 59
  verified: 57
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 5
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: CL:0002450
    reported_labels:
    - substantia nigra
    ontology_label: tether cell
  - term_id: NCBITaxon:10090
    reported_labels:
    - Mus musculus
    - Taxonomy of species used:** *Mus musculus
    ontology_label: Mus musculus
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
- **Disease Name:** VPS35-Related Parkinson Disease
- **MONDO ID:** MONDO:0013625 (if available)
- **Causal gene(s):** VPS35
- **OMIM:** OMIM:614203
- **Synonyms:** Parkinson disease type 17; Parkinson disease caused by mutation in VPS35; VPS35 Parkinson disease
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **VPS35-Related Parkinson Disease** covering all of the
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

Checking the existing KB entry and its cached references, then I'll search the web.

Found cached primary papers locally; reading their abstracts now.

I have enough retrieved material now — writing the report from the cached primary papers and searches.

---

# Research Report: VPS35-Related Parkinson Disease (PARK17 / PARK-VPS35)

**Interpretation note:** This report covers the disease caused by variants in **VPS35** (HGNC:13487, vacuolar protein sorting 35 ortholog), i.e. MONDO:0013625 / OMIM:614203 / PARK17, as specified in the request. All claims below are sourced from material retrieved in this session (locally cached PubMed abstracts and full texts in this repository's `references_cache/`, plus web searches). Where I could not retrieve a source, the section says so rather than filling from memory.

---

## 1. Disease Information

VPS35-related Parkinson disease is an **autosomal dominant, late-onset parkinsonism** caused by a single recurrent missense variant, **c.1858G>A (p.Asp620Asn; D620N)**, in *VPS35*, the cargo-recognition subunit of the retromer complex. It was identified in 2011 by two independent exome-sequencing studies: Vilariño-Güell et al. in a Swiss kindred (PMID:21763482) and Zimprich et al. in an Austrian family with 16 affected individuals (PMID:21763483).

- Vilariño-Güell et al.: *"This study describes the application of next-generation sequencing technologies to a Swiss kindred presenting with autosomal-dominant, late-onset Parkinson disease (PD). The family has tremor-predominant dopa-responsive parkinsonism with a mean onset of 50.6 ± 7.3 years. Exome analysis suggests that an aspartic-acid-to-asparagine mutation within vacuolar protein sorting 35 (VPS35 c.1858G>A; p.Asp620Asn) is the genetic determinant of disease."* (PMID:21763482)
- Zimprich et al.: *"We found a missense mutation, c.1858G>A (p.Asp620Asn), in the VPS35 gene in all seven affected family members who are alive... the same variant cosegregating with the disease in an autosomal-dominant mode with high but incomplete penetrance in two further families... The mean age of onset in the affected individuals was 53 years."* (PMID:21763483)

**Identifiers** (as given in the request / retrieved cache): MONDO:0013625 (Parkinson disease 17); OMIM:614203 (PARKINSON DISEASE 17; PARK17); HGNC:13487 (*VPS35*). The ClinGen Parkinson's Disease Gene Curation Expert Panel classifies the gene–disease relationship as **Definitive** with autosomal dominant inheritance, against the broader MONDO:0005180 (Parkinson disease) concept — quoted row from the cached ClinGen assertion: `VPS35 | HGNC:13487 | Parkinson disease | MONDO:0005180 | AD | Definitive | SOP8 | Parkinson's Disease Gene Curation Expert Panel | 2021-11-03T13:45:17.796Z`. I did not retrieve Orphanet, ICD-10/11 or MeSH identifiers for this specific subtype in this session.

**Synonyms:** Parkinson disease 17; PARK17; PARK-VPS35; VPS35 Parkinson disease; Parkinson disease caused by mutation in VPS35.

**Information provenance:** Almost entirely **aggregated disease-level** sources — family-based genetic studies, international screening cohorts, the MDSGene systematic review (PMID:30357936), and the GeneReviews chapter (PMID:28796472). There is no EHR-derived or registry-level individual-patient resource for this subtype that I was able to retrieve.

---

## 2. Etiology

### Disease causal factors
A single heterozygous germline missense variant, *VPS35* p.D620N, is the only variant established as pathogenic. The largest screening study to date is explicit on this point:

> *"We performed the largest multi-center study to ascertain the frequency and pathogenicity of the reported vacuolar protein sorting 35 gene variants in more than 15,000 individuals worldwide. p.Asp620Asn was detected in 5 familial and 2 sporadic PD cases and not in healthy controls, p.Leu774Met in 6 cases and 1 control, p.Gly51Ser in 3 cases and 2 controls. Overall analyses did not reveal any significant increased risk for p.Leu774Met and p.Gly51Ser in our cohort."* (Lesage et al. / multi-centre clinico-genetic analysis, PMID:23125461)

A 2018 review summarising this literature states that *"with over 15 000 individuals worldwide studied — the VPS35[D620N] is the only clearly pathogenic mutation characterised to date"* and gives an estimated frequency of *"0.4% of all PD cases"* for VPS35-associated PD (PMID:29743203).

### Genetic risk factors
- **Causal variant:** *VPS35* c.1858G>A, p.Asp620Asn (D620N).
- **Variants of uncertain significance:** p.Pro316Ser (PMID:21763482 — *"the pathogenicity of this mutation remains uncertain"*), p.Arg524Trp (predicted damaging, found in a sporadic case; PMID:21763483), p.Leu774Met and p.Gly51Ser (not associated with risk in the 15,000-individual study; PMID:23125461).
- **Haplotype:** Zimprich et al. reported *"the shared haplotype extends across 65 kilobases around VPS35"* (PMID:21763483), consistent with a shared ancestral origin in at least some families.
- **Possible pathway interaction with LRRK2:** *VPS35* D620N acts upstream of LRRK2 kinase (see §6), so LRRK2-pathway genetic variation is a biologically plausible modifier — but I retrieved no study testing *VPS35* D620N modifiers in human carriers.

### Environmental risk factors
**No disease-specific environmental risk factor was identified in the retrieved literature.** One mechanistic link exists in vitro: Wang et al. (Nature Medicine 2016) report that *"oxidative stress increased the VPS35-DLP1 interaction, which we also found to be increased in the brains of sporadic PD cases"* — a plausible but unproven gene–environment node. Age is the only well-established co-factor: the Vps35 D620N knock-in mouse work concludes that *"such a genetic predisposition and age-related alterations in the nigrostriatal dopamine system cooperatively influence the pathogenesis of PARK17"* (PMID:28173004).

### Protective factors
**Not available.** I retrieved no protective genetic variant, allele, dietary or lifestyle factor specific to *VPS35*-related PD.

### Gene–environment interactions
Beyond the oxidative-stress/VPS35–DLP1 observation above, no GxE data specific to this disease were retrieved.

---

## 3. Phenotypes

The authoritative clinical summary is the GeneReviews chapter (PMID:28796472), whose Clinical Characteristics section states:

> *"VPS35-related Parkinson disease (PARK-VPS35) is indistinguishable from Parkinson disease of unknown cause representing a simplex case (also referred to as 'sporadic' Parkinson disease). PARK-VPS35 is characterized by typical parkinsonism (resting tremor, bradykinesia, rigidity, disturbance of postural reflexes) presenting on average a decade earlier than in individuals with simplex Parkinson disease of unknown cause. Median age of onset is approximately 50 years, with a range of onset spanning the third to eighth decade of life. PARK-VPS35 subtypes can include tremor dominant, akinetic rigid, gait difficulty, or mixed. Asymmetric presentation is typical. The disease course is usually milder than that of simplex Parkinson disease of unknown cause, with a decreased incidence of atypical signs. Dyskinesia and motor fluctuations may occur. Neuropsychiatric manifestations (depression and schizophrenia), learning difficulties, mild cognitive impairment, and dementia have been reported, albeit with lower occurrence than in simplex Parkinson disease of unknown cause. Additional findings include impaired sense of smell and autonomic manifestations including orthostasis and constipation."*

| Phenotype | Type | HPO suggestion | Notes / frequency | Source |
|---|---|---|---|---|
| Parkinsonism (overall) | clinical sign | HP:0001300 Parkinsonism | Defining feature | PMID:28796472 |
| Resting tremor | clinical sign | HP:0002322 Resting tremor | Tremor-predominant in the Swiss kindred; "tremor dominant" is one named subtype | PMID:21763482; PMID:28796472 |
| Bradykinesia | clinical sign | HP:0002067 Bradykinesia | Typical | PMID:28796472 |
| Rigidity | clinical sign | HP:0002063 Rigidity | Typical | PMID:28796472 |
| Postural instability | clinical sign | HP:0002172 Postural instability | "disturbance of postural reflexes" | PMID:28796472 |
| Asymmetric onset | characteristic | — (qualifier) | "Asymmetric presentation is typical" | PMID:28796472 |
| Levodopa-responsive parkinsonism | treatment response | HP:0002548 Parkinsonism with favorable response to dopaminergic medication | "VPS35 mutation carriers have good response to l-dopa" | PMID:30357936 |
| Dyskinesia / motor fluctuations | clinical sign | HP:0100660 Dyskinesia | "may occur" | PMID:28796472 |
| Depression | behavioral | HP:0000716 Depression | More common in Austrian carriers than sporadic PD | PMID:24557499; PMID:28796472 |
| Psychosis / schizophrenia | behavioral | HP:0100753 Schizophrenia | Reported, lower occurrence than sporadic PD | PMID:28796472 |
| Mild cognitive impairment | cognitive | HP:0001268 Mental deterioration (or HP:0100543 Cognitive impairment) | Reported; one carrier had MCI on MoCA | PMID:28796472; PMID:22801713 |
| Dementia | cognitive | HP:0000726 Dementia | Reported, less often than sporadic PD | PMID:28796472 |
| Hyposmia | sensory | HP:0004409 Hyposmia | "impaired sense of smell" | PMID:28796472 |
| Orthostatic hypotension | autonomic | HP:0001278 Orthostatic hypotension | Autonomic manifestation | PMID:28796472 |
| Constipation | autonomic | HP:0002019 Constipation | Autonomic manifestation | PMID:28796472 |

**Characteristics:** onset adult/mid-life (median ~50 years, range third to eighth decade); progressive course; severity reportedly **milder** than idiopathic PD with fewer atypical signs (PMID:28796472). One longitudinally followed German carrier progressed *"from Hoehn and Yahr stage 1 to 3"* over 13 years from onset at age 45 (PMID:22801713).

**Quality-of-life impact:** **No disease-specific QoL instrument data (EQ-5D, SF-36, PDQ-39) for *VPS35* carriers were retrieved.** The MDSGene review notes *"the high degree of missingness of phenotypic features"* in the primary literature (PMID:30357936), which applies here.

---

## 4. Genetic / Molecular Information

**Causal gene:** *VPS35*, HGNC:13487, chromosome 16q11.2 (locus position not re-verified in this session). OMIM disease entry OMIM:614203.

**Pathogenic variant:**
- **c.1858G>A, p.Asp620Asn (D620N)** — missense, germline, heterozygous in patients. Classified **Definitive** for autosomal dominant Parkinson disease by the ClinGen PD GCEP (cached CGGV assertion, 2021-11-03).
- **Population frequency:** not observed in 3,309 controls in the discovery study (PMID:21763482) and not in healthy controls in the >15,000-individual multicentre study (PMID:23125461). I did not retrieve a gnomAD allele frequency in this session.
- **Variant type:** single-nucleotide missense; no structural, repeat-expansion or chromosomal mechanism is implicated.
- **Protein location:** *"the structure of a VPS35 sub-complex shows that the VPS35[D620N] mutation is located at the surface of the convex face of an α-helical solenoid domain... suggesting that the D620N mutation may impact interaction with an as yet unknown effector"* (PMID:29743203). Zavodszky et al. place it differently: *"The D620N mutation falls within the horseshoe-shaped region that comprises many helical repeats and folds around VPS29"* (PMID:24819384).

**Functional consequence — genuinely contested.** Three positions are represented in the retrieved literature, and this disagreement should be carried into any KB entry rather than resolved:

1. **Partial loss of function, restricted to one retromer activity.** Zavodszky et al.: *"Our data suggest that the D620N mutation is a partial loss of function mutation of just one role of VPS35: that of binding the WASH complex and FKBP15, and not a generalized VPS35 hypomorph."* (PMID:24819384). Munsie et al. likewise find *"VPS35 p.D620N acts as a loss-of-function mutation with respect to VPS35 activity regulating synaptic transmission and AMPAR recycling"* (PMID:25416282). The mouse knock-in work of Niu et al. concludes *"Vps35 D620N allele is a partial-loss-of-function allele"* (PMID:28173004).
2. **Gain of function via LRRK2.** Mir et al.: *"Our observations indicate that VPS35 controls LRRK2 activity and that the VPS35[D620N] mutation results in a gain of function, potentially causing PD through hyperactivation of the LRRK2 kinase."* (PMID:29743203)
3. **The mutant protein is fully functional for core retromer roles.** Chen et al.: *"by crossing VPS35 KI and null mice, our data demonstrate that a single D620N VPS35 allele is sufficient for survival and early maintenance of dopaminergic neurons, indicating that the D620N VPS35 protein is fully functional."* (PMID:30842285)

Several groups independently confirm what the mutation **does not** do: it does not destabilise the heterotrimer. *"Immunoisolation followed by western blotting also established that VPS35(D620N) retained the ability to form a heterotrimeric complex with VPS29 and VPS26A. These data establish that the molecular defect associated with the VPS35(D620N) mutation lies outside of heterotrimeric retromer assembly and retromer's endosome association."* (PMID:24980502). Follett et al. add *"Vps35 D620N is correctly folded and binds Vps29 and Vps26A with the same affinity as wild-type Vps35"* (PMID:24152121).

**Modifier genes:** no human modifier established. In mice, *parkin* is not required: a retrieved summary of Tsika/Moore-lab work states *"Parkin is not required for dopaminergic neurodegeneration induced by the expression of PD-linked D620N VPS35 in mice."* Also in mice, D620N VPS35 *"fails to modify the lethal neurodegenerative phenotype of human A53T-α-synuclein transgenic mice"* (PMID:30842285).

**Epigenetics, chromosomal abnormalities:** **not applicable / no data retrieved.** This is a single-nucleotide Mendelian disorder with no reported epigenetic or cytogenetic mechanism.

---

## 5. Environmental Information

**No environmental, lifestyle, or infectious etiologic factor specific to *VPS35*-related PD was retrieved.** The one mechanistically relevant exposure-like variable is oxidative stress, which augments the pathogenic VPS35–DLP1 interaction in vitro (Wang et al., Nature Medicine 2016, doi:10.1038/nm.3983). Infectious agents: not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous germline *VPS35* **c.1858G>A (p.D620N)** substitution alters a surface residue on the convex face of the VPS35 α-solenoid, **without** disrupting folding or assembly of the VPS35–VPS29–VPS26 cargo-selective retromer trimer or its endosomal targeting (PMID:24980502, PMID:24152121). *This step is demonstrated.*
2. The substituted surface **reduces affinity for FAM21**, the WASH-complex subunit that docks the complex onto retromer — quantitatively, *"the affinity of VPS35(D620N)/VPS29 to R20-21 (Kd = 4.6 ± 0.7 μM) was significantly lower (by 2.2 ± 0.5-fold) than that of the wild-type VPS35/VPS29 (Kd = 2.4 ± 0.6 μM)"* (PMID:24980502). *Demonstrated biophysically.*
3. Reduced FAM21 affinity **leads to** diminished retromer association with the whole WASH complex and its partners: *"there was a clear decrease in the enrichment of all components of the WASH complex within the VPS35(D620N) interactome... In addition, there was a decrease in enrichment of the known retromer interactor RME-8 and two of the newly identified interactors SDCCAG3 and ANKRD50"* (PMID:24980502); FKBP15 binding is *"almost abolished"* (PMID:24819384). *Demonstrated.*
4. **Branch 4a — WASH mislocalisation.** Reduced binding **results in** less membrane-associated WASH: *"Cells expressing the D620N mutant had less membrane-associated FKBP15 and strumpellin"* and *"the D620N-expressing cells have reduced endosomally localized FKBP15 and FAM21"* (PMID:24819384). **This step is contested** — McGough et al., using the same mutation, *"saw no obvious impairment of FAM21 endosomal localization"* (PMID:24980502). Either way, WASH-dependent cargo is affected: the D620N line shows *"reduced cell surface staining of GLUT-1 and increased intracellular staining"* plus a cell-spreading defect (PMID:24819384).
5. **Branch 4b — endosome-to-TGN retrieval failure.** Independently, the mutation **leads to** impaired retrograde transport: *"in cells expressing VPS35(D620N) there is a perturbation in endosome-to-TGN transport but not endosome-to-plasma membrane recycling, which we confirm in patient cells harboring the VPS35(D620N) mutation"*, specifically mis-sorting of the cation-independent mannose-6-phosphate receptor (CI-MPR) (PMID:24980502). Follett et al. add morphological consequences: *"expression of the PD-linked Vps35 D620N mutant redistributes retromer-positive endosomes to a perinuclear subcellular localization and that these endosomes are enlarged in both model cell lines and fibroblasts isolated from a PD patient"* (PMID:24152121). *Note the direct conflict:* Zavodszky et al. report *"D620N-expressing cells exhibited apparently normal VPS26, SNX1, CIMPR, and LAMP1 localization"* (PMID:24819384).
6. CI-MPR missorting **results in** failed delivery of its hydrolase ligand: *"its expression disrupts the trafficking of cathepsin D, a CI-MPR ligand and protease responsible for degradation of α-synuclein"* (PMID:24152121). *Demonstrated in cells/patient fibroblasts; the onward link to α-synuclein accumulation in human carriers is inferred.*
7. **Branch 4c — autophagy block.** Loss of WASH coupling **leads to** mistrafficking of ATG9A and failed autophagosome formation: *"Autophagy is impaired in cells expressing PD-mutant VPS35 or lacking WASH. The autophagy defects can be explained, at least in part, by abnormal trafficking of the autophagy protein ATG9A"* (PMID:24819384). The epistasis experiment supports the causal order — FAM21-tail overexpression reduced autophagosome formation in wild-type but not D620N cells, *"suggesting that the observed effects on autophagosome formation are indeed due to the decreased association between VPS35 and the WASH complex."* Functional consequence: increased mutant-huntingtin aggregates and *"increased levels of another autophagy substrate, PD-variant α-synuclein A53T"* (PMID:24819384).
8. **Branch 4d — chaperone-mediated autophagy.** In dopamine neurons the retrieval defect extends to the CMA receptor: *"VPS35-deficient DA neurons or DA neurons expressing PD-linked VPS35 mutant (D620N) had impaired endosome-to-Golgi retrieval of lysosome-associated membrane glycoprotein 2a (Lamp2a) and accelerated Lamp2a degradation. Expression of Lamp2a in VPS35-deficient DA neurons reduced α-synuclein"* (PMID:26203154). *Demonstrated in mouse DA neurons; note most of that paper's in vivo phenotype comes from VPS35 deficiency, not the knock-in allele.*
9. **Branch 4e — LRRK2 hyperactivation.** In parallel, the mutation **results in** elevated LRRK2 kinase output: *"the VPS35[D620N] knock-in mutation strikingly elevates LRRK2-mediated phosphorylation of Rab8A, Rab10, and Rab12 in mouse embryonic fibroblasts"*, with *"the phosphorylation of Rab10 was strikingly elevated, ∼6-fold compared with wild-type cells"* in homozygotes and *"4–5-fold elevation... in heterozygous VPS35[D620N] MEFs"*. Critically this is confirmed in human carriers: *"LRRK2-mediated Rab10 phosphorylation is increased in neutrophils as well as monocytes isolated from three Parkinson's patients with a heterozygous VPS35[D620N] mutation compared with healthy donors and idiopathic Parkinson's patients"*, and *"VPS35[D620N] mutation promotes Rab10 phosphorylation more potently than LRRK2 pathogenic mutations"* (PMID:29743203). *Demonstrated; the mechanism by which VPS35 controls LRRK2 is explicitly unknown — "further work is required to pinpoint the mechanism".*
10. **Branch 4f — mitochondrial fragmentation.** Mutant VPS35 **leads to** excess mitochondrial fission: *"VPS35 mutants showed increased interaction with dynamin-like protein (DLP) 1, which enhanced turnover of the mitochondrial DLP1 complexes via the mitochondria-derived vesicle-dependent trafficking of the complexes to lysosomes for degradation"*, with effects *"greatest in neurons expressing VPS35D620N"* and reversible by fission inhibition (Wang et al. 2016, doi:10.1038/nm.3983).
11. **Branch 4g — synaptic dysfunction.** The mutation **results in** altered glutamatergic signalling: *"VPS35 localizes to dendritic spines and is involved in the trafficking of excitatory AMPA-type glutamate receptors (AMPARs)... VPS35 p.D620N acts as a loss-of-function mutation with respect to VPS35 activity regulating synaptic transmission and AMPAR recycling in mouse cortical neurons and dopamine neuron-like cells produced from induced pluripotent stem cells of human p.D620N carriers."* The onward step is explicitly inferred by those authors: *"Such perturbations to synaptic function likely produce chronic pathophysiological stress upon neuronal circuits that may contribute to neurodegeneration"* (PMID:25416282).
12. These branches **converge on** dopaminergic dysfunction in the nigrostriatal system. Presynaptic release is reduced before any cell loss: *"DA release evoked by 120 mM potassium chloride was significantly reduced in the caudate putamen of adult homozygous Vps35 D620N KI mice"* (PMID:28173004); a separate knock-in line shows *"Impaired striatal dopamine release in homozygous Vps35 D620N knock-in mice"* (title, PMID:28173004 line).
13. With ageing, this **leads to** frank nigrostriatal degeneration: *"a heterozygous or homozygous D620N mutation is sufficient to reproduce key neuropathological hallmarks of PD as indicated by the progressive degeneration of nigrostriatal pathway dopaminergic neurons and widespread axonal pathology"* (PMID:30842285). **Contested:** *"Neither homozygous nor heterozygous Vps35 D620N KI mice suffered from premature death or developed clear neurodegeneration up to 70 weeks of age"* (PMID:28173004).
14. Nigrostriatal dopamine loss **results in** the clinical parkinsonian syndrome — tremor, bradykinesia, rigidity, postural instability, levodopa-responsive (PMID:28796472). *This final step is inferred by analogy with idiopathic PD; no human carrier study has correlated nigral cell counts with clinical severity.*

**The proteinopathy question is unresolved and is the main open gap.** Chen et al.: *"we find no evidence for α-synuclein-positive neuropathology in aged VPS35 KI mice, a hallmark of Lewy body pathology in PD"*, but instead *"endogenous D620N VPS35 expression induces robust tau-positive somatodendritic pathology throughout the brain as indicated by abnormal hyperphosphorylated and conformation-specific tau"*, raising *"the tantalizing possibility of a pathogenic interplay between mutant VPS35 and tau"* (PMID:30842285). A retrieved summary notes the tau finding has not replicated — a separate study using the same AT8 and MC-1 antibodies observed no tau pathology in 15–16-month-old mice in SNpc or cortex (Niu et al. 2021). Human neuropathology is near-absent: the single reported D620N autopsy had an incomplete examination of cortex and basal ganglia excluding the brainstem, and showed no Lewy body disease or α-synuclein immunoreactivity in the examined areas — so nigral pathology in human carriers is **unknown**.

**Ontology suggestions (mechanism):**
- GO:0042147 retrograde transport, endosome to Golgi — the core defective process
- GO:0032456 endocytic recycling; GO:0030100 regulation of endocytosis
- GO:0000045 autophagosome assembly; GO:0061684 chaperone-mediated autophagy
- GO:0000266 mitochondrial fission
- GO:0098887 neurotransmitter receptor transport, endosome to plasma membrane (AMPAR recycling)
- GO:0016310 phosphorylation / GO:0004674 protein serine/threonine kinase activity (LRRK2–Rab axis)
- GO:0030672 synaptic vesicle membrane; GO:0014046 dopamine secretion
- Cell types: CL:0000700 dopaminergic neuron; CL:0002450 (substantia nigra) — bind the specific midbrain dopaminergic neuron term after lookup; CL:0000598 pyramidal neuron (cortical neuron experiments); CL:0000057 fibroblast (patient fibroblasts); CL:0000775 neutrophil and CL:0000576 monocyte (the human pRab10 biomarker work)
- Chemical entities: CHEBI:18243 dopamine; CHEBI:6054 levodopa; CHEBI:16708 adenine-? (no — do not bind without lookup)

*Every CURIE above should be re-verified at the source before being written into a KB entry; they are offered as leads, not as checked bindings.*

**Molecular profiling:** no transcriptomic, proteomic, metabolomic or lipidomic dataset specific to *VPS35* D620N carriers was retrieved in this session, other than the SILAC interactome experiment in PMID:24980502 (which is an interactome, not a patient omics dataset). Single-cell and spatial data: none retrieved.

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** central nervous system (UBERON:0001017), specifically the **nigrostriatal pathway** — substantia nigra pars compacta (UBERON:0002038 substantia nigra) and striatum/caudate-putamen (UBERON:0002435 striatum; the mouse work measures dopamine release in caudate putamen, PMID:28173004). *"VPS35 was expressed in mouse dopamine (DA) neurons in substantia nigra pars compacta (SNpc) and STR (striatum)—regions that are PD vulnerable"* (PMID:26203154).
- **Secondary involvement:** cerebral cortex and wider brain in the tau-pathology report — *"tau-positive somatodendritic pathology throughout the brain"* (PMID:30842285); olfactory system (hyposmia) and autonomic nervous system (orthostasis, constipation) clinically (PMID:28796472).
- **Non-neural tissues show the biochemical defect without disease:** *"The VPS35[D620N] mutation also increases Rab10 phosphorylation in mouse tissues (the lung, kidney, spleen, and brain)"* and in human peripheral blood neutrophils and monocytes (PMID:29743203). This dissociation — ubiquitous biochemistry, selective neurodegeneration — is itself an unexplained feature.
- **Cell populations:** dopaminergic neurons (CL:0000700) are the degenerating population; dendritic spines are a site of VPS35 action (PMID:25416282).
- **Subcellular compartments (GO Cellular Component leads):** GO:0030904 retromer complex; GO:0005769 early endosome; GO:0005802 trans-Golgi network; GO:0005764 lysosome; GO:0005739 mitochondrion; GO:0005776 autophagosome; GO:0044309 neuron spine. The retromer's own compartment identity is documented: GFP-VPS35(D620N) *"localized predominantly to a sorting nexin-1 (SNX1) positive early-to-late transitional endosomal compartment"* (PMID:24980502).
- **Lateralization:** clinically **asymmetric** at onset — *"Asymmetric presentation is typical"* (PMID:28796472).

---

## 8. Temporal Development

- **Age of onset:** adult, mid-life. Mean 50.6 ± 7.3 years in the Swiss kindred (PMID:21763482); mean 53 years in the Austrian families (PMID:21763483); *"Median age of onset is approximately 50 years, with a range of onset spanning the third to eighth decade of life"* (PMID:28796472). GeneReviews also cites a median of 52 years (IQR 45–61) in 67 affected individuals from Trinh et al. and 48 years (IQR 44–56) in 23 affected individuals from a later series. The MDSGene review across the three dominant PD genes reports *"later onset of disease (median age at onset: ∼49 years) compared to recessive forms of PD"* (PMID:30357936). Onset about a decade earlier than idiopathic PD is the consistent signal.
- **Onset pattern:** insidious and chronic, as in typical PD.
- **Progression:** slowly progressive and lifelong. One carrier moved *"from Hoehn and Yahr stage 1 to 3"* across 13 years of follow-up (PMID:22801713). GeneReviews: *"The disease course is usually milder than that of simplex Parkinson disease of unknown cause, with a decreased incidence of atypical signs."*
- **Critical period / preclinical window:** the mouse data suggest a long presynaptic phase before cell loss — reduced evoked striatal dopamine release in adult knock-in mice *without* clear neurodegeneration to 70 weeks (PMID:28173004) — and tau abnormality reported *"even as early as at 3 months of age"* in the other line. This implies a therapeutic window before degeneration, but no human prodromal natural-history study was retrieved.
- **Remission:** none; no spontaneous remission is reported. Symptomatic improvement is treatment-induced only.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006). *"the same variant cosegregating with the disease in an autosomal-dominant mode with high but incomplete penetrance"* (PMID:21763483).
- **Penetrance:** **incomplete and age-dependent.** Zimprich et al. describe "high but incomplete penetrance" (PMID:21763483). Kumar et al. provide a concrete demonstration: in the extended German family, *"An affected paternal aunt and 3 reportedly unaffected siblings were also found to be mutation carriers"*, concluding *"Genetic analysis of the extended family revealed incomplete penetrance of the p.D620N mutation"* (PMID:22801713). Independently, a global survey of MDSGene corresponding authors counted *"23 VPS35"* affected individuals alongside *"3 VPS35"* unaffected carriers. **No quantitative age-specific penetrance estimate was retrieved.**
- **Expressivity:** variable — onset spans the third to eighth decade and motor subtype varies (tremor dominant, akinetic rigid, gait difficulty, mixed) within the same genotype (PMID:28796472).
- **Frequency among PD:** rare. *"VPS35-associated PD is overall rare with an estimated frequency of 0.4% of all PD cases"* (PMID:29743203). A separate retrieved estimate puts carrier frequency at ~0.1% among PD patients. In the 1,774-patient international screen, *"A single mutation carrier was identified"* (~0.06%) (PMID:22801713); in the >15,000-individual study, p.D620N appeared in 5 familial and 2 sporadic cases (PMID:23125461).
- **Population prevalence / incidence in the general population:** **not available.** No Orphanet point prevalence or incidence figure for PARK17 was retrieved. Given ~0.1–0.4% of PD cases, any population figure would be derivative.
- **Affected populations and geography:** identified predominantly in families of **European descent** — Swiss (PMID:21763482), Austrian (PMID:21763483), French (PMID:22517097, "Identification of VPS35 mutations replicated in French families with Parkinson disease"), German, Serbian, Chilean and US referral centres screened in PMID:22801713, plus a Japanese cohort reported as typical adult-onset tremor-predominant PD. A review retrieved in search states the variant has been found *"mainly in families of European descent."*
- **Founder effect:** the 65-kb shared haplotype around *VPS35* (PMID:21763483) is consistent with a common ancestral founder among the reported families, though no formal founder-population claim was retrieved.
- **Genetic anticipation:** not applicable (not a repeat expansion); none reported.
- **Germline mosaicism, consanguinity, carrier screening frequency:** no data retrieved. Consanguinity is not relevant to a dominant mechanism.
- **Sex ratio and age distribution:** **not retrieved.** No sex-ratio figure specific to *VPS35* carriers was found.

---

## 10. Diagnostics

**Genetic testing is the diagnostic modality.** Because the clinical picture is *"indistinguishable from Parkinson disease of unknown cause"* (PMID:28796472), the diagnosis rests on finding the *VPS35* p.D620N variant in a person with parkinsonism, usually with a family history — GeneReviews notes about 90% of affected individuals have a family history of PD.

- **Single-gene / targeted variant testing:** since D620N is the only established pathogenic variant, targeted testing of *VPS35* c.1858G>A is the highest-yield approach. The original studies used Sanger sequencing of the *VPS35* coding sequence (PMID:21763483 screened 860 cases and 1,014 controls this way).
- **Gene panels / WES / WGS:** the variant was discovered by exome sequencing (both PMID:21763482 and PMID:21763483), and exome or a PD gene panel including *VPS35* is appropriate for a dominant PD pedigree. **I did not retrieve GTR panel listings or diagnostic-yield figures in this session.**
- **CMA, karyotyping, FISH, mtDNA testing, repeat-expansion testing:** not applicable — no structural, cytogenetic, mitochondrial or repeat mechanism.

**Biomarkers:** the one disease-specific molecular readout retrieved is **LRRK2-dependent Rab10 Thr73 phosphorylation in peripheral blood cells**, which is elevated in D620N carriers relative to both healthy donors and idiopathic PD patients (PMID:29743203). That paper develops the assay in monocytes and neutrophils and reports *P < 0.0001* for the carrier-versus-control difference in both cell types (n = 3 carriers, 9 idiopathic PD, 9 controls). Note the very small carrier number; this is a research assay, not a validated clinical biomarker. LOINC coding: not retrieved.

**Imaging:** no *VPS35*-specific imaging signature. In the single longitudinally followed carrier, *"No abnormalities were observed by multimodal neuroimaging"* (PMID:22801713). Standard PD imaging (dopamine-transporter SPECT) would be expected to be abnormal but I retrieved no carrier-cohort imaging study.

**Laboratory / functional / electrophysiology / biopsy / pathology:** nothing disease-specific. Patient **fibroblasts** are a useful research substrate — CI-MPR dispersal and enlarged perinuclear endosomes are demonstrable in carrier fibroblasts (PMID:24980502, PMID:24152121) — but this is not a diagnostic test. Neuropathology is not diagnostic and, as noted in §6, is essentially uncharacterised in human carriers.

**Clinical criteria:** standard PD diagnostic criteria (MDS clinical diagnostic criteria / UK Brain Bank) apply; I did not retrieve a *VPS35*-specific criteria document. **Differential diagnosis:** idiopathic PD (the default, since the phenotypes are indistinguishable), and other dominant monogenic PD — *LRRK2*-related PD (later onset, typical PD; PMID:30357936) and *SNCA*-related PD (*"SNCA mutation carriers have a younger age at onset compared to LRRK2 and VPS35"* and *"often have additional psychiatric symptoms"*, PMID:30357936). *VPS35L*-related Ritscher-Schinzel/3C syndrome is a distinct retriever-complex disease and not a differential for adult parkinsonism (PMID:31712251, PMID:36113987).

**Screening:** cascade (at-risk relative) testing is the relevant modality for a dominant adult-onset condition; newborn and population carrier screening are not applicable. I retrieved no society recommendation specific to *VPS35* predictive testing.

---

## 11. Outcome / Prognosis

- **Survival, life expectancy, mortality rate, disease-specific mortality:** **no data retrieved.** No survival analysis or mortality figure for *VPS35*-related PD was found in this session. A knowledge-base entry should record these as unknown rather than importing idiopathic-PD figures.
- **Course and morbidity:** chronic, progressive, lifelong; disability accrues from motor decline. The retrieved evidence points to a **comparatively favourable** course: *"The disease course is usually milder than that of simplex Parkinson disease of unknown cause, with a decreased incidence of atypical signs"*, and neuropsychiatric manifestations, mild cognitive impairment and dementia occur *"albeit with lower occurrence than in simplex Parkinson disease of unknown cause"* (PMID:28796472). The one 13-year follow-up reached Hoehn–Yahr stage 3 (PMID:22801713).
- **Complications:** levodopa-induced dyskinesia and motor fluctuations *"may occur"*; depression, psychosis, cognitive decline and dementia; autonomic failure (orthostasis, constipation) (PMID:28796472). Depression was *"more common in Austrian patients compared to sporadic PD patients"* (PMID:24557499).
- **Quality-of-life measures:** none retrieved (see §3).
- **Recovery potential:** none — treatment is symptomatic, not disease-modifying.
- **Prognostic factors and prognostic biomarkers:** **none established.** No study retrieved relates age at onset, motor subtype, or pRab10 level to outcome. Peripheral pRab10 is a candidate *target-engagement* biomarker rather than a prognostic one.

---

## 12. Treatment

**Treatment is symptomatic and identical to that of idiopathic PD.** GeneReviews states treatment is the same as for simplex PD, and notes that dopamine agonists are considered suitable candidates because of the lower rates of atypical features and dementia in this subtype.

- **Levodopa and dopaminergic therapy — the mainstay, and the response is good.** The discovery kindred had *"tremor-predominant dopa-responsive parkinsonism"* (PMID:21763482). The MDSGene systematic review concludes *"VPS35 mutation carriers have good response to l-dopa"* and describes *"an overall excellent treatment response"* across the dominant PD forms (PMID:30357936). GeneReviews: *"most individuals respond well to levodopa and other dopaminergic medications."* NCIT leads: `NCIT:C15986` Pharmacotherapy as the action, with `CHEBI:6054` levodopa (and a carbidopa/benserazide combination) as `therapeutic_agent`.
- **Dopamine agonists:** suitable per GeneReviews; agent-level CHEBI/NCIT identifiers were not looked up in this session.
- **Targeted / mechanism-based therapy — LRRK2 kinase inhibition is the one genotype-directed proposal.** Mir et al. state it explicitly: *"our findings suggest that it may be possible to elaborate compounds that target the retromer complex to suppress LRRK2 activity. Moreover, patients with VPS35[D620N] associated Parkinson's might benefit from LRRK2 inhibitor treatment that have entered clinical trials in humans."* (PMID:29743203). Preclinical support is partial, not complete: in knock-in mice Rab10 hyperphosphorylation was reversed by LRRK2 kinase inhibition, *"but this did not rescue elevated glutamate release or surface GluA1 expression"* (Kadgien et al.). The tool compounds used in the retrieved work are MLi-2, GSK2578215A and PF-06447475 (PMID:29743203); MLi-2 at 30 mg/kg subcutaneously suppressed tissue pRab10 in vivo. **I retrieved no clinical trial of a LRRK2 inhibitor enrolling *VPS35* carriers and no NCT identifier**; do not assert one.
- **Mitochondrial-fission blockade** is a second preclinical lead: a decoy peptide blocking the VPS35–DLP1 interaction *"rescued D620N-induced fragmentation and respiratory deficits... in both M17 cells overexpressing D620N or PD fibroblasts bearing this mutation"* (follow-up to Wang et al. 2016). Preclinical only.
- **Surgical / interventional:** deep brain stimulation is standard PD care, but **no *VPS35*-specific DBS outcome data were retrieved.** Do not assert a genotype-specific DBS response.
- **Gene therapy, cell therapy, RNA-based therapy, immunotherapy:** none reported for this disease.
- **Supportive care and rehabilitation:** physical, occupational and speech therapy as in PD generally; no disease-specific evidence retrieved. NCIT leads: `NCIT:C15302` Physical Therapy, `NCIT:C121351` Occupational Therapy, `NCIT:C159273` Speech Language Therapy, `NCIT:C15240` Genetic Counseling, `NCIT:C15747` Supportive Care.
- **Pharmacogenomics, treatment response rates, adverse-event data, treatment algorithms, combination therapy:** no *VPS35*-specific data retrieved.

---

## 13. Prevention

- **Primary prevention:** none available. A dominant germline missense variant with no established environmental co-factor leaves no modifiable primary-prevention target. Nothing in the retrieved literature supports a risk-factor-modification strategy.
- **Secondary prevention / early detection:** no screening programme exists or is recommended. The theoretical basis for a prodromal window (reduced striatal dopamine release before cell loss in knock-in mice, PMID:28173004) is preclinical.
- **Genetic counselling** is the substantive preventive intervention: autosomal dominant transmission with a 50% recurrence risk per offspring, complicated by **incomplete penetrance** (PMID:21763483, PMID:22801713) and variable age at onset spanning the third to eighth decade (PMID:28796472). Counselling for predictive testing of asymptomatic adult relatives must address that an at-risk relative may carry the variant and remain unaffected — three reportedly unaffected siblings were carriers in one pedigree (PMID:22801713). I retrieved no NSGC/ACMG statement specific to *VPS35*.
- **Prenatal testing / PGD:** technically feasible for a known familial missense variant; **no guidance specific to this disease was retrieved**, and the adult-onset, incompletely penetrant nature makes this an ethically weighted decision rather than a recommendation.
- **Immunization, public-health and environmental interventions, prophylaxis:** not applicable.
- **Risk stratification:** carrier status is the only stratifier; peripheral pRab10 elevation (PMID:29743203) distinguishes carriers biochemically but has not been shown to predict onset.

---

## 14. Other Species / Natural Disease

- **Evolutionary conservation:** *VPS35* is *"evolutionarily highly conserved"* (PMID:21763482), and the retromer complex is *"a conserved membrane-associated protein complex"* (PMID:24819384). The D620N-equivalent residue is conserved: Zavodszky et al. aligned *"human VPS35 residues 610–680... with VPS35 homologues from other well-studied eukaryotes"* (PMID:24819384). Mechanistic conservation extends to *Drosophila*, where *"Drosophila VPS35 and LRRK2 were shown to affect the same set of synaptic vesicle processes including dopaminergic synaptic release"* (cited in PMID:29743203). Notably, conservation is **not** complete across the pathway: *"Unlike the WASH complex, FKBP15 is not conserved in either Caenorhabditis elegans or Drosophila melanogaster"* (PMID:24819384), and *"the WASH complex is not conserved [in yeast]"* (PMID:24819384) — a real constraint on invertebrate modelling.
- **Taxonomy of species used:** *Mus musculus* (NCBITaxon:10090), *Drosophila melanogaster* (NCBITaxon:7227), *Homo sapiens* (NCBITaxon:9606). Mouse gene: *Vps35*, MGI identifier **not looked up in this session** — resolve it at MGI before binding (per this repository's MOD-first rule, a mouse model's gene takes `MGI:`, not `hgnc:13487`).
- **Naturally occurring disease in other species, breeds (VBO), veterinary relevance, zoonotic potential, cross-species susceptibility:** **no data retrieved.** I found no OMIA record or veterinary report of naturally occurring *VPS35*-related parkinsonism in any animal. This is expected — all animal evidence is engineered, not natural.
- **Comparative pathology:** the most informative cross-species discrepancy is the proteinopathy. Human idiopathic PD is defined by Lewy pathology; D620N knock-in mice show *"no evidence for α-synuclein-positive neuropathology in aged VPS35 KI mice"* and instead tau pathology (PMID:30842285). Whether that is a species difference or a true feature of the human disease cannot be settled, because human carrier neuropathology is essentially unexamined (§6).

---

## 15. Model Organisms

### Mouse — the principal system, and the models disagree

Two independently generated **D620N knock-in** lines exist, and they do not agree on whether the allele causes neurodegeneration. This disagreement should be curated as such, with each model's limitation recorded.

**Model 1 — B6(Cg)-Vps35^tm1.1Mjff/J (JAX stock 023409), germline knock-in.** Generated by Matthew Farrer's group with the Michael J. Fox Foundation, Ozgene and the Jackson Laboratory; constructed with a floxed "mini-cDNA" in intron 14–15 removed by Cre to allow constitutive D620N expression from exon 15, on a C57BL/6 background (detailed construction described in PMID:29743203, Methods). Available from JAX.
- Used for the LRRK2 finding: heterozygous and homozygous MEFs show 4–5-fold and ~6-fold Rab10 Thr73 hyperphosphorylation respectively, abolished by 100 nM MLi-2; elevated pRab10 also in lung, kidney, spleen and brain in vivo (PMID:29743203). *Recapitulates the human biochemical phenotype — the same elevation is measurable in carrier neutrophils and monocytes.*
- Chen et al. report the neurodegenerative phenotype in a germline D620N knock-in: *"a heterozygous or homozygous D620N mutation is sufficient to reproduce key neuropathological hallmarks of PD as indicated by the progressive degeneration of nigrostriatal pathway dopaminergic neurons and widespread axonal pathology"*, plus widespread tau pathology including *"in TH-positive cells within the substantia nigra"* (PMID:30842285).
- **Limitations:** no Lewy/α-synuclein pathology; the tau finding has not replicated (Niu et al. 2021, same AT8/MC-1 antibodies, no tau pathology at 15–16 months); the mutant allele is *"fully functional"* for survival and early dopaminergic maintenance, so the model does not demonstrate haploinsufficiency; and D620N *"fails to modify the lethal neurodegenerative phenotype of human A53T-α-synuclein transgenic mice"* (PMID:30842285).

**Model 2 — CRISPR/Cas9 Vps35 D620N knock-in plus Vps35 Del1 null, Niu et al.** *"we generated Vps35 D620N knock-in (KI) mice, expressing the homologous mutant protein with endogenous patterns of expression, simultaneously with Vps35 deletion 1 (Del1) mice, which carry 1bp deletion in the exon15 of Vps35, by CRISPR/Cas9-mediated genome engineering."* (PMID:28173004)
- **Negative for degeneration:** *"Neither homozygous nor heterozygous Vps35 D620N KI mice suffered from premature death or developed clear neurodegeneration up to 70 weeks of age."*
- **Positive for presynaptic dysfunction:** *"In vivo microdialysis showed that DA release evoked by 120 mM potassium chloride was significantly reduced in the caudate putamen of adult homozygous Vps35 D620N KI mice."* The companion paper title is explicit — *"Impaired striatal dopamine release in homozygous Vps35 D620N knock-in mice."*
- **Allelic series is informative:** *"Vps35 Del1 allele appeared to be a null or at least severely hypomorphic allele and homozygous Vps35 Del1 showed early embryonic lethality"*, and *"the D620N/Del1 compound heterozygous mice, but not heterozygous Del1 mice, suffered from survival disadvantage"* — the basis for the authors' conclusion that *"Vps35 D620N allele is a partial-loss-of-function allele."*
- **Limitation:** the degeneration phenotype is absent, and the informative genotypes are homozygous or compound heterozygous, whereas human patients are heterozygous.

**Model 3 — Vps35 conditional deficiency in dopamine neurons (not the knock-in allele).** *"VPS35-deficient mice exhibited PD-relevant deficits including accumulation of α-synuclein in SNpc-DA neurons, loss of DA transmitter and DA neurons in SNpc and STR, and impairment of locomotor behavior"*, with the Lamp2a/CMA mechanism (PMID:26203154). **Limitation and a frequent misreading:** most of that in vivo phenotype comes from VPS35 *deficiency*, not from D620N; the D620N result there is the cell-level Lamp2a retrieval defect. Deficiency is not the human genotype.

**Model 4 — Viral overexpression in rat.** A retrieved review reports that *"in a rat model the expression of D620N VPS35 induces the marked degeneration of substantia nigra dopaminergic neurons"* while noting the common D620N mutation *"does not compromise its protein stability or localization to endosomal and lysosomal vesicles."* **Limitation:** supraphysiological viral expression; not an endogenous-level model.

**Model 5 — *Drosophila*.** A retrieved review reports a *Drosophila* study that *"found no evidence of dominant toxicity from any variant form including the pathogenic D620N and suggested a partial loss-of-function mechanism."* **Limitation:** FKBP15 is absent in flies (PMID:24819384), so a key part of the mammalian retromer–WASH–FKBP15 tripartite defect cannot be modelled.

### Cellular and in vitro systems
- **Patient-derived fibroblasts** from D620N carriers — reproduce CI-MPR dispersal (*"we also examined the steady-state distribution of CI-MPR in fibroblasts obtained from a healthy donor and from a patient harboring the VPS35(D620N) mutation. Again an increased dispersal of CI-MPR was observed"*, PMID:24980502) and enlarged perinuclear endosomes (PMID:24152121). The rescue control is the strength of this system: dispersal *"could be rescued by suppression of endogenous VPS35 and re-expression of wild-type GFP-VPS35... suggesting that the differences in CI-MPR distribution are not due to variability between cell lines isolated from different patients"* (PMID:24980502).
- **iPSC-derived dopamine neuron-like cells from human D620N carriers** — used for the AMPAR-recycling loss-of-function result (PMID:25416282). This is the most human-relevant cellular system retrieved.
- **Primary mouse embryonic fibroblasts** from the knock-in line, wild-type/heterozygous/homozygous from littermate E12.5 embryos — the pRab10 workhorse (PMID:29743203).
- **Patient peripheral blood neutrophils and monocytes** — not a "model" but the human ex vivo readout (PMID:29743203).
- **Engineered cell lines:** HeLa and RPE1 stably expressing GFP-VPS35 WT vs D620N with endogenous VPS35 knocked down (PMID:24980502, PMID:24819384); SH-SY5Y neuroblastoma for toxicity assays; A549 VPS35 and Rab12 CRISPR knockouts (PMID:29743203); M17 cells for the DLP1 work. Note a negative result worth recording: in SH-SY5Y, suppression of VPS35, FAM21, SDCCAG3, RME-8 or ANKRD50 produced *"no increase in cell death"* on MPP+ challenge (PMID:24980502).
- **Mouse cortical neuron cultures** — VPS35 localisation to dendritic spines and AMPAR trafficking (PMID:25416282).

### Resources
JAX (stock 023409) for the Mjff knock-in. MGI, IMSR and the Alliance of Genome Resources are the appropriate registries; **I did not query them in this session**, so no MGI allele or IMSR identifier is asserted here.

---

## Summary of what is NOT available or NOT applicable

Recorded explicitly so a KB entry does not fill these from inference:

- Population prevalence/incidence of PARK17; Orphanet, ICD-10/11 and MeSH identifiers for the subtype
- Survival, life expectancy, mortality figures; prognostic factors and prognostic biomarkers
- Sex ratio; age distribution of affected individuals; quantitative age-specific penetrance
- Quality-of-life instrument data
- gnomAD allele frequency for c.1858G>A (not retrieved this session)
- Any environmental or lifestyle risk factor; any protective factor; any GxE study
- Epigenetic mechanism; chromosomal abnormality — **not applicable**
- Infectious agent — **not applicable**
- Patient-level omics (transcriptomic/proteomic/metabolomic/lipidomic/single-cell/spatial) datasets
- Clinical trial identifiers (NCT or ICTRP) enrolling *VPS35* carriers; DBS outcomes in carriers; pharmacogenomic data
- Naturally occurring disease in other species (OMIA); breed (VBO); zoonotic potential — **not applicable**
- MGI/NCBI Gene identifiers for orthologs (not looked up; must be resolved at source before binding)
- Human carrier neuropathology beyond one incomplete autopsy — this is the single largest genuine knowledge gap

## Three contested points to curate as disagreements, not as settled facts

1. **Loss vs gain of function** (PMID:24819384 / PMID:28173004 / PMID:25416282 versus PMID:29743203, with PMID:30842285 arguing the mutant protein is fully functional).
2. **Whether CI-MPR/cathepsin D trafficking is affected** (PMID:24980502 and PMID:24152121 say yes; PMID:24819384 reports normal CIMPR and LAMP1 localisation).
3. **Whether the endogenous-level mouse allele causes neurodegeneration, and whether tau pathology is real** (PMID:30842285 versus PMID:28173004 and the Niu et al. 2021 non-replication).

---

**Sources:**

Locally cached in this repository's `references_cache/` (read in full this session): [PMID:21763482](https://pubmed.ncbi.nlm.nih.gov/21763482/), [PMID:21763483](https://pubmed.ncbi.nlm.nih.gov/21763483/), [PMID:22517097](https://pubmed.ncbi.nlm.nih.gov/22517097/), [PMID:22801713](https://pubmed.ncbi.nlm.nih.gov/22801713/), [PMID:23125461](https://pubmed.ncbi.nlm.nih.gov/23125461/), [PMID:24152121](https://pubmed.ncbi.nlm.nih.gov/24152121/), [PMID:24557499](https://pubmed.ncbi.nlm.nih.gov/24557499/), [PMID:24819384](https://pubmed.ncbi.nlm.nih.gov/24819384/), [PMID:24980502](https://pubmed.ncbi.nlm.nih.gov/24980502/), [PMID:25416282](https://pubmed.ncbi.nlm.nih.gov/25416282/), [PMID:26203154](https://pubmed.ncbi.nlm.nih.gov/26203154/), [PMID:28173004](https://pubmed.ncbi.nlm.nih.gov/28173004/), [PMID:28796472](https://pubmed.ncbi.nlm.nih.gov/28796472/), [PMID:29743203](https://pubmed.ncbi.nlm.nih.gov/29743203/), [PMID:30357936](https://pubmed.ncbi.nlm.nih.gov/30357936/), [PMID:30842285](https://pubmed.ncbi.nlm.nih.gov/30842285/), [PMID:31712251](https://pubmed.ncbi.nlm.nih.gov/31712251/), [PMID:36113987](https://pubmed.ncbi.nlm.nih.gov/36113987/), and ClinGen assertion `CGGV:assertion_b0e546d6-8a44-4e9d-83aa-f781ec4ec166-2021-11-03T134517.796Z`.

Retrieved by web search this session: [Wang et al., Nature Medicine 2016 (VPS35–DLP1)](https://www.nature.com/articles/nm.3983.pdf), [PMC4826611](https://pmc.ncbi.nlm.nih.gov/articles/PMC4826611), [PMC6431187 (D620N knock-in neuropathology)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6431187), [PMC10903469 (WASH binding, mixed trafficking findings)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10903469), [npj Parkinson's Disease 2023 (VKI mice, LRRK2 gain of function)](https://www.nature.com/articles/s41531-023-00609-7), [Mechanisms of VPS35-Mediated Neurodegeneration review, PMID:35497708](https://pubmed.ncbi.nlm.nih.gov/35497708/), [Parkinson's disease-linked mutations in VPS35 induce dopaminergic neurodegeneration, PMID:24740878](https://pubmed.ncbi.nlm.nih.gov/24740878/), [JAMA Neurology D620N international screen](https://jamanetwork.com/journals/jamaneurology/fullarticle/1217312), [GeneReviews VPS35-Related Parkinson Disease (NBK447258)](https://ncbi.nlm.nih.gov/books/NBK447258), [OMIM 614203](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/614203), [VPS35, the Retromer Complex and Parkinson's Disease (JPD 161020)](https://journals.sagepub.com/doi/10.3233/JPD-161020), [Vollstedt et al. global monogenic PD survey](https://core.ac.uk/download/228204114.pdf), [MDSGene VPS35 review record](https://research.uni-luebeck.de/en/publications/genotype-phenotype-relations-for-the-parkinsons-disease-genes-snc/).

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0002450` (1 mention) - the report calls it "substantia nigra"; CL calls it **tether cell**
- `NCBITaxon:10090` (1 mention) - the report calls it "Mus musculus", "Taxonomy of species used:** *Mus musculus"; NCBITaxon calls it **Mus musculus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000700` (2 mentions) - the report calls it "Cell populations:** dopaminergic neurons"; CL calls it **dopaminergic neuron**
- `UBERON:0001017` (1 mention) - the report calls it "Primary organ/system:** central nervous system"; UBERON calls it **central nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:10090` - called "Mus musculus", "Taxonomy of species used:** *Mus musculus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.