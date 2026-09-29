---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T13:09:41.180057'
end_time: '2026-09-28T13:15:49.715226'
duration_seconds: 368.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Epidermolytic Hyperkeratosis 2
  mondo_id: MONDO:0958184
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
citation_count: 21
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 21
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0001510
    reported_labels:
    - palm of hand
    ontology_label: skin of knee
  - term_id: UBERON:0001509
    reported_labels:
    - sole of foot
    ontology_label: triceps brachii
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  - Orphanet
  - OMIM
  - CT
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epidermolytic Hyperkeratosis 2
- **MONDO ID:** MONDO:0958184 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epidermolytic Hyperkeratosis 2** covering all of the
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

# Epidermolytic Hyperkeratosis 2 (Epidermolytic Ichthyosis due to KRT10): An Integrated Clinical, Molecular, and Translational Overview

Epidermolytic Hyperkeratosis 2 (EHK2), more commonly referred to within contemporary nosology as **epidermolytic ichthyosis due to KRT10** or **epidermolytic hyperkeratosis type 2**, is a rare keratinopathic ichthyosis characterized by congenital erythroderma, blistering, and later progressive hyperkeratosis, caused by pathogenic variants in the *KRT10* gene encoding keratin 10, a major suprabasal epidermal intermediate filament protein.[3][4][11][13][20] Autosomal dominant EHK2 (EHK2A, OMIM 620150) arises from heterozygous missense or small in-frame variants that exert dominant-negative effects on keratin filament assembly, whereas autosomal recessive forms (often grouped as recessive epidermolytic ichthyosis) result from biallelic loss-of-function mutations that abolish K10 expression and produce a distinct, sometimes lethal neonatal phenotype.[2][12][13][14] Clinically, affected neonates present with generalized erythema, skin fragility, and blistering, evolving over time into focal or generalized hyperkeratosis with variable palmoplantar involvement, significant risk of infection, and profound impact on quality of life.[3][4][9][13][20] Histopathology shows the classic pattern of epidermolytic hyperkeratosis with suprabasal cytolysis and keratin clumping, while genetic testing identifies *KRT10* variants and allows precise genotype–phenotype correlations that increasingly guide prognosis and management.[4][5][11][14][20] Animal models, especially transgenic mice expressing mutant K10 and K10-null mice, have elucidated the dominant-negative versus loss-of-function biology of K10 and provide powerful systems for testing emerging therapies, including retinoid regimens and experimental gene-based approaches.[15][16][17][4] This report synthesizes current knowledge across clinical, molecular, mechanistic, epidemiologic, diagnostic, and therapeutic domains, with particular attention to autosomal dominant EHK2A and autosomal recessive KRT10-associated epidermolytic ichthyosis, and frames these insights within relevant biomedical ontologies to support structured disease knowledge base construction.[11][12][13][14][20]  

## 1. Disease Information

### 1.1 Definition, Nosology, and Disease Concept

Epidermolytic Hyperkeratosis 2 is best understood within the broader family of **keratinopathic ichthyoses**, which are inherited disorders of epidermal cornification caused by pathogenic variants in suprabasal keratin genes *KRT1*, *KRT10*, and *KRT2*.[13][4][20] The principal clinical entity is epidermolytic ichthyosis (EI), historically named bullous congenital ichthyosiform erythroderma (BCIE), characterized by generalized erythema, blistering, erosions, and later hyperkeratosis, with histopathology revealing epidermolytic hyperkeratosis in the upper epidermal layers.[4][9][12][13][20] Within this umbrella, **EHK1** denotes disease due to *KRT1* mutations on chromosome 12q13.13, whereas **EHK2** refers to disease caused by *KRT10* mutations on chromosome 17q21.2–q21.3, with autosomal dominant EHK2A (OMIM 620150) and autosomal recessive EHK2B (OMIM 620707) distinguished by inheritance mode and mutational mechanism.[1][6][8][11][12][13][20] Orphanet classifies autosomal dominant epidermolytic ichthyosis (EI) as a rare keratinopathic ichthyosis with neonatal blistering that progressively becomes hyperkeratotic, caused by mutations in *KRT1* or *KRT10* and assigned Orphanet ID 312.[20] Autosomal recessive epidermolytic ichthyosis, often collodion at birth and lacking palmoplantar keratoderma, is recognized separately (Orphanet ID 512103) and is consistently associated with *KRT10* loss-of-function variants.[2][12][13][14]  

EHK2 is part of the ICD-10 category Q80.3 “Other congenital ichthyosis,” shared with epidermolytic ichthyosis broadly, and ICD-11 includes EC20.03 for epidermolytic ichthyosis.[4][5][6][20] MedlinePlus Genetics describes epidermolytic hyperkeratosis as a skin disorder present at birth, with red, blistering skin evolving to thickened, often malodorous hyperkeratotic plaques, and specifies that *KRT1* mutations are associated with **palmoplantar hyperkeratosis (PS-type)** whereas *KRT10* mutations usually produce **non-palmoplantar (NPS-type)** disease.[3][8] Orphanet and OMIM note that keratinopathic ichthyoses have very low prevalence, with estimates of EI ranging from 1 in 100,000–300,000 in some studies and between 1/2,300,000–4,350,000 in Japanese and Danish populations.[4][9][20][13] Within these, EHK2 cases are a subset but likely represent a substantial fraction due to the mutational hotspot in *KRT10* and the predominance of *KRT10* mutations in some cohorts.[14][13][20]  

From a disease ontological perspective, EHK2 would be mapped as a child of MONDO terms for epidermolytic ichthyosis and keratinopathic ichthyosis, and the user’s suggested MONDO:0958184 appears to correspond to “epidermolytic hyperkeratosis 2” or “epidermolytic ichthyosis due to KRT10,” although this mapping should be cross-checked against up-to-date MONDO releases.[20] At the level of Human Phenotype Ontology (HPO), EHK2 is associated with phenotypes such as congenital erythroderma, skin blistering, erosions, hyperkeratosis, palmoplantar keratoderma (in some cases), and recurrent skin infections, among others.[3][4][9][13][20] Disease information for EHK2 is derived from aggregated case series, registries, and genetic databases, rather than isolated electronic health records, with major resources including OMIM entries for EHK2A and recessive EI, Orphanet disease summaries, DermNet clinical reviews, and peer-reviewed cohort analyses.[1][2][4][11][12][13][14][20]  

### 1.2 Identifiers, Synonyms, and Coding Systems

EHK2 is embedded in a complex synonymy reflecting historical terminology and evolving molecular classification. OMIM lists “epidermolytic hyperkeratosis 2A, autosomal dominant” under entry 620150, linked to *KRT10* at 17q21.2, and references older generic terms for epidermolytic ichthyosis and bullous congenital ichthyosiform erythroderma.[11][1][10][20] Orphanet’s entry for autosomal dominant epidermolytic ichthyosis (ORPHA:312) and MedlinePlus identify numerous synonyms, including **BCIE**, **BIE**, **Bullous congenital ichthyosiform erythroderma**, **Bullous erythroderma ichthyosiformis congenita of Brocq**, **Bullous ichthyosis**, **epidermolytic ichthyosis**, **epidermolytic hyperkeratosis**, and **Ichthyosis hystrix Brocq type**.[3][4][9][20] The KRT10-associated recessive entity is often referred to as **autosomal recessive epidermolytic ichthyosis**, **recessive EI**, or **lethal autosomal recessive epidermolytic ichthyosis** when neonatally fatal, and has Orphanet ID 512103.[2][12][13][14]  

