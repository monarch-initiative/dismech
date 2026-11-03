---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-18T05:35:57.504557'
end_time: '2026-10-18T05:39:34.142869'
duration_seconds: 216.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Infantile Liver Failure Syndrome 2
  mondo_id: MONDO:0014659
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
citation_count: 51
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMC:PMC8296689
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 64
  verified: 59
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 4
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0099022
    ontology_label: obsolete vesicle tethering
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
- **Disease Name:** Infantile Liver Failure Syndrome 2
- **MONDO ID:** MONDO:0014659 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile Liver Failure Syndrome 2** covering all of the
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

# Infantile Liver Failure Syndrome 2  
**Disease-knowledge report — current to 18 October 2026**

## Executive summary

**Infantile liver failure syndrome 2 (ILFS2)** is an ultra-rare, autosomal-recessive Mendelian disorder caused by **biallelic pathogenic variants in *NBAS***. Its defining presentation is recurrent, frequently fever-triggered acute liver failure beginning in infancy or early childhood, with partial or complete biochemical recovery between crises. It represents the predominantly hepatic end of a broader *NBAS*-associated disease spectrum that also includes SOPH syndrome and a combined multisystem phenotype. The strongest ILFS2 association is with missense or in-frame variants affecting the **Sec39 region** of NBAS. [1][17][108]

The primary cellular defect involves temperature-sensitive dysfunction of the NBAS-containing **NRZ/syntaxin-18 tethering complex**, impairing Golgi-to-endoplasmic-reticulum trafficking. Resulting ER/Golgi stress, defective protein secretion, altered autophagy and—inferred downstream—oxidative stress and hepatocyte death become markedly worse during fever. [31][17]

There is no disease-specific curative medicine. Current management centers on rapid fever control, prevention of catabolism, close biochemical monitoring and intensive supportive treatment of acute liver failure. Liver transplantation can prevent recurrent hepatic crises but does not correct extrahepatic NBAS deficiency and carries substantial perioperative risk. [17][126][130]

> **Scope note:** “ILFS2” should be used for the predominantly hepatic *NBAS* phenotype, especially the Sec39 subgroup. Many publications combine ILFS2, SOPH and the β-propeller-associated combined phenotype under “NBAS-associated disease”; frequencies from such cohorts must not automatically be interpreted as ILFS2-specific.

---

# 1. Disease information

## Definition and classification

ILFS2 is a genetic parenchymal liver disease characterized by infantile or early-childhood onset of recurrent acute liver failure during febrile illnesses. Between attacks, liver function may normalize completely, particularly in the classical Sec39-associated phenotype. [1][17]

The original molecular discovery study reported:

> “Exome sequencing in five unrelated individuals with fever-dependent RALF revealed biallelic mutations in NBAS.”

It subsequently found affected individuals in five additional families and demonstrated reduced NBAS and p31 protein in patient fibroblasts. [31]

## Identifiers and synonyms

| Resource | Identifier or preferred term |
|---|---|
| MONDO | **MONDO:0014659**, infantile liver failure syndrome 2 |
| OMIM disease | **616483**, Infantile liver failure syndrome 2 |
| Causal gene OMIM | ***NBAS*: 608025** |
| Orphanet | **ORPHA:391677** is submitted as an ILFS2 mapping in GenCC; some resources also associate the broader fever-associated infantile liver-failure grouping with ORPHA:464724. The Orphanet scope should therefore be retained with provenance rather than treated as an unambiguous one-to-one mapping. [62] |
| UMLS | **C3809651** |
| MedGen | **UID 815981** |
| MeSH | No dedicated ILFS2 descriptor identified; index through **Liver Failure, Acute**, genetics, recurrence, infant, and NBAS protein. The discovery paper is indexed under these headings. [31] |
| ICD-10/ICD-11 | No dedicated disease-specific code identified. Code the acute clinical manifestation under the locally applicable acute hepatic/liver-failure category, with a rare-genetic-disease code or extension where supported. |
| Gene | HGNC:**15625**; NCBI Gene:**51594**; Ensembl:**ENSG00000151779** |
| Protein | UniProtKB:**A2RRP1**, 2,371 amino acids |
| Chromosome | **2p24.3** |
| Reference transcript | **NM_015909.4**; older publications commonly use NM_015909.3 |

Recognized names include:

- Infantile liver failure syndrome type 2
- ILFS2
- Fever-associated acute infantile liver failure syndrome
- NBAS-associated recurrent acute liver failure
- NBAS deficiency, predominantly hepatic phenotype
- Fever-triggered recurrent acute liver failure due to *NBAS*

The gene’s historical aliases include **NAG**, “neuroblastoma amplified gene,” and “neuroblastoma amplified sequence.” Its current name is **NBAS subunit of NRZ tethering complex**. [76][78][79]

## Nature of the evidence

The evidence is predominantly **aggregated disease-level evidence**, assembled from:

- individual case reports and pedigrees;
- international multicenter cohorts;
- exome/panel sequencing and segregation studies;
- patient-derived fibroblast experiments;
- model-organism and cell-based functional studies.

It is not principally derived from population EHR datasets. The largest foundational systematic cohort comprised 110 affected individuals from 97 families and 639 cumulative patient-years. [28][108]

---

# 2. Etiology

## Primary cause

ILFS2 is caused by **germline biallelic pathogenic or likely pathogenic variants in *NBAS***. The disease mechanism is recessive loss or severe impairment of NBAS function rather than somatic mutation, infection or toxic exposure. [31][62]

### Genetic risk factors

Risk requires pathogenic variants on both alleles, most often:

- compound-heterozygous missense plus truncating variants;
- homozygous missense variants;
- frameshift, nonsense or canonical splice variants;
- in-frame deletions;
- occasionally larger exon deletions or functionally abnormal noncanonical splice variants.

In the 110-patient study, 86 pathogenic variants were represented: 40 missense, 13 frameshift, 13 splice-site, 12 nonsense, five exon deletions, two in-frame deletions and one intronic variant. No recurrent genotype other than the Yakut p.Arg1914His founder genotype appeared in more than two unrelated families. [108]

