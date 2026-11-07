---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-23T15:02:15.239040'
end_time: '2026-10-23T15:06:04.527797'
duration_seconds: 229.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cocoon Syndrome
  mondo_id: MONDO:0013334
  category: Mendelian
  causal_genes: CHUK
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
citation_count: 56
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMC:PMC7275878
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 70
  verified: 63
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0013334
    reported_labels:
    - MONDO
    ontology_label: cocoon syndrome
  - term_id: DOID:0060647
    reported_labels:
    - Disease Ontology
    ontology_label: fetal encasement syndrome
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
- **Disease Name:** Cocoon Syndrome
- **MONDO ID:** MONDO:0013334 (if available)
- **Causal gene(s):** CHUK
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

Please provide a comprehensive research report on **Cocoon Syndrome** covering all of the
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

# Cocoon syndrome / fetal encasement syndrome  
**Disease-knowledge report; evidence reviewed through 23 October 2026**

## Executive summary

**Cocoon syndrome is an autosomal-recessive, usually embryo/fetal-lethal developmental disorder caused by biallelic loss-of-function variants in *CHUK***, which encodes inhibitor of nuclear factor-κB kinase subunit-α (IKKα). The defining molecularly confirmed cases were two female fetuses homozygous for *CHUK* **NM_001278:c.1264C>T, p.(Gln422Ter)**, with absent detectable IKKα protein, severe craniofacial malformation, omphalocele, immobile hypoplastic limbs bound to the trunk, and thin membrane-like skin encasing the limbs. The correct identifiers are **MONDO:0013334, OMIM:613630 and ORPHA:465824**; thus, contrary to the supplied “OMIM not recorded” field, an OMIM phenotype entry is available. [28][102][106]

The direct human evidence remains exceptionally small: **two genotyped fetuses from one Finnish family**. A phenotypically similar 1987 “cocoon fetus” was not molecularly tested. Orphanet consequently lists only two published molecularly established cases, and no incidence or population prevalence can be calculated reliably. [52][104]

The principal primary report concluded:

> “We report an autosomal recessive lethal syndrome characterized by multiple fetal malformations, the most obvious anomalies being the defective face and seemingly absent limbs, which are bound to the trunk and encased under the skin.”  
> — Lahtela et al., *New England Journal of Medicine*, 21 October 2010; PMID **20961246**. [58]

---

## Evidence interpretation

| Evidence type | Evidence available | Main limitation |
|---|---|---|
| Human clinical/genetic | Two molecularly confirmed affected fetuses in one family; segregation in both parents | No independent molecularly confirmed classic Cocoon family and no untreated longitudinal course |
| Human functional | Fetal fibroblast RNA, immunoprecipitation/Western blot and expression-array studies | Small number of fetal samples; some expression findings were exploratory |
| Model organism | Three independent *Chuk* null mouse lines with closely matching skin, limb, craniofacial and abdominal-wall phenotypes | Mice survive to birth and have less severe craniofacial disease than the human fetuses |
| In vitro/cellular | Keratinocyte, fibroblast and pathway studies of IKKα; rescue experiments in hypomorphic human disease | Many findings address general IKKα biology rather than the p.Gln422Ter Cocoon genotype specifically |
| Computational/curated | MONDO, OMIM, Orphanet, GenCC, MGI, MedGen | Frequency estimates inherit the two-case ascertainment limitation |

---

# 1. Disease information

## 1.1 Definition

Cocoon syndrome—preferably also called **fetal encasement syndrome**—is a severe developmental ectodermal/morphogenetic disorder. Its characteristic appearance results from abnormal epidermal development: the limbs are hypoplastic and immobile, bound to the trunk, and covered by transparent membrane-like skin. Severe abnormalities of the face, eyes, mouth/palate, skull, abdominal wall, muscle and skeleton accompany the cutaneous phenotype; cardiac, renal, diaphragmatic and lung-lobulation defects can occur. [102][207]

It must not be confused with **abdominal cocoon syndrome**, an unrelated acquired or idiopathic encapsulating peritoneal disorder.

## 1.2 Identifiers and nomenclature

| Resource | Identifier or term | Status/comment |
|---|---|---|
| MONDO | **MONDO:0013334** | Cocoon syndrome |
| OMIM phenotype | **613630** | “Cocoon syndrome”; mapping to *CHUK*; OMIM currently prefixes the name with “?” because the classic association is based on one family |
| OMIM gene | **600664** | *CHUK* |
| Orphanet | **ORPHA:465824** | Preferred term: fetal encasement syndrome |
| Disease Ontology | **DOID:0060647** | Fetal encasement syndrome |
| MedGen | **C3150891**, UID 462241 | Cocoon syndrome |
| SNOMED CT | **1220575002** | Cocoon syndrome / fetal encasement syndrome |
| ICD-10/ICD-10-CM | No dedicated disease-specific code found | If coding is required, a nonspecific congenital-malformation code would depend on the local coding system and documented manifestations |
| ICD-11 | No dedicated Cocoon/fetal-encasement entity found | Phenotype-specific congenital-malformation coding may be necessary |
| MeSH | No dedicated disease descriptor identified | A supplementary concept exists for human CHUK protein, not for the syndrome itself |
| Gene | **CHUK**, HGNC:**1974**, NCBI Gene:**1147**, Ensembl:**ENSG00000213341** |
| Protein | IKKα, UniProt:**O15111** | 745-aa serine/threonine kinase |

OMIM explicitly maps phenotype 613630 to *CHUK* at 10q24.31 with autosomal-recessive inheritance, while Orphanet and MedGen use fetal encasement syndrome as the descriptive name. [1][14][87][102][302]

## 1.3 Synonyms