ICD-10 includes EHK/EI within Q80.3 “Other congenital ichthyosis,” and DermNet explicitly associates epidermolytic ichthyosis (formerly epidermolytic hyperkeratosis) with Q80.3 and ICD-11 code EC20.03.[4][5][6][20] Superficial epidermolytic ichthyosis (SEI, Ichthyosis bullosa of Siemens), which is due to *KRT2* mutations, is classified separately under ICD-10 Q80.8 and ICD-11 EC20.03.[7][13] SNOMED CT concepts such as 254167000 have been linked to epidermolytic hyperkeratosis and related entities.[1][4][5][20] MedGen, GARD, and UMLS also provide concepts for epidermolytic ichthyosis and bullous congenital ichthyosiform erythroderma, and ClinVar uses these disease names when annotating *KRT10* variants.[19][8][20]  

From a structured data perspective, the disease can be annotated with the following key identifiers and ontology concepts, though exact mappings should be verified in current releases: Orphanet:312 (AD EI), Orphanet:512103 (AR EI), OMIM:620150 (EHK2A), OMIM:148080 (*KRT10* gene), ICD-10:Q80.3, ICD-11:EC20.03, SNOMED CT:254167000 (epidermolytic hyperkeratosis or epidermolytic ichthyosis), UMLS C0079153 (epidermolytic hyperkeratosis), and a MONDO term for epidermolytic ichthyosis, with MONDO:0958184 as a candidate for the KRT10-specific subtype.[1][3][4][5][6][8][11][19][20] The disease-level knowledge summarized here is derived from aggregated resources (OMIM, Orphanet, DermNet, MedlinePlus, peer-reviewed clinical cohorts), rather than individual patient records, though many primary studies analyze detailed phenotypic and genotypic information at the patient level.[3][4][9][12][13][14][20]  

### 1.3 Relation to Broader Disease Categories

Conceptually, EHK2 resides at the intersection of **ichthyoses**, **genodermatoses**, and **disorders of cornification**. MedlinePlus emphasizes that epidermolytic hyperkeratosis is part of the group of conditions called ichthyoses, which classically show scaly skin, but notes that in EHK the skin is thick but not necessarily scaly, highlighting its distinct clinical pattern.[3] DermNet identifies epidermolytic ichthyosis as one of the five main types of ichthyosis alongside lamellar ichthyosis, ichthyosis vulgaris, congenital ichthyosiform erythroderma, and X-linked ichthyosis, and categorizes it as a genetic disorder of keratinization.[4] Orphanet groups EHK/EI under **keratinopathic ichthyoses**, distinguished by a blistering neonatal presentation followed by hyperkeratosis, and links them to mutations in suprabasal keratin genes.[13][20]  

Within keratin disorders, EHK/EI is unique in several respects. DermNet notes that epidermolytic ichthyosis is the only keratin disease with well-documented genetic mosaicism, manifesting clinically as epidermolytic nevi when postzygotic mutations occur, and posing a risk of generalized disease in offspring if germ cells are involved.[4][13][14] Superficial epidermolytic ichthyosis, due to *KRT2* mutations, is recognized as a distinct but closely related entity with more superficial blistering and erosions.[7][13] Among disorders of cornification, EHK2 offers a clear example of how single amino acid substitutions in conserved helix boundary motifs of structural proteins can dramatically perturb tissue architecture and function, providing a model system for broader principles of intermediate filament biology and skin barrier physiology.[12][14][15][16]  

In summary, Epidermolytic Hyperkeratosis 2 represents a molecularly defined subtype of epidermolytic ichthyosis, anchored in the *KRT10* gene, distinguished clinically by a non-palmoplantar-predominant pattern in most autosomal dominant cases and distinct recessive phenotypes, and situated within the broader conceptual frameworks of keratinopathic ichthyoses, genodermatoses, and Mendelian disorders of epidermal cornification.[3][4][9][12][13][14][20]  

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary etiologic factor in Epidermolytic Hyperkeratosis 2 is the presence of **pathogenic variants in the *KRT10* gene**, which encodes keratin 10 (K10), a type I intermediate filament protein abundantly expressed in suprabasal keratinocytes of the epidermis.[8][11][12][13][14] OMIM entry 620150 explicitly states that autosomal dominant epidermolytic hyperkeratosis 2A is caused by heterozygous mutation in *KRT10* on chromosome 17q21, and Orphanet confirms that autosomal dominant EI/EHK can be due to mutations in either *KRT1* or *KRT10*.[11][20] MedlinePlus Genetics notes that dozens of mutations in *KRT10* have been found in people with epidermolytic hyperkeratosis, most often associated with the non-palmoplantar subtype and featuring widespread thick skin on many parts of the body but sparing palms and soles.[3][8] DermNet similarly reports that epidermolytic ichthyosis is caused by missense mutations in keratin genes *KRT1* and *KRT10*, with *KRT10* mutations leading to variable disruption and decreased stability of K1/K10 tonofilaments and hyperkeratosis due to impaired desquamation.[4]  

Extensive mutational catalogs underscore the genetic heterogeneity within EHK2. A British Journal of Dermatology cohort study analyzing 28 patients with EI identified 14 different mutations in *KRT1* and *KRT10*, of which four were novel, and noted that approximately 87% of reported mutations are heterozygous missense changes in conserved helix boundary motifs critical for filament formation.[14] That study highlighted that palmoplantar keratoderma suggests *KRT1* mutations, whereas *KRT10* mutations in most instances give rise to non-palmoplantar variants, reinforcing the clinical distinction between EHK1 and EHK2.[14] More recently, a large clinical spectrum study of keratinopathic ichthyoses documented autosomal dominant EI due to *KRT10* variants clustered in the rod domain and autosomal recessive EI caused by null mutations that abolish keratin 10 expression, with recessive cases manifesting collodion presentation at birth and sometimes lethal erythroderma.[13][12][14]  

Autosomal recessive epidermolytic ichthyosis due to *KRT10* represents a distinct etiologic scenario characterized by **loss-of-function**. A 2010 British Journal of Dermatology report described a lethal autosomal recessive epidermolytic ichthyosis caused by a novel donor splice-site mutation in *KRT10* (c.1155+5G>A), with the affected neonate homozygous and both parents heterozygous, and emphasized that three inbred pedigrees with recessive EI due to *KRT10* null mutations had previously been described.[12] In the recent clinical spectrum study, recessive EI is attributed to loss of keratin 10 expression regardless of mutation location, underscoring a consistent pathogenic mechanism across different truncating or frameshift variants.[13]  

Thus, EHK2 arises from germline *KRT10* mutations—heterozygous, typically missense or small in-frame changes exerting dominant-negative effects in autosomal dominant disease, and biallelic loss-of-function mutations in autosomal recessive disease—against a background of normal *KRT1* and *KRT2* function.[11][12][13][14] Postzygotic *KRT10* mutations lead to mosaic manifestations (epidermolytic nevi), which can have reproductive consequences if gonadal tissue is involved.[4][13][14] No non-genetic primary causal factors have been documented, confirming EHK2 as a purely Mendelian, monogenic disorder of structural protein function.[3][4][11][13][20]  

### 2.2 Genetic Risk Factors and Susceptibility

Within the context of EHK2, **genetic risk is essentially synonymous with carrying a pathogenic *KRT10* variant**, either heterozygous (dominant) or biallelic (recessive).[11][12][13][14] ClinVar reports numerous *KRT10* variants interpreted as pathogenic or likely pathogenic for epidermolytic ichthyosis, including missense changes at conserved residues in the rod domain and truncating variants associated with recessive EI.[19][8][13][14] For autosomal dominant EHK2A, each child of an affected heterozygous individual has a 50% probability of inheriting the mutation and therefore the disease, assuming full penetrance.[3][4][11][13][20] De novo mutations are common; DermNet indicates spontaneous mutation occurs in approximately 50% of EI cases, and the genotype–phenotype study noted that 17 of 28 patients had de novo mutations, illustrating that parental family history may be absent despite high genetic risk to offspring once the mutation arises.[4][9][14][13]  

