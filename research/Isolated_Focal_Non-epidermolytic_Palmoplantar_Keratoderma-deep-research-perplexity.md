---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T14:37:42.488875'
end_time: '2026-10-15T14:41:33.604565'
duration_seconds: 231.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Isolated Focal Non-epidermolytic Palmoplantar Keratoderma
  mondo_id: MONDO:0014622
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
citation_count: 51
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 2
  off_topic: 1
  off_topic_references:
  - DOI:10.1111/ddg.150_12930
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 41
  verified: 35
  not_found: 0
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 14
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014622
    reported_labels:
    - MONDO
    ontology_label: isolated focal non-epidermolytic palmoplantar keratoderma
  - term_id: DOID:0111711
    reported_labels:
    - Disease Ontology
    ontology_label: focal nonepidermolytic palmoplantar keratoderma 2
  - term_id: GO:0005887
    reported_labels:
    - Integral component of plasma membrane
    ontology_label: GO_0005887
  - term_id: UBERON:0001514
    reported_labels:
    - Palmar skin
    ontology_label: descending aorta
  - term_id: UBERON:0001516
    reported_labels:
    - Plantar skin
    ontology_label: abdominal aorta
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0005887
    ontology_label: GO_0005887
    replaced_by: GO:0005886
  unresolvable_prefixes:
  - ORPHA
  - OMIA
  - MGI
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isolated Focal Non-epidermolytic Palmoplantar Keratoderma
- **MONDO ID:** MONDO:0014622 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Isolated Focal Non-epidermolytic Palmoplantar Keratoderma** covering all of the
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

# Isolated Focal Non-epidermolytic Palmoplantar Keratoderma  
**Disease-knowledge-base research report — evidence reviewed through 15 October 2026**

## Executive summary and scope clarification

**Isolated focal non-epidermolytic palmoplantar keratoderma corresponding specifically to MONDO:0014622 is FNEPPK2, OMIM 616400, an extremely rare autosomal-dominant disorder caused by activating germline variants in *TRPV3*.** It produces localized hyperkeratotic plaques on palmoplantar pressure/friction sites without histologic epidermolysis or the extensive periorificial, hair, nail, and mutilating manifestations of classic Olmsted syndrome. The defining report identified heterozygous *TRPV3* NM_145068.4:c.1739A>C, p.(Gln580Pro), rs786205869 in a Chinese father and son; the variant arose de novo in the father and was inherited by his son. Functional assays showed increased intracellular Ca²⁺, supporting gain of function (GOF) (PMID: **25285920**). [79][106]

A terminology warning is essential:

- **MONDO:0014622 / OMIM 616400 / FNEPPK2** denotes the *TRPV3*-related condition requested here. [18][20]
- **OMIM 613000 / FNEPPK1** is a clinically overlapping but distinct *KRT16*-related disorder. [21]
- **OMIM 615735** is focal-or-diffuse non-epidermolytic PPK with plantar blistering due chiefly to *KRT6C*. [10][17]
- Clinical literature sometimes uses “focal non-epidermolytic PPK” for this broader phenotype group, including *KRT16*, *KRT6C*, *DSG1*, and *TRPV3*. Those data should not automatically be assigned to MONDO:0014622. [50][424]

Evidence for the precise MONDO entity remains sparse: the canonical disease–gene assignment rests principally on one father–son family, supplemented by a 2020 report titled “Mutation in *TRPV3* causes painful focal plantar keratoderma” (PMID: **32314439**) whose PubMed record has no abstract. [83][121]

---

## 1. Disease information

### 1.1 Definition

Isolated FNEPPK2 is a hereditary keratinization disorder characterized by **focal, patchy hyperkeratosis of the palms and soles**, rather than uniform involvement of the entire palmoplantar surface. “Non-epidermolytic” means that biopsy does not show the keratinocyte cytolysis and tonofilament clumping typical of epidermolytic PPK. Orphanet describes it as “a rare hereditary palmoplantar keratoderma characterized by focal hyperkeratotic lesions on the palms and soles.” [16]

The canonical *TRPV3* family had focal PPK “with no other abnormalities,” distinguishing the mild isolated phenotype from classic TRPV3-related Olmsted syndrome. [79]

### 1.2 Identifiers and synonyms

| Resource | Identifier/name | Notes and URL |
|---|---|---|
| MONDO | **MONDO:0014622** | Isolated focal non-epidermolytic palmoplantar keratoderma; https://monarchinitiative.org/MONDO:0014622 [20] |
| OMIM | **616400** | Palmoplantar keratoderma, nonepidermolytic, focal 2; FNEPPK2; https://omim.org/entry/616400 [118] |
| Orphanet | **ORPHA:448264** | https://www.orpha.net/en/disease/detail/448264 [16] |
| Disease Ontology | **DOID:0111711** | Listed in OMIM clinical synopsis. [227] |
| MedGen | **C4225339**, UID 895056 | https://www.ncbi.nlm.nih.gov/medgen/895056 [18] |
| MeSH | **D007645**, Keratoderma, Palmoplantar | Broad parent descriptor; no dedicated focal-TRPV3 MeSH term. [212] |
| SNOMED CT | **706885006**, palmoplantar keratoderma | Broad clinical concept; a dedicated FNEPPK2 code was not identified. [406] |
| ICD-10 | **Q82.8**, other specified congenital malformations of skin | Common umbrella code for hereditary PPK; not specific to FNEPPK2. [216][217] |
| ICD-11 | **EC20.3Z**, other specified hereditary palmoplantar keratoderma | Best-fitting umbrella category; no uniquely indexed FNEPPK2 code was identified. [216] |

**Preferred synonyms**

