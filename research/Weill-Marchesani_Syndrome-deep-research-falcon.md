---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T00:24:26.588866'
end_time: '2026-08-01T00:34:21.212653'
duration_seconds: 594.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Weill-Marchesani syndrome
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
  path: Weill-Marchesani_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Weill-Marchesani syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Weill-Marchesani syndrome** covering all of the
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
- **Disease Name:** Weill-Marchesani syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Weill-Marchesani syndrome** covering all of the
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


# Weill–Marchesani syndrome: comprehensive disease-characteristics report

## Executive summary

Weill–Marchesani syndrome (WMS) is a rare, congenital, Mendelian extracellular-matrix disorder in the acromelic-dysplasia spectrum. Its defining combination is **microspherophakia/lenticular myopia, ectopia lentis and secondary glaucoma together with short stature, brachydactyly and joint stiffness**. Thick skin, a pseudomuscular habitus and cardiovascular abnormalities occur variably. Estimated prevalence is approximately **1 in 100,000**, but this is based on rare-disease summaries rather than population surveillance. Both autosomal-dominant and autosomal-recessive forms exist: dominant disease is principally associated with heterozygous **FBN1** variants, whereas recessive disease results from biallelic **ADAMTS10, ADAMTS17, or LTBP2** variants. The common biological theme is defective fibrillin-rich extracellular microfibrils and altered tissue-specific growth-factor microenvironments. (li2026anovelhomozygous pages 1-2, protasiuk2025weillmarchesanisyndromea pages 1-2)

The most important preventable morbidity is visual loss from lens-induced angle closure and glaucoma. There is no disease-modifying drug, gene therapy, or validated molecular prognostic biomarker; current care combines early molecular diagnosis, detailed anterior-segment assessment, lifelong glaucoma surveillance, complication-directed lens/glaucoma surgery, cardiac monitoring, orthopedic/rehabilitative care and genetic counseling. (protasiuk2025weillmarchesanisyndromea pages 3-5, protasiuk2025weillmarchesanisyndromea pages 1-2)

The following compact curation table summarizes disease, phenotype, mechanism, anatomy, diagnostic and intervention mappings.

