---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-23T15:48:34.132785'
end_time: '2026-10-23T15:52:43.493678'
duration_seconds: 249.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Alacrima, Achalasia, and Intellectual Disability Syndrome
  mondo_id: MONDO:0014219
  category: Mendelian
  causal_genes: GMPPA
  omim_id: OMIM:615510
  synonyms: alacrima, achalasia, and mental retardation syndrome
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 50
reference_validation:
  total_references: 25
  verified: 24
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.04
  relevance_assessed: 24
  on_topic: 13
  off_topic: 1
  off_topic_references:
  - DOI:10.3389/fped.2021.715151
  unresolved_references:
  - DOI:10.1093/gastro/goaf083/8259572
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 78
  verified: 63
  not_found: 0
  obsolete: 1
  unverifiable: 14
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014219
    reported_labels:
    - MONDO
    ontology_label: alacrima, achalasia, and intellectual disability syndrome
  - term_id: DOID:0112321
    reported_labels:
    - Disease Ontology
    ontology_label: alacrima, achalasia, and impaired intellectual development syndrome
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  unresolvable_prefixes:
  - OMIM
  - Gene
  - ORPHA
  - NC_000002.12
  - Taxon
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alacrima, Achalasia, and Intellectual Disability Syndrome
- **MONDO ID:** MONDO:0014219 (if available)
- **Causal gene(s):** GMPPA
- **OMIM:** OMIM:615510
- **Synonyms:** alacrima, achalasia, and mental retardation syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Alacrima, Achalasia, and Intellectual Disability Syndrome** covering all of the
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

# Research report: Alacrima, Achalasia, and Intellectual Disability Syndrome  
**Disease identifiers:** MONDO:0014219; OMIM:615510  
**Causal gene:** ***GMPPA*** (HGNC:22923; NCBI Gene:29926; OMIM:615495), chromosome 2q35

## Executive summary

Alacrima, achalasia, and intellectual disability syndrome is an ultra-rare, autosomal-recessive congenital disorder of glycosylation caused by **biallelic germline pathogenic variants in *GMPPA***. It is also called **GMPPA-CDG**, AAMR syndrome, or alacrima-achalasia-impaired intellectual development syndrome. The characteristic presentation is congenital or early-infantile alacrima, achalasia with feeding difficulty, and developmental delay/intellectual disability, usually without adrenal insufficiency. The most recent systematic review, published July 18, 2025, assembled 26 molecularly confirmed patients; all 26 had alacrima, achalasia, and developmental delay. [40]

Mechanistically, GMPPA is not the principal catalytic GDP-mannose-producing enzyme. Rather, it binds GDP-mannose, interacts with GMPPB, and functions as a **GDP-mannose-dependent allosteric feedback inhibitor of GMPPB**. Loss of GMPPA therefore increases GDP-mannose and causes excessive incorporation of mannose into selected glycoconjugates, including α-dystroglycan. This is unusual among congenital disorders of glycosylation because the defect involves **hyperglycosylation/dysregulated glycosylation**, rather than a simple shortage of glycan synthesis. Human muscle biopsies and *Gmppa*-knockout mice show α-dystroglycan hyperglycosylation, reduced α-dystroglycan abundance, extracellular-matrix disorganization, myopathy, and neurological abnormalities (PMID:33755596). [46]

---

## 1. Disease information

### 1.1 Definition

GMPPA-CDG is a congenital multisystem disease affecting autonomic functions, neurodevelopment, swallowing, tear production, growth, and—variably—skeletal muscle, hearing, vision, and ectodermal structures. Onset is generally at birth or in the first year of life. Unlike *AAAS*-related triple-A/Allgrove syndrome, adrenal insufficiency has not been a feature in molecularly confirmed GMPPA-CDG. [18][42]

A key 2013 discovery paper stated:

> “Mutations in *GMPPA* were subsequently found in ten additional individuals from eight independent families affected by the combination of achalasia, alacrima, and neurological deficits.”  
> —Koehler et al., *American Journal of Human Genetics*, October 3, 2013; PMID:24035193. [61][63]

### 1.2 Identifiers and nomenclature

| Resource | Identifier/name | Interpretation |
|---|---|---|
| MONDO | **MONDO:0014219** | Alacrima, achalasia, and intellectual disability syndrome |
| OMIM disease | **615510** | Alacrima, achalasia, and impaired intellectual development syndrome; AAMR |
| OMIM gene | **615495** | GDP-mannose pyrophosphorylase A; *GMPPA* |
| HGNC | **HGNC:22923** | *GMPPA* |
| NCBI Gene | **29926** | Human *GMPPA* |
| MedGen | **C4706563** | Alacrima, achalasia, and intellectual disability syndrome |
| Disease Ontology | **DOID:0112321** | Alacrima, achalasia, and impaired intellectual development syndrome |
| ICD-10/ICD-11 | No specific validated disease-level code identified | Manifestations may be coded individually, such as achalasia, lacrimal disorder, developmental disorder, or CDG |
| MeSH | No disease-specific descriptor identified | Broader terms include congenital disorders of glycosylation, achalasia, alacrima, and intellectual disability |

The MONDO record explicitly links MONDO:0014219 to *GMPPA* and OMIM:615510. [15]

### 1.3 Important Orphanet curation problem

A reliable disease-specific Orphanet mapping could not be confirmed. **ORPHA:869 is triple-A/Allgrove syndrome**, principally associated with *AAAS*, and should not be used as if it were a specific identifier for GMPPA-CDG. [153] **ORPHA:289483** is an older “intellectual disability-alacrima-achalasia syndrome” record linked by OMIM to X-linked syndromic intellectual disability 17 rather than definitively to *GMPPA*. [154][157] For a knowledge base, MONDO:0014219 and OMIM:615510 are the safer disease identifiers.

### 1.4 Synonyms

- GMPPA-congenital disorder of glycosylation  
- GMPPA-CDG  
- AAMR syndrome  
- Alacrima, achalasia, and mental retardation syndrome—the historical term  
- Alacrima, achalasia, and impaired intellectual development syndrome  
- Alacrima-achalasia-intellectual disability syndrome  
- GDP-mannose pyrophosphorylase A deficiency

### 1.5 Evidence provenance

The evidence is mostly **aggregated disease-level information** derived from:

- Published case reports and small case series;
- The 2013 multicenter discovery cohort;
- A 2025 review of 23 published patients plus three participants in the Frontiers in Congenital Disorders of Glycosylation Consortium natural-history database, NCT04199000;
- Human fibroblast, lymphoblast, and muscle-biopsy experiments;
- Mouse and in-vitro disease models.

The natural-history patients reflect prospectively collected research data, not population-scale EHR evidence. No large epidemiological or administrative-database cohort exists.

---

## 2. Etiology

