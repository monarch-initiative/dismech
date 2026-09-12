---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T10:06:06.403361'
end_time: '2026-09-01T10:18:33.441161'
duration_seconds: 747.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hearing Loss Autosomal Dominant 82 (DFNA82, ATP2B2-related)
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 18
  verified: 18
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
  path: Hearing_Loss_Autosomal_Dominant_82-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Dominant 82 (DFNA82, ATP2B2-related)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 82 (DFNA82, ATP2B2-related)** covering all of the
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
- **Disease Name:** Hearing Loss Autosomal Dominant 82 (DFNA82, ATP2B2-related)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 82 (DFNA82, ATP2B2-related)** covering all of the
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


# Hearing Loss, Autosomal Dominant 82 (DFNA82; ATP2B2-related)

## Executive summary

DFNA82 is an exceptionally rare, usually nonsyndromic, autosomal-dominant sensorineural hearing-loss disorder caused by heterozygous loss-of-function variants in **ATP2B2**, which encodes plasma-membrane Ca²⁺-ATPase 2 (**PMCA2**). The defining human series described five unrelated Dutch or Polish families and 11 clinically evaluated affected people. Most passed newborn hearing screening, developed bilateral high-frequency hearing loss at approximately 2–6 years, and then experienced rapid progression, sometimes to severe or profound loss. PMCA2 normally exports Ca²⁺ from cochlear hair-cell stereocilia into endolymph; reduced dosage disrupts stereociliary Ca²⁺ homeostasis and is inferred from mouse models to produce outer-hair-cell dysfunction followed by basal cochlear hair-cell degeneration. Vestibular dysfunction, structural inner-ear abnormalities, and systemic manifestations were not characteristic of the original DFNA82 cohort. The evidence base remains small, and no disease-specific therapy or clinical trial was identified.