| Domain | Finding | Suggested ontology/identifier | Evidence/notes |
|---|---|---|---|
| Disease | Weill-Marchesani syndrome (rare hereditary connective-tissue / acromelic dysplasia syndrome with ocular, skeletal, and sometimes cardiac involvement) | ORPHA:3447; MONDO:0018097 *(verification recommended)*; Mendelian disease | Estimated prevalence about 1 in 100,000; phenotype and gene evidence are disease-level aggregated from published case reports/reviews, not EHR-derived (li2026anovelhomozygous pages 1-2, protasiuk2025weillmarchesanisyndromea pages 1-2) |
| Disease subtypes | Historically subdivided by gene/inheritance into AD and AR forms; “WMS4” used for ADAMTS17-related disease in recent literature | OMIM subtype labels *verification needed* | Recent sources explicitly distinguish AD FBN1-associated disease from AR ADAMTS10/ADAMTS17/LTBP2-associated disease; exact OMIM subtype mapping should be checked directly in OMIM before database load (li2026anovelhomozygous pages 1-2, huang2023abnormallensthickening pages 1-2) |
| Synonym/related label | Weill-Marchesani-like syndrome | Disease synonym/related concept *(verification needed)* | Used especially for some LTBP2-associated families and overlapping phenotypes; may not always be nosologically identical to classic WMS (chen2024autosomaldominantweillmarchesanilike pages 7-8) |
| Gene / inheritance | FBN1: autosomal dominant WMS | HGNC: FBN1 | Dominant WMS linked to heterozygous FBN1 variants; often associated with ectopia lentis/joint stiffness and acromelic dysplasia overlap (li2026anovelhomozygous pages 1-2, protasiuk2025weillmarchesanisyndromea pages 1-2, arnaud2024pathogenicvariantsaffecting pages 8-8) |
| Gene / inheritance | ADAMTS10: autosomal recessive WMS | HGNC: ADAMTS10 | Established AR cause; recent quantitative review of 19 ADAMTS10 cases found universal microspherophakia, high myopia, short stature, brachydactyly, and joint stiffness (li2026anovelhomozygous pages 1-2, li2026anovelhomozygous pages 4-6) |
| Gene / inheritance | ADAMTS17: autosomal recessive WMS / WMS4 | HGNC: ADAMTS17 | ADAMTS17-related disease shows ocular-predominant presentation and may lack heart defects/joint stiffness compared with other forms (huang2023abnormallensthickening pages 1-2) |
| Gene / inheritance | LTBP2: autosomal recessive WMS; atypical dominant WMS-like families also reported | HGNC: LTBP2 | Classic teaching supports AR disease; a 2024 Chinese family report proposed dominant WMS-like inheritance from haplotypic LTBP2 variants, requiring cautious interpretation (li2026anovelhomozygous pages 1-2, chen2024autosomaldominantweillmarchesanilike pages 7-8) |
| Variant class | Germline pathogenic variants include missense, nonsense, frameshift, splice-site, exon deletions, and in-frame/deletion events depending on gene | ACMG/AMP classification framework | Somatic origin is not implicated; reported disease variants are germline. ADAMTS10 frameshift c.1560_1575dup p.Ile526Valfs*51 classified pathogenic in 2026 report (li2026anovelhomozygous pages 1-2, li2026anovelhomozygous pages 4-6) |
| Phenotype | Microspherophakia / spherophakia | HPO term suggestion: Microspherophakia | Core ocular trait; 100% in ADAMTS10 literature synthesis cited in recent report (19/19) (li2026anovelhomozygous pages 4-6) |
| Phenotype | High myopia / lenticular myopia | HPO term suggestion: High myopia; Lenticular myopia | Universal in ADAMTS10 synthesis (19/19); in WMS4 child, progressive myopia tracked with lens thickening despite normal axial length (li2026anovelhomozygous pages 4-6, huang2023abnormallensthickening pages 1-2) |
| Phenotype | Ectopia lentis / lens subluxation | HPO term suggestion: Ectopia lentis | Frequently reported across genetic subtypes; especially emphasized in dominant FBN1 disease and WMS-like families (protasiuk2025weillmarchesanisyndromea pages 1-2, chen2024autosomaldominantweillmarchesanilike pages 7-8) |
| Phenotype | Glaucoma, often secondary angle closure / phacomorphic mechanism | HPO term suggestion: Glaucoma; Angle-closure glaucoma | Glaucoma in 47.4% (9/19) in ADAMTS10 synthesis; literature range 44.4%–51%; mean onset in one cited series ~20 ± 13 years, but childhood acute attacks can occur (li2026anovelhomozygous pages 4-6, li2026anovelhomozygous pages 7-9, li2026anovelhomozygous pages 9-10) |
| Phenotype | Short stature | HPO term suggestion: Short stature | Universal in recent ADAMTS10 synthesis; common across WMS spectrum (protasiuk2025weillmarchesanisyndromea pages 1-2, li2026anovelhomozygous pages 4-6) |
| Phenotype | Brachydactyly | HPO term suggestion: Brachydactyly | Universal in recent ADAMTS10 synthesis; useful for syndromic recognition in ophthalmology settings (li2026anovelhomozygous pages 4-6, huang2023abnormallensthickening pages 1-2) |
| Phenotype | Joint stiffness / contractures | HPO term suggestion: Joint stiffness | Universal in ADAMTS10 synthesis; may be absent or less conspicuous in ADAMTS17-related WMS4 (li2026anovelhomozygous pages 4-6, huang2023abnormallensthickening pages 1-2) |
| Phenotype | Thick skin / muscular habitus | HPO term suggestion: Thickened skin; Muscular hypertrophy/pseudomuscular build | Recurrently described in reviews and classic WMS descriptions; frequency not well quantified in retrieved recent primary evidence (li2026anovelhomozygous pages 1-2, protasiuk2025weillmarchesanisyndromea pages 1-2) |
| Phenotype | Cardiac abnormalities (valves/other cardiovascular findings) | HPO term suggestion: Abnormality of the cardiovascular system; Heart valve abnormality | Cardiac abnormalities in 55.6% (10/18) of literature cases in one ADAMTS10 review; ADAMTS17-related WMS4 may have fewer/no heart defects (li2026anovelhomozygous pages 4-6, huang2023abnormallensthickening pages 1-2) |
| Onset/course | Usually congenital or childhood-onset, chronic lifelong condition | Temporal descriptor: congenital/childhood onset | Ocular findings often first recognized in childhood; WMS4 can present insidiously as “high myopia” before glaucoma or overt ectopia lentis (li2026anovelhomozygous pages 1-2, huang2023abnormallensthickening pages 1-2) |
| Anatomy affected | Crystalline lens, zonule/ciliary zonule, anterior chamber angle | UBERON term suggestions: lens of eye; suspensory ligament of lens / ciliary zonule; anterior chamber angle of eye | Ocular biometry/imaging shows thick, small-diameter lenses, shallow anterior chambers, and zonular pathology driving glaucoma risk (li2026anovelhomozygous pages 9-10, huang2023abnormallensthickening pages 1-2, wang2019adamts10inactivationin pages 24-29) |
| Anatomy affected | Cornea / anterior segment | UBERON term suggestions: cornea; anterior segment of eyeball | Increased corneal thickness reported in WMS; anterior segment crowding is clinically important for angle-closure risk (li2026anovelhomozygous pages 9-10) |
| Anatomy affected | Growth plate, long bone skeleton, digits, joints | UBERON term suggestions: epiphyseal growth plate; long bone; digit; synovial joint | Short stature/brachydactyly implicate disturbed skeletogenesis and endochondral growth (mead2022proteolysisoffibrillin2 pages 32-34) |
| Anatomy affected | Heart valves / cardiovascular connective tissue | UBERON term suggestions: heart valve; cardiovascular system | Cardiovascular manifestations are less consistent than ocular/skeletal features but important for surveillance (protasiuk2025weillmarchesanisyndromea pages 1-2, li2026anovelhomozygous pages 4-6) |
| Cell/tissue context | Connective tissue fibroblasts, chondrocytes, ocular microfibril-rich tissues | CL term suggestions: fibroblast; chondrocyte | Mechanistic studies and models implicate ECM-producing stromal cells and growth-plate chondrocytes; exact cell ontology IDs should be verified during curation (mead2022proteolysisoffibrillin2 pages 32-34, wang2019adamts10inactivationin pages 24-29) |
| Mechanism | Extracellular matrix and fibrillin microfibril assembly disorder | GO term suggestion: extracellular matrix organization; microfibril assembly | Strong convergence across FBN1, ADAMTS10, ADAMTS17, and LTBP2 supports a shared microfibril/ECM pathway (protasiuk2025weillmarchesanisyndromea pages 1-2, mead2022proteolysisoffibrillin2 pages 32-34, hubmacher2015adamtsproteinsas pages 10-10) |
| Mechanism | ADAMTS10 proteolytic regulation of fibrillin-2 in ocular tissues | GO term suggestion: proteolysis; extracellular matrix disassembly | Mouse/in vitro work showed reduced fibrillin-2 cleavage and persistence of ocular microfibrils after Adamts10 inactivation (wang2019adamts10inactivationin pages 24-29) |
| Mechanism | Local tissue-microenvironment dysregulation rather than classic Marfan-like generalized TGF-β activation | GO term suggestion: regulation of signaling receptor activity; extracellular structure organization | FBN1 WMS models suggest altered local microenvironments and collagen regulation; mechanism diverges from canonical Marfan pathogenesis (mead2022proteolysisoffibrillin2 pages 32-34) |
| Mechanism | BMP-Smad pathway involvement in skeletogenesis (especially ADAMTS17 biology) | GO term suggestion: BMP signaling pathway; endochondral bone morphogenesis | Experimental data in Adamts17 biology support BMP-Smad1/5/8 modulation during skeletogenesis; relevance to human WMS is plausible but still mechanistically incomplete (mead2022proteolysisoffibrillin2 pages 32-34) |
| Mechanism | LTBP2-related zonule/microfibril and elastic-fiber biology | GO term suggestion: elastic fiber assembly; ciliary zonule development | LTBP2 is implicated in microfibril formation and ocular connective tissue integrity; precise causal chain to all WMS manifestations remains incompletely resolved (chen2024autosomaldominantweillmarchesanilike pages 7-8, hubmacher2015adamtsproteinsas pages 10-10) |
| Diagnostics | Clinical recognition based on syndromic combination of microspherophakia/high myopia/ectopia lentis plus short stature and brachydactyly | Clinical feature set *(no single universal formal criteria retrieved)* | No universally adopted formal diagnostic criteria were retrieved; diagnosis is phenotype-led and then molecularly confirmed (protasiuk2025weillmarchesanisyndromea pages 1-2, huang2023abnormallensthickening pages 1-2) |
| Diagnostics | Ophthalmic biometry and imaging | Test suggestions: slit-lamp exam; ocular biometry; Pentacam; ultrasound biomicroscopy; IOLMaster | 2023 WMS4 case used multiple imaging modalities to document lens thickening and reduced equatorial diameter over 3 years (huang2023abnormallensthickening pages 1-2) |
| Diagnostics | Intraocular pressure assessment / gonioscopy for glaucoma surveillance | Test suggestions: tonometry; gonioscopy | Essential because glaucoma is common and may arise acutely in anatomically crowded eyes (li2026anovelhomozygous pages 9-10, li2026anovelhomozygous pages 7-9) |
| Diagnostics | Echocardiography / cardiovascular evaluation | Test suggestion: echocardiography | Recommended because cardiac involvement occurs in a substantial subset, especially some AR forms (protasiuk2025weillmarchesanisyndromea pages 1-2, li2026anovelhomozygous pages 4-6) |
| Diagnostics | Molecular testing | WES/WGS/gene panel; confirmatory Sanger sequencing | WES plus Sanger was used in recent ADAMTS10 and ADAMTS17 cases; gene panels for ectopia lentis/anterior segment dysgenesis/connective-tissue disease are reasonable (li2026anovelhomozygous pages 1-2, huang2023abnormallensthickening pages 1-2) |
| Differential diagnosis | Marfan syndrome, isolated ectopia lentis, acromicric dysplasia, geleophysic dysplasia, other microspherophakia syndromes | Related disease term suggestions | Distinguishing clues include short stature/brachydactyly/joint stiffness rather than tall stature; acromelic dysplasia spectrum overlaps at FBN1 TB5 domain (protasiuk2025weillmarchesanisyndromea pages 1-2, arnaud2024pathogenicvariantsaffecting pages 8-8) |
| Intervention | Peripheral iridotomy / laser iridotomy | NCIT-style term suggestion: Peripheral Iridotomy | Used prophylactically or therapeutically for pupillary block/angle closure risk in WMS (protasiuk2025weillmarchesanisyndromea pages 3-5, protasiuk2025weillmarchesanisyndromea pages 1-2) |
| Intervention | Lensectomy / lens extraction | NCIT-style term suggestion: Lensectomy | Key intervention for microspherophakia-related glaucoma or lens-induced crowding; recent pediatric case used staged bilateral lens extraction (protasiuk2025weillmarchesanisyndromea pages 3-5, li2026anovelhomozygous pages 9-10) |
| Intervention | Anterior vitrectomy | NCIT-style term suggestion: Anterior Vitrectomy | Used in advanced ocular surgical management alongside lensectomy in reviews/case-based practice (protasiuk2025weillmarchesanisyndromea pages 3-5) |
| Intervention | Intraocular lens implantation | NCIT-style term suggestion: Intraocular Lens Implantation | May be deferred initially in high-risk eyes; individualized surgical planning is emphasized (protasiuk2025weillmarchesanisyndromea pages 3-5, li2026anovelhomozygous pages 9-10) |
| Intervention | Glaucoma drainage or filtering procedures | NCIT-style term suggestions: Glaucoma Surgery; Molteno Implantation; ExPRESS Shunt Placement | Described for refractory glaucoma in review literature (protasiuk2025weillmarchesanisyndromea pages 3-5) |
| Intervention | Multidisciplinary supportive care | NCIT-style term suggestions: Ophthalmologic Monitoring; Cardiology Follow-Up; Orthopedic Care; Physical Therapy | No disease-modifying pharmacotherapy identified; management is complication-directed and longitudinal (protasiuk2025weillmarchesanisyndromea pages 3-5, protasiuk2025weillmarchesanisyndromea pages 1-2) |
| Prevention | Genetic counseling, cascade testing, reproductive counseling | Clinical service term suggestion: Genetic Counseling | Most actionable prevention relates to family-risk assessment for AD or AR inheritance and early ophthalmic surveillance of at-risk relatives (li2026anovelhomozygous pages 1-2, protasiuk2025weillmarchesanisyndromea pages 1-2) |
| Prognosis | Morbidity driven mainly by progressive refractive error, ectopia lentis, and glaucoma; vision can be preserved with early detection/intervention | Outcome descriptor *(no validated prognostic biomarker retrieved)* | Acute glaucoma can occur in childhood, but mean glaucoma onset in one cited literature set was ~20 years; survival/life-expectancy data were not retrieved (li2026anovelhomozygous pages 7-9, li2026anovelhomozygous pages 9-10) |
| Model organisms | Adamts10-null mouse | Model suggestion: Mus musculus Adamts10 loss-of-function | Recapitulates ocular microfibril persistence and supports ADAMTS10-mediated fibrillin-2 cleavage mechanism; limited for full human multisystem spectrum (wang2019adamts10inactivationin pages 24-29) |
| Model organisms | Fbn1 WMS mouse model | Model suggestion: Mus musculus Fbn1 WMS-associated deletion model | Replicates thick skin, short stature, and brachydactyly, supporting tissue-microenvironment mechanism distinct from Marfan syndrome (mead2022proteolysisoffibrillin2 pages 32-34) |
| Evidence limitations | Most evidence comes from small case reports/series and mechanistic mouse studies; phenotype frequencies differ by gene and publication bias is likely | Evidence-quality note | No randomized trials retrieved; no disease-specific interventional ClinicalTrials.gov evidence found in the search set; several detailed 2024 papers were cited in references but not fully available in retrieved text (protasiuk2025weillmarchesanisyndromea pages 1-2, li2026anovelhomozygous pages 10-10, li2026anovelhomozygous pages 9-10) |


