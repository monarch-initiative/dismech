---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T11:41:17.606114'
end_time: '2026-10-27T11:47:41.396939'
duration_seconds: 383.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Dysplasminogenemia
  mondo_id: MONDO:0100538
  category: Genetic
  causal_genes: PLG
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
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 12
  validator_version: 0.4.0
term_validation:
  total_terms: 27
  verified: 23
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 6
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0100538
    reported_labels:
    - Mondo
    ontology_label: dysplasminogenemia
  - term_id: DOID:0111592
    reported_labels:
    - Disease Ontology
    ontology_label: plasminogen deficiency type I
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
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
- **Disease Name:** Dysplasminogenemia
- **MONDO ID:** MONDO:0100538 (if available)
- **Causal gene(s):** PLG
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

Please provide a comprehensive research report on **Dysplasminogenemia** covering all of the
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

# Dysplasminogenemia — comprehensive disease-characteristics report

**Dysplasminogenemia (MONDO:0100538) is a congenital qualitative disorder of plasminogen caused by germline variants in the causal gene *PLG*.** It is also called **type II plasminogen deficiency** and is defined biochemically by reduced plasminogen functional activity despite a normal or only mildly reduced plasminogen antigen concentration. Unlike quantitative type I plasminogen deficiency—hypoplasminogenemia—dysplasminogenemia is usually asymptomatic and has not been convincingly shown to cause ligneous conjunctivitis or other fibrin-rich mucosal pseudomembranes. Its status as an independent thrombophilia remains controversial: individual thrombotic cases and small cerebral-infarction series have been reported, but family studies, population data, ClinVar interpretation, and a *Plg*-Tochigi knock-in mouse model argue that the common p.Ala620Thr variant alone is generally insufficient to produce thrombosis. [2][17][30][375]

**Evidence scope.** Most available information comes from aggregated disease databases, research cohorts, pedigrees, case reports, laboratory studies, and animal models—not longitudinal EHR-derived disease cohorts. The 2024 authoritative review is Brito-Robinson et al., published June 25, 2024, *Frontiers in Cardiovascular Medicine*, PMID **38984351**, DOI **10.3389/fcvm.2024.1406953**, [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11231438/). [375]

---

## 1. Disease information

### 1.1 Definition

Dysplasminogenemia is a **qualitative plasminogen deficiency**:

- **Plasminogen activity:** reduced.
- **Plasminogen antigen:** normal or slightly reduced.
- **Activity-to-antigen ratio:** reduced.
- **Usual clinical state:** asymptomatic.
- **Characteristic type I mucosal disease:** ordinarily absent.

This distinction is essential because OMIM and some terminology systems combine dysplasminogenemia and type I plasminogen deficiency under the same record, even though their biochemical and clinical phenotypes differ substantially. OMIM states that type II patients “are usually asymptomatic” and that ligneous pseudomembranes have been associated with type I, not type II disease. [2]

### 1.2 Identifiers and terminology

