---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T07:57:46.631016'
end_time: '2026-05-06T08:24:29.975005'
duration_seconds: 1603.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cervical Artery Dissection
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cervical Artery Dissection
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Artery Dissection** covering all of the
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
- **Disease Name:** Cervical Artery Dissection
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Artery Dissection** covering all of the
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


# Cervical Artery Dissection (CeAD) — Comprehensive Disease Characteristics Report

**Target disease:** Cervical Artery Dissection (carotid and/or vertebral artery dissection, typically extracranial).  
**Category:** Complex (multifactorial; small monogenic fraction).  
**Evidence note:** Many retrieved full texts/abstracts did **not** include PMIDs in-line; therefore, citations are given to the retrieved sources by evidence IDs plus DOI/URL and publication date when available.

---

## Executive quantitative summary

| Domain | Key finding (with numbers) | Study/source (short) | Publication year | URL |
|---|---|---|---|---|
| Incidence and age | Extracranial artery dissection incidence ~2.6–3.0 per 100,000/year; mean age for EAD ~44 years (debette2021esoguidelinefor pages 2-4) | ESO guideline | 2021 | https://doi.org/10.1177/23969873211046475 |
| Proportion of ischemic presentations | EAD complicated by cerebral ischemia in about two thirds to three quarters of series (debette2021esoguidelinefor pages 1-2); in a real-world cohort, ischemic symptoms in 43/62 (69%) with TIA 16%, minor stroke 27%, major stroke 25% (lodato2025tenyearoutcomesof pages 5-9) | ESO guideline; Lodato et al. | 2021; 2025 | https://doi.org/10.1177/23969873211046475; https://doi.org/10.3390/jcm14196836 |
| Recanalization and aneurysm evolution | Stenosis recanalizes in 33–90% within 6 months; dissecting aneurysms resolve/decrease in 40–50%; CADISS-related data: 24/264 aneurysms at baseline vs 36/248 at 3 months, with 12 persistent and 24 new (debette2021esoguidelinefor pages 2-4) | ESO guideline | 2021 | https://doi.org/10.1177/23969873211046475 |
| TREAT-CAD outcomes | Primary endpoint: 23.1% (21/91) aspirin vs 14.6% (12/82) VKA; ischemic stroke: 7/91 (7.7%) vs 0/82; major extracranial hemorrhage: 0 vs 1/82 (1.2%); no deaths (engelter2021aspirinversusanticoagulation pages 7-11) | TREAT-CAD RCT | 2021 | https://doi.org/10.1016/S1474-4422(21)00044-2 |
| ESO guideline key recommendations | Acute symptomatic EAD: IV alteplase within 4.5 h if eligible; mechanical thrombectomy for anterior-circulation LVO; either anticoagulants or antiplatelets may be prescribed in acute symptomatic EAD; expert consensus supports DOACs as possible VKA substitutes and short-term DAPT for TIA/minor stroke (debette2021esoguidelinefor pages 42-43, debette2021esoguidelinefor pages 37-41) | ESO guideline | 2021 | https://doi.org/10.1177/23969873211046475 |
| HRMR-VWI vs MRA findings | In 34 patients/38 vessels, HRMR-VWI detected typical signs in all acute/subacute patients; intimal flap/double-lumen detection superior to MRA (P=0.012); IMH and grade II enhancement higher in acute/subacute vs chronic stage (P=0.000/0.000/0.016); MRA stage differences not significant (P=0.902) (ma2023imaginginvestigationof pages 1-2, ma2023imaginginvestigationof pages 6-9) | Ma et al. imaging study | 2023 | https://doi.org/10.1186/s12880-023-01133-z |
| STOP-CAD TCD survey | 29/58 centers (50%) routinely used TCD; European vs North American use 76.4% vs 34.3% (P=0.007); after HITS detection, 32.8% switched from antiplatelet to anticoagulation; 20.7% switched DAPT to anticoagulation; 12.1% switched SAPT to anticoagulation (guo2024applicationoftranscranial pages 1-2, guo2024applicationoftranscranial pages 4-4, guo2024applicationoftranscranial pages 3-3) | Guo et al. STOP-CAD survey | 2024 | https://doi.org/10.1002/neo2.70004 |
| Long-term outcome cohort | Median follow-up 78 months: recurrent ischemic stroke in 2 patients (4%), both within 12 months; 10-year overall survival 71%; 10-year stroke/death-free survival 70%; medically treated subgroup stroke/death-free survival 86% with anticoagulation vs 67% with antiplatelets (lodato2025tenyearoutcomesof pages 5-9) | Lodato et al. cohort | 2025 | https://doi.org/10.3390/jcm14196836 |


*Table: This table compiles the main quantitative findings for cervical artery dissection across epidemiology, presentation, imaging, treatment trials, guideline recommendations, implementation surveys, and long-term outcomes. It is useful as a quick-reference evidence summary anchored to the retrieved context IDs.*

Key guideline recommendation tables (ESO) were also retrieved as images (debette2021esoguidelinefor media df12240a, debette2021esoguidelinefor media 106e3d8a).

---

## 1. Disease Information

### 1.1 Overview (current understanding)
Cervical artery dissection (CeAD; also “cervical artery dissection/CAD”) is defined by **intramural hematoma** in the wall of the cervical portion of the **internal carotid artery** and/or **vertebral artery**, often producing stenosis/occlusion or a dissecting aneurysm and predisposing to thromboembolism and ischemic stroke. (engelter2021cervicalandintracranial pages 1-2, debette2021esoguidelinefor pages 1-2)

**Direct quote (definition hallmark):** the Engelter et al. review describes CeAD as having the “**hallmark intramural hematoma** of the cervical portion of the internal carotid or vertebral arteries.” (engelter2021cervicalandintracranial pages 1-2)

