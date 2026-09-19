---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T23:58:15.151006'
end_time: '2026-07-31T00:10:26.313200'
duration_seconds: 731.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autism, susceptibility to, X-linked 3 (AUTSX3; MECP2-related X-linked
    autism susceptibility)
  mondo_id: MONDO:0010342
  category: Complex (X-linked genetic susceptibility; MECP2)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autism_Susceptibility_to_X-Linked_3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autism, susceptibility to, X-linked 3 (AUTSX3; MECP2-related X-linked autism susceptibility)
- **MONDO ID:** MONDO:0010342 (if available)
- **Category:** Complex (X-linked genetic susceptibility; MECP2)

## Research Objectives

Please provide a comprehensive research report on **Autism, susceptibility to, X-linked 3 (AUTSX3; MECP2-related X-linked autism susceptibility)** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Autism, susceptibility to, X-linked 3 (AUTSX3; MECP2-related X-linked autism susceptibility)
- **MONDO ID:** MONDO:0010342 (if available)
- **Category:** Complex (X-linked genetic susceptibility; MECP2)

## Research Objectives

Please provide a comprehensive research report on **Autism, susceptibility to, X-linked 3 (AUTSX3; MECP2-related X-linked autism susceptibility)** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# AUTSX3 / MECP2-related X-linked autism susceptibility

## Executive summary and curation warning

**AUTSX3 (“autism susceptibility, X-linked 3”; OMIM 300496)** is a historical phenotype label linking autism susceptibility to **MECP2** at Xq28. Modern literature does not support it as a well-bounded disease with its own validated diagnostic criteria, phenotype frequencies, prevalence, natural history, or treatment evidence. It is better curated as a **legacy MECP2-associated phenotype within the broader spectrum of male MECP2-related neurodevelopmental disorders**, with explicit cross-references to Rett syndrome (RTT), severe neonatal encephalopathy, X-linked intellectual developmental disorder 13/PPM-X, and MECP2 duplication syndrome—but not treated as synonymous with any of them. Contemporary reviews explicitly list autism susceptibility (OMIM 300496) among male MECP2 phenotypes, while emphasizing a spectrum from mild intellectual impairment to neonatal encephalopathy and premature death. (pascualalonso2021mecp2relateddisordersin pages 2-4, pascualalonso2021mecp2relateddisordersin pages 1-2)

Accordingly, statistics and treatment results below are labeled either **direct AUTSX3 evidence** or **MECP2-spectrum/RTT comparator evidence**. RTT prevalence, survival, regression, and trofinetide data must not be entered as AUTSX3-specific facts.

| Entity | Molecular lesion | Typical sex / inheritance | Defining phenotype / course | Evidence strength | Key caveat |
|---|---|---|---|---|---|
| AUTSX3 / autism susceptibility, X-linked 3 (OMIM 300496) | Historical MECP2-associated susceptibility label; not well delineated as a modern, discrete clinical entity in the gathered evidence | X-linked; historically associated with males carrying MECP2 variants, but current literature tends to subsume such cases under broader MECP2-related disorders (pascualalonso2021mecp2relateddisordersin pages 1-2, balicza2024multilevelevidenceof pages 1-2) | Autism/autistic features may occur with MECP2 variants, but the gathered evidence does not define a consistent standalone natural history, phenotype spectrum, prevalence, or diagnostic criteria for AUTSX3 specifically (pascualalonso2021mecp2relateddisordersin pages 1-2, pascualalonso2021mecp2relateddisordersin pages 11-12) | Sparse / historical | Do **not** transfer Rett syndrome prevalence, survival, or treatment data directly to AUTSX3; current evidence supports treating AUTSX3 as a legacy nosologic label within the wider MECP2-related disorder spectrum (pascualalonso2021mecp2relateddisordersin pages 1-2, pascualalonso2021mecp2relateddisordersin pages 11-12) |
| Rett syndrome due to MECP2 loss of function | MECP2 loss-of-function variants; >300 LOF variants documented, with 8 hotspot variants accounting for >60% of cases (gold2024rettsyndrome pages 3-4, gold2024rettsyndrome pages 1-2) | Predominantly females; X-linked dominant with major effect in heterozygous females; males usually require mosaicism or 47,XXY to present with classic RTT (coleman2022mosaicismofcommon pages 8-9, gold2024rettsyndrome pages 3-4, gold2024rettsyndrome pages 1-2) | Regression after early apparently typical development with loss of spoken language and purposeful hand use, hand stereotypies, gait impairment; chronic neurodevelopmental course with stabilization after regression and multisystem comorbidity burden (gold2024rettsyndrome pages 1-2, petriti2023globalprevalenceof pages 1-2, may2024characterizingthejourney pages 1-2) | Strong | RTT statistics apply to RTT, not to historical AUTSX3; X-inactivation modifies severity and blood XCI may not reflect brain disease (gold2024rettsyndrome pages 3-4, percy2024rettsyndromethe pages 2-3) |
| Severe neonatal encephalopathy in males (OMIM 300673) | Usually severe pathogenic MECP2 loss-of-function variants, often overlapping with classic female RTT-causing variants in hemizygous males (pascualalonso2021mecp2relateddisordersin pages 2-4, balicza2024multilevelevidenceof pages 1-2) | Typically 46,XY males; X-linked; often de novo | Severe early encephalopathy with neonatal/infantile onset, profound developmental impairment, ventilatory needs, and early death; considered among the most severe male MECP2 phenotypes (pascualalonso2021mecp2relateddisordersin pages 2-4, pascualalonso2021mecp2relateddisordersin pages 4-5, balicza2024multilevelevidenceof pages 1-2) | Moderate | Male MECP2 genotype-phenotype prediction remains limited; severity is broad and individual cases may not fit neatly into categories (coleman2022mosaicismofcommon pages 8-9, coleman2022mosaicismofcommon pages 8-8) |
| X-linked intellectual developmental disorder 13 / PPM-X (OMIM 300055) | Pathogenic MECP2 variants, including missense, truncating, and other alleles associated with non-classic male phenotypes (pascualalonso2021mecp2relateddisordersin pages 1-2, pascualalonso2021mecp2relateddisordersin pages 11-12, balicza2024multilevelevidenceof pages 1-2) | Usually males; X-linked | Cognitive impairment / intellectual disability with variable neurologic and behavioral involvement; may be static or less progressive than RTT/neonatal encephalopathy and may include autism-related features (pascualalonso2021mecp2relateddisordersin pages 2-4, pascualalonso2021mecp2relateddisordersin pages 11-12, balicza2024multilevelevidenceof pages 1-2) | Moderate | Boundaries with AUTSX3 and other historical MECP2 male diagnoses are blurred in modern literature; classification has shifted toward broader “MECP2-related disorders in males” (pascualalonso2021mecp2relateddisordersin pages 2-4, pascualalonso2021mecp2relateddisordersin pages 1-2) |
| MECP2 duplication syndrome (OMIM 300260) | Copy-number gain / duplication (or triplication) involving MECP2; dosage gain rather than loss of function (pascualalonso2021mecp2relateddisordersin pages 5-7) | Predominantly males; X-linked, often inherited from asymptomatic or mildly affected carrier mothers with skewed XCI (pascualalonso2021mecp2relateddisordersin pages 5-7, pascualalonso2021mecp2relateddisordersin pages 4-5) | Hypotonia, developmental delay, moderate-to-severe intellectual disability, poor/absent speech, autistic features, progressive spasticity, recurrent respiratory infections, GI problems, epilepsy in >50%, and possible motor regression/loss of ambulation over time (pascualalonso2021mecp2relateddisordersin pages 5-7) | Strong | Pathobiology is opposite in direction to RTT (gene dosage gain vs loss); should not be grouped with AUTSX3/RTT for prognosis or treatment assumptions (pascualalonso2021mecp2relateddisordersin pages 5-7, pascualalonso2021mecp2relateddisordersin pages 4-5) |


