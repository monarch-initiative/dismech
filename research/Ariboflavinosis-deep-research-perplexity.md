---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-16T11:54:01.301292'
end_time: '2026-10-16T11:57:50.495787'
duration_seconds: 229.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ariboflavinosis
  mondo_id: MONDO:0004573
  category: Nutritional
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
  total_references: 17
  verified: 16
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.059
  relevance_assessed: 16
  on_topic: 9
  unresolved_references:
  - PMC:PMC7330481
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 65
  verified: 64
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0004573
    reported_labels:
    - MONDO
    ontology_label: ariboflavinosis
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ariboflavinosis
- **MONDO ID:** MONDO:0004573 (if available)
- **Category:** Nutritional

## Research Objectives

Please provide a comprehensive research report on **Ariboflavinosis** covering all of the
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

# Ariboflavinosis: comprehensive disease-characteristics report

**Disease:** Ariboflavinosis  
**Preferred interpretation:** acquired nutritional riboflavin (vitamin B2) deficiency  
**MONDO:** MONDO:0004573, as specified in the query; this identifier should be revalidated against the production MONDO release before database import because public search interfaces did not return a stable term page.  
**Category:** nutritional deficiency  
**Evidence current through:** 16 October 2026

> **Scope distinction.** Ariboflavinosis is primarily an acquired nutritional deficiency. It should not be conflated with autosomal-recessive riboflavin transporter deficiency caused by *SLC52A2* or *SLC52A3*, nor with riboflavin-responsive multiple acyl-CoA dehydrogenase deficiency. Those genetic diseases can produce systemic riboflavin depletion or overlapping biochemical findings but are distinct entities.

---

## Executive summary

Ariboflavinosis is the clinical syndrome produced by insufficient biologically available riboflavin. Riboflavin is converted to flavin mononucleotide (FMN) and flavin adenine dinucleotide (FAD), cofactors for flavoproteins involved in mitochondrial electron transport, fatty-acid oxidation, antioxidant defense, iron handling, and folate, vitamin B6, and niacin metabolism. Classic disease consists of angular cheilitis/stomatitis, cheilosis, magenta glossitis, pharyngeal inflammation, seborrheic dermatitis, ocular irritation or corneal vascularization, and—when severe or prolonged—normocytic anemia with erythroid hypoplasia. The 2023 authoritative review summarizes that “severe riboflavin deficiency…clinically manifests as cheilosis, angular stomatitis, glossitis, seborrheic dermatitis, and severe anemia with erythroid hypoplasia” (McNulty et al., published 21 August 2023; PMID: **37603429**). [7]

Dietary insufficiency, low intake of dairy or animal-source foods, generalized malnutrition, alcohol use disorder, malabsorption, pregnancy/lactation, adolescence, and light exposure during neonatal phototherapy are major risks. Clinical deficiency is uncommon in well-fortified populations, but biochemical deficiency can be frequent even in high-income countries and is under-recognized because population surveys rarely measure functional biomarkers. [7][50]

Diagnosis combines dietary and clinical assessment with biochemical confirmation. Erythrocyte glutathione reductase activation coefficient (EGRac) is the principal functional biomarker: values ≤1.2–1.26 are generally adequate, 1.27–1.39 marginal/suboptimal, and ≥1.40 deficient, although assay methods and cutoffs are not universally standardized. [1][14]

Acquired disease generally responds rapidly and completely to oral riboflavin and dietary correction. A randomized trial of 123 deficient young women found dose-responsive biochemical improvement after 2 or 4 mg/day for eight weeks, with the greatest hemoglobin benefit in women whose baseline EGRac exceeded 1.65 (PMID: **21525198**). [139]

---

# 1. Disease information

## 1.1 Definition

Ariboflavinosis is the clinical expression of riboflavin deficiency. Riboflavin is a water-soluble B vitamin and precursor of FMN and FAD. More than 90% of food riboflavin occurs as FAD or FMN; absorbed riboflavin is converted intracellularly into these coenzymes. Human storage is limited, making continuing dietary supply important. [1]

The MeSH scope note defines it as:

> “A dietary deficiency of riboflavin causing a syndrome chiefly marked by cheilitis, angular stomatitis, glossitis associated with a purplish red or magenta-colored tongue that may show fissures, corneal vascularization, dyssebacia, and anemia.” [117]

## 1.2 Identifiers and synonyms

| Resource | Identifier/name | Notes |
|---|---|---|
| MONDO | **MONDO:0004573** | Supplied target identifier; validate against the current MONDO release before production import |
| ICD-10/ICD-10-CM | **E53.0** | Riboflavin deficiency; includes ariboflavinosis and vitamin B2 deficiency [76] |
| ICD-11 | **5B5B** | Vitamin B2 deficiency [127] |
| MeSH | **D012257** | Riboflavin Deficiency; tree C18.654.521.500.133.699.713 [117] |
| MeSH chemical | **D012256** | Riboflavin [116] |
| KEGG Disease | **H02544** | Riboflavin deficiency [127] |
| OMIM | Not assigned for acquired nutritional ariboflavinosis | OMIM records instead cover specific inherited transporter/metabolic disorders |
| Orphanet | No general acquired-ariboflavinosis record identified | Orphanet separately catalogs riboflavin transporter deficiency, ORPHA:97229 [124] |
| SNOMED CT | Riboflavin deficiency concept available; verify local edition | Coding varies by national release |
| UMLS | Corresponding concepts exist under riboflavin deficiency/ariboflavinosis | Verify current UMLS release |

| Synonym or alternative name | Scope |
|---|---|
| Riboflavin deficiency | Preferred modern clinical name |
| Vitamin B2 deficiency | Common synonym |
| Vitamin B₂ deficiency disease | Descriptive synonym |
| Ariboflavinosis | Clinical syndrome, especially overt deficiency |
| Riboflavin avitaminosis | Older term |
| Hyporiboflavinosis | Sometimes used for low/subclinical status |
| Oculo-oro-genital syndrome | Historical phenotype description; not specific |
| Riboflavin-deficiency syndrome | Descriptive term |

