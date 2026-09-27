---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T11:53:46.762451'
end_time: '2026-08-01T12:03:28.639894'
duration_seconds: 581.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Sensory Ataxia 1
  mondo_id: MONDO:0012166
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Sensory_Ataxia_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Sensory Ataxia 1
- **MONDO ID:** MONDO:0012166 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Sensory Ataxia 1** covering all of the
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
- **Disease Name:** Autosomal Dominant Sensory Ataxia 1
- **MONDO ID:** MONDO:0012166 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Sensory Ataxia 1** covering all of the
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


# Autosomal Dominant Sensory Ataxia 1: Comprehensive Disease Report

## Executive summary

Autosomal dominant sensory ataxia 1 (ADSA1; also **SNAX1**) is an exceptionally rare, adult-onset, slowly progressive neurodegenerative disorder caused by a heterozygous **RNF170 c.595C>T (p.Arg199Cys)** variant. Its defining abnormality is degeneration or dysfunction of proprioceptive sensory pathways—especially dorsal-root-ganglion neurons and/or their central projections in the posterior spinal columns—producing impaired vibration and joint-position sense, sensory gait ataxia, and a positive Romberg sign. Pyramidal signs, peripheral sensory-neuronopathy, and bilateral vestibular areflexia are variable extensions of the phenotype. The disorder is not primarily a cerebellar ataxia. Published dominant cases remain limited to a few Canadian, Ecuadorian, and Belgian/European families, precluding reliable estimates of prevalence, penetrance, survival, or phenotype frequencies. (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 2-4, wagner2019biallelicvariantsin pages 8-10, daele2022rnf170mutationcauses pages 1-2)

A crucial curation distinction is that **biallelic loss-of-function RNF170 variants cause a separate, infancy-onset autosomal-recessive hereditary spastic paraplegia (HSP)**. Findings from that allelic disorder illuminate RNF170 biology but should not be assigned directly to ADSA1. (wagner2019biallelicvariantsin pages 8-10, wagner2019biallelicvariantsin pages 1-2, wagner2019biallelicvariantsin pages 3-4)

| Domain | Curated finding | Evidence type | Key source |
|---|---|---|---|
| Identity / variant | Autosomal dominant sensory ataxia 1 maps to MONDO:0012166 and is associated with RNF170; dominant disease is consistently linked to the heterozygous RNF170 c.595C>T (p.Arg199Cys) variant. Distinct disorder: biallelic RNF170 variants cause autosomal recessive hereditary spastic paraplegia (HSP), not ADSA1. | Aggregated disease-target mapping + human genetics | Open Targets disease-target association; human reports and review synthesis (OpenTargets Search: Autosomal dominant sensory ataxia 1, daele2022rnf170mutationcauses pages 2-4, wagner2019biallelicvariantsin pages 8-10) |
| Phenotype / onset | Core dominant phenotype is late-onset, slowly progressive sensory ataxia with sensory loss and gait imbalance; reported onset spans ages 35, 47, 55, 64, and 68 in described families, with broader literature range in the 4th-8th decades. Variable pyramidal involvement occurs; vestibular areflexia can occur and mimic CANVAS in some patients. | Human family/case reports | Belgian family, Ecuadorian family, review of prior Canadian families (cortese2020mutationinrnf170 pages 1-2, wagner2019biallelicvariantsin pages 8-10, daele2022rnf170mutationcauses pages 1-2) |
| Neurophysiology / MRI | Dominant RNF170 disease shows posterior-column / preganglionic sensory pathway dysfunction: impaired or absent SSEPs are common; SNAPs may be preserved in classic cases but reduced/absent in some families, indicating phenotypic variability with possible sensory ganglionopathy. Brain MRI may be normal without cerebellar atrophy; cervical spine MRI can show posterior-column T2 hyperintensity/volume loss; spine MRI may also be normal in some affected relatives. | Human clinical neurophysiology/imaging | Ecuadorian CANVAS-mimic family; Belgian family; comparative discussion (cortese2020mutationinrnf170 pages 1-1, daele2022rnf170mutationcauses pages 1-2, cortese2020mutationinrnf170 pages 2-2) |
| Mechanism | RNF170 is an ER-membrane E3 ubiquitin ligase that, with ERLIN1/ERLIN2, mediates ubiquitination-dependent degradation of activated IP3 receptors (ITPRs) via ERAD/proteasomal turnover, thereby regulating ER Ca2+ signaling. For dominant p.Arg199Cys ADSA1, available evidence supports protein destabilization with increased auto-ubiquitination and a likely toxic gain-of-function mechanism; precise sensory-neuron selectivity remains unresolved. | Cell/mechanistic studies + pathway inference + human genetics | RNF170/ITPR pathway and dominant-vs-recessive contrast (wagner2019biallelicvariantsin pages 8-10, wagner2019biallelicvariantsin pages 10-11, wagner2019biallelicvariantsin pages 1-2, wagner2019biallelicvariantsin pages 11-12) |
| Inheritance / epidemiology | Inheritance is autosomal dominant for ADSA1. Known dominant evidence remains sparse: historically two Eastern Canadian families, later one Ecuadorian family, and one Belgian/European family. Founder haplotype was reported in Canadian families; common ancestry across all families is unclear. Reduced penetrance or de novo occurrence has been considered in one pedigree. No robust prevalence, incidence, sex ratio, or population allele-frequency estimates were identified. | Human pedigree studies; evidence gap for population metrics | Founder and family-count discussion (daele2022rnf170mutationcauses pages 2-4, cortese2020mutationinrnf170 pages 1-2) |
| Diagnosis | Diagnostic clues: dominant family history, progressive sensory ataxia, posterior-column signs, impaired proprioception/vibration, reduced or absent reflexes, abnormal SSEPs, and/or sensory neuronopathy with normal motor conduction. RNF170 testing should be considered in RFC1-negative CANVAS-like cases and included in ataxia gene panels, especially after excluding repeat expansions and common acquired causes. | Human case reports + expert diagnostic recommendation | CANVAS-mimic report and Belgian panel recommendation (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 1-2, daele2022rnf170mutationcauses pages 2-4, cortese2020mutationinrnf170 pages 1-1) |
| Differential diagnosis | Important differentials include RFC1-related CANVAS, Friedreich ataxia, POLG-related mitochondrial disease, vitamin E deficiency, abetalipoproteinemia, spinocerebellar ataxias with neuropathy, Charcot-Marie-Tooth disease 4C, paraneoplastic sensory neuronopathy, autoimmune causes such as Sjögren syndrome, and toxic neuropathies (eg, cisplatin, pyridoxine). | Human report / review-level clinical differential | Differential lists from case/family reports (daele2022rnf170mutationcauses pages 2-4, cortese2020mutationinrnf170 pages 1-1) |
| Prognosis / disability | Disease course is chronic and progressive. Functional disability can become substantial; in the Ecuadorian index case, gait deterioration progressed over a decade and required a walking aid by age 57. No survival, mortality, or formal quality-of-life datasets specific to ADSA1 were found. | Human case report + evidence gap | Progressive disability in case report; no cohort outcomes (cortese2020mutationinrnf170 pages 1-2) |
| Therapy / trials | No disease-modifying therapy, genotype-guided treatment, or disease-specific biomarker has been established for ADSA1. No relevant registered interventional clinical trials were identified in the tool search. Current care is supportive/extrapolated: rehabilitation, balance and fall-prevention strategies, mobility aids, symptomatic management, and genetic counseling/cascade testing. | Evidence gap + standard rare-neurology supportive practice extrapolation | Negative trial search and absence in case literature (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 1-2) |
| Models | Mouse: Rnf170-null mice develop age-dependent gait abnormalities, supporting a role in motor/sensory pathway integrity, but this is a loss-of-function model and does not fully replicate dominant p.Arg199Cys disease. Zebrafish: dominant p.Arg199Cys shows dose-dependent toxicity; separate knockdown/overexpression studies support RNF170 developmental and neuronal functions. Dog: a 2024 naturally occurring recessive RNF170 frameshift model in Miniature American Shepherds causes neuroaxonal dystrophy; 23/27 homozygotes (85%) were clinically affected, providing a large-animal model of the broader RNF170 phenotypic spectrum, not a direct ADSA1 model. | Mouse, zebrafish, canine models | Mouse/zebrafish/canine model evidence and limitations (cook2024rnf170frameshiftdeletion pages 10-12, wagner2019biallelicvariantsin pages 10-11, wagner2019biallelicvariantsin pages 8-10) |
| Evidence gaps | No convincing evidence was found for environmental or infectious causes, protective factors, gene-environment interactions, formal diagnostic criteria, disease-specific omics biomarkers, epigenetic signatures, prevention trials, or established targeted therapies for ADSA1. | Explicit absence of evidence | Across retrieved ADSA1 literature and searches (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 1-2, daele2022rnf170mutationcauses pages 2-4) |


