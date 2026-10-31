---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-16T11:53:41.819818'
end_time: '2026-10-16T11:57:36.244220'
duration_seconds: 234.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Sclerosing Poikiloderma With Tendon And Pulmonary Involvement
  mondo_id: MONDO:0014310
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 51
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 16
  off_topic: 1
  off_topic_references:
  - PMC:PMC11650971
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 79
  verified: 76
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014310
    reported_labels:
    - MONDO
    ontology_label: hereditary sclerosing poikiloderma with tendon and pulmonary involvement
  obsolete_terms:
  - term_id: HP:0001006
    ontology_label: obsolete Hypotrichosis
    replaced_by: HP:0008070
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Sclerosing Poikiloderma With Tendon And Pulmonary Involvement
- **MONDO ID:** MONDO:0014310 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Sclerosing Poikiloderma With Tendon And Pulmonary Involvement** covering all of the
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

# Hereditary sclerosing poikiloderma with tendon and pulmonary involvement  
## Comprehensive disease-characteristics report

**Preferred contemporary name:** Hereditary fibrosing poikiloderma with tendon contractures, myopathy, and pulmonary fibrosis (**POIKTMP syndrome**)  
**MONDO:** MONDO:0014310  
**Disease class:** Ultra-rare autosomal-dominant Mendelian multisystem fibrosing disorder  
**Established gene:** *FAM111B*  
**Evidence status:** Most clinical knowledge derives from fewer than 40 molecularly confirmed patients, case reports, and small retrospective series; mechanistic evidence is chiefly from transfected human cell lines rather than patient tissues or disease-specific animal models. A 2024 review counted 39 reported mutation-associated cases. [39]

---

## 1. Disease information

### 1.1 Definition and overview

POIKTMP is an age-progressive genodermatosis caused principally by heterozygous pathogenic variants in *FAM111B*. The usual sequence is:

1. Facial or photodistributed poikiloderma, sparse hair, and reduced sweating beginning in infancy;
2. Achilles/triceps-surae and sometimes upper-limb contractures in childhood;
3. Progressive fibrofatty myopathy and weakness;
4. Restrictive respiratory impairment caused by respiratory-muscle weakness, interstitial lung disease, or both;
5. In some adults, rapidly progressive and potentially fatal pulmonary fibrosis.

Additional involvement may include pancreatic exocrine insufficiency, growth failure, liver disease, lymphedema, cataract, and other fibrotic or fatty-degenerative organ abnormalities. In the principal 15-patient series, poikiloderma was universal, muscle weakness occurred in 8/11 evaluable patients, hypohidrosis or heat intolerance in 11/12, and pulmonary fibrosis in 3/6 adults. [16]

> “Key features consist of: (i) early-onset poikiloderma, hypotrichosis and hypohidrosis; (ii) multiple contractures… (iii) diffuse progressive muscular weakness; (iv) pulmonary fibrosis in adulthood…” — Mercier et al., 2015, PMID: **26471370**. [16]

### 1.2 Identifiers and synonyms

| Resource | Identifier/name | Notes |
|---|---|---|
| MONDO | **MONDO:0014310** | Hereditary sclerosing poikiloderma with tendon and pulmonary involvement |
| OMIM phenotype | **615704** | Poikiloderma, hereditary fibrosing, with tendon contractures, myopathy, and pulmonary fibrosis |
| OMIM gene | **615584** | *FAM111B* |
| Orphanet | **ORPHA:221043** | Hereditary fibrosing poikiloderma–tendon contractures–myopathy–pulmonary fibrosis syndrome [46] |
| MedGen | **C3810325** | Hereditary sclerosing poikiloderma with tendon and pulmonary involvement [70] |
| GeneReviews/GTR disease label | Hereditary fibrosing poikiloderma with tendon contractures, myopathy, and pulmonary fibrosis | Listed under *FAM111B* testing [20] |
| MeSH | Supplementary concept: **Poikiloderma, Hereditary Sclerosing** | Related indexed terms include pulmonary fibrosis, contracture, tendon pathology, atrophy, mutation, and cell-cycle proteins [35] |
| ICD-10 | No unique disease-specific code | Depending on purpose, component codes may be used for poikiloderma, congenital skin disorder, myopathy, contracture, or pulmonary fibrosis; these are not equivalent to POIKTMP |
| ICD-11 | No verified unique POIKTMP code | Use the rare-disease identifier alongside component coding where supported |

**Synonyms**

- POIKTMP syndrome;
- hereditary fibrosing poikiloderma with tendon contractures, myopathy, and pulmonary fibrosis;
- hereditary sclerosing poikiloderma with tendon and pulmonary involvement;
- hereditary sclerosing poikiloderma with tendon, muscle, and pulmonary involvement;
- hereditary fibrosing poikiloderma, or HFP.

The name “hereditary sclerosing poikiloderma with tendon and pulmonary involvement” was proposed before discovery of *FAM111B*; the molecularly defined designation POIKTMP is now more informative. OMIM maps the disorder to chromosome 11q12.1 and *FAM111B*. [17]

### 1.3 Data provenance

This entry is an **aggregated disease-level synthesis**, not an individual EHR record. Evidence comes from:

- molecularly confirmed case reports and pedigrees;
- retrospective clinical series;
- pathology/autopsy observations;
- ClinVar, OMIM, Orphanet, GTR, and MONDO;
- experimental human cell-line studies.

Published percentages are subject to ascertainment bias, missing evaluations, age-dependent expressivity, and repeated reporting of the same patients.

---

## 2. Etiology

### 2.1 Primary cause

The established cause is a **heterozygous germline pathogenic variant in *FAM111B***, usually a missense variant clustered near or within its C-terminal trypsin-like serine-peptidase domain. Familial transmission is autosomal dominant, but many cases arise de novo. Whole-exome sequencing established causality in 2013 by identifying segregating or de novo variants in five kindreds. PMID: **24268661**. [5]

> “The three single-nucleotide mutations code for amino acid changes that are clustered within a putative trypsin-like cysteine/serine peptidase domain of FAM111B.” — Mercier et al., 2013, PMID: 24268661. [5]

