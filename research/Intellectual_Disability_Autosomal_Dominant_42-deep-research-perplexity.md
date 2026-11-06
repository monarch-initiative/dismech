---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-22T13:25:31.790819'
end_time: '2026-10-22T13:30:24.144691'
duration_seconds: 292.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intellectual Disability Autosomal Dominant 42
  mondo_id: MONDO:0014855
  category: Mendelian
  causal_genes: GNB1
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
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability Autosomal Dominant 42
- **MONDO ID:** MONDO:0014855 (if available)
- **Causal gene(s):** GNB1
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

Please provide a comprehensive research report on **Intellectual Disability Autosomal Dominant 42** covering all of the
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

# Intellectual Disability, Autosomal Dominant 42 (*GNB1* encephalopathy)

**Report date: 22 October 2026.** Intellectual disability, autosomal dominant 42 is a rare, usually *de novo*, autosomal-dominant neurodevelopmental disorder caused by heterozygous pathogenic variants in ***GNB1***, which encodes the G-protein β1 subunit. The preferred clinically informative name is ***GNB1*-related neurodevelopmental disorder** or ***GNB1* encephalopathy (GNB1-E)**. It is characterized principally by congenital/infantile global developmental delay, intellectual disability, hypotonia, epilepsy, movement and visual disorders, and variably abnormal brain imaging. ClinGen’s Intellectual Disability/Autism Expert Panel classified the *GNB1*–disease relationship as **Definitive** on 16 August 2023. [3][376]

> **Evidence caveat:** Published cohorts are small, clinically heterogeneous, and affected by ascertainment and missing-data bias. Frequencies below should therefore be treated as provisional rather than population estimates.

---

## 1. Disease information

### Definition and identifiers

| Resource | Identifier/name | Interpretation |
|---|---|---|
| MONDO | **MONDO:0014855** | Intellectual disability, autosomal dominant 42 |
| OMIM phenotype | **616973** | Intellectual developmental disorder, autosomal dominant 42 |
| OMIM gene | **139380** | *GNB1* |
| Orphanet | **ORPHA:488613** | Global developmental delay–neuro-ophthalmological abnormalities–seizures–intellectual disability syndrome |
| Disease Ontology | **DOID:0070072** | Autosomal dominant intellectual developmental disorder 42 |
| MedGen | **C4310774**; UID 934741 | MRD42 / *GNB1* encephalopathy |
| HGNC | **HGNC:4396** | *GNB1* |
| NCBI Gene | **2782** | *GNB1*, chromosome 1p36.33 |
| Ensembl | **ENSG00000078369** | Human *GNB1* |
| UniProt | **P62873** | G-protein β1 |
| ClinVar condition | MONDO:0014855 / OMIM:616973 | Germline variant submissions for MRD42 |
| ICD-10/ICD-11 | No specific *GNB1*-E code identified | Code the manifestations—intellectual developmental disorder, epilepsy, dystonia, visual impairment, feeding disorder, etc.—according to local coding rules |
| MeSH/SNOMED CT | No disease-specific public identifier confirmed | Broader intellectual-disability/neurodevelopmental-disorder concepts may be used |

The OMIM phenotype number is **616973**, notwithstanding the query’s “not recorded” field; **139380** is the gene’s OMIM number. Orphanet links causal germline *GNB1* variation to ORPHA:488613. [6][196][475]

### Synonyms

- *GNB1* encephalopathy / GNB1-E  
- *GNB1*-related disorder  
- *GNB1*-related neurodevelopmental disorder  
- Intellectual developmental disorder, autosomal dominant 42  
- Intellectual disability, autosomal dominant 42  
- MRD42  
- Global developmental delay–neuro-ophthalmological abnormalities–seizures–intellectual disability syndrome  
- Historical: autosomal dominant mental retardation 42

These aliases are consolidated in MedGen, ClinVar, GARD, and Orphanet. [1][197][468]

### Data provenance

The clinical evidence comes primarily from **aggregated, publication-level case series and case reports**, not population EHR studies. The foundational study used exome sequencing in 5,855 individuals with undiagnosed genetic disorders and identified 13 affected subjects; subsequent reports combined laboratory referrals, trio sequencing, international clinical collaborations, and literature review. GeneReviews, OMIM, ClinVar, HPO, MedGen, ClinGen, and Orphanet aggregate these patient-level reports into disease-level summaries. [48][191]

---

## 2. Etiology, risk, protection, and environment

### Causal factor

The direct cause is a **heterozygous germline pathogenic or likely pathogenic *GNB1* variant**. Most reported cases are *de novo* missense variants, particularly in the Gα/Gγ/effector-interaction region of the Gβ1 WD40 propeller, but splice-site, frameshift and nonsense variants causing loss of function/haploinsufficiency are established as a second mechanism. [48][154][156]

### Risk and protective factors

| Factor class | Current evidence |
|---|---|
| Genetic causal risk | A heterozygous pathogenic *GNB1* variant is sufficient. Recurrent residues include Asp76, Gly77, Lys78, Ile80, Leu95, Met101 and Asp118. |
| Inherited risk | An affected heterozygous parent transmits the variant with a **50% probability per pregnancy**. |
| Parental mosaicism | Clinically unaffected parents can theoretically carry germline or low-level somatic mosaicism; recurrence risk after an apparently *de novo* case is therefore above population background, often counseled at approximately 1%. [80][181] |
| Proband mosaicism | One mosaic patient had a milder phenotype, suggesting variant allele fraction can modify severity. [106] |
| Variant-specific modifiers | Ile80 substitutions have been associated with dystonia and growth delay; truncating/splice variants are associated with obesity/hyperphagia. These are provisional correlations. [123][36] |
| Sex | Both sexes are affected. No convincing sex-dependent penetrance is known; genitourinary abnormalities have been reported specifically in males. |
| Ethnicity/geography | No enriched ancestry, geographic cluster, or founder effect has been established. |
| Environmental risk | No toxin, diet, occupation, smoking, alcohol, radiation, or infection causes the Mendelian disorder. |
| Protective genetic variants | None established. |
| Protective lifestyle factors | None can prevent the genotype. Early therapy, seizure control, safe feeding and weight management may reduce secondary morbidity but are not genetically protective. |
| Gene–environment interaction | Limited evidence. Fever/influenza or other acute physiologic stress may precipitate seizures or acute encephalopathy in susceptible individuals, but this is based on two patients rather than controlled evidence. [301] |