| Preferred or alternative name | Comment |
|---|---|
| Cocoon syndrome | Name proposed by Lahtela et al. because membrane-like skin encased the fetus |
| Fetal encasement syndrome | Preferred Orphanet/descriptive term |
| Foetal encasement syndrome | British spelling |
| Cocoon fetus | Historical descriptive term; the 1987 fetus was not molecularly confirmed |
| Severe fetal encasement malformation | Descriptive wording in the primary report |

“Bartsocas–Papas syndrome type 2” is an allelic *CHUK* disorder and may represent a less severe part of a CHUK-related phenotypic continuum, but it should not automatically be substituted for classic, complete-null Cocoon syndrome. ClinGen has elected to lump the conditions for gene-validity assessment, whereas phenotype databases retain separate entries. [35][89][146]

## 1.4 Provenance

This entry is **not derived from an EHR cohort**. It is an aggregated disease-level synthesis whose foundational patient evidence is the 2010 study of one Finnish family with five pregnancies, including two affected fetuses. OMIM, Orphanet, MONDO/MedGen and GenCC curate that primary report. [28][106][326]

---

# 2. Etiology

## 2.1 Primary causal factor

The established cause is **biallelic germline loss of CHUK/IKKα function**. In the defining family, both fetuses were homozygous for a nonsense variant and both unaffected parents were heterozygous carriers. Fetal CHUK RNA was approximately **12% of control**, and no IKKα protein was detected by an N-terminal antibody, supporting nonsense-mediated RNA decay and/or instability of the truncated protein. [296][331]

## 2.2 Risk and protective factors

| Factor category | Finding |
|---|---|
| Causal genetic risk | Homozygosity or compound heterozygosity for sufficiently severe loss-of-function *CHUK* alleles |
| Family history | Previous similarly malformed fetus, recurrent early miscarriage, or known parental carrier status increases prior probability |
| Consanguinity/remote relatedness | The Finnish parents shared an ancestor traced to the 18th century; this supports identity by descent but not a general requirement for consanguinity |
| Sex | Both confirmed fetuses were 46,XX, but two cases cannot establish female susceptibility |
| Age | No maternal- or paternal-age effect reported |
| Environmental/toxic/infectious factors | None established |
| Lifestyle factors | None established |
| Modifier genes | None demonstrated for classic Cocoon syndrome |
| Genetic protective alleles | None identified |
| Environmental protective factors | None identified |
| Gene–environment interaction | No evidence specific to this disorder |

The two normal later births in the family are compatible with Mendelian segregation, not with a protective exposure. No GWAS, susceptibility locus or polygenic-risk data are applicable.

---

# 3. Phenotypes

All frequency estimates below refer to the **two molecularly confirmed fetuses**, unless explicitly marked “reported association.” They must not be treated as stable population percentages.

| Phenotype/type | Characteristics and observed frequency | Onset/course and functional effect | Suggested HPO term |
|---|---|---|---|
| Severe craniofacial malformation—physical sign | Large craniofacial defect in 2/2; essential primary facial structures failed to form normally | Embryonic/fetal onset; severe, fixed and lethal; incompatible with normal feeding or airway function | Abnormality of facial morphology, **HP:0001999**; abnormal craniofacial morphology, **HP:0000152** |
| Cranial cyst/cystic structure—imaging sign | Abnormal fluid-filled cyst in cranial region in 2/2; exact anatomical identity uncertain | Visible by 12–13 weeks; possibly pharynx or beginning of gut, according to authors | Intracranial cystic lesion, **HP:0010576** or broader abnormal intracranial morphology |
| Hypoplastic eyeballs—physical sign | Reported in syndrome definition | Congenital, severe | Microphthalmia, **HP:0000568** |
| Abnormal nasal and oral openings—physical sign | Two nasal-region openings separated by a septum and an abnormal opening replacing the mouth; unopened stomodeum was considered | Embryonic, severe; normal oral function impossible | Abnormal oral morphology, **HP:0000153**; abnormal nasal morphology, **HP:0000366** |
| Absent/undeveloped palate—physical sign | Palate did not develop | Embryonic, severe | Abnormality of the palate, **HP:0000174** |
| Omphalocele—physical/imaging sign | 2/2 | Present at first-trimester ultrasound; fixed abdominal-wall defect | Omphalocele, **HP:0001539** |
| Fetal akinesia/immobility—functional sign | Immobile limbs in 2/2 | Detected at 12–13 weeks; severe; likely contributed secondarily to muscle underdevelopment | Decreased fetal movement, **HP:0001558**; akinesia, **HP:0002304** |
| Upper-limb hypoplasia—physical sign | 2/2; limbs looked absent externally but contained modestly shortened, nearly normally shaped bones | Embryonic, severe, nonprogressive malformation | Upper-limb undergrowth, **HP:0009824** |
| Lower-limb hypoplasia—physical sign | 2/2 | Embryonic, severe | Lower-limb undergrowth, **HP:0009816** |
| Limbs bound/fused to trunk—physical sign | Defining feature in 2/2; externally only rudimentary protrusions were visible | Embryonic; total loss of independent limb function | Broad annotation: abnormal limb morphology, **HP:0040064**; congenital contracture/pterygium terms as appropriate |
| Transparent membrane-like skin encasing limbs—physical/pathology sign | Defining feature in 2/2; epidermis only 2–5 cell layers | Embryonic, severe barrier-development defect | Thin skin, **HP:0000963**; abnormal skin morphology, **HP:0011121** |
| Absent epidermal granular layer—histologic abnormality | 2/2 examined | Developmental; contributes to failed terminal differentiation/barrier formation | Absent stratum granulosum, **HP:0025815** |
| Absent stratum corneum/horny layer—histologic abnormality | 2/2 examined | Developmental epidermal-barrier failure | Abnormal stratum corneum morphology, **HP:0011127** |
| Absent adnexal structures on outer limbs—histologic sign | 2/2; primitive follicles occurred only within skin infoldings | Congenital ectodermal-appendage defect | Abnormality of skin appendages, **HP:0011138** |
| Muscle hypoplasia—pathology sign | Very poorly developed skeletal muscle in 2/2; authors considered lack of movement contributory | Fetal; severe; both primary developmental signaling and secondary disuse are plausible | Hypoplasia of the musculature, **HP:0009004** |
| General skeletal/bone hypoplasia—radiographic sign | All visible bones hypoplastic in 2/2; growth plates normal and no chondrodystrophy | Fetal, generalized, fixed | Skeletal hypoplasia, **HP:0002652**; limb undergrowth terms above |
| Skull-bone hypoplasia/acalvaria spectrum—radiographic sign | Particularly described in fetus 1 | Fetal, severe | Acalvaria, **HP:0001476**, if complete absence is documented; otherwise skull hypoplasia |
| Abnormal lung lobulation—anatomic sign | Present in both: fetus 1 had four right and three left lobes; fetus 2 had three lobes in each lung | Congenital; clinical respiratory effect unmeasurable | Abnormal lung lobation, **HP:0002101** |
| Tetralogy of Fallot—cardiac sign | 1/2 | Congenital, severe; would impair oxygenation if liveborn | Tetralogy of Fallot, **HP:0001636** |
| Horseshoe kidney—anatomic sign | 1/2 | Congenital; isolated functional impact could not be assessed | Horseshoe kidney, **HP:0000085** |
| Diaphragmatic defect—anatomic sign | 1/2 | Congenital; respiratory effect could not be assessed | Congenital diaphragmatic hernia/defect, **HP:0000776** |
| Normal karyotype—laboratory result | 46,XX in 2/2 | Helped exclude a visible numerical/large structural chromosomal cause | Not a disease HPO abnormality |

