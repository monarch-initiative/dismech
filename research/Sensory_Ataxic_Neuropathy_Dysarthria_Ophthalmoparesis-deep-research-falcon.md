---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-03T23:23:23.160288'
end_time: '2026-06-03T23:33:21.935243'
duration_seconds: 598.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis** covering all of the
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
- **Disease Name:** Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis** covering all of the
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


# Sensory Ataxic Neuropathy, Dysarthria, and Ophthalmoparesis (SANDO) — Disease Characteristics Research Report

**Target disease:** Sensory ataxic neuropathy, dysarthria, and ophthalmoparesis (SANDO) (POLG-related ataxia-neuropathy spectrum)  
**Category:** Mendelian (nuclear gene defect affecting mtDNA maintenance)  
**MONDO / Orphanet / ICD / MeSH:** Not captured in the retrieved sources used for this report (see “Evidence gaps”).  

## Executive summary
SANDO is a clinical syndrome defined by the triad of **sensory ataxic neuropathy**, **dysarthria**, and **ophthalmoparesis/ophthalmoplegia**, and is best understood today as part of the broader **POLG-related ataxia-neuropathy spectrum (ANS)**, an umbrella term that includes disorders previously referred to as MIRAS and SANDO. (specchio2020polg1relatedepilepsyreview pages 1-3, rahman2019polgrelateddisordersand pages 4-6) The dominant disease mechanism is impaired mitochondrial DNA (mtDNA) replication/repair due to pathogenic variants in **POLG**, leading to **mtDNA deletions and/or depletion**, mitochondrial respiratory chain dysfunction (often demonstrated as **COX-deficient ragged-red fibers** in muscle), and progressive neuro(myopathic) degeneration. (wong2008molecularandclinical pages 1-2, mchugh2010sensoryataxicneuropathy pages 1-2) A key real-world management point is that **valproic acid is contraindicated in all patients with POLG mutations** due to risk of precipitating liver failure. (rahman2019polgrelateddisordersand pages 4-6) The most notable 2023–2024 development relevant to disease modification is an **open-label phase 2 trial of enteral deoxycytidine/deoxythymidine (dC/dT)** in POLG-related disorders (ClinicalTrials.gov **NCT04802707**) with encouraging interim clinical and biomarker signals. (pekeles2024safetyandefficacy pages 1-2)

