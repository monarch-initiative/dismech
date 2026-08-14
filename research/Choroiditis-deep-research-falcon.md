---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T08:40:28.008386'
end_time: '2026-08-01T08:48:31.396231'
duration_seconds: 483.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Choroiditis
  mondo_id: ''
  category: Immune
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
  path: Choroiditis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Choroiditis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Choroiditis** covering all of the
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
- **Disease Name:** Choroiditis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Choroiditis** covering all of the
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


# Choroiditis: disease-characteristics research report

## Executive interpretation

**Choroiditis is not one etiologically uniform disease.** It is an anatomic/pathologic term for inflammation centered in the choroid, usually classified clinically under **posterior uveitis** and often accompanied by retinal inflammation, hence *chorioretinitis* or *retinochoroiditis*. Named entities include infectious toxoplasma or tubercular choroiditis and immune-mediated birdshot chorioretinopathy, multifocal choroiditis, punctate inner choroidopathy (PIC), serpiginous choroiditis, and Vogt–Koyanagi–Harada (VKH) disease. Etiology, genetics, laterality, course, treatment, and prognosis must therefore be represented at subtype level rather than assigned indiscriminately to “choroiditis.” A 2023 expert review similarly describes posterior uveitis as a broad spectrum of infectious, autoimmune, drug-related, systemic, and masquerading diseases (paezescamilla2023challengesinposterior pages 1-2).

| Domain/subtype | Strongest quantitative finding | Evidence type and year | Source DOI or NCT |
|---|---|---|---|
| Choroiditis umbrella / posterior uveitis context | Posterior/infectious inflammatory disorders are vision-threatening and epidemiologically heterogeneous; in a 30-year Greek tertiary cohort, 6,191 uveitis cases included 1,925 infectious, 4,125 non-infectious, and 141 masquerade syndromes (kalogeropoulos2023thelargehellenic pages 1-2) | Observational cohort, 2023 | https://doi.org/10.1007/s10792-023-02772-5 |
| Birdshot chorioretinopathy (epidemiology) | Accounts for 0.6–1.5% of uveitis cases at tertiary centers, 5–8% of posterior uveitis, with estimated prevalence 0.1–0.6/100,000; mean onset ~53 years (bousquet2022birdshotchorioretinopathya pages 1-2) | Review of clinical literature, 2022 | https://doi.org/10.3390/jcm11164772 |
| Birdshot chorioretinopathy (core HLA association) | >95% of patients carry HLA-A29; reported OR 157.5 for HLA-A29 association (gelfman2021erap1erap2and pages 1-2) | Human genetic association study, 2021 | https://doi.org/10.1167/iovs.62.14.3 |
| Birdshot chorioretinopathy (ERAP/HLA modifiers) | ERAP1-rs27432 OR 2.46 (95% CI 1.85–3.26), ERAP2-rs10044354 OR 1.95 (1.55–2.44), protective ERAP2-rs2248374 OR 0.56 (0.45–0.70); combined ERAP1/2 risk genotypes + two HLA-Aw19 alleles OR 13.53 (3.79–54.77) (gelfman2021erap1erap2and pages 1-2) | Human genetic association/meta-analysis, 2021 | https://doi.org/10.1167/iovs.62.14.3 |
| Birdshot chorioretinopathy (2024 HLA-A29 homozygosity/protection) | Second HLA-A29 allele overrepresented in cases vs HLA-A29-positive controls: OR 1.57 (95% CI 1.01–2.44); HLA-A32 under-represented/protective: OR 0.40 (0.19–0.85); no severity effect detected (loeliger2024theimpactof pages 1-2) | Human genetic association study, 2024 | https://doi.org/10.1167/iovs.65.13.47 |
| Ocular toxoplasmosis / toxoplasma retinochoroiditis | In 92 patients (95 eyes), 21% had VA ≤20/200 at final visit; 3-year recurrence 33.9% (95% CI 19.7–54.2%); poor 6-month VA ≤20/50 associated with immunocompromise aOR 4.9, macular lesion aOR 5.4, initial VA ≤20/200 aOR 9.1 (sittivarakul2024clinicalcharacteristicsvisual pages 1-2, sittivarakul2024clinicalcharacteristicsvisual pages 13-14) | Retrospective clinical cohort, 2024 | https://doi.org/10.1371/journal.pntd.0012232 |
| Ocular toxoplasmosis (recurrence biology/clinical risk) | Contralateral-eye recurrence reported as 40% when bilateral retinal scars are present versus 4% in unaffected eyes; pregnancy-related recurrence estimates vary (IRR 0.54–0.75 in some studies, 7.4-fold increase in another) (miyagaki2024oculartoxoplasmosisadvances pages 14-15) | Review, 2024 | https://doi.org/10.3390/pathogens13100898 |
| Hellenic uveitis etiologies relevant to choroiditis differential | Of all 6,191 cases, 24.2% were linked to 4 microorganisms; most common infectious causes were herpetic uveitis 14.87%, toxoplasmosis 6.6%, tuberculosis 2.74%; 49.2% of non-infectious cases had no systemic correlation (kalogeropoulos2023thelargehellenic pages 1-2) | Observational cohort, 2023 | https://doi.org/10.1007/s10792-023-02772-5 |
| Human intraocular immune mechanisms | In aqueous fluid, 6 chemokines were elevated and enriched in active uveitis; CCL2 and CXCL10 were consistently enriched across patients, and single-cell RNA-seq implicated macrophages as a key source (lin2024aqueousmacrophagescontribute pages 1-2) | Single-cell + protein profiling study, 2024 | https://doi.org/10.1016/j.xops.2023.100453 |
| Systems proteomics / biomarker discovery | 3,668 proteins identified and >3,000 quantified from 278 samples; EV proteomes correlated with disease better than plasma, with disease-specific biomarker panels validated (wu2023comprehensiveprofilingof pages 1-2) | Proteomics biomarker study, 2023 | https://doi.org/10.1186/s12967-023-04228-x |
| Trial: Birdshot treatment | Randomized phase 2 BIRDFERON trial in birdshot chorioretinopathy with macular edema; enrollment 58; compared interferon alfa-2a vs prednisone; primary endpoint: decrease in OCT macular-center thickness over 4 months (NCT00508040 chunk 1) | Interventional trial record, 2007–2013 | NCT00508040 |
| Trial: Ocular toxoplasmosis recurrence prevention | Randomized triple-masked phase 3 ISROT trial; enrollment 141; after acute TMP-SMX treatment, prophylaxis used TMP-SMX every other day for 311 days vs placebo, with recurrence followed to 120 months (NCT01449877 chunk 1) | Interventional trial record, 2011–2016 | NCT01449877 |
| Trial: Tubercular posterior uveitis/choroiditis | Randomized phase 4 non-inferiority trial; enrollment 58; compared 6 vs 9 months anti-TB therapy for tubercular posterior uveitis/choroiditis; primary endpoint: non-recurrence of inflammation 1 year after ATT completion (NCT06613919 chunk 1) | Interventional trial record, 2024 posting | NCT06613919 |