## 1.3 Data provenance

This report is assembled from **aggregated disease-level resources**, nutrition guidelines, reviews, trials, and population studies—not individual EHR records. Some evidence comes from individual case reports or farm outbreaks, but no identifiable patient-level data are presented.

---

# 2. Etiology

## 2.1 Causal and risk factors

| Factor | Role and evidence |
|---|---|
| Insufficient dietary intake | Principal global cause; diets low in milk, dairy, meat, eggs, fortified cereals, and diverse vegetables are high risk. |
| Generalized malnutrition/food insecurity | Riboflavin deficiency commonly coexists with other B-vitamin and mineral deficiencies rather than occurring alone. [111] |
| Vegan or very low-dairy diet | Risk increases if foods or supplements are not fortified; milk is a major contributor in many populations. [50] |
| Alcohol use disorder | Combines poor intake with impaired intestinal absorption and renal conservation; chronic ethanol exposure reduces RFVT1/RFVT3-mediated transport in experimental work (PMID: **23804199**). |
| Malabsorption | Celiac disease, inflammatory bowel disease, pancreatic insufficiency, bacterial overgrowth, bowel resection, and bariatric procedures may reduce uptake. |
| Pregnancy and lactation | Requirements increase to approximately 1.4 and 1.6 mg/day, respectively; low-animal-food diets increase maternal and infant risk. [1] |
| Infancy/adolescence | Rapid growth raises metabolic demand; maternal deficiency can produce low infant stores. |
| Older age | Low dietary diversity, chronic disease, and malabsorption may contribute. |
| Hemodialysis or chronic illness | Increased loss, catabolism, restricted intake, or inflammation can lower status. |
| Neonatal phototherapy or prolonged UV/visible-light exposure | Riboflavin is photosensitive and may be degraded during prolonged light exposure. [1] |
| Endocrine/hepatobiliary disease | Hypothyroidism, adrenal insufficiency, diabetes, hepatic disease, and biliary obstruction have been reported as precipitating or exacerbating conditions. [56] |
| Increased physical activity | May increase flux through flavin-dependent pathways; vegetarian athletes with marginal intake may be vulnerable. |
| Medication effects | Some drugs alter intake, absorption, or urinary excretion, but robust drug-specific causal evidence is limited. Oral contraceptives are not established as a common cause of overt disease. |

No infectious organism directly causes ariboflavinosis. Infection or inflammation can increase metabolic demand and aggravate pre-existing marginal status.

## 2.2 Genetic factors and gene–environment interaction

Acquired ariboflavinosis has **no required causal germline variant**. Relevant genetic relationships are:

| Gene/genotype | Relationship |
|---|---|
| *SLC52A2*, *SLC52A3* | Biallelic pathogenic variants cause distinct riboflavin transporter deficiency syndromes, not ordinary nutritional ariboflavinosis. They impair cellular distribution or intestinal uptake and markedly increase dependence on pharmacologic riboflavin. |
| *SLC52A1* | Placental/systemic transporter; rare defects can contribute to maternal riboflavin deficiency and transient neonatal MADD-like disease. |
| *RFK* | Encodes riboflavin kinase, which generates FMN; no established common ariboflavinosis susceptibility allele. |
| *FLAD1* | Encodes FAD synthase; biallelic defects cause lipid-storage myopathy/MADD-like flavin deficiency, a separate Mendelian disorder. |
| *MTHFR* c.665C>T, historically C677T; rs1801133 | FAD-dependent MTHFR is less stable in 677TT individuals. Low riboflavin status amplifies effects on homocysteine, vitamin B6 status, and blood pressure; supplementation trials have lowered systolic pressure by approximately 5–13 mmHg in selected 677TT adults. [69][70] |
| G6PD deficiency | Does not cause riboflavin deficiency but can invalidate or reduce the sensitivity of EGRac because glutathione reductase behavior is altered. [1] |

### Protective factors

| Protective factor | Evidence-based interpretation |
|---|---|
| Adequate dietary diversity | Regular dairy, eggs, meat/fish, mushrooms, leafy vegetables, and fortified grains reduce risk. |
| Food fortification | Riboflavin-containing flour and cereal fortification protects populations in which unfortified diets are inadequate. |
| Supplement use in high-risk states | Low-dose multivitamin or riboflavin supplementation prevents deficiency when intake or absorption is insufficient. |
| Treating alcohol use disorder or malabsorption | Restores intake/absorption and reduces recurrence. |
| Protecting foods from light | Prevents photodegradation, particularly in milk. |
| Genetic protection | No validated protective allele specific to acquired ariboflavinosis has been established. |

---

# 3. Phenotypes

Clinical signs are not individually sensitive or specific and usually appear in combinations or with other deficiencies. Reliable per-phenotype percentages are unavailable.

