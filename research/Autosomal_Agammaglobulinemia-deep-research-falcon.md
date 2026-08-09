---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T08:33:46.466918'
end_time: '2026-08-01T08:42:59.285558'
duration_seconds: 552.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Agammaglobulinemia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Agammaglobulinemia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Agammaglobulinemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Agammaglobulinemia** covering all of the
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
- **Disease Name:** Autosomal Agammaglobulinemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Agammaglobulinemia** covering all of the
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


# Autosomal Agammaglobulinemia: Disease-Characteristics Research Report

## Executive summary and scope

**Autosomal agammaglobulinemia is not one monogenic disease but a heterogeneous group of inherited disorders in which early B-cell development fails because of an autosomal defect.** The defining laboratory pattern is profound reduction or absence of circulating B cells, markedly reduced immunoglobulins, and preserved T-cell numbers/function in the classic forms. It phenocopies X-linked agammaglobulinemia (XLA) but lacks a causal **BTK** variant. Autosomal recessive (AR) disease predominates; uncommon autosomal dominant (AD) syndromes involve genes such as **TCF3** and **TOP2B**. XLA accounts for approximately 85% of congenital agammaglobulinemia, leaving autosomal and genetically unresolved forms as a small minority. AR forms generally present younger and more severely than XLA. (benali2020geneticapproachesfor pages 1-2, mina2021molecularrequirementsfor pages 4-5, cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5)