### 2.1 Primary causal factor

The disease is caused by **biallelic pathogenic or likely pathogenic germline variants in *GMPPA***. The molecular disease mechanism is loss of GMPPA regulatory function, resulting in inadequate feedback inhibition of GMPPB and excess GDP-mannose production. ClinGen’s Congenital Disorders of Glycosylation expert curation classified the *GMPPA*–MONDO:0014219 relationship as **definitive** on September 6, 2023. It cited approximately 20 known patients at that time and concluded that loss of function is the pathogenic mechanism. [33][34]

### 2.2 Genetic risk factors

| Factor | Evidence and interpretation |
|---|---|
| Biallelic pathogenic *GMPPA* variants | Necessary and sufficient cause in documented Mendelian families |
| Homozygosity | Common in affected children of consanguineous parents |
| Compound heterozygosity | Documented in nonconsanguineous families, including c.874A>C (p.Thr292Pro) and c.952C>T (p.Arg318Trp) in one infant, initially reported as VUS but clinically concordant [124] |
| Family history | Each full sibling of an affected individual has a 25% recurrence risk when both parents are heterozygous carriers |
| Founder ancestry | c.265dup, p.Leu89fs was reported homozygously in three patients from two unrelated Maya-Mam families from Concepción Chiquirichapa, Guatemala, consistent with a founder allele (PMID:31898852) [113] |
| Consanguinity | Increases the probability that both parents carry the same rare allele; it does not itself alter the molecular mechanism |
| Uniparental disomy | A 2025 case indicates that uniparental disomy can provide an unusual route to homozygosity, but this is not the usual inheritance mechanism [64] |

### 2.3 Environmental and lifestyle risk factors

No toxin, infection, radiation exposure, diet, smoking, alcohol, occupation, sex, or lifestyle factor has been shown to cause GMPPA-CDG. Environmental exposures could modify complications—for example, low humidity may worsen ocular-surface disease and feeding practice may alter aspiration risk—but these are not causes of the Mendelian disorder.

### 2.4 Protective factors and gene–environment interaction

No human protective allele or validated modifier gene is known. In *Gmppa*-knockout mice, reducing dietary free mannose beginning at postnatal day 14 normalized much of the biochemical and neuromuscular phenotype. It did not correct abnormal cortical layering or contextual-learning impairment, implying a developmental window during which irreversible CNS abnormalities may arise. This is strong model-organism evidence for a nutrient–gene interaction, but it is **not proof that dietary mannose restriction is safe or effective in humans**. [49][54]

No controlled human study has demonstrated that dietary mannose restriction, mannose-rich-food avoidance, or another lifestyle intervention protects against disease.

---

## 3. Phenotypes

### 3.1 Best current frequency estimates

The most complete dataset contains 26 molecularly confirmed patients, aged 9 months to 47 years, comprising 9 males and 17 females. Ascertainment and missing-data bias are substantial because most observations come from case reports. [40]

| Phenotype/type | Frequency in 2025 review | Onset/course and severity | Functional or quality-of-life impact | Suggested HPO term |
|---|---:|---|---|---|
| Alacrima, clinical sign | 26/26, 100% | Congenital or early infancy; persistent; may range from markedly reduced tears to complete absence | Dryness, irritation, keratitis, corneal vascularization, scarring, perforation, and potential visual loss | **HP:0000522 Alacrima** |
| Achalasia, digestive/autonomic sign | 26/26, 100% | Usually infancy; reported onset from birth to childhood; chronic without intervention | Dysphagia, vomiting, regurgitation, failure to thrive, aspiration pneumonia, tube feeding or surgery | **HP:0002571 Achalasia** |
| Developmental delay | 26/26, 100% | Infancy; persistent | Delayed mobility, communication, learning, adaptive function | **HP:0001263 Global developmental delay** |
| Intellectual disability | 22 reported; missing in four | Usually moderate but variable; lifelong | Dependence in education, communication, employment, and daily living | **HP:0001249 Intellectual disability** |
| Severe speech delay/absent speech | Most described patients; exact denominator incomplete | Childhood; often severe and persistent | Major communication limitation; augmentative communication may be required | **HP:0000750 Delayed speech and language development; HP:0001344 Absent speech** |
| Impaired growth/short stature or failure to thrive | 11/12 with available growth data, 91%; short stature in 10 | Infancy to childhood; multifactorial and variable | Nutritional vulnerability, reduced stature, treatment burden | **HP:0001508 Failure to thrive; HP:0004322 Short stature** |
| Facial dysmorphism | 8/12 | Congenital; variable, no consistent gestalt | Usually limited direct functional effect | **HP:0001999 Abnormal facial shape** |
| Hypotonia | 10/21 | Neonatal or early childhood; variable; sometimes stable | Delays motor milestones and may compound swallowing and gait difficulty | **HP:0001252 Hypotonia** |
| Gait abnormality—ataxia or spasticity | 7/17 | Childhood onward; may progress through neuromuscular involvement | Reduced mobility and fall risk | **HP:0001288 Gait disturbance; HP:0001251 Ataxia; HP:0001257 Spasticity** |
| Hearing loss | 6/17 | Variable | Worsens speech, learning, and communication | **HP:0000365 Hearing impairment** |
| Postural hypotension | 5/17 | Childhood/adulthood; autonomic | Dizziness, syncope risk, reduced activity | **HP:0001278 Orthostatic hypotension** |
| Hypohidrosis/anhidrosis | 8/24 | Persistent autonomic/ectodermal sign | Heat intolerance and overheating risk | **HP:0000966 Hypohidrosis; HP:0000970 Anhidrosis** |
| Hyperkeratosis | 4/17 | Variable | Skin discomfort and care burden | **HP:0000962 Hyperkeratosis** |
| Microcephaly | 3/10 | Developmental | Marker of altered neurodevelopment | **HP:0000252 Microcephaly** |
| Anodontia/missing teeth | 2/5 assessed | Developmental | Chewing, speech, nutrition, and dental-prosthetic needs | **HP:0000674 Anodontia** |
| Eye abnormalities | Seven individuals | Nystagmus, anisocoria, esotropia/strabismus, astigmatism | May impair vision and balance | **HP:0000639 Nystagmus; HP:0009916 Anisocoria; HP:0000486 Strabismus** |
| Seizures | 2 patients | Variable; not a core finding | Safety and neurologic treatment burden | **HP:0001250 Seizure** |
| Hyperreflexia | 2/18 | Variable | Marker of upper-motor-neuron dysfunction | **HP:0001347 Hyperreflexia** |
| Abnormal brain MRI | 1/4 | Most imaged patients had normal conventional MRI | Imaging can underestimate cellular/developmental pathology | **HP:0410263 Abnormal brain MRI** |
| Adrenal insufficiency | 0/26 | Not expected | Its presence strongly suggests *AAAS*-related triple-A syndrome or another diagnosis | **HP:0000846 Adrenal insufficiency**, negative finding |

