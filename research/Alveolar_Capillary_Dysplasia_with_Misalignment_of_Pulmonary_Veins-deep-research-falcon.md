---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T13:19:47.107507'
end_time: '2026-08-01T13:31:32.733042'
duration_seconds: 705.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alveolar capillary dysplasia with misalignment of pulmonary veins
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
  path: Alveolar_Capillary_Dysplasia_with_Misalignment_of_Pulmonary_Veins-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alveolar capillary dysplasia with misalignment of pulmonary veins
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Alveolar capillary dysplasia with misalignment of pulmonary veins** covering all of the
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
- **Disease Name:** Alveolar capillary dysplasia with misalignment of pulmonary veins
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Alveolar capillary dysplasia with misalignment of pulmonary veins** covering all of the
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


# Alveolar capillary dysplasia with misalignment of pulmonary veins (ACDMPV)

## Executive summary

Alveolar capillary dysplasia with misalignment of pulmonary veins (ACDMPV) is an ultra-rare, congenital developmental disorder of the pulmonary microvasculature and alveolar gas-exchange unit. Most affected infants develop cyanosis, profound hypoxemia, persistent pulmonary hypertension, and respiratory failure within hours to two days after birth. Typical disease is resistant to mechanical ventilation, pulmonary vasodilators, and extracorporeal membrane oxygenation (ECMO), and is usually fatal in the neonatal period. A minority have patchy or atypical disease with delayed presentation and may survive long enough for bilateral lung transplantation. Human genetic evidence establishes heterozygous loss of **FOXF1** function—through coding variants, gene deletions, or deletion/disruption of its distant regulatory region at chromosome 16q24.1—as the principal cause. The major recent advance is a 2023 human single-cell RNA/ATAC study showing that FOXF1 insufficiency depletes pulmonary CAP1/CAP2 endothelial progenitors, pericytes, and mature capillary endothelium, secondarily disrupting alveolar epithelial differentiation and expanding systemic bronchial-type vessels. (guo2023singlecellmultiomics pages 2-3, guo2023singlecellmultiomics pages 1-2, guo2023singlecellmultiomics pages 4-6)

| domain | established finding | evidence type/strength | key quantitative detail | suggested ontology terms |
|---|---|---|---|---|
| Identifiers | ACDMPV is a rare, usually lethal developmental lung disorder caused by FOXF1 insufficiency; MIM noted as 265380 in recent primary literature. Synonym: alveolar capillary dysplasia / alveolar capillary dysplasia with misalignment of pulmonary veins. | Human primary genetics + human single-cell multiomics; strong (landmark + recent) (guo2023singlecellmultiomics pages 1-2, stankiewicz2009genomicandgenic pages 1-2) | ~200 cases reported in 2009 literature; >80% with additional malformations in early series (stankiewicz2009genomicandgenic pages 1-2) | MONDO: alveolar capillary dysplasia with misalignment of pulmonary veins; MeSH/ICD terms not confirmed from gathered evidence |
| Cause | Primary cause is germline FOXF1 haploinsufficiency due to heterozygous SNVs/indels, gene deletions, or noncoding/enhancer-region CNVs at 16q24.1. | Human primary genetics; very strong (landmark AJHG + replication) (stankiewicz2009genomicandgenic pages 6-8, kozłowska2020genotype–phenotypecorrelationin pages 1-2, sen2013novelfoxf1mutations pages 10-13) | >100 pathogenic SNVs and >70 CNV deletions reported by 2023 review of primary cases (guo2023singlecellmultiomics pages 1-2) | HGNC: FOXF1; SO: copy_number_loss, nonsense_variant, frameshift_variant, missense_variant, regulatory_region_variant |
| Regulatory genetics | Disease can result from deletions sparing FOXF1 coding sequence but removing a distant enhancer; LINC01081 positively regulates FOXF1; evidence supports partial paternal imprinting and maternal-origin pathogenic deletions. | Human primary molecular genetics; strong (szafranski2014twodeletionsoverlapping pages 3-5, szafranski2014twodeletionsoverlapping pages 5-6) | Two de novo maternal chr16 deletions; ~75 kb enhancer region implicated; severity varied with enhancer/LINC01081 involvement (szafranski2014twodeletionsoverlapping pages 5-6) | Sequence Ontology: enhancer_variant; Gene: LINC01081; GO: regulation of transcription by RNA polymerase II |
| Core presentation | Typical presentation is neonatal cyanosis, severe pulmonary hypertension, and hypoxemic respiratory failure shortly after birth, often within 48 hours, refractory to therapy. | Human clinical/pathology literature; strong (guo2023singlecellmultiomics pages 2-3, kozłowska2020genotype–phenotypecorrelationin pages 1-2, stankiewicz2009genomicandgenic pages 1-2) | Death usually in days to weeks/months; first month emphasized in landmark cohort (stankiewicz2009genomicandgenic pages 1-2) | HPO: Cyanosis, Pulmonary hypertension, Respiratory failure, Persistent pulmonary hypertension of the newborn |
| Core phenotypes | Frequent associated anomalies involve gastrointestinal, cardiovascular, and genitourinary systems; examples include intestinal malrotation, hypoplastic left heart/aortic arch lesions, omphalocele, hydronephrosis, ASD/VSD, hepatosplenomegaly. | Human case series/case reports; moderate-strong (kozłowska2020genotype–phenotypecorrelationin pages 2-4, kozłowska2020genotype–phenotypecorrelationin pages 1-2, stankiewicz2009genomicandgenic pages 1-2) | >80% had additional malformations in early series (stankiewicz2009genomicandgenic pages 1-2) | HPO: Intestinal malrotation, Omphalocele, Hydronephrosis, Atrial septal defect, Ventricular septal defect, Hepatosplenomegaly |
| Histopathology | Hallmarks are misaligned pulmonary veins adjacent to bronchioles, medial hyperplasia of small pulmonary arteries, thickened/widened alveolar septa, paucity/mislocalization of capillaries, lobular simplification/underdevelopment, and sometimes lymphangiectasis. | Human pathology + genetics; very strong (stankiewicz2009genomicandgenic pages 6-8, kozłowska2020genotype–phenotypecorrelationin pages 2-4, guo2023singlecellmultiomics pages 2-3) | In landmark 2009 series, 10/10 reviewed lungs showed characteristic changes; pulmonary lymphangiectasis seen in all 4 deletion cases and 1/4 mutation cases examined (stankiewicz2009genomicandgenic pages 6-8) | HPO: Misalignment of pulmonary veins, Decreased pulmonary capillaries, Thickened alveolar septa; UBERON: lung, pulmonary vein, pulmonary arteriole |
| Mechanism / causal chain | FOXF1 loss disrupts endothelial/pericyte developmental programs, preventing CAP1-to-CAP2 maturation and pulmonary vasculogenesis; reduced alveolar microvasculature impairs epithelial-mesenchymal signaling and AT1 differentiation, producing gas-exchange failure and severe PH. | Human single-nucleus RNA/ATAC multiomics; very strong recent mechanistic evidence (guo2023singlecellmultiomics pages 1-2, guo2023singlecellmultiomics pages 4-6, guo2023singlecellmultiomics pages 13-15, guo2023singlecellmultiomics pages 3-4) | 6 subjects analyzed; 35 cell types identified; 32,300 ACDMPV nuclei profiled; CAP2 reduction correlated with severity (guo2023singlecellmultiomics pages 3-4, guo2023singlecellmultiomics pages 4-6) | GO: vasculogenesis, angiogenesis, endothelial cell differentiation, epithelial cell differentiation, cell-cell signaling; CL: capillary endothelial cell, pericyte, fibroblast, alveolar type 1 cell, alveolar type 2 cell |
| Molecular pathways | Downregulated/perturbed pathways include PTEN, ERK/MAPK, STAT3, FAK, integrin, WNT/β-catenin, ID1, semaphorin, and Rho GTPase signaling; abnormal VEGFA signaling accompanies expansion of systemic bronchial-type ECs. | Human multiomics + supporting translational studies; strong (guo2023singlecellmultiomics pages 3-4, guo2023singlecellmultiomics pages 4-6, guo2023singlecellmultiomics pages 13-15, guo2023singlecellmultiomics pages 8-12) | 61 genes downregulated in pericytes; 58.8% of predicted FOXF1 targets validated in integrated analysis (guo2023singlecellmultiomics pages 4-6) | GO/Pathways: MAPK cascade, STAT3 signaling, integrin signaling, Wnt signaling, VEGFA-VEGFR2 signaling, semaphorin-plexin signaling |
| Cell types / anatomy | Major affected cell populations are CAP1/CAP2 capillary ECs, pericytes, AF1 fibroblasts, and alveolar epithelial cells; compensatory COL15A1+ systemic/bronchial EC expansion occurs. Primary organ is lung, with secondary cardiovascular consequences from PH. | Human multiomics + pathology; strong (guo2023singlecellmultiomics pages 4-6, guo2023singlecellmultiomics pages 3-4, guo2023singlecellmultiomics pages 1-2) | FOXF1 RNA absent in CAP1/CAP2 in 3/5 ACDMPV subjects with severe disease (guo2023singlecellmultiomics pages 3-4) | CL: endothelial cell, pericyte, fibroblast, alveolar epithelial type 1 cell, alveolar epithelial type 2 cell; UBERON: alveolus, pulmonary capillary, bronchovascular bundle |
| Diagnosis | Gold standard remains lung histopathology from biopsy/autopsy; molecular confirmation uses FOXF1 sequencing plus deletion/duplication testing/CMA for coding and enhancer CNVs. CD31/CD34 immunostaining may help. | Human primary case reports/genetics; strong for pathology + moderate for testing workflow (kozłowska2020genotype–phenotypecorrelationin pages 2-4, kozłowska2020genotype–phenotypecorrelationin pages 1-2, szafranski2014twodeletionsoverlapping pages 5-6) | Two 2020 neonates had ~1.45 Mb and ~0.7 Mb deletions identified by array CGH; one spared FOXF1 coding region (kozłowska2020genotype–phenotypecorrelationin pages 2-4) | NCIT: Lung Biopsy, Autopsy, Array Comparative Genomic Hybridization; HPO: Abnormal lung histology |
| Differential diagnosis | Important clinical differential is persistent pulmonary hypertension of the newborn; developmental lung disease / childhood interstitial lung disease framework is relevant, but tissue/genetic confirmation distinguishes ACDMPV. | Human reviews/consensus + cited genetics literature; moderate (sen2013novelfoxf1mutations pages 10-13) | No validated biomarker-only diagnostic alternative identified in gathered evidence | HPO/NCIT: Persistent pulmonary hypertension of the newborn, Interstitial lung disease |
| Treatment | Standard supportive measures (mechanical ventilation, inhaled nitric oxide, prostaglandin E1 in selected congenital-heart contexts, surfactant, inotropes, ECMO) are usually temporizing and often ineffective; bilateral lung transplantation can be life-saving in atypical survivors. | Human case reports + expert consensus; moderate-strong (szafranski2014twodeletionsoverlapping pages 3-5, kozłowska2020genotype–phenotypecorrelationin pages 2-4, kozłowska2020genotype–phenotypecorrelationin pages 1-2) | One atypical patient underwent bilateral lung transplant at 15 months; recent multiomics cohort included transplants at 9 months and 3.5 years (szafranski2014twodeletionsoverlapping pages 3-5, guo2023singlecellmultiomics pages 2-3) | NCIT: Mechanical Ventilation, Nitric Oxide, Extracorporeal Membrane Oxygenation, Lung Transplantation |
| Prognosis | Prognosis is poor and usually fatal in infancy, but variable expressivity exists with atypical late presentation and prolonged survival in a minority, often culminating in transplantation. | Human case series + 2023 multiomics; strong (guo2023singlecellmultiomics pages 2-3, stankiewicz2009genomicandgenic pages 1-2, szafranski2014twodeletionsoverlapping pages 5-6) | Severe subjects died at 2–5 weeks in the 2023 cohort; atypical survivors reached 9 months, 15 months, or 3.5 years with transplantation (guo2023singlecellmultiomics pages 3-4, szafranski2014twodeletionsoverlapping pages 3-5, guo2023singlecellmultiomics pages 2-3) | HPO: Neonatal death, Respiratory insufficiency; NCIT: Overall Survival |
| Inheritance | Usually de novo, autosomal dominant by mechanism (heterozygous loss), with reported familial cases, variable expressivity, and evidence for parental-origin effects/partial paternal imprinting. Recurrence risk may be increased if parental mosaicism is present, though ACDMPV-specific mosaicism data are limited in gathered sources. | Human primary genetics + reproductive genetics inference; moderate (sen2013novelfoxf1mutations pages 10-13, szafranski2014twodeletionsoverlapping pages 5-6, xu2023parentalmosaicismdetection pages 1-1, xu2023parentalmosaicismdetection pages 6-6) | Early series estimated ~10% familial association; parental mosaicism study in other severe de novo disorders found sperm mosaicism in 2/10 families at 2.88% and 2.5% VAF (disease-nonspecific but relevant to counseling) (stankiewicz2009genomicandgenic pages 1-2, xu2023parentalmosaicismdetection pages 4-5) | HP/GENO terms: De novo mutation, Autosomal dominant inheritance, Genomic imprinting, Germline mosaicism |
| Prenatal / reproductive testing | Prenatal detection is feasible when familial variant/CNV is known; preimplantation genetic testing and targeted prenatal diagnosis are conceptually applicable for recurrent de novo disorders and mosaicism risk. | Human reproductive genetics + disease-specific prenatal citation trail; moderate (xu2023parentalmosaicismdetection pages 1-1, xu2023parentalmosaicismdetection pages 4-5, kozłowska2020genotype–phenotypecorrelationin pages 7-7) | Deep targeted sequencing >5000× with ~0.5% VAF detection limit used for mosaicism detection in analogous severe DNM disorders (xu2023parentalmosaicismdetection pages 1-1) | NCIT: Prenatal Diagnosis, Preimplantation Genetic Testing, Genetic Counseling |
| Model / translational evidence | Mouse and integrated human-mouse data support FOXF1 roles in pulmonary endothelial and mesenchymal development; nanoparticle FOXF1 or STAT3 delivery to endothelial cells rescued pulmonary vasculogenesis in newborn mice (preclinical). | Preclinical translational evidence referenced within recent human mechanistic study; moderate (guo2023singlecellmultiomics pages 13-15, guo2023singlecellmultiomics pages 8-12) | Rescue described in newborn mice; no human interventional trial identified in gathered evidence (guo2023singlecellmultiomics pages 13-15) | NCIT: Gene Therapy; GO: lung development, vasculogenesis |
| Evidence gaps | No disease-specific interventional clinical trials were found; no robust prevalence/incidence estimates from registries were retrieved; no validated circulating biomarkers, proteomic/metabolomic signatures, spatial transcriptomics, natural animal disease, or established protective/environmental factors were identified from gathered evidence. | Evidence-gap assessment from available search results; moderate confidence | ClinicalTrials.gov search yielded no ACDMPV-specific interventional trial in gathered results | Terms as needed: Not available / evidence gap |


