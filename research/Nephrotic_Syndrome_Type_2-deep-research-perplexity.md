---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-16T11:36:06.781141'
end_time: '2026-10-16T11:40:32.222356'
duration_seconds: 265.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Nephrotic Syndrome Type 2
  mondo_id: MONDO:0010974
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
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 43
  verified: 37
  not_found: 0
  obsolete: 2
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 9
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0010974
    reported_labels:
    - MONDO
    ontology_label: nephrotic syndrome, type 2
  - term_id: DOID:0080379
    reported_labels:
    - Disease Ontology
    ontology_label: nephrotic syndrome type 2
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0031532
    ontology_label: obsolete actin cytoskeleton reorganization
    replaced_by: GO:0030036
  - term_id: GO:0031235
    ontology_label: obsolete intrinsic component of the cytoplasmic side of the plasma
      membrane
    replaced_by: GO:0009898
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nephrotic Syndrome Type 2
- **MONDO ID:** MONDO:0010974 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nephrotic Syndrome Type 2** covering all of the
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

# Nephrotic Syndrome Type 2 — comprehensive disease-characteristics report

**Disease:** Nephrotic syndrome type 2  
**Preferred symbol:** NPHS2-related steroid-resistant nephrotic syndrome  
**MONDO:** MONDO:0010974  
**Category:** Mendelian, autosomal recessive podocytopathy  
**Assessment date:** October 16, 2026

> **Scope note.** “Nephrotic syndrome type 2” specifically denotes the **biallelic NPHS2-associated Mendelian disorder**, not type 2 diabetes-associated nephropathy and not all hereditary steroid-resistant nephrotic syndrome (SRNS). Most epidemiologic and quality-of-life studies aggregate multiple SRNS genotypes; where evidence is not NPHS2-specific, that limitation is stated.

---

## 1. Disease information

### Definition

Nephrotic syndrome type 2 is an autosomal recessive glomerular filtration-barrier disorder caused by pathogenic variants on both alleles of **NPHS2**, which encodes **podocin**. It usually presents in infancy or childhood with nephrotic-range proteinuria, hypoalbuminemia, edema and hyperlipidemia, is resistant to standard glucocorticoid therapy, and commonly progresses to chronic kidney disease and kidney failure. Kidney histology is variable—most often focal segmental glomerulosclerosis (FSGS), but minimal-change disease, diffuse mesangial proliferation or diffuse mesangial sclerosis may occur. [18][46]

The gene–disease relationship is definitive. The landmark positional-cloning study found ten segregating nonsense, frameshift and missense variants and concluded that these findings demonstrated “a crucial role for podocin in the function of the glomerular filtration barrier” (Boute et al., *Nature Genetics*, April 2000; PMID **10742096**). [31]

### Identifiers and synonyms

| Resource | Identifier or term |
|---|---|
| MONDO | **MONDO:0010974** |
| OMIM phenotype | **600995**, Nephrotic syndrome, type 2 |
| OMIM gene | **604766**, NPHS2 |
| Orphanet | **ORPHA:656**, hereditary steroid-resistant nephrotic syndrome; this is a broader category than NPHS2 alone |
| MedGen/UMLS | **C1868672**, MedGen UID 358380 |
| Disease Ontology | **DOID:0080379** |
| MeSH | **D009404**, Nephrotic Syndrome; no uniquely NPHS2-specific MeSH descriptor |
| ICD-10-CM | No genotype-specific code; usually **N04** (nephrotic syndrome), particularly **N04.1** when documented as focal/segmental glomerular lesions |
| ICD-11 | **GB41**, nephrotic syndrome; no NPHS2-specific billable subdivision identified |
| Gene | **NPHS2**, HGNC:13394; NCBI Gene:7827; Ensembl ENSG00000116218 |
| Protein | Podocin, UniProt **Q9NP85** |
| Common synonyms | NPHS2-related nephrotic syndrome; steroid-resistant nephrotic syndrome, autosomal recessive; podocin-associated SRNS; hereditary SRNS; familial FSGS due to NPHS2; nephrosis 2; SRN1 |

The MONDO, OMIM, Orphanet and MedGen mappings are cross-referenced in ClinVar and MedGen. [18][20] ICD-11 places hereditary and other nephrotic syndromes under GB41. [14][15]

### Evidence provenance

This report is an **aggregated disease-level synthesis** from OMIM, Orphanet, ClinVar, GeneReviews, guidelines, registries, cohorts and primary experimental literature. It is **not derived from an individual EHR**. Individual case reports are used only as supporting examples and should not be interpreted as population frequencies.

---

## 2. Etiology

### Primary causal factor

The necessary molecular cause is usually **two pathogenic or likely pathogenic germline NPHS2 variants in trans**—homozygous or compound heterozygous. NPHS2 is at **1q25.2** and encodes podocin, a membrane-associated scaffolding protein concentrated at the podocyte slit diaphragm. [17][211]

Pathogenic alleles include missense, nonsense, frameshift, splice-altering, start-loss and other small insertion/deletion variants. A systematic mutation update identified **126 pathogenic variants**: 53 missense, 17 nonsense, 11 small insertions, 26 small deletions, 16 splice variants, two indels and one stop-codon variant; 43 additional variants were then considered uncertain. [256]

### Genetic risk factors

| Factor | Evidence and interpretation |
|---|---|
| Biallelic loss or dysfunction of NPHS2 | Causal and sufficient in most affected families; variants cause absent podocin or defective folding, stability, oligomerization, trafficking or slit-diaphragm localization. |
| Homozygous p.Arg138Gln | Common European pathogenic genotype; usually early onset. It is retained intracellularly/ER-associated, degraded more rapidly and fails to recruit nephrin normally. [119][575] |
| p.Arg229Gln in selected compound heterozygous states | **Mutation-dependent pathogenicity**: disease generally occurs only when p.Arg229Gln is in trans with particular C-terminal variants, especially those affecting residues 270–351/exons 7–8; onset is usually later and penetrance is incomplete. [106][108] |
| Null alleles | Nonsense, frameshift, canonical splice and start-loss alleles generally predict loss of function and often early/severe disease. |
| Family history and consanguinity | Increase the prior probability of a recessive diagnosis but are not required; apparently sporadic cases commonly reflect two carrier parents. |
| Founder ancestry | Important for p.Arg138Gln in Europe, p.Arg138Ter in Israeli-Arab/Arabian families, p.Val260Glu in Oman and southern African populations, p.Pro118Leu in Turkey, p.Val180Met in North Africa, and c.1032delT among Polish Kashubians. [258][264] |

### Environmental, infectious and lifestyle risk factors