These updated frequencies come from the 2025 review; earlier reports gave achalasia in 15/17, alacrima in 17/17, intellectual disability in 17/17, ocular findings in 11/17, hypotonia in 6/17, and gait abnormalities in 7/17. [45]

### 3.2 Laboratory phenotype

- Intracellular GDP-mannose is markedly elevated in patient lymphoblasts.
- Routine GDP-mannose pyrophosphorylase activity may appear normal because GMPPB remains catalytically active.
- Serum transferrin isoelectric focusing and tested serum N-glycan profiles are generally normal.
- Apo-CIII glycosylation and serum-protein N-glycans were not clearly abnormal in the original cohort.
- Serum creatine kinase was normal in knockout mice despite myopathy; no validated circulating muscle biomarker has been established in humans.

Thus, a normal transferrin glycosylation screen **does not exclude** GMPPA-CDG.

### 3.3 Quality of life

No disease-specific EQ-5D, SF-36, PROMIS, or formal caregiver-burden study has been published. Likely major determinants include:

1. Dysphagia, aspiration risk, repeated procedures, and nutritional support;
2. Severe communication and cognitive disability;
3. Chronic ocular discomfort and threat to sight;
4. Mobility impairment and muscle weakness;
5. Hearing and visual deficits;
6. Need for lifelong multidisciplinary and caregiver support.

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Property | Value |
|---|---|
| Gene | ***GMPPA*** |
| Full name | GDP-mannose pyrophosphorylase A / mannose-1-phosphate guanylyltransferase regulatory subunit alpha |
| HGNC | **22923** |
| NCBI Gene | **29926** |
| OMIM gene | **615495** |
| Ensembl | **ENSG00000144591** |
| UniProt | **Q96IJ6** |
| Location | **2q35**, GRCh38 chromosome 2 approximately 219.50 Mb |
| Protein size | 420 amino acids for the principal reference protein |
| Broad compartment | Cytosol/cytoplasm |
| Protein role | Regulatory, catalytically inactive paralogue and feedback inhibitor of GMPPB |

NCBI places the protein-coding gene at 2q35 and gives GRCh38 coordinates NC_000002.12:219,498,891–219,506,989 for the displayed reference interval. [93]

### 4.2 Pathogenic variant spectrum

The 2025 review identified **17 different disease-associated variants** among 26 patients, spanning nonsense, missense, frameshift, deletion, and duplication alleles; it found no genotype–phenotype correlation. [40]

Representative reported variants include:

| HGVS, reference transcript NM_013335.x | Protein consequence | Class/evidence | Functional interpretation |
|---|---|---|---|
| c.295C>T | p.Arg99Ter | Pathogenic; homozygous in three Pakistani siblings | Truncation/no detectable transfected protein; loss of function |
| c.210delA | p.Ala71ProfsTer19 | Pathogenic | Frameshift, premature termination |
| c.642G>A | p.Trp214Ter | Pathogenic | Truncating loss of function [21] |
| c.993+1G>A | Splice consequence not fully defined in original table | Canonical splice variant | Predicted abnormal splicing/loss of function |
| c.1000A>C | p.Thr334Pro | Pathogenic | Reduced GMPPA abundance and interaction/inhibition of GMPPB [121] |
| c.1001C>T | p.Thr334Met | Disease-associated | Missense loss of function |
| c.1202A>C | p.Asn401Thr | Disease-associated | Reduced protein stability/function |
| c.1169G>C | p.Arg390Pro | Disease-associated | Missense loss of function |
| c.545G>A | p.Gly182Asp | Disease-associated | Impaired inhibition of GMPPB |
| c.1118G>C | p.Arg373Pro in the publication | Pathogenic/disease-associated in two adult sisters | Predicted destabilization; low GMPPA in muscle; note inconsistent legacy annotation in the article |
| c.853+1G>A | Splice-site | Disease-associated in two sisters | Achalasia, alacrima, hypohidrosis, seizures, microcephaly and ID [39] |
| c.265dup | p.Leu89fs | Founder pathogenic variant | Homozygous in two Maya-Mam families [113] |
| c.874A>C | p.Thr292Pro | Initially VUS | Compound heterozygous infant; clinical evidence supportive but limited |
| c.952C>T | p.Arg318Trp | Initially VUS | In trans with p.Thr292Pro in the same infant [124] |
| c.637_640dup | p.Trp214fs | ClinVar pathogenic listing | Frameshift loss of function [129] |

Pathogenic alleles are germline, not somatic. Early discovery variants were absent from dbSNP build 137, 1000 Genomes, and the NHLBI Exome Variant Server. Current allele frequencies should be checked variant-by-variant in the current gnomAD release; no common disease-causing allele is known. A rare-variant frequency alone is not sufficient for pathogenicity.

### 4.3 Variant interpretation

Recommended classification should follow ACMG/AMP criteria:

- **PVS1** may apply to bona fide nonsense, frameshift, and essential splice variants expected to cause loss of function;
- **PM2** may apply where absent or extremely rare in population databases;
- **PP1** for segregation in affected relatives;
- **PS3** where validated functional experiments demonstrate loss of GMPPA abundance, GMPPB interaction, or feedback inhibition;
- **PM3** for confirmed in-trans occurrence in recessive disease.

Do not report a patient as molecularly confirmed on the basis of a single heterozygous variant or two VUS without segregation and phenotype-level evidence.

### 4.4 Modifier, epigenetic, and chromosomal findings

- No validated modifier gene has been reported.
- GMPPB activity, dietary mannose availability, glycoprotein turnover, and developmental timing are plausible mechanistic modifiers but are not established human prognostic factors.
- No reproducible disease-specific methylation episignature or chromatin abnormality has been described.
- No recurrent deletion, translocation, inversion, aneuploidy, or other chromosomal syndrome is established as a cause.
- Copy-number variants disrupting both *GMPPA* alleles would be mechanistically possible, so deletion/duplication analysis is appropriate if sequencing finds only one allele.

A 2024 study showed that GMPPB ubiquitination modulates its catalytic activity without materially changing its turnover or interaction with GMPPA. This adds a regulatory layer to GDP-mannose supply but has not yet produced a clinical modifier or biomarker for GMPPA-CDG (published June 24, 2024; PMID:38979475). [198][199]

---

## 5. Environmental information

| Domain | Current evidence |
|---|---|
| Toxins/pollution/radiation | No causal association |
| Smoking/alcohol/exercise | No effect on occurrence demonstrated |
| Diet | Not causal; mannose availability modifies disease biology in knockout mice |
| Infection | No infectious cause or trigger |
| Immune mechanism | No primary autoimmune or immunodeficiency mechanism established |
| Occupational exposure | Not applicable |
| Gene–environment interaction | Experimental mannose restriction modifies hypermannosylation and neuromuscular degeneration in mice |