The primary histology showed a very thin epidermis with **two to five cell layers**, absent granular and horny layers and absent adnexal structures over the outer limbs. Bone growth plates were normal and the bones were only modestly shortened, indicating that apparent “absence” of limbs was chiefly caused by failed outgrowth/encasement rather than complete skeletal agenesis. [28][213][218][226]

### Quality of life

No EQ-5D, SF-36, PROMIS or other patient-reported outcomes exist. Both confirmed pregnancies were terminated at 13–14 gestational weeks after severe abnormalities were detected. Given the embryonic severity and absence of a surviving classic-null patient, postnatal quality of life cannot be measured; the aggregate impact is fetal death or pregnancy termination and substantial reproductive and psychological burden for the family.

---

# 4. Genetic and molecular information

## 4.1 Gene and protein

| Field | Value |
|---|---|
| Gene | *CHUK* |
| Official name | Component of inhibitor of nuclear factor kappa-B kinase complex |
| HGNC | **HGNC:1974** |
| NCBI Gene | **1147** |
| Ensembl | **ENSG00000213341** |
| Chromosomal location | **10q24.31** |
| OMIM gene | **600664** |
| Protein | IKKα / IKK1 |
| UniProt | **O15111** |
| Protein length | 745 amino acids |
| Major domains | Protein kinase 15–302; leucine zipper 455–476; C-terminal NEMO-binding region 738–743 |
| Principal compartments | Cytosol, IKK complex and nucleoplasm |
| Gene-disease validity | GenCC “Definitive” for Cocoon syndrome; ClinGen assesses a broader lumped CHUK/Bartsocas–Papas relationship separately |

CHUK encodes a serine/threonine kinase that participates in the IKK complex and has additional nuclear, kinase-independent functions in epidermal differentiation. [14][21][311][326]

## 4.2 Classic Cocoon-syndrome variant

| Variant field | Finding |
|---|---|
| Transcript used in original report | **NM_001278** |
| Coding variant | **c.1264C>T** |
| Protein variant | **p.(Gln422Ter)**, originally p.Gln422X |
| Exon | 12 of 21 |
| Variant class | Nonsense/stop-gain |
| Origin | Germline |
| Zygosity | Homozygous in both affected fetuses |
| Segregation | Both unaffected parents heterozygous |
| Predicted product | 421-aa truncated protein |
| Observed RNA consequence | CHUK transcript approximately 12% of control in affected fibroblasts |
| Observed protein consequence | No detectable IKKα protein |
| Functional class | Complete or near-complete loss of function |
| Original control frequency | Absent from 100 ancestry-matched unaffected controls |
| gnomAD/1000 Genomes/TOPMed frequency | No reliable public frequency for this exact CHUK nomenclature was identified; do not infer a numerical frequency |
| ClinVar | No clearly matching, condition-specific ClinVar record for the original CHUK p.Gln422Ter allele was identified |
| ACMG interpretation | **Pathogenic** is strongly supported by PVS1, cosegregation, extreme rarity in matched controls, absent protein and highly specific recessive phenotype, although no formal expert-panel ClinVar assertion was located |

The stop occurs before the leucine zipper and NEMO-binding region, but the decisive experimental observation was **absence of protein**, not merely loss of those C-terminal domains. [28][296][311]

## 4.3 Other genetic mechanisms

| Mechanism | Evidence in classic Cocoon syndrome |
|---|---|
| Large deletion/CNV | Not reported |
| Aneuploidy | Excluded by normal 46,XX karyotypes in the two confirmed fetuses |
| Translocation/inversion | Not reported |
| Somatic mutation | Not applicable; disease-causing variant is germline |
| Modifier genes | None known |
| Founder effect | Possible remote Finnish founder/identity-by-descent, but unproven beyond one pedigree |
| Germline mosaicism | Not reported; residual recurrence risk would still be discussed if parental testing were negative in another family |
| Epigenetic defect | No disease-specific methylation or chromatin signature reported |
| Repeat expansion/mitochondrial DNA | Not relevant |