*Table: This table distinguishes the historical AUTSX3 label from better-supported MECP2-related entities. It is useful for preventing misclassification, especially the inappropriate reuse of Rett syndrome statistics for AUTSX3.*

## 1. Disease information

### Definition and identifiers

- **Preferred knowledge-base label:** Autism susceptibility, X-linked 3 (AUTSX3), MECP2-associated.
- **OMIM:** **300496**.
- **Gene:** **MECP2**, methyl-CpG binding protein 2; Xq28. Modern reviews identify MECP2 as dosage-sensitive: loss-of-function (LOF) produces RTT and related encephalopathies, whereas copy-number gain causes MECP2 duplication syndrome. (pascualalonso2021mecp2relateddisordersin pages 1-2, pascualalonso2021mecp2relateddisordersin pages 5-7)
- **MONDO:** The user-supplied mapping is **MONDO:0010342**; it should be validated against the current MONDO release before production import because the literature retrieved here did not independently confirm that mapping.
- **Orphanet:** No clearly supported AUTSX3-specific Orphanet entity was identified.
- **ICD-10/ICD-11, MeSH, SNOMED CT:** No dedicated AUTSX3 code was identified. Coding should ordinarily reflect the observed clinical diagnosis—autism spectrum disorder, intellectual developmental disorder, Rett syndrome, or another defined MECP2-related disorder—rather than assuming these are equivalent.
- **Synonyms:** AUTSX3; autism susceptibility, X-linked 3; MECP2-related X-linked autism susceptibility; MECP2-associated autism susceptibility.

**Evidence provenance:** AUTSX3 itself is represented mainly by aggregated disease-level resources and historical case literature. Current clinical and mechanistic understanding comes from aggregated MECP2/RTT literature, natural-history registries, individual male cases, cellular systems, and model organisms—not EHR-derived AUTSX3 cohorts.

## 2. Etiology, risk, protection, and environment

### Causal and genetic factors

The strongest causal factor is a **germline or post-zygotic MECP2 variant** that alters MeCP2 abundance or function. For the historical AUTSX3 label, however, variant-specific causality and penetrance are insufficiently delineated. Male MECP2 disorders encompass missense, nonsense, frameshift, splice, deletion, mosaic, and dosage variants, and the same variant class can produce different clinical diagnoses. Pathogenic MECP2 variants have been estimated in approximately **2% of males with intellectual disability**, but this is not an AUTSX3 prevalence or diagnostic yield. (pascualalonso2021mecp2relateddisordersin pages 11-12, balicza2024multilevelevidenceof pages 1-2)

Relevant genetic modifiers include:

- **Sex and hemizygosity:** A 46,XY male has no second normal MECP2 allele.
- **Somatic mosaicism:** It can attenuate an otherwise severe allele and permit survival. Two males with classic RTT were reported with mosaic **c.730C>T (p.Gln244\*)** and **c.397C>T (p.Arg133Cys)** variants; male genotype–phenotype correlations remain too sparse for reliable prediction. (coleman2022mosaicismofcommon pages 8-9, coleman2022mosaicismofcommon pages 8-8)
- **47,XXY karyotype:** A second X chromosome can permit a female-like RTT phenotype in males. (pascualalonso2021mecp2relateddisordersin pages 2-4)
- **X-chromosome inactivation (XCI):** In heterozygous females, skewing modifies expressivity; blood XCI does not necessarily represent brain XCI. Up to 36% of one natural-history cohort showed significant skewing. (gold2024rettsyndrome pages 3-4, percy2024rettsyndromethe pages 2-3)
- **Allelic severity and protein domain:** RTT comparator data associate R106W, R168*, R255*, and R270* with greater severity; R133C, R294*, and R306C tend to be milder and T158M intermediate. These relationships cannot be transferred uncritically to males or AUTSX3. (gold2024rettsyndrome pages 3-4)

