---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T16:55:10.182715'
end_time: '2026-07-31T17:05:04.304211'
duration_seconds: 594.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Progressive External Ophthalmoplegia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Progressive_External_Ophthalmoplegia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Progressive External Ophthalmoplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Progressive External Ophthalmoplegia** covering all of the
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
- **Disease Name:** Autosomal Dominant Progressive External Ophthalmoplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Progressive External Ophthalmoplegia** covering all of the
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


# Autosomal Dominant Progressive External Ophthalmoplegia: Disease-Characteristics Report

## Scope and evidence note

Autosomal dominant progressive external ophthalmoplegia (adPEO; often **adCPEO**) is a genetically heterogeneous **nuclear-genome mitochondrial DNA (mtDNA)-maintenance disorder**. It must be distinguished from the broader phenotype “mitochondrial CPEO,” which also includes sporadic single large-scale mtDNA deletions, mtDNA point variants, and recessive nuclear disorders. Statistics from mixed CPEO cohorts are therefore labeled as such rather than attributed directly to adPEO.

The strongest directly applicable human evidence retrieved was a 25-patient TWNK-adPEO cohort published online in December 2021, together with mitochondrial PEO cohorts and 2023–2024 clinical reviews. The following table summarizes the principal knowledge-base fields.

| domain | established finding | quantitative evidence | ontology suggestions | evidence scope/caveat |
|---|---|---|---|---|
| Disease definition | Autosomal dominant progressive external ophthalmoplegia (adPEO) is an adult-onset mitochondrial DNA maintenance disorder caused by heterozygous nuclear-gene defects, typically with secondary multiple mtDNA deletions in muscle and progressive ptosis/ophthalmoparesis (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, bermejoguerrero2021clinicalhistologicaland pages 1-2) | Typical onset reported at 20–40 years in review literature; TWNK cohort mean onset 43 years, mean diagnosis 63 years (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, bermejoguerrero2021clinicalhistologicaland pages 1-2) | HP:0000508 Ptosis; HP:0000602 Ophthalmoplegia; GO:0006260 DNA replication; GO:0005739 mitochondrion | Distinct from all-cause mitochondrial CPEO, which also includes mtDNA deletions/point mutations and recessive nuclear etiologies (ali2024mitochondrialchronicprogressive pages 1-3, chen2023mitochondriaandthe pages 1-2) |
| Core causal genes | Established adPEO genes include TWNK, POLG, POLG2, SLC25A4, DNA2, and RRM2B; OPA1 can produce a syndromic dominant phenotype with external ophthalmoplegia plus optic atrophy/deafness/ataxia and multiple mtDNA deletions (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, kierdaszuk2020progressiveexternalophthalmoplegia pages 11-12) | No single gene frequency is established for all adPEO; in one TWNK-specific cohort, 25/25 had heterozygous TWNK variants (bermejoguerrero2021clinicalhistologicaland pages 1-2, bermejoguerrero2021clinicalhistologicaland pages 2-4) | HGNC gene symbols as listed; GO:0003678 DNA helicase activity (TWNK); GO:0003887 DNA-directed DNA polymerase activity (POLG); GO:0140355 ADP/ATP transmembrane transporter activity (SLC25A4) | Gene list is disease-level and heterogeneous; OPA1 should be annotated as syndromic/overlap rather than core isolated adPEO in all cases (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| TWNK-specific variant data | TWNK-related adPEO is caused by heterozygous missense variants affecting mtDNA helicase function and replication (bermejoguerrero2021clinicalhistologicaland pages 1-2) | 10 different TWNK mutations in 25 patients; most frequent c.1361T>G (p.Val454Gly) in 7 patients/6 families and c.1070G>C (p.Arg357Pro) in 7 patients/5 families; c.1121G>A (p.Arg374Gln) in 3 patients; c.1411T>G (p.Tyr471Asp) in 2 siblings (bermejoguerrero2021clinicalhistologicaland pages 7-9) | Sequence Ontology: missense_variant; GO:0004386 helicase activity; GO:0006268 DNA unwinding involved in DNA replication | These frequencies apply to one Madrid laboratory cohort, not all adPEO populations (bermejoguerrero2021clinicalhistologicaland pages 2-4, bermejoguerrero2021clinicalhistologicaland pages 7-9) |
| Inheritance/family history | Inheritance is autosomal dominant with variable expressivity and adult presentation (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, kierdaszuk2020progressiveexternalophthalmoplegia pages 11-12) | In TWNK cohort, 22/25 (88%) had first-degree relatives with ptosis and/or ophthalmoplegia; 64% female (16/25) (bermejoguerrero2021clinicalhistologicaland pages 2-4) | HP:0000006 Autosomal dominant inheritance | Penetrance was not quantified in the retrieved evidence; sex distribution from one cohort should not be generalized (bermejoguerrero2021clinicalhistologicaland pages 2-4) |
| Core phenotype | Hallmark phenotype is bilateral progressive ptosis with progressive external ophthalmoplegia; weakness and exercise intolerance are common extrasocular features (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 13-14, bermejoguerrero2021clinicalhistologicaland pages 1-2) | TWNK cohort: ptosis 92%, PEO 80%, weakness 48%, exercise intolerance 28% (bermejoguerrero2021clinicalhistologicaland pages 1-2) | HP:0000508 Ptosis; HP:0000602 Ophthalmoplegia; HP:0001324 Muscle weakness; HP:0003546 Exercise intolerance | Frequencies are strongest for TWNK-related adPEO; broader adPEO due to other genes may differ (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, bermejoguerrero2021clinicalhistologicaland pages 1-2) |
| Additional/systemic phenotypes | adPEO may include bulbar dysfunction, hearing loss, ataxia, neuropathy, parkinsonism, cataracts, cardiac and respiratory involvement (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 13-14, bermejoguerrero2021clinicalhistologicaland pages 5-6) | TWNK cohort: bulbar involvement 24%, cardiac 24%, respiratory 4%, neuropathy 8%, ataxia 4%, parkinsonism 4%; cataracts reported in 2 related patients (bermejoguerrero2021clinicalhistologicaland pages 5-6, bermejoguerrero2021clinicalhistologicaland pages 1-2) | HP:0002015 Dysphagia; HP:0000407 Sensorineural hearing impairment; HP:0001251 Ataxia; HP:0002355 Difficulty walking; HP:0000518 Cataract; HP:0011675 Arrhythmia/cardiac conduction abnormality | Systemic manifestations are variable and may be gene- and family-specific (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| Pathology/biopsy | Skeletal muscle typically shows mitochondrial myopathy with ragged-red fibers, COX-negative fibers, and multiple mtDNA deletions (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, bermejoguerrero2021clinicalhistologicaland pages 6-7, bermejoguerrero2021clinicalhistologicaland pages 7-9) | In mitochondrial PEO series, biopsy showed mitochondrial changes in 95%; in TWNK cohort, all 19 available biopsies showed mitochondrial dysfunction and all 17 tested muscle samples had multiple mtDNA deletions (ali2024mitochondrialchronicprogressive pages 1-3, bermejoguerrero2021clinicalhistologicaland pages 7-9) | HP:0003200 Ragged-red muscle fibers; HP:0003688 Abnormal muscle mitochondria; GO:0006119 oxidative phosphorylation | 95% biopsy yield was for mixed mitochondrial PEO, not adPEO alone; deletion testing is tissue-sensitive (ali2024mitochondrialchronicprogressive pages 1-3) |
| Mechanism/pathophysiology | Upstream defects fall into mtDNA replication/repair, nucleotide supply/balance, and mitochondrial dynamics/quality control; downstream consequence is multiple mtDNA deletions causing respiratory-chain deficiency and energy failure in high-demand muscle (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) | Respiratory complex activities can range from normal to ~50% of control means in affected muscle (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) | GO:0006260 DNA replication; GO:0007005 mitochondrion organization; GO:0006091 generation of precursor metabolites and energy; CL:0000187 skeletal muscle cell | Mechanistic framework is established for mtDNA-maintenance disorders broadly; adPEO-specific omics and cell-type-resolved datasets were not identified (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| Electrophysiology/labs | EMG may show myopathic or mixed changes; CK and lactate can be normal or mildly elevated; GDF-15 may be elevated (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, bermejoguerrero2021clinicalhistologicaland pages 5-6, bermejoguerrero2021clinicalhistologicaland pages 6-7) | TWNK cohort: hyperCKemia 28%; mild hyperlactacidemia in 3/6 tested; GDF-15 elevated in 2/3 tested (1454–2727 pg/mL); EMG myopathic in 60%, neurogenic in 13%, normal in 27% of 15 tested (bermejoguerrero2021clinicalhistologicaland pages 5-6, bermejoguerrero2021clinicalhistologicaland pages 6-7) | LOINC/biomarkers: CK, lactate, GDF15; HP:0003236 Elevated serum creatine phosphokinase | Biomarker evidence is limited and from small tested subsets (bermejoguerrero2021clinicalhistologicaland pages 6-7) |
| Diagnosis | Current understanding supports sequencing-based diagnosis, complemented by muscle biopsy and mtDNA rearrangement analysis when suspicion remains high; in one mitochondrial PEO algorithm, biopsy was proposed as first step because it enables mtDNA rearrangement studies (ali2024mitochondrialchronicprogressive pages 1-3, bermejoguerrero2021clinicalhistologicaland pages 1-2) | Mixed mitochondrial PEO series achieved genetic diagnosis in 96%; biopsy informative in 95% (ali2024mitochondrialchronicprogressive pages 1-3) | NCIT: Genetic Testing; HP terms above; GO:0003723? not needed | These performance metrics are from all-cause mitochondrial PEO rather than strictly adPEO; practice has shifted toward broader NGS-first workflows in recent reviews (ali2024mitochondrialchronicprogressive pages 1-3, chen2023mitochondriaandthe pages 1-2) |
| Differential diagnosis | adPEO is commonly misdiagnosed as seronegative myasthenia gravis or oculopharyngeal muscular dystrophy (bermejoguerrero2021clinicalhistologicaland pages 1-2) | In TWNK cohort, 56% were misdiagnosed before genetic confirmation: 36% myasthenia, 20% oculopharyngeal muscular dystrophy (bermejoguerrero2021clinicalhistologicaland pages 1-2) | Differential ontology suggestions: HP:0000602 Ophthalmoplegia; disease comparators include myasthenia gravis and OPMD | Differential data derive from TWNK-related cases and specialist-center experience (bermejoguerrero2021clinicalhistologicaland pages 1-2) |
| Management | No definitive disease-modifying therapy is established; management is supportive, includes lifestyle/risk modification, supplements used empirically in mitochondrial care, ptosis repair, and monitoring for multisystem complications (ali2024mitochondrialchronicprogressive pages 1-3, ali2024mitochondrialchronicprogressive pages 18-19) | No adPEO-specific response rates were identified in retrieved evidence (ali2024mitochondrialchronicprogressive pages 18-19) | NCIT: Supportive Care; NCIT: Blepharoplasty/Ptosis Repair; NCIT: Physical Therapy | Do not extrapolate LHON gene-therapy efficacy to adPEO; retrieved therapeutic advances largely concern other mitochondrial phenotypes (ali2024mitochondrialchronicprogressive pages 18-19) |
| Real-world implementation / trials | Real-world care currently relies on diagnostic genomics and symptom-directed interventions; relevant mitochondrial/PEO trials exist but are not adPEO genotype-specific efficacy trials (clinical-trial contexts summarized in prior retrieval) | Examples retrieved: NCT02161848 observational MRI study in CPEO, enrollment 133, completed; NCT04678115 severe blepharoptosis non-surgical treatment trial, enrollment 16, completed; NCT05162768 phase 3 elamipretide in primary mitochondrial disease from nuclear DNA mutations, enrollment 102, completed | NCIT: Magnetic Resonance Imaging; NCIT: Elamipretide; NCIT: Blepharoptosis intervention | Trial records were not specific to autosomal dominant PEO and do not establish standard-of-care efficacy for adPEO |
| Epidemiology | Robust adPEO-specific prevalence/incidence estimates were not identified in the retrieved evidence | Only broader CPEO estimates were found: incidence 1–2 per 100,000 and prevalence ~1 in 30,000 or 3.4 per 100,000 in review sources (ali2024mitochondrialchronicprogressive pages 1-3, chen2023mitochondriaandthe pages 1-2) | MONDO/Orphanet term suggestion should await authoritative identifier confirmation | These figures apply to mitochondrial CPEO broadly, not specifically to autosomal dominant PEO; epidemiology remains a knowledge gap for the AD subtype (ali2024mitochondrialchronicprogressive pages 1-3, chen2023mitochondriaandthe pages 1-2) |


*Table: This table summarizes established, citable knowledge for autosomal dominant progressive external ophthalmoplegia, emphasizing what is supported directly for the AD subtype versus broader mitochondrial CPEO. It is useful for populating structured disease fields while preserving important scope caveats and evidence gaps.*

## 1. Disease information

### Definition and nomenclature

adPEO is usually a slowly progressive, adult-onset mitochondrial myopathy characterized by **bilateral ptosis and limitation of extraocular movements**, with secondary accumulation of multiple mtDNA deletions in post-mitotic tissues. “PEO-plus” denotes ophthalmoplegia accompanied by systemic manifestations such as proximal, neck, or bulbar weakness; exercise intolerance; neuropathy; ataxia; hearing loss; cataract; cardiac disease; or parkinsonism. The typical review-level onset range is approximately 20–40 years, although onset and severity vary considerably. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

Common names are **autosomal dominant progressive external ophthalmoplegia**, **autosomal dominant chronic progressive external ophthalmoplegia**, **adPEO**, **adCPEO**, **dominant PEO**, and, where systemic disease is present, **adPEO-plus/CPEO-plus**.

### Identifiers

* **OMIM phenotype:** the literature explicitly cites autosomal dominant PEO as **OMIM 157640**; individual gene-related phenotypes can also have separate OMIM entries.
* **MONDO:** a stable adPEO-specific MONDO identifier was not confirmed in the retrieved evidence; it should not be populated without direct MONDO verification. A broader progressive external ophthalmoplegia concept may be available.
* **Orphanet:** CPEO and autosomal-dominant PEO are represented in Orphanet’s mitochondrial-disease hierarchy, but an exact ORPHA number was not confirmed here.
* **ICD:** there is no highly specific, universally used ICD-10 code for genetically confirmed adPEO. Cases are generally coded under mitochondrial metabolism/myopathy or ophthalmoplegia categories. ICD-11 provides more granular mitochondrial-disease concepts, but local coding should be verified.
* **MeSH:** relevant concepts include *Ophthalmoplegia, Chronic Progressive External* and *Mitochondrial Myopathies*.

The report describes **aggregated disease-level evidence**, not an individual EHR. The TWNK statistics derive from a specialist laboratory/clinical cohort of individual patients subsequently aggregated for publication. (bermejoguerrero2021clinicalhistologicaland pages 2-4)

## 2. Etiology, risk, protection, and environment

### Primary cause

adPEO is caused by a **heterozygous germline pathogenic variant in a nuclear gene required for mtDNA replication, repair, nucleotide balance, or mitochondrial dynamics**. Established genes include **TWNK, POLG, POLG2, SLC25A4, DNA2, and RRM2B**. Dominant **OPA1** variants can produce an overlapping syndromic disorder with optic atrophy, PEO, deafness, ataxia, and multiple mtDNA deletions. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, kierdaszuk2020progressiveexternalophthalmoplegia pages 11-12)

The causal hierarchy is:

1. heterozygous nuclear variant;
2. defective mtDNA replication/maintenance or nucleotide homeostasis;
3. progressive formation and clonal expansion of multiple mtDNA deletions;
4. mosaic respiratory-chain deficiency;
5. ATP failure in high-demand, long-lived cells;
6. extraocular and skeletal-muscle dysfunction, with variable multisystem disease.

### Risk factors

* **Genetic:** an affected parent, a pathogenic heterozygous allele, and increasing age are the major established risk determinants. In the TWNK cohort, 22/25 patients (88%) had a first-degree relative with ptosis and/or ophthalmoplegia. (bermejoguerrero2021clinicalhistologicaland pages 2-4)
* **Age:** deletion burden and clinical manifestations generally increase with age; presymptomatic carriers may have subclinical biochemical abnormalities. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)
* **Sex:** no established biological sex predisposition exists. The TWNK cohort was 64% female, but this small referral cohort cannot establish a sex ratio. (bermejoguerrero2021clinicalhistologicaland pages 2-4)
* **Environmental/infectious:** no toxin, infection, occupational exposure, diet, smoking behavior, or lifestyle factor is known to cause Mendelian adPEO.

### Protective factors and gene–environment interaction

No validated protective variant, diet, drug, or behavioral intervention prevents adPEO. Avoidance of mitochondrial stressors is prudent clinical practice but is not demonstrated primary prevention. Potentially mitochondrion-toxic drugs and prolonged metabolic stress may aggravate mitochondrial symptoms generally, but a quantified adPEO-specific gene–environment interaction has not been established. No infectious trigger is implicated.

## 3. Phenotypes

### Core and systemic manifestations

| Phenotype | Type/course | Direct TWNK-adPEO frequency | Suggested HPO term |
|---|---|---:|---|
| Ptosis, generally bilateral | Sign; insidious, progressive; mild to severe | 92% | **HP:0000508** |
| External ophthalmoplegia/ophthalmoparesis | Sign; usually symmetric and progressive | 80% | **HP:0000602** |
| Skeletal-muscle weakness | Sign; proximal, neck, facial, or bulbar; progressive/variable | 48% | **HP:0001324** |
| Exercise intolerance/fatigue | Symptom; chronic | 28% | **HP:0003546** |
| Bulbar weakness/dysphagia/dysphonia | Symptom/sign; variable | 24% | **HP:0002015**, HP:0001618 |
| Cardiac abnormality | Sign; variable, clinically important | 24% | **HP:0011675** or finding-specific term |
| Peripheral neuropathy | Sign; variable | 8% | **HP:0009830** |
| Respiratory involvement | Sign; uncommon in this cohort | 4% | **HP:0002795** |
| Ataxia | Sign | 4% | **HP:0001251** |
| Parkinsonism | Sign | 4% | **HP:0001300** |
| Cataract | Sign; two related subjects, ages 48 and 50 | 2 patients | **HP:0000518** |
| Mild CK elevation | Laboratory abnormality | 28% | **HP:0003236** |

These percentages are from 25 individuals with TWNK variants and should not be treated as universal frequencies for POLG-, POLG2-, SLC25A4-, DNA2-, RRM2B-, or OPA1-related disease. (bermejoguerrero2021clinicalhistologicaland pages 5-6, bermejoguerrero2021clinicalhistologicaland pages 1-2)

Additional reported adPEO-spectrum manifestations include sensorineural hearing loss, facial weakness, hypogonadism, psychiatric abnormalities, gastrointestinal dysmotility, and cataracts. OPA1-related “DOA-plus” particularly suggests optic atrophy and hearing loss. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 13-14)

