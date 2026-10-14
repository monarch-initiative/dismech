---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:28.610407'
end_time: '2026-10-09T20:59:09.671103'
duration_seconds: 221.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: KLICK Syndrome
  mondo_id: MONDO:0011169
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
citation_count: 53
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - Taxon
  - Gene
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KLICK Syndrome
- **MONDO ID:** MONDO:0011169 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KLICK Syndrome** covering all of the
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

# KLICK syndrome: disease-characteristics research report

**KLICK syndrome** is a lifelong, autosomal-recessive disorder of epidermal keratinization caused, in genetically confirmed reports, by a **homozygous one-base deletion in the 5′ untranslated region of *POMP*, c.-95delC**. Its defining combination is congenital ichthyosiform scaling, palmoplantar keratoderma, linear keratotic lesions—especially in flexures—and sclerosing constriction bands around digits (*pseudoainhum*). The strongest mechanistic evidence links reduced POMP activity in differentiating keratinocytes to defective proteasome maturation, disturbed epidermal differentiation, and endoplasmic-reticulum (ER) stress. Evidence for a further, disease-specific inflammatory signaling cascade remains preliminary. [121][122][146][80]

**Evidence convention:** “Human” denotes patients or their skin; “in vitro” denotes experimental cell or epidermal cultures; “computational” denotes pathway or drug-prediction analyses. Percentages derived from ontology aggregators are **not** treated as measured patient frequencies.

## 1. Disease information

| Identifier or name | KLICK syndrome entry or interpretation |
|---|---|
| MONDO | **MONDO:0011169**. [300] |
| OMIM phenotype | **601952**; the causal *POMP* gene is **OMIM 613386**. [24][108] |
| Orphanet | **ORPHA:281201**. [146] |
| ICD-11 | **EC20.0Y**, as mapped by KEGG; this is a keratinization-disorder code, not a uniquely named KLICK code. [296] |
| ICD-10 | No verified **KLICK-specific** code identified. **Q80.8**, “other congenital ichthyosis,” is a broader potential coding category, not an exact synonym. [330][339] |
| MeSH / MedGen | MeSH supplementary concept **C566600**; MedGen concept **C1866029**. [296][300] |
| Other | KEGG disease **H00790**; SNOMED CT **763775000**. [296][1] |
| Names | “Keratosis linearis with ichthyosis congenita and sclerosing keratoderma”; “keratosis linearis–ichthyosis congenita–sclerosing keratoderma syndrome”; **KLICK syndrome**. [146][300] |
| Evidence provenance | This entry synthesizes **published individuals and families, patient biopsies, experimental models, and aggregated disease resources**. It is **not** an individual-patient EHR record. [121][122][146] |

The original 1989 report described four affected members of a consanguineous family; the 1997 report introduced “KLICK” and described a 32-year-old man without systemic involvement. The discovery study examined DNA from eight European probands. [181][151][121]

## 2. Etiology: causal, risk, protective, and environmental factors

**Established cause:** biallelic germline *POMP* c.-95delC, a **noncoding regulatory deletion**, rather than a protein-truncating mutation. In the original series, 12 patients from eight European families were homozygous; six available parents were heterozygous, and five unaffected siblings tested were carriers or noncarriers. Several affected haplotypes support a **recurrent variant**, rather than one demonstrated founder chromosome. [121][125][135]

**Risk factors:** having two pathogenic alleles is the established genetic risk. A family history and consanguinity increase the chance of such a recessive genotype within a family, but consanguinity is **not required**: affected unrelated families and a later family with non-consanguineous parents have been reported. No validated KLICK susceptibility loci or severity-modifier genes have been established. A reported combination of KLICK and woolly hair/hypotrichosis was attributed to **two separate recessive disorders**, not proof that the hair-disorder gene modifies KLICK. [181][125][145][43]

**Protective and gene–environment factors:** no protective human allele, preventive diet, toxin exposure, infection, lifestyle determinant, or demonstrated gene–environment interaction has been established. Mechanical effects of established hyperkeratosis may contribute to digital constriction; this is a consequence of the skin disorder, not evidence that friction causes KLICK. [121][269]

