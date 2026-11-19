---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-30T11:19:15.397817'
end_time: '2026-10-30T11:23:31.011904'
duration_seconds: 255.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: AFG3L2-related Optic Atrophy And/Or Spastic Ataxia Spectrum
  mondo_id: MONDO:0700372
  category: Mendelian
  causal_genes: AFG3L2
  omim_id: not recorded
  synonyms: not recorded
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
  total_references: 20
  verified: 19
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.05
  relevance_assessed: 19
  on_topic: 14
  unresolved_references:
  - DOI:10.1093/brain/awad340/7296494
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 80
  verified: 71
  not_found: 0
  obsolete: 0
  unverifiable: 9
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0700372
    reported_labels:
    - MONDO
    ontology_label: AFG3L2-related optic atrophy and/or spastic ataxia spectrum
  labels_variant: 3
  unresolvable_prefixes:
  - Gene
  - ORPHA
  - Taxon
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AFG3L2-related Optic Atrophy And/Or Spastic Ataxia Spectrum
- **MONDO ID:** MONDO:0700372 (if available)
- **Causal gene(s):** AFG3L2
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

Please provide a comprehensive research report on **AFG3L2-related Optic Atrophy And/Or Spastic Ataxia Spectrum** covering all of the
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

# Comprehensive disease-characteristics report  
## AFG3L2-related optic atrophy and/or spastic ataxia spectrum

**AFG3L2-related optic atrophy and/or spastic ataxia spectrum is caused by germline pathogenic variants in the nuclear gene *AFG3L2* (HGNC:315; NCBI Gene:10939), encoding a mitochondrial inner-membrane m-AAA ATP-dependent metalloprotease.** The ClinGen disease entity **MONDO:0700372** deliberately combines *AFG3L2*-related optic atrophy 12 and autosomal-recessive spastic ataxia 5 because monoallelic and biallelic loss-of-function/hypomorphic alleles produce a continuous mitochondrial-neurodegenerative spectrum. ClinGen classified the relationship as **Definitive** with **semidominant inheritance** on May 16, 2024. Importantly, classic spinocerebellar ataxia type 28 (SCA28), usually associated with protease-domain dominant-negative variants and generally lacking optic atrophy, was split from this particular MONDO entity. [18][21]

**Scope note.** Evidence is exceptionally sparse: most phenotype assertions derive from case reports or small families rather than population cohorts. Frequencies below therefore describe reported patients, not reliable population-level probabilities.

---

## 1. Disease information

### 1.1 Definition and identifiers

| Field | Information |
|---|---|
| Preferred disease | *AFG3L2*-related optic atrophy and/or spastic ataxia spectrum |
| MONDO | **MONDO:0700372** |
| Causal gene | ***AFG3L2***, HGNC:315; NCBI Gene:10939; OMIM gene **604581**; UniProt **Q9Y4W6** |
| Chromosomal locus | **18p11.21** |
| Included OMIM phenotypes | **Optic atrophy 12 (OPA12), OMIM 618977**; **spastic ataxia 5, autosomal recessive (SPAX5), OMIM 614487** |
| Excluded from this precise ClinGen/MONDO lump | **Spinocerebellar ataxia 28, OMIM 610246**, because its variant distribution and dominant-negative mechanism appear distinct |
| ClinGen validity | **Definitive**, approved May 16, 2024 |
| ClinGen inheritance | **Semidominant**, HP:0032113 |
| MedGen concepts | OPA12: C5436534; SPAX5: C3280977 |
| Disease Ontology | OPA12: DOID:0080840; SPAX5: DOID:0050944 |
| Orphanet | The SPAX5 component is represented as autosomal-recessive spastic ataxia type 5, **ORPHA:313772** |
| SNOMED CT | SPAX5/AFG3L2-related spastic ataxia–myoclonic epilepsy–neuropathy syndrome: **771469002** |
| ICD-10/ICD-11 | No uniquely specific code was identified; coding generally uses broader optic-atrophy, hereditary-ataxia, spastic-paraplegia, epilepsy, or neuropathy categories |
| MeSH | No disease-specific MeSH heading identified; broader headings include *Optic Atrophy*, *Spinocerebellar Ataxias*, *Spastic Paraplegia, Hereditary*, and *Mitochondrial Diseases* |

ClinGen includes OPA12 and SPAX5 because their phenotypic variability appears to represent “a spectrum of disease rather than separate disease entities,” with loss of *AFG3L2* function and mitochondrial-network dysfunction shared across both. [39] The gene is located at 18p11.21 and encodes the mitochondrial inner-membrane m-AAA protease component AFG3L2. [91][92]

### 1.2 Synonyms

- *AFG3L2*-related optic atrophy with or without extraocular features  
- *AFG3L2*-related optic atrophy and/or ataxia  
- Optic atrophy type 12; OPA12  
- Autosomal-recessive spastic ataxia type 5; SPAX5  
- Early-onset spastic ataxia–myoclonic epilepsy–neuropathy syndrome  
- *AFG3L2*-related spastic ataxia, myoclonic epilepsy and neuropathy syndrome  
- *AFG3L2* autosomal-recessive spastic ataxia [106][110]

### 1.3 Nature of the evidence

The evidence is primarily:

1. **Individual-patient/family clinical data** from ophthalmology, neurology, WES and panel studies.
2. **Aggregated disease-level curation** from ClinGen, MONDO, OMIM, MedGen and GeneReviews.
3. **Functional evidence** from patient fibroblasts, yeast complementation, cultured cells, induced pluripotent stem cells and mice.
4. **No substantial EHR-derived epidemiologic cohort** or population-based registry analysis was found.

ClinGen scored 13 suspected causal variants—three nonsense and ten missense—in 11 probands from three core publications, with six monoallelic and five biallelic probands. [18]

---

## 2. Etiology, risk and protective factors

### 2.1 Primary cause

The cause is **germline monoallelic or biallelic *AFG3L2* dysfunction**:

- **Monoallelic loss-of-function/hypomorphic variants**, particularly in or around the ATPase/AAA domain, can cause dominant optic atrophy, sometimes with hearing loss, dystonia, spasticity or neurodevelopmental abnormalities.
- **Biallelic null, hypomorphic or missense/null combinations** generally cause earlier and more severe spastic-ataxia, neuropathy, epilepsy or developmental-neurodegenerative disease.
- ClinGen interprets this dosage relationship as **semidominant**: one defective allele may cause optic atrophy or a subclinical phenotype, while two damaging alleles usually produce more severe multisystem neurologic disease. [18][39]

All established pathogenic variants are presumed **germline**. No somatic disease mechanism is established.

### 2.2 Genetic risk factors

| Risk factor | Evidence/interpretation |
|---|---|
| Pathogenic monoallelic *AFG3L2* allele | Risk of OPA12; penetrance may be reduced or subclinical |
| Biallelic pathogenic alleles | High risk of SPAX5 or a severe developmental-neurodegenerative phenotype |
| Null/null genotype | Likely greater severity than missense/missense or null/hypomorphic combinations, although numbers are too small for precise prediction |
| ATPase-domain variants | Enriched in OPA12 and associated with altered OPA1 processing and mitochondrial fragmentation |
| Proteolytic-domain biallelic variants | Associated with SPAX5 and related recessive ataxia |
| Family history/consanguinity | Raises prior probability for dominant or recessive disease, respectively |
| De novo variation | Documented in OPA12; two of 12 families in one series carried de novo variants |

Reduced penetrance and subclinical disease occur in OPA12. Some heterozygous relatives of recessive cases have isolated optic atrophy or cerebellar atrophy rather than being completely unaffected. [18]

### 2.3 Environmental, lifestyle and infectious factors

No toxin, infection, radiation, occupation, diet, smoking behavior or other environmental exposure is known to **cause** this Mendelian disorder. No disease-specific gene–environment interaction has been demonstrated.

Potential **symptom modifiers**, not causes, include:

- Alcohol and sedating drugs may worsen coordination and gait ataxia.
- Benzodiazepines may worsen coordination when used as sedatives, although clonazepam can be medically useful for myoclonus.
- Carbamazepine and phenytoin may exacerbate myoclonus in SPAX5.
- Obesity and inactivity can compound mobility impairment.
- Visual impairment can be functionally worsened by glare, insufficient contrast and inaccessible environments. [151]

### 2.4 Protective factors

No validated genetic protective allele, diet, supplement or prophylactic medication is known. Practical protective measures are secondary/tertiary:

- activity and individualized physiotherapy;
- fall prevention;
- avoidance of excessive alcohol and unnecessary sedatives;
- early seizure control;
- low-vision support;
- nutritional and aspiration surveillance.

In models, activation of the OMA1–DELE1–HRI integrated stress response appears protective, but this has not yet become a proven human therapy. [61]

---

## 3. Phenotypes

### 3.1 Principal phenotype matrix

Frequencies are generally unavailable for the exact MONDO spectrum; “common,” “occasional” and “variable” reflect published case series.

| Phenotype and type | Onset, course and frequency | Functional/QOL effect | Suggested HPO |
|---|---|---|---|
| Bilateral optic atrophy; clinical sign | Usually childhood/first two decades, but adult onset occurs; slowly progressive or sometimes relatively stable; core OPA12 feature and present in some biallelic cases | Reading, education, driving, face recognition and independent navigation may be impaired | Optic atrophy HP:0000648; bilateral optic atrophy HP:0012502 |
| Reduced visual acuity; sign | Variable, often approximately 0.2/10–2/10; can progress to counting-fingers vision or blindness | Major low-vision disability | Reduced visual acuity HP:0007663; visual impairment HP:0000505; blindness HP:0000618 |
| Optic-disc pallor; sign | Characteristically temporal or diffuse, bilateral | Objective marker of retinal-ganglion-cell/optic-nerve injury | Optic disc pallor HP:0000543; temporal optic-disc pallor HP:0012511 |
| RNFL thinning on OCT; imaging sign | Often severe and diffuse; persistent/progressive | Correlates with optic-nerve axon loss | Abnormal retinal nerve-fiber-layer morphology HP:0020119 |
| Color-vision defect; symptom/sign | Common in OPA12; variable pattern and severity | Difficulty with color-coded information and school/work tasks | Color vision defect HP:0000551 |
| Photophobia; symptom | Reported in OPA12, variable | Outdoor and screen intolerance | Photophobia HP:0000613 |
| Cerebellar/gait ataxia; sign | Infancy/childhood in SPAX5; occasionally later; usually progressive | Falls, impaired feeding/writing, loss of independent ambulation in severe cases | Ataxia HP:0001251; gait ataxia HP:0002066; progressive gait ataxia HP:0007240 |
| Limb dysmetria/dysdiadochokinesis; sign | Variable, usually progressive with cerebellar syndrome | Impaired fine-motor and self-care tasks | Dysmetria HP:0001310; dysdiadochokinesis HP:0002075 |
| Spasticity/spastic gait or paraparesis; sign | Usually childhood in SPAX5; severity ranges from mild hyperreflexia to tetraplegia | Contractures, pain, impaired transfers and ambulation | Spasticity HP:0001257; spastic gait HP:0002064; progressive spastic paraparesis HP:0007199 |
| Dysarthria; sign | Frequent in the spastic-ataxia phenotype; progressive | Reduced intelligibility and communication | Dysarthria HP:0001260 |
| Myoclonus and myoclonic epilepsy; symptom/sign | Particularly SPAX5; childhood onset, occasionally medically refractory | Injury risk, reduced independence and developmental disruption | Myoclonus HP:0001336; generalized myoclonic seizure HP:0002123 |
| Peripheral sensorimotor neuropathy; sign/electrophysiologic abnormality | Variable; may include distal weakness and amyotrophy | Foot drop, falls, impaired hand/leg function | Sensorimotor neuropathy HP:0007141; distal lower-limb weakness HP:0009053 |
| Dystonia/chorea/hyperkinetic movement | Occasional | Pain, abnormal postures and mobility/feeding impairment | Dystonia HP:0001332; chorea HP:0002072; hyperkinetic movements HP:0002487 |
| Ptosis, ophthalmoparesis or oculomotor apraxia | Variable, mainly complex biallelic disease | Restricted gaze, visual-field obstruction and worsened balance | Ptosis HP:0000508; ophthalmoparesis HP:0000597; oculomotor apraxia HP:0000657 |
| Sensorineural hearing loss | Occasional in optic-atrophy families; may be progressive | Communication and educational impact | Sensorineural hearing impairment HP:0000407 |
| Developmental delay/regression and intellectual disability | Mainly severe biallelic disease; regression can begin around nine months | Lifelong dependence and educational limitations | Global developmental delay HP:0001263; developmental regression HP:0002376; intellectual disability HP:0001249 |
| Microcephaly/poor weight gain | Severe infantile biallelic disease | Marker of severe neurodevelopmental/systemic involvement | Microcephaly HP:0000252; poor weight gain HP:0001508 |
| Cerebellar/cerebral atrophy | Common imaging correlate in severe biallelic disease; MRI can be normal in isolated OPA12 | Predicts broad motor/developmental impairment | Cerebellar atrophy HP:0001272; cerebral atrophy HP:0002059 |
| Raised blood lactate | Reported in some SPAX5 cases, not universal or diagnostic | Indicates mitochondrial metabolic stress | Increased blood lactate HP:0002151 |

