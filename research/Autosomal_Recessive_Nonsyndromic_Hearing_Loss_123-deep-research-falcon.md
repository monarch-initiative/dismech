---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-17T10:59:00.148368'
end_time: '2026-09-17T11:12:16.436496'
duration_seconds: 796.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: DFNB123 STX4-related autosomal recessive nonsyndromic hearing loss
  mondo_id: MONDO:0958277
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 6
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_123-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DFNB123 STX4-related autosomal recessive nonsyndromic hearing loss
- **MONDO ID:** MONDO:0958277 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DFNB123 STX4-related autosomal recessive nonsyndromic hearing loss** covering all of the
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
- **Disease Name:** DFNB123 STX4-related autosomal recessive nonsyndromic hearing loss
- **MONDO ID:** MONDO:0958277 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DFNB123 STX4-related autosomal recessive nonsyndromic hearing loss** covering all of the
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


# DFNB123: STX4-related autosomal-recessive nonsyndromic hearing loss

## Executive summary and evidence scope

DFNB123 is an ultra-rare Mendelian hearing disorder attributed to biallelic loss of **STX4**, encoding syntaxin-4, a plasma-membrane target-SNARE. The defining evidence is one large consanguineous Pakistani pedigree containing eight affected relatives with bilateral severe-to-profound or profound hearing impairment and homozygous **STX4 NM_004604.5:c.232+6T>C**. Segregation was strong (two-point LOD 5.9), and a minigene assay demonstrated exon-3 skipping and a frameshift predicted to cause nonsense-mediated decay. Mouse inner-ear localization and zebrafish knockdown studies provide complementary biological support. Because only one specifically nonsyndromic family has been published, estimates of prevalence, penetrance, natural history, and genotype–phenotype relationships remain provisional. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 1-2, schrauwen2023syntaxin4is pages 3-6)

