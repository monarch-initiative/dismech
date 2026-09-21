---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T11:45:32.455622'
end_time: '2026-09-02T11:55:12.584780'
duration_seconds: 580.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acute Ackee Fruit Intoxication
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Acute_Ackee_Fruit_Intoxication-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Ackee Fruit Intoxication
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Ackee Fruit Intoxication** covering all of the
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
- **Disease Name:** Acute Ackee Fruit Intoxication
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Ackee Fruit Intoxication** covering all of the
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


# Acute Ackee Fruit Intoxication: Disease-Characteristics Report

## Executive summary

Acute ackee fruit intoxication—classically **Jamaican vomiting sickness**—is an acquired, potentially fatal foodborne metabolic poisoning caused mainly by **hypoglycin A (HGA)** in immature *Blighia sapida* fruit. It produces an acquired multiple-acyl-CoA-dehydrogenase-deficiency phenotype: impaired mitochondrial fatty-acid oxidation deprives fasting patients of ketones and gluconeogenic energy, causing recurrent vomiting, profound hypoketotic hypoglycemia, encephalopathy, seizures, coma, hepatic steatosis/injury, and sometimes death. Children and undernourished or fasting persons are especially vulnerable. The evidence base is unusual: landmark human observations are old, modern human cohorts are scarce, and much current mechanistic, biomarker, and therapeutic evidence comes from rats, mice, and naturally poisoned horses. Accordingly, animal values below must not be used as human reference intervals.

| domain | strongest finding | evidence type/species | key quantitative datum | source/date/DOI |
|---|---|---|---|---|
| Human clinical syndrome | Acute ackee intoxication follows ingestion of unripe ackee and presents with vomiting, hypoglycemia, and CNS depression; severe cases may progress to seizures, coma, and death | Human clinical case/report | Onset reported within 6–48 h; death in severe cases may occur within 48 h; unripe fruit reported to contain hypoglycin A at about 100-fold higher concentration than ripe fruit | Latif & Luthra, 2017, DOI: 10.23937/2377-3634/1410073 (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 1-2) |
| Human historical pathology | Fatal human cases show multi-organ fatty degeneration, especially liver, with renal, pancreatic, cardiac, and pulmonary involvement | Human historical autopsy series | Severe cases described with onset within about 2 h; historical mortality estimates 80–90% in early reports | Scott, 1916, DOI: 10.1080/00034983.1916.11684104 (scott1916onthevomiting pages 56-58, scott1916onthevomiting pages 58-62) |
| Mechanism | Hypoglycin A is metabolized to MCPA-CoA, causing an acquired multiple acyl-CoA dehydrogenase deficiency and impaired fatty-acid oxidation/gluconeogenesis | Mixed evidence: human biochemical inference plus extrapolative rat/horse data | Extrapolative horse biomarker data: serum HGA 387.8–8493.8 μg/L; urine HGA 143.8–926.4 μg/L; controls less than 10 μg/L | Bochnia et al., 2015, DOI: 10.1371/journal.pone.0136785; Boemer et al., 2017, DOI: 10.1371/journal.pone.0182761 (bochnia2015hypoglycinacontent pages 1-2, boemer2017acylcarnitinesprofilebest pages 15-16, boemer2017acylcarnitinesprofilebest pages 16-16) |
| Analytical diagnostics | Exposure can be supported by measuring hypoglycin A and downstream metabolites or conjugates; acylcarnitine and organic-acid profiling are informative | Human analytical mention plus extrapolative horse biomarker data | Extrapolative horse MCPA-carnitine data: serum 0.17–0.65 mmol/L vs controls less than 0.01; urine 0.34–2.05 μmol/mmol vs controls less than 0.001 | Bochnia et al., 2015, DOI: 10.1371/journal.pone.0136785; Latif & Luthra, 2017, DOI: 10.23937/2377-3634/1410073 (latif2017newdevelopmentof pages 2-3, bochnia2015hypoglycinacontent pages 1-2) |
| 2023 development | A derivatization-free UPLC-MS/MS method was validated for hypoglycin A, methylenecyclopropylglycine, and metabolites in milk and urine, improving surveillance capability | Extrapolative analytical method development | HGA limit of quantification in milk 1.12 μg/L; 68 milk samples from 35 farms showed no quantifiable toxin or metabolites | El-Khatib et al., 2023, DOI: 10.1007/s00216-023-04607-9 (medina2018detectionofequine pages 10-11) |
| Treatment evidence | Best-supported management is early dextrose plus supportive care, including fluids, electrolyte correction, and monitoring of glucose, liver, and kidney injury | Human case evidence plus extrapolative mouse/rat evidence | Recovery may occur within about 1 week in nonfatal cases; no validated antidote identified | Latif & Luthra, 2017, DOI: 10.23937/2377-3634/1410073 (latif2017newdevelopmentof pages 3-4) |
| Treatment limitations | Glycine, methylene blue, and carnitine have experimental rationale, but clinical efficacy in humans remains unproven | Mixed evidence; mouse/rat/horse evidence extrapolative | No controlled human trial identified; no ackee-specific interventional trial found in retrieved trial search | Latif & Luthra, 2017, DOI: 10.23937/2377-3634/1410073 (latif2017newdevelopmentof pages 3-4) |
| Epidemiology and outbreaks | Disease clusters seasonally where ackee is consumed, with children disproportionately affected; modern epidemiologic data are sparse | Human historical evidence plus outbreak review snippets | Haiti 2000–2001 outbreak reported as 60 intoxication cases; older reports emphasize child predominance | Scott, 1916, DOI: 10.1080/00034983.1916.11684104 (scott1916onthevomiting pages 58-62, scott1916onthevomiting pages 56-58) |
| Food safety and prevention | Prevention depends on avoiding unripe or unopened ackee, removing seeds and membrane, and using regulated low-hypoglycin products | Human public-health and food-safety evidence | FDA import standard cited as hypoglycin A limit of 100 ppm for regulated products | Latif & Luthra, 2017, DOI: 10.23937/2377-3634/1410073 (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 1-2) |
| Animal models | Rat, mouse, horse, and related Sapindaceae toxin studies support mechanism and biomarker development, but remain extrapolative for human disease | Extrapolative animal evidence | Rat dose-response model exists; horse disease shows strong biomarker association with HGA exposure | Bochnia et al., 2015, DOI: 10.1371/journal.pone.0136785; Boemer et al., 2017, DOI: 10.1371/journal.pone.0182761 (bochnia2015hypoglycinacontent pages 1-2, boemer2017acylcarnitinesprofilebest pages 15-16) |