There are no validated modifier genes, protective alleles, GWAS loci, infectious causes, or environmental exposure interactions.

---

## 3. Phenotypes

The foundational 13-person cohort reported global developmental delay in **13/13**, hypotonia in **11/13**, seizures in **10/13**, ophthalmologic abnormalities in **8/13**, and growth delay in **6/13**. [48] In the later 18-person cohort, developmental disability was moderate–severe, more than half were nonambulatory and nonverbal, gastrointestinal abnormalities occurred in **61%**, and genitourinary abnormalities in **50% of males**. [106] Frequencies vary substantially by cohort.

### Phenotype matrix

| Phenotype/type | Onset, severity, course and frequency | Functional/QoL impact | Suggested HPO term |
|---|---|---|---|
| Global developmental delay; clinical sign | Infancy/early childhood; essentially universal in early cohorts; usually moderate–severe and lifelong. Motor and language domains are prominent. | Dependence for education, communication, mobility and self-care; frequent need for lifelong support. | Global developmental delay **HP:0001263** |
| Intellectual disability; clinical/cognitive | Usually becomes formally evident in childhood; reported in approximately 74–87%; mild cases exist, but moderate–severe is typical. [184] | Limits adaptive functioning, independent living and employment. | Intellectual disability **HP:0001249** |
| Speech/language delay | Childhood; all 18 patients in the 2018 cohort had speech delay and 13 were nonverbal; approximately 40% nonverbal in an earlier synthesis. [291][133] | Major communication burden; requires AAC and speech-language therapy. | Delayed speech and language development **HP:0000750**; absent speech **HP:0001344** |
| Motor delay/inability to walk | Early childhood; more than half of the expanded cohort were nonambulatory; some acquire late walking, occasionally after intensive therapy. [106][133] | Mobility devices, positioning support and caregiver assistance may be required. | Motor delay **HP:0001270**; inability to walk **HP:0002540** |
| Infantile hypotonia | Congenital/infantile; 11/13 in the original series and 37/49 or 76% in a later summary. May be severe with quadriplegia or dysphagia. [113][109] | Feeding difficulty, delayed head control, impaired sitting/walking and respiratory vulnerability. | Hypotonia **HP:0001252**; infantile hypotonia **HP:0008947** |
| Hypertonia/spasticity | Often follows infantile hypotonia; variable and sometimes progressive in the limbs. | Contractures, pain, falls and impaired ambulation. | Limb hypertonia **HP:0002509**; spasticity **HP:0001257** |
| Epilepsy/seizures | Infancy to childhood, occasionally as late as 11 years; about 53–65% in broader summaries, though 10/13 in the discovery cohort. Focal, generalized tonic-clonic, tonic, atonic, myoclonic, absence seizures and infantile spasms occur; some are drug resistant. [102][109][128] | Injury risk, emergency admissions, developmental interference and caregiver burden. | Seizure **HP:0001250**; infantile spasms **HP:0012469** |
| Abnormal EEG | May occur with or without recognized seizures. Hypsarrhythmia, burst suppression, focal/multifocal spikes, generalized spike-wave and background slowing are reported. [286][295] | Detects subclinical epilepsy and guides antiseizure treatment. | Multifocal epileptiform discharges **HP:0010841**; generalized epileptiform discharges **HP:0011198** |
| Dystonia/movement disorder | Dystonia may begin from age 2–16 years and range from finger posturing to severe generalized dystonia; ataxia, chorea, athetosis, myoclonus and tics are less common. [107] | Can become the principal cause of pain, impaired mobility and loss of daily activities; rare severe crises may require DBS or intrathecal baclofen. | Dystonia **HP:0001332**; myoclonus **HP:0001336**; ataxia **HP:0001251** |
| Nystagmus/ocular motor disorder | Usually infancy/childhood; nystagmus approximately 36–46%; strabismus and ophthalmoplegia also occur. [107][422] | Impairs visual tracking, reading, balance and motor learning. | Nystagmus **HP:0000639**; strabismus **HP:0000486**; ophthalmoplegia **HP:0000602** |
| Cortical visual impairment/optic atrophy | Approximately 11% in one review; severity varies from reduced vision to cortical blindness. [107] | Requires vision-adapted learning and environmental support. | Cortical visual impairment **HP:0100704**; optic atrophy **HP:0000648** |
| Abnormal brain MRI | Approximately 25/50 or 50%; findings include delayed/abnormal myelination, corpus-callosum abnormality, cerebral volume loss, ventriculomegaly, polymicrogyria, cerebellar hypoplasia and nonspecific white-matter changes. [292][396] | Correlates imperfectly with impairment; helps exclude acquired injury and characterize complications. | Abnormal brain morphology **HP:0012443**, delayed myelination **HP:0012448**, corpus-callosum abnormality **HP:0001273** |
| Growth delay/failure to thrive | Childhood; 6/13 in the original cohort, associated in some reports with Ile80 substitutions. | Feeding interventions and sometimes gastrostomy are needed. | Growth delay **HP:0001510**; failure to thrive **HP:0001508** |
| Dysphagia/feeding problems | Often neonatal/infantile, particularly with severe hypotonia; aspiration risk is clinically important. | Poor nutrition, aspiration and prolonged mealtimes; swallow study or tube feeding may be necessary. | Feeding difficulties **HP:0011968**; oropharyngeal dysphagia **HP:0200136** |
| GI abnormalities | Reflux, constipation, cyclic vomiting, abdominal distension/cramps and rare hepatic-vein anomaly; 61% in the 18-person cohort. [106][429] | Pain, poor intake, sleep disruption and recurrent medical care. | Constipation **HP:0002019**; gastroesophageal reflux **HP:0002020**; cyclic vomiting **HP:0002572** |
| GU abnormalities in males | Cryptorchidism, hydronephrosis and duplicated collecting system; 50% of males in the 2018 new cohort. [106] | May require ultrasound, urology review or surgery. | Cryptorchidism **HP:0000028**; hydronephrosis **HP:0000126** |
| Behavioral/neuropsychiatric changes | Autism traits, stereotypies, ADHD, anxiety, low frustration tolerance, sleep disturbance and occasional psychiatric symptoms; frequency uncertain. | Adds educational, family and behavioral-management burden. | Autistic behavior **HP:0000729**; ADHD **HP:0007018**; stereotypy **HP:0000733** |
| Cutaneous mastocytosis | Four published patients in one synthesis; three of four carried p.Ile80Thr. Association is plausible but rare. [314] | Pruritus, flushing and risk of mediator-triggered symptoms. | Cutaneous mastocytosis **HP:0011970** |
| Obesity/hyperphagia | Important 2024 expansion: obesity in 8/42 patients with known weight status (19%), but 6/8 or 75% of informative truncating/splice-variant carriers versus 2/34 or 6% with missense variants. Median obesity onset was 3.5 years. [36] | Cardiometabolic risk, impaired mobility and need for environmental food control. | Obesity **HP:0001513**; hyperphagia **HP:0002591** |
| Congenital cardiac/craniofacial/hearing findings | Occasional congenital heart disease, palatal anomalies, craniosynostosis and hearing loss; no reliable frequencies. | Manifestation-dependent. | Use specific finding, e.g. congenital heart defect **HP:0001627**, hearing impairment **HP:0000365** |
| Acute encephalopathy/regression | Not typical, but two 2023 patients developed acute MRI lesions, cerebral atrophy, spastic tetraplegia and severe regression after influenza-associated seizures or respiratory arrest. [301] | Potential catastrophic loss of motor and cognitive function. | Acute encephalopathy **HP:0006846**; developmental regression **HP:0002376** |

