---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:25.479893'
end_time: '2026-10-09T20:58:43.746851'
duration_seconds: 198.27
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Goldberg-Shprintzen Syndrome
  mondo_id: MONDO:0012280
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0002251
    reported_labels:
    - Hirschsprung disease/aganglionic megacolon; congenital clinical sign and pathology
    ontology_label: Aganglionic megacolon
  - term_id: HP:0001250
    reported_labels:
    - Seizures; episodic symptom
    ontology_label: Seizure
  labels_variant: 5
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
- **Disease Name:** Goldberg-Shprintzen Syndrome
- **MONDO ID:** MONDO:0012280 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Goldberg-Shprintzen Syndrome** covering all of the
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

# Goldberg–Shprintzen syndrome: disease-characteristics report

**Goldberg–Shprintzen syndrome (GOSHS; MONDO:0012280) is an exceptionally rare, autosomal-recessive neurodevelopmental disorder caused by biallelic loss-of-function variants in *KIFBP*.** Its characteristic combination is microcephaly, developmental impairment and distinctive facial features, with variable Hirschsprung disease and cerebral malformations. The name must **not** be confused with **Shprintzen–Goldberg syndrome**, a different, *SKI*-associated craniosynostosis disorder. The authoritative ClinGen assessment classifies the *KIFBP*–GOSHS relationship as **definitive**. [2][3][151][160]

**Evidence convention.** “Human” below means affected individuals or patient-derived material; “model” means experimental animals; “cellular” means cell-culture experiments. Proposed links from an experimental finding to a particular human manifestation are identified as inferences. Frequencies from small, literature-assembled case series are **not** population estimates. [60][151]

## 1. Disease information

| Identifier or name | Knowledge-base value and interpretation |
|---|---|
| Preferred name; disease class | Goldberg–Shprintzen syndrome; Mendelian, multiple-congenital-anomaly/neurodevelopmental syndrome. [2][3] |
| MONDO | **MONDO:0012280**. [155] |
| OMIM | **609460**; causal-gene entry **609367**. [2][104] |
| Orphanet | **ORPHA:66629**. [3] |
| ICD-10; ICD-11 | **Q87.8**; **LD2F.1Y**, respectively. These are classification mappings, not uniquely identifying codes. [50] |
| MeSH; UMLS; SNOMED CT | **C537279**; **C1836123**; **717822006**, respectively. [50][53][54] |
| Synonyms | Goldberg–Shprintzen **megacolon** syndrome; megacolon–microcephaly syndrome; GOSHS. Historic gene names include *KIAA1279* and *KIF1BP*. [3][50][151] |
| Evidence unit and provenance | This entry synthesizes **aggregated disease-level resources**, published individual cases/families, experimental studies and expert curation. It is **not** derived from a supplied patient EHR. [60][151] |

Orphanet describes a syndrome combining Hirschsprung disease, characteristic facial dysmorphism, global developmental delay/intellectual disability and variable polymicrogyria or corpus-callosum hypoplasia. A person can nevertheless have molecularly confirmed GOSHS **without** Hirschsprung disease. [3][60]

## 2. Etiology: causal, risk and protective factors

The established initiating cause is **two pathogenic *KIFBP* alleles**, usually inherited in the germline. Documented disease-associated classes include nonsense variants, frameshifts and intragenic exon deletions. In its 25 July 2023 evaluation, ClinGen counted nine homozygous loss-of-function variants in ten probands and concluded: **“The mechanism of pathogenicity appears to be loss of function.”** This is stronger evidence than the evidence for individual reported missense alleles. [151]