*Table: This compact table summarizes the strongest gathered evidence for alveolar capillary dysplasia with misalignment of pulmonary veins across clinical, genetic, mechanistic, diagnostic, prognostic, and translational domains. It is designed for rapid knowledge-base population with ontology suggestions and citation-backed findings.*

## Evidence framework

Evidence below is labeled as **human clinical/pathology**, **human genetics**, **human multiomics**, **model organism/preclinical**, or **expert consensus**. Most numerical estimates arise from small, selected case series rather than population registries. Consequently, percentages should not be interpreted as population-level penetrance or incidence.

---

## 1. Disease information

### Definition and classification

ACDMPV is a congenital disorder of lung morphogenesis characterized by deficient alveolar capillary development, abnormal localization of pulmonary veins beside pulmonary arteries and bronchioles, muscularization of small pulmonary arteries, and failure of effective alveolar–capillary gas exchange. Although traditionally grouped among childhood interstitial or diffuse developmental lung diseases, its dominant pathology is pulmonary vascular and alveolar developmental dysmaturity rather than inflammatory interstitial lung disease. The 2023 primary study calls it a “**lethal developmental disorder of lung morphogenesis caused by insufficiency of FOXF1 transcription factor function**.” (guo2023singlecellmultiomics pages 1-2)

### Identifiers and synonyms

| Resource | Identifier or preferred term | Qualification |
|---|---|---|
| OMIM | **265380**, *Alveolar capillary dysplasia with misalignment of pulmonary veins* | Confirmed in recent primary literature. |
| MONDO | **Alveolar capillary dysplasia with misalignment of pulmonary veins**; commonly mapped as **MONDO:0012071** | Database mapping should be revalidated at ingestion because ontology releases change. |
| Orphanet | **ORPHA:210122**, ACDMPV | Recommended database-level mapping; revalidate against current Orphanet release. |
| MeSH | No clearly disease-specific descriptor established in the retrieved evidence | Index through relevant concepts such as lung developmental abnormality/pulmonary hypertension. |
| ICD-10-CM | No specific ACDMPV code | Typically represented with congenital lung-malformation and pulmonary-hypertension codes; coding is jurisdiction dependent. |
| ICD-11 | No disease-specific code confirmed in the retrieved material | Use the closest congenital lung/vascular-developmental category after local coding review. |

