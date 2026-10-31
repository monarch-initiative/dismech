---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T07:55:07.216460'
end_time: '2026-10-15T07:58:37.529002'
duration_seconds: 210.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PIP5K1C-Related Neurodevelopmental Disorder
  mondo_id: MONDO:1010145
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 52
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:34211152
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 60
  verified: 57
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:1010145
    reported_labels:
    - MONDO supplied in request
    ontology_label: PIP5K1C-related neurodevelopmental disorder
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PIP5K1C-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:1010145 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PIP5K1C-Related Neurodevelopmental Disorder** covering all of the
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

# PIP5K1C-Related Neurodevelopmental Disorder  
## Disease-characteristics research report

**Current assessment (15 October 2026).** *PIP5K1C*-related neurodevelopmental disorder is an ultra-rare, autosomal-dominant developmental disorder caused by recurrent **de novo gain-of-function missense variants** in *PIP5K1C*. The best-defined phenotype is now named **neurodevelopmental disorder with intellectual, visual, and language impairment (NEDVIL; OMIM 621635)**. It is mechanistically and clinically distinct from **lethal congenital contracture syndrome 3 (LCCS3; OMIM 611369)**, which results from biallelic loss-of-function *PIP5K1C* variants. The foundational human evidence remains a 2023 cohort of nine unrelated children, so frequencies and prognosis should be treated as provisional. [31][10]

**Principal primary source:** Morleo M, et al. *American Journal of Human Genetics*. Published online **13 July 2023**; issue date **3 August 2023**. PMID **37451268**; PMCID **PMC10432144**; DOI **10.1016/j.ajhg.2023.06.012**; URL: https://pubmed.ncbi.nlm.nih.gov/37451268/ [31]

---

## 1. Disease information

### Definition and scope

NEDVIL is a congenital/early-childhood-onset Mendelian neurodevelopmental syndrome characterized by global developmental delay, intellectual and severe language impairment, motor delay, frequent epilepsy, acquired microcephaly, visual or ophthalmologic abnormalities, and a recognizable but variable craniofacial/skeletal phenotype. In the original cohort, all nine affected children had heterozygous de novo missense variants that increased PIP5KIγ activity and endosomal phosphatidylinositol-4,5-bisphosphate—PI(4,5)P₂—production. [31]

The defining abstract states:

> “We identified three de novo heterozygous missense variants in *PIP5K1C* … in nine unrelated children exhibiting intellectual disability, developmental delay, acquired microcephaly, seizures, visual abnormalities, and dysmorphic features.” — Morleo et al., 2023, PMID 37451268. [31]

### Identifiers and names

| Resource | Identifier/name | Status or interpretation |
|---|---|---|
| OMIM disease | **621635 — Neurodevelopmental disorder with intellectual, visual, and language impairment** | Current specific Mendelian phenotype; synonym **NEDVIL**. [10] |
| OMIM gene | **606102 — PIP5K1C** | Gene record; chromosome 19p13.3. [5] |
| HGNC | **HGNC:8996 — PIP5K1C** | Approved gene symbol. [22] |
| MONDO supplied in request | **MONDO:1010145** | Could not be independently confirmed in the accessible MONDO/MedGen records; retain only as a provisional knowledge-base mapping pending direct ontology-release validation. |
| Other MONDO mappings encountered | **MONDO:0100038**, “complex neurodevelopmental disorder,” and broader NDD mappings | GenCC currently uses MONDO:0100038 for the dominant gene–disease assertion; this is broader than NEDVIL. [3][41] |
| MedGen | **UID 1057551 — NEDVIL** | Linked to *PIP5K1C* and OMIM 621635. [76] |
| Orphanet | No disease-specific NEDVIL ORPHAcode located | The gene page lists *PIP5K1C* and ORPHA:160322 as a gene-related record, not a clearly disease-specific NEDVIL code. [1][6] |
| ICD-10/ICD-11 | No specific code | Code manifestations as appropriate, e.g., developmental disorder/intellectual disability, epilepsy, microcephaly, and visual impairment; avoid treating those nonspecific codes as equivalent to NEDVIL. |
| MeSH | No specific disease heading identified | “Neurodevelopmental Disorders,” “Intellectual Disability,” “Epilepsy,” and “Microcephaly” are potential broader indexing concepts. |
| Distinct allelic disease | **LCCS3, OMIM 611369; MONDO:0012656** | Biallelic loss-of-function disorder; not a synonym for NEDVIL. [8][25] |

**Common names:** *PIP5K1C*-related neurodevelopmental disorder; *PIP5K1C* gain-of-function neurodevelopmental disorder; NEDVIL; neurodevelopmental syndrome associated with altered phosphoinositide signaling.

