---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:25.484407'
end_time: '2026-10-09T20:58:59.252115'
duration_seconds: 213.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypomyelination with Brain Stem and Spinal Cord Involvement and Leg
    Spasticity
  mondo_id: MONDO:0014115
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 51
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 29
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014115
    reported_labels:
    - MONDO
    ontology_label: hypomyelination with brain stem and spinal cord involvement and
      leg spasticity
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - OMIM
  - UniProtKB
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomyelination with Brain Stem and Spinal Cord Involvement and Leg Spasticity
- **MONDO ID:** MONDO:0014115 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypomyelination with Brain Stem and Spinal Cord Involvement and Leg Spasticity** covering all of the
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

# Hypomyelination with Brainstem and Spinal Cord Involvement and Leg Spasticity (HBSL)

**HBSL is a rare, autosomal-recessive *DARS1*-related leukodystrophy.** Its characteristic combination is lower-limb-predominant spasticity and a recognizable pattern of brain and spinal-cord white-matter abnormalities. Infantile disease often impairs motor development severely, but adolescent and late-adult presentations show that neither onset age nor MRI appearance is uniform. There is **no established disease-modifying treatment**. The strongest evidence consists of a small number of human case series, functional studies and mouse models—not population-based natural-history data or treatment trials. [18][77][61][17]

**Evidence convention.** *Human clinical* denotes observations in affected people; *human tissue/in vitro* denotes expression or enzyme experiments; *mouse* denotes induced models. Frequencies below are **reported-case fractions**, not reliable population frequencies. Ontology terms are suggested knowledge-base annotations, not independently validated diagnostic criteria. Source URLs appear in the linked citations; PMIDs and publication dates are given where available.

## 1. Disease information

| Identifier or name | Value | Interpretation |
|---|---|---|
| Preferred name and acronym | Hypomyelination with brainstem and spinal cord involvement and leg spasticity; **HBSL** | Named for its clinical and imaging pattern. [18] |
| MONDO | **MONDO:0014115** | Disease identifier. [1] |
| OMIM phenotype | **615281** | Distinct from the *DARS1* **gene** entry, OMIM **603084**. [16] |
| Orphanet | **ORPHA:363412** | Classified as a rare genetic leukodystrophy. [20] |
| MedGen; SNOMED CT | **C4755254; 777999008** | Disease-level cross-references. [42][16] |
| ICD-10 | **E75.2**, as mapped by Orphanet | A broad classification code, **not** an HBSL-specific molecular diagnosis. An HBSL-specific ICD-11 or MeSH disease identifier was not established from the reviewed sources. [20] |
| Alternative names | Aspartyl-tRNA synthetase deficiency; *DARS*-associated leukoencephalopathy | Historical literature uses *DARS* for the gene now designated *DARS1*. [2][77] |

This report **aggregates published individual-patient observations and disease-level resources**. It does not use an identifiable patient's EHR or claim that the published cases constitute a representative registry. Orphanet describes diffuse supratentorial, brainstem and spinal involvement, with nystagmus, hypotonia, motor delay and leg spasticity among the usual clinical features. [20]

## 2. Etiology, risk, protection and gene–environment interaction

**Established cause:** pathogenic biallelic germline *DARS1* variants—either homozygous or on opposite parental alleles—alter cytosolic aspartyl-tRNA synthetase (AspRS). The original 2013 sequencing study identified such variants in **10 individuals from seven unrelated families**. Its abstract states: “These mutations cause nonsynonymous changes to seven highly conserved amino acids,” situated adjacent to or within the enzyme's active-site pocket. PMID **23643384**, published **May 2, 2013**. [18][16]

| Factor category | Disease-specific assessment |
|---|---|
| Genetic risk | A child inheriting two disease-causing *DARS1* alleles is at risk. Family history and shared ancestry can help identify carriers; documented cases include homozygosity and compound heterozygosity. A rare allele **alone**, particularly one classified as a VUS, does not establish HBSL. [18][77][195] |
| Environmental causation | **None established.** No toxin, occupation, diet, lifestyle factor or infectious agent is an established cause of this Mendelian disease. [16][17] |
| Possible triggers of deterioration | Viral illness and trauma preceded deterioration in individual reports; **five of 19** cases compiled in a 2023 review reportedly deteriorated with infection. These observations do not prove causation or define a quantified gene–environment interaction. PMID **25527264**; review PMID **36712860**. [77][17] |
| Protective genetic or environmental factors | **None validated** for preventing HBSL. Clinically unaffected single-allele carriers and mildly affected mouse genotypes support a dosage effect, but do not identify a proven protective modifier. [77][153] |
| Modifier genes, susceptibility loci, epigenetic modifiers | No reproducibly established HBSL-specific examples in the reviewed evidence. [17][39] |

