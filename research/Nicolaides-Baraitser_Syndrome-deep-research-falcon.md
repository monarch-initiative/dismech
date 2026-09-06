---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T18:26:09.463376'
end_time: '2026-07-31T18:36:39.660694'
duration_seconds: 630.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nicolaides-Baraitser Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Nicolaides-Baraitser_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nicolaides-Baraitser Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nicolaides-Baraitser Syndrome** covering all of the
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
- **Disease Name:** Nicolaides-Baraitser Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nicolaides-Baraitser Syndrome** covering all of the
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


# Nicolaides–Baraitser Syndrome: Comprehensive Disease-Characteristics Report

## Executive summary

Nicolaides–Baraitser syndrome (NCBRS) is a rare, congenital, lifelong neurodevelopmental **BAFopathy/chromatinopathy** caused primarily by heterozygous, usually de novo, non-truncating pathogenic variants in the ATPase/helicase region of **SMARCA2**. Its characteristic combination is developmental delay/intellectual disability, severely impaired speech, epilepsy, postnatal microcephaly and short stature, sparse scalp hair, progressive facial coarsening, brachydactyly, and prominent interphalangeal joints. The largest deeply phenotyped molecular cohort available in the retrieved literature comprised only 61 individuals, so most frequency estimates remain imprecise and vulnerable to ascertainment bias. (sousa2014phenotypeandgenotype pages 2-2, sousa2014phenotypeandgenotype pages 1-2)

Recent work has shifted the mechanistic model from simple loss of SMARCA2 activity toward mutation-specific dysregulation of BAF-complex targeting and enhancer selection. The most clinically mature recent development is peripheral-blood DNA-methylation episignature testing, used as an adjunct for interpreting uncertain SMARCA2 variants. No disease-modifying therapy or NCBRS-specific interventional trial was identified; current care is multidisciplinary and symptom-directed. (chaterdiehl2019newinsightsinto pages 1-2, gao2019heterozygousmutationsin pages 1-3, trajkova2024dnamethylationanalysis pages 1-2, NCT01793168 chunk 4)

The following table summarizes the strongest quantitative evidence.

| Domain | Best-supported finding | Quantitative evidence | Evidence type/date |
|---|---|---|---|
| Identifiers | Nicolaides-Baraitser syndrome is a Mendelian neurodevelopmental disorder; available disease identifiers include MONDO:0011053, OMIM 601358, Orphanet 3051 | MONDO:0011053; OMIM 601358; Orphanet 3051 (OpenTargets Search: Nicolaides-Baraitser syndrome-SMARCA2, pretegiani2016nicolaides–baraitsersyndromedefining pages 1-2) | Disease-resource association/Open Targets and human clinical letter, 2016 |
| Cause / inheritance | Core cause is de novo heterozygous non-truncating SMARCA2 variation, usually in the ATPase/helicase region, consistent with autosomal-dominant sporadic disease | 61/61 analyzed cases sporadic; SMARCA2 mutations in 34/37 clinically typical patients and 2/7 less typical patients in early grouped analyses; >50% (36/61, 59%) in C-terminal helicase region (sousa2014phenotypeandgenotype pages 2-2, sousa2014phenotypeandgenotype pages 10-10, sousa2014phenotypeandgenotype pages 1-2) | Human cohort/review, 2014 |
| Intellectual disability | Intellectual disability is universal and often moderate-to-severe | Mild 18.0%, moderate 36.1%, severe 45.9% among 61 cases (sousa2014phenotypeandgenotype pages 3-3) | Molecularly confirmed 61-case cohort, 2014 |
| Seizures | Epilepsy is a major feature with usual onset in infancy/early childhood | 39/61 (63.9%); median onset 18 months, range 0–168 months; review text also notes typical onset 1–2.5 years (sousa2014phenotypeandgenotype pages 10-11, sousa2014phenotypeandgenotype pages 3-3) | Molecularly confirmed cohort/review, 2014 |
| Speech | Severe speech impairment is common, including absent speech and later decline | Absent speech 19/60 (31.7%); speech decline 9/42 (21.4%); first words median 24 months, range 10–96 months (sousa2014phenotypeandgenotype pages 3-3) | Molecularly confirmed 61-case cohort, 2014 |
| Growth / stature | Postnatal growth impairment is common | Short stature 30/56 (53.6%); reduced weight 24/46 (52.2%); birth weight < -2 SD in 19/57 (33.3%); birth length < -2 SD in 8/38 (21.1%) (sousa2014phenotypeandgenotype pages 2-2, sousa2014phenotypeandgenotype pages 2-3, sousa2014phenotypeandgenotype pages 3-3) | Molecularly confirmed cohort/review, 2014 |
| Microcephaly | Microcephaly often emerges or becomes more evident over time | 34/52 (65.4%) later in life; 7/30 (23%) at birth (sousa2014phenotypeandgenotype pages 2-3, sousa2014phenotypeandgenotype pages 3-3) | Molecularly confirmed cohort/review, 2014 |
| Hypotonia / motor delay | Hypotonia and delayed gross motor milestones are frequent | Hypotonia 19/51 (37.3%); sitting median 8 months (range 6–20); walking median 18 months (range 10–60) (sousa2014phenotypeandgenotype pages 3-3) | Molecularly confirmed 61-case cohort, 2014 |
| Feeding / skin / organ findings | Supportive morbidity includes feeding problems, eczema, and occasional cardiac/hearing involvement | Feeding problems 23/49 (46.9%); eczema 22/58 (37.9%); cardiac defects 6/61 (9.8%); hearing loss 4/59 (6.8%) (sousa2014phenotypeandgenotype pages 4-4) | Molecularly confirmed cohort table, 2014 |
| Mechanism | NCBRS is a BAFopathy caused by SMARCA2 dysfunction affecting chromatin remodeling and neural differentiation; engineered human stem-cell models support enhancer retargeting rather than simple haploinsufficiency | In engineered hESC-derived neural progenitors with SMARCA2 K755R/+ or R1159Q/+ mutations, neural differentiation was severely impaired; ~97% of upregulated genes with increased accessibility were FRA2-bound (gao2019heterozygousmutationsin pages 1-3, gao2019heterozygousmutationsin pages 10-12, gao2019heterozygousmutationsin pages 12-14) | Experimental human hESC/NPC study, 2019 |
| Methylation diagnostics | Peripheral-blood DNA methylation episignatures can aid SMARCA2 variant interpretation | 429 differentially methylated CpGs in 8 NCBRS cases vs 23 controls; validation reported 100% sensitivity and 100% specificity with 8 cases and 96 controls; 9 SMARCA2 VUS assessed (chaterdiehl2019newinsightsinto pages 1-2) | Epigenomic diagnostic study, 2019 |
| Recent diagnostic development | 2024 work supports episignatures as a practical adjunct for NDD/BAFopathy variant resolution but highlights interpretive limitations | Validation cohort 59 and test cohort 38 in a broader NDD study; 90% expected episignature recovery; intermediate SMARCA2 classifications reported in familial/VUS contexts (trajkova2024dnamethylationanalysis pages 1-2, awamleh2024dnamethylationsignatures pages 3-6) | Diagnostic/epigenomic studies and review, 2024 |
| Trials / implementation | No disease-modifying interventional trial was identified; current formal research implementation is observational registry participation | NCT01793168 is observational, recruiting, prospective, case-only, target enrollment 20,000 across rare diseases including NCBRS; no syndrome-specific therapeutic intervention reported (NCT01793168 chunk 4) | ClinicalTrials.gov registry entry, 2010–current |