For autosomal recessive EHK2B, consanguinity and carrier status in both parents constitute major genetic risk factors. The lethal recessive EI case report and the genotype–phenotype study both involved consanguineous families with homozygous *KRT10* truncating mutations, and the authors emphasized that the existence of a recessive form increases recurrence risk from ≤1% (for new dominant mutations) to 25% in consanguineous couples carrying the same *KRT10* null variant.[12][14] This has important implications for genetic counseling in communities where consanguineous marriage is common, as recessive *KRT10* mutations may be enriched and carrier frequency elevated. Population-level allele frequencies for specific *KRT10* variants in gnomAD or ExAC are not provided in the current search results, but given the extreme rarity of EI/EHK, pathogenic alleles are expected to be very infrequent in general populations.[13][20]  

Modifier genes affecting EHK2 severity have not been definitively identified, but variation in other keratin genes (*KRT1*, *KRT2*, *KRT5*, *KRT14*) and in genes controlling epidermal differentiation, inflammation, or desquamation could plausibly modulate phenotype, as suggested by animal models where suprabasal keratin composition changes compensate for K10 loss.[15][16][13] The clinical spectrum study documented striking inter-individual variability even among patients sharing the same *KRT10* mutation, indicating that epigenetic, environmental, or polygenic background effects may influence susceptibility to severe blistering, infection, or psychosocial impact.[13][14]  

### 2.3 Environmental and Lifestyle Risk Factors

Although EHK2 is fundamentally genetic, several **environmental and lifestyle factors exacerbate disease manifestations or precipitate acute complications**. Clinical reviews and cohort reports consistently highlight mechanical friction, minor trauma, heat, humidity, and occlusion as triggers of blistering and erosions, particularly in infancy and early childhood when the skin is fragile.[3][4][9][13][20] DermNet describes peeling, erosions, and denuded skin occurring after minor friction or trauma in epidermolytic ichthyosis, and emphasizes that blisters and superficial ulcerations at birth can be worsened by physical stress.[4] MedlinePlus notes that newborns with EHK lack the protection of normal skin and are at risk of dehydration and infection, with sepsis being a serious risk, implying that environmental exposures such as high ambient temperature and inadequate hydration can increase morbidity.[3]  

Secondary infections represent another key environmental risk factor. Thick hyperkeratotic skin in older individuals often harbors bacteria that can proliferate and cause a distinct malodor; DermNet mentions that bleach baths and antiseptic washes are used to reduce microbial colonization and prevent infections.[4][17] Recurrent bacterial skin infections can worsen erythema, pain, and systemic symptoms, and septicemia remains a life-threatening complication in severely affected neonates and infants.[3][4][13] Hygienic conditions, access to medical care, and cultural practices regarding bathing and emollient use therefore influence disease course.  

Lifestyle factors such as clothing choice, occupational activities, and climate also modulate symptom burden. In hot climates, sweating and occlusion under clothing can increase maceration and blistering, whereas in cold, dry environments xerosis may aggravate fissuring and pain.[4][13][18] Patients often adopt strategies to minimize friction and heat—such as wearing soft, loose garments, avoiding vigorous physical contact sports, and living in temperature-controlled environments—to reduce disease flares.[13][17][18] No data currently implicate toxins, radiation, or specific dietary components as primary causes, but nutritional status and hydration are clearly important in managing skin barrier dysfunction and preventing complications.[4][17][18]  

### 2.4 Protective Factors and Gene–Environment Interactions

Documented **protective factors** in EHK2 primarily relate to optimized skin care and avoidance of physical stress rather than intrinsic genetic protection. Systematic reviews and European guidelines on congenital ichthyoses emphasize that multidimensional therapy—including hydration, lubrication, keratolytic agents, and careful infection control—can substantially reduce symptoms and improve quality of life, thereby functioning as environmental modifiers that protect against disease exacerbation.[17][18] Long baths to hydrate and soften hyperkeratotic skin, lubrication with oils and ointments, humidification of indoor environments, and routine antiseptic measures (e.g., bleach baths) are described as critical interventions that limit skin damage and infection in ichthyoses, including epidermolytic ichthyosis.[4][17][18]  

At the genetic level, **complete absence of K10** appears, paradoxically, to confer relative protection against the severe dominant phenotype, as demonstrated in K10-null mice that develop a structurally intact epidermis without significant fragility, in contrast to transgenic mice expressing mutant K10 that show epidermolytic hyperkeratosis and neonatal lethality.[15][16] The K10-null mouse study concluded that “the deletion of K10, which is the most abundant epidermal protein, does not lead to epidermal fragility,” suggesting that persistence of K5/K14 suprabasally and altered keratin filament composition can maintain epidermal integrity in the absence of K10.[15] In humans, recessive K10-null mutations cause a distinct EI phenotype that may be severe but mechanistically lacks dominant-negative filament disruption, illustrating a gene–environment interplay in which the cellular keratin network adapts to loss-of-function but not to misfolded, aggregation-prone proteins.[12][13][15][16]  

Gene–environment interactions in EHK2 thus involve the interplay between **keratin network resilience or compensatory expression** and **external mechanical and microbial stressors**. Dominant-negative *KRT10* variants predispose suprabasal keratinocytes to cytolysis under mechanical load, and environmental friction directly tests the integrity of these compromised cell layers, resulting in blistering.[4][16] Conversely, in recessive K10 loss-of-function, cellular compensatory mechanisms involving K5/K14 and K1 may be sufficient to withstand moderate stress, but extreme environmental challenges such as infection or severe dehydration can reveal vulnerability, particularly in neonates with collodion-like presentation.[12][13][15] Future multi-omics studies may uncover additional molecular protective factors, such as upregulation of stress keratins or barrier lipids, that buffer disease severity under different environmental conditions.[13][15][16]  

Overall, the etiologic picture of EHK2 is dominated by *KRT10* mutations, with de novo and inherited variants conferring high genetic risk, consanguinity amplifying recessive risk, and environmental factors—especially friction, heat, and infection—modulating clinical expression within the constraints imposed by the underlying keratin network pathology.[3][4][11][12][13][14][17][18][20]  

## 3. Phenotypes

### 3.1 Neonatal and Early-Life Phenotypic Presentation

The **neonatal phenotype** of Epidermolytic Hyperkeratosis 2 is characterized by generalized skin fragility, erythema, and blistering, accompanied by erosions and superficial ulceration. MedlinePlus reports that affected babies may have very red skin (erythroderma) and severe blisters at birth, and notes that because they lack the protection provided by normal skin, they are at risk of dehydration and infections, including potentially life-threatening sepsis.[3] DermNet similarly describes that epidermolytic ichthyosis typically presents at birth with widespread erythroderma, skin fragility, blisters, and peeling or denuded skin after minor friction; the lesions are often superficial but can be extensive and painful.[4] Orphanet’s summary of autosomal dominant EI emphasizes a blistering phenotype at birth that progressively becomes hyperkeratotic over time, and the clinical spectrum study of keratinopathic ichthyoses corroborates that EI manifests with congenital blistering and erosions with variable erythroderma.[13][20]  