Common names include **ACDMPV**, **ACD/MPV**, **alveolar capillary dysplasia**, **congenital alveolar capillary dysplasia**, and **alveolar capillary dysplasia with misaligned pulmonary veins**. “Misaligned pulmonary veins” is a historical pathologic description: the anomalous vessels in bronchovascular bundles may have a systemic/bronchial endothelial identity rather than simply representing normally specified pulmonary veins in the wrong position. (stankiewicz2009genomicandgenic pages 6-8, guo2023singlecellmultiomics pages 3-4)

### Data provenance

The knowledge base is aggregated primarily from autopsy and biopsy series, molecular diagnostic cohorts, individual transplant cases, and small research tissue cohorts—not longitudinal EHR population data. The 2009 landmark study examined 14 molecularly characterized patients, with histology reviewed in 10; the 2023 multiomics study analyzed six affected subjects and profiled 32,300 affected-lung nuclei. (stankiewicz2009genomicandgenic pages 6-8, guo2023singlecellmultiomics pages 3-4)

---

## 2. Etiology, risks, protective factors, and gene–environment interaction

### Primary causal factors

The established cause is **germline FOXF1 haploinsufficiency** or disruption of the FOXF1 regulatory domain at **16q24.1**. Disease-producing changes include heterozygous nonsense, frameshift, missense/DNA-binding-domain, stop-loss, splice-disrupting or other inactivating variants; whole-gene or multigene deletions; and structural/regulatory variants deleting a distant lung enhancer while leaving the FOXF1 coding sequence intact. The original 2009 study identified overlapping 16q24 deletions and four heterozygous inactivating FOXF1 variants, establishing causality. (stankiewicz2009genomicandgenic pages 6-8, stankiewicz2009genomicandgenic pages 1-2)

Approximately **80–90% of histopathologically verified cases** have a detectable FOXF1 coding or locus abnormality in several clinical summaries. By 2023, more than **100 pathogenic SNVs/indels and 70 CNV deletions** had been reported. The remaining molecularly unresolved cases may reflect difficult-to-detect regulatory or structural variants, mosaicism, alternative developmental genes, or non-genetic phenocopies; absence of a detected FOXF1 variant does not exclude pathology-confirmed ACDMPV. (guo2023singlecellmultiomics pages 1-2, kozłowska2020genotype–phenotypecorrelationin pages 1-2)

### Genetic risk factors

* A heterozygous pathogenic FOXF1 or FOXF1-regulatory variant is a high-penetrance causal risk factor for severe developmental lung disease, but expressivity varies markedly.
* Larger 16q24 deletions may encompass **FOXC2**, **FOXL1**, or neighboring regulatory elements and produce broader congenital-malformation phenotypes.
* Two maternal-chromosome deletions that spared FOXF1 but overlapped an approximately **75-kb distant enhancer** implicated both that enhancer and **LINC01081**, a lung-expressed lncRNA that positively regulates FOXF1. Additional LINC01081 disruption was associated with more severe disease in these two cases. (szafranski2014twodeletionsoverlapping pages 5-6)
* Familial disease and variable severity within families demonstrate that variant position, enhancer activity, parent of origin, mosaicism, and other modifiers influence expression. No clinically validated modifier-gene panel currently predicts severity.

### Environmental and demographic risks

No toxin, infection, maternal lifestyle, diet, occupation, sex, or postnatal exposure is established as a primary cause. A viral infection and high-altitude exposure preceded decompensation in one child with atypical, previously compensated disease; these are best regarded as physiological triggers that unmasked a congenital limitation, not causes of ACDMPV. (szafranski2014twodeletionsoverlapping pages 3-5)

There is no evidence that smoking, alcohol, nutrition, exercise, vaccination, or avoidance of pollution prevents FOXF1-related ACDMPV. No validated protective genetic allele exists. A 2024 preprint proposed that hyperfunctional enhancer variation may partially compensate for damaging FOXF1 alleles, but this remains investigational and is not a clinically established protective factor. (gomezarroyo2024roleofforkhead pages 11-13)

### Gene–environment interaction

A defensible model is that FOXF1 dosage establishes a fixed developmental deficit, while oxygen demand, infection, surgery, altitude, or withdrawal of pulmonary-circulation support can precipitate clinical decompensation in partially compensated disease. Evidence is limited to cases and does not establish a quantitative interaction. In two neonates, surgery and cessation of prostaglandin E1 were temporally associated with deterioration, but causality was not proved. (kozłowska2020genotype–phenotypecorrelationin pages 2-4)

---

## 3. Phenotypes

### Core pulmonary and cardiovascular phenotype

| Phenotype | Type, timing, severity/course | Frequency evidence | Suggested HPO term |
|---|---|---|---|
| Persistent pulmonary hypertension | Clinical sign; congenital/neonatal, severe and rapidly progressive | Defining clinical feature in typical cases | **Pulmonary hypertension, HP:0002092**; persistent pulmonary hypertension of the newborn where locally available |
| Hypoxemia/cyanosis | Laboratory abnormality/sign; usually hours to ≤48 h after birth | Typical; may follow a short asymptomatic interval | **Hypoxemia, HP:0012418**; **Cyanosis, HP:0000961** |
| Respiratory distress/failure | Symptom/sign; severe, refractory, progressive | Typical disease is nearly universal and often fatal | Respiratory distress; **Respiratory failure, HP:0002878** |
| Abnormal alveolar development | Histopathologic manifestation; congenital | Defining pathology | Abnormal pulmonary alveolar morphology; alveolar simplification |
| Capillary paucity/malposition | Histopathologic manifestation; congenital | Defining pathology | Decreased number of pulmonary capillaries; abnormal pulmonary capillary morphology |
| Misalignment of pulmonary veins | Histopathologic manifestation | Characteristic but may be focal in atypical disease | Misalignment of pulmonary veins |
| Small pulmonary-artery medial hypertrophy | Histopathologic/vascular sign | Characteristic | Pulmonary arterial medial hypertrophy |
| Intrapulmonary right-to-left shunting | Functional vascular abnormality | Demonstrated in vascular studies | Intrapulmonary shunt |

Histology comprises deficient lobular/alveolar development, widened septa with centrally located rather than apposed capillaries, reduced microvascular density, medial hypertrophy of small pulmonary arteries, and anomalous venous/systemic vessels within bronchovascular bundles. In the landmark molecular series, all **10/10** reviewed lungs showed characteristic abnormalities. Pulmonary lymphangiectasis occurred in **4/4 deletion cases** and **1/4 coding-variant cases** assessed, although these small denominators preclude firm genotype–phenotype conclusions. (stankiewicz2009genomicandgenic pages 6-8)

### Extrapulmonary manifestations

More than **80%** of patients in early compiled series had at least one additional malformation. Reported abnormalities include intestinal malrotation, omphalocele, congenital heart disease—including atrial or ventricular septal defects, coarctation/aortic-arch abnormalities and hypoplastic left heart—hydronephrosis and other genitourinary abnormalities, polyhydramnios, and hepatosplenomegaly. (kozłowska2020genotype–phenotypecorrelationin pages 2-4, stankiewicz2009genomicandgenic pages 1-2)

Suggested HPO terms include **Intestinal malrotation (HP:0002566)**, **Omphalocele (HP:0001539)**, **Hydronephrosis (HP:0000126)**, **Ventricular septal defect (HP:0001629)**, atrial septal defect, coarctation of the aorta, hypoplastic left heart, polyhydramnios, and hepatosplenomegaly. Frequencies for individual anomalies are not robustly established by modern population-based cohorts.

### Quality of life

No ACDMPV-specific EQ-5D, SF-36, PROMIS, or validated caregiver quality-of-life dataset was found. In typical disease, intensive ventilation, sedation, ECMO, and early death dominate morbidity. Atypical survivors have severe pulmonary-hypertension and oxygen/ventilatory burdens and may undergo prolonged hospitalization and transplantation. Thus, functional and family impact is profound, but quantitative patient-reported outcomes are unavailable.

---

## 4. Genetic and molecular information

### Causal gene

**FOXF1** encodes forkhead box F1, a DNA-binding transcription factor expressed in pulmonary endothelial and mesenchymal progenitors, fibroblasts, and pericytes during organogenesis. Its dosage coordinates pulmonary vascular development, mesenchymal–epithelial communication, and maturation of the alveolar gas-exchange unit. Suggested annotation: **HGNC:3815**; chromosome **16q24.1**; disease mechanism **haploinsufficiency/loss of function**. (guo2023singlecellmultiomics pages 1-2, guo2023singlecellmultiomics pages 13-15)

### Variant interpretation

Pathogenic and likely pathogenic variants include truncating and functionally damaging coding changes and deletions affecting FOXF1 or its enhancer. Classification should follow ACMG/AMP sequence-variant criteria and ACMG/ClinGen CNV standards, incorporating de novo status, absence from population databases, predicted loss of function, phenotype/pathology specificity, and functional/regulatory data. Individual variants must be checked in current ClinVar and gnomAD releases; no universal allele frequency can be assigned. Fully penetrant neonatal-lethal variants are expected to be absent or exceptionally rare in adult population databases.