The defining paper is Schrauwen et al., **“Syntaxin 4 is essential for hearing in human and zebrafish,”** *Human Molecular Genetics* 32:1184–1192, advance publication **10 November 2022**, issue publication **2023**, DOI [10.1093/hmg/ddac257](https://doi.org/10.1093/hmg/ddac257). The retrieved record did not expose a PMID, so no PMID is supplied rather than guessed. A complementary pleiotropic STX4 study is Perl et al., **“Stx4 is required to regulate cardiomyocyte Ca2+ handling during vertebrate cardiac development,”** published **July 2022**, DOI [10.1016/j.xhgg.2022.100115](https://doi.org/10.1016/j.xhgg.2022.100115). (perl2022stx4isrequired pages 11-13, schrauwen2023syntaxin4is pages 1-2)

| Domain | Best-supported finding | Evidence type/sample | Certainty/limitations |
|---|---|---|---|
| Defining human phenotype | One consanguineous Pakistani family had eight affected relatives with bilateral severe-to-profound or profound hearing impairment and no consistent vestibular, facial, neurologic, or cardiac abnormality, supporting a predominantly nonsyndromic phenotype. (schrauwen2023syntaxin4is pages 1-2) | Human pedigree; eight affected and five unaffected examined; pure-tone audiometry at 250–8000 Hz in affected individuals aged 10–25 years. | Strong within-family evidence, but only one DFNB123 family has been published; congenital onset, progression, sex effects, and population-level penetrance remain unestablished. |
| Gene and inheritance | Hearing impairment segregated as an autosomal-recessive trait with homozygous **STX4** NM_004604.5:c.232+6T>C; two-point LOD score was **5.9 at θ=0**. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 1-2) | Exome sequencing, homozygosity mapping, linkage analysis, and Sanger segregation in a large consanguineous pedigree. | Compelling locus-level segregation, although independent DFNB123 families and additional alleles are needed for replication. |
| Variant rarity | c.232+6T>C had gnomAD v2 MAF **7.98×10⁻⁶**, observed heterozygously in two non-Finnish Europeans, and was absent from gnomAD v3, TOPMed Bravo, GME, and the examined All of Us release. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 1-2) | Population-database analysis; ClinVar submission SCV002499562. (schrauwen2023syntaxin4is pages 7-8) | Supports PM2 rarity; carrier frequency and disease prevalence cannot be estimated reliably from one exceptionally rare allele. |
| RNA consequence | A minigene assay demonstrated that c.232+6T>C disrupts splicing and causes **exon 3 skipping**, producing a frameshift predicted to trigger nonsense-mediated decay. (schrauwen2023syntaxin4is pages 2-3) | In-vitro functional splicing assay plus computational prediction. | Direct evidence for aberrant splicing; nonsense-mediated decay and loss of STX4 protein were predicted rather than demonstrated in patient cochlear tissue. |
| Cochlear expression/localization | Murine Stx4a is broadly expressed in the developing and adult inner ear; STX4A localized to the stereocilia, plasma membrane, and cell body/cytoplasm of inner and outer hair cells, with expression also reported in spiral and vestibular ganglia. (schrauwen2023syntaxin4is pages 2-3) | Mouse transcriptomic datasets and P12 cochlear immunofluorescence. | Strong anatomical plausibility, but mouse localization does not by itself identify the precise human pathogenic process. |
| Zebrafish functional evidence | Morpholino knockdown of **stx4** caused abnormal acoustic startle/ABER responses, absent or markedly impaired FM1-43 uptake in neuromast hair cells, developmental abnormalities, and impaired mechanotransduction. (schrauwen2023syntaxin4is pages 3-6) | Zebrafish larvae; ATG- and splice-blocking morpholinos; behavioral, ABER, and FM1-43 assays at 5 dpf. | Supports conserved auditory function, but morpholino toxicity, multisystem developmental defects, lack of a stable auditory knockout/rescue model, and species-specific splicing limit mechanistic specificity. |
| Proposed mechanism | STX4 is a target-SNARE involved in membrane fusion and vesicle trafficking; loss is proposed to disturb apical recycling/stereocilia maintenance and/or basal synaptic trafficking, leading to defective hair-cell mechanotransduction and auditory signaling. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 3-6) | Integration of protein function, cochlear localization, human splicing, and zebrafish assays. | Variant→aberrant splicing and knockdown→mechanotransduction deficit are demonstrated; the intervening vesicle-trafficking and synaptic steps remain inferred. |
| Phenotypic boundary | DFNB123 should be distinguished from broader biallelic STX4 disease: a separate homozygous p.Arg240Trp patient had congenital sensorineural hearing loss, developmental delay, hypotonia, myopathy, and severe dilated cardiomyopathy, while another compound-heterozygous patient had lethal multisystem fetal disease. (perl2022stx4isrequired pages 6-7, perl2022stx4isrequired pages 11-13) | Two unrelated human cases plus CRISPR zebrafish cardiac studies. | Establishes possible allelic pleiotropy but does not show that cardiac or neurologic disease is part of the c.232+6T>C DFNB123 phenotype; ECGs were normal in two members of the nonsyndromic family. |
| Treatment and trials | No DFNB123-specific drug, gene/RNA/cell therapy, or relevant clinical trial has been reported; the defining study recommends adding **STX4** to diagnostic hearing-loss panels. (schrauwen2023syntaxin4is pages 3-6) | Literature and trial search; defining family report. | Evidence is absent rather than negative. A separate pleiotropic p.Arg240Trp patient received a cochlear implant at age six with improved communication, but this single case is not evidence of genotype-specific efficacy. (perl2022stx4isrequired pages 6-7) |


*Table: Concise evidence map for the human genetic association, phenotype, functional validation, mechanistic interpretation, phenotypic boundaries, and therapeutic status of STX4-related DFNB123 hearing loss.*

## 1. Disease information

**Definition.** DFNB123 denotes autosomal-recessive, predominantly nonsyndromic, bilateral severe-to-profound hearing impairment caused by biallelic STX4 dysfunction. The defining family had no consistent vestibular, facial, neurologic, or cardiac phenotype; ECGs were normal in two tested affected relatives. One individual was borderline macrocephalic, but macrocephaly is not established as part of DFNB123. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 3-6)

**Names/synonyms:** DFNB123; STX4-related autosomal-recessive nonsyndromic hearing loss; STX4-related hearing impairment; syntaxin-4-related hearing loss. “STX4-related disorder” should be reserved for the wider allelic spectrum because other biallelic variants have produced multisystem disease. (perl2022stx4isrequired pages 6-7, perl2022stx4isrequired pages 11-13)