*Table: This table summarizes the strongest available evidence for acute ackee fruit intoxication across clinical, mechanistic, diagnostic, epidemiologic, preventive, and animal-model domains. It prioritizes direct human evidence and clearly labels extrapolations from horse, rat, mouse, and other comparative studies.*

## 1. Disease information

### Definition and synonyms

The disorder is an **acute exogenous intoxication**, not a Mendelian disease. Synonyms include **ackee poisoning**, **ackee fruit poisoning**, **acute ackee intoxication**, **hypoglycin A poisoning**, **toxic hypoglycemic syndrome**, and **Jamaican vomiting sickness**. The classic syndrome consists of gastrointestinal illness, severe hypoglycemia, and central nervous-system depression after consumption of unripe ackee; severe disease includes seizures, coma, and death. Mature arils from fruit that has opened naturally are ordinarily consumed safely. (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 1-2)

### Identifiers and coding

* **MONDO:** no disease-specific MONDO identifier was substantiated in the retrieved sources; do not assign one without checking the current MONDO release.
* **OMIM/Orphanet:** not applicable as disease-specific inherited-disorder identifiers; no dedicated entry was substantiated.
* **MeSH:** best represented under broad concepts such as plant poisoning, foodborne intoxication, hypoglycemia, and hypoglycins; a dedicated descriptor was not substantiated.
* **ICD:** coding is generally under toxic effects of ingested berries/other noxious food substances or plant poisoning, with intent and encounter extensions where required. The precise ICD-10-CM/ICD-11 code should be validated against the jurisdiction and release rather than inferred from literature.

The report is assembled from **aggregated disease-level literature**, human case reports and autopsies, outbreak investigations, analytical-method studies, and animal experiments—not individual EHR data.