| Synonym | Scope |
|---|---|
| Palmoplantar keratoderma, nonepidermolytic, focal 2 | Exact OMIM phenotype |
| FNEPPK2 | Exact abbreviation |
| Isolated focal non-epidermolytic palmoplantar keratoderma | Orphanet/MONDO preferred label |
| Focal non-epidermolytic palmoplantar keratoderma due to *TRPV3* | Unambiguous descriptive label |
| Focal plantar keratoderma due to *TRPV3* | Used in later clinical literature, but may describe a narrower plantar-only presentation |

“Hereditary painful callosities,” “keratosis palmoplantaris nummularis,” and generic “focal PPK” may instead refer to *KRT6C*- or *KRT16*-related disease and should not be treated as exact synonyms without molecular confirmation. [424]

### 1.3 Evidence provenance

The entry is based on:

1. **Individual-level human case data:** principally a Chinese father and son, with segregation, biopsy, omics, and in-vitro functional studies (PMID 25285920).
2. **A later individual case report:** PMID 32314439.
3. **Aggregated disease-level resources:** OMIM, Orphanet, MONDO, MedGen, ClinVar and expert gene panels.

It is **not** based on population EHR aggregation or a disease registry.

---

## 2. Etiology

### 2.1 Causal factor

The established cause is a **heterozygous germline activating missense variant in *TRPV3***. In the defining family, p.Gln580Pro arose de novo in the father and was transmitted to his affected son, demonstrating vertical autosomal-dominant transmission. Transfected HEK293T cells expressing mutant TRPV3 had increased intracellular Ca²⁺ relative to wild type. [46][93]

*TRPV3* encodes a warmth-sensitive, Ca²⁺-permeable, nonselective cation channel expressed especially in keratinocytes. It forms a fourfold-symmetric tetramer, with each subunit containing six transmembrane helices. [369][370]

### 2.2 Risk and protective factors

| Factor class | Current evidence |
|---|---|
| Causal genetic factor | Heterozygous GOF *TRPV3* variant; strongest exact-disease evidence is p.Gln580Pro. |
| Family history | An affected parent confers a theoretical 50% transmission probability for each pregnancy, assuming heterozygosity and full germline representation. |
| De novo occurrence | Demonstrated in the father of the canonical family. [83] |
| Mechanical pressure/friction | Likely determines lesion localization and severity; focal PPK generally arises over mechanically stressed pressure points. [409][424] |
| Warmth | Biologically plausible symptom modifier because TRPV3 is warmth-activated, but disease-specific quantitative exposure data are unavailable. [64][404] |
| Age/sex/ethnicity | No validated susceptibility effect. Two affected males in one Chinese family cannot establish male predominance or an ethnic association. |
| Toxins, smoking, alcohol, diet, occupation | No evidence that these cause the Mendelian disorder. High-friction occupations may aggravate established lesions. |
| Infectious agents | None are causal. Fissures may permit secondary bacterial or fungal infection. |
| Protective genetic variants/modifiers | None established. |
| Protective environmental factors | No controlled evidence; reducing repetitive pressure/friction is rational symptomatic prevention, not prevention of the genotype. |

### 2.3 Gene–environment interaction

The best-supported model is that **constitutive genetically enhanced TRPV3 activity creates a susceptible epidermis, while repetitive pressure, friction, weight bearing, and possibly warmth amplify local calcium signaling, keratinocyte turnover, pain, and callus formation**. The localization mechanism is biologically plausible but has not been experimentally demonstrated specifically for p.Gln580Pro.

There are no published FNEPPK2 GWAS, formal interaction analyses, susceptibility loci, or validated modifier genes.

---

## 3. Phenotypes

Because the defining family contains only two affected individuals, percentages would be misleading. “2/2” below describes that family, not a population frequency.

| Phenotype | Type and characteristics | Frequency/evidence | Suggested HPO |
|---|---|---|---|
| Focal/patchy palmoplantar hyperkeratosis | Physical sign; localized plaques on palms and soles rather than diffuse disease; chronic | Defining feature, 2/2 canonical cases | **HP:0007497** focal friction-related palmoplantar hyperkeratosis; **HP:0000982** palmoplantar keratoderma [406][409] |
| Non-epidermolytic PPK | Histopathologic sign; absence of epidermolytic degeneration | Defining diagnostic qualifier | **HP:0007404** nonepidermolytic palmoplantar hyperkeratosis [405] |
| Prominent hyperkeratosis/acanthosis | Biopsy sign: thick stratum corneum and stratum spinosum | Reported in defining disease description | HP:0000962 hyperkeratosis; HP:0032243 acanthosis, if supported locally |
| Reduced stratum granulosum | Histologic abnormality | Reported | No precise widely used HPO term; encode as pathology text |
| Suprabasal cell disadhesion | Histologic sign | Reported | HP:0008066 abnormal blistering of skin only if clinically present; otherwise textual annotation |
| Elongated rete ridges | Histologic sign | Reported | No specific HPO term |
| Sparse dermal lymphocytes | Histologic/laboratory pathology finding | Reported | No specific disease-level HPO term |
| Palmoplantar pain | Symptom, especially in the 2020 “painful focal plantar” report; potentially pressure- or warmth-provoked | Not quantified for canonical family | **HP:0012531** pain; consider HP:0025538 plantar pain |
| Fissuring | Physical manifestation common to focal PPK, potentially painful and infection-prone | Not established in every FNEPPK2 patient | **HP:0010646** skin fissures |
| Erythromelalgia-like warmth/pain | Possible allelic TRPV3 manifestation, better documented in atypical Olmsted phenotypes | Not part of the defining isolated family | HP:0032147 erythromelalgia |
| Absence of major extracutaneous abnormalities | Negative phenotype: no classic periorificial plaques, alopecia, mutilation, or major nail changes in the defining family | 2/2 defining cases | Record as explicit negative HPO annotations |

Orphanet’s disease-level pathology includes “prominent hyperkeratosis, thickened stratum spinosum with reduced stratum granulosum, disadhesion of cells in the suprabasal layers, elongation of rete ridges, and sparse lymphocyte infiltration in the dermis.” [47]