### Non-genetic risk, protective factors, and gene–environment interaction

No reproducible environmental, occupational, dietary, lifestyle, infectious, vaccine-related, or toxin exposure has been established as a cause or specific modifier of AUTSX3. No validated protective MECP2 allele or environmental protective factor was identified. General developmental environment and access to early support may modify functional outcomes, but do not prevent the molecular disorder. The best-supported “gene–environment” effects are activity- and development-dependent neuronal consequences of altered epigenetic regulation, not a proven epidemiological exposure interaction.

## 3. Phenotypes

### Directly defensible AUTSX3 phenotype

The narrowly defensible phenotype is **early-onset neurodevelopmental impairment with autism/autistic features**, variably accompanied by intellectual disability and speech or psychomotor delay. Modern male MECP2 literature stresses that manifestations range from mild cognitive impairment through progressive or neonatal encephalopathy; therefore, frequencies and a fixed progression pattern cannot be assigned to AUTSX3. (pascualalonso2021mecp2relateddisordersin pages 2-4, pascualalonso2021mecp2relateddisordersin pages 1-2)

Suggested ontology annotations:

- Autism / autistic behavior — **HP:0000717**
- Intellectual disability — **HP:0001249**
- Global developmental delay — **HP:0001263**
- Delayed speech and language development — **HP:0000750**
- Abnormal social behavior — **HP:0012433**
- Stereotypic behavior — **HP:0000733**
- Hypotonia — **HP:0001252**
- Seizure — **HP:0001250**, only where observed
- Abnormality of gait — **HP:0001288**, only where observed

### RTT/MECP2-spectrum comparator phenotype

Classic RTT requires regression followed by recovery or stabilization and four core features: loss of purposeful hand skills, loss of spoken language, gait abnormality, and stereotypic hand movements. Associated manifestations include seizures, breathing and autonomic abnormalities, cardiac abnormalities, sleep disturbance, growth deceleration, constipation, scoliosis, and autistic features. MECP2 variants are found in approximately **95–97% of typical RTT** and about **85% of atypical RTT**. These are comparator facts, not AUTSX3 criteria. (gold2024rettsyndrome pages 1-2, petriti2023globalprevalenceof pages 1-2)

Caregiver-priority data from **925** participants in the US natural-history study identified communication, seizures, walking/balance, hand use, and constipation as the major concerns, demonstrating substantial effects on independence and family quality of life. Concern rankings varied by age, severity, seizure activity, and MECP2 variant. This is RTT/related-disorder evidence. 

**Suggested additional HPO terms for an individual with RTT-like manifestations:** loss of acquired skills (**HP:0002376**), hand stereotypies (**HP:0000733**), absent speech (**HP:0001344**), acquired microcephaly (**HP:0005484**), episodic hyperventilation (**HP:0002883**), bruxism (**HP:0003763**), constipation (**HP:0002019**), scoliosis (**HP:0002650**), and sleep disturbance (**HP:0002360**).

## 4. Genetic and molecular information

### Gene and variants

- **MECP2** is the sole established gene attached to AUTSX3; suggested identifier **HGNC:6990**.
- Pathogenicity must be assessed per ACMG/AMP criteria using phenotype, inheritance, population frequency, functional evidence, and ClinVar/ClinGen assertions. A MECP2 variant alone does not justify the AUTSX3 label.
- Pathogenic MECP2 alleles are generally exceedingly rare or absent in population databases; exact gnomAD frequency must be reported variant-by-variant.
- Most clinically causal variants are **germline**, commonly de novo in RTT. Post-zygotic somatic mosaicism is particularly important in surviving 46,XY males. (coleman2022mosaicismofcommon pages 8-9, coleman2022mosaicismofcommon pages 8-8)
- More than **300 LOF variants** are documented in RTT; eight recurrent variants account for over **60%** of reported RTT cases. Variant classes include missense, nonsense, frameshift, splice, and large deletion. (gold2024rettsyndrome pages 3-4, gold2024rettsyndrome pages 1-2)
- MECP2 duplications/triplications are a separate dosage-gain disorder. They should not be annotated as AUTSX3-causing variants. (pascualalonso2021mecp2relateddisordersin pages 5-7)

### Functional consequences and epigenetics

MeCP2 binds methylated DNA, including neuronal non-CG methylation and 5-hydroxymethylcytosine contexts, organizes chromatin, recruits transcriptional coregulators, and modulates transcription rather than acting as a simple universal repressor. LOF perturbs long neuronal genes, synaptic programs, RNA processing, and cell homeostasis. The downstream phenotype is strongly influenced by XCI mosaicism in females and cell-type-specific MeCP2 requirements. (gold2024rettsyndrome pages 3-4, gold2024rettsyndrome pages 4-6, gold2024rettsyndrome pages 14-14)

No validated modifier gene is routinely used prognostically. **TCF20-complex biology**, BDNF/miR-132 feedback, and XCI regulators are plausible mechanistic modifiers, but not established clinical modifier tests.

## 5. Environmental, lifestyle, and infectious information

