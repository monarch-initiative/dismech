---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T14:33:01.794231'
end_time: '2026-09-04T14:42:35.922455'
duration_seconds: 574.13
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: "Dilated cardiomyopathy 2J, CMD2J, OMIM 620635 \u2014 an autosomal\
    \ recessive pediatric dilated cardiomyopathy caused by biallelic variants in FLII,\
    \ the human flightless-I homolog, a gelsolin-family actin-remodelling protein.\
    \ Not FLNC, not FLII-adjacent LRRFIP genes."
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 10
  verified: 10
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cardiomyopathy_Dilated_2J-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated cardiomyopathy 2J, CMD2J, OMIM 620635 — an autosomal recessive pediatric dilated cardiomyopathy caused by biallelic variants in FLII, the human flightless-I homolog, a gelsolin-family actin-remodelling protein. Not FLNC, not FLII-adjacent LRRFIP genes.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated cardiomyopathy 2J, CMD2J, OMIM 620635 — an autosomal recessive pediatric dilated cardiomyopathy caused by biallelic variants in FLII, the human flightless-I homolog, a gelsolin-family actin-remodelling protein. Not FLNC, not FLII-adjacent LRRFIP genes.** covering all of the
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
- **Disease Name:** Dilated cardiomyopathy 2J, CMD2J, OMIM 620635 — an autosomal recessive pediatric dilated cardiomyopathy caused by biallelic variants in FLII, the human flightless-I homolog, a gelsolin-family actin-remodelling protein. Not FLNC, not FLII-adjacent LRRFIP genes.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated cardiomyopathy 2J, CMD2J, OMIM 620635 — an autosomal recessive pediatric dilated cardiomyopathy caused by biallelic variants in FLII, the human flightless-I homolog, a gelsolin-family actin-remodelling protein. Not FLNC, not FLII-adjacent LRRFIP genes.** covering all of the
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


# Dilated cardiomyopathy 2J (CMD2J; FLII-related pediatric DCM)

## Executive summary and evidence grade

Dilated cardiomyopathy 2J is a newly delineated, autosomal-recessive infantile cardiomyopathy caused by biallelic germline variants in **FLII**, encoding flightless-I homolog, a gelsolin-family actin-remodeling protein. It is **not FLNC-related cardiomyopathy**, **not disease caused by the adjacent LRRFIP genes**, and **not FLI1**, the unrelated ETS-family transcription factor. The defining evidence comprises only three affected children from three unrelated families, supplemented by patient-variant zebrafish models and independent mouse cardiac studies. Consequently, its core gene–disease relationship is compelling, but penetrance, complete phenotypic spectrum, population frequency, and prognosis remain poorly quantified. (ruijmbeek2023biallelicvariantsin pages 2-4, ruijmbeek2023biallelicvariantsin pages 1-2, lipov2023exploringthecomplex pages 3-4)

