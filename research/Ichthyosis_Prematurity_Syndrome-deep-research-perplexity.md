---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:25.480453'
end_time: '2026-10-09T20:59:06.000756'
duration_seconds: 220.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ichthyosis Prematurity Syndrome
  mondo_id: MONDO:0012089
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
citation_count: 58
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMC:PMC8613581
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012089
    reported_labels:
    - MONDO
    ontology_label: ichthyosis prematurity syndrome
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - OMIM
  - OMIA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ichthyosis Prematurity Syndrome
- **MONDO ID:** MONDO:0012089 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ichthyosis Prematurity Syndrome** covering all of the
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

# Ichthyosis Prematurity Syndrome: disease-characteristics report

**Ichthyosis prematurity syndrome (IPS; MONDO:0012089) is a rare, autosomal-recessive disorder caused by biallelic germline pathogenic variants in *SLC27A4*.** It typically presents with premature birth, thick vernix-like desquamating skin, and potentially life-threatening neonatal respiratory distress. The conspicuous birth scale usually sheds over weeks; mild ichthyosis, follicular hyperkeratosis, pruritus, or atopic disease can persist. The strongest mechanistic evidence implicates defective epidermal acylceramide synthesis and skin-barrier formation. [1][45][75]

**Evidence conventions.** “Human” below denotes clinical observations or patient-derived material; “mouse,” “dog,” and “in vitro” identify other evidence types. Phenotype percentages come from a **2025 systematic review of 59 published patients**, searched through September 3, 2024—not a population-based registry. A percentage calculated across all 59 must not be interpreted as penetrance when many reports did not assess or mention the feature. [30][90][web:31974308][web:12285567]

## 1. Disease information

| Identifier or name | Value | Interpretation |
|---|---|---|
| MONDO | **MONDO:0012089** | Target disease concept. [6] |
| OMIM phenotype | **608649** | Ichthyosis prematurity syndrome. [1] |
| OMIM gene | **604194** | *SLC27A4*. [1] |
| Orphanet | **ORPHA:88621** | Ichthyosis-prematurity syndrome. [3] |
| ICD-10 | **Q80.8** | Broader “other congenital ichthyosis” code, not IPS-specific. [107] |
| ICD-11 | **LD27.2** | Listed by Orphanet for IPS. [107] |
| MeSH | **C536271** | Supplementary concept; the broader ichthyosis descriptor is D007057. [122][70] |
| Other names | **IPS; ichthyosis-prematurity syndrome; ichthyosis congenita type IV; congenital ichthyosis type 4** | Naming varies by resource. [62][73] |

This is an **aggregated disease-level synthesis**, not an analysis of identifiable patients or EHR records. Its numerical observations derive chiefly from published cases and a 23-patient clinical series; neither is an unselected epidemiological sample. [45][web:12285567]

## 2. Etiology, risk, protection, and gene–environment interaction

The established initiating cause is **biallelic loss or impairment of *SLC27A4* function**. *SLC27A4* encodes fatty acid transport protein 4 (FATP4), also called ACSVL4. Disease has been observed with homozygous and compound-heterozygous alleles, including nonsense, missense, splice-site, and exon-deletion variants. Patient-derived cells lacking full-length FATP4 have reduced very-long-chain-fatty-acid CoA-synthetase activity. **PMID: 19631310**; https://pubmed.ncbi.nlm.nih.gov/19631310/. [84][145]

| Factor | Disease-specific assessment |
|---|---|
| **Genetic and family-history risk** | Having two carrier parents creates the conventional **25% affected / 50% carrier / 25% neither familial variant** risk for each pregnancy, assuming both parental alleles are pathogenic and independently transmitted. Consanguinity can increase the chance that both parents carry the same rare allele; it is not required. The 59-case review recorded consanguinity in **10/59**, but it was unreported in **33/59**. [105][web:12285567] |
| **Founder effect** | Scandinavian families shared the nonsense allele **NM_005094.4:c.504C>A, p.(Cys168*)**; the original study reported a shared approximately **786-kb** haplotype. This is a population-specific allele observation, not evidence that IPS is restricted to Scandinavia. **PMID: 19631310.** [84] |
| **Environmental or lifestyle causes** | No toxin, diet, occupation, smoking exposure, or infectious agent is established as a cause of IPS. **Polyhydramnios and prematurity are manifestations/consequences of an affected pregnancy**, rather than independently established causes of the Mendelian condition. [45][47] |
| **Protective factors** | No verified protective allele, diet, supplement, vaccine, or exposure prevents disease in someone with a causative biallelic genotype. Carrier identification and reproductive options can prevent *recurrence of an affected pregnancy*; neonatal planning can reduce complications, not reverse the genotype. [105][106] |
| **Gene–environment interaction** | The best-supported interaction is developmental: impaired fetal epidermis sheds corneocytes into **amniotic fluid**, creating a physical aspiration hazard around delivery. Prematurity also contributes to respiratory vulnerability. This is not evidence of a specific chemical-exposure-by-genotype interaction. **PMIDs: 21856041, 21465607.** [45][47] |