AUTSX3 is not an infectious, toxic, radiation-induced, or lifestyle disease. No pathogen, diet, smoking, alcohol, exercise pattern, or occupational exposure is established as causal. Environmental management—communication access, physical activity, nutrition, seizure safety, sleep support, and avoidance of medication-related respiratory or cardiac risk—can influence morbidity but not the underlying genotype. Vaccination is not implicated in causation.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic event:** pathogenic or function-altering MECP2 allele, mosaicism, or abnormal dosage.
2. **Nuclear/epigenomic defect:** abnormal methylated-DNA recognition, chromatin organization, transcriptional modulation, and interactions with coregulatory complexes.
3. **Cellular dysregulation:** altered BDNF/IGF1 signaling, mTOR–AKT activity, protein synthesis, synaptic maturation, neurotransmitter balance, mitochondrial respiration, lipid metabolism, calcium handling, and redox homeostasis. (gold2024rettsyndrome pages 4-6)
4. **Circuit dysfunction:** abnormal excitatory–inhibitory balance and impaired maturation/homeostasis across cortical and subcortical networks.
5. **Clinical effects:** impaired communication and cognition, stereotypies, motor dysfunction, seizures, autonomic and respiratory abnormalities, and—in severe RTT-like disease—regression.

### Cell types and processes

- **Neurons:** MeCP2 is abundant in mature neurons; deficient neurons are smaller, have shorter and less-branched dendrites and atypical spines. Suggested CL terms: neuron (**CL:0000540**), glutamatergic neuron (**CL:0000679**), GABAergic neuron (**CL:0000617**).
- **Astrocytes:** Astrocyte-specific Mecp2 loss causes non-cell-autonomous neuronal injury, reversible after re-expression in mice. Human organoid/cell work shows mitochondrial abnormalities, impaired respiration, altered TCA/electron-transport proteins, amino-acid stress, and elevated ROS. Suggested term: astrocyte (**CL:0000127**). (gold2024rettsyndrome pages 3-4, gold2024rettsyndrome pages 4-6)
- **Microglia:** MeCP2 deficiency can alter inflammatory signaling and glutamate release. Suggested term: microglial cell (**CL:0000129**). (gold2024rettsyndrome pages 4-6)
- **Oligodendroglial and other glial cells:** likely contribute, but their AUTSX3-specific role is unquantified.

Suggested GO annotations include regulation of transcription by RNA polymerase II (**GO:0006357**), chromatin organization (**GO:0006325**), DNA methylation-dependent heterochromatin formation (**GO:0006346**), synapse organization (**GO:0050808**), regulation of synaptic plasticity (**GO:0048167**), mitochondrial electron transport (**GO:0006120**), cellular response to oxidative stress (**GO:0034599**), and nervous-system development (**GO:0007399**). Relevant cellular components include nucleus (**GO:0005634**), chromatin (**GO:0000785**), synapse (**GO:0045202**), postsynaptic density (**GO:0014069**), and mitochondrion (**GO:0005739**).

### 2023–2024 molecular profiling

- A 2024 longitudinal single-nucleus RNA-seq study of Mecp2e1-mutant cortex found **sixfold more differentially expressed genes in mutant females than males**, female changes before overt symptoms, and dynamic non-cell-autonomous homeostatic effects. This is mouse-model evidence, not an AUTSX3 biomarker.
- A 2024 human astrocyte/organoid multi-omics study found smaller mitochondria—especially in glia—reduced astrocytic respiration, altered TCA/electron-transport proteins, increased ROS, and effects of transferred mutant mitochondria on cortical-neuron activity. 
- A 2024 forebrain-organoid study using female **MECP2 R255X** hiPSCs and isogenic controls profiled days 0, 13, 40, and 75. RTT organoids showed late changes in EV hsa-miR-302/367 and strong C14MC upregulation, proposed as candidate progression biomarkers—not validated clinical tests. (sangani2024involvementofextracellular pages 1-3)
- A 2024 PNAS meta-analysis of human-brain single-cell data found marked MECP2 expression variability across cell types, regions, developmental stages, and donors. This variability defines both a minimum restoration target and an upper toxicology margin for gene-restorative therapy. (zito2024variableexpressionof pages 1-2)
- RettDb, released in 2024, integrates mouse Mecp2 genomic and transcriptomic datasets to support target discovery; it is a research resource rather than a diagnostic database.

Representative exact abstract wording includes: **“Non-cell-autonomous effects were prominent and dynamic across disease progression”** in the single-cell mouse study; and the organoid study reported that C14MC miRNAs showed **“strong upregulation in RTT forebrain organoids.”** (sangani2024involvementofextracellular pages 1-3)

## 7. Anatomical structures affected

The primary system is the **central nervous system**, particularly cerebral cortical networks. RTT comparator neuropathology shows globally reduced brain and neuronal size, higher neuronal packing density, reduced dendritic arborization, and atypical spines without a primary neurodegenerative pattern. MRI shows generalized volume reduction, selective dorsal parietal reduction, frontal volume–severity correlations, and white-matter tract abnormalities including the superior longitudinal fasciculus. (gold2024rettsyndrome pages 1-2, gold2024rettsyndrome pages 4-6)

Suggested anatomy terms:

- Brain — **UBERON:0000955**
- Cerebral cortex — **UBERON:0000956**
- Frontal cortex — **UBERON:0001870**
- Parietal cortex — **UBERON:0001872**
- White matter — **UBERON:0002316**
- Spinal cord — **UBERON:0002240**, where motor/autonomic involvement is documented
- Skeletal muscle, gastrointestinal tract, heart, and respiratory system are secondary functional sites in severe MECP2 disorders.

