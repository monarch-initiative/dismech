---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:05:05.992772'
end_time: '2026-08-01T17:13:02.518455'
duration_seconds: 476.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MTO1 Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: MTO1_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MTO1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MTO1 Deficiency** covering all of the
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
- **Disease Name:** MTO1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MTO1 Deficiency** covering all of the
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


# MTO1 Deficiency: Comprehensive Disease-Characteristics Report

## Executive summary

**MTO1 deficiency** is an ultra-rare, autosomal-recessive mitochondrial translation disorder caused by biallelic pathogenic variants in **MTO1**. It is classically termed **combined oxidative phosphorylation deficiency 10 (COXPD10)** or **mitochondrial hypertrophic cardiomyopathy with lactic acidosis due to MTO1 deficiency**. The central defect is impaired modification and maturation of mitochondrial tRNAs, reducing mitochondrial protein synthesis and oxidative-phosphorylation (OXPHOS) capacity. The heart and nervous system are especially vulnerable.

The largest disease-specific synthesis comprised only **35 affected individuals from 26 families**, illustrating both the rarity of the disorder and the limited precision of current frequency and prognostic estimates. In that cohort, eventual frequencies included lactic acidosis in 100%, developmental delay/intellectual disability in 97%, hypertrophic cardiomyopathy in 79%, hypotonia in 63%, optic atrophy in 52%, feeding difficulty in 49%, seizures in 34%, and ataxia in 21%. Overall mortality was 34%, concentrated among patients with neonatal presentation and severe genotypes. No curative or disease-modifying therapy, validated biomarker, formal diagnostic criteria, or MTO1-specific interventional clinical trial was identified. Management is multidisciplinary and supportive. (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 1-5, obyrne2018thegenotypicand pages 12-16)

The following table provides a compact knowledge-base representation; the narrative sections then document each requested domain.