## 2. Etiology, risk, and protective factors

### Cause

The initiating exposure is ingestion of toxic ackee material, especially an **immature, forcibly opened, damaged, or improperly prepared fruit**. HGA occurs in arils and seeds; hypoglycin B is a less potent γ-glutamyl conjugate concentrated in seeds. One clinical review reports approximately **100-fold more HGA in unripe than ripe fruit**, although toxin concentration varies with maturity and processing. (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 1-2)

Suggested chemical annotations are **hypoglycin A**, **hypoglycin B**, methylenecyclopropylpyruvate, methylenecyclopropylacetate/MCPA, MCPA-CoA, MCPA-carnitine, and MCPA-glycine; exact ChEBI identifiers should be release-validated.

### Risk factors

* **Environmental/dietary:** unripe or unopened ackee, seeds or attached membrane, contaminated cooking liquid, inadequate washing, and unregulated processing.
* **Physiological:** childhood, low body mass, overnight fasting, malnutrition, depleted glycogen, and delayed glucose treatment plausibly increase vulnerability. Historical disease was strongly seasonal and concentrated in children when other foods were scarce. (scott1916onthevomiting pages 56-58, scott1916onthevomiting pages 58-62)
* **Clustering:** multiple members of a household may become ill after sharing fruit. (scott1916onthevomiting pages 56-58)
* **Sex:** historical work found no clear sex preference. (scott1916onthevomiting pages 56-58)

Historical ethnic differences are more parsimoniously explained by dietary access and exposure than inherited susceptibility. No reproducible human susceptibility locus or pharmacogenomic association has been established.

### Protective factors

Primary protection consists of eating only fruit that has **opened naturally**, discarding seeds and the attached pink/red membrane, washing arils thoroughly, using validated processing controls, and avoiding prolonged fasting—particularly in children. Regulated products and hazard-analysis systems reduce exposure; a clinical review cites an FDA import/HACCP ceiling of **100 ppm HGA**. (latif2017newdevelopmentof pages 1-2)

No genetic protective variant is known. Gene–environment interaction remains hypothetical: variants affecting fatty-acid oxidation or toxin disposition could modify severity, but this has not been demonstrated in human ackee poisoning.

## 3. Phenotypes

Percentages are unavailable from modern, adequately sized cohorts; frequencies therefore remain qualitative.

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Recurrent severe vomiting | Cardinal early symptom; episodes may alternate with quiescent intervals | Vomiting, HP:0002013 |
| Hypoglycemia, usually hypoketotic | Cardinal laboratory abnormality; may be profound or refractory | Hypoglycemia, HP:0001943; Hypoketotic hypoglycemia, HP:0001985 |
| Encephalopathy/CNS depression | Variable from lethargy to coma; downstream of energy failure and possibly direct toxicity | Encephalopathy, HP:0001298; Coma, HP:0001259 |
| Seizures | Severe manifestation, often accompanying marked hypoglycemia | Seizure, HP:0001250 |
| Metabolic acidosis/organic aciduria | Laboratory manifestation of blocked oxidation and alternative ω-oxidation | Metabolic acidosis, HP:0001942; Organic aciduria, HP:0001992 |
| Hepatic steatosis/injury | Transaminase elevation to fulminant injury; historical autopsies show diffuse fatty change | Hepatic steatosis, HP:0001397; Elevated hepatic transaminase, HP:0002910 |
| Renal injury | Creatinine elevation or tubular injury in severe disease | Acute kidney injury, HP:0001919 |
| Weakness/hypotonia | Reported during hypoglycemic crisis and recovery | Muscle weakness, HP:0001324; Hypotonia, HP:0001252 |

Symptoms generally begin **within 6–48 hours**, although historical fulminant cases began near two hours after exposure. Severe cases may die within 48 hours; survivors commonly improve over days and may recover within approximately one week. (latif2017newdevelopmentof pages 2-3, scott1916onthevomiting pages 56-58, scott1916onthevomiting pages 58-62)

Quality-of-life instruments such as EQ-5D or SF-36 have not been studied. Acute impact is nevertheless major: inability to eat or function, emergency hospitalization, seizures, ventilation/critical care, and risk of neurologic injury or death.

