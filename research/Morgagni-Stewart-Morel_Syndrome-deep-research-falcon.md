---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T05:16:27.424955'
end_time: '2026-05-10T05:24:11.849232'
duration_seconds: 464.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Morgagni-Stewart-Morel Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Morgagni-Stewart-Morel Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Morgagni-Stewart-Morel Syndrome** covering all of the
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
- **Disease Name:** Morgagni-Stewart-Morel Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Morgagni-Stewart-Morel Syndrome** covering all of the
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


## Comprehensive Research Report: Morgagni–Stewart–Morel Syndrome (MSMS)

### Executive summary (current understanding)
Morgagni–Stewart–Morel syndrome (MSMS; also “Morgagni syndrome” / “Stewart–Morel syndrome”) is typically used to describe the syndromic co-occurrence of **hyperostosis frontalis interna (HFI)** (benign thickening/proliferation of the inner table of the frontal bone) with **metabolic/endocrine abnormalities** (commonly obesity and diabetes; sometimes thyroid/parathyroid abnormalities) and **neuropsychiatric/neurologic manifestations** (headache, mood/cognitive/behavioral symptoms, seizures). The literature base remains dominated by case reports and small series, with uncertain causality between bone overgrowth and symptoms. (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, inal2024themultidetectorct pages 7-8, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)

| Item | Details | Evidence (context id) | Publication (year, journal) | URL |
|---|---|---|---|---|
| Disease concept | Morgagni–Stewart–Morel syndrome (MSMS/MSM) is a rare syndrome in which hyperostosis frontalis interna (HFI) co-occurs with metabolic, endocrine, and neuropsychiatric abnormalities; commonly described with obesity, virilization/hirsutism, headache, seizures, mood/cognitive symptoms, and endocrine dysfunction. | (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, dogan2019morgagnisteawartmorelsendromuolgu pages 1-3, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3) | 2025, Acta Medica Nicomedia; 2025, European Journal of Case Reports in Internal Medicine; 2019, Turkish Journal of Clinics and Laboratory | https://doi.org/10.53446/actamednicomedia.1644183 ; https://doi.org/10.12890/2025_005836 ; https://doi.org/10.18663/tjcl.453912 |
| Core skeletal lesion | HFI is benign thickening/proliferation of the inner table of the frontal bone and is the principal radiologic feature of MSMS. | (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, dogan2019morgagnisteawartmorelsendromuolgu pages 1-3, inal2024themultidetectorct pages 7-8) | 2025, European Journal of Case Reports in Internal Medicine; 2019, Turkish Journal of Clinics and Laboratory; 2024, Romanian Journal of Rhinology | https://doi.org/10.12890/2025_005836 ; https://doi.org/10.18663/tjcl.453912 ; https://doi.org/10.2478/rjr-2024-0018 |
| Common synonyms/alternate names | Morgagni syndrome; Stewart–Morel syndrome; Morgagni–Stewart–Morel syndrome; metabolic craniopathy; hyperostosis frontalis interna with obesity/virilization/neuropsychiatric symptoms. Some sources loosely use HFI itself as synonymous, but retrieved evidence supports HFI as the imaging lesion and MSMS as the syndromic form. | (dogan2019morgagnisteawartmorelsendromuolgu pages 1-3, inal2024themultidetectorct pages 7-8, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3) | 2019, Turkish Journal of Clinics and Laboratory; 2024, Romanian Journal of Rhinology | https://doi.org/10.18663/tjcl.453912 ; https://doi.org/10.2478/rjr-2024-0018 |
| Identifier: MONDO | Not found in retrieved sources. | (cetinok2025hyperostosisfrontalisinterna pages 5-6) | 2025, Acta Medica Nicomedia | https://doi.org/10.53446/actamednicomedia.1644183 |
| Identifier: OMIM | Not found in retrieved sources. | (cetinok2025hyperostosisfrontalisinterna pages 5-6) | 2025, Acta Medica Nicomedia | https://doi.org/10.53446/actamednicomedia.1644183 |
| Identifier: Orphanet | Not found in retrieved sources. | (cetinok2025hyperostosisfrontalisinterna pages 5-6) | 2025, Acta Medica Nicomedia | https://doi.org/10.53446/actamednicomedia.1644183 |
| Identifier: MeSH | Not found in retrieved sources. | (cetinok2025hyperostosisfrontalisinterna pages 5-6) | 2025, Acta Medica Nicomedia | https://doi.org/10.53446/actamednicomedia.1644183 |
| Identifier: ICD-10 / ICD-11 | Not found in retrieved sources. | (cetinok2025hyperostosisfrontalisinterna pages 5-6) | 2025, Acta Medica Nicomedia | https://doi.org/10.53446/actamednicomedia.1644183 |
| Typical demographics | Strong female predominance, especially postmenopausal and older women. In one CT series of diffuse HFI, 148/154 (96.1%) cases were female; a cadaveric study found HFI in 31/74 donors, with 77.42% of HFI cases in women. | (inal2024themultidetectorct pages 3-4, inal2024themultidetectorct pages 1-3, cetinok2025hyperostosisfrontalisinterna pages 2-3) | 2024, Romanian Journal of Rhinology; 2025, Acta Medica Nicomedia | https://doi.org/10.2478/rjr-2024-0018 ; https://doi.org/10.53446/actamednicomedia.1644183 |
| Endocrine/metabolic associations | Reported associations include obesity, diabetes mellitus, hypothyroidism, hyperparathyroidism, menstrual disturbances, galactorrhea, and hirsutism/virilization. Etiology remains uncertain but hormonal/metabolic factors are repeatedly emphasized. | (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, inal2024themultidetectorct pages 7-8, otken2023hyperostosisfrontoparietooccipitalisa pages 4-5, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3) | 2025, European Journal of Case Reports in Internal Medicine; 2024, Romanian Journal of Rhinology; 2023, Cureus; 2019, Turkish Journal of Clinics and Laboratory | https://doi.org/10.12890/2025_005836 ; https://doi.org/10.2478/rjr-2024-0018 ; https://doi.org/10.7759/cureus.41445 ; https://doi.org/10.18663/tjcl.453912 |
| Neuropsychiatric/neurologic features | Headache, depression, cognitive/behavioral change, psychosis, seizures, dizziness, and executive dysfunction have been reported; presentations range from incidental imaging findings to acute neurologic/respiratory decompensation. | (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, otken2023hyperostosisfrontoparietooccipitalisa pages 4-5, abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3) | 2025, Acta Medica Nicomedia; 2025, European Journal of Case Reports in Internal Medicine; 2023, Cureus; 2019, Turkish Journal of Clinics and Laboratory | https://doi.org/10.53446/actamednicomedia.1644183 ; https://doi.org/10.12890/2025_005836 ; https://doi.org/10.7759/cureus.41445 ; https://doi.org/10.18663/tjcl.453912 |
| Core diagnostic element: imaging | Diagnosis depends on radiographic confirmation of frontal inner-table thickening. CT is emphasized as confirmatory; MRI may show internal frontal hyperostosis and associated cortico-subcortical atrophy. | (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, inal2024themultidetectorct pages 7-8) | 2025, European Journal of Case Reports in Internal Medicine; 2024, Romanian Journal of Rhinology | https://doi.org/10.12890/2025_005836 ; https://doi.org/10.2478/rjr-2024-0018 |
| Core diagnostic element: CT morphometry | In diffuse HFI, CT shows increased frontal/calvarial thickness at the vertex, frontal tuberosity, and frontal sinus levels. Example vertex thicknesses in HFI vs controls: midline 12.88±3.43 mm vs 8.01±2.04 mm; right lateral 15.94±4.75 mm vs 8.69±1.96 mm; left lateral 15.48±4.66 mm vs 8.64±1.97 mm. | (inal2024themultidetectorct pages 3-4, inal2024themultidetectorct pages 1-3) | 2024, Romanian Journal of Rhinology | https://doi.org/10.2478/rjr-2024-0018 |
| Core diagnostic element: density findings | CT density in HFI regions is increased at least at the vertex and frontal tuberosity. Example: vertex HFI region 1064.56±244.33 HU vs control 837.06±214.25 HU. | (inal2024themultidetectorct pages 3-4, inal2024themultidetectorct pages 5-7, inal2024themultidetectorct pages 4-5) | 2024, Romanian Journal of Rhinology | https://doi.org/10.2478/rjr-2024-0018 |
| Radiologic classification | Retrieved sources reference Hershkovitz radiologic classification for HFI and describe Type A (<25% frontal endocranial surface, isolated thickness <1 cm) and Types B–D with increasing extent/nodularity; radiology reports should specify presence and degree. | (dogan2019morgagnisteawartmorelsendromuolgu pages 1-3, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3, inal2024themultidetectorct media cb19ca47) | 2019, Turkish Journal of Clinics and Laboratory; 2024, Romanian Journal of Rhinology | https://doi.org/10.18663/tjcl.453912 ; https://doi.org/10.2478/rjr-2024-0018 |
| Suggested diagnostic workflow | Combine characteristic imaging (HFI) with syndromic features and assess endocrine/metabolic comorbidities. Retrieved studies recommend radiology consultation and endocrinologic assessment when HFI is detected. | (inal2024themultidetectorct pages 7-8, inal2024themultidetectorct pages 1-3) | 2024, Romanian Journal of Rhinology | https://doi.org/10.2478/rjr-2024-0018 |
| Differential diagnosis clues | Retrieved reports note need to distinguish HFI/MSMS from Paget disease, fibrous dysplasia, acromegaly, hyperostosis cranialis interna, and osseous metastasis mimics on imaging. | (inal2024themultidetectorct pages 7-8, otken2023hyperostosisfrontoparietooccipitalisa pages 4-5) | 2024, Romanian Journal of Rhinology; 2023, Cureus | https://doi.org/10.2478/rjr-2024-0018 ; https://doi.org/10.7759/cureus.41445 |
| Information source level | The retrieved evidence is mainly aggregated disease-level interpretation built from case reports, case series, and imaging studies rather than large registries or EHR-derived population datasets. | (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, hiremath2024diagnosticchallengesand pages 1-3, dogan2019morgagnisteawartmorelsendromuolgu pages 1-3, inal2024themultidetectorct pages 1-3) | 2025, European Journal of Case Reports in Internal Medicine; 2024, case report; 2019, Turkish Journal of Clinics and Laboratory; 2024, Romanian Journal of Rhinology | https://doi.org/10.12890/2025_005836 ; https://doi.org/10.18663/tjcl.453912 ; https://doi.org/10.2478/rjr-2024-0018 |


*Table: This table summarizes how the retrieved literature defines Morgagni–Stewart–Morel syndrome and related hyperostosis frontalis interna, including synonyms, missing identifiers in the retrieved sources, and the main diagnostic features. It is useful as a quick normalization and diagnostic reference for knowledge-base curation.*

---

## 1. Disease information

### 1.1 Concise overview
- **Disease definition (syndromic form):** MSMS is the term applied when **HFI coexists with metabolic, endocrine and neuropsychiatric abnormalities**. One recent source explicitly frames the definition as: MSMS is used when HFI “coexists with metabolic, endocrine and neuropsychiatric abnormalities,” and when HFI occurs with “virilisation, obesity and neuropsychiatric issues” it is classified as MSMS. (cetinok2025hyperostosisfrontalisinterna pages 5-6)
- **Key lesion:** HFI is repeatedly emphasized as the **principal radiologic hallmark** and the “only way to confirm” HFI is radiographic visualization of frontal inner-table thickening. (inal2024themultidetectorct pages 7-8, abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2)

### 1.2 Key identifiers (ontology/clinical coding)
The retrieved primary sources did **not** provide MONDO, OMIM, Orphanet, MeSH, or ICD-10/ICD-11 mappings for MSMS/HFI; therefore, these identifiers cannot be confirmed from the tool-retrieved literature in this run. (cetinok2025hyperostosisfrontalisinterna pages 5-6)

### 1.3 Synonyms and alternative names
- Morgagni syndrome; Stewart–Morel syndrome; Morgagni–Stewart–Morel syndrome; “metabolic craniopathy” (term used in older clinical literature). (dogan2019morgagnisteawartmorelsendromuolgu pages 1-3, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)
- Some case literature uses **HFI** as “aka MSMS,” but other sources distinguish **HFI (lesion)** from **MSMS (syndromic form)**. (hiremath2024diagnosticchallengesand pages 1-3, cetinok2025hyperostosisfrontalisinterna pages 5-6)

### 1.4 Evidence source type
Across retrieved sources, MSMS characterization is primarily derived from **individual case reports**, plus some **aggregated imaging cohorts** focused on HFI rather than MSMS specifically. (hiremath2024diagnosticchallengesand pages 1-3, inal2024themultidetectorct pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors (current evidence)
**No single validated causal gene or pathogen** emerges from the retrieved literature; the etiology is consistently described as uncertain, with hormonal/metabolic drivers repeatedly hypothesized.

**Hormonal/endocrine hypotheses**
- Long-term estrogen exposure and female sex/postmenopausal status are repeatedly discussed as central correlates of HFI/MSMS; one recent review-like paper states HFI occurs “nine times more frequently in women,” especially “postmenopausal women,” and links the condition to “long-term estrogen exposure,” obesity, diabetes, and endocrine imbalance. (cetinok2025hyperostosisfrontalisinterna pages 5-6)
- Case-based MSMS descriptions emphasize association with endocrine abnormalities (notably hypothyroidism in an acute presentation report). (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4)

**Metabolic hypotheses**
- Diabetes mellitus and obesity are commonly mentioned as associated conditions in MSMS/HFI. (inal2024themultidetectorct pages 7-8, otken2023hyperostosisfrontoparietooccipitalisa pages 4-5, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)

**Possible genetic contribution (low-evidence/older literature)**
- A case-report source notes possible autosomal dominant transmission as a hypothesis, but also states that overall etiology remains unexplained. (dogan2019morgagnisteawartmorelsendromuolgu pages 1-3)

### 2.2 Risk factors
Supported/recurring risk associations in retrieved literature:
- **Female sex and postmenopausal age** (strong association). (cetinok2025hyperostosisfrontalisinterna pages 5-6, inal2024themultidetectorct pages 1-3)
- **Obesity and diabetes mellitus**. (cetinok2025hyperostosisfrontalisinterna pages 5-6, otken2023hyperostosisfrontoparietooccipitalisa pages 4-5)
- **Endocrine disorders** (e.g., hypothyroidism; hyperparathyroidism). (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, inal2024themultidetectorct pages 7-8, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interaction
No explicit gene–environment interaction studies were retrieved.

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core phenotypes (with suggested HPO terms)
The syndrome is variably expressed, ranging from incidental HFI to symptomatic neuropsychiatric and endocrine/metabolic disease.

**A. Skeletal/imaging**
- Internal frontal hyperostosis / frontal inner-table thickening (core finding). (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, inal2024themultidetectorct pages 7-8)
  - Suggested HPO: **Hyperostosis frontalis interna (HP term likely exists; if not, map to Hyperostosis [HP:0100775])**

**B. Neurologic & neuropsychiatric**
- Headache (often cited; hypothesized relation to thickening). (inal2024themultidetectorct pages 1-3, inal2024themultidetectorct pages 7-8)
  - HPO: Headache **HP:0002315**
- Seizures/epilepsy reported in some cases. (cetinok2025hyperostosisfrontalisinterna pages 5-6, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)
  - HPO: Seizures **HP:0001250**
- Depression and other psychiatric disturbances; cognitive/behavioral changes reported. (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)
  - HPO: Depressed mood **HP:0000716**; Cognitive impairment **HP:0100543**; Abnormal behavior **HP:0000708**

**C. Endocrine/metabolic**
- Obesity (common association). (cetinok2025hyperostosisfrontalisinterna pages 5-6, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)
  - HPO: Obesity **HP:0001513**
- Diabetes mellitus and other metabolic disorders mentioned. (dogan2019morgagnisteawartmorelsendromuolgu pages 3-3, inal2024themultidetectorct pages 7-8)
  - HPO: Diabetes mellitus **HP:0000819**
- Hypothyroidism emphasized in at least one acute MSMS case. (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4)
  - HPO: Hypothyroidism **HP:0000821**
- Hyperparathyroidism mentioned as associated. (inal2024themultidetectorct pages 7-8, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)
  - HPO: Hyperparathyroidism **HP:0000873**

**D. Androgen-related/virilization phenotype**
- Hirsutism/virilization is repeatedly described in the classic MSMS triad. (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, dogan2019morgagnisteawartmorelsendromuolgu pages 3-3)
  - HPO: Hirsutism **HP:0001007**; Virilization **HP:0000841**

### 3.2 Onset, progression, severity (as reported)
- Demographic and temporal statements in one source suggest mild HFI can appear in early adulthood, while advanced forms and/or psychological symptoms are usually later (e.g., after mid-30s). (cetinok2025hyperostosisfrontalisinterna pages 5-6)
- Many patients are described as asymptomatic or having nonspecific symptoms. (cetinok2025hyperostosisfrontalisinterna pages 5-6)

### 3.3 Frequency among affected individuals
Robust phenotype frequencies for MSMS were not identified in retrieved sources; most evidence is descriptive. However, sex distribution for **diffuse HFI** in a CT series is quantified (see Epidemiology/Statistics). (inal2024themultidetectorct pages 3-4, inal2024themultidetectorct pages 1-3)

### 3.4 Quality of life impact
Quality-of-life instruments (EQ-5D/SF-36/PROMIS) were not reported in retrieved sources. Clinical narratives suggest significant functional impact in some cases (e.g., cognitive/behavioral change, gait decline, urinary incontinence, seizures), but no standardized QoL quantification was retrievable. (hiremath2024diagnosticchallengesand pages 1-3)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
- No validated causal genes or pathogenic variants for MSMS were identified in retrieved sources.

### 4.2 Proposed molecular contributors (hypothesis-level)
- One source discusses developmental bone formation mechanisms involving FGFR1 in neural crest cells (“The absence of Fgfr1 in neural crest cells results in heterotopic chondrogenesis and osteogenesis”), offered as mechanistic context for cranial heterotopic ossification rather than a proven MSMS mechanism. (cetinok2025hyperostosisfrontalisinterna pages 5-6)

### 4.3 Suggested ontology mappings (hypothesis-level)
- **GO biological process candidates:** osteoblast differentiation; bone mineralization; intramembranous ossification; bone remodeling.
- **CL cell types:** osteoblast (CL:0000062), osteoclast (CL:0000092), osteocyte (CL:0000132).

---

## 5. Environmental information
No toxin, occupational, radiation, or infectious triggers were identified in the retrieved sources. The dominant non-genetic associations were metabolic/endocrine (obesity, diabetes, hypothyroidism), which may reflect lifestyle and aging but are not explicitly treated as environmental exposures in the retrieved literature. (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2)

---

## 6. Mechanism / pathophysiology (proposed causal chains)

### 6.1 Leading mechanistic model (evidence-limited)
A recurring conceptual chain is:
1) **Hormonal/metabolic dysregulation** (e.g., estrogen exposure/imbalance; obesity/diabetes; hypothyroidism) (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2)
→ 2) **Altered cranial bone remodeling** with overgrowth of frontal inner table (HFI) (inal2024themultidetectorct pages 7-8, inal2024themultidetectorct pages 3-4)
→ 3) Potential **mass effect / intracranial volume reduction / cortical interaction** contributing to headaches, seizures, or neuropsychiatric symptoms in some patients; however the relationship is not conclusively established. (cetinok2025hyperostosisfrontalisinterna pages 5-6, abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4)

### 6.2 Imaging/functional correlates supporting mechanism hypotheses
- A recent review-like paper states calvarial thickening may reduce intracranial volume, and discusses scintigraphy/PET findings with symmetric frontal uptake patterns (e.g., a “butterfly pattern” on bone scintigraphy), reflecting altered bone metabolism/activity. (cetinok2025hyperostosisfrontalisinterna pages 5-6)

### 6.3 Suggested ontology mappings
- **UBERON (anatomy):** frontal bone (UBERON:0001421); skull (UBERON:0003129); cerebral cortex (UBERON:0000956).
- **GO cellular component:** extracellular matrix; bone extracellular matrix.

---

## 7. Anatomical structures affected
- **Primary:** frontal bone inner table (HFI). (inal2024themultidetectorct pages 7-8)
- **Secondary/adjacent:** potential compression/interaction with frontal lobes/dura; one case report notes frontal lobe compression with clinical syndrome and improvement after surgical intervention. (hiremath2024diagnosticchallengesand pages 1-3)

---

## 8. Temporal development
- Typically described as a disorder of **older women**, often postmenopausal, with long-term progression of thickening. (cetinok2025hyperostosisfrontalisinterna pages 5-6, inal2024themultidetectorct pages 1-3)
- Acute life-threatening presentations are reported but appear rare; one 2025 acute case highlights emergency recognition when HFI coexists with severe endocrine dysfunction. (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (statistics available from recent studies)
MSMS-specific population prevalence is not established in retrieved sources; HFI prevalence and sex distribution are better studied.

**CT cohort (2024) – diffuse HFI**
- Retrospective CT cohort: **154 adults with diffuse HFI** and **151 controls**. Mean age of HFI group **69.33 ± 14.34** years. Sex distribution in HFI group: **148/154 (96.1%) female** and **6/154 (3.9%) male**. (In controls: 143/151 female, 8/151 male; p=0.559). (inal2024themultidetectorct pages 1-3, inal2024themultidetectorct pages 3-4)

**Cadaveric cohort (2016–2019 sampling, published 2025) – HFI prevalence**
- 74 donors examined; HFI in **31/74 (41.89%)**. Reported sex-specific proportions: **32.43% in women** and **9.45% in men** (as presented by the authors for their sample). (cetinok2025hyperostosisfrontalisinterna pages 2-3)

### 9.2 Demographics
- Strong female predominance, particularly postmenopausal age. (cetinok2025hyperostosisfrontalisinterna pages 5-6, inal2024themultidetectorct pages 1-3)

### 9.3 Inheritance
- A possible autosomal dominant hypothesis is mentioned in older case-report literature, but no genetic validation was identified in retrieved sources. (dogan2019morgagnisteawartmorelsendromuolgu pages 1-3)

---

## 10. Diagnostics

### 10.1 Clinical evaluation
- MSMS diagnosis in practice appears to rely on recognizing **HFI on imaging** plus a compatible syndromic context (obesity/endocrinopathy/neuropsychiatric symptoms), with emphasis on multidisciplinary evaluation (neurology + endocrinology + radiology). (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2, inal2024themultidetectorct pages 1-3)

### 10.2 Imaging
- **CT:** highlighted as confirmatory; the 2024 CT study quantified increased thickness at vertex, frontal tuberosity, and frontal sinus levels in diffuse HFI. Example vertex thickness (HFI vs controls): midline **12.88±3.43 mm vs 8.01±2.04 mm**, right lateral **15.94±4.75 mm vs 8.69±1.96 mm**, left lateral **15.48±4.66 mm vs 8.64±1.97 mm**. (inal2024themultidetectorct pages 3-4)
- **CT density:** example vertex density in HFI regions **1064.56±244.33 HU** vs controls **837.06±214.25 HU**. (inal2024themultidetectorct pages 3-4)
- **Imaging measurement approach (visual evidence):** the CT measurement scheme for thickness/density at specified levels is shown in figures from the 2024 CT paper. (inal2024themultidetectorct media cb19ca47, inal2024themultidetectorct media a3b14aa3)

### 10.3 Differential diagnosis (radiology)
- Suggested differentials in retrieved sources include Paget disease, fibrous dysplasia, acromegaly, other cranial hyperostosis syndromes, and other causes of calvarial thickening. (inal2024themultidetectorct pages 7-8, otken2023hyperostosisfrontoparietooccipitalisa pages 4-5)

### 10.4 Diagnostic criteria
No standardized diagnostic criteria or society guidelines were identified in the retrieved sources.

### 10.5 Genetic testing
No gene-based diagnostic strategy was supported by retrieved evidence.

---

## 11. Outcome / prognosis
- Many cases are described as incidental/asymptomatic, suggesting benign course for HFI itself; nevertheless, symptomatic neuropsychiatric and endocrine complications can be clinically significant. (cetinok2025hyperostosisfrontalisinterna pages 5-6)
- An acute case report demonstrates that severe endocrine dysfunction (profound hypothyroidism) with HFI can lead to respiratory failure and depressed consciousness, but clinical improvement followed supportive care and thyroid hormone replacement. (abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4)

No survival curves, mortality rates, or validated prognostic biomarkers were identified in the retrieved sources.

---

## 12. Treatment (current practice / real-world implementations)
No disease-modifying therapy for HFI/MSMS is established in retrieved sources; management is generally symptomatic and comorbidity-focused.

### 12.1 Multidisciplinary supportive care
- One MSMS acute case emphasizes airway/ventilation stabilization and multisystem management; endocrine treatment (thyroid hormone replacement) was central to recovery when hypothyroidism was severe. (abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4)

### 12.2 Endocrine/metabolic management
- The 2024 CT cohort recommends that when HFI is detected, **endocrinological assessment** should be performed and clinicians should consult radiology; it highlights the need to explore the HFI–headache relationship. (inal2024themultidetectorct pages 1-3, inal2024themultidetectorct pages 7-8)

### 12.3 Neurosurgical intervention (selected cases)
- A 2024 case report describes frontal bone thickening with frontal lobe compression; it states that **surgical intervention** led to significant clinical improvement in that patient context. (hiremath2024diagnosticchallengesand pages 1-3)

### 12.4 MAXO suggestions (for knowledge base annotation)
- Endocrine hormone replacement therapy (e.g., thyroid hormone replacement)
- Metabolic disease management
- Neurosurgical decompression / cranioplasty (selected cases)
- Antiseizure medication (if seizures)

(These MAXO mappings are suggestions; specific MAXO IDs were not provided in retrieved sources.)

### 12.5 Clinical trials
A clinical trial search did not yield a clearly relevant interventional trial for MSMS/HFI within the retrieved trial record set. (clinical trials tool run produced no relevant trials)

---

## 13. Prevention
No MSMS-specific primary/secondary prevention strategies were identified in retrieved sources. Reasonable prevention concepts are indirect (management of obesity/diabetes/endocrine disorders), but direct evidence for prevention of HFI/MSMS is not established in retrieved literature. (cetinok2025hyperostosisfrontalisinterna pages 5-6)

---

## 14. Other species / natural disease
No naturally occurring MSMS/HFI animal disease reports were identified in the retrieved sources.

---

## 15. Model organisms
No MSMS-specific model organism systems were identified in retrieved sources. Mechanistic discussion referencing FGFR1/neural crest perturbation was presented as developmental biology context rather than a validated MSMS model. (cetinok2025hyperostosisfrontalisinterna pages 5-6)

---

## Recent developments (prioritizing 2023–2024)

### 2024: Quantitative CT characterization of diffuse HFI
- A 2024 multidetector CT study (n=154 diffuse HFI) provided quantitative thickness/density data and reinforced the strong female predominance (96.1% female). It also recommended clinician recognition and endocrinologic assessment when HFI is detected. (inal2024themultidetectorct pages 1-3, inal2024themultidetectorct pages 3-4, inal2024themultidetectorct pages 7-8)

### 2024: Diagnostic pitfalls and management implications in neurology
- A 2024 case report highlighted misdiagnosis risk (initially considered autoimmune encephalitis) and emphasized that HFI may present with neurobehavioral syndromes and that selected cases with compression may benefit from neurosurgical management. (hiremath2024diagnosticchallengesand pages 1-3)

### 2023: Continued reliance on case-based synthesis for MSMS
- A 2023 anatomical case report reiterated the classic syndromic association: MSMS as HFI plus “hormonal imbalances, neuropsychiatric disease, and metabolic disturbances such as obesity and diabetes,” and emphasized that radiography is often required for detection. (otken2023hyperostosisfrontoparietooccipitalisa pages 4-5)

---

## Expert opinions / authoritative analysis (from retrieved sources; evidence-limited)
Because MSMS is rare, “authoritative” views in the retrieved set largely come from radiology/anatomy reviews and case-report discussions:
- A recent review-like article notes many patients are “typically asymptomatic or exhibit non-specific symptoms, including headache, neurological, or mental issues,” underscoring uncertainty about symptom attribution to HFI. (cetinok2025hyperostosisfrontalisinterna pages 5-6)
- The 2024 CT cohort’s concluding clinical guidance is pragmatic (recognize imaging pattern, consider headache association, consult radiology, and evaluate endocrine status). (inal2024themultidetectorct pages 1-3)

---

## Direct quotes from abstracts (from retrieved sources)
- “Morgagni–Stewart–Morel (MSM) syndrome is the term used when hyperostosis frontalis interna (HFI) coexists with metabolic, endocrine and neuropsychiatric abnormalities.” (cetinok2025hyperostosisfrontalisinterna pages 5-6)
- “The only way to confirm a diagnosis of HFI is through a radiographic image that clearly shows thickened bone.” (inal2024themultidetectorct pages 7-8)

---

## Key limitations of this evidence package
1. **Ontology identifiers (MONDO/OMIM/Orphanet/MeSH/ICD)** were not present in the retrieved sources and could not be verified here.
2. **PMIDs** were not available in the retrieved excerpts/metadata for the key recent sources used.
3. MSMS-specific epidemiology is poorly defined; most quantification is for **HFI**, not the full MSMS syndrome.
4. Mechanistic claims are largely hypothesis-driven, with limited direct molecular evidence.

## Primary URLs (publication dates where available)
- Inal et al. “The multidetector CT evaluation of diffuse hyperostosis frontalis interna.” **Jul 2024**. https://doi.org/10.2478/rjr-2024-0018 (inal2024themultidetectorct pages 1-3)
- Otken et al. “Hyperostosis Fronto-Parieto-Occipitalis: A Cadaveric Case Report.” **Jul 2023**. https://doi.org/10.7759/cureus.41445 (otken2023hyperostosisfrontoparietooccipitalisa pages 4-5)
- Doğan & Mouline. “Morgagni-Steawart-Morel sendromu: Olgu sunumu.” **Sep 2019**. https://doi.org/10.18663/tjcl.453912 (dogan2019morgagnisteawartmorelsendromuolgu pages 1-3)
- Hiremath et al. “Diagnostic challenges and therapeutic implications of Hyperostosis Frontalis Interna (HFI)…” **2024** (journal/URL not available in retrieved record). (hiremath2024diagnosticchallengesand pages 1-3)
- (Post-2024, included for completeness) Abdallah et al. MSMS acute presentation. **Oct 2025**. https://doi.org/10.12890/2025_005836 (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2)
- (Post-2024, included for completeness) Çetinok. “Hyperostosis Frontalis Interna and Its Clinical Significance.” **Jun 2025**. https://doi.org/10.53446/actamednicomedia.1644183 (cetinok2025hyperostosisfrontalisinterna pages 5-6)


References

1. (cetinok2025hyperostosisfrontalisinterna pages 5-6): Hürriyet Çetinok. Hyperostosis frontalis interna and its clinical significance. Acta Medica Nicomedia, 8:169-175, Jun 2025. URL: https://doi.org/10.53446/actamednicomedia.1644183, doi:10.53446/actamednicomedia.1644183. This article has 1 citations.

2. (abdallah2025morgagnistewartmorelsyndromepresenting pages 1-2): Marwa Ben Abdallah, Aymen Farroukh, Faten Mzoughi, Houssem Affes, Mariam Mallek, Wassel Mokni, and Adel Chaari. Morgagni-stewart-morel syndrome presenting as acute neurological and respiratory distress. European Journal of Case Reports in Internal Medicine, Oct 2025. URL: https://doi.org/10.12890/2025\_005836, doi:10.12890/2025\_005836. This article has 0 citations.

3. (inal2024themultidetectorct pages 7-8): Mikail Inal, Nuray Bayar Muluk, and Enes Nusret Celik. The multidetector ct evaluation of diffuse hyperostosis frontalis interna. Romanian Journal of Rhinology, 14:117-124, Jul 2024. URL: https://doi.org/10.2478/rjr-2024-0018, doi:10.2478/rjr-2024-0018. This article has 0 citations.

4. (dogan2019morgagnisteawartmorelsendromuolgu pages 3-3): E. Doğan and M. Mouline. Morgagni-steawart-morel sendromu: olgu sunumu. Turkish Journal of Clinics and Laboratory, Sep 2019. URL: https://doi.org/10.18663/tjcl.453912, doi:10.18663/tjcl.453912. This article has 1 citations.

5. (dogan2019morgagnisteawartmorelsendromuolgu pages 1-3): E. Doğan and M. Mouline. Morgagni-steawart-morel sendromu: olgu sunumu. Turkish Journal of Clinics and Laboratory, Sep 2019. URL: https://doi.org/10.18663/tjcl.453912, doi:10.18663/tjcl.453912. This article has 1 citations.

6. (inal2024themultidetectorct pages 3-4): Mikail Inal, Nuray Bayar Muluk, and Enes Nusret Celik. The multidetector ct evaluation of diffuse hyperostosis frontalis interna. Romanian Journal of Rhinology, 14:117-124, Jul 2024. URL: https://doi.org/10.2478/rjr-2024-0018, doi:10.2478/rjr-2024-0018. This article has 0 citations.

7. (inal2024themultidetectorct pages 1-3): Mikail Inal, Nuray Bayar Muluk, and Enes Nusret Celik. The multidetector ct evaluation of diffuse hyperostosis frontalis interna. Romanian Journal of Rhinology, 14:117-124, Jul 2024. URL: https://doi.org/10.2478/rjr-2024-0018, doi:10.2478/rjr-2024-0018. This article has 0 citations.

8. (cetinok2025hyperostosisfrontalisinterna pages 2-3): Hürriyet Çetinok. Hyperostosis frontalis interna and its clinical significance. Acta Medica Nicomedia, 8:169-175, Jun 2025. URL: https://doi.org/10.53446/actamednicomedia.1644183, doi:10.53446/actamednicomedia.1644183. This article has 1 citations.

9. (otken2023hyperostosisfrontoparietooccipitalisa pages 4-5): Emily Otken, Emily O'Brien, Braden Nyboer, Huy Nguyen, Cody Orvin, and Adegbenro O Fakoya. Hyperostosis fronto-parieto-occipitalis: a cadaveric case report. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.41445, doi:10.7759/cureus.41445. This article has 1 citations.

10. (abdallah2025morgagnistewartmorelsyndromepresenting pages 2-4): Marwa Ben Abdallah, Aymen Farroukh, Faten Mzoughi, Houssem Affes, Mariam Mallek, Wassel Mokni, and Adel Chaari. Morgagni-stewart-morel syndrome presenting as acute neurological and respiratory distress. European Journal of Case Reports in Internal Medicine, Oct 2025. URL: https://doi.org/10.12890/2025\_005836, doi:10.12890/2025\_005836. This article has 0 citations.

11. (inal2024themultidetectorct pages 5-7): Mikail Inal, Nuray Bayar Muluk, and Enes Nusret Celik. The multidetector ct evaluation of diffuse hyperostosis frontalis interna. Romanian Journal of Rhinology, 14:117-124, Jul 2024. URL: https://doi.org/10.2478/rjr-2024-0018, doi:10.2478/rjr-2024-0018. This article has 0 citations.

12. (inal2024themultidetectorct pages 4-5): Mikail Inal, Nuray Bayar Muluk, and Enes Nusret Celik. The multidetector ct evaluation of diffuse hyperostosis frontalis interna. Romanian Journal of Rhinology, 14:117-124, Jul 2024. URL: https://doi.org/10.2478/rjr-2024-0018, doi:10.2478/rjr-2024-0018. This article has 0 citations.

13. (inal2024themultidetectorct media cb19ca47): Mikail Inal, Nuray Bayar Muluk, and Enes Nusret Celik. The multidetector ct evaluation of diffuse hyperostosis frontalis interna. Romanian Journal of Rhinology, 14:117-124, Jul 2024. URL: https://doi.org/10.2478/rjr-2024-0018, doi:10.2478/rjr-2024-0018. This article has 0 citations.

14. (hiremath2024diagnosticchallengesand pages 1-3): PM Hiremath, A Mehta, and R Srinivasa. Diagnostic challenges and therapeutic implications of hyperostosis frontalis interna (hfi) in a post-menopausal woman-a case report. Unknown journal, 2024.

15. (inal2024themultidetectorct media a3b14aa3): Mikail Inal, Nuray Bayar Muluk, and Enes Nusret Celik. The multidetector ct evaluation of diffuse hyperostosis frontalis interna. Romanian Journal of Rhinology, 14:117-124, Jul 2024. URL: https://doi.org/10.2478/rjr-2024-0018, doi:10.2478/rjr-2024-0018. This article has 0 citations.