| Phenotype | Type and characteristics | Typical temporal/severity pattern | Suggested HPO term |
|---|---|---|---|
| Angular cheilitis/angular stomatitis | Painful erythema, maceration, fissuring at one or both labial commissures | Early/classic; mild–moderate; usually reversible | **HP:0030318 Angular cheilitis** [91] |
| Cheilosis | Dry, swollen, scaly or fissured vermilion lips | Early/classic; fluctuates with status | HP:0000233 Abnormality of the lips; use a more specific local cheilitis term if available |
| Glossitis/magenta tongue | Smooth, painful, intensely red-purple tongue, sometimes fissured | Classic; variable severity | **HP:0000206 Glossitis** |
| Stomatitis/oral mucosal inflammation | Hyperemia, edema, pain, erosions | Early-to-intermediate | **HP:0010280 Stomatitis** |
| Sore throat/pharyngitis | Burning or soreness with pharyngeal hyperemia and edema | Early, nonspecific | HP:0025439 Sore throat; HP:0005363 Abnormality of the pharynx |
| Seborrheic dermatitis-like eruption | Greasy/scaly erythematous lesions around nose, mouth, ears, eyelids, trunk or genital region | Chronic deficiency; mild–moderate | **HP:0001051 Seborrheic dermatitis** |
| Dyssebacia | Altered sebaceous-gland function | Historical/classic description | HP:0000969 Abnormality of the skin |
| Conjunctival irritation | Red, itchy, watery or burning eyes | Early, variable | **HP:0000509 Conjunctivitis** |
| Photophobia | Light sensitivity, usually with ocular surface disease | Uncommon; more advanced | **HP:0000613 Photophobia** |
| Corneal neovascularization/keratitis | New vessels invading cornea, lacrimation, visual discomfort | Rare, prolonged severe deficiency; structural damage may become irreversible | HP:0011496 Abnormal corneal vascularization; HP:0000491 Keratitis |
| Normocytic, normochromic anemia | Low hemoglobin with initially normal MCV/MCH; severe cases may show erythroid hypoplasia | Intermediate/advanced; variable | **HP:0001903 Anemia**; HP:0001897 Normocytic anemia |
| Erythroid hypoplasia | Reduced erythroid marrow production | Severe deficiency, uncommon | HP:0005528 Abnormality of bone-marrow cell morphology |
| Fatigue/weakness | Consequence of anemia and impaired energy metabolism | Nonspecific, usually reversible | **HP:0012378 Fatigue**, HP:0001324 Muscle weakness |
| Pallor/tachycardia | Secondary to anemia | Advanced or combined deficiency | HP:0000980 Pallor; HP:0001649 Tachycardia |
| Hair loss | Diffuse alopecia/telogen effects | Variable and nonspecific | **HP:0001596 Alopecia** |
| Impaired growth | Primarily infants/children with severe or mixed malnutrition | Chronic, severity dependent | **HP:0001510 Growth delay** |
| Reproductive impairment | Reported in severe deficiency; strongest evidence is preclinical/veterinary | Uncommon in humans | HP:0000080 Abnormality of reproductive system |
| Neurologic dysfunction | Peripheral or central abnormalities mainly in severe/prolonged or inherited deficiency | Rare in isolated acquired deficiency | HP:0000707 Abnormality of the nervous system |
| Hepatic degeneration/steatosis | Mainly experimental or severe combined malnutrition | Evidence stronger in animals than humans | HP:0001392 Abnormality of the liver; HP:0001397 Hepatic steatosis |
| Low EGR/FAD saturation | Functional laboratory abnormality | Preclinical/subclinical stage | No established disease-specific HPO term; represent with assay observation |
| Low urinary riboflavin | Laboratory abnormality reflecting low recent intake/body saturation | Early biochemical deficiency | HP:0011034 Abnormality of the urinary system is too broad; use LOINC measurement plus value |

### Quality-of-life effects

No validated ariboflavinosis-specific EQ-5D, SF-36, or PROMIS study was identified. Painful oral lesions may impair eating and speaking; dermatitis and alopecia can affect appearance and comfort; photophobia impairs visual activities; and anemia causes fatigue, exercise intolerance, and reduced work or school performance. These impacts are clinically plausible but lack disease-specific quantitative utility estimates.

---

# 4. Genetic and molecular information

## 4.1 Causal genes and variants

| Feature requested | Acquired nutritional ariboflavinosis |
|---|---|
| Required causal gene | None |
| Pathogenic variant set | Not applicable |
| Somatic variants | Not applicable |
| Chromosomal abnormality | None established |
| Mendelian inheritance | None |
| Penetrance/anticipation/mosaicism | Not applicable |
| Founder effects/carrier frequency | Not applicable |
| Routine ClinVar interpretation | Not indicated for typical acquired disease |
| Modifier genes | *MTHFR* C677T is the best-characterized nutrigenetic modifier, particularly for homocysteine and blood pressure |
| Epigenetic signature | No clinically validated disease-specific methylation or chromatin signature |

When severe neurologic, respiratory, auditory, or MADD-like abnormalities accompany low riboflavin, sequence-based evaluation of *SLC52A2*, *SLC52A3*, *SLC52A1*, *ETFA*, *ETFB*, *ETFDH*, *FLAD1*, and other flavoprotein-pathway genes may identify a **different inherited disorder**.

## 4.2 Relevant molecular entities

| Entity | Identifier suggestion | Function |
|---|---|---|
| Riboflavin | CHEBI:17015 | Vitamin B2; precursor of FMN/FAD |
| FMN | CHEBI:17621 | Flavin mononucleotide; redox cofactor |
| FAD | CHEBI:16238 | Flavin adenine dinucleotide; redox cofactor |
| RFVT1 | *SLC52A1* | Systemic/placental riboflavin transport |
| RFVT2 | *SLC52A2* | Tissue riboflavin transport, especially nervous system |
| RFVT3 | *SLC52A3* | Major intestinal riboflavin uptake transporter |
| Riboflavin kinase | *RFK* | Riboflavin → FMN |
| FAD synthase | *FLAD1* | FMN → FAD |
| Glutathione reductase | *GSR* | FAD-dependent antioxidant enzyme; basis of EGRac |
| MTHFR | *MTHFR* | FAD-dependent folate/one-carbon enzyme |
| Succinate dehydrogenase | SDHA–D complex | FAD-linked TCA-cycle/electron-transport complex II |
| Acyl-CoA dehydrogenases | Multiple genes | FAD-dependent fatty-acid and amino-acid oxidation |

---

# 5. Environmental and lifestyle information