No disease-specific EQ-5D, SF-36, PROMIS or validated caregiver-burden study was found. Functional effects are inferred from nonverbal status, nonambulation, dysphagia, epilepsy and dystonia rather than formal health-utility measurements.

---

## 4. Genetic and molecular information

### Gene/protein

| Item | Annotation |
|---|---|
| Gene | *GNB1* |
| HGNC | HGNC:4396 |
| NCBI Gene | 2782 |
| OMIM gene | 139380 |
| Location | 1p36.33 |
| MANE transcript | NM_002074.5 |
| Protein | Gβ1; UniProt P62873 |
| Protein architecture | Seven-bladed WD40 β-propeller; protein-interaction scaffold |
| Normal role | Forms a Gβγ dimer, assembles with Gα into heterotrimeric G proteins, and regulates GPCR–effector signaling |
| Main compartments | Plasma membrane, cytosol, heterotrimeric G-protein complex and synapse |
| ClinGen validity | Definitive, 16 August 2023 |
| ClinGen dosage note | The older 2019 dosage curation assigned “little evidence” for haploinsufficiency, but later functional and clinical studies provide stronger evidence that selected truncating/splice variants cause disease. [17][156] |

The WD40 repeats form a circular seven-bladed propeller that provides interaction surfaces for Gα, Gγ and downstream effectors. [453][456] Gβ1 is strongly expressed in brain but is not brain-specific. [136]

### Pathogenic variant spectrum

| Variant/class | Germline evidence and functional interpretation |
|---|---|
| p.Asp76Gly/Glu/Asn | Recurrent interaction-region missense changes; Asp76 variants were represented in the discovery cohort. |
| p.Gly77Ser/Arg/Ala/Val | Recurrent missense variants in the mutational cluster around residues 76–80. |
| **p.Lys78Arg (K78R)** | Pathogenic missense; increased GIRK activation in cortical neurons/oocytes and caused developmental, cognitive and seizure phenotypes in knock-in mice. |
| **p.Ile80Thr / p.Ile80Asn** | Most recurrent site; Ile80 variants represented about 28% in the 2018 synthesis and are associated provisionally with dystonia and growth delay. [123] |
| **p.Leu95Pro** | Recurrent pathogenic missense variant; associated with severe hypotonia, epilepsy, visual impairment and loss of GIRK regulation in functional studies. |
| p.Met101Val, p.Cys114Tyr, p.Asp118Gly/Tyr/His | Recurrent or functionally supported missense variants; Asp118 changes may prominently cause dystonia. |
| c.268-1G>T, c.700-1G>T, c.917-1G>T | Pathogenic/likely pathogenic splice variants; loss of normal transcript or truncation supports loss of function. |
| c.272_275del p.His91Profs*10; c.915_916del p.Gly306Cysfs*6; c.987_988del p.Gly330Valfs*4 | Frameshift variants supporting haploinsufficiency. |
| p.Trp211*, p.Arg214*, p.Cys114Trpfs*10 | Truncating variants enriched among patients with hyperphagia/obesity. [36] |

The 2017 functional study found that p.Arg52Gly, p.Gly64Val, p.Ala92Thr, p.Pro94Ser, p.Arg96Leu, p.Ala106Thr and p.Asp118Gly impaired Gβγ dimer formation, heterotrimer assembly or receptor-driven activation, whereas p.Leu30Phe, p.His91Arg and p.Lys337Gln were normal in that particular assay. A normal assay does not by itself prove clinical benignity because it tests only selected functions. [68][74]

### Classification, frequency and origin

- **Classification:** Each variant must be assessed under ACMG/AMP criteria as pathogenic, likely pathogenic, VUS, likely benign or benign. A VUS does **not** establish the diagnosis. [380]
- **Population frequency:** Well-supported causal variants are generally absent or exceptionally rare in gnomAD/1000 Genomes/ExAC. One recurrently reported p.Gly77Val variant was absent from ExAC, 1000 Genomes and ESP6500; individual ClinVar records also document absence from gnomAD. [153][165]
- **Origin:** Predominantly germline and *de novo*. Rare inherited dominant and proband-mosaic cases exist.
- **Mechanism:** Variant-specific—loss of heterotrimer assembly or haploinsufficiency, altered Gβγ-effector coupling, and GIRK gain or loss of function are all documented. A universal “gain-of-function” or “loss-of-function” label is therefore inappropriate.
- **Somatic distinction:** Somatic *GNB1* mutations also occur in hematologic malignancies and activate PI3K–AKT–mTOR and MAPK signaling. These cancer mutations are biologically relevant but should not be conflated with a germline diagnosis. [361][365]