## Evidence map (knowledge-base ready)
| Category | Key item | Short notes |
|---|---|---|
| Definition/Identifiers | Disease name | Sensory ataxic neuropathy, dysarthria, and ophthalmoparesis (SANDO); defined within the POLG-related ataxia-neuropathy spectrum (ANS) (specchio2020polg1relatedepilepsyreview pages 1-3, wong2008molecularandclinical pages 1-2) |
| Definition/Identifiers | Synonym/relationship | ANS is an umbrella term that includes disorders previously referred to as MIRAS and SANDO (rahman2019polgrelateddisordersand pages 4-6) |
| Definition/Identifiers | Identifier status | OMIM for SANDO was not directly captured in readable evidence; MONDO/Orphanet/ICD/MeSH not captured in retrieved sources (rahman2019polgrelateddisordersand pages 4-6) |
| Etiology | Causal gene | POLG is the principal causal gene; it encodes mitochondrial DNA polymerase gamma required for mtDNA replication/repair (pekeles2024safetyandefficacy pages 1-2, specchio2020polg1relatedepilepsyreview pages 1-3) |
| Etiology | Inheritance | Biallelic pathogenic POLG variants are common in recessive POLG disease/SANDO-spectrum presentations; homozygous p.A467T and compound heterozygous cases are reported (mchugh2010sensoryataxicneuropathy pages 1-2, rotig2024distinctclinicalcourses pages 1-2) |
| Etiology | Recurrent variants | A467T, W748S, and G848S are major recurrent POLG variants across POLG-related disease cohorts; p.A467T is repeatedly linked to SANDO cases (specchio2020polg1relatedepilepsyreview pages 1-3, mchugh2010sensoryataxicneuropathy pages 3-4) |
| Core phenotypes | Sensory ataxia/neuropathy | Ataxia is often early and dominant, frequently driven by proprioceptive loss from sensory neuropathy; absent sensory nerve action potentials and sensory axonal neuropathy are typical (wei2023phenotypicvariabilityof pages 1-4, mchugh2010sensoryataxicneuropathy pages 1-2, lipponen2024mitataxhereditaryataxias pages 39-42) |
| Core phenotypes | Dysarthria and ophthalmoparesis | Progressive dysarthria with ophthalmoparesis/ophthalmoplegia and ptosis form the classic clinical triad; gaze limitation is often bilateral and progressive (wei2023phenotypicvariabilityof pages 1-4, ali2024mitochondrialchronicprogressive pages 1-3, mchugh2010sensoryataxicneuropathy pages 1-2) |
| Additional features | Other neurologic features | Dysphagia, exercise intolerance, seizures/epilepsy, hearing loss, myopathy, neuropathic pain, and encephalopathy may occur; PEO can appear late in some patients (wei2023phenotypicvariabilityof pages 1-4, rahman2019polgrelateddisordersand pages 4-6, lipponen2024mitataxhereditaryataxias pages 39-42) |
| Diagnostics | Genetic testing | Final diagnosis relies on identification of deleterious POLG variants; sequencing of mtDNA-maintenance genes and broader mitochondrial testing is recommended in appropriate phenotypes (wei2023phenotypicvariabilityof pages 1-4, kierdaszuk2020progressiveexternalophthalmoplegia pages 1-2, ali2024mitochondrialchronicprogressive pages 1-3) |
| Diagnostics | Electrophysiology and imaging | NCS/EMG commonly show sensory axonal neuropathy; EEG may show occipital slowing/epileptiform abnormalities in POLG disease; MRI can show cerebellar atrophy or thalamic/occipital/cerebellar lesions, though imaging may be noncontributory early (lipponen2024mitataxhereditaryataxias pages 39-42, wei2023phenotypicvariabilityof pages 1-4, specchio2020polg1relatedepilepsyreview pages 1-3) |
| Diagnostics | Muscle pathology/biochemistry | Muscle biopsy can show COX-deficient ragged-red fibers and multiple mtDNA deletions; however, biopsy may be normal and blood mtDNA can be less sensitive than muscle-derived material (mchugh2010sensoryataxicneuropathy pages 1-2, mchugh2010sensoryataxicneuropathy pages 3-4) |
| Pathophysiology | Molecular chain | POLG dysfunction impairs mtDNA replication/repair, causing mtDNA deletions and/or depletion, respiratory-chain/OXPHOS failure, reduced ATP production, and mitochondrial dysfunction in high-energy tissues (wei2023phenotypicvariabilityof pages 1-4, wong2008molecularandclinical pages 1-2, dombi2024nucleosidesupplementsas pages 1-2) |
| Pathophysiology | Tissue-level consequences | Post-mitotic tissues such as muscle and nervous system accumulate mtDNA defects; biopsy evidence includes COX deficiency and ragged-red fibers, consistent with mitochondrial myopathic/neurodegenerative injury (mchugh2010sensoryataxicneuropathy pages 1-2, wong2008molecularandclinical pages 1-2) |
| Natural history/outcomes | Onset and progression | Onset is variable from childhood to late adulthood; gait ataxia is a common initial symptom, and progression is chronic and degenerative with substantial morbidity (lipponen2024mitataxhereditaryataxias pages 39-42, pekeles2024safetyandefficacy pages 1-2) |
| Natural history/outcomes | Outcome signals | In broader POLG cohorts, epilepsy-associated disease can be severe: status epilepticus occurred in 46.4% of reviewed epilepsy cases and 5-year survival was 30.2%; childhood-onset POLG disease had only 6/40 survivors in one series (specchio2020polg1relatedepilepsyreview pages 1-3, rotig2024distinctclinicalcourses pages 1-2) |
| Treatments/management | Supportive care and contraindications | No definitive disease-modifying standard therapy is established; management is multidisciplinary and symptomatic. Valproic acid/valproate is contraindicated in POLG mutation carriers because it can precipitate liver failure (rahman2019polgrelateddisordersand pages 4-6, ali2024mitochondrialchronicprogressive pages 1-3) |
| Recent research 2023-2024 | Nucleoside therapy trial | Phase 2 open-label POLG trial NCT04802707 tested enteral deoxycytidine/deoxythymidine (dC/dT); in the first 10 participants, mean NMDS improved 27.3→20.7, mean GDF-15 1031→729 pg/mL, EEG improved in 5/8 abnormal baselines, with diarrhea in 2 patients (pekeles2024safetyandefficacy pages 1-2) |
| Recent research 2023-2024 | Preclinical fibroblast findings | In POLG1 fibroblasts, ATGC nucleoside supplementation increased mtDNA content and significantly improved mtDNA recovery after ddC-induced depletion in quiescent cells; lower-dose regimens reduced toxicity concerns (dombi2024nucleosidesupplementsas pages 1-2) |
| Models | Experimental systems | Yeast (Saccharomyces cerevisiae; MIP1 ortholog), patient fibroblasts, and broader POLG disease models are used to study mtDNA maintenance defects and therapeutic screening; yeast-based drug-drop tests are highlighted for mitochondrial disease discovery pipelines (magistrati2023drugdroptest pages 1-2, dombi2024nucleosidesupplementsas pages 1-2) |


*Table: This table condenses the main disease-knowledge-base attributes for SANDO from retrieved evidence, including etiology, phenotype, mechanisms, diagnosis, management, and recent 2023-2024 therapeutic developments. It is useful as a structured reference for curating core facts and citations.*