### 2.2 Genetic risk factors

- A pathogenic heterozygous *FAM111B* allele is the principal risk factor.
- Recurrent variants include:
  - NM_198947.4:c.1861T>G, p.(Tyr621Asp);
  - c.1879A>G, p.(Arg627Gly);
  - c.1883G>A, p.(Ser628Asn).
- De novo occurrence is common: a 2023 report summarized 36 patients and estimated that approximately half had de novo variants. [82]
- Family history confers a **50% transmission probability per pregnancy** for an affected heterozygous parent, subject to viability and reproductive fitness.
- Expressivity is strongly age-dependent and variable, so a mildly affected parent cannot be assumed to predict mild disease in offspring.

No validated susceptibility loci, polygenic risk scores, or clinically established modifier genes have been reported.

### 2.3 Environmental risk factors and triggers

No environmental exposure is known to cause the Mendelian disorder. Potential modifiers of manifestations include:

- **Ultraviolet exposure:** may transiently exacerbate facial erythema and photodistributed skin changes but is not the underlying cause.
- **Heat:** reduced sweating produces heat intolerance.
- **Respiratory infection:** can precipitate deterioration in patients with limited pulmonary reserve. In one adult, interstitial pneumonia worsened after bacterial pneumonia. PMID: **35601499**. [6]
- **Smoking and occupational inhalants:** no POIKTMP-specific association has been demonstrated, but avoidance is prudent in any person at risk of pulmonary fibrosis.
- **Immobility:** can secondarily worsen contractures, deconditioning, and respiratory-muscle weakness; this remains a clinical inference rather than a proven disease interaction.

### 2.4 Protective factors

No genetic protective allele or disease-preventing lifestyle factor is established. Reasonable complication-reduction measures include sun protection, heat precautions, avoidance of smoking and fibrogenic inhalants, vaccination against respiratory pathogens, infection treatment, physiotherapy, and nutritional replacement. These measures do not correct the causal variant.

### 2.5 Gene–environment interaction

Formal gene–environment studies are unavailable. The clearest probable interactions are:

- *FAM111B*-mediated skin vulnerability plus UV exposure → transient erythema/photosensitive exacerbation;
- restrictive lung disease plus respiratory infection or pulmonary edema → acute decompensation;
- exocrine pancreatic insufficiency plus inadequate replacement → malabsorption, low weight, and fat-soluble vitamin deficiency.

---

## 3. Phenotypes

Frequencies below use the best-described 15-patient cohort unless otherwise specified. They should not be interpreted as population prevalence. [16]

| Phenotype/type | Onset, progression, frequency and severity | Functional/QoL impact | Suggested HPO term |
|---|---|---|---|
| Poikiloderma; physical sign | Usually first 6 months; 15/15 in the main cohort; facial and often photo-exposed distribution; may become less prominent with age | Cosmetic burden, photosensitivity, skin fragility | **Poikiloderma, HP:0001029** |
| Telangiectasia and mixed pigmentation; signs | Infantile; part of poikiloderma; hyper- and hypopigmentation | Visible facial difference, sun avoidance | Telangiectasia **HP:0001009**; abnormal skin pigmentation **HP:0001000** |
| Epidermal/skin atrophy and sclerosis; signs/pathology | Early and chronic; scleroderma-like dermal fibrosis and elastic-fiber fragmentation | Reduced skin flexibility; possible lagophthalmos or digit limitation | Skin atrophy **HP:0004334**; sclerodermatous skin |
| Hypotrichosis/alopecia; sign | Early; scalp hair and eyebrows affected in essentially all well-characterized patients; eyelashes variably absent | Psychosocial/cosmetic burden | **Hypotrichosis, HP:0001006**; sparse eyebrows **HP:0045075** |
| Hypohidrosis/heat intolerance; symptom/sign | 11/12 evaluable; lifelong | Risk of overheating, restricted activity in warm environments | **Hypohidrosis, HP:0000966**; heat intolerance |
| Eczematous/ichthyosiform/psoriasiform lesions | Childhood; variable, sometimes steroid-responsive; may improve | Pruritus and need for topical care | Eczematoid dermatitis **HP:0000964**; ichthyosis **HP:0008064** |
| Extremity lymphedema | 7 patients in the main series; variable | Swelling, discomfort, recurrent cellulitis | **Lymphedema, HP:0001004** |
| Recurrent cellulitis | 3 patients in main series | Pain, hospitalization, antimicrobial use | Recurrent skin infections |
| Tendon/muscle contractures | Sometimes by age 2; chiefly triceps surae/Achilles, but biceps and wrist extensors may be involved | Toe walking, pes varus, falls, reduced gait, surgery | **Tendon contracture, HP:0001230**; joint contracture **HP:0001371** |
| Progressive myopathy/weakness | 8/11; median onset 5.9 years, range 1–11; proximal and distal, sometimes axial/respiratory; severity from subclinical MRI change to loss of ambulation | Difficulty climbing stairs, walking, transfers, swallowing, head control; wheelchair in severe cases | **Muscle weakness, HP:0001324**; proximal muscle weakness **HP:0003701**; muscle atrophy **HP:0003202** |
| Fibrofatty muscle replacement | Childhood onward; frequent on MRI/biopsy | Progressive loss of strength and endurance | Abnormality of muscle morphology **HP:0011805** |
| Mild CK elevation | 5/8 tested; maximum approximately 500 IU/L; 3/8 normal | Limited direct impact; useful supportive finding | **Elevated serum creatine kinase, HP:0003236** |
| Restrictive ventilatory defect | Reported in all evaluable patients in the main series, including children; may reflect muscle weakness or lung fibrosis | Exercise intolerance, dyspnea, possible ventilatory support | **Restrictive ventilatory defect, HP:0002091** |
| Interstitial pulmonary fibrosis | 3/6 adults in the principal cohort; generally absent in children; may progress rapidly after respiratory symptoms | Major mortality driver; dyspnea, oxygen/ventilatory requirements | **Pulmonary fibrosis, HP:0002206**; interstitial lung disease **HP:0006530** |
| Exocrine pancreatic insufficiency | 4 patients in principal cohort; pancreatic atrophy/fatty replacement documented | Steatorrhea, diarrhea, malnutrition and vitamin deficiency; improves with enzymes | **Exocrine pancreatic insufficiency, HP:0001738** |
| Growth failure/low weight | 6 patients; variable | Nutritional burden and reduced physical reserve | **Short stature, HP:0004322**; failure to thrive **HP:0001508** |
| Liver involvement | At least 4 in main series; transaminitis, cholestasis, hepatomegaly, duct loss, portal fibrosis, or cirrhosis described | Can progress to portal hypertension, hepatic encephalopathy and liver failure | Elevated transaminases **HP:0002910**; hepatic fibrosis **HP:0001395**; cirrhosis **HP:0001394** |
| Scoliosis | 2 in main cohort | Posture, mobility, and respiratory restriction | **Scoliosis, HP:0002650** |
| Dysphagia/dysarthria | Reported in advanced myopathy | Aspiration and nutritional risk, communication impairment | Dysphagia **HP:0002015**; dysarthria **HP:0001260** |
| Cataract/ocular abnormalities | Cataract uncommon; other reported findings include retinal, corneal, lacrimal, or motility abnormalities | Variable visual impairment | **Cataract, HP:0000518** |
| Nail dysplasia | 3 patients in principal series | Usually minor functional effect | **Nail dysplasia, HP:0001597** |
| Cognitive development | Usually normal | Distinguishes syndrome from many multisystem developmental conditions | Normal cognition—not encoded as a disease phenotype |