### Onset, severity, and progression

- The exact age at onset for both defining patients was not available in the PubMed record, which has **no abstract**.
- The father retained only focal PPK at age 37, supporting a relatively mild, non-mutilating course for p.Gln580Pro. [139]
- Focal hereditary PPK as a broader category usually begins in childhood and may become painful after mechanical stress, but this must be tagged as **phenotype-group evidence**, not exact-disease frequency. [50]
- A 2020 report establishes that some *TRPV3*-related focal plantar disease is painful (PMID 32314439), but its publicly accessible record does not disclose the exact variant or complete clinical course. [121][196]

### Quality-of-life impact

No FNEPPK2-specific validated DLQI, EQ-5D, SF-36, or PROMIS study exists. Expected burden includes pain on walking, reduced mobility, difficulty standing or working, impaired grip if palms are affected, shoe intolerance, and time spent on debridement and topical treatment.

For context only, a mixed palmoplantar-dermatosis study reported mean DLQI **8.53** and CDLQI **8.28** in its PPK subgroup, but this is not an FNEPPK2-specific estimate. [326]

---

## 4. Genetic and molecular information

### 4.1 Causal gene

| Item | Annotation |
|---|---|
| Gene | ***TRPV3***, transient receptor potential cation channel subfamily V member 3 |
| HGNC | **HGNC:18084** |
| NCBI Gene | **162514** |
| Ensembl | **ENSG00000167723** |
| UniProt | **Q8NET8** |
| OMIM gene | **607066** |
| Location | **17p13.2**; GRCh38 chr17:3,510,502–3,557,812 |
| Protein | Ca²⁺-permeable nonselective cation channel; homotetramer with six transmembrane helices per monomer |
| Primary cell expression | Epidermal and follicular keratinocytes; lower-level expression in sensory and other tissues |

Identifiers and chromosomal localization are supported by NCBI/Alliance/UniProt-linked resources. [362][365][374]

### 4.2 Pathogenic variant

| Variant field | p.Gln580Pro |
|---|---|
| Transcript | NM_145068.4 |
| HGVS coding | **c.1739A>C** |
| Protein | **p.(Gln580Pro), Q580P** |
| dbSNP | **rs786205869** |
| Genomic description in original report | GRCh37 chr17:3,427,496 T>G, reflecting the reverse-strand orientation |
| Exon/domain | Exon 13; cytosolic S4–S5 linker |
| Variant class | Missense SNV |
| Origin | Germline; de novo in father, inherited by son |
| Inheritance | Autosomal dominant |
| Functional consequence | Gain of function, increased intracellular Ca²⁺ |
| ClinVar status | Reported as pathogenic in current aggregated variant resources |
| OMIM allelic variant | 607066.0005 |
| Population frequency | No credible common-population frequency was identified; the rarity, de novo observation, segregation and functional effect support pathogenicity. A current exact gnomAD count should be rechecked before production ingestion. |
| Evidence level | Limited human case count but supportive segregation, de novo occurrence, functional assay, transcriptomics, proteomics and immunohistochemistry |

The variant lies at a conserved residue in the linker between transmembrane segments S4 and S5, a region central to channel gating. [93][113]

### 4.3 Other variants and allelic disorders

Other activating *TRPV3* variants—such as p.Gly573Cys, p.Gly573Ser, p.Trp692Gly, p.Leu673Phe and others—usually produce **Olmsted syndrome or an Olmsted-like phenotype**, not necessarily isolated FNEPPK2. Severe variants are associated with mutilating PPK, periorificial plaques, alopecia, warmth-induced pain and pruritus. p.Gln580Pro has a comparatively mild focal phenotype. [167][180]

Accordingly, a laboratory finding of a different *TRPV3* variant should be interpreted against the complete allelic spectrum rather than automatically assigned to MONDO:0014622.

### 4.4 Modifier, epigenetic and chromosomal findings

| Category | Finding |
|---|---|
| Modifier genes | None validated for FNEPPK2 |
| Epigenetic signature | None reported |
| DNA methylation/histone changes | No disease-specific studies |
| Copy-number/structural variants | None established |
| Aneuploidy/translocation/inversion | Not implicated |
| Somatic mosaicism | Not reported for *TRPV3*-FNEPPK2; somatic mosaicism is described in some *KRT16* disorders but is a different entity |
| Anticipation | Not reported and not expected for a missense channelopathy |

---

## 5. Environmental and lifestyle information

| Domain | Assessment |
|---|---|
| Mechanical exposure | Pressure, friction, prolonged walking, standing, and repetitive hand use are expected to aggravate localization and pain. |
| Temperature | Warmth is a plausible trigger because TRPV3 activation begins in the innocuous-warm range; disease-specific challenge studies are lacking. [64][440] |
| Humidity/sweating | May promote maceration, fissuring or secondary infection, but no FNEPPK2-specific evidence exists. |
| Smoking/alcohol/diet/exercise | No causal associations. Exercise can mechanically aggravate plantar disease. |
| Occupational factors | Manual labor, prolonged standing and restrictive footwear may worsen manifestations but do not cause the Mendelian disorder. |
| Toxins/radiation/pollution | Not implicated. |
| Infectious agents | No initiating pathogen. Bacteria or fungi may secondarily colonize fissures. |
| Drugs | No drug is known to induce inherited FNEPPK2; acquired drug-induced PPK is a differential diagnosis. |

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **Heterozygous germline *TRPV3* p.Gln580Pro alters the S4–S5 channel-gating linker, which leads to increased channel activity.**
2. **Increased TRPV3 activity leads to excessive Ca²⁺ influx and elevated intracellular Ca²⁺ in epidermal keratinocytes**, demonstrated in mutant-transfected HEK293T cells.
3. **Abnormal Ca²⁺ signaling leads to dysregulation of keratinocyte proliferation, terminal differentiation and survival**, supported by lesional transcriptomic/proteomic data and keratin-marker immunohistochemistry.
4. **Dysregulated differentiation leads to persistence/expansion of KRT14-positive basal-like cells and reduced KRT10-positive differentiated suprabasal cells.**
5. **The differentiation imbalance leads to reduced expression of proteins involved in terminal differentiation, tight junctions, gap junctions and desmosomes, while proliferation- and cell-death-associated proteins increase.**
6. **Impaired differentiation and intercellular adhesion lead to acanthosis, suprabasal disadhesion, altered granular-layer development and excessive cornified material.**
7. **Excess cornification leads to focal hyperkeratotic palmoplantar plaques.**
8. **Mechanical load at palmar/plantar pressure points likely amplifies local injury and repair signaling, resulting in focal distribution**—this localization step is inferred rather than directly demonstrated for p.Gln580Pro.
9. **Branch—pain:** hyperkeratosis/fissuring plus keratinocyte release of ATP, inflammatory mediators and neuroactive substances may activate cutaneous nociceptive pathways, leading to pressure- or warmth-provoked pain; this branch is supported by broader TRPV3 evidence but not fully demonstrated in FNEPPK2.
10. **Branch—inflammation:** cell stress/death and barrier disruption may produce sparse dermal lymphocytic inflammation; marked systemic immune activation is not a defining feature.