| Domain | Key facts | Suggested ontology IDs | Evidence |
|---|---|---|---|
| Identity / identifiers | MTO1 deficiency is a rare Mendelian mitochondrial disease, commonly described as combined oxidative phosphorylation deficiency-10 (COXPD10) and also as mitochondrial hypertrophic cardiomyopathy with lactic acidosis due to MTO1 deficiency; evidence here is aggregated from published case reports/series rather than EHR-only resources. | MONDO:0013865; OMIM for MTO1 deficiency/COXPD10: not confidently verified here; Orphanet/MeSH/ICD: unavailable or not confidently verified here | (OpenTargets Search: combined oxidative phosphorylation deficiency 10-MTO1, obyrne2018thegenotypicand pages 1-5, obyrne2018thegenotypicand pages 5-9) |
| Genetics / inheritance | Cause: biallelic pathogenic variants in **MTO1** (mitochondrial tRNA translation optimization 1), autosomal recessive. Largest compiled cohort: 35 patients from 26 unrelated families, 17 male/18 female, across 11 countries. Variant spectrum in that cohort: 19 pathogenic variants total (15 missense, 3 frameshift, 1 splice-site); no confirmed biallelic truncating genotypes, suggesting complete loss of function may be incompatible with human survival. Consanguinity reported in 34% of cases. | Gene: **MTO1**; inheritance term: autosomal recessive (ontology ID not asserted here); GO process suggestions: mitochondrial translational elongation/translation **GO:0032543** (mitochondrial translation), oxidative phosphorylation **GO:0006119** | (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 12-16, obyrne2018thegenotypicand pages 16-18) |
| Core phenotype frequencies | Frequent clinical features in the 35-patient series: lactic acidosis 100% eventually; hypertrophic cardiomyopathy 79% eventually (44% presenting feature); developmental delay/intellectual disability 97%; hypotonia 63% eventually; feeding difficulties 49%; optic atrophy 52%; seizures 34%; failure to thrive 34%; ataxia 21%. | HP:0003128 lactic acidosis; HP:0001639 hypertrophic cardiomyopathy; HP:0001263 global developmental delay; HP:0001252 hypotonia; HP:0001250 seizures; HP:0000648 optic atrophy; ataxia: HPO ID not confidently asserted here; failure to thrive: HPO ID not confidently asserted here | (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 1-5, obyrne2018thegenotypicand pages 5-9) |
| Biochemical signature | Peak plasma lactate averaged 13.6 mmol/L (range 3.4-57.8). Elevated plasma alanine in 88% of tested patients. Muscle respiratory-chain enzymology commonly showed combined deficiencies, especially complex IV deficiency in 28/30 muscle samples (93%); combined complex I+IV deficiency was most common (20/30). Fibroblast testing can be falsely normal. | CHEBI lactate/alanine: not asserted here; GO:0006120 mitochondrial electron transport, NADH to ubiquinone; GO:0006123 mitochondrial electron transport, cytochrome c to oxygen; GO:0006119 oxidative phosphorylation | (obyrne2018thegenotypicand pages 12-16, obyrne2018thegenotypicand pages 18-22) |
| Mechanism / causal chain | Upstream defect: impaired MTO1-dependent wobble U34 taurine-related modification of specific mt-tRNAs (reported for mt-tRNA\(Glu\), mt-tRNA\(Gln\), mt-tRNA\(Lys\), mt-tRNA\(Trp\), mt-tRNA\(Leu\(UUR\)\)). Intermediate effects: abnormal mt-tRNA structure/stability and aminoacylation, impaired mitochondrial transcript maturation/polyadenylation, reduced mitochondrial translation, defective OXPHOS complex assembly/activity. Downstream effects: bioenergetic failure, increased anaerobic glycolysis/lactic acidosis, altered fatty-acid metabolism with lipid droplet accumulation, cardiomyocyte hypertrophy and multisystem disease. Human fibroblasts further support HIF-1 activation with PPARγ/UCP2/AMPK-axis dysregulation. | GO:0032543 mitochondrial translation; GO:0000959 mitochondrial RNA metabolic process; GO:0006119 oxidative phosphorylation; GO:0006635 fatty acid beta-oxidation; GO:0001666 response to hypoxia; GO:0005739 mitochondrion | (zhang2021ablationofmto1 pages 11-12, boutoual2018defectsinthe pages 1-2, boutoual2018defectsinthe pages 2-3, kazuhito2020posttranscriptionalmodificationsin pages 14-15) |
| Affected anatomy / cells / compartments | Organs/systems: heart, brain/CNS, skeletal muscle, eye/optic nerve; multisystem disease with high-energy tissues preferentially affected. Imaging abnormalities reported in >70% with involvement of claustrum, thalami, white matter, cerebellar peduncles, and corpus callosum. Cell types implicated include cardiomyocytes and fibroblasts; subcellular localization centers on mitochondria/mitochondrial matrix and inner-membrane respiratory-chain machinery. | UBERON heart/brain/skeletal muscle/eye terms: not confidently asserted here; CL: cardiomyocyte and fibroblast IDs not confidently asserted here; GO:0005739 mitochondrion; GO:0005759 mitochondrial matrix; GO:0005743 mitochondrial inner membrane | (obyrne2018thegenotypicand pages 16-18, zhang2021ablationofmto1 pages 5-6) |
| Diagnosis | Best-confirming test strategy is genomic: WES or comprehensive mitochondrial/nuclear gene sequencing, because phenotype is nonspecific and fibroblast respiratory-chain testing may miss cases. Supportive findings: elevated lactate/alanine, urinary mitochondrial markers, brain MRI abnormalities, and reduced muscle complex I/III/IV activities. Muscle biopsy with respiratory-chain enzyme analysis is more sensitive than fibroblasts but not specific. Differential diagnosis includes other nuclear mitochondrial-translation disorders causing infantile cardiomyopathy/lactic acidosis (for example GTPBP3, TRMU/MTU1, MTFMT, MRPL44, FARS2, RARS2-related disease). | Diagnostic ontology IDs: not asserted here; GO terms as above may support annotation of functional assays | (obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 37-40, obyrne2018thegenotypicand pages 18-22) |
| Treatment evidence | No evidence-based disease-specific therapy established. Supportive regimens used include L-carnitine, coenzyme Q10, riboflavin, vitamins, dichloroacetate, and antiseizure therapies; most had little or no appreciable objective benefit. Ketogenic diet showed subjective or seizure-related benefit in a minority (2/5 cases in one summary; 1/5 improved in another extract), so evidence remains limited and individualized. Experimental mechanistic suggestions from cell work include PPARγ agonism/AMPK activation and N-acetyl-cysteine, but these are not established clinical therapies for MTO1 deficiency. No disease-specific interventional clinical trial was retrieved in the tool search. | NCIT intervention IDs: not confidently asserted here; diet/drug ontologies not asserted here | (obyrne2018thegenotypicand pages 12-16, obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 18-22, obyrne2018thegenotypicand pages 1-5) |
| Prognosis / natural history | Onset ranged from day 1 of life to 8 years (average ~10.2 months); 44% presented within first 2 days of life. Mortality in the 35-patient series was 34% overall, mean age at death 2.67 years; early neonatal presentation predicted worse outcome, and patients with one truncating plus one missense allele had particularly severe disease. Cardiomyopathy is common but not obligatory, and a minority survive into adolescence/adulthood, demonstrating variable expressivity. | Natural-history ontology IDs: not asserted here | (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 12-16) |
| Models | **Zebrafish mto1 knockout** recapitulates human hypertrophic cardiomyopathy, showing heart-looping defects, cardiomyocyte hypertrophy, myofiber disarray, mitochondrial fragmentation/cristae loss, impaired mt-tRNA maturation, altered mRNA polyadenylation, and reduced OXPHOS activity. **Mouse models:** partial knockdown yields mild cardiac phenotype with reduced mitochondrial translation/respiration; complete knockout causes >80% loss of mitochondrial translation and embryonic lethality around E8. **Yeast models:** conserved MTO1 ortholog supports pathogenicity testing and links U34 hypomodification to mitochondrial translation defects. No clearly established naturally occurring veterinary disease was identified here. | NCBI Taxon suggestions: Danio rerio 7955; Mus musculus 10090; Saccharomyces cerevisiae 4932 | (zhang2021ablationofmto1 pages 11-12, magistrati2023modopathiescausedby pages 8-9, zhang2021ablationofmto1 pages 5-6, kazuhito2020posttranscriptionalmodificationsin pages 14-15) |


*Table: This compact table summarizes high-value knowledge-base facts for MTO1 deficiency, including identifiers, genetics, phenotype frequencies, mechanism, diagnosis, treatment evidence, prognosis, and model systems. It also suggests ontology mappings where the identifier is confidently supported and flags unavailable or uncertain IDs rather than inventing them.*

---

## 1. Disease information

### Definition and classification

MTO1 deficiency is a **primary nuclear-encoded mitochondrial disease** in which defective mitochondrial RNA modification compromises translation of the 13 mtDNA-encoded OXPHOS polypeptides. It is a Mendelian, multisystem, combined respiratory-chain disorder rather than an isolated sarcomeric cardiomyopathy. Clinical expression ranges from fatal neonatal lactic acidosis and hypertrophic cardiomyopathy to later-onset neurodevelopmental, optic-nerve, or predominantly neurologic disease. Cardiomyopathy is common but not obligatory. (obyrne2018thegenotypicand pages 1-5, obyrne2018thegenotypicand pages 18-22)

### Identifiers and names