## 1. Disease information
### 1.1 What is the disease?
SANDO is a **clinical mnemonic** for a progressive neurologic syndrome characterized by **sensory ataxic neuropathy**, **dysarthria**, and **ophthalmoparesis/ophthalmoplegia**, and is now typically classified within the **POLG-related ataxia-neuropathy spectrum (ANS)**. (wong2008molecularandclinical pages 1-2, specchio2020polg1relatedepilepsyreview pages 1-3) In a POLG-associated ataxia case series, SANDO was used as a diagnostic label when sensory ataxia (driven by sensory neuropathy) co-occurred with ophthalmoplegia/ptosis and bulbar involvement (dysarthria/dysphagia). (wei2023phenotypicvariabilityof pages 1-4)

**Direct abstract-quotable definitions/examples** (for evidentiary traceability):
- POLG-associated ataxia report: “Mutations in the mitochondrial DNA polymerase gamma (POLG) are causing a wide spectrum of overlapping disorders…” and patients were “identified as sensory ataxic neuropathy, dysarthria and ophthalmoparesis (SANDO)”. (wei2023phenotypicvariabilityof pages 1-4)
- POLG epilepsy review: “The ataxia neuropathy spectrum (ANS) includes mitochondrial recessive ataxia syndrome (MIRAS) and sensory ataxia neuropathy dysarthria and ophthalmoplegia (SANDO).” (specchio2020polg1relatedepilepsyreview pages 1-3)

### 1.2 Key identifiers
- **OMIM / Orphanet / ICD-10/ICD-11 / MeSH / MONDO:** Not captured in the retrieved evidence excerpts used here; therefore not reported to avoid fabrication. (rahman2019polgrelateddisordersand pages 4-6)

### 1.3 Synonyms and alternative names
- **Ataxia-neuropathy spectrum (ANS):** umbrella term including disorders previously referred to as MIRAS and SANDO. (rahman2019polgrelateddisordersand pages 4-6)
- SANDO is frequently discussed alongside the broader **POLG-related disorder** phenotypic spectrum (including PEO and epilepsy-dominant presentations). (rahman2019polgrelateddisordersand pages 4-6, pekeles2024safetyandefficacy pages 1-2)

### 1.4 Evidence source type
The SANDO-specific clinical characterization in the retrieved set is derived primarily from:
- **Human case reports/series** (e.g., sibling pair with homozygous POLG p.A467T; muscle pathology and course). (mchugh2010sensoryataxicneuropathy pages 1-2)
- **Aggregated disease-level reviews and cohorts** of POLG-related disorders, which provide the most robust statistics and management guidance (e.g., valproate contraindication; outcome statistics in POLG epilepsy). (rahman2019polgrelateddisordersand pages 4-6, specchio2020polg1relatedepilepsyreview pages 1-3)

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** pathogenic variants in **POLG**, encoding the catalytic subunit of mitochondrial DNA polymerase gamma, essential for mtDNA replication and repair. (pekeles2024safetyandefficacy pages 1-2, specchio2020polg1relatedepilepsyreview pages 1-3)

**Mechanistic causal chain (high-level):** POLG dysfunction → impaired mtDNA replication/repair → mtDNA deletions and/or depletion → oxidative phosphorylation (OXPHOS) failure / reduced ATP production → progressive dysfunction and degeneration in high-energy tissues (nervous system, muscle). (wei2023phenotypicvariabilityof pages 1-4, wong2008molecularandclinical pages 1-2)

### 2.2 Risk factors
- **Genetic risk:** carrying pathogenic POLG variants; in many SANDO/ANS cases this is **biallelic** (autosomal recessive). (mchugh2010sensoryataxicneuropathy pages 1-2, rotig2024distinctclinicalcourses pages 1-2)
- **Iatrogenic trigger:** exposure to **valproic acid (VPA)** in individuals with POLG mutations can precipitate severe hepatic failure; it is explicitly contraindicated. (rahman2019polgrelateddisordersand pages 4-6)

### 2.3 Protective factors
No genetic or environmental protective factors specific to SANDO were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Strongest documented interaction in the retrieved evidence is **drug-triggered toxicity**: VPA exposure interacting with POLG genotype to precipitate liver failure. (rahman2019polgrelateddisordersand pages 4-6)

## 3. Phenotypes
### 3.1 Core phenotypes (with suggested HPO terms)
Below, phenotype type is indicated, followed by suggested **HPO** terms.

1) **Sensory ataxia due to sensory neuropathy** (symptom/sign)  
- Key features: prominent proprioceptive loss and sensory neuropathy driving the ataxia. (wei2023phenotypicvariabilityof pages 1-4)  
- Electrophysiology: absent sensory nerve action potentials (SNAPs) described in a SANDO sibling-pair case. (mchugh2010sensoryataxicneuropathy pages 1-2)  
- Suggested HPO: **HP:0001251 Ataxia**, **HP:0000762 Sensory ataxia**, **HP:0001278 Orthostatic hypotension** (only if autonomic involvement), **HP:0002936 Areflexia**, **HP:0003401 Axonal neuropathy**, **HP:0002497 Abnormal proprioception**.