Variants determining the classical ILFS2 phenotype cluster particularly in the **Sec39 region**, approximately residues 722–1369. N-terminal β-propeller variants tend to cause combined hepatic/multisystem disease, whereas C-terminal variants more often produce SOPH syndrome. These are correlations, not absolute rules. [17][108]

### Environmental and physiological triggers

Environmental factors do **not independently cause** ILFS2. Important crisis precipitants are:

- febrile viral or bacterial infection;
- elevated core temperature;
- vomiting, fasting and catabolism during illness;
- possibly surgery or other major physiological stress.

The triggering factor is most consistently fever rather than a specific pathogen. No toxin, occupation, diet, sex or lifestyle exposure is established as a primary risk factor. [17]

### Protective factors

No genetically protective variant has been established. Practical protective factors are:

- presymptomatic diagnosis through cascade testing;
- early and sustained fever control;
- prompt provision of carbohydrate and, when needed, lipid calories;
- avoidance of prolonged fasting and dehydration;
- rapid laboratory monitoring during infection;
- routine immunization and ordinary infection-reduction measures.

Reports of siblings diagnosed before symptoms suggest that early emergency management may attenuate or prevent crises, but this is observational rather than randomized evidence. [17]

## Gene–environment interaction

The clearest interaction is **NBAS genotype × fever**:

1. the pathogenic genotype reduces NBAS-complex stability or function;
2. temperature elevation to approximately 40°C causes a further reduction in NBAS and p31 in patient fibroblasts;
3. deficient ER–Golgi trafficking becomes more severe;
4. hepatocytes, which have a high secretory burden, decompensate;
5. acute hepatocytolysis and synthetic failure follow.

This temperature-sensitive cell-biological effect supplies a plausible causal explanation for fever-triggered attacks. [17]

No validated GWAS susceptibility locus, environmental modifier gene or formally demonstrated epigenetic modifier is known.

---

# 3. Phenotypes

## Core phenotype table

Frequencies are often unavailable for pure ILFS2 because published cohorts combine all *NBAS* subgroups. “Typical” below means repeatedly documented in Sec39-associated ILFS2 rather than a measured population prevalence.

| Phenotype/type | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| Recurrent acute liver failure — clinical/laboratory | Defining manifestation; severe, episodic and typically fever-triggered. First crisis usually in infancy or early childhood. Recovery between episodes is often complete. | **HP:0006554 Acute liver failure**; HP:0033246 Recurrent acute liver failure, if supported in the deployed HPO version |
| Fever-triggered episodes — sign/trigger | Very common in classical ILFS2; infection-associated fever is the principal trigger. | **HP:0001945 Fever**; HP:0001954 Episodic fever where appropriate |
| Markedly elevated aminotransferases — laboratory | Can be extreme. In one summarized ILFS2 dataset, mean recorded maxima were AST 13,359 U/L and ALT 9,146 U/L, n=32. [17] | **HP:0002910 Elevated hepatic transaminases** |
| Coagulopathy/synthetic failure — laboratory/sign | Prolonged PT/INR and deficient coagulation-factor synthesis during ALF; severe and potentially life-threatening. | **HP:0003256 Abnormality of coagulation** |
| Hyperbilirubinemia/jaundice — laboratory/sign | Variable during attacks; may be less striking than aminotransferase elevation early in a crisis. | **HP:0002904 Hyperbilirubinemia**; **HP:0000952 Jaundice** |
| Hepatomegaly — sign | Episodic or persistent, depending on phenotype; persistence is more suggestive of multisystem/SOPH overlap. | **HP:0002240 Hepatomegaly** |
| Hepatic steatosis — pathology | Reported in biopsies and imaging; variable. | **HP:0001397 Hepatic steatosis** |
| Fibrosis/cirrhosis — pathology | Not the defining feature of classical ILFS2; may occur after recurrent injury or in broader NBAS disease. | **HP:0001395 Hepatic fibrosis**; **HP:0001394 Cirrhosis** |
| Hyperammonemia — laboratory | Can be severe in ALF and may cause encephalopathy. | **HP:0001987 Hyperammonemia** |
| Hepatic encephalopathy — neurologic sign | Variable; marks severe ALF and profoundly affects consciousness, feeding and safety. | **HP:0001298 Encephalopathy** |
| Hypoglycemia — laboratory | Possible during hepatic failure or catabolic illness; requires urgent correction. | **HP:0001943 Hypoglycemia** |
| Vomiting/poor intake — symptom | Common nonspecific prodrome during infection and worsens catabolism. | **HP:0002013 Vomiting**; **HP:0004395 Malnutrition** when persistent |
| Short stature — physical | Approximately one-third of the predominantly hepatic subgroup in a review; much more prominent in SOPH/C-terminal disease. [17] | **HP:0004322 Short stature** |
| Mild facial dysmorphism — physical | May include flat cheekbones or hypotelorism; usually milder than in SOPH. | **HP:0001999 Abnormal facial shape**; **HP:0000601 Hypotelorism** |
| NK-cell deficiency/dysfunction — laboratory/immune | Reported to variable degrees even in the hepatic subgroup; infection susceptibility may follow. | **HP:0005403 Decreased proportion of natural killer cells** |
| Hypogammaglobulinemia/B-cell deficiency — laboratory | More typical of combined or C-terminal disease but part of the broader spectrum. | **HP:0004313 Decreased circulating antibody level**; **HP:0010976 B-cell immunodeficiency** |
| Developmental delay/hypotonia — neurologic | Not a defining classical ILFS2 feature; consider β-propeller combined disease, consequences of severe crises, or another diagnosis. | **HP:0001263 Global developmental delay**; **HP:0001252 Hypotonia** |
| Optic atrophy — ocular | Primarily SOPH/combined phenotype rather than isolated ILFS2. | **HP:0000648 Optic atrophy** |
| Pelger–Huët anomaly — hematologic morphology | Primarily SOPH-associated. | **HP:0004440 Pelger–Huët anomaly** |
| Osteopenia/fractures — skeletal | More typical of combined or SOPH disease; relates plausibly to impaired collagen trafficking. | **HP:0000939 Osteoporosis**; **HP:0002757 Recurrent fractures** |