### Quality of life

Ptosis can obstruct the visual axis, fixed ophthalmoplegia restricts gaze, and weakness, dysphagia, fatigue, neuropathy, or hearing loss can limit mobility, work, communication, and participation. Robust adPEO-specific EQ-5D, SF-36, PROMIS, survival, and disability-transition estimates were not identified. Accordingly, quality-of-life impact is clinically credible but insufficiently quantified by genotype.

## 4. Genetic and molecular information

### Genes and functional classes

* **TWNK** encodes the mitochondrial replicative helicase. Dominant missense variants impair helicase function, stall replication, and produce multiple mtDNA deletions.
* **POLG** encodes the catalytic polymerase-γ subunit; dominant variants can alter polymerase, proofreading, or replisome function.
* **POLG2** encodes the accessory polymerase-γ subunit.
* **SLC25A4/ANT1** encodes the muscle-predominant mitochondrial ADP/ATP carrier and influences nucleotide/energy homeostasis.
* **DNA2** participates in mtDNA replication/repair and flap processing.
* **RRM2B** supports deoxyribonucleotide production in non-dividing cells.
* **OPA1** controls inner-membrane fusion/cristae organization and, in dominant syndromic disease, indirectly compromises mtDNA maintenance.

These proteins converge on mtDNA replication/maintenance despite performing different proximal functions. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Variant evidence