| Factor category | Disease-specific conclusion |
|---|---|
| Genetic risk | Having pathogenic variants on **both** *KIFBP* alleles is the established causal risk. Consanguinity increases the chance that relatives inherit the same rare allele; eight of the ten probands included in the 2023 ClinGen curation came from known-consanguineous families. [151] |
| Possible phenotypic modifiers | Hirschsprung status can differ among relatives with the **same** *KIFBP* variant. A study testing selected common *RET*, *NRG1* and *SEMA3A* polymorphisms found **no significant association** with Hirschsprung status in its small comparison (*p* ≈ 0.526). These genes are **not established GOSHS modifiers**. [60] |
| Environmental risk or protection | No exposure, diet, lifestyle behavior, pathogen, vaccine or protective environmental intervention is established as causing or preventing this Mendelian syndrome. Nutrition and infection prevention may improve health **after diagnosis**, not prevent the genotype. [3][151] |
| Protective alleles; gene–environment interactions | No validated protective *KIFBP* allele, modifier allele or disease-specific gene–environment interaction was identified in the reviewed evidence. Differences between similarly genotyped siblings suggest additional influences, but do not identify them. [60] |

## 3. Phenotypes

**Frequency interpretation:** The most useful case compilation tabulates **34 reported people**, heavily enriched for recognizable features. Its **24/34 Hirschsprung cases (~71%)** should not be interpreted as penetrance in an unselected population. Orphanet reports cerebral MRI abnormalities in **about half** of patients, whereas the literature table records “brain malformation” for **32/34**; differences in case ascertainment, definitions and available imaging make those figures unsuitable for pooling. The HPO terms below are annotation suggestions, not a claim that every feature is diagnostic. [60][50][169]

| Phenotype and type | Suggested HPO term | Onset, severity, course and available frequency | Functional or quality-of-life effect |
|---|---|---|---|
| Hirschsprung disease/aganglionic megacolon; congenital clinical sign and pathology | **HP:0002251** | Usually neonatal; **24/34** in one literature compilation. Ranges from constipation to severe obstruction; aganglionosis persists without definitive treatment. [60][50] | Feeding, bowel function and hospitalization; possible enterocolitis. [50][255] |
| Microcephaly; physical sign | **HP:0000252** | Congenital/early; **33/34** recorded in the same case table; severity varies. [60] | Accompanies neurodevelopmental impairment, although head size alone does not measure function. [60] |
| Global developmental delay, particularly expressive-language impairment; clinical/functional sign | **HP:0001263**; speech/language delay **HP:0000750** | Early childhood; Orphanet describes severe delay, while individual abilities vary. [50] | Learning, communication and support needs. [50] |
| Intellectual disability; developmental/behavioral finding | **HP:0001249** | Recognized during childhood; often moderate–severe in Orphanet’s description. [50] | Lifelong effects on education and independent functioning; no syndrome-specific validated QoL score was found. [50] |
| Cerebral gyral malformation, including polymicrogyria or pachygyria; imaging/structural sign | **HP:0002126**; **HP:0001302** | Developmental/congenital; occurrence depends substantially on imaging and case definition. [50][179] | May accompany developmental or neurological disability; an individual lesion’s contribution is not quantified. [50] |
| Hypoplastic corpus callosum; imaging sign | **HP:0002079** | Congenital, variably reported. [50][169] | Potential interhemispheric-network impairment; individual functional effect uncertain. |
| Axonal/peripheral neuropathy; examination or electrophysiologic finding | **HP:0009830**; motor axonal neuropathy **HP:0007002** where demonstrated | Childhood or later; insufficient standardized testing for a reliable frequency. One reported patient had sensorimotor neuropathy; another had demyelinating neuropathy. [60][169] | Possible gait, strength and sensory impairment. |
| Hypotonia; clinical sign | **HP:0001252** | Usually apparent in infancy/childhood; variable. [50][179] | Can add to motor and feeding difficulties. |
| Seizures; episodic symptom | **HP:0001250** | Variable childhood presentation; not universal. [60][179] | Episodic safety and care burden. |
| Short stature; physical sign | **HP:0004322** | Growth-related, variable. [50][179] | Growth/nutrition assessment may be needed. |
| Facial gestalt—hypertelorism, ptosis, sloping forehead, prominent ears and pointed chin; physical signs | **HP:0000316**, **HP:0000508**, **HP:0000340**, **HP:0000400**, **HP:0000307** | Present at birth but may become more evident with age; no dependable feature-by-feature percentage. [50][179] | Mainly diagnostic; ptosis can warrant visual assessment. |
| Ocular anomalies, including iris coloboma, hyperopia, megalocornea or corneal problems; physical/clinical signs | Iris coloboma **HP:0000612**; other terms require finding-specific coding | Variable; the 34-case table records **eye anomalies as a group**, not an interchangeable frequency for each diagnosis. [50][60] | Visual impairment or corneal injury can affect daily function. |
| Cleft palate or bifid uvula; structural signs | Cleft palate **HP:0000175** | Occasional/variable; present from birth. [50][179] | Feeding and speech effects depend on the defect. |
| Congenital cardiac, renal/urogenital or skeletal findings; structural signs | Assign **finding-specific HPO terms**, rather than one syndrome-wide code | Ventricular septal defect, valve incompetence, cryptorchidism, reflux/renal dysplasia, scoliosis and hand/foot differences are reported but individually uncommon or poorly quantified. [50] | Organ-specific surveillance or intervention may be needed. |
| Progressive ataxia, ophthalmoparesis and hypogonadotropic hypogonadism; late neurological/endocrine findings | Ataxia **HP:0001251**; code other findings to confirmed examination/laboratory result | **Early-adult-onset, progressive findings in one four-sibling family**, reported in 2024; do **not** treat them as common or inevitable. [77] | May add later mobility, ocular-motor and reproductive-health needs. |