The 2024/2025 vesicular-trafficking review reported median first liver-crisis age of **12 months**, range 0–39 months, among 26 patients assigned to the ILFS2 subgroup. It also noted that crises generally decrease in frequency and severity with age, although attacks have occurred in adulthood. [17]

## Quality-of-life effect

No validated ILFS2-specific EQ-5D, PedsQL, SF-36 or PROMIS dataset was identified. The likely burden is substantial:

- recurrent emergency admission and intensive-care risk;
- restrictions around travel, school and infection exposure;
- continuous vigilance during fever;
- repeated blood testing and possible transplant evaluation;
- neurodevelopmental injury after severe hyperammonemia or encephalopathy;
- chronic visual, skeletal or immunological disability in combined phenotypes.

These effects are clinically apparent but have not been quantified using a standardized ILFS2 quality-of-life instrument.

---

# 4. Genetic and molecular information

## Gene and protein

| Attribute | Value |
|---|---|
| Gene | ***NBAS*** |
| Official name | NBAS subunit of NRZ tethering complex |
| HGNC | **HGNC:15625** |
| NCBI Gene | **51594** |
| Ensembl | **ENSG00000151779** |
| OMIM gene | **608025** |
| UniProt | **A2RRP1 / NBAS_HUMAN** |
| Location | **2p24.3** |
| Protein length | **2,371 aa** |
| Main compartments | Cytoplasm, ER and ER membrane |
| Major functions | NRZ/syntaxin-18 vesicle tethering; Golgi-to-ER retrograde transport; localized ER-associated nonsense-mediated mRNA decay |

NBAS is broadly expressed rather than liver-specific. The unusually high secretory activity of hepatocytes is thought to explain their particular vulnerability. [76][78][82]

## Representative pathogenic variants

This table is illustrative, not a complete ClinVar export.

| Variant, transcript NM_015909.4 | Type/classification | Functional or clinical note |
|---|---|---|
| c.686dup, p.(Ser230fs) | Frameshift; pathogenic in ClinVar | Reported in compound heterozygous ILFS2; ClinVar RCV000186578. [48] |
| c.558_560del, p.(Ile187del) | In-frame deletion; pathogenic | N-terminal/β-propeller-associated variant |
| c.603_605del, p.(Leu202del) | In-frame deletion; pathogenic/likely pathogenic | β-propeller region |
| c.2708T>G, p.(Leu903Arg) | Missense; pathogenic | Sec39 region; compatible with hepatic phenotype |
| c.2819A>C, p.(His940Pro) | Missense; reported pathogenic | Homozygous in a child with recurrent liver failure. [60] |
| c.3164T>C, p.(Leu1055Pro) | Missense; pathogenic | Sec39 region; rs796052121. [49][53] |
| c.3596G>A, p.(Cys1199Tyr) | Missense; recurrent pathogenic variant | Sec39 region; repeatedly reported in ILFS2 |
| c.1749G>A, p.(Trp583Ter) | Nonsense; pathogenic | Predicted loss of function/NMD |
| c.4288C>T, p.(Gln1430Ter) | Nonsense; pathogenic | Predicted loss of function/NMD |
| c.5262del, p.(Phe1754fs) | Frameshift; pathogenic | Truncating |
| c.6433-2A>G | Canonical splice; pathogenic | Abnormal splicing |
| c.6840G>A, p.(Thr2280=) | Synonymous splice-altering; pathogenic | Demonstrates that synonymous variants may be pathogenic through RNA processing |
| c.5741G>A, p.(Arg1914His) | Missense founder variant | Homozygous Yakut founder genotype; principally SOPH rather than classical ILFS2 |
| c.1342T>C | Missense | A 2023 functional study found attenuated NBAS mRNA and protein expression. [19][105] |
| c.1725+1G>T | Canonical splice | Homozygous in a 2023 ILFS2 case diagnosed by WES. [58] |

Because many NBAS variants are private, allele-specific assertions should be taken directly from current ClinVar submissions and interpreted with segregation, phenotype, population frequency and functional RNA/protein evidence. As of a 2025 aggregated resource, over 100 ClinVar disease-associated NBAS records were listed, but submissions vary in review strength. [53]

### Population frequency

Pathogenic ILFS2 variants are generally absent or extremely rare in gnomAD/1000 Genomes. Exact ancestry-specific allele frequencies must be retrieved per variant and genome build. The Yakut p.Arg1914His allele is a population-specific founder variant associated mainly with SOPH syndrome, not a globally frequent ILFS2 allele. [17][108]

## Functional consequences

- Most truncating variants lead to reduced transcript by nonsense-mediated decay or reduced protein.
- Some late truncations or splice variants escape NMD and produce shorter proteins.
- Missense variants may impair folding, temperature stability, protein interactions or domain-specific function.
- Patient fibroblasts show reduced NBAS and frequently reduced **p31/USE1**, an interacting syntaxin-18-complex component. [31][108]
- Classical disease is best described as **partial loss of function/hypomorphism**; complete biallelic null loss may be embryonically lethal, although this has not been definitively proven in humans.

## Modifiers, epigenetics and structural variation

- No reproducible modifier gene is established.
- No disease-specific methylation signature, histone modification or chromatin abnormality is known.
- Exon deletions occur, but ILFS2 is not generally a chromosomal-abnormality syndrome.
- No recurrent pathogenic translocation, inversion or aneuploidy has been established.
- The domain affected, residual protein function, variant combination, fever exposure and speed of treatment appear to be major determinants of expressivity.

---

# 5. Environmental information