**Source granularity:** Published information is aggregated from standardized clinical assessments of individual research/clinical cases, not routine population EHR data. Eight cases were identified by exome sequencing and one by genome sequencing; two were enrolled through the Undiagnosed Diseases Network or Telethon Undiagnosed Disease Program, while others were clinically ascertained and connected through Matchmaker Exchange/GeneMatcher. [53]

---

## 2. Etiology, risks, protection, and gene–environment interaction

### Causal factor

The established cause is a **germline heterozygous activating missense variant in the catalytic domain of PIP5KIγ**, encoded by *PIP5K1C*. Three recurrent variants accounted for the original nine cases:

1. NM_012398.3:c.436G>A, p.(Glu146Lys);
2. c.614A>G, p.(Tyr205Cys);
3. c.662A>G, p.(Tyr221Cys). [53]

These variants elevate PI(4,5)P₂, unlike LCCS3-associated biallelic variants that abolish or markedly reduce enzyme function and PI(4,5)P₂ synthesis. [5][19]

### Risk and protective factors

| Factor class | Evidence for NEDVIL |
|---|---|
| Causal genetic risk | A de novo activating *PIP5K1C* variant is the principal known risk and is sufficient to cause disease. |
| Parental age | Not assessed in the nine-person cohort. |
| Sex | Six males and three females were reported, but this sample is too small to establish a sex effect. |
| Family history | Usually negative because variants are de novo; parental germline mosaicism remains theoretically possible. |
| Environmental, infectious, lifestyle or occupational risks | None established. |
| Susceptibility loci/modifier genes | None validated. Other rare variants were evaluated in the discovery study, but no modifier was established. |
| Genetic protective factors | None known. The milder phenotype in one mosaic individual suggests that lower variant allele burden may reduce severity, but this is an observation, not an established protective allele. |
| Environmental protective factors | None demonstrated. |
| Gene–environment interaction | No disease-specific interaction has been studied. Seizure burden, access to therapy, nutrition, intercurrent illness, and sensory support could modify function or complications without altering the primary genetic cause. |

The mosaic p.Tyr221Cys individual was the least severely affected and had an IQ of 67, providing preliminary evidence for a dosage relationship; this is based on one case and requires replication. [40]

---

## 3. Phenotypes

### Cohort-level phenotype summary

Frequencies below are from only **nine** affected individuals aged 3–15 years and are not population estimates. [32]

| Phenotype type | Phenotype and suggested HPO term | Frequency | Onset, severity and course | Functional/QOL effect |
|---|---|---:|---|---|
| Developmental sign | Global developmental delay — **HP:0001263** | 9/9 | Infancy/early childhood; moderate to profound; chronic | Dependence for age-appropriate mobility, communication and self-care |
| Motor sign | Motor delay — **HP:0001270** | 9/9 | Early childhood; variable | Four or more individuals remained non-ambulatory; independent walking, when attained, could be delayed to 2–5 years |
| Behavioral/developmental sign | Speech/language delay — **HP:0000750**; absent speech **HP:0001344** where applicable | 9/9 | Early and persistent; usually severe | Most were nonverbal or used very few words; major communication limitation |
| Neurocognitive sign | Intellectual disability — **HP:0001249** | 9/9 | Developmental; moderate to severe/profound in most | IQs reported were 52, 57 and 67; marked adaptive-function impact |
| Neurologic sign | Seizure — **HP:0001250** | 7/9 | Childhood; variable; sometimes severe | Medication burden, injury risk and developmental interference |
| Neurologic sign | Infantile spasms — **HP:0012469** | 3/9 | Infancy | Three children developed severe developmental and epileptic encephalopathy |
| Growth sign | Acquired/postnatal microcephaly — **HP:0005484/HP:0011451** | 7/9 | Usually emerged after birth | Marker of altered brain growth; direct QOL effect not separately measured |
| Neurologic sign | Hypotonia — **HP:0001252** | 5/9 | Childhood; variable | Likely contributes to delayed sitting, walking, posture and therapy needs |
| Sensory/ocular | Visual impairment — **HP:0000505**, with variable ocular findings | 8/9 | Infancy/childhood; variable | Impairs orientation, communication, learning and mobility |
| Ocular | Strabismus — **HP:0000486** | Several cases | Childhood; variable | May affect binocular vision and require ophthalmic treatment |
| Ocular | Optic atrophy — **HP:0000648** / pale optic nerves | 2/9 optic-nerve abnormalities | Childhood | Potential irreversible visual loss |
| Ocular | Cerebral visual impairment — **HP:0100704** | Reported/probable in several | Childhood | Visual-processing limitations despite variable ocular anatomy |
| Skeletal | Skeletal abnormality | 6/9 | Congenital or childhood; heterogeneous | Can affect gait, posture and need for orthopedics |
| Cranial | Craniosynostosis — **HP:0001363** | Confirmed bilateral coronal synostosis in 1/9 | Congenital | One child required clinical management; not a universal feature |
| Skeletal | Scoliosis — **HP:0002650** | 1 reported | Childhood | Potential mobility and respiratory consequences with progression |
| Craniofacial sign | Prominent maxilla/upper lip | 9/9 | Congenital/persistent | Primarily diagnostic/dysmorphologic |
| Craniofacial sign | Micrognathia — **HP:0000347** | 6/9 | Congenital or historical | Potential feeding/airway implications, although these were not quantified |
| Craniofacial sign | Long ears — **HP:0000400** | 6/9 | Congenital | Primarily dysmorphic |
| Craniofacial sign | Hypertelorism — **HP:0000316** | Common, exact denominator not provided | Congenital | Primarily diagnostic |
| Neuroimaging sign | Abnormal white-matter signal — **HP:0002500** | Multiple cases | Childhood; nonspecific and inconsistent | Prognostic meaning unknown |
| Neuroimaging sign | Focal dysgyria/cortical malformation — **HP:0032046** or closest curated term | Several possible cases | Congenital | May contribute to epilepsy/developmental impairment, but causality is unproven |