---

# 5. Environmental, lifestyle and infectious information

No toxin, medication, radiation, maternal disease, nutritional deficiency, smoking, alcohol exposure or occupational factor has been associated with molecularly confirmed Cocoon syndrome. No pathogen causes or triggers it, and it is neither transmissible nor zoonotic.

General inflammatory stimuli can activate IKKα-containing signaling complexes, but this normal biochemical responsiveness is not evidence of a disease-specific gene–environment interaction. Complete developmental loss of IKKα is sufficient to produce the phenotype.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Homozygous germline *CHUK* c.1264C>T creates p.Gln422Ter**, which **leads to** marked transcript depletion and no detectable IKKα protein.  
2. **Loss of IKKα leads to** failure of its nuclear, largely kinase-independent program for embryonic keratinocyte cell-cycle exit and terminal differentiation.  
3. **Failed keratinocyte/periderm differentiation leads to** absent granular/cornified epidermal layers, abnormal skin-appendage development and membrane-like, adhesive/encasing skin.  
4. **Abnormal epidermis leads to** defective ectoderm–mesoderm signaling during limb, skeletal and craniofacial morphogenesis; mouse rescue studies specifically implicate failure to repress ectodermal FGF-family signals such as FGF8.  
5. **Defective morphogenetic signaling leads to** severe craniofacial malformation, inadequate limb outgrowth and abnormal body-wall closure, including omphalocele.  
6. **Skin encasement and malformed limbs lead to** profound fetal akinesia; reduced movement likely **results in** additional secondary skeletal-muscle hypoplasia.  
7. **Branch A:** developmental signaling failure **leads to** skull/bone and lung-lobulation defects and, variably, cardiac, renal and diaphragmatic malformations. The exact human tissue-specific intermediates are **inferred**, not demonstrated.  
8. **Branch B:** absence of IKKα also **would be expected to disrupt** noncanonical and portions of canonical NF-κB signaling in immune/stromal cells; this is demonstrated for surviving hypomorphic/kinase-domain CHUK disease, but an immune phenotype cannot be measured in classic fetal-lethal Cocoon syndrome.  
9. **The combined craniofacial, skin, body-wall and limb defects lead to** fetal lethality or medically indicated pregnancy termination.

## 6.2 Epidermal differentiation and ectoderm–mesoderm signaling

IKKα-null mice and keratinocytes fail to undergo normal terminal epidermal differentiation. The granular layer and stratum corneum are absent, while proliferative epidermal cells persist. Importantly, several experiments indicate that this developmental function depends more on nuclear IKKα scaffolding/coregulation than on its kinase activity or NF-κB activation. Nuclear IKKα participates in a Smad2/3-associated TGF-β program controlling keratinocyte cell-cycle exit and differentiation, and interacts with Notch/p63 regulatory networks. [122][125][126][131]

An epidermis-specific IKKα transgene rescued both epidermal and skeletal morphology in otherwise IKKα-deficient mice. This supports the expert interpretation that abnormal skeleton and limbs are substantially **downstream of defective epidermal signaling**, rather than a primary chondrocyte growth-plate disorder. Elevated limb-bud ectodermal FGF8 is one implicated signal. [118]

Suggested GO/CL annotations:

| Mechanism | Suggested GO biological-process terms | Principal cell type |
|---|---|---|
| Keratinocyte differentiation | GO:0030216, keratinocyte differentiation; GO:0008544, epidermis development | Keratinocyte, **CL:0000312** |
| Epidermal barrier formation | GO:0061436, establishment of skin barrier | Suprabasal keratinocyte; epidermal cell |
| Cell-cycle exit | GO:0045786, negative regulation of cell-cycle progression | Basal and suprabasal keratinocytes |
| Ectoderm–mesoderm signaling | GO:0009887, animal organ morphogenesis; GO:0048736, appendage development | Keratinocyte, mesenchymal cell **CL:0000134** |
| Craniofacial morphogenesis | GO:0048701, embryonic cranial-skeleton morphogenesis | Cranial-neural-crest-derived mesenchymal cell |
| Limb morphogenesis | GO:0035108, limb morphogenesis | Limb-bud ectodermal cell and mesenchymal cell |
| Muscle hypoplasia secondary to akinesia | GO:0007519, skeletal-muscle tissue development | Skeletal muscle cell, **CL:0000188** |

## 6.3 NF-κB pathways

IKKα has separable roles:

* In the **canonical NF-κB pathway**, IKKα can partner with IKKβ and NEMO to phosphorylate IκB proteins, permitting NF-κB nuclear translocation.
* In the **noncanonical pathway**, NIK activates IKKα, promoting processing of NF-κB2 p100 to p52 and RELB-dependent transcription.
* In embryonic epidermis, the crucial terminal-differentiation role is substantially **kinase- and NF-κB-independent**.

This distinction explains why complete IKKα absence causes catastrophic morphogenesis, whereas some kinase-domain or NIK-interaction variants permit survival but cause ectodermal abnormalities plus immunodeficiency.

Suggested pathway annotations include GO:0043123, positive regulation of IκB kinase/NF-κB signaling; GO:0038061, NIK/NF-κB signaling; GO:0007249, IκB kinase/NF-κB signaling; and GO:0008385, IκB kinase complex.

## 6.4 Human molecular profiling

Affected fetal fibroblast expression arrays identified **132 differentially expressed transcripts**, 91 corresponding to recognized genes. Enriched groups involved ossification, the IKK–NF-κB cascade, actin-filament binding and extracellular matrix. *MMP14* RNA was reduced, although MMP14 protein was detected in affected but not age-matched control fibroblasts, which the authors proposed might reflect negative feedback. These findings are exploratory and have not been replicated in additional classic Cocoon samples. [28]