*Table: This table summarizes key quantitative evidence for choroiditis as a heterogeneous umbrella syndrome, spanning immune and infectious subtypes, mechanisms, and clinical trials. It is useful for quickly identifying the strongest current numbers and the exact source records behind them.*

## 1. Disease information

### Definition and classification

The choroid is the vascular, pigmented posterior component of the uveal tract. Choroiditis denotes inflammatory infiltration or injury of this tissue; adjacent retinal, retinal-pigment-epithelial (RPE), vitreous, retinal vascular, and optic-disc involvement is common. In the Standardization of Uveitis Nomenclature framework, lesions centered primarily in the retina/choroid constitute posterior uveitis; simultaneous anterior, intermediate, and posterior inflammation is panuveitis.

**Common names:** choroiditis; posterior uveitis with choroidal involvement; chorioretinitis; retinochoroiditis; disseminated/multifocal choroiditis. “Central serous chorioretinopathy” is not ordinarily an inflammatory choroiditis and should not be merged with this entity.

**Identifiers and coding:**

- **MeSH:** Choroiditis, **D002833**; related terms include Posterior Uveitis and Chorioretinitis. The MeSH identifier is explicitly present in ClinicalTrials.gov-derived indexing (NCT00508040 chunk 1, NCT06613919 chunk 1).
- **ICD-10-CM:** principally **H30.-, Chorioretinal inflammation**, with subtype and laterality extensions; coding should use the most specific clinical diagnosis.
- **MONDO/OMIM/Orphanet:** no single disease-level record should be assumed for the umbrella term. Named subtypes may have individual ontology entries. **No OMIM disease or Mendelian inheritance model is appropriate for nonspecific choroiditis.** A MONDO identifier was not verified in the retrieved evidence.
- **Data provenance:** the present entry synthesizes aggregated literature, tertiary cohorts, human biospecimens, and clinical-trial records—not individual EHR-level data.

## 2. Etiology

### Causal factors

1. **Infectious:** *Toxoplasma gondii*; *Mycobacterium tuberculosis*; *Treponema pallidum*; herpesviruses; fungi, especially in immunocompromised hosts; and less commonly other bacterial, viral, or parasitic agents. In a 6,191-case Greek tertiary uveitis cohort, 1,925 cases were infectious; herpetic disease accounted for 14.87% of all cases, toxoplasmosis 6.6%, and tuberculosis 2.74%. These are overall uveitis—not choroiditis-specific—frequencies and reflect referral and geography (kalogeropoulos2023thelargehellenic pages 1-2).
2. **Immune-mediated/idiopathic:** birdshot chorioretinopathy, multifocal choroiditis/PIC, serpiginous choroiditis, VKH, sarcoidosis, Behçet disease, and other systemic inflammatory disorders. In the same cohort, 4,125 cases were noninfectious and 49.2% of those lacked an identified systemic association (kalogeropoulos2023thelargehellenic pages 1-2).
3. **Drug or iatrogenic triggers:** immune-checkpoint inhibitors, MEK inhibitors, paradoxical anti-TNF inflammation, intraocular drugs, and occasionally temporally associated vaccination have been reported; causality requires careful pharmacovigilance assessment (paezescamilla2023challengesinposterior pages 1-2).
4. **Masqueraders:** primary vitreoretinal lymphoma, leukemia/lymphoma, inherited retinal degeneration, vascular/ischemic disease, amyloidosis, and central serous chorioretinopathy can mimic inflammatory choroiditis. Masquerade syndromes represented 141/6,191 cases in the Greek tertiary cohort (kalogeropoulos2023thelargehellenic pages 1-2).

### Risk and protective factors