## 3. Phenotypes

**Frequency key:** the numerator/59 is the number positively reported in the 2025 published-case review, **not** the proportion among patients actually assessed. Where useful, the assessed denominator is supplied. The review reports a mean gestational age of **32.30 weeks** (range **28.00–35.86**). Its 23-patient Norwegian source series found peripheral eosinophilia in every patient it examined and a history of respiratory and/or food allergy in **more than 70%**; neither estimate establishes population-wide penetrance. **PMID: 21856041.** [web:12285567][45]

| Phenotype and type | Suggested HPO term | Onset, severity, course, and reported frequency | Function or quality-of-life impact |
|---|---|---|---|
| **Premature birth**; birth outcome | Premature birth **HP:0001622** | Prenatal; characteristic in clinically recognized IPS. Mean **32.30 weeks** in the 59-case review; all **23** patients in the Norwegian series were born prematurely. [71][45][web:12285567] | NICU admission and complications of prematurity; IPS-specific quality-of-life score unavailable. |
| **Polyhydramnios**, sometimes echogenic amniotic fluid or membrane separation; prenatal sign | Polyhydramnios **HP:0001561** | Usually detectable in the third trimester; **27/59 reported positive**, **30/59 unreported**. All five pregnancies in one ultrasound series developed polyhydramnios between **28 and 31 weeks**. **PMID: 21465607.** [47][web:12285567] | Prompts fetal assessment and delivery planning; no separate IPS quality-of-life measurement. |
| **Thick caseous/vernix-like scale and desquamation**; physical sign | Ichthyosis **HP:0008064**; desquamation shortly after birth **HP:0007549** | Severe or extensive at birth in **all 59 reviewed cases** by case selection; subsequently improves. Median reported scale duration **10 weeks** among only **14 cases** with an exact duration. [71][web:12285567] | Skin-care burden; occasionally constriction or ear-canal blockage. |
| **Respiratory distress/asphyxia**; clinical sign | Neonatal respiratory distress **HP:0002643** | Acute at birth; potentially critical. **47/59 reported positive**, **10/59 unreported**. The Norwegian series documents variable, sometimes life-threatening asphyxia. **PMID: 21856041.** [45][71][web:12285567] | May require suction, oxygen, ventilation, and prolonged NICU care. |
| **Erythroderma/swollen skin**; physical sign | Erythroderma **HP:0001019** | Neonatal; **41/59 reported positive**, **18/59 unreported**; improves as scale sheds. [71][web:12285567] | Skin discomfort and intensive neonatal monitoring. |
| **Peripheral eosinophilia**; laboratory abnormality | Increased total eosinophil count **HP:0001880** | Neonatal, often transient; **37/59 reported positive**, but **37/38** among cases reporting a count; reported values **1,050–14,175 cells/µL**. [71][web:12285567] | A diagnostic clue, not by itself a measure of disability. |
| **Elevated serum IgE and allergic disease**; laboratory finding/clinical manifestation | Use the corresponding current HPO elevated-IgE and allergy terms after ontology validation | Raised IgE in **17/59 reported positive**, **17/19 assessed**. Respiratory or food allergy occurred in **>70%** of the 23-patient clinical series; atopy can persist after neonatal improvement. **PMID: 21856041.** [45][web:12285567] | Allergy symptoms, treatment burden, and possible effects on sleep and daily functioning; IPS-specific EQ-5D/SF-36 data unavailable. |
| **Mild chronic ichthyosis and follicular hyperkeratosis**; physical signs | Follicular hyperkeratosis **HP:0007502**; ichthyosis **HP:0008064** | Childhood through adulthood; generally milder than neonatal scale. No defensible pooled frequency; a 2024 adult report documents extensive follicular hyperkeratosis at age **25**. [45][48][71] | Persistent dryness, visible skin change, and ongoing skin care. |
| **Pruritus**; symptom | Pruritus **HP:0000989** | Variable, sometimes chronic and severe; present in the clinical series, without a dependable pooled percentage. **PMID: 21856041.** [45][71] | Can impair comfort and sleep; no IPS-specific validated score located. |
| **Alopecia, hypotrichosis, or hypohidrosis**; physical signs/symptoms | Select the precise HPO term for the observed hair-loss or reduced-sweating phenotype | Not core neonatal criteria or quantified population features. The 2024 report describes adult scalp alopecia, sparse body hair, reduced sweating, and overheating. [48] | Cosmetic burden or heat intolerance, depending on the individual. |
| **Epidermal acanthosis, hyperkeratosis, and curved lamellar aggregates**; biopsy findings | Epidermal acanthosis **HP:0025092**; add a histology/ultrastructure term only after exact ontology matching | Characteristic biopsy findings, not universal clinical tests. Hyperkeratosis was reported in **11/15** biopsied cases and curved multilamellar aggregates in **9** cases in the review. **PMIDs: 21856041, 19119129.** [45][50][web:12285567] | Diagnostic relevance; no independent demonstrated quality-of-life effect. |

