---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-18T05:28:45.759479'
end_time: '2026-10-18T05:33:08.490994'
duration_seconds: 262.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Gabriele-de Vries Syndrome
  mondo_id: MONDO:0044738
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
citation_count: 58
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 99
  verified: 93
  not_found: 0
  obsolete: 3
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0044738
    reported_labels:
    - MONDO
    ontology_label: Gabriele de Vries syndrome
  obsolete_terms:
  - term_id: GO:0016573
    ontology_label: obsolete histone acetylation
  - term_id: GO:0044237
    ontology_label: obsolete cellular metabolic process
    replaced_by: GO:0008152
  - term_id: CL:0002609
    ontology_label: obsolete neuron of cerebral cortex
    replaced_by: CL:0010012
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
- **Disease Name:** Gabriele-de Vries Syndrome
- **MONDO ID:** MONDO:0044738 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gabriele-de Vries Syndrome** covering all of the
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

# Gabriele-de Vries syndrome: disease-characteristics research report

**Disease:** Gabriele-de Vries syndrome  
**Preferred abbreviation:** GADEVS  
**Molecular basis:** Heterozygous loss of function of **YY1**  
**Inheritance:** Autosomal dominant, usually *de novo*  
**MONDO:** MONDO:0044738  
**Evidence cut-off:** October 18, 2026

> **Evidence caveat:** GADEVS is exceptionally rare. Most clinical frequencies derive from cohorts of approximately 10–37 molecularly diagnosed individuals, sometimes mixing intragenic variants with larger 14q32 deletions. Percentages should therefore be treated as provisional, ascertainment-sensitive estimates rather than population parameters.

---

## 1. Disease information

### Definition and overview

Gabriele-de Vries syndrome is a congenital, multisystem neurodevelopmental disorder caused by heterozygous pathogenic variants in, or deletions involving, **YY1**, a zinc-finger transcription factor and chromatin regulator at 14q32.2. The defining manifestations are developmental delay/intellectual disability, delayed speech, feeding difficulty, characteristic but variable facial dysmorphism, prenatal or postnatal growth disturbance, behavioral abnormalities, hypotonia or movement/gait disorders, and variably penetrant congenital anomalies of the brain, eyes, heart, kidneys, genitalia, skeleton, and craniofacial structures. [31][32]

The foundational 2017 study identified 23 affected individuals—10 with *de novo* intragenic variants and 13 with deletions encompassing **YY1**—and concluded:

> “Our combined clinical and molecular data define ‘YY1 syndrome’ as a haploinsufficiency syndrome.”  
> —Gabriele *et al.*, 2017, PMID: **28575647** [20]

GADEVS is therefore best classified as a **Mendelian autosomal-dominant chromatin/transcriptional-regulation disorder**, sometimes described mechanistically as an **enhanceropathy**.

### Identifiers and terminology

| Resource | Identifier/name |
|---|---|
| MONDO | **MONDO:0044738** |
| OMIM disease | **617557**, Gabriele-de Vries syndrome |
| OMIM gene | **600013**, YY1 |
| Orphanet | **ORPHA:506358** |
| MedGen | **C4479652**, UID 1375401 |
| SNOMED CT | **1186730002**, Gabriele-de Vries syndrome / YY1 haploinsufficiency syndrome |
| ICD-10 | **Q87.8**, other specified congenital malformation syndromes, not elsewhere classified; no dedicated GADEVS code [210] |
| ICD-11 | No clearly established disease-specific code; code according to the dominant congenital-malformation or neurodevelopmental presentation |
| MeSH | No dedicated GADEVS heading identified; literature is indexed under terms such as Intellectual Disability, Developmental Disabilities, and YY1 Transcription Factor |
| UMLS/MedGen concept | **C4479652** |
| Category | Mendelian; genetic neurodevelopmental/multiple-congenital-anomaly syndrome |

Identifiers, synonyms, and the associated locus are consolidated by MedGen, which links MONDO:0044738, OMIM 617557, ORPHA:506358, SNOMED CT 1186730002, and **YY1** at 14q32.2. [31]

**Synonyms**

- Gabriele-de Vries syndrome
- Gabriele de Vries syndrome
- GADEVS
- YY1 haploinsufficiency syndrome
- YY1 syndrome
- YY1-related syndrome

### Evidence granularity

The information in this report is predominantly **aggregated disease-level evidence** derived from published case series, GeneReviews, Orphanet, ClinVar, and mechanistic studies. Original reports use individual clinical records, parental testing, imaging, and molecular laboratory data, but this is not a report generated from a single patient’s EHR.

---

## 2. Etiology

### Causal factors

The primary cause is a **heterozygous germline pathogenic variant in YY1** or a deletion of 14q32.2 that disrupts YY1. Established classes include:

- Nonsense and frameshift variants causing nonsense-mediated decay or truncated protein
- Missense substitutions concentrated in the C-terminal zinc-finger DNA-binding domains
- In-frame deletions affecting zinc-finger structure
- Canonical splice variants
- Partial or whole-gene deletions
- Larger 14q32 deletions that include YY1 and additional genes

The founding study found no disease variants in then-available control databases and experimentally demonstrated reduced YY1 chromatin occupancy for both truncating and zinc-finger missense variants. [34]

### Risk factors

| Factor | Evidence and interpretation |
|---|---|
| Pathogenic YY1 variant | Necessary molecular risk factor in confirmed monogenic GADEVS |
| Parental carrier status | No conventionally inherited familial series is established; parental testing is still essential |
| Parental germline mosaicism | Theoretical recurrence mechanism; no confirmed cases in the older GeneReviews dataset |
| Advanced parental age | No GADEVS-specific association demonstrated |
| Sex | Both sexes are affected; no reliable sex bias established |
| Ethnicity/geography | Cases occur across multiple ancestries; no population enrichment or founder variant established |
| Consanguinity | Not causative for this dominant, typically *de novo* disorder |
| Family history | Usually negative because most variants are *de novo* |
| Environment/lifestyle | No environmental, dietary, infectious, toxic, or occupational cause has been demonstrated |

All tested parents in the early cohorts were negative for the proband’s variant in blood, supporting predominantly *de novo* occurrence. The estimated sibling recurrence risk after negative parental blood testing is approximately **1%**, reflecting possible germline mosaicism. [46]

### Protective factors