The variants are generally **germline**, not cancer-associated somatic mutations. Low-level parental somatic/germline mosaicism is possible and relevant to recurrence, although strong ACDMPV-specific frequency estimates are lacking. A disease-nonspecific 2023 study of ten recurrent-de-novo-disorder families found paternal sperm mosaicism in **2/10**, at **2.88% and 2.5% variant allele fractions**, illustrating why deep parental testing may be useful after recurrent affected pregnancies but not establishing an ACDMPV frequency. (xu2023parentalmosaicismdetection pages 1-1, xu2023parentalmosaicismdetection pages 4-5)

### Regulatory and epigenetic architecture

Evidence supports **partial paternal imprinting** or parent-of-origin-biased FOXF1 regulation: many pathogenic enhancer deletions occur on the maternal chromosome, consistent with greater functional consequence when the more active allele is disrupted. This is not a simple binary imprinting system and should not be encoded as complete paternal silencing. The enhancer and LINC01081 contribute positively to FOXF1 expression. Two de novo maternal deletions produced strikingly different severity, suggesting that the exact regulatory segments removed influence residual dosage. (szafranski2014twodeletionsoverlapping pages 5-6)

No reproducible disease-specific genome-wide DNA-methylation, histone-mark, or chromatin biomarker has entered clinical practice. ATAC-seq evidence demonstrates altered cell-specific chromatin accessibility and FOXF1 regulatory networks, but it is mechanistic rather than diagnostic. (guo2023singlecellmultiomics pages 4-6, guo2023singlecellmultiomics pages 8-12)

### Chromosomal abnormalities

Relevant abnormalities include 16q24.1 microdeletions encompassing FOXF1, deletions limited to the upstream enhancer, larger deletions including neighboring FOX genes, and rare inversions or complex structural rearrangements that separate FOXF1 from regulatory elements. Routine karyotyping can miss these submicroscopic or balanced events; chromosomal microarray and, where needed, genome sequencing are more appropriate.

---

## 5. Environmental information

No environmental toxin, radiation exposure, pollutant, occupational agent, lifestyle behavior, or infectious organism is established as etiologic. ACDMPV is not communicable and has no zoonotic component. Infection, altitude, anesthesia, surgery, or altered pulmonary blood flow may expose limited cardiopulmonary reserve in atypical disease, but evidence is anecdotal. Consequently, CTD-style chemical–disease associations should not be encoded as causal without independent validation. (szafranski2014twodeletionsoverlapping pages 3-5, kozłowska2020genotype–phenotypecorrelationin pages 2-4)

---

## 6. Mechanism and pathophysiology

### Upstream-to-downstream causal chain

1. **Upstream genetic lesion:** heterozygous FOXF1 coding loss or disruption of the 16q24.1 enhancer/LINC01081 regulatory domain reduces FOXF1 dosage.
2. **Cell-autonomous developmental effects:** FOXF1-dependent transcription fails in KIT-positive CAP1 endothelial progenitors, CAP2 gas-exchange capillary cells, and pericytes, compromising differentiation, survival, migration, and vascular stabilization.
3. **Network disruption:** PTEN, ERK/MAPK, STAT3, focal-adhesion kinase, integrin, WNT/β-catenin, ID1, semaphorin, and Rho-GTPase programs are reduced or altered. Direct/predicted FOXF1 targets include **ACVRL1, AQP1, BCAM, CASZ1, CDH5, CPNE8, DAAM1, DLL4**, and capillary-selective **BTNL9**. (guo2023singlecellmultiomics pages 4-6, guo2023singlecellmultiomics pages 3-4, guo2023singlecellmultiomics pages 8-12)
4. **Microvascular phenotype:** CAP1/CAP2 cells become markedly depleted; pericytes are reduced, whereas COL15A1-positive systemic/bronchial endothelial cells expand. Abnormal VEGFA signaling shifts toward this systemic circulation.
5. **Epithelial–mesenchymal consequence:** loss of normal AT1-to-CAP2 VEGFA–VEGFR2 communication and altered fibroblast FGF signaling impair alveolar type 1-cell maturation. Transitional HOPX/SFTPC-coexpressing epithelial cells accumulate while mature AT1 cells decline.
6. **Tissue and physiological outcome:** simplified lobules, thick septa, sparse capillaries, arterial muscularization, anomalous bronchovascular vessels, right-to-left shunting, pulmonary hypertension, hypoxemia, and respiratory failure result. (guo2023singlecellmultiomics pages 4-6, guo2023singlecellmultiomics pages 13-15)

### 2023 single-cell multiomics advance

Guo et al. used single-nucleus RNA-seq, ATAC-seq, microscopy, and in-situ hybridization in six FOXF1-positive ACDMPV subjects. Across affected, preterm, and control tissues they identified **35 cell types**; the RNA dataset included **32,300 affected**, 15,817 preterm, and 17,692 control nuclei. FOXF1 RNA was absent in CAP1/CAP2 cells in **3/5 evaluable affected subjects**, and CAP2 loss tracked clinical severity. Pericytes had **61 downregulated genes**, and **58.8%** of predicted FOXF1 targets were supported in the integrated analysis. (guo2023singlecellmultiomics pages 4-6, guo2023singlecellmultiomics pages 3-4)

A direct abstract quotation captures the central result: “**Pathogenic variants involving the FOXF1 gene locus disrupt gene expression in EC progenitors, inhibiting differentiation or survival of CAP2 ECs and cell-cell interactions necessary for both pulmonary vasculogenesis and AT1 cell differentiation.**” The same abstract reports that microvascular loss was associated with “**increased VEGFA signalling and marked expansion of systemic bronchial ECs expressing COL15A1**.” Publication: September 2023; DOI URL: https://doi.org/10.1164/rccm.202210-2015oc. (guo2023singlecellmultiomics pages 1-2)

### Suggested ontology annotations

* **GO biological processes:** lung development; vasculogenesis; angiogenesis; endothelial-cell differentiation; blood-vessel morphogenesis; epithelial-cell differentiation; alveolar development; cell–cell signaling; VEGF-receptor signaling; canonical WNT signaling; MAPK cascade; integrin-mediated signaling.
* **Cell Ontology:** pulmonary capillary endothelial cell; endothelial progenitor cell; pericyte; pulmonary fibroblast; vascular smooth-muscle cell; alveolar type 1 epithelial cell; alveolar type 2 epithelial cell; bronchial endothelial cell.
* **GO cellular components:** nucleus/chromatin and transcription-regulator complex for FOXF1; cell–cell junction, focal adhesion, and plasma membrane for downstream endothelial defects.

### Immune, metabolic, and tissue-injury components

ACDMPV is not primarily autoimmune or inflammatory. Hypoxic vasoconstriction, high pulmonary vascular resistance, right-heart strain, and ischemic/hypoxemic injury are downstream. No validated disease-specific metabolic, metabolomic, lipidomic, or proteomic signature was found. Fibrosis is not the initiating mechanism, although prolonged atypical disease and vascular remodeling can produce secondary matrix changes.

### Advanced technology gaps

Single-cell transcriptomics and chromatin accessibility are established research tools. Disease-specific spatial transcriptomics, comprehensive proteomics, metabolomics, lipidomics, CRISPR screens, patient-iPSC assays, or validated organoid diagnostics were not identified in the retrieved evidence.

---

## 7. Anatomical structures affected

The primary organ is the **lung**, especially distal lung parenchyma, alveolar septa, pulmonary capillary plexus, small pulmonary arteries, pulmonary venous/systemic bronchial vessels, and bronchovascular bundles. Suggested UBERON mappings include lung, lung alveolus, alveolar septum, pulmonary capillary, pulmonary arteriole, pulmonary vein, bronchus, and bronchovascular bundle.

At tissue and cell level, endothelial, mesenchymal/connective, smooth-muscle, and alveolar epithelial compartments are affected. Secondary involvement includes the right ventricle and systemic organs injured by severe hypoxemia. Congenital gastrointestinal, cardiac, and genitourinary malformations are pleiotropic developmental manifestations rather than consequences of lung failure. Disease is bilateral and diffuse in typical cases; atypical disease may be patchy, creating biopsy sampling error. (guo2023singlecellmultiomics pages 2-3, stankiewicz2009genomicandgenic pages 6-8)

---

## 8. Temporal development

The anatomical lesion originates prenatally during pulmonary vascular and alveolar morphogenesis. Typical clinical onset is acute within hours or the first **48 hours**, sometimes after a brief apparently normal interval. It progresses rapidly from oxygen requirement and pulmonary hypertension to refractory hypoxemia, right-to-left shunting, multiorgan hypoxic injury, and death in days or weeks. (kozłowska2020genotype–phenotypecorrelationin pages 1-2, stankiewicz2009genomicandgenic pages 1-2)