## 3. Phenotypes

The table separates **reported disease features** from suggested HPO coding. Qualitative frequency is deliberately conservative: small case series do not justify patient-level percentages. A secondary phenotype aggregator labels ichthyosis and palmoplantar keratoderma “80–99%,” but supplies no corresponding observed-case denominator; those labels should **not** be entered as measured frequencies. [web:4nCoJaX02N7jbUnYFD4vhaVy][181][146]

| Phenotype and type | Onset, severity, course, and defensible frequency | Functional or quality-of-life effect | Suggested HPO term |
|---|---|---|---|
| **Ichthyosiform scaling**, clinical sign | Often **congenital**; generalized or variably mild scaling; chronic. **Characteristic**, without a reliable percentage. [181][146][43] | Visible scaling and continuing skin care may be burdensome; no KLICK-specific validated quality-of-life score was identified. [80] | Ichthyosis **HP:0008064**; use more specific subtypes only when documented. [web:4nCoJaX02N7jbUnYFD4vhaVy] |
| **Palmoplantar keratoderma**, clinical sign | Congenital or develops in early childhood; diffuse, sometimes sclerosing and functionally severe; persistent. **Characteristic**, unquantified. [181][192][151] | Thick, stiff skin and associated deformity can impair hand and foot function. [80] | Palmoplantar keratoderma **HP:0000982**; diffuse palmoplantar hyperkeratosis **HP:0007447** when appropriate. [198][197] |
| **Linear keratotic papules and plaques**, clinical sign | Typically symmetric, cord-like flexural lesions at wrists, antecubital or popliteal folds; plaques may affect other sites. **Characteristic but not obligatory**; one family report noted that typical flexural papules were not always present. [146][145] | Visible lesions and thickened skin may affect comfort and daily care; effect has not been quantified separately. [146] | Linear arrays of macular hyperkeratoses in flexural areas **HP:0007490**; hyperkeratotic papule **HP:0045059** where applicable. [web:4nCoJaX02N7jbUnYFD4vhaVy][246] |
| **Digital sclerosis, constriction bands, pseudoainhum, flexural deformity**, physical manifestations | Can become conspicuous in childhood or later; severity varies and may restrict movement. **Characteristic**, without a trustworthy frequency or KLICK-specific progression rate. [151][146][43] | Hand use and mobility may be impaired; assess threatened digits clinically. [80] | Flexion contracture of digit **HP:0030044** if present. Describe **pseudoainhum in free text**: HPO **HP:0009775** means *amniotic* constriction ring and should not automatically be used for keratoderma-related bands. [247][250][277] |
| **Hyperkeratosis, acanthosis, hypergranulosis, sometimes parakeratosis and enlarged keratohyaline granules**, biopsy signs | Findings in lesional epidermis; prevalence across patients **unknown**. Sparse upper-dermal inflammatory infiltrates have also been described. [80][337] | These are diagnostic tissue findings, not independently measured patient-reported outcomes. | Hyperkeratosis **HP:0000962**; epidermal acanthosis **HP:0025092**; hypergranulosis **HP:0025114**; parakeratosis **HP:0001036** when observed. [246][242][web:4nCoJaX02N7jbUnYFD4vhaVy] |
| **Erythema or atypically placed plaques**, variable clinical signs | Reported in some individuals; a **2024 clinically diagnosed but genetically unconfirmed** boy had symmetric extensor-foot plaques. These are not universal defining findings. [80][43] | Not separately measured. | Code the observed erythema or plaque morphology individually; do not generalize from one case. |
| **Nail or dental abnormalities**, occasional findings | Described inconsistently; normal hair, nails, teeth, and hearing have also been documented. Their absence does not exclude KLICK. [80][43][337] | Not established. | Nail dystrophy **HP:0008404** only if actually present. [web:4nCoJaX02N7jbUnYFD4vhaVy] |

No characteristic behavioral or psychiatric phenotype, systemic laboratory abnormality, or electrophysiologic phenotype has been demonstrated for KLICK. The characteristic disorder is predominantly **cutaneous**; do not transfer immunodeficiency or systemic autoinflammation findings from other *POMP*-related diseases to KLICK. [80][296]