Scalp scale was reported in **55/59 (93.2%)**, upper limbs **51/59 (86.4%)**, trunk **49/59 (83.1%)**, lower limbs **47/59 (79.7%)**, palms/soles **46/59 (78.0%)**, and face **37/59 (62.7%)**. These are distributions *within selected published cases*, not separate disease prevalences. [web:12285567]

## 4. Genetic and molecular information

***SLC27A4* is the established causal gene**, located at **9q34.11**: **HGNC:10998; NCBI Gene:10999; OMIM:604194; UniProt:Q6P1M0**. The associated phenotype is **OMIM:608649**. The relevant variants are **germline**, not somatic cancer drivers. There is no established recurrent aneuploidy or chromosomal rearrangement defining IPS; a *gene-level* exon deletion is reported. [1][60][61][145]

| *SLC27A4* variant or class | Evidence and classification | Population frequency and functional interpretation |
|---|---|---|
| **NM_005094.4:c.504C>A; p.(Cys168*)** | Pathogenic homozygous nonsense variant in one **2024 Finnish** genetically tested patient; originally established as a Scandinavian founder allele. **PMIDs: 39189679, 19631310.** [135][199][84] | A ClinVar frequency display lists **gnomAD 0.00009**, with other source-specific figures also shown; version, ancestry, and dataset must accompany reuse. Patient cells had no detectable full-length protein and reduced very-long-chain acyl-CoA synthetase activity. [182][84] |
| **c.716-1G>A** | Homozygous canonical splice-acceptor variant reported in a North African family; predicted truncation. **PMID: 19631310.** [84] | A reliable current population frequency was not established from the consulted sources. |
| **c.556+2T>G**, in trans with **c.899A>G; p.(Gln300Arg)** | A **2024 conference case** describes the splice variant as pathogenic and the missense variant as likely pathogenic; the adult patient had IPS-compatible lifelong findings. These are the case authors’ classifications, not independently established consensus classifications. [48] | Population frequencies not established here. |
| **c.1430T>A; p.(Val477Asp)** | **ClinVar likely pathogenic, one submitter/one star**, evaluated **May 8, 2024**; missense, germline. This is not expert-panel adjudication. [32] | Population allele frequency not verified from the accessed condition record. |
| **c.1628-1G>A** | ClinVar **likely pathogenic** splice-acceptor variant, reported in a premature infant with congenital ichthyosis in compound-heterozygous state. [180] | ClinVar submitter reports **1/248,182 gnomAD chromosomes**—approximately **4.0 × 10⁻⁶** for that stated dataset. [180] |
| **Deletion of exons 8–10**, in trans with **c.986C>T; p.(Thr329Met)** | A **2025 human case** describes the exon deletion as pathogenic and the missense allele as a **variant of uncertain significance**; the latter should **not** be promoted to pathogenic solely because it occurred in an affected patient. [145] | Frequencies not established here; the deletion shows why a negative sequencing-only result may warrant deletion/duplication analysis. |