The original primary report concluded from functional and omics findings that p.Gln580Pro disrupts the balance between keratinocyte proliferation and differentiation (PMID 25285920). [162]

### 6.2 Molecular and cellular detail

Normal TRPV3 participates in epidermal calcium signaling and can form a functional complex with TGF-α/EGFR. Activation influences EGFR signaling and calcium-dependent transglutaminase activity, thereby coordinating proliferation, terminal differentiation, cornified-envelope formation and barrier repair. [142][275]

In the p.Gln580Pro lesions:

- differentiation and cell-junction proteins were reduced;
- proliferation and cell-death proteins were increased;
- KRT14 staining extended through a broader basal layer;
- KRT10 staining was weaker in the spinous layer. [137][138]

Potential downstream pathways supported principally by broader TRPV3 studies include:

- Ca²⁺/calmodulin and CaMKII signaling;
- TGF-α/ADAM17/EGFR signaling;
- PI3K–AKT and NF-κB signaling;
- calcium-dependent transglutaminase-1 activity;
- ATP-mediated signaling to sensory neurons;
- apoptosis and inflammatory mediator release.

EGFR/mTORC2/NF-κB involvement is best regarded as broader hyperactive-TRPV3 biology, not yet directly established in p.Gln580Pro FNEPPK2. [61]

### 6.3 Suggested GO and Cell Ontology annotations

| Biological entity/process | Suggested ontology term |
|---|---|
| Keratinocyte | **CL:0000312** |
| Epidermal keratinocyte | **CL:4052061** |
| Suprabasal keratinocyte | **CL:4033013** [442] |
| Calcium channel activity | **GO:0005262** |
| Ion channel activity | **GO:0005216** |
| Plasma membrane | **GO:0005886** |
| Integral component of plasma membrane | **GO:0005887** |
| Calcium-ion transport | **GO:0006816** |
| Response to temperature stimulus | **GO:0009266** |
| Keratinocyte differentiation | **GO:0030216** |
| Positive regulation of keratinocyte differentiation | **GO:0045618** |
| Cell population proliferation | **GO:0008283** |
| Apoptotic process | **GO:0006915** |
| Cell–cell adhesion | **GO:0098609** |
| Desmosome | **GO:0030057** |
| Tight junction | **GO:0070160** |
| Cornification | **GO:0070268** |
| Epidermis development | **GO:0008544** |

Core TRPV3 annotations include calcium-channel activity and localization to plasma membrane/lysosome. [437][438]

### 6.4 Molecular profiling and advanced technologies

| Modality | Disease-specific evidence |
|---|---|
| Transcriptomics | Performed in the defining study; altered keratinocyte proliferation/differentiation transcriptional programs |
| Proteomics | Performed; reduced differentiation/junction proteins and increased proliferation/cell-death proteins |
| Immunohistochemistry | Broader KRT14-positive layer and weaker KRT10 expression |
| Metabolomics/lipidomics | No FNEPPK2-specific data |
| Single-cell RNA sequencing | No disease-specific study |
| Spatial transcriptomics | None |
| Patient-derived organoids/iPSCs | None reported |
| CRISPR/RNAi screens | None specific to FNEPPK2 |
| Structural biology | General TRPV3 cryo-EM structures exist; a recent structure database lists human TRPV3-Q580P, but this is not yet a clinical diagnostic assay. [113] |

---

## 7. Anatomical structures affected

| Level | Affected structure | Suggested ontology |
|---|---|---|
| Organ | Skin | UBERON:0002097 |
| Primary site | Palmar and plantar skin | **UBERON:0013776**, skin of palmar/plantar part of autopod |
| Palm | Palmar skin | **UBERON:0001514** |
| Sole | Plantar skin | **UBERON:0001516** |
| Tissue | Keratinized stratified squamous epithelium/epidermis | UBERON:0001003, epidermis |
| Epidermal layers | Basal, spinous, granular and cornified layers | Textual or layer-specific UBERON terms |
| Main cell | Keratinocyte | CL:0000312 |
| Secondary cells | Sparse dermal lymphocytes; sensory nerve endings potentially involved in pain | CL:0000542 lymphocyte; nociceptor annotations where demonstrated |
| Subcellular | Plasma membrane TRPV3 channel | GO:0005886 |
| Secondary subcellular systems | Cell junctions/desmosomes/tight junctions | GO:0030057; GO:0070160 |
| Lateralization | Generally bilateral/symmetric is expected for inherited PPK, but exact lateralization frequency is unavailable |

There is no established internal-organ involvement in isolated FNEPPK2.

---

## 8. Temporal development