Infections can occur secondarily—especially aspiration pneumonia from achalasia or ocular infection from severe alacrima—but they are complications rather than causes.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **Biallelic loss-of-function variants in *GMPPA*** lead to absent, unstable, or functionally defective cytosolic GMPPA protein.  
2. **Loss of GMPPA–GMPPB interaction and feedback inhibition** leads to inadequately restrained GMPPB activity.  
3. **Unrestrained conversion of mannose-1-phosphate plus GTP to GDP-mannose** results in an abnormally enlarged intracellular GDP-mannose pool.  
4. **Excess GDP-mannose availability** leads to increased mannose incorporation into selected N-linked, O-linked, and other glycoconjugates; the exact substrate spectrum is cell-type dependent.  
5. **α-Dystroglycan hyperglycosylation** leads to increased α-dystroglycan turnover and reduced α-dystroglycan-core abundance.  
6. **Reduced or abnormal dystroglycan-mediated extracellular-matrix coupling** leads to altered laminin/nidogen/collagen organization, myofibrillar and Z-disc disorganization, myofiber apoptosis, and progressive myopathy.  
7. **In developing and mature neural tissues**, altered glycosylation and extracellular-matrix signaling lead to abnormal cortical layering and later neuronal loss; this branch is demonstrated in mice but incompletely established in human brain.  
8. **In autonomic circuits supplying the lower esophageal sphincter and lacrimal apparatus**, glycosylation dysregulation is inferred to impair neuronal or target-organ function, resulting in achalasia and alacrima.  
9. **Developmental CNS dysfunction** results in developmental delay, severe speech impairment, intellectual disability, and variable gait abnormalities.  
10. **Secondary consequences of achalasia and alacrima** lead to malnutrition, growth failure, aspiration risk, chronic ocular-surface injury, corneal scarring, and possible visual loss.

### 6.2 Upstream biochemical mechanism

GMPPB is the active enzyme that converts mannose-1-phosphate and GTP to GDP-mannose. GMPPA is a structurally related but catalytically inactive regulatory protein. Recombinant experiments showed:

- GMPPA directly binds GMPPB;
- Its C-terminal region, including the hexapeptide domain, is required for interaction;
- GMPPA inhibits GMPPB more strongly as GDP-mannose increases;
- Disease-associated p.Gly182Asp and p.Thr334Pro fail to inhibit GMPPB normally;
- Patient lymphoblasts and knockout-mouse muscle contain excess GDP-mannose.

The 2013 discovery study summarized the unexpected biochemical result as:

> “GDP-mannose pyrophosphorylase activity was unchanged and GDP-mannose levels were strongly increased in lymphoblasts of individuals with *GMPPA* mutations.”  
> —Koehler et al., 2013; PMID:24035193. [61]

### 6.3 Downstream cellular and tissue mechanisms

**Muscle:** Human quadriceps biopsies from two affected sisters showed increased glycosylation-specific α-dystroglycan epitopes, a higher apparent molecular mass, reduced α-dystroglycan core, irregular laminin, near-loss of the regular α-actinin pattern, and disorganized myofibers/Z-discs. The mouse model additionally showed smaller myofibers, central nuclei, apoptosis, impaired late myotube size, and progressive weakness.

**Brain:** Knockout mice showed abnormal somatosensory cortical layering, impaired contextual fear memory, and age-dependent loss of hippocampal pyramidal neurons and Purkinje cells. Peripheral motor conduction was largely preserved, favoring a combined central and myopathic process over a primary motor neuropathy.

**Signaling:** Phosphorylated ERK1/2 was elevated in knockout muscle and normalized with mannose restriction. This places MAPK/ERK activation downstream of glycosylation/ECM disturbance, but its causal contribution remains uncertain.

**Immune system:** IMPC screening lists immune-system effects in the knockout, but no human immunodeficiency, autoimmunity, or inflammatory syndrome has been established. [59]

### 6.4 Molecular profiling

| Modality | Findings |
|---|---|
| Metabolomics | Elevated GDP-mannose in patient lymphoblasts and knockout muscle |
| Glycomics | Increased high-mannose N-glycans, selected O-glycans, oligomannose, paucimannose, and PNA-reactive glycans in mouse muscle |
| Proteomics | Reduced CAPZB and other muscle-contraction-associated proteins; PRIDE dataset **PXD014260** |
| Human glycoprotein analysis | α-Dystroglycan hyperglycosylation and reduced core abundance in two muscle biopsies |
| Transcriptomics | No defining patient transcriptomic signature |
| Single-cell/spatial transcriptomics | No disease-specific study identified |
| Epigenomics | No disease-specific profile |
| CRISPR screens | No disease-specific genome-wide screen identified |
| Multi-omics | No comprehensive human multi-omic integration study |

### 6.5 Suggested mechanism ontology terms

**GO biological process**

- GDP-mannose biosynthetic process — GO:0009298  
- Protein glycosylation — GO:0006486  
- N-linked glycosylation — GO:0006487  
- O-linked glycosylation — GO:0006493  
- Regulation of catalytic activity — GO:0050790  
- Extracellular matrix organization — GO:0030198  
- Nervous system development — GO:0007399  
- Muscle-structure development — GO:0061061  
- Learning or memory — GO:0007611  
- Apoptotic process — GO:0006915  

**GO cellular component**

- Cytosol — GO:0005829  
- Cytoplasm — GO:0005737  
- Sarcolemma — GO:0042383  
- Extracellular matrix — GO:0031012  
- Dystrophin-associated glycoprotein complex — GO:0016010  

**Suggested Cell Ontology targets**

- Neuron — CL:0000540  
- Autonomic neuron — CL:0000107  
- Skeletal muscle fiber — CL:0000188  
- Skeletal muscle satellite cell — CL:0000596  
- Purkinje cell — CL:0000121  
- Pyramidal neuron — CL:0000598  
- Lacrimal-gland epithelial cell—use the most specific available release term  
- Esophageal smooth-muscle cell — CL:0000192/general smooth-muscle-cell mapping where no site-specific term is available  

---

## 7. Anatomical structures affected