No GOSHS-specific EQ-5D, SF-36, PROMIS or per-phenotype quality-of-life estimates were established by these sources; functional effects above are clinical interpretations, **not measured scores**. [50][60]

## 4. Genetic and molecular information

**Gene annotation:** *KIFBP*, **HGNC:23419**, NCBI Gene **26128**, OMIM **609367**, UniProt **Q96EK5**, at **10q22.1**. *KIAA1279* and *KIF1BP* are older names for the **same gene**, not additional established GOSHS genes. The pathogenic variants described here are **germline**, rather than a recognized somatic cancer mechanism. [91][104][151][155]

| Illustrative *KIFBP* variant or class | Human and functional evidence; interpretation |
|---|---|
| **NM_015634.4:c.268C>T, p.(Arg90Ter)** | Homozygous nonsense variant in a reported family; a condition-specific ClinVar record calls it **pathogenic**, with **no assertion criteria supplied**. Patient-cell work indicates markedly decreased mutant RNA/protein. Historic publications use differing cDNA numbering; retain the stated transcript with any HGVS name. [155][146] |
| **c.1516dupA, p.(Ile506Asnfs*3)**; **c.1694_1695delAG, p.(Glu565Asnfs*15)** | Reported homozygous frameshifts; experimental truncating-variant work found decreased RNA and no detectable protein. Both are examples, **not** an exhaustive variant catalogue. [60] |
| **Exon-6 or exons-5–6 deletions** | Reported homozygous intragenic deletions, illustrating why copy-number analysis matters if sequencing does not explain a compelling phenotype. [60] |
| **c.1723delC, p.(His575Ilefs*19)** | Homozygous last-exon frameshift in an 18-month-old with microcephaly, developmental delay, dysmorphism and Hirschsprung disease; reported in **2021**, PMID **34421502**. Its last-exon position makes an automatic nonsense-mediated-decay prediction inappropriate without testing. [78] |
| **c.68A>G, p.(Glu23Gly); c.1279A>G, p.(Ser427Gly); c.565C>T, p.(Pro189Ser)** | Missense alleles reported in affected individuals. A **2020 cellular study** measured reduced expression and proposed a protein-expression threshold; its reported gnomAD exome frequencies were approximately **0.001707**, **0.0000244** and **0**, respectively, in the datasets it used. **Do not assign class-wide pathogenicity:** ClinGen’s 2023 expert curation specifically judged evidence for missense causation **insufficient**. Review each current variant record and segregation/functional evidence separately. [60][151] |

No recurrent **large chromosomal abnormality**, validated GOSHS modifier gene, disease-specific methylation signature or established epigenetic causal mechanism is documented here. Intragenic *KIFBP* deletions **are** established variant types. [60][151]