| Feature | Current understanding |
|---|---|
| Onset | Exact onset in the canonical patients is not stated in the accessible PubMed record. Broader hereditary focal PPK commonly begins in infancy or childhood. |
| Pattern | Chronic and insidious rather than acute |
| Early stage | Localized thickening at pressure/friction sites |
| Intermediate stage | Increasing compact hyperkeratosis, potentially pain or fissuring |
| Advanced stage | Persistent painful plaques may impair walking or grip; mutilation is not characteristic of the defining p.Gln580Pro phenotype |
| Progression | Mild/slow or mechanically fluctuating; father remained focal at age 37 [139] |
| Duration | Presumed lifelong |
| Remission | No spontaneous-remission data; symptomatic reduction requires ongoing treatment |
| Critical periods | Early pressure management may reduce secondary callus, pain and fissures, but no formally validated window exists |

No accepted staging system or longitudinal natural-history cohort exists.

---

## 9. Inheritance and population

### 9.1 Inheritance

| Characteristic | Assessment |
|---|---|
| Mode | Autosomal dominant, monoallelic |
| Recurrence risk | 50% for offspring of a heterozygous affected person |
| De novo risk | Demonstrated; p.Gln580Pro arose de novo in the father |
| Penetrance | Both known carriers in the defining family were affected, but the sample is insufficient to establish complete penetrance |
| Expressivity | Likely variable across *TRPV3* alleles; p.Gln580Pro is mild compared with classic Olmsted variants |
| Anticipation | Not reported |
| Germline mosaicism | Not reported; low residual recurrence risk after an apparently de novo case cannot be excluded |
| Consanguinity | Not relevant to the canonical dominant family |
| Founder effect | None established |
| Carrier frequency | Unknown; for a dominant disorder, “carrier” generally means an at-risk heterozygous individual |

### 9.2 Epidemiology

No defensible prevalence or incidence estimate exists for the exact MONDO entity. Orphanet labels it rare but does not provide a numeric estimate. [376]

The defining OMIM evidence originally involved one Chinese family with two affected males. Consequently:

- prevalence per 100,000: **unknown**;
- annual incidence: **unknown**;
- sex ratio: **unknown**;
- geographic or ethnic enrichment: **not established**;
- age distribution: **unknown**.

Precise prevalence estimates are generally unavailable for hereditary PPKs and mild cases may be underdiagnosed. [383]

For context, a 2024 Danish PPK cohort included 142 participants from 76 families and achieved a molecular diagnosis in 63/76 families (**83%**), but it did not identify *TRPV3* among the reported causal genes and therefore supplies diagnostic-context—not FNEPPK2 prevalence—data. The cohort was 63% female, with median age 52 years, range 18–92 (published online 4 December 2024; DOI 10.1001/jamadermatol.2024.4824). [331][332]

---

## 10. Diagnostics

### 10.1 Recommended workflow

1. **Clinical morphology:** document focal versus diffuse or punctate lesions; palmar/plantar distribution; pressure dependence; pain, blistering and fissures.
2. **History:** childhood onset, affected relatives, de novo presentation, occupational friction, medication exposure, infection and systemic symptoms.
3. **Examine extracutaneous sites:** nails, hair, teeth, oral/periorificial mucosa, joints, hearing, heart and esophagus to detect syndromic mimics.
4. **Exclude acquired causes:** fungal microscopy/culture, patch testing when dermatitis is suspected, and selected laboratory studies guided by history.
5. **Skin biopsy:** confirm non-epidermolytic hyperkeratosis and assess acanthosis, granular-layer changes and cell adhesion.
6. **Molecular testing:** sequence a multigene hereditary PPK panel including *TRPV3*, *KRT16*, *KRT6C*, *KRT6A*, *KRT6B*, *KRT17*, *DSG1*, *DSP*, *KRT1*, *KRT9*, *AAGAB* and other phenotype-relevant genes.
7. **Segregation and variant interpretation:** confirm candidate variants by orthogonal testing and test parents/affected relatives.
8. **WES/WGS:** use when panel testing is negative, the phenotype is atypical, or structural/noncoding variants are suspected.

Histopathology and molecular testing are recommended because clinically similar PPKs can have different molecular causes. [421] A recent cohort used WES or WGS with an in-silico PPK panel, plus targeted Sanger testing, and achieved an 83% family-level diagnostic yield across PPKs. [425]

### 10.2 Test utility

| Test | Utility in FNEPPK2 |
|---|---|
| Targeted *TRPV3* sequencing | Appropriate when focal PPK is isolated and TRPV3 channelopathy is strongly suspected |
| Multigene PPK panel | Preferred first-line molecular test because of major phenotypic overlap |
| WES | Useful after negative panel testing or for atypical disease |
| WGS | Useful for unresolved cases, CNVs, noncoding variants and research discovery |
| CMA | Low expected yield for an isolated single-gene phenotype; consider only with developmental anomalies |
| Karyotype/FISH | Not routinely indicated |
| Mitochondrial testing | Not indicated |
| Repeat-expansion testing | Not indicated |
| RNA sequencing | Research/variant-resolution tool; not routine |
| Proteomics/metabolomics/liquid biopsy | No diagnostic role |
| Imaging/electrophysiology | Not routine unless symptoms suggest another disorder |

### 10.3 Histopathology

Expected findings are:

- prominent hyperkeratosis;
- thickened spinous layer/acanthosis;
- reduced granular layer;
- suprabasal disadhesion;
- elongated rete ridges;
- sparse dermal lymphocytes;
- absence of classic epidermolytic degeneration. [47]

### 10.4 Differential diagnosis