## 4. Genetic and molecular information

There is **no established causal gene, pathogenic germline or somatic variant, inheritance pattern, chromosomal lesion, penetrance estimate, modifier gene, or disease-specific epigenetic abnormality**. WES, WGS, panels, CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine diagnostic tests.

Mechanistically relevant human proteins include mitochondrial acyl-CoA dehydrogenases—especially **ACADM/MCAD** and IVD—and electron-transfer flavoprotein pathways. These are inhibited by toxin metabolites rather than altered genetically. Thus, intoxication phenocopies inherited MADD/glutaric acidemia type II but must not be represented as an ETF-pathway genetic disorder. Comparative work supports inhibition of multiple acyl-CoA dehydrogenases and consequent abnormal acylcarnitines and organic acids. (bochnia2015hypoglycinacontent pages 1-2, boemer2017acylcarnitinesprofilebest pages 15-16, boemer2017acylcarnitinesprofilebest pages 16-16)

## 5. Environmental information

The disease is entirely exposure driven. *Blighia sapida* is the relevant plant; unripe fruit is the principal source. Diet, food scarcity, harvesting before natural opening, and unsafe preparation govern risk. There is no infectious agent, person-to-person transmission, radiation association, or conventional occupational syndrome, although harvesters, processors, and food inspectors have exposure-control responsibilities.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Ingestion of immature/improperly prepared ackee leads to absorption of HGA** and related methylenecyclopropyl compounds.
2. **HGA metabolism leads to methylenecyclopropyl intermediates and MCPA-CoA**, the active inhibitory metabolite.
3. **MCPA-CoA leads to irreversible or functionally sustained inhibition of several mitochondrial acyl-CoA dehydrogenases**, including MCAD and IVD, producing acquired MADD. (bochnia2015hypoglycinacontent pages 1-2, boemer2017acylcarnitinesprofilebest pages 15-16, boemer2017acylcarnitinesprofilebest pages 16-16)
4. **Blocked β-oxidation leads to reduced acetyl-CoA, reducing equivalents, ATP, and ketogenesis**, while accumulating acyl-CoAs.
5. **Energy/cofactor depletion leads to impaired hepatic gluconeogenesis and depleted glucose availability**, producing hypoketotic hypoglycemia. (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 3-4)
6. **Accumulated acyl-CoAs branch into acylcarnitines/acylglycines and ω-oxidation**, resulting in characteristic acylcarnitinemia, dicarboxylic aciduria, and metabolic acidosis. Rat studies identify glutaric, adipic, unsaturated dicarboxylic acids, MCPA-glycine, and isovalerylglycine; their diagnostic interpretation in humans is partly extrapolative. (boemer2017acylcarnitinesprofilebest pages 15-16)
7. **Hepatic lipid oxidation failure leads to triglyceride accumulation and hepatocellular energy failure**, resulting in micro-/macrovesicular fatty change and potentially acute liver injury.
8. **Neuroglycopenia leads to vomiting-associated lethargy, seizures, encephalopathy, and coma**; a separate direct neurotoxic contribution is reported but less firmly resolved in humans. (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 3-4)
9. **Severe systemic energy failure branches to renal, pancreatic, cardiac, and pulmonary injury**, resulting in multiorgan failure and death in fulminant cases. (scott1916onthevomiting pages 56-58)

Upstream processes are exposure, toxin bioactivation, and enzyme inhibition; downstream processes are metabolic energy failure, alternative metabolite formation, steatosis, neuroglycopenia, and organ injury.

Suggested GO annotations include **fatty-acid beta-oxidation** (GO:0006635), **mitochondrial fatty-acid beta-oxidation** (GO:0006635 with mitochondrial context), **gluconeogenesis** (GO:0006094), **ketone-body biosynthetic process** (GO:0046951), **cellular response to hypoglycemia**, and **lipid-storage process**. Principal cells are hepatocytes (CL:0000182), neurons (CL:0000540), renal tubular epithelial cells, pancreatic acinar cells, and cardiomyocytes (CL:0000746). Principal compartment: mitochondrion (GO:0005739), especially mitochondrial matrix (GO:0005759).

