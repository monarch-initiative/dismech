---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-06T17:44:55.636930'
end_time: '2026-11-06T17:50:50.965996'
duration_seconds: 355.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MARK2-Related Intellectual Developmental Disorder
  mondo_id: MONDO:0979575
  category: Mendelian
  causal_genes: MARK2
  omim_id: OMIM:621285
  synonyms: MRD76; MARK2-related neurodevelopmental disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 18
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 2
  validator_version: 0.5.1
term_validation:
  total_terms: 59
  verified: 57
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 45
  labels_matching: 37
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0000045
    reported_labels:
    - Severe speech and language impairment
    ontology_label: Abnormal scrotum morphology
  - term_id: HP:0000389
    reported_labels:
    - Dysplastic ears
    ontology_label: Chronic otitis media
  - term_id: GO:0045184
    reported_labels:
    - establishment or maintenance of cell polarity
    ontology_label: establishment of protein localization
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MARK2-Related Intellectual Developmental Disorder
- **MONDO ID:** MONDO:0979575 (if available)
- **Causal gene(s):** MARK2
- **OMIM:** OMIM:621285
- **Synonyms:** MRD76; MARK2-related neurodevelopmental disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MARK2-Related Intellectual Developmental Disorder** covering all of the
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

# MARK2-Related Intellectual Developmental Disorder (MRD76)

MARK2-related intellectual developmental disorder, also known as autosomal dominant intellectual developmental disorder-76 (MRD76), is a rare monogenic neurodevelopmental syndrome caused by heterozygous pathogenic variants in the **MARK2** gene, which encodes microtubule affinity–regulating kinase 2, a serine/threonine protein kinase critical for neuronal polarity and microtubule dynamics.[1][6][9][12] Affected individuals present with a highly penetrant combination of developmental delay, intellectual disability, severe speech and language impairment, and a very high prevalence of autism spectrum disorder (ASD), together with variable seizures, motor delay, behavioral disturbances, and distinctive craniofacial features.[1][11][12][16][17] Recent large-scale sequencing studies and detailed clinical–mechanistic investigations have established MARK2 as an ASD and neurodevelopmental disorder (NDD) gene reaching exome-wide significance, and have shown that most pathogenic variants cause partial or complete loss of function that disrupts microtubule organization and downregulates WNT/β‑catenin signaling, leading to early defects in neural progenitor cell polarity, proliferation, and cortical organization.[7][8][9][12] Human induced pluripotent stem cell (iPSC) models, humanized Drosophila lines, and Mark2^+/−^ mice collectively demonstrate that reduced MARK2 activity is sufficient to cause ASD-like behaviors and neuroanatomical abnormalities, while preclinical work suggests that pharmacologic activation of WNT/β‑catenin signaling (for example, by lithium) can partially rescue cellular and behavioral phenotypes, identifying a potential, though still experimental, avenue for targeted therapy.[7][8][9][12][13][15][18]

## 1. Disease Information

### 1.1 Definition and clinical overview

MARK2-related intellectual developmental disorder is a Mendelian neurodevelopmental syndrome defined by the presence of heterozygous germline pathogenic variants in **MARK2** and a characteristic constellation of developmental and behavioral features. The disorder is catalogued in OMIM as **“Intellectual developmental disorder, autosomal dominant 76”** (MRD76; OMIM 621285) and in MedGen and MONDO as a specific autism–intellectual disability phenotype linked to MARK2.[1][11][16][17] MedGen summarizes the condition as an autosomal dominant intellectual developmental disorder characterized by developmental delay, mildly to severely impaired intellectual development with speech and language deficits, and autism, with more variable additional features including seizures, motor delay, behavioral problems, eye abnormalities, and distinctive facial features.[1][11][16][17] Gong and colleagues’ 2024 American Journal of Human Genetics study, which currently constitutes the most comprehensive clinical series, reported 31 individuals with MARK2 variants, of whom 96.8% had ASD, 100% had developmental delay or intellectual disability, 100% had speech and language problems, and a majority had other behavioral and neurologic comorbidities.[12][13][15]

Thus, the disease can be succinctly described as a highly penetrant, autosomal dominant **MARK2-associated neurodevelopmental disorder** that lies within the broader spectrum of syndromic ASD and intellectual disability (ID) syndromes. It is distinct from nonspecific ASD or ID in that it is genetically defined, has recurrent facial features, and is underpinned by a convergent cellular mechanism involving impaired neuronal polarity and WNT/β‑catenin pathway downregulation.[8][9][12] The clinical phenotype appears non-degenerative: the core deficits arise in early childhood and persist, but there is no consistent evidence of progressive neurological decline, in contrast to neurodegenerative tauopathies in which MARK2 is also implicated.[9] Rather, the disorder occupies the category of congenital or early-onset, life-long neurodevelopmental disorders with stable or slowly evolving cognitive and behavioral profiles.

From a nosologic standpoint, the condition belongs to the MONDO and Orphanet classes of rare, monogenic, primarily central nervous system (CNS) disorders with predominant cognitive, language, and behavioral manifestations. In Orphanet, MARK2 is listed as a disease-causing gene for *non-specific syndromic intellectual disability* (ORPHA:528084), reflecting that the clinical picture overlaps with generalized syndromic ID beyond autism-specific features.[3] The evidence base arises largely from aggregated clinical cohorts identified via exome and genome sequencing in tertiary care settings, rather than from population-based epidemiologic data, and thus the current phenotype description reflects those individuals who have come to genetic attention rather than the full spectrum of possible expressivity.[7][8][12][18]

### 1.2 Identifiers, nomenclature, and synonyms

The disease has multiple identifiers across genetic and clinical ontologies that together define its identity and distinguish it from other numerically labeled intellectual developmental disorders. In OMIM it is recorded as **“INTELLECTUAL DEVELOPMENTAL DISORDER, AUTOSOMAL DOMINANT 76; MRD76”** with entry number 621285, and the causal gene is explicitly listed as **MARK2** (MIM 600526).[1][6][11][16][17] MedGen assigns the concept ID **C6012756** for “Intellectual developmental disorder, autosomal dominant 76,” mapping it to OMIM 621285 and to the corresponding MONDO and other ontology entries.[1][11] MONDO uses the identifier **MONDO:0979575** for this disease entity, underlining its ontology-level identity as a *MARK2-related neurodevelopmental disorder*; this MONDO ID is also referenced in ClinVar and other resources.[2][14] Orphanet lists *non-specific syndromic intellectual disability* associated with MARK2 under its disease list with ORPHA number 528084, though the specific MRD76 label is primarily used in OMIM and MedGen.[3]

The common synonyms and alternative names include **MRD76**, **Intellectual developmental disorder, autosomal dominant 76**, **MARK2-related neurodevelopmental disorder**, and **MARK2-related intellectual developmental disorder**.[1][11][17] In some gene-centered databases such as SFARI Gene and GeneGlobe, the gene is listed as “MARK2 (microtubule affinity regulating kinase 2)” with associated disease labels such as “autism spectrum disorder” or “pervasive developmental disorder” rather than the MRD76 code itself, but cross-references to OMIM 621285 and MedGen C6012756 confirm that these refer to the same entity.[8][10] Importantly, this MRD76 designation is specific to MARK2 and should not be confused with other “autosomal dominant intellectual developmental disorder” entries that are numbered differently (for example, MRD64, MRD26) and correspond to distinct genes.

From the standpoint of clinical coding, there is not yet a dedicated ICD-10 or ICD-11 code assigned specifically to MARK2-related intellectual developmental disorder. In practice, affected individuals are likely coded under broader categories such as F84.0 (childhood autism) or F84.5 (Asperger syndrome) for ASD, and F70–F79 series for mild to severe intellectual disabilities in ICD-10, or their ICD-11 equivalents, combined with a secondary genetic diagnosis code if available. MeSH does not currently provide a disease heading specifically for MRD76, but the gene is indexed under *Microtubule-Associated Serine/Threonine Kinase MARK2* and related functional descriptors.[6][9] Thus, precise identification in research and clinical genomics relies predominantly on OMIM, MedGen, MONDO, and gene-centric databases rather than on general clinical coding systems.

