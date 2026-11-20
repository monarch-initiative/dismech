---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-06T18:21:07.259619'
end_time: '2026-11-06T18:27:03.296623'
duration_seconds: 356.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: IL6ST-Related Hyper-IgE Syndrome (Autosomal Dominant)
  mondo_id: MONDO:0800131
  category: Mendelian
  causal_genes: IL6ST
  omim_id: OMIM:619752
  synonyms: HIES4A; autosomal dominant IL6ST deficiency
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.5.1
term_validation:
  total_terms: 22
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IL6ST-Related Hyper-IgE Syndrome (Autosomal Dominant)
- **MONDO ID:** MONDO:0800131 (if available)
- **Causal gene(s):** IL6ST
- **OMIM:** OMIM:619752
- **Synonyms:** HIES4A; autosomal dominant IL6ST deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **IL6ST-Related Hyper-IgE Syndrome (Autosomal Dominant)** covering all of the
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

# IL6ST-Related Hyper-IgE Syndrome (Autosomal Dominant): A Comprehensive Disease Overview

IL6ST-related hyper-IgE syndrome (autosomal dominant), also known as hyper-IgE recurrent infection syndrome 4A (HIES4A; OMIM 619752), is a rare Mendelian primary immunodeficiency caused by heterozygous dominant-negative variants in the **IL6ST** gene, which encodes the common cytokine receptor subunit gp130.[1][5][17] This disorder is part of the broader clinical spectrum of hyper-IgE syndromes and closely phenocopies the classical autosomal dominant STAT3-related hyper-IgE syndrome, with patients presenting with markedly elevated serum IgE, eosinophilia, severe eczema, recurrent sinopulmonary and skin infections, and characteristic skeletal and dental abnormalities.[1][6][8][11][16] In 2020, Béziat and colleagues reported 12 patients from eight kindreds with truncating **IL6ST** variants that disrupt gp130’s intracellular recycling motif and STAT3-binding tyrosines, establishing a new form of autosomal dominant (AD) HIES in which mutant gp130 accumulates at the cell surface and exerts a dominant-negative effect on IL-6, IL-11, leukemia inhibitory factor (LIF), and oncostatin M (OSM) signaling.[8][11] Subsequent work in 2023 expanded the allelic and phenotypic spectrum by identifying additional dominant-negative **IL6ST** variants associated with variable clinical expressivity, including milder HIES phenotypes, thereby refining genotype–phenotype correlations and emphasizing the importance of residual gp130 activity in shaping disease severity.[15][16] Mechanistically, IL6ST-related AD HIES illustrates how selective disruption of gp130-dependent cytokine signaling leads to skewed T helper cell differentiation, heightened Th2 responses, modest impairment of Th17 immunity, defective IL-6/IL-11–mediated host defense and bone remodeling, and ultimately to chronic infections, allergic inflammation, and skeletal fragility.[8][11][12][16][19] This report synthesizes current knowledge on disease definition, etiology, clinical phenotypes, molecular mechanisms, diagnostics, management, and research models for IL6ST-related autosomal dominant hyper-IgE syndrome, integrating data from primary case series, mechanistic studies, and contemporary reviews to support ontology-based disease modeling and knowledge-base construction.[1][6][8][11][12][15][16][19]  

---

## 1. Disease Information and Nosology

### 1.1 Overview and core disease definition

IL6ST-related hyper-IgE syndrome (autosomal dominant) is a primary immunodeficiency and immune dysregulation disorder characterized by recurrent predominantly bacterial infections, particularly of the skin and respiratory tract, elevated serum IgE, eosinophilia, eczema, and a constellation of skeletal and dental abnormalities typical of the hyper-IgE syndromes.[1][6][8][11][16] MedGen and OMIM designate this condition as “Hyper-IgE syndrome-4A with recurrent infections (HIES4A), autosomal dominant” and assign OMIM entry 619752; it is also captured in NCBI Gene as a phenotype associated with **IL6ST** and in the broader Orphanet grouping of hyper-IgE syndromes (ORPHA:331223).[1][17][18] The central pathogenic concept is that monoallelic truncating variants in **IL6ST** encode gp130 receptors that retain the extracellular and transmembrane domains but lack the intracellular recycling motif and the four tyrosine residues required for STAT3 recruitment, resulting in a dominant-negative loss of function for several IL-6 family cytokines.[5][8][11][16] Clinically, patients present with features overlapping those of STAT3-dominant-negative HIES, such as recurrent pneumonia with bronchiectasis and pneumatoceles, “cold” Staphylococcus aureus skin abscesses, chronic eczema, skeletal anomalies including scoliosis and osteoporosis, and retention of primary teeth, but they typically preserve an acute-phase response, distinguishing them from autosomal recessive IL6ST deficiency.[6][8][11][12][16] From a nosologic perspective, IL6ST-related AD HIES exemplifies a “phenocopy” of STAT3-HIES arising from upstream receptor dysfunction, and it is part of a growing catalog of monogenic disorders that disturb the IL-6/gp130/STAT3 axis and converge on similar clinical phenotypes.[6][7][8][11][12][16]  

### 1.2 Key identifiers, nomenclature, and synonyms

The principal identifiers for IL6ST-related autosomal dominant hyper-IgE syndrome include OMIM:619752 and MedGen concept C5676920, which both correspond to “Hyper-IgE recurrent infection syndrome 4A, autosomal dominant.”[1][5] NCBI Gene lists **IL6ST** (HGNC-approved symbol) at chromosome 5q11.2 and associates it with “Hyper-IgE recurrent infection syndrome 4, autosomal recessive (HIES4B)” and “Hyper-IgE recurrent infection syndrome 4A, autosomal dominant,” reflecting the existence of both recessive and dominant IL6ST-related disorders.[1][3][17] Although a specific MONDO identifier for HIES4A is not explicitly listed in the sources provided, the disease is encompassed within the broader MONDO/Orphanet category of hyper-IgE syndromes and can be referenced as an IL6ST-associated Mendelian disease within that ontology framework.[17][18] Common synonyms include “IL6ST-related hyper-IgE syndrome, autosomal dominant,” “gp130-dependent hyper-IgE syndrome,” “HIES-AD due to IL6ST dominant-negative variants,” and “autosomal dominant IL6ST deficiency (hyper-IgE phenotype),” although the latter term is somewhat imprecise because the dominant-negative variants do not completely abolish gp130 function.[5][8][11][15][16] At the coding level, the disease is typically captured under ICD-10 categories for primary immunodeficiencies, such as D83 (“Common variable immunodeficiency”) or D84 (“Other immunodeficiencies”), and in clinical practice it may be initially coded under atopic dermatitis (L20) or recurrent pneumonia (J18–J19) before a definitive molecular diagnosis is made.[6][7][8] MeSH does not yet provide a dedicated heading for IL6ST-related HIES, but the disease falls under “Hyperimmunoglobulin E Syndrome” and “Primary Immunodeficiency Diseases,” reinforcing its classification as a monogenic primary immune deficiency with allergic and skeletal features.[6][7][18]  

### 1.3 Evidence sources and aggregation level

Information about IL6ST-related autosomal dominant HIES arises from a combination of aggregated disease-level resources and detailed individual patient reports. OMIM and MedGen entries synthesize clinical and molecular data from the primary literature, particularly case series describing IL6ST variants and associated phenotypes, and present standardized summaries of inheritance, key clinical features, and molecular mechanisms.[1][5][17] The seminal human data come from two major publications: Schwerd et al. (2017) identified a homozygous missense IL6ST variant (p.N404Y) causing autosomal recessive immunodeficiency with craniosynostosis and HIES-like features, while Béziat et al. (2020) described 12 patients with heterozygous truncating IL6ST variants causing autosomal dominant HIES, and Shahin et al. (2019) characterized additional biallelic IL6ST variants underlying recessive HIES.[4][8][11][12][13] A 2023 Journal of Clinical Immunology article by Arlabosse and colleagues expanded the dominant-negative IL6ST variant spectrum and provided detailed immunological and clinical characterization, further enriching the disease description.[15] These patient-level data are supplemented by broader reviews of hyper-IgE syndromes, such as the 2021 update that integrates IL6ST-HIES into the hyper-IgE gene list, and by general gp130 biology reviews, including a 2023 “gp130 expression atlas” that organizes IL6ST-related phenotypes into distinct clinical classes.[6][16] Collectively, this evidence base is relatively small in absolute numbers—fewer than 30 individuals with dominant-negative IL6ST HIES have been reported—but it is rich in mechanistic detail and supported by functional studies in patient cells and in vitro systems, providing high-confidence gene–disease causality and mechanistic insight.[4][8][11][12][13][15][16]  

---

## 2. Etiology, Causal Factors, and Risk Determinants

### 2.1 Primary genetic cause: dominant-negative IL6ST variants