No toxin, diet, infection, behavior or occupational exposure is established as a cause of **NPHS2-related nephrotic syndrome type 2**. Congenital infections such as syphilis or toxoplasmosis cause a different, acquired differential diagnosis—not NPHS2 disease. No population-level NPHS2 gene–environment interaction study was identified in the principal epidemiologic review. [418][420]

Intercurrent infections, dehydration, nephrotoxic drugs and uncontrolled hypertension can nevertheless worsen edema, precipitate acute kidney injury or accelerate damage in someone already affected. These are **course modifiers**, not primary causes.

### Protective factors

* **Genetic:** No validated naturally protective NPHS2 allele is established. A single pathogenic allele usually represents unaffected carrier status. p.Arg229Gln alone or in many nonpermissive combinations is not sufficient to cause the disease, but it should not be labeled a protective allele.
* **Environmental/clinical:** Early reduction of intraglomerular pressure and proteinuria with renin–angiotensin–aldosterone system inhibition, avoidance of dehydration and nephrotoxins, blood-pressure control, vaccination and rapid treatment of infection can reduce secondary injury; none prevents inheritance or the initiating podocin defect.

### Modifier genes and gene–environment interaction

Candidate oligogenic modifiers include **NPHS1, CD2AP** and potentially other slit-diaphragm/cytoskeletal genes. Tri-allelic NPHS1/NPHS2 inheritance has been reported in unusually severe congenital FSGS, but it is uncommon and not a routine diagnostic assumption. [541]

In Nphs2-null mice, genetic background and maternal environment significantly altered survival and progression, supporting biological plausibility for modifiers; equivalent human gene–environment effects have not been quantified (PMID **18385421**). [425]

---

## 3. Phenotypes

Precise NPHS2-only percentages are unavailable for many features. The core nephrotic abnormalities are expected in clinically manifest cases; pathology varies with biopsy timing and sampling.

| Phenotype and type | Typical characteristics | Frequency/evolution | Suggested HPO |
|---|---|---|---|
| Nephrotic-range proteinuria — laboratory | Usually infantile/childhood; may be congenital or adult-onset with selected alleles; persistent and progressive | Defining/very frequent | **HP:0000093 Proteinuria** |
| Hypoalbuminemia — laboratory | Follows sustained urinary albumin loss; severity tracks protein loss and hepatic compensation | Very frequent in full nephrotic syndrome | **HP:0003073 Hypoalbuminemia** |
| Generalized/periorbital edema — sign | Periorbital or dependent edema, progressing to anasarca, ascites or effusions in severe disease; fluctuates with protein loss and sodium balance | Very frequent but can be absent in subnephrotic presentations | **HP:0000969 Edema**; **HP:0100539 Periorbital edema** |
| Hyperlipidemia/hypercholesterolemia — laboratory | Secondary hepatic lipoprotein overproduction and altered clearance | Very frequent in active nephrosis | **HP:0003119 Abnormal circulating lipid concentration**; **HP:0003124 Hypercholesterolemia** |
| Steroid resistance — treatment-response phenotype | Failure to achieve complete remission after approximately four weeks of standard glucocorticoids, with a two-week confirmation period in partial responders | Characteristic; classic biallelic NPHS2 disease exhibits primary resistance | **HP:0032946 Steroid-resistant nephrotic syndrome** if supported by local HPO release |
| FSGS — biopsy finding | Segmental scar in a subset of glomeruli; may emerge after earlier minimal-change/mesangial lesions | Common but not universal | **HP:0000097 Focal segmental glomerulosclerosis** |
| Minimal glomerular change or mesangial proliferation — pathology | Can precede FSGS or reflect sampling/stage | Less common/variable | **HP:0000090 Nephrotic syndrome** plus pathology text |
| Podocyte foot-process effacement — ultrastructural sign | Diffuse or extensive loss of normal interdigitating processes on EM | Expected in active disease | **HP:0012573 Abnormal podocyte morphology** if available; otherwise free-text annotation |
| Progressive renal insufficiency — laboratory/sign | Declining eGFR after persistent proteinuria; usually chronic and progressive | Common | **HP:0012622 Chronic kidney disease** |
| Kidney failure/ESKD | Dialysis or transplantation often required in childhood, adolescence or early adulthood, depending on genotype | Common in severe early-onset disease | **HP:0003774 End-stage renal disease** |
| Hypertension | Often develops with CKD, sodium retention or advanced nephrosis | Variable, later/downstream | **HP:0000822 Hypertension** |
| Ascites/pleural effusion | Severe edema phenotype | Variable | **HP:0001541 Ascites**; **HP:0002202 Pleural effusion** |
| Infection susceptibility | Secondary to urinary immunoglobulin/opsonin loss, edema and immunosuppressive exposure | Variable complication | **HP:0002719 Recurrent infections** |
| Thromboembolism | Secondary to loss of anticoagulants, increased procoagulant synthesis, hemoconcentration and immobility | Uncommon but potentially fatal | **HP:0001977 Abnormal thrombosis** |

Orphanet classifies proteinuria, edema, hypoalbuminemia and FSGS as core or very frequent manifestations of hereditary SRNS. [454][455]

### Quality-of-life impact

Disease-specific NPHS2 utility values are unavailable. Across pediatric nephrotic syndrome cohorts, SRNS is consistently associated with the poorest physical, school, social and total PedsQL scores. In one study, nephrotic-syndrome children had significantly lower overall, physical, social and school scores than controls, and SRNS had the worst domain scores; CNI use and multiple immunosuppressants predicted poorer quality of life (PMID **35106675**). [186] The burdens arise from edema, fatigue, dietary/fluid restrictions, frequent monitoring, hospitalization, treatment toxicity, dialysis and transplantation rather than a behavioral phenotype intrinsic to NPHS2.

---

## 4. Genetic and molecular information

### Gene and protein

| Attribute | Value |
|---|---|
| Gene | **NPHS2**, NPHS2 stomatin family member, podocin |
| HGNC | **HGNC:13394** |
| NCBI Gene | **7827** |
| Ensembl | **ENSG00000116218** |
| OMIM gene | **604766** |
| Location | **1q25.2**; GRCh38 approximately chr1:179.55–179.58 Mb |
| Transcript used clinically | **NM_014625.4** |
| Protein | Podocin; UniProt **Q9NP85** |
| Canonical protein length | 383 residues in the historically described full-length isoform; transcript databases also represent a 316-aa isoform, so HGVS annotation must specify transcript |
| Gene structure | Eight exons in the commonly cited disease transcript |
| Protein family | Stomatin/prohibitin/flotillin/HflK/C family, also called band-7/SPFH |
| Cellular localization | Cytoplasmic face of podocyte plasma membrane, membrane rafts and slit diaphragm; mutant protein may accumulate in ER, Golgi or late endosomes |