There is no established lateralization pattern. Subcellular emphasis is nuclear chromatin, synaptic compartments, and mitochondria.

## 8. Temporal development

**AUTSX3-specific course:** not established. Autism and developmental delay ordinarily emerge in infancy or early childhood, but historical AUTSX3 does not have validated stages.

**RTT comparator:** development may appear relatively typical initially, followed by regression commonly beginning around **6–18 months**, then partial recovery or stabilization and a chronic lifelong course. Head-growth deceleration can begin from the second month. Disease severity and motor dysfunction may continue to increase, especially during childhood and adolescence. (petriti2023globalprevalenceof pages 1-2, may2024characterizingthejourney pages 1-2, percy2024rettsyndromethe pages 2-3)

A 2024 real-world cohort of **455 females**, followed for a median of four years, found an annual pediatric Clinical Severity Scale increase of **0.24** (95% CI 0.03–0.44), while Motor Behavioral Assessment scores increased **1.12/year** (95% CI 0.63–1.60) in pediatric participants and **0.97/year** (95% CI 0.53–1.41) in classic RTT. These values should not be assigned to AUTSX3. (may2024characterizingthejourney pages 1-2)

## 9. Inheritance and population

### Inheritance

The locus is **X-linked**, but recurrence depends on the variant and parental status. Many severe LOF cases are de novo. Carrier females may be asymptomatic or variably affected because of XCI. A carrier mother can transmit the allele to 50% of pregnancies; sons receiving a pathogenic allele are hemizygous and may be more severely affected. Parental and low-level germline mosaicism make recurrence risk non-zero even when blood testing is negative.

Penetrance and expressivity for AUTSX3 are unknown. Male MECP2 expressivity is highly variable and cannot be reliably predicted from variant identity alone. Genetic anticipation and consanguinity are not established features. No AUTSX3 founder variant or carrier frequency is established. (coleman2022mosaicismofcommon pages 8-9, coleman2022mosaicismofcommon pages 8-8)

### Epidemiology

No AUTSX3-specific prevalence, incidence, sex ratio, ethnic distribution, geographic clustering, or carrier frequency is available. This is likely partly due to obsolete/overlapping nosology.

For context only, a 2023 meta-analysis of ten RTT studies—**9.57 million females and 673 cases**—estimated RTT prevalence at **7.1 per 100,000 females** (95% CI 4.8–10.5). RTT is almost exclusively diagnosed in females. This is not AUTSX3 epidemiology. (petriti2023globalprevalenceof pages 1-2)

## 10. Diagnostics

### Clinical diagnosis

AUTSX3 has no standalone clinical criteria. Assess autism using standard DSM-5-TR/ICD-11 criteria and characterize development, cognition, language, movement, regression, hand stereotypies, breathing, sleep, seizures, feeding, growth, and autonomic function. A MECP2 finding should trigger phenotype-driven classification rather than automatic assignment of RTT or AUTSX3.

### Recommended genetic approach

1. **Trio exome or genome sequencing** with copy-number and mosaic-variant calling is generally the most efficient approach for unexplained syndromic autism/developmental delay.
2. **MECP2 sequencing with deletion/duplication analysis** is appropriate where RTT, male MECP2 encephalopathy, or a familial MECP2 disorder is suspected.
3. Use **high-depth NGS** and consider **digital PCR** or an orthogonal deep assay when mosaicism is suspected; conventional Sanger sequencing may miss variants below approximately 15–20% allele fraction. (coleman2022mosaicismofcommon pages 8-9, pascualalonso2021mecp2relateddisordersin pages 4-5)
4. **Chromosomal microarray** detects MECP2-region deletions/duplications and other pathogenic CNVs. Whole-gene duplication suggests MDS, not AUTSX3.
5. **Karyotype** is useful in a male with a female-like RTT phenotype to detect 47,XXY.
6. RNA studies may resolve splice variants; methylation/XCI studies can be supportive in females but are not definitive because blood may not reflect brain.

FISH, mitochondrial DNA testing, repeat-expansion testing, biopsy, or metabolomics are not first-line AUTSX3 tests unless another differential diagnosis is suspected. Elevated lactate, muscle pathology, or respiratory-chain changes can occur in individual MECP2 cases but are neither sensitive nor specific. A 2024 male p.Arg179Trp case showed elevated exercise lactate, muscle histopathology, and transcriptomic oxidative-phosphorylation abnormalities. (balicza2024multilevelevidenceof pages 1-2)

### Differential diagnosis

Important alternatives include classic/atypical RTT, MECP2 duplication syndrome, severe neonatal encephalopathy due to MECP2, CDKL5 deficiency disorder, FOXG1 syndrome, fragile X syndrome, Angelman syndrome, Phelan–McDermid syndrome, Pitt–Hopkins syndrome, other monogenic autism/ID syndromes, cerebral palsy, mitochondrial disease, and epileptic encephalopathy.

There is no validated newborn biochemical screen. Family-specific cascade, carrier, prenatal, and preimplantation testing are possible after a pathogenic variant is established.

## 11. Outcome and prognosis

No AUTSX3-specific survival, mortality, disability, recovery, or prognostic model exists. Prognosis should be individualized from sex, variant mechanism, mosaic fraction, neurological severity, seizures, feeding/respiratory status, mobility, and the best-fitting modern MECP2 diagnosis.

RTT comparator data indicate chronic disability rather than progressive neuronal death. Approximately **70% survive into their 50s**, and survival exceeds **70% at age 45** in modern cohorts; cardiorespiratory disease is a major cause of death and sudden death accounts for an estimated 20–30% of deaths. These figures are not applicable to AUTSX3 without a Rett phenotype. (gold2024rettsyndrome pages 1-2, may2024characterizingthejourney pages 1-2)