The primary causal factor in IL6ST-related autosomal dominant hyper-IgE syndrome is the presence of a heterozygous truncating variant in **IL6ST**, leading to expression of a mutant gp130 receptor that exerts a dominant-negative effect on IL-6 family cytokine signaling.[5][8][11][16] Béziat et al. identified seven different truncating IL6ST alleles in 12 patients from eight unrelated families, including frameshift and nonsense variants such as p.L708*, p.I719Nfs, p.Y759*, p.T761Ifs*29, p.S754*, and others, all of which preserve the transmembrane domain but delete the distal cytoplasmic tail containing the recycling motif and the four STAT3-recruiting tyrosines.[8][11] Functional assays in patient-derived leukocytes and fibroblasts showed that these mutant gp130 proteins accumulate at the cell surface and interfere with IL-6, IL-11, LIF, and OSM signaling, leading to impaired STAT3 phosphorylation and transcriptional responses, while leaving certain aspects of gp130 signaling, such as residual LIF function, relatively preserved.[5][8][11][16] A 2023 study further identified two additional dominant-negative IL6ST variants, p.Ser731Valfs*8 and p.Arg768*, in three families with HIES; the first lacks the recycling motif and all STAT3-binding residues but is expressed at only slightly increased levels on the cell surface, correlating with milder and variable clinical phenotypes, whereas the second accumulates markedly and is associated with severe disease.[15] These findings underscore that IL6ST-related AD HIES is a **dominant-negative receptoropathy** in which mutant gp130 receptors poison the function of wild-type receptors by forming nonfunctional signaling complexes with IL-6 family cytokines and their specific receptor subunits, thereby selectively disrupting IL-6/IL-11–dependent pathways.[5][8][11][15][16]  

### 2.2 Other IL6ST-related genetic syndromes and their relationship to HIES

IL6ST is increasingly recognized as a pleiotropic disease gene, with distinct classes of variants causing different Mendelian disorders that nonetheless share a common mechanistic foundation in altered gp130 signaling.[5][12][16] Biallelic complete loss-of-function IL6ST variants cause an extended form of Stüve–Wiedemann syndrome (STWS2; OMIM 619751), characterized by dysautonomia, skeletal dysplasia, and perinatal lethality, reflecting near-complete disruption of all gp130-dependent cytokines.[5][16] Biallelic partial loss-of-function IL6ST variants, such as the homozygous p.N404Y missense variant and the P498L and A517P substitutions, preferentially disrupt IL-6 and IL-11 signaling while preserving some LIF activity, leading to autosomal recessive hyper-IgE syndrome (HIES4B; OMIM 618523) with immunodeficiency, craniosynostosis, eosinophilia, high IgE, and retained teeth.[2][3][4][6][12][13][16] A distinct biallelic cytokine-specific IL6ST variant that selectively impairs IL-11 signaling has been associated with craniosynostosis and tooth anomalies without overt immunodeficiency, illustrating the modularity of gp130-mediated cytokine pathways.[16] Conversely, somatic mosaic gain-of-function IL6ST variants that cause ligand-independent, constitutive activation of STAT3 have been described in hepatocytes from patients with inflammatory hepatocellular adenomas, demonstrating that IL6ST can also participate in oncogenic signaling when hyperactivated.[5][16] IL6ST-related autosomal dominant HIES fits within this spectrum as a class of monoallelic dominant-negative variants that cause selective IL-6/IL-11 loss-of-function while preserving enough LIF signaling to avoid the lethal dysautonomia seen in Stüve–Wiedemann syndrome, thereby producing a phenotype that overlaps with, but is not identical to, STAT3-dominant-negative HIES and recessive IL6ST deficiency.[5][6][8][11][12][15][16]  

### 2.3 Genetic risk factors, modifiers, and susceptibility loci

Beyond the primary IL6ST mutations, there is currently limited evidence for additional genetic risk factors or modifier loci specifically influencing IL6ST-related autosomal dominant HIES. The small number of reported families and the strong effect size of dominant-negative IL6ST variants make it difficult to detect subtle modifiers in human cohorts.[8][11][15] However, intra-familial variability in clinical expressivity, particularly among carriers of the p.Ser731Valfs*8 variant, suggests that other genetic or epigenetic factors may modulate disease severity, perhaps by influencing residual gp130 expression levels, alternative signaling pathways, or host defense mechanisms.[15][16] For example, in the 2023 series, some individuals with the p.Ser731Valfs*8 variant had high IgE levels and recurrent infections, whereas others had milder atopic manifestations and fewer infections, despite carrying the same IL6ST variant.[15] Although no specific modifier genes have been identified, one can infer that variation in STAT3, downstream cytokine receptors (such as IL6R or IL11RA), or negative regulators of gp130 signaling (such as SOCS3) could theoretically influence phenotype, given their roles in the IL-6/gp130/STAT3 pathway.[6][7][16][19] At present, genome-wide association or modifier studies focused on IL6ST-related HIES have not been reported, and ClinGen has not yet curated formal gene–phenotype strength or modifier evidence for IL6ST in this context; gene-level evidence rests primarily on the strong co-segregation and functional data from case reports and case series.[4][8][11][12][13][15][16]  

### 2.4 Environmental, infectious, and lifestyle factors

In contrast to complex polygenic diseases, IL6ST-related AD HIES is fundamentally a monogenic disorder, and environmental or lifestyle factors primarily influence the **expression** and complications of disease rather than its occurrence. Patients are particularly susceptible to recurrent bacterial and fungal infections of the skin and respiratory tract, often with Staphylococcus aureus, Aspergillus fumigatus, and Mucorales species isolated from lesions and airway secretions.[8][11][12] For example, in the J Exp Med series, one patient developed chronic pulmonary aspergillosis with repeated isolation of A. fumigatus and Mucorales, requiring prolonged antifungal therapy, highlighting the contribution of environmental fungal exposures to disease burden in the context of impaired IL-6/gp130-mediated immunity.[8][11] Environmental factors such as high pathogen load in crowded living conditions, exposure to mold and damp environments, and poor access to antimicrobial prophylaxis or healthcare are likely to exacerbate infection risk and severity, although these have not been systematically quantified in IL6ST-HIES cohorts.[6][8][11] Lifestyle factors such as smoking or chronic exposure to air pollutants may further damage respiratory epithelium and exacerbate bronchiectasis and pneumatoceles in patients with underlying immune defects, by analogy to other primary immunodeficiencies, but specific data in IL6ST-HIES are lacking.[6] Conversely, adherence to prophylactic antibiotics, early treatment of infections, and vaccination against pneumococcal and influenza pathogens can reduce but not eliminate the burden of infections, suggesting that environmental management plays a key role in secondary prevention.[6][7][8][11]  

### 2.5 Protective factors and gene–environment interactions

No specific genetic protective variants have been described that reduce penetrance or risk of IL6ST-related autosomal dominant HIES among carriers of dominant-negative IL6ST alleles. The high penetrance reported in the original kindreds, with essentially all carriers developing some features of HIES, suggests limited intrinsic protection.[8][11] Nonetheless, the milder phenotypes observed with the p.Ser731Valfs*8 variant in some carriers indicate that lower levels of surface accumulation of mutant gp130 or more subtle disruption of STAT3-binding motifs may confer relative protection compared to more proximal truncations that accumulate strongly at the cell surface.[15][16] Environmental protective factors are largely related to healthcare access and infection control, including prophylactic antibiotics, immunoglobulin replacement in cases with hypogammaglobulinemia, aggressive management of eczema to prevent skin barrier breakdown, and avoidance of environments with high fungal load, all of which can reduce infection frequency and severity.[6][7][8][11][15] Conceptually, gene–environment interactions in IL6ST-HIES are evident in the way that pathogen exposure unmasks and amplifies the consequences of impaired IL-6/IL-11 signaling: in a low-pathogen environment with robust prophylaxis and immunization, patients may experience fewer severe infections and thus less structural lung damage, whereas in high-exposure settings, the same genetic defect can lead to life-threatening infections and early organ damage.[6][8][11][12] These interactions underscore the importance of considering both the fixed genetic lesion in **IL6ST** and the modifiable environmental context when evaluating risk and designing preventive strategies for affected individuals and families.[6][7][8][11][15]  

---

## 3. Phenotypes and Clinical Manifestations

### 3.1 Immunologic and infectious phenotypes

The immunologic and infectious phenotype of IL6ST-related autosomal dominant HIES is dominated by recurrent bacterial and fungal infections of the skin and respiratory tract, reflecting impaired gp130-dependent cytokine signaling in both innate and adaptive immune responses.[1][6][8][11][16] Patients in the 2020 J Exp Med series frequently experienced recurrent pneumonia, often progressing to chronic lung disease with severe cystic bronchiectasis and pneumatoceles, mirroring the pulmonary complications seen in STAT3-HIES.[8][11] Skin infections, particularly “cold” staphylococcal abscesses lacking prominent inflammatory signs, were also common, as were recurrent otitis media and sinusitis, indicating a broad susceptibility to pyogenic infections of the respiratory tract and skin.[6][8][11] Laboratory evaluation typically reveals markedly elevated serum IgE levels, often exceeding several thousand IU/mL, along with peripheral blood eosinophilia; in Béziat’s cohort, all patients had elevated IgE, and many had eosinophilia, consistent with a Th2-skewed immune response.[8][11][16] Total IgG and IgG subclass levels are often normal, but a subset of patients shows hypogammaglobulinemia or specific antibody deficiencies, such as low IgG2/IgG3 and impaired vaccine responses, leading to initial misdiagnosis as common variable immunodeficiency in some cases.[8][11][12] From an HPO perspective, key immunologic and infectious phenotypes include recurrent respiratory infections, recurrent pneumonia, bronchiectasis, lung cavitation or pneumatoceles, recurrent skin abscesses, and chronic fungal infections; these can be mapped to HPO terms such as *Recurrent sinopulmonary infections*, *Bronchiectasis*, *Pneumatoceles*, *Recurrent skin infections*, and *Chronic pulmonary aspergillosis* or related descriptors.[6][8][11][12]  