| Exposure or behavior | Effect |
|---|---|
| Low animal-source-food intake without fortification | Reduces riboflavin intake |
| Food insecurity and monotonous cereal-based diets | Increase risk, particularly where flour is not fortified |
| Boiling and discarding cooking water | Increases loss of water-soluble riboflavin; approximately twice as much may be lost as with steaming or microwaving. [1] |
| Visible/UV light exposure of milk or solutions | Photodegrades riboflavin |
| Chronic heavy alcohol consumption | Reduces intake, intestinal absorption, and renal reabsorption |
| Smoking | Not established as an independent specific cause; may correlate with poorer diet |
| Physical exercise | Raises metabolic demand; usually relevant only with marginal intake |
| Occupational toxin/radiation exposure | No established specific causal exposure |
| Infection | Not a primary cause; systemic stress may expose marginal status |
| Gut microbiome | Some microbes synthesize or use riboflavin, but microbiome manipulation is not an established treatment for ariboflavinosis |

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Inadequate intake, malabsorption, excess loss, photodegradation, increased requirement, or impaired transport leads to reduced systemic riboflavin availability.**
2. **Reduced riboflavin availability leads to decreased synthesis and tissue saturation of FMN and FAD.**
3. **FMN/FAD depletion leads to reduced activity or stability of multiple flavoproteins**, including glutathione reductase, succinate dehydrogenase, acyl-CoA dehydrogenases, MTHFR, and enzymes required for vitamin B6 and niacin metabolism.
4. **Impaired glutathione reductase and flavin-dependent redox reactions lead to reduced antioxidant capacity and increased reactive oxygen species/lipid peroxidation.**
5. **Impaired mitochondrial electron transport and fatty-acid oxidation lead to reduced ATP generation and altered lipid metabolism.**
6. **These changes branch into:**
   1. **High-turnover epithelial injury**, which leads to cheilosis, angular stomatitis, glossitis, pharyngitis, and seborrheic dermatitis.
   2. **Disordered iron absorption, mobilization, and utilization**, which leads to impaired erythropoiesis and normocytic anemia.
   3. **Ocular epithelial and retinal metabolic stress**, which leads to conjunctival symptoms and, in prolonged severe disease, corneal vascularization or retinal dysfunction.
   4. **Impaired MTHFR/one-carbon metabolism**, which can lead to elevated homocysteine and genotype-dependent vascular effects.
   5. **Impaired hepatic lipid oxidation**, which may lead to lipid accumulation; this branch is demonstrated mainly in animal models and is only inferred as a major manifestation of human nutritional disease.
7. **Sustained cellular energetic failure and oxidative injury lead to tissue dysfunction and, if prolonged, potentially irreversible structural damage such as cataract or retinal/corneal change.**

## 6.2 Molecular and cellular detail

Dietary FAD and FMN are hydrolyzed before absorption; free riboflavin is absorbed predominantly in the proximal small intestine through RFVT3 and related transporters. Intracellular RFK phosphorylates riboflavin to FMN, and FLAD1/FAD synthase adenylates FMN to FAD. Human transporter experiments show that riboflavin itself, rather than FMN or FAD, is efficiently moved through RFVT proteins (PMID: **29093349**). [71]

FAD-dependent succinate dehydrogenase connects the tricarboxylic-acid cycle to mitochondrial respiratory complex II. Acyl-CoA dehydrogenases transfer electrons during β-oxidation. Loss of flavin saturation therefore impairs both carbohydrate-linked and lipid-derived energy production.

Glutathione reductase requires FAD to regenerate reduced glutathione. EGRac measures how much erythrocyte glutathione reductase activity increases after exogenous FAD is added: a large increase indicates poor in-vivo FAD saturation. [14]

The 2023 review’s abstract states:

> “Riboflavin, in its cofactor forms flavin adenine dinucleotide (FAD) and flavin mononucleotide (FMN), plays fundamental roles in energy metabolism, cellular antioxidant potential, and metabolic interactions with other micronutrients, including iron, vitamin B6, and folate.”  
> —McNulty et al., 21 August 2023, PMID: **37603429** [7]

### Suggested GO and CL annotations

| Mechanism | Suggested GO biological-process terms | Principal cell types |
|---|---|---|
| Riboflavin transport | GO:0032218 riboflavin transport; transmembrane transport | Intestinal epithelial cell/enterocyte, **CL:0000584** |
| FMN/FAD synthesis | Flavin-containing compound biosynthetic process; riboflavin metabolic process | Broadly ubiquitous |
| Mitochondrial energy failure | GO:0006099 tricarboxylic acid cycle; GO:0022900 electron transport chain; GO:0006119 oxidative phosphorylation | Enterocytes, keratinocytes, erythroid cells, hepatocytes, neurons |
| Fatty-acid oxidation impairment | **GO:0006635 fatty acid beta-oxidation** | Hepatocyte **CL:0000182**, myocyte, retinal pigment epithelial cell |
| Oxidative stress | **GO:0006979 response to oxidative stress**; GO:0006749 glutathione metabolic process | Keratinocyte **CL:0000312**, RPE, hepatocyte, erythrocyte |
| Erythropoiesis impairment | **GO:0030218 erythrocyte differentiation**; GO:0042541 hemoglobin biosynthesis | Erythroid progenitor **CL:0000764**, erythroblast **CL:0000765** |
| Epithelial injury | GO:0030216 keratinocyte differentiation; GO:0008544 epidermis development | Oral keratinocyte, epidermal keratinocyte |
| Apoptosis under severe stress | **GO:0006915 apoptotic process** | Tissue dependent |
| Inflammatory response | **GO:0006954 inflammatory response** | Keratinocytes, epithelial cells, macrophages |
| Bone effect—preclinical | GO:0001503 ossification; BMP signaling | Osteoblast **CL:0000062** |

## 6.3 Recent mechanistic research, 2022–2024