## 3. Phenotypes and functional impact

The **2023 literature review counted 19 reported patients**, with **11 males and eight females**; onset ranged from **4 months to 18 years** in that compilation. Its denominators are small, some features were incompletely reported, and a subsequently described late-adult case is **not** captured by that onset range. Use the counts as observations within the review, not penetrance estimates. PMID **36712860**, online **January 12, 2023**. [17][61]

| Phenotype | Type; onset, course and severity | Reported frequency and daily-function impact | Suggested HPO term |
|---|---|---|---|
| Lower-limb-predominant spasticity or spastic paraparesis | Clinical sign; usually infancy, often progressive; severity variable | Defining manifestation; walking and transfers may require assistance. No defensible pooled percentage for spasticity itself. [16][17] | Spasticity **HP:0001257**; spastic paraplegia **HP:0001258**. [106] |
| Motor developmental delay, stagnation or regression | Symptom/sign; typically early childhood; variable progression | **16/19** with motor retardation in the review; substantial effects on sitting, standing and ambulation. [17] | Motor delay **HP:0001270**; delayed gross motor development **HP:0002194**. [107][112] |
| Lower-limb hyperreflexia | Examination sign; accompanies upper-motor-neuron disease | **18/19**; helps localize tract dysfunction, rather than measuring quality of life by itself. [17] | Lower limb hyperreflexia **HP:0002395**. [112] |
| Extensor plantar responses | Examination sign; variable | **13/19**; supports corticospinal involvement. [17] | Use the HPO **extensor plantar response/Babinski sign** term after terminology-system verification; no code assigned here. |
| Nystagmus | Ocular sign; can begin in infancy | The review reported **7/19** with a movement abnormality *accompanied by nystagmus*; this is **not necessarily the total nystagmus count**. Can interfere with visual tasks. [17] | Nystagmus **HP:0000639**. [107] |
| Ataxia | Clinical sign; variable onset and severity | **5/19** on examination; worsens balance and gait. [17] | Ataxia **HP:0001251**. [135] |
| Cognitive dysfunction | Symptom/sign; variable | **6/19** in the review; may affect learning and independence. The original series described mild impairment in some, not all, patients. [17][16] | Mild intellectual disability **HP:0001256** *only when clinically established*. [225] |
| Myopia; other retinal or optic findings | Ocular signs; variable | Myopia **6/19**; retinal abnormalities **3/19**. These are less consistent than motor findings. [17] | Record the specific examined ocular finding, rather than assigning all patients an optic phenotype. |
| Dysarthria | Clinical sign; variable, potentially progressive | **3/19**; can limit communication. A later adult-onset patient became anarthric. [17][61] | Dysarthria **HP:0001260**. [225] |
| Axial hypotonia | Clinical sign; often early | Characteristic in the original series; impaired trunk control can compound mobility problems. No dependable pooled count. [16] | Axial hypotonia **HP:0008936**. [239] |
| CNS hypomyelination/white-matter signal change | MRI finding, not a symptom; distribution varies with presentation | Central diagnostic clue; infantile cases can have diffuse abnormalities, whereas adolescent cases can have focal cerebral changes despite extensive tract abnormalities in the cord. [18][77] | CNS hypomyelination **HP:0003429**, **only where imaging supports hypomyelination**. [226] |
| Seizures or epilepsy | Clinical symptom; uncommon/variable | **Two patients with epileptic events** were identified by the review; effects depend on the individual event and its control. [17] | Seizure: select the specific HPO seizure term supported by the record. |

**Quality-of-life evidence is indirect:** walking, communication and cognitive effects are documented, but no HBSL-specific EQ-5D, SF-36 or PROMIS estimate was established in these sources. The original infantile series reported **no independent walkers**, while outcomes in later reports varied; those observations must not be merged into a single lifetime walking probability. [16][77][17]

## 4. Genetic and molecular information

