---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T11:41:26.879295'
end_time: '2026-10-27T11:48:13.118789'
duration_seconds: 406.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Distal Arthrogryposis Type 5
  mondo_id: MONDO:0007158
  category: Genetic
  causal_genes: PIEZO2
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
citation_count: 53
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 14
  validator_version: 0.4.0
term_validation:
  total_terms: 66
  verified: 61
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0007158
    reported_labels:
    - MONDO
    ontology_label: arthrogryposis- oculomotor limitation-electroretinal anomalies
      syndrome
  - term_id: DOID:0111608
    reported_labels:
    - Disease Ontology
    ontology_label: distal arthrogryposis type 5
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Distal Arthrogryposis Type 5
- **MONDO ID:** MONDO:0007158 (if available)
- **Causal gene(s):** PIEZO2
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

Please provide a comprehensive research report on **Distal Arthrogryposis Type 5** covering all of the
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

# Distal Arthrogryposis Type 5: comprehensive disease-characteristics report

**Scope and nomenclature.** Distal arthrogryposis type 5 (DA5) is a congenital, usually autosomal-dominant mechanosensory channelopathy caused by heterozygous variants in **PIEZO2**, generally with a gain-of-function effect. The requested concept is **MONDO:0007158 / OMIM:108145 / ORPHA:1154**, not “distal arthrogryposis type 5D,” an autosomal-recessive, predominantly **ECEL1**-related disorder. DA5 combines congenital distal joint contractures with ocular-motor abnormalities—especially ophthalmoplegia, ptosis, or strabismus—and may include progressive restrictive thoracic disease. PIEZO2-related DA3/Gordon syndrome and Marden–Walker syndrome overlap substantially and may represent a phenotypic continuum. [16][24][105]

**Evidence status.** Most disease-specific clinical evidence consists of families and case series rather than population cohorts or randomized trials. Mechanistic evidence includes heterologous electrophysiology, a conditional knock-in mouse model, and a *Caenorhabditis elegans* suppressor model. No disease-specific prevalence study, validated prognostic model, approved molecular therapy, or controlled treatment trial was identified.

---

## 1. Disease information

### 1.1 Definition

DA5 is an inherited distal arthrogryposis in which congenital contractures predominantly affect the hands and feet, accompanied by characteristic ocular-motor involvement. Additional findings can include short stature, triangular or deeply set eyes, “woody” or unusually firm muscles, scoliosis or spinal rigidity, abnormal retinal/electroretinal findings, and restrictive pulmonary disease with secondary pulmonary hypertension. [122][149]

The landmark 2014 study found heterozygous **PIEZO2** variants in **24 of 29 DA5 families (83%)**, including 14/16 familial and 10/13 simplex cases. Its abstract concluded that DA5, Gordon syndrome, and Marden–Walker syndrome are “*etiologically related and perhaps represent variable expressivity of the same condition*” (PMID **24726473**, published May 1, 2014). [3]

### 1.2 Identifiers and synonyms