| Factor | Role in ILFS2 |
|---|---|
| Febrile infection | Principal trigger of hepatic crises; not the underlying cause |
| Hyperthermia | Directly worsens stability/function of the mutant NBAS/p31 trafficking complex in cellular studies |
| Fasting/vomiting | Promotes catabolism and may intensify a crisis |
| Diet | No causal diet identified; maintaining caloric intake during illness is protective |
| Alcohol, smoking, occupation | Not relevant to disease initiation in infants; standard avoidance of hepatotoxins remains appropriate |
| Hepatotoxic medicines | Not proven to specifically trigger ILFS2, but unnecessary hepatotoxic exposure should be avoided |
| Radiation/pollution/toxins | No established association |
| Specific infectious agent | None; multiple febrile viral and bacterial illnesses can trigger attacks |

A 2024 case report linking NBAS deficiency with hemophagocytic lymphohistiocytosis emphasized impaired NK-cell cytotoxicity and vesicle degranulation, but HLH is not an established universal ILFS2 feature. [24]

---

# 6. Mechanism and pathophysiology

## Ordered causal chain

1. **Biallelic pathogenic *NBAS* variants lead to reduced abundance, impaired folding or domain-specific dysfunction of NBAS.**
2. **Defective NBAS leads to instability or impaired assembly of the NBAS–RINT1–ZW10 NRZ tether and the syntaxin-18 SNARE complex**, frequently reducing p31/USE1.
3. **NRZ/syntaxin-18 dysfunction leads to impaired COPI-vesicle tethering and retrograde Golgi-to-ER transport.**
4. **Trafficking impairment leads to defective membrane/protein recycling, altered autophagy and impaired ER-to-Golgi secretion of selected cargo.**
5. **Fever leads to further destabilization of mutant NBAS and p31**, experimentally demonstrated in patient fibroblasts shifted from 37°C to 40°C.
6. **Worsened trafficking dysfunction leads to ER/Golgi stress and activation of the integrated stress response.**
7. **ER stress leads to reactive-oxygen-species generation and hepatocyte injury/apoptosis or necrosis**; the exact death pathway and its relative contributions remain partly inferred.
8. **Hepatocyte destruction results in massive AST/ALT release and loss of synthetic/metabolic capacity.**
9. **Synthetic failure results in coagulopathy; metabolic failure branches to hypoglycemia and hyperammonemia.**
10. **Hyperammonemia and systemic liver failure lead to encephalopathy, cerebral edema risk, multiorgan complications and potentially death.**
11. **Resolution of fever and restoration of trafficking reserve lead to hepatic recovery between episodes**, provided irreversible injury has not occurred.
12. **Parallel branch:** chronic secretory-traffic dysfunction leads to impaired collagen, immunoglobulin or insulin handling, plausibly producing skeletal, immune and endocrine manifestations in combined NBAS disease.
13. **Parallel branch:** altered NBAS-dependent localized nonsense-mediated mRNA decay may lead to dysregulated ER-associated transcripts and developmental phenotypes; its quantitative contribution to human ILFS2 remains unproven.

The 2015 primary paper demonstrated reduced NBAS and p31 in mutant fibroblasts:

> “Immunoblot analysis of mutant fibroblasts showed reduced protein levels of NBAS and its proposed interaction partner p31, both involved in retrograde transport between endoplasmic reticulum and Golgi.”  
> — Haack et al., 2015; PMID **26073778**. [31]

## Pathway and cellular annotation

| Mechanism | Evidence and ontology suggestions |
|---|---|
| Golgi-to-ER retrograde transport | Demonstrated role of NBAS/NRZ. **GO:0006890 retrograde vesicle-mediated transport, Golgi to ER** |
| Vesicle tethering | NBAS–RINT1–ZW10 complex docks COPI vesicles. **GO:0099022 vesicle tethering to endoplasmic reticulum** or closest current GO term |
| SNARE-complex organization | NRZ participates in syntaxin-18 SNARE assembly. **GO:0035542 regulation of SNARE complex assembly** |
| Protein secretion | Impaired trafficking of large secretory cargo, including collagen. **GO:0006886 intracellular protein transport**, **GO:0009306 protein secretion** |
| ER stress | Increased ER-stress transcripts reported in NBAS-deficient fibroblasts. **GO:0034976 response to endoplasmic reticulum stress** |
| Unfolded-protein/integrated stress response | Mechanistically plausible and partly supported. **GO:0036503 ERAD pathway** and **GO:0036498 IRE1-mediated unfolded protein response**, where experimentally appropriate |
| Autophagy | Retrograde-traffic defects can impair autophagic flux. **GO:0006914 autophagy** |
| Oxidative stress | Downstream/inferred contributor to hepatocytolysis. **GO:0006979 response to oxidative stress** |
| Cell death | Hepatocyte death causes the biochemical crisis. **GO:0008219 cell death**, with apoptosis/necrosis subterms only when demonstrated |
| Nonsense-mediated decay | NBAS recruits or cooperates with UPF1 at the ER. **GO:0000184 nuclear-transcribed mRNA catabolic process, nonsense-mediated decay** |
| NK-cell degranulation | Altered lytic-vesicle transport can impair NK cytotoxicity. **GO:0043323 positive regulation of natural killer cell degranulation** |

## Principal cell types

- **Hepatocyte — CL:0000182:** primary disease-effector cell.
- **Natural killer cell — CL:0000623:** reduced number/function in some patients.
- **B lymphocyte — CL:0000236:** quantitative or functional deficiency in broader disease.
- **Pancreatic beta cell — CL:0000169:** possible insulin-secretory involvement in multisystem disease.
- **Osteoblast — CL:0000062** and **fibroblast — CL:0000057:** relevant to collagen secretion and skeletal/connective-tissue features.
- Retinal ganglion cells are likely relevant to optic atrophy, but direct disease-specific mechanistic evidence is limited.

## Molecular profiling

No validated diagnostic transcriptomic, proteomic, metabolomic or lipidomic signature exists. Reported research findings include:

- reduced NBAS and p31 protein;
- aberrant NBAS splicing or reduced transcript;
- increased ER-stress-associated RNA expression;
- transient urinary **3-methylglutaconic acid** elevation during crises in two patients;
- RNA sequencing as a means of demonstrating splice consequences and solving otherwise uncertain diagnoses.

No ILFS2-specific single-cell atlas, spatial-transcriptomic map or integrated multi-omics cohort was identified through 2026. A 2025 study demonstrated that RNA sequencing could expand diagnosis and phenotype definition in NBAS deficiency, but this is not yet a standardized clinical test. [10]

---

# 7. Anatomical structures affected

| Level | Structure | Ontology suggestion and significance |
|---|---|---|
| Primary organ | Liver | **UBERON:0002107**; recurrent hepatocellular injury and acute failure |
| Tissue | Hepatic parenchyma | **UBERON:0001114**; hepatocytes are the principal injured cells |
| Secondary nervous system | Brain | **UBERON:0000955**; affected secondarily by hyperammonemia/encephalopathy or directly in combined disease |
| Eye | Optic nerve | **UBERON:0000962**; principally SOPH/combined phenotype |
| Skeletal system | Bone and vertebral column | **UBERON:0002481 bone tissue**, **UBERON:0001130 vertebral column** |
| Immune system | Peripheral blood/lymphoid compartment | Reduced NK and B cells in some patients |
| Endocrine pancreas | Islets/beta cells | Diabetes is a broader-spectrum manifestation |
| Subcellular | Endoplasmic reticulum | **GO:0005783** |
| Subcellular | ER membrane | **GO:0005789** |
| Subcellular | Golgi apparatus | **GO:0005794** |
| Subcellular | COPI-coated vesicle | **GO:0030137** |
| Subcellular | Cytoplasm | **GO:0005737** |

Liver disease is diffuse, so laterality is not applicable. Optic atrophy, when present, is generally bilateral.

---

# 8. Temporal development

## Onset and course

- **Typical onset:** infancy; median first liver crisis approximately 12 months in an ILFS2 subgroup, with reported range from birth to 39 months. [17]
- **Pattern:** acute or hyperacute attacks superimposed on an otherwise stable interval.
- **Early crisis:** fever/infection followed by vomiting, lethargy and rapidly rising aminotransferases.
- **Advanced crisis:** coagulopathy, hypoglycemia, hyperammonemia, encephalopathy and possible multiorgan failure.
- **Intercritical stage:** biochemical normalization is common in classical ILFS2.
- **Age trend:** attack frequency and severity generally decrease with age, but crises can continue into adulthood.

## Critical intervention window

The principal opportunity is **the first hours of fever or vomiting**, before major hepatic involvement develops. Family emergency protocols should therefore initiate antipyretic therapy and anti-catabolic support before profound coagulopathy or encephalopathy appears. [17]

No spontaneous genetic remission occurs. Apparent clinical improvement with age reflects declining crisis frequency, not correction of the underlying defect.

Pregnancy is possible in adult survivors. A 2023 report documented pregnancy, delivery and the postpartum period in a woman with Sec39-associated ILFS2, expanding the known adult natural history. [55]

---

# 9. Inheritance, epidemiology and population

## Inheritance

- **Autosomal recessive**
- For two carrier parents: 25% affected, 50% carrier and 25% unaffected/noncarrier risk per pregnancy.
- Both sexes are affected.
- Variants are germline.
- Genetic anticipation is not expected.
- Germline mosaicism has not been systematically documented but remains a small theoretical explanation for recurrence if only one parent carries a detected variant.

## Penetrance and expressivity

Formal age-dependent penetrance has not been quantified. Penetrance for some NBAS-associated manifestation appears high in individuals with convincingly pathogenic biallelic variants, but:

- whether ALF occurs is genotype-dependent;
- severity and number of crises vary;
- extrahepatic expressivity is highly variable;
- early management may modify the observed phenotype.

## Epidemiology

No reliable population prevalence, incidence per 100,000, carrier frequency or sex ratio is available. This is an ultra-rare disease and likely underdiagnosed among indeterminate pediatric acute liver failure.

By 2023, more than **160 NBAS-associated cases** and more than 70 distinct pathogenic variants had been published worldwide. These figures include SOPH and combined phenotypes, not only strict ILFS2. [17]

The 2020 international cohort contained 110 individuals from 97 families; patients originated from every continent except South America in that dataset. Median age at last assessment was seven years, range 1–42 years. [108]

## Founder effect and consanguinity

The best-established founder genotype is homozygous **c.5741G>A, p.Arg1914His** in the Yakut population of eastern Russia, primarily causing SOPH syndrome. Thirty families in the 110-patient series carried this genotype. [108]

Consanguinity increases the chance that a rare pathogenic allele is inherited homozygously, but ILFS2 also occurs frequently in nonconsanguineous families through compound heterozygosity.

---

# 10. Diagnostics

## When to suspect ILFS2

Suspect ILFS2 in an infant or child with:

1. recurrent or unexplained acute hepatocellular liver failure;
2. a clear association with fever or infection;
3. extreme AST/ALT elevation;
4. normalization or near-normalization between episodes;
5. similarly affected siblings or consanguinity;
6. short stature, mild dysmorphism or immune abnormalities.

Haack et al. concluded:

> “We recommend NBAS analysis in individuals with acute infantile liver failure, especially if triggered by fever.”  
> PMID **26073778**. [31]

## Acute laboratory evaluation

Recommended studies include:

- AST, ALT, bilirubin fractions, alkaline phosphatase and GGT;
- PT/INR, aPTT, fibrinogen and factor V;
- glucose, lactate, ammonia, blood gas and electrolytes;
- albumin;
- CBC with differential and blood-film review;
- creatinine, urea and urinalysis;
- plasma amino acids, acylcarnitine profile, urine organic acids;
- viral PCR/serology and bacterial cultures as clinically indicated;
- acetaminophen concentration and toxicology where relevant;
- ferritin, triglycerides, soluble IL-2 receptor and marrow assessment if HLH is suspected;
- immunoglobulins, lymphocyte subsets and NK-cell number/function after stabilization.