- **MONDO:** **MONDO:0013865**, “mitochondrial hypertrophic cardiomyopathy with lactic acidosis due to MTO1 deficiency.” Open Targets links this entity to MTO1/ENSG00000135297 and supporting literature including PMIDs **22608499, 23929671, 27604308, 34547275, 34990597, and 39472908**. (OpenTargets Search: combined oxidative phosphorylation deficiency 10-MTO1)
- **Disease OMIM:** commonly reported as **COXPD10, OMIM #614702**; the O’Byrne paper’s extracted text also associates MTO1 deficiency with OMIM #614667, which is likely a gene/disease-record ambiguity. The identifiers should therefore be checked directly against the current OMIM release before database ingestion.
- **Gene:** **MTO1**, mitochondrial tRNA translation optimization 1; HGNC symbol MTO1; Ensembl **ENSG00000135297**. (OpenTargets Search: combined oxidative phosphorylation deficiency 10-MTO1)
- **Synonyms:** MTO1-related disorder; MTO1 deficiency; combined oxidative phosphorylation deficiency 10; COXPD10; mitochondrial hypertrophic cardiomyopathy with lactic acidosis due to MTO1 deficiency; MTO1-related mitochondrial translation disorder.
- **Orphanet, MeSH, ICD-10/ICD-11:** a confidently disease-specific code was not recovered. In clinical coding, the condition may fall under broader mitochondrial-metabolism or cardiomyopathy categories, but these should not be treated as equivalent disease identifiers.

The evidence is predominantly **aggregated disease-level literature**—case reports, retrospective international case series, and laboratory/model studies—not longitudinal EHR-derived population data. The principal cohort included 35 patients from 11 countries. (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 16-18)

---

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

The established cause is **biallelic germline pathogenic or likely pathogenic variation in MTO1**, inherited in an autosomal-recessive manner. MTO1 encodes a mitochondrial tRNA-modifying protein required for efficient wobble-uridine decoding and mitochondrial transcript maturation. Loss of sufficient activity leads to mt-tRNA hypomodification, impaired mitochondrial translation, defective OXPHOS, ATP deficiency, and compensatory glycolysis with lactate accumulation. (zhang2021ablationofmto1 pages 11-12, boutoual2018defectsinthe pages 1-2, boutoual2018defectsinthe pages 2-3)

### Genetic risk

In the 35-patient cohort, investigators found **19 variants: 15 missense, three frameshift, and one splice-site variant**. Genotypes included homozygous and compound-heterozygous combinations. No patient carried two clearly truncating alleles; patients with one truncating and one missense allele tended to have earlier, more severe disease. Complete MTO1 loss is consequently inferred to be developmentally lethal, consistent with complete mouse knockout. (obyrne2018thegenotypicand pages 1-5, obyrne2018thegenotypicand pages 12-16, kazuhito2020posttranscriptionalmodificationsin pages 14-15)

Examples include **c.1451G>A (p.Arg484Gln)** and **c.1273G>A (p.Gly425Arg)** in compound heterozygosity, and **c.1392C>T (p.Arg464Cys)** in a mechanistically studied patient fibroblast line. Variants reported in affected families are germline, not somatic. Exact ClinVar classifications and current gnomAD frequencies must be assessed variant by variant; the retrieved cohort described the alleles as rare and damaging but does not support a single aggregate carrier-frequency estimate. (obyrne2018thegenotypicand pages 9-12, boutoual2018defectsinthe pages 1-2)

### Non-genetic risk and protective factors

No toxin, infection, occupation, sex-specific exposure, smoking behavior, diet, or lifestyle factor is established as a primary cause. Because this is a recessive congenital disorder, **family history, parental carrier status, and consanguinity** are the relevant risk factors. Consanguinity was reported in approximately **34%** of the 35 cases. (obyrne2018thegenotypicand pages 9-12)

No validated protective human allele or environmental protective factor has been established. Residual MTO1 function is plausibly protective: survival with missense or hypomorphic alleles, together with the absence of biallelic null human genotypes, supports a functional threshold. This is a genotype–function inference rather than a clinically validated protective-variant association. (obyrne2018thegenotypicand pages 12-16, obyrne2018thegenotypicand pages 16-18)

Illness, fasting, and catabolic stress can worsen mitochondrial energy imbalance in principle, but an MTO1-specific gene–environment interaction has not been quantified. Ketogenic metabolism may benefit selected patients with epilepsy, yet evidence is sparse and adverse effects are possible; it is not an established environmental modifier of MTO1 penetrance. There are no validated modifier genes, GWAS loci, epigenetic modifiers, or protective pharmacogenomic alleles.

---

## 3. Phenotypes

The best frequency estimates come from a heterogeneous, retrospectively assembled 35-person cohort and are susceptible to ascertainment, missing-data, and survival biases. (obyrne2018thegenotypicand pages 18-22)

### Major clinical and laboratory phenotypes

- **Lactic acidosis — HP:0003128; laboratory abnormality/clinical sign.** Present initially in 62% and eventually in **100%**. Peak plasma lactate averaged **13.6 mmol/L**, range **3.4–57.8 mmol/L**. It may be neonatal, persistent, episodically exacerbated, and life-threatening. (obyrne2018thegenotypicand pages 12-16)
- **Hypertrophic cardiomyopathy — HP:0001639; clinical/imaging sign.** Presenting feature in **44%** and eventually present in **79%**. Severity ranges from asymptomatic hypertrophy to heart failure and death. It is often early-onset but is not required for diagnosis. (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 18-22)
- **Global developmental delay/intellectual disability — HP:0001263/HP:0001249; developmental phenotype.** Reported in **97% of evaluable patients**. Severity is variable and usually chronic; it substantially affects education, communication, independence, and caregiver burden. (obyrne2018thegenotypicand pages 9-12)
- **Hypotonia — HP:0001252; neurologic sign.** Eventually present in **63%**; contributes to delayed motor development, feeding difficulty, and mobility impairment. (obyrne2018thegenotypicand pages 9-12)
- **Optic atrophy — HP:0000648; ophthalmic sign.** Reported in **52%**, potentially causing progressive visual impairment and loss of independence. (obyrne2018thegenotypicand pages 1-5)
- **Feeding difficulty — HP:0011968; symptom/functional manifestation.** Reported in **49%**, with aspiration and nutritional risks; some children require intensive feeding support. (obyrne2018thegenotypicand pages 9-12)
- **Seizures — HP:0001250; neurologic sign.** Reported in **34%**; severity ranges from controllable epilepsy to refractory seizures requiring multiple antiseizure medicines or ketogenic therapy. (obyrne2018thegenotypicand pages 1-5, obyrne2018thegenotypicand pages 9-12)
- **Failure to thrive — HP:0001508; growth sign.** Reported in **34%**, generally secondary to feeding problems and high metabolic demands. (obyrne2018thegenotypicand pages 1-5)
- **Ataxia — HP:0001251; neurologic sign.** Reported in **21%**, affecting balance, gait, and activities of daily living. (obyrne2018thegenotypicand pages 1-5)
- **Elevated alanine — HP:0031987 may be considered; laboratory abnormality.** Present in **88% of tested cases**, consistent with chronic pyruvate/lactate disequilibrium. (obyrne2018thegenotypicand pages 12-16)
- **Respiratory-chain deficiency — laboratory/pathology phenotype.** Complex IV deficiency occurred in **28/30 muscle samples (93%)**; 27/30 had combined deficiencies, most commonly complexes I and IV together (**20/30**). (obyrne2018thegenotypicand pages 12-16)