Gene and protein identifiers are curated by HGNC, NCBI and UniProt. [211][212][221]

### Representative pathogenic and clinically important variants

| Variant, NM_014625.4 | Class/type | Population information | Functional/clinical consequence |
|---|---|---|---|
| **c.413G>A, p.Arg138Gln** | Pathogenic; missense | gnomAD approximately 0.1% in non-Finnish Europeans; European founder allele [231][240] | ER-associated retention, reduced stability/degradation, deficient membrane-raft localization and impaired nephrin recruitment; usually early-onset SRNS |
| **c.412C>T, p.Arg138Ter** | Pathogenic; nonsense | Very rare globally; enriched in Israeli-Arab/Arabian families | Premature stop/NMD or truncation; loss of function and early severe disease [234] |
| **c.419delG, p.Gly140AspfsTer41** | Pathogenic; frameshift | Rare; recurrent European/Italian allele | Truncation and loss of function [226] |
| **c.871C>T, p.Arg291Trp** | Pathogenic/likely pathogenic; missense | Rare | Aberrant intracellular accumulation, reported in homozygous and compound-heterozygous disease [63] |
| **p.Val180Met** | Pathogenic in biallelic state; missense | Population-dependent | Residual trafficking/function; associated with later onset, approximately 11 years for homozygotes in a recent large series [609] |
| **p.Arg238Ser** | Pathogenic/likely pathogenic; missense | gnomAD about 0.00003 in one compilation | Later onset reported relative to p.Arg138Gln [227] |
| **p.Val260Glu** | Pathogenic; missense | Founder/enriched in Oman and black South African populations | Homozygosity found in 8/30 black South African children with SRNS and accounted for about one-third of unrelated SR-FSGS in that cohort [249] |
| **c.1032delT** | Pathogenic; frameshift | Kashubian founder allele | Loss of function; regional clustering in northern Poland [258][548] |
| **c.686G>A, p.Arg229Gln** | Risk allele/mutation-dependent pathogenic variant; missense | Common, gnomAD approximately 2.8% globally and ~3.7% in Europe | Not independently pathogenic; causes later-onset disease only with selected trans C-terminal alleles through altered oligomerization and mislocalization [229][269] |

### Origin, classification and frequencies

* Disease-causing variants are **constitutional germline** variants. A somatic NPHS2 mechanism has not been established.
* Pathogenic or likely pathogenic classifications should follow ACMG/AMP criteria and current ClinVar assertions. VUSs should not establish the diagnosis, guide irreversible treatment or be used for predictive testing without reclassification/segregation evidence.
* Most fully penetrant pathogenic alleles are individually rare. High frequency makes p.Arg229Gln incompatible with classification as a conventional fully penetrant recessive pathogenic allele.
* Copy-number variants are possible but less prominent than sequence-level variants; panels should include exon-level deletion/duplication analysis.
* No recurrent aneuploidy, translocation or inversion defines the disease.

### Penetrance and modifiers

Penetrance appears high for two severe pathogenic alleles, but age and severity remain variably expressive. The p.Arg229Gln-containing genotype is a major exception: estimated penetrance for the allele in relevant disease configurations has been reported at approximately **1.4%**, reflecting interallelic dependency and incomplete penetrance. [544][551]

There is no repeat expansion, anticipation or established parent-of-origin effect. Germline mosaicism is theoretically possible but is not a characteristic documented mechanism; recurrence counseling generally uses standard autosomal-recessive risks.

### Epigenetics

No diagnostic NPHS2 methylation signature or primary epimutation is established. Experimental toxicology suggests heavy metals and other podocyte stresses can suppress podocin expression epigenetically, but this does not demonstrate that epigenetic silencing causes MONDO:0010974 in humans. [419]

---

## 5. Environmental information

| Category | Assessment |
|---|---|
| Toxins, pollution, occupational exposure | No exposure is established as necessary or sufficient for NPHS2-related disease. Cadmium/lead effects on podocyte-gene expression are experimental and nonspecific. |
| Diet | High sodium worsens edema and hypertension; diet does not cause the inherited disease. Severe protein restriction is inappropriate in growing children; nutritional management should be individualized. |
| Smoking/alcohol/exercise | No NPHS2-specific causal data. Avoid smoking and maintain activity as general cardiovascular/CKD care; mobilization also reduces thrombosis risk. |
| Infection | Does not cause the genetic disorder. Infection can precipitate decompensation, AKI or thrombosis and is an important complication during immunosuppression/nephrosis. |
| Drugs | NSAIDs and other nephrotoxins may worsen kidney function. Glucocorticoids do not correct the structural podocin defect and add toxicity when continued without benefit. |
| Radiation | No established relationship. |

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic NPHS2 variants lead to** absent podocin or variant-specific defects in podocin folding, stability, oligomerization and intracellular trafficking.
2. **Defective or absent podocin leads to** reduced delivery and organization of podocin at cholesterol-rich membrane rafts on the cytoplasmic face of the podocyte slit diaphragm.
3. **Loss of functional podocin scaffolding leads to** impaired interaction with nephrin, CD2AP and associated slit-diaphragm/signaling complexes and, for some variants, disturbed TRPC-channel regulation.
4. **Slit-diaphragm disorganization leads to** abnormal nephrin localization/signaling and impaired coupling of the slit diaphragm to the actin-rich podocyte foot process.
5. **Defective structural and mechanosensory signaling leads to** foot-process cytoskeletal remodeling, effacement, podocyte stress and, for some variants, apoptosis.
6. **Podocyte and slit-diaphragm failure results in** loss of glomerular size-selective permeability and massive urinary albumin and protein loss.
7. **Proteinuria leads to two downstream branches:**
   1. **Systemic branch:** urinary albumin loss leads to hypoalbuminemia; hypoalbuminemia plus renal sodium retention leads to edema/ascites; hepatic compensation leads to hyperlipidemia; urinary loss of immunoglobulins and anticoagulants leads to infection and thrombosis susceptibility.
   2. **Kidney-injury branch:** filtered protein overload leads to tubular inflammatory, oxidative, autophagic and profibrotic stress, which results in tubulointerstitial fibrosis and progressive nephron loss.
8. **Ongoing podocyte depletion and maladaptive glomerular scarring lead to** FSGS/diffuse sclerosis, declining GFR and kidney failure.
9. **Because the upstream lesion is structural rather than primarily immune-mediated, it results in** glucocorticoid resistance and very low recurrence after transplantation into a kidney with normal NPHS2.