No genetic protective allele, diet, medication, lifestyle, vaccination, or environmental exposure has been shown to prevent GADEVS. The incomplete phenotype of some **Yy1**-heterozygous mice suggests genetic-background modifiers probably exist, but no human modifier gene has been validated. In C57BL/6-backcrossed mice, only 7/29 heterozygotes—about 24%—showed developmental retardation or neurulation defects, illustrating background-dependent penetrance in that model. [171]

### Gene–environment interaction

No specific human YY1-by-environment interaction is established. Environmental conditions can influence general developmental outcome—nutrition, access to therapy, educational support, seizure control—but do not appear to initiate the syndrome. The relevant “environment” at the mechanistic level is primarily the developmental cellular environment: mutant neurons can alter neighboring astrocyte inflammatory transcription even when the astrocytes themselves are genetically normal. [1]

---

## 3. Phenotypes

### Core phenotype catalogue

Frequencies below preferentially use intragenic-variant cohorts because large deletions may create contiguous-gene effects. “Rare” usually means one or a few published individuals.

| Phenotype/type | Onset, severity, course, frequency | Functional/QOL impact | Suggested HPO term |
|---|---|---|---|
| Developmental delay | Infancy/early childhood; mild to profound; essentially universal in established cases | Dependence in education, communication and activities of daily living | Global developmental delay **HP:0001263** |
| Intellectual disability | Childhood recognition; usually mild–moderate, occasionally severe/profound; lifelong | Educational, vocational and independent-living limitations | Intellectual disability **HP:0001249** |
| Motor delay | Infancy; 8/10 in the original intragenic cohort; walking 15 months–6.5 years, median approximately 2 years | Reduced mobility; need for PT or assistive devices | Delayed gross motor development **HP:0002194** |
| Speech/language delay | Childhood; at least 5/10 early cases, ranging from mild delay to absent speech | Major effect on education and social participation; AAC may be required | Delayed speech and language development **HP:0000750** |
| Feeding difficulty/dysphagia | Usually neonatal or infancy; common; variable persistence | Poor growth, aspiration risk, caregiver burden; some require gastrostomy | Feeding difficulties **HP:0011968**; dysphagia **HP:0002015** |
| IUGR/low birth weight | Antenatal/neonatal; low birth weight 5/9 in an early cohort | Neonatal feeding/growth surveillance | IUGR **HP:0001511**; low birth weight **HP:0001518** |
| Short stature/poor growth | Childhood; minority; weight may catch up | Endocrine assessment and nutritional support | Short stature **HP:0004322** |
| Hypotonia | Congenital/childhood; approximately half when neurologic manifestations are combined | Delayed motor milestones, feeding and gait difficulty | Muscular hypotonia **HP:0001252** |
| Abnormal gait | Childhood; toe walking, waddling, ataxic or dystonic gait; variable | Falls, mobility restriction, assistive-device need | Gait disturbance **HP:0001288** |
| Dystonia/tremor/myoclonus | Childhood to juvenile onset; uncommon but potentially progressive and severe | Pain, impaired walking, hand use, speech and self-care | Dystonia **HP:0001332**; tremor **HP:0001337**; myoclonus **HP:0001336** |
| Seizures | Rare; febrile and non-febrile cases reported | Injury risk and medication burden | Seizure **HP:0001250** |
| Behavioral/psychiatric features | Childhood onward; 5/9 in the early series | School, family and social-function impact | Abnormal behavior **HP:0000708** |
| Autism/autistic behavior | Childhood; variable | Social-communication and adaptive-function effects | Autism **HP:0000717** |
| ADHD/hyperactivity | Childhood; variable | Attention and educational impairment | ADHD **HP:0007018** |
| Anxiety | Childhood/adolescence/adulthood | Emotional distress and reduced participation | Anxiety **HP:0000739** |
| Sleep disturbance | Childhood onward; 2/9 in early data | Family sleep and daytime functioning | Sleep abnormality **HP:0002360** |
| Facial asymmetry | Congenital; common in original descriptions; generally stable | Usually cosmetic, occasionally linked to craniofacial evaluation | Facial asymmetry **HP:0000324** |
| Broad forehead | Congenital; 10/10 in the original intragenic cohort | Diagnostic clue, little direct functional impact | Broad forehead **HP:0000337** |
| Posteriorly rotated/simple ears | Congenital; common | Usually minimal functional effect | Posteriorly rotated ears **HP:0000358** |
| Full upper eyelids/periorbital fullness | Congenital/childhood; common | Primarily morphologic | Periorbital fullness **HP:0000629** |
| Downslanted palpebral fissures | Congenital; variable | Primarily morphologic | Downslanting palpebral fissures **HP:0000494** |
| Bulbous/full nasal tip | Congenital; common | Primarily morphologic | Bulbous nose **HP:0000414** |
| Thick lower-lip vermilion | Congenital; common | Primarily morphologic | Thick lower lip vermilion **HP:0000179** |
| Micrognathia/Pierre Robin/cleft palate | Congenital; rare | Airway, feeding, speech and surgical burden | Micrognathia **HP:0000347**; cleft palate **HP:0000175** |
| Craniosynostosis | Congenital; uncommon, more frequent in large deletions | Abnormal skull growth; possible neurosurgery | Craniosynostosis **HP:0001363** |
| Strabismus/refractive error | Childhood; eye findings in more than half in early summaries | Visual development and school functioning | Strabismus **HP:0000486**; hypermetropia **HP:0000540** |
| Brain MRI abnormalities | Congenital/childhood; inconsistent | Variable neurologic significance | Abnormal brain MRI **HP:0410263** |
| Cardiac anomaly | Congenital; rare: PFO, Ebstein anomaly, septal or arch lesions | Cardiology follow-up or intervention | Congenital heart defect **HP:0001627** |
| Hydronephrosis/UPJ stenosis | Congenital; hydronephrosis 2/7 and UPJ stenosis 1/7 in early data | UTI/renal-function surveillance | Hydronephrosis **HP:0000126** |
| Cryptorchidism | Congenital; expanded phenotype in the 2022 cohort | Fertility/malignancy risk and surgery | Cryptorchidism **HP:0000028** |
| Joint laxity, patellar luxation, arthrogryposis | Congenital/childhood; individually rare | Mobility and orthopedic burden | Joint hypermobility **HP:0001382**; distal arthrogryposis **HP:0005684** |
| Hypothyroidism/GH deficiency | Childhood; uncommon | Growth, energy and neurodevelopment; treatable | Hypothyroidism **HP:0000821**; GH deficiency **HP:0000824** |
| Thin/sparse hair | Congenital/childhood; newly emphasized in 2022 | Mostly cosmetic | Sparse hair **HP:0008070** |
| Hearing impairment | Uncommon but reported | Communication and education | Hearing impairment **HP:0000365** |
| Recurrent infections | Approximately 1/5 in one patient-oriented summary, but poorly characterized | Illness and health-care burden | Recurrent infections **HP:0002719** |

