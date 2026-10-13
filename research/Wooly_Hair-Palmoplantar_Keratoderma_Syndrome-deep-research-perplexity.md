---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-11T20:05:42.093816'
end_time: '2026-10-11T20:08:30.995569'
duration_seconds: 168.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Wooly Hair-Palmoplantar Keratoderma Syndrome
  mondo_id: MONDO:0014492
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
citation_count: 54
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 28
  verified: 18
  not_found: 0
  obsolete: 0
  unverifiable: 10
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - Taxon
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Wooly Hair-Palmoplantar Keratoderma Syndrome
- **MONDO ID:** MONDO:0014492 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Wooly Hair-Palmoplantar Keratoderma Syndrome** covering all of the
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

# Woolly hair–palmoplantar keratoderma syndrome: disease-characteristics report

**Disease identity and scope.** **MONDO:0014492** refers specifically to **KANK2-associated palmoplantar keratoderma and woolly hair (PPKWH)**, also called *keratoderma with woolly hair type IV*. Its characteristic combination is sparse or woolly hair, childhood-onset palmoplantar keratoderma, and nail changes **without the cardiomyopathy characteristic of the clinically overlapping Naxos and Carvajal syndromes**. That distinction is important both for knowledge-base annotation and for the initial assessment of a person whose genetic diagnosis is not yet known. [46][47][53][141]

**Evidence boundary.** The central human genetic and mechanistic evidence is a 2014 investigation of **two consanguineous families**, subsequently described as comprising **seven affected people**. Later reports diagnosed type IV clinically but did not establish a new, molecularly confirmed *KANK2* series. Thus, percentages calculated from published cases would misleadingly imply a representative cohort. Evidence below is labeled as human clinical, patient-cell, other-gene/model, or inference where that distinction matters. [31][93][79]

## 1. Disease information and identifiers

| Identifier or name | Value and interpretation |
|---|---|
| Disease name and MONDO | Woolly hair–palmoplantar keratoderma syndrome; **MONDO:0014492**. [46] |
| OMIM | **616099**, *Palmoplantar keratoderma and woolly hair*; **PPKWH**. The *KANK2* **gene**, separately, is OMIM **614610**. [46][34] |
| Orphanet | **ORPHA:420686**. [47] |
| ICD-10 | **Q82.8**, an Orphanet-listed, nonspecific congenital skin-malformation code—not a uniquely identifying code for this genotype. [47] |
| ICD-11; disease-specific MeSH | A distinct identifier was **not verified**. PubMed indexes the founding article under broader terms including *Keratoderma, Palmoplantar* and *Hair Diseases*. [31] |
| Other identifiers | MedGen **C4015202**; an alternative MedGen concept, **C4706686**, and SNOMED CT **764108000** are also associated with the type-IV description. [46][172] |
| Synonyms | *Palmoplantar keratoderma and woolly hair*; *PPKWH*; *woolly hair-palmoplantar hyperkeratosis syndrome*; *keratoderma with woolly hair type IV*; *KWWH type IV*. The 2025 classification also calls it **KANK2-pEDD**, meaning a *KANK2*-associated palmoplantar epidermal differentiation disorder. [47][61] |
| Evidence provenance | **Aggregated disease-level resources**, anchored principally in published family examinations, sequencing, patient keratinocyte assays, and individual case reports—not an EHR-derived incidence or outcomes dataset. [31][47][93] |

Orphanet describes the syndrome as “a very rare, hereditary epidermal disorder” in which palmoplantar keratoderma “progressively worsens with age” and cardiomyopathy is “notably absent.” [47]

## 2. Etiology, risks, protection, and gene–environment interaction