## 5. Environmental information

GOSHS is a **genetic developmental disease**, not an infectious or toxin-induced syndrome; there is no established causal smoking, alcohol, diet, occupational, pollution, radiation or infectious-agent exposure. Environmental and social circumstances can affect nutrition, infection risk, access to developmental services and outcomes **after** disease onset, without becoming an established cause of GOSHS. There is consequently no disease-specific pathogen taxonomy, CHEBI-coded causal chemical or exposure-based prevention target to populate. [3][151][255]

## 6. Mechanism and pathophysiology

**Ordered causal chain — experimental evidence and inference separated**

1. **Biallelic germline *KIFBP* loss-of-function variants lead to absent or markedly reduced functional KIFBP protein.** This is supported by human genetics and variant-expression experiments. [151][81]
2. **Reduced KIFBP leads to altered regulation of selected kinesin motors and cytoskeletal dynamics.** Structural experiments show that normal KIFBP can remodel kinesin motor heads and prevent their microtubule binding; which particular motor disruption produces each patient feature remains **inferred**. [106]
3. **Neural-development branch:** cytoskeletal dysregulation leads to abnormal axon extension/maintenance and neuronal migration, morphology and survival in models; these changes **plausibly lead to** human neuropathy, cortical malformations and developmental impairment. The model-to-individual-manifestation connection is **inferred**, not directly proved in patients. [258][107]
4. **Enteric branch:** *Kifbp* loss leads to **delayed** neural-crest colonization of mouse gut and defective extrinsic gut innervation; insufficient human enteric ganglion development leads to rectal/colonic aganglionosis, impaired motility and Hirschsprung symptoms. Importantly, newborn knockout mice **did have neurons along the entire bowel**: a fully aganglionic mouse colon was **not** demonstrated. [web:29192291][229]
5. **Cell-division branch:** KIFBP loss/knockdown leads to midbody microtubule and cytokinesis abnormalities in cultured cells; impaired neural-progenitor production **may contribute to** microcephaly. That final contribution remains **a hypothesis**, not a demonstrated human causal step. [web:34100550]

The chain is principally **cytoskeletal and developmental**, not an established Wnt, MAPK, mTOR or PI3K–AKT syndrome pathway. KIFBP is a kinesin-binding regulator, **not an enzyme deficiency or receptor defect**. Cryo-EM work found that KIFBP blocks kinesin–microtubule interaction through both steric and allosteric effects; its abstract states: **“KIFBP remodels kinesin motors and blocks microtubule binding.”** (Structural/in-vitro evidence; PMID **34797717**, 19 November 2021.) [106]

For the brain branch, embryonic-mouse cortical *Kifbp* knockdown disrupted migration, dendritic/axonal development and postnatal survival. Approximately **one-third of labeled neurons remained ectopically in white matter at postnatal day 6** in that experiment; this is a **model result**, not a patient frequency. (PMID **31736709**, 1 November 2019.) [web:31736709] For the enteric branch, the mouse-study abstract explicitly says **“the colonization of the gut by neural crest-derived cells was delayed”** (PMID **29192291**, 30 November 2017). [web:29192291]

| Mechanistic annotation | Suggested controlled terms and evidence boundary |
|---|---|
| Cytoskeletal organization; axon formation | **GO:0000226** microtubule cytoskeleton organization; **GO:0007409** axonogenesis; **GO:0030424** axon. Model and structural support. [200][205][258] |
| Enteric precursor and cortical neuron movement | **GO:0001755** neural crest cell migration; **GO:0001764** neuron migration; **CL:0000333** migratory neural crest cell. Model support; human pathway attribution is inferential. [166][167][209][107] |
| Division of precursor cells | **GO:0000910** cytokinesis; **GO:0030496** midbody. Demonstrated in cellular work; contribution to patient microcephaly proposed. [201][202][web:34100550] |
| Metabolism, immune injury and other ‘omics | No reproducible **GOSHS-specific** metabolomic, lipidomic, immune, proteomic-diagnostic, epigenomic, patient single-cell or spatial-transcriptomic signature is established by these studies. Interactome/proteomic methods helped identify the **CITK–KIFBP interaction**, but do not constitute a clinical proteomic biomarker. [web:34100550] |

