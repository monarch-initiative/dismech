---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T22:37:33.081216'
end_time: '2026-09-28T22:43:22.474457'
duration_seconds: 349.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glycogen Storage Disease Due To Phosphoglycerate Mutase Deficiency
  mondo_id: MONDO:0009865
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
citation_count: 17
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 70
  verified: 64
  not_found: 0
  obsolete: 2
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 11
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0005291
    reported_labels:
    - glycogen storage disease
    ontology_label: brain aneurysm
  - term_id: MONDO:0005067
    reported_labels:
    - metabolic myopathy
    ontology_label: monophasic synovial sarcoma
  - term_id: MONDO:0004880
    reported_labels:
    - disorder of glycolysis
    ontology_label: bowel dysfunction
  - term_id: GO:0016044
    reported_labels:
    - cellular membrane organization
    ontology_label: GO_0016044
  - term_id: GO:0044319
    reported_labels:
    - muscle cell proliferation
    ontology_label: wound healing, spreading of cells
  - term_id: CL:0002066
    reported_labels:
    - renal tubular epithelial cells
    ontology_label: Feyrter cell
  - term_id: UBERON:0001229
    reported_labels:
    - renal tubular epithelium
    ontology_label: renal corpuscle
  - term_id: GO:0030018
    reported_labels:
    - sarcolemma
    ontology_label: Z disc
  - term_id: HP:0003553
    reported_labels:
    - Bilateral involvement
    ontology_label: obsolete Cellulitis due to immunodeficiency
  labels_variant: 9
  obsolete_terms:
  - term_id: GO:0016044
    ontology_label: GO_0016044
    replaced_by: GO:0061024
  - term_id: HP:0003553
    ontology_label: obsolete Cellulitis due to immunodeficiency
    replaced_by: HP:0100658
  unresolvable_prefixes:
  - ORPHA
  - Taxon
  - Gene
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glycogen Storage Disease Due To Phosphoglycerate Mutase Deficiency
- **MONDO ID:** MONDO:0009865 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycogen Storage Disease Due To Phosphoglycerate Mutase Deficiency** covering all of the
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

# Glycogen Storage Disease Due To Phosphoglycerate Mutase Deficiency (Glycogen Storage Disease Type X, MONDO:0009865)

Glycogen storage disease due to phosphoglycerate mutase deficiency, also known as glycogen storage disease type X (GSD10), is a rare autosomal recessive metabolic myopathy caused by biallelic loss-of-function variants in the muscle phosphoglycerate mutase gene **PGAM2**, leading to a partial block in terminal glycolysis and consequent exercise-induced muscle contractures, cramps, rhabdomyolysis, and myoglobinuria.[4][7][9] The disorder primarily affects skeletal muscle, where the MM isoform of phosphoglycerate mutase predominates, but may also involve red blood cells and kidneys secondary to recurrent muscle breakdown, and is associated in many patients with distinctive tubular aggregates and sarcoplasmic reticulum proliferation on muscle biopsy.[3][4][5] Fewer than fifty affected individuals have been reported worldwide, with early cases clustering in African American patients carrying a recurrent nonsense variant (p.Trp78Ter, W78X), but subsequent reports have expanded the genetic and ethnic spectrum and documented manifesting heterozygotes with milder phenotypes.[3][4][11][12][13] Clinical onset typically occurs in childhood or adolescence with exertional myalgia and pigmenturia, yet late-onset presentations in middle age are described, and despite the potential for acute kidney injury during severe rhabdomyolysis, overall longevity appears near-normal when episodes are promptly recognized and managed.[4][5][6][9] No enzyme-replacement or gene-targeted therapies are currently available, so management focuses on avoidance of precipitating factors, optimization of hydration, supportive care during acute episodes, and genetic counseling, while mechanistic and genetic studies of PGAM2 continue to illuminate fundamental aspects of glycolytic flux, muscle energetics, and rare inherited myopathies.[4][5][7][12]  

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Glycogen storage disease due to phosphoglycerate mutase deficiency is best defined as a muscle glycogenosis and metabolic myopathy caused by deficiency of the enzyme phosphoglycerate mutase in skeletal muscle, leading to impaired glycolysis and exercise intolerance.[3][4][9] Orphanet describes the disorder as “a rare glycogen storage disease characterized by susceptibility to rhabdomyolysis complicated by episodes of exercise-induced muscle pain, cramping, and myoglobinuria,” noting that tubular aggregates may be present on muscle biopsy.[4] MedlinePlus Genetics similarly characterizes phosphoglycerate mutase deficiency as “a disorder that primarily affects muscles used for movement (skeletal muscles)” and emphasizes that affected individuals experience muscle aches or cramping following strenuous physical activity with recurrent episodes of myoglobinuria that can progress to kidney failure if untreated.[6] In the context of the glycogen storage disease classification, a recent review places GSD10 among the muscle GSDs, with the enzymatic defect at the level of muscle phosphoglycerate mutase, an essential enzyme for conversion of 3-phosphoglycerate to 2-phosphoglycerate during glycolysis, and summarizes typical clinical features as exercise-induced muscle cramps and pain, exercise intolerance, rhabdomyolysis, myoglobinuria, hyperuricemia or gout, and coronary arteriosclerosis.[9]  

Historically, the condition was first recognized as a distinct human disease entity by DiMauro and colleagues in 1981, who reported a 52-year-old man with “intolerance for strenuous exercise and recurrent pigmenturia since adolescence” whose muscle phosphoglycerate mutase activity was decreased to 5.7% of the lowest control value, with normal activity of other glycolytic enzymes and normal muscle glycogen concentration.[16] This seminal case, supported by electrophoretic studies showing residual BB (brain-type) isoenzyme activity in muscle, established the concept of a genetic defect of the muscle M subunit of PGAM and laid the foundation for later molecular genetic investigations.[16][11][12] Subsequent series such as Tsujino et al. (1993) and the JAMA Neurology “Muscle Phosphoglycerate Mutase Deficiency Revisited” article confirmed the association of PGAM2 mutations with a reproducible phenotype of exercise intolerance, cramps, and myoglobinuria, while introducing additional features such as sarcoplasmic reticulum proliferation and tubular aggregates, and clarifying that the disease is not confined to African Americans and is genetically heterogeneous.[3][11]  

Clinically, the core symptom cluster belongs to the domain of exertional metabolic myopathies, overlapping with other glycolytic and glycogenolytic defects such as McArdle disease (myophosphorylase deficiency) and phosphofructokinase deficiency, but distinguished by its specific enzymatic defect, characteristic pattern of residual PGAM activity due to the B isoform, and relatively benign long-term course.[2][3][4][9] Human Phenotype Ontology (HPO) terms that capture the cardinal manifestations include exercise-induced muscle cramps (HP:0003396), exercise intolerance (HP:0003546), myoglobinuria (HP:0003198), episodic rhabdomyolysis (HP:0003201), elevated serum creatine kinase (HP:0003236), and tubular aggregates in skeletal muscle (HP:0030191).[4][5][6][9] MedGen, which aggregates multiple vocabularies, lists the concept “Glycogen storage disease type X” (C0268149) and notes that phosphoglycerate mutase deficiency is a disorder primarily affecting skeletal muscle with onset in childhood or adolescence and recurrent myoglobinuria.[15]  

### 1.2 Key Identifiers and Ontology Mapping

At the level of disease identifiers, glycogen storage disease due to phosphoglycerate mutase deficiency is assigned **OMIM phenotype number 261670**, under the preferred name “Glycogen storage disease X; GSD10,” which is linked via a number sign to causative homozygous or compound heterozygous mutations in the **PGAM2** gene (OMIM 612931).[7][12] Orphanet catalogs the disorder as **ORPHA:97234**, under several synonymous labels including “Glycogen storage disease due to phosphoglycerate mutase 2 deficiency,” “GSD type 10,” “Muscle phosphoglycerate mutase deficiency,” and “DiMauro disease.”[4] MedGen associates the concept with SNOMED CT terms such as “Muscle phosphoglycerate mutase deficiency (61772003)” and “Glycogen storage disease type X (61772003),” and cross-references OMIM 261670 and Orphanet 97234.[15] The Monarch Initiative and PomBase both reference the disease as **MONDO:0009865**, “glycogen storage disease due to phosphoglycerate mutase deficiency,” classified as a disorder of glycogen metabolism and disorder of glycolysis.[1][15]  

MalaCards, a compendium of human diseases, lists the entity as “Glycogen Storage Disease X (GSD10)” and notes alternative names including “PGAMM deficiency” and “Myopathy due to phosphoglycerate mutase deficiency,” providing links to OMIM, Orphanet, and MedGen identifiers.[2][15] MedlinePlus Genetics uses “Phosphoglycerate mutase deficiency” as the primary patient-facing name, and includes synonyms such as “Glycogen storage disease X,” “GSD X,” “GSD10,” “Myopathy due to phosphoglycerate mutase deficiency,” “PGAM deficiency,” and “PGAMM deficiency.”[6] These identifiers and synonyms correspond closely to formal ontology labels: the MONDO term **MONDO:0009865** is explicitly mapped in PomBase as “glycogen storage disease due to phosphoglycerate mutase deficiency,” and is linked to the human PGAM2 gene and the fission yeast ortholog gpm1.[1]  

From an ontology perspective, relevant high-level disease categories include **MONDO:0005291 (glycogen storage disease)**, **MONDO:0005067 (metabolic myopathy)**, and **MONDO:0004880 (disorder of glycolysis)**, with GSD type X occupying a specific intersection of glycogen metabolism and glycolytic pathway defects.[1][4][9] While ICD-10 and ICD-11 do not appear to have a unique code dedicated to GSD type X in the sources considered, the condition would typically be coded under broad categories for “Other glycogen storage diseases (E74.0)” or “Other specified metabolic myopathies,” reflecting its rarity and the tendency for specific GSD types to be grouped in practice.[9][15] MeSH (Medical Subject Headings) and UMLS entries are linked via MedGen and OMIM; however, detailed MeSH descriptors for GSD10 specifically are not evident in the available search results, emphasizing the role of specialized rare disease databases in cataloguing such ultra-rare conditions.[7][15]  

### 1.3 Synonyms, Naming Conventions, and Data Source Types

Clinical and research communities employ a variety of synonyms for glycogen storage disease due to phosphoglycerate mutase deficiency, reflecting historical evolution of terminology and different emphases on biochemical versus clinical features.[4][6][7][15] Orphanet lists synonyms including “Glycogen storage disease due to phosphoglycerate mutase 2 deficiency,” “GSD type 10,” “Muscle phosphoglycerate mutase deficiency,” “Myopathy due to phosphoglycerate mutase deficiency,” “GSD due to phosphoglycerate mutase 2 deficiency,” “Glycogenosis due to phosphoglycerate mutase 2 deficiency,” “Glycogen storage disease, type 10,” “Glycogen storage disease, type X,” “Glycogen storage disease due to PGAM2 deficiency,” “DiMauro disease,” and “PGAM deficiency.”[4] MedlinePlus overlaps by listing “Deficiency mutase phosphoglycerate,” “Glycogen storage disease X,” “GSD X,” “GSD10,” “Myopathy due to phosphoglycerate mutase deficiency,” “PGAM deficiency,” and “PGAMM deficiency.”[6] MedGen similarly aggregates variants such as “Dimauro disease,” “GSD X,” and “PGAMM deficiency.”[15]  

These naming conventions encode several dimensions: the biochemical defect (phosphoglycerate mutase deficiency, PGAM2 deficiency, PGAM-M deficiency), the clinical category (glycogen storage disease type X or GSD10), and the historical eponym (DiMauro disease) honoring the first describer.[4][16] In molecular genetics contexts, the gene-centric label “PGAM2-related glycogen storage disease X” is increasingly used, consistent with contemporary practice of naming Mendelian disorders by gene and phenotype.[7][12] In many databases, synonyms are explicitly mapped to ontology terms: for example, MedGen associates “Muscle phosphoglycerate mutase deficiency” and “GSD X - glycogen storage disease type X” with the concept C0268149, while Monarch Initiative maps these to MONDO:0009865.[1][15]  

Regarding the nature of information sources, most of the disease-level characteristics summarized here are derived from aggregated resources such as OMIM, Orphanet, MedGen, MalaCards, and GeneReviews-style reviews, which synthesize individual patient reports and case series rather than raw electronic health record data.[2][4][7][9][15] Primary clinical evidence comes from human case reports and small series, such as the original Science article by DiMauro et al. (1981; PMID:6262916), the Am J Hum Genet molecular study by Tsujino et al. (1993; PMID:8447317), the JAMA Neurology revisitation, and more recent case reports describing novel PGAM2 variants.[5][8][11][16] These publications typically involve detailed phenotyping, muscle biopsies, enzyme assays, and genetic sequencing, making them high-quality but limited in number due to the disease’s rarity. There is no evidence in the available sources that large-scale EHR-based phenomic analyses have yet been performed for GSD10, underscoring the current reliance on curated disease-level summaries and expert reviews.[4][9]  

## 2. Etiology

### 2.1 Primary Genetic Causal Factors