### 1.3 Data sources and evidence base

The information currently available on MARK2-related intellectual developmental disorder derives predominantly from aggregated disease-level resources and detailed case series, rather than from broad electronic health record–based datasets. OMIM, MedGen, and Orphanet compile and synthesize data from published case reports, cohort studies, and gene discovery projects to define the clinical spectrum and molecular basis of MRD76.[1][3][11][16][17] ClinVar and related variant databases contribute curated information on specific MARK2 variants submitted by diagnostic laboratories and research groups, including their molecular classification and associated phenotypic terms.[2][14] SFARI Gene summarizes the relevance of MARK2 to ASD based on large-scale exome sequencing studies, particularly the SPARK cohort, and integrates functional data from Gong et al. and other mechanistic studies.[8]

The pivotal primary literature includes several landmark studies. Gong and colleagues’ 2024 American Journal of Human Genetics article “MARK2 variants cause autism spectrum disorder via the downregulation of WNT/β-catenin signaling pathway” provides an extensive clinical, genetic, and mechanistic characterization of 31 individuals with MARK2 variants and establishes lithium-responsive WNT pathway dysregulation as a core pathophysiologic mechanism.[6][12][13][15] A 2026 Human Genetics and Genomics Advances article, “Loss-of-function variants in MARK2 cause neurodevelopmental disorder,” expands the cohort to an additional 11 individuals (for a total of 20 in that study) and uses a humanized Drosophila model to systematically evaluate the functional consequences of eight NDD-linked MARK2 variants.[7][18] More broadly, a 2024 Nature review on the role of MARK2 in the nervous system and cancer synthesizes the kinase’s roles in microtubule-associated protein phosphorylation, WNT, PI3K/AKT/mTOR, and NF‑κB signaling, and links these pathways to both neurodevelopmental and oncologic processes.[9]

These disease definitions and mechanistic insights are thus grounded primarily in human clinical genetics, supported by in vitro cellular models using iPSC-derived neural cells, in vivo mouse and Drosophila models, and bioinformatic analyses of population and case–control sequence datasets.[7][8][9][12][18] There is, at present, no registry-based or population prevalence study dedicated to MARK2-related intellectual developmental disorder, and the frequency estimates, prognosis, and natural history must be inferred from relatively small but deeply characterized cohorts.

## 2. Etiology

### 2.1 Genetic causal factors

The primary causal factor in MARK2-related intellectual developmental disorder is the presence of a heterozygous pathogenic or likely pathogenic variant in **MARK2** (HGNC:3332), which encodes microtubule affinity–regulating kinase 2, a serine/threonine kinase of the PAR-1 family.[1][3][6][8][10] MARK2 is located on chromosome 11q13.1 and produces multiple isoforms that localize to cell membranes and cytoplasmic compartments in epithelial and neuronal cells.[1][3][10] GeneGlobe describes MARK2 as “an important regulator of cell polarity in epithelial and neuronal cells” that “controls the stability of microtubules through phosphorylation and inactivation of several microtubule-associating proteins,” including microtubule-associated proteins MAP2, MAP4, tau, and others.[6][9][10] In humans, germline disease-causing variants in MARK2 lead to MRD76, whereas somatic or expression-level alterations in MARK2 may contribute to cancers and neurodegenerative diseases, underscoring the gene’s pleiotropic importance.[6][9][10]

Clinically ascertained pathogenic variants span multiple classes, including nonsense, frameshift, canonical splice site, multiexon deletions, and missense variants, with truncating and loss-of-function (LoF) alleles predominating. Gong et al. reported that 81% of the MARK2 variants in their 31-individual cohort were LoF variants, and functional assays of the remaining missense variants supported a loss-of-function effect on protein stability or kinase activity.[6][12][13][15] ClinVar lists at least 22 distinct MARK2 variants associated with MRD76 or autism, including early truncating alleles such as p.Arg71Ter, p.Tyr215Ter, p.Tyr267Ter, frameshift variants like p.Ala216fs, p.Phe271fs, p.Gly580fs, p.Cys723fs, and nonsense variants such as p.Gln747Ter, as well as splice alterations like c.337+1G>T, c.1101+5G>A, c.2006+2T>G, and c.1514+2G>T.[2][14] Several of these variants are classified as pathogenic or likely pathogenic by multiple submitters, often with evidence of de novo occurrence and absence from population databases such as gnomAD.[2][12][14]

The emerging consensus from human, mouse, and Drosophila models is that MARK2-related intellectual developmental disorder is predominantly a **haploinsufficiency** or loss-of-function disorder, in which a 50% reduction in normal MARK2 activity disrupts microtubule cytoskeleton organization and WNT/β‑catenin signaling sufficiently to impair neurodevelopment.[7][9][12] In their 2026 Human Genetics and Genomics Advances study, Yang, Shim, Neuhaus and colleagues used a humanized Drosophila model expressing human MARK2 variants and concluded that “MARK2 variants span a range of functional consequences, primarily exhibiting hypomorphic or loss-of-function effects,” and that truncating variants consistently show reduced protein levels and act as LoF alleles.[7][18] Although dominant-negative or gain-of-function mechanisms cannot be entirely excluded for particular missense variants, the weight of current evidence supports a shared pathogenic mechanism rooted in reduced kinase activity or destabilized protein.

In most reported cases, pathogenic variants have occurred de novo in affected individuals, consistent with a severe, early-onset neurodevelopmental phenotype that compromises reproductive fitness. Gong et al. documented multiple de novo truncating and splice variants, including a c.337+1G>T splice-site mutation resulting in exon skipping and a 49 bp deletion of the MARK2 transcript in a patient with MRD76.[2][12] However, the 2026 HGG Advances study identified at least one familial case with vertical transmission, demonstrating that familial autosomal dominant inheritance with variable expressivity is possible when affected individuals survive to reproductive age.[7][18] Thus, the etiologic landscape is currently dominated by rare, high-penetrance germline variants in MARK2 that are either de novo or segregate in small families, defining a classic monogenic Mendelian disorder.

### 2.2 Genetic risk factors and variant spectrum

Within this monogenic framework, the primary genetic risk factor for MARK2-related intellectual developmental disorder is the presence of a pathogenic or likely pathogenic germline variant in MARK2. Large-scale exome sequencing studies in autism have identified MARK2 as a statistically significant ASD risk gene, driven primarily by de novo coding variants. SFARI Gene notes that a two-stage analysis of rare de novo and inherited coding variants in 42,607 ASD cases, including 35,130 from the SPARK cohort, identified MARK2 as a gene reaching exome-wide significance (P < 2.5 × 10^−6), with association primarily driven by de novo variants.[8] Additional de novo missense variants in MARK2 have been reported in ASD probands from cohorts such as SAGE.[8] These data indicate that, while MARK2 mutations are rare in the general population, when present they confer a very large effect size on ASD and neurodevelopmental risk.

ClinVar and the Gong et al. cohort provide a window into the variant spectrum. Gong and colleagues identified 31 individuals with diverse MARK2 variants, including multiple truncating alleles scattered throughout the coding sequence, frameshift and insertion–deletion variants leading to premature stop codons, canonical splice-site mutations, and missense variants targeting conserved residues in the kinase domain and C-terminal regions.[6][12][13][15] Functional assays showed that many missense variants destabilized the protein or reduced kinase function, again converging on a LoF mechanism.[12] Among the ClinVar entries, several variants have been specifically linked to MRD76 with ACMG classifications ranging from pathogenic to uncertain significance, reflecting the evolving nature of variant interpretation as more functional and segregation data become available.[2][14] Population databases like gnomAD reveal that bona fide truncating variants in MARK2 are extremely rare or absent in control individuals, reinforcing their pathogenicity.[2][12]