*Table: This table summarizes key disease, gene, phenotype, anatomy, mechanism, diagnostic, and management mappings for Weill-Marchesani syndrome. It is designed as a compact curation aid and flags ontology identifiers or claims that should be verified before formal database ingestion.*

## 1. Disease information

### Definition and identifiers

WMS is a hereditary connective-tissue disorder and acromelic skeletal dysplasia involving the eye, skeleton, joints, skin and, inconsistently, cardiovascular system. Suggested identifiers are **ORPHA:3447**, **MONDO:0018097** and **OMIM 277600** for the classic/recessive disease concept; subtype-level OMIM assignments should be checked directly in OMIM before database ingestion because nomenclature varies by gene and “WMS-like” versus classic WMS. The disorder does not appear to have a uniquely specific ICD-10 code and will generally require a broader congenital connective-tissue or ocular diagnosis code. MeSH indexing is usually through the disease name and related terms such as microspherophakia or ectopia lentis. (li2026anovelhomozygous pages 1-2)

Synonyms include **Weill-Marchesani syndrome**, **Weill–Marchesani syndrome**, **brachymorphia–ectopia lentis syndrome**, and, for overlapping presentations, **Weill-Marchesani-like syndrome**. “WMS4” is used for ADAMTS17-related disease. WMS-like should not automatically be treated as exactly equivalent to classic WMS, particularly in atypical LTBP2 families. (huang2023abnormallensthickening pages 1-2, chen2024autosomaldominantweillmarchesanilike pages 7-8)

