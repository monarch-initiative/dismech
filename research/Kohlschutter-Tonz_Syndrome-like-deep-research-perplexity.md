---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T14:37:57.690848'
end_time: '2026-10-27T14:45:27.685442'
duration_seconds: 449.99
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Kohlschutter-Tonz Syndrome-like
  mondo_id: MONDO:0030990
  category: Genetic
  causal_genes: SATB1
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 54
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 8
  validator_version: 0.4.0
term_validation:
  total_terms: 65
  verified: 62
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 16
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000060
    reported_labels:
    - Ameloblast
    - Presecretory and secretory ameloblasts
    ontology_label: odontoblast
  labels_variant: 4
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
- **Disease Name:** Kohlschutter-Tonz Syndrome-like
- **MONDO ID:** MONDO:0030990 (if available)
- **Causal gene(s):** SATB1
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Genetic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Kohlschutter-Tonz Syndrome-like** covering all of the
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

# Kohlschutter–Tonz syndrome-like: comprehensive disease-characteristics report

## Executive summary

**Kohlschutter–Tonz syndrome-like disease is caused by heterozygous pathogenic variants in the chromatin organizer and transcription factor gene *SATB1*.** The preferred contemporary name is **den Hoed–de Boer–Voisin syndrome (DHDBV)** or **intellectual disability–epilepsy–dental anomalies–facial dysmorphism syndrome**. It is an autosomal-dominant, usually de novo neurodevelopmental disorder characterized by developmental delay, moderate-to-profound intellectual disability, severe speech impairment, hypotonia or spasticity, early-onset epilepsy, behavioral abnormalities, distinctive but variable facial features, and dental/enamel abnormalities. Importantly, this entry is **not** classic autosomal-recessive, *ROGDI*-related Kohlschütter–Tönz syndrome and should not be merged with it. MedGen maps the SATB1 disorder to MONDO:0030990 and OMIM 619229. [18][214]

The defining 2021 human study evaluated 42 people with *SATB1* variants and demonstrated mutation-specific phenotypes. Its central conclusion was: **“Missense variants in the CUT1 and CUT2 DNA-binding domains result in stronger chromatin binding, increased transcriptional repression, and a severe phenotype.”** By contrast, *SATB1* haploinsufficiency and C-terminal truncating variants usually produce the milder allelic disorder DEFDA, OMIM 619228. The severe CUT-domain missense phenotype is the best match to MONDO:0030990/OMIM 619229. [91][214][264]

**Evidence status:** extremely rare; one principal international cohort, several individual reports, functional cell assays, dental knockout-mouse experiments, and a 2025 truncating-rat model. No disease-specific guideline, validated natural-history scale, approved molecular therapy, or registered interventional trial was identified.

---

## 1. Disease information

### 1.1 Definition

DHDBV/KTZSL is a syndromic neurodevelopmental disorder in which dysregulated SATB1-mediated chromatin binding and transcription particularly affect brain development and tooth-enamel formation. Most established severe cases carry heterozygous missense substitutions clustered in the CUT1 or CUT2 DNA-binding domains. The phenotype resembles Kohlschütter–Tönz syndrome because both include epilepsy, severe neurodevelopmental impairment, and enamel/dental abnormalities, but their genes and inheritance differ. [46][264]

### 1.2 Identifiers and nomenclature

| Resource | Identifier/name | Status or interpretation |
|---|---|---|
| MONDO | **MONDO:0030990** — Kohlschutter-Tonz syndrome-like | Target disease specified in the request and cross-referenced by MedGen. [122] |
| OMIM phenotype | **619229** — Den Hoed-de Boer-Voisin syndrome; DHDBV | Autosomal dominant; caused by heterozygous *SATB1* variants. [214] |
| OMIM gene | **602075** — *SATB1* | Gene entry. [38] |
| Orphanet | **ORPHA:684232** — Intellectual disability–epilepsy–dental anomalies–facial dysmorphism syndrome | Synonym: den Hoed–De Boer–Voisin syndrome; prevalence category <1 per 1,000,000. [121] |
| MedGen | **C5543202**, UID 1781649 | Kohlschutter-Tonz syndrome-like; gene *SATB1*. [122] |
| HGNC | **HGNC:10541** | Official gene symbol *SATB1*. [36] |
| NCBI Gene | **6304** | Human *SATB1*, chromosome 3p24.3. [1] |
| ICD-10/ICD-11 | No disease-specific code identified | Use local coding for genetic neurodevelopmental disorder, intellectual disability, epilepsy, and dental anomaly as appropriate; these are not equivalent to a dedicated DHDBV code. |
| MeSH | No disease-specific descriptor identified | Indexing generally falls under intellectual disability, developmental disabilities, epilepsy, amelogenesis imperfecta, and genetic diseases. |
| GeneReviews | No dedicated GeneReview identified | NCBI Gene explicitly reports “GeneReviews: Not available.” [27] |

**Synonyms**

- Den Hoed–de Boer–Voisin syndrome  
- DHDBV  
- Kohlschutter–Tonz syndrome-like  
- KTZSL  
- Intellectual disability–epilepsy–dental anomalies–facial dysmorphism syndrome  
- SATB1-related neurodevelopmental disorder, severe CUT-domain missense form

The milder allelic condition **developmental delay with dysmorphic facies and dental anomalies (DEFDA; OMIM 619228; MONDO:0030988)** should remain a related but distinct entry. [28][132]

### 1.3 Data provenance

The disease description is an **aggregated disease-level synthesis**, principally from an international research cohort assembled through exome/genome sequencing and clinical collaborations—not an EHR-derived population study. The 2021 report included 42 molecularly ascertained individuals across the broader SATB1 spectrum; OMIM assigned 28 individuals with heterozygous missense variants to DHDBV/KTZSL. [197][214]