The original ten-person intragenic cohort documented walking as late as 6.5 years, moderate–severe ID in some individuals, gastrostomy use in three, and heterogeneous MRI abnormalities. [20] The later methylation cohort added **thin/sparse hair and cryptorchidism** to the recognized spectrum. [76] A 2024 clinical review stated that about 90% of compiled patients had motor delay or intellectual disability, although denominator definitions varied. [68]

### Neuroimaging

Reported findings include delayed myelination, cortical dysplasia, frontal gliosis, enlarged subarachnoid spaces or ventricles, white-matter loss or foci, encephalomalacia, and corpus-callosum hypoplasia/agenesis. These findings are neither obligatory nor specific. Some affected individuals have a normal MRI. [46]

### Rare expansion phenotypes

A 2023 newborn report described lumbosacral meningomyelocele, hydrocephalus, Chiari II malformation, syringomyelia, spinal cysts, and tethered cord, but this is a **single association** and not yet an established recurrent YY1 phenotype. The authors called it the first GADEVS case with spinal dysraphism. PMID: **37189872**, published March 26, 2023. [238][243]

### Quality-of-life evidence

No GADEVS-specific EQ-5D, SF-36, PROMIS, or validated natural-history/QOL study was identified. Expected burden derives from intellectual disability, limited speech, feeding support, movement disorder, behavioral symptoms, congenital surgery, and need for lifelong educational and rehabilitative services.

---

## 4. Genetic and molecular information

### Gene and protein

| Attribute | Value |
|---|---|
| Gene | **YY1**, YY1 transcription factor |
| HGNC | **HGNC:12856** |
| NCBI Gene | **7528** |
| Ensembl | **ENSG00000100811** |
| OMIM gene | **600013** |
| UniProt | **P25490** |
| Cytogenetic locus | **14q32.2** |
| GRCh38 coordinates | chr14:100,239,144–100,282,788 |
| MANE transcript | **NM_003403.5** |
| Protein | **NP_003394.1**, 414 amino acids |
| Functional class | Ubiquitous GLI/Krüppel-class zinc-finger transcription factor; transcriptional activator/repressor and chromatin-loop regulator |

These identifiers and the current MANE transcript are provided by NCBI/ENCODE. [92][93]

### Representative disease-associated variants

| Variant, NM_003403.5 | Class | Reported interpretation/effect |
|---|---|---|
| c.385del, p.Asp129Ilefs*127 | Frameshift | Pathogenic; loss of function |
| c.458_476del, p.Val153fs*97 | Frameshift | *De novo*, pathogenic by PVS1_Strong+PS2+PM2; absent from HGMD, dbSNP, ExAC, gnomAD and ClinVar when reported [123] |
| c.535A>T, p.Lys179Ter | Nonsense | NMD; approximately 50% protein in patient cells |
| c.690del, p.Glu231Ilefs*25 | Frameshift | *De novo*, pathogenic; PMID **34729769** [105] |
| c.958C>T, p.His320Tyr | Missense, zinc finger 1 | Pathogenic; impaired zinc coordination/DNA binding |
| c.1015A>C, p.Lys339Gln | Missense, zinc finger 2 | Pathogenic; impaired DNA interaction |
| c.1030C>T, p.Gln344Ter | Nonsense | Loss of zinc fingers 3–4 |
| c.1096C>G, p.Leu366Val | Missense, zinc finger 3 | Pathogenic |
| c.1097T>C, p.Leu366Pro | Missense, zinc finger 3 | Pathogenic |
| c.1138G>T, p.Asp380Tyr | Missense, zinc finger 4 | Pathogenic; predicted destabilization |
| c.1173del, p.Asn391Lysfs*10 | Frameshift | Disrupts zinc finger 4 |
| c.1174_1176del, p.Lys393del | In-frame deletion | Disrupts zinc finger 4 |
| c.1062+1G>A | Canonical splice | ClinVar pathogenic |
| Whole/partial YY1 deletion | Copy-number loss | Haploinsufficiency |
| Larger 14q32.2 deletion | Structural variant | GADEVS plus possible contiguous-gene effects |

ClinVar-linked summaries listed at least 36 disease-associated submissions by 2025, although submission count is not equivalent to independent affected individuals or expert-panel curation. [121]

### Variant origin and frequency

- Established variants are **germline heterozygous**.
- Most confirmed cases are **de novo**.
- Pathogenic truncating and critical zinc-finger variants are generally absent or exceptionally rare in population databases.
- The gene is strongly loss-of-function constrained; one case report cited **pLI 0.99** and observed/expected loss-of-function ratio approximately 0.10. [130]
- Somatic YY1 variants occur in some tumors, notably insulinoma, but do not imply constitutional GADEVS or hereditary tumor predisposition.

### Functional consequence

The dominant established mechanism is **haploinsufficiency**. Truncating alleles reduce dosage; zinc-finger missense alleles can preserve protein quantity while eliminating effective chromatin binding. The 2024/2025 organoid study suggested that at least one variant, p.Cys303Arg, could exert a dominant-negative effect, but that interpretation was inferred from elevated mutant protein and reduced binding and is not yet a general mechanism for all YY1 missense variants. [18]

### Modifier genes and genotype–phenotype relationships

No validated human modifier gene or robust genotype–phenotype correlation exists. Larger deletions may be more severe because of neighboring genes or disruption of the chromosome-14 imprinted region. Missense variants outside the usual zinc-finger region warrant caution and may benefit from episignature or functional testing.

### Epigenetics

A distinctive peripheral-blood DNA-methylation episignature was identified from 13 available DNA samples, supporting functional confirmation and possible reclassification of uncertain variants. PMID: **35027293**, published January 10, 2022 online / April 2022 print. [76]

At the chromatin level, affected lymphoblastoid cells showed reduced YY1 binding, loss of H3K27 acetylation particularly at YY1-bound enhancers, and a relative shift toward repressive H3K27 methylation at some loci. [11]

---

## 5. Environmental information