In **autosomal recessive EHK2B**, neonatal presentation can be even more dramatic. The BJD report on lethal autosomal recessive EI due to a *KRT10* donor splice-site mutation described a newborn with severe generalized erythroderma, erosions, and skin breakdown; the infant died early despite intensive care, underscoring the potential for neonatal lethality.[12] The genotype–phenotype study documented several recessive EI cases with collodion presentation at birth, characterized by a tight, shiny membrane encasing the neonate, which later evolves into hyperkeratotic plaques, reflecting a severe disturbance of cornification from the earliest developmental stages.[14][2][13] In clinical practice, such presentations require differential diagnosis against other congenital ichthyoses, epidermolysis bullosa, and syndromic genodermatoses, making histopathology and genetic testing crucial.[4][20]  

Age of onset for EHK2 is thus **neonatal**, with lesions apparent at or soon after birth. Symptom severity in the first days and weeks is typically **moderate to severe**, depending on the specific *KRT10* mutation and inheritance pattern, with recessive null variants tending toward more severe and sometimes lethal phenotypes.[12][13][14] The progression during infancy involves partial healing of erosions and diminished blistering, but persistent erythema and initiation of hyperkeratosis along flexural surfaces, neck, and other high-friction regions.[3][4][9][13] From an HPO standpoint, key neonatal phenotypes include *erythroderma*, *skin blistering*, *erosions*, *collodion baby* in recessive forms, and *neonatal skin fragility*—all of which significantly impair barrier function and homeostasis.[3][4][12][13][20]  

### 3.2 Evolution to Hyperkeratosis and Later Cutaneous Manifestations

As affected individuals with EHK2 age, the phenotype undergoes a well-documented shift from **fragility and blistering** toward **persistent hyperkeratosis**. MedlinePlus notes that in subsequent months after birth, erythema and blistering improve, but patients develop hyperkeratotic thickening especially along joint flexures, on areas where skin comes into contact with itself, and on the scalp or neck.[3] DermNet describes that hyperkeratosis gradually replaces erosions, with thickened, verrucous or ridged plaques in flexural areas, often accompanied by palmoplantar keratoderma in many EI cases, though palm involvement is less common in *KRT10*-associated EHK2.[4][13][14] The clinical spectrum study confirms that blistering becomes less frequent later in life while hyperkeratosis increases, and that the distribution and severity of hyperkeratosis vary with genotype, including more localized or intermediate patterns.[13]  

Hyperkeratotic skin in EHK2 tends to be **thick, darkened, and malodorous**, with a texture that may be ridged or verrucous. MedlinePlus notes that thickened skin is usually darker than normal, and bacteria can grow in the thick skin, often causing a distinct odor, contributing to social stigmatization and quality-of-life impairment.[3] DermNet lists typical features such as hyperkeratosis of flexural folds, trunk, and extremities, sometimes with spiky or hystrix-like scaling, and palmoplantar keratoderma particularly in *KRT1*-mutant cases.[4] In *KRT10*-driven EHK2, the non-palmoplantar subtype is common, but exceptions exist, and some patients show focal palmoplantar hyperkeratosis or keratotic papules on hands and feet.[3][14]  

Symptom **progression** in EHK2 is generally **chronic and lifelong**, with blistering episodes becoming episodic and less frequent but hyperkeratosis persisting or worsening with age.[3][4][9][13] Severity can range from mild localized keratosis with occasional erosions to extensive, disabling hyperkeratotic plaques with recurrent infections and pain. The clinical spectrum study quantified disease burden using scoring tools and found substantial heterogeneity, with some individuals reporting moderate impact and others severe disability.[13] Quality-of-life impact is considerable: patients may require daily intensive skin care, face social isolation due to appearance and odor, experience limitations in physical activities, and suffer from chronic discomfort or pruritus.[4][13][17][18]  

Suggested HPO terms for these later phenotypes include *hyperkeratosis*, *hyperpigmented skin lesions*, *palmoplantar keratoderma* (when present), *recurrent skin infections*, *malodor*, and *pruritus*, each with variable frequency among affected individuals.[3][4][9][13][20] For EHK2 specifically, **non-palmoplantar generalized hyperkeratosis** is a hallmark in most autosomal dominant cases, while **collodion baby with subsequent hyperkeratosis without palmoplantar involvement** defines autosomal recessive K10-null disease.[2][12][13][14]  

### 3.3 Variability, Subtypes, and Mosaic Manifestations

Phenotypic expression in EHK2 is notably **variable**, influenced by mutation type, zygosity, mosaicism, and environmental factors. The genotype–phenotype correlation study observed a broad spectrum of manifestations and severity across patients with *KRT10* mutations, ranging from superficial blistering with mild keratosis to extensive hyperkeratosis with severe blistering and erythroderma.[14] The authors identified mutational hotspots in *KRT10* and found that helix boundary mutations typically produce more severe phenotypes, whereas some rod domain or tail variants lead to milder disease, reflecting differences in dominant-negative impact on filament assembly.[14][13]  

Mosaic manifestations, known clinically as **epidermolytic nevi**, arise when postzygotic *KRT10* mutations occur in keratinocyte progenitors during embryogenesis. DermNet notes that epidermolytic ichthyosis is the only keratin disease associated with genetic mosaicism, and that offspring of parents with epidermolytic epidermal nevi can develop generalized EI if gonadal tissue is involved, representing germline mosaicism.[4] The genotype–phenotype study included patients with epidermolytic nevi harboring *KRT10* mutations such as p.Arg156His, who exhibited linear keratotic papules along Blaschko’s lines, reflecting somatic mosaic patterns.[14] These mosaic forms often present with localized hyperkeratotic streaks or plaques, without generalized disease, but they pose a reproductive risk when the mutation is present in germ cells, effectively making the parent a somatic–gonadal mosaic.[4][13][14]  

Phenotypic **expressivity** in autosomal dominant EHK2A is therefore highly variable, from mild localized keratosis to severe generalized disease, while penetrance is generally complete—i.e., individuals carrying heterozygous *KRT10* mutations typically show some clinical features.[4][9][13][14][20] In autosomal recessive EHK2B, expressivity includes lethal neonatal erythroderma, collodion presentation, and intermediate localized disease, but phenotype remains distinct from dominant forms because loss-of-function removes K10 without producing aberrant filaments.[12][13][14][15]  

### 3.4 Quality of Life and Psychosocial Impact

The **quality-of-life impact** of EHK2 is profound and multifaceted. Orphanet and DermNet emphasize that patients who survive the neonatal period continue to experience episodes of infection, skin fragility, and blistering throughout their lives, along with psychological stress and social isolation associated with visible skin lesions and malodor.[4][13][20] The clinical spectrum and burden study explicitly aimed to quantify disease burden, demonstrating that keratinopathic ichthyoses exert significant physical, emotional, and social impacts, including limitations in mobility, daily activities, interpersonal relationships, and employment.[13]  

Thick, malodorous hyperkeratotic plaques interfere with clothing, heat regulation, and body image, while chronic erosions and blistering cause pain and limit physical activity, particularly in children.[3][4][13][17][18] Recurrent infections necessitate frequent medical visits and sometimes hospitalizations, and the fear of sepsis in neonates imposes emotional strain on families.[3][12][13] Parents of affected infants must perform intensive caregiving tasks, including daily bathing, application of emollients and keratolytics, infection surveillance, and coordination of multidisciplinary care, which can be exhausting and financially burdensome.[17][18]  

Validated quality-of-life instruments such as the Dermatology Life Quality Index (DLQI), SF-36, or disease-specific ichthyosis QoL scales have been applied in some cohorts, demonstrating reductions across domains of physical functioning, emotional well-being, and social participation.[13][18] HPO terms related to quality of life, such as *impaired quality of life*, *social isolation*, and *chronic pain*, are appropriate for annotating the broader phenotypic impact of EHK2 beyond cutaneous signs.[13][17][18]  