No disease-specific metabolomics, lipidomics, spatial transcriptomics, single-cell atlas, proteomic signature, DNA-methylation signature or CRISPR-screen result has been published for classic Cocoon syndrome.

## 6.5 Recent research, 2023–2024

A 2023 authoritative review of cutaneous inborn errors of NF-κB emphasized that IKKα is required for keratinocyte differentiation—including filaggrin and loricrin expression—but that this function is independent of kinase activity and NF-κB signaling. [124][138]

A 17 May 2024 preprint (PMID **38798321**, subsequently peer-reviewed after the requested 2023–2024 window) described a surviving female with biallelic kinase-domain *CHUK* variants, hypogammaglobulinemia, recurrent lung infections and Hay–Wells-like ectodermal features. Both alleles were loss-of-function; noncanonical NF-κB activation was profoundly diminished, canonical signaling was partially impaired, and wild-type *CHUK* restored noncanonical signaling. This broadens the **CHUK allelic spectrum**, but it does not alter the fetal-lethal prognosis for complete-null p.Gln422Ter Cocoon syndrome. [147]

The 2024 abstract states:

> “Reintroducing wild-type *CHUK* restored non-canonical NF-κB activation.” [147]

---

# 7. Anatomical structures affected

| Level | Structures | Suggested ontology terms |
|---|---|---|
| Primary organ/tissue | Skin and epidermis, especially limb-covering epidermis | UBERON:0002097 skin; UBERON:0001003 epidermis |
| Primary anatomical region | Upper and lower limbs/limb buds | UBERON:0002102 upper limb; UBERON:0002103 lower limb |
| Primary craniofacial | Head, face, palate, primitive mouth/pharyngeal region, eyes and skull | UBERON:0000033 head; UBERON:0001456 face; UBERON:0001716 secondary palate; UBERON:0000970 eye |
| Body wall | Ventral abdominal wall/umbilical region | UBERON:0003697 abdominal wall; omphalocele annotation |
| Musculoskeletal | Skeletal muscle, bone, cartilage/growth plates | UBERON:0001134 skeletal muscle organ; UBERON:0001474 bone element |
| Variable secondary organs | Heart, kidneys, diaphragm and lungs | UBERON:0000948 heart; UBERON:0002113 kidney; UBERON:0001103 diaphragm; UBERON:0002048 lung |
| Principal cells | Keratinocytes, dermal fibroblasts, mesenchymal cells; secondarily myocytes, chondrocytes and osteoblasts | CL:0000312, CL:0000057, CL:0000134, CL:0000188, CL:0000138, CL:0000062 |
| Subcellular | Cytosol, nucleoplasm and IKK complex | GO:0005829, GO:0005654, GO:0008385 |

No consistent lateralization was reported; the encasement and limb phenotype was generalized/bilateral.

---

# 8. Temporal development

| Temporal feature | Evidence |
|---|---|
| Biological onset | Embryonic, during epidermal, craniofacial, limb and body-wall morphogenesis |
| Earliest clinical detection | Multiple abnormalities detected by ultrasound at **12 weeks** in fetus 2 and **13 weeks** in fetus 1 |
| Course | Fixed congenital malformation rather than episodic or relapsing disease |
| Progression | Morphogenetic failure evolves as embryogenesis proceeds; it is not a postnatal degenerative disorder |
| Pregnancy outcomes in confirmed cases | Termination at 13 and 14 weeks |
| Untreated duration | Unknown; authors inferred that similarly affected pregnancies may miscarry early |
| Remission | None reported or biologically expected |
| Critical period | First trimester/early fetal epidermal and limb development |
| Intervention window | No corrective fetal intervention exists; the practical window is early ultrasound and molecular prenatal diagnosis |

The family had a first-trimester miscarriage before the two affected pregnancies, but it was not genotyped and cannot be counted as Cocoon syndrome. Two subsequent pregnancies produced unaffected children. [28]

---

# 9. Inheritance and population

## 9.1 Epidemiology

| Measure | Current estimate |
|---|---|
| Molecularly confirmed classic cases | **2 fetuses** |
| Molecularly confirmed families | **1 Finnish family** |
| Additional historical possible case | 1 ungenotyped “cocoon fetus,” reported in 1987 |
| Prevalence per 100,000 | Not calculable |
| Incidence per 100,000 births/year | Not calculable |
| Orphanet epidemiologic descriptor | Two published cases |
| Geographic evidence | Finland for the molecularly confirmed pedigree; no demonstrated endemic distribution |
| Sex ratio | Both confirmed fetuses female, but no inference is possible from n=2 |
| Age distribution | Prenatal only for classic complete-null disease |

Orphanet’s prevalence compilation lists fetal encasement syndrome as **“2 case(s)”**, not as a numerical population prevalence. [104]

## 9.2 Mendelian parameters

| Parameter | Assessment |
|---|---|
| Inheritance | Autosomal recessive |
| Recurrence for two confirmed carrier parents | 25% affected, 50% carrier and 25% unaffected noncarrier per conception |
| Penetrance | Apparently complete for homozygous complete-null p.Gln422Ter in the observed pedigree; broader allele-specific penetrance is unknown |
| Expressivity | Severe and similar in the two classic fetuses, with variable internal-organ defects |
| Heterozygote phenotype | Parents clinically unaffected; no established carrier phenotype |
| Anticipation | Not applicable |
| Consanguinity | No close consanguinity reported, but a shared 18th-century ancestor was identified |
| Founder effect | Possible but not established |
| Carrier frequency | Unknown |
| Germline mosaicism | Not reported |
| Population enrichment | Not established in Finnish or other populations |