## 4. Genetic and molecular information

| Field | Knowledge-base annotation |
|---|---|
| Causal gene | ***POMP***, proteasome maturation protein; **HGNC:20330**, NCBI Gene **51371**, Ensembl **ENSG00000132963**, OMIM **613386**; chromosome **13q12.3**. [106][46][108] |
| Established KLICK allele | **NM_015932.5:c.-95delC**, **rs112368783**, ClinVar variation **116 / VCV000000116**, OMIM allelic variant **613386.0001**. ClinVar’s GRCh38 expression is **NC_000013.11:g.28659090del**. Specify transcript and genome build when recording coordinates. [web:6g8nEzSiusklPoXtMf9sE4Zs] |
| Classification and origin | **Pathogenic germline** deletion. ClinVar’s KLICK-specific record **RCV000000136** is pathogenic but its OMIM assertion has **no assertion criteria provided**; the overall *variant-level* record has additional concordant submissions. [web:6g8nEzSiusklPoXtMf9sE4Zs] |
| Population frequency | The ClinVar page quotes approximately **0.01%** in gnomAD and **0.013% of European non-Finnish alleles** in a submitter comment. These are quoted submitter figures, **not** an independently verified current release-wide carrier-frequency estimate. The discovery report found no deletion in **280 Swedish control chromosomes**. [web:6g8nEzSiusklPoXtMf9sE4Zs] |
| Functional consequence | Shift toward longer *POMP* 5′-UTR transcripts in patient keratinocytes, with reduced effective POMP expression in differentiating epidermis and altered proteasome-subunit distribution: **regulatory hypomorphic effect**, not a coding frameshift. [121][122] |
| Important boundary | Heterozygous truncating *POMP* variants are associated with a **distinct immune-dysregulatory syndrome**; other *POMP* variants appearing in disease aggregators must not automatically be annotated as KLICK-causing. [80][132][254] |

No KLICK-specific pathogenic chromosomal rearrangement, somatic driver, modifier gene, disease-specific DNA-methylation signature, or histone-change signature has been established in the cited evidence. [121][80]

## 5. Environmental information

KLICK is **not an infectious disease**. No implicated pathogen, toxin, radiation exposure, occupation, smoking pattern, alcohol exposure, or diet has been identified as a cause or reproducible trigger. Skin care and physical stress can matter to **symptom management**, but they should not be recorded as proven etiologic exposures or gene–environment interactions. [121][146][43]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Homozygous *POMP* c.-95delC leads to** a shift toward longer 5′-UTR transcripts in patient keratinocytes; this upstream change was observed in human material. [121]
2. **The transcript shift leads to** reduced effective POMP availability during terminal keratinocyte differentiation; altered patient-skin staining and knockdown experiments support this connection. [121][122]
3. **Reduced POMP leads to** impaired maturation or availability of proteasomes, with altered epidermal α7 and β5 subunit distribution; patient staining and *POMP*-silenced cultures support this step. [121][122]
4. **Proteasome insufficiency leads to two overlapping downstream branches:** **(a)** disturbed profilaggrin processing and epidermal differentiation; **(b)** increased ER stress and unfolded-protein-response markers, including CHOP. These branches are supported experimentally, although their exact causal order and contribution in each patient are **not fully demonstrated**. [122]
5. **Disordered differentiation leads to** hyperkeratosis, scaling, thick palmoplantar skin, and keratotic flexural lesions; this clinicopathologic link is strongly supported, but the exact mechanism producing each lesion’s distribution remains **inferred**. [121][122][146]
6. **Thickening and sclerosis of acral skin lead to** constricting digital bands and functional deformity; their clinical co-occurrence is established, while a complete tissue-level account of band formation remains **inferred**. [181][151][80]
7. **Possible inflammatory branch:** chronic epidermal stress **may lead to** local inflammatory signaling and upper-dermal infiltrates. The infiltrates are observed; a causal, KLICK-specific type-I-interferon or innate-immune pathway has **not** been established. Single-patient 2023 transcriptomics subsequently implicated interferon and other inflammatory pathways, which remains hypothesis-generating. [80][web:Tf1ZaGLHBmtWAOFIPhrk7u7I]