---

## 2. Etiology, risk and protective factors

### 2.1 Primary cause

- **Cause:** heterozygous germline pathogenic variants in *SATB1*, especially missense substitutions affecting the CUT1 or CUT2 DNA-binding domains.
- **Molecular category:** abnormal chromatin binding and excessive transcriptional repression—best described as an **altered-function/hypermorphic or gain-of-abnormal-function mechanism**, rather than simple haploinsufficiency.
- **Variant origin:** usually de novo, but inherited and parental-mosaic cases occur.
- **Non-genetic cause:** none established.

In the full 2021 SATB1 cohort, 28 variants were de novo, three inherited from an affected parent, five arose through known or suspected parental mosaicism, two were inherited from reportedly unaffected parents, and inheritance was unresolved in four. These totals span both SATB1 phenotypes and therefore should not be interpreted as KTZSL-specific penetrance estimates. [197]

### 2.2 Risk factors

| Risk-factor class | Current evidence |
|---|---|
| Pathogenic *SATB1* allele | Principal and sufficient risk factor. CUT1/CUT2 missense variants confer the strongest risk for the severe DHDBV phenotype. |
| Affected parent | Each pregnancy has a theoretical 50% probability of inheriting a heterozygous allele, although severity and penetrance may vary. |
| Parental germline/somatic mosaicism | Documented or suspected in several families; recurrence risk can therefore exceed the usual low risk after an apparently de novo variant. |
| Family history | Often absent because most variants are de novo. |
| Sex | No established sex-specific risk. |
| Ethnicity/geography | No founder population or ancestry enrichment established. |
| Maternal age, paternal age, toxins, diet or infection | No disease-specific association demonstrated. |

### 2.3 Protective factors

No protective allele, modifier locus, diet, exposure, or medication has been shown to prevent penetrance. Control missense variants p.Ser366Leu, p.Val519Leu and p.Ala573Thr showed wild-type-like behavior in the original functional assays, but they are benign/control alleles rather than demonstrated protective variants. [197]

### 2.4 Gene–environment interaction

No formal gene–environment interaction has been reported. Seizure burden, intercurrent illness, sleep disruption and access to developmental therapy may affect clinical functioning, but these are modifiers of morbidity, not proven causes of the syndrome. Pregnancy and delivery abnormalities occurred in subsets of the original cohort without a consistent causal pattern. [91]

---

## 3. Phenotypes

Because the main publication pooled severe missense and milder truncating cases, the **missense column is the best published quantitative approximation of KTZSL**, but it may include a small number of variants later considered uncertain. Frequencies are percentages among individuals assessed, not population prevalence. [91]

### 3.1 Core and associated phenotypes

| Phenotype/type | KTZSL/missense frequency | Onset, severity and course | Functional/QOL effect | Suggested HPO term |
|---|---:|---|---|---|
| Global developmental delay; clinical sign | 23/24, **96%** | Infancy/early childhood; usually persistent | Dependence in learning and daily activities | Global developmental delay — **HP:0001263** |
| Intellectual disability | 20/21, **95%** | Developmental; moderate to profound is characteristic | Major effect on education, autonomy and communication | Intellectual disability — **HP:0001249** |
| Severe/profound ID | 12/21, **57%** | Lifelong | Often requires continuous support | Severe ID — HP:0010864; profound ID — HP:0002187 |
| Motor delay | 23/25, **92%** | Infancy; variable acquisition of sitting/walking | Mobility limitation; need for PT and assistive devices | Motor delay — **HP:0001270** |
| Speech/language delay | 22/24, **92%** | Early childhood; some remain nonverbal | Major communication impairment | Delayed speech and language — **HP:0000750** |
| Dysarthria | 5/9, **56%** | Childhood | Reduces intelligibility; may require AAC | Dysarthria — **HP:0001260** |
| Epilepsy | 20/25, **80%** | Often infancy or early childhood; may be refractory | Injury risk, hospitalization and interruption of development | Seizure — **HP:0001250**; epileptic encephalopathy — HP:0200134 |
| EEG abnormality | 17/17, **100%** assessed | May include hypsarrhythmia, multifocal discharges or focal epileptiform activity | Guides treatment; sleep activation may occur | Abnormal EEG — **HP:0002353** |
| Hypotonia | 23/25, **92%** | Usually infantile/childhood; may coexist with later spasticity | Feeding, posture and motor difficulties | Hypotonia — **HP:0001252** |
| Spasticity | 10/24, **42%** | Variable, sometimes later | Contracture, gait and care burden | Spasticity — **HP:0001257** |
| Ataxia | 4/15, **27%** | Variable | Balance and gait impairment | Ataxia — **HP:0001251** |
| Developmental regression | 5/23, **22%** | Episodic or following seizure burden in some patients | Loss of skills; major caregiver impact | Neurodevelopmental regression — HP:0012759 |
| Behavioral disturbance | 17/22, **77%** | Childhood onward | Autism features, anxiety or other maladaptive behavior can affect participation | Behavioral abnormality — **HP:0000708**; autism — HP:0000717 |
| Sleep disturbance | 9/18, **50%** | Variable/chronic | Patient and caregiver sleep impairment | Sleep abnormality — **HP:0002360** |
| Abnormal brain imaging | 14/24, **58%** | Nonspecific and variable | Usually supportive rather than diagnostic | Abnormal CNS morphology — HP:0012639 |
| Dental/oral abnormality | 18/23, **78%** | Apparent with tooth eruption; chronic | Fragility, decay, chewing difficulty, pain and cosmetic impact | Abnormality of teeth — **HP:0000164** |
| Enamel discoloration/hypoplasia or AI-like enamel | Qualitatively common; exact subfeature frequency unavailable | Primary and/or permanent teeth; persistent | Sensitivity, accelerated wear and dental-care burden | Amelogenesis imperfecta — **HP:0000705**; enamel hypoplasia — HP:0006297 |
| Widely spaced/malpositioned or missing teeth | Qualitatively reported | Childhood with eruption | Feeding, articulation and appearance | Widely spaced teeth — **HP:0000687**; hypodontia — HP:0000668 |
| Facial dysmorphism | 17/25, **68%** | Congenital; generally stable | Usually limited direct functional effect | Abnormal facial shape — **HP:0001999** |
| Drooling/dysphagia | 9/20, **45%** | Childhood; variable | Aspiration, nutrition and social burden | Drooling — **HP:0002307**; dysphagia — HP:0002015 |
| Vision abnormality | 9/20, **45%** | Variable | May further impair development and mobility | Visual impairment — **HP:0000505** |
| Skeletal/limb abnormality | 11/23, **48%** | Congenital/developmental | Variable effect on mobility | Abnormality of skeletal system — HP:0000924 |
| Joint hypermobility | 5/17, **29%** | Variable | Instability, fatigue or pain | Joint hypermobility — **HP:0001382** |
| Gastrointestinal abnormality | 14/21, **67%** | Often feeding-related; details heterogeneous | Growth and nutrition burden | GI abnormality — HP:0011024 |
| Urogenital abnormality | 5/19, **26%** | Nonspecific | Patient dependent | Genitourinary abnormality — HP:0000119 |
| Endocrine/metabolic abnormality | 9/19, **47%** | Heterogeneous, no defining biomarker | Patient dependent | Endocrine abnormality — HP:0000818 |
| Immunologic abnormality | 6/17, **35%** | Heterogeneous; not a defining immunodeficiency | Uncertain | Immune-system abnormality — HP:0002715 |
| Cardiac abnormality | 3/21, **14%** | Usually congenital/nonspecific | Depends on lesion | Cardiovascular abnormality — HP:0001626 |
| Microcephaly | 6/22, **27%** | Usually postnatal in the cohort | Marker of neurodevelopmental severity | Microcephaly — **HP:0000252** |
| Abnormal weight | 12/18, **67%** | Both underweight and overweight reported | Nutrition and care burden | Abnormal body weight — HP:0004323 |