**Identifiers.** The user-supplied identifier is **MONDO:0958277**, but it could not be independently verified in the retrieved resources. Open Targets maps STX4 (Ensembl **ENSG00000103496**) to MONDO’s broader “hearing loss, autosomal recessive” (**MONDO:0019588**) and “nonsyndromic genetic hearing loss” (**MONDO:0019497**); its underlying evidence display was sparse and should not replace the primary pedigree report. Disease-specific OMIM, Orphanet, MeSH, ICD-10, and ICD-11 identifiers were not recoverable from the retrieved evidence. General clinical coding will therefore usually use sensorineural or congenital hearing-loss categories rather than a DFNB123-specific code. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-STX4)

The evidence is **aggregated disease-level literature derived from a deeply phenotyped family**, not EHR-derived population data. The foundational study examined eight affected and five unaffected relatives. (schrauwen2023syntaxin4is pages 6-7, schrauwen2023syntaxin4is pages 3-6)

## 2. Etiology

The primary cause is germline, biallelic STX4 dysfunction. In the defining pedigree, homozygosity for c.232+6T>C disrupts normal splicing; environmental causes including infection, ototoxic medication, and trauma were specifically excluded. No susceptibility loci, modifier genes, protective alleles, epigenetic determinants, or reproducible gene–environment interactions are known. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 6-7)

Consanguinity is a reproductive/genetic-context risk factor because it increases the probability that both parents carry the same rare allele. For two heterozygous parents, standard autosomal-recessive counseling implies a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability per pregnancy; these are Mendelian expectations, not empirically measured DFNB123 penetrance estimates.

Noise avoidance and avoidance of ototoxic agents remain prudent for preserving residual hearing, but neither prevents the initiating genetic lesion, and no STX4-specific protective environmental factor has been demonstrated.

## 3. Phenotypes

The core phenotype is **bilateral severe-to-profound or profound hearing impairment**, documented by pure-tone audiometry over 250–8000 Hz in affected relatives aged 10–25 years. Suggested HPO terms are **Sensorineural hearing impairment (HP:0000407)**, **Bilateral sensorineural hearing impairment (HP:0008619)**, **Severe hearing impairment (HP:0012714)**, and **Profound hearing impairment (HP:0012715)**. The publication describes congenital hearing impairment at the study level, but the retrieved individual data do not establish exact onset in every relative; “congenital” should therefore be curated with caution. (schrauwen2023syntaxin4is pages 1-2, schrauwen2023syntaxin4is pages 6-7)

No vestibular dysfunction was detected by history, tandem gait, or Romberg testing; facial and neurological examinations were normal. Increased head circumference was noted, but only one person reached borderline macrocephaly (+2 SD), making **Macrocephaly (HP:0000256)** an uncertain rather than defining association. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 6-7)

Severity was consistently high in the family, but stable versus progressive course, audiometric configuration, speech discrimination, age of first words, tinnitus, and longitudinal frequency-specific threshold change were not reported. Formal EQ-5D, SF-36, PROMIS, or hearing-specific quality-of-life scores are unavailable. Severe early bilateral hearing loss would be expected to affect speech/language acquisition, education, and communication, but these generic consequences were not quantified in DFNB123.

## 4. Genetic and molecular information

**Causal gene:** **STX4** (syntaxin 4; Ensembl ENSG00000103496). It encodes a plasma-membrane t-SNARE with an N-terminal peptide, Habc regulatory/stabilization region, coiled-coil SNARE-homology domain, and transmembrane region. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-STX4, perl2022stx4isrequired pages 7-9)

**Defining DFNB123 allele:** NM_004604.5:c.232+6T>C, alternatively NM_001272096.1:c.226+6T>C. It is a germline splice-region SNV, submitted to ClinVar as **SCV002499562**. It had CADD 23, gnomAD-v2 MAF **7.98×10⁻⁶**, was seen heterozygously in two non-Finnish Europeans, and was absent from gnomAD-v3, TOPMed Bravo, GME, and the examined All of Us release. Homozygosity mapping, segregation, and linkage gave LOD 5.9 at θ=0. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 1-2, schrauwen2023syntaxin4is pages 7-8)

A minigene assay demonstrated exon-3 skipping and a resulting frameshift. Nonsense-mediated decay and complete protein loss are biologically plausible but were predicted rather than measured in patient cochlear tissue. The evidence supports a loss-of-function mechanism; no gain-of-function or dominant-negative mechanism is demonstrated. (schrauwen2023syntaxin4is pages 2-3)