## 7. Anatomical structures affected

| Level | Sites, laterality and annotation |
|---|---|
| Primary organs | **Brain/cerebral cortex** (**UBERON:0000955; UBERON:0000956**) and **colon/rectum** (**UBERON:0001155; UBERON:0001052**) are principal sites. Distal enteric plexuses and cortical neuronal circuits are particularly relevant. [243][244][229][50] |
| Primary tissues and cells | Developing nervous tissue; migrating neural-crest-derived enteric precursors (**CL:0000333**, broad precursor term), enteric neurons, cortical neural progenitors and projection neurons. Enteric **submucosal and myenteric plexus** ganglion cells are absent in affected bowel; do not equate that biopsy finding with demonstrated loss of every neuron throughout the gut. [209][229][web:29192291][web:31736709] |
| Secondary involvement | Peripheral nerves, eyes, craniofacial structures and, variably, cardiac, renal/urogenital or skeletal structures. These are variable clinical findings, not proof of a single tissue-specific injury mechanism. [50][60] |
| Subcellular sites | Cytoplasmic microtubules/axons (**GO:0030424**), actin-associated cytoskeleton (**GO:0005856**) and dividing-cell midbody (**GO:0030496**). Earlier mitochondrial-localization proposals should not be treated as established universal localization: a human-fibroblast experiment instead observed actin/tubulin interaction **without** mitochondrial colocalization. [30][202][207] |
| Localization pattern | Aganglionosis particularly involves the **distal bowel**; cerebral gyral abnormalities may be focal or more generalized. No universal left-versus-right lateralization is established. [50][229] |

## 8. Temporal development

GOSHS begins **developmentally**, commonly presenting with microcephaly and, when present, bowel-obstruction signs in the **neonatal period**. Dysmorphism may become more recognizable with age; developmental and language limitations emerge through childhood. Congenital malformations do not imply that every manifestation is static: the four-sibling 2024 report introduced **early-adulthood-onset progressive** ataxia, ophthalmoparesis and hypogonadotropic hypogonadism. [50][77]

There is no validated early/intermediate/end-stage scheme, measured population-wide progression rate, typical remission pattern or fixed disease duration beyond its genetic, lifelong basis. Clinically important windows are **prompt evaluation of neonatal obstruction**, early developmental assessment and later follow-up tailored to emerging neurological and other needs; those are care priorities, not proven GOSHS-specific critical-period trial results. [50][255]

## 9. Inheritance and population

| Characteristic | Best-supported value |
|---|---|
| Mode; recurrence | **Autosomal recessive**. For two confirmed carrier parents, each pregnancy has a **25% affected**, **50% carrier** and **25% neither-variant** Mendelian probability. [50][151] |
| Prevalence; incidence | Orphanet lists **<1 per 1,000,000 prevalence**. No reliable annual incidence per 100,000 is available. Its narrative’s “24 cases” is an **outdated literature count**, not a present-day census: a 2020 analysis already tabulated **34**, and subsequent reports added cases. [50][60][78] |
| Penetrance; expressivity | No robust quantitative estimate of overall biallelic penetrance. **Expressivity is variable**: Hirschsprung disease affected **24/34** assembled cases and can differ between siblings with the same variant. Do not interpret Hirschsprung frequency as overall syndrome penetrance. [60] |
| Anticipation; mosaicism; carrier frequency | No established anticipation, recurrent germline mosaicism mechanism or reliable population-wide *KIFBP* pathogenic-carrier frequency. Do not derive one by treating all rare missense alleles as pathogenic. [151] |
| Consanguinity; founder effects | Consanguinity appears in many reported families. Recurrence of an allele within a family does **not**, by itself, establish a population-wide founder effect. [151][146] |
| Demography and geography | Cases are reported across different ancestries and locations, but no validated geographic prevalence gradient, sex ratio or age-distribution estimate is available. The adult siblings show that ascertainment need not stop in childhood. [60][77] |