In the TWNK cohort, all variants were heterozygous missense substitutions in exons 1–2. Ten variants were found: **c.1361T>G (p.Val454Gly)** occurred in seven patients from six families; **c.1070G>C (p.Arg357Pro)** in seven patients from five families; **c.1121G>A (p.Arg374Gln)** in three patients; and **c.1411T>G (p.Tyr471Asp)** in two siblings. All 17 tested muscle samples contained multiple mtDNA deletions. (bermejoguerrero2021clinicalhistologicaland pages 7-9)

Variants should be classified individually under ACMG/AMP criteria using ClinVar/ClinGen evidence, segregation, functional data, phenotype specificity, and population frequency. Disease association alone does not make every rare variant pathogenic. Causal alleles are germline; secondary mtDNA deletions arise somatically and clonally in affected tissues. Pathogenic dominant alleles are generally absent or extremely rare in population databases, but no single allele-frequency threshold is valid for every gene or variant.

### Modifiers, epigenetics, and chromosome abnormalities

No reproducible modifier gene, protective allele, disease-specific methylation signature, histone alteration, or recurrent chromosomal rearrangement is established for adPEO. Conventional aneuploidy or translocation is not the characteristic lesion. The clinically relevant structural abnormalities are **multiple mtDNA deletions**, not a nuclear karyotypic defect.