OPA12 usually begins before age 20 and comprises reduced acuity, impaired color vision, optic-nerve pallor and markedly reduced RNFL thickness; brain MRI is often normal. [6] In a 2023 father–daughter report, both developed visual loss in the first decade without neurologic deficits. The daughter had acuity of 20/125−1 bilaterally and RNFL thicknesses of 52 and 48 μm; her father progressed to counting-fingers vision with RNFL thickness 45 μm in the measurable eye. [19]

SPAX5 has been reported in only approximately 14 individuals in the latest aggregated clinical description. Presentations range from infantile microcephaly, poor growth, severe developmental delay and regression around nine months—with death reported as early as 2.5 years—to milder childhood cerebellar ataxia and myoclonic epilepsy. [14][69]

### 3.2 Recent illustrative cases

- **Brodsky et al., 2023; PMID:36974169; published March 8, 2023:** father and daughter with childhood-onset nonsyndromic optic atrophy due to c.1064C>T, p.Thr355Met. Abstract quote: **“No additional neurologic or neuroimaging abnormalities were detected.”** [167]
- **Jin et al., 2023; PMID:37025825; published March 24, 2023:** severe biallelic disease with c.1834G>T, p.Glu612Ter and c.2176-6T>A. Abstract quote: **“early-onset and intractable epilepsy, developmental regression, microcephaly, and premature death.”** MRI showed global atrophy involving cerebrum, cerebellum, corpus callosum, brainstem, vermis and basal ganglia. [166]
- **Colucci et al., 2023; PMID:36447112; issue publication December 2023:** two patients carrying the same biallelic p.Met625Ile genotype nevertheless had different ataxia-plus courses, illustrating marked intragenotypic variability. [171][175]

No disease-specific EQ-5D, SF-36, PROMIS or validated quality-of-life dataset was identified.

---

## 4. Genetic and molecular information

### 4.1 Gene/protein

| Attribute | Value |
|---|---|
| Symbol | *AFG3L2* |
| Full name | AFG3-like matrix AAA peptidase subunit 2 |
| HGNC | HGNC:315 |
| NCBI Gene | 10939 |
| OMIM gene | 604581 |
| UniProt | Q9Y4W6 |
| Location | 18p11.21 |
| Canonical protein | Mitochondrial inner-membrane m-AAA protease component AFG3L2 |
| Principal functions | ATP binding/hydrolysis, ATP-dependent proteolysis, metallopeptidase activity, unfolded-protein recognition, mitochondrial protein quality control |
| Complex | AFG3L2 homohexamers or heterohexamers with SPG7/paraplegin |

AFG3L2 complexes are anchored in the mitochondrial inner membrane with ATPase and protease portions facing the matrix; substrates enter a central ATPase channel, are unfolded and translocated to the proteolytic pore. [93]

Suggested GO annotations:

- mitochondrial inner membrane — **GO:0005743**
- mitochondrial matrix — **GO:0005759**
- ATP binding — **GO:0005524**
- ATP hydrolysis activity — **GO:0016887**
- metalloendopeptidase activity — **GO:0004222**
- proteolysis — **GO:0006508**
- mitochondrial protein-containing complex — **GO:0098798**
- mitochondrial organization — **GO:0007005**
- mitochondrial fusion — **GO:0008053**
- cellular response to mitochondrial stress — **GO:0034514**

### 4.2 Representative pathogenic or likely pathogenic variants

This is representative rather than a complete ClinVar catalogue.

| Variant, transcript NM_006796.3 | Type/zygosity reported | Phenotype/mechanistic evidence |
|---|---|---|
| c.1064C>T, p.Thr355Met | Heterozygous missense | Dominant childhood optic atrophy; classified pathogenic in the 2023 family report; absent from gnomAD v2.1.1 in a 2021 panel review |
| c.1220A>G, p.Asp407Gly | Heterozygous missense | Optic atrophy; defective yeast complementation and substrate processing |
| c.1385C>T, p.Ala462Val | Heterozygous or part of compound heterozygous genotype | Recurrent OPA12 allele; functional loss of activity |
| c.1394G>A, p.Arg465Lys | Heterozygous missense, de novo in one proband | Childhood optic atrophy and intellectual disability; functional loss of activity |
| c.1541C>T, p.Pro514Leu | Heterozygous missense | Severe optic atrophy with complex neurologic findings; functional loss of activity |
| c.1858C>A, p.Gln620Lys | Compound heterozygous missense | Hypomorphic; optic atrophy plus spastic ataxia/chorea/myoclonus |
| c.1847A>G, p.Tyr616Cys; rs387906889 | Homozygous missense | Foundational SPAX5 variant; hypomorphic protease activity; ClinVar pathogenic |
| c.383G>A, p.Trp128Ter plus c.2083A>G, p.Arg695Gly | Compound heterozygous nonsense/missense | Spastic ataxia with dysarthria and pallidal MRI abnormality |
| c.1901_1902del, p.Ser634Ter plus c.916A>G, p.Lys306Glu | Compound heterozygous truncating/missense | Syndromic optic neuropathy, ataxia, dystonia and basal-ganglia abnormalities |
| c.1834G>T, p.Glu612Ter plus c.2176-6T>A | Compound heterozygous nonsense/splice-region | Severe developmental regression, epilepsy, microcephaly and global cerebral atrophy |
| c.1A>G, p.Met1Val plus c.1894C>T, p.Arg632Ter | Compound heterozygous start-loss/nonsense | Recessive ataxia; patient-iPSC work showed reduced protein stability, mitochondrial dysfunction and MCU-mediated calcium overload |
| c.245dup, p.Asn82LysfsTer6 plus p.Met625Ile | Compound heterozygous frameshift/missense | SPAX5; reduced AFG3L2 expression and mitochondrial membrane potential |