Brain MRI was abnormal in approximately **70% or more** of reported cases, with lesions or signal abnormalities involving white matter, thalami, claustra, corpus callosum, cerebellar peduncles, and other structures; lactate may be detected by MR spectroscopy. The pattern is not disease-specific. (obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 12-16)

No MTO1-specific EQ-5D, SF-36, PROMIS, or validated caregiver-burden study was identified. Quality-of-life impact must therefore be inferred from developmental disability, vision loss, epilepsy, feeding dependence, impaired mobility, repeated metabolic/cardiac surveillance, and risk of heart failure.

---

## 4. Genetic and molecular information

### Gene and variant architecture

**MTO1** is a nuclear gene whose protein product is imported into mitochondria. The disease mechanism is predominantly **loss of function or severe reduction of function**, not gain of function or dominant-negative activity. Pathogenic classes include missense, frameshift, and splice-altering alleles. Germline biallelic inheritance is established; large rearrangements, chromosomal aneuploidies, repeat expansions, and somatic mutations are not characteristic. (obyrne2018thegenotypicand pages 12-16, boutoual2018defectsinthe pages 1-2)

Variant interpretation should follow ACMG/AMP criteria using segregation, rarity, computational evidence, RNA effects for splice variants, and functional complementation or mitochondrial-translation assays. A VUS should not be considered diagnostic without appropriate evidence. Patient fibroblasts may show a subtle phenotype; muscle or engineered yeast/zebrafish assays can improve functional interpretation. (obyrne2018thegenotypicand pages 18-22, magistrati2023modopathiescausedby pages 8-9)

No confirmed MTO1-specific modifier gene or disease-associated methylation signature is established. The reported association with EEF1A1 in Open Targets appears to reflect variant-record or evidence integration and does **not** establish EEF1A1 as a causal or modifier gene for MTO1 deficiency. (OpenTargets Search: combined oxidative phosphorylation deficiency 10-MTO1)

---

## 5. Environmental, lifestyle, and infectious information

No infectious agent, toxin, radiation exposure, pollution source, occupational factor, alcohol exposure, smoking behavior, or exercise pattern is known to cause MTO1 deficiency. Environmental interventions cannot correct the underlying recessive genotype.

Practical mitochondrial care generally seeks to avoid prolonged fasting, dehydration, and untreated fever or infection because catabolic stress can increase energy demand and lactic acidosis; however, this is extrapolated from mitochondrial medicine rather than demonstrated in an MTO1 trial. Diet changes, particularly ketogenic therapy, require specialist supervision because potential seizure benefit must be balanced against hypoglycemia, acidosis, dyslipidemia, growth effects, and cardiometabolic risk.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** biallelic MTO1 variants reduce functional mitochondrial MTO1 protein.
2. **Primary molecular lesion:** deficient modification of wobble uridine 34 in selected mitochondrial tRNAs, particularly mt-tRNA^Glu, mt-tRNA^Gln, mt-tRNA^Lys, mt-tRNA^Trp, and mt-tRNA^Leu(UUR). Suggested annotations include mitochondrial RNA modification and **GO:0032543, mitochondrial translation**. (zhang2021ablationofmto1 pages 11-12, boutoual2018defectsinthe pages 1-2)
3. **RNA-level consequences:** altered tRNA conformation, reduced stability, increased nuclease sensitivity, and decreased aminoacylation. Zebrafish additionally demonstrate altered MTO1–MTPAP-associated mitochondrial mRNA polyadenylation; the ND1 poly(A) tail fell from about 47 to 33 nucleotides after mto1 ablation. (zhang2021ablationofmto1 pages 11-12)
4. **Translation/OXPHOS consequences:** impaired synthesis of mtDNA-encoded respiratory-chain subunits, disturbed OXPHOS complex stoichiometry and assembly, and combined complex I/III/IV dysfunction. Complete mouse knockout reduces mitochondrial translation by more than 80% and causes catastrophic respiratory-complex disassembly. Suggested terms: **GO:0006119 oxidative phosphorylation**, **GO:0006120 mitochondrial electron transport, NADH to ubiquinone**, and **GO:0006123 mitochondrial electron transport, cytochrome c to oxygen**. (boutoual2018defectsinthe pages 2-3, kazuhito2020posttranscriptionalmodificationsin pages 14-15)
5. **Metabolic compensation:** ATP deficit promotes glycolytic reliance and lactate accumulation. In patient fibroblasts, MTO1 deficiency inactivates AMPK, decreases PPARγ and UCP2, activates HIF-1, disrupts fatty-acid oxidation, and causes lipid-droplet accumulation. This distinguishes MTO1 from the related GTPBP3 defect and suggests functions beyond tRNA modification. (boutoual2018defectsinthe pages 1-2, boutoual2018defectsinthe pages 2-3)
6. **Cell/tissue injury:** high-energy postmitotic cells—especially cardiomyocytes, neurons, skeletal myofibers, and optic-nerve cells—cannot meet energetic demands. Mitochondrial fragmentation, cristae loss, altered proteostasis (including increased LONP1), cardiomyocyte hypertrophy, fiber disarray, and neural dysfunction follow. (boutoual2018defectsinthe pages 2-3, zhang2021ablationofmto1 pages 5-6)
7. **Clinical outcome:** hypertrophic cardiomyopathy/heart failure, lactic acidosis, developmental impairment, hypotonia, seizures, optic atrophy, and multisystem morbidity.