*Table: This table summarizes the main curated findings for Autosomal Dominant Sensory Ataxia 1, emphasizing that the dominant disorder is specifically linked to heterozygous RNF170 p.Arg199Cys and is distinct from biallelic RNF170 hereditary spastic paraplegia. It also highlights the strongest available clinical and mechanistic evidence while clearly labeling major evidence gaps.*

## 1. Disease information

### Definition and classification

ADSA1 is a Mendelian, autosomal-dominant sensory ataxia characterized by late-onset progressive impairment of large-fiber proprioceptive pathways. The usual clinical syndrome comprises imbalance worsened by loss of visual input, sensory loss, gait ataxia, and posterior-column neurophysiological abnormalities. Sensory nerve action potentials (SNAPs) may remain preserved in the classic predominantly central/preganglionic phenotype, but some families exhibit sensory ganglionopathy with reduced or absent SNAPs. (wagner2019biallelicvariantsin pages 8-10, daele2022rnf170mutationcauses pages 4-5, cortese2020mutationinrnf170 pages 1-1)

### Identifiers and synonyms

- **MONDO:** MONDO:0012166, autosomal dominant sensory ataxia 1.
- **OMIM phenotype:** MIM **608984**, reported in the literature as autosomal dominant sensory ataxia/ADSA.
- **Causal gene:** **RNF170**, ring finger protein 170; Ensembl ENSG00000120925.
- **Common names:** autosomal dominant sensory ataxia; autosomal dominant sensory ataxia 1; ADSA; ADSA1; sensory ataxia 1; **SNAX1**; RNF170-related dominant sensory ataxia.
- **Orphanet, MeSH, ICD-10, and ICD-11:** no disease-specific codes were established from the retrieved evidence. In clinical coding, the condition will generally require broader hereditary ataxia or hereditary neuropathy categories; these are not exact semantic equivalents.

Open Targets maps MONDO:0012166 specifically to RNF170 and reports five association-evidence records, including literature linked to PMID **21115467**. (OpenTargets Search: Autosomal dominant sensory ataxia 1)

### Evidence provenance

The phenotype is derived primarily from individually examined members of a very small number of pedigrees, not from EHR-scale cohorts, population registries, or surveillance systems. MONDO/Open Targets and similar resources aggregate these family-level reports. Consequently, apparently precise clinical frequencies should not be generalized to the wider population.

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is a **germline heterozygous RNF170 c.595C>T (p.Arg199Cys)** missense variant in a transmembrane region of RNF170. The same amino-acid substitution has been reported across geographically separated dominant families and remains the only heterozygous RNF170 variant convincingly linked to this specific phenotype in the retrieved literature. (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 2-4, daele2022rnf170mutationcauses pages 4-5)

### Genetic risk

An affected heterozygote has, in principle, a **50% probability of transmitting** the variant in each pregnancy. Family history is therefore the principal recognized risk factor. Two Eastern Canadian families shared a disease haplotype, supporting a founder event. Common ancestry with the Ecuadorian and Belgian families has not been demonstrated. Reduced penetrance or a de novo event was considered in the Belgian pedigree because the paternal grandparents reportedly remained asymptomatic beyond age 70. (daele2022rnf170mutationcauses pages 2-4)

Reliable age-specific penetrance, carrier frequency, population allele frequency, sex effect, germline-mosaicism rate, modifier genes, and genetic anticipation have not been established. There is no evidence of a repeat-expansion mechanism, so anticipation is not expected mechanistically, but this has not been tested in a sufficiently large cohort.