| Level | Structure/site | Evidence and manifestations | Suggested anatomy term |
|---|---|---|---|
| Organ | Esophagus, especially lower esophageal sphincter | Achalasia, dysphagia, regurgitation, aspiration | UBERON:0001043 esophagus; UBERON:0004550 lower esophageal sphincter |
| Organ | Lacrimal gland/apparatus | Absent or markedly reduced tear production; one patient had bilateral gland absence | UBERON:0001817 lacrimal gland |
| Organ | Brain | Developmental delay, ID, seizures; mouse cortical, hippocampal and cerebellar pathology | UBERON:0000955 brain |
| Region | Cerebral cortex | Abnormal layering in knockout mice | UBERON:0000956 cerebral cortex |
| Region | Hippocampus | Pyramidal-neuron loss in aged knockout mice | UBERON:0002421 hippocampal formation |
| Region | Cerebellum | Purkinje-cell loss in knockout mice | UBERON:0002037 cerebellum |
| Tissue | Skeletal muscle | Hypotonia, weakness, myopathic biopsy changes | UBERON:0001134 skeletal muscle tissue |
| Tissue | Cornea/ocular surface | Dryness, inflammation, vascularization and scarring secondary to alacrima | UBERON:0000964 cornea |
| Organ/system | Peripheral autonomic nervous system | Inferred substrate of alacrima, achalasia, hypohidrosis, anisocoria and orthostatic hypotension | UBERON:0000010 peripheral nervous system |
| Organ | Ear/auditory system | Variable hearing loss | UBERON:0001690 ear |
| Tissue | Skin and appendages | Hyperkeratosis, hypohidrosis | UBERON:0002097 skin |
| Organ | Teeth | Anodontia/missing teeth | UBERON:0001091 tooth |

Alacrima is generally bilateral or systemic; no consistent lateralization is reported. Strabismus and pupil abnormalities may be asymmetric.

---

## 8. Temporal development and natural history

### 8.1 Onset

- **Congenital/neonatal:** alacrima, hypotonia, respiratory or feeding difficulty may be present from birth.
- **First year:** achalasia commonly presents through poor feeding, vomiting, dysphagia, or failure to thrive.
- **Infancy/early childhood:** motor, cognitive, and speech delay becomes evident.
- **Childhood/adulthood:** short stature, gait dysfunction, hearing loss, orthostatic symptoms, and muscle weakness may become clearer.

In the original series, achalasia onset ranged from birth to seven years, although most cases began during infancy. Alacrima was usually congenital but was recognized as late as six years in one patient.

### 8.2 Course

There is no validated staging system. A practical clinical course is:

1. **Early feeding/ocular stage:** alacrima and feeding intolerance;
2. **Diagnostic gastrointestinal stage:** progressive dysphagia, regurgitation, aspiration or growth failure leading to achalasia diagnosis;
3. **Neurodevelopmental stage:** speech, motor and cognitive delays become established;
4. **Chronic multisystem stage:** variable hypotonia, gait abnormality, hearing/visual impairment, autonomic dysfunction and possible progressive myopathy.

The disease is lifelong. Achalasia and ocular complications are treatable but do not remit spontaneously. Developmental disability generally persists. Two sisters were alive at 28 and 47 years with stable intellectual disability and hypotonia, demonstrating survival into middle adulthood. Progressive neuromuscular decline is biologically plausible and supported by the mouse model, but longitudinal human data remain limited.

### 8.3 Critical windows

Mouse data suggest that postnatal mannose restriction can prevent later neurodegeneration and motor decline but cannot reverse developmental cortical-layering abnormalities. This supports, but does not prove, the importance of prenatal and early-neonatal disease mechanisms. [46]

---

## 9. Inheritance, epidemiology, and population distribution

### 9.1 Inheritance

- **Pattern:** Autosomal recessive.
- **Affected-person genotype:** Homozygous or compound heterozygous pathogenic variants.
- **Parents:** Usually unaffected heterozygous carriers.
- **Sibling recurrence:** 25% affected, 50% carrier, 25% unaffected/non-carrier per pregnancy.
- **Penetrance:** Apparently high for the triad among individuals with established biallelic loss-of-function variants, but exact age-dependent penetrance cannot be calculated.
- **Expressivity:** Variable for muscle weakness, gait, hearing, growth, ectodermal features, seizures, and ocular abnormalities.
- **Anticipation:** Not expected; no repeat-expansion mechanism.
- **Germline mosaicism:** Not specifically reported; residual recurrence risk after an apparently de novo event cannot be assumed to be zero.
- **Consanguinity:** Prominent in the initial series; many—but not all—patients have homozygous variants.
- **Founder effect:** p.Leu89fs in the Guatemalan Maya-Mam population.
- **Sex limitation:** None expected. The observed 9:17 male:female ratio in 26 patients is likely sampling variation rather than biological sex bias.

### 9.2 Epidemiology

No population prevalence, birth incidence, mortality rate, or carrier frequency has been calculated. The condition is best designated **ultra-rare**:

- 13 affected individuals were characterized in the original 2013 study;
- 21 had been summarized by a 2022 CDG epidemiology review; [78]
- 26 molecularly confirmed patients were included in the 2025 systematic review;
- Advocacy sources describe fewer than 30 recognized individuals worldwide, although underdiagnosis is likely. [184]

Cases have been reported among Pakistani, Arab/Middle Eastern, Turkish, Kosovan, Palestinian, Dominican, Mexican, Guatemalan Maya-Mam, European, African and East Asian backgrounds. There is no evidence that the disorder is geographically restricted.

---

## 10. Diagnostics

### 10.1 When to suspect GMPPA-CDG

Strong suspicion is warranted in an infant or child with:

- Alacrima or severe aqueous tear deficiency;
- Congenital/infantile achalasia or unexplained dysphagia;
- Developmental delay, severe speech delay, hypotonia, or intellectual disability;
- Normal adrenal function.

The combination of early alacrima and achalasia **without adrenal insufficiency** should prompt *GMPPA* testing.

### 10.2 Clinical tests

| Domain | Recommended assessment | Expected/possible result |
|---|---|---|
| Tear production | Schirmer test; slit-lamp and corneal examination | Very low or absent tear production; ocular-surface injury |
| Achalasia | Upper GI contrast/barium esophagram | Dilated esophagus, delayed emptying, distal “bird-beak” narrowing |
| Esophageal function | High-resolution esophageal manometry | Impaired lower-esophageal-sphincter relaxation and absent/abnormal peristalsis; type II achalasia documented in one infant [137] |
| Endoscopy | Exclude mechanical obstruction and evaluate esophagitis | Retained food/fluid; no primary obstructing lesion |
| Nutrition | Weight, length/height, BMI, feeding and swallow assessment | Failure to thrive or short stature |
| Adrenal axis | Morning cortisol, ACTH; stimulation test if indicated | Expected normal; abnormal result warrants evaluation for triple-A syndrome |
| Development | Formal neurodevelopmental, speech-language, adaptive-behavior and cognitive testing | Global developmental delay and ID |
| Neuromuscular | Examination, CK, EMG/NCS if progressive weakness | Hypotonia/gait dysfunction; CK may be normal |
| Audiology | Age-appropriate audiogram/ABR | Variable hearing impairment |
| Ophthalmology | Visual acuity, refraction, ocular alignment, corneal surveillance | Strabismus, nystagmus, anisocoria, keratopathy |
| Brain imaging | MRI when seizures, regression, focal signs or microcephaly are present | Often normal; no diagnostic imaging signature |
| Routine CDG screen | Carbohydrate-deficient transferrin/transferrin isoelectric focusing | Often normal and cannot exclude GMPPA-CDG |