No validated POIKTMP-specific quality-of-life instrument, EQ-5D study, SF-36 cohort, or PROMIS analysis was found. QoL effects must presently be inferred from mobility loss, disfigurement, heat intolerance, malabsorption, respiratory disability, and repeated specialist care.

---

## 4. Genetic and molecular information

### 4.1 Gene

| Item | Annotation |
|---|---|
| Gene | ***FAM111B***, FAM111 trypsin-like peptidase B |
| HGNC | **HGNC:24200** |
| NCBI Gene | **374393** |
| OMIM | **615584** |
| Location | **11q12.1** |
| Protein | Nuclear protein with a C-terminal trypsin-like serine-protease domain |
| Inheritance | Germline heterozygous, autosomal dominant |
| Disease mechanism | Best-supported: mutant protease **gain of function/hyperactivity**; some newer work also raises context-dependent dominant-negative effects |
| Constraint/variant pattern | Disease variants are enriched in specific missense clusters rather than being distributed as conventional haploinsufficient null alleles |

### 4.2 Representative pathogenic variants

| Variant, NM_198947.4 | Protein consequence/type | Evidence/classification | Population frequency/origin |
|---|---|---|---|
| c.1262_1264delAAG | p.(Lys421del), in-frame deletion | Reported disease-associated | Ultra-rare/absent from contemporaneous controls |
| c.1289A>C | p.(Gln430Pro), missense | Reported in an affected adult | Absent from databases used in original report |
| c.1292T>C | p.(Leu431Pro), missense | Pathogenic, de novo in a 2023 case | Ultra-rare; germline [82] |
| c.1861T>G | p.(Tyr621Asp), missense | ClinVar pathogenic; familial segregation | ClinVar Variation ID 120217; rs587777236 [76][77] |
| c.1874C>A | p.(Thr625Asn), missense | De novo disease-associated | Absent from ExAC and tested controls in original series |
| c.1879A>G | p.(Arg627Gly), missense | Recurrent pathogenic; de novo and inherited cases | ClinVar Variation ID 120218; rs587777237 [76] |
| c.1883G>A | p.(Ser628Asn), missense | Recurrent pathogenic; experimentally hyperactive protease | ClinVar Variation ID 120219; rs587777238 [76] |
| c.1886T>G | p.(Phe629Cys), missense | ACMG pathogenic; de novo | Absent from gnomAD and 96 Japanese controls; ClinVar Variation ID 1676282 [79] |
| c.1462delT | p.(Cys488Valfs*21), frameshift | Reported likely pathogenic in progressive osseous heteroplasia-like presentation; phenotypic fit with classic POIKTMP is less certain | De novo; germline; PMID 36575358 [87] |

Early disease variants were absent from 388 ethnically diverse controls and the population databases available at discovery. PMID: **24268661**. [5] Current variant-level gnomAD frequencies should be checked against the exact transcript and genome build at curation time; pathogenic POIKTMP alleles are generally absent or exceptionally rare.

### 4.3 Functional consequence

In inducible U2OS cells, disease-associated FAM111B mutants:

- had amplified intrinsic protease activity;
- suppressed DNA and RNA synthesis;
- displaced RFC1, PCNA, and RNA polymerase-II subunit RPB1 from chromatin;
- disrupted microtubules;
- induced caspase-dependent apoptosis.

Introducing a catalytic-inactivating p.Asp544Asn substitution abolished these effects, providing strong in-vitro support for protease-dependent gain of function. PMID associated with EMBO Reports 2020, article e50662. [44]

> “Disease-associated FAM111B mutants display amplified proteolytic activity and phenocopy the cellular impact of deregulated FAM111A catalytic activity.” [44]

### 4.4 Modifier genes, epigenetics, and chromosome abnormalities

- **Modifier genes:** none validated. Two *CLCN1* variants were found in one patient without clinical or EMG myotonia, so modification was unproven.
- **Epigenetics:** no reproducible POIKTMP-specific DNA-methylation or histone signature has been established.
- **Chromosomal abnormalities:** no recurrent deletion, duplication, translocation, or aneuploidy defines the disorder.
- **Somatic variants:** disease-causing variants are germline; somatic *FAM111B* dysregulation studied in cancers should not be conflated with POIKTMP.
- **Cancer predisposition:** pancreatic cancer and spontaneous chromosome instability have been reported, but patient numbers are insufficient to quantify risk or establish surveillance standards. Patient lymphocytes carrying p.Arg627Gly showed spontaneous chromosomal instability in a 2021 study. [88]

---

## 5. Environmental, lifestyle, and infectious information