| Domain | Conclusion |
|---|---|
| Toxins, radiation, pollution | No demonstrated etiologic role |
| Smoking, alcohol, diet, exercise | No evidence that these cause or prevent GADEVS |
| Occupational exposure | Not applicable to congenital causation |
| Infectious agents | No pathogen causes or triggers the syndrome |
| Maternal environment | No specific association established |
| Environmental modification of outcome | General developmental supports, nutrition, safe feeding, treatment of hearing/vision problems and early education can modify functional outcome, not genotype |

No CHEBI disease-causing chemical should currently be assigned.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous truncating/deletion allele or critical zinc-finger missense variant in **YY1** **leads to** reduced effective YY1 dosage or DNA-binding capacity.
2. Reduced functional YY1 **leads to** a global loss of YY1 chromatin occupancy, with preferential retention at high-affinity/high-occupancy sites.
3. Loss of occupancy at promoters and especially enhancers **results in** reduced H3K27 acetylation and altered enhancer–promoter regulation; increased H3K27me3 at some affected sites is consistent with transcriptional repression.
4. Dysregulated chromatin architecture **leads to** cell-type-specific changes in transcriptional networks governing organogenesis, metabolism, protein synthesis, neural-progenitor survival, differentiation and synapse formation.
5. **Neurodevelopmental branch:** altered YY1–NEUROG2–ETV5 regulation in radial glia and intermediate progenitors **leads to** disturbed corticogenesis and abnormal ventricle-like cytoarchitecture.
6. Impaired neural-progenitor biosynthesis/cell-cycle control **results in** G1/S arrest and p53-dependent apoptosis in mouse conditional knockouts; contribution of the same pathway to human heterozygous disease is strongly plausible but partly inferred.
7. Altered excitatory-neuron transcription and synaptic organization **lead to** abnormal neuronal maturation, connectivity and signaling, providing a mechanistic bridge to DD/ID, speech delay, seizures and movement/behavioral phenotypes.
8. **Glial branch:** altered signals from mutant neurons **lead to** non-cell-autonomous activation of adjacent astrocytes and an inflammatory/astrogliosis-like transcriptional response; its importance in living patients remains inferred from co-culture.
9. Dysregulation in neural crest and non-neural embryonic lineages **leads to** variably penetrant craniofacial, ocular, cardiac, renal, genital and skeletal malformations.
10. The combined developmental and network-level abnormalities **result in** the multisystem GADEVS phenotype.

### Direct human cellular evidence

In lymphoblastoid cells from four affected individuals:

- YY1 peaks were markedly reduced.
- Quantitative analysis estimated a 43%–87% global decrease in occupancy, depending on normalization.
- 416 consistently lost peaks were identified.
- There were 152 differentially expressed genes, including enrichment for chromatin-silencing functions.
- About 82% of YY1-bound enhancers showed significantly reduced H3K27ac under one normalization scheme.
- Distally regulated YY1 genes were disproportionately likely to be differentially expressed.
- Data are deposited as **GEO GSE98478**. [11]

The authors’ abstract directly stated:

> “YY1 deletions and missense mutations lead to a global loss of YY1 binding with a preferential retention at high-occupancy sites.” [20]

### 2024 single-cell and organoid research

Pereira *et al.* combined patient-derived iPSCs, cortical organoids, NGN2-induced neurons, neuron–astrocyte co-culture, single-cell RNA/ATAC multiomics, imaging, and regulatory-network reconstruction. PMID: **38405909**, online publication February 17, 2024. [18][260]

Key findings included:

- Three patient lines: p.Lys179Ter, p.Asp129Ilefs*127, and p.Cys303Arg.
- Reduced YY1 binding in all affected lines.
- 764 iPSC DEGs at the reported threshold, 585 downregulated.
- Day-30 organoids: **31,214 cells**; strong disruption in radial glia, intermediate progenitors and maturing excitatory neurons.
- Day-90 organoids: **32,677 cells**; broad dysregulation and an increased upper-layer-neuron cluster.
- GADEVS organoids developed irregular PAX6-positive ventricle-like structures.
- NGN2 cultures contained **14,828 cells**; glutamatergic neurons were the most dysregulated.
- Astrocytes exposed to GADEVS neurons had **291 DEGs**—248 upregulated and 43 downregulated—with immune/cell-activation enrichment.
- Regulatory reconstruction implicated YY1, NEUROG2, ETV5, MYC, MXI1, EBF3 and related networks.

The abstract concluded:

> “YY1 haploinsufficiency causes a pervasive alteration of cell type specific transcriptional networks, disrupting corticogenesis at the level of neural progenitors and terminally differentiated neurons.” [18]

### Molecular pathways and processes

| Mechanism | Evidence status | Suggested GO terms |
|---|---|---|
| DNA-dependent transcriptional activation/repression | Directly established | DNA-templated transcription **GO:0006351**; regulation of transcription **GO:0006355** |
| Enhancer–promoter looping/chromatin organization | Established YY1 biology; disease-linked occupancy effects demonstrated | Chromatin organization **GO:0006325**; chromosome organization **GO:0051276** |
| Histone H3K27 acetylation loss | Directly demonstrated in patient cells | Histone acetylation **GO:0016573** |
| Neural-progenitor proliferation/survival | Strong mouse-model evidence; supported by organoid transcription | Neural precursor cell proliferation **GO:0061351**; regulation of cell cycle **GO:0051726** |
| p53-dependent apoptosis | Direct in conditional mouse knockout; inferred contribution to GADEVS | Intrinsic apoptotic signaling by p53 **GO:0072332** |
| Corticogenesis/neurogenesis | Directly disrupted in patient-derived organoids | Neurogenesis **GO:0022008**; cerebral cortex development **GO:0021987** |
| Synapse assembly/signaling | Transcriptomic and imaging evidence | Synapse organization **GO:0050808**; trans-synaptic signaling **GO:0099537** |
| MAPK/EGFR signaling | Enriched in late radial-glial communication analyses; subtle and computationally inferred | MAPK cascade **GO:0000165**; EGFR signaling **GO:0007173** |
| Astrocyte activation/inflammation | Direct co-culture transcriptomics, but in-vitro significance | Astrocyte activation **GO:0048143**; inflammatory response **GO:0006954** |
| Protein synthesis/metabolism | Mouse cortical knockout evidence | Translation **GO:0006412**; cellular metabolic process **GO:0044237** |
| Oligodendrocyte differentiation/myelination | Established YY1 biology; possible relevance to delayed myelination | Oligodendrocyte differentiation **GO:0048709**; myelination **GO:0042552** |