2) **Dysarthria** (symptom/sign)  
- Reported as part of the defining triad and common associated feature in POLG ataxia syndromes. (specchio2020polg1relatedepilepsyreview pages 1-3, wei2023phenotypicvariabilityof pages 1-4)  
- Suggested HPO: **HP:0001260 Dysarthria**.

3) **Ophthalmoparesis / ophthalmoplegia / ptosis** (clinical sign)  
- CPEO-related definition: “bilateral symmetrical progressive ptosis and reduced ocular motility” (as a broader mitochondrial ophthalmoplegia construct relevant to SANDO). (ali2024mitochondrialchronicprogressive pages 1-3)  
- Suggested HPO: **HP:0000602 Ophthalmoplegia**, **HP:0000657 Oculomotor apraxia** (only if present), **HP:0000508 Ptosis**.

### 3.2 Additional/common associated phenotypes (HPO suggestions)
- **Dysphagia** (wei2023phenotypicvariabilityof pages 1-4): **HP:0002015 Dysphagia**.
- **Seizures / epilepsy** (wei2023phenotypicvariabilityof pages 1-4, pekeles2024safetyandefficacy pages 1-2): **HP:0001250 Seizures**, **HP:0002133 Status epilepticus**.
- **Myopathy / exercise intolerance** (wei2023phenotypicvariabilityof pages 1-4): **HP:0003198 Myopathy**, **HP:0003546 Exercise intolerance**.
- **Neuropathic pain** noted as relatively frequent in POLG-related neuropathy cohorts (not necessarily SANDO-specific). (rahman2019polgrelateddisordersand pages 4-6): **HP:0012531 Neuropathic pain**.

### 3.3 Age of onset, severity, progression, frequency
- **Age of onset:** variable; SANDO can be adult-onset (e.g., fifth decade onset in a sibling pair). (mchugh2010sensoryataxicneuropathy pages 1-2) POLG-related disease overall ranges from childhood to late adulthood. (rahman2019polgrelateddisordersand pages 4-6)
- **Progression:** generally progressive; in the p.A467T sibling pair, severe disability developed over ~12 years. (mchugh2010sensoryataxicneuropathy pages 1-2)
- **Frequency among affected individuals:** Specific frequency of individual SANDO features was not available in the retrieved sources; however, in a POLG cohort **6 of 11 (55%) SANDO patients** had POLG mutations leading to multiple mtDNA deletions. (rahman2019polgrelateddisordersand pages 4-6)

### 3.4 Quality-of-life impact
Direct QoL instrument data (EQ-5D/SF-36/PROMIS) were not found in the retrieved evidence; functional decline to severe disability over years is documented in at least one SANDO family report. (mchugh2010sensoryataxicneuropathy pages 1-2)

## 4. Genetic / molecular information
### 4.1 Causal genes
- **POLG** (primary): encodes mitochondrial DNA polymerase gamma. (pekeles2024safetyandefficacy pages 1-2)

### 4.2 Pathogenic variants and variant classes
- **Recurrent variants across POLG disease:** A467T, W748S, G848S were prevalent in a POLG-epilepsy review (74.2% of patients carried one of these across aggregated cases). (specchio2020polg1relatedepilepsyreview pages 1-3)
- **SANDO-specific example (primary human case report):** homozygous **POLG p.A467T (c.1399G>A)** in two siblings with classic SANDO triad. (mchugh2010sensoryataxicneuropathy pages 1-2)

**Population frequency example (variant-specific):** In a SANDO sibling-pair paper, p.A467T allele frequency in controls was reported as 0.6% (Belgian) and 0.7% (British). (mchugh2010sensoryataxicneuropathy pages 3-4)

**Functional consequence example:** p.A467T “results in a 96% reduction in the catalytic activity of the polymerase gamma protein.” (mchugh2010sensoryataxicneuropathy pages 3-4)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No SANDO-specific modifier gene or epigenetic signatures were identified in the retrieved evidence.

## 5. Environmental information
The most salient non-genetic factor in the retrieved evidence is **drug exposure**:
- **Valproic acid** can precipitate liver failure in POLG-related disease and is contraindicated. (rahman2019polgrelateddisordersand pages 4-6)
Other environmental/lifestyle risk factors were not identified as SANDO-specific.

## 6. Mechanism / pathophysiology
### 6.1 Molecular pathways and cellular processes
- **mtDNA replication/repair failure:** POLG is essential for mtDNA replication and repair; pathogenic variants cause mtDNA maintenance defects. (pekeles2024safetyandefficacy pages 1-2)
- **mtDNA deletions/depletion → OXPHOS failure:** POLG mutations can lead to mtDNA depletion and deletions with downstream defective oxidative phosphorylation and reduced ATP. (wei2023phenotypicvariabilityof pages 1-4)
- **Muscle mitochondrial pathology evidence:** COX-deficient ragged-red fibers and multiple mtDNA deletions documented in SANDO siblings. (mchugh2010sensoryataxicneuropathy pages 1-2)