Suggested annotations include **SO:0001583 missense_variant**, GO:0006260 DNA replication, GO:0006281 DNA repair, GO:0007005 mitochondrion organization, and GO:0006119 oxidative phosphorylation.

## 5. Environmental information

adPEO is not infectious, contagious, toxic, or environmentally acquired. No causal association with pollution, radiation, smoking, alcohol, occupation, or a specific diet has been demonstrated. Lifestyle measures—adequate nutrition, avoidance of prolonged fasting/dehydration, appropriately paced aerobic activity, and avoidance of unnecessary mitochondrial-toxic exposures—are supportive rather than curative or preventive. Vaccination has no disease-specific etiologic role, although routine immunization is appropriate.

## 6. Mechanism and pathophysiology

### Upstream pathways

The principal upstream modules are **mtDNA replication/repair** (TWNK, POLG, POLG2, DNA2), **nucleotide supply/balance** (RRM2B and indirectly SLC25A4), and **mitochondrial dynamics/quality control** (OPA1). A major review summarizes mtDNA-maintenance disorders as involving “mtDNA replication and maintenance, nucleotide supply and balance, and mitochondrial dynamics and quality control.” (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Downstream cellular injury

Multiple deletions remove mtDNA genes encoding respiratory-chain subunits and RNAs. Deletion burden varies among fibers, producing a mosaic of cytochrome-c-oxidase-negative cells. Respiratory-chain activities may range from normal to approximately 50% of control means, explaining why blood biomarkers can be normal despite muscle disease. Energy failure and compensatory mitochondrial proliferation produce ragged-red fibers; extraocular muscles are particularly vulnerable because of sustained activity and high mitochondrial demand. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

Suggested terms:

* **GO biological process:** GO:0006260 mitochondrial-DNA replication; GO:0006119 oxidative phosphorylation; GO:0007005 mitochondrion organization; GO:0006091 generation of precursor metabolites and energy.
* **GO cellular component:** **GO:0005739 mitochondrion**, GO:0005743 mitochondrial inner membrane, GO:0005759 mitochondrial matrix, GO:0005758 mitochondrial intermembrane space.
* **Cell Ontology:** **CL:0000187 skeletal muscle cell**; extraocular myofiber-specific annotations may require anatomy plus skeletal-muscle-cell terms.
* **Metabolic consequence:** impaired ATP production, variable lactate elevation, and compensatory mitochondrial biogenesis.

No primary autoimmune mechanism is established. Oxidative stress may be downstream of respiratory dysfunction, but chronic inflammation is not considered the initiating pathology.

### Molecular profiling and advanced technologies

Routine pathology and bulk biochemical/genomic testing dominate the evidence base. No validated adPEO-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omics diagnostic signature was identified. GDF-15 is promising as a general mitochondrial biomarker but not specific to adPEO: it was elevated in 2/3 tested TWNK patients at 1,454–2,727 pg/mL. (bermejoguerrero2021clinicalhistologicaland pages 6-7)

## 7. Anatomical structures affected

The primary structures are the **extraocular muscles** and **levator palpebrae superioris**, generally bilaterally and relatively symmetrically. Other skeletal muscles—proximal limb, cervical, facial, pharyngeal, and respiratory muscles—can be involved. Secondary sites vary by genotype and can include peripheral nerves, cochlea/auditory pathways, optic nerve, basal ganglia/cerebellar pathways, gastrointestinal smooth muscle/enteric nervous system, and heart. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

Suggested anatomy terms include **UBERON:0001135 skeletal muscle tissue**, UBERON extraocular-muscle and eyelid terms after database verification, and organ-specific terms for heart, peripheral nerve, optic nerve, and cochlea. At the subcellular level, mitochondria—especially matrix replisomes and inner-membrane OXPHOS machinery—are central.

## 8. Temporal development

adPEO is typically insidious and chronic. Review literature places usual onset around 20–40 years; broader mitochondrial CPEO has a reported mean onset around 29 years. In the TWNK series, 80% began at age ≥18, mean onset was 43 years, and mean molecular diagnosis was 63 years—a roughly 20-year average diagnostic gap. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, chen2023mitochondriaandthe pages 1-2, bermejoguerrero2021clinicalhistologicaland pages 1-2)