### Relevant cell types

| Cell type | Role | Suggested CL term |
|---|---|---|
| Neural stem/progenitor cell | Proliferation and survival are dosage-sensitive | Neural stem cell **CL:0000047** |
| Radial glial cell | Disrupted developmental transcription and intercellular signaling | Radial glial cell **CL:0000681** |
| Intermediate neuronal progenitor | Altered indirect neurogenesis | Neural progenitor cell **CL:0011020** |
| Excitatory/glutamatergic neuron | Strong synaptic and transcriptional disturbance | Glutamatergic neuron **CL:0000679** |
| Cortical neuron | Principal affected differentiated lineage | Cerebral cortex neuron **CL:0002609** |
| Astrocyte | Non-cell-autonomous inflammatory activation | Astrocyte **CL:0000127** |
| Neural crest cell | Plausible source of craniofacial and peripheral anomalies | Neural crest cell **CL:0000333** |
| Oligodendrocyte progenitor | YY1-dependent differentiation/myelination | Oligodendrocyte precursor cell **CL:0002453** |
| Lymphoblastoid cell | Experimental chromatin/transcriptomic model, not principal diseased tissue | B lymphoblast **CL:0000905** |

### Omics and advanced technologies

- **Bulk RNA-seq/ChIP-seq:** Patient lymphoblastoid cells and iPSCs.
- **Single-cell multiome:** Simultaneous RNA expression and chromatin accessibility in cortical organoids.
- **3D models:** Patient-derived cortical organoids.
- **Cell–cell communication analysis:** LIANA/tensor-cell2cell and neuron–astrocyte transwell co-culture.
- **Regulatory-network inference:** CellOracle, Cicero, PROGENy, VIPER and DoRothEA.
- **Proteomics/metabolomics/lipidomics:** No replicated GADEVS-specific clinical signature identified.
- **Spatial transcriptomics:** No published disease-specific study identified.
- **CRISPR screens:** No GADEVS-focused therapeutic screen identified.

---

## 7. Anatomical structures affected

| Level/system | Structures and manifestations | Suggested ontology |
|---|---|---|
| Central nervous system | Cerebral cortex, white matter, corpus callosum, ventricles; occasionally spinal cord | Brain **UBERON:0000955**; cerebral cortex **UBERON:0000956**; white matter **UBERON:0002316** |
| Craniofacial | Forehead, jaws, palate, cranial sutures, ears, lips | Face **UBERON:0001456**; palate **UBERON:0007375** |
| Eyes/visual system | Ocular alignment and refraction; rare micro/nanophthalmos | Eye **UBERON:0000970** |
| Cardiovascular | Atrial septum, tricuspid valve, aortic arch/collaterals | Heart **UBERON:0000948** |
| Renal/urinary | Kidneys, renal pelvis and ureteropelvic junction | Kidney **UBERON:0002113** |
| Genital | Testes/scrotum/penis; cryptorchidism or micropenis | Testis **UBERON:0000473** |
| Skeletal/joints | Skull, hands/feet, patellae and limb joints | Skeleton **UBERON:0001434** |
| Gastrointestinal/oropharyngeal | Oral–pharyngeal swallowing apparatus, esophagus; reflux/constipation | Esophagus **UBERON:0001043** |
| Endocrine | Thyroid and pituitary growth axis | Thyroid gland **UBERON:0002046** |
| Subcellular | Nucleus and chromatin; enhancer/promoter complexes | Nucleus **GO:0005634**; chromatin **GO:0000785** |
| Protein compartment | Nuclear transcriptional/chromatin-regulatory complexes | Transcription regulator complex **GO:0005667** |

Facial asymmetry can be lateralized, but no consistent right/left predilection is known. Most neurologic and systemic involvement is bilateral or diffuse.

---

## 8. Temporal development

- **Biologic onset:** Prenatal, because YY1 dosage affects embryogenesis, growth and organogenesis.
- **Clinical onset:** Antenatal IUGR or congenital anomaly; neonatal feeding/hypotonia; developmental and speech delays become apparent during infancy or early childhood. Orphanet classifies onset as antenatal/neonatal. [32]
- **Pattern:** Chronic and lifelong, not episodic or relapsing.
- **Development:** Children generally acquire skills, but at a delayed rate. Developmental disability itself is usually stable rather than neurodegenerative.
- **Potentially progressive components:** Dystonia and related gait/movement disorders can progress substantially in a minority.
- **No formal stages:** There is no accepted early/intermediate/advanced staging system.
- **Remission:** No spontaneous molecular remission; individual feeding or growth problems may improve, while therapies can improve function.
- **Critical period:** Prenatal corticogenesis is the primary biological vulnerability; infancy and preschool years are the practical window for early PT/OT/speech/feeding and communication intervention.

Adult natural-history data remain sparse. Newer adult analyses suggest that thyroid abnormalities, motor impairment, hearing loss and anxiety may be especially relevant in adulthood, but denominators are very small. [227]

---

## 9. Inheritance and population

### Genetic inheritance

| Characteristic | Current conclusion |
|---|---|
| Mode | Autosomal dominant |
| Typical origin | *De novo* |
| Penetrance | Not formally quantified; DD/ID appears highly penetrant among clinically ascertained pathogenic-variant carriers |
| Expressivity | Markedly variable |
| Anticipation | Not reported; no repeat-expansion mechanism |
| Germline mosaicism | Theoretical; not conclusively documented in early reports |
| Sibling recurrence | Approximately 1% after negative parental blood testing |
| Offspring risk | Theoretical 50% for a heterozygous affected individual, although reproduction has been rarely documented |
| Founder effect | None known |
| Carrier frequency | Not meaningful for a usually *de novo* dominant disorder |
| Consanguinity | No causal role |

### Epidemiology

True prevalence and incidence are unknown. GeneReviews cited detection of *de novo* pathogenic YY1 variants in approximately **0.03%–1% of selected cohorts with unexplained intellectual disability**, not in the general population. [66]

The 2017 discovery cohort found ten intragenic variants among **14,969** individuals with intellectual disability—approximately 0.067%—but the constituent cohorts used different ascertainment and sequencing approaches. [20]

By 2024, a patient-community summary stated that at least **37 molecularly recognized individuals** had been identified clinically. [23] This is not a prevalence estimate and likely undercounts unpublished diagnoses.

