---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-15T20:32:58.578199'
end_time: '2026-09-15T20:39:15.314816'
duration_seconds: 376.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Leukoencephalopathy Progressive Infantile-onset With Or Without Deafness
  mondo_id: MONDO:0030893
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
citation_count: 14
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 65
  verified: 62
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 41
  labels_matching: 28
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: GO:0008213
    reported_labels:
    - neuron death
    ontology_label: protein alkylation
  - term_id: UBERON:0002436
    reported_labels:
    - white matter of brain
    ontology_label: primary visual cortex
  - term_id: UBERON:0001755
    reported_labels:
    - cochlea
    ontology_label: distal part of styloid process of temporal bone
  - term_id: UBERON:0000943
    reported_labels:
    - cranial nerve VIII
    ontology_label: obsolete labial sensillum
  - term_id: CL:0000203
    reported_labels:
    - inner hair cell of cochlea
    ontology_label: gravity sensitive cell
  - term_id: UBERON:0001476
    reported_labels:
    - retina
    ontology_label: deltoid
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0070469
    ontology_label: obsolete respirasome
    replaced_by: GO:0098803
  - term_id: UBERON:0000943
    ontology_label: obsolete labial sensillum
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leukoencephalopathy Progressive Infantile-onset With Or Without Deafness
- **MONDO ID:** MONDO:0030893 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leukoencephalopathy Progressive Infantile-onset With Or Without Deafness** covering all of the
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

# Leukoencephalopathy, Progressive, Infantile-Onset, With or Without Deafness (LEPID): Comprehensive Disease Characteristics

Infantile-onset progressive leukoencephalopathy with or without deafness (LEPID) is a recently delineated autosomal recessive neurodegenerative leukodystrophy caused by biallelic variants in the lysyl‑tRNA synthetase 1 gene (KARS1), characterized by early-onset white matter disease with brainstem and spinal cord calcifications, sensorineural hearing loss in most patients, global developmental delay, episodic neurologic regression, and high childhood mortality.[1][11][2] Clinical descriptions from multiple cohorts and case reports emphasize a complex multisystem phenotype including spastic tetraplegia, seizures, microcephaly, visual impairment, microcytic anemia, hepatic abnormalities, lactic acidosis, and marked failure to thrive, reflecting the underlying global mitochondrial dysfunction inferred from elevated serum lactate and respiratory chain deficiencies.[1][11][2][12][14] Neuroradiologic studies consistently show deep cerebral white matter abnormalities and calcifications involving the brainstem and spinal cord, placing LEPID within the broader group of genetic leukoencephalopathies with calcifications, yet it is genetically distinct from SNORD118‑related leukoencephalopathy with calcifications and cysts.[1][8][9][11] Functional analyses of KARS1 variants demonstrate impaired lysyl‑tRNA synthetase aminoacylation activity and inhibition of mitochondrial translation, providing a mechanistic link between the genetic lesions and defective oxidative phosphorylation in high‑energy tissues such as the central nervous system and auditory system.[6][14] Natural history data, though limited, indicate a relentlessly progressive course with onset in infancy or early childhood, episodic deterioration often precipitated by intercurrent illness, and premature death in many affected children despite supportive care, underscoring the urgent need for better diagnostic pathways, mechanistic understanding, and therapeutic strategies for this rare Mendelian disorder.[1][2][11][14]

## 1. Disease Information and Nomenclature

### 1.1 Clinical Overview and Core Definition

Infantile-onset progressive leukoencephalopathy with or without deafness (LEPID) is defined as an autosomal recessive, complex neurodegenerative disorder characterized by early-onset progressive leukoencephalopathy, typically manifesting in infancy or early childhood.[1][11] Most described patients present with congenital or early sensorineural deafness or hypoacusis, global developmental delay, and episodic neurologic regression that leads over time to spastic tetraplegia, loss of independent ambulation, and severe intellectual disability with poor or absent speech.[1][9][11] Additional features are variably present and include poor overall growth with microcephaly, intractable seizures, visual loss or optic neuropathy, microcytic anemia, and hepatic enlargement or abnormal liver enzymes, confirming that LEPID is a multisystem mitochondrial disorder rather than a purely isolated leukodystrophy.[1][2][9][11][12][14] Brain imaging consistently reveals deep white matter abnormalities compatible with a progressive leukoencephalopathy, with involvement of both brain and spinal cord; calcifications within these regions, particularly the brainstem and spinal cord, are a hallmark neuroradiological feature that helps distinguish LEPID from other KARS1-related phenotypes and from many other leukodystrophies.[1][9][11] Laboratory studies demonstrate increased serum lactate and deficiencies of mitochondrial respiratory chain complexes in patient-derived tissues, consistent with global mitochondrial dysfunction as the proximate biochemical basis of disease.[1][2][6][11][14]

From a clinical nosology perspective, LEPID belongs to the group of inherited leukodystrophies, defined by primary involvement of cerebral white matter, but it exhibits distinctive combinations of calcifications, neurosensory deficits, and systemic manifestations that justify its separate designation.[1][9][11] Itoh et al. (2019), who reported seven children from five unrelated Japanese families with early-onset progressive leukoencephalopathy and identified biallelic KARS1 mutations, emphasized congenital deafness, hypotonia, global developmental delay, impaired intellectual development, poor or absent speech, nystagmus, and intractable seizures as recurring features, alongside progressive motor deterioration and early death in most affected children.[11] These observations, together with additional cases collated in OMIM and other databases, support a unified disease concept in which KARS1-related mitochondrial dysfunction produces a recognizable but variable phenotype of infantile-onset progressive leukoencephalopathy with or without deafness, now codified under specific identifiers in Mendelian disease ontologies.[1][11][12][14]

### 1.2 Identifiers and Classification