The principal primary paper is Smits et al., *Human Genetics*, published online **8 December 2018** and in the **January 2019** issue, DOI [10.1007/s00439-018-1965-1](https://doi.org/10.1007/s00439-018-1965-1), PMID **30535804**. Its abstract states: “After normal newborn hearing screening, a rapidly progressive high-frequency hearing impairment was diagnosed at the age of about 3–6 years” and concludes that the findings “indicate a monogenic cause of hearing impairment in cases with loss-of-function variants of ATP2B2.” (smits2019denovoand pages 1-2)

| Evidence category | Finding | Quantitative/detail | Evidence type/source |
|---|---|---|---|
| Core monogenic report | ATP2B2 loss-of-function variants define ATP2B2-related autosomal dominant hearing loss (DFNA82) | Five heterozygous variants across five families: c.397+1G>A, c.955delG p.Ala319fs, c.1963G>T p.Glu655*, c.1998C>A p.Cys666*, c.2329C>T p.Arg777* (smits2019denovoand pages 1-2, smits2019denovoand pages 4-5) | Human clinical genetics, WES/segregation; Smits et al. 2019 (smits2019denovoand pages 1-2, smits2019denovoand pages 4-5) |
| Inheritance | Mixed de novo and familial autosomal dominant transmission | Two variants de novo (c.955delG, c.1963G>T); three in families with autosomal dominant inheritance (smits2019denovoand pages 1-2, smits2019denovoand pages 4-5) | Human pedigree/segregation (smits2019denovoand pages 1-2, smits2019denovoand pages 4-5) |
| Cohort size | Clinically characterized affected subjects | 11 clinically evaluated affected individuals; ages 6-68 years in analyzed cohort (smits2019denovoand pages 5-7, smits2019denovoand pages 4-5) | Human clinical series (smits2019denovoand pages 5-7, smits2019denovoand pages 4-5) |
| Onset/screening | Early childhood onset despite normal newborn screening | All four screened subjects passed newborn screening; diagnosis typically followed at ~2-6 years, with most onset in first decade; one outlier reported onset at 55 years (smits2019denovoand pages 1-2, smits2019denovoand pages 5-7, smits2019denovoand pages 7-9) | Human audiology/natural history (smits2019denovoand pages 1-2, smits2019denovoand pages 5-7, smits2019denovoand pages 7-9) |
| Audiometric phenotype | Nonsyndromic progressive SNHL with characteristic configuration | Bilateral, sensorineural, symmetric, mild-to-profound loss; audiograms typically (steeply) downsloping with high frequencies most affected (smits2019denovoand pages 5-7, smits2019denovoand pages 7-9) | Human audiometry (smits2019denovoand pages 5-7, smits2019denovoand pages 7-9) |
| Progression | Quantified annual deterioration | Average annual threshold deterioration ages 10-70 years: 0.5 dB/year low frequencies, 1.1 dB/year middle, 0.7 dB/year high (smits2019denovoand pages 5-7) | Cross-sectional ARTA analysis in human cohort (smits2019denovoand pages 5-7) |
| Imaging | No structural inner-ear or retrocochlear abnormality | CT/MRI in five subjects showed normal temporal bone/cochlear anatomy and no retrocochlear pathology (except unrelated operated ear findings) (smits2019denovoand pages 1-2, smits2019denovoand pages 5-7) | Human radiology/clinical workup (smits2019denovoand pages 1-2, smits2019denovoand pages 5-7) |
| Vestibular findings | Vestibular function essentially normal in heterozygotes | No balance complaints overall; extensive testing showed only minor/nonspecific abnormalities, with no clear ATP2B2-related vestibular dysfunction (smits2019denovoand pages 1-2, smits2019denovoand pages 9-10) | Human vestibular phenotyping (smits2019denovoand pages 1-2, smits2019denovoand pages 9-10) |
| Population frequency | Variants are ultra-rare/absent in reference datasets | None of the five variants present in gnomAD v2.02 or an in-house database of ~20,000 exomes (smits2019denovoand pages 4-5) | Human population genetics/filtering (smits2019denovoand pages 4-5) |
| Molecular mechanism | Loss of PMCA2 function is the likely disease mechanism | Variants affect exons/splice sites encoding the PMCA2 w/a ortholog; 4/5 predicted to trigger nonsense-mediated decay; distribution supports haploinsufficiency (smits2019denovoand pages 1-2, smits2019denovoand pages 7-9) | Human molecular interpretation supported by model-organism biology (smits2019denovoand pages 1-2, smits2019denovoand pages 7-9) |
| Cochlear biology | PMCA2 is a stereociliary Ca2+ pump required for hair-cell ion homeostasis | PMCA2 extrudes Ca2+ from stereocilia to endolymph; w/a isoform is highly abundant in OHC stereocilia and present apically in IHCs (smits2019denovoand pages 1-2, smits2019denovoand pages 9-10) | Mechanistic synthesis from human report citing prior auditory biology (smits2019denovoand pages 1-2, smits2019denovoand pages 9-10) |
| Model support | Mouse dosage effects mirror the human phenotype | Heterozygous Atp2b2 loss-of-function mice show rapidly progressive early-onset high-frequency hearing loss; homozygotes typically have severe hearing and vestibular/ataxic phenotypes (smits2019denovoand pages 1-2, smits2019denovoand pages 7-9, smits2019denovoand pages 10-11) | Model-organism evidence (mouse) (smits2019denovoand pages 1-2, smits2019denovoand pages 7-9, smits2019denovoand pages 10-11) |
| Genetic interaction context | Distinguish monogenic DFNA82 from earlier modifier evidence | ATP2B2 p.Val586Met is a hypofunctional PMCA2 allele reported as a modifier/digenic contributor with CDH23-related hearing loss, not the core monogenic DFNA82 mechanism established by ATP2B2 loss-of-function alleles (schultz2005modificationofhuman pages 3-4, schultz2005modificationofhuman pages 4-6, smits2019denovoand pages 1-2) | Human modifier study vs later monogenic clinical-genetic study (schultz2005modificationofhuman pages 3-4, schultz2005modificationofhuman pages 4-6, smits2019denovoand pages 1-2) |


*Table: This table condenses the key human and supporting model evidence defining ATP2B2-related autosomal dominant hearing loss (DFNA82). It separates the core monogenic loss-of-function evidence from the earlier ATP2B2 p.Val586Met modifier/digenic report.*

## 1. Disease information

### Definition and names

**Preferred name:** Hearing loss, autosomal dominant 82.  
**Synonyms:** DFNA82; ATP2B2-related autosomal-dominant nonsyndromic hearing loss; ATP2B2-related progressive sensorineural hearing impairment; PMCA2-related hearing loss.

The condition should be distinguished from: (1) **ATP2B2 as a modifier/digenic contributor** to CDH23-related deafness, and (2) recently emerging, generally missense-variant ATP2B2-associated neurodevelopmental/cerebellar phenotypes, which are not equivalent to classic nonsyndromic DFNA82.

### Identifiers

* **Gene:** ATP2B2; approved name *ATPase plasma membrane Ca²⁺ transporting 2*; Ensembl **ENSG00000157087**; chromosomal locus **3p25.3**. Open Targets associates ATP2B2 with autosomal-dominant nonsyndromic hearing loss, whose umbrella MONDO identifier is **MONDO:0019587**. A DFNA82-specific MONDO identifier was not recoverable from the searched evidence and should not be inferred from the umbrella term. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss-ATP2B2, zhang2019researchanddiscussion pages 1-2)
* **OMIM/Orphanet:** A disease-specific accession was not reliably recovered by the available tools. These fields should be populated only after direct verification in OMIM/Orphanet; the ATP2B2 gene record must not be substituted for a disease record.
* **ICD-10/ICD-11 and MeSH:** No DFNA82-specific code exists in the retrieved evidence. Use the appropriate generic code for bilateral sensorineural hearing loss, supplemented by the molecular diagnosis.

The source evidence is **aggregated disease-level literature and family-based research**, not individual EHR data. The foundational report aggregated five pedigrees evaluated through specialist genetics, audiology, vestibular, and imaging services. (smits2019denovoand pages 1-2, smits2019denovoand pages 4-5)

## 2. Etiology, risk, and protective factors

### Primary cause

The established cause is a **heterozygous germline ATP2B2 loss-of-function allele**, usually nonsense, frameshift, or canonical splice-site, acting predominantly through **haploinsufficiency**. Four of the five original variants were predicted to truncate PMCA2; three were expected to undergo nonsense-mediated decay. ATP2B2 had a reported pLI of 1.00, supporting marked intolerance of loss-of-function variation. (smits2019denovoand pages 5-7, smits2019denovoand pages 7-9)

### Genetic modifiers

**CDH23** is the best-supported modifier candidate. The earlier p.Val586Met PMCA2 allele reduced pump activity to about 50% and aggravated hearing loss in people homozygous for CDH23 p.Phe1888Ser; it did not establish classic monogenic DFNA82. Mouse Atp2b2–Cdh23 interactions independently support this modifier relationship. (schultz2005modificationofhuman pages 4-6, schultz2005modificationofhuman pages 3-4)