- **Birdshot:** HLA-A29 is the dominant susceptibility factor; European ancestry and middle age characterize the typical population. It is necessary or nearly necessary in conventional classification but is not sufficient because HLA-A29 is far more common than birdshot disease (bousquet2022birdshotchorioretinopathya pages 1-2, gelfman2021erap1erap2and pages 1-2).
- **Ocular toxoplasmosis:** undercooked meat, contaminated soil/water or food, cat-feces exposure, congenital transmission, and immunosuppression are biologically relevant exposure routes. Immunocompromise is associated with larger lesions and poor vision. In a 2024 Thai cohort, the adjusted odds ratio for 6-month VA ≤20/50 was 4.9 in immunocompromised patients (sittivarakul2024clinicalcharacteristicsvisual pages 1-2, sittivarakul2024clinicalcharacteristicsvisual pages 13-14).
- **Tubercular disease:** residence or exposure in TB-endemic settings and evidence of latent/systemic infection increase diagnostic probability, although active pulmonary TB and ocular-fluid microbiological confirmation are often absent (NCT06613919 chunk 1).
- **Broad noninfectious uveitis observations:** smoking and vitamin-D deficiency have been associated with risk, but these should not be encoded as proven causal factors for every choroiditis subtype.
- **Potential protection in birdshot:** HLA-A32 was underrepresented among cases in a 2024 French study, OR 0.40 (95% CI 0.19–0.85), suggesting—not proving—a protective effect. ERAP2 rs2248374, which disrupts full-length ERAP2 expression, was also protective, OR 0.56 (95% CI 0.45–0.70) (gelfman2021erap1erap2and pages 1-2, loeliger2024theimpactof pages 1-2).

### Gene–environment interaction

The clearest model is birdshot: HLA-A29-dependent antigen presentation is modified by ERAP1/ERAP2 peptide trimming, but the low penetrance among HLA-A29 carriers implies additional environmental or stochastic immune triggers. No specific exposure has yet been established as the necessary trigger. In infection-associated disease, pathogen exposure interacts with host immunity, pregnancy, age, strain biology, and immunosuppression; these are multifactorial rather than Mendelian interactions.

## 3. Phenotypes

| Phenotype | Character and course | Suggested HPO term |
|---|---|---|
| Blurred or reduced vision | Common, variable; acute in infection, episodic or progressive in immune disease | Visual impairment (HP:0000505) |
| Floaters | Vitreous inflammatory cells/debris; often acute or fluctuating | Vitreous floaters (use current HPO label/ID validation) |
| Photopsia | Prominent in white-dot syndromes/PIC/MFC | Photopsia (validate current HPO ID) |
| Scotoma/field loss | Focal lesions or diffuse retinal dysfunction; progressive in birdshot | Visual field defect (HP:0001123) |
| Photophobia/ocular discomfort | Variable; posterior disease may be relatively painless | Photophobia (HP:0000613) |
| Chorioretinal inflammatory lesions | Cream-colored, punctate, placoid, serpiginous, granulomatous, or necrotizing depending on subtype | Chorioretinal abnormality; chorioretinal scar (validate subtype-specific HPO IDs) |
| Vitritis | Clinical sign accompanying many posterior uveitides | Vitreous inflammation/opacity |
| Retinal vasculitis | Leakage/occlusion on fluorescein angiography | Retinal vasculitis |
| Macular edema | Major cause of reduced acuity in birdshot and other immune subtypes | Cystoid macular edema (HP:0011510) |
| Choroidal neovascularization | Important complication of PIC/MFC and healed inflammatory lesions | Choroidal neovascularization (HP:0011506) |
| Chorioretinal atrophy/scarring | Downstream structural damage causing permanent scotoma or central loss | Chorioretinal atrophy (HP:0000533) |

**Age and laterality are subtype dependent.** Birdshot is a bilateral chronic disorder with mean onset around 53 years; ocular toxoplasmosis in the 2024 Thai cohort had median age 35.9 years and was unilateral in 92.4% (bousquet2022birdshotchorioretinopathya pages 1-2, sittivarakul2024clinicalcharacteristicsvisual pages 1-2). PIC/MFC generally affects young-to-middle-aged, often myopic women, whereas congenital infection can manifest in infancy or later through reactivation.

In active ocular toxoplasmosis, focal necrotizing retinitis, hyperpigmented scars, vitritis, and vasculitis are characteristic. In the Thai cohort, 62% had primary retinitis without an old scar, 56% had posterior-pole lesions, and 75% had lesions no larger than two disc areas; the source abstract’s exact summary was: **“Ocular toxoplasmosis mainly presents as unilateral primary retinitis within the posterior pole.”** (sittivarakul2024clinicalcharacteristicsvisual pages 1-2, sittivarakul2024clinicalcharacteristicsvisual pages 2-4).

Quality-of-life loss arises from impaired reading, driving, work, contrast sensitivity, visual fields, and recurrent-treatment burden. No reliable umbrella-level EQ-5D or SF-36 estimate was identified.

## 4. Genetic and molecular information

There is **no established single causal gene, pathogenic variant, chromosomal abnormality, or inheritance pattern for choroiditis as an umbrella condition**. Routine WES/WGS, karyotyping, CMA, FISH, repeat-expansion, or mitochondrial testing is therefore not indicated solely for acquired choroiditis.

### Birdshot susceptibility architecture

- More than 95% of conventional birdshot cases carry **HLA-A29**; one study reports an OR of approximately 157.5. HLA-A29 nevertheless has incomplete penetrance and is a susceptibility allele, not a deterministic pathogenic variant (gelfman2021erap1erap2and pages 1-2).
- Human sequencing of 286 cases and 108 HLA-A29-positive controls found **ERAP1 rs27432**, OR 2.46 (95% CI 1.85–3.26), and **ERAP2 rs10044354**, OR 1.95 (1.55–2.44). A second HLA-Aw19-family allele gave OR 4.44, while combined ERAP1/ERAP2 risk genotypes plus two HLA-Aw19 alleles gave OR 13.53 (3.79–54.77) (gelfman2021erap1erap2and pages 1-2).
- A 2024 study expanded the series by 120 cases and compared it with 151,997 French subjects. HLA-A29 homozygosity increased susceptibility, OR 1.57 (1.01–2.44), but did not measurably affect severity; HLA-A32 was potentially protective (loeliger2024theimpactof pages 1-2).
- Functional interpretation: ERAP1/ERAP2 alter peptide trimming for HLA class-I presentation. The investigators’ exact conclusion was that the findings suggest **“exceeding a peptide presentation threshold activates the immune response in choroids of A29 carriers.”** (gelfman2021erap1erap2and pages 1-2).