No validated modifier gene or reproducible disease-specific epigenetic signature is known. No characteristic chromosomal rearrangement is required, although deletions encompassing *GNB1* occur within 1p36-deletion syndrome and may contribute to its neurodevelopmental and obesity phenotypes. [191]

---

## 5. Environmental and lifestyle information

No environmental, infectious or lifestyle factor is necessary or sufficient to cause *GNB1*-E. Prenatal toxin exposure, smoking, diet and occupational exposure have not been implicated. Environmental factors can nevertheless alter **complications**:

- Febrile illnesses may lower seizure threshold.
- Influenza A preceded acute encephalopathy in one reported child, but causality beyond physiologic stress cannot be established. [301]
- In reduced mobility, inadequate fiber/fluid and medication effects may worsen constipation.
- Excess food availability and weight-promoting medication may aggravate hyperphagia-associated obesity, especially in loss-of-function genotypes.
- Mast-cell triggers may worsen symptoms in patients with cutaneous mastocytosis.

No infectious agent, zoonotic transmission, or person-to-person transmission is involved.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous germline *GNB1* missense, splice, nonsense or frameshift variant leads to** altered quantity, folding or interaction surfaces of Gβ1.
2. **Altered Gβ1 leads to** variant-dependent failure or distortion of Gβγ dimer formation, Gαβγ assembly, GPCR activation/deactivation and effector coupling; splice/truncating variants can instead lead to haploinsufficiency.
3. **Abnormal Gβγ signaling leads to** dysregulation of neuronal GIRK/Kir3 potassium channels and potentially voltage-gated calcium channels, adenylyl cyclases, phospholipases, kinases and synaptic-release machinery.
4. **K78R-mediated GIRK overactivation leads to** excessive inhibition of selected inhibitory neurons—an interneuron-disinhibition mechanism that is partly inferred rather than fully demonstrated in humans—and results in network hyperexcitability and generalized seizures. [63][70]
5. **Branch A: GIRK gain or loss of function leads to** altered membrane excitability and thalamocortical/cortical synchronization, resulting in spike-wave discharges, epilepsy and possibly developmental interference.
6. **Branch B: defective G-protein assembly/signaling leads to** abnormal neural-progenitor proliferation, differentiation, cytoskeletal organization and embryonic neurogenesis; this is demonstrated in knockout mice and inferred for human structural brain abnormalities. [347]
7. **Branch C: altered signaling through AKT–mTOR–ERK/MAPK leads to** abnormal growth and cell-survival/proliferation programs; its role in human neurodevelopment is plausible, while direct evidence is strongest in mutant-cell and cancer models.
8. **Disrupted circuit development and neuronal excitability lead to** global developmental delay, intellectual disability, hypotonia evolving to spasticity/dystonia, impaired motor control and sensory/visual dysfunction.
9. **For truncating/splice genotypes, Gβ1 dosage reduction may lead to** hypothalamic leptin–melanocortin/energy-balance disruption and results in hyperphagia and obesity; this remains a 2024 clinical association rather than a fully demonstrated mechanism. [36]
10. **Rarely, infection, hypoxia or severe seizures may trigger** acute network/metabolic decompensation and result in encephalopathy, brain atrophy and permanent regression; susceptibility is suggested by two cases but not yet established. [301]

### Mechanistic evidence by level

| Evidence type | Finding |
|---|---|
| Human genetics | Strong enrichment of *de novo GNB1* variants: 13 variants among 5,855 undiagnosed individuals; chance probability \(p=7.1\times10^{-21}\). [191] |
| In-vitro BRET/assembly assays | Several missense variants disrupt Gβγ and Gαβγ assembly or dopamine-D1-receptor-driven activation. [68] |
| Electrophysiology | K78R, I80T and I80N profoundly alter GIRK regulation while not uniformly altering Gi/o coupling or CaV2.2 regulation. [482] |
| Knock-in mouse | *Gnb1* K78R/+ mice show developmental delay, motor/cognitive deficits, low seizure threshold and absence-like generalized seizures. [167][168] |
| Pharmacologic model | Ethosuximide inhibited aberrant GIRK activity, normalized neuronal bursting and suppressed spike-wave discharges in K78R mice; this is preclinical, not a human treatment trial. [234] |
| Knockout mouse | Homozygous loss causes impaired neural-progenitor proliferation, neural-tube defects in about 40%, microencephaly and neonatal lethality. [347] |
| Human obesity association | Obesity was strongly enriched among truncating/splice carriers, suggesting a dosage-sensitive hypothalamic mechanism. [36] |

### Suggested ontology annotations

| Domain | Suggested ontology terms |
|---|---|
| Biological process | GPCR signaling pathway **GO:0007186**; heterotrimeric G-protein signaling **GO:0007200**; regulation of membrane potential **GO:0042391**; potassium-ion transmembrane transport **GO:0071805**; neurogenesis **GO:0022008**; neural-progenitor proliferation **GO:0061351**; synaptic signaling **GO:0099536** |
| Molecular function | G-protein β-subunit activity; protein binding **GO:0005515**; GIRK-channel regulator activity |
| Cellular component | Heterotrimeric G-protein complex **GO:0005834**; plasma membrane **GO:0005886**; synapse **GO:0045202**; cytosol **GO:0005829** |
| Cell types | Neuron **CL:0000540**; neural progenitor cell **CL:0011020**; cortical neuron **CL:0002609**; GABAergic neuron **CL:0000617**; parvalbumin GABAergic interneuron; thalamic neuron |
| Pathways | Reactome Signaling by GPCR / GPCR downstream signaling; GIRK-channel signaling; PI3K–AKT–mTOR and MAPK/ERK as secondary or variant-dependent pathways |