| Resource | Identifier/name | URL or note |
|---|---|---|
| MONDO | **MONDO:0007158** | Arthrogryposis–oculomotor limitation–electroretinal anomalies syndrome [24] |
| OMIM phenotype | **108145** | [OMIM 108145](https://www.omim.org/entry/108145); autosomal dominant, PIEZO2 [122] |
| OMIM gene | **PIEZO2: 613629** | Chromosome 18p11.22–p11.21 [150] |
| Orphanet | **ORPHA:1154** | Distinct from ORPHA:329457/DA5D [27] |
| MedGen | **C1862472**, UID 350678 | [NCBI MedGen](https://www.ncbi.nlm.nih.gov/medgen/C1862472/) [67] |
| Disease Ontology | **DOID:0111608** | [DO browser](https://www.informatics.jax.org/disease/DOID:0111608) [105] |
| MeSH | **C537737** supplementary concept | Reported by Disease Ontology [17] |
| SNOMED CT | **715217004** | Distal arthrogryposis type 5/oculomelic amyoplasia [67] |
| ICD-10 | **Q74.3** is commonly mapped for arthrogryposis multiplex congenita | No unique DA5-specific ICD-10 code [95] |
| ICD-11 | **LD26.4Y**, other specified syndromes with limb anomalies as a major feature | Broader distal-arthrogryposis category, not DA5-specific [102] |
| NCBI Gene | **PIEZO2, Gene ID 63895** | [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/63895) [76] |
| HGNC | **HGNC:26270** | Official symbol PIEZO2 [77] |
| Ensembl | **ENSG00000154864** | Human Protein Atlas/Open Targets cross-reference [87] |
| UniProt | **Q9H5I5** | PIEZO2 protein [275] |

**Accepted synonyms:** DA5; DAIIB; distal arthrogryposis type IIB; distal arthrogryposis with ophthalmoplegia; oculomelic amyoplasia; arthrogryposis with oculomotor limitation and electroretinal abnormalities/anomalies. [67][105]

**Important exclusion:** “DA5D,” “DA5 without ophthalmoplegia,” or OMIM **615065** generally refers to recessive **ECEL1** disease and should not be merged with MONDO:0007158. [68][120]

### 1.3 Data provenance

This entry is an **aggregated disease-level synthesis**. Its sources include OMIM, Orphanet, MedGen/HPO, ClinVar, published pedigrees and case series, and experimental models. It is not derived from a single EHR or individual patient record.

---

## 2. Etiology, risk factors, and protective factors

### 2.1 Primary cause

The established cause is a **heterozygous germline PIEZO2 variant**, usually altering channel inactivation or recovery so that mechanically activated currents are prolonged or more efficiently repeated—i.e., a **gain-of-function channelopathy**. In the original electrophysiological study, p.Glu2727del slowed inactivation and accelerated recovery, while p.Ile802Phe accelerated recovery; both increased activity in response to mechanical stimulation (PMID **23487782**, published March 19, 2013). [60][229]

> “Both types of changes in kinetics result in increased channel activity in response to a given mechanical stimulus.” — Coste et al., 2013, PMID 23487782. [257]

### 2.2 Risk factors

| Factor | Evidence and interpretation |
|---|---|
| Pathogenic heterozygous PIEZO2 variant | Necessary molecular risk factor for the requested disorder; inheritance may be familial or de novo. [3] |
| Affected parent | Each pregnancy has a theoretical **50% chance** of inheriting the familial variant, although severity cannot be predicted reliably because of variable expressivity. [317] |
| De novo mutation | Numerous simplex patients have de novo variants; parental testing is therefore essential. [3] |
| Parental mosaicism | Demonstrated for p.Glu2727del: an unaffected father carried approximately 10–12% variant allele fraction in blood, buccal cells, and saliva, indicating recurrence risk can exceed the usual assumption after an apparently de novo event. [3] |
| Family history | Increases prior probability, but absence of family history does not exclude DA5 because of de novo mutation, mosaicism, or subtle parental disease. |
| Variant location/function | Many reported variants cluster in or near the PIEZO2 C-terminal pore/channel region; 11/13 variants in the 2014 spectrum study affected the intracellular C-terminal region. [3] |

There are **no demonstrated age, sex, ethnic, occupational, dietary, infectious, or toxic-exposure risk factors for acquiring DA5**. Male-to-female transmission is expected to be equal for an autosomal-dominant disorder.

### 2.3 Protective factors and gene–environment interaction

No human protective allele, environmental prevention factor, or validated modifier gene has been established. A *C. elegans* screen identified reduced activity of **gex-3**, the worm ortholog of human **NCKAP1**, as an allele-specific suppressor of the PIEZO2-equivalent p.Arg2718Pro model; this is experimental modifier evidence, not a human protective association. [267]

In mice, an eicosapentaenoic-acid-enriched maternal diet shortened mutant PIEZO2 current inactivation and partially prevented joint malformation, showing a plausible lipid–channel interaction. It has **not** been shown to prevent or treat human DA5 and should not be interpreted as a dietary recommendation. [59]

No environmental toxin, lifestyle behavior, or infectious agent is known to cause or trigger the disorder.

---

## 3. Phenotypes

Frequencies are imprecise because cohorts are small and ascertainment favors classic ocular and respiratory cases. “Very frequent/frequent” designations below reflect HPO/Orphanet aggregation where available; later features are based on case series.

| Phenotype type | Phenotype and suggested HPO term | Onset, frequency, severity/course | Functional or quality-of-life effect |
|---|---|---|---|
| Physical manifestation | Distal arthrogryposis; **HP:0005684** or joint contracture **HP:0001371** | Congenital/usually prenatal; defining feature; severity variable and sometimes worsens during growth | Limits grasp, dressing, gait, transfers, and endurance |
| Sign | Joint contracture of hand **HP:0009473** | Very common; congenital; often bilateral | Reduced dexterity and fine-motor function |
| Sign | Camptodactyly of finger **HP:0100490**; broader camptodactyly **HP:0012385** | Frequent; congenital; fixed or progressive | Impairs grasp and release |
| Sign | Ulnar deviation of hand **HP:0009487** | Common; congenital | Alters wrist/hand mechanics |
| Sign | Bilateral talipes equinovarus **HP:0001776**; clubfoot **HP:0001762** | Common; prenatal/congenital | Delays standing or walking; may require casting/tenotomy |
| Sign | Limited wrist extension **HP:0006248**; absent/decreased palmar or phalangeal creases **HP:0010488/HP:0006184** | Congenital, variable | Marker of longstanding fetal contracture |
| Sign | Arachnodactyly **HP:0001166**, clinodactyly **HP:0030084** | Variable | Usually less disabling than contractures |
| Ocular sign | Ophthalmoplegia **HP:0000602** | Very frequent and often congenital; usually persistent | Restricted gaze, compensatory head posture, possible visual disability |
| Ocular sign | Ptosis **HP:0000508** | Very frequent; congenital; mild to marked | May obstruct visual axis or contribute to amblyopia |
| Ocular sign | Strabismus **HP:0000486** | Frequent/variable | Diplopia or amblyopia risk |
| Ocular/laboratory sign | Abnormal electroretinogram **HP:0000512**; abnormal retinal pigmentation **HP:0007703** | Reported as frequent in historical aggregation, but not universal | Requires retinal surveillance; clinical visual impact varies [73][377] |
| Craniofacial sign | Deep-set eyes **HP:0000490**, triangular face **HP:0000325**, blepharophimosis **HP:0000581** | Congenital, variable | Primarily appearance; possible psychosocial impact |
| Growth | Short stature **HP:0004322** | Common/very frequent in classic series; may become clearer with age | Affects reach and mobility |
| Muscle sign | Firm or “woody” muscles **HP:0003707**; hypertonia **HP:0001276** | Variable; chest and abdominal muscles may be prominent | May contribute to rigidity and respiratory restriction |
| Axial musculoskeletal | Scoliosis **HP:0002650**, kyphosis **HP:0002808**, stiff spine/joint stiffness **HP:0001387** | Childhood to adult; can progress | Pain, mobility loss, reduced thoracic expansion |
| Respiratory sign/test | Restrictive ventilatory defect **HP:0002091**; exertional dyspnea **HP:0002875** | Reported in approximately **35%** in a 2023 review; may emerge or progress in childhood/adulthood | Exercise intolerance, nocturnal hypoventilation, pulmonary hypertension, respiratory failure [398] |
| Cardiopulmonary complication | Pulmonary hypertension **HP:0002092** | Uncommon; secondary to severe restrictive chest disease/chronic hypoventilation | Potentially life-threatening [150] |
| Feeding/sign | Dysphagia **HP:0002015**, neonatal poor suck/feeding difficulty | Variable; can occur in infancy or later | Aspiration and nutritional risk |
| Neurologic sign | Hyporeflexia **HP:0001265**, hypotonia **HP:0001252** | Reported in some infants; not the defining mechanism | May delay motor milestones |
| Skeletal sign | Absent anterior cruciate ligaments, knee instability/recurrent patellar dislocation **HP:0005001** | Occasional; congenital structural anomaly | Instability, falls, pain; reported in the original PIEZO2 family [409] |
| Pain | Back, joint, or limb pain | More evident in older patients; frequency in DA5 is being formally studied | Can reduce mobility, sleep, and quality of life [226] |
| Additional rare findings | Metacarpal/metatarsal synostosis, optic-disc excavation, raised intraocular pressure, keratoconus/keratoglobus, dysphagia and spinal-stenosis-like symptoms | Family- or patient-specific; uncertain frequencies | Support long-term ophthalmic and spinal surveillance [407] |
| Possible expanded phenotype | Pretibial vertical crease, immobile skin/tongue, lipid myopathy | One severe 2023 case; association requires replication | Severe respiratory course [38] |

The 2014 cohort showed that cognitive delay was generally absent among DA5-labelled individuals, although central nervous-system abnormalities can occur in overlapping Marden–Walker-spectrum cases. [3]

A 2024 Russian series of seven patients reported more severe disease with c.8238G>A and c.7095G>T than with p.Glu2727del or p.Met712Val, and noted that manifestations may progress as the child grows; these genotype–phenotype observations require replication. [169]

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Attribute | Information |
|---|---|
| Gene | **PIEZO2**, HGNC:26270; NCBI Gene 63895; OMIM 613629 |
| Location | 18p11.22–p11.21 |
| Protein | Large, multi-pass plasma-membrane, mechanically activated nonselective cation channel; more than 30 predicted transmembrane regions |
| Principal physiological role | Converts membrane force into cation influx/electrical signaling in mechanosensory neurons, especially touch receptors and proprioceptors |
| Subcellular location | Plasma/cell membrane; multi-pass membrane protein |
| Disease mechanism | For dominant DA5, predominantly altered channel gating/inactivation causing gain of mechanotransduction function |
| Variant origin | Constitutional/germline; inherited, de novo, or parental mosaic. No evidence that somatic mutation is a usual cause |
| HGNC/NCBI | HGNC:26270; Gene ID 63895 [76][77] |

### 4.2 Published DA5-associated variants

HGVS differs by transcript; older literature predominantly uses **NM_022068.3**. A variant should be normalized to the laboratory transcript before database import.

| PIEZO2 variant | Type | DA5 evidence/classification | Functional or population evidence |
|---|---|---|---|
| p.Ile802Phe | Missense | Pathogenic disease-associated variant in original DA5 study | Faster recovery from inactivation; gain of channel activity, PMID 23487782 [257] |
| c.2134A>G, p.Met712Val | Missense | Reported in two DA5 families; ClinVar status should be checked by current accession | Disease association from PMID 24726473 [3] |
| c.2993T>C, p.Met998Thr | Missense | De novo, likely pathogenic in published DA5 cohort | Associated with ophthalmoplegia, scoliosis and pulmonary disease [401] |
| c.2994G>A, p.Met998Ile | Missense | Recurrent de novo pathogenic/likely pathogenic variant; severe reported case | 2023 case with respiratory insufficiency and lipid myopathy, PMID 36317804 [391] |
| c.2993T>C equivalent nomenclature requires transcript confirmation | Missense | Do not merge automatically with p.Met998Ile | Transcript/numbering ambiguity |
| c.4456G>C, p.Ala1486Pro | Missense | Segregated in a two-generation four-person DA5 family | Restrictive lung disease in older but not younger relatives; PMID 25712306 [331] |
| c.6662C>T, p.Thr2221Ile | Missense | Multiple DA5 families, some de novo | Predicted structural effect; no disease-specific allele frequency reported [3] |
| c.6668C>T, p.Ser2223Leu | Missense | De novo DA5 report | Limited direct functional evidence [3] |
| c.7067C>T, p.Thr2356Met | Missense | Familial DA5 report | Limited direct functional evidence [3] |
| c.7095G>T, p.Trp2365Cys | Missense | Reported as newly identified pathogenic heterozygous variant in 2024 Russian series | Associated with severe phenotype; independent confirmation needed [169] |
| c.8057G>A, p.Arg2686His | Missense | Recurrent across DA3 and DA5; phenotype-dependent classification | Demonstrates allelic/phenotypic overlap; no cleft palate in two DA5 probands [3] |
| c.8068A>C, p.Ser2690Arg | Missense | **VUS** in a three-generation Canadian DA5 family | Segregation supportive but insufficient for definitive pathogenic classification, PMID 30938034 [332] |
| c.8153G>T, p.Arg2718Leu | Missense | Familial likely pathogenic DA5 variant | Multiple affected relatives; direct functional evidence limited [347] |
| c.8153G>C, p.Arg2718Pro | Missense | De novo likely pathogenic/pathogenic | GOF supported by orthologous worm electrophysiology and mouse/worm disease modeling [267] |
| c.8181_8183delAGA, p.Glu2727del | In-frame deletion | Recurrent pathogenic hotspot; 10/24 variant-positive DA5 families in 2014 | Slower inactivation plus faster recovery; ClinVar pathogenic; absent from gnomAD according to ClinVar [166][353] |
| c.8208delA, p.Tyr2737IlefsTer7 | Frameshift near terminal exon | De novo DA5 report | Mechanism may differ from ordinary haploinsufficiency; limited functional evidence [3] |
| c.8215T>C, p.Ser2739Pro | Missense | Familial DA5 report | Limited functional evidence [3] |
| c.8238G>A, reported p.Trp2746Ter or p.Trp274Ter | Nonsense; nomenclature conflict | Reported in severe DA5 | Must be transcript-normalized; apparently near-terminal and not assumed to be simple haploinsufficiency [172][169] |

**Interpretive caution:** not every heterozygous PIEZO2 variant causes DA5. Biallelic loss-of-function variants cause **distal arthrogryposis with impaired proprioception and touch (DAIPT; OMIM 617146)**, a distinct recessive disorder. Variant mechanism, phase, phenotype, segregation, population frequency, and functional evidence must be considered together. [10][150]

### 4.3 Modifier, epigenetic and structural evidence

- **Human modifier genes:** none validated.
- **Experimental modifier:** *gex-3/NCKAP1–WAVE–Arp2/3 actin regulation* suppressed some effects of the p.Arg2718Pro-equivalent worm allele; transferability to humans is unknown. [267]
- **Epigenetics:** no DA5-specific methylation, histone, or chromatin signature identified.
- **Chromosomal abnormalities:** DA5 is not ordinarily caused by aneuploidy, translocation, or large copy-number change.
- **Molecular profiling:** no validated patient transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, or multi-omic diagnostic signature was found.
- PIEZO2 is extensively alternatively spliced, but disease-specific isoform effects in DA5 remain insufficiently characterized. [361]

---

## 5. Environmental, lifestyle, and infectious information

No environmental exposure, radiation, pollution, toxin, occupation, smoking, alcohol, diet, or infectious agent is established as a cause or trigger. Reduced fetal movement is part of the developmental pathway to contracture, but in PIEZO2 DA5 it is interpreted as a downstream consequence of altered neurosensory–musculoskeletal signaling rather than an external exposure.

Ordinary exercise, diet, or infection has not been shown to change genetic penetrance. Respiratory infections can plausibly destabilize a person with severe restrictive physiology, but are complications rather than etiologic factors.

The experimental EPA diet and botulinum-toxin results are mouse data only; neither constitutes proven human environmental protection. [59]

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. A **heterozygous PIEZO2 gating-region variant** leads to altered channel inactivation and/or faster recovery from inactivation.  
2. Altered gating leads to **excessive or prolonged mechanically activated cation current** during repetitive mechanical stimulation.  
3. Excess current leads to abnormal mechanotransduction in PIEZO2-expressing peripheral sensory neurons, particularly proprioceptive neurons innervating muscle spindles and Golgi tendon organs.  
4. In mice, sensory-neuron hyperfunction leads to increased local efferent/exocytotic signaling from afferent endings; the precise secreted mediator is **inferred, not demonstrated**.  
5. Abnormal sensory-terminal signaling during a developmental critical window leads to shortened tendons and altered joint development; direct expression in limb mesenchyme alone does not reproduce the phenotype in mice.  
6. Shortened tendons and abnormal neuromusculoskeletal loading lead to fixed distal joint contractures, clubfoot, camptodactyly, and reduced limb function.  
7. **Branch A:** analogous dysfunction in ocular-motor/proprioceptive systems leads—mechanistically still incompletely demonstrated—to ophthalmoplegia, ptosis, and strabismus.  
8. **Branch B:** spinal/chest-wall rigidity and contracture lead to reduced thoracic expansion, which results in restrictive ventilatory impairment and, in severe cases, hypoventilation, pulmonary hypertension, or respiratory failure.  
9. **Branch C:** persistent abnormal mechanical signaling after birth may lead to worsening contractures, pain, spinal disease, and variable progression; this downstream human mechanism remains partly inferred.

### 6.2 Molecular and cellular detail

PIEZO2 is a pore-forming plasma-membrane mechanosensitive cation channel. The 2013 study found that p.Glu2727del and p.Ile802Phe did **not** cause constitutive current or overt cellular toxicity; instead, they changed gating so repetitive force produced greater net channel activity. This supports a mechanotransduction defect rather than protein aggregation, apoptosis, or primary metabolic toxicity. [257]

The strongest contemporary mechanism comes from the 2023 *Science* study (PMID **36634173**, January 13, 2023):

> “Expression of a gain-of-function PIEZO2 mutation in proprioceptive sensory neurons…is sufficient to induce DA5-like phenotypes in mice.” [46]

Conditional p.Glu2727del-equivalent expression in **Pvalb-positive proprioceptive sensory neurons** produced joint contractures, shortened tendons, and impaired motor performance. Expression in **Prrx1-positive limb mesenchyme**, including skeletal muscle, cartilage, and tendon, did not. Induction before or during postnatal days 7–10 produced abnormalities, whereas induction after postnatal day 21 or in adulthood did not, identifying a mouse developmental critical window. [59]

Botulinum toxin rescued joint/tendon defects, whereas repeated α-bungarotoxin blockade of motor-neuron-to-muscle transmission did not. The investigators therefore inferred that local exocytosis from sensory afferent endings, rather than excessive motor output, mediates the structural phenotype. Measured muscle-spindle firing was not significantly increased ex vivo, emphasizing that the exact downstream signal remains unresolved. [59]

### 6.3 Other pathway categories

| Category | Current conclusion |
|---|---|
| Canonical Wnt/MAPK/mTOR/PI3K-AKT | No DA5-specific causal role established |
| Ion-channel defect | Central demonstrated biochemical abnormality |
| Calcium signaling/exocytosis | Mechanistically plausible downstream of cation influx; local exocytosis is supported indirectly by mouse pharmacology |
| Actin cytoskeleton | Worm suppressor evidence implicates NCKAP1/WAVE/Arp2/3 regulation, not yet verified in human DA5 |
| Apoptosis/autophagy/cell cycle | No central evidence |
| Metabolism | No reproducible metabolic signature; one severe case had lipid myopathy |
| Immune/inflammation | No primary immune or inflammatory mechanism |
| Tissue injury | Mainly developmental malformation and mechanical/functional deterioration rather than necrosis or fibrosis |
| Epigenetics | No disease-specific evidence |

### 6.4 Suggested ontology annotations

- **GO molecular function:** mechanosensitive monoatomic cation channel activity, **GO:0008381**; monoatomic cation channel activity, **GO:0005261**.
- **GO biological process:** response to mechanical stimulus, **GO:0009612**; detection of mechanical stimulus involved in sensory perception, **GO:0050974**; regulation of membrane potential, **GO:0042391**; cation transport, **GO:0006812**.
- **GO cellular component:** plasma membrane, **GO:0005886**; neuronal cell-body membrane where applicable.
- **Cell Ontology:** sensory neuron, **CL:0000101**; mechanoreceptor cell, **CL:0000199**; sensory neuron of dorsal root ganglion, **CL:1001451**; dorsal-root-ganglion PIEZO2 neuron, **CL:4033181**; skeletal muscle cell, **CL:0000188**; tendon cell, **CL:0000388**. [286][290][292]

---

## 7. Anatomical structures affected

| Level | Principal structures | Suggested ontology terms |
|---|---|---|
| Organ/system | Distal upper and lower limbs; ocular motor system; musculoskeletal and peripheral nervous systems | UBERON:0002398 manus/hand; UBERON:0002387 pes/foot |
| Joints | Finger, wrist, toe, ankle; variably knee, hip, shoulder and spine | UBERON:0001488 ankle joint; generic joint UBERON:0000982 |
| Muscle/tendon | Hand/foot tendons, chest-wall and abdominal muscles, extraocular muscles; tendon shortening shown in mouse model | Skeletal muscle tissue UBERON:0001134; chest muscle UBERON:0002426 |
| Peripheral sensory structures | DRG proprioceptors, muscle spindles and Golgi tendon organs | Dorsal root ganglion UBERON:0000044 |
| Eye | Eyelids, extraocular muscles, retina/optic disc and occasionally cornea | Retina UBERON:0000966; eye UBERON:0000970 |
| Spine/thorax | Vertebral column, chest wall, sometimes pectus excavatum | Vertebral column UBERON:0001130 |
| Respiratory | Thoracic mechanics and secondarily lungs/pulmonary circulation | Lung UBERON:0002048 |
| Subcellular | PIEZO2-containing plasma membrane; no primary mitochondrial, nuclear, ER, or lysosomal lesion | GO:0005886 plasma membrane |

Contractures and clubfeet are commonly **bilateral**, although severity may be asymmetric. Ptosis can be bilateral or asymmetric; no fixed right/left lateralization is recognized.

---

## 8. Temporal development and natural history

- **Initiation:** prenatal developmental abnormality; reduced fetal movement, flexed wrists or clubfeet may be detected by second-trimester ultrasound. [164]
- **Clinical onset:** congenital/neonatal. Contractures and ocular restriction are usually present at birth.
- **Early childhood:** feeding difficulty, respiratory distress, delayed motor milestones, and treatment of clubfoot/hand contractures may dominate.
- **Growth:** contractures can remain stable, improve with early therapy, recur after correction, or worsen as the child grows. The 2024 Russian series explicitly reported possible progression. [169]
- **Adolescence/adulthood:** scoliosis or spinal rigidity, pain, dysphagia, raised intraocular pressure, spinal-stenosis-like symptoms, and progressive restrictive lung disease may emerge. [407]
- **Remission:** spontaneous molecular remission is not expected. Mechanical deformities may improve with therapy but commonly recur.
- **Critical period:** mouse data indicate a postnatal developmental window corresponding to P7–P21; the equivalent human period is unknown and should not be assumed to be postnatal. [59]
- **Duration:** lifelong.

---

## 9. Inheritance and population characteristics

| Characteristic | Best current evidence |
|---|---|
| Inheritance | Autosomal dominant for PIEZO2-related DA5 |
| Penetrance | Not quantified; likely high for clinically significant variants but demonstrably incomplete or threshold-dependent in a low-level mosaic father |
| Expressivity | Markedly variable both within and between families |
| Anticipation | No evidence |
| Germline/somatic mosaicism | Parental multi-tissue mosaicism documented; germline involvement cannot be excluded |
| Founder effect | None established |
| Consanguinity | Not relevant to usual dominant DA5; relevant instead to biallelic PIEZO2/DAIPT or ECEL1 DA5D |
| Carrier frequency | Not established; dominant pathogenic alleles are individually extremely rare |
| Sex ratio | No documented difference; both sexes affected |
| Ethnic/geographic enrichment | None established; families reported from multiple populations |
| Prevalence/incidence | **Unknown for DA5 specifically** |
| General AMC/DA statistic | Approximately 1 per 3,000 live births is often quoted for arthrogryposis/DA collectively, but must not be assigned to PIEZO2 DA5. [109][110] |

The 2014 finding that PIEZO2 variants explained 24/29 ascertained DA5 families is a **diagnostic yield in a selected cohort**, not a population prevalence estimate. [3]

---

## 10. Diagnostics

### 10.1 Clinical suspicion and criteria

A general distal-arthrogryposis diagnosis requires at least two major distal criteria in a proband—e.g., camptodactyly/pseudocamptodactyly, absent flexion creases, overriding fingers or ulnar wrist deviation; and talipes equinovarus, calcaneovalgus, vertical talus or metatarsus varus. One criterion may suffice in a relative of a clearly affected proband. Ocular-motor restriction strongly suggests DA5. [151]

### 10.2 Recommended evaluation

| Domain/test | Purpose and expected findings |
|---|---|
| Detailed prenatal/perinatal history | Fetal movement, oligohydramnios, contractures, respiratory or feeding difficulty |
| Dysmorphology and joint examination | Document distribution, passive range of motion, palmar/phalangeal creases, muscle firmness, spine and chest-wall rigidity |
| Ophthalmology | Alignment, ocular motility, ptosis, refraction, visual acuity, intraocular pressure, optic disc and retina |
| Electroretinography | Consider when retinal disease, night-vision complaint or abnormal pigmentation is suspected; abnormal ERG is reported but not universal |
| Pulmonary function | Serial spirometry, FVC, lung volumes and respiratory-muscle assessment; FVC as low as 26–50% has been described in severe disease [210] |
| Sleep/respiratory evaluation | Oximetry or polysomnography if hypoventilation, fatigue, morning headache or severe restriction |
| Echocardiography | If severe restriction, hypoxia, murmur or suspected pulmonary hypertension |
| Imaging | Limb/spine radiographs; ultrasound in infancy; CT/MRI guided by instability, spinal stenosis, or surgical planning |
| EMG/nerve conduction | Often not diagnostic; useful if primary neuropathy/myopathy is suspected |
| Laboratory testing | CK and routine blood chemistry may be normal; no specific biochemical biomarker |
| Feeding/swallow study | If dysphagia, recurrent pneumonia or poor growth |
| Audiology | Not a defining test, but hearing loss has been reported in individual patients |

### 10.3 Genetic testing algorithm

1. **First-line:** multigene distal-arthrogryposis panel including at least **PIEZO2, ECEL1, FBN2, MYBPC1, MYH3, MYH8, NALCN, TNNI2, TNNT3, TPM2**. [155][320]
2. If the ocular phenotype is strongly classic and resources favor focused testing, perform full **PIEZO2 sequencing** with copy-number assessment.
3. Use **trio WES or WGS** when panel testing is negative, phenotype is atypical, or de novo status is important.
4. Confirm a candidate variant by orthogonal testing and perform **parental segregation testing**, including attention to low-level mosaicism.
5. **CMA/karyotype/FISH** are not primary DA5 tests, but CMA is appropriate when multiple congenital anomalies or developmental delay suggest a chromosomal disorder.
6. Mitochondrial, repeat-expansion and liquid-biopsy testing have no routine role.
7. RNA sequencing may help selected splice-variant interpretation but is not a validated DA5 diagnostic assay.

A negative PIEZO2 result does not exclude distal arthrogryposis and should trigger evaluation of alternative genes and acquired fetal-akinesia causes.

### 10.4 Differential diagnosis

| Differential | Distinguishing features |
|---|---|
| PIEZO2-related DA3/Gordon syndrome | Cleft palate/bifid uvula more characteristic; substantial overlap |
| Marden–Walker syndrome/PIEZO2 spectrum | Mask-like face, blepharophimosis, micrognathia, neurodevelopmental or hindbrain abnormalities |
| PIEZO2 biallelic DAIPT | Recessive; marked proprioceptive and touch impairment, sensory ataxia, weakness |
| ECEL1-related DA5D | Recessive; asymmetric ptosis but typically no classic ophthalmoplegia |
| Freeman–Sheldon/Sheldon–Hall syndromes | MYH3 or TNNI2/TNNT3/TPM2-related facial and contracture patterns |
| Congenital myopathy/muscular dystrophy | Primary weakness, elevated CK or myopathic pathology in some disorders |
| Congenital fibrosis of extraocular muscles | Dominant ocular-motor abnormality without the characteristic generalized distal-contracture pattern |
| Fetal akinesia sequence | Broader prenatal immobility, pulmonary hypoplasia and multiple etiologies |
| Schwartz–Jampel syndrome | Myotonia, chondrodysplasia and characteristic electrophysiology |

---

## 11. Outcome and prognosis

No reliable 5-year survival, 10-year survival, life-expectancy, or disease-specific mortality rate exists.

Most mildly or moderately affected individuals appear capable of long-term survival and substantial independence. Prognosis depends principally on contracture severity, spinal/chest-wall rigidity, respiratory impairment, ocular disability, dysphagia, and pain. A lethal respiratory course has nevertheless been reported in a boy with de novo p.Met998Ile, showing that severe respiratory disease is possible. [391]

A three-generation p.Glu2727del family had congenital DA and ophthalmoplegia in all four affected members but variable later mobility and joint restriction; longer-term complications included dysphagia, back pain, spinal-stenosis-like symptoms, raised intraocular pressure, and progressive restrictive lung disease. [407]

Disease-specific quality-of-life data are lacking. In broader adult arthrogryposis cohorts:

- A 177-person international study found lower physical function and activity, but similar or higher nonphysical SF-36 domains; **50% reported chronic back pain and 60% joint pain**. [198]
- A 42-person adult study found back pain in 60%, hip pain in 50%, wrist pain in 58%, and reduced physical function despite self-rated quality of life similar to the general population. These figures are not DA5-specific. [196]

There are no validated molecular prognostic biomarkers. Baseline and serial FVC, spinal rigidity, scoliosis, swallowing function and functional mobility are practical prognostic measures.

---

## 12. Treatment and current applications

### 12.1 Current standard of care

There is **no curative or approved PIEZO2-targeted therapy**. Management is individualized and multidisciplinary.

| Intervention | Role and evidence | Suggested NCIT intervention concept |
|---|---|---|
| Physical therapy | Early passive/active range-of-motion work, stretching and strengthening; may improve early contractures but cannot reliably prevent recurrence | Physical Therapy |
| Occupational/hand therapy | Fine-motor function, adaptive equipment and independence in activities of daily living | Occupational Therapy |
| Orthoses/splints | Maintain correction, support wrists/hands/feet and reduce recurrence | Orthotic Device |
| Serial casting | Particularly for clubfoot and selected contractures | Cast Application |
| Ponseti method | Manipulation, serial casting, Achilles tenotomy and bracing for clubfoot; used in the reported Italian infant | Clubfoot Correction; Tendon Release [214] |
| Orthopedic surgery | Tendon lengthening/transfer, contracture release, osteotomy, joint stabilization or spinal surgery when function is likely to improve | Corrective Surgery; Tendon Lengthening; Spinal Fusion |
| Ophthalmic treatment | Refraction/amblyopia management; selected ptosis or strabismus surgery; intraocular-pressure monitoring and treatment | Ophthalmic Surgery; Strabismus Surgery |
| Respiratory support | Vaccination, airway-clearance support, noninvasive ventilation when hypoventilation occurs, and pulmonary-hypertension evaluation | Noninvasive Ventilation; Respiratory Therapy |
| Feeding support | Swallow therapy, nutritional intervention and tube feeding when aspiration or poor growth is significant | Nutritional Support; Enteral Nutrition |
| Pain management | Multimodal rehabilitation, positioning, orthotics and individualized analgesia; DA5-specific evidence is limited | Pain Management |
| Psychosocial support | School/work accommodations, genetic counseling and support for visible differences/chronic disability | Psychosocial Intervention; Genetic Counseling |

A 2024 review emphasizes early rehabilitation and reconstructive surgery while noting that recurrence is common. [211]

### 12.2 Experimental and emerging approaches

**Mouse proof of concept—not human treatment:**

- A single intramuscular botulinum-toxin injection at P7–P10 rescued joint and tendon abnormalities in treated mouse hindlimbs.
- Maternal EPA-enriched diet partially prevented joint malformation and improved motor assays.
- Neither intervention has demonstrated human efficacy or safety for preventing DA5 malformation. [59]

Suggested chemical annotation: **eicosapentaenoic acid, CHEBI:28364**; botulinum toxin type A should be annotated as an experimental neuromuscular-blocking biological product, not standard DA5 therapy.

**Human studies:** PAOLO3, **NCT07360574**, is a French noninterventional, 14-day observational study of people aged ≥10 years with confirmed PIEZO2 gain-of-function variants. It measures daily pain, body distribution, EQ-5D-5L, SF-12 and existing treatments; it does not administer therapy. [227]

A proposed adult trial aims to test a repurposed voltage-gated sodium-channel antagonist for pain, but no public NCT identifier, drug name, response rate, or results were available. [226]

No gene therapy, CRISPR therapy, ASO, siRNA, cell therapy, immunotherapy, or approved channel-selective antagonist is currently available.

---

## 13. Prevention

### Primary prevention

Because DA5 results from a constitutional genetic variant, diet, exercise, vaccination, or exposure avoidance cannot prevent a sporadic mutation or reliably prevent phenotype after inheritance.

### Genetic and reproductive prevention

- Obtain a three-generation pedigree and examine apparently unaffected parents for subtle contractures, bifid uvula, ptosis or ocular-motor restriction.
- Test parents for the proband’s variant, with mosaicism-sensitive analysis if recurrence counseling depends on the result.
- An affected heterozygous individual has a **50% transmission probability per pregnancy**; phenotype severity cannot be predicted accurately.
- Targeted prenatal diagnosis by chorionic-villus sampling or amniocentesis is technically possible after identifying a familial pathogenic variant.
- Preimplantation genetic testing for a known familial variant is technically possible.
- Prenatal ultrasound may identify reduced movement, flexed wrists, clubfeet, oligohydramnios, or other contractures; a normal scan does not exclude DA5. [317][324]

### Secondary and tertiary prevention

- Cascade testing and early assessment of at-risk relatives.
- Early PT/OT, casting and orthotic management to preserve range of motion.
- Serial pulmonary function, sleep-respiratory assessment when indicated, spine examination, ophthalmology including intraocular pressure, swallowing assessment, and nutrition monitoring.
- Prompt treatment of respiratory infection and hypoventilation in patients with restrictive disease.
- Vaccination follows ordinary age- and risk-based schedules; no DA5-specific vaccine exists.

Population newborn screening and general-population carrier screening are not indicated for this rare dominant disorder.

---

## 14. Other species and natural disease

| Species | Taxonomy/ortholog | Natural disease evidence | Comparative relevance |
|---|---|---|---|
| Human, *Homo sapiens* | NCBI Taxon 9606; PIEZO2 Gene 63895 | Natural DA5 | Reference disease |
| Mouse, *Mus musculus* | NCBI Taxon 10090; **Piezo2 Gene 667742**, MGI:1918781 | No analogous common spontaneous veterinary syndrome identified | Engineered GOF model recapitulates contractures and shortened tendons [242] |
| *Caenorhabditis elegans* | NCBI Taxon 6239; *pezo-1* is the sole PIEZO1/PIEZO2 ortholog | No natural DA5 equivalent | CRISPR GOF and suppressor-screen model |
| Domestic horse, cattle, goat, sheep | Various genes/unknown in generic arthrogryposis records | Natural arthrogryposis occurs, but no evidence links the generic syndromes specifically to PIEZO2 | Phenotypic, not established molecular, similarity [241] |
| Zebrafish and other vertebrates | Conserved Piezo orthologs | No verified spontaneous PIEZO2-DA5 syndrome found | PIEZO2 expression/mechanosensation is evolutionarily conserved |

There is no zoonotic potential or cross-species transmission; DA5 is not infectious.

---

## 15. Model organisms and experimental systems

| Model | Construction | Recapitulated findings | Applications and limitations |
|---|---|---|---|
| Heterologous human-cell electrophysiology | Wild-type or p.Ile802Phe/p.Glu2727del PIEZO2 cDNA in cultured cells | Slower inactivation and/or faster recovery, increased response to repeated mechanical stimulus; no constitutive toxicity | Establishes channel GOF but lacks tissue development and neural circuitry; PMID 23487782 [257] |
| Conditional knock-in mouse | Human-equivalent p.Glu2727del allele, mouse p.Glu2799del, activated globally or by tissue-specific Cre | Contractures, smaller joint angles, shortened tendons, abnormal gait and poor hanging/inverted-screen performance | Best mechanistic DA5 model; ocular and respiratory phenotypes were not comprehensively reproduced [59] |
| Proprioceptor-specific mouse | Pvalb-Cre activation | Sufficient to cause DA5-like musculoskeletal phenotype | Identifies proprioceptive sensory neurons as key upstream cell type |
| Limb-mesenchyme mouse | Prrx1-Cre activation | Normal joint angles/tendon lengths | Shows muscle/cartilage/tendon expression alone is insufficient in this system |
| Inducible sensory-neuron mouse | Advillin-CreERT2 at embryonic, P7–10, P21 or adult stages | Phenotype after early but not late induction | Defines developmental window and enables intervention testing |
| Pharmacologic mouse | Botulinum toxin, α-bungarotoxin, EPA-enriched diet | Botulinum toxin and EPA improved selected outcomes; α-bungarotoxin did not | Proof of mechanism only; dosing, developmental timing and human safety/efficacy remain unknown |
| CRISPR *C. elegans* | *pezo-1(R2405P)*, orthologous to human p.Arg2718Pro | GOF current, low brood size, low ovulation and crushed oocytes rather than limb contractures | High-throughput modifier screen; does not anatomically recapitulate human DA5 |
| Worm suppressor model | *gex-3(L353F)* or *gex-3* RNAi with *pezo-1(R2405P)* | Crushed oocytes fell from 31.4% to 11.1%; partial restoration of ovulation and actin organization | Implicates NCKAP1/WAVE/F-actin regulation; likely allele-specific and not yet validated in humans [267] |

The 2024 worm study’s key abstract conclusion was that the suppressor “*suggests that the PIEZO coordinates with the cytoskeleton regulator to maintain the F-actin network*” (PMID **38349741**, published February 13, 2024). [14]

---

## Overall assessment

DA5 is best understood as a **PIEZO2 gain-of-function developmental mechanotransduction disorder**. Its defining clinical combination is congenital distal contracture plus ocular-motor limitation, but respiratory, spinal, retinal, swallowing and pain complications justify lifelong multidisciplinary surveillance. The strongest recent advance is the 2023 demonstration that excessive PIEZO2 activity in proprioceptive sensory neurons—not simply a primary muscle defect—is sufficient to produce contractures in mice. The major unresolved questions are the identity of the sensory-neuron-derived developmental signal, reliable human genotype–phenotype relationships, true prevalence and penetrance, natural history into later adulthood, and whether channel-modulating or sensory-terminal therapies can safely improve human disease.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 66 |
| Resolved | 61 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007158` (3 mentions) - the report calls it "MONDO"; MONDO calls it **arthrogryposis- oculomotor limitation-electroretinal anomalies syndrome**
- `DOID:0111608` (3 mentions) - the report calls it "Disease Ontology"; DOID calls it **distal arthrogryposis type 5**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.