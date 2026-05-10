---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:23:37.580254'
end_time: '2026-05-09T09:37:33.833932'
duration_seconds: 836.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteochondritis of Tarsal/Metatarsal Bone
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Osteochondritis of Tarsal/Metatarsal Bone
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Osteochondritis of Tarsal/Metatarsal Bone** covering all of the
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
- **Disease Name:** Osteochondritis of Tarsal/Metatarsal Bone
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Osteochondritis of Tarsal/Metatarsal Bone** covering all of the
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


## Comprehensive disease characteristics report: Osteochondritis/Osteochondrosis of tarsal/metatarsal bone

### Scope and entity mapping (important nosology note)
The umbrella phrase **“osteochondritis of tarsal/metatarsal bone”** is not a single well-defined disease entity in the retrieved literature; rather, it most consistently maps to a group of **osteochondroses/osteonecroses** affecting (i) the **tarsal navicular** in children (**Köhler disease**), (ii) the **metatarsal head** (classically the 2nd) in adolescents (**Freiberg disease / Freiberg infraction**), and (iii) the **tarsal navicular** in adults (**Müller–Weiss disease**, spontaneous adult navicular osteonecrosis). (liu2024footpainin pages 8-10, goncalvesdos2024necrosisavasculardel pages 2-4, maruszczak2024lowerlimbosteochondrosis pages 9-10)

Because no ontology/terminology databases (MONDO/Orphanet/MeSH/ICD) were directly queried in the available toolchain for this run, **definitive MONDO IDs, MeSH IDs, Orphanet IDs, and ICD-10/ICD-11 codes could not be verified from primary evidence in the retrieved texts**. The report therefore focuses on evidence-backed clinical entities and their characteristics.

| Entity | Primary bone/joint | Typical age | Sex predominance | Key synonyms | Key imaging features | Notes on etiology/risk factors | Key sources with DOI and year |
|---|---|---|---|---|---|---|---|
| Freiberg disease | Usually 2nd metatarsal head / 2nd metatarsophalangeal joint; less often 3rd, 4th metatarsal head | Adolescence; often adolescent athletes | Female predominance; reported ~5:1 female:male | Freiberg infraction; osteochondrosis/avascular necrosis of the metatarsal head | Radiographs: widening of MTP joint, then subchondral flattening/collapse, sclerosis, fragmentation; MRI: bone marrow edema and subchondral/cartilage defects; US: flattened/fragmented metatarsal head, irregular bony surface, synovial hyperplasia/effusion | Multifactorial; trauma/repetitive microtrauma, mechanical overload, possible vascular insufficiency/watershed supply, mechanical arterial compression; associated systemic disorders reported include hypercoagulability, SLE, diabetes | Carmont et al., 2009, DOI: 10.3113/fai-2009-0167; Kim et al., 2024, DOI: 10.7547/22-025; Liu et al., 2024, DOI: 10.14366/usg.24002 (liu2024footpainin pages 8-10, kim2024shorttermoutcomesof pages 1-2, carmont2009currentconceptsreview pages 1-2) |
| Köhler disease | Tarsal navicular | Usually children; commonly 4–7 years; also described in children <10 years | Male predominance; boys affected about 4 times more often; bilateral in up to 25% | Köhler’s disease; navicular osteochondrosis; avascular necrosis of the navicular in childhood | Radiographs: wafer-thin navicular, bony collapse, fragmentation, patchy sclerosis/increased radiodensity, flattening and loss of normal trabecular pattern; US: unsmooth/bumpy/fragmented navicular ossification center, possible deformity | Self-limited osteochondrosis in skeletally immature children; thought related to delayed/late ossification with increased mechanical compression/loading before complete ossification; trauma and ischemia also implicated | Maruszczak et al., 2024, DOI: 10.3390/app142411795; Liu et al., 2024, DOI: 10.14366/usg.24002; Steinborn & Glaser, 2019, DOI: 10.1055/s-0039-1695721 (liu2024footpainin pages 1-2, steinborn2019normalvariationsand pages 1-2, maruszczak2024lowerlimbosteochondrosis pages 9-10) |
| Müller-Weiss disease | Adult tarsal navicular / midfoot | Adults, typically 4th–6th decades; many diagnosed in 4th–5th decades | Female predominance; about 70% female in reviewed series | Müller-Weiss disease; spontaneous osteonecrosis/avascular necrosis of the navicular | Radiographs: condensation/sclerosis, fragmentation, dorsolateral fragmentation, deformity; may show osteophytes and paradoxical flatfoot; MRI may mimic osteonecrosis | Rare adult navicular osteonecrosis; proposed factors include delayed ossification plus abnormal force distribution, vascular compromise, bone dysplasia/uneven compressive stress, trauma/stress fracture history, childhood physical/nutritional stress; may be unilateral or bilateral | Gonçalves-dos Santos et al., 2024, DOI: 10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4, santos2024avascularnecrosisof pages 1-2) |


*Table: This table maps the umbrella concept of osteochondritis/osteochondrosis affecting tarsal or metatarsal bones to the main clinical entities encountered in practice. It summarizes age/sex patterns, synonymous names, imaging hallmarks, and supported etiologic notes using only the gathered evidence.*

### 1. Disease information
#### 1.1 Definitions (current understanding)
- **Freiberg disease (Freiberg infraction):** described as **osteochondrosis/avascular necrosis of the (usually) second metatarsal head**, presenting at the metatarsophalangeal (MTP) joint. (liu2024footpainin pages 8-10, carmont2009currentconceptsreview pages 1-2)
- **Köhler disease:** **osteochondrosis/avascular necrosis of the tarsal navicular** in children; described as a self-limited osteochondrosis of an ossification center in skeletally immature patients. (liu2024footpainin pages 1-2, tuthill2014imagingoftarsal pages 8-9, maruszczak2024lowerlimbosteochondrosis pages 9-10)
- **Müller–Weiss disease:** **adult navicular avascular necrosis/osteonecrosis** characterized by **deformation, fragmentation, and sclerosis/condensation** of the navicular and associated midfoot pain and deformity patterns. (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4)

#### 1.2 Synonyms / alternate names (examples from the literature)
- Freiberg disease has multiple historical terms (e.g., “Kohler’s second disease”, “eggshell fracture”, “metatarsal epiphysitis”, “osteochondritis deformans metatarsojuvenilis”). (schade2015surgicalmanagementof pages 1-2, carmont2009currentconceptsreview pages 1-2)
- Köhler disease is also explicitly called “avascular necrosis of the navicular bone” in a 2024 review. (maruszczak2024lowerlimbosteochondrosis pages 9-10)
- Müller–Weiss is consistently referred to as “avascular necrosis of the navicular” / “spontaneous osteonecrosis of the navicular” in 2024 systematic-review material. (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4, santos2024avascularnecrosisof pages 1-2)

#### 1.3 Evidence source type
The retrieved evidence is mostly **aggregated disease-level clinical literature** (reviews and systematic reviews) plus a **retrospective surgical cohort** for Freiberg disease; it is not derived from EHR-scale datasets in the retrieved corpus. (goncalvesdos2024necrosisavasculardel pages 1-2, kim2024shorttermoutcomesof pages 1-2, schade2015surgicalmanagementof pages 1-2)

### 2. Etiology
#### 2.1 Causal factors and risk factors
**Freiberg disease**
- Etiology is described as **multifactorial**, with proposed roles for **trauma/microtrauma**, **mechanical arterial compression**, possible **vascular “watershed” vulnerability**, and **systemic disorders** including **hypercoagulability, systemic lupus erythematosus, and diabetes**. (liu2024footpainin pages 8-10, carmont2009currentconceptsreview pages 1-2)
- Vascular anatomy studies in a systematic review context: one cadaveric study reported **65%** of second metatarsals lacked a vascular branch from the first web-space artery; another noted the epiphysis is supplied by small vessels near the joint capsule, hypothesized to be vulnerable to compression. (schade2015surgicalmanagementof pages 1-2)

**Köhler disease**
- 2024 review synthesis suggests the likely driver is **increased mechanical compression/loading of the navicular before complete ossification**, disrupting blood supply and leading to ischemia/avascular necrosis; trauma is also discussed as a possible contributor. (maruszczak2024lowerlimbosteochondrosis pages 9-10)

**Müller–Weiss disease**
- Proposed etiologies in a 2024 systematic review include: delayed ossification plus **abnormal force distribution**, **bone dysplasia/uneven compressive stress**, and **vascular compromise**, with possible contributors such as intensive childhood physical stress, nutritional/environmental/metabolic factors, and trauma/stress fractures. (goncalvesdos2024necrosisavasculardel pages 1-2)

#### 2.2 Protective factors / GxE
No specific protective genetic variants, environmental protective factors, or formal gene–environment interaction studies were identified in the retrieved evidence set.

### 3. Phenotypes
Across entities, pain and functional limitation are dominant, with entity-specific location and imaging findings.

| Entity | Phenotype (plain language) | Phenotype type (symptom/sign/imaging) | Typical onset/age | Frequency (if available) | Suggested HPO term(s) (best-effort) | Supporting citation (with DOI/year) |
|---|---|---|---|---|---|---|
| Freiberg disease | Forefoot chronic pain | Symptom | Adolescence; often adolescent athletic females | not reported | HP:0001836 Pain in the metatarsal region; HP:0001767 Foot pain | Liu et al., 2024, DOI:10.14366/usg.24002 (liu2024footpainin pages 8-10) |
| Freiberg disease | Swelling around the metatarsophalangeal joint | Sign | Adolescence | not reported | HP:0001389 Arthritis; HP:0011463 Swelling of joint | Liu et al., 2024, DOI:10.14366/usg.24002 (liu2024footpainin pages 8-10) |
| Freiberg disease | Tenderness over affected metatarsal head | Sign | Adolescence | not reported | HP:0033748 Tenderness | Liu et al., 2024, DOI:10.14366/usg.24002; Gillespie, 2010, DOI:10.1249/jsr.0b013e3181f19488 (liu2024footpainin pages 8-10, gillespie2010osteochondrosesandapophyseal pages 1-2) |
| Freiberg disease | Restricted metatarsophalangeal joint motion | Sign | Adolescence | not reported | HP:0031372 Reduced joint range of motion | Liu et al., 2024, DOI:10.14366/usg.24002 (liu2024footpainin pages 8-10) |
| Freiberg disease | Focal pain and tenderness | Symptom/sign | Adolescent girls | not reported | HP:0001767 Foot pain; HP:0033748 Tenderness | Reginelli et al., 2018, DOI:10.23750/abm.v89i1-s.7009 (steinborn2019normalvariationsand pages 1-2) |
| Freiberg disease | Widening of the MTP joint, followed by metatarsal head collapse and sclerosis on radiographs | Imaging | Adolescence | not reported | HP:0001363 Osteonecrosis; HP:0100807 Abnormality of the metatarsal bones | Gillespie, 2010, DOI:10.1249/jsr.0b013e3181f19488 (gillespie2010osteochondrosesandapophyseal pages 1-2) |
| Freiberg disease | Flattened/fragmented metatarsal head with rough irregular bony surface on ultrasound | Imaging | Adolescence | not reported | HP:0100807 Abnormality of the metatarsal bones; HP:0001363 Osteonecrosis | Liu et al., 2024, DOI:10.14366/usg.24002 (liu2024footpainin pages 8-10) |
| Freiberg disease | Bone marrow edema and subchondral/cartilage defects on MRI | Imaging | Adolescence to adulthood | not reported | HP:0011849 Abnormality of the epiphysis; HP:0001363 Osteonecrosis | Kim et al., 2024, DOI:10.7547/22-025 (kim2024shorttermoutcomesof pages 1-2) |
| Köhler disease | Dorsomedial midfoot pain | Symptom | Children, usually 4–7 years | not reported | HP:0001767 Foot pain | Maruszczak et al., 2024, DOI:10.3390/app142411795 (maruszczak2024lowerlimbosteochondrosis pages 9-10) |
| Köhler disease | Local swelling over navicular region | Sign | Children, usually 4–7 years | not reported | HP:0001389 Arthritis; HP:0011463 Swelling of joint | Maruszczak et al., 2024, DOI:10.3390/app142411795 (maruszczak2024lowerlimbosteochondrosis pages 9-10) |
| Köhler disease | Tenderness over navicular | Sign | Children <10 years; commonly 4–7 years | not reported | HP:0033748 Tenderness | Maruszczak et al., 2024, DOI:10.3390/app142411795 (maruszczak2024lowerlimbosteochondrosis pages 9-10) |
| Köhler disease | Limp favoring the lateral side of the foot | Sign | Children, usually 4–7 years | not reported | HP:0002204 Abnormal gait; HP:0002515 Limping | Maruszczak et al., 2024, DOI:10.3390/app142411795 (maruszczak2024lowerlimbosteochondrosis pages 9-10) |
| Köhler disease | Bilateral involvement | Sign/distribution | Children younger than 10 years | up to 25% | HP:0012832 Bilateral | Liu et al., 2024, DOI:10.14366/usg.24002 (liu2024footpainin pages 1-2) |
| Köhler disease | Unsmooth, bumpy, fragmented, sometimes deformed navicular ossification center on ultrasound | Imaging | Children younger than 10 years | not reported | HP:0000925 Abnormality of the skeletal system; HP:0011849 Abnormality of the epiphysis | Liu et al., 2024, DOI:10.14366/usg.24002 (liu2024footpainin pages 1-2) |
| Köhler disease | Wafer-thin navicular with collapse, fragmentation, patchy sclerosis, and increased radiodensity on radiographs | Imaging | Children, usually 4–7 years | not reported | HP:0001363 Osteonecrosis; HP:0000925 Abnormality of the skeletal system | Maruszczak et al., 2024, DOI:10.3390/app142411795 (maruszczak2024lowerlimbosteochondrosis pages 9-10) |
| Köhler disease | Navicular flattening, increased density, and fragmentation on radiographs | Imaging | Children aged ~3–9 years | not reported | HP:0001363 Osteonecrosis; HP:0000925 Abnormality of the skeletal system | Steinborn & Glaser, 2019, DOI:10.1055/s-0039-1695721 (steinborn2019normalvariationsand pages 1-2) |
| Müller-Weiss disease | Chronic midfoot pain | Symptom | Adults, typically 4th–6th decades | not reported | HP:0001767 Foot pain | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 1-2) |
| Müller-Weiss disease | Long-term mechanical dorsal foot pain | Symptom | Adults, usually diagnosed in 4th–5th decades | not reported | HP:0001767 Foot pain | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 2-4) |
| Müller-Weiss disease | Midfoot varus deformity | Sign | Adults, 4th–6th decades | not reported | HP:0004689 Varus deformity of foot | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 1-2) |
| Müller-Weiss disease | Ankle instability | Sign/symptom | Adults | not reported | HP:0002141 Ankle instability | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 2-4) |
| Müller-Weiss disease | Reduced subtalar mobility | Sign | Adults | not reported | HP:0031372 Reduced joint range of motion | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 2-4) |
| Müller-Weiss disease | Peroneal tendonitis | Sign | Adults | not reported | HP:0100526 Tendinitis | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 2-4) |
| Müller-Weiss disease | Condensation/sclerosis and fragmentation of the navicular on radiographs | Imaging | Adults, 4th–6th decades | not reported | HP:0001363 Osteonecrosis; HP:0000925 Abnormality of the skeletal system | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 1-2, santos2024avascularnecrosisof pages 1-2) |
| Müller-Weiss disease | Osteophytes and dorsolateral fragmentation of the navicular | Imaging | Adults | not reported | HP:0002808 Osteophyte; HP:0001363 Osteonecrosis | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 2-4) |
| Müller-Weiss disease | Paradoxical flatfoot | Sign/imaging | Adults | not reported | HP:0001762 Flat feet | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 2-4) |
| Müller-Weiss disease | Bilateral or unilateral involvement | Sign/distribution | Adults | not reported | HP:0012832 Bilateral | Gonçalves-dos Santos et al., 2024, DOI:10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 2-4) |


*Table: This table summarizes key clinical and imaging phenotypes reported in context for Freiberg disease, Köhler disease, and Müller-Weiss disease. It is useful for building phenotype annotations and suggested HPO mappings while clearly marking where frequencies were not reported.*

### 4. Genetic / molecular information
- The pediatric imaging-focused review describes Freiberg’s disease etiology as including possible **“genetic susceptibility”** among multiple factors, but **no specific genes/variants, inheritance patterns, or ClinVar-grade pathogenic variants** were identified in the retrieved corpus. (liu2024footpainin pages 8-10)
- Consequently, **no causal genes** can be asserted from the retrieved evidence. The current retrieved literature supports predominantly **biomechanical/vascular/ossification-timing** hypotheses rather than a monogenic etiology for these specific entities. (goncalvesdos2024necrosisavasculardel pages 1-2, maruszczak2024lowerlimbosteochondrosis pages 9-10, carmont2009currentconceptsreview pages 1-2)

### 5. Environmental information
The evidence base emphasizes **mechanical load/repetitive stress** and (for adult navicular osteonecrosis) systemic/metabolic contributors as possible factors, rather than discrete toxins or infectious causes. (goncalvesdos2024necrosisavasculardel pages 1-2, maruszczak2024lowerlimbosteochondrosis pages 9-10)

### 6. Mechanism / pathophysiology (causal chains)
#### 6.1 Osteochondrosis as a process (general)
A sports-medicine review describes osteochondroses as “bone-cartilage conditions” associated with disturbed endochondral ossification and a typical sequence of **necrosis → revascularization → granulation/invasion → osteoclast resorption → osteoid replacement and lamellar bone formation**. (gillespie2010osteochondrosesandapophyseal pages 1-2)

#### 6.2 Entity-specific mechanistic hypotheses
- **Freiberg disease:** proposed chain includes repetitive microtrauma/overload in a vulnerable epiphysis during growth, plus compromised blood supply (e.g., anatomically variable arterial supply) leading to subchondral necrosis/structural collapse and degenerative changes. (carmont2009currentconceptsreview pages 1-2)
- **Köhler disease:** mechanical compression/loading of the navicular during incomplete ossification is proposed to disrupt blood supply, causing ischemia and transient osteonecrosis with later resolution (self-limited course). (maruszczak2024lowerlimbosteochondrosis pages 9-10)
- **Müller–Weiss disease:** overload and compressive deformation of the navicular within the medial arch, plus vascular obstruction and stress fracture/trauma contributions, are proposed to lead to chronic fragmentation/deformity and arthritic changes with pain and gait alteration. (goncalvesdos2024necrosisavasculardel pages 2-4)

**Suggested GO biological processes (best-effort, not explicitly asserted in retrieved texts):** endochondral ossification; bone remodeling; angiogenesis; response to mechanical stress.

**Suggested CL cell types (best-effort):** osteoblast; osteoclast; chondrocyte; endothelial cell.

### 7. Anatomical structures affected
- **Freiberg:** metatarsal head and MTP joint (classically 2nd). (carmont2009currentconceptsreview pages 1-2)
- **Köhler:** tarsal navicular in the midfoot. (liu2024footpainin pages 1-2, maruszczak2024lowerlimbosteochondrosis pages 9-10)
- **Müller–Weiss:** tarsal navicular with associated perinavicular arthritis and midfoot deformity (e.g., midfoot varus; paradoxical flatfoot). (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4)

**UBERON suggestions (best-effort):** navicular bone of foot; metatarsal bone; metatarsophalangeal joint; midfoot.

### 8. Temporal development
- **Köhler:** pediatric onset (commonly ~4–7 years in 2024 review). (maruszczak2024lowerlimbosteochondrosis pages 9-10)
- **Freiberg:** onset typically during adolescence/skeletal growth; clinical series included Smillie stages I–V at treatment. (kim2024shorttermoutcomesof pages 1-2, carmont2009currentconceptsreview pages 1-2)
- **Müller–Weiss:** adult onset/diagnosis primarily in 4th–6th decades; systematic review reports ages 28–69 with most patients >40. (goncalvesdos2024necrosisavasculardel pages 2-4)

### 9. Inheritance and population / epidemiology
#### 9.1 Demographics (from retrieved sources)
- **Köhler:** male predominance; bilateral involvement **up to 25%**. (liu2024footpainin pages 1-2)
- **Freiberg:** strong predilection for adolescent athletic females; female:male ratio reported as ~**5:1**. (liu2024footpainin pages 8-10, carmont2009currentconceptsreview pages 1-2)
- **Müller–Weiss:** systematic review across included studies reports **134 patients (138 feet)** with **female predominance ~70%** and typical diagnosis in the 4th–5th decades. (goncalvesdos2024necrosisavasculardel pages 2-4)

#### 9.2 Prevalence/incidence
No population-based prevalence/incidence estimates for these entities were identified in the retrieved evidence set.

### 10. Diagnostics
#### 10.1 Imaging and clinical workup
- **Radiography** is repeatedly identified as front-line for Köhler and Freiberg; Freiberg commonly uses radiographs for **Smillie staging**. (kim2024shorttermoutcomesof pages 2-6, maruszczak2024lowerlimbosteochondrosis pages 9-10)
- **MRI** is emphasized for detecting **bone marrow edema** and subchondral/cartilage abnormalities (Freiberg), and for evaluating navicular osteonecrosis-like changes (Müller–Weiss). (liu2024footpainin pages 8-10, kim2024shorttermoutcomesof pages 2-6, goncalvesdos2024necrosisavasculardel pages 2-4)
- **High-frequency musculoskeletal ultrasound** is described as a useful pediatric modality for diagnosis and monitoring, capable of visualizing bone surfaces and adjacent soft tissues in real time; ultrasonographic patterns are described for Köhler and Freiberg. (liu2024footpainin pages 1-2, liu2024footpainin pages 8-10)

#### 10.2 Freiberg staging/classification (Smillie)
A 2024 retrospective arthroscopy cohort restates Smillie I–V definitions (I fissure+sclerosis; II cancellous absorption with dorsal sinking; III absorption with bony projections; IV loose body; V arthrosis with flattening/deformity) and reports surgical outcomes across stages. (kim2024shorttermoutcomesof pages 1-2)

### 11. Outcome / prognosis
- **Köhler:** characterized as **self-limiting** in a 2024 review, supporting a generally favorable prognosis with conservative management. (maruszczak2024lowerlimbosteochondrosis pages 9-10)
- **Freiberg:** surgical literature suggests many procedures can relieve pain and restore activity; systematic review notes joint-sparing procedures are reported more often and appear to have better prognosis for symptom resolution and return to activity. (schade2015surgicalmanagementof pages 1-2)
- **Müller–Weiss:** chronic course with long-term mechanical pain; treatment selection is stage-dependent, and classification/consensus limitations are noted in 2024 systematic review material. (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4)

### 12. Treatment
A consolidated treatment-and-outcomes table is provided below.

| Entity | First-line diagnostics | Key staging/classification | Conservative treatments | Surgical options | Reported outcomes/statistics (with numbers, follow-up) when available | Suggested MAXO terms (best-effort) | Supporting citations |
|---|---|---|---|---|---|---|---|
| Freiberg disease | Plain radiographs for diagnosis and Smillie staging; follow-up radiographs; MRI to assess bone marrow edema, subchondral cortical irregularity, and cartilage defects; ultrasound can show flattened/fragmented metatarsal head, irregular bony surface, synovial hyperplasia, effusion, Doppler angiogenesis | Smillie I-V: I fissure+sclerosis; II cancellous absorption with dorsal cartilage sinking; III further absorption with medial/lateral projections; IV central loose body; V arthrosis with flattening/deformity | Rest, activity modification, footwear modification, orthosis/padding, NSAIDs, immobilization | Arthroscopic synovectomy/debridement/chondroplasty/microfracture; core decompression; debridement; perichondral grafting; dorsal closing-wedge osteotomy; osteochondral autologous transplantation (OAT); arthroplasty; metatarsal head restoration/resection | Arthroscopy series: 13 patients/15 feet, 12-month radiographs showed no progression; AOFAS improved from 39.67±5.04 pre-op to 93.07±1.83 at 12 months; VAS 7.20±1.42 to 1.80±0.41; ROM 33.67°±4.81° to 51.67°±5.23°; return to normal activities in 4-6 weeks (12-month follow-up) (kim2024shorttermoutcomesof pages 2-6, kim2024shorttermoutcomesof pages 6-7). Systematic review: 257 joint-sparing procedures, mean follow-up 30.4 months, >90% pain resolution/full return to activity; 70 joint-destructive procedures, mean follow-up 15.0 months, >70% pain resolution/full return to activity (schade2015surgicalmanagementof pages 1-2). Adult late-stage comparative study: OAT AOFAS 95.7 vs DCWMO 87.9 at final follow-up; fewer complications with OAT (kim2020comparisonofosteochondral pages 7-7) | MAXO: physical activity modification; orthopedic insole/orthotic use; NSAID therapy; immobilization/casting; arthroscopic debridement; microfracture surgery; osteotomy; osteochondral graft transplantation; arthroplasty | (liu2024footpainin pages 8-10, kim2024shorttermoutcomesof pages 1-2, schade2015surgicalmanagementof pages 1-2, kim2020comparisonofosteochondral pages 7-7, kim2024shorttermoutcomesof pages 2-6, kim2024shorttermoutcomesof pages 6-7) |
| Köhler disease | Radiographs are the diagnostic method of choice; ultrasound can show unsmooth/bumpy/fragmented or deformed navicular ossification center; CT or MRI if symptoms fail to improve or more detail is needed | No formal staging/classification identified in retrieved context | Rest, ice, firm-soled shoes, arch supports, non-weight-bearing crutches, immobilization with cast (~6 weeks) or controlled-ankle-motion shoe, NSAIDs | Usually no surgery indicated; refractory pediatric cases reported with navicular decompression and microcirculation reconstruction | Disease is self-limiting; bilateral involvement reported in up to 25% (diagnostic/epidemiologic statistic). Small surgical series: 3 pediatric patients had pain resolution within 3 months and restoration of navicular density after decompression/microcirculation reconstruction (liu2024footpainin pages 1-2, maruszczak2024lowerlimbosteochondrosis pages 9-10) | MAXO: rest; cryotherapy; shoe modification; arch support; assistive device use/crutches; non-weight-bearing; cast immobilization; NSAID therapy; navicular decompression surgery | (liu2024footpainin pages 1-2, maruszczak2024lowerlimbosteochondrosis pages 9-10) |
| Müller-Weiss disease | Radiographs showing osteophytes, sclerosis/condensation, fragmentation, dorsolateral navicular fragmentation; MRI when radiographs are equivocal and for osteonecrosis-like changes; functional assessment often with AOFAS and VAS in studies | Early vs advanced stages referenced; early stages noted as S1-S2 in review context, but no full staging scheme provided in retrieved text | Conservative treatment may be used in early stages; reported as giving acute symptomatic improvement and favorable evaluation in S1-S2; biomechanical offloading considerations implied by altered plantar pressures | Arthrodesis most common (isolated talonavicular, double, triple/perinavicular), calcaneal osteotomy, grafting | Systematic review included 17 studies with 134 patients (138 feet); ages 28-69 years; most >40 years; females ~70%; conservative treatment favorable in early S1-S2, surgery preferred in remaining stages; outcomes commonly measured with AOFAS and VAS, but pooled quantitative response rates not available in retrieved context (goncalvesdos2024necrosisavasculardel pages 2-4). Another review states isolated talonavicular arthrodesis gives good results in early stages, with double/triple arthrodesis used in advanced disease (goncalvesdos2024necrosisavasculardel pages 1-2, santos2024avascularnecrosisof pages 1-2) | MAXO: activity modification; analgesic/NSAID therapy; orthotic/offloading support; talonavicular arthrodesis; double arthrodesis; triple arthrodesis; calcaneal osteotomy; bone grafting | (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4, santos2024avascularnecrosisof pages 1-2) |


*Table: This table summarizes diagnostic approaches, staging systems, conservative care, surgical options, and reported outcomes for Freiberg disease, Köhler disease, and Müller-Weiss disease. It is useful for comparing how these related tarsal/metatarsal osteochondroses are diagnosed and managed in current evidence.*

#### Visual evidence from recent clinical series (Freiberg)
A cropped outcome table and outcome figure from the 2024 arthroscopic Freiberg series provide visual confirmation of the **AOFAS/VAS/ROM improvements** summarized in Artifact-02. (kim2024shorttermoutcomesof media 28b80a18, kim2024shorttermoutcomesof media 2d3231ac)

### 13. Prevention
No disease-specific primary prevention programs or screening protocols were identified in the retrieved evidence set. Practical prevention concepts implied by etiology include **load management / activity modification** and early evaluation of persistent forefoot/midfoot pain in at-risk groups (adolescent athletes; active children; adults with chronic midfoot pain). (liu2024footpainin pages 8-10, maruszczak2024lowerlimbosteochondrosis pages 9-10, goncalvesdos2024necrosisavasculardel pages 2-4)

### 14. Other species / natural disease
No veterinary/natural disease evidence specific to these tarsal/metatarsal entities was retrieved in this run.

### 15. Model organisms
No model-organism–based mechanistic studies specific to these entities were retrieved in this run.

## Recent developments (2023–2024 emphasis)
- **Broader adoption/positioning of musculoskeletal ultrasound in pediatric foot pain evaluation** (including osteochondroses such as Köhler and Freiberg) is emphasized in a 2024 review, highlighting real-time imaging and monitoring potential beyond radiography/MRI in young patients. Publication: **May 2024**; URL: https://doi.org/10.14366/usg.24002 (liu2024footpainin pages 1-2, liu2024footpainin pages 8-10)
- **Updated synthesis of lower-limb osteochondroses in young athletes** includes a dedicated Köhler section with practical conservative treatment recommendations and radiographic hallmarks. Publication: **Dec 2024**; URL: https://doi.org/10.3390/app142411795 (maruszczak2024lowerlimbosteochondrosis pages 9-10)
- **Stage-inclusive arthroscopic management data for Freiberg disease**: a 2024 retrospective study reports significant improvements in validated clinical scores and motion at 12 months across Smillie stages, supporting arthroscopy (debridement/microfracture-based) as a real-world option even across radiographic stages (short-term evidence). Publication: **May/June 2024**; URL: https://doi.org/10.7547/22-025 (kim2024shorttermoutcomesof pages 2-6, kim2024shorttermoutcomesof pages 6-7)
- **Müller–Weiss evidence remains limited and heterogeneous**: a 2024 systematic review notes limited studies, variable approaches, and the need for long-term outcomes/complication data; it also summarizes available demographic patterns (female predominance; typical 4th–6th decade). Publication: **Jan 2024**; URL: https://doi.org/10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4)

## Expert opinion / evidence-quality considerations
- The Freiberg systematic review concludes that joint-sparing procedures are more commonly reported and appear to have better prognosis for symptom resolution/return to activity, but also highlights inconsistency in staging usage (“Smillie stage was not consistently …”). This reflects a broader limitation: most data are case series and retrospective cohorts rather than randomized trials. (schade2015surgicalmanagementof pages 1-2)
- For Müller–Weiss, the 2024 systematic review characterizes the disease as rare with small study samples and notes that additional classifications might be needed/validated, again reflecting evidence scarcity and the importance of standardized staging/outcome reporting. (goncalvesdos2024necrosisavasculardel pages 2-4)

## Key statistics (from the retrieved evidence)
- Köhler disease: bilateral involvement **up to 25%**. (liu2024footpainin pages 1-2)
- Freiberg disease: female:male ratio reported ~**5:1**. (carmont2009currentconceptsreview pages 1-2)
- Müller–Weiss systematic review: **134 patients (138 feet)**; age range **28–69**; **~70% female**. (goncalvesdos2024necrosisavasculardel pages 2-4)
- Freiberg arthroscopy cohort (n=13 patients/15 feet): AOFAS improved **39.67±5.04 → 93.07±1.83** at 12 months; VAS **7.20±1.42 → 1.80±0.41**; ROM **33.67°±4.81° → 51.67°±5.23°**, P=.001. (kim2024shorttermoutcomesof pages 2-6, kim2024shorttermoutcomesof pages 6-7)
- Freiberg systematic review: **257 joint-sparing** procedures (mean follow-up **30.4 months**) with **>90%** pain resolution/return to activity; **70 joint-destructive** procedures (mean follow-up **15.0 months**) with **>70%** pain resolution/return to activity. (schade2015surgicalmanagementof pages 1-2)

## Evidence gaps relative to knowledge-base template
- **Ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM)**: not extractable from the retrieved texts in this run.
- **Genetics/variants**: no specific genes/variants identified; only nonspecific “genetic susceptibility” mentioned for Freiberg among multifactorial risk factors. (liu2024footpainin pages 8-10)
- **Incidence/prevalence**: no population-level estimates found in retrieved evidence.
- **Clinical trials**: no clearly relevant interventional trials were identified from the clinical-trials search results used in this run.

### Primary source URL list (publication date when available)
- Liu L, Wang T, Qi H. *Ultrasonography* **May 2024**. https://doi.org/10.14366/usg.24002 (liu2024footpainin pages 1-2, liu2024footpainin pages 8-10)
- Maruszczak K, Madej T, Gawda P. *Applied Sciences* **Dec 2024**. https://doi.org/10.3390/app142411795 (maruszczak2024lowerlimbosteochondrosis pages 9-10)
- Kim J-K et al. *J Am Podiatr Med Assoc* **May/June 2024**. https://doi.org/10.7547/22-025 (kim2024shorttermoutcomesof pages 2-6, kim2024shorttermoutcomesof pages 6-7)
- Gonçalves-dos Santos R et al. *Acta Ortopédica Mexicana* **Jan 2024**. https://doi.org/10.35366/117381 (goncalvesdos2024necrosisavasculardel pages 1-2, goncalvesdos2024necrosisavasculardel pages 2-4)
- Schade VL. *Foot & Ankle Specialist* **May 2015**. https://doi.org/10.1177/1938640015585966 (schade2015surgicalmanagementof pages 1-2)
- Carmont MR et al. *Foot & Ankle International* **Feb 2009**. https://doi.org/10.3113/fai-2009-0167 (carmont2009currentconceptsreview pages 1-2)

**PMID note:** PMIDs were not present in the retrieved text excerpts for these articles; therefore PMID-based citations could not be provided from the available evidence context.

References

1. (liu2024footpainin pages 8-10): Lihua Liu, Tiezheng Wang, and Hengtao Qi. Foot pain in children and adolescents: a problem-based approach in musculoskeletal ultrasonography. Ultrasonography, 43:193-208, May 2024. URL: https://doi.org/10.14366/usg.24002, doi:10.14366/usg.24002. This article has 7 citations.

2. (goncalvesdos2024necrosisavasculardel pages 2-4): Santos R Gonçalves-dos, V. Furtuoso-Junior, W. L. Pinto de Barros-Moreira, A. Assunção-Tostes, F. Caixeta, and T. dos Santos-Carneiro. Necrosis avascular del navicular (müller-weiss). una revisión sistemática. Acta Ortopédica Mexicana, 38:333-339, Jan 2024. URL: https://doi.org/10.35366/117381, doi:10.35366/117381. This article has 0 citations.

3. (maruszczak2024lowerlimbosteochondrosis pages 9-10): Krystian Maruszczak, Tomasz Madej, and Piotr Gawda. Lower limb osteochondrosis and apophysitis in young athletes—a comprehensive review. Applied Sciences, 14:11795, Dec 2024. URL: https://doi.org/10.3390/app142411795, doi:10.3390/app142411795. This article has 2 citations.

4. (kim2024shorttermoutcomesof pages 1-2): Jong-Kil Kim, Do-Yeon Kim, Jong-Sung Oh, Dong-ill Ko, and Kwang-Bok Lee. Short-term outcomes of arthroscopic treatment of freiberg disease. Journal of the American Podiatric Medical Association, May 2024. URL: https://doi.org/10.7547/22-025, doi:10.7547/22-025. This article has 0 citations and is from a peer-reviewed journal.

5. (carmont2009currentconceptsreview pages 1-2): Michael R. Carmont, Robin J. Rees, and Christopher M. Blundell. Current concepts review: freiberg's disease. Foot & Ankle International, 30:167-176, Feb 2009. URL: https://doi.org/10.3113/fai-2009-0167, doi:10.3113/fai-2009-0167. This article has 139 citations and is from a peer-reviewed journal.

6. (liu2024footpainin pages 1-2): Lihua Liu, Tiezheng Wang, and Hengtao Qi. Foot pain in children and adolescents: a problem-based approach in musculoskeletal ultrasonography. Ultrasonography, 43:193-208, May 2024. URL: https://doi.org/10.14366/usg.24002, doi:10.14366/usg.24002. This article has 7 citations.

7. (steinborn2019normalvariationsand pages 1-2): Marc Steinborn and Christian Glaser. Normal variations and pathologic disorders of chondrification and ossification of the foot and related diseases. Seminars in Musculoskeletal Radiology, 23:497-510, Sep 2019. URL: https://doi.org/10.1055/s-0039-1695721, doi:10.1055/s-0039-1695721. This article has 7 citations and is from a peer-reviewed journal.

8. (goncalvesdos2024necrosisavasculardel pages 1-2): Santos R Gonçalves-dos, V. Furtuoso-Junior, W. L. Pinto de Barros-Moreira, A. Assunção-Tostes, F. Caixeta, and T. dos Santos-Carneiro. Necrosis avascular del navicular (müller-weiss). una revisión sistemática. Acta Ortopédica Mexicana, 38:333-339, Jan 2024. URL: https://doi.org/10.35366/117381, doi:10.35366/117381. This article has 0 citations.

9. (santos2024avascularnecrosisof pages 1-2): RG Santos, VF Furtuoso-Junior, and WL Moreira. Avascular necrosis of the navicular (müller-weiss). a systematic review. Unknown journal, 2024.

10. (tuthill2014imagingoftarsal pages 8-9): Heidi L. Tuthill, Evan R. Finkelstein, Allen M. Sanchez, Paul D. Clifford, Ty K. Subhawong, and Jean Jose. Imaging of tarsal navicular disorders. Foot & Ankle Specialist, 7:210-224, Mar 2014. URL: https://doi.org/10.1177/1938640014528042, doi:10.1177/1938640014528042. This article has 49 citations.

11. (schade2015surgicalmanagementof pages 1-2): Valerie L. Schade. Surgical management of freiberg’s infraction. Foot & Ankle Specialist, 8:498-519, May 2015. URL: https://doi.org/10.1177/1938640015585966, doi:10.1177/1938640015585966. This article has 49 citations.

12. (gillespie2010osteochondrosesandapophyseal pages 1-2): Heather Gillespie. Osteochondroses and apophyseal injuries of the foot in the young athlete. Current Sports Medicine Reports, 9:265-268, Sep 2010. URL: https://doi.org/10.1249/jsr.0b013e3181f19488, doi:10.1249/jsr.0b013e3181f19488. This article has 103 citations and is from a peer-reviewed journal.

13. (kim2024shorttermoutcomesof pages 2-6): Jong-Kil Kim, Do-Yeon Kim, Jong-Sung Oh, Dong-ill Ko, and Kwang-Bok Lee. Short-term outcomes of arthroscopic treatment of freiberg disease. Journal of the American Podiatric Medical Association, May 2024. URL: https://doi.org/10.7547/22-025, doi:10.7547/22-025. This article has 0 citations and is from a peer-reviewed journal.

14. (kim2024shorttermoutcomesof pages 6-7): Jong-Kil Kim, Do-Yeon Kim, Jong-Sung Oh, Dong-ill Ko, and Kwang-Bok Lee. Short-term outcomes of arthroscopic treatment of freiberg disease. Journal of the American Podiatric Medical Association, May 2024. URL: https://doi.org/10.7547/22-025, doi:10.7547/22-025. This article has 0 citations and is from a peer-reviewed journal.

15. (kim2020comparisonofosteochondral pages 7-7): Sung Jae Kim, Young Woo Kim, Jin Ho Park, and Gab Lae Kim. Comparison of osteochondral autologous transplantation and dorsiflexion closing wedge metatarsal osteotomy for late-stage freiberg disease in adults. Foot & Ankle International, 41:529-535, Feb 2020. URL: https://doi.org/10.1177/1071100720904363, doi:10.1177/1071100720904363. This article has 14 citations and is from a peer-reviewed journal.

16. (kim2024shorttermoutcomesof media 28b80a18): Jong-Kil Kim, Do-Yeon Kim, Jong-Sung Oh, Dong-ill Ko, and Kwang-Bok Lee. Short-term outcomes of arthroscopic treatment of freiberg disease. Journal of the American Podiatric Medical Association, May 2024. URL: https://doi.org/10.7547/22-025, doi:10.7547/22-025. This article has 0 citations and is from a peer-reviewed journal.

17. (kim2024shorttermoutcomesof media 2d3231ac): Jong-Kil Kim, Do-Yeon Kim, Jong-Sung Oh, Dong-ill Ko, and Kwang-Bok Lee. Short-term outcomes of arthroscopic treatment of freiberg disease. Journal of the American Podiatric Medical Association, May 2024. URL: https://doi.org/10.7547/22-025, doi:10.7547/22-025. This article has 0 citations and is from a peer-reviewed journal.