No validated patient transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic or multi-omic diagnostic signature was available through the report date. Most molecular profiling has been experimental and variant-specific.

---

## 7. Anatomical structures affected

| Level | Structures and suggested ontology terms |
|---|---|
| Primary organ/system | Central nervous system; brain **UBERON:0000955**; nervous system **UBERON:0001016** |
| Cerebral cortex | Development, volume and network excitability; cerebral cortex **UBERON:0000956** |
| White matter/myelin | Delayed or abnormal myelination and periventricular white-matter changes; cerebral white matter **UBERON:0002437** |
| Corpus callosum | Hypoplasia/dysgenesis; corpus callosum **UBERON:0002336** |
| Basal ganglia | Dystonia and occasional caudate/globus-pallidus imaging abnormalities; globus pallidus **UBERON:0001875** |
| Thalamocortical circuits | Implicated in absence-like seizures in mice; thalamus **UBERON:0001897** |
| Cerebellum | Occasional cerebellar hypoplasia and dentate-nucleus abnormalities; cerebellum **UBERON:0002037** |
| Eye/visual pathways | Retina/optic nerve, ocular-motor system and visual cortex; eye **UBERON:0000970**, optic nerve **UBERON:0000966** |
| Skeletal muscle/motor apparatus | Secondary consequences of central hypotonia, spasticity and dystonia rather than primary myopathy |
| GI/GU/skin | GI tract, kidneys/urinary tract, testes and skin mast cells are variably affected |
| Subcellular | Plasma membrane, synaptic membrane, cytosol and heterotrimeric G-protein complexes; no primary mitochondrial, lysosomal or ER-storage lesion is established |

MRI abnormalities are generally bilateral/diffuse rather than consistently lateralized. Bilateral pallidal changes were described in the 2024 adult report. [286]

---

## 8. Temporal development and natural history

- **Onset:** Congenital or early infantile. Hypotonia, feeding difficulty, abnormal visual behavior, delayed milestones, infantile spasms or seizures may be the first manifestations.
- **Development:** Developmental delay becomes increasingly apparent over infancy and early childhood. Intellectual and communication disability is chronic and lifelong.
- **Motor course:** Hypotonia may remain stable or evolve into limb hypertonia, spasticity or dystonia. Dystonia can appear later, from approximately 2–16 years. [107]
- **Epilepsy:** Onset ranges from infancy to about 11 years. It may be episodic, controlled, or drug resistant; there is no single disease stage sequence. [128]
- **Imaging:** Some findings are congenital/developmental; rare patients have acquired atrophy after acute encephalopathy.
- **Obesity:** In loss-of-function cases, weight gain usually begins in childhood; median onset among six informative patients was 3.5 years. [36]
- **Duration/remission:** The genetic disorder is lifelong. Seizures or dystonia may improve with therapy, but there is no molecular remission.
- **Critical windows:** Early childhood is important for neurodevelopmental therapies, visual stimulation, communication support, feeding safety and seizure recognition.
- **Regression:** Not typical for most patients. Abrupt regression should prompt investigation for status epilepticus, infection, hypoxia, metabolic disturbance or acute encephalopathy rather than being assumed to be ordinary progression.

---

## 9. Inheritance and population

| Characteristic | Current understanding |
|---|---|
| Inheritance | Autosomal dominant |
| Typical origin | *De novo* heterozygous variant |
| Vertical transmission | Documented; transmission risk from an affected heterozygous parent is 50% per pregnancy |
| Penetrance | Appears high for developmental manifestations among clearly pathogenic variants, but precise penetrance is unknown |
| Expressivity | Highly variable, ranging from mild cognitive/movement phenotypes to profound nonverbal, nonambulatory developmental and epileptic encephalopathy |
| Mosaicism | Proband mosaicism can produce a milder phenotype; parental germline mosaicism remains a recurrence consideration |
| Anticipation | Not reported; no repeat-expansion mechanism |
| Consanguinity | Not etiologically relevant to the dominant disorder |
| Founder effects | None established |
| Carrier frequency | Not meaningfully defined for a highly penetrant, usually *de novo* dominant disorder |
| Sex ratio | In the 2024 compilation, 33/71 were female (46%), broadly consistent with no major sex bias. [36] |
| Age distribution | Mostly children and young adults; the 2024 compilation had median age 6 years, 10 adults and an oldest age of 40 years. [36] |
| Ethnic/geographic pattern | No population enrichment known |

### Epidemiology

No population-based prevalence or annual incidence estimate is available. Reports cited approximately **68 published cases** in early 2024, while a broader 2024 clinical/research summary stated that more than 73 people had been clinically identified. These counts measure ascertainment, not prevalence, and the true number is likely greater. [32][43] In early sequencing cohorts, pathogenic *GNB1* variants accounted for less than 0.5% of heterogeneous undiagnosed genetic cases. [188]

---

## 10. Diagnostics

### Diagnostic definition

The diagnosis is established by identification of a **heterozygous pathogenic or likely pathogenic *GNB1* variant** in a patient with compatible neurodevelopmental findings. Clinical findings alone are insufficiently specific. [80]

### Recommended testing pathway

1. **Phenotype and family history:** Developmental, neurologic, seizure, movement, vision, feeding, growth and three-generation pedigree assessment.
2. **First-line genomic testing:** Trio exome or genome sequencing is preferred where available; ACMG recommends ES/GS as a first- or second-tier test for pediatric developmental delay/intellectual disability. [241][246]
3. **Alternative:** A comprehensive developmental-delay/intellectual-disability, epilepsy or movement-disorder panel that includes *GNB1*.
4. **CMA:** Useful concurrently or when a copy-number disorder such as 1p36 deletion is suspected. It will not detect most single-nucleotide *GNB1* variants.
5. **Single-gene sequencing:** Appropriate when the phenotype or familial variant strongly points to *GNB1*; include deletion/duplication analysis if sequencing is negative.
6. **Parental testing:** Determine *de novo* status, segregation and possible mosaicism; deep sequencing may be appropriate when mosaicism is suspected.
7. **WGS:** Can detect coding, noncoding, structural and mosaic variation missed by standard WES, although disease-specific incremental yield is unknown.
8. **RNA sequencing:** Potentially useful to resolve splice variants, but not a routine diagnostic requirement.
9. **Not routinely indicated:** Karyotype/FISH unless a large rearrangement is suspected; mitochondrial-DNA or repeat-expansion testing only when the broader differential warrants it.