A practical trajectory is:

1. subtle asymmetric or bilateral ptosis;
2. gradually restricted ocular motility, often with limited diplopia because progression is symmetric;
3. neck/proximal weakness or exercise intolerance;
4. variable PEO-plus manifestations later in life.

There are no validated formal stages, predictable annual progression rate, spontaneous remission pattern, or defined end-stage. Disease is lifelong and generally progressive. Critical opportunities are early genetic diagnosis, surveillance before cardiac/respiratory complications, and ptosis management before visual-axis obstruction or compensatory head posture becomes disabling.

## 9. Inheritance and population

Inheritance is autosomal dominant: an affected heterozygous individual generally has a **50% transmission probability per pregnancy**, independent of sex. Expressivity is markedly variable and penetrance is likely age-dependent, but robust gene- and variant-specific penetrance estimates are unavailable. Anticipation is not established. Germline mosaicism is biologically possible but not a defining feature; consanguinity is not relevant to dominant transmission. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, kierdaszuk2020progressiveexternalophthalmoplegia pages 11-12)

adPEO-specific incidence, prevalence, carrier frequency, ethnic enrichment, geographic distribution, and sex ratio remain inadequately characterized. Broader CPEO estimates—**1–2 per 100,000 incidence**, approximately **1 in 30,000 prevalence**, or **3.4 per 100,000**—must not be interpreted as adPEO-specific. (ali2024mitochondrialchronicprogressive pages 1-3, chen2023mitochondriaandthe pages 1-2)

No universal founder allele was established. Recurrent TWNK variants in a Spanish cohort may reflect referral or ancestry patterns; their cohort frequencies are not population frequencies. (bermejoguerrero2021clinicalhistologicaland pages 7-9)

## 10. Diagnostics

### Clinical and laboratory approach

Clinical suspicion is raised by slowly progressive bilateral ptosis and ophthalmoparesis, especially with an autosomal-dominant pedigree or proximal/bulbar weakness. Examination should document eyelid position, Bell phenomenon, corneal exposure, ocular ductions, diplopia, visual acuity, fundus/optic nerve, hearing, bulbar function, strength, gait, neuropathy, and systemic involvement.