The strongest recent synthesis is Tangye et al., *Journal of Experimental Medicine*, published June 2023, DOI [10.1084/jem.20221105](https://doi.org/10.1084/jem.20221105). Its abstract states: **“The fundamental importance of the role of human B cells in host defense against infectious diseases has been established by the discovery of inborn errors of immunity that disrupt B cell development, differentiation, or function.”** (tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3)

**Evidence boundary.** Autosomal disease is exceptionally rare, and most treatment, outcome, quality-of-life, and infection-management evidence is extrapolated from combined agammaglobulinemia or primary-antibody-deficiency cohorts dominated by XLA. Subtype-specific claims below are identified where possible. PMID values were not exposed in the retrieved full-text metadata; DOI URLs are therefore supplied rather than inventing PMID identifiers.

---

## 1. Disease information

### Definition and classification

Autosomal agammaglobulinemia is an **inborn error of immunity/predominantly antibody deficiency** caused by germline variants that interrupt B-cell lineage development, usually at the pro-B–to–pre-B transition. The operational phenotype is:

- severe hypogammaglobulinemia or agammaglobulinemia;
- absent or profoundly reduced peripheral CD19+/CD20+ B cells, commonly below 0.5–2% of lymphocytes;
- recurrent, severe, or unusual bacterial infections, usually beginning in infancy after maternally transferred IgG wanes;
- no pathogenic **BTK** variant;
- usually normal T-cell counts in isolated pre-BCR-pathway defects. (benali2020geneticapproachesfor pages 1-2, benali2020geneticapproachesfor pages 4-6)

### Identifiers and synonyms

- **Preferred label:** autosomal agammaglobulinemia.
- **Common synonyms:** autosomal recessive agammaglobulinemia; non-X-linked agammaglobulinemia; congenital autosomal agammaglobulinemia; agammaglobulinemia due to a specified gene defect; autosomal B-cell deficiency.
- **ICD-10-CM:** **D80.0, hereditary hypogammaglobulinemia**, is the closest umbrella code; coding should preserve the molecular subtype in accompanying text.
- **ICD-11:** classified under predominantly antibody deficiencies/inborn errors of immunity; a subtype-specific code should be verified in the local release.
- **MeSH:** *Agammaglobulinemia*.
- **MONDO/OMIM/Orphanet:** individual molecular forms have separate entries; the retrieved evidence did not verify a single authoritative MONDO or Orphanet identifier covering every autosomal form. A knowledge base should therefore model “autosomal agammaglobulinemia” as an umbrella concept linked to gene-defined child diseases, rather than assign an unverified single identifier.

The evidence is primarily **aggregated disease-level literature**, reviews, and small molecular cohorts—not individual EHR records. The most informative primary cohort comprised six affected people from four consanguineous North-African families. (benali2020geneticapproachesfor pages 1-2)

---

## 2. Etiology, risks, protective factors, and gene–environment relationships

### Causal factors

The primary cause is a **germline genetic defect** affecting one of four functional modules:

1. **Pre-B-cell receptor assembly:** **IGHM, IGLL1, CD79A, CD79B**.
2. **Pre-BCR/BCR signal transduction:** **BLNK, PIK3R1**, and in some classifications **PIK3CD**.
3. **Transcription, DNA topology, or ionic homeostasis:** **TCF3, TOP2B, SLC39A7**.
4. **Cellular metabolic control:** **FNIP1**, involving AMPK–mTOR homeostasis. (mina2021molecularrequirementsfor pages 4-5, tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3, tangye2023inbornerrorsof pages 6-7)

A 2020 human study found homozygous **IGHM** frameshifts p.Val378Alafs*1 and p.Ile184Serfs*21 in three patients and homozygous **CD79A** p.Trp66* in two sisters. All had undetectable or very low immunoglobulins, B cells below 0.5%, and normal T-cell counts. A sixth agammaglobulinemic patient had homozygous **RAG2** p.Glu407*, illustrating that a broader combined-immunodeficiency differential may mimic the phenotype. (benali2020geneticapproachesfor pages 1-2, benali2020geneticapproachesfor pages 4-6)

### Risk factors

- **Family history and consanguinity:** the major ascertainable risks for AR disease. The North-African cohort explicitly arose from consanguineous families. (benali2020geneticapproachesfor pages 1-2)
- **Sex:** unlike XLA, autosomal disease affects all sexes. A female infant or child with absent B cells particularly warrants evaluation for an autosomal defect.
- **De novo dominant variation:** relevant to AD **TCF3** or **TOP2B** disease.
- **Age:** age does not cause disease, but clinical infection susceptibility rises as maternal IgG falls during infancy.

### Protective factors

No validated protective allele, diet, lifestyle, or environmental exposure prevents the underlying developmental defect. Clinically protective measures include early diagnosis, immunoglobulin replacement, rapid antimicrobial treatment, selected prophylactic antibiotics, respiratory surveillance, and avoidance of live vaccines. (benali2020geneticapproachesfor pages 1-2, cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10)

### Gene–environment interaction

The genotype establishes profound humoral immune failure; environmental exposure determines which infections occur and how much secondary organ damage accumulates. Repeated airway infections cause a feed-forward cycle of epithelial injury, impaired mucociliary clearance, bronchiectasis, and further infection. There is no evidence that toxins, smoking, diet, pollution, or occupational exposure initiates the Mendelian disease, although smoke and respiratory pollutants plausibly worsen acquired lung damage. Infectious agents are complications, not causes.

---

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Profoundly reduced/absent B cells | Laboratory abnormality; congenital, persistent; B cells often <0.5–2% of lymphocytes | **HP:0005363**, Abnormality of B-cell physiology; use the current HPO child term for decreased circulating B cells |
| Agammaglobulinemia/hypogammaglobulinemia | Laboratory abnormality; severe and lifelong without immune reconstitution | **HP:0004432**, Agammaglobulinemia; **HP:0004313**, Hypogammaglobulinemia |
| Recurrent respiratory infection | Symptom/sign; usually begins in infancy or early childhood; episodic but recurrent | **HP:0002205**, Recurrent respiratory infections |
| Recurrent bacterial infection | Clinical manifestation; often encapsulated organisms; severity variable to life-threatening sepsis | **HP:0002718**, Recurrent bacterial infections |
| Otitis media/sinusitis/pneumonia | Clinical signs; recurrent; downstream bronchiectasis risk | **HP:0000403**, Recurrent otitis media; **HP:0011108**, Recurrent sinusitis; **HP:0006532**, Recurrent pneumonia |
| Gastrointestinal infection/diarrhea | Episodic or chronic, especially with enteric pathogens | **HP:0002028**, Chronic diarrhea; **HP:0004387**, Enteric infection |
| Enteroviral infection | Potentially severe or chronic; neurologic disease is a feared complication of agammaglobulinemia | **HP:0031693**, Recurrent viral infections; add organism-specific annotation |
| Sepsis | Acute, potentially fatal; *Pseudomonas* sepsis particularly reported in μ-heavy-chain deficiency | **HP:0100806**, Sepsis |
| Neutropenia | Laboratory abnormality; sometimes an early presenting feature; approximately 30% in reported **IGHM** deficiency and notable in **PIK3R1** disease; may improve with treatment/time | **HP:0001875**, Neutropenia |
| Small/absent tonsils and lymph nodes | Physical sign reflecting absent mature B-cell follicles; not universally documented in autosomal-only cohorts | **HP:0030245**, Tonsillar hypoplasia, if confirmed |
| Bronchiectasis/chronic lung disease | Acquired complication; progressive if infections are not controlled | **HP:0002110**, Bronchiectasis |
| Syndromic malformations | **TOP2B/Hoffman syndrome:** facial dysmorphism, limb and urogenital anomalies; variable | **HP:0001999**, Abnormal facial shape; phenotype-specific limb/urogenital terms |

Children with **IGHM** deficiency presented at a reported mean of **11 months**, compared with 35 months in BTK-related XLA, and had severe infections including enteroviral disease and *Pseudomonas* sepsis. Approximately 30% developed neutropenia. (cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5)

Quality of life is impaired by infection burden, chronic airway disease, school/work disruption, repeated infusions, venous access, and anxiety about infection. However, no validated EQ-5D, SF-36, or PROMIS estimates specific to autosomal agammaglobulinemia were identified.

---

## 4. Genetic and molecular information

The principal molecular subtypes are summarized below.

| Gene/pathway | Inheritance | Developmental block / mechanism | Human phenotype or quantitative evidence | Representative variant / evidence |
|---|---|---|---|---|
| **Autosomal agammaglobulinemia (umbrella term)** | Mostly autosomal recessive; rarer autosomal dominant forms reported | Heterogeneous early B-cell developmental disorders; often a phenocopy of X-linked agammaglobulinemia, usually involving pre-BCR/BCR components or downstream signaling | Review evidence indicates XLA accounts for ~85% of congenital agammaglobulinemia, with non-BTK autosomal forms comprising the remainder; AR forms typically present younger and more severely than XLA (cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5, cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10, tangye2023inbornerrorsof pages 2-3) | Classification caveat: this is an umbrella category rather than a single monogenic disease entity (benali2020geneticapproachesfor pages 1-2, cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5) |
| **IGHM (μ heavy chain / pre-BCR)** | Autosomal recessive | Early block at the pro-B to pre-B transition due to absent/defective μ heavy chain in the pre-BCR (mina2021molecularrequirementsfor pages 4-5, tangye2023inbornerrorsof pages 2-3) | Mean age at presentation reported as **11 months** versus **35 months** for BTK/XLA; μ heavy-chain deficiency accounts for about **5%** of agammaglobulinemia cases; ~**30%** of affected patients develop neutropenia; severe infections including enteroviral infection and *Pseudomonas* sepsis emphasized (cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5) | Human cohort: novel homozygous frameshifts **p.Val378Alafs*1** and **p.Ile184Serfs*21** in 3 patients; absent/severely reduced B cells **<0.5%** with very low/undetectable immunoglobulins (benali2020geneticapproachesfor pages 1-2, benali2020geneticapproachesfor pages 4-6) |
| **IGLL1 (λ5 surrogate light chain / pre-BCR)** | Autosomal recessive | Pre-BCR assembly defect causing block at the pro-B to pre-B transition (mina2021molecularrequirementsfor pages 4-5, tangye2023inbornerrorsof pages 2-3) | Patients with **CD79A, CD79B, IGLL1, or BLNK** defects are described as clinically indistinguishable from BTK deficiency in major features (mina2021molecularrequirementsfor pages 4-5) | Identified by review evidence as a recurrent AR cause of agammaglobulinemia/B-cell deficiency; no quantitative patient numbers in available context (cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5, cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) |
| **CD79A (Igα / pre-BCR signaling)** | Autosomal recessive | Complete block in B-cell development from defective Igα-mediated pre-BCR signaling (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) | In a human cohort, 2 sisters had undetectable/very low immunoglobulins, absent or severely reduced B cells **<0.5%**, and normal T-cell counts (benali2020geneticapproachesfor pages 4-6) | Novel homozygous nonsense variant **p.Trp66*** (c.197G>A) in extracellular domain; review literature characterizes CD79A defects as causing a complete developmental block (benali2020geneticapproachesfor pages 4-6, cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) |
| **CD79B (Igβ / pre-BCR signaling)** | Autosomal recessive | Defective Igβ signaling in the pre-BCR/BCR pathway; described as a more **hypomorphic/leaky** developmental defect than CD79A (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) | Clinically grouped with CD79A/IGLL1/BLNK deficiencies as resembling BTK-related agammaglobulinemia (mina2021molecularrequirementsfor pages 4-5) | Human case evidence is referenced in reviews, including hypomorphic/leaky defects; no exact variant details available in cited context (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) |
| **BLNK (B-cell linker protein)** | Autosomal recessive | Downstream pre-BCR/BCR signal transduction defect; integrated with BTK and PI3K signaling during B-cell development (tangye2023inbornerrorsof pages 3-3) | Review evidence states BLNK-deficient patients are phenotypically similar to BTK/XLA; no quantitative cohort details in available context (mina2021molecularrequirementsfor pages 4-5) | Listed in recent reviews among genes causing AR agammaglobulinemia; heterozygous carriers reported healthy, supporting biallelic disease mechanism (tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3) |
| **PIK3R1 / PIK3CD (PI3K pathway)** | PIK3R1: autosomal recessive and dominant disease forms reported in agammaglobulinemia literature; PIK3CD mentioned as a B-cell deficiency/agammaglobulinemia gene in review context | PI3K regulatory/catalytic subunits activated after BCR ligation to generate PIP3; disruption impairs BCR signaling and B-cell development (tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3) | Review evidence highlights **early neutropenia** as notable in **PIK3R1**-related agammaglobulinemia, often improving over time (cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10) | Included in 2022-2023 reviews as established pathway genes for autosomal agammaglobulinemia/B-cell deficiency; no exact patient-level variants in available context (cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10, tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3) |
| **SLC39A7 (zinc transporter / signaling homeostasis)** | Autosomal recessive | Perturbs divalent-cation–dependent signaling required for early B-cell development; developmental block grouped with pre-B to immature B-cell deficiency (mina2021molecularrequirementsfor pages 4-5) | Review notes **6 individuals from 5 kindreds** with peripheral B-cell deficiency and preserved T-cell function (mina2021molecularrequirementsfor pages 4-5) | Identified in recent reviews as a novel AR cause of agammaglobulinemia/B-cell lymphopenia; no specific variant listed in available context (mina2021molecularrequirementsfor pages 4-5) |
| **TCF3 (E2A/E47 transcription factor)** | Autosomal recessive and autosomal dominant | Earlier developmental defect than classic pre-BCR genes, with block around the common lymphoid progenitor to pro-B stage; dominant-negative E47 effect can yield BCR-negative B cells (mina2021molecularrequirementsfor pages 4-5, cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) | Review evidence describes autosomal dominant and recessive agammaglobulinemia, including cases from Pakistan; clinical severity can include agammaglobulinemia and neutropenia-spectrum presentations (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) | Recent reviews note dominant-negative mechanism and BCR-negative B cells; exact variant not provided in available context (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13) |
| **TOP2B (topoisomerase IIβ)** | Autosomal dominant | Earlier block in B-cell development; patient mutations have a **dominant negative** effect, impairing proliferation/survival of B-2 cells and humoral responses (mina2021molecularrequirementsfor pages 4-5) | Primary paper identified **10 individuals from 5 kindreds** with syndromic B-cell immunodeficiency/Hoffman syndrome features including facial dysmorphism, limb anomalies, and urogenital malformations (mina2021molecularrequirementsfor pages 4-5) | Abstract-supported model evidence: patient mutations in **TOP2B** had a dominant-negative effect; yeast plus knock-in/knockout mouse models showed defective B-cell development and impaired humoral function (mina2021molecularrequirementsfor pages 4-5) |
| **FNIP1 (metabolic/mTOR-AMPK pathway)** | Autosomal recessive | Early B-cell developmental defect with altered cellular energy homeostasis; increased **mTOR** and **AMPK** activity compromises B-cell development/survival (tangye2023inbornerrorsof pages 6-7) | **6 patients from 5 families** had frank B-cell deficiency, agammaglobulinemia, and recurrent respiratory infections; bone marrow showed increased pro-B and pre-B1 cells with reduced pre-BII and immature B cells (tangye2023inbornerrorsof pages 6-7) | Recent 2023 review highlights FNIP1 as an AR agammaglobulinemia cause with marrow-stage quantitative abnormalities, representing a newer metabolic subtype (tangye2023inbornerrorsof pages 6-7) |


*Table: This table summarizes the autosomal genetic subtypes of agammaglobulinemia supported by the retrieved evidence, highlighting inheritance, developmental mechanisms, and representative human findings. It is useful for distinguishing the umbrella diagnosis from its heterogeneous molecular causes.*

### Variant interpretation

- **Origin:** causal variants are germline; somatic disease is not the recognized mechanism.
- **Common classes:** nonsense, frameshift, splice-disrupting, missense/hypomorphic, and occasionally larger deletions.
- **Functional effects:** most AR variants are loss-of-function; dominant **TOP2B** and some **TCF3/E47** variants act through dominant-negative effects. (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13, benali2020geneticapproachesfor pages 4-6)
- **Population frequency:** pathogenic alleles are expected to be rare; no defensible gene-wide carrier frequency or exact gnomAD frequency can be assigned without variant-specific database queries.
- **ACMG classification:** each variant requires case-level ACMG/AMP evaluation incorporating segregation, population frequency, predicted loss of function, functional evidence, and phenotype. “Gene associated with disease” does not make every rare variant pathogenic.
- **Penetrance/expressivity:** severe biallelic null pre-BCR defects are generally highly penetrant, but hypomorphic variants can be leaky. Expressivity is variable, as illustrated by complete **CD79A** versus hypomorphic **CD79B** developmental blocks and syndromic **TOP2B** disease. (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13)

No consistently validated modifier genes, disease-specific methylation signature, histone abnormality, recurrent aneuploidy, or characteristic chromosomal rearrangement was identified. Copy-number variants remain diagnostically relevant when sequencing is negative.

---

## 5. Environmental, lifestyle, and infectious information

No non-genetic exposure is known to cause autosomal agammaglobulinemia. Environmental and lifestyle factors primarily modify complications:

- respiratory smoke and pollution should be minimized because chronic airway damage can compound infection risk;
- safe food and water practices reduce gastrointestinal pathogen exposure;
- prompt evaluation of fever and respiratory symptoms is important;
- household infection control is relevant during outbreaks.

Typical infectious susceptibility includes recurrent bacterial respiratory infections, enteric infections, and severe or chronic enterovirus infection. **IGHM** deficiency has been associated with enteroviral infection and *Pseudomonas* sepsis. Serology is unreliable because patients cannot produce normal antibody responses; pathogen diagnosis should preferentially use culture, antigen detection, or nucleic-acid amplification. (cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5)

---

## 6. Mechanism and pathophysiology

### Core causal chain

**Pathogenic germline variant → defective pre-BCR assembly/signaling or B-lineage transcription/metabolism → developmental arrest in bone marrow → profound loss of immature and mature B cells → absent plasma-cell and antibody output → impaired neutralization, opsonization, complement recruitment, and mucosal defense → recurrent infection → cumulative tissue injury, especially bronchiectasis and gastrointestinal disease.** (mina2021molecularrequirementsfor pages 4-5, tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3)

### Upstream mechanisms

1. **Pre-BCR assembly:** productive μ-heavy-chain expression (**IGHM**) must combine with surrogate light-chain components, including λ5 (**IGLL1**), and signal through Igα/Igβ (**CD79A/CD79B**). Disruption prevents the proliferative and survival checkpoint from pro-B to pre-B cell. (mina2021molecularrequirementsfor pages 4-5, tangye2023inbornerrorsof pages 2-3)
2. **Signal transduction:** BLNK coordinates signaling involving BTK and PI3K. **PIK3R1/PIK3CD** encode regulatory/catalytic PI3K subunits that produce PIP3 after receptor ligation. Failure suppresses developmental survival and expansion. (tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3)
3. **Transcription/development:** **TCF3/E47** acts earlier, around common lymphoid progenitor–to–pro-B commitment; dominant-negative variants may produce BCR-negative B cells. (mina2021molecularrequirementsfor pages 4-5, cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13)
4. **DNA topology:** dominant-negative **TOP2B** variants impair proliferation and survival of conventional B-2 cells, blocking development and humoral responses. (mina2021molecularrequirementsfor pages 4-5)
5. **Ion/metabolic homeostasis:** **SLC39A7** demonstrates a requirement for divalent-cation homeostasis in lymphocyte signaling. **FNIP1** deficiency perturbs energy homeostasis, increasing mTOR and AMPK activity; marrow shows excess pro-B/pre-BI cells and reduced pre-BII/immature B cells. Six patients from five families had B-cell deficiency, agammaglobulinemia, and recurrent respiratory infection. (mina2021molecularrequirementsfor pages 4-5, tangye2023inbornerrorsof pages 6-7)

### Downstream mechanisms

The downstream injury is predominantly infection-mediated rather than autoimmune or intrinsically degenerative. Deficient antibody production impairs opsonophagocytosis of encapsulated bacteria and viral neutralization. Repeated pulmonary infections damage airway epithelium, producing chronic suppuration and bronchiectasis. Enteroviral persistence can produce severe neurologic or systemic disease.

### Ontology suggestions

- **GO biological process:** B-cell differentiation (GO:0030183); B-cell activation (GO:0042113); B-cell receptor signaling pathway (GO:0050853); immune response (GO:0006955); immunoglobulin production (GO:0002377); phosphatidylinositol 3-kinase signaling; regulation of mTOR signaling.
- **Cell Ontology:** hematopoietic stem cell; common lymphoid progenitor; pro-B cell; pre-B cell; immature B cell; mature B cell; plasma cell. Exact CL identifiers should be resolved against the current Cell Ontology release.
- **GO cellular component:** pre-B-cell receptor complex; B-cell receptor complex; plasma membrane; cytosol; nucleus for TCF3/TOP2B.

No clinically validated autosomal-specific transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, or multi-omics diagnostic signature was found. Marrow flow cytometry and functional genetic studies remain more directly informative.

---

## 7. Anatomical structures affected

### Primary site

The primary anatomical lesion is in **bone marrow B-cell development**.

- Suggested UBERON: bone marrow (**UBERON:0002371**).
- Affected cells: pro-B, pre-B, immature B, and consequently circulating mature B cells and plasma cells.
- Primary compartments: pre-BCR/BCR at the plasma membrane; cytosolic signaling complexes; nucleus for TCF3 and TOP2B.

### Secondary sites

- **Respiratory system:** middle ear, paranasal sinuses, bronchi, and lungs; recurrent infection may lead to bronchiectasis.
- **Gastrointestinal tract:** recurrent infection and chronic diarrhea.
- **Central nervous system:** secondary involvement in severe or chronic enteroviral infection.
- **Lymphoid organs:** small or poorly developed tonsils/lymph nodes may reflect absent B-cell follicles.
- **TOP2B-related disease:** craniofacial, limb, and urogenital structures may be congenitally abnormal. Ten affected people from five kindreds were summarized in the retrieved review. (mina2021molecularrequirementsfor pages 4-5)

Lateralization is not characteristic.

---

## 8. Temporal development

The molecular defect is congenital, but symptoms usually emerge when maternally transferred IgG declines during the first year of life. AR forms tend to present earlier and more severely than XLA; **IGHM** deficiency had a mean reported presentation age of 11 months. (cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5)

The untreated course is chronic and punctuated by acute infections. There are no formal disease stages, but a useful clinical model is:

1. **Pre-symptomatic congenital phase:** absent/low B-cell output; KREC may already be undetectable.
2. **Early infectious phase:** recurrent otitis, sinusitis, pneumonia, diarrhea, sepsis, or neutropenia.
3. **Established chronic disease:** recurrent infection despite care, chronic sinus or lung disease.
4. **Complicated disease:** bronchiectasis, chronic enteroviral infection, organ damage, or severe sepsis.

There is no spontaneous remission of a true null developmental defect. Apparent improvement may reflect immunoglobulin replacement, resolution of infection-associated neutropenia, or a hypomorphic/leaky genotype. The critical intervention window is before recurrent infections produce irreversible lung damage.

---

## 9. Inheritance and population

### Epidemiology

Reliable prevalence or incidence per 100,000 is unavailable for autosomal agammaglobulinemia as an umbrella category. XLA represents about 85% of congenital agammaglobulinemia; **IGHM** deficiency alone has been estimated at approximately 5% of all cases. Other subtypes are generally represented by individual families or very small series. (benali2020geneticapproachesfor pages 1-2, cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5)

### Inheritance

- **AR:** IGHM, IGLL1, CD79A, CD79B, BLNK, SLC39A7, FNIP1, and some PIK3R1/TCF3 presentations.
- **AD:** selected TCF3 and TOP2B disorders; dominant disease may be de novo.
- **Recurrence risk:** for a confirmed AR disorder, each full sibling has a 25% affected, 50% carrier, and 25% non-carrier probability. For an affected heterozygous AD parent, transmission risk is 50%, subject to penetrance.
- **Consanguinity:** materially increases AR disease probability and has facilitated discovery in North-African and other consanguineous families. (benali2020geneticapproachesfor pages 1-2)
- **Sex ratio:** expected to be approximately equal for nonsyndromic autosomal disease, although tiny cohorts preclude a stable estimate.
- **Anticipation:** not expected.
- **Germline mosaicism:** theoretically possible, particularly after an apparently de novo variant, but no subtype-specific rate is established.
- **Founder effects/carrier frequency:** may exist for individual variants, but no generalizable frequency was found.

---

## 10. Diagnostics

### Clinical and laboratory evaluation

Suspect the disorder in any child—especially a girl, a child of consanguineous parents, or a patient without a BTK defect—with recurrent severe infection, extremely low immunoglobulins, and absent B cells.

Recommended evaluation:

1. Quantitative serum **IgG, IgA, and IgM**, interpreted using age-specific ranges.
2. CBC and differential, particularly for neutropenia.
3. Flow cytometry for CD3, CD4, CD8, CD19/CD20, and NK cells. In classic agammaglobulinemia, B cells are commonly below 2%; the molecular cohort reported below 0.5% with normal T-cell numbers. (benali2020geneticapproachesfor pages 1-2, benali2020geneticapproachesfor pages 4-6)
4. Vaccine-specific antibody titers are generally absent, but intentional live-vaccine challenge is contraindicated and additional vaccination solely to prove failure is usually unnecessary in profound agammaglobulinemia.
5. Culture/PCR rather than antibody serology for suspected infection.
6. Pulmonary assessment—oxygen saturation, chest imaging, and pulmonary function when age-appropriate—if recurrent pneumonia, chronic cough, or suspected bronchiectasis is present.
7. Bone-marrow immunophenotyping is not routinely required but can localize the developmental block in unresolved cases.

### Genetic testing strategy

- Begin with an **inborn-errors-of-immunity/agammaglobulinemia panel** containing at least **BTK, IGHM, IGLL1, CD79A, CD79B, BLNK, PIK3R1, PIK3CD, SLC39A7, TCF3, TOP2B, FNIP1**, and relevant phenocopy genes such as **RAG1/RAG2**.
- In a classic male phenotype, BTK testing remains essential even if the referral label says “autosomal.”
- Use deletion/duplication analysis because sequence-only assays can miss exon or multiexon copy-number changes.
- If the panel is negative or the phenotype is syndromic, proceed to trio WES or WGS. The 2020 cohort concluded that sequential testing was expensive and slow, whereas WES produced a more efficient definitive diagnosis in genetically heterogeneous families. (benali2020geneticapproachesfor pages 1-2)
- Confirm candidate variants by orthogonal sequencing, segregation, population-frequency review, and functional studies when classification remains uncertain.
- CMA is reasonable for syndromic disease or suspected copy-number change; routine karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line.

### Newborn screening

Kappa-deleting recombination excision circles (**KREC**) may be low or undetectable from birth and remain low in autosomal agammaglobulinemia. Combined TREC/KREC screening can identify severe B-cell lymphopenia before infection, but KREC screening is not universally implemented and may miss leaky defects. Its potential value is earlier immunology referral, avoidance of live vaccines, and timely Ig replacement. (cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10)

### Differential diagnosis

- XLA due to **BTK** variants.
- Severe combined immunodeficiency or leaky SCID, including **RAG1/RAG2** disease.
- Transient hypogammaglobulinemia of infancy—B cells are generally present.
- Common variable immunodeficiency—usually later onset with B cells present.
- Hyper-IgM syndromes—IgM is normal/high rather than universally absent.
- Secondary hypogammaglobulinemia from anti-CD20 therapy, nephrotic/protein-losing disease, malignancy, or immunosuppressive therapy.
- Thymoma-associated immunodeficiency in adults.

---

## 11. Outcome and prognosis

Without treatment, severe bacterial infection, sepsis, chronic enteroviral disease, and progressive lung injury confer substantial morbidity and mortality. Immunoglobulin replacement prevents many infections and improves survival, but it does not reverse established bronchiectasis or congenital syndromic abnormalities. (benali2020geneticapproachesfor pages 1-2)

Major morbidity includes recurrent hospitalization, chronic sinus and lung disease, bronchiectasis, gastrointestinal infection, neurologic enterovirus complications, and treatment burden. Prognosis is best with diagnosis before irreversible organ damage, adequate Ig exposure, adherence, rapid treatment of breakthrough infections, and specialist respiratory care.

No robust autosomal-only 5-year survival, life-expectancy, mortality, disability, or quality-of-life statistic was identified. Genotype may influence prognosis: **IGHM** disease is often early and severe; hypomorphic **CD79B/IGLL1** defects may be milder; **TOP2B** prognosis includes nonimmune congenital anomalies. These genotype–phenotype relationships remain based on small cohorts and should not be used deterministically. (mina2021molecularrequirementsfor pages 4-5, cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5, cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13)

---

## 12. Treatment

### Standard therapy

**Lifelong immunoglobulin replacement is the treatment of choice** for non-transplanted patients. IVIG and SCIG provide passive IgG, reduce serious bacterial infection, and improve survival. The dose and interval should be individualized to infection control, pharmacokinetics, weight, bronchiectasis, and adverse effects rather than a universal trough alone. (benali2020geneticapproachesfor pages 1-2, cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10)

Suggested NCIt concepts include **Immunoglobulin Replacement Therapy**, **Intravenous Immunoglobulin**, **Subcutaneous Immunoglobulin**, **Antibiotic Therapy**, and **Hematopoietic Stem Cell Transplantation**; exact NCIt codes should be resolved against the current NCIt release.

### Antimicrobial and supportive care

- Treat suspected bacterial infection promptly; obtain cultures where feasible.
- Consider prophylactic antibiotics for recurrent infection despite optimized Ig replacement or established bronchiectasis.
- Use airway-clearance therapy and respiratory specialist management for bronchiectasis.
- Monitor CBC, immunoglobulin exposure, infection frequency, pulmonary function, and liver/renal status as clinically indicated.
- Adverse effects of Ig therapy include infusion reactions, headache/aseptic meningitis, thrombosis, hemolysis, and renal injury; SCIG generally reduces systemic reactions but causes local-site reactions.

### Advanced and experimental therapy

Hematopoietic stem-cell transplantation is not routine first-line therapy for isolated agammaglobulinemia because lifelong Ig replacement is effective and transplantation has substantial risk. It may be considered for selected severe syndromic/combined defects, uncontrollable complications, or a genotype for which immune reconstitution is established. No approved gene therapy, CRISPR therapy, RNA therapy, or genotype-specific small molecule exists for the autosomal agammaglobulinemia umbrella.

A ClinicalTrials.gov search retrieved IVIG/SCIG studies enrolling broad primary hypo-/agammaglobulinemia populations, including NCT00138697, NCT00161993, and NCT00520494, but no clearly autosomal-subtype-specific interventional trial. Consequently, product studies support Ig replacement generally but cannot establish gene-specific response rates.

### Pharmacogenomics

No validated CPIC/PharmGKB genotype-guided dosing rule specific to these genes and immunoglobulin replacement was identified.

---

## 13. Prevention

### Primary prevention

The disease cannot be prevented after conception through lifestyle change. Reproductive options after identifying the familial variant include genetic counseling, carrier testing, prenatal diagnosis, and preimplantation genetic testing. Cascade testing is appropriate for at-risk relatives.

### Secondary prevention

- Identify affected newborns through family-based testing or TREC/KREC programs where available.
- Begin immunology follow-up and Ig replacement before severe infection when diagnostic criteria are met.
- Avoid delays caused by repeated treatment of infections without immune evaluation.

### Tertiary prevention

- Maintain adequate Ig replacement and adherence.
- Use antimicrobial prophylaxis selectively.
- Perform respiratory surveillance and airway clearance.
- Ensure dental, nutritional, and gastrointestinal care.
- Prefer inactivated vaccines when vaccination is indicated; responses may be minimal but household immunization provides indirect protection.
- **Avoid live attenuated vaccines in the affected person**, particularly oral poliovirus and other live viral products, unless a specialist has documented sufficient immunity in an atypical leaky phenotype.
- Vaccinate close contacts according to public-health guidance while considering precautions around transmissible live vaccines.

No diet, supplement, exercise program, or environmental intervention substitutes for Ig replacement.

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary disorder exactly equivalent to the full human autosomal-agammaglobulinemia umbrella was identified in the retrieved evidence. Therefore, no defensible breed, VBO identifier, animal incidence, or zoonotic implication can be assigned.

Orthologs of the implicated genes are evolutionarily conserved across vertebrates, and the pre-BCR checkpoint is conserved in mammals. The disorder is inherited and **not transmissible or zoonotic**. Any veterinary annotation should be made at the individual gene/ortholog level through OMIA and NCBI Gene rather than inferred from the human umbrella label.

---

## 15. Model organisms and experimental systems

The best retrieved primary model evidence concerns **TOP2B**. Broderick et al., *Nature Communications*, published August 2019, DOI [10.1038/s41467-019-11570-6](https://doi.org/10.1038/s41467-019-11570-6), used *Saccharomyces cerevisiae* and knock-in/knockout mice. The abstract reports that patient variants **“have a dominant negative effect on enzyme function, resulting in defective proliferation, survival of B-2 cells, causing a block in B cell development, and impair humoral function in response to immunization.”** This provides cross-system functional evidence connecting variant, enzyme dysfunction, cellular phenotype, and impaired antibody response. (mina2021molecularrequirementsfor pages 4-5)

### Model categories and uses

- **Mouse knockout/conditional knockout:** localizes B-lineage developmental checkpoints and measures marrow subsets, peripheral B cells, serum immunoglobulins, and immunization responses.
- **Knock-in/humanized alleles:** tests dominant-negative or hypomorphic patient variants.
- **Yeast:** useful for TOP2B enzyme-function studies but cannot model adaptive immunity.
- **Patient-derived cells:** flow cytometry, immunoblotting, signaling assays, and rescue experiments can validate candidate variants.
- **iPSC/organoid systems:** potentially useful but no clinically mature autosomal-agammaglobulinemia platform was identified.

### Limitations

Murine B-cell development is informative but not identical to human development; redundancy and lineage distribution differ. Complete knockout models may overstate the severity of human hypomorphic alleles. Yeast models assess conserved enzymatic function but not B-cell-specific physiology.

---

## Recent developments and expert interpretation

1. **2023 mechanistic consolidation:** Tangye et al. integrated pre-BCR, PI3K, transcriptional, ionic, and metabolic defects into a human B-cell-development framework, emphasizing that rare patients function as natural experiments defining essential pathways. (tangye2023inbornerrorsof pages 3-3, tangye2023inbornerrorsof pages 2-3, tangye2023inbornerrorsof pages 6-7)
2. **FNIP1 as a metabolic B-cell-development disorder:** six patients from five families showed agammaglobulinemia with a marrow shift from later pre-B/immature cells toward earlier pro-B/pre-BI stages and abnormal AMPK–mTOR activity. (tangye2023inbornerrorsof pages 6-7)
3. **Broadening phenotype recognition:** recent work increasingly recognizes leaky B-cell lymphopenia and hypogammaglobulinemia rather than only complete absence of B cells. This supports early genomic testing and argues against requiring a textbook phenotype before sequencing.
4. **Screening innovation:** KREC measurement can detect severe B-cell lymphopenia at birth, although implementation and sensitivity for partial defects remain unresolved. (cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10)
5. **Expert consensus:** early molecular diagnosis matters because it confirms inheritance, directs family counseling, distinguishes isolated antibody deficiency from combined immunodeficiency, and may alter consideration of transplantation. The 2020 cohort demonstrates the practical superiority of WES over serial single-gene testing in consanguineous, genetically heterogeneous families. (benali2020geneticapproachesfor pages 1-2)

## Knowledge-base conclusions

Autosomal agammaglobulinemia should be represented as a **Mendelian disease family**, not as a single gene–disease pair. Its invariant biological axis is failure of early B-cell development and antibody production, but inheritance, developmental checkpoint, syndromic involvement, and severity depend on the causal gene and allele. The most robust annotations are absent/reduced B cells, severe hypogammaglobulinemia, recurrent respiratory infection, early childhood onset, pre-BCR/BCR-pathway dysfunction, and benefit from lifelong immunoglobulin replacement. Autosomal-specific prevalence, survival, quality-of-life, environmental interaction, omics biomarkers, and treatment-response statistics remain major evidence gaps.

References

1. (benali2020geneticapproachesfor pages 1-2): Meriem Ben-Ali, Nadia Kechout, Najla Mekki, Jing Yang, Koon Wing Chan, Abdelhamid Barakat, Zahra Aadam, Jouda Gamara, Lamia Gargouri, Beya Largueche, Nabil BelHadj-Hmida, Amel Nedri, Houcine Ben Ameur, Fethi Mellouli, Rachida Boukari, Mohamed Bejaoui, Aziz Bousfiha, Imen Ben-Mustapha, Yu-Lung Lau, and Mohamed-Ridha Barbouche. Genetic approaches for definitive diagnosis of agammaglobulinemia in consanguineous families. Journal of Clinical Immunology, 40:96-104, Nov 2020. URL: https://doi.org/10.1007/s10875-019-00706-4, doi:10.1007/s10875-019-00706-4. This article has 13 citations and is from a domain leading peer-reviewed journal.

2. (mina2021molecularrequirementsfor pages 4-5): Erika Della Mina, Antoine Guérin, and Stuart G. Tangye. Molecular requirements for human lymphopoiesis as defined by inborn errors of immunity. Stem Cells, 39:389-402, Jan 2021. URL: https://doi.org/10.1002/stem.3327, doi:10.1002/stem.3327. This article has 4 citations and is from a highest quality peer-reviewed journal.

3. (cardenasmorales2022agammaglobulinemiafromxlinked pages 4-5): Melissa Cardenas-Morales and Vivian P. Hernandez-Trujillo. Agammaglobulinemia: from x-linked to autosomal forms of disease. Clinical Reviews in Allergy & Immunology, 63:22-35, Jul 2022. URL: https://doi.org/10.1007/s12016-021-08870-5, doi:10.1007/s12016-021-08870-5. This article has 86 citations and is from a peer-reviewed journal.

4. (tangye2023inbornerrorsof pages 3-3): Stuart G. Tangye, Tina Nguyen, Elissa K. Deenick, Vanessa L. Bryant, and Cindy S. Ma. Inborn errors of human b cell development, differentiation, and function. The Journal of Experimental Medicine, Jun 2023. URL: https://doi.org/10.1084/jem.20221105, doi:10.1084/jem.20221105. This article has 72 citations.

5. (tangye2023inbornerrorsof pages 2-3): Stuart G. Tangye, Tina Nguyen, Elissa K. Deenick, Vanessa L. Bryant, and Cindy S. Ma. Inborn errors of human b cell development, differentiation, and function. The Journal of Experimental Medicine, Jun 2023. URL: https://doi.org/10.1084/jem.20221105, doi:10.1084/jem.20221105. This article has 72 citations.

6. (benali2020geneticapproachesfor pages 4-6): Meriem Ben-Ali, Nadia Kechout, Najla Mekki, Jing Yang, Koon Wing Chan, Abdelhamid Barakat, Zahra Aadam, Jouda Gamara, Lamia Gargouri, Beya Largueche, Nabil BelHadj-Hmida, Amel Nedri, Houcine Ben Ameur, Fethi Mellouli, Rachida Boukari, Mohamed Bejaoui, Aziz Bousfiha, Imen Ben-Mustapha, Yu-Lung Lau, and Mohamed-Ridha Barbouche. Genetic approaches for definitive diagnosis of agammaglobulinemia in consanguineous families. Journal of Clinical Immunology, 40:96-104, Nov 2020. URL: https://doi.org/10.1007/s10875-019-00706-4, doi:10.1007/s10875-019-00706-4. This article has 13 citations and is from a domain leading peer-reviewed journal.

7. (tangye2023inbornerrorsof pages 6-7): Stuart G. Tangye, Tina Nguyen, Elissa K. Deenick, Vanessa L. Bryant, and Cindy S. Ma. Inborn errors of human b cell development, differentiation, and function. The Journal of Experimental Medicine, Jun 2023. URL: https://doi.org/10.1084/jem.20221105, doi:10.1084/jem.20221105. This article has 72 citations.

8. (cardenasmorales2022agammaglobulinemiafromxlinked pages 8-10): Melissa Cardenas-Morales and Vivian P. Hernandez-Trujillo. Agammaglobulinemia: from x-linked to autosomal forms of disease. Clinical Reviews in Allergy & Immunology, 63:22-35, Jul 2022. URL: https://doi.org/10.1007/s12016-021-08870-5, doi:10.1007/s12016-021-08870-5. This article has 86 citations and is from a peer-reviewed journal.

9. (cardenasmorales2022agammaglobulinemiafromxlinked pages 12-13): Melissa Cardenas-Morales and Vivian P. Hernandez-Trujillo. Agammaglobulinemia: from x-linked to autosomal forms of disease. Clinical Reviews in Allergy & Immunology, 63:22-35, Jul 2022. URL: https://doi.org/10.1007/s12016-021-08870-5, doi:10.1007/s12016-021-08870-5. This article has 86 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Agammaglobulinemia-deep-research-falcon_artifacts/artifact-00.md)