ClinGen found both monoallelic and biallelic null/hypomorphic mechanisms, but noted that some alleles causing disease in trans did not produce overt disease in heterozygous relatives. [18] ClinVar classifications can change and should be checked by accession and laboratory date before clinical use; a VUS alone neither establishes nor excludes the diagnosis.

### 4.3 Population frequency and origin

Disease-causing alleles are individually very rare, and several well-supported optic-atrophy variants were absent from older gnomAD releases. [136] Exact contemporary gnomAD v4 frequencies were not consistently available from the primary reports, so no zero frequency should be assumed without direct current database verification. All reported causal alleles are **germline**.

### 4.4 Modifier, epigenetic and structural-genomic findings

- ***SPG7*** is the strongest biological interactor: paraplegin and AFG3L2 form hetero-oligomeric m-AAA complexes. Digenic or modifying effects are biologically plausible, but no clinically validated modifier model exists.
- OPA1, OMA1, DELE1, HRI/EIF2AK1, MCU, EMRE/SMDT1 and MICU proteins are mechanistic pathway components, not established inherited modifier loci.
- No reproducible disease-specific DNA-methylation signature, histone modification or chromatin abnormality is known.
- No recurrent pathogenic aneuploidy, translocation, inversion or copy-number syndrome defines this disease. Sequence variants account for **>99%** of currently recognized pathogenic alleles; deletion/duplication variants account for **<1%**. [6]

---

## 5. Environmental information

This is a **primary genetic mitochondrial disease**, not an environmentally caused, infectious or zoonotic disorder.

| Category | Current evidence |
|---|---|
| Environmental toxicants | None established as etiologic |
| Radiation/pollution/occupation | No association demonstrated |
| Smoking/diet/alcohol | Not causal; alcohol may worsen ataxia |
| Exercise | Does not cure or demonstrably halt neurodegeneration, but helps preserve conditioning, mobility and function |
| Infection | No bacterial, viral, fungal or parasitic trigger identified |
| Immune trigger | No autoimmune etiology established |
| Gene–environment interaction | No validated interaction; sedatives, alcohol, obesity and inaccessible environments can magnify disability |

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **A germline monoallelic or biallelic pathogenic *AFG3L2* variant leads to reduced, hypomorphic or abnormally assembled AFG3L2 m-AAA protease.**
2. **Deficient ATP-dependent unfolding/proteolysis leads to impaired mitochondrial inner-membrane proteostasis and abnormal accumulation or processing of mitochondrial proteins.**
3. **Proteostatic failure leads to respiratory-chain impairment, reduced membrane potential and ATP generation, and—in some models—increased reactive oxygen species.**
4. **AFG3L2 dysfunction leads to inappropriate OMA1 activation and excess conversion of long OPA1 isoforms to short fission-promoting isoforms.**
5. **Abnormal OPA1 processing results in mitochondrial-network fragmentation and abnormal mitochondrial distribution in neuronal axons and dendrites.**
6. **In a parallel branch, failure to degrade unassembled EMRE/SMDT1 leads to inadequately gated MCU–EMRE channels and mitochondrial Ca²⁺ overload.**
7. **Fragmentation, respiratory failure and Ca²⁺ overload lead to permeability-transition susceptibility, impaired axonal transport, oxidative stress and neuronal dysfunction/death.**
8. **In retinal ganglion cells and optic-nerve axons, these abnormalities lead to RNFL loss, optic-disc pallor, dyschromatopsia and progressive central visual impairment.**
9. **In Purkinje cells, corticospinal motor neurons and peripheral axons, they lead to cerebellar ataxia, dysarthria, spasticity and neuropathy.**
10. **In severe biallelic disease, widespread mitochondrial failure leads to developmental regression, epilepsy, microcephaly and cerebral/cerebellar atrophy.**
11. **A compensatory branch activates OMA1–DELE1–HRI signaling, which leads to an integrated stress response that is protective in fibroblast and mouse experiments; benefit in human patients remains inferred, not demonstrated.**

### 6.2 Evidence and pathway detail

AFG3L2 is an ATP-dependent metalloprotease of the inner mitochondrial membrane and physically associates with SPG7/paraplegin. Loss of activity perturbs both degradation of damaged/unassembled proteins and maturation of selected substrates. [18][93]

In OPA12 patient fibroblasts, ATPase-domain variants caused excess short OPA1 isoforms and fragmented mitochondrial networks. The primary paper concluded that **“unbalanced processing of OPA1 consequent to AFG3L2 dysfunction possibly leads to the optic atrophy phenotype.”** PMID:32219868, published April 2, 2020. [46][52]

The Ca²⁺ branch reflects failure to clear unassembled EMRE/SMDT1, producing deregulated MCU channels, excessive mitochondrial Ca²⁺ uptake and susceptibility to calcium-induced neuronal death. A 2024 study of c.[1A>G];[1894C>T] patient-derived iPSCs found impaired mitochondrial function, reduced AFG3L2 stability and MCU-complex-mediated Ca²⁺ overload. PMID:39428429; epub October 11, 2024. [78]

The most important 2023–2024 experimental development was the OMA1 stress-response study:

> “Mitochondrial proteotoxicity in the absence/mutation of AFG3L2 activates the OMA1-DELE1-HRI pathway eliciting the integrated stress response.”

The pathway was activated in SPAX5 fibroblasts and *Afg3l2*-null mouse cerebellum; Sephin-1 improved fibroblast growth, Purkinje-cell survival/arborization and mouse survival, indicating that the response was protective rather than simply injurious. PMID:37804316; online October 7, 2023; *Brain* 2024;147:1043–1056. [61][67]

### 6.3 Cell types, processes and ontology suggestions