The broader cohort’s abstract-level phenotype summary was: developmental delay 97%, intellectual disability 90%, hypotonia 76%, epilepsy 61%, behavioral problems 71%, facial dysmorphism 67%, and dental abnormalities 71%. The authors directly observed that missense cases were substantially more severe: epilepsy 80% versus 18% in truncating/deletion cases, hypotonia 92% versus 42%, and spasticity 42% versus 0%. [91]

### 3.2 Dysmorphic and dental details

Reported facial findings include facial asymmetry, high forehead, prominent ears, straight/full eyebrows, puffy eyelids, downslanting palpebral fissures, low nasal bridge, full nasal tip/alae, lip-shape differences, and retrognathia. No single feature is obligatory.

Dental findings include widely spaced teeth, fragility, missing teeth, disorganized positioning, decay and enamel discoloration. The human phenotype has been described as “amelogenesis-imperfecta-like,” but formal dental imaging or histology has not been reported for every patient.

### 3.3 Quality of life evidence

No KTZSL-specific EQ-5D, SF-36, PROMIS or caregiver-burden study was found. Expected major determinants are seizure control, communication ability, mobility, feeding safety, behavior, sleep and dental pain. This is clinical inference, not a validated disease-specific QOL result.

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Item | Annotation |
|---|---|
| Gene | *SATB1*, SATB homeobox 1 |
| HGNC | HGNC:10541 |
| NCBI Gene | 6304 |
| OMIM gene | 602075 |
| Location | 3p24.3 |
| Protein function | Nuclear matrix/scaffold-associated DNA-binding protein; chromatin-loop organizer; recruits chromatin-remodeling factors and regulates transcription. [1] |
| Principal disease transcript in discovery paper | NM_001131010.4 |
| Current commonly used RefSeq in ClinVar | NM_002971.6 |
| Relevant domains | N-terminal oligomerization region, CUT1, CUT2 and homeobox domain |
| Expression/localization | Nuclear, particularly nucleoplasm and nuclear bodies; enriched in CNS neurons and immune/T cells. [136][146] |

### 4.2 Pathogenic variant spectrum

Reported KTZSL-associated or candidate severe missense changes include:

| Protein change | cDNA where established | Domain | Evidence/interpretation |
|---|---|---|---|
| p.Gln402Arg | c.1205A>G | CUT1 | Recurrent disease-cluster residue |
| p.Glu407Gly | c.1220A>G | CUT1 | Functional stronger binding/repression; ClinVar pathogenic for KTZSL. [211] |
| p.Glu407Gln | c.1219G>C | CUT1 | De novo severe-phenotype case. [209] |
| p.Glu413Lys | Not consistently reported in searchable text | CUT1 | Disease-cohort variant |
| p.Gln420Arg | c.1259A>G | CUT1 | De novo; stronger chromatin binding and increased IL2-promoter repression |
| p.Gln525Arg | c.1574A>G; rs1695858904 | CUT2 | Familial/suspected mosaic cases; ClinVar pathogenic. [196][211] |
| p.Glu530Gly | cDNA not recovered | CUT2 | Disease-cohort variant |
| p.Glu530Lys | c.1588G>A; rs1694399198 | CUT2 | Recurrent de novo pathogenic variant; absent from gnomAD v2.1.1 in cited assessment; functional evidence. [213] |
| p.Glu530Gln | c.1588G>C | CUT2 | Functional stronger chromatin binding/repression |
| p.Glu547Lys | c.1639G>A | CUT2 | Functional stronger chromatin binding/repression |
| p.His577Arg | cDNA not recovered | Near/within CUT2 region | Cohort candidate |
| p.Pro181Leu | cDNA not recovered | N-terminal/CUTL region | Reported in cohort; mechanism less well established |

