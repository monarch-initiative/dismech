---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T23:23:57.020012'
end_time: '2026-09-04T23:39:29.499948'
duration_seconds: 932.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Multiple Osteochondromas
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 73
  verified: 62
  not_found: 0
  obsolete: 1
  unverifiable: 10
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: NCIT:C121924
    ontology_label: Enostosis
  unresolvable_prefixes:
  - Orphanet
  - OMIM
  - PMIDs
  - Taxon
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hereditary_Multiple_Osteochondromas-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Multiple Osteochondromas
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Multiple Osteochondromas** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Multiple Osteochondromas
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Multiple Osteochondromas** covering all of the
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


# Hereditary Multiple Osteochondromas: Disease Characteristics Research Report

**Scope.** This report synthesizes disease-level resources, human cohorts, molecular studies, clinical-trial records, and model-organism evidence. Evidence is aggregated rather than derived from an individual electronic health record, except where a cited study explicitly analyzed clinical records. Literature was prioritized through 2024; a 2025 imaging review is used only where it clarifies current diagnostic practice.

## Executive summary

Hereditary multiple osteochondromas (HMO), historically called hereditary multiple exostoses (HME), is a highly penetrant autosomal-dominant skeletal tumor-predisposition disorder. Multiple cartilage-capped osteochondromas arise near growth plates during childhood, enlarge during skeletal growth, and usually become quiescent after physeal closure. Heterozygous loss-of-function variants in **EXT1** or **EXT2**, encoding the Golgi heparan-sulfate polymerase complex, explain approximately 70–95% of clinically diagnosed cases. A local somatic second hit and severe focal heparan-sulfate deficiency are strongly supported as the initiating events in many osteochondromas. Clinical morbidity includes deformity, impaired growth, restricted motion, neurovascular compression, pain, fatigue, repeated surgery, and a small but important risk of secondary peripheral chondrosarcoma. There is no approved disease-modifying treatment; management remains surveillance, symptom-directed surgery, pain care, and rehabilitation. Recent 2024 work expanded the detectable variant spectrum, implicated mosaic structural variants and possible **PTPN11** overlap, quantified major adult pain/fatigue burden, and demonstrated palovarotene activity against established lesions in mice—but not established clinical benefit in HMO. (borovikov2024themissingpiece pages 1-2, gnoli2024secondaryperipheralchondrosarcoma pages 1-2, amajjar2024painandfatigue pages 1-2, garcia2024analysisofthe pages 1-2)

The following table provides a compact knowledge-base summary.