*DARS1* is at **2q21.3**; gene identifiers are **HGNC:2678**, **NCBI Gene:1615**, **OMIM:603084** and **UniProtKB:P14868**. The disorder involves **germline**, predominantly **missense**, variation. Published associations include a small insertion; a patient-specific structural-variant, aneuploidy or somatic mechanism was not established in the reviewed literature. [57][47][17]

| Reported *DARS1* variant or genotype | Human and functional evidence; classification caution |
|---|---|
| **c.821C>T, p.Ala274Val** in trans with **c.1099G>T, p.Asp367Tyr** | Original Australian genotype. In an expression-based aminoacylation assay, Ala274Val abolished measured activity, whereas Asp367Tyr showed slightly **increased**, not decreased, activity in that assay. Asp367Tyr/one-null-allele mice subsequently modeled aspects of disease. Thus, **not every HBSL missense allele is demonstrated to be a simple enzymatic null**. PMIDs **23643384**, **33551752**. [18][24] |
| **c.766A>C, p.Met256Leu**, homozygous | Reported in affected original-series families; listed as pathogenic in a ClinVar literature submission. Homozygous knock-in mice were much less affected than human patients with this variant. PMIDs **23643384**, **35357600**. [181][78] |
| **c.1277T>C, p.Leu426Ser**, homozygous in reported patients | Present in adolescent and late-adult presentations. **Current ClinVar aggregate interpretation is conflicting: one likely-pathogenic and two VUS submissions**; Variation ID **488394**. The 2023 adult report gave gnomAD v2.1.1 global frequency **1/83,472**. These are source- and version-dependent estimates, not a carrier-frequency estimate for HBSL. PMID **25527264**; adult case **March 2023**, DOI **10.54029/2023vkd**. [77][61][195] |
| **c.599C>G, p.Ser200Cys** / **c.830C>T, p.Ser277Phe**; **c.839A>T, p.His280Leu** / **c.1099G>C, p.Asp367His** | Two compound-heterozygous genotypes in the 2015 human series; interpretation rests on case and segregation evidence, not an asserted uniform functional consequence for every allele. PMID **25527264**. [77] |
| **c.1363T>C, p.Tyr455His** / **c.821C>G, p.Ala274Gly** | Compound-heterozygous genotype reported in a Chinese family. The paper called the pair pathogenic/likely pathogenic under ACMG guidance **without clearly assigning one class to each individual variant**. PMID **35571067**, **April 26, 2022**. [65] |
| Other published substitutions | The 2023 review tabulates **p.Arg487Cys, p.Arg460His, p.Pro464Leu, p.Arg494Cys, p.Arg494Gly, p.Met404Val, p.Met478Val and p.Arg179Lys**, among others. Treat its table as a report of variants, **not** as proof that every listed allele has the same current ClinVar class or population frequency. PMID **36712860**. [17] |
| Reported insertion | **c.1498_1499insTCA**, reported as a protein-level Ile insertion in the review. Confirm transcript, HGVS normalization, phase and present-day classification before entering it as a clinically actionable pathogenic variant. [17] |

**Data-quality warning:** the review inconsistently labels a **c.1480C>T** substitution as both p.Arg494Gly and p.Arg494Cys in portions of its table/text. Do **not** propagate that pairing without checking the primary report and reference transcript; its listed **c.1480C>G** corresponds to a different substitution. [17]

No validated HBSL-specific severity-modifier gene, methylation signature, chromosomal syndrome or protective allele emerged from the reviewed primary evidence. [17][39]

## 5. Environmental information

There is **no established environmental, lifestyle or infectious etiology** for HBSL, and no HBSL-specific dietary, smoking, exercise or exposure-risk estimate. Infections or trauma may coincide with a **decline in an already affected individual**, as illustrated by the 2015 case series; they do not substitute for biallelic *DARS1* variation as the disease cause. Consequently, no pathogen taxonomy identifier or zoonotic transmission pathway applies. [77][16]

## 6. Mechanism and pathophysiology

**Ordered causal chain — demonstrated steps and marked inferences**