### Baseline clinical evaluation

| Domain | Recommended evaluation |
|---|---|
| Development | Formal cognitive, language, motor and adaptive assessment; assess need for AAC |
| Neurology | Examination for hypotonia, spasticity, dystonia, ataxia and other abnormal movements |
| Epilepsy | Awake and sleep EEG for suspicious events or subclinical seizures; prolonged EEG if needed |
| Imaging | Brain MRI, particularly with seizures, abnormal head growth, focal signs, regression or changing neurologic status |
| Feeding/GI | Nutrition and feeding assessment; swallow evaluation when coughing, aspiration or dysphagia is suspected |
| Vision/hearing | Ophthalmology and audiology |
| Musculoskeletal | PT/OT/rehabilitation and orthopedic assessment for tone, contractures, scoliosis and equipment |
| Cardiac | Echocardiogram at baseline where clinically indicated because occasional congenital heart defects have been reported |
| GU | Renal ultrasound; in males assess testes/cryptorchidism |
| Skin | Examine for mastocytosis; dermatology referral for compatible lesions |
| Endocrine/metabolic | Growth, BMI and thyroid testing; monitor glucose/lipids in obesity |
| Hematologic | GeneReviews suggests CBC surveillance because of rare leukemia reports, but the magnitude of germline malignancy risk is unknown. [436] |

### Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| *GNAO1*-related disorder | Often severe hyperkinetic movement crises and epilepsy; another G-protein-complex disorder |
| *GNAI1*-related NDD | Very similar DD/ID, hypotonia, epilepsy and behavioral phenotype; molecular testing is decisive |
| *GNA11*, *ADCY5*, *PDE10A* and other GPCR/cAMP disorders | Movement phenotype may predominate; gene-specific testing |
| Developmental and epileptic encephalopathies | *STXBP1, SCN2A, SCN8A, KCNQ2, KCNT1, HECW2, DDX3X,* etc.; broad panel/ES |
| Genetic cerebral-palsy mimics | Consider when spasticity/dystonia is attributed to perinatal injury but history or MRI is discordant; *GNB1* cases can resemble dyskinetic or spastic CP. [448] |
| 1p36 deletion syndrome | Larger chromosomal deletion detected by CMA; multisystem phenotype |
| Prader–Willi syndrome | Especially in hypotonia followed by hyperphagia/obesity; methylation testing distinguishes it |
| Rett/Angelman and mitochondrial/metabolic disorders | Regression, characteristic behavior, episodic metabolic decompensation or multisystem signs guide testing |

### Screening

There is no routine newborn or population carrier screening. Targeted familial testing, prenatal diagnosis and preimplantation genetic testing are possible once the familial variant is known.

---

## 11. Outcome and prognosis

- **Survival:** No valid 5-year, 10-year, overall-survival or disease-specific mortality rate exists.
- **Life expectancy:** Undetermined because most reported patients are children or young adults. Survival into the fourth decade is documented. [124][36]
- **Developmental outcome:** Usually persistent disability. More than half of one expanded cohort were nonverbal and nonambulatory, although milder independently mobile individuals occur. [106]
- **Epilepsy:** Variable; some patients respond to conventional treatment, while infantile-onset epilepsy can be refractory.
- **Movement disorder:** Dystonia may be stable or progressive and can become more disabling than epilepsy.
- **Acute deterioration:** Fever, respiratory arrest, refractory seizures or status epilepticus may rarely be followed by severe regression and cerebral atrophy. [301]
- **Major morbidity:** Communication impairment, mobility dependence, aspiration/poor nutrition, constipation/reflux, vision impairment, epilepsy, dystonia, contractures and obesity.
- **Malignancy:** Cutaneous mastocytosis has been reported in four patients and acute lymphoblastic leukemia in one. This is insufficient to quantify cancer penetrance; surveillance recommendations are precautionary. [304][314]
- **Prognostic indicators:** Severe early hypotonia, early/drug-resistant epilepsy, absent speech, nonambulation and acute encephalopathy plausibly predict greater disability. Mosaicism may predict a milder course; truncating/splice variants may predict obesity. No validated prognostic biomarker or calculator exists.
- **Recovery:** The genotype cannot be reversed with current care, but developmental skills, mobility, communication and seizure/movement control may improve with treatment. Recovery after catastrophic acute encephalopathy may be limited.

---

## 12. Treatment

There is **no approved disease-modifying therapy** or standardized *GNB1*-specific guideline. Care is multidisciplinary and manifestation-directed. [93]