Taken together, the phenotypic profile of Epidermolytic Hyperkeratosis 2 encompasses congenital erythroderma, blistering, erosions, and collodion presentation in some recessive cases, evolving into variable patterns of hyperkeratosis, pigmentary change, malodor, infection, and psychosocial distress, with significant impairment of daily functioning and quality of life that persists across the lifespan.[3][4][9][12][13][14][17][18][20]  

## 4. Genetic and Molecular Information

### 4.1 The *KRT10* Gene and Keratin 10 Protein

The **KRT10 gene** encodes keratin 10, a type I intermediate filament protein that pairs with keratin 1 (K1, encoded by *KRT1*) to form heterodimeric filaments in suprabasal layers of the epidermis.[8][4][13][14] MedlinePlus Genetics identifies *KRT10* as a gene on chromosome 17, and OMIM places autosomal dominant EHK2A at 17q21.2, with *KRT10* as the causative gene.[8][11] Keratin 10 is synthesized in spinous and granular layer keratinocytes and contributes to the dense network of tonofilaments that provide mechanical resilience to suprabasal cells; this network is critical for withstanding mechanical stress and maintaining epidermal integrity.[4][12][14][16]  

Structurally, K10—like other type I keratins—features a central α-helical rod domain flanked by non-helical head and tail domains, with conserved helix boundary motifs at the 1A/1B and 2A/2B transitions that are crucial for filament assembly.[14][15][16] Mutations in these boundary motifs disrupt coiled-coil formation and heterodimerization with K1, leading to disorganized filaments, keratin clumping, and cell fragility.[12][14][16] The K10 protein is highly expressed, making up a substantial fraction of epidermal protein content, and its loss or dysfunction has major consequences for terminal differentiation and cornification.[15][16]  

The *KRT10* gene is catalogued in many genomic databases, with OMIM entry 148080 (“KERATIN 10, TYPE I; KRT10”) listing associated conditions such as epidermolytic ichthyosis and ichthyosis with confetti.[8][10][11][13][14] ClinVar contains numerous variant entries for *KRT10* associated with epidermolytic ichthyosis, many classified as pathogenic or likely pathogenic based on clinical and functional evidence.[19][8][13][14] Genomic sequencing in EI cohorts typically covers exons 1–7 of *KRT10*, which contain most known pathogenic variants, particularly in the rod domain.[14]  

From a Gene Ontology perspective, K10 participates in biological processes such as keratinization, epidermis development, and response to mechanical stimulus, and localizes to the cytoplasmic intermediate filament network (GO:0005882, intermediate filament; GO:0005829, cytosol). Keratin 10 is expressed in keratinocytes (CL:0000312), especially suprabasal epidermal keratinocytes located in skin (UBERON:0002097) and the epidermis (UBERON:0001003).[13][14][15][16]  

### 4.2 Pathogenic Variant Classes in *KRT10*

Pathogenic variants in *KRT10* causing EHK2 fall into two main mechanistic classes: **dominant-negative missense or in-frame variants** and **loss-of-function (null) variants**. DermNet and OMIM report that autosomal dominant EI/EHK 2A is caused by heterozygous missense mutations in *KRT10*, often at highly conserved residues in the helix boundary motifs.[4][11][14] The genotype–phenotype study identified multiple *KRT10* missense mutations (e.g., p.Met150Thr, p.Met150Arg, p.Arg156His, p.Tyr449Cys) that affect critical sites in the rod domain and result in dominant disease.[14] These missense changes produce structurally aberrant K10 proteins that incorporate into filaments and disrupt their architecture, leading to keratin clumping and cytolysis—classic dominant-negative behavior.[12][14][16]  

In contrast, autosomal recessive EI/EHK2B arises from **frameshift, nonsense, or splice-site mutations** that abolish K10 expression. The lethal recessive EI case report identified a homozygous G>A substitution affecting the donor splice site of intron 5 (c.1155+5G>A), predicted to impair mRNA splicing and generate a truncated or unstable transcript.[12] The genotype–phenotype study documented recessive EI cases with *KRT10* truncating variants such as c.1300C>T (p.Gln434X) and c.1325insC (p.Lys439fsX6), both found in consanguineous families, and concluded that recessive EI results from loss of keratin 10 expression regardless of mutation location.[14][13]  

ClinVar provides specific examples of pathogenic *KRT10* variants, such as NM_000421.5(KRT10):c.376G>A (p.Gly126Ser), annotated as associated with epidermolytic ichthyosis and epidemic hyperkeratosis.[19] Many ClinVar variants are classified according to ACMG/AMP criteria as pathogenic or likely pathogenic, based on segregation, de novo occurrence, functional data, and consistency with known mutational hotspots.[19][13][14] Variant types include missense, nonsense, frameshift, splice-site, and occasionally small in-frame insertions or deletions, with most autosomal dominant disease arising from missense alterations in helix boundaries and most recessive disease arising from truncating or splice-disrupting changes that lead to nonsense-mediated decay or non-functional protein.[12][14][15][16]  

Allele frequencies of these pathogenic variants in population databases such as gnomAD are not detailed in the current search results, but given their severe phenotypic consequences and early detection, they are expected to be extremely rare (minor allele frequencies far below 0.001).[13][20] The distinction between **germline** and **somatic (postzygotic)** origin is crucial in mosaic EHK2; epidermolytic nevi result from somatic mutations in *KRT10* confined to skin segments, while generalized EI/EHK arises from germline mutations present in all cells.[4][13][14]  

### 4.3 Functional Consequences: Dominant-Negative vs Loss-of-Function

Functional studies in animal models and human tissues demonstrate that **dominant-negative K10 mutations** and **loss-of-function K10 mutations** have markedly different biological consequences. In transgenic mice expressing a mutant keratin 10 gene, researchers observed an epidermolytic hyperkeratosis phenotype, including cytolysis of suprabasal keratinocytes, induction of hyperproliferative keratins, and perinatal lethality, suggesting that a defect in suprabasal cells can stimulate basal cell proliferation and that intermediate filament perturbation has profound effects on nuclear morphology and cytokinesis.[16] The authors concluded that transgenic mice expressing mutant K10 recapitulate the human EH phenotype and strongly implicate *KRT10* and *KRT1* mutations as the likely genetic basis of epidermolytic hyperkeratosis.[16]  

In contrast, K10-null mice engineered to completely lack keratin 10 expression formed a normal stratified epidermis without signs of fragility or wound-healing response; suprabasal keratin filaments were composed of K5/K14 that persisted suprabasally at elevated protein levels despite mRNAs remaining restricted to basal keratinocytes, indicating a novel mechanism regulating keratin turnover and filament composition.[15] The authors noted that the amount of K1 was reduced and a small amount of novel K1/14/15 filaments formed, but epidermal integrity was maintained and cytolysis absent, leading to the conclusion that filaments with K1/K10 are not essential for suprabasal integrity in mice and that deletion of K10 does not induce epidermal fragility or up-regulation of hyperproliferative keratins K6 and K17.[15]  

These findings align with human clinical observations. Dominant missense *KRT10* mutations cause EI/EHK2 by producing mutant K10 that destabilizes the K1/K10 filament network, leading to keratin clumps, perinuclear aggregates, and cell lysis in suprabasal layers—classic **dominant-negative** behavior.[4][5][12][14][16] Recessive *KRT10* mutations, in contrast, abolish K10 expression and allow compensatory expression of other keratins, producing a distinct phenotype with collodion presentation and later hyperkeratosis but without the same degree of cytolysis, at least in mice; human recessive EI can be severe due to additional factors such as inflammatory responses or impaired cornification pathways.[12][13][15]  

Quoting the K10-null mouse study:  