In the 2024 US registry analysis, **44.6%** had a hospital or emergency-room visit during follow-up. Pediatric participants used physical therapy more often than adults (**87.3% versus 40.2%**) and speech-language therapy (**86.8% versus 23.9%**), illustrating substantial lifelong functional burden and gaps in adult services. (may2024characterizingthejourney pages 1-2)

## 12. Treatment and applications

### AUTSX3-specific treatment

There is **no approved AUTSX3-specific or genotype-corrective therapy**, no established pharmacogenomic algorithm, and no AUTSX3-specific randomized trial. Management is phenotype-directed:

- autism-focused developmental and behavioral intervention;
- augmentative and alternative communication;
- speech-language, occupational, and physical therapy;
- individualized education;
- standard antiseizure treatment where required;
- management of sleep, constipation, feeding, reflux, scoliosis, tone, mobility, anxiety, and respiratory/autonomic problems.

Suggested MAXO concepts include genetic counseling (**MAXO:0001004**), molecular genetic testing, developmental assessment, speech therapy, occupational therapy, physical therapy, augmentative communication, EEG, seizure management, nutritional management, and scoliosis surveillance; exact current MAXO identifiers should be verified before database import.

### Rett comparator and recent developments

**Trofinetide**, a synthetic IGF1-derived tripeptide analogue, became the first FDA-approved RTT treatment on **10 March 2023**. Phase III evidence showed statistically significant improvement in RTT Behaviour Questionnaire and clinician global-improvement outcomes, but it is symptomatic, not gene-corrective. Common clinically important adverse effects are diarrhea, vomiting, and weight loss, sometimes causing discontinuation. It is approved for RTT—not AUTSX3—and efficacy in an autistic male carrying a MECP2 variant cannot be assumed. (gold2024rettsyndrome pages 1-2, gold2024rettsyndrome pages 14-14)

Gene replacement, regulated AAV-MECP2 delivery, RNA editing, CRISPR-based editing, and selective reactivation of the normal inactive X are investigational. Because both deficiency and excess MECP2 are harmful, dose control and cell/region targeting are central safety constraints. Human-brain single-cell data reveal wide physiological MECP2 expression ranges that may help define therapeutic windows. (gold2024rettsyndrome pages 14-14, zito2024variableexpressionof pages 1-2)

A 2024 individual male p.Arg179Trp report described improvement of prominent negative psychiatric symptoms with cariprazine, but this is hypothesis-generating single-patient evidence, not a disease treatment recommendation. (balicza2024multilevelevidenceof pages 1-2)

## 13. Prevention

Primary prevention through lifestyle modification, vaccination, infection control, or medication is not available. Relevant measures are reproductive and secondary/tertiary prevention:

- pre-test and post-test genetic counseling;
- parental testing, including consideration of low-level mosaicism;
- cascade testing in relatives;
- prenatal diagnosis or preimplantation genetic testing for a known familial pathogenic variant;
- early developmental surveillance and intervention;
- prevention of complications through seizure safety, nutrition and aspiration assessment, mobility and bone-health support, scoliosis surveillance, sleep and respiratory assessment, and ECG/QTc review where clinically indicated.

No population newborn or universal carrier-screening program is established for AUTSX3. Risk-stratified family testing is more appropriate.

## 14. Other species and natural disease

No well-established naturally occurring AUTSX3-equivalent veterinary disease or breed predisposition was identified. MECP2 is evolutionarily conserved in vertebrates, but animal work largely uses engineered models. There is no infectious transmission, zoonotic potential, or cross-species contagion.

Useful taxa include human (**NCBI Taxonomy 9606**), house mouse (**10090**), rat (**10116**), zebrafish (**7955**), fruit fly (**7227**), and *Caenorhabditis elegans* (**6239**). Orthologue identifiers should be retrieved from the current NCBI Gene/Alliance release at ingestion time.

## 15. Model organisms and experimental systems

### Models

- **Mouse:** hemizygous null males, heterozygous females, conditional cell-type deletions, recurrent human-variant knock-ins, duplication models, and Mecp2e1 isoform models. They reproduce motor dysfunction, stereotypies, breathing abnormalities, seizures, altered social behavior, reduced growth, and shortened lifespan. Conditional restoration demonstrates substantial reversibility, supporting a disorder of neuronal maintenance/homeostasis rather than irreversible degeneration.
- **Rat and zebrafish:** useful for behavior, respiration, development, pharmacology, and circuit analysis.
- **Drosophila/C. elegans:** useful for conserved pathways and modifier screens, but they incompletely reproduce mammalian MeCP2/XCI biology.
- **Patient-derived iPSC neurons and astrocytes:** preserve patient genotype and, in female clones, XCI state; useful for synaptic, mitochondrial, and drug studies.
- **Isogenic CRISPR-corrected lines:** reduce background-genome confounding.
- **Cerebral/forebrain organoids:** model human developmental timing, cell interactions, and extracellular-vesicle biomarkers. The 2024 R255X organoid study identified RTT-specific EV miRNA trajectories. (sangani2024involvementofextracellular pages 1-3)
- **Single-cell and spatial transcriptomics:** resolve vulnerable neuronal and glial populations and non-cell-autonomous effects. (zito2024variableexpressionof pages 1-2)

### Limitations

Male null mice progress rapidly and do not model female XCI mosaicism; heterozygous females are more clinically relevant but variable and slower. Rodent social behavior is not equivalent to human autism, and organoids lack mature vasculature, full immune representation, long-range circuitry, and lifelong maturation. Most models represent classic RTT-causing LOF, not the poorly defined historical AUTSX3 phenotype.