**Experimental detail.** In 2012, *POMP* siRNA in human air–liquid-interface epidermal cultures reduced *POMP* transcripts by about **54%** and produced abnormal POMP, α7, and filaggrin staining resembling patient biopsies. Cultures showed altered profilaggrin cleavage; prolonged knockdown induced CHOP in cultured cells. This is an **in-vitro approximation**, not a precise recreation of the human regulatory deletion. The authors concluded that reduced POMP causes “**proteasome insufficiency in differentiating keratinocytes**.” PMID **22235297**. [122]

**Recent molecular profiling.** Two 2023–2024 conference abstracts describe analyses centered on a biopsy from a **32-year-old woman**, not a large cohort. Immunostaining showed early involucrin/loricrin expression and retained corneal loricrin; RNA sequencing implicated differentiation, cornification, interferon-related, WNT, and EGFR pathways. The 2024 abstract additionally reports hyperkeratosis, hypergranulosis, delayed cellular flattening, and upregulated epidermal-development pathways. Pathway enrichment shows **association**, not that EGFR, WNT, PI3K, or interferon signaling is an initiating lesion. No KLICK-specific proteomic, metabolomic, lipidomic, single-cell, or spatial-transcriptomic signature was established in these reports. [web:Tf1ZaGLHBmtWAOFIPhrk7u7I][web:D3ONl5rWbzCOhp8RZ9J0LKCn]

**Suggested annotations:** POMP’s established biological role maps to proteasome assembly **GO:0043248**; downstream processes can be annotated as ER unfolded-protein response **GO:0030968**, keratinocyte differentiation **GO:0030216**, and epidermis development **GO:0008544**. The principal cell type is keratinocyte **CL:0000312**. KEGG proteasome pathway **hsa03050** is relevant. These are **term suggestions**, not claims that every branch has been causally validated in KLICK. [219][311][315][212][web:OBwZDlDrUUCwK4OoTkS8VFYr]

## 7. Anatomical structures affected

The principal organ is **skin**: especially palmoplantar skin, finger and toe skin, wrists, and flexural skin around large joints. Lesions are often **bilaterally symmetric**, though severity and location can vary. The key tissue is stratified **epidermal epithelium**, particularly differentiating granular and cornified layers; sparse inflammatory cells may occur in the superficial **dermis**. There is no reproducibly established primary internal-organ lesion. [146][80][43]

Suggested anatomy codes are **skin epidermis UBERON:0001003**, **stratum granulosum UBERON:0002069**, and **dermis UBERON:0002067**; principal cell **keratinocyte CL:0000312**. The implicated subcellular machinery comprises proteasome precursors and ER-associated stress responses; proteasome component **GO:0000502** can be considered for the complex. The clinical reports do not establish a primary mitochondrial or lysosomal defect. [213][217][212][108][122]

## 8. Temporal development

Scaling can begin **at birth**; keratoderma and distinctive plaques become recognizable during childhood, and digital changes can remain or become more consequential over time. The course is **chronic**, not episodic or relapsing-remitting; formal early/intermediate/end-stage criteria and a measured progression rate are unavailable. In one reported patient, acitretin improved skin disease during ages **8–18**, symptoms worsened after withdrawal, and improvement followed restarting treatment—evidence for **symptom recurrence**, not cure or a defined remission pattern. No established critical intervention window or longitudinal natural-history cohort was found. [181][192][337][web:DbOxl2jVYciByL4D8NA19q5j]

## 9. Inheritance and population

**Inheritance is autosomal recessive.** For two confirmed heterozygous parents, standard Mendelian counseling gives a **25% affected, 50% carrier, and 25% noncarrier probability per pregnancy**. Penetrance is not reliably quantified; expressivity varies in lesion distribution and severity. No evidence establishes anticipation, germline mosaicism, or a population-specific founder effect. The discovery families came from Spain, Italy, the Netherlands, Sweden, and Norway; this is **case ascertainment**, not a geographic prevalence map or sex-ratio estimate. [121][125][145]