| Differential | Distinguishing features |
|---|---|
| *KRT16*-FNEPPK1, OMIM 613000 | Focal painful callosities at friction sites; may include follicular/orogenital keratosis; keratin structural defect rather than ion channel GOF |
| *KRT6C*-PPK, OMIM 615735 | Plantar-predominant focal/diffuse disease, painful blistering, minimal nail changes [17] |
| Pachyonychia congenita | Thickened/dystrophic nails, plantar pain, oral leukokeratosis; genes *KRT6A/B/C*, *KRT16*, *KRT17* |
| Olmsted syndrome | Severe progressive/mutilating PPK, periorificial plaques, alopecia, nail abnormalities, pseudoainhum, warmth-induced pain/pruritus |
| Striate PPK | Linear palmar keratosis along flexor surfaces; *DSG1*, *DSP* or *KRT1* |
| Punctate PPK | Numerous small discrete “raindrop” keratoses; frequently *AAGAB* |
| Epidermolytic PPK | Diffuse sharply demarcated PPK with epidermolytic histology; often *KRT9* or *KRT1* |
| Tylosis with esophageal cancer | Focal PPK plus oral/esophageal leukokeratosis and high esophageal SCC risk; *RHBDF2* |
| Acquired calluses/corns | Direct mechanical relationship, no Mendelian segregation, normal intervening skin |
| Tinea manuum/pedis | Positive fungal microscopy/culture |
| Palmoplantar psoriasis/eczema | Erythema, inflammation, scale, pruritus; biopsy/clinical course differs |
| Acquired paraneoplastic/drug-related PPK | Adult onset and temporal relationship to malignancy or medication |

### 10.5 Screening

- No population or newborn screening is recommended.
- **Cascade testing** is appropriate after identifying a familial pathogenic variant.
- Predictive testing of asymptomatic relatives should follow genetic counseling.
- Prenatal diagnosis and preimplantation genetic testing are technically possible once the familial variant is known.

---

## 11. Outcome and prognosis

| Outcome domain | Assessment |
|---|---|
| Survival | Expected to be normal for isolated FNEPPK2 |
| Life expectancy | No evidence of reduction |
| Disease-specific mortality | None reported |
| Malignancy risk | No established increased risk for isolated *TRPV3*-FNEPPK2; do not extrapolate the esophageal-cancer risk of *RHBDF2* tylosis |
| Chronic morbidity | Painful calluses, fissures, difficulty walking/standing, impaired hand function, footwear limitations |
| Complications | Secondary bacterial/fungal infection through fissures; altered gait and activity avoidance |
| Recovery | Genetic predisposition is lifelong; lesions can improve symptomatically but recurrence is expected |
| Prognostic factors | Mechanical load, lesion thickness, fissuring, pain and exact *TRPV3* allele |
| Molecular prognostic biomarkers | None validated |

The hereditary PPK treatment review concluded that hPPK is generally not life-threatening but can impair mobility and cause discomfort or intractable pain; evidence is dominated by case reports and small heterogeneous series rather than randomized trials. [318]

---

## 12. Treatment

### 12.1 Current standard care

No treatment is approved specifically for MONDO:0014622, and no curative therapy exists for hereditary PPK. [301]

| Treatment/intervention | Use and evidence | Important adverse effects/limitations | Suggested NCIT annotation |
|---|---|---|---|
| Emollients/occlusive moisturizers | First-line softening of compact keratin | Temporary effect; frequent application | Emollient Preparation |
| Urea | Topical humectant/keratolytic, commonly 10–40% depending on tolerance | Burning on fissured skin | Urea; Keratolytic Agent |
| Salicylic acid | Keratolytic, often around 5–10%; DermNet gives 6% as an example | Irritation; systemic salicylate risk if extensive/occluded, especially in children | Salicylic Acid |
| Lactic acid/ammonium lactate | Keratolytic and moisturizer | Stinging/irritation | Lactic Acid |
| Propylene glycol under occlusion | Softens hyperkeratosis | Irritant/contact dermatitis | Propylene Glycol |
| Mechanical paring/debridement | Reduces plaque thickness and focal pressure | Cuts, bleeding, infection if excessive | Debridement |
| Pressure redistribution | Cushioned footwear, orthotics, gloves, activity modification | Does not change molecular disease | Orthotic Device; Supportive Care |
| Topical retinoid | May reduce limited hyperkeratosis | Irritation; avoid during pregnancy | Retinoid |
| Calcipotriol | Occasionally used empirically | Irritation; limited evidence | Calcipotriol |
| Oral acitretin/isotretinoin | For severe refractory hyperkeratosis; responses vary | Teratogenicity, dryness, hyperlipidemia, hepatotoxicity; may increase fragility and pain | Acitretin; Isotretinoin |
| Antibiotic/antifungal therapy | Only for documented secondary infection | Organism/drug-specific adverse effects | Anti-Infective Agent |
| Analgesia | Individualized for painful lesions | Does not treat hyperkeratosis | Analgesic Agent |
| Surgery/excision/grafting | Rare, last-resort intervention | Recurrence, scarring and inconsistent outcomes | Surgical Procedure; Skin Grafting |

Mechanical debridement and topical urea, salicylic acid or lactic acid are standard first-line measures. Oral retinoids may improve hyperkeratosis, but increased skin fragility can limit their use. [305] Topical treatment must generally be continued because it reduces manifestations rather than curing the disorder. [310]

### 12.2 Mechanism-targeted and experimental therapy

#### EGFR inhibition

In three patients with severe *TRPV3*-related Olmsted syndrome—not isolated FNEPPK2—erlotinib produced disappearance of hyperkeratosis and pain within three months, sustained during continued treatment. This supports the relevance of TRPV3–EGFR coupling but remains off-label and potentially disproportionate for mild focal disease (PMCID PMC6990711). [201]

Erlotinib can cause acneiform rash, diarrhea, paronychia, hepatic toxicity and rare interstitial lung disease; specialist risk–benefit review is essential.

#### Direct TRPV3 inhibitors