### Environmental, lifestyle, infectious, and protective factors

No environmental toxin, lifestyle exposure, infection, diet, protective allele, or protective behavior has been shown to alter ADSA1 occurrence or progression. No disease-specific gene–environment interaction has been reported. Acquired toxic, autoimmune, nutritional, and paraneoplastic sensory neuronopathies are important **differential diagnoses**, not established modifiers of RNF170 disease. (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 2-4, cortese2020mutationinrnf170 pages 1-1)

## 3. Phenotypes

### Core and variable manifestations

| Manifestation | Characteristics and evidence | Suggested HPO term |
|---|---|---|
| Sensory ataxia | Core, apparently universal among clinically affected reported cases; chronic and progressive | Sensory ataxia, **HP:0002066** |
| Gait ataxia/unsteadiness | Common presenting disability; may progress to need for a walking aid | Gait ataxia, **HP:0002064**; unsteady gait, **HP:0002317** |
| Impaired proprioception | Reduced joint-position and vibration sense, usually distal and lower-limb predominant | Impaired proprioception, **HP:0010831**; decreased vibration sense, **HP:0006934** |
| Positive Romberg sign | Reflects visual compensation for proprioceptive failure | Positive Romberg sign, **HP:0002403** |
| Sensory loss/dysesthesia | Feet and legs first; hands may become involved; pinprick can also be reduced | Distal sensory impairment, **HP:0002936**; paresthesia, **HP:0003401** |
| Hyporeflexia/areflexia | Variable, especially with peripheral ganglion/postganglionic involvement | Hyporeflexia, **HP:0001265**; areflexia, **HP:0001284** |
| Pyramidal signs | Babinski signs, hypertonia, or spastic-ataxic gait in a subset; 3/10 in an earlier summarized cohort had pyramidal signs without manifest spasticity | Babinski sign, **HP:0003487**; lower-limb hyperreflexia, **HP:0002395**; spasticity, **HP:0001257** |
| Sensory neuropathy/ganglionopathy | Variable; SNAPs can be reduced or absent despite normal motor conduction | Sensory neuropathy, **HP:0000763** |
| Vestibular areflexia | Documented bilaterally in the Ecuadorian index case; may emerge in advanced disease and mimic CANVAS | Bilateral vestibular hypofunction, **HP:0031609** |
| Upper-limb ataxia/pseudoathetosis | Usually later or milder than lower-limb gait involvement | Limb ataxia, **HP:0002070**; pseudoathetosis, **HP:0011443** |
| Slow-pursuit abnormality | Variable oculomotor finding; does not establish cerebellar degeneration | Abnormal smooth pursuit, **HP:0000617** |

The Belgian family had onset at ages **35, 55, 64, and 68 years** in four affected relatives. The Ecuadorian proband developed poor balance at **47 years** and required a walking aid by 57; her father and grandmother reportedly began near age 60. Across earlier reports, onset ranged from the **fourth through eighth decades**. (cortese2020mutationinrnf170 pages 1-2, wagner2019biallelicvariantsin pages 8-10, daele2022rnf170mutationcauses pages 1-2)

### Laboratory, neurophysiological, and imaging phenotypes

- **Somatosensory evoked potentials:** delayed, abnormal, or absent lower-extremity responses support posterior-column/preganglionic dysfunction.
- **Nerve conduction:** motor studies are generally normal. SNAPs may be preserved in classic Canadian disease but reduced or absent in Belgian and Ecuadorian cases, demonstrating genuine phenotypic variability rather than a mandatory normal sensory NCS.
- **MRI:** brain MRI can be normal without cerebellar atrophy. Cervical spinal MRI may show posterior-column T2 hyperintensity and volume loss, although normal spinal MRI has also been reported. Frontal atrophy was described in one Belgian evaluation but is not established as a defining feature.
- **Vestibular testing:** video head-impulse or equivalent testing may demonstrate reduced vestibulo-ocular-reflex gain bilaterally. (cortese2020mutationinrnf170 pages 1-1, daele2022rnf170mutationcauses pages 1-2, cortese2020mutationinrnf170 pages 2-2)

### Quality-of-life effect

Progressive imbalance, loss of position sense, and vestibular impairment increase falls, restrict independent mobility, and may eventually require a cane, walker, or other aid. No ADSA1-specific EQ-5D, SF-36, PROMIS, employment, caregiver-burden, or activities-of-daily-living datasets were found. The Ecuadorian case provides direct evidence of meaningful mobility disability over approximately ten years. (cortese2020mutationinrnf170 pages 1-2)

## 4. Genetic and molecular information

### Gene and variant

- **Gene:** RNF170, encoding an endoplasmic-reticulum membrane RING-finger E3 ubiquitin ligase.
- **Dominant ADSA1 variant:** NM transcript-dependent notation **c.595C>T; p.Arg199Cys (R199C)**.
- **Variant class:** germline heterozygous missense substitution in a transmembrane region.
- **Population frequency:** no numerical gnomAD, TOPMed, 1000 Genomes, or ExAC frequency was recovered; the familial evidence and scarcity of reports imply extreme rarity, but a database value should be checked directly before production curation.
- **Clinical classification:** the family-level segregation and repeated phenotype association support pathogenicity for ADSA1. A current ClinVar assertion and review status were not independently recovered and should not be inferred from the papers alone.
- **Somatic status:** no somatic disease mechanism is known.

Arg199's positive charge appears important for ionic interactions that stabilize the transmembrane region. The substitution is associated with reduced RNF170 abundance through increased autoubiquitination and proteasomal degradation, but the dominant clinical mechanism is not adequately explained by simple haploinsufficiency because heterozygous carriers of truncating variants can be unaffected. A variant-specific toxic gain of function is therefore favored, although the exact toxic species and basis of sensory-neuron selectivity remain unresolved. (daele2022rnf170mutationcauses pages 2-4, wagner2019biallelicvariantsin pages 8-10, cook2024rnf170frameshiftdeletion pages 10-12, wagner2019biallelicvariantsin pages 10-11)

### Allelic-disorder warning