A **2014 French capture–recapture study** recorded **two** KLICK patients and estimated **0.23 per million people**—**0.023 per 100,000**—with a reported **95% CI of 0.19–0.30 per million**. Its regional sampling and two observed cases make that estimate unsuitable as a precise current global prevalence. **Incidence, carrier frequency, sex ratio, and population age distribution are unknown.** PMID **24393603**. [web:l8hwjUlxLNP95I2ckj2kB2E9][web:XLIpeecMmc7bsWpaMAssV2mA][166]

## 10. Diagnostics

**Clinical approach:** suspect KLICK when congenital scaling coexists with diffuse palmoplantar keratoderma, linear flexural keratoses, and digital sclerosis or pseudoainhum. Examine skin distribution, digital movement and constrictions, nails, hair, hearing, and family history; biopsy can show acanthosis, hypergranulosis, hyperkeratosis, abnormal keratohyaline granules, and sometimes parakeratosis. Histology supports but does **not** independently establish the molecular diagnosis. There are no validated KLICK-specific blood, urine, enzyme, circulating, imaging, electrophysiologic, or functional biomarkers. Imaging may be clinically useful for a severely affected digit, but is not a routine confirmatory KLICK test. [181][337][80][43]

**Confirmatory genetic approach:** test for **biallelic *POMP* c.-95delC with explicit 5′-UTR coverage and deletion calling**, followed by parental segregation testing where possible. Targeted variant testing is efficient for a classic presentation; a palmoplantar-keratoderma or ichthyosis panel that demonstrably covers this **noncoding** position is useful for broader differentials. WGS may help if the result is unresolved and covers the site; WES or an exon-only panel may miss it. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion assays are **not** first-line confirmatory tests for this one-base regulatory deletion. RNA sequencing is research-useful, not a validated clinical diagnostic requirement. Genomics England lists *POMP* on relevant panels and flags the noncoding allele. [web:6g8nEzSiusklPoXtMf9sE4Zs][web:hxtT0cGAbBRZFmp1k1sc18df][121]

**Differential:** other inherited ichthyoses and mutilating palmoplantar keratodermas, including loricrin/Vohwinkel-spectrum disease; evaluate genetic results and accompanying features rather than assuming that ichthyosis plus constriction bands identifies KLICK. Also distinguish recessive KLICK from the **different**, often systemic phenotype of heterozygous truncating *POMP* variants. No validated population newborn-screening program or KLICK-specific clinical diagnostic scoring criteria were identified. [203][80][192]

## 11. Outcome and prognosis

Cutaneous morbidity can be substantial, particularly where stiff keratoderma and digital constriction impair function. The 1997 case and later descriptions did **not** establish a characteristic systemic illness or reduced life expectancy. **Survival, mortality, life expectancy, formal disability rates, prognostic biomarkers, and KLICK-specific EQ-5D/SF-36/PROMIS results are unavailable.** A **2011 letter reported aggressive cutaneous squamous-cell carcinoma in one KLICK patient**; this establishes an observed case, **not** a measured cancer incidence or proven elevated risk. Clinical attention to new or changing skin lesions is reasonable. [151][80][web:4MK80yHz0MUgrWJs1ZOMahEi]

## 12. Treatment

Treatment evidence consists chiefly of **individual case reports**, not comparative KLICK trials. Suggested NCIT labels below are **intervention concepts to map and verify locally**, not asserted numeric NCIT codes. [151][337][43]