*Table: This table condenses the strongest available evidence for Nicolaides-Baraitser syndrome across identifiers, genetics, phenotype frequencies, mechanism, diagnostics, and trial status. It is useful as a quick-reference artifact for disease knowledge-base population with denominated cohort data and recent diagnostic advances.*

---

## 1. Disease information

### Definition and classification

NCBRS is a Mendelian syndromic intellectual-developmental disorder caused by altered ATP-dependent chromatin remodeling. It belongs to the group of SWI/SNF-related intellectual-disability disorders, particularly the **BAFopathies**, which overlap clinically and molecularly with Coffin–Siris syndrome. Open Targets links the disease to **SMARCA2**, with the preferred gene name “SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2.” (OpenTargets Search: Nicolaides-Baraitser syndrome-SMARCA2, pretegiani2016nicolaides–baraitsersyndromedefining pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0011053
- **OMIM:** 601358
- **Orphanet:** ORPHA:3051
- **Causal-gene OMIM:** SMARCA2, OMIM 600014
- **Common names:** Nicolaides–Baraitser syndrome; NCBRS; intellectual disability–sparse hair–brachydactyly syndrome; intellectual disability–sparse hair–prominent distal phalanges syndrome.
- **ICD-10/ICD-11 and MeSH:** no disease-specific code or dedicated MeSH descriptor was established in the retrieved evidence. In practice, nonspecific codes for congenital malformation syndromes, intellectual disability, developmental delay, or epilepsy may be used, but these should not be treated as exact NCBRS mappings.

The disease-level identifiers are aggregated ontology/resource assertions, whereas the clinical frequencies below derive from aggregated published patients, diagnostic-laboratory cases, and questionnaire-based phenotyping rather than longitudinal EHR surveillance. The principal 61-person analysis included 47 previously reported and 14 unpublished molecularly confirmed cases. (OpenTargets Search: Nicolaides-Baraitser syndrome-SMARCA2, sousa2014phenotypeandgenotype pages 1-2)

---

## 2. Etiology

### Causal and genetic factors

The core cause is a heterozygous pathogenic **SMARCA2** variant, most often a de novo missense change or small in-frame deletion affecting the conserved ATPase/helicase region. The 2012 discovery study is indexed as **PMID 22366787**. Open Targets independently associates SMARCA2 with MONDO:0011053 and cites that study. (OpenTargets Search: Nicolaides-Baraitser syndrome-SMARCA2)

Classic NCBRS variants are non-truncating and cluster within functional ATPase motifs rather than being distributed like ordinary haploinsufficient alleles. In the 61-case analysis, 36/61 (59%) involved the C-terminal helicase region. Motif VI, particularly Arg1159, was a hotspot; this residue participates in ATP-phosphate interaction and hydrolysis. Variants p.Pro883Leu, p.Leu946Ser/Phe, and p.Ala1201Val were associated with relatively milder presentations, whereas motif-VI variants were more often associated with severe intellectual disability and epilepsy. These correlations remain provisional because individual variant groups were small. (sousa2014phenotypeandgenotype pages 10-10, sousa2014phenotypeandgenotype pages 1-2)

Atypical variants outside the canonical region require caution. For example, a reported p.Gly1420Arg bromodomain-region variant produced partial phenotypic overlap but lacked some classic findings. Conversely, a de novo p.Gln1241Glu variant outside the usual ATPase cluster was reported with myoclonic–astatic epilepsy. Thus, location is strongly informative but not an absolute diagnostic rule. (sousa2014phenotypeandgenotype pages 10-11, sousa2014phenotypeandgenotype pages 11-11)

### Risk, protective, and environmental factors

- **Established risk factor:** conception of a child with a de novo pathogenic SMARCA2 allele.
- **Parental age:** mean paternal and maternal ages in the 61-case cohort were 32.9 and 30.1 years, respectively, but no causal age effect was established. (sousa2014phenotypeandgenotype pages 2-2, sousa2014phenotypeandgenotype pages 1-2)
- **Environmental, infectious, occupational, dietary, lifestyle, or toxic causes:** none established.
- **Protective variants or environmental protective factors:** none established.
- **Modifier genes:** no validated modifier gene was identified. Variation in residual BAF activity, paralogous SMARCA4 recruitment, developmental context, mosaicism, or epigenetic state are plausible modifiers but are not clinically validated.
- **Gene–environment interaction:** no disease-specific interaction has been demonstrated. Environmental factors may influence seizure threshold, nutrition, and rehabilitation outcomes without causing the syndrome.

---

## 3. Phenotypes

### Neurodevelopment, behavior, and epilepsy

All 61 molecularly confirmed individuals had intellectual disability: mild in 18.0%, moderate in 36.1%, and severe in 45.9%. Median independent sitting was 8 months (range 6–20) and walking 18 months (10–60); hypotonia occurred in 19/51 (37.3%). Suggested HPO terms include **Intellectual disability (HP:0001249)**, **Global developmental delay (HP:0001263)**, **Delayed speech and language development (HP:0000750)**, **Motor delay (HP:0001270)**, and **Muscular hypotonia (HP:0001252)**. (sousa2014phenotypeandgenotype pages 3-3)

Speech is disproportionately impaired. First words occurred at a median of 24 months (range 10–96); 19/60 (31.7%) had no speech, and 9/42 (21.4%) had speech decline. Some lost speech around seizure onset. These deficits materially restrict communication, education, autonomy, and caregiver quality of life, although no NCBRS-specific EQ-5D, SF-36, PROMIS, or utility study was found. (sousa2014phenotypeandgenotype pages 10-11, sousa2014phenotypeandgenotype pages 3-3)

Seizures occurred in 39/61 (63.9%), with median onset at 18 months (range birth to 14 years); the typical onset window was approximately 1–2.5 years. Among seizure-affected cases, 23 had severe ID and only three had mild ID, although causality between epilepsy and developmental severity cannot be inferred. Suggested HPO: **Seizure (HP:0001250)** and, where clinically documented, specific seizure-type terms. EEG phenotype and antiseizure-drug response should be recorded at patient level because robust syndrome-wide response rates could not be verified from accessible full text. (sousa2014phenotypeandgenotype pages 10-11, sousa2014phenotypeandgenotype pages 3-3)

Behavioral problems are recognized but heterogeneous; reported manifestations include aggressive episodes, autism-like behavior, anxiety, and sleep disturbance. The retrieved evidence did not support reliable syndrome-wide percentages. A 35-year-old woman had occasional aggression associated with moderate hyperglycemia, but this is a single case and not evidence of a general metabolic-behavioral mechanism. (pretegiani2016nicolaides–baraitsersyndromedefining pages 1-2, sousa2014phenotypeandgenotype pages 1-2)

### Growth and craniofacial phenotype

- Small for gestational age/birth weight below −2 SD: 19/57 (33.3%).
- Birth length below −2 SD: 8/38 (21.1%).
- Reduced postnatal weight: 24/46 (52.2%); 36/46 (75%) were below the 50th centile and none were overweight.
- Short stature: 30/56 (53.6%).
- Microcephaly: 7/30 (23%) at birth and 34/52 (65.4%) later, demonstrating a predominantly postnatal or progressive pattern. (sousa2014phenotypeandgenotype pages 2-2, sousa2014phenotypeandgenotype pages 2-3, sousa2014phenotypeandgenotype pages 3-3)

Suggested HPO terms are **Short stature (HP:0004322)**, **Microcephaly (HP:0000252)**, **Postnatal growth retardation**, and **Failure to thrive** when individually documented.

Facial characteristics include a triangular facial shape in younger children, broad nasal base, thick alae, upturned nasal tip, rounded premaxilla, broad philtrum, thin upper vermilion, thick/everted lower vermilion, wide mouth, dense eyelashes, and increasingly coarse features. Coarse face occurred in 43/56 (76.6%), and progressive coarsening in 18/31 (58.0%). The gestalt can be subtle in infancy and becomes more recognizable with age. (sousa2014phenotypeandgenotype pages 4-4, sousa2014phenotypeandgenotype pages 3-3)

### Hair, skin, limbs, and skeleton

Sparse scalp hair is cardinal but age dependent and may improve. Eyebrows can be initially dense and later become less prominent; eyelashes generally remain dense. Non-scalp hypertrichosis occurred in 22/50 (44%), and eczema in 22/58 (37.9%). Suggested HPO: **Sparse scalp hair**, **Hypertrichosis (HP:0000998)**, and **Eczema (HP:0000964)**. (sousa2014phenotypeandgenotype pages 4-4)

Brachydactyly, broad distal phalanges, prominent/swollen interphalangeal joints, and broad fingertips are characteristic. Radiographs may show shortened distal phalanges, cone-shaped or ivory epiphyses, tarsal fusions, and broad first metatarsals. These findings affect dexterity, footwear, and occupational function, although formal functional scores are unavailable. Suggested HPO terms include **Brachydactyly (HP:0001156)**, **Broad distal phalanges**, **Prominent interphalangeal joints**, **Cone-shaped epiphyses**, and **Tarsal synostosis**. (mari2015coffin–sirisandnicolaides–baraitser pages 15-17)

### Other systems

Feeding problems affected 23/49 (46.9%), frequent infections 13/48 (27.1%), congenital cardiac defects 6/61 (9.8%), hearing loss 4/59 (6.8%), and hypospadias 1/36 males (2.8%). Myopia and astigmatism were reported, but complete denominators were unavailable. No malignancy occurred among the 61 reported patients. Rare vascular malformations, insulin resistance, and hypertrophic cardiomyopathy are case-level observations and should remain “possible/uncertain,” not cardinal disease features. (pretegiani2016nicolaides–baraitsersyndromedefining pages 1-2, sousa2014phenotypeandgenotype pages 4-4)

---

## 4. Genetic and molecular information

### Gene and variant interpretation

- **Gene:** SMARCA2; approved name above; Ensembl target **ENSG00000080503**.
- **Origin:** constitutional/germline; overwhelmingly de novo. Somatic SMARCA2 changes in cancer are biologically distinct and do not constitute NCBRS.
- **Variant classes:** predominantly missense; less commonly small in-frame deletions. A 32-kb de novo in-frame deletion removing part of the C-terminal helicase domain established that domain’s importance.
- **Population frequency:** causal variants are expected to be absent or exceptionally rare in gnomAD/other reference populations. Exact per-variant frequencies must be checked against the current genome build and database release.
- **ACMG/AMP:** classification should integrate de novo status, absence from population databases, ATPase-domain clustering, phenotype specificity, computational/functional evidence, and—where available—the NCBRS methylation episignature. An episignature is supporting functional evidence, not an automatic stand-alone pathogenic classification.

The disease is not adequately explained by simple haploinsufficiency. Earlier clinical literature favored a dominant-negative mechanism; engineered-cell evidence instead indicates mutation-dependent gain or redistribution of remodeling activity and retargeting of the paralogous SMARCA4 complex. The safest current annotation is **altered-function/dominant dysregulation of BAF chromatin remodeling**, with mechanism potentially variant dependent. (sousa2014phenotypeandgenotype pages 1-2, gao2019heterozygousmutationsin pages 1-3, gao2019heterozygousmutationsin pages 12-14)

### Epigenetics

Whole-blood methylation profiling identified 429 differentially methylated CpGs in eight NCBRS cases compared with 23 controls. A classifier tested in eight cases and 96 controls achieved reported 100% sensitivity and specificity and helped assess nine SMARCA2 VUS. This requires external validation because the development cohorts were small. (chaterdiehl2019newinsightsinto pages 1-2)

A broader 2024 study analyzed 97 neurodevelopmental-disorder cases—59 with known pathogenic/likely pathogenic variants and 38 test cases—and recovered the expected episignature in 90% of its validation cohort. It included a SMARCA2 p.Met856Val case and supported relationships between homologous SMARCA2/SMARCA4 residues. Current expert analysis warns that age, tissue/cell composition, mosaicism, hypomorphic alleles, intrafamilial variability, cohort size, and experimental design can yield intermediate or misleading scores. (trajkova2024dnamethylationanalysis pages 1-2, awamleh2024dnamethylationsignatures pages 3-6)

---

## 5. Environmental information

NCBRS is not caused by pollution, radiation, occupational exposure, smoking, alcohol, diet, exercise, or an infectious agent. No lifestyle factor is known to prevent the causal de novo variant. Standard health measures—adequate nutrition, vaccination, safe physical activity, sleep hygiene, and avoidance of seizure triggers—may reduce complications but do not alter the genetic cause. Zoonotic transmission and person-to-person transmission are not applicable.

---

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. A de novo non-truncating SMARCA2 variant alters a conserved ATPase/helicase residue.
2. Mutant SMARCA2 is incorporated into mammalian SWI/SNF/BAF chromatin-remodeling complexes.
3. ATP-dependent nucleosome remodeling and, importantly, genomic targeting of BAF complexes become dysregulated.
4. Enhancer accessibility and transcription-factor recruitment are reprogrammed during neurodevelopment.
5. Neural progenitor differentiation and neuronal gene programs are impaired, producing developmental delay, intellectual disability, speech impairment, epilepsy, and altered craniofacial/skeletal development.

SMARCA2 normally couples ATP hydrolysis to nucleosome remodeling. In engineered human embryonic stem cells carrying heterozygous K755R or R1159Q NCBRS variants, stem-cell maintenance appeared relatively normal, but differentiation into neural progenitors was severely impaired. Neural SOX3-dependent enhancers lost accessibility, whereas FRA2/AP-1 pioneered de novo astrocytic enhancers and retargeted both SMARCA2- and SMARCA4-containing complexes; approximately 97% of upregulated genes with increased accessibility were FRA2 bound. Ectopically activated programs included CD44, F3, CLU, FSTL1, and NFI-family genes. This is direct in-vitro human evidence, not merely pathway inference. (gao2019heterozygousmutationsin pages 1-3, gao2019heterozygousmutationsin pages 10-12, gao2019heterozygousmutationsin pages 12-14)

A concise exact statement from the 2019 study’s title captures the central finding: **“Heterozygous mutations in SMARCA2 reprogram the enhancer landscape by global retargeting of SMARCA4.”** The experiment supports an altered enhancer-selection mechanism rather than global absence of chromatin remodeling. (gao2019heterozygousmutationsin pages 1-3)

### Recent structural understanding

A 2023 Nature Genetics analysis placed neurodevelopmental variants across mSWI/SNF structures and found that non-truncating variants disproportionately affect cBAF and cluster at nucleosome interfaces, the ATPase-core/ARID-armadillo insertion site, Arp module, and DNA-binding domains. More than 70% of NDD-perturbed residues overlapped residues altered in cancer, although about 60% of the exact amino-acid substitutions were NDD specific. This is powerful structural/computational context, but it is not a disease-specific therapeutic study. DOI: https://doi.org/10.1038/s41588-023-01451-6; published July 2023.

### Suggested ontology annotations

- **GO biological process:** chromatin remodeling (GO:0006338); regulation of transcription by RNA polymerase II; neurogenesis; neural precursor-cell proliferation; neuron differentiation; regulation of chromatin accessibility.
- **GO molecular function:** ATP hydrolysis activity; ATP-dependent chromatin-remodeler activity; chromatin binding; nucleosome binding.
- **GO cellular component:** nucleus (GO:0005634); SWI/SNF superfamily-type complex; BAF complex; chromatin.
- **Cell Ontology:** neural stem cell, neural progenitor cell, neuroblast, neuron, astrocyte, and cranial neural-crest cell. Neural progenitors are directly supported by the engineered-cell work; the other cell types are mechanistically plausible and should be annotated with lower evidence strength. (gao2019heterozygousmutationsin pages 1-3, gao2019heterozygousmutationsin pages 10-12)

No validated NCBRS-specific metabolomic, lipidomic, proteomic, immune, inflammatory, oxidative-stress, single-cell, spatial-transcriptomic, organoid, or in-vivo CRISPR-screen signature was identified.

---

## 7. Anatomical structures affected

The **central nervous system** is the primary functional target, with developmental effects on cerebral networks governing cognition, language, motor control, and seizure susceptibility. Secondary systems include craniofacial structures, scalp/hair follicles, skin, phalanges and interphalangeal joints, and growth-related musculoskeletal tissues. Cardiac, auditory, ocular, and genitourinary involvement occurs in minorities. (pretegiani2016nicolaides–baraitsersyndromedefining pages 1-2, mari2015coffin–sirisandnicolaides–baraitser pages 15-17, sousa2014phenotypeandgenotype pages 4-4)

Suggested UBERON mappings include brain, cerebral cortex, scalp, hair follicle, skin, hand digit, foot digit, interphalangeal joint, epiphyseal plate, heart, inner ear, and external male genitalia. No consistent lateralization is described. At the subcellular level, the relevant compartment is the **nucleus/chromatin**, not mitochondria, lysosome, or endoplasmic reticulum.

---

## 8. Temporal development

NCBRS is congenital in cause but often not recognizable morphologically in the neonatal period. Developmental delay emerges in infancy; epilepsy most commonly begins in the first few years, with median onset 18 months. Microcephaly, sparse hair, facial coarsening, and joint prominence can become more evident postnatally, although scalp-hair density may later improve. (sousa2014phenotypeandgenotype pages 2-3, sousa2014phenotypeandgenotype pages 10-11, sousa2014phenotypeandgenotype pages 4-4, sousa2014phenotypeandgenotype pages 3-3)

The course is chronic and lifelong rather than relapsing-remitting. Developmental skills may continue to accrue slowly, but speech can plateau or regress, especially around uncontrolled seizures. No formal stages, remission pattern, or end-stage phase are recognized. Early childhood is the principal intervention window for communication therapy, developmental rehabilitation, nutritional support, and seizure control.

---

## 9. Inheritance and population

NCBRS follows an **autosomal-dominant** mechanism but is usually sporadic because variants arise de novo. The 61-person cohort contained 35 males and 26 females, median age 10 years (range 2–33), with no ancestry-based pattern. No consanguinity, founder effect, or convincing familial recurrence was reported, apart from affected monozygotic twins. (sousa2014phenotypeandgenotype pages 2-2, sousa2014phenotypeandgenotype pages 1-2)

Penetrance for classic ATPase-domain pathogenic variants appears high, but expressivity is variable from borderline/mild intellectual impairment to severe disability and epilepsy. Anticipation is not expected. Gonadal mosaicism has not been quantified; therefore recurrence after an apparently de novo event is low but not zero. Carrier frequency is not meaningful for a predominantly de novo dominant disorder.

No reliable population prevalence or incidence per 100,000 was found. Orphanet classifies it as rare, and published cohorts are too selected to calculate prevalence. There is no established ethnic, geographic, or sex predilection.

---

## 10. Diagnostics

### Clinical recognition

Clinical suspicion is strongest when developmental delay—especially severe speech impairment—is accompanied by seizures, postnatal microcephaly/short stature, sparse scalp hair, coarse or triangular facies, brachydactyly, and prominent interphalangeal joints. Clinical gestalt alone is insufficient because the phenotype evolves with age and overlaps Coffin–Siris and other chromatinopathies. (sousa2014phenotypeandgenotype pages 11-11, sousa2014phenotypeandgenotype pages 1-2)

### Recommended molecular workflow

1. **Trio exome or genome sequencing** is the preferred broad first-line strategy for an unexplained syndromic neurodevelopmental disorder; it detects de novo SMARCA2 SNVs/indels and alternative diagnoses.
2. A neurodevelopmental/epilepsy or chromatinopathy panel should include **SMARCA2** and relevant differential genes.
3. If phenotype is classic and broad sequencing is unavailable, sequence SMARCA2, with particular attention to exons encoding the ATPase/helicase region; older guidance prioritized exons 15–25.
4. Add exon-level deletion/duplication analysis, MLPA, read-depth CNV analysis, or genome sequencing to detect in-frame intragenic deletions.
5. Confirm parental samples to establish de novo status and evaluate possible mosaicism.
6. Use a validated peripheral-blood DNA-methylation episignature assay as an adjunct for a VUS or phenotypically ambiguous result. (sousa2014phenotypeandgenotype pages 11-11, chaterdiehl2019newinsightsinto pages 1-2, trajkova2024dnamethylationanalysis pages 1-2)

Chromosomal microarray can identify larger deletions but is not the most sensitive test for canonical missense NCBRS. Karyotype and FISH have low routine yield unless a structural rearrangement is suspected. Mitochondrial, repeat-expansion, liquid-biopsy, proteomic, and metabolomic testing are not disease-specific diagnostic methods.

### Clinical evaluations after diagnosis

Recommended baseline assessments include growth and nutrition; developmental, speech-language, and behavioral evaluation; neurologic examination and EEG if seizures or concerning events occur; hearing and ophthalmologic testing; cardiac examination with echocardiography when clinically indicated; musculoskeletal/hand assessment; dermatologic and dental review; and renal/genitourinary assessment guided by findings. Brain MRI is appropriate for seizures, regression, abnormal examination, or concern for structural/vascular abnormalities, but no pathognomonic MRI biomarker is established.

### Differential diagnosis

The closest differential is Coffin–Siris syndrome/ARID1B-related disorder. Other considerations include Wiedemann–Steiner, Coffin–Lowry, Cornelia de Lange, Kabuki, KBG, DOORS, Pitt–Hopkins, and other BAF/chromatin-remodeling disorders. NCBRS favors sparse hair, prominent interphalangeal joints and broad distal phalanges rather than classic fifth-digit hypoplasia. Exome sequencing is valuable because clinically suspected CSS/NCBRS cohorts contain unexpected molecular diagnoses. (sousa2014phenotypeandgenotype pages 11-11, mari2015coffin–sirisandnicolaides–baraitser pages 15-17)

No newborn biochemical screen or population screening program exists. Testing is phenotype-driven or familial after a molecular diagnosis.

---

## 11. Outcome and prognosis

No valid 5-year/10-year survival, mortality rate, or disease-specific life-expectancy estimate exists. Adults into at least their third and fourth decades have been reported, but the small, young cohorts preclude concluding that lifespan is normal. The largest cohort’s age range ended at 33 years, while a separate case was 35. (pretegiani2016nicolaides–baraitsersyndromedefining pages 1-2, sousa2014phenotypeandgenotype pages 1-2)

The main long-term burden is neurodevelopmental disability: limited speech, dependence in activities of daily living, epilepsy, feeding/growth difficulty, behavioral problems, and motor or hand-function limitations. Severe ID correlated with epilepsy, speech impairment, short stature, and microcephaly. Prognosis is variable; certain motif-VI variants appear more severe, whereas variants at Pro883, Leu946, or Ala1201 may be milder, but these associations are not sufficiently powered for individual prediction. (sousa2014phenotypeandgenotype pages 10-10, sousa2014phenotypeandgenotype pages 10-11)

No validated prognostic biomarker exists. The blood episignature is diagnostic/functional rather than proven prognostic. Recovery to typical development is not expected, although early communication support, rehabilitation, nutrition, and seizure control can improve function and participation.

---

## 12. Treatment and current applications

There is no approved therapy that corrects SMARCA2 or BAF-complex dysfunction. Treatment is individualized:

- **Epilepsy:** standard antiseizure medication chosen by seizure type and EEG; rescue plans for prolonged seizures; specialist management for drug resistance. No genotype-specific drug or robust NCBRS response-rate hierarchy could be verified.
- **Development:** early physical, occupational, speech-language, feeding, behavioral, and educational therapies; augmentative and alternative communication is particularly important when speech is absent.
- **Nutrition/GI:** growth monitoring, dietetic assessment, swallow study when indicated, reflux/constipation management, and enteral feeding if oral intake is unsafe or inadequate.
- **Musculoskeletal:** physiotherapy, orthotics, monitoring of joint limitations/contractures and spine; orthopedic intervention based on functional impairment.
- **Hearing/vision/dental/skin:** hearing aids, refractive correction, preventive dental care, emollients/topical anti-inflammatory therapy for eczema, and routine specialty care.
- **Cardiac/genitourinary:** lesion-specific surveillance or intervention rather than universal syndrome-specific surgery.

Suggested NCIT intervention concepts include anticonvulsant therapy, physical therapy, occupational therapy, speech and language therapy, behavioral therapy, nutritional support, enteral nutrition, hearing aid, corrective lenses, and genetic counseling. Exact NCIT identifiers should be resolved against the target NCIT release.

No gene replacement, CRISPR editing, ASO, siRNA, mRNA, cell therapy, immunotherapy, or targeted small-molecule therapy is clinically available. Although chromatin remodelers are drug targets in oncology, inhibiting a broadly essential developmental complex is not presently a validated NCBRS strategy.

The only directly relevant registered study found was **NCT01793168**, a recruiting, prospective, observational rare-disease registry that includes NCBRS, targets 20,000 participants across all included diseases, and offers online/Sanford Health enrollment. It is not an interventional treatment trial and has no NCBRS efficacy endpoint. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT01793168. (NCT01793168 chunk 4)

---

## 13. Prevention

Primary prevention by lifestyle or vaccination is not possible because the disorder usually results from a de novo constitutional variant. Secondary prevention consists of early molecular diagnosis, prompt seizure recognition, developmental intervention, and surveillance for feeding, hearing, visual, cardiac, and orthopedic complications. Tertiary prevention focuses on avoiding aspiration/malnutrition, seizure injury/status epilepticus, loss of mobility, communication deprivation, and preventable dental or skin disease.

After identifying the familial variant, genetic counseling should explain autosomal-dominant inheritance, high expected penetrance for classic pathogenic variants, low-but-nonzero recurrence from possible parental gonadal mosaicism, and a 50% transmission risk if an affected individual reproduces. Prenatal diagnosis and preimplantation genetic testing are technically possible when the causal variant is known. Routine population carrier or newborn screening is not justified.

---

## 14. Other species and natural disease

SMARCA2 and ATP-dependent SWI/SNF mechanisms are evolutionarily conserved across vertebrates and invertebrates, supporting comparative functional work. However, no well-established naturally occurring veterinary analogue of NCBRS, breed predisposition, cross-species transmission, or zoonotic potential was identified. NCBI Taxonomy examples relevant to experimental ortholog studies include human (*Homo sapiens*, 9606), mouse (*Mus musculus*, 10090), zebrafish (*Danio rerio*, 7955), and fruit fly (*Drosophila melanogaster*, 7227). Species-specific ortholog gene IDs should be retrieved from the current NCBI/Alliance release before database ingestion.

---

## 15. Model organisms and experimental systems

The strongest disease-specific model in the retrieved literature is **engineered human embryonic stem cells differentiated into neural progenitor cells**, carrying heterozygous K755R or R1159Q SMARCA2 variants. It reproduces impaired neural differentiation and reveals enhancer retargeting, altered SOX3/FRA2 programs, and SMARCA4 redistribution. Its principal limitation is that a two-dimensional developmental cell system cannot reproduce epilepsy, cognition, craniofacial morphogenesis, growth, or whole-organism pharmacology. (gao2019heterozygousmutationsin pages 1-3, gao2019heterozygousmutationsin pages 10-12, gao2019heterozygousmutationsin pages 12-14)

Generic Smarca2 knockout or perturbation models can elucidate BAF biology, but they should not automatically be labeled NCBRS models because canonical human disease is usually caused by specific non-truncating altered-function alleles rather than complete gene loss. No thoroughly validated NCBRS knock-in mouse, zebrafish, Drosophila, patient-iPSC organoid, or natural animal model with quantified recapitulation of the full human phenotype was established in the retrieved evidence. This is a major translational gap.

---

## Recent developments and expert interpretation, 2023–2024

1. **Structural grouping of BAF variants (July 2023):** mapping neurodevelopmental variants onto mSWI/SNF structures highlighted recurrent perturbation of nucleosome interfaces and ATPase structural hubs. This strengthens domain-aware variant interpretation but does not replace functional or clinical evidence. DOI: https://doi.org/10.1038/s41588-023-01451-6.
2. **Episignature implementation (April–July 2024):** recent work supports blood methylation profiling as a practical second-line assay for uncertain chromatinopathy variants. In a broader NDD cohort, expected signatures were recovered in 90% of validation cases. Experts emphasize that intermediate scores can reflect mosaicism, hypomorphic alleles, age, tissue composition, or familial variability—not simply “positive” versus “negative.” DOI: https://doi.org/10.1016/j.xhgg.2024.100309, published July 2024; review DOI: https://doi.org/10.1007/s00439-023-02544-2, published April 2024. (trajkova2024dnamethylationanalysis pages 1-2, awamleh2024dnamethylationsignatures pages 3-6)
3. **Clinical reality:** research has advanced mechanistic and diagnostic resolution, but there remains no disease-modifying intervention, validated molecular prognostic test, or NCBRS-specific interventional trial. (NCT01793168 chunk 4)

## Key evidence quotations

- The 2018 methylation study’s abstract stated that a machine-learning model could **“resolve ambiguous clinical cases, reclassify those with variants of unknown significance, and identify previously undiagnosed subjects.”** This supports diagnostic utility but not treatment or prognosis.
- The 2024 chromatinopathy perspective states that DNA-methylation signatures **“serve as both a research avenue for elucidating disease pathophysiology and a clinical diagnostic tool,”** particularly for VUS classification. (awamleh2024dnamethylationsignatures pages 3-6)
- The foundational clinical synthesis characterized NCBRS through progressive hair, facial, and joint findings and emphasized that its phenotypic spectrum is probably broader than initially recognized. (sousa2014phenotypeandgenotype pages 1-2)

## Evidence limitations

The evidence base is constrained by rarity, referral bias, small cohorts, incomplete denominators, cross-sectional rather than longitudinal assessment, and limited adult follow-up. Many management recommendations are expert-practice extrapolations rather than trial-tested NCBRS guidelines. Rare cardiac, vascular, endocrine, or imaging findings should not be promoted to core associations without replication. Ontology terms above are suggested mappings and should be validated against current HPO, GO, CL, UBERON, NCIT, and MONDO releases before production ingestion.

References

1. (sousa2014phenotypeandgenotype pages 2-2): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

2. (sousa2014phenotypeandgenotype pages 1-2): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

3. (chaterdiehl2019newinsightsinto pages 1-2): Eric Chater-Diehl, Resham Ejaz, Cheryl Cytrynbaum, Michelle T. Siu, Andrei Turinsky, Sanaa Choufani, Sarah J. Goodman, Omar Abdul-Rahman, Melanie Bedford, Naghmeh Dorrani, Kendra Engleman, Josue Flores-Daboub, David Genevieve, Roberto Mendoza-Londono, Wendy Meschino, Laurence Perrin, Nicole Safina, Sharron Townshend, Stephen W. Scherer, Evdokia Anagnostou, Amelie Piton, Matthew Deardorff, Michael Brudno, David Chitayat, and Rosanna Weksberg. New insights into dna methylation signatures: smarca2 variants in nicolaides-baraitser syndrome. BMC Medical Genomics, Jul 2019. URL: https://doi.org/10.1186/s12920-019-0555-y, doi:10.1186/s12920-019-0555-y. This article has 48 citations and is from a peer-reviewed journal.

4. (gao2019heterozygousmutationsin pages 1-3): Fangjian Gao, Nicholas J. Elliott, Josephine Ho, Alexzander Sharp, Maxim N. Shokhirev, and Diana C. Hargreaves. Heterozygous mutations in smarca2 reprogram the enhancer landscape by global retargeting of smarca4. Molecular cell, 75:891-904.e7, Sep 2019. URL: https://doi.org/10.1016/j.molcel.2019.06.024, doi:10.1016/j.molcel.2019.06.024. This article has 72 citations and is from a highest quality peer-reviewed journal.

5. (trajkova2024dnamethylationanalysis pages 1-2): Slavica Trajkova, Jennifer Kerkhof, Matteo Rossi Sebastiano, Lisa Pavinato, Enza Ferrero, Chiara Giovenino, Diana Carli, Eleonora Di Gregorio, Roberta Marinoni, Giorgia Mandrile, Flavia Palermo, Silvia Carestiato, Simona Cardaropoli, Verdiana Pullano, Antonina Rinninella, Elisa Giorgio, Tommaso Pippucci, Paola Dimartino, Jessica Rzasa, Kathleen Rooney, Haley McConkey, Aleksandar Petlichkovski, Barbara Pasini, Elena Sukarova-Angelovska, Christopher M. Campbell, Kay Metcalfe, Sarah Jenkinson, Siddharth Banka, Alessandro Mussa, Giovanni Battista Ferrero, Bekim Sadikovic, and Alfredo Brusco. Dna methylation analysis in patients with neurodevelopmental disorders improves variant interpretation and reveals complexity. Jul 2024. URL: https://doi.org/10.1016/j.xhgg.2024.100309, doi:10.1016/j.xhgg.2024.100309. This article has 23 citations and is from a peer-reviewed journal.

6. (NCT01793168 chunk 4):  Rare Disease Patient Registry & Natural History Study - Coordination of Rare Diseases at Sanford. Sanford Health. 2010. ClinicalTrials.gov Identifier: NCT01793168

7. (OpenTargets Search: Nicolaides-Baraitser syndrome-SMARCA2): Open Targets Query (Nicolaides-Baraitser syndrome-SMARCA2, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (pretegiani2016nicolaides–baraitsersyndromedefining pages 1-2): Elena Pretegiani, Francesca Mari, Alessandra Renieri, Silvana Penco, and Maria Teresa Dotti. Nicolaides–baraitser syndrome: defining a phenotype. Journal of Neurology, 263:1659-1660, Jun 2016. URL: https://doi.org/10.1007/s00415-016-8194-0, doi:10.1007/s00415-016-8194-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

9. (sousa2014phenotypeandgenotype pages 10-10): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

10. (sousa2014phenotypeandgenotype pages 3-3): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

11. (sousa2014phenotypeandgenotype pages 10-11): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

12. (sousa2014phenotypeandgenotype pages 2-3): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

13. (sousa2014phenotypeandgenotype pages 4-4): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

14. (gao2019heterozygousmutationsin pages 10-12): Fangjian Gao, Nicholas J. Elliott, Josephine Ho, Alexzander Sharp, Maxim N. Shokhirev, and Diana C. Hargreaves. Heterozygous mutations in smarca2 reprogram the enhancer landscape by global retargeting of smarca4. Molecular cell, 75:891-904.e7, Sep 2019. URL: https://doi.org/10.1016/j.molcel.2019.06.024, doi:10.1016/j.molcel.2019.06.024. This article has 72 citations and is from a highest quality peer-reviewed journal.

15. (gao2019heterozygousmutationsin pages 12-14): Fangjian Gao, Nicholas J. Elliott, Josephine Ho, Alexzander Sharp, Maxim N. Shokhirev, and Diana C. Hargreaves. Heterozygous mutations in smarca2 reprogram the enhancer landscape by global retargeting of smarca4. Molecular cell, 75:891-904.e7, Sep 2019. URL: https://doi.org/10.1016/j.molcel.2019.06.024, doi:10.1016/j.molcel.2019.06.024. This article has 72 citations and is from a highest quality peer-reviewed journal.

16. (awamleh2024dnamethylationsignatures pages 3-6): Zain Awamleh, Sarah Goodman, Sanaa Choufani, and Rosanna Weksberg. Dna methylation signatures for chromatinopathies: current challenges and future applications. Human Genetics, 143:551-557, Apr 2024. URL: https://doi.org/10.1007/s00439-023-02544-2, doi:10.1007/s00439-023-02544-2. This article has 26 citations and is from a peer-reviewed journal.

17. (sousa2014phenotypeandgenotype pages 11-11): Sérgio B. Sousa and Raoul C. Hennekam. Phenotype and genotype in nicolaides–baraitser syndrome. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 166:302-314, Sep 2014. URL: https://doi.org/10.1002/ajmg.c.31409, doi:10.1002/ajmg.c.31409. This article has 99 citations.

18. (mari2015coffin–sirisandnicolaides–baraitser pages 15-17): Francesca Mari, Annabella Marozza, Maria Antonietta Mencarelli, Caterina Lo Rizzo, Chiara Fallerini, Laura Dosa, Chiara Di Marco, Giulia Carignani, Margherita Baldassarri, Paola Cianci, Rossella Vivarelli, Marina Vascotto, Salvatore Grosso, Pietro Rubegni, Carla Caffarelli, Elena Pretegiani, Michele Fimiani, Livia Garavelli, Francesca Cristofoli, Joris R. Vermeesch, Ranuccio Nuti, Maria Teresa Dotti, Paolo Balestri, Joussef Hayek, Angelo Selicorni, and Alessandra Renieri. Coffin–siris and nicolaides–baraitser syndromes are a common well recognizable cause of intellectual disability. Brain and Development, 37(5):527-536, May 2015. URL: https://doi.org/10.1016/j.braindev.2014.08.009, doi:10.1016/j.braindev.2014.08.009. This article has 54 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Nicolaides-Baraitser_Syndrome-deep-research-falcon_artifacts/artifact-00.md)