## 10. Diagnostics

**Practical diagnostic route:** recognize a suggestive combination—particularly microcephaly/developmental impairment, characteristic face, bowel symptoms and/or cortical malformation—then establish **biallelic pathogenic/likely pathogenic *KIFBP* variants** with segregation where feasible. Do **not** require Hirschsprung disease. The causal molecular marker is *KIFBP* genotype; there is no established syndrome-specific circulating protein, metabolite or enzyme assay. [50][60][151]

| Investigation | Purpose and interpretation |
|---|---|
| *KIFBP* sequencing or an appropriate Hirschsprung/neurodevelopmental-malformation panel | Detect SNVs and small indels; interpret each allele using current ACMG/AMP-style evidence, inheritance and phenotype. A missense finding alone is particularly uncertain given ClinGen’s caution. [151][221] |
| WES or WGS | Useful when the phenotype is broad or the differential is substantial; exome analysis identified a homozygous last-exon frameshift in a published child. Assess coverage and copy-number detection before calling testing negative. [78][60] |
| Deletion/duplication analysis | Include when one/no explanatory allele is found: homozygous **intragenic exon deletions** have been reported. Chromosomal microarray may find a sufficiently large deletion but is **not** a substitute for sequence and appropriately resolved copy-number testing. [60] |
| Rectal suction or surgical biopsy | **Confirm suspected Hirschsprung disease by representative rectal histology showing aganglionosis**; biopsy should include adequate submucosa. Contrast enema and anorectal manometry can assist but do not replace histologic confirmation. [50][185][259] |
| Brain MRI; developmental and organ assessments | MRI characterizes cortical/callosal differences; growth, hearing/vision, neurological and developmental assessments—and targeted cardiac, renal or orthopedic evaluation—address the person’s findings. EEG or peripheral nerve studies are **indication-driven**, not validated universal GOSHS tests. [50][60] |
| Tests without an established routine GOSHS indication | Karyotype, FISH, mitochondrial-DNA, repeat-expansion, RNA-seq, proteomic/metabolomic/epigenomic assays and liquid biopsy do **not** have established routine diagnostic roles for this monogenic condition; a specialist may use selected tests to investigate an alternative diagnosis or unresolved variant. [151] |

Important differentials include **Mowat–Wilson syndrome** and **Baraitser–Winter syndrome**, which can overlap in developmental or facial findings; **Shprintzen–Goldberg syndrome** is especially liable to name-based confusion but involves *SKI* and a different craniosynostosis/connective-tissue presentation. There is no standalone standardized clinical score that replaces molecular confirmation. [50][160] For an asymptomatic relative, offer **familial-variant cascade/carrier testing** rather than claiming a population newborn-screening program exists. [50]

## 11. Outcome and prognosis

The central long-term burdens are developmental disability and, in affected individuals, bowel dysmotility, possible enterocolitis, visual/neurological problems or other organ-specific complications. Severity differs appreciably even within families. **No defensible GOSHS-specific five- or ten-year survival percentage, mortality rate, life expectancy, quantitative disability score, validated prognostic model or prognostic biomarker is available.** Orphanet states that long-term information is limited and outcome depends on the presence and severity of associated defects. Mouse knockout perinatal lethality **must not** be presented as human life expectancy. [50][60][web:29192291]

## 12. Treatment and real-world implementation

There is **no established treatment that restores KIFBP function**. Care is individualized and multidisciplinary; Hirschsprung interventions treat the bowel consequence, while developmental and organ-specific interventions address other needs. The intervention labels below are **suggested NCIt/NCIT search terms**, *not verified NCIt accession codes*. [50][151]