The age of onset for infections is typically in early childhood, often within the first few years of life, although some patients may present later with recurrent pneumonia or bronchiectasis as the first recognized manifestation.[1][6][8][11][15] Severity varies from moderate recurrent infections responsive to antibiotics to severe, treatment-refractory lung disease requiring prolonged antifungal therapy and oxygen support.[8][11][12][15] Disease progression in the respiratory system is often progressive if infections are not adequately controlled, with repeated pneumonias leading to structural damage in the form of bronchiectasis, pneumatoceles, and chronic colonization with opportunistic pathogens; these complications can significantly impair quality of life and lead to chronic respiratory failure.[6][8][11][12] Patients may also exhibit a modestly impaired Th17 cell response, which likely contributes to bacterial and fungal susceptibility; however, chronic mucocutaneous candidiasis appears to be less frequent than in STAT3-HIES, occurring in only one of the 12 IL6ST-HIES patients in the original cohort.[8][11] Quality of life is substantially impacted by recurrent hospitalizations, chronic cough, exertional dyspnea, and the need for ongoing prophylaxis and monitoring, affecting schooling, employment, and psychosocial functioning.[6][8][11]  

### 3.2 Dermatologic, allergic, and atopic manifestations

Dermatologic and atopic manifestations are central features of IL6ST-related autosomal dominant HIES and contribute significantly to morbidity and healthcare utilization. Nearly all reported patients display chronic eczema or atopic dermatitis-like skin inflammation beginning in early childhood, often associated with intense pruritus, excoriations, and secondary bacterial infections.[6][8][11][15] Béziat et al. reported that high IgE levels and severe eczema were consistent findings, and many patients exhibited additional allergic manifestations such as allergic rhinitis, asthma, or food allergies, reflecting a generalized atopic diathesis.[8][11] Functional studies in naive CD4^+ T cells from IL6ST-HIES patients demonstrated increased Th2 cytokine production, with elevated IL-4, IL-5, and IL-13 secretion compared to controls, alongside a modestly reduced Th17 response; the authors concluded that “these in vitro data reveal an increased Th2 cell response and a modestly impaired Th17 cell response in DN IL6ST patients,” providing a mechanistic link to elevated IgE and atopic disease.[8][11] HPO terms applicable here include *Eczema*, *Atopic dermatitis*, *Elevated serum IgE*, *Eosinophilia*, *Asthma*, and *Allergic rhinitis*, among others.  

In terms of age of onset and course, eczema usually appears in infancy or early childhood, may be severe and refractory to conventional topical therapies, and tends to be chronic with relapsing–remitting flares.[6][8][11][15] Quality of life impairment is substantial: children and adults may experience sleep disturbance, social embarrassment, and functional limitations due to pruritus and skin pain, similar to severe atopic dermatitis in the general population but compounded by the risk of recurrent skin infections.[6][9][10] Importantly, targeted biologic therapy with dupilumab, an anti–IL-4Rα monoclonal antibody that blocks IL-4 and IL-13 signaling, has shown benefit in HIES more broadly, and at least one patient with IL6ST-related AD HIES (carrying the p.Ser731Valfs*8 variant) experienced a significant improvement in eczema and normalization of IgE levels under dupilumab treatment, although asthma control did not improve.[15][16] This observation suggests that, despite the upstream defect in IL-6/gp130 signaling, downstream Th2 cytokines remain critical drivers of atopic manifestations and can be therapeutically targeted, providing an example of pathway-level intervention in this disorder.[9][10][15][16]  

### 3.3 Skeletal, craniofacial, and dental phenotypes

Skeletal, craniofacial, and dental abnormalities are hallmarks of the hyper-IgE syndromes and are also prominent in IL6ST-related autosomal dominant HIES, reflecting the role of IL-11 and related gp130-dependent cytokines in bone development and remodeling.[6][8][11][12][16] Patients commonly exhibit scoliosis, osteopenia or osteoporosis, pathological fractures, joint hyperextensibility, and characteristic facial features such as high-arched palate or coarse facial appearance, paralleling the phenotype seen in STAT3-HIES.[1][6][8][11][16] A 2021 review noted that IL6ST-dominant-negative HIES patients share “very similar clinical phenotype with STAT3-DN HIES including pneumatocele” and that non-immunological features such as scoliosis, osteoporosis, and retention of primary teeth are present in IL6ST-DN HIES, underscoring their nosologic proximity.[6] However, unlike patients with STAT3-DN HIES, IL6ST-DN patients generally do **not** show craniosynostosis, in contrast to those with partial loss-of-function IL6ST variants or complete IL11RA deficiency, who often do, suggesting that residual IL-11 signaling may be preserved in the dominant-negative context.[6][12][16]  

Dental anomalies, particularly retention of primary teeth and delayed eruption of permanent teeth, are frequently reported and can be mapped to HPO phenotypes such as *Retention of primary teeth* and *Delayed eruption of permanent teeth*; these features may require orthodontic or surgical intervention and contribute to malocclusion and mastication difficulties.[6][8][11][12][16] Skeletal manifestations often emerge in late childhood or adolescence, with scoliosis and vertebral fractures presenting as early indicators of bone fragility; bone densitometry in IL6ST-HIES patients has revealed osteopenia, and this can progress over time if not recognized and managed with appropriate bone health strategies.[15][16] The quality of life impact of skeletal and dental anomalies includes chronic pain, reduced mobility, risk of fractures, and cosmetic and functional consequences of craniofacial and dental abnormalities, all of which may require multidisciplinary management involving orthopedics, dentistry, and endocrinology.[6][8][11][12][15][16]  

### 3.4 Additional organ system involvement and behavioral impacts

Beyond the canonical triad of infections, eczema, and skeletal/dental anomalies, IL6ST-related autosomal dominant HIES can involve other organ systems and functional domains. Some patients exhibit clubbing of the fingers and toes, reflecting chronic hypoxemia secondary to advanced lung disease; this was noted, for example, in a patient with severe bronchiectasis and hypogammaglobulinemia misdiagnosed initially as common variable immunodeficiency.[8][11] Hepatic involvement is not a consistent feature of IL6ST-DN HIES, in contrast to somatic gain-of-function IL6ST variants associated with inflammatory hepatocellular adenomas, which represent a distinct clinical entity rather than part of the HIES4A phenotype.[5][16] Neurologic development is generally normal in IL6ST-DN HIES, although mild motor delays have been reported more frequently in autosomal recessive IL6ST HIES than in the dominant-negative form, possibly reflecting more profound cytokine signaling deficits in the former.[6][12][16]  

Behavioral and psychosocial impacts are significant but understudied. Chronic disease, visible eczema and scars, repeated hospitalizations, and limitations on physical activity due to skeletal fragility and respiratory compromise contribute to anxiety, depression, and reduced social participation in some patients, by analogy to other primary immunodeficiencies and severe atopic diseases.[6][7] Sleep disturbance due to pruritus and chronic cough further compounds fatigue and cognitive difficulties. From a quality-of-life perspective, IL6ST-HIES can be conceptualized as affecting multiple domains captured in generic instruments like the SF‑36 or EQ‑5D—physical functioning, role limitations, pain, general health, vitality, social functioning, and emotional well-being—although formal quality-of-life studies specific to this condition have not yet been performed.[6][7][9][10]  

### 3.5 HPO term suggestions and phenotype structuring

To support ontology-based disease modeling, the major phenotypes of IL6ST-related autosomal dominant HIES can be mapped to existing Human Phenotype Ontology (HPO) terms. Core immunologic and infectious phenotypes correspond to terms such as *Recurrent pneumonia*, *Recurrent bacterial infections*, *Bronchiectasis*, *Pneumatoceles*, *Recurrent skin abscesses*, and *Chronic fungal infections of the lung*, while dermatologic and atopic manifestations align with *Eczema*, *Atopic dermatitis*, *Elevated serum IgE*, *Eosinophilia*, and *Asthma*.[6][8][11][12][16] Skeletal and dental anomalies map to *Scoliosis*, *Osteopenia*, *Osteoporosis*, *Pathologic fracture*, *Joint hypermobility*, *Retention of primary teeth*, and *Delayed eruption of permanent teeth*, and additional features may include *High-arched palate* and *Clubbing*.[1][6][8][11][12][16] Age of onset for most features would be coded as infancy or childhood, with progressive respiratory complications and skeletal fragility developing over time, yielding a chronic, life-long disease course with episodic exacerbations.[1][6][8][11][15][16] These HPO mappings provide a structured framework for capturing phenotype frequency and severity in future registries and for integrating IL6ST-HIES into computational phenotype matching systems alongside other primary immunodeficiencies.[6][7][16]  

---

## 4. Genetic and Molecular Information