> “In conclusion, we have demonstrated that the deletion of K10, which is the  
> most abundant epidermal protein, does not lead to epidermal fragility or to the  
> up-regulation of the hyperproliferative keratins 6 and 17.”[15]  

and the transgenic mutant K10 study:  

> “We have discovered that transgenic mice expressing a mutant keratin 10 gene  
> have the EH phenotype, thereby suggesting that a genetic basis for human EH  
> resides in mutations in genes encoding suprabasal keratins K1 and K10.”[16]  

These experimental observations provide strong functional evidence that the pathogenic mechanism in autosomal dominant EHK2A is **dominant-negative disruption of K1/K10 filaments**, whereas autosomal recessive EHK2B arises from **loss-of-function** and altered compensatory keratin expression, explaining differences in phenotype, inheritance, and severity.[12][13][14][15][16]  

### 4.4 Modifier Genes, Epigenetics, and Chromosomal Abnormalities

To date, **no specific modifier genes** have been conclusively shown to alter EHK2 severity, although the diversity of clinical manifestations among individuals with identical *KRT10* mutations suggests the presence of genetic or epigenetic modifiers.[13][14] Potential candidates include other keratin genes (*KRT1*, *KRT2*, *KRT5*, *KRT14*) and genes involved in desmosomal adhesion, cornified envelope formation, or lipid barrier synthesis, but direct evidence remains lacking in the current literature.[13][15][16] Epigenetic regulation of keratin gene expression, such as DNA methylation or histone modifications affecting *KRT10* transcription, may also influence disease expression, particularly in mosaic forms, but specific epigenetic patterns have not been described in EI/EHK2 studies.[13]  

No **large-scale chromosomal abnormalities** (aneuploidy, translocations, inversions) have been linked to EHK2; disease arises from point mutations or small indels in *KRT10* within otherwise normal karyotypes.[11][14][19] Cytogenetic locations are well defined (17q21.2 for *KRT10*), and there is no evidence of structural genomic rearrangements contributing to this condition.[10][11][13]  

Thus, genetic and molecular information in EHK2 centers on *KRT10* variants and their dominant-negative or loss-of-function effects, with potential but as yet undefined contributions from modifier genes and epigenetic regulation that may shape the spectrum of keratin expression and filament architecture in affected skin.[12][13][14][15][16][19]  

## 5. Environmental Information

### 5.1 Non-Genetic Factors Influencing Disease Expression

EHK2 itself is not caused by environmental insults, but **non-genetic factors substantially modulate symptom severity and complication risk**. Clinical reviews and guidelines highlight that environmental humidity, temperature, clothing, and mechanical trauma influence skin fragility and blistering episodes.[4][13][17][18] High temperatures and humidity can promote sweating, maceration, and bacterial growth, exacerbating erosions and infections, while low humidity and cold climates may worsen xerosis and fissuring, leading to pain and impaired mobility.[4][13][18]  

Mechanical trauma, including rubbing, scratching, and pressure from clothing or shoes, is particularly important in early life, as suprabasal keratinocytes in EHK2 are prone to cytolysis under mechanical load due to compromised filament networks.[4][16] Caregivers are advised to minimize friction through soft clothing, careful handling, and avoidance of adhesive dressings that might tear fragile skin.[17][18] In older children and adults, physical activities that involve repetitive friction or trauma, such as contact sports or manual labor, may precipitate erosions and require adaptation of lifestyle and occupational choices.[13][17][18]  

### 5.2 Infectious and Microbial Influences

Infections, particularly **bacterial skin infections**, represent a key environmental factor in EHK2. MedlinePlus notes that bacteria can grow in thickened hyperkeratotic skin, often causing a distinct odor, and DermNet recommends antiseptic measures such as chlorhexidine washes and sodium hypochlorite (bleach) baths to reduce microbial load and prevent infection.[3][4] The systemic retinoids review and European guidelines emphasize that infection control is central to managing ichthyoses, including prophylactic or therapeutic use of topical and systemic antibiotics when necessary, and that unchecked infection can evolve into sepsis, especially in neonates with extensive erosions.[17][18]  

The skin microbiome in EHK2 has not been extensively profiled, but the presence of thick plaques, impaired barrier function, and recurrent erosions likely alters microbial composition and may predispose to colonization by *Staphylococcus aureus* and other opportunistic pathogens.[4][13][17] In neonates, hospital-acquired infections may occur if barrier care is inadequate, and management in specialized neonatal intensive care settings with infection control protocols can substantially influence survival.[12][18]  

### 5.3 Lifestyle, Nutrition, and Care Environment

Lifestyle factors such as **bathing practices, emollient use, and ambient humidity** strongly affect EHK2 manifestation and long-term outcomes. The systemic retinoids review notes that therapy for ichthyoses is usually multidimensional, including humidification with long baths, scale removal by gentle abrasives, lubrication with oils and creams applied to wet skin, and environmental humidification.[17] European guidelines stress the importance of structured topical therapy plans and caregiver education in congenital ichthyoses, advocating for regular follow-up and adjustment of regimens as patients age.[18] These practices directly modulate disease expression, reducing fissuring, pain, and infection risk, and thus can be considered environmental protective factors.  

Nutrition and hydration also play roles. Adequate hydration is crucial in neonates with extensive skin loss to prevent dehydration and electrolyte imbalance, and energy requirements may be increased in severe EI due to hypermetabolism associated with chronic skin inflammation and repair.[3][12][17][18] Malnutrition or failure to thrive can exacerbate overall morbidity and should be addressed in multidisciplinary care frameworks. No specific dietary components are known to alter keratin expression or disease severity, but general nutritional support remains fundamental to resilience against infection and wound healing.[17][18]  

In summary, environmental influences in EHK2 revolve around mechanical, thermal, microbial, and care-related factors that do not cause the disease but substantially shape its clinical trajectory, highlighting the necessity of comprehensive supportive environments to minimize disease burden.[3][4][13][17][18]  

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

The mechanistic sequence leading from *KRT10* mutation to EHK2 clinical features can be summarized as follows within a single causal chain. First, pathogenic germline or postzygotic variants in *KRT10* arise, either heterozygous dominant-negative missense mutations or biallelic loss-of-function changes in the gene encoding keratin 10, which alters keratin 10 protein structure or expression and thereby perturbs the formation of K1/K10 heterodimers in suprabasal keratinocytes.[11][12][13][14][15][16] Second, the resulting defective or absent K1/K10 complexes lead to disorganized intermediate filament networks, keratin clumping, and impaired cytoskeletal integrity in suprabasal cells, which in turn causes mechanical fragility and cytolysis under physiological stress, as demonstrated in human histopathology and transgenic mouse models; this step is directly observed in electron microscopy and inferred from filament assembly studies.[4][5][12][15][16] Third, the cytolysis of suprabasal keratinocytes results in epidermolytic changes characterized by vacuolization, perinuclear keratin aggregates, and breakdown of the spinous and granular layers, leading to clinical blistering, erosions, and erythema, particularly in neonates exposed to mechanical friction; this process is well documented histologically and clinically.[4][5][12][13][20] Fourth, the epidermal damage and barrier disruption elicit inflammatory and wound-healing responses, including induction of hyperproliferative keratins (such as K6 and K16), altered differentiation programs, and increased keratinocyte turnover, which over time produces thickened hyperkeratotic stratum corneum and scaling, as inferred from gene expression studies and animal models.[15][16][13] Fifth, chronic hyperkeratosis, coupled with persistent barrier defects and recurrent microtrauma, fosters microbial colonization, particularly by bacteria, resulting in malodor, recurrent infections, and risk of systemic sepsis, especially in early life, which contributes to morbidity and sometimes mortality.[3][4][13][17] Finally, these cumulative cutaneous changes and complications interfere with thermoregulation, hydration, mobility, and social functioning, causing chronic pain, psychosocial distress, and reduced quality of life, as demonstrated in clinical burden studies and patient-reported outcomes.[13][17][18]  

