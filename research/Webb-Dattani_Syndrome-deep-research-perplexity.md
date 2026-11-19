---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-30T11:05:50.879908'
end_time: '2026-10-30T11:11:12.454223'
duration_seconds: 321.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Webb-Dattani Syndrome
  mondo_id: MONDO:0014404
  category: Mendelian
  causal_genes: ARNT2
  omim_id: OMIM:615926
  synonyms: hypothalamic insufficiency-secondary microcephaly-visual impairment-urinary
    anomalies syndrome
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 54
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 52
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014404
    reported_labels:
    - MONDO
    ontology_label: Webb-Dattani syndrome
  - term_id: GO:0005634
    reported_labels:
    - Nucleus
    - ARNT2 acts in the nucleus/nucleoplasm
    ontology_label: nucleus
  labels_variant: 2
  unresolvable_prefixes:
  - Gene
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Webb-Dattani Syndrome
- **MONDO ID:** MONDO:0014404 (if available)
- **Causal gene(s):** ARNT2
- **OMIM:** OMIM:615926
- **Synonyms:** hypothalamic insufficiency-secondary microcephaly-visual impairment-urinary anomalies syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Webb-Dattani Syndrome** covering all of the
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

# Webb–Dattani syndrome: comprehensive disease-characteristics report