The 2019 DFNA82 cohort did not require pathogenic CDH23 variants: rare CDH23 findings failed segregation or had benign/VUS interpretations, supporting monogenic ATP2B2 loss of function. A MYO6 variant in one family could not be completely excluded as a modifier but did not explain the shared phenotype across families. (smits2019denovoand pages 5-7, smits2019denovoand pages 7-9)

### Environmental and lifestyle risks

No affected person in the defining series reported excessive noise, prolonged antibiotic exposure, meningitis, or head trauma, so these were not necessary causes. Nevertheless, avoiding noise and ototoxic agents is biologically reasonable because reduced PMCA2 reserve may increase cochlear vulnerability. In a separate case-control study of **760 Chinese textile workers**—not DFNA82 patients—the ATP2B2 rs3209637 C allele was associated with noise-induced hearing loss (OR 1.67, 95% CI 1.08–2.58); among workers exposed above 95 dB, reported susceptibility was OR 1.34 (95% CI 1.07–1.68). Interactions involving ATP2B2 polymorphisms, smoking, and alcohol were also reported, but these common-variant associations cannot be directly extrapolated to rare DFNA82 alleles. (smits2019denovoand pages 4-5, zhang2019researchanddiscussion pages 1-2)

No validated genetic or environmental **protective factor** is known. Hearing protection reduces an avoidable superimposed insult but does not prevent inheritance or the intrinsic progression. A 2024 developmental mouse study suggested thyroid hormone regulation of cochlear Atp2b2 expression; this remains preclinical and does not establish thyroid supplementation as prevention or treatment for DFNA82. (gregersen2024localizationandquantification pages 59-63, gregersen2024localizationandquantificationa pages 59-63)

## 3. Phenotypes

### Core phenotype

* **Bilateral sensorineural hearing impairment** — symptom/sign; typically symmetric, mild through profound depending on age; suggested HPO **Sensorineural hearing impairment (HP:0000407)** and **Bilateral sensorineural hearing impairment (HP:0008619)**.
* **High-frequency-predominant/downsloping loss** — clinical audiometric sign; suggested HPO **High-frequency hearing impairment (HP:0005101)**.
* **Progressive hearing impairment** — temporal characteristic; suggested HPO **Progressive hearing impairment (HP:0001730)**.
* **Childhood onset** — usually recognized at 2–6 years after a normal newborn screen; suggested HPO **Childhood onset (HP:0011463)**. One person reported onset at 55 years, indicating substantial age-dependent variability. (smits2019denovoand pages 1-2, smits2019denovoand pages 5-7)

Among 11 evaluated affected subjects, loss was generally bilateral, symmetric, sensorineural, and steeply downsloping. Severity ranged from mild to profound. Cross-sectional age-related analysis estimated annual threshold deterioration from ages 10–70 of **0.5 dB/year at 250–500 Hz, 1.1 dB/year at 1–2 kHz, and 0.7 dB/year at 4–8 kHz**. Four of four screened newborns passed; the screening method may miss thresholds below approximately 35 dB HL or loss predominantly above 4 kHz. (smits2019denovoand pages 5-7, smits2019denovoand pages 7-9)

Delayed speech development and school difficulty prompted hearing assessment in several children. Suggested HPO terms are **Delayed speech and language development (HP:0000750)** and **Learning difficulty (HP:0001328)**, but these are secondary functional consequences rather than invariant primary manifestations. Two subjects reported tinnitus—suggested **Tinnitus (HP:0000360)**—so frequency is uncertain. (smits2019denovoand pages 4-5, smits2019denovoand pages 7-9)

### Findings usually absent

Vestibular complaints were not characteristic; extensive oculomotor, caloric, rotational-chair, video-head-impulse, and vestibular-evoked-myogenic-potential testing yielded no convincing ATP2B2-related vestibulopathy. CT/MRI showed no structural inner-ear or retrocochlear pathology. Thus **vertigo, vestibular areflexia, and inner-ear malformation should not be asserted as core DFNA82 phenotypes**. (smits2019denovoand pages 9-10, smits2019denovoand pages 5-7)

### Quality of life

No DFNA82-specific EQ-5D, SF-36, PROMIS, or hearing-related quality-of-life study was found. Expected burdens include impaired speech perception, educational difficulty, communication limitations, social isolation, and dependence on hearing technology. More generally, childhood moderate-to-profound SNHL affects language and school performance, while hearing loss in adults adversely affects social connection and autonomy. (smits2019denovoand pages 7-9, petit2023deafnessfromgenetic pages 1-5)

## 4. Genetic and molecular information

**ATP2B2/PMCA2:** the five defining variants, described on **NM_001001331.2** and GRCh37/hg19, were:

1. c.397+1G>A, canonical splice-donor;
2. c.955delG, p.(Ala319fs), de novo frameshift;
3. c.1963G>T, p.(Glu655*), de novo nonsense;
4. c.1998C>A, p.(Cys666*), nonsense;
5. c.2329C>T, p.(Arg777*), nonsense.

All were absent from gnomAD v2.02 and approximately 20,000 in-house exomes. Three variants segregated in dominant families; two arose de novo with parentage confirmed. All affect exons or splice sites encoding the PMCA2 w/a ortholog expressed in hair cells. Current ClinVar classifications should be checked variant-by-variant at the time of database entry because classifications can change. (smits2019denovoand pages 1-2, smits2019denovoand pages 4-5)