**Other biallelic STX4 alleles—not defining nonsyndromic DFNB123:** homozygous c.718C>T, p.Arg240Trp produced congenital sensorineural hearing loss plus developmental delay, hypotonia, myopathy, and severe dilated cardiomyopathy; compound-heterozygous c.89_90delGC, p.Gly30Aspfs*28 and c.232+4A>C occurred in a fetus with lethal multisystem disease. The p.Arg240Trp-equivalent zebrafish allele behaved as hypomorphic. These cases show allelic pleiotropy and argue against assuming that every biallelic STX4 genotype is nonsyndromic. (perl2022stx4isrequired pages 6-7, perl2022stx4isrequired pages 11-13)

No validated modifier gene, disease-specific methylation signature, chromosomal rearrangement, somatic event, or repeat expansion has been reported.

## 5. Environmental information

DFNB123 is genetic, not infectious, toxic, nutritional, occupational, radiation-induced, or lifestyle-mediated. Infection, ototoxic drugs, and trauma were excluded in the defining family. No smoking, diet, alcohol, exercise, pollution, infectious-agent, or chemical interaction with STX4 has been demonstrated. (schrauwen2023syntaxin4is pages 6-7)

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Homozygous STX4 c.232+6T>C leads to exon-3 skipping** in a minigene assay. (schrauwen2023syntaxin4is pages 2-3)
2. **Exon skipping results in a frameshift predicted to trigger nonsense-mediated decay**, leading to reduced functional syntaxin-4; protein depletion in patient cochlea remains inferred. (schrauwen2023syntaxin4is pages 2-3)
3. **Loss of syntaxin-4 is inferred to impair target-SNARE-mediated membrane fusion and vesicle recycling** in cochlear hair cells, where STX4A localizes to stereocilia, plasma membrane, and cytoplasm. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 1-2)
4. **Impaired apical trafficking is inferred to disrupt stereocilia maintenance and/or organization of the mechanotransduction apparatus.** This branch is supported by absent FM1-43 uptake after zebrafish stx4 knockdown but has not been resolved molecularly in human cells. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 3-6)
5. **Possible basal branch:** defective vesicle trafficking is inferred to impair synaptic exocytosis/recycling and afferent signaling; this has not been directly demonstrated for STX4 at mammalian inner-hair-cell ribbon synapses. (schrauwen2023syntaxin4is pages 3-6, schrauwen2023syntaxin4is pages 1-2)
6. **Hair-cell mechanotransduction/auditory signaling failure leads to abnormal zebrafish ABER/startle responses and, in homozygous humans, bilateral severe-to-profound hearing impairment.** (schrauwen2023syntaxin4is pages 1-2, schrauwen2023syntaxin4is pages 3-6)

STX4 participates broadly in vesicle docking/fusion and recycling rather than a canonical Wnt, MAPK, mTOR, or PI3K-AKT disease cascade. Relevant suggested GO annotations include **SNARE complex assembly (GO:0035493)**, **vesicle fusion (GO:0006906)**, **exocytosis (GO:0006887)**, **endocytic recycling (GO:0032456)**, **sensory perception of sound (GO:0007605)**, and **mechanosensory behavior (GO:0007638)**. Suggested cellular components include **plasma membrane (GO:0005886)**, **SNARE complex (GO:0031201)**, and **stereocilium (GO:0032420)**.

Mouse data place STX4A in inner and outer hair cells and also report expression in spiral and vestibular ganglia. Suggested Cell Ontology terms are **inner hair cell (CL:0000589)**, **outer hair cell (CL:0000601)**, and spiral-ganglion neuron where an appropriate current CL term is available. (schrauwen2023syntaxin4is pages 2-3)

No DFNB123-specific metabolomic, lipidomic, proteomic, epigenomic, patient transcriptomic, spatial-transcriptomic, multi-omic, organoid, iPSC, or CRISPR-screen signature has been reported. Available advanced data are mainly reanalysis of mouse developmental, microarray, and single-cell expression resources plus cochlear immunofluorescence. (schrauwen2023syntaxin4is pages 7-8, schrauwen2023syntaxin4is pages 2-3)

Complementary cardiac work demonstrates that CRISPR stx4 loss reduces Vamp2-positive vesicle docking at the cardiomyocyte sarcolemma and alters L-type Ca²⁺-channel-dependent calcium handling. This validates a general STX4 trafficking role but should not be substituted for a directly demonstrated cochlear mechanism. (perl2022stx4isrequired pages 7-9, perl2022stx4isrequired pages 13-14)

## 7. Anatomical structures affected