1. **Biallelic germline *DARS1* variants lead to altered cytosolic AspRS protein.** Active-site proximity and disease association are demonstrated in humans; effects vary by allele. [18][24]
2. **Altered AspRS can lead to impaired charging of tRNA\(^\mathrm{Asp}\) with aspartate.** This is directly demonstrated for **p.Ala274Val in a cell-based assay**, but must **not** be generalized to p.Asp367Tyr, which did not reduce measured activity in that assay. [24]
3. **Abnormal tRNA charging is inferred to lead to disturbed protein synthesis or translational fidelity in vulnerable neural cells.** The enzyme reaction is established; the precise in-vivo route from each HBSL allele to neural injury remains unresolved. [210][24][69]
4. **Branch A—neuronal pathway:** dysfunction in translation-rich neurons or their processes is **inferred** to impair axon function and neuronal–glial support; expression enrichment in neurons is demonstrated, but a universal primary human axon lesion is **not**. [76][153][17]
5. **Branch B—myelin pathway:** primary or secondary oligodendrocyte dysfunction is **inferred** to lead to deficient myelin formation/maintenance. Reduced myelin-protein markers and spinal white-matter damage are **demonstrated in hypomorphic mice**; they do not establish which human cell type is first affected. [24][78]
6. **White-matter abnormalities in brainstem, cerebral tracts and spinal long tracts lead to impaired motor-pathway function**, consistent with progressive leg spasticity, hyperreflexia and gait disability; ocular, coordination and cognitive manifestations vary with involvement. Human MRI–clinical concordance supports this step, without resolving all intermediate cellular events. [18][77][17]

AspRS catalyzes **tRNA(Asp) + L-aspartate + ATP → aspartyl-tRNA(Asp) + AMP + diphosphate**. Suggested annotations are **GO:0006422** (aspartyl-tRNA aminoacylation), **GO:0006412** (translation), **GO:0005829** (cytosol), **CHEBI:29991** (L-aspartate anion) and **CHEBI:30616** (ATP). The ribosome participates downstream; describing AspRS itself as a ribosomal protein would be incorrect. [118][218][211]

In human post-mortem tissue and stem-cell-derived neural cells, *DARS1* expression was enriched in **cerebellum and neurons**, with lower abundance in oligodendrocytes, astrocytes and microglia. The human-expression abstract says: “Although obligatorily expressed in all cells, DARS shows a distinct expression pattern with enrichment in neurons.” PMID **29615866**, **March 20, 2018**. Mouse work additionally detected AspRS along neurites and at synapses, potentially supporting local translation. Suggested cell terms: **CL:0000540 neuron**, **CL:0000128 oligodendrocyte**, **CL:0000127 astrocyte**; precursor **CL:0002453** is a research-relevant cell annotation, **not** a demonstrated uniquely affected population. [76][153][165][179]

**Downstream and unresolved pathways.** At 10 months, Asp367Tyr/null mice showed spinal white-matter vacuolization/demyelination and reduced major myelin markers, while Met256Leu/null mice showed later spinal vacuolization and reduced selected hindbrain markers. The latter model also showed altered fuel use—an approximately **0.8-to-0.9** active-phase respiratory-exchange-ratio shift—but **a human HBSL metabolic signature has not been established**. ER unfolded-protein stress and apoptosis are **proposed explanations**, not experimentally proven HBSL causal steps; similarly, inflammatory signaling has been suggested in discussing steroid responses but is not demonstrated as the initiating pathology. No disease-specific Wnt, MAPK, mTOR, PI3K–AKT, epigenomic, single-cell, spatial-transcriptomic, proteomic, lipidomic or metabolomic causal signature was established in the reviewed evidence. PMIDs **33551752**, **35357600**, **25527264**. [24][78][77]

## 7. Anatomical structures affected

| Level | Sites, pattern and suggested ontology terms |
|---|---|
| Organ and system | Primarily **central nervous system**: brain **UBERON:0000955**, brainstem **UBERON:0002298**, spinal cord **UBERON:0002240**. Motor impairment can secondarily affect musculoskeletal function; primary cardiac, liver or bone-marrow disease is **not established in people**, despite findings in one mouse model. [20][195][202][78] |
| White-matter localization | Supratentorial white matter, corpus callosum, internal capsule, pyramidal tracts, cerebellar peduncles, and spinal **dorsal columns and lateral corticospinal tracts**. MRI findings are generally tract-patterned and often bilateral; **individual adult patterns can evolve**, so uniform diffuse cerebral hypomyelination is not required. [18][77][61] |
| Tissue and cell | Myelinated CNS axon tracts; neurons **CL:0000540** and myelin-forming oligodendrocytes **CL:0000128** are mechanistically relevant. Cell-selective causation remains unsettled. [76][24][165] |
| Subcellular | **Cytosol GO:0005829** is the established site for *DARS1* AspRS activity; neuronal soma and processes contain the protein. ER involvement is a **hypothesis**, not an established localization of the initiating defect; mitochondrial AspRS is encoded by ***DARS2***, not *DARS1*. [153][210][78][77] |