Steps 1–6 are supported by human genetics, human cells, organoids and animal models. The exact relative contribution of altered ion-channel mechanosensation versus structural slit-diaphragm failure in human disease is partly inferred.

### Molecular and cellular detail

Wild-type podocin is a hairpin-like membrane protein whose N- and C-termini face the cytoplasm. It forms higher-order oligomers in membrane rafts and interacts through its C-terminal region with nephrin and CD2AP. Schwarz et al. directly showed by immunoelectron microscopy, pull-down and co-immunoprecipitation that podocin localizes at the slit-diaphragm insertion and associates with nephrin/CD2AP (December 2001; PMID **11733557**). [91][126]

Podocin recruits nephrin into lipid rafts, where nephrin phosphorylation and downstream signaling can occur. Pathogenic variants may prevent membrane targeting while retaining oligomerization, thereby disrupting both the structure and signaling function of the complex. [95]

Relevant pathways/processes include:

* slit-diaphragm assembly and maintenance;
* membrane-raft/cholesterol organization;
* nephrin–CD2AP signaling, including links to PI3K–AKT and actin regulation;
* actin-cytoskeleton reorganization and cell-junction stability;
* protein folding, ER quality control, ubiquitin–proteasome degradation and vesicular trafficking;
* podocyte apoptosis;
* protein-overload-induced tubular inflammation, autophagic stress and fibrosis.

Filtered proteins can exceed proximal-tubule autophagic capacity, activate complement and inflammatory/profibrotic mediators and promote tubular apoptosis and interstitial fibrosis. [412]

### Variant-specific mechanisms and recent molecular research

**Human kidney organoids, 2023.** Dorison et al. generated CRISPR-edited and patient-derived iPSC kidney organoids carrying p.Gly92Cys, p.Pro118Leu, p.Arg138Gln, p.Arg168His or p.Arg291Trp. The variants produced reduced podocin abundance, variant-specific ER/Golgi mislocalization, impaired nephrin association and ER-stress-independent podocyte apoptosis (*JASN*, January 1, 2023; PMID **36167728**). [170][172]

**Small-molecule rescue, 2024.** Kuzmuk et al. found that misfolded p.Arg138Gln podocin aberrantly associates with keratin-8 and showed that the experimental small molecule **c407** disrupted this trapping and restored trafficking toward the plasma membrane in laboratory models. This is preclinical, not an approved treatment (*Kidney International*, April 2024; epub November 22, 2023; PMID **37995908**). [151][152]

**AAV gene replacement, 2023.** AAV-LK03 transduced human podocytes in vitro, while AAV2/9-mediated delivery of wild-type podocin reduced albuminuria and histologic damage and improved survival in inducible knockout and p.Arg140Gln mouse models, including treatment after proteinuria began (*Science Translational Medicine*, August 9, 2023; PMID **37556557**). [522][523][528]

### Suggested ontology terms

**GO biological processes**

* GO:0003093 — regulation of glomerular filtration
* GO:0031532 — actin cytoskeleton reorganization
* GO:0072149 — metanephric glomerular visceral epithelial cell development
* protein localization to plasma membrane
* membrane organization
* cell–cell junction organization
* apoptotic process
* response to endoplasmic-reticulum stress
* ubiquitin-dependent proteasomal protein catabolic process

**GO cellular components**

* GO:0036057 — slit diaphragm
* GO:0098846 — podocyte foot process
* GO:0045121 — membrane raft
* GO:0005886 — plasma membrane
* GO:0005783 — endoplasmic reticulum
* GO:0005794 — Golgi apparatus
* GO:0005911 — cell–cell junction
* GO:0031235 — intrinsic component of cytoplasmic side of plasma membrane

**GO molecular function**

* GO:0005515 — protein binding
* cholesterol binding
* scaffold-protein binding

**Cell Ontology**

* **CL:0000653 — podocyte/glomerular visceral epithelial cell**
* proximal tubular epithelial cells as secondary targets of protein overload; use segment-specific CL terms where known.

The curated podocin GO annotations include slit diaphragm, membrane raft, plasma membrane, cell–cell junction and actin-cytoskeleton reorganization. [481][491]

### Immune and metabolic involvement

Immune activation is largely **downstream**, unlike immune-mediated minimal-change disease. Chronic proteinuria can activate tubular complement/inflammatory pathways, but an autoimmune trigger is not required. Systemic metabolic changes include hypoalbuminemia, increased hepatic lipoprotein synthesis, hypercholesterolemia and altered vitamin/hormone-carrier protein levels. Loss of antithrombin III and immunoglobulins contributes to thrombosis and infection risk. [403][404]

---

## 7. Anatomical structures affected

| Level | Structures/cells | Ontology suggestions |
|---|---|---|
| Primary organ | Both kidneys; disease is bilateral and diffuse at the molecular level, although biopsy sclerosis is focal/segmental | **UBERON:0002113 kidney** |
| Functional unit | Nephron and renal corpuscle | **UBERON:0001285 nephron**; **UBERON:0001229 renal corpuscle** |
| Primary site | Renal glomerulus and glomerular filtration barrier | **UBERON:0000074 glomerulus** |
| Primary tissue | Visceral glomerular epithelium | **UBERON:0005751 visceral layer of glomerular capsule**; **UBERON:0004188 glomerular epithelium** |
| Primary cell | Podocyte | **CL:0000653** |
| Subcellular site | Podocyte foot process, slit diaphragm, cytoplasmic plasma-membrane leaflet and membrane rafts | **GO:0098846**, **GO:0036057**, **GO:0031235**, **GO:0045121** |
| Secondary renal injury | Glomerular basement membrane interface, mesangium, proximal tubules and interstitium | **UBERON:0004134 proximal tubule** |
| Secondary systems | Cardiovascular/volume regulation, lipid metabolism, coagulation and host defense | Annotate as complications rather than primary NPHS2 expression sites |

Podocytes are specialized epithelial cells in the visceral layer of Bowman’s capsule whose interdigitating foot processes wrap glomerular capillaries. [463] No meaningful lateralization is expected.

---

## 8. Temporal development and natural history

### Onset

* Classic severe genotypes generally present between **3 months and 6 years**, but congenital presentation and adult-onset FSGS both occur. [48]
* In the 2024 transplant cohort, median age at diagnosis was **0.7 years** for homozygous/compound p.Arg138Gln and **1.8 years** for other biallelic NPHS2 variants, versus 9 years in genetically unresolved SRNS. [613]
* p.Arg138Gln historically correlated with onset around **12 ± 3 months**, whereas p.Val180Met/p.Arg238Ser correlated with approximately **129 ± 12 months**. [54]
* p.Arg229Gln plus a permissive C-terminal trans allele is typically associated with adolescent or adult onset and slower progression.