| Treatment or intervention | Indication, mechanism, evidence and suggested NCIT term |
|---|---|
| Rectal irrigation/decompression and stabilization | Used when clinically indicated for obstructive Hirschsprung presentations before definitive care; addresses fecal retention, **not** the genetic cause. **NCIT search term:** *Bowel Irrigation*. Apply Hirschsprung guidance with a pediatric surgical team. [265][255] |
| Histology-guided pull-through surgery, sometimes staged with a stoma | Removes/bypasses aganglionic bowel and connects normally innervated bowel; confirm diagnosis histologically first. **NCIT search terms:** *Pull-Through Procedure*, *Colostomy*. Technique and timing depend on bowel anatomy and condition. Published guidelines are for Hirschsprung disease generally, **not GOSHS-specific response trials**. [185][181][259] |
| Management and follow-up of enterocolitis, constipation and bowel function | Specialist-directed treatment and surveillance for Hirschsprung complications. The updated ERNICA guidance addresses individualized diet, long-term follow-up and the role of botulinum toxin for selected Hirschsprung-associated enterocolitis management; it **does not establish botulinum toxin as GOSHS therapy**. **NCIT search terms:** *Supportive Care*, *Botulinum Toxin Treatment*. [255] |
| Early intervention, special education, speech, occupational and physical therapies | Tailor support to communication, learning, motor function and independence. **NCIT search terms:** *Speech Therapy*, *Occupational Therapy*, *Physical Therapy*, *Supportive Care*. No GOSHS-specific comparative response rate is available. [50] |
| Targeted ocular, cardiac, renal/urogenital, skeletal or neurological care | Examination, monitoring and conventional correction/treatment **if the relevant abnormality exists**; there is no evidence that every patient needs each intervention. **NCIT search terms:** *Ophthalmologic Examination*, *Cardiac Monitoring*, *Surgical Procedure*. [50] |
| Gene, cell, RNA, targeted or immune therapy | **No established or approved GOSHS-specific intervention** or efficacy/adverse-event rate was identified in the reviewed evidence. Do not transfer *SKI*-syndrome or unrelated aortopathy trials to this diagnosis. [63][151][160] |

The **2025-updated ERNICA rectosigmoid-Hirschsprung guideline**, published online **30 April 2026** (PMID **42057764**), incorporates evidence through 2024 and specifically says **“Routine preventive anal dilatations were no longer recommended.”** Its scope is Hirschsprung care, not syndrome-specific proof of treatment effect; neither drug pharmacogenomics nor genotype-guided *KIFBP* therapy is established. [web:42057764]

## 13. Prevention

**Primary prevention of an affected genotype** is a reproductive-counseling question, not a lifestyle, vaccine or environmental-control intervention. Once familial pathogenic variants are established, offer genetic counseling, relative/carrier testing and discussion of available prenatal or preimplantation genetic-testing options according to the family’s preferences and local practice. A prior affected child of two carriers implies a **25% recurrence risk per pregnancy**. Ultrasound findings may raise suspicion but cannot reliably establish or exclude GOSHS. **NCIT search term:** *Genetic Counseling*. [50]

**Secondary prevention** means prompt recognition of neonatal obstruction, biopsy when Hirschsprung disease is suspected, and early developmental/organ assessment; it is **not** population newborn screening for GOSHS. **Tertiary prevention** means bowel-complication surveillance, appropriate nutrition and rehabilitative support. Routine childhood immunization remains ordinary preventive care, not GOSHS-specific prophylaxis. No disease-specific preventive drug, vaccine, environmental intervention or public-health screening program is established. [50][255]

## 14. Other species and natural disease

**Naturally occurring, clinically diagnosed Goldberg–Shprintzen syndrome is established in humans, not as a documented veterinary breed disorder.** Accordingly there is no substantiated affected breed/VBO entry, naturally occurring animal incidence, veterinary treatment pathway or zoonotic transmission to populate. Orthologs and engineered/induced phenotypes are **comparative models**, not evidence of naturally occurring animal disease. [151][270][273]