Additional findings included myopia, hyperopia, astigmatism, nystagmus, delayed or deficient myelination, abnormal ventricular contours, cerebral atrophy, Chiari I malformation, hypoplastic anterior temporal lobes, coronal synostosis, prominent metopic ridge, talipes equinovarus, coxa valga, camptodactyly, clinodactyly, pes planus, and small feet. MRI findings were heterogeneous and were considered normal, nonspecific, or inconsistent on centralized review in the subset available. [53]

No disease-specific EQ-5D, SF-36, PROMIS, caregiver-burden or adaptive-behavior study has been published. The principal expected QOL burdens arise from nonverbal status, impaired mobility, epilepsy, visual impairment, intellectual disability, and lifelong dependence.

---

## 4. Genetic and molecular information

### Gene and protein

| Field | Annotation |
|---|---|
| Gene | *PIP5K1C* |
| HGNC | **HGNC:8996** |
| OMIM | **606102** |
| Location | **19p13.3** |
| Protein | Phosphatidylinositol-4-phosphate 5-kinase type 1 gamma, PIP5KIγ/PIP5Kγ |
| UniProt | **O60331** |
| Enzyme function | Phosphorylates phosphatidylinositol 4-phosphate, PI4P, to form PI(4,5)P₂ |
| Important processes | Actin organization, receptor and endosomal trafficking, clathrin/AP-2-mediated endocytosis, synaptic-vesicle endocytosis/exocytosis and cell adhesion/migration [61] |

### NEDVIL variants

| Variant, NM_012398.3 | Protein | Cases in 2023 cohort | Origin | Functional consequence | Population/classification evidence |
|---|---|---:|---|---|---|
| c.436G>A | p.(Glu146Lys) | 1 | De novo germline | Gain of function; surface-charge reversal may alter interactions | ClinVar VCV001172539; numerical gnomAD frequency not reported in the article |
| c.614A>G | p.(Tyr205Cys) | 2 | De novo germline | Gain of function; near ATP-binding region; increased PI(4,5)P₂ | ClinVar VCV001809611; absent/ultra-rare population evidence used in filtering |
| c.662A>G | p.(Tyr221Cys) | 6 | De novo; constitutional in five and mosaic in one | Gain of function; near ATP-binding region; increased PI(4,5)P₂ | ClinVar VCV001172538; ClinVar classifies it as pathogenic and reports absence from gnomAD. [46] |

All are missense substitutions in the amino-terminal portion of the kinase domain. Structural modeling suggested that Tyr205Cys and Tyr221Cys enlarge the ATP-binding-pocket cavity, potentially improving ATP access, whereas Glu146Lys changes local surface charge; those structural effects are **inferred**, while excess PI(4,5)P₂ production was experimentally demonstrated. [53]

### Distinct recessive allelic disorder

Biallelic loss-of-function *PIP5K1C* variants cause LCCS3: severe fetal akinesia/arthrogryposis, muscle atrophy, growth restriction and early death from respiratory insufficiency. The original homozygous p.Asp253Asn variant abolished kinase activity. A 2024 report added compound-heterozygous frameshifts c.949_952dup, p.(Ser318Ilefs*28), and c.688_689del, p.(Gly230Glnfs*114), in two affected fetuses. PMID **38491417**, published **15 March 2024**; URL: https://pubmed.ncbi.nlm.nih.gov/38491417/ [34]

**Important curation rule:** do not merge dominant gain-of-function NEDVIL with recessive loss-of-function LCCS3 into a single phenotype.

### Other molecular categories