### Progression

1. **Preclinical stage:** biallelic genotype, normal routine urine testing.
2. **Early disease:** persistent proteinuria, sometimes before edema.
3. **Nephrotic stage:** hypoalbuminemia, edema and hyperlipidemia; primary steroid resistance becomes evident.
4. **Structural progression:** FSGS and increasing tubulointerstitial damage.
5. **CKD stage:** hypertension and progressive decline in eGFR.
6. **Kidney failure:** dialysis and transplantation.

The course is chronic and generally progressive, not relapsing–remitting in the immunologic sense. Apparent partial remissions can occur with RAAS blockade or occasionally CNI therapy but usually do not eliminate the underlying defect.

### Remission and intervention window

Spontaneous durable remission is uncommon. The most important current window is **early diagnosis before substantial podocyte and nephron loss**, permitting withdrawal of ineffective immunosuppression, initiation of antiproteinuric therapy and preparation for genotype-specific trials. Experimental chaperone and gene-replacement approaches are also likely to be more effective before irreversible sclerosis, but this remains unproven clinically.

---

## 9. Inheritance and population

### Inheritance

* **Autosomal recessive.**
* When both parents carry a confirmed pathogenic allele, each pregnancy has a **25% affected, 50% carrier and 25% unaffected non-carrier** probability. [495]
* Apparent pseudodominant pedigrees can occur because some alleles are relatively common.
* Anticipation is not expected.
* Expressivity is variable and strongly genotype-dependent.
* Penetrance is high for two severe alleles but low/incomplete for p.Arg229Gln-containing configurations.
* Consanguinity increases homozygosity and case clustering but is not necessary.

### Epidemiology

A reliable NPHS2-specific incidence or prevalence has not been established. Orphanet reports hereditary SRNS prevalence as unknown and an annual incidence around **1 per 200,000–500,000 children**, encompassing many genes. [244]

Among affected cohorts:

* NPHS2 accounts for roughly **40% of familial recessive SRNS** and **6–17% of sporadic pediatric SRNS** in commonly cited European studies. [253]
* Across all genetic causes, a landmark international study found a monogenic diagnosis in **526/1,783 families (29.5%)** with SRNS onset before age 25 (PMID **25349199**). [271]
* Population modeling across several nephrotic-syndrome genes estimated an overall carrier frequency around 1:218 and disease prevalence around 1:189,036, but these figures are not specific to NPHS2 and depend heavily on in-silico variant classification. [242]

### Population and founder patterns

| Population/region | Enriched allele or observation |
|---|---|
| Northwestern/central Europe | p.Arg138Gln |
| Europe generally | p.Arg229Gln common risk allele, approximately 2–7% allele frequency |
| Israeli-Arab/Arabian families | p.Arg138Ter |
| Turkey | p.Pro118Leu reported recurrently, though some classifications have been downgraded because of high population frequency |
| North Africa | p.Val180Met |
| Oman/Arabian Peninsula | p.Val260Glu |
| Black South African children | p.Val260Glu enrichment |
| Kashubian population, Poland | c.1032delT founder |
| Latin American/Spanish cohorts | p.Ala284Val enrichment reported |

No consistent sex bias is expected for an autosomal disorder; ascertainment cohorts may show modest male predominance without a mechanistic sex-linked explanation.

---

## 10. Diagnostics

### Clinical diagnostic criteria

In children, nephrotic syndrome is generally established by nephrotic-range proteinuria—first-morning urine protein/creatinine ratio (UPCR) approximately **≥2 mg/mg or ≥200 mg/mmol**, or equivalent timed excretion—plus hypoalbuminemia and/or edema. SRNS is diagnosed when complete remission is absent after four weeks of daily standard-dose prednisone/prednisolone, with an optional two-week confirmation period for partial responders. [197][301][307]

### Recommended evaluation

| Test | Expected finding or purpose |
|---|---|
| Urinalysis and first-morning UPCR | Persistent nephrotic-range proteinuria; hematuria may be absent or mild |
| Serum albumin/total protein | Low during active nephrosis |
| Lipid profile | Hypercholesterolemia/hypertriglyceridemia |
| Creatinine, cystatin C and eGFR | Baseline and progression assessment |
| Electrolytes, bicarbonate, calcium/phosphate | CKD and treatment monitoring |
| CBC, IgG, coagulation evaluation when indicated | Infection and thrombosis-risk assessment |
| Blood pressure and volume status | Detect hypertension, hypovolemia or fluid overload |
| Renal ultrasound | Usually nonspecific; assesses anatomy, size and complications |
| Kidney biopsy | Light microscopy may show MCD, mesangial proliferation, FSGS or DMS; EM shows foot-process effacement; immunostaining may show reduced/mislocalized podocin/nephrin |
| Genetic test | Confirms biallelic pathogenic/likely pathogenic NPHS2 variants and distinguishes structural from likely immune-mediated SRNS |

### Genetic-testing strategy

1. **First line:** comprehensive SRNS/FSGS multigene panel, including sequencing and deletion/duplication analysis. At minimum it should include NPHS2, NPHS1, WT1, LAMB2, PLCE1, INF2, TRPC6, ACTN4, CD2AP, COQ2, COQ6, COQ8B/ADCK4 and relevant nucleoporin/cytoskeletal genes.
2. **Single-gene NPHS2 testing:** reasonable when phenotype, ancestry or a known family variant makes NPHS2 overwhelmingly likely; otherwise a panel is more efficient.
3. **WES:** appropriate after a negative panel or when the phenotype is atypical/syndromic.
4. **WGS:** useful for deep intronic, regulatory, complex structural or poorly captured variants; highest technical breadth but cost and interpretation remain limiting.
5. **RNA studies:** targeted RNA sequencing or patient-derived cell assays can clarify suspected splice variants.
6. **CMA/karyotype/FISH:** not routine for isolated NPHS2 disease; reserve for syndromic presentations or suspected chromosomal abnormalities.
7. **Mitochondrial or repeat-expansion testing:** not routine unless another phenotype suggests it.

A 2024 comparison found WGS had the highest detection efficiency, followed by WES, while panels were most cost-effective and therefore reasonable first-line tests. [287] IPNA recommends genetic testing in all children with primary SRNS, ideally during the diagnostic confirmation period. [310]

### Interpretation requirements

* Demonstrate two pathogenic/likely pathogenic variants in trans.
* Perform parental segregation whenever possible.
* Do not assume p.Arg229Gln is disease-causing without examining the exact trans allele.
* A heterozygous pathogenic variant alone establishes carrier status, not NPHS2-related disease; pursue CNV, intronic or alternate-gene analysis.
* Reassess VUSs periodically and avoid using them alone to stop effective treatment.