These are germline common-variant associations; they are not ACMG “pathogenic variants,” and clinical population allele frequency is ancestry dependent. No validated modifier-gene panel or genotype-guided treatment is standard.

## 5. Environmental, lifestyle, and infectious information

Environmental determinants are mostly subtype-specific. Food/water hygiene and meat preparation affect toxoplasma acquisition; TB exposure, crowding, migration, and regional endemicity affect tubercular posterior uveitis; immunosuppressive therapy and HIV modify opportunistic disease. Infectious ocular disease is geographically heterogeneous and often unilateral or asymmetric, while climate, conflict, poverty, urbanization, and environmental degradation may influence future burdens (miyagaki2024oculartoxoplasmosisadvances pages 14-15).

Smoking cessation is prudent because smoking is associated with uveitis and may worsen inflammatory/vascular outcomes, but direct prevention data for nonspecific choroiditis are insufficient. No diet, exercise, alcohol, toxin, radiation, pollution, or occupational intervention has been proven to prevent all choroiditis.

## 6. Mechanism and pathophysiology

### Causal chains

**Infectious choroiditis:** pathogen exposure/reactivation → invasion or persistence in retina/choroid/RPE → innate immune sensing and leukocyte recruitment → focal necrosis, granuloma, or vasculitis → edema and photoreceptor/RPE injury → scar/atrophy, field defect, or reduced acuity. In toxoplasmosis, currently available drugs suppress replicating tachyzoites but do not eradicate latent tissue cysts, explaining recurrence (miyagaki2024oculartoxoplasmosisadvances pages 14-15, NCT01449877 chunk 1).

**Immune-mediated choroiditis:** susceptibility plus an incompletely defined trigger → breakdown of ocular immune privilege and antigen presentation → activation of T-cell/macrophage pathways → chemokine-mediated recruitment across the blood–ocular barrier → choroidal stromal/RPE/retinal inflammation → vascular leakage, macular edema, photoreceptor injury, atrophy, fibrosis, or neovascularization.

**Birdshot-specific upstream mechanism:** HLA-A29 plus ERAP1/ERAP2-dependent immunopeptidome changes → aberrant class-I peptide presentation → CD8-associated and broader adaptive immune activation → independent but concurrent choroidal stromal and retinal inflammation (bousquet2022birdshotchorioretinopathya pages 14-15, gelfman2021erap1erap2and pages 1-2).

### Recent human molecular profiling

A 2024 human aqueous-fluid study measured 31 inflammatory proteins and performed single-cell expression analysis. Six chemokines—CCL2, CXCL10, CXCL9, CXCL8, CCL3, and CCL14—were elevated in active uveitis and enriched in aqueous relative to plasma. CCL2 and CXCL10 were consistently enriched, and single-cell RNA sequencing implicated ocular macrophages as a source. The authors concluded: **“ocular macrophages may play a central role, via CCL2 and CXCL10 production, in recruiting inflammatory cells to the eye.”** This is pan-uveitis evidence, not proof that all choroiditis subtypes share identical signaling (lin2024aqueousmacrophagescontribute pages 1-2).

A 2023 SWATH-MS study analyzed 278 plasma/EV samples, identified 3,668 proteins, quantified more than 3,000, and found that small- and large-EV proteomes correlated with disease better than plasma. It validated candidate panels for AS-related uveitis, Behçet uveitis, VKH, and posterior scleritis; these remain research biomarkers rather than routine diagnostics (wu2023comprehensiveprofilingof pages 1-2).

**Suggested GO biological processes:** inflammatory response (GO:0006954), immune response (GO:0006955), leukocyte migration (GO:0050900), chemotaxis (GO:0006935), antigen processing and presentation of peptide antigen via MHC class I (GO:0002474), T-cell activation (GO:0042110), macrophage activation (GO:0042116), angiogenesis (GO:0001525), and apoptotic process (GO:0006915).

**Suggested CL terms:** macrophage (CL:0000235), CD8-positive alpha-beta T cell (CL:0000625), CD4-positive alpha-beta T cell (CL:0000624), retinal pigment epithelial cell (CL:0002586), vascular endothelial cell (CL:0000115), photoreceptor cell (CL:0000210), and choroidal melanocyte where an appropriate current CL identifier is available.

## 7. Anatomical structures affected

- **Primary organ:** eye.
- **Primary site:** choroid; suggested **UBERON:0001776** (choroid).
- **Frequent contiguous structures:** retina (**UBERON:0000966**), RPE, vitreous body (**UBERON:0001797**), optic disc/nerve, retinal and choroidal vessels, and macula.
- **Tissue/cell targets:** choroidal stroma and vasculature, melanocytes, resident macrophages, RPE, photoreceptors, retinal vascular endothelium, and infiltrating lymphocytes.
- **Subcellular processes:** ER peptide trimming and MHC-I loading are particularly relevant in birdshot; mitochondria, lysosomes, and apoptotic machinery participate downstream but no universal organelle defect is established.
- **Laterality:** bilateral in birdshot and typically VKH; often unilateral in active toxoplasmosis; PIC/MFC may be unilateral, bilateral, or asymmetric.
- **Secondary organs:** depend on cause—neurologic/auditory/integumentary involvement in VKH, pulmonary/lymphatic disease in sarcoidosis or TB, mucocutaneous/vascular disease in Behçet, and systemic infection in immunocompromised patients.

## 8. Temporal development