- **Modifier genes:** none validated.
- **Epigenetic signature:** no NEDVIL-specific methylation episignature or pathogenic chromatin mechanism reported.
- **Chromosomal abnormalities:** no recurrent deletion, duplication, inversion or translocation defines the disorder.
- **Somatic disease:** no somatic oncogenic mechanism is established; the one mosaic case reflects postzygotic constitutional mosaicism.
- **Allele frequency:** exact gnomAD allele counts were not given for all three variants; pathogenic dominant variants are expected to be absent or extremely rare because of severe pediatric disease.
- **Pharmacogenomics:** no *PIP5K1C*-specific drug–gene prescribing guideline exists.

---

## 5. Environmental information

No toxin, radiation, pollution, diet, smoking, alcohol, occupation, lifestyle behavior or infectious agent is known to initiate NEDVIL. It is not infectious, contagious or zoonotic. Environmental and health-care factors may influence secondary outcomes—especially seizure control, nutrition, contractures, communication and visual development—but they are not established causes.

Consequently:

- CTD-style chemical associations with *PIP5K1C* should not be interpreted as proven disease risks.
- Vaccination, dietary avoidance and exposure reduction do not prevent the underlying variant.
- Standard infection prevention remains important in children with impaired mobility or feeding, but is supportive rather than disease-specific.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous de novo activating missense variant in the *PIP5K1C* kinase domain **leads to** excessive PIP5KIγ catalytic output.  
2. Increased PIP5KIγ activity **leads to** increased conversion of PI4P to PI(4,5)P₂, particularly in the early-endosomal compartment.  
3. Excess endosomal PI(4,5)P₂ **leads to** ectopic recruitment/polymerization of filamentous actin on EEA1-positive early endosomes.  
4. Abnormal actin coating **results in** defective early-endosomal cargo sorting and recycling, demonstrated by slower transferrin-receptor recycling.  
5. Defective membrane trafficking during development **is inferred to lead to** altered neuronal/synaptic development and function and impaired forebrain, eye and craniofacial morphogenesis.  
6. These developmental abnormalities **result in** developmental delay, intellectual and language impairment, epilepsy, acquired microcephaly, visual dysfunction and dysmorphism.  
7. **Branch:** altered trafficking and cytoskeletal regulation in developing skeletal/craniofacial tissues **is inferred to lead to** cranial-suture and limb/skeletal abnormalities.  
8. **Severity branch:** lower postzygotic variant burden from mosaicism **may lead to** a milder phenotype; this is supported by one individual only.

Morleo et al. summarized the central result as:

> “The *PIP5K1C* variants result in an increase of the endosomal PI(4,5)P2 pool, giving rise to ectopic recruitment of filamentous actin at early endosomes … that in turn causes dysfunction in EE trafficking.” [31]

### Experimental support

| Evidence system | Result | Interpretation |
|---|---|---|
| Patient fibroblasts, p.Tyr205Cys | Total PI(4,5)P₂ increased **1.6-fold**; early-endosomal PI(4,5)P₂ increased **2.4-fold** | Direct human-cell evidence of gain of function |
| Patient fibroblasts | Approximately **80%** of EEA1-positive endosomes associated with actin versus approximately **20%** in controls | Excess PI(4,5)P₂ drives abnormal endosomal F-actin |
| Patient fibroblasts | Transferrin binding was reduced and recycling was slower, while normalized internalization rate was comparable | Defective surface receptor re-exposure/endosomal recycling |
| Transfected fibroblast/HeLa models | All three NEDVIL variants generated more PI(4,5)P₂ than wild-type PIP5KIγ under comparable expression | Variant-specific biochemical activation |
| Protein turnover | Wild type and dominant variants had half-lives around six hours | Disease is not primarily due to increased protein stability |
| Zebrafish mRNA overexpression | Variant-injected larvae developed microcephaly, eye loss/microphthalmia and altered craniofacial cartilage | In-vivo developmental pathogenicity |
| Endogenous zebrafish base editing | Approximately **30%** of embryos edited at the homologous Glu146 site had microphthalmia and/or microcephaly | Independent in-vivo genetic support |

The authors caution that “the mechanistic link bridging these *PIP5K1C* gain-of-function variants … and the clinical manifestation … remain[s] to be determined and need[s] to be explored in neuronal tissue.” Thus, the lipid/endosome defect is demonstrated, but its precise neuronal-cell-type consequences remain partly inferred. [53]

### Suggested ontology annotations

