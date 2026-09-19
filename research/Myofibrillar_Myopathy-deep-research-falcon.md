---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T05:03:41.865725'
end_time: '2026-08-01T05:11:50.303951'
duration_seconds: 488.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myofibrillar Myopathy
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
  path: Myofibrillar_Myopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myofibrillar Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myofibrillar Myopathy** covering all of the
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
- **Disease Name:** Myofibrillar Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myofibrillar Myopathy** covering all of the
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


# Myofibrillar Myopathy: Disease Characteristics Research Report

## Executive summary

Myofibrillar myopathy (MFM) is not one molecular disease but a genetically heterogeneous group of inherited **protein-aggregate myopathies**. Its defining lesion is focal myofibrillar dissolution, usually beginning at the Z-disc, followed by accumulation of desmin, myotilin, αB-crystallin and other sarcomeric or protein-quality-control proteins. Skeletal muscle is invariably central, but cardiac muscle, respiratory muscles and peripheral nerves can also be affected. Clinical onset ranges from infancy to late adulthood, although classic DES-, FLNC- and MYOT-associated disease is commonly adult-onset and slowly progressive. No approved disease-modifying treatment exists; present implementation consists of molecular diagnosis, cardiac and respiratory surveillance, rehabilitation, assistive devices and treatment of organ-specific complications. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 1-6)

The following reusable ontology-oriented summary complements the narrative report. IDs marked “suggested” should be checked against the current source ontology before database ingestion.