Onset ranges from congenital to geriatric. Infection may be acute or subacute; toxoplasma lesions resolve into scars but can reactivate. Immune subtypes are commonly episodic, relapsing-remitting, or chronic progressive. Birdshot is indolent but potentially severe and usually requires prolonged control; mean onset is approximately 53 years (bousquet2022birdshotchorioretinopathya pages 1-2, gelfman2021erap1erap2and pages 1-2).

In the 2024 toxoplasmosis cohort, cumulative recurrence at three years was 33.9% (95% CI 19.7–54.2%). A broader 2024 review reported greater recurrence risk in younger people and approximately 40% contralateral recurrence when bilateral scars were present versus 4% in previously unaffected contralateral eyes (miyagaki2024oculartoxoplasmosisadvances pages 14-15, sittivarakul2024clinicalcharacteristicsvisual pages 1-2).

The critical therapeutic window is active inflammation before irreversible macular/optic-nerve injury, vascular occlusion, or fibrosis. Delay in anti-TB therapy has been associated with chronic inflammation and prolonged visual impairment (NCT06613919 chunk 1).

## 9. Inheritance and population

Choroiditis is generally acquired and **not inherited in Mendelian fashion**. Penetrance, anticipation, mosaicism, founder effects, carrier frequency, and reproductive genetic screening are therefore not applicable at the umbrella level. Birdshot has polygenic immune susceptibility with markedly incomplete penetrance.

Reliable global incidence/prevalence is unavailable because “choroiditis” pools multiple disorders and coding practices. Overall uveitis estimates reported in the 2023 Greek study were incidence 20–50/100,000/year and prevalence 38–714/100,000, but these should not be entered as choroiditis-specific rates (kalogeropoulos2023thelargehellenic pages 1-2).

Birdshot is rare: approximately 0.6–1.5% of tertiary-center uveitis, 5–8% of posterior uveitis, and an estimated 0.1–0.6/100,000 population prevalence. It predominantly affects middle-aged people of European ancestry and has no consistent sex predominance (bousquet2022birdshotchorioretinopathya pages 1-2). Infectious subtype frequencies vary strongly with geography, sanitation, pathogen prevalence, migration, and immune status.

## 10. Diagnostics

### Core clinical approach

1. Confirm intraocular inflammation by dilated slit-lamp and fundus examination.
2. Localize primary pathology using color/wide-field photography, OCT with enhanced-depth choroidal imaging, fluorescein angiography, indocyanine-green angiography, fundus autofluorescence, and OCT angiography. Multimodal imaging is now a real-world standard for lesion activity, macular edema, vasculitis, atrophy, and CNV (bousquet2022birdshotchorioretinopathya pages 14-15, paezescamilla2023challengesinposterior pages 1-2, miyagaki2024oculartoxoplasmosisadvances pages 14-15).
3. Use targeted rather than indiscriminate laboratory testing: syphilis serology; TB IGRA/TST and thoracic imaging where relevant; toxoplasma serology with ocular-fluid PCR or intraocular antibody testing in atypical cases; CBC/chemistry; and directed studies for sarcoidosis, HIV, or systemic autoimmunity.
4. Consider aqueous/vitreous PCR, cytology, flow cytometry, cytokine analysis, or biopsy when infection or lymphoma remains plausible.

### Subtype-supportive tests

- **Birdshot:** HLA-A29 testing, ICG angiography, fluorescein angiography, OCT, autofluorescence, visual fields, and electroretinography. HLA-A29 supports classification but is not a standalone diagnostic test (bousquet2022birdshotchorioretinopathya pages 14-15, bousquet2022birdshotchorioretinopathya pages 1-2).
- **Toxoplasmosis:** classic focal necrotizing retinitis adjacent to a pigmented scar may be diagnosed clinically; multimodal imaging and laboratory confirmation are more important in atypical or immunocompromised disease (miyagaki2024oculartoxoplasmosisadvances pages 14-15, sittivarakul2024clinicalcharacteristicsvisual pages 2-4).
- **Tubercular posterior uveitis:** characteristic lesions/vasculitis plus evidence of TB infection and exclusion of alternatives; ocular-fluid microbiology is often negative. The phase-4 trial used TST/IGRA, CBC, ESR, HIV and VDRL testing, and contrast-enhanced chest CT or radiography (NCT06613919 chunk 1).

### Differential diagnosis

Infectious retinitis/choroiditis, white-dot syndromes, sarcoidosis, VKH, Behçet disease, posterior scleritis, retinal vasculitis, central serous chorioretinopathy, age-related or myopic CNV, intraocular lymphoma, leukemia, metastatic disease, inherited retinal degeneration, and drug toxicity must be distinguished before immunosuppression. Expert analysis emphasizes that overlapping phenotypes and masqueraders make history, medication review, imaging, and sometimes genetic or tissue testing essential (paezescamilla2023challengesinposterior pages 1-2).

No asymptomatic population screening or newborn screening program exists for choroiditis. Genetic testing is limited mainly to HLA-A29 as a diagnostic adjunct in suspected birdshot; WGS/WES and broad panels are not standard.

## 11. Outcome and prognosis

Choroiditis rarely affects life expectancy directly; survival statistics are not meaningful for the umbrella diagnosis. Morbidity is predominantly visual. Important complications are macular edema, chorioretinal atrophy/scarring, retinal vasculitis/occlusion, CNV, epiretinal membrane, cataract, glaucoma/ocular hypertension, retinal detachment, and treatment toxicity.

In the Thai toxoplasmosis cohort, 21% of affected eyes had final VA ≤20/200. Severe permanent loss occurred in 17% of immunocompetent and 50% of immunocompromised patients; macular scarring accounted for 24.7% of vision loss. Ocular hypertension occurred in 20.6%, epiretinal membrane in 12.6%, and cataract in 6.2%. Poor 6-month vision was predicted by immunocompromise (aOR 4.9), macular lesions (aOR 5.4), and initial VA ≤20/200 (aOR 9.1) (sittivarakul2024clinicalcharacteristicsvisual pages 1-2, sittivarakul2024clinicalcharacteristicsvisual pages 13-14).