The European Stroke Organisation (ESO) guideline uses the term **extracranial artery dissection (EAD)** to refer to dissections of the **cervical carotid or vertebral arteries** and contrasts this with **intracranial artery dissection (IAD)**; EAD/IAD are confirmed by characteristic radiologic signs (mural hematoma, dissecting aneurysm, long tapering stenosis, intimal flap, double lumen, etc.). (debette2021esoguidelinefor pages 2-4)

### 1.2 Key identifiers (ontology/coding)
* **MONDO / Orphanet / OMIM / MeSH / ICD-10/ICD-11:** Not retrievable from the current tool evidence set (no authoritative coding tables were present in the retrieved texts). This should be populated from ontology resources (MONDO, MeSH, ICD) directly.

### 1.3 Synonyms and alternative names
* Cervical artery dissection (CeAD) (engelter2021cervicalandintracranial pages 1-2)  
* Cervical artery dissection (CAD) (common abbreviation in multiple sources) (filip2023cervicalarterydissections—a pages 1-2)  
* Extracranial artery dissection (EAD; ESO terminology) (debette2021esoguidelinefor pages 2-4)  
* Carotid artery dissection; vertebral artery dissection (subtypes) (engelter2021cervicalandintracranial pages 1-2, filip2023cervicalarterydissections—a pages 1-2)

### 1.4 Evidence provenance (patient-level vs aggregated)
The knowledge base content here is derived from **aggregated disease-level resources** (ESO guideline; systematic reviews) and **patient cohorts** / pragmatic studies (single-center case series, retrospective cohort, multicenter survey, RCT). (debette2021esoguidelinefor pages 2-4, filip2023cervicalarterydissections—a pages 1-2, ma2023imaginginvestigationof pages 1-2, guo2024applicationoftranscranial pages 1-2, engelter2021aspirinversusanticoagulation pages 7-11, lodato2025tenyearoutcomesof pages 5-9)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic framing)
CeAD occurs when a tear in the arterial wall or vasa vasorum results in an **intramural hematoma** and possibly a **false lumen**, which can cause luminal stenosis/occlusion and promote **local thrombus** and **artery-to-artery embolism**. (filip2023cervicalarterydissections—a pages 1-2, debette2021esoguidelinefor pages 1-2)

### 2.2 Risk factors

#### Mechanical / traumatic triggers
CeAD can be **spontaneous or traumatic**, and minor cervical strain/trauma (including whiplash-type mechanisms) is commonly reported as a trigger. (filip2023cervicalarterydissections—a pages 1-2)

#### Connective-tissue and arteriopathy associations
Predisposing conditions include **fibromuscular dysplasia** and **heritable connective tissue disorders** such as **Ehlers–Danlos syndrome** and **Marfan syndrome**. (filip2023cervicalarterydissections—a pages 1-2, blum2015cervicalarterydissection pages 1-3)

#### Vascular and neurologic comorbidities
Associated factors reported across clinical reviews and cohorts include **hypertension** and **migraine**. (filip2023cervicalarterydissections—a pages 1-2, blum2015cervicalarterydissection pages 1-3)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
The retrieved evidence supports a **multifactorial** model where an underlying predisposition affecting arterial wall integrity (genetic and/or connective tissue phenotype) may interact with mechanical stressors (minor trauma/exertion) to precipitate dissection, but formal GxE effect-size estimates were not available in the retrieved texts. (filip2023cervicalarterydissections—a pages 1-2, shlapakova2024peripheralbloodgene pages 1-2, nino2024thenaturalhistory pages 84-88)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with HPO suggestions)
CeAD commonly presents with **local symptoms** (pain, Horner syndrome, cranial nerve palsy) and/or **cerebral ischemia** (TIA/stroke). In ESO-cited series, ischemia complicates EAD in about **two thirds to three quarters** of patients. (debette2021esoguidelinefor pages 1-2)

**HPO suggestions (non-exhaustive):**
* Headache — **HP:0002315**  
* Neck pain — **HP:0000467**  
* Horner syndrome — **HP:0000005**  
* Transient ischemic attack — **HP:0002326** (approximate)  
* Ischemic stroke — **HP:0002140**  
* Cranial nerve palsy — **HP:0001290** (broad)  
* Vertigo (posterior circulation) — **HP:0002321**  
* Ataxia — **HP:0001251**

### 3.2 Phenotype characteristics (age, severity, progression)
* **Age of onset:** often young/middle-aged; ESO guideline reports mean age ~44 years for extracranial dissection. (debette2021esoguidelinefor pages 2-4)
* **Onset pattern:** typically acute/subacute neurological syndrome. (debette2021esoguidelinefor pages 1-2)
* **Progression:** ischemic events often occur early after diagnosis, supporting immediate antithrombotic initiation. (engelter2021cervicalandintracranial pages 1-2)

### 3.3 Frequency and statistics from cohorts
In a real-world cohort of 62 patients, **69%** presented with ischemic manifestations (16% TIA; 27% minor stroke; 25% major stroke). (lodato2025tenyearoutcomesof pages 5-9)

### 3.4 Quality-of-life impact
Direct QoL instrument data (e.g., EQ-5D, SF-36) were not captured in the retrieved evidence set; however, CeAD is highlighted as a leading cause of stroke in younger adults and thus a major potential driver of disability. (engelter2021cervicalandintracranial pages 1-2, debette2021esoguidelinefor pages 1-2)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes (monogenic contribution)
A minority of CeAD is attributable to monogenic heritable connective tissue disorders.

**Direct quote (proportion):** “**Monogenic heritable connective tissue diseases account for fewer than 5% of cases of CeAD**.” (Shlapakova et al., 2024) (shlapakova2024peripheralbloodgene pages 1-2)

Examples of single-gene disorders plausibly increasing risk include connective tissue disorder genes such as **FBN1** (Marfan) and **COL3A1** (vascular Ehlers–Danlos), as well as TGF-β pathway genes in Loeys–Dietz spectrum (e.g., **TGFBR1/2**, **SMAD2/3**, **TGFB2/3**). (maly2025carotidarterydissection pages 2-4, nino2024thenaturalhistory pages 84-88)

### 4.2 Susceptibility loci / GWAS-implicated genes
GWAS signals in CeAD often map to **non-coding variants** influencing transcription/RNA processing. Reported CeAD-associated genes/loci include **PHACTR1** and **LRP1**, among others (e.g., PLCE1, IRAG1). (shlapakova2024peripheralbloodgene pages 2-4)

### 4.3 Variant example with mechanistic follow-through
A mechanistic study of the pleiotropic vascular-risk locus **LRP1 rs11172113** supports an allele-specific regulatory mechanism in smooth muscle cells leading to extracellular matrix remodeling and altered signaling:

**Direct quote (key abstract statement):** “**Multitrait colocalization analyses pointed at rs11172113 as the most likely causal variant in LRP1 for fibromuscular dysplasia, migraine, pulse pressure, and spontaneous coronary artery dissection**.” (Liu et al., Circulation Research, 2024) (liu2024lrp1repressionby pages 1-2)

Mechanistically, the study shows LRP1 perturbation in iPSC-derived smooth muscle cells affects extracellular matrix composition and potentiates canonical **TGF-β/SMAD2/3** signaling. (liu2024lrp1repressionby pages 11-12, liu2024lrp1repressionby pages 1-2)

### 4.4 Transcriptomics and molecular profiling (2024)
Peripheral blood bulk RNA-seq (19 CeAD vs 18 controls) identified differential expression and pathway signals consistent with systemic stress and vascular biology.

**Direct quote (key molecular pathways):** “We found potential correlations between CeAD and the dysregulation of genes linked to **nucleolar stress, senescence-associated secretory phenotype, mitochondrial malfunction, and epithelial–mesenchymal plasticity**.” (Shlapakova et al., 2024) (shlapakova2024peripheralbloodgene pages 1-2)

### 4.5 Suggested ontology terms
**GO biological processes (examples):**
* extracellular matrix organization (GO:0030198) (supported conceptually by ECM remodeling evidence) (liu2024lrp1repressionby pages 11-12, liu2024lrp1repressionby pages 1-2)
* transforming growth factor beta receptor signaling pathway (GO:0007179) (liu2024lrp1repressionby pages 11-12, liu2024lrp1repressionby pages 1-2)
* smooth muscle cell proliferation/migration (GO:0048660/GO:0016477) (liu2024lrp1repressionby pages 1-2)

**Cell Ontology (CL) (examples):**
* vascular smooth muscle cell — CL:0000192 (liu2024lrp1repressionby pages 11-12, liu2024lrp1repressionby pages 1-2)
* endothelial cell — CL:0000115 (implicated in vascular integrity discussions; not directly profiled here)

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
The retrieved evidence emphasizes mechanical neck stress/trauma and vascular risk factors (e.g., hypertension) rather than specific toxins or occupational exposures. (filip2023cervicalarterydissections—a pages 1-2, blum2015cervicalarterydissection pages 1-3)

### 5.2 Infectious agents
Specific pathogens were not established as causal in the retrieved evidence. However, reviews note infection has been described as a risk factor in broader literature; the retrieved excerpted evidence did not provide quantitative estimates. (shlapakova2024peripheralbloodgene pages 2-4, nino2024thenaturalhistory pages 84-88)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (trigger → lesion → clinical event)
1. **Trigger/predisposition:** underlying arterial wall vulnerability (connective tissue phenotype; genetic susceptibility) ± mechanical stressor (minor trauma/strain). (filip2023cervicalarterydissections—a pages 1-2, shlapakova2024peripheralbloodgene pages 1-2, nino2024thenaturalhistory pages 84-88)
2. **Wall injury:** formation of **intramural hematoma** and potentially an **intimal flap/double lumen**, producing stenosis/occlusion or dissecting aneurysm. (debette2021esoguidelinefor pages 2-4, ma2023imaginginvestigationof pages 4-6)
3. **Stroke mechanism:** local thrombus formation and distal embolization are emphasized as key mechanisms. (guo2024applicationoftranscranial pages 1-2)
4. **Clinical manifestations:** local pain/Horner syndrome and/or TIA/stroke depending on embolic burden and hemodynamic compromise. (debette2021esoguidelinefor pages 1-2)

### 6.2 Upstream vs downstream mechanisms
* **Upstream:** genetic regulation of vascular smooth muscle/ECM integrity (e.g., LRP1 regulatory mechanisms; TGF-β pathway), connective tissue dysplasia. (shlapakova2024peripheralbloodgene pages 1-2, liu2024lrp1repressionby pages 11-12, liu2024lrp1repressionby pages 1-2)
* **Downstream:** intramural hematoma and luminal stenosis/occlusion; thromboembolism → ischemic lesions. (debette2021esoguidelinefor pages 2-4, guo2024applicationoftranscranial pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
* Primary: cervical segments of **internal carotid arteries** and **vertebral arteries** (cardiovascular system; cerebrovascular interface). (engelter2021cervicalandintracranial pages 1-2, debette2021esoguidelinefor pages 2-4)
* Secondary: brain ischemia (neurologic system) and rarely intracranial extension/SAH (more relevant to IAD). (debette2021esoguidelinefor pages 1-2)

**UBERON suggestions:**
* internal carotid artery — UBERON:0001645  
* vertebral artery — UBERON:0001646  
* cervical region vasculature — (composite; ontology-dependent)

### 7.2 Tissue/cell level
* arterial wall layers; vascular smooth muscle and extracellular matrix remodeling are implicated. (shlapakova2024peripheralbloodgene pages 1-2, liu2024lrp1repressionby pages 11-12)

### 7.3 Lateralization
Unilateral is common; bilateral and multi-vessel dissections occur (ESO: multiple cervical arteries involved in ~15–20% of EAD). (debette2021esoguidelinefor pages 2-4)

---

## 8. Temporal Development

### 8.1 Onset
Often acute/subacute; antithrombotic therapy is recommended to start immediately after diagnosis due to early stroke risk. (engelter2021cervicalandintracranial pages 1-2)

### 8.2 Progression / natural history
Recanalization is common: ESO guideline reports stenosis recanalization **33–90% within 6 months**; dissecting aneurysms resolve/decrease in **40–50%** (with dynamic evolution in CADISS follow-up). (debette2021esoguidelinefor pages 2-4)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
* Incidence estimate for extracranial artery dissection: **~2.6–3.0 per 100,000/year** (ESO guideline). (debette2021esoguidelinefor pages 2-4)
* Mean age reported for EAD: **~44 years**. (debette2021esoguidelinefor pages 2-4)

### 9.2 Inheritance
Most CeAD appears multifactorial/polygenic with rare monogenic CTD contribution (<5%). (shlapakova2024peripheralbloodgene pages 1-2, nino2024thenaturalhistory pages 84-88)

---

## 10. Diagnostics

### 10.1 Imaging-based diagnosis (core)
ESO diagnostic confirmation includes mural hematoma, dissecting aneurysm, long tapering stenosis, intimal flap, double lumen, or characteristic occlusion patterns. (debette2021esoguidelinefor pages 2-4)

### 10.2 Advanced imaging developments (2023–2024 prioritized)
**High-resolution MR vessel wall imaging (HRMR-VWI)** provides improved detection of direct wall signs (intimal flap/double lumen/intramural hematoma) and enables staging and quantitative vessel-wall metrics.

In a 2023 BMC Medical Imaging study (34 patients; 38 vessels), **intimal flap/double-lumen detection** was more common on HRMR-VWI than MRA (**P = 0.012**), and intramural hematoma and grade II enhancement were more often detected in acute/subacute vs chronic stages. (ma2023imaginginvestigationof pages 1-2, ma2023imaginginvestigationof pages 6-9)

**Direct quote:** HRMR-VWI “**visualizes vessel walls, thereby effectively characterizing the direct signs, such as intimal flap, double lumen, and intramural hematoma (IMH)**.” (ma2023imaginginvestigationof pages 2-4)

### 10.3 TCD as an implementation/monitoring tool (STOP-CAD survey, 2024)
A multicenter STOP-CAD survey shows TCD adoption is variable but common.

**Direct quotes:**
* “**Half (29 out of 58) of the sites routinely perform TCD** on CAD patients…” (guo2024applicationoftranscranial pages 1-2)
* “European institutions show a notably higher rate of TCD application… **76.4%** compared to… North America… **34.3%** (p = 0.007)” (guo2024applicationoftranscranial pages 3-3)

HITS detection often prompts escalation from antiplatelet to anticoagulation in practice. (guo2024applicationoftranscranial pages 4-4, guo2024applicationoftranscranial pages 5-5)

### 10.4 Differential diagnosis
Not comprehensively addressed in retrieved sources; typical differential in practice includes atherosclerotic stenosis, vasculitis, fibromuscular dysplasia without dissection, and thromboembolic disease without wall hematoma.

---

## 11. Outcome/Prognosis

### 11.1 Short-term outcomes
A review of emergency medicine literature notes generally favorable outcomes with high proportions achieving functional independence (mRS 0–2) at 3–6 months in historical cohorts, and low mortality (reported ~1.9–5%). (robertson2016cervicalarterydissections pages 6-7)

### 11.2 Long-term outcomes (real-world cohort)
In a 10-year retrospective cohort (n=62), recurrent ischemic stroke was **4%** (2 patients), both within the first 12 months, and estimated **10-year overall survival 71%** with **10-year stroke/death-free survival 70%**. (lodato2025tenyearoutcomesof pages 5-9)

---

## 12. Treatment

### 12.1 Acute reperfusion treatments (guideline + evidence)
ESO guideline suggests:
* IV alteplase within 4.5 hours for eligible acute ischemic stroke with EAD (weak recommendation, low-quality evidence). (debette2021esoguidelinefor pages 42-43)
* Mechanical thrombectomy for anterior-circulation large-vessel occlusion associated with EAD (weak recommendation, very low-quality evidence). (debette2021esoguidelinefor pages 42-43)

These recommendations are summarized in ESO tables (debette2021esoguidelinefor media df12240a, debette2021esoguidelinefor media 106e3d8a).

### 12.2 Antithrombotic secondary prevention
ESO guideline: in acute symptomatic EAD, clinicians may prescribe **either anticoagulants or antiplatelet therapy** (strong recommendation; moderate quality). (debette2021esoguidelinefor pages 42-43, debette2021esoguidelinefor pages 37-41)

#### RCT evidence (TREAT-CAD)
TREAT-CAD randomized 194 patients to aspirin vs VKA; **non-inferiority of aspirin was not demonstrated**.

Key outcomes at 3 months (per protocol): primary endpoint **23.1%** aspirin vs **14.6%** VKA; ischemic stroke **7.7%** aspirin vs **0%** VKA; major extracranial hemorrhage **0%** vs **1.2%**; no deaths. (engelter2021aspirinversusanticoagulation pages 7-11)

**Direct quote:** “**non-inferiority of aspirin was not demonstrated**.” (engelter2021aspirinversusanticoagulation pages 7-11)

### 12.3 Expert consensus (ESO) on special situations
ESO expert consensus (when evidence is low) supports:
* DOACs as potential substitutes for VKA in symptomatic EAD patients treated with anticoagulation. (debette2021esoguidelinefor pages 37-41)
* Short-term dual antiplatelet therapy (aspirin + clopidogrel) for a few weeks in EAD-related TIA/minor stroke. (debette2021esoguidelinefor pages 37-41)

### 12.4 Real-world practice (TCD-guided escalation)
In the STOP-CAD TCD survey, after HITS detection, some centers switch from SAPT/DAPT to anticoagulation (e.g., 20.7% DAPT→AC; 12.1% SAPT→AC). (guo2024applicationoftranscranial pages 4-4)

### 12.5 MAXO (Medical Action Ontology) suggestions
* Antithrombotic therapy — MAXO:0000508 (approximate)  
* Antiplatelet therapy — MAXO:0000515 (approximate)  
* Anticoagulant therapy — MAXO:0000516 (approximate)  
* Intravenous thrombolysis — MAXO:0001025 (approximate)  
* Mechanical thrombectomy — MAXO:0001206 (approximate)  
* Endovascular stenting — MAXO:0001097 (approximate)

(Exact MAXO IDs should be verified against MAXO; provided as best-effort suggestions.)

---

## 13. Prevention

### 13.1 Primary prevention
No evidence-based primary prevention strategy specific to CeAD was captured in the retrieved texts beyond general avoidance of neck trauma in high-risk individuals and control of vascular risk factors.

### 13.2 Secondary/tertiary prevention
Immediate initiation of antithrombotic therapy after diagnosis is supported by the observation that ischemic events occur early after CeAD diagnosis. (engelter2021cervicalandintracranial pages 1-2)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human species evidence was identified in the retrieved texts.

---

## 15. Model Organisms
The retrieved evidence includes iPSC-derived human smooth muscle cell models used to test vascular-risk loci mechanisms (LRP1 enhancer/KO) rather than animal models.

**Model type:** in vitro human iPSC-derived smooth muscle cells + CRISPR editing. (liu2024lrp1repressionby pages 1-2)

---

## Current applications and real-world implementation highlights

1. **Guideline-concordant acute stroke care** (IV alteplase, thrombectomy) is recommended for eligible CeAD-related strokes similarly to other causes, with evidence-quality caveats in guidelines. (debette2021esoguidelinefor pages 42-43, engelter2021cervicalandintracranial pages 3-5)
2. **Advanced imaging (HRMR-VWI)** is increasingly used to improve early diagnosis and staging, particularly for intramural hematoma and direct dissection signs not reliably seen on lumenography alone. (ma2023imaginginvestigationof pages 1-2, ma2023imaginginvestigationof pages 2-4)
3. **TCD monitoring** is used by about half of advanced stroke centers and can change antithrombotic decisions when HITS are detected, although standardized protocols are lacking. (guo2024applicationoftranscranial pages 1-2, guo2024applicationoftranscranial pages 4-4)

---

## Expert opinion & analysis (authoritative sources)

* ESO guideline authors conclude that, based on two phase-2 RCTs, there is no clear net benefit difference between anticoagulants vs antiplatelets for acute symptomatic EAD; hence either is acceptable, with additional expert consensus for DOACs and short DAPT in selected scenarios. (debette2021esoguidelinefor pages 42-43, debette2021esoguidelinefor pages 37-41)
* Engelter et al. emphasize that with CADISS and TREAT-CAD, “the evidence to consider aspirin as the standard therapy of CeAD is weak” and advocate immediate antithrombotic initiation. (engelter2021cervicalandintracranial pages 1-2)

---

## Limitations of this report (evidence availability)

* **AHA 2024 scientific statement** (“Treatment and outcomes of cervical artery dissection in adults”) was detected in search results but was unobtainable in this run; therefore, its content is not quoted here.  
* **PMIDs** were not embedded in most retrieved text chunks; thus, PMID-preferred citations could not be consistently provided.
* **Ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM)** were not available in the retrieved documents and should be filled via dedicated ontology lookups.

---

## References (key retrieved sources with dates/URLs)

* Debette S, et al. **ESO guideline for the management of extracranial and intracranial artery dissection**. *European Stroke Journal*. Sep 2021. https://doi.org/10.1177/23969873211046475 (debette2021esoguidelinefor pages 2-4, debette2021esoguidelinefor pages 42-43, debette2021esoguidelinefor pages 37-41, debette2021esoguidelinefor media df12240a, debette2021esoguidelinefor media 106e3d8a)
* Ma W, et al. **Imaging investigation… using high resolution magnetic resonance VWI and MRA**. *BMC Medical Imaging*. Nov 2023. https://doi.org/10.1186/s12880-023-01133-z (ma2023imaginginvestigationof pages 1-2, ma2023imaginginvestigationof pages 2-4)
* Guo X, et al. **Application of transcranial Doppler… STOP-CAD survey**. *Clinical Neuroimaging*. Mar 2024. https://doi.org/10.1002/neo2.70004 (guo2024applicationoftranscranial pages 1-2, guo2024applicationoftranscranial pages 4-4)
* Shlapakova PS, et al. **Peripheral Blood Gene Expression Profiling… CeAD**. *Int J Mol Sci*. May 2024. https://doi.org/10.3390/ijms25105205 (shlapakova2024peripheralbloodgene pages 1-2, shlapakova2024peripheralbloodgene pages 2-4)
* Liu L, et al. **LRP1 repression by SNAIL results in ECM remodeling…** *Circulation Research*. Nov 2024. https://doi.org/10.1161/CIRCRESAHA.124.325269 (liu2024lrp1repressionby pages 1-2)
* Engelter ST, et al. **Aspirin versus anticoagulation in cervical artery dissection (TREAT-CAD)**. *Lancet Neurology*. May 2021. https://doi.org/10.1016/S1474-4422(21)00044-2 (engelter2021aspirinversusanticoagulation pages 7-11)
* Lodato M, et al. **Ten-Year Outcomes of Cervical Artery Dissection**. *J Clin Med*. Sep 2025. https://doi.org/10.3390/jcm14196836 (lodato2025tenyearoutcomesof pages 5-9)



References

1. (debette2021esoguidelinefor pages 2-4): Stephanie Debette, Mikael Mazighi, Philippe Bijlenga, Alessandro Pezzini, Masatoshi Koga, Anna Bersano, Janika Kõrv, Julien Haemmerli, Isabella Canavero, Piotr Tekiela, Kaori Miwa, David J Seiffge, Sabrina Schilling, Avtar Lal, Marcel Arnold, Hugh S Markus, Stefan T Engelter, and Jennifer J Majersik. Eso guideline for the management of extracranial and intracranial artery dissection. European Stroke Journal, 6:XXXIX-LXXXVIII, Sep 2021. URL: https://doi.org/10.1177/23969873211046475, doi:10.1177/23969873211046475. This article has 174 citations and is from a peer-reviewed journal.

2. (debette2021esoguidelinefor pages 1-2): Stephanie Debette, Mikael Mazighi, Philippe Bijlenga, Alessandro Pezzini, Masatoshi Koga, Anna Bersano, Janika Kõrv, Julien Haemmerli, Isabella Canavero, Piotr Tekiela, Kaori Miwa, David J Seiffge, Sabrina Schilling, Avtar Lal, Marcel Arnold, Hugh S Markus, Stefan T Engelter, and Jennifer J Majersik. Eso guideline for the management of extracranial and intracranial artery dissection. European Stroke Journal, 6:XXXIX-LXXXVIII, Sep 2021. URL: https://doi.org/10.1177/23969873211046475, doi:10.1177/23969873211046475. This article has 174 citations and is from a peer-reviewed journal.

3. (lodato2025tenyearoutcomesof pages 5-9): Marcello Lodato, Rodolfo Pini, Alessandra Porcelli, Enrico Gallitto, Andrea Vacirca, Mauro Gargiulo, and Gianluca Faggioli. Ten-year outcomes of cervical artery dissection: a retrospective study in a real-world cohort. Journal of Clinical Medicine, 14:6836, Sep 2025. URL: https://doi.org/10.3390/jcm14196836, doi:10.3390/jcm14196836. This article has 1 citations.

4. (engelter2021aspirinversusanticoagulation pages 7-11): Stefan T Engelter, Christopher Traenka, Henrik Gensicke, Sabine A Schaedelin, Andreas R Luft, Barbara Goeggel Simonetti, Urs Fischer, Patrik Michel, Gaia Sirimarco, Georg Kägi, Jochen Vehoff, Krassen Nedeltchev, Timo Kahles, Lars Kellert, Sverre Rosenbaum, Regina von Rennenberg, Roman Sztajzel, Stephen L Leib, Simon Jung, Jan Gralla, Nicole Bruni, David Seiffge, Katharina Feil, Alexandros A Polymeris, Levke Steiner, Janne Hamann, Leo H Bonati, Alex Brehm, Gian Marco De Marchis, Nils Peters, Christoph Stippich, Christian H Nolte, Hanne Christensen, Susanne Wegener, Marios-Nikos Psychogios, Marcel Arnold, Philippe Lyrer, Timo Kahles, Krassen Nedeltchev, Valerian Altersberger, Leo H Bonati, Alex Brehm, Nicole Bruni, Gian Marco De Marchis, Stefan T Engelter, Thomas Fabbro, Urs Fisch, Joachim Fladt, Henrik Gensicke, Lisa Hert, Philippe A Lyrer, Marina Maurer, Nils Peters, Alexandros Polymeris, Marios-Nikos Psychogios, Sabine Schaedelin, Christoph Stippich, Sebastian Thilemann, Christopher Traenka, Benjamin Wagner, Marcel Arnold, Urs Fischer, Barbara Goeggel Simonetti, Jan Gralla, Mirjam Heldner, Simon Jung, Stephen L Leib, David J Seiffge, Hubertus Mueller, Lukas Sveikata, Roman Sztajzel, Hubertus Mueller, Pamela Correia, Ashraf Eskandari, Ivo Meyer, Patrik Michel, Stefania Nannoni, Suzette Remillard, Gaia Sirimarco, Alexandros Zachariadis, Georg Kaegi, Anna Mueller, Jochen Vehoff, Janne Hamann, Andreas R Luft, Levke Steiner, Susanne Wegener, Hebun J Erdur, Christian H Nolte, Regina von Rennenberg, Jan F Scheitz, Katharina Feil, Lars Kellert, Hanne Christensen, and Sverre Rosenbaum. Aspirin versus anticoagulation in cervical artery dissection (treat-cad): an open-label, randomised, non-inferiority trial. The Lancet Neurology, 20:341-350, May 2021. URL: https://doi.org/10.1016/s1474-4422(21)00044-2, doi:10.1016/s1474-4422(21)00044-2. This article has 161 citations and is from a highest quality peer-reviewed journal.

5. (debette2021esoguidelinefor pages 42-43): Stephanie Debette, Mikael Mazighi, Philippe Bijlenga, Alessandro Pezzini, Masatoshi Koga, Anna Bersano, Janika Kõrv, Julien Haemmerli, Isabella Canavero, Piotr Tekiela, Kaori Miwa, David J Seiffge, Sabrina Schilling, Avtar Lal, Marcel Arnold, Hugh S Markus, Stefan T Engelter, and Jennifer J Majersik. Eso guideline for the management of extracranial and intracranial artery dissection. European Stroke Journal, 6:XXXIX-LXXXVIII, Sep 2021. URL: https://doi.org/10.1177/23969873211046475, doi:10.1177/23969873211046475. This article has 174 citations and is from a peer-reviewed journal.

6. (debette2021esoguidelinefor pages 37-41): Stephanie Debette, Mikael Mazighi, Philippe Bijlenga, Alessandro Pezzini, Masatoshi Koga, Anna Bersano, Janika Kõrv, Julien Haemmerli, Isabella Canavero, Piotr Tekiela, Kaori Miwa, David J Seiffge, Sabrina Schilling, Avtar Lal, Marcel Arnold, Hugh S Markus, Stefan T Engelter, and Jennifer J Majersik. Eso guideline for the management of extracranial and intracranial artery dissection. European Stroke Journal, 6:XXXIX-LXXXVIII, Sep 2021. URL: https://doi.org/10.1177/23969873211046475, doi:10.1177/23969873211046475. This article has 174 citations and is from a peer-reviewed journal.

7. (ma2023imaginginvestigationof pages 1-2): Weiqiong Ma, Kexin Zhou, Bowen Lan, Kangyin Chen, Wu-ming Li, and Guihua Jiang. Imaging investigation of cervicocranial artery dissection by using high resolution magnetic resonance vwi and mra: qualitative and quantitative analysis at different stages. BMC Medical Imaging, Nov 2023. URL: https://doi.org/10.1186/s12880-023-01133-z, doi:10.1186/s12880-023-01133-z. This article has 5 citations and is from a peer-reviewed journal.

8. (ma2023imaginginvestigationof pages 6-9): Weiqiong Ma, Kexin Zhou, Bowen Lan, Kangyin Chen, Wu-ming Li, and Guihua Jiang. Imaging investigation of cervicocranial artery dissection by using high resolution magnetic resonance vwi and mra: qualitative and quantitative analysis at different stages. BMC Medical Imaging, Nov 2023. URL: https://doi.org/10.1186/s12880-023-01133-z, doi:10.1186/s12880-023-01133-z. This article has 5 citations and is from a peer-reviewed journal.

9. (guo2024applicationoftranscranial pages 1-2): Xiaofan Guo, Behnam Sabayan, Benjamin Shifflett, Muhib Khan, Kateryna Antonenko, Mirjam R. Heldner, Michele Romoli, João Pedro Marto, Zafer Keser, Aaron Rothstein, Ossama Khazaal, Marwa Elnazeir, Harjot Hansra, Brett C. Meyer, Dawn M. Meyer, and Reza Bavarsad Shahripour. Application of transcranial doppler in the diagnosis and management of cervical artery dissection: insights from a multicenter survey within the stop‐cad study. Clinical Neuroimaging, Mar 2024. URL: https://doi.org/10.1002/neo2.70004, doi:10.1002/neo2.70004. This article has 1 citations.

10. (guo2024applicationoftranscranial pages 4-4): Xiaofan Guo, Behnam Sabayan, Benjamin Shifflett, Muhib Khan, Kateryna Antonenko, Mirjam R. Heldner, Michele Romoli, João Pedro Marto, Zafer Keser, Aaron Rothstein, Ossama Khazaal, Marwa Elnazeir, Harjot Hansra, Brett C. Meyer, Dawn M. Meyer, and Reza Bavarsad Shahripour. Application of transcranial doppler in the diagnosis and management of cervical artery dissection: insights from a multicenter survey within the stop‐cad study. Clinical Neuroimaging, Mar 2024. URL: https://doi.org/10.1002/neo2.70004, doi:10.1002/neo2.70004. This article has 1 citations.

11. (guo2024applicationoftranscranial pages 3-3): Xiaofan Guo, Behnam Sabayan, Benjamin Shifflett, Muhib Khan, Kateryna Antonenko, Mirjam R. Heldner, Michele Romoli, João Pedro Marto, Zafer Keser, Aaron Rothstein, Ossama Khazaal, Marwa Elnazeir, Harjot Hansra, Brett C. Meyer, Dawn M. Meyer, and Reza Bavarsad Shahripour. Application of transcranial doppler in the diagnosis and management of cervical artery dissection: insights from a multicenter survey within the stop‐cad study. Clinical Neuroimaging, Mar 2024. URL: https://doi.org/10.1002/neo2.70004, doi:10.1002/neo2.70004. This article has 1 citations.

12. (debette2021esoguidelinefor media df12240a): Stephanie Debette, Mikael Mazighi, Philippe Bijlenga, Alessandro Pezzini, Masatoshi Koga, Anna Bersano, Janika Kõrv, Julien Haemmerli, Isabella Canavero, Piotr Tekiela, Kaori Miwa, David J Seiffge, Sabrina Schilling, Avtar Lal, Marcel Arnold, Hugh S Markus, Stefan T Engelter, and Jennifer J Majersik. Eso guideline for the management of extracranial and intracranial artery dissection. European Stroke Journal, 6:XXXIX-LXXXVIII, Sep 2021. URL: https://doi.org/10.1177/23969873211046475, doi:10.1177/23969873211046475. This article has 174 citations and is from a peer-reviewed journal.

13. (debette2021esoguidelinefor media 106e3d8a): Stephanie Debette, Mikael Mazighi, Philippe Bijlenga, Alessandro Pezzini, Masatoshi Koga, Anna Bersano, Janika Kõrv, Julien Haemmerli, Isabella Canavero, Piotr Tekiela, Kaori Miwa, David J Seiffge, Sabrina Schilling, Avtar Lal, Marcel Arnold, Hugh S Markus, Stefan T Engelter, and Jennifer J Majersik. Eso guideline for the management of extracranial and intracranial artery dissection. European Stroke Journal, 6:XXXIX-LXXXVIII, Sep 2021. URL: https://doi.org/10.1177/23969873211046475, doi:10.1177/23969873211046475. This article has 174 citations and is from a peer-reviewed journal.

14. (engelter2021cervicalandintracranial pages 1-2): Stefan T. Engelter, Philippe Lyrer, and Christopher Traenka. Cervical and intracranial artery dissections. Therapeutic Advances in Neurological Disorders, Jan 2021. URL: https://doi.org/10.1177/17562864211037238, doi:10.1177/17562864211037238. This article has 25 citations and is from a peer-reviewed journal.

15. (filip2023cervicalarterydissections—a pages 1-2): Iulian Roman Filip, Valentin Morosanu, Doina Spinu, Claudiu Motoc, Zoltan Bajko, Emanuela Sarmasan, Corina Roman, and Rodica Balasa. Cervical artery dissections—a demographical analysis of risk factors, clinical characteristics treatment procedures, and outcomes—a single centre study of 54 consecutive cases. Journal of Personalized Medicine, 14:48, Dec 2023. URL: https://doi.org/10.3390/jpm14010048, doi:10.3390/jpm14010048. This article has 5 citations.

16. (blum2015cervicalarterydissection pages 1-3): Christina A. Blum and Shadi Yaghi. Cervical artery dissection: a review of the epidemiology, pathophysiology, treatment, and outcome. Archives of neuroscience, Oct 2015. URL: https://doi.org/10.5812/archneurosci.26670, doi:10.5812/archneurosci.26670. This article has 214 citations.

17. (shlapakova2024peripheralbloodgene pages 1-2): Polina S. Shlapakova, Larisa A. Dobrynina, Ludmila A. Kalashnikova, Mariia V. Gubanova, Maria S. Danilova, Elena V. Gnedovskaya, Anastasia P. Grigorenko, Fedor E. Gusev, Andrey D. Manakhov, and Evgeny I. Rogaev. Peripheral blood gene expression profiling reveals molecular pathways associated with cervical artery dissection. International Journal of Molecular Sciences, 25:5205, May 2024. URL: https://doi.org/10.3390/ijms25105205, doi:10.3390/ijms25105205. This article has 4 citations.

18. (nino2024thenaturalhistory pages 84-88): AC Vargas Nino. The natural history and genetics of cranio-cervical arterial dissections in childhood. Unknown journal, 2024.

19. (maly2025carotidarterydissection pages 2-4): Petr Malý, Leona Chrastinová, Martin Malý, and Jan M. Horáček. Carotid artery dissection and connective tissue disorders: a review of known gene/protein mutation findings. Military Medical Science Letters, Oct 2025. URL: https://doi.org/10.31482/mmsl.2024.016, doi:10.31482/mmsl.2024.016. This article has 0 citations.

20. (shlapakova2024peripheralbloodgene pages 2-4): Polina S. Shlapakova, Larisa A. Dobrynina, Ludmila A. Kalashnikova, Mariia V. Gubanova, Maria S. Danilova, Elena V. Gnedovskaya, Anastasia P. Grigorenko, Fedor E. Gusev, Andrey D. Manakhov, and Evgeny I. Rogaev. Peripheral blood gene expression profiling reveals molecular pathways associated with cervical artery dissection. International Journal of Molecular Sciences, 25:5205, May 2024. URL: https://doi.org/10.3390/ijms25105205, doi:10.3390/ijms25105205. This article has 4 citations.

21. (liu2024lrp1repressionby pages 1-2): Lu Liu, Joséphine Henry, Yingwei Liu, Charlène Jouve, Jean-Sébastien Hulot, Adrien Georges, and Nabila Bouatia-Naji. <i>lrp1</i> repression by snail results in ecm remodeling in genetic risk for vascular diseases. Circulation Research, 135:1084-1097, Nov 2024. URL: https://doi.org/10.1161/circresaha.124.325269, doi:10.1161/circresaha.124.325269. This article has 13 citations and is from a highest quality peer-reviewed journal.

22. (liu2024lrp1repressionby pages 11-12): Lu Liu, Joséphine Henry, Yingwei Liu, Charlène Jouve, Jean-Sébastien Hulot, Adrien Georges, and Nabila Bouatia-Naji. <i>lrp1</i> repression by snail results in ecm remodeling in genetic risk for vascular diseases. Circulation Research, 135:1084-1097, Nov 2024. URL: https://doi.org/10.1161/circresaha.124.325269, doi:10.1161/circresaha.124.325269. This article has 13 citations and is from a highest quality peer-reviewed journal.

23. (ma2023imaginginvestigationof pages 4-6): Weiqiong Ma, Kexin Zhou, Bowen Lan, Kangyin Chen, Wu-ming Li, and Guihua Jiang. Imaging investigation of cervicocranial artery dissection by using high resolution magnetic resonance vwi and mra: qualitative and quantitative analysis at different stages. BMC Medical Imaging, Nov 2023. URL: https://doi.org/10.1186/s12880-023-01133-z, doi:10.1186/s12880-023-01133-z. This article has 5 citations and is from a peer-reviewed journal.

24. (ma2023imaginginvestigationof pages 2-4): Weiqiong Ma, Kexin Zhou, Bowen Lan, Kangyin Chen, Wu-ming Li, and Guihua Jiang. Imaging investigation of cervicocranial artery dissection by using high resolution magnetic resonance vwi and mra: qualitative and quantitative analysis at different stages. BMC Medical Imaging, Nov 2023. URL: https://doi.org/10.1186/s12880-023-01133-z, doi:10.1186/s12880-023-01133-z. This article has 5 citations and is from a peer-reviewed journal.

25. (guo2024applicationoftranscranial pages 5-5): Xiaofan Guo, Behnam Sabayan, Benjamin Shifflett, Muhib Khan, Kateryna Antonenko, Mirjam R. Heldner, Michele Romoli, João Pedro Marto, Zafer Keser, Aaron Rothstein, Ossama Khazaal, Marwa Elnazeir, Harjot Hansra, Brett C. Meyer, Dawn M. Meyer, and Reza Bavarsad Shahripour. Application of transcranial doppler in the diagnosis and management of cervical artery dissection: insights from a multicenter survey within the stop‐cad study. Clinical Neuroimaging, Mar 2024. URL: https://doi.org/10.1002/neo2.70004, doi:10.1002/neo2.70004. This article has 1 citations.

26. (robertson2016cervicalarterydissections pages 6-7): Jennifer J. Robertson and Alex Koyfman. Cervical artery dissections: a review. The Journal of emergency medicine, 51 5:508-518, Nov 2016. URL: https://doi.org/10.1016/j.jemermed.2015.10.044, doi:10.1016/j.jemermed.2015.10.044. This article has 129 citations.

27. (engelter2021cervicalandintracranial pages 3-5): Stefan T. Engelter, Philippe Lyrer, and Christopher Traenka. Cervical and intracranial artery dissections. Therapeutic Advances in Neurological Disorders, Jan 2021. URL: https://doi.org/10.1177/17562864211037238, doi:10.1177/17562864211037238. This article has 25 citations and is from a peer-reviewed journal.