| Study | Model/evidence | Main result |
|---|---|---|
| Bian et al., 2023; PMID **37788723** | Riboflavin-deficient rats and osteoblast cultures | Lower bone mineral density, bone alkaline phosphatase, phosphorus and calcium; impaired mineralization through p38 MAPK/BMP-2/Smad1/5/9 signaling. The abstract concludes that deficiency “causes osteoblast malfunction and retards bone matrix mineralization.” [161] |
| Wang et al., 2024; PMID **38169398** | Dietary mouse model | Riboflavin deficiency increased hepatic lipid accumulation, with a synergistic effect in high-fat-fed mice. This does not establish clinical fatty liver as a routine human manifestation. [163] |
| Sinha et al., 2022; PMID **35738087** | Diet-induced mouse deficiency | Oxidative and lipid-metabolic abnormalities preceded severe retinal dysfunction and structural neural-retina/RPE change. [162] |
| McNulty et al., 2023; PMID **37603429** | Human evidence synthesis | Highlighted widespread unrecognized subclinical deficiency and potential consequences including anemia and hypertension. [7] |

No disease-defining human single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omic atlas was identified. Transcriptomic, lipidomic, and metabolomic findings remain predominantly preclinical.

---

# 7. Anatomical structures affected

| Level | Structures/cells | Ontology suggestions |
|---|---|---|
| Primary organs | Lips, oral mucosa, tongue, pharynx, skin, conjunctiva/cornea, erythroid marrow | UBERON:0001833 lip; UBERON:0000165 mouth; UBERON:0001723 tongue; UBERON:0001042 pharynx; UBERON:0002097 skin; UBERON:0000964 cornea; UBERON:0002371 bone marrow |
| Secondary organs | Liver, nervous system, retina, reproductive tissues; strongest evidence in severe, inherited, or experimental disease | UBERON:0002107 liver; UBERON:0001017 central nervous system; UBERON:0000966 retina |
| Tissues | Stratified squamous epithelium, sebaceous units, corneal epithelium, erythroid tissue | CL:0000312 keratinocyte; CL:0000764 erythroid progenitor |
| Cells | Enterocytes, oral/epidermal keratinocytes, erythroblasts/erythrocytes, hepatocytes, RPE cells, neurons, osteoblasts | CL:0000584, CL:0000312, CL:0000232, CL:0000182, CL:0000062 |
| Subcellular compartments | Cytosol, mitochondria, mitochondrial inner membrane/electron-transfer complexes | GO:0005737 cytoplasm; GO:0005739 mitochondrion; GO:0005743 mitochondrial inner membrane |
| Lateralization | Usually bilateral or symmetric for oral commissures, dermatitis, and ocular disease; no intrinsic right/left preference | Not applicable |

---

# 8. Temporal development

| Feature | Typical pattern |
|---|---|
| Onset | Any age; determined by intake, stores, growth, pregnancy, illness, alcohol exposure, or malabsorption |
| Earliest phase | Biochemical depletion with elevated EGRac or reduced urinary riboflavin, often asymptomatic |
| Early clinical phase | Fatigue, mouth soreness, sore throat, burning/itchy eyes |
| Established disease | Angular cheilitis, cheilosis, glossitis, stomatitis and seborrheic dermatitis |
| Advanced disease | Anemia, corneal neovascularization, severe epithelial or neurologic/hepatic abnormalities |
| Course | Usually subacute or chronic/insidious; fluctuates with diet and underlying disease |
| Progression rate | Days to weeks with severe restriction; generally slower with marginal intake |
| Remission | Treatment-induced remission is expected; spontaneous improvement can occur if diet improves |
| Duration | Reversible nutritional disorder rather than lifelong disease, unless the cause persists |
| Critical periods | Pregnancy, lactation, infancy, adolescence, severe malnutrition, and prolonged malabsorption |
| Irreversibility | Early lesions reverse readily; established cataract or chronic retinal/corneal structural change may not reverse. [1] |

---

# 9. Epidemiology, inheritance and population

There are no reliable global incidence or prevalence rates for **clinical ariboflavinosis per 100,000**. Studies generally report biochemical deficiency, and estimates vary sharply by assay and cutoff.

| Population/statistic | Finding and interpretation |
|---|---|
| United States | Clinical deficiency is considered very rare; fewer than 6% had dietary intake below the EAR in a 2003–2006 NHANES analysis, but NHANES did not establish biochemical prevalence using EGRac. [1] |
| Cambodia, women of reproductive age | Approximately 80% deficiency at EGRac ≥1.40 in prior urban/rural studies. [15] |
| Canadian women of reproductive age | Around 40% biochemical deficiency in one study; low status was associated with lower hemoglobin and more anemia (PMID: **31318024**). |
| Malaysian women of reproductive age | Approximately 71% biochemical deficiency in the same comparative literature. |
| United Kingdom adolescents | Older surveys using lower cutoffs reported very high poor-status estimates; cutoff and assay differences limit comparison. |
| Global pattern | Overt disease is concentrated in low-income settings; subclinical deficiency also occurs in high-income countries and is probably undercounted. [7] |
| Sex distribution | No intrinsic sex-linked disease; women may have higher observed risk because of pregnancy/lactation, menstrual iron demands, diet, and study selection. |
| Geographic distribution | Higher risk in South Asia and eastern/southern Africa and wherever dairy/animal-food consumption and fortification are low. |
| Incidence | Not established |
| Mortality rate | Not established; isolated acquired disease is rarely recorded as an underlying cause of death |

The disease is **non-Mendelian and acquired**. Penetrance, genetic anticipation, germline mosaicism, consanguinity, and carrier frequency are therefore not applicable. Familial clustering may reflect shared diet or socioeconomic conditions.

---

# 10. Diagnostics

## 10.1 Recommended diagnostic approach

