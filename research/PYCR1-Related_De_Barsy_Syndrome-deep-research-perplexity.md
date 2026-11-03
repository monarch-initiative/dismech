---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-18T05:41:23.963306'
end_time: '2026-10-18T05:45:09.942851'
duration_seconds: 225.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PYCR1-Related De Barsy Syndrome
  mondo_id: MONDO:0013755
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
citation_count: 54
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 63
  verified: 58
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0006561
    ontology_label: obsolete proline biosynthetic process
    replaced_by: GO:0055129
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
- **Disease Name:** PYCR1-Related De Barsy Syndrome
- **MONDO ID:** MONDO:0013755 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PYCR1-Related De Barsy Syndrome** covering all of the
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

# PYCR1-Related De Barsy Syndrome  
**Disease-characteristics research report — evidence reviewed through 18 October 2026**

## Executive summary

**PYCR1-related De Barsy syndrome** is the severe end of the phenotypic spectrum of **biallelic PYCR1-related autosomal-recessive cutis laxa**, historically called **autosomal-recessive cutis laxa type IIIB (ARCL3B)**. Core manifestations are congenital loose, thin, translucent or wrinkled skin; a triangular/progeroid facial appearance; pre- and postnatal growth deficiency; hypotonia and developmental delay; joint laxity or contractures; osteopenia; and variably cataract, corneal clouding, movement disorder, seizures, or corpus-callosum abnormalities. The boundary between ARCL2B and ARCL3B is not biologically sharp: many authorities now treat them as one **PYCR1-related ARCL spectrum**, reserving “De Barsy syndrome” for severe cases, particularly those with ocular and neurologic involvement. [4][38][61]

The disease is caused by **germline biallelic loss-of-function or function-reducing variants in PYCR1**, encoding mitochondrial pyrroline-5-carboxylate reductase 1. PYCR1 catalyzes the final NAD(P)H-dependent step of de novo proline synthesis. Patient fibroblasts exhibit altered mitochondrial morphology, reduced membrane potential, and increased oxidative-stress-induced apoptosis; vertebrate models show dermal or epidermal abnormalities and apoptosis. These findings support a mechanism combining disturbed proline/redox metabolism, mitochondrial stress, loss of connective-tissue cells, and impaired extracellular-matrix maintenance. [17][19][33]

There is **no disease-modifying therapy** and no validated drug, gene, RNA, or cell therapy. Care is multidisciplinary and symptomatic. Amino-acid supplementation has only case-report-level evidence, without established clinical benefit. [172][175]

---

# 1. Disease information

## 1.1 Definition and scope

PYCR1-related De Barsy syndrome is a congenital Mendelian neurocutaneous and connective-tissue disorder caused by biallelic pathogenic variants in **PYCR1**. It belongs to the mitochondrial proline-synthesis disorders and the autosomal-recessive cutis laxa group. The classic De Barsy phenotype comprises progeroid facies, cutis laxa, growth restriction, intellectual/developmental disability, movement abnormalities, and ocular opacities. [35][39]

A major nosologic issue is that identical or overlapping PYCR1 genotypes have been diagnosed as:

- De Barsy syndrome;
- ARCL type 2B;
- ARCL type 3B;
- wrinkly-skin syndrome;
- geroderma osteodysplasticum-like disease; or
- a nonspecific progeroid cutis laxa syndrome.

A 2013 cohort included **33 individuals from 27 families** whose original diagnoses spanned those categories, supporting one continuous PYCR1-related spectrum rather than sharply distinct disorders. [106]

## 1.2 Identifiers

| Resource | Identifier/name | Qualification |
|---|---|---|
| MONDO | **MONDO:0013755**, PYCR1-related De Barsy syndrome | Target concept |
| OMIM disease | **614438**, Cutis laxa, autosomal recessive, type IIIB | De Barsy/ARCL3B |
| OMIM overlapping disease | **612940**, Cutis laxa, autosomal recessive, type IIB | Same PYCR1 spectrum, generally less severe |
| OMIM gene | **179035**, PYCR1 | Gene entry |
| Orphanet | **ORPHA:293633**, PYCR1-related De Barsy syndrome | Gene-defined subtype |
| Broader Orphanet concept | **ORPHA:2962**, De Barsy syndrome | Includes genetically heterogeneous DBS |
| MeSH | **C535990**, De Barsy syndrome | Supplementary concept |
| SNOMED CT | **1295488006** | PYCR1-related De Barsy syndrome / ARCL3B |
| MedGen | **C3280799** | PYCR1-related De Barsy syndrome |
| ICD-10 | **Q87.0** in current Orphanet/SNOMED mapping | Congenital malformation syndromes predominantly affecting facial appearance |
| ICD-11 | **LD28.2** | Syndromes with multiple structural anomalies, not elsewhere classified |

The ICD mappings are not disease-specific and vary among legacy resources: older documents also use Q87.7 or Q87.8. The curated Orphanet listing currently supplies Q87.0 and ICD-11 LD28.2. [1][2][152][153][155]

## 1.3 Synonyms

Common names include:

- PYCR1-related De Barsy syndrome;
- De Barsy syndrome B;
- autosomal-recessive cutis laxa type IIIB / ARCL3B;
- PYCR1 deficiency;
- pyrroline-5-carboxylate reductase 1 deficiency;
- cutis laxa–corneal clouding–intellectual disability syndrome;
- progeroid syndrome of De Barsy;
- De Barsy–Moens–Dierckx syndrome.

**Related but not completely interchangeable:** PYCR1-related ARCL2B, wrinkly-skin syndrome, and geroderma osteodysplasticum-like phenotype. [151][153][163]

## 1.4 Evidence granularity

This report is an **aggregated disease-level synthesis**, not an EHR-derived individual-patient record. Evidence includes:

- small human case series and case reports;
- the 33-person genotype–phenotype cohort;
- curated resources such as OMIM, Orphanet, ClinVar and GeneReviews;
- patient-derived fibroblast and transfected-cell experiments;
- zebrafish, Xenopus and mouse models.