| Domain | Current evidence |
|---|---|
| Toxins/radiation/pollution | No demonstrated causal exposure |
| Smoking | No disease-specific data; avoidance is strongly advisable because pulmonary fibrosis is a major complication |
| Diet | Does not prevent disease; calorie/protein support and fat-soluble vitamins may be needed when pancreatic insufficiency is present |
| Exercise | No preventive trial; supervised stretching and low-impact activity may preserve function, whereas excessive loading of severely weak muscles should be avoided |
| Alcohol | No POIKTMP-specific study; minimizing alcohol is prudent with liver disease |
| UV exposure | Can exacerbate erythema/photosensitive skin findings; photoprotection is symptom-directed |
| Infection | No pathogen causes POIKTMP. Bacterial respiratory infections can precipitate decompensation in fibrotic or restrictive lung disease |
| Zoonosis/transmission | Not infectious and not zoonotic |

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **A heterozygous pathogenic *FAM111B* variant leads to** alteration of a nuclear trypsin-like serine protease, usually near its regulatory/protease-domain region.
2. **Loss of normal autoinhibitory control leads to** excessive or mistimed protease activity—demonstrated in transfected cells for disease-associated mutants, particularly p.Ser628Asn. [44]
3. **Hyperactive proteolysis leads to** displacement or degradation of factors required for DNA replication and transcription and to microtubule disruption; the direct physiological substrates remain partly inferred.
4. **Replication/transcriptional stress leads to** caspase-dependent apoptosis and reduced cellular fitness in vitro.
5. **FAM111B dysfunction also leads to** abnormal nuclear-envelope localization, impaired recruitment of TRF2 to telomeres, shortened/fragile telomeres, micronuclei, ultrafine DNA bridges, and chromosome fusions in cell models. PMID: **37342232**. [95][97]
6. **Repeated injury or loss of susceptible cells is inferred to lead to** abnormal tissue repair, extracellular-matrix deposition, fibrosis, and fatty replacement.
7. **In skin, this leads to** epidermal atrophy, collagen sclerosis, elastic-fiber fragmentation, telangiectasia, and pigmentary abnormalities—clinically poikiloderma.
8. **In skeletal muscle and tendons, this leads to** fibrofatty muscle replacement, progressive weakness, tendon shortening, contractures, and gait loss.
9. **In lung, the process branches:**
   - **respiratory-muscle involvement leads to** restrictive ventilatory impairment;
   - **interstitial injury and fibrosis lead to** reduced DLCO, progressive dyspnea, and potentially fatal respiratory failure.
10. **In pancreas and liver, fibrofatty injury leads to** exocrine pancreatic insufficiency and variable cholangiopathic, steatotic, fibrotic, or cirrhotic liver disease.

Steps 1–5 have genetic and cell-biological support; the direct bridge from protease hyperactivity/telomere dysfunction to organ-specific fibrosis remains **inferred**, not fully demonstrated.

### 6.2 Molecular pathways and cellular processes

| Mechanism | Evidence and interpretation | Suggested GO terms |
|---|---|---|
| Serine-protease hyperactivity | Patient mutants have increased autocleavage and protease-dependent toxicity in U2OS cells | Serine-type endopeptidase activity **GO:0004252**; proteolysis **GO:0006508** |
| DNA-replication suppression | Mutant expression reduced EdU incorporation and displaced RFC1/PCNA | DNA replication **GO:0006260**; regulation of DNA replication **GO:0006275** |
| Transcriptional suppression | Mutants reduced EU incorporation and displaced RPB1 | DNA-templated transcription **GO:0006351** |
| Apoptosis | Mutant toxicity was caspase-dependent | Apoptotic process **GO:0006915**; execution phase of apoptosis **GO:0097194** |
| Microtubule disorganization | Mutant phenotypes required catalytic activity | Microtubule cytoskeleton organization **GO:0000226** |
| Nuclear-pore association | FAM111B interacts with nuclear-pore components and disease mutants accumulate at the nuclear periphery | Nucleocytoplasmic transport **GO:0006913** |
| Telomere maintenance | FAM111B loss or a disease-associated mutant reduced telomeric DNA/TRF2 recruitment and increased fusions | Telomere maintenance **GO:0000723**; chromosome organization **GO:0051276** |
| Genome instability | Micronuclei, mitotic DNA synthesis and ultrafine bridges were increased in knockout cells | DNA-damage response **GO:0006974**; mitotic chromosome segregation **GO:0000070** |
| Fibrosis/ECM remodeling | Strong human pathology evidence but incomplete molecular bridge; later expression studies implicate TGF-β, PDGF, integrin, matrix metalloproteinase, and CCN2 networks | ECM organization **GO:0030198**; collagen fibril organization **GO:0030199**; tissue remodeling **GO:0048771** |

The 2023 telomere study used FAM111B-deficient U2OS and MCF7 cells and concluded:

> “Loss of FAM111B expression resulted in abnormal nuclear shape and reduced telomeric DNA content…” — Kliszczak et al., 2023, PMID: **37342232**, published June 5, 2023. [95]

### 6.3 Cell types and tissues

Likely relevant cells include:

- keratinocytes — **CL:0000312**;
- dermal fibroblasts — **CL:0002551**;
- skeletal muscle cells/myocytes — **CL:0000188**;
- tendon fibroblasts/tenocytes — use fibroblast plus tendon context where no preferred specific CL term is adopted;
- alveolar epithelial cells — **CL:0002062**;
- lung fibroblasts — **CL:0002553**;
- pancreatic acinar cells — **CL:0000622**;
- hepatocytes — **CL:0000182**;
- cholangiocytes — **CL:0000064**;
- adipocytes — **CL:0000136**.

Direct patient-cell mechanistic proof is strongest for muscle/skin pathology and weakest for precise lineage-specific initiation of fibrosis.

### 6.4 Immune, metabolic, and biochemical changes