## 8. Temporal development

**Typical course:** insidious or progressive motor disease beginning in infancy. The original 10 patients developed progressive motor dysfunction between **4 and 12 months**; the 2023 review's 19 cases had a **mean onset of 3.6 years**, but ranged from **4 months to 18 years**. Adolescents can instead have subacute or apparently relapsing deterioration. A **March 2023** report extended the described spectrum to a man whose unsteady gait began at **55**, followed by wheelchair dependence at **59** and anarthria at **60**. These reports demonstrate variability, not validated early/intermediate/end-stage boundaries. [16][17][77][61]

HBSL is generally **chronic**, with variable progression. Partial improvement after illness or steroid treatment has been reported, but durable remission or spontaneous cure is not established. Early onset was associated with poorer function in the small published series; no validated developmental treatment window or individual progression-rate model exists. [17][77]

## 9. Inheritance and population

| Population characteristic | Best-supported assessment |
|---|---|
| Inheritance; family risk | **Autosomal recessive.** If both parents carry pathogenic variants in *DARS1*, the conventional **per-pregnancy Mendelian probability** is **25% affected, 50% carrier, 25% neither allele**; confirm variant pathogenicity and parental phase before applying this to a family. [16][18] |
| Prevalence and incidence | Orphanet lists prevalence **<1 per 1,000,000**; a robust disease-specific incidence and precise point-prevalence estimate are **unavailable**. [20] |
| Reported-case demographics | The 2023 review counted **19** published patients (**11 male, eight female**) from several regions; this is **not** a measured sex ratio or worldwide case total as of 2026. [17] |
| Geographic/founder evidence | Homozygous p.Met256Leu was described in Indian/Pakistani families. One Malay adult case report measured p.Leu426Ser in its sampled control datasets, including **three heterozygotes among 170 Singapore Malay exomes**; neither observation alone proves a population founder effect or establishes a general carrier frequency. [181][61] |
| Penetrance, anticipation, mosaicism | **Not quantified or established** for HBSL. Variable onset and expressivity are documented; repeat-expansion anticipation is not an established mechanism. [77][61] |

## 10. Diagnostics

**Practical diagnostic sequence:** recognize progressive or otherwise unexplained spasticity/motor impairment; obtain **brain and spinal-cord MRI**; then establish **two appropriately classified *DARS1* variants in trans**, ideally with parental segregation. MRI pattern recognition plus molecular testing identified cases in the original and follow-up series. **WES and WGS** have both been useful; targeted *DARS1* sequencing is reasonable when imaging is strongly suggestive, while a leukodystrophy/spasticity panel should include ***DARS1* and *DARS2*** and broader alternatives. PMID **23643384**; PMID **25527264**. [18][77][17]

| Test or method | Disease-specific use and limitation |
|---|---|
| Brain and whole-spine MRI, including T1/T2/FLAIR | Look for characteristic cerebral/brainstem signal abnormalities and long-tract spinal involvement. In adolescent cases, **focal** brain findings and preserved cerebral myelination can coexist with cord changes. The 2023 late-adult case documented **new cervical tract involvement C2–C7** on follow-up imaging after an initially normal spine MRI. [77][61] |
| WES, WGS, gene panel or single-gene sequencing | Identify and classify both *DARS1* alleles, confirm phase and verify the reference transcript. WGS has a role in undiagnosed leukodystrophy broadly; **NCT02699190** is a WGS **diagnostic**, not HBSL drug-treatment, study. [18][77][61][68] |
| CSF, metabolic and inflammatory investigations | Useful when evaluating mimics, **not validated HBSL-specific biomarkers**. CSF oligoclonal bands were absent in the two adolescent patients tested in the 2015 series; absence is not by itself diagnostic. [77] |
| EMG/electrophysiology | Consider according to the neurologic differential. One long-surviving reported patient had EMG abnormalities, but there is **no defining HBSL electrophysiologic signature**. [65] |
| Biopsy, enzyme/metabolite profiling, RNA-seq | No standardized diagnostic biopsy, clinical AspRS assay, circulating biomarker or diagnostic omics signature was established. Laboratory aminoacylation assays are **research evidence**, not a replacement for clinical variant interpretation. [24][17] |
| CMA, karyotype, FISH, mitochondrial-DNA or repeat-expansion testing | **Not first-line confirmation of classic biallelic sequence-variant HBSL**; deploy if another diagnosis or variant class is suspected. *DARS2* is a **nuclear gene encoding a mitochondrial enzyme**, so testing it does not mean testing mitochondrial DNA. [16][77] |