**Modifiers and epigenetics:** No clinically validated *modifier gene*, protective allele, IPS-specific DNA-methylation signature, histone signature, or diagnostic epigenetic assay was established in the consulted evidence. Reduced epidermal *Elovl1* expression in knockout mice is an observed **downstream molecular change**, not proof that *ELOVL1* is a human IPS modifier. **PMID: 31974308.** [web:31974308]

## 5. Environmental information

No pathogen, occupational exposure, pollution exposure, radiation exposure, diet, alcohol use, or smoking pattern has been shown to initiate IPS. The clinically important non-genetic **setting** is the affected pregnancy and birth: corneocytes accumulate in amniotic fluid and can enter neonatal airways. This is a downstream fetal–maternal/physical interaction, not infection or person-to-person transmission. **PMIDs: 21856041, 22927265.** [45][57]

## 6. Mechanism and pathophysiology

**Ordered causal chain—upstream lesion to manifestations**

1. **Biallelic pathogenic *SLC27A4* variants lead to** absent or impaired FATP4 fatty-acid–activating function. This is supported by human genetics and patient-cell assays. **PMID: 19631310.** [84]
2. **Reduced FATP4 acyl-CoA-synthetase activity leads to** impaired activation of very-long-chain and **ω-hydroxy fatty acids** needed for epidermal lipid synthesis. The ω-hydroxy substrate activity is demonstrated **in vitro**; its disease contribution is supported by mouse and human-keratinocyte experiments. **PMIDs: 19631310, 31974308.** [84][web:31974308]
3. **Impaired fatty-acid activation leads to** reduced epidermal **ω-*O*-acylceramide** production and altered ceramide composition. *Fatp4*-knockout mouse epidermis had approximately **10% of wild-type total acylceramide**; FATP4 knockdown also reduced acylceramide in cultured human keratinocytes. **PMID: 31974308.** [web:31974308]
4. **Altered barrier lipids lead to** a defective epidermal permeability barrier and abnormal keratinization, producing thick fetal/neonatal scale. The barrier defect is demonstrated in mice; the complete lipid-to-clinical-scale sequence in human fetal skin is a **strong mechanistic inference**, not a controlled human experiment. **PMIDs: 12821645, 31974308.** [197][web:31974308]
5. **The abnormal fetal epidermis leads to** excessive corneocyte shedding into amniotic fluid; **one branch leads to** echogenic fluid, polyhydramnios, and association with preterm delivery. The findings are documented clinically; exactly how debris produces polyhydramnios or triggers labor remains **inferred**. **PMIDs: 21856041, 21465607.** [45][47]
6. **A second branch—corneocyte-containing amniotic fluid entering the airway—leads to** bronchial/alveolar obstruction and neonatal respiratory failure. Keratin debris was found in the lungs of **two** deceased patients in the clinical series, directly supporting this route; prematurity can contribute independently. **PMID: 21856041.** [45]
7. **Barrier dysfunction and downstream inflammation may lead to** eosinophilia, raised IgE, pruritus, and later atopy. The clinical association is strong, but a particular immune-signaling cascade causally connecting FATP4 loss to each finding has **not** been demonstrated in affected humans. **PMID: 21856041.** [45]

**Cellular, biochemical, and profiling evidence.** In patient fibroblasts homozygous for p.(Cys168*), activity using a **C22:1** substrate fell **55%**, whereas measured activity using **C16:0** was unchanged; incorporation of C22:1 into cholesterol esters, triglycerides, and phospholipids fell **69%, 60%, and 37%**, respectively. These are **in-vitro patient-cell** measurements, not circulating diagnostic cutoffs. Patient epidermis also showed altered lipid-droplet staining. **PMID: 19631310.** [84]