A birdshot trial record cites legal blindness in 14% at five years and macular edema in 80%, but these historical estimates should be interpreted cautiously because they derive from older referred cohorts (NCT00508040 chunk 1). Early control, lesion location, baseline acuity, immunocompetence, recurrence, and development of macular edema/CNV are major prognostic determinants.

## 12. Treatment

Treatment must follow etiology; **systemic corticosteroids must not be given as unopposed therapy until important infections have been excluded.**

### Infectious disease

- **Toxoplasmosis:** commonly TMP–sulfamethoxazole, or pyrimethamine plus sulfadiazine and folinic acid; alternatives include clindamycin, azithromycin, atovaquone, and intravitreal clindamycin in selected cases. Corticosteroid is adjunctive only after effective antiparasitic therapy in vision-threatening inflammation. In the 2024 Thai cohort, 85% received oral TMP–sulfamethoxazole monotherapy (sittivarakul2024clinicalcharacteristicsvisual pages 1-2).
- **Tuberculosis:** multidrug anti-tuberculosis treatment, frequently with adjunctive corticosteroid or immunomodulation after antimicrobial coverage. NCT06613919 compared six versus nine months (NCT06613919 chunk 1).
- **Syphilis:** intravenous aqueous penicillin G according to neurosyphilis/ocular-syphilis protocols.
- **Herpetic disease:** systemic acyclovir/valacyclovir or appropriate antiviral, with intravitreal therapy for severe necrotizing retinitis.
- **Fungal disease:** systemic and/or intravitreal antifungal treatment plus source control.

### Noninfectious disease

- Corticosteroids—local, periocular, intravitreal, or systemic—provide rapid induction but are unsuitable as long-term monotherapy in chronic disease.
- Steroid-sparing agents include methotrexate, mycophenolate mofetil, azathioprine, cyclosporine/tacrolimus, and other conventional immunomodulators.
- Biologics, especially anti-TNF agents such as adalimumab or infliximab, are used for refractory noninfectious posterior uveitis; subtype and systemic comorbidity guide selection. Current cytokine-targeted therapies fail in an estimated 30–50% of heterogeneous uveitis patients, motivating chemokine-directed research (lin2024aqueousmacrophagescontribute pages 1-2).
- **Inflammatory CNV:** intravitreal anti-VEGF, generally combined with control of underlying inflammation.
- Surgery treats complications—cataract extraction when inflammation is controlled, vitrectomy for nonclearing opacity/traction or diagnostic sampling, and retinal-detachment repair.

Suggested NCIT intervention concepts include Corticosteroid Therapy, Immunosuppressive Therapy, Methotrexate, Mycophenolate Mofetil, Cyclosporine, Adalimumab, Infliximab, Interferon Alfa-2a, Anti-infective Therapy, Anti-VEGF Therapy, Intravitreal Injection, Vitrectomy, and Cataract Surgery; current NCIT codes should be validated at ingestion.

### Trials and experimental applications

- **NCT00508040/BIRDFERON:** completed randomized phase 2, 58 participants, interferon alfa-2a versus prednisone for HLA-A29-positive birdshot with macular edema; OCT central thickness was the primary endpoint (NCT00508040 chunk 1).
- **NCT01449877/ISROT:** completed randomized triple-masked phase 3, 141 participants. After 45 days of acute TMP–sulfamethoxazole, prophylaxis every other day for 311 days was compared with placebo, with recurrence follow-up planned through ten years (NCT01449877 chunk 1).
- **NCT06613919:** completed randomized phase 4 noninferiority study, 58 participants, comparing six and nine months of anti-TB therapy; endpoint was nonrecurrence one year after treatment (NCT06613919 chunk 1).

No approved gene, RNA, stem-cell, or CRISPR therapy exists for choroiditis. EV biomarker panels and CCL2/CXCL10-directed strategies remain investigational (lin2024aqueousmacrophagescontribute pages 1-2, wu2023comprehensiveprofilingof pages 1-2).

## 13. Prevention

**Primary prevention:** food and water hygiene, adequate cooking of meat, hand hygiene after soil/raw-meat exposure, prevention and treatment of maternal infection, TB control and contact management, HIV prevention/treatment, vaccination against relevant preventable systemic infections, and avoidance of unnecessary immunosuppression. There is no vaccine preventing all choroiditis and no licensed human toxoplasma vaccine.

**Secondary prevention:** rapid ophthalmic assessment for new floaters, photopsia, scotoma, or reduced vision; early etiologic testing and multimodal imaging; surveillance of the fellow eye and of high-risk immunocompromised patients.

**Tertiary prevention:** maintain inflammatory remission, monitor OCT/angiography and visual fields, minimize corticosteroid toxicity, promptly treat CNV and macular edema, and provide low-vision rehabilitation. TMP–sulfamethoxazole prophylaxis after recurrent toxoplasma retinochoroiditis is supported by randomized investigation, but it is subtype- and patient-specific rather than universal prophylaxis (NCT01449877 chunk 1).

Pregnancy and toxoplasmosis recurrence data are inconsistent: reported estimates range from lower recurrence during pregnancy (IRR 0.54–0.75) to a 7.4-fold increase in another population. This precludes a single universal risk estimate and supports specialist monitoring (miyagaki2024oculartoxoplasmosisadvances pages 14-15).

## 14. Other species and natural disease