No biochemical marker is specific for NBAS deficiency. Normal laboratory findings between attacks do not exclude it. [17]

Suggested LOINC concepts should be selected locally for ALT, AST, bilirubin, ammonia, glucose and prothrombin time/INR rather than assigning a single composite test.

## Imaging and pathology

- **Ultrasound with Doppler:** assesses liver size, echogenicity, vascular patency, ascites and alternative structural causes.
- **MRI/CT:** not routinely diagnostic; used for complications or neurologic injury.
- **Liver biopsy:** not required when molecular diagnosis is available and may be unsafe in severe coagulopathy.
- Reported histology is nonspecific and can include steatosis, hepatocellular injury/necrosis and variable fibrosis.

## Genetic testing strategy

1. **Rapid trio WES or WGS** is preferred in unexplained severe or recurrent pediatric ALF because the differential is genetically heterogeneous.
2. A validated **pediatric liver-failure/cholestasis panel** should include at minimum *NBAS, RINT1, SCYL1, LARS1, IARS1, MARS1, TRMU, DLD,* urea-cycle genes and relevant mitochondrial genes.
3. **Single-gene *NBAS* sequencing** is reasonable when fever-triggered recurrent ALF is highly characteristic.
4. Include deletion/duplication analysis because exon-level deletions have occurred.
5. Confirm variants by segregation testing.
6. Use RNA sequencing, targeted RT-PCR or minigene analysis for suspected splice variants.
7. Consider immunoblotting of patient fibroblasts for NBAS/p31 in research or specialized diagnostic laboratories.

Clinical GTR entries include full coding-region NBAS sequencing and multigene infantile-liver-failure panels. [46][47]

### Limited utility

- CMA: detects large copy-number abnormalities but is not first-line for this single-gene disorder.
- Karyotype/FISH: generally not useful.
- Mitochondrial DNA sequencing: appropriate only as part of the differential.
- Repeat-expansion testing: not applicable.
- Liquid biopsy and epigenomic testing: not established.

## Differential diagnosis

| Disorder | Distinguishing features |
|---|---|
| *LARS1* ILFS1 | Infantile liver failure, anemia, hypoalbuminemia and growth failure; not specifically an ER–Golgi trafficking defect |
| *RINT1* ILFS3 | Fever-triggered ALF plus skeletal and neurologic abnormalities; same NRZ complex |
| *SCYL1* CALFAN | Recurrent low-GGT cholestasis, progressive fibrosis and later peripheral neuropathy/ataxia |
| *TRMU* deficiency | Reversible infantile liver failure, often age-limited; mitochondrial translation defect |
| *DLD* deficiency | Liver failure with lactic acidosis, hypoglycemia and metabolic/neurologic features |
| Urea-cycle defects | Disproportionate hyperammonemia, often without massive transaminase elevation |
| Mitochondrial DNA-maintenance disorders | Persistent liver disease, lactic acidosis and multisystem findings |
| Gestational alloimmune liver disease | Neonatal onset with iron overload; not recurrent fever-triggered disease |
| Viral, autoimmune or toxic ALF | Established infectious, immunologic or exposure evidence |
| HLH | Persistent fever, cytopenias, hyperferritinemia, splenomegaly and immune activation |

The main vesicular-trafficking review recommends WES in recurrent ALF of unknown etiology because there are no specific biomarkers capable of reliably separating *NBAS, RINT1* and *SCYL1* disease. [17]

## Screening

There is no population newborn screening assay. Appropriate measures are:

- molecular cascade testing of siblings and relatives;
- carrier testing for the familial variants;
- prenatal or preimplantation testing once the familial genotype is established;
- presymptomatic testing of at-risk siblings because emergency planning may prevent severe attacks.

---

# 11. Outcome and prognosis

## Survival and mortality

No unbiased five- or ten-year natural-history survival estimate exists.

In the 110-patient NBAS cohort:

- 10 deaths were reported among the 73 patients with individualized survival data;
- nine were caused by acute liver failure;
- median age of ALF-related death was **2.3 years**, range **1.5–3.9 years**;
- one patient died during liver transplantation at age 15 years. [108]

A later review table reported 7 deaths among 36 ILFS2-subgroup patients, but cohort composition, ascertainment and follow-up differ; this should not be treated as a population mortality rate. [17]

## Prognostic factors

Adverse factors include:

- β-propeller/combined genotype rather than a purely hepatic Sec39 phenotype;
- very early and severe first crisis;
- delayed recognition and persistent fever/catabolism;
- profound coagulopathy, hyperammonemia, hypoglycemia or encephalopathy;
- recurrent severe ALF;
- irreversible neurologic injury;
- need for transplantation.

Favorable factors include:

- prompt diagnosis;
- early treatment during fever;
- preservation of normal liver function between episodes;
- declining crisis frequency with age;
- successful transplantation in carefully selected severe cases.

There is no validated molecular prognostic biomarker beyond broad genotype/domain correlations.

## Long-term morbidity

Potential long-term effects include:

- neurodevelopmental disability after severe encephalopathy;
- short stature and skeletal fragility;
- optic atrophy;
- immune deficiency and recurrent infections;
- chronic liver enzyme elevation or fibrosis in overlap phenotypes;
- psychosocial burden and transplant complications.

---

# 12. Treatment

## Emergency treatment algorithm

1. **At fever, recurrent vomiting, lethargy or reduced intake:** contact the metabolic/hepatology team immediately.
2. Begin the patient-specific antipyretic plan and physical cooling.
3. Prevent catabolism with oral carbohydrate if safe; if not, give IV dextrose and consider insulin to maintain euglycemia.
4. Check AST/ALT, bilirubin, INR/PT, glucose, ammonia, lactate, CBC, electrolytes and renal function urgently.
5. Treat infection promptly when clinically indicated.
6. If hepatic involvement develops, admit to an experienced pediatric liver/metabolic center.
7. Consider IV lipid, NAC and other ALF-directed supportive measures according to specialist protocol.
8. Monitor for encephalopathy, cerebral edema, bleeding, hypoglycemia, hyperammonemia and multiorgan failure.
9. Contact a transplant center early if synthetic function deteriorates or recovery is uncertain.