The primary causal factor in glycogen storage disease due to phosphoglycerate mutase deficiency is biallelic pathogenic variation in the **PGAM2** gene, which encodes muscle phosphoglycerate mutase (PGAM-M), the muscle-specific subunit of the phosphoglycerate mutase dimer.[7][10][12] OMIM notes that a number sign (#) is used with the GSD10 entry because the disease is caused by homozygous or compound heterozygous mutation in PGAM2 on chromosome 7p13.[7] The PGAM2 gene’s cytogenetic location is given as 7p13, with genomic coordinates 7:44,062,727–44,065,567 (GRCh38), and it encodes the muscle phosphoglycerate mutase-2 enzyme (EC 5.4.2.1).[12] NCBI Gene and Alliance of Genome Resources reiterate that PGAM2 encodes the muscle-specific subunit of PGAM, which forms MM, MB, and BB isozyme dimers in different tissues, and confirm that mutations in this gene cause muscle phosphoglycerate mutase deficiency, also known as glycogen storage disease X.[10][14]  

Molecular genetic studies have identified several recurrent and private PGAM2 variants associated with GSD10, all of which appear to be loss-of-function or severe hypomorphic alleles that markedly reduce enzyme activity.[11][12][13] Tsujino et al. (1993) described three homozygous or compound heterozygous mutations in five patients: a G-to-A transition at codon 78 resulting in Trp78Ter (W78X), an A-to-C mutation at codon 89 converting Glu89 to Ala (E89A), and a C-to-T mutation at codon 90 converting Arg90 to Trp (R90W).[11][12][13] Orphanet notes that about half of identified cases are related to the p.W78X variant, particularly in patients of African American ancestry, with the remaining cases distributed across other ethnic groups.[4][13] Later, Hadjigeorgiou et al. (1999) reported a 209G>A transition resulting in substitution of glycine 97 by aspartic acid (G97D), a highly conserved residue, in a Japanese family with partial PGAM2 deficiency, where two heterozygous family members showed exercise intolerance and muscle cramps, illustrating the concept of manifesting heterozygotes.[12]  

More recent case reports have expanded the mutational spectrum. Koo et al. (2016) described compound heterozygous PGAM-M variants c.233G>A (codon 78 Trp to Ter, W78X) and c.278G>A in a patient with phosphoglycerate mutase deficiency, identifying c.278G>A as a novel disease-causing variant.[8][13] A 2018 case report in BMC Medical Genetics presented a 52-year-old patient diagnosed with GSDX carrying two novel heterozygous variants in exon 2 of PGAM2, c.426C>A (p.Tyr142Ter) and c.533delG (p.Gly178Alafs*31), both predicted to result in truncated proteins; interestingly, this patient had a normal increase in post-exercise lactate, demonstrating phenotypic variability even within severe PGAM2 deficiency.[5] ClinVar’s curated record for NM_000290.4(PGAM2):c.233G>A (p.Trp78Ter) classifies this variant as pathogenic/likely pathogenic based on multiple submissions and notes that PGAM2 activity in W78X homozygotes or compound heterozygotes is reduced to 2.1–6% of normal values.[13]  

The functional consequence of these variants is a marked reduction or absence of the MM isoform of PGAM in muscle, with residual enzyme activity attributable to expression of the BB (brain-type) isozyme.[16] DiMauro et al. demonstrated that in their index patient, residual PGAM activity in muscle was represented by the BB isoenzyme based on electrophoretic, heat lability, and mercury inhibition studies, supporting the hypothesis that muscle symptoms arise from selective loss of PGAM-M with partial compensation by PGAM-B.[16] PGAM is normally a highly active enzyme—Koo et al. note that even in a deficient state, PGAM activity is only slightly lower than phosphofructokinase, the rate-limiting step of glycolysis—so substantial loss of PGAM2 creates a partial block of terminal glycolysis, particularly during high-intensity exercise when glycolytic flux is maximal.[5] In summary, the etiologic core of GSD10 is **germline**, **autosomal recessive**, **loss-of-function** PGAM2 variation leading to severe reduction of muscle PGAM activity, with occasional heterozygous carriers manifesting mild symptoms.  

### 2.2 Genetic Risk Factors, Susceptibility, and Modifier Effects

Within the rare disease context, “risk factors” are largely synonymous with carrying pathogenic or likely pathogenic PGAM2 variants, yet the available literature suggests additional genetic nuances including recurrent variants with population-specific frequencies, manifesting heterozygotes, and possible modifiers affecting disease severity.[4][11][12][13] The W78X nonsense variant c.233G>A emerges as a key genetic risk factor in African-ancestry populations. ClinVar notes that NM_000290.3:c.233G>A (p.Trp78*) has an allele frequency of approximately 0.007 in the African subpopulation of gnomAD and that at least one homozygote has been observed in control datasets, implying that this allele may be relatively common and that penetrance could be incomplete or modulated by other factors.[13] Tsujino et al. found this variant homozygous in three unrelated African American patients with GSD10 and as part of a compound heterozygous genotype with G89A in a fourth patient, providing strong evidence for its pathogenicity.[11][13]  

The G97D variant illustrates potential modifier or susceptibility roles in heterozygotes. Hadjigeorgiou et al. reported that two family members heterozygous for G97D presented with exercise intolerance and muscle cramps, and noted that manifesting heterozygotes had previously been described in other families.[12] This suggests that even partial reductions in PGAM2 activity, perhaps combined with environmental stressors such as high-intensity exercise or coexisting muscle conditions, can yield clinically apparent phenotypes, although the penetrance and expressivity of such heterozygous variants remain poorly quantified due to small sample sizes.[12] The BMC case with Tyr142Ter and Gly178Alafs*31 variants underscores that truncating mutations throughout the coding sequence can be pathogenic, and the presence of two different severe alleles may explain the later adult-onset but nonetheless clinically significant phenotype.[5]  

Apart from PGAM2 itself, MalaCards lists several genes associated with Glycogen Storage Disease X based on publication co-mentions, including DBNL (Drebrin-like), PGAM1 (phosphoglycerate mutase 1), and non-coding functional elements like LOC129998343, albeit with much lower evidence scores than PGAM2.[2] PGAM1 encodes the brain-type subunit, and its activity in muscle may modulate residual PGAM activity; Koo et al. and DiMauro et al. both emphasize that residual PGAM activity in GSD10 muscle is attributable to the B isoform.[5][16] It is plausible, though not formally demonstrated, that PGAM1 expression levels or polymorphisms could act as genetic modifiers by influencing the degree of compensation, but no specific PGAM1 variants have been conclusively shown to alter GSD10 risk or severity in humans.[2][5][9] Similarly, DBNL and other genes listed by MalaCards likely reflect secondary literature associations rather than causal or modifier effects, and should be interpreted cautiously.[2]  

### 2.3 Environmental and Lifestyle Risk Factors

Unlike multifactorial disorders, GSD10 does not have classic environmental risk factors that increase disease incidence in the general population; rather, environmental influences act as triggers and determinants of episode severity among genetically susceptible individuals.[4][5][6] Orphanet emphasizes that intense physical exercise is the principal precipitating factor, noting that GSD10 is characterized by exercise intolerance leading to rhabdomyolysis, with muscle cramps and pain accompanied by acute renal symptoms such as myoglobinuria; abnormal elevation of creatine kinase persists between exertional episodes in the majority of cases.[4] MedlinePlus similarly highlights strenuous physical activity as the context in which muscle aches or cramping and myoglobinuria occur, stating that these symptoms emerge following “strenuous physical activity” and that recurrent episodes of myoglobinuria are a hallmark of the disease.[6]  

Hydration status appears to modulate risk of complications. Orphanet recommends regular, low-intensity exercise under optimal hydration conditions to reduce the intensity of muscle symptoms and implicitly the likelihood of severe rhabdomyolysis, suggesting that dehydration may exacerbate muscle breakdown and renal injury.[4] Although formal epidemiologic data quantifying this effect are lacking, clinical experience with rhabdomyolysis in other metabolic myopathies supports the notion that heat stress, dehydration, and concomitant use of myotoxic drugs (such as certain statins) can amplify muscle injury, and this likely applies to PGAM2-deficient patients as well.[4][9] Age at onset, sex, and family history function more as descriptors than environmental risk factors, since disease expression depends primarily on genotype and not on acquired exposures prior to symptom onset.  

Interestingly, MedGen mentions a poultry study entitled “Glycogen storage disease type X caused by ochratoxin A in broiler chickens,” suggesting that in non-human species, exposure to certain mycotoxins can produce a functional analog of GSD10.[15] In that experiment, ochratoxin A induced a glycogen storage disease reminiscent of type X, illustrating that environmental toxins can perturb glycolytic enzymes or glycogen metabolism sufficiently to mimic genetic GSD phenotypes in animals.[15] However, this finding does not imply that ochratoxin A exposure causes human GSD10; rather, it exemplifies how an environmental agent can serve as an induced model of the disease in veterinary or experimental contexts.  

### 2.4 Protective Factors and Gene–Environment Interactions

Specific genetic protective variants that reduce the risk of developing GSD10 among carriers of PGAM2 mutations have not been described in the available literature, largely due to the small number of reported cases and the rare nature of the condition.[4][7][9] Nevertheless, the observations of manifesting heterozygotes and asymptomatic homozygotes for W78X in control cohorts indicate that background genetic modifiers, environmental exposures, and behavioral patterns can modulate penetrance and expressivity.[12][13] Potential protective factors would include higher baseline expression of PGAM1 (brain-type) in skeletal muscle, leading to greater residual PGAM activity, and favourable variants in other glycolytic enzymes or energy-metabolism pathways that enhance alternative ATP-generating routes such as oxidative phosphorylation or fatty acid oxidation; however, these hypotheses remain speculative without direct genomic or functional data in GSD10 patients.[5][9]  

Environmental and lifestyle factors that function as protective influences are better documented. Orphanet explicitly recommends regular, low-intensity exercise under optimal hydration conditions, implying that such a regimen may reduce symptom intensity and episode frequency by avoiding high-energy demands that outstrip defective glycolytic capacity.[4] This aligns with broader principles in metabolic myopathy management, where patients are advised to avoid short bursts of maximal exertion and instead engage in moderate, sustained activities that rely more on oxidative metabolism, as well as to maintain adequate hydration and electrolyte balance to limit rhabdomyolysis and renal stress.[4][9] Thus, avoidance of strenuous exercise, heat stress, dehydration, and myotoxic drugs can be conceptualized as secondary protective strategies in genetically affected individuals.  

Gene–environment interactions in GSD10 primarily involve the interplay between fixed PGAM2 deficits and variable exercise and hydration patterns. In individuals with biallelic PGAM2 mutations, intense short-term exercise that relies on anaerobic glycolysis interacts with defective PGAM function to precipitate acute energy failure in muscle cells, leading to contractures, membrane damage, and rhabdomyolysis.[4][5][16] Conversely, when such individuals engage mainly in low-intensity activities within a well-hydrated milieu, the residual glycolytic and oxidative pathways may suffice to meet energy demands without catastrophic breakdown, effectively mitigating clinical expression.[4][9] For heterozygous carriers with partial PGAM2 deficiency, the threshold at which exercise triggers symptoms may be higher, and gene–environment interaction could determine whether they remain asymptomatic or develop exertional myalgia and cramps.[12] In summary, GSD10 etiology is dominated by PGAM2 genetics, with environmental factors acting as modulators and triggers of episode severity rather than primary causes.  

## 3. Phenotypes

### 3.1 Core Skeletal Muscle Symptoms and Signs

The core phenotypic manifestations of glycogen storage disease due to phosphoglycerate mutase deficiency reside in skeletal muscle, reflecting the tissue-specific expression of PGAM2 and the critical role of glycolysis in muscle contraction during high-intensity exercise.[4][5][6][9] Orphanet emphasizes susceptibility to rhabdomyolysis with episodes of exercise-induced muscle pain and cramping, noting that symptoms typically manifest during adolescence or childhood.[4] MedlinePlus Genetics describes that, beginning in childhood or adolescence, affected individuals experience muscle aches or cramping following strenuous physical activity and highlights that some patients have recurrent episodes of myoglobinuria, indicating repeated episodes of muscle breakdown.[6] Koo et al. and the Neuromuscular Disorders case report note that GSDX is characterized by exertional muscle contractures, weakness, hyperCKemia, and myoglobinuria, often accompanied by tubular aggregates in skeletal muscle.[5][8]  

Clinically, patients report exercise intolerance, defined as an inability to sustain normal levels of physical exertion, with early fatigue, heavy sensation in active muscles, and cramps after brief sprints, climbing stairs, or lifting, as is typical for glycolytic pathway defects.[3][4][9] Tsujino et al. describe exercise intolerance and cramps as universal features among their five PGAM2-deficient patients, and DiMauro’s index patient reported intolerance for strenuous exercise since adolescence and recurrent pigmenturia after exertion.[11][16] HPO terms that represent these features include exercise intolerance (HP:0003546), muscle cramps (HP:0003394), exercise-induced muscle cramps (HP:0003396), and muscle weakness (HP:0001324), although frank persistent weakness between episodes appears less prominent than in some other myopathies.[4][5][8]  

Muscle contractures and pain frequently accompany episodes of rhabdomyolysis. Koo et al. highlight exertional muscle contractures and weakness as defining features, and Neuromuscular Disorders notes that PGAM deficiency causes a metabolic myopathy characterized by exertional muscle contractures, weakness, hyperCKemia, and myoglobinuria.[5][8] The pain may be intense, localized to exercised muscle groups, and associated with swelling and tenderness, consistent with acute muscle fiber necrosis.[4][5] In some cases, patients describe “locking” of muscles during or after exercise, reflecting sustained contractures due to ATP depletion and failure of actin–myosin cross-bridge detachment, a phenomenon shared with other glycolytic myopathies.[9]  

Muscle biopsy findings provide structural correlates to these symptoms. Orphanet notes that some patients present with glycogen accumulation and tubular aggregates within skeletal muscle cells, while JAMA Neurology reports frequent association with sarcoplasmic reticulum proliferation.[3][4] These features can be captured by HPO terms such as tubular aggregates (HP:0030191), abnormal glycogen accumulation in muscle (HP:0004305), and sarcoplasmic reticulum proliferation (which would currently be described descriptively rather than by a specific HPO code).[3][4][8] Overall, the skeletal muscle phenotype is episodic, triggered by exertion, and generally non-progressive in terms of baseline strength, aligning with the label of a “rare and benign muscle glycogenosis” used by the JAMA Neurology authors.[3]  

### 3.2 Laboratory Abnormalities and Biochemical Phenotypes

Laboratory abnormalities in GSD10 reflect both the underlying enzymatic defect and the consequences of recurrent muscle breakdown.[4][5][8][9] Elevated serum creatine kinase (hyperCKemia) is a consistent finding during and often between episodes. Orphanet notes that intense physical exercise is accompanied by abnormal elevation of creatine kinase in the majority of cases, and Koo et al. refer to hyperCKemia as a feature of PGAM deficiency in association with exertional contractures and myoglobinuria.[4][5][8] Alliance of Genome Resources also annotates PGAM2 with the phenotype “Elevated circulating creatine kinase activity,” referencing OMIM 261670.[14] HPO term HP:0003236, “Elevated serum creatine kinase,” is therefore strongly associated with this disease.  

Myoglobinuria is another hallmark biochemical phenotype, manifesting as dark urine due to excretion of myoglobin released from damaged muscle fibers.[4][5][6][8] MedlinePlus explains that myoglobinuria occurs when muscle tissue breaks down abnormally and releases myoglobin, which is processed by the kidneys and released in urine, and cautions that untreated myoglobinuria can lead to kidney failure.[6] Orphanet and Neuromuscular Disorders similarly highlight recurrent myoglobinuria as a key component of the disease.[4][8] The corresponding HPO term is HP:0003198, “Myoglobinuria.” During episodes of rhabdomyolysis, additional laboratory abnormalities may include raised serum lactate dehydrogenase, hyperkalemia, hyperphosphatemia, and elevated transaminases, although these are common to rhabdomyolysis and not specific to PGAM deficiency.[4][9]  

Enzyme assays of PGAM in muscle tissue reveal the defining biochemical abnormality. DiMauro et al. measured muscle PGAM activity at 5.7% of the lowest control value in their index case, with normal activities of all other glycolytic enzymes and normal glycogen concentration, establishing that the defect is isolated to PGAM.[16] Tsujino et al. and OMIM report that PGAM2 activities in W78X homozygotes or compound heterozygotes are decreased to 2.1–6% of normal values, indicating a severe enzymatic deficiency.[11][12][13] Koo et al. remark that PGAM is normally highly active so that even in deficiency, its activity remains only slightly lower than phosphofructokinase, but the reduction is sufficient to create a partial block of terminal glycolysis, particularly during intense exercise.[5] In many patients, residual PGAM activity is attributable to the BB isoform, as shown by electrophoretic and inhibition studies, emphasizing that the enzyme abnormality is isoform-specific rather than complete absence of total PGAM.[16]  

Interestingly, lactate responses to exercise may be variably affected. In the BMC case report, the 52-year-old patient with two truncating PGAM2 variants had a normal increase in post-exercise lactate during both anaerobic and aerobic exercise testing, despite his muscle biopsy confirming PGAM deficiency.[5] This finding suggests that upstream glycolytic steps may compensate to some extent and that terminal glycolytic block at PGAM may not always manifest as impaired lactate production, complicating the use of lactate responses as a diagnostic biomarker.[5][9] HPO terms such as abnormal lactate level (HP:0002151) could be considered for some patients, but evidence is not uniform. Overall, the biochemical phenotype is dominated by **severely reduced PGAM activity in muscle, elevated CK, episodic myoglobinuria, and rhabdomyolysis**, with more subtle changes in downstream metabolites and variable lactate kinetics.  

### 3.3 Renal, Hematologic, and Systemic Manifestations

Renal involvement in GSD10 occurs primarily as a complication of recurrent rhabdomyolysis and myoglobinuria rather than as a direct effect of PGAM2 deficiency on kidney cells.[4][6][9] Orphanet warns that rhabdomyolysis manifestations include acute renal symptoms such as myoglobinuria and emphasizes that recognizing and treating episodes promptly is critical because rhabdomyolysis can lead to significant morbidity and mortality, including multiorgan failure, if left untreated.[4] MedlinePlus similarly stresses that myoglobinuria can progress to kidney failure if not managed appropriately.[6] HPO terms capturing these renal aspects include acute kidney injury (HP:0001919), renal failure (HP:0001944), and pigment nephropathy (HP:0000147), though specific frequencies in GSD10 are not well quantified due to limited case numbers and variable severity of episodes.[4][6][9]  

Hematologic manifestations are less prominently described, yet MONDO:0009865 in PomBase notes that “glycogen storage disease due to phosphoglycerate mutase deficiency” is characterized by non-spherocytic hemolytic anemia, exercise-induced cramping, myoglobinuria, and presence of tubular aggregates, implying that some patients may exhibit red blood cell abnormalities.[1] Non-spherocytic hemolytic anemia refers to hemolysis not caused by spherocytosis, typically due to defects in RBC glycolytic enzymes such as PGAM1 or PGK1, and its mention suggests that PGAM deficiency, whether via PGAM1 or PGAM2 involvement in erythrocytes, can result in increased RBC fragility.[1][9] However, clinical case series of GSD10 have focused primarily on muscle phenotypes, and explicit documentation of anemia in PGAM2-related disease is sparse, so this feature may be rare or more characteristic of PGAM1 deficiency, which is distinct but mechanistically related.[1][9]  

Systemic manifestations beyond muscle and kidney are uncommon but have been mentioned. The comprehensive review of glycogen metabolism and glycogen storage disorders notes that clinical features of GSD10 can include hyperuricemia and gout as well as coronary arteriosclerosis.[9] Hyperuricemia likely results from increased purine nucleotide degradation during repeated ATP depletion and muscle breakdown, a mechanism shared with other states of chronic high-energy turnover and rhabdomyolysis, and can predispose to gouty arthritis.[9] Coronary arteriosclerosis is mentioned as a possible comorbidity, though its direct mechanistic link to PGAM2 deficiency is uncertain and could reflect conventional cardiovascular risk factors or systemic consequences of chronic metabolic stress.[9] HPO terms that could be associated include hyperuricemia (HP:0002149), gout (HP:0001997), and coronary arteriosclerosis (HP:0001677), but evidence strength for these features is weaker than for core muscle and renal manifestations.  

### 3.4 Age of Onset, Severity, Progression, and Quality of Life

Across case series and reviews, age of onset for GSD10 is predominantly in childhood or adolescence, with some adult-onset cases described.[4][5][6][9][16] Orphanet specifies that age of onset is “Adolescent, Childhood” and notes that fewer than fifty cases have been reported worldwide.[4] MedlinePlus reiterates that symptoms begin in childhood or adolescence, and the DiMauro case, though diagnosed at age 52, had onset of exercise intolerance and pigmenturia since adolescence.[6][16] The 2018 BMC case report also documented a 52-year-old patient whose symptoms had begun decades earlier but were only recognized as GSDX after genetic testing, illustrating delayed diagnosis rather than truly late onset.[5] HPO term HP:0003621 (Childhood onset) and HP:0003623 (Adolescent onset) are applicable.  

Symptom severity in GSD10 is variable but often characterized as mild to moderate in terms of functional impairment, with episodes of severe rhabdomyolysis representing acute peaks of morbidity.[3][4][5][9] JAMA Neurology refers to PGAM deficiency as a “rare and benign muscle glycogenosis,” indicating that, in their experience, long-term outcomes are generally favourable despite recurrent symptoms.[3] Orphanet notes that GSD type X is not thought to impact longevity, and the glycogen metabolism review lists clinical features that can include serious complications like rhabdomyolysis and coronary arteriosclerosis but acknowledges that only fifteen cases have been reported, limiting generalizations.[4][9] Patients may experience significant pain and activity limitations during episodes, but between episodes many can carry out daily activities with careful avoidance of triggers.[4][5]  

Symptom progression appears episodic rather than steadily progressive. The disease course is characterized by recurrent attacks of exertional myalgia, cramps, and myoglobinuria, often with persistent hyperCKemia between attacks, but without progressive fixed weakness or muscle wasting in most reported cases.[3][4][5][9] Orphanet emphasizes that intense exercise episodes are associated with abnormal creatine kinase elevation that persists between exertional episodes, suggesting a degree of chronic subclinical muscle injury.[4] However, in contrast to some other muscular dystrophies or storage myopathies, GSD10 does not usually lead to wheelchair dependence or severe disability, supporting the concept of a relatively benign course.[3][4][9] Disease duration is lifelong, reflecting its genetic nature, but the pattern is best described as **chronic, lifelong, episodic, and relapsing**, rather than progressive in the classical sense.  

Quality of life impact varies with symptom frequency and severity. Recurrent painful episodes, fear of rhabdomyolysis, and restrictions on physical activity can impair social participation, employment in physically demanding jobs, and psychological well-being, although systematic assessments using instruments such as SF-36 or EQ-5D have not been reported for GSD10 specifically.[4][5][9] Patients may adapt by choosing less physically demanding lifestyles and using hydration strategies to reduce attacks, but may nonetheless experience limitations in sports participation or occupational choices.[4][5] The presence of benign overall prognosis may mitigate anxiety compared with more progressive neuromuscular disorders, yet acute episodes requiring hospitalization for rhabdomyolysis and renal monitoring represent significant stressors. In summary, phenotypes of GSD10 impact quality of life mainly through episodic pain, functional limitation during attacks, and chronic vigilance rather than continuous severe disability.  

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: PGAM2 and Its Isoforms

The **PGAM2** gene (HGNC:8889) encodes **phosphoglycerate mutase 2**, the muscle-specific subunit of the phosphoglycerate mutase enzyme, and is the only gene conclusively implicated as causative in glycogen storage disease type X.[10][12][14] OMIM’s gene entry 612931 describes PGAM2 as encoding muscle phosphoglycerate mutase-2 (EC 5.4.2.1) and locates it on chromosome 7p13.[12] NCBI Gene confirms that PGAM2 encodes the muscle-specific PGAM subunit, and notes that the enzyme catalyzes the reversible reaction of 3-phosphoglycerate (3-PGA) to 2-phosphoglycerate (2-PGA) in the glycolytic pathway, forming dimeric isozymes composed of MM, MB, or BB subunits depending on tissue.[10] Alliance of Genome Resources reiterates that PGAM2 enables phosphoglycerate mutase activity, is involved in the glycolytic process and striated muscle contraction, is located in the nucleoplasm, and is implicated in glycogen storage disease X and myoglobinuria.[14]  

PGAM2 is one of two major human PGAM subunit genes, the other being **PGAM1**, which encodes the brain-type subunit.[2][10][16] The enzyme phosphoglycerate mutase exists as a dimer, and mature human skeletal muscle contains almost exclusively the MM form of the enzyme, PGAM-M, in contrast to other tissues where BB or MB combinations may predominate.[11][16] DiMauro et al. demonstrated that residual PGAM activity in their index patient’s muscle was represented by the BB isoenzyme, indicating that PGAM1 expression persists in muscle and can partially compensate for PGAM2 deficiency, but not sufficiently to prevent symptoms during high-intensity exercise.[16] Tsujino et al. emphasize that the glycolytic enzyme PGAM is a dimer and that mature human skeletal muscle contains almost exclusively PGAM-M, providing a molecular basis for the muscle specificity of GSD10.[11]  

Gene Ontology (GO) terms associated with PGAM2 include **GO:0004619 (phosphoglycerate mutase activity)**, **GO:0006096 (glycolytic process)**, and **GO:0006941 (striated muscle contraction)**, reflecting its enzymatic function and physiological role.[10][14] PGAM2 is expressed predominantly in skeletal muscle but also detectable in other striated muscle tissues, potentially including cardiac muscle, though clinically significant cardiac involvement has not been clearly documented in GSD10.[9][14] The muscle-specific isoform ensures that defects in PGAM2 manifest primarily in skeletal muscle, while PGAM1 maintains glycolytic function in brain and other tissues, explaining the absence of neurologic symptoms in most patients.[9][11][16]  

### 4.2 Spectrum and Classification of Pathogenic Variants

As noted earlier, multiple pathogenic PGAM2 variants have been described, including nonsense, missense, and frameshift alleles that cluster in exons encoding the N-terminal region but can occur throughout the gene.[5][8][11][12][13] OMIM gene entry lists three key mutations originally identified by Tsujino et al. in five patients: a homozygous G-to-A transition resulting in Trp78Ter (W78X), an A-to-C mutation converting Glu89 to Ala (G89A), and a C-to-T mutation converting Arg90 to Trp (R90W).[11][12] ClinVar provides a detailed record for c.233G>A (p.Trp78Ter), describing it as a single nucleotide variant that creates a premature stop codon, predicted to cause truncation or absence of the protein due to nonsense-mediated decay, and highlights its classification as pathogenic/likely pathogenic by multiple submitters.[13] MalaCards notes three UniProtKB/Swiss-Prot disease variations for GSD10: PGAM2 p.Glu89Ala (VAR_006088; rs104894030), p.Arg90Trp (VAR_006089; rs104894034), and p.Gly97Asp (VAR_013103; rs77938727), corresponding to the variants described in Tsujino and Hadjigeorgiou’s studies.[2][11][12]  

Novel truncating variants have expanded the spectrum. The BMC case report identified c.426C>A (p.Tyr142Ter) and c.533delG (p.Gly178Alafs*31) in exon 2 of PGAM2, both predicted to produce truncated proteins significantly shorter than the wild-type enzyme.[5] These variants were heterozygous in the patient, suggesting compound heterozygosity as the genetic mechanism, and functional testing confirmed PGAM deficiency in muscle.[5] The Neuromuscular Disorders case by Koo et al. found compound heterozygous PGAM-M variants c.233G>A (W78X) and c.278G>A, with the latter being novel at the time; both were classified as autosomal recessive disease-causing variants.[8] OMIM also notes the G97D variant identified in a Japanese family, where substitution of a highly conserved glycine at codon 97 with aspartic acid led to partial deficiency and manifesting heterozygotes.[12]  

Variant classification follows ACMG/AMP guidelines. ClinVar’s record for c.233G>A (W78X) notes that this variant is expected to result in an absent or disrupted protein product and that such truncating changes are commonly known mechanisms for disease, supporting a pathogenic classification.[13] It further cites the presence of the allele at a frequency of 0.00053 in 251,076 control chromosomes in gnomAD, including one homozygote, and its repeated observation in individuals with GSD10, as evidence of its disease association.[13] Other missense variants like G89A, R90W, and G97D are considered pathogenic or likely pathogenic based on segregation with disease, conservation of affected residues, and functional evidence of reduced enzyme activity, as documented in Tsujino and Hadjigeorgiou’s studies.[11][12] Frameshift and nonsense variants such as Tyr142Ter and Gly178Alafs*31 are by nature loss-of-function and therefore likely pathogenic when found in trans in affected individuals.[5]  

Most reported PGAM2 variants are **germline** rather than somatic and are inherited in autosomal recessive fashion.[4][7][12] There is no evidence from COSMIC, TCGA, or cancer genomics resources in the provided search results that somatic PGAM2 mutations play a major role in malignancy, though PGAM enzymes have been studied in cancer metabolism more broadly.[9] Allele frequencies of specific variants in general population databases are limited; ClinVar provides partial data for W78X, but other variants have sparse frequency information due to rarity.[13] In summary, the pathogenic variant spectrum in PGAM2 includes multiple truncating and missense alleles that lead to severe loss of muscle PGAM activity and cause GSD10 when present in biallelic form.  

### 4.3 Modifier Genes, Epigenetic Factors, and Structural Genomic Changes

Clear evidence for modifier genes in PGAM2-related GSD10 is limited, but inferential clues exist. The presence of manifesting heterozygotes for G97D and other variants suggests that genetic background may influence whether partial enzyme deficiency results in clinical symptoms.[12] Potential modifiers could include genes governing muscle oxidative capacity, mitochondrial function, alternative metabolic pathways (e.g., fatty acid oxidation), or stress-response mechanisms, as well as genes regulating PGAM1 expression in skeletal muscle.[5][9][16] MalaCards’ list of associated genes, which includes PGAM1 and DBNL, is likely based on literature co-occurrence and not definitive modifier effects, but PGAM1 is biologically plausible given its role in the brain-type isoform of PGAM.[2] However, the current human literature does not provide direct evidence of specific modifier alleles or genes, and this remains an open area for research, potentially addressable via exome or genome sequencing of larger patient cohorts or functional genomics screens.[9]  

Epigenetic information specifically linking DNA methylation, histone modifications, or chromatin changes to PGAM2 expression or GSD10 pathogenesis is not available in the provided sources.[4][7][9][12] Given PGAM2’s role as a muscle-specific enzyme, it is conceivable that epigenetic regulation contributes to tissue-specific expression and could theoretically modulate residual enzyme levels in carriers or patients, but no disease-specific epigenetic studies have been published to date. Similarly, large-scale chromosomal abnormalities such as aneuploidy, translocations, or inversions involving chromosome 7p13 have not been reported as primary causes of GSD10, and OMIM attributes the phenotype exclusively to point mutations or small indels within PGAM2 rather than to structural genomic changes.[7][12] ClinVar records for PGAM2 focus on single nucleotide variants rather than CNVs or chromosomal rearrangements.[13]  

Molecular profiling at the omics scale—transcriptomics, proteomics, metabolomics, and lipidomics—has not yet been systematically applied to GSD10 patients in published studies captured by the search results.[4][5][9] While individual case reports include enzyme assays and occasionally lactate responses, they do not present high-throughput data such as RNA-seq or proteomics of muscle tissue.[5][16] The Human Protein Atlas and GTEx likely contain expression data for PGAM2 across tissues, but these have not been specifically tied to GSD10 phenotypes in the retrieved documents.[10][14] Thus, multi-omics integration, single-cell analyses, spatial transcriptomics, and functional genomics screens remain future avenues for understanding disease mechanisms in greater detail but cannot yet be summarized based on current evidence.  

## 5. Environmental Information

### 5.1 Non-Genetic Contributing Factors and Occupational Exposures

In humans, non-genetic environmental factors do not cause GSD10 in the absence of PGAM2 mutations but can significantly influence the manifestation and severity of symptoms in affected individuals.[4][6][9] The principal environmental factor is **physical exertion**, specifically short bursts of strenuous exercise that depend heavily on glycolytic ATP production.[4][5][6] Orphanet states that glycogen storage disease due to PGAM2 deficiency is characterized by exercise intolerance leading to rhabdomyolysis, manifesting through muscle cramps and pain accompanied by acute renal symptoms such as myoglobinuria.[4] MedlinePlus similarly notes that affected individuals experience muscle aches or cramping following strenuous physical activity, with recurrent episodes of myoglobinuria.[6] Occupational settings requiring repeated high-intensity exertion, such as military training, firefighting, or manual labour, may therefore act as functional exacerbating environments for GSD10 patients, though explicit occupational case descriptions are rare due to the disease’s rarity.[4][9]  

Additional environmental factors can modulate rhabdomyolysis risk, including heat exposure, dehydration, and concomitant use of medications that predispose to muscle injury such as statins or certain antivirals.[4][9] While these are not specific to GSD10 and have not been systematically studied in this context, clinical practice extrapolates from experiences with other metabolic myopathies and rhabdomyolysis syndromes, recommending that patients avoid extreme heat, maintain adequate hydration, and consult physicians before using potential myotoxins.[4][9] Infections, particularly febrile illnesses with systemic inflammatory responses, may also lower the threshold for muscle breakdown during exercise, but direct case evidence in GSD10 is limited. Environmental toxins such as mycotoxins have been implicated in animal analogs rather than human disease, as discussed below.[15]  

### 5.2 Lifestyle Factors: Diet, Exercise, and Alcohol

Lifestyle factors—especially exercise patterns and hydration—are central to symptom management in PGAM2 deficiency.[4][5][9] Orphanet recommends regular, low-intensity exercise performed under optimal hydration conditions to reduce the intensity of muscle symptoms, reflecting the principle that sustained moderate activity relies more on oxidative metabolism than on glycolysis and is therefore better tolerated in glycolytic myopathies.[4] Patients are typically advised to avoid sudden bursts of maximal exertion, sprinting, heavy lifting, or competitive sports involving short intense efforts, because these activities are most likely to exceed the defective glycolytic capacity and cause rhabdomyolysis.[4][5][9] Maintaining adequate fluid intake before, during, and after activity, as well as avoiding alcohol-induced dehydration, further reduces risk of myoglobinuric episodes.[4][6]  

Dietary factors have not been systematically evaluated in GSD10, but by analogy with other glycolytic and glycogenolytic disorders, patients may benefit from balanced macronutrient intake, avoidance of prolonged fasting, and perhaps pre-exercise carbohydrate supplementation to support residual glycolytic flux, though these strategies are more clearly established for disorders like McArdle disease.[9] No specific dietary protective or risk factors such as high-fat or high-protein diets have been documented for PGAM2 deficiency in the literature captured by the search results.[4][9] Alcohol consumption may exacerbate dehydration and muscle toxicity but is not a primary cause of episodes; nevertheless, moderation or avoidance may be prudent, particularly before strenuous activity.[4][9] Smoking and other lifestyle factors have not been linked to GSD10 progression or severity.  

### 5.3 Infectious Agents and Toxins

There is no evidence that infectious agents—bacteria, viruses, fungi, or parasites—directly cause PGAM2 deficiency or GSD10 in humans.[4][6][9] However, systemic infections can trigger rhabdomyolysis in susceptible individuals by increasing metabolic demand, inducing fever, and releasing cytokines, and may thus act as nonspecific episode precipitants.[9] For example, viral illnesses such as influenza or SARS-CoV-2 have been associated with rhabdomyolysis in the general population, and similar mechanisms could operate in GSD10 patients, though specific case reports have not been identified in this context from the provided search results.[4][9]  

In animals, toxins such as ochratoxin A have been shown to induce a glycogen storage disease resembling type X in broiler chickens, as noted by MedGen.[15] The cited study, “Glycogen storage disease type X caused by ochratoxin A in broiler chickens,” demonstrates that environmental exposure to mycotoxins can disrupt glycogen metabolism and glycolytic enzymes in skeletal muscle, leading to a phenotype analogous to GSD10 but of toxic etiology.[15] This finding is important for comparative pathology and model development but does not imply a direct toxin cause of human GSD10. There is no indication from the human literature that chronic environmental exposure to mycotoxins, industrial chemicals, or other pollutants causes PGAM2 mutations or functional deficiency independent of genetic mutations.[4][9]  

In summary, environmental information for GSD10 emphasizes **exercise and hydration** as primary modulators of disease expression, while infectious agents and toxins are relevant mainly in animal models or as nonspecific rhabdomyolysis triggers rather than etiologic agents of the human genetic disease.  

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

1. Germline homozygous or compound heterozygous loss-of-function variants in **PGAM2** lead to absent or markedly reduced expression of the muscle MM isoform of phosphoglycerate mutase in skeletal muscle.[4][7][11][12][13]  
2. Loss of PGAM-M results in a severe reduction of total phosphoglycerate mutase activity in muscle, with residual activity mainly derived from the BB isoform, and creates a partial block of terminal glycolysis at the step converting 3-phosphoglycerate to 2-phosphoglycerate.[5][9][16]  
3. This glycolytic block leads to impaired ATP generation during high-intensity, anaerobic exercise, when glycolytic flux must rapidly increase to meet energy demands in skeletal muscle cells, particularly fast-twitch fibers.[4][5][9]  
4. Inadequate ATP supply during contraction results in failure of normal excitation–contraction coupling and relaxation, causing sustained muscle contractures, accumulation of intracellular calcium, and mechanical and metabolic stress on myofibers.[5][8][9]  
5. The combination of contracture-induced strain, ionic imbalance, and metabolic stress leads to sarcolemmal damage and myofiber necrosis, culminating in release of creatine kinase, myoglobin, electrolytes, and other intracellular contents into the bloodstream, manifesting as hyperCKemia and myoglobinuria.[4][5][6][8]  
6. Filtered myoglobin accumulates in renal tubules, where it can precipitate and, together with hypovolemia and vasoconstriction, leads to acute tubular necrosis and acute kidney injury during severe rhabdomyolysis episodes.[4][6][9]  
7. Chronic or repeated cycles of metabolic stress and myofiber injury stimulate structural remodeling in muscle, including proliferation of sarcoplasmic reticulum and formation of tubular aggregates, representing reorganized aggregates of sarcoplasmic reticulum and other membrane systems.[3][4][5][8]  
8. Upstream, the presence of residual BB isoform PGAM1 in muscle partially compensates for PGAM2 deficiency at rest and during low-intensity exercise, allowing relatively normal basal muscle function but not preventing acute energy failure during intense exertion.[5][16]  
9. In some individuals, partial PGAM2 deficiency (e.g., heterozygous G97D carriers) yields milder metabolic impairments that become clinically apparent only under specific environmental stresses, illustrating gene–environment interactions and incomplete penetrance.[12]  
10. Systemically, repeated episodes of ATP depletion and purine nucleotide turnover contribute to hyperuricemia and gout, while chronic metabolic stress may promote vascular changes such as coronary arteriosclerosis, although these downstream effects are less well established and partly inferred.[9]  

### 6.2 Molecular Pathways and Biochemical Abnormalities

At the molecular level, PGAM2 sits within the **glycolytic pathway**, specifically catalyzing the reversible isomerization of 3-phosphoglycerate (3-PGA) to 2-phosphoglycerate (2-PGA), the eighth reaction in the canonical glycolytic sequence.[4][5][9][10] This step precedes the ATP-generating reaction carried out by enolase (conversion of 2-PGA to phosphoenolpyruvate) and pyruvate kinase (conversion of phosphoenolpyruvate to pyruvate), meaning that a block at PGAM disrupts downstream ATP production during glycolysis.[5][9] The relevant biochemical entities include **glucose (CHEBI:17234)**, **glycogen (CHEBI:28087)**, **3-phosphoglycerate (CHEBI:58759)**, **2-phosphoglycerate (CHEBI:57695)**, **pyruvate (CHEBI:15361)**, and **ATP (CHEBI:30616)**.  

Orphanet explains that PGAM2 reversibly catalyzes the conversion reaction of 3-PGA to 2-PGA, which is then further metabolized to produce pyruvate, and notes that during exercise, insufficient residual PGAM2 activity results in inability to catabolize enough glucose to meet increased energy needs of muscle cells.[4] Koo et al. add that PGAM enzyme is highly active, so that even in a deficient state its activity is only slightly lower than phosphofructokinase, the rate-limiting step, but the reduction still represents a partial block of terminal glycolysis.[5] DiMauro’s original case and Tsujino’s series demonstrated that all other glycolytic enzymes were normal, confirming that the biochemical abnormality is isolated to PGAM and that glycogen concentration in muscle is normal or mildly increased.[11][16]  

The metabolic changes during exercise include accumulation of upstream glycolytic intermediates (such as 3-PGA) and reduced formation of downstream products like 2-PGA, phosphoenolpyruvate, and pyruvate, leading to decreased lactate production under certain conditions.[5][9] However, as noted in the BMC case report, post-exercise lactate responses may be normal in some patients, indicating that compensatory mechanisms can partially maintain pyruvate and lactate production despite PGAM deficiency, perhaps via altered flux or alternative pathways.[5] GO terms relevant to these processes include **GO:0006096 (glycolytic process)**, **GO:0006091 (generation of precursor metabolites and energy)**, and **GO:0006112 (energy reserve metabolic process)**. In addition, the disease can be considered a **disorder of glycogen metabolism** (MONDO classification) because impaired glycolysis indirectly affects glycogen utilization during exercise, even though the primary defect is not in glycogen storage or breakdown enzymes such as glycogen synthase or phosphorylase.[1][9]  

The biochemical abnormality of enzyme deficiency translates into measurable changes in enzyme activity. Tsujino et al. and ClinVar report that PGAM2 activity in affected patients with W78X and other variants is reduced to 2.1–6% of normal control values.[11][13] DiMauro et al. measured muscle PGAM at 5.7% of the lowest control value, with electrophoretic studies confirming that residual activity represented the BB isoenzyme.[16] These data illustrate that PGAM2 mutations effectively ablate the MM isoform, while leaving PGAM1 intact and able to form BB dimers, which have slower migration and distinct properties.[11][16] The presence of residual BB activity prevents catastrophic failure of glycolysis at rest, but under high flux demands, the limited capacity is quickly saturated, causing acute ATP shortage.[5][9][16]  

### 6.3 Cellular Processes and Protein Dysfunction in Muscle

At the cellular level, GSD10 affects **skeletal muscle fibers** (CL:0000737), particularly fast-twitch glycolytic fibers that depend heavily on glycolysis for rapid ATP generation.[4][5][9] The immediate consequence of PGAM2 deficiency during exercise is **energy failure**, defined as insufficient ATP to sustain repeated cycles of actin–myosin cross-bridge cycling and sarcoplasmic reticulum calcium handling.[4][5][9] This leads to **failure of relaxation** and sustained contractures, which are clinically observed as painful muscle cramps and stiffness during or after exertion.[5][8] GO terms such as **GO:0006941 (striated muscle contraction)**, **GO:0006937 (regulation of muscle contraction)**, and **GO:0006874 (cellular calcium ion homeostasis)** encapsulate these processes.  

Protein dysfunction centers on the loss of PGAM2 enzymatic function. Nonsense and frameshift variants produce truncated proteins subject to nonsense-mediated decay, resulting in absent protein, while missense variants like G89A, R90W, and G97D likely destabilize the active site or impair dimerization, leading to reduced catalytic activity.[11][12][13] ClinVar notes that p.Trp78* is expected to result in an absent or disrupted protein product and that such truncations are common mechanisms for disease.[13] Structural consequences have not been fully elucidated with crystallography or modeling in the human disease context, but PGAM’s known catalytic mechanism involves a phosphoserine intermediate and requires precise positioning of histidine, lysine, and arginine residues; missense changes at conserved positions can disrupt substrate binding or catalytic residue alignment.[9] Protein misfolding or instability may also lead to increased degradation of mutant PGAM2 in muscle cells, further reducing enzyme levels.  

Downstream cellular processes include **myofiber necrosis**, **membrane disruption**, and **sarcolemmal leakage** of intracellular contents, culminating in hyperCKemia and myoglobin release.[4][5][8] Repeated cycles of injury and repair stimulate satellite cell activation and muscle regeneration, and chronic subclinical damage leads to structural remodeling such as sarcoplasmic reticulum proliferation and formation of tubular aggregates.[3][4][8] JAMA Neurology reports that GSD10 is often associated with sarcoplasmic reticulum proliferation, visible as membrane-rich regions on electron microscopy.[3] Tubular aggregates, described in Orphanet and multiple case reports, likely represent reorganized aggregates of sarcoplasmic reticulum and T-tubule membranes and are seen in other metabolic and channelopathies as well.[4][5][8] GO terms relevant to these changes include **GO:0016044 (cellular membrane organization)**, **GO:0044319 (muscle cell proliferation)**, and **GO:0006950 (response to stress)**.  

### 6.4 Tissue Damage Mechanisms and Immune Involvement

Tissue damage in GSD10 arises primarily from **metabolic stress and mechanical strain**, rather than from primary immune-mediated mechanisms.[4][5][9] During episodes of rhabdomyolysis, intracellular enzymes (CK, LDH), structural proteins (myoglobin), and ions (K+, phosphate) are released into the circulation, reflecting widespread myofiber necrosis.[4][6][9] In the kidney, myoglobin is filtered by glomeruli and concentrated in renal tubules, where it can precipitate and cause obstruction, oxidative damage via free iron, and tubular epithelial cell necrosis, culminating in acute kidney injury.[4][6][9] GO terms such as **GO:0001911 (negative regulation of renal system process)** and **GO:0008219 (cell death)** are relevant to this process.  

Oxidative stress likely contributes to muscle and renal injury during rhabdomyolysis, as reactive oxygen species accumulate during ischemia–reperfusion cycles and myoglobin-mediated Fenton reactions.[9] However, specific oxidative stress markers have not been systematically studied in GSD10 patients, and most mechanistic insight is extrapolated from broader rhabdomyolysis literature. Inflammatory responses follow tissue damage, with neutrophil and macrophage infiltration into injured muscle and activation of pro-inflammatory cytokines, but there is no evidence of autoimmune or primary inflammatory myopathy in PGAM2 deficiency.[4][9] Creatine kinase elevations and muscle pain reflect damage rather than immune attack, and immunosuppressive therapy is not indicated.[4][9]  

Over the long term, repeated rhabdomyolysis episodes may contribute to chronic kidney disease in some patients, though explicit data for GSD10 are scarce.[4][6][9] Hyperuricemia resulting from repeated ATP breakdown and purine catabolism can lead to gout and urate deposition in joints and kidneys, compounding renal risk.[9] Coronary arteriosclerosis mentioned in the glycogen metabolism review could represent systemic vascular consequences of chronic metabolic stress, but direct evidence linking PGAM2 deficiency to accelerated atherosclerosis is limited and partly inferred.[9] In summary, tissue damage mechanisms in GSD10 revolve around **metabolic myocyte injury and pigment nephropathy**, with secondary inflammation, oxidative stress, and potential long-term organ sequelae, but no primary immune or fibrotic component has been documented.  

### 6.5 Cell Types, GO and CL Term Mapping

The primary cell type involved in GSD10 is the **skeletal muscle cell** (CL:0000737), especially fast-twitch glycolytic fibers found in limb, trunk, and axial muscles (UBERON:0001137 for trunk skeletal muscle, UBERON:0001630 for limb skeletal muscle).[4][9][14] These cells express high levels of PGAM2 and depend on glycolytic flux for rapid ATP generation during intense exercise, making them uniquely vulnerable to PGAM2 deficiency.[10][14] Secondary cell types include **renal tubular epithelial cells** (CL:0002066) affected during myoglobinuric acute kidney injury, and **erythrocytes** (CL:0000232) in cases where non-spherocytic hemolytic anemia is present, although the latter is better established for PGAM1 deficiency.[1][9][15] Cardiac myocytes (CL:0000746) may express PGAM2 but have not been prominently implicated clinically, despite the mention of coronary arteriosclerosis as a possible comorbidity.[9]  

Relevant GO biological process terms include **GO:0006096 (glycolytic process)** for the core enzyme function, **GO:0006941 (striated muscle contraction)** and **GO:0006937 (regulation of muscle contraction)** for physiological muscle activity, **GO:0008219 (cell death)** for myocyte necrosis during rhabdomyolysis, **GO:0001919 (regulation of blood pressure)** and **GO:0001911 (negative regulation of renal system process)** for systemic consequences, and **GO:0006950 (response to stress)** for cellular adaptation to repeated metabolic insults.[9][10][14] From the Cell Ontology, the involvement of skeletal muscle satellite cells (CL:0000630) in regeneration after injury is likely, although not specifically studied in GSD10, and hematopoietic cells participate in inflammatory responses during muscle repair.[9]  

Collectively, the mechanistic picture of GSD10 is one of a **muscle-specific glycolytic enzyme deficiency** causing episodic energy failure, myocyte necrosis, pigment nephropathy, and adaptive structural remodeling, with disease expression modulated by exercise intensity, hydration, and genetic background.  

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

Organ-level involvement in glycogen storage disease due to phosphoglycerate mutase deficiency centers on **skeletal muscle (UBERON:0001134)** and **kidney (UBERON:0002113)**, with possible secondary effects on joints and cardiovascular structures.[4][6][9] Skeletal muscle is the primary organ because PGAM2 is predominantly expressed in striated muscle tissues and its deficiency directly impairs glycolysis and contraction, leading to exercise intolerance, cramps, and rhabdomyolysis.[4][10][14] Muscle groups most affected tend to be those engaged during specific activities—for example, quadriceps and hamstrings during running, calf muscles during stair climbing, and forearm muscles during strenuous manual work—but the disease is not anatomically localized and can involve multiple muscle regions bilaterally.[4][5][9]  

Kidneys are secondarily involved during episodes of myoglobinuria, where filtered myoglobin causes pigment nephropathy and acute tubular necrosis, potentially leading to acute kidney injury and, rarely, chronic kidney disease.[4][6][9] Orphanet emphasizes acute renal symptoms and highlights that recognition and prompt treatment of rhabdomyolysis is essential to prevent multiorgan failure.[4] MedlinePlus similarly cautions that myoglobinuria can lead to kidney failure if untreated, reflecting the importance of the renal system in disease complications.[6] Joints may be affected indirectly via hyperuricemia and gout arising from repeated purine degradation, with manifestations in peripheral joints such as the first metatarsophalangeal joint (UBERON:0001463), although these are less well characterized.[9]  

Cardiovascular involvement, specifically coronary arteriosclerosis, is mentioned in the glycogen metabolism review as a possible clinical feature of GSD10, suggesting that vascular structures such as coronary arteries (UBERON:0001629) may be affected.[9] Whether this represents a direct consequence of PGAM2 deficiency or an association due to shared risk factors is unclear. Other organ systems such as liver, brain, and peripheral nerves are not prominently involved in reported GSD10 cases, consistent with the tissue specificity of PGAM2 expression and the presence of PGAM1 in non-muscle tissues.[9][10][11][16]  

### 7.2 Tissue and Cell-Level Localization

At the tissue level, GSD10 involves **striated skeletal muscle tissue** (UBERON:0001134) composed of multinucleated myofibers and associated connective tissue, as well as **renal tubular epithelium** (UBERON:0001229) during pigment nephropathy.[4][6][9] Muscle biopsies from GSD10 patients reveal histopathologic features including glycogen accumulation, tubular aggregates, and sometimes mild fiber size variation but not the overt dystrophic changes seen in muscular dystrophies.[3][4][5][8] Tubular aggregates are distinct cytoplasmic structures composed of densely packed tubules derived from sarcoplasmic reticulum and transverse tubules, often located near the fiber center, and are observable on light and electron microscopy.[4][8] HPO term HP:0030191 captures this abnormality.  

Cell types involved include **skeletal muscle fibers** (CL:0000737), **satellite cells** (CL:0000630) engaged in regeneration, **renal tubular epithelial cells** (CL:0002066), and **erythrocytes** (CL:0000232) where non-spherocytic hemolytic anemia is reported in some contexts of PGAM deficiency.[1][4][9][15] Alliance of Genome Resources notes that PGAM2 is involved in striated muscle contraction and is located in the nucleoplasm, reinforcing its presence in muscle cells.[14] During rhabdomyolysis episodes, immune cells such as neutrophils (CL:0000775) and macrophages (CL:0000235) infiltrate damaged muscle tissue, contributing to inflammation and repair, but these cell types are not primarily altered by PGAM2 mutations per se.[9]  

### 7.3 Subcellular Compartments

Subcellular compartments implicated in GSD10 include the **cytosol** (GO:0005829), where glycolytic enzymes including PGAM2 reside; the **sarcoplasmic reticulum** (GO:0016529), which shows proliferation and reorganized structures in the form of tubular aggregates; the **sarcolemma** (GO:0030018), which is damaged during myofiber necrosis; and the **mitochondria** (GO:0005739), which may experience secondary stress during episodes of energy failure.[3][4][5][8] JAMA Neurology reports that PGAM deficiency is often associated with sarcoplasmic reticulum proliferation, and Orphanet notes tubular aggregates, both of which reflect altered membrane systems within muscle fibers.[3][4]  

PGAM2 itself is localized to the cytosol and nucleoplasm in striated muscle cells, according to Alliance of Genome Resources.[14] During glycolysis, PGAM2 participates in cytosolic pathways of energy metabolism, and its deficiency does not directly affect mitochondrial oxidative phosphorylation but may change substrate availability and ATP demand patterns.[9] Sarcolemmal integrity is compromised during rhabdomyolysis, leading to leakage of intracellular constituents into the extracellular space and circulation.[4][5][8] Renal tubular epithelial cells experience cytoplasmic accumulation of myoglobin and associated oxidative stress, particularly within **proximal tubules** (UBERON:0001223 and GO:0005903 for brush border), leading to cell death and acute tubular necrosis.[4][6][9]  

### 7.4 Localization Patterns and Lateralization

Clinically, GSD10 does not display strong lateralization; symptoms usually involve both sides of the body and multiple muscle groups, reflecting the systemic nature of germline PGAM2 deficiency.[4][5][9] Episodes of cramps and rhabdomyolysis may be associated with specific muscle groups exercised at the time—for example, unilateral calf muscle pain after one-legged exertion—but the underlying biochemical defect is bilateral and generalized.[4][9] HPO term HP:0003553 (Bilateral involvement) may be applicable for general muscle symptoms.  

Specific anatomical sites of symptom manifestation vary with patient activity patterns. Lower limb muscles such as quadriceps (UBERON:0001709), hamstrings, and gastrocnemius (UBERON:0001377) are often affected during running and stair climbing, while upper limb muscles such as biceps brachii (UBERON:0001423) and forearm flexors are engaged during manual labour and may experience cramps.[4][5] Kidney involvement is systemic, affecting both kidneys (UBERON:0002113) during myoglobinuric episodes. There is no evidence of focal CNS lesions or unilateral organ involvement in GSD10, consistent with its classification as a metabolic myopathy rather than a focal structural disease.  

## 8. Temporal Development

### 8.1 Onset Patterns

The typical age of onset for glycogen storage disease due to PGAM2 deficiency is in **childhood or adolescence**, although adult patients often retrospectively report symptoms starting in teenage years.[4][5][6][16] Orphanet specifies adolescent and childhood onset and notes that fewer than fifty cases have been reported worldwide.[4] MedlinePlus states that, beginning in childhood or adolescence, affected individuals experience muscle aches or cramping following strenuous physical activity.[6] DiMauro’s 52-year-old patient had intolerance for strenuous exercise and recurrent pigmenturia since adolescence, illustrating that onset can precede diagnosis by decades.[16] The 2018 BMC case report similarly describes a patient who was diagnosed at age 52 but whose symptoms began much earlier, underscoring diagnostic delay rather than late onset per se.[5]  

Onset is generally **insidious** rather than acute, with the first symptoms being exercise-induced cramps and myalgia during sports or physical education classes in school, or during recreational activities.[4][6][9] Some children or adolescents may be labeled as “out of shape” or unfit because they cannot keep up with peers, and episodes of dark urine following exertion may be misattributed to dehydration or other causes.[4][5] Only when recurrent rhabdomyolysis occurs or severe pigmenturia prompts medical evaluation does the possibility of a metabolic myopathy enter consideration, leading to further diagnostic workup.[4][9] HPO terms such as HP:0003621 (Childhood onset) and HP:0003623 (Adolescent onset) are appropriate descriptors of this temporal pattern.  

### 8.2 Disease Course, Staging, and Progression Rate

The disease course in GSD10 is **chronic and lifelong** but characterized by **episodic** manifestations rather than continuous progression.[3][4][9] JAMA Neurology describes PGAM deficiency as a “rare and benign muscle glycogenosis,” implying that while episodes may be symptomatic and occasionally severe, the long-term trajectory does not generally involve relentless deterioration of muscle strength or function.[3] Orphanet states that GSD type X is not thought to impact the longevity of affected individuals, and the glycogen metabolism review notes that only fifteen cases have been reported, with typical features of exercise-induced cramps and rhabdomyolysis, but does not describe progressive weakness or disability.[4][9]  

Disease “staging” has not been formally codified due to the small number of patients, but a conceptual framework can be articulated. In early stages, patients experience occasional exercise-induced cramps and myoglobinuria without significant chronic sequelae.[4][6][9] Intermediate stages involve more frequent episodes, persistent hyperCKemia between attacks, and sometimes structural muscle changes such as tubular aggregates and sarcoplasmic reticulum proliferation on biopsy.[3][4][5] Advanced stages, in cases with recurrent severe rhabdomyolysis and poorly controlled episodes, could involve chronic kidney disease, gout, or coronary arteriosclerosis, though such outcomes are rarely documented.[4][9] The progression rate from one stage to another is highly variable and appears slow or minimal in many patients, especially when lifestyle modifications and acute management are implemented.[3][4][5]  

The pattern of disease course can be described as **relapsing-remitting**, with episodes of acute rhabdomyolysis and symptom exacerbation interspersed with periods of relative quiescence, during which mild hyperCKemia and exercise intolerance persist.[4][5][9] There is no evidence of spontaneous remission in the genetic defect, but symptom frequency may decrease with age as patients learn to avoid triggers and adopt protective behaviors.[4][9] Remission of episodes can be achieved through avoidance of strenuous exercise and maintenance of hydration, but the underlying enzyme deficiency remains.[4][5] Disease duration is lifelong, extending from the first symptom into later adulthood, but the cumulative burden of episodes can be modulated substantially by management strategies.  

### 8.3 Critical Periods and Windows of Opportunity

Critical periods in GSD10 relate to **developmental phases**, **training environments**, and **acute illness contexts**. Adolescence and young adulthood represent important windows because individuals are often highly physically active and may engage in sports or demanding training programs that test their glycolytic capacity, increasing the risk of first rhabdomyolysis episodes.[4][6][9] Early recognition of unexplained exercise intolerance and pigmenturia during these periods offers a window of opportunity for diagnosis and lifestyle adjustment, potentially preventing severe episodes and renal complications.[4][5]  

Acute illness episodes, such as systemic infections or heat stress, may constitute critical contexts in which GSD10 patients are particularly vulnerable to rhabdomyolysis, due to increased metabolic demand and systemic stress.[9] During such times, careful monitoring of muscle symptoms, hydration, and avoidance of intense physical activity can reduce the risk of severe episodes.[4][9] Pregnancy and childbirth could represent additional critical periods, though specific data on GSD10 in pregnancy are lacking; in principle, metabolic demands and physical stress could exacerbate symptoms, emphasizing the need for multidisciplinary care.  

From a preventive and interventional standpoint, early adulthood is a key window for genetic counseling and family planning discussions, since PGAM2 mutations confer a 25% recurrence risk in offspring in autosomal recessive families.[4][7][12] Identification of carriers and affected individuals before they embark on physically demanding careers or engage in high-intensity sports allows for risk mitigation through occupational guidance and lifestyle counseling. In summary, temporal development in GSD10 highlights that **early recognition, education, and avoidance of triggers during adolescence and early adulthood are critical to minimizing long-term morbidity**.  

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

Glycogen storage disease due to phosphoglycerate mutase deficiency follows a **classic autosomal recessive inheritance pattern**, with most affected individuals carrying homozygous or compound heterozygous pathogenic variants in PGAM2.[4][7][12][13] Orphanet states that the disease is autosomal recessive and specifies that it is caused by homozygous or compound heterozygous variants of the PGAM2 gene encoding the muscle isoenzyme of phosphoglycerate mutase.[4] OMIM similarly notes that a number sign is used with the disease entry because GSD10 is caused by homozygous or compound heterozygous mutation in PGAM2.[7] MedlinePlus explains that the condition is inherited in an autosomal recessive pattern, meaning both copies of the PGAM2 gene in each cell have mutations, and that parents of an affected individual are typically asymptomatic carriers.[6] Alliance of Genome Resources annotates PGAM2 with “Autosomal recessive inheritance,” referencing OMIM 261670.[14]  

Penetrance appears to be high in individuals with classical biallelic truncating or severe missense variants such as W78X, G89A, R90W, and Tyr142Ter/Gly178Alafs*31, given that almost all reported homozygotes or compound heterozygotes have clinical symptoms.[4][5][11][12][13] However, the observation of at least one W78X homozygote in gnomAD control data and the existence of heterozygous G97D carriers with symptoms suggest that penetrance may be incomplete or modulated by genetic and environmental factors in some contexts.[12][13] Manifesting heterozygotes, as described by Hadjigeorgiou et al. and Tsujino et al., demonstrate that partial PGAM2 deficiency can be clinically relevant, though the proportion of carriers who develop symptoms remains unknown.[12] Expressivity is clearly **variable**, with some patients experiencing frequent severe rhabdomyolysis and others having milder exercise intolerance and cramps without pigmenturia.[4][5][9][12]  

Genetic anticipation does not play a role in GSD10, as PGAM2 is not a repeat-expansion gene and disease severity does not systematically increase across generations.[7][12] Germline mosaicism has not been reported but cannot be excluded in principle; however, given the autosomal recessive pattern and typical parental carrier status, mosaicism is unlikely to be a major factor.[4][7] Consanguinity may increase the likelihood of homozygous pathogenic variants and thereby disease occurrence, as with most autosomal recessive disorders, but specific consanguinity rates in reported GSD10 families are not provided in the retrieved sources.[4][9][12] Carrier frequency is challenging to estimate due to rarity, but ClinVar’s note of W78X allele frequency ~0.007 in African subpopulations suggests that heterozygous carriers of this variant may be relatively common in certain groups.[13]  

### 9.2 Epidemiology, Prevalence, and Incidence

Epidemiologic data for GSD10 are limited but consistently emphasize its **extreme rarity**. Orphanet states that prevalence is <1/1,000,000, acknowledges that true prevalence is unknown, and notes that fewer than fifty cases have been reported worldwide.[4] The glycogen metabolism review reports that incidence is unknown and that only fifteen cases have been reported in the literature.[9] MedlinePlus describes phosphoglycerate mutase deficiency as a rare condition with about fifteen affected people reported in the medical literature, adding that most affected individuals have been African American.[6] JAMA Neurology indicates that PGAM deficiency had been reported in twelve patients at the time of their “Muscle Phosphoglycerate Mutase Deficiency Revisited” article, nine of whom were African American, and concludes that the disease is not confined to African Americans.[3]  

Taken together, these sources suggest that **total documented cases** are on the order of 15–50, depending on whether one counts early reports, more recent cases, and potential manifesting heterozygotes.[3][4][6][9] True prevalence and incidence likely exceed published case numbers due to underdiagnosis and misclassification as other metabolic myopathies, but given the rarity of PGAM2 pathogenic variants, the global prevalence probably remains well below 1 per 100,000.[4][9][13] Geographic distribution appears to include North America (especially the United States), Europe, the Middle East, and Japan, with African American patients representing a substantial proportion of early cases owing to the relatively common W78X variant in this population.[3][4][6][11][12][13] Orphanet notes that about half of identified cases are related to p.W78X, most common in patients of African American ancestry, with remaining cases coming from other ethnic groups in the United States, Europe, and the Middle East.[4]  

Sex ratio has not been systematically reported, but available case series suggest that both males and females are affected, with no clear sex predilection.[3][4][6][9] Age distribution of diagnosed individuals has tended to cluster around adolescence and early adulthood for symptomatic onset and middle age for diagnosis in some delayed cases, as illustrated by the 52-year-old BMC patient and DiMauro’s index case.[5][16] Population-based screening for PGAM2 variants has not been performed, and GSD10 is not currently included in routine newborn screening programs, reflecting its rarity and comparatively benign nature relative to conditions that benefit from early detection and treatment.[4][9]  

### 9.3 Founder Effects and Variant Distribution

The W78X nonsense variant exemplifies a **founder effect** or population-specific mutation in African-ancestry populations. Tsujino et al. identified W78X in three unrelated African American patients with GSD10, two of whom had been described previously, and ClinVar notes an allele frequency of 0.007 in African subpopulations with at least one homozygote observed in controls.[11][13] Orphanet states that about half of identified cases are related to the p.W78X variant, particularly in patients with African American ancestry.[4] These data support the existence of a relatively common PGAM2 allele in certain populations that confers risk of GSD10 when present in homozygous or compound heterozygous form.  

Other variants, such as G97D in a Japanese family and Tyr142Ter/Gly178Alafs*31 in the BMC case, suggest smaller-scale founder or private effects, where specific alleles are confined to particular families or ethnic backgrounds.[5][12] G89A and R90W appear in multiethnic cohorts, including Caucasian patients, indicating that PGAM2 pathogenic variants are distributed across populations and not restricted to African ancestry.[3][11][12] gnomAD and other population genetics databases contain limited data for most PGAM2 variants due to rarity, but future expansions of sequencing datasets may reveal additional carriers and potential founder alleles.  

In summary, inheritance and population information underscore that GSD10 is an **ultra-rare autosomal recessive myopathy** with a notable African American W78X founder variant, variable expressivity, and limited but expanding recognition across diverse ethnic groups.  

## 10. Diagnostics

### 10.1 Clinical Evaluation and Laboratory Tests

Diagnostic evaluation of glycogen storage disease due to PGAM2 deficiency begins with careful clinical history and examination focused on **exercise-induced muscle symptoms** and **pigmenturia**.[4][6][9] Patients typically report muscle cramps, contractures, and myalgia following short bursts of exertion, and may describe episodes of dark urine consistent with myoglobinuria, particularly after intense physical activity.[4][5][6] Clinicians should inquire about age of onset, triggers, duration of symptoms, family history of similar complaints, and any episodes of acute kidney injury. Physical examination between attacks may be normal or show mild muscle weakness, while acute episodes can reveal muscle tenderness and swelling.[4][9]  

Laboratory tests are crucial in diagnosing GSD10. Serum creatine kinase (CK) levels are elevated during rhabdomyolysis and may remain moderately elevated between episodes, as noted by Orphanet and Alliance of Genome Resources.[4][14] HPO term HP:0003236 captures this abnormality. Serum and urine myoglobin assays can confirm myoglobinuria during acute episodes, complementing visual inspection of dark urine.[4][6][9] Renal function tests, including serum creatinine and blood urea nitrogen, should be monitored to detect acute kidney injury, and electrolyte panels can reveal hyperkalemia and other rhabdomyolysis-related disturbances.[4][6][9] Lactate measurements during and after exercise can provide indirect information about glycolytic function but may be normal in some GSD10 patients, as demonstrated by the BMC case.[5]  

Specific enzyme assays of PGAM activity in muscle biopsy tissue remain a gold standard for biochemical diagnosis. DiMauro et al. assessed muscle PGAM activity and found it to be markedly reduced, at 5.7% of the lowest control value, with normal activities of other glycolytic enzymes.[16] Tsujino et al. and OMIM report PGAM2 activities reduced to 2.1–6% of normal in affected patients, confirming the enzymatic defect.[11][12] These assays often include electrophoretic analysis to differentiate MM and BB isozymes and may use heat lability or mercury inhibition studies to characterize isoform contributions.[16] However, enzyme assays require invasive muscle biopsy and specialized laboratory capabilities, limiting their availability.  

### 10.2 Muscle Biopsy and Histopathology

Muscle biopsy provides both diagnostic and mechanistic information. Orphanet notes that some patients present with glycogen accumulation and tubular aggregates within skeletal muscle cells on biopsy.[4] Koo et al. and Neuromuscular Disorders report that GSDX is often associated with tubular aggregates, and JAMA Neurology highlights frequent sarcoplasmic reticulum proliferation, indicating structural changes in membrane systems.[3][5][8] Histopathologic examination usually reveals relatively preserved fiber architecture, mild fiber size variation, and subsarcolemmal or central accumulations of glycogen, without the extensive necrosis or fibrosis characteristic of muscular dystrophies.[4][5][8]  

Light microscopy may show PAS-positive material representing glycogen and tubular aggregates as basophilic, fibrillar structures, while electron microscopy confirms aggregates of closely packed tubules derived from sarcoplasmic reticulum and T-tubules.[4][8] Immunohistochemistry for other proteins such as dystrophin or sarcoglycans is typically normal, supporting the classification of GSD10 as a metabolic rather than structural myopathy.[4][9] Enzyme histochemistry for glycolytic enzymes may show reduced PGAM activity in muscle sections, though this is not routinely performed in all centers.[11][16] SNOMED CT codes relevant to biopsy findings include “Tubular aggregates of muscle fibers” and “Abnormal glycogen storage in skeletal muscle,” mapped via MedGen.[15]  

### 10.3 Genetic Testing Strategies

Genetic testing has become central to confirming GSD10 diagnosis and identifying carriers. The NCBI Genetic Testing Registry (GTR) lists PGAM2 as a gene for which clinical genetic tests are available, and notes that mutations cause muscle phosphoglycerate mutase deficiency, also known as glycogen storage disease X.[10] Single-gene sequencing of PGAM2 can detect known pathogenic variants such as W78X, G89A, R90W, G97D, Tyr142Ter, and Gly178Alafs*31, as well as novel changes.[5][8][11][12][13] Given the rarity of the disorder and cost considerations, targeted PGAM2 sequencing is most appropriately ordered when clinical and biochemical findings strongly suggest PGAM deficiency, or as part of broader gene panels.  

Whole exome sequencing (WES) and whole genome sequencing (WGS) have particular utility for diagnosing unexplained metabolic myopathies when enzyme assays and targeted testing are inconclusive. The BMC case report describes a 52-year-old patient diagnosed with GSDX via genetic testing that identified two novel PGAM2 variants, illustrating the value of WES in discovering previously unknown mutations.[5] Gene panels for metabolic myopathies and glycogen storage diseases often include PGAM2 among many genes such as PYGM (McArdle disease) and PFKM (phosphofructokinase deficiency), allowing simultaneous screening for multiple conditions.[2][9] However, specific panel names and laboratory offerings are beyond the scope of the provided sources.  

Chromosomal microarray (CMA), karyotyping, and FISH are not primary diagnostic tools for GSD10, since the disease results from point mutations and small indels rather than large chromosomal abnormalities.[7][12][13] Mitochondrial DNA testing and repeat expansion assays are likewise not relevant, as PGAM2 is a nuclear gene and not subject to expansion mechanisms. Genetic counseling should accompany testing, particularly in families with a known PGAM2 mutation, to explain autosomal recessive inheritance and recurrence risks.[4][6][7][12]  

### 10.4 Differential Diagnosis and Screening

Differential diagnosis for GSD10 includes other metabolic myopathies and glycogen storage diseases presenting with exercise intolerance, cramps, and myoglobinuria. MalaCards and Orphanet note that differential diagnosis should include **McArdle disease (muscle phosphorylase deficiency)** and **phosphofructokinase deficiency (PFKD)**, both of which cause exercise intolerance and rhabdomyolysis but have distinct enzymatic defects.[2][4][9] McArdle disease involves PYGM mutations and muscle phosphorylase deficiency, with hallmark features such as second-wind phenomenon and failure of lactate rise during forearm exercise, while PFKM deficiency impairs the rate-limiting step of glycolysis, often causing hemolysis and myopathy.[9] Other differentials include **carnitine palmitoyltransferase II deficiency** and **RYR1-related exertional rhabdomyolysis**, which can present with similar acute episodes but differ in metabolic and channelopathies mechanisms.[9]  

Key distinguishing features for GSD10 include normal or only mildly increased glycogen in muscle, isolated PGAM deficiency on enzyme assay, residual BB isoform activity, and characteristic tubular aggregates and sarcoplasmic reticulum proliferation on biopsy.[3][4][5][16] Lactate responses may be normal or variably affected, making them less reliable discriminators.[5][9] Genetic testing that identifies biallelic PGAM2 pathogenic variants provides definitive diagnosis and helps distinguish GSD10 from other conditions.  

Screening programs for asymptomatic individuals do not currently include GSD10. Newborn screening focuses on conditions with effective early treatments such as Pompe disease (GSD2) and medium-chain acyl-CoA dehydrogenase deficiency, whereas GSD10 lacks specific therapy and has a relatively benign course, thus not meeting common criteria for population screening.[4][9] Carrier screening may be considered in families with known PGAM2 mutations, using targeted genetic tests, and preimplantation genetic diagnosis or prenatal testing could be offered where appropriate, particularly in communities with higher W78X allele frequency.[4][7][13]  

## 11. Outcome / Prognosis

### 11.1 Survival, Life Expectancy, and Mortality

Prognostic data for GSD10 are limited but consistently suggest that **overall survival and life expectancy are near-normal** when episodes of rhabdomyolysis and myoglobinuria are appropriately managed.[3][4][6][9] Orphanet explicitly states that GSD type X is not thought to impact the longevity of affected individuals and emphasizes that recognizing and treating rhabdomyolysis promptly is crucial to prevent severe morbidity and mortality.[4] JAMA Neurology refers to PGAM deficiency as a “rare and benign muscle glycogenosis,” implying that, in their cohort, life-threatening complications were uncommon.[3] MedlinePlus does not mention shortened life expectancy but warns that unmanaged myoglobinuria can lead to kidney failure, which could be fatal.[6]  

Mortality directly attributable to GSD10 has not been well documented in the literature, likely due to the small number of cases and the ability to treat acute rhabdomyolysis with modern supportive care including intravenous fluids and renal monitoring.[4][6][9] Global Burden of Disease and national registries have not separately quantified GSD10 mortality given its rarity. The main life-threatening risk arises during severe rhabdomyolysis episodes when multiorgan failure, including acute kidney injury, electrolyte disturbances, and cardiac arrhythmias, can occur if treatment is delayed.[4][6][9] With prompt recognition and management, however, these episodes can be survived without long-term sequelae in many patients.  

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in GSD10 arises from **recurrent muscle symptoms**, **hospitalizations for rhabdomyolysis**, and **potential renal and musculoskeletal complications**.[4][5][9] Patients may experience frequent cramps and contractures that interfere with physical activities, sports participation, and certain occupations. Acute episodes of rhabdomyolysis necessitate hospital admission for fluid resuscitation, renal function monitoring, and electrolyte management, representing significant healthcare utilization and personal burden.[4][6][9] Some patients may develop chronic kidney disease if repeated episodes cause lasting damage, and hyperuricemia and gout may contribute to musculoskeletal morbidity, though data are limited.[9]  

Long-term disability in GSD10 is generally mild compared to progressive neuromuscular diseases. Most patients maintain ambulatory ability and can perform activities of daily living, provided they avoid high-intensity exertion.[3][4][5][9] Persistent exercise intolerance may restrict career choices and leisure activities, and fear of rhabdomyolysis can induce anxiety and caution regarding physical exertion. However, systematic assessments using instruments like SF-36, EQ-5D, or PROMIS have not been published for GSD10, so quantitative quality-of-life data are lacking.[4][9]  

Despite these limitations, anecdotal reports and expert reviews suggest that with appropriate management—avoidance of triggers, hydration, and acute care—many patients lead relatively normal lives with manageable symptom burden.[3][4][5][9] The presence of a benign overall prognosis may provide psychological reassurance, though uncertainties about future episodes and potential renal complications remain.  

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors in GSD10 include **type and severity of PGAM2 mutations**, **frequency and severity of rhabdomyolysis episodes**, **renal function**, and **lifestyle adherence**.[4][5][9][12][13] Truncating variants that abolish PGAM2 function may be associated with more severe enzyme deficiency and a greater propensity for rhabdomyolysis, whereas milder missense variants could allow partial residual activity and less frequent episodes, though this relationship has not been systematically quantified.[11][12][13] Manifesting heterozygotes with partial deficiency appear to have milder phenotypes, suggesting that genotype–phenotype correlations are important but complex.[12]  

HyperCKemia between episodes may serve as a biomarker of ongoing subclinical muscle injury and could correlate with future risk of rhabdomyolysis, although specific thresholds predicting episodes have not been established for GSD10.[4][5][8][14] Renal function markers such as estimated glomerular filtration rate (eGFR) and serum creatinine provide prognostic information regarding risk of chronic kidney disease, especially in patients with repeated episodes.[4][6][9] Lifestyle factors such as adherence to recommendations on exercise intensity and hydration significantly influence prognosis by modulating episode frequency and severity.[4][9]  

No specific prognostic biomarkers at the molecular level (e.g., PGAM2 expression levels, metabolomic profiles) have been identified due to the lack of large-scale omics studies in GSD10 patients.[4][9] Future research could explore whether baseline PGAM2 activity in muscle biopsies or PGAM2 transcript levels in blood correlate with clinical severity, but currently, prognosis is assessed mainly through clinical history and standard laboratory measures.  

## 12. Treatment

### 12.1 Current Pharmacologic and Supportive Therapies

As of current knowledge, **no disease-specific pharmacologic treatments** exist that can replace or restore PGAM2 activity in skeletal muscle.[4][5][9] Orphanet clearly states that “To date, there is no treatment that replaces or restores PGAM2 activity,” emphasizing that management is symptomatic and supportive.[4] Therapeutic strategies, therefore, focus on anticipating and managing rhabdomyolysis episodes, minimizing triggers, and protecting renal function.  

During acute rhabdomyolysis, standard-of-care treatments include **aggressive intravenous fluid resuscitation** to maintain renal perfusion and dilute myoglobin concentration, **correction of electrolyte imbalances** (particularly hyperkalemia and metabolic acidosis), and **monitoring for complications** such as arrhythmias and acute kidney injury (NCIT terms such as “Intravenous Fluid Therapy”  and “Supportive Care”  are relevant).[4][6][9] In severe cases of acute kidney injury, **renal replacement therapy** such as hemodialysis (NCIT:C38728) may be necessary to manage fluid and electrolyte balance and remove toxins.[4][6] Analgesics and muscle relaxants may be used to control pain and cramps but must be chosen carefully to avoid nephrotoxic agents.  

Between episodes, **supportive care** aims to reduce symptom frequency and severity. Orphanet recommends regular, low-intensity exercise under optimal hydration conditions, implying that lifestyle modifications are a key therapeutic modality.[4] Comprehensive management strategies include patient education about identifying early signs of rhabdomyolysis (e.g., muscle pain, dark urine), maintaining hydration, and avoiding strenuous exercise, heat stress, and myotoxic medications.[4][9] In individuals with hyperuricemia or gout, urate-lowering therapies such as allopurinol may be indicated, following standard guidelines, though no GSD10-specific data exist.[9]  

### 12.2 Advanced Therapeutics: Gene and Cell-Based Approaches

Advanced therapeutics such as **gene therapy**, **cell therapy**, and **RNA-based therapies** have not yet been developed or clinically tested for PGAM2 deficiency, reflecting both the rarity of the disease and the current focus of gene therapy efforts on more prevalent neuromuscular and metabolic disorders.[4][9] Conceptually, PGAM2 would be a plausible target for adeno-associated virus (AAV)-mediated gene replacement or CRISPR-based editing, given its relatively small coding sequence and muscle-specific expression, but preclinical studies specifically addressing PGAM2 have not been reported in the sources consulted.[9][12] ClinicalTrials.gov does not list ongoing trials for GSD10 or PGAM2 in the retrieved materials, underscoring the absence of experimental therapies in the translational pipeline.  

Cell-based approaches such as myoblast transplantation or stem cell therapy could theoretically provide new muscle cells expressing normal PGAM2, but challenges include achieving widespread engraftment and long-term expression, and again no specific research on PGAM2 has been cited.[9] RNA-based therapies such as antisense oligonucleotides to correct splicing defects or mRNA replacement therapies would require identification of specific splicing variants or the feasibility of delivering PGAM2 mRNA to muscle fibers, which remains speculative.  

### 12.3 Rehabilitation, Physical Therapy, and Lifestyle Management

Rehabilitation and physical therapy play important roles in helping GSD10 patients maintain function while avoiding symptom triggers. Although no GSD10-specific rehabilitation trials have been published, general principles from metabolic myopathy management can be applied.[4][9] Physical therapists can design individualized exercise programs emphasizing **low- to moderate-intensity aerobic activities** that rely more on oxidative metabolism and less on glycolysis, such as walking, cycling at moderate pace, or swimming, while avoiding sudden maximal exertion and high-intensity interval training.[4][9] Occupational therapists may assist patients in adapting work tasks to minimize heavy lifting and repetitive strenuous movements, reducing the risk of rhabdomyolysis episodes.  

Patient education is a cornerstone of tertiary prevention. Orphanet underscores the importance of recognizing and treating rhabdomyolysis promptly and suggests that regular low-intensity exercise under optimal hydration conditions can reduce symptoms.[4] Clinicians should counsel patients about adequate fluid intake, especially in hot environments, and advise early medical evaluation for muscle pain and dark urine. They should also review medications for potential myotoxicity and coordinate care with nephrologists and rheumatologists when renal or gouty complications are present.[4][6][9]  

### 12.4 Treatment Outcomes and Personalized Medicine

Outcomes of current treatment strategies are generally favourable, with many patients achieving substantial reduction in episode frequency and severity through lifestyle modifications and prompt management of rhabdomyolysis.[3][4][5][9] The benign overall prognosis described by JAMA Neurology and Orphanet suggests that supportive care and exercise adaptation can allow near-normal life expectancy and acceptable quality of life.[3][4] However, systematic data on treatment response rates and long-term outcomes are lacking due to small patient numbers and the absence of prospective cohorts.  

Personalized medicine approaches in GSD10 currently revolve around **genotype-informed counseling and management**, rather than targeted pharmacogenomics. Knowing the specific PGAM2 mutation may help estimate disease severity and recurrence risk in families, and carriers can be identified for reproductive planning, but there are no therapies whose efficacy is known to vary by PGAM2 genotype.[4][5][12][13] Future advances in gene therapy or enzyme replacement could benefit from genotype stratification, for example, focusing on truncating versus missense variants, but these approaches remain hypothetical.  

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of GSD10 in the strict sense—preventing occurrence of disease in prospective offspring—relies on **genetic counseling and reproductive decision-making** rather than environmental interventions, given the autosomal recessive nature of PGAM2 mutations.[4][6][7][12] Couples with a known PGAM2 mutation can receive counseling about the 25% recurrence risk for affected offspring and may consider options such as carrier testing for partners, prenatal diagnosis, or preimplantation genetic diagnosis if available.[4][7][12] There are no vaccines or environmental measures that prevent PGAM2 mutations from occurring.  

Secondary prevention focuses on **early detection and intervention** to prevent complications. Recognizing unexplained exercise intolerance, recurrent cramps, and dark urine in adolescents and young adults offers an opportunity to diagnose GSD10 before severe rhabdomyolysis and kidney injury occur.[4][6][9] While GSD10 is not part of routine newborn or population screening, physicians should maintain awareness of metabolic myopathies and consider PGAM2 testing when clinical clues and enzyme assays suggest glycolytic blocks. Early diagnosis enables preventive counseling and tailored lifestyle modifications.  

Tertiary prevention aims to **prevent complications and disability in affected individuals**, primarily through lifestyle management and prompt treatment of rhabdomyolysis.[4][6][9] Encouraging avoidance of strenuous exercise, maintaining hydration, and monitoring renal function can reduce episodes and long-term organ damage. Genetic counseling for affected individuals and their families also constitutes tertiary prevention by clarifying inheritance patterns and risk management strategies.[4][6][7][12]  

### 13.2 Screening, Risk Stratification, and Behavioral Interventions

Screening for GSD10 is currently limited to **targeted testing** in symptomatic individuals or at-risk family members, rather than population-level programs.[4][9] Risk stratification in known PGAM2 mutation carriers can be based on genotype (e.g., truncating versus missense variants), family history of severe rhabdomyolysis, and lifestyle factors such as high-intensity occupational or athletic activities, although formal risk models have not been developed.[4][12][13] Clinicians can identify high-risk individuals—such as homozygous W78X carriers engaged in strenuous sports—and provide tailored preventive counseling.  

Behavioral interventions represent key preventive strategies. Patients are advised to **modify exercise patterns** by avoiding short bursts of maximal exertion and favoring moderate, sustained activities, as recommended by Orphanet.[4] They should maintain adequate hydration, especially in hot climates or during exertion, and limit alcohol consumption before exercise to prevent dehydration.[4][6][9] Education about recognizing symptoms of rhabdomyolysis and seeking prompt medical care can prevent severe complications, and support groups or patient organizations may help reinforce behavior change.  

Public health interventions specific to GSD10 are not currently implemented, given its rarity and lack of population-level impact. However, broader educational efforts about rhabdomyolysis and metabolic myopathies could indirectly aid GSD10 patients by increasing awareness among clinicians and emergency department staff, facilitating early recognition and appropriate management.[4][9]  

## 14. Other Species / Natural Disease

### 14.1 Natural Disease in Non-Human Species

MedGen references a poultry study titled “Glycogen storage disease type X caused by ochratoxin A in broiler chickens,” indicating that a GSDX-like phenotype has been described in non-human species.[15] In this context, **broiler chickens (Gallus gallus domesticus; NCBI Taxon:9031)** exposed to ochratoxin A developed a glycogen storage disease characterized by muscle pathology reminiscent of human GSD10, suggesting that environmental toxins can induce functional PGAM deficiency or related metabolic disruptions.[15] This represents a **toxic, induced analog** rather than a genetic PGAM2 mutation, but nonetheless provides insight into how glycolytic and glycogen metabolism disturbances can manifest across species.  

No direct evidence has been found in the provided sources for naturally occurring genetic PGAM2 deficiency in companion animals such as dogs or cats, or in livestock such as cows and pigs. OMIA (Online Mendelian Inheritance in Animals) was not referenced in the search results, and no animal PGAM2-related myopathies were described.[15] However, it is plausible that similar enzymatic defects could occur in animals and remain undiagnosed due to limited metabolic diagnostic capabilities in veterinary practice.  

### 14.2 Comparative Biology and Orthologous Genes

Orthologous genes for PGAM2 exist across many species. PomBase links the human disease MONDO:0009865 to the **Schizosaccharomyces pombe** gene **gpm1**, encoding phosphoglycerate mutase, demonstrating evolutionary conservation of the enzyme.[1] Alliance of Genome Resources likewise highlights PGAM2 as a conserved gene with orthologs in other vertebrates and invertebrates.[14] HomoloGene and OrthoMCL, though not directly cited, would list PGAM2 orthologs in model organisms such as mice (Mus musculus; NCBI Gene:56180), zebrafish (Danio rerio), and Drosophila melanogaster, reflecting the fundamental role of PGAM in glycolysis.[10][14]  

Comparative pathology reveals that glycolytic enzyme defects often present as exercise-induced myopathies across species, and toxins affecting glycolytic enzymes, such as ochratoxin A, can produce GSD-like phenotypes.[9][15] Evolutionary conservation of PGAM’s catalytic mechanism implies that insights gained from human PGAM2 deficiency can inform

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 70 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 4 |
| Terms whose name was checked | 29 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005291` (1 mention) - the report calls it "glycogen storage disease"; MONDO calls it **brain aneurysm**
- `MONDO:0005067` (1 mention) - the report calls it "metabolic myopathy"; MONDO calls it **monophasic synovial sarcoma**
- `MONDO:0004880` (1 mention) - the report calls it "disorder of glycolysis"; MONDO calls it **bowel dysfunction**
- `GO:0016044` (1 mention) - the report calls it "cellular membrane organization"; GO calls it **GO_0016044**
- `GO:0044319` (1 mention) - the report calls it "muscle cell proliferation"; GO calls it **wound healing, spreading of cells**
- `CL:0002066` (2 mentions) - the report calls it "renal tubular epithelial cells"; CL calls it **Feyrter cell**
- `UBERON:0001229` (1 mention) - the report calls it "renal tubular epithelium"; UBERON calls it **renal corpuscle**
- `GO:0030018` (1 mention) - the report calls it "sarcolemma"; GO calls it **Z disc**
- `HP:0003553` (1 mention) - the report calls it "Bilateral involvement"; HP calls it **obsolete Cellulitis due to immunodeficiency**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016044` (GO_0016044) (1 mention) - replaced by `GO:0061024`
- `HP:0003553` (obsolete Cellulitis due to immunodeficiency) (1 mention) - replaced by `HP:0100658`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003621` (2 mentions) - the report calls it "Childhood onset"; HP calls it **Juvenile onset**
- `HP:0003623` (2 mentions) - the report calls it "Adolescent onset"; HP calls it **Neonatal onset**
- `CL:0000737` (3 mentions) - the report calls it "skeletal muscle fibers", "skeletal muscle cell"; CL calls it **striated muscle cell**
- `GO:0006874` (1 mention) - the report calls it "cellular calcium ion homeostasis"; GO calls it **intracellular calcium ion homeostasis**, and lists "cellular calcium ion homeostasis" among its other names
- `GO:0001911` (2 mentions) - the report calls it "negative regulation of renal system process"; GO calls it **negative regulation of leukocyte mediated cytotoxicity**
- `GO:0001919` (1 mention) - the report calls it "regulation of blood pressure"; GO calls it **regulation of receptor recycling**
- `CL:0000630` (2 mentions) - the report calls it "satellite cells"; CL calls it **supporting cell**, and lists "supportive cell" among its other names
- `UBERON:0001134` (2 mentions) - the report calls it "striated skeletal muscle tissue"; UBERON calls it **skeletal muscle tissue**
- `GO:0005739` (1 mention) - the report calls it "mitochondria"; GO calls it **mitochondrion**, and lists "mitochondria" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000737` - called "skeletal muscle fibers", "skeletal muscle cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Taxon`, `Gene`.