---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-08-22T19:29:35.542176'
end_time: '2026-08-22T19:29:35.547316'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RFT1-congenital disorder of glycosylation
  mondo_id: MONDO:0012783
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: RFT1-congenital_disorder_of_glycosylation-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RFT1-congenital disorder of glycosylation
- **MONDO ID:** MONDO:0012783 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RFT1-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** RFT1-congenital disorder of glycosylation
- **MONDO ID:** MONDO:0012783 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RFT1-congenital disorder of glycosylation** covering all of the
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


# RFT1-congenital disorder of glycosylation: comprehensive disease-characteristics report

## Executive summary

RFT1-congenital disorder of glycosylation (RFT1-CDG; historical **CDG-In**) is an ultra-rare, autosomal-recessive disorder of endoplasmic-reticulum (ER) protein N-glycosylation caused by biallelic pathogenic variants in **RFT1**. The best-established phenotype is congenital/early-infantile, predominantly neurologic disease comprising severe developmental impairment, hypotonia, epilepsy, feeding failure, visual dysfunction, and particularly sensorineural hearing loss. Respiratory insufficiency, coagulopathy/thrombosis, microcephaly, brain atrophy, gastrointestinal problems, and occasional hepatomegaly are variable. Published evidence is based on individual patients and very small case series—not EHR-scale cohorts—so percentages, incidence, survival estimates, and genotype–phenotype relationships remain unreliable. Early literature counted six patients in 2009; a 2021 neurological review reported only 11 described patients. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7, paprocka2021congenitaldisordersof pages 14-15)

The cellular hallmark is accumulation of **Man5GlcNAc2-PP-dolichol (M5-DLO)**, reduced mature Glc3Man9GlcNAc2-PP-dolichol, and protein hypoglycosylation. Although RFT1 was initially called the M5-DLO “flippase,” biochemical reconstitution, an Rft1-null *Trypanosoma brucei* model, and 2024 molecular work show that the actual transbilayer scramblase remains unidentified; RFT1 may instead facilitate M5-DLO presentation, chaperoning, or conversion to mature DLO. (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3, a2008humanrft1deficiency pages 4-5, jelk2013glycoproteinbiosynthesisin pages 1-2)

No disease-modifying therapy, approved gene therapy, or RFT1-specific clinical trial was identified. Current care is supportive, with molecular diagnosis enabling recurrence-risk counseling, carrier testing, prenatal diagnosis, and preimplantation genetic testing.