Biallelic RNF170 variants—including splice, missense, multiexon/genomic-deletion, and frameshift alleles—cause an autosomal-recessive HSP with onset usually before age five, progressive lower-limb spasticity, and frequent optic atrophy. Wagner et al. studied nine affected individuals from four families; seven had optic atrophy and median onset was two years. These variants and phenotypes must not be entered as ADSA1-associated dominant variants. (wagner2019biallelicvariantsin pages 8-10, wagner2019biallelicvariantsin pages 3-4)

No established ADSA1 modifier gene, chromosomal abnormality, DNA-methylation signature, histone alteration, or chromatin mechanism was identified.

## 5. Environmental information

ADSA1 is a monogenic inherited disorder. No evidence supports pollution, radiation, occupation, smoking, alcohol, diet, physical inactivity, or infectious agents as causal or triggering factors. Avoiding neurotoxic exposures—such as excessive pyridoxine or certain chemotherapy agents—is prudent in a person with sensory dysfunction but represents prevention of superimposed neuropathy, not prevention of RNF170 disease. (cortese2020mutationinrnf170 pages 1-2, cortese2020mutationinrnf170 pages 1-1)

## 6. Mechanism and pathophysiology

### Normal pathway

RNF170 is an ER-membrane E3 ubiquitin ligase. Following activation of inositol 1,4,5-trisphosphate receptors (**IP3Rs/ITPRs**), the ERLIN1–ERLIN2 complex recruits RNF170, which ubiquitinates the activated receptors and directs them toward ER-associated degradation and proteasomal turnover. This feedback limits IP3-mediated calcium release from the ER and helps restore calcium homeostasis. (wagner2019biallelicvariantsin pages 10-11, wagner2019biallelicvariantsin pages 1-2, wagner2019biallelicvariantsin pages 11-12)

The abstract of Wagner et al. states directly: **“We provide evidence that mutations in the ubiquitin E3 ligase gene RNF170, which targets inositol 1,4,5-trisphosphate receptors for degradation, are the likely cause of autosomal recessive HSP in four unrelated families.”** It further concludes that the findings **“highlight inositol 1,4,5-trisphosphate signaling as a candidate key pathway for hereditary spastic paraplegias and cerebellar ataxias.”** Although this experiment concerned recessive HSP, the biochemical pathway is relevant to interpreting dominant RNF170 disease. (wagner2019biallelicvariantsin pages 1-2)

### Proposed ADSA1 causal chain

1. **Upstream genetic trigger:** heterozygous p.Arg199Cys alters a critical RNF170 transmembrane residue.
2. **Protein effect:** altered intramembrane interactions and RNF170 instability, with increased autoubiquitination/proteasomal turnover.
3. **Pathway disturbance:** dysregulated RNF170–ERLIN1/2–IP3R quality control and abnormal ER calcium signaling; available data favor a p.Arg199Cys-specific toxic gain of function rather than generic dosage loss.
4. **Cellular vulnerability:** long-projecting proprioceptive sensory neurons—dorsal-root-ganglion neurons and their posterior-column axons—are preferentially impaired or lost. The reason for this selectivity is unknown.
5. **Tissue pathology:** dysfunction/degeneration of central sensory tracts, with variable ganglionic/postganglionic and vestibular involvement.
6. **Clinical output:** loss of proprioceptive input causes Romberg-positive sensory ataxia; involvement of corticospinal pathways adds pyramidal signs, and vestibular involvement can produce a CANVAS-like syndrome. (cortese2020mutationinrnf170 pages 1-2, wagner2019biallelicvariantsin pages 8-10, daele2022rnf170mutationcauses pages 4-5, wagner2019biallelicvariantsin pages 10-11)

### Suggested ontology annotations

- **GO biological process:** protein ubiquitination (GO:0016567); ER-associated ubiquitin-dependent protein catabolic process (GO:0030433); proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161); regulation of cytosolic calcium-ion concentration (GO:0051480); inositol-1,4,5-trisphosphate-sensitive calcium-release channel activity pathway.
- **GO molecular function:** ubiquitin-protein transferase activity (GO:0004842); ligase activity (GO:0016874).
- **GO cellular component:** endoplasmic-reticulum membrane (GO:0005789); integral component of ER membrane.
- **Cell Ontology:** sensory neuron (CL:0000526); peripheral sensory neuron (CL:0000101); dorsal-root-ganglion neuron; proprioceptor (CL:0000199).

No disease-specific human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics profile was found. Immune activation, fibrosis, ischemia, primary mitochondrial failure, and a defined metabolic signature are not established components of ADSA1.

## 7. Anatomical structures affected

The **nervous system** is the primary affected system. Principal sites are bilateral and length-dependent rather than unilateral:

- dorsal-root ganglia and large myelinated sensory neurons;
- peripheral sensory axons in cases with ganglionopathy;
- posterior/dorsal columns of the cervical and more caudal spinal cord;
- proprioceptive pathways and somatosensory projections;
- variably, corticospinal tracts and bilateral vestibular pathways.

The cerebellum may be structurally normal; therefore, “ataxia” should not automatically be annotated as primary cerebellar degeneration. No consistent involvement of heart, lung, kidney, endocrine, gastrointestinal, or immune organs has been established. (wagner2019biallelicvariantsin pages 8-10, cortese2020mutationinrnf170 pages 1-1, cortese2020mutationinrnf170 pages 2-2)

Suggested anatomy terms include **UBERON:0000955 nervous system**, **UBERON:0002240 spinal cord**, **UBERON:0002392 dorsal root ganglion**, **UBERON:0002291 posterior funiculus**, and **UBERON:0002037 cerebellum** only when documenting a normal/differential assessment rather than proven primary disease.

## 8. Temporal development

Onset is chronic and insidious, typically in adulthood or later life. Published individual onsets range from 35 to 68 years, while summarized historical observations extend into the eighth decade. Early disease commonly consists of fatigue, imbalance, or distal sensory symptoms; intermediate disease adds marked proprioceptive loss, Romberg positivity, and gait ataxia; advanced disease may include upper-limb sensory ataxia, sensory ganglionopathy, pyramidal signs, vestibular areflexia, and dependence on mobility aids. (cortese2020mutationinrnf170 pages 1-2, wagner2019biallelicvariantsin pages 8-10, daele2022rnf170mutationcauses pages 1-2)

