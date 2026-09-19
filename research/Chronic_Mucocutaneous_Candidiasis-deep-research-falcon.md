---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T07:33:26.731074'
end_time: '2026-08-01T07:41:39.486377'
duration_seconds: 492.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Mucocutaneous Candidiasis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Chronic_Mucocutaneous_Candidiasis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Mucocutaneous Candidiasis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chronic Mucocutaneous Candidiasis** covering all of the
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
- **Disease Name:** Chronic Mucocutaneous Candidiasis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chronic Mucocutaneous Candidiasis** covering all of the
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


# Chronic Mucocutaneous Candidiasis: Disease-Characteristics Report

## Executive summary and scope

Chronic mucocutaneous candidiasis (CMC) is a **clinical phenotype**, not one molecularly uniform disease. It comprises persistent or recurrent, usually non-invasive *Candida* infection of oral, esophageal, genital, cutaneous, and nail surfaces. *Candida albicans* predominates. CMC may be relatively isolated—particularly with direct IL-17 pathway defects—or part of broader inborn errors of immunity such as STAT1 gain-of-function (GOF), CARD9 deficiency, or AIRE-associated autoimmune polyendocrine syndrome type 1 (APS-1/APECED). Thus, “Mendelian CMC” should be represented as a disease family with genotype-specific child entities rather than as a single-gene disorder. A recent review summarizes it as recurrent or persistent infection of “nails, skin, mouth, and genital organs,” and emphasizes defects in fungal recognition, IL-17 production/signaling, and Th17 development (published March 2024; DOI: https://doi.org/10.1097/INF.0000000000004321). (cinicola2024mucocutaneouscandidiasisinsights pages 1-2)

The strongest general causal model is: **impaired epithelial IL-17 immunity → inadequate chemokine, antimicrobial-peptide, and neutrophil recruitment responses → failure to contain commensal *Candida* at barrier surfaces → recurrent/chronic candidiasis**. STAT1 GOF is the most common currently recognized genetic cause and may account for up to approximately half of genetically investigated CMC, although ascertainment strongly affects that estimate. (egri2021primaryimmunodeficiencyand pages 1-2, egri2021primaryimmunodeficiencyand pages 7-8)

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Chronic mucocutaneous candidiasis; British spelling: chronic mucocutaneous candidosis.
* **MONDO:** **MONDO:0015279**.
* **Orphanet:** **ORPHA:1334**, Chronic mucocutaneous candidosis.
* **MeSH concept:** candidiasis/chronic mucocutaneous candidiasis is generally indexed under candidiasis and immunodeficiency-associated candidiasis; exact descriptor assignment should be verified against the current MeSH release.
* **OMIM:** there is no single OMIM entry adequately representing the whole phenotype. Molecular subtypes are distributed among familial candidiasis and gene-specific immunodeficiency entries; examples include direct IL-17-pathway deficiencies and STAT1-GOF-associated autosomal-dominant CMC.
* **ICD:** ICD-10-CM commonly places disease under candidiasis codes, selected by site—e.g., B37.0 oral, B37.2 skin/nail, B37.81 esophageal, B37.3 genital—and D84.89 or another immune-defect code when appropriate. ICD-11 similarly codes candidosis by site and the underlying inborn error separately. A unique universally used CMC code is not established.
* **Synonyms:** CMC; chronic mucocutaneous candidosis; chronic mucocutaneous *Candida* infection; familial chronic mucocutaneous candidiasis; candidiasis, familial; autosomal-dominant CMC when specifically STAT1/IL17F-related.

Open Targets independently maps MONDO:0015279 to IL17RA, STAT1, IL17RC, CLEC7A, TRAF3IP2, IL17F, and IL23R, while ORPHA:1334 additionally maps CARD9. This is aggregated disease-level evidence, not an individual-patient EHR dataset. (OpenTargets Search: chronic mucocutaneous candidiasis)

### Data provenance

Most knowledge derives from aggregated rare-disease resources, pedigrees, case series, retrospective international cohorts, functional immune assays, and experimental models. Quantitative clinical frequencies below are primarily from **genotype-selected STAT1-GOF cohorts** and must not be generalized to every CMC genotype.

## 2. Etiology, risk, protective factors, and gene–environment interaction

CMC arises when normally commensal *Candida* encounters a heritable defect in epithelial antifungal immunity. Direct causes include abnormal fungal sensing (CLEC7A/Dectin-1–CARD9), reduced Th17 differentiation or cytokine production (STAT1 GOF, RORC), neutralization of IL-17-family cytokines in AIRE deficiency, or defective IL-17 ligand/receptor/adaptor function (IL17F, IL17RA, IL17RC, TRAF3IP2/ACT1). CARD9 deficiency differs because deep-organ and CNS candidiasis may occur. (egri2021primaryimmunodeficiencyand pages 5-6, cinicola2024mucocutaneouscandidiasisinsights pages 1-2, OpenTargets Search: chronic mucocutaneous candidiasis)

| Gene/pathway | Inheritance and functional class | Characteristic phenotype beyond mucocutaneous *Candida* | Key evidence/PMIDs |
|---|---|---|---|
| **STAT1 (GOF)** | **AD**; gain-of-function JAK-STAT signaling with impaired Th17/IL-17 immunity | Broad immune dysregulation: bacterial and viral infections, autoimmunity, vascular complications/aneurysm risk; CMC is the most common manifestation and may account for a large fraction of Mendelian CMC cases (egri2021primaryimmunodeficiencyand pages 1-2, egri2021primaryimmunodeficiencyand pages 7-8, parackova2023neutrophilsinstat1 pages 1-3, meesilpavikkai2024unravelingtheimmunogenetics pages 4-7) | PMID **21727188** (Open Targets literature link), large CMC cohort with **35/57** mutated and **61%** of screened CMC patients carrying heterozygous STAT1 variants (OpenTargets Search: chronic mucocutaneous candidiasis, depner2016theextendedclinical pages 1-2) |
| **IL17F** | Likely **AD** cytokine defect; impaired IL-17 effector signaling at mucosa (direct Mendelian association supported in disease-target evidence) | Primarily isolated CMC phenotype in the IL-17 axis; broader extra-Candida phenotype not defined in gathered context (egri2021primaryimmunodeficiencyand pages 5-6, OpenTargets Search: chronic mucocutaneous candidiasis) | PMID **21350122** (Open Targets literature link) (OpenTargets Search: chronic mucocutaneous candidiasis) |
| **IL17RA** | **AR** receptor deficiency; loss of IL-17 receptor signaling | Predisposition centered on chronic/recurrent mucocutaneous candidiasis due to failed IL-17 responses; broader phenotype not detailed in gathered context (egri2021primaryimmunodeficiencyand pages 5-6, OpenTargets Search: chronic mucocutaneous candidiasis) | PMID **21350122**, PMID **22951726** (Open Targets literature links) (OpenTargets Search: chronic mucocutaneous candidiasis) |
| **IL17RC** | Receptor deficiency; likely **AR** loss of IL-17A/F signaling | CMC with defective IL-17-mediated mucosal antifungal immunity; limited extra-Candida detail in gathered context (egri2021primaryimmunodeficiencyand pages 8-9, OpenTargets Search: chronic mucocutaneous candidiasis) | PMID **25918342** (Open Targets literature link) (OpenTargets Search: chronic mucocutaneous candidiasis) |
| **TRAF3IP2 / ACT1** | Adaptor/signaling defect downstream of IL-17 receptor; loss of function, likely **AR** | CMC from impaired IL-17 signal transduction; broader syndromic features not specified in gathered context (egri2021primaryimmunodeficiencyand pages 5-6, egri2021primaryimmunodeficiencyand pages 8-9, OpenTargets Search: chronic mucocutaneous candidiasis) | PMID **24120361** (Open Targets literature link) (OpenTargets Search: chronic mucocutaneous candidiasis) |
| **RORC** | Bi-allelic transcription-factor deficiency affecting Th17 development/function | Not isolated to Candida: impaired immunity to *Candida* plus susceptibility to mycobacterial infection is noted in gathered context (indirect mechanistic support) (cinicola2024mucocutaneouscandidiasisinsights pages 9-9, cinicola2024mucocutaneouscandidiasisinsights pages 1-2) | No direct PMID extracted in current context; association supported indirectly by cited 2024 review reference list and mechanistic review snippet (cinicola2024mucocutaneouscandidiasisinsights pages 9-9, cinicola2024mucocutaneouscandidiasisinsights pages 1-2) |
| **CARD9** | **AR** innate antifungal signaling defect downstream of C-type lectin pathways | Distinguishing feature is **invasive candidiasis including CNS disease**, not just mucocutaneous infection (egri2021primaryimmunodeficiencyand pages 5-6, cinicola2024mucocutaneouscandidiasisinsights pages 9-9, cinicola2024mucocutaneouscandidiasisinsights pages 1-2) | PMIDs linked by Open Targets include **19864672**, **23335372**, **24131138**, **25057046**, **26679537** (OpenTargets Search: chronic mucocutaneous candidiasis) |
| **CLEC7A (Dectin-1)** | Pattern-recognition receptor defect in fungal sensing; association appears weaker/more indirect than STAT1/IL-17 pathway genes | Mucocutaneous Candida susceptibility via impaired fungal recognition; invasive phenotype less clearly established in gathered context (cinicola2024mucocutaneouscandidiasisinsights pages 1-2, OpenTargets Search: chronic mucocutaneous candidiasis) | PMIDs linked by Open Targets include **19864674** and related supporting literature; indirect/uncertain strength for isolated Mendelian CMC should be noted (OpenTargets Search: chronic mucocutaneous candidiasis) |
| **AIRE** | **AR** autoimmune polyendocrine syndrome type 1 (APS-1/APECED); autoimmune cytokine-neutralizing pathobiology affecting IL-17/IL-22 axis | Classic triad includes **hypoparathyroidism** and **adrenal insufficiency/Addison disease**; CMC is among the earliest and most frequent manifestations (egri2021primaryimmunodeficiencyand pages 5-6, cinicola2024mucocutaneouscandidiasisinsights pages 9-9) | AIRE is strongly linked to APS-1 rather than isolated CMC; Open Targets supports AIRE–APS1 association (e.g., PMID **11275943**) (OpenTargets Search: chronic mucocutaneous candidiasis) |
| **STAT3, DOCK8** *(differential; broader Th17 defects rather than classic isolated CMC)* | Syndromic inborn errors with **Th17 deficiency**; not presented in gathered context as primary isolated CMC genes | Should prompt differential diagnosis because they cause wider immunodeficiency syndromes with CMC as one feature rather than isolated familial CMC (cinicola2024mucocutaneouscandidiasisinsights pages 9-9) | Review-level support in gathered context; no direct disease-specific PMID extracted here for isolated CMC assignment (cinicola2024mucocutaneouscandidiasisinsights pages 9-9) |


*Table: This table summarizes the main genes and syndromic pathways linked to chronic mucocutaneous candidiasis in the gathered evidence. It distinguishes core IL-17/STAT1 causes from broader differentials such as APS-1, CARD9 deficiency, and syndromic Th17 disorders.*

### Genetic risk factors

* **STAT1 GOF:** heterozygous germline variants, usually autosomal dominant, with both familial and de novo disease. A 57-patient screen found variants in **35/57 (61%)**, including 26/39 familial (67%) and 9/18 sporadic cases (50%). Thirteen variants included p.M202V, p.A267V, p.R274W/Q, p.T385M/K, p.K388E, p.N397D, p.F404Y, p.F172L, p.Y287D, p.P293S, and p.S466R. (depner2016theextendedclinical pages 1-2)
* **Direct IL-17 defects:** IL17F is classically dominant-negative/autosomal dominant; IL17RA, IL17RC, and TRAF3IP2 deficiencies are generally biallelic/autosomal recessive loss-of-function disorders. Landmark human evidence is linked to PMID **21350122** for IL17F/IL17RA, PMID **25918342** for IL17RC, and PMID **24120361** for ACT1. (OpenTargets Search: chronic mucocutaneous candidiasis)
* **CARD9, RORC, AIRE:** generally biallelic recessive disease. AIRE causes APS-1 rather than isolated CMC; hypoparathyroidism and primary adrenal insufficiency are major diagnostic clues. (egri2021primaryimmunodeficiencyand pages 5-6, OpenTargets Search: chronic mucocutaneous candidiasis)
* **Broader syndromic risk:** STAT3 loss-of-function, DOCK8 deficiency and other combined immunodeficiencies can include CMC through reduced Th17 function but should not be labeled isolated familial CMC. (cinicola2024mucocutaneouscandidiasisinsights pages 9-9)

All established monogenic variants are **germline**. Somatic mosaicism, repeat expansions, mitochondrial variants, anticipation, and recurrent CMC-specific chromosomal rearrangements are not established major mechanisms. Pathogenic alleles are individually rare or absent from population databases; exact gnomAD frequency and ACMG classification must be retrieved per HGVS variant and transcript. A variant should not be classified from phenotype alone: segregation, population rarity, computational evidence, and—especially for STAT1—functional hyperphosphorylation/dephosphorylation assays are important.

### Environmental and acquired risk factors

Antibiotic exposure, corticosteroid or other immunosuppression, HIV, diabetes, malnutrition, denture use, barrier trauma, and local moisture can promote ordinary mucocutaneous candidiasis and must be excluded as secondary explanations. In Mendelian CMC, these exposures may amplify disease but are not the primary cause. Persistent colonization and repeated azole exposure select resistant *Candida*, creating an important gene–environment–treatment interaction. Azole resistance is described as the principal limitation of long-term management. (egri2021primaryimmunodeficiencyand pages 1-2)

No reproducible **genetic protective allele** or specific protective diet/lifestyle intervention has been established. Practical protective factors are avoidance of unnecessary antibiotics/immunosuppression, good oral/dental and skin-fold hygiene, glycemic control, keeping affected skin dry, and culture-guided antifungal stewardship. These reduce exposure or complications but do not correct the inherited immune defect.

## 3. Phenotypes

### Core phenotype and quantitative frequencies

A 26-person STAT1-GOF cohort found oral candidiasis in **73%**, esophageal candidiasis in **65%**, intertrigo in **50%**, pustular skin disease in **46%**, and scalp infection in **44%**. Untreated oral disease became chronic in 42%, while 50% of affected patients had chronic cutaneous disease. Aphthous stomatitis occurred in 69%; 82% of those cases were recurrent. (depner2016theextendedclinical pages 6-8)

Suggested phenotype annotations include:

| Manifestation | Type/course | Suggested HPO term |
|---|---|---|
| Recurrent oral thrush, pseudomembranes | Sign; childhood onset common; relapsing/chronic | Recurrent oral candidiasis **HP:0002728** |
| Esophageal candidiasis/dysphagia | Infection/symptom; recurrent | Esophageal candidiasis; Dysphagia **HP:0002015** |
| Cutaneous candidiasis, intertrigo, pustules | Sign; episodic or chronic | Cutaneous candidiasis **HP:0001597**; Intertrigo |
| Onychomycosis, onycholysis, nail dystrophy | Sign; often progressive without suppression | Onychomycosis; Onycholysis **HP:0001806**; Nail dystrophy **HP:0001597** should be verified because HPO releases change |
| Genital candidiasis | Sign/symptom; recurrent | Recurrent vulvovaginal candidiasis/genital candidiasis |
| Aphthous ulcers | Sign; recurrent | Recurrent oral ulceration **HP:0000155** |
| Reduced Th17 cells/IL-17 production | Laboratory abnormality | Abnormal T-helper 17 cell physiology; Abnormal cytokine secretion |
| Bacterial respiratory infections | Syndromic STAT1-GOF feature | Recurrent respiratory infections **HP:0002205** |
| Viral infections | Syndromic feature | Recurrent viral infections **HP:0004429** |
| Autoimmune thyroid disease/cytopenia/diabetes | STAT1-GOF or APS-1 feature | Autoimmune thyroiditis **HP:0002923**; Autoimmune cytopenia; Diabetes mellitus |
| Hypoparathyroidism/Addison disease | APS-1 clues | Hypoparathyroidism **HP:0000829**; Adrenal insufficiency **HP:0000846** |
| Cerebral/aortic aneurysm or vasculopathy | Severe STAT1-GOF complication | Cerebral aneurysm **HP:0004944**; Aortic aneurysm **HP:0004942** |
| Oral/esophageal squamous-cell carcinoma | Late complication | Squamous cell carcinoma **HP:0002860** |

IDs should be validated against the target HPO release before database ingestion. Nail disease may impair walking, footwear use, manual work, and appearance; oral/esophageal disease impairs eating and causes pain; genital and visible skin disease affect intimacy and psychosocial wellbeing. No robust CMC-specific EQ-5D, SF-36, or PROMIS reference values were identified.

### Extended STAT1-GOF phenotype

A 2024 synthesis reports more than 400 patients and over 100 STAT1-GOF variants. CMC occurs in over 60%; bacterial respiratory infection occurs in over 50% (lower respiratory disease approximately 37%), viral infections in roughly half, and autoimmunity in over 60%. More than 95% have onset before age 35, usually in early childhood. These frequencies describe STAT1 GOF, not direct IL-17 receptor deficiency. (meesilpavikkai2024unravelingtheimmunogenetics pages 4-7)

Complications include bronchiectasis from repeated respiratory infection, endocrinopathy, cytopenias, enteropathy, cerebral or large-vessel aneurysm/vasculopathy, and oral or esophageal squamous-cell carcinoma after longstanding inflammation. The literature review explicitly notes mouth/esophageal neoplasia and rare cerebral vasculitis. (egri2021primaryimmunodeficiencyand pages 1-2)

## 4. Genetic and molecular information

### Functional consequences

STAT1 GOF variants cluster in coiled-coil, DNA-binding, SH2, and other functional domains. Many coiled-coil/DNA-binding variants impair nuclear dephosphorylation, prolonging phosphorylated STAT1; some SH2 variants increase phosphorylation by other means. This exaggerates IFN-driven transcription and interferes with STAT3-dependent Th17 differentiation. In four Iranian patients, p.R274Q and p.Q271P were associated with increased IFN-γ-induced STAT1 phosphorylation, reduced Th17 cells, reduced IL17A/IL17F/IL22 expression, and impaired Candida-specific T-cell proliferation. (ostadi2021functionalanalysisof pages 1-2, ostadi2021functionalanalysisof pages 7-8, meesilpavikkai2024unravelingtheimmunogenetics pages 4-7)

In one literature synthesis, **82%** of STAT1-GOF patients had deficient CD4+IL-17+ cells. This is a useful supportive biomarker but not a perfectly sensitive diagnostic test. (ostadi2021functionalanalysisof pages 7-8)

### Modifier, epigenetic, and structural evidence

Penetrance and expressivity are variable even within pedigrees, implying modifier genes, pathogen exposure, microbiome, treatment history, and stochastic immune effects. No validated CMC-specific modifier gene is ready for routine annotation. No reproducible disease-defining DNA-methylation, histone, chromatin, lipidomic, or metabolomic signature has been established. There is likewise no characteristic karyotypic abnormality, aneuploidy, translocation, or inversion.

## 5. Environmental and infectious information

The proximate infectious agent is usually ***Candida albicans***—NCBI Taxonomy **5476**—although other *Candida* species may occur. CMC is not ordinarily acquired by zoonotic transmission; it reflects failure to control endogenous or environmentally acquired commensal yeast at barrier sites. Fungal morphology and cell-wall β-glucans/mannans engage Dectin-1 and Toll-like receptors. CARD9 transduces C-type lectin signals and promotes cytokines needed for Th17 differentiation. (egri2021primaryimmunodeficiencyand pages 1-2, cinicola2024mucocutaneouscandidiasisinsights pages 1-2)

Smoking, alcohol, exercise, occupational toxins, radiation, or pollution are not established primary causes of Mendelian CMC. Tobacco and alcohol plausibly worsen oral/esophageal injury and cancer risk, but genotype-specific quantitative interaction data are lacking.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Recognition:** epithelial/myeloid CLEC7A/Dectin-1 and TLRs recognize *Candida* wall ligands.
2. **Upstream signaling:** CARD9-dependent innate signaling induces inflammatory cytokines; IL-6/IL-1/IL-23 and STAT3/RORγt support Th17 differentiation.
3. **Effector production:** Th17, γδ T cells, innate lymphoid cells, and other lymphocytes produce IL-17A/F and IL-22.
4. **Barrier response:** IL-17A/F engage IL-17RA/IL-17RC on keratinocytes and mucosal epithelial cells; ACT1/TRAF3IP2 activates NF-κB/MAPK programs, chemokines, antimicrobial peptides, and granulopoietic/neutrophil-recruiting signals.
5. **Failure states:** ligand/receptor/adaptor loss, low Th17 generation, anti-cytokine autoantibodies, or excessive STAT1 signaling interrupts this axis.
6. **Clinical output:** persistent epithelial colonization becomes symptomatic oral, esophageal, genital, cutaneous, and nail candidiasis. Chronic inflammation and repeated infection contribute downstream to scarring, structural lung disease, and malignancy.

The centrality of IL-17 is supported by human Mendelian defects across IL17F, IL17RA, IL17RC and TRAF3IP2 and by the common reduced Th17 phenotype in STAT1 GOF. (egri2021primaryimmunodeficiencyand pages 5-6, OpenTargets Search: chronic mucocutaneous candidiasis)

Suggested biological-process terms include GO:0045087 innate immune response, GO:0006955 immune response, GO:0032496 response to lipopolysaccharide only if experimentally appropriate, GO:0071346 cellular response to interferon-γ, GO:0032743 positive regulation of IL-17 production, GO:0030593 neutrophil chemotaxis, GO:0009617 response to bacterium/fungus-specific child term, and GO:0050832 defense response to fungus. Suggested cell types include CL:0000542 lymphocyte, CL:0000899 T-helper 17 cell, CL:0000624 CD4-positive alpha-beta T cell, CL:0000775 neutrophil, CL:0000451 dendritic cell, CL:0000576 monocyte, CL:0000312 keratinocyte, and mucosal epithelial-cell terms appropriate to site.

### Recent molecular profiling

A 2023 three-adult study combined CyTOF and a 265-protein Olink panel during JAK inhibition. Clinical CMC improved, and one strong responder had greater Candida-specific reactivity after seven weeks. NK cells increased CD45/CD52/CD99; monocytes and eosinophils reduced CD16; CXCL10, annexin A1, granzymes B/H, and oncostatin M fell while FGF21 rose; IFN-γ and CXCL10 were reduced at three months. The abstract states: **“Overall, JAK inhibitors improved clinical symptoms of CMC, but caused side effects in two patients.”** (published 2023; DOI: https://doi.org/10.1007/s10875-022-01351-0). (borgstrom2023threeadultcases pages 1-2, borgstrom2023threeadultcases pages 7-11)

A separate 2023 ten-patient study showed immature, activated STAT1-GOF neutrophils with enhanced degranulation, NETosis, platelet aggregation, basal STAT1 phosphorylation, and interferon-stimulated genes. Ruxolitinib did **not** normalize this signature. The abstract states that neutrophils had a **“strong propensity for degranulation, NETosis, and platelet-neutrophil aggregation.”** (DOI: https://doi.org/10.1007/s10875-023-01528-1). (parackova2023neutrophilsinstat1 pages 1-3)

These are small exploratory studies. No validated single-cell atlas, spatial transcriptomic diagnostic signature, integrated lipidome/metabolome, or clinically deployed CRISPR-screen result was identified.

## 7. Anatomical structures affected

Primary sites are oral mucosa/tongue/oropharynx, esophageal epithelium, genital mucosa, epidermis and skin folds, scalp, periungual tissue, and nail plate/bed. Suggested UBERON annotations include oral epithelium, tongue, esophagus **UBERON:0001043**, skin of body **UBERON:0002097**, nail, scalp, vagina **UBERON:0000996**, and penis/glans where applicable. Disease is not lateralized.

Relevant tissues are stratified squamous epithelium and keratinized appendages. Key target/responding cells are keratinocytes and mucosal epithelial cells; immune participants include Th17 cells, neutrophils, monocytes, dendritic cells, NK cells, and B/T lymphocytes. Subcellular compartments depend on genotype: plasma membrane for IL-17RA/RC and Dectin-1; cytosol for CARD9 and ACT1; cytoplasm/nucleus for STAT1; nucleus for RORC and AIRE. Suggested GO cellular components include plasma membrane GO:0005886, cytoplasm GO:0005737, cytosol GO:0005829, and nucleus GO:0005634.

## 8. Temporal development

Onset is usually pediatric and insidious, often beginning as persistent oral thrush; most STAT1-GOF cases begin in early childhood, though diagnosis may be delayed into adulthood. More than 95% of STAT1-GOF patients reportedly manifest before 35 years. (egri2021primaryimmunodeficiencyand pages 7-8, meesilpavikkai2024unravelingtheimmunogenetics pages 4-7)

The natural course is chronic, episodic, and relapsing rather than a fixed staged disease. Oral disease can progress to nails, skin, esophagus, and genital sites. Treatment induces remission, but recurrence is common: in the 26-person STAT1 cohort, 87% of esophageal cases relapsed despite 67% achieving complete remission during treatment. (depner2016theextendedclinical pages 6-8)

Critical intervention periods include early childhood—before recurrent infection causes nutritional, dental, nail, or pulmonary injury—and before prolonged inflammation/azole exposure creates resistance or malignancy risk. Rapid recurrence after JAK-inhibitor withdrawal has been reported, so remission should not be equated with cure. (egri2021primaryimmunodeficiencyand pages 7-8)

## 9. Inheritance and population

Inheritance is genotype-specific: autosomal dominant for most STAT1 GOF and IL17F disease; autosomal recessive for IL17RA, IL17RC, TRAF3IP2, CARD9, RORC, and classic AIRE-associated APS-1. STAT1 GOF displays variable expressivity and may arise de novo. Penetrance is high but not uniformly quantified across variants. Anticipation is not expected. Germline mosaicism is theoretically possible but not a documented common mechanism.

CMC is ultra-rare, but reliable population-wide incidence or prevalence per 100,000 is unavailable because it is a phenotype spanning multiple disorders. APS-1 prevalence is approximately **1:100,000 globally**, with enrichment in Finns, Sardinians, and Persian Jews. (egri2021primaryimmunodeficiencyand pages 5-6)

No consistent sex bias is established; one recent mechanistic cohort included 3 males and 7 females, but this is not an epidemiologic ratio. (parackova2023neutrophilsinstat1 pages 1-3) Founder effects and consanguinity are important for recessive AIRE, CARD9, and IL-17-pathway disease in particular populations. Carrier frequency must be calculated gene/variant/population-specifically from gnomAD; no defensible aggregate CMC carrier frequency exists.

## 10. Diagnostics

### Clinical and microbiological evaluation

Diagnosis requires persistent/recurrent candidiasis confirmed by microscopy and culture or molecular identification, coupled with exclusion of common secondary causes. Record species and antifungal susceptibility, especially after azole exposure. Endoscopy with brushings/biopsy is appropriate for dysphagia or suspected esophageal disease. Histology typically shows yeast/pseudohyphae in superficial epithelium with inflammation; imaging is not routine unless evaluating lung damage, aneurysm/vasculopathy, deep fungal disease, or CARD9-associated CNS infection.

### Immune work-up

Recommended baseline tests are CBC/differential, lymphocyte subsets (T, B, NK), immunoglobulins, HIV testing, glucose/HbA1c, liver/renal tests, and evaluation for endocrine autoimmunity. The review recommends quantifying T, B, and NK cells and ruling out secondary causes before establishing an inborn error. (egri2021primaryimmunodeficiencyand pages 5-6)

Genotype-directed functional tests include:

* frequency of circulating Th17/CD4+IL-17+ cells;
* Candida-specific T-cell proliferation/cytokine production;
* IL-17A, IL-17F, and IL-22 production;
* STAT1 phosphorylation after IFN-α, IFN-γ, or IL-27 and, where possible, dephosphorylation kinetics;
* anti-IL-17A/F and anti-IL-22 autoantibodies when APS-1 is suspected.

Flow-cytometric phospho-STAT1 testing is a rapid adjunct, not a substitute for molecular confirmation. In the international cohort, stimulated patient PBMCs showed hyperphosphorylation; the authors explicitly recommended it alongside genetic testing. (depner2016theextendedclinical pages 1-2, depner2016theextendedclinical pages 5-6)

### Genetic testing strategy

1. Use an inborn-error-of-immunity/CMC panel including at minimum **STAT1, IL17F, IL17RA, IL17RC, TRAF3IP2, CARD9, CLEC7A, RORC, AIRE**, plus syndromic genes such as STAT3 and DOCK8.
2. If phenotype strongly suggests STAT1 GOF, sequence STAT1 with copy-number analysis and functional validation.
3. If panel-negative, proceed to trio WES or WGS; WGS is valuable for noncoding, copy-number, and structural variants.
4. Reanalyze periodically as disease genes expand.
5. CMA/karyotype/FISH, mtDNA, and repeat-expansion testing are not first-line unless unrelated features suggest another diagnosis.

Cascade testing is appropriate after a pathogenic familial variant is found. Prenatal and preimplantation testing are technically feasible for a known familial variant.

### Differential diagnosis

Exclude HIV, diabetes, antibiotics/corticosteroids, neutropenia, severe combined/combined immunodeficiency, hyper-IgE syndrome, DOCK8 deficiency, common variable immunodeficiency, chronic granulomatous disease, APS-1, CARD9 deficiency, thymoma-associated immunodeficiency, and ordinary recurrent vulvovaginal candidiasis. Deep CNS candidiasis strongly suggests CARD9; candidiasis plus hypoparathyroidism/Addison disease suggests AIRE; CMC plus viral/bacterial infection, autoimmunity, and vasculopathy suggests STAT1 GOF.

## 11. Outcome and prognosis

There are no validated 5- or 10-year survival statistics for CMC as a whole. Isolated IL-17-pathway disease is often compatible with long survival but requires chronic antifungal management. Prognosis worsens with invasive fungal disease, recurrent bacterial/viral infection, bronchiectasis, endocrine crisis, vasculopathy/aneurysm, malignancy, or multidrug-resistant *Candida*.

In the 26-person STAT1 cohort, azoles produced partial remission in **62%** and complete response in **38%**; 58% required antifungal prophylaxis. (depner2016theextendedclinical pages 6-8) HSCT evidence is highly selected: one review summarized only **4/15** symptomatic patients achieving immune reconstitution while **9 died**, indicating substantial transplant risk and likely confounding by severe baseline disease. Outcomes were better when transplantation occurred in stable patients. (egri2021primaryimmunodeficiencyand pages 8-9)

Longstanding mouth/esophageal inflammation warrants surveillance because squamous-cell carcinoma is reported. Functional morbidity includes pain, dysphagia, poor intake, nail destruction, recurrent medical care, treatment toxicity, and psychosocial burden. Validated prognostic biomarkers are lacking; candidate markers include genotype/domain, infection burden, organ damage, autoimmunity, treatment response, CXCL10/IFN signature, and persistent neutrophil activation.

## 12. Treatment and real-world implementation

### Antifungal therapy

First-line treatment is usually a topical agent for limited disease and a systemic azole—commonly fluconazole—for extensive, nail, esophageal, or recurrent disease. Culture and susceptibility testing should guide refractory disease. Alternatives include itraconazole, posaconazole, voriconazole, isavuconazole, echinocandins, and amphotericin B according to site, species, resistance, interactions, and toxicity. Azoles inhibit fungal lanosterol 14α-demethylase; echinocandins inhibit β-1,3-D-glucan synthase; amphotericin binds ergosterol. Suggested NCIt intervention terms include Fluconazole, Itraconazole, Voriconazole, Posaconazole, Isavuconazole, Amphotericin B, Caspofungin/Micafungin/Anidulafungin, Antifungal Therapy, and Hematopoietic Stem Cell Transplantation.

Long-term suppression is frequently needed, but monitor hepatic toxicity, QT effects, drug interactions, and resistance. In the 26-person cohort, treatment often controlled rather than eradicated disease. (depner2016theextendedclinical pages 6-8)

### Genotype-directed immune therapy

**Ruxolitinib** and **baricitinib** inhibit JAK signaling upstream of STAT1 and are off-label precision therapies for severe STAT1 GOF with refractory CMC or autoimmunity. They can improve IL-17 responses and clinical disease, but infection, cytopenia, liver injury, thrombosis and viral reactivation require monitoring. Treatment duration is undefined and relapse may follow withdrawal. (egri2021primaryimmunodeficiencyand pages 7-8)

In three adults, baricitinib 2 mg/day improved mucocutaneous inflammation within one month in one patient. Another stopped after three weeks because of painful aphthae, cough, fever, and elevated liver enzymes. Ruxolitinib 15 mg/day initially helped a third patient, but recurrent respiratory infections developed after one year; that patient subsequently improved after HSCT. (borgstrom2023threeadultcases pages 12-13, borgstrom2023threeadultcases pages 4-5)

HSCT is potentially curative but should be reserved for severe, life-threatening, medically refractory immune dysregulation after expert multidisciplinary assessment; published mortality is substantial. (egri2021primaryimmunodeficiencyand pages 7-8, egri2021primaryimmunodeficiencyand pages 8-9)

### Experimental/registered studies

Relevant registered implementations include NIH natural-history study **NCT01386437** (recruiting; planned enrollment 1,200), phase 2 oral MAT2203 in mucocutaneous candidiasis **NCT02629419** (completed; n=4), phase 3 ibrexafungerp for refractory/intolerant fungal disease **NCT03059992** (completed; n=233, not CMC-specific), and anti-cytokine-autoantibody disease study **NCT01842386** (completed; n=7). These registrations establish research activity, not routine efficacy for Mendelian CMC.

No approved gene, RNA, or CRISPR therapy exists. No established CMC-specific pharmacogenomic dosing guideline from CPIC/PharmGKB was identified; CYP-mediated interactions remain clinically important for azoles.

## 13. Prevention

There is no licensed *Candida* vaccine or population screening program for CMC. Primary prevention of the germline disorder is limited to reproductive counseling. Secondary prevention consists of early recognition, culture confirmation, immune/genetic diagnosis, cascade testing, and prompt treatment before irreversible tissue damage. Tertiary prevention includes susceptibility-guided suppression, oral/dental care, skin-fold care, endocrine surveillance, pulmonary monitoring, avoidance of unnecessary antibiotics, and surveillance for oral/esophageal malignancy in longstanding disease.

Families with a molecular diagnosis should receive counseling on genotype-specific recurrence: approximately 50% per pregnancy for a heterozygous autosomal-dominant variant and 25% affected/50% carrier risk when both parents carry the same autosomal-recessive allele. These are Mendelian expectations and may be modified by de novo status, penetrance, or parental mosaicism.

## 14. Other species and natural disease

Mucocutaneous candidiasis occurs in animals, but no well-established naturally occurring veterinary disorder was identified that is directly orthologous to the full human STAT1-GOF/IL-17-deficient CMC phenotype. *Candida* is generally opportunistic across species. The disease is not considered zoonotic in the usual sense; human CMC reflects host susceptibility rather than sustained animal-to-human transmission.

Relevant taxa include human **NCBI Taxon 9606**, mouse **10090**, zebrafish **7955**, and *Candida albicans* **5476**. Orthologues of STAT1, IL17RA, CARD9, RORC, and TRAF3IP2 are evolutionarily conserved, supporting comparative mechanistic studies. Breed-specific VBO annotations and an OMIA-equivalent natural Mendelian syndrome were not established from the retrieved evidence.

## 15. Model organisms

* **Mouse:** Il17ra-knockout mice are highly susceptible to *C. albicans*; one study reported rapid death after systemic challenge, demonstrating IL-17RA’s role in fungal immunity. However, systemic candidiasis is not identical to chronic human mucocutaneous disease. (OpenTargets Search: chronic mucocutaneous candidiasis)
* **Genetic mouse models:** Stat1-GOF knock-in, Aire-null, Card9-null, Il17ra/Il17rc-null, Act1-deficient, and Rorc-deficient systems can dissect cytokine production, receptor signaling, autoantibodies, neutrophil recruitment, and organ tropism. Their limitations include species-specific Candida commensalism and immune development.
* **Zebrafish:** larval/adult *C. albicans* infection permits live imaging and antifungal screening, but does not reproduce human nail/oral chronicity.
* **Cellular systems:** patient PBMCs, Candida-stimulated whole blood, phospho-flow assays, primary keratinocytes, epithelial cultures, and gene-edited cell lines are the most directly translational models. Patient-derived organoids/iPSCs are plausible but not yet standard CMC platforms.

Applications include variant functional classification, defining STAT1 dephosphorylation, testing IL-17 signaling, evaluating Candida-specific lymphocyte responses, and preclinical JAK-inhibitor or antifungal studies.

## Evidence quality, current expert interpretation, and knowledge gaps

The highest-confidence conclusions are that CMC is genetically heterogeneous, barrier IL-17 immunity is central, STAT1 GOF is the leading recognized cause, and management requires both fungal control and diagnosis of the underlying immune defect. The 2021 review’s abstract states: **“The key immune defect is a disruption of the action of cytokine IL-17, whose most common genetic etiology is STAT1 gene gain-of-function mutations.”** (DOI: https://doi.org/10.15586/aei.v49i1.20). (egri2021primaryimmunodeficiencyand pages 1-2)

The major limitations are rarity, referral bias, mixing of molecular subtypes, retrospective cohorts, and small uncontrolled treatment series. Epidemiologic incidence, genotype-specific penetrance, quality-of-life scores, variant-level carrier frequencies, long-term JAK-inhibitor safety, transplant selection criteria, protective modifiers, epigenomics, spatial/single-cell atlases, and validated prognostic biomarkers remain insufficiently defined. Accordingly, cohort percentages should always retain the genotype and denominator, and JAK inhibition should be described as promising off-label precision therapy—not established universal CMC treatment.

References

1. (cinicola2024mucocutaneouscandidiasisinsights pages 1-2): Bianca Laura Cinicola, Andrea Uva, Marzia Duse, Anna Maria Zicari, and Danilo Buonsenso. Mucocutaneous candidiasis: insights into the diagnosis and treatment. The Pediatric Infectious Disease Journal, 43:694-703, Mar 2024. URL: https://doi.org/10.1097/inf.0000000000004321, doi:10.1097/inf.0000000000004321. This article has 6 citations.

2. (egri2021primaryimmunodeficiencyand pages 1-2): Natalia Egri, Ana Esteve-Solé, Àngela Deyà-Martínez, Iñaki Ortiz de Landazuri, Alexandru Vlagea, AP Garcia, Celia Cardozo, Carolina Garcia-Vidal, Clara San Bartolomé, Marta Español-Rego, L Yiyi, Xavier Bosch-Amate, J Ferrando, Jordi Yagüe, Manel Juan, and Laia Alsina. Primary immunodeficiency and chronic mucocutaneous candidiasis: pathophysiological, diagnostic, and therapeutic approaches. Allergologia et immunopathologia, 49 1:118-127, Jan 2021. URL: https://doi.org/10.15586/aei.v49i1.20, doi:10.15586/aei.v49i1.20. This article has 26 citations and is from a peer-reviewed journal.

3. (egri2021primaryimmunodeficiencyand pages 7-8): Natalia Egri, Ana Esteve-Solé, Àngela Deyà-Martínez, Iñaki Ortiz de Landazuri, Alexandru Vlagea, AP Garcia, Celia Cardozo, Carolina Garcia-Vidal, Clara San Bartolomé, Marta Español-Rego, L Yiyi, Xavier Bosch-Amate, J Ferrando, Jordi Yagüe, Manel Juan, and Laia Alsina. Primary immunodeficiency and chronic mucocutaneous candidiasis: pathophysiological, diagnostic, and therapeutic approaches. Allergologia et immunopathologia, 49 1:118-127, Jan 2021. URL: https://doi.org/10.15586/aei.v49i1.20, doi:10.15586/aei.v49i1.20. This article has 26 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: chronic mucocutaneous candidiasis): Open Targets Query (chronic mucocutaneous candidiasis, 18 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (egri2021primaryimmunodeficiencyand pages 5-6): Natalia Egri, Ana Esteve-Solé, Àngela Deyà-Martínez, Iñaki Ortiz de Landazuri, Alexandru Vlagea, AP Garcia, Celia Cardozo, Carolina Garcia-Vidal, Clara San Bartolomé, Marta Español-Rego, L Yiyi, Xavier Bosch-Amate, J Ferrando, Jordi Yagüe, Manel Juan, and Laia Alsina. Primary immunodeficiency and chronic mucocutaneous candidiasis: pathophysiological, diagnostic, and therapeutic approaches. Allergologia et immunopathologia, 49 1:118-127, Jan 2021. URL: https://doi.org/10.15586/aei.v49i1.20, doi:10.15586/aei.v49i1.20. This article has 26 citations and is from a peer-reviewed journal.

6. (parackova2023neutrophilsinstat1 pages 1-3): Zuzana Parackova, Petra Vrabcova, Irena Zentsova, Anna Sediva, and Marketa Bloomfield. Neutrophils in stat1 gain-of-function have a pro-inflammatory signature which is not rescued by jak inhibition. Journal of Clinical Immunology, 43:1640-1659, Jun 2023. URL: https://doi.org/10.1007/s10875-023-01528-1, doi:10.1007/s10875-023-01528-1. This article has 16 citations and is from a domain leading peer-reviewed journal.

7. (meesilpavikkai2024unravelingtheimmunogenetics pages 4-7): Kornvalee Meesilpavikkai, N. Hirankarn, Virgil A.S.H. Dalm, P. M. Hagen, Willem A. Dik, and Hanna IJspeert. Unraveling the immunogenetics of stat proteins: clinical perspectives on gain-of-function and loss-of-function variants. Asian Pacific journal of allergy and immunology, May 2024. URL: https://doi.org/10.12932/ap-270124-1776, doi:10.12932/ap-270124-1776. This article has 7 citations and is from a peer-reviewed journal.

8. (depner2016theextendedclinical pages 1-2): Mark Depner, Sebastian Fuchs, Jan Raabe, Natalie Frede, Cristina Glocker, Rainer Doffinger, Effrossyni Gkrania-Klotsas, Dinakantha Kumararatne, T. Prescott Atkinson, Harry W. Schroeder, Tim Niehues, Gregor Dückers, Asbjørg Stray-Pedersen, Ulrich Baumann, Reinhold Schmidt, Jose L. Franco, Julio Orrego, Moshe Ben-Shoshan, Christine McCusker, Cristina Miuki Abe Jacob, Magda Carneiro-Sampaio, Lisa A. Devlin, J. David M. Edgar, Paul Henderson, Richard K. Russell, Anne-Bine Skytte, Suranjith L. Seneviratne, Jennifer Wanders, Hans Stauss, Isabelle Meyts, Leen Moens, Milos Jesenak, Robin Kobbe, Stephan Borte, Michael Borte, Dowain A. Wright, David Hagin, Troy R. Torgerson, and Bodo Grimbacher. The extended clinical phenotype of 26 patients with chronic mucocutaneous candidiasis due to gain-of-function mutations in stat1. Journal of Clinical Immunology, 36:73-84, Nov 2016. URL: https://doi.org/10.1007/s10875-015-0214-9, doi:10.1007/s10875-015-0214-9. This article has 177 citations and is from a domain leading peer-reviewed journal.

9. (egri2021primaryimmunodeficiencyand pages 8-9): Natalia Egri, Ana Esteve-Solé, Àngela Deyà-Martínez, Iñaki Ortiz de Landazuri, Alexandru Vlagea, AP Garcia, Celia Cardozo, Carolina Garcia-Vidal, Clara San Bartolomé, Marta Español-Rego, L Yiyi, Xavier Bosch-Amate, J Ferrando, Jordi Yagüe, Manel Juan, and Laia Alsina. Primary immunodeficiency and chronic mucocutaneous candidiasis: pathophysiological, diagnostic, and therapeutic approaches. Allergologia et immunopathologia, 49 1:118-127, Jan 2021. URL: https://doi.org/10.15586/aei.v49i1.20, doi:10.15586/aei.v49i1.20. This article has 26 citations and is from a peer-reviewed journal.

10. (cinicola2024mucocutaneouscandidiasisinsights pages 9-9): Bianca Laura Cinicola, Andrea Uva, Marzia Duse, Anna Maria Zicari, and Danilo Buonsenso. Mucocutaneous candidiasis: insights into the diagnosis and treatment. The Pediatric Infectious Disease Journal, 43:694-703, Mar 2024. URL: https://doi.org/10.1097/inf.0000000000004321, doi:10.1097/inf.0000000000004321. This article has 6 citations.

11. (depner2016theextendedclinical pages 6-8): Mark Depner, Sebastian Fuchs, Jan Raabe, Natalie Frede, Cristina Glocker, Rainer Doffinger, Effrossyni Gkrania-Klotsas, Dinakantha Kumararatne, T. Prescott Atkinson, Harry W. Schroeder, Tim Niehues, Gregor Dückers, Asbjørg Stray-Pedersen, Ulrich Baumann, Reinhold Schmidt, Jose L. Franco, Julio Orrego, Moshe Ben-Shoshan, Christine McCusker, Cristina Miuki Abe Jacob, Magda Carneiro-Sampaio, Lisa A. Devlin, J. David M. Edgar, Paul Henderson, Richard K. Russell, Anne-Bine Skytte, Suranjith L. Seneviratne, Jennifer Wanders, Hans Stauss, Isabelle Meyts, Leen Moens, Milos Jesenak, Robin Kobbe, Stephan Borte, Michael Borte, Dowain A. Wright, David Hagin, Troy R. Torgerson, and Bodo Grimbacher. The extended clinical phenotype of 26 patients with chronic mucocutaneous candidiasis due to gain-of-function mutations in stat1. Journal of Clinical Immunology, 36:73-84, Nov 2016. URL: https://doi.org/10.1007/s10875-015-0214-9, doi:10.1007/s10875-015-0214-9. This article has 177 citations and is from a domain leading peer-reviewed journal.

12. (ostadi2021functionalanalysisof pages 1-2): Vajiheh Ostadi, Roya Sherkat, Melanie Migaud, Seyed-Mehran Modaressadeghi, Jean-Laurent Casanova, Anne Puel, Nioosha Nekooie-Marnany, and Mazdak Ganjalikhani-Hakemi. Functional analysis of two stat1 gain-of-function mutations in two iranian families with autosomal dominant chronic mucocutaneous candidiasis. Medical mycology, 59:180-188, Jun 2021. URL: https://doi.org/10.1093/mmy/myaa043, doi:10.1093/mmy/myaa043. This article has 14 citations and is from a peer-reviewed journal.

13. (ostadi2021functionalanalysisof pages 7-8): Vajiheh Ostadi, Roya Sherkat, Melanie Migaud, Seyed-Mehran Modaressadeghi, Jean-Laurent Casanova, Anne Puel, Nioosha Nekooie-Marnany, and Mazdak Ganjalikhani-Hakemi. Functional analysis of two stat1 gain-of-function mutations in two iranian families with autosomal dominant chronic mucocutaneous candidiasis. Medical mycology, 59:180-188, Jun 2021. URL: https://doi.org/10.1093/mmy/myaa043, doi:10.1093/mmy/myaa043. This article has 14 citations and is from a peer-reviewed journal.

14. (borgstrom2023threeadultcases pages 1-2): Emilie W. Borgström, Marie Edvinsson, Lucía P. Pérez, Anna C. Norlin, Sara L. Enoksson, Susanne Hansen, Anders Fasth, Vanda Friman, Olle Kämpe, Robert Månsson, Hernando Y. Estupiñán, Qing Wang, Tan Ziyang, Tadepally Lakshmikanth, Carl Inge E. Smith, Petter Brodin, and Peter Bergman. Three adult cases of stat1 gain-of-function with chronic mucocutaneous candidiasis treated with jak inhibitors. Journal of Clinical Immunology, 43:136-150, Sep 2023. URL: https://doi.org/10.1007/s10875-022-01351-0, doi:10.1007/s10875-022-01351-0. This article has 32 citations and is from a domain leading peer-reviewed journal.

15. (borgstrom2023threeadultcases pages 7-11): Emilie W. Borgström, Marie Edvinsson, Lucía P. Pérez, Anna C. Norlin, Sara L. Enoksson, Susanne Hansen, Anders Fasth, Vanda Friman, Olle Kämpe, Robert Månsson, Hernando Y. Estupiñán, Qing Wang, Tan Ziyang, Tadepally Lakshmikanth, Carl Inge E. Smith, Petter Brodin, and Peter Bergman. Three adult cases of stat1 gain-of-function with chronic mucocutaneous candidiasis treated with jak inhibitors. Journal of Clinical Immunology, 43:136-150, Sep 2023. URL: https://doi.org/10.1007/s10875-022-01351-0, doi:10.1007/s10875-022-01351-0. This article has 32 citations and is from a domain leading peer-reviewed journal.

16. (depner2016theextendedclinical pages 5-6): Mark Depner, Sebastian Fuchs, Jan Raabe, Natalie Frede, Cristina Glocker, Rainer Doffinger, Effrossyni Gkrania-Klotsas, Dinakantha Kumararatne, T. Prescott Atkinson, Harry W. Schroeder, Tim Niehues, Gregor Dückers, Asbjørg Stray-Pedersen, Ulrich Baumann, Reinhold Schmidt, Jose L. Franco, Julio Orrego, Moshe Ben-Shoshan, Christine McCusker, Cristina Miuki Abe Jacob, Magda Carneiro-Sampaio, Lisa A. Devlin, J. David M. Edgar, Paul Henderson, Richard K. Russell, Anne-Bine Skytte, Suranjith L. Seneviratne, Jennifer Wanders, Hans Stauss, Isabelle Meyts, Leen Moens, Milos Jesenak, Robin Kobbe, Stephan Borte, Michael Borte, Dowain A. Wright, David Hagin, Troy R. Torgerson, and Bodo Grimbacher. The extended clinical phenotype of 26 patients with chronic mucocutaneous candidiasis due to gain-of-function mutations in stat1. Journal of Clinical Immunology, 36:73-84, Nov 2016. URL: https://doi.org/10.1007/s10875-015-0214-9, doi:10.1007/s10875-015-0214-9. This article has 177 citations and is from a domain leading peer-reviewed journal.

17. (borgstrom2023threeadultcases pages 12-13): Emilie W. Borgström, Marie Edvinsson, Lucía P. Pérez, Anna C. Norlin, Sara L. Enoksson, Susanne Hansen, Anders Fasth, Vanda Friman, Olle Kämpe, Robert Månsson, Hernando Y. Estupiñán, Qing Wang, Tan Ziyang, Tadepally Lakshmikanth, Carl Inge E. Smith, Petter Brodin, and Peter Bergman. Three adult cases of stat1 gain-of-function with chronic mucocutaneous candidiasis treated with jak inhibitors. Journal of Clinical Immunology, 43:136-150, Sep 2023. URL: https://doi.org/10.1007/s10875-022-01351-0, doi:10.1007/s10875-022-01351-0. This article has 32 citations and is from a domain leading peer-reviewed journal.

18. (borgstrom2023threeadultcases pages 4-5): Emilie W. Borgström, Marie Edvinsson, Lucía P. Pérez, Anna C. Norlin, Sara L. Enoksson, Susanne Hansen, Anders Fasth, Vanda Friman, Olle Kämpe, Robert Månsson, Hernando Y. Estupiñán, Qing Wang, Tan Ziyang, Tadepally Lakshmikanth, Carl Inge E. Smith, Petter Brodin, and Peter Bergman. Three adult cases of stat1 gain-of-function with chronic mucocutaneous candidiasis treated with jak inhibitors. Journal of Clinical Immunology, 43:136-150, Sep 2023. URL: https://doi.org/10.1007/s10875-022-01351-0, doi:10.1007/s10875-022-01351-0. This article has 32 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Chronic_Mucocutaneous_Candidiasis-deep-research-falcon_artifacts/artifact-00.md)