- Inflammation is usually not the dominant muscle-biopsy feature; most biopsies show fibrofatty replacement without substantial necrosis or inflammation.
- Organizing pneumonia and inflammatory interstitial lesions may coexist with fibrosis and can be steroid responsive in individual patients.
- No primary enzyme deficiency, metabolomic signature, lipidomic signature, or circulating disease-specific biomarker has been validated.
- Pancreatic acinar loss causes secondary malabsorption and fat-soluble vitamin deficiency.
- No disease-specific single-cell, spatial-transcriptomic, organoid, or integrated multi-omics atlas was identified through 2024.

---

## 7. Anatomical structures affected

| Level | Structures and effects | Suggested ontology |
|---|---|---|
| Primary organs | Skin, skeletal muscle/tendons, lung | Skin **UBERON:0002097**; skeletal muscle organ **UBERON:0001630**; tendon **UBERON:0000043**; lung **UBERON:0002048** |
| Secondary organs | Pancreas, liver, lymphatic system, eye, esophagus; occasionally kidney, thyroid, myocardium, testis | Pancreas **UBERON:0001264**; liver **UBERON:0002107**; eye **UBERON:0000970**; kidney **UBERON:0002113** |
| Skin tissues | Epidermis and dermis; collagen and elastic-fiber network | Epidermis **UBERON:0001003**; dermis **UBERON:0002067** |
| Musculoskeletal sites | Triceps surae/Achilles tendon most characteristic; quadriceps, paraspinal, abdominal, upper-limb and neck musculature may be affected | Achilles tendon; skeletal muscle tissue **UBERON:0001134** |
| Lung tissue | Interstitium and parenchyma; upper-lobe-predominant disease in one adult is not established as a universal pattern | Lung parenchyma |
| Subcellular | Nucleus, nuclear envelope, nuclear pore complex, chromatin, telomere, microtubule cytoskeleton | Nucleus **GO:0005634**; nuclear envelope **GO:0005635**; nuclear pore **GO:0005643**; telomere **GO:0000781**; microtubule cytoskeleton **GO:0015630** |
| Lateralization | Generally bilateral or diffuse; contractures and weakness can be asymmetric in individual patients | No characteristic lateralization |

Autopsy of a Japanese adult showed fibrosis or fatty degeneration in lung, liver, kidney, skeletal muscle, heart, pancreas, and thyroid, supporting a systemic fibrofatty process. PMID: **35601499**. [6]

---

## 8. Temporal development and natural history

| Stage | Typical findings |
|---|---|
| Infancy, often first 6 months | Facial/photodistributed erythema and poikiloderma, sparse hair/eyebrows, hypohidrosis, eczematous lesions; growth or liver abnormalities may begin |
| Early childhood | Lymphedema, Achilles/triceps-surae shortening, toe walking, lower-limb deformity; myopathy can begin as early as infancy |
| Later childhood/adolescence | Progressive proximal/distal and sometimes axial weakness, fibrofatty change on MRI, scoliosis, dysphagia, pancreatic insufficiency |
| Second decade onward | Restrictive pulmonary physiology may emerge or worsen; pulmonary fibrosis becomes increasingly important |
| Adulthood | Progressive myopathy, loss of mobility, interstitial pulmonary fibrosis, liver or pancreatic complications; potentially premature death |

The course is chronic and lifelong. Skin changes may stabilize or become less conspicuous, while muscle, pulmonary, pancreatic, and liver manifestations become more prominent. A 2023 review of 34 previously published cases emphasized “marked age-dependent clinical expressivity.” PMID: **36102338**. [35]

There is no recognized spontaneous remission. A crucial intervention window is likely **before irreversible fibrofatty replacement or pulmonary fibrosis**, although no disease-modifying treatment has yet proved this concept.

---

## 9. Inheritance and population

### 9.1 Epidemiology

- The syndrome is ultra-rare.
- No population-based prevalence or incidence estimate is available.
- Approximately 30 cases had been reported by 2022, 36 by a 2023 case report, 37 in a 2022 review, and 39 in a 2024 review; these are literature counts, not epidemiological estimates. [58][82][75][39]
- It has been reported in people with European, South African European-descent, Algerian, Moroccan, Italian, Irish, Dominican, Chinese, Mexican, Japanese, and other backgrounds.
- There is no established ethnic or geographic restriction.
- The principal 15-patient series contained 9 males and 6 females, insufficient to infer a sex difference. [16]

### 9.2 Genetic counseling characteristics

| Characteristic | Current conclusion |
|---|---|
| Inheritance | Autosomal dominant |
| De novo disease | Common, approximately half of reported molecularly confirmed cases in one summary |
| Penetrance | Appears high for characteristic early skin disease among classic variants, but exact age-specific penetrance is unknown |
| Expressivity | Highly variable and age-dependent |
| Anticipation | Not demonstrated |
| Germline mosaicism | Not reported as confirmed; low residual recurrence risk should still be discussed after an apparently de novo case |
| Founder effect | No proven population-wide founder variant; p.Tyr621Asp segregated in the original South African family |
| Consanguinity | Not etiologically required; occurrence in consanguineous families does not alter dominant inheritance |
| Carrier frequency | Unknown and expected to be extremely low |
| Sex bias | None established |
| Reproductive risk | 50% per pregnancy for an affected heterozygous parent |

The original discovery involved three variants in five kindreds of different ethnic backgrounds; p.Arg627Gly was independently recurrent, arguing against a single founder explanation. PMID: **24268661**. [5]

---

## 10. Diagnostics

### 10.1 Clinical suspicion

Suspect POIKTMP in a child with:

- poikiloderma beginning in infancy, particularly facial or photodistributed;
- hypotrichosis, sparse eyebrows/eyelashes;
- hypohidrosis or heat intolerance;
- Achilles/triceps-surae or multiple contractures;
- progressive weakness or fibrofatty muscle MRI abnormalities;
- unexplained restrictive physiology, pancreatic insufficiency, or liver disease.

There are no internationally standardized point-based diagnostic criteria. Molecular confirmation is strongly recommended.

### 10.2 Recommended evaluation