| Domain | Curated fact | Quantitative evidence | Suggested ontology IDs | Strongest source/date |
|---|---|---|---|---|
| Disease identity | Hereditary multiple osteochondromas (HMO), also called multiple osteochondromas, hereditary multiple exostoses, diaphyseal aclasis, and multiple cartilaginous exostoses, is a Mendelian skeletal disorder producing multiple cartilage-capped, corticomedullary-continuous bone outgrowths. | Diagnostic definition commonly requires ≥2 osteochondromas. | MONDO:0005508; Orphanet:321; OMIM:133700 and 133701 | Open Targets (OpenTargets Search: hereditary multiple osteochondromas-EXT1,EXT2); D’Arienzo et al., 20-Dec-2019, DOI:10.2147/ORR.S183979 (darienzo2019hereditarymultipleexostoses pages 1-2) |
| Causal genes | Heterozygous loss-of-function variants in **EXT1** or **EXT2** are the principal causes; their Golgi-resident glycosyltransferase complex polymerizes heparan sulfate. | EXT1/EXT2 variants explain approximately 70–95% of cases; earlier studies reported EXT1 in 28–65% and EXT2 in 21–61%. | HGNC:3512 (**EXT1**); HGNC:3513 (**EXT2**); GO:0000139, Golgi membrane; GO:0015012, heparan sulfate proteoglycan biosynthetic process | Open Targets (OpenTargets Search: hereditary multiple osteochondromas-EXT1,EXT2); PMID:10639137; PMID:11391482 (pacifici2018hereditarymultipleexostoses pages 7-9, pacifici2017hereditarymultipleexostoses pages 12-13) |
| Inheritance and prevalence | HMO is autosomal dominant with variable expressivity and nearly complete, partly sex-dependent penetrance. | Prevalence approximately 1:50,000 in Western populations; reported penetrance approximately 100% in males and 96% in females; recurrence risk for an affected heterozygous parent is 50% per pregnancy. | HP:0000006, autosomal dominant inheritance; HP:0003829, incomplete penetrance | D’Arienzo et al., 2019, DOI:10.2147/ORR.S183979 (darienzo2019hereditarymultipleexostoses pages 1-2) |
| Onset and course | Lesions are rarely apparent at birth, emerge in early childhood, enlarge while physes are open, and generally stop growing at skeletal maturity. | Median diagnosis approximately 3 years; visible lesion in 50% by age 5 and 80% by age 10; >80% present during the first decade. | HP:0011463, childhood onset; HP:0003674, onset in infancy | Tepelenis et al., Jan-2021, DOI:10.21873/invivo.12308 (tepelenis2021osteochondromasanupdated pages 1-2, tepelenis2021osteochondromasanupdated pages 2-3) |
| Core phenotype | Multiple sessile or pedunculated cartilage-capped osteochondromas arise mainly near growth plates and on surfaces of flat bones. | Mean reported burden approximately six lesions; common sites include distal femur 30%, proximal tibia 15–20%, and humerus 10–20%. | HP:0000934, multiple exostoses; HP:0030434, osteochondroma | Tepelenis et al., 2021, DOI:10.21873/invivo.12308 (tepelenis2021osteochondromasanupdated pages 1-2, tepelenis2021osteochondromasanupdated pages 2-3) |
| Musculoskeletal morbidity | Common consequences include short or disproportionate stature, limb bowing, forearm deformity, genu or ankle valgum, limb-length inequality, restricted joint motion, bursitis, and premature osteoarthritis. | In 158 children, 80.4% developed new lesions, 57.6% new deformities, and 23.4% new functional limitations; 46.2% showed progression. | HP:0004322, short stature; HP:0002970, genu valgum; HP:0001376, limitation of joint mobility; HP:0002814, abnormality of the lower limb | Mordenti et al., Oct-2020, DOI:10.1016/j.bone.2020.115499 (mordenti2020thenaturalhistory pages 1-6) |
| Pain, fatigue, and quality of life | Chronic mechanical pain and fatigue substantially impair physical, psychosocial, occupational, and social functioning in adults. | Among 353 adults, pain affected 87.8% (NRS 3.19±2.6) and fatigue 90.4% (NRS 4.1±2.6); CIS fatigue was 84.1±15.3 and exceeded healthy and rheumatoid-arthritis references (p<0.001). | HP:0012531, pain; HP:0012378, fatigue | Amajjar et al., 17-Jul-2024, DOI:10.1371/journal.pone.0305640 (amajjar2024painandfatigue pages 1-2) |
| Pathogenesis | Germline EXT haploinsufficiency lowers systemic heparan sulfate; a local somatic second hit can create EXT-null growth-plate or perichondrial cells, disrupting morphogen distribution and promoting ectopic chondrogenesis. | Human blood shows an approximately 50% reduction in the heparan-sulfate:chondroitin-sulfate ratio; loss of heterozygosity was found in 6 of 8 analyzed osteochondromas in one series. | GO:0030201, heparan sulfate proteoglycan metabolic process; GO:0061035, regulation of cartilage development; CL:0000138, chondrocyte | PMID:23514715; PMIDs:10441575, 17341731, 20813973 (pacifici2017hereditarymultipleexostoses pages 12-13, pacifici2017hereditarymultipleexostoses pages 10-12, pacifici2018hereditarymultipleexostoses pages 7-9) |
| Signaling consequences | Heparan-sulfate deficiency alters BMP, Indian hedgehog/PTHrP, FGF–MEK–ERK, and WNT/β-catenin signaling; increased pro-chondrogenic BMP/hedgehog activity and reduced anti-chondrogenic FGF signaling are chiefly supported by model systems. | No validated clinical pathway biomarker or disease-specific omics diagnostic is available. | GO:0030509, BMP signaling pathway; GO:0007224, smoothened signaling pathway; GO:0008543, fibroblast growth factor receptor signaling pathway; GO:0016055, Wnt signaling pathway | Pacifici, Jun-2018, DOI:10.1080/21678707.2018.1483232; PMID:23458899 (pacifici2018hereditarymultipleexostoses pages 12-13, pacifici2018hereditarymultipleexostoses pages 7-9) |
| Diagnosis | Diagnosis is clinical-radiographic: multiple lesions with continuity of lesion cortex and medulla with the parent bone. Radiography is first line; CT defines complex anatomy, and MRI evaluates cartilage caps, neurovascular or spinal complications, and malignancy. | Suspicious findings include new pain or growth after maturity and cartilage-cap thickness >2 cm in adults or >3 cm in children. | HP:0000934; NCIT:C38101, radiography; NCIT:C16809, magnetic resonance imaging; NCIT:C17204, computed tomography | Tepelenis et al., 2021, DOI:10.21873/invivo.12308 (tepelenis2021osteochondromasanupdated pages 1-2, tepelenis2021osteochondromasanupdated pages 7-8) |
| Genetic testing | Recommended testing begins with sequencing of **EXT1** and **EXT2**, followed by deletion/duplication analysis; unresolved cases may require genome or RNA analysis for mosaic, deep-intronic, or structural variants. **PTPN11** analysis is relevant when metachondromatosis or an overlapping phenotype is suspected. | Conventional EXT testing yields approximately 78–95%; 10–20% can remain unresolved after coding-region and copy-number analysis. | NCIT:C101293, genetic testing; NCIT:C18477, molecular diagnostic testing | Borovikov et al., Feb-2024, DOI:10.1155/2024/8849348 (borovikov2024themissingpiece pages 1-2) |
| Malignant transformation | The principal life-threatening complication is secondary peripheral chondrosarcoma arising from an osteochondroma cartilage cap; estimates vary by ascertainment, so specialist-center percentages should not be generalized. | Population-oriented estimates are approximately 0.5–5% or up to 3.9%. In 105 affected cases, median diagnosis was 34 years; pelvis accounted for 44%, and grade 2/3 disease or partial resection predicted worse disease-free survival. | NCIT:C121924, secondary peripheral chondrosarcoma; HP:0002664, neoplasm | Gnoli et al., Feb-2024, DOI:10.1186/s13023-023-03006-8 (gnoli2024secondaryperipheralchondrosarcoma pages 1-2) |
| Management | No approved disease-modifying therapy exists for HMO. Asymptomatic lesions are observed; surgery is used for pain, deformity, functional or neurovascular compromise, fracture, or suspected malignancy. Procedures include complete excision, corrective osteotomy, hemiepiphysiodesis, and limb lengthening. | Complete excision has reported recurrence below 2%; postoperative complications approximately 11.6–12.5%. Evidence that forearm reconstruction improves long-term function or quality of life remains weak. | NCIT:C15329, surgical procedure; NCIT:C52003, excision; NCIT:C51932, osteotomy; NCIT:C15214, rehabilitation | Tepelenis et al., 2021, DOI:10.21873/invivo.12308 (tepelenis2021osteochondromasanupdated pages 7-8); Beltrami et al., May-2016, DOI:10.11138/ccmbm/2016.13.2.110 (beltrami2016hereditarymultipleexostoses pages 7-8) |
| Recent genetics | A 2024 cohort expanded the recognized genetic overlap with metachondromatosis and showed that restricting testing to EXT1/EXT2 may miss relevant diagnoses. | Among 244 unrelated probands, 177 unique variants were detected across three genes—80 known and 97 novel; five osteochondroma-only cases carried **PTPN11** loss-of-function variants. | HGNC:9644 (**PTPN11**); MONDO:0008162, metachondromatosis | Borovikov et al., Feb-2024, DOI:10.1155/2024/8849348 (borovikov2024themissingpiece pages 1-2) |
| Experimental therapy | The RARγ agonist palovarotene suppresses osteochondroma growth in mice but is not approved for HMO; pediatric safety concern centers on premature physeal closure. | In mice, treated tumors remained 0.31±0.049 mm³ versus 0.27±0.031 mm³ initially (p=0.66), while controls reached 1.03±0.23 mm³; phase 2 HMO trial NCT03442985 was terminated. | CHEBI:177944, palovarotene; NCIT:C96038, retinoic acid receptor gamma agonist | Garcia et al., 11-Jul-2024, DOI:10.3390/ijms25147610 (garcia2024analysisofthe pages 1-2); ClinicalTrials.gov NCT03442985 (NCT03442985 chunk 2) |
| Models | Conditional or clonal chondrocyte **Ext1** loss, compound **Ext1/Ext2** deficiency, and **ext2**-null zebrafish reproduce aspects of abnormal endochondral ossification and osteochondroma biology. Models strongly support the second-hit/low-heparan-sulfate mechanism but do not capture the full variable human phenotype. | Single heterozygous mice are largely normal; conditional biallelic or compound deficiency produces multiple lesions. | NCBI Taxon:10090, *Mus musculus*; NCBI Taxon:7955, *Danio rerio*; CL:0000138, chondrocyte | PMIDs:20080592, 20534475, 21310272, 16236767 (pacifici2017hereditarymultipleexostoses pages 12-13, pacifici2018hereditarymultipleexostoses pages 7-9, pacifici2017hereditarymultipleexostoses pages 1-2) |
| Research infrastructure | Longitudinal registries integrate clinical, imaging, genetic, surgical, biospecimen, and quality-of-life data to define natural history and genotype–phenotype associations. | Italian REM registry NCT04133285 plans enrollment of 10,000 and follow-up through 2032. | NCIT:C61393, patient registry; NCIT:C15273, longitudinal study | ClinicalTrials.gov NCT04133285, updated Nov-2025 (NCT04133285 chunk 1) |


*Table: Compact evidence table summarizing the identity, genetics, natural history, clinical burden, diagnosis, management, recent findings, and experimental models of hereditary multiple osteochondromas. Quantitative findings and ontology suggestions are paired with the strongest available cited sources.*

## 1. Disease information

### Definition and identifiers

HMO is defined by multiple benign, cartilage-capped bony outgrowths with cortical and medullary continuity with the parent bone. A commonly used clinical/radiologic threshold is at least two juxta-epiphyseal osteochondromas. The lesions are developmental skeletal neoplasms rather than inflammatory “exostoses.” (mordenti2020thenaturalhistory pages 1-6, tepelenis2021osteochondromasanupdated pages 1-2, ruedadeeusebio2025hereditarymultipleexostoses pages 1-2)

* **MONDO:** MONDO:0005508, hereditary multiple osteochondromas.
* **Orphanet:** ORPHA:321, multiple osteochondromas.
* **OMIM phenotypes:** 133700, exostoses, multiple, type 1; 133701, type 2.
* **MeSH:** Multiple Hereditary Exostoses.
* **ICD:** ICD-10-CM commonly uses **D16.9** (benign neoplasm of bone and articular cartilage, unspecified) or site-specific D16 codes; **Q78.6** is used in some national modifications for multiple congenital exostoses. Coding therefore depends on jurisdiction and should not be treated as a globally uniform disease identifier.
* **Synonyms:** hereditary multiple exostoses, multiple hereditary exostoses, multiple osteochondromas, hereditary multiple osteochondromas, osteochondromatosis, diaphyseal aclasis, hereditary deforming dyschondroplasia, and multiple cartilaginous exostoses. (OpenTargets Search: hereditary multiple osteochondromas-EXT1,EXT2, darienzo2019hereditarymultipleexostoses pages 1-2)