At present, there is no evidence of common, low-effect-size polymorphisms in MARK2 that act as diffuse susceptibility alleles for ASD or ID in the general population; all reported disease-associated variants are rare, high-impact coding or splice changes, typical of monogenic NDD genes.[8][12] There is likewise no evidence that copy-number variations or large chromosomal rearrangements involving MARK2 contribute significantly to the disease, although ClinVar reports at least one multiexon deletion (EX2–19DEL) classified as pathogenic for MRD76.[14] Thus, the known risk architecture is dominated by rare, high-penetrance coding variants.

### 2.3 Environmental and non-genetic factors

To date, no specific environmental, infectious, or lifestyle factors have been identified as primary etiologic contributors to MARK2-related intellectual developmental disorder. The available clinical series do not report consistent exposures to toxins, infections, or perinatal insults that could plausibly act as necessary or sufficient causes.[7][12][18] Moreover, the presence of de novo pathogenic variants and the replication of key disease features in animal and cellular models with engineered MARK2 loss strongly support a primarily genetic etiology.[7][9][12]

It is important, however, to distinguish between causal factors and modulators of disease expression. While non-genetic factors are not known to cause MRD76 in the absence of a MARK2 variant, environmental influences such as early developmental enrichment, access to therapies, seizure control, and management of comorbidities likely modulate the clinical course and quality of life, much as they do in other monogenic ASD/ID syndromes. For example, early intensive behavioral intervention, speech and language therapy, and educational support may ameliorate functional impairments even though they do not alter the underlying genetic defect. These influences are better considered as determinants of outcome rather than causative factors.

From a mechanistic standpoint, the pathways in which MARK2 functions—such as WNT/β‑catenin and PI3K/AKT/mTOR—are known to be sensitive to metabolic state, growth factors, and inflammatory signals.[9][10] However, there is no disease-specific evidence that particular environmental exposures modulate these pathways in a way that alters MRD76 risk. The Comparative Toxicogenomics Database and related resources do not currently list MARK2-specific toxicant interactions that translate into human neurodevelopmental disease risk.[10] Thus, environmental contributions remain hypothetical and unsubstantiated for this specific condition.

### 2.4 Protective factors and gene–environment interactions

No genetic protective factors—such as modifier alleles that reduce disease severity in individuals with pathogenic MARK2 variants—have been empirically identified. In the cohorts reported to date, phenotypic variability exists across individuals with similar classes of variants, but this variation has not yet been convincingly linked to specific modifier genes.[7][12][18] It remains possible that genetic variation in parallel pathways, such as other microtubule-associated kinases or WNT pathway components, could modulate disease expressivity; however, this remains an area of conjecture rather than demonstrated evidence.

Likewise, no specific environmental factors have been shown to protect against the development of MRD76 in genetically susceptible individuals. Standard public health measures that promote healthy neurodevelopment—such as avoidance of teratogens, adequate maternal nutrition, and early developmental screening—are likely beneficial at a general level but have not been studied in the context of MARK2-related disease. There is no evidence of classical gene–environment interactions in which a specific exposure (for example, a toxin) interacts with MARK2 variants to precipitate disease in one context but not another.

On a mechanistic level, some gene–environment interactions can be inferred from pathway biology, albeit without direct human evidence. For instance, WNT/β‑catenin signaling is influenced by extracellular ligands like WNT3A and by pharmacologic agents such as lithium, which inhibits GSK3β and thereby stabilizes β‑catenin.[9][12] Gong et al. demonstrated that exogenous WNT3A and lithium can rescue WNT/β‑catenin signaling and associated cellular phenotypes in MARK2-mutant neural progenitor cells, indicating that environmental or pharmacologic manipulation of this pathway can modulate the cellular consequences of MARK2 loss.[12] However, this has not yet been translated into population-level gene–environment interaction data, and lithium’s potential role is still at the experimental, preclinical stage rather than a recognized protective factor in humans.

## 3. Phenotypes

### 3.1 Core neurodevelopmental features: developmental delay, intellectual disability, and speech–language impairment

The core phenotypic triad of MARK2-related intellectual developmental disorder comprises global developmental delay, intellectual disability of variable severity, and pronounced impairment of speech and language. This triad is universally present in the currently described cohorts and defines the disorder’s primary clinical signature.[1][11][12][16][17]

MedGen and OMIM summarize MRD76 as “characterized by developmental delay, mildly to severely impaired intellectual development with speech and language deficits, and autism,” emphasizing that cognitive and language deficits are central features.[1][11][16][17] In the Gong et al. cohort of 31 individuals with MARK2 variants, all 29 individuals with available cognitive assessment data exhibited developmental delay or intellectual disability, and all 31 individuals had speech and language problems.[12] The authors report that delays are often recognized in infancy or early childhood, with late acquisition of motor milestones and particularly delayed expressive language; some individuals remain minimally verbal or nonverbal.[12] The severity of intellectual disability ranges from mild to severe, with a predominance of moderate impairment, though detailed IQ distributions are still limited.[12]

These features correspond to Human Phenotype Ontology terms such as *Global developmental delay* (HP:0001263), *Intellectual disability* (HP:0001249), and *Speech delay* (HP:0000750), with many individuals likely meeting criteria for *Severe speech and language impairment* (HP:0000045). The onset is uniformly in the pediatric period, typically within the first two years of life, and the deficits are chronic and non-remitting, consistent with a congenital neurodevelopmental etiology rather than acquired regression.[1][11][12] Although developmental progress continues over time, the gap relative to age-matched peers often widens or remains significant, indicating that the disorder follows a non-progressive but persistent trajectory.

The impact of these core deficits on daily functioning and quality of life is substantial. Children often require early intervention services, special education, and life-long support for activities of daily living and communication. Limitations in expressive and receptive language significantly constrain social participation and access to education, and may contribute indirectly to behavioral challenges when individuals cannot effectively express needs or discomfort. Such impacts are well captured by quality-of-life instruments like the EQ-5D and SF-36, although disease-specific data for MRD76 are not yet available. Clinically, early recognition and referral for speech and language therapy and developmental services are critical components of management.

### 3.2 Autism spectrum disorder and behavioral manifestations

Autism spectrum disorder is a nearly universal feature of MARK2-related intellectual developmental disorder. Gong et al. report that 30 of 31 individuals (96.8%) in their cohort had ASD or strong autistic features, and SFARI Gene reiterates that 96.8% of individuals in this series met criteria for ASD, emphasizing the tight linkage.[8][12] The autism phenotype includes deficits in social communication, restricted and repetitive behaviors, sensory abnormalities, and often co-occurring behavioral disturbances such as aggression, anxiety, and attention-deficit/hyperactivity disorder (ADHD) features.[7][8][12][18]

The 2024 Gong paper explicitly states:

> “Here, we report 31 individuals with *MARK2* variants and presenting with ASD, other neurodevelopmental disorders, and distinctive facial features…Other NDDs were common within the cohort, including intellectual disability/developmental delay (100%), speech-language problems (100%), seizure/epilepsy (46%), motor delay (62%), and behavior disorders (74%).”[12]

This description underscores that ASD is not only prevalent but also embedded in a broader constellation of NDDs and behavioral conditions. The Human Genetics and Genomics Advances study similarly notes that among their expanded set of individuals with MARK2 variants, most exhibited ASD features, including social difficulties, repetitive behaviors, and sensory sensitivities.[7][18] These features map to HPO terms such as *Autism* (HP:0000717), *Attention deficit hyperactivity disorder* (HP:0007018), *Aggressive behavior* (HP:0000718), *Anxiety* (HP:0000739), and *Abnormality of behavior* (HP:0000708).

Behavior disorders—including aggression, self-injury, anxiety, and attention problems—were reported in 74% of individuals in the Gong cohort.[12] Such behavioral issues have profound implications for family stress, educational placement, and the need for psychiatric or behavioral interventions. They may also complicate medical management, particularly when co-occurring with seizures or sensory hypersensitivities. The behavioral phenotype thus contributes substantially to disease burden and may be an important target for intervention.