The course is slowly progressive and lifelong. No relapsing-remitting pattern, spontaneous remission, disease stage system, validated progression rate, or critical therapeutic window has been defined.

## 9. Inheritance and population

Inheritance is autosomal dominant. Available reports support vertical transmission in both sexes, without evidence for sex limitation. The Canadian founder haplotype indicates a regional founder effect, but ADSA1 has also been detected in Ecuadorian and Belgian/European families. By 2022, the literature described two Canadian families, one Ecuadorian family, and one Belgian family; this is case ascertainment, not a population prevalence estimate. (daele2022rnf170mutationcauses pages 2-4, cortese2020mutationinrnf170 pages 1-2)

No defensible incidence per 100,000, prevalence per 100,000, carrier frequency, sex ratio, ethnic-risk estimate, or geographic burden is available. Penetrance is probably age-dependent but cannot be quantified. Expressivity is clearly variable: central posterior-column disease predominates in some families, whereas sensory ganglionopathy, pyramidal findings, or vestibular areflexia occur in others. Consanguinity is not relevant to the dominant disorder, though it is relevant to recessive RNF170-HSP.

## 10. Diagnostics

### Clinical and physiological work-up

A practical diagnostic sequence is:

1. Document sensory rather than primary cerebellar ataxia: Romberg testing, vibration and joint-position sensation, reflexes, pinprick, pseudoathetosis, eye movements, and pyramidal signs.
2. Obtain motor and sensory NCS/EMG. Normal motor conduction with preserved or reduced/absent SNAPs is compatible with the spectrum.
3. Perform tibial/median SSEPs to identify central or preganglionic sensory-pathway dysfunction.
4. Obtain brain and cervical-spine MRI, looking for posterior-column signal/atrophy and assessing cerebellar structure.
5. If oscillopsia or a CANVAS-like presentation is present, assess vestibulo-ocular reflexes using video head-impulse testing, calorics, or rotational testing.
6. Exclude acquired sensory neuronopathy: nutritional deficiencies, paraproteinemia, Sjögren/autoimmune disease, paraneoplastic anti-Hu disease, infection where indicated, and medication/toxin exposure.
7. Conduct genetic testing. (cortese2020mutationinrnf170 pages 1-2, cortese2020mutationinrnf170 pages 2-2, cortese2020mutationinrnf170 pages 1-1)

### Genetic testing

Targeted sequencing of **RNF170**, including direct testing for c.595C>T, is appropriate when the phenotype and dominant pedigree are compelling. More commonly, RNF170 should be included in a hereditary ataxia, sensory-neuropathy, or combined ataxia/HSP panel. The Belgian authors specifically recommended RNF170 inclusion in ataxia panels, while the Ecuadorian report recommended RNF170 testing in **RFC1-negative CANVAS-like disease with dominant family history**. (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 1-2, daele2022rnf170mutationcauses pages 2-4)

Testing should usually first or concurrently address common repeat expansions because standard WES may miss them, especially biallelic **RFC1 AAGGG** expansions and dominant spinocerebellar-ataxia expansions. WES is useful when panel testing is negative; WGS may identify sequence and structural variants and improve repeat analysis if the validated pipeline supports it. CMA, karyotyping, FISH, mitochondrial testing, and RNA sequencing are not first-line ADSA1 tests unless other clinical or variant-specific evidence warrants them.

No formal society diagnostic criteria, biochemical biomarker, enzyme assay, liquid biopsy, epigenomic test, or validated prognostic biomarker exists.

### Differential diagnosis

Key alternatives are RFC1-related CANVAS; Friedreich ataxia; dominant spinocerebellar ataxias; POLG-related mitochondrial sensory ataxia; vitamin-E deficiency; abetalipoproteinemia; CMT4C and other inherited neuropathies; Sjögren sensory neuronopathy; anti-Hu/paraneoplastic ganglionopathy; and pyridoxine-, cisplatin-, or other toxin-associated neuropathy. Absence of cerebellar atrophy, a dominant pedigree, prominent posterior-column physiology, and RNF170 p.Arg199Cys distinguish ADSA1, but no single clinical sign is pathognomonic. (daele2022rnf170mutationcauses pages 2-4, cortese2020mutationinrnf170 pages 1-1)

## 11. Outcome and prognosis

ADSA1 causes chronic progressive neurological disability, principally impaired balance, falls, and declining independent ambulation. One Ecuadorian patient progressed from initial imbalance at 47 to requiring a walking aid by 57. The late onset and absence of reported systemic organ failure suggest that morbidity rather than early mortality is the dominant concern, but available studies are too small to conclude that life expectancy is normal. (cortese2020mutationinrnf170 pages 1-2)

No five- or ten-year survival rate, standardized disability trajectory, mortality rate, recovery rate, or quality-of-life score is available. Neurological recovery is not documented; stabilization with supportive care has not been quantified. Potential adverse prognostic features—earlier onset, ganglionopathy, pyramidal involvement, or vestibular areflexia—are plausible but unvalidated.

## 12. Treatment and current implementation

No disease-modifying pharmacotherapy, approved RNF170-targeted therapy, gene therapy, ASO, siRNA, cell therapy, immunotherapy, surgical treatment, pharmacogenomic rule, or genotype-specific treatment algorithm exists. The ClinicalTrials.gov search retrieved no relevant disease-specific interventional trial. Published human reports do not provide response rates or controlled treatment outcomes. (cortese2020mutationinrnf170 pages 1-2, daele2022rnf170mutationcauses pages 1-2)

Current care is supportive and should be individualized:

- neurologic and rehabilitation follow-up;
- physical therapy for balance, strength, gait, and safe transfers;
- occupational therapy and home-safety modification;
- cane, trekking poles, walker, orthoses, or wheelchair as needed;
- vestibular rehabilitation when bilateral hypofunction is present;
- fall prevention, footwear and foot inspection where sensation is reduced;
- treatment of neuropathic pain or dysesthesia using standard agents when present;
- correction of superimposed nutritional deficiencies and avoidance of sensory neurotoxins;
- genetic counseling and family cascade testing.

