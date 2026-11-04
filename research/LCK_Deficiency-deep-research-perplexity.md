---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-03T14:09:30.926028'
end_time: '2026-11-03T14:14:21.241515'
duration_seconds: 290.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: LCK Deficiency
  mondo_id: MONDO:0014334
  category: Mendelian
  causal_genes: LCK
  omim_id: OMIM:615758
  synonyms: immunodeficiency type 22; SCID due to LCK deficiency; SCID due to lymphocyte-specific
    protein tyrosine kinase deficiency; severe combined immunodeficiency due to lymphocyte-specific
    protein tyrosine kinase deficiency
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 52
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 9
  validator_version: 0.5.1
term_validation:
  total_terms: 60
  verified: 53
  not_found: 0
  obsolete: 2
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014334
    reported_labels:
    - MONDO
    ontology_label: severe combined immunodeficiency due to LCK deficiency
  - term_id: DOID:0111937
    reported_labels:
    - Disease Ontology
    ontology_label: immunodeficiency 22
  obsolete_terms:
  - term_id: HP:0005407
    ontology_label: obsolete Decreased proportion of CD4-positive helper T cells
    replaced_by: HP:0032218
  - term_id: HP:0001002
    ontology_label: obsolete Decreased subcutaneous fat
    replaced_by: HP:0003758
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** LCK Deficiency
- **MONDO ID:** MONDO:0014334 (if available)
- **Causal gene(s):** LCK
- **OMIM:** OMIM:615758
- **Synonyms:** immunodeficiency type 22; SCID due to LCK deficiency; SCID due to lymphocyte-specific protein tyrosine kinase deficiency; severe combined immunodeficiency due to lymphocyte-specific protein tyrosine kinase deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **LCK Deficiency** covering all of the
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

# LCK Deficiency: comprehensive disease-characteristics report

**LCK deficiency**—also called immunodeficiency 22 or combined/severe combined immunodeficiency due to LCK deficiency—is a very rare, autosomal-recessive inborn error of immunity caused by biallelic loss-of-function variants in ***LCK***, which encodes lymphocyte-specific protein tyrosine kinase. The disorder chiefly impairs thymic T-cell development and proximal T-cell receptor signaling, producing profound or “leaky” T-cell immunodeficiency, recurrent infections, and—in hypomorphic disease—immune dysregulation such as intestinal or cutaneous inflammation. The relevant disease is **MONDO:0014334 / OMIM:615758**, not another numbered immunodeficiency. The LCK–disease relationship was upgraded to **definitive** by the GenCC/ClinGen SCID-CID expert curation in July 2025. [160]

## Executive summary

- **Core lesion:** germline biallelic loss of LCK function.
- **Characteristic immune phenotype:** low total T cells, especially CD4-positive and naïve αβ T cells; very low TRECs; restricted or oligoclonal TCR repertoire; relatively increased γδ T cells; reduced CD4 and often CD8 surface density; poor TCR-induced phosphorylation, calcium flux, activation and proliferation. B- and NK-cell numbers are often preserved, although switched-memory B cells and immunoglobulins may be secondarily reduced. [1][75]
- **Clinical spectrum:** infancy-onset recurrent bacterial, viral, fungal and opportunistic infections, diarrhea, failure to thrive and candidiasis; partial-function alleles may additionally cause inflammatory bowel disease, panniculitis/vasculitis, autoimmunity, epidermodysplasia-verruciformis-like HPV disease and virus-associated squamous-cell carcinoma. [119][278]
- **Definitive diagnosis:** compatible immunophenotype plus pathogenic/likely pathogenic biallelic *LCK* variants, supported when needed by reduced LCK expression and abnormal TCR-signaling assays.
- **Definitive treatment:** early allogeneic hematopoietic stem-cell transplantation (HSCT/HCT). Immunoglobulin replacement and antimicrobial treatment/prophylaxis are supportive, not curative. There is no approved LCK-specific gene, RNA or small-molecule replacement therapy.
- **Evidence limitations:** knowledge remains based principally on individual families and mechanistic models rather than registries or natural-history cohorts. By the end of 2024, approximately **nine molecularly confirmed affected individuals from five families** had been described in the five principal reports; a sixth frameshift case was presented only as a 2025 conference abstract. Consequently, frequencies, penetrance and survival percentages cannot be estimated reliably. [289][409]

---

## 1. Disease information

### 1.1 Definition and identifiers

| Resource | Identifier/name | Comment |
|---|---|---|
| MONDO | **MONDO:0014334** | Severe combined immunodeficiency due to LCK deficiency |
| OMIM disease | **615758** | Immunodeficiency 22 |
| OMIM gene | **153390** | *LCK* |
| Orphanet | **ORPHA:280142** | Combined immunodeficiency due to LCK deficiency; Orphanet describes failure to thrive, severe diarrhea, opportunistic infections and abnormal T-cell differentiation/function. [16] |
| MedGen/UMLS | **C4014233** | Severe combined immunodeficiency due to LCK deficiency |
| Disease Ontology | **DOID:0111937** | Immunodeficiency 22 [37] |
| MeSH | **D016511** | Severe Combined Immunodeficiency; no dedicated LCK-deficiency MeSH heading was identified. [90] |
| ICD-10-CM | **D81.89**, other combined immunodeficiencies, is the most defensible general code | LCK deficiency does not have a dedicated ICD-10 code. D81.2 may sometimes be used for SCID with low/normal B-cell numbers, but the phenotype is often leaky CID rather than classic SCID. [93][99] |
| ICD-11 MMS | **4A01.10**, severe combined immunodeficiencies | Appropriate for severe presentations; a distinct LCK subtype code was not identified. [91] |
| Gene | **HGNC:6524; NCBI Gene 3932; Ensembl ENSG00000182866; UniProt P06239** | Located at **1p35.2**. [104] |