---

# 10. Diagnostics

## 10.1 Diagnostic strategy

1. **Prenatal ultrasound:** Suspect the disorder when first-trimester imaging shows a large craniofacial defect, cranial cystic structure, omphalocele and profoundly immobile hypoplastic limbs apparently incorporated into or encased by the trunk skin.
2. **Detailed fetal assessment:** High-resolution ultrasound, fetal echocardiography and, where useful, fetal MRI to define craniofacial, brain, cardiac, diaphragmatic, renal and lung abnormalities.
3. **Chromosomal testing:** Karyotype and/or chromosomal microarray to exclude common aneuploidies and pathogenic CNVs; these do not diagnose single-nucleotide *CHUK* disease.
4. **Molecular confirmation:** Sequence *CHUK* with deletion/duplication analysis. In a known family, targeted testing for the familial variant is fastest.
5. **Broader sequencing:** A fetal-malformation/ectodermal-dysplasia/pterygium panel, trio WES or WGS is appropriate when the phenotype is atypical or the familial variant is unknown.
6. **Segregation:** Test both parents to establish phase and autosomal-recessive inheritance.
7. **Pathology:** If pregnancy loss or termination occurs, fetal radiography, autopsy and skin histology can document limb encasement, epidermal thinning, missing granular/cornified layers and absent adnexa.

GTR lists **eight clinical tests** under Cocoon syndrome, including single-gene *CHUK* testing and whole-coding-region NGS. [268][269][284]

## 10.2 Utility of test modalities

| Modality | Utility |
|---|---|
| Targeted familial-variant test | Preferred for prenatal or preimplantation testing in a known family |
| *CHUK* sequencing | Diagnostic for coding SNVs/small indels |
| Deletion/duplication analysis | Complements sequencing if only one pathogenic allele is found |
| Multigene fetal-anomaly panel | Useful differential genes include *RIPK4*, *IRF6*, *ZMPSTE24*, *LMNA*, *P4HB*, *NALCN*, *GLDN* and genes for lethal pterygium/fetal-akinesia syndromes |
| Trio WES | High utility for an unexplained recurrent fetal malformation phenotype after karyotype/CMA |
| WGS | Can detect coding, intronic and structural variants; no Cocoon-specific diagnostic-yield study exists |
| CMA | Excludes CNVs but will usually miss the causative nonsense SNV |
| Karyotype | Excludes aneuploidy/large rearrangements; was normal in both confirmed fetuses |
| FISH | No routine role unless a specific rearrangement is suspected |
| mtDNA testing | Not indicated by this phenotype |
| Repeat-expansion testing | Not applicable |
| RNA sequencing | Potentially useful for suspected splice variants, but not validated as routine testing |
| Proteomics/metabolomics/liquid biopsy | No established diagnostic role |

Prenatal exome sequencing may be considered for a structurally abnormal fetus when karyotype and CMA are nondiagnostic, preferably with clinical-genetics consultation. [293][294]

## 10.3 Differential diagnosis

| Differential | Distinguishing features |
|---|---|
| *CHUK*-related Bartsocas–Papas syndrome type 2 | Same gene and overlapping mechanism, but generally less complete fetal encasement; popliteal pterygia, clefting, syndactyly and genital anomalies may predominate |
| *RIPK4*-related Bartsocas–Papas/CHAND syndrome | Similar pterygia, clefting and epidermal differentiation defects; distinguished molecularly by *RIPK4* |
| IRF6-related popliteal pterygium syndrome | Usually autosomal dominant and compatible with survival; cleft lip/palate, lower-lip pits, pterygia and syndactyly |
| Restrictive dermopathy (*ZMPSTE24*, rarely *LMNA*) | Tight thin skin, joint contractures and pulmonary hypoplasia, but usually recognizable facial restriction and hyperkeratotic/restrictive skin rather than the characteristic severe facial-development failure and limb encasement |
| Neu–Laxova syndrome | Severe growth restriction, edema, microcephaly, ocular abnormalities and ichthyosis; biochemical/genetic defects differ |
| Pena–Shokeir/fetal-akinesia deformation sequence | Akinesia, contractures and pulmonary hypoplasia due to many neuromuscular causes; does not intrinsically reproduce the IKKα-null epidermal histology |
| Lethal multiple-pterygium syndrome | Multiple webs and akinesia, often involving neuromuscular-junction genes; lacks the characteristic membrane-like encasement |
| Harlequin ichthyosis (*ABCA12*) | Thick armor-like hyperkeratotic plates and eclabium/ectropion rather than thin membrane-like epidermis |
| Amniotic-band sequence | Asymmetric disruptions/constriction amputations; not recessively recurrent and lacks uniform abnormal epidermal differentiation |
| Severe chromosomal disorder | Excluded or clarified by karyotype/CMA and genomic sequencing |

Restrictive dermopathy’s accepted differential includes Neu–Laxova, Pena–Shokeir and lethal multiple-pterygium syndromes, reflecting the shared fetal-akinesia/tight-skin presentation. [253][265]

## 10.4 Screening

Cocoon syndrome is not included in population newborn screening because classic disease manifests prenatally and is lethal. Appropriate approaches are:

* cascade carrier testing in a molecularly diagnosed family;
* targeted prenatal diagnosis by chorionic-villus sampling or amniocentesis;
* preimplantation genetic testing for monogenic disease, PGT-M;
* carrier testing of reproductive partners where a familial pathogenic allele is known.

---

# 11. Outcome and prognosis