### Suggested ontology annotations

- **GO biological processes:** GO:0032543 mitochondrial translation; GO:0006119 oxidative phosphorylation; GO:0000959 mitochondrial RNA metabolic process; GO:0006635 fatty-acid beta-oxidation; GO:0001666 response to hypoxia.
- **GO cellular components:** GO:0005739 mitochondrion; GO:0005759 mitochondrial matrix; GO:0005743 mitochondrial inner membrane.
- **Cell types:** cardiomyocyte, neuron, skeletal muscle cell, fibroblast; exact CL identifiers should be ontology-release validated before ingestion.
- **Chemicals:** lactate, alanine, ATP, taurine-containing uridine modifications, coenzyme Q10, riboflavin, levocarnitine, and dichloroacetate; CHEBI identifiers should likewise be release validated.

### Molecular profiling and advanced technologies

Disease-specific transcriptomic and metabolic evidence is limited. Fibroblast studies define HIF–PPARγ–UCP2–AMPK reprogramming, while zebrafish heart analyses identify RNA-processing, ribonucleoside-biosynthesis, mRNA-catabolism, and mitochondrial-biogenesis changes. No validated single-cell atlas, spatial transcriptomic study, patient-tissue proteomic signature, lipidomic diagnostic classifier, organoid study, or genome-wide CRISPR therapeutic screen was found. (zhang2021ablationofmto1 pages 11-12, boutoual2018defectsinthe pages 1-2)