A recently published NBAS emergency protocol included early continuous antipyretics, anti-catabolic IV dextrose, IV lipid 1–2 g/kg/day and NAC; however, evidence for the exact regimen remains observational. [121]

## Treatment table

| Intervention | Rationale/evidence | Suggested NCIt term |
|---|---|---|
| Antipyretic treatment and physical cooling | Limits the thermally aggravated trafficking defect; early treatment is associated with milder crises | **Antipyretic Therapy** |
| IV glucose/dextrose | Prevents fasting catabolism and treats hypoglycemia | **Dextrose**, **Intravenous Infusion** |
| IV lipid emulsion | Adds calories when enteral intake is inadequate; evidence limited to case experience | **Lipid Emulsion** |
| N-acetylcysteine | Antioxidant/glutathione support; used empirically in some centers, but pediatric non-acetaminophen ALF trial data do not demonstrate a clear universal survival benefit | **N-Acetylcysteine** |
| Infection-directed antimicrobial therapy | Treats the trigger when bacterial or another treatable infection is present | **Antibiotic Therapy**, agent-specific terms |
| Ammonia/encephalopathy management | Standard pediatric ALF support; may include renal replacement therapy in severe cases | **Renal Replacement Therapy**, **Hemofiltration** |
| Blood-product/coagulation support | Reserved primarily for active bleeding or invasive procedures; INR correction alone can obscure prognostic trends | **Plasma Transfusion**, **Blood Product Transfusion** |
| Liver transplantation | Prevents future liver crises; last-resort definitive hepatic treatment | **Liver Transplantation** |
| Immunoglobulin replacement | Consider for clinically significant hypogammaglobulinemia/recurrent infections | **Intravenous Immunoglobulin Therapy** |
| Nutritional, PT/OT and vision support | Addresses chronic multisystem morbidity | **Nutritional Support**, **Physical Therapy**, **Occupational Therapy**, **Vision Rehabilitation** |

### Medication cautions

The 2024 review discouraged routine acetaminophen/paracetamol because its toxicity converges on oxidative and integrated-stress-response mechanisms and cautioned against ibuprofen in established ALF because of bleeding and renal risks. Metamizole was suggested where locally approved. These are expert recommendations rather than comparative ILFS2 trial results; local pediatric hepatology guidance takes precedence. [17]

## Liver transplantation

Six transplanted patients in the 110-patient study had no post-transplant liver crisis over 44 cumulative follow-up years. [108]

A 2023 series described transplantation in three children—two males and one female—with fever-triggered recurrent ALF and concluded that transplantation was effective, while emphasizing postoperative complications. PMID **36594124**. [126]

The broader 2025 cohort recorded 16 transplants: none had recurrent ALF, but nine experienced complications and estimated five-year post-transplant survival was 70%. This supports transplantation for recurrent life-threatening or irreversible ALF, not routine prophylactic transplantation. [122][123]

## Experimental or advanced therapies

- No approved NBAS-targeted drug.
- No established gene replacement, CRISPR, ASO, siRNA or mRNA therapy for germline NBAS deficiency.
- No disease-specific interventional clinical trial was identified.
- Gene replacement is technically difficult because the NBAS coding sequence and 271-kDa protein are very large.
- Chaperones that stabilize selected missense proteins are conceptually attractive but remain preclinical.
- Liver-directed gene or cell therapy might not correct eye, immune, skeletal or neurologic manifestations.

No established pharmacogenomic guideline applies.

---

# 13. Prevention

## Primary prevention

The inherited genotype cannot be prevented after conception. Reproductive options include:

- carrier testing for relatives;
- prenatal diagnosis using familial variants;
- preimplantation genetic testing for monogenic disease;
- donor gametes or other family-planning options.

## Secondary prevention

- Presymptomatic testing of siblings.
- Written emergency letter/card.
- Baseline liver, growth, immune, skeletal, developmental and ophthalmologic assessment.
- Immediate testing during fever.
- Routine vaccination, including influenza and other age-appropriate vaccines, unless contraindicated.
- Prompt medical review for infection.

No ILFS2-specific vaccine exists.

## Tertiary prevention

- prevent fasting and dehydration;
- use an illness-specific anti-catabolic plan;
- monitor ammonia and glucose before neurologic deterioration;
- treat immune deficiency and recurrent infections;
- monitor bone density, vitamin D/calcium status and growth;
- ophthalmologic surveillance;
- developmental and rehabilitation services;
- timely transplant referral after severe recurrent crises.

There is no evidence that ordinary exercise, a special chronic diet or environmental decontamination prevents the genetic disease.

---

# 14. Other species and natural disease

| Item | Evidence |
|---|---|
| Naturally occurring veterinary ILFS2 | No well-established naturally occurring NBAS-associated recurrent liver-failure syndrome was identified in companion animals, livestock or wildlife. |
| Zoonotic potential | None; ILFS2 is a germline human genetic disorder and is not transmissible. |
| Cross-species conservation | NBAS/SMGL-1 function in vesicular trafficking and nonsense-mediated decay is evolutionarily conserved. |
| Zebrafish | *Danio rerio*, NCBI Taxonomy **7955**; Nbas depletion causes abnormal embryogenesis and reduced viability. |
| Mouse | *Mus musculus*, NCBI Taxonomy **10090**; MGI gene **Nbas/MGI:1918419**. |
| Nematode | *Caenorhabditis elegans*, NCBI Taxonomy **6239**; functional counterpart **smgl-1** participates in NMD. |

No VBO breed association is applicable.

---