The pathway to annotate is **fatty-acyl-CoA formation → epidermal sphingolipid/acylceramide synthesis → cornified-layer barrier assembly**, rather than an established IPS-specific Wnt, MAPK, mTOR, or PI3K–AKT signaling lesion. Suggested **GO biological-process** terms are **GO:0006629 lipid metabolic process**, **GO:0006665 sphingolipid metabolic process**, **GO:0008544 epidermis development**, **GO:0030216 keratinocyte differentiation**, and **GO:0031424 keratinization**; these are *annotation suggestions*, not claims that every term has been individually demonstrated in IPS. Principal **CL** cell types are **CL:0000312 keratinocyte** and, for the downstream blood finding, **CL:0000771 eosinophil**. [153][156][150][151][web:31974308]

Targeted lipid measurements and cell knockdown provide the principal molecular-profiling evidence. No IPS-specific clinically validated whole-transcriptome, proteomic, metabolomic, epigenomic, single-cell, spatial-transcriptomic, multi-omics, or CRISPR-screen signature was established from the consulted literature. [84][web:31974308]

> **Exact primary-abstract excerpts:** “Fibroblasts derived from a patient with IPS show reduced activity of very long-chain fatty acids (VLCFA)-CoA synthetase”; and “The total amount of acylceramide in *Fatp4* KO mice was reduced to ∼10% of wild-type mice.” **PMIDs: 19631310, 31974308**, respectively. [84][web:31974308]

## 7. Anatomical structures affected

| Level or site | Disease relationship and suggested ontology term |
|---|---|
| **Skin and epidermis—primary** | Generalized cutaneous disease, particularly fetal/neonatal epidermis and cornified layer. Suggested **UBERON:0002097 skin of body; UBERON:0001003 skin epidermis; UBERON:0002027 stratum corneum of epidermis**. Scale is often prominent on the scalp but is **not characteristically unilateral**. [45][web:12285567][158][161] |
| **Hair follicles and skin appendages** | Later follicular hyperkeratosis; alopecia or reduced sweating in some reported adults. Mouse experiments additionally demonstrate altered sebaceous-gland biology, which should not be recorded as a universal human phenotype. [48][web:12285567] |
| **Amniotic compartment—pregnancy manifestation** | Echogenic, corneocyte-containing amniotic fluid and sometimes polyhydramnios or membrane separation; annotate a precise amniotic-fluid or membrane UBERON term only after terminology validation. **PMIDs: 21465607, 21856041.** [47][45] |
| **Airways and lungs—secondary injury** | Aspiration/obstruction of bronchial tree and alveoli; suggested **UBERON:0002048 lung**, with specific airway terms selected to match the documented site. **PMID: 21856041.** [45][158] |
| **Cells and subcellular sites** | **CL:0000312 keratinocyte**, including differentiated corneocytes; **CL:0000771 eosinophil** for the laboratory phenotype. Suggested compartments: **GO:0005783 endoplasmic reticulum; GO:0005789 endoplasmic-reticulum membrane; GO:0005886 plasma membrane**. Compartment annotations require care because FATP4 has fatty-acid-transport and intracellular activation functions; they are not evidence of mitochondrial disease. [84][150][151][169] |

## 8. Temporal development

IPS is **prenatal in origin and evident at birth**, not an early-childhood-onset ichthyosis despite occasional later molecular diagnosis. In a five-pregnancy ultrasound study, polyhydramnios appeared at **28–31 weeks**; neonatal respiratory compromise is acute. The birth scale typically sheds over weeks—median **10 weeks** among **14** cases with timing—while residual skin or atopic manifestations can be lifelong. The **2024** account of a woman diagnosed at **25 years** illustrates persistence of follicular hyperkeratosis, alopecia, and hypohidrosis, not adult onset. IPS has **no validated stage classification**, predictable remission timetable, or documented anticipation pattern. **PMIDs: 21465607, 21856041.** [47][45][48][web:12285567]

The critical intervention window is **delivery through neonatal stabilization**, when airway obstruction and consequences of prematurity are most concerning. A later, different opportunity is evaluation and management of persistent skin or allergic symptoms. [45][106]

## 9. Inheritance and population

IPS is **autosomal recessive**. Penetrance for particular biallelic variant combinations has **not been reliably estimated**, and expression varies, particularly for respiratory severity and longer-term manifestations. There is no established anticipation or quantified germline-mosaicism risk. Disease has been reported across multiple geographic and ancestral backgrounds; a Scandinavian founder allele is not an ancestry restriction. [1][84][web:12285567]