The principal organ is the **inner ear**, particularly the **cochlea** and its sensory epithelium/organ of Corti. Suggested UBERON terms are **inner ear (UBERON:0001846)**, **cochlea (UBERON:0001844)**, and **organ of Corti (UBERON:0002227)**. At cellular level, inner and outer hair cells are implicated; at subcellular level, stereocilia, plasma membrane, and cytoplasm are involved. Expression in spiral and vestibular ganglia provides anatomical plausibility, although no clinical vestibular deficit was observed. Disease is bilateral. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 1-2)

Cardiac, skeletal-muscle, neurologic, renal, and gastrointestinal involvement belongs to the broader biallelic STX4 spectrum, not the established c.232+6T>C DFNB123 phenotype. (perl2022stx4isrequired pages 6-7, perl2022stx4isrequired pages 11-13)

## 8. Temporal development

The disorder is characterized as congenital/early hearing impairment, and STX4 is expressed in both developing and adult mouse inner ear. Nevertheless, individual onset ages were not documented sufficiently to establish universal congenital onset. Audiometry at ages 10–25 years confirmed persistent severe disease. Progression rate, stages, fluctuation, remission, and untreated longitudinal course are unknown. (schrauwen2023syntaxin4is pages 1-2)

The clinically important intervention window is infancy and early childhood, when auditory access supports speech and language development; this is a general congenital-hearing-loss principle rather than a measured STX4-specific critical period. The defining article explicitly emphasizes prompt recognition and intervention. (schrauwen2023syntaxin4is pages 1-2)

## 9. Inheritance and population

Inheritance is autosomal recessive. All eight affected relatives in the reported consanguineous family were homozygous, while carrier parents were unaffected, consistent with high penetrance within that pedigree. Linkage modeling assumed complete penetrance; this assumption is not equivalent to a population estimate. Anticipation and germline mosaicism have not been reported. (schrauwen2023syntaxin4is pages 6-7, schrauwen2023syntaxin4is pages 1-2)

Only one DFNB123 family was found among **473 hearing-loss families** in the investigators’ dataset, and no independent second family was identified. This is a discovery-cohort proportion, not prevalence. No incidence per 100,000, carrier frequency, sex ratio, or geographic prevalence is available. The only established concentration is the reported consanguineous family from Khyber Pakhtunkhwa, Pakistan; the allele’s two gnomAD carriers were non-Finnish European. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 1-2, schrauwen2023syntaxin4is pages 3-6)

## 10. Diagnostics

The clinical evaluation should establish bilateral sensorineural hearing loss using newborn hearing screening, diagnostic ABR/ABER where age-appropriate, otoacoustic emissions, tympanometry, and pure-tone/speech audiometry. The defining study used 250–8000-Hz pure-tone audiometry, vestibular history, tandem gait, Romberg testing, physical/neurological examination, and selected ECGs. (schrauwen2023syntaxin4is pages 6-7)

**Preferred molecular approach:** a comprehensive hearing-loss panel that includes **STX4**, with deletion/duplication analysis; exome or genome sequencing is appropriate after negative panel testing or where a multisystem phenotype is present. The authors explicitly recommended adding STX4 to diagnostic panels. Candidate variants require parental segregation and phenotype review. RNA analysis or a minigene assay can clarify noncanonical splice variants. (schrauwen2023syntaxin4is pages 3-6, schrauwen2023syntaxin4is pages 6-7)

The discovery workflow excluded coding GJB2/common hearing-loss variants, used WES, homozygosity mapping, CNV analysis, Sanger segregation, linkage, population-frequency filtering, and functional splice testing. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not targeted assays for this sequence-level disorder but may be selected when the broader phenotype suggests another diagnosis. (schrauwen2023syntaxin4is pages 6-7)

Differential diagnosis includes the many other autosomal-recessive nonsyndromic hearing-loss genes—especially GJB2 and genes causing severe congenital disease—and acquired infection, ototoxicity, or trauma. Cardiac examination and consideration of ECG/echocardiography are reasonable when a patient has p.Arg240Trp, truncating alleles, weakness, hypotonia, developmental delay, arrhythmia, or cardiomyopathy because broader STX4 disease can be pleiotropic. This surveillance proposal is precautionary and not a formal guideline. (perl2022stx4isrequired pages 6-7, perl2022stx4isrequired pages 11-13)

Cascade testing can identify carriers and affected relatives. Prenatal diagnosis and PGT-M are technically feasible once familial pathogenic variants are known, subject to local regulation and nondirective counseling.