This causal chain underscores that **mutations in *KRT10*** are upstream events that initiate a cascade of molecular, cellular, tissue, and systemic processes culminating in the characteristic clinical manifestations of Epidermolytic Hyperkeratosis 2.[11][12][13][14][15][16]  

### 6.2 Keratin Intermediate Filament Biology and Molecular Pathways

At the **molecular level**, EHK2 pathophysiology centers on disruption of the epidermal intermediate filament network. Keratins are the major structural proteins of epithelial cells, assembling into obligate heterodimers of type I and type II keratins that polymerize into filaments providing mechanical resilience.[4][12][14][15][16] In suprabasal epidermis, K1 (type II) and K10 (type I) form the principal heterodimer, replacing basal K5/K14 as keratinocytes differentiate and migrate outward.[4][14][15][16] Mutations in *KRT10*, particularly in conserved helix boundary motifs of the rod domain, alter the ability of K10 to form proper coiled-coil structures with K1 and thereby impair filament assembly.[12][14][16]  

DermNet notes that mutations in KRT1 and KRT10 lead to “variable disruption and decreased stability of the K1/K10 tonofilaments and hyperkeratosis due to lack of desquamation,” emphasizing that impaired filament stability both compromises mechanical function and alters terminal differentiation.[4] In autosomal dominant EHK2A, mutant K10 incorporates into filaments, leading to misaligned, clumped, or fragmented filaments and creating large perinuclear aggregates observed in electron microscopy.[4][5][12][15][16] This disorganization affects cytoskeletal linkage to desmosomes and other cell–cell junctions, weakening tissue cohesion and making suprabasal layers prone to mechanical failure.  

Molecular pathways downstream of filament disruption include activation of stress and differentiation pathways. Transgenic mice expressing mutant K10 show induction of hyperproliferative keratins (e.g., K6/16), increased basal cell proliferation, and evidence of aberrant cytokinesis and nuclear shape distortion, indicating that intermediate filament perturbation can signal to cell cycle machinery and nuclear architecture.[16] These changes likely involve pathways such as MAPK and NF-κB, which respond to mechanical and inflammatory stress, though direct mapping in EI is not yet fully elaborated. The K10-null mouse study revealed compensatory persistence of K5/K14 in suprabasal layers at elevated protein levels, suggesting upregulation of basal keratin expression or altered protein turnover to restore filament networks in the absence of K10.[15]  

From a Gene Ontology perspective, the key biological processes implicated include *epidermis development*, *keratinization*, *cornification*, *response to mechanical stimulus*, *cell adhesion*, and *regulation of cell proliferation*.[13][14][15][16] At the signaling pathway level (KEGG, Reactome), intermediate filament perturbations may intersect with pathways regulating cytoskeletal dynamics, cell junctions, and inflammatory responses, though specific pathway mapping (e.g., Wnt, MAPK, PI3K-AKT) in EHK2 remains an area for future research.[13][15][16]  

### 6.3 Cellular Processes: Cytolysis, Differentiation, and Inflammation

At the **cellular level**, EHK2 is characterized by cytolysis of suprabasal keratinocytes, altered differentiation, and chronic mild inflammation. Histopathology of epidermolytic hyperkeratosis shows hyperkeratosis with orthokeratosis, hypergranulosis, and cytolysis in the upper stratum spinosum and granular layers, with characteristic intracellular vacuolization and perinuclear keratin clumps.[5][20][13] Electron microscopy reveals suprabasal keratinocytes filled with coarse keratin filament aggregates and vacuoles, and perinuclear clumps in the upper epidermis.[5][20][13] These findings indicate that the intermediate filament cytoskeleton is severely disrupted, leading to structural failure and cell death.  

Cytolysis can occur through mechanical rupture when weakened cells are subjected to friction or shear forces, or through apoptosis triggered by cytoskeletal damage and stress signaling. Transgenic mutant K10 mice show strong induction of wound-healing responses and hyperproliferative keratins, implying that epidermal damage stimulates basal cell proliferation and possibly inflammatory cytokine release.[16] Hypergranulosis and thickened stratum corneum in human EI/EHK reflect altered differentiation programs, with keratinocytes undergoing abnormal cornification and retention in the cornified layer, contributing to hyperkeratosis and scaling.[4][5][13]  

Inflammation in EHK2 is generally mild to moderate but can be exacerbated by infections and erosions. Erythema in neonates and older individuals likely reflects vascular and immunologic responses to barrier disruption and microbial stimuli, involving cytokines such as IL-1, TNF-α, and chemokines that recruit immune cells to damaged skin.[3][4][13] Although EI/EHK is not primarily an inflammatory dermatosis like psoriasis or atopic dermatitis, chronic barrier defects and mechanical injury may induce a low-grade inflammatory milieu that influences itch, pain, and secondary tissue remodeling.[13][17][18]  

Cell types involved include **suprabasal epidermal keratinocytes** (CL:0000312) as primary cells affected by K10 dysfunction, **basal keratinocytes** that proliferate in response to suprabasal damage, **immune cells** such as neutrophils and macrophages that respond to infection and tissue injury, and **fibroblasts** that support dermal repair.[13][15][16] Desmosomes and cornified envelope proteins (e.g., involucrin, loricrin) may be secondarily affected by filament disruption, altering cell–cell adhesion and barrier function.[4][13]  

### 6.4 Tissue-Level Pathology and Barrier Dysfunction

At the **tissue level**, EHK2 produces a distinctive pattern of epidermal pathology termed **epidermolytic hyperkeratosis**, captured in the name of the condition. DermNet’s pathology description notes that epidermolytic hyperkeratosis is characterized by marked hyperkeratosis in the stratum corneum, hypergranulosis, and vacuolization with clumped keratin filaments in the upper spinous and granular layers.[5] Orphanet reports that histological examination in EI shows hyperkeratosis with orthokeratosis, hypergranulosis, and cytolysis in the upper layers, and electron microscopy reveals perinuclear keratin clumps.[20]  

These tissue-level changes translate to **barrier dysfunction**. Although the stratum corneum is thickened, its structural organization is abnormal, with disrupted lipid lamellae and corneocyte cohesion, resulting in increased transepidermal water loss and vulnerability to trauma and infection.[3][4][13][17] Neonates with EI/EHK lack effective barrier function, leading to rapid dehydration and high risk of electrolyte derangement; management centers on hydration, lubrication, and careful monitoring.[3][4][17][18] As hyperkeratosis develops, barrier function improves somewhat, but fissures and erosions remain, and the thick superficial layers impede normal desquamation and can trap heat and microbes.[4][13]  

Tissue damage mechanisms in EHK2 encompass **mechanical stress** leading to cytolysis, **microbial invasion** through erosions, and **chronic frictional trauma** in flexural sites and areas of skin-to-skin contact. DermNet notes that minor friction can cause peeling, erosions, and denuded skin, and emphasizes that palmoplantar keratoderma may develop, particularly in KRT1-mutant disease, but is less typical in pure KRT10 EHK2.[4] The clinical spectrum study documented localized and generalized patterns of hyperkeratosis, with flexural, truncal, and extremity involvement variably affecting function and comfort.[13]  

Suggested UBERON terms for anatomical localization include *skin* (UBERON:0002097), *epidermis* (UBERON:0001003), *palm of hand* (UBERON:0001510), *sole of foot* (UBERON:0001509), and *scalp skin* (UBERON:0001511), reflecting common sites of involvement.[4][13][20] Tissue-level pathology in EHK2 is thus characterized by epidermolytic changes in suprabasal layers, hyperkeratosis, hypergranulosis, and barrier impairment that collectively underpin the clinical picture of fragility, blistering, and thickened plaques.[4][5][13][20]  