| Component | Suggested ontology |
|---|---|
| Retinal ganglion cell | CL:0000740 |
| Cerebellar Purkinje neuron | CL:0000121 |
| Astrocyte/Bergmann glia | CL:0000127; Bergmann glial cell where available |
| Upper motor neuron/corticospinal neuron | CL:0000117 or more specific corticospinal-neuron term |
| Peripheral motor/sensory neuron | CL nervous-system neuron terms |
| Mitochondrial inner membrane | GO:0005743 |
| Mitochondrial matrix | GO:0005759 |
| Protein proteolysis | GO:0006508 |
| Mitochondrial organization | GO:0007005 |
| Mitochondrial fusion | GO:0008053 |
| Calcium-ion homeostasis | GO:0055074 |
| Cellular respiration | GO:0045333 |
| ATP metabolic process | GO:0046034 |
| Neuron apoptotic process | GO:0051402 |
| Integrated stress response | GO cellular-response-to-stress hierarchy |

Astrocyte-specific *Afg3l2* deletion also causes Bergmann-glia degeneration, altered EAAT2 expression and secondary Purkinje-cell abnormalities, demonstrating a non-cell-autonomous glial contribution in mice. [127]

### 6.4 Molecular profiling and advanced technologies

- **Transcriptomics/proteomics/metabolomics:** no validated patient diagnostic signature existed through 2024. Later multi-omics work in mutant lymphoblasts supports mitochondrial, metabolic and proteostatic disruption, but is not yet a clinical biomarker. [9]
- **Patient iPSCs:** the 2024 p.Met1Val/p.Arg632Ter study showed reduced protein stability, mitochondrial dysfunction and calcium overload. [78]
- **Single-cell/spatial transcriptomics:** no disease-defining human dataset identified.
- **CRISPR/RNAi screens:** no clinically validated disease-specific screen identified.
- **Epigenomics/lipidomics:** no reproducible patient signature identified.
- **Immune involvement:** reactive astrogliosis occurs in models, but primary autoimmunity is not implicated.

---

## 7. Anatomical structures affected

| Level | Primary/secondary involvement | Suggested ontology |
|---|---|---|
| Organ/system | Central and peripheral nervous systems; visual system | Nervous system UBERON:0001016 |
| Eye/optic pathway | Bilateral retina—especially ganglion-cell/RNFL compartment—optic discs, optic nerves and occasionally chiasm/tract | Retina UBERON:0000966; optic nerve UBERON:0000958 |
| Cerebellum | Purkinje-cell layer, cerebellar cortex and superior vermis; cerebellar atrophy in severe disease | Cerebellum UBERON:0002037 |
| Cerebrum | Global cerebral and callosal atrophy in severe biallelic disease | Brain UBERON:0000955 |
| Basal ganglia | Globus pallidus, putamen, caudate and substantia-nigra MRI abnormalities in selected cases | Relevant UBERON regional terms |
| Corticospinal system | Long descending motor axons underlying pyramidal signs/spasticity | Spinal cord UBERON:0002240 |
| Peripheral nerves | Sensorimotor axons, sometimes with reduced large-caliber fibers and onion-bulb formation | Peripheral nerve UBERON:0001021 |
| Skeletal muscle | Secondary denervation weakness; abnormal mitochondrial distribution/lipid droplets described in biopsy | Skeletal muscle tissue UBERON:0001134 |
| Subcellular | Mitochondrial inner membrane, matrix-facing m-AAA complex, cristae/network | GO:0005743, GO:0005759 |

Optic atrophy is normally bilateral. Ataxia and spasticity are generally bilateral, though severity can be asymmetric.

---

## 8. Temporal development

### 8.1 Onset and course

| Clinical form | Typical onset | Course |
|---|---|---|
| Predominantly OPA12 | Usually first decade or before age 20; adult onset possible | Insidious, chronic, stable to slowly progressive |
| SPAX5, severe | Infancy; developmental regression may begin around nine months | Progressive neurodegeneration; seizures and diffuse atrophy; early death possible |
| SPAX5, milder | Infancy or childhood | Chronic progressive ataxia/spasticity with variable epilepsy, movement disorder and neuropathy |
| Biallelic late-onset ataxia | Rarely adulthood | Slowly progressive |

No formal staging system exists. A useful clinical staging framework is:

1. **Presymptomatic/subclinical:** familial pathogenic variant with normal or subtly abnormal OCT/MRI.
2. **Early:** reduced acuity/color vision or gait imbalance/hyperreflexia.
3. **Intermediate:** marked RNFL loss, gait ataxia, spasticity, dysarthria or seizures.
4. **Advanced:** severe low vision/blindness, loss of independent ambulation, dysphagia, severe epilepsy or developmental dependence.

The disease is lifelong; spontaneous remission is not documented. Visual and neurologic rehabilitation can improve function but does not reverse neuronal loss.

### 8.2 Critical periods

The severe biallelic phenotype suggests prenatal/early-postnatal nervous-system vulnerability. This supports—in principle—treatment before substantial optic-nerve, Purkinje-cell or corticospinal axon loss, but no human therapeutic window has been established.

---

## 9. Inheritance and population characteristics

### 9.1 Inheritance

The best current label for MONDO:0700372 is **semidominant**:

- One pathogenic allele can cause dominant optic atrophy.
- Two damaging alleles usually cause more severe recessive spastic-ataxia/neurodevelopmental disease.
- Some heterozygous carriers of recessive-family alleles are asymptomatic, while others show subtle optic or cerebellar findings.

For a clearly dominant allele, each child has a **50%** chance of inheriting it. When both parents carry pathogenic alleles, each pregnancy has a nominal **25% biallelic affected, 50% heterozygous and 25% neither-allele** distribution; however, heterozygotes may not be clinically neutral under the semidominant model. [6]

OPA12 penetrance is incomplete or age-dependent/subclinical. Genetic anticipation is not established. Parental germline mosaicism is possible for apparently de novo variants; when a variant is absent from parental leukocyte DNA, an approximate 1% sibling recurrence risk is commonly used. No established founder variant or reliable carrier-frequency estimate exists.

### 9.2 Epidemiology