No credible annual incidence, male:female ratio, ethnicity-specific prevalence, endemic region, geographic gradient, or founder variant has been established.

---

## 10. Diagnostics

### Diagnostic standard

There are no sufficient clinical criteria. Diagnosis requires:

1. A heterozygous pathogenic or likely pathogenic **YY1** sequence variant; or
2. A heterozygous deletion disrupting **YY1**, interpreted in the context of whether neighboring genes are also deleted.

GeneReviews specifically notes that the phenotype is not sufficiently specific for diagnosis without molecular confirmation. [46]

### Recommended testing strategy

| Test | Utility |
|---|---|
| Chromosomal microarray | Detects whole-gene/larger 14q32 copy-number losses; should define neighboring genes and the imprinted region |
| Neurodevelopmental multigene panel | Appropriate if it includes YY1 and sequence plus deletion/duplication analysis |
| Trio whole-exome sequencing | High utility because the phenotype is nonspecific and most variants are *de novo* |
| Trio whole-genome sequencing | Useful for coding variants, splice/regulatory variants and better structural-variant breakpoint resolution |
| YY1 single-gene sequencing | Reasonable only when phenotype/known family variant is strongly suggestive; not usually first-line |
| Sanger sequencing | Confirmation and parental segregation testing |
| Gene-targeted del/dup testing | Can detect exon-level events but is less informative than genome-wide CNV testing for larger deletions |
| DNA methylation episignature | Functional adjunct for VUS or atypical variants; not a replacement for sequence/CNV testing |
| RNA sequencing | Research/selected splice-VUS clarification; not routine |
| Karyotype/FISH | Low yield for intragenic variants; may characterize large cytogenetic rearrangements |
| mtDNA/repeat-expansion testing | Not indicated specifically for GADEVS |
| Liquid biopsy | Not applicable |

The 2024 case report used WES followed by Sanger confirmation to identify **c.458_476del, p.Val153fs*97**. [16] GTR listed four available clinical testing entries in the retrieved version, although laboratory availability changes over time. [55]

### Baseline evaluation after molecular diagnosis

- Growth parameters, nutrition and feeding/swallow safety
- Comprehensive developmental, speech/language and adaptive assessment
- Neurologic examination; EEG only for suspected seizures
- Brain MRI for abnormal head growth, seizures, regression, focal signs or substantial movement disorder
- Behavioral/autism/ADHD/anxiety and sleep screening
- Ophthalmology and hearing assessment
- Echocardiography
- Renal ultrasound
- Examination for cryptorchidism and other genital anomalies
- Craniofacial assessment for cleft palate, micrognathia, craniosynostosis or abnormal skull shape
- Musculoskeletal examination
- Thyroid function and growth/endocrine evaluation where indicated

These recommendations closely follow the GeneReviews multidisciplinary evaluation table. [46]

### Laboratory biomarkers

No routine serum enzyme, metabolite, protein, immune or endocrine biomarker diagnoses GADEVS. Thyroid studies, growth-axis testing and nutritional laboratories are problem-directed. The only disease-linked molecular biomarkers are:

- Pathogenic/likely pathogenic **YY1** genotype
- 14q32 deletion
- Peripheral-blood DNA-methylation episignature

### Differential diagnosis

The differential is broad because GADEVS lacks a pathognomonic clinical sign:

- Other chromatinopathies/enhanceropathies
- KANSL1-related Koolen-de Vries syndrome
- Wiedemann-Steiner, Coffin-Siris, Kabuki and Cornelia de Lange syndromes
- White-Sutton syndrome, CDK13-related disorder, ADNP-related disorder and SETD5-related NDD
- Imprinting disorders involving chromosome 14, particularly in large deletions
- Monogenic movement disorders when dystonia/myoclonus dominates
- Syndromic craniosynostosis or Pierre Robin sequence when craniofacial findings dominate

Distinguishing GADEVS ultimately depends on YY1 testing and, when uncertain, segregation and functional/episignature evidence.

### Screening

- Not included in routine newborn biochemical screening.
- Population carrier screening is not appropriate.
- Cascade testing is limited because most cases are *de novo*.
- Test both parents to establish inheritance and assess recurrence.
- Prenatal or preimplantation testing is possible once the familial/proband variant is known.

---

## 11. Outcome and prognosis

### Survival

No 5-year/10-year survival rate, standardized mortality rate, disease-specific mortality estimate, or reliable life-expectancy calculation exists. Published individuals have survived into adulthood, including people assessed in their third and fourth decades. There is no current evidence that uncomplicated GADEVS is inevitably life-limiting.

### Morbidity and function

The principal long-term burdens are:

- Lifelong cognitive and adaptive disability
- Speech/communication impairment
- Feeding and gastrointestinal problems
- Motor delay, hypotonia and gait impairment
- Behavioral or psychiatric morbidity
- Visual/hearing impairment
- Progressive dystonia in a subset
- Complications of individual congenital anomalies

Recovery from the underlying genetic condition is not expected. Nevertheless, acquisition of skills, improved communication, safer feeding, mobility gains, behavioral stabilization and correction of structural anomalies are realistic treatment goals.

### Prognostic indicators

No validated biomarker or prediction model exists. Likely practical indicators include:

- Baseline developmental severity
- Presence of severe feeding/aspiration difficulty
- Major congenital brain or cardiac anomaly
- Severe/progressive movement disorder
- Hearing/vision impairment
- Access to early developmental intervention
- Size and gene content of a 14q32 deletion

There is no established variant-specific prognosis.

---

## 12. Treatment

### General principle

There is **no approved disease-modifying therapy** for YY1 haploinsufficiency. Care is individualized and multidisciplinary. The 2024 review stated that symptomatic treatment and comprehensive rehabilitation may improve quality of life. [54]