## Knowledge-base conclusions

1. Curate AUTSX3 as a **historical, sparse MECP2-associated autism susceptibility phenotype**, not as a synonym for Rett syndrome.
2. Record **OMIM 300496** and MECP2/HGNC:6990, but validate the supplied MONDO mapping before release.
3. Do not assign RTT prevalence, survival, regression frequencies, or trofinetide indication to AUTSX3.
4. Prefer a patient-specific modern diagnosis based on variant mechanism and phenotype: RTT, male MECP2 encephalopathy, MECP2-related intellectual developmental disorder, or MECP2 duplication syndrome.
5. Mark AUTSX3-specific incidence, penetrance, protective factors, variant frequencies, natural history, biomarkers, and treatment response as **not established**.

### Key source URLs and publication dates

- Pascual-Alonso et al., **September 2021**, *MECP2-Related Disorders in Males*: https://doi.org/10.3390/ijms22179610. (pascualalonso2021mecp2relateddisordersin pages 2-4, pascualalonso2021mecp2relateddisordersin pages 1-2)
- Petriti et al., **January 2023**, global RTT prevalence meta-analysis: https://doi.org/10.1186/s13643-023-02169-6. (petriti2023globalprevalenceof pages 1-2)
- May et al., **July 2024**, US real-world natural-history study: https://doi.org/10.1186/s11689-024-09557-6. (may2024characterizingthejourney pages 1-2)
- Zito and Lee, **February 2024**, human-brain single-cell expression: https://doi.org/10.1073/pnas.2312757121. (zito2024variableexpressionof pages 1-2)
- Sangani et al., **September 2024**, RTT brain-organoid EV miRNAs: https://doi.org/10.1007/s00018-024-05409-7. (sangani2024involvementofextracellular pages 1-3)
- Gold et al., **November 2024**, *Nature Reviews Disease Primers*: https://doi.org/10.1038/s41572-024-00568-0. (gold2024rettsyndrome pages 3-4, gold2024rettsyndrome pages 1-2)
- Balicza et al., **January 2024**, male MECP2 mitochondrial case: https://doi.org/10.3389/fpsyt.2023.1301272. (balicza2024multilevelevidenceof pages 1-2)

**PMID note:** PMID values were not exposed reliably in the retrieved full-text metadata; DOIs and journal dates are therefore supplied rather than risking incorrect PMID assignment.

References

1. (pascualalonso2021mecp2relateddisordersin pages 2-4): Ainhoa Pascual-Alonso, Antonio F. Martínez-Monseny, Clara Xiol, and Judith Armstrong. Mecp2-related disorders in males. International Journal of Molecular Sciences, 22:9610, Sep 2021. URL: https://doi.org/10.3390/ijms22179610, doi:10.3390/ijms22179610. This article has 57 citations.

2. (pascualalonso2021mecp2relateddisordersin pages 1-2): Ainhoa Pascual-Alonso, Antonio F. Martínez-Monseny, Clara Xiol, and Judith Armstrong. Mecp2-related disorders in males. International Journal of Molecular Sciences, 22:9610, Sep 2021. URL: https://doi.org/10.3390/ijms22179610, doi:10.3390/ijms22179610. This article has 57 citations.

3. (balicza2024multilevelevidenceof pages 1-2): Peter Balicza, Andras Gezsi, Mariann Fedor, Judit C. Sagi, Aniko Gal, Noemi Agnes Varga, and Maria Judit Molnar. Multilevel evidence of mecp2-associated mitochondrial dysfunction and its therapeutic implications. Frontiers in Psychiatry, Jan 2024. URL: https://doi.org/10.3389/fpsyt.2023.1301272, doi:10.3389/fpsyt.2023.1301272. This article has 8 citations.

4. (pascualalonso2021mecp2relateddisordersin pages 11-12): Ainhoa Pascual-Alonso, Antonio F. Martínez-Monseny, Clara Xiol, and Judith Armstrong. Mecp2-related disorders in males. International Journal of Molecular Sciences, 22:9610, Sep 2021. URL: https://doi.org/10.3390/ijms22179610, doi:10.3390/ijms22179610. This article has 57 citations.

5. (gold2024rettsyndrome pages 3-4): Wendy A. Gold, Alan K. Percy, Jeffrey L. Neul, Stuart R. Cobb, Lucas Pozzo-Miller, Jasmeen K. Issar, Bruria Ben-Zeev, Aglaia Vignoli, and Walter E. Kaufmann. Rett syndrome. Nov 2024. URL: https://doi.org/10.1038/s41572-024-00568-0, doi:10.1038/s41572-024-00568-0. This article has 82 citations.

6. (gold2024rettsyndrome pages 1-2): Wendy A. Gold, Alan K. Percy, Jeffrey L. Neul, Stuart R. Cobb, Lucas Pozzo-Miller, Jasmeen K. Issar, Bruria Ben-Zeev, Aglaia Vignoli, and Walter E. Kaufmann. Rett syndrome. Nov 2024. URL: https://doi.org/10.1038/s41572-024-00568-0, doi:10.1038/s41572-024-00568-0. This article has 82 citations.