The evidence summarized here is **aggregated disease-level evidence** from published families, case reports, small cohorts, reviews and experimental models—not individual EHR-derived data. The rarity of WMS and gene-specific ascertainment produce substantial publication and referral bias.

## 2. Etiology, risk and protective factors

### Causal factors

WMS is primarily genetic. Established causes are germline pathogenic variants in:

* **FBN1**—usually heterozygous, autosomal dominant;
* **ADAMTS10**—biallelic, autosomal recessive;
* **ADAMTS17**—biallelic, autosomal recessive;
* **LTBP2**—classically biallelic and recessive, although a 2024 four-generation family suggested an unusual dominant WMS-like mechanism from two variants in cis. (li2026anovelhomozygous pages 1-2, chen2024autosomaldominantweillmarchesanilike pages 7-8)

The 2024 LTBP2 family contained 25 examined relatives, nine clinically affected individuals and seven children of uncertain status. The reported haplotype combined **c.2657C>A (p.Thr886Lys)** with deletion of exons 25–36 and segregated with ectopia lentis, short stature and obesity. This expands the proposed inheritance spectrum but should be regarded as family-level evidence requiring replication. Publication: May 2024; DOI: https://doi.org/10.1159/000538844. (chen2024autosomaldominantweillmarchesanilike pages 7-8)

### Risk factors

The principal risks are inheritance of a causal allele, an affected parent in dominant WMS, two carrier parents in recessive WMS, consanguinity and family history. For each pregnancy, a heterozygous affected parent generally confers a 50% transmission probability; two carriers of the same recessive condition confer 25% affected, 50% carrier and 25% unaffected probabilities, assuming full Mendelian segregation.

No reproducible environmental, infectious, occupational, dietary, sex-specific or lifestyle risk factors are established. Atropine did not cause WMS, but pharmacologic pupillary dilation precipitated acute angle closure in one anatomically predisposed child, illustrating that environmental or iatrogenic exposures may trigger complications rather than disease initiation. (li2026anovelhomozygous pages 7-9, li2026anovelhomozygous pages 9-10)

### Protective factors and gene–environment interaction

No validated protective allele, diet, drug or lifestyle exposure prevents WMS. Early diagnosis, avoidance of unsupervised mydriatic/anticholinergic exposure in narrow-angle eyes, and surveillance are best considered complication prevention rather than etiologic protection. Formal gene–environment interaction studies are unavailable.

## 3. Phenotypes

### Ocular phenotype

* **Microspherophakia/spherophakia** (suggested HPO: Microspherophakia) is a small-equatorial-diameter, abnormally thick and spherical lens. It causes increased lenticular power, high myopia, zonular instability, pupillary block and anterior-segment crowding.
* **High or lenticular myopia** (HPO: High myopia) often appears in childhood and may be mistaken for ordinary axial myopia.
* **Ectopia lentis/lens subluxation** (HPO: Ectopia lentis), iridodonesis and shallow anterior chamber are common.
* **Secondary glaucoma**, especially angle-closure/phacomorphic or pupillary-block glaucoma (HPO: Glaucoma; Angle-closure glaucoma), is the major vision-threatening complication.

A recent synthesis of 19 ADAMTS10-associated patients reported microspherophakia and high myopia in **19/19**, and glaucoma in **9/19 (47.4%)**. The wider published glaucoma range was 44.4–51%; a cited ocular series reported glaucoma in 81/159 eyes with mean onset **20 ± 13 years**. These estimates are not population frequencies and are vulnerable to ascertainment bias. (li2026anovelhomozygous pages 7-9, li2026anovelhomozygous pages 4-6)

A 2023 three-year longitudinal WMS4 case provides direct evidence of progression. At age eight, lens thickness was 4.38/4.31 mm and equatorial diameter 7.33/7.17 mm; three years later thickness increased to 4.49/4.48 mm while diameter remained approximately 7.32/7.21 mm. Myopia progressed despite normal axial length. The authors’ abstract states that the report “highlights the abnormal thickening of the lens in WMS4 compared to the physiological thinning process during childhood.” Publication: January 2023; DOI: https://doi.org/10.3389/fmed.2022.1021489. (huang2023abnormallensthickening pages 1-2)

### Skeletal, joint and integumentary phenotype

Short stature (HPO: Short stature), brachydactyly (HPO: Brachydactyly), short hands/feet, joint stiffness or contractures (HPO: Joint stiffness), thickened skin and a muscular or pseudomuscular build are characteristic. A 19-person ADAMTS10 synthesis reported short stature, brachydactyly and joint stiffness in **100%**, but this is a selected genotype-specific literature sample rather than a universal WMS estimate. ADAMTS17-related WMS4 may be more ocular-predominant and can lack conspicuous joint stiffness. (huang2023abnormallensthickening pages 1-2, li2026anovelhomozygous pages 4-6)

### Cardiovascular and other manifestations

Heart-valve abnormalities and other cardiovascular findings are variably described. In the recent ADAMTS10 literature synthesis, cardiac abnormalities occurred in **10/18 (55.6%)** previously reported cases. Apparent rates differed by variant category, including 2/2 compound-heterozygous splice cases and 6/9 homozygous missense cases, but numbers are far too small for clinical prediction. Hearing impairment and intellectual disability have occasionally been reported; neither is a defining or well-quantified phenotype. (li2026anovelhomozygous pages 4-6, li2026anovelhomozygous pages 7-9, li2026anovelhomozygous pages 1-2)