Orphanet lists prevalence as **<1 per 1,000,000**, whereas the 2025 review repeats an estimate of **1 per 200,000**. These estimates conflict and lack a comparably defined population denominator; **do not convert either into a measured incidence**. Incidence per 100,000/year and overall carrier frequency are not established. In the review’s *selected* 59 reports, **29 were male and 30 female**—not proof of a population sex ratio. [3][web:12285567]

## 10. Diagnostics

**Suspect IPS immediately** when a preterm neonate has thick, greasy or clay-like vernix-like scale **and** respiratory distress, especially after a pregnancy with polyhydramnios or echogenic amniotic fluid. Stabilization must not await genetic confirmation. **PMIDs: 21856041, 21465607.** [45][47]

| Assessment | Practical interpretation |
|---|---|
| **Prenatal ultrasound** | Look for polyhydramnios, echogenic amniotic fluid, and separation of amniotic/chorionic membranes; findings can support planning but are **not diagnostic alone**. **PMID: 21465607.** [47] |
| **Neonatal examination and respiratory assessment** | Document gestational age, distribution and appearance of scale, oxygenation, and need for airway support. Chest radiography may evaluate respiratory complications, **not diagnose the genotype**. [45][web:12285567] |
| **Blood tests** | CBC with differential can detect eosinophilia; total IgE may be elevated. Neither is specific or sufficient for molecular confirmation. **PMID: 21856041.** [45] |
| **Skin biopsy** | Light microscopy may show hyperkeratosis, acanthosis, and inflammation; electron microscopy can reveal characteristic curved lamellar/membrane aggregates. Useful when the phenotype or genotype remains uncertain, but invasive sampling is not mandatory when molecular findings are decisive. **PMIDs: 21856041, 19119129.** [45][50] |
| **First-line molecular testing** | **Sequence *SLC27A4*** when the IPS pattern is convincing. Alternatively use a congenital-ichthyosis multigene panel containing *SLC27A4*; establish that the two qualifying alleles are **in trans**, preferably through parental testing. GeneReviews specifically recommends starting IPS testing with *SLC27A4*. [105] |
| **If initial sequencing is unresolved** | Assess **gene-level deletion/duplication**, then consider exome or genome sequencing and clinical/genetic re-evaluation. WES or WGS can help with atypical cases or alternative diagnoses; **CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not routine IPS tests**. A reported exons **8–10** deletion supports considering copy-number assessment. [105][145] |
| **Specialized omics** | RNA studies can investigate a difficult splice allele, but routine transcriptomics, proteomics, metabolomics, epigenomics, and liquid biopsy have **no established IPS diagnostic role**. [105][web:31974308] |

A **2024 Finnish retrospective study** found one patient with homozygous pathogenic *SLC27A4* p.(Cys168*) through Sanger sequencing. Its overall congenital-ichthyosis testing results—**33 molecular diagnoses among 41 tested patients**—must **not** be presented as an IPS-specific test sensitivity. **PMID: 39189679**; https://pubmed.ncbi.nlm.nih.gov/39189679/. [135][199]

The differential includes **harlequin ichthyosis** (*ABCA12*; characteristic severe constrictive plates), other congenital ichthyoses including **TGM1-related** disease, and syndromic disorders with neonatal skin changes. Respiratory disease can occur in other severe ichthyoses, so the **combination** of prematurity, vernix-like scale, eosinophilia, and amniotic-fluid findings is more informative than one feature. There is no IPS-specific population newborn biochemical screen or validated standalone clinical scoring criterion. [52][105][web:12285567]

## 11. Outcome and prognosis

The 2025 review identified **six reported deaths among 59 patients (10.2%)**, occurring by six months; its estimated **six-month survival was 87.6% (95% CI 78.8%–97.4%)** among cases with usable follow-up. These figures describe **published cases**, with ascertainment, missing-data, and short-follow-up limitations; they are **not** a general-population mortality rate or an estimate of untreated risk. Severe early respiratory/cardiac complications and sepsis were reported among fatal cases. Most surviving patients improve markedly after the neonatal period, though atopy, pruritus, and milder skin findings may continue. No reliable IPS-specific five- or ten-year survival, life expectancy, disability rate, EQ-5D/SF-36 result, or validated prognostic biomarker is established. **PMID: 40000070**; https://pubmed.ncbi.nlm.nih.gov/40000070/. [web:12285567]

