---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T01:14:41.433384'
end_time: '2026-07-31T01:24:55.999138'
duration_seconds: 614.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 4B
  mondo_id: MONDO:0013931,PEX6-related,OMIM:614863,also-called-SCAR3/SCABD1,non-classic-Zellweger-spectrum
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peroxisome_Biogenesis_Disorder_4B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 4B
- **MONDO ID:** MONDO:0013931,PEX6-related,OMIM:614863,also-called-SCAR3/SCABD1,non-classic-Zellweger-spectrum (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 4B** covering all of the
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
- **Disease Name:** Peroxisome Biogenesis Disorder 4B
- **MONDO ID:** MONDO:0013931,PEX6-related,OMIM:614863,also-called-SCAR3/SCABD1,non-classic-Zellweger-spectrum (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 4B** covering all of the
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


# Peroxisome Biogenesis Disorder 4B: comprehensive disease-characteristics report

## Executive summary and entity-resolution warning

**Peroxisome biogenesis disorder 4B (PBD4B)** is an autosomal-recessive, **PEX6-related Zellweger-spectrum disorder (ZSD)**. Residual PEX6 activity produces a continuum from childhood/adult neurologic disease to the very mild **Heimler syndrome 2** phenotype; near-complete loss of function produces severe neonatal Zellweger disease. Open Targets maps **MONDO:0013931** specifically to **PEX6** (Ensembl ENSG00000124587) with a disease–target score of 0.809. (OpenTargets Search: peroxisome biogenesis disorder 4B-PEX6)

The supplied synonym string requires correction. **“SCAR3/SCABD1” is not supported as a synonym of PEX6-related PBD4B** in the retrieved disease-gene or clinical evidence and should not be loaded as an exact synonym. “Non-classic Zellweger-spectrum disorder,” “mild PEX6-related ZSD,” and “Heimler syndrome 2” are appropriate overlapping labels, although Heimler syndrome describes the mild sensory-dental end of the spectrum rather than every PBD4B patient. (OpenTargets Search: peroxisome biogenesis disorder 4B-PEX6, munozpujol2022diagnosticodysseyin pages 1-2)

The following table provides a compact curation summary; details and qualifications follow.

| domain | high-confidence finding | evidence type | key quantitative/example data | ontology suggestions | evidence limitations |
|---|---|---|---|---|---|
| Identity / nomenclature | Peroxisome biogenesis disorder 4B is a PEX6-related autosomal recessive peroxisome biogenesis disorder within the Zellweger spectrum; mild presentations overlap with Heimler syndrome 2 / non-classic ZSD. SCAR3/SCABD1 is **not supported** as a synonym by retrieved disease-gene evidence and appears to be conflated nomenclature. (OpenTargets Search: peroxisome biogenesis disorder 4B-PEX6, munozpujol2022diagnosticodysseyin pages 1-2, slaton2023zellweger’ssyndromewith pages 1-2) | Disease-gene database + human clinical/review | Open Targets maps MONDO:0013931 to **PEX6** with evidence from multiple publications; 2022 review states ZSD ranges from severe Zellweger syndrome to mild Heimler syndrome. (OpenTargets Search: peroxisome biogenesis disorder 4B-PEX6, munozpujol2022diagnosticodysseyin pages 1-2) | MONDO:0013931; MONDO: Zellweger spectrum disorder; HP:0001417 | MONDO/OMIM cross-labeling for severe vs mild PEX6 entities is not fully resolved in retrieved sources; no direct source supporting SCAR3/SCABD1 was found. |
| Inheritance / gene | Cause is biallelic pathogenic variation in **PEX6**, encoding a peroxisomal AAA-ATPase complex component required for peroxisome biogenesis and matrix-protein import. (OpenTargets Search: peroxisome biogenesis disorder 4B-PEX6, ahangari2026unravelingpex6insights pages 2-3, biase2020laboratorydiagnosisof pages 1-2) | Human disease-gene evidence + ACMG standard + review | Autosomal recessive; PEX6 acts with PEX1 and PEX26 in the AAA complex. Example severe neonatal variant: **c.1409G>C (p.Gly470Ala)** homozygous in 3 Mixteco infants. (slaton2023zellweger’ssyndromewith pages 1-2, slaton2023zellweger’ssyndromewith pages 3-4) | HGNC:8856; NCBI Gene: PEX6; GO:0016560 protein import into peroxisome matrix, GO:0005777 peroxisome | Most detailed mechanistic data are often shared across AAA-complex genes, not PEX6-only. |
| Severe phenotype | Severe neonatal PEX6 disease presents with hypotonia, craniofacial/ocular anomalies, abnormal liver tests, VLCFA abnormalities, feeding/respiratory problems, and early death. (slaton2023zellweger’ssyndromewith pages 1-2, slaton2023zellweger’ssyndromewith pages 2-3, slaton2023zellweger’ssyndromewith pages 3-4) | PEX6-specific human case series (2023) | 3 Mixteco neonates with homozygous **p.Gly470Ala**: all had elevated C26:0 (7.17–8.27 µmol/L), high C26/C22 ratios (0.424–0.592), hypotonia; 2/3 died by ~3–6 months; all had abnormal hepatic panels. (slaton2023zellweger’ssyndromewith pages 2-3, slaton2023zellweger’ssyndromewith pages 3-4) | HP:0001252 hypotonia; HP:0001508 failure to thrive; HP:0002240 hepatomegaly; HP:0000365 hearing impairment; HP:0000478 abnormality of the eye | Very small cohort; founder-effect population; not representative of full PEX6 spectrum. |
| Mild / non-classic phenotype | Mild ZSD / Heimler-like PEX6 disease can present with sensorineural hearing loss, enamel defects, retinal dystrophy, and sometimes late or adult diagnosis. (munozpujol2022diagnosticodysseyin pages 1-2, ahangari2026unravelingpex6insights pages 2-3) | Human clinical review / synthesis | 2022 review: mild phenotypes may show hearing loss, amelogenesis imperfecta, retinal dystrophy and only slight/normal biochemical abnormalities; adult diagnostic odyssey highlighted for mild ZSD. (munozpujol2022diagnosticodysseyin pages 1-2) | HP:0000365; HP:0000548 retinitis pigmentosa; HP:0000674 dental enamel abnormality | Retrieved mild examples were often PEX1-centered or review-level, not primary PEX6 cohorts. |
| Biochemical diagnostics | First-line testing relies on peroxisomal metabolites, especially VLCFAs; supportive markers include plasmalogens, phytanic/pristanic acid, bile-acid intermediates, pipecolic acid. (biase2020laboratorydiagnosisof pages 1-2, klouwer2021autophagyinhibitorsdo pages 1-2) | ACMG technical standard + disease reviews | ACMG: current approach relies heavily on biochemical tests measuring plasma very-long-chain and branched-chain fatty acids and red-cell plasmalogens; trial protocols also monitor phytanic acid and plasmalogens. (biase2020laboratorydiagnosisof pages 1-2, NCT03856866 chunk 1) | CHEBI: very long-chain fatty acid; CHEBI: phytanic acid; CHEBI: pristanic acid; LOINC concept suggestions for VLCFA/plasmalogen assays | Biomarker profile is generic to peroxisomal disorders and not specific to PEX6. |
| Diagnostic caveat | Normal plasma VLCFA does **not** exclude PEX6-related disease; integrated biochemical + molecular testing is needed, especially in mild phenotypes. (ahangari2026unravelingpex6insights pages 2-3, ahangari2026unravelingpex6insights pages 3-5, ahangari2026unravelingpex6insights pages 1-2) | PEX6-focused review/synthesis | Example cited PEX6 case: homozygous **c.1992G>C (p.Glu664Asp)** with developmental delay, dysmorphism, hearing loss, but **normal plasma VLCFA**. (ahangari2026unravelingpex6insights pages 2-3, ahangari2026unravelingpex6insights pages 3-5) | MAXO: genetic testing; GO:0005777 peroxisome | Evidence comes from review-level summary of individual cases, not a large cohort. |
| Mechanism | PEX6 forms, with PEX1 and PEX26, the peroxisomal AAA-ATPase complex that recycles ubiquitinated **PEX5** from the peroxisomal membrane; dysfunction leads to impaired matrix-protein import and increased pexophagy. (biase2020laboratorydiagnosisof pages 1-2, law2017theperoxisomalaaa pages 1-6, klouwer2021autophagyinhibitorsdo pages 1-2) | Primary cell biology + ACMG background | Law 2017: loss of AAA-complex function causes accumulation of ubiquitinated PEX5 and signals pexophagy; Klouwer 2021 describes impaired PEX1/PEX6-complex function and defective matrix-protein import. (law2017theperoxisomalaaa pages 1-6, klouwer2021autophagyinhibitorsdo pages 1-2) | GO:0016558 protein import into peroxisome matrix; GO:0000425 autophagy of peroxisome; GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process; CL:0000057 fibroblast | Core mechanistic experiments largely used PEX1/AAA-complex models rather than PEX6-mutant primary datasets. |
| Downstream metabolic consequences | Peroxisome dysfunction causes accumulation of VLCFAs and other substrates plus reduced plasmalogens, mature bile acids, and DHA, affecting liver, nervous system, retina, and hearing. (biase2020laboratorydiagnosisof pages 1-2, klouwer2021autophagyinhibitorsdo pages 1-2, ahangari2026unravelingpex6insights pages 2-3) | ACMG standard + review + case evidence | ACMG lists increased VLCFAs, pristanic acid and bile-acid precursors, and decreased plasmalogens, mature bile acids and DHA in PBD-ZSD. (klouwer2021autophagyinhibitorsdo pages 1-2, biase2020laboratorydiagnosisof pages 1-2) | UBERON:0002107 liver; UBERON:0000955 brain; UBERON:0000966 retina; UBERON:0001723 cochlea; HP:0001290 developmental delay | Not all abnormalities are present in every mild PEX6 patient. |
| Epidemiology / founder effect | ZSD is rare; a 2023 PEX6-specific report suggests a possible Mixteco founder effect for **p.Gly470Ala**. (slaton2023zellweger’ssyndromewith pages 1-2, slaton2023zellweger’ssyndromewith pages 6-6) | Human case series / epidemiologic observation | Report states ZSD incidence ~**1/50,000** newborns in the U.S.; all 3 cases were born to Mixteco mothers and shared homozygous **PEX6 c.1409G>C (p.Gly470Ala)**. (slaton2023zellweger’ssyndromewith pages 1-2) | HP:0034341 founder effect (concept suggestion) | Founder-effect inference is preliminary and based on 3 cases plus cited prior literature. |
| Prognosis | Prognosis is highly variable: neonatal presentations often have survival <1 year, whereas milder ZSD can persist into adolescence/adulthood. (slaton2023zellweger’ssyndromewith pages 1-2, munozpujol2022diagnosticodysseyin pages 1-2, ahangari2026unravelingpex6insights pages 1-2) | Human case series + clinical reviews | 2023 PEX6 neonatal report: 2/3 infants died before 1 year; review notes some ZSD patients survive into adulthood, especially mild forms. (slaton2023zellweger’ssyndromewith pages 1-2, munozpujol2022diagnosticodysseyin pages 1-2) | HP:0003819 neonatal onset; HP:0011463 childhood onset; HP:0003581 adult onset | No PEX6-specific longitudinal natural-history cohort with survival estimates was retrieved. |
| Supportive treatment | No curative therapy is established; management is supportive and organ-directed, including nutritional, hepatic, audiologic, ophthalmologic, developmental, and palliative care. (munozpujol2022diagnosticodysseyin pages 1-2, slaton2023zellweger’ssyndromewith pages 1-2) | Clinical review + human case reports | 2023 case report notes no curative treatment; neonatal patients received comfort-focused care; ZSD reviews emphasize supportive care across systems. (slaton2023zellweger’ssyndromewith pages 1-2, munozpujol2022diagnosticodysseyin pages 1-2) | MAXO: supportive care; MAXO: hearing aid/cochlear management; MAXO: ophthalmologic monitoring; MAXO: physical therapy | PEX6-specific treatment guidelines were not separately retrieved from generic ZSD management guidance. |
| Cholic acid / liver-directed therapy | Cholic acid is used in ZSD liver disease contexts, but evidence is **generic ZSD**, not PEX6-specific, and benefit may be incomplete. (slaton2023zellweger’ssyndromewith pages 1-2) | Review-level mention in retrieved PEX6 report | 2023 report cites “promising” prior study for cholic acid; not evaluated in the reported PEX6 neonatal series. (slaton2023zellweger’ssyndromewith pages 1-2) | CHEBI: cholic acid; MAXO: bile acid replacement | No direct PEX6-stratified efficacy data retrieved here. |
| Experimental therapy / hydroxychloroquine | Hydroxychloroquine was clinically tested for PEX1/PEX6/PEX26 PBD-ZSD eligibility, but in-vitro evidence does **not** support autophagy inhibitors as effective restoration therapy. (NCT03856866 chunk 1, klouwer2021autophagyinhibitorsdo pages 1-2) | Phase II clinical trial registry + in-vitro study | **NCT03856866**: randomized double-blind crossover N-of-1 HCQ trial, enrollment **3**, included **PEX6** patients with abnormal VLCFAs; Klouwer 2021 found no improvement and worsening of peroxisomal functions with HCQ/chloroquine/3-MA. (NCT03856866 chunk 1, klouwer2021autophagyinhibitorsdo pages 1-2) | MAXO: hydroxychloroquine administration; GO:0000425 pexophagy | Trial record available, but no retrieved peer-reviewed clinical outcomes by genotype; lab evidence mainly PEX1-G843D cells. |
| Other trials / real-world implementation | Active observational infrastructure exists for natural history, caregiver QoL, and retinopathy, but not proven disease-modifying PEX6 therapy. (NCT03440905 chunk 1, NCT01668186 chunk 1) | ClinicalTrials.gov observational studies | **NCT01668186** natural history: enrollment **244**, recruiting; **NCT03440905** caregiver QoL: **92** completed; **NCT06190626** retinopathy study: **30** recruiting; **NCT03115086** Cholbam registry: **55** active-not-recruiting. (NCT01668186 chunk 1, NCT03440905 chunk 1) | MAXO: natural history study participation; MAXO: retinal monitoring | Most studies are pan-ZSD/PBD and not PEX6-specific. |
| Model systems | Mechanistic understanding comes from patient fibroblasts and generic ZSD animal models (mouse, zebrafish, Drosophila), with strong relevance to AAA-complex/peroxisome biology. (law2017theperoxisomalaaa pages 1-6, klouwer2021autophagyinhibitorsdo pages 1-2) | In vitro + animal model/review | Patient-cell and fibroblast work support AAA-complex/pexophagy model; Drosophila and zebrafish peroxisome models show conserved import, lipid, and neurodevelopmental phenotypes. (law2017theperoxisomalaaa pages 1-6, klouwer2021autophagyinhibitorsdo pages 1-2) | CL:0000057 fibroblast; NCBITaxon:10090 mouse; NCBITaxon:7955 zebrafish; NCBITaxon:7227 Drosophila | Retrieved animal models were mostly PEX1 or non-PEX6 peroxisome models, so disease recapitulation is indirect for PEX6-PBD4B. |


*Table: This table condenses high-confidence knowledge-base facts for PEX6-related peroxisome biogenesis disorder 4B, separating PEX6-specific findings from broader Zellweger spectrum evidence. It is useful for rapid curation of nomenclature, phenotypes, diagnostics, mechanism, prognosis, treatment status, and model-system evidence.*

## 1. Disease information

### Definition

PBD4B is a congenital disorder of peroxisome assembly caused by biallelic pathogenic variants in **PEX6**. The resulting deficiency affects multiple peroxisomal pathways rather than one enzyme. ZSD is therefore a clinical and biochemical continuum: severe neonatal disease includes profound hypotonia, seizures, feeding and respiratory failure, liver dysfunction, sensory impairment and dysmorphism; attenuated disease may present with hearing loss, retinal dystrophy, enamel abnormalities, ataxia, neuropathy or leukodystrophy in childhood or adulthood. The mildest recognized presentation, Heimler syndrome, is dominated by sensorineural hearing loss, amelogenesis imperfecta and retinal dystrophy. (munozpujol2022diagnosticodysseyin pages 1-2, ahangari2026unravelingpex6insights pages 2-3)

A useful published definition is: **“Peroxisomal biogenesis disorders (PBDs) are a heterogeneous group of genetic diseases. Multiple peroxisomal pathways are impaired.”** The same report emphasizes that presentation ranges from “severe, lethal multisystemic disorders to milder, late-onset disease.” (munozpujol2022diagnosticodysseyin pages 1-2)

### Identifiers and names

- **MONDO:** MONDO:0013931, peroxisome biogenesis disorder 4B.
- **OMIM:** 614863 is the supplied and conventionally used PBD4B identifier; severe PEX6-related PBD4A is separately represented as OMIM 614862. The phenotypes are allelic and clinically continuous.
- **Gene:** PEX6, peroxisomal biogenesis factor 6; Ensembl ENSG00000124587. (OpenTargets Search: peroxisome biogenesis disorder 4B-PEX6)
- **MeSH:** Zellweger syndrome, **D015211**; Peroxisome Biogenesis Disorders, **C536664**, as represented in ClinicalTrials.gov indexing. (NCT03856866 chunk 1)
- **Orphanet:** ZSD is generally indexed at spectrum level; a PBD4B-specific Orphanet identifier was not verified in the retrieved material.
- **ICD-10/ICD-11:** no uniquely verified PBD4B code was found. Coding generally falls under disorders of peroxisomal function/other specified metabolic disorders; local terminology should be checked before database ingestion.
- **Supported synonyms:** PEX6-related peroxisome biogenesis disorder; PEX6-related Zellweger-spectrum disorder; mild/non-classic ZSD due to PEX6; Heimler syndrome 2 for the mild sensory-dental phenotype.
- **Not an exact synonym:** SCAR3/SCABD1.

Evidence in this report is primarily **aggregated disease-level literature and registries**, supplemented by individual case reports and small cohorts. It is not derived from an EHR population.

## 2. Etiology

### Causal factor

The cause is **germline biallelic pathogenic PEX6 variation**. PEX6 encodes an AAA-family ATPase that complexes with PEX1 and is anchored by PEX26. The complex extracts ubiquitinated PEX5 from the peroxisomal membrane after delivery of PTS1-containing matrix proteins. Loss of this activity disrupts matrix-protein import and peroxisome quality control. (biase2020laboratorydiagnosisof pages 1-2, law2017theperoxisomalaaa pages 1-6)

### Genetic risk and genotype–phenotype relationship

- Two pathogenic alleles are ordinarily required. Null/truncating alleles or severely disruptive missense alleles tend toward neonatal disease; hypomorphic missense/splice alleles retaining activity tend toward PBD4B, Heimler-like or adult-onset disease. This is a tendency, not a deterministic rule. (ahangari2026unravelingpex6insights pages 2-3, ahangari2026unravelingpex6insights pages 1-2)
- A 2023 PEX6-specific series identified homozygous **NM_000287.4:c.1409G>C, p.(Gly470Ala)** in three Mixteco neonates with severe ZSD. All had hypotonia, liver abnormalities and marked VLCFA abnormalities; two were known to die by approximately three to six months. (slaton2023zellweger’ssyndromewith pages 3-4, slaton2023zellweger’ssyndromewith pages 2-3, slaton2023zellweger’ssyndromewith pages 1-2)
- A reported homozygous **c.1992G>C, p.(Glu664Asp)** case had developmental delay, dysmorphism and hearing loss despite normal plasma VLCFAs, illustrating that genotype can be more informative than a single biochemical screen. (ahangari2026unravelingpex6insights pages 2-3, ahangari2026unravelingpex6insights pages 3-5)
- PEX6 can also phenocopy **Perrault syndrome**, with hearing loss and ovarian dysfunction/neurologic disease. Genomic work identified PEX6 variants including p.(Leu124Pro) and p.(Arg786Trp), broadening ascertainment beyond classic ZSD. (tucker2020genomicsequencinghighlights pages 1-7)

Variant interpretation should use ClinVar/ACMG evidence at the exact transcript and genome build. No comprehensive, current PEX6 ClinVar export or variant-level gnomAD frequencies was retrieved, so individual population frequencies and classifications should not be inferred here.

### Environmental, protective and gene–environment factors

No toxin, infection, smoking, alcohol, occupation or lifestyle exposure is established as a primary cause. Sex is not a causal risk factor. Consanguinity and founder structure increase the probability that two carriers reproduce but do not alter the molecular mechanism. The Mixteco clustering suggests a founder effect, but three cases are insufficient to establish a population carrier frequency. (slaton2023zellweger’ssyndromewith pages 1-2)

No validated protective PEX6 allele, environmental protective factor or reproducible PEX6-specific modifier gene is known from the retrieved evidence. Nutrition and avoidance of prolonged fasting may reduce secondary metabolic stress but do not prevent the genetic disease. Temperature-sensitive residual import has been demonstrated for some other AAA-complex defects; it is mechanistically interesting but not an established clinical gene–environment intervention.

## 3. Phenotypes

Phenotype frequencies are poorly quantified for PEX6-PBD4B because published cohorts combine genes and severity classes. The values below are therefore qualitative unless a PEX6-specific denominator is given.

| Phenotype and suggested HPO term | Type, onset and course | Frequency/effect |
|---|---|---|
| Hypotonia — **HP:0001252** | Clinical sign; congenital in severe disease; persistent and often profound | All 3/3 p.Gly470Ala Mixteco neonates; impairs feeding, respiration and motor development. (slaton2023zellweger’ssyndromewith pages 1-2) |
| Global developmental delay/intellectual disability — **HP:0001263/HP:0001249** | Infancy/childhood; variable, frequently progressive or static after early injury | Common in moderate/severe PEX6 disease; may be minimal in Heimler syndrome. (ahangari2026unravelingpex6insights pages 2-3) |
| Seizures — **HP:0001250** | Often neonatal/infantile in severe ZSD; variable | Characteristic but not universal. (ahangari2026unravelingpex6insights pages 2-3, slaton2023zellweger’ssyndromewith pages 1-2) |
| Sensorineural hearing impairment — **HP:0000407** | Congenital or early childhood; often progressive | Defining in Heimler syndrome; 2/3 severe Mixteco infants failed ABR. Hearing loss affects language, education and social functioning. (munozpujol2022diagnosticodysseyin pages 1-2, slaton2023zellweger’ssyndromewith pages 1-2) |
| Retinal dystrophy/retinitis pigmentosa — **HP:0000556/HP:0000548** | Childhood to adult; usually progressive | Important in mild ZSD/Heimler; causes nyctalopia, field loss and low vision. (munozpujol2022diagnosticodysseyin pages 1-2) |
| Enamel hypoplasia/amelogenesis imperfecta — **HP:0006297/HP:0000703** | Appears with tooth eruption; persistent | Characteristic of Heimler syndrome; increases dental breakdown and treatment burden. (munozpujol2022diagnosticodysseyin pages 1-2, ahangari2026unravelingpex6insights pages 2-3) |
| Failure to thrive/growth restriction — **HP:0001508/HP:0001510** | Prenatal or infancy; chronic | Severe infants may cross downward in weight and head circumference. Two Mixteco infants had discharge weights at the 1.0% and 3.6% percentiles. (slaton2023zellweger’ssyndromewith pages 2-3) |
| Feeding difficulty — **HP:0011968** | Neonatal/infantile; persistent or progressive | May require gavage or gastrostomy; aspiration risk and caregiver burden are substantial. (slaton2023zellweger’ssyndromewith pages 3-4) |
| Liver dysfunction/cholestasis — **HP:0002910/HP:0001396** | Often neonatal in severe disease; may become chronic | All three Mixteco infants had abnormal hepatic panels. Maximum AST was 246–772 U/L and ALT 60–313 U/L. (slaton2023zellweger’ssyndromewith pages 2-3) |
| Craniofacial dysmorphism, large fontanelle, microcephaly — **HP:0001999, HP:0000239, HP:0000252** | Congenital, stable physical manifestations | Prominent in severe neonatal disease; minimal or absent in mild disease. (slaton2023zellweger’ssyndromewith pages 2-3) |
| Respiratory insufficiency — **HP:0002093** | Neonatal in severe disease; episodic/progressive | Related to hypotonia, weak respiratory drive, aspiration and infection. (slaton2023zellweger’ssyndromewith pages 3-4, slaton2023zellweger’ssyndromewith pages 2-3) |
| Ataxia/peripheral neuropathy/leukodystrophy — **HP:0001251, HP:0009830, HP:0002415** | Childhood or adult; slowly progressive, sometimes stepwise | Important non-classic neurologic presentations; can mimic X-linked adrenoleukodystrophy. (ahangari2026unravelingpex6insights pages 2-3, biase2020laboratorydiagnosisof pages 1-2) |
| Adrenal insufficiency — **HP:0000821** | Childhood/adult; potentially life-threatening | Reported across attenuated ZSD and warrants surveillance. (ahangari2026unravelingpex6insights pages 2-3) |
| Renal abnormalities — **HP:0000077** | Congenital or secondary | Variable; bilateral grade-1 hydronephrosis occurred in one severe infant. (slaton2023zellweger’ssyndromewith pages 3-4) |

In the three-infant series, C26:0 was **7.17–8.27 µmol/L** versus a stated reference of 0.17–0.73; C26/C22 was **0.424–0.592** versus 0.003–0.015. Phytanic and pristanic acids were normal in all three, showing that not every pathway marker is abnormal at every age. (slaton2023zellweger’ssyndromewith pages 2-3)

Formal patient-level EQ-5D, SF-36 or PROMIS estimates were not found. A completed caregiver study, NCT03440905, enrolled **92** caregivers and measured communication, medical care, emotional distress, role function, family interaction, parenting and disability-related support using PIP and FQOL instruments. This confirms substantial multidomain family burden, although retrieved registry text did not provide outcome scores. (NCT03440905 chunk 1)

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** PEX6; peroxisomal biogenesis factor 6.
- **Protein class:** type-II AAA ATPase/peroxin.
- **Cellular location/function:** cytosolic/peroxisome-associated PEX1–PEX6 complex, recruited by PEX26, which uses ATP to recycle PEX5.
- **Origin:** germline; somatic PEX6 mutations are not the mechanism of Mendelian PBD4B.
- **Functional consequence:** predominantly loss of function or partial loss of function. No established gain-of-function or dominant-negative PBD4B mechanism was identified.

Variant classes include missense, nonsense, frameshift, canonical and deep-intronic splice variants, and potentially exon-level deletions/duplications. A negative sequencing test should therefore prompt assessment of copy-number and splice-altering variants when biochemical or clinical suspicion remains high.

### Variant examples

- **c.1409G>C, p.Gly470Ala:** severe homozygous neonatal phenotype in three Mixteco infants; described as pathogenic in the clinical report. (slaton2023zellweger’ssyndromewith pages 3-4, slaton2023zellweger’ssyndromewith pages 1-2)
- **c.1992G>C, p.Glu664Asp:** homozygous PEX6-related ZSD with normal plasma VLCFA in a reported child. (ahangari2026unravelingpex6insights pages 2-3)
- **p.Leu124Pro and p.Arg786Trp:** identified in genomic analysis of a Perrault-like PEX6 phenotype; the supplementary evidence documents phase/haplotype work. (tucker2020genomicsequencinghighlights pages 1-7)

Population allele frequencies were not available in the retrieved full text. Database curation should record a frequency only after direct gnomAD/TOPMed query on the correct transcript/build.

### Modifiers, epigenetics and chromosome abnormalities

No validated modifier gene, disease-specific methylation signature, histone alteration or recurrent chromosomal rearrangement was identified. Large deletions encompassing PEX6 are theoretically detectable by copy-number analysis, but PBD4B is principally a sequence-level recessive disorder. Karyotype, FISH and methylation testing are not first-line tests.

## 5. Environmental information

Environmental toxins, radiation, pollution, smoking, alcohol and infectious agents do not cause PBD4B. Intercurrent infection, fasting, malnutrition and drug toxicity can worsen an affected person's clinical state, especially liver, respiratory or adrenal instability, but these are **stressors/complications**, not etiologic factors. Influenza A with bacterial pneumonia and recurrent pneumonia contributed to deterioration in one severely affected infant. (slaton2023zellweger’ssyndromewith pages 3-4)

There is no zoonotic, transmissible or infectious component. Standard vaccination, infection prevention and adequate nutrition are applicable supportive measures, not disease-specific prevention.

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic PEX6 loss/hypomorphism** reduces ATP-dependent activity of the PEX1–PEX6–PEX26 AAA complex.
2. **PEX5 recycling fails.** PEX5 normally binds PTS1-tagged cargo, docks at PEX13/PEX14, releases cargo, becomes ubiquitinated and is extracted back into cytosol by the AAA complex. (biase2020laboratorydiagnosisof pages 1-2, law2017theperoxisomalaaa pages 1-6)
3. **Ubiquitinated PEX5 accumulates** on the membrane, matrix-protein import becomes inefficient, and residual empty membrane structures—“peroxisomal ghosts”—predominate.
4. Ubiquitinated PEX5 can recruit selective autophagy machinery, increasing **pexophagy** and reducing functional peroxisome abundance. Law et al. stated: **“The loss of AAA-complex function in cells results in the accumulation of ubiquitinated PEX5 on the peroxisomal membrane that signals pexophagy.”** (law2017theperoxisomalaaa pages 1-6)
5. Multiple metabolic pathways fail simultaneously: VLCFA β-oxidation; phytanic-acid α-oxidation; C27 bile-acid-intermediate shortening; DHA synthesis; ether-phospholipid/plasmalogen synthesis; pipecolate oxidation; and peroxisomal redox control. ACMG emphasizes plasma VLCFA/branched-chain fatty acids and erythrocyte plasmalogens because they sample these defects. (biase2020laboratorydiagnosisof pages 1-2)
6. **Downstream tissue injury** reflects toxic substrate accumulation, membrane-lipid deficiency, altered bile acids, oxidative stress and secondary mitochondrial/ER dysfunction. Vulnerable systems include developing brain and white matter, retina, cochlea, hepatocytes, adrenal cortex, kidney and skeletal/dental tissues.

### Suggested ontology annotations

- **GO biological process:** protein import into peroxisome matrix; peroxisomal transport; very-long-chain fatty-acid catabolic process; fatty-acid beta-oxidation; ether-lipid biosynthetic process; bile-acid biosynthetic process; reactive-oxygen-species metabolic process; autophagy of peroxisome/pexophagy.
- **GO cellular component:** peroxisome (**GO:0005777**), peroxisomal membrane, peroxisomal matrix, PEX1–PEX6 ATPase complex.
- **Cell Ontology candidates:** hepatocyte (**CL:0000182**), neuron (**CL:0000540**), oligodendrocyte (**CL:0000128**), retinal photoreceptor cell (**CL:0000210**), retinal pigment epithelial cell, cochlear hair cell, adrenal cortical cell, renal tubular epithelial cell, fibroblast (**CL:0000057**).
- **CHEBI candidates:** hexacosanoic acid/C26:0; phytanic acid; pristanic acid; plasmalogens; dihydroxycholestanoic acid; trihydroxycholestanoic acid; docosahexaenoic acid; cholic acid; hydrogen peroxide.

### Immune, omics and advanced technology evidence

Immune activation is probably secondary to tissue stress rather than a primary autoimmune or immunodeficiency mechanism. No PEX6-specific human single-cell, spatial-transcriptomic, epigenomic or integrated multi-omics dataset was retrieved. Current molecular profiling is dominated by targeted metabolite/lipid measurements and cell-based import assays. Thus, claims about specific inflammatory cell populations or epigenetic drivers would be premature.

## 7. Anatomical structures affected

**Primary organ systems:** central and peripheral nervous systems; eye/retina; inner ear/cochlea; liver and biliary system; adrenal gland; kidney; skeleton and teeth. Secondary involvement includes respiratory muscle/airway function, nutrition/gastrointestinal feeding, cardiac congenital anomalies and reproductive function in Perrault-like presentations. (ahangari2026unravelingpex6insights pages 2-3, slaton2023zellweger’ssyndromewith pages 3-4)

Suggested anatomical terms include **UBERON:0000955 brain**, **UBERON:0002316 white matter**, **UBERON:0000966 retina**, cochlea/inner ear, **UBERON:0002107 liver**, adrenal gland, kidney, peripheral nerve, tooth enamel and skeletal muscle. Disease is generally bilateral/systemic; unilateral localization is not characteristic. Retinal and auditory disease are commonly bilateral.

At subcellular resolution, the primary compartment is the peroxisome, especially its membrane import/export machinery and matrix. Secondary organelle effects involve mitochondria, ER and lysosome/autophagosome pathways.

## 8. Temporal development

Three broad courses are recognized:

1. **Neonatal–infantile severe ZSD:** congenital dysmorphism, profound hypotonia, low Apgar scores, feeding/respiratory failure, liver dysfunction and sensory abnormalities. Progression is rapid, with death often during the first year. The 2023 series states that neonatal presentations “typically have a life expectancy of less than one year.” (slaton2023zellweger’ssyndromewith pages 1-2)
2. **Childhood attenuated ZSD/PBD4B:** developmental impairment, hearing/visual loss, liver/adrenal abnormalities, neuropathy and evolving white-matter disease. Course is chronic and variably progressive.
3. **Adolescent/adult or Heimler-like disease:** hearing loss, enamel defects and retinal dystrophy may dominate; ataxia, neuropathy or leukodystrophy can emerge later. Mild cases may have normal first-line biochemical tests and long diagnostic delays. (munozpujol2022diagnosticodysseyin pages 1-2, ahangari2026unravelingpex6insights pages 2-3)

There is no established spontaneous remission. Early diagnosis is important for hearing/vision support, nutrition, adrenal surveillance, family planning and avoidance of diagnostic delay, but no proven developmental window for curative therapy exists.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. When both parents are confirmed heterozygotes, each pregnancy has a 25% affected, 50% carrier and 25% non-carrier probability. Penetrance for two truly pathogenic severe alleles is expected to be high, but expressivity is markedly variable because residual function differs. Anticipation is not expected. Germline mosaicism is theoretically possible but not a recognized major mechanism.

The ZSD birth incidence quoted in the 2023 clinical report is approximately **1 in 50,000 US newborns**, but this is pan-ZSD, not PEX6-PBD4B prevalence. No reliable PEX6-specific incidence, prevalence, sex ratio or carrier frequency was found. Both sexes are affected. (slaton2023zellweger’ssyndromewith pages 1-2)

Possible population effects include:

- **Mixteco:** three homozygous p.Gly470Ala infants born at one Central California hospital; the authors proposed a founder mutation but explicitly called for larger, culturally inclusive study. (slaton2023zellweger’ssyndromewith pages 1-2)
- A French-Canadian PEX6 founder mutation was cited by the Mixteco report, but exact carrier/incidence estimates were not available in retrieved text. (slaton2023zellweger’ssyndromewith pages 6-6)
- Consanguinity increases recessive disease risk but was denied in one Mixteco family and unknown in two, so it cannot explain that cluster by itself. (slaton2023zellweger’ssyndromewith pages 1-2)

## 10. Diagnostics

### Biochemical testing

The ACMG technical standard recommends a coordinated biochemical and molecular approach. First-line biochemical investigations include:

- plasma VLCFAs: C26:0 concentration and C24/C22, C26/C22 ratios;
- plasma phytanic and pristanic acids;
- erythrocyte plasmalogens;
- plasma/urine C27 bile-acid intermediates;
- pipecolic acid where available;
- liver enzymes, bilirubin, coagulation, adrenal function and renal studies according to presentation. (biase2020laboratorydiagnosisof pages 1-2)

The standard states: **“The current diagnostic approach relies heavily on biochemical genetic tests measuring peroxisomal metabolites, including very long-chain and branched-chain fatty acids in plasma and plasmalogens in red blood cells.”** (biase2020laboratorydiagnosisof pages 1-2)

Normal VLCFAs do not exclude mild PEX6 disease. Where phenotype suggests Heimler syndrome, retinal-hearing disease or unexplained ataxia/leukodystrophy, molecular testing plus broader metabolomics—such as C26:0-lysophosphatidylcholine and bile-acid species—is appropriate. (ahangari2026unravelingpex6insights pages 2-3, ahangari2026unravelingpex6insights pages 3-5)

### Clinical and functional testing

Recommended phenotyping includes newborn/diagnostic ABR and serial audiology; ophthalmologic examination, fundus photography, OCT, ERG and visual fields; brain MRI for neuronal migration defects or leukodystrophy; liver ultrasound/elastography as indicated; EEG for seizures; nerve-conduction studies/EMG for neuropathy; developmental assessment; dental examination; and morning cortisol/ACTH testing where adrenal disease is possible. HARP used ERG voltage, OCT, visual acuity, plasmalogens, phytanic acid and C26/C22 as measurable endpoints. (NCT03856866 chunk 1)

### Molecular testing strategy

1. Use a **peroxisomal-disorder/ZSD multigene panel** that includes PEX6 and deletion/duplication analysis, or WES/WGS when presentation is broad.
2. Confirm candidate variants and parental phase by Sanger/segregation analysis.
3. If only one allele is identified, examine CNVs, intronic/splice variants and consider RNA sequencing in fibroblasts or blood when informative.
4. Pair sequencing with biochemical evaluation to establish the extent of peroxisome dysfunction and help classify VUS. ACMG notes that molecular testing commonly uses a multigene panel or exome/genome approach and that metabolic evaluation remains important when NGS is first tier. (biase2020laboratorydiagnosisof pages 1-2)

CMA may detect a large deletion but is low-yield for typical PBD4B. Karyotyping, FISH, mtDNA testing and repeat-expansion testing are not routine. RNA-seq is an adjunct for suspected splice defects; proteomics, epigenomics and liquid biopsy are not established diagnostics.

### Differential diagnosis

Important alternatives include other PEX-gene ZSDs; single-enzyme peroxisomal disorders such as D-bifunctional protein deficiency and ACOX1 deficiency; X-linked adrenoleukodystrophy; rhizomelic chondrodysplasia punctata; Usher syndrome and other deaf-blindness syndromes; isolated amelogenesis imperfecta with hearing loss; Perrault syndrome genes; mitochondrial disease; congenital disorders of glycosylation; lysosomal disease; and hereditary ataxia/leukodystrophy. Distinguishing features are a multi-pathway peroxisomal biochemical signature and biallelic PEX6 variants.

### Screening

PEX6-PBD4B is not a universal stand-alone newborn-screening target. C26:0-lysophosphatidylcholine screening used for X-ALD may incidentally identify some severe peroxisomal disorders, but mild PEX6 cases can be biochemically normal. Cascade carrier testing is recommended after a familial genotype is known. Prenatal diagnosis and PGT-M are feasible using known familial variants.

## 11. Outcome and prognosis

There are no robust PEX6-specific 5- or 10-year survival curves. Prognosis is driven principally by residual peroxisomal function and neonatal severity.

- Severe neonatal disease has high infant mortality. In the three p.Gly470Ala cases, one male died at approximately three months and one female at about six months; the third was placed on comfort care, with subsequent survival not established in the report. (slaton2023zellweger’ssyndromewith pages 3-4, slaton2023zellweger’ssyndromewith pages 1-2)
- Mild patients can survive into adulthood but may experience progressive hearing loss, retinal degeneration, ataxia, neuropathy, adrenal disease and leukodystrophy. (munozpujol2022diagnosticodysseyin pages 1-2, ahangari2026unravelingpex6insights pages 2-3)
- Major morbidity arises from deafness/blindness, motor and cognitive disability, seizures, feeding dependence, liver disease and respiratory infections.

Adverse prognostic indicators include neonatal onset, profound hypotonia, seizures, severe liver/coagulation disease, major feeding/respiratory compromise, markedly defective import and two null/severe alleles. Residual biochemical function and hypomorphic missense alleles generally predict longer survival, but individual prediction remains imprecise.

## 12. Treatment

### Current standard

There is **no curative or proven PEX6-specific disease-modifying therapy**. Management is multidisciplinary and symptom-directed:

- nutrition assessment, caloric support, feeding therapy, aspiration management and gastrostomy when necessary;
- seizure treatment using standard antiseizure medicines selected with attention to liver function;
- hearing aids/cochlear implantation and communication support;
- low-vision services, refraction, retinal monitoring and treatment of actionable ocular complications;
- physical, occupational, speech and developmental therapy;
- liver, coagulation, renal and adrenal monitoring, with hormone replacement for confirmed adrenal insufficiency;
- dental prevention/restoration for enamel disease;
- respiratory support, infection treatment, sleep/airway evaluation and palliative care for severe neonatal disease.

Suggested MAXO concepts include genetic counseling, molecular genetic testing, biochemical testing, hearing assessment, hearing-aid fitting, cochlear implantation, ophthalmologic examination, retinal imaging, physical therapy, occupational therapy, speech therapy, gastrostomy, enteral nutrition, seizure management, adrenal surveillance and palliative care.

### Pharmacologic and experimental interventions

**Cholic acid.** This can suppress synthesis of hepatotoxic C27 bile-acid intermediates in selected ZSD patients with bile-acid abnormalities/liver disease. Evidence is pan-ZSD and does not establish neurologic or PEX6-specific efficacy. Liver disease can progress despite treatment, so it is not curative.

**Hydroxychloroquine/pexophagy inhibition.** HARP, **NCT03856866**, was a completed randomized, quadruple-masked, placebo-controlled crossover series of N-of-1 trials. It enrolled **3** participants with PEX1-, PEX6- or PEX26-related PBD, using hydroxychloroquine 4 mg/kg/day for 84 days, an 84-day washout and crossover; endpoints included ERG, plasmalogens, phytanic acid and C26/C22. No genotype-stratified peer-reviewed clinical benefit was retrieved. (NCT03856866 chunk 1) Moreover, a 2021 cellular study found that chloroquine, hydroxychloroquine and 3-methyladenine did not restore function and could worsen matrix import/metabolism. Its conclusion was: **“Our results do not support the use of autophagy inhibitors as potential treatment for PBD-ZSD patients.”** This was primarily PEX1-G843D cellular evidence, but it argues against off-label HCQ for PEX6 outside research. (klouwer2021autophagyinhibitorsdo pages 1-2)

**Betaine.** **NCT01838941** was an open-label, single-group six-month trial in **12** participants, but eligibility was restricted to PEX1-G843D genotypes. It is therefore not evidence for PEX6-PBD4B. Doses were 6 g/day below 30 kg and 12 g/day above 30 kg. (NCT01838941 chunk 1)

**L-arginine and molecular chaperones.** L-arginine improved functions in some PEX1-G843D cells and remains preclinical; applicability to PEX6 is unproven. (klouwer2021autophagyinhibitorsdo pages 1-2)

**Gene/RNA/cell therapy.** No approved PEX6 gene replacement, CRISPR, ASO, siRNA or cell therapy was identified. Major challenges include multisystem delivery, treatment before developmental injury and appropriate control of PEX6 expression/complex assembly.

### Current studies and real-world infrastructure

- **NCT01668186:** recruiting longitudinal PBD natural-history study, planned enrollment **244**, with annual clinical, biochemical, MRI and retinal assessments. (NCT01668186 chunk 1)
- **NCT06190626:** recruiting ZSD retinopathy natural-history study, enrollment **30**.
- **NCT03440905:** completed caregiver symptom/QoL survey, enrollment **92**. (NCT03440905 chunk 1)
- **NCT03115086:** active-not-recruiting Cholbam/cholic-acid registry, enrollment **55**.

No established PEX6 pharmacogenomic dosing guideline was found.

## 13. Prevention

Primary lifestyle prevention is not possible after conception because disease is caused by inherited PEX6 variants. Effective genetic prevention options are:

- preconception and prenatal **genetic counseling**;
- targeted carrier testing for relatives and potentially founder populations after the founder association is validated;
- partner testing;
- IVF with PGT-M;
- chorionic-villus sampling or amniocentesis for known familial variants;
- donor gametes or adoption according to family preferences.

Secondary prevention means early recognition through biochemical and genetic diagnosis, especially when hearing loss, enamel defects and retinal dystrophy coexist. Tertiary prevention includes vaccination, aspiration and infection prevention, nutrition, hearing/vision intervention, seizure control, adrenal-crisis education and surveillance of liver/renal disease. No vaccine, prophylactic drug or environmental intervention prevents the underlying PEX6 defect.

## 14. Other species and naturally occurring disease

PEX6 and the PEX1–PEX6 recycling mechanism are evolutionarily conserved across eukaryotes. Relevant taxa include **Homo sapiens (NCBI Taxon 9606), Mus musculus (10090), Danio rerio (7955), Drosophila melanogaster (7227)** and budding yeast. Orthologous Pex6 participates in ATP-dependent receptor recycling.

No well-established, naturally occurring companion-animal or livestock PEX6 syndrome with validated breed/VBO annotation was found in the retrieved evidence. Therefore, a specific veterinary breed association, cross-species transmission or zoonotic potential should be recorded as **not established/not applicable**. PBD4B is inherited, not infectious.

## 15. Model organisms and experimental systems

### Patient cells

Cultured skin fibroblasts are the most directly relevant model. Assays include catalase or PTS1 immunofluorescence, matrix-protein import, temperature rescue, VLCFA oxidation, plasmalogen synthesis and complementation. AAA-complex cellular models show ubiquitinated PEX5 accumulation and pexophagy. Law et al. reported rescue of peroxisome number/import/function after autophagy inhibition, whereas later work in four PEX1-G843D cell types found metabolic worsening with pharmacologic autophagy inhibitors, illustrating model- and genotype-dependence. (klouwer2021autophagyinhibitorsdo pages 1-2, law2017theperoxisomalaaa pages 1-6)

### Mouse

Global severe peroxisome-biogenesis knockouts reproduce hypotonia, neuronal migration abnormalities, liver disease and early lethality, limiting longitudinal postnatal experiments. Hypomorphic PEX1 models reproduce attenuated ZSD liver/metabolic disease and are useful for therapy development, but they are not exact PEX6-PBD4B models. Conditional neural, hepatic or glial Pex knockouts help identify tissue-specific mechanisms.

### Zebrafish

Zebrafish peroxisome-deficiency models permit live developmental imaging, locomotor and retinal phenotyping, lipid analysis and drug screening. They can reproduce VLCFA/branched-chain lipid accumulation, defective import, visual abnormalities and stress/pexophagy signatures. Most retrieved models were Pex1 or other peroxins rather than Pex6, so translation to PBD4B is mechanistically relevant but indirect.

### Drosophila and yeast

Drosophila peroxin mutants reproduce reduced lifespan, locomotor abnormalities, retinal/neural degeneration, lipid dysregulation and infertility. Yeast remains a powerful structural and functional system for Pex1/Pex6 ATPase assembly, Pex5 export and variant complementation. Limitations include divergent organ physiology, lipid pathways and developmental phenotypes.

### Evidence gaps and research priorities

1. A PEX6-specific longitudinal cohort with standardized HPO frequencies, survival and genotype-residual-function data.
2. Direct ClinVar/gnomAD curation of all reported PEX6 alleles, including founder haplotypes.
3. Human retinal, cochlear, neural and hepatic cell models—preferably isogenic iPSC/organoid systems.
4. PEX6 knock-in animal models for common severe and hypomorphic alleles.
5. Biomarkers sensitive to mild disease when VLCFAs are normal.
6. Controlled testing of gene replacement, allele-specific rescue or safe modulation of peroxisome quality control.

## Selected authoritative sources and dates

- Slaton D et al. **“Zellweger’s Syndrome With PEX6 Gene Mutation in Mixteco Neonates Due to Possible Founder Effect.”** Published 13 September 2023. DOI/URL: https://doi.org/10.7759/cureus.45162. PEX6-specific human case series. (slaton2023zellweger’ssyndromewith pages 1-2)
- De Biase I et al. **ACMG technical standard for laboratory diagnosis of peroxisomal disorders.** Approved 15 October 2019; published 2020. DOI/URL: https://doi.org/10.1038/s41436-019-0713-9. (biase2020laboratorydiagnosisof pages 1-2)
- Law KB et al. **“The peroxisomal AAA ATPase complex prevents pexophagy and development of peroxisome biogenesis disorders.”** 2017. DOI/URL: https://doi.org/10.1080/15548627.2017.1291470. Primary cell-mechanism study. (law2017theperoxisomalaaa pages 1-6)
- Klouwer FCC et al. **“Autophagy Inhibitors Do Not Restore Peroxisomal Functions…”** Published 1 April 2021. DOI/URL: https://doi.org/10.3389/fcell.2021.661298. Primary in-vitro study. (klouwer2021autophagyinhibitorsdo pages 1-2)
- Muñoz-Pujol G et al. **Adult mild ZSD diagnosis using WES/RNA-seq.** Published October 2022. DOI/URL: https://doi.org/10.3390/ijms232012367. Although PEX1-specific, it supports diagnostic principles for mild PEX6 disease. (munozpujol2022diagnosticodysseyin pages 1-2)
- Braverman NE et al. **Current diagnosis, manifestations and treatment guidelines.** PMID **26750748**; DOI: 10.1016/j.ymgme.2015.12.009. Listed as authoritative background for the ZSD QoL trial. (NCT03440905 chunk 1)
- HARP hydroxychloroquine trial, **NCT03856866**: https://clinicaltrials.gov/study/NCT03856866. (NCT03856866 chunk 1)
- PBD natural-history study, **NCT01668186**: https://clinicaltrials.gov/study/NCT01668186. (NCT01668186 chunk 1)
- ZSD caregiver QoL study, **NCT03440905**: https://clinicaltrials.gov/study/NCT03440905. (NCT03440905 chunk 1)

**Overall evidence assessment:** the causal PEX6–PBD4B relationship and core peroxisomal-import mechanism are strong. Phenotype breadth is well established, but PEX6-specific frequencies, population prevalence, long-term survival, modifier genes and treatment-response estimates remain limited. Most therapeutic and natural-history evidence is pan-ZSD or PEX1-dominant and should not be represented as proven PEX6-specific efficacy.

References

1. (OpenTargets Search: peroxisome biogenesis disorder 4B-PEX6): Open Targets Query (peroxisome biogenesis disorder 4B-PEX6, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (munozpujol2022diagnosticodysseyin pages 1-2): Gerard Muñoz-Pujol, Socorro Alforja-Castiella, Ricardo Casaroli-Marano, Blai Morales-Romero, Judit García-Villoria, Vicente A. Yépez, Julien Gagneur, Mirjana Gusic, Holger Prokisch, Frederic Tort, and Antonia Ribes. Diagnostic odyssey in an adult patient with ophthalmologic abnormalities and hearing loss: contribution of rna-seq to the diagnosis of a pex1 deficiency. International Journal of Molecular Sciences, 23:12367, Oct 2022. URL: https://doi.org/10.3390/ijms232012367, doi:10.3390/ijms232012367. This article has 7 citations.

3. (slaton2023zellweger’ssyndromewith pages 1-2): Daniel Slaton, Ashley Chang, Tamanna Ahluwalia, Sophie Alfaro, Britani Javed, and Rocky Greer. Zellweger’s syndrome with pex6 gene mutation in mixteco neonates due to possible founder effect. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45162, doi:10.7759/cureus.45162. This article has 1 citations.

4. (ahangari2026unravelingpex6insights pages 2-3): Najmeh Ahangari, Bita Barazandeh Shirvan, Farah Ashrafzadeh, Ehsan Ghayoor Karimiani, Narges Hashemi, Shima Imannezhad, Hashem Lashgari Kalat, Farnoosh Ebrahimzadeh, Javad Akhondian, and Mehran Beiraghi Toosi. Unraveling pex6: insights into very-long-chain fatty acid levels and peroxisome biogenesis disorders in pediatric populations. Annals of Pediatric Endocrinology &amp; Metabolism, 31:3-10, Feb 2026. URL: https://doi.org/10.6065/apem.2550134.067, doi:10.6065/apem.2550134.067. This article has 1 citations.

5. (biase2020laboratorydiagnosisof pages 1-2): Irene De Biase, Silvia Tortorelli, Lisa Kratz, Steven J. Steinberg, Kristina Cusmano-Ozog, and Nancy Braverman. Laboratory diagnosis of disorders of peroxisomal biogenesis and function: a technical standard of the american college of medical genetics and genomics (acmg). Genetics in Medicine, 22:686-697, Apr 2020. URL: https://doi.org/10.1038/s41436-019-0713-9, doi:10.1038/s41436-019-0713-9. This article has 29 citations and is from a highest quality peer-reviewed journal.

6. (slaton2023zellweger’ssyndromewith pages 3-4): Daniel Slaton, Ashley Chang, Tamanna Ahluwalia, Sophie Alfaro, Britani Javed, and Rocky Greer. Zellweger’s syndrome with pex6 gene mutation in mixteco neonates due to possible founder effect. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45162, doi:10.7759/cureus.45162. This article has 1 citations.

7. (slaton2023zellweger’ssyndromewith pages 2-3): Daniel Slaton, Ashley Chang, Tamanna Ahluwalia, Sophie Alfaro, Britani Javed, and Rocky Greer. Zellweger’s syndrome with pex6 gene mutation in mixteco neonates due to possible founder effect. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45162, doi:10.7759/cureus.45162. This article has 1 citations.

8. (klouwer2021autophagyinhibitorsdo pages 1-2): Femke C. C. Klouwer, Kim D. Falkenberg, Rob Ofman, Janet Koster, Démi van Gent, Sacha Ferdinandusse, Ronald J. A. Wanders, and Hans R. Waterham. Autophagy inhibitors do not restore peroxisomal functions in cells with the most common peroxisome biogenesis defect. Frontiers in Cell and Developmental Biology, Apr 2021. URL: https://doi.org/10.3389/fcell.2021.661298, doi:10.3389/fcell.2021.661298. This article has 23 citations.

9. (NCT03856866 chunk 1): Neal Sondheimer. Hydroxychloroquine Administration for Reduction of Pexophagy. The Hospital for Sick Children. 2019. ClinicalTrials.gov Identifier: NCT03856866

10. (ahangari2026unravelingpex6insights pages 3-5): Najmeh Ahangari, Bita Barazandeh Shirvan, Farah Ashrafzadeh, Ehsan Ghayoor Karimiani, Narges Hashemi, Shima Imannezhad, Hashem Lashgari Kalat, Farnoosh Ebrahimzadeh, Javad Akhondian, and Mehran Beiraghi Toosi. Unraveling pex6: insights into very-long-chain fatty acid levels and peroxisome biogenesis disorders in pediatric populations. Annals of Pediatric Endocrinology &amp; Metabolism, 31:3-10, Feb 2026. URL: https://doi.org/10.6065/apem.2550134.067, doi:10.6065/apem.2550134.067. This article has 1 citations.

11. (ahangari2026unravelingpex6insights pages 1-2): Najmeh Ahangari, Bita Barazandeh Shirvan, Farah Ashrafzadeh, Ehsan Ghayoor Karimiani, Narges Hashemi, Shima Imannezhad, Hashem Lashgari Kalat, Farnoosh Ebrahimzadeh, Javad Akhondian, and Mehran Beiraghi Toosi. Unraveling pex6: insights into very-long-chain fatty acid levels and peroxisome biogenesis disorders in pediatric populations. Annals of Pediatric Endocrinology &amp; Metabolism, 31:3-10, Feb 2026. URL: https://doi.org/10.6065/apem.2550134.067, doi:10.6065/apem.2550134.067. This article has 1 citations.

12. (law2017theperoxisomalaaa pages 1-6): Kelsey B. Law, Dana Bronte-Tinkew, Erminia Di Pietro, Ann Snowden, Richard O. Jones, Ann Moser, John H. Brumell, Nancy Braverman, and Peter K. Kim. The peroxisomal aaa atpase complex prevents pexophagy and development of peroxisome biogenesis disorders. Autophagy, 13:868-884, May 2017. URL: https://doi.org/10.1080/15548627.2017.1291470, doi:10.1080/15548627.2017.1291470. This article has 134 citations and is from a domain leading peer-reviewed journal.

13. (slaton2023zellweger’ssyndromewith pages 6-6): Daniel Slaton, Ashley Chang, Tamanna Ahluwalia, Sophie Alfaro, Britani Javed, and Rocky Greer. Zellweger’s syndrome with pex6 gene mutation in mixteco neonates due to possible founder effect. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45162, doi:10.7759/cureus.45162. This article has 1 citations.

14. (NCT03440905 chunk 1):  Proxy-Reported Symptoms and Quality of Life Survey in Zellweger Spectrum Disorders. University of South Florida. 2018. ClinicalTrials.gov Identifier: NCT03440905

15. (NCT01668186 chunk 1): Nancy Braverman. Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD). McGill University Health Centre/Research Institute of the McGill University Health Centre. 2012. ClinicalTrials.gov Identifier: NCT01668186

16. (tucker2020genomicsequencinghighlights pages 1-7): Elena J. Tucker, Rocio Rius, Sylvie Jaillard, Katrina Bell, Phillipa J. Lamont, André Travessa, Juliette Dupont, Lurdes Sampaio, Jérôme Dulon, Sandrine Vuillaumier-Barrot, Sandra Whalen, Arnaud Isapof, Tanya Stojkovic, Susana Quijano-Roy, Gorjana Robevska, Jocelyn van den Bergen, Chloe Hanna, Andrea Simpson, Katie Ayers, David R. Thorburn, John Christodoulou, Philippe Touraine, and Andrew H. Sinclair. Genomic sequencing highlights the diverse molecular causes of perrault syndrome: a peroxisomal disorder (pex6), metabolic disorders (clpp, ggps1), and mtdna maintenance/translation disorders (lars2, tfam). Human Genetics, 139:1325-1343, May 2020. URL: https://doi.org/10.1007/s00439-020-02176-w, doi:10.1007/s00439-020-02176-w. This article has 48 citations and is from a peer-reviewed journal.

17. (NCT01838941 chunk 1): Nancy Braverman. Betaine and Peroxisome Biogenesis Disorders. McGill University Health Centre/Research Institute of the McGill University Health Centre. 2013. ClinicalTrials.gov Identifier: NCT01838941

## Artifacts

- [Edison artifact artifact-00](Peroxisome_Biogenesis_Disorder_4B-deep-research-falcon_artifacts/artifact-00.md)