### Differential diagnosis

| Differential | Distinguishing features |
|---|---|
| Immune-mediated minimal-change disease/FSGS | More likely steroid/CNI responsive; no causative biallelic NPHS2 variants; higher post-transplant recurrence |
| NPHS1-related nephrotic syndrome | Often congenital, massive placentomegaly/elevated fetal AFP; nephrin variants |
| WT1-related nephropathy | Possible genital anomalies, Wilms-tumor risk or Frasier/Denys–Drash spectrum |
| LAMB2/Pierson syndrome | Microcoria/ocular and neurologic abnormalities |
| PLCE1-related NS | DMS/FSGS; occasionally treatment-responsive |
| CoQ10-biosynthesis disorders | Neurologic features; potentially responsive to CoQ10 |
| COL4A3–COL4A5 disease | Persistent hematuria, hearing/ocular features, GBM abnormalities |
| APOL1-associated FSGS | Relevant African ancestry; complex/recessive risk genotype rather than classic NPHS2 phenotype |
| Secondary infection-associated NS | Congenital infection evidence, serology/PCR |
| Adaptive, obesity-, reflux-, drug- or virus-associated FSGS | Corresponding exposure/systemic disease; often non-nephrotic proteinuria |
| Alport syndrome, lupus, membranous nephropathy | Serology, complements, biopsy and extrarenal findings |

### Screening

There is no population newborn biochemical screening program. Recommended strategies are:

* cascade testing of siblings and relatives after a molecular diagnosis;
* urinalysis/UPCR and blood-pressure surveillance for at-risk siblings pending testing;
* targeted carrier testing for the known family variants;
* prenatal diagnosis or PGT-M after both familial variants are established.

---

## 11. Outcome and prognosis

### Kidney survival

Prognosis depends strongly on genotype, onset age, baseline kidney function and degree of proteinuria. In PodoNet, overall primary-SRNS ESKD-free survival was approximately **74% at five years, 58% at ten years and 48% at 15 years**. Genetic podocytopathies had poorer outcomes; one analysis estimated only **28% ten-year ESKD-free survival for NPHS2-associated disease**, although another reporting convention described approximately 72% as progressing-free at ten years, illustrating cohort and endpoint-definition differences. [435][443]

In the 2024 transplant cohort, median age at kidney failure was **7.3 years** for the p.Arg138Gln group and **9.2 years** for other NPHS2 genotypes; median transplant ages were 9.0 and 10.7 years, respectively. [613]

### Transplantation

Kidney transplantation is highly effective because the donor kidney has normal podocin. In 117 transplanted patients with biallelic NPHS2 variants, only **one recurrence (0.85%)** occurred over a median 8.5-year follow-up; none occurred among p.Arg138Gln carriers. By comparison, 7/44 genetically unresolved patients recurred, all within seven days (Bharat et al., *Kidney International Reports*, January 10, 2024; PMID **38765578**). [612][613]

### Morbidity and complications

* edema, ascites, pleural effusion and intravascular depletion;
* hypertension and progressive CKD;
* bacterial infection, especially cellulitis, pneumonia and spontaneous bacterial peritonitis;
* venous thromboembolism, including renal-vein, cerebral-venous and pulmonary thrombosis;
* malnutrition, growth impairment and endocrine/vitamin-carrier losses;
* dyslipidemia and long-term cardiovascular risk;
* treatment toxicity from unnecessary steroids/CNIs;
* dialysis and transplant-related burdens.

In one pediatric SRNS cohort, infections occurred in 31.9%, peritonitis in 29.7%, venous thrombosis in 2.2% and death in 5.5%, but these figures combine genetic and nongenetic SRNS and are highly setting-dependent. [433]

Long-term survival after successful transplantation can approach that of other pediatric transplant recipients; no reliable NPHS2-specific five- or ten-year patient-survival percentage is available.

### Prognostic factors

**Poorer prognosis:** early onset, severe/null genotypes, p.Arg138Gln homozygosity, persistent heavy proteinuria, impaired eGFR at diagnosis, FSGS/DMS, failure to obtain at least partial proteinuria reduction, hypertension and delayed diagnosis.

**Relatively milder/later course:** p.Val180Met, p.Arg238Ser and selected p.Arg229Gln compound genotypes.

No circulating biomarker is sufficiently validated to replace genotype, UPCR, eGFR, blood pressure and histology.

---

## 12. Treatment

### Disease-specific principle

There is presently **no approved pharmacologic therapy that corrects NPHS2**. Management aims to lower proteinuria, control nephrotic complications and CKD progression, and transplant when kidney failure develops. Once a convincing genetic diagnosis is established, prolonged glucocorticoid or broad immunosuppressive therapy should generally be stopped because it does not repair the structural defect. GeneReviews recommends avoiding ineffective prednisone and using RAAS inhibition to reduce proteinuria. [329]

### Clinical treatment table

| Intervention | Role and evidence | Important adverse effects/monitoring | Suggested NCIT intervention label |
|---|---|---|---|
| ACE inhibitor, e.g., enalapril/lisinopril | First-line antiproteinuric and antihypertensive supportive therapy | Hyperkalemia, creatinine rise, hypotension; stop during severe dehydration/AKI | Angiotensin-Converting Enzyme Inhibitor Therapy |
| ARB, e.g., losartan | Alternative to ACE inhibitor; avoid routine ACEi–ARB dual blockade | Same renal/potassium monitoring; teratogenic | Angiotensin Receptor Blocker Therapy |
| Prednisone/prednisolone initial diagnostic course | Required initially in typical childhood NS to establish steroid response; **not effective as continued NPHS2 therapy** | Growth suppression, infection, hypertension, obesity, bone/eye toxicity | Corticosteroid Therapy |
| Cyclosporine or tacrolimus | Not routinely recommended after confirmed monogenic NPHS2 disease; occasional partial/transient antiproteinuric response may occur through podocyte effects | Nephrotoxicity, hypertension, neurotoxicity, diabetes, drug interactions | Calcineurin Inhibitor Therapy |
| Loop diuretic, e.g., furosemide | Symptomatic severe edema | Hypovolemia, AKI, electrolyte depletion and thrombosis | Diuretic Therapy |
| Albumin infusion plus diuretic | Refractory edema, symptomatic hypovolemia or prerenal crisis under specialist supervision | Pulmonary edema, hypertension, volume shifts | Albumin Infusion |
| Statin | Selected patients with persistent severe dyslipidemia and CKD/cardiovascular risk; pediatric evidence limited | Liver enzymes, CK | Lipid-Lowering Therapy |
| Anticoagulation | Treat confirmed thrombosis; prophylaxis only for major individualized risk factors, not routinely | Bleeding | Anticoagulant Therapy |
| Antibiotics/IVIG | Treat infection; IVIG may be considered with low IgG plus recurrent/severe infections | Agent-specific | Anti-Infective Therapy; Immunoglobulin Therapy |
| Dialysis | Kidney-replacement therapy for kidney failure | Access infection/thrombosis, nutrition and growth burdens | Hemodialysis; Peritoneal Dialysis |
| Kidney transplantation | Preferred definitive renal-replacement treatment; recurrence risk extremely low | Standard graft rejection/infection risks | Kidney Transplantation |