## 12. Treatment

**There is no established treatment that corrects the inherited FATP4 defect.** Management is principally neonatal airway support and supportive skin care, followed by individualized care for persistent skin or allergic symptoms. The congenital-ichthyosis guideline titled the **“2024 update” was published April 7, 2025**; its IPS-specific recommendation—immediate oropharyngeal suction, with ventilation/intubation as needed, and NICU care—is **expert/low-level evidence (level 4, grade D)**. [106]

| Intervention | IPS application, evidence, and cautions | Suggested NCIT annotation |
|---|---|---|
| **Immediate oropharyngeal suction; NICU assessment** | IPS-specific guideline recommendation at delivery, reflecting the aspiration hazard. [106] | Map to the current NCIT **oropharyngeal suctioning** and **neonatal intensive care** concepts after code verification. |
| **Oxygen, CPAP, or invasive ventilation when indicated** | Treat respiratory compromise according to neonatal findings; **16/59** published cases reported noninvasive ventilation and **14/59** invasive ventilation, with substantial missing treatment reporting and some overlap. These are **use counts, not response rates**. [web:12285567] | NCIT **oxygen therapy**, **noninvasive ventilation**, **mechanical ventilation** concepts; verify current codes. |
| **Temperature/humidity, fluids, electrolytes, and nutrition** | Individualize neonatal supportive care. Humidified incubators, monitoring, and nutritional support are described in broader severe congenital-ichthyosis guidance; do not assume every IPS infant requires an incubator. [106][web:12285567] | NCIT **supportive care** and **nutritional support** concepts; verify current codes. |
| **Gentle cleansing and bland emollients** | Reduce dryness and support skin care, commonly with petrolatum/paraffin preparations. Because birth scale often sheds spontaneously, **IPS-specific comparative benefit is unproven**. Avoid contamination and monitor skin condition. [web:12285567][106] | NCIT **skin care/emollient therapy** concept; verify current code. |
| **Treatment of clinically diagnosed atopic dermatitis, allergy, infection, or pruritus** | Treat the *identified condition* using age-appropriate usual care; no IPS-specific drug-response or pharmacogenomic rule is validated. Antibiotics are for suspected/confirmed infection, **not routine prophylaxis**. [45][web:12285567] | NCIT **symptom management** or the intervention-specific drug concept, once an actual therapy is recorded. |
| **Keratolytics or retinoids in selected later cases** | Specialist judgment is required; evidence from other ichthyosis types must not be represented as IPS trial evidence. Broader neonatal congenital-ichthyosis guidance **contraindicates salicylic acid** because of systemic toxicity risk and cautions against potentially absorbed active topical agents. [16][106] | Drug-specific NCIT concept only if actually used; **not** a standard IPS intervention. |
| **Surgery or rehabilitation for an exceptional complication** | One reported constrictive-scale **compartment syndrome** required escharotomy/fasciotomy and later motor rehabilitation. It is **not routine disease treatment**. [web:12285567] | NCIT **fasciotomy** or **rehabilitation** concepts if applicable; verify codes. |

No IPS-specific approved gene, cell, RNA, immunologic, or molecularly targeted replacement therapy—and no established IPS-specific treatment-response rate—was identified in the consulted sources. Experimental mouse keratinocyte rescue demonstrates a biological principle, **not** a clinically available human gene therapy. [201][web:12285567]

## 13. Prevention

**Primary prevention of the genotype** is not available through lifestyle modification or vaccination. For families with a known causative genotype, **carrier/parental testing, genetic counseling, prenatal testing, and preimplantation genetic testing** can inform reproductive decisions. **Secondary prevention of severe complications** means recognizing a high-risk pregnancy, planning delivery where neonatal airway care is available, and promptly recognizing affected newborns. **Tertiary prevention** addresses respiratory complications, skin-barrier problems, nutrition, and later atopy. There is no IPS-specific population newborn-screening program, prophylactic medication, or relevant vaccine. [105][47][106]

## 14. Other species and naturally occurring disease