Topical KM-001, a TRPV3 inhibitor, has been studied in pachyonychia congenita and punctate PPK1—not FNEPPK2—in phase 1 studies NCT05435638 and NCT05956314. Company-reported 2024 results described improvement in at least one prespecified parameter in 88% of eight UK completers and 86% of seven Israeli completers, with only mild treatment-emergent events; these small, open-label results cannot establish efficacy in *TRPV3*-FNEPPK2. [289][297]

As of the review date:

- no interventional trial was identified as specifically enrolling MONDO:0014622; [291]
- oral selective TRPV3 inhibitors are under development for Olmsted syndrome and severe keratodermas;
- no gene, RNA or cell therapy has reached clinical testing for FNEPPK2.

### 12.3 Practical algorithm

1. Reduce friction/pressure and optimize footwear.
2. Daily emollient plus urea, lactic acid or cautious salicylic acid.
3. Regular professional or carefully supervised paring.
4. Treat fissures and confirmed infection.
5. Add topical retinoid or calcipotriol for refractory limited plaques.
6. Consider low-dose systemic retinoid only for substantial disability.
7. For severe molecularly confirmed *TRPV3* disease, discuss specialist access to trials or exceptional targeted therapy; erlotinib evidence comes from severe Olmsted syndrome, not isolated FNEPPK2.

No FNEPPK2-specific pharmacogenomic guidance exists.

---

## 13. Prevention

| Prevention level | Intervention |
|---|---|
| Primary prevention | The genotype cannot be prevented after conception. Reproductive options include donor gametes, prenatal testing and preimplantation genetic testing for a known familial variant. |
| Secondary prevention | Early dermatologic and genetic evaluation of symptomatic relatives; cascade variant testing |
| Tertiary prevention | Reduce friction/pressure, maintain skin hydration, pare thick keratin safely, treat fissures early, and monitor for secondary infection |
| Behavioral | Cushioned shoes, moisture-wicking socks, gloves for repetitive manual work, gradual activity adjustment |
| Environmental | Avoid poorly fitting footwear and repetitive high-pressure tasks where feasible |
| Counseling | Explain autosomal-dominant 50% transmission risk, possibility of de novo occurrence, uncertain penetrance estimates and allelic overlap with Olmsted syndrome |
| Immunization/prophylaxis | No disease-specific vaccine or prophylactic medication |
| Public health | No population screening program is justified by present evidence |

---

## 14. Other species and naturally occurring disease

No natural animal disorder caused by the exact human *TRPV3* p.Gln580Pro variant has been established. The best natural comparative disease is **KRT16-related FNEPPK1 in dogs**, which models a related but molecularly distinct human focal PPK.

| Species/model | Gene and variant | Phenotype and relevance | Limitations |
|---|---|---|---|
| Dog, *Canis lupus familiaris*; NCBI Taxon 9615; Dogue de Bordeaux | Canine *KRT16*, NCBI Gene 490978; c.[1147_1148delinsCGGA;1165del], p.(Val383ArgfsTer11); OMIA:002088-9615 | Painful focal non-epidermolytic footpad hyperkeratosis, fissures, infection and lameness; natural large-animal model of human FNEPPK1; PMID **25521457** | Autosomal recessive in dogs and *KRT16*-based, whereas human MONDO:0014622 is dominant *TRPV3*-GOF disease [256][257] |
| DS-Nh mouse, *Mus musculus*; Taxon 10090 | *Trpv3* p.Gly573Ser GOF | Constitutive channel activity, hyperkeratosis, thickened epidermal layers, abnormal hair and dermatitis; models hyperactive TRPV3 biology | Does not reproduce isolated palmoplantar localization; mice lack human-like palms/soles [271][274] |
| WBN/Kob-Ht rat, *Rattus norvegicus*; Taxon 10116 | *Trpv3* p.Gly573Cys GOF | Hairlessness and dermatitis-like disease | Not a focal PPK model [271] |
| *Trpv3*-knockout mouse | Loss of function | Defective terminal differentiation, reduced cornified-envelope density and impaired barrier | Opposite direction of effect from p.Gln580Pro GOF, useful mainly for normal gene function [278][281] |

There is no zoonotic potential or cross-species transmission; these are inherited, noninfectious disorders.

---

## 15. Model organisms and experimental systems

| Model type | Model | Findings/applications | Principal limitation |
|---|---|---|---|
| Human clinical | p.Gln580Pro father and son | Defines genotype–phenotype relationship and mild focal presentation | Only two canonical affected people |
| Heterologous cellular | HEK293T cells expressing wild-type or Q580P TRPV3 | Mutant increased intracellular Ca²⁺, establishing GOF | Non-keratinocyte cell line |
| Human tissue | Lesional/nonlesional skin transcriptomics, proteomics and IHC | Differentiation/junction proteins down; proliferation/cell-death proteins up; KRT14 expanded and KRT10 reduced | Tiny sample size and no independent cohort |
| Spontaneous GOF mouse | DS-Nh *Trpv3* G573S | Channel hyperactivity, epidermal hyperplasia, hyperkeratosis, itch/dermatitis and altered sensory behavior | Allele and tissue distribution differ from FNEPPK2 |
| Spontaneous GOF rat | WBN/Kob-Ht G573C | Confirms conserved GOF effect | Hair/dermatitis-dominant phenotype |
| Knockout mouse | *Trpv3*−/− | Establishes requirement for terminal differentiation and barrier formation | Models loss rather than gain of function |
| Natural canine model | Recessive *KRT16* Dogue de Bordeaux | Footpad hyperkeratosis and fissuring closely mimic focal mechanical disease | Different gene and inheritance |
| Structural model | Cryo-EM/biophysical TRPV3 systems | Channel gating, S4–S5 linker function and antagonist design | Structural effects do not alone predict human severity |
| Future model | Patient-derived keratinocytes, organotypic palmoplantar epidermis or CRISPR Q580P knock-in | Could test pressure, temperature, EGFR and direct TRPV3 inhibitors | No validated FNEPPK2-specific platform yet reported |