No ackee-specific human transcriptomic, proteomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics dataset was substantiated. Targeted metabolomics is currently the relevant molecular-profiling modality.

## 7. Anatomical structures affected

The **liver** is the principal metabolic organ; the **brain** is the principal clinically vulnerable organ. Historical fatal pathology demonstrated diffuse fatty liver, renal tubular fatty degeneration/nephritis, pancreatic necrobiosis, myocardial fat droplets, and pulmonary/visceral congestion. (scott1916onthevomiting pages 56-58)

Suggested anatomy annotations include liver (UBERON:0002107), brain (UBERON:0000955), kidney (UBERON:0002113), pancreas (UBERON:0001264), heart (UBERON:0000948), and lung (UBERON:0002048). At cell level, hepatocytes and renal tubular epithelial cells are central. At subcellular level, mitochondria are primary; cytosolic lipid droplets are secondary. Lateralization is not relevant.

## 8. Temporal development

The disease is acute and monophasic after a discrete meal. A useful clinical staging scheme is:

1. **Latent/early phase:** hours after ingestion; nausea, malaise, vomiting.
2. **Metabolic phase:** recurrent vomiting, hypoglycemia, low ketones, aciduria/acidosis.
3. **Neurologic/organ-injury phase:** altered consciousness, seizures, rising aminotransferases/creatinine.
4. **Recovery or fulminant phase:** improvement over several days after glucose/support, or coma, multiorgan failure, and death—often within 48 hours in severe cases. (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 3-4)

There is no chronic relapsing course unless exposure recurs. The crucial therapeutic window is **before prolonged neuroglycopenia and hepatic energy failure**; glucose should not await confirmatory toxicology.

## 9. Inheritance and population epidemiology

Inheritance, anticipation, mosaicism, founder effects, consanguinity, carrier frequency, and penetrance are not applicable.

Reliable contemporary incidence and prevalence per 100,000 are unavailable. Historical Jamaican reports described seasonality, household clusters, disproportionate pediatric disease, and mortality estimates as high as **80–90%**, but these figures predate modern critical care and should not be treated as current case-fatality rates. (scott1916onthevomiting pages 58-62)

A secondary retrieved source reports **60 intoxications in Haiti during 2000–2001**; the primary outbreak report should be consulted before database ingestion. Disease is concentrated where ackee grows or is imported, particularly Jamaica, Haiti, and parts of West Africa. Historical racial/ethnic patterns likely reflected food practices and poverty rather than proven biology. No current sex ratio is established.

## 10. Diagnostics

### Clinical diagnosis

Diagnosis is based on compatible exposure plus acute vomiting and **hypoketotic hypoglycemia**, with neurologic or hepatic abnormalities. Immediate tests should include serial bedside glucose, blood gas, electrolytes, bicarbonate/anion gap, lactate, serum/urine ketones, AST/ALT, bilirubin, INR, creatinine, urea, ammonia, CK, urinalysis, ECG, and continuous neurologic monitoring where severe.

### Specific and omics-based tests

Confirmation can use LC-MS/MS or GC-MS measurement of HGA, MCPA-glycine, MCPA-carnitine, related acylcarnitines, acylglycines, and urinary organic acids. The clinical report describes urinary MCPAA detection by GC-MS and HGA/metabolite measurement in blood and urine. (latif2017newdevelopmentof pages 2-3)

Horse data demonstrate the principle but not human cutoffs: affected horses had serum HGA **387.8–8,493.8 μg/L** and urine HGA **143.8–926.4 μg/L**, versus controls below 10 μg/L; serum MCPA-carnitine was **0.17–0.65 mmol/L**, versus below 0.01 in controls. (bochnia2015hypoglycinacontent pages 1-2)

A 2023 derivatization-free UPLC-MS/MS method achieved an HGA quantification limit of **1.12 μg/L in milk**, 85–106% recovery across milk/urine, and ≤20% precision; none of 68 samples from 35 German dairy farms contained quantifiable analytes. This is an exposure-surveillance advance, not a validated human diagnostic threshold. The authors’ abstract states: “The determination of HGA, MCPrG, and their glycine and carnitine metabolites in blood and urine is a useful tool for screening for potential exposure to these toxins.” DOI: https://doi.org/10.1007/s00216-023-04607-9, published March 2023.