| domain | key entities/findings | suggested ontology terms/IDs | evidence notes |
|---|---|---|---|
| disease definition | Inherited protein-aggregate myopathy characterized by myofibrillar dissolution beginning at the Z-disc, accumulation of desmin/myotilin/\u03b1B-crystallin and other proteins, and progressive skeletal \u00b1 cardiac/respiratory involvement | MONDO: myofibrillar myopathy **[suggested; validate]**; MeSH: Myopathies **[broader; validate]**; GO: sarcomere organization (GO:0045214), protein-containing complex assembly (GO:0065003) | Workshop and reviews describe MFM as Z-disc-initiated myofibrillar degradation with pleomorphic aggregates and multisystem muscle involvement (olive2021246thenmcinternational pages 1-6, batonnetpichon2017myofibrillarmyopathiesnew pages 1-2) |
| core causal genes | **DES**, **CRYAB**, **MYOT**, **LDB3**/**ZASP**, **FLNC**, **BAG3** | HGNC gene symbols; OMIM-linked disease subtypes **[suggested; validate exact IDs]** | Recurrent/core MFM genes consistently listed across reviews and workshop synthesis (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 1-6) |
| expanded/associated genes | **FHL1, TTN, DNAJB6, PLEC, ACTA1, HSPB8, PYROXD1, SQSTM1/TIA1**; additional overlap genes reported in MFM/protein aggregate myopathy spectrum | HGNC symbols; MONDO disease links **[suggested; validate]** | Expanded genetic heterogeneity emphasized in genomic-context review and ENMC workshop; Japanese screening found a molecular diagnosis in 34% of 297 cases, with **TTN** most common among solved cases (olive2021246thenmcinternational pages 6-10, olive2021246thenmcinternational pages 1-6) |
| inheritance | Predominantly autosomal dominant; variable penetrance/expressivity; some recessive, X-linked, and digenic examples reported in expanded spectrum | HP: Family history (HP:0032316) **[suggested]**; inheritance terms from HPO/GENO **[suggested; validate]** | Autosomal dominant inheritance is typical for classic forms, but broader genomic studies show heterogeneous inheritance patterns (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 6-10) |
| phenotype: muscle weakness | Slowly progressive proximal, distal, scapuloperoneal, or limb-girdle weakness; axial/facial weakness can occur | HP: Muscle weakness (HP:0001324), Proximal muscle weakness (HP:0003701), Distal muscle weakness (HP:0002460), Axial muscle weakness (HP:0003323), Facial weakness (HP:0000204) | Major phenotype across cohorts and reviews; onset and distribution are genotype-dependent (olive2021246thenmcinternational pages 1-6, luo2019characterizationofchinese pages 6-7, olive2005myotilinopathyrefiningthe pages 1-2) |
| phenotype: progression/onset | Usually chronic progressive disease; many classic forms adult-onset, but BAG3 and some TTN-related forms can begin in childhood or earlier | HP: Progressive muscle weakness (HP:0003323 **[broader/validate]**), Adult onset (HP:0003581), Childhood onset (HP:0011463) | Mayo/French cohorts summarized by ENMC showed mean onset ages ~52 and ~42 years; genotype-specific childhood onset noted for BAG3opathy (olive2021246thenmcinternational pages 1-6, luo2019characterizationofchinese pages 6-7) |
| phenotype: cardiac | Cardiomyopathy, conduction disease, arrhythmia; some patients require pacemaker/defibrillator or transplantation | HP: Cardiomyopathy (HP:0001638), Arrhythmia (HP:0011675), Cardiac conduction abnormality (HP:0000076), Pacemaker implantation **[procedure term, validate]** | Cardiac involvement is a major morbidity driver; reviews cite frequent cardiac disease and intervention needs, especially in DES/BAG3-related disease (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, luo2019characterizationofchinese pages 6-7) |
| phenotype: respiratory | Respiratory insufficiency/restrictive respiratory involvement; early respiratory failure in some genotypes; ventilatory support may be required | HP: Respiratory insufficiency (HP:0002093), Restrictive ventilatory defect (HP:0002091), Sleep-disordered breathing (HP:0002360) **[suggested]** | Respiratory dysfunction occurs in a substantial subset; one review notes ~one-third with respiratory insufficiency/dysphagia, with severe BAG3 cases showing high respiratory burden (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, luo2019characterizationofchinese pages 6-7) |
| phenotype: neuropathy | Peripheral neuropathy may accompany myopathy, often axonal/sensorimotor; can complicate phenotypic classification | HP: Peripheral neuropathy (HP:0009830), Axonal neuropathy (HP:0003447), Sensorimotor neuropathy (HP:0007141) | ENMC and cohort data note peripheral neuropathy in subsets; Chinese series reported motor/sensorimotor axonopathy predominance (olive2021246thenmcinternational pages 6-10, luo2019characterizationofchinese pages 6-7) |
| phenotype: bulbar/other | Dysphagia, dysphonia, stiffness, myalgia, ophthalmoparesis, contractures/spine deformity in some subtypes | HP: Dysphagia (HP:0002015), Dysphonia (HP:0001618), Myalgia (HP:0003326), Ophthalmoparesis (HP:0000602), Joint contracture (HP:0001371), Scoliosis (HP:0002650) | Recognized but variably frequent features in workshop and gene-specific series (olive2021246thenmcinternational pages 1-6, luo2019characterizationofchinese pages 6-7, olive2005myotilinopathyrefiningthe pages 1-2) |
| pathology/histology | Myofibrillar dissolution starts at Z-disc; protein aggregates; hyaline/eosinophilic inclusions; rimmed vacuoles; desmin/myotilin/\u03b1B-crystallin accumulation; Z-line streaming on EM | GO CC: Z disc (GO:0030018), myofibril (GO:0030016), sarcomere (GO:0030017); HP: Rimmed vacuoles (HP:0003795), Myofibrillar disorganization **[suggested]** | Defining pathologic pattern across MFM subtypes and myotilinopathy/filaminopathy literature (olive2021246thenmcinternational pages 1-6, olive2005myotilinopathyrefiningthe pages 1-2, wadmore2021theroleof pages 1-2) |
| molecular mechanism: Z-disc failure | Disease proteins cluster at/around the Z-disc, disrupting force transmission and sarcomere integrity | GO: sarcomere organization (GO:0045214), actin filament organization (GO:0007015), muscle filament sliding (GO:0030049) | Z-disc proteins such as FLNC, MYOT, ZASP/LDB3, DES are central to MFM pathogenesis (wadmore2021theroleof pages 1-2, batonnetpichon2017myofibrillarmyopathiesnew pages 1-2) |
| molecular mechanism: proteostasis/CASA | Misfolding/aggregation with impaired chaperone-assisted selective autophagy (CASA), aggrephagy, UPS/autophagy stress responses; BAG3/HSPB8/DNAJB6 network implicated | GO: autophagy (GO:0006914), selective autophagy (GO:0061919), protein folding (GO:0006457), response to unfolded protein (GO:0006986), ubiquitin-dependent protein catabolic process (GO:0006511) | Reviews connect MFM to defective protein quality control near the sarcomere; BAG3 and DNAJB6 are highlighted in protein aggregate myopathy biology (olive2021246thenmcinternational pages 6-10, batonnetpichon2017myofibrillarmyopathiesnew pages 1-2) |
| molecular mechanism: aggregate toxicity | Aggregates contain Z-disc and stress-response proteins and likely contribute to myofiber dysfunction rather than being purely epiphenomenal | GO: protein-containing complex disassembly (GO:0043624), aggrephagy **[GO mapping validate]** | Protein aggregation is a defining lesion in MFM and broader protein aggregate myopathies (olive2021246thenmcinternational pages 1-6, wadmore2021theroleof pages 1-2) |
| molecular mechanism: mitochondria/metabolism | Especially in desmin-related disease, mitochondrial architecture, respiration, and metabolic activity can be impaired, contributing to cardiomyopathy | GO: mitochondrial organization (GO:0007005), oxidative phosphorylation (GO:0006119), ATP metabolic process (GO:0046034) | 2024 hiPSC-cardiomyocyte study of **DES E439K** linked mutant desmin to mitochondrial defects and contractile dysfunction (findlay2024dominantlyinheritedmuscle pages 8-9) |
| anatomy: primary organs | Skeletal muscle is primary; heart and respiratory musculature are frequent secondary/parallel targets | UBERON: skeletal muscle tissue (UBERON:0001134), heart (UBERON:0000948), diaphragm (UBERON:0001103), respiratory system (UBERON:0001004) | Clinical burden spans neuromuscular, cardiac, and respiratory systems (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 1-6) |
| anatomy: tissue/cell types | Striated muscle fibers/myofibers; cardiomyocytes; peripheral nerve involvement in subsets | CL: skeletal muscle fiber (CL:0000188), cardiomyocyte (CL:0000746), neuron (CL:0000540), Schwann cell (CL:0002573) **[suggested]** | Reviews and cohorts support primary involvement of skeletal/cardiac muscle with occasional neuropathic features (luo2019characterizationofchinese pages 6-7, wadmore2021theroleof pages 1-2) |
| subcellular localization | Z-disc, sarcomere, myofibril, intermediate filament network, protein aggregates, mitochondria | GO CC: Z disc (GO:0030018), sarcomere (GO:0030017), myofibril (GO:0030016), intermediate filament (GO:0005882), mitochondrion (GO:0005739), protein-containing aggregate (GO:0061702) | Subcellular sites align with pathology and mechanism across major MFM genes (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, wadmore2021theroleof pages 1-2, findlay2024dominantlyinheritedmuscle pages 8-9) |
| diagnostics: biopsy | Muscle biopsy remains key: modified Gomori trichrome, immunohistochemistry for desmin/myotilin/\u03b1B-crystallin/BAG3, EM for Z-line streaming/disarray | NCIT: Muscle Biopsy (C51895) **[suggested]**; HP pathology terms above | Biopsy defines the MFM pattern and helps triage genetic testing (olive2021246thenmcinternational pages 1-6, luo2019characterizationofchinese pages 6-7, olive2005myotilinopathyrefiningthe pages 1-2) |
| diagnostics: electrophysiology | EMG usually myopathic with abnormal electrical irritability; NCS may reveal axonal or sensorimotor neuropathy in mixed phenotypes | NCIT: Electromyography (C38054) **[suggested]**; nerve conduction study **[suggested]** | ENMC notes myopathic EMG patterns; cohort data show neuropathy in subsets (olive2021246thenmcinternational pages 6-10, luo2019characterizationofchinese pages 6-7) |
| diagnostics: imaging | Muscle MRI can show characteristic distribution patterns aiding subtype recognition and differential diagnosis | NCIT: Magnetic Resonance Imaging (C16809) **[suggested]** | Reviews note MRI utility as part of diagnostic work-up in hereditary myopathies including MFM (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2) |
| diagnostics: cardiac/respiratory assessment | ECG, echocardiography, Holter, pulmonary function testing, sleep/ventilation assessment according to symptoms/genotype | NCIT: Electrocardiography (C38053), Echocardiography (C16550), Pulmonary Function Test (C38036) **[suggested]** | Cardiac and respiratory complications are common enough to justify systematic surveillance in many patients (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, luo2019characterizationofchinese pages 6-7) |
| diagnostics: genomics | NGS gene panels, WES/WGS increasingly used because phenotype overlaps with muscular dystrophies/distal myopathies; genomics expanded solved gene list | NCIT: Next Generation Sequencing (C126060), Whole Exome Sequencing (C101294), Whole Genome Sequencing (C150810) **[suggested]** | Genomic-context review and ENMC workshop emphasize heterogeneous genetics and value of NGS; 2024 neuromuscular gene table reflects updated gene-disease curation (olive2021246thenmcinternational pages 6-10, batonnetpichon2017myofibrillarmyopathiesnew pages 1-2) |
| differential diagnosis | Distal myopathies, limb-girdle muscular dystrophies, hereditary myopathy with early respiratory failure, inclusion body myositis, congenital myopathies with aggregates, neuropathy-plus-myopathy syndromes | MONDO/HPO differential terms **[suggested; validate]** | Consider broad overlap because MFM pathology and genetics intersect multiple inherited myopathy groups (olive2021246thenmcinternational pages 6-10, olive2021246thenmcinternational pages 1-6) |
| prognosis | Variable but chronic progressive; morbidity driven by loss of ambulation, cardiomyopathy/arrhythmia, respiratory failure, and occasionally sudden death or transplant need | HP: Reduced mobility (HP:0002374) **[suggested]**, Sudden cardiac death (HP:0001645) | Severity depends strongly on genotype; BAG3 and some DES forms can be particularly aggressive (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, luo2019characterizationofchinese pages 6-7) |
| treatment/supportive care | No approved disease-modifying therapy established; multidisciplinary supportive care includes physiotherapy, orthotics, respiratory support, cardiac rhythm management, heart failure therapy, pacemaker/ICD, transplantation in selected cases | NCIT: Physical Therapy (C15313), Orthotic Device Use **[suggested]**, Ventilatory Support (C15785), Cardiac Pacing (C99532), Implantable Cardioverter Defibrillator Placement (C99925), Heart Transplantation (C15239) **[all suggested; validate]** | Reviews emphasize supportive management and organ-specific interventions; no definitive pharmacologic cure cited (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 6-10) |
| prevention/genetic counseling | Cascade testing, reproductive counseling, and early cardiac/respiratory surveillance in at-risk relatives are pragmatic secondary/tertiary prevention strategies | NCIT: Genetic Counseling (C15271); cascade screening **[suggested]** | Given inherited and variably penetrant nature, family-based testing and surveillance are clinically relevant (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 6-10) |
| model systems | Animal and cellular models include mouse, zebrafish, Drosophila, and patient-derived/iPSC systems for DES/CRYAB/FLNC/BAG3 and related genes | NCBITaxon: Mus musculus (10090), Danio rerio (7955), Drosophila melanogaster (7227); Cell line/iPSC model terms **[suggested]** | Animal-model review highlights broad model ecosystem; 2024 desmin cardiomyopathy work used patient-derived/gene-edited hiPSC cardiomyocytes (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, findlay2024dominantlyinheritedmuscle pages 8-9) |
| evidence gaps | Exact MONDO/Orphanet/HPO mappings for all subtypes, population prevalence/incidence, penetrance, and modifier genes often require source-by-source validation | Ontology IDs in this table are **suggestions requiring database validation where uncertain** | MFM remains genetically and phenotypically heterogeneous, and many summary statistics come from specialized cohorts rather than population registries (olive2021246thenmcinternational pages 6-10, batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 1-6) |


*Table: This compact table organizes key disease, gene, phenotype, mechanism, anatomy, diagnostic, and intervention facts for myofibrillar myopathy into a knowledge-base-friendly format. Suggested ontology mappings are included for rapid curation, but uncertain IDs should be validated against source ontologies before ingestion.*

## 1. Disease information

### Definition and classification

MFM is a **histopathologic and mechanistic disease category** characterized by myofibrillar degradation beginning around the Z-disc, pleomorphic sarcoplasmic inclusions, protein aggregation and, variably, rimmed vacuoles. The category overlaps distal myopathies, limb-girdle muscular dystrophies, hereditary myopathy with early respiratory failure and other protein-aggregate myopathies. Consequently, “MFM” may describe a biopsy pattern before a molecular subtype is known rather than a single etiologic diagnosis. (olive2021246thenmcinternational pages 6-10, olive2021246thenmcinternational pages 1-6)

A foundational review states directly: **“Myofibrillar myopathies (MFMs) are muscular disorders involving proteins that play a role in the structure, maintenance processes and protein quality control mechanisms closely related to the Z-disc.”** It further identifies “progressive disorganization of the interfibrillar network and protein aggregation” as shared pathology. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2)

### Identifiers and synonyms

* **MONDO:** Myofibrillar myopathy is represented in MONDO, but the exact current parent-class ID should be validated through the live MONDO release before ingestion; individual molecular subtypes have separate records.
* **OMIM:** MFM is distributed across subtype records rather than represented adequately by one number. A commonly cited record is **MFM1, OMIM 601419** for desmin-related MFM; other numbered MFM records correspond to CRYAB, MYOT, LDB3, FLNC, BAG3 and additional gene-specific diseases.
* **Orphanet:** Orphanet organizes MFM and several gene-defined subtypes as rare genetic myopathies; current ORPHA identifiers should likewise be resolved through the live API.
* **ICD-10:** no highly specific universal MFM code; cases are commonly captured under hereditary/progressive muscular dystrophy or other specified myopathy categories, depending on jurisdiction.
* **ICD-11:** classified within genetic/developmental disorders of muscle; exact extension coding should be jurisdictionally validated.
* **MeSH:** generally indexed through *Myopathies, Structural, Congenital*, *Muscular Diseases*, gene-specific terms, and pathology concepts rather than one perfectly specific heading.
* **Synonyms:** myofibrillar myopathies; MFM; desmin-related myopathy/desminopathy when DES-associated; αB-crystallinopathy; myotilinopathy; filamin-C myopathy/filaminopathy; ZASP-related myopathy; BAG3 myopathy; protein-aggregate myopathy.

The evidence summarized here is **aggregated disease-level literature**, not individual EHR data. Some statistics derive from retrospective patient cohorts or individual pedigrees.

## 2. Etiology, risk and protective factors

MFM is principally Mendelian. Pathogenic germline variants affect structural Z-disc/intermediate-filament proteins or proteins responsible for sarcomeric proteostasis. Classic genes are **DES, CRYAB, MYOT, LDB3/ZASP, FLNC and BAG3**. The broader MFM-like/protein-aggregate spectrum includes **FHL1, TTN, DNAJB6, PLEC, ACTA1, HSPB8, PYROXD1, KY**, and digenic **SQSTM1–TIA1**, among others. The expansion reflects genuine biological overlap and the fact that one gene can cause several pathologic phenotypes. (olive2021246thenmcinternational pages 6-10, batonnetpichon2017myofibrillarmyopathiesnew pages 1-2)

Most classic forms are autosomal dominant with variable, often age-dependent penetrance and marked intrafamilial expressivity. Recessive, X-linked and digenic disorders occur in the broader spectrum. De novo dominant variants are particularly important in severe childhood BAG3 disease. Variants include missense substitutions, small insertions/deletions, truncating and splice variants; the functional effect is gene- and domain-specific and may be dominant-negative, toxic gain-of-function, aggregation-prone or loss-of-function.

No reproducible environmental cause, infectious trigger, toxin, diet, smoking exposure or protective allele has been established for inherited MFM. Mechanical loading is biologically relevant because contraction repeatedly unfolds or damages Z-disc proteins, but ordinary exercise is not established as a primary cause. Excessive unaccustomed exercise may aggravate symptoms in an already vulnerable muscle; conversely, appropriately dosed rehabilitation may preserve function. Evidence for formal gene–environment interactions, validated protective variants, epigenetic risk states or specific diets is presently insufficient.

## 3. Phenotypes

The phenotype is genotype-dependent and cannot be summarized by one frequency. In two major cohorts summarized by the ENMC workshop, mean onset was **52 years in 82 Mayo Clinic patients** and **42 years in 48 French patients**. Childhood disease occurs, especially with BAG3, while TTN-related phenotypes can range from infancy through adulthood. (olive2021246thenmcinternational pages 6-10, luo2019characterizationofchinese pages 6-7, olive2021246thenmcinternational pages 1-6)

* **Progressive muscle weakness:** distal, proximal, limb-girdle, scapuloperoneal or mixed; axial and facial weakness can occur. Suggested HPO: HP:0001324, HP:0003701, HP:0002460, HP:0003323 and HP:0000204. Weakness impairs walking, stairs, rising, hand use and eventually independent activities.
* **Cardiac disease:** dilated, hypertrophic or restrictive cardiomyopathy; conduction block and ventricular arrhythmia; risk is particularly important in DES and BAG3 disease. Suggested HPO: HP:0001638, HP:0001644, HP:0001639, HP:0001723, HP:0001678. An older synthesis estimated cardiac complications in approximately **60–70%** across selected MFM series and reported pacemaker/defibrillator implantation or transplantation in approximately **10%**; these are referral-cohort estimates, not population rates. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2)
* **Respiratory muscle weakness:** restrictive ventilatory defect, nocturnal hypoventilation and respiratory failure; it may be disproportionate to limb weakness. Respiratory insufficiency and/or dysphagia were reported in approximately one-third in a historical synthesis. Suggested HPO: HP:0002093 and HP:0002091. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2)
* **Peripheral neuropathy:** motor or sensorimotor, frequently axonal, especially in BAG3 and some DES phenotypes. Suggested HPO: HP:0009830, HP:0003447 and HP:0007141. In one 18-person Chinese series, motor/sensorimotor axonopathy was the predominant neuropathy pattern. (luo2019characterizationofchinese pages 6-7)
* **Bulbar/axial/orthopedic features:** dysphagia (HP:0002015), dysphonia (HP:0001618), rigid spine, scoliosis (HP:0002650), contractures (HP:0001371), myalgia (HP:0003326), stiffness and occasional ophthalmoparesis (HP:0000602). (olive2005myotilinopathyrefiningthe pages 1-2, olive2021246thenmcinternational pages 1-6)
* **Laboratory abnormalities:** serum creatine kinase is often normal or mildly/moderately elevated and is neither sensitive nor specific. EMG is generally myopathic with irritability; nerve-conduction testing may disclose concomitant neuropathy. (olive2021246thenmcinternational pages 6-10)

Validated MFM-specific quality-of-life instruments and robust EQ-5D/SF-36 population estimates are lacking. The major burdens are progressive mobility loss, fatigue, ventilatory dependency, dysphagia and anxiety associated with arrhythmia or sudden-death risk.

## 4. Genetic and molecular information

The six canonical proteins occupy complementary roles: DES forms the extrasarcomeric intermediate-filament network; FLNC crosslinks actin and links Z-discs to membrane complexes; MYOT and LDB3/ZASP scaffold the Z-disc; CRYAB is a small heat-shock chaperone; and BAG3 coordinates chaperone-assisted selective autophagy. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, wadmore2021theroleof pages 1-2)

Examples of informative genotype–phenotype relationships include adult-onset DES/FLNC/MYOT disease, childhood-onset severe BAG3 disease and TTN variants causing hereditary myopathy with early respiratory failure or MFM-like pathology. In myotilinopathy, onset in a 13-patient study ranged from **42 to 77 years**, initially affecting distal or proximal legs and later upper limbs. (olive2005myotilinopathyrefiningthe pages 1-2)

A Japanese screen summarized by ENMC evaluated **297 cases from 288 families** and found a causal variant in **89 cases (34%)**. TTN was most frequent among solved cases (**18 cases**), followed by VCP, DES and FHL1. This both demonstrates substantial locus heterogeneity and shows that many patients remain genetically unresolved. (olive2021246thenmcinternational pages 6-10)

Variant interpretation must be transcript- and domain-specific. Rare frequency in gnomAD is necessary but not sufficient; segregation, phenotype, biopsy localization, functional evidence and ACMG/AMP criteria should be integrated. Population allele frequency cannot be supplied generically because it is variant-specific. The causal variants are overwhelmingly **germline**, not somatic. No recurrent chromosomal aneuploidy, translocation or epigenetic signature defines MFM. Modifier-gene and variant-load hypotheses are plausible, but no modifier is sufficiently validated for routine clinical prediction.

## 5. Environmental information

No infectious agent, radiation exposure, occupational toxin or lifestyle exposure is recognized as causal. Mechanical strain likely interacts with genetically impaired Z-disc maintenance and protein quality control, providing a biologically plausible but incompletely quantified gene–environment relationship. Smoking and obesity may worsen cardiopulmonary reserve but are nonspecific comorbidity modifiers. Vaccination, nutrition and moderate activity should follow general neuromuscular-care principles rather than MFM-specific evidence.

## 6. Mechanism and pathophysiology

The principal causal chain is:

**pathogenic variant → unstable/misfolded or dysfunctional Z-disc/intermediate-filament protein → impaired sarcomeric force transmission and proteostasis → Z-disc streaming and myofibrillar dissolution → recruitment of chaperones, ubiquitin and structural proteins into aggregates → autophagic/UPS overload, mitochondrial and energetic dysfunction → myofiber degeneration, fibrosis and progressive weakness.** Cardiac involvement follows an analogous chain in cardiomyocytes, with conduction-system disease or arrhythmogenic remodeling in susceptible genotypes. (olive2021246thenmcinternational pages 1-6, wadmore2021theroleof pages 1-2)

Upstream events are variant-dependent protein dysfunction and mechanical instability. Intermediate processes include protein misfolding, aggregate formation and failure of **CASA/aggrephagy**, involving BAG3, HSPB8/HSPA, DNAJB6, SQSTM1/p62 and autophagy machinery. Downstream lesions include vacuolization, mitochondrial injury, fiber loss and fibrosis. Suggested GO terms include Z-disc organization/sarcomere organization (GO:0045214), protein folding (GO:0006457), response to unfolded protein (GO:0006986), autophagy (GO:0006914), selective autophagy (GO:0061919), ubiquitin-dependent protein catabolism (GO:0006511), mitochondrial organization (GO:0007005) and oxidative phosphorylation (GO:0006119).

Proteomic work has shown that aggregates contain many proteins beyond the mutant protein, supporting a shared secondary aggregate proteome. However, disease-specific single-cell atlases, spatial transcriptomics, lipidomics and clinically validated metabolomic signatures remain sparse. Immune inflammation is not considered the initiating mechanism, although secondary inflammatory responses may accompany degeneration.

## 7. Anatomical structures affected

The primary site is **skeletal muscle tissue** (UBERON:0001134), involving skeletal myofibers (CL:0000188), often bilaterally but sometimes asymmetrically. Distribution varies by genotype and may emphasize distal lower limbs, proximal girdles, paraspinal muscles, neck, diaphragm (UBERON:0001103) or facial/bulbar musculature. Secondary/parallel targets are heart (UBERON:0000948), cardiomyocytes (CL:0000746), respiratory musculature and, in mixed phenotypes, peripheral nerves and Schwann cells.

Relevant subcellular compartments are Z-disc (GO:0030018), myofibril (GO:0030016), sarcomere (GO:0030017), intermediate filament (GO:0005882), protein-containing aggregate (GO:0061702), autophagosome (GO:0005776), lysosome (GO:0005764) and mitochondrion (GO:0005739).

## 8. Temporal development

The usual course is chronic, insidious and progressive. Adult-onset disease may advance over decades; severe childhood BAG3 disease can progress rapidly. Early stages feature focal distal or proximal weakness, cramps or exercise limitation. Intermediate disease brings generalized, axial or bulbar weakness and orthopedic deformity. Advanced disease may include loss of ambulation, ventilatory dependence, cardiomyopathy, conduction block or transplantation. Sustained spontaneous remission is not characteristic. Critical intervention windows are before irreversible respiratory decompensation or malignant arrhythmia, supporting surveillance from diagnosis rather than symptom-triggered testing alone. (olive2021246thenmcinternational pages 6-10, luo2019characterizationofchinese pages 6-7)

## 9. Inheritance and population

MFM is rare, but robust population prevalence and incidence per 100,000 are unavailable. Referral cohorts cannot establish population epidemiology. Both sexes are affected in autosomal disease; sex effects arise in X-linked FHL1-related disease. Most classic disease is autosomal dominant with variable, age-dependent penetrance; recessive and X-linked subtypes occur. Expressivity is markedly variable, even within families. Anticipation is not established. Germline mosaicism is theoretically possible in apparently de novo disease but is not a defining feature. Founder variants exist in individual populations, yet no universal carrier frequency can be stated.

## 10. Diagnostics

A practical workflow is:

1. **Phenotyping:** three-generation pedigree; distribution of weakness; CK; ECG, echocardiography and ambulatory rhythm monitoring; spirometry sitting and supine, maximal inspiratory pressure and sleep assessment; EMG/NCS.
2. **Muscle MRI:** identifies selective fatty replacement, guides biopsy and can support a genotype hypothesis.
3. **Genomics:** a comprehensive neuromuscular panel including canonical and overlap genes is generally first-line. Exome or genome sequencing is appropriate when panel testing is negative, with CNV analysis and periodic reanalysis. RNA sequencing from muscle may resolve splice variants. Standard karyotype, FISH and chromosomal microarray have low yield unless syndromic features suggest a structural disorder. Repeat-expansion and mitochondrial testing are differential-directed, not routine MFM tests.
4. **Muscle biopsy:** modified Gomori trichrome may show amorphous/hyaline inclusions and rimmed vacuoles; immunohistochemistry commonly demonstrates desmin, myotilin, αB-crystallin, ubiquitin/p62 and genotype-related proteins; electron microscopy shows Z-line streaming and granulofilamentous material. Biopsy can establish the pattern but cannot reliably identify the gene. (luo2019characterizationofchinese pages 6-7, olive2005myotilinopathyrefiningthe pages 1-2, olive2021246thenmcinternational pages 1-6)

Important differentials include sporadic inclusion-body myositis, immune-mediated necrotizing myopathy, Pompe disease, myotonic dystrophy, GNE myopathy, VCP multisystem proteinopathy, muscular dystrophies, nemaline/core myopathies, hereditary motor neuropathy and TTN-related hereditary myopathy with early respiratory failure.

Cascade genetic testing is appropriate after identification of a pathogenic familial variant. MFM is not included in routine newborn screening; prenatal or preimplantation testing is technically possible for a known familial pathogenic variant after counseling.

## 11. Outcome and prognosis

No reliable five- or ten-year survival estimate exists for MFM as a group. Prognosis depends on genotype, age at onset, respiratory involvement and cardiac phenotype. Cardiac conduction disease, ventricular arrhythmia, restrictive/dilated cardiomyopathy and respiratory failure are the major potentially fatal complications. DES and BAG3 disease may require pacing, defibrillation, ventilation or transplantation. In the 18-person Chinese cohort, **3 of 8 DES-associated patients required pacemakers**, illustrating the clinical importance of rhythm surveillance. (luo2019characterizationofchinese pages 6-7)

Recovery of lost muscle is generally limited because the disease is degenerative. Rehabilitation may maintain function but does not reverse the molecular lesion. No validated circulating prognostic biomarker is established; genotype, serial pulmonary function, rhythm monitoring, ventricular function, ambulation and swallowing status remain the most actionable predictors.

## 12. Treatment and current implementation

There is no approved MFM-specific pharmacotherapy, gene therapy, ASO, siRNA or cell therapy. The 2017 review’s abstract stated plainly: **“Currently no treatment is available.”** Current care remains multidisciplinary and genotype-informed. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2)

* Physiotherapy and low-to-moderate individualized aerobic/strength activity, avoiding overwork injury; occupational therapy, orthoses, mobility aids and fall prevention. Suggested NCIt: Physical Therapy, Occupational Therapy, Orthotic Device and Assistive Device.
* Noninvasive ventilation, cough augmentation and vaccination/rapid treatment of respiratory infections when respiratory weakness develops. Suggested NCIt: Ventilatory Support.
* Guideline-directed cardiomyopathy therapy; pacemaker for conduction disease, ICD for arrhythmic risk and heart transplantation in selected end-stage cases. Suggested NCIt: Cardiac Pacing, Implantable Cardioverter Defibrillator Placement and Heart Transplantation. (olive2021246thenmcinternational pages 6-10, batonnetpichon2017myofibrillarmyopathiesnew pages 1-2)
* Swallowing assessment, texture modification, nutritional support and gastrostomy when necessary.
* Pain, contracture, scoliosis and psychosocial management.

No treatment-response percentage is defensible because controlled MFM therapeutic trials are lacking. Experimental directions include allele-selective silencing for dominant toxic variants, enhancement of CASA/autophagy, chemical chaperones, aggregate clearance and correction of mitochondrial dysfunction. Dominant-negative/toxic gain-of-function mechanisms make simple gene addition less suitable than for recessive loss-of-function disease. A 2024 authoritative review emphasizes RNA-interference and viral tools as increasingly plausible platforms for dominant muscle disorders, but MFM translation remains preclinical. (findlay2024dominantlyinheritedmuscle pages 8-9)

## 13. Prevention

Primary prevention is not possible after conception except through reproductive options. Genetic counseling should address autosomal-dominant 50% transmission risk where applicable, variable penetrance, de novo disease and subtype-specific inheritance. Preimplantation genetic testing or prenatal diagnosis can be offered for a confirmed familial pathogenic variant.

Secondary prevention comprises cascade testing and presymptomatic cardiac/respiratory surveillance. Tertiary prevention includes early ventilation, rhythm treatment, fall prevention, contracture management, aspiration precautions and rehabilitation. There is no disease-specific vaccine, prophylactic drug or population screening program.

## 14. Other species and natural disease

Orthologs of DES, FLNC, CRYAB, BAG3 and other MFM genes are deeply conserved across vertebrates and many invertebrates. Nevertheless, well-validated naturally occurring veterinary homologs are much less established than induced laboratory models, and MFM is not zoonotic or transmissible.

Commercial claims of equine “MFM” require particular caution. A 2023 Quarter Horse study found no MFM histopathology and no association of marketed MYOT/FLNC/MYOZ3 variants with PSSM2; therefore, these tests should not be extrapolated to human MFM or treated as validated natural-disease models.

## 15. Model organisms and advanced technologies

Mouse knock-in/transgenic models, zebrafish, Drosophila and cultured muscle systems reproduce varying combinations of aggregate formation, Z-disc disruption, weakness, cardiomyopathy and defective autophagy. They are useful for temporal mechanistic analysis and therapy screening, but overexpression models may exaggerate aggregate toxicity and rarely reproduce the full human age-dependent multisystem course. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2, olive2021246thenmcinternational pages 30-34)

Drosophila expression of disease-associated CRYAB variants produces myofibrillar disruption and cardiac abnormalities, supporting evolutionary conservation of sarcomeric proteostasis. Zebrafish provide rapid imaging of muscle architecture and have been used to study FLNC/BAG3-associated autophagy defects. Mouse DES/CRYAB models better approximate mammalian cardiac and skeletal physiology but differ in lifespan and loading.

Patient-derived and gene-edited induced-pluripotent-stem-cell cardiomyocytes are an important recent implementation. Human models permit isogenic comparison, contractility testing and mitochondrial phenotyping but remain developmentally immature. These systems are particularly valuable for variant-specific dominant disease and personalized therapeutic screening.

## Recent developments and evidence limitations

The 2024 literature increasingly frames MFM as a convergence of **mechanical Z-disc injury, dominant protein toxicity and failed proteostasis**, rather than a passive storage disorder. Dominantly inherited FLNC disease was reviewed as typically adult-onset and slowly progressive, with grip weakness followed by ankle plantar-flexion weakness in a recognized phenotype. (findlay2024dominantlyinheritedmuscle pages 8-9)

The principal limitations are the absence of population registries, small genotype-specific cohorts, inconsistent historical use of “MFM,” incomplete molecular diagnosis and lack of randomized trials. Exact PMID metadata was not available for every retrieved source; DOI URLs and publication dates are therefore supplied below rather than inventing identifiers.

### Key sources

* Olivé M, et al. **246th ENMC International Workshop: Protein aggregate myopathies.** *Neuromuscular Disorders*. Published February 2021. https://doi.org/10.1016/j.nmd.2020.11.003 (olive2021246thenmcinternational pages 6-10, olive2021246thenmcinternational pages 1-6)
* Batonnet-Pichon S, et al. **Myofibrillar Myopathies: New Perspectives from Animal Models to Potential Therapeutic Approaches.** *Journal of Neuromuscular Diseases*. Published February 2017. https://doi.org/10.3233/JND-160203 (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2)
* Wadmore K, et al. **The Role of Z-disc Proteins in Myopathy and Cardiomyopathy.** *International Journal of Molecular Sciences*. Published March 2021. https://doi.org/10.3390/ijms22063058 (wadmore2021theroleof pages 1-2)
* Olivé M, et al. **Myotilinopathy: refining the clinical and myopathological phenotype.** *Brain*. Published October 2005. https://doi.org/10.1093/brain/awh576 (olive2005myotilinopathyrefiningthe pages 1-2)
* Findlay AR. **Dominantly inherited muscle disorders: understanding their complexity and exploring therapeutic approaches.** *Disease Models & Mechanisms*. Published October 2024. https://doi.org/10.1242/dmm.050720 (findlay2024dominantlyinheritedmuscle pages 8-9)

**Knowledge-base interpretation:** MFM should be represented as a parent protein-aggregate myopathy linked to gene-defined child diseases, not as one uniform Mendelian entity. Frequencies, inheritance, prognosis and surveillance should be attached to the molecular subtype whenever possible.

References

1. (batonnetpichon2017myofibrillarmyopathiesnew pages 1-2): Sabrina Batonnet-Pichon, Anthony Behin, Eva Cabet, Florence Delort, Patrick Vicart, and Alain Lilienbaum. Myofibrillar myopathies: new perspectives from animal models to potential therapeutic approaches. Journal of Neuromuscular Diseases, 4:1-15, Feb 2017. URL: https://doi.org/10.3233/jnd-160203, doi:10.3233/jnd-160203. This article has 55 citations and is from a peer-reviewed journal.

2. (olive2021246thenmcinternational pages 1-6): Montse Olivé, Lilli Winter, Dieter O. Fürst, Rolf Schröder, Anthony Behin, Alexandra Breukel, Matthias Brumhard, Robert Bryson-Richardson, Kristl Claeys, Ana Ferreiro, Dieter Fürst, Hans H. Goebel, Vandana Gupta, Rudolf Kley, Ami Mankodi, Satoru Noguchi, Anders Oldfors, Montse Olivé, Rolf Schröder, Duygu Selcen, Vincent Timmerman, Bjarne Udd, Maggie Walter, Conrad Weihl, Gerhard Wiche, and Lilly Winter. 246th enmc international workshop: protein aggregate myopathies 24–26 may 2019, hoofddorp, the netherlands. Neuromuscular Disorders, 31(2):158-166, Feb 2021. URL: https://doi.org/10.1016/j.nmd.2020.11.003, doi:10.1016/j.nmd.2020.11.003. This article has 14 citations and is from a peer-reviewed journal.

3. (olive2021246thenmcinternational pages 6-10): Montse Olivé, Lilli Winter, Dieter O. Fürst, Rolf Schröder, Anthony Behin, Alexandra Breukel, Matthias Brumhard, Robert Bryson-Richardson, Kristl Claeys, Ana Ferreiro, Dieter Fürst, Hans H. Goebel, Vandana Gupta, Rudolf Kley, Ami Mankodi, Satoru Noguchi, Anders Oldfors, Montse Olivé, Rolf Schröder, Duygu Selcen, Vincent Timmerman, Bjarne Udd, Maggie Walter, Conrad Weihl, Gerhard Wiche, and Lilly Winter. 246th enmc international workshop: protein aggregate myopathies 24–26 may 2019, hoofddorp, the netherlands. Neuromuscular Disorders, 31(2):158-166, Feb 2021. URL: https://doi.org/10.1016/j.nmd.2020.11.003, doi:10.1016/j.nmd.2020.11.003. This article has 14 citations and is from a peer-reviewed journal.

4. (luo2019characterizationofchinese pages 6-7): Yue-Bei Luo, Yuyao Peng, Yuling Lu, Qiuxiang Li, Huiqian Duan, Fangfang Bi, and Huan Yang. Characterization of chinese patients with myofibrillar myopathy from a single center: expanding the clinico-genetic spectrum. ArXiv, Nov 2019. URL: https://doi.org/10.21203/rs.2.17905/v1, doi:10.21203/rs.2.17905/v1. This article has 0 citations.

5. (olive2005myotilinopathyrefiningthe pages 1-2): Montse Olivé, Lev G. Goldfarb, Alexey Shatunov, Dirk Fischer, and Isidro Ferrer. Myotilinopathy: refining the clinical and myopathological phenotype. Brain : a journal of neurology, 128 Pt 10:2315-26, Oct 2005. URL: https://doi.org/10.1093/brain/awh576, doi:10.1093/brain/awh576. This article has 172 citations.

6. (wadmore2021theroleof pages 1-2): Kirsty Wadmore, Amar J. Azad, and Katja Gehmlich. The role of z-disc proteins in myopathy and cardiomyopathy. International Journal of Molecular Sciences, 22:3058, Mar 2021. URL: https://doi.org/10.3390/ijms22063058, doi:10.3390/ijms22063058. This article has 75 citations.

7. (findlay2024dominantlyinheritedmuscle pages 8-9): Andrew R. Findlay. Dominantly inherited muscle disorders: understanding their complexity and exploring therapeutic approaches. Disease Models & Mechanisms, Oct 2024. URL: https://doi.org/10.1242/dmm.050720, doi:10.1242/dmm.050720. This article has 9 citations and is from a domain leading peer-reviewed journal.

8. (olive2021246thenmcinternational pages 30-34): Montse Olivé, Lilli Winter, Dieter O. Fürst, Rolf Schröder, Anthony Behin, Alexandra Breukel, Matthias Brumhard, Robert Bryson-Richardson, Kristl Claeys, Ana Ferreiro, Dieter Fürst, Hans H. Goebel, Vandana Gupta, Rudolf Kley, Ami Mankodi, Satoru Noguchi, Anders Oldfors, Montse Olivé, Rolf Schröder, Duygu Selcen, Vincent Timmerman, Bjarne Udd, Maggie Walter, Conrad Weihl, Gerhard Wiche, and Lilly Winter. 246th enmc international workshop: protein aggregate myopathies 24–26 may 2019, hoofddorp, the netherlands. Neuromuscular Disorders, 31(2):158-166, Feb 2021. URL: https://doi.org/10.1016/j.nmd.2020.11.003, doi:10.1016/j.nmd.2020.11.003. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Myofibrillar_Myopathy-deep-research-falcon_artifacts/artifact-00.md)