Standard achalasia evaluation includes manometry, barium swallow, and endoscopy. [140]

### 10.3 Genetic-testing strategy

1. **First-line molecular testing**
   - Trio whole-exome sequencing or genome sequencing, particularly when achalasia accompanies developmental delay;
   - Alternatively, an achalasia/autonomic-neuropathy or congenital-disorders-of-glycosylation panel including *GMPPA*, *AAAS*, and *GUCY1A1*.

2. **Variant confirmation**
   - Sanger confirmation and parental segregation;
   - Confirm that two variants are in trans when compound heterozygous.

3. **Copy-number analysis**
   - Exon-level deletion/duplication analysis if only one pathogenic variant is found;
   - Genome sequencing can detect noncoding, structural, and copy-number variants not captured by exome sequencing.

4. **Lower-yield tests**
   - Chromosomal microarray can identify large deletions but is not a sensitive primary test for typical single-nucleotide/indel disease;
   - Karyotyping and FISH have no routine role;
   - Mitochondrial DNA and repeat-expansion testing are not indicated unless the phenotype suggests another diagnosis;
   - RNA sequencing may clarify splice variants but is not a validated routine biomarker;
   - Proteomics, glycomics and metabolomics remain research tools.

Exome sequencing was the main diagnostic method in 20 of the 26 patients reviewed in 2025. [136]

### 10.4 Differential diagnosis

| Disorder/gene | Overlap | Distinguishing features |
|---|---|---|
| Triple-A/Allgrove syndrome, ***AAAS*** | Alacrima, achalasia, autonomic and neurological findings | ACTH-resistant adrenal insufficiency is characteristic; ID is less uniformly central |
| Moyamoya 6 with achalasia, ***GUCY1A1*** | Congenital achalasia | Moyamoya vasculopathy, stroke/ischemia, hypertension or other NO-signaling phenotype |
| NGLY1 deficiency, ***NGLY1*** | Alacrima, developmental disability, movement abnormalities | Elevated transaminases, hyperkinetic movement disorder, constipation and broader ERAD phenotype |
| Familial/isolated achalasia | Achalasia | No consistent alacrima plus neurodevelopmental syndrome |
| Primary lacrimal-gland agenesis | Alacrima | No achalasia or ID |
| Other congenital disorders of glycosylation | Developmental delay, hypotonia, growth failure | Different organ pattern; many have abnormal transferrin glycosylation |
| Hereditary sensory/autonomic neuropathy | Autonomic dysfunction, alacrima | Sensory loss, ulcers, pain insensitivity; achalasia–ID triad not typical |

### 10.5 Screening

There is no newborn-screening program or validated biochemical screening assay. Appropriate strategies are:

- Cascade testing of adult relatives after the familial variants are known;
- Targeted carrier testing in at-risk relatives and founder populations;
- Prenatal diagnosis or preimplantation genetic testing for monogenic disease when familial variants are established.

---

## 11. Outcome and prognosis

No 5-year or 10-year survival rates, disease-specific mortality estimates, or validated prognostic scores exist. Life expectancy is unknown. Survival to at least 47 years is documented, but the cohort is too small for population inference.

### Principal morbidity and complications

- Malnutrition and growth failure;
- Recurrent vomiting and dehydration;
- Aspiration and aspiration pneumonia;
- Progressive esophageal dilation;
- Corneal dryness, inflammation, infection, vascularization, ulceration, perforation, scarring, and blindness;
- Severe communication and adaptive-function limitations;
- Mobility impairment, falls, and progressive muscle weakness;
- Orthostatic symptoms and heat intolerance;
- Hearing and visual impairment;
- Possible osteopenia/low bone mineral density in adults.

### Prognostic factors

No validated biomarker predicts outcome. Clinically plausible factors include:

- Age at achalasia diagnosis and adequacy of nutritional rescue;
- Severity of aspiration;
- Early ocular lubrication and corneal surveillance;
- Degree of developmental disability;
- Presence of gait decline or progressive muscle weakness;
- Access to developmental and communication interventions.

No genotype–phenotype correlation was identified among 26 patients. [40]

---

## 12. Treatment

There is no approved disease-modifying therapy. Management is multidisciplinary and symptom-directed.

### 12.1 Practical management pathway

1. **Immediately protect the ocular surface** with preservative-free artificial tears and ophthalmology follow-up.
2. **Evaluate swallowing and nutrition urgently**, especially in infants with vomiting or failure to thrive.
3. **Confirm and treat achalasia** using pediatric gastroenterology and surgery.
4. **Provide nutrition support**, including temporary nasogastric or gastrostomy feeding where necessary.
5. **Assess development, hearing, vision, mobility and autonomic symptoms** at baseline and longitudinally.
6. **Initiate physical, occupational, feeding and speech-language therapy**, including augmentative communication where appropriate.
7. **Offer genetic counseling and familial testing.**
8. **Restrict experimental metabolic treatments to specialist-supervised protocols or trials.**

### 12.2 Interventions