From a DSM-5 perspective, most individuals meet criteria for ASD plus comorbid intellectual disability and language disorder, and some may meet criteria for ADHD or anxiety disorders. The Research Domain Criteria (RDoC) framework would categorize the observed deficits across social processes, cognitive systems, and arousal/regulatory systems. However, no standardized, MRD76-specific psychiatric assessment data have been published, and the behavioral description is currently based on clinical impression and parental reports, emphasizing the need for more systematic evaluation.

### 3.3 Neurologic features: seizures, motor delay, and hypotonia

Neurological manifestations beyond cognitive and behavioral features are common but variable in MARK2-related intellectual developmental disorder. Seizure disorders, motor delay, and hypotonia represent the most frequently reported neurologic phenotypes. Gong et al. report seizures or epilepsy in 46% of their cohort, motor delay in 62%, and a range of other neurologic signs.[12] MedGen and OMIM also list seizures and motor delay as variable features of MRD76.[1][11][16][17]

Seizures can be classified under HPO terms such as *Seizure* (HP:0001250) and *Epilepsy* (HP:0001250 with appropriate subterms). The age at seizure onset, type of seizures (for example, generalized tonic–clonic, focal), and response to antiepileptic medications are not yet systematically summarized for MARK2-related disease, but case-level descriptions suggest heterogeneity and generally manageable epilepsy, rather than severe early-onset epileptic encephalopathy.[12] The presence of seizures contributes to overall morbidity, increases the need for neurologic follow-up, and may exacerbate developmental impairments, particularly if poorly controlled.

Motor delay, as reflected in late attainment of milestones such as sitting, crawling, and walking, is reported in approximately two-thirds of individuals and corresponds to HPO terms such as *Motor delay* (HP:0001270) and *Gait disturbance* (HP:0001288).[12] Hypotonia—reduced muscle tone—is not explicitly quantified in the Gong abstract but is frequently seen in monogenic NDDs involving cytoskeletal regulators and may be present in a subset of patients. Mark2’s role in axon development and neuronal polarity, as inferred from mouse studies, suggests that altered corticospinal and cerebellar circuits may underlie subtle motor coordination deficits.[4][9] However, overt cerebellar signs are not consistently reported, and most individuals eventually gain independent ambulation, albeit delayed.

Neuroimaging data for human patients remain sparse in the published literature. Nevertheless, the Mark2^+/−^ mouse model used by Gong et al. demonstrated “abnormal cortical formation and partition,” indicating that partial loss of MARK2 can disrupt cortical lamination and regionalization.[12] This finding raises the possibility that subtle cortical malformations or connectivity alterations might be present in human MRD76, even if gross brain MRI appears unremarkable. Future studies with high-resolution imaging and quantitative morphometry may elucidate such structural correlates.

Collectively, seizure susceptibility and motor delay add to the complexity of clinical management, necessitating routine neurologic evaluation and individualized seizure monitoring. These neurologic features also impact quality of life by limiting independence, driving restrictions, and increasing caregiver burden.

### 3.4 Craniofacial and systemic features

Distinctive facial features and other systemic manifestations provide additional phenotypic clues to MARK2-related intellectual developmental disorder. MedGen, drawing on the Gong 2024 study and other reports, lists a range of craniofacial findings including a narrow face, abnormal or broad forehead, downslanting palpebral fissures, large or dysplastic ears, and additional features such as bulbous nose, frontal bossing, telecanthus or hypertelorism, short philtrum, and ptosis.[1][11][12][16][17] SFARI Gene similarly emphasizes “distinctive recurrent facial features including a narrow face, abnormal or broad forehead, downslanting palpebral fissures, and large or dysplastic ears.”[8]

These features map to HPO terms such as *Narrow face* (HP:0000275), *Broad forehead* or *Prominent forehead* (HP:0002003, HP:0001999), *Downslanting palpebral fissures* (HP:0000494), *Large ears* (HP:0000400), *Dysplastic ears* (HP:0000389), *Bulbous nose* (HP:0000414), *Telecanthus* (HP:0000506), *Hypertelorism* (HP:0000316), *Short philtrum* (HP:0000322), *Ptosis* (HP:0000508), and *Microcephaly* (HP:0000252) where head circumference is below −2 standard deviations.[11] MedGen elaborates on these features by defining, for example, bulbous nose as “increased volume and globular shape of the anteroinferior aspect of the nose,” and narrow face as a reduction in bizygomatic and bigonial width beyond 2 standard deviations below the mean.[11] Such detailed morphologic phenotyping aids in recognizing recurrent syndromic patterns.

Ophthalmologic abnormalities, referred to in the OMIM/MedGen summaries as “eye abnormalities,” may include ptosis, epicanthal folds, or other minor anomalies, though systematic ophthalmologic data are lacking.[1][11][16][17] Growth parameters, such as stature and weight, have not been systematically described, but the available evidence does not suggest a consistent pattern of overgrowth or failure to thrive; most individuals appear to have normal or mildly altered growth, with occasional microcephaly or macrocephaly.[11][12]

Non-neurologic systemic involvement appears limited, consistent with MARK2’s predominant function in the nervous system and epithelia. GeneGlobe and UniProt note that MARK2 is strongly expressed in heart, brain, skeletal muscle, and pancreas, with lower levels in lung and liver, but clinical reports have not documented consistent cardiac, endocrine, or renal abnormalities attributable to MARK2 variants.[6][10] The GeneGlobe disease association list includes terms such as hyperplasia, hypoglycemia, weight gain, lymphadenopathy, and depression, but these associations reflect broader data mining rather than specific features of MRD76.[10] Thus, the disease is best characterized as primarily neurodevelopmental and craniofacial, with systemic features being minor or incidental.

### 3.5 Age of onset, severity, progression, and variability

MARK2-related intellectual developmental disorder is an early-onset condition, with manifestations arising during prenatal or early postnatal brain development and becoming clinically apparent in infancy or early childhood. Gong et al. report that the age at clinical assessment in their cohort ranged from 2 to 46 years, but the underlying developmental abnormalities—including delays in milestones, language acquisition, and social interaction—were typically evident by the second year of life.[12] The developmental delay often encompasses both gross and fine motor skills, language, and adaptive functioning, consistent with global developmental delay in toddlers, and evolves into diagnosed intellectual disability and ASD by school age.

The severity of intellectual disability and ASD varies among individuals, reflecting variable expressivity. Some individuals may have mild intellectual disability and relatively preserved adaptive skills, while others exhibit severe cognitive impairment and limited functional independence.[12][7] Speech and language impairment tends to be severe, with many individuals having markedly reduced expressive language or remaining nonverbal, although receptive language may be somewhat better preserved.[12] Seizures, where present, add to the severity of the neurologic phenotype, but even seizure-free individuals can have significant impairments.

The progression of the disorder appears non-degenerative; that is, there is no evidence of progressive loss of skills or neurodegenerative decline. Instead, the course is characterized by delayed acquisition and persistent deficits, with gradual skill gain over time under supportive therapies. This pattern distinguishes MRD76 from conditions such as Rett syndrome or certain mitochondrial disorders, where early normal development is followed by regression. Where longitudinal data exist, they suggest a chronic, life-long condition with stable or slowly improving developmental trajectories rather than a progressive worsening.[7][12]

Despite the overall consistency of the core phenotype, individual variability is evident in the presence and severity of seizures, behavioral disorders, motor impairments, and facial dysmorphism. Some of this variability likely reflects stochastic factors, environmental influences, and genetic background, including unidentified modifier genes. The presence of a familial case in the HGG Advances study underscores that even within the same family, phenotype can vary among carriers of the same MARK2 variant, indicating variable expressivity.[7][18] Thus, clinicians should anticipate a spectrum of presentations, though all with a shared core of ASD, ID, and language impairment.

### 3.6 Quality of life impact

The impact of MARK2-related intellectual developmental disorder on quality of life is substantial and multifaceted, affecting the affected individuals, their families, and broader support systems. Core deficits in cognition, language, and social communication limit educational attainment, employment prospects, and independent living. Behavioral issues such as aggression, anxiety, and ADHD symptoms can strain family relationships, increase caregiver stress, and necessitate psychopharmacologic interventions. Seizures and motor impairments contribute to physical morbidity, restrict activities, and require ongoing medical supervision.[7][12][18]