**Suggested GO biological process terms:** 
- **GO:0006260 DNA replication** (mitochondrial context), **GO:0007005 mitochondrion organization**, **GO:0006119 oxidative phosphorylation**, **GO:0032543 mitochondrial translation** (downstream consequences).

### 6.2 Cell types and tissue vulnerability
Evidence indicates vulnerability of high-energy tissues (nervous system, muscle) in mtDNA maintenance disorders; extraocular muscles are particularly affected in CPEO/ophthalmoplegia due to high mitochondrial demand. (ali2024mitochondrialchronicprogressive pages 1-3)

**Suggested Cell Ontology (CL) terms:** 
- **CL:0000540 neuron**, **CL:0000100 motor neuron** (as clinically relevant), **CL:0000187 skeletal muscle cell**.

### 6.3 Anatomical chain from trigger to manifestations (causal chain)
POLG pathogenic variant (germline) → reduced/aberrant pol γ activity → mtDNA deletions/depletion (especially in post-mitotic tissues) → respiratory chain dysfunction (COX deficiency) → impaired ATP generation → degeneration/dysfunction in peripheral sensory neurons (sensory neuropathy/ataxia), bulbar/brainstem circuits (dysarthria/dysphagia), and extraocular muscles (ophthalmoparesis). (wong2008molecularandclinical pages 1-2, mchugh2010sensoryataxicneuropathy pages 1-2, ali2024mitochondrialchronicprogressive pages 1-3)

## 7. Anatomical structures affected
### 7.1 Organ/system level
- **Nervous system:** peripheral neuropathy and central manifestations (seizures in some POLG cases). (rahman2019polgrelateddisordersand pages 4-6, pekeles2024safetyandefficacy pages 1-2)
- **Skeletal muscle / extraocular muscle system:** ophthalmoplegia/ptosis and myopathy features. (ali2024mitochondrialchronicprogressive pages 1-3, rahman2019polgrelateddisordersand pages 4-6)
- **Liver (in POLG spectrum):** vulnerability especially with VPA exposure; hepatic failure prominent in severe POLG phenotypes (Alpers and others). (rahman2019polgrelateddisordersand pages 4-6, pekeles2024safetyandefficacy pages 1-2)

**Suggested UBERON terms:** 
- Peripheral nerve (UBERON:0001021), cerebellum (UBERON:0002037; if cerebellar component), extraocular muscle (UBERON:0001631), skeletal muscle tissue (UBERON:0001134), liver (UBERON:0002107).

### 7.2 Subcellular localization
- **Mitochondrion (matrix/nucleoid context):** mtDNA maintenance and OXPHOS systems. (pekeles2024safetyandefficacy pages 1-2, zeviani2022mitochondrialneurodegeneration pages 1-2)

**Suggested GO cellular component terms:** 
- **GO:0005739 mitochondrion**, **GO:0005759 mitochondrial matrix**, **GO:0005764 lysosome** (only if evidence; not found here), **GO:0005743 mitochondrial inner membrane**.

## 8. Temporal development
- **Onset:** from childhood to adult/late-life; case evidence includes fifth-decade onset. (mchugh2010sensoryataxicneuropathy pages 1-2, rahman2019polgrelateddisordersand pages 4-6)
- **Course:** chronic progressive, degenerative. (pekeles2024safetyandefficacy pages 1-2)

## 9. Inheritance and population
### 9.1 Inheritance
- Many POLG-related SANDO/ANS presentations are associated with **biallelic pathogenic variants** (autosomal recessive). (mchugh2010sensoryataxicneuropathy pages 1-2, rotig2024distinctclinicalcourses pages 1-2)

### 9.2 Epidemiology
- SANDO-specific prevalence/incidence was not found in the retrieved sources.

## 10. Diagnostics
### 10.1 Clinical tests and biomarkers
- **Electrophysiology:** sensory neuropathy patterns (e.g., absent SNAPs). (mchugh2010sensoryataxicneuropathy pages 1-2)
- **Muscle biopsy:** COX-deficient ragged-red fibers; detection of multiple mtDNA deletions (long-range PCR). (mchugh2010sensoryataxicneuropathy pages 1-2)
- **Blood biomarkers:** GDF-15 used as a “biomarker of mitochondrial dysfunction” in the 2024 POLG dC/dT trial. (pekeles2024safetyandefficacy pages 1-2)

### 10.2 Genetic testing
- **Gold standard:** molecular confirmation of deleterious POLG variants; WES was used in a POLG-associated ataxia report and “The final diagnosis relies on the molecular finding of deleterious mutations in POLG.” (wei2023phenotypicvariabilityof pages 1-4)
- **Testing caveat:** lymphocyte-derived mtDNA can be less sensitive than muscle-derived tissue for detecting mtDNA deletions in POLG disease. (mchugh2010sensoryataxicneuropathy pages 3-4)