Atypical disease can present after weeks, months, or rarely later childhood and may fluctuate with infections or physiological stress. In the 2023 research cohort, three severe subjects died or underwent tissue sampling at **2–5 weeks**, whereas less severe subjects reached transplant at **9 months and 3.5 years**. Another enhancer-deletion patient decompensated at 14 months and received bilateral transplantation at 15 months. (guo2023singlecellmultiomics pages 3-4, szafranski2014twodeletionsoverlapping pages 3-5)

There is no spontaneous anatomical remission. Temporary improvement with inhaled nitric oxide, prostaglandin, ventilation, or ECMO reflects altered vascular tone and support—not restoration of the missing capillary bed. The critical intervention window is therefore early recognition before prolonged futile ECMO or irreversible end-organ injury, while urgently assessing transplant suitability in unusually stable or patchy disease.

---

## 9. Inheritance and population characteristics

### Epidemiology

Reliable incidence and prevalence per 100,000 are unknown. Approximately **200 cases** had been reported by 2009, but underdiagnosis is probable because infants may be classified as idiopathic persistent pulmonary hypertension and because definitive pathology was historically obtained only at autopsy. A 2024 French chILD cohort exists, but no ACDMPV-specific national incidence could be extracted from the retrieved text. (stankiewicz2009genomicandgenic pages 1-2)

No ethnicity, geography, sex, consanguinity, or founder population is known to have a reproducibly increased risk. The age distribution is overwhelmingly neonatal, with rare infantile or childhood survivors.

### Inheritance

The molecular mechanism is **autosomal dominant**, usually caused by a **de novo heterozygous** pathogenic variant or deletion. Approximately **10% familial association** was reported in early literature, but this estimate is based on published cases and may be biased. Partial paternal imprinting/parent-of-origin effects complicate conventional Mendelian counseling. (stankiewicz2009genomicandgenic pages 1-2, szafranski2014twodeletionsoverlapping pages 5-6)

Penetrance is high for clearly loss-of-function variants but not adequately quantified; expressivity ranges from neonatal lethality to patchy, delayed disease. Anticipation and consanguinity are not established. Germline mosaicism is possible, so recurrence after an apparently de novo event is not zero. Testing both parents and considering deep mosaicism assays after recurrent pregnancies is appropriate. Carrier frequency cannot be reliably estimated because severe causal variants are individually ultra-rare and commonly de novo.

---

## 10. Diagnostics

### When to suspect ACDMPV

Suspect the disease in a term or near-term neonate with severe persistent pulmonary hypertension and hypoxemia that are disproportionate to radiographic parenchymal disease, respond only transiently to pulmonary vasodilators, and recur or worsen despite optimized ventilation and ECMO—especially when congenital gastrointestinal, cardiac, or genitourinary anomalies coexist. Atypical disease should be considered in unexplained infantile/childhood pulmonary hypertension with diffuse developmental lung abnormalities.

### Clinical evaluation

* **Echocardiography:** documents pulmonary hypertension, right-to-left ductal/atrial shunting, right-ventricular dysfunction, and associated heart defects, but is not specific.
* **Blood gases and oxygenation:** show severe hypoxemia and often acidosis; no disease-specific laboratory biomarker exists.
* **Chest radiograph/CT:** may show diffuse ground-glass opacity, septal/interstitial thickening, edema-like change, or developmental simplification. Imaging cannot reliably confirm or exclude ACDMPV.
* **Cardiac catheterization/angiography:** may characterize pulmonary vascular resistance and shunting but is not routinely required in unstable neonates.
* **Histopathology:** remains the diagnostic gold standard when molecular testing is negative, delayed, or ambiguous. Adequate tissue from more than one region is desirable because atypical lesions may be patchy. CD31 and CD34 endothelial immunostaining can clarify capillary distribution. (kozłowska2020genotype–phenotypecorrelationin pages 2-4, kozłowska2020genotype–phenotypecorrelationin pages 1-2)

### Molecular testing algorithm

1. Order rapid sequencing of **FOXF1**, including deletion/duplication analysis and coverage of the known distant enhancer/regulatory domain.
2. Use **chromosomal microarray** to detect 16q24.1 gene or enhancer CNVs and associated multigene deletions. In two neonates, array CGH identified approximately **1.45-Mb** and **0.7-Mb** deletions; the latter left FOXF1 intact and removed its enhancer. (kozłowska2020genotype–phenotypecorrelationin pages 2-4)
3. If negative and suspicion remains high, pursue trio genome sequencing, which is preferable to exome sequencing for noncoding deletions, inversions, breakpoints, and mosaicism. WES can detect coding variants but may miss the principal regulatory domain.
4. Analyze parental samples to establish de novo status and recurrence risk. Consider tissue-specific/deep testing when mosaicism is suspected.
5. Lung biopsy should not be delayed if the molecular result will not arrive rapidly enough to guide ECMO continuation or transplant decisions.

Karyotyping has low sensitivity for submicroscopic CNVs. FISH can test a known deletion but is not comprehensive. Mitochondrial DNA and repeat-expansion testing are not indicated unless a different diagnosis is suspected. RNA-seq/ATAC-seq remain research tools rather than validated clinical assays.

### Differential diagnosis

Major alternatives include idiopathic or secondary persistent pulmonary hypertension of the newborn; congenital diaphragmatic hernia and pulmonary hypoplasia; congenital heart disease; pulmonary veno-occlusive disease; pulmonary capillary hemangiomatosis; congenital pulmonary lymphangiectasia; acinar dysplasia; congenital alveolar dysplasia; surfactant dysfunction disorders involving **SFTPB, SFTPC, ABCA3**, or **NKX2-1**; TBX4-related developmental lung/PAH disease; infection; meconium aspiration; and severe parenchymal lung disease. Histology and comprehensive genetics distinguish these conditions. The 2024 developmental-lung-disease consensus emphasizes interdisciplinary review involving neonatology, pulmonary hypertension, radiology, pathology, genetics, intensive care, and transplantation. Publication: August 2024; DOI URL: https://doi.org/10.1183/13993003.00639-2024.

### Screening

ACDMPV is not included in routine newborn biochemical screening, and population screening is inappropriate given its rarity and lack of a simple validated marker. Targeted prenatal diagnosis, cascade testing, and preimplantation genetic testing are appropriate when a familial pathogenic variant or CNV is known.

---

## 11. Outcome and prognosis

Typical disease is almost universally fatal without transplantation, usually within the first month, although death from severe respiratory failure may occur over days to months. Mechanical support does not correct the developmental absence of an adequate gas-exchange microvasculature. The 2020 report states that both molecularly confirmed neonates died despite maximal ventilation, inhaled nitric oxide, inotropes, and surfactant. (kozłowska2020genotype–phenotypecorrelationin pages 1-2)

No meaningful 5- or 10-year survival estimate exists because typical neonatal mortality is so high and long-term survivors are exceptionally selected. Favorable prognostic features appear to include later onset, patchy histology, residual CAP2 capillary endothelium, partial vasodilator responsiveness, and absence of prohibitive extrapulmonary anomalies; these are not validated prognostic models. Severe diffuse capillary depletion and early refractory pulmonary hypertension predict poor survival. (guo2023singlecellmultiomics pages 3-4, guo2023singlecellmultiomics pages 4-6)

Long-term morbidity among transplanted survivors includes standard pediatric lung-transplant risks: rejection, infection, chronic lung-allograft dysfunction, medication toxicity, and neurodevelopmental effects of critical illness. Disease-specific quality-of-life and neurodevelopmental statistics are unavailable.

---

## 12. Treatment and current applications

### Supportive and pharmacological treatment

There is no approved disease-modifying drug. Mechanical ventilation, high inspired oxygen, inhaled nitric oxide, sildenafil or prostacyclin-pathway therapy, inotropes, correction of acidosis, surfactant when another neonatal indication exists, and prostaglandin E1 in selected ductal-dependent or right-heart unloading contexts can transiently improve physiology. They do not rebuild the capillary bed. Relevant NCIT concepts include **Mechanical Ventilation**, **Nitric Oxide Therapy**, **Vasodilator Therapy**, **Extracorporeal Membrane Oxygenation**, and **Supportive Care**. (kozłowska2020genotype–phenotypecorrelationin pages 2-4, kozłowska2020genotype–phenotypecorrelationin pages 1-2)

ECMO is generally a bridge to diagnosis, decision-making, or transplantation—not curative therapy. Continuing ECMO after confirmed diffuse typical ACDMPV without a transplant pathway is usually futile and requires careful multidisciplinary and family-centered discussion.

### Lung transplantation