### Functional and quality-of-life effect

Visual blur, repeated examinations, glaucoma, surgery and possible irreversible visual-field loss can impair schooling, mobility, work and independence. Short stature and joint limitation can restrict reach, dexterity and physical activity. No WMS-specific EQ-5D, SF-36, PROMIS or validated quality-of-life dataset was identified.

## 4. Genetic and molecular information

All established WMS variants are **germline**; a somatic disease mechanism is not recognized. Reported classes include missense, nonsense, frameshift, splice-altering and in-frame variants, plus exon-level deletions. Variant interpretation should follow ACMG/AMP criteria and incorporate segregation, population frequency, predicted loss of function, phenotype specificity and functional evidence.

A recent ADAMTS10 example is **NM_030957.4:c.1560_1575dup; p.Ile526Valfs*51**, a homozygous 16-bp duplication predicted to truncate the protein before thrombospondin type-1 and cysteine-rich regions and/or undergo nonsense-mediated decay. It was classified pathogenic using PVS1+PM3+PM2; both unaffected parents were heterozygous carriers. (li2026anovelhomozygous pages 7-9, li2026anovelhomozygous pages 4-6)

A 2023 ADAMTS17 case carried compound-heterozygous missense variants **c.2984G>A (p.Arg995Gln)** and **c.2254A>G (p.Ile752Val)**. Their reported association with WMS4 is clinically informative, although individual missense classifications should always be rechecked in current ClinVar/gnomAD and against updated segregation/functional evidence. (huang2023abnormallensthickening pages 1-2)

FBN1-related acromelic dysplasias cluster around functionally important fibrillin-1 regions, particularly the fifth TGF-β-binding-protein-like domain (TB5). However, 2024 data showed that TB5 variants can also produce classic Marfan syndrome, demonstrating that domain location alone does not establish phenotype. Publication: March 2024; DOI: https://doi.org/10.1136/jmg-2023-109646. (arnaud2024pathogenicvariantsaffecting pages 8-8)

No validated modifier genes, WMS-specific epigenetic signature, recurrent chromosomal rearrangement, anticipation phenomenon or established germline-mosaicism rate is known. Large deletions can occur within a causal gene, but WMS is not primarily an aneuploidy or contiguous-gene disorder. Population allele frequencies should be retrieved variant-by-variant from current gnomAD; pathogenic alleles are expected to be absent or extremely rare.

## 5. Environmental information

No toxin, radiation exposure, pollutant, dietary pattern, smoking behavior, alcohol exposure or infectious agent is known to cause WMS. Environmental and lifestyle variables may influence general cardiovascular, musculoskeletal and ocular health but have not been shown to modify penetrance. Mydriasis can provoke angle closure in predisposed eyes and therefore warrants ophthalmic caution. (li2026anovelhomozygous pages 7-9)

## 6. Mechanism and pathophysiology

### Upstream molecular defect

FBN1 encodes fibrillin-1, the principal structural component of 10–12-nm extracellular microfibrils. ADAMTS10 and ADAMTS17 are secreted metalloproteases that interact functionally with fibrillin-rich matrices. LTBP2 is an extracellular microfibril-associated latent-TGF-β-binding-protein-family member important to the ciliary zonule and elastic-fiber organization. Human genetics therefore converges on defective **extracellular-matrix organization and microfibril assembly/homeostasis**. Suggested GO terms include extracellular matrix organization, microfibril assembly, proteolysis, elastic-fiber assembly, BMP signaling and endochondral ossification. (chen2024autosomaldominantweillmarchesanilike pages 7-8, hubmacher2015adamtsproteinsas pages 10-10)

### Ocular causal chain

ADAMTS10 deficiency reduces fibrillin-2 processing. In Adamts10-null mice, fibrillin-2 accumulates in the zonule and vitreous. In vitro, active ADAMTS10 cleaved a 185-kDa fibrillin-2 construct and generated an approximately 100-kDa fragment, whereas catalytically inactive ADAMTS10 did not. The supported chain is: **ADAMTS10 loss → reduced fibrillin-2 proteolysis/persistent ocular microfibrils → abnormal zonular/lens development → microspherophakia and lens instability → lenticular myopia, anterior chamber crowding and secondary angle closure/glaucoma**. This is strong model/in-vitro evidence, though direct confirmation of every intermediate in human eyes remains incomplete. PMID **30201140**; DOI: https://doi.org/10.1016/j.matbio.2018.09.004. (mead2022proteolysisoffibrillin2 pages 32-34, wang2019adamts10inactivationin pages 24-29)

### Skeletal and connective-tissue causal chain

Disrupted fibrillin/ADAMTS matrix organization alters local growth-factor presentation and growth-plate extracellular matrix. Fibrillin-1 WMS models support tissue-specific microenvironmental disturbance and altered dermal collagen production rather than the broad TGF-β activation emphasized in Marfan syndrome. ADAMTS17 experimental work also implicates BMP–SMAD1/5/8 regulation during skeletogenesis. The likely chain is **microfibril dysfunction → altered chondrocyte matrix/signaling and endochondral growth → short long bones, short digits and joint limitation**. Relevant cells include fibroblasts (CL: fibroblast), growth-plate chondrocytes (CL: chondrocyte) and ocular stromal/zonular matrix-producing cells. (mead2022proteolysisoffibrillin2 pages 32-34)

No disease-specific metabolomic, lipidomic, proteomic, single-cell, spatial-transcriptomic or integrated multi-omic signature is validated. Immune activation, autoimmunity, infection, mitochondrial dysfunction and primary metabolic enzyme deficiency are not established central mechanisms.

## 7. Anatomical structures affected

Primary sites are bilateral crystalline lenses, ciliary zonules, iris–lens/anterior-chamber-angle anatomy and other anterior-segment tissues; long bones, epiphyseal growth plates, digits and joints; skin/dermal connective tissue; and, variably, heart valves and cardiovascular connective tissue. Suggested UBERON mappings include lens of eye, ciliary zonule/suspensory ligament of lens, anterior chamber of eye, cornea, epiphyseal growth plate, long bone, digit, synovial joint, skin and heart valve.