CK and lactate may be normal or mildly elevated. In the TWNK cohort, mild hyperCKemia occurred in 28%; mild hyperlactacidemia in 3/6 tested; EMG was myopathic in 9/15 (60%), neurogenic in 2/15 (13%), and normal in 4/15 (27%). Brain and muscle imaging were often normal or nonspecific. (bermejoguerrero2021clinicalhistologicaland pages 5-6, bermejoguerrero2021clinicalhistologicaland pages 6-7)

### Genetic testing strategy

1. Use a **mitochondrial disease/PEO nuclear-gene panel** including at least TWNK, POLG, POLG2, SLC25A4, DNA2, RRM2B, OPA1 and relevant recessive genes.
2. Concurrently or reflexively assess mtDNA for point variants, single deletions, and multiple deletions.
3. If blood is nondiagnostic, test a clinically affected tissue—usually skeletal muscle—because secondary deletions can be tissue-restricted.
4. Use WES/WGS when panel testing is negative; WGS may improve detection of nuclear structural/noncoding variants and mtDNA abnormalities, but tissue and analytic validation remain important.
5. Perform segregation testing in relatives and interpret variants under ACMG/AMP standards.

CMA, karyotyping, FISH, and repeat-expansion testing have low first-line yield unless another diagnosis is suspected. RNA sequencing may clarify splice variants but is not routine. Prenatal and preimplantation testing require a known familial pathogenic nuclear variant.

### Biopsy and pathology

Muscle shows ragged-red fibers, subsarcolemmal mitochondrial accumulation, COX-negative fibers, and sometimes neurogenic changes. All 19 biopsied patients in the TWNK cohort had mitochondrial abnormalities; all 17 tested had multiple mtDNA deletions. In a mixed 89-patient mitochondrial PEO series, biopsy showed mitochondrial changes in 95% and molecular diagnosis was reached in 96%. Those mixed-cohort performance estimates should not be assigned specifically to adPEO. (bermejoguerrero2021clinicalhistologicaland pages 7-9, ali2024mitochondrialchronicprogressive pages 1-3)

### Differential diagnosis

Important alternatives are myasthenia gravis, oculopharyngeal muscular dystrophy, congenital myasthenic syndromes, thyroid eye disease, orbital disease, cranial neuropathies, myotonic dystrophy, and other mitochondrial PEO etiologies. In the TWNK cohort, 56% were initially misdiagnosed—36% as myasthenia and 20% as oculopharyngeal muscular dystrophy—showing the real-world value of early molecular testing. (bermejoguerrero2021clinicalhistologicaland pages 1-2)

## 11. Outcome and prognosis

adPEO commonly causes chronic visual-functional and neuromuscular morbidity but isolated ocular disease is not usually directly fatal. Prognosis depends on PEO-plus involvement, particularly cardiac conduction disease/cardiomyopathy, respiratory weakness, dysphagia/aspiration, severe neuropathy, and central neurologic disease. No reliable adPEO-specific 5- or 10-year survival, mortality rate, or life-expectancy estimate was found.

Recovery of lost extraocular movement is not expected with current care. Ptosis and diplopia can be palliated, and rehabilitation may preserve function, but treatment does not remove the causal nuclear variant or accumulated mtDNA deletions. No validated molecular prognostic biomarker exists; genotype, age, deletion burden in muscle, respiratory-chain deficiency, cardiac involvement, dysphagia, and respiratory function are plausible clinical prognostic variables.

## 12. Treatment and current implementation

There is **no approved disease-modifying therapy specifically for adPEO**. The 2024 review states that “No definitive treatment option is available for mitochondrial diseases,” with management focused on lifestyle measures, supplements, and symptomatic relief such as ptosis repair. (ali2024mitochondrialchronicprogressive pages 1-3)

### Symptomatic and supportive care

* **Ptosis:** lubricants and exposure prevention; ptosis crutch or eyelid tape in selected patients; cautious levator advancement or frontalis suspension. Surgery must account for poor Bell phenomenon and risk of exposure keratopathy. Suggested NCIT concepts: *Supportive Care*, *Blepharoplasty/Ptosis Repair*.
* **Diplopia/ophthalmoplegia:** prisms when deviation is suitable; selected strabismus surgery, with counseling that progression can alter alignment.
* **Myopathy/fatigue:** individualized submaximal aerobic/resistance exercise, physiotherapy, pacing, and fall prevention. NCIT: *Physical Therapy*, *Exercise Therapy*.
* **Dysphagia:** speech/swallow assessment, dietary modification, and aspiration prevention; enteral feeding if severe. In the TWNK cohort, no patient required enteral nutrition despite bulbar involvement. (bermejoguerrero2021clinicalhistologicaland pages 5-6)
* **Hearing/vision:** hearing aids or cochlear assessment; low-vision support where optic or retinal disease occurs.
* **Cardiac/respiratory:** ECG, echocardiographic and rhythm surveillance; pulmonary-function and sleep assessment when indicated; standard specialist treatment.

Coenzyme Q10, riboflavin, antioxidants, and other “mitochondrial cocktails” are often used empirically, but no adPEO-specific response rate or high-quality efficacy evidence was identified. Pharmacogenomic dosing guidance is not established.

### Trials and advanced therapy

Relevant but nonspecific studies include **NCT02161848**, an observational MRI study in CPEO (completed; 133 participants); **NCT04678115**, a completed 16-participant trial of nonsurgical approaches for severe blepharoptosis; and **NCT05162768**, a completed phase III study of elamipretide in nuclear-DNA primary mitochondrial disease (102 participants). These records do not establish genotype-specific efficacy or standard-of-care use in adPEO.

Gene replacement/editing is conceptually more tractable for nuclear adPEO than for primary mtDNA mutations, but no approved TWNK-, POLG-, POLG2-, SLC25A4-, DNA2-, or RRM2B-directed gene therapy exists. LHON ND4 gene-therapy results and mitochondrial augmentation studies concern other disorders and should not be extrapolated to adPEO. (ali2024mitochondrialchronicprogressive pages 18-19)