Bilateral lung transplantation is the only currently implemented definitive replacement therapy and is feasible only for selected atypical or sufficiently stable infants/children. One child with an upstream enhancer deletion received an orthotopic bilateral transplant at **15 months**; the 2023 cohort included transplants at **9 months** and **3.5 years**. These cases prove feasibility but do not establish a response rate. Donor availability, body size, ECMO complications, neurological injury, and extrapulmonary malformations sharply limit access. NCIT: **Bilateral Lung Transplantation**. (szafranski2014twodeletionsoverlapping pages 3-5, guo2023singlecellmultiomics pages 2-3)

### Experimental therapy

Endothelial-targeted nanoparticle delivery of **FOXF1** or **STAT3** rescued pulmonary vasculogenesis in newborn mouse experiments cited by the 2023 human mechanistic study. Separate mouse work shows endothelial FOXF1 delivery can improve experimental pulmonary fibrosis, supporting targetability but not efficacy in congenital ACDMPV. No ACDMPV-specific human gene, RNA, cell, CRISPR, or pharmacologic interventional trial was identified in the ClinicalTrials.gov search. (guo2023singlecellmultiomics pages 13-15)

A rational future strategy would require prenatal or very early postnatal restoration of FOXF1 in the correct endothelial/mesenchymal progenitors, with careful dosage control because FOXF1 is a developmental transcription factor. This remains preclinical; no pharmacogenomic prescribing guideline exists.

---

## 13. Prevention

There is no lifestyle, environmental, vaccine, or drug-based primary prevention. For sporadic de novo disease, prevention is limited to reproductive genetics after the causal lesion is identified.

* **Primary/reproductive prevention:** genetic counseling, parental testing, preimplantation genetic testing for monogenic/CNV disease, and prenatal diagnosis by chorionic-villus sampling or amniocentesis.
* **Secondary prevention:** targeted fetal testing in known-risk pregnancies and rapid neonatal genetic diagnosis may prevent prolonged ineffective treatment and enable earlier transplant referral; they do not prevent lung maldevelopment after it has occurred.
* **Tertiary prevention:** meticulous oxygenation and hemodynamic support, prevention of ECMO/ventilator complications, and timely transplant evaluation may reduce secondary organ injury.

A 2023 reproductive-genetics study—not ACDMPV-specific—showed that deep sequencing and PGT can prevent transmission in families with recurrent de novo mutations and demonstrated a **>5,000×** assay with an approximately **0.5% VAF** detection limit. This supports methodology for counseling but should not be presented as an ACDMPV outcome study. (xu2023parentalmosaicismdetection pages 1-1)

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart, breed predisposition, or OMIA-defined ACDMPV syndrome was identified. Therefore, prevalence, veterinary importance, and VBO breed terms are unavailable. The disease is noninfectious, nontransmissible, and has no zoonotic potential.

FOXF1 developmental function is evolutionarily conserved across vertebrates. Mouse **Foxf1** is the principal comparative ortholog and has supplied most mechanistic evidence. Comparative interpretation must account for species differences in lung developmental timing and placentation.

---

## 15. Model organisms

### Engineered mouse models

Heterozygous, conditional, or cell-type-specific **Foxf1** loss models reproduce important components of human disease, including impaired pulmonary vasculogenesis, capillary deficiency, abnormal endothelial differentiation, alveolar developmental defects, pulmonary hypertension, and neonatal mortality. Mesodermal **Pten** inactivation can also produce an ACDMPV-like phenotype, supporting the relevance of PTEN/FOXF1-linked developmental signaling. (guo2023singlecellmultiomics pages 3-4, sen2013novelfoxf1mutations pages 10-13)

Applications include mapping FOXF1 transcriptional targets, lineage tracing of endothelial progenitors, testing endothelial–epithelial communication, and evaluating nanoparticle gene delivery. Strengths are experimental control and prenatal developmental access. Limitations include incomplete reproduction of human pulmonary-vein/systemic-vessel anatomy, species-specific developmental timing, and the fact that many human cases involve complex regulatory or multigene CNVs rather than simple coding knockout.

### Cellular and other models

Primary human ACDMPV lung tissue and single-nucleus multiomics currently provide the most disease-proximal cellular system. No mature, widely validated ACDMPV patient-iPSC, lung-organoid, zebrafish, rat, Drosophila, or *C. elegans* platform was established in the retrieved evidence. Relevant resources for future model registration include MGI, IMPC, KOMP, IMSR/MMRRC, ZFIN, and Cellosaurus.

---

## Key recent developments and expert interpretation

1. **Human cellular mechanism resolved, 2023:** single-cell RNA/ATAC analysis connected FOXF1 insufficiency to CAP1/CAP2 and pericyte loss, failed AT1 maturation, altered VEGFA communication, and compensatory COL15A1-positive bronchial endothelial expansion. This shifts the model from a nonspecific vascular malformation to a cell- and lineage-specific developmental network disorder. (guo2023singlecellmultiomics pages 1-2, guo2023singlecellmultiomics pages 4-6)
2. **Clinical framing updated, 2024:** expert consensus places FOXF1-ACDMPV among developmental lung diseases presenting with neonatal/infantile pulmonary hypertension and recommends interdisciplinary integration of genetics, imaging, pathology, biopsy decisions, ECMO, transplant assessment, and family counseling.
3. **Translational direction:** endothelial-targeted FOXF1/STAT3 replacement has preclinical plausibility, but irreversible prenatal developmental loss, narrow timing, delivery specificity, and transcription-factor dosage are major barriers. (guo2023singlecellmultiomics pages 13-15)
4. **Real-world implementation:** rapid FOXF1 sequencing plus CNV/enhancer analysis is increasingly capable of replacing postmortem-only diagnosis, while pathology remains essential for negative or ambiguous molecular cases. Selected atypical patients can survive through bilateral transplantation. (szafranski2014twodeletionsoverlapping pages 3-5, kozłowska2020genotype–phenotypecorrelationin pages 2-4)

## Evidence gaps requiring explicit knowledge-base flags

No reliable population incidence/prevalence, sex ratio, ethnicity effect, carrier frequency, prospective natural-history registry, validated severity biomarker, quality-of-life instrument, standardized treatment algorithm, disease-specific interventional trial, human gene-therapy result, or established environmental/protective factor was identified. Variant-level ClinVar classification and gnomAD frequency should be imported dynamically rather than generalized. Proteomics, metabolomics, lipidomics, spatial transcriptomics, natural animal disease, and robust patient-derived organoid/iPSC findings remain absent or insufficiently established.

## Selected primary references and publication details

* **Guo M, et al.** *Single Cell Multiomics Identifies Cells and Genetic Networks Underlying Alveolar Capillary Dysplasia.* **American Journal of Respiratory and Critical Care Medicine. September 2023;208:709–725.** https://doi.org/10.1164/rccm.202210-2015oc. Human lung single-nucleus RNA/ATAC study, six subjects. (guo2023singlecellmultiomics pages 3-4, guo2023singlecellmultiomics pages 1-2)
* **Stankiewicz P, et al.** *Genomic and Genic Deletions of the FOX Gene Cluster on 16q24.1 and Inactivating Mutations of FOXF1 Cause Alveolar Capillary Dysplasia and Other Malformations.* **American Journal of Human Genetics. June 2009;84:780–791.** DOI: https://doi.org/10.1016/j.ajhg.2009.05.005; **PMID 19500772**. Landmark human genetic/pathology study. (stankiewicz2009genomicandgenic pages 6-8, stankiewicz2009genomicandgenic pages 1-2)
* **Sen P, et al.** *Novel FOXF1 mutations in sporadic and familial cases of alveolar capillary dysplasia with misaligned pulmonary veins imply a role for its DNA binding domain.* **Human Mutation. June 2013;34:801–811.** https://doi.org/10.1002/humu.22313. Human genetics cohort. (sen2013novelfoxf1mutations pages 10-13)
* **Szafranski P, et al.** *Two deletions overlapping a distant FOXF1 enhancer unravel the role of lncRNA LINC01081 in etiology of ACDMPV.* **American Journal of Medical Genetics Part A. August 2014;164:2013–2019.** https://doi.org/10.1002/ajmg.a.36606. Human regulatory genetics and transplant cases. (szafranski2014twodeletionsoverlapping pages 3-5, szafranski2014twodeletionsoverlapping pages 5-6)
* **Kozłowska Z, et al.** *Genotype–phenotype correlation in two Polish neonates with alveolar capillary dysplasia.* **BMC Pediatrics. June 2020;20.** https://doi.org/10.1186/s12887-020-02200-y. Human clinical, pathology, and CNV report. Its abstract states: “**The diagnosis of ACD is based on histopathological evaluation of lung biopsy or autopsy tissue or genetic testing of FOXF1 on chromosome 16q24.1.**” (kozłowska2020genotype–phenotypecorrelationin pages 2-4, kozłowska2020genotype–phenotypecorrelationin pages 1-2)
* **Varghese NP, et al.** *An interdisciplinary consensus approach to pulmonary hypertension in developmental lung disease.* **European Respiratory Journal. August 2024;64:2400639.** https://doi.org/10.1183/13993003.00639-2024. Expert consensus, not an ACDMPV treatment trial.