**Differential diagnosis:** *DARS2*-related leukoencephalopathy with brainstem and spinal-cord involvement and lactate elevation (**LBSL**), inflammatory demyelination such as multiple sclerosis, and other genetic leukodystrophies or hereditary spastic paraplegias. In the 2015 study, the selective, extensive spinal-tract pattern was a useful clue even when subacute deterioration and steroid response suggested inflammation. Its abstract states: “Adolescents with mutations in *DARS* can present with a comparable clinical picture.” PMID **25527264**, **January 20, 2015**. [77]

There is **no established population newborn-screening program** for HBSL. Once familial variants are known, targeted testing of relatives and reproductive screening are more informative than nonspecific population screening. [16][17]

## 11. Outcome and prognosis

The most documented burden is **long-term mobility disability**, with variable additional ocular, coordination, speech and cognitive problems. Earlier-onset disease appeared more severe in the published series, yet the contrast between severely affected infants and later-onset patients precludes a single reliable prognostic trajectory. One death was noted among the 19 patients reviewed in 2023, **not** a disease-specific mortality rate. **Five-/ten-year survival, mean life expectancy, validated prognostic biomarkers and HBSL-specific quality-of-life scores are unavailable** from these small reports. [16][17][77][61]

Reported complications include deterioration with intercurrent illness and, in individual patients, severe loss of ambulation or hydrocephalus requiring a shunt; infrequent findings must not be treated as inevitable complications. Mouse hydrocephalus and early mortality must **not** be converted into human survival estimates. [17][24]

## 12. Treatment and current implementations

**Care is supportive and individualized; no intervention below is proven to correct *DARS1* dysfunction in patients.** The 2023 review concluded: “No consensus exists for HBSL treatment.” PMID **36712860**. Suggested NCIt concepts below are *term labels* for curation; no unverified NCIt identifiers are assigned. [17]

| Intervention; suggested NCIt concept | Human use, outcome and important limitation |
|---|---|
| Physical therapy, gait rehabilitation and mobility aids; **Physical Therapy / Rehabilitation** | Address strength, positioning, transfers and mobility. Reported rehabilitation did **not** completely reverse disease. [17] |
| Occupational and speech therapy; **Occupational Therapy / Speech Therapy** | Reasonable function-directed supportive approaches for impaired daily activities or speech; **HBSL-specific response rates are unavailable**. [17][65] |
| Symptom-directed spasticity, pain, bladder and seizure care; applicable **symptom-management/drug** concept | Tailor to the individual's problems. **No HBSL-specific pharmacogenomic rule or comparative drug trial** was identified. [17][77] |
| Methylprednisolone or other corticosteroids; **Corticosteroid Therapy / Methylprednisolone** | Uncontrolled reports describe partial improvement, particularly after subacute deterioration: the review counted improvement in **four of five steroid-exposed patients**. A 2015 adolescent received **1,000 mg IV daily for five days**; another received three-day pulses. The fraction is **not an efficacy estimate**—one infant had no additional benefit and improvement could be transient. PMID **25527264**. [17][77] |
| Immunoglobulin; **Intravenous Immunoglobulin Therapy** | Reported in an individual in combination with steroids; no isolated or established HBSL benefit. [17] |
| Thiamine, methylcobalamin and citicoline; applicable **agent** concepts | Given together for a year in one 2022 case report, followed by reported functional improvement. Without a comparator, the drugs' individual effects or disease modification **cannot be inferred**. PMID **35571067**. [65] |
| Ventriculoperitoneal shunt; **Ventriculoperitoneal Shunt Procedure** | Used to treat **one patient's hydrocephalus**, not underlying leukodystrophy. [17] |
| *DARS1* gene replacement; **Gene Therapy**, *experimental concept only* | Proposed from expression and mouse-model work; **not an established human HBSL treatment**. No HBSL-specific therapeutic gene-, cell-, RNA- or immunotherapy efficacy trial was identified in the reviewed sources. PMIDs **29615866**, **33551752**. [76][24] |