## 13. Prevention

Primary prevention by lifestyle or medication is not currently possible. The principal preventive intervention is **genetic counseling**: molecular confirmation, cascade testing of adult relatives, and discussion of the 50% transmission risk. If a familial pathogenic variant is known, prenatal diagnosis and PGT-M are technically possible; reproductive decisions require nondirective counseling because penetrance and severity can be variable.

Secondary prevention consists of identifying presymptomatic carriers and detecting cardiac, respiratory, hearing, swallowing, visual, or neurologic complications early. Tertiary prevention includes fall and aspiration prevention, corneal protection, paced exercise, hearing support, and timely cardiac/respiratory care. Population newborn screening, vaccination, antimicrobial prophylaxis, and public-health environmental control are not disease-specific interventions.

## 14. Other species and natural disease

No well-established naturally occurring veterinary disorder directly equivalent to human adPEO was identified. Thus, breed prevalence, VBO identifiers, animal incidence, and veterinary management cannot currently be populated reliably. The disease is noninfectious and has no zoonotic or cross-species transmission potential.

The implicated genes are evolutionarily conserved across mammals and many eukaryotes, particularly POLG, TWNK, OPA1, and adenine nucleotide translocators. Conservation permits functional modeling, but orthologous-gene presence does not imply naturally occurring clinical adPEO.

## 15. Model organisms

Experimental systems include engineered **mouse models** affecting Twinkle, Polg, Slc25a4/Ant1, or Opa1; patient fibroblasts/myoblasts; transmitochondrial or cybrid systems; and **Saccharomyces cerevisiae** models of conserved mitochondrial maintenance genes. Twinkle mutants can reproduce replication stalling and progressive multiple-deletion/respiratory-chain pathology; polymerase-γ models interrogate replication fidelity and age-related mtDNA mutation accumulation.

Yeast is useful for rapid functional validation and phenotype-based drug screening because its mitochondrial biogenesis and metabolism are experimentally tractable. A 2023 review emphasizes that yeast has been used both “to validate alleged pathogenic variants” and to identify potentially beneficial molecules, although yeast lacks extraocular muscles and cannot reproduce the complete human phenotype.

Model limitations include species-specific eye-muscle physiology, differences in mtDNA replication and lifespan, severe phenotypes in some knockouts that do not match heterozygous adult disease, and failure of cultured cells to reproduce age-dependent clonal deletion expansion. Relevant resources include MGI, IMPC, IMSR, SGD, Cellosaurus, and the Alliance of Genome Resources.

## Key recent and primary sources

* **Ali A, Esmaeil A, Behbehani R.** “Mitochondrial Chronic Progressive External Ophthalmoplegia.” *Brain Sciences*. Published January 2024. DOI: https://doi.org/10.3390/brainsci14020135. Abstract: “Genetic sequencing is the gold standard for diagnosing mitochondrial encephalomyopathies…” (ali2024mitochondrialchronicprogressive pages 1-3)
* **Chen BS et al.** “Mitochondria and the eye—manifestations of mitochondrial diseases and their management.” *Eye*. Published April 2023. DOI: https://doi.org/10.1038/s41433-023-02523-x. The abstract notes that genotype–phenotype correlations “can be imprecise.” (chen2023mitochondriaandthe pages 1-2)
* **Bermejo-Guerrero L et al.** “Clinical, Histological, and Genetic Features of 25 Patients with Autosomal Dominant Progressive External Ophthalmoplegia (ad-PEO)/PEO-Plus Due to TWNK Mutations.” *Journal of Clinical Medicine*. Published December 2021. DOI: https://doi.org/10.3390/jcm11010022. The abstract reports mean onset at 43 years, diagnosis at 63 years, ptosis in 92%, PEO in 80%, and prior misdiagnosis in 56%. (bermejoguerrero2021clinicalhistologicaland pages 1-2)
* **Rodríguez-López C et al.** “Clinical, pathological and genetic spectrum in 89 cases of mitochondrial progressive external ophthalmoplegia.” *Journal of Medical Genetics*. Published March 2020. DOI: https://doi.org/10.1136/jmedgenet-2019-106649. The abstract reports “pure PEO” in 42%, mitochondrial biopsy changes in 95%, and genetic diagnosis in 96%; this was a mixed-etiology PEO cohort. (ali2024mitochondrialchronicprogressive pages 1-3)
* **Viscomi C, Zeviani M.** “MtDNA-maintenance defects: syndromes and genes.” *Journal of Inherited Metabolic Disease*. Published March 2017. DOI: https://doi.org/10.1007/s10545-017-0027-5. Its abstract states that these disorders can cause “mtDNA depletion, accumulation of mtDNA multiple deletions, or both.” (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

## Principal knowledge gaps

The most important unresolved fields are adPEO-specific prevalence and incidence, gene- and variant-specific penetrance, longitudinal progression rates, standardized patient-reported outcomes, validated prognostic biomarkers, environmental modifiers, cell-resolved multi-omics, and controlled genotype-specific treatment trials. Broader CPEO or mitochondrial-disease findings should remain separately annotated until directly validated in autosomal-dominant mtDNA-maintenance PEO.

References

1. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4): Carlo Viscomi and Massimo Zeviani. Mtdna-maintenance defects: syndromes and genes. Journal of Inherited Metabolic Disease, 40:587-599, Mar 2017. URL: https://doi.org/10.1007/s10545-017-0027-5, doi:10.1007/s10545-017-0027-5. This article has 226 citations and is from a peer-reviewed journal.