1. Identify compatible oral, skin, ocular, or hematologic findings.
2. Assess diet, dairy/animal-food intake, fortification, alcohol exposure, pregnancy/lactation, malabsorption, bariatric surgery, and other deficiencies.
3. Obtain EGRac when available.
4. Measure urinary or blood riboflavin if EGRac is unavailable.
5. Check CBC, reticulocytes, ferritin/iron indices, folate, B12, B6, and other nutritional markers.
6. Consider a monitored therapeutic trial of riboflavin.
7. If neurologic, respiratory, auditory, hypoglycemic, or MADD-like disease is disproportionate, evaluate for inherited transporter or flavoprotein disorders.

## 10.2 Laboratory tests

| Test | Interpretation | Limitations |
|---|---|---|
| EGRac | Commonly ≤1.2–1.26 adequate; 1.27–1.39 suboptimal; ≥1.40 deficient | Methods/cutoffs not fully standardized; unreliable in G6PD deficiency; high values do not linearly grade severity [1] |
| 24-hour urinary riboflavin | ≥120 µg/day typical of replete adults; <40 µg/day indicates deficiency | Reflects recent intake and renal function more than long-term status [1] |
| Urinary riboflavin/creatinine | <27 µg/g creatinine is commonly treated as deficient | Catabolism, age, drugs, and renal status affect results |
| Erythrocyte riboflavin | <10 µg/dL RBC or <170 nmol/L suggested as low | Less widely standardized |
| Plasma riboflavin/FMN/FAD | Can support assessment | Sensitive to recent intake; no universal diagnostic threshold |
| CBC | Normocytic/normochromic anemia; severe disease may show erythroid hypoplasia | Mixed deficiencies may cause microcytosis or macrocytosis |
| Bone marrow | Erythroid hypoplasia in severe disease | Not indicated solely to diagnose riboflavin deficiency |
| Therapeutic response | Improvement after supplementation supports diagnosis | Not specific if multiple vitamins are administered |

EGRac is a ratio of FAD-stimulated to basal erythrocyte glutathione-reductase activity. The standardized protocol literature emphasizes that it reflects the degree to which enzyme activity is limited by riboflavin availability. [14]

### Imaging, electrophysiology and biopsy

Routine imaging, EEG, EMG, nerve conduction studies, biopsy, karyotyping, or FISH are **not indicated** in uncomplicated ariboflavinosis. They may be appropriate only for alternative diagnoses or suspected inherited riboflavin transporter deficiency.

## 10.3 Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| Iron deficiency | Microcytosis, low ferritin/transferrin saturation; can coexist |
| Niacin deficiency/pellagra | Photosensitive dermatitis, diarrhea, neuropsychiatric dysfunction |
| Vitamin B6 deficiency | Seborrheic dermatitis, cheilitis, neuropathy, sideroblastic anemia |
| Folate/B12 deficiency | Usually macrocytic anemia; B12 may cause neurologic deficits |
| Zinc deficiency | Periorificial/acral dermatitis, alopecia, diarrhea, impaired wound healing |
| Oral candidiasis | Pseudomembranes or positive fungal testing |
| Infectious angular cheilitis | *Candida* or *Staphylococcus*, local maceration/denture factors |
| Contact or actinic cheilitis | Exposure distribution and patch-testing/history |
| Seborrheic or atopic dermatitis | Typical distribution without biochemical deficiency |
| Riboflavin transporter deficiency | Sensorimotor neuropathy, deafness, bulbar/respiratory disease; biallelic *SLC52A2/3* variants |
| MADD | Hypoglycemia, metabolic acidosis, characteristic acylcarnitines/organic acids; genetic causes |
| Eating disorder/general malnutrition | Multiple simultaneous deficiencies and systemic signs |

## 10.4 Genetic and omics testing

| Test | Role |
|---|---|
| Single-gene/panel sequencing | Not for ordinary dietary disease; use for severe atypical neurologic/metabolic cases |
| WES/WGS | Reserved for unresolved suspected inherited flavin disorder |
| CMA/karyotype/FISH | No established role |
| mtDNA/repeat-expansion testing | No routine role |
| RNA-seq/proteomics/metabolomics | Research or complex metabolic-disease evaluation, not standard ariboflavinosis diagnosis |
| Newborn screening | No population newborn screen for acquired ariboflavinosis |
| Population screening | EGRac may be used in nutritional surveys but is not routine clinical screening |

---

# 11. Outcome and prognosis

| Outcome domain | Current understanding |
|---|---|
| Survival | No disease-specific 5- or 10-year survival estimates; prompt treatment of acquired deficiency restores normal expected survival |
| Mortality | Isolated nutritional deficiency is rarely fatal; severe generalized malnutrition or unrecognized inherited transporter deficiency carries greater risk |
| Recovery | Oral lesions, dermatitis, biochemical abnormalities, and anemia usually improve over days to weeks |
| Recurrence | Likely if food insecurity, alcohol use, malabsorption, or an uncorrected restrictive diet persists |
| Long-term disability | Uncommon after prompt treatment |
| Irreversible complications | Cataract, chronic corneal or retinal injury, and neurologic damage are possible after prolonged severe disease, although much evidence derives from experimental or genetic deficiency |
| Prognostic factors | Duration, baseline EGRac, severity of anemia, coexisting deficiencies, malabsorption, and treatment adherence |
| Prognostic biomarkers | No validated biomarker beyond severity/persistence of biochemical deficiency and response to supplementation |
| Quality of life | No disease-specific validated instrument or utility estimate |

Women with the poorest baseline status obtained the largest hematologic benefit in RIBOFEM, suggesting that baseline EGRac is a treatment-response modifier rather than a formally validated prognostic biomarker. [133]

---

# 12. Treatment

## 12.1 Treatment strategy