| Category | Suggested terms |
|---|---|
| Molecular function | **GO:0016308**, 1-phosphatidylinositol-4-phosphate 5-kinase activity; **GO:0016301**, kinase activity |
| Biological process | **GO:0006661**, phosphatidylinositol biosynthetic process; **GO:0006897**, endocytosis; **GO:0045022**, early endosome to late endosome transport; **GO:0030036**, actin cytoskeleton organization; **GO:0048488**, synaptic vesicle endocytosis |
| Cellular component | **GO:0005769**, early endosome; **GO:0005886**, plasma membrane; **GO:0015629**, actin cytoskeleton; **GO:0030666**, endocytic vesicle membrane; **GO:0098794**, postsynapse |
| Chemicals | PI4P — **CHEBI:17526** or release-equivalent curated phosphoinositide term; PI(4,5)P₂ — **CHEBI:18348** or release-equivalent term; ATP — **CHEBI:15422** |
| Relevant cells | Neuron — **CL:0000540**; glutamatergic neuron — **CL:0000679**; GABAergic neuron — **CL:0000617**; retinal neuron — use the appropriate subtype; fibroblast — **CL:0000057** |
| Biological tissues | Cerebral cortex, forebrain, retina/optic pathway, craniofacial cartilage and skeletal tissue |

No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic or integrated multi-omic patient dataset has been reported. The direct lipid-immunostaining and trafficking assays are currently the most informative molecular profiling.

---

## 7. Anatomical structures affected

| Level | Structures/cells | Suggested ontology terms | Evidence |
|---|---|---|---|
| Primary organ | Brain/central nervous system | Brain **UBERON:0000955**; forebrain **UBERON:0001890**; cerebral cortex **UBERON:0000956** | Developmental impairment, epilepsy, microcephaly; heterogeneous MRI abnormalities |
| Sensory system | Eye, optic nerve and cerebral visual pathways | Eye **UBERON:0000970**; optic nerve **UBERON:0000966**; retina **UBERON:0000966** should be release-checked because identifiers may differ | Strabismus, cerebral visual impairment, optic atrophy, refractive errors |
| Craniofacial system | Cranial sutures, maxilla, mandible and facial skeleton | Skull **UBERON:0003129**; mandible **UBERON:0001684** | Coronal synostosis, metopic ridging, prominent maxilla and micrognathia |
| Musculoskeletal system | Spine, hips, hands, feet and joints | Vertebral column **UBERON:0001130**; limb joint **UBERON:0000982** | Scoliosis, coxa valga, talipes, camptodactyly and clinodactyly |
| Cellular | Developing neurons and neural progenitors are biologically plausible targets; direct patient-neuronal evidence is lacking | Neuron **CL:0000540**; neural progenitor cell **CL:0000047** | Inferred from phenotype and zebrafish forebrain defects |
| Subcellular | Plasma membrane, early endosome, cytosol, actin cytoskeleton and synaptic compartments | GO:0005886, GO:0005769, GO:0005829, GO:0015629 | Direct biochemical/cell-biological evidence [61][69] |

No consistent laterality is established. Eye and brain findings may be bilateral or asymmetric depending on the manifestation.

---

## 8. Temporal development

- **Onset:** congenital molecular lesion with manifestations emerging in infancy or early childhood. Motor and speech delay become apparent as milestones are missed; postnatal microcephaly develops after relatively less abnormal birth head circumference in many cases.
- **Course:** chronic and lifelong. Development may continue slowly, but affected children generally remain substantially delayed.
- **Epilepsy:** variable; infantile spasms were the first severe epilepsy presentation in three children.
- **Progression:** acquired microcephaly and scoliosis can evolve with age. There is no evidence for a primary neurodegenerative course, although follow-up only extended to age 15 years.
- **Stages:** no validated staging system exists.
- **Remission:** no spontaneous remission of the neurodevelopmental syndrome is reported. Individual seizures may respond to treatment, but response rates are unavailable.
- **Critical periods:** prenatal and early postnatal brain, visual-system and craniofacial development are likely biologically critical. Early seizure recognition, visual habilitation and developmental therapy are practical intervention windows, although no NEDVIL-specific controlled evidence exists.

---

## 9. Inheritance and population

| Characteristic | Current evidence |
|---|---|
| Inheritance | Autosomal dominant |
| Typical origin | De novo |
| Penetrance | Appears high for established activating variants, but cannot be quantified from nine ascertained cases |
| Expressivity | Variable; moderate-to-profound developmental disability, variable epilepsy and visual/skeletal involvement |
| Mosaicism | One postzygotic mosaic p.Tyr221Cys case, with comparatively mild presentation |
| Germline mosaicism | Not reported but cannot be excluded; recurrence risk is therefore low but above zero after a confirmed de novo result |
| Anticipation | Not applicable/no evidence |
| Founder effect | None identified for NEDVIL |
| Consanguinity | Not relevant to the usual dominant de novo phenotype; important in recessive LCCS3 |
| Carrier frequency | Not established; conventional unaffected “carriers” are not expected for highly penetrant activating variants |
| Prevalence/incidence | Unknown; no registry-based estimate |
| Sex ratio | Six male:three female in the discovery cohort; insufficient evidence for sex bias |
| Geographic/ethnic distribution | Cases were unrelated and internationally ascertained; no ethnic or geographic enrichment demonstrated |
| Age distribution | Published individuals were 3–15 years old at last evaluation |