Overall, the strongest current interpretation is that ACDMPV is a FOXF1-dosage-sensitive, predominantly de novo developmental vasculopathy in which failure to establish the alveolar capillary endothelial–pericyte network secondarily prevents normal alveolar epithelial maturation. Rapid combined coding, CNV, and regulatory-region testing—integrated with expert pathology—offers the best diagnostic approach, while bilateral lung transplantation remains the only implemented definitive therapy for the rare patient who can be stabilized long enough to receive it.

References

1. (guo2023singlecellmultiomics pages 2-3): Minzhe Guo, Kathryn A. Wikenheiser-Brokamp, Joseph A. Kitzmiller, Cheng Jiang, Guolun Wang, Allen Wang, Sebastian Preissl, Xiaomeng Hou, Justin Buchanan, Justyna A. Karolak, Yifei Miao, David B. Frank, William J. Zacharias, Xin Sun, Yan Xu, Mingxia Gu, Pawel Stankiewicz, Vladimir V. Kalinichenko, Jennifer A. Wambach, and Jeffrey A. Whitsett. Single cell multiomics identifies cells and genetic networks underlying alveolar capillary dysplasia. American Journal of Respiratory and Critical Care Medicine, 208:709-725, Sep 2023. URL: https://doi.org/10.1164/rccm.202210-2015oc, doi:10.1164/rccm.202210-2015oc. This article has 37 citations and is from a highest quality peer-reviewed journal.

2. (guo2023singlecellmultiomics pages 1-2): Minzhe Guo, Kathryn A. Wikenheiser-Brokamp, Joseph A. Kitzmiller, Cheng Jiang, Guolun Wang, Allen Wang, Sebastian Preissl, Xiaomeng Hou, Justin Buchanan, Justyna A. Karolak, Yifei Miao, David B. Frank, William J. Zacharias, Xin Sun, Yan Xu, Mingxia Gu, Pawel Stankiewicz, Vladimir V. Kalinichenko, Jennifer A. Wambach, and Jeffrey A. Whitsett. Single cell multiomics identifies cells and genetic networks underlying alveolar capillary dysplasia. American Journal of Respiratory and Critical Care Medicine, 208:709-725, Sep 2023. URL: https://doi.org/10.1164/rccm.202210-2015oc, doi:10.1164/rccm.202210-2015oc. This article has 37 citations and is from a highest quality peer-reviewed journal.

3. (guo2023singlecellmultiomics pages 4-6): Minzhe Guo, Kathryn A. Wikenheiser-Brokamp, Joseph A. Kitzmiller, Cheng Jiang, Guolun Wang, Allen Wang, Sebastian Preissl, Xiaomeng Hou, Justin Buchanan, Justyna A. Karolak, Yifei Miao, David B. Frank, William J. Zacharias, Xin Sun, Yan Xu, Mingxia Gu, Pawel Stankiewicz, Vladimir V. Kalinichenko, Jennifer A. Wambach, and Jeffrey A. Whitsett. Single cell multiomics identifies cells and genetic networks underlying alveolar capillary dysplasia. American Journal of Respiratory and Critical Care Medicine, 208:709-725, Sep 2023. URL: https://doi.org/10.1164/rccm.202210-2015oc, doi:10.1164/rccm.202210-2015oc. This article has 37 citations and is from a highest quality peer-reviewed journal.

4. (stankiewicz2009genomicandgenic pages 1-2): Paweł Stankiewicz, Partha Sen, Samarth S. Bhatt, Mekayla Storer, Zhilian Xia, Bassem A. Bejjani, Zhishuo Ou, Joanna Wiszniewska, Daniel J. Driscoll, Juan Bolivar, Mislen Bauer, Elaine H. Zackai, Donna McDonald-McGinn, Małgorzata M.J. Nowaczyk, Mitzi Murray, Tamim H. Shaikh, Vicki Martin, Matthew Tyreman, Ingrid Simonic, Lionel Willatt, Joan Paterson, Sarju Mehta, Diana Rajan, Tomas Fitzgerald, Susan Gribble, Elena Prigmore, Ankita Patel, Lisa G. Shaffer, Nigel P. Carter, Sau Wai Cheung, Claire Langston, and Charles Shaw-Smith. Genomic and genic deletions of the fox gene cluster on 16q24.1 and inactivating mutations of foxf1 cause alveolar capillary dysplasia and other malformations. American Journal of Human Genetics, 84:780-791, Jun 2009. URL: https://doi.org/10.1016/j.ajhg.2009.05.005, doi:10.1016/j.ajhg.2009.05.005. This article has 489 citations and is from a highest quality peer-reviewed journal.

5. (stankiewicz2009genomicandgenic pages 6-8): Paweł Stankiewicz, Partha Sen, Samarth S. Bhatt, Mekayla Storer, Zhilian Xia, Bassem A. Bejjani, Zhishuo Ou, Joanna Wiszniewska, Daniel J. Driscoll, Juan Bolivar, Mislen Bauer, Elaine H. Zackai, Donna McDonald-McGinn, Małgorzata M.J. Nowaczyk, Mitzi Murray, Tamim H. Shaikh, Vicki Martin, Matthew Tyreman, Ingrid Simonic, Lionel Willatt, Joan Paterson, Sarju Mehta, Diana Rajan, Tomas Fitzgerald, Susan Gribble, Elena Prigmore, Ankita Patel, Lisa G. Shaffer, Nigel P. Carter, Sau Wai Cheung, Claire Langston, and Charles Shaw-Smith. Genomic and genic deletions of the fox gene cluster on 16q24.1 and inactivating mutations of foxf1 cause alveolar capillary dysplasia and other malformations. American Journal of Human Genetics, 84:780-791, Jun 2009. URL: https://doi.org/10.1016/j.ajhg.2009.05.005, doi:10.1016/j.ajhg.2009.05.005. This article has 489 citations and is from a highest quality peer-reviewed journal.

6. (kozłowska2020genotype–phenotypecorrelationin pages 1-2): Zuzanna Kozłowska, Zuzanna Owsiańska, Joanna P. Wroblewska, Apolonia Kałużna, Andrzej Marszałek, Yogen Singh, Bartłomiej Mroziński, Qian Liu, Justyna A. Karolak, Paweł Stankiewicz, Gail Deutsch, Marta Szymankiewicz-Bręborowicz, and Tomasz Szczapa. Genotype–phenotype correlation in two polish neonates with alveolar capillary dysplasia. BMC Pediatrics, Jun 2020. URL: https://doi.org/10.1186/s12887-020-02200-y, doi:10.1186/s12887-020-02200-y. This article has 8 citations and is from a peer-reviewed journal.

7. (sen2013novelfoxf1mutations pages 10-13): Partha Sen, Yaping Yang, Colby Navarro, Iris Silva, Przemyslaw Szafranski, Katarzyna E. Kolodziejska, Avinash V. Dharmadhikari, Hasnaa Mostafa, Harry Kozakewich, Debra Kearney, John B. Cahill, Merrissa Whitt, Masha Bilic, Linda Margraf, Adrian Charles, Jack Goldblatt, Kathleen Gibson, Patrick E. Lantz, A. Julian Garvin, John Petty, Zeina Kiblawi, Craig Zuppan, Allyn McConkie-Rosell, Marie T. McDonald, Stacey L. Peterson-Carmichael, Jane T. Gaede, Binoy Shivanna, Deborah Schady, Philippe S. Friedlich, Stephen R. Hays, Irene Valenzuela Palafoll, Ulrike Siebers-Renelt, Axel Bohring, Laura S. Finn, Joseph R. Siebert, Csaba Galambos, Lananh Nguyen, Melissa Riley, Nicolas Chassaing, Adeline Vigouroux, Gustavo Rocha, Susana Fernandes, Jane Brumbaugh, Kari Roberts, Luk Ho-ming, Ivan F. M. Lo, Stephen Lam, Romana Gerychova, Marta Jezova, Iveta Valaskova, Florence Fellmann, Katayoun Afshar, Eric Giannoni, Vincent Muhlethaler, Jinlong Liang, Jacques S. Beckmann, Janet Lioy, Hitesh Deshmukh, Lakshmi Srinivasan, Daniel T. Swarr, Melissa Sloman, Charles Shaw-Smith, Rosa Laura van Loon, Cecilia Hagman, Yves Sznajer, Catherine Barrea, Christine Galant, Thierry Detaille, Jennifer A. Wambach, F. Sessions Cole, Aaron Hamvas, Lawrence S. Prince, Karin E.M. Diderich, Alice S. Brooks, Robert M. Verdijk, Hari Ravindranathan, Ella Sugo, David Mowat, Michael L. Baker, Claire Langston, Stephen Welty, and Pawel Stankiewicz. Novel foxf1 mutations in sporadic and familial cases of alveolar capillary dysplasia with misaligned pulmonary veins imply a role for its dna binding domain. Human Mutation, 34:801-811, Jun 2013. URL: https://doi.org/10.1002/humu.22313, doi:10.1002/humu.22313. This article has 96 citations and is from a domain leading peer-reviewed journal.