### 4.1 IL6ST gene structure and gp130 protein

The **IL6ST** gene (interleukin 6 cytokine family signal transducer), located on chromosome 5q11.2, encodes gp130, a transmembrane receptor subunit that serves as the common signal-transducing component for multiple IL-6 family cytokines.[1][5][17][19] NCBI Gene lists IL6ST as the official symbol provided by HGNC and associates it with several phenotypes, including autosomal recessive and autosomal dominant hyper-IgE recurrent infection syndromes and other immunodeficiency and skeletal dysplasia syndromes.[5][16][17] The gp130 protein comprises an extracellular region with cytokine-binding and immunoglobulin-like domains, followed by fibronectin type III domains that help position the transmembrane segments; these domains participate in forming the hexameric IL-6 receptor complex in conjunction with IL-6 and IL-6Rα, as shown in structural and biochemical studies.[19][20] The intracellular domain contains multiple tyrosine residues that, upon phosphorylation by associated JAK kinases, recruit STAT1 and STAT3 transcription factors and the phosphatase PTPN11 (SHP2), thereby activating both the JAK-STAT and Ras-MAPK pathways; it also harbors a recycling motif that controls receptor internalization and trafficking.[19][20]  

Reactome’s IL-6 signaling pathway emphasizes that IL-6 first binds IL-6Rα (either membrane-bound or soluble) and then the IL-6:IL-6R complex dimerizes with two gp130 molecules, forming a hexameric receptor complex in which JAK1, JAK2, and TYK2 are associated with the cytoplasmic tails of gp130.[19][20] Upon ligand-induced receptor dimerization, JAKs phosphorylate gp130, creating docking sites for STAT1 and STAT3, which are subsequently phosphorylated, dimerize, and translocate to the nucleus to regulate gene transcription, while SOCS3 and SHP2 serve as negative regulators.[19][20] gp130 thus functions as a central hub in a pleiotropic cytokine network, transmitting signals from IL-6, IL-11, IL-27, LIF, OSM, and other related cytokines to elicit diverse responses in hematopoietic, immune, skeletal, and other tissues.[12][16][19] The centrality and structural organization of gp130 explain why different classes of IL6ST variants—ranging from complete loss-of-function to dominant-negative and gain-of-function—produce distinct yet mechanistically related human diseases.[5][12][16]  

### 4.2 Spectrum of pathogenic variants in autosomal dominant IL6ST-HIES

In autosomal dominant IL6ST-related HIES (HIES4A), pathogenic variants cluster in the distal portion of the IL6ST coding sequence and encode truncated gp130 receptors that retain the extracellular and transmembrane domains but lack the distal portion of the cytoplasmic tail, including the four STAT3-binding tyrosines and the recycling motif.[5][8][11][15][16] The original J Exp Med report identified seven different truncating variants across eight kindreds: several frameshift mutations such as c.2277_2281dup (p.T761Ifs*29) and c.2155dup (p.I719Nfs*?), as well as nonsense mutations including p.L708*, p.Y759*, and p.S754*; these variants all result in early termination downstream of the transmembrane domain.[8][11] Sanger sequencing confirmed that affected individuals were heterozygous for these variants, and no mutations were found in other known HIES genes such as STAT3, ZNF341, IL6R, DOCK8, TYK2, or PGM3, reinforcing IL6ST as the causal locus.[8][11] Functional analyses showed that overexpressed mutant gp130 proteins accumulate at the cell surface in higher amounts than wild-type gp130, lack all four STAT3-recruiting tyrosines, and are loss-of-function for IL-6, IL-11, LIF, and OSM responses, while acting in a dominant-negative fashion by blocking signaling from co-expressed wild-type gp130.[5][8][11][16]  

The 2023 J Clin Immunol study expanded this variant spectrum by identifying two additional dominant-negative IL6ST alleles: p.Ser731Valfs*8 (a frameshift variant that truncates gp130 after the transmembrane domain and eliminates all STAT3-binding residues and the recycling motif) and p.Arg768* (a nonsense variant that removes the recycling motif and three of the four STAT3-binding residues, leaving one proximal tyrosine intact).[15] The p.Ser731Valfs*8 variant, found in seven patients from two families, yields a gp130 protein that accumulates only slightly at the cell surface, underlying milder biochemical and clinical phenotypes with variable expressivity; in contrast, p.Arg768* results in strong surface accumulation and is associated with more severe HIES manifestations in a single patient.[15] These findings highlight that dominant-negative potency is influenced by both the presence or absence of STAT3-binding sites and the degree of receptor accumulation, and they demonstrate that even partially truncated gp130 receptors can act in a dominant-negative fashion when they interfere with wild-type receptor complexes.[5][8][11][15][16] ClinVar entries for IL6ST also include variants such as c.1493C>T (p.Pro498Leu) and c.1552+3A>C, but these are associated with autosomal recessive HIES4B when biallelic, illustrating the importance of zygosity and variant context in determining disease mechanism.[2][3][4][13][16]  

### 4.3 Variant classification, population frequency, and constraint

Dominant-negative IL6ST variants causing HIES4A are classified as pathogenic or likely pathogenic under ACMG/AMP guidelines, based on strong evidence including de novo occurrence in several patients, segregation with disease in multiple kindreds, absence or extreme rarity in population databases, and robust functional data demonstrating dominant-negative loss-of-function effects.[5][8][11][15][16] For example, the p.T761Ifs*29 and p.I719Nfs variants were reported as de novo in some patients, and none of the truncating variants identified in HIES4A have been found at appreciable frequency in gnomAD or ExAC, consistent with strong purifying selection against such alleles.[8][11][15][16] Population genetics analyses in the J Exp Med study showed that IL6ST tolerates some heterozygous loss-of-function variants in the general population without obvious disease, indicating that not all IL6ST truncations are pathogenic; rather, the specific location and structural consequences of truncations—particularly their inclusion of the transmembrane domain and deletion of STAT3-binding tyrosines and recycling motifs—determine dominant-negative behavior.[11][16][17]  

IL6ST displays moderate to high intolerance to complete loss-of-function, reflected in constraint metrics that show depletion of homozygous LOF variants, in line with the severe phenotypes observed in biallelic IL6ST deficiency.[11][16][17] However, some heterozygous LOF variants are present in gnomAD, suggesting that haploinsufficiency per se is not sufficient to cause disease; indeed, autosomal dominant IL6ST-HIES is not a simple haploinsufficiency disorder but a dominant-negative receptoropathy in which mutant gp130 proteins must be expressed and incorporated into receptor complexes to exert their deleterious effect.[5][8][11][16] Therefore, variant interpretation in IL6ST must integrate structural and functional context, not just LOF annotation, and should be guided by knowledge of the specific domains affected, the presence or absence of the transmembrane region, and the predicted impact on STAT3-binding sites and receptor trafficking.[5][11][15][16]  

### 4.4 Relationship to autosomal recessive IL6ST disorders and other HIES genes

IL6ST-related autosomal dominant HIES exists within a broader landscape of IL6ST-associated disorders and hyper-IgE etiologies. Autosomal recessive IL6ST HIES (HIES4B; OMIM 618523) arises from biallelic missense or splicing variants that selectively impair IL-6 and IL-11 signaling without causing complete gp130 loss, as exemplified by the p.N404Y patient described by Schwerd et al. and the P498L and exon 12 del/ins variants reported by Shahin and Chen.[2][3][4][6][12][13][16] These patients present with recurrent infections, eczema, high IgE, eosinophilia, craniosynostosis, and defective acute-phase response, underscoring the importance of IL-6/IL-11 signaling in both immunity and skeletal development.[4][6][12][13][16] In contrast, IL6ST-dominant-negative HIES patients typically retain normal acute-phase responses, as illustrated by fever and elevated C-reactive protein during infections, reflecting preserved IL-6–induced STAT3 activation in hepatocytes sufficient for acute-phase protein synthesis, despite partial systemic impairment.[8][11][16] This distinction highlights how different variant classes within the same gene can differentially affect tissue-specific signaling outputs and clinical phenotypes.  

IL6ST-HIES also closely resembles STAT3-dominant-negative HIES, which remains the most common genetic cause of autosomal dominant hyper-IgE syndrome.[6][7][8][11] Both disorders share elevated IgE, eczema, recurrent infections, and skeletal/dental anomalies, and both involve impaired STAT3 signaling; however, in IL6ST-HIES, the defect lies upstream at the receptor level and affects multiple cytokines, whereas in STAT3-HIES, the transcription factor itself is mutated.[6][7][8][11][16] Additional HIES genes include DOCK8 (autosomal recessive HIES with severe viral infections), PGM3 (congenital glycosylation defect with HIES), ZNF341 (autosomal recessive STAT3 hypomorphic state), CARD11 (BENTA and HIES-like phenotypes), IL6R, and TYK2, among others.[6][7][10] The existence of IL6ST-HIES emphasizes that HIES is not a single disease but a heterogeneous group of monogenic disorders affecting multiple nodes in the IL-6/STAT3 axis, and it underscores the need for comprehensive gene panels or exome sequencing in patients with HIES phenotypes but no STAT3 variants.[6][7][8][11][15]  

### 4.5 Epigenetic and chromosomal considerations