| Intervention | Indication/evidence | Outcome and cautions | Suggested NCIt intervention concept |
|---|---|---|---|
| Preservative-free artificial tears/lubricant ointment | Alacrima and keratopathy | Reduces dryness and risk of scarring; frequent dosing often needed | Artificial Tears; Ophthalmic Solution |
| Ophthalmic antibiotics | Secondary infection only | Not prophylactic long-term therapy | Anti-Infective Agent |
| Protective eyewear/humidity measures | Severe dry eye | Supportive; no disease-modifying effect | Supportive Care |
| Nasogastric/gastrostomy feeding | Unsafe or inadequate oral feeding | Restores nutrition and reduces immediate aspiration burden | Enteral Nutrition; Gastrostomy |
| Laparoscopic Heller myotomy, often with partial fundoplication | Definitive achalasia treatment | Feeding tolerance and growth can improve; reflux is a risk | Heller Myotomy; Fundoplication |
| Pneumatic dilation | Achalasia in selected patients | Effective but recurrence/perforation risk must be considered | Esophageal Dilation |
| Peroral endoscopic myotomy | Achalasia; increasing pediatric use | Minimally invasive; reflux monitoring required | Peroral Endoscopic Myotomy |
| Botulinum toxin injection | Temporary bridge where definitive treatment is unsuitable | Benefit is usually temporary | Botulinum Toxin Injection |
| Calcium-channel blocker, e.g. nifedipine | Rarely used temporary symptom relief | Limited efficacy and hypotension risk, particularly relevant in autonomic disease | Calcium Channel Blocker |
| Physical/occupational therapy | Hypotonia, weakness and gait dysfunction | Maintains mobility and function; no quantified response rate | Physical Therapy; Occupational Therapy |
| Speech-language and augmentative communication therapy | Severe speech impairment | Improves communication access rather than underlying cognition | Speech Therapy |
| Audiology/hearing aids | Hearing loss | Supports language and communication | Hearing Aid |
| Growth hormone | Documented GH deficiency | One reported patient responded without reported adverse effects; not indicated for nonspecific short stature without endocrine evaluation | Recombinant Growth Hormone |
| Oral N-acetylglucosamine | Experimental pilot in three patients | Reported improved eye symptoms in all three and swallowing in one; no developmental or growth improvement; one had abdominal discomfort | N-Acetyl-D-Glucosamine; Dietary Supplement |
| Mannose-restricted diet | Experimental, mouse evidence only | Prevented much neuromuscular decline in mice but did not rescue cortical development/cognition; human safety and efficacy unknown | Dietary Intervention |
| Gene replacement/editing | Preclinical concept | No reported human trial or approved construct | Gene Therapy |
| Repirinast | Orphan-designated experimental candidate | U.S. orphan designation dated July 11, 2024, but no demonstrated clinical efficacy or GMPPA-CDG trial identified [181] | Repirinast; Investigational Agent |

### 12.3 Achalasia treatment evidence

Definitive options include Heller myotomy with or without fundoplication, pneumatic dilation, and POEM. Pharmacological therapy has limited efficacy, while botulinum toxin is generally temporary. [137] In reported GMPPA-CDG patients, achalasia-directed interventions improved feeding tolerance, but robust response rates and comparative outcomes are unavailable.

### 12.4 N-acetylglucosamine pilot

Three patients received escalating oral GlcNAc, generally up to 6 g/day, for 6–18 months:

- All three had subjective and ophthalmologist-confirmed improvement in corneal dryness/irritation;
- One had reduced corneal vascularization;
- One reported improved swallowing;
- Artificial-tear dependence decreased;
- No growth or developmental improvement was observed;
- One patient remained at 4 g/day because of abdominal discomfort.

This was an uncontrolled, nonblinded observational experience and should not be considered proof of efficacy. The 2025 abstract reported:

> “Under treatment with GlcNAc (4–6 g/day), we noted improved tear production in our 3 patients.”  
> —Altassan et al., *Molecular Genetics and Metabolism*, July 18, 2025; PMID:40706141. [40]

### 12.5 Advanced therapies and pharmacogenomics

No gene therapy, cell therapy, ASO, siRNA, mRNA therapy, CRISPR treatment, immunotherapy, or approved targeted metabolic therapy is currently available. No *GMPPA*-specific pharmacogenomic dosing guideline exists.

---

## 13. Prevention

### Primary prevention

The occurrence of a recessive Mendelian disorder cannot be prevented by vaccination or lifestyle modification. Reproductive options after identification of familial variants include:

- Carrier testing of partners and relatives;
- Preimplantation genetic testing for monogenic disease;
- Chorionic-villus sampling or amniocentesis;
- Use of donor gametes;
- Adoption or natural conception with informed testing choices.

### Secondary prevention

There is no population newborn screen. Targeted early detection should include:

- Testing siblings promptly;
- Schirmer testing and ophthalmology assessment before corneal injury develops;
- Investigation of feeding difficulty before severe malnutrition or aspiration;
- Early developmental, hearing, and vision assessment.

### Tertiary prevention

- Continuous lubrication to prevent corneal complications;
- Timely achalasia intervention to prevent aspiration and growth failure;
- Safe-swallow and nutritional plans;
- Physical therapy and fall prevention;
- Hearing aids and communication supports;
- Dental care for missing teeth;
- Heat-safety planning for hypohidrosis;
- Bone-health assessment in patients with poor growth, low mobility, or osteopenia.

No immunization or antimicrobial prophylaxis is specific to GMPPA-CDG; routine age-appropriate vaccination remains appropriate.

---

## 14. Other species and natural disease

No naturally occurring GMPPA-CDG-equivalent veterinary disease, breed predisposition, zoonotic transmission, or cross-species infectious risk has been established. An OMIA disease entry specifically linking spontaneous animal disease to *GMPPA* was not identified.

| Species | Taxonomy/orthologue | Relevance |
|---|---|---|
| *Homo sapiens* | NCBI Taxon:9606; *GMPPA*, Gene:29926 | Natural human disease |
| *Mus musculus* | NCBI Taxon:10090; *Gmppa*, Gene:69080; MGI:1916330 | Validated knockout disease model [166] |
| *Danio rerio* | NCBI Taxon:7955; orthologue *gmppaa* | Conserved orthologue; no well-characterized GMPPA-CDG model identified |
| *Drosophila melanogaster* | NCBI Taxon:7227; *Gmppa*, FBgn0034035 | Predicted catalytically inactive regulator of Gmppb [173] |
| *Rattus norvegicus* | NCBI Taxon:10116; *Gmppa* orthologue | Comparative genomics; no disease model identified |

The conserved regulatory relationship across species supports evolutionary conservation of GDP-mannose control, but the complete human triad has only been modeled partially in mice.

---

## 15. Model organisms and experimental systems

### 15.1 *Gmppa*-knockout mouse

The principal model is a homozygous knockout lacking exon 5, produced from EUCOMM embryonic stem-cell clone EPD0621_7_G03 on a C57BL/6 background. The deletion causes a frameshift, transcript depletion through nonsense-mediated decay, and absence of detectable GMPPA.

| Human feature/mechanism | Mouse recapitulation |
|---|---|
| Cognitive disability | Impaired hippocampus-dependent contextual memory |
| CNS developmental pathology | Altered somatosensory cortical layering |
| Possible progression | Age-dependent hippocampal pyramidal-neuron and cerebellar Purkinje-cell loss |
| Hypotonia/weakness | Progressive reduced grip strength, abnormal foot-base angle and poor inverted-screen performance |
| Myopathy | Reduced muscle mass, small fibers, central nuclei, apoptosis, Z-band disruption |
| GDP-mannose excess | Elevated skeletal-muscle GDP-mannose |
| Hyperglycosylation | Increased high-mannose glycans and α-dystroglycan hyperglycosylation |
| Reduced α-dystroglycan | Increased turnover and reduced core abundance |
| ECM disturbance | Abnormal laminin/nidogen/collagen-IV distribution |
| MAPK response | Increased phospho-ERK1/2 |
| Achalasia | Not clearly demonstrated |
| Alacrima | Not established as a defining model feature |
| Severe speech delay | Cannot be directly modeled |