The demonstrated cause is an **inherited, biallelic *KANK2* missense variant**, **c.2009C>T, p.(Ala670Val)**, identified by whole-exome sequencing in affected members of the two founding families. *KANK2* encodes steroid receptor coactivator–interacting protein (**SIP**), which regulates the localization and transcriptional activity of nuclear-receptor coactivators. This is a **non-desmosomal** cause of the hair–keratoderma combination; *JUP*, *DSP*, and *DSC2* belong primarily in the **differential diagnosis**, not as established causes of MONDO:0014492. [53][51]

**Genetic risk** is chiefly inheriting two disease-associated alleles; parental consanguinity can increase the chance of homozygosity for a rare familial allele. Six unaffected parents in the founding-family assessment were reported as heterozygous. No validated susceptibility locus, severity-modifier allele, protective allele, or population carrier frequency was established for this syndrome. The clinically reported families originated near Jerusalem, but that observation does **not** establish an ethnic-specific risk or a quantified founder effect. [79][95][53]

**Environmental causation and protection:** no toxin, diet, infection, occupation, smoking exposure, or protective lifestyle practice has been shown to cause or prevent the *KANK2* disorder. Because palmoplantar skin bears mechanical load, friction may reasonably aggravate existing keratoderma; **this is a care-related inference, not a demonstrated *KANK2* gene–environment interaction**. In the founding experiments, vitamin D was an **assay stimulus** revealing increased receptor-mediated transcription—not evidence that vitamin D exposure causes disease or that supplementation treats it. [53][44]

## 3. Phenotypes and functioning

The table separates **reported manifestations** from features of a **clinically suspected but genetically unconfirmed** case. “Not quantified” means that neither a valid disease-wide percentage nor a standardized quality-of-life score is available. HPO identifiers are **suggested phenotype annotations**, not assertions of HPO-curated frequencies. [47][53][93]

| Phenotype and type | Onset, course, severity, and frequency | Function or quality-of-life impact; suggested HPO |
|---|---|---|
| **Palmoplantar keratoderma**—physical sign: typically striate on palms, with marked plantar involvement | Early childhood; progressively thickens; variable extent. A later clinically diagnosed case reported onset at **6 months** and unusually diffuse disease. Cardinal feature in the genetically studied families; no population percentage. [47][93][61] | Thick plantar skin may impede comfortable walking or hand use; individual disability scores are unavailable. **HP:0000982** (*palmoplantar keratoderma*). [177][93] |
| **Woolly, tightly curled scalp hair**—physical sign | Usually apparent from birth; texture and prominence vary, so “woolly” should not be forced as 100% of molecularly affected individuals. **HP:0002224**. [53][47][198] | Visible hair difference may affect well-being, but syndrome-specific patient-reported measures are unavailable. [47] |
| **Sparse scalp and body hair**, including eyebrows or eyelashes—physical signs | Congenital or early-life hair abnormality; degree varies; frequency not quantified. **HP:0002209** (*sparse scalp hair*); use a more specific eyebrow/eyelash term only when documented. [47][282] | Possible cosmetic and psychosocial burden; not measured for this cohort. [47] |
| **Leukonychia**—nail sign | Reported fingernail whitening; precise onset, penetrance, and severity unavailable. **HP:0001820**. [47][279] | Functional impairment not established. [47] |
| **Follicular keratoses or papules**—skin sign | Reported as a clinical clue, including on extremities and cheeks; frequency and timing unknown. **HP:0007502** (*follicular hyperkeratosis*) when histologically or clinically appropriate. [95][61][369] | Discomfort or appearance-related impact is plausible, not quantified. [61] |
| **Fifth-toe pseudoainhum**—constricting-band sign | **Occasionally reported**; age and risk of digit loss in molecularly confirmed PPKWH are unknown. Record the observed digital constriction precisely rather than assigning an unverified HPO code. [47][93] | Potentially important for toe function and early assessment; disease-specific outcome data are absent. [47] |
| **Severe finger contractures; thickened nails**—additional signs in one case | Observed in a **35-year-old clinically diagnosed, unsequenced man** with diffuse keratoderma. Do **not** treat these as established frequencies or genotype-specific manifestations. [93] | Contractures directly limited joint movement in that patient; no cohort-level measure. [93] |
| **Sensorineural hearing loss and maculopathy**—provisional findings | A **2026 report** describes these in one **25-year-old woman** labeled type IV. Its abstract does not report *KANK2* confirmation; a causal association remains **unproven**. [391] | Hearing and visual consequences require their own evaluation; do not yet populate them as established *KANK2*-PPKWH phenotypes. [391] |