## 11. Outcome and prognosis

No DFNB123-specific mortality, survival, or life-expectancy decrement is documented. The nonsyndromic family had no reported life-threatening manifestation. Hearing impairment appears chronic and severe, with no spontaneous remission reported, but longitudinal stability versus progression is unknown. Formal disability and quality-of-life outcomes are unavailable. (schrauwen2023syntaxin4is pages 3-6, schrauwen2023syntaxin4is pages 1-2)

Broader STX4 disease can be severe: the p.Arg240Trp patient required heart transplantation, and the compound-heterozygous fetus died at five days from multiorgan failure. These outcomes must not be assigned to DFNB123 c.232+6T>C without evidence. (perl2022stx4isrequired pages 6-7)

## 12. Treatment

No STX4-directed drug, gene replacement, gene editing, ASO, siRNA, mRNA, cell therapy, or disease-specific pharmacogenomic strategy is available. No relevant STX4/DFNB123 interventional trial was identified in the tool search. (schrauwen2023syntaxin4is pages 3-6, schrauwen2023syntaxin4is pages 2-3)

Current care should follow severity- and age-appropriate hearing-loss practice: hearing aids when useful, cochlear-implant evaluation for severe-to-profound loss with inadequate aided speech access, speech/language or auditory-verbal therapy, educational accommodations, and Deaf/community communication options according to patient and family preference. Suggested NCIt terms include **Hearing Aid Device (NCIt concept where current)**, **Cochlear Implantation**, **Speech Therapy**, and **Audiologic Rehabilitation**; exact current NCIt identifiers should be ontology-validated before database loading.

The separate p.Arg240Trp patient’s hearing aids were replaced by a cochlear implant at age six, with improved communication. This is a single pleiotropic case and neither a response rate nor proof of STX4-specific implant efficacy. (perl2022stx4isrequired pages 6-7)

The LTCC agonist Bay K-8644 rescued zebrafish cardiac bradycardia, not hearing. It is mechanistic model evidence and not a proposed human DFNB123 treatment. (perl2022stx4isrequired pages 11-13, perl2022stx4isrequired pages 13-14)

## 13. Prevention

There is no primary lifestyle or vaccine prevention for a germline recessive disorder. Primary genetic prevention options are informed reproductive choice after carrier testing, including natural conception with prenatal diagnosis, PGT-M, donor gametes, or adoption; counseling must remain nondirective.

Secondary prevention consists of universal newborn hearing screening, rapid diagnostic audiology, early molecular testing, cascade testing, and prompt auditory/communication intervention. Tertiary prevention includes amplification or implantation where indicated, communication rehabilitation, educational support, and avoidance of additional noise or ototoxic injury. No medication prophylaxis or immunization is disease-specific. The family data support recessive carrier and relative testing but do not constitute a formal prevention trial. (schrauwen2023syntaxin4is pages 1-2, schrauwen2023syntaxin4is pages 2-3)

## 14. Other species and natural disease

Experimental evidence exists in **Danio rerio** (zebrafish; NCBI Taxon **7955**) and expression/localization evidence in **Mus musculus** (mouse; Taxon **10090**). No naturally occurring veterinary STX4 deafness syndrome, breed association, OMIA entry, zoonotic transmission, or cross-species infectious risk was identified. Human and zebrafish findings support evolutionary conservation of STX4-dependent auditory function. (schrauwen2023syntaxin4is pages 1-2, schrauwen2023syntaxin4is pages 2-3)

## 15. Model organisms

**Zebrafish auditory model:** ATG- and splice-blocking morpholinos at approximately 9 ng were evaluated at five days post-fertilization. Knockdown caused reduced 1-kHz auditory/startle responses, with reported P values of **0.0001** and **0.0017**, absent/impaired FM1-43 uptake in neuromast hair cells, edema, increased head size, and broad developmental abnormalities. It recapitulates impaired mechanotransduction and auditory behavior but not a clean isolated human DFNB123 phenotype. Limitations include morpholino toxicity/off-target effects, developmental pleiotropy, absence of a stable knock-in/rescue auditory model, and species-specific splicing—the zebrafish splice morpholino caused intron retention, whereas human c.232+6T>C caused exon skipping. (schrauwen2023syntaxin4is pages 3-6, schrauwen2023syntaxin4is pages 7-8)