### 1.2 Synonyms

- Immunodeficiency 22; IMD22
- Immunodeficiency type 22
- LCK-related combined immunodeficiency
- CID due to LCK deficiency
- SCID due to LCK deficiency
- SCID/CID due to lymphocyte-specific protein tyrosine kinase deficiency
- Severe combined immunodeficiency due to LCK deficiency
- Severe combined immunodeficiency due to lymphocyte-specific protein tyrosine kinase deficiency [19][27]

### 1.3 Nature of the evidence

The primary evidence is **patient-level**, derived from individual case reports or small families with clinical records, flow cytometry, sequencing and functional experiments. OMIM, Orphanet, MONDO, MedGen and IUIS classifications are **aggregated disease-level resources** synthesizing those cases. There are no sufficiently large EHR cohorts, population registries or formal natural-history studies specific to LCK deficiency.

---

## 2. Etiology, risk, protective factors and gene–environment interaction

### 2.1 Primary cause

The disease is caused by **germline biallelic loss-of-function or hypomorphic variants in *LCK***. Pathogenic classes documented in patients include missense substitutions, a canonical splice-acceptor variant and a frameshift/truncating variant. The accepted mechanism is reduced or absent LCK protein and/or kinase activity, leading to defective TCR signal initiation. [160]

There is no evidence that toxins, nutrition, occupation, smoking, alcohol or other environmental exposures independently cause LCK deficiency.

### 2.2 Genetic risk factors

- Having two pathogenic *LCK* alleles is the principal risk factor.
- Consanguinity was present in most reported families and increases the probability of homozygosity for a rare familial allele.
- The original p.Leu341Pro patient was homozygous because of **uniparental isodisomy**, rather than ordinary biparental inheritance. [47][142]
- No established modifier genes, common susceptibility loci, polygenic score or founder allele have been demonstrated.
- Heterozygous relatives are generally clinically healthy. One p.Cys465Arg carrier mother nevertheless had intermediate reductions in CD4/CD8 expression and partial loss of naïve T cells, so complete absence of a laboratory carrier phenotype should not be assumed. [57]

### 2.3 Environmental and infectious modifiers

Pathogens are **complications and phenotype modifiers**, not the inherited cause. Documented organisms include:

- *Candida* species, including *C. glabrata*
- *Cryptosporidium*
- CMV, EBV, adenovirus, HSV and norovirus
- *Salmonella*
- MRSA and vancomycin-resistant enterococci
- HPV types 5, 20 and 38 in epidermodysplasia-verruciformis-like lesions, and HPV-6 in genital warts [65][75]

Residual T-cell activity appears to interact with antigenic and microbial exposure. In the p.Pro440Ser knock-in mouse, conventional CD4 T cells with residual signaling caused intestinal inflammation when Treg control was inadequate; gut microbiota were proposed as a stimulus but were **not directly demonstrated**, and the authors called for germ-free or antimicrobial experiments. [247]

For the HPV-associated family, persistent HPV infection clearly preceded cutaneous squamous-cell carcinoma. Ultraviolet exposure is a known cofactor in epidermodysplasia verruciformis generally, but its specific contribution was not quantified in the LCK family. [269]

### 2.4 Protective factors

No genetic protective variant has been established. Practical protective measures are:

- early newborn detection;
- infection avoidance;
- avoidance of live vaccines before immune reconstitution;
- immunoglobulin replacement where indicated;
- antibacterial, antifungal and antiviral prophylaxis;
- prompt infection treatment; and
- early HSCT before serious infection develops.

These measures reduce complications but do not prevent inheritance of the disorder. Standard SCID-center practice includes near-universal immunoglobulin replacement and Pneumocystis prophylaxis. [195]

---

## 3. Phenotypes

Because published numbers are tiny, “frequency” below means the qualitative consistency across reported families, not a population estimate.