**Negative clinical feature:** absence of cardiomyopathy is part of the currently described *KANK2* phenotype, **not** a test that safely identifies the gene before sequencing. The small number of observed patients cannot establish lifetime cardiac risk as exactly zero. [53][47][141]

## 4. Genetic and molecular information

| Item | Knowledge-base-ready finding and evidence limit |
|---|---|
| Established syndrome-associated gene | ***KANK2***; **HGNC:29300**, **NCBI Gene:25959**, chromosome **19p13.2**, gene OMIM **614610**. The disease association has **limited/supportive, rather than uniformly definitive, submitted GenCC assessments**; Genomics England retains a low-evidence panel classification. [235][57][79] |
| Principal reported allele | ***KANK2* c.2009C>T, p.(Ala670Val)**: inherited **germline**, homozygous **missense** allele segregating with the syndrome in the founding families. Patient-cell experiments support altered function, but a single paper’s designation of it as causal should **not** be misrepresented as an independently verified, current ClinVar ACMG/AMP “pathogenic” classification. [53][79] |
| Population frequency and variant classification | A reliable **allele-specific gnomAD frequency, rsID, and current ClinVar assertion for this exact *KANK2* allele were not verified**. Do not substitute the identically written **PIDD1** c.2009C>T, p.Ala670Val ClinVar record: it is a **different gene**. [205][53] |
| Functional direction | Evidence supports **impaired cytoplasmic sequestration of SRC-2/NCOA2 and SRC-3/NCOA3**, with **increased vitamin-D-stimulated transcription** in patient keratinocytes. A specific downstream epidermal target gene and the full molecular route to hair-shaft shape remain unresolved; calling the allele a universal *KANK2* null would go beyond the experiments. [53][68] |
| Protein-structure resource | **PDB 6TMD** is an experimentally solved, **1.50-Å** crystal structure of the human A670V ankyrin-repeat fragment, released **2020-12-16**. It is structural evidence, **not** a measured clinical penetrance or treatment response. [250] |
| Other alleles and phenotypes | Biallelic alterations of ***KANK2*** have separately been implicated in **nephrotic syndrome 16**. Those renal findings must not automatically be added as manifestations of the **p.Ala670Val hair–skin syndrome**. [112][57] |
| Modifiers, epigenetics, chromosomal abnormalities | No validated modifier gene, disease-specific DNA-methylation or chromatin signature, recurrent causative chromosomal rearrangement, anticipation mechanism, or germline-mosaicism estimate was identified for **MONDO:0014492**. The established lesion is a single-nucleotide variant, not an aneuploidy. [53][79] |

## 5. Environmental and infectious information