The discovery cohort also contained p.Leu682Val in the homeobox domain, but assays were wild-type-like and the patient carried a pathogenic *FOXP2* duplication; the authors considered p.Leu682Val unlikely to explain that phenotype. [91]

**Classification caution:** ClinVar classifications are variant- and condition-specific and are often based on one or a few submitters. The strongest KTZSL assertions concern recurrent CUT-domain variants with de novo, case-enrichment and functional evidence. ClinGen’s September 17, 2024 expert curation classified the broader relationship between *SATB1* and autosomal-dominant complex neurodevelopmental disorder as **definitive**. [181][256]

### 4.3 Population frequency and constraint

The pathogenic CUT-domain variants are absent or exceptionally rare in population databases. In gnomAD v2.1.1, *SATB1* showed strong constraint:

- predicted loss-of-function observed/expected: **0.15 (95% interval 0.08–0.29)**
- missense observed/expected: **0.46 (0.41–0.52)**. [197]

No reliable carrier-frequency estimate can be calculated because the syndrome is dominant, usually de novo, and many possible private variants exist.

### 4.4 Germline, mosaic and structural variation

- Established disease variants are primarily **germline heterozygous**.
- Low-level parental mosaicism has been demonstrated; in one family, a mother carried p.Glu407Gly in approximately 1.4% of peripheral-blood reads and transmitted it to three children.
- Partial *SATB1* deletions and loss-of-function variants cause the overlapping, generally milder DEFDA spectrum rather than prototypical KTZSL.
- Large duplications/triplications involving 3p24.3 are not yet proven to cause KTZSL through SATB1 triplosensitivity.

### 4.5 Modifier and epigenetic data

No validated human modifier gene, DNA-methylation episignature, histone signature or diagnostic chromatin profile has been established. Because SATB1 organizes chromatin and recruits histone acetyltransferase/deacetylase complexes, downstream epigenetic dysregulation is biologically plausible, but no disease-specific patient episignature is validated.

---

## 5. Environmental, lifestyle and infectious information

No toxin, radiation exposure, pollution source, occupational exposure, diet, smoking behavior, alcohol exposure or infectious agent is known to cause KTZSL. These categories are therefore **not applicable as primary etiology**.

General factors can modify complications—for example, missed antiseizure medication, sleep loss or fever can worsen seizures—but disease-specific interaction statistics are unavailable. The syndrome is not infectious, transmissible or zoonotic.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **A heterozygous pathogenic missense variant in the SATB1 CUT1 or CUT2 DNA-binding domain leads to** altered charge/structure at or near the DNA-binding interface.  
2. **The altered interface leads to** abnormally stabilized SATB1 binding to chromatin and a clustered, cage-like nuclear distribution.  
3. **Stronger chromatin engagement leads to** excessive repression of at least some SATB1-responsive regulatory elements; this was demonstrated in reporter assays but the complete disease-relevant target set remains unknown.  
4. **Aberrant transcriptional control is inferred to lead to** disturbed neuronal differentiation, interneuron development/migration, dendritic maturation and excitation–inhibition balance.  
5. **These neural defects lead to** developmental delay, intellectual disability, severe speech impairment, autism/behavioral abnormalities, hypotonia or spasticity and epilepsy.  
6. **In a dental branch, altered SATB1-dependent transcription is inferred to lead to** abnormal ameloblast differentiation, apicobasal polarity, tight-junction/actin organization and directional enamel-matrix secretion.  
7. **Impaired amelogenin transport and enamel-matrix secretion lead to** thin, hypomineralized or disorganized enamel, tooth fragility, discoloration and abnormal spacing/position.  
8. **Recurrent seizures and feeding/mobility impairment can secondarily lead to** developmental interruption, nutritional compromise, contractures and reduced daily functioning.

### 6.2 Human-cell functional evidence

In HEK293T/17 cells, wild-type SATB1 showed a granular nuclear distribution inverse to Hoechst-dense DNA. p.Glu407Gly, p.Gln420Arg, p.Glu530Lys/Gln and p.Glu547Lys instead formed a cage-like nuclear pattern strongly colocalizing with DNA. All five variants increased repression of an **IL2-promoter** reporter; CUT1 variants and one CUT2 variant also increased repression of an IgH matrix-attachment-region reporter. FRAP showed reduced nuclear mobility or prolonged recovery, supporting stabilized chromatin binding. The variants retained the ability to interact with wild-type SATB1 in BRET assays. [91][197]

The decisive human-paper quotation is:

> “Clinical evaluation of 42 individuals carrying *SATB1* variants identified overt genotype-phenotype relationships… Missense variants in the CUT1 and CUT2 DNA-binding domains result in stronger chromatin binding, increased transcriptional repression, and a severe phenotype.”  
> — den Hoed et al., published January 28, 2021; PMID 33513338; DOI 10.1016/j.ajhg.2021.01.007; [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7895900/). [264]

### 6.3 Neural mechanisms

SATB1 is expressed in postnatal cortical and amygdalar neurons, including excitatory and inhibitory neuronal subsets. Mouse work showed binding at immediate-early genes and altered expression timing and dendritic-spine density after *Satb1* loss. [145]

The 2025 truncating-rat model—not a direct model of CUT-domain KTZSL—showed:

- smaller brains and reduced cortical-layer thickness;
- reduced somatostatin-positive cortical interneurons;
- reduced dendritic complexity and spine density;
- impaired communication, motor development, memory and sociability;
- increased cortical gamma power;
- 545 cortical differentially expressed genes, including enrichment for interneuron migration, CNS neuron differentiation, precursor proliferation and positive MAPK-cascade regulation. [151]