| Intervention | Use and dose | Evidence/outcome | Ontology suggestions |
|---|---|---|---|
| Oral riboflavin | Physiologic replacement often **2–4 mg/day for about 8 weeks**; some clinical references recommend **5–30 mg/day in divided doses until recovery** | Corrects biochemical deficiency and usually resolves early clinical signs [191][193] | NCIT: Riboflavin; CHEBI:17015 |
| Diet optimization | Add milk/yogurt, eggs, meat/fish, mushrooms, leafy vegetables and fortified cereals/grains | Corrects cause and prevents recurrence | NCIT: Dietary Intervention |
| B-complex/multivitamin replacement | Appropriate when generalized malnutrition or several deficiencies coexist | Ariboflavinosis rarely occurs in isolation; avoid treating B2 alone when broader deficiencies are likely | NCIT: Vitamin Supplementation |
| Intramuscular/parenteral riboflavin | For inability to tolerate or absorb oral therapy; uncommon | Clinical guidance supports parenteral treatment when oral administration is not feasible [191] | NCIT: Intramuscular Injection |
| Treat underlying disease | Alcohol-use treatment, gluten-free diet for celiac disease, management of IBD/pancreatic insufficiency, nutrition after bariatric surgery | Prevents persistent or recurrent depletion | Condition-specific terms |
| High-dose riboflavin | **10–50 mg/kg/day or higher** for inherited RTD/MADD—not routine acquired ariboflavinosis | Potentially life-saving in genetically determined disease | NCIT: High-Dose Therapy; Riboflavin |

### Primary human intervention evidence

The RIBOFEM randomized, double-blind trial enrolled 123 women aged 19–25 years with EGRac >1.40; 119 completed treatment with placebo, 2 mg/day, or 4 mg/day for eight weeks. Supplementation produced a significant dose-responsive improvement in riboflavin status, and improved status correlated with increased hemoglobin. Women with baseline EGRac >1.65 had the greatest hematologic response. Trial registration: **ISRCTN35811298**; PMID: **21525198**. [138][139]

The authors concluded:

> “Moderately poor riboflavin status can affect iron status: the lower the riboflavin status, the greater the hematologic benefits of improving status.” [139]

## 12.2 Safety and adverse effects

Riboflavin has low toxicity because intestinal absorption is saturable and excess is excreted in urine. No tolerable upper intake level has been established. Doses up to 400 mg/day for at least three months have not produced consistent serious toxicity, although absence of a UL should not be interpreted as proof that unlimited intake is harmless. Harmless bright-yellow urine is common. Clinically important drug interactions are not established. [1]

## 12.3 Advanced, surgical and experimental therapies

| Modality | Applicability |
|---|---|
| Surgery | None for the deficiency itself |
| Gene therapy/CRISPR | None for acquired ariboflavinosis |
| Cell therapy | None |
| RNA therapy | None |
| Immunotherapy | None |
| Rehabilitation | Rarely needed; nutrition rehabilitation and physical therapy may be useful after severe generalized malnutrition |
| Clinical trials specifically treating ariboflavinosis | No active pivotal trial identified |
| Related research | NCT03151096 studies 5 mg/day riboflavin in a riboflavin-deplete Gambian population; NCT05488106 studies 1.6, 5 and 20 mg/day for vascular outcomes; NCT05803811 examines colon-delivered vitamin B2 and microbiota. These are not registration trials for clinical ariboflavinosis. [177][178][183] |

Pharmacogenomics is not used to set replacement doses. *MTHFR* C677T-directed riboflavin treatment for hypertension is an emerging personalized-nutrition application, not standard ariboflavinosis therapy.

---

# 13. Prevention

| Prevention level | Measures |
|---|---|
| Primary | Dietary diversity; dairy or fortified alternatives; eggs, meat/fish or appropriate plant/fortified sources; food-security programs; flour/cereal fortification; low-dose supplementation in high-risk people |
| Secondary | Dietary-risk assessment and biochemical testing in malnutrition, pregnancy with restricted diet, alcohol use disorder, malabsorption, bariatric patients, unexplained cheilosis/glossitis, or anemia |
| Tertiary | Treat deficiency and co-deficiencies, correct underlying malabsorption or alcohol exposure, monitor EGRac/hemoglobin, and prevent ocular or neurologic complications |
| Immunization | Not applicable |
| Genetic counseling | Not indicated for dietary ariboflavinosis; indicated if inherited transporter/metabolic disease is diagnosed |
| Prenatal/carrier testing | Not applicable for acquired disease |
| Environmental control | Protect milk and riboflavin-containing solutions from light; minimize avoidable cooking-water losses |
| Prophylaxis | Prenatal or general multivitamin supplementation when diet is inadequate; no vaccine or antimicrobial prophylaxis |

WHO recommends considering wheat-flour fortification when industrially produced flour is widely consumed, with nutrient selection based on documented population needs, food-consumption patterns, effects on the food vehicle, other fortification programs, and cost. [208] WHO materials list riboflavin or riboflavin-5′-phosphate at a suggested average fortification level of approximately 2.0 mg/kg in relevant flour scenarios. [206]

### Intake targets for prevention

| Population | US RDA or AI |
|---|---:|
| Birth–6 months | 0.3 mg/day |
| 7–12 months | 0.4 mg/day |
| 1–3 years | 0.5 mg/day |
| 4–8 years | 0.6 mg/day |
| 9–13 years | 0.9 mg/day |
| Male 14+ years | 1.3 mg/day |
| Female 14–18 years | 1.0 mg/day |
| Female 19+ years | 1.1 mg/day |
| Pregnancy | 1.4 mg/day |
| Lactation | 1.6 mg/day |

These are prevention/adequacy targets, not necessarily therapeutic doses. [1]

---

# 14. Other species and naturally occurring disease

