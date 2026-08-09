---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:46:28.690296'
end_time: '2026-08-01T18:54:11.004190'
duration_seconds: 462.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Heart Defects and Skeletal Malformations Syndrome
  mondo_id: MONDO:0060532,OMIM:617602,gene=ABL1/HGNC:76,acronym=CHDSKM,NOT-Holt-Oram-TBX5,NOT-Ellis-van-Creveld,NOT-VACTERL,NOT-Char-syndrome
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Heart_Defects_and_Skeletal_Malformations_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Heart Defects and Skeletal Malformations Syndrome
- **MONDO ID:** MONDO:0060532,OMIM:617602,gene=ABL1/HGNC:76,acronym=CHDSKM,NOT-Holt-Oram-TBX5,NOT-Ellis-van-Creveld,NOT-VACTERL,NOT-Char-syndrome (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Defects and Skeletal Malformations Syndrome** covering all of the
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
- **Disease Name:** Congenital Heart Defects and Skeletal Malformations Syndrome
- **MONDO ID:** MONDO:0060532,OMIM:617602,gene=ABL1/HGNC:76,acronym=CHDSKM,NOT-Holt-Oram-TBX5,NOT-Ellis-van-Creveld,NOT-VACTERL,NOT-Char-syndrome (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Defects and Skeletal Malformations Syndrome** covering all of the
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


# Congenital Heart Defects and Skeletal Malformations Syndrome (CHDSKM)

## Executive summary

Congenital heart defects and skeletal malformations syndrome is an ultra-rare, congenital, autosomal-dominant developmental disorder caused by heterozygous **gain-of-function missense variants in ABL1**. The cardinal phenotype comprises congenital heart disease, digital/skeletal abnormalities, characteristic facial dysmorphism, prenatal or postnatal growth impairment, and variably developmental delay, microcephaly, palatal anomalies, and hearing loss. It is mechanistically distinct from BCR::ABL1-positive leukemia and from recently described biallelic loss-of-function **ABL1 deficiency**. The evidence base remains small—approximately 18 aggregated individuals by the principal 2021 series—so frequencies, penetrance, prognosis, and management recommendations are provisional. (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 3-4)

The foundational paper reported that “ABL1 germline variants [co-segregate] with an autosomal dominant disorder characterized by congenital heart disease, skeletal abnormalities, and failure to thrive.” It identified recurrent p.Tyr245Cys and de novo p.Ala356Thr and showed increased tyrosine phosphorylation in transfected cells. [Wang et al., *Nature Genetics*, published March 2017; PMID: **28288113**; DOI: **10.1038/ng.3815**; https://doi.org/10.1038/ng.3815]. (wang2017germlinemutationsin pages 3-3, wang2017germlinemutationsin pages 1-2)

A useful evidence synopsis is provided below.

| Domain | Best-supported finding | Quantitative evidence | Evidence type/source |
|---|---|---|---|
| Disease identifiers | ABL1-related congenital heart defects and skeletal malformations syndrome is a Mendelian developmental disorder linked to **MONDO:0060532** and **ABL1**; Open Targets shows a single strong disease-target association for ABL1. | Open Targets association score **0.8012**; evidence count **5** tied to the foundational literature. | Curated disease-target resource and literature linkage (Open Targets context) (OpenTargets Search: congenital heart defects and skeletal malformations syndrome-ABL1) |
| Core definition | Foundational human evidence established that **germline ABL1 variants cause an autosomal dominant syndrome characterized by congenital heart defects, skeletal abnormalities/malformations, dysmorphic features, and failure to thrive**. | Initial report: **6 affected individuals** from **4 families**. | Human clinical genetics, Nature Genetics 2017, doi:10.1038/ng.3815 (PMID linked in Open Targets as **28288113**) (wang2017germlinemutationsin pages 3-3, wang2017germlinemutationsin pages 1-2) |
| Inheritance | CHDSKM shows **autosomal dominant** inheritance with both **de novo** occurrence and vertical transmission/cosegregation in families. | 2017 series: **p.Tyr245Cys** occurred **de novo or cosegregated** in families 1-3; **p.Ala356Thr** was **de novo** in family 4. 2021 series: **5/6** new cases had **de novo confirmation**. | Human clinical genetics, Nature Genetics 2017 doi:10.1038/ng.3815; Eur J Hum Genet 2021 doi:10.1038/s41431-020-00766-w (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 6-8) |
| Molecular mechanism class | The disorder is best supported as an **ABL1 gain-of-function kinase syndrome**, not haploinsufficiency. Mutant proteins show increased tyrosine phosphorylation/kinase activity. | Increased phosphorylation of ABL1-specific substrates in HEK293T/HEK 293T assays for **p.Tyr245Cys, p.Ala356Thr**, and additional 2021 variants; 2024 biochemical work shows **E528K vmax ~202 vs WT ~89** (>2-fold), with **KM unchanged**. | Human variant functional assays and biochemical/structural studies, 2017/2021/2024 (doi:10.1038/ng.3815; doi:10.1038/s41431-020-00766-w; doi:10.1101/2023.10.04.560671) (blakes2021pathogenicvariantscausing pages 1-2, wang2017germlinemutationsin pages 3-4, paladini2024themolecularbasis pages 9-10, paladini2024themolecularbasis pages 6-9) |
| Variant spectrum | Reported pathogenic CHDSKM missense variants include **p.Tyr245Cys, p.Val244Ala, p.Ala356Thr, p.Ala452Thr, p.Val525Ala, p.Glu528Lys**. Several cluster in/near the kinase regulatory myristoyl-binding pocket. | 2017: **2 variants** (**c.734A>G p.Tyr245Cys**, **c.1066G>A p.Ala356Thr**). 2021: total **5 germline variants** listed as **c.731T>C p.Val244Ala**, **c.1066G>A p.Ala356Thr**, **c.1354G>A p.Ala452Thr**, **c.1574T>C p.Val525Ala**, **c.1582G>A p.Glu528Lys**. | Human clinical/variant interpretation studies, 2017 and 2021 (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 5-6) |
| Variant: Tyr245Cys | **p.Tyr245Cys** is a recurrent causal variant in the **SH2-kinase linker region** associated with CHDSKM and increased kinase signaling. | Seen in **5 individuals** across families 1-3 in the 2017 report; absent from dbSNP/ESP/ExAC/COSMIC in that study. | Human clinical genetics plus in vitro functional assay, Nature Genetics 2017 doi:10.1038/ng.3815 (PMID 28288113 via Open Targets) (wang2017germlinemutationsin pages 3-3, wang2017germlinemutationsin pages 3-4) |
| Variant: Val244Ala | **p.Val244Ala** is a de novo CHDSKM variant affecting the SH2-kinase linker/regulatory region and functionally increases ABL1 signaling. | Reported among the **6 new unrelated individuals** in 2021; described as **de novo**; functional assays showed increased STAT5B/overall tyrosine phosphorylation. | Human case series with in vitro functional validation, Eur J Hum Genet 2021 doi:10.1038/s41431-020-00766-w (blakes2021pathogenicvariantscausing pages 8-9, blakes2021pathogenicvariantscausing pages 6-8) |
| Variant: Ala356Thr | **p.Ala356Thr** is a de novo kinase-domain CHDSKM variant with increased kinase activity. | Present in **1 individual** in 2017 and also represented in 2021 aggregated variant list; increased phosphotyrosine and STAT5 phosphorylation in vitro. | Human clinical genetics and in vitro assay, 2017/2021 (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 5-6, blakes2021pathogenicvariantscausing pages 4-5) |
| Variant: Ala452Thr | **p.Ala452Thr** is a CHDSKM-associated kinase-domain variant included in the expanded 2021 spectrum. | Listed among pathogenic/likely pathogenic variants in 2021; individual table excerpt notes growth, craniofacial, and cardiac findings in affected patient(s). | Human case series, Eur J Hum Genet 2021 doi:10.1038/s41431-020-00766-w (blakes2021pathogenicvariantscausing pages 5-6, blakes2021pathogenicvariantscausing pages 4-5) |
| Variant: Val525Ala | **p.Val525Ala** is a de novo variant in the **myristoyl-binding pocket/kinase domain** supporting the autoinhibition-loss model. | Included in 2021 five-variant set; one of the variants clustering in the myristoyl pocket. | Human case series with structural interpretation and kinase assay, Eur J Hum Genet 2021 doi:10.1038/s41431-020-00766-w (blakes2021pathogenicvariantscausing pages 8-9, blakes2021pathogenicvariantscausing pages 5-6) |
| Variant: Glu528Lys | **p.Glu528Lys (E528K)** is a de novo myristoyl-pocket/αI'-helix variant strongly linked to gain-of-function and later structural definition. | Included in 2021 case series as de novo; 2024 study shows disruption of the **E528-R479** salt bridge, increased core disassembly, and **>2-fold** activity increase. | Human case series + biochemical/structural mechanism, 2021/2024 (blakes2021pathogenicvariantscausing pages 8-9, paladini2024themolecularbasis pages 9-10, paladini2024themolecularbasis pages 11-12, paladini2024themolecularbasis pages 10-11) |
| Population frequency | Reported CHDSKM variants are extremely rare; the expanded 2021 series states all listed pathogenic variants were **absent from gnomAD**. | **5/5** listed 2021 variants absent from gnomAD; 2017 variants absent from dbSNP, ESP, ExAC, COSMIC. | Human variant interpretation, 2017 and 2021 (blakes2021pathogenicvariantscausing pages 5-6, wang2017germlinemutationsin pages 3-4) |
| Aggregated phenotype burden | Across the **18 reported cases** summarized in 2021, the most frequent findings were dysmorphic facies, digital anomalies, congenital heart disease, failure to thrive, developmental delay, IUGR, ear abnormalities, palatal deformity, and microcephaly. | **Dysmorphic facies 18/18 (100%)**; **finger/toe abnormalities 17/18 (94%)**; **congenital heart disease 14/18 (78%)**; **failure to thrive 14/18 (78%)**; **developmental delay 11/18 (61%)**; **IUGR 10/18 (56%)**; **ear abnormalities 9/18 (50%)**; **palatal deformity 9/18 (50%)**; **microcephaly 9/18 (50%)**. | Aggregated human case series, Eur J Hum Genet 2021 doi:10.1038/s41431-020-00766-w (blakes2021pathogenicvariantscausing pages 3-4) |
| Cardiac phenotype | Cardiac disease is a cardinal manifestation; specific reported defects include septal defects, patent ductus arteriosus, supravalvular pulmonary stenosis, and aortic root dilatation. | CHD in **6/6** initial 2017 patients and **14/18** pooled cases by 2021. | Human clinical case reports/series, 2017 and 2021 (wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 8-9, blakes2021pathogenicvariantscausing pages 2-3, blakes2021pathogenicvariantscausing pages 4-5) |
| Skeletal/limb phenotype | Skeletal/digital anomalies are pervasive and include scoliosis, pectus excavatum, hindfoot deformity, finger contractures, camptodactyly, clinodactyly, Dupuytren contracture, and toe syndactyly. | Skeletal abnormalities in **6/6** initial 2017 cohort; finger/toe abnormalities **17/18** pooled; camptodactyly noted in **5/6** in one excerpt from the 2021 cohort. | Human clinical case series, 2017/2021 (wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 5-6, blakes2021pathogenicvariantscausing pages 2-3) |
| Hearing | Hearing impairment appears to be a recurrent feature in the expanded syndrome. | 2021 cohort excerpt: hearing impairment **4/6** in the new series; authors state hearing impairment is a common feature. | Human clinical case series, Eur J Hum Genet 2021 doi:10.1038/s41431-020-00766-w (blakes2021pathogenicvariantscausing pages 1-2, blakes2021pathogenicvariantscausing pages 2-3, blakes2021pathogenicvariantscausing pages 5-6) |
| Growth/development | Growth restriction and neurodevelopmental issues are common but variable. | Failure to thrive **14/18**; IUGR **10/18**; developmental delay **11/18**. 2017 series also reported failure to thrive in **5/6**. | Human clinical case series, 2017/2021 (wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 3-4) |
| Other organ involvement | Additional reported manifestations include male genital anomalies, GI anomalies, renal hypoplasia, ocular abnormalities, and occasional other malformations. | 2017: hypospadias/hypogonadism **3/4 males**, pyloric muscle thickening **1/6**, imperforate anus **1/6**. 2021 abstract notes renal hypoplasia and ocular abnormalities in affected individuals. | Human clinical reports, 2017/2021 (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 1-2) |
| 2024 structural mechanism | The best current mechanistic explanation for **E528K** is disruption of the **E528-R479 salt bridge** at the end of the **αI'-helix**, increasing force on the SH2 domain, disassembling the SH3-SH2-kinase regulatory core, and activating kinase function. | 2024 study reports Pearson correlation between activity and imatinib-induced disassembly **r=0.89**; **vmax ~202 vs ~89** for WT, **KM unchanged**. | Biochemical/structural study, eLife 2024/preprint DOI 10.1101/2023.10.04.560671 (paladini2024themolecularbasis pages 9-10, paladini2024themolecularbasis pages 11-12, paladini2024themolecularbasis pages 10-11, paladini2024themolecularbasis pages 1-2) |
| Pharmacologic implication | In vitro, mutant hyperphosphorylation can be **suppressed by imatinib**; 2024 work also supports opposing effects of type II ATP-site inhibitors versus allosteric stabilization of the myristoyl pocket/αI-helix. | 2021: imatinib abolished phosphorylation across constructs. 2024: **asciminib** reduces activity by fixating the αI-helix, whereas type II inhibitors like imatinib promote core disassembly despite ATP-site inhibition. | Functional/structural pharmacology, 2021 and 2024 (blakes2021pathogenicvariantscausing pages 1-2, blakes2021pathogenicvariantscausing pages 6-8, paladini2024themolecularbasis pages 1-2) |
| Diagnosis | Diagnosis has been established primarily by **clinical exome sequencing / whole exome sequencing** in individuals with syndromic CHD plus skeletal/dysmorphic features, followed by variant interpretation and, in research settings, functional testing. | 2017 and 2021 causal discoveries both relied on exome-based approaches; one 2022 ES study cited CHDSKM as a diagnosable syndromic entity in broader congenital anomaly testing. | Human diagnostic genomics studies, 2017/2021/2022 (wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 1-2) |
| Management considerations | Published management suggestions are supportive and surveillance-based: assess congenital heart disease, consider **aortic root diameter screening**, and obtain **audiology assessment** because aortopathy/hearing issues recur. | Explicit 2021 recommendations mention **aortic root diameter screening at diagnosis** and **audiological assessment**; no disease-specific treatment outcomes reported. | Expert interpretation within human case series, Eur J Hum Genet 2021 doi:10.1038/s41431-020-00766-w (blakes2021pathogenicvariantscausing pages 8-9) |
| Malignancy risk | Despite ABL1’s oncologic relevance, no hematologic malignancy was reported in available CHDSKM cases, though long-term surveillance has been suggested because evidence is sparse. | Reported CHDSKM cases with malignancy: **0** in available excerpts. | Human case series commentary, 2017/2021 (blakes2021pathogenicvariantscausing pages 8-9, wang2017germlinemutationsin pages 3-4) |
| Distinction from ABL1 deficiency | CHDSKM is **not** equivalent to biallelic ABL1 loss/deficiency. Available evidence supports **constitutional gain-of-function** in CHDSKM, while separate literature notes **biallelic loss-of-function ABL1 deficiency** is phenotypically distinct. | Distinction stated explicitly in 2023 diagnostic-pitfall literature; mouse **Abl1** knockout phenotypes (growth delay, cardiac hyperplasia, osteoporosis, lymphopenia, eye/head defects, perinatal lethality) differ from the human GOF syndrome. | Human genetics commentary plus model-organism evidence (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 2-3) |
| Evidence gaps | Major gaps remain: ultra-rare disease frequency/prevalence unknown; no validated biomarkers or formal diagnostic criteria; no disease-specific clinical trials; no robust natural-history, survival, QoL, penetrance, or genotype-response datasets. | Published evidence is based on roughly **18 aggregated human cases** by 2021 plus mechanistic follow-up; no interventional CHDSKM trial evidence was retrieved. | Synthesis of available human case series and lack of retrieved disease-specific trials (blakes2021pathogenicvariantscausing pages 3-4) |


*Table: This table condenses the strongest currently retrieved evidence for ABL1-related congenital heart defects and skeletal malformations syndrome, including identifiers, inheritance, variant spectrum, pooled phenotype frequencies, mechanism, and management implications. It is useful as a curation-ready summary that also flags where evidence remains sparse or absent.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Congenital heart defects and skeletal malformations syndrome.
* **Common alternatives:** ABL1-related congenital heart defects and skeletal malformations syndrome; ABL1-related malformation syndrome; ABL1 malformation syndrome; CHDSKM.
* **MONDO:** **MONDO:0060532**.
* **OMIM phenotype:** **617602**.
* **Causal gene:** **ABL1**, HGNC:**76**; Ensembl **ENSG00000097007**; protein name, ABL proto-oncogene 1, non-receptor tyrosine kinase.
* **Gene–disease validity:** Open Targets links MONDO:0060532 only to ABL1, with five evidence records ultimately anchored to PMID 28288113. (OpenTargets Search: congenital heart defects and skeletal malformations syndrome-ABL1)
* **Orphanet, MeSH, ICD-10/ICD-11:** No disease-specific identifier was established in the retrieved authoritative evidence. In clinical coding, component anomalies are therefore likely coded separately; a syndrome-specific ICD code should not be inferred.

This entry is based on **aggregated disease-level resources and published patient cohorts**, not an individual EHR. Nevertheless, almost all phenotype estimates originate from a small number of individually described patients and are vulnerable to ascertainment and publication bias.

### Scope exclusions

CHDSKM is **not** Holt–Oram syndrome/TBX5 disorder, Ellis–van Creveld syndrome, VACTERL association, Char syndrome, or a BCR::ABL1-positive hematologic neoplasm. It is also not “human ABL1 deficiency syndrome,” which results from biallelic loss-of-function alleles and represents a different allelic disorder. (wang2017germlinemutationsin pages 3-3)

## 2. Etiology, risk, and protective factors

### Primary cause

The established cause is a **constitutional, heterozygous ABL1 missense variant that increases kinase activity**. Reported disease alleles affect the SH2–kinase linker or regulatory kinase/myristoyl-pocket region, impairing normal autoinhibition. Both de novo occurrence and vertical transmission have been documented. (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 5-6, blakes2021pathogenicvariantscausing pages 6-8)

### Genetic risk factors

Supported variants include:

* NM_005157.6:c.731T>C, **p.Val244Ala**;
* c.734A>G, **p.Tyr245Cys**;
* c.1066G>A, **p.Ala356Thr**;
* c.1354G>A, **p.Ala452Thr**;
* c.1574T>C, **p.Val525Ala**;
* c.1582G>A, **p.Glu528Lys**. (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 5-6)

The recurrent p.Tyr245Cys allele occurred de novo or segregated with disease in five individuals from three families; p.Ala356Thr was de novo in the sixth original patient. Five of six newly reported individuals in 2021 had confirmed de novo variants. The studied alleles were absent from gnomAD, and the original alleles were absent from dbSNP, ESP, ExAC, and COSMIC at publication. (wang2017germlinemutationsin pages 3-3, wang2017germlinemutationsin pages 3-4, blakes2021pathogenicvariantscausing pages 6-8)

### Environmental, infectious, lifestyle, and protective factors

No environmental exposure, infection, diet, behavior, occupational factor, sex-specific exposure, protective allele, or validated modifier has been shown to cause or prevent CHDSKM. Because malformations originate during embryogenesis from a high-effect germline allele, generic congenital-heart risk factors should not be entered as CHDSKM-specific causes. No demonstrated gene–environment interaction is available.

The developmental abnormalities reported after fetal exposure to BCR–ABL inhibitors provide biological support that tightly regulated ABL activity matters in embryogenesis, but drug exposure is **not evidence of the etiology of inherited CHDSKM**. (wang2017germlinemutationsin pages 3-3)

## 3. Phenotypes

### Pooled phenotype frequencies

Among 18 individuals summarized in 2021:

* dysmorphic facies: **18/18 (100%)**;
* finger/toe abnormalities: **17/18 (94%)**;
* congenital heart disease: **14/18 (78%)**;
* failure to thrive: **14/18 (78%)**;
* developmental delay: **11/18 (61%)**;
* intrauterine growth restriction: **10/18 (56%)**;
* ear abnormalities: **9/18 (50%)**;
* palatal deformity: **9/18 (50%)**;
* microcephaly: **9/18 (50%)**. (blakes2021pathogenicvariantscausing pages 3-4)

These figures are descriptive case-series proportions, not population penetrance estimates.

### Cardiovascular

Reported manifestations include septal defects, patent ductus arteriosus, supravalvular pulmonary stenosis, and aortic-root dilatation. CHD was present in all six original patients and 14/18 pooled cases. Aortic dilatation may be progressive and warrants longitudinal measurement, whereas repaired structural defects may remain stable after intervention. Suggested terms include **HP:0001627 Congenital heart defect**, ventricular/atrial septal defect terms, patent ductus arteriosus, pulmonary stenosis, and aortic-root dilatation. (wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 8-9, blakes2021pathogenicvariantscausing pages 4-5)

### Skeletal, limb, and connective-tissue manifestations

The spectrum includes scoliosis, pectus excavatum, hindfoot deformity, finger contractures, camptodactyly, clinodactyly, Dupuytren-type contracture, toe syndactyly, and occasionally scaphocephaly. Finger/toe abnormalities occurred in 17/18 pooled cases; camptodactyly was reported in 5/6 of the expanded cohort, and scoliosis in 3/6 of the original cohort. Suggested terms include **HP:0000924 Abnormality of the skeletal system**, camptodactyly, clinodactyly, syndactyly, scoliosis, pectus excavatum, and joint contracture. (wang2017germlinemutationsin pages 1-2, wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 2-3, blakes2021pathogenicvariantscausing pages 5-6)

### Craniofacial, oral, hearing, growth, and neurologic features

Facial findings include an elongated/narrow face, long narrow nose, deep-set eyes, high-arched eyebrows, microretrognathia or small chin, thin lips, and downturned mouth. Palatal findings include a high-arched or otherwise abnormal palate and dental crowding. Suggested HPO terms include facial dysmorphism, **HP:0000347 Micrognathia**, high-arched palate, and dental crowding. (blakes2021pathogenicvariantscausing pages 5-6, blakes2021pathogenicvariantscausing pages 4-5)

Hearing impairment was present in 4/6 newly reported patients and may be conductive or mixed. Baseline and serial audiology are therefore reasonable. Suggested term: **HP:0000365 Hearing impairment**, refined to conductive or mixed hearing loss when documented. (blakes2021pathogenicvariantscausing pages 1-2, blakes2021pathogenicvariantscausing pages 2-3)

Growth manifestations begin prenatally or in infancy and include IUGR, failure to thrive, and variable short stature. Neurodevelopmental involvement ranges from apparently normal development to developmental delay; microcephaly occurred in 9/18. Suggested terms include **HP:0001511 Intrauterine growth retardation**, **HP:0001508 Failure to thrive**, **HP:0000252 Microcephaly**, and **HP:0001263 Global developmental delay**. (blakes2021pathogenicvariantscausing pages 3-4, blakes2021pathogenicvariantscausing pages 4-5)

### Other organ systems

Male genital abnormalities—hypospadias or hypogonadism—occurred in 3/4 males in the original cohort. Pyloric muscle thickening and imperforate anus each occurred in one of six. Renal hypoplasia and ocular abnormalities have also been reported, but frequencies are not robust. Suggested HPO concepts include hypospadias, hypogonadism, pyloric stenosis/thickening, imperforate anus, renal hypoplasia, and the specific ocular abnormality observed. (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 1-2)

### Quality of life

No CHDSKM-specific EQ-5D, SF-36, PROMIS, functional-status, or caregiver-burden study was found. Likely burdens arise from cardiac procedures and surveillance, feeding/growth problems, hearing impairment, developmental support needs, and orthopedic limitations, but quantitative disease-specific effects are unavailable.

## 4. Genetic and molecular information

### Gene and variant class

**ABL1** encodes a ubiquitously expressed non-receptor tyrosine kinase. CHDSKM variants are germline, heterozygous missense alleles. Available functional evidence supports **gain of function through loss of autoinhibition**, not haploinsufficiency or a dominant-negative effect. The 2021 alleles were classified as pathogenic or likely pathogenic under ACMG/AMP reasoning and were absent from gnomAD. (blakes2021pathogenicvariantscausing pages 1-2, blakes2021pathogenicvariantscausing pages 5-6)

The 2017 abstract states: “We overexpressed the mutant constructs in HEK 293T cells and observed increased tyrosine phosphorylation, suggesting increased ABL1 kinase activities associated with both the p.Tyr245Cys and p.Ala356Thr substitutions.” (wang2017germlinemutationsin pages 3-3, wang2017germlinemutationsin pages 3-4)

### Allelic disorders and cancer distinction

CHDSKM germline GOF alleles should not be conflated with the acquired **BCR::ABL1 fusion**, which drives chronic myeloid and other leukemias. No hematologic malignancy was reported in the available CHDSKM patients, although follow-up is too short and the cohort too small to establish lifetime risk. Biallelic ABL1 loss-of-function causes a separate deficiency syndrome and should not be merged with CHDSKM. (blakes2021pathogenicvariantscausing pages 8-9, wang2017germlinemutationsin pages 3-4, wang2017germlinemutationsin pages 3-3)

### Modifiers, epigenetics, and chromosome abnormalities

No validated modifier gene, syndrome-specific methylation signature, histone alteration, chromatin biomarker, recurrent copy-number variant, translocation, inversion, or aneuploidy is known. The causal lesions reported for CHDSKM are sequence-level ABL1 missense variants.

## 5. Environmental information

No toxin, radiation source, pollution exposure, maternal lifestyle factor, nutritional deficit, infection, or immune trigger has been established. CHDSKM is neither infectious nor transmissible. Environmental information should therefore be recorded as **not established**, rather than “absent,” because the cohort is too small for formal interaction studies.

## 6. Mechanism and pathophysiology

### Causal chain

1. A germline missense substitution affects the SH2–kinase linker, kinase domain, or myristoyl-binding/αI-helix regulatory region.
2. The substitution weakens intramolecular autoinhibition and favors disassembly of the SH3–SH2–kinase regulatory core.
3. ABL1 kinase activity and phosphorylation of downstream substrates, including STAT5B in experimental assays, increase.
4. Dysregulated signaling during embryonic cardiac, craniofacial, skeletal, growth, auditory, and other organ development produces congenital malformations and postnatal growth/developmental consequences. Steps 1–3 are experimentally supported; the precise lineage-specific route from kinase hyperactivity to each human malformation remains unresolved. (blakes2021pathogenicvariantscausing pages 1-2, blakes2021pathogenicvariantscausing pages 5-6, wang2017germlinemutationsin pages 3-4)

### 2024 structural advance: p.Glu528Lys

The most important recent mechanistic development is the structural/biochemical analysis of p.Glu528Lys. In wild-type ABL1, Glu528 at the end of the αI′ helix forms a salt bridge with Arg479 in the kinase-domain C-lobe, constraining αI′-helix motion and stabilizing the assembled, low-activity regulatory core. E528K breaks this bridge, increases force from the αI helix onto SH2, promotes SH3–SH2–kinase-core disassembly, and raises kinase activity. The mutant had a reported Vmax of approximately 202 versus 89 for wild type, with unchanged KM; kinase activity correlated with imatinib-induced core disassembly at **r=0.89**. [Paladini et al., *eLife*, January 2024; DOI landing page: https://doi.org/10.1101/2023.10.04.560671]. (paladini2024themolecularbasis pages 9-10, paladini2024themolecularbasis pages 11-12, paladini2024themolecularbasis pages 10-11, paladini2024themolecularbasis pages 6-9)

The paper’s abstract summarizes that E528K “strongly activates Abl by breaking a salt bridge with the KD C-lobe and thereby increasing the force onto the SH2 domain.” It also shows that the allosteric inhibitor asciminib stabilizes the αI helix and reduces this force, while type-II ATP-site inhibitors can promote regulatory-core opening even while inhibiting catalysis. This mechanistic complexity argues against simply translating leukemia dosing into children with a developmental syndrome. (paladini2024themolecularbasis pages 1-2)

### Cellular and biochemical annotation

Suggested GO annotations include **protein tyrosine kinase activity (GO:0004713)**, protein phosphorylation, signal transduction, regulation of cell adhesion and cytoskeletal organization, and developmental processes. Relevant cellular compartments include cytoplasm (**GO:0005737**), nucleus (**GO:0005634**), plasma-membrane-associated signaling complexes, and the ABL1 SH3–SH2–kinase regulatory core. STAT5B phosphorylation is an experimental readout, not a validated patient biomarker. (blakes2021pathogenicvariantscausing pages 5-6, wang2017germlinemutationsin pages 3-4)

No CHDSKM-specific metabolomic, lipidomic, proteomic, patient transcriptomic, epigenomic, spatial-transcriptomic, organoid, or single-cell dataset was established in the retrieved evidence. Candidate developmental cell types—cardiomyocytes, endocardial/valvular interstitial cells, cardiac neural-crest derivatives, chondrocytes/osteoblast-lineage cells, fibroblasts, and craniofacial mesenchyme—remain biologically plausible rather than directly demonstrated CHDSKM targets. Corresponding broad CL concepts may be used only as hypotheses, not asserted disease associations.

## 7. Anatomical structures affected

Primary organ systems are:

* **cardiovascular:** cardiac septa, ductus arteriosus, pulmonary outflow tract/valve region, and aortic root;
* **musculoskeletal/connective tissue:** axial skeleton, thoracic cage, hands, feet, joints, and tendons/fascia;
* **craniofacial/oral:** skull, mandible, palate, dentition, and external ears;
* **auditory:** middle/inner-ear pathways depending on hearing-loss type;
* **growth/neurodevelopment:** head growth and central nervous system development;
* **secondary/variable:** kidney, eye, pylorus, anorectum, and male genital tract. (wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 8-9, wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 1-2, blakes2021pathogenicvariantscausing pages 4-5)

Suggested UBERON concepts include heart, interventricular/interatrial septum, aortic root, pulmonary artery/valve, axial skeleton, hand, foot, palate, mandible, ear, kidney, eye, pylorus, anus, and male external genitalia. No consistent lateralization has been reported.

## 8. Temporal development and natural history

Onset is **prenatal/congenital**: IUGR and structural cardiac/skeletal malformations originate during embryofetal development. Failure to thrive, hearing impairment, developmental delay, microcephaly, scoliosis, contractures, and aortic-root enlargement may become more evident during childhood. (wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 8-9, blakes2021pathogenicvariantscausing pages 3-4)

There is no validated staging system. Structural malformations are generally persistent unless surgically corrected; developmental and growth trajectories are variable; scoliosis, contractures, hearing loss, and aortic dimensions merit longitudinal monitoring. No remission pattern is applicable to the underlying germline disorder. The critical causal period is embryogenesis, while postnatal opportunities concern early cardiac correction, hearing intervention, nutrition, therapy, and surveillance.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Both de novo and inherited disease have been demonstrated, including paternal transmission and multigenerational cosegregation. Expressivity is variable. The small pedigrees suggest substantial penetrance for recognizable developmental abnormalities, but numerical penetrance cannot be estimated. There is no evidence of anticipation, a founder allele, population enrichment, consanguinity dependence, or a defined carrier frequency. (wang2017germlinemutationsin pages 3-3, wang2017germlinemutationsin pages 1-2, blakes2021pathogenicvariantscausing pages 6-8)

No prevalence, incidence, geographic distribution, ethnic enrichment, sex ratio, or population-based age distribution has been measured. The published denominator—approximately 18 aggregated cases by 2021—indicates extreme rarity but is not a prevalence estimate. (blakes2021pathogenicvariantscausing pages 3-4)

## 10. Diagnosis

### Clinical recognition

Suspect CHDSKM in a patient with syndromic congenital heart disease plus digital/skeletal abnormalities, characteristic narrow facial appearance or micrognathia, growth restriction/failure to thrive, hearing impairment, palatal anomaly, or microcephaly. There are no consensus clinical diagnostic criteria or pathognomonic biochemical biomarkers.

### Baseline clinical evaluation

Recommended phenotype-driven studies include:

* echocardiography with explicit aortic-root dimensions; ECG as clinically indicated;
* skeletal survey or targeted radiographs, spinal examination, and orthopedic assessment;
* formal audiology;
* growth, nutrition, developmental, and neurologic assessment;
* renal ultrasound, ophthalmology, and GI/GU evaluation when indicated by examination;
* consideration of routine blood counts during long-term follow-up, recognizing that cancer risk is unquantified. Aortic-root and audiologic screening were specifically recommended by the expanded case series. (blakes2021pathogenicvariantscausing pages 8-9)

### Molecular testing

The preferred test is a congenital-heart/multiple-malformation panel that includes **ABL1**, trio exome sequencing, or trio genome sequencing. Exome sequencing identified the original and expanded cohorts. A positive result should establish phase and germline origin, include parental testing, and evaluate whether the missense allele falls in a known regulatory region and matches the GOF disease mechanism. (blakes2021pathogenicvariantscausing pages 1-2, wang2017germlinemutationsin pages 1-2)

Single-gene sequencing is reasonable when the phenotype is highly characteristic or a familial variant is known. Genome sequencing may detect noncoding or structural lesions missed by exome, but no CHDSKM-specific incremental yield is known. CMA is appropriate for multiple congenital anomalies when sequence testing is negative or CNV disease is suspected, but it does not reliably detect these single-nucleotide variants. Karyotype/FISH, mitochondrial testing, and repeat-expansion testing are not first-line CHDSKM assays.

A VUS should not establish diagnosis. Functional kinase/substrate-phosphorylation assays remain research tools rather than validated clinical tests.

### Differential diagnosis

Important alternatives include Holt–Oram syndrome (**TBX5**; upper-limb radial-ray defects), Ellis–van Creveld syndrome (**EVC/EVC2**; short ribs, polydactyly, disproportionate short stature), Char syndrome (**TFAP2B**; PDA with characteristic facies and fifth-finger anomalies), VACTERL association, Kabuki syndrome, RASopathies, connective-tissue aortopathies, and chromosomal/CNV syndromes. Distinction requires detailed limb patterning, associated-organ phenotype, inheritance, and molecular testing. CHDSKM is especially supported by an appropriate heterozygous GOF-region **ABL1** variant.

### Screening

There is no population newborn or carrier-screening program. Cascade testing is indicated after a familial pathogenic variant is identified. Prenatal diagnosis by CVS/amniocentesis and preimplantation genetic testing for monogenic disease are technically possible for a known familial variant. Fetal echocardiography and detailed ultrasound assess manifestations but cannot exclude the disorder.

## 11. Outcome and prognosis

No 5- or 10-year survival rate, life-expectancy estimate, mortality rate, prognostic score, or validated prognostic biomarker is available. Prognosis is probably driven chiefly by the type and severity of congenital heart disease, aortic involvement, feeding/growth difficulties, hearing impairment, developmental needs, and orthopedic complications. This is an inference from the phenotype, not a measured outcome model.

No malignancy was reported in the available patients, but the absence of events in a very small, mostly young cohort does not prove normal lifetime cancer risk. Long-term registries should capture aortic dimensions, cardiovascular procedures, hearing trajectory, growth, neurodevelopment, mobility, malignancy, and patient-reported quality of life. (blakes2021pathogenicvariantscausing pages 8-9, wang2017germlinemutationsin pages 3-4)

## 12. Treatment

### Current real-world management

There is no approved disease-modifying treatment. Care is individualized and multidisciplinary:

* pediatric/adult congenital cardiology for defect-specific catheter or surgical management and serial aortic imaging;
* orthopedics, physiotherapy, and occupational therapy for scoliosis, foot deformity, contractures, and hand function;
* audiology, hearing aids, or ENT intervention as appropriate;
* nutrition and gastroenterology for feeding difficulty/failure to thrive;
* developmental pediatrics with physical, occupational, and speech/language therapy;
* renal, ophthalmologic, GI, and urologic management according to manifestations.

Suggested NCIT intervention concepts include cardiac surgical procedure, echocardiography, hearing aid, physical therapy, occupational therapy, speech therapy, nutritional support, orthopedic surgery, and genetic counseling; exact NCIT identifiers should be resolved against the current NCIt release.

### ABL inhibitors: experimental only

In HEK293T assays, imatinib suppressed increased mutant ABL1-substrate phosphorylation and abolished phosphorylation across tested constructs, demonstrating pharmacologic tractability. This is **preclinical evidence**, not proof of clinical benefit, dose, timing, or safety in CHDSKM. (blakes2021pathogenicvariantscausing pages 1-2, blakes2021pathogenicvariantscausing pages 6-8)

The 2024 structural work suggests that allosteric myristoyl-pocket inhibition by asciminib stabilizes the αI-helix, whereas type-II inhibitors such as imatinib have more complex effects on regulatory-core assembly. Moreover, inhibiting ABL during development may itself be teratogenic. Consequently, imatinib, asciminib, or other tyrosine-kinase inhibitors should not be considered routine CHDSKM treatment outside a rigorously justified research protocol. (wang2017germlinemutationsin pages 3-3, paladini2024themolecularbasis pages 1-2)

No CHDSKM-specific interventional trial or NCT identifier was found. Retrieved ABL1 inhibitor trials concerned BCR::ABL1-positive leukemia and are not applicable to this congenital syndrome.

## 13. Prevention

Primary prevention of a de novo pathogenic variant is not currently possible. For an affected heterozygous parent, each pregnancy has an expected **50% transmission probability**, although severity cannot be predicted reliably because expressivity is variable. Genetic counseling, cascade testing, prenatal molecular diagnosis, fetal echocardiography, and PGT-M are the principal reproductive-risk interventions. (wang2017germlinemutationsin pages 3-3, wang2017germlinemutationsin pages 1-2)

Secondary prevention consists of early molecular diagnosis and prompt detection of cardiac, aortic, auditory, growth, and developmental involvement. Tertiary prevention includes timely repair of hemodynamically important defects, serial aortic surveillance, hearing support, nutritional intervention, rehabilitation, and orthopedic management. Vaccination, antimicrobial prophylaxis, or lifestyle modification does not prevent the genetic syndrome; ordinary congenital-heart guidelines may still govern immunization and procedure-specific endocarditis prophylaxis.

## 14. Other species and natural disease

No naturally occurring veterinary CHDSKM caused by an orthologous ABL1 gain-of-function allele was established, and there is no zoonotic or cross-species transmission. The relevant ortholog in mouse is **Abl1**; orthologs are broadly conserved across vertebrates. No breed-specific VBO annotation can presently be supported.

## 15. Model organisms and experimental systems

### Mouse

Abl1-null mice provide evidence that ABL1 is essential in development, with reported growth delay, cardiac hyperplasia, osteoporosis, eye/head defects, lymphopenia, thymic/splenic abnormalities, and perinatal lethality. These are loss-of-function models and do **not** faithfully reproduce the human heterozygous gain-of-function syndrome; they establish developmental importance rather than allele-specific phenocopy. (wang2017germlinemutationsin pages 3-3, blakes2021pathogenicvariantscausing pages 2-3)

A disease-faithful model would require knock-in of recurrent human alleles such as p.Tyr245Cys or p.Glu528Lys, ideally conditionally in cardiac mesoderm, neural crest, endocardial/valvular, and skeletal mesenchymal lineages. No validated knock-in animal model was established in the retrieved literature.

### Cellular and biochemical systems

HEK293T overexpression assays showed increased global phosphotyrosine and STAT5/STAT5B phosphorylation for multiple variants and suppression by imatinib. These assays directly support kinase gain of function but cannot reproduce embryonic tissue patterning. (blakes2021pathogenicvariantscausing pages 5-6, wang2017germlinemutationsin pages 3-4)

Purified-protein, NMR, and structural/biochemical studies of E528K defined the E528–R479 salt bridge, αI-helix mechanics, regulatory-core disassembly, and increased catalytic output. These provide strong molecular evidence but not organism-level developmental validation. (paladini2024themolecularbasis pages 9-10, paladini2024themolecularbasis pages 10-11, paladini2024themolecularbasis pages 6-9)

## Evidence limitations and curation recommendations

The strongest evidence consists of the 2017 discovery study, the 2021 six-patient expansion with pooled 18-case phenotyping, and the 2024 structural study. Recent 2023–2024 case reports suggest continued phenotypic expansion, but their full text was not available in the retrieved evidence; novel features such as additional cardiac findings or Dandy–Walker malformation should therefore not be treated as established frequencies here.

For knowledge-base curation, annotate CHDSKM as an **autosomal-dominant, germline ABL1 gain-of-function developmental disorder** with congenital onset. Preserve patient-level denominators, distinguish observed findings from inferred mechanisms, and keep ABL1 deficiency and BCR::ABL1 neoplasia as separate disease entities. Epidemiology, penetrance, survival, quality of life, modifiers, omics signatures, validated biomarkers, and disease-specific therapeutic outcomes should be recorded as unknown rather than extrapolated.

References

1. (wang2017germlinemutationsin pages 3-3): Xia Wang, Wu-Lin Charng, Chun-An Chen, Jill A Rosenfeld, Aisha Al Shamsi, Lihadh Al-Gazali, Marianne McGuire, Nicholas Ah Mew, Georgianne L Arnold, Chunjing Qu, Yan Ding, Donna M Muzny, Richard A Gibbs, Christine M Eng, Magdalena Walkiewicz, Fan Xia, Sharon E Plon, James R Lupski, Christian P Schaaf, and Yaping Yang. Germline mutations in abl1 cause an autosomal dominant syndrome characterized by congenital heart defects and skeletal malformations. Mar 2017. URL: https://doi.org/10.1038/ng.3815, doi:10.1038/ng.3815. This article has 73 citations and is from a highest quality peer-reviewed journal.

2. (blakes2021pathogenicvariantscausing pages 3-4): Alexander J. M. Blakes, Emily Gaul, Wayne Lam, Nora Shannon, Karen M. Knapp, Louise S. Bicknell, Meremaihi R. Jackson, Emma M. Wade, Stephen Robertson, Susan M. White, Raoul Heller, Andrew Chase, Diana Baralle, and Andrew G. L. Douglas. Pathogenic variants causing abl1 malformation syndrome cluster in a myristoyl-binding pocket and increase tyrosine kinase activity. European Journal of Human Genetics, 29:593-603, Nov 2021. URL: https://doi.org/10.1038/s41431-020-00766-w, doi:10.1038/s41431-020-00766-w. This article has 22 citations and is from a domain leading peer-reviewed journal.

3. (wang2017germlinemutationsin pages 1-2): Xia Wang, Wu-Lin Charng, Chun-An Chen, Jill A Rosenfeld, Aisha Al Shamsi, Lihadh Al-Gazali, Marianne McGuire, Nicholas Ah Mew, Georgianne L Arnold, Chunjing Qu, Yan Ding, Donna M Muzny, Richard A Gibbs, Christine M Eng, Magdalena Walkiewicz, Fan Xia, Sharon E Plon, James R Lupski, Christian P Schaaf, and Yaping Yang. Germline mutations in abl1 cause an autosomal dominant syndrome characterized by congenital heart defects and skeletal malformations. Mar 2017. URL: https://doi.org/10.1038/ng.3815, doi:10.1038/ng.3815. This article has 73 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: congenital heart defects and skeletal malformations syndrome-ABL1): Open Targets Query (congenital heart defects and skeletal malformations syndrome-ABL1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (blakes2021pathogenicvariantscausing pages 6-8): Alexander J. M. Blakes, Emily Gaul, Wayne Lam, Nora Shannon, Karen M. Knapp, Louise S. Bicknell, Meremaihi R. Jackson, Emma M. Wade, Stephen Robertson, Susan M. White, Raoul Heller, Andrew Chase, Diana Baralle, and Andrew G. L. Douglas. Pathogenic variants causing abl1 malformation syndrome cluster in a myristoyl-binding pocket and increase tyrosine kinase activity. European Journal of Human Genetics, 29:593-603, Nov 2021. URL: https://doi.org/10.1038/s41431-020-00766-w, doi:10.1038/s41431-020-00766-w. This article has 22 citations and is from a domain leading peer-reviewed journal.

6. (blakes2021pathogenicvariantscausing pages 1-2): Alexander J. M. Blakes, Emily Gaul, Wayne Lam, Nora Shannon, Karen M. Knapp, Louise S. Bicknell, Meremaihi R. Jackson, Emma M. Wade, Stephen Robertson, Susan M. White, Raoul Heller, Andrew Chase, Diana Baralle, and Andrew G. L. Douglas. Pathogenic variants causing abl1 malformation syndrome cluster in a myristoyl-binding pocket and increase tyrosine kinase activity. European Journal of Human Genetics, 29:593-603, Nov 2021. URL: https://doi.org/10.1038/s41431-020-00766-w, doi:10.1038/s41431-020-00766-w. This article has 22 citations and is from a domain leading peer-reviewed journal.

7. (wang2017germlinemutationsin pages 3-4): Xia Wang, Wu-Lin Charng, Chun-An Chen, Jill A Rosenfeld, Aisha Al Shamsi, Lihadh Al-Gazali, Marianne McGuire, Nicholas Ah Mew, Georgianne L Arnold, Chunjing Qu, Yan Ding, Donna M Muzny, Richard A Gibbs, Christine M Eng, Magdalena Walkiewicz, Fan Xia, Sharon E Plon, James R Lupski, Christian P Schaaf, and Yaping Yang. Germline mutations in abl1 cause an autosomal dominant syndrome characterized by congenital heart defects and skeletal malformations. Mar 2017. URL: https://doi.org/10.1038/ng.3815, doi:10.1038/ng.3815. This article has 73 citations and is from a highest quality peer-reviewed journal.

8. (paladini2024themolecularbasis pages 9-10): Johannes Paladini, Annalena Maier, Judith Maria Habazettl, Ines Hertel, Rajesh Sonti, and Stephan Grzesiek. The molecular basis of abelson kinase regulation by its αi-helix. eLife, Jan 2024. URL: https://doi.org/10.1101/2023.10.04.560671, doi:10.1101/2023.10.04.560671. This article has 7 citations and is from a domain leading peer-reviewed journal.

9. (paladini2024themolecularbasis pages 6-9): Johannes Paladini, Annalena Maier, Judith Maria Habazettl, Ines Hertel, Rajesh Sonti, and Stephan Grzesiek. The molecular basis of abelson kinase regulation by its αi-helix. eLife, Jan 2024. URL: https://doi.org/10.1101/2023.10.04.560671, doi:10.1101/2023.10.04.560671. This article has 7 citations and is from a domain leading peer-reviewed journal.

10. (blakes2021pathogenicvariantscausing pages 5-6): Alexander J. M. Blakes, Emily Gaul, Wayne Lam, Nora Shannon, Karen M. Knapp, Louise S. Bicknell, Meremaihi R. Jackson, Emma M. Wade, Stephen Robertson, Susan M. White, Raoul Heller, Andrew Chase, Diana Baralle, and Andrew G. L. Douglas. Pathogenic variants causing abl1 malformation syndrome cluster in a myristoyl-binding pocket and increase tyrosine kinase activity. European Journal of Human Genetics, 29:593-603, Nov 2021. URL: https://doi.org/10.1038/s41431-020-00766-w, doi:10.1038/s41431-020-00766-w. This article has 22 citations and is from a domain leading peer-reviewed journal.

11. (blakes2021pathogenicvariantscausing pages 8-9): Alexander J. M. Blakes, Emily Gaul, Wayne Lam, Nora Shannon, Karen M. Knapp, Louise S. Bicknell, Meremaihi R. Jackson, Emma M. Wade, Stephen Robertson, Susan M. White, Raoul Heller, Andrew Chase, Diana Baralle, and Andrew G. L. Douglas. Pathogenic variants causing abl1 malformation syndrome cluster in a myristoyl-binding pocket and increase tyrosine kinase activity. European Journal of Human Genetics, 29:593-603, Nov 2021. URL: https://doi.org/10.1038/s41431-020-00766-w, doi:10.1038/s41431-020-00766-w. This article has 22 citations and is from a domain leading peer-reviewed journal.

12. (blakes2021pathogenicvariantscausing pages 4-5): Alexander J. M. Blakes, Emily Gaul, Wayne Lam, Nora Shannon, Karen M. Knapp, Louise S. Bicknell, Meremaihi R. Jackson, Emma M. Wade, Stephen Robertson, Susan M. White, Raoul Heller, Andrew Chase, Diana Baralle, and Andrew G. L. Douglas. Pathogenic variants causing abl1 malformation syndrome cluster in a myristoyl-binding pocket and increase tyrosine kinase activity. European Journal of Human Genetics, 29:593-603, Nov 2021. URL: https://doi.org/10.1038/s41431-020-00766-w, doi:10.1038/s41431-020-00766-w. This article has 22 citations and is from a domain leading peer-reviewed journal.

13. (paladini2024themolecularbasis pages 11-12): Johannes Paladini, Annalena Maier, Judith Maria Habazettl, Ines Hertel, Rajesh Sonti, and Stephan Grzesiek. The molecular basis of abelson kinase regulation by its αi-helix. eLife, Jan 2024. URL: https://doi.org/10.1101/2023.10.04.560671, doi:10.1101/2023.10.04.560671. This article has 7 citations and is from a domain leading peer-reviewed journal.

14. (paladini2024themolecularbasis pages 10-11): Johannes Paladini, Annalena Maier, Judith Maria Habazettl, Ines Hertel, Rajesh Sonti, and Stephan Grzesiek. The molecular basis of abelson kinase regulation by its αi-helix. eLife, Jan 2024. URL: https://doi.org/10.1101/2023.10.04.560671, doi:10.1101/2023.10.04.560671. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (blakes2021pathogenicvariantscausing pages 2-3): Alexander J. M. Blakes, Emily Gaul, Wayne Lam, Nora Shannon, Karen M. Knapp, Louise S. Bicknell, Meremaihi R. Jackson, Emma M. Wade, Stephen Robertson, Susan M. White, Raoul Heller, Andrew Chase, Diana Baralle, and Andrew G. L. Douglas. Pathogenic variants causing abl1 malformation syndrome cluster in a myristoyl-binding pocket and increase tyrosine kinase activity. European Journal of Human Genetics, 29:593-603, Nov 2021. URL: https://doi.org/10.1038/s41431-020-00766-w, doi:10.1038/s41431-020-00766-w. This article has 22 citations and is from a domain leading peer-reviewed journal.

16. (paladini2024themolecularbasis pages 1-2): Johannes Paladini, Annalena Maier, Judith Maria Habazettl, Ines Hertel, Rajesh Sonti, and Stephan Grzesiek. The molecular basis of abelson kinase regulation by its αi-helix. eLife, Jan 2024. URL: https://doi.org/10.1101/2023.10.04.560671, doi:10.1101/2023.10.04.560671. This article has 7 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Congenital_Heart_Defects_and_Skeletal_Malformations_Syndrome-deep-research-falcon_artifacts/artifact-00.md)