A concise abstract statement is: **“Hereditary multiple exostoses (HME), also called hereditary multiple osteochondromas, is a rare genetic disorder characterized by multiple osteochondromas that grow near the growth plates.”** (D’Arienzo et al., published 20 December 2019; DOI: https://doi.org/10.2147/ORR.S183979). (darienzo2019hereditarymultipleexostoses pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal and genetic factors

The primary cause is a germline heterozygous loss-of-function variant in **EXT1** or **EXT2**. Both are strongly supported disease targets in Open Targets; EXT1 is ENSG00000182197 and EXT2 is ENSG00000151348. In individual lesions, loss of the remaining functional allele or another somatic event can create an EXT-null clone. Human tumor series have documented loss of heterozygosity, although lesion heterogeneity can obscure it. (OpenTargets Search: hereditary multiple osteochondromas-EXT1,EXT2, pacifici2017hereditarymultipleexostoses pages 12-13, pacifici2017hereditarymultipleexostoses pages 10-12, pacifici2017hereditarymultipleexostoses pages 1-2)

Risk of having HMO is determined principally by carrying a pathogenic germline allele or having an affected parent. **EXT1** disease is generally associated with a greater lesion burden, more severe deformity, and possibly greater malignancy risk than **EXT2**, but marked intra- and interfamilial variability limits individual prediction. Age and skeletal immaturity increase the probability of new lesion formation because lesions arise during active endochondral growth; these are modifiers of expression, not independent causes. (mordenti2020thenaturalhistory pages 1-6, tepelenis2021osteochondromasanupdated pages 2-3, pacifici2017hereditarymultipleexostoses pages 6-7)

### Environmental, lifestyle, infectious, and protective factors

No toxin, infection, diet, smoking behavior, occupational exposure, or lifestyle factor is established as a cause of this Mendelian disorder. No validated environmental or genetic protective allele prevents HMO in a pathogenic-variant carrier. Avoiding mechanical irritation may reduce lesion-related symptoms, but it does not prevent osteochondroma initiation. Evidence for clinically important gene–environment interactions is insufficient.

A human biochemical study found a modest effect of EXT1 heterozygosity on postprandial lipid clearance (PMID: **25568062**), but this is not evidence that diet causes or protects against HMO. Likewise, the approximately halved heparan-sulfate:chondroitin-sulfate ratio in blood is a consequence of EXT dysfunction, not an exposure biomarker (PMID: **23514715**). (pacifici2018hereditarymultipleexostoses pages 7-9, pacifici2017hereditarymultipleexostoses pages 12-13)

## 3. Phenotypes

### Core and associated manifestations

| Phenotype and type | Typical characteristics | Frequency/effect | Suggested HPO term |
|---|---|---|---|
| Multiple osteochondromas; physical sign | Rarely evident at birth; childhood onset; increase until skeletal maturity | Defining feature; mean reported burden about six lesions | HP:0000934 Multiple exostoses; HP:0030434 Osteochondroma |
| Palpable bony masses; sign | Usually painless initially; metaphyseal/juxtaphyseal | 50% visible by age 5; 80% by age 10 | HP:0000924 Abnormality of the skeletal system |
| Short/disproportionate stature; sign | Variable; reflects disturbed physeal growth | Qualitatively common | HP:0004322 Short stature; HP:0003508 Proportionate short stature where appropriate |
| Limb bowing/valgus and length inequality; sign | Progressive during growth; forearm, knee, and ankle prominent | New deformity in 57.6% of one pediatric cohort | HP:0002970 Genu valgum; HP:0003027 Mesomelia; HP:0002814 Abnormality of lower limb |
| Restricted range of motion; sign/function | Mechanical impingement or deformity; variable | New functional limitations in 23.4% of 158 children | HP:0001376 Limitation of joint mobility |
| Pain; symptom | Mechanical pressure, bursitis, fracture, osteoarthritis, nerve compression, or malignancy | 87.8% of 353 adults; NRS 3.19±2.6 | HP:0012531 Pain |
| Fatigue; symptom | Chronic and strongly associated with psychological factors and pain | 90.4%; NRS 4.1±2.6; CIS 84.1±15.3 | HP:0012378 Fatigue |
| Neurovascular compression; complication | Focal neuropathy, vessel displacement, pseudoaneurysm, or rare cord compression | Uncommon but potentially severe | HP:0003477 Peripheral axonal neuropathy or site-specific term; HP:0002176 Spinal cord compression |
| Scoliosis/axial deformity; sign | Usually growth-associated | Variable | HP:0002650 Scoliosis |
| Bursitis/fracture/early osteoarthritis; complication | Mechanical sequelae | Variable | HP:0003045 Abnormality of the synovium; HP:0002757 Recurrent fractures if applicable; HP:0002758 Osteoarthritis |
| Secondary peripheral chondrosarcoma; neoplasm | Usually adult, but pediatric cases occur | Estimated approximately 0.5–5%; ascertainment-dependent | HP:0002664 Neoplasm |

In the 158-child natural-history cohort, 80.4% developed new lesions, 57.6% new deformities, 23.4% new functional limitations, and 46.2% met criteria for progression; new lesions appeared in 28.5%, 39.9%, and 50% by 12, 24, and 36 months, respectively. (Mordenti et al., October 2020; DOI: https://doi.org/10.1016/j.bone.2020.115499). (mordenti2020thenaturalhistory pages 1-6)

### Quality of life

The strongest recent quantitative evidence is the 2024 Dutch study of 353 adults. Its abstract reports: **“Pain was reported by 87.8% … and fatigue by 90.4%.”** Fatigue exceeded reference values for both healthy people and rheumatoid-arthritis patients (p<0.001). Fear-avoidance beliefs and fatigue were most strongly associated with pain; anxiety and depression were the strongest correlates in fatigue models. These data favor multidisciplinary management rather than a surgery-only model. (Amajjar et al., published 17 July 2024; DOI: https://doi.org/10.1371/journal.pone.0305640). (amajjar2024painandfatigue pages 1-2)

## 4. Genetic and molecular information

### Genes and proteins

* **EXT1:** chromosome 8q24.11–q24.13; HGNC:3512; OMIM gene 608177.
* **EXT2:** chromosome 11p11–p12; HGNC:3513; OMIM gene 608210.

EXT1 and EXT2 form a Golgi-resident hetero-oligomeric glycosyltransferase complex that alternately adds glucuronic acid and N-acetylglucosamine to elongate heparan-sulfate chains. Functional polymerase activity is supported by PMID **11391482**; Golgi complex localization/function by PMID **10639137**. (pacifici2018hereditarymultipleexostoses pages 7-9, pacifici2017hereditarymultipleexostoses pages 12-13)

### Pathogenic variants and diagnostic yield

The disease mechanism is loss of function/haploinsufficiency followed, in many lesions, by focal biallelic deficiency. Reported variant classes include nonsense, frameshift, canonical splice, missense with proven functional effect, exon or multiexon deletion, whole-gene deletion, and other structural rearrangements. Pathogenic missense calls require caution because loss of function is the established mechanism and some historical missense classifications may be incorrect. Combined EXT1/EXT2 detection ranges from roughly 70–95%; individual historical ranges were 28–65% for EXT1 and 21–61% for EXT2. Causal alleles are rare or absent from population databases as expected for a highly penetrant rare disorder; variant-specific gnomAD frequency must be documented rather than assigning a single disease-wide frequency. (darienzo2019hereditarymultipleexostoses pages 1-2, mordenti2020thenaturalhistory pages 1-6, beltrami2016hereditarymultipleexostoses pages 1-2, pacifici2017hereditarymultipleexostoses pages 6-7)

Important 2024 developments include:

1. A study of 244 unrelated probands found 177 unique single-nucleotide/copy-number variants across EXT1, EXT2, and PTPN11—80 known and 97 novel. Five patients with osteochondromas but no enchondromas carried **PTPN11** loss-of-function variants, suggesting overlap with metachondromatosis rather than proving that PTPN11 is a routine third HMO gene. The abstract states that prior EXT1/EXT2 DNA diagnostic yields were **“78 to 95%.”** (Borovikov et al., February 2024; DOI: https://doi.org/10.1155/2024/8849348). (borovikov2024themissingpiece pages 1-2)
2. Mosaic EXT1 deletions involving exons 8–11 and 2–11 were identified by genome/RNA-based investigation after standard tests were negative, supporting low-level mosaicism as one explanation for unresolved disease.
3. A novel tandem intragenic duplication involving EXT1 exon 4, c.(1128_1202)_(1284+29_1344)dup, demonstrated why dosage testing should accompany sequence analysis. The published abstract notes: **“Our finding expands the spectrum of MO-causing variants … underlying the importance of quantitative analysis in patients with negative sequencing.”** (Bartolotti et al., September 2024; DOI: https://doi.org/10.3390/genes15091169).

Variants in constitutional blood are germline; lesion-specific second hits are somatic. Constitutional mosaicism can produce milder or asymmetric expression and changes recurrence counseling. Large chromosomal deletions encompassing EXT genes can produce contiguous-gene phenotypes; routine karyotyping is otherwise low yield.

### Modifiers and epigenetics

No modifier gene or protective allele has sufficient replicated evidence for clinical use. **EXT1 versus EXT2 genotype**, sex, lesion location, and genetic background correlate imperfectly with severity. Evidence for disease-defining DNA methylation, histone modification, or chromatin signatures is insufficient; epigenomic assays are not diagnostic. (pacifici2017hereditarymultipleexostoses pages 13-14, pacifici2017hereditarymultipleexostoses pages 6-7)

## 5. Environmental information

HMO is not infectious, transmissible, toxicant-induced, or lifestyle-caused. No vaccination, antimicrobial therapy, dietary intervention, or exposure avoidance prevents the initiating lesion. Mechanical load and trauma may make an existing osteochondroma symptomatic or cause fracture/bursal inflammation but are not established causes. Smoking and alcohol may affect general surgical or cancer health but have no demonstrated disease-specific etiologic role.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline heterozygous pathogenic **EXT1** or **EXT2** variant **leads to** reduced EXT1–EXT2 glycosyltransferase activity and systemic heparan-sulfate insufficiency.
2. A focal somatic second hit in a growth-plate/perichondrial progenitor or chondrocyte **results in** biallelic EXT dysfunction and a severely heparan-sulfate-deficient clone; this step is demonstrated in subsets of human tumors and strongly supported by mouse models. (pacifici2017hereditarymultipleexostoses pages 12-13, pacifici2017hereditarymultipleexostoses pages 10-12, pacifici2017hereditarymultipleexostoses pages 1-2)
3. Reduced cell-surface/extracellular-matrix heparan sulfate **leads to** abnormal distribution, stability, and receptor presentation of morphogens.
4. This altered morphogen handling **results in** increased pro-chondrogenic BMP/hedgehog activity and reduced anti-chondrogenic FGF–MEK–ERK restraint and Noggin/Gremlin expression; detailed directionality is primarily model-organism/in-vitro evidence. WNT/β-catenin disturbance is implicated but less completely resolved. (pacifici2018hereditarymultipleexostoses pages 12-13, beltrami2016hereditarymultipleexostoses pages 1-2, garcia2021osteochondromapathogenesismouse pages 1-2)
5. Abnormal signaling at the growth-plate/perichondrial border **leads to** failure of normal border function, ectopic chondrocyte differentiation, and recruitment of adjacent wild-type cells into a heterogeneous cartilage cap.
6. Ectopic cartilage undergoes endochondral ossification **resulting in** a cortex- and marrow-continuous osteochondroma that grows while the physis is open.
7. Multiple lesions near active growth plates **lead to** physeal tethering, asymmetric growth, bowing, limb-length inequality, restricted motion, and short stature.
8. **Branch A:** Lesion mass effect **results in** pain, bursitis, tendon irritation, fracture, neurovascular compression, and—rarely—spinal-cord compromise.
9. **Branch B:** Additional neoplastic evolution in a cartilage cap **can lead to** secondary peripheral chondrosarcoma; this is uncommon and incompletely predictable.

Human biochemical evidence includes approximately 50% reduction in the blood heparan-sulfate:chondroitin-sulfate ratio (PMID **23514715**). Human lesion studies found LOH in 6/8 analyzed osteochondromas in one series. Mouse work provides causal evidence from clonal/chondrocyte-specific Ext1 loss (PMIDs **20080592**, **20534475**) and compound Ext1/Ext2 deficiency (PMID **21310272**). (pacifici2018hereditarymultipleexostoses pages 7-9, pacifici2017hereditarymultipleexostoses pages 12-13, pacifici2017hereditarymultipleexostoses pages 10-12)

**Suggested GO terms:** GO:0015012 heparan sulfate proteoglycan biosynthetic process; GO:0030201 heparan sulfate proteoglycan metabolic process; GO:0030509 BMP signaling; GO:0007224 Smoothened signaling; GO:0008543 FGFR signaling; GO:0016055 Wnt signaling; GO:0051216 cartilage development; GO:0001503 ossification; GO:0001958 endochondral ossification. **Cell Ontology:** CL:0000138 chondrocyte; CL:0000062 osteoblast; CL:0000134 mesenchymal stem cell, with growth-plate/perichondrial progenitor annotations where available.

### Profiling and advanced technologies

No validated transcriptomic, proteomic, metabolomic, lipidomic, liquid-biopsy, single-cell, spatial, or epigenomic diagnostic signature currently exists. In a 2024 mouse/cell study, palovarotene activated an osteoarthritis-like transcriptional program, upregulated matrix-catabolic genes, downregulated matrix-anabolic genes, and activated STAT3 but not STAT1/2. These are mechanistic/preclinical observations, not patient biomarkers. (garcia2024analysisofthe pages 1-2)

## 7. Anatomical structures affected

Primary sites are metaphyseal/metadiaphyseal regions of bones formed by endochondral ossification—especially distal femur, proximal tibia/fibula, proximal humerus, forearm, pelvis, scapula, ribs, and vertebrae. Nearly half of lesions occur around the knee; approximate site estimates include distal femur 30%, proximal tibia 15–20%, and humerus 10–20%. Hand/foot lesions occur but are less prominent. Craniofacial bones formed predominantly by intramembranous ossification are generally spared, although cranial-base lesions have been reported. Lesions may be bilateral and multiple but are often asymmetric. (darienzo2019hereditarymultipleexostoses pages 1-2, tepelenis2021osteochondromasanupdated pages 1-2, tepelenis2021osteochondromasanupdated pages 2-3, pacifici2018hereditarymultipleexostoses pages 7-9)

At tissue level, the cartilage cap, perichondrium, growth plate, adjacent cortical/trabecular bone, marrow, tendon/bursa, and nearby nerves/vessels are relevant. At cellular level, chondrocytes and perichondrial/skeletogenic progenitors are central, with osteoblast-lineage cells participating in endochondral conversion. The key subcellular compartment is the **Golgi apparatus/Golgi membrane**, where EXT1–EXT2 synthesizes heparan sulfate; downstream abnormalities occur at the plasma membrane and extracellular matrix.

**Suggested anatomy:** UBERON:0000981 femur; UBERON:0000979 tibia; UBERON:0001424 humerus; UBERON:0000976 radius; UBERON:0001423 ulna; UBERON:0001270 pelvis; UBERON:0001132 parietal pleura/rib-region annotations should be refined to the exact lesion; UBERON:0002412 vertebral column. **GO cellular components:** GO:0005794 Golgi apparatus; GO:0000139 Golgi membrane; GO:0005576 extracellular region; GO:0005886 plasma membrane.

## 8. Temporal development

HMO is genetically present from conception but usually clinically silent at birth. Lesions can appear by age 2; median diagnosis is approximately 3 years, 50% have a visible lesion by age 5, and 80% by age 10. Growth is chronic and insidious, with the highest lesion-accrual risk during rapid skeletal growth. Lesions generally stop enlarging at skeletal maturity; new growth or pain thereafter warrants investigation for complications or malignant transformation. (mordenti2020thenaturalhistory pages 1-6, tepelenis2021osteochondromasanupdated pages 2-3, ruedadeeusebio2025hereditarymultipleexostoses pages 2-5)

There is no standard stage system. A practical course is: early palpable lesions; accumulating lesions and deformity during childhood; functional restriction and corrective surgery during later growth; stable residual lesions after maturity; and adult complications such as osteoarthritis, chronic pain, fatigue, or rare chondrosarcoma. Spontaneous true remission is not expected, although some lesions regress and symptoms may improve after surgery. The critical monitoring window is childhood/adolescence for growth disturbance and adulthood for new pain or lesion enlargement. (beltrami2016hereditarymultipleexostoses pages 7-8, mordenti2020thenaturalhistory pages 1-6)

## 9. Inheritance and population

Inheritance is autosomal dominant. An affected heterozygous individual has a 50% transmission probability per pregnancy. Penetrance is near complete and has historically been estimated at approximately 100% in males and 96% in females, although ascertainment and modern imaging may alter this difference. Expressivity is highly variable, including within families. Anticipation is not established. De novo disease and constitutional/germline mosaicism occur; therefore, an apparently negative family history does not exclude HMO. Consanguinity has no special etiologic role in this dominant disorder. (darienzo2019hereditarymultipleexostoses pages 1-2, mangualgarcia2015multipleskeletaldeformities pages 1-2)

Reported prevalence is approximately 1:50,000 in Western populations; incidence estimates extend to 1:100,000 in some sources. Historical male:female ratios of about 1.5:1 probably reflect reduced clinical ascertainment in mildly affected females rather than true sex-linked inheritance. No consistently high-risk ethnicity is established, although founder variants may occur in individual families or isolates. Population carrier frequency cannot be reliably inferred from gnomAD because pathogenic alleles are heterogeneous, very rare, and incompletely captured. (darienzo2019hereditarymultipleexostoses pages 1-2, ruedadeeusebio2025hereditarymultipleexostoses pages 1-2)

## 10. Diagnostics

### Clinical and imaging diagnosis

Diagnosis is based on physical examination, family history, and imaging showing at least two osteochondromas with cortical and medullary continuity. Plain radiography is first line. CT is valuable for complex pelvic, scapular, costal, or spinal anatomy. MRI best depicts the hyaline-cartilage cap, marrow, soft tissue, neurovascular structures, and suspected spinal or malignant complications. Ultrasound can measure a superficial cartilage cap. (tepelenis2021osteochondromasanupdated pages 1-2, ruedadeeusebio2025hereditarymultipleexostoses pages 1-2, tepelenis2021osteochondromasanupdated pages 7-8)

Red flags for secondary chondrosarcoma include new or increasing pain, growth after skeletal maturity, an irregular/lobulated surface, internal lysis or irregular calcification, erosion of adjacent bone, a soft-tissue mass, and a thick cartilage cap. Common thresholds are >2 cm in adults and >3 cm in children, although some HMO literature uses 1.5–2 cm; thresholds must be interpreted with age and imaging quality. Histology shows a perichondrial/fibrous covering, hyaline-cartilage cap, and endochondral bone. Suspected malignancy requires expert musculoskeletal radiology and pathology, with biopsy planned by the treating sarcoma team. (gnoli2024secondaryperipheralchondrosarcoma pages 1-2, tepelenis2021osteochondromasanupdated pages 7-8)

### Genetic testing algorithm

1. Sequence **EXT1** and **EXT2** using a validated panel with full coding and splice-region coverage.
2. Perform exon-level deletion/duplication analysis—such as MLPA—if not already integrated.
3. Reassess phenotype and variant classification under ACMG/AMP criteria; do not assume every rare missense allele is causal.
4. If unresolved, consider high-depth genome sequencing, structural-variant analysis, and RNA studies; test another tissue when low-level mosaicism is suspected.
5. Add **PTPN11** when enchondromas, lesions directed toward joints, spontaneous regression, or other features suggest metachondromatosis/overlap.
6. Use parental testing for segregation, de novo confirmation, and recurrence counseling.

WES can identify coding variants but may miss mosaic or structural lesions; WGS is more useful for noncoding and structural variants. CMA is appropriate for a syndromic phenotype suggesting a large deletion; karyotype/FISH are not routine first-line tests. Mitochondrial and repeat-expansion assays are not relevant. No omics-based clinical diagnostic is validated. (borovikov2024themissingpiece pages 1-2, pacifici2017hereditarymultipleexostoses pages 10-12, pacifici2017hereditarymultipleexostoses pages 6-7)

### Differential diagnosis and screening

Differentials include solitary osteochondroma; metachondromatosis (**PTPN11**, osteochondromas plus enchondromas, often joint-directed); Ollier disease and Maffucci syndrome (enchondromas, with vascular anomalies in Maffucci); dysplasia epiphysealis hemimelica/Trevor disease (epiphyseal osteochondral overgrowth); Langer–Giedion syndrome/TRPS II (contiguous deletion including EXT1); and secondary peripheral chondrosarcoma. (borovikov2024themissingpiece pages 13-13, borovikov2024themissingpiece pages 1-2)

There is no newborn biochemical screen. Cascade clinical and molecular testing is appropriate for relatives. Prenatal or preimplantation genetic testing is possible after the familial variant is known. Routine indiscriminate repeated whole-body ionizing imaging is undesirable; surveillance should be individualized.

## 11. Outcome and prognosis

Life expectancy is usually near normal unless malignant or severe neurovascular complications occur. Disease burden is chiefly chronic morbidity rather than mortality. Pain, fatigue, mobility restriction, deformity, early osteoarthritis, work/sport limitations, and repeated operations can substantially impair quality of life. (amajjar2024painandfatigue pages 1-2, mordenti2020thenaturalhistory pages 1-6)

Malignant transformation estimates vary from approximately 0.5–5% in population-oriented literature, with higher figures in referral centers reflecting ascertainment bias. In the 2024 Rizzoli series of 105 HMO-associated secondary peripheral chondrosarcomas, age at diagnosis ranged from 13–63 years (median 34); pelvis was the commonest site (46/105, 44%), followed by lower limbs (35). Of 103 graded tumors, 59 were grade 1, 40 grade 2, and 4 grade 3. Grade 2/3 histology and partial resection predicted worse disease-free survival. The abstract concludes that malignant transformation **“can occur also in younger patient[s]”** and therefore age alone should not negate suspicious findings. (Gnoli et al., February 2024; DOI: https://doi.org/10.1186/s13023-023-03006-8). (gnoli2024secondaryperipheralchondrosarcoma pages 1-2)

For secondary peripheral chondrosarcoma, complete surgical margins and grade are major prognostic factors. Historical estimates include approximately 90% five-year survival overall and ten-year survival of 83% for grade I versus 29% for grade III disease, but these figures are not HMO-specific in every source and should not be used as an individualized calculator. (beltrami2016hereditarymultipleexostoses pages 7-8, tepelenis2021osteochondromasanupdated pages 7-8)

## 12. Treatment

### Current standard care

No pharmacologic therapy prevents or reverses HMO. Asymptomatic lesions are observed. Indications for surgery include persistent pain, functional restriction, tendon or joint impingement, progressive deformity, fracture, neurovascular compromise, spinal-cord compression, and suspected malignancy. Procedures include complete marginal excision with removal of cartilage cap/perichondrium, corrective osteotomy, hemiepiphysiodesis, limb or ulnar lengthening, and sarcoma-wide resection. Incomplete cap/perichondrium removal increases recurrence. Reported recurrence after complete excision is below 2%, while postoperative complication estimates are approximately 11.6–12.5%. (beltrami2016hereditarymultipleexostoses pages 7-8, tepelenis2021osteochondromasanupdated pages 7-8)

Forearm surgery illustrates the evidence limitations: among 315 forearms in a systematic review, 66.7% underwent ulnar lengthening with or without associated procedures and 20.6% isolated excision, but evidence that reconstruction improves long-term function or quality of life was poor. Treatment must therefore be individualized rather than triggered by radiographic appearance alone.

Supportive care includes age-appropriate analgesia, physical and occupational therapy, maintenance of strength and safe range of motion, gait or orthotic assessment, workplace/school accommodation, and psychological treatment for fear avoidance, anxiety, or depression. Refractory pain occasionally prompts neuromodulation or intrathecal analgesia, but evidence is limited to case reports. (amajjar2024painandfatigue pages 1-2)

**Suggested NCIT intervention terms:** NCIT:C15329 Surgical Procedure; NCIT:C52003 Excision; NCIT:C51932 Osteotomy; NCIT:C15214 Rehabilitation; NCIT:C16809 MRI; NCIT:C101293 Genetic Testing.

### Experimental and targeted therapy

Palovarotene is a retinoic-acid receptor-γ agonist (**CHEBI:177944**) investigated in phase 2 pediatric HMO trial **NCT03442985**. The study enrolled genetically confirmed, symptomatic children aged 2–14 but was terminated/held amid concern about premature growth-plate closure, a particularly serious risk in a pediatric skeletal-growth disorder. No approved HMO indication or established response rate exists. (NCT03442985 chunk 2, garcia2024analysisofthe pages 1-2)

In a 2024 mouse study, escalating systemic palovarotene held pre-existing tumor volume near baseline—0.31±0.049 mm³ versus 0.27±0.031 initially (p=0.66)—while controls grew to 1.03±0.23 mm³ (p=0.023 versus treated). Local nanoparticle delivery also reduced growth (0.26±0.10 versus 0.52±0.11 mm³; p=0.008). The abstract states: **“These findings suggest that palovarotene treatment is effective against pre-existing osteochondromas and that the Stat3 pathway is involved.”** This is preclinical evidence and does not overcome human safety/efficacy uncertainty. (Garcia et al., published 11 July 2024; DOI: https://doi.org/10.3390/ijms25147610). (garcia2024analysisofthe pages 1-2)

BMP antagonism, heparanase inhibition, hedgehog/IHH inhibition, and restoration of FGF restraint have reduced chondrogenesis or lesion formation in models. They remain experimental, with no validated HMO gene therapy, CRISPR therapy, RNA therapy, cell therapy, immunotherapy, or pharmacogenomic treatment algorithm. (pacifici2018hereditarymultipleexostoses pages 12-13, beltrami2016hereditarymultipleexostoses pages 8-8, pacifici2017hereditarymultipleexostoses pages 10-12, pacifici2018hereditarymultipleexostoses pages 7-9)

## 13. Prevention

Primary prevention through lifestyle change or immunization is not possible. Reproductive options after molecular confirmation include genetic counseling, prenatal diagnosis, and IVF with preimplantation genetic testing. Counseling should address 50% transmission risk, variable expressivity, mosaicism, and the inability to predict severity precisely from genotype.

Secondary prevention consists of cascade testing and early clinical recognition in at-risk children, allowing monitoring of growth, limb alignment, motion, spinal/neurologic signs, and symptomatic lesions. Tertiary prevention includes timely correction of progressive deformity, complete excision when indicated, rehabilitation, pain management, and prompt MRI/sarcoma referral for adult lesion growth or new persistent pain. There is no accepted population screening program or prophylactic medication. Suggested follow-up intervals in older reviews—6–12 months in growing children and 12–24 months in adults—are expert-practice recommendations rather than high-level trial evidence and should be individualized. (beltrami2016hereditarymultipleexostoses pages 7-8)

## 14. Other species and natural disease

A well-characterized, naturally occurring veterinary counterpart attributable to orthologous EXT1/EXT2 variants is not established strongly enough in the retrieved evidence for a curated natural-disease assertion. Osteochondromas occur in domestic animals, but sporadic veterinary lesions should not automatically be labeled orthologous HMO. There is no zoonotic potential or cross-species transmission.

Relevant taxa for experimental comparative biology are **Mus musculus** (NCBI Taxon:10090) and **Danio rerio** (Taxon:7955). EXT heparan-sulfate biosynthesis and endochondral ossification are evolutionarily conserved, explaining why engineered models reproduce key mechanisms.

## 15. Model organisms

### Mouse

Ext1- or Ext2-single-heterozygous mice are often largely normal, limiting their utility as simple haploinsufficiency models. Compound Ext1+/−;Ext2+/− mice, chondrocyte-specific conditional Ext1-null mice, and mosaic/clonal Ext1 inactivation models develop multiple osteochondroma-like lesions. These models strongly support severe focal heparan-sulfate deficiency and a second-hit mechanism and are used to test BMP antagonists, heparanase inhibitors, and RARγ agonists. Key studies include PMIDs **16236767**, **20080592**, **20534475**, and **21310272**. Limitations include engineered timing/cell specificity, more uniform genetic backgrounds, and incomplete reproduction of variable human pain, deformity, and malignancy. (beltrami2016hereditarymultipleexostoses pages 8-8, pacifici2017hereditarymultipleexostoses pages 12-13, pacifici2018hereditarymultipleexostoses pages 7-9, pacifici2017hereditarymultipleexostoses pages 1-2)

### Zebrafish

The **dackel/ext2** mutant reproduces abnormal cartilage and bone patterning. Homozygous ext2-null fish show failed terminal chondrocyte differentiation, impaired osteoblast differentiation, altered bone–fat lineage balance, misshapen bones, and muscle abnormalities. These models are powerful for developmental imaging and pathway screening but do not anatomically reproduce every human osteochondroma. Dental abnormalities observed in ext2 mutants generated a hypothesis of underrecognized dental manifestations in patients, illustrating both comparative utility and the need for human validation.

### Cellular systems

Primary chondrocytes, lesion-derived cells, and cultured skeletal progenitors permit assays of heparan-sulfate production, BMP/FGF/hedgehog/WNT signaling, matrix synthesis, and retinoid response. No validated human HMO organoid, iPSC assay, or CRISPR screen currently functions as a clinical diagnostic or treatment-selection platform.

## Current research infrastructure and evidence gaps

The Italian Registry of Multiple Osteochondromas, **NCT04133285**, is a recruiting retrospective/prospective cohort designed for up to 10,000 participants through 2032. It integrates clinical, genetic, genealogic, imaging, surgery, quality-of-life, tissue, and longitudinal malignancy data. Such registries are essential because rarity, variable expressivity, and referral bias undermine precise prevalence, malignancy-risk, and treatment-effect estimates. (NCT04133285 chunk 1)

Major gaps are: validated age- and genotype-specific surveillance schedules; prospective surgical comparative studies; robust malignant-transformation biomarkers; replicated modifier genes; longitudinal patient-reported outcomes; human single-cell/spatial maps of lesion initiation; and a safe disease-modifying therapy. The current expert interpretation is therefore conservative: molecular diagnosis and multidisciplinary longitudinal care are clinically actionable, whereas pathway-targeted treatment remains investigational.

References

1. (borovikov2024themissingpiece pages 1-2): Artem Borovikov, Nailya Galeeva, Andrey Marakhonov, Aysylu Murtazina, Varvara Kadnikova, Kseniya Davydenko, Anna Orlova, Peter Sparber, Tatiana Markova, Maria Orlova, Darya Osipova, Tatyana Nagornova, Natalia Semenova, Olga Levchenko, Alexandra Filatova, Margarita Sharova, Peter Vasiluev, Ilya Kanivets, Denis Pyankov, Artem Sharkov, Vasilisa Udalova, Vladimir Kenis, Natalia Nikitina, Maria Sumina, Konstantin Zherdev, Aleksandr Petel'guzov, Oleg Chelpachenko, Pavel Zubkov, Ivan Dan, Andrey Snetkov, Alexandra Akinshina, Yury Buklemishev, Oxana Ryzhkova, Vyacheslav Tabakov, Ekaterina Zakharova, Sergey Korostelev, Rena Zinchenko, Mikhail Skoblov, Alexander Polyakov, Elena Dadali, Sergey Kutsev, and Olga Shchagina. The missing piece of the puzzle: unveiling the role of ptpn11 gene in multiple osteochondromas in a large cohort study. Human Mutation, 2024:1-13, Feb 2024. URL: https://doi.org/10.1155/2024/8849348, doi:10.1155/2024/8849348. This article has 6 citations and is from a domain leading peer-reviewed journal.

2. (gnoli2024secondaryperipheralchondrosarcoma pages 1-2): Maria Gnoli, Marco Gambarotti, Alberto Righi, Eric Lodewijk Staals, Andrea Evangelista, Morena Tremosini, Evelise Brizola, Marina Mordenti, Manila Boarini, Manuela Locatelli, Elena Pedrini, and Luca Sangiorgi. Secondary peripheral chondrosarcoma in multiple osteochondromas: a retrospective single-institution case series. Orphanet Journal of Rare Diseases, Feb 2024. URL: https://doi.org/10.1186/s13023-023-03006-8, doi:10.1186/s13023-023-03006-8. This article has 12 citations and is from a peer-reviewed journal.

3. (amajjar2024painandfatigue pages 1-2): Ihsane Amajjar, Kuni Vergauwen, Nienke W. Willigenburg, S. John Ham, and Rob J. E. M. Smeets. Pain and fatigue in adult patients with multiple osteochondromas: the netherlands. PLOS ONE, 19:e0305640, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0305640, doi:10.1371/journal.pone.0305640. This article has 6 citations and is from a peer-reviewed journal.

4. (garcia2024analysisofthe pages 1-2): Sonia A. Garcia, Kimberly Wilson, Ningfeng Tang, Hongying Tian, Takeshi Oichi, Aruni T. Gunawardena, Michael Chorny, Ivan S. Alferiev, John E. Herzenberg, Vincent Y. Ng, Masahiro Iwamoto, and Motomi Enomoto-Iwamoto. Analysis of the actions of rarγ agonists on growing osteochondromas in a mouse model. Jul 2024. URL: https://doi.org/10.3390/ijms25147610, doi:10.3390/ijms25147610. This article has 4 citations.

5. (OpenTargets Search: hereditary multiple osteochondromas-EXT1,EXT2): Open Targets Query (hereditary multiple osteochondromas-EXT1,EXT2, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (darienzo2019hereditarymultipleexostoses pages 1-2): Antonio D'Arienzo, Lorenzo Andreani, Federico Sacchetti, Simone Colangeli, and Rodolfo Capanna. Hereditary multiple exostoses: current insights. Orthopedic Research and Reviews, 11:199-211, Dec 2019. URL: https://doi.org/10.2147/orr.s183979, doi:10.2147/orr.s183979. This article has 138 citations and is from a peer-reviewed journal.

7. (pacifici2018hereditarymultipleexostoses pages 7-9): Maurizio Pacifici. Hereditary multiple exostoses: are there new plausible treatment strategies? Expert Opinion on Orphan Drugs, 6:385-391, Jun 2018. URL: https://doi.org/10.1080/21678707.2018.1483232, doi:10.1080/21678707.2018.1483232. This article has 18 citations.

8. (pacifici2017hereditarymultipleexostoses pages 12-13): Maurizio Pacifici. Hereditary multiple exostoses: new insights into pathogenesis, clinical complications, and potential treatments. Current Osteoporosis Reports, 15:142-152, May 2017. URL: https://doi.org/10.1007/s11914-017-0355-2, doi:10.1007/s11914-017-0355-2. This article has 159 citations and is from a peer-reviewed journal.

9. (tepelenis2021osteochondromasanupdated pages 1-2): KOSTAS TEPELENIS, GEORGIOS PAPATHANAKOS, AIKATERINI KITSOULI, THEODOROS TROUPIS, ALEXANDRA BARBOUTI, KONSTANTINOS VLACHOS, PANAGIOTIS KANAVAROS, and PANAGIOTIS KITSOULIS. Osteochondromas: an updated review of epidemiology, pathogenesis, clinical presentation, radiological features and treatment options. In Vivo, 35:681-691, Jan 2021. URL: https://doi.org/10.21873/invivo.12308, doi:10.21873/invivo.12308. This article has 247 citations and is from a peer-reviewed journal.

10. (tepelenis2021osteochondromasanupdated pages 2-3): KOSTAS TEPELENIS, GEORGIOS PAPATHANAKOS, AIKATERINI KITSOULI, THEODOROS TROUPIS, ALEXANDRA BARBOUTI, KONSTANTINOS VLACHOS, PANAGIOTIS KANAVAROS, and PANAGIOTIS KITSOULIS. Osteochondromas: an updated review of epidemiology, pathogenesis, clinical presentation, radiological features and treatment options. In Vivo, 35:681-691, Jan 2021. URL: https://doi.org/10.21873/invivo.12308, doi:10.21873/invivo.12308. This article has 247 citations and is from a peer-reviewed journal.

11. (mordenti2020thenaturalhistory pages 1-6): Marina Mordenti, Fei Shih, Manila Boarini, Elena Pedrini, Maria Gnoli, Diego Antonioli, Morena Tremosini, and Luca Sangiorgi. The natural history of multiple osteochondromas in a large italian cohort of pediatric patients. Oct 2020. URL: https://doi.org/10.1016/j.bone.2020.115499, doi:10.1016/j.bone.2020.115499. This article has 32 citations and is from a domain leading peer-reviewed journal.

12. (pacifici2017hereditarymultipleexostoses pages 10-12): Maurizio Pacifici. Hereditary multiple exostoses: new insights into pathogenesis, clinical complications, and potential treatments. Current Osteoporosis Reports, 15:142-152, May 2017. URL: https://doi.org/10.1007/s11914-017-0355-2, doi:10.1007/s11914-017-0355-2. This article has 159 citations and is from a peer-reviewed journal.

13. (pacifici2018hereditarymultipleexostoses pages 12-13): Maurizio Pacifici. Hereditary multiple exostoses: are there new plausible treatment strategies? Expert Opinion on Orphan Drugs, 6:385-391, Jun 2018. URL: https://doi.org/10.1080/21678707.2018.1483232, doi:10.1080/21678707.2018.1483232. This article has 18 citations.

14. (tepelenis2021osteochondromasanupdated pages 7-8): KOSTAS TEPELENIS, GEORGIOS PAPATHANAKOS, AIKATERINI KITSOULI, THEODOROS TROUPIS, ALEXANDRA BARBOUTI, KONSTANTINOS VLACHOS, PANAGIOTIS KANAVAROS, and PANAGIOTIS KITSOULIS. Osteochondromas: an updated review of epidemiology, pathogenesis, clinical presentation, radiological features and treatment options. In Vivo, 35:681-691, Jan 2021. URL: https://doi.org/10.21873/invivo.12308, doi:10.21873/invivo.12308. This article has 247 citations and is from a peer-reviewed journal.

15. (beltrami2016hereditarymultipleexostoses pages 7-8): G. Beltrami, G. Ristori, G. Scoccianti, A. Tamburini, and R. Capanna. Hereditary multiple exostoses: a review of clinical appearance and metabolic pattern. Clinical cases in mineral and bone metabolism : the official journal of the Italian Society of Osteoporosis, Mineral Metabolism, and Skeletal Diseases, 13 2:110-118, May 2016. URL: https://doi.org/10.11138/ccmbm/2016.13.2.110, doi:10.11138/ccmbm/2016.13.2.110. This article has 120 citations.

16. (NCT03442985 chunk 2):  An Efficacy and Safety Study of Palovarotene for the Treatment of MO. Clementia Pharmaceuticals Inc.. 2018. ClinicalTrials.gov Identifier: NCT03442985

17. (pacifici2017hereditarymultipleexostoses pages 1-2): Maurizio Pacifici. Hereditary multiple exostoses: new insights into pathogenesis, clinical complications, and potential treatments. Current Osteoporosis Reports, 15:142-152, May 2017. URL: https://doi.org/10.1007/s11914-017-0355-2, doi:10.1007/s11914-017-0355-2. This article has 159 citations and is from a peer-reviewed journal.

18. (NCT04133285 chunk 1): Luca Sangiorgi. Registry of Multiple Osteochondromas. Luca Sangiorgi. 2013. ClinicalTrials.gov Identifier: NCT04133285

19. (ruedadeeusebio2025hereditarymultipleexostoses pages 1-2): Alvaro Rueda-de-Eusebio, Sara Gomez-Pena, María José Moreno-Casado, Gloria Marquina, Juan Arrazola, and Ana María Crespo-Rodríguez. Hereditary multiple exostoses: an educational review. Insights into Imaging, Feb 2025. URL: https://doi.org/10.1186/s13244-025-01899-6, doi:10.1186/s13244-025-01899-6. This article has 28 citations and is from a peer-reviewed journal.

20. (pacifici2017hereditarymultipleexostoses pages 6-7): Maurizio Pacifici. Hereditary multiple exostoses: new insights into pathogenesis, clinical complications, and potential treatments. Current Osteoporosis Reports, 15:142-152, May 2017. URL: https://doi.org/10.1007/s11914-017-0355-2, doi:10.1007/s11914-017-0355-2. This article has 159 citations and is from a peer-reviewed journal.

21. (beltrami2016hereditarymultipleexostoses pages 1-2): G. Beltrami, G. Ristori, G. Scoccianti, A. Tamburini, and R. Capanna. Hereditary multiple exostoses: a review of clinical appearance and metabolic pattern. Clinical cases in mineral and bone metabolism : the official journal of the Italian Society of Osteoporosis, Mineral Metabolism, and Skeletal Diseases, 13 2:110-118, May 2016. URL: https://doi.org/10.11138/ccmbm/2016.13.2.110, doi:10.11138/ccmbm/2016.13.2.110. This article has 120 citations.

22. (pacifici2017hereditarymultipleexostoses pages 13-14): Maurizio Pacifici. Hereditary multiple exostoses: new insights into pathogenesis, clinical complications, and potential treatments. Current Osteoporosis Reports, 15:142-152, May 2017. URL: https://doi.org/10.1007/s11914-017-0355-2, doi:10.1007/s11914-017-0355-2. This article has 159 citations and is from a peer-reviewed journal.

23. (garcia2021osteochondromapathogenesismouse pages 1-2): Sonia Arely Garcia, Vincent Y. Ng, Masahiro Iwamoto, and Motomi Enomoto-Iwamoto. Osteochondroma pathogenesis: mouse models and mechanistic insights into interactions with retinoid signaling. The American journal of pathology, 191 12:2042-2051, Dec 2021. URL: https://doi.org/10.1016/j.ajpath.2021.08.003, doi:10.1016/j.ajpath.2021.08.003. This article has 20 citations.

24. (ruedadeeusebio2025hereditarymultipleexostoses pages 2-5): Alvaro Rueda-de-Eusebio, Sara Gomez-Pena, María José Moreno-Casado, Gloria Marquina, Juan Arrazola, and Ana María Crespo-Rodríguez. Hereditary multiple exostoses: an educational review. Insights into Imaging, Feb 2025. URL: https://doi.org/10.1186/s13244-025-01899-6, doi:10.1186/s13244-025-01899-6. This article has 28 citations and is from a peer-reviewed journal.

25. (mangualgarcia2015multipleskeletaldeformities pages 1-2): M Mangual-García and A Sánchez-Cruz. Multiple skeletal deformities in a middle-aged man. Unknown journal, 2015.

26. (borovikov2024themissingpiece pages 13-13): Artem Borovikov, Nailya Galeeva, Andrey Marakhonov, Aysylu Murtazina, Varvara Kadnikova, Kseniya Davydenko, Anna Orlova, Peter Sparber, Tatiana Markova, Maria Orlova, Darya Osipova, Tatyana Nagornova, Natalia Semenova, Olga Levchenko, Alexandra Filatova, Margarita Sharova, Peter Vasiluev, Ilya Kanivets, Denis Pyankov, Artem Sharkov, Vasilisa Udalova, Vladimir Kenis, Natalia Nikitina, Maria Sumina, Konstantin Zherdev, Aleksandr Petel'guzov, Oleg Chelpachenko, Pavel Zubkov, Ivan Dan, Andrey Snetkov, Alexandra Akinshina, Yury Buklemishev, Oxana Ryzhkova, Vyacheslav Tabakov, Ekaterina Zakharova, Sergey Korostelev, Rena Zinchenko, Mikhail Skoblov, Alexander Polyakov, Elena Dadali, Sergey Kutsev, and Olga Shchagina. The missing piece of the puzzle: unveiling the role of ptpn11 gene in multiple osteochondromas in a large cohort study. Human Mutation, 2024:1-13, Feb 2024. URL: https://doi.org/10.1155/2024/8849348, doi:10.1155/2024/8849348. This article has 6 citations and is from a domain leading peer-reviewed journal.

27. (beltrami2016hereditarymultipleexostoses pages 8-8): G. Beltrami, G. Ristori, G. Scoccianti, A. Tamburini, and R. Capanna. Hereditary multiple exostoses: a review of clinical appearance and metabolic pattern. Clinical cases in mineral and bone metabolism : the official journal of the Italian Society of Osteoporosis, Mineral Metabolism, and Skeletal Diseases, 13 2:110-118, May 2016. URL: https://doi.org/10.11138/ccmbm/2016.13.2.110, doi:10.11138/ccmbm/2016.13.2.110. This article has 120 citations.

## Artifacts

- [Edison artifact artifact-00](Hereditary_Multiple_Osteochondromas-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 73 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 10 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C121924` (Enostosis) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`, `OMIM`, `PMIDs`, `Taxon`, `ORPHA`.

62 of 73 terms resolved to a current term; the rest could not be looked up either way.