The original clinical genotype study concluded: “patients with homozygous or compound heterozygous mutations in NPHS2 exhibit primary resistance to standard steroid treatment” and that a second standard steroid trial is not justified (Ruf et al., *JASN*, 2004). [597][602]

In PodoNet, transient non-nephrotic-range proteinuria reduction with cyclosporine occurred in several genetically diagnosed patients, including four with NPHS2, but most relapsed or progressed; investigators could not separate CNI effects from concurrent RAAS blockade or declining filtration. [338]

### Supportive strategy

1. Confirm volume status before diuretics or RAAS blockade.
2. Restrict excessive sodium, but maintain appropriate calories and protein for growth.
3. Use ACE inhibitor or ARB if tolerated.
4. Monitor UPCR, albumin, eGFR, potassium, blood pressure, growth and lipids.
5. Stop ineffective immunosuppression after molecular confirmation unless an independent immune-mediated process is convincingly present.
6. Prepare early for CKD care, dialysis access and transplantation when progression is evident.
7. Genotype potential related donors and avoid donation by someone with unresolved renal findings or an at-risk biallelic genotype.

### Experimental and advanced therapeutics

| Approach | Status |
|---|---|
| **c407 small-molecule chaperone** | Preclinical rescue of p.Arg138Gln podocin trafficking by disrupting keratin-8 trapping; no human efficacy or safety data. PMID **37995908**. [152] |
| **AAV podocin gene replacement** | AAV-LK03 human-podocyte and AAV2/9 mouse studies showed rescue; not approved. PMID **37556557**. [522][528] |
| **PS-001 local podocyte-targeted AAV** | 2024 conference/preclinical program reported expression in 89% ± 11% of minipig glomeruli and no identified treatment-related toxicity in the reported small study; clinical efficacy remains untested. [343] |
| CRISPR/gene editing | Conceptually applicable but no clinical NPHS2 program with established safety or efficacy identified |
| RNA therapy | No approved NPHS2-specific ASO/siRNA/mRNA therapy |
| Stem/cell therapy | No established benefit |
| Rituximab or other immunotherapy | No mechanistic rationale for isolated biallelic NPHS2 deficiency; use would generally represent empiric treatment before genetic clarification, not genotype-directed care |

No active, completed human trial has established an NPHS2-specific disease-modifying response. Trials for idiopathic FSGS/SRNS should not be automatically extrapolated to structural NPHS2 disease.

### Pharmacogenomics

No CPIC or PharmGKB dosing guideline is specific to NPHS2. Genotype affects **therapeutic indication and expected efficacy**, not hepatic drug metabolism: confirmation of biallelic NPHS2 strongly predicts glucocorticoid nonresponse and low post-transplant recurrence.

---

## 13. Prevention

### Primary prevention

The inherited molecular defect cannot be prevented by diet, vaccination or lifestyle. Primary reproductive options are:

* preconception carrier testing for the familial variants;
* partner testing when one carrier is known;
* PGT-M with IVF;
* prenatal diagnosis using chorionic-villus sampling or amniocentesis;
* donor gametes or adoption, according to family preferences.

PGT-M counseling must account for mutation-dependent alleles such as p.Arg229Gln; ASRM specifically cautions against offering PGT-M for combinations not actually associated with disease. [492]

### Secondary prevention/early detection

* Cascade testing of siblings and relatives.
* Urinalysis, UPCR, serum creatinine and blood pressure in untested at-risk children.
* Prompt genetic testing in congenital, infantile, familial or steroid-resistant nephrotic syndrome.
* Early RAAS blockade and avoidance of repeated ineffective steroid courses after diagnosis.

### Tertiary prevention

* Vaccination against pneumococcus and annual influenza; meningococcal vaccination where indicated.
* Varicella immunization before immunosuppression in nonimmune patients; avoid live vaccines during high-dose immunosuppression.
* Rapid assessment of fever, abdominal pain, cellulitis or respiratory symptoms.
* Maintain mobility and hydration; avoid unnecessary central venous lines.
* Do not use routine thromboprophylaxis in all children; consider low-molecular-weight heparin when severe prolonged hypoalbuminemia is combined with prior thrombosis, central access, inherited thrombophilia, infection, dehydration or immobilization. [313][315]
* Avoid nephrotoxins, smoking, uncontrolled hypertension and episodes of severe dehydration.
* Genetic counseling should include the 25% recurrence risk, variable severity and favorable transplant recurrence profile.

Public-health sanitation or vector control has no disease-specific role.

---

## 14. Other species and natural disease

### Natural disease

No well-validated naturally occurring animal disease caused by **biallelic NPHS2 variants** was identified. Dogs develop naturally occurring protein-losing nephropathies, but the best-characterized Soft-Coated Wheaten Terrier disorder is genetically complex and associated with **NPHS1 and KIRREL2**, not established NPHS2 disease. In that breed, homozygosity for the risk alleles carried an odds ratio of 9.06 and average onset was 6.3 years (PMID **23325127**). [377]

Thus, canine nephrotic syndrome provides comparative podocyte biology but should not be entered as a natural NPHS2 orthologous disease without variant-level evidence. There is no zoonotic potential or cross-species transmission.

### Orthologs and taxonomy

| Species | NCBI Taxon | Ortholog/resource | Relevance |
|---|---:|---|---|
| Human, *Homo sapiens* | 9606 | NPHS2, NCBI Gene 7827 | Disease species |
| Mouse, *Mus musculus* | 10090 | Nphs2, NCBI Gene **170484**, MGI:2157018 | Principal mammalian genetic model |
| Rat, *Rattus norvegicus* | 10116 | Nphs2 ortholog | Podocyte/FSGS physiology models |
| Zebrafish, *Danio rerio* | 7955 | nphs2, NCBI Gene **557914**, ZFIN:ZDB-GENE-051102-2 | Filtration, edema and proteinuria models |
| Dog, *Canis lupus familiaris* | 9615 | NPHS2 ortholog | Comparative glomerular disease; no definitive natural NPHS2 syndrome |
| *Caenorhabditis elegans* | 6239 | **mec-2**, functional SPFH-family homolog | Cholesterol-dependent mechanosensory channel biology, not a kidney model |
| *Drosophila melanogaster* | 7227 | No direct introduced human NPHS2 disease model in FlyBase | Nephrocytes model slit-diaphragm biology, chiefly nephrin/Neph1 analogues |

The zebrafish orthology and NCBI Gene identifier are curated by the Alliance of Genome Resources. [358]

---

## 15. Model organisms and experimental systems

| Model | Type and phenotype recapitulation | Applications | Limitations |
|---|---|---|---|
| Constitutive **Nphs2-null mouse** | Antenatal proteinuria, foot-process effacement, massive mesangial sclerosis and death from kidney failure within days/weeks | Establishes that podocin is indispensable; studies developmental injury and modifiers | More severe than typical human NPHS2 disease; DMS rather than classic human FSGS; survival strongly strain-dependent |
| **Nphs2 p.Arg140Gln knock-in mouse** | Human p.Arg138Gln analog; early albuminuria, progressive renal insufficiency, mesangiolysis/sclerosis and death in first month | Variant-specific pathogenesis, chaperones and gene replacement | Earlier/severer than many patients; background effects |
| Adult inducible podocyte-specific **Nphs2 knockout** | Albuminuria, hypercholesterolemia, hypertension and renal failure; FSGS appears at approximately four weeks, followed by diffuse glomerulosclerosis/tubulointerstitial injury | Temporal sequence from podocin loss to FSGS; therapeutic intervention after onset | Artificial near-complete loss; rapid course |
| Human immortalized podocytes expressing variants | Measures membrane trafficking, rafts, protein stability, ER degradation and interaction with nephrin/K8 | Mechanistic screening and drug rescue | Lacks mature 3-D filtration barrier, hemodynamics and multicellular context |
| CRISPR-edited/patient-derived **iPSC kidney organoids** | Reduced podocin, variant-specific ER/Golgi localization, nephrin defects and podocyte apoptosis | Human developmental context, allelic series, functional classification and drug screening | Immature, poorly perfused, limited filtration and long-term fibrosis; not equivalent to an adult glomerulus |
| Zebrafish **nphs2 morphants** | Glomerular hypoplasia, foot-process effacement, filtration-barrier damage and pericardial edema | Rapid in-vivo screening and proteinuria reporters | Pronephros differs from human metanephros; morpholino off-target/transient effects |
| Tg(nphs2:NTR) zebrafish | Metronidazole-induced podocyte ablation causes proteinuria and whole-body edema | Podocyte loss/regeneration and drug screens | Induced ablation is not variant-specific NPHS2 disease |
| *C. elegans mec-2* | Cholesterol-dependent mechanosensory complex; mec-2-null worms are touch-insensitive | SPFH-domain, cholesterol binding and channel regulation | No kidney or podocyte; human podocin cannot fully rescue mec-2-null touch phenotype [398] |
| Drosophila nephrocytes | Podocyte-like slit diaphragms and filtration/endocytosis | High-throughput slit-diaphragm and cytoskeletal genetics | No direct podocin orthologous renal physiology; human NPHS2 has not been introduced in the curated FlyBase disease model [389] |

Primary mouse evidence includes:

* Roselli et al.: Nphs2-null mice developed antenatal proteinuria and died from massive mesangial sclerosis (*Molecular and Cellular Biology*, 2004). [596]
* Philippe et al.: p.Arg140Gln mice developed early albuminuria, foot-process effacement and severe renal failure; “survival depends on the genetic background” (*Kidney International*, May 2008; PMID **18288100**). [582]
* Mollet et al.: adult podocin inactivation produced FSGS at four weeks followed by diffuse sclerosis and tubulointerstitial damage (PMID **19713307**). [583]

---

# Current expert interpretation and knowledge gaps

1. **The diagnosis is molecular, not histologic alone.** FSGS is a pattern of injury; biallelic NPHS2 variants identify the specific structural podocytopathy.
2. **Early genetic testing changes treatment.** IPNA and GeneReviews support testing all primary pediatric SRNS because a genetic diagnosis prevents unnecessary immunosuppression, informs recurrence risk and enables family testing. [285][310]
3. **p.Arg229Gln requires unusually careful interpretation.** It is common, incompletely penetrant and pathogenic only in selected trans configurations; labeling it simply “pathogenic” without haplotype and second-allele analysis risks overdiagnosis.
4. **Transplant prognosis is a major strength of molecular diagnosis.** The 2024 117-patient cohort provides the strongest recent evidence that recurrence is near zero in true biallelic NPHS2 disease. [612]
5. **The leading precision-therapy concepts are trafficking rescue and podocyte-targeted gene replacement.** Both produced convincing preclinical correction in 2023–2024, but neither has yet demonstrated safety, durable efficacy or prevention of kidney failure in humans. [152][522]
6. **Major gaps** include true genotype-specific prevalence, prospective untreated natural history, validated modifiers, human pharmacodynamic biomarkers, long-term organoid maturation, safe repeatable podocyte gene delivery and controlled trials stratified by exact NPHS2 genotype.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 4 |
| Terms whose name was checked | 15 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010974` (3 mentions) - the report calls it "MONDO"; MONDO calls it **nephrotic syndrome, type 2**
- `DOID:0080379` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **nephrotic syndrome type 2**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0031532` (obsolete actin cytoskeleton reorganization) (1 mention) - replaced by `GO:0030036`
- `GO:0031235` (obsolete intrinsic component of the cytoplasmic side of the plasma membrane) (2 mentions) - replaced by `GO:0009898`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0031532` (1 mention) - the report calls it "actin cytoskeleton reorganization"; GO calls it **obsolete actin cytoskeleton reorganization**, and lists "actin cytoskeleton reorganisation" among its other names
- `GO:0072149` (1 mention) - the report calls it "metanephric glomerular visceral epithelial cell development"; GO calls it **podocyte cell fate commitment**, and lists "glomerular visceral epithelial cell fate commitment" among its other names
- `GO:0031235` (2 mentions) - the report calls it "intrinsic component of cytoplasmic side of plasma membrane"; GO calls it **obsolete intrinsic component of the cytoplasmic side of the plasma membrane**, and lists "intrinsic to cytoplasmic side of plasma membrane" among its other names
- `CL:0000653` (2 mentions) - the report calls it "podocyte/glomerular visceral epithelial cell", "Podocyte"; CL calls it **podocyte**, and lists "glomerular visceral epithelial cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000653` - called "podocyte/glomerular visceral epithelial cell", "Podocyte"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `MGI`.