LEPID is curated in multiple rare disease and Mendelian databases, each providing standardized identifiers that facilitate cross‑reference and integration into computational disease knowledge bases.[1][9][11] In the Online Mendelian Inheritance in Man (OMIM) database, the disorder is assigned entry number 619147 under the title “Leukoencephalopathy, progressive, infantile-onset, with or without deafness,” with a number sign (#) indicating that causation has been established for mutations in KARS1 (MIM 601421) on chromosome 16q23.1.[11] ClinVar submissions describing specific KARS1 variants often reference the associated condition using the same OMIM label or closely related phrases, and some records also map the disease to MONDO:0030893 in the Mondo Disease Ontology, confirming its recognition as a distinct Mendelian entity.[3][6][10] MedGen and related NCBI resources similarly list LEPID with identifiers such as C5542996, while Orphanet catalogs a closely related entity under ORPHA:3240, “Early-onset progressive leukoencephalopathy–central nervous system calcification–deafness–visual impairment syndrome,” whose clinical description substantially overlaps with the LEPID phenotype and likely corresponds to the same or a very closely related KARS1-associated disorder.[9][11]

Diagnostic classification within broader clinical taxonomies is less standardized, as LEPID is a rare and recently defined disease. However, based on its core features, it would typically be coded within ICD systems under categories for hereditary or primary leukoencephalopathies and hereditary sensorineural hearing loss, while MESH and SNOMED CT terms related to leukodystrophy, mitochondrial disease, and neurosensory deafness are relevant for semantic mapping.[1][9][11] Orphanet describes the disorder as a rare genetic neurological disease with prevalence estimated at less than 1 per 1,000,000, reinforcing its orphan disease status.[9] In Mendelian disease classification frameworks, LEPID is firmly categorized as a monogenic, autosomal recessive condition belonging to the “Mendelian” category requested in the query, and its primary causal factor is a biallelic germline mutation in KARS1 affecting lysyl-tRNA synthetase function.[1][2][11][14]

### 1.3 Synonyms and Alternative Names

Several synonymous or closely related names have been used in the literature and databases to describe LEPID or overlapping KARS1-related phenotypes, reflecting evolving knowledge about the clinical spectrum. Malacards and OMIM use the canonical name “Leukoencephalopathy, progressive, infantile-onset, with or without deafness (LEPID)” and sometimes the shorthand “infantile-onset progressive leukoencephalopathy with or without deafness.”[1][11] Orphanet lists “Early-onset progressive leukoencephalopathy–central nervous system calcification–hearing loss–visual impairment syndrome” and “Early-onset progressive leukoencephalopathy–central nervous system calcification–deafness–visual impairment syndrome” as synonyms for its ORPHA:3240 disorder, which appears to be clinically congruent with LEPID.[9] ClinVar records for KARS1 variants sometimes specify “infantile-onset progressive leukoencephalopathy with deafness,” emphasizing the high frequency of hearing loss, while for related but distinct phenotypes they use “Deafness, congenital, and adult-onset progressive leukoencephalopathy (DEAPLE)” to denote KARS1-associated disease with later neurological onset.[6][11][13]

In the primary literature, KARS1-associated leukoencephalopathy has been described under descriptive labels such as “infantile-onset progressive leukoencephalopathy with deafness,” “progressive leukoencephalopathy, infantile-onset, with or without deafness,” or more broadly as “KARS1-related mitochondrial disorder with progressive leukoencephalopathy, infantile-onset, with or without deafness,” as in a detailed Saudi case report published in JBC Genetics.[2] The broader category of “KARS1-related diseases” encompasses additional phenotypes, including Charcot–Marie–Tooth neuropathy, congenital visual impairment with progressive microcephaly, nonsyndromic hearing impairment, and complex immune‑hematological disorders, which must be distinguished from LEPID in clinical and research contexts.[2][7][12][14] For ontology mapping, it is therefore important to associate the precise LEPID label with MONDO:0030893, OMIM 619147, and ORPHA:3240, while preserving links to related KARS1 phenotypes through gene-centric annotations.

### 1.4 Nature of Available Information and Evidence Base

Because LEPID is a rare and recently delineated Mendelian disorder, the available information is derived almost entirely from aggregated disease-level resources and small case series rather than large cohort studies or electronic health record mining. The core clinical and genetic description is synthesized in OMIM, which summarizes data from Itoh et al. (2019) and other groups reporting children with early-onset progressive leukoencephalopathy and biallelic KARS1 mutations, providing an integrated view of typical features, neuroimaging, laboratory abnormalities, and natural history.[11] Malacards compiles information from OMIM, Orphanet, PubMed, and other databases, listing clinical traits, associated gene, and related phenotypes, while ClinVar and MedGen contribute variant‑level evidence and phenotype mapping for individual patients.[1][3][6][10][11]

Primary clinical evidence consists of individual case reports and small series such as the JBC Genetics report of a Saudi child with compound heterozygous KARS1 mutations and progressive infantile-onset leukoencephalopathy with deafness and anemia, McMillan et al.’s report of two siblings with congenital visual impairment and progressive microcephaly due to KARS mutations, and several studies collated in a comprehensive review of loss‑of‑function KARS-related diseases.[2][12][14] A recent review of mitochondrial aminoacyl‑tRNA synthetase (mt‑ARS) genes and hereditary sensorineural hearing loss includes LEPID within the spectrum of KARS1-associated disorders and tabulates specific variants and phenotypes, adding further granularity to the clinical spectrum.[7] The evidence base for mechanistic conclusions is a combination of human clinical data, in vitro functional studies of mutant KARS1 proteins and patient-derived fibroblasts, and structural analyses, as summarized in the loss-of-function KARS article.[14] There are currently no large prospective natural history studies or randomized clinical trials specific to LEPID, and much of the epidemiologic, prognostic, and treatment‑related information must be inferred from small datasets and extrapolated from general principles of mitochondrial leukodystrophies.

## 2. Etiology, Inheritance, and Population Genetics

### 2.1 Genetic Causal Factors: KARS1 and LEPID

The primary etiologic factor in LEPID is biallelic loss‑of‑function or function‑impairing missense variants in the KARS1 gene, which encodes lysyl‑tRNA synthetase 1, a bifunctional aminoacyl‑tRNA synthetase that operates in both cytosolic and mitochondrial compartments.[1][11][12][14] OMIM clearly states that evidence supports causation of infantile-onset progressive leukoencephalopathy with or without deafness by homozygous or compound heterozygous mutation in KARS1 on chromosome 16q23.1, and ClinVar records for multiple pathogenic KARS1 variants link them directly to LEPID.[3][6][10][11][13] KARS1 is responsible for attaching lysine to its cognate tRNA (tRNA^Lys), an essential step in protein synthesis; McMillan et al. note that “Lysyl-transfer RNA synthetase (KARS) links the amino acid lysine to its cognate transfer RNA,” situating the gene within the aminoacyl‑tRNA synthetase family whose dysfunction is increasingly recognized as a cause of human disease.[12] In LEPID, the prevailing mechanistic interpretation is that impaired KARS1 activity disrupts mitochondrial translation, leading to respiratory chain deficiencies and consequent energy failure in vulnerable tissues.[1][6][11][14]

Several different KARS1 variants have been associated specifically with LEPID or closely overlapping phenotypes. Itoh et al. identified homozygous or compound heterozygous missense or splice‑site mutations in seven children from Japanese families with early-onset progressive leukoencephalopathy, congenital deafness, and epilepsy, establishing KARS1 as the causal gene.[11] Ruzzenente et al., as summarized in OMIM and ClinVar, described a French girl with infantile-onset progressive leukoencephalopathy with deafness who carried compound heterozygous KARS1 mutations: c.683C>T (p.Pro228Leu) and c.1438delC (p.Leu480TrpfsTer3), and demonstrated that her fibroblasts showed inhibition of mitochondrial translation, implicating this mechanism as central to disease pathogenesis.[6][11] McMillan et al. reported two siblings with severe infantile visual loss, progressive microcephaly, developmental delay, seizures, and abnormal subcortical white matter carrying KARS mutations c.1312C>T (p.Arg438Trp) and c.1573G>A (p.Glu525Lys), whose phenotype is closely aligned with LEPID and expands the recognized spectrum of KARS-related leukoencephalopathy.[12] A recent mt‑ARS review tabulates several KARS1 variants linked to “Leukoencephalopathy, progressive, infantile-onset, with deafness” or “with or without deafness,” including c.1702C>T (p.Leu568Phe), c.1573G>A (p.Glu525Lys), c.1354del (p.Leu452fs), c.1328T>C (p.Leu443Pro), and c.795+1G>A, along with references to Demain et al. (2020), McMillan et al. (2015), Ruzzenente et al. (2018), Itoh et al. (2019), and ClinVar.[7]

ClinVar and OMIM also document additional pathogenic or likely pathogenic KARS1 variants associated with LEPID, including c.1312C>T (p.Arg438Trp) classified as pathogenic for LEPID, c.683C>T (p.Pro228Leu) linked to infantile-onset progressive leukoencephalopathy with deafness, c.953T>C (p.Ile318Thr) classified as likely pathogenic for LEPID, and c.1430G>A (p.Arg477His), which is more strongly associated with congenital deafness and adult-onset progressive leukoencephalopathy but has been reported in a compound heterozygous state in a Colombian boy with LEPID.[3][6][10][11][13] Functional analyses in the loss-of-function KARS paper show that these and other mutations impair aminoacylation activity of lysyl-tRNA synthetase, supporting a loss‑of‑function mechanism.[14] Altogether, the genetic evidence firmly establishes KARS1 as the disease gene for LEPID and defines a growing catalogue of pathogenic variants that can be used for diagnostic and research purposes.

### 2.2 Spectrum of KARS1-Related Disorders and Phenotypic Boundaries

While LEPID represents one distinct phenotype within the spectrum of KARS1-related disease, it is important to recognize that biallelic KARS1 variants can cause several clinically distinct disorders that share some features but differ in age of onset, organ involvement, and course. OMIM notes that KARS1 mutations can cause congenital deafness with adult-onset progressive leukoencephalopathy (DEAPLE; OMIM 619196), a similar disorder with overlapping features but later neurologic deterioration.[11][13] ClinVar’s entry for NM_005548.3(KARS1):c.1430G>A (p.Arg477His) associates this variant with “Deafness, congenital, and adult-onset progressive leukoencephalopathy,” and describes patients who had infantile-onset deafness and learning difficulties in childhood, but developed progressive cognitive decline in their second or third decades, illustrating the DEAPLE phenotype.[13] In contrast, LEPID typically involves neurological regression beginning in infancy or early childhood, often accompanied by seizures and global developmental delay, with more rapid progression and earlier mortality.[1][2][11]

McMillan et al. reported a phenotype of congenital visual impairment and progressive microcephaly due to KARS mutations, with severe infantile visual loss, developmental delay, seizures, and abnormal subcortical white matter, which they suggested represents an expansion of the aminoacyl‑tRNA synthetase mutation phenotypic spectrum.[12] The authors drew attention to similarities between KARS and glutaminyl-tRNA synthetase (QARS) mutations, noting that “This finding expands the phenotypic spectrum associated with mutations in KARS and draws attention to aminoacyl-transfer RNA synthetase as a group of enzymes that are increasingly being implicated in human disease.”[12] The loss-of-function KARS review further indicates that homozygous variants in KARS1 have been linked to diverse phenotypes involving various organ systems, including Charcot–Marie–Tooth disease, infantile-onset progressive leukoencephalopathy with or without deafness, congenital deafness, adult-onset progressive leukoencephalopathy, cardiomyopathies, and immune‑hematological disorders.[2][14] This heterogeneity implies that specific KARS1 variants, genetic background, and possibly environmental factors modulate disease expression, and underscores the need for precise genotype–phenotype correlations in clinical practice.

Within this broad spectrum, LEPID occupies the segment characterized by early-onset white matter disease, brainstem/spinal cord calcifications, neurosensory deficits (particularly hearing loss), and systemic mitochondrial signs, often with a rapidly progressive course in early life.[1][2][7][9][11] The Orphanet ORPHA:3240 entity, described as “early-onset progressive leukoencephalopathy–central nervous system calcification–deafness–visual impairment syndrome,” appears to reconcile many of these features and likely corresponds to KARS1-associated LEPID.[9] However, the existence of overlapping and partially distinct phenotypes necessitates careful phenotypic annotation in disease knowledge bases, including explicit mapping to MONDO terms for specific clinical entities and cross-references to gene-level KARS1 annotations.

### 2.3 Risk Factors, Protective Factors, and Gene–Environment Interactions

As a monogenic autosomal recessive disorder caused by biallelic pathogenic variants in KARS1, LEPID’s primary “risk factor” is the presence of two deleterious KARS1 alleles, typically inherited from carrier parents.[1][11][13][14] There is currently no evidence for common susceptibility loci or modifier genes in genome-wide association studies, and given the rarity and severity of the disease, such studies have not been performed. However, the existence of multiple, clinically distinct KARS1-related phenotypes suggests that other genetic factors may act as modifiers of severity, age at onset, or organ involvement. The loss-of-function KARS review, by cataloguing diverse phenotypes linked to KARS1, implicitly supports the notion that genetic context influences disease expression, but specific modifier genes have not yet been identified.[14]

Environmental risk factors, in the sense of exposures that increase the likelihood of developing LEPID in individuals without biallelic KARS1 variants, are not known, as the disease is strictly dependent on germline mutations. However, certain environmental or physiological stressors—especially infections and fever—are reported to precipitate episodic neurologic regression and clinical deterioration in affected children. Malacards notes that “Neurologic regression associated with infection or fever” is a trait of LEPID, and OMIM indicates that affected individuals show episodic regression with progressive motor deterioration, implying that intercurrent illness can exacerbate symptoms.[1][11] This pattern is consistent with many mitochondrial diseases, in which energy-demanding states such as fever or systemic infection overwhelm compromised oxidative phosphorylation, leading to acute decompensation. Thus, while environment does not cause LEPID, it modulates disease course and should be considered in counseling and management.

Protective factors—either genetic variants that mitigate disease severity or environmental exposures that reduce risk—have not been systematically described for LEPID. Given the essential role of KARS1 in protein synthesis, it is unlikely that common protective variants exist that fully counteract biallelic loss-of-function; however, partial compensation by other components of the translational machinery or mitochondrial biogenesis pathways cannot be excluded. Similarly, general measures that support mitochondrial health, such as avoidance of fasting, proper nutrition, and aggressive management of infections, may help to prevent acute decompensation, but robust data for LEPID are lacking.[1][2][11][14]

Gene–environment interactions in LEPID are therefore best conceptualized as interactions between the underlying KARS1-mediated mitochondrial translation defect and external stressors that increase metabolic demand. Infections, fever, and possibly other factors such as anesthesia or certain drugs may precipitate regression or seizures in affected children by exacerbating energy deficits in the brain and other organs. This model, inferred from clinical observation and general mitochondrial disease principles, aligns with the report that neurologic regression is associated with infection or fever in LEPID.[1][11] Further research is needed to delineate specific triggers and to develop evidence-based recommendations for avoidance or prophylaxis.

### 2.4 Inheritance Pattern, Penetrance, and Population Distribution

LEPID is consistently described as an autosomal recessive disorder, with affected individuals carrying homozygous or compound heterozygous pathogenic KARS1 variants and unaffected carrier parents.[1][2][9][11][13][14] OMIM explicitly notes that LEPID is an autosomal recessive complex neurodegenerative disorder, and reports by Itoh et al. and Ruzzenente et al. document segregation patterns compatible with recessive inheritance in families where parental DNA was available.[2][9][11] ClinVar entries for individual KARS1 variants linked to LEPID list their origin as “germline” and report biallelic configurations in affected individuals.[3][6][10][13] The autosomal recessive inheritance implies that each child of two carriers has a 25% risk of being affected, a 50% chance of being a carrier, and a 25% chance of inheriting two normal alleles, assuming random segregation and absence of de novo mutations.

Penetrance appears to be high or complete for biallelic pathogenic variants, as all reported individuals with such variants exhibit clinical disease; there are no descriptions of asymptomatic homozygous carriers.[1][2][11][12][14] However, expressivity is variable, with differences in severity, age at onset, organ involvement, and rate of progression, even among individuals with similar or identical KARS1 variants. For example, patients with p.Arg505His (R505H) or p.Arg477His (R477H) show both infantile-onset LEPID and adult-onset DEAPLE phenotypes in different reports, suggesting that expressivity may be influenced by additional genetic or environmental factors.[11][13][14] Age-dependent penetrance is relevant for DEAPLE, where neurologic manifestations emerge in adulthood, but for LEPID the onset is typically in infancy or early childhood, and penetrance of developmental delay, neurologic regression, and imaging abnormalities appears uniform among affected children.[1][2][9][11]

Epidemiologic data are scant because of the rarity of LEPID. Orphanet estimates the prevalence of the clinically similar ORPHA:3240 disorder at less than 1 per 1,000,000, consistent with a very rare autosomal recessive condition with limited reported cases worldwide.[9] OMIM and primary reports indicate that LEPID has been documented in multiple geographic regions, including Japan (Itoh et al.), France (Ruzzenente et al.), Italy (Ardissone et al.), Colombia (Vargas et al.), Saudi Arabia (JBC Genetics report), and Canada (McMillan et al.), implying that the disease is panethnic but extremely rare.[2][7][11][12][13][14] Some variants, such as p.Pro228Leu (P228L), have low but detectable frequency in population databases like ExAC (0.014%), supporting their status as rare recessive alleles that can cause disease in homozygous or compound heterozygous states.[6][11] Consanguinity appears to play a role in certain families with homozygous variants, particularly in populations with higher consanguineous marriage rates such as Japan and Saudi Arabia, but systematic data are not available.[2][11][14]

Carrier frequency for pathogenic KARS1 variants has not been formally determined, but given the rarity of disease and the low allele frequencies reported in ExAC and other databases, it is likely to be very low in the general population.[6][11] There is no evidence of founder mutations confined to specific ethnic groups, although the concentration of particular variants in certain cohorts (e.g., Japanese families studied by Itoh et al.) may reflect local founder effects or ascertainment bias.[11] Sex ratio appears to be approximately equal, as both males and females are affected in reported series, and there is no indication of sex-linked inheritance or sex-specific penetrance.[1][2][9][11][14]

## 3. Clinical Phenotypes and Natural History

### 3.1 Neurological and Developmental Features

The neurological phenotype of LEPID is dominated by early-onset progressive leukoencephalopathy with associated developmental delay, motor dysfunction, and episodic neurologic regression. OMIM and Malacards summarize that affected individuals present in infancy or early childhood with hypotonia, delayed motor milestones, global developmental delay, and impaired intellectual development, often with poor or absent speech.[1][11] Itoh et al. reported seven children with LEPID in whom hypotonia, delayed walking or inability to walk, and global developmental delay were consistent early features; many required assistance for mobility and failed to develop effective verbal communication.[11] Over time, these children experienced episodic regression, often associated with infection or fever, leading to progressive motor deterioration, spastic tetraplegia, and loss of ambulation.[1][11] Malacards notes “Neurologic regression associated with infection or fever” and “spastic tetraplegia” as traits of LEPID, highlighting the dynamic and progressive nature of neurologic impairment.[1]

Seizures are common in LEPID, frequently intractable and contributing to morbidity. Orphanet describes seizures in the majority of patients with early-onset progressive leukoencephalopathy–central nervous system calcification–deafness–visual impairment syndrome, and OMIM notes that the children reported by Itoh et al. had intractable seizures, often difficult to control with standard antiepileptic medications.[9][11] McMillan et al.’s siblings with KARS mutations also had epilepsy, which the authors include as a key part of the phenotype in their paper titled “Congenital Visual Impairment and Progressive Microcephaly Due to Lysyl-Transfer Ribonucleic Acid (RNA) Synthetase (KARS) Mutations: The Expanding Phenotype of Aminoacyl-Transfer RNA Synthetase Mutations in Human Disease.”[12] Seizure onset is typically in infancy or early childhood, in parallel with developmental delay and white matter changes, and the seizures may worsen during episodes of metabolic stress.

Cognitive impairment is universal in reported LEPID cases, ranging from severe intellectual disability with absent speech to moderate delay with limited communication. OMIM indicates “impaired intellectual development with poor or absent speech” as a characteristic feature.[11] The JBC Genetics case of a Saudi child with LEPID describes global developmental delay and regressive course, with loss of previously acquired skills, consistent with severe cognitive impact.[2] McMillan et al. describe “developmental delay” alongside progressive microcephaly and seizure in their KARS-mutated siblings, emphasizing that KARS1 dysfunction leads to profound neurodevelopmental effects.[12] These observations suggest that LEPID’s impact on quality of life is particularly severe in the cognitive and communicative domains, and that early identification and supportive interventions, though unlikely to halt disease progression, are essential for maximizing developmental potential.

From a natural history standpoint, the neurologic phenotype evolves from hypotonia and developmental delay in infancy to spasticity, tetraplegia, seizures, and severe cognitive impairment by early childhood, with episodes of acute regression superimposed on a chronic progressive course.[1][2][9][11][12][14] Many children lose ambulation and require wheelchair or bedbound care, and epilepsy, feeding difficulties, and respiratory complications become major determinants of daily functioning. There is no evidence for spontaneous remission, and the disease is universally chronic and progressive, leading to severe disability and, in many cases, early death.[1][2][11][14] For phenotype annotation, key Human Phenotype Ontology (HPO) terms include leukoencephalopathy (HP:0002415), global developmental delay (HP:0001263), intellectual disability (HP:0001249), absent speech (HP:0001344), spastic tetraplegia (HP:0002500), hypotonia (HP:0001252), and seizures (HP:0001250), each with severe impact on quality of life.

### 3.2 Auditory, Visual, and Cognitive Neurosensory Impairment

Sensorineural hearing loss is among the most defining features of LEPID, present in most but not all reported patients. OMIM notes that “Most patients present with sensorineural deafness or hypoacousia,” and Orphanet describes “early-onset or congenital deafness (only few cases reported without hearing loss)” in the closely related ORPHA:3240 disorder.[9][11] The mt‑ARS review lists KARS1 among seven mitochondrial aminoacyl‑tRNA synthetase genes reported to cause hereditary sensorineural hearing loss, and includes several KARS1 variants associated with “Leukoencephalopathy, progressive, infantile-onset, with deafness” or “with or without deafness.”[7] ClinVar entries for KARS1 P228L, I318T, and other variants emphasize sensorineural deafness as part of the phenotype and report lactic acidosis, developmental delay, and leukoencephalopathy, supporting the central role of auditory dysfunction in LEPID.[6][10] Given the frequency and clinical impact of hearing loss, HPO terms such as sensorineural hearing impairment (HP:0000407) and congenital deafness (HP:0000387) should be prominently associated with the disease in knowledge bases.

Visual impairment is variably present but can be severe, particularly in phenotypes overlapping LEPID. Orphanet notes “visual impairment” as a characteristic feature of early-onset progressive leukoencephalopathy–central nervous system calcification–deafness–visual impairment syndrome.[9] McMillan et al. explicitly describe “2 siblings with severe infantile visual loss, progressive microcephaly, developmental delay, seizures, and abnormal subcortical white matter,” and emphasize that their phenotype is remarkably similar to that recently reported in glutaminyl‑tRNA synthetase (QARS) mutations.[12] ClinVar and OMIM summaries of KARS-related disease mention optic neuropathy in association with certain KARS1 mutations, and the loss-of-function KARS paper notes that “Mutations in KARS cause a severe neurological and neurosensory disease with optic neuropathy” in some patients.[13][14] Visual loss may manifest as reduced visual acuity, nystagmus, or cortical visual impairment, contributing significantly to functional disability and quality-of-life burden.

Cognitive and behavioral manifestations extend beyond static intellectual disability to progressive decline, particularly in adult-onset KARS1 phenotypes like DEAPLE. ClinVar notes that patients with congenital deafness and adult-onset progressive leukoencephalopathy “presented with progressive cognitive decline later in the second or third decades,” highlighting a neurodegenerative dementing component in these individuals.[13] In LEPID, cognitive impairment is severe from early life, with global developmental delay and limited acquisition of skills, but episodic regression and ongoing demyelination likely further diminish cognitive abilities over time.[1][2][9][11][12] Behavioral abnormalities such as irritability, sleep disturbances, or movement disorders have not been systematically described but are plausible given the extent of cerebral involvement.

The combined neurosensory deficits—hearing loss, visual impairment, and cognitive disability—produce a profound impact on quality of life. Children with LEPID may be unable to communicate effectively, perceive auditory or visual stimuli, or participate in age‑appropriate social and educational activities, placing heavy burdens on families and caregivers. HPO terms such as visual impairment (HP:0000505), optic neuropathy (HP:0000545), nystagmus (HP:0000639), and developmental regression (HP:0002376) should be linked to LEPID in phenotype databases. Qualitative assessments from case reports and series, though limited, indicate a very low health-related quality-of-life state, which could be codified in instruments like EQ‑5D or SF‑36 if systematically measured in future studies.

### 3.3 Systemic Manifestations: Growth, Hematologic, and Hepatic Features

LEPID is not confined to the central nervous system and sensory organs; systemic manifestations reflect underlying mitochondrial dysfunction and multisystem involvement. Poor overall growth and microcephaly are reported in many patients. OMIM and Malacards list “poor overall growth with microcephaly” as a variable but frequent feature, and McMillan et al.’s siblings with KARS mutations had “progressive microcephaly” alongside visual impairment and seizures.[1][11][12] Failure to thrive, weight loss, and stunted linear growth are noted in several case descriptions, likely due to a combination of chronic illness, feeding difficulties, and systemic energy deficits.[1][2][11][12] Microcephaly can be congenital or progressive, and its presence correlates with severe neurodevelopmental impairment.

Hematologic abnormalities, particularly microcytic anemia, occur in a subset of LEPID patients. OMIM and Malacards mention “microcytic anemia” as a variable feature, and the JBC Genetics report of a Saudi child with KARS1-related LEPID emphasizes anemia as part of the phenotype, stating that “He had a matching phenotype of leukoencephalopathy, progressive infantile-onset, with deafness and anemia.”[1][2][11] The loss-of-function KARS paper notes that KARS1 mutations have been linked to “immune-hematological disorders,” although details are not extensively provided in the available excerpt.[2][14] The pathophysiology of anemia in LEPID is not fully understood but may relate to mitochondrial dysfunction in erythroid precursors or systemic nutritional compromise.

Hepatic manifestations are also reported. OMIM notes “hepatic enlargement or abnormal liver enzymes” as additional variable features in LEPID.[11] Malacards lists “hepatic abnormalities” among traits of the disease, and the JBC Genetics case, describing a mitochondrial disorder with progressive leukoencephalopathy, includes lactic acidosis and other metabolic signs that can involve the liver.[1][2] Elevated liver transaminases, hepatomegaly, and steatosis are common findings in mitochondrial disorders and likely reflect impaired oxidative phosphorylation and increased oxidative stress in hepatocytes. Lactic acidosis, noted in ClinVar’s description of the P228L variant (“sensorineural deafness, developmental delay, and lactic acidosis”) implies systemic metabolic dysregulation that may burden the liver’s capacity to clear lactate.[6]

Other systemic features in LEPID and related KARS1 disorders include cardiomyopathy, immune abnormalities, and gastrointestinal symptoms, as suggested by the loss-of-function KARS article’s mention of cardiomyopathies and immune‑hematological disorders associated with homozygous KARS1 variants.[2][14] However, detailed characterization of these manifestations in LEPID-specific cohorts is lacking. Overall, the systemic phenotype reinforces the classification of LEPID as a mitochondrial disease with multi‑organ involvement, though neurological and neurosensory manifestations remain dominant determinants of disability and prognosis. HPO terms relevant to systemic features include microcephaly (HP:0000252), failure to thrive (HP:0001531), microcytic anemia (HP:0001935), hepatomegaly (HP:0002240), elevated serum lactate (HP:0002151), and lactic acidosis (HP:0003128).

### 3.4 Neuroradiologic and Laboratory Phenotypes

Neuroimaging is central to the recognition and diagnosis of LEPID. The hallmark radiologic phenotype consists of deep cerebral white matter abnormalities consistent with a progressive leukoencephalopathy, accompanied by calcifications in the brainstem and spinal cord. OMIM and Malacards state that “Brain imaging shows deep white matter abnormalities consistent with a progressive leukoencephalopathy. The brain and spinal cord are usually both involved; calcifications of these regions are often observed.”[1][11] Orphanet’s description of the ORPHA:3240 disorder notes that “All patients manifest calcifications in brain and spinal cord,” which matches the LEPID imaging pattern.[9] Magnetic resonance imaging (MRI) typically reveals diffuse or patchy T2‑hyperintense lesions in the periventricular and subcortical white matter, while computed tomography (CT) is particularly sensitive for detecting calcifications in the brainstem, cerebellum, and spinal cord. These calcifications help distinguish LEPID from many other leukodystrophies that lack such mineralization.

The radiologic phenotype shares similarities with SNORD118-related leukoencephalopathy with calcifications and cysts, a distinct autosomal recessive disorder characterized by intracranial calcification, cerebral white matter disease, and multiple cysts.[8] A case report of early-infantile onset, rapidly progressive leukoencephalopathy with calcifications and cysts caused by biallelic SNORD118 variants notes that “Leukoencephalopathy with calcifications and cysts is a rare autosomal recessive genetic disorder neuroradiologically characterized by intracranial calcification, cerebral white matter disease, and multiple cysts,” highlighting overlapping imaging features.[8] However, the presence of multiple cysts and the involvement of SNORD118, a noncoding RNA, distinguish this condition from KARS1-associated LEPID. Careful neuroimaging follow-up, as recommended by the SNORD118 case authors, may be necessary when initial exome sequencing fails to reveal coding variants, underscoring the role of imaging in differential diagnosis.[8]

Laboratory phenotypes in LEPID reflect mitochondrial dysfunction. Serum lactate is frequently elevated, and mitochondrial respiratory chain complex deficiencies are detected in muscle or fibroblast biopsies. Malacards and OMIM report that “Laboratory studies show increased serum lactate and deficiencies of mitochondrial respiratory chain complexes, consistent with global mitochondrial dysfunction.”[1][11] ClinVar’s P228L variant record references a publication titled “Inhibition of mitochondrial translation in fibroblasts from a patient expressing the KARS p.(Pro228Leu) variant and presenting with sensorineural deafness, developmental delay, and lactic acidosis,” which directly links KARS1 mutation to impaired mitochondrial translation and lactic acidosis in vitro.[6] The loss-of-function KARS paper summarizes that “Functional and structural analyses revealed that these mutations impair aminoacylation activity of lysyl-tRNA synthetase, indicating that defective KARS function is responsible for the phenotypes in these individuals,” confirming that aminoacylation defects underlie respiratory chain deficiencies.[14]

Additional laboratory findings may include elevated liver transaminases, microcytic anemia, and abnormal metabolic profiles, though specific values are seldom reported.[1][2][9][11] EEG often shows epileptiform discharges or generalized slowing in patients with seizures, and evoked potentials or audiologic tests confirm sensorineural hearing loss.[2][7][11] Collectively, neuroradiologic and laboratory phenotypes provide objective evidence for white matter injury, calcification, and systemic mitochondrial dysfunction, and should be codified with appropriate SNOMED CT, LOINC, and HPO terms in disease knowledge bases.

### 3.5 Quality of Life and Functional Impact

The impact of LEPID on quality of life and functional status is profound and multifaceted, affecting motor abilities, sensory perception, cognition, communication, and systemic health. Children with LEPID often experience delayed attainment of basic developmental milestones and may never achieve independent ambulation or speech.[1][2][9][11][12] Many become wheelchair-bound or bedridden due to spastic tetraplegia, require feeding assistance because of dysphagia or failure to thrive, and depend on caregivers for all activities of daily living. Seizures, often refractory to standard antiepileptic therapy, impose additional burdens, including risk of injury and frequent hospitalizations.[9][11][12] Sensorineural hearing loss and visual impairment limit interaction with the environment, further isolating affected children and complicating educational inclusion.[7][9][12]

While formal quality-of-life instruments such as EQ‑5D, SF‑36, or PROMIS have not been systematically applied to LEPID cohorts, the clinical descriptions clearly indicate extremely low health-related quality-of-life states. Parents and caregivers must manage complex medical needs, including seizure control, nutrition, physical therapy, and respiratory support, often in the context of progressive deterioration and uncertain prognosis.[2][11][14] The high frequency of early mortality magnifies psychological distress for families and underscores the need for palliative care and psychosocial support. In conceptual terms, LEPID likely ranks among the most disabling pediatric neurological disorders on measures of physical functioning, role limitations, social functioning, and general health perception.

From a knowledge base perspective, mapping LEPID to International Classification of Functioning (ICF) domains would highlight severe impairments in mobility, self-care, communication, interpersonal interactions, learning and applying knowledge, and major life areas. HPO terms for “severe intellectual disability,” “spastic tetraplegia,” “sensorineural deafness,” “visual impairment,” and “developmental regression” collectively capture the functional impact, and additional annotations such as “reduced quality of life” or “palliative care required” could be modeled as disease-level attributes. Future studies incorporating standardized patient-reported outcomes or caregiver assessments would be invaluable for quantifying quality-of-life impacts and informing multidisciplinary care strategies.

## 4. Genetic and Molecular Architecture

### 4.1 KARS1 Gene Structure, Function, and Isoforms

KARS1 (lysyl‑tRNA synthetase 1) encodes lysyl‑tRNA synthetase (KARS), an essential enzyme that catalyzes the attachment of lysine to its cognate tRNA, tRNA^Lys, enabling incorporation of lysine into nascent polypeptides during translation.[12][14] McMillan et al. succinctly state that “Lysyl-transfer RNA synthetase (KARS) links the amino acid lysine to its cognate transfer RNA,” highlighting its fundamental role in protein synthesis.[12] KARS is unusual among aminoacyl‑tRNA synthetases in being bifunctional, with both cytosolic and mitochondrial isoforms produced by alternative splicing or post-translational modifications, allowing it to participate in translation in both compartments.[14] The gene is located on chromosome 16q23.1, as indicated by OMIM and ClinVar entries, and spans multiple exons encoding a protein with catalytic and anticodon-binding domains.[11][13][14]

Structurally, lysyl‑tRNA synthetase belongs to the class II aminoacyl‑tRNA synthetase family and contains highly conserved motifs that bind ATP, lysine, and the tRNA anticodon loop. The loss-of-function KARS paper describes functional and structural analyses of mutant KARS proteins, noting that “Functional and structural analyses revealed that these mutations impair aminoacylation activity of lysyl-tRNA synthetase,” and likely affect regions critical for catalytic efficiency or substrate binding.[14] Mutations such as p.Pro228Leu occur in the anticodon-binding domain, while others like p.Arg438Trp and p.Glu525Lys lie in the catalytic core, reinforcing the notion that disruption of these regions can severely compromise enzyme function.[6][12][14] The existence of multiple domains suggests potential differential effects of mutations on cytosolic versus mitochondrial localization or function, which may contribute to phenotype heterogeneity.

Because KARS1’s mitochondrial isoform is essential for mitochondrial translation, its dysfunction has particularly severe consequences for tissues with high oxidative phosphorylation demands, such as the brain, auditory system, and heart. The mt‑ARS review lists KARS1 among several mitochondrial aminoacyl‑tRNA synthetases implicated in hereditary sensorineural hearing loss, highlighting the specific vulnerability of the auditory system to mitochondrial translational defects.[7] In addition, KARS interacts with other components of the translation apparatus and may participate in noncanonical functions such as signaling or stress responses, though these roles are not well characterized in human disease.[14] Gene Ontology (GO) terms relevant to KARS1’s function include “lysine-tRNA ligase activity” (GO:0004827), “tRNA aminoacylation for protein translation” (GO:0006418), “mitochondrial translation” (GO:0032543), and “cytosolic translation” (GO:0002181).

### 4.2 Catalog of Pathogenic Variants in LEPID

A growing catalog of pathogenic KARS1 variants has been associated with LEPID and closely related phenotypes. These variants are primarily missense changes, though frameshift and splice-site mutations also occur. The mt‑ARS review provides a useful snapshot of KARS1 variants linked to hereditary hearing loss and leukoencephalopathy. Among those explicitly associated with “Leukoencephalopathy, progressive, infantile-onset, with deafness” or “with or without deafness” are c.1702C>T (p.Leu568Phe), c.1573G>A (p.Glu525Lys), c.1354del (p.Leu452fs), c.1328T>C (p.Leu443Pro), and c.795+1G>A, with references to Demain et al. (2020), McMillan et al. (2015), Ruzzenente et al. (2018), Itoh et al. (2019), and ClinVar.[7] The p.Leu568Phe variant affects a highly conserved residue in the catalytic domain and was associated with infantile-onset progressive leukoencephalopathy with deafness in Demain et al.’s report, though details are not fully available in the excerpt.[7] McMillan et al.’s c.1573G>A (p.Glu525Lys) mutation occurs in a highly conserved region of the catalytic domain and was found in compound heterozygosity with c.1312C>T (p.Arg438Trp) in their two siblings with visual impairment, microcephaly, and leukoencephalopathy.[12]

Ruzzenente et al., as summarized in OMIM and ClinVar, described compound heterozygous KARS1 mutations c.683C>T (p.Pro228Leu) and c.1438delC (p.Leu480TrpfsTer3) in a French girl with infantile-onset progressive leukoencephalopathy with deafness.[6][11] The p.Pro228Leu substitution occurs at a highly conserved residue in the anticodon-binding domain, while the frameshift p.Leu480TrpfsTer3 introduces a premature termination codon, both predicted to impair protein function.[6][11][14] ClinVar’s entry for the P228L variant notes experimental evidence that “Inhibition of mitochondrial translation underlies the disease mechanism,” based on fibroblast studies from this patient.[6] Itoh et al. identified additional mutations, including a splice-site variant c.795+1G>A and missense changes such as those designated 601421.0012 and 601421.0013 in OMIM (exact amino acid changes not fully visible in the excerpt), in Japanese children with LEPID.[11]

ClinVar and OMIM provide further variant-level detail. The NM_005548.3(KARS1):c.1312C>T (p.Arg438Trp) variant is classified as pathogenic for LEPID based on McMillan et al.’s report, with literature-only evidence and the citation “Congenital visual impairment and progressive microcephaly due to lysyl-transfer ribonucleic acid (RNA) synthetase (KARS) mutations: the expanding phenotype of aminoacyl-transfer RNA synthetase mutations in human disease.”[3][12] The NM_001130089.2(KARS1):c.683C>T (p.Pro228Leu) variant is classified as pathogenic for “LEUKOENCEPHALOPATHY, PROGRESSIVE, INFANTILE-ONSET, WITH DEAFNESS,” with functional data showing inhibited mitochondrial translation.[6][11] The NM_005548.3(KARS1):c.953T>C (p.Ile318Thr) variant is listed by ClinVar as likely pathogenic for LEPID; the record notes that biallelic KARS1 variants have been linked to sensorineural hearing loss, neuropathy, seizures, and leukodystrophy, and that the gene has recently been linked to progressive infantile-onset leukoencephalopathy with or without deafness, citing PMIDs including 23596069, 33942428, 34172899, 30715177, and 25330800.[10]

ClinVar’s entry for c.1430G>A (p.Arg477His) primarily associates this variant with congenital deafness and adult-onset progressive leukoencephalopathy (DEAPLE), but OMIM notes that in a Colombian boy with LEPID, Vargas et al. (2020) identified compound heterozygous missense mutations R477H and A526V (A498V), both present at very low frequencies in public databases.[11][13] Another variant, p.Arg505His (R505H), was found homozygous in an Italian boy with infantile-onset progressive leukoencephalopathy with deafness, originally reported by Orcesi et al. and later linked to KARS1.[13] Loss-of-function KARS analyses mention additional variants such as p.T587M and other changes affecting aminoacylation activity.[14] Population frequency data from ExAC and gnomAD, as cited in OMIM and ClinVar, indicate that many of these variants are extremely rare or absent from large datasets, consistent with pathogenicity.[6][11][13]

### 4.3 Functional Consequences and Loss-of-Function Mechanisms

Functional studies of KARS1 variants in LEPID and related disorders provide compelling evidence for a loss‑of‑function mechanism centered on impaired aminoacylation and mitochondrial translation. The loss-of-function KARS paper states that “Functional and structural analyses revealed that these mutations impair aminoacylation activity of lysyl-tRNA synthetase, indicating that defective KARS function is responsible for the phenotypes in these individuals.”[14] This conclusion is based on enzymatic assays showing reduced charging of tRNA^Lys by mutant KARS proteins, structural modeling indicating disruption of key catalytic or binding residues, and possibly complementation studies in model systems, though the latter are not detailed in the excerpt.[14] Mutations located in the anticodon-binding domain, such as p.Pro228Leu, likely impair recognition or binding of tRNA^Lys, while those in the catalytic core, such as p.Arg438Trp or p.Glu525Lys, may directly reduce catalytic efficiency.[6][12][14]

The P228L variant has been studied in patient fibroblasts, where investigators observed inhibition of mitochondrial translation, a direct downstream consequence of impaired mitochondrial KARS1 function.[6][11] ClinVar notes that “Inhibition of mitochondrial translation in fibroblasts from a patient expressing the KARS p.(Pro228Leu) variant and presenting with sensorineural deafness, developmental delay, and lactic acidosis,” and OMIM summarizes Ruzzenente et al.’s conclusion that “inhibition of mitochondrial translation underlies the disease mechanism.”[6][11] Reduced mitochondrial translation leads to decreased synthesis of mitochondrially encoded subunits of oxidative phosphorylation complexes, causing respiratory chain deficiencies as documented in laboratory studies of LEPID patients.[1][11][14] This, in turn, results in impaired ATP production, increased reliance on glycolysis, and accumulation of lactate, explaining the lactic acidosis observed clinically.[1][2][6][11]

The functional consequences of frameshift and splice-site variants are presumed to include truncated or absent KARS protein, leading to more severe loss-of-function. For example, the c.1438delC (p.Leu480TrpfsTer3) variant introduces a premature stop codon, likely causing nonsense-mediated mRNA decay or production of a nonfunctional truncated protein.[6][11][14] The c.795+1G>A splice-site variant probably disrupts normal splicing, resulting in exon skipping or intron retention and loss of functional protein.[7][11] Together, these mutations reinforce the concept that LEPID arises when KARS1 function falls below a critical threshold for maintaining adequate mitochondrial translation and oxidative phosphorylation, particularly in tissues with high energy demands.

There is currently no evidence for gain-of-function or dominant-negative mechanisms in LEPID. Dominant KARS1 mutations have not been reported; all described pathogenic variants in this context are recessive and cause disease only when biallelic, consistent with loss-of-function.[1][2][11][13][14] Somatic mutations in KARS1 have not been implicated in cancer or other somatic diseases in the available data, and ClinVar notes “Somatic classification of clinical impact: None” for several LEPID-associated variants.[3][6][10][13] Thus, germline loss-of-function or severely hypomorphic KARS1 alleles are the primary determinants of LEPID, and therapeutic strategies should focus on restoring or compensating for KARS1 function rather than inhibiting its activity.

### 4.4 Modifier Genes, Epigenetic Factors, and Structural Variation

At present, specific modifier genes that alter LEPID severity or expression have not been identified. However, the phenotypic diversity of KARS1-related disease, ranging from LEPID to DEAPLE, Charcot–Marie–Tooth neuropathy, congenital visual impairment, and immune-hematological disorders, suggests that genetic background plays a role in shaping clinical manifestations.[2][11][12][14] It is plausible that variants in genes involved in mitochondrial biogenesis, oxidative phosphorylation, myelination, or sensory organ development could modulate the impact of KARS1 dysfunction, but such hypotheses remain untested. Future exome or genome-wide association studies in larger cohorts of KARS1-mutated patients may reveal modifier loci, though the rarity of the disease poses challenges.

Epigenetic factors, such as DNA methylation or histone modifications affecting KARS1 expression or mitochondrial gene regulation, have not been specifically studied in LEPID. However, broader research on mitochondrial diseases suggests that epigenetic regulation of nuclear-encoded mitochondrial genes can influence disease severity, and that epigenetic therapies may have potential in modulating mitochondrial function. In LEPID, epigenetic changes might arise secondary to chronic illness or as adaptive responses to energy deficits, but there is no direct evidence from the available literature.[1][2][11][14] Disease knowledge bases can therefore note epigenetic mechanisms as speculative or inferred rather than demonstrated.

Chromosomal structural abnormalities involving KARS1 have not been reported as causes of LEPID. The gene resides in a relatively stable region of chromosome 16, and all described pathogenic variants are single nucleotide substitutions, small insertions/deletions, or splice-site changes rather than large deletions, duplications, or translocations.[3][6][10][11][13][14] DECIPHER and other structural variation databases may contain KARS1‑adjacent CNVs, but these have not been linked to LEPID in the current data. Consequently, chromosomal microarray or karyotyping is unlikely to detect LEPID-causing variants and should be considered secondary to sequence-based methods.

## 5. Pathophysiology and Mechanistic Causal Chain

### 5.1 Ordered Causal Chain from Mutation to Clinical Phenotype

In LEPID, the mechanistic sequence from initiating lesion to clinical manifestation can be conceptualized as follows, with each step explicitly stating its causal relationship and noting where inference is involved.

Step 1: Biallelic germline pathogenic variants in KARS1 (missense, frameshift, or splice-site) lead to reduced or dysfunctional lysyl‑tRNA synthetase 1, impairing its ability to aminoacylate tRNA^Lys in both cytosolic and mitochondrial compartments, as demonstrated by enzymatic and structural analyses.[12][14]

Step 2: Impaired mitochondrial KARS1 function results in defective aminoacylation of mitochondrial tRNA^Lys, which leads to inhibition of mitochondrial translation and decreased synthesis of mitochondrially encoded subunits of oxidative phosphorylation complexes, as shown in patient fibroblast studies and inferred from respiratory chain deficiencies.[6][11][14]

Step 3: Reduced mitochondrial translation leads to combined deficiencies of oxidative phosphorylation complexes (e.g., complexes I, III, IV, and V), resulting in impaired ATP production, increased reliance on glycolysis, and accumulation of lactate, producing lactic acidosis and systemic energy failure, as evidenced by elevated serum lactate and respiratory chain defects.[1][2][6][11]

Step 4: Chronic and episodic energy failure in high-demand tissues such as cerebral white matter, brainstem, spinal cord, auditory pathways, and visual system leads to cellular stress, impaired myelination, oligodendrocyte dysfunction, axonal injury, and ultimately white matter degeneration and calcification, a mechanism inferred from neuroradiologic findings and general mitochondrial disease principles.[1][8][9][11][14]

Step 5: White matter degeneration, brainstem/spinal cord calcifications, and neurosensory pathway damage result in clinical manifestations including global developmental delay, intellectual disability, spastic tetraplegia, seizures, sensorineural deafness, visual impairment, and episodic regression, as observed in affected individuals.[1][2][9][11][12][14]

Step 6: Systemic energy failure and mitochondrial dysfunction in peripheral tissues such as liver, bone marrow, and heart lead to secondary manifestations including microcytic anemia, hepatic enlargement or elevated liver enzymes, lactic acidosis, and possibly cardiomyopathy and immune-hematological abnormalities, which are reported in some KARS1-related disorders and inferred for LEPID.[1][2][11][14]

Step 7: Intercurrent infections, fever, and other physiologic stressors increase metabolic demands and further compromise already impaired mitochondrial function, leading to episodic neurologic regression, seizure exacerbation, and acute decompensation, a mechanism inferred from clinical observations of regression associated with infection or fever.[1][11]

Step 8: Over time, cumulative tissue injury, progressive demyelination, neurosensory loss, and systemic complications culminate in severe disability and early death in many affected children, as documented in natural history reports.[1][2][11][14]

This causal chain distinguishes upstream mechanisms (KARS1 mutations, impaired aminoacylation, inhibited mitochondrial translation) from downstream consequences (respiratory chain failure, white matter degeneration, clinical phenotypes), and acknowledges that several steps are inferred based on general mitochondrial biology and leukodystrophy pathophysiology rather than directly demonstrated in LEPID-specific experiments.

### 5.2 Mitochondrial Translation Defect and Respiratory Chain Failure

The core molecular pathway implicated in LEPID is mitochondrial translation and its impact on oxidative phosphorylation. KARS1 mutations impair the charging of mitochondrial tRNA^Lys, an essential substrate for translation of mitochondrially encoded proteins. Ruzzenente et al., as summarized in ClinVar and OMIM, concluded that “inhibition of mitochondrial translation underlies the disease mechanism” in a French girl with infantile-onset progressive leukoencephalopathy with deafness harboring P228L and frameshift KARS1 mutations.[6][11] Functional experiments in fibroblasts from this patient showed inhibited mitochondrial translation, directly linking KARS1 dysfunction to reduced synthesis of mitochondrial-encoded respiratory chain subunits.[6] The loss-of-function KARS paper reinforces this mechanism, noting that “Functional and structural analyses revealed that these mutations impair aminoacylation activity of lysyl-tRNA synthetase,” which would necessarily reduce mitochondrial translation efficiency.[14]

Reduced mitochondrial translation leads to quantitative and qualitative defects in oxidative phosphorylation complexes, particularly those containing mitochondrially encoded subunits. These include complex I (NADH dehydrogenase), complex III (cytochrome bc1), complex IV (cytochrome c oxidase), and complex V (ATP synthase), all of which are partially encoded by mitochondrial DNA. Laboratory studies in LEPID report “deficiencies of mitochondrial respiratory chain complexes,” and elevated serum lactate, consistent with secondary respiratory chain failure.[1][11] This pattern is characteristic of many mt‑ARS disorders, where defective charging of specific mitochondrial tRNAs leads to combined oxidative phosphorylation deficiencies and lactic acidosis. The GO terms “mitochondrial translation” (GO:0032543), “oxidative phosphorylation” (GO:0006119), and “respiratory chain” (GO:0070469) are central to LEPID pathophysiology.

Respiratory chain failure impairs ATP production, forcing cells to rely more on glycolysis for energy and leading to accumulation of lactate as an end product of anaerobic metabolism. Elevated lactate and lactic acidosis are hallmark biochemical features of mitochondrial diseases and are documented in LEPID patients.[1][2][6][11] ClinVar’s P228L record explicitly notes lactic acidosis in the patient studied, and the JBC Genetics case refers to a “mitochondrial disorder with progressive leukoencephalopathy” in a child with lactic acidosis.[2][6] The resulting energy deficit is particularly deleterious for tissues with high ATP demands and limited glycolytic capacity, such as oligodendrocytes, neurons, inner hair cells of the cochlea, retinal cells, and cardiomyocytes, explaining the multisystem involvement of LEPID.

### 5.3 Cellular and Tissue-Level Mechanisms of White Matter Injury

At the cellular level, LEPID’s primary neuropathologic feature is white matter injury, which can arise from a combination of oligodendrocyte dysfunction, axonal degeneration, and microvascular changes associated with calcification. While direct histopathological studies in LEPID are sparse, neuroradiologic findings and general principles of leukodystrophy provide a framework for inference. Deep cerebral white matter abnormalities on MRI, together with brainstem and spinal cord calcifications on CT, suggest widespread demyelination and possibly necrosis or mineral deposition in these regions.[1][9][11] Oligodendrocytes, the myelinating cells of the central nervous system, have high metabolic demands and rely on robust mitochondrial function to maintain myelin sheath integrity. In LEPID, mitochondrial respiratory chain failure likely impairs oligodendrocyte survival and function, leading to demyelination and weakening of axonal conduction.[1][11][14]

Neurons, particularly long‑projection fibers traversing white matter tracts, are also vulnerable to energy deficits. Axonal degeneration in major tracts such as the corticospinal pathways could contribute to spastic tetraplegia and motor dysfunction. Calcifications in the brainstem and spinal cord may represent dystrophic mineralization in areas of chronic injury or microvascular compromise. Orphanet notes that “All patients manifest calcifications in brain and spinal cord” in the ORPHA:3240 disorder, and similar calcifications are reported in LEPID.[9][11] The precise cellular mechanisms of calcification (e.g., microglial activation, vascular basement membrane mineralization) are not delineated but likely involve chronic inflammation, cell death, and disrupted calcium homeostasis, which can be exacerbated by mitochondrial dysfunction.

The SNORD118-related leukoencephalopathy with calcifications and cysts provides a useful comparative model. In that condition, biallelic variants in a small nucleolar RNA lead to a distinct but overlapping phenotype characterized by intracranial calcification, cerebral white matter disease, and multiple cysts.[8] The authors of a case report note that “As SNORD118 variants might be missed by regular whole-exome sequencing, careful neuroimaging follow-up may be necessary to diagnose this disease,” highlighting the importance of imaging in identifying calcifications and cysts.[8] Although the molecular mechanism differs from LEPID, both disorders illustrate how primary defects in RNA processing or translation can lead to white matter injury, calcification, and cyst formation. For LEPID, the predominant mechanism is impaired mitochondrial translation leading to energy deficits in oligodendrocytes and neurons.

Relevant GO terms for cellular processes in LEPID include “myelination” (GO:0042552), “axonogenesis” (GO:0007409), “neuron death” (GO:0008213), “cellular response to oxidative stress” (GO:0034599), and “calcium ion homeostasis” (GO:0055074). Cell Ontology (CL) terms for affected cell types include “oligodendrocyte” (CL:0000128), “neuron” (CL:0000540), “microglial cell” (CL:0000129), and “astrocyte” (CL:0000127). The exact contribution of each cell type to LEPID pathogenesis has not been experimentally mapped, but oligodendrocytes and neurons are likely central, given the leukoencephalopathy and neurodegeneration.

### 5.4 Systemic Metabolic and Organ-Level Pathophysiology

Beyond the central nervous system, LEPID involves systemic metabolic and organ-level pathophysiology driven by mitochondrial dysfunction. Lactic acidosis, elevated serum lactate, and microcytic anemia reflect global energy deficits and possible impairment of mitochondrial function in peripheral tissues.[1][2][6][11] Hepatic enlargement and abnormal liver enzymes suggest hepatocellular stress, steatosis, or fibrosis arising from oxidative phosphorylation failure in hepatocytes.[11] Cardiomyopathies described in some KARS1-related disorders indicate sensitivity of the heart to KARS1 dysfunction, though specific data for LEPID are limited.[2][14] Immune-hematological disorders mentioned in the loss-of-function KARS paper may involve bone marrow mitochondrial dysfunction, leading to anemia, leukopenia, or thrombocytopenia.[2][14]

The auditory phenotype, characterized by sensorineural hearing loss, likely arises from mitochondrial dysfunction in cochlear hair cells, spiral ganglion neurons, or stria vascularis, all of which are highly dependent on ATP for ion transport and synaptic transmission.[7][11][14] Mitochondrial diseases frequently cause hearing loss, and KARS1 is one of several mt‑ARS genes implicated in hereditary sensorineural hearing loss, underscoring the vulnerability of the auditory system to translational defects.[7] Visual impairment and optic neuropathy may similarly reflect energy failure in retinal ganglion cells, photoreceptors, or optic nerve fibers. McMillan et al.’s siblings with severe infantile visual loss and progressive microcephaly provide a compelling example of KARS1-related visual system involvement.[12]

Systemic metabolic changes associated with LEPID include increased reliance on glycolysis, accumulation of lactate and pyruvate, and possible abnormalities in amino acid or lipid metabolism, though specific metabolomic studies are not available. In general, mitochondrial respiratory chain deficiency leads to a shift in cellular metabolism toward anaerobic pathways, with CHEBI-relevant entities such as lactate (CHEBI:28358), pyruvate (CHEBI:15361), and ATP (CHEBI:30616) playing key roles. Organ-level consequences of chronic lactic acidosis may include fatigue, muscle weakness, and multi-organ dysfunction. For knowledge base annotation, relevant UBERON terms include “brain” (UBERON:0000955), “white matter of brain” (UBERON:0002436), “spinal cord” (UBERON:0002240), “cochlea” (UBERON:0001755), “optic nerve” (UBERON:0000941), “liver” (UBERON:0002107), and “heart” (UBERON:0000948).

### 5.5 Molecular Profiling and Emerging Mechanistic Insights

To date, there are no published large-scale transcriptomic, proteomic, metabolomic, or lipidomic profiling studies specifically focused on LEPID. However, the functional analyses of KARS1 variants and patient-derived fibroblasts provide molecular-level insights that can be integrated with general knowledge of mitochondrial disease. Ruzzenente et al.’s work on P228L fibroblasts demonstrates inhibited mitochondrial translation, and likely observed altered expression or assembly of respiratory chain complexes, though detailed transcriptomic or proteomic data are not available in the excerpt.[6][11] The loss-of-function KARS paper’s structural modeling of mutant KARS proteins provides insight into how specific amino acid changes disrupt active sites or tRNA binding, informing computational predictions of pathogenicity and guiding further functional studies.[14]

In the broader mt‑ARS context, research has shown that different aminoacyl‑tRNA synthetase mutations can produce tissue-specific phenotypes despite ubiquitous expression, possibly due to differential isoform usage, local translation demands, or compensatory mechanisms.[7][14] For KARS1, the bifunctional nature and dual localization may create complex interactions between cytosolic and mitochondrial translation systems. Single-cell RNA sequencing or spatial transcriptomics could, in principle, reveal cell-type specific expression patterns of KARS1 and downstream oxidative phosphorylation genes in brain and cochlea, shedding light on why certain tissues are preferentially affected. However, such advanced technologies have not yet been applied to LEPID, and any discussion of their implications remains speculative.[1][2][11][14]

Future mechanistic research could include CRISPR-based functional genomics screens to identify pathways that modulate vulnerability to KARS1 loss-of-function, or multi-omics integration to correlate KARS1 variant type with specific molecular signatures. In vitro models using induced pluripotent stem cells (iPSCs) differentiated into neurons, oligodendrocytes, or cochlear hair cell-like cells could be used to study cell-type specific responses to KARS1 deficiency. These directions, while not yet realized, align with general trends in mitochondrial disease research and could greatly enhance mechanistic understanding of LEPID.

## 6. Anatomical Structures and Temporal Development

### 6.1 Organ, Tissue, and Cell Types Affected

The primary organ affected in LEPID is the central nervous system, particularly cerebral white matter, brainstem, and spinal cord. OMIM and Orphanet consistently describe progressive leukoencephalopathy and calcifications in brain and spinal cord, indicating widespread involvement of CNS structures.[1][9][11] UBERON terms relevant to these structures include “cerebrum” (UBERON:0000956), “white matter of brain” (UBERON:0002436), “brainstem” (UBERON:0002298), and “spinal cord” (UBERON:0002240). Within the CNS, specific tissue types affected include nervous tissue (white matter tracts, gray matter nuclei) and supporting glial tissues, with oligodendrocytes, neurons, astrocytes, and microglia being the primary cell populations involved.[1][9][11][14]

The auditory system is a secondary but critical organ system affected. Sensorineural hearing loss in LEPID implies damage to inner ear structures such as the cochlea, organ of Corti, inner hair cells, and auditory nerve. UBERON terms include “cochlea” (UBERON:0001755) and “cranial nerve VIII” (UBERON:0000943), while CL terms for relevant cell types include “inner hair cell of cochlea” (CL:0000203) and “spiral ganglion neuron.”[7][11] The visual system, including retina and optic nerve, is also implicated in many KARS1-related phenotypes.[9][12][13][14] UBERON terms “retina” (UBERON:0001476) and “optic nerve” (UBERON:0000941) and CL terms such as “retinal ganglion cell” (CL:0000740) are pertinent.

Peripheral organs affected include the liver, bone marrow (for hematologic manifestations), and possibly heart and immune system. OMIM mentions hepatic enlargement and abnormal liver enzymes, suggesting hepatocellular involvement.[11] Microcytic anemia implies bone marrow or erythroid precursor dysfunction, and cardiomyopathies have been reported in other KARS1-related contexts.[2][11][14] UBERON terms include “liver” (UBERON:0002107), “bone marrow” (UBERON:0002371), and “heart” (UBERON:0000948). CL terms such as “hepatocyte” (CL:0000182), “erythrocyte” (CL:0000232), and “cardiomyocyte” (CL:0000746) can be associated.

At the tissue level, LEPID predominantly affects nervous tissue (central and peripheral), but also involves connective and epithelial tissues through systemic manifestations. White matter tracts, composed of myelinated axons and oligodendrocytes, are particularly vulnerable to mitochondrial dysfunction. GO cellular component terms like “myelin sheath” (GO:0043209), “axon” (GO:0030424), and “mitochondrion” (GO:0005739) are central to modeling LEPID’s tissue pathology.

### 6.2 Subcellular Localization and Compartmental Vulnerability

Subcellular compartments implicated in LEPID include mitochondria, cytosol, and nucleus. KARS1’s bifunctional isoforms localize to both cytosolic and mitochondrial compartments, with mitochondrial KARS1 being essential for mitochondrial translation. The mitochondrial matrix houses the translational machinery for mtDNA-encoded proteins, and KARS1 acts within this compartment to charge mitochondrial tRNA^Lys.[12][14] GO cellular component terms “mitochondrion” (GO:0005739), “mitochondrial matrix” (GO:0005759), and “cytosol” (GO:0005829) are relevant. Dysfunction in these compartments leads to downstream consequences in organelles like the inner mitochondrial membrane, where oxidative phosphorylation complexes reside, and the plasma membrane, where energy-dependent ion channels and transporters maintain neuronal excitability and cochlear hair cell function.[7][14]

Calcifications in CNS tissues imply altered subcellular ion handling, possibly involving deposition of calcium salts in extracellular matrix or within cells. Microglial and astrocytic compartments may participate in this process through inflammatory signaling and phagocytosis of debris. While specific subcellular localization of calcifications in LEPID has not been studied, analogous conditions suggest involvement of lysosomes and extracellular spaces in mineral deposition.[8][9][11] GO terms such as “calcium ion binding” (GO:0005509) and “extracellular matrix” (GO:0031012) may be relevant.

Compartmental vulnerability in LEPID reflects the reliance of certain organelles on mitochondrial ATP production. Synaptic terminals in neurons and hair cells, which maintain transmembrane ion gradients and neurotransmitter cycling, are especially sensitive to ATP deficits. Disturbances in these compartments lead to synaptic dysfunction, excitotoxicity, and cell death, manifesting as seizures and hearing loss.[7][11][14] Integration of subcellular compartment annotations in knowledge bases can help link KARS1 dysfunction to specific cellular processes and phenotypes.

### 6.3 Age of Onset, Disease Course, and Critical Periods

LEPID is characterized by infantile or early childhood onset, with symptoms typically emerging in the first months to few years of life. OMIM describes LEPID as having onset of symptoms in infancy or early childhood, and Orphanet refers to “early-onset progressive leukoencephalopathy” in its ORPHA:3240 description.[9][11] Itoh et al.’s series included children aged 2 to 12 years at evaluation, with many showing congenital or very early deafness, hypotonia, and developmental delay from infancy.[11] McMillan et al.’s siblings presented with severe infantile visual loss and microcephaly, indicating onset within the first year of life.[12] Thus, the typical age of onset is pediatric, often within the first two years, with congenital manifestations such as deafness and microcephaly frequently present.[1][2][9][11][12][14]

The onset pattern is chronic and insidious rather than acute, with developmental delay and hypotonia gradually becoming apparent. However, episodic regression events can occur, often precipitated by infections or fever, giving a relapsing‑progressive course. Malacards notes “Neurologic regression associated with infection or fever,” and OMIM emphasizes episodic regression with progressive motor deterioration.[1][11] Over time, the disease follows a relentlessly progressive trajectory, with gradual accumulation of deficits and worsening disability. There is no evidence for spontaneous remission, and while some periods of relative stability may occur, the overall trend is downward.[1][2][9][11][14]

Critical periods in LEPID likely correspond to stages of brain myelination and sensory system development. Early childhood is a window of rapid myelination and synaptic refinement; mitochondrial dysfunction during this period can have disproportionate impacts on white matter integrity and cognitive development. Similarly, cochlear hair cell and retinal development in infancy are critical for sensory function. Disruption of KARS1 function during these windows may result in irreversible deficits. From an intervention standpoint, early diagnosis, supportive care, and avoidance of metabolic stressors may provide opportunities to mitigate acute regression events, though current therapies cannot halt progression.[1][2][11][14]

Disease duration spans the remaining lifespan of affected individuals. Many LEPID patients die in childhood; OMIM notes that “Early death often occurs,” and Itoh et al. report that five of seven children died between 2 and 12 years of age.[1][11] Those who survive into adolescence or adulthood experience severe disability and require lifelong care. In DEAPLE, neurologic manifestations may begin in adulthood, extending the timeline and shifting critical periods to later life.[13][14] HPO terms for age of onset such as “infantile onset” (HP:0003593) and “childhood onset” (HP:0003674) should be associated with LEPID.

## 7. Diagnostics, Differential Diagnosis, and Screening



## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 65 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 41 |
| Terms named correctly | 28 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0008213` (1 mention) - the report calls it "neuron death"; GO calls it **protein alkylation**
- `UBERON:0002436` (2 mentions) - the report calls it "white matter of brain"; UBERON calls it **primary visual cortex**
- `UBERON:0001755` (2 mentions) - the report calls it "cochlea"; UBERON calls it **distal part of styloid process of temporal bone**
- `UBERON:0000943` (1 mention) - the report calls it "cranial nerve VIII"; UBERON calls it **obsolete labial sensillum**
- `CL:0000203` (1 mention) - the report calls it "inner hair cell of cochlea"; CL calls it **gravity sensitive cell**
- `UBERON:0001476` (1 mention) - the report calls it "retina"; UBERON calls it **deltoid**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070469` (obsolete respirasome) (1 mention) - replaced by `GO:0098803`
- `UBERON:0000943` (obsolete labial sensillum) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004827` (1 mention) - the report calls it "lysine-tRNA ligase activity"; GO calls it **proline-tRNA ligase activity**
- `GO:0002181` (1 mention) - the report calls it "cytosolic translation"; GO calls it **cytoplasmic translation**
- `GO:0070469` (1 mention) - the report calls it "respiratory chain"; GO calls it **obsolete respirasome**, and lists "respiratory chain" among its other names
- `UBERON:0000941` (2 mentions) - the report calls it "optic nerve"; UBERON calls it **cranial nerve II**, and lists "optic nerve" among its other names
- `UBERON:0000956` (1 mention) - the report calls it "cerebrum"; UBERON calls it **cerebral cortex**, and lists "cortex cerebri" among its other names
- `CL:0000746` (1 mention) - the report calls it "cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `HP:0003674` (1 mention) - the report calls it "childhood onset"; HP calls it **Onset**, and lists "Age of onset" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.