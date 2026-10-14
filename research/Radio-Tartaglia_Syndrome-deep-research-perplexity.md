---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:25.486118'
end_time: '2026-10-09T20:59:35.928708'
duration_seconds: 250.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Radio-Tartaglia Syndrome
  mondo_id: MONDO:0859143
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
citation_count: 55
reference_validation:
  total_references: 13
  verified: 12
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.077
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 12
  on_topic: 5
  unresolved_references:
  - DOI:10.1371/journal.pgen.1008333&type=printable
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 23
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 10
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - OMIM
  - Taxon
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Radio-Tartaglia Syndrome
- **MONDO ID:** MONDO:0859143 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Radio-Tartaglia Syndrome** covering all of the
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

# Radio–Tartaglia syndrome: disease-characteristics research report

**Radio–Tartaglia syndrome (RATARS; MONDO:0859143) is a rare, autosomal-dominant, *SPEN*-related neurodevelopmental disorder.** Its best-established molecular cause is a heterozygous truncating *SPEN* variant consistent with haploinsufficiency. Developmental and speech delay, intellectual disability, hypotonia, behavioral differences, and variable congenital anomalies define the clinical picture. The principal human evidence remains a study of **34 affected individuals from 33 families**; consequently, many frequencies below are *observations among assessed people*, not population estimates. [63][27][16][2]

**Evidence convention.** “Human” denotes affected-person observations; “mouse,” “fly,” and “in vitro” denote experimental evidence that must not be treated as proof of the corresponding mechanism or treatment effect in patients. Percentages retain their published denominators. This is an **aggregated disease-level report**, not an individual-patient EHR extract. [16][31]

## 1. Disease information and identifiers

| Identifier or name | Value and interpretation |
|---|---|
| Preferred name | Radio–Tartaglia syndrome; abbreviation **RATARS**. [2] |
| Alternative name | *SPEN*-related neurodevelopmental disorder. **SHARP** and **MINT** are names for the *protein*, not separate disease names. [63][44] |
| MONDO | **MONDO:0859143**. [63] |
| OMIM phenotype | **619312**; *SPEN* gene OMIM **613484**. [27] |
| Orphanet | **ORPHA:662234**. [27][63] |
| MedGen | Concept **C5543339**; UID **1778557**. [62] |
| MeSH | **No syndrome-specific descriptor verified.** D065886, sometimes cross-referenced from disease resources, means the broader category **Neurodevelopmental Disorders**. [64][77] |
| ICD-10/ICD-11 | **No syndrome-specific code verified.** ICD-10-CM **Q87.89** is a general “other specified congenital malformation syndromes” category, **not** an established RATARS-specific mapping; an ICD-11-specific mapping was not established. [80][86] |