| Outcome domain | Finding |
|---|---|
| Survival | No surviving patient with the classic complete-null fetal-encasement phenotype |
| Five-/ten-year survival | Not applicable |
| Life expectancy | Intrauterine lethal or pregnancy terminated after diagnosis |
| Mortality rate | Cannot be statistically calculated from two terminated pregnancies |
| Recovery | None expected because malformations arise during embryogenesis |
| Principal morbidity | Catastrophic craniofacial, limb, epidermal and abdominal-wall malformation |
| Complications if gestation continued | Likely airway/feeding impossibility, respiratory failure from craniofacial/diaphragmatic/lung abnormalities and cardiac compromise; largely inferred |
| Prognostic factors | Complete absence of IKKα predicts the severe classic phenotype; residual protein/function appears associated with less severe, sometimes surviving CHUK-related disease |
| Validated prognostic biomarker | None |
| Quality-of-life instruments | None used |

The authors characterized complete CHUK loss as a “lethal inherited condition” and suggested that some affected conceptions may be recorded as miscarriages of unknown cause. [275][331]

---

# 12. Treatment

## 12.1 Current treatment status

There is **no disease-modifying pharmacotherapy, surgery, fetal intervention, gene therapy, RNA therapy or approved targeted therapy for classic Cocoon syndrome**, and no Cocoon-specific interventional clinical trial or NCT identifier was identified.

| Intervention category | Current role | Suggested NCIT term |
|---|---|---|
| Maternal–fetal medicine assessment | Defines severity and associated anomalies; not curative | Fetal Ultrasound, NCIT concept family |
| Genetic counseling | Explains inheritance, prognosis and reproductive options | Genetic Counseling |
| Pregnancy continuation with palliative planning | Family-dependent; anticipatory neonatal comfort care if live birth is possible | Palliative Care |
| Pregnancy termination where legal and chosen | Reproductive-management option, not treatment of the molecular disorder | Pregnancy Termination |
| Postmortem examination | Confirms phenotype and improves recurrence counseling | Autopsy |
| Gene replacement/editing | Theoretical only; no preclinical fetal-therapy program reported | Gene Therapy; Genome Editing |
| Pharmacotherapy | None | Not applicable |
| Surgery | No corrective procedure can address the multisystem embryonic malformations | Not applicable |
| Rehabilitation | Not applicable to classic fetal-lethal disease | Not applicable |

IKK inhibitors would be mechanistically inappropriate for a complete loss-of-function syndrome. Conversely, delivering functional *CHUK* after major first-trimester structures have formed would probably be too late; this is an inference, not an experimentally tested therapeutic conclusion.

No treatment response rates, adverse-event data, pharmacogenomic guidance or combination-therapy algorithms exist.

---

# 13. Prevention

| Prevention level | Applicable measure |
|---|---|
| Primary prevention | No diet, vaccine, lifestyle or environmental intervention prevents a recessive *CHUK* disorder |
| Reproductive primary prevention | Carrier identification, genetic counseling, donor gametes, PGT-M or use of an unaffected embryo |
| Secondary prevention/early detection | First-trimester ultrasound and targeted prenatal molecular testing |
| Tertiary prevention | No method prevents malformation progression after it is established; care focuses on informed pregnancy management and avoidance of nonbeneficial interventions |
| Cascade screening | Offer testing to adult relatives after a familial pathogenic variant is established |
| Public-health screening | Not justified by current prevalence and evidence |
| Immunization/prophylaxis | No disease-specific role |

For two confirmed carriers, counseling should communicate the **25% recurrence risk in each conception**, independent of outcomes in previous pregnancies.

---

# 14. Other species and natural disease

| Species/taxon | Ortholog | Natural Cocoon-like disease | Relevance |
|---|---|---|---|
| Human, *Homo sapiens*—NCBI Taxon 9606 | *CHUK*, NCBI Gene 1147 | Yes | Target disease |
| Mouse, *Mus musculus*—Taxon 10090 | *Chuk*, NCBI Gene **12675**, MGI:99484 | No documented spontaneous veterinary syndrome; engineered null models exist | Best-established comparative model |
| Rat, *Rattus norvegicus*—Taxon 10116 | *Chuk*, NCBI Gene **309361** | None identified | Ortholog, no established natural disease |
| Zebrafish, *Danio rerio*—Taxon 7955 | *chuk*, NCBI Gene **393287**, ZFIN:ZDB-GENE-040426-1069 | None identified | Developmental/pathway ortholog |
| Domestic dog/cat/livestock | Conserved CHUK orthologs | No verified naturally occurring fetal-encasement syndrome identified | No current veterinary or breed-specific/VBO association |

No evidence supports zoonotic transmission or cross-species infection. The mechanism is conserved developmental gene function, not transmissible disease. Ortholog records confirm mouse and zebrafish CHUK conservation and expression in developing structures. [162][163][115]

---

# 15. Model organisms

## 15.1 Available models