At the time of the 2023 report, only nine molecularly confirmed NEDVIL cases were described. Therefore, neither prevalence per 100,000 nor annual incidence can be calculated responsibly.

---

## 10. Diagnostics

### Recommended diagnostic approach

1. **Recognize the phenotype:** unexplained global developmental delay/intellectual disability with profound speech impairment, motor delay, acquired microcephaly, epilepsy and visual abnormalities, particularly with prominent upper lip/maxilla, micrognathia or skeletal findings.
2. **Order trio exome or genome sequencing**, preferably with copy-number analysis and sufficient read-level review to detect low-level mosaicism. ACMG strongly recommends exome/genome sequencing as a first- or second-tier test for pediatric congenital anomalies or DD/ID. PMID **34211152**, published July 2021; URL: https://pubmed.ncbi.nlm.nih.gov/34211152/ [120][122]
3. Alternatively, use a comprehensive neurodevelopmental/epilepsy panel that includes *PIP5K1C* and detects single-nucleotide variants, small indels and mosaicism.
4. Confirm a candidate variant by an orthogonal method if needed and test both parents to establish de novo occurrence.
5. Interpret **mechanism-specifically**: dominant catalytic-domain activating missense variants support NEDVIL; biallelic loss-of-function variants support LCCS3.
6. Reanalyse negative exome/genome data as gene–disease knowledge evolves.

### Utility of test types

| Test | Utility |
|---|---|
| Trio WES | High; identified eight of the original nine cases |
| Trio WGS | High; identified one original case and can better detect structural/noncoding variation and mosaicism |
| NDD/epilepsy panel | Reasonable if *PIP5K1C* is included and coverage is adequate |
| Single-gene sequencing | Appropriate after a highly suggestive phenotype or known familial variant; less efficient for nonspecific DD/ID |
| CMA | Useful for the broader DD/ID differential but will usually miss the causal single-nucleotide variants |
| Karyotype/FISH | Not routinely informative unless another chromosomal disorder is suspected |
| RNA sequencing | Research/adjunctive use for suspected splice variants; no established NEDVIL RNA signature |
| Mitochondrial/repeat-expansion testing | Not indicated specifically unless the phenotype suggests an alternative disorder |
| Biochemical assay | No validated clinical PI(4,5)P₂ or PIP5KIγ enzyme diagnostic assay |
| Prenatal testing | Targeted testing is possible once a familial pathogenic variant is known |

### Clinical assessments after diagnosis

- Developmental, cognitive, language and adaptive-function testing.
- EEG for seizures, regression, suspicious spells or sleep-related events.
- Brain MRI, particularly with epilepsy, microcephaly, focal neurologic signs or regression.
- Formal ophthalmology and functional-vision assessment.
- Serial head circumference, height, weight and nutritional review.
- Orthopedic examination for scoliosis, contractures, feet/hip abnormalities.
- Craniofacial/neurosurgical evaluation if craniosynostosis is suspected.
- Feeding/swallowing assessment where clinically indicated.

No standardized clinical criteria or laboratory biomarker can replace molecular diagnosis.

### Differential diagnosis

Broad differentials include genetic developmental and epileptic encephalopathies, phosphoinositide disorders such as Lowe syndrome and other PI-metabolism disorders, syndromic microcephaly with visual impairment, tubulinopathies/cortical-malformation syndromes, and other disorders with severe speech impairment and craniosynostosis. Distinguishing NEDVIL requires the characteristic *PIP5K1C* activating variant and, when needed, functional evidence.

---

## 11. Outcome and prognosis

- **Survival:** no NEDVIL deaths were reported through ages 3–15 years. Five- and ten-year survival rates and life expectancy are unknown.
- **Development:** morbidity is substantial. Most original cases were nonverbal or minimally verbal, and several remained non-ambulatory.
- **Epilepsy:** present in 7/9; infantile spasms/DEE in 3/9 may predict greater developmental burden.
- **Vision:** visual or ocular abnormalities affected 8/9 and may compound developmental disability.
- **Prognostic indicators:** mosaicism/lower variant burden may be associated with milder severity; epilepsy severity, degree of visual impairment and ability to acquire independent mobility are plausible clinical predictors but are unvalidated.
- **Recovery:** no cure or reversal of the developmental phenotype has been reported. Developmental gains can occur, and functional potential may improve with seizure control, vision support, communication systems and rehabilitation.
- **Disease-specific mortality:** unknown and not shown to be elevated in the limited NEDVIL cohort.
- **Do not extrapolate LCCS3 mortality:** perinatal respiratory death is characteristic of severe recessive loss of function, not demonstrated for dominant NEDVIL.

---

## 12. Treatment and management