In one recent child, corneal thickness was 714/724 μm versus a reported control mean of 549.97 ± 25.78 μm; anterior chambers measured 1.70/1.80 mm and axial lengths 21.75/21.18 mm. These findings illustrate anterior-segment crowding but should not be treated as diagnostic cutoffs. Ocular disease is usually bilateral, although severity and glaucoma damage may be asymmetric. (li2026anovelhomozygous pages 9-10)

At subcellular level, the relevant compartment is predominantly extracellular: fibrillin microfibrils, elastic-fiber-associated matrix and pericellular matrix. Suggested GO cellular-component terms are extracellular matrix and proteinaceous extracellular matrix.

## 8. Temporal development and natural history

WMS is congenital and lifelong, but recognition is often delayed until childhood myopia, lens displacement or glaucoma. Skeletal proportions and brachydactyly emerge during growth; joint stiffness is chronic. The ocular course may be insidious and progressive: increasing lens thickness/power, zonular instability, shallow angles and glaucoma risk. The 2023 WMS4 follow-up directly documented progressive lens thickening over three years. (huang2023abnormallensthickening pages 1-2)

A 2024 Journal of Medical Genetics study reported natural history and genotype–phenotype correlations in **18 new cases** plus literature review (Marzin et al., volume 61, pages 109–116; DOI: https://doi.org/10.1136/jmg-2023-109288). Retrieved text confirmed the study’s existence and scope but did not expose its complete tables; exact subtype frequencies should therefore be taken from the original paper before database loading. (li2026anovelhomozygous pages 10-10)

There is no accepted stage classification, remission pattern or end-stage definition. The disease does not spontaneously remit. The critical intervention window is before irreversible glaucomatous optic neuropathy or amblyopia develops.

## 9. Inheritance and population

Prevalence is commonly cited as approximately **1/100,000**; robust incidence, sex-ratio, carrier-frequency and mortality estimates are unavailable. WMS occurs across ancestries, with no established ethnic restriction. Consanguinity increases the probability of recessive disease, while family clustering occurs in both inheritance modes. (li2026anovelhomozygous pages 1-2, protasiuk2025weillmarchesanisyndromea pages 1-2)

Penetrance and expressivity are incompletely quantified and vary by gene and variant. The 2024 dominant LTBP2 family included young carriers of uncertain status, consistent with age-dependent ascertainment or possible reduced penetrance. No established anticipation exists. Founder effects may occur in individual populations, but no globally dominant founder allele was identified in the retrieved evidence. (chen2024autosomaldominantweillmarchesanilike pages 7-8)

## 10. Diagnostics

### Clinical and ophthalmic evaluation

Suspect WMS when childhood high myopia or ectopia lentis co-occurs with microspherophakia, short stature, brachydactyly or stiff joints. Recommended evaluation includes refraction, slit-lamp examination after careful angle assessment, tonometry, gonioscopy, optic-nerve/visual-field assessment when age appropriate, axial-length and lens biometry, anterior-segment OCT or ultrasound biomicroscopy, corneal tomography/pachymetry, and dilated retinal examination when safe. The 2023 case used IOLMaster 700, Pentacam and ultrasound biomicroscopy to distinguish lenticular from axial myopia. (huang2023abnormallensthickening pages 1-2)

Systemic assessment should include height and proportions, hands/feet, range of motion, skin and muscular habitus, blood pressure, cardiac examination and baseline echocardiography. Routine blood/urine chemistry, biopsy, EEG, EMG or metabolic assays are not diagnostic.

### Genetic testing

A practical strategy is an ectopia-lentis/microspherophakia or connective-tissue panel containing **FBN1, ADAMTS10, ADAMTS17 and LTBP2**, with deletion/duplication analysis. Phenotype-guided single-gene testing is reasonable in a strongly suggestive family. Trio or family WES is useful for atypical or panel-negative cases and was diagnostic in recent ADAMTS10/ADAMTS17 reports; WGS can identify noncoding and structural variants missed by WES. Candidate variants require orthogonal confirmation and segregation analysis. (li2026anovelhomozygous pages 1-2, huang2023abnormallensthickening pages 1-2)

CMA, karyotyping, FISH, mitochondrial sequencing and repeat-expansion testing are not first-line unless additional findings suggest another diagnosis. RNA sequencing may help resolve a suspected splice variant but is not validated as routine WMS testing.

### Differential diagnosis

Major alternatives are Marfan syndrome, isolated ectopia lentis from ADAMTSL4, homocystinuria, sulfite oxidase/molybdenum-cofactor deficiency, isolated microspherophakia, geleophysic dysplasia, acromicric dysplasia, congenital contractural arachnodactyly and other anterior-segment dysgeneses. Short stature, brachydactyly, stiff joints and a spherical lens favor WMS; tall stature, arachnodactyly and aortic-root disease favor Marfan syndrome. Homocystinuria requires urgent biochemical exclusion when clinically plausible.

No universally accepted scoring criteria or population/newborn-screening program exists. Cascade molecular testing is appropriate after a familial variant is established.

## 11. Outcome and prognosis

Life-expectancy, five- or ten-year survival and disease-specific mortality have not been quantified. Most morbidity is ophthalmic and musculoskeletal rather than fatal. Untreated angle closure can cause irreversible optic-nerve damage and blindness; early recognition and appropriate surgery can preserve useful vision. Refractive error and joint limitations are chronic, and surgery does not correct the underlying matrix disorder.

Prognosis depends on age at recognition, angle anatomy, intraocular pressure, optic-nerve damage, lens position, amblyopia, surgical complexity and cardiac involvement. No validated molecular prognostic biomarker exists. In a selected ADAMTS10 dataset, loss-of-function groups appeared to have more glaucoma, but sample sizes—e.g., two nonsense and one frameshift case—are insufficient for clinical genotype-based prediction. (li2026anovelhomozygous pages 4-6)

## 12. Treatment and current implementation

There is no approved disease-modifying pharmacotherapy. Refractive correction and amblyopia treatment are appropriate early measures. Pressure-lowering drops may be used, but lens-induced pupillary block or crowded-angle anatomy often requires intervention.

**Ocular procedures** include peripheral laser iridotomy for pupillary block risk, lensectomy/lens extraction for microspherophakia-related crowding or uncontrolled glaucoma, anterior vitrectomy when indicated, individualized intraocular-lens implantation, and filtering or drainage surgery for refractory glaucoma. Reported procedures include Molteno and ExPRESS shunts. Suggested NCIT intervention concepts are Peripheral Iridotomy, Lensectomy, Anterior Vitrectomy, Intraocular Lens Implantation and Glaucoma Surgery. (protasiuk2025weillmarchesanisyndromea pages 3-5)

A recent eight-year-old underwent bilateral lens extraction; IOL placement was initially deferred in one eye because of malignant-glaucoma risk and subsequently individualized after anterior-chamber reformation and pressure control. This is useful real-world evidence but not a comparative trial. (li2026anovelhomozygous pages 9-10)

Systemic care includes periodic cardiology review/echocardiography, orthopedic assessment, physiotherapy or occupational therapy for joint limitation, hearing evaluation if symptomatic and educational support. No WMS-specific pharmacogenomic guidance exists. Growth-hormone efficacy is unproven and should not be extrapolated from isolated reports in overlapping acromelic dysplasias.

No disease-specific interventional ClinicalTrials.gov study, gene therapy, CRISPR therapy, cell therapy, RNA therapy or targeted biologic was identified. Management recommendations are therefore based on rare-disease reviews, case series and extrapolation from glaucoma/ectopia-lentis practice rather than randomized trials. (protasiuk2025weillmarchesanisyndromea pages 3-5, protasiuk2025weillmarchesanisyndromea pages 1-2)

## 13. Prevention

Primary prevention through lifestyle change or vaccination is not applicable. Genetic counseling is the central preventive strategy. Once the familial pathogenic variant is known, options include cascade testing, prenatal diagnosis and preimplantation genetic testing, subject to local regulations and informed patient choice.

Secondary prevention consists of early ophthalmic examination of affected or at-risk relatives, careful assessment before pharmacologic dilation, periodic intraocular-pressure/angle/optic-nerve monitoring and cardiac surveillance. Tertiary prevention includes timely iridotomy or lens/glaucoma surgery, amblyopia management, rehabilitation and adaptation for joint or visual disability. No vaccine, chemoprophylaxis or population screening program is indicated.

## 14. Other species and natural disease

No well-established naturally occurring veterinary disorder identical to human WMS was identified. Related fibrillin/ADAMTS-family diseases occur in animals, but they should not be labeled WMS without equivalent genotype and phenotype. Musladin–Lueke syndrome in Beagles is an **ADAMTSL2** founder disorder with stiff skin and joint contractures and is a model of geleophysic-dysplasia biology, not WMS itself. WMS is noninfectious and has no zoonotic or cross-species transmission potential.

Orthologues of FBN1, ADAMTS10, ADAMTS17 and LTBP2 are evolutionarily conserved in vertebrates, supporting comparative analysis of microfibrils, ocular zonules and skeletal development.

## 15. Model organisms

The strongest WMS-relevant models are genetically engineered mice:

* **Adamts10-null mouse:** persistence of fibrillin-2-rich ocular microfibrils in the zonule/vitreous, directly supporting defective fibrillin-2 clearance. It is valuable for ocular microfibril biology but does not reproduce every human systemic feature. (wang2019adamts10inactivationin pages 24-29)
* **Fbn1 WMS-associated deletion mouse:** recapitulates thick skin, short stature and brachydactyly and supports altered local microenvironments/collagen regulation rather than a Marfan phenotype. (mead2022proteolysisoffibrillin2 pages 32-34)
* **Adamts17-related experimental models:** support a role in skeletogenesis and BMP–SMAD1/5/8 modulation, but translation to the complete human WMS4 phenotype remains incomplete. (mead2022proteolysisoffibrillin2 pages 32-34)

Cellular approaches include patient or engineered fibroblasts for fibrillin/collagen deposition and microfibril assembly, plus recombinant-protein cleavage assays. No validated WMS organoid, iPSC disease platform, zebrafish therapeutic screen or humanized model was identified in the retrieved literature.

## Recent developments and expert assessment

The important 2023–2024 developments are: longitudinal recognition of abnormal childhood lens thickening in ADAMTS17-associated WMS4; publication of an 18-case natural-history/genotype–phenotype cohort; an atypical dominant LTBP2 WMS-like family; and evidence that FBN1 TB5-domain location alone does not uniquely predict an acromelic phenotype. Together, these findings reinforce three expert conclusions: WMS is genetically and phenotypically heterogeneous; quantitative ocular biometry can reveal disease before overt glaucoma; and genotype–phenotype rules remain provisional because cohorts are small. (huang2023abnormallensthickening pages 1-2, chen2024autosomaldominantweillmarchesanilike pages 7-8, li2026anovelhomozygous pages 10-10, arnaud2024pathogenicvariantsaffecting pages 8-8)

A later 2026 ADAMTS10 synthesis supplies useful numerical estimates—19/19 core ocular and skeletal features, 9/19 glaucoma and 10/18 cardiac abnormalities—but postdates the requested 2023–2024 priority window and combines highly selected published cases. It should be used as supportive rather than definitive epidemiologic evidence. (li2026anovelhomozygous pages 4-6)

## Evidence limitations

WMS lacks large registries, population-based epidemiology, standardized diagnostic criteria, controlled treatment trials, validated patient-reported outcomes and robust genotype-specific penetrance estimates. Several claims derive from individual families or literature-assembled cohorts. Exact HPO, UBERON, GO, NCIT, MONDO and subtype OMIM identifiers should be validated against current ontology releases before production ingestion. The retrieved evidence supported selected exact abstract statements and PMIDs, but not every paper exposed a PubMed identifier or complete abstract; DOI URLs and publication dates are therefore supplied where available.

References

1. (li2026anovelhomozygous pages 1-2): Mengyang Li, Rong Bai, Yuanyuan Lian, Can Shu, Huiping Li, and Xun-Lun Sheng. A novel homozygous adamts10 frameshift variant in weill-marchesani syndrome in a chinese family. BMC Medical Genomics, Feb 2026. URL: https://doi.org/10.1186/s12920-026-02308-7, doi:10.1186/s12920-026-02308-7. This article has 1 citations and is from a peer-reviewed journal.

2. (protasiuk2025weillmarchesanisyndromea pages 1-2): Agnieszka Protasiuk, Agata Żak-Gontarz, Rafał Sierzpowski, Patrycja Tymoszuk, Bartosz Kasperek, Katarzyna Augustowska, Kamila Budzyńska, Klaudia Klimczak, and Laura Loryś. Weill-marchesani syndrome: a comprehensive review of pathogenesis, clinical features, and management. Lekarz Wojskowy, 103:206-210, Sep 2025. URL: https://doi.org/10.53301/lw/204988, doi:10.53301/lw/204988. This article has 0 citations.

3. (protasiuk2025weillmarchesanisyndromea pages 3-5): Agnieszka Protasiuk, Agata Żak-Gontarz, Rafał Sierzpowski, Patrycja Tymoszuk, Bartosz Kasperek, Katarzyna Augustowska, Kamila Budzyńska, Klaudia Klimczak, and Laura Loryś. Weill-marchesani syndrome: a comprehensive review of pathogenesis, clinical features, and management. Lekarz Wojskowy, 103:206-210, Sep 2025. URL: https://doi.org/10.53301/lw/204988, doi:10.53301/lw/204988. This article has 0 citations.

4. (huang2023abnormallensthickening pages 1-2): Junting Huang, Kailai Nie, Xinpin Lv, Yuting Liu, Guiqi Yang, Junjiang Fu, Longqian Liu, and Hongbin Lv. Abnormal lens thickening in a child with weill–marchesani syndrome 4: a 3-year follow-up case report. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2022.1021489, doi:10.3389/fmed.2022.1021489. This article has 2 citations.

5. (chen2024autosomaldominantweillmarchesanilike pages 7-8): Juan Chen, Jifeng Wan, Jiayi Jin, Guangming Jin, Yongxin Zheng, Danying Zheng, and Liuxueying Zhong. Autosomal dominant weill-marchesani-like syndrome in a chinese family due to novel haplotypic mutations in ltbp2. Ophthalmic research, May 2024. URL: https://doi.org/10.1159/000538844, doi:10.1159/000538844. This article has 6 citations and is from a peer-reviewed journal.

6. (arnaud2024pathogenicvariantsaffecting pages 8-8): Pauline Arnaud, Zakaria Mougin, Genevieve Baujat, Valérie Drouin-Garraud, Salima El Chehadeh, Laurent Gouya, Sylvie Odent, Guillaume Jondeau, Catherine Boileau, Nadine Hanna, and Carine Le Goff. Pathogenic variants affecting the tb5 domain of the fibrillin-1 protein: not only in geleophysic/acromicric dysplasias but also in marfan syndrome. Journal of Medical Genetics, 61:469-476, Mar 2024. URL: https://doi.org/10.1136/jmg-2023-109646, doi:10.1136/jmg-2023-109646. This article has 2 citations and is from a domain leading peer-reviewed journal.

7. (li2026anovelhomozygous pages 4-6): Mengyang Li, Rong Bai, Yuanyuan Lian, Can Shu, Huiping Li, and Xun-Lun Sheng. A novel homozygous adamts10 frameshift variant in weill-marchesani syndrome in a chinese family. BMC Medical Genomics, Feb 2026. URL: https://doi.org/10.1186/s12920-026-02308-7, doi:10.1186/s12920-026-02308-7. This article has 1 citations and is from a peer-reviewed journal.

8. (li2026anovelhomozygous pages 7-9): Mengyang Li, Rong Bai, Yuanyuan Lian, Can Shu, Huiping Li, and Xun-Lun Sheng. A novel homozygous adamts10 frameshift variant in weill-marchesani syndrome in a chinese family. BMC Medical Genomics, Feb 2026. URL: https://doi.org/10.1186/s12920-026-02308-7, doi:10.1186/s12920-026-02308-7. This article has 1 citations and is from a peer-reviewed journal.

9. (li2026anovelhomozygous pages 9-10): Mengyang Li, Rong Bai, Yuanyuan Lian, Can Shu, Huiping Li, and Xun-Lun Sheng. A novel homozygous adamts10 frameshift variant in weill-marchesani syndrome in a chinese family. BMC Medical Genomics, Feb 2026. URL: https://doi.org/10.1186/s12920-026-02308-7, doi:10.1186/s12920-026-02308-7. This article has 1 citations and is from a peer-reviewed journal.

10. (wang2019adamts10inactivationin pages 24-29): Lauren W. Wang, Wendy E. Kutz, Timothy J. Mead, Lauren C. Beene, Shweta Singh, Michael W. Jenkins, Dieter P. Reinhardt, and Suneel S. Apte. Adamts10 inactivation in mice leads to persistence of ocular microfibrils subsequent to reduced fibrillin-2 cleavage. Matrix biology : journal of the International Society for Matrix Biology, 77:117-128, Apr 2019. URL: https://doi.org/10.1016/j.matbio.2018.09.004, doi:10.1016/j.matbio.2018.09.004. This article has 61 citations.

11. (mead2022proteolysisoffibrillin2 pages 32-34): Timothy J. Mead, Daniel R. Martin, Lauren W. Wang, Stuart A. Cain, Cagri Gulec, Elisabeth Cahill, Joseph Mauch, Dieter P. Reinhardt, Cecilia W. Lo, Clair Baldock, and Suneel S. Apte. Proteolysis of fibrillin-2 microfibrils is essential for normal skeletal development. eLife, Feb 2021. URL: https://doi.org/10.1101/2021.02.03.429587, doi:10.1101/2021.02.03.429587. This article has 40 citations and is from a domain leading peer-reviewed journal.

12. (hubmacher2015adamtsproteinsas pages 10-10): Dirk Hubmacher and Suneel S. Apte. Adamts proteins as modulators of microfibril formation and function. Matrix biology : journal of the International Society for Matrix Biology, 47:34-43, Sep 2015. URL: https://doi.org/10.1016/j.matbio.2015.05.004, doi:10.1016/j.matbio.2015.05.004. This article has 196 citations.

13. (li2026anovelhomozygous pages 10-10): Mengyang Li, Rong Bai, Yuanyuan Lian, Can Shu, Huiping Li, and Xun-Lun Sheng. A novel homozygous adamts10 frameshift variant in weill-marchesani syndrome in a chinese family. BMC Medical Genomics, Feb 2026. URL: https://doi.org/10.1186/s12920-026-02308-7, doi:10.1186/s12920-026-02308-7. This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Weill-Marchesani_Syndrome-deep-research-falcon_artifacts/artifact-00.md)