| Phenotype/type | Characteristics, onset and course | Suggested HPO term |
|---|---|---|
| Combined immunodeficiency | Core disease feature; congenital molecular defect, clinically apparent from birth to early childhood; severe to variable | Immunodeficiency, **HP:0002721** |
| Recurrent respiratory infections | Usually begin in infancy; pneumonia and otitis are common; may be bacterial, viral or fungal; can be progressive and fatal | Recurrent respiratory infections, **HP:0002205**; recurrent pneumonia, **HP:0006532** |
| Opportunistic infection | Candidiasis, cryptosporidiosis, severe CMV/EBV/adenovirus and suspected Pneumocystis have occurred | Opportunistic infection, **HP:0002723** |
| Chronic/protracted diarrhea | Frequent in severe and partial-function disease; infectious and/or inflammatory; can be persistent | Chronic diarrhea, **HP:0002028** |
| Failure to thrive | Usually infantile; linked to chronic infection, diarrhea and inflammation; often severe | Failure to thrive, **HP:0001508**; failure to thrive in infancy, **HP:0001531** |
| Oral/perianal candidiasis | Early and recurrent in several families; esophageal candidiasis caused strictures in one patient | Chronic oral candidiasis, **HP:0009098** |
| Lymphopenia | Core laboratory abnormality; often progressive | Lymphopenia, **HP:0001888** |
| T-cell lymphopenia | Marked reduction in CD3, CD4 and usually CD8 αβ T cells | Decreased total T-cell count, **HP:0032180**; decreased CD4-positive T cells, **HP:0005407** |
| Loss of naïve T cells/low TRECs | Frequently profound; TRECs were 0 or far below reference in recent cases; suggests reduced thymic output | Decreased naïve T-cell proportion; decreased TRECs—use the current HPO release term where supported |
| Reduced CD4/CD8 surface expression | Highly characteristic laboratory sign; reduced CD4 is proposed as a specific diagnostic clue | Decreased CD4-positive T-cell proportion, **HP:0032218** |
| Restricted/oligoclonal TCR repertoire | Seen particularly with truncated or near-null variants; reflects limited thymic output and homeostatic expansion | Restricted T-cell receptor repertoire |
| Relative γδ T-cell increase | Recurrent finding despite low absolute T-cell numbers | Increased γδ T-cell proportion |
| Poor T-cell activation/proliferation | Reduced responses to anti-CD3/CD28, PHA and antigens; severe functional consequence | Abnormal lymphocyte proliferation |
| Hypogammaglobulinemia | Variable and likely secondary to deficient T-cell help; switched-memory B cells may be depleted despite normal total B cells | Hypogammaglobulinemia, **HP:0004313** |
| Autoimmunity/autoinflammation | Variable; panniculitis, vasculitis, arthritis, retinal vasculitis, pericarditis/serositis, cytopenias and dsDNA antibodies in the original case | Autoimmunity, **HP:0002960**; panniculitis, **HP:0012490** |
| Intestinal inflammation | Prominent with p.Pro440Ser partial loss of function; likely caused by residual conventional CD4 activity plus inadequate Treg control | Inflammatory bowel disease, **HP:0002037** |
| Cutaneous inflammatory plaques | Granulomatous CD68-positive/CD8-positive lesions in one truncating-variant patient; autoimmune attribution remained uncertain | Inflammatory skin lesions; granulomatous dermatitis |
| Epidermodysplasia-verruciformis-like HPV disease | Later-onset, chronic flat warts/pityriasis-versicolor-like lesions in the splice-variant family | Epidermodysplasia verruciformis; verrucae, **HP:0001002** |
| Cutaneous squamous-cell carcinoma | Two of three splice-variant siblings developed carcinoma; one died from disseminated SCC | Squamous-cell carcinoma of skin, **HP:0006739** |
| Hepatosplenomegaly | Reported especially in p.Pro440Ser patients; secondary to infection/inflammation | Hepatosplenomegaly, **HP:0001433** |
| Bronchiectasis/emphysematous bulla | Secondary damage from recurrent infection in an older p.Pro440Ser patient | Bronchiectasis, **HP:0002110** |
| Anemia/cytopenias | Variable; may be inflammatory, infectious, autoimmune or treatment related | Anemia, **HP:0001903** |

### Patient-level quantitative examples

- The p.Ser377LysfsTer14 cousins had CD3 counts of **328 and 69/µL**, CD4 counts of **227 and 29/µL**, and TRECs of **3.5 and 8 copies** against a reference of more than 400. Their B- and NK-cell numbers were largely preserved. [75]
- The p.Pro440Ser brothers had CD3 counts of **494 and 298/µL**, naïve CD4 fractions of **1% and 3%**, and **zero detectable TRECs**. PHA proliferation was 40% and 34% of control; anti-CD3/CD28 responses were 52% and 54%. [284]
- The p.Cys465Arg infant had CD3 **667/µL**, CD4 **289/µL**, CD8 **332/µL**, and simultaneous CMV, EBV and adenovirus viremia. [57]

### Quality-of-life impact

No LCK-specific EQ-5D, SF-36, PROMIS or other validated quality-of-life study exists. Available cases show major effects: repeated hospitalization, mechanical ventilation, chronic diarrhea, poor growth, feeding by gastrostomy, esophageal strictures, skin disease, prolonged antimicrobial treatment and transplant-related morbidity. One successfully transplanted p.Ser377LysfsTer14 patient was infection-free and attending school 4.5 years later, demonstrating the potential for substantial functional recovery. [75]

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

***LCK***, HGNC:6524, is on chromosome **1p35.2** and encodes the Src-family non-receptor tyrosine kinase LCK/p56-LCK, UniProt **P06239**. It is expressed predominantly in lymphoid cells and is essential for thymic selection, T-cell maturation and mature TCR signaling. [104][107]

The protein contains:

1. an N-terminal unique region with membrane-targeting lipid modifications;
2. an SH3 domain;
3. an SH2 domain;
4. a catalytic tyrosine-kinase domain;
5. activating Tyr394; and
6. inhibitory/regulatory Tyr505.

### 4.2 Established disease-causing variants through 2024