**Mouse:** developmental datasets and P12 immunofluorescence establish cochlear expression and hair-cell localization, but no hearing phenotype from a cochlea-specific Stx4 knockout was reported. Global Stx4 knockout is embryonic lethal, limiting adult auditory study. (schrauwen2023syntaxin4is pages 2-3, perl2022stx4isrequired pages 6-7)

**CRISPR zebrafish cardiac model:** a 38-bp exon-3 splice-donor deletion generated out-of-frame transcripts and broad developmental/cardiac disease. It is useful for SNARE-dependent vesicle docking, Ca²⁺ handling, and allelic hypomorphism, but is not a specific DFNB123 model. (perl2022stx4isrequired pages 7-9, perl2022stx4isrequired pages 11-13)

No reported rat, Drosophila, C. elegans, yeast, patient-iPSC, cochlear-organoid, or humanized knock-in DFNB123 model was identified.

## Evidence appraisal and 2023–2024 status

The 2023 Schrauwen study remains the pivotal and most recent retrieved DFNB123-specific primary report. Its strengths are eight affected relatives, strong segregation/linkage, extreme allele rarity, functional splice validation, cross-species localization, and auditory assays. Its central limitations are a single pedigree, one DFNB123 allele, morpholino rather than stable auditory modeling, no patient-derived cochlear tissue, and sparse longitudinal and treatment data. The authors’ own expert conclusion was that STX4 should be added to diagnostic hearing-loss panels and that additional families are required to define the phenotype. (schrauwen2023syntaxin4is pages 2-3, schrauwen2023syntaxin4is pages 3-6)

A suitable exact abstract quotation is: **“This identified a homozygous splice region variant in STX4 (c.232 + 6 T > C), which causes exon skipping and a frameshift, that segregated with hearing impairment (two-point LOD score = 5.9).”** A second is: **“Our findings indicate that STX4 dysfunction leads to hearing impairment in humans and zebrafish and supports the evolutionary conserved role of STX4 in inner ear development and hair cell functioning.”** (schrauwen2023syntaxin4is pages 1-2)

No retrieved 2024 primary study independently replicated DFNB123, supplied epidemiologic estimates, or advanced an STX4-specific therapy. Accordingly, this knowledge-base entry should be labeled **limited human evidence/one replicated-within-family locus report**, with the nonsyndromic DFNB123 phenotype kept distinct from severe multisystem biallelic STX4 disease.

References

1. (schrauwen2023syntaxin4is pages 2-3): Isabelle Schrauwen, Amama Ghaffar, Thashi Bharadwaj, Khadim Shah, Sakina Rehman, Anushree Acharya, Khurram Liaqat, Nicole S Lin, Jenna L Everard, Anwar Khan, Zubair M Ahmed, Wasim Ahmad, Saima Riazuddin, and Suzanne M Leal. Syntaxin 4 is essential for hearing in human and zebrafish. Human molecular genetics, 32:1184-1192, Nov 2023. URL: https://doi.org/10.1093/hmg/ddac257, doi:10.1093/hmg/ddac257. This article has 3 citations and is from a domain leading peer-reviewed journal.

2. (schrauwen2023syntaxin4is pages 1-2): Isabelle Schrauwen, Amama Ghaffar, Thashi Bharadwaj, Khadim Shah, Sakina Rehman, Anushree Acharya, Khurram Liaqat, Nicole S Lin, Jenna L Everard, Anwar Khan, Zubair M Ahmed, Wasim Ahmad, Saima Riazuddin, and Suzanne M Leal. Syntaxin 4 is essential for hearing in human and zebrafish. Human molecular genetics, 32:1184-1192, Nov 2023. URL: https://doi.org/10.1093/hmg/ddac257, doi:10.1093/hmg/ddac257. This article has 3 citations and is from a domain leading peer-reviewed journal.

3. (schrauwen2023syntaxin4is pages 3-6): Isabelle Schrauwen, Amama Ghaffar, Thashi Bharadwaj, Khadim Shah, Sakina Rehman, Anushree Acharya, Khurram Liaqat, Nicole S Lin, Jenna L Everard, Anwar Khan, Zubair M Ahmed, Wasim Ahmad, Saima Riazuddin, and Suzanne M Leal. Syntaxin 4 is essential for hearing in human and zebrafish. Human molecular genetics, 32:1184-1192, Nov 2023. URL: https://doi.org/10.1093/hmg/ddac257, doi:10.1093/hmg/ddac257. This article has 3 citations and is from a domain leading peer-reviewed journal.