| Resource | Identifier or term | Interpretation and URL |
|---|---|---|
| Mondo | **MONDO:0100538** | Dysplasminogenemia; requested primary disease identifier. Persistent URI: [MONDO:0100538](http://purl.obolibrary.org/obo/MONDO_0100538). ClinVar maps this identifier to dysplasminogenemia. [4] |
| OMIM phenotype | **217090** | OMIM uses the same phenotype record for “Dysplasminogenemia” and “Plasminogen deficiency, type I.” This is a source of conceptual conflation. [OMIM 217090](https://omim.org/entry/217090). [2] |
| OMIM gene | **173350** | *PLG*, plasminogen. [OMIM 173350](https://www.omim.org/entry/173350). [1] |
| Orphanet | **ORPHA:722** | Hypoplasminogenemia; broader/primarily type I record rather than a clean type II-specific concept. [2] |
| MedGen | **C4225445**; concept also indexed as **CN043003** | Dysplasminogenemia. [4][94] |
| MeSH supplementary concept | **C566897** | “Plasminogen Deficiency, Type I”; confusingly lists “Dysplasminogenemia” as an entry term. [77] |
| ICD-10-CM | **E88.02** | Plasminogen deficiency; not type II-specific. [2] |
| ICD-11 | No dedicated type II code identified | Use the closest inherited metabolic/coagulation disorder concept locally, preserving MONDO and *PLG* identifiers. |
| SNOMED CT | **95844003** | Plasminogen deficiency; not reliably type-specific. [2] |
| Disease Ontology | **DOID:0111592** | Mapped by OMIM to the broader plasminogen-deficiency concept. [2] |

### 1.3 Synonyms

- Type II plasminogen deficiency
- Congenital plasminogen deficiency type II
- Qualitative plasminogen deficiency
- Abnormal plasminogen
- Hereditary dysplasminogenemia
- Dysplasminogenaemia
- Plasminogen Tochigi/Tochigi I/Tochigi II, Nagoya, Kagoshima, or M5—historical variant/protein names primarily associated with p.Ala620Thr
- Plasminogen Osaka—associated with a p.Asp695Asn precursor-protein variant, historically numbered p.Asp676Asn in mature plasminogen

**Not preferred as exact synonyms:** hypoplasminogenemia, type I plasminogen deficiency, ligneous conjunctivitis, and ligneous membranitis. Those denote the quantitative, clinically different disorder.

---

## 2. Etiology, risk, protective factors, and gene–environment interaction

### 2.1 Primary cause

The initiating cause is a **germline *PLG* variant that permits production of immunoreactive plasminogen but reduces activation or catalytic function**. Most reported type II-associated alleles are missense substitutions, particularly in the serine-protease domain. Approximately 86% of the variants assembled in the 2024 review clustered in that domain. [37]

The best-characterized allele is:

- **NM_000301.5:c.1858G>A, NP_000292.1:p.Ala620Thr**
- Mature-protein historical numbering: **p.Ala601Thr**
- dbSNP: **rs121918027**
- Historical protein: **plasminogen Tochigi**
- ClinVar: **VCV000013574.13**, conflicting classifications, with current submissions ranging from benign/likely benign to VUS; the old OMIM pathogenic submission is flagged as an outlier. [92]

### 2.2 Risk factors

| Factor | Evidence and interpretation |
|---|---|
| *PLG* dysfunctional allele | Establishes the biochemical phenotype. Heterozygous p.Ala620Thr generally produces activity near 50–70%; homozygotes can have activity around 1.5–25%, yet may remain clinically well. [17][108] |
| Biallelic or compound-heterozygous variants | Can produce more severe biochemical deficiency. A 2025 report described p.Gly568Arg/p.Ala620Thr with activity 27% and antigen 103%, meeting the definition of type II deficiency; PMID **41398600**, published December 15, 2025. [18] |
| Additional thrombophilia or provoking condition | Likely explains at least some thrombotic reports. Examples include antiphospholipid antibodies, paroxysmal nocturnal hemoglobinuria, elevated lipoprotein(a), cardiac myxoma, infection, and conventional VTE triggers. These are associations, not validated *PLG*-specific modifiers. [16][27][97] |
| East Asian ancestry | Increases the likelihood of carrying p.Ala620Thr because of a founder/population effect, but does not itself establish symptomatic disease. [108][117] |
| Family history of thrombosis | Relevant to overall thrombotic risk, but affected and unaffected relatives often fail to cosegregate with the *PLG* biochemical phenotype. [19][30] |

A study of 1,192 thrombophilia probands found plasminogen deficiency in 1.9% overall—2.2% among venous and 1.4% among arterial cases—but thrombotic events were equally frequent in deficient and nondeficient relatives, and 11 of 23 probands had another thrombophilia or circumstantial risk factor. PMID **9684804**. [26]

### 2.3 Protective factors

No validated genetic or environmental protective factor has been identified. Proposed explanations for low clinical penetrance include:

1. **Residual plasmin activity:** even very low activity may be sufficient for physiologic clot clearance.
2. **Preserved kringle domains and receptor binding:** most type II variants leave extravascular and clot-surface localization intact.
3. **Compensatory fibrinolysis:** leukocyte-derived proteases and matrix metalloproteinases may partially compensate.
4. **Normal antigen concentration:** abundant dysfunctional protein may retain enough activity when concentrated on fibrin or cell surfaces.

These mechanisms are plausible but not proven protective modifiers in human carriers. [37][124]

### 2.4 Gene–environment interaction

A reasonable model is that a dysfunctional *PLG* allele lowers fibrinolytic reserve, while **surgery, trauma, immobilization, infection, pregnancy, estrogen exposure, malignancy, cardiac embolic sources, or another thrombophilia** may determine whether thrombosis becomes clinically manifest. This interaction remains inferential: the common p.Ala620Thr allele has not shown a reproducible independent VTE effect. The 2017 mouse investigators similarly cautioned that their negative models did not exclude effects under other genetic or environmental conditions. [124]

No toxin, pollutant, radiation exposure, diet, smoking behavior, infectious agent, or occupation is known to cause inherited dysplasminogenemia.

---

## 3. Phenotypes

### 3.1 Core and reported phenotypes

| Phenotype type | Phenotype and characteristics | Frequency/onset/course | Suggested HPO term |
|---|---|---|---|
| Laboratory abnormality—defining | Reduced plasma plasminogen functional activity, usually with a reduced activity:antigen ratio | Present from birth; stable biochemical trait; heterozygotes often approximately 50–70%, while biallelic cases can be much lower | No dedicated “reduced plasminogen activity” HPO term was identified; use **HP:0011900 Abnormality of coagulation** with a local laboratory annotation |
| Laboratory abnormality—defining | Normal or mildly reduced plasminogen antigen despite low activity | Expected in type II; distinguishes it from type I | **HP:0011900** plus explicit assay result |
| Clinical state | No symptoms | Apparently the most frequent phenotype; may persist lifelong even in homozygotes | **HP:0000001 All** is not appropriate; encode “asymptomatic” as a clinical-status field rather than an HPO phenotype |
| Vascular manifestation—disputed association | Venous thrombosis/DVT | Rare case reports; onset from adolescence to adulthood; episodic and potentially recurrent; causality uncertain | **HP:0004936 Venous thrombosis**; **HP:0002625 Deep venous thrombosis**; **HP:0004850 Recurrent DVT** [197][198][201] |
| Vascular manifestation—disputed association | Pulmonary embolism | Rare case reports; acute, potentially severe | **HP:0002204 Pulmonary embolism** |
| Vascular manifestation—disputed association | Cerebral infarction/ischemic stroke or cerebral venous sinus thrombosis | Reports include ages 14, 16, and 19 years in three 2023 pedigrees; broader 2026 retrospective series included ages 16–70; association is not yet causal | **HP:0025722 Cerebral infarction**; **HP:0002140 Ischemic stroke**; **HP:0004936 Venous thrombosis** [361][367] |
| Neurologic consequence | Hemiparesis, limb weakness, ataxia, headache | Acute and lesion-dependent in reported stroke cases | **HP:0001269 Hemiparesis** [373] |
| Ocular vascular manifestation—disputed | Retinal vein/artery occlusion or retinochoroidal vascular disorder | Very rare case reports; unilateral or bilateral site-specific disease; lipoprotein(a) may contribute | Use relevant retinal vascular occlusion term; broader **HP:0004936** if no exact HPO mapping |
| Tissue phenotype specifically not expected | Ligneous conjunctivitis, gingivitis, airway/genital pseudomembranes | Not reported as a characteristic of isolated type II disease; these should prompt reconsideration of type I deficiency | Do not assign type I HPO terms to type II solely because OMIM/Orphanet combines the records |

In the 2023 three-pedigree study, all three probands had heterozygous p.Ala620Thr and plasminogen activities of **65%, 56%, and 58%**, with normal-range antigen. Several clinically unaffected relatives carried the same variant and had approximately 43–54% activity, illustrating low clinical penetrance and poor cosegregation. Published March 30, 2023; PMID **37065478**. [32]

### 3.2 Severity, progression, and quality of life

- **Biochemical severity and clinical severity correlate poorly.** A Korean woman homozygous for p.Ala620Thr had 25% activity and no VTE by age 53, while her heterozygous son had extensive arterial emboli in the setting of atrial myxoma. PMID **35244080**, published March 4, 2022. [17]
- Dysplasminogenemia itself is not ordinarily progressive.
- Thrombotic events, when they occur, are acute and organ-dependent rather than a predictable stage of the disorder.
- There are **no disease-specific EQ-5D, SF-36, PROMIS, disability, or quality-of-life cohorts for type II deficiency**. Asymptomatic carriers should have no direct quality-of-life impairment; stroke, PE, or retinal occlusion can cause substantial event-specific disability.

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Field | Value |
|---|---|
| Gene | ***PLG***, plasminogen |
| HGNC | **HGNC:9071** |
| NCBI Gene | **5340** |
| OMIM gene | **173350** |
| Ensembl | **ENSG00000122194** |
| UniProt | **P00747** |
| Location | **6q26**, GRCh38 approximately chr6:160,702,105–160,754,097 |
| Gene structure | 19 exons; approximately 52 kb |
| Protein | Secreted 810-aa preprotein; 19-aa signal peptide removed to produce a 791-aa mature zymogen |
| Major expression | Liver-enriched, predominantly hepatocyte-derived |
| Protein domains | N-terminal activation peptide, five kringle domains, activation loop, C-terminal trypsin-like serine-protease domain |
| Activation | Cleavage at precursor Arg561–Val562 by tissue-type or urokinase-type plasminogen activator |
| Catalytic triad | Mature-protein His603–Asp646–Ser741; precursor numbering is shifted by the signal peptide |

The NCBI gene record confirms HGNC:9071, NCBI Gene 5340, Ensembl ENSG00000122194, and OMIM 173350. [256] The Human Protein Atlas classifies *PLG* as tissue-enriched in liver. [226]

### 4.2 Reported type II-associated variants

Nomenclature varies because older literature numbers residues after removal of the signal peptide. The table therefore gives current precursor-protein HGVS first.

| Variant, current HGVS | Historical mature-protein name | Domain/mechanism | Current evidence/classification |
|---|---|---|---|
| **c.1120G>T, p.Val374Phe** | p.Val355Phe | Interdomain region near kringles 3/4; reduced activity and sometimes antigen; predicted destabilization | Reported as pathogenic in the 2024 structural review, but phenotype overlap with type I is possible |
| **c.1699T>G, p.Cys567Gly** | p.Cys548Gly | Serine-protease region; loss of cysteine likely disrupts disulfide/structure | Very rare; no robust ClinVar classification reported |
| **c.1702G>A, p.Gly568Arg** | p.Gly549Arg | Near activation/serine-protease region; compound heterozygosity with p.Ala620Thr reported in 2025 | Newly reported; pathogenicity requires replication; PMID **41398600** [18] |
| **c.1858G>A, p.Ala620Thr** | p.Ala601Thr; Tochigi/M5/Nagoya/Kagoshima | Near catalytic His; protein is activated to two-chain plasmin but has severely impaired proteolytic activity | ClinVar **conflicting**, including benign/likely benign/VUS; biochemical effect is established but disease penetrance is low |
| **c.2083G>A, p.Asp695Asn** | p.Asp676Asn; Osaka | Creates a proposed Asn-Arg-Thr N-glycosylation site near the active region, disrupting activity | Rare; primary functional report PMID **9239510** [96] |
| **c.2108G>A, p.Gly703Asp** | — | Serine-protease domain | Reported in a 2026 cerebral-infarction series; classification not established |
| **c.2134G>A, p.Gly712Arg** | p.Gly693Arg | Serine-protease domain; predicted destabilization | VUS in the 2024 review |
| **c.2144T>C, p.Leu715Pro** | p.Leu696Pro | Serine-protease domain; proline likely distorts local structure | Rare; no settled classification |
| **c.2251G>A, p.Gly751Arg** | p.Gly732Arg; Kanagawa-I when combined with p.Ala620Thr | Serine-protease domain; compound heterozygous activity as low as 7.7% reported | ClinVar VUS |
| **c.398A>G, p.His133Arg** | — | Kringle-region variant | Newly reported in the 2026 cerebral-infarction series; functional classification not established |

The 2024 review’s seven-variant type II table included p.Val374Phe, p.Cys567Gly, p.Ala620Thr, p.Asp695Asn, p.Gly712Arg, p.Leu715Pro, and p.Gly751Arg. [37] The 2026 retrospective study added p.His133Arg, p.Gly568Arg, and p.Gly703Asp among 18 selected cerebral-infarction patients; because that cohort was preselected for infarction plus low PLG activity and lacked population controls, it cannot by itself quantify penetrance or relative risk. PMID **41778291**, published online March 4, 2026. [21]

### 4.3 p.Ala620Thr frequency

- gnomAD v4 frequency reported by the 2024 review: **1.675% in East Asians**, approximately **0.051% overall**.
- Historical estimates: allele frequency approximately **2.0% in Japanese**, **1.5% in Chinese**, and **1.6–2.33% in Koreans**.
- Approximately 3–4% of East Asians may be heterozygous.
- Under Hardy–Weinberg assumptions, Japanese homozygotes are expected around **1 in 2,500**; Korean estimates were **0.0256–0.0543%**, corresponding to roughly 13,000–28,000 people in a population of 52 million. [108][117]

These frequencies are too high for p.Ala620Thr to be interpreted as a highly penetrant monogenic thrombophilia.

### 4.4 Variant origin and other molecular categories

- **Origin:** germline.
- **Somatic disease mechanism:** none established.
- **Functional class:** principally partial or severe loss of catalytic function; dominant-negative activity has not been established.
- **Gain of function:** not supported.
- **Modifier genes:** none validated. *PROS1*, *SERPINE1*, *CPB2/TAFI*, *LPA*, and other hemostatic genes are biologically plausible but not demonstrated disease modifiers.
- **Chromosomal abnormalities:** no recurrent deletion, duplication, translocation, inversion, or aneuploidy is established for isolated dysplasminogenemia.
- **Epigenetics:** no disease-specific methylation, histone, or chromatin signature is known.
- **Structural variation/CNV:** not a recognized common cause of the qualitative phenotype.
- **Anticipation and repeat expansion:** not applicable.
- **Germline mosaicism:** not reported.

---

## 5. Environmental, lifestyle, and infectious information

No environmental or infectious agent causes the inherited biochemical defect. Potential relevance is limited to **provocation of thrombosis in a carrier**, not causation of dysplasminogenemia:

- Major surgery, trauma, immobility, cancer, pregnancy/postpartum state, estrogen exposure, obesity, smoking, and infection should be assessed as conventional thrombotic factors.
- Pneumonia and PNH were both present in one historical thrombosis case, making attribution to plasminogen Tochigi uncertain. [16]
- Local injury and infection trigger ligneous lesions in type I deficiency, but this has **not** been shown for type II.
- No diet, exercise regimen, alcohol pattern, occupational exposure, toxin avoidance, or vaccine specifically modifies the type II biochemical phenotype.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **A germline missense variant in *PLG* leads to** synthesis and secretion of structurally abnormal but immunoreactive plasminogen.
2. **Normal or near-normal secretion leads to** a normal/slightly reduced antigen concentration, while the structural lesion **results in** impaired activation, active-site geometry, stability, or catalytic activity.
3. **Impaired functional plasminogen leads to** reduced generation of effective plasmin after cleavage by tPA or uPA.
4. **Reduced effective plasmin results in** slower proteolysis of cross-linked fibrin and reduced fibrinolytic reserve, demonstrated in biochemical assays and p.Ala620Thr knock-in mouse plasma.
5. **The pathway then branches:**
   - **Branch A—usual outcome:** residual plasmin activity, clot-surface concentration, receptor binding, and compensatory proteases **lead to** adequate in-vivo fibrin clearance and lifelong absence of symptoms.
   - **Branch B—inferred and incompletely demonstrated:** an additional thrombotic trigger or modifier **may lead to** persistence of an intravascular fibrin clot.
6. **Persistent or embolizing clot, if it occurs, leads to** DVT, PE, cerebral infarction, retinal vascular occlusion, or other ischemic injury; direct causation by isolated dysplasminogenemia remains unproven.
7. **Preservation of antigen and sufficient extravascular activity likely leads to** normal mucosal wound repair, explaining the absence of classic ligneous lesions—an inference supported by human observations and knock-in mice.

### 6.2 Protein dysfunction

Plasminogen is recruited to fibrin through lysine-binding sites in its kringle domains. tPA or uPA cleaves it at Arg561–Val562 to form plasmin; plasmin then solubilizes cross-linked fibrin. Reactome’s **Dissolution of Fibrin Clot, R-HSA-75205** describes clot-surface tPA activation as the main intravascular mechanism. [242]

For p.Ala620Thr, the substituted threonine lies close to the catalytic histidine. The landmark structural study concluded:

> “The Thr at position 55 in plasminogen (plasmin) Tochigi may perturb His-57 such that the proton transfers associated with the normal catalytic process cannot occur.”

Miyata et al., 1982; PMID **6216475**, DOI **10.1073/pnas.79.20.6132**. [100]

Thus the protein can be cleaved into two-chain plasmin but remains catalytically inefficient. p.Asp695Asn may instead create an abnormal N-glycosylation motif near the active site. [91]

### 6.3 Pathways and ontology suggestions

| Biological component | Suggested ontology annotation |
|---|---|
| Fibrin-clot dissolution | Reactome **R-HSA-75205** |
| Fibrinolysis | **GO:0042730**; note that some GO browsers now flag this term as obsolete, so verify against the current GO release before production use. [190] |
| Proteolysis | **GO:0006508** |
| Serine-type endopeptidase activity—active plasmin | **GO:0004252** |
| Extracellular space | **GO:0005615** |
| Extracellular region | **GO:0005576** |
| Blood coagulation, fibrin-clot formation—upstream substrate-generating process | **GO:0072378** |
| Plasminogen activation | Historical **GO:0031639**, now marked obsolete; use a current replacement/parent term in the deployed GO version. [182] |
| Complement and coagulation cascades | KEGG **hsa04610** |
| Hepatocyte source | **CL:0000182** |
| Blood-vessel endothelial cell/clot surface | **CL:0000071** |
| Neutrophil/monocyte compensatory fibrinolysis | Relevant cell types, but their compensatory role in human dysplasminogenemia is inferred rather than established |

### 6.4 Cellular, immune, tissue, and metabolic effects

- **Upstream:** abnormal PLG protein structure and catalytic activity.
- **Downstream:** decreased fibrin breakdown.
- **Cellular source:** hepatocytes produce most circulating plasminogen.
- **Sites of activation:** fibrin clot surfaces and cell membranes, especially endothelial and leukocyte surfaces.
- **Inflammation:** plasmin participates in leukocyte migration, extracellular-matrix processing, complement interactions, and wound repair, but no reproducible immune phenotype has been demonstrated in type II patients.
- **Tissue injury:** if a clinically important thrombus occurs, injury is secondary ischemia/infarction—not direct PLG cytotoxicity.
- **Metabolism:** no characteristic energy, lipid, amino-acid, or small-molecule metabolomic abnormality is known.

### 6.5 Molecular profiling and advanced technologies

No disease-specific human:

- transcriptomic signature,
- proteomic panel beyond plasminogen antigen/activity,
- metabolomic or lipidomic signature,
- single-cell atlas,
- spatial-transcriptomic study,
- patient iPSC/organoid model,
- CRISPR screen, or
- integrated multi-omics diagnostic classifier

has been validated for dysplasminogenemia. Computational structural modeling has been used to predict destabilization of rare missense variants, but such predictions are not substitutes for functional or clinical classification. [37]

---

## 7. Anatomical structures affected

### 7.1 Primary anatomical context

The condition is primarily a **circulating plasma-protein abnormality**, not an organ-specific degenerative disorder.

| Level | Structure/cell/compartment | Suggested ontology |
|---|---|---|
| Organ producing protein | Liver | **UBERON:0002107** |
| Producing cell | Hepatocyte | **CL:0000182** |
| Circulating compartment | Blood | **UBERON:0000178** |
| Functional compartment | Blood plasma/extracellular space | **GO:0005615** |
| Potential target system | Blood vessel | **UBERON:0001981** |
| Vascular cell | Blood-vessel endothelial cell | **CL:0000071** |
| Veins in reported VTE | Vein | **UBERON:0001638** |
| Secondary organs after thrombosis | Brain, lung, retina, kidney, spleen, limbs, heart | Site depends on the thrombotic/embolic event |

There is no characteristic lateralization. Reported strokes and retinal events can be unilateral according to the vessel involved.

### 7.2 Subcellular level

*PLG* contains a signal peptide and enters the hepatocyte secretory pathway before release to the extracellular compartment. No disease-specific accumulation in the nucleus, mitochondrion, lysosome, or endoplasmic reticulum has been demonstrated. The key functional defect is extracellular.

---

## 8. Temporal development and natural history

- **Biochemical onset:** congenital and lifelong.
- **Clinical onset:** usually never.
- **When thrombosis is reported:** from childhood/adolescence through late adulthood; no reliable typical age exists.
- **Course:** stable biochemical abnormality; possible acute, episodic thrombotic events.
- **Progression:** there are no accepted early/intermediate/advanced stages.
- **Remission:** not applicable to the genotype or biochemical phenotype. A thrombotic event may resolve with treatment but does not normalize the inherited PLG defect.
- **Critical periods:** no PLG-specific window is established; conventional high-risk periods—surgery, prolonged immobility, pregnancy/postpartum, active cancer, major infection—should be treated according to ordinary VTE-risk protocols.
- **Natural-history limitation:** there is no large unselected, longitudinal type II registry capable of calculating age-specific penetrance or recurrence.

---

## 9. Inheritance and population epidemiology

### 9.1 Inheritance

Terminology resources often label OMIM 217090 **autosomal recessive** because the record primarily reflects type I deficiency. For dysplasminogenemia, the more accurate description is:

- **Autosomal inheritance with a codominant biochemical phenotype.**
- Heterozygotes have intermediate activity and can be identified biochemically.
- Homozygotes/compound heterozygotes generally have more severe activity reduction.
- Clinical thrombotic penetrance is incomplete and apparently very low.
- Expressivity is variable, ranging from no symptoms to disputed thrombotic manifestations.

A 2023 report described it as an “autosomal disease that exhibits incomplete dominance,” but this refers mainly to biochemical expression rather than established clinical penetrance. [327]

### 9.2 Epidemiology

| Measure | Best current estimate |
|---|---|
| Symptomatic disease prevalence | Unknown |
| Annual incidence | Unknown |
| p.Ala620Thr East Asian allele frequency | Approximately 1.5–2.3%, depending on population/database |
| Estimated heterozygote frequency in East Asians | Approximately 3–4% |
| Estimated Japanese homozygote frequency | Approximately 1 in 2,500 |
| Korean predicted homozygote frequency | Approximately 0.0256–0.0543% |
| Scottish dysplasminogenemia estimate in an older report | Approximately 0.03%, assay/definition dependent [118] |
| Sex ratio | No credible type II-specific sex difference |
| Geographic concentration | Japan, Korea, and China for p.Ala620Thr; other rare variants occur globally |

These figures describe **genotype or laboratory phenotype**, not clinically symptomatic disease.

### 9.3 Other inheritance features

- **Penetrance:** high for reduced activity, low/uncertain for thrombosis.
- **Anticipation:** absent.
- **Founder effect:** likely for p.Ala620Thr in East Asians. [37]
- **Consanguinity:** relevant to rare biallelic variants but less important for the common East Asian allele.
- **Germline mosaicism:** not reported.
- **Carrier frequency:** population-specific; “carrier” is somewhat imprecise because heterozygotes express the biochemical phenotype.
- **Ethnic distribution:** p.Ala620Thr is common in East Asia and very rare in European and African datasets.
- **Sex:** both sexes affected; no proven male or female excess.
- **Age:** congenital laboratory abnormality at every age.

---

## 10. Diagnostics

### 10.1 Recommended diagnostic sequence

1. **Establish the indication.** Consider testing in unexplained low fibrinolytic activity, an affected family, or selected unusually young/unexplained thrombosis—not as routine population thrombophilia screening.
2. **Measure plasminogen activity** in citrated plasma, usually by chromogenic substrate assay after streptokinase or urokinase activation.
3. **Repeat an abnormal result** when the patient is clinically stable.
4. **Measure plasminogen antigen** by ELISA, nephelometry, immunoturbidimetry, or equivalent immunoassay.
5. **Interpret the pattern:**
   - Low activity + low antigen in parallel → type I/quantitative deficiency.
   - Low activity + normal or near-normal antigen → type II/dysplasminogenemia.
6. **Exclude acquired causes:** liver disease, DIC/consumption, leukemia, primary fibrinolysis, recent cardiopulmonary bypass, or recent thrombolytic therapy.
7. **Perform *PLG* sequencing** when confirmation, family testing, or variant characterization will alter counseling or management.
8. **Investigate conventional causes of thrombosis independently**; finding a PLG variant should not stop evaluation for APS, myeloproliferative neoplasm, PNH, malignancy, cardiac embolic sources, or ordinary provoking factors.

A plasminogen activity below approximately **75%** may indicate congenital deficiency after acquired causes are excluded; absolute reference limits are assay-specific. [331]

### 10.2 Testing modalities

| Test | Utility |
|---|---|
| Chromogenic plasminogen activity | Primary functional test; detects both quantitative and qualitative deficiency |
| Plasminogen antigen | Essential for distinguishing type I from type II |
| Activity:antigen ratio | Useful summary of specific activity |
| Clot-lysis or plasmin-generation assays | Research/advanced characterization; may better reflect integrated fibrinolysis |
| Isoelectric focusing | Historical method for Tochigi/M5 and other abnormal protein isoforms |
| *PLG* single-gene sequencing | Preferred confirmatory molecular test |
| Deletion/duplication analysis | Secondary test if sequencing is negative and suspicion remains; low expected yield for type II |
| Thrombosis gene panel | Useful when phenotype suggests a broader hereditary thrombophilia; one available panel includes *PLG*, *F2*, *F5*, *PROC*, *PROS1*, *SERPINC1*, *PLAT*, and others. [56] |
| WES/WGS | Reasonable for unresolved complex familial disease, but not required when the biochemical phenotype is clear and *PLG* sequencing is available |
| RNA sequencing/proteomics/metabolomics | Not validated diagnostic tests |
| CMA, karyotype, FISH | No routine role |
| Mitochondrial or repeat-expansion testing | No role |
| Imaging | Not diagnostic of dysplasminogenemia; use Doppler ultrasound, CT pulmonary angiography, MRI/MR venography, retinal imaging, or other studies only for the suspected complication |
| Biopsy | No routine role; fibrin-rich pseudomembranes would suggest type I disease rather than isolated type II |

A GTR-listed test, **GTR000591164.1**, provides complete *PLG* coding-region sequencing for dysplasminogenemia and type I deficiency. [46]

### 10.3 Assay limitations

Streptokinase antibodies, plasmin inhibitors, lipoprotein(a), fibrin degradation products, aprotinin, tranexamic acid, and recent thrombolytic treatment can affect some functional methods. Functional assays should therefore be interpreted with the assay platform, clinical state, and antigen level. [335]

### 10.4 Differential diagnosis

| Differential | Distinguishing feature |
|---|---|
| Type I plasminogen deficiency | Both activity and antigen are reduced; ligneous conjunctivitis and mucosal pseudomembranes may occur |
| Acquired low plasminogen | Liver failure, DIC, leukemia, consumption, thrombolytic therapy, or major systemic illness |
| Protein C, protein S, or antithrombin deficiency | Different functional assays and genes; better-established VTE associations |
| Factor V Leiden or prothrombin G20210A | DNA-based thrombophilias with established risk estimates |
| Antiphospholipid syndrome | Persistent antiphospholipid antibodies plus clinical criteria |
| PNH or myeloproliferative neoplasm | Flow cytometry or hematologic/molecular findings; especially relevant to unusual-site thrombosis |
| Cardioembolism | Atrial fibrillation, cardiac myxoma, valvular disease, or intracardiac thrombus |
| Hereditary angioedema due to *PLG* | Distinct gain-of-function *PLG* phenotype, usually p.Lys330Glu; recurrent edema rather than low plasminogen activity |
| Dysfibrinogenemia | Abnormal fibrinogen function/antigen pattern, caused by fibrinogen genes |

### 10.5 Screening

- No population or newborn screening program is recommended.
- Routine PLG testing in VTE panels is not supported by strong evidence.
- The British Society for Haematology advises against routine coagulation-factor testing to estimate thrombosis risk and against routine heritable-thrombophilia testing when results will not alter management. [271][273]
- Targeted cascade biochemical/genetic testing may be offered after an unequivocal familial variant, primarily for counseling and interpretation of low activity.
- Prenatal or preimplantation testing is technically possible once familial variants are known, but is rarely clinically justified for isolated p.Ala620Thr because clinical penetrance is low and prognosis is generally normal.

---

## 11. Outcome and prognosis

### 11.1 Survival

No dysplasminogenemia-specific:

- five- or ten-year survival rate,
- standardized mortality rate,
- disease-attributable mortality estimate, or
- life-expectancy reduction

has been reported.

Most isolated carriers—including homozygotes with very low activity—appear to have normal survival. A Japanese compound heterozygote with 7.7% activity reportedly had a generally healthy lifespan into old age. [37]

### 11.2 Morbidity and prognostic factors

- **Most likely outcome:** lifelong asymptomatic biochemical abnormality.
- **If thrombosis occurs:** prognosis is determined by clot site, infarct size, embolic source, provoking factors, treatment delay, and recurrence—not by PLG activity alone.
- **PLG activity is not a validated prognostic biomarker.**
- Homozygosity is not reliably predictive of clinical events.
- A concurrent strong thrombophilia or cardiac source is more persuasive than an isolated p.Ala620Thr result.
- There are no validated disease-specific prognostic calculators.

The strongest negative human evidence includes 25 heterozygous family members with one thrombotic history versus two events among 41 biochemically unaffected relatives, leading the authors to conclude that heterozygous dysplasminogenemia was not associated with increased thrombosis. PMID **11039677**. [30]

---

## 12. Treatment

### 12.1 Management principles

There is **no approved or evidence-based treatment for an asymptomatic person solely because of dysplasminogenemia or a p.Ala620Thr genotype**. Management should focus on demonstrated clinical disease and conventional thrombotic risk.

| Intervention | Role in dysplasminogenemia | Evidence/limitations | Suggested NCIt intervention concept |
|---|---|---|---|
| Observation and education | Preferred for asymptomatic individuals | No evidence supports chronic therapy based only on low activity | Clinical Observation |
| Anticoagulation | Treat confirmed VTE, cerebral venous thrombosis, or other thrombotic disease according to ordinary site-specific guidelines | Case reports used heparin/warfarin, but optimal duration is determined by whether the event was provoked, recurrence risk, bleeding risk, and other causes—not PLG genotype alone | Anticoagulant Therapy |
| Antiplatelet therapy | May be indicated after arterial ischemic stroke under standard stroke guidance | No PLG-specific efficacy evidence | Antiplatelet Therapy |
| Thromboembolectomy/thrombectomy | For selected limb-, organ-, brain-, or life-threatening arterial/venous occlusion | Used successfully in a patient with atrial myxoma and systemic emboli | Thrombectomy; Embolectomy |
| Thrombolysis with alteplase/related agents | Use only under the applicable emergency protocol | Because tPA requires plasminogen as substrate, markedly dysfunctional plasminogen could theoretically reduce response; no type II dosing guideline exists | Thrombolytic Therapy |
| Plasminogen, human-tvmh—Ryplazim | **Not approved for type II disease** | FDA indication is limited to type I hypoplasminogenemia. [61] | Plasminogen Replacement Therapy |
| Fresh frozen plasma/plasminogen supplementation | No established routine role in type II | Occasionally discussed when thrombolysis is required in severe deficiency, but evidence is indirect and largely pediatric/type I | Plasma Transfusion |
| Gene, RNA, or cell therapy | None available | No clinical trials specific to type II dysplasminogenemia | Gene Therapy, if future studies arise |
| Genetic counseling | Appropriate after confirmed familial disease | Must emphasize uncertain clinical penetrance and avoid labeling p.Ala620Thr as a high-risk thrombophilia | Genetic Counseling |

An 18-year-old with PE and DVT plus heterozygous p.Ala620Thr received lifelong anticoagulation and remained event-free for two years, but this single case cannot establish a universal strategy. PMID **23772166**. [20][316]

### 12.2 Ryplazim and clinical trials

The FDA approved Ryplazim on **June 4, 2021** only for **type I plasminogen deficiency (hypoplasminogenemia)**. [62] The pivotal replacement study—NCT02690714—showed improvement of type I fibrin-rich lesions, but it does not establish benefit in asymptomatic type II carriers. PMID **29321155**. [74]

No completed or active interventional trial specifically targeting isolated dysplasminogenemia was identified. NCT02312180 and related plasminogen-replacement programs enrolled hypoplasminogenemia/severe congenital deficiency rather than a defined type II population. [292]

### 12.3 Pharmacogenomics

There is no CPIC or PharmGKB prescribing guideline based on *PLG*. Theoretical reduced responsiveness to plasminogen activators is mechanistically plausible but has not been translated into validated genotype-guided alteplase, tenecteplase, urokinase, or anticoagulant dosing.

---

## 13. Prevention

### Primary prevention

The genotype cannot be prevented after conception, and there is no indication for chronic anticoagulation in an asymptomatic p.Ala620Thr carrier. General measures are reasonable:

- avoid smoking,
- maintain mobility and healthy weight,
- manage malignancy and cardiovascular risk factors,
- use ordinary perioperative and hospitalization VTE-risk assessment,
- discuss estrogen-containing therapy or pregnancy risk based on personal/family thrombosis history rather than PLG status alone.

### Secondary prevention

- Confirm an abnormal activity result with antigen and repeat testing.
- Evaluate unexplained thrombosis for conventional inherited and acquired causes.
- Consider targeted family testing only when results have clear counseling or clinical value.
- No newborn, general-population, or periodic imaging screening is recommended.

### Tertiary prevention

- Standard secondary prevention after VTE or stroke.
- Rehabilitation after neurologic or limb ischemia as clinically indicated.
- Control concurrent APS, cancer, cardiac sources, PNH, or other thrombophilia.
- Educate patients regarding DVT, PE, and stroke warning symptoms.

### Reproductive counseling

Autosomal transmission should be explained, including the difference between:

1. inheritance of a low-activity laboratory phenotype, and
2. uncertain/low penetrance for clinical thrombosis.

Prenatal and preimplantation testing are technically possible after identifying familial variants, but the poor genotype–clinical phenotype correlation must be made explicit.

No immunization, antimicrobial prophylaxis, environmental remediation, or disease-specific public-health program is applicable.

---

## 14. Other species and naturally occurring disease

| Species | Taxonomy/gene | Natural disease and relevance |
|---|---|---|
| Human, *Homo sapiens* | NCBI Taxon **9606**; *PLG* Gene **5340** | Dysplasminogenemia/type II deficiency |
| Dog, *Canis lupus familiaris* | NCBI Taxon **9615**; canine *PLG* | Naturally occurring **type I-like plasminogen deficiency/ligneous membranitis**, OMIA **002020-9615**, reported in Scottish Terriers, Maltese dogs, Yorkshire Terriers, Golden Retrievers, and Doberman Pinschers. This is comparative PLG deficiency, not confirmed natural dysplasminogenemia. [152][157] |
| Mouse, *Mus musculus* | Taxon **10090**; *Plg* NCBI Gene **18815**, MGI:97620 | Engineered knockout and Tochigi knock-in models; no established naturally occurring breed disease [141] |
| Rat, *Rattus norvegicus* | Taxon **10116**; *Plg* NCBI Gene **85253** | Ortholog available; no well-established natural dysplasminogenemia syndrome [138] |

In Scottish Terriers, homozygous canine *PLG* c.1256+2T>A causes complete loss of activity and ligneous membranitis. A Maltese dog was reported with a large *PLG* deletion. These diseases resemble human type I deficiency and demonstrate evolutionary conservation of plasmin-dependent mucosal fibrin clearance. [152]

No zoonotic transmission or cross-species infectious risk exists.

---

## 15. Model organisms and experimental systems

### 15.1 p.Ala620Thr/Tochigi knock-in mouse

The closest disease-specific model is the C57BL/6J mouse carrying homozygous **Plg p.Ala622Thr**, equivalent to human p.Ala620Thr.

| Model feature | Result |
|---|---|
| Plasmin activity after uPA activation | **8.1 ± 4.1%** of wild type |
| Plasminogen antigen | Approximately **48%** of wild type |
| In-vitro clot lysis | Markedly delayed; half-maximal lysis at approximately 80 versus 20 minutes |
| Growth/fertility | Normal |
| Ligneous conjunctivitis | Absent |
| Electrolytic DVT model | No significant difference in thrombus weight |
| Tissue-factor PE model | No significant survival difference; HR 1.18, 95% CI 0.40–3.50 |
| Ischemic-stroke model | No difference in infarct volume or edema |
| Skin wound healing | Essentially normal |
| Combined *Pros1* K196E thrombophilia | Tochigi allele did not worsen PE survival |

The authors concluded:

> “Although mice with the *Plg* T/T mutation showed reduced plasmin activity (~8%) and slower fibrin clot lysis, they showed thrombotic phenotypes largely similar to those of the wild-type mice.”

Tashima et al., published July 7, 2017, *PLOS ONE* 12:e0180981, PMID **29040284**, DOI [10.1371/journal.pone.0180981](https://doi.org/10.1371/journal.pone.0180981). [124][381]

**Strength:** directly models the common human allele and separates biochemical dysfunction from clinical thrombosis.

**Limitations:** artificial acute thrombosis models, one mouse background, no analysis of all environmental triggers, and incomplete validation that each model was sensitive to plasminogen function.

### 15.2 *Plg* knockout mice

*Plg*−/− mice model severe quantitative deficiency, not type II dysplasminogenemia. They exhibit:

- ligneous conjunctivitis,
- widespread fibrin deposition,
- impaired growth and survival,
- delayed skin/corneal wound healing,
- otitis media and periodontitis,
- impaired tissue remodeling.

The knockout generated by Bugge et al. is supported by PMID **7705657**; ligneous conjunctivitis was demonstrated in PMID **9473227**. [170] Removal or reduction of fibrinogen rescues several abnormalities, providing strong causal evidence that persistent fibrin is a major downstream lesion.

### 15.3 In-vitro systems

Available systems include:

- purified normal and variant plasminogen,
- streptokinase/uPA/tPA activation assays,
- chromogenic plasmin-substrate assays,
- plasma clot-lysis assays,
- recombinant missense-protein expression,
- structural modeling using X-ray and cryo-EM plasminogen structures.

These are useful for determining whether a variant impairs secretion, activation, substrate binding, or catalysis but cannot alone establish thrombotic penetrance.

No validated zebrafish, Drosophila, *C. elegans*, organoid, or human iPSC disease model specific to dysplasminogenemia was identified.

---

## Recent developments and expert interpretation

### 2023

Chen et al. reported three Chinese pedigrees in which adolescent/young-adult cerebral infarction probands and several relatives carried heterozygous p.Ala620Thr with approximately 50–65% activity. The authors proposed increased cerebral-infarction risk but acknowledged the sample size was small and that larger controlled studies were required. Published March 30, 2023; PMID **37065478**; DOI [10.3389/fgene.2023.1132654](https://doi.org/10.3389/fgene.2023.1132654). [32]

### 2024

The comprehensive 2024 review integrated structural, population, clinical, and animal evidence and concluded that dysplasminogenemias “may not necessarily lead to disease or thrombotic risk,” while allowing that other genetic or environmental challenges could reveal reduced fibrinolytic reserve. It also emphasized that routine genetic determination of *PLG* polymorphisms is not currently recommended for estimating venous or arterial thrombosis risk. PMID **38984351**. [37]

### 2025–2026 update

- A December 2025 report identified compound-heterozygous **p.Gly568Arg/p.Ala620Thr** in a patient with activity 27% and antigen 103%, expanding the molecular spectrum. PMID **41398600**. [18]
- A March 2026 retrospective series selected 18 cerebral-infarction patients with low PLG activity and identified p.Ala620Thr, p.His133Arg, p.Gly703Asp, and p.Gly568Arg. All had activity 19–67%. Because every participant was selected for both infarction and low activity, a controlled prospective study is still needed before concluding that these variants significantly increase population risk. PMID **41778291**. [21]

---

## Evidence-weighted knowledge-base conclusions

1. **Definitive disease–gene relationship:** dysplasminogenemia is a qualitative plasminogen abnormality caused by germline ***PLG*** variants.
2. **Definitive biochemical phenotype:** low functional plasminogen activity with normal or mildly reduced antigen.
3. **Best-established molecular lesion:** p.Ala620Thr impairs the plasmin catalytic site and markedly reduces activity.
4. **Usual clinical phenotype:** asymptomatic.
5. **Mucosal ligneous disease:** not characteristic of type II; its presence should trigger evaluation for type I deficiency.
6. **Thrombosis association:** biologically plausible but not established as an independent effect for common p.Ala620Thr; individual cases and selected stroke series conflict with family, population, ClinVar, and animal-model evidence.
7. **Inheritance:** autosomal codominant biochemical expression with very low/uncertain clinical penetrance; the blanket “autosomal recessive” label reflects ontology conflation with type I deficiency.
8. **Diagnosis:** paired plasminogen activity and antigen measurements, exclusion of acquired causes, then targeted *PLG* sequencing when useful.
9. **Treatment:** none for an asymptomatic laboratory phenotype; treat actual thrombosis by standard site-specific protocols.
10. **Prognosis:** generally normal, with no demonstrated reduction in life expectancy from isolated dysplasminogenemia.
11. **Research need:** large unselected prospective cohorts with standardized tPA/uPA-based functional assays, matched controls, complete sequencing, and systematic measurement of conventional thrombotic modifiers.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 13 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100538` (5 mentions) - the report calls it "Mondo"; MONDO calls it **dysplasminogenemia**
- `DOID:0111592` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **plasminogen deficiency type I**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (2 mentions) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004252` (1 mention) - the report calls it "Serine-type endopeptidase activity—active plasmin"; GO calls it **serine-type endopeptidase activity**
- `GO:0005615` (2 mentions) - the report calls it "Extracellular space", "Blood plasma/extracellular space"; GO calls it **obsolete extracellular space**
- `GO:0072378` (1 mention) - the report calls it "Blood coagulation, fibrin-clot formation—upstream substrate-generating process"; GO calls it **blood coagulation, fibrin clot formation**
- `CL:0000182` (2 mentions) - the report calls it "Hepatocyte source", "Hepatocyte"; CL calls it **hepatocyte**
- `CL:0000071` (2 mentions) - the report calls it "Blood-vessel endothelial cell/clot surface", "Blood-vessel endothelial cell"; CL calls it **blood vessel endothelial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005615` - called "Extracellular space", "Blood plasma/extracellular space"
- `CL:0000182` - called "Hepatocyte source", "Hepatocyte"
- `CL:0000071` - called "Blood-vessel endothelial cell/clot surface", "Blood-vessel endothelial cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.