| Species | NCBI Taxon | Natural/veterinary phenotype | Relevance |
|---|---:|---|---|
| Domestic pig, *Sus scrofa domesticus* | 9825 | Reproductive failure, premature farrowing, stillbirths, weak neonates and neonatal mortality | A 2023 two-farm report documented 60–100% intra-litter mortality; supplementation one month before farrowing eliminated observed stillbirth and intra-litter mortality (PMID: **37143142**). [146] |
| Chicken, *Gallus gallus domesticus* | 9031 | Poor growth, enlarged sciatic/brachial nerve sheaths, peripheral demyelination, leg weakness and curled-toe paralysis; reduced egg production and hatchability | Classic veterinary manifestation; restoration of dietary riboflavin reverses early production problems, but advanced nerve damage may persist. [149] |
| Turkey and other poultry | Species dependent | Curled-toe paralysis, growth failure and hatchability defects | Feed formulation is the main preventive application |
| Dog, *Canis lupus familiaris* | 9615 | Experimental or dietary deficiency causes poor growth, anorexia, weight loss, weakness, ataxia and corneal opacity | Naturally isolated disease is uncommon in animals fed complete commercial diets |
| Cat, *Felis catus* | 9685 | Experimental deficiency causes anorexia, weight loss, alopecia, bilateral cataracts, testicular hypoplasia and hepatic fat accumulation | Primarily comparative and nutritional relevance |
| Rat, *Rattus norvegicus* | 10116 | Growth failure, dermatitis, nerve/myelin pathology, endocrine and reproductive atrophy, low bone mineralization | Major induced research model |
| Mouse, *Mus musculus* | 10090 | Growth retardation, ocular/retinal changes, altered lipid metabolism, and death in severe transporter or dietary models | Widely used mechanistic model |

The disorder is nutritional and **not transmissible or zoonotic**. Orthologs of *SLC52A1–3*, *RFK*, *FLAD1*, *GSR*, and other flavoprotein genes are evolutionarily conserved.

No specific breed ontology association is established; disease reflects feed composition and physiological state more than breed.

---

# 15. Model organisms and experimental systems

| Model | Induction/genotype | Phenotypes recapitulated | Applications and limitations |
|---|---|---|---|
| Dietary riboflavin-deficient rat | Riboflavin-depleted feed | Growth failure, dermatitis, anemia-related abnormalities, nerve pathology, reduced bone mineral density | Useful for dose-response, bone and iron studies; severe purified-diet depletion may exceed typical human exposure |
| Dietary riboflavin-deficient mouse | Deficient feed, sometimes with high fat | Retinal/RPE oxidative stress, impaired retinal function, hepatic lipid accumulation | Models metabolic and ocular mechanisms; human clinical retinal/hepatic relevance remains uncertain |
| Intestinal *Slc52a3* conditional-knockout mouse | Cre/Lox intestinal RFVT3 deletion | Systemic deficiency, growth retardation, low bone density, lethargy, ocular surface disease; nearly two-thirds died at 6–12 weeks; high-dose riboflavin rescued growth and oxidative-stress markers | Demonstrates intestinal transport biology, but models genetic transporter loss rather than ordinary dietary ariboflavinosis (PMID associated with 2015 report). [16] |
| Constitutive *Slc52a3* knockout mouse | Germline knockout | Fetal/neonatal deficiency, hypoglycemia, hyperlipidemia, cortical-development abnormalities and neonatal death | Model of RTD/maternal-fetal transport, not uncomplicated acquired disease [19] |
| Osteoblast culture | Riboflavin-depleted medium | Impaired matrix mineralization and p38 MAPK/BMP-2/Smad signaling | Mechanistic dissection of bone phenotype; lacks whole-body homeostasis |
| Retinal/RPE systems | Dietary mouse model and retinal assays | Oxidative stress, lipid dysregulation, RPE atrophy, retinal dysfunction | Demonstrates plausibility of ocular injury; exposure duration and severity limit clinical extrapolation |
| Poultry feed-depletion model | Riboflavin-deficient feed | Peripheral demyelination and curled-toe paralysis | Highly sensitive model for neural and husbandry outcomes; avian physiology differs from humans |
| Pig gestational deficiency | Inadequate feed supplementation | Prematurity, stillbirth and neonatal death | Strong real-world reproductive model; human obstetric translation is indirect |

A useful translational hierarchy is:

1. **Human clinical evidence:** mucocutaneous syndrome, biochemical deficiency, anemia association, treatment response.
2. **Human observational/nutrigenetic evidence:** interactions with iron, B6, folate and *MTHFR*.
3. **Animal evidence:** retinal degeneration, hepatic lipid accumulation, bone impairment and reproductive failure.
4. **Cellular evidence:** oxidative stress, mitochondrial dysfunction, apoptosis and altered BMP/MAPK signaling.
5. **Inferred mechanisms:** direct attribution of common human fatty liver, osteoporosis, or neurodegeneration to isolated riboflavin deficiency remains unproven.

---

# Evidence gaps and curation recommendations

| Knowledge-base field | Recommended representation |
|---|---|
| Disease class | Acquired nutritional/metabolic disease |
| Etiologic agent | Insufficient bioavailable riboflavin |
| Required gene | None |
| Phenotype frequency | Use “characteristic,” “variable,” or “rare”; avoid invented percentages |
| Primary biomarker | EGRac |
| Diagnostic threshold | Store ≥1.40 as widely accepted but annotate assay/cutoff uncertainty |
| Standard treatment | Oral riboflavin plus correction of diet and co-deficiencies |
| Prognosis | Excellent with prompt treatment |
| Inherited differential | Riboflavin transporter deficiency and riboflavin-responsive MADD |
| Evidence gaps | No global incidence; no robust disease-specific QOL data; no validated omics signature; sparse modern prospective natural-history studies |
| Ontology caution | Validate all HPO, GO, CL, UBERON, NCIT and MONDO accessions against the current release before automated import |

The most important recent expert conclusion is that overt ariboflavinosis is only the visible end of a larger problem: as the 2023 review states, “subclinical deficiency may be much more widespread, including in high-income countries,” but often remains undetected because riboflavin biomarkers are rarely measured (PMID: **37603429**). [7]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMC:PMC7330481` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 65 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0004573` (2 mentions) - the report calls it "MONDO"; MONDO calls it **ariboflavinosis**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.