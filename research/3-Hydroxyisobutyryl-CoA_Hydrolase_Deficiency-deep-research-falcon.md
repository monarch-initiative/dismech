---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-29T19:26:24.957373'
end_time: '2026-05-29T19:35:32.633255'
duration_seconds: 547.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 3-hydroxyisobutyryl-CoA hydrolase deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: 3-Hydroxyisobutyryl-CoA_Hydrolase_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3-hydroxyisobutyryl-CoA hydrolase deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3-hydroxyisobutyryl-CoA hydrolase deficiency** covering all of the
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
- **Disease Name:** 3-hydroxyisobutyryl-CoA hydrolase deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3-hydroxyisobutyryl-CoA hydrolase deficiency** covering all of the
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


# Comprehensive Research Report: 3-hydroxyisobutyryl‑CoA hydrolase deficiency (HIBCH deficiency)

## Executive summary
3-hydroxyisobutyryl‑CoA hydrolase deficiency (HIBCH deficiency; HIBCHD) is an ultra-rare autosomal recessive inborn error of **mitochondrial valine catabolism** caused by biallelic pathogenic variants in **HIBCH**, typically presenting in infancy with developmental delay/regression and Leigh/Leigh-like neuroimaging (basal ganglia lesions, often globus pallidus) and characteristic metabolite abnormalities such as **C4‑OH (hydroxy‑C4) acylcarnitine** and valine-pathway urinary metabolites. It is frequently evaluated under the **Leigh syndrome spectrum** diagnostic framework, where parallel biochemical testing (acylcarnitines + urinary organic acids) alongside NGS/WES is emphasized to accelerate identification of potentially treatable causes. (stiles2015successfuldiagnosisof pages 1-3, wang2021cinicalmetabolicand pages 1-2, marti‐sanchez2021delineatingtheneurological pages 7-8, baldo2024acomprehensiveapproach pages 2-4)


## 1. Disease information
### 1.1 What is the disease?
HIBCH deficiency is an inborn error of metabolism due to impaired function of 3-hydroxyisobutyryl‑CoA hydrolase, a mitochondrial enzyme in the valine degradation pathway, leading to a Leigh/Leigh-like neurodegenerative phenotype with episodic metabolic decompensation in many patients. (stiles2015successfuldiagnosisof pages 1-3, jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, wang2021cinicalmetabolicand pages 1-2)

### 1.2 Key identifiers and database mappings
- **OMIM (disease):** **250620** (stiles2015successfuldiagnosisof pages 1-3, jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 1-2, alayed2020metabolicacidosisand pages 2-3)
- **OMIM (gene):** **HIBCH (gene OMIM 610690)** as reported in a 2024 Bahrain cohort paper (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3)
- **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not identified in the retrieved full-text evidence for this run; these should be added by querying MONDO/Orphanet/MeSH/ICD resources directly in a subsequent curation step. (evidence gap)

### 1.3 Synonyms / alternative names
- “HIBCH deficiency”, “HIBCHD”, “3‑hydroxyisobutyryl‑CoA hydrolase deficiency”, and “Leigh/Leigh-like syndrome due to HIBCH variants” are used across the clinical genetics literature. (stiles2015successfuldiagnosisof pages 1-3, wang2021cinicalmetabolicand pages 1-2, taura2023leighlikesyndromewith pages 1-2)

### 1.4 Evidence sources: individual vs aggregated
The current evidence base is largely derived from **case reports and small cohorts**, including retrospective clinic cohorts and multi-center natural history-style aggregations. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, wang2021cinicalmetabolicand pages 1-2, marti‐sanchez2021delineatingtheneurological pages 3-5)


## 2. Etiology
### 2.1 Disease causal factors
- **Primary cause:** biallelic (autosomal recessive) pathogenic variants in **HIBCH**, disrupting mitochondrial valine catabolism. (stiles2015successfuldiagnosisof pages 1-3, alayed2020metabolicacidosisand pages 2-3)
- **Mechanistic causal link:** disruption of the valine pathway leads to accumulation of valine-derived intermediates (including reactive species discussed in the literature), contributing to secondary mitochondrial dysfunction/Leigh-like presentations. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, stiles2015successfuldiagnosisof pages 6-8)

### 2.2 Risk factors
- **Genetic risk factor:** being homozygous/compound heterozygous for pathogenic HIBCH variants; consanguinity is present in some pedigrees and supports autosomal recessive inheritance in affected families. (stiles2015successfuldiagnosisof pages 3-5, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)
- **Environmental/triggering factors (precipitants):** intercurrent infection/illness and metabolic stress can precipitate encephalopathy/regression in many patients with valine-pathway defects, including HIBCH deficiency. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6, taura2023leighlikesyndromewith pages 1-2)

### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the retrieved evidence for HIBCH deficiency. (evidence gap)

### 2.4 Gene–environment interactions
Evidence is largely descriptive: infections and increased metabolic demands appear to trigger decompensation, but formal gene–environment interaction studies were not identified. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6, taura2023leighlikesyndromewith pages 1-2)


## 3. Phenotypes (with HPO suggestions)
### 3.1 Core neurologic phenotype
Commonly reported manifestations include developmental delay/regression, hypotonia, encephalopathy, feeding difficulties, and movement disorders (dystonia/spasticity/ataxia), with seizures and ocular abnormalities in some patients. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, wang2021cinicalmetabolicand pages 1-2, marti‐sanchez2021delineatingtheneurological pages 7-8)

**HPO term suggestions (non-exhaustive):**
- Developmental delay **HP:0001263**
- Developmental regression **HP:0002376**
- Hypotonia **HP:0001252**
- Encephalopathy **HP:0001298**
- Dystonia **HP:0001332**
- Spasticity **HP:0001257**
- Ataxia **HP:0001251**
- Seizure **HP:0001250**
- Feeding difficulties **HP:0011968**
- Optic atrophy **HP:0000648**
- Nystagmus **HP:0000639**

### 3.2 Age of onset and course
- Onset is typically in infancy/early childhood; one cohort reports onset “from as early as **6 weeks to 6 months**” (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6), while another case-series reported **median onset 13 months (8–18 months)** (wang2021cinicalmetabolicand pages 1-2).
- Course is often progressive and can include episodic worsening with acute encephalopathy. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6, marti‐sanchez2021delineatingtheneurological pages 7-8)

### 3.3 Neuroimaging phenotype
- Leigh/Leigh-like basal ganglia involvement is typical; HIBCH deficiency can show **“Bilateral globus pallidus T2-WI hyperintensities”** as a distinguishing neuroradiologic pattern in comparative series. (marti‐sanchez2021delineatingtheneurological pages 7-8)
- Longitudinal imaging can show additional features, including progressive cerebellar atrophy in some cases, expanding the known phenotype. (taura2023leighlikesyndromewith pages 1-2)

**HPO suggestions:**
- Abnormality of the basal ganglia **HP:0002134**
- Abnormal brain MRI signal **HP:0012448**
- Cerebellar atrophy **HP:0001272**

### 3.4 Laboratory abnormalities
Key biochemical findings used clinically include elevated C4‑OH acylcarnitine and urine valine-pathway metabolites (see Diagnostics). (wang2021cinicalmetabolicand pages 1-2, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)

### 3.5 Quality of life
Formal QoL instruments were not identified in the retrieved evidence, but functional outcomes can be severe (persistent developmental delay; loss of ambulation in severe cases), implying substantial QoL impact. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6, taura2023leighlikesyndromewith pages 2-3)


## 4. Genetic / molecular information
### 4.1 Causal gene and function
HIBCH catalyzes a step in valine catabolism; in a comparative natural history study, the authors state: **“HIBCH catalyses the fifth step of valine catabolism”** and note biochemical accumulation of 3-hydroxyisobutyrylcarnitine in HIBCH deficiency. (marti‐sanchez2021delineatingtheneurological pages 3-5, marti‐sanchez2021delineatingtheneurological pages 7-8)

### 4.2 Pathogenic variant spectrum (examples from cohorts)
- A 2024 Bahrain cohort reported a novel homozygous variant **c.860A>G (p.Asp287Gly)** in all eight patients in that cohort. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6)
- A 2021 case-series identified six novel variants (including splice and truncating) among eight patients. (wang2021cinicalmetabolicand pages 1-2)
- A 2015 sibling pair study reported a novel homozygous variant **c.196C>T (p.Arg66Trp)** and demonstrated enzyme deficiency in fibroblasts. (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 3-5)
- A 2023 case report described two novel variants **c.782T>C (p.Leu261Pro)** and **c.1012-1G>A** (compound heterozygous), with long-term MRI follow-up showing progressive cerebellar atrophy. (taura2023leighlikesyndromewith pages 1-2)

**Variant class patterns (from cited case series):** missense, truncating, and splice-site variants are all represented. (wang2021cinicalmetabolicand pages 1-2, taura2023leighlikesyndromewith pages 1-2)

### 4.3 Genotype–phenotype correlations (evidence-supported)
A multi-center aggregation reported survival differences suggesting genotype–outcome correlation:
- Within HIBCH deficiency, **homozygous variants inside/near the catalytic region** were associated with worse survival than **surface** variants (log-rank P = 0.004). (marti‐sanchez2021delineatingtheneurological pages 3-5)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities were identified in the retrieved evidence. (evidence gap)


## 5. Environmental information
No specific toxins, lifestyle factors, or infectious agents were identified as causal; however, febrile illness/infection can act as a trigger for acute decompensation. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6, taura2023leighlikesyndromewith pages 1-2)


## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic understanding
The working model is that loss of HIBCH activity perturbs valine degradation, with accumulation of upstream metabolites and reactive intermediates, contributing to mitochondrial dysfunction and Leigh/Leigh-like neurodegeneration. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, stiles2015successfuldiagnosisof pages 6-8)

A comparative clinical series emphasizes that HIBCH deficiency’s main biochemical hallmark is **“Elevated plasma levels of 3-hydroxyisobutyryl carnitine”** (marti‐sanchez2021delineatingtheneurological pages 7-8), and a diagnostic review for Leigh syndrome spectrum notes that in HIBCH deficiency acylcarnitine profiles may show **“high levels of 3-hydroxyisobutyryl carnitine.”** (baldo2024acomprehensiveapproach pages 2-4)

### 6.2 Causal chain (clinically oriented)
1. **Biallelic HIBCH variants** → reduced HIBCH activity in mitochondria (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 3-5)
2. **Impaired valine catabolism** → accumulation of valine-pathway metabolites (C4‑OH acylcarnitine; urine organic acids and cysteine/cysteamine conjugates) (wang2021cinicalmetabolicand pages 1-2, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)
3. **Secondary mitochondrial dysfunction** / energy failure in vulnerable tissues → Leigh/Leigh-like basal ganglia injury (stiles2015successfuldiagnosisof pages 1-3, marti‐sanchez2021delineatingtheneurological pages 7-8)
4. **Clinical manifestations**: neurodevelopmental regression, encephalopathy, movement disorders, seizures, feeding difficulties; potentially progressive neurodegeneration (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, marti‐sanchez2021delineatingtheneurological pages 7-8)

### 6.3 Pathways / ontology mapping suggestions
- **GO biological process (suggestions):** valine catabolic process; branched-chain amino acid catabolic process; mitochondrial metabolic process.
- **GO cellular component (suggestions):** mitochondrion / mitochondrial matrix.
- **Cell Ontology (CL) suggestions for susceptible cell types:** neurons (CL:0000540), astrocytes (CL:0000127), oligodendrocytes (CL:0000128), microglia (CL:0000129) (suggested because disease is primarily neurodegenerative with basal ganglia/cerebellar involvement).

(These ontology suggestions are provided for knowledge base structuring; the specific GO/CL identifiers were not enumerated in the retrieved full-text evidence.)

### 6.4 Molecular profiling / multi-omics
No transcriptomic/proteomic/metabolomic multi-omics studies specific to HIBCH deficiency were identified in the retrieved evidence set for this run beyond targeted metabolite profiling used diagnostically. (wang2021cinicalmetabolicand pages 1-2)


## 7. Anatomical structures affected
### 7.1 Organ-level involvement
The central nervous system is the primary affected system, with imaging lesions in the basal ganglia and sometimes cerebellar atrophy. (marti‐sanchez2021delineatingtheneurological pages 7-8, taura2023leighlikesyndromewith pages 1-2)

**UBERON suggestions:**
- Basal ganglion **UBERON:0002420** (suggested)
- Globus pallidus **UBERON:0001885** (suggested)
- Cerebellum **UBERON:0002037** (suggested)

### 7.2 Subcellular localization
Function is mitochondrial; the disease is framed in mitochondrial metabolism and mitochondrial disease diagnostics. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, baldo2024acomprehensiveapproach pages 2-4)


## 8. Temporal development
- Typical onset: infancy/early childhood, sometimes within the first months of life. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6, wang2021cinicalmetabolicand pages 1-2)
- Course patterns: progressive neurodegeneration and/or episodic decompensation; some patients show chronic phases after an acute encephalopathic event. (taura2023leighlikesyndromewith pages 1-2)


## 9. Inheritance and population
### 9.1 Inheritance
Autosomal recessive inheritance is supported by multiple pedigrees and case series (biallelic variants; heterozygous parents). (stiles2015successfuldiagnosisof pages 3-5, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)

### 9.2 Epidemiology / frequency estimates
- A 2024 Bahrain cohort cites OMIM-based estimates: **“1 in 127,939 in East Asians”** and **“1 in 551,545 in Europeans.”** (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3)
- Earlier series also cite incidence on the order of ~1 in 130,000 and suggest underdiagnosis. (stiles2015successfuldiagnosisof pages 1-3, wang2021cinicalmetabolicand pages 1-2)

### 9.3 Founder effects / population-specific variants
A Bahrain cohort reported a shared homozygous variant in all eight patients (consistent with a local recurrent variant), but also notes no broadly “confirmed founder mutation” across populations. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6)

Carrier frequency estimates from population databases were referenced in the 2015 study’s incidence modeling approach, but detailed per-population carrier frequencies were not present in the retrieved excerpts. (stiles2015successfuldiagnosisof pages 3-5)


## 10. Diagnostics
### 10.1 Clinical suspicion
HIBCH deficiency should be considered in infants/children with Leigh/Leigh-like presentation (basal ganglia lesions) and compatible metabolic findings, particularly when valine-pathway metabolites are present. (stiles2015successfuldiagnosisof pages 1-3, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 1-2)

### 10.2 Biochemical testing (key real-world implementation)
Common diagnostic markers:
- **C4‑OH (hydroxy‑C4) acylcarnitine** in dried blood spots or plasma; one series reported hydroxy‑C4 elevations on newborn screening cards, supporting NBS detectability when hydroxy‑C4 is measured. (stiles2015successfuldiagnosisof pages 5-6)
- **Urine metabolites** used for screening/confirmation include **S-(2-carboxypropyl) cysteine** and **S-(2-carboxypropyl) cysteamine** and their carnitine esters (tandem MS), plus other valine-pathway organic acids. (kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)
- In a longitudinal case-series, urinary **2,3-dihydroxy-2-methylbutyrate** was elevated in **6/7** and **S-(2-carboxypropyl) cysteamine** in **3/3**, and dried blood spot **C4‑OH** elevation occurred in **5/7**. (wang2021cinicalmetabolicand pages 1-2)

Important limitation: hydroxy‑C4 can be normal in milder phenotypes; thus reliance on a single marker may miss cases. (kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 1-2)

### 10.3 Genetic testing
NGS-based testing (gene panels, WES, WGS) is a primary route to diagnosis in modern practice; several reports demonstrate WES/WGS leading to diagnosis, including in Leigh-like presentations with variable/negative metabolic screens. (stiles2015successfuldiagnosisof pages 1-3, taura2023leighlikesyndromewith pages 1-2)

### 10.4 Enzymatic confirmation
Measurement of HIBCH activity in patient fibroblasts/tissues can confirm diagnosis but may not be widely available in routine clinical settings. (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 5-6)

### 10.5 Leigh syndrome spectrum diagnostic frameworks (2023–2024 development)
A 2024 diagnostic framework for Leigh syndrome spectrum recommends parallel biochemical testing and states: **“basic metabolic studies are mandatory for all patients, including an L/P ratio, plasma amino acids and acylcarnitine profiles, and urinary organic acids”** and that their approach **“characterized 80% of our cohort and promoted specific intervention in 10% of confirmed cases.”** (baldo2024acomprehensiveapproach pages 2-4, baldo2024acomprehensiveapproach pages 1-2)

### 10.6 Newborn screening status
- Retrospective analysis of newborn screening cards in an affected sibling pair showed elevated hydroxy‑C4 and suggested that “this disorder could be screened for by NBS programs” when hydroxy‑C4 is included/assessed. (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 5-6)
- No evidence was retrieved in this run that HIBCH deficiency is universally included in national newborn screening panels; implementation appears program-dependent. (evidence gap)

### 10.7 Differential diagnosis (examples)
Valine-pathway and related mitochondrial/Leigh-like conditions (e.g., ECHS1/SCEH deficiency) are prominent differentials; comparative neuroradiology and metabolite patterns (e.g., predominance of globus pallidus involvement; 3-hydroxyisobutyrylcarnitine) can help differentiate. (marti‐sanchez2021delineatingtheneurological pages 7-8, marti‐sanchez2021delineatingtheneurological pages 11-13)


## 11. Outcomes / prognosis
- Outcomes vary but can be severe. In the Bahrain cohort, despite interventions, many patients had severe persistent developmental delay and some died due to complications (including sepsis). (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3)
- Comparative survival analysis across aggregated cohorts found **longer survival in HIBCH** compared with ECHS1/SCEH deficiency (Breslow test P = 0.036). (marti‐sanchez2021delineatingtheneurological pages 3-5)
- Earlier onset was associated with poorer prognosis in the Bahrain cohort. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6)


## 12. Treatment
### 12.1 Current standard of care (no disease-specific curative therapy)
Management is largely supportive and empiric metabolic therapy:
- **Dietary management:** low-valine / low-protein dietary strategies are commonly suggested/used. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)
- **Supplements/adjuncts:** carnitine and N-acetylcysteine are commonly mentioned; “mitochondrial cocktail” approaches are described in Leigh-like care contexts. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)
- **Acute decompensation care:** supportive management (e.g., IV fluids, correction of acidosis, high-glucose support) is described in severe presentations. (kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)

Evidence for benefit is limited and mainly observational:
- In an 8-patient longitudinal case-series, five patients “responded positively to treatment with a significant decrease in NPMDS scores” after drug and dietary treatment. (wang2021cinicalmetabolicand pages 1-2)
- In a comparative cohort, only one patient showed “a mild improvement in lower limb dystonia while receiving valine restricted formula,” and most had no clear neurologic improvement. (marti‐sanchez2021delineatingtheneurological pages 7-8)

### 12.2 MAXO suggestions (treatment action ontology)
- Dietary amino acid restriction / valine restriction (MAXO term suggestion)
- Carnitine supplementation (MAXO term suggestion)
- N-acetylcysteine therapy (MAXO term suggestion)
- Supportive critical care for metabolic decompensation (MAXO term suggestion)

### 12.3 Clinical trials
No interventional clinical trials were identified in the tool-run state for HIBCH deficiency. (evidence gap)


## 13. Prevention
- **Primary prevention:** not applicable in the usual sense for an autosomal recessive Mendelian disorder, except via reproductive options.
- **Secondary prevention:** early detection (potentially via newborn screening hydroxy‑C4 signal where implemented) and early metabolic management may reduce decompensation risk, but controlled evidence is lacking. (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 5-6)
- **Genetic counseling:** indicated for affected families (implied by autosomal recessive inheritance and pedigree studies). (stiles2015successfuldiagnosisof pages 3-5, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3)


## 14. Other species / natural disease
No naturally occurring veterinary HIBCH deficiency reports were identified in the retrieved evidence set. (evidence gap)


## 15. Model organisms
No HIBCH-deficiency-specific animal models or iPSC models were identified in the retrieved evidence for this run. (evidence gap)


## Structured evidence table (for knowledge base entry)
| Disease / synonym field | Summary |
|---|---|
| Preferred disease name | 3-hydroxyisobutyryl-CoA hydrolase deficiency |
| Common synonyms | HIBCH deficiency; HIBCHD; 3-hydroxy-isobutyryl-CoA hydrolase deficiency; Leigh/Leigh-like syndrome due to HIBCH deficiency (stiles2015successfuldiagnosisof pages 1-3, jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, wang2021cinicalmetabolicand pages 1-2) |
| OMIM disease ID | OMIM #250620 (reported across cohort/case-series literature) (stiles2015successfuldiagnosisof pages 1-3, jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 1-2, alayed2020metabolicacidosisand pages 2-3) |
| Causal gene | **HIBCH**; gene OMIM reported as **610690** in the Bahrain cohort (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3) |
| Inheritance | Autosomal recessive; biallelic pathogenic variants confirmed in reported families and cohorts (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 3-5, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 1-2, alayed2020metabolicacidosisand pages 2-3) |
| Core biochemical pathway | Mitochondrial **valine catabolism**; HIBCH catalyzes the conversion of 3-hydroxyisobutyryl-CoA to 3-hydroxyisobutyric acid / the fifth step of valine catabolism (wang2021cinicalmetabolicand pages 1-2, marti‐sanchez2021delineatingtheneurological pages 3-5) |
| Pathophysiologic consequence | Accumulation of 3-hydroxyisobutyryl-CoA and reactive valine-derived intermediates (including methacrylyl-CoA-related species), contributing to secondary pyruvate dehydrogenase and respiratory-chain dysfunction / Leigh-like disease (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, stiles2015successfuldiagnosisof pages 6-8) |
| Key blood biomarker | Elevated **hydroxy-C4 / C4-OH acylcarnitine** (3-hydroxyisobutyryl-carnitine signal); detectable in dried blood spots and sometimes plasma, but can be normal in milder cases (stiles2015successfuldiagnosisof pages 1-3, wang2021cinicalmetabolicand pages 1-2, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 1-2, stiles2015successfuldiagnosisof pages 5-6) |
| Key urine biomarkers | **2,3-dihydroxy-2-methylbutyrate**; **S-(2-carboxypropyl)cysteine (SCPC)**; **S-(2-carboxypropyl)cysteamine (SCPCM)**; some reports also note valine-pathway organic acids and variable 3-hydroxy-isovaleric acid elevations (stiles2015successfuldiagnosisof pages 1-3, wang2021cinicalmetabolicand pages 1-2, kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3, baldo2024acomprehensiveapproach pages 2-4) |
| Typical neuroimaging | Bilateral symmetric **basal ganglia** lesions, especially **globus pallidus** T2 hyperintensity; Leigh/Leigh-like pattern; white-matter changes may occur; cavitation/small cysts in pallidum/putamen reported; some long-term follow-up shows **progressive cerebellar atrophy** (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, marti‐sanchez2021delineatingtheneurological pages 3-5, marti‐sanchez2021delineatingtheneurological pages 7-8, taura2023leighlikesyndromewith pages 1-2, taura2023leighlikesyndromewith pages 3-4) |
| Typical age of onset | Usually **infancy / early childhood**; onset reported from **6 weeks to 6 months** in one cohort, median **13 months** (range 8–18 months) in another; developmental delay/regression commonly begins in the first 2 years of life (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6, wang2021cinicalmetabolicand pages 1-2) |
| Core clinical picture | Developmental delay or regression, hypotonia, encephalopathy/acute decompensation, feeding difficulties, dystonia/spasticity/ataxia; seizures and ocular abnormalities may occur; phenotype overlaps Leigh syndrome spectrum (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, wang2021cinicalmetabolicand pages 1-2, marti‐sanchez2021delineatingtheneurological pages 7-8) |
| Epidemiology / rarity | Ultra-rare. One study citing OMIM reported estimated frequency about **1 in 127,939** in East Asians and **1 in 551,545** in Europeans; earlier work suggested incidence may be around **1 in 130,000** and underdiagnosed (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, wang2021cinicalmetabolicand pages 1-2) |
| Newborn screening relevance | Retrospective newborn screening card analysis showed elevated hydroxy-C4 in affected siblings, supporting potential detectability by NBS if hydroxy-C4 is assessed (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 6-8, stiles2015successfuldiagnosisof pages 5-6) |
| Diagnostic approach | Parallel **biochemical screening** (acylcarnitine + urinary organic acids) plus **NGS/WES** is recommended; enzymatic confirmation in fibroblasts/tissues is possible but less routinely available (stiles2015successfuldiagnosisof pages 1-3, wang2021cinicalmetabolicand pages 1-2, baldo2024acomprehensiveapproach pages 2-4, stiles2015successfuldiagnosisof pages 5-6) |
| Best recent cohort / case-series references | **Al jishi et al., 2024** retrospective Bahrain cohort, 8 patients, DOI/URL: https://doi.org/10.24911/jbcgenetics.183-1722167696 (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6) |
|  | **Baldo et al., 2024** Leigh syndrome spectrum diagnostic framework; emphasizes parallel biochemical testing and notes HIBCH as a treatable valine-metabolism cause, URL: https://doi.org/10.3390/diagnostics14192133 (baldo2024acomprehensiveapproach pages 2-4, baldo2024acomprehensiveapproach pages 1-2) |
|  | **Wang et al., 2021** clinical/metabolic/genetic follow-up of 8 HIBCH patients, URL: https://doi.org/10.3389/fphar.2021.605803 (wang2021cinicalmetabolicand pages 1-2) |
|  | **Marti-Sanchez et al., 2021** neurological phenotype/natural history across HIBCH and ECHS1 defects; survival and imaging comparisons, URL: https://doi.org/10.1002/jimd.12288 (marti‐sanchez2021delineatingtheneurological pages 3-5, marti‐sanchez2021delineatingtheneurological pages 1-3, marti‐sanchez2021delineatingtheneurological pages 7-8) |
|  | **Taura et al., 2023** case report expanding imaging spectrum to progressive cerebellar atrophy, URL: https://doi.org/10.1038/s41439-023-00251-y (taura2023leighlikesyndromewith pages 1-2, taura2023leighlikesyndromewith pages 2-3, taura2023leighlikesyndromewith pages 3-4) |
|  | **Stiles et al., 2015** seminal diagnostic/NBS paper on two siblings, URL: https://doi.org/10.1016/j.ymgme.2015.05.008 (stiles2015successfuldiagnosisof pages 1-3, stiles2015successfuldiagnosisof pages 6-8, stiles2015successfuldiagnosisof pages 5-6) |


*Table: This table summarizes the main identifiers, pathway context, biomarkers, imaging features, onset pattern, and key references for 3-hydroxyisobutyryl-CoA hydrolase deficiency. It is designed as a compact evidence-backed reference for a disease knowledge base entry.*


## Recent developments and authoritative perspectives (2023–2024 emphasis)
- **2024 (Diagnostics, MDPI):** A Leigh syndrome spectrum diagnostic pipeline emphasizes parallel metabolic testing and notes that biochemical workups can rapidly characterize cases and enable intervention in a subset, relevant because HIBCH deficiency is among treatable metabolic causes within LSS. URL: https://doi.org/10.3390/diagnostics14192133 (published Sep 2024). (baldo2024acomprehensiveapproach pages 2-4, baldo2024acomprehensiveapproach pages 1-2)
- **2024 (Bahrain cohort):** A retrospective cohort expands real-world phenotypic and biochemical characterization, reports a recurrent homozygous variant in their population, and provides incidence estimates (from OMIM) across ancestries. URL: https://doi.org/10.24911/jbcgenetics.183-1722167696 (published Dec 2024). (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3, jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6)
- **2023 (Human Genome Variation):** Long-term MRI follow-up in a genetically confirmed case expands the neuroradiologic spectrum to include progressive cerebellar atrophy. URL: https://doi.org/10.1038/s41439-023-00251-y (published Aug 2023). (taura2023leighlikesyndromewith pages 1-2)


## Key direct abstract quotes (verbatim as captured in retrieved full text)
- Leigh syndrome spectrum diagnostics: **“basic metabolic studies are mandatory for all patients, including an L/P ratio, plasma amino acids and acylcarnitine profiles, and urinary organic acids”** (baldo2024acomprehensiveapproach pages 2-4).
- Leigh syndrome spectrum diagnostics: **“characterized 80% of our cohort and promoted specific intervention in 10% of confirmed cases”** (baldo2024acomprehensiveapproach pages 1-2).
- HIBCH vs ECHS1 comparative series (biochemistry): **“Elevated plasma levels of 3-hydroxyisobutyryl carnitine”** (marti‐sanchez2021delineatingtheneurological pages 7-8).
- HIBCH function statement: **“HIBCH catalyses the fifth step of valine catabolism”** (marti‐sanchez2021delineatingtheneurological pages 3-5).


## Notable evidence gaps for knowledge base completion
1. MONDO, Orphanet, MeSH, and ICD mappings were not retrieved in the current tool-run evidence and require direct ontology/database queries.
2. Robust prevalence and carrier frequency statistics remain sparse; estimates exist but vary by ancestry and methodology.
3. No controlled clinical trials; treatment evidence is largely observational.
4. Limited published mechanistic studies directly in patient tissues; multi-omics and model organism resources appear underdeveloped in the retrieved set.


References

1. (stiles2015successfuldiagnosisof pages 1-3): Ashlee R. Stiles, Sacha Ferdinandusse, Arnaud Besse, Vivek Appadurai, Karen B. Leydiker, E.J. Cambray-Forker, Penelope E. Bonnen, and Jose E. Abdenur. Successful diagnosis of hibch deficiency from exome sequencing and positive retrospective analysis of newborn screening cards in two siblings presenting with leigh's disease. Molecular Genetics and Metabolism, 115(4):161-167, Aug 2015. URL: https://doi.org/10.1016/j.ymgme.2015.05.008, doi:10.1016/j.ymgme.2015.05.008. This article has 48 citations and is from a peer-reviewed journal.

2. (wang2021cinicalmetabolicand pages 1-2): Junling Wang, Zhimei Liu, Manting Xu, Xiaodi Han, Changhong Ren, Xinying Yang, Chunhua Zhang, and Fang Fang. Cinical, metabolic, and genetic analysis and follow-up of eight patients with hibch mutations presenting with leigh/leigh-like syndrome. Frontiers in Pharmacology, Mar 2021. URL: https://doi.org/10.3389/fphar.2021.605803, doi:10.3389/fphar.2021.605803. This article has 23 citations.

3. (marti‐sanchez2021delineatingtheneurological pages 7-8): Laura Marti‐Sanchez, Heidy Baide‐Mairena, Anna Marcé‐Grau, Roser Pons, Anastasia Skouma, Eduardo López‐Laso, Maria Sigatullina, Cristiano Rizzo, Michela Semeraro, Diego Martinelli, Rosalba Carrozzo, Carlo Dionisi‐Vici, Luis González‐Gutiérrez‐Solana, Marta Correa‐Vela, Juan Dario Ortigoza‐Escobar, Ángel Sánchez‐Montañez, Élida Vazquez, Ignacio Delgado, Sergio Aguilera‐Albesa, María Eugenia Yoldi, Antonia Ribes, Frederic Tort, Luca Pollini, Serena Galosi, Vincenzo Leuzzi, Manuela Tolve, Laura Pérez‐Gay, Luis Aldamiz‐Echevarría, Mireia Del Toro, Antonio Arranz, Filip Roelens, Roser Urreizti, Rafael Artuch, Alfons Macaya, and Belén Pérez‐Dueñas. Delineating the neurological phenotype in children with defects in the <scp><i>echs1</i></scp> or <scp><i>hibch</i></scp> gene. Aug 2021. URL: https://doi.org/10.1002/jimd.12288, doi:10.1002/jimd.12288. This article has 48 citations and is from a peer-reviewed journal.

4. (baldo2024acomprehensiveapproach pages 2-4): Manuela Schubert Baldo, Luísa Azevedo, Margarida Paiva Coelho, Esmeralda Martins, and Laura Vilarinho. A comprehensive approach to the diagnosis of leigh syndrome spectrum. Diagnostics, 14:2133, Sep 2024. URL: https://doi.org/10.3390/diagnostics14192133, doi:10.3390/diagnostics14192133. This article has 2 citations.

5. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 1-3): Emtithal Al jishi, Zahra Al sahlawi, Huda Omran, Mohammed S. Almaliki, Faten Al mahroos, and Heba Alkoheji. Characterization of 3-hydroxyisobutyryl-coa hydrolase (hibch) deficiency in bahrain: a retrospective cohort study. Journal of Biochemical and Clinical Genetics, 7:068-074, Dec 2024. URL: https://doi.org/10.24911/jbcgenetics.183-1722167696, doi:10.24911/jbcgenetics.183-1722167696. This article has 0 citations.

6. (kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 1-2): Mustafa Kılıç and Fatma Kurt-Çolak. 3-hydroxyisobutyryl-coa hydrolase deficiency in a turkish child with a novel hibch gene mutation and literature review. Molecular Syndromology, 11:170-175, Jun 2020. URL: https://doi.org/10.1159/000508728, doi:10.1159/000508728. This article has 2 citations and is from a peer-reviewed journal.

7. (alayed2020metabolicacidosisand pages 2-3): Alaa M Alayed, Eissa Ali Faqeih, Abdulwahed Aldehaimi, Roy W A Peake, and and Naif A M Almontashiri. Metabolic acidosis and hypoglycemia in a child with leigh-like phenotype. Clinical chemistry, 66 5:739-741, May 2020. URL: https://doi.org/10.1093/clinchem/hvaa079, doi:10.1093/clinchem/hvaa079. This article has 1 citations and is from a highest quality peer-reviewed journal.

8. (taura2023leighlikesyndromewith pages 1-2): Yoshihiro Taura, Takenori Tozawa, Kenichi Isoda, Satori Hirai, Tomohiro Chiyonobu, Naoko Yano, Takahiro Hayashi, Takeshi Yoshida, and Tomoko Iehara. Leigh-like syndrome with progressive cerebellar atrophy caused by novel hibch variants. Human Genome Variation, Aug 2023. URL: https://doi.org/10.1038/s41439-023-00251-y, doi:10.1038/s41439-023-00251-y. This article has 8 citations.

9. (marti‐sanchez2021delineatingtheneurological pages 3-5): Laura Marti‐Sanchez, Heidy Baide‐Mairena, Anna Marcé‐Grau, Roser Pons, Anastasia Skouma, Eduardo López‐Laso, Maria Sigatullina, Cristiano Rizzo, Michela Semeraro, Diego Martinelli, Rosalba Carrozzo, Carlo Dionisi‐Vici, Luis González‐Gutiérrez‐Solana, Marta Correa‐Vela, Juan Dario Ortigoza‐Escobar, Ángel Sánchez‐Montañez, Élida Vazquez, Ignacio Delgado, Sergio Aguilera‐Albesa, María Eugenia Yoldi, Antonia Ribes, Frederic Tort, Luca Pollini, Serena Galosi, Vincenzo Leuzzi, Manuela Tolve, Laura Pérez‐Gay, Luis Aldamiz‐Echevarría, Mireia Del Toro, Antonio Arranz, Filip Roelens, Roser Urreizti, Rafael Artuch, Alfons Macaya, and Belén Pérez‐Dueñas. Delineating the neurological phenotype in children with defects in the <scp><i>echs1</i></scp> or <scp><i>hibch</i></scp> gene. Aug 2021. URL: https://doi.org/10.1002/jimd.12288, doi:10.1002/jimd.12288. This article has 48 citations and is from a peer-reviewed journal.

10. (stiles2015successfuldiagnosisof pages 6-8): Ashlee R. Stiles, Sacha Ferdinandusse, Arnaud Besse, Vivek Appadurai, Karen B. Leydiker, E.J. Cambray-Forker, Penelope E. Bonnen, and Jose E. Abdenur. Successful diagnosis of hibch deficiency from exome sequencing and positive retrospective analysis of newborn screening cards in two siblings presenting with leigh's disease. Molecular Genetics and Metabolism, 115(4):161-167, Aug 2015. URL: https://doi.org/10.1016/j.ymgme.2015.05.008, doi:10.1016/j.ymgme.2015.05.008. This article has 48 citations and is from a peer-reviewed journal.

11. (stiles2015successfuldiagnosisof pages 3-5): Ashlee R. Stiles, Sacha Ferdinandusse, Arnaud Besse, Vivek Appadurai, Karen B. Leydiker, E.J. Cambray-Forker, Penelope E. Bonnen, and Jose E. Abdenur. Successful diagnosis of hibch deficiency from exome sequencing and positive retrospective analysis of newborn screening cards in two siblings presenting with leigh's disease. Molecular Genetics and Metabolism, 115(4):161-167, Aug 2015. URL: https://doi.org/10.1016/j.ymgme.2015.05.008, doi:10.1016/j.ymgme.2015.05.008. This article has 48 citations and is from a peer-reviewed journal.

12. (kılıc20203hydroxyisobutyrylcoahydrolasedeficiency pages 3-3): Mustafa Kılıç and Fatma Kurt-Çolak. 3-hydroxyisobutyryl-coa hydrolase deficiency in a turkish child with a novel hibch gene mutation and literature review. Molecular Syndromology, 11:170-175, Jun 2020. URL: https://doi.org/10.1159/000508728, doi:10.1159/000508728. This article has 2 citations and is from a peer-reviewed journal.

13. (jishi2024characterizationof3hydroxyisobutyrylcoa pages 4-6): Emtithal Al jishi, Zahra Al sahlawi, Huda Omran, Mohammed S. Almaliki, Faten Al mahroos, and Heba Alkoheji. Characterization of 3-hydroxyisobutyryl-coa hydrolase (hibch) deficiency in bahrain: a retrospective cohort study. Journal of Biochemical and Clinical Genetics, 7:068-074, Dec 2024. URL: https://doi.org/10.24911/jbcgenetics.183-1722167696, doi:10.24911/jbcgenetics.183-1722167696. This article has 0 citations.

14. (taura2023leighlikesyndromewith pages 2-3): Yoshihiro Taura, Takenori Tozawa, Kenichi Isoda, Satori Hirai, Tomohiro Chiyonobu, Naoko Yano, Takahiro Hayashi, Takeshi Yoshida, and Tomoko Iehara. Leigh-like syndrome with progressive cerebellar atrophy caused by novel hibch variants. Human Genome Variation, Aug 2023. URL: https://doi.org/10.1038/s41439-023-00251-y, doi:10.1038/s41439-023-00251-y. This article has 8 citations.

15. (stiles2015successfuldiagnosisof pages 5-6): Ashlee R. Stiles, Sacha Ferdinandusse, Arnaud Besse, Vivek Appadurai, Karen B. Leydiker, E.J. Cambray-Forker, Penelope E. Bonnen, and Jose E. Abdenur. Successful diagnosis of hibch deficiency from exome sequencing and positive retrospective analysis of newborn screening cards in two siblings presenting with leigh's disease. Molecular Genetics and Metabolism, 115(4):161-167, Aug 2015. URL: https://doi.org/10.1016/j.ymgme.2015.05.008, doi:10.1016/j.ymgme.2015.05.008. This article has 48 citations and is from a peer-reviewed journal.

16. (baldo2024acomprehensiveapproach pages 1-2): Manuela Schubert Baldo, Luísa Azevedo, Margarida Paiva Coelho, Esmeralda Martins, and Laura Vilarinho. A comprehensive approach to the diagnosis of leigh syndrome spectrum. Diagnostics, 14:2133, Sep 2024. URL: https://doi.org/10.3390/diagnostics14192133, doi:10.3390/diagnostics14192133. This article has 2 citations.

17. (marti‐sanchez2021delineatingtheneurological pages 11-13): Laura Marti‐Sanchez, Heidy Baide‐Mairena, Anna Marcé‐Grau, Roser Pons, Anastasia Skouma, Eduardo López‐Laso, Maria Sigatullina, Cristiano Rizzo, Michela Semeraro, Diego Martinelli, Rosalba Carrozzo, Carlo Dionisi‐Vici, Luis González‐Gutiérrez‐Solana, Marta Correa‐Vela, Juan Dario Ortigoza‐Escobar, Ángel Sánchez‐Montañez, Élida Vazquez, Ignacio Delgado, Sergio Aguilera‐Albesa, María Eugenia Yoldi, Antonia Ribes, Frederic Tort, Luca Pollini, Serena Galosi, Vincenzo Leuzzi, Manuela Tolve, Laura Pérez‐Gay, Luis Aldamiz‐Echevarría, Mireia Del Toro, Antonio Arranz, Filip Roelens, Roser Urreizti, Rafael Artuch, Alfons Macaya, and Belén Pérez‐Dueñas. Delineating the neurological phenotype in children with defects in the <scp><i>echs1</i></scp> or <scp><i>hibch</i></scp> gene. Aug 2021. URL: https://doi.org/10.1002/jimd.12288, doi:10.1002/jimd.12288. This article has 48 citations and is from a peer-reviewed journal.

18. (taura2023leighlikesyndromewith pages 3-4): Yoshihiro Taura, Takenori Tozawa, Kenichi Isoda, Satori Hirai, Tomohiro Chiyonobu, Naoko Yano, Takahiro Hayashi, Takeshi Yoshida, and Tomoko Iehara. Leigh-like syndrome with progressive cerebellar atrophy caused by novel hibch variants. Human Genome Variation, Aug 2023. URL: https://doi.org/10.1038/s41439-023-00251-y, doi:10.1038/s41439-023-00251-y. This article has 8 citations.

19. (marti‐sanchez2021delineatingtheneurological pages 1-3): Laura Marti‐Sanchez, Heidy Baide‐Mairena, Anna Marcé‐Grau, Roser Pons, Anastasia Skouma, Eduardo López‐Laso, Maria Sigatullina, Cristiano Rizzo, Michela Semeraro, Diego Martinelli, Rosalba Carrozzo, Carlo Dionisi‐Vici, Luis González‐Gutiérrez‐Solana, Marta Correa‐Vela, Juan Dario Ortigoza‐Escobar, Ángel Sánchez‐Montañez, Élida Vazquez, Ignacio Delgado, Sergio Aguilera‐Albesa, María Eugenia Yoldi, Antonia Ribes, Frederic Tort, Luca Pollini, Serena Galosi, Vincenzo Leuzzi, Manuela Tolve, Laura Pérez‐Gay, Luis Aldamiz‐Echevarría, Mireia Del Toro, Antonio Arranz, Filip Roelens, Roser Urreizti, Rafael Artuch, Alfons Macaya, and Belén Pérez‐Dueñas. Delineating the neurological phenotype in children with defects in the <scp><i>echs1</i></scp> or <scp><i>hibch</i></scp> gene. Aug 2021. URL: https://doi.org/10.1002/jimd.12288, doi:10.1002/jimd.12288. This article has 48 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](3-Hydroxyisobutyryl-CoA_Hydrolase_Deficiency-deep-research-falcon_artifacts/artifact-00.md)