4. (perl2022stx4isrequired pages 11-13): Eliyahu Perl, Padmapriyadarshini Ravisankar, Manu E. Beerens, Lejla Mulahasanovic, Kelly Smallwood, Marion Bermúdez Sasso, Carina Wenzel, Thomas D. Ryan, Matej Komár, Kevin E. Bove, Calum A. MacRae, K. Nicole Weaver, Carlos E. Prada, and Joshua S. Waxman. Stx4 is required to regulate cardiomyocyte ca2+ handling during vertebrate cardiac development. Jul 2022. URL: https://doi.org/10.1016/j.xhgg.2022.100115, doi:10.1016/j.xhgg.2022.100115. This article has 9 citations and is from a peer-reviewed journal.

5. (schrauwen2023syntaxin4is pages 7-8): Isabelle Schrauwen, Amama Ghaffar, Thashi Bharadwaj, Khadim Shah, Sakina Rehman, Anushree Acharya, Khurram Liaqat, Nicole S Lin, Jenna L Everard, Anwar Khan, Zubair M Ahmed, Wasim Ahmad, Saima Riazuddin, and Suzanne M Leal. Syntaxin 4 is essential for hearing in human and zebrafish. Human molecular genetics, 32:1184-1192, Nov 2023. URL: https://doi.org/10.1093/hmg/ddac257, doi:10.1093/hmg/ddac257. This article has 3 citations and is from a domain leading peer-reviewed journal.

6. (perl2022stx4isrequired pages 6-7): Eliyahu Perl, Padmapriyadarshini Ravisankar, Manu E. Beerens, Lejla Mulahasanovic, Kelly Smallwood, Marion Bermúdez Sasso, Carina Wenzel, Thomas D. Ryan, Matej Komár, Kevin E. Bove, Calum A. MacRae, K. Nicole Weaver, Carlos E. Prada, and Joshua S. Waxman. Stx4 is required to regulate cardiomyocyte ca2+ handling during vertebrate cardiac development. Jul 2022. URL: https://doi.org/10.1016/j.xhgg.2022.100115, doi:10.1016/j.xhgg.2022.100115. This article has 9 citations and is from a peer-reviewed journal.

7. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-STX4): Open Targets Query (autosomal recessive nonsyndromic hearing loss-STX4, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (schrauwen2023syntaxin4is pages 6-7): Isabelle Schrauwen, Amama Ghaffar, Thashi Bharadwaj, Khadim Shah, Sakina Rehman, Anushree Acharya, Khurram Liaqat, Nicole S Lin, Jenna L Everard, Anwar Khan, Zubair M Ahmed, Wasim Ahmad, Saima Riazuddin, and Suzanne M Leal. Syntaxin 4 is essential for hearing in human and zebrafish. Human molecular genetics, 32:1184-1192, Nov 2023. URL: https://doi.org/10.1093/hmg/ddac257, doi:10.1093/hmg/ddac257. This article has 3 citations and is from a domain leading peer-reviewed journal.

9. (perl2022stx4isrequired pages 7-9): Eliyahu Perl, Padmapriyadarshini Ravisankar, Manu E. Beerens, Lejla Mulahasanovic, Kelly Smallwood, Marion Bermúdez Sasso, Carina Wenzel, Thomas D. Ryan, Matej Komár, Kevin E. Bove, Calum A. MacRae, K. Nicole Weaver, Carlos E. Prada, and Joshua S. Waxman. Stx4 is required to regulate cardiomyocyte ca2+ handling during vertebrate cardiac development. Jul 2022. URL: https://doi.org/10.1016/j.xhgg.2022.100115, doi:10.1016/j.xhgg.2022.100115. This article has 9 citations and is from a peer-reviewed journal.

10. (perl2022stx4isrequired pages 13-14): Eliyahu Perl, Padmapriyadarshini Ravisankar, Manu E. Beerens, Lejla Mulahasanovic, Kelly Smallwood, Marion Bermúdez Sasso, Carina Wenzel, Thomas D. Ryan, Matej Komár, Kevin E. Bove, Calum A. MacRae, K. Nicole Weaver, Carlos E. Prada, and Joshua S. Waxman. Stx4 is required to regulate cardiomyocyte ca2+ handling during vertebrate cardiac development. Jul 2022. URL: https://doi.org/10.1016/j.xhgg.2022.100115, doi:10.1016/j.xhgg.2022.100115. This article has 9 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_123-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.