To date, no specific epigenetic mechanisms—such as DNA methylation changes, histone modifications, or chromatin remodeling—have been implicated in IL6ST-related autosomal dominant HIES. The disorder is best understood as a structural and functional receptoropathy caused by coding variants directly affecting the gp130 protein sequence, rather than by epigenetic dysregulation of IL6ST expression.[5][8][11][15][16] Similarly, no recurrent chromosomal abnormalities involving IL6ST (such as deletions, duplications, or translocations) have been reported in association with HIES4A; structural variants at the IL6ST locus would likely cause haploinsufficiency or complete loss-of-function rather than dominant-negative effects, and such events might instead manifest as recessive or lethal IL6ST deficiency syndromes when biallelic.[5][12][16][17] Nevertheless, as genome-wide structural variant detection becomes more common in clinical practice, rare IL6ST structural variants with dominant-negative properties could theoretically be identified, and careful interpretation will be required to distinguish such variants from benign copy-number changes.[16][17]  

---

## 5. Environmental, Infectious, and Lifestyle Contributors

Although IL6ST-related autosomal dominant HIES is fundamentally defined by a germline dominant-negative IL6ST mutation, environmental exposures and lifestyle can significantly influence disease manifestation, complications, and quality of life. Patients with impaired IL-6/gp130 signaling are particularly vulnerable to recurrent respiratory tract infections, and environmental factors such as exposure to crowded settings, poor indoor air quality, and mold contribute to the pathogen load and infection burden.[6][8][11][12] In the reported cohorts, many pulmonary infections were caused by common community and hospital pathogens, including *Staphylococcus aureus*, *Streptococcus pneumoniae*, and *Aspergillus fumigatus*, and in at least one case, fungal organisms from the order Mucorales were isolated, highlighting the role of environmental fungi.[8][11][12] Climatic conditions, housing quality, and occupational exposures (such as agricultural work or construction in dusty environments) may further modulate infection risk, although these variables have not been systematically assessed in IL6ST-HIES studies.  

Lifestyle factors, particularly smoking and exposure to secondhand smoke or biomass fuels, can compound underlying immune defects by damaging airway epithelium, impairing mucociliary clearance, and promoting chronic bronchitis, thereby increasing pneumonia and bronchiectasis risk.[6] Diet, exercise, and vitamin D status may influence bone density and skeletal health, which is particularly relevant given the osteopenia and osteoporosis seen in many IL6ST-HIES patients.[6][15][16] Behavioral factors such as adherence to prophylactic antibiotic regimens, consistent use of moisturizers and topical anti-inflammatory therapies for eczema, and infection-preventive practices (like hand hygiene and avoidance of sick contacts) can materially affect disease course and complication rates, especially in childhood.[6][7][8][11] From a public health perspective, vaccination against encapsulated bacteria and influenza is critical, although responses may be variably impaired and should be monitored; herd immunity and community vaccination coverage therefore serve as indirect environmental protective factors for these patients.[6][7][8][11]  

---

## 6. Mechanism and Pathophysiology

### 6.1 Ordered causal chain from IL6ST mutation to clinical phenotype

The pathophysiology of IL6ST-related autosomal dominant HIES can be conceptualized as a sequential causal chain linking the initiating genetic lesion to downstream cellular and clinical outcomes. To satisfy the requirement for an ordered chain, the core steps can be summarized in tabular form, with each step leading causally to the next; some links are directly demonstrated by experimental data, whereas others are inferred from broader cytokine biology and related disorders.  

| Step | Mechanistic description |
|------|-------------------------|
| 1 | A heterozygous truncating variant in **IL6ST** produces a gp130 receptor that retains the extracellular and transmembrane domains but lacks the distal cytoplasmic tail containing the recycling motif and STAT3-binding tyrosines.[5][8][11][15] |
| 2 | The truncated gp130 is expressed and trafficked to the plasma membrane, where it accumulates at higher levels than wild-type gp130 due to loss of the recycling motif, leading to increased surface density of nonfunctional receptors.[5][8][11][15][16] |
| 3 | Mutant gp130 incorporates into IL-6 family receptor complexes (e.g., IL-6:IL-6R:gp130) and interferes with normal signaling, resulting in a dominant-negative loss of function for IL-6, IL-11, LIF, and OSM signaling in cells expressing both mutant and wild-type gp130.[5][8][11][16] |
| 4 | Impaired gp130-mediated activation of the JAK-STAT and MAPK pathways leads to reduced STAT3 phosphorylation and transcriptional responses downstream of IL-6 and IL-11 in immune cells, fibroblasts, and other tissues, while some LIF signaling may be preserved.[5][8][11][12][16][19] |
| 5a | In the immune system, diminished IL-6/gp130/STAT3 signaling leads to skewed CD4^+ T cell differentiation with increased Th2 responses and modestly reduced Th17 responses, as demonstrated in patient T cells, resulting in elevated IgE, eosinophilia, and impaired antibacterial and antifungal immunity.[8][11][12] |
| 5b | In bone and connective tissues, reduced IL-11/gp130/STAT3 signaling disrupts osteoblast and chondrocyte function, leading to skeletal anomalies such as scoliosis, osteopenia, and dental abnormalities, by analogy to IL11RA and IL6ST recessive disorders.[6][12][16] |
| 6 | The combination of impaired mucocutaneous host defense and Th17 function results in recurrent bacterial and fungal infections of the skin and lungs, eventually causing bronchiectasis, pneumatoceles, chronic lung disease, and skin scarring.[6][8][11][12] |
| 7 | Enhanced Th2 differentiation and elevated Th2 cytokines (IL-4, IL-5, IL-13) drive atopic manifestations, including eczema, asthma, elevated IgE, and eosinophilia, contributing to chronic allergic inflammation and skin barrier dysfunction.[8][11][15] |
| 8 | Over time, recurrent infections and chronic inflammation lead to cumulative organ damage (particularly in the lungs and skeleton), functional limitations, and reduced quality of life, constituting the clinical phenotype of IL6ST-related autosomal dominant HIES.[6][8][11][12][15][16] |

Some of these steps, particularly those relating to Th2/Th17 skewing and skeletal effects, are supported by direct experimental observations in IL6ST-HIES patients, while others, such as the detailed contributions of each cytokine to specific clinical features, are inferred from animal models and related human disorders (e.g., IL11RA deficiency, STAT3-HIES), but are highly plausible given shared pathway biology.[6][7][8][11][12][16][19]  

### 6.2 IL-6 family cytokine signaling via gp130: molecular pathway context

IL-6 family cytokines use gp130 as a common signal-transducing component, and understanding this pathway is crucial for interpreting how IL6ST mutations lead to HIES. Reactome’s IL-6 signaling pathway describes how IL-6 binds the IL-6 receptor alpha chain (IL6R), forming a complex that then recruits two gp130 molecules to assemble a hexameric receptor complex composed of two IL-6, two IL6R, and two gp130 subunits.[19][20] The gp130 cytoplasmic tail is pre-associated with JAK1, JAK2, and TYK2; upon ligand-induced receptor dimerization and hexamer formation, JAKs are activated, leading to phosphorylation of gp130 on specific tyrosine residues that become docking sites for STAT1, STAT3, and the phosphatase PTPN11 (SHP2).[19][20] Phosphorylated STAT1 and STAT3 then dimerize and translocate to the nucleus, where they regulate gene expression involved in acute-phase responses, cell survival, proliferation, differentiation, and immune effector functions; SHP2 and SOCS3 act as negative regulators by dephosphorylating gp130 and inhibiting JAK activity.[19][20]  

In addition to “classic” signaling via membrane-bound IL6R, IL-6 can also signal via “trans-signaling,” in which soluble IL6R (sIL6R) binds IL-6 and then engages gp130 on cells that do not express IL6R, vastly expanding the range of IL-6–responsive cells and contributing to pro-inflammatory activities.[19] Similar gp130-based complexes are formed by IL-11 (with IL11RA), IL-27 (with IL27RA), OSM (with either OSMR or LIFR), and LIF (with LIFR), each using gp130 as a shared signaling core.[12][16][19] Forced dimerization of gp130 or related receptor subunits is sufficient to drive ligand-independent activation of STAT1/STAT3 and ERK1/2, underscoring that mere juxtaposition of gp130 intracellular domains is enough to trigger downstream signaling; this principle explains how certain gain-of-function IL6ST variants produce constitutive STAT3 activation in hepatocellular adenomas.[16][19] In IL6ST-dominant-negative HIES, the truncated gp130 receptors lack the intracellular tyrosines required for STAT recruitment, so even though ligand binding and receptor dimerization may occur, downstream JAK-STAT signaling cannot be properly engaged, and mutant receptors interfere with the function of wild-type gp130 by occupying a share of receptor complexes.[5][8][11][16][19]  

### 6.3 Dominant-negative gp130 dysfunction: receptor-level mechanism