Suggested resources are MGI (**MGI:2181407** for mouse *Trpv3*), IMSR for mouse strains, OMIA for the canine disorder, and NCBI Gene/Alliance for orthology. MGI currently links *Trpv3* to human FNEPPK2 but does not list a mouse model that precisely reproduces the human focal phenotype. [58]

---

## Recent developments and current expert interpretation

### 2023–2024 developments

1. A 2023 review emphasized that TRPV3 is a nonselective cation channel highly expressed in keratinocytes and specifically noted that p.Gln580Pro produces much milder focal PPK than the severe Olmsted variants (published 10 March 2023). [67][167]
2. A 2023 ion-channel/pain review connected TRPV3 variants to painful neuropathic and erythromelalgia-like phenotypes, supporting neurocutaneous mechanisms but not providing FNEPPK2-specific prevalence data. [192]
3. A July 2024 review highlighted the reciprocal positive-feedback relationship between TRPV3 calcium signaling and TGF-α/EGFR pathways. [71]
4. A December 2024 review of TRPV3-related Olmsted syndrome summarized genotype–phenotype correlations and the p.Gln580Pro omics findings. It reported that variants with stronger gating effects generally produce more severe keratinization than p.Gln580Pro. [63][180]
5. The 2024 Danish PPK cohort demonstrated the practical value of deep phenotyping plus WES/WGS panels, with an 83% family-level diagnostic yield, although no *TRPV3* diagnosis was reported. [331]

### Expert synthesis

Current evidence supports treating MONDO:0014622 as the **mild focal end of the TRPV3 gain-of-function channelopathy spectrum**, while keeping it distinct from classic Olmsted syndrome for clinical coding. The strongest mechanistic evidence is the combination of:

- de novo occurrence and parent-to-child segregation;
- increased mutant-channel calcium activity;
- altered lesional differentiation and junctional programs;
- concordant histology and keratin-marker abnormalities.

The principal uncertainties are the very small number of molecularly characterized patients, unknown penetrance and epidemiology, absence of prospective natural-history data, and lack of treatment trials specific to FNEPPK2.

---

## Primary evidence quotations

The two principal disease-specific publications are letters with **no PubMed abstract**, so an exact abstract quotation is not available. Their titles provide the most direct author-level statements:

- He et al., *J Invest Dermatol*, epub 6 October 2014; print March 2015, PMID **25285920**, DOI **10.1038/jid.2014.429**: **“A gain-of-function mutation in TRPV3 causes focal palmoplantar keratoderma in a Chinese family.”** [79]
- Peters et al., *J Eur Acad Dermatol Venereol*, first published 20 April 2020, PMID **32314439**, DOI **10.1111/jdv.16498**: **“Mutation in TRPV3 causes painful focal plantar keratoderma.”** [121][390]

A review-level treatment summary states: **“No specific or curative therapy exists for hereditary palmoplantar keratoderma”** and notes potentially profound quality-of-life impairment, pain and functional limitation. [301]

---

## Knowledge-base curation recommendations

1. Use **MONDO:0014622 → OMIM:616400 → ORPHA:448264 → *TRPV3*** as the primary mapping.
2. Store p.Gln580Pro as the canonical disease variant:
   - NM_145068.4:c.1739A>C;
   - NP_659529.1:p.(Gln580Pro), subject to transcript verification;
   - rs786205869;
   - germline, heterozygous, autosomal dominant, GOF.
3. Do **not** merge OMIM 613000/*KRT16* or OMIM 615735/*KRT6C* into this entry; represent them as differential/phenotypically related diseases.
4. Record **HP:0007497** as the most specific core phenotype and **HP:0007404** as the non-epidermolytic qualifier.
5. Represent pressure/friction aggravation, pain, fissures and childhood onset as lower-confidence or broader-focal-PPK annotations unless supported in an individual FNEPPK2 case.
6. Tag mechanistic assertions by evidence:
   - human case tissue: transcriptomics/proteomics/IHC;
   - in vitro: mutant HEK293T calcium assay;
   - model organism: GOF mouse/rat and KO mouse;
   - inferred: mechanical localization, nociceptive ATP signaling and detailed EGFR downstream branches.
7. Mark prevalence, incidence, sex ratio, carrier frequency, validated penetrance, protective factors, epigenetic signatures and prognostic biomarkers as **unknown/not available**.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 2 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1111/ddg.150_12930` (1 mention) - Keratosis palmoplantaris: klinische und genetische Aspekte
  - shared terms: ppk

Weighed against this report's own most characteristic terms: `trpv3`, `focal`, `fneppk2`, `ppk`, `pain`, `variant`, `gln580pro`, `disease`, `pressure`, `phenotype`, `isolated`, `olmsted`, `gene`, `palmoplantar`, `painful`, `disorder`, `hyperkeratosis`, `keratinocyte`, `mondo`, `plantar`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 22 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014622` (12 mentions) - the report calls it "MONDO"; MONDO calls it **isolated focal non-epidermolytic palmoplantar keratoderma**
- `DOID:0111711` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **focal nonepidermolytic palmoplantar keratoderma 2**
- `GO:0005887` (1 mention) - the report calls it "Integral component of plasma membrane"; GO calls it **GO_0005887**
- `UBERON:0001514` (1 mention) - the report calls it "Palmar skin"; UBERON calls it **descending aorta**
- `UBERON:0001516` (1 mention) - the report calls it "Plantar skin"; UBERON calls it **abdominal aorta**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005887` (GO_0005887) (1 mention) - replaced by `GO:0005886`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005216` (1 mention) - the report calls it "Ion channel activity"; GO calls it **monoatomic ion channel activity**, and lists "ion channel activity" among its other names
- `GO:0005886` (2 mentions) - the report calls it "Plasma membrane", "Plasma membrane TRPV3 channel"; GO calls it **plasma membrane**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005886` - called "Plasma membrane", "Plasma membrane TRPV3 channel"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`, `MGI`, `OMIM`.