These data support neuronal-development and excitation–inhibition mechanisms but should not be treated as proof that severe human missense variants act identically.

### 6.4 Dental mechanism

In *Satb1* knockout mice, ameloblasts were shortened and lost Tomes’ processes, apical F-actin organization and normal claudin-1 localization. Amelogenin accumulated intracellularly rather than being directionally secreted, producing thin, hypomineralized, non-prismatic enamel. The paper concluded:

> “SATB1 is essential for establishing secretory ameloblast cell polarity and for EMP secretion.”  
> — Zhang et al., December 13, 2019; PMID 31830989; DOI 10.1186/s12915-019-0722-9; [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6909472/). [167]

Relevant molecular components include **EPS8**, F-actin, CLDN1, RAB30, amelogenin/AMELX and c-MAF. *Amelx* transcript abundance was unchanged, favoring defective trafficking/secretion over overproduction. [166]

### 6.5 Pathways and ontology suggestions

| Mechanism | Suggested ontology annotations |
|---|---|
| Chromatin organization | GO:0006325 — chromatin organization |
| DNA-templated transcription regulation | GO:0006355 |
| Negative regulation of transcription | GO:0045892 |
| DNA binding | GO:0003677 |
| Cell polarity establishment | GO:0030010 / GO:0007163 |
| Protein secretion | GO:0009306 |
| Nervous-system development | GO:0007399 |
| Neuron differentiation | GO:0030182 |
| Interneuron migration | GO:0097475 |
| Dendrite development | GO:0016358 |
| Actin-filament organization | GO:0007015 |
| Nucleus | GO:0005634 |
| Nucleoplasm | GO:0005654 |
| Chromatin | GO:0000785 |
| Neuron | CL:0000540 |
| GABAergic neuron | CL:0000617 |
| Glutamatergic neuron | CL:0000679 |
| Somatostatin-positive interneuron | CL term should be selected from the current interneuron hierarchy |
| Ameloblast | CL:0000060 |

### 6.6 Omics and advanced technologies

- **Human dental transcriptomics:** fetal ameloblast-lineage microarray, GEO **GSE75954**, identified SATB1 upregulation and stage-specific transcriptional programs.
- **Rat bulk RNA-seq:** 545 cortical DEGs in the 2025 truncation model.
- **Single-cell/spatial transcriptomics:** no disease-specific patient study identified.
- **Proteomics/metabolomics/lipidomics:** no diagnostic KTZSL profile.
- **CRISPR screens:** none specific to the disorder.
- **Patient-derived iPSC/organoid model:** none clearly established for KTZSL.

---

## 7. Anatomical structures affected

| Level | Primary structures | Suggested ontology |
|---|---|---|
| Organ/system | Brain/CNS | UBERON:0000955 — brain |
| Region | Cerebral cortex, with nonspecific possible cerebellar/white-matter involvement | UBERON:0000956 — cerebral cortex |
| Functional neural tissue | Cortical neuronal networks, interneurons and pyramidal neurons | CL:0000540; CL:0000617; CL:0000679 |
| Oral organ | Primary and permanent teeth | UBERON:0001091 — tooth |
| Dental tissue | Enamel and enamel-forming epithelium | UBERON:0001752 — enamel |
| Dental cell | Presecretory and secretory ameloblasts | CL:0000060 |
| Secondary systems | GI/feeding apparatus, musculoskeletal system, eye and occasionally heart/urogenital system | Patient dependent |
| Subcellular | Nucleus, nucleoplasm, chromatin-associated nuclear bodies | GO:0005634; GO:0005654 |
| Ameloblast compartments | Apical actin belt, Tomes’ process, secretory vesicles and tight junctions | Use current GO epithelial-polarity, actin and vesicle terms |

Neurologic involvement is generally bilateral/systemic rather than consistently lateralized. No reproducible unilateral lesion is characteristic.

---

## 8. Temporal development

- **Onset:** developmental abnormalities generally emerge in infancy or early childhood. Hypotonia and delayed milestones may precede epilepsy.
- **Epilepsy:** frequently begins in infancy or early childhood; severe cases can have pharmacoresistant epileptic encephalopathy, hypsarrhythmia, multifocal discharges or status epilepticus.
- **Dentition:** dental signs become evident with eruption of primary or permanent teeth.
- **Course:** chronic and lifelong. Some individuals show developmental regression, particularly in the setting of severe epilepsy; others acquire skills slowly.
- **Progression:** there is no validated staging system. The genetic developmental lesion is static, but its manifestations change with maturation, seizures, growth, dentition and secondary complications.
- **Remission:** no spontaneous disease remission is known. Seizures may remit or improve with therapy; developmental disability generally persists.
- **Critical intervention windows:** early seizure control, feeding management, vision/hearing correction, dental protection and early developmental therapy are clinically important, although no controlled KTZSL timing study exists.

---

## 9. Inheritance and population epidemiology

| Characteristic | Best current assessment |
|---|---|
| Inheritance | Autosomal dominant |
| Typical origin | De novo |
| Penetrance | Not quantified; apparently high for established severe CUT-domain variants, but unaffected transmitting parents in the broader SATB1 cohort indicate possible reduced penetrance or mosaicism |
| Expressivity | Markedly variable |
| Anticipation | Not reported; no repeat-expansion mechanism |
| Germline mosaicism | Possible; several suspected parental-mosaic families |
| Founder effect | None established |
| Consanguinity | Not relevant to the usual dominant mechanism |
| Sex ratio | No reliable estimate |
| Ethnic/geographic distribution | Cases from multiple ancestries and countries; no enrichment established |
| Prevalence | Orphanet category **<1 per 1,000,000**. [121] |
| Incidence | Not measured |
| Number initially assigned to DHDBV | 28 patients with heterozygous missense variants, including nine patients from three families. [214] |