There is **no approved disease-modifying treatment**, no published NEDVIL treatment trial, and no reliable treatment-response percentage. Management is multidisciplinary and manifestation-directed.

| Intervention | Indication/strategy | Suggested NCIT concept |
|---|---|---|
| Antiseizure medication | Select according to seizure type and standard pediatric epilepsy practice; urgent treatment of infantile spasms | Anticonvulsant therapy; **NCIT:C15313** or current release equivalent |
| Ketogenic diet, epilepsy surgery or neuromodulation | Consider only for refractory epilepsy after specialist evaluation; no NEDVIL-specific outcomes | Ketogenic diet; epilepsy surgery; vagus nerve stimulation |
| Physical therapy | Hypotonia, gross-motor delay, contracture prevention, mobility | Physical therapy **NCIT:C15300** or release equivalent |
| Occupational therapy | Fine-motor skills, adaptive equipment, self-care and sensory needs | Occupational therapy |
| Speech-language therapy | Severe receptive/expressive language impairment | Speech therapy |
| AAC | Early augmentative and alternative communication for nonverbal/minimally verbal individuals | Assistive communication device/intervention |
| Vision services | Refraction, strabismus management, low-vision and cerebral-visual-impairment habilitation | Ophthalmologic examination; vision rehabilitation |
| Nutritional/feeding support | Poor oral intake, dysphagia or growth problems | Nutritional support; feeding therapy |
| Orthopedic care | Scoliosis, talipes, hip/hand/foot abnormalities | Orthopedic procedure/orthosis as appropriate |
| Craniofacial surgery | Confirmed clinically significant craniosynostosis | Craniosynostosis repair |
| Psychological/social support | Family support, individualized education plan, respite and disability services | Supportive care |

### Experimental approaches

Because disease variants increase PIP5KIγ activity, selective kinase inhibition is mechanistically attractive. Morleo et al. stated, “From a clinical point of view, PIP5Ks represent attractive therapeutic targets,” but no rescue was demonstrated in patient neurons or affected children. [109]

UNC3230 lowers PIP₂ in dorsal-root-ganglion neurons and reduced nociceptive hypersensitivity in mouse pain models, but it also inhibits PIP4K2C and has not been tested as NEDVIL therapy. PMID **24853942**. [110] In 2024, medicinal-chemistry work reported novel potent bicyclic-pyrazole PIP5K1C inhibitors, but these remain preclinical and have no established pediatric CNS safety, selectivity, dosing or developmental benefit. [107]

Gene replacement would be biologically inappropriate without allele-specific control because NEDVIL is a gain-of-function disorder. Potential future strategies include allele-selective silencing, targeted RNA interference/ASOs or selective PIP5KIγ inhibition, but none has entered disease-specific clinical testing.

---

## 13. Prevention

### Primary prevention

There is no lifestyle, vaccine or environmental intervention that prevents a spontaneous de novo mutation. General preconception health measures do not specifically alter NEDVIL risk.

### Secondary prevention and early detection

- Prompt genetic evaluation of unexplained DD/ID, epilepsy, postnatal microcephaly and visual impairment.
- Early EEG when spasms or developmental regression are suspected.
- Early ophthalmology/functional-vision assessment.
- Immediate developmental, speech, PT/OT and AAC referral without waiting for a molecular diagnosis.

There is no newborn biochemical screening program for NEDVIL and insufficient evidence to support population screening.

### Reproductive prevention/counseling

- Offer formal genetic counseling after molecular confirmation.
- Test parents using a method sensitive to low-level mosaicism where possible.
- If the variant is absent from parental blood, recurrence risk is low but not zero because of possible germline mosaicism.
- If a parent is mosaic or constitutionally positive, recurrence risk may approach 50%, modified by germline allele fraction.
- Targeted prenatal diagnosis by chorionic-villus sampling or amniocentesis and preimplantation genetic testing for monogenic disease are technically feasible after identification of the familial variant.
- Cascade testing is appropriate for a mosaic/affected parent or an unexpectedly familial variant, but routine testing of distant relatives is not useful for a confirmed de novo case.

### Tertiary prevention

Prevent secondary complications through seizure control, aspiration and nutrition surveillance, mobility/contracture programs, scoliosis monitoring, visual habilitation, communication support and individualized educational planning.

---

## 14. Other species and naturally occurring disease

| Species | Taxon | Ortholog/model relevance | Natural disease |
|---|---:|---|---|
| Human, *Homo sapiens* | NCBI Taxon **9606** | *PIP5K1C*, HGNC:8996 | NEDVIL and LCCS3 |
| Mouse, *Mus musculus* | **10090** | *Pip5k1c*, MGI:1298224 | Experimental alleles cause neonatal/embryonic lethality and neurologic, synaptic, visual and homeostatic abnormalities. [96] |
| Zebrafish, *Danio rerio* | **7955** | Paralogs *pip5k1ca* and *pip5k1cb* | Engineered gain-of-function models reproduce microcephaly, eye and craniofacial abnormalities. [7][90] |