### Differential diagnosis

Important alternatives are inherited fatty-acid-oxidation disorders/MADD, Reye syndrome, sepsis, malaria or meningoencephalitis in endemic settings, insulin/sulfonylurea exposure, starvation, alcohol-related hypoglycemia, adrenal insufficiency, inborn organic acidemias, acetaminophen or other hepatotoxic poisoning, and litchi-associated MCPG/HGA encephalopathy. Historical cases were mistaken for meningitis or yellow fever. (scott1916onthevomiting pages 58-62)

Imaging, EEG, biopsy, and genetic testing are not routine; use them for complications or unresolved alternatives. There is no asymptomatic population screening program.

## 11. Outcome and prognosis

Outcome depends on dose, maturity of fruit, age/body mass, nutritional state, depth/duration of hypoglycemia, hepatic injury, and speed of glucose administration. Nonfatal cases can recover rapidly or within approximately one week; prolonged seizures, coma, acute liver failure, renal injury, aspiration, and death are principal complications. (latif2017newdevelopmentof pages 2-3, latif2017newdevelopmentof pages 3-4)

Historical 80–90% mortality estimates represent selected early severe outbreaks and are not generalizable to current treated patients. No validated human prognostic score, long-term survival curve, disability estimate, or quality-of-life dataset exists. Serial glucose, neurologic status, pH/lactate, INR, aminotransferases, creatinine, and ammonia are practical severity markers, but none is a validated ackee-specific prognostic biomarker.

## 12. Treatment

### Immediate clinical algorithm

1. **Stabilize airway, breathing, and circulation; check glucose immediately.**
2. **Administer IV dextrose promptly** for symptomatic or documented hypoglycemia, then continue glucose-containing fluids/titrated infusion with frequent checks; recurrent hypoglycemia is expected.
3. Correct dehydration, electrolytes, acid–base disturbance, and temperature; stop fasting and provide carbohydrate when safe.
4. Treat seizures conventionally while correcting glucose; protect the airway if consciousness is impaired.
5. Monitor liver enzymes, bilirubin, INR, ammonia, creatinine, urine output, CK, ECG, and neurologic status; transfer severe cases to intensive care or a liver-capable center.
6. Contact a poison center/medical toxicologist and retain food, blood, and urine for targeted testing.

Human evidence supports early dextrose and supportive care; one review characterizes IV dextrose as extremely effective when administered early. (latif2017newdevelopmentof pages 3-4)

Suggested NCIt intervention concepts are dextrose administration, intravenous fluid therapy, electrolyte replacement, anticonvulsant therapy, mechanical ventilation, intensive-care management, and liver transplantation when fulminant failure meets standard criteria.

### Unproven therapies

Glycine, methylene blue, and carnitine have experimental rationales. Mouse studies support early glucose and methylene blue; rat-hepatocyte experiments did not establish carnitine as an antidote. No controlled human efficacy data support these agents, and they should not replace dextrose/supportive care. (latif2017newdevelopmentof pages 3-4)

No ackee-specific gene, cell, RNA, immunologic, targeted, or surgical therapy exists. A ClinicalTrials.gov search retrieved **no relevant ackee/HGA interventional trial**. Pharmacogenomic guidance and response-rate estimates are unavailable.

## 13. Prevention

* **Primary:** consume only naturally opened, fully mature fruit; never force open immature pods; discard seeds and membrane; wash arils; use approved processors and validated HACCP controls. (latif2017newdevelopmentof pages 1-2)
* **Secondary:** recognize household clusters rapidly, test glucose in every exposed symptomatic person, and treat before encephalopathy. Assess children who shared the meal even if symptoms are initially mild.
* **Tertiary:** prevent recurrent hypoglycemia, aspiration, seizures, cerebral injury, liver failure, and renal failure through monitoring and critical care.
* **Public health:** trace and withdraw implicated lots, communicate safe harvesting/preparation practices, train clinicians in endemic regions, and maintain analytical capacity for HGA/MCPA compounds.

Vaccination, antimicrobial prophylaxis, genetic counseling, prenatal testing, carrier screening, and newborn screening are not applicable.

## 14. Other species and natural disease