| Manifestation/intervention | Evidence and practical use | Suggested NCIT intervention term |
|---|---|---|
| Early developmental intervention | Begin PT, OT, speech-language, feeding, visual and behavioral therapies promptly; individualized education and AAC are often needed. | Physical Therapy **NCIT:C15329**; Occupational Therapy; Speech Therapy |
| Epilepsy | Treat with standard antiseizure medications selected by seizure type and EEG. No ASM has proven disorder-specific superiority. | Anticonvulsant Agent **NCIT:C264** |
| Ethosuximide | Suppressed GIRK-related bursting and absence-like seizures in K78R mice; human efficacy and applicability to non-K78R variants are unknown. It should be used clinically only for an appropriate human seizure type, not solely because of genotype. [234] | Ethosuximide **NCIT:C617** |
| Feeding therapy | Clinical feeding assessment, swallow study, texture modification and nutrition support. | Nutritional Support; Feeding Therapy |
| Gastrostomy | Consider for persistent unsafe or inadequate oral feeding. | Gastrostomy **NCIT:C52003** |
| Spasticity | Stretching, positioning, orthoses, PT/OT; consider baclofen, botulinum toxin or other standard therapy based on distribution. | Baclofen; Botulinum Toxin; Rehabilitation |
| Dystonia | Individualized trials of anticholinergics such as trihexyphenidyl, baclofen, benzodiazepines, levodopa in selected cases, or VMAT2 inhibitors such as tetrabenazine. Evidence is anecdotal. | Anticholinergic Agent; Baclofen; Benzodiazepine; Tetrabenazine |
| Deep-brain stimulation | One patient with *GNB1*-related myoclonus-dystonia improved after pallidal DBS; consider only severe medication-refractory disease in an expert center. PMID:31034681. [481] | Deep Brain Stimulation **NCIT:C116551** |
| Intrathecal baclofen | Potential option for severe generalized spasticity/dystonia; disease-specific evidence is very limited. Oral baclofen caused drowsiness without benefit in the 2024 case. [226] | Intrathecal Baclofen Therapy |
| Vision/hearing support | Ophthalmologic treatment of strabismus/refractive problems, early visual stimulation, hearing aids where indicated. | Vision Rehabilitation; Hearing Aid |
| GI treatment | Standard constipation, reflux and cyclic-vomiting management. | Laxative; Proton Pump Inhibitor; Antiemetic |
| Mastocytosis | Avoid triggers; dermatology/allergy-directed H1 antihistamines and standard mast-cell management. | Histamine H1 Receptor Antagonist |
| Obesity/hyperphagia | Early dietetic support, structured food environment, activity adapted to disability, metabolic monitoring and avoidance of unnecessary weight-promoting drugs. No *GNB1*-specific anti-obesity drug trial exists. | Weight Management; Nutritional Counseling |
| Family support | Social work, respite, home nursing, palliative-care consultation when appropriate, and emergency seizure plans. | Supportive Care **NCIT:C15747** |

The complete GeneReviews treatment table likewise recommends standard ASMs, feeding therapy or gastrostomy, rehabilitation, vision/hearing support, constipation treatment, standard dystonia care and mastocytosis management. [92]

### Experimental treatments and trials

- **ClinicalTrials.gov:** No interventional, genotype-directed *GNB1*-E treatment trial was identified.  
- **NCT01793168:** Broad rare-disease patient registry/natural-history study that includes GNB1 syndrome; it is observational, not a therapeutic trial. [258]
- **Preclinical GIRK targeting:** Ethosuximide and future GIRK modulators are mechanistically interesting for K78R-like gain-of-function disease, but generalization to GIRK loss-of-function variants could be ineffective or harmful.
- **Gene therapy:** AAV-based silencing-plus-replacement work was reported in 2026 at the preclinical cell/mouse-validation stage, not in human trials. [261][266]
- **Cell, RNA, CRISPR or immunotherapy:** No clinical implementation is available.
- **Pharmacogenomics:** No CPIC or PharmGKB genotype-guided prescribing recommendation specific to germline *GNB1*-E.

---

## 13. Prevention

| Level | Measures |
|---|---|
| Primary prevention | The usually *de novo* variant cannot be prevented through lifestyle or vaccination. Genetic counseling, preimplantation testing and prenatal diagnosis can reduce recurrence or support reproductive decision-making after a familial variant is identified. |
| Secondary prevention | Prompt genomic diagnosis; early EEG when seizures are suspected; early developmental, feeding, vision and hearing assessment; monitor growth and BMI. |
| Tertiary prevention | Seizure action plan, aggressive treatment of status epilepticus, aspiration precautions, contracture prevention, safe mobility, constipation treatment, obesity prevention and mastocytosis-trigger avoidance. |
| Family planning | Test parents for the proband’s variant. If absent from blood, recurrence remains low but above background because of possible germline mosaicism. If a parent is heterozygous, recurrence is 50%. |
| Prenatal options | Targeted chorionic-villus or amniotic-fluid testing and preimplantation genetic testing are possible. Phenotype severity generally cannot be predicted reliably from a positive result. |
| Population screening | No newborn, universal carrier or public-health screening program is recommended. |
| Immunization | Routine vaccination is appropriate; there is no disease-specific vaccine. Fever plans should be individualized for children with fever-sensitive seizures. |

---

## 14. Other species and natural disease

| Species/model | Taxonomy/gene | Natural or comparative relevance |
|---|---|---|
| Human | *Homo sapiens*, Taxon 9606; *GNB1* Gene 2782 | Germline variants cause MRD42; somatic variants occur in cancer. |
| Mouse | *Mus musculus*, Taxon 10090; *Gnb1* Gene **14688**, MGI:95781 | Experimental knockout and K78R knock-in models; no equivalent naturally occurring clinical syndrome established. [318][326] |
| Zebrafish | *Danio rerio*, Taxon 7955; *gnb1a* Gene **322104**, ZFIN:ZDB-GENE-030131-823; *gnb1b* Gene **406796**, ZFIN:ZDB-GENE-040426-2855 | Conserved orthologs suitable for developmental and functional study; no established natural veterinary syndrome. [316][317] |
| Drosophila | *Drosophila melanogaster*, Taxon 7227; ortholog **Gβ13F** | Conserved Gβγ biology; not a validated patient-variant disease model in the core literature. |
| *C. elegans* | Taxon 6239; ortholog **gpb-1** | Comparative G-protein signaling; not a direct clinical model. |
| Dog | *Canis lupus familiaris*, Taxon 9615 | Somatic *GNB1* mutations occur in canine mast-cell tumors—14/81 or 17.3% in one study—but this is a cancer association, not a natural germline neurodevelopmental syndrome. PMID:31999054. [339] |

No breed-specific VBO-annotated natural counterpart of human germline *GNB1*-E was identified. There is no transmission or zoonotic potential.

---

## 15. Model organisms and experimental systems