No well-established naturally occurring *PIP5K1C*-associated veterinary syndrome, breed predisposition or OMIA disease entry was identified. Consequently, no VBO breed term is applicable. There is no zoonotic transmission or cross-species contagion.

The pathway is evolutionarily conserved: zebrafish *pip5k1ca* and *pip5k1cb* proteins were reported as approximately 71% and 62% identical to human PIP5KIγ, respectively, supporting comparative functional modeling.

---

## 15. Model organisms and experimental systems

| Model | Genetic/manipulation type | Phenotype and application | Limitations/resources |
|---|---|---|---|
| Patient dermal fibroblasts | Endogenous heterozygous p.Tyr205Cys | Increased total/endosomal PI(4,5)P₂, excess early-endosomal F-actin, impaired transferrin recycling | Non-neuronal; available evidence came from one affected individual |
| HeLa/control fibroblast overexpression | Wild type, three dominant variants and recessive p.Asp253Asn comparator | Demonstrated variant-dependent PI(4,5)P₂ gain of function and endosomal actin recruitment | Overexpression may exceed physiological protein levels |
| Zebrafish mRNA model | One-cell-stage expression of human mutant mRNA | p.Glu146Lys: 46% eye/microcephaly plus 3.4% severe no-eye phenotype; p.Tyr205Cys: 32.7% plus 6.7%; p.Tyr221Cys: 32% plus 14% | Transient overexpression; mortality 27%–57.5%; not a stable heterozygous humanized line [90] |
| Zebrafish base-editing model | Endogenous *pip5k1ca* Glu146-region edit | About 30% developed microphthalmia and/or microcephaly | Editing mosaicism and imperfect amino-acid equivalence; only one variant modeled |
| Global mouse knockout | *Pip5k1c* null | Roughly 50% reduction in brain PIP₂, impaired mobility/feeding, synaptic-vesicle defects and death within 24 hours | Models loss of function/LCCS3 biology, not dominant NEDVIL gain of function [72][74] |
| Conditional sensory-neuron mouse knockout | Tissue-specific *Pip5k1c* deletion | Early-onset proprioceptive deficit and altered pain signaling | Relevant to neuronal function but opposite molecular direction from NEDVIL [104] |
| Future preferred models | Heterozygous knock-in mouse, patient iPSC-derived cortical neurons/retinal organoids, cerebral organoids | Could test cell-type specificity, neuronal trafficking, network excitability, variant dosage and therapeutic rescue | No such published NEDVIL model was located |

In the landmark knockout mouse study, reduced brain PI(4,5)P₂ produced decreased miniature-current frequency, enhanced synaptic depression, a smaller readily releasable vesicle pool, delayed endocytosis and slower vesicle recycling. PMID **15386003**. This establishes that tightly regulated PIP5KIγ activity is essential for synaptic-vesicle trafficking, although it models deficient rather than excessive kinase activity. [72]

---

## Evidence appraisal and knowledge gaps

1. **Human evidence strength:** convincing gene–disease relationship based on recurrent de novo variants, clustering in the kinase domain, functional gain-of-function data and in-vivo zebrafish phenocopy.
2. **Main limitation:** only nine published NEDVIL individuals in the defining cohort; ascertainment strongly favors severe pediatric cases.
3. **Key unresolved questions:** full variant spectrum, penetrance, adult natural history, epilepsy treatment response, genotype–phenotype correlations, neuronal and retinal cell-type mechanisms, and whether selective kinase inhibition can safely normalize—not over-suppress—PI(4,5)P₂.
4. **Ontology caution:** **MONDO:1010145 could not be independently verified** against the accessible records; OMIM **621635/NEDVIL** is currently the most specific, clearly supported disease identifier.
5. **Clinical distinction:** dominant gain-of-function NEDVIL and recessive loss-of-function LCCS3 must remain separate knowledge-base entities, connected as allelic disorders rather than synonyms.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:34211152` (2 mentions) - Exome and genome sequencing for pediatric patients with congenital anomalies or intellectual disability: an evidence-based clinical guideline of the American College of Medical Genetics and Genomics (ACMG).
  - shared terms: developmental

Weighed against this report's own most characteristic terms: `nedvil`, `variant`, `pip5k1c`, `developmental`, `visual`, `phenotype`, `epilepsy`, `microcephaly`, `disease`, `impairment`, `novo`, `craniofacial`, `abnormalitie`, `severe`, `disorder`, `affected`, `function`, `mosaicism`, `dominant`, `individual`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1010145` (2 mentions) - the report calls it "MONDO supplied in request"; MONDO calls it **PIP5K1C-related neurodevelopmental disorder**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:8996` - called "PIP5K1C", "HGNC"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.