In the foundational paper’s abstract, the authors describe “**34 individuals with truncating variants in SPEN**” and a disorder overlapping proximal 1p36 deletion syndrome (Radio *et al.*, electronically published **16 February 2021**, PMID **33596411**, DOI [10.1016/j.ajhg.2021.01.015](https://doi.org/10.1016/j.ajhg.2021.01.015)). [45][16]

## 2. Etiology, risks, protection, and gene–environment interaction

| Factor | Disease-specific evidence and interpretation |
|---|---|
| Primary cause | Heterozygous, predominantly **de novo**, protein-truncating variants of *SPEN* at **1p36.21–p36.13**. Familial transmission from an affected parent establishes autosomal-dominant inheritance. Loss of function/haploinsufficiency is the supported disease model; individual variants in the original series were **not** all functionally tested. [27][22][30] |
| Chromosomal contribution | A **proximal 1p36 deletion encompassing *SPEN*** can contribute to overlapping findings, but a multigene deletion is not interchangeable with an isolated *SPEN* variant. Distal 1p36 deletions can also produce overlapping findings **without deleting *SPEN***. [16][31] |
| Other genetic risks or modifiers | No established susceptibility locus, severity-modifying allele, founder variant, or protective human allele was identified in the reviewed RATARS studies. Variant position did not show a clear genotype–phenotype relationship in the 34-person series. [27][16] |
| Sex and age effects | These affect *observed expression*, not proven risk of acquiring the mutation: obesity occurred in **6/16 assessed females versus 0/15 males**; BMI generally rose after approximately age four. [16] |
| Environmental, lifestyle, or infectious causes | None established for this Mendelian syndrome. In particular, no toxin, infection, smoking exposure, or dietary pattern has been shown to cause RATARS. [27][16] |
| Protective factors and gene–environment interaction | **No protective intervention is validated in humans.** In *Drosophila* with experimental *Spen* depletion, diet changed metabolic outcomes: extra yeast partly rescued larval adiposity/development, while effects differed in adults. This is an experimental gene–diet interaction, **not a patient dietary recommendation** (Gillette *et al.*, online **27 February 2020**, PMID **32107279**). [119] |

## 3. Phenotypes

**How to read the table:** “Frequency” is the count among people *evaluated for that feature* in the original 34-person cohort, as tabulated in the 2024 Korean case comparison. A later case does not change those original denominators. Proposed HPO labels/IDs are annotation suggestions, not a claim that each has been independently validated as a syndrome-specific association. Most developmental findings arise in infancy or childhood; cohort-wide, feature-specific severity and progression were generally not measured. Functional impacts are clinical implications, **not measured EQ-5D, SF-36, or PROMIS results**. [31][16]

| Phenotype and type | Onset, severity, course and frequency | Function or quality-of-life relevance | Suggested HPO term |
|---|---|---|---|
| Global developmental delay; clinical sign | Childhood; variable impairment; **32/33 (97%)** in the detailed 2024 comparison. The original paper’s broader combined delay/intellectual-disability category is **33/33**. [31][16] | Developmental and educational support needs. | Global developmental delay **HP:0001263**. [61] |
| Intellectual disability; clinical sign | Childhood; mild to severe in the cohort; **23/24 (96%)** assessed separately. [31][16] | Variable lifelong learning and adaptive-function needs. | Intellectual disability **HP:0001249**. [61] |
| Delayed speech/language; clinical sign | Childhood; **31/32 (97%)**; the original report described language delay as nearly universal. [31][16] | Communication and educational access. | Delayed speech and language development **HP:0000750**. [61] |
| Delayed gross and fine motor skills; clinical signs | Childhood; **26/30 (87%)** gross and **23/24 (96%)** fine motor; severity variable. [31] | Mobility, play, self-care, handwriting. | Gross motor delay; fine motor delay—verify exact HPO IDs before database entry. |
| Hypotonia; clinical sign | Usually evident early; **22/30 (73%)**. Oral-motor hypotonia: **12/28 (43%)**. [16][31] | Posture, motor milestones, feeding. | Hypotonia **HP:0001252**; oral-motor hypotonia—ID to verify. [61] |
| Behavioral differences; behavioral signs | Childhood onward; broad abnormal-behavior category **22/30 (73%)**. The original narrative also reports behavioral **and/or psychiatric** findings in **81%**, using a different definition. [31][16] | Social participation and caregiver support; individual impact unquantified. | Aggressive behavior **HP:0000718** where applicable. [61] |
| Autism-spectrum features; behavioral sign | **18/28 (64%)** evaluated; variable expression. [31] | Communication, sensory and social-support needs vary. | Autistic behavior **HP:0000729**. [61] |
| Aggressive behavior; behavioral sign | **18/29 (62%)** in the detailed comparison. [31] | May complicate daily functioning and support. | Aggressive behavior **HP:0000718**. [61] |
| Motor stereotypy; behavioral sign | **13/28 (46%)**; course not characterized. [31] | Variable; cannot infer impairment from presence alone. | Motor stereotypy **HP:0000733**. [61] |
| Gait imbalance; clinical sign | **14/27 (52%)**; childhood motor difficulty. [16] | Walking and fall risk may be affected. | Gait imbalance **HP:0002141**. [61] |
| Abnormal pyramidal signs; neurological sign | **6/24 (25%)**; progression not established. [31] | May add motor-management needs. | Abnormal pyramidal signs—ID to verify. |
| Seizures; symptom/sign | **3/32 (9%)** in the original cohort; episodic when present. [31] | Safety and seizure-care burden for affected individuals. | Seizure **HP:0001250**. [61] |
| Brain/spine anomalies; imaging signs | **14/22 (64%)** imaged had a reported CNS anomaly, including polymicrogyria, heterotopia, cerebellar atrophy, periventricular white-matter changes, callosal agenesis, or tethered cord. This is a **selected imaged denominator**, not a birth prevalence. [16] | Consequences depend on the specific lesion; not quantified. | Annotate the **specific demonstrated lesion**, rather than assigning every lesion to every patient. |
| Craniofacial differences; physical signs | **28/31 (90%)** had dysmorphism in the detailed comparison. Reported examples include bitemporal narrowing **39%**, epicanthus **39%**, synophrys **33%**, and a broad/bulbous nose or prominent tip **52%**. [31][22] | Mainly diagnostic relevance; quality-of-life effect not established. | Epicanthus **HP:0000286**; specific remaining facial terms require ID verification. [61] |
| Congenital heart defect; physical/imaging sign | **8/29 (28%)** for specifically classified CHD in the detailed comparison. VSD, patent ductus arteriosus, and other findings occur. A broader original-table category, **“cardiac features/CHD,” is 14/22 (64%)**; **do not equate the two rates**. [31][16] | Depends on cardiac lesion and hemodynamic significance. | Specific defect term after echocardiographic confirmation. |
| Gastrointestinal features; clinical signs | **13/31 (42%)**; includes reflux or constipation. Feeding/swallowing difficulty separately occurred in **8/30 (27%)**. [31][16] | Nutrition, aspiration risk, and daily feeding needs in some patients. | Specific reflux, constipation, or feeding-difficulty term, as documented. |
| Hearing loss; clinical sign | **3/31 (10%)** in the original series; type and individual severity vary. [16] | Communication and educational access. | Hearing impairment—ID to verify. |
| Ocular involvement; clinical sign | **6/30 (20%)**; findings include strabismus; the detailed comparison separately records myopia **6/30 (20%)**. [31] | Vision and learning access. | Specific documented ocular finding. |
| Brachydactyly; physical sign | **5/30 (17%)**; congenital/nonprogressive morphology. Toe abnormalities: **4/27 (15%)**. [16] | Functional impact usually requires individual assessment. | Brachydactyly; specific toe anomaly—IDs to verify. |
| Scoliosis/kyphosis; physical sign | **5/28 (18%)** radiographically supported in the original comparison; subsequent course unknown. [16] | Posture and mobility if clinically significant. | Specific confirmed spinal-deformity term. |
| Precocious puberty; endocrine sign | **4/18 (22%)** assessed; timing is early by definition, but age-specific natural history is unavailable. [16] | May require endocrine evaluation. | Precocious puberty—ID to verify. |
| Increased BMI/obesity; clinical sign | Age-related tendency, especially females: **6/16 females obese versus 0/15 males** among those assessed; raised BMI **10/16 females versus 3/15 males**. [16] | Potential longer-term metabolic and psychosocial effects have **not** been quantified specifically for RATARS. | Obesity; increased body mass index—IDs to verify. |

**Frequency caution:** the 2024 comparison reports **8/29 CHD**, whereas the original cohort’s broader *cardiac-features/CHD* table reports **14/22**. Those are different ascertainment and phenotype definitions, not evidence that the underlying heart-defect rate changed. Likewise, syndrome-page percentages without clear denominators should not replace the primary study counts. [31][16]

## 4. Genetic and molecular information

*SPEN* (**HGNC:17575; NCBI Gene:23013; OMIM:613484**) encodes a nuclear transcriptional repressor also called SHARP/MINT. It has RNA-recognition motifs and a C-terminal SPOC region involved in corepressor interactions. Disease-associated variants in the foundational series are **germline-consistent heterozygous stop-gain or frameshift variants**; fibroblast testing in three people supported a non-blood-restricted origin. The reported variants were absent from the gnomAD dataset examined **at publication**, which must not be interpreted as a newly verified 2026 allele frequency. [44][16][27]

| Variant evidence or class | Findings and interpretation |
|---|---|
| Foundational cohort variant set | **32 distinct truncating changes in 34 people**, distributed across *SPEN*; the published Table 1 supplies each HGVS change, domain, inheritance observation, and original gnomAD check. Of the 34 individuals, a subsequent comparison summarizes **28 de novo, three familial, and three unknown**. These are *observed cases*, not penetrance estimates. [16][31] |
| Recurrent stop-gain example | **NM_015001.3:c.5806C>T, p.(Arg1936Ter)** occurred in the original cohort and independently in the Korean boy; the latter was **de novo**, classified pathogenic, and absent from gnomAD in that report. Predicted nonsense-mediated decay was **not directly demonstrated for that patient**. [16][31] |
| Recurrent frameshift example | **NM_015001.3:c.6223_6227del, p.(Ser2075GlufsTer46)** occurred in the original series and a Japanese girl; the latter’s variant was **de novo** and described as pathogenic (Nishi *et al.*, online **21 October 2024**, PMID **39431794**, DOI [10.1002/ajmg.a.63910](https://doi.org/10.1002/ajmg.a.63910)). [16][34] |
| Familial evidence | The original cohort included inheritance from an **affected mother** for p.(Arg1936Ter) and from an **affected father** for p.(Glu2443GlyfsTer17) in two siblings. An independently de novo p.(Arg1936Ter) demonstrates that the same coding change can have different family histories. [16][31] |
| Missense variants and uncertain findings | The defining 34-person study contained **truncating**, not missense, variants. A rare *SPEN* missense finding should **not** automatically be called causal for RATARS: apply variant-specific ACMG/AMP interpretation and phenotype/segregation evidence. [16][27] |
| Copy-number changes | Deletions including *SPEN* may contribute to a **multigene proximal 1p36 deletion phenotype**; evaluate deleted genes and breakpoints rather than labeling every 1p36 deletion isolated RATARS. No recurrent RATARS-specific translocation, inversion, aneuploidy, or repeat expansion is established. [16][31] |
| Modifier genes and epigenetics | No clinically established modifier. In **seven affected females** versus **six batch-matched female controls**, blood-DNA analysis yielded an X-chromosome methylation signature; the 11-patient initial genome-wide comparison did **not** show substantial global methylation change. Affected males were not reliably distinguished by that X-specific classifier. [16] |

## 5. Environmental and infectious information

**No infectious agent, toxic exposure, radiation exposure, occupational hazard, or lifestyle behavior is established as a cause or trigger of RATARS.** The disease’s genetic cause should not be confused with factors that can influence general health or with the experimental *Spen*–diet effects observed in flies. Consequently, CTD-style chemical–disease causation, a pathogen taxon, and a disease-preventive CHEBI exposure should **not** be populated without new evidence. [27][119]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Initiating lesion:** A germline heterozygous truncating *SPEN* variant **leads to** predicted reduced functional SPEN dosage; the aggregate genetic evidence supports haploinsufficiency, although variant-by-variant protein loss was not measured in the original patients. [27][16]
2. **Upstream molecular branch—transcription:** Reduced SPEN **is inferred to lead to** altered recruitment or action of transcriptional corepressors during development. SPEN’s transcription-repressor function is experimentally supported, but the exact disrupted developmental targets in RATARS patients have not been established. [44][132]
3. **Epigenetic/X-chromosome branch:** Reduced SPEN **leads to** an observed, female-specific **blood X-chromosome DNA-methylation episignature**. Its relationship to silencing of particular genes in patients, and to their individual symptoms, **remains inferred**. [16]
4. **Experimental explanation of that branch:** In cellular and mouse systems, XIST/Xist RNA **recruits SPEN/SHARP**, which **promotes** corepressor/HDAC3-dependent chromatin repression and X-linked gene silencing. Whether altered X inactivation itself **causes** the full RATARS phenotype is **not demonstrated**. [46][47][54]
5. **Neurodevelopmental branch:** Perturbed developmental gene regulation **is inferred to result in** altered nervous-system development and neuronal maintenance, **leading to** developmental, motor, speech, cognitive, and behavioral manifestations. Human clinical associations and mouse neural-knockout phenotypes support this chain, but its intermediate human cell types and target genes remain unresolved. [16][92]
6. **Additional organ branches:** Altered developmental transcription **is inferred to contribute to** congenital cardiac and other structural findings; separate altered energy regulation **might contribute to** later obesity. The cardiac-development and fat-metabolism mechanisms derive chiefly from **mouse and fly models**, respectively, and are **not demonstrated patient-level causal chains**. [92][100][16]

### Mechanistic detail and annotation suggestions

| Mechanism or evidence type | What has actually been shown; limits | Suggested annotations |
|---|---|---|
| **XIST–SPEN binding; human proteins, in vitro** | A **2024 primary biochemical study** found that SPEN **RRM4** was needed for high-affinity binding to XIST A-repeat RNA; at least four repeat units supported high-affinity binding under its experimental conditions. This establishes binding determinants, **not an assay of RATARS patient variants** (Button *et al.*, *RNA*, **March 2024**, PMID **38164599**, DOI [10.1261/rna.079713.123](https://doi.org/10.1261/rna.079713.123)). Its abstract states: “**Binding of SPEN to XIST RNA requires RRM 4 of the protein**.” [54] | Protein: SPEN; RNA: XIST. GO biological-process suggestions: X-chromosome inactivation; negative regulation of transcription. NCBI annotates SPEN to these processes and to the **nucleus/nucleoplasm**. [44] |
| **Chromatin repression; cell and mouse evidence** | McHugh *et al.* showed XIST–SHARP/SPEN interaction and implicated SMRT/HDAC3-mediated transcriptional silencing (**2015**, PMID **25915022**). Dossin *et al.* found SPEN required to **initiate** X silencing in mouse preimplantation embryos and embryonic stem cells, but dispensable for its **maintenance** in neural progenitors (**2020**, PMID **32025035**). This distinction matters when interpreting a developmental syndrome. [46][47] | GO suggestions: random X-chromosome inactivation; negative regulation of transcription by RNA polymerase II; regulatory-ncRNA-mediated heterochromatin formation. GO cellular component: nucleus/nucleoplasm, transcription-repressor complex. [44] |
| **Human methylomics; affected-person biomarker research** | Blood DNA from 11 affected people was assayed with the MethylationEPIC array. The informative female X-chromosome analysis selected **122 probes** and separated tested affected females from controls; the genome-wide difference was not substantial, and the autosomal classifier did not generalize robustly across batches. **Research-stage classification evidence, not a validated stand-alone clinical diagnostic test.** [16] | Biospecimen: peripheral-blood leukocyte DNA; compartment implicated: nuclear chromatin. Do **not** annotate tissue-specific brain methylation as measured. |
| **Neural development; expression and mouse model** | Analyses of existing human developing-brain bulk and single-cell RNA data placed *SPEN* expression in early cortical development, including the transition from **ventricular radial glia to intermediate progenitors**. Neural conditional *Spen* knockout mice showed reduced cortex/hippocampus and enlarged ventricles; these are not human single-cell RATARS profiles. [16][92] | Suggested CL labels: radial glial cell, neural intermediate progenitor, neuron—**cell involvement is inferred**, not a demonstrated patient-cell lesion. GO: neurogenesis; anatomical terms: cerebral cortex, hippocampus, brain. |
| **Notch/RBP-J and development; experimental** | In mouse work, MINT/SPEN opposed Notch-dependent RBP-J transactivation; null mutants had embryonic lethality and altered B-cell differentiation (Kuroda *et al.*, **2003**, PMID **12594956**). A **specific Notch-driven immune deficiency in patients has not been demonstrated**. [132] | GO: Notch signaling pathway; use B-cell annotations only for the **mouse experiment**, not a patient immune phenotype. [44] |
| **Metabolism; fly model** | *Spen*-depleted *Drosophila* fat-storage cells had impaired lipid mobilization and β-oxidation-associated metabolic changes, including reduced free carnitine/acylcarnitines (Hazegh *et al.*, **2017**, PMID **28640815**). A corresponding human metabolic signature, enzyme deficiency, or carnitine treatment indication has **not** been established. [100][94][16] | Suggested process: fatty-acid β-oxidation; chemical-entity suggestion: **L-carnitine**, with its CHEBI identifier verified before entry. Fly tissue: fat body—not a proven human target tissue. |

There is **no established RATARS-specific** patient proteomic, metabolomic, lipidomic, spatial-transcriptomic, single-cell atlas, multi-omics integration, or CRISPR-screen signature. The human developmental single-cell data above are **expression-context analyses**, not single-cell sequencing of affected patients. No primary evidence supports adding ischemia, fibrosis, chronic inflammation, apoptosis, mTOR, PI3K–AKT, or mitochondrial enzyme deficiency as a demonstrated RATARS mechanism. [16][54]

## 7. Anatomical structures affected

| Level | Supported sites, localization, and ontology suggestions |
|---|---|
| Organ/system | **Central nervous system**, heart, and variable gastrointestinal, musculoskeletal, ocular, auditory, and endocrine involvement are clinically reported. Suggested verified broad UBERON anchors: **brain UBERON:0000955** and **heart UBERON:0000948**; choose specific anatomical terms only when the patient has that finding. [16][31] |
| CNS structures | Reported lesions include cerebral cortex polymicrogyria, neuronal heterotopia, cerebellar atrophy, periventricular white matter changes, corpus-callosum agenesis, and tethered cord. **These are alternatives observed across patients**, not a uniform anatomical lesion. [16] |
| Tissues/cells | Developing neural tissue is strongly implicated by clinical and model evidence; radial glial cells, intermediate progenitors, and neurons are **research-relevant candidate populations**. Cardiac developmental cells are plausible but not resolved as patient-specific targets. Assign precise **CL identifiers only after ontology lookup**. [16][92] |
| Subcellular compartment | SPEN acts principally in the **nucleus/nucleoplasm** and transcription-repressor complexes; the X-chromosome chromatin branch is pertinent in females. Fly mitochondrial fatty-acid metabolism is a **downstream model observation**, not evidence that SPEN is primarily a mitochondrial protein in patients. [44][54][94] |
| Lateralization | **No characteristic unilateral, bilateral, or asymmetric pattern** is established for RATARS. [16] |

## 8. Temporal development

**Onset is developmental:** hypotonia and feeding problems can be apparent in infancy, while speech, learning, behavior, and some structural findings become apparent as the child grows. In the foundational series, ages at last assessment ranged from **fetal life to 24 years 6 months**. Increased BMI tended to emerge **after about age four**. These observations do **not** establish formal early/intermediate/end-stage categories or a common progressive neurological course. [16]

A Korean boy’s longitudinal case illustrates variability rather than a universal trajectory: axial hypotonia was present in infancy; at **28 months** developmental testing showed substantial delays; at **five years** he could walk with support and combine two words. The study’s abstract describes his diagnosis as resulting from “**whole genome sequencing**” (Kim *et al.*, published online **16 December 2024**, DOI [10.26815/acn.2024.00717](https://doi.org/10.26815/acn.2024.00717)). No standardized remission pattern, disease duration estimate beyond its developmental nature, or validated critical treatment window has been published. [31]

## 9. Inheritance and population

| Population or inheritance measure | Best-supported answer |
|---|---|
| Inheritance | **Autosomal dominant**. Most original cases were de novo; **28 de novo, three familial, three unknown** is the published retrospective accounting. [27][31] |
| Penetrance and expressivity | **Expressivity is variable.** Penetrance has **not** been quantified in an unbiased carrier series; ascertainment of affected families cannot establish complete penetrance. [16][27] |
| Anticipation, mosaicism, founder effect, consanguinity, carrier frequency | **Not established** as RATARS features; unaffected carrier frequency and parental germline-mosaicism frequency cannot be estimated from the available reports. [16][27] |
| Prevalence and incidence | **No reliable population-based cases-per-100,000 or annual incidence estimate.** “34” is the size of the landmark cohort, **not** prevalence or a complete count of all affected people. [16][34] |
| Sex and ages | Original cohort: **17 female and 17 male**; ages at last examination **fetus to 24 years 6 months**. A 1:1 *reported-cohort* split is **not** a population sex ratio. [16] |
| Ancestry/geography | A Korean boy and a Japanese girl were subsequently reported; no ancestry-specific risk, endemic region, or geographic variant distribution is established. [31][34] |

## 10. Diagnostics

**The diagnostic anchor is molecular identification and interpretation of a plausible heterozygous *SPEN* loss-of-function variant in the appropriate clinical setting.** Phenotypic findings alone are insufficiently specific to separate RATARS from 1p36 deletion syndrome or other neurodevelopmental disorders. [27][31][34]

| Diagnostic approach | Utility and limitation |
|---|---|
| Clinical evaluation | Developmental and neurologic assessment, speech/feeding evaluation, growth/BMI and pubertal review; cardiac, hearing, vision, and renal evaluation **guided by findings**. No published RATARS-specific clinical scoring criteria or laboratory enzyme assay exists. [16][31] |
| Exome sequencing | Appropriate for heterogeneous developmental-delay presentations; trio **WES** identified the Japanese girl’s recurrent *SPEN* frameshift after cytogenetics and microarray did not explain her findings. [34] |
| Genome sequencing | Trio **WGS** identified de novo *SPEN* c.5806C>T in the Korean boy after a **normal 46,XY karyotype**. Its abstract says: “**A 3-year-old boy ... underwent whole genome sequencing**.” WGS can also aid evaluation of other candidate variant types, but a disease-specific comparative diagnostic yield is unavailable. [31] |
| Multigene panel or targeted test | A neurodevelopmental-disorder/intellectual-disability panel **including *SPEN*** is a reasonable option; targeted familial-variant testing is appropriate when a causal variant is already known. The Korean investigators specifically recommended including *SPEN* in relevant genetic testing. [45][31] |
| Chromosomal microarray; karyotype/FISH | **CMA** addresses 1p36 copy-number deletions and other CNVs, not typical sequence-level *SPEN* truncations. Karyotyping helped exclude trisomy 21 in the Japanese case but was not the molecular RATARS test. FISH is not routinely established for isolated sequence variants. [34][31] |
| Imaging and functional tests | Brain MRI **when indicated** can characterize reported anomalies; echocardiography identifies heart defects. Audiology, ophthalmology, swallow assessment, and EEG **if clinically indicated** address associated manifestations. There is no characteristic diagnostic MRI, EEG, biochemical, biopsy, or pathology result. [16][31] |
| Methylation/other omics | Female X-chromosome blood methylation classification is a **research finding** with batch and sex limitations; RNA-seq, proteomics, metabolomics, liquid biopsy, and mitochondrial or repeat-expansion testing are **not established RATARS diagnostic tests**. [16] |
| Differential diagnosis | **Proximal or distal 1p36 deletion syndrome:** determine deletion boundaries by CMA/sequence analysis; overlap alone does not show *SPEN* deletion. **Down syndrome:** assess cytogenetics when clinically suspected; the Japanese case initially resembled it, but cytogenetics and CMA did not identify the cause and trio WES found *SPEN*. Broader neurodevelopmental disorders require variant-led evaluation. [31][34] |
| Asymptomatic screening | No established population newborn or universal carrier-screening program. Once a familial pathogenic variant is known, offer genetics-led evaluation and targeted **cascade testing** where appropriate; these are practice implications, not outcome-tested RATARS programs. [27] |

## 11. Outcome and prognosis

**Survival probability, mortality rate, life expectancy, and validated prognostic biomarkers are unknown.** The original series included individuals assessed into young adulthood, but its ascertainment and follow-up cannot generate a survival estimate. Developmental, speech, behavioral, mobility, feeding, cardiac, and sometimes weight-related needs contribute to morbidity; **no disease-specific EQ-5D, SF-36, or PROMIS results, formal disability distribution, or reliable treatment-response rate** were established in the cited cohort. Variant location did not yield a clear severity predictor. Recovery probabilities, including a treated-versus-untreated comparison, are unavailable. [16][27]

Potential complications should be recorded **patient by patient**, not assumed: for example, aspiration and poor growth in the Korean child required substantial feeding support. The original cohort observed seizures in only **3/32**, so epilepsy should not be represented as inevitable or as a demonstrated major mortality cause. [31][16]

## 12. Treatment and real-world implementation

**There is no demonstrated disease-modifying treatment for RATARS.** Care is individualized around documented developmental and organ-specific needs; the interventions below are management suggestions or reported care, **not syndrome-specific efficacy claims**. No RATARS drug-response rates, pharmacogenomic rule, approved gene/RNA/cell therapy, immunotherapy, or RATARS-specific NCT trial was established in the reviewed evidence. Suggested NCIT *intervention labels* are provided for knowledge-base matching; **NCIT codes require independent terminology verification**. [16][31]

| Treatment or intervention | Clinical role and evidence boundary | Suggested NCIT intervention term |
|---|---|---|
| Developmental, speech-language, occupational, and physical therapies | Reasonable functional support for documented developmental, communication, and motor needs; **RATARS-specific comparative outcomes unavailable**. [16] | Speech Therapy; Occupational Therapy; Physical Therapy. |
| Feeding/swallowing and nutritional support | Assess aspiration and growth individually. In the Korean case, **fundoplication and gastrostomy at four months** addressed poor weight gain/recurrent aspiration; tube feeding continued until age three. A single case does not establish routine surgical indications. [31] | Nutritional Support; Gastrostomy; Fundoplication. |
| Cardiac, neurologic, behavioral, and endocrine management | Assess and manage a **confirmed** heart defect, seizures, behavioral condition, precocious puberty, or elevated BMI according to that manifestation. **No RATARS-specific drug, combination regimen, response rate, or adverse-event series** is available. [16][31] | Cardiac Assessment; Seizure Management; Behavioral Therapy; Endocrine Evaluation—term/code validation needed. |
| Diet modification proposed from fly experiments | Extra yeast or sugar altered outcomes of *Spen*-depleted flies; **neither is an established patient treatment**, and extra sugar increased adiposity in that model. [119] | **Do not annotate as a validated RATARS intervention.** |
| Gene editing, gene replacement, ASOs, cell therapy, or methylation-directed treatment | **Experimental concepts only** in this disease context; the cited human studies report no therapeutic implementation or outcome. [16][31] | **No established disease-specific NCIT treatment annotation.** |

## 13. Prevention and counseling

**Primary prevention of a spontaneous de novo *SPEN* variant is not known.** No vaccine, antimicrobial prophylaxis, toxin-avoidance program, or lifestyle change prevents RATARS. Genetics-led counseling can explain autosomal-dominant transmission, the distinction between de novo and inherited variants, and reproductive options **after a familial variant is established**; a de novo result does not by itself quantify possible parental germline mosaicism. Targeted familial testing and, where desired, reproductive testing are individualized options, not population screening. [27][31]

**Secondary and tertiary prevention** means recognizing developmental and organ-specific issues early and addressing complications—for example, aspiration or a clinically important cardiac defect—rather than preventing the genetic disorder itself. There is no validated RATARS risk score, prophylactic medication, or disease-specific public-health/environmental intervention. [16][31]

## 14. Other species and natural disease

| Species and taxonomy | Ortholog or natural-disease evidence | Veterinary/transmission interpretation |
|---|---|---|
| Human, *Homo sapiens* (**NCBI Taxon:9606**) | RATARS is the **naturally described human disease**; *SPEN* NCBI Gene **23013**. [16][44] | Inherited genetic condition, **not infectious or zoonotic**. |
| Mouse, *Mus musculus* (**NCBI Taxon:10090**) | Ortholog ***Spen***, **NCBI Gene:56381; MGI:1891706**. Experimental mutant phenotypes exist, but **naturally occurring veterinary RATARS has not been established**. [106][92] | No demonstrated breed-specific natural disease or cross-species transmission. |
| Fruit fly, *Drosophila melanogaster* (**NCBI Taxon:7227**) | Experimental *Spen* depletion reveals conserved transcription/metabolic research questions; this is **not** a reported natural animal RATARS diagnosis. [100][119] | No breed identifier or zoonotic relevance. |
| Zebrafish, *Danio rerio* (**NCBI Taxon:7955**) | A *spen* ortholog is catalogued in ZFIN, which reports **no experimentally associated RATARS model data** on the cited gene page. [65] | No established natural disease or transmission. |

## 15. Model organisms and model limitations

| Model system | Manipulation and recapitulated findings | What it can—and cannot—establish |
|---|---|---|
| Mouse, *Spen* null or conditional knockout | Null embryos have developmental and cardiac abnormalities and embryonic lethality; neural conditional deletion produced reduced brain weight/cortical thickness and hippocampal size with enlarged ventricles. MGI catalogs *Spen* mutant alleles, including a **conditional-ready** targeted allele. Primary mouse Notch/B-cell evidence: PMID **12594956**; conditional-allele publication: PMID **17457934**. [92][106][108][132][129] | Useful for developmental requirements and cell-restricted mechanisms. **Biallelic/conditional loss is not equivalent to the typical human heterozygous truncation**; full RATARS behavior, penetrance, and treatment response are not established by these models. [16][92] |
| Mouse embryos and embryonic stem cells | *Spen* perturbation impairs **initiation** of X-chromosome silencing; neural progenitor maintenance findings differ (Dossin *et al.*, PMID **32025035**). [47] | Tests an upstream epigenetic function, **not** proof that altered X inactivation alone produces every human symptom. |
| *Drosophila* larval fat body; RNAi knockdown | Increased fat storage and impaired energy mobilization/β-oxidation-associated measures; diet-modification experiments show stage-dependent partial rescue (PMIDs **28640815**, **32107279**). [100][119] | Tests a candidate metabolic branch and gene–diet interaction; **does not validate fly diets, carnitine, or obesity mechanisms as patient treatments**. |
| Purified human SPEN/XIST components; in vitro | RNA-binding/domain and XIST A-repeat experiments quantify an upstream interaction (PMID **38164599**). [54] | Mechanistically precise, but lacks intact human tissues, affected-patient variants, and clinical outcomes. |
| Human affected-person samples | Clinical genotypes/phenotypes and female blood-DNA methylation constitute **human disease evidence**, not an established patient-derived organoid, iPSC, or gene-corrected model. [16] | Most directly relevant to annotation, but small, ascertained cohorts and limited longitudinal follow-up constrain causal and prognostic inference. |

**Knowledge-base priority:** enter the *SPEN*–RATARS loss-of-function association and the **denominator-qualified human phenotypes** as established; label the X-chromosome methylation signature as a **female-biased research biomarker**; and keep Notch, neural-cell-specific, and fatty-acid-metabolism explanations tagged to their **experimental evidence type** rather than asserting them as proven patient mechanisms. [16][31][47][100]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1371/journal.pgen.1008333&type=printable` (2 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 10 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `OMIM`, `Taxon`, `MGI`.

13 of 23 terms resolved to a current term; the rest could not be looked up either way.