These are **germline**, not somatic, variants. The likely functional class is reduced PMCA2 dosage through NMD or a severely truncated pump. Dominant-negative or gain-of-function effects have not been demonstrated for classic truncating DFNA82 alleles. No recurrent chromosomal rearrangement, methylation signature, repeat expansion, mitochondrial defect, or disease-specific epigenetic lesion is established. Deletions involving ATP2B2 in 3p deletion syndromes provide supporting dosage evidence but may include additional genes. (smits2019denovoand pages 7-9)

## 5. Environmental information

DFNA82 is a genetic disease; toxins, radiation, pollution, infection, diet, smoking, and alcohol are not demonstrated primary causes. General acquired causes of SNHL—including intense noise, aminoglycosides, platinum chemotherapy, congenital CMV and other TORCH infections—remain clinically important competing or additive causes. Noise is the strongest plausible ATP2B2 interaction, supported by human common-variant association and mouse susceptibility data. (schultz2005modificationofhuman pages 7-8, petit2023deafnessfromgenetic pages 1-5, zhang2019researchanddiscussion pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous ATP2B2 truncating or splice variant leads to** NMD or production of a severely impaired PMCA2 molecule.
2. **Reduced functional PMCA2 dosage leads to** deficient ATP-dependent Ca²⁺ extrusion from auditory hair-cell stereocilia into endolymph.
3. **Deficient extrusion leads to** disturbed stereociliary cytosolic and local extracellular Ca²⁺ homeostasis, affecting mechanotransduction-channel behavior, tip-link/cadherin function, and hair-bundle physiology; several details of this step are inferred from animal and cellular work rather than directly measured in patients. (smits2019denovoand pages 9-10, smits2019denovoand pages 1-2)
4. **Ca²⁺ dysregulation leads first to** outer-hair-cell dysfunction and impaired cochlear amplification, with the basal/high-frequency cochlea most vulnerable.
5. **Persistent Ca²⁺ dysregulation is inferred to cause** Ca²⁺ cytotoxicity and progressive degeneration of outer hair cells, inner hair cells, and supporting cells.
6. **Basal cochlear dysfunction and degeneration result in** early high-frequency SNHL, which progressively extends in severity and frequency range.
7. **Branch:** with biallelic or very severe Atp2b2 deficiency in mice, the same mechanism also affects vestibular hair cells and cerebellar circuitry, producing imbalance/ataxia; this branch is not typical of heterozygous human DFNA82. (smits2019denovoand pages 9-10, smits2019denovoand pages 7-9)

PMCA2 is the predominant plasma-membrane Ca²⁺ pump in rodent hair bundles. The w/a isoform is abundant in outer-hair-cell stereocilia and less abundant at the apical surface of inner hair cells. Alternative splicing at site A regulates hair-bundle targeting. Neuroplastin/Np55 acts as an essential PMCA auxiliary partner: adult outer-hair-cell neuroplastin is required to maintain PMCA2 membrane localization, and Nptn deficiency reduces mature mechanotransduction currents. (newton2022neuroplastingeneticallyinteracts pages 1-2, smits2019denovoand pages 1-2, smits2019denovoand pages 7-9)

Suggested annotations include **GO:0055085 transmembrane transport**, **GO:0006816 calcium ion transport**, **GO:1901660 calcium ion export across plasma membrane**, **GO:0050881 musculoskeletal movement/vestibular-related processes only for model evidence**, **GO:0007605 sensory perception of sound**, and **GO:0032420 stereocilium**. Relevant cell types are **cochlear outer hair cell**, **cochlear inner hair cell**, vestibular hair cell, and supporting cell; CL accession verification is recommended before ingestion. Relevant compartments are **plasma membrane (GO:0005886)**, **stereocilium membrane**, and **hair bundle**.

No DFNA82-specific human transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, single-cell, or CRISPR-screen signature was identified. A 2024 developmental mouse study localized Atp2b2/PMCA2 in hair-cell stereocilia and greater epithelial ridge and reported thyroid-hormone-associated expression changes, but proposed scRNA-seq and ChIP-seq remained future work. (gregersen2024localizationandquantification pages 59-63, gregersen2024localizationandquantificationa pages 59-63)

## 7. Anatomical structures affected

The primary organ is the **inner ear**, specifically the **cochlea/organ of Corti**. Suggested terms include **UBERON:0001844 cochlea**, **UBERON:0002227 organ of Corti**, and stereociliary hair bundles at the apical surface of inner and outer hair cells. The basal cochlear turn is functionally most affected, explaining high-frequency loss. Disease is normally bilateral and approximately symmetric. (smits2019denovoand pages 9-10, smits2019denovoand pages 5-7)

Although ATP2B2 is expressed in vestibular sensory epithelia, cerebellum, retina, and mammary tissue, reproducible secondary-organ disease was not observed in the original DFNA82 families. These expression sites should not be converted into human disease phenotypes without variant- and syndrome-specific evidence.

## 8. Temporal development

The usual course is **insidious, chronic, lifelong, and progressive**. Hearing may be normal or only subtly abnormal at birth; recognizable loss usually emerges in early childhood. High frequencies are affected first, followed by progressive involvement of speech frequencies. One late-onset case at 55 years suggests variable expressivity or genetic/environmental modification. There is no spontaneous remission. (smits2019denovoand pages 1-2, smits2019denovoand pages 5-7, smits2019denovoand pages 7-9)

The interval after newborn screening but before speech and educational consequences is the critical diagnostic and potential therapeutic window. Progressive DFNA disorders are considered attractive future gene-therapy targets because residual hair cells and a postnatal intervention window may remain, but no ATP2B2 intervention has yet demonstrated rescue in humans. (petit2023deafnessfromgenetic pages 23-26)

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with both vertical transmission and de novo occurrence. Each affected heterozygote has an expected 50% transmission risk per pregnancy, assuming a conventional germline genotype. Penetrance appears high in the few reported pedigrees but is not quantifiable; it may be age-dependent. Expressivity is variable, especially for age at onset and severity. No anticipation, founder effect, sex bias, carrier frequency, or consanguinity effect is established. Germline mosaicism was not reported, although low residual recurrence risk is generally considered after an apparently de novo variant.

Disease-specific prevalence and incidence are unknown. The defining study found qualifying ATP2B2 variants while examining approximately **700 hearing-impaired index cases**, including 110 referred with dominant inheritance, but this selected diagnostic cohort cannot provide population prevalence. The five families were Dutch or Polish, with no evidence that DFNA82 is restricted to these populations. (smits2019denovoand pages 4-5)

## 10. Diagnostics

### Recommended approach

1. **Audiology:** age-appropriate pure-tone audiometry including frequencies through 8 kHz, bone conduction, speech reception/recognition, tympanometry, and otoacoustic emissions. Serial testing is essential because newborn screening may be normal.
2. **Clinical assessment:** otoscopy; developmental, educational, tinnitus, vestibular, noise, infection, trauma, and ototoxic-exposure history; three-generation pedigree.
3. **Molecular testing:** a comprehensive hereditary-hearing-loss panel that includes ATP2B2 and copy-number analysis, or exome/genome sequencing with CNV calling. Confirm candidate variants by an orthogonal method and test parents/relatives for segregation and de novo status.
4. **Variant interpretation:** prioritize rare heterozygous predicted loss-of-function variants affecting biologically relevant transcripts. Evaluate CDH23 and other hearing-loss genes, but do not require a second CDH23 allele for monogenic DFNA82.
5. **Imaging/vestibular testing:** not required to prove DFNA82; use CT/MRI for atypical, asymmetric, conductive, neurologic, implant-planning, or retrocochlear concerns. Vestibular testing is indicated for imbalance, vertigo, delayed motor milestones, or atypical variants. The defining cohort’s imaging was normal and vestibular testing essentially unrevealing. (smits2019denovoand pages 1-2, smits2019denovoand pages 5-7)

WES was effective in the original discovery and broader hearing-loss cohorts; WGS may add noncoding and structural-variant detection. CMA, karyotype, FISH, mitochondrial sequencing, repeat-expansion testing, biopsy, metabolomics, and liquid biopsy are not routine for an otherwise typical ATP2B2 phenotype. A 2020 clinical series emphasized that WES can identify rare genes, dual diagnoses, and initially inapparent syndromic disease and that molecular diagnosis informs prognosis, surveillance, and counseling. (morgan2020lightsandshadows pages 12-14)

Differential diagnoses include other dominant progressive high-frequency hearing losses—such as KCNQ4/DFNA2, COCH/DFNA9, MYO6/DFNA22, ACTG1/DFNA20/26, POU4F3/DFNA15, TECTA-related disease—and acquired noise, ototoxic, infectious, autoimmune, and age-related loss. Vestibular dysfunction or neurologic disease should prompt consideration of COCH-related disease or a broader ATP2B2-associated neurologic phenotype rather than classic DFNA82.

Cascade audiologic and molecular testing is appropriate for relatives. Normal newborn screening does **not** exclude the disorder. Prenatal or preimplantation genetic testing becomes technically possible after a familial pathogenic variant is established.

## 11. Outcome and prognosis

DFNA82 is not known to shorten life expectancy or cause disease-specific mortality. Morbidity is auditory: progressive communication disability, educational and speech effects in childhood, tinnitus in some patients, and eventual need for amplification or implantation. At least one person in the defining cohort received a cochlear implant by age 24, demonstrating that severe progression can occur, but ATP2B2-specific implant response rates were not reported. (smits2019denovoand pages 4-5)

Prognostic indicators are age, serial audiometric slope, baseline speech-frequency thresholds, speech recognition, and possibly variant class or modifiers. No validated molecular prognostic biomarker exists. Recovery of lost native hearing is not expected with present care; functional rehabilitation is possible with hearing technology.

## 12. Treatment and current applications

There is no approved ATP2B2-targeted drug, pharmacogenomic guideline, RNA therapy, cell therapy, gene therapy, or immunotherapy. No relevant ATP2B2/DFNA82 clinical trial was identified in the ClinicalTrials.gov search.

Current care is supportive and follows pediatric/adult SNHL practice:

* **Hearing aids** for aidable mild-to-severe loss; suggested NCIT concept: *Hearing Aid*.
* **Remote microphone/classroom systems**, educational accommodations, auditory-verbal or speech-language therapy; NCIT concepts should be mapped locally to *Assistive Device*, *Speech Therapy*, and *Audiologic Rehabilitation*.
* **Cochlear implantation** when appropriately fitted hearing aids no longer provide sufficient speech understanding; suggested NCIT concept: *Cochlear Implantation*. Genetic diagnosis helps set expectations, although no ATP2B2-specific response estimate is available. (morgan2020lightsandshadows pages 12-14, petit2023deafnessfromgenetic pages 1-5)
* **Tinnitus management** and psychosocial/communication support when required.

The authoritative 2023 review by Petit, Bonnet, and Safieddine states that hearing aids and cochlear implants remain the corrective options for mild-to-severe and profound SNHL, respectively, while reviewing preclinical gene replacement, augmentation, and editing strategies. It also cautions that mouse cochlear physiology does not fully reproduce human low-frequency speech hearing. ATP2B2 is therefore a plausible future gene-augmentation target, but vector capacity, cell-specific delivery, dosage control, timing, and durable safety remain unresolved. (petit2023deafnessfromgenetic pages 23-26, petit2023deafnessfromgenetic pages 1-5)

## 13. Prevention

**Primary prevention of the genotype is not possible.** Reproductive options after molecular confirmation include genetic counseling, prenatal diagnosis, donor gametes, and preimplantation genetic testing. Counseling should cover the nominal 50% transmission risk, de novo cases, uncertain age-dependent penetrance, and variable severity.

**Secondary prevention** consists of cascade testing, audiologic surveillance of genetically at-risk children despite a passed newborn screen, prompt assessment of speech or school difficulties, and early amplification. **Tertiary prevention** includes hearing conservation, careful risk–benefit review of ototoxic drugs, treatment of middle-ear disease, optimized hearing technology, speech/language services, and educational accommodations. Vaccination has no DFNA82-specific preventive role, though routine vaccination helps prevent some infectious causes of acquired hearing loss.

## 14. Other species and natural disease

The principal comparative species is **Mus musculus** (NCBI Taxonomy **10090**), with ortholog **Atp2b2**. Numerous naturally occurring or induced *deafwaddler* alleles produce hearing and balance phenotypes. Heterozygous loss-of-function mice develop early, rapidly progressive, high-frequency hearing loss resembling human DFNA82; homozygotes commonly have congenital severe-to-profound deafness plus vestibular/ataxic behavior. Degeneration is most severe in the cochlear base. (smits2019denovoand pages 7-9)

The phenotype is noninfectious and nontransmissible, with no zoonotic potential. No robust naturally occurring companion-animal breed disease equivalent was identified. Conservation of PMCA-dependent Ca²⁺ handling across mammalian mechanosensory hair cells makes the mouse especially informative, although timing, frequency range, and cochlear dimensions differ from humans.

## 15. Model organisms and experimental systems

### Mouse models

Available models include spontaneous **deafwaddler**, null, missense, truncating, ENU-induced, and interaction strains. They are assessed with auditory brainstem response, distortion-product otoacoustic emissions, vestibular behavior, hair-cell electrophysiology, and cochlear histology. Heterozygotes reproduce the human dosage-sensitive, progressive high-frequency phenotype; homozygotes model more severe auditory, vestibular, and cerebellar consequences. (smits2019denovoand pages 10-11, xu2011identificationofa pages 8-8, smits2019denovoand pages 7-9)

The models support a sequence in which outer-hair-cell dysfunction precedes degeneration and show that relatively small changes in PMCA2 activity can markedly change hearing. Their limitations include faster disease time scales, different audible-frequency ranges, strain-specific Cdh23 alleles, and poor modeling of human speech-frequency perception. (smits2019denovoand pages 9-10, smits2019denovoand pages 7-9, petit2023deafnessfromgenetic pages 23-26)

### Interaction and cellular models

Nptn knockout/conditional mouse models establish that neuroplastin maintains PMCA2 at the outer-hair-cell membrane. Nptn-null mature outer hair cells have reduced maximum mechanotransduction currents and channel-open probability; most hearing loss reflects hair-cell dysfunction rather than afferent-synapse abnormalities. The abstract states: “continued expression of NEUROPLASTIN in OHCs of adult mice is required for membrane localisation of Plasma Membrane Ca2+ ATPase 2.” (newton2022neuroplastingeneticallyinteracts pages 1-2)

Heterologous cell assays demonstrated reduced activity of the older PMCA2 p.Val586Met modifier allele, but patient-derived iPSC hair cells, cochlear organoids carrying defining DFNA82 variants, and ATP2B2-specific therapeutic rescue models were not identified. These constitute important current research gaps.

## Evidence appraisal and key gaps

The gene–disease relationship is supported by five independent loss-of-function alleles, two confirmed de novo events, dominant segregation, absence from large reference datasets, a coherent dosage mechanism, and strong mouse phenocopy. Nevertheless, clinical confidence intervals are wide because the foundational phenotype rests on only five families and 11 evaluated affected people. Penetrance, prevalence, sex effects, genotype–phenotype correlations, cochlear-implant outcomes, vestibular risk across the lifespan, and the boundary between nonsyndromic DFNA82 and neurologic ATP2B2 disease remain insufficiently characterized.

The most important recent advances are broader genomic diagnosis of hearing loss, increasingly precise definition of the neuroplastin–PMCA2 complex, developmental localization studies, and rapid progress in inner-ear gene therapy generally. As of the searched 2023–2024 literature, none has yet produced an ATP2B2-specific clinical intervention. The disease entry should therefore separate **established human DFNA82 facts**, **mouse-supported mechanistic inference**, and **general hearing-loss management extrapolation** rather than presenting all three as equivalent evidence.

References

1. (smits2019denovoand pages 1-2): Jeroen J. Smits, Jaap Oostrik, Andy J. Beynon, Sarina G. Kant, Pia A. M. de Koning Gans, Liselotte J. C. Rotteveel, Jolien S. Klein Wassink-Ruiter, Rolien H. Free, Saskia M. Maas, Jiddeke van de Kamp, Paul Merkus, Wouter Koole, Ilse Feenstra, Ronald J. C. Admiraal, Cornelis P. Lanting, Margit Schraders, Helger G. Yntema, Ronald J. E. Pennings, and Hannie Kremer. De novo and inherited loss-of-function variants of atp2b2 are associated with rapidly progressive hearing impairment. Human Genetics, 138:61-72, Dec 2019. URL: https://doi.org/10.1007/s00439-018-1965-1, doi:10.1007/s00439-018-1965-1. This article has 62 citations and is from a peer-reviewed journal.

2. (smits2019denovoand pages 4-5): Jeroen J. Smits, Jaap Oostrik, Andy J. Beynon, Sarina G. Kant, Pia A. M. de Koning Gans, Liselotte J. C. Rotteveel, Jolien S. Klein Wassink-Ruiter, Rolien H. Free, Saskia M. Maas, Jiddeke van de Kamp, Paul Merkus, Wouter Koole, Ilse Feenstra, Ronald J. C. Admiraal, Cornelis P. Lanting, Margit Schraders, Helger G. Yntema, Ronald J. E. Pennings, and Hannie Kremer. De novo and inherited loss-of-function variants of atp2b2 are associated with rapidly progressive hearing impairment. Human Genetics, 138:61-72, Dec 2019. URL: https://doi.org/10.1007/s00439-018-1965-1, doi:10.1007/s00439-018-1965-1. This article has 62 citations and is from a peer-reviewed journal.

3. (smits2019denovoand pages 5-7): Jeroen J. Smits, Jaap Oostrik, Andy J. Beynon, Sarina G. Kant, Pia A. M. de Koning Gans, Liselotte J. C. Rotteveel, Jolien S. Klein Wassink-Ruiter, Rolien H. Free, Saskia M. Maas, Jiddeke van de Kamp, Paul Merkus, Wouter Koole, Ilse Feenstra, Ronald J. C. Admiraal, Cornelis P. Lanting, Margit Schraders, Helger G. Yntema, Ronald J. E. Pennings, and Hannie Kremer. De novo and inherited loss-of-function variants of atp2b2 are associated with rapidly progressive hearing impairment. Human Genetics, 138:61-72, Dec 2019. URL: https://doi.org/10.1007/s00439-018-1965-1, doi:10.1007/s00439-018-1965-1. This article has 62 citations and is from a peer-reviewed journal.

4. (smits2019denovoand pages 7-9): Jeroen J. Smits, Jaap Oostrik, Andy J. Beynon, Sarina G. Kant, Pia A. M. de Koning Gans, Liselotte J. C. Rotteveel, Jolien S. Klein Wassink-Ruiter, Rolien H. Free, Saskia M. Maas, Jiddeke van de Kamp, Paul Merkus, Wouter Koole, Ilse Feenstra, Ronald J. C. Admiraal, Cornelis P. Lanting, Margit Schraders, Helger G. Yntema, Ronald J. E. Pennings, and Hannie Kremer. De novo and inherited loss-of-function variants of atp2b2 are associated with rapidly progressive hearing impairment. Human Genetics, 138:61-72, Dec 2019. URL: https://doi.org/10.1007/s00439-018-1965-1, doi:10.1007/s00439-018-1965-1. This article has 62 citations and is from a peer-reviewed journal.

5. (smits2019denovoand pages 9-10): Jeroen J. Smits, Jaap Oostrik, Andy J. Beynon, Sarina G. Kant, Pia A. M. de Koning Gans, Liselotte J. C. Rotteveel, Jolien S. Klein Wassink-Ruiter, Rolien H. Free, Saskia M. Maas, Jiddeke van de Kamp, Paul Merkus, Wouter Koole, Ilse Feenstra, Ronald J. C. Admiraal, Cornelis P. Lanting, Margit Schraders, Helger G. Yntema, Ronald J. E. Pennings, and Hannie Kremer. De novo and inherited loss-of-function variants of atp2b2 are associated with rapidly progressive hearing impairment. Human Genetics, 138:61-72, Dec 2019. URL: https://doi.org/10.1007/s00439-018-1965-1, doi:10.1007/s00439-018-1965-1. This article has 62 citations and is from a peer-reviewed journal.

6. (smits2019denovoand pages 10-11): Jeroen J. Smits, Jaap Oostrik, Andy J. Beynon, Sarina G. Kant, Pia A. M. de Koning Gans, Liselotte J. C. Rotteveel, Jolien S. Klein Wassink-Ruiter, Rolien H. Free, Saskia M. Maas, Jiddeke van de Kamp, Paul Merkus, Wouter Koole, Ilse Feenstra, Ronald J. C. Admiraal, Cornelis P. Lanting, Margit Schraders, Helger G. Yntema, Ronald J. E. Pennings, and Hannie Kremer. De novo and inherited loss-of-function variants of atp2b2 are associated with rapidly progressive hearing impairment. Human Genetics, 138:61-72, Dec 2019. URL: https://doi.org/10.1007/s00439-018-1965-1, doi:10.1007/s00439-018-1965-1. This article has 62 citations and is from a peer-reviewed journal.

7. (schultz2005modificationofhuman pages 3-4): Julie M. Schultz, Yandan Yang, Ariel J. Caride, Adelaida G. Filoteo, Alan R. Penheiter, Ayala Lagziel, Robert J. Morell, Saidi A. Mohiddin, Lameh Fananapazir, Anne C. Madeo, John T. Penniston, and Andrew J. Griffith. Modification of human hearing loss by plasma-membrane calcium pump pmca2. The New England journal of medicine, 352 15:1557-64, Apr 2005. URL: https://doi.org/10.1056/nejmoa043899, doi:10.1056/nejmoa043899. This article has 223 citations and is from a highest quality peer-reviewed journal.

8. (schultz2005modificationofhuman pages 4-6): Julie M. Schultz, Yandan Yang, Ariel J. Caride, Adelaida G. Filoteo, Alan R. Penheiter, Ayala Lagziel, Robert J. Morell, Saidi A. Mohiddin, Lameh Fananapazir, Anne C. Madeo, John T. Penniston, and Andrew J. Griffith. Modification of human hearing loss by plasma-membrane calcium pump pmca2. The New England journal of medicine, 352 15:1557-64, Apr 2005. URL: https://doi.org/10.1056/nejmoa043899, doi:10.1056/nejmoa043899. This article has 223 citations and is from a highest quality peer-reviewed journal.

9. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss-ATP2B2): Open Targets Query (autosomal dominant nonsyndromic hearing loss-ATP2B2, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (zhang2019researchanddiscussion pages 1-2): Suhao Zhang, Enmin Ding, Haoyang Yin, Hengdong Zhang, and Baoli Zhu. Research and discussion on the relationships between noise-induced hearing loss and atp2b2 gene polymorphism. International Journal of Genomics, 2019:1-8, Dec 2019. URL: https://doi.org/10.1155/2019/5048943, doi:10.1155/2019/5048943. This article has 12 citations.

11. (gregersen2024localizationandquantification pages 59-63): E Gregersen. Localization and quantification of atpase, ca2+ transporting, plasma membrane 2 (atp2b2) in the developing euthyroid and hypothyroid cochlea. Unknown journal, 2024.

12. (gregersen2024localizationandquantificationa pages 59-63): E Gregersen. Localization and quantification of atpase, ca2+ transporting, plasma membrane 2 (atp2b2) in the developing euthyroid and hypothyroid cochlea. Unknown journal, 2024.

13. (petit2023deafnessfromgenetic pages 1-5): Christine Petit, Crystel Bonnet, and Saaïd Safieddine. Deafness: from genetic architecture to gene therapy. Nature Reviews Genetics, 24:665-686, May 2023. URL: https://doi.org/10.1038/s41576-023-00597-7, doi:10.1038/s41576-023-00597-7. This article has 120 citations and is from a domain leading peer-reviewed journal.

14. (schultz2005modificationofhuman pages 7-8): Julie M. Schultz, Yandan Yang, Ariel J. Caride, Adelaida G. Filoteo, Alan R. Penheiter, Ayala Lagziel, Robert J. Morell, Saidi A. Mohiddin, Lameh Fananapazir, Anne C. Madeo, John T. Penniston, and Andrew J. Griffith. Modification of human hearing loss by plasma-membrane calcium pump pmca2. The New England journal of medicine, 352 15:1557-64, Apr 2005. URL: https://doi.org/10.1056/nejmoa043899, doi:10.1056/nejmoa043899. This article has 223 citations and is from a highest quality peer-reviewed journal.

15. (newton2022neuroplastingeneticallyinteracts pages 1-2): Sherylanne Newton, Fanbo Kong, Adam J. Carlton, Carlos Aguilar, Andrew Parker, Gemma F. Codner, Lydia Teboul, Sara Wells, Steve D. M. Brown, Walter Marcotti, and Michael R. Bowl. Neuroplastin genetically interacts with cadherin 23 and the encoded isoform np55 is sufficient for cochlear hair cell function and hearing. Jan 2022. URL: https://doi.org/10.1371/journal.pgen.1009937, doi:10.1371/journal.pgen.1009937. This article has 16 citations and is from a domain leading peer-reviewed journal.

16. (petit2023deafnessfromgenetic pages 23-26): Christine Petit, Crystel Bonnet, and Saaïd Safieddine. Deafness: from genetic architecture to gene therapy. Nature Reviews Genetics, 24:665-686, May 2023. URL: https://doi.org/10.1038/s41576-023-00597-7, doi:10.1038/s41576-023-00597-7. This article has 120 citations and is from a domain leading peer-reviewed journal.

17. (morgan2020lightsandshadows pages 12-14): Anna Morgan, Stefania Lenarduzzi, Beatrice Spedicati, Elisabetta Cattaruzzi, Flora Maria Murru, Giulia Pelliccione, Daniela Mazzà, Marcella Zollino, Claudio Graziano, Umberto Ambrosetti, Marco Seri, Flavio Faletra, and Giorgia Girotto. Lights and shadows in the genetics of syndromic and non-syndromic hearing loss in the italian population. Genes, 11:1237, Oct 2020. URL: https://doi.org/10.3390/genes11111237, doi:10.3390/genes11111237. This article has 35 citations.

18. (xu2011identificationofa pages 8-8): Lin XU, Zixing WANG, Xiwen XIONG, Xingxing GU, Xiang GAO, and Xia GAO. Identification of a novel point mutation of mouse atp2b2 induced by n-ethyl-n-nitrosourea mutagenesis. Experimental animals, 60 1:71-8, Jan 2011. URL: https://doi.org/10.1538/expanim.60.71, doi:10.1538/expanim.60.71. This article has 10 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hearing_Loss_Autosomal_Dominant_82-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.