| Model | Characteristics reproduced | Applications | Limitations/resources |
|---|---|---|---|
| *Gnb1* K78R/+ knock-in mouse | Developmental delay, impaired motor/cognitive performance, low electroconvulsive threshold and spontaneous absence-like generalized seizures. [167] | GIRK and thalamocortical mechanisms; EEG; preclinical antiseizure testing | Represents one gain-of-function missense variant and does not model all missense or haploinsufficient genotypes; MGI:95781 |
| K78R cultured cortical neurons | Abnormal network bursting and increased GIRK activation | Cellular electrophysiology and drug screening | Culture lacks full circuit and developmental context |
| Xenopus oocytes expressing mutant Gβ1 | Quantifies variant-specific GIRK currents and ethosuximide inhibition | Ion-channel mechanism and pharmacology | Heterologous overexpression; not a mammalian neuron |
| Homozygous *Gnb1* knockout mouse | About 40% neural-tube defects; impaired neural-progenitor proliferation, microencephaly and neonatal lethality. [347] | Role of Gβ1 in embryonic neurogenesis and cytoskeletal/ERK signaling | More severe than the usual heterozygous human disorder |
| BRET/BiFC cell systems | Gβγ dimerization, Gαβγ assembly and GPCR activation defects | Variant classification and mechanism | Tests selected pathways only; a normal result does not exclude disease |
| Patient-derived cells/neurons | Reported as part of preclinical gene-therapy development | Allele silencing, replacement and expression control | Published peer-reviewed disease-relevant outcome data remain limited |
| Zebrafish ortholog models | Potential rapid developmental and behavioral assays | High-throughput functional screening | Core validated human-variant phenotypes were not established in the cited literature by the report date |

---

## Recent developments and key primary literature

| Publication date | Study and evidence type | Key contribution | URL / identifier |
|---|---|---|---|
| 21 April 2016 | Petrovski et al.; human discovery cohort | Identified 13 *de novo* missense variants and defined the syndrome | PMID **27108799**; https://pubmed.ncbi.nlm.nih.gov/27108799/ [48] |
| 13 January 2017 online / 15 March 2017 issue | Lohmann et al.; human plus in-vitro functional assays | Demonstrated defective G-protein assembly and signaling | PMID **28087732**; https://pubmed.ncbi.nlm.nih.gov/28087732/ [483] |
| 8 September 2018 online | Hemati et al.; 18 new patients plus review | Expanded phenotype, mosaicism and Ile80 genotype–phenotype correlation | PMID **30194818**; https://pubmed.ncbi.nlm.nih.gov/30194818/ [106][123] |
| 12 September 2020 | Fukuda et al.; human plus functional assays | Established truncating/splice loss-of-function and haploinsufficiency | PMID **32918542**; https://pmc.ncbi.nlm.nih.gov/articles/PMC7667315/ [370] |
| 21 August 2021 | Reddy et al.; electrophysiology and computational work | Showed variant-specific GIRK dysregulation | PMID **34522861**; https://pubmed.ncbi.nlm.nih.gov/34522861/ [482] |
| 9 November 2022 | Sensory regulation study; K78R mouse | Identified thalamic/sensory modulation of frequent spike-wave discharges | PMID **36405774**; https://pmc.ncbi.nlm.nih.gov/articles/PMC9667301/ [345] |
| 18 May 2023 | Mouse/neuronal study | Ethosuximide suppressed GIRK-related bursting and generalized seizures | PMID **37275776**; https://pubmed.ncbi.nlm.nih.gov/37275776/ [38][234] |
| 13 July 2023 online | Tsuji et al.; two human cases | Reported acute encephalopathy, regression and acquired cerebral atrophy | PMID **37453880**; https://pubmed.ncbi.nlm.nih.gov/37453880/ [301] |
| 30 November 2023 | Wagnon expert commentary | Interpreted GIRK signaling as a major mechanistic axis while noting complexity | PMID **38269351**; https://pubmed.ncbi.nlm.nih.gov/38269351/ [33] |
| 1 April 2024 | Žutautas et al.; adult case and review | Adult dystonia/nystagmus phenotype, diagnostic and treatment synthesis | PMID **38674235**; https://pubmed.ncbi.nlm.nih.gov/38674235/ [32] |
| 10 April 2024 | Kleinendorst et al.; three cases plus 68-case review | Linked truncating/splice variants with hyperphagia and syndromic obesity | PMID **38596856**; https://pubmed.ncbi.nlm.nih.gov/38596856/ [36] |

### Exact abstract quotations supporting central claims

> “Whole-exome sequencing of 13 individuals with developmental delay commonly accompanied by abnormal muscle tone and seizures identified de novo missense mutations enriched within a sub-region of *GNB1*.” — Petrovski et al., 2016, PMID:27108799. [48]

> “Consistent with previous reports, developmental delay in these patients was moderate to severe, and more than half of the patients were non-ambulatory and nonverbal.” — Hemati et al., 2018, PMID:30194818. [106]

> “Here, we show that mice carrying a pathogenic mutation, K78R, recapitulate aspects of the disorder, including developmental delay and generalized seizures.” — 2023 K78R mouse study, PMID:37275776. [63]

> “Of the 42 patients whose weight status we could determine, obesity was present in 8 patients (19%). Obesity is significantly over-represented in the group with truncating and splicing variants.” — Kleinendorst et al., published 10 April 2024, PMID:38596856. [36]

## Overall knowledge-base conclusion

*GNB1*-E is a **definitively established, autosomal-dominant developmental encephalopathy** with broad expressivity. The most defensible upstream mechanism is variant-dependent disruption of Gβ1-containing heterotrimeric G-protein signaling. GIRK-channel dysregulation now provides a strong mechanistic bridge from selected variants—especially K78R—to neuronal network hyperexcitability, while G-protein assembly failure and haploinsufficiency explain other genotypes. The most important 2023–2024 advances were the demonstration of GIRK-targetable epilepsy in a mouse model, recognition of rare acute encephalopathic deterioration, and identification of a probable truncating/splice-variant obesity phenotype. Clinical implementation remains genomic diagnosis, anticipatory surveillance and individualized multidisciplinary supportive care; precision therapy is still preclinical.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 82 |
| Resolved | 77 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014855` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **intellectual disability, autosomal dominant 42**
- `DOID:0070072` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **autosomal dominant intellectual developmental disorder 42**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0002609` (obsolete neuron of cerebral cortex) (1 mention) - replaced by `CL:0010012`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014855` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `MGI`.