### 10.3 Differential diagnosis
Not exhaustively enumerated in retrieved evidence; the main differential frame is within **autosomal recessive ataxias with ocular involvement** and mitochondrial CPEO+ phenotypes, where POLG is a key gene to test. (ali2024mitochondrialchronicprogressive pages 1-3, lopergolo2024autosomalrecessivecerebellar pages 6-7)

## 11. Outcome / prognosis
SANDO-specific survival estimates were not retrieved; prognosis is typically progressive disability.

For broader POLG-related disease (important contextual statistics):
- POLG-related epilepsy review (195 patients): **status epilepticus in 46.4%**; **5-year survival 30.2%**. (specchio2020polg1relatedepilepsyreview pages 1-3)
- Pediatric biallelic POLG cohort (n=40): **24/40 required urgent neurointensive care for seizures/status epilepticus**, and **6/40 survived** (study-specific cohort). (rotig2024distinctclinicalcourses pages 1-2)

## 12. Treatment
### 12.1 Standard-of-care management (symptomatic/supportive)
No definitive established disease-modifying therapy exists for POLG-related disease; management is typically symptomatic and multidisciplinary. (pekeles2024safetyandefficacy pages 1-2, ali2024mitochondrialchronicprogressive pages 1-3)

**Critical safety guidance:**
- Review-level expert statement: “valproic acid (VPA) is contra-indicated in all patients with POLG mutations,” and can precipitate liver failure. (rahman2019polgrelateddisordersand pages 4-6)

**Suggested MAXO terms:** 
- **MAXO:0000058 genetic testing**, **MAXO:0000474 physical therapy**, **MAXO:0000934 speech therapy**, **MAXO:0000747 seizure management**, **MAXO:0001072 avoidance of harmful medication** (for VPA avoidance).

### 12.2 Recent developments (prioritizing 2023–2024)
#### (A) Phase 2 open-label dC/dT trial in POLG disorders (2024)
**Study:** Pekeles et al., *eClinicalMedicine* (Aug 2024), “Safety and efficacy of deoxycytidine/deoxythymidine combination therapy in POLG-related disorders: 6-month interim results…”  
**URL:** https://doi.org/10.1016/j.eclinm.2024.102740  
**ClinicalTrials.gov:** **NCT04802707** (trial registration cited in paper). (pekeles2024safetyandefficacy pages 1-2)

Key quantitative interim results in first 10 participants:
- Mean **NMDS improved from 27.3 to 20.7** at 6 months. (pekeles2024safetyandefficacy pages 1-2)
- Mean **GDF-15 decreased from 1031 pg/mL to 729 pg/mL**. (pekeles2024safetyandefficacy pages 1-2)
- **EEG improved in 5/8** with abnormal baseline EEG. (pekeles2024safetyandefficacy pages 1-2)
- Notable adverse event: diarrhea in 2 patients, self-resolving. (pekeles2024safetyandefficacy pages 1-2)

#### (B) POLG/TWNK fibroblast nucleoside supplementation study (2024)
**Study:** Dombi et al., *Frontiers in Cell and Developmental Biology* (Published 02 Apr 2024)  
**URL:** https://doi.org/10.3389/fcell.2024.1260496  
Key findings: In POLG1 cells, certain nucleoside combinations (notably ATGC) increased mtDNA content and significantly improved mtDNA recovery after ddC-induced depletion, with dose-dependent toxicity mitigated at lower concentrations. (dombi2024nucleosidesupplementsas pages 1-2)

## 13. Prevention
SANDO is genetic; therefore prevention is mainly via genetic counseling and avoidance of triggers.
- **Primary prevention (iatrogenic):** avoid valproate in POLG mutation carriers. (rahman2019polgrelateddisordersand pages 4-6)
- **Reproductive prevention:** not specifically described in retrieved evidence.

## 14. Other species / natural disease
No naturally occurring veterinary SANDO-like disease evidence was found in the retrieved sources.

## 15. Model organisms
- **Yeast (Saccharomyces cerevisiae):** highlighted as an efficient model organism for mitochondrial disease variant validation and drug screening (“drug drop test”). (magistrati2023drugdroptest pages 1-2)
- **Patient-derived fibroblasts:** used to assay mtDNA copy number and mitochondrial membrane potential and to test nucleoside combinations in POLG/TWNK deficiency. (dombi2024nucleosidesupplementsas pages 1-2)

## Evidence gaps and limitations (important for knowledge-base curation)
1) **Formal disease identifiers (MONDO, Orphanet, ICD-10/11, MeSH, and explicit OMIM for SANDO)** were not present in the retrieved full-text excerpts available to the toolchain for this run; they are therefore intentionally omitted to avoid hallucination. (rahman2019polgrelateddisordersand pages 4-6)
2) Many quantitative statistics come from **broader POLG cohorts** (especially epilepsy-focused), not SANDO-only cohorts, reflecting the rarity of SANDO and limited cohort-size literature. (specchio2020polg1relatedepilepsyreview pages 1-3, rotig2024distinctclinicalcourses pages 1-2)