Dominant-negative IL6ST variants act at the receptor level to impede gp130 signaling, and their mechanism has been elucidated through a combination of patient cell analyses and overexpression studies. In Béziat’s cohort, mutant gp130 proteins were shown to be expressed on the cell surface at higher levels than wild-type gp130, due to the absence of the recycling motif that normally mediates receptor internalization and degradation.[5][8][11][16] The truncated receptors contain the transmembrane domain and extracellular cytokine-binding domains but lack all or most of the cytoplasmic STAT3-binding tyrosines and the recycling motif, rendering them signaling incompetent but capable of participating in receptor complexes.[5][8][11] Overexpression experiments in transfected cells showed that these mutant gp130 proteins are loss-of-function and dominant-negative for IL-6, IL-11, LIF, and OSM responses: when co-expressed with wild-type gp130, they reduce STAT3 phosphorylation and transcriptional responses to these cytokines, demonstrating that they interfere with normal signaling.[5][8][11][16]  

Clinically, patients with dominant-negative IL6ST variants retain some aspects of inflammatory responses, such as fever and C-reactive protein elevation during infection, distinguishing them from patients with biallelic IL6ST or IL6R deficiencies, in whom acute-phase responses are markedly impaired.[8][11][12][16] This observation indicates that dominant-negative gp130 does not completely abolish IL-6 signaling in all tissues but rather causes a partial defect that varies by cell type and context, perhaps reflecting differences in IL6ST expression, receptor stoichiometry, or downstream signaling redundancies.[8][11][12][16] The 2023 study further revealed that different dominant-negative variants can differ in their degree of cell-surface accumulation and, consequently, their dominant-negative strength: p.Ser731Valfs*8 accumulates only slightly and is associated with milder biochemical defects and variable clinical expressivity, whereas p.Arg768* accumulates markedly and leads to more severe impairment and phenotype.[15] These findings illustrate a continuum of dominant-negative potency among IL6ST variants and reinforce the importance of receptor trafficking and surface expression in determining functional outcomes.[5][8][11][15][16]  

### 6.4 Immune cell-level mechanisms: Th2/Th17 balance and B cell function

At the cellular level, IL6ST-related autosomal dominant HIES manifests as a complex immune dysregulation affecting T helper cell differentiation, B cell memory, and potentially innate immune functions. In vitro studies of naive CD4^+ T cells from IL6ST-HIES patients demonstrated that, under polarizing conditions, these cells produce increased amounts of Th2 cytokines (IL-4, IL-5, IL-13) and only modestly reduced Th17 cytokines (IL-17A, IL-17F) compared to control T cells.[8][11] Béziat et al. concluded that dominant-negative IL6ST variants “reveal an increased Th2 cell response and a modestly impaired Th17 cell response,” proposing that the strong Th2 response accounts for high IgE levels and allergic manifestations, while the subnormal Th17 response contributes to susceptibility to bacterial and fungal infections but may explain the relative rarity of chronic mucocutaneous candidiasis compared to STAT3-HIES.[8][11] These observations suggest that gp130-dependent cytokines, particularly IL-6 and IL-11, normally constrain Th2 differentiation and promote balanced Th17 development; their partial disruption skews the immune response toward Th2 dominance without completely abrogating Th17 immunity.[8][11][12]  

B cell function is also affected. In the p.N404Y recessive IL6ST deficiency patient, impaired IL-6 and IL-27 signaling led to defective B cell memory generation, reduced switched memory B cells, and poor vaccination responses, reflecting the role of IL-6/gp130/STAT3 signaling in germinal center reactions.[4][12] In IL6ST-dominant-negative HIES, memory B cell defects are less consistent but some patients exhibit hypogammaglobulinemia and poor specific antibody responses, supporting a milder but relevant impairment in humoral immunity.[8][11][12][13] Innate immune cells such as neutrophils and monocytes rely less directly on IL-6/gp130 for core effector functions, but gp130-dependent cytokines contribute to acute-phase responses, neutrophil survival, and inflammatory cytokine networks; thus, partial gp130 dysfunction may subtly alter innate immune responses, although this has not been extensively characterized in IL6ST-HIES.[8][11][12][16][19] From a Gene Ontology standpoint, relevant biological processes include *interleukin-6–mediated signaling pathway*, *JAK-STAT cascade*, *T helper 2 cell differentiation*, *T helper 17 cell differentiation*, *regulation of immunoglobulin production*, and *acute-phase response*, among others, illustrating the breadth of gp130’s influence on immune cell behavior.[16][19]  

### 6.5 Tissue- and organ-level mechanisms: lung, skin, bone, and teeth

At the tissue level, the consequences of impaired gp130 signaling manifest in the lung, skin, bone, and teeth, which together generate the characteristic clinical picture of IL6ST-related autosomal dominant HIES. In the lung, recurrent bacterial and fungal infections, coupled with impaired inflammatory and tissue repair responses, lead to chronic airway damage and structural remodeling, including bronchiectasis and pneumatoceles.[6][8][11][12] The combination of impaired IL-6/IL-11 signaling in airway epithelial cells, fibroblasts, and immune cells, along with defective Th17-mediated mucosal immunity, likely contributes to impaired clearance of pathogens and delayed resolution of inflammation, thereby predisposing to chronic infection and scarring.[6][8][11][12][16][19] Over time, repeated cycles of infection and repair produce irreversible structural damage, reduced lung function, and increased risk of colonization with opportunistic organisms such as *Aspergillus* and Mucorales.[8][11][12]  

In the skin, elevated Th2 cytokines and IgE, coupled with a predisposition to Staphylococcus aureus colonization, drive chronic eczema and recurrent superficial infections.[6][8][11][15] IL-6 family cytokines also participate in keratinocyte proliferation and barrier function; thus, their partial disruption may further destabilize the epidermal barrier, although direct evidence in IL6ST-HIES is limited.[6][16][19] In bone and connective tissue, IL-11 and other gp130-dependent cytokines regulate osteoblast and chondrocyte differentiation and activity; disruption of these signals leads to skeletal anomalies such as scoliosis, osteopenia, and craniofacial abnormalities, as demonstrated in IL11RA and IL6ST recessive deficiency disorders.[4][6][12][16] Dental anomalies, particularly retention of primary teeth and delayed shedding, are thought to arise from impaired resorption of primary tooth roots and altered osteoclast function, processes in which IL-11/gp130/STAT3 signaling participates.[6][12][16] The observation that IL6ST-dominant-negative HIES patients do not typically exhibit craniosynostosis, whereas IL6ST partial loss-of-function and IL11RA deficiency do, suggests that the degree and tissue specificity of IL-11 signaling impairment differ between variant classes, with dominant-negative variants preserving enough IL-11 signaling in cranial sutures to prevent premature fusion.[6][12][16]  

### 6.6 Omics and systems-level insights

The small number of IL6ST-HIES patients has limited the application of large-scale omics approaches, but available transcriptomic and functional genomic analyses provide insights into pathway-level perturbations. In patient cells stimulated with IL-6 family cytokines, gene expression profiling reveals reduced induction of STAT3 target genes, confirming that dominant-negative gp130 impairs canonical JAK-STAT signaling.[8][11][12] In the p.N404Y recessive IL6ST deficiency case, functional assays showed defective IL-6, IL-11, OSM, and IL-27 responses, with near-normal LIF responses, suggesting that different cytokine pathways may be differentially affected by specific variants.[12] A 2023 review on the “Human GP130 Cytokine Receptor and Its Expression Atlas” emphasized that IL6ST variants can be grouped into classes based on their functional impact (complete loss-of-function, partial loss-of-function affecting specific receptor complexes, dominant-negative variants with selective IL-6/IL-11 loss-of-function, and gain-of-function variants), and that these classes map onto distinct clinical syndromes, illustrating a genotype–mechanism–phenotype continuum.[16]  

From a systems biology perspective, IL6ST-related HIES exemplifies a network-level vulnerability where disruption of a central hub (gp130) affects multiple upstream ligands and downstream transcriptional programs, but with partial redundancy and compensatory pathways mitigating complete system failure.[8][11][12][16][19] Multi-omics integration—combining genomic, transcriptomic, proteomic, and metabolomic data—has not yet been systematically applied to IL6ST-HIES, but the disease could serve as a model for studying how specific receptoropathies reshape immune network topology and resilience. For example, single-cell RNA sequencing could reveal cell type–specific alterations in cytokine signaling and effector gene expression, while phosphoproteomics might quantify global changes in JAK-STAT and MAPK activation across cell types. Functional genomics screens (e.g., CRISPR-based perturbation of negative regulators like SOCS3 or SHP2) in cellular models could identify potential modifiers that enhance or suppress the effects of dominant-negative gp130, informing future therapeutic strategies.[16][19]  

---

## 7. Anatomical Structures and Cell Types Affected

### 7.1 Organ-level involvement and body systems

IL6ST-related autosomal dominant HIES primarily affects the immune system, respiratory system, integumentary system, and skeletal system, with secondary effects in other organs through chronic inflammation and infection. At the organ level, the lungs (UBERON:0002048) are prominently involved, with recurrent pneumonia, bronchiectasis, and pneumatoceles; chronic lung disease can progress to respiratory insufficiency if not adequately managed.[6][8][11][12] The skin (UBERON:0002097) is another key site, manifesting with eczema, recurrent infections, and scarring; mucocutaneous tissues more broadly are affected by atopic inflammation and recurrent infections.[6][8][11][15] The skeletal system, including the spine (UBERON:0002414), long bones, and craniofacial skeleton (UBERON:0003129), shows scoliosis, osteopenia, fractures, and dental anomalies involving the teeth (UBERON:0001091), particularly primary dentition.[6][8][11][12][16]  