Standardized health-related quality-of-life measures such as the EQ-5D, SF-36, or Pediatric Quality of Life Inventory (PedsQL) have not yet been applied specifically to MRD76 cohorts, but extrapolation from similar ASD–ID syndromes suggests that significant impairments exist across domains of physical functioning, emotional well-being, social participation, and school performance. Caregivers frequently report high levels of stress, depression, and financial burden in managing children with complex neurodevelopmental disorders, and it is reasonable to infer similar challenges in families affected by MARK2-related disease.

Importantly, the non-degenerative nature of the disorder and the presence of learning potential mean that supportive interventions—speech and language therapy, occupational therapy, behavioral therapy, individualized education plans—can yield meaningful improvements in function and quality of life. Early diagnosis via genomic testing allows families to access appropriate services and plan for the future, although access may be limited by socioeconomic factors and healthcare disparities. Future targeted therapies, if developed, would ideally complement, not replace, these foundational supportive measures.

## 4. Genetic and Molecular Information

### 4.1 MARK2 gene structure, expression, and protein function

The **MARK2** gene (microtubule affinity–regulating kinase 2) is located on chromosome 11q13.1 and encodes a serine/threonine protein kinase belonging to the PAR-1 family.[1][3][6][10] The gene produces multiple transcript variants that encode different isoforms, reflecting alternative splicing and transcript initiation, and the encoded proteins localize to cell membranes and cytosolic compartments.[6][10] UniProt describes the canonical MARK2 protein as a multi-domain kinase comprising an N-terminal kinase domain, a ubiquitin-associated (UBA)–like domain, and regulatory C-terminal regions that influence subcellular targeting and activity.[6] The enzyme is also known by alternative names such as ELK, EMK1, and PAR-1 homolog B, reflecting historical nomenclatures in different organisms and research contexts.[6][9][10]

MARK2 is widely expressed, with particularly high levels in the brain, heart, skeletal muscle, and pancreas, and lower expression in lung and liver.[6][10] In the nervous system, MARK2 is expressed in progenitor zones and mature neurons, including cortical neurons, hippocampal neurons, and cerebellar neurons, and localizes to axons, dendrites, and synapses.[4][6][9][10] NCBI Gene and Gene Ontology annotations indicate that MARK2 participates in processes such as microtubule cytoskeleton organization, axon development, neuron migration, establishment and maintenance of cell polarity, and regulation of neuron projection development.[4][10] In mouse, Mark2 expression has been observed in early embryonic stages, cerebral cortex, and oocytes, consistent with roles in early development and neurogenesis.[4]

At the biochemical level, MARK2 functions as a protein serine/threonine kinase with ATP binding, magnesium ion binding, and tau protein binding activities.[4][6][10] It phosphorylates a variety of substrates, including microtubule-associated proteins MAP2, MAP4, tau, and doublecortin (DCX), as well as proteins involved in vesicular trafficking (for example, KIF13B, RAB11FIP2) and signaling (for example, CRTC2/TORC2, HDAC7).[4][6][9][10] Through phosphorylation of these substrates, MARK2 regulates microtubule stability, neurite outgrowth, centrosome positioning, and the establishment of neuronal polarity. As summarized in a 2024 Nature review, “Microtubule-Affinity Regulating Kinase 2 (MARK2) phosphorylates microtubule-associated proteins, playing a crucial role in cancer and neurodegenerative diseases,” and “is required for neurite outgrowth and establishment of neuronal polarity.”[9]

Functional annotations from Gene Ontology include molecular functions such as *protein serine/threonine kinase activity* (GO:0004674), *tau-protein kinase activity* (GO:0050317), *ATP binding* (GO:0005524), and *microtubule binding* (GO:0008017), as well as biological processes like *microtubule cytoskeleton organization* (GO:0007010), *neuron migration* (GO:0001764), *axonogenesis* (GO:0007409), *establishment or maintenance of epithelial cell apical/basal polarity* (GO:0045197), and *Wnt receptor signaling pathway* (GO:0016055).[4][9][10] Cellular component annotations include *cytoplasm* (GO:0005737), *cell cortex* (GO:0005938), *dendrite* (GO:0030425), and *lateral plasma membrane* (GO:0016328), reflecting MARK2’s localization to structures where it can regulate microtubule dynamics and polarity.[4][5][9]

### 4.2 Pathogenic variant types and distribution

Pathogenic variants in MARK2 associated with MRD76 encompass a range of variant types distributed across the gene, with a predominance of truncating and loss-of-function alleles. Gong et al. identified 31 individuals with rare MARK2 variants, the majority of which were predicted to result in loss of function.[6][12][13][15] The variant spectrum included:

Truncating variants such as nonsense mutations (for example, p.Arg71Ter, p.Gln747Ter) and frameshift insertions or deletions (for example, p.Ala216fs, p.Phe271fs, p.Gly580fs, p.Cys723fs) that introduce premature stop codons and likely trigger nonsense-mediated decay or produce truncated, nonfunctional proteins.[2][6][12][14]

Canonical splice-site variants such as c.337+1G>T, c.1101+5G>A, c.2006+2T>G, and c.1514+2G>T, which alter RNA splicing and can lead to exon skipping, intron retention, or activation of cryptic splice sites.[2][12][14] For example, Gong et al. demonstrated that the c.337+1G>T variant results in skipping of exon 1 and a 49 bp deletion in the MARK2 transcript in minigene assays.[2][12]

Multiexon deletions such as the EX2–19DEL variant in ClinVar, which removes a large portion of the coding sequence.[14]

Missense variants affecting conserved residues in the kinase domain or regulatory regions, some of which were shown by in vitro expression assays to reduce protein stability, alter kinase activity, or impair subcellular localization.[6][7][12][18]

ClinVar’s compilation of 22 MARK2 variants associated with MRD76 or ASD illustrates this diversity. For example, NM_001039469.3:c.211C>T (p.Arg71Ter) is a nonsense variant linked to intellectual disability; c.239C>T (p.Ala80Val) is a missense variant associated with ASD; c.644dup (p.Tyr215Ter) and c.800dup (p.Tyr267Ter) are duplications introducing premature stops; c.812del (p.Phe271fs) and c.1737_1738dup (p.Gly580fs) are frameshift variants classified as pathogenic; and c.2239C>T (p.Gln747Ter) is a nonsense variant associated with ASD.[14] Several missense variants (for example, p.Ser247Phe, p.Asp410Glu, p.Pro556Leu, p.Ser577Asn, p.Ala432Thr, p.Leu758Arg) are currently classified as variants of uncertain significance, reflecting the need for additional functional and segregation data.[14]

The distribution of variants across the gene suggests that there is no single mutational hotspot; rather, pathogenic variants can occur throughout the coding sequence, including the kinase domain and C-terminal regulatory regions. This pattern is consistent with a general sensitivity of MARK2 function to haploinsufficiency or disruption, rather than a specific domain-limited effect. However, functional assays suggest that variants in the kinase domain may have particularly strong impacts on catalytic activity, whereas C-terminal variants may affect localization or protein–protein interactions.[6][7][12][18]

### 4.3 Variant classification, population frequencies, and germline origin

The classification of MARK2 variants follows standard ACMG/AMP guidelines, integrating evidence from population frequency, computational predictions, segregation, de novo occurrence, functional studies, and phenotypic consistency.[2][12][14] Many truncating variants meet criteria for pathogenicity or likely pathogenicity based on their nature, de novo status, and absence from population databases. For example, Gong et al. reported multiple de novo truncating variants not observed in gnomAD, with consistent phenotypes across carriers, supporting their classification as pathogenic.[12] The ClinVar entries for several truncating variants (for example, p.Phe271fs, p.Cys723fs, p.Gln747Ter, EX2–19DEL, c.1514+2G>T) are labeled pathogenic, reflecting concordant interpretations by multiple laboratories.[14]