*T. gondii* naturally infects many warm-blooded vertebrates; felids are definitive hosts and numerous mammals and birds are intermediate hosts. Ocular toxoplasmosis occurs naturally in companion and production animals, although species-specific lesion patterns and clinical importance vary. Equine recurrent uveitis, canine/feline uveitis, and infectious chorioretinitis are important comparative conditions but should not be treated as exact equivalents of human immune-mediated choroiditis.

Suggested taxa include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), *Rattus norvegicus* (10116), *Canis lupus familiaris* (9615), *Felis catus* (9685), and *Toxoplasma gondii* (5811). No breed-specific VBO association, orthologous monogenic disease, or zoonotic transmission from human choroiditis itself is established. Zoonotic relevance pertains to the causal pathogen, particularly *T. gondii*, not to ocular inflammation as a transmissible phenotype.

## 15. Model organisms

- **Experimental autoimmune uveitis (EAU):** mice or rats immunized with retinal antigens such as interphotoreceptor retinoid-binding protein, usually with adjuvant, develop T-cell-driven retinal/choroidal inflammation. It is useful for immune recruitment, Th1/Th17 biology, blood–retinal barrier failure, and therapeutic screening, but does not reproduce the full etiologic or chronic heterogeneity of human choroiditis.
- **Unprimed mycobacterial uveitis:** the 2024 chemokine study injected killed *M. tuberculosis* H37Ra antigen intravitreally into C57BL/6J mice. This models acute innate ocular inflammation and chemokine recruitment, not viable tubercular choroiditis (lin2024aqueousmacrophagescontribute pages 1-2).
- **Ocular toxoplasmosis:** mouse infection models and retinal/RPE cell culture systems permit analysis of parasite invasion, cyst persistence, inflammation, and strain effects; differences in ocular anatomy, immunity, and parasite strains limit direct clinical translation.
- **VKH/birdshot:** antigen-induced or humanized HLA models probe melanocyte/retinal antigen responses, but no model fully reproduces HLA-A29-restricted human birdshot.
- **In vitro systems:** primary RPE, retinal organoids, choroidal endothelial cells, macrophage/T-cell coculture, and iPSC-derived ocular cells can dissect cell-specific injury and drug response. They lack complete vascular, neural, and systemic immunity.

Model resources include MGI, IMSR, MMRRC, RGD, ZFIN, Cellosaurus, GEO, and CELLxGENE. Animal-model findings should be labeled experimental and not used as direct evidence of human treatment efficacy.

## Evidence limitations and knowledge-base recommendations

1. Encode **choroiditis as a parent anatomic inflammatory concept**, with infectious, immune-mediated, and masquerade children.
2. Do not attach birdshot HLA findings, toxoplasma recurrence, or TB treatment directly to every choroiditis case.
3. Mark HLA-A29/ERAP findings as **susceptibility associations**, not ACMG-pathogenic Mendelian variants.
4. Treat EV proteomics and aqueous single-cell signatures as research-stage biomarkers/mechanisms, not validated diagnostic tests.
5. Epidemiologic values are mostly uveitis-wide or subtype-specific; a defensible global prevalence or incidence for undifferentiated choroiditis is unavailable.
6. Retrieved records supplied DOI URLs consistently, but PMIDs were not available for most cited 2023–2024 articles; PMIDs should be resolved through PubMed during database ingestion rather than inferred.

References

1. (paezescamilla2023challengesinposterior pages 1-2): Manuel Paez-Escamilla, Sonny Caplash, Gagan Kalra, Jamie Odden, Danielle Price, Oscar C. Marroquin, Stephen Koscumb, Patrick Commiskey, Chad Indermill, Jerome Finkelstein, Anna G. Gushchin, Andreea Coca, Thomas R. Friberg, Andrew W. Eller, Denise S. Gallagher, Jean C. Harwick, Evan L. Waxman, Jay Chhablani, Gabrielle Bonhomme, Colin Prensky, Alexander J. Anetakis, Joseph N. Martel, Erika Massicotte, Raphaelle Ores, Jean-Francois Girmens, Thomas M Pearce, Jose-Alain Sahel, Kunal Dansingani, Mark Westcott, and Marie-Helene Errera. Challenges in posterior uveitis—tips and tricks for the retina specialist. Journal of Ophthalmic Inflammation and Infection, Aug 2023. URL: https://doi.org/10.1186/s12348-023-00342-5, doi:10.1186/s12348-023-00342-5. This article has 20 citations and is from a peer-reviewed journal.

2. (kalogeropoulos2023thelargehellenic pages 1-2): Dimitrios Kalogeropoulos, Ioannis Asproudis, Maria Stefaniotou, Marilita M. Moschos, Vassilios P. Kozobolis, Paraskevi V. Voulgari, Andreas Katsanos, Constantina Gartzonika, and Chris Kalogeropoulos. The large hellenic study of uveitis: epidemiology, etiologic factors and classification. International Ophthalmology, 43:3633-3650, Jul 2023. URL: https://doi.org/10.1007/s10792-023-02772-5, doi:10.1007/s10792-023-02772-5. This article has 43 citations and is from a peer-reviewed journal.

3. (bousquet2022birdshotchorioretinopathya pages 1-2): Elodie Bousquet, Pierre Duraffour, Louis Debillon, Swathi Somisetty, Dominique Monnet, and Antoine P. Brézin. Birdshot chorioretinopathy: a review. Journal of Clinical Medicine, 11:4772, Aug 2022. URL: https://doi.org/10.3390/jcm11164772, doi:10.3390/jcm11164772. This article has 45 citations.