## Key references (with publication dates and URLs)
- Rahman S, Copeland WC. *POLG-related disorders and their neurological manifestations.* **Nat Rev Neurol.** (manuscript available in PMC 2022; published 2019). https://doi.org/10.1038/s41582-018-0101-0 (rahman2019polgrelateddisordersand pages 4-6)
- Pekeles H, et al. *Safety and efficacy of deoxycytidine/deoxythymidine combination therapy in POLG-related disorders…* **eClinicalMedicine. Aug 2024.** https://doi.org/10.1016/j.eclinm.2024.102740 (pekeles2024safetyandefficacy pages 1-2)
- Dombi E, et al. *Nucleoside supplements as treatments for mitochondrial DNA depletion syndrome.* **Front Cell Dev Biol. 02 Apr 2024.** https://doi.org/10.3389/fcell.2024.1260496 (dombi2024nucleosidesupplementsas pages 1-2)
- McHugh JC, et al. *SANDO in a sibling pair with a homozygous p.A467T POLG mutation.* **Muscle Nerve. Feb 2010.** https://doi.org/10.1002/mus.21494 (mchugh2010sensoryataxicneuropathy pages 1-2)
- Specchio N, et al. *POLG1-Related Epilepsy: Review of Diagnostic and Therapeutic Findings.* **Brain Sciences. Oct 2020.** https://doi.org/10.3390/brainsci10110768 (specchio2020polg1relatedepilepsyreview pages 1-3)
- Wong LJC, et al. *Molecular and clinical genetics of mitochondrial diseases due to POLG mutations.* **Human Mutation. Sep 2008.** https://doi.org/10.1002/humu.20824 (wong2008molecularandclinical pages 1-2)
- Ali A, et al. *Mitochondrial Chronic Progressive External Ophthalmoplegia.* **Brain Sciences. Jan 2024.** https://doi.org/10.3390/brainsci14020135 (ali2024mitochondrialchronicprogressive pages 1-3)

References

1. (specchio2020polg1relatedepilepsyreview pages 1-3): Nicola Specchio, Nicola Pietrafusa, Costanza Calabrese, Marina Trivisano, Chiara Pepi, Luca de Palma, Alessandro Ferretti, Paolo Curatolo, and Federico Vigevano. Polg1-related epilepsy: review of diagnostic and therapeutic findings. Brain Sciences, 10:768, Oct 2020. URL: https://doi.org/10.3390/brainsci10110768, doi:10.3390/brainsci10110768. This article has 15 citations.

2. (rahman2019polgrelateddisordersand pages 4-6): Shamima Rahman and William C. Copeland. Polg-related disorders and their neurological manifestations. Nov 2019. URL: https://doi.org/10.1038/s41582-018-0101-0, doi:10.1038/s41582-018-0101-0. This article has 491 citations and is from a highest quality peer-reviewed journal.

3. (wong2008molecularandclinical pages 1-2): Lee-Jun C. Wong, Robert K. Naviaux, Nicola Brunetti-Pierri, Qing Zhang, Eric S. Schmitt, Cavatina Truong, Margherita Milone, Bruce H. Cohen, Beverly Wical, Jaya Ganesh, Alice A. Basinger, Barbara K. Burton, Kathryn Swoboda, Donald L. Gilbert, Adeline Vanderver, Russell P. Saneto, Bruno Maranda, Georgianne Arnold, Jose E. Abdenur, Paula J. Waters, and William C. Copeland. Molecular and clinical genetics of mitochondrial diseases due to polg mutations. Human Mutation, 29:E150-E172, Sep 2008. URL: https://doi.org/10.1002/humu.20824, doi:10.1002/humu.20824. This article has 366 citations and is from a domain leading peer-reviewed journal.

4. (mchugh2010sensoryataxicneuropathy pages 1-2): John C. McHugh, Roisin Lonergan, Rachel Howley, Killian O'Rourke, Robert W. Taylor, Michael Farrell, Michael Hutchinson, and Sean Connolly. Sensory ataxic neuropathy dysarthria and ophthalmoparesis (sando) in a sibling pair with a homozygous p.a467t polg mutation. Muscle & Nerve, 41:265-269, Feb 2010. URL: https://doi.org/10.1002/mus.21494, doi:10.1002/mus.21494. This article has 25 citations and is from a peer-reviewed journal.

5. (pekeles2024safetyandefficacy pages 1-2): Heather Pekeles, Saoussen Berrahmoune, Christelle Dassi, Anthony C.T. Cheung, Tommy Gagnon, Paula J. Waters, Ralf Eberhard, Daniela Buhas, and Kenneth A. Myers. Safety and efficacy of deoxycytidine/deoxythymidine combination therapy in polg-related disorders: 6-month interim results of an open-label, single arm, phase 2 trial. Aug 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102740, doi:10.1016/j.eclinm.2024.102740. This article has 15 citations and is from a peer-reviewed journal.