**No infectious agent or transmissible process is implicated.** There is no established disease-specific toxic, radiation, pollution, occupational, dietary, alcohol, or smoking etiology. Mechanical skin care can matter **after disease develops**, but should not be coded as a proven initiating exposure. The available family and keratinocyte evidence supports a Mendelian condition, rather than an acquired keratoderma. [53][47][44]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Inherited homozygous *KANK2* p.Ala670Val** **leads to** altered function of the SIP/KANK2 ankyrin-repeat protein; the genotype and patient-cell effects are demonstrated, while the precise molecular binding defect is **inferred**. [53][250]
2. **Altered SIP regulation** **leads to** less effective cytoplasmic retention of the steroid-receptor coactivators **SRC-2/NCOA2 and SRC-3/NCOA3**: their **nuclear localization in patient basal epidermal cells**, versus cytoplasmic localization in a heterozygous control, was observed. [53]
3. **Increased nuclear coactivator availability** **results in** increased **vitamin-D-induced receptor transactivation** in patient keratinocytes, as experimentally measured. This places altered coactivator localization **upstream** of the measured transcriptional output. [53]
4. **Altered epidermal transcription and differentiation** **is inferred to lead to** excessive palmoplantar cornification and altered follicular/hair growth, **resulting in** keratoderma, woolly or sparse hair, and associated nail findings. The individual transcriptional targets and the route to each anatomical feature have **not** been demonstrated. [53][68]
5. **Branch—other *KANK2* dysfunction, not established as this syndrome’s causal route:** *KANK2* deficiency **leads to** altered podocyte RHOA signaling and filtration defects in experimental systems. This explains why *KANK2* can also be associated with a **separate nephrotic phenotype**; it does **not** demonstrate that the skin-associated A670V allele causes nephrosis. [112][216]

**Pathway and cell annotation.** The best-supported syndrome-specific pathway is **nuclear-receptor coactivation, including vitamin D receptor signaling**—suggested **GO:0070561**—in epidermal keratinocytes, particularly **CL:0002187** basal epidermal cells; broader **CL:0000312** denotes keratinocytes. Cytoplasm-to-nucleus redistribution is directly relevant; a desmosomal structural defect, Wnt/MAPK/mTOR activation, mitochondrial metabolic lesion, primary immunodeficiency, and systemic inflammatory mechanism have **not** been demonstrated for this genotype. The A670V protein structure is available, but no disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or CRISPR-screen signature was established. [53][129][220][230][250]

**Cross-phenotype caution:** research in other cells shows KANK2 interactions with focal-adhesion/cytoskeletal machinery, and podocyte knockdown alters RHOA activity. These are useful **functional hypotheses**, not proof that those pathways drive *A670V* keratoderma. [112][106]

> **Exact founding-abstract evidence (human patient-cell study; PMID: 24671081):** “Indeed, vitamin D-induced transactivation was increased in patient's keratinocytes.” The authors also report that SRC-2 and SRC-3 “are localised to the nucleus of epidermal basal cells in patients, in contrast to the cytoplasmic distribution in the heterozygous control.” Published online **26 March 2014**; DOI **10.1136/jmedgenet-2014-102346**; URL: https://pubmed.ncbi.nlm.nih.gov/24671081/. [31]

## 7. Anatomy and localization

| Level | Affected site or compartment; suggested ontology |
|---|---|
| Organ and system | Primarily **skin and hair**, within the integumentary system; nails are also affected. No confirmed primary cardiac involvement in molecularly described PPKWH. [47][53] |
| Palm and sole | Epidermis (**UBERON:0001003**) of palmar skin (**UBERON:0001514**) and plantar skin (**UBERON:0001516**); a combined palm/sole site can use **UBERON:0013776**. Plantar involvement may be more severe. [47][222][304] |
| Follicle and cells | Scalp **hair follicle, UBERON:0002074**; epidermal **keratinocyte, CL:0000312**, and **basal cell of epidermis, CL:0002187**. Hair-follicle involvement is clinically evident, whereas the reported coactivator-localization assay specifically examined basal epidermal cells. [222][230][53] |
| Subcellular | **Cytoplasm and nucleus**, the experimentally compared coactivator locations. Assign specific GO cellular-component accessions only after ontology validation; mitochondria, ER, and lysosomes are **not** implicated by the patient assay. [53] |
| Laterality | Generally described as palmoplantar involvement rather than a defined unilateral lesion; **a numerical bilateral-versus-asymmetric frequency is unavailable**. Fifth-toe pseudoainhum can be recorded by its actual side for each patient. [47][93] |

## 8. Temporal development