HGA-containing **Acer** seeds/seedlings cause equine atypical myopathy, a naturally occurring, often fatal acquired MADD in horses. This is a mechanistically strong analogue but differs clinically: horses predominantly develop severe rhabdomyolysis, whereas human ackee intoxication is dominated by vomiting, hypoglycemia, encephalopathy, and liver injury. Horse exposure studies show that clinically normal co-grazers can contain HGA, demonstrating that exposure does not equal disease. (bochnia2015hypoglycinacontent pages 1-2)

A 2023 dairy study addressed possible carry-over into milk; its 68 field samples from 35 farms were negative at the assay’s quantification limits. This does not exclude exposure under different conditions. No zoonotic transmission occurs; susceptibility reflects shared plant toxins, not infection.

Suggested taxonomy annotations include *Homo sapiens* (NCBI Taxon 9606), *Equus caballus* (9796), *Mus musculus* (10090), *Rattus norvegicus* (10116), and *Danio rerio* (7955). Breed-specific susceptibility is not established.

## 15. Model organisms and recent research

### Established models

* **Rat:** HGA dose-response and hepatocyte systems reproduce hypoglycemia, abnormal fatty-acid oxidation, dicarboxylic aciduria, and enzyme inhibition. They are valuable for mechanism and antidote testing but incompletely model human vomiting/encephalopathy.
* **Mouse:** unripe-ackee exposure models have tested early glucose and methylene blue; timing and dosing limit translation.
* **Horse natural model:** provides abundant blood/urine metabolomics and tissue pathology for acquired MADD. It strongly supports HGA causality and MCPA-conjugate biomarkers, but its muscle-dominant phenotype differs from human disease. In one study, HGA and MCPA conjugates clearly separated diseased horses, exposed healthy co-grazers, and unexposed controls. (bochnia2015hypoglycinacontent pages 1-2)
* **Zebrafish embryo:** a 2024 study developed a Sapindaceae-poisoning platform to screen therapeutic compounds (Wouters et al., *Molecules*, October 2024; DOI: https://doi.org/10.3390/molecules29204954). This is a preclinical screening system, not evidence of human efficacy.
* **Historical guinea-pig/rabbit experiments:** results were inconclusive because of limited extracts, solvent effects, and species selection. (scott1916onthevomiting pages 40-43)

No standardized knockout, knock-in, humanized mouse, organoid, or patient-derived iPSC model specific to ackee intoxication was identified. Genetic ETF/ETFDH/ACADM models may illuminate downstream energy failure but model inherited enzyme defects rather than toxin bioactivation.

## Evidence interpretation and research gaps

The most authoritative conclusion is that acute ackee intoxication is a preventable exposure-induced mitochondrial energy crisis requiring immediate glucose and supportive care. The major gaps are contemporary prospective human cohorts, validated human toxin/metabolite reference ranges, dose–response data, standardized diagnostic criteria, controlled antidote trials, long-term neurodevelopmental follow-up, and modern incidence/case-fatality surveillance. Recent work has advanced sensitive mass-spectrometric exposure measurement and preclinical screening rather than changing clinical management.

Representative exact abstract quotation from the 2018 analytical/model literature is: “Hypoglycin A (HGA) toxicity, following ingestion of material from certain plants, is linked to an acquired multiple acyl-CoA dehydrogenase deficiency.” DOI: https://doi.org/10.1371/journal.pone.0199521, published July 2018. (medina2018detectionofequine pages 10-11)

Where PMIDs were not verified in the retrieved records, DOI URLs are provided rather than risking incorrect PMID assignment.

References

1. (latif2017newdevelopmentof pages 2-3): Summaya Abdul Latif and Pooja Luthra. New development of hypoglycemia in a previously poorly-controlled type 2 diabetic: ackee fruit-induced hypoglycemia. International Journal of Diabetes and Clinical Research, Dec 2017. URL: https://doi.org/10.23937/2377-3634/1410073, doi:10.23937/2377-3634/1410073. This article has 2 citations.

2. (latif2017newdevelopmentof pages 1-2): Summaya Abdul Latif and Pooja Luthra. New development of hypoglycemia in a previously poorly-controlled type 2 diabetic: ackee fruit-induced hypoglycemia. International Journal of Diabetes and Clinical Research, Dec 2017. URL: https://doi.org/10.23937/2377-3634/1410073, doi:10.23937/2377-3634/1410073. This article has 2 citations.

3. (scott1916onthevomiting pages 56-58): H. Harold Scott. On the 'vomiting sickness' of jamaica. Annals of Tropical Medicine and Parasitology, 10:1-78, Apr 1916. URL: https://doi.org/10.1080/00034983.1916.11684104, doi:10.1080/00034983.1916.11684104. This article has 54 citations.

4. (scott1916onthevomiting pages 58-62): H. Harold Scott. On the 'vomiting sickness' of jamaica. Annals of Tropical Medicine and Parasitology, 10:1-78, Apr 1916. URL: https://doi.org/10.1080/00034983.1916.11684104, doi:10.1080/00034983.1916.11684104. This article has 54 citations.

5. (bochnia2015hypoglycinacontent pages 1-2): M. Bochnia, J. Ziegler, J. Sander, A. Uhlig, S. Schaefer, S. Vollstedt, M. Glatter, Steffen Abel, S. Recknagel, G. Schusser, M. Wensch-Dorendorf, and A. Zeyner. Hypoglycin a content in blood and urine discriminates horses with atypical myopathy from clinically normal horses grazing on the same pasture. PLoS ONE, 10:e0136785, Sep 2015. URL: https://doi.org/10.1371/journal.pone.0136785, doi:10.1371/journal.pone.0136785. This article has 75 citations and is from a peer-reviewed journal.

6. (boemer2017acylcarnitinesprofilebest pages 15-16): François Boemer, Johann Detilleux, Christophe Cello, Hélène Amory, Christel Marcillaud-Pitel, Eric Richard, Gaby van Galen, Gunther van Loon, Laurence Lefère, and Dominique-Marie Votion. Acylcarnitines profile best predicts survival in horses with atypical myopathy. PLoS ONE, 12:e0182761, Aug 2017. URL: https://doi.org/10.1371/journal.pone.0182761, doi:10.1371/journal.pone.0182761. This article has 36 citations and is from a peer-reviewed journal.

7. (boemer2017acylcarnitinesprofilebest pages 16-16): François Boemer, Johann Detilleux, Christophe Cello, Hélène Amory, Christel Marcillaud-Pitel, Eric Richard, Gaby van Galen, Gunther van Loon, Laurence Lefère, and Dominique-Marie Votion. Acylcarnitines profile best predicts survival in horses with atypical myopathy. PLoS ONE, 12:e0182761, Aug 2017. URL: https://doi.org/10.1371/journal.pone.0182761, doi:10.1371/journal.pone.0182761. This article has 36 citations and is from a peer-reviewed journal.

8. (medina2018detectionofequine pages 10-11): Sonia González Medina, Carolyne Hyde, Imogen Lovera, and Richard J. Piercy. Detection of equine atypical myopathy-associated hypoglycin a in plant material: optimisation and validation of a novel lc-ms based method without derivatisation. PLoS ONE, 13:e0199521, Jul 2018. URL: https://doi.org/10.1371/journal.pone.0199521, doi:10.1371/journal.pone.0199521. This article has 24 citations and is from a peer-reviewed journal.

9. (latif2017newdevelopmentof pages 3-4): Summaya Abdul Latif and Pooja Luthra. New development of hypoglycemia in a previously poorly-controlled type 2 diabetic: ackee fruit-induced hypoglycemia. International Journal of Diabetes and Clinical Research, Dec 2017. URL: https://doi.org/10.23937/2377-3634/1410073, doi:10.23937/2377-3634/1410073. This article has 2 citations.

10. (scott1916onthevomiting pages 40-43): H. Harold Scott. On the 'vomiting sickness' of jamaica. Annals of Tropical Medicine and Parasitology, 10:1-78, Apr 1916. URL: https://doi.org/10.1080/00034983.1916.11684104, doi:10.1080/00034983.1916.11684104. This article has 54 citations.

## Artifacts

- [Edison artifact artifact-00](Acute_Ackee_Fruit_Intoxication-deep-research-falcon_artifacts/artifact-00.md)