| Species or breed | Gene and natural disease | Relevance and limitation |
|---|---|---|
| ***Homo sapiens***; NCBI Taxon **9606** | Biallelic *SLC27A4* causes IPS. [84] | Reference human disease. |
| **Domestic dog, *Canis lupus familiaris***; NCBI Taxon **9615**; **Great Dane**, VBO:**0200623** | Naturally occurring *SLC27A4*-related ichthyosis, **OMIA:001973-9615**. A 2015 study found an associated **g.8684G>A** allele predicted to create a splice acceptor, with markedly reduced skin FATP4 protein in affected dogs. **PMID: 26506231**; https://pubmed.ncbi.nlm.nih.gov/26506231/. [165][167][90] | Supports conservation of the epidermal function and offers veterinary carrier-testing relevance. **Canine ichthyosis is not shown to reproduce human prematurity, amniotic-fluid changes, or neonatal aspiration.** [90][45] |

The disorder is inherited rather than infectious: **no zoonotic transmission** applies. [84][90]

## 15. Model organisms and experimental systems

| Model | Recapitulated finding and research application | Important limitation |
|---|---|---|
| **Mouse, *Slc27a4/Fatp4* targeted knockout** | Hyperproliferative hyperkeratosis, abnormal ceramides, defective skin barrier, restrictive skin, impaired breathing/suckling, and neonatal lethality. Establishes an upstream requirement for FATP4 in epidermal integrity. **PMID: 12821645**; https://pubmed.ncbi.nlm.nih.gov/12821645/. [197][198] | More severe and often lethal than the course of many human survivors; it does **not** reproduce the full obstetric IPS phenotype. |
| **Mouse, *Fatp4* knockout lipid analysis** | Approximately **90% lower acylceramide** than wild type, altered other ceramides, and severe barrier dysfunction; tests the ω-hydroxy-fatty-acid/acylceramide mechanism. **PMID: 31974308**; https://pubmed.ncbi.nlm.nih.gov/31974308/. [web:31974308] | Mouse epidermal biochemistry strengthens, but does not replace, direct measurement across a representative human IPS cohort. |
| **Mouse, keratinocyte-specific FATP4 re-expression on a mutant background** | Rescued neonatally lethal skin defects and produced viable, fertile mice; tests whether restoring cutaneous enzyme function can address the model phenotype. Moulson and colleagues, **2007**. [201][202] | A genetic rescue experiment, **not** an available human treatment. |
| **Mouse, spontaneous *Slc27a4* splice-site mutant** | Inherited skin phenotype resembling congenital ichthyosis; useful for genotype–barrier studies. **PMID: 23226340**; https://pubmed.ncbi.nlm.nih.gov/23226340/. [30] | Human pregnancy and airway manifestations are not established by its skin resemblance. |
| **Human patient fibroblasts/keratinocytes and FATP4-knockdown keratinocytes** | Assay altered fatty-acid activation, lipid incorporation, protein expression, and acylceramide production. **PMIDs: 19631310, 31974308.** [84][web:31974308] | Cultures cannot reproduce a fetus, pregnancy, or neonatal airway aspiration. |
| **Naturally affected Great Danes** | Validate conserved *SLC27A4* skin biology outside engineered models. **PMID: 26506231.** [90] | A related canine ichthyosis, **not proven to be the entire human IPS syndrome**. |

**Knowledge-base priorities:** record *SLC27A4* biallelic germline disease causation as established; record **ω-*O*-acylceramide deficiency** as strongly supported mechanistically by in-vitro and mouse evidence; retain **prenatal fluid accumulation and aspiration** as clinically supported downstream mechanisms with the indicated inferential links. Keep case-report frequencies, individual variant classifications, and animal phenotypes explicitly separate from population penetrance and validated human-treatment effects. [84][web:31974308][45][web:12285567]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC8613581` (1 mention) - Gene Ontology Enrichment Analysis of Renal Agenesis: Improving Prenatal Molecular Diagnosis.
  - shared terms: neonatal

Weighed against this report's own most characteristic terms: `web`, `ips`, `neonatal`, `disease`, `skin`, `respiratory`, `ichthyosis`, `established`, `patient`, `ips-specific`, `slc27a4`, `fluid`, `affected`, `airway`, `prematurity`, `human`, `validated`, `phenotype`, `scale`, `fatp4`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012089` (2 mentions) - the report calls it "MONDO"; MONDO calls it **ichthyosis prematurity syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `OMIM`, `OMIA`.