The primary disease report is Ruijmbeek et al., *JCI Insight*, published 5 September 2023, DOI [10.1172/jci.insight.168247](https://doi.org/10.1172/jci.insight.168247). Its abstract states: **“we identified biallelic variants in the highly conserved flightless-I (FLII) gene in 3 families with idiopathic, early-onset dilated CM”** and concludes that the data “report biallelic variants as a genetic cause of pediatric CM.” (ruijmbeek2023biallelicvariantsin pages 1-2)

The compact case and model-evidence audit is shown below.

| Evidence type | Subject / finding | Core evidence | Genotype / frequency | Outcome or interpretation | Citation |
|---|---|---|---|---|---|
| Human—disease definition | CMD2J / dilated cardiomyopathy 2J | Autosomal-recessive, early-onset pediatric DCM caused by biallelic variants in **FLII** (flightless-I homolog); initially established in three unrelated families. This is **FLII**, not *FLNC*, *FLI1*, or an adjacent *LRRFIP* gene. | OMIM **620635** | Newly delineated ultra-rare Mendelian cardiomyopathy | (ruijmbeek2023biallelicvariantsin pages 2-4, ruijmbeek2023biallelicvariantsin pages 1-2) |
| Human—patient 1 | Family 1, Dutch, nonconsanguineous; individual II:2, female | Presented at **2 months** with tachyarrhythmia and DCM; reported cohort LVEF range was **23%–32%**, but the exact patient-specific value was not available in the extracted evidence | **NM_002018.3:** compound heterozygous c.1360C>T, p.(Gln454Ter) and c.3502C>T, p.(Arg1168Trp); gnomAD: truncating allele not reported in extracted table, p.Arg1168Trp MAF **0.000024** | Alive at **2 years**; cardiac function stable or improved; no reported extracardiac phenotype | (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4) |
| Human—patient 2 | Family 2, Saudi Arabian, consanguineous; individual II:1, female | Presented at **5 months** with heart failure, DCM, and secundum atrial septal defect; cohort LVEF **23%–32%**, individual value unavailable | **NM_002018.3:** homozygous c.2020C>G, p.(Leu674Val); gnomAD **not reported/absent** in the study table | Alive at **6 years**; cardiac function stable or improved; ASD-II was the only additional reported structural feature | (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4) |
| Human—patient 3 | Family 3, Saudi Arabian, consanguineous; individual II:1, male | Presented at **3 months** with heart failure and DCM; cohort LVEF **23%–32%**, individual value unavailable | **NM_002018.3:** homozygous c.3718C>T, p.(Arg1240Cys); gnomAD MAF **0.000057** | Alive at **9 years**; cardiac function stable or improved; no reported extracardiac phenotype | (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4) |
| Human—inheritance and segregation | Three families | Recessive segregation: affected children carried biallelic variants, whereas heterozygous parents were reportedly unaffected by DCM | One protein-truncating and three conserved missense alleles; variants absent or extremely rare in gnomAD and predicted damaging | Supports autosomal-recessive causation; penetrance and expressivity cannot be estimated from three affected individuals | (ruijmbeek2023biallelicvariantsin pages 2-4, lipov2023exploringthecomplex pages 3-4) |
| Model—direct disease evidence | CRISPR/Cas9 zebrafish carrying patient-mimicking *flii* alleles | Patient-specific alleles caused reduced ventricular fractional-area change/ejection fraction, abnormal trabeculation, myofibrillar disorganization, and altered cardiomyocyte adhesion; Flii localized to intercalated-disk and costamere-like adhesions | Modeled alleles included *flii* p.Arg1158Trp and p.Arg1230Cys plus a truncating allele; these are zebrafish equivalents, not human HGVS designations | Recapitulated key human cardiac abnormalities and supported hypomorphic pathogenic effects | (ruijmbeek2023biallelicvariantsin pages 12-13, ruijmbeek2023biallelicvariantsin pages 8-11) |
| Model—direct mechanistic branch | Zebrafish *flii* loss of function | Disrupted focal-adhesion/cell-junction organization: vinculin became diffuse and cadherin-2 lost punctate membrane localization; Notch reporter activity and nuclear Wwtr1/Taz were reduced, linking adhesion/myofibril defects to altered Notch and Hippo signaling | Null-like *flii* p.Asp110fs caused a more severe phenotype than patient-specific alleles | Severe trabeculation and ventricular-wall morphogenesis defects led to systolic failure and larval lethality; patient-specific alleles were milder | (ruijmbeek2023biallelicvariantsin pages 12-13, ruijmbeek2023biallelicvariantsin pages 8-11) |
| Model—complementary FLII mechanism | Cardiac-specific knockout and human-variant knock-in mice | Flii regulates sarcomeric actin thin-filament length through interaction/sequestration of tropomodulin-1; cardiac deletion shortened thin filaments and caused hypertrophy, impaired ventricular function, lung congestion, and early death. The syntenic p.Arg1245His knock-in also shortened thin filaments and increased cardiomyopathy susceptibility | Human low-frequency allele **rs8821, p.Arg1243His**; overall MAF **0.0175**, European MAF **0.0267**. This susceptibility allele is not one of the CMD2J family alleles | Independently establishes FLII as a cardiac sarcomere regulator; LMOD2 overexpression partially rescued knockout disease in mice, but this is not a validated human therapy | (kuwabara2023ahumanflii pages 2-3, kuwabara2023ahumanflii pages 1-2) |
| Evidence limitations | Current knowledge base | Only **three affected children from three families** were available in the defining report; no disease-specific prevalence, incidence, sex ratio, penetrance estimate, validated biomarker, histopathologic signature, quality-of-life measurement, or FLII-targeted treatment trial was identified | ACMG/AMP classifications and complete ancestry-stratified carrier frequencies were not available in the extracted primary evidence | Clinical management must presently follow general pediatric DCM/heart-failure guidance; zebrafish and mouse mechanisms should not be treated as demonstrated human myocardial pathology | (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4, malinow2024pediatricdilatedcardiomyopathy pages 9-10) |


*Table: Compact audit table of the defining human cases, segregation evidence, direct zebrafish validation, complementary mouse mechanism, and principal evidence gaps for FLII-related CMD2J.*

## 1. Disease information

**Definition.** CMD2J is a Mendelian myocardial disorder presenting in early infancy with left-ventricular dilation and severe systolic dysfunction in the absence of a sufficient loading condition or another identified cause. The reported phenotype is predominantly isolated DCM; one child had a secundum atrial septal defect. (ruijmbeek2023biallelicvariantsin pages 2-4, ruijmbeek2023biallelicvariantsin pages 12-13)

**Identifiers and terminology.** The disease identifier specified for this entity is **OMIM 620635**, with preferred names *dilated cardiomyopathy 2J*, *CMD2J*, *FLII-related dilated cardiomyopathy*, and *autosomal-recessive pediatric cardiomyopathy due to FLII*. A confidently disease-specific MONDO, Orphanet, MeSH, ICD-10, or ICD-11 code was not identified in the retrieved literature. Until such mappings are curated, generic DCM codes should not be represented as uniquely identifying CMD2J. Suggested knowledge-base mapping is a provisional child of MONDO “dilated cardiomyopathy” with causal gene **FLII** and autosomal-recessive inheritance.

**Evidence provenance.** Current clinical information is a published, aggregated disease-level case series derived from three individually evaluated probands—not EHR-derived population data. Evaluations included examination, 12-lead ECG, transthoracic echocardiography, exome sequencing, and Sanger confirmation. (ruijmbeek2023biallelicvariantsin pages 12-13)

## 2. Etiology, risk, protection, and environment

The necessary initiating factor is **biallelic germline variation in FLII**. One family was nonconsanguineous and compound heterozygous; two Saudi families were consanguineous and had homozygous variants. Unaffected heterozygous parents support recessive inheritance. (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4)

No validated susceptibility modifier, protective allele, environmental cause, toxin, infectious trigger, diet, lifestyle factor, or FLII-specific gene–environment interaction has been reported. Consanguinity increases the probability that a rare recessive allele becomes homozygous but is not itself a biological cause. Viral illness and toxins belong in the differential diagnosis of pediatric DCM; they are not established triggers of CMD2J. Likewise, the common/low-frequency **rs8821, p.Arg1243His** susceptibility allele studied in adults and mice is not one of the four family alleles defining CMD2J. (kuwabara2023ahumanflii pages 2-3, kuwabara2023ahumanflii pages 1-2)

No genetic or environmental protective factor is established. Partial rescue of cardiac Flii-deletion phenotypes by LMOD2 overexpression in mice is mechanistic proof of principle, not evidence of a protective human allele or available therapy. (kuwabara2023ahumanflii pages 1-2)

## 3. Human phenotypes

All three known patients developed severe disease between **2 and 5 months**, making infantile onset the defining temporal feature. LVEF across the cohort was **23%–32%**. Two presented with overt heart failure and one with tachyarrhythmia; no subsequent arrhythmias or extracardiac abnormalities were reported. All were alive with stable or improved function at last review, ages 2, 6, and 9 years. (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4)

Suggested HPO annotations are:

- **Dilated cardiomyopathy — HP:0001644:** 3/3 reported; severe at presentation.
- **Left ventricular systolic dysfunction — HP:0100598:** 3/3, reflected by LVEF 23%–32%.
- **Infantile onset — HP:0003593:** 3/3, onset 2–5 months.
- **Heart failure — HP:0001635:** explicitly 2/3; likely clinically relevant to the third but should not be imputed.
- **Tachycardia/tachyarrhythmia — HP:0001649 or the most specific rhythm term available:** 1/3.
- **Secundum atrial septal defect — HP:0001684:** 1/3; uncertain whether integral to CMD2J or coincidental.
- **Cardiac chamber dilation — HP:0200127:** intrinsic to the DCM diagnosis.

No skeletal-muscle weakness, neurodevelopmental abnormality, dysmorphism, inflammatory syndrome, behavioral phenotype, or reproducible laboratory abnormality was described. “Not reported” should not be encoded as “absent” unless the source explicitly examined and excluded it. No disease-specific quality-of-life instrument, functional score, school-impact assessment, or caregiver-burden measure is available.

## 4. Genetic and molecular information

**Gene.** The causal gene is **FLII** (flightless-I homolog), represented in the primary report by transcript **NM_002018.3**. FLII combines an N-terminal leucine-rich-repeat region with six gelsolin-homology domains. The gelsolin-like region binds actin; FLII participates in actin capping/remodeling, focal adhesions, and sarcomeric organization. (kuwabara2023ahumanflii pages 2-3, strudwick2020multifunctionalrolesof pages 4-6, strudwick2020multifunctionalrolesof pages 3-4)

**Reported disease alleles.** Four germline alleles were observed:

1. c.1360C>T, **p.(Gln454Ter)**—protein-truncating, in compound heterozygosity.
2. c.3502C>T, **p.(Arg1168Trp)**—missense; gnomAD MAF 0.000024; compound heterozygous with p.Gln454Ter.
3. c.2020C>G, **p.(Leu674Val)**—homozygous missense; not reported in gnomAD in the source table.
4. c.3718C>T, **p.(Arg1240Cys)**—homozygous missense; gnomAD MAF 0.000057. (ruijmbeek2023biallelicvariantsin pages 4-5)

The missense substitutions affect conserved residues and were predicted damaging; CADD scores were 27, 31, and 26.1 for p.Arg1168Trp, p.Leu674Val, and p.Arg1240Cys, respectively. The source did not supply definitive ClinVar/ClinGen assertions or complete ACMG/AMP rule combinations in the extracted evidence. They should therefore not automatically be labeled “pathogenic” variant-by-variant solely because the gene–disease relationship is supported. (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4)

The alleles are inherited constitutional variants, not somatic mutations. No CMD2J-associated copy-number variant, translocation, inversion, aneuploidy, repeat expansion, mitochondrial variant, epigenetic signature, modifier gene, or founder haplotype is established. There is also no disease-specific methylome, transcriptome, proteome, metabolome, lipidome, single-cell, spatial-transcriptomic, or human myocardial multi-omic dataset.

## 5. Environmental information

No environmental, occupational, nutritional, behavioral, radiation, medication, or infectious cause has been associated specifically with FLII-related CMD2J. Smoking and alcohol are irrelevant as causal exposures in the reported infants. Standard investigation should nevertheless exclude myocarditis, metabolic disease, nutritional deficiency, toxic exposure, and abnormal loading conditions because these can phenocopy pediatric DCM; exclusion does not imply a demonstrated interaction with FLII.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic or loss-of-function FLII variants lead to reduced or altered flightless-I function in cardiomyocytes.** Complete loss appears more severe than the patient alleles in zebrafish. (ruijmbeek2023biallelicvariantsin pages 12-13, ruijmbeek2023biallelicvariantsin pages 8-11)
2. **Altered FLII leads to defective actin regulation and adhesion-complex organization** at intercalated-disk/costamere-like sites; abnormal vinculin and cadherin-2 localization directly demonstrates this branch in zebrafish. (ruijmbeek2023biallelicvariantsin pages 2-4, ruijmbeek2023biallelicvariantsin pages 8-11)
3. **Defective actin/adhesion regulation leads to myofibrillar disorganization and abnormal cardiomyocyte mechanical coupling.** (ruijmbeek2023biallelicvariantsin pages 12-13, ruijmbeek2023biallelicvariantsin pages 8-11)
4. **In parallel, FLII dysfunction leads to abnormal sarcomeric thin-filament length regulation through TMOD1 interaction/sequestration**—demonstrated in mouse cardiomyocytes and genetically modified mice, but not yet directly in patient myocardium. (kuwabara2023ahumanflii pages 2-3, kuwabara2023ahumanflii pages 1-2)
5. **Adhesion and cytoskeletal defects lead to impaired ventricular-wall morphogenesis and trabeculation**, with reduced Notch activity and reduced nuclear Wwtr1/Taz/Hippo-pathway output in zebrafish; whether signaling changes are primary or secondary remains incompletely resolved. (ruijmbeek2023biallelicvariantsin pages 12-13, ruijmbeek2023biallelicvariantsin pages 8-11)
6. **Abnormal chamber architecture and sarcomere function lead to reduced ventricular fractional-area change/ejection fraction and blood-flow velocity.** (ruijmbeek2023biallelicvariantsin pages 8-11)
7. **Reduced contractility leads to ventricular dilation and clinical systolic heart failure in infancy.** This final connection is supported by concordance between human DCM and the engineered models. (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 8-11)

### Mechanistic detail and ontology suggestions

FLII is a multifunctional actin-associated protein. Its gelsolin-homology domains bind G-actin/F-actin and can cap filament barbed ends; biochemical work indicates inhibition of polymerization without robust severing in several contexts. Its LRR region mediates protein interactions, including LRRFIP1/2, but the human disease alleles and causal locus here are **FLII itself**. (gorog2026flightlessiand pages 15-17, strudwick2020multifunctionalrolesof pages 4-6, strudwick2020multifunctionalrolesof pages 3-4)

The most relevant proposed GO biological-process terms are **actin filament organization**, **actin filament polymerization/depolymerization regulation**, **sarcomere organization**, **myofibril assembly**, **cell–cell adhesion**, **cell–matrix adhesion**, **cardiac muscle contraction**, **ventricular trabecula morphogenesis**, **Notch signaling**, and **Hippo signaling**. Suggested cellular components are **sarcomere**, **actin cytoskeleton**, **myofibril**, **focal adhesion**, **costamere**, **intercalated disc**, **adherens junction**, and **Z disc**. Exact GO identifiers should be ontology-validated before ingestion.

Primary cell type: **cardiomyocyte (CL:0000746)**, especially ventricular cardiomyocytes. Cardiac fibroblasts, endothelial cells, and immune cells have not been implicated directly in CMD2J. There is no demonstrated disease-specific apoptosis, autophagy, mitochondrial failure, metabolic reprogramming, fibrosis, inflammation, or immune activation in human tissue.

## 7. Anatomical structures affected

The primary organ is the **heart**, particularly **ventricular myocardium**, left ventricle, ventricular wall/trabeculae, and cardiomyocyte contractile/adhesion structures. Suggested anatomy mappings include **UBERON:0000948 heart**, **UBERON:0002084 heart left ventricle**, ventricular myocardium, interventricular/cardiac septal structures, and atrial septum for the single ASD-II case. Laterality is not applicable. Secondary lung, liver, or kidney involvement from congestion was not reported in the three patients.

At subcellular resolution, relevant sites are sarcomeric thin filaments, myofibrils, intercalated-disk/costamere-like adhesion complexes, focal adhesions, and adherens junctions. Flii localized to cardiac sarcomeres in mouse studies and to intercalated-disk/costamere-like adhesions in zebrafish. (ruijmbeek2023biallelicvariantsin pages 2-4, kuwabara2023ahumanflii pages 2-3)

## 8. Temporal development and natural history

Onset was uniformly early and clustered at 2–5 months. The presentation may be acute—heart failure or tachyarrhythmia—but the underlying developmental cytoskeletal defect is congenital. Patient-specific zebrafish alleles behaved as milder hypomorphs, whereas a null-like allele caused severe wall-morphogenesis defects, systolic failure, and larval death. This supports a dosage/severity continuum but does not establish a human stage system. (ruijmbeek2023biallelicvariantsin pages 8-11)

The three children survived to ages 2–9 with stable or improved cardiac function; therefore, CMD2J is not invariably lethal in infancy. Remission rates, relapse, adult course, pregnancy risk, arrhythmia burden, and critical treatment windows remain unknown. Early infancy is the clearest period of vulnerability.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous carrier parents, each pregnancy has a theoretical 25% affected, 50% carrier, and 25% noncarrier probability, subject to confirmation of parental phase and molecular diagnosis. Heterozygous parents were clinically unaffected, and heterozygous Flii-null mice lacked a reported cardiac phenotype. (ruijmbeek2023biallelicvariantsin pages 2-4, kuwabara2023ahumanflii pages 2-3)

Only three affected individuals—two females and one male—are known from the defining series, precluding sex-ratio, penetrance, expressivity, anticipation, germline-mosaicism, prevalence, or incidence estimates. Two children were Saudi Arabian from consanguineous families and one was Dutch from a nonconsanguineous family. This is ascertainment evidence, not proof of ethnic predisposition or founder effect. (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4)

For context only, general pediatric DCM prevalence is estimated at **0.57–1.13 per 100,000 children**, rising to **8.34 per 100,000 infants**; these values must not be assigned to CMD2J. General pediatric DCM has a median diagnosis age of 1.5 years, with 41% diagnosed in the first year. (malinow2024pediatricdilatedcardiomyopathy pages 2-3)

## 10. Diagnostics

### Disease-specific approach

1. Establish DCM by history, examination, ECG, and echocardiography showing ventricular dilation and systolic dysfunction not explained by loading conditions.
2. Evaluate reversible/acquired and syndromic causes: myocarditis, coronary anomaly, congenital loading lesion, metabolic/mitochondrial disease, neuromuscular disease, endocrine/nutritional disorder, and toxin exposure.
3. Perform trio-based cardiomyopathy sequencing with robust **FLII** coverage. A contemporary panel may be used only if FLII is included; otherwise WES/WGS is preferable.
4. Confirm candidate variants and phase by Sanger sequencing or an equivalent orthogonal method; interpret under ACMG/AMP criteria with recessive segregation, population frequency, predicted consequence, and functional evidence.
5. Once biallelic causal variants are established, offer targeted familial testing and cardiac evaluation of siblings. (ruijmbeek2023biallelicvariantsin pages 12-13, malinow2024pediatricdilatedcardiomyopathy pages 3-4)

Echocardiographic measurements should include LV dimensions/z-scores, fractional shortening, LVEF, mitral regurgitation, and serial remodeling. ECG/Holter monitoring is reasonable given the tachyarrhythmia in one patient. CMR can characterize anatomy, function, edema, inflammation, iron, or fibrosis but is not mandatory for diagnosis and lacks fully standardized pediatric monitoring methods. BNP/NT-proBNP and troponin can support heart-failure assessment but are not CMD2J-specific biomarkers. (malinow2024pediatricdilatedcardiomyopathy pages 9-10, malinow2024pediatricdilatedcardiomyopathy pages 3-4)

RNA sequencing may help resolve suspected splice variants or variants of uncertain significance but has not been reported for CMD2J. CMA, karyotyping, FISH, mtDNA testing, and repeat-expansion assays are not first-line FLII tests unless clinical findings suggest an alternative diagnosis. No biochemical FLII enzyme assay, biopsy hallmark, newborn screen, or liquid-biopsy test exists.

**Differential diagnosis.** Important genetic alternatives include other infantile sarcomeric/cytoskeletal DCMs, metabolic and mitochondrial cardiomyopathies, Barth syndrome, neuromuscular disease, myocarditis, and congenital structural lesions. FLNC-related DCM is generally a different gene–disease entity and must not be conflated with FLII.

## 11. Outcome and prognosis

All three reported CMD2J patients were alive with stable or improved function at last follow-up, but three observations cannot support survival estimates. No transplant, ventricular-assist-device use, sudden death, or extracardiac disability was reported in the extracted cases. (ruijmbeek2023biallelicvariantsin pages 4-5, ruijmbeek2023biallelicvariantsin pages 2-4)

General pediatric DCM has substantially worse aggregate outcomes: nearly 40% undergo transplantation or die within two years, while reported transplant-free survival is 69%, 54%, and 46% at 1, 5, and 10 years. These figures are contextual and may overstate risk for treated CMD2J, whose known patients improved or stabilized. (malinow2024pediatricdilatedcardiomyopathy pages 1-2, malinow2024pediatricdilatedcardiomyopathy pages 7-8)

General prognostic markers include larger LVEDD, lower LVEF/fractional shortening, and severe mitral regurgitation. Disease-specific prognostic biomarkers are unavailable. (malinow2024pediatricdilatedcardiomyopathy pages 7-8)

## 12. Treatment and applications

There is **no FLII-directed approved therapy**, genotype-specific clinical protocol, pharmacogenomic recommendation, gene therapy, RNA therapy, CRISPR trial, or registered FLII cardiomyopathy trial identified.

Management should follow pediatric systolic-heart-failure practice under a specialist cardiomyopathy team. Depending on congestion, blood pressure, renal function, and age, treatment commonly includes diuretics, ACE inhibitors/ARBs, beta-blockers, and mineralocorticoid-receptor antagonists. Ivabradine, sacubitril/valsartan, and SGLT2 inhibitors may be considered in selected children, but pediatric evidence is limited and much practice is extrapolated from adults. Acute decompensation may require inotropes such as milrinone; refractory stage-D disease may require ECMO, VAD, transplantation, or palliation. (malinow2024pediatricdilatedcardiomyopathy pages 9-10, malinow2024pediatricdilatedcardiomyopathy pages 8-9)

Suggested NCIT intervention concepts include **heart-failure pharmacotherapy**, **diuretic therapy**, **ACE-inhibitor therapy**, **beta-blocker therapy**, **mineralocorticoid-receptor-antagonist therapy**, **mechanical circulatory support**, **ventricular-assist device**, **extracorporeal membrane oxygenation**, and **heart transplantation**; exact NCIT codes should be validated before ingestion.

In general pediatric DCM cohorts, transplant occurred in 22%, 27%, and 29% by 1, 3, and 5 years, with post-transplant survival of 92% at one year and 80% at five years. These are not CMD2J-specific response rates. (malinow2024pediatricdilatedcardiomyopathy pages 8-9)

The LMOD2 rescue experiment and manipulation of FLII–TMOD1 biology are attractive research directions, but systemic alteration of actin regulation could have substantial safety risks. No human efficacy or toxicology data justify clinical use. (kuwabara2023ahumanflii pages 1-2)

## 13. Prevention

Primary prevention cannot eliminate a spontaneously inherited allele through lifestyle change. Reproductive options after molecular confirmation include genetic counseling, carrier testing of relatives, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Population carrier screening and newborn screening are not established.

Secondary prevention consists of presymptomatic cascade testing and cardiac surveillance in at-risk siblings. General familial-DCM guidance suggests screening first-degree relatives annually at ages 0–5, every 1–2 years at 6–12, and every 1–3 years at 13–19, individualized for genotype and family course. (malinow2024pediatricdilatedcardiomyopathy pages 3-4)

Tertiary prevention includes early guideline-directed heart-failure therapy, rhythm surveillance, vaccination and prompt treatment of intercurrent infection according to routine pediatric practice, avoidance of cardiotoxic exposures, and timely referral for advanced support. Vaccination prevents infection-related decompensation but does not prevent the genetic disorder.

## 14. Other species and natural disease

No naturally occurring FLII-related CMD2J-like veterinary disorder, breed predisposition, zoonotic transmission, or cross-species infectious risk was identified. The disorder is noncommunicable.

Relevant experimental taxa are **Homo sapiens (NCBI Taxon 9606)**, **Danio rerio (7955)**, **Mus musculus (10090)**, and historically **Drosophila melanogaster (7227)**. Orthologous flightless-I proteins are evolutionarily conserved, supporting comparative functional inference, but model phenotypes are induced genetically rather than documented natural veterinary disease.

## 15. Model organisms

**Zebrafish—strongest disease-specific model.** CRISPR/Cas9 patient-mimicking alleles reproduced reduced ventricular contractility, abnormal trabeculation, myofibril disorganization, and adhesion defects. Null-like flii loss caused more severe systolic failure and larval lethality, while patient-specific alleles allowed survival, supporting hypomorphic effects. Altered vinculin, cadherin-2, Notch, and Wwtr1/Taz localization/activity supplied mechanistic resolution. Limitations include the two-chambered fish heart, regenerative capacity, and differences in hemodynamic load. (ruijmbeek2023biallelicvariantsin pages 12-13, ruijmbeek2023biallelicvariantsin pages 8-11)

**Mouse—complementary cardiac model.** Cardiac Flii deletion shortened sarcomeric actin filaments and caused hypertrophy, impaired ventricular performance, pulmonary congestion, heart failure, and early death. The syntenic knock-in corresponding to human rs8821 p.Arg1243His also shortened thin filaments and increased susceptibility to cardiomyopathy. The PNAS abstract summarizes: **“the Flii gene regulates sarcomeric actin thin filament length by sequestering tropomodulin-1.”** These models establish a cardiac structural role for FLII but do not model the exact three CMD2J genotypes or prove the same thin-filament lesion in human myocardium. Published May 2023; DOI [10.1073/pnas.2213696120](https://doi.org/10.1073/pnas.2213696120). (kuwabara2023ahumanflii pages 2-3, kuwabara2023ahumanflii pages 1-2)

**Drosophila.** Flightless-I studies support conserved barbed-end/Z-disc actin regulation and myofibril growth, but they are more remote comparative-mechanistic evidence. LRRFIP cooperation in flies does not make LRRFIP a demonstrated cause of CMD2J. (gorog2026flightlessiand pages 21-28, gorog2026flightlessiand pages 15-17, gorog2026flightlessiand pages 12-15)

No patient-derived iPSC-cardiomyocyte, cardiac organoid, humanized exact-variant mouse, large-animal model, or therapeutic CRISPR screen was identified.

## Overall assessment and priority knowledge gaps

CMD2J is best represented as a **very rare, autosomal-recessive, infantile-onset, predominantly isolated DCM caused by biallelic FLII variants**. The mechanistic center is defective cardiomyocyte actin/myofibril organization and adhesion, with downstream ventricular morphogenesis, Notch/Hippo, and contractile abnormalities. Evidence is strongest for gene causality and zebrafish phenocopy; human tissue-level mechanism and long-term clinical behavior remain uncertain. (ruijmbeek2023biallelicvariantsin pages 2-4, ruijmbeek2023biallelicvariantsin pages 8-11)

The highest priorities are additional case ascertainment, standardized ACMG/ClinVar deposition, longitudinal rhythm and imaging surveillance, patient-derived cardiomyocytes, direct measurement of human thin-filament length and adhesion complexes, and development of exact-variant mammalian models. Disease-specific prevalence, penetrance, carrier frequency, quality of life, adult outcomes, and treatment-response data are currently unavailable.

References

1. (ruijmbeek2023biallelicvariantsin pages 2-4): Claudine W.B. Ruijmbeek, Filomena Housley, Hafiza Idrees, Michael P. Housley, Jenny Pestel, Leonie Keller, Jason K.H. Lai, Herma C. van der Linde, Rob Willemsen, Janett Piesker, Zuhair N. Al-Hassnan, Abdulrahman Almesned, Michiel Dalinghaus, Lisa M. van den Bersselaar, Marjon A. van Slegtenhorst, Federico Tessadori, Jeroen Bakkers, Tjakko J. van Ham, Didier Y.R. Stainier, Judith M.A. Verhagen, and Sven Reischauer. Biallelic variants in flii cause pediatric cardiomyopathy by disrupting cardiomyocyte cell adhesion and myofibril organization. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168247, doi:10.1172/jci.insight.168247. This article has 10 citations and is from a domain leading peer-reviewed journal.

2. (ruijmbeek2023biallelicvariantsin pages 1-2): Claudine W.B. Ruijmbeek, Filomena Housley, Hafiza Idrees, Michael P. Housley, Jenny Pestel, Leonie Keller, Jason K.H. Lai, Herma C. van der Linde, Rob Willemsen, Janett Piesker, Zuhair N. Al-Hassnan, Abdulrahman Almesned, Michiel Dalinghaus, Lisa M. van den Bersselaar, Marjon A. van Slegtenhorst, Federico Tessadori, Jeroen Bakkers, Tjakko J. van Ham, Didier Y.R. Stainier, Judith M.A. Verhagen, and Sven Reischauer. Biallelic variants in flii cause pediatric cardiomyopathy by disrupting cardiomyocyte cell adhesion and myofibril organization. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168247, doi:10.1172/jci.insight.168247. This article has 10 citations and is from a domain leading peer-reviewed journal.

3. (lipov2023exploringthecomplex pages 3-4): Alex Lipov, Sean J. Jurgens, Francesco Mazzarotto, Mona Allouba, James P. Pirruccello, Yasmine Aguib, Massimo Gennarelli, Magdi H. Yacoub, Patrick T. Ellinor, Connie R. Bezzina, and Roddy Walsh. Exploring the complex spectrum of dominance and recessiveness in genetic cardiomyopathies. Nature Cardiovascular Research, 2:1078-1094, Oct 2023. URL: https://doi.org/10.1038/s44161-023-00346-3, doi:10.1038/s44161-023-00346-3. This article has 40 citations and is from a peer-reviewed journal.

4. (ruijmbeek2023biallelicvariantsin pages 4-5): Claudine W.B. Ruijmbeek, Filomena Housley, Hafiza Idrees, Michael P. Housley, Jenny Pestel, Leonie Keller, Jason K.H. Lai, Herma C. van der Linde, Rob Willemsen, Janett Piesker, Zuhair N. Al-Hassnan, Abdulrahman Almesned, Michiel Dalinghaus, Lisa M. van den Bersselaar, Marjon A. van Slegtenhorst, Federico Tessadori, Jeroen Bakkers, Tjakko J. van Ham, Didier Y.R. Stainier, Judith M.A. Verhagen, and Sven Reischauer. Biallelic variants in flii cause pediatric cardiomyopathy by disrupting cardiomyocyte cell adhesion and myofibril organization. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168247, doi:10.1172/jci.insight.168247. This article has 10 citations and is from a domain leading peer-reviewed journal.

5. (ruijmbeek2023biallelicvariantsin pages 12-13): Claudine W.B. Ruijmbeek, Filomena Housley, Hafiza Idrees, Michael P. Housley, Jenny Pestel, Leonie Keller, Jason K.H. Lai, Herma C. van der Linde, Rob Willemsen, Janett Piesker, Zuhair N. Al-Hassnan, Abdulrahman Almesned, Michiel Dalinghaus, Lisa M. van den Bersselaar, Marjon A. van Slegtenhorst, Federico Tessadori, Jeroen Bakkers, Tjakko J. van Ham, Didier Y.R. Stainier, Judith M.A. Verhagen, and Sven Reischauer. Biallelic variants in flii cause pediatric cardiomyopathy by disrupting cardiomyocyte cell adhesion and myofibril organization. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168247, doi:10.1172/jci.insight.168247. This article has 10 citations and is from a domain leading peer-reviewed journal.

6. (ruijmbeek2023biallelicvariantsin pages 8-11): Claudine W.B. Ruijmbeek, Filomena Housley, Hafiza Idrees, Michael P. Housley, Jenny Pestel, Leonie Keller, Jason K.H. Lai, Herma C. van der Linde, Rob Willemsen, Janett Piesker, Zuhair N. Al-Hassnan, Abdulrahman Almesned, Michiel Dalinghaus, Lisa M. van den Bersselaar, Marjon A. van Slegtenhorst, Federico Tessadori, Jeroen Bakkers, Tjakko J. van Ham, Didier Y.R. Stainier, Judith M.A. Verhagen, and Sven Reischauer. Biallelic variants in flii cause pediatric cardiomyopathy by disrupting cardiomyocyte cell adhesion and myofibril organization. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168247, doi:10.1172/jci.insight.168247. This article has 10 citations and is from a domain leading peer-reviewed journal.

7. (kuwabara2023ahumanflii pages 2-3): Yasuhide Kuwabara, Allen J. York, Suh-Chin Lin, Michelle A. Sargent, Kelly M. Grimes, James P. Pirruccello, and Jeffery D. Molkentin. A human flii gene variant alters sarcomeric actin thin filament length and predisposes to cardiomyopathy. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2213696120, doi:10.1073/pnas.2213696120. This article has 16 citations and is from a highest quality peer-reviewed journal.

8. (kuwabara2023ahumanflii pages 1-2): Yasuhide Kuwabara, Allen J. York, Suh-Chin Lin, Michelle A. Sargent, Kelly M. Grimes, James P. Pirruccello, and Jeffery D. Molkentin. A human flii gene variant alters sarcomeric actin thin filament length and predisposes to cardiomyopathy. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2213696120, doi:10.1073/pnas.2213696120. This article has 16 citations and is from a highest quality peer-reviewed journal.

9. (malinow2024pediatricdilatedcardiomyopathy pages 9-10): Ian Malinow, Daniel C. Fong, Matthew Miyamoto, Sarah Badran, and Charles C. Hong. Pediatric dilated cardiomyopathy: a review of current clinical approaches and pathogenesis. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1404942, doi:10.3389/fped.2024.1404942. This article has 41 citations.

10. (strudwick2020multifunctionalrolesof pages 4-6): Xanthe L. Strudwick and Allison J. Cowin. Multifunctional roles of the actin-binding protein flightless i in inflammation, cancer and wound healing. Frontiers in Cell and Developmental Biology, Nov 2020. URL: https://doi.org/10.3389/fcell.2020.603508, doi:10.3389/fcell.2020.603508. This article has 41 citations.

11. (strudwick2020multifunctionalrolesof pages 3-4): Xanthe L. Strudwick and Allison J. Cowin. Multifunctional roles of the actin-binding protein flightless i in inflammation, cancer and wound healing. Frontiers in Cell and Developmental Biology, Nov 2020. URL: https://doi.org/10.3389/fcell.2020.603508, doi:10.3389/fcell.2020.603508. This article has 41 citations.

12. (gorog2026flightlessiand pages 15-17): Péter Görög, Krisztina Tóth, Dávid Farkas, Balázs Vedelek, Tamás F. Polgár, Anna Zsuzsanna Tihanyi, Péter Bíró, Tibor Novák, Johannes Salomonsson, Kristina Djinovic Carugo, Aladár Pettkó-Szandtner, Zsuzsanna Darula, Miklós Erdélyi, Szilárd Szikora, and József Mihály. Flightless i and lrrfip work together to regulate lateral growth of the sarcomeres in <i>drosophila</i>. Jun 2026. URL: https://doi.org/10.64898/2026.06.02.729301, doi:10.64898/2026.06.02.729301. This article has 0 citations.

13. (malinow2024pediatricdilatedcardiomyopathy pages 2-3): Ian Malinow, Daniel C. Fong, Matthew Miyamoto, Sarah Badran, and Charles C. Hong. Pediatric dilated cardiomyopathy: a review of current clinical approaches and pathogenesis. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1404942, doi:10.3389/fped.2024.1404942. This article has 41 citations.

14. (malinow2024pediatricdilatedcardiomyopathy pages 3-4): Ian Malinow, Daniel C. Fong, Matthew Miyamoto, Sarah Badran, and Charles C. Hong. Pediatric dilated cardiomyopathy: a review of current clinical approaches and pathogenesis. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1404942, doi:10.3389/fped.2024.1404942. This article has 41 citations.

15. (malinow2024pediatricdilatedcardiomyopathy pages 1-2): Ian Malinow, Daniel C. Fong, Matthew Miyamoto, Sarah Badran, and Charles C. Hong. Pediatric dilated cardiomyopathy: a review of current clinical approaches and pathogenesis. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1404942, doi:10.3389/fped.2024.1404942. This article has 41 citations.

16. (malinow2024pediatricdilatedcardiomyopathy pages 7-8): Ian Malinow, Daniel C. Fong, Matthew Miyamoto, Sarah Badran, and Charles C. Hong. Pediatric dilated cardiomyopathy: a review of current clinical approaches and pathogenesis. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1404942, doi:10.3389/fped.2024.1404942. This article has 41 citations.

17. (malinow2024pediatricdilatedcardiomyopathy pages 8-9): Ian Malinow, Daniel C. Fong, Matthew Miyamoto, Sarah Badran, and Charles C. Hong. Pediatric dilated cardiomyopathy: a review of current clinical approaches and pathogenesis. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1404942, doi:10.3389/fped.2024.1404942. This article has 41 citations.

18. (gorog2026flightlessiand pages 21-28): Péter Görög, Krisztina Tóth, Dávid Farkas, Balázs Vedelek, Tamás F. Polgár, Anna Zsuzsanna Tihanyi, Péter Bíró, Tibor Novák, Johannes Salomonsson, Kristina Djinovic Carugo, Aladár Pettkó-Szandtner, Zsuzsanna Darula, Miklós Erdélyi, Szilárd Szikora, and József Mihály. Flightless i and lrrfip work together to regulate lateral growth of the sarcomeres in <i>drosophila</i>. Jun 2026. URL: https://doi.org/10.64898/2026.06.02.729301, doi:10.64898/2026.06.02.729301. This article has 0 citations.

19. (gorog2026flightlessiand pages 12-15): Péter Görög, Krisztina Tóth, Dávid Farkas, Balázs Vedelek, Tamás F. Polgár, Anna Zsuzsanna Tihanyi, Péter Bíró, Tibor Novák, Johannes Salomonsson, Kristina Djinovic Carugo, Aladár Pettkó-Szandtner, Zsuzsanna Darula, Miklós Erdélyi, Szilárd Szikora, and József Mihály. Flightless i and lrrfip work together to regulate lateral growth of the sarcomeres in <i>drosophila</i>. Jun 2026. URL: https://doi.org/10.64898/2026.06.02.729301, doi:10.64898/2026.06.02.729301. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Cardiomyopathy_Dilated_2J-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.