| Manifestation/intervention | Approach and evidence | Suggested NCIT term |
|---|---|---|
| Developmental delay/ID | Early intervention, individualized education, developmental pediatrics | Developmental Therapy; Early Intervention |
| Gross-motor delay/hypotonia | Physical therapy, orthotics, walkers or wheelchairs as required | Physical Therapy **NCIT:C15309** |
| Fine-motor/adaptive limitation | Occupational therapy | Occupational Therapy **NCIT:C15310** |
| Speech/language impairment | Speech-language therapy; AAC evaluation for limited speech | Speech Therapy **NCIT:C15308** |
| Feeding dysfunction | Feeding therapy, dietitian input, swallow assessment, texture modification | Nutritional Support **NCIT:C15440** |
| Persistent unsafe/inadequate feeding | Gastrostomy where necessary | Gastrostomy **NCIT:C52004** |
| GERD/constipation | Standard pediatric/adult therapy | Supportive Care |
| Seizures | Standard antiseizure medication selected by seizure type; no GADEVS-specific agent | Anticonvulsant Therapy |
| ADHD/anxiety/autism-related behavior | Behavioral intervention; standard psychotropic treatment when appropriate | Behavioral Therapy **NCIT:C15185** |
| Dystonia | PT, standard dystonia medications, botulinum toxin for focal symptoms; specialist movement-disorder care | Botulinum Toxin Therapy |
| Severe refractory generalized dystonia | Consider bilateral GPi deep-brain stimulation in highly selected cases | Deep Brain Stimulation **NCIT:C116507** |
| Strabismus/refractive error | Glasses, patching or surgery as indicated | Ophthalmic Procedure |
| Hearing impairment | Audiology, amplification/communication support | Hearing Aid Device |
| Cleft palate/craniosynostosis | Multidisciplinary craniofacial surgery | Surgical Procedure **NCIT:C15329** |
| Cardiac/renal anomalies | Lesion-specific cardiology, nephrology or urology care | Supportive/Corrective Surgery |
| Cryptorchidism | Standard orchiopexy timing | Orchiopexy |
| Hypothyroidism/GH deficiency | Standard endocrine replacement after confirmation | Thyroid Hormone Replacement; Growth Hormone Therapy |

GeneReviews recommends PT, OT, speech and feeding therapies from infancy, individualized education, augmentative communication, standard management of seizures and congenital anomalies, and gastrostomy when persistent feeding difficulty warrants it. [46]

### Deep-brain stimulation evidence

Evidence is limited to case reports. A 2021 report described long-term response of YY1-related dystonia to DBS, PMID **33638881**. [183] A later case documented a 35-year-old man whose Burke-Fahn-Marsden motor score improved from **100 to 50 at six months** and to **46 at four years** after bilateral GPi-DBS; disability score improved from 20 to 14. This supports consideration for medication-refractory severe dystonia, not routine GADEVS treatment. [181]

### Experimental therapies

No validated gene replacement, CRISPR editing, RNA therapy, cell therapy, targeted anti-inflammatory therapy, or syndrome-specific pharmacotherapy is available. The organoid/co-culture work raises hypotheses involving inflammatory modulation and astrocyte–neuron signaling, but the investigators explicitly note that preclinical validation is required. [1]

No clearly verified GADEVS-specific interventional ClinicalTrials.gov study or treatment-response trial was identified. Generic natural-history or sequencing studies should not be represented as therapeutic trials.

### Pharmacogenomics

No YY1-specific CPIC/PharmGKB prescribing guideline or reproducible genotype-dependent drug response is known.

---

## 13. Prevention

### Primary prevention

Because most cases arise from a *de novo* germline event, lifestyle change, vaccination, diet or exposure avoidance cannot prevent occurrence.

### Secondary prevention and early detection

- Prompt genomic testing in children with unexplained DD/ID plus feeding difficulty, growth restriction, dysmorphism or congenital anomalies
- Parental testing after diagnosis
- Prenatal diagnosis by chorionic-villus sampling or amniocentesis when a familial/proband variant is known
- Preimplantation genetic testing for monogenic disease
- Early developmental, feeding, hearing, vision, renal and cardiac assessment

### Tertiary prevention

- Swallow-safety intervention to reduce aspiration/malnutrition
- Seizure recognition and treatment
- Early PT/OT/speech/AAC to reduce secondary functional limitation
- Growth and thyroid monitoring
- Behavioral and sleep surveillance
- Prompt treatment of visual, auditory, cardiac, renal, orthopedic and movement complications

### Genetic counseling

After a confirmed *de novo* variant absent from both parents’ blood, counsel an approximate **1% sibling recurrence risk** because of possible germline mosaicism. If a parent is found to carry the variant, each pregnancy has a 50% transmission risk, with unpredictable severity. Prenatal and preimplantation testing are technically feasible once the causal variant is known. [46]

Vaccines, antimicrobial prophylaxis and public-health/environmental control measures are not disease-specific; routine age-appropriate immunization remains appropriate.

---

## 14. Other species and natural disease

No naturally occurring veterinary syndrome clearly homologous to human GADEVS and no breed-specific OMIA entry were identified. There is no infectious transmission, zoonotic potential or cross-species contagion.

### Orthologs

| Species | Taxon ID | Ortholog/resource | Relevance |
|---|---:|---|---|
| Human, *Homo sapiens* | 9606 | YY1; NCBI Gene 7528 | Disease gene |
| Mouse, *Mus musculus* | 10090 | **Yy1**; NCBI Gene 22632; MGI:99150 | Principal developmental model |
| Rat, *Rattus norvegicus* | 10116 | **Yy1**; NCBI Gene 24919 | Conserved ortholog; no natural GADEVS model |
| Zebrafish, *Danio rerio* | 7955 | **yy1b**, NCBI Gene 406394; a second paralog also exists | Developmental knockdown model [162] |
| Dog, *Canis lupus familiaris* | 9615 | **YY1**, NCBI Gene 611171 | Conserved ortholog; no established natural disease |
| Cat, *Felis catus* | 9685 | **YY1**, NCBI Gene 101080802 | Conserved ortholog; no established natural disease |
| Fruit fly, *Drosophila melanogaster* | 7227 | **pho/pleiohomeotic**, with phol as a related homolog | Polycomb recruitment/comparative chromatin biology |

Mammalian YY1 can partially rescue loss of *Drosophila pho*, demonstrating evolutionary conservation of parts of its Polycomb-related function, although mammalian and fly genomic targeting are not identical. [151][163]

---

## 15. Model organisms and experimental models