| Domain | Test and characteristic findings |
|---|---|
| Dermatology | Full skin/hair/nail examination; photographs; assess sweating, heat intolerance and lymphedema |
| Skin biopsy | Epidermal atrophy, collagen sclerosis, fragmented/enlarged elastic fibers and elastotic globules; supportive but not specific |
| Neuromuscular | Strength testing, contracture measurements, gait assessment, CK, EMG, muscle MRI |
| Muscle MRI | Atrophy and fatty infiltration; reported pattern includes vastus-lateralis/anterior-thigh involvement with relative posterior-thigh sparing |
| Muscle biopsy | Fibroadipose replacement, atrophic/heterogeneous fibers and central nuclei; usually little inflammation or necrosis |
| Pulmonary | Baseline and serial spirometry/FVC, lung volumes, DLCO, oxygen saturation; respiratory-muscle measurements where possible |
| Chest imaging | High-resolution CT if symptoms, abnormal PFTs, or concern for interstitial disease; avoid unnecessary radiation in children |
| Pancreatic/nutritional | Fecal elastase, stool fat if indicated, weight/BMI, albumin, vitamins A/D/E/K, coagulation/INR |
| Liver | AST, ALT, ALP, GGT, bilirubin, albumin, INR; ultrasound/elastography; hepatology assessment |
| Cardiac | Clinical examination and echocardiography if symptoms or multisystem disease; routine disease-specific interval is undefined |
| Ophthalmic/audiologic | Baseline and symptom-directed assessments |
| Bone health | Vitamin D, calcium/phosphate, DXA when malnutrition, delayed puberty, fractures, or chronic steroids are relevant |

PFT surveillance should include vital capacity and DLCO because severe abnormalities may precede obvious radiographic fibrosis. [16]

### 10.3 Genetic testing strategy

1. **First-line:** sequence *FAM111B* with deletion/duplication analysis, preferably as part of a validated poikiloderma/genodermatosis or interstitial-lung-disease panel.
2. **WES:** appropriate when the phenotype is atypical or panel testing is negative; WES discovered the gene and continues to identify de novo variants.
3. **WGS:** useful after nondiagnostic panel/WES for poorly covered exons, regulatory variants, mosaicism, or structural changes, although no recurrent structural mechanism is established.
4. **Sanger sequencing:** suitable for targeted familial testing and confirmation.
5. **CMA, karyotype, FISH, mitochondrial DNA, and repeat-expansion testing:** not routine unless additional features suggest another diagnosis.
6. **RNA sequencing:** potentially useful for suspected splice variants but not a validated standard diagnostic assay.

A listed commercial single-gene assay reports analytical sensitivity >98%, specificity 96%, and accuracy 97%; laboratory-specific validation should be reviewed before use. [43]

### 10.4 Variant interpretation

Interpretation should incorporate:

- phenotype specificity;
- de novo status or segregation;
- absence/rarity in gnomAD;
- clustering near known pathogenic residues;
- conservation and computational predictions;
- functional evidence of altered protease activity where available.

A VUS should not be used alone for predictive testing or irreversible decisions.

### 10.5 Differential diagnosis

| Differential | Distinguishing features |
|---|---|
| Rothmund–Thomson syndrome, *RECQL4* | Poikiloderma and sparse hair but recessive inheritance; skeletal anomalies, juvenile cataracts or osteosarcoma risk; lacks characteristic dominant *FAM111B* fibrofatty myopathy pattern |
| Poikiloderma with neutropenia, *USB1* | Chronic neutropenia, recurrent infections, nail dystrophy and palmoplantar hyperkeratosis |
| Clericuzio-type poikiloderma with neutropenia | Neutropenia is central; recessive inheritance |
| Dyskeratosis congenita/telomere biology disorders | Nail dystrophy, reticulate pigmentation, oral leukoplakia, marrow failure; telomere defects but different phenotype |
| Weary hereditary sclerosing poikiloderma | Historically overlapping terminology; cardiac involvement and absence of the molecularly defined POIKTMP constellation may distinguish |
| Kindler epidermolysis bullosa | Acral blistering, photosensitivity and progressive poikiloderma; *FERMT1* |
| Werner syndrome | Adolescent/adult premature aging, cataracts, diabetes and atherosclerosis |
| Systemic sclerosis | Usually acquired autoimmune disease, Raynaud phenomenon and autoantibodies; lacks infantile poikiloderma and dominant congenital pattern |
| Muscular dystrophies/contractural myopathies | Weakness and contractures without characteristic infantile poikiloderma |
| Other monogenic interstitial lung diseases | Pulmonary fibrosis without the characteristic skin, hair, tendon and muscle pattern |

### 10.6 Screening

- Not included in newborn screening.
- Cascade testing is appropriate for relatives of a molecularly confirmed patient.
- Predictive testing of asymptomatic minors may be justified because surveillance begins in childhood.
- Prenatal diagnosis and preimplantation genetic testing are technically feasible once the familial pathogenic variant is known.

---

## 11. Outcome and prognosis

### 11.1 Survival

No 5-year, 10-year, or median-survival estimates exist. In the main cohort, three individuals died at ages **30, 40, and 56**; two died only **3–4 years after onset of respiratory symptoms**. [16] GARD similarly notes that progressive interstitial pulmonary fibrosis can become life-threatening within three to four years after respiratory symptoms appear. [1]

These observations indicate serious risk but cannot be converted into a population mortality rate.

### 11.2 Major morbidity

- progressive loss of walking, transfers, stair climbing and self-care;
- fixed tendon contractures and skeletal deformity;
- restrictive ventilatory impairment;
- pulmonary fibrosis and respiratory failure;
- dysphagia and aspiration risk;
- pancreatic malabsorption and vitamin deficiency;
- chronic liver disease, portal hypertension, cirrhosis, and hepatic failure;
- lymphedema and cellulitis;
- heat intolerance and reduced outdoor activity.

### 11.3 Prognostic factors

Probable adverse factors include:

- declining FVC or DLCO;
- radiographic pulmonary fibrosis;
- respiratory-muscle weakness;
- rapidly progressive muscle fatty replacement;
- dysphagia or severe low BMI;
- pancreatic insufficiency without adequate replacement;
- progressive liver fibrosis, impaired synthetic function, or portal hypertension;
- recurrent respiratory infections.