2. (bermejoguerrero2021clinicalhistologicaland pages 1-2): Laura Bermejo-Guerrero, Carlos Pablo de Fuenmayor-Fernández de la Hoz, Pablo Serrano-Lorenzo, Alberto Blázquez-Encinar, Gerardo Gutiérrez-Gutiérrez, Laura Martínez-Vicente, Lucía Galán-Dávila, Jorge García-García, Joaquín Arenas, Nuria Muelas, Aurelio Hernández-Laín, Cristina Domínguez-González, and Miguel A. Martín. Clinical, histological, and genetic features of 25 patients with autosomal dominant progressive external ophthalmoplegia (ad-peo)/peo-plus due to twnk mutations. Journal of Clinical Medicine, 11:22, Dec 2021. URL: https://doi.org/10.3390/jcm11010022, doi:10.3390/jcm11010022. This article has 12 citations.

3. (ali2024mitochondrialchronicprogressive pages 1-3): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

4. (chen2023mitochondriaandthe pages 1-2): Benson S. Chen, Joshua P. Harvey, Michael J. Gilhooley, Neringa Jurkute, and Patrick Yu-Wai-Man. Mitochondria and the eye—manifestations of mitochondrial diseases and their management. Eye, 37:2416-2425, Apr 2023. URL: https://doi.org/10.1038/s41433-023-02523-x, doi:10.1038/s41433-023-02523-x. This article has 44 citations and is from a peer-reviewed journal.

5. (kierdaszuk2020progressiveexternalophthalmoplegia pages 11-12): Biruta Kierdaszuk, Magdalena Kaliszewska, Joanna Rusecka, Joanna Kosińska, Ewa Bartnik, Katarzyna Tońska, Anna M. Kamińska, and Anna Kostera-Pruszczyk. Progressive external ophthalmoplegia in polish patients—from clinical evaluation to genetic confirmation. Genes, 12:54, Dec 2020. URL: https://doi.org/10.3390/genes12010054, doi:10.3390/genes12010054. This article has 6 citations.

6. (bermejoguerrero2021clinicalhistologicaland pages 2-4): Laura Bermejo-Guerrero, Carlos Pablo de Fuenmayor-Fernández de la Hoz, Pablo Serrano-Lorenzo, Alberto Blázquez-Encinar, Gerardo Gutiérrez-Gutiérrez, Laura Martínez-Vicente, Lucía Galán-Dávila, Jorge García-García, Joaquín Arenas, Nuria Muelas, Aurelio Hernández-Laín, Cristina Domínguez-González, and Miguel A. Martín. Clinical, histological, and genetic features of 25 patients with autosomal dominant progressive external ophthalmoplegia (ad-peo)/peo-plus due to twnk mutations. Journal of Clinical Medicine, 11:22, Dec 2021. URL: https://doi.org/10.3390/jcm11010022, doi:10.3390/jcm11010022. This article has 12 citations.

7. (bermejoguerrero2021clinicalhistologicaland pages 7-9): Laura Bermejo-Guerrero, Carlos Pablo de Fuenmayor-Fernández de la Hoz, Pablo Serrano-Lorenzo, Alberto Blázquez-Encinar, Gerardo Gutiérrez-Gutiérrez, Laura Martínez-Vicente, Lucía Galán-Dávila, Jorge García-García, Joaquín Arenas, Nuria Muelas, Aurelio Hernández-Laín, Cristina Domínguez-González, and Miguel A. Martín. Clinical, histological, and genetic features of 25 patients with autosomal dominant progressive external ophthalmoplegia (ad-peo)/peo-plus due to twnk mutations. Journal of Clinical Medicine, 11:22, Dec 2021. URL: https://doi.org/10.3390/jcm11010022, doi:10.3390/jcm11010022. This article has 12 citations.

8. (ali2024mitochondrialchronicprogressive pages 13-14): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

9. (bermejoguerrero2021clinicalhistologicaland pages 5-6): Laura Bermejo-Guerrero, Carlos Pablo de Fuenmayor-Fernández de la Hoz, Pablo Serrano-Lorenzo, Alberto Blázquez-Encinar, Gerardo Gutiérrez-Gutiérrez, Laura Martínez-Vicente, Lucía Galán-Dávila, Jorge García-García, Joaquín Arenas, Nuria Muelas, Aurelio Hernández-Laín, Cristina Domínguez-González, and Miguel A. Martín. Clinical, histological, and genetic features of 25 patients with autosomal dominant progressive external ophthalmoplegia (ad-peo)/peo-plus due to twnk mutations. Journal of Clinical Medicine, 11:22, Dec 2021. URL: https://doi.org/10.3390/jcm11010022, doi:10.3390/jcm11010022. This article has 12 citations.

10. (bermejoguerrero2021clinicalhistologicaland pages 6-7): Laura Bermejo-Guerrero, Carlos Pablo de Fuenmayor-Fernández de la Hoz, Pablo Serrano-Lorenzo, Alberto Blázquez-Encinar, Gerardo Gutiérrez-Gutiérrez, Laura Martínez-Vicente, Lucía Galán-Dávila, Jorge García-García, Joaquín Arenas, Nuria Muelas, Aurelio Hernández-Laín, Cristina Domínguez-González, and Miguel A. Martín. Clinical, histological, and genetic features of 25 patients with autosomal dominant progressive external ophthalmoplegia (ad-peo)/peo-plus due to twnk mutations. Journal of Clinical Medicine, 11:22, Dec 2021. URL: https://doi.org/10.3390/jcm11010022, doi:10.3390/jcm11010022. This article has 12 citations.

11. (ali2024mitochondrialchronicprogressive pages 18-19): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Progressive_External_Ophthalmoplegia-deep-research-falcon_artifacts/artifact-00.md)