7. (coleman2022mosaicismofcommon pages 8-9): Jessica A. Cooley Coleman, Timothy Fee, Renee Bend, Raymond Louie, Fran Annese, Jennifer Stallworth, Jessica Worthington, Caroline Black Buchanan, David B. Everman, Steven Skinner, Michael J. Friez, Julie R. Jones, and Catherine J. Spellicy. Mosaicism of common pathogenic mecp2 variants identified in two males with a clinical diagnosis of rett syndrome. American Journal of Medical Genetics Part A, 188:2988-2998, Aug 2022. URL: https://doi.org/10.1002/ajmg.a.62913, doi:10.1002/ajmg.a.62913. This article has 10 citations.

8. (petriti2023globalprevalenceof pages 1-2): Uarda Petriti, Daniel C. Dudman, Emil Scosyrev, and Sandra Lopez-Leon. Global prevalence of rett syndrome: systematic review and meta-analysis. Systematic Reviews, Jan 2023. URL: https://doi.org/10.1186/s13643-023-02169-6, doi:10.1186/s13643-023-02169-6. This article has 136 citations and is from a peer-reviewed journal.

9. (may2024characterizingthejourney pages 1-2): Damian May, Kalé Kponee-Shovein, Jeffrey L. Neul, Alan K. Percy, Malena Mahendran, Nathaniel Downes, Grace Chen, Talissa Watson, Dominique C. Pichard, Melissa Kennedy, and Patrick Lefebvre. Characterizing the journey of rett syndrome among females in the united states: a real-world evidence study using the rett syndrome natural history study database. Journal of Neurodevelopmental Disorders, Jul 2024. URL: https://doi.org/10.1186/s11689-024-09557-6, doi:10.1186/s11689-024-09557-6. This article has 11 citations and is from a peer-reviewed journal.

10. (percy2024rettsyndromethe pages 2-3): Alan K. Percy, Amitha Ananth, and Jeffrey L. Neul. Rett syndrome: the emerging landscape of treatment strategies. CNS Drugs, 38:851-867, Sep 2024. URL: https://doi.org/10.1007/s40263-024-01106-y, doi:10.1007/s40263-024-01106-y. This article has 41 citations and is from a peer-reviewed journal.

11. (pascualalonso2021mecp2relateddisordersin pages 4-5): Ainhoa Pascual-Alonso, Antonio F. Martínez-Monseny, Clara Xiol, and Judith Armstrong. Mecp2-related disorders in males. International Journal of Molecular Sciences, 22:9610, Sep 2021. URL: https://doi.org/10.3390/ijms22179610, doi:10.3390/ijms22179610. This article has 57 citations.

12. (coleman2022mosaicismofcommon pages 8-8): Jessica A. Cooley Coleman, Timothy Fee, Renee Bend, Raymond Louie, Fran Annese, Jennifer Stallworth, Jessica Worthington, Caroline Black Buchanan, David B. Everman, Steven Skinner, Michael J. Friez, Julie R. Jones, and Catherine J. Spellicy. Mosaicism of common pathogenic mecp2 variants identified in two males with a clinical diagnosis of rett syndrome. American Journal of Medical Genetics Part A, 188:2988-2998, Aug 2022. URL: https://doi.org/10.1002/ajmg.a.62913, doi:10.1002/ajmg.a.62913. This article has 10 citations.

13. (pascualalonso2021mecp2relateddisordersin pages 5-7): Ainhoa Pascual-Alonso, Antonio F. Martínez-Monseny, Clara Xiol, and Judith Armstrong. Mecp2-related disorders in males. International Journal of Molecular Sciences, 22:9610, Sep 2021. URL: https://doi.org/10.3390/ijms22179610, doi:10.3390/ijms22179610. This article has 57 citations.

14. (gold2024rettsyndrome pages 4-6): Wendy A. Gold, Alan K. Percy, Jeffrey L. Neul, Stuart R. Cobb, Lucas Pozzo-Miller, Jasmeen K. Issar, Bruria Ben-Zeev, Aglaia Vignoli, and Walter E. Kaufmann. Rett syndrome. Nov 2024. URL: https://doi.org/10.1038/s41572-024-00568-0, doi:10.1038/s41572-024-00568-0. This article has 82 citations.

15. (gold2024rettsyndrome pages 14-14): Wendy A. Gold, Alan K. Percy, Jeffrey L. Neul, Stuart R. Cobb, Lucas Pozzo-Miller, Jasmeen K. Issar, Bruria Ben-Zeev, Aglaia Vignoli, and Walter E. Kaufmann. Rett syndrome. Nov 2024. URL: https://doi.org/10.1038/s41572-024-00568-0, doi:10.1038/s41572-024-00568-0. This article has 82 citations.

16. (sangani2024involvementofextracellular pages 1-3): Nasim Bahram Sangani, Jarno Koetsier, Ana Rita Gomes, Maria Margarida Diogo, Tiago G. Fernandes, Freek G. Bouwman, Edwin C. M. Mariman, Mehrnaz Ghazvini, Joost Gribnau, Leopold M. G. Curfs, Chris P. Reutelingsperger, and Lars M. T. Eijssen. Involvement of extracellular vesicle microrna clusters in developing healthy and rett syndrome brain organoids. Cellular and Molecular Life Sciences: CMLS, Sep 2024. URL: https://doi.org/10.1007/s00018-024-05409-7, doi:10.1007/s00018-024-05409-7. This article has 15 citations.

17. (zito2024variableexpressionof pages 1-2): Antonino Zito and Jeannie T. Lee. Variable expression of mecp2, cdkl5, and fmr1 in the human brain: implications for gene restorative therapies. Proceedings of the National Academy of Sciences of the United States of America, Feb 2024. URL: https://doi.org/10.1073/pnas.2312757121, doi:10.1073/pnas.2312757121. This article has 15 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autism_Susceptibility_to_X-Linked_3-deep-research-falcon_artifacts/artifact-00.md)