# 15. Model organisms and experimental systems

| Model | Findings | Relevance and limitations |
|---|---|---|
| Patient-derived fibroblasts | Reduced NBAS and p31, defective vesicle tethering, ER-stress changes and temperature-dependent worsening at 40°C | Best disease-specific mechanistic model, but fibroblasts do not reproduce hepatocyte secretory metabolism |
| HEK293/other cultured cells | NBAS knockdown and trafficking/NMD assays define protein function and variant effects | Useful for molecular dissection; lacks liver-specific physiology |
| Zebrafish Nbas morphants | Severe developmental defects, reduced embryonic viability and defective degradation of premature-termination-codon transcripts | Establishes conserved NMD function, but is a transient knockdown and does not faithfully reproduce episodic fever-triggered human ALF |
| Human-mRNA rescue in zebrafish | Human full-length NBAS mRNA rescued much of the 24-hour morphant phenotype | Supports functional orthology |
| Mouse knockout/IMPC | Nbas knockout has significant mortality/aging, eye, nervous-system, adipose and cardiovascular phenotypes in IMPC screening | Demonstrates systemic importance; current model is not a validated ILFS2 crisis model and reported liver recapitulation is limited |
| Patient iPSC/hepatocyte or liver organoid | No widely validated, standardized published ILFS2 model identified | High-priority future platform for thermal-stress and therapeutic screening |
| Computational structural modeling | Defines N-terminal β-propeller, Sec39-like α-solenoid and C-terminal variant clusters | Supports genotype–phenotype grouping but does not substitute for biochemical validation |

The zebrafish primary study reported:

> “Morpholino-induced depletion of zebrafish Dhx34 and Nbas proteins results in severe developmental defects and reduced embryonic viability.”

It also found that the proteins were required for degradation of premature-stop-containing mRNAs. PMID **21227923**, published 11 January 2011 online. [169][170]

The IMPC has tested 20 physiological systems in Nbas-knockout mice and reports significant effects in five—vision/eye, nervous system, mortality/aging, adipose and cardiovascular systems—but this is a broad knockout phenotype rather than a fever-dependent hepatic knock-in model. [168]

---

# Current research assessment

## Important 2023–2024 developments

1. **Functional validation of new variants:** A 2023 study showed that an infant’s c.1342T>C NBAS variant reduced NBAS mRNA and protein, reinforcing the need for RNA/protein evidence when missense variants are novel. [19][105]

2. **Adult and reproductive natural history:** A 2023 pregnancy report demonstrated survival into reproductive age and highlighted the need for metabolic/hepatology planning during pregnancy, delivery and postpartum stress. [55]

3. **Transplant experience:** A 2023 three-patient series supported transplantation for otherwise uncontrollable NBAS-related ALF while documenting postoperative risk. PMID **36594124**. [126]

4. **Integrated trafficking-disease framework:** The 2024 review unified *NBAS, RINT1* and *SCYL1* disorders as fever-triggered vesicular-trafficking liver-failure diseases and recommended WES plus immediate emergency protocols. PMID **38279772**, publication online 27 January 2024. [17]

5. **Immune-system expansion:** A 2024 report of HLH associated with NBAS deficiency drew attention to impaired NK-cell cytotoxic degranulation, although this remains rare and cannot yet be considered a defining ILFS2 manifestation. PMID **39429260**. [24]

## Expert interpretation

The highest-confidence conclusions are that *NBAS* has a definitive recessive relationship with ILFS2, that fever acts through a temperature-sensitive cellular defect, and that rapid anti-catabolic crisis management is medically rational. The major remaining uncertainties are:

- why hepatocytes are dramatically affected while many other secretory cells are spared;
- how much disease arises from vesicular trafficking versus localized NMD;
- which variants retain enough function for pharmacological stabilization;
- the true population incidence and age-dependent penetrance;
- the comparative effectiveness of NAC, lipid infusion and specific antipyretic regimens;
- when recurrent crises justify transplantation.

The GenCC relationship between *NBAS* and MONDO:0014659 is currently classified as **definitive**, consistent with multiple affected families, segregation, characteristic phenotype and functional evidence. [62]

---

# Knowledge-base curation recommendations

1. Curate **ILFS2/MONDO:0014659** as an autosomal-recessive, *NBAS*-caused, predominantly hepatic disease.
2. Maintain links to the broader *NBAS*-associated disease spectrum, but do not automatically attach every SOPH phenotype to strict ILFS2.
3. Represent fever as a **trigger/modifier**, not an etiologic infectious cause.
4. Annotate the key causal pathway:
   - *NBAS* loss of function  
   → NRZ/syntaxin-18 dysfunction  
   → impaired Golgi-to-ER trafficking  
   → ER stress  
   → hepatocyte death  
   → recurrent acute liver failure.
5. Mark oxidative stress, exact hepatocyte-death modality and NMD contribution as partly inferred.
6. Store clinical frequencies with subgroup and denominator provenance.
7. Treat all therapy evidence as observational/supportive except general pediatric-ALF evidence; no ILFS2-specific randomized treatment trial exists.
8. Use PMID **26073778** as the landmark gene-discovery evidence, PMID **31761904** as the major genotype–phenotype cohort, PMID **36594124** for the 2023 transplant series, PMID **38279772** for the 2024 trafficking-disease review, and PMID **21227923** for the zebrafish NMD model.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC8296689` (1 mention) - Disease ontologies for knowledge graphs.
  - shared terms: disease

Weighed against this report's own most characteristic terms: `nbas`, `ilfs2`, `liver`, `recurrent`, `disease`, `variant`, `phenotype`, `failure`, `fever`, `function`, `patient`, `hepatic`, `protein`, `infection`, `acute`, `severe`, `pathogenic`, `include`, `deficiency`, `trafficking`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 64 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 5 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0099022` (obsolete vesicle tethering) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005789` (1 mention) - the report calls it "ER membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.

59 of 64 terms resolved to a current term; the rest could not be looked up either way.