- No robust population prevalence or incidence exists for MONDO:0700372.
- In a cohort of 2,186 probands with suspected hereditary optic neuropathy, 451 received a dominant or recessive molecular diagnosis; *AFG3L2* accounted for **14/451, approximately 3%**, placing it among the ten most frequent nuclear genes in that diagnosed subset. This is not general-population prevalence. [19]
- OPA12 has been estimated at roughly **4%–5% of autosomal-dominant optic atrophy** or approximately 4% of *OPA1*-negative optic atrophy. [6]
- SPAX5 remained limited to approximately **14 published individuals** in the latest aggregated review, underscoring extreme rarity and ascertainment instability. [148]
- No reproducible sex bias, ethnic enrichment or geographic concentration has been established.
- Cases have been reported across European, East African, East Asian, Middle Eastern and Hispanic/Latino families.

---

## 10. Diagnostics

### 10.1 Clinical evaluation

No consensus clinical diagnostic criteria exist. Diagnosis requires compatible findings plus pathogenic/likely pathogenic *AFG3L2* variant(s). [6]

Recommended baseline evaluation:

| Domain | Tests/findings |
|---|---|
| Ophthalmology | Best-corrected acuity, color testing, pupils, fundus photography, OCT RNFL/ganglion-cell layer, visual fields, visual-evoked potentials where useful |
| Neurology | Gait/limb coordination, tone, reflexes, plantar responses, dystonia/chorea/myoclonus, eye movements, cranial nerves |
| Ataxia severity | SARA or another standardized scale |
| Imaging | Brain MRI, including optic pathways, cerebellum, basal ganglia and cerebral volume; spine MRI if needed to exclude alternatives |
| Epilepsy | EEG in suspected SPAX5 or episodic myoclonus |
| Neuropathy | Nerve-conduction studies/EMG |
| Hearing | Audiometry, especially in syndromic optic atrophy |
| Development/cognition | Formal developmental, neuropsychological and school assessment |
| Swallowing/nutrition | Speech-language/feeding evaluation; video swallow when aspiration is suspected |
| Laboratory | Lactate, metabolic studies and CK can support a mitochondrial differential but are neither sensitive nor specific |
| Biopsy | Generally unnecessary; historical muscle/nerve biopsies may show mitochondrial mislocalization, lipid droplets, axonal loss or onion bulbs |

### 10.2 Genetic-testing strategy

1. **Preferred first line:** phenotype-appropriate multigene panel covering hereditary optic neuropathy, spastic ataxia, hereditary spastic paraplegia and mitochondrial-neurologic genes, including full *AFG3L2* sequencing and copy-number analysis.
2. **WES:** highly useful; most known alleles are coding missense, nonsense, frameshift or splice variants.
3. **WGS:** useful after negative panel/WES for noncoding, structural or poorly covered variants and for uniform coverage.
4. **Reanalysis:** strongly recommended for previously negative exome/genome data. The 2023 p.Thr355Met family was diagnosed only after reinterpretation of an initially negative exome. [167]
5. **Single-gene sequencing:** possible when phenotype and family variant are clear, but usually not preferred because the phenotype is not gene-specific.
6. **CMA/karyotype/FISH:** low yield for this sequence-level condition; use when broader developmental or chromosomal disease is suspected.
7. **mtDNA testing:** does not test *AFG3L2* because it is nuclear, but may be appropriate in the mitochondrial differential.
8. **Repeat-expansion testing:** not an *AFG3L2* assay; may still be needed for alternative inherited ataxias.
9. **RNA studies:** useful for splice-region or deep-intronic VUS, but not routine.
10. **Familial testing:** segregation and phase determination are critical, especially in compound-heterozygous cases.

Sequence analysis detects **>99%** of recognized *AFG3L2* pathogenic variants, while deletion/duplication testing has contributed **<1%** to date. [6]

### 10.3 Differential diagnosis

| Presentation | Important alternatives/distinguishing clues |
|---|---|
| Childhood dominant optic atrophy | *OPA1* first; also *ACO2, OPA3, WFS1, DNM1L, SSBP1, RTN4IP1, YME1L1, TMEM126A* |
| Acute/subacute optic neuropathy | LHON mtDNA variants, *DNAJC30*; toxic/nutritional optic neuropathy; optic neuritis, NMOSD, MOGAD |
| Spastic ataxia | *SPG7, SACS, KIF1C, CAPN1, CYP7B1, NKX6-2, GBA2, PNPLA6, FA2H, COQ4, MARS2, MTPAP* |
| Ataxia with neuropathy | Friedreich ataxia (*FXN*), RFC1-CANVAS, *SETX*, *APTX*, POLG-related disease |
| Ataxia with ocular motor abnormalities | *SPG7*, mitochondrial disease, SCA28, *CACNA1A*, repeat-expansion SCAs |
| Myoclonic epilepsy/regression | MERRF, POLG disease, Unverricht–Lundborg, Lafora disease and developmental epileptic encephalopathies |

*SPG7* disease can be clinically indistinguishable and requires molecular discrimination. [6]

### 10.4 Screening

- No population or newborn screening program exists.
- Targeted cascade testing is appropriate after identifying a familial variant.
- Predictive testing should be accompanied by genetic counseling because penetrance and severity are variable.
- Prenatal and preimplantation genetic testing are technically possible once familial variant(s) are established.

---

## 11. Outcome and prognosis

No reliable 5- or 10-year survival estimates, mortality rates or population life-expectancy data exist.

### Predominantly optic-atrophy phenotype

- Lifespan is not known to be shortened by isolated OPA12.
- Central acuity may remain stable for years or slowly deteriorate to severe visual impairment.
- Peripheral navigation can remain better than central acuity suggests.
- Neural visual loss is not currently reversible.

### Biallelic spastic-ataxia phenotype

- Prognosis is highly genotype- and severity-dependent.
- Milder patients may remain ambulatory for years with ataxia/spasticity and controlled epilepsy.
- Severe infantile disease can cause regression, microcephaly, intractable epilepsy, diffuse cerebral/cerebellar atrophy, profound dependence and early death; death as early as 2.5 years has been reported. [6]
- Potential complications include falls, contractures, scoliosis, aspiration, malnutrition, seizure injury, communication impairment and loss of ambulation.