6. (rotig2024distinctclinicalcourses pages 1-2): Agnès Rötig, Pauline Gaignard, Giulia Barcia, Zahra Assouline, Claire-Marine Berat, Magalie Barth, Léna Damaj, Nolwenn Laborde, Marie-Thérèse Abi-Warde, Brigitte Chabrol, Pascale De Lonlay, Isabelle Desguerre, Alice Goldenberg, Emmanuel Gonzales, Emmanuel Jacquemin, Patrizia Amati -Bonneau, Dominique Bonneau, Véronique Abadie, Chrystèle Bonnemains, Pierre Broue, Anne De Saint-Martin, Philippe Durand, Alain Fouilhoux, Bertrand Isidor, Marianne Jaroussie, Guillaume Jedraszak, Hélène Maurey, Karine Mention, Sylvie S. Odent, Laurent Pasquier, Christelle Rougeot-Jung, Cyril Gitiaux, Charles-Joris Roux, Nathalie Boddaert, Arnold Munnich, and Manuel Schiff. Distinct clinical courses and shortened lifespans in childhood-onset dna polymerase gamma deficiency. Aug 2024. URL: https://doi.org/10.1212/nxg.0000000000200167, doi:10.1212/nxg.0000000000200167. This article has 10 citations.

7. (mchugh2010sensoryataxicneuropathy pages 3-4): John C. McHugh, Roisin Lonergan, Rachel Howley, Killian O'Rourke, Robert W. Taylor, Michael Farrell, Michael Hutchinson, and Sean Connolly. Sensory ataxic neuropathy dysarthria and ophthalmoparesis (sando) in a sibling pair with a homozygous p.a467t polg mutation. Muscle & Nerve, 41:265-269, Feb 2010. URL: https://doi.org/10.1002/mus.21494, doi:10.1002/mus.21494. This article has 25 citations and is from a peer-reviewed journal.

8. (wei2023phenotypicvariabilityof pages 1-4): Yanping Wei, Yuzhou Guan, and Min Qian. Phenotypic variability of polymerase gamma–associated ataxia. Unknown journal, Sep 2023. URL: https://doi.org/10.21203/rs.3.rs-3340280/v1, doi:10.21203/rs.3.rs-3340280/v1.

9. (lipponen2024mitataxhereditaryataxias pages 39-42): J Lipponen. Mitatax: hereditary ataxias in northern finland. Unknown journal, 2024.

10. (ali2024mitochondrialchronicprogressive pages 1-3): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 24 citations.

11. (kierdaszuk2020progressiveexternalophthalmoplegia pages 1-2): Biruta Kierdaszuk, Magdalena Kaliszewska, Joanna Rusecka, Joanna Kosińska, Ewa Bartnik, Katarzyna Tońska, Anna M. Kamińska, and Anna Kostera-Pruszczyk. Progressive external ophthalmoplegia in polish patients—from clinical evaluation to genetic confirmation. Genes, 12:54, Dec 2020. URL: https://doi.org/10.3390/genes12010054, doi:10.3390/genes12010054. This article has 6 citations.

12. (dombi2024nucleosidesupplementsas pages 1-2): Eszter Dombi, Tony Marinaki, Paolo Spingardi, Val Millar, Nastasia Hadjichristou, Janet Carver, Iain G. Johnston, Carl Fratter, and Joanna Poulton. Nucleoside supplements as treatments for mitochondrial dna depletion syndrome. Frontiers in Cell and Developmental Biology, Apr 2024. URL: https://doi.org/10.3389/fcell.2024.1260496, doi:10.3389/fcell.2024.1260496. This article has 13 citations.

13. (magistrati2023drugdroptest pages 1-2): Martina Magistrati, Alexandru Ionut Gilea, Maria Carla Gerra, Enrico Baruffini, and Cristina Dallabona. Drug drop test: how to quickly identify potential therapeutic compounds for mitochondrial diseases using yeast saccharomyces cerevisiae. International Journal of Molecular Sciences, 24:10696, Jun 2023. URL: https://doi.org/10.3390/ijms241310696, doi:10.3390/ijms241310696. This article has 8 citations.

14. (zeviani2022mitochondrialneurodegeneration pages 1-2): Massimo Zeviani and Carlo Viscomi. Mitochondrial neurodegeneration. Cells, 11:637, Feb 2022. URL: https://doi.org/10.3390/cells11040637, doi:10.3390/cells11040637. This article has 53 citations.

15. (lopergolo2024autosomalrecessivecerebellar pages 6-7): Diego Lopergolo, Francesca Rosini, Elena Pretegiani, Alessia Bargagli, Valeria Serchi, and Alessandra Rufa. Autosomal recessive cerebellar ataxias: a diagnostic classification approach according to ocular features. Frontiers in Integrative Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fnint.2023.1275794, doi:10.3389/fnint.2023.1275794. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis-deep-research-falcon_artifacts/artifact-00.md)