Missense variants are more challenging to interpret, and several are currently classified as variants of uncertain significance (VUS) despite being associated with ASD or MRD76 phenotypes.[14] Gong et al. addressed this gap by performing in vitro expression assays, demonstrating that many missense variants lead to reduced protein levels or altered kinase activity, thereby providing functional evidence supporting a loss-of-function mechanism.[12] Nevertheless, in the absence of extensive segregation data, some missense variants remain formally VUS, emphasizing the importance of functional genomics in variant interpretation.

Population frequency data from gnomAD and similar databases indicate that LoF variants in MARK2 are extremely rare in the general population, consistent with strong purifying selection. Many pathogenic variants identified in patients are absent or occur at exceedingly low frequencies (<1 in 100,000) in control datasets.[2][12] This rarity further supports their pathogenicity. At the same time, the scarcity of LoF variants in healthy individuals suggests that haploinsufficiency of MARK2 is not well tolerated, aligning with the severe neurodevelopmental phenotypes observed.

With respect to origin, most pathogenic MARK2 variants identified in the Gong and HGG Advances cohorts are de novo, consistent with the severe, early-onset nature of the disorder.[7][12][18] Trio exome or genome sequencing was used in many cases to demonstrate de novo status, adding strong evidence for causality.[7][12] However, at least one familial case has been reported in which a pathogenic variant segregated with NDD phenotypes, confirming that autosomal dominant inheritance with vertical transmission can occur.[7][18] Germline mosaicism has not yet been formally documented, but given the general patterns in de novo dominant NDDs, it remains a possibility in parents of apparently sporadic cases and should be considered in genetic counseling.

All reported disease-associated variants are germline, not somatic, and arise in the context of constitutional DNA. Somatic mutations in MARK2 have been described in cancers, but these are distinct from the germline variants causing MRD76 and are associated with tumorigenesis rather than neurodevelopmental disorders.[9][10] Thus, the etiologic variants in MRD76 are primarily germline, high-penetrance alleles.

### 4.4 Functional consequences and disease mechanism at the gene–protein level

Functional studies in human cells, mouse models, and Drosophila have converged on the conclusion that most MARK2 variants associated with MRD76 exert **loss-of-function** or hypomorphic effects on the kinase, with haploinsufficiency as the predominant mechanism.[7][9][12][18] Gong et al. performed a combination of expression analyses, minigene assays, and iPSC-derived neural cell studies, showing that truncating and splice variants reduce MARK2 mRNA and protein levels and that many missense variants destabilize the protein or impair its kinase activity.[12] In particular, the c.337+1G>T splice-site variant was shown to result in skipping of exon 1 and a 49 bp deletion of the MARK2 transcript, leading to reduced gene expression and functional loss.[2][12]

In their HGG Advances study, Yang and colleagues established a humanized Drosophila model in which human MARK2 variants were expressed in fly neurons. They found that “MARK2 variants span a range of functional consequences, primarily exhibiting hypomorphic or loss-of-function effects” and that truncating variants “consistently showed reduced protein levels and rescued lethality, a loss-of-function mechanism.”[7][18] These experiments provided in vivo evidence that patient-derived variants reduce MARK2 activity to levels that impair neuronal function but may not completely abolish it, consistent with the partial loss-of-function and hypomorphic classification.

At the cellular level, reduced MARK2 activity disrupts microtubule cytoskeleton organization and neuronal polarity. Gong et al. used proband-derived and CRISPR-engineered iPSCs to generate neural progenitor cells (NPCs) and neural rosettes, demonstrating that MARK2 loss leads to early neuronal developmental and functional deficits, including anomalous polarity and disorganization in neural rosettes, as well as imbalanced proliferation and differentiation in NPCs.[12] These phenotypes reflect the known roles of MARK2 in regulating microtubule-associated proteins and cell polarity, and they provide a direct link between gene-level loss of function and developmental abnormalities in human neural cells.

At the signaling level, MARK2 loss has been shown to downregulate WNT/β‑catenin signaling, as discussed in detail in Section 6. Gong et al. reported that RNA-seq of MARK2-mutant NPCs revealed downregulation of WNT pathway components, including decreased expression of WNT3A, and that β‑catenin protein levels were reduced.[12] They further demonstrated that exogenous WNT3A and lithium could restore WNT/β‑catenin signaling and rescue NPC phenotypes, indicating that WNT pathway disruption is a key downstream consequence of MARK2 loss.[12] This WNT pathway effect is consistent with GO annotations linking MARK2 to the WNT receptor signaling pathway and with broader literature on MARK2’s role in WNT, PI3K/AKT/mTOR, and NF‑κB pathways.[9][10]

Collectively, these studies establish a causal chain from gene-level loss of function to cellular and pathway-level dysfunction, providing a robust mechanistic foundation for understanding MRD76.

### 4.5 Modifier genes, epigenetics, and structural variation

To date, no specific modifier genes have been definitively identified that alter the severity or expression of MARK2-related intellectual developmental disorder. The observed phenotypic variability—particularly in seizures, behavioral issues, and facial features—suggests that genetic background and possibly other gene–gene interactions influence expressivity, but no single modifier locus has emerged from the relatively small cohorts analyzed.[7][12][18] Future genomic studies with larger sample sizes and integrative analyses may reveal modifiers, potentially in genes encoding other microtubule-associated proteins, kinases, or WNT pathway components.

Epigenetic dysregulation specific to MARK2-related disease has not been reported. The existing mechanistic work has focused primarily on transcriptomic and protein-level changes downstream of MARK2 loss, rather than on DNA methylation, histone modifications, or chromatin architecture at the MARK2 locus or elsewhere.[12] However, given the central role of WNT/β‑catenin signaling in regulating gene expression during neurodevelopment, it is plausible that MARK2 loss indirectly affects epigenetic landscapes through altered transcriptional programs, although this remains speculative.

Structural variation involving MARK2, such as large deletions or duplications, appears to be rare. ClinVar reports one multiexon deletion (EX2–19DEL) classified as pathogenic for MRD76, implying that significant loss of coding sequence can cause the disorder.[14] No recurrent balanced translocations or inversions disrupting MARK2 have been described. The absence of more extensive structural variation data likely reflects both the rarity of such events and the predominant use of exome sequencing (which is less sensitive to structural variants) in current cohorts. Genome sequencing and array-based copy-number analysis in future studies may reveal additional structural variants.

## 5. Environmental Information

### 5.1 Environmental exposures and toxins

There is currently no evidence that specific environmental exposures—such as toxins, heavy metals, radiation, or pollutants—play a direct etiologic role in MARK2-related intellectual developmental disorder. The comparative toxicogenomics and environmental health literature does not identify any particular exposure that induces germline MARK2 mutations or selectively interacts with existing MARK2 variants to cause MRD76.[10] Moreover, the high proportion of de novo germline variants in affected individuals suggests random mutational processes rather than specific environmental mutagens, although as in other dominant NDDs, paternal age effects or germline exposure histories have not been systematically studied.[7][12]

While environmental exposures are important for general neurodevelopmental health, their contribution to this monogenic, high-penetrance disorder appears limited. However, environmental factors may modulate disease course and symptom severity, for example, by influencing seizure thresholds, sleep, and behavioral regulation. Standard pediatric neurology practice emphasizes the avoidance of known seizure triggers and maintenance of a stable, supportive environment, but these measures are general rather than specific to MARK2-related disease.

### 5.2 Lifestyle and psychosocial factors

Lifestyle factors such as diet, physical activity, and sleep patterns, as well as psychosocial factors like family support and access to educational services, can influence the lived experience and functional outcomes of individuals with MARK2-related intellectual developmental disorder. However, these influences operate as modifiers rather than causative factors. No study has identified particular diets, exercise regimes, or lifestyle modifications that specifically alter MARK2-related disease expression beyond their general role in child development.

Public health datasets and surveys such as NHANES and WHO reports do not contain disease-specific entries for MRD76, reflecting its rarity and relatively recent recognition. As such, lifestyle and psychosocial data specific to MARK2-related disease are lacking, and clinicians must extrapolate from broader ASD and ID populations when making recommendations. General health promotion—balanced nutrition, regular physical activity, adequate sleep, and avoidance of substance use in adolescents—is advisable but not disease-specific.