No validated molecular prognostic biomarker exists. Likely adverse factors are biallelic null/severe loss-of-function genotypes, infantile regression, refractory epilepsy, diffuse brain atrophy and early respiratory-chain dysfunction. These remain clinically plausible rather than validated prediction-model variables.

---

## 12. Treatment

### 12.1 Current standard: supportive multidisciplinary care

There is **no approved disease-modifying treatment** and no disease-specific clinical-practice guideline. Management is individualized and multidisciplinary. [151]

| Manifestation | Intervention | Suggested NCIT annotation |
|---|---|---|
| Ataxia and weakness | Physical therapy, balance/gait training, strengthening, mobility aids, home fall prevention | Physical Therapy, NCIT:C15329; Rehabilitation Therapy |
| Impaired ADLs | Occupational therapy and adaptive utensils/devices | Occupational Therapy |
| Spasticity | Stretching; baclofen, tizanidine or clonazepam; focal botulinum toxin; orthotics | Baclofen NCIT:C617; Botulinum Toxin; Muscle Relaxant Therapy |
| Dystonia | Anticholinergic or baclofen therapy; botulinum toxin for focal dystonia | Pharmacotherapy; Botulinum Toxin Therapy |
| Myoclonic epilepsy | Levetiracetam or valproate where appropriate; alternatives include topiramate, zonisamide, lamotrigine, brivaracetam, piracetam, perampanel, clonazepam or clobazam | Anticonvulsant Therapy |
| Low vision/photophobia | Magnification, high-contrast materials, screen readers, orientation/mobility training, tinted lenses | Low Vision Rehabilitation |
| Ptosis | Blepharoplasty if functionally significant | Blepharoplasty, NCIT:C51597 |
| Dysarthria | Speech-language therapy and augmentative communication | Speech Therapy |
| Dysphagia | Feeding therapy, texture modification, aspiration precautions; gastrostomy for severe unsafe swallowing | Gastrostomy; Nutritional Support |
| Hearing loss | Hearing aids or specialist-directed auditory rehabilitation | Hearing Aid |
| Behavioral/psychiatric symptoms | Standard psychological, psychiatric and social interventions | Psychotherapy; Supportive Care |
| Nutrition | Dietitian assessment; avoid obesity while maintaining adequate calories | Nutritional Counseling |

Valproate requires special caution in females who may become pregnant and in undiagnosed mitochondrial disease where *POLG* has not been excluded. Carbamazepine and phenytoin may aggravate myoclonus.

### 12.2 Surveillance

- Neurology and standardized ataxia assessment: annually or more often if changing.
- PT/OT/physiatry mobility review: annually.
- Ophthalmology with acuity, OCT and functional assessment: annually.
- EEG/seizure review in SPAX5: every 6–12 months or as clinically indicated.
- Hearing, cognition, speech, swallowing, weight and mood: based on phenotype and progression.
- Genetic counseling: at diagnosis and reproductive decision points.

### 12.3 Experimental treatment

**Sephin-1/ISR potentiation.** In SPAX5 fibroblasts and *Afg3l2*-null mice, Sephin-1—an inhibitor of stress-induced eIF2α dephosphorylation—improved cell growth, Purkinje-neuron survival and arborization, mitochondrial ultrastructure/respiration and mouse survival. This is compelling **preclinical**, not patient-treatment, evidence. PMID:37804316. [61][67]

**Gene replacement.** An AAV-based *AFG3L2* replacement strategy is being investigated in SPAX5 mice, motivated by markedly reduced AFG3L2 protein in patient cells. This remains preclinical; a 2025 National Ataxia Foundation project specifically aimed to restore AFG3L2 in cerebellar and other neuronal systems. [159]

No disease-specific approved gene therapy, CRISPR therapy, ASO, siRNA, cell therapy or immunotherapy was identified, and no confirmed disease-specific interventional NCT study was found.

### 12.4 Pharmacogenomics

No CPIC/PharmGKB genotype-guided prescribing rule is specific to *AFG3L2*. Treatment is phenotype-guided rather than *AFG3L2*-allele-guided.

---

## 13. Prevention

### Primary prevention

Because this is an inherited disorder, lifestyle or vaccination cannot prevent a de novo or inherited pathogenic variant. Reproductive options after molecular diagnosis include:

- preconception carrier/partner testing;
- preimplantation genetic testing;
- chorionic-villus or amniotic-fluid prenatal diagnosis;
- donor gametes or adoption.

### Secondary prevention

- Cascade testing of at-risk relatives.
- Baseline OCT and neurologic examination in variant-positive relatives.
- Early developmental and seizure assessment in children at risk for biallelic disease.
- Periodic reinterpretation of initially negative genomic tests.

### Tertiary prevention

- Fall and contracture prevention.
- Prompt seizure treatment.
- Aspiration and nutritional surveillance.
- Low-vision rehabilitation.
- Hearing and communication support.
- Avoidance of excessive alcohol, unnecessary sedatives and medications that worsen myoclonus.

There is no applicable vaccine, antimicrobial prophylaxis or public-health environmental intervention.

---

## 14. Other species and natural disease

No well-established naturally occurring *AFG3L2*-ortholog disease in a domestic-animal breed was identified in OMIA; therefore, no validated breed/VBO annotation or veterinary natural-disease entity can currently be recommended. The condition is not infectious and has no zoonotic or cross-species transmission.

Relevant orthologous systems include:

| Species | Taxon | Ortholog/model relevance |
|---|---:|---|
| Human | NCBI Taxon:9606 | *AFG3L2*, NCBI Gene:10939 |
| Mouse | NCBI Taxon:10090 | *Afg3l2*, MGI:1916847; extensive spontaneous, knockout, conditional and knock-in models |
| Zebrafish | NCBI Taxon:7955 | *afg3l2*; human ortholog associated with optic atrophy and spastic ataxia |
| Fruit fly | NCBI Taxon:7227 | *Afg3l2*/FBgn0036702; tissue-specific knockdown models mitochondrial and locomotor defects |
| Budding yeast | NCBI Taxon:559292 | YTA10/YTA12 system used for complementation and protease-function testing |

The mitochondrial AAA+ protease mechanism is strongly evolutionarily conserved, which permits yeast complementation and cross-species modeling. [99][132][133]

---