| Model | Manipulation | Phenotype/mechanistic contribution | Limitations/resource |
|---|---|---|---|
| Germline Yy1-null mouse | Homozygous targeted disruption | Peri-implantation lethality; establishes essential embryonic role | Too severe to model heterozygous human disease; PMID **10490658** [168] |
| Yy1+/− mouse | Heterozygous disruption | Incomplete growth retardation, exencephaly, pseudoventricles and brain asymmetry; approximately 24% affected in one backcross | Variable penetrance; not a complete behavioral model; MGI:99150 [153][171] |
| Dorsal-cortex conditional mouse | Emx1-Cre Yy1 deletion | Reduced forebrain/cortical thickness, G1/S arrest and p53-dependent progenitor apoptosis | Biallelic tissue-specific loss exceeds human haploinsufficiency [172] |
| Mid-hindbrain conditional mouse | Region-specific deletion | Reduced proliferation, p53 accumulation, apoptosis and cerebellar agenesis | Models severe regional loss, not systemic heterozygosity [177] |
| Neural-crest conditional mouse | Premigratory neural-crest deletion | Embryonic death with midbrain and craniofacial defects | Useful for craniofacial mechanism; severe knockout [165] |
| Oligodendrocyte-lineage models | Conditional Yy1 loss | Impaired oligodendrocyte differentiation/myelination program | Relevance to GADEVS white-matter findings remains indirect |
| Zebrafish yy1a/yy1 knockdown | Morpholino/experimental knockdown | Abnormal brain and heart development, linked in one study to phosphatidylserine-receptor regulation | Knockdown artifacts and paralog redundancy; not variant-specific [175] |
| Patient lymphoblastoid cells | Endogenous pathogenic variants/deletion | Reduced YY1 binding, altered H3K27ac/H3K27me3 and transcription; GEO **GSE98478** | Blood-derived transformed cells do not model corticogenesis |
| Patient-derived iPSCs | Reprogrammed cells carrying YY1 variants | Dosage, occupancy and pluripotent-stage transcription studies | Reprogramming and line-to-line variability |
| Neural crest stem cells | Differentiated patient iPSCs | Differentiation failure and apoptotic blebbing | In-vitro approximation |
| Cortical organoids | Patient-derived 3D organoids | Irregular ventricle-like structures and cell-type-specific corticogenesis defects | No vasculature, microglial completeness or whole-body physiology |
| NGN2-induced cortical neurons | Patient iPSC-derived excitatory neurons | Synaptic transcriptomic disturbance and increased synaptic puncta | Forced differentiation may bypass developmental stages |
| Neuron–astrocyte co-culture | Patient neurons plus normal mouse astrocytes | Non-cell-autonomous inflammatory/astrogliosis-like astrocyte response | Cross-species, in-vitro system |

The 2024 organoid study is currently the most disease-proximal experimental platform because it uses endogenous patient variants and resolves affected radial-glial, progenitor, neuronal and astrocytic programs at single-cell level. However, its regulatory networks and dominant-negative interpretation are partly computational or inferential and require in-vivo validation. [18]

---

## Selected primary literature and current authoritative resources

| Publication/resource | Publication date | Key contribution | URL/identifier |
|---|---:|---|---|
| Gabriele M, *et al.* “YY1 Haploinsufficiency Causes an Intellectual Disability Syndrome Featuring Transcriptional and Chromatin Dysfunction” | June 1, 2017 | Foundational 23-person cohort; haploinsufficiency, YY1 ChIP-seq, H3K27ac and transcriptomics | PMID **28575647**; DOI [10.1016/j.ajhg.2017.05.006](https://doi.org/10.1016/j.ajhg.2017.05.006) [20] |
| Khamirani HJ, *et al.* “Clinical features of patients with Yin Yang 1 deficiency…” | January 2022; online November 3, 2021 | Iranian case and 13-case literature review; c.690del | PMID **34729769**; DOI [10.1111/ahg.12448](https://doi.org/10.1111/ahg.12448) [105] |
| Cherik F, *et al.* “DNA methylation episignature in Gabriele-de Vries syndrome” | April 2022; online January 10, 2022 | 13-person methylation analysis; blood episignature; expanded phenotype | PMID **35027293**; DOI [10.1016/j.gim.2021.12.003](https://doi.org/10.1016/j.gim.2021.12.003) [76] |
| dos Santos SR, *et al.* “A de novo YY1 missense variant…” | October 2022; online July 13, 2022 | Phenotypic expansion and altered X-chromosome inactivation | PMID **35829845**; DOI [10.1007/s11011-022-01024-2](https://doi.org/10.1007/s11011-022-01024-2) [43] |
| Koruga N, *et al.* “First Reported Case…with Spinal Dysraphism” | March 26, 2023 | Single-case expansion: meningomyelocele, hydrocephalus and Chiari II | PMID **37189872**; DOI [10.3390/children10040623](https://doi.org/10.3390/children10040623) [238] |
| Yang J, *et al.* “Clinical analysis of Gabriele-de Vries caused by YY1 mutations…” | January 2024; online September 1, 2023 | Novel c.458_476del frameshift and review of 28 reported patients | PMID **37658636**; DOI [10.1002/mgg3.2281](https://doi.org/10.1002/mgg3.2281) [16] |
| Pereira MF, *et al.* “YY1 mutations disrupt corticogenesis…” | Online February 17, 2024; journal version 2025 | Patient iPSCs, cortical organoids, single-cell multiomics and neuron–astrocyte signaling | PMID **38405909**; DOI [10.1038/s41380-025-02929-x](https://doi.org/10.1038/s41380-025-02929-x) [18] |
| GeneReviews: “Gabriele-de Vries Syndrome” | Initial posting May 30, 2019 | Diagnostic strategy, genetic counseling, evaluations, management and surveillance | [https://europepmc.org/books/n/gene/gabriele-devries/](https://europepmc.org/books/n/gene/gabriele-devries/) [46] |
| Orphanet GADEVS | Current database entry | ORPHA identifier, concise definition, inheritance and onset | [https://www.orpha.net/en/disease/detail/506358](https://www.orpha.net/en/disease/detail/506358) [32] |

### Overall interpretation

The strongest current model is that GADEVS is a **YY1 dosage-dependent developmental enhanceropathy**. Reduced effective YY1 binding destabilizes enhancer activation and cell-type-specific transcriptional networks during organogenesis, with the cerebral cortex—particularly radial glia, intermediate progenitors, excitatory neurons and their interaction with astrocytes—showing marked vulnerability. Clinical care remains supportive and surveillance-based; molecular diagnosis, early developmental intervention, feeding safety, and individualized management of movement, behavioral, sensory and congenital abnormalities are presently the most actionable measures.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 99 |
| Resolved | 93 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0044738` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Gabriele de Vries syndrome**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016573` (obsolete histone acetylation) (1 mention)
- `GO:0044237` (obsolete cellular metabolic process) (1 mention) - replaced by `GO:0008152`
- `CL:0002609` (obsolete neuron of cerebral cortex) (1 mention) - replaced by `CL:0010012`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.