8. (szafranski2014twodeletionsoverlapping pages 3-5): Przemyslaw Szafranski, Avinash V. Dharmadhikari, Jennifer A. Wambach, Chris T. Towe, Frances V. White, R. Mark Grady, Pirooz Eghtesady, F. Sessions Cole, Gail Deutsch, Partha Sen, and Paweł Stankiewicz. Two deletions overlapping a distant foxf1 enhancer unravel the role of lncrna linc01081 in etiology of alveolar capillary dysplasia with misalignment of pulmonary veins. American Journal of Medical Genetics Part A, 164:2013-2019, Aug 2014. URL: https://doi.org/10.1002/ajmg.a.36606, doi:10.1002/ajmg.a.36606. This article has 58 citations.

9. (szafranski2014twodeletionsoverlapping pages 5-6): Przemyslaw Szafranski, Avinash V. Dharmadhikari, Jennifer A. Wambach, Chris T. Towe, Frances V. White, R. Mark Grady, Pirooz Eghtesady, F. Sessions Cole, Gail Deutsch, Partha Sen, and Paweł Stankiewicz. Two deletions overlapping a distant foxf1 enhancer unravel the role of lncrna linc01081 in etiology of alveolar capillary dysplasia with misalignment of pulmonary veins. American Journal of Medical Genetics Part A, 164:2013-2019, Aug 2014. URL: https://doi.org/10.1002/ajmg.a.36606, doi:10.1002/ajmg.a.36606. This article has 58 citations.

10. (kozłowska2020genotype–phenotypecorrelationin pages 2-4): Zuzanna Kozłowska, Zuzanna Owsiańska, Joanna P. Wroblewska, Apolonia Kałużna, Andrzej Marszałek, Yogen Singh, Bartłomiej Mroziński, Qian Liu, Justyna A. Karolak, Paweł Stankiewicz, Gail Deutsch, Marta Szymankiewicz-Bręborowicz, and Tomasz Szczapa. Genotype–phenotype correlation in two polish neonates with alveolar capillary dysplasia. BMC Pediatrics, Jun 2020. URL: https://doi.org/10.1186/s12887-020-02200-y, doi:10.1186/s12887-020-02200-y. This article has 8 citations and is from a peer-reviewed journal.

11. (guo2023singlecellmultiomics pages 13-15): Minzhe Guo, Kathryn A. Wikenheiser-Brokamp, Joseph A. Kitzmiller, Cheng Jiang, Guolun Wang, Allen Wang, Sebastian Preissl, Xiaomeng Hou, Justin Buchanan, Justyna A. Karolak, Yifei Miao, David B. Frank, William J. Zacharias, Xin Sun, Yan Xu, Mingxia Gu, Pawel Stankiewicz, Vladimir V. Kalinichenko, Jennifer A. Wambach, and Jeffrey A. Whitsett. Single cell multiomics identifies cells and genetic networks underlying alveolar capillary dysplasia. American Journal of Respiratory and Critical Care Medicine, 208:709-725, Sep 2023. URL: https://doi.org/10.1164/rccm.202210-2015oc, doi:10.1164/rccm.202210-2015oc. This article has 37 citations and is from a highest quality peer-reviewed journal.

12. (guo2023singlecellmultiomics pages 3-4): Minzhe Guo, Kathryn A. Wikenheiser-Brokamp, Joseph A. Kitzmiller, Cheng Jiang, Guolun Wang, Allen Wang, Sebastian Preissl, Xiaomeng Hou, Justin Buchanan, Justyna A. Karolak, Yifei Miao, David B. Frank, William J. Zacharias, Xin Sun, Yan Xu, Mingxia Gu, Pawel Stankiewicz, Vladimir V. Kalinichenko, Jennifer A. Wambach, and Jeffrey A. Whitsett. Single cell multiomics identifies cells and genetic networks underlying alveolar capillary dysplasia. American Journal of Respiratory and Critical Care Medicine, 208:709-725, Sep 2023. URL: https://doi.org/10.1164/rccm.202210-2015oc, doi:10.1164/rccm.202210-2015oc. This article has 37 citations and is from a highest quality peer-reviewed journal.

13. (guo2023singlecellmultiomics pages 8-12): Minzhe Guo, Kathryn A. Wikenheiser-Brokamp, Joseph A. Kitzmiller, Cheng Jiang, Guolun Wang, Allen Wang, Sebastian Preissl, Xiaomeng Hou, Justin Buchanan, Justyna A. Karolak, Yifei Miao, David B. Frank, William J. Zacharias, Xin Sun, Yan Xu, Mingxia Gu, Pawel Stankiewicz, Vladimir V. Kalinichenko, Jennifer A. Wambach, and Jeffrey A. Whitsett. Single cell multiomics identifies cells and genetic networks underlying alveolar capillary dysplasia. American Journal of Respiratory and Critical Care Medicine, 208:709-725, Sep 2023. URL: https://doi.org/10.1164/rccm.202210-2015oc, doi:10.1164/rccm.202210-2015oc. This article has 37 citations and is from a highest quality peer-reviewed journal.

14. (xu2023parentalmosaicismdetection pages 1-1): Naixin Xu, Weihui Shi, Xianling Cao, Xuanyou Zhou, Li Jin, He-Feng Huang, Songchang Chen, and Chenming Xu. Parental mosaicism detection and preimplantation genetic testing in families with multiple transmissions of de novo mutations. Journal of Medical Genetics, 60:910-917, Jan 2023. URL: https://doi.org/10.1136/jmg-2022-108920, doi:10.1136/jmg-2022-108920. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (xu2023parentalmosaicismdetection pages 6-6): Naixin Xu, Weihui Shi, Xianling Cao, Xuanyou Zhou, Li Jin, He-Feng Huang, Songchang Chen, and Chenming Xu. Parental mosaicism detection and preimplantation genetic testing in families with multiple transmissions of de novo mutations. Journal of Medical Genetics, 60:910-917, Jan 2023. URL: https://doi.org/10.1136/jmg-2022-108920, doi:10.1136/jmg-2022-108920. This article has 11 citations and is from a domain leading peer-reviewed journal.

16. (xu2023parentalmosaicismdetection pages 4-5): Naixin Xu, Weihui Shi, Xianling Cao, Xuanyou Zhou, Li Jin, He-Feng Huang, Songchang Chen, and Chenming Xu. Parental mosaicism detection and preimplantation genetic testing in families with multiple transmissions of de novo mutations. Journal of Medical Genetics, 60:910-917, Jan 2023. URL: https://doi.org/10.1136/jmg-2022-108920, doi:10.1136/jmg-2022-108920. This article has 11 citations and is from a domain leading peer-reviewed journal.

17. (kozłowska2020genotype–phenotypecorrelationin pages 7-7): Zuzanna Kozłowska, Zuzanna Owsiańska, Joanna P. Wroblewska, Apolonia Kałużna, Andrzej Marszałek, Yogen Singh, Bartłomiej Mroziński, Qian Liu, Justyna A. Karolak, Paweł Stankiewicz, Gail Deutsch, Marta Szymankiewicz-Bręborowicz, and Tomasz Szczapa. Genotype–phenotype correlation in two polish neonates with alveolar capillary dysplasia. BMC Pediatrics, Jun 2020. URL: https://doi.org/10.1186/s12887-020-02200-y, doi:10.1186/s12887-020-02200-y. This article has 8 citations and is from a peer-reviewed journal.

18. (gomezarroyo2024roleofforkhead pages 11-13): Jose Gomez-Arroyo, Arjan C. Houweling, Harm Jan Bogaard, Jurjan Aman, Joseph A. Kitzmiller, Aleksey Porollo, Dennis Dooijes, Lilian J. Meijboom, Phillip Hale, Michael W. Pauciulo, Jason Hong, Na Zhu, Carrie Welch, Yufeng Shen, William J. Zacharias, Francis X. McCormack, Micheala A. Aldred, Matthew T. Weirauch, Stefan Graf, Christopher Rhodes, Wendy K. Chung, Jeffrey A. Whitsett, Lisa J. Martin, Vladimir V. Kalinichenko, and William C. Nichols. Role of forkhead box f1 in the pathobiology of pulmonary arterial hypertension. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.18.611448, doi:10.1101/2024.09.18.611448. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](Alveolar_Capillary_Dysplasia_with_Misalignment_of_Pulmonary_Veins-deep-research-falcon_artifacts/artifact-00.md)