Suggested NCIt intervention concepts include **Physical Therapy (NCIT:C15308)**, **Occupational Therapy**, **Rehabilitation Therapy**, **Genetic Counseling (NCIT:C15241)**, and **Assistive Device**. These are supportive interventions extrapolated from neurological rehabilitation practice, not ADSA1-tested treatments.

The RNF170–ERLIN–IP3R pathway is a biologically plausible therapeutic target, but indiscriminate inhibition or enhancement could disrupt calcium homeostasis. Expert interpretation should therefore treat pathway modulation as preclinical, not clinically actionable. (wagner2019biallelicvariantsin pages 10-11, wagner2019biallelicvariantsin pages 1-2)

## 13. Prevention

Primary prevention through lifestyle modification or immunization is not possible for a germline dominant disorder. Secondary prevention consists of early molecular diagnosis, cascade testing of adult relatives who choose testing, baseline neurological assessment, and early fall-risk intervention. Tertiary prevention includes rehabilitation, mobility aids, home modification, vestibular therapy, prevention of injury, and avoidance of additional neuropathic insults.

After identification of a familial pathogenic variant, prenatal diagnosis and preimplantation genetic testing are technically feasible. Predictive testing of asymptomatic adults requires counseling about uncertain age-specific penetrance and the absence of preventive disease-modifying therapy. Testing minors for a usually adult-onset disorder should follow established ethics guidance and generally be deferred unless a clear childhood medical benefit emerges.

## 14. Other species and natural disease

A 2024 study/preprint reported naturally occurring autosomal-recessive neuroaxonal dystrophy in **Miniature American Shepherd dogs** (*Canis lupus familiaris*; NCBI Taxon **9615**) caused by **RNF170 c.367delG, p.Ala123Glnfs*11**. Affected young-adult dogs developed pelvic-limb weakness and ataxia; **23/27 homozygotes (85%)** were clinically affected, and linkage reached **LOD 9.70**. The abstract states that the deletion **“perfectly segregates in an autosomal recessive pattern”** and describes the dogs as an opportunity for therapeutic trials because of their relatively long lifespan. (cook2024rnf170frameshiftdeletion pages 10-12)

This is a valuable large-animal model of RNF170-associated neurodegeneration, but it models recessive truncating loss of function and neuroaxonal dystrophy—not human dominant p.Arg199Cys ADSA1. No zoonotic transmission is applicable, and no naturally occurring nonhuman disease with the exact dominant human variant was identified.

## 15. Model organisms

### Mouse

Rnf170-null mice develop age-dependent gait abnormalities at approximately 12 months, involving interlimb coupling and step-sequence organization. They support a role for RNF170 in long-term nervous-system integrity but are loss-of-function models and do not reproduce the human heterozygous p.Arg199Cys mechanism exactly. (cook2024rnf170frameshiftdeletion pages 10-12, wagner2019biallelicvariantsin pages 10-11)

### Zebrafish

Zebrafish knockdown and RNF170-expression experiments demonstrate developmental and neuronal consequences of disturbed RNF170 function, including abnormal body axis, eye/brain development, and impaired neurogenesis in loss-of-function paradigms. Separate expression work found dose-dependent toxicity from Arg199Cys, supporting a variant-specific toxic effect. These assays are mechanistically informative but cannot model decades-long human sensory tract degeneration. (cortese2020mutationinrnf170 pages 1-2, wagner2019biallelicvariantsin pages 10-11, wagner2019biallelicvariantsin pages 8-10)

### Cellular systems

Patient fibroblasts and engineered SH-SY5Y neuroblastoma cells have been used to measure RNF170 abundance and IP3R degradation. Recessive loss-of-function variants increase basal IP3R levels and impair ligand-stimulated receptor degradation, supporting the RNF170–ERLIN–IP3R–ERAD mechanism. These systems lack mature proprioceptive-neuron architecture and therefore do not explain selective posterior-column vulnerability. (wagner2019biallelicvariantsin pages 1-2, wagner2019biallelicvariantsin pages 11-12, wagner2019biallelicvariantsin pages 8-10)

No validated ADSA1 patient-derived iPSC proprioceptor, sensory organoid, conditional p.Arg199Cys knock-in mouse, or humanized large-animal model was identified. Developing such models is a major research priority.

## Recent developments and evidence gaps

The most relevant recent development in 2023–2024 was the 2024 canine RNF170 frameshift model, which broadens comparative understanding and may provide a practical platform for longitudinal biomarker and treatment studies. It does not, however, resolve the dominant p.Arg199Cys mechanism. No 2023–2024 human ADSA1 natural-history cohort, therapeutic trial, molecular biomarker study, or multi-omics analysis was identified. The most recent directly informative human dominant-family study retrieved was published online in 2021/print 2022 and expanded the phenotype to variable pyramidal involvement. (daele2022rnf170mutationcauses pages 2-4, daele2022rnf170mutationcauses pages 1-2, cook2024rnf170frameshiftdeletion pages 10-12)

Highest-priority research needs are: international case aggregation; standardized NCS/SSEP/vestibular phenotyping; direct population-frequency and ClinVar curation; longitudinal disability and quality-of-life measurement; p.Arg199Cys knock-in and patient-iPSC sensory-neuron models; and experiments distinguishing altered IP3R regulation from other toxic RNF170 substrates.

## Key publications