The <1 per million figure is an Orphanet rarity category, not a measured epidemiologic prevalence. Underdiagnosis is likely because broad exome/genome testing only recently incorporated *SATB1*.

---

## 10. Diagnostics

### 10.1 Clinical suspicion

Consider KTZSL in a child with:

1. global developmental delay or moderate-to-profound ID;
2. severe speech delay or absent speech;
3. early-onset epilepsy, especially difficult-to-control epilepsy;
4. hypotonia with or without later spasticity;
5. enamel discoloration/hypoplasia, widely spaced, fragile, missing or malpositioned teeth;
6. variable facial dysmorphism, feeding problems, behavioral abnormalities or growth disturbance.

There are no consensus clinical criteria; molecular confirmation is required.

### 10.2 Recommended evaluation

| Domain | Test/evaluation | Expected role |
|---|---|---|
| Genetics | Trio WES or WGS with SNV/indel and CNV analysis | Preferred broad diagnostic approach; establishes de novo status and detects competing diagnoses |
| Targeted genetics | Neurodevelopmental/epileptic-encephalopathy panel including *SATB1*, *ROGDI* and *SLC13A5* | Appropriate when phenotype is strongly suggestive |
| Confirmation | Sanger or orthogonal NGS confirmation; parental testing | Confirms variant and inheritance |
| Mosaicism | High-depth parental testing, ideally with more than one tissue when recurrence counseling matters | Detects low-level parental mosaicism |
| CMA | Useful if WES/WGS lacks reliable CNV detection or congenital anomalies are present | Detects partial gene/3p CNVs and other diagnoses |
| Karyotype/FISH | Not first line | Reserve for suspected large rearrangement |
| mtDNA/repeat expansion | Not routinely indicated | Use only if independent clinical evidence |
| EEG | Baseline and repeated/sleep EEG | Seizure classification and occult epileptiform activity |
| Brain MRI | Baseline when seizures, regression, microcephaly or focal findings are present | Findings are variable and nonspecific |
| Dental | Pediatric dental examination, photographs and radiographs | Documents enamel, eruption, spacing, hypodontia and decay |
| Feeding | Swallow assessment and nutrition/growth evaluation | Detects dysphagia and aspiration risk |
| Other | Ophthalmology, hearing, cardiac examination/echo if indicated, orthopedic assessment | Phenotype-directed surveillance |

SATB1 is currently a green/high-evidence gene on expert intellectual-disability and early-onset/syndromic-epilepsy panels. [246][253]

### 10.3 Variant interpretation

A CUT1/CUT2 missense variant is most compelling when it is:

- absent or nearly absent from gnomAD;
- de novo or segregates with disease;
- at a recurrent, conserved DNA-interacting residue;
- classified pathogenic/likely pathogenic in ClinVar with phenotype match;
- supported by established functional data;
- consistent with the severe KTZSL phenotype.

A truncating variant should not automatically be labeled KTZSL: many cause the milder DEFDA phenotype, and final-exon variants may escape nonsense-mediated decay.

### 10.4 Differential diagnosis

| Disorder | Gene/inheritance | Distinguishing points |
|---|---|---|
| Classic Kohlschütter–Tönz syndrome | *ROGDI*, autosomal recessive | Severe early epilepsy, ID and characteristic yellow/brown amelogenesis imperfecta; biallelic inheritance. [235] |
| SLC13A5 developmental and epileptic encephalopathy 25 | *SLC13A5*, autosomal recessive | Seizures typically begin neonatally or in the first weeks; movement disorder and severe hypodontia/enamel hypoplasia are common. [228][231] |
| SATB1-related DEFDA | *SATB1*, autosomal dominant | Usually loss-of-function/truncating/deletion variants; milder ID and less severe epilepsy than CUT-domain KTZSL |
| SATB2-associated syndrome | *SATB2*, autosomal dominant | Severe speech disorder, palatal and dental anomalies; characteristic craniofacial phenotype, usually without the same epilepsy pattern |
| Other developmental epileptic encephalopathies | Numerous genes | Usually lack the specific combination of SATB1-domain variant and enamel/tooth phenotype |
| Nonsyndromic amelogenesis imperfecta plus unrelated epilepsy | Multiple | Requires segregation and molecular analysis to determine whether one or two disorders are present |

### 10.5 Screening

No population or newborn screening program exists. Appropriate strategies are:

- cascade testing after a familial pathogenic variant;
- targeted testing for parents and at-risk relatives;
- prenatal diagnosis or preimplantation genetic testing for a known familial variant;
- early EEG/dental surveillance after presymptomatic molecular diagnosis.

---

## 11. Outcome and prognosis

- **Survival/life expectancy:** no 5-year or 10-year survival estimates and no evidence-based life-expectancy figure are available.
- **Mortality:** disease-specific mortality is unquantified. Potential risks include prolonged seizures/status epilepticus, aspiration and severe immobility, but no cohort-level rates exist.
- **Long-term disability:** commonly substantial because of intellectual, language, motor and epilepsy burden.
- **Recovery:** the causal developmental disorder is not reversible with current treatment. Skills and participation may improve with seizure control, communication support and rehabilitation.
- **Complications:** refractory epilepsy, regression, aspiration/feeding problems, poor growth or obesity, contractures, falls, dental decay/fracture and caregiver burden.
- **Prognostic factors:** variant class is the strongest known predictor. CUT1/CUT2 missense variants predict more severe ID, epilepsy, hypotonia and spasticity than haploinsufficient/truncating variants. [91]
- **Biomarkers:** no validated molecular, EEG or imaging prognostic biomarker.