4. (gelfman2021erap1erap2and pages 1-2): Sahar Gelfman, Dominique Monnet, Ann J. Ligocki, Thierry Tabary, Arden Moscati, Xiaodong Bai, Jan Freudenberg, Blerta Cooper, Jack A. Kosmicki, Sarah Wolf, Manuel A. R. Ferreira, John Overton, Jonathan Weyne, Eli A. Stahl, Aris Baras, Carmelo Romano, Jacques H. M. Cohen, Giovanni Coppola, and Antoine Brézin. Erap1, erap2, and two copies of hla-aw19 alleles increase the risk for birdshot chorioretinopathy in hla-a29 carriers. Nov 2021. URL: https://doi.org/10.1167/iovs.62.14.3, doi:10.1167/iovs.62.14.3. This article has 30 citations.

5. (loeliger2024theimpactof pages 1-2): Jordan Loeliger, Romain Lhotte, Sahar Gelfman, Eli A. Stahl, Dominique Monnet, Valentin Clichet, Linda Imikirene, Souhila Kecili, Jean-Luc Taupin, Thierry Tabary, Jacques H. M. Cohen, and Antoine P. Brézin. The impact of hla-a29 homozygosity and of the second hla-a allele on susceptibility and severity of birdshot chorioretinitis. Investigative Ophthalmology &amp; Visual Science, 65:47, Nov 2024. URL: https://doi.org/10.1167/iovs.65.13.47, doi:10.1167/iovs.65.13.47. This article has 2 citations and is from a domain leading peer-reviewed journal.

6. (sittivarakul2024clinicalcharacteristicsvisual pages 1-2): Wantanee Sittivarakul, Wanitcha Treerutpun, and Usanee Tungsattayathitthan. Clinical characteristics, visual acuity outcomes, and factors associated with loss of vision among patients with active ocular toxoplasmosis: a retrospective study in a thai tertiary center. PLOS Neglected Tropical Diseases, 18:e0012232, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012232, doi:10.1371/journal.pntd.0012232. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (sittivarakul2024clinicalcharacteristicsvisual pages 13-14): Wantanee Sittivarakul, Wanitcha Treerutpun, and Usanee Tungsattayathitthan. Clinical characteristics, visual acuity outcomes, and factors associated with loss of vision among patients with active ocular toxoplasmosis: a retrospective study in a thai tertiary center. PLOS Neglected Tropical Diseases, 18:e0012232, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012232, doi:10.1371/journal.pntd.0012232. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (miyagaki2024oculartoxoplasmosisadvances pages 14-15): Miki Miyagaki, Yuan Zong, Mingming Yang, Jing Zhang, Yaru Zou, Kyoko Ohno-Matsui, and Koju Kamoi. Ocular toxoplasmosis: advances in toxoplasma gondii biology, clinical manifestations, diagnostics, and therapy. Pathogens, 13:898, Oct 2024. URL: https://doi.org/10.3390/pathogens13100898, doi:10.3390/pathogens13100898. This article has 35 citations.

9. (lin2024aqueousmacrophagescontribute pages 1-2): Joseph B. Lin, Kathryn L. Pepple, Christian Concepcion, Yulia Korshunova, Michael A. Paley, Grace L. Paley, Jennifer Laurent, Rajendra S. Apte, and Lynn M. Hassman. Aqueous macrophages contribute to conserved ccl2 and cxcl10 gradients in uveitis. Ophthalmology Science, 4:100453, Jul 2024. URL: https://doi.org/10.1016/j.xops.2023.100453, doi:10.1016/j.xops.2023.100453. This article has 15 citations.

10. (wu2023comprehensiveprofilingof pages 1-2): Lingzi Wu, Lei Zhou, Jinying An, Xianfeng Shao, Hui Zhang, Chunxi Wang, Guixia Zhao, Shuang Chen, Xuexue Cui, Xinyi Zhang, Fuhua Yang, Xiaorong Li, and Xiaomin Zhang. Comprehensive profiling of extracellular vesicles in uveitis and scleritis enables biomarker discovery and mechanism exploration. Journal of Translational Medicine, Jun 2023. URL: https://doi.org/10.1186/s12967-023-04228-x, doi:10.1186/s12967-023-04228-x. This article has 18 citations and is from a peer-reviewed journal.

11. (NCT00508040 chunk 1):  Evaluation of Birdshot Retine Choroidopathy Treatment by Either Steroid or Interferon alpha2a. Assistance Publique - Hôpitaux de Paris. 2007. ClinicalTrials.gov Identifier: NCT00508040

12. (NCT01449877 chunk 1): Joao Paulo Felix. Influence of Trimethoprim-Sulfamethoxazole for the Recurrence of Ocular Toxoplasmosis. University of Campinas, Brazil. 2011. ClinicalTrials.gov Identifier: NCT01449877

13. (NCT06613919 chunk 1): HERF. Six-months Versus Nine-months ATT for Ocular TB. L.V. Prasad Eye Institute. 2020. ClinicalTrials.gov Identifier: NCT06613919

14. (sittivarakul2024clinicalcharacteristicsvisual pages 2-4): Wantanee Sittivarakul, Wanitcha Treerutpun, and Usanee Tungsattayathitthan. Clinical characteristics, visual acuity outcomes, and factors associated with loss of vision among patients with active ocular toxoplasmosis: a retrospective study in a thai tertiary center. PLOS Neglected Tropical Diseases, 18:e0012232, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012232, doi:10.1371/journal.pntd.0012232. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (bousquet2022birdshotchorioretinopathya pages 14-15): Elodie Bousquet, Pierre Duraffour, Louis Debillon, Swathi Somisetty, Dominique Monnet, and Antoine P. Brézin. Birdshot chorioretinopathy: a review. Journal of Clinical Medicine, 11:4772, Aug 2022. URL: https://doi.org/10.3390/jcm11164772, doi:10.3390/jcm11164772. This article has 45 citations.

## Artifacts

- [Edison artifact artifact-00](Choroiditis-deep-research-falcon_artifacts/artifact-00.md)