### 5.3 Infectious agents and immune factors

No infectious agents have been implicated in the etiology or pathogenesis of MARK2-related intellectual developmental disorder. There is no evidence that prenatal infections, neurotropic viruses, or postnatal infections play a causal role, nor that infections interact with MARK2 variants in a gene–environment fashion. Similarly, no immunologic abnormalities—such as autoimmunity or chronic inflammation—have been reported as central features of MRD76.[1][11][12]

Nevertheless, infections and immune responses can influence seizure control, behavioral stability, and overall health in affected individuals, as they do in other children with neurologic disorders. Standard vaccination schedules and infection prevention measures should be followed. There is no indication that immunization adversely interacts with MARK2 variants, and indeed prevention of central nervous system infections is especially important in individuals with baseline neurologic vulnerability.

## 6. Mechanism and Pathophysiology

To structure the mechanistic understanding of MARK2-related intellectual developmental disorder, it is useful to lay out an ordered causal chain from the initiating lesion at the gene level to the clinical manifestations observed. This chain synthesizes evidence from human genetics, cell biology, and animal models and distinguishes demonstrated mechanisms from plausible inferences.

1) Germline heterozygous loss-of-function or hypomorphic variants in MARK2 reduce functional MARK2 protein levels or kinase activity in neural progenitor cells and neurons, leading to decreased phosphorylation of key microtubule-associated substrates and disruption of microtubule cytoskeleton organization; this step is demonstrated by human variant functional assays and iPSC models.[7][9][12]

2) Reduced MARK2 activity impairs neuronal polarity, neurite outgrowth, and centrosome positioning, resulting in anomalous polarity and disorganization of neural rosettes and cortical progenitor architecture; this is demonstrated in human iPSC-derived neural rosettes and inferred from mouse and Drosophila models of MARK2 loss.[4][7][9][12]

3) MARK2 loss leads to downregulation of WNT/β‑catenin signaling, including decreased expression of WNT3A and reduced β‑catenin levels, which in turn cause imbalanced proliferation and differentiation in neural progenitor cells; this step is demonstrated by RNA-seq, protein assays, and rescue experiments with WNT3A and lithium.[9][12]

4) The combined disruption of microtubule dynamics, cell polarity, and WNT signaling in neural progenitors results in abnormal cortical formation and partition, altered neuronal migration, and miswiring of cortical circuits; this step is demonstrated in Mark2^+/−^ mice and inferred in humans.[4][9][12]

5) These neurodevelopmental abnormalities lead to impaired synaptic connectivity, dendritic spine development, and network function in cortical and subcortical regions implicated in cognition, language, and social behavior, producing the core clinical triad of intellectual disability, speech–language impairment, and autism spectrum disorder; this step is inferred from the known roles of MARK2 and from behavioral phenotypes in Mark2^+/−^ mice and Drosophila.[7][8][9][12][18]

6) Additional downstream consequences, such as altered excitatory–inhibitory balance, may lower seizure thresholds and contribute to epilepsy and motor abnormalities, while subtle craniofacial developmental effects yield distinctive facial features; these steps are inferred based on the overlapping developmental pathways and observed clinical phenotypes.[1][11][12][16][17]

### 6.1 MARK2, microtubule dynamics, and cell polarity

A central mechanistic theme in MARK2-related intellectual developmental disorder is the disruption of microtubule cytoskeleton organization and cell polarity. In neurons, proper microtubule organization is essential for axon and dendrite formation, neuronal migration, and synaptic connectivity. MARK2, as a microtubule affinity–regulating kinase, phosphorylates microtubule-associated proteins, thereby modulating microtubule stability and dynamic behavior.[4][6][9][10]

Early work in model systems established that MARK/PAR-1 kinases are required for neurite outgrowth and establishment of neuronal polarity. Biernat et al., cited in the 2024 Nature review, showed that MARK/PAR-1 activity is necessary for neurite outgrowth in cultured neurons, with overexpression or inhibition altering axon–dendrite specification.[9] Terabayashi and colleagues demonstrated that MARK2 negatively regulates dendritic development in hippocampal neurons, emphasizing its role in dendrite–axon balance.[9] NCBI Gene annotations for mouse Mark2 note that it is “predicted to be involved in generation of neurons; regulation of neuron projection development; and regulation of neurofibrillary tangle assembly,” and that it is active in glutamatergic synapses and postsynaptic compartments, consistent with roles in synaptic structure and function.[4]

MARK2 phosphorylates substrates such as tau, MAP2, MAP4, and DCX, promoting their detachment from microtubules and thereby destabilizing microtubules or altering their dynamics.[4][6][9][10] In neurons, this phosphorylation allows for dynamic remodeling of microtubules during axon formation and branching. In MARK2-deficient conditions, reduced phosphorylation may lead to aberrant microtubule stability, mispositioned centrosomes, and failed polarization, as observed in neural rosettes derived from MARK2-mutant human iPSCs.[12] Gong et al. describe “anomalous polarity and dis-organization in neural rosettes” and “imbalanced proliferation and differentiation in neural progenitor cells (NPCs)” in MARK2-loss iPSC models, reinforcing this mechanistic link.[12]

At the cellular process level, these roles correspond to GO terms such as *microtubule cytoskeleton organization* (GO:0007010), *neuron projection development* (GO:0031175), *axonogenesis* (GO:0007409), *neuron migration* (GO:0001764), and *establishment or maintenance of cell polarity* (GO:0045184). The relevant cell types include neural progenitor cells (CL:0000125), excitatory cortical neurons (CL:0002603), inhibitory interneurons (CL:0000099), and glial cells such as astrocytes (CL:0000127), though MARK2’s primary pathogenic effects appear concentrated in progenitors and neurons.[4][9][10][12]

### 6.2 WNT/β‑catenin pathway downregulation and neural progenitors

A key mechanistic advance from Gong et al.’s 2024 study is the demonstration that MARK2 loss leads to downregulation of the WNT/β‑catenin signaling pathway in human neural progenitor cells, and that this downregulation underlies early neurogenesis defects.[12] RNA sequencing of MARK2-mutant iPSC-derived NPCs revealed significant reductions in expression of WNT pathway components, particularly *WNT3A*, *ASCL1*, *HES5*, and *FEZF2*, with WNT3A identified as the top downregulated gene.[12] Western blotting confirmed decreased WNT3A and β‑catenin protein levels in mutant and CRISPR-deleted cells, along with reduced phosphorylation of GSK3β at Ser9, indicative of reduced WNT pathway activation.[12]

Gong et al. hypothesized that “MARK2 loss led to abnormal early neuronal development via inhibition of the WNT signaling pathway” and tested this by treating mutant NPCs with recombinant human WNT3A and with lithium, a known GSK3β inhibitor and WNT pathway activator.[12] They found that WNT3A treatment increased p‑GSK3β (Ser9) and β‑catenin accumulation and rescued NPC proliferation and differentiation phenotypes, while lithium similarly restored WNT/β‑catenin signaling and corrected neural rosette organization both in vitro and in vivo in Mark2^+/−^ mice.[12][13][15] These rescue experiments strongly support a causal link between MARK2 loss, WNT/β‑catenin pathway downregulation, and neurodevelopmental abnormalities.

The WNT/β‑catenin pathway is a master regulator of neurogenesis, influencing NPC proliferation, self-renewal, and differentiation. WNT3A, in particular, is crucial for cortical neurogenesis; its depletion leads to reduced NPC proliferation and premature differentiation, phenotypes mirrored in MARK2-mutant NPCs.[12] Reduced β‑catenin levels impair transcription of WNT target genes via TCF/LEF transcription factors, altering gene expression programs in developing cortex. GO terms relevant to this pathway include *Wnt signaling pathway* (GO:0016055), *canonical Wnt signaling pathway* (GO:0060070), *regulation of neurogenesis* (GO:0050767), and *regulation of cell proliferation* (GO:0042127).