| Intervention and suggested NCIT concept | Evidence, intended role, and limits |
|---|---|
| **Emollients and humectants** — topical emollient therapy | Supportive management of scaling and dryness. A 2024 case used emollients alongside systemic treatment; their isolated KLICK response was not quantified. [43] |
| **Topical urea or other keratolytics** — topical keratolytic therapy; urea | Used to reduce thick scale; **30% urea cream** was reported in clinical care. No controlled response or adverse-event rate is available for KLICK. [43][36] |
| **Oral acitretin** — systemic retinoid therapy; acitretin | Case experience reports improvement, including after re-initiation following worsening off treatment. A 2024 boy received **25 mg/day**, but that report did **not** quantify his response and did **not** genetically confirm KLICK. Assess systemic-retinoid risks and contraindications individually; no KLICK-specific optimal dose or response rate is established. [web:DbOxl2jVYciByL4D8NA19q5j][43] |
| **Oral etretinate** — systemic retinoid therapy; etretinate | The 1997 primary case abstract reports that disease “**improved on oral etretinate therapy**.” This is case evidence, not a comparative efficacy estimate. PMID **9188877**. [151] |
| **Digit assessment and functional support** — dermatologic assessment; rehabilitative therapy | Individualized clinical management of painful, function-threatening constrictions and impaired hand or foot function is reasonable. No validated KLICK-specific surgical algorithm, operation outcome, or rehabilitation trial was identified. [80][146] |
| **Erlotinib / EGFR inhibition; PI3K inhibition** — targeted therapy **research candidates only** | A 2024 **computational reverse-transcriptomics** analysis shortlisted erlotinib; a 2023 abstract also proposed EGFR and PI3K inhibition. Neither abstract establishes treatment efficacy or safety in a KLICK patient. [web:D3ONl5rWbzCOhp8RZ9J0LKCn][web:Tf1ZaGLHBmtWAOFIPhrk7u7I] |
| **Anti-cytokine treatment or proteostasis-directed therapy** — investigational interventions only | Discussed as hypotheses by experts, **not demonstrated KLICK therapies**. A registered study **NCT04996485** concerns broader congenital ichthyosis; its listing is not evidence of KLICK-specific enrollment or benefit. [80][298] |

No established KLICK gene therapy, cell therapy, RNA therapy, immunotherapy, genotype-specific pharmacogenomic rule, licensed targeted treatment, or comparative combination-treatment algorithm was identified. [80][web:D3ONl5rWbzCOhp8RZ9J0LKCn]

## 13. Prevention

**Primary prevention of the mutation through lifestyle or vaccination is not applicable.** Reproductive genetic counseling can explain recessive risk and discuss carrier testing of relatives and, where appropriate, prenatal or preimplantation testing for the **known familial variant**. **Secondary prevention** consists of timely clinical recognition and confirmatory testing in symptomatic relatives, with targeted family testing as appropriate; no population newborn-screening program is established. **Tertiary prevention** focuses on skin care, monitoring constricting digits and function, and assessment of concerning new lesions. No KLICK-specific vaccine, chemoprophylaxis, environmental intervention, or risk-prediction model has been established. [121][web:6g8nEzSiusklPoXtMf9sE4Zs][80][web:4MK80yHz0MUgrWJs1ZOMahEi]

## 14. Other species and naturally occurring disease

The genetically established **natural disease** described here is human (**NCBI Taxon:9606**). The mouse (**NCBI Taxon:10090**) has a *Pomp* ortholog, **NCBI Gene:66537**, but orthology is **not** evidence of naturally occurring veterinary KLICK. No confirmed companion-animal breed or VBO entry, spontaneous nonhuman KLICK disease, zoonotic potential, cross-species transmission, or comparative natural-disease prevalence was identified. Proteasome assembly is conserved, but the specific human clinical phenotype cannot be assigned to another species solely from that conservation. [116][112][122]

## 15. Model organisms and experimental systems