1. **Foundational RNF170 association**, literature indexed as PMID **21115467**; linked by Open Targets to MONDO:0012166. (OpenTargets Search: Autosomal dominant sensory ataxia 1)
2. **Cortese et al.** “Mutation in RNF170 causes sensory ataxic neuropathy with vestibular areflexia: a CANVAS mimic.” *Journal of Neurology, Neurosurgery & Psychiatry*. Published September 2020. DOI/URL: https://doi.org/10.1136/jnnp-2020-323719. (cortese2020mutationinrnf170 pages 1-2)
3. **Van Daele et al.** “RNF170 mutation causes autosomal dominant sensory ataxia with variable pyramidal involvement.” *European Journal of Neurology* 29:345–349. Online September 2021/2022 volume. DOI/URL: https://doi.org/10.1111/ene.15091. (daele2022rnf170mutationcauses pages 2-4, daele2022rnf170mutationcauses pages 1-2)
4. **Wagner et al.** “Bi-allelic variants in RNF170 are associated with hereditary spastic paraplegia.” *Nature Communications*. Published October 2019. DOI/URL: https://doi.org/10.1038/s41467-019-12620-9. This is mechanistic/allelic-disorder evidence, not a dominant ADSA1 cohort. (wagner2019biallelicvariantsin pages 1-2, wagner2019biallelicvariantsin pages 3-4)
5. **Kim et al.** “Age-dependent gait abnormalities in mice lacking the Rnf170 gene linked to human autosomal-dominant sensory ataxia.” *Human Molecular Genetics* 24:7196–7206. Published December 2015. DOI/URL: https://doi.org/10.1093/hmg/ddv417. (cook2024rnf170frameshiftdeletion pages 10-12)
6. **Cook et al.** “RNF170 frameshift deletion in Miniature American Shepherd dogs with neuroaxonal dystrophy provides a naturally occurring model for human RNF170 phenotypic spectrum.” Posted February 2024. DOI/URL: https://doi.org/10.21203/rs.3.rs-3914204/v1. Its preprint/publication status should be checked before assigning the highest evidence grade. (cook2024rnf170frameshiftdeletion pages 10-12)

**Overall evidence assessment:** strong evidence links heterozygous RNF170 p.Arg199Cys to a recognizable autosomal-dominant sensory-ataxia syndrome, but virtually all clinical knowledge comes from a handful of families. Mechanistic evidence firmly places RNF170 in ER-associated IP3R ubiquitination and calcium regulation; the exact p.Arg199Cys dominant-toxic mechanism, neuronal selectivity, epidemiology, prognosis, and treatment remain incompletely defined.

References

1. (cortese2020mutationinrnf170 pages 1-2): Andrea Cortese, Ilaria Callegari, Riccardo Currò, Elisa Vegezzi, Silvia Colnaghi, Maurizio Versino, Enrico Alfonsi, Giuseppe Cosentino, Enzamaria Valente, Simone Gana, Cristina Tassorelli, Anna Pichiecchio, Alexander M Rossor, Enrico Bugiardini, Antonio Biroli, Daniela Di Capua, Henry Houlden, and Mary M Reilly. Mutation in rnf170 causes sensory ataxic neuropathy with vestibular areflexia: a canvas mimic. Journal of Neurology, Neurosurgery, and Psychiatry, 91:1237-1238, Sep 2020. URL: https://doi.org/10.1136/jnnp-2020-323719, doi:10.1136/jnnp-2020-323719. This article has 24 citations.

2. (daele2022rnf170mutationcauses pages 2-4): Sien H. Van Daele, Matthieu Moisse, Valérie Race, Amélie Van Eesbeeck, Liesbeth Keldermans, Sascha Vermeer, Hilde Van Esch, Kristl G. Claeys, and Philip Van Damme. <i>rnf170</i> mutation causes autosomal dominant sensory ataxia with variable pyramidal involvement. European Journal of Neurology, 29:345-349, Sep 2022. URL: https://doi.org/10.1111/ene.15091, doi:10.1111/ene.15091. This article has 9 citations and is from a domain leading peer-reviewed journal.

3. (wagner2019biallelicvariantsin pages 8-10): Matias Wagner, Daniel P. S. Osborn, Ina Gehweiler, Maike Nagel, Ulrike Ulmer, Somayeh Bakhtiari, Rim Amouri, Reza Boostani, Faycal Hentati, Maryam M. Hockley, Benedikt Hölbling, Thomas Schwarzmayr, Ehsan Ghayoor Karimiani, Christoph Kernstock, Reza Maroofian, Wolfgang Müller-Felber, Ege Ozkan, Sergio Padilla-Lopez, Selina Reich, Jennifer Reichbauer, Hossein Darvish, Neda Shahmohammadibeni, Abbas Tafakhori, Katharina Vill, Stephan Zuchner, Michael C. Kruer, Juliane Winkelmann, Yalda Jamshidi, and Rebecca Schüle. Bi-allelic variants in rnf170 are associated with hereditary spastic paraplegia. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12620-9, doi:10.1038/s41467-019-12620-9. This article has 62 citations and is from a highest quality peer-reviewed journal.

4. (daele2022rnf170mutationcauses pages 1-2): Sien H. Van Daele, Matthieu Moisse, Valérie Race, Amélie Van Eesbeeck, Liesbeth Keldermans, Sascha Vermeer, Hilde Van Esch, Kristl G. Claeys, and Philip Van Damme. <i>rnf170</i> mutation causes autosomal dominant sensory ataxia with variable pyramidal involvement. European Journal of Neurology, 29:345-349, Sep 2022. URL: https://doi.org/10.1111/ene.15091, doi:10.1111/ene.15091. This article has 9 citations and is from a domain leading peer-reviewed journal.

5. (wagner2019biallelicvariantsin pages 1-2): Matias Wagner, Daniel P. S. Osborn, Ina Gehweiler, Maike Nagel, Ulrike Ulmer, Somayeh Bakhtiari, Rim Amouri, Reza Boostani, Faycal Hentati, Maryam M. Hockley, Benedikt Hölbling, Thomas Schwarzmayr, Ehsan Ghayoor Karimiani, Christoph Kernstock, Reza Maroofian, Wolfgang Müller-Felber, Ege Ozkan, Sergio Padilla-Lopez, Selina Reich, Jennifer Reichbauer, Hossein Darvish, Neda Shahmohammadibeni, Abbas Tafakhori, Katharina Vill, Stephan Zuchner, Michael C. Kruer, Juliane Winkelmann, Yalda Jamshidi, and Rebecca Schüle. Bi-allelic variants in rnf170 are associated with hereditary spastic paraplegia. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12620-9, doi:10.1038/s41467-019-12620-9. This article has 62 citations and is from a highest quality peer-reviewed journal.