The immune system (UBERON:0002405), encompassing lymphoid organs such as lymph nodes, spleen, thymus, and bone marrow, is functionally affected through altered T and B cell responses and cytokine signaling, although gross anatomic abnormalities of lymphoid organs are not typically reported.[6][8][11][12] The liver (UBERON:0002107) participates in acute-phase responses, and its function is partially preserved in IL6ST-dominant-negative HIES, as evidenced by normal or present C-reactive protein induction during infection; this contrasts with autosomal recessive IL6ST deficiency, in which acute-phase responses are impaired.[8][11][12][16] Other organ systems, such as the cardiovascular, nervous, and gastrointestinal systems, are generally less directly involved, although chronic disease and treatment complications (e.g., from prolonged steroids or antifungals) may have secondary effects.[6][8][11][12]  

### 7.2 Tissue and cell-level specificity

At the tissue and cellular levels, IL6ST-related HIES involves multiple cell types, reflecting gp130’s ubiquitous expression but diverse functional roles. In the immune system, key affected cell types include CD4^+ T helper cells (CL:0000545), particularly Th2 (CL:0000546) and Th17 (CL:0001039) subsets, which show altered differentiation and cytokine production; naive CD4^+ T cells from patients exhibit exaggerated Th2 responses and modestly impaired Th17 responses under polarizing conditions.[8][11][12] B cells (CL:0000236), especially germinal center B cells and memory B cells, rely on IL-6 and IL-27 signaling through gp130 for proper differentiation and class-switching; defects in these pathways can lead to impaired memory formation and hypogammaglobulinemia in some patients.[4][8][11][12][13] Innate immune cells such as monocytes (CL:0000576), macrophages (CL:0000235), and neutrophils (CL:0000775) express gp130 and respond to IL-6 family cytokines that modulate inflammatory responses and survival; partial disruption of gp130 signaling may subtly alter their function, contributing to impaired pathogen clearance and aberrant inflammatory responses.[12][16][19]  

Epithelial cells in the respiratory tract (e.g., bronchiolar epithelial cells) and skin keratinocytes (CL:0000312) also express gp130 and respond to IL-6 family cytokines, which regulate barrier integrity, antimicrobial peptide production, and tissue repair; thus, IL6ST dysfunction likely contributes to impaired barrier function and repair in these tissues.[16][19] Osteoblasts (CL:0000062) and chondrocytes (CL:0000138) in bone and cartilage rely on IL-11/gp130/STAT3 signaling for normal development and remodeling; disruption of this signaling leads to skeletal anomalies, as demonstrated in IL11RA deficiency and IL6ST recessive disorders.[4][6][12][16] Dental tissues, including odontoblasts (CL:0000388) and periodontal ligament fibroblasts, may be affected through altered IL-11 signaling, contributing to retention of primary teeth and delayed tooth eruption.[6][12][16]  

### 7.3 Subcellular compartments and cellular components

Subcellularly, gp130 is a plasma membrane protein (GO:0005886) that, upon ligand engagement, participates in receptor complexes that are internalized and trafficked through endosomal compartments before recycling or degradation.[19][20] Dominant-negative IL6ST variants disrupt this dynamic by removing the recycling motif, leading to altered receptor internalization and increased surface accumulation of truncated gp130.[5][8][11][16] The cytoplasmic tail of gp130 interacts with JAK kinases (which localize to the inner surface of the plasma membrane) and with STAT1/STAT3, whose phosphorylated forms translocate to the nucleus (GO:0005634) to regulate transcription.[19][20] The absence of STAT3-binding tyrosines in truncated gp130 prevents STAT recruitment, thereby reducing nuclear STAT3 activation and altering gene expression profiles in target cells.[5][8][11][19] Relevant GO Cellular Component terms include *plasma membrane*, *cell surface receptor complex*, *cytoplasm*, and *nucleus*, reflecting the journey of the gp130 signaling complex and downstream transcription factors.[19][20]  

---

## 8. Temporal Development and Natural History

### 8.1 Age of onset and early manifestations

IL6ST-related autosomal dominant HIES is typically a pediatric-onset disorder, with most manifestations appearing in infancy or early childhood, although some patients may only be recognized in adolescence or adulthood when complications such as bronchiectasis or skeletal anomalies become evident.[1][6][8][11][15] Eczema and elevated serum IgE often appear within the first months to years of life, paralleling atopic dermatitis in age of onset; recurrent skin and respiratory infections may also begin early, especially once children experience repeated viral and bacterial exposures in daycare or school settings.[6][8][11][15] In some families, subtle atopic manifestations and mild infections in early childhood may be overlooked or attributed to common pediatric conditions, delaying recognition of an underlying primary immunodeficiency until more severe or recurrent infections occur.[6][8][11] Skeletal manifestations such as scoliosis and osteopenia typically emerge later, during late childhood or adolescence, as growth accelerates and cumulative bone remodeling defects become more apparent.[6][15][16] Dental anomalies, particularly retention of primary teeth, may be noticed when children fail to shed their primary dentition at expected ages, prompting dental evaluation and, in some cases, contributing to the suspicion of hyper-IgE syndrome when combined with infections and eczema.[6][7][8][11]  

### 8.2 Disease progression and clinical course

The clinical course of IL6ST-HIES is chronic and lifelong, with a pattern of episodic infections and atopic flares superimposed on progressive organ-specific damage, particularly in the lungs and skeleton. Recurrent bacterial pneumonias and fungal infections, if not adequately prevented or treated, lead over years to chronic lung disease with bronchiectasis and pneumatoceles; this progressive structural damage can result in declining lung function, exercise intolerance, chronic hypoxemia, and respiratory failure in severe cases.[6][8][11][12] The pace of progression varies, influenced by factors such as infection prevention strategies, adherence to prophylactic antibiotics, access to specialized care, and environmental exposures; some patients maintain relatively stable lung function into adulthood, whereas others develop severe bronchiectasis in adolescence.[6][8][11][15] Eczema tends to follow a relapsing–remitting course, often improving somewhat in adolescence but persisting into adulthood in many patients, especially in the absence of targeted biologic therapy; chronic skin inflammation and scratching can lead to lichenification, scarring, and pyoderma.[6][9][10][15]  

Skeletal manifestations may progress insidiously, with scoliosis worsening during growth spurts and osteopenia culminating in fractures, particularly in the vertebrae and long bones; bone densitometry in IL6ST-HIES patients has revealed osteopenia and, in some cases, osteoporosis.[15][16] Dental issues such as retained primary teeth and malocclusion can impair chewing and speech and may require surgical extraction and orthodontic treatment, which, if delayed, can cause long-term functional and cosmetic consequences.[6][7][8][11] Taken together, the disease course is characterized by a combination of short-term acute events (infections, eczema flares) and long-term cumulative damage (bronchiectasis, skeletal deformities), requiring ongoing multidisciplinary management throughout life.[6][7][8][11][12][15][16]  

### 8.3 Remission, critical periods, and windows of intervention

Spontaneous remission of IL6ST-related autosomal dominant HIES does not occur, given its genetic basis, but certain manifestations may partially abate with age or targeted therapy. For example, eczema often becomes less severe in adulthood in many hyper-IgE patients, although this is variable, and biologic therapy such as dupilumab can induce sustained remission of skin inflammation in some individuals.[9][10][15][16] Critical periods in disease trajectory include early childhood, when recurrent infections and eczema first appear; this period represents a key window for diagnosis and initiation of prophylactic measures, which can reduce the risk of severe lung damage later.[6][7][8][11] Another critical period occurs during adolescence, when skeletal growth accelerates and scoliosis and bone density issues may worsen, highlighting the importance of orthopedic monitoring and bone health interventions during these years.[6][15][16]  

Early genetic diagnosis and pathway-specific management (e.g., prophylactic antibiotics, immunoglobulin replacement when indicated, eczema control, and vigilant infection monitoring) can modify natural history by reducing cumulative organ damage, even though they do not correct the underlying defect.[6][7][8][11][12] Emerging targeted therapies may eventually offer new windows of intervention; for instance, gene therapy or small-molecule modulators of gp130 signaling, if developed, could theoretically be applied early in life to prevent or mitigate disease manifestations, although such approaches remain speculative at present.[16]  

---

## 9. Inheritance, Population Genetics, and Epidemiology

### 9.1 Mode of inheritance, penetrance, and expressivity

IL6ST-related hyper-IgE syndrome 4A is inherited in an autosomal dominant manner, with dominant-negative IL6ST variants exerting their effects in heterozygous state.[1][5][8][11][16] The original cohorts reported both familial and de novo cases; at least four truncating variants (e.g., p.L708*, p.I719Nfs, p.Y759*, and p.T761Ifs*29) occurred de novo in affected individuals, confirming that novel IL6ST variants can cause sporadic cases.[6][8][11][16] In the initial kindreds, segregation data suggested high penetrance: virtually all individuals carrying the dominant-negative IL6ST variant exhibited some manifestation of HIES, although severity varied, particularly with the newer p.Ser731Valfs*8 variant.[8][11][15][16] The 2021 HIES review noted that IL6ST-dominant-negative HIES exhibits an autosomal dominant inheritance pattern with “full penetrance like STAT3-DN HIES,” though subsequent data on p.Ser731Valfs*8 indicate that penetrance may be high for biochemical abnormalities (high IgE) but clinical expressivity can range from mild to severe.[6][15][16]  