| Model type and system | Demonstrated recapitulation, use, and limitation |
|---|---|
| **In-vitro human epidermal air–liquid culture with *POMP* siRNA** | Reproduced aspects of patient POMP/proteasome/filaggrin staining and disturbed profilaggrin processing. Useful for testing proteasome insufficiency and differentiation; knockdown is **not** the patient’s exact c.-95delC allele, and cultures cannot reproduce whole-person digital deformity. PMID **22235297**. [122] |
| **In-vitro HaCaT keratinocytes and HeLa comparison cultures with *POMP* knockdown** | Supported reduced proteasome-subunit abundance and CHOP induction with prolonged depletion; cell-line results cannot establish patient-level natural history or treatment response. PMID **22235297**. [122] |
| **CRISPR-edited HaCaT cells carrying the KLICK allele** | Reported as successfully generated in a **2024 conference abstract**; a genotype-matched experimental platform, **not yet evidence** that a candidate drug works. [web:D3ONl5rWbzCOhp8RZ9J0LKCn] |
| **Patient-derived induced pluripotent stem-cell line** | Reported generated in the same **2024 abstract** for prospective disease modeling. No differentiated-organism phenotype or drug-response result was reported there. [web:D3ONl5rWbzCOhp8RZ9J0LKCn] |
| **KLICK-specific mouse or other whole-animal knock-in model** | **Not established in the retrieved KLICK studies.** A mouse *Pomp* ortholog exists, but an ortholog or a model of another inflammatory disorder must not be represented as a KLICK phenocopy. MGI is an appropriate resource for checking future alleles. [80][112][161] |

### Primary-source anchors and exact abstract excerpts

| Publication date | PMID and URL | Exact supporting abstract excerpt and evidence type |
|---|---|---|
| **January 1989** | **2521286** — https://pubmed.ncbi.nlm.nih.gov/2521286/ | “**Four members of a consanguineous family showed a congenital disorder characterized by an ichthyosiform dermatosis, sclerosing palmoplantar keratoderma, and multiple keratotic papules arranged in bands with a linear, cordlike distribution.**” **Human clinical.** [181] |
| **May 1997** | **9188877** — https://pubmed.ncbi.nlm.nih.gov/9188877/ | “**The condition, which improved on oral etretinate therapy, had not appeared previously in the family.**” **Human clinical, single case.** [151] |
| **9 April 2010** | **20226437** — https://pubmed.ncbi.nlm.nih.gov/20226437/ | “**Sequence analysis of the ten annotated genes in the candidate region revealed homozygosity for a single-nucleotide deletion at position c.-95 in the proteasome maturation protein (POMP) gene, in all probands.**” **Human genetic and biopsy research.** [web:nnNpUmDlV0JUFMameO0eW531][134] |
| **3 January 2012** | **22235297** — https://pmc.ncbi.nlm.nih.gov/articles/PMC3250448/ | “**The combined results indicate that KLICK is caused by reduced levels of POMP, leading to proteasome insufficiency in differentiating keratinocytes.**” **In vitro**, compared with human biopsies. [122] |
| **6 January 2014** | **24393603** — https://ojrd.biomedcentral.com/articles/10.1186/1750-1172-9-1/tables/5 | The study’s disease table records **“KLICK syndrome \| 2 (1.7) \| 0.23 [0.19 – 0.30]”**, with prevalence per million. **Population study**, based on two recorded KLICK cases. [web:l8hwjUlxLNP95I2ckj2kB2E9][166] |
| **7 July 2023** | **No PMID verified** — https://academic.oup.com/bjd/article/189/1/e21/7221241 | “**RNA sequencing revealed dysregulated pathways relating to keratinocyte differentiation, keratinization, cornification, and interferon signalling.**” **Single-patient biopsy and transcriptomics; conference abstract.** [web:Tf1ZaGLHBmtWAOFIPhrk7u7I] |
| **17 May 2024** | **No PMID verified** — https://academic.oup.com/bjd/article/190/6/e78/7675832 | “**HaCaT keratinocytes were successfully edited using CRISPR-Cas9 to carry the KLICK patient POMP variant and a KLICK patient iPSC line was generated**.” **Cell-model and computational research; conference abstract.** [web:D3ONl5rWbzCOhp8RZ9J0LKCn] |

**Knowledge-base caution:** annotate *POMP* c.-95delC and the characteristic skin phenotype as established; annotate specific inflammatory cascades, repurposed EGFR inhibitors, long-term outcomes, and animal phenocopy claims as **unproven or not available**. [121][122][80][web:D3ONl5rWbzCOhp8RZ9J0LKCn]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Taxon`, `Gene`.

22 of 27 terms resolved to a current term; the rest could not be looked up either way.