Hair texture is generally abnormal **at birth**; keratoderma emerges in **infancy or early childhood** and may increase with age. One clinically diagnosed adult recalled palmoplantar thickening from **six months**; Orphanet lists neonatal, infancy, and childhood onset. The disorder is **chronic**, not an acute infection or relapsing-remitting episode. Published evidence does not support a formal early/intermediate/end-stage system, a measured progression rate, or predictable spontaneous remission. The useful intervention window is **early recognition of hair plus keratoderma**—both to address progressive skin thickening and, before molecular clarification, to investigate possible cardiac syndromes. [47][93][141]

## 9. Inheritance and population

Orphanet estimates prevalence at **fewer than 1 per 1,000,000 people**—equivalently **fewer than 0.1 per 100,000**—rather than a measured point prevalence. **Incidence per 100,000 per year is unavailable.** Reported inheritance is **autosomal recessive**. Consanguinity characterized the two original Arab families; a separate clinically diagnosed case had non-consanguineous parents, but lacked *KANK2* testing. No reliable sex ratio, age distribution, allele-specific geographic distribution, population carrier frequency, lifetime penetrance, or expressivity percentage exists. There is no evidence for genetic anticipation. For two confirmed carrier parents, standard autosomal-recessive segregation implies a **25% affected-child probability per pregnancy**, assuming both carry disease-causing alleles. [47][53][79][93]

**Do not transfer population statistics from Naxos disease**—including estimates from Greek islands—to this distinct, non-cardiomyopathic *KANK2* condition. [28][47]

## 10. Diagnosis and differential diagnosis

**Clinical entry point:** examine hair texture and density, distribution of palmar versus plantar thickening, nails, follicular papules, and toe constrictions; document pedigree and age at onset. **Before the genotype is established, obtain cardiac evaluation**, including **ECG and echocardiography**, because phenotypically similar desmosomal disorders can develop cardiomyopathy. These tests were normal in the founding description and in a later clinically diagnosed case; a normal examination alone **does not establish a *KANK2* diagnosis**. [53][93][141]

**Molecular strategy:** a hereditary palmoplantar-keratoderma or cardiocutaneous panel including ***KANK2, JUP, DSP,* and *DSC2*** is a practical first approach. If a familial *KANK2* allele is known, targeted testing and segregation analysis are appropriate. **WES** found the founding allele; **WES or WGS** can help when a panel is negative or features are atypical. NCBI GTR lists *KANK2* coding-region sequencing. Chromosomal microarray, karyotype, FISH, mitochondrial sequencing, and repeat-expansion assays are **not routine tests for this established single-gene phenotype**, absent a separate indication. No validated blood metabolite, enzyme assay, circulating biomarker, RNA-sequencing test, proteomic assay, epigenomic test, or liquid biopsy diagnoses it. [53][54][404][61]

A biopsy may show **nonepidermolytic hyperkeratosis and acanthosis** but is not molecularly diagnostic. The unsequenced adult case showed hyperkeratosis, parakeratosis, hypergranulosis, and epidermal hyperplasia without epidermolysis. [61][93]

| Differential | Crucial distinction or test |
|---|---|
| **Naxos disease—*JUP*** | Similar hair and keratoderma with **arrhythmogenic, predominantly right-ventricular cardiomyopathy**; assess heart and sequence the relevant gene. [18][51] |
| **Carvajal syndrome—*DSP*** | Similar ectodermal signs with potentially serious **left-ventricular or dilated cardiomyopathy**, often developing in childhood. [17][50] |
| ***DSC2*-associated cardiocutaneous disease** | Keratoderma/hair findings can overlap, with **arrhythmogenic cardiomyopathy**; use a multigene assessment rather than appearance alone. [51] |
| **Other inherited palmoplantar keratodermas**, including *DSG1*- or *KRT1*-associated disease | Skin distribution, nails, other organ findings, inheritance, and sequencing help separate them. A Danish cohort published online **4 December 2024** identified a genetic diagnosis in **63/76 families (83%)**, but **reported no *KANK2* diagnosis**; its yield is **not a PPKWH-specific diagnostic sensitivity**. PMID **39630431**; https://jamanetwork.com/journals/jamadermatology/fullarticle/2826499. [264][308][320] |