Mechanistically, MARK2 may interact with the WNT/β‑catenin pathway at multiple levels. The 2024 Nature review notes that MARK2 regulates WNT signaling and other pathways such as PI3K/AKT/mTOR and NF‑κB, potentially through phosphorylation of pathway components or via cross-talk at the level of cytoskeletal organization.[9] In cancer models, MARK2 loss has been reported to inhibit tumor growth and metastasis by altering PI3K/AKT/mTOR signaling, illustrating the kinase’s broader influence on cellular signaling networks.[9] In the neurodevelopmental context, however, the dominant effect appears to be WNT pathway downregulation and its consequences for NPC behavior.

### 6.3 Cortical development, neuronal migration, and circuit formation

At the tissue level, the combined effects of microtubule dysregulation and WNT pathway impairment in neural progenitors culminate in abnormal cortical development. Mark2^+/−^ mice used in the Gong study exhibited “abnormal cortical formation and partition,” indicating disruptions in cortical layering and regionalization.[12] Although detailed histologic descriptions are not provided in the abstract, such phenotypes likely reflect altered radial glial scaffolding, impaired radial migration of neurons, and irregular formation of cortical columns, all of which depend on proper microtubule dynamics and WNT signaling.

These cortical abnormalities align with known roles of MARK2 and WNT3A in cortical development. WNT3A signaling from cortical hem regions is important for patterning dorsomedial cortex and for progenitor expansion, while microtubule-regulating kinases like MARK2 ensure proper orientation and stability of the mitotic spindle and leading processes in radial glia.[4][9][12] Disruption of these processes leads to mispositioned neurons, altered areal identity, and aberrant connectivity, particularly in association cortices implicated in higher-order cognitive and social functions (UBERON:0000956 brain; UBERON:0001869 cerebral cortex).

Neuronal migration defects, as suggested by altered centrosome behavior and radial glial function in Mark2-perturbed systems, would correspond to GO terms such as *neuron migration* (GO:0001764) and *cerebral cortex development* (GO:0021987). The affected cell types include radial glial progenitors (CL:0000125), intermediate progenitors (CL:0002320), and excitatory pyramidal neurons (CL:0002603). Given the roles of these populations in establishing cortical lamination and long-range connectivity, defects in their development can have wide-ranging effects on cognition and behavior.

While human neuroimaging correlates are not yet well documented, the presence of ASD, ID, and language impairments in MRD76 suggests involvement of frontotemporal and perisylvian networks, including Broca and Wernicke regions (UBERON:0001871 temporal lobe; UBERON:0001870 frontal lobe). Altered cortical partitioning in mice may be a structural analog of disrupted cortical specialization in humans, although direct translation requires further study.

### 6.4 Synaptic function, dendritic spines, and network dysfunction

Beyond early developmental roles, MARK2 also contributes to synaptic structure and function in mature neurons. SFARI Gene notes that “MARK2 contributes to establishing neuronal polarity and developing dendritic spines,” and that dysregulation of MARK2 is associated with impaired neuronal differentiation and synaptic function, processes frequently altered in ASD.[7][8][9] The kinase’s phosphorylation of tau, MAP2, and other microtubule-associated proteins influences microtubule stability in dendrites and axons, thereby affecting spine morphology and synaptic connectivity.[4][6][9][10]

In hippocampal neuron cultures, MARK2 has been shown to regulate dendritic branching and spine density, with overexpression or knockdown altering dendrite complexity.[9] In Mark2-deficient mice, abnormalities in dendritic morphology and synaptic plasticity may contribute to behavioral phenotypes, including ASD-like behaviors observed in the Mark2^+/−^ mice described by Gong et al.[12] Although detailed electrophysiologic data are not provided in the available summaries, the combination of dendritic spine abnormalities and altered cortical organization implies synaptic network dysfunction, likely involving both excitatory and inhibitory circuits.

At the process level, these roles correspond to GO terms such as *synapse organization* (GO:0050808), *dendrite morphogenesis* (GO:0048813), *regulation of synaptic plasticity* (GO:0048167), and *regulation of excitatory postsynaptic potential* (GO:0060079). The cell types most directly affected are pyramidal neurons (CL:0002603) and interneurons (CL:0000099), particularly those forming cortical microcircuits implicated in ASD pathophysiology. Network-level consequences include altered oscillatory activity, impaired long-range synchronization, and disrupted sensory integration, all of which are features commonly observed in ASD and related NDDs.

The convergence of microtubule, WNT, and synaptic mechanisms on ASD phenotypes underscores the notion that MRD76 fits within a broader class of “synaptopathies” and “neurodevelopmental connectivity disorders.” However, the specific combination of early progenitor defects and later synaptic abnormalities may distinguish MARK2-related disease from purely synaptic or purely progenitor-level disorders.

### 6.5 Other pathways: PI3K/AKT/mTOR, NF‑κB, and cancer–neurodevelopmental intersections

MARK2’s regulatory influence extends beyond microtubules and WNT to include PI3K/AKT/mTOR and NF‑κB signaling pathways, as highlighted by the 2024 Nature review on MARK2 in the nervous system and cancer.[9] The review notes that “This kinase regulates multiple signaling pathways, including the WNT, PI3K/AKT/mTOR (PAM), and NF-κB pathways, potentially linking it to cancer and the nervous system,” and that “as a crucial regulator of the PI3K/AKT/mTOR pathway, the loss of MARK2 inhibits the growth and metastasis of cancer cells.”[9] Although these insights derive primarily from cancer research, they suggest that MARK2 acts as an important node in growth and survival pathways.

In the neurodevelopmental context, PI3K/AKT/mTOR signaling governs neural progenitor proliferation, neuronal size, and synaptic plasticity, and dysregulation of this pathway is implicated in ASD and macrocephaly syndromes such as PTEN-related disorders. Whether MARK2 loss alters PI3K/AKT/mTOR signaling in developing human brain remains to be demonstrated, but the possibility raises intriguing questions about cross-talk between WNT and PAM pathways in MRD76.[9][12] Similarly, NF‑κB signaling influences neuroinflammation and synaptic function, though its role in MARK2-related disease is speculative at present.

Another important aspect of MARK2’s broader biology is its involvement in tau phosphorylation and neurodegeneration. The Nature review notes that “MARK2 is involved in the excessive phosphorylation of tau, thus influencing neurodegeneration,” and that it participates in regulation of neurofibrillary tangle assembly.[4][9] In Alzheimer disease models, hyperactive MARK2 can contribute to tau pathology, whereas in MRD76, haploinsufficiency may shift tau phosphorylation patterns in the opposite direction. The net effect on tau and potential long-term neurodegenerative risk in MRD76 is unknown, and there is no evidence to date that individuals with

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 45 |
| Terms named correctly | 37 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000045` (1 mention) - the report calls it "Severe speech and language impairment"; HP calls it **Abnormal scrotum morphology**
- `HP:0000389` (1 mention) - the report calls it "Dysplastic ears"; HP calls it **Chronic otitis media**
- `GO:0045184` (1 mention) - the report calls it "establishment or maintenance of cell polarity"; GO calls it **establishment of protein localization**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000708` (1 mention) - the report calls it "Abnormality of behavior"; HP calls it **Atypical behavior**
- `GO:0050317` (1 mention) - the report calls it "tau-protein kinase activity"; GO calls it **tagatose kinase activity**
- `GO:0007010` (2 mentions) - the report calls it "microtubule cytoskeleton organization"; GO calls it **cytoskeleton organization**
- `GO:0042127` (1 mention) - the report calls it "regulation of cell proliferation"; GO calls it **regulation of cell population proliferation**, and lists "regulation of cell proliferation" among its other names
- `GO:0060079` (1 mention) - the report calls it "regulation of excitatory postsynaptic potential"; GO calls it **excitatory postsynaptic potential**, and lists "regulation of excitatory post-synaptic membrane potential" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0016055` - called "Wnt receptor signaling pathway", "Wnt signaling pathway"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.