| Species; NCBI Taxon ID | Ortholog and identifier | Comparative relevance |
|---|---|---|
| Human, *Homo sapiens*; **9606** | *KIFBP*; NCBI Gene **26128** | Naturally occurring germline syndrome. [91][151] |
| House mouse, *Mus musculus*; **10090** | *Kifbp*; NCBI Gene **72320**, MGI **1919570** | Experimental loss recapitulates aspects of brain and gut-neural development, but knockout survival and bowel histology differ from humans. [273][web:29192291] |
| Zebrafish, *Danio rerio*; **7955** | *kifbp*; **ZDB-GENE-070117-1989** | Experimental axonal/enteric nervous-system biology; anatomy and developmental timing are not identical to humans. [270][272][258] |

## 15. Model organisms and experimental systems

| Model and resource | Recapitulated findings, application and limitation |
|---|---|
| **Mouse *Kifbp* knockout**; MGI **MGI:1919570** | Two knockout lines showed smaller brains/olfactory bulbs/anterior commissures, delayed enteric-crest colonization and defective vagal/sympathetic gut innervation; mice died shortly after birth. **Limitation:** neurons remained along the entire newborn bowel, so this is not a complete reproduction of human Hirschsprung aganglionosis or human survival. Used to study CNS/ENS development and axon extension. PMID **29192291**. [web:29192291][26] |
| **Mouse embryonic-cortex shRNA knockdown**, delivered by *in utero* electroporation | Tests cortical migration, axonal/dendritic morphology and survival; about one-third of labeled neurons remained ectopic at postnatal day 6. **Limitation:** regional, partial knockdown is not whole-organism biallelic inherited disease. PMID **31736709**. [web:31736709] |
| **Zebrafish *kifbp*<sup>st23</sup> mutant**; ZFIN *kifbp* **ZDB-GENE-070117-1989** | Splice-donor-disrupting, strong loss-of-function model; impaired axonal outgrowth/maintenance and later axon degeneration, with peripheral, central and enteric nervous-system findings. Useful for live imaging of axon development; it does **not** reproduce the whole human clinical syndrome. PMID **18192286**. [279][258][270] |
| **Human fibroblast and neuronal-like cell experiments** | Demonstrate cytoskeletal interaction and altered neurite growth; variant-expression experiments test whether specific alleles reduce protein. **Limitation:** assays alone cannot establish clinical penetrance or pathogenicity for every missense allele. PMIDs **23427148** and **32939943**. [30][81][151] |
| **Cultured-cell CITK/midbody studies; purified-protein cryo-EM** | Probe cytokinesis and the molecular mechanism of kinesin inhibition, respectively. **Limitation:** the proposed human microcephaly contribution and exact disease-producing kinesin targets remain unresolved. PMIDs **34100550** and **34797717**. [web:34100550][106] |

**Knowledge-base caution:** retain *KIFBP*–GOSHS as a definitive **loss-of-function** gene–disease relationship, but keep missense pathogenicity, individual modifier genes, disease-specific treatment efficacy and long-term survival in **unresolved** fields unless variant- or patient-specific evidence supports them. A 2024 case report’s statement that this *KIFBP* syndrome is “autosomal dominant,” and a separate 2024 report’s conflation of *KIFBP* with *SKI*, conflict with expert gene–disease curation and should **not** be imported into this entry. [151][211][212]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002251` (1 mention) - the report calls it "Hirschsprung disease/aganglionic megacolon; congenital clinical sign and pathology"; HP calls it **Aganglionic megacolon**
- `HP:0001250` (1 mention) - the report calls it "Seizures; episodic symptom"; HP calls it **Seizure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000252` (1 mention) - the report calls it "Microcephaly; physical sign"; HP calls it **Microcephaly**
- `HP:0001249` (1 mention) - the report calls it "Intellectual disability; developmental/behavioral finding"; HP calls it **Intellectual disability**
- `HP:0002079` (1 mention) - the report calls it "Hypoplastic corpus callosum; imaging sign"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplastic corpus callosum" among its other names
- `HP:0001252` (1 mention) - the report calls it "Hypotonia; clinical sign"; HP calls it **Hypotonia**
- `HP:0004322` (1 mention) - the report calls it "Short stature; physical sign"; HP calls it **Short stature**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.