Expressivity is clearly variable. In the 2023 J Clin Immunol series, the p.Ser731Valfs*8 variant was associated with heterogeneous clinical presentations among carriers, ranging from classic HIES with recurrent infections and severe eczema to milder atopy with fewer infections; in contrast, the p.Arg768* variant produced a more severe phenotype.[15] No evidence of genetic anticipation has been reported, and there is currently no documented germline mosaicism in IL6ST-HIES families, although mosaicism remains a theoretical consideration, especially for de novo variants.[8][11][15][16] Given the rarity of IL6ST-HIES, formal penetrance estimates and genotype–phenotype correlations remain preliminary and will require larger cohorts or registries for refinement.[6][7][16]  

### 9.2 Population distribution, founder effects, and demographics

IL6ST-related autosomal dominant HIES is extremely rare, with fewer than 30 patients reported worldwide as of the latest publications.[8][11][15][16] The published families originate from diverse geographic and ethnic backgrounds, including European and other populations, and there is currently no evidence for a strong founder effect for any specific dominant-negative IL6ST variant.[8][11][15][16] Biallelic IL6ST variants causing recessive HIES and related syndromes have been described in consanguineous families, particularly from Turkey and other regions with higher rates of consanguinity, but this pattern reflects autosomal recessive inheritance rather than the dominant-negative HIES4A phenotype.[2][3][4][12][13][16]  

Because of its rarity and recent recognition, no robust epidemiological data on prevalence or incidence exist for IL6ST-HIES; it can be considered an ultra-rare primary immunodeficiency within the broader hyper-IgE syndrome category.[6][7][18] Sex distribution in the reported IL6ST-HIES cohorts appears approximately balanced, with both male and female patients affected, consistent with autosomal inheritance.[8][11][15] Age distribution spans from early childhood to adulthood, with some patients diagnosed in childhood and others only recognized in late adolescence or adulthood when recurrent infections and skeletal or dental anomalies prompted investigation.[6][8][11][15] As awareness of IL6ST-HIES increases and next-generation sequencing becomes more widely used, additional cases will likely be identified, allowing more precise epidemiological characterization and assessment of potential population-specific variants.[6][7][16]  

---

## 10. Diagnostics and Clinical Evaluation

### 10.1 Clinical suspicion and diagnostic criteria

Diagnosis of IL6ST-related autosomal dominant HIES requires a combination of careful clinical evaluation and genetic testing. Clinically, patients present with a constellation of findings suggestive of hyper-IgE syndrome: markedly elevated serum IgE, chronic eczematous dermatitis, recurrent skin and respiratory infections (often with Staphylococcus aureus and other pyogenic bacteria), and skeletal and dental anomalies such as scoliosis and retention of primary teeth.[1][6][7][8][11][16] The NIH HIES scoring system, originally developed for STAT3-HIES, incorporates features like characteristic facial appearance, severe eczema, history of “cold” abscesses, recurrent pneumonias leading to pneumatoceles, elevated IgE, eosinophilia, skeletal abnormalities, and dental anomalies; IL6ST-HIES patients generally score highly on this scale, reflecting their phenotypic similarity to STAT3-HIES.[6][7][8][11] For example, Béziat et al. reported that all IL6ST-HIES patients exhibited high IgE, eczema, and recurrent lung infections, with many showing skeletal and dental anomalies, fulfilling clinical criteria for autosomal dominant HIES.[8][11]  

However, clinical criteria alone cannot distinguish IL6ST-HIES from STAT3-HIES or other genetic forms of HIES, making molecular testing essential. Suspicion for an alternative genetic cause beyond STAT3 may arise when patients with a HIES phenotype lack STAT3 mutations and show particular features such as preserved acute-phase responses, absence of craniosynostosis, or specific immunologic profiles, but these clues are not definitive.[6][7][8][11][12][16] Therefore, comprehensive genetic analysis is recommended in all patients with a strong HIES phenotype, with IL6ST included in targeted gene panels or exome/genome sequencing pipelines.[6][7][8][11][15]  

### 10.2 Laboratory tests, imaging, and functional assays

Routine laboratory evaluation in suspected IL6ST-HIES includes measurement of serum immunoglobulins (IgG, IgA, IgM, IgE), eosinophil counts, complete blood count, and basic inflammatory markers such as C-reactive protein and ESR.[6][7][8][11] IL6ST-HIES patients typically show markedly elevated IgE, often in the thousands of IU/mL, and eosinophilia, whereas IgG and IgA levels are usually normal but can be reduced in some patients; specific antibody responses to vaccines should be assessed, as defects may necessitate immunoglobulin replacement.[6][7][8][11][12] Lymphocyte subset analysis may reveal alterations in T and B cell subsets, including reduced memory B cells or subtle changes in Th17 cells, but these findings are not specific to IL6ST-HIES.[4][8][11][12][13]  

Imaging studies, particularly chest CT scans, are critical for evaluating lung involvement, documenting bronchiectasis, pneumatoceles, and other structural complications; these findings support the diagnosis of a chronic immunodeficiency and help monitor disease progression.[6][8][11][12] Skeletal imaging can reveal scoliosis, vertebral fractures, and osteopenia, while dental radiographs show retained primary teeth and delayed eruption of permanent teeth.[6][7][8][11][16] Biopsy is rarely needed for diagnosis but may be employed to evaluate unusual infections or suspected malignancies; histopathology typically shows chronic inflammation with features consistent with recurrent infection and atopic dermatitis in the skin.[6][8][11]  

Functional assays specific to IL6ST-HIES include in vitro cytokine stimulation of patient leukocytes or fibroblasts followed by measurement of STAT3 phosphorylation and downstream gene expression in response to IL-6, IL-11, LIF, and OSM; dominant-negative IL6ST variants yield reduced STAT3 activation to these cytokines.[5][8][11][12][16] These assays are primarily used in research settings but can provide strong support for pathogenicity of novel IL6ST variants. In contrast, acute-phase responses (e.g., CRP) should be evaluated clinically during infections; preserved CRP induction in IL6ST-HIES helps distinguish it from autosomal recessive IL6ST or IL6R deficiencies, in which CRP responses are markedly impaired.[8][11][12][16]  

### 10.3 Genetic testing strategies

Genetic testing is the definitive diagnostic tool for IL6ST-related autosomal dominant HIES. Given the expanding list of HIES-associated genes, targeted gene panels encompassing STAT3, IL6ST, DOCK8, ZNF341, PGM3, TYK2, CARD11, IL6R, and others are a practical first-line approach; if panel testing is negative, whole-exome sequencing (WES) or whole-genome sequencing (WGS) can be employed.[6][7][8][11][15] In Béziat’s series, patients initially tested negative for STAT3 mutations using Sanger sequencing, and whole-exome sequencing then revealed heterozygous truncating IL6ST variants; such exome or genome approaches are increasingly standard for undiagnosed primary immunodeficiencies.[8][11] Once a candidate IL6ST variant is identified, segregation analysis in family members and functional validation (where feasible) are important for confirming causality, particularly for novel truncating or missense variants.[5][8][11][15][16]  

Single-gene testing of IL6ST may be considered when there is a strong suspicion based on family history (autosomal dominant inheritance) and clinical features consistent with IL6ST-HIES and when broader panels or exome sequencing are unavailable; however, given the phenotypic overlap with other HIES genes, broader testing is generally preferred.[6][7][8][11] Chromosomal microarray and karyotyping have limited utility in IL6ST-HIES because pathogenic variants are typically single nucleotide variants or small indels rather than large structural changes.[5][16][17] Mitochondrial DNA testing and repeat expansion analyses are not relevant to this disorder.  

### 10.4 Differential diagnosis

The differential diagnosis of IL6ST-related autosomal dominant HIES includes other forms of hyper-IgE syndrome and primary immunodeficiencies with overlapping features. STAT3-dominant-negative HIES is the most important comparator, sharing elevated IgE, eczema, recurrent infections, and skeletal/dental anomalies; distinguishing features may include more severe Th17 deficiency and higher prevalence of chronic mucocutaneous candidiasis in STAT3-HIES, whereas IL6ST-HIES tends to have preserved acute-phase responses and rare candidiasis.[6][7][8][11][16] Autosomal recessive IL6ST HIES (HIES4B) and IL11RA deficiency present with HIES features plus craniosynostosis and more profound acute-phase defects, distinguishing them from IL6ST-dominant-negative HIES.[4][6][12][16] DOCK8 deficiency, an autosomal recessive HIES, is characterized by severe viral infections, malignancy risk, and autoimmunity, often with severe eczema and elevated IgE, but lacks the skeletal and dental anomalies typical of STAT3/IL6ST-HIES.[6][7] PGM3 deficiency, ZNF341 mutations

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.

20 of 22 terms resolved to a current term; the rest could not be looked up either way.