6. (wagner2019biallelicvariantsin pages 3-4): Matias Wagner, Daniel P. S. Osborn, Ina Gehweiler, Maike Nagel, Ulrike Ulmer, Somayeh Bakhtiari, Rim Amouri, Reza Boostani, Faycal Hentati, Maryam M. Hockley, Benedikt Hölbling, Thomas Schwarzmayr, Ehsan Ghayoor Karimiani, Christoph Kernstock, Reza Maroofian, Wolfgang Müller-Felber, Ege Ozkan, Sergio Padilla-Lopez, Selina Reich, Jennifer Reichbauer, Hossein Darvish, Neda Shahmohammadibeni, Abbas Tafakhori, Katharina Vill, Stephan Zuchner, Michael C. Kruer, Juliane Winkelmann, Yalda Jamshidi, and Rebecca Schüle. Bi-allelic variants in rnf170 are associated with hereditary spastic paraplegia. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12620-9, doi:10.1038/s41467-019-12620-9. This article has 62 citations and is from a highest quality peer-reviewed journal.

7. (OpenTargets Search: Autosomal dominant sensory ataxia 1): Open Targets Query (Autosomal dominant sensory ataxia 1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (cortese2020mutationinrnf170 pages 1-1): Andrea Cortese, Ilaria Callegari, Riccardo Currò, Elisa Vegezzi, Silvia Colnaghi, Maurizio Versino, Enrico Alfonsi, Giuseppe Cosentino, Enzamaria Valente, Simone Gana, Cristina Tassorelli, Anna Pichiecchio, Alexander M Rossor, Enrico Bugiardini, Antonio Biroli, Daniela Di Capua, Henry Houlden, and Mary M Reilly. Mutation in rnf170 causes sensory ataxic neuropathy with vestibular areflexia: a canvas mimic. Journal of Neurology, Neurosurgery, and Psychiatry, 91:1237-1238, Sep 2020. URL: https://doi.org/10.1136/jnnp-2020-323719, doi:10.1136/jnnp-2020-323719. This article has 24 citations.

9. (cortese2020mutationinrnf170 pages 2-2): Andrea Cortese, Ilaria Callegari, Riccardo Currò, Elisa Vegezzi, Silvia Colnaghi, Maurizio Versino, Enrico Alfonsi, Giuseppe Cosentino, Enzamaria Valente, Simone Gana, Cristina Tassorelli, Anna Pichiecchio, Alexander M Rossor, Enrico Bugiardini, Antonio Biroli, Daniela Di Capua, Henry Houlden, and Mary M Reilly. Mutation in rnf170 causes sensory ataxic neuropathy with vestibular areflexia: a canvas mimic. Journal of Neurology, Neurosurgery, and Psychiatry, 91:1237-1238, Sep 2020. URL: https://doi.org/10.1136/jnnp-2020-323719, doi:10.1136/jnnp-2020-323719. This article has 24 citations.

10. (wagner2019biallelicvariantsin pages 10-11): Matias Wagner, Daniel P. S. Osborn, Ina Gehweiler, Maike Nagel, Ulrike Ulmer, Somayeh Bakhtiari, Rim Amouri, Reza Boostani, Faycal Hentati, Maryam M. Hockley, Benedikt Hölbling, Thomas Schwarzmayr, Ehsan Ghayoor Karimiani, Christoph Kernstock, Reza Maroofian, Wolfgang Müller-Felber, Ege Ozkan, Sergio Padilla-Lopez, Selina Reich, Jennifer Reichbauer, Hossein Darvish, Neda Shahmohammadibeni, Abbas Tafakhori, Katharina Vill, Stephan Zuchner, Michael C. Kruer, Juliane Winkelmann, Yalda Jamshidi, and Rebecca Schüle. Bi-allelic variants in rnf170 are associated with hereditary spastic paraplegia. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12620-9, doi:10.1038/s41467-019-12620-9. This article has 62 citations and is from a highest quality peer-reviewed journal.

11. (wagner2019biallelicvariantsin pages 11-12): Matias Wagner, Daniel P. S. Osborn, Ina Gehweiler, Maike Nagel, Ulrike Ulmer, Somayeh Bakhtiari, Rim Amouri, Reza Boostani, Faycal Hentati, Maryam M. Hockley, Benedikt Hölbling, Thomas Schwarzmayr, Ehsan Ghayoor Karimiani, Christoph Kernstock, Reza Maroofian, Wolfgang Müller-Felber, Ege Ozkan, Sergio Padilla-Lopez, Selina Reich, Jennifer Reichbauer, Hossein Darvish, Neda Shahmohammadibeni, Abbas Tafakhori, Katharina Vill, Stephan Zuchner, Michael C. Kruer, Juliane Winkelmann, Yalda Jamshidi, and Rebecca Schüle. Bi-allelic variants in rnf170 are associated with hereditary spastic paraplegia. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12620-9, doi:10.1038/s41467-019-12620-9. This article has 62 citations and is from a highest quality peer-reviewed journal.

12. (cook2024rnf170frameshiftdeletion pages 10-12): Shawna R. Cook, Cleo Schwarz, Julien Guevar, Charles-Antoine Assenmacher, Maeve Sheehy, Nathan Fanzone, Molly E. Church, Leonardo Murgiano, Margret L. Casal, Vidhya Jagannathan, Rodrigo Gutierrez-Quintana, Mark Lowrie, Frank Steffen, Tosso Leeb, and Kari J. Ekenstedt. Rnf170 frameshift deletion in miniature american shepherd dogs with neuroaxonal dystrophy provides a naturally occurring model for human rnf170 phenotypic spectrum. Unknown journal, Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3914204/v1, doi:10.21203/rs.3.rs-3914204/v1.

13. (daele2022rnf170mutationcauses pages 4-5): Sien H. Van Daele, Matthieu Moisse, Valérie Race, Amélie Van Eesbeeck, Liesbeth Keldermans, Sascha Vermeer, Hilde Van Esch, Kristl G. Claeys, and Philip Van Damme. <i>rnf170</i> mutation causes autosomal dominant sensory ataxia with variable pyramidal involvement. European Journal of Neurology, 29:345-349, Sep 2022. URL: https://doi.org/10.1111/ene.15091, doi:10.1111/ene.15091. This article has 9 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Sensory_Ataxia_1-deep-research-falcon_artifacts/artifact-00.md)