The model therefore has strong construct validity and good validity for the molecular, CNS and neuromuscular components, but incomplete face validity for the human autonomic triad.

### 15.2 Dietary intervention in mice

A nominally mannose-free diet, replacing the 1% free mannose in standard chow with sucrose from postnatal day 14 to 12 months:

- Nearly normalized serum mannose;
- Corrected α-dystroglycan hyperglycosylation and abundance;
- Improved myofiber morphology and ECM organization;
- Largely prevented hippocampal and Purkinje-neuron loss;
- Prevented progressive motor decline;
- Did **not** rescue cortical layering or contextual cognition.

The key abstract conclusion was:

> “In mice, dietary mannose restriction beginning after weaning corrected α-DG hyperglycosylation and abundance, normalized skeletal muscle morphology, and prevented neuron degeneration and the development of motor deficits.”  
> —Franzka et al., *Journal of Clinical Investigation*, May 3, 2021; PMID:33755596. [46]

### 15.3 Cellular and in-vitro systems

- Patient Epstein–Barr-virus-transformed lymphoblasts: GDP-mannose quantification and enzyme activity;
- Patient fibroblasts: GMPPA abundance and variant effects;
- Human quadriceps biopsies: α-dystroglycan and ECM pathology;
- HEK-293T cells: GMPPA–GMPPB co-immunoprecipitation;
- COS-7 cells: variant-protein abundance/localization;
- Primary mouse myoblasts and C2C12 cells: α-dystroglycan turnover, differentiation and myotube size;
- Recombinant GMPPA/GMPPB proteins: direct binding and enzymatic inhibition.

No published patient-derived iPSC, cerebral organoid, esophageal organoid, lacrimal-gland organoid, or single-cell disease model was identified.

---

## Recent developments, 2023–2026

| Date | Development | Significance |
|---|---|---|
| September 6, 2023 | ClinGen CDG expert panel classified the *GMPPA*–MONDO:0014219 relationship as definitive | Strengthens clinical gene validity and confirms AR loss-of-function mechanism [33] |
| June 24, 2024 | GMPPB ubiquitination shown to regulate enzyme activity; PMID:38979475 | Adds a second regulatory layer controlling GDP-mannose supply, though not yet clinically actionable [199] |
| July 11, 2024 | Repirinast received U.S. orphan designation for GMPPA-CDG | Regulatory designation only; it does not establish safety, efficacy, approval, or trial availability [181] |
| July 18, 2025 | Review of 26 molecularly confirmed cases and three-patient GlcNAc experience; PMID:40706141 | Largest phenotype aggregation, updated frequency estimates, and preliminary treatment observations [40] |
| 2025 | Achalasia treated with POEM in a child with GMPPA homozygosity attributed to uniparental disomy | Expands the inheritance/management literature but remains a single case [64] |
| 2026 status | Fewer than approximately 30 recognized patients; no approved disease-modifying therapy | Major unmet needs remain epidemiology, natural history, biomarkers, and controlled intervention studies [184] |

---

## Evidence assessment and knowledge gaps

### Well-supported conclusions

- Biallelic *GMPPA* variants cause MONDO:0014219/OMIM:615510.
- Inheritance is autosomal recessive.
- Alacrima, achalasia and developmental impairment form the core phenotype.
- Adrenal insufficiency is not characteristic.
- GMPPA is an allosteric feedback inhibitor of GMPPB.
- Loss of GMPPA elevates GDP-mannose and causes α-dystroglycan hyperglycosylation.
- Achalasia and ocular-surface disease require active treatment.

### Important uncertainties

- True prevalence, incidence, carrier frequency and life expectancy;
- Penetrance of individual alleles;
- Complete current variant spectrum and population-specific frequencies;
- Mechanism producing selective lacrimal and esophageal autonomic dysfunction;
- Long-term rate of neuromuscular progression;
- Whether dietary mannose restriction is safe or beneficial in people;
- Whether GlcNAc meaningfully increases tear production in controlled testing;
- Utility of repirinast or gene replacement;
- Disease-specific patient-reported outcomes and caregiver burden;
- Prenatal natural history and optimal early-intervention window.

## Key publications and URLs

- Koehler K et al. **“Mutations in GMPPA Cause a Glycosylation Disorder Characterized by Intellectual Disability and Autonomic Dysfunction.”** *American Journal of Human Genetics*. Published October 3, 2013. PMID:24035193. DOI:10.1016/j.ajhg.2013.08.002. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3791256/ [61]
- Franzka P et al. **“GMPPA defects cause a neuromuscular disorder with α-dystroglycan hyperglycosylation.”** *Journal of Clinical Investigation*. Published May 3, 2021. PMID:33755596. DOI:10.1172/JCI139076. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8087212/ [46]
- Diaz J, Kane TD, Leon E. **“Evidence of GMPPA founder mutation in indigenous Guatemalan population associated with alacrima, achalasia, and mental retardation syndrome.”** *American Journal of Medical Genetics Part A*. Published online January 3, 2020. PMID:31898852. DOI:10.1002/ajmg.a.61476. [108][113]
- Franzka P et al. **“Ubiquitination contributes to the regulation of GDP-mannose pyrophosphorylase B activity.”** *Frontiers in Molecular Neuroscience*. Published June 24, 2024. PMID:38979475. DOI:10.3389/fnmol.2024.1375297. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11228364/ [198][199]
- Altassan R et al. **“Phenotypic and genotypic description of GMPPA-congenital disorder of glycosylation: A review of 26 cases.”** *Molecular Genetics and Metabolism*. Published July 18, 2025. PMID:40706141. DOI:10.1016/j.ymgme.2025.109196. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC12746796/ [40]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 13 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1093/gastro/goaf083/8259572` (1 mention) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.3389/fped.2021.715151` (2 mentions) - Congenital Disorders of Glycosylation: What Clinicians Need to Know?
  - shared terms: patient

Weighed against this report's own most characteristic terms: `achalasia`, `gmppa`, `patient`, `disease`, `developmental`, `alacrima`, `gdp-mannose`, `human`, `muscle`, `variant`, `loss`, `disability`, `gmppa-cdg`, `gmppb`, `hearing`, `gene`, `syndrome`, `autonomic`, `mechanism`, `aspiration`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 78 |
| Resolved | 63 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 14 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014219` (8 mentions) - the report calls it "MONDO"; MONDO calls it **alacrima, achalasia, and intellectual disability syndrome**
- `DOID:0112321` (2 mentions) - the report calls it "Disease Ontology"; DOID calls it **alacrima, achalasia, and impaired intellectual development syndrome**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`, `ORPHA`, `NC_000002.12`, `Taxon`, `MGI`.