The relevant registered studies are **observational**, not therapeutic trials: **NCT02699190** evaluates WGS for leukodystrophy diagnosis, and **NCT03047369** is a myelin-disorders biorepository/natural-history registry that lists HBSL among eligible conditions. They should not be entered as HBSL treatment-response evidence. [68]

## 13. Prevention

**Primary prevention by vaccination, exposure control, diet or prophylactic medication is not established for this inherited disorder.** For a family with molecularly confirmed variants, genetic counseling, testing of at-risk relatives, and discussion of reproductive options—including prenatal or preimplantation testing where appropriate—can inform decisions; these measures are **not cures**. Early recognition and rehabilitation may help address functional needs, but evidence that screening or early intervention changes the underlying disease course is unavailable. Infection prevention and prompt assessment of new neurologic deterioration are reasonable supportive measures, **not proven HBSL-specific prophylaxis**. [16][17][77]

## 14. Other species and natural disease

HBSL is established as a **human** disease (*Homo sapiens*, NCBI Taxon **9606**). Its mouse ortholog is ***Dars1***, NCBI Gene **226414**, in *Mus musculus* (Taxon **10090**). The reviewed evidence supports **engineered mouse analogues**, not a documented naturally occurring *DARS1*-HBSL syndrome in a named animal breed; consequently no disease-specific breed/VBO term is assigned. Other species' hypomyelination must not be conflated with HBSL: for example, OMIA records **FNIP2**-related canine CNS hypomyelination, a **different genetic condition**. No zoonotic or cross-species infectious transmission applies. [47][48][126][18]

## 15. Model organisms and experimental applications

| Model or system | Recapitulation, use and limitation |
|---|---|
| Human post-mortem brain and stem-cell-derived neurons/glia; **human tissue/in vitro** | Defined cell-type and regional *DARS1* expression, supporting studies of neural vulnerability and cell-targeted approaches; expression **does not itself prove** the initiating diseased cell type. PMID **29615866**. [76] |
| Expressed human AspRS variants in HEK293 lysates; **in vitro** | Assayed tRNA aminoacylation: p.Ala274Val abolished measured activity, while p.Asp367Tyr did not. Useful for allele-specific hypotheses, but one assay cannot fully predict a patient's CNS phenotype. PMID **33551752**. [24] |
| *Dars1* complete knockout and heterozygous knockout; **engineered mouse** | Complete-null mice died **before embryonic day 11**. Heterozygotes lacked major gross motor abnormalities but showed reduced acoustic-startle prepulse inhibition. Useful for essentiality/dosage studies; **not a full HBSL phenotype**. PMID **27816769**, published **January 2017**. [153] |
| *Dars1* p.Asp367Tyr knock-in, homozygous versus variant/null; **engineered mouse** | Homozygotes were unexpectedly largely normal. Among **286 live-born offspring** from the cross, **25 (9%)** were variant/null; those mice showed developmental deficits, frequent early hydrocephalus and later spinal white-matter pathology and motor impairment. Small histology samples and absent full human-like brain disease limit extrapolation. PMID **33551752**, **January 20, 2021**. [24] |
| *Dars1* p.Met256Leu knock-in, homozygous versus variant/null; **engineered mouse** | Homozygotes were only mildly affected despite severe reported human homozygous disease. Variant/null mice showed developmental delay, hydrocephalus, later spinal vacuolization and metabolic/peripheral changes, but **not the full human cerebral MRI or motor phenotype**. Useful for dosage and tissue-vulnerability research. PMID **35357600**, **March 31, 2022**. [78] |

**Knowledge-base bottom line:** encode **biallelic *DARS1* variation → allele-dependent AspRS dysfunction → unresolved neuronal/oligodendroglial white-matter mechanism → tract-predominant CNS abnormalities → variable spastic motor disease**. Keep **human observations, cell assays and mouse phenotypes separate**, particularly when annotating variant effects, prevalence, prognosis and treatment efficacy. [18][24][78][17]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014115` (1 mention) - the report calls it "MONDO"; MONDO calls it **hypomyelination with brain stem and spinal cord involvement and leg spasticity**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `OMIM`, `UniProtKB`.