**Webb–Dattani syndrome (WEDAS) is a severe autosomal-recessive neurodevelopmental–neuroendocrine disorder caused by biallelic pathogenic variants in *ARNT2* (aryl hydrocarbon receptor nuclear translocator 2; HGNC:16876; NCBI Gene:9915; OMIM gene:606036).** Its defining combination is congenital hypothalamic–pituitary insufficiency—particularly arginine-vasopressin deficiency—followed by secondary microcephaly, profound developmental impairment, seizures and spasticity, post-retinal/cortical visual impairment, and renal/urinary-tract abnormalities. The landmark report described six affected children from a highly consanguineous Saudi family and demonstrated near-absence of *ARNT2* transcript and protein from a homozygous frameshift variant, establishing loss of function as the disease mechanism (PMID:24022475; published September 10, 2013; DOI: https://doi.org/10.1093/brain/awt218). [1]

**Evidence status.** WEDAS remains exceptionally rare. Most quantitative estimates below come from the original six-person family rather than a population cohort; they must not be interpreted as stable population frequencies. Later reports include three affected siblings, twin girls, two individuals in an autozygome study, a single ClinVar VUS case, and a likely longitudinal report of an adolescent from the extended Saudi kindred. Duplication between some reports cannot be excluded.

---

## 1. Disease information

### Definition and identifiers

| Field | Entry |
|---|---|
| Preferred name | Webb–Dattani syndrome |
| Abbreviation | WEDAS |
| MONDO | **MONDO:0014404** |
| OMIM phenotype | **615926** |
| OMIM gene | *ARNT2*, **606036** |
| Orphanet | **ORPHA:370006**, listed in the OMIM clinical synopsis [98] |
| MedGen | **C4014708**, UID 863145 [106] |
| Causal gene | ***ARNT2*** |
| Chromosomal locus | 15q25.1 |
| Inheritance | Autosomal recessive |
| Common synonym | Hypothalamo-pituitary-frontotemporal hypoplasia with visual and renal anomalies |
| User-supplied synonym | Hypothalamic insufficiency–secondary microcephaly–visual impairment–urinary anomalies syndrome |
| ICD-10/ICD-11 | No dedicated disease-specific code identified. Broad coding may use a congenital-malformation syndrome category such as ICD-10 Q87.8 and separate endocrine, neurologic and renal manifestation codes; E23.0 can represent hypopituitarism. |
| MeSH | No dedicated WEDAS descriptor identified. **D007018** denotes hypopituitarism, not WEDAS itself. [256] |

The NIH Genetic Testing Registry summarizes the condition as frontotemporal hypoplasia, global developmental delay, and pituitary/hypothalamic insufficiency, with neonatal hormone deficiencies followed by microcephaly, seizures, spasticity, post-retinal blindness and renal abnormalities. [107]

### Nature of the evidence

The knowledge base is assembled from:

1. **Individual-patient/family clinical reports**, including endocrine laboratory data, MRI, electrodiagnostic vision studies and renal imaging.
2. **Aggregated disease resources**, principally OMIM, MedGen, MONDO, GTR, ClinVar and Orphanet.
3. **Experimental evidence**, including patient fibroblast RNA/protein studies, human embryonic expression analysis, and *Arnt2*-deficient mouse and zebrafish studies.

No EHR-derived population cohort, formal natural-history registry, randomized trial or disease-specific quality-of-life study was found.

---

## 2. Etiology

### Primary cause

WEDAS is caused by **biallelic germline loss-of-function or probable loss-of-function variants in *ARNT2***. The best-established variant is the homozygous two-base duplication originally reported as NM_014862.3:c.1373_1374dupTC, p.(Tyr459ArgfsTer52). On the current NM_014862.4 transcript ClinVar represents it as c.1372_1373dup, p.Tyr459fs, Variation ID 805850, classified pathogenic for WEDAS. [76]

The original variant:

- segregated with disease in the extended family;
- was heterozygous in unaffected parents;
- was absent from dbSNP, ESP6500, 172 internal exomes and 200 ethnically matched controls;
- produced a 50–150-fold reduction in patient-fibroblast *ARNT2* RNA and greatly reduced/undetectable ARNT2 protein, consistent with nonsense-mediated decay. [1]

### Risk factors

| Risk factor | Evidence and interpretation |
|---|---|
| Two pathogenic *ARNT2* alleles | Necessary Mendelian cause in confirmed WEDAS. |
| Parental consanguinity | Strongly represented in reported Saudi families and increases the probability that both parents carry the same rare allele. It is not itself a biological cause. |
| Family history | An affected sibling or known familial *ARNT2* variant indicates substantial recurrence risk. |
| Saudi Arabian ancestry | Most early cases were Saudi, and one splice allele was described as a shared founder allele. This may reflect founder effects and ascertainment rather than ancestry-specific biology. [193][1] |
| Sex | No evidence of sex-dependent risk; both sexes are affected. |
| Maternal age, paternal age, lifestyle or exposure | No demonstrated association. |

For two carrier parents, the theoretical risk at each conception is **25% affected, 50% heterozygous carrier and 25% unaffected non-carrier**.

### Protective factors and gene–environment interaction

No genetic protective allele, validated modifier gene, diet, medication, lifestyle or exposure that prevents WEDAS has been identified. Environmental factors can, however, markedly modify **outcome**:

- inadequate water access or desmopressin interruption can exacerbate hypernatremia;
- intercurrent infection can precipitate adrenal crisis, dehydration or death;
- delayed hormone replacement can worsen endocrine complications.

These are disease-management interactions, not evidence that environment initiates WEDAS. No formal ARNT2-specific gene–environment study was found.

---

## 3. Phenotypes

### Core phenotype and observed frequencies

The following frequencies are primarily from the original six affected children and therefore have wide uncertainty.

| Phenotype; suggested HPO | Type | Onset/course | Observed frequency and severity | Functional/QOL impact |
|---|---|---|---|---|
| Central diabetes insipidus/AVP deficiency; **HP:0000863** | Endocrine sign/laboratory abnormality | Neonatal, presentation at 2–10 days; lifelong | 6/6; severe hypernatremia, sodium 145–172 mmol/L | Requires lifelong desmopressin, prescribed water and frequent sodium monitoring; adipsia increases risk |
| ACTH deficiency/central adrenal insufficiency; HP:0011748 / HP:0000846 | Endocrine/laboratory | Neonatal | 6/6 were described with cortisol insufficiency | Risk of hypotension, adrenal crisis and death during illness |
| Central hypothyroidism; HP:0011784 | Endocrine/laboratory | Infancy/childhood | 4/6 in original series | Untreated deficiency aggravates growth and neurodevelopment |
| GH deficiency or abnormal GH secretion; **HP:0000824** | Endocrine/laboratory | Early childhood | Definitively tested in two; abnormal growth patterns in 4/6 | Short stature, delayed bone age, reduced bone health |
| Hypogonadotropic hypogonadism/delayed puberty; HP:0000044 / HP:0000823 | Endocrine | Congenital axis defect, clinically evident at puberty | Male cryptorchidism in the original cohort; absent puberty documented in the adolescent follow-up | Sexual development, fertility and bone-mass consequences |
| Postnatal microcephaly; **HP:0005484** | Physical sign | Acquired/progressive after initially normal head size | 6/6; reported head-circumference SDS −3.4 to −6.4 | Marker of severe impaired brain growth [303] |
| Severe global developmental delay; **HP:0001263** | Neurodevelopmental | Infancy; chronic | 6/6 | Profound dependence for mobility, communication and activities of daily living |
| Seizures; HP:0001250 | Neurologic sign | 8 days–1 year in original cohort; persistent/variable control | 6/6 | Hospitalization, injury risk and medication burden |
| Spastic tetraplegia/quadriplegic cerebral palsy; **HP:0002510** | Motor sign | Childhood, progressive emergence | 6/6; GMFCS grade V | Non-ambulatory status, contractures, hip displacement, complete caregiving dependence |
| Cortical/post-retinal visual impairment; HP:0100704 | Sensory sign | Congenital/infancy | 6/6; absent response to light despite normal globes/fundi | Severe blindness affecting development and communication |
| Frontotemporal hypoplasia/cerebral atrophy | MRI sign | Acquired postnatally | 6/6 in original report | Correlates with developmental and motor disability |
| Delayed CNS myelination; **HP:0002188** or HP:0012448 | MRI sign | Postnatal; persistent | 6/6 in original MRI pattern | Likely contributes to motor and cognitive impairment [308] |
| Thin corpus callosum; HP:0033725 | MRI sign | Childhood MRI | Common/6-person pattern | Interhemispheric white-matter abnormality |
| Hypoplastic anterior pituitary; HP:0012506 | MRI sign | Congenital | 6/6 | Structural correlate of pituitary deficiency |
| Thin/absent pituitary stalk; HP:0001498 | MRI sign | Congenital | 6/6 | Supports congenital hypothalamo-pituitary disorder |
| Absent posterior pituitary bright spot | MRI sign | Congenital | 6/6 | Supports AVP-axis disruption |
| Vesicoureteral reflux; HP:0000076 | Renal/urinary sign | Congenital/infancy | 6/6, often grades III–V | UTI and renal-damage risk |
| Hydronephrosis; HP:0000126 | Renal imaging sign | Congenital/infancy | 6/6, usually bilateral | Requires nephrology/urology surveillance |
| Neurogenic bladder; HP:0000011 | Urologic sign | Infancy/childhood | 6/6 in original report | Retention/incontinence, catheterization and infection risk |
| Severe gastroesophageal reflux; HP:0002020 | Gastrointestinal | Infancy | 6/6; surgery in 3/6 | Feeding difficulty, aspiration and hospitalization |
| Hip dysplasia/dislocation; HP:0001385 | Musculoskeletal | Before age 1 in severe cases | Radiographic dislocation in 4/6 | Pain, positioning and care difficulties |
| Central hypotonia/hypoventilation | Neuromuscular/respiratory | Congenital, prominent in second family | 3 affected siblings reported | Respiratory support and infection risk |
| Dysmorphism | Physical manifestation | Congenital | Original family: prominent forehead, deep-set eyes, grooved philtrum, retrognathia | Primarily diagnostic; feeding/airway relevance possible |

The original report states:

> “MRI of the brain revealed a strikingly similar pattern of abnormalities in all children,” including an absent posterior pituitary bright spot, thin stalk, hypoplastic anterior pituitary, frontotemporal hypoplasia, thin corpus callosum and delayed myelination.

It also reports:

> “All children demonstrated no clinical response to light with minimal pupil responses. Ophthalmic examination of the globe and fundi were normal.”

Electroretinograms showed generalized retinal activation, whereas visual-evoked potentials were attenuated or asymmetric, localizing major dysfunction to post-retinal pathways (PMID:24022475). [1]

### Quality of life

No EQ-5D, SF-36, PROMIS or disease-specific patient-reported outcome data exist. Clinical severity implies profound effects: blindness, GMFCS-V motor disability, severe intellectual/developmental impairment, recurrent endocrine emergencies, seizures, bladder care and continuous caregiver supervision.

---

## 4. Genetic and molecular information

### Gene and protein

| Attribute | Information |
|---|---|
| Gene | *ARNT2* |
| HGNC | HGNC:16876 |
| NCBI Gene | 9915 |
| Ensembl | ENSG00000172379 |
| OMIM | 606036 |
| Location | 15q25.1 |
| UniProt | Q9HBZ2 |
| Protein class | Nuclear basic helix–loop–helix–PAS transcription factor |
| Principal domains | bHLH residues 63–116; PAS1 134–209; PAS2 323–393; PAC 398–441 [64] |
| Major developmental partner | SIM1 |
| Principal compartment | Nucleus; **GO:0005634** |
| Expression | Predominantly CNS, with relevant expression in hypothalamus, pituitary, retina and renal tubules; Human Protein Atlas describes nuclear expression most abundant in CNS. [62] |

### Disease-associated or potentially relevant variants

| Variant | Type/status | Human evidence | Population/functional evidence |
|---|---|---|---|
| NM_014862.3:c.1373_1374dupTC, p.(Tyr459ArgfsTer52); current transcript c.1372_1373dup | Homozygous frameshift; pathogenic | Six affected relatives; complete segregation | Absent from historical controls; marked RNA/protein loss and NMD; ClinVar VCV000805850 [76][78] |
| NM_014862.3:c.378C>T, p.(Gly126=) | Synonymous, predicted cryptic splice donor; originally “unclear variant” | Homozygous in affected twins from a three-sibling family | In-silico splice prediction only; no RNA confirmation reported [42] |
| NM_014862.3:c.147-1G>A | Canonical splice acceptor; pathogenic in research study, ACMG PVS1/PM2/PP3 | Homozygous in two patients/siblings with microcephaly, developmental delay, poor vision and pituitary MRI abnormalities | Described as a founder allele; rare/absent in internal and gnomAD filters [25] |
| NM_014862.4:c.726-3T>G | Intronic; ClinVar VUS | One homozygous affected individual; parents heterozygous | Absent from gnomAD; predicted cryptic splice activation, but no functional RNA study; ClinVar last updated June 23, 2024 [77] |
| NM_014862.4:c.835del, p.(Val279TrpfsTer16) | Frameshift; ClinVar pathogenic | Not reported in a clinically characterized WEDAS patient | Absent from gnomAD; predicted LoF, no variant-specific functional evidence [80] |

All reported constitutional WEDAS variants are **germline**, not somatic.

### Functional consequence

The established mechanism is **biallelic loss of function**. Gain of function and dominant-negative mechanisms have not been demonstrated for classic WEDAS. Heterozygous *ARNT2* variants have been investigated in obesity or neurodevelopmental phenotypes, but those associations should not be merged with recessive WEDAS.

### Modifier, epigenetic and chromosomal information

- No validated modifier gene or severity-modifying allele is known.
- No WEDAS-specific episignature has been established.
- Experimental neuronal differentiation work indicates that the *Arnt2* promoter can transition from bivalent H3K4me3/H3K27me3 chromatin to loss of repressive H3K27me3, but this is regulatory biology, not a demonstrated disease-causing epimutation. [377]
- No recurrent deletion, translocation, inversion or aneuploidy uniquely defining WEDAS has been reported. CNV analysis is still appropriate when sequence analysis is negative.

---

## 5. Environmental, lifestyle and infectious information

There is no evidence that toxins, radiation, pollution, diet, smoking, alcohol, occupational exposure or an infectious agent causes WEDAS. It is a constitutional Mendelian developmental disorder.

Infections are clinically important **complications**. Three children in the original report died from sepsis, and respiratory infections contributed to morbidity and death in the adolescent follow-up. Infections also increase cortisol requirements and fluid losses and therefore can precipitate adrenal or hypernatremic crises. [1]

No zoonotic, contagious or transmissible infectious component applies.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function *ARNT2* variants lead to** frameshift/premature termination or abnormal splicing.
2. **Premature termination leads to** nonsense-mediated RNA decay and markedly reduced ARNT2 protein; this was directly demonstrated for c.1373_1374dupTC.
3. **Loss of nuclear ARNT2 leads to** failure of normal bHLH-PAS heterodimeric transcription, particularly SIM1–ARNT2 activity.
4. **Reduced SIM1–ARNT2 transcription leads to** defective terminal differentiation of hypothalamic paraventricular and supraoptic neurosecretory neurons; this is strongly demonstrated in mice and inferred in humans.
5. **Defective AVP-neuron differentiation leads to** arginine-vasopressin deficiency, polyuria, hyperosmolarity and severe hypernatremia, compounded by probable impaired thirst regulation.
6. **Defective CRH/TRH/somatostatin neuroendocrine programs lead to** ACTH/cortisol, TSH/thyroxine and GH-axis deficiencies; gonadotropin deficiency is additionally documented clinically.
7. **Branch A—impaired CNS development and postnatal maintenance leads to** frontotemporal hypoplasia, delayed myelination and thin corpus callosum, which result in secondary microcephaly, profound developmental delay, seizures and spastic quadriplegia.
8. **Branch B—abnormal visual-pathway development leads to** post-retinal/chiasmal/cortical dysfunction, resulting in severe visual impairment despite relatively preserved retinal responses.
9. **Branch C—ARNT2 loss in developing kidney/urinary tissues and/or neurogenic bladder circuitry leads to** vesicoureteral reflux and hydronephrosis; the exact direct-versus-neurogenic contribution is inferred.
10. **Combined endocrine, neurologic, respiratory, feeding and urinary dysfunction leads to** recurrent hypernatremia, aspiration/infection, sepsis and premature mortality.

### Molecular and cellular details

ARNT2 is a DNA-binding transcriptional partner for class-I bHLH-PAS proteins. Its bHLH domain supports DNA binding/dimerization, and its PAS domains mediate partner interactions. NCBI describes ARNT2 heterodimers as binding regulatory sequences in genes responsive to developmental and environmental stimuli. [69]

The central developmental partner is **SIM1**. In *Arnt2*-null mice, paraventricular and supraoptic nuclei are hypocellular and lack terminally differentiated neurons expressing:

- arginine vasopressin;
- oxytocin;
- corticotropin-releasing hormone;
- thyrotropin-releasing hormone;
- somatostatin.

The primary mouse paper reported:

> “Heterozygous Arnt2 mice were viable, but homozygous Arnt2 gene knockout mice died shortly after birth,” and AVP-, oxytocin-, CRH- and somatostatin-expressing neurons were absent.

(PMID:11318878; April 2001; DOI: https://doi.org/10.1046/j.1365-2443.2001.00421.x). [54]

### Cell types, processes and ontology suggestions

| Mechanistic element | Suggested ontology |
|---|---|
| Neuroendocrine/neurosecretory cell | **CL:0000165** |
| Magnocellular neurosecretory cell | **CL:0011003** [316] |
| AVP-producing magnocellular neuron | CL:0011003 with AVP marker annotation |
| CRH/TRH/somatostatin parvocellular neurons | Neuroendocrine cell, CL:0000165; more specific terms where available |
| Neuron differentiation | **GO:0030182** |
| Neuron development | **GO:0048666** |
| Neuroendocrine-cell differentiation | GO:0061101, noting that QuickGO currently marks this term obsolete; use a current replacement during production curation. [336] |
| DNA-binding transcription-factor activity | GO:0003700 |
| Positive regulation of DNA-templated transcription | GO:0045893 |
| Nucleus | **GO:0005634** |
| CNS development | GO:0007417 |
| Myelination | GO:0042552 |
| Kidney development | GO:0001822 |
| Collecting-duct development | **GO:0072044** [342] |

### Metabolism, immunity and tissue injury

- There is no primary enzyme deficiency or characteristic human metabolomic signature.
- The original patients had normal amino acids, acylcarnitines, lactate and ammonia and normal muscle biopsy, arguing against a primary mitochondrial/metabolic disease.
- Immune testing in two original patients was normal; no primary immunodeficiency or autoimmune mechanism is established.
- Tissue injury is mainly developmental and secondary: reflux nephropathy risk, hypoxic/aspiration injury, seizure-related injury, and dehydration/hypernatremia.

### Molecular profiling and advanced technologies

No WEDAS-specific patient single-cell atlas, spatial transcriptomic study, proteomic, metabolomic, lipidomic, CRISPR screen, organoid or multi-omics study was found. Patient fibroblast RT-qPCR and Western blot remain the principal human functional assays. A heterozygous-*ARNT2* obesity iPSC line exists, but it is not a biallelic WEDAS model. [386]

---

## 7. Anatomical structures affected

| Level | Structures | Suggested ontology |
|---|---|---|
| Primary organ/system | Hypothalamus and hypothalamo-pituitary axis | Hypothalamus **UBERON:0001898**; pituitary gland UBERON:0000007 |
| Hypothalamic nuclei | Paraventricular and supraoptic nuclei | Use specific UBERON/brain-region terms in the production ontology |
| Pituitary | Anterior pituitary, posterior pituitary and stalk | Adenohypophysis UBERON:0002196; neurohypophysis UBERON:0002198 |
| Cerebrum | Frontal and temporal lobes, motor and occipital cortex, corpus callosum and white matter | Cerebral cortex UBERON:0000956; corpus callosum UBERON:0002336 |
| Visual system | Optic chiasm/post-retinal pathway, lateral geniculate and occipital cortex | Visual-system and regional UBERON terms |
| Renal/urinary | Kidney, renal tubules/collecting system, ureters and bladder | Kidney **UBERON:0002113**; nephron tubule UBERON:0001231; collecting system UBERON:0004100; urinary bladder **UBERON:0001255** [317][319] |
| Musculoskeletal | Hips and limbs secondarily affected by severe spasticity | Hip joint UBERON:0001463 |
| Gastrointestinal | Esophagus/stomach junction affected by reflux | Esophagus UBERON:0001043 |
| Subcellular | ARNT2 acts in the nucleus/nucleoplasm | GO:0005634 |

Visual impairment is generally bilateral. Hydronephrosis and reflux are often bilateral but can be asymmetric. No consistent cerebral lateralization has been reported.

---

## 8. Temporal development and natural history

### Typical course

1. **Prenatal/congenital phase:** abnormal hypothalamic–pituitary, visual and urinary development begins embryonically.
2. **Neonatal presentation:** hypernatremia from AVP deficiency, low cortisol and other pituitary deficits, often within days to three months.
3. **Infancy:** developmental delay, hypotonia, visual non-responsiveness, seizures, reflux and urinary abnormalities become evident.
4. **Early childhood:** acquired severe microcephaly, frontotemporal hypoplasia, delayed myelination and spastic quadriplegia emerge or progress.
5. **Later childhood/adolescence:** chronic endocrine replacement, absent/delayed puberty, recurrent hypernatremia, respiratory or urinary infections and severe lifelong disability.

In one original child, neonatal MRI was normal except for the pituitary axis, while MRI at 18 months showed frontotemporal hypoplasia and delayed myelination. This provides direct evidence that part of the cerebral phenotype is **postnatal and progressive**, rather than entirely prenatal. [1]

There is no spontaneous remission. Hormone deficiencies are chronic and may become more apparent over time. Early diagnosis is critical because untreated cortisol and AVP deficiencies are immediately life-threatening, while prompt therapy may prevent avoidable endocrine injury but cannot reverse established developmental brain malformations.

---

## 9. Inheritance and population characteristics

### Epidemiology

No reliable prevalence per 100,000, annual incidence or carrier-frequency estimate exists. The exact prevalence remains unknown because only a small number of families have been published. [184]

### Inheritance features

| Feature | Current interpretation |
|---|---|
| Mode | Autosomal recessive |
| Penetrance | Apparently high for individuals with confirmed biallelic severe LoF variants, but sample size is too small for a numerical estimate |
| Expressivity | Variable in endocrine profile, renal severity, respiratory involvement and survival |
| Anticipation | Not expected and not reported |
| Germline mosaicism | Not reported; generally less relevant where both parents are confirmed heterozygous carriers |
| Founder effect | Plausible for Saudi variants, particularly c.147-1G>A based on shared haplotype [25] |
| Consanguinity | Prominent in reported families |
| Geographic distribution | Published cases predominantly involve Saudi Arabian ancestry; this is not proof that disease is absent elsewhere |
| Sex ratio | Both sexes affected; original family had five females and one male, too few to infer a true ratio |
| Carrier phenotype | Heterozygous parents in the original family were unaffected |

No validated ethnicity-specific carrier frequency is available from gnomAD. The disorder is likely underdiagnosed in individuals categorized more broadly as congenital hypopituitarism, septo-optic dysplasia or severe neurodevelopmental disease.

---

## 10. Diagnostics

### Clinical suspicion

Consider WEDAS when an infant has:

- hypernatremia with inappropriately dilute urine and AVP deficiency;
- low cortisol and one or more additional pituitary deficiencies;
- small anterior pituitary, thin/absent stalk or absent posterior bright spot;
- acquired microcephaly, severe developmental delay, seizures or spasticity;
- cortical/post-retinal blindness with a relatively normal eye and retina;
- vesicoureteral reflux, hydronephrosis or neurogenic bladder.

### Recommended investigations

| Domain | Tests and expected findings |
|---|---|
| Fluid balance | Paired serum sodium/osmolality and urine osmolality; hyperosmolar plasma with inappropriately dilute urine; response to desmopressin |
| Adrenal axis | 08:00 cortisol and ACTH; ACTH stimulation when safe/needed |
| Thyroid axis | Free T4 with TSH; central disease may show low free T4 without appropriately elevated TSH |
| Growth axis | Serial length/height and velocity, IGF-1/IGFBP-3; GH stimulation testing if clinically actionable |
| Gonadal axis | LH, FSH, estradiol/testosterone; genital and pubertal assessment |
| Other pituitary tests | Prolactin, glucose and electrolytes |
| MRI | Dedicated hypothalamic–pituitary MRI plus full brain sequences |
| Ophthalmology | Fundoscopy, electroretinogram and visual-evoked potentials |
| Neurology | EEG for seizures; developmental and motor assessments |
| Renal/urology | Renal/bladder ultrasonography, creatinine/eGFR, urinalysis/culture; voiding cystourethrogram when reflux is suspected; bladder-function assessment |
| Musculoskeletal | Hip surveillance in non-ambulant children |
| Respiratory/feeding | Swallow/aspiration and hypoventilation evaluation where indicated |

### Genetic-testing algorithm

1. **First line:** an NGS congenital-hypopituitarism, microcephaly/neurodevelopmental, CAKUT or syndromic visual-impairment panel that includes *ARNT2*, with exon-level deletion/duplication analysis.
2. **Single-gene *ARNT2* testing:** appropriate when the phenotype is highly characteristic or a familial variant is known.
3. **Trio WES/WGS:** preferred when the phenotype is atypical, panel testing is negative, or splice/CNV/noncoding variants are suspected.
4. **RNA analysis:** useful for synonymous or intronic variants such as c.378C>T or c.726-3T>G.
5. **CMA:** useful for broader syndromic differential diagnoses and pathogenic CNVs but will not detect most single-nucleotide/short-indel *ARNT2* variants.
6. **Karyotype/FISH:** low yield unless a chromosomal rearrangement is suspected.
7. **Mitochondrial and repeat-expansion testing:** not routinely indicated by classic WEDAS.

GTR lists four condition-specific molecular tests, including full coding-region sequencing, targeted familial-variant testing and deletion/duplication analysis; 23 tests list *ARNT2* more broadly. [121]

### Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| Septo-optic dysplasia, including *HESX1* | Optic-nerve hypoplasia and absent septum pellucidum are typical; WEDAS often has normal ocular fundi with post-retinal dysfunction, acquired microcephaly and urinary anomalies |
| *SOX2*-related disorder | Anophthalmia/microphthalmia, esophageal and genital anomalies are more characteristic |
| *SOX3*-related hypopituitarism | Usually X-linked; midline brain and intellectual phenotypes without the characteristic WEDAS renal constellation |
| *OTX2* disorder | Eye malformations, pituitary stalk interruption and variable developmental delay |
| *LHX3/LHX4, PROP1, POU1F1* CPHD | Endocrine overlap but typically no severe cortical blindness, acquired microcephaly and high-grade reflux/hydronephrosis combination |
| SIM1-related disease | Obesity and neurobehavioral phenotype, generally dominant and without classic WEDAS multisystem malformations |
| Congenital disorders of glycosylation/mitochondrial disease | May produce multisystem developmental disease but biochemical, imaging and genetic findings differ |

A 2023 Endotext review identifies the characteristic *ARNT2* combination as CPHD with DI, absent posterior bright spot, stalk thinning, hypoplastic anterior pituitary, postnatal microcephaly, frontotemporal hypoplasia, renal anomalies and visual impairment. [286]

### Screening

WEDAS is not part of routine newborn screening. Targeted neonatal testing is warranted in at-risk pregnancies or newborn siblings. Cascade testing should be offered to adult relatives after the familial variant is established.

---

## 11. Outcome and prognosis

No formal 5-year survival, life expectancy or disease-specific mortality rate has been calculated.

In the original 2013 report:

- 3/6 children had died by ages 1.2, 4.2 and 5 years, all from sepsis;
- the oldest living child was approximately 5.3 years at publication;
- all six had profound neurologic and visual disability.

A later report followed a girl with panhypopituitarism, adipsic AVP deficiency, blindness, spastic quadriplegia, neurogenic bladder and a small kidney to age 17. She experienced recurrent hypernatremia and infections and died in August 2024. The authors described this as the longest reported survival at the time (published November 25, 2025; PMID:41363294; DOI: https://doi.org/10.1530/EDM-25-0114). [32]

> “Despite multiple hospitalizations due to complications including hypernatremia and infections, the patient survived into adolescence … before passing away at age 17.”

Major morbidity includes profound developmental disability, non-ambulatory spastic quadriplegia, blindness, refractory seizures, aspiration/reflux, recurrent infections, urinary dysfunction, endocrine crises and delayed puberty. Prognosis probably improves with meticulous hormone replacement, scheduled hydration, infection prevention and multidisciplinary care, but no comparative treated-versus-untreated outcome data exist.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**. Treatment replaces deficient hormones and prevents secondary complications.

| Intervention | Indication/mechanism | Important considerations | Suggested NCIt term |
|---|---|---|---|
| Desmopressin, **CHEBI:4450** | V2-receptor-selective AVP analogue; controls renal free-water loss | Use scheduled fluid intake in adipsia; monitor sodium and weight; excessive drug/water can cause hyponatremia [159][346] | Desmopressin; Hormone Replacement Therapy |
| Prescribed water/fluid regimen | Prevents hypernatremia where thirst is impaired | Caregiver-supervised intake, daily weight and illness plan; fixed dDAVP plus fixed/titrated fluid is recommended for adipsic DI [156] | Fluid Therapy |
| Hydrocortisone | Replaces cortisol in ACTH deficiency | Give before levothyroxine; educate about stress dosing and emergency parenteral steroid | Hydrocortisone; Corticosteroid Therapy |
| Levothyroxine | Replaces thyroid hormone | Dose to free T4 rather than TSH alone; ensure cortisol replacement first | Levothyroxine; Thyroid Hormone Replacement |
| Recombinant GH | Confirmed clinically relevant GH deficiency | Consider after cortisol/thyroid stabilization; no WEDAS-specific response data | Recombinant Human Growth Hormone |
| Estradiol/progestogen or testosterone | Induction/maintenance of puberty in gonadotropin deficiency | Individualize for growth, bone health and family goals | Sex Hormone Replacement Therapy |
| Antiseizure medication | Seizure control | Individualized to seizure type; interactions with steroid metabolism should be reviewed | Anticonvulsant Therapy |
| Physical/occupational therapy | Positioning, mobility, contracture prevention and equipment | Severe GMFCS-V disability generally requires long-term services | Physical Therapy; Occupational Therapy |
| Speech/communication and visual habilitation | Communication and sensory support | Consider augmentative communication and blindness services | Speech Therapy; Rehabilitation Therapy |
| Feeding/reflux management | Nutrition and aspiration prevention | Thickening/tube feeding, acid suppression or fundoplication as clinically indicated | Nutritional Support; Antireflux Surgery |
| Urologic management | Neurogenic bladder, reflux and hydronephrosis | Timed voiding/catheterization, antibiotic treatment or prophylaxis where justified, and corrective surgery in selected cases | Urinary Catheterization; Urologic Surgery |
| Orthopedic management | Hip displacement/contractures | Surveillance, bracing, tone management and surgery as needed | Orthopedic Surgery |

Pediatric adrenal guidance identifies hydrocortisone as the preferred glucocorticoid, commonly around 8–10 mg/m²/day in physiologic replacement, adjusted individually with stress dosing. [166] Hormone replacement should proceed in safety order: **glucocorticoid first, thyroid hormone second, followed by sex hormone and GH when appropriate**, because levothyroxine can precipitate adrenal crisis in untreated cortisol deficiency. [170]

No WEDAS-specific NCT-registered trial, gene therapy, cell therapy, antisense therapy, RNA therapy or approved targeted therapy was identified. No pharmacogenomic guidance specific to *ARNT2* exists.

---

## 13. Prevention

### Primary prevention

The phenotype cannot currently be prevented after conception by vaccination, diet or environmental modification. Reproductive prevention options require identification of the familial pathogenic variant:

- carrier testing for adult at-risk relatives;
- partner testing;
- preimplantation genetic testing for monogenic disease;
- prenatal diagnosis using chorionic villus sampling or amniocentesis;
- donor gametes or other reproductive options.

A GTR-listed *ARNT2* test accepts chorionic villi and amniotic fluid and offers familial-variant/carrier testing. [283]

### Secondary prevention

For an at-risk newborn:

- test immediately for the familial *ARNT2* variant;
- measure sodium, plasma/urine osmolality, glucose, cortisol/ACTH and free T4;
- institute hydrocortisone, desmopressin and controlled fluid therapy promptly when indicated;
- perform early brain/pituitary and renal imaging.

### Tertiary prevention

Preventable complications include:

- adrenal crisis through stress-dose education and emergency hydrocortisone;
- hypernatremia through scheduled fluids, desmopressin adherence, daily weight and sodium monitoring;
- aspiration through feeding assessment;
- renal damage through bladder and reflux management;
- hip dislocation and contractures through surveillance and therapy;
- osteoporosis through puberty induction where appropriate, mobility/positioning, calcium/vitamin D assessment and endocrine optimization.

Routine immunization is appropriate because infection can trigger decompensation, but no WEDAS-specific vaccine exists.

---

## 14. Other species and natural disease

No naturally occurring veterinary syndrome clearly homologous to human WEDAS was identified in OMIA, and there is no zoonotic or cross-species transmission.

| Species | Taxon | Ortholog/resource | Relevance |
|---|---:|---|---|
| Human | NCBI Taxon 9606 | *ARNT2*, NCBI Gene 9915 | Natural disease |
| Mouse | 10090 | *Arnt2*, NCBI Gene 11864; MGI:107188 | Null and hypomorphic experimental models [226] |
| Rat | 10116 | *Arnt2*, NCBI Gene 25243 | Expression and neurobiological studies [208] |
| Zebrafish | 7955 | *arnt2*, NCBI Gene 64277; ZFIN:ZDB-GENE-001207-3 | Conserved hypothalamic/diencephalic development [230] |
| Xenopus tropicalis | 8364 | *arnt2* | Conserved vertebrate ortholog |
| Xenopus laevis | 8355 | *arnt2.L*, *arnt2.S* | Duplicated amphibian orthologs |

Conservation across mouse, rat, zebrafish and frog supports an ancient developmental role for ARNT2 in CNS and neuroendocrine specification. [232]

---

## 15. Model organisms

### Mouse null models

Targeted homozygous *Arnt2* knockout mice die shortly after birth and show defective terminal differentiation of secretory neurons in the paraventricular and supraoptic hypothalamic nuclei. Heterozygotes are viable. These models strongly reproduce the **upstream neuroendocrine developmental mechanism**, but their neonatal lethality prevents modeling the human postnatal microcephaly, seizures, chronic renal phenotype and long-term hormone management. MGI records include *Arnt2*^tm1Yfk^ and *Arnt2*^tm1Mcs^. [46][47]

### Viable hypomorphic mouse

An ENU-derived and CRISPR-recreated *Arnt2* p.Arg74Cys hypomorphic model developed:

- hyperphagia;
- increased adiposity;
- insulin resistance and glucose intolerance;
- diabetes;
- hepatic steatosis.

The mutant protein had reduced transcriptional activity when co-expressed with SIM1 (PMID:30563851; published December 18, 2018; DOI: https://doi.org/10.1242/dmm.035451). [246]

> “The CRISPR/Cas9-targeted (*Arnt2*R74C/R74C) mice demonstrated hyperphagia and increased adiposity as well as hepatic steatosis and abnormalities in glucose homeostasis.”

This model is useful for residual-function and hypothalamic feeding studies but does **not** reproduce the complete human WEDAS phenotype.

### Zebrafish

Zebrafish *arnt2* studies support a conserved role with *sim1a* in the differentiation of diencephalic dopaminergic and neuroendocrine neurons. Zebrafish permit developmental imaging and genetic perturbation but have not yet yielded a validated full WEDAS therapeutic-screening model.

### Cellular models

- Primary fibroblasts from affected individuals demonstrated NMD and loss of protein.
- Reporter assays can quantify SIM1–ARNT2 transcriptional activity.
- No published biallelic WEDAS iPSC-derived hypothalamic-neuron or organoid model was identified.
- A rational future platform would combine CRISPR knock-in of patient alleles with iPSC differentiation into AVP-, CRH- and TRH-lineage hypothalamic neurons, followed by single-cell transcriptomics and rescue with wild-type *ARNT2*.

---

## Recent developments and expert assessment

No disease-specific 2023–2024 clinical trial, natural-history study or mechanistic multi-omics paper was identified. The most relevant developments during that period were:

1. **2023:** Endotext incorporated *ARNT2* into the genetic differential diagnosis of congenital hypopituitarism and highlighted its distinctive DI–microcephaly–visual–renal phenotype. [131][286]
2. **June 23, 2024:** ClinVar updated a homozygous c.726-3T>G case but retained **uncertain significance**, emphasizing the need for RNA validation of noncanonical splice variants. [77]
3. **2024:** Current AVP-deficiency expertise continued to support desmopressin as first-line replacement, with scheduled aquaresis and careful fluid/sodium control to prevent both hypernatremia and hyponatremia. [159]
4. **2025 publication reporting 2021–2024 follow-up:** survival to 17 years showed that prolonged survival is possible with coordinated care, while recurrent hypernatremia and infection remain major hazards. [32]

The strongest expert interpretation is that WEDAS is fundamentally a **developmental transcription-factor loss-of-function syndrome**. Endocrine replacement can substantially reduce preventable mortality, but it does not correct the prenatal/postnatal CNS developmental defect. The highest-priority research needs are an international registry, standardized longitudinal endocrine and neurologic phenotyping, functional assessment of newer splice variants, and patient-derived hypothalamic cellular models.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 52 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014404` (1 mention) - the report calls it "MONDO"; MONDO calls it **Webb-Dattani syndrome**
- `GO:0005634` (3 mentions) - the report calls it "Nucleus", "ARNT2 acts in the nucleus/nucleoplasm"; GO calls it **nucleus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000165` (2 mentions) - the report calls it "Neuroendocrine/neurosecretory cell"; CL calls it **neuroendocrine cell**
- `GO:0007417` (1 mention) - the report calls it "CNS development"; GO calls it **central nervous system development**, and lists "CNS development" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "Nucleus", "ARNT2 acts in the nucleus/nucleoplasm"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Gene`, `ORPHA`, `MGI`.