| domain | high-confidence finding | quantitative/detail | evidence type | suggested ontology terms |
|---|---|---|---|---|
| Disease identity | RFT1-congenital disorder of glycosylation is a rare congenital disorder of N-linked glycosylation caused by RFT1 deficiency | Supported IDs: MONDO:0012783; OMIM disease 612015; historical nomenclature proposed as CDG-In in 2008 literature (OpenTargets Search: RFT1-congenital disorder of glycosylation-RFT1, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2) | Disease ontology/resource linkage + human primary literature | Suggested: MONDO:0012783 |
| Causal gene / inheritance | Causal gene is RFT1; inheritance is autosomal recessive | RFT1 gene OMIM 611908; biallelic pathogenic variants reported in affected individuals; homozygous and compound heterozygous missense alleles documented (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 1-3, jaeken2009rft1cdgdeafnessas pages 1-4) | Human clinical genetics + functional complementation | Suggested: HGNC RFT1; GENO autosomal recessive inheritance |
| Pathogenic variants | Recurrently reported disease-associated missense variants include p.R67C, p.K152E, p.E298K, p.I296K, p.I296R; additional variants were examined functionally in 2024 molecular work | c.199C>T (p.R67C), c.454A>G (p.K152E), c.892G>A (p.E298K), c.887T>A (p.I296K), c.887T>G (p.I296R); most reported variants are missense and map to conserved regions (vleugels2009rft1deficiencyin pages 4-6, jaeken2009rft1cdgdeafnessas pages 4-7, hirata2024molecularcharacterizationof pages 1-3, hirata2024molecularcharacterizationof pages 35-37) | Human case reports/series + yeast functional assays | Suggested: SO:0001583 missense_variant |
| Core phenotype | Severe neurodevelopmental disease is the dominant presentation | Common findings across early reported patients: severe developmental delay/intellectual disability, hypotonia, seizures/epilepsy, feeding problems/failure to thrive, visual impairment, microcephaly, and sensorineural hearing loss (vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4) | Human case series | Suggested HPO: HP:0001263 developmental delay; HP:0001252 hypotonia; HP:0001250 seizures; HP:0001508 failure to thrive; HP:0000252 microcephaly; HP:0000407 sensorineural hearing impairment; HP:0000505 visual impairment |
| Distinguishing phenotype | Sensorineural deafness is a notable and repeatedly emphasized feature | Early literature reported deafness in all 4 initially compared patients and later described RFT1-CDG as the first CDG firmly associated with deafness; by 2021 review, 11 patients had been described in the literature (vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4) | Human case series + review summary | Suggested HPO: HP:0000407 sensorineural hearing impairment |
| Additional/variable phenotypes | Other features are variable rather than universal | Respiratory insufficiency, pulmonary infections, coagulopathy, hepatomegaly, nystagmus, stroke-like episodes, venous thrombosis, brisk reflexes, dysmorphy, and gastrointestinal problems reported in subsets of patients (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 1-3, jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4) | Human case reports | Suggested HPO: HP:0002093 respiratory insufficiency; HP:0003256 thrombosis; HP:0012379 abnormal coagulation; HP:0000622 nystagmus |
| Onset / course | Typical onset is congenital or infantile, with severe early course but some longer-term survival | One reported patient died at 8 months; severe infantile presentations are common, but adult survivors with milder intellectual disability have been noted in cohort/review literature (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 6-7) | Human longitudinal case observation + cohort review | Suggested HPO: HP:0003577 congenital onset; HP:0011463 childhood onset |
| Diagnostic screening biomarker | Serum transferrin testing shows a type I hypoglycosylation pattern | Capillary zone electrophoresis / serum sialotransferrin type 1 pattern reported; generalized CDG guidance still considers transferrin IEF a first-line test for many N-glycosylation disorders (vleugelsUnknownyearcharacterizationofnovel pages 93-96, jaeken2009rft1cdgdeafnessas pages 1-4) | Human biochemical diagnostics + CDG practice review | Suggested LOINC class: transferrin glycoform analysis; Suggested HPO: HP:0012345 abnormal glycosylation test |
| Disease-specific biochemical hallmark | Cells accumulate incomplete dolichol-linked oligosaccharide intermediate M5-DLO / DolPP-GlcNAc2Man5 | Patient fibroblasts showed accumulation of DolPP-GlcNAc2Man5 / Man5GlcNAc2-PP-dolichol with reduced full-length Glc3Man9GlcNAc2-PP-dolichol and hypoglycosylation (vleugels2009rft1deficiencyin pages 4-6, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2) | Human cellular biochemistry | Suggested CHEBI: dolichol-linked oligosaccharide terms; Suggested GO: protein N-linked glycosylation |
| Functional confirmation | Wild-type RFT1 rescues the cellular defect | Lentiviral expression of normal RFT1 cDNA in patient fibroblasts restored synthesis of complete LLO and normalized secretion/glycosylation readouts; mutant p.R67C failed in yeast complementation (vleugels2009rft1deficiencyin pages 11-13, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2) | Human patient fibroblasts + yeast complementation | Suggested ECO: functional complementation evidence |
| Mechanism / pathway | RFT1 is an ER membrane protein required for normal assembly of the N-glycosylation donor used in protein N-glycosylation | Upstream defect: impaired handling of M5-DLO in ER membrane biogenesis pathway; downstream effect: depletion of mature donor and protein hypoglycosylation, despite intact downstream glycosyltransferases/OST (hirata2024molecularcharacterizationof pages 1-3, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2) | Human cellular biochemistry + mechanistic primary literature | Suggested GO: GO:0006487 protein N-linked glycosylation; GO:0005783 endoplasmic reticulum |
| Mechanistic uncertainty | Whether RFT1 is itself the M5-DLO flippase/scramblase remains unresolved | 2013 Trypanosoma work found Rft1-null cells retained significant N-glycosylation and normal steady-state mature DLO; 2024 work found Rft1-depleted proteoliposomes had undiminished M5-DLO scramblase activity and concluded any such activity by Rft1 would be minor/redundant (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3, jelk2013glycoproteinbiosynthesisin pages 1-2) | Model-organism and reconstitution studies | Suggested GO: lipid translocation; GO: endoplasmic reticulum membrane |
| Protein features | Human Rft1 is a multispanning ER membrane protein with cytoplasmic N- and C-termini and is not N-glycosylated | 2024 molecular characterization predicted 14 transmembrane spans; Nin/Cin topology supported experimentally; N227 sequon is in a cytoplasmic loop and not glycosylated (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3) | Yeast reporter system + structural prediction + topology assays | Suggested GO: GO:0016021 integral component of membrane; GO:0005789 endoplasmic reticulum membrane |
| Anatomical systems affected | Nervous system involvement is primary; multisystem involvement occurs secondarily/variably | Brain/neurodevelopmental, auditory, visual, respiratory, coagulation/vascular, and possibly hepatic systems affected in reported patients (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7) | Human phenotype aggregation | Suggested UBERON: brain, inner ear, eye, liver; Suggested CL: neuron |
| Models | Useful models include yeast complementation systems, patient fibroblasts, and Rft1-null Trypanosoma brucei | Yeast shows essentiality and supports human RFT1 rescue assays; patient fibroblasts recapitulate M5-DLO accumulation; Trypanosoma null model challenges simple flippase assignment (vleugels2009rft1deficiencyin pages 11-13, a2008humanrft1deficiency pages 4-5, jelk2013glycoproteinbiosynthesisin pages 1-2) | In vitro cellular + model organism | Suggested NCBITaxon: Saccharomyces cerevisiae, Trypanosoma brucei; Suggested CL: fibroblast |
| Diagnostics in practice | Best-supported diagnostic approach is biochemical screening followed by molecular confirmation of biallelic RFT1 variants | Real-world implementation: transferrin glycoform testing, LLO analysis in specialized settings, and exome/genome/panel-based confirmation; hearing evaluation such as brainstem audiometry has been informative clinically (vleugelsUnknownyearcharacterizationofnovel pages 93-96, jaeken2009rft1cdgdeafnessas pages 1-4) | Clinical diagnostic workflow | Suggested NCIT: Genetic Testing; Suggested HPO: HP:0000407 sensorineural hearing impairment |
| Treatment status | No disease-specific approved therapy identified; management is supportive/symptomatic | Symptomatic seizure management reported (e.g., valproic acid in one case); no RFT1-specific interventional trials identified in the trial search performed here (jaeken2009rft1cdgdeafnessas pages 1-4) | Human case management + trial search negative finding | Suggested NCIT: Supportive Care; Anticonvulsant Therapy |
| Prevention / counseling | Prevention is genetic rather than environmental | Autosomal recessive inheritance supports carrier testing, reproductive counseling, prenatal or preimplantation testing when familial variants are known; no environmental protective factors established (vleugels2009rft1deficiencyin pages 1-3, jaeken2009rft1cdgdeafnessas pages 1-4) | Genetic counseling inference from Mendelian etiology | Suggested NCIT: Genetic Counseling |
| Epidemiology | Extremely rare; precise prevalence/incidence are not established from direct patient registries | Literature review noted only 11 described patients by 2021 review context; broader 2021 prevalence study emphasizes that most non-PMM2 N-linked CDGs are expected to be rarer than 1 in 100,000 and that estimates for specific rare CDGs are uncertain (paprocka2021congenitaldisordersof pages 14-15, pajusalu2021theestimatedprevalence pages 3-4) | Review summary + population-allele-frequency modeling context | Suggested MONDO rare disease classification |
| Evidence gaps | Major gaps remain in prevalence, genotype-phenotype correlations, natural history, prognosis, and molecular mechanism | No robust disease-specific incidence data, no established modifier/protective factors, no validated prognostic biomarkers, no RFT1-specific treatment trials, and no definitive proof that RFT1 is the M5-DLO flippase (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3, pajusalu2021theestimatedprevalence pages 3-4, jelk2013glycoproteinbiosynthesisin pages 1-2) | Evidence-gap synthesis | Suggested: none; ontology mapping not applicable |
| Source provenance | Evidence comes primarily from aggregated disease-level resources and small patient series rather than EHR-scale datasets | High-confidence claims rely on a handful of primary human case reports/series and mechanistic model studies; not from large observational databases (vleugels2009rft1deficiencyin pages 4-6, jaeken2009rft1cdgdeafnessas pages 4-7, hirata2024molecularcharacterizationof pages 1-3) | Evidence characterization | Suggested ECO: case report evidence; experimental evidence |


*Table: This compact table summarizes high-confidence disease knowledge for RFT1-CDG across identifiers, genetics, phenotype, mechanism, diagnostics, models, treatment status, and evidence gaps. It is structured for direct knowledge-base ingestion and labels ontology mappings as suggested rather than asserted.*

## 1. Disease information

### Definition and classification

RFT1-CDG is a Mendelian inborn error of metabolism affecting assembly of the lipid-linked oligosaccharide donor required for N-linked protein glycosylation in the ER. The initial report demonstrated that a homozygous **RFT1** variant caused intracellular DolPP-GlcNAc2Man5 accumulation and profound glycosylation dysfunction, and proposed the historical name **CDG-In**. (a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2)

**Identifiers and names**

- **MONDO:** MONDO:0012783.
- **OMIM disease:** **612015**.
- **Causal gene:** **RFT1**, OMIM **611908**; Ensembl ENSG00000163933; approved name “RFT1 glycolipid translocator homolog.” Open Targets gives RFT1 the strongest disease association among listed targets (score 0.816); weaker associations to other CDG genes reflect shared pathway/disease annotations rather than additional causes of RFT1-CDG. (OpenTargets Search: RFT1-congenital disorder of glycosylation-RFT1, vleugels2009rft1deficiencyin pages 1-3)
- **Synonyms:** RFT1-CDG; RFT1 deficiency; congenital disorder of glycosylation type In; CDG-In; RFT1-related congenital disorder of glycosylation.
- **Orphanet:** a disease-specific ORPHA number was not verified in the retrieved evidence.
- **ICD-10/ICD-11:** no uniquely specific disease code was verified; cases are generally coded under congenital disorders of glycoprotein metabolism/other specified metabolic disorders.
- **MeSH:** no disease-specific MeSH descriptor was verified; broader terms include congenital disorders of glycosylation and glycoprotein-metabolism disorders.

**Evidence provenance:** chiefly aggregated disease resources plus patient-level case reports, pedigrees, fibroblast studies, and model systems. No disease registry or population-scale EHR study was found.

## 2. Etiology, risk, and protective factors

The cause is **germline biallelic loss or severe reduction of RFT1 function**. Both homozygous and compound-heterozygous missense genotypes have been reported, with autosomal-recessive segregation. Functional causality was shown by failure of mutant p.Arg67Cys to complement Rft1-deficient yeast and restoration of normal lipid-linked oligosaccharide profiles after wild-type RFT1 expression in patient fibroblasts. (vleugels2009rft1deficiencyin pages 1-3, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2)

Genetic risk is therefore determined by parental carrier status. Consanguinity occurred in Italian and Algerian families, increasing the probability of homozygosity, but affected children have also been born to unrelated parents. No susceptibility loci, validated modifier genes, protective alleles, epigenetic risk factors, environmental triggers, infections, toxins, diet, sex, or lifestyle effects have been established. (vleugels2009rft1deficiencyin pages 4-6, jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4)

There is no demonstrated gene–environment interaction. Intercurrent infection, feeding difficulty, or respiratory stress may worsen clinical status, but these are complications rather than proven causes or modifiers.

## 3. Phenotypes and quality-of-life effects

Because cohorts are tiny and overlapping, early frequencies should not be treated as stable population estimates. In the first four compared patients, hearing loss was 4/4; by 2009, six patients were described with a highly consistent neurologic syndrome. (vleugelsUnknownyearcharacterizationofnovel pages 93-96, vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7)

### Core manifestations

- **Global developmental delay/intellectual disability**—usually severe or profound, beginning in infancy; sometimes described as psychomotor retardation. This substantially limits mobility, communication, education, and independent living. Suggested HPO: **HP:0001263**, **HP:0001249**. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 6-7)
- **Hypotonia**—often marked or “extreme,” neonatal/infantile, contributing to respiratory and feeding dysfunction. Suggested HPO: **HP:0001252**. (jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4)
- **Epilepsy**—early-onset seizures, infantile spasms, myoclonic jerks, or polymorphic seizures; frequently drug-resistant, although one reported child’s seizures were controlled with valproate. Suggested HPO: **HP:0001250**, **HP:0001257**, **HP:0002123**. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 1-4)
- **Sensorineural hearing impairment**—bilateral, often severe, demonstrable by brainstem evoked-response audiometry. Early authors concluded that “hearing loss belongs to the phenotype of RFT1-CDG,” calling it the first CDG firmly associated with deafness. It further restricts language acquisition and communication. Suggested HPO: **HP:0000407**. (vleugelsUnknownyearcharacterizationofnovel pages 93-96, jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4)
- **Feeding problems/failure to thrive**—infantile feeding difficulty and poor growth are common; severe cases may require intensive nutritional support. Suggested HPO: **HP:0011968**, **HP:0001508**. (vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7)
- **Visual dysfunction**—poor visual contact, reduced visual acuity, nystagmus, and occasional glaucoma. Suggested HPO: **HP:0000505**, **HP:0000639**, **HP:0000622**, **HP:0000501**. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 6-7)
- **Microcephaly/brain atrophy**—microcephaly is variable; progressive cortical and subcortical atrophy has been reported. Suggested HPO: **HP:0000252**, **HP:0002120**. (vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7)

### Variable multisystem findings

Respiratory insufficiency, apnea, recurrent pulmonary infection, gastrointestinal symptoms, hepatomegaly, abnormal coagulation factors, deep-venous thrombosis, stroke-like episodes, brisk reflexes, and dysmorphism occur in subsets. One patient had reduced factor XI, protein C, and antithrombin; thrombosis was reported as early as four months in one case. Suggested HPO terms include **HP:0002093** respiratory insufficiency, **HP:0002105** apnea, **HP:0002240** hepatomegaly, **HP:0012379** abnormal coagulation, **HP:0002625** deep venous thrombosis, and **HP:0001297** stroke-like episode. (vleugels2009rft1deficiencyin pages 4-6, vleugelsUnknownyearcharacterizationofnovel pages 93-96, jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4)

No validated RFT1-CDG-specific quality-of-life instrument, EQ-5D, SF-36, PROMIS dataset, or quantitative caregiver-burden study was found. Severe neurologic, auditory, visual, respiratory, and feeding impairments imply major lifelong effects, but this remains clinically inferred rather than formally measured.

## 4. Genetic and molecular information

### Gene and variant spectrum

RFT1-CDG is a single-gene disorder. Well-documented variants include:

- **NM-level c.199C>T, p.Arg67Cys (R67C)**—homozygous in the first reported patient; functionally deficient in yeast and rescued by wild-type RFT1 in fibroblasts.
- **c.454A>G, p.Lys152Glu (K152E)**—reported homozygously.
- **c.892G>A, p.Glu298Lys (E298K)**—reported homozygously.
- **c.887T>A, p.Ile296Lys (I296K)** and **c.887T>G, p.Ile296Arg (I296R)**—reported in compound heterozygosity.
- Later functional work also examined reported substitutions including p.Cys70Arg, p.Gly276Asp, p.Tyr301Cys, and p.Gly340Ser. (vleugels2009rft1deficiencyin pages 4-6, vleugelsUnknownyearcharacterizationofnovel pages 96-98, jaeken2009rft1cdgdeafnessas pages 4-7, hirata2024molecularcharacterizationof pages 35-37, a2008humanrft1deficiency pages 1-2)

Most reported alleles are missense variants affecting conserved residues. The 2024 structure/topology study found that most disease variants map to highly conserved regions, many near a central hydrophilic cavity. Variant classification should nevertheless be checked against the current ClinVar record using the exact transcript and genome build; the retrieved literature predates modern uniform ACMG/AMP classification. Population allele frequencies were not reliably available in the retrieved evidence and should not be inferred as zero. (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3)

The variants are **germline**, not somatic. The likely mechanism is loss/reduction of function; dominant-negative or gain-of-function mechanisms are unsupported. No disease-causing chromosomal rearrangement, repeat expansion, mitochondrial variant, epimutation, or recurrent copy-number change was identified. No validated modifier gene or disease-specific methylation signature is known.

## 5. Environmental information

No toxin, radiation, pollution, occupation, smoking, alcohol, diet, exercise pattern, or infectious agent is known to cause RFT1-CDG. It is not contagious and has no zoonotic transmission. Environmental interventions cannot prevent disease occurrence in an individual who has inherited a pathogenic biallelic genotype, although good nutrition, vaccination, infection prevention, aspiration precautions, and respiratory care may reduce complications.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic event:** biallelic RFT1 variants reduce functional Rft1 protein.
2. **ER membrane defect:** normal handling of M5-DLO is impaired.
3. **Biochemical lesion:** M5-DLO accumulates while mature Glc3Man9GlcNAc2-DLO becomes relatively depleted.
4. **Glycoprotein consequence:** fewer complete oligosaccharides are available to oligosaccharyltransferase, causing deficient occupancy of N-glycosylation sites and generalized glycoprotein hypoglycosylation.
5. **Cell/tissue consequence:** altered folding, ER quality control, trafficking, secretion, stability, receptor function, and circulating glycoprotein activity plausibly affect developing neurons, auditory pathways, visual system, coagulation proteins, and respiratory/feeding functions.
6. **Clinical outcome:** developmental encephalopathy, epilepsy, hypotonia, deafness, growth failure, sensory impairment, and variable multisystem disease. (hirata2024molecularcharacterizationof pages 1-3, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2)

The 2008 primary-paper abstract states: **“RFT1 deficiency in both yeast and human cells leads to the accumulation of incomplete DolPP-GlcNAc2Man5 and to a profound glycosylation disorder in humans.”** Wild-type RFT1 restored complete DLO synthesis in patient fibroblasts, providing direct functional evidence for this chain. (a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2)

### Current expert interpretation of RFT1 function

The older model assigned Rft1 as an ATP-independent M5-DLO flippase. That label is now uncertain. Rft1-null *T. brucei* retained normal steady-state mature DLO and substantial N-glycosylation despite **30–100-fold** M5-DLO accumulation; the authors concluded that Rft1 is not required for flipping in that organism and may act as an M5-DLO chaperone. Their concise conclusion was: **“The M5-DLO flippase remains to be identified.”** (jelk2013glycoproteinbiosynthesisin pages 1-2)

The 2024 study found that removing Rft1 did not reduce M5-DLO scramblase activity in reconstituted proteoliposomes: approximately 65% of M5-DLO was captured in both Rft1-containing and Rft1-depleted preparations. It concluded that if Rft1 has scramblase activity, it is a minor/redundant contributor. Human Rft1 was characterized as an ER-localized, non-N-glycosylated protein with **14 predicted transmembrane helices** and both termini facing the cytoplasm; its fold resembles the MOP transporter family, but its essential substrate/function remains unresolved. (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3)

Suggested GO annotations: **GO:0006487** protein N-linked glycosylation; **GO:0005783** endoplasmic reticulum; **GO:0005789** ER membrane; **GO:0016021** integral component of membrane; lipid-linked oligosaccharide biosynthetic process and transmembrane lipid transport. Suggested cell terms: **CL:0000057 fibroblast** for demonstrated patient models; neurons, auditory sensory cells, and hepatocytes are biologically plausible targets but have not been directly profiled disease-specifically.

No RFT1-CDG-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or human multi-omics dataset was identified. The disease-defining targeted lipid-glycan profile is accumulation of M5-DLO rather than a validated circulating metabolomic signature. Immune activation, oxidative stress, fibrosis, apoptosis, and epigenetic dysregulation have not been established as primary mechanisms.

## 7. Anatomical structures affected

The **central nervous system** is the primary clinically affected system, with developmental dysfunction and occasional cortical/subcortical atrophy. The **inner ear/auditory pathway** is strongly implicated by bilateral sensorineural deafness. The **eye/visual pathway**, skeletal/respiratory muscle or central respiratory control, gastrointestinal tract, liver, and vascular/coagulation system can be variably involved. No consistent lateralization has been reported. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 6-7, jaeken2009rft1cdgdeafnessas pages 4-7)

Suggested UBERON mappings: brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), inner ear (**UBERON:0001846**), eye (**UBERON:0000970**), liver (**UBERON:0002107**), lung (**UBERON:0002048**), and ER at the subcellular level (**GO:0005783/GO:0005789**). These are suggested knowledge-base mappings, not all experimentally confirmed sites of primary injury.

## 8. Temporal development

Onset is usually congenital, neonatal, or early infantile. Hypotonia, respiratory or feeding difficulty may be evident neonatally; developmental delay, visual/auditory impairment, and seizures emerge during infancy. The course is chronic and lifelong, often severe and sometimes progressive, with brain atrophy, refractory epilepsy, respiratory morbidity, or thrombosis. One North American patient died at eight months; other patients survived through childhood, and adult siblings with milder intellectual disability have been reported, establishing marked variability. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 11-13, vleugels2009rft1deficiencyin pages 6-7)

There is no validated staging system, median progression rate, remission pattern, or critical therapeutic window. Developmental infancy is logically the period of greatest vulnerability, but presymptomatic treatment benefit has not been tested.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous carrier parents, each pregnancy has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability, assuming standard Mendelian segregation. Penetrance for genuinely pathogenic biallelic genotypes appears high, but cannot be quantified; expressivity is variable from lethal neonatal disease to adult survival. Anticipation is not expected. Germline mosaicism has not been specifically reported, although residual recurrence risk remains after apparently de novo findings.

Cases have included Moroccan, Italian, Algerian, North American Scottish-English, and other European backgrounds; this distribution does not establish ethnic predilection. Consanguinity contributed in some families. No founder allele, robust carrier frequency, geographic cluster, or sex bias has been demonstrated. (vleugels2009rft1deficiencyin pages 4-6, jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4)

Precise incidence and prevalence are unknown. A 2021 allele-frequency study examined 27 autosomal-recessive N-glycosylation disorders and concluded that only PMM2-CDG exceeded 1:100,000 in the broad populations assessed; however, its assumptions—ClinVar classification, gnomAD ascertainment, Hardy–Weinberg equilibrium, and exclusion of many structural/regulatory variants—make extrapolation to RFT1-CDG uncertain. Therefore, “ultra-rare” and “fewer than a few dozen published patients” are more defensible than a numeric prevalence. (paprocka2021congenitaldisordersof pages 14-15, pajusalu2021theestimatedprevalence pages 3-4)

## 10. Diagnostics

### Recommended workflow

1. **Clinical suspicion:** infant with unexplained developmental encephalopathy, hypotonia, epilepsy, feeding failure, visual dysfunction, and especially sensorineural deafness.
2. **Biochemical screening:** serum transferrin isoelectric focusing, capillary-zone electrophoresis, HPLC, or mass spectrometry. Reported RFT1-CDG patients show a **type I transferrin pattern**, consistent with deficient glycan-site occupancy. Normal results do not absolutely exclude every CDG and should not override a compelling genomic finding. (vleugelsUnknownyearcharacterizationofnovel pages 93-96, jaeken2009rft1cdgdeafnessas pages 1-4)
3. **Molecular confirmation:** identify pathogenic/likely pathogenic variants on both RFT1 alleles with parental segregation. A comprehensive CDG/epileptic-encephalopathy panel, WES, or WGS is appropriate. Single-gene sequencing plus deletion/duplication analysis is efficient when phenotype and biochemical profile are characteristic.
4. **Functional confirmation for uncertain variants:** patient-fibroblast DLO analysis for M5-DLO accumulation, glycoprotein secretion/glycosylation assays, or validated yeast complementation in a specialist laboratory. Wild-type RFT1 rescue is strong evidence but is a research-level assay. (vleugels2009rft1deficiencyin pages 11-13, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2)

WGS can detect noncoding and structural alleles missed by exome sequencing; RNA-seq may clarify suspected splice variants, but no disease-specific validated RNA diagnostic protocol exists. CMA and karyotyping are low-yield for a sequence-level recessive disorder unless broader syndromic findings suggest a CNV. FISH, mtDNA testing, and repeat-expansion testing are not routine RFT1-CDG tests.

### Clinical assessment after diagnosis

Recommended baseline evaluations include EEG; brain MRI; brainstem auditory evoked responses/audiology; ophthalmology; swallowing and nutritional assessment; respiratory assessment; liver enzymes; albumin; coagulation profile including antithrombin/protein C where available; developmental, physical, occupational, and speech-language evaluation. These recommendations derive from observed complications rather than a formal RFT1-specific guideline. (vleugels2009rft1deficiencyin pages 4-6, vleugelsUnknownyearcharacterizationofnovel pages 93-96, jaeken2009rft1cdgdeafnessas pages 4-7)

### Differential diagnosis

The differential includes PMM2-CDG and other type-I N-glycosylation defects—particularly ALG3-CDG, DPM1-CDG, MPDU1-CDG, ALG11-CDG, and disorders causing developmental epileptic encephalopathy with deafness. M5-DLO accumulation narrows the biochemical differential, but localization and complete DLO/N-glycan profiles plus sequencing distinguish the defects. The original authors noted biochemical/clinical resemblance to ALG3 and DPM1 deficiencies. (a2008humanrft1deficiency pages 4-5)

No population newborn screening program exists. Targeted cascade testing is indicated for relatives after familial variants are established.

## 11. Outcome and prognosis

No 5-year/10-year survival estimates, mortality rate, or formal life-expectancy analysis exists. Prognosis ranges from death in infancy due to severe respiratory/neurologic disease to survival into adulthood. Major long-term morbidity includes profound developmental disability, epilepsy, hearing and visual impairment, feeding dependence, impaired mobility, and respiratory and thrombotic complications. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 11-13, vleugels2009rft1deficiencyin pages 6-7)

No validated prognostic biomarker exists. Residual RFT1 activity and genotype plausibly influence severity, but current numbers are insufficient for clinical prediction. Early respiratory failure, refractory seizures, severe feeding dysfunction, and progressive brain atrophy are clinically concerning, but not statistically validated prognostic factors. Recovery to normal function has not been documented; symptomatic improvement may occur with seizure, nutrition, hearing, and rehabilitation interventions.

## 12. Treatment and current applications

No approved RFT1-directed pharmacotherapy or dietary substrate replacement is available. Management is multidisciplinary and symptom-directed:

- antiseizure medication selected by seizure type and tolerability; valproate controlled seizures in one reported case, but no drug-specific response rate exists;
- enteral nutrition and dysphagia/aspiration management;
- respiratory support, airway clearance, infection treatment, and tracheostomy/ventilation where required;
- hearing aids or cochlear-implant assessment according to audiologic anatomy and function;
- ophthalmologic treatment;
- physical, occupational, feeding, communication, and speech therapy;
- surveillance and standard treatment of coagulation abnormalities or thrombosis;
- management of hepatic, gastrointestinal, orthopedic, and sleep complications as they arise. (vleugels2009rft1deficiencyin pages 4-6, vleugelsUnknownyearcharacterizationofnovel pages 93-96, jaeken2009rft1cdgdeafnessas pages 1-4)

Suggested NCIT mappings include **Supportive Care**, **Anticonvulsant Therapy**, **Enteral Nutrition**, **Physical Therapy**, **Occupational Therapy**, **Speech and Language Therapy**, **Hearing Aid**, **Cochlear Implantation**, **Mechanical Ventilation**, and **Genetic Counseling**. These are intervention annotations, not evidence of RFT1-specific efficacy.

Patient-fibroblast correction by lentiviral wild-type RFT1 provides proof of biological reversibility at the cellular level: complete DLO synthesis and DNase-1 secretion normalized. This is not a clinical gene-therapy result and does not establish safety, CNS delivery, dosing, or patient benefit. No RFT1-specific gene editing, ASO, siRNA, mRNA, cell therapy, immunotherapy, or clinical-stage small molecule was found. (vleugels2009rft1deficiencyin pages 11-13, a2008humanrft1deficiency pages 4-5)

The ClinicalTrials.gov search returned trials for other CDGs, such as PGM1-CDG and PMM2-CDG, but none relevant to RFT1-CDG; these should not be presented as treatment options for this disease.

## 13. Prevention

There is no environmental or pharmacologic primary prevention. **Genetic prevention and early ascertainment** are applicable:

- genetic counseling and parental segregation testing;
- cascade carrier testing in adult relatives;
- prenatal diagnosis by chorionic-villus or amniotic-fluid testing for known familial variants;
- preimplantation genetic testing for monogenic disease;
- early testing of symptomatic siblings and, where desired, newborn familial testing.

Secondary/tertiary prevention focuses on early hearing rehabilitation, seizure control, nutritional support, aspiration prevention, vaccination, respiratory infection reduction, thrombosis awareness, and developmental therapies. Routine immunizations are appropriate unless an unrelated contraindication exists. There is no RFT1-specific vaccine or prophylactic medication.

## 14. Other species and natural disease

No naturally occurring RFT1-CDG-like veterinary disease, affected breed, zoonotic potential, or cross-species transmission was identified. RFT1 function is evolutionarily conserved from yeast to humans; human RFT1 can complement yeast Rft1 deficiency, whereas p.Arg67Cys cannot, supporting conserved biology. (a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2)

Relevant species include *Homo sapiens* (NCBI Taxon 9606), *Saccharomyces cerevisiae* (559292), and *Trypanosoma brucei* (5691). The parasite model is mechanistically informative but does not reproduce the human neurologic syndrome.

## 15. Model organisms and experimental systems

- **Patient-derived fibroblasts:** reproduce M5-DLO accumulation and impaired glycoprotein secretion. Lentiviral wild-type RFT1 restores the biochemical phenotype, making this the most disease-proximal functional model. Limitation: fibroblasts do not model neuronal development, hearing, or whole-organ physiology. (vleugels2009rft1deficiencyin pages 11-13, a2008humanrft1deficiency pages 4-5, a2008humanrft1deficiency pages 1-2)
- **Yeast Rft1-deficient systems:** human wild-type RFT1 supports viability and N-glycosylation; disease variants can be assayed by growth and carboxypeptidase-Y glycosylation. These are useful for variant interpretation and structure–function studies. Limitation: yeast lacks human tissue complexity. (hirata2024molecularcharacterizationof pages 1-3, a2008humanrft1deficiency pages 4-5)
- ***Trypanosoma brucei* Rft1-null model:** null procyclic parasites grow nearly normally, maintain mature DLO and significant N-glycosylation, but accumulate M5-DLO 30–100-fold. This model was decisive in challenging the simple flippase hypothesis. Limitation: early-diverging parasite biology and insect-stage metabolism differ substantially from humans. (jelk2013glycoproteinbiosynthesisin pages 1-2)
- **Proteoliposome/microsome systems:** directly assay M5-DLO scrambling and show activity persists after Rft1 depletion. These isolate membrane transport chemistry but lose intact-cell ER architecture. (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3)

No validated RFT1-CDG mouse, rat, zebrafish, Drosophila, *C. elegans*, organoid, or patient-iPSC model reproducing the human syndrome was identified. Developing neural and inner-ear organoids or conditional mammalian knockouts would be particularly valuable because constitutive RFT1 loss is expected to compromise viability.

## Recent developments and research priorities

The most important 2024 development was the molecular characterization of human Rft1 in yeast reporter systems. It supports a 14-transmembrane, ER-localized Nin/Cin topology; shows that Rft1 itself is not N-glycosylated; maps most known disease variants to conserved regions; and strengthens evidence that the majority of measurable M5-DLO scramblase activity comes from another protein or complex. The version retrieved was posted **22 June 2024** under DOI **10.1101/2024.04.03.587922**; it should be treated according to its retrieved preprint status even though bibliographic search metadata also associated it with JBC. (hirata2024molecularcharacterizationof pages 7-8, hirata2024molecularcharacterizationof pages 1-3)

Priority gaps are: a curated international natural-history registry; systematic reanalysis of all variants with current ACMG/AMP criteria and gnomAD frequencies; standardized audiologic, neurologic, coagulation, and glycomic phenotyping; identification of the M5-DLO scramblase and RFT1’s direct substrate; neural/inner-ear disease models; and testing whether early RFT1 replacement can safely restore glycosylation in relevant tissues.

## Key primary sources, publication dates, PMIDs, and URLs

1. **Haeuptle et al. “Human RFT1 deficiency leads to a disorder of N-linked glycosylation.”** *American Journal of Human Genetics*, March 2008; **PMID 18313027**; DOI [10.1016/j.ajhg.2007.12.021](https://doi.org/10.1016/j.ajhg.2007.12.021). Exact abstract statement: “The causality of the RFT1 p.R67C mutation was further established by restoration of normal glycosylation profiles in patient-derived fibroblasts after lentiviral expression of a normal RFT1 cDNA.” (a2008humanrft1deficiency pages 1-2)
2. **Vleugels et al. “RFT1 deficiency in three novel CDG patients.”** *Human Mutation*, October 2009; DOI [10.1002/humu.21085](https://doi.org/10.1002/humu.21085). Reports p.Arg67Cys, p.Lys152Glu, and p.Glu298Lys and fibroblast rescue. (vleugels2009rft1deficiencyin pages 4-6, vleugels2009rft1deficiencyin pages 1-3, vleugels2009rft1deficiencyin pages 11-13)
3. **Jaeken et al. “RFT1-CDG: Deafness as a novel feature of congenital disorders of glycosylation.”** *Journal of Inherited Metabolic Disease*, October 2009; DOI [10.1007/s10545-009-1297-3](https://doi.org/10.1007/s10545-009-1297-3). Concluded that hearing loss belongs to the phenotype and described p.Ile296Lys/p.Ile296Arg. (jaeken2009rft1cdgdeafnessas pages 4-7, jaeken2009rft1cdgdeafnessas pages 1-4)
4. **Jelk et al. “Glycoprotein biosynthesis in a eukaryote lacking the membrane protein Rft1.”** *Journal of Biological Chemistry*, 12 July 2013; DOI [10.1074/jbc.M113.479642](https://doi.org/10.1074/jbc.M113.479642). Exact summary: “Rft1 is not required for M5-DLO flipping in vivo but aids conversion of M5-DLO to mDLO by another mechanism.” (jelk2013glycoproteinbiosynthesisin pages 1-2)
5. **Hirata et al. “Molecular characterization of Rft1…”** posted 22 June 2024; DOI [10.1101/2024.04.03.587922](https://doi.org/10.1101/2024.04.03.587922). Exact abstract statement: “It is therefore not known what essential role Rft1 plays in N-glycosylation.” (hirata2024molecularcharacterizationof pages 1-3)

## Evidence limitations

The evidence base is dominated by fewer than a few dozen patients, overlapping case reports, and experimental models. Therefore, phenotype percentages beyond the earliest denominators, penetrance, carrier frequency, incidence, prevalence, survival, treatment-response rates, sex ratios, and genotype–phenotype predictions cannot currently be stated reliably. No disease-specific clinical guideline, randomized trial, registry-scale natural-history study, validated outcome measure, advanced human omics atlas, or mammalian phenocopy was identified.

References

1. (vleugels2009rft1deficiencyin pages 4-6): Wendy Vleugels, Micha A. Haeuptle, Bobby G. Ng, Jean-Claude Michalski, Roberta Battini, Carlo Dionisi-Vici, Mark D. Ludman, Jaak Jaeken, François Foulquier, Hudson H. Freeze, Gert Matthijs, and Thierry Hennet. Rft1 deficiency in three novel cdg patients. Human Mutation, 30:1428-1434, Oct 2009. URL: https://doi.org/10.1002/humu.21085, doi:10.1002/humu.21085. This article has 50 citations and is from a domain leading peer-reviewed journal.

2. (vleugels2009rft1deficiencyin pages 6-7): Wendy Vleugels, Micha A. Haeuptle, Bobby G. Ng, Jean-Claude Michalski, Roberta Battini, Carlo Dionisi-Vici, Mark D. Ludman, Jaak Jaeken, François Foulquier, Hudson H. Freeze, Gert Matthijs, and Thierry Hennet. Rft1 deficiency in three novel cdg patients. Human Mutation, 30:1428-1434, Oct 2009. URL: https://doi.org/10.1002/humu.21085, doi:10.1002/humu.21085. This article has 50 citations and is from a domain leading peer-reviewed journal.

3. (jaeken2009rft1cdgdeafnessas pages 4-7): J. Jaeken, W. Vleugels, L. Régal, C. Corchia, N. Goemans, M. A. Haeuptle, F. Foulquier, T. Hennet, G. Matthijs, and C. Dionisi‐Vici. Rft1-cdg: deafness as a novel feature of congenital disorders of glycosylation. Journal of Inherited Metabolic Disease, 32:335-338, Oct 2009. URL: https://doi.org/10.1007/s10545-009-1297-3, doi:10.1007/s10545-009-1297-3. This article has 45 citations and is from a peer-reviewed journal.

4. (paprocka2021congenitaldisordersof pages 14-15): Justyna Paprocka, Aleksandra Jezela-Stanek, Anna Tylki-Szymańska, and Stephanie Grunewald. Congenital disorders of glycosylation from a neurological perspective. Brain Sciences, 11:88, Jan 2021. URL: https://doi.org/10.3390/brainsci11010088, doi:10.3390/brainsci11010088. This article has 137 citations.

5. (hirata2024molecularcharacterizationof pages 7-8): Eri Hirata, Ken-taro Sakata, Grace I. Dearden, Faria Noor, Indu Menon, George N. Chiduza, and Anant K. Menon. Molecular characterization of rft1, an er membrane protein associated with congenital disorder of glycosylation rft1-cdg. The Journal of Biological Chemistry, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587922, doi:10.1101/2024.04.03.587922. This article has 10 citations.

6. (hirata2024molecularcharacterizationof pages 1-3): Eri Hirata, Ken-taro Sakata, Grace I. Dearden, Faria Noor, Indu Menon, George N. Chiduza, and Anant K. Menon. Molecular characterization of rft1, an er membrane protein associated with congenital disorder of glycosylation rft1-cdg. The Journal of Biological Chemistry, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587922, doi:10.1101/2024.04.03.587922. This article has 10 citations.

7. (a2008humanrft1deficiency pages 4-5): M A Haeuptle, F M Pujol, C Neupert, B Winchester, A J Kastaniotis, M Aebi, and T Hennet. Human rft1 deficiency leads to a disorder of n-linked glycosylation. American journal of human genetics, 82 3:600-6, Mar 2008. URL: https://doi.org/10.1016/j.ajhg.2007.12.021, doi:10.1016/j.ajhg.2007.12.021. This article has 89 citations and is from a highest quality peer-reviewed journal.

8. (jelk2013glycoproteinbiosynthesisin pages 1-2): Jennifer Jelk, Ningguo Gao, Mauro Serricchio, Aita Signorell, Remo Schmidt, James D Bangs, Alvaro Acosta-Serrano, Mark A Lehrman, Peter Bütikofer, and Anant K Menon. Glycoprotein biosynthesis in a eukaryote lacking the membrane protein rft1. JournalArticle, Jul 2013. URL: https://doi.org/10.7892/boris.43260, doi:10.7892/boris.43260. This article has 38 citations.

9. (OpenTargets Search: RFT1-congenital disorder of glycosylation-RFT1): Open Targets Query (RFT1-congenital disorder of glycosylation-RFT1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (a2008humanrft1deficiency pages 1-2): M A Haeuptle, F M Pujol, C Neupert, B Winchester, A J Kastaniotis, M Aebi, and T Hennet. Human rft1 deficiency leads to a disorder of n-linked glycosylation. American journal of human genetics, 82 3:600-6, Mar 2008. URL: https://doi.org/10.1016/j.ajhg.2007.12.021, doi:10.1016/j.ajhg.2007.12.021. This article has 89 citations and is from a highest quality peer-reviewed journal.

11. (vleugels2009rft1deficiencyin pages 1-3): Wendy Vleugels, Micha A. Haeuptle, Bobby G. Ng, Jean-Claude Michalski, Roberta Battini, Carlo Dionisi-Vici, Mark D. Ludman, Jaak Jaeken, François Foulquier, Hudson H. Freeze, Gert Matthijs, and Thierry Hennet. Rft1 deficiency in three novel cdg patients. Human Mutation, 30:1428-1434, Oct 2009. URL: https://doi.org/10.1002/humu.21085, doi:10.1002/humu.21085. This article has 50 citations and is from a domain leading peer-reviewed journal.

12. (jaeken2009rft1cdgdeafnessas pages 1-4): J. Jaeken, W. Vleugels, L. Régal, C. Corchia, N. Goemans, M. A. Haeuptle, F. Foulquier, T. Hennet, G. Matthijs, and C. Dionisi‐Vici. Rft1-cdg: deafness as a novel feature of congenital disorders of glycosylation. Journal of Inherited Metabolic Disease, 32:335-338, Oct 2009. URL: https://doi.org/10.1007/s10545-009-1297-3, doi:10.1007/s10545-009-1297-3. This article has 45 citations and is from a peer-reviewed journal.

13. (hirata2024molecularcharacterizationof pages 35-37): Eri Hirata, Ken-taro Sakata, Grace I. Dearden, Faria Noor, Indu Menon, George N. Chiduza, and Anant K. Menon. Molecular characterization of rft1, an er membrane protein associated with congenital disorder of glycosylation rft1-cdg. The Journal of Biological Chemistry, Apr 2024. URL: https://doi.org/10.1101/2024.04.03.587922, doi:10.1101/2024.04.03.587922. This article has 10 citations.

14. (vleugelsUnknownyearcharacterizationofnovel pages 93-96): W Vleugels. Characterization of novel cdg-i defects. Unknown journal, Unknown year.

15. (vleugels2009rft1deficiencyin pages 11-13): Wendy Vleugels, Micha A. Haeuptle, Bobby G. Ng, Jean-Claude Michalski, Roberta Battini, Carlo Dionisi-Vici, Mark D. Ludman, Jaak Jaeken, François Foulquier, Hudson H. Freeze, Gert Matthijs, and Thierry Hennet. Rft1 deficiency in three novel cdg patients. Human Mutation, 30:1428-1434, Oct 2009. URL: https://doi.org/10.1002/humu.21085, doi:10.1002/humu.21085. This article has 50 citations and is from a domain leading peer-reviewed journal.

16. (pajusalu2021theestimatedprevalence pages 3-4): Sander Pajusalu, Mari-Anne Vals, Laura Mihkla, Ustina Šamarina, Tiina Kahre, and Katrin Õunap. The estimated prevalence of n-linked congenital disorders of glycosylation across various populations based on allele frequencies in general population databases. Frontiers in Genetics, Aug 2021. URL: https://doi.org/10.3389/fgene.2021.719437, doi:10.3389/fgene.2021.719437. This article has 38 citations and is from a peer-reviewed journal.

17. (vleugelsUnknownyearcharacterizationofnovel pages 96-98): W Vleugels. Characterization of novel cdg-i defects. Unknown journal, Unknown year.

## Artifacts

- [Edison artifact artifact-00](RFT1-congenital_disorder_of_glycosylation-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. jelk2013glycoproteinbiosynthesisin pages 1-2
2. hirata2024molecularcharacterizationof pages 1-3
3. paprocka2021congenitaldisordersof pages 14-15
4. hirata2024molecularcharacterizationof pages 7-8
5. hirata2024molecularcharacterizationof pages 35-37
6. pajusalu2021theestimatedprevalence pages 3-4
7. 10.1016/j.ajhg.2007.12.021
8. 10.1002/humu.21085
9. 10.1007/s10545-009-1297-3
10. 10.1074/jbc.M113.479642
11. 10.1101/2024.04.03.587922
12. https://doi.org/10.1016/j.ajhg.2007.12.021
13. https://doi.org/10.1002/humu.21085
14. https://doi.org/10.1007/s10545-009-1297-3
15. https://doi.org/10.1074/jbc.M113.479642
16. https://doi.org/10.1101/2024.04.03.587922
17. https://doi.org/10.1002/humu.21085,
18. https://doi.org/10.1007/s10545-009-1297-3,
19. https://doi.org/10.3390/brainsci11010088,
20. https://doi.org/10.1101/2024.04.03.587922,
21. https://doi.org/10.1016/j.ajhg.2007.12.021,
22. https://doi.org/10.7892/boris.43260,
23. https://doi.org/10.3389/fgene.2021.719437,

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.