## 15. Model organisms and experimental systems

| Model | Characteristics recapitulated | Applications and limitations |
|---|---|---|
| Homozygous *Afg3l2*-deficient/Emv66 or paralysé mouse | Small size, postural instability, limb dysmetria, axonal/myelination defects, paralysis, respiratory-complex impairment and death by about postnatal day 16 | Strong model of severe biallelic neurologic disease; perinatal lethality limits chronic-treatment studies |
| Heterozygous *Afg3l2* mouse | Late-onset motor incoordination, respiratory dysfunction, ROS and Purkinje-cell dark degeneration | Models cerebellar vulnerability; does not fully reproduce human OPA12 |
| Purkinje-cell conditional knockout | Mitochondrial fragmentation, abnormal dendritic mitochondrial distribution and Purkinje-cell death | Defines cell-autonomous cerebellar mechanism; excludes systemic/optic effects |
| Astrocyte-specific knockout | Bergmann-glia degeneration, altered EAAT2, reactive inflammatory signature and secondary Purkinje-cell dysfunction | Demonstrates non-cell-autonomous glial contribution |
| SPAX5 patient fibroblasts | Reduced AFG3L2, OMA1 activation, OPA1 overprocessing, fragmentation and integrated stress response | Human genotype-specific mechanistic and drug testing; fibroblasts do not reproduce neuronal circuitry |
| Patient-derived iPSCs | Protein instability, mitochondrial dysfunction and calcium overload | Potential differentiation into neurons/retinal ganglion cells; limited clinical numbers |
| Yeast complementation | Respiratory-growth and substrate-processing defects rescued by wild-type AFG3L2 | Efficient functional testing of variants; lacks vertebrate neurons and optic pathways |
| Drosophila knockdown | Shortened lifespan, locomotor defects and mitochondrial/muscle abnormalities; neuronal silencing can be near lethal | Rapid genetic/modifier screening; limited direct phenotypic correspondence |
| Zebrafish | Conserved ortholog and tractable visual/motor development | Promising for screening, but disease-specific phenotypic validation remains limited |

The foundational mouse study found reduced sciatic axons, reduced corticospinal neurofilament density, respiratory-chain defects and early paralysis, closely matching several SPAX5 features. PMID:18337413. [18] A Purkinje-cell conditional model showed that AFG3L2 supports mitochondrial protein synthesis and survival of the cell type most vulnerable in cerebellar disease. [124]

---

## Current expert interpretation and research priorities

1. **The 2024 ClinGen consensus is that OPA12 and SPAX5 are not wholly separate diseases but a semidominant *AFG3L2* loss-of-function spectrum.** This is the most authoritative current framework for MONDO:0700372. [18]
2. **Classic SCA28 should not automatically be merged into this entry.** Its protease-domain dominant-negative variants and lack of reported optic atrophy support separate curation.
3. **Variant dosage and domain help but do not fully predict phenotype.** The same allele can produce isolated optic atrophy in one person and extraocular movement disorder in another, while biallelic p.Met625Ile caused different ataxia-plus courses in two patients. [171]
4. **Mitochondrial proteostasis, OPA1-dependent dynamics and MCU-mediated calcium control are the central converging mechanisms.**
5. **The integrated stress response is a therapeutic lead rather than a simple injury marker.** The 2024 *Brain* study indicates OMA1–DELE1–HRI activation can protect stressed cells and neurons. [61]
6. **Major evidence gaps** include prospective natural history, standardized visual/ataxia outcomes, contemporary penetrance estimates, genotype-specific progression, patient-derived retinal-ganglion-cell models, validated fluid biomarkers, and human therapeutic trials.

## Key primary/recent literature

| Publication date | Study | Key contribution |
|---|---|---|
| 2011 | Pierson et al., PMID:22022284 | Homozygous p.Tyr616Cys established recessive SPAX5 and demonstrated hypomorphic protease function |
| April 2, 2020 | Caporali et al., PMID:32219868 | ATPase-domain variants, OPA1 overprocessing and mitochondrial fragmentation in optic neuropathy |
| March 8, 2023 | Brodsky et al., PMID:36974169 | p.Thr355Met dominant nonsyndromic optic atrophy diagnosed by exome reanalysis [167] |
| March 24, 2023 | Jin et al., PMID:37025825 | Severe biallelic developmental-neurodegenerative phenotype with epilepsy and global cerebral atrophy [166] |
| December 2023 | Colucci et al., PMID:36447112 | Marked clinical variability with the same biallelic p.Met625Ile genotype [175] |
| October 7, 2023 online / 2024 print | Franchino et al., PMID:37804316 | Protective OMA1–DELE1–HRI integrated stress response and Sephin-1 rescue in preclinical models [61] |
| November 28, 2023 online / July 2024 print | Ghosh Dastidar et al., PMID:38012514 | Contemporary mechanistic review of AFG3L2 proteostasis, OPA1, calcium and clinical disorders [16] |
| October 11, 2024 online | Compound-heterozygous iPSC study, PMID:39428429 | Protein instability, mitochondrial impairment and MCU-mediated calcium overload [78] |

Overall, **MONDO:0700372 is best modeled as a dosage-sensitive, semidominant mitochondrial-neurodegenerative disorder in which one *AFG3L2* loss-of-function/hypomorphic allele commonly produces optic-nerve-predominant disease, while biallelic impairment shifts the phenotype toward early, multisystem spastic ataxia, epilepsy and neurodevelopmental degeneration.**

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 14 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1093/brain/awad340/7296494` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 80 |
| Resolved | 71 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 9 |
| Terms whose name was checked | 12 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700372` (6 mentions) - the report calls it "MONDO"; MONDO calls it **AFG3L2-related optic atrophy and/or spastic ataxia spectrum**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006508` (2 mentions) - the report calls it "Protein proteolysis"; GO calls it **proteolysis**
- `GO:0007005` (2 mentions) - the report calls it "Mitochondrial organization"; GO calls it **mitochondrion organization**, and lists "mitochondrial organization" among its other names
- `CL:0000121` (1 mention) - the report calls it "Cerebellar Purkinje neuron"; CL calls it **Purkinje cell**, and lists "cerebellar Purkinje cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Gene`, `ORPHA`, `Taxon`, `MGI`.