| Variant, family and evidence | Type/classification | Population data | Functional consequence |
|---|---|---|---|
| **NM_005356.5:c.1022T>C, p.(Leu341Pro)**; one child; PMID **22985903**, [published 15 Sep 2012](https://pubmed.ncbi.nlm.nih.gov/22985903/) | Missense; ClinVar pathogenic; homozygous through uniparental isodisomy | Extremely rare; rs587777335 | Weak protein expression, absent kinase activity, failure to restore TCR signaling in LCK-null cells. The abstract states: “The mutant LCK protein … was weakly expressed with no kinase activity.” [47][136] |
| **c.188-2A>G**; three Chinese Hui siblings; PMID **27087313**, [published 18 Apr 2016](https://doi.org/10.1111/bjd.14679) | Canonical splice acceptor; ClinVar pathogenic | Absent from 100 ancestry-matched controls; broader frequency not established | Exon 3 skipping, frameshift and mRNA decay; residual long LCK isoform probably explained partial function. [134][278] |
| **c.1393T>C, p.(Cys465Arg)**; one Syrian infant; PMID **38100037**, [issued 15 Dec 2023](https://doi.org/10.1007/s10875-023-01602-8) | Missense; pathogenic in report/ClinVar | Absent from gnomAD; CADD 26.1 | Near-absent protein, absent LCK/ZAP70 activation and calcium flux; distal ERK response rescued by PMA/ionomycin. [168] |
| **c.1129dupA, p.(Ser377LysfsTer14)**; two cousins; PMID **38112969**, [published 19 Dec 2023](https://pubmed.ncbi.nlm.nih.gov/38112969/) | Frameshift/truncating; ClinVar **likely pathogenic** | dbSNP rs1569967422; no population frequency reported | Truncated, unstable, mislocalized protein lacking Tyr394 and Tyr505; absent/markedly reduced ITK, SLP76, ZAP70, calcium and ERK signaling. At matched experimental expression, limited residual signaling remained. [164][166] |
| **c.1318C>T, p.(Pro440Ser)**; two Saudi brothers; PMID **37962568**, [published 1 Jan 2024](https://pubmed.ncbi.nlm.nih.gov/37962568/) | Missense; ClinVar pathogenic | gnomAD allele frequency approximately **0.00001**; CADD 26.1 | Approximately tenfold lower protein, shorter half-life and partial kinase/signaling activity; decreased phosphorylation of LCK Tyr394, CD3ζ, ZAP70 and SLP76. [149][284] |

A 2025 conference abstract described **p.Gly190fs*31** in the SH2-domain region, causing nonsense-mediated decay, absent protein and CID; because this remains an abstract rather than a fully peer-reviewed patient report, it should be treated as preliminary. [409]

**Important ClinVar caution:** many variants are listed under the disease record without human case-level proof. For example, **p.Tyr505Cys is a VUS**, not an established LCK-deficiency allele, even though experimental screening suggests altered T-cell activity. [419][421]

### 4.3 Variant origin and mechanism

- Reported causal variants are **constitutional germline**, not somatic.
- Mechanism: loss of function, ranging from near-null to hypomorphic.
- No pathogenic gain-of-function, dominant-negative or recurrent chromosomal rearrangement has been established for this Mendelian disease.
- No disease-defining copy-number variant, aneuploidy, translocation or inversion has been reported.
- No validated epigenetic signature, disease-specific DNA methylation pattern or histone modification has been identified.
- No established modifier gene exists.

---

## 5. Environmental information

Environmental exposures do not create the genetic disease. Their main roles are:

1. **Microbial exposure:** precipitates infection and may provide inflammatory stimuli to residual T cells.
2. **Live vaccines:** may cause disease in severe cellular immunodeficiency. Some p.Pro440Ser patients tolerated BCG, oral polio and MMR, but this individual observation does not establish safety.
3. **HPV and ultraviolet light:** persistent HPV was causally linked to EV-like lesions and carcinoma in the splice-variant family; UV is a plausible general EV cofactor but was not measured in that family.
4. **Gut microbiota:** a proposed, not proven, driver of colitis in partial LCK function.
5. **Lifestyle/toxin factors:** no disease-specific association with diet, exercise, smoking, alcohol, pollution, radiation or occupation has been demonstrated.

There is no zoonotic transmission: LCK deficiency is inherited, not contagious.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **Biallelic pathogenic *LCK* variation leads to** absent, unstable, truncated or catalytically impaired LCK protein.
2. **Defective LCK leads to** reduced phosphorylation of CD3/TCRζ ITAMs after TCR engagement.
3. **Reduced ITAM phosphorylation leads to** inadequate recruitment and activation of ZAP70.
4. **Defective ZAP70 activation leads to** reduced phosphorylation of LAT, SLP76 and ITK, with impaired PLCγ1 signaling.
5. **Impaired proximal signaling leads to** absent or reduced intracellular calcium mobilization and diminished ERK/MAPK, NFAT and other activation outputs; AKT–mTOR signaling may be partially preserved in some hypomorphic/truncating alleles.
6. **Weak pre-TCR/TCR signaling in the thymus leads to** impaired DN3-to-DN4 progression, positive selection and maturation of CD4/CD8 αβ thymocytes.
7. **Reduced thymic output leads to** low TRECs, profound naïve αβ T-cell lymphopenia, reduced CD4/CD8 surface expression and a restricted TCR repertoire.
8. **T-cell lymphopenia and poor effector activation lead to** defective cellular immunity and deficient T-cell help to B cells, resulting in recurrent bacterial, viral, fungal and opportunistic infection, with variable hypogammaglobulinemia.
9. **Branch A—near-null function leads to** overwhelming infection and early death unless immune reconstitution is achieved.
10. **Branch B—partial residual signaling leads to** survival and homeostatic expansion of a limited conventional T-cell population.
11. **Residual conventional T-cell activity combined with inadequate Treg number/function leads to** immune dysregulation and tissue inflammation; in p.Pro440Ser disease, the gut-microbiota contribution is inferred rather than demonstrated.
12. **Failure of antiviral T-cell surveillance leads to** persistent HPV infection and, in the splice-variant family, virus-associated cutaneous squamous-cell carcinoma.

### 6.2 Normal pathway and protein dysfunction

Normally, CD4- or CD8-associated LCK is activated after TCR–MHC engagement. Active LCK phosphorylates ITAMs in CD3 and TCRζ, initiating ZAP70–LAT–SLP76–ITK–PLCγ1 signaling and downstream calcium, Ras–MAPK, cytoskeletal and transcriptional responses. Reactome places LCK at the proximal “phosphorylation of CD3 and TCR zeta chains” step. [106][111]

The recent human data show allele-dependent disruption:

- **Leu341Pro and Cys465Arg:** essentially signaling-null.
- **Ser377LysfsTer14:** very low expression, mislocalization and almost absent signaling at physiological levels, but some calcium/ERK response when experimentally expressed at matched levels.
- **Pro440Ser:** partial loss of function, sufficient for limited T-cell development and inflammatory activity.
- **c.188-2A>G:** partial expression through an unaffected longer isoform, probably accounting for survival into adulthood and an HPV-dominant phenotype.

The 2024 p.Pro440Ser abstract concluded:

> “These findings demonstrate that P440S LCK spares sufficient T cell function to allow the maturation of some conventional T cells but not regulatory T cells—leading to intestinal inflammation.” [284]

### 6.3 Cells, tissues and ontology suggestions

**Suggested GO biological processes**

- T-cell receptor signaling pathway — **GO:0050852** [390]
- T-cell activation — **GO:0042110**
- T-cell differentiation in thymus — **GO:0033077**
- Thymic T-cell selection — **GO:0045061**
- Calcium-mediated signaling — **GO:0019722**
- Positive regulation of lymphocyte proliferation — **GO:0050671**
- Protein tyrosine phosphorylation — **GO:0018108**
- Immune response-regulating cell-surface receptor signaling — **GO:0002768**

**Suggested molecular functions**

- Protein tyrosine kinase activity — **GO:0004713**
- ATP binding — **GO:0005524**
- SH2-domain binding — **GO:0042169**

**Suggested Cell Ontology terms**

- T cell — **CL:0000084**
- CD4-positive αβ T cell — **CL:0000624**
- CD8-positive αβ T cell — **CL:0000625**
- γδ T cell — **CL:0000798** [381]
- Naïve T cell — **CL:0000898**
- Double-positive αβ thymocyte — **CL:0000809**
- CD4-positive αβ thymocyte — **CL:0000810** [401]
- Regulatory T cell and CD4-positive/CD25-positive αβ regulatory T-cell terms in the current CL release
- B cell — **CL:0000236**
- Natural killer cell — **CL:0000623**
- Macrophage — **CL:0000235**

### 6.4 Metabolic, profiling and advanced-technology findings

No reproducible disease-specific metabolomic, lipidomic, epigenomic, spatial-transcriptomic, single-cell or multi-omic signature has been published. Existing molecular profiling consists mostly of:

- phosphoprotein immunoblotting/flow cytometry;
- calcium-flux assays;
- TCR Vβ flow analysis;
- high-throughput TRG repertoire sequencing;
- protein-expression and localization studies; and
- structure/modeling simulations.

Thus, claims about altered energy metabolism, autophagy, mitochondrial dysfunction or oxidative stress would presently be speculative.

---

## 7. Anatomical structures affected

| Level | Structures/cells | Interpretation and ontology suggestions |
|---|---|---|
| Primary organ | **Thymus**, UBERON:0002370 | Defective thymocyte development and selection; thymic tissue was not routinely biopsied in patients but is strongly supported by TRECs and mouse models. [388] |
| Primary system | Blood/immune system, blood UBERON:0000178 | Low circulating T cells, loss of naïve compartments and impaired function |
| Secondary organs | Lung, UBERON:0002048 | Pneumonia, respiratory failure, bronchiectasis, bulla |
| Secondary organs | Small and large intestine, UBERON:0002108 and UBERON:0000059 | Infection-associated diarrhea and allele-dependent immune-mediated inflammation |
| Secondary organs | Skin, UBERON:0002097 | Panniculitis, granulomatous plaques, HPV warts, EV and SCC |
| Secondary organs | Spleen, UBERON:0002106; lymph nodes, UBERON:0000029 | Immune-cell compartments; hepatosplenomegaly can occur |
| Secondary sites | Oral cavity/esophagus | Candidiasis and, in one patient, candidal esophageal strictures |
| Subcellular | Plasma membrane, **GO:0005886**; immunological synapse, **GO:0001772**; cytoplasm, **GO:0005737** | LCK is membrane-associated and concentrates at the TCR/co-receptor signaling interface. [374] |

There is no meaningful lateralization. Bilateral lung disease can occur, but laterality is not intrinsic to LCK deficiency.

---

## 8. Temporal development

- **Molecular onset:** congenital.
- **Typical clinical onset:** birth through the first year, especially for near-null variants. The p.Pro440Ser brothers presented in the first days of life and at 1.5 months; the p.Cys465Arg patient became ill at six months; the truncating-variant patients developed infections in infancy. [57][284]
- **Partial/splice disease:** may evolve more slowly, with HPV skin disease and carcinoma emerging in adolescence or early adulthood.
- **Course without definitive therapy:** chronic and often progressive, with repeated infections, cumulative lung/GI injury and possible malignancy.
- **Immune trajectory:** progressive depletion of naïve T cells and homeostatic expansion of memory/effector or γδ populations.
- **Remission:** spontaneous immunologic remission has not been documented. Temporary infection control can follow antimicrobials and immunoglobulin; durable remission requires successful immune reconstitution.
- **Critical intervention window:** before severe infection and ideally in early infancy. In general SCID cohorts, age under 3.5 months and absence of active infection at HCT are major predictors of survival. [341]

---

## 9. Inheritance and population

### 9.1 Inheritance

- **Autosomal recessive**
- Both sexes are affected.
- For two carrier parents, each pregnancy has a **25% affected, 50% carrier and 25% unaffected/non-carrier** probability.
- Heterozygous carriers are usually clinically unaffected.
- Penetrance for proven biallelic severe loss-of-function variants appears high, but formal penetrance cannot be calculated.
- Expressivity is markedly variable and correlates broadly with residual LCK function.
- No anticipation, germline mosaicism or confirmed founder effect has been reported.
- Consanguinity is prominent in the reported families but is not required.

### 9.2 Epidemiology

No prevalence, incidence, carrier-frequency, sex-ratio or geographic-rate estimate specific to LCK deficiency exists. Reports include families of European, Chinese Hui, Syrian, Israeli/consanguineous and Saudi ancestry, arguing against a single endemic population.

By the end of 2024, the principal literature contained roughly:

- 1 p.Leu341Pro patient;
- 3 c.188-2A>G siblings;
- 1 p.Cys465Arg patient;
- 2 p.Ser377LysfsTer14 cousins; and
- 2 p.Pro440Ser brothers.

That is approximately **nine genetically established affected people in five families**, far too few for meaningful epidemiologic rates. GenCC’s evidence set contains five principal variants/publications. [289]

For context only—not an LCK-specific rate—population newborn screening detects all genetic forms of SCID at approximately **1 per 58,000 births** in US screening programs. [191]

---

## 10. Diagnostics

### 10.1 Recommended diagnostic approach

1. **Urgent screening/confirmation**
   - CBC with differential and absolute lymphocyte count.
   - Flow cytometry for CD3, CD4, CD8, CD19/20 and CD16/56.
   - Naïve/memory T-cell markers, especially CD45RA/CCR7 and recent thymic emigrants.
   - TRECs.
   - Immunoglobulins and vaccine-specific antibodies.
   - T-cell proliferation to PHA and anti-CD3/CD28.
   - Viral PCR and pathogen-directed evaluation.

2. **LCK-directed clues**
   - Measure CD4 and CD8 surface mean fluorescence intensity, not only cell percentages.
   - Examine γδ versus αβ T cells.
   - TCR repertoire analysis.
   - Intracellular LCK protein expression.
   - If available, TCR-induced phosphorylation of LCK, CD3ζ, ZAP70, SLP76/ITK and ERK, plus calcium flux.

Reduced CD4 surface expression is repeatedly proposed as a useful hallmark:

> “A diagnostic hallmark of this immunodeficiency is the reduced surface expression of CD4.” [75]

It is a clue rather than a stand-alone criterion.

3. **Molecular confirmation**
   - A comprehensive SCID/CID or inborn-error-of-immunity NGS panel including ***LCK*** is usually the fastest approach.
   - WES is proven useful: it identified p.Cys465Arg, p.Ser377LysfsTer14 and p.Pro440Ser.
   - WGS is reasonable when panel/WES testing is negative, especially for intronic, regulatory, copy-number or structural variants.
   - Confirm candidate variants by Sanger sequencing and parental/family segregation.
   - RNA studies are useful for suspected splice variants.
   - Single-gene testing is efficient when the biochemical phenotype or familial variant is already known.

CMA, karyotyping and FISH are not first-line because the established disease is sequence-level and recessive. Mitochondrial DNA and repeat-expansion testing are not relevant unless another diagnosis is suspected.

### 10.2 Newborn screening

TREC-based SCID newborn screening should detect most severe LCK cases because reported severe patients had absent or profoundly reduced TRECs. However, hypomorphic patients with residual thymic output could theoretically escape threshold-based screening; direct sensitivity for LCK deficiency has not been established.

A 2023 review found TREC screening to have **100% sensitivity for typical SCID in reported case series**, while positive predictive value varied because many positive screens identify non-SCID T-cell lymphopenia. [192][193]

### 10.3 Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| *IL2RG*, *JAK3*, *ADA*, *RAG1/2*, *DCLRE1C*, *IL7R* SCID | T/B/NK pattern, enzyme testing and genotype; LCK often has reduced CD4/CD8 surface density and residual leaky phenotype |
| *ZAP70* deficiency | Often normal/preserved CD4 numbers with absent CD8 T cells; signaling block downstream of LCK |
| *LAT*, *LCP2/SLP76*, *ITK* deficiency | Other proximal TCR defects; overlapping infection and immune dysregulation |
| MHC class II deficiency | Severe CD4 lymphopenia but absent HLA-DR/DQ/DP expression on antigen-presenting cells |
| *STK4*, *RHOH*, *CARMIL2*, *DOCK8* deficiency | Viral skin disease/warts with different immunophenotypes and syndromic findings |
| *TMC6/TMC8/CIB1* epidermodysplasia verruciformis | Predominantly keratinocyte-intrinsic β-HPV susceptibility, generally without broad CID |
| Idiopathic CD4 lymphocytopenia/HIV | Acquired or diagnosis-of-exclusion; lacks biallelic *LCK* defect |
| Omenn syndrome | Erythroderma, eosinophilia, high IgE and activated oligoclonal T cells |
| Secondary immunodeficiency | HIV, immunosuppressive drugs, malignancy, malnutrition or protein loss |

---

## 11. Outcome and prognosis

There are no disease-specific five- or ten-year survival estimates.

### Reported outcomes

- **p.Leu341Pro:** HSCT attempted; death at 30 months, seven days after transplant. [306]
- **c.188-2A>G family:** two siblings died in their early twenties—one from disseminated SCC and one from unknown causes; status of the third was not clearly reported. [278]
- **p.Cys465Arg:** HSCT was declined; death at 12 months after severe pneumonia/respiratory failure. [57]
- **p.Ser377LysfsTer14:** one child remained well, infection-free and in school 4.5 years after HSCT despite 20% donor chimerism; the second died from *Candida glabrata*/VRE septic shock 20 days after HSCT. [75]
- **p.Pro440Ser:** the older brother died from pneumonia 102 days after HSCT; the younger survived initial transplant complications and was discharged seven months after HSCT. [284]

These outcomes must not be converted into a formal response or mortality rate because of tiny numbers, variable alleles, publication bias and different transplant eras.

### Prognostic factors

Likely favorable:

- early diagnosis;
- preserved clinical status;
- clearance of active infection before HSCT;
- younger transplant age;
- suitable donor and successful durable engraftment.

Likely adverse:

- near-null LCK activity;
- profound naïve T-cell depletion and very low TRECs;
- active CMV, fungal or other systemic infection;
- failure to thrive and established organ damage;
- HPV-associated malignancy;
- poor engraftment or severe transplant infection.

Across 902 patients with all forms of SCID, five-year survival rose to **87% in 2010–2018**, and was **92.5%** among newborn-screen-identified children. Active infection at HCT carried an HR of **2.41** for mortality and age ≥3.5 months an HR of **2.12**; these are informative but are not LCK-specific estimates. [337][341]

---

## 12. Treatment

### 12.1 Treatment strategy

| Stage | Intervention | Purpose/evidence | Suggested NCIt intervention label |
|---|---|---|---|
| Suspected SCID/CID | Protective precautions; urgent immunology and transplant-center referral | Prevent exposure while completing diagnosis | Protective Isolation |
| Infection prevention | TMP-SMX or alternative Pneumocystis prophylaxis; antifungal/antiviral prophylaxis individualized | Standard SCID supportive management [195] | Anti-Infective Agent; Antibiotic Prophylaxis |
| Humoral support | IVIG or SCIG | Replaces deficient antibody and mitigates secondary B-cell dysfunction | Intravenous Immunoglobulin; Subcutaneous Immunoglobulin |
| Active infection | Pathogen-directed antibacterial, antiviral, antifungal or antiparasitic therapy | Essential before and during HSCT | Antimicrobial Therapy |
| Definitive therapy | **Allogeneic HSCT/HCT** | Replaces defective hematopoietic immune system; successful long-term infection-free survival has been documented | Allogeneic Hematopoietic Stem Cell Transplantation |
| HPV/skin surveillance | Dermatologic examinations, biopsy of suspicious lesions, SCC excision/oncologic management | Important for hypomorphic/EV phenotype | Dermatologic Examination; Surgical Excision |
| Nutritional/organ support | Enteral feeding, management of diarrhea, pulmonary care | Treats failure to thrive and organ complications | Nutritional Support; Supportive Care |
| Rehabilitation | PT/OT and developmental support as individually required | No LCK-specific rehabilitation protocol | Physical Therapy; Occupational Therapy |

### 12.2 HSCT considerations

HSCT is the only established potentially curative therapy. Conditioning and donor choice should follow current EBMT/ESID or experienced SCID-center protocols rather than an LCK-specific algorithm. Reported LCK cases have used matched related, mismatched unrelated and haploidentical donors with mixed success.

Current SCID practice also recommends:

- no live vaccines;
- CMV-safe, irradiated and leukoreduced blood products;
- Pneumocystis prophylaxis;
- immunoglobulin replacement;
- aggressive infection surveillance; and
- BCG prophylaxis/treatment where prior vaccination creates risk. [194][198]

### 12.3 Pharmacotherapy and pharmacogenomics

No drug corrects the LCK defect. Corticosteroids, cyclosporine and mycophenolate produced only a partial response in one patient’s inflammatory skin lesions and increased immunosuppression can worsen infection risk. [75]

There is no validated pharmacogenomic rule linking an *LCK* genotype to antimicrobial, immunoglobulin or conditioning-drug dosing.

### 12.4 Experimental treatment

- No LCK-specific gene-replacement, CRISPR, RNA or targeted-drug clinical trial was identified.
- Ex vivo correction of autologous hematopoietic stem cells is conceptually possible but remains preclinical.
- LCK inhibitors are biologically inappropriate for restoring a loss-of-function state and could aggravate immunodeficiency.
- Experimental Treg transfer prevented intestinal inflammation in p.Pro440Ser mice, but this is mechanistic evidence, not a human treatment. [284]

---

## 13. Prevention

### Primary prevention

The inherited mutation cannot be prevented by lifestyle modification. Primary reproductive prevention options include:

- preconception carrier testing for known family variants;
- cascade testing of relatives;
- preimplantation genetic testing for monogenic disease;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis; and
- use of donor gametes where desired.

For two carriers, recurrence risk is 25% in every pregnancy. [320][321]

### Secondary prevention

- Universal TREC newborn screening.
- Immediate flow-cytometric confirmation of an abnormal result.
- Targeted testing at birth in an at-risk family even if newborn screening is normal.
- Early donor search and transplant planning.
- Prenatal diagnosis can permit delivery near a specialist SCID center.

### Tertiary prevention

- Immunoglobulin and antimicrobial prophylaxis.
- Avoid live vaccines such as BCG, rotavirus, oral polio and MMR until specialist-confirmed immune reconstitution.
- Household infection precautions and avoidance of unpasteurized/high-risk foods where advised.
- Irradiated, leukoreduced, CMV-safe blood products.
- HPV/skin surveillance and sun protection in patients with EV-like disease.
- Pulmonary monitoring after recurrent pneumonia.
- Monitor growth, nutrition, liver function, CMV/EBV and transplant complications.

Inactivated vaccines should be deferred or individualized during profound immunodeficiency and immunoglobulin replacement; revaccination after successful HSCT follows transplant-center immune-reconstitution protocols.

---

## 14. Other species and natural disease

No naturally occurring, molecularly confirmed LCK-deficiency syndrome was identified in a companion-animal breed, livestock or wildlife. Therefore:

- no OMIA disease entry, breed association or VBO breed term can presently be assigned;
- veterinary prevalence and zoonotic potential are not applicable;
- cross-species relevance comes from evolutionary conservation and engineered models, not natural disease.

### Orthologs

| Species | Taxon | Ortholog |
|---|---:|---|
| Human | NCBI Taxon **9606** | *LCK*, NCBI Gene **3932** |
| Mouse | NCBI Taxon **10090** | *Lck*, NCBI Gene **16818**, MGI:96756 [260] |
| Rat | NCBI Taxon **10116** | *Lck*, RGD:2994 [255] |
| Zebrafish | NCBI Taxon **7955** | *lck*, NCBI Gene **414333** [259] |
| *Xenopus tropicalis* | NCBI Taxon **8364** | *lck*, Xenbase:XB-GENE-6054021 [257] |

Porcine LCK is approximately 96% identical to human LCK, illustrating strong vertebrate conservation, but no porcine immunodeficiency phenotype has been attributed to natural *LCK* variants. [253]

---

## 15. Model organisms and experimental systems

| Model | Principal findings | Strengths and limitations |
|---|---|---|
| **Lck-null mouse** | Thymic atrophy, dramatic loss of CD4/CD8 double-positive thymocytes, no mature single-positive thymocytes and very few peripheral T cells | Strong model of near-null human disease and thymic block; does not reproduce inflammatory manifestations of hypomorphic human alleles. Landmark PMID **1579166**. [224] |
| **Lck p.Pro440Ser knock-in mouse** | 20–50-fold lower Lck, profound T-cell lymphopenia, reduced CD4/CD8 expression, skewed memory phenotype, reduced Tregs, colitis, weight loss and splenomegaly | Best allele-specific model of human partial LCK deficiency. Colitis was prevented by CD4 depletion or WT Treg transfer. Mouse microbiome and immune development may differ from humans. [247] |
| **FOXP3-GFP/Treg-transfer experiments** | WT Tregs normalized multiple colitis measures in p.Pro440Ser mice | Demonstrates causal Treg insufficiency in the model, not yet validated therapeutically in patients |
| **LCK-null Jurkat/J.CaM1.6 cells** | Reconstitution with WT versus mutant LCK measures protein stability, localization, phosphorylation, calcium and ERK output | Powerful for variant function; transformed cell line, lacks thymic developmental context |
| **Doxycycline-inducible matched-expression Jurkat model** | p.Ser377LysfsTer14 supported limited calcium and ERK signaling when expressed sufficiently | Separates intrinsic residual activity from low protein abundance; overexpression can exaggerate residual function |
| **Primary patient T cells** | Direct evidence of reduced protein, defective TCR phosphorylation, calcium flux, activation, proliferation and degranulation | Highest human relevance but very limited cell numbers and confounding by infection/treatment |
| **Healthy PBMC plus LCK inhibitor A770041** | Reproduced major proximal-signaling defects while suggesting some mTOR phosphorylation is LCK independent | Pharmacologic inhibition may not precisely model congenital structural variants |
| **TCR-repertoire sequencing** | Oligoclonality/restricted diversity and expanded γδ clones in truncating-variant patients | Provides molecular readout of limited thymic output; no large controls or longitudinal data |

The mouse evidence supports a key genotype–mechanism principle: **complete loss of LCK prevents enough conventional T-cell function to produce profound immunodeficiency, whereas partial loss permits a small, dysregulated T-cell compartment capable of tissue inflammation.** The p.Pro440Ser paper states:

> “While both *Lck*−/− and *Lck*P440S/P440S mice exhibit arrested thymic T cell development and profound T cell lymphopenia, only *Lck*P440S/P440S mice show residual T cell proliferation, cytokine production, and intestinal inflammation.” [284]

---

## Recent developments and expert interpretation

The most consequential 2023–2024 advances were:

1. **Expansion beyond the original two genetic presentations:** p.Cys465Arg, p.Ser377LysfsTer14 and p.Pro440Ser established a broader allelic spectrum. [438]
2. **Recognition of reduced CD4 surface expression as a diagnostic clue**, not merely low CD4-cell number. [75]
3. **Demonstration of residual signaling in truncating/hypomorphic alleles**, explaining “leaky” CID rather than uniform T-negative SCID.
4. **Allele-specific mouse evidence for immune dysregulation:** partial LCK activity can be more inflammatory than complete absence because conventional effector cells persist while Treg control is inadequate. [284]
5. **Definitive gene–disease validity:** the GenCC/ClinGen classification changed from moderate to definitive in 2025 as the new 2023–2024 cases and functional evidence accumulated. [289]

A 2025/2026 expert review summarizes the present model: loss-of-function variants cause combined immunodeficiency with defective differentiation and signaling, while hypomorphic alleles retaining activity can promote immune dysregulation and autoimmunity. [445]

## Knowledge gaps

- True prevalence, incidence, carrier frequency and penetrance
- Prospective natural history and standardized quality-of-life outcomes
- Allele-specific newborn-screen sensitivity
- Optimal conditioning, donor selection and chimerism targets for HSCT
- Long-term outcomes after successful transplantation
- Human confirmation of the microbiota–Treg–colitis mechanism
- Disease-specific single-cell, spatial, proteomic and metabolomic profiles
- Safe autologous gene-replacement or editing strategies
- Natural LCK deficiency in nonhuman species

Overall, LCK deficiency should be entered in a knowledge base as an **autosomal-recessive, loss-of-function TCR-signaling disorder with a continuum from profound SCID-like disease to hypomorphic CID with inflammation or HPV-associated malignancy**, rather than as a uniform classic SCID phenotype.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 5 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014334` (3 mentions) - the report calls it "MONDO"; MONDO calls it **severe combined immunodeficiency due to LCK deficiency**
- `DOID:0111937` (2 mentions) - the report calls it "Disease Ontology"; DOID calls it **immunodeficiency 22**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005407` (obsolete Decreased proportion of CD4-positive helper T cells) (1 mention) - replaced by `HP:0032218`
- `HP:0001002` (obsolete Decreased subcutaneous fat) (1 mention) - replaced by `HP:0003758`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`, `RGD`.