The prognosis literature is strongly limited by small samples, variable ages and short follow-up.

---

## 12. Treatment and current applications

### 12.1 Treatment principles

There is no curative or disease-specific approved treatment. Management is multidisciplinary and phenotype directed.

| Intervention | Application/evidence | Suggested NCIt concept |
|---|---|---|
| Antiseizure medication | Select by seizure type and EEG; severe cases may require combination therapy | Anticonvulsant Therapy |
| Valproic acid | Single-case evidence in SATB1 disease; monotherapy was initially inadequate in one child | Valproic Acid; anticonvulsant therapy |
| Oxcarbazepine | Added to valproate in one child, after which seizures became controlled | Oxcarbazepine; combination therapy |
| Levetiracetam | Short course used for sleep-activated EEG abnormalities in a 2024 truncating-variant case; evidence insufficient for a preferred regimen | Levetiracetam |
| Rescue/status treatment | Standard epilepsy protocols, individualized by neurology | Status Epilepticus Treatment |
| Physical therapy | Hypotonia, delayed motor skills, balance and contracture prevention | Physical Therapy |
| Occupational therapy | Adaptive function, fine motor and self-care | Occupational Therapy |
| Speech-language therapy and AAC | Severe speech disorder/nonverbal communication | Speech Therapy; Augmentative Communication |
| Feeding therapy/nutrition | Dysphagia, poor growth, aspiration risk; gastrostomy if clinically necessary | Nutritional Support; Enteral Feeding |
| Dental prevention/restoration | Fluoride, desensitization, frequent surveillance, sealants, crowns/restoration as indicated | Dental Restoration; Preventive Dentistry |
| Behavioral/sleep management | Autism features, anxiety, challenging behavior and sleep disturbance | Behavioral Therapy |
| Vision/hearing correction | Treat detected deficits | Supportive Care |
| Orthopedic/spasticity care | Stretching, orthoses, antispasticity agents or surgery according to standard indications | Rehabilitation Therapy; Orthopedic Procedure |

In the reported seven-year-old girl, valproate 25 mg/kg twice daily did not adequately suppress seizures. Later low-dose valproate plus oxcarbazepine was associated with seizure freedom and markedly improved EEG, but this is uncontrolled single-patient evidence and the patient had a truncating variant rather than prototypical CUT-domain KTZSL. [99]

Relevant chemicals include valproic acid (**CHEBI:39867**) and oxcarbazepine; genotype-specific pharmacogenomic guidance is unavailable.

### 12.2 Advanced and experimental therapy

- No approved gene-replacement, gene-editing, ASO, siRNA, mRNA, cell or targeted chromatin therapy.
- No KTZSL-specific registered interventional study was identified; a 2026 search summary reported zero studies registered under the Orphanet disease name. [259]
- In a 2025 truncating-rat model, clonazepam 0.04 mg/kg improved Y-maze alternation, social recognition and sociability, but did not improve Morris-water-maze performance; gamma-power reduction did not reach conventional statistical significance. This is **preclinical evidence only** and does not justify disease-specific clonazepam treatment in humans. [151]

---

## 13. Prevention

### Primary prevention

The occurrence of a de novo pathogenic allele cannot currently be prevented by lifestyle, vaccination or exposure modification.

### Secondary prevention/early detection

- genetic diagnosis after developmental delay, epilepsy and/or enamel abnormalities;
- cascade and parental mosaicism testing;
- early EEG monitoring;
- early dental examination and enamel protection;
- feeding and aspiration assessment;
- vision/hearing screening;
- early developmental and communication intervention.

### Tertiary prevention

- maintain seizure control and rescue plans;
- prevent aspiration and malnutrition;
- prevent contractures and falls;
- prevent tooth wear, decay and pain;
- use AAC to reduce communication-related frustration;
- monitor caregiver burden and provide social/educational support.

### Reproductive prevention and counseling

Offer nondirective genetic counseling, prenatal diagnosis and preimplantation genetic testing when the familial variant is known. For a constitutively heterozygous affected parent, transmission risk is 50% per pregnancy. After an apparently de novo event, recurrence is low but not zero because parental germline mosaicism is documented in this disease spectrum.

No vaccine, prophylactic medication or public-health environmental measure is applicable.

---

## 14. Other species and natural disease

| Species/model | Taxonomy/gene | Findings | Interpretation |
|---|---|---|---|
| Human | *Homo sapiens*, NCBI Taxon 9606; *SATB1* Gene 6304 | Natural genetic disease | Definitive disease species |
| Mouse | *Mus musculus*, Taxon 10090; *Satb1* Gene 20230 | Knockout causes thin hypomineralized non-prismatic enamel, abnormal ameloblast polarity and early death | Strong mechanistic dental model, but not a precise heterozygous CUT-missense model |
| Rat | *Rattus norvegicus*, Taxon 10116; *Satb1* Gene 316164 | Engineered N-terminal truncation causes developmental, cognitive, social and cortical-neuron abnormalities | Neurologic model of SATB1 loss/altered localization, not exact KTZSL mechanism. [272] |
| Zebrafish | *Danio rerio*, Taxon 7955; *satb1a* Gene 378993 | Knockout reported to reduce body size | Limited disease recapitulation; no established full KTZSL model. [271] |

No verified naturally occurring homologous SATB1 syndrome in companion animals, livestock or wildlife was identified in OMIA. Consequently, there is no veterinary prevalence, breed association, VBO term or cross-species transmission concern.

---

## 15. Model organisms and research resources

### 15.1 Existing models

1. **Constitutive *Satb1*-null mouse**
   - Type: mammalian knockout.
   - Recapitulates: enamel hypoplasia/hypomineralization, abnormal ameloblast shape, loss of Tomes’ processes and defective amelogenin secretion.
   - Limitations: biallelic complete loss and early death differ from heterozygous missense KTZSL.