| Model | Resource/allele | Phenotype recapitulation | Limitations and applications |
|---|---|---|---|
| Global *Chuk* null mouse | **Chuk^tm1Aki**, MGI:1857735 | Perinatal death; shiny, taut/adhesive abnormal epidermis; limb outgrowth failure and encasement; craniofacial defects | Closely reproduces skin/limb phenotype but mice reach birth and human facial defects are more severe; useful for epidermal differentiation and NF-κB studies |
| Global *Chuk* null mouse | **Chuk^tm1Mka**, MGI:1857768 | Rudimentary protruding limbs, absent/truncated tail and external ears, short snout, omphalocele and taut skin | Same limitations; independently validates gene mechanism |
| Global *Chuk/IKK1* null mouse | **Chuk^tm1Ver**, MGI:2386272 | Abnormal skin and skeleton, perinatal lethality | Useful for confirming that phenotypes are not allele-construction artifacts |
| Epidermis-specific rescue | Epidermal *Ikka* transgene on null background | Rescues epidermal differentiation and skeletal morphology | Demonstrates epidermal control of mesodermal morphogenesis; does not model a human treatment |
| Conditional keratinocyte knockout | K5-Cre/K15-Cre with floxed *Chuk* | Epidermal hyperplasia, impaired differentiation and later skin pathology | Useful for tissue-specific function; less representative of complete embryonic null disease |
| Primary affected fetal fibroblasts | Skin fibroblasts from the two human fetuses | Low CHUK RNA, absent protein and altered developmental/ECM transcripts | Irreplaceable human evidence but finite, non-keratinocyte-biased material |
| Keratinocyte culture | Experimental IKKα knockdown/knockout and rescue | Failed terminal differentiation, persistent proliferation; Notch/TGF-β pathway interrogation | Simplifies multicellular craniofacial and limb morphogenesis |
| Zebrafish | *chuk* ortholog resources available | Ortholog expressed in eye, nervous system, notochord, fin and segmental plate | No well-validated Cocoon-specific zebrafish line identified |

MGI recognizes three global null models for human fetal encasement syndrome. Homozygous null mice die neonatally and exhibit thickened taut adhesive skin that prevents appendages from protruding, absent whiskers, skeletal abnormalities and esophageal closure. [171][177][178][189]

The landmark mouse abstract reported:

> “IKKalpha-deficient mice died perinatally. In IKKalpha-deficient fetuses, limb outgrowth was severely impaired despite unaffected skeletal development.”  
> — Takeda et al., *Science*, 9 April 1999; PMID **10195895**. [192]

The models support an unusually strong cross-species genotype–phenotype relationship: global IKKα absence produces nearly the same skin-encased rudimentary limbs and craniofacial/body-wall abnormalities in humans and mice. The key species difference is timing—mice commonly survive until birth, while human complete-null disease appears lethal in utero.

---

# Overall interpretation and knowledge-base recommendations

1. **Canonical entry:** Cocoon syndrome / fetal encasement syndrome, MONDO:0013334, OMIM:613630, ORPHA:465824.
2. **Causal gene:** *CHUK*; HGNC:1974; autosomal recessive.
3. **Defining molecular mechanism:** Complete IKKα loss of function, established for homozygous c.1264C>T, p.(Gln422Ter).
4. **Core phenotypes:** Severe craniofacial malformation, omphalocele, fetal akinesia, hypoplastic limbs bound to the trunk, membrane-like epidermis, absent terminal epidermal layers, muscle and skeletal hypoplasia.
5. **Evidence strength:** Mechanistically compelling human and mouse evidence, but extremely limited human case count.
6. **Frequency representation:** Use “2/2 molecularly confirmed fetuses” rather than generalized percentages.
7. **Allelic-series warning:** Surviving individuals with partial/hypomorphic *CHUK* dysfunction may have Bartsocas–Papas-, Hay–Wells-like or immunodeficiency phenotypes and should not be assigned the classic fetal-encasement prognosis solely because *CHUK* is involved.
8. **Clinical actionability:** Prenatal recognition, molecular confirmation, carrier testing, genetic counseling, PGT-M and targeted prenatal diagnosis; no disease-modifying treatment.

## Key primary and recent sources

| Publication | Date | Evidence | PMID/URL |
|---|---|---|---|
| Lahtela J et al. “Mutant CHUK and severe fetal encasement malformation.” *N Engl J Med* 363:1631–1637 | **21 October 2010** | Foundational human family, variant, fetal pathology, fibroblast functional studies | PMID **20961246**; https://pubmed.ncbi.nlm.nih.gov/20961246/ [58] |
| Takeda K et al. “Limb and skin abnormalities in mice lacking IKKalpha.” *Science* 284:313–316 | **9 April 1999** | Global null mouse | PMID **10195895**; https://pubmed.ncbi.nlm.nih.gov/10195895/ [192] |
| Sil AK et al. “IκB kinase-alpha acts in the epidermis to control skeletal and craniofacial morphogenesis.” *Nature* | **8 April 2004** | Epidermal rescue and FGF mechanism | PMID **15071597**; https://pubmed.ncbi.nlm.nih.gov/15071597/ [118] |
| Cadieux-Dion M et al. “Novel heterozygous pathogenic variants in CHUK…” *BMC Med Genet* | **9 March 2018** | Broader CHUK allelic spectrum | PMID **29523099**; https://pubmed.ncbi.nlm.nih.gov/29523099/ [32] |
| Skin manifestations of inborn errors of NF-κB | **17 January 2023** | Current synthesis of kinase-independent keratinocyte role | https://pmc.ncbi.nlm.nih.gov/articles/PMC9888762/ [138] |
| Riller Q et al. “Compound heterozygous mutations in the kinase domain of IKKα…” | **17 May 2024**, preprint | Kinase-domain CHUK disease, canonical/noncanonical signaling and rescue | PMID **38798321**; https://pubmed.ncbi.nlm.nih.gov/38798321/ [147] |

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
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC7275878` (1 mention) - The genetic basis of pneumococcal and staphylococcal infections: inborn errors of human TLR and IL-1R immunity.
  - shared terms: disease

Weighed against this report's own most characteristic terms: `syndrome`, `chuk`, `fetal`, `ikk`, `cocoon`, `phenotype`, `limb`, `disease`, `severe`, `family`, `classic`, `confirmed`, `encasement`, `skin`, `fetuse`, `gene`, `epidermal`, `craniofacial`, `malformation`, `protein`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 70 |
| Resolved | 63 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013334` (3 mentions) - the report calls it "MONDO"; MONDO calls it **cocoon syndrome**
- `DOID:0060647` (3 mentions) - the report calls it "Disease Ontology"; DOID calls it **fetal encasement syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.