A 2023 review characterized these disorders as mitochondrial RNA **“modopathies”** and emphasized that many variants are private, making conserved yeast systems valuable for pathogenicity testing. (Publication: January 2023; DOI: https://doi.org/10.3390/ijms24032178.) (magistrati2023modopathiescausedby pages 8-9)

---

## 7. Anatomical structures affected

### Organ and tissue levels

- **Heart:** myocardium, especially ventricular cardiomyocytes; hypertrophy, fiber disarray, impaired respiration, and possible heart failure. Suggested UBERON concepts: heart, myocardium, ventricle.
- **Central nervous system:** cerebral white matter, thalamus, claustrum, corpus callosum, cerebellar pathways, and potentially broader neuronal networks.
- **Eye/visual pathway:** optic nerve and retinal ganglion-cell pathway, reflected by optic atrophy.
- **Skeletal muscle:** mitochondrial myopathy, hypotonia, weakness, and combined respiratory-chain deficiency.
- **Gastrointestinal/nutritional system:** feeding dysfunction and poor growth are often secondary functional consequences.

Disease is generally bilateral/systemic rather than consistently unilateral. No characteristic lateralization is reported. The principal subcellular compartments are the mitochondrial matrix, where RNA modification/translation occurs, and the inner mitochondrial membrane, where OXPHOS complexes reside. (obyrne2018thegenotypicand pages 16-18, zhang2021ablationofmto1 pages 5-6)

---

## 8. Temporal development and natural history

Onset in the principal cohort ranged from **day 1 to 8 years**, averaging approximately **10.2 months**; **44% presented during the first two days of life**. Onset may be acute with neonatal lactic acidosis or cardiopulmonary decompensation, or insidious with developmental delay, hypotonia, visual loss, or seizures. (obyrne2018thegenotypicand pages 9-12)

The disease is chronic and lifelong in survivors, with a highly variable course. Cardiac and neurologic involvement can emerge after the initial presentation, as illustrated by cardiomyopathy increasing from 44% at presentation to 79% eventually and hypotonia becoming evident in 63%. There is no accepted staging system. Neonatal presentation is a critical vulnerability period: approximately half of neonatal presenters died by two years in the cohort analysis. Conversely, some patients without cardiomyopathy survived into their twenties, demonstrating substantial variable expressivity. (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 18-22)

No spontaneous molecular remission is established. Symptomatic improvement—particularly seizure control—does not represent correction of the underlying mitochondrial translation defect.

---

## 9. Inheritance and population characteristics

Inheritance is **autosomal recessive**. For two confirmed carrier parents, each pregnancy conventionally carries a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of an unaffected non-carrier, assuming no unusual mosaicism or uniparental mechanism.

Penetrance appears high for pathogenic biallelic genotypes, but expressivity is markedly variable. There is no evidence for genetic anticipation. Germline mosaicism has not emerged as a defining feature, though residual recurrence risk after an apparently de novo event should be discussed according to standard genetic-counseling principles.

The 35-person cohort contained **17 males and 18 females**, providing no evidence of a major sex-incidence imbalance. Male mortality was higher in that small cohort—47% at a mean 0.96 years versus 22% at a mean 6.1 years in females—but this observation is underpowered and should not be treated as a proven sex modifier. Cases were reported from 11 countries, supporting a pan-ethnic distribution. No robust prevalence, incidence, carrier frequency, founder effect, endemic region, or population-specific sex ratio is known. (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 16-18)

---

## 10. Diagnostics

### Clinical and biochemical evaluation

Suspect MTO1 deficiency in an infant or child with otherwise unexplained combinations of hypertrophic cardiomyopathy, lactic acidosis, developmental delay, hypotonia, seizures, optic atrophy, feeding failure, or combined respiratory-chain deficiency.

Recommended evaluation includes:

- Plasma lactate, blood gas, pyruvate, lactate:pyruvate ratio, alanine, glucose, liver and renal indices, CK, acylcarnitines, plasma amino acids, and urine organic acids.
- ECG, echocardiography, and rhythm monitoring; cardiac MRI when clinically appropriate.
- Brain MRI with diffusion and MR spectroscopy; EEG for seizures.
- Ophthalmologic examination, visual electrophysiology where indicated, hearing assessment, developmental evaluation, and nutritional/swallow assessment.
- Respiratory-chain enzyme analysis and histology if biopsy is clinically justified. Muscle is more informative than fibroblasts, but combined complex I/IV deficiency is supportive rather than specific. Normal fibroblast enzymology does not exclude MTO1 deficiency. (obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 18-22)

### Genetic testing strategy

1. **Preferred:** trio WES or WGS with nuclear mitochondrial-gene analysis and copy-number/splice-aware calling.
2. **Alternative:** a comprehensive mitochondrial cardiomyopathy/mitochondrial translation panel including MTO1.
3. **Single-gene sequencing:** appropriate when familial variants are known or the biochemical phenotype is strongly suggestive; deletion/duplication analysis should be included if sequencing is negative.
4. **RNA sequencing:** useful for unresolved splice variants or cryptic splicing, preferably in an informative tissue.
5. **Functional studies:** mitochondrial translation, oxygen consumption, respiratory-chain assembly, tRNA modification/stability, or complementation may clarify VUSs.

Karyotyping, FISH, repeat-expansion testing, and isolated mtDNA testing do not directly detect ordinary biallelic MTO1 sequence variants. Chromosomal microarray may detect a rare deletion involving MTO1 but is not a sensitive first-line test for this single-gene disorder.

### Differential diagnosis

Important mimics include **GTPBP3**, **TRMU**, **MTFMT**, **MRPL44**, **TSFM**, **TUFM**, **FARS2**, **AARS2**, and **RARS2** disorders; mtDNA tRNA diseases such as MELAS; pyruvate dehydrogenase deficiency; primary complex I/IV assembly disorders; Pompe disease; fatty-acid oxidation defects; Barth syndrome; and sarcomeric or RASopathy-associated hypertrophic cardiomyopathy. Molecular confirmation is essential because the clinical and biochemical findings are nonspecific. (obyrne2018thegenotypicand pages 18-22, obyrne2018thegenotypicand pages 37-40)

No validated clinical scoring criteria, disease-specific newborn screen, or liquid-biopsy assay exists. Cascade testing is appropriate for relatives after familial variants are established.

---

## 11. Outcome and prognosis

In the 35-person series, **34% had died**, at an average age of **2.67 years**. Early neonatal presentation and a truncating-plus-missense genotype were associated with particularly poor outcomes; reported mean survival for the severe frameshift-containing group was approximately **0.24 years**. Complete loss of function is likely embryonically lethal. (obyrne2018thegenotypicand pages 9-12, obyrne2018thegenotypicand pages 12-16)

No reliable five- or ten-year survival curve exists. Potential causes of morbidity and death include severe lactic acidosis, progressive cardiomyopathy/heart failure, arrhythmia, neurologic deterioration, refractory epilepsy, aspiration, and nutritional compromise. Survivors may have lifelong cognitive, visual, motor, and feeding disability. Formal disease-specific quality-of-life and disability-adjusted-life-year data are unavailable.

Useful prognostic indicators are age at presentation, cardiac severity and ventricular function, magnitude/persistence of lactic acidosis, neurologic burden, feeding/respiratory dependence, and genotype class. These are cohort-derived associations, not validated prognostic biomarkers or calculators. (obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 12-16)

---

## 12. Treatment and current applications

### Current clinical implementation

There is **no approved MTO1-specific disease-modifying treatment**. Care should be coordinated through mitochondrial medicine, metabolic genetics, cardiology, neurology, nutrition, ophthalmology, rehabilitation, and palliative-care services as appropriate.

- **Cardiac care:** guideline-based surveillance and treatment of cardiomyopathy, heart failure, and arrhythmias. Advanced disease may prompt evaluation for mechanical support or transplantation on an individualized basis; MTO1-specific transplant outcomes are unavailable.
- **Lactic acidosis/metabolic crises:** treat precipitating illness, maintain glucose and hydration, monitor acid–base status, and avoid prolonged fasting. Bicarbonate or renal support is reserved for clinically indicated severe acidosis.
- **Epilepsy:** standard antiseizure medications selected with mitochondrial safety in mind; ketogenic therapy may be considered for refractory epilepsy only in an experienced team.
- **Nutrition/feeding:** dietitian support, swallow evaluation, calorie optimization, and enteral feeding when necessary.
- **Rehabilitation:** physical, occupational, speech, vision, and developmental therapies; exercise should be individualized to avoid exhaustion while preventing deconditioning.

### Evidence for specific agents

Cohort treatments included coenzyme Q10 in 68%, levocarnitine in 56%, riboflavin in 44%, dichloroacetate in 32%, and ketogenic diet in 23%, alongside vitamins and other “mitochondrial cocktails.” Most produced **“no appreciable effect.”** Dichloroacetate was associated with improvement of lactic acidosis and cardiomyopathy in one case, but neuropathy and other toxicity concerns preclude assuming general efficacy. Ketogenic therapy showed seizure-related benefit in only a minority—reported as 2/5 in one analysis—and remains low-quality evidence. (obyrne2018thegenotypicand pages 12-16, obyrne2018thegenotypicand pages 16-18, obyrne2018thegenotypicand pages 1-5)

Mechanistic cell work found partial reversal with the PPARγ agonist rosiglitazone or AMPK activator AICAR, while N-acetylcysteine has been proposed to support mitochondrial translation. These are **preclinical hypotheses**, not recommended MTO1 treatments. (boutoual2018defectsinthe pages 2-3, obyrne2018thegenotypicand pages 18-22)

No MTO1-specific gene replacement, CRISPR therapy, RNA therapy, cell therapy, immunotherapy, or approved targeted therapy is available. The ClinicalTrials.gov search retrieved no relevant disease-specific interventional trial or NCT identifier. NCIt annotations may include supportive-care, anticonvulsant therapy, cardiac monitoring, physical therapy, occupational therapy, and genetic counseling, but term IDs should be validated against the current NCIt release.

---

## 13. Prevention

The phenotype cannot presently be prevented after an affected individual inherits two pathogenic alleles. Primary prevention is therefore reproductive:

- genetic counseling and parental segregation testing;
- cascade carrier testing for adult relatives;
- preimplantation genetic testing for monogenic disease;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis for known familial variants;
- donor gametes or other reproductive options according to family preferences.

Secondary prevention consists of early molecular diagnosis, baseline cardiac and neurologic assessment, and prospective surveillance before overt organ failure. Tertiary prevention includes vaccination and prompt infection treatment, avoidance of prolonged fasting/dehydration, seizure control, nutritional and aspiration management, and guideline-directed cardiomyopathy care. No vaccine, medication prophylaxis, population newborn-screening program, or behavioral intervention prevents the inherited disorder.

---

## 14. Other species and naturally occurring disease

No well-established, naturally occurring companion-animal, livestock, or wildlife syndrome caused by biallelic MTO1 variation was identified. Accordingly, there is no demonstrated zoonotic potential or cross-species transmission; the disease is genetic and noninfectious.

The mechanism is strongly evolutionarily conserved. Relevant taxa include **Homo sapiens (NCBI Taxon 9606), Mus musculus (10090), Danio rerio (7955), and Saccharomyces cerevisiae (4932)**. Conserved yeast Mto1 function permits functional testing of human missense alleles, especially when clinical variants are private. (magistrati2023modopathiescausedby pages 8-9)

---

## 15. Model organisms and experimental systems

### Zebrafish

CRISPR/Cas9 **mto1-knockout Danio rerio** are viable and reproduce major human cardiac and mitochondrial phenotypes. Mutants show defective heart looping—no-loop morphology in **58% versus 16% of wild-type embryos**—cardiomyocyte hypertrophy, myocardial-fiber disarray, mitochondrial fragmentation and cristae loss, impaired tRNA aminoacylation, altered mRNA polyadenylation, reduced mitochondrial translation, and diminished OXPHOS activity. (zhang2021ablationofmto1 pages 11-12, zhang2021ablationofmto1 pages 5-6)

The primary report’s abstract states: **“These cardiac defects in the mto1KO zebrafish recapitulated the clinical phenotypes in HCM patients carrying the MTO1 mutation(s).”** This is strong mechanistic evidence for cardiac causality, although zebrafish do not reproduce the full human neurodevelopmental course. Publication: April 2021; DOI: https://doi.org/10.1093/nar/gkab228. (zhang2021ablationofmto1 pages 11-12)

### Mouse

Partial Mto1 knockdown produces mild cardiac dilation/fibrosis, decreased mitochondrial translation and complex-I assembly, and impaired cardiac mitochondrial respiration. Complete knockout causes **>80% reduction in mitochondrial translation**, severe respiratory-complex disassembly, increased anaerobic glycolysis, and embryonic death around E8. This supports a dosage threshold and the inferred nonviability of human biallelic null genotypes. The limitation is that complete knockout models embryonic lethality rather than survivable hypomorphic human disease. (kazuhito2020posttranscriptionalmodificationsin pages 14-15)

### Yeast and human cellular models

Saccharomyces cerevisiae MTO1-pathway mutants exhibit respiratory growth and mitochondrial-translation defects and can test pathogenicity of humanized alleles. Species-specific mitochondrial genetic-code and respiratory differences limit direct clinical extrapolation. (magistrati2023modopathiescausedby pages 8-9)

Patient fibroblasts and MTO1-silenced cell lines demonstrate substrate-specific tRNA hypomodification, altered angiogenin sensitivity, OXPHOS/proteostasis imbalance, HIF-1 activation, PPARγ/UCP2/AMPK suppression, defective fatty-acid oxidation, and lipid accumulation. Fibroblasts are experimentally tractable but may underrepresent heart, brain, and muscle disease and can yield normal clinical respiratory-chain assays. (boutoual2018defectsinthe pages 1-2, boutoual2018defectsinthe pages 2-3, obyrne2018thegenotypicand pages 16-18)

---

## Recent developments and expert assessment, 2023–2024

Recent literature has mainly refined the conceptual framework rather than delivered an MTO1-specific therapy. The 2023 mitochondrial RNA-modopathy review emphasized conserved model systems for interpreting private variants and linked loss of RNA modification to inefficient or inaccurate mitochondrial translation. Its abstract summarizes the field: **“Most of these mutations are sporadic or private, thus it is fundamental that their pathogenicity is confirmed through the use of a model system.”** Publication: January 2023; DOI: https://doi.org/10.3390/ijms24032178. (magistrati2023modopathiescausedby pages 8-9)

A 2024 review of defective mitochondrial protein synthesis emphasized that such disorders are commonly multisystemic and preferentially affect high-energy tissues; it highlighted mouse and zebrafish MTO1 knockouts as cardiac-disease models. A parallel 2024 mouse-model review argued that organ-specific models are essential because mitochondrial-translation disorders show marked tissue specificity. These recent authoritative syntheses support integrated genomic, transcriptomic, proteomic, and tissue-functional approaches, but they do not change current MTO1 clinical management.

The principal expert conclusions are therefore:

1. **Genomic diagnosis should be early and broad**, usually WES/WGS rather than phenotype-restricted single-gene testing.
2. **Residual MTO1 activity is a major biological determinant**; complete loss appears incompatible with mammalian development.
3. **Cardiomyopathy and lactic acidosis are signature features but not obligatory at presentation**, so absence of either should not exclude testing.
4. **Muscle functional testing is more sensitive than fibroblast respiratory-chain enzymology**, although molecular confirmation remains decisive.
5. **Therapeutic evidence is insufficient** for routine disease-targeted pharmacotherapy; cell-based pathway rescue is hypothesis-generating only. (obyrne2018thegenotypicand pages 18-22, kazuhito2020posttranscriptionalmodificationsin pages 14-15, obyrne2018thegenotypicand pages 16-18)

## Evidence limitations and knowledge gaps

The evidence base is dominated by one 35-person retrospective synthesis, individual cases, and preclinical models. There are no population-based incidence studies, prospective natural-history registry, validated patient-reported outcome, randomized treatment trial, disease-specific clinical guideline, standardized biomarker, single-cell human tissue atlas, or established gene therapy. Variant frequencies and classifications evolve and should be refreshed directly from ClinVar and gnomAD. Phenotype percentages should not be interpreted as precise population risks because referral and survival biases probably enrich severe pediatric disease.

References

1. (obyrne2018thegenotypicand pages 9-12): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 43 citations and is from a peer-reviewed journal.

2. (obyrne2018thegenotypicand pages 1-5): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 43 citations and is from a peer-reviewed journal.

3. (obyrne2018thegenotypicand pages 12-16): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 43 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: combined oxidative phosphorylation deficiency 10-MTO1): Open Targets Query (combined oxidative phosphorylation deficiency 10-MTO1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (obyrne2018thegenotypicand pages 5-9): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 43 citations and is from a peer-reviewed journal.

6. (obyrne2018thegenotypicand pages 16-18): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 43 citations and is from a peer-reviewed journal.

7. (obyrne2018thegenotypicand pages 18-22): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 43 citations and is from a peer-reviewed journal.

8. (zhang2021ablationofmto1 pages 11-12): Qinghai Zhang, Xiao He, Shihao Yao, Tianxiang Lin, Luwen Zhang, Danni Chen, Chao Chen, Qingxian Yang, Feng Li, Yi-Min Zhu, and Min-Xin Guan. Ablation of mto1 in zebrafish exhibited hypertrophic cardiomyopathy manifested by mitochondrion rna maturation deficiency. Nucleic Acids Research, 49:4689-4704, Apr 2021. URL: https://doi.org/10.1093/nar/gkab228, doi:10.1093/nar/gkab228. This article has 28 citations and is from a highest quality peer-reviewed journal.

9. (boutoual2018defectsinthe pages 1-2): Rachid Boutoual, Salvador Meseguer, Magda Villarroya, Elena Martín-Hernández, Mohammed Errami, Miguel A. Martín, Marta Casado, and M.-Eugenia Armengod. Defects in the mitochondrial-trna modification enzymes mto1 and gtpbp3 promote different metabolic reprogramming through a hif-pparγ-ucp2-ampk axis. Scientific Reports, Jan 2018. URL: https://doi.org/10.1038/s41598-018-19587-5, doi:10.1038/s41598-018-19587-5. This article has 40 citations and is from a peer-reviewed journal.

10. (boutoual2018defectsinthe pages 2-3): Rachid Boutoual, Salvador Meseguer, Magda Villarroya, Elena Martín-Hernández, Mohammed Errami, Miguel A. Martín, Marta Casado, and M.-Eugenia Armengod. Defects in the mitochondrial-trna modification enzymes mto1 and gtpbp3 promote different metabolic reprogramming through a hif-pparγ-ucp2-ampk axis. Scientific Reports, Jan 2018. URL: https://doi.org/10.1038/s41598-018-19587-5, doi:10.1038/s41598-018-19587-5. This article has 40 citations and is from a peer-reviewed journal.

11. (kazuhito2020posttranscriptionalmodificationsin pages 14-15): Tomizawa Kazuhito and Fan-Yan Wei. Posttranscriptional modifications in mitochondrial trna and its implication in mitochondrial translation and disease. Journal of biochemistry, 168:435-444, Aug 2020. URL: https://doi.org/10.1093/jb/mvaa098, doi:10.1093/jb/mvaa098. This article has 28 citations and is from a peer-reviewed journal.

12. (zhang2021ablationofmto1 pages 5-6): Qinghai Zhang, Xiao He, Shihao Yao, Tianxiang Lin, Luwen Zhang, Danni Chen, Chao Chen, Qingxian Yang, Feng Li, Yi-Min Zhu, and Min-Xin Guan. Ablation of mto1 in zebrafish exhibited hypertrophic cardiomyopathy manifested by mitochondrion rna maturation deficiency. Nucleic Acids Research, 49:4689-4704, Apr 2021. URL: https://doi.org/10.1093/nar/gkab228, doi:10.1093/nar/gkab228. This article has 28 citations and is from a highest quality peer-reviewed journal.

13. (obyrne2018thegenotypicand pages 37-40): James J. O'Byrne, Maja Tarailo-Graovac, Aisha Ghani, Michael Champion, Charu Deshpande, Ali Dursun, Riza K. Ozgul, Peter Freisinger, Ian Garber, Tobias B. Haack, Rita Horvath, Ivo Barić, Ralf A. Husain, Leo A.J. Kluijtmans, Urania Kotzaeridou, Andrew A. Morris, Colin J. Ross, Saikat Santra, Jan Smeitink, Mark Tarnopolsky, Saskia B. Wortmann, Johannes A. Mayr, Michaela Brunner-Krainz, Holger Prokisch, Wyeth W. Wasserman, Ron A. Wevers, Udo F. Engelke, Richard J. Rodenburg, Teck Wah Ting, Robert McFarland, Robert W. Taylor, Ramona Salvarinova, and Clara D.M. van Karnebeek. The genotypic and phenotypic spectrum of mto1 deficiency. Molecular Genetics and Metabolism, 123:28-42, Jan 2018. URL: https://doi.org/10.1016/j.ymgme.2017.11.003, doi:10.1016/j.ymgme.2017.11.003. This article has 43 citations and is from a peer-reviewed journal.

14. (magistrati2023modopathiescausedby pages 8-9): Martina Magistrati, Alexandru Ionut Gilea, Camilla Ceccatelli Berti, Enrico Baruffini, and Cristina Dallabona. Modopathies caused by mutations in genes encoding for mitochondrial rna modifying enzymes: molecular mechanisms and yeast disease models. International Journal of Molecular Sciences, 24:2178, Jan 2023. URL: https://doi.org/10.3390/ijms24032178, doi:10.3390/ijms24032178. This article has 14 citations.

## Artifacts

- [Edison artifact artifact-00](MTO1_Deficiency-deep-research-falcon_artifacts/artifact-00.md)