2. **Engineered truncating rat**
   - Type: TALEN-induced exon-1 frameshift with translational reinitiation and N-terminally truncated protein.
   - Recapitulates: growth retardation, microcephaly, delayed neurobehavioral development, impaired vocalization, hypotonia, learning/memory and social deficits.
   - Cellular findings: reduced somatostatin interneurons and dendritic/spine abnormalities.
   - Limitations: truncating-loss mechanism differs from the chromatin-hyperbinding CUT-domain missense mechanism; bulk RNA-seq cannot resolve cell-specific changes. Published June 26, 2025, PMID 40571781, DOI 10.1038/s41401-025-01588-6. [157]

3. **HEK293T/17 expression assays**
   - Type: in vitro heterologous cell system.
   - Applications: localization, reporter repression, FRAP chromatin mobility and BRET oligomerization.
   - Limitations: not neuronal or ameloblast physiology and relies on overexpression.

4. **Human ameloblast-lineage cultures**
   - Type: primary/developmental dental-cell system.
   - Applications: stage-specific expression, SATB1 induction and CLDN1/EPS8 regulation.
   - Limitations: not patient-derived and not a pathogenic-variant model.

### 15.2 Priority future models

- heterozygous knock-in mouse/rat models of recurrent p.Glu407Gly, p.Gln420Arg and p.Glu530Lys variants;
- patient-derived iPSC cortical neurons and interneurons;
- cerebral and tooth organoids;
- single-cell and spatial transcriptomic profiling;
- CUT-domain variant ChIP-seq/CUT&RUN to identify direct disease-relevant targets;
- longitudinal EEG and behavioral studies;
- rescue experiments that normalize, rather than eliminate, SATB1 chromatin residence.

### 15.3 Databases/resources

- MGI: *Satb1*, MGI:105084 [13]
- NCBI Gene: human 6304, mouse 20230, rat 316164
- ClinVar: condition C5543202/OMIM 619229 searches
- ClinGen: 2024 definitive broad SATB1–complex NDD curation
- GEO: GSE75954, ameloblast developmental transcriptomics
- PanelApp: SATB1 green for intellectual disability and early-onset/syndromic epilepsy

---

## Recent developments and expert assessment

### 2023–2024

- **2023:** broader amelogenesis-imperfecta sequencing literature reinforced the importance of distinguishing *SATB1* disease from *ROGDI* and *SLC13A5* disorders based on inheritance, seizure onset and dental phenotype. [227]
- **April 25, 2024:** Privitera et al. reported a de novo p.Gln606Hisfs*101 variant and reviewed eight C-terminal LoF/PTV cases. Their analysis found developmental/motor delay in 8/8, speech delay in 7/8 and dental abnormalities in 5/8, while emphasizing that LoF cases are generally milder than CUT-domain missense disease. PMID 38790177; DOI 10.3390/genes15050548; [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11120869/). [62][67]
- **September 17, 2024:** the ClinGen Intellectual Disability and Autism Expert Panel classified the broader *SATB1*–autosomal-dominant complex neurodevelopmental-disorder relationship as **definitive**, with the maximum genetic-evidence score reached. [181]

### 2025–2026 context

The 2025 rat model supplies the first broad in-vivo neurologic framework and implicates somatostatin interneurons, cortical gamma activity and neuronal differentiation pathways, but it models truncation rather than the KTZSL-defining CUT-domain missense mechanism. The central expert interpretation therefore remains mutation-specific: **variant class and domain must be considered before predicting disease severity or mechanism.**

---

## Knowledge-base conclusions

1. **Preferred entity:** den Hoed–de Boer–Voisin syndrome/Kohlschutter–Tonz syndrome-like, MONDO:0030990, OMIM 619229, ORPHA:684232.
2. **Causal gene:** *SATB1*.
3. **Inheritance:** autosomal dominant, mostly de novo, with parental mosaicism and variable penetrance/expressivity.
4. **Defining mechanism:** CUT1/CUT2 missense variants stabilize chromatin binding and increase transcriptional repression.
5. **Core phenotype:** developmental delay, moderate-to-profound ID, severe speech impairment, hypotonia, early epilepsy, behavioral abnormalities and dental/enamel defects.
6. **Key distinction:** *SATB1* truncating/haploinsufficient disease is usually the milder DEFDA spectrum; classic *ROGDI*-KTZS and *SLC13A5*-DEE are autosomal recessive differentials.
7. **Diagnosis:** trio WES/WGS or a comprehensive NDD/epilepsy panel with inheritance testing and careful domain-specific variant interpretation.
8. **Treatment:** supportive and symptomatic; antiseizure therapy, rehabilitation, AAC, feeding management and proactive dental care.
9. **Evidence gaps:** true prevalence, penetrance, natural history, survival, validated outcome scales, patient-derived models and disease-modifying therapy remain unknown.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 65 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 21 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000060` (2 mentions) - the report calls it "Ameloblast", "Presecretory and secretory ameloblasts"; CL calls it **odontoblast**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006355` (1 mention) - the report calls it "DNA-templated transcription regulation"; GO calls it **regulation of DNA-templated transcription**
- `GO:0045892` (1 mention) - the report calls it "Negative regulation of transcription"; GO calls it **negative regulation of DNA-templated transcription**
- `GO:0097475` (1 mention) - the report calls it "Interneuron migration"; GO calls it **motor neuron migration**
- `UBERON:0001091` (1 mention) - the report calls it "tooth"; UBERON calls it **calcareous tooth**, and lists "tooth" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000060` - called "Ameloblast", "Presecretory and secretory ameloblasts"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.