No molecular, circulating, or imaging biomarker has been prospectively validated for survival prediction. Genotype–phenotype correlations remain preliminary; some reports suggest variants in the cluster near residues 621–629 produce more severe multisystem disease, but cohort size is inadequate for deterministic counseling.

---

## 12. Treatment

### 12.1 General principles

There is **no approved disease-modifying, gene, RNA, cell, or targeted protease therapy** for POIKTMP. Management is multidisciplinary and complication-directed.

| Intervention | Indication/evidence | Important risks or limitations | Suggested NCIt concept |
|---|---|---|---|
| Photoprotection, emollients | Photosensitive erythema, xerosis, dermatitis | Does not prevent systemic progression | Sun protection; topical therapy |
| Topical corticosteroid | Eczematous inflammatory lesions; individual benefit reported | Skin atrophy with prolonged potent use | Corticosteroid therapy **NCIT:C15447** |
| Physiotherapy/stretching | Maintain range of motion, posture, mobility and respiratory conditioning | Avoid overwork in severe myopathy | Physical therapy **NCIT:C15301** |
| Occupational therapy/assistive devices | Reduced hand function and activities of daily living | Individualized | Occupational therapy |
| Orthoses | Ankle positioning and prevention of secondary deformity | Pressure injury, tolerance | Orthopedic device |
| Achilles tendon lengthening | Severe fixed equinus/contracture; five patients underwent surgery, and one regained walking | Recurrence, weakness, operative risk | Tendon lengthening procedure |
| Pancreatic enzyme replacement | Steatorrhea/exocrine pancreatic insufficiency; symptoms normalized in reported patients | Dose adjustment and adherence | Pancrelipase therapy |
| Vitamin A/D/E/K replacement | Documented deficiency or malabsorption | Monitor toxicity, especially vitamins A/D | Vitamin supplementation |
| Nutritional support/enteral feeding | Low BMI, failure to thrive, dysphagia | Aspiration and tube-related complications | Nutritional support |
| Non-invasive ventilation | Nocturnal hypoventilation or severe respiratory-muscle restriction | Mask tolerance and secretion management | Noninvasive ventilation |
| Oxygen | Documented hypoxemia | Does not correct hypoventilation; monitor carefully | Oxygen therapy **NCIT:C94624** |
| Vaccination and rapid infection treatment | Limited pulmonary reserve | Standard contraindications only | Vaccination |
| Lymphedema care | Compression, skin care, cellulitis prevention | Fit and tolerance | Compression therapy |
| Prednisolone | One adult with organizing/unclassifiable interstitial pneumonia improved after 40 mg/day for two weeks | Not established for fixed fibrosis; infection, osteoporosis, muscle and metabolic toxicity | Prednisone/prednisolone therapy |
| Liver-directed care | Cholestasis, portal hypertension, encephalopathy, cirrhosis | Disease-specific efficacy unknown | Supportive care |
| Palliative/supportive care | Advanced respiratory, hepatic or neuromuscular disease | Should accompany rather than replace active care | Palliative care **NCIT:C15292** |

In the steroid-responsive adult, %DLCO improved from **42.6% to 54.5%**, %VC from **45.7% to 49.5%**, and CT shadows improved after two weeks; autopsy showed organizing pneumonia superimposed on fibrosis. This is single-patient evidence and does not establish corticosteroids as routine antifibrotic treatment. PMID: **35601499**. [6]

### 12.2 Suggested clinical pathway

1. Confirm the molecular diagnosis.
2. Establish baseline skin, neuromuscular, pulmonary, pancreatic/nutritional, liver, ophthalmic, and functional status.
3. Repeat PFTs and functional evaluations at least annually, more frequently with symptoms or decline.
4. Treat malabsorption, deficiencies, dermatitis, lymphedema, and infections early.
5. Use daily stretching, orthoses, mobility aids, and carefully selected contracture surgery.
6. Obtain HRCT and ILD-specialist review when PFTs decline or respiratory symptoms emerge.
7. Distinguish active inflammatory/organizing pneumonia from established fibrosis before immunosuppression.
8. Introduce ventilatory, nutritional, and palliative support according to need.

### 12.3 Experimental approaches

The strongest experimental rationale is **selective inhibition of mutant FAM111B protease activity**, because catalytic inactivation rescued mutant cellular toxicity. The 2023 clinical review proposed specific catalytic inhibition as a future strategy but emphasized that such treatment does not yet exist. PMID: **36102338**. [35]

No completed interventional trial, NCT-listed POIKTMP-specific gene therapy, CRISPR therapy, antisense therapy, or approved FAM111B inhibitor was identified. Broad antifibrotics such as nintedanib or pirfenidone have not been specifically evaluated in POIKTMP.

---

## 13. Prevention

### 13.1 Primary prevention

The occurrence of a de novo pathogenic variant cannot currently be prevented. For known familial disease:

- preconception genetic counseling;
- preimplantation genetic testing for monogenic disease;
- chorionic-villus or amniotic-fluid prenatal diagnosis;
- donor gametes or other reproductive options.

### 13.2 Secondary prevention

Early molecular diagnosis permits surveillance before irreversible complications:

- serial lung function;
- early muscle MRI and functional assessment;
- pancreatic screening in underweight patients or those with diarrhea;
- liver chemistry and fibrosis assessment;
- nutritional and vitamin monitoring;
- cascade testing of at-risk relatives.

### 13.3 Tertiary prevention

- sun and heat precautions;
- smoking avoidance;
- influenza, COVID-19, pneumococcal, and other age-appropriate immunizations;
- respiratory infection prevention and prompt treatment;
- stretching, orthoses and mobility support;
- aspiration assessment;
- pancreatic enzymes and vitamin replacement;
- lymphedema skin care and cellulitis prevention;
- avoidance of unnecessary pulmonary toxins and potentially hepatotoxic exposures.

No vaccine prevents the genetic disease, and there is no population screening program.

---

## 14. Other species and natural disease