Only **114 individuals with biallelic PYCR1 variants** had been collated in the 2026 GeneReviews synthesis; therefore, frequency estimates remain vulnerable to referral, ascertainment and publication bias. [61]

---

# 2. Etiology

## 2.1 Causal factor

The primary cause is **biallelic germline pathogenic or likely pathogenic PYCR1 variation**, inherited in an autosomal-recessive manner. The established molecular mechanism is predominantly **loss of function**, including absent protein after truncating variants and instability or reduced catalytic activity from missense variants. The gene–disease relationship is classified as definitive. [41][79][222]

No infectious, toxic, nutritional or lifestyle cause has been demonstrated.

## 2.2 Genetic risk factors

Disease risk requires two affected alleles, typically:

- homozygosity for one pathogenic allele, often in consanguineous families;
- compound heterozygosity for two pathogenic alleles;
- rarely, a whole-gene or intragenic deletion paired with another pathogenic allele.

Reported variant classes include missense, nonsense, frameshift, canonical splice-site, small insertion/deletion and whole-gene deletion variants. Most variants in the 2013 cohort clustered in exons 4–6; missense substitutions of conserved residues were most frequent, followed by splice variants and a nonsense variant. [106]

Representative variants—not a complete ClinVar catalogue—include:

| Variant, transcript NM_006907.4 | Type | Evidence/status |
|---|---|---|
| c.356G>A, p.Arg119His | Missense | ClinVar pathogenic |
| c.355C>G, p.Arg119Gly | Missense | Pathogenic; foundational reports |
| c.616G>T, p.Gly206Trp | Missense | ClinVar pathogenic |
| c.797G>A, p.Arg266Gln | Missense | Pathogenic; reported in two French-Acadian Canadian families |
| c.540+1G>T | Canonical splice | ClinVar likely pathogenic |
| c.11del, p.Gly4fs | Frameshift | Pathogenic |
| c.345del, p.Arg116fs / historically p.Pro115fsTer7 | Frameshift | De Barsy case; germline |
| c.743G>A, p.Gly248Glu | Missense | De Barsy case, in trans with frameshift |
| c.559G>A, p.Ala187Thr | Missense | Homozygous 2024 case; absent from gnomAD/1000 Genomes/dbSNP in that report; reduced protein and enzymatic activity |

[81][85][197][200][202]

The 2024 p.Ala187Thr study measured activity of **8.12±0.64 nmol/min/mg** in mutant cells versus **17.78±0.62** in wild-type cells, *P*<0.01, providing functional evidence of impaired enzyme activity (PMID **39172257**, published 22 August 2024). [33]

## 2.3 Susceptibility and modifier factors

- **Consanguinity** increases the probability that both parents carry the same rare pathogenic allele; it does not alter the molecular mechanism.
- A French-Acadian founder context has been reported for p.Arg266Gln in Maritime Canadian families, but no global founder mutation dominates.
- Variants in the first coding exon or first two exons have been associated with lower average severity and absent or mild intellectual disability, possibly because of alternative translation or residual function.
- Whole-gene deletion has been reported with the cutis-laxa phenotype but without intellectual disability, emphasizing imperfect genotype–phenotype correlation. [61][106][213]

No validated modifier gene, protective allele, polygenic-risk score, anticipation phenomenon or established germline-mosaicism rate is known.

## 2.4 Environmental and protective factors

No environmental exposure has been shown to cause or prevent the disorder. Oxidative stress is mechanistically relevant at the cellular level: PYCR1-deficient fibroblasts are unusually vulnerable to hydrogen peroxide and related oxidative challenges. This does **not** establish ordinary environmental oxidants as epidemiologic causes. Avoidance of smoking, excessive ultraviolet exposure, prolonged fasting and unnecessary high-injury activities is precautionary rather than primary prevention. [19][61]

There is no demonstrated protective diet or supplement. Proline, citrulline, arginine, antioxidant or vitamin-C therapy remains unproven.

---

# 3. Phenotypes

## 3.1 Frequency caveat

The best consolidated percentages encompass mitochondrial proline-synthesis disorders collectively, not exclusively molecularly confirmed ARCL3B. They are therefore useful estimates but should not be treated as precise PYCR1-specific penetrance figures. [61]

## 3.2 Core phenotype matrix

| Phenotype and suggested HPO term | Type | Onset/course | Approximate frequency or strength of association | Functional/QOL impact |
|---|---|---|---|---|
| Cutis laxa — **HP:0000973** | Physical sign | Congenital; wrinkles may lessen with age while translucency/lipoatrophy becomes more evident | 100% in pooled proline-synthesis cohort | Cosmetic difference, bruising/wound and pressure-injury concerns |
| Thin/translucent skin — **HP:0000963** | Sign | Congenital/lifelong | 90% pooled | Visible veins, skin fragility |
| Progeroid appearance — **HP:0007495** | Sign | Congenital/early childhood | Dysmorphic/progeroid features 95% pooled | Psychosocial and cosmetic impact |
| Triangular face — **HP:0000325** | Sign | Congenital; pointed chin becomes more evident with age | Characteristic | Diagnostic clue |
| Intrauterine growth restriction — **HP:0001511** | Sign | Prenatal | 96% pooled | Low birth weight/length |
| Postnatal growth retardation — **HP:0008897** | Sign | Infancy/childhood; may improve somewhat | 85% pooled | Nutritional and mobility effects |
| Microcephaly — **HP:0000252** | Sign | Congenital or progressive relative microcephaly | 68% pooled; generally mild in PYCR1 | Correlates variably with neurodevelopment |
| Global developmental delay — **HP:0001263** | Neurodevelopmental | Infancy; chronic, usually non-regressive | 98% pooled; usually milder in PYCR1 than ALDH18A1-ARCL | Major educational, communication and self-care burden |
| Intellectual disability — **HP:0001249** | Behavioral/cognitive | Childhood | Variable, mild to severe | Lifelong assistance may be needed |
| Hypotonia — **HP:0001252** | Sign | Often congenital | 93% pooled; moderate truncal hypotonia in PYCR1 | Delayed sitting/walking, feeding problems |
| Hyperreflexia — **HP:0001347** / lower-limb spasticity — **HP:0002061** | Sign | May emerge/progress | Mild peripheral spasticity in PYCR1 | Gait and contracture burden |
| Athetoid/dystonic movements — **HP:0002305/HP:0001332** | Sign | Childhood; variable | Athetoid movement 26% pooled; uncommon but predictive | Impairs motor control |
| Seizures — **HP:0001250** | Sign | Variable pediatric onset | Occasional in PYCR1 ARCL | Safety and medication burden |
| Corpus-callosum dysgenesis — **HP:0001273** | Imaging abnormality | Congenital | 55% pooled, but mild/variable in PYCR1 | Variable developmental significance |
| Joint hypermobility — **HP:0001382** | Sign | Congenital | 98% pooled | Instability, delayed motor skills |
| Adducted thumb — **HP:0001181** / contractures — **HP:0001371** | Sign | Congenital | Adducted thumbs/clubfoot 67% pooled | Hand function and mobility limitations |
| Congenital hip dislocation — **HP:0001374** | Sign | Congenital | 53% pooled | Orthopedic treatment/surgery |
| Osteopenia — **HP:0000938** | Imaging/sign | Childhood onward | 74% pooled | Fracture risk, though spontaneous fractures are uncommon |
| Wormian bones — **HP:0002645** | Imaging sign | Congenital/childhood | 49% pooled | Usually diagnostic rather than symptomatic |
| Large/delayed-closing fontanel — **HP:0000239/HP:0001476** | Sign | Infancy | 37% pooled | Monitoring/protection |
| Hernia — **HP:0000023**, **HP:0001537** | Sign | Congenital/childhood | 46% pooled | Possible surgical correction |
| Cataract — **HP:0000518** | Ocular sign | Congenital or early childhood | 58% pooled; generally mild/less frequent in PYCR1 | Visual impairment |
| Strabismus — **HP:0000486** | Ocular sign | Childhood | 40% pooled | Amblyopia risk |
| Blue sclerae — **HP:0000592** | Sign | Congenital | 35% pooled | Usually limited direct impairment |
| Corneal opacity/clouding — **HP:0007957** | Ocular sign | May be congenital | 20% pooled; less frequent in PYCR1 than ALDH18A1 disease | Potential severe visual loss |
| Sparse hair — **HP:0008070** | Sign | Early childhood | Recurrent, exact PYCR1 frequency unavailable | Cosmetic impact |
| Feeding difficulty — **HP:0011968** | Symptom | Infancy | Recurrent, unquantified | Malnutrition/poor growth |
| Cryptorchidism — **HP:0000028** | Sign | Congenital, males | Occasional | Surgical/endocrine implications |

Frequencies and course derive from the 2026 aggregate synthesis and must be applied cautiously to PYCR1-related De Barsy syndrome. [61]

### Important natural-history points

- Skin wrinkling is present at birth but may become less conspicuous with age.
- Thin/translucent skin and reduced subcutaneous fat may become more conspicuous.
- Motor and speech delay vary from mild to profound, but **neurodevelopmental regression has not been a characteristic finding**.
- Growth deficiency may partially improve with age.
- Brain MRI can be normal despite profound developmental disability. [61][66]

In a 2024 Chinese child homozygous for p.Ala187Thr, birth weight was **1,400 g**; at 33 months he could not sit or hold an object independently, and his estimated developmental age was **1.5 months**, despite a normal MRI. This demonstrates the severe end of expressivity but is a single case, not a typical outcome (PMID **39172257**). [33]

## 3.3 Quality of life

No disease-specific EQ-5D, SF-36, PROMIS or validated caregiver-burden studies were located. Anticipated major burdens arise from developmental disability, impaired mobility, feeding problems, visual impairment, seizures, orthopedic deformity and need for long-term therapies. Cosmetic differences and the “prematurely aged” appearance may also affect psychosocial well-being. These impacts are clinically plausible but not quantified by formal PYCR1-specific quality-of-life research.

---

# 4. Genetic and molecular information

## 4.1 Gene and protein

| Attribute | Value |
|---|---|
| Gene | **PYCR1**, pyrroline-5-carboxylate reductase 1 |
| HGNC | **HGNC:9721** |
| NCBI Gene | **5831** |
| OMIM gene | **179035** |
| Ensembl | **ENSG00000183010** |
| Chromosomal locus | **17q25.3** |
| UniProt | **P32322** |
| Protein | Mitochondrial pyrroline-5-carboxylate reductase 1 |
| Approximate protein size | 319 amino acids, 33.4 kDa |
| Normal reaction | P5C + NAD(P)H → L-proline + NAD(P)+ |
| Main localization | Mitochondrion, especially mitochondrial matrix |
| Oligomeric state | Homopolymeric enzyme |

[91][94][95]

## 4.2 Variant interpretation

- Disease-associated variants are **germline**, not somatic.
- Classification should use ACMG/AMP criteria and current ClinVar evidence.
- A VUS, or one pathogenic variant plus one VUS, does not establish the diagnosis.
- Population frequency must be checked per variant in gnomAD; causal alleles are generally absent or exceptionally rare. No single global disease-allele frequency or reliable carrier-frequency estimate is available.
- The principal mechanism is **loss of function or reduced function**, not established gain of function or dominant-negative action. [61][222]

The p.Ala187Thr allele illustrates a function-reducing missense mechanism: altered hydrogen-bonding was predicted, exogenous protein abundance was reduced, and catalytic activity fell by approximately 54% in transfected HEK293T cells. [33]

## 4.3 Modifier, epigenetic and structural-genomic evidence

- No validated modifier genes have been established.
- No disease-specific DNA-methylation signature, histone alteration or chromatin biomarker has been validated.
- Large chromosomal abnormalities are not typical; rare intragenic or whole-gene deletions may occur.
- CMA can detect a sufficiently large deletion but is not a first-line standalone test.
- There is no recurrent aneuploidy, translocation or inversion defining the disease.

---

# 5. Environmental information

There are no causal toxins, occupational exposures, pollutants, infections, smoking patterns, alcohol exposures or exercise behaviors known to produce PYCR1-related De Barsy syndrome.

Potentially relevant modifiers are largely precautionary:

- smoking may accelerate general elastic-fiber damage;
- excessive sun exposure may aggravate cutis-laxa skin;
- prolonged fasting may be undesirable in a mitochondrial/metabolic disorder;
- contact sports may increase injury risk in persons with joint laxity, osteopenia or cervical instability.

These recommendations are extrapolations from phenotype and mechanism, not proven gene–environment interactions. [61]

No bacterium, virus, fungus or parasite causes or transmits the disease; it is not contagious or zoonotic.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Biallelic pathogenic PYCR1 variants lead to** absent, unstable, misfolded or catalytically impaired mitochondrial PYCR1 protein.  
2. **Reduced PYCR1 activity leads to** impaired conversion of Δ¹-pyrroline-5-carboxylate to L-proline and reduced oxidation of NAD(P)H to NAD(P)+.  
3. **This metabolic/redox disturbance leads to** altered mitochondrial morphology and reduced mitochondrial membrane potential; a direct causal sequence is supported in patient fibroblasts, although the relative contribution of proline shortage versus redox imbalance remains unresolved.  
4. **Mitochondrial dysfunction leads to** increased susceptibility to oxidative-stress-induced apoptosis.  
5. **Increased apoptosis and impaired survival of dermal/connective-tissue cells lead to** dermal thinning and defective maintenance of collagen- and elastin-rich extracellular matrix; the precise collagen/elastin biochemical linkage is partly inferred.  
6. **Dermal and extracellular-matrix loss results in** thin, translucent, lax and wrinkled skin, visible veins, reduced subcutaneous tissue and progeroid appearance.  
7. **The same proline/redox and cell-survival disturbance in bone, cartilage and periarticular connective tissue leads to** osteopenia, delayed fontanel closure, Wormian bones, joint laxity, hip dislocation and contractures; parts of this tissue-level sequence remain inferred.  
8. **Branch A—neural development:** mitochondrial stress and increased vulnerability of neural cells lead to, or are inferred to contribute to, hypotonia, developmental disability, movement abnormalities, seizures and variable corpus-callosum/gyral abnormalities.  
9. **Branch B—ocular connective tissue:** impaired development or maintenance of corneal and lens structures leads to cataract, corneal clouding, blue sclerae and visual impairment.  
10. **Combined skin, skeletal, neurologic and ocular abnormalities result in** the recognizable PYCR1-related De Barsy/ARCL phenotype.

The foundational human-cell and vertebrate study stated directly: **“Altered mitochondrial morphology, membrane potential and increased apoptosis rate upon oxidative stress were evident in fibroblasts from affected individuals.”** It further reported that PYCR1 knockdown in zebrafish and Xenopus caused epidermal hypoplasia, blistering and markedly increased apoptosis (PMID **19648921**, published online 2 August 2009). [17][107]

## 6.2 Pathway and biochemical detail

PYCR1 is downstream of **ALDH18A1/P5CS** in mitochondrial de novo proline synthesis:

**Glutamate → glutamate semialdehyde/P5C → L-proline**

PYCR1 catalyzes the second step and consumes NADH or NADPH. Suggested annotations include:

- **GO:0006561** — proline biosynthetic process;
- **GO:0004657** — pyrroline-5-carboxylate reductase activity;
- **GO:0005739** — mitochondrion;
- **GO:0005759** — mitochondrial matrix;
- **GO:0034599** — cellular response to oxidative stress;
- **GO:0008631** — intrinsic apoptotic signaling in response to oxidative stress;
- **GO:0043066** — negative regulation of apoptotic process;
- **GO:0043062** — extracellular structure organization;
- **GO:0030199** — collagen fibril organization.

The affected metabolites/substrates include L-proline (**CHEBI:17203**), Δ¹-pyrroline-5-carboxylate, NADH, NADPH, NAD+ and NADP+. [91][105]

Plasma or urine proline, ornithine, citrulline and arginine may be low, but normal values are common. Thus amino-acid analysis is supportive, not diagnostic. [61][218]

## 6.3 Cellular and tissue mechanisms

**Demonstrated in human fibroblasts:**

- fragmented/altered mitochondrial network;
- reduced mitochondrial membrane potential;
- increased apoptosis after oxidative stress;
- reduced PYCR1 enzyme activity for at least some missense variants.

**Supported or inferred at tissue level:**

- reduced dermal thickness;
- reduced or fragmented elastic fibers;
- disturbed extracellular-matrix organization;
- reduced collagen abundance in experimental models.

Neurometabolic cutis-laxa biopsies have shown decreased, irregular, short, thick and fragmented elastic fibers and generalized ECM disorganization, although these findings are not unique to PYCR1 deficiency. [184]

Suggested cell types:

- dermal fibroblast — **CL:0000057**;
- keratinocyte — **CL:0000312**;
- neuron — **CL:0000540**;
- oligodendrocyte — **CL:0000128**, only indirectly implicated;
- osteoblast — **CL:0000062**;
- chondrocyte — **CL:0000138**;
- lens epithelial cell and corneal stromal keratocyte, appropriate ocular cell concepts where available.

## 6.4 Immune and epigenetic mechanisms

No primary immunodeficiency, autoimmunity or disease-driving inflammatory pathway is established. Secondary inflammatory responses to tissue stress have not been sufficiently characterized.

No reproducible disease-specific epigenomic, single-cell, spatial-transcriptomic, proteomic, lipidomic or multi-omic signature has entered clinical use. Much PYCR1 omics work concerns cancer metabolism and should not be extrapolated to congenital PYCR1 loss-of-function disease.

## 6.5 Recent mechanistic research, 2023–2024

A 2023 study/preprint reported five pathogenic PYCR1 alleles and a constitutive **Pycr1-null mouse**. Mutant mice had dermal thinning and fewer collagen fibers but relatively normal overall development, apparently because mouse **Pycr2** can compensate more effectively than human PYCR2 in cutaneous fibroblasts. The authors proposed that a Pycr1/Pycr2 double knockout may better reproduce the full human phenotype. [124][126]

The 2024 p.Ala187Thr study provided variant-specific evidence of reduced protein expression and enzyme activity and quantitatively documented an extremely severe developmental trajectory (PMID **39172257**). Its abstract concludes: **“Our findings confirmed abnormal enzymatic activity and neurodevelopmental trajectory of this PYCR1 mutation.”** [33]

---

# 7. Anatomical structures affected

| Level | Structure/system | Suggested ontology annotation |
|---|---|---|
| Organ | Skin, especially hands, feet, face, trunk and extremities | **UBERON:0002097**, skin of body |
| Tissue | Dermis, subcutaneous tissue, elastic-fiber/collagen ECM | **UBERON:0002067**, dermis; adipose tissue concepts |
| Skeleton | Skull/fontanelles, hips, vertebral column, hands and feet | UBERON skull, hip joint, vertebral column |
| Nervous system | Brain, corpus callosum, corticospinal/motor system | **UBERON:0000955**, brain; **UBERON:0002336**, corpus callosum |
| Eye | Cornea, lens and sclera | **UBERON:0000964**, cornea; **UBERON:0000965**, lens; **UBERON:0001775**, sclera |
| Cardiovascular | Usually not primary; occasional aortic-root dilation or other findings require individual evaluation | Heart/aorta terms |
| Subcellular | Mitochondrion/mitochondrial matrix | **GO:0005739**, **GO:0005759** |
| Molecular structure | Collagen- and elastin-containing extracellular matrix | **GO:0031012**, extracellular matrix |

Disease distribution is generally bilateral and systemic; no consistent lateralization is known. A unilateral manifestation such as isolated limb anomaly should be recorded separately rather than treated as characteristic.

---

# 8. Temporal development

## 8.1 Onset

- **Prenatal:** intrauterine growth restriction is common.
- **Congenital/neonatal:** cutis laxa, wrinkled skin, low weight/length, hypotonia, large fontanel, hip dislocation, adducted thumbs or clubfoot may be apparent.
- **Infancy:** feeding difficulty, poor growth and developmental delay become evident.
- **Childhood:** speech/motor disability, movement disorder, spasticity, scoliosis, osteopenia, cataract or corneal clouding may become clearer.

The onset is developmental and chronic rather than acute or episodic. [61]

## 8.2 Course

There is no formal staging system. A practical course model is:

1. **Prenatal/neonatal phase:** growth restriction and congenital connective-tissue phenotype.
2. **Infancy/early childhood:** emerging neurodevelopmental and feeding problems.
3. **Later childhood/adolescence:** orthopedic complications, mobility limitations and ocular disease may dominate.
4. **Adulthood:** data are sparse; disease is lifelong, with some skin wrinkling and growth parameters becoming less striking.

Regression and spontaneous remission are not typical. Skin appearance changes with age, but the genetic disease does not resolve. No critical therapeutic window has been established, although early visual, developmental, nutritional and orthopedic intervention is clinically important.

---

# 9. Inheritance and population

## 9.1 Inheritance

- **Mode:** autosomal recessive — **HP:0000007**.
- If both parents are heterozygous, each pregnancy has a **25% affected, 50% carrier and 25% non-carrier/unaffected** probability.
- Heterozygous carriers are generally asymptomatic.
- Penetrance for convincingly pathogenic biallelic genotypes appears high, but formal age-specific estimates are unavailable.
- Expressivity is markedly variable.
- Genetic anticipation is not expected.
- Parental mosaicism, uniparental isodisomy or a hidden deletion can theoretically explain unusual segregation, but no disease-specific mosaicism frequency is known. [61]

## 9.2 Epidemiology

- Estimated prevalence: **unknown, probably below 1 per 1,000,000**.
- Incidence per 100,000 person-years: not established.
- Reported molecularly confirmed PYCR1 cases collated by 2026: **114**.
- No consistent sex bias is expected for an autosomal-recessive condition.
- Cases occur worldwide, with no established ethnic preponderance.
- Consanguinity is common in published families because it increases homozygosity for rare alleles, but affected children also occur in non-consanguineous families.
- Reliable global carrier frequency is unavailable. [61]

A French-Acadian cluster involving p.Arg266Gln is evidence of a local founder effect, not globally elevated prevalence. [213]

---

# 10. Diagnostics

## 10.1 Diagnostic approach

Diagnosis requires compatible clinical findings plus **biallelic pathogenic or likely pathogenic PYCR1 variants in trans**.

### Recommended workflow

1. Recognize congenital cutis laxa/progeroid facies with growth and neurodevelopmental abnormalities.
2. Obtain serum and urine amino-acid profiles, while recognizing that results may be normal.
3. Perform a cutis-laxa/connective-tissue/neurodevelopmental multigene panel or trio exome/genome sequencing.
4. Confirm variants and parental phase by Sanger or equivalent testing.
5. Add exon-level deletion/duplication analysis if sequencing identifies only one allele.
6. Undertake phenotype-directed baseline investigations.

Sequence analysis is estimated to detect about **98%** of known PYCR1 pathogenic variants, with deletion/duplication analysis contributing approximately **2%**. PYCR1 accounts for about **80.5%** of reported mitochondrial proline-synthesis neurocutaneous disorders, not 80.5% of all cutis laxa. [61]

## 10.2 Clinical tests

| Test | Purpose/findings |
|---|---|
| Physical and dermatologic examination | Distribution and severity of cutis laxa, translucency, bruising and pressure-injury risk |
| Growth measurements | Weight, length/height and head circumference |
| Serum/urine amino acids | Proline, ornithine, citrulline and arginine may be low or normal |
| Developmental/neuropsychological assessment | Quantifies motor, language, adaptive and cognitive impairment |
| Brain MRI | May show thin/dysgenetic corpus callosum, cerebral atrophy or abnormal gyration; may be normal |
| EEG | If seizures or suspicious events occur |
| Hip ultrasound/radiographs | Congenital hip dislocation |
| Skeletal survey/targeted radiographs | Osteopenia, Wormian bones, scoliosis, contractures |
| Flexion–extension cervical radiographs | Consider instability where clinically indicated |
| Full ophthalmologic/anterior-segment examination | Cataract, corneal clouding, strabismus and refractive error |
| Echocardiography | Baseline/periodic evaluation; occasional aortic or cardiac involvement |
| Pulmonary function testing | Older cooperative children, particularly if respiratory symptoms |
| Skin biopsy with elastic stain/electron microscopy | Can demonstrate reduced/fragmented elastic fibers but is nonspecific and usually unnecessary after molecular diagnosis |

The 2011 compound-heterozygous case broadened the phenotype to include congenital glaucoma, aortic-root dilation and hypertrophic pyloric stenosis, but these should be regarded as uncommon associations rather than defining criteria (PMID **22052856**). [81]

## 10.3 Genetic-testing modalities

- **Multigene panel:** appropriate first-line test where a cutis-laxa phenotype is recognizable. Include at least PYCR1, ALDH18A1, ATP6V0A2, ATP6V1A, ATP6V1E1, GORAB, FBLN5, EFEMP2, LTBP4, LOX, EMILIN1, SLC25A24, LTBP1 and relevant progeroid genes.
- **WES:** highly useful because most known variants are coding or splice-proximal and phenotypic overlap is extensive.
- **WGS:** useful after negative panel/WES, particularly for structural, deep intronic or regulatory variants.
- **Single-gene sequencing:** reasonable in a highly characteristic familial phenotype or for cascade testing.
- **CMA:** low yield as an isolated test; can identify large deletions or an alternative genomic diagnosis.
- **Karyotype/FISH:** not routinely indicated.
- **Mitochondrial-DNA testing:** not indicated unless a separate mtDNA disorder is suspected.
- **Repeat-expansion testing:** not applicable.
- **RNA sequencing:** potentially useful to resolve a suspected splice variant, but not routine.
- **Proteomics/metabolomics/epigenomics/liquid biopsy:** research only.

## 10.4 Differential diagnosis

| Disorder/gene | Distinguishing considerations |
|---|---|
| ALDH18A1-related ARCL/De Barsy | Often more severe developmental impairment, metabolic amino-acid abnormalities and corneal disease; substantial overlap |
| ATP6V0A2/ATP6V1A/ATP6V1E1-related cutis laxa | Abnormal transferrin glycosylation, large fontanel and characteristic brain/cortical findings |
| GORAB-related geroderma osteodysplasticum | Recurrent fractures, little CNS involvement, usually no IUGR |
| FBLN5/LTBP4-related ARCL | Severe pulmonary emphysema, diaphragmatic hernia or visceral diverticula; cognition usually normal |
| EFEMP2/LOX/EMILIN1 disorders | Arterial tortuosity, aneurysm/dissection or marfanoid features |
| Hutchinson–Gilford progeria, LMNA | Progressive atherosclerosis, alopecia and characteristic skeletal changes rather than congenital cutis laxa |
| Wiedemann–Rautenstrauch syndrome, POLR3A | Neonatal progeroid appearance and natal teeth |
| Fontaine progeroid syndrome, SLC25A24 | Craniosynostosis and hypertrichosis |
| Nestor–Guillermo progeria, BANF1 | Severe mandibular hypoplasia |
| SOPH syndrome, NBAS | Pelger–Huët anomaly, elevated liver enzymes and optic atrophy |
| Menkes/occipital-horn syndrome, ATP7A | Abnormal copper metabolism, pili torti and X-linked inheritance |

[61]

There are no universally adopted disease-specific clinical criteria; molecular confirmation is the standard.

## 10.5 Screening

- Not included in routine newborn biochemical screening.
- Newborn evaluation is indicated when there is an affected sibling or known familial genotype.
- Carrier and cascade testing should be offered after familial variants are identified.
- Prenatal diagnosis and preimplantation genetic testing are technically feasible.
- Population-wide carrier screening is not currently standard.

---

# 11. Outcome and prognosis

No valid 5- or 10-year survival rate, mortality rate or median life expectancy has been established. Available data do **not** support applying the high early mortality of severe pulmonary ARCL1 disorders to PYCR1-related ARCL.

Likely long-term morbidity includes:

- intellectual and developmental disability;
- impaired speech, mobility and self-care;
- joint instability or contractures;
- scoliosis and hip disease;
- osteopenia and occasional fracture;
- feeding and growth problems;
- cataract or corneal-clouding-associated visual impairment;
- seizures or movement disorder in some individuals.

Developmental improvement may occur with therapy, but full recovery from the genetic neurodevelopmental phenotype is not expected. Regression is not usual. Wrinkling and growth deficiency can become less prominent, which is phenotypic evolution rather than remission. [61]

No validated prognostic biomarker exists. Potential prognostic indicators include:

- variant location/residual enzyme function;
- degree of early developmental impairment;
- ocular involvement;
- congenital orthopedic burden;
- seizures or spasticity;
- nutritional status.

Variant-specific prediction remains unreliable: the same p.Ala187Thr allele was associated with mild intellectual disability in one compound-heterozygous individual and extremely severe delay in a homozygous child. [33]

---

# 12. Treatment

## 12.1 Current standard

There is **no approved disease-modifying therapy**. Management is individualized and multidisciplinary. No PYCR1-specific treatment-response rates or controlled adverse-event data are available. [169][172]

| Intervention | Indication/purpose | Evidence | Suggested NCIT concept |
|---|---|---|---|
| Physical therapy | Hypotonia, delayed motor skills, hypermobility, spasticity, contractures | Expert consensus/supportive | Physical Therapy |
| Occupational therapy | Hand function, adaptive skills, activities of daily living | Expert consensus | Occupational Therapy |
| Speech/language and feeding therapy | Speech delay, dysphagia and communication | Expert consensus | Speech Therapy |
| Nutritional support | Feeding difficulty, malnutrition, poor growth | Supportive | Nutritional Support |
| Standard antiseizure medication | Epilepsy | Treat as other epilepsies; no genotype-specific drug | Anticonvulsant Therapy |
| Orthoses/mobility devices | Contractures, gait impairment, long-distance mobility | Supportive | Assistive Device |
| Orthopedic intervention | Hip dislocation, scoliosis, clubfoot, severe contracture | Case-specific | Orthopedic Surgery |
| Cataract/corneal surgery | Vision-limiting opacity | Case-specific | Cataract Surgery / Corneal Transplantation |
| Hernia repair | Symptomatic inguinal/umbilical hernia | Standard surgical practice | Hernia Repair |
| Calcium/vitamin D management | Documented deficiency or osteopenia | General bone-health practice; not disease-modifying | Calcium Supplementation / Vitamin D Supplementation |
| Arginine supplementation | Low ornithine/citrulline/arginine | Case reports only; benefit unconfirmed | Arginine Supplementation |
| Citrulline/proline replacement | Biochemical deficiency | Case reports only; benefit unconfirmed | Amino Acid Supplementation |
| Blood-pressure/cardiology care | Individual vascular/cardiac abnormality | Precautionary/standard care | Antihypertensive Therapy |

The limited literature explicitly states that supplementation evidence is confined to case reports and that clinical benefit remains unconfirmed. [172][175]

## 12.2 Surveillance

A reasonable schedule based on the current GeneReviews framework is:

- neurologic examination every six months initially, then annually;
- developmental/educational review every six months initially, then annually;
- growth and nutrition at each visit;
- orthopedic review every six months through infancy, then annually;
- annual anterior-chamber and lens examination;
- EEG as clinically indicated;
- echocardiography approximately every three years, more often if abnormal;
- brain MRI/MR angiography approximately every ten years or sooner for new neurologic findings;
- pulmonary function testing every three years from about age eight, where feasible. [63]

Some vascular surveillance recommendations are precautionary extrapolations across mitochondrial proline-synthesis disorders because intracranial arterial tortuosity has not been adequately evaluated in PYCR1 disease.

## 12.3 Experimental therapy

No confirmed active interventional trial, gene therapy, CRISPR therapy, RNA therapy, cell therapy, targeted small molecule or immunotherapy specific to PYCR1-related De Barsy syndrome was identified.

Proposed research directions—not clinical recommendations—include:

- restoration of PYCR1 expression;
- augmentation of compensatory PYCR2;
- mitochondrial/redox-targeted antioxidants;
- proline-pathway supplementation;
- prevention of stress-induced apoptosis;
- cell-specific gene replacement.

Proline or antioxidant rescue remains speculative; normal systemic proline in many patients and incomplete animal-model recapitulation argue against assuming that simple supplementation will correct disease. [180][218]

## 12.4 Anaesthesia and procedures

Before surgery, assess:

- difficult airway from craniofacial anatomy;
- joint and cervical-spine instability;
- ocular vulnerability;
- nutritional status;
- respiratory and cardiovascular involvement;
- skin fragility and pressure-point protection.

No PYCR1-specific pharmacogenomic guidance exists in PharmGKB/CPIC terms.

---

# 13. Prevention

## 13.1 Primary prevention

The phenotype cannot be prevented through vaccination, diet, lifestyle or avoidance of infection. Reproductive prevention options after identifying familial variants include:

- carrier testing of relatives;
- partner testing;
- preimplantation genetic testing for monogenic disease;
- chorionic-villus or amniotic-fluid prenatal diagnosis;
- donor gametes or other informed reproductive choices.

Genetic counseling should communicate the **25% recurrence risk per pregnancy** when both parents are carriers. [61]

## 13.2 Secondary prevention

There is no population newborn-screening program. In an at-risk neonate:

- perform targeted familial-variant testing promptly;
- evaluate feeding, growth, hips, eyes, development and tone;
- begin early intervention before fixed contractures or preventable visual loss develops.

## 13.3 Tertiary prevention

Measures include:

- early developmental therapy;
- hip and scoliosis surveillance;
- maintenance of mobility and range of motion;
- treatment of cataract/corneal opacity before irreversible visual deprivation;
- seizure recognition and treatment;
- pressure-injury and skin protection;
- assessment of bone density and nutritional deficiencies;
- avoidance of smoking, excessive sun exposure, high-impact/contact sports where unsafe and prolonged fasting.

No vaccine, antimicrobial prophylaxis or public-health environmental intervention is disease-specific.

---

# 14. Other species and natural disease

No well-established naturally occurring PYCR1-related De Barsy syndrome was identified in companion animals, livestock or wildlife. Accordingly:

- there is no recognized affected breed;
- no Vertebrate Breed Ontology term is applicable;
- there is no zoonotic or cross-species transmission.

Relevant orthologues include:

| Species | NCBI taxonomy | Orthologue/resource | Natural disease |
|---|---:|---|---|
| Human, *Homo sapiens* | 9606 | PYCR1, NCBI Gene 5831 | Yes |
| Mouse, *Mus musculus* | 10090 | Pycr1, MGI:2384795 | Experimental knockout; no established natural homologous disease |
| Zebrafish, *Danio rerio* | 7955 | pycr1a, NCBI Gene **393799**; also pycr1b paralogue | Experimental model only |
| Frog, *Xenopus* spp. | Species-dependent | pycr1 orthologue | Morpholino/knockdown model only |

Mouse, rat and human have one stringent PYCR1 orthologue, whereas zebrafish have two related orthologues/paralogues. [137][138]

---

# 15. Model organisms

| Model | Manipulation | Phenotype recapitulated | Limitations and applications |
|---|---|---|---|
| Patient dermal fibroblasts | Endogenous biallelic pathogenic variants | Altered mitochondrial morphology, reduced membrane potential, oxidative-stress hypersensitivity and increased apoptosis | Most directly disease-relevant cellular model, but lacks whole-organism development |
| HEK293T cells | Overexpression of p.Ala187Thr | Reduced PYCR1 abundance and approximately 54% lower enzyme activity | Artificial overexpression and non-dermal cell context; useful for variant functional testing |
| Zebrafish embryo | pycr1 knockdown | Epidermal hypoplasia, blistering and increased apoptosis | Morpholino-specific limitations |
| Zebrafish pycr1a knockout | TALEN-generated 2-bp frameshift | Progeroid appearance from about four months, behavioral abnormalities, increased senescence/apoptosis and approximately 50% mortality near six months | Fish skin and lifespan differ from humans; valuable for aging and drug-screen research |
| Xenopus embryo | Orthologue knockdown | Epidermal hypoplasia, blistering and marked apoptosis | Transient developmental model |
| Mouse Pycr1 knockout, KOMP line | Null allele | Male impaired glucose tolerance and reduced triglycerides; no overt cutis laxa phenotype | Poor human-phenotype recapitulation, likely Pycr2 compensation |
| Mouse constitutive Pycr1 knockout, 2023 model | Near-complete loss of Pycr1 | Dermal thinning and fewer collagen fibers | Epidermis and overall phenotype comparatively normal; may require Pycr1/Pycr2 double knockout |

The original model-organism abstract reports: **“Knockdown of the orthologous genes in Xenopus and zebrafish led to epidermal hypoplasia and blistering that was accompanied by a massive increase of apoptosis.”** (PMID **19648921**). [107]

The stable zebrafish knockout was viable but developed a progeroid phenotype from four months and reached approximately 50% mortality by six months (PMID **31091804**, published 14 May 2019). [123][125]

Mouse results are model-dependent. A 2021 KOMP study found no overt integumentary or cutis-laxa phenotype, whereas the more recent model detected dermal thinning and reduced collagen. Together these indicate partial rather than complete recapitulation and likely species-specific PYCR2 compensation. [130][126]

Recommended resources include MGI/IMPC/KOMP for mouse alleles, ZFIN for **pycr1a**, and patient-derived fibroblast repositories where consent permits.

---

# Evidence highlights and exact abstract quotations

| Evidence type | Publication | Key quotation/finding |
|---|---|---|
| Human genetics + patient fibroblasts + vertebrate knockdown | Reversade et al., *Nature Genetics*, published online **2 August 2009**, PMID **19648921**, DOI: https://doi.org/10.1038/ng.413 | “Altered mitochondrial morphology, membrane potential and increased apoptosis rate upon oxidative stress were evident in fibroblasts from affected individuals.” [17] |
| Human genotype–phenotype cohort | Dimopoulou et al., *Molecular Genetics and Metabolism*, November **2013**, PMID **24035636**, DOI: https://doi.org/10.1016/j.ymgme.2013.08.009 | “Here we describe 33 patients with PYCR1-related ARCL from 27 families…” Twenty mutations were identified, seven novel; first-two-exon variants were associated with lower severity. [106][115] |
| Human De Barsy case | Lin et al., *American Journal of Medical Genetics A*, December **2011**, PMID **22052856**, DOI: https://doi.org/10.1002/ajmg.a.34326 | Compound heterozygous frameshift/missense alleles expanded the clinical spectrum to congenital glaucoma, aortic-root dilation and pyloric stenosis. [81] |
| Variant assay + longitudinal child assessment | 2024 study, published **22 August 2024**, PMID **39172257**, DOI: https://doi.org/10.1007/s00438-024-02173-y | “Mutagenesis and enzyme assay study revealed decreased activity of the mutant protein in vitro, indicating that this mutation impairs PYCR1 function.” [33] |
| Stable zebrafish model | Liang et al., *Cells*, published **14 May 2019**, PMID **31091804** | pycr1-deficient fish developed premature-aging and behavioral phenotypes and approximately 50% mortality near six months. [123][125] |
| Recent skin-aging/mouse work | *PYCR1 Levels Track with Premature and Chronological Skin Aging*, **2023** | Pycr1 loss caused dermal thinning and reduced collagen, but the mouse remained otherwise relatively normal, indicating incomplete phenocopy. [124][126] |

---

# Knowledge gaps and curation cautions

1. **ARCL2B versus ARCL3B:** these should be cross-referenced as a spectrum, not treated as completely independent molecular disorders.
2. **Phenotype frequencies:** most percentages combine PYCR1 and ALDH18A1 disorders; annotate them as pooled estimates.
3. **Epidemiology:** no population-based incidence or robust prevalence data exist.
4. **Prognosis:** life expectancy and long-term adult natural history are unknown.
5. **Mechanism:** mitochondrial oxidative-stress susceptibility is demonstrated, but whether deficient proline supply, altered NAD(P)H redox balance, apoptosis or another PYCR1 function is dominant remains unresolved.
6. **Treatment:** no controlled therapeutic trial or validated disease-modifying intervention exists.
7. **Omics:** disease-specific single-cell, spatial, proteomic, lipidomic and epigenomic datasets are lacking.
8. **Animal models:** current models only partially reproduce human disease, especially the neurologic and ocular phenotype.
9. **Ontology practice:** retain **MONDO:0013755** for gene-defined PYCR1-related De Barsy syndrome, while linking OMIM 614438, ARCL3B, ARCL2B/OMIM 612940 and the broader PYCR1-related ARCL spectrum.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 63 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006561` (obsolete proline biosynthetic process) (1 mention) - replaced by `GO:0055129`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.

58 of 63 terms resolved to a current term; the rest could not be looked up either way.