### 6.5 Biochemical Abnormalities and Metabolic Changes

Biochemical abnormalities in EHK2 are largely **structural and protein-based** rather than enzymatic or metabolic per se. K10 mutations disrupt protein folding and assembly into intermediate filaments, leading to protein aggregation and altered proteostasis.[4][12][14][15][16] These aggregates may be poorly degraded by proteasomes or autophagy pathways, contributing to cytosolic stress and potential activation of unfolded protein response mechanisms, although specific evidence for UPR activation in EI is limited.[13][15][16]  

Keratins themselves are not enzymes, but their misfolding may alter cellular metabolism indirectly, for example by changing cytoskeletal organization and intracellular trafficking, or by promoting inflammatory signaling that affects energy metabolism in skin.[13][16] The thickened stratum corneum may have altered lipid composition and desquamation dynamics, with accumulation of corneocyte aggregates and retained corneodesmosomes, but detailed lipidomics or metabolomics signatures for EHK2 have not been reported.[4][13]  

No clear epigenetic changes have been documented specifically in EHK2, but given the regulatory complexity of keratin gene expression, DNA methylation and histone modifications likely play roles in tissue-specific expression patterns and compensatory responses to K10 loss, especially in recessive disease where K5/K14 persist suprabasally.[15][16][13] Future multi-omics integration, including transcriptomics and proteomics of EI skin, may elucidate gene expression changes beyond keratins—for example, upregulation of stress-response genes, cytokines, and cornified envelope proteins—that contribute to disease mechanisms.[13]  

### 6.6 Immune System Involvement and Inflammatory Mechanisms

The **immune system** plays a secondary but important role in EHK2, primarily through responses to barrier disruption and microbial invasion. Erythema and erosions in neonates and older patients reflect vasodilation and infiltration of inflammatory cells such as neutrophils, macrophages, and lymphocytes into damaged skin.[3][4][13] Infections superimposed on erosions can trigger robust inflammatory responses, leading to pain, swelling, and systemic symptoms, and sepsis in severe cases.[3][12][17][18]  

While EHK2 is not classically considered an autoimmune or primary inflammatory dermatosis, chronic low-grade inflammation is a feature of hyperkeratotic skin exposed to constant microtrauma and colonized by bacteria. This inflammatory milieu can influence keratinocyte proliferation and differentiation, potentially exacerbating hyperkeratosis and pruritus.[13][17][18] Cytokines such as IL-1β, TNF-α, and IL-6, as well as chemokines, are likely involved in these responses, though specific profiling in EI/EHK has not yet been extensively published.[13]  

Immune cells thus act downstream of keratin defects, responding to tissue damage rather than initiating disease. CL ontology terms for relevant cell types include *keratinocyte* (CL:0000312), *neutrophil* (CL:0000775), *macrophage* (CL:0000235), and *T cell* (CL:0000084), which may be recruited to EHK lesions.[13][17][18] Immune-mediated treatments such as systemic immunosuppressants are not standard in EHK2; instead, infection control and barrier repair remain the primary methods of modulating inflammation.[4][17][18]  

### 6.7 Advanced Molecular Profiling and Future Mechanistic Insights

Advanced technologies such as **transcriptomics, proteomics, and single-cell analysis** have only begun to be applied to keratinopathic ichthyoses but hold promise for deeper mechanistic understanding. The recent clinical spectrum study of EI hints at broader gene expression changes and burden but does not yet detail multi-omics data.[13] Single-cell RNA sequencing of lesional and non-lesional skin could reveal cell-type-specific alterations in keratinocyte states, immune infiltration, and barrier gene expression, while spatial transcriptomics could map the topography of mutant versus wild-type keratin expression in mosaic cases.[13][15][16]  

Functional genomics screens using CRISPR or RNAi in cultured keratinocytes could identify **modifier genes** whose knockdown or overexpression alters the impact of mutant K10 on filament assembly, pointing to potential therapeutic targets.[13][15][16] Proteomics studies may detect changes in desmosomal proteins, cornified envelope components, and stress-response proteins, while lipidomics could characterize alterations in epidermal lipid barrier composition in EI/EHK.[4][13]  

In summary, the mechanistic pathophysiology of Epidermolytic Hyperkeratosis 2 involves *KRT10* mutations disrupting K1/K10 filament assembly, leading to suprabasal cytolysis, epidermolytic histopathology, barrier dysfunction, hyperkeratosis, infection susceptibility, and inflammatory responses that collectively give rise to the clinical phenotype, with dominant-negative and loss-of-function variants producing distinct but overlapping mechanistic cascades.[4][5][11][12][13][14][15][16][17][20]  

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

EHK2 predominantly affects the **skin**, particularly the **epidermis**, across the entire body. DermNet and Orphanet note that epidermolytic ichthyosis presents with generalized erythroderma and blistering at birth, implying widespread cutaneous involvement.[4][13][20] Hyperkeratosis later in life typically affects the trunk, flexural regions, extremities, and in some cases palms and soles, with variability depending on genotype and subtype.[3][4][13][14] There is no direct involvement of internal organs such as heart, lungs, liver, or nervous system; however, systemic complications like dehydration, electrolyte imbalance, and sepsis can indirectly affect multiple organ systems.[3][12][18]  

From an anatomical ontology perspective, primary organ-level terms include **skin** (UBERON:0002097), **integumentary system** (UBERON:0002330), and **epidermis** (UBERON:0001003).[4][13][20] Secondary involvement arises in the **immune system** (UBERON:0002405) due to infection and inflammation, and **circulatory system** (UBERON:0007798) when sepsis occurs, but these are downstream consequences rather than direct targets of *KRT10* mutations.[3][12][17][18]  

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, EHK2 primarily affects the **stratum spinosum and stratum granulosum** of the epidermis, where suprabasal keratinocytes express K1 and K10 and form the main intermediate filament network.[4][5][13][14][15][16] Histopathology in EHK shows cytolysis and vacuolization in these layers, with hypergranulosis and hyperkeratosis in the stratum corneum.[5][20][13] The dermis is relatively spared, though chronic inflammation may induce some dermal changes such as fibrosis or vascular dilation.  

Cell populations targeted include **suprabasal keratinocytes**, which express K10 and are directly affected by its mutation or absence, and **basal keratinocytes**, which respond to suprabasal damage by proliferating and sometimes expressing stress keratins.[4][13][15][16] The CL ontology term *epid

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001510` (1 mention) - the report calls it "palm of hand"; UBERON calls it **skin of knee**
- `UBERON:0001509` (1 mention) - the report calls it "sole of foot"; UBERON calls it **triceps brachii**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000312` (3 mentions) - the report calls it "suprabasal epidermal keratinocytes", "keratinocyte"; CL calls it **keratinocyte**
- `UBERON:0002097` (3 mentions) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0001003` (3 mentions) - the report calls it "epidermis"; UBERON calls it **skin epidermis**, and lists "epidermis" among its other names
- `UBERON:0001511` (1 mention) - the report calls it "scalp skin"; UBERON calls it **skin of leg**, and lists "leg skin" among its other names
- `UBERON:0002330` (1 mention) - the report calls it "integumentary system"; UBERON calls it **exocrine system**, and lists "exocrine glandular system" among its other names
- `UBERON:0007798` (1 mention) - the report calls it "circulatory system"; UBERON calls it **vascular system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000312` - called "suprabasal epidermal keratinocytes", "keratinocyte"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Orphanet`, `OMIM`, `CT`.