| Topic | Finding |
|---|---|
| Naturally occurring veterinary POIKTMP | No well-validated spontaneous *FAM111B*-associated POIKTMP analogue was identified in OMIA or the veterinary literature |
| Human taxonomy | *Homo sapiens*, NCBI Taxonomy **9606** |
| Orthologs | Conserved *Fam111b/FAM111B* orthologs occur in mouse, rat, zebrafish, and other vertebrates |
| Comparative mechanism | Protease-domain conservation supports cross-species functional study; the precise human combination of poikiloderma, contractures, myopathy, and adult fibrosis has not been established as a natural animal disease |
| Breed association | None known; no applicable VBO breed term |
| Zoonotic potential | None—the disorder is inherited, not transmissible |

Reports of *FAM111B* manipulation in tumor xenografts or viral studies are not natural animal POIKTMP and should not be annotated as such.

---

## 15. Model organisms and experimental systems

### 15.1 Established systems

| Model | Manipulation and phenotype | Application | Limitations |
|---|---|---|---|
| U2OS human osteosarcoma cells | Inducible wild-type or patient-mutant FAM111B; mutant protein suppresses DNA/RNA synthesis, disrupts microtubules and induces apoptosis | Protease mechanism and inhibitor screening | Cancer cell line; does not model differentiated skin, muscle or lung |
| FAM111B-knockout U2OS cells | Abnormal nuclei, micronuclei, ultrafine DNA bridges, reduced telomeric DNA and altered TRF2 recruitment | Nuclear-pore/telomere biology | Loss-of-function model may not fully reproduce dominant hypermorphic disease |
| MCF7 human cells | FAM111B-deficiency studies of nuclear shape and telomere maintenance | Independent cellular validation | Cancer-cell context |
| Recombinant protein/yeast expression | FAM111B autocleavage and serine-protease inhibition assays | Direct biochemical activity; compound screening | Lacks human tissue context |
| Patient skin and muscle biopsy | Sclerodermiform skin pathology and fibrofatty myopathy | Direct human pathological validation | Scarce samples; late-stage tissue does not reveal initiating events |
| Patient lymphocytes | Spontaneous chromosome instability reported in p.Arg627Gly carriers | Cancer/genome-instability hypothesis | Very small sample |
| Preliminary zebrafish and mouse expression models | Human mutant FAM111B reportedly produces a patient-like muscle phenotype in preliminary project data | In-vivo muscle mechanism and therapeutic testing | Not yet a mature, peer-reviewed natural-history model; systemic fibrosis recapitulation remains uncertain [67] |
| Planned rAAV-mutant mouse model | Systemic delivery of mutant FAM111B proposed | Test tissue mechanisms and candidate interventions | Induced overexpression may not reproduce endogenous dosage or development |

The disease field still lacks a widely validated knock-in model reproducing the complete human sequence of infantile skin disease, childhood contractures/myopathy, and adult pulmonary fibrosis.

### 15.2 Priority model-development needs

1. Endogenous heterozygous knock-in mice for recurrent variants such as p.Tyr621Asp, p.Arg627Gly, and p.Ser628Asn;
2. Patient-derived iPSC keratinocyte, myocyte, tenocyte, lung fibroblast, and pancreatic-acinar models;
3. Skin, muscle and lung organoids;
4. Longitudinal single-cell and spatial profiling of fibrosis;
5. Protease-substrate identification by degradomics;
6. Allele-selective suppression or selective protease-inhibitor screens.

---

## Recent developments, 2023–2024

| Publication date | Development | Significance |
|---|---|---|
| January 2023 | Review/case analysis of 34 previously reported cases, PMID **36102338** | Emphasized age-dependent expressivity, early multisystem imaging, and catalytic inhibition as a therapeutic concept [35] |
| February 17, 2023 | De novo c.1292T>C *FAM111B* case with pneumonitis and autoimmune-polyendocrine-like findings | Expanded phenotype and documented that roughly half of then-reported cases were de novo [82] |
| June 5, 2023 | Kliszczak et al., PMID **37342232** | Linked FAM111B to nuclear-pore components, TRF2 recruitment, telomere maintenance, abnormal nuclear shape, and genomic instability [95][97] |
| December 22, 2023 | Expert commentary on liver involvement | Highlighted possible relevance of telomere/nuclear-envelope biology to multisystem disease while noting that hepatic pathogenesis remains unresolved [92] |
| February 29, 2024 | Molecular review, PMID **38474092** | Integrated evidence for FAM111B in cell-cycle regulation, apoptosis, nuclear transport and telomere maintenance; counted 39 reported cases [32][39] |

---

## Overall expert assessment

POIKTMP is best understood as a **dominant protease-dysregulation disorder with age-progressive, multisystem fibrofatty tissue injury**. The causal relationship between heterozygous *FAM111B* variants and disease is strong. Protease hyperactivity, apoptosis, nuclear-envelope abnormalities, and impaired telomere maintenance are experimentally supported, but the exact cell-specific route to fibrosis remains unresolved.

The most immediately actionable clinical points are:

- recognize infantile poikiloderma plus hypotrichosis and contractures;
- confirm *FAM111B* molecularly;
- monitor pulmonary function even before symptoms;
- investigate pancreatic and liver disease proactively;
- preserve mobility and range of motion;
- distinguish potentially treatable inflammatory/organizing lung lesions from irreversible fibrosis;
- provide autosomal-dominant reproductive counseling.

The evidence base remains too small for reliable prevalence, survival, penetrance, response-rate, or genotype-specific prognosis estimates. Nevertheless, respiratory and hepatic surveillance is justified because documented complications can be rapidly progressive and fatal.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 16 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC11650971` (1 mention) - E2F3-dependent activation of FAM111B restricts mouse cytomegalovirus replication in primate cells.
  - shared terms: fam111b

Weighed against this report's own most characteristic terms: `disease`, `fibrosis`, `pulmonary`, `fam111b`, `pancreatic`, `skin`, `muscle`, `variant`, `contracture`, `patient`, `liver`, `respiratory`, `poikiloderma`, `lung`, `established`, `poiktmp`, `progressive`, `tendon`, `weakness`, `replacement`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 79 |
| Resolved | 76 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014310` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hereditary sclerosing poikiloderma with tendon and pulmonary involvement**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001006` (obsolete Hypotrichosis) (1 mention) - replaced by `HP:0008070`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.