## 11. Outcomes and prognosis

The described *KANK2* syndrome lacks the **documented cardiomyopathy burden** of Naxos and Carvajal syndromes. Nevertheless, **five- or ten-year survival, life expectancy, syndrome-specific mortality, disability rates, and EQ-5D/SF-36/PROMIS scores have not been measured**. The principal documented burden is chronic, potentially progressive keratoderma with hair/nail changes; occasional constricting toes warrant attention. A **35-year-old clinically diagnosed but unsequenced** man had marked finger contractures, demonstrating a possible functional concern without establishing its frequency in confirmed *KANK2* disease. Neither a validated prognostic molecular marker nor a genotype-based prediction model exists. [47][93][53]

**Important renal distinction:** *KANK2* is also a nephrotic-syndrome gene, but available evidence does not establish proteinuria or renal failure as an expected complication of the founding **p.Ala670Val PPKWH phenotype**. [112][216]

## 12. Treatment and implementation

There is **no established curative or *KANK2*-targeted treatment**. Treatment is directed at keratoderma, function, and correctly identifying any patient who instead has a cardiomyopathy-associated genotype. A clinical report documented improvement after combined topical keratolytics and oral acitretin, but **did not genotype its patient**; it cannot supply a *KANK2*-specific response rate. [93][44][141]

| Intervention and suggested annotation | Use, evidence, outcomes, and cautions |
|---|---|
| **Emollients and topical keratolytics**; suggested chemicals **urea CHEBI:16199**, **salicylic acid CHEBI:16914** | Symptomatic softening and reduction of hyperkeratosis, based largely on broader inherited-keratoderma management. The clinically diagnosed adult received topical keratolytics alongside acitretin, so their separate effect cannot be estimated. No *KANK2*-specific NCIt intervention code was verified. [44][93][326][330] |
| **Careful mechanical reduction of callus, footwear or pressure accommodation, and functional support** | Practical measures for symptomatic keratoderma; tailor podiatry or hand therapy to pain, gait, or contractures. This is **supportive extrapolation**, not a syndrome-specific trial result. [44][93] |
| **Oral acitretin**, a systemic retinoid; **CHEBI:50173**, **NCIT:C985** | In one **unsequenced** 35-year-old, **25 mg daily plus topical keratolytics** produced reported “remarkable improvement” within **two months**. This is **one combined-treatment observation**, not a response percentage. The authors monitored liver function and lipid profile; systemic-retinoid reproductive and other safety precautions require specialist review. [93][324] |
| **Assessment of a toe constriction, with procedural referral if threatening function** | Pseudoainhum was reported, but no *KANK2*-specific surgical outcome or preferred procedure was established. [47][93] |
| **Gene, cell, RNA, immunologic, or pathway-targeted therapy** | No established treatment, response rate, *KANK2*-PPKWH-specific NCT trial identifier, or validated genotype-guided drug regimen was identified. Increased vitamin-D-stimulated transcription **does not justify vitamin D or VDR-targeted treatment**. [53][61] |

> **Exact case-report text (human clinical, genetically unconfirmed; PMID: 35283492):** “Remarkable improvement in palmoplantar keratoderma was noticed within 2 months of oral acitretin therapy.” The publication is a **letter without an abstract**, so this is an article-text quotation, not an abstract quotation. *Indian Journal of Dermatology*, **2021**, 66:693–695; DOI **10.4103/ijd.IJD_107_21**; URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8906310/. [93]

## 13. Prevention and counseling

**Primary prevention of the mutation itself** is not achievable through vaccination, diet, or exposure avoidance; the condition is not infectious. **Genetic counseling** can explain recessive recurrence risk and offer testing of relatives for a **known familial variant**, carrier testing, and, where appropriate and desired, reproductive options including prenatal or preimplantation testing. These are family-planning measures, not treatment of an affected child. [47][53][61]

**Secondary prevention** is timely recognition of congenital unusual hair followed by evolving palmoplantar thickening, molecular clarification, and **initial cardiac assessment while Naxos/Carvajal-type disease remains possible**. No established population newborn-screening program for this syndrome was identified. **Tertiary prevention** focuses on skin comfort and mobility, inspection of constricting bands, and care of any clinically present fissures or complications; no syndrome-specific prophylactic medication is established. [141][47][44]

## 14. Other species and natural disease

| Species or comparative finding | Relevance and limit |
|---|---|
| **Human, *Homo sapiens* (NCBI Taxon:9606)** | The naturally occurring, genetically studied disease is human *KANK2*-associated PPKWH. [53] |
| **Dog, *Canis lupus familiaris* (NCBI Taxon:9615)** | OMIA records **woolly hair** as an animal trait, but this is **not evidence of a naturally occurring canine *KANK2* palmoplantar-keratoderma syndrome**; no qualifying breed/VBO identifier was established. [382] |
| **Other animal species** | *Kank2* orthologs enable mechanistic comparisons, but no verified spontaneous animal case recapitulating this **specific combined human skin-and-hair syndrome** was identified. It is **not zoonotic**. [112][294] |

## 15. Model organisms and research applications

| Model or resource | What it demonstrates; what it does **not** recapitulate |
|---|---|
| **Patient-derived human keratinocytes and epidermal biopsy** | **Most directly relevant disease model:** increased vitamin-D-induced transactivation and altered SRC-2/SRC-3 localization in A670V-associated disease. These are functional findings in patient material, but do not identify all downstream target genes. PMID **24671081**. [53] |
| **Purified human A670V protein fragment; PDB 6TMD** | X-ray structure of mutant KANK2 ankyrin repeats at **1.50 Å** supports structural investigation; a purified fragment does not reproduce hair-follicle development or a whole patient’s disease. [250] |
| **Zebrafish, *Danio rerio* (NCBI Taxon:7955), *kank2* NCBI Gene:571549** | Experimental **knockdown** produced **proteinuria and podocyte foot-process effacement**, modeling a **renal KANK-deficiency phenotype**, **not demonstrated woolly hair plus keratoderma**. PMID **25961457**; published **2015**; https://pubmed.ncbi.nlm.nih.gov/25961457/. [112][242] |
| **Cultured podocytes and Drosophila nephrocytes** | Knockdown experiments support conserved renal-cell functions and altered RHOA-associated behavior; they are **not validated models of the A670V epidermal syndrome**. PMID **25961457**. [112] |
| **Mouse, *Mus musculus* (NCBI Taxon:10090), *Kank2* NCBI Gene:235041; MGI:2384568** | Ortholog and knockout resources exist, including an available knockout strain, but a verified **A670V knock-in reproducing both human hair and palmoplantar findings** was not identified. A general knockout must not be described as a phenotypically validated PPKWH model. [294][296][297] |

### Evidence assessment for database ingestion

The **highest-confidence entry** is the specific combination **MONDO:0014492 → autosomal-recessive *KANK2* → reported homozygous p.Ala670Val → hair, keratoderma, nail findings → altered SRC localization and vitamin-D-induced keratinocyte transactivation**. Code the last step from transcriptional dysregulation to particular hair and skin structures as **mechanistic inference**. Keep cardiomyopathy-associated *JUP/DSP/DSC2* disorders, other-*KANK2*-allele nephrotic syndrome, and the **unconfirmed 2026 hearing/retinal findings** distinct from the established disease phenotype. [53][57][68][112][391]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 10 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `Taxon`, `MGI`.

18 of 28 terms resolved to a current term; the rest could not be looked up either way.