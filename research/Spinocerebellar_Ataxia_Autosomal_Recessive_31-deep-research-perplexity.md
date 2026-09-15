---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-23T07:40:49.167065'
end_time: '2026-08-23T07:45:17.000774'
duration_seconds: 267.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinocerebellar ataxia, autosomal recessive 31 (SCAR31, biallelic
    ATG7 deficiency)
  mondo_id: MONDO:0030323
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 17
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar ataxia, autosomal recessive 31 (SCAR31, biallelic ATG7 deficiency)
- **MONDO ID:** MONDO:0030323 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar ataxia, autosomal recessive 31 (SCAR31, biallelic ATG7 deficiency)** covering all of the
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

# Spinocerebellar ataxia, autosomal recessive 31 (SCAR31, biallelic ATG7 deficiency): comprehensive characterization for disease knowledge bases

Spinocerebellar ataxia, autosomal recessive 31 (SCAR31) is a recently defined, ultra‑rare, Mendelian neurodevelopmental disorder caused by biallelic deleterious variants in the autophagy gene **ATG7**, leading to a congenital disorder of autophagy characterized by global developmental delay, hypotonia, cerebellar ataxia, musculoskeletal and endocrine abnormalities, and characteristic brain malformations including cerebellar hypoplasia and thinning of the posterior corpus callosum.[1][3][7][13] The disorder demonstrates how near‑complete loss of a non‑redundant core autophagy protein in humans can be compatible with survival into adulthood, but at the cost of profound neurological and systemic impairment.[3][7] Mechanistically, ATG7 deficiency disrupts canonical degradative autophagy by impairing ATG12–ATG5 conjugation and LC3 lipidation, resulting in diminished autophagic flux, accumulation of cargo adaptors such as p62/SQSTM1, defective long‑lived protein degradation, and widespread cellular stress in selectively vulnerable tissues including cerebellar Purkinje cells, skeletal muscle, hematopoietic lineages, and endocrine organs.[3][5][7][15][16] Clinically, SCAR31 must be distinguished from the adult‑onset autosomal dominant spinocerebellar ataxia type 31 (SCA31) caused by BEAN1 repeat expansions, highlighting the importance of precise molecular diagnosis.[8][13] This report synthesizes current knowledge about SCAR31 across clinical, genetic, mechanistic, anatomical, diagnostic, prognostic, therapeutic, preventive, comparative, and model organism dimensions, with explicit annotation to biomedical ontologies and primary literature, to support structured representation in disease knowledge bases.

## 1. Disease Information

### 1.1. Concise overview and core definition

Spinocerebellar ataxia, autosomal recessive 31 (SCAR31) is a **Mendelian neurodevelopmental ataxia syndrome** caused by homozygous or compound heterozygous loss‑of‑function variants in **ATG7** on chromosome 3p25.3.[1][5][13] Patients present in infancy or early childhood with global developmental delay, axial and appendicular hypotonia, variably impaired intellectual and language development, and a characteristic motor phenotype dominated by an ataxic gait, tremor, dysarthria, and, in more severe cases, spasticity that can culminate in inability to walk.[1][3][7][13] Brain MRI consistently reveals cerebellar hypoplasia and a thin posterior corpus callosum, often with enlarged ventricles, indicating a neurodevelopmental rather than purely neurodegenerative process.[3][7][13] Additional features include optic atrophy or other ocular dysfunction, retinitis pigmentosa, sensorineural hearing loss, musculoskeletal abnormalities such as reduced muscle mass and strength, facial dysmorphism, and occasional endocrine dysfunction.[3][7][13] 

At the molecular level, ATG7 encodes a ubiquitin‑like modifier‑activating enzyme essential for both the ATG12 conjugation system and LC3 (ATG8 family) lipidation, which are core steps in autophagosome biogenesis and autophagic cargo sequestration.[5][7][15] The first description of human ATG7 deficiency came from a series of twelve patients from five unrelated families who harbored deleterious biallelic ATG7 variants and exhibited a complex neurodevelopmental disorder with brain, muscle, and endocrine involvement; this study provided compelling evidence that impaired autophagy resulting from ATG7 dysfunction underlies SCAR31.[3][7] As the review by Collier and colleagues emphasized, this discovery established **“a direct association between ATG7 dysfunction and disease … in patients with biallelic ATG7 variants and childhood‑onset neuropathology”**.[7] The disease thus represents a paradigmatic human congenital autophagy defect, with implications for understanding autophagy’s role in nervous system development and maintenance.

### 1.2. Key identifiers and ontology mapping

SCAR31 is catalogued in multiple disease classification systems and ontologies. The Online Mendelian Inheritance in Man (OMIM) database designates **“Spinocerebellar ataxia, autosomal recessive 31”** with MIM number **619422**, and explicitly links it to biallelic ATG7 mutations on chromosome 3p25.3.[1][5][12][13] The OMIM entry uses a number sign (#) to indicate that SCAR31 is defined by molecular evidence implicating ATG7 as the causative gene.[1] The ATG7 gene itself has OMIM gene entry **608760**, with cytogenetic location 3p25.3 and mapping to genomic coordinates 3:11,272,397–11,576,353 (GRCh38).[5] 

Orphanet recognizes SCAR31 under the concept associated with **ORPHA:88644**, as indicated in linkage tables that connect OMIM phenotype 619422 to Orphanet disease nomenclature.[12][13] In the Disease Ontology, SCAR31 is represented under **DOID:0070412**, with the definition “an autosomal recessive cerebellar ataxia characterized by global developmental delay with hypotonia and variably impaired intellectual and language development that has material basis in homozygous or compound heterozygous mutation in the ATG7 gene on chromosome 3p25.”[14] The Zebrafish Information Network (ZFIN) explicitly cross‑references ATG7 and its zebrafish ortholog *atg7* to DOID:0070412, providing an ontological bridge for comparative disease modeling.[14] In the Mondo Disease Ontology, SCAR31 is aligned as **MONDO:0030323**, corresponding to “autosomal recessive spinocerebellar ataxia 31,” although this identifier is inferred from curation rather than directly shown in the search snippets.

Malacards maintains distinct entries for **“Spinocerebellar ataxia 31 (SCA31)”** and **“Spinocerebellar ataxia, autosomal recessive 31 (SCAR31)”**, avoiding conflation between the autosomal dominant BEAN1‑associated adult‑onset SCA31 and the autosomal recessive ATG7‑related congenital ataxia.[8][13] The SCAR31 Malacards entry aggregates information from ClinVar, MedGen, OMIM, and PubMed, and lists multiple external clinical coding identifiers, including numerous SNOMED CT and related terminologies, reflecting the disease’s integration into electronic health record and terminology systems.[13] ICD‑10 and ICD‑11 do not currently provide a unique code specifically for SCAR31; affected individuals are generally coded under the broader category of **hereditary ataxia** (ICD‑10 G11.x, ICD‑11 8B10), or under global developmental delay, depending on clinical context, although these codes are not explicitly documented in the provided resources.

In terms of ontology mapping for structured knowledge bases, SCAR31 can be represented by the Mondo term for autosomal recessive spinocerebellar ataxia 31 (MONDO:0030323), with cross‑links to OMIM:619422, DOID:0070412, ORPHA:88644, and SNOMED CT concepts for hereditary ataxia and developmental delay.[12][13][14] The ATG7 gene is annotated with HGNC symbol **ATG7**, OMIM:608760, UniProt accession O95352, and relevant Gene Ontology (GO) terms for autophagy, ubiquitin‑like protein ligase activity, and cytoplasm‑to‑vacuole transport.[5][7][15]

### 1.3. Synonyms and alternative names

The primary preferred name for the disease in clinical and genetic databases is **“Spinocerebellar ataxia, autosomal recessive 31”**, often abbreviated as **SCAR31**.[1][12][13][14] Synonymous phrases include **“autosomal recessive spinocerebellar ataxia 31”**, **“autosomal recessive cerebellar ataxia 31”**, and more descriptive expressions such as **“ATG7‑related neurodevelopmental disorder”** or **“congenital disorder of autophagy due to ATG7 deficiency”**, as used in mechanistic reviews.[1][3][7][13][14] The Disease Ontology synonym list explicitly includes “SCAR31” and “autosomal recessive spinocerebellar ataxia 31” for DOID:0070412.[14] 

It is important to distinguish SCAR31 from **spinocerebellar ataxia type 31 (SCA31)**, an autosomal dominant adult‑onset disorder caused by a repeat expansion mutation in the **BEAN1** gene, which manifests as progressive cerebellar ataxia, dysarthria, horizontal gaze‑evoked nystagmus, and occasionally pyramidal signs and hearing difficulties.[8] Malacards clearly separates the two entities, assigning SCA31 to autosomal dominant cerebellar ataxias type III (ADCA III) characterized by pure cerebellar ataxia, and SCAR31 to autosomal recessive cerebellar ataxias with complex neurodevelopmental features.[8][13] Confusing these entities could lead to misinterpretation of inheritance patterns and misdirection of genetic testing; hence knowledge bases should ensure that synonyms and cross‑references accurately capture this distinction.

### 1.4. Source of information: aggregate versus individual data

The current characterization of SCAR31 is derived primarily from **aggregated disease‑level resources** and **case series published in the clinical genetics literature**, rather than large‑scale epidemiologic datasets or de‑identified EHR mining. OMIM and Malacards compile information from Collier et al.’s landmark paper describing twelve patients from five unrelated families, together with earlier functional studies of ATG7 in model organisms and autophagy biology.[1][3][5][7][13] The Disease Ontology and ZFIN entries reflect curated definitions based on this literature and on OMIM cross‑references.[14] The Collier et al. study is based on detailed clinical, neuroimaging, histopathologic, and functional analyses of individual patients and their cells, but the data are presented as a cohesive syndrome rather than as population‑level statistical summaries.[3] 

The review “Emerging roles of ATG7 in human health and disease” integrates data from human patients with biallelic ATG7 variants, mouse Atg7 knockout models, and other experimental systems to provide a broader disease concept—congenital ATG7 deficiency as a **“recessive congenital disorder of autophagy”** hallmarked by neurodevelopmental deficits.[7] Malacards and OMIM additionally draw on ClinVar submissions and text‑mined publications to identify specific variants and associated phenotypes.[5][13] At present, there is no dedicated registry or large natural history cohort for SCAR31, and no evidence that clinical decision support systems or EHR‑based phenome‑wide association studies have contributed substantially to disease definition. Knowledge bases should therefore treat SCAR31 as an entity whose characteristics are based on a relatively small but well‑described clinical series, enriched by extensive mechanistic data from model organisms and cellular studies.

## 2. Etiology

### 2.1. Primary causal factors: genetic basis and mechanistic classification

The primary causal factor for SCAR31 is **biallelic deleterious variants in the ATG7 gene**, leading to **germline, autosomal recessive loss of function** in a core autophagy effector enzyme.[1][3][5][7][13] ATG7 encodes an E1‑like ubiquitin‑activating enzyme essential for the conjugation of ATG12 to ATG5 and for LC3 (ATG8) lipidation, both of which are critical steps in autophagosome formation and function.[5][7][15] In their seminal study, Collier et al. identified eleven patients from five unrelated families with homozygous or compound heterozygous ATG7 mutations, including one family with biallelic complete loss‑of‑function variants.[1][3] The authors reported that **“twelve patients from five families with distinct ATG7 variants had complex neurodevelopmental disorders with brain, muscle, and endocrine involvement,”** and they concluded that **“impaired autophagy resulting from biallelic deleterious ATG7 variants is a cause of neurodevelopmental disorders involving neurologic, musculoskeletal, and endocrine involvement.”**[3] 

Mechanistically, ATG7 dysfunction leads to **autophagy deficiency** in affected tissues, as evidenced by diminished ATG7 protein levels, defective ATG7 dimerization and protein folding, reduced LC3 processing, and impaired autophagic flux in patient fibroblasts and skeletal muscle.[1][3][7] OMIM summarizes that patient cells show decreased ATG7 protein associated with defective folding and dimerization, accumulation of p62 (SQSTM1) in puncta, and impaired LC3 processing, all of which are classic signatures of autophagy impairment.[1] Functional rescue experiments in patient cells demonstrate that expression of wild‑type ATG7 can restore autophagic defects, strongly supporting a causal relationship between ATG7 loss of function and the disease phenotype.[1][3] Similar studies in yeast and mouse models show that ATG7 deletion or mutation severely attenuates autophagy, leading to neurodegeneration and tissue dysfunction.[1][5][7][9][15]

From an etiologic classification perspective, SCAR31 is a **monogenic, germline, loss‑of‑function disorder of autophagy**, with mechanisms grounded in disruption of cellular degradation and homeostasis pathways. There is no evidence that environmental, infectious, or acquired factors play a primary causal role; however, environmental influences may modulate disease expression and progression, as discussed below.

### 2.2. Genetic risk factors: causal variants and potential susceptibility loci

The principal genetic risk factors for SCAR31 are **rare, deleterious ATG7 variants** that abolish or severely compromise protein function when present in both alleles. Collier et al. catalogued multiple missense, nonsense, and splice‑site variants scattered across the ATG7 coding sequence, affecting highly conserved residues in functional domains.[3] The OMIM SCAR31 entry notes that in eleven patients from five families, there were **“1 nonsense, 2 splice site, and 6 missense mutations,”** and that only one family had biallelic complete loss‑of‑function mutations, though there was not a clear genotype–phenotype correlation.[1] Examples include missense variants such as c.1727G>A (p.Arg576His), c.1870C>T (p.His624Tyr), c.700C>A (p.Pro234Thr), and c.1762G>A (p.Val588Met), all affecting amino acids that are highly conserved across species.[3] Malacards lists specific pathogenic variants, including a nonsense variant NM_001349232.2(ATG7):c.339G>A (p.Trp113Ter) classified as pathogenic in ClinVar, reflecting the presence of early truncating alleles among disease‑causing variants.[13] 

These variants are **germline** and segregate in families following autosomal recessive inheritance, with affected individuals typically born to heterozygous carrier parents who are clinically unaffected.[1][3][13] Exome sequencing in Collier’s series identified ATG7 variants in affected individuals but not in unaffected relatives, and segregation analysis supported recessive transmission.[3] The transmission pattern in the families reported by Collier et al. was explicitly described as consistent with autosomal recessive inheritance.[1][3] There is no evidence that somatic mutations in ATG7 contribute to SCAR31; somatic ATG7 alterations may be relevant to cancer or other acquired conditions, but they are outside the etiologic spectrum of this congenital disorder.[7]

Population genetic data from gnomAD and other databases indicate that **loss‑of‑function variants in ATG7 are extremely rare**, consistent with strong purifying selection against disruptive alleles, yet the existence of SCAR31 kindreds indicates that such variants do occur at low frequency in specific populations.[11] gnomAD implements the **loss‑of‑function observed/expected upper bound fraction (LOEUF)** metric to quantify gene intolerance to loss‑of‑function variation, and ATG7 is categorized among genes with low LOEUF, indicating intolerance to LoF even in general populations.[11][7] The gnomAD v4.0 constraint update notes that genes in each LOEUF decile are stable across versions, and recommends LOEUF <0.6 as a threshold for LoF‑constrained genes.[11] ATG7 falls into these constrained categories, supporting its essential role and explaining the rarity of biallelic null alleles. Nevertheless, the Collier cohort demonstrates that complete or near‑complete ATG7 loss can be compatible with human life in rare familial contexts, albeit with severe pathology.[3][7]

Beyond ATG7, other autophagy genes such as **ATG5**, **WIPI2**, **WDR45**, **WDR45B**, and **ATG9B** have been implicated in Mendelian human diseases with neurodevelopmental or neurodegenerative features, suggesting that the autophagy machinery as a whole constitutes a network of potential susceptibility loci for related phenotypes.[4][7][10] For example, Kim et al. described two siblings with congenital ataxia and mental retardation due to a homozygous missense mutation in ATG5, which reduced autophagy and led to neurodevelopmental defects, providing a parallel to ATG7 deficiency.[4] An MDPI study on ATG9B variants notes that ATG7 mutations have been linked to Mendelian diseases causing spinocerebellar ataxia and neurodevelopmental disorders, situating SCAR31 within a broader class of autophagy‑related human pathologies.[10] However, in the context of SCAR31, ATG7 is the sole established causal gene, and no modifier genes or polygenic susceptibility loci have yet been identified with robust evidence.

### 2.3. Environmental and lifestyle risk factors

To date, there is **no direct evidence** that specific environmental exposures, toxins, lifestyle factors, or infectious agents act as primary risk factors for developing SCAR31, which is determined by germline, biallelic ATG7 variants present at conception.[1][3][7][13] Because the disease is rare and familial, environmental studies are lacking, and no association has been reported between SCAR31 and occupational exposures, dietary patterns, perinatal insults, or infections. It is theoretically possible that environmental factors influencing autophagy—such as caloric intake, physical activity, or certain medications—could modify disease severity or progression by modulating residual autophagic capacity, especially in patients with hypomorphic rather than null ATG7 alleles, but this remains speculative and untested in clinical cohorts.

General considerations for neurodevelopmental disorders suggest that enriched environments, early intervention, nutrition, and avoidance of neurotoxic exposures may influence functional outcomes, but these are nonspecific and not documented as formal risk factors for SCAR31. Knowledge bases should therefore categorize environmental risk factors for SCAR31 as **unknown or not established**, while acknowledging that autophagy is sensitive to metabolic and stress cues, which might interact with genetic defects in complex ways. 

### 2.4. Protective factors and gene–environment interactions

Similarly, **specific protective factors** for SCAR31 have not been identified. The autosomal recessive inheritance pattern implies that **heterozygous carriers** of ATG7 loss‑of‑function variants do not manifest overt disease and may be protected by one functional allele, reflecting the sufficiency of 50% ATG7 dosage for normal autophagy in most tissues.[1][3][7] At a population level, the strong purifying selection against ATG7 loss‑of‑function and the low frequency of deleterious alleles in gnomAD suggest that the human genome and environmental milieu collectively maintain robust autophagic capacity as a protective mechanism.[11][7] However, this is an evolutionary perspective rather than an individual‑level protective factor.

Gene–environment interactions for SCAR31 are **largely unexplored**. Autophagy responds to nutrient deprivation, oxidative stress, infection, and other environmental stimuli, and ATG7 plays a central role in transducing these signals into autophagic responses.[7][15] In model organisms, nutrient status, caloric restriction, and pharmacologic modulators of mTOR and AMPK strongly influence autophagy, and could hypothetically modulate phenotypes in ATG7‑deficient states.[7][16] For example, Clarke et al. demonstrated that B1a B cells depend on autophagy for metabolic homeostasis and self‑renewal, and that deletion of Atg7 causes accumulation of dysfunctional mitochondria and global metabolic dysfunction.[16] They observed that autophagy‑deficient B1a cells fail to utilize lipophagy to manage lipid stores, implicating environmental lipid availability as a potential modifier of autophagy‑deficient phenotypes.[16] Translating such gene–environment interactions to human SCAR31 patients would require detailed metabolic and clinical studies, which have not yet been performed.

From an ontology standpoint, potential gene–environment interactions could be described using CTD (Comparative Toxicogenomics Database) entries linking ATG7 to environmental chemicals, or using GxE ontologies to represent interactions between ATG7 variants and nutritional or pharmacologic exposures, but at present these would be speculative. Knowledge bases should therefore indicate that **no validated gene–environment interactions are known for SCAR31**, while flagging autophagy biology as a mechanistic framework that may eventually give rise to such interactions.

## 3. Phenotypes

### 3.1. Overall clinical phenotype and age of onset

SCAR31 presents as a **complex neurodevelopmental disorder** with multi‑system involvement, dominated by neurological, musculoskeletal, ocular, and endocrine features emerging in infancy or early childhood.[1][3][7][13][14] OMIM describes SCAR31 as a disorder characterized by **“global developmental delay with hypotonia and variably impaired intellectual and language development,”** accompanied by an ataxic gait, tremor, and dysarthria; more severely affected patients also have spasticity with inability to walk.[1] Malacards and the Disease Ontology reiterate this definition, emphasizing global developmental delay and hypotonia as core features.[13][14] Collier et al. reported that all patients in their series had developmental delay and neurological impairment, with symptoms appearing in early childhood and persisting throughout life.[3] 

Age of onset is typically **congenital or early pediatric**, with delayed motor milestones, hypotonia, and developmental delays evident in the first year or two of life.[1][3][7][13] The disease does not resemble adult‑onset degenerative ataxias; instead, it conforms to a neurodevelopmental ataxia phenotype with static or slowly progressive features superimposed on anomalous brain development. Using Human Phenotype Ontology (HPO) terms, core age‑related features include *Global developmental delay* (HP:0001263), *Developmental delay, motor* (HP:0001270), and *Childhood onset* (HP:0011463), although precise age ranges are variably reported.

Symptom severity is **variable**, ranging from mild intellectual disability with ambulatory ataxia and tremor to severe spastic paraplegia with inability to walk, seizures, and significant musculoskeletal and endocrine complications.[1][3][7][13] Collier et al. noted that patients with undetectable ATG7 protein and near‑complete loss of autophagic flux could survive into adulthood with mild–moderate neurological impairments, whereas one patient died in childhood, indicating heterogeneity in severity even among those with severe molecular defects.[3][7] Symptom progression is often **progressive but relatively slow**, with motor deterioration, increased spasticity, and cumulative musculoskeletal and endocrine effects over time, superimposed on early developmental deficits that may be relatively static once established.[3][7][13] 

### 3.2. Neurological and motor phenotypes

Neurological and motor manifestations constitute the **central phenotype** of SCAR31. Patients typically exhibit an **ataxic gait**, reflecting cerebellar dysfunction, with unsteady walking, wide‑based stance, and difficulty with coordination of limb movements.[1][3][7][13] HPO terms capturing this include *Gait ataxia* (HP:0002141) and *Cerebellar ataxia* (HP:0001251). Tremor is commonly present, often described as action or postural tremor affecting the upper limbs, contributing to impaired fine motor skills and tremulous movements during intentional tasks.[1][3][7][13] Dysarthria, or slurred and scanning speech, emerges from cerebellar involvement and motor planning deficits, limiting verbal communication and contributing to social and functional impairment; this can be represented by HPO term *Dysarthria* (HP:0001260).[1][3][7][13]

More severe cases display **spasticity**, particularly in the lower limbs, with increased muscle tone, hyperreflexia, and clonus, resulting in **spastic paraplegia** that can render patients wheelchair‑bound.[1][3][7][13] OMIM notes that more severely affected patients have spasticity with inability to walk, and Collier’s series included individuals who were wheelchair dependent due to spastic paraplegia.[1][3][7] HPO terms such as *Spastic paraplegia* (HP:0001257) and *Inability to walk* (HP:0002540) are appropriate. Seizures occur in some patients, especially in the more severe end of the spectrum, although they are not universal; this can be represented by *Seizures* (HP:0001250).[7][13] Behavioral abnormalities, including hyperactivity, attention deficits, or autistic features, are mentioned in the Collier review, indicating broader neuropsychiatric involvement.[7]

Neuroimaging reveals **cerebellar hypoplasia** and a **thin posterior corpus callosum** in all assessed patients, consistent with a structural substrate for the ataxia and interhemispheric communication deficits.[3][7][13] Enlarged ventricles or ventriculomegaly may also be present, suggesting global brain volume reduction or developmental anomalies.[13] HPO terms *Cerebellar hypoplasia* (HP:0001321), *Thin corpus callosum* (HP:0002079), and *Ventriculomegaly* (HP:0002119) appropriately capture these findings. The selective vulnerability of cerebellum and posterior corpus callosum to ATG7 deficiency is highlighted by Collier and Collier’s review, which note that these regions are consistently affected on MRI.[3][7] The motor phenotype reflects dysfunction of cerebellar Purkinje cells, cerebellar pathways, and corticospinal tracts.

Quality of life impact of these neurological features is profound. Ataxia, tremor, and dysarthria impair mobility, communication, and independence in daily activities, often necessitating assistive devices, caregiver support, and specialized education and therapies. Spastic paraplegia and inability to walk greatly limit autonomy and increase risk for secondary complications such as contractures and pain. Cognitive and behavioral impairments further restrict educational attainment and social participation. Standardized quality of life instruments such as EQ‑5D or SF‑36 have not been systematically applied in SCAR31 cohorts, but extrapolating from other hereditary ataxias suggests substantial impairment across domains of physical functioning, role participation, and emotional well‑being.

### 3.3. Developmental, cognitive, and language phenotypes

Global developmental delay and intellectual disability are **signature features** of SCAR31.[1][3][7][13][14] OMIM and Malacards state that SCAR31 is characterized by **“global developmental delay with hypotonia and variably impaired intellectual and language development,”** clarifying that both motor and cognitive domains are affected.[1][13] Collier et al. reported that patients had developmental delay, with delayed acquisition of motor milestones such as sitting and walking, and variable degrees of cognitive impairment ranging from mild to severe intellectual disability.[3] HPO terms *Global developmental delay* (HP:0001263), *Intellectual disability* (HP:0001249), and *Speech delay* or *Impaired language development* (HP:0000750) are appropriate.

Hypotonia, particularly axial hypotonia, is noted in infancy and early childhood, manifesting as poor head control, “floppiness,” and delays in motor progression.[1][3][13][14] HPO term *Hypotonia* (HP:0001252) captures this. Hypotonia contributes to delayed motor milestones and interacts with cerebellar dysfunction to produce a complex movement disorder. Language development is often delayed, with late onset of first words, limited vocabulary, and dysarthric speech quality, further impairing communication. Some patients may have receptive language relatively better preserved than expressive, though data are limited.

These developmental phenotypes have substantial quality of life impact, affecting educational trajectories, employment prospects, and independence in adulthood. Early recognition of developmental delay and comprehensive neuropsychological evaluation can guide interventions such as special education, speech therapy, and occupational therapy, which are important tertiary preventive measures. Knowledge bases should represent these phenotypes with explicit HPO terms and note that severity is variable, with some patients achieving limited independence while others remain fully dependent on caregivers.

### 3.4. Musculoskeletal, neuromuscular, and endocrine phenotypes

SCAR31 includes **neuromuscular abnormalities**, with loss of muscle mass and strength, myopathic changes, and sometimes musculoskeletal deformities.[3][7][13] Collier’s cohort showed that patients had decreased muscle mass and strength, and skeletal muscle biopsy from a patient with undetectable ATG7 protein revealed myopathic changes, including subsarcolemmal accumulation of p62 and evidence of inflammation.[7] HPO terms such as *Muscle weakness* (HP:0001324), *Muscle atrophy* (HP:0003202), and *Myopathy* (HP:0003198) are relevant. Limb tremors and abnormal limb grasping behavior, reminiscent of the tremors and limb grasping phenotypes seen in Atg7 knockout mouse models, further indicate neuromuscular involvement.[9][7]

Endocrine dysfunction is reported in some SCAR31 patients. Collier’s review mentions evidence of endocrine abnormalities, including growth disturbances, pubertal anomalies, or hormone imbalances, although details vary.[7] OMIM and Malacards note “possibly endocrine dysfunction” as an additional feature, indicating that endocrine manifestations are not universal but present in a subset.[1][13] HPO terms might include *Endocrine abnormality* (HP:0000819) and more specific terms once detailed phenotypes are better documented. These endocrine issues may reflect ATG7’s role in autophagy within endocrine tissues and the general importance of autophagy in hormone secretion and cellular homeostasis.

Quality of life impact of neuromuscular and endocrine phenotypes is significant, contributing to fatigue, reduced exercise tolerance, endocrine symptoms such as delayed puberty or metabolic disturbances, and increased medical care needs. Musculoskeletal weakness compounds motor disability from ataxia and spasticity, limiting mobility and increasing risk for falls and fractures. Inflammation and myopathy may cause pain and discomfort. Knowledge bases should capture these phenotypes even though precise frequencies are not yet quantified, indicating them as **additional features**.

### 3.5. Ocular, auditory, and other systemic phenotypes

Ocular dysfunction is a prominent non‑neurological feature of SCAR31. Collier’s review notes that **ocular dysfunction, predominantly optic atrophy**, is commonly displayed by patients.[7] OMIM and Malacards list **optic atrophy** and **retinitis pigmentosa** among additional features, along with **sensorineural deafness**, indicating that both visual and auditory systems can be affected.[1][13] HPO terms such as *Optic atrophy* (HP:0000648), *Retinitis pigmentosa* (HP:0000651), and *Sensorineural hearing impairment* (HP:0000407) are appropriate. Optic atrophy manifests as progressive visual impairment due to degeneration of retinal ganglion cell axons and optic nerve, whereas retinitis pigmentosa involves photoreceptor degeneration and visual field constriction. Sensorineural deafness contributes to communication challenges and may necessitate hearing aids or cochlear implants.

Facial dysmorphism is noted in the Collier series and review, with patients exhibiting subtle to moderate alterations in facial features, which may include broad forehead, flat midface, or other characteristics, although precise patterns are not standardized.[3][7] HPO term *Facial dysmorphism* (HP:0001999) captures this. Behavioral abnormalities and possible endocrine dysfunction have been mentioned, as well as occasional systemic inflammation or organ dysfunction, although these are less well characterized.[7][13]

The presence of multi‑system features underscores SCAR31 as a systemic disorder of autophagy rather than a purely neurological disease. Quality of life impacts include visual and hearing impairment affecting education and social participation, facial dysmorphism contributing to psychosocial challenges, and systemic issues increasing medical complexity. Knowledge bases should annotate these phenotypes as variable or “occasional” features, with explicit mention that frequencies are not yet rigorously quantified in published cohorts.

## 4. Genetic and Molecular Information

### 4.1. Causal gene: ATG7 and its canonical function

The sole established causal gene for SCAR31 is **ATG7 (Autophagy Related 7)**, approved by HGNC and catalogued in OMIM as **608760**.[5][13][14] ATG7 maps to chromosome 3p25.3, with genomic coordinates 3:11,272,397–11,576,353 (GRCh38).[5] OMIM describes ATG7 as **“a ubiquitin‑activating enzyme E1‑like protein essential for the Apg12 conjugation system that mediates membrane fusion in autophagy,”** referencing studies by Tanida et al. that defined ATG7’s role in autophagy.[5] UniProt adds that ATG7 is an E1‑like activating enzyme involved in two ubiquitin‑like systems required for cytoplasm‑to‑vacuole transport (Cvt) and autophagy.[15] 

ATG7 catalyzes ATP‑dependent activation of ATG12 and LC3 (ATG8 family proteins) via formation of thioester intermediates, enabling subsequent transfer to E2‑like enzymes (ATG10 for ATG12 and ATG3 for LC3) and ultimate conjugation to their targets (ATG12 to ATG5 and LC3 to phosphatidylethanolamine, respectively).[5][7][15] These conjugation cascades are central to autophagosome biogenesis, elongation, and cargo sequestration, and ATG7 has no known functional paralogue, making it a **non‑redundant core autophagy protein**.[3][7] Deletion of Atg7 in yeast, mouse, and human cells severely impairs autophagy, as evidenced by reduced LC3‑II accumulation and decreased cargo sequestration, establishing ATG7 as indispensable to classical degradative autophagy.[7][15]

Komatsu et al. demonstrated that loss of Atg7 in mice leads to neurodegeneration, highlighting ATG7’s essential role in maintaining axonal homeostasis and preventing axonal degeneration.[1][5][7] Tissue‑specific Atg7 ablation in nerve and muscle results in ataxia and myopathy, respectively, recapitulating key features observed in human SCAR31 patients.[3][7][9] These model organism data provided critical mechanistic background that guided the search for human ATG7 deficiency as a cause of neurodevelopmental disorders.

### 4.2. Pathogenic variants: types, classification, and functional consequences

SCAR31 is caused by **germline, biallelic deleterious variants in ATG7**, encompassing nonsense, splice‑site, and missense changes that disrupt protein expression, folding, dimerization, or enzymatic activity.[1][3][7][13] In the Collier cohort, there were one nonsense, two splice site, and six missense mutations among eleven patients.[1][3] Missense variants affected highly conserved residues, such as p.Arg576His, p.His624Tyr, p.Pro234Thr, and p.Val588Met, suggesting disruption of critical functional domains.[3] Nonsense and splice‑site variants likely cause truncated or absent protein via nonsense‑mediated decay or aberrant splicing, although one family with biallelic complete loss‑of‑function mutations still had residual basal autophagy in some tissues, implying complex compensatory mechanisms.[3][7]

ClinVar and Malacards list specific pathogenic ATG7 variants associated with SCAR31, including NM_001349232.2(ATG7):c.339G>A (p.Trp113Ter), a nonsense variant classified as pathogenic.[13] The variant classification in ClinVar follows ACMG/AMP guidelines, integrating criteria such as null variant in a gene where loss of function is a known mechanism of disease (PVS1), segregation in affected individuals, absence or rarity in population databases, and functional studies showing loss of autophagic activity.[3][13] Most reported ATG7 variants causing SCAR31 are classified as **pathogenic** or **likely pathogenic**, with strong evidence from biochemical assays demonstrating impaired ATG7 function, diminished LC3‑II formation, and reduced long‑lived protein degradation.[3][7]

Collier et al. performed detailed functional analyses of patient fibroblasts and skeletal muscle, finding severely diminished ATG7 protein levels, impaired ATG7 folding and dimerization, accumulation of p62 in puncta, decreased LC3 processing, and markedly reduced autophagic sequestration.[1][3][7] They wrote that **“biochemical profiling of patient fibroblasts revealed severely diminished ATG7 protein levels … impairments in autophagic flux, evidenced by both diminished LC3‑II accumulation and decreased cargo sequestration activity,”** and that expression of wild‑type ATG7 rescued these defects in at least one patient’s cells.[1][3][7] These findings demonstrate that SCAR31 variants confer **loss‑of‑function** in ATG7, rendering cells **autophagy deficient**. There is no evidence for gain‑of‑function, dominant‑negative, or toxic aggregation mechanisms; disease arises from insufficient autophagic capacity.

Regarding allele frequency, disease‑causing ATG7 variants are **extremely rare** in population databases such as gnomAD, consistent with strong negative selection against disruptive variants in this essential gene.[7][11] Many SCAR31 variants are absent from gnomAD or present at very low heterozygous carrier frequencies, reinforcing their pathogenicity.[3][13] The LOEUF metric identifies ATG7 as LoF‑constrained, with observed LoF variants far fewer than expected given mutation rates and gene length.[11][7] These data support the conclusion that **biallelic ATG7 LoF is highly deleterious**, manifesting clinically only in rare familial clusters.

All SCAR31 variants described to date are **germline**, present in all cells of the affected individuals, and segregate in families according to autosomal recessive inheritance.[1][3][13] There is no evidence for somatic ATG7 mutations causing SCAR31 or for mosaicism altering disease risk, although germline mosaicism in unaffected parents cannot be entirely excluded in individual cases. Knowledge bases should therefore categorize SCAR31 as a **germline, autosomal recessive, loss‑of‑function ATG7 disorder**, with variant types including missense, nonsense, and splice‑site mutations.

### 4.3. Modifier genes, epigenetic and chromosomal information

At present, **no modifier genes** have been convincingly implicated in altering SCAR31 severity, penetrance, or expressivity. The small number of families and the rarity of the disease limit power to detect such modifiers. However, the observation that patients with biallelic complete loss‑of‑function ATG7 mutations can survive with variable severity suggests that genetic background and environmental factors likely modulate disease phenotype, potentially via variation in autophagy regulators such as mTOR, AMPK, or other autophagy genes, but formal evidence is lacking.[3][7] 

Epigenetic regulation of ATG7 has been documented in other contexts, with DNA methylation, histone modifications, and microRNAs influencing autophagy gene expression, but no SCAR31‑specific epigenetic abnormalities have been reported.[7] It is plausible that epigenetic mechanisms might affect residual ATG7 expression or compensate via up‑regulation of other autophagy pathways, but this remains speculative. For disease knowledge bases, epigenetic information for SCAR31 should be noted as **not yet characterized**, while cross‑referencing general autophagy epigenetics for mechanistic context.

Chromosomal abnormalities such as aneuploidy, translocations, or large deletions involving ATG7 have not been reported as causes of SCAR31.[1][3][5][13] The disease is currently attributed to point mutations and small indels at the sequence level, with no evidence of structural variants or copy number changes as primary etiologic factors. Clinical exome and genome sequencing in SCAR31 families did not identify other pathogenic structural alterations, further supporting the point mutation mechanism.[3] DECIPHER or dbVar could be consulted for large structural variants involving 3p25, but in the absence of documented cases, chromosomal abnormalities should be regarded as **not established** contributors to SCAR31.

## 5. Environmental Information

### 5.1. Non‑genetic contributing factors

As a **monogenic congenital disorder** caused by biallelic ATG7 variants, SCAR31 is primarily determined by genetic factors present from conception.[1][3][7][13] Non‑genetic contributing factors such as toxins, radiation, pollution, occupational exposure, or diet are not documented as primary causes. Autophagy is responsive to environmental stressors, and ATG7 deficiency likely alters cellular responses to such stress, but no specific exposure has been shown to trigger or significantly worsen SCAR31.

Comparative Toxicogenomics Database (CTD) resources linking ATG7 to environmental chemicals may reveal interactions between ATG7 expression and toxins in experimental settings, but these have not been translated into SCAR31 clinical evidence. Similarly, lifestyle factors like smoking, alcohol consumption, or exercise might modulate general health or comorbidities in SCAR31 patients, but their impact on core neurological phenotypes is unknown. Knowledge bases should therefore mark environmental factors for SCAR31 as **unknown or not established**, while noting the potential for future discoveries given autophagy’s sensitivity to environmental cues.

### 5.2. Infectious agents and secondary triggers

There is no indication that SCAR31 is caused or triggered by infectious agents. Infections may exacerbate neurological symptoms or unmask latent deficits in any neurodevelopmental disorder, but SCAR31 is not classified as an infection‑related ataxia. ATG7’s role in autophagy implicates it in host defense and pathogen clearance, and ATG7 deficiency in other contexts can influence susceptibility to infections, but no SCAR31 patient series has highlighted unusual infectious susceptibility as a defining feature.[7] Knowledge bases should therefore treat infectious agents as **not applicable** to primary SCAR31 etiology, though they may be relevant to general health management.

## 6. Mechanism and Pathophysiology

### 6.1. Molecular pathways: autophagy and related signaling

The central mechanistic pathway in SCAR31 is **macroautophagy**, the evolutionarily conserved process by which cells degrade cytoplasmic components in lysosomes to maintain homeostasis.[3][5][7][15] ATG7 functions as an E1‑like activating enzyme in two **ubiquitin‑like conjugation cascades**: the ATG12–ATG5 system and the LC3 (ATG8) lipidation system.[5][7][15] These cascades are integrated into broader autophagy signaling networks that include mTOR (mechanistic target of rapamycin), AMPK (AMP‑activated protein kinase), ULK1 complex, and PI3K class III complexes.[7]

In canonical autophagy, nutrient deprivation or stress inhibits mTOR and activates ULK1, initiating autophagosome formation. PI3K class III generates PI3P at autophagy initiation sites, recruiting ATG proteins, including the ATG12–ATG5–ATG16L1 complex and LC3. ATG7 activates ATG12 and LC3, enabling ATG12 transfer to ATG5 and LC3 conjugation to phosphatidylethanolamine (PE), yielding LC3‑II, which associates with autophagosomal membranes.[5][7][15] LC3‑II is required for autophagosome elongation and cargo recruitment via adaptors like p62, which bind ubiquitinated cargo and LC3 simultaneously.[7] Autophagosomes then fuse with lysosomes, forming autolysosomes where cargo is degraded. GO terms capturing these processes include *Autophagy* (GO:0006914), *Macroautophagy* (GO:0016236), *Protein ubiquitination* (GO:0016567), and *Cytoplasm to vacuole transport* (GO:0006623).

ATG7 deficiency disrupts these cascades at a fundamental level. Without functional ATG7, ATG12 cannot be efficiently activated and conjugated to ATG5, and LC3 cannot be properly lipidated, leading to **severe impairment of autophagosome formation and cargo sequestration**.[3][7][15] Collier et al. documented diminished LC3 processing, reduced LC3‑II accumulation, and decreased cargo sequestration activity in patient fibroblasts, hallmark features of impaired autophagic flux.[3][7] The accumulation of p62 in puncta further indicates that cargo destined for autophagic degradation is not properly cleared, resulting in **protein and organelle aggregation**.[1][3][7] Thus, SCAR31 can be conceptualized as a **congenital disorder of autophagy** caused by disruption of ATG7‑dependent ubiquitin‑like conjugation pathways.

Upstream, signaling pathways such as mTOR and AMPK may still respond to nutrient and stress cues, but downstream execution via ATG7‑dependent conjugation is compromised. This decoupling of autophagy initiation from execution may lead to chronic stress, activation of alternative degradation pathways (e.g., proteasome), and maladaptive signaling responses. Downstream consequences include oxidative stress, mitochondrial dysfunction, and activation of cell death pathways, all of which contribute to tissue damage and neurodegeneration.[7][16]

### 6.2. Cellular processes: axonal homeostasis, neurodevelopment, and metabolic homeostasis

At the cellular level, ATG7 and autophagy are critical for **axonal homeostasis**, **neurodevelopment**, and **metabolic homeostasis**, processes that are severely perturbed in SCAR31.[3][5][7][9][16] Komatsu et al. demonstrated in mice that loss of Atg7 in neurons leads to axonal degeneration, accumulation of abnormal organelles, and neurodegeneration, highlighting autophagy’s role in maintaining axonal integrity.[1][5][7][9] Their work established that Atg7 is essential for preventing axonal degeneration in long‑projection neurons, particularly in cerebellar and cortical circuits.[5][7][9] GO terms such as *Axon maintenance* (GO:0007411) and *Neuronal homeostasis* (GO:0070482) capture these processes.

In human SCAR31 patients, cerebellar hypoplasia and corpus callosum thinning suggest that ATG7 deficiency affects **brain development**, not only maintenance. Autophagy plays roles in neuronal differentiation, synaptic pruning, and removal of developmental debris, and ATG7 deficiency may impair these functions, leading to structural abnormalities and miswiring.[3][7] The resulting cerebellar and callosal anomalies create a substrate for ataxia and cognitive deficits. GO terms such as *Nervous system development* (GO:0007399), *Cerebellar development* (GO:0021549), and *Corpus callosum development* (GO:0021543) are relevant.

Metabolic homeostasis, particularly in long‑lived cells and stem cells, is another key process impacted by ATG7 deficiency. Clarke et al. showed that B1a B cells require autophagy for metabolic homeostasis and self‑renewal, and that deletion of Atg7 leads to accumulation of dysfunctional mitochondria, metabolic gene down‑regulation, and selective loss of B1a cells due to failure of self‑renewal.[16] They reported that **“autophagy is differentially activated in B1a B cells, and deletion of the autophagy gene Atg7 leads to a selective loss of B1a B cells caused by a failure of self‑renewal,”** and that autophagy‑deficient B1a cells accumulate lipid droplets and dysfunctional mitochondria, highlighting autophagy’s role in lipophagy and mitophagy.[16] Although SCAR31 is primarily a neurological disorder, these findings underscore systemic roles of ATG7 in hematopoietic and immune cells, which may contribute to subtle immunological or metabolic phenotypes in patients.

Muscle tissue also depends on autophagy for turnover of sarcomeric proteins and maintenance of contractile function. Tissue‑specific Atg7 knockout in muscle leads to myopathy in mice, and muscle biopsy in SCAR31 patients shows myopathic changes and inflammation.[3][7][9] Autophagy deficiency in muscle likely contributes to muscle weakness, atrophy, and fatigue. GO terms such as *Muscle cell homeostasis* (GO:0048872) and *Autophagy of mitochondrion* (GO:0000422) describe these processes.

### 6.3. Protein dysfunction: ATG7 misfolding, dimerization defects, and enzyme loss

At the protein level, SCAR31 variants cause **ATG7 dysfunction** through mechanisms including truncated protein production, misfolding, defective dimerization, and reduced enzymatic activity.[1][3][5][7][15] ATG7 functions as a dimer and has domains required for ATP binding, cysteine‑based catalytic activity, and interaction with ATG12 and LC3.[15] Missense variants that alter conserved residues can disrupt folding or stability, leading to reduced protein levels and impaired function, while nonsense and splice‑site variants may produce truncated protein or trigger nonsense‑mediated decay, resulting in **complete loss of ATG7 protein**.[1][3][7][15]

OMIM notes that patient cells show **“decreased levels of ATG7 protein associated with defective protein folding and dimerization,”** implying that missense variants compromise structural integrity.[1] Collier et al. observed that ATG7 protein was severely diminished or undetectable in patient fibroblasts and skeletal muscle, and that autophagic flux was correspondingly reduced.[3][7] Expression of wild‑type ATG7 rescued autophagic defects in one patient’s cells, demonstrating that the disease arises from ATG7 deficiency rather than downstream pathway abnormalities.[1][3][7]

UniProt describes ATG7’s domain architecture and function, including its adenylation domain, catalytic cysteine, and interfaces for binding ATG10 and ATG3.[15] Variants affecting these regions likely impair E1‑like activity, preventing activation and transfer of ATG12 and LC3, and thereby blocking downstream conjugation cascades. Structural modeling and functional assays in Collier’s study and related work show that specific missense variants reduce enzymatic activity, confirming **loss‑of‑function** as the primary molecular consequence.[3][7]

### 6.4. Metabolic changes, immune system involvement, and tissue damage

ATG7 deficiency leads to **metabolic changes** at the cellular and tissue levels, particularly in long‑lived cells such as neurons, muscle fibers, and B1a B cells. Autophagy regulates energy metabolism by recycling macromolecules, clearing damaged mitochondria, and managing lipid stores via lipophagy.[7][16] In B1a B cells, loss of Atg7 causes accumulation of active mitochondria and intracellular lipid droplets, down‑regulation of fatty acid synthesis genes, and impaired fatty acid uptake, resulting in metabolic dysfunction and failure of self‑renewal.[16] Clarke et al. interpreted these findings as evidence that **“B1 B cells depend, unlike Fo B2 B cells, on autophagy to survive and self‑renew, and loss of autophagy causes global metabolic dysfunction and failure of lipid and mitochondrial homeostasis.”**[16] These principles likely extend to other cell types in SCAR31, where impaired autophagy leads to mitochondrial dysfunction, oxidative stress, and metabolic stress.

Immune system involvement in SCAR31 is suggested by ATG7’s role in hematopoietic stem cell maintenance and B cell function. Komatsu and colleagues reported that the autophagy protein Atg7 is essential for hematopoietic stem cell maintenance, and Atg7‑deficient mice showed decreased B cell, T cell, and NK cell numbers.[9][16][7] Collier’s review notes that patient skeletal muscle biopsy showed inflammation, and that Atg7 deficiency in immune cells can alter immune homeostasis.[7] However, overt immunodeficiency is not reported as a core SCAR31 phenotype; immune involvement may be subtle and manifest as increased susceptibility to infection or altered inflammatory responses in individual patients.

Tissue damage mechanisms in SCAR31 involve **accumulation of damaged organelles and protein aggregates**, leading to oxidative stress, activation of apoptotic pathways, and eventual cell death. Komatsu’s Atg7 knockout mice exhibit absent cerebral cortex pyramidal cells, absent hippocampus pyramidal cells, increased neuron apoptosis, axon degeneration, and tremors, reflecting widespread neuronal loss and degeneration.[9] Mammalian phenotype ontology annotations for Atg7‑deficient mice include abnormal nervous system physiology, axon degeneration, increased neuron apoptosis, tremors, limb grasping, and weight loss.[9] These findings parallel the neurological phenotypes in human SCAR31 and illustrate tissue damage mechanisms such as oxidative stress, mitochondrial dysfunction, and apoptosis. GO terms such as *Neuronal apoptosis* (GO:0051402), *Axon degeneration* (GO:0030425), and *Response to oxidative stress* (GO:0006979) describe these processes.

Biochemically, SCAR31 involves **enzyme deficiency**—namely, ATG7 deficiency—as the core molecular defect. While ATG7 is not a classical metabolic enzyme, its E1‑like activity is essential for autophagy. Loss of ATG7 leads to enzyme deficiency in the autophagy conjugation systems, analogous to enzyme deficiencies in lysosomal storage diseases, and results in accumulation of undegraded substrates such as p62 and ubiquitinated proteins.[1][3][7] Knowledge bases can represent ATG7 deficiency as an enzyme deficiency with GO term *Ubiquitin‑like protein ligase activity* (GO:0061578) impaired.

### 6.5. Molecular profiling and advanced technologies

Collier et al. performed **biochemical profiling** of patient fibroblasts and skeletal muscle, measuring ATG7 protein levels, LC3 processing, p62 distribution, and long‑lived protein degradation.[3][7] They reported that patient fibroblasts exhibited severely diminished ATG7 protein, impaired LC3‑II accumulation, decreased cargo sequestration, and reduced long‑lived protein degradation, evidencing near absence of autophagic flux.[3][7] These assays constitute a form of **proteomics** and functional molecular profiling but are targeted rather than high‑throughput. There is no published transcriptomic, metabolomic, or lipidomic profiling specifically for SCAR31 patients, although broader studies of ATG7 deficiency in model organisms and other diseases provide insight into gene expression and metabolic changes associated with ATG7 impairment.[7][16]

Single‑cell analysis, spatial transcriptomics, and multi‑omics integration have not yet been applied to SCAR31, largely because of the small patient cohorts and the rarity of the disease. However, advanced models such as Atg7 knockout mice, conditional tissue‑specific Atg7 knockouts, and induced pluripotent stem cell (iPSC) models could be leveraged to perform multi‑omics analyses that illuminate cell‑type specific mechanisms and heterogeneity. Functional genomics screens using CRISPR or RNAi have identified autophagy genes, including ATG7, as essential in various contexts, but these screens have not been directly tied to SCAR31.

For disease knowledge bases, molecular profiling data should focus on **functional assays** that demonstrate impaired autophagy in patient cells, including LC3 processing, p62 accumulation, and long‑lived protein degradation, with clear attribution to ATG7 deficiency.[1][3][7] Advanced omics data may be incorporated as general ATG7 biology rather than SCAR31‑specific findings.

### 6.6. Causal chain from ATG7 deficiency to clinical manifestations

The **causal chain** from ATG7 deficiency to SCAR31 clinical manifestations can be summarized as follows. Germline biallelic loss‑of‑function variants in ATG7 result in severely diminished or absent ATG7 protein, abolishing its E1‑like activity in autophagy conjugation pathways.[1][3][5][7][15] This leads to failure of ATG12 activation and conjugation to ATG5, and failure of LC3 activation and lipidation, thereby impairing autophagosome formation and cargo sequestration.[3][7][15] Autophagic flux is markedly reduced, as evidenced by diminished LC3‑II accumulation, decreased long‑lived protein degradation, and accumulation of p62 in puncta.[1][3][7] Cells become unable to efficiently clear damaged organelles, aggregated proteins, and metabolic waste, leading to chronic cellular stress.

In neurons, particularly cerebellar Purkinje cells and cortical pyramidal neurons, impaired autophagy causes accumulation of dysfunctional mitochondria, axonal swellings, and neurodegeneration, as shown in Atg7‑deficient mice.[5][7][9] During development, autophagy deficiency disrupts neuronal differentiation, synaptic pruning, and brain morphogenesis, resulting in cerebellar hypoplasia and corpus callosum thinning in human patients.[3][7] These structural abnormalities and axonal dysfunction manifest clinically as ataxia, tremor, dysarthria, spasticity, and developmental delay.[1][3][7][13]

In muscle, ATG7 deficiency leads to myopathic changes, subsarcolemmal accumulation of p62, inflammation, and loss of muscle mass and strength, contributing to fatigue, weakness, and musculoskeletal limitations.[3][7] In endocrine tissues, autophagy impairment may disrupt hormone production and secretion, leading to endocrine dysfunction in some patients.[7][13] In hematopoietic and immune cells, ATG7 deficiency affects stem cell maintenance and B1a B cell metabolism, potentially altering immune responses and contributing to subtle immunological phenotypes.[7][9][16] Ocular and auditory systems, which rely on autophagy for photoreceptor and hair cell maintenance, exhibit optic atrophy, retinitis pigmentosa, and sensorineural deafness in some SCAR31 patients, paralleling Atg7‑deficient mouse models showing outer hair cell loss and deafness.[7]

Downstream of cellular dysfunction, tissue‑level damage accumulates, leading to cerebellar and cortical atrophy, muscle wasting, endocrine organ dysfunction, and multi‑system impairments. Clinically, this cascade manifests as the full SCAR31 phenotype: global developmental delay, hypotonia, intellectual disability, ataxia, tremor, dysarthria, spastic paraplegia, seizures, musculoskeletal weakness, optic atrophy, hearing loss, endocrine abnormalities, and facial dysmorphism.[1][3][7][13] The upstream mechanism is ATG7 deficiency and autophagy failure; downstream consequences encompass neurodevelopmental disruption, neurodegeneration, myopathy, endocrine dysfunction, and systemic metabolic imbalance.

Cell types involved include cerebellar Purkinje neurons (CL:0000127), cerebral cortical pyramidal neurons (CL:0002604), skeletal muscle fibers (CL:0000746), retinal ganglion cells (CL:0000740), photoreceptor cells (CL:0000210), inner ear hair cells (CL:0000208), B1a B cells (CL:0000842), hematopoietic stem cells (CL:0000034), and endocrine gland cells such as pituitary and pancreatic endocrine cells (CL:0000163). Biological processes include autophagy (GO:0006914), axon maintenance (GO:0007411), nervous system development (GO:0007399), muscle cell homeostasis (GO:0048872), endocrine system development (GO:0035270), and immune system process (GO:0002376). These ontology terms should be linked to SCAR31 in knowledge bases to capture mechanistic detail.

## 7. Anatomical Structures Affected

### 7.1. Organ‑level involvement

SCAR31 primarily affects the **central nervous system**, especially the cerebellum and corpus callosum, but also involves skeletal muscle, ocular and auditory organs, and endocrine glands.[1][3][7][13] Brain MRI findings consistently show **cerebellar hypoplasia**, especially in the vermis and hemispheres, and a **thin posterior corpus callosum**, reflecting abnormal development of these structures.[3][7][13] Enlarged ventricles or ventriculomegaly suggest reduced brain tissue volume or developmental anomalies.[13] UBERON terms for these structures include *Cerebellum* (UBERON:0002037), *Corpus callosum* (UBERON:0002312), and *Cerebral ventricle* (UBERON:0001944). The cerebellar ataxia and motor deficits arise from cerebellar dysfunction and impaired connectivity via the corpus callosum and corticospinal tracts.

Skeletal muscle is involved, showing myopathic changes and reduced mass and strength, likely due to autophagy deficiency in muscle fibers.[3][7] This affects the musculoskeletal system (UBERON:0002385) and contributes to motor disability. The ocular system is affected through optic nerve and retina involvement, with optic atrophy and retinitis pigmentosa, implicating the eye (UBERON:0000970), optic nerve (UBERON:0001023), and retina (UBERON:0000966).[7][13] The auditory system may be affected via sensorineural hearing loss, involving the cochlea (UBERON:0001844) and hair cells (UBERON:0001845), paralleling Atg7‑deficient mouse models with outer hair cell loss and deafness.[7]

Endocrine glands, such as the pituitary, thyroid, and gonads, may be involved in endocrine dysfunction reported in some patients, though specific glands are not consistently identified.[7][13] UBERON terms such as *Pituitary gland* (UBERON:0000007), *Thyroid gland* (UBERON:0002046), and *Gonad* (UBERON:0000997) may be relevant. The hematopoietic system and immune organs, including bone marrow (UBERON:0001474), spleen (UBERON:0002106), and lymph nodes (UBERON:0000029), are implicated in Atg7‑deficient mouse models but less clearly in SCAR31 clinical descriptions.[9][16][7]

### 7.2. Tissue and cell‑level involvement

At the tissue level, SCAR31 involves **nervous tissue**, **muscle tissue**, **retinal and auditory sensory epithelia**, and **endocrine and hematopoietic tissues**.[3][7][9][16] Nervous tissue includes cerebellar cortex, cerebral cortex, corpus callosum white matter, brainstem, and spinal cord, with Purkinje cells, granule cells, pyramidal neurons, oligodendrocytes, and astrocytes all potentially impacted by autophagy deficiency.[5][7][9] Cell Ontology terms for these cell types include *Purkinje neuron* (CL:0000127), *Cerebellar granule neuron* (CL:0000128), *Cerebral cortical pyramidal neuron* (CL:0002604), *Oligodendrocyte* (CL:0002453), and *Astrocyte* (CL:0000127).

Muscle tissue comprises skeletal muscle fibers with satellite cells and neuromuscular junctions, and autophagy deficiency in these cells leads to myopathy.[3][7][9] CL terms such as *Skeletal muscle cell* (CL:0000746) and *Satellite cell* (CL:0000175) are relevant. Retinal tissue includes photoreceptor cells, retinal ganglion cells, and pigmented epithelium, with autophagy playing important roles in photoreceptor maintenance and retinal health.[7] CL terms include *Photoreceptor cell* (CL:0000210) and *Retinal ganglion cell* (CL:0000740). Auditory epithelia include inner ear hair cells (CL:0000208), and Atg7 deficiency in mice causes electromotility disturbances and outer hair cell loss.[7]

Endocrine tissues include hormone‑producing cells in the pituitary, thyroid, adrenal glands, and gonads, and ATG7 deficiency may affect hormone secretion and endocrine rhythms.[7][13] CL terms such as *Endocrine cell* (CL:0000163) capture these. Hematopoietic tissues involve hematopoietic stem cells (CL:0000034), common lymphoid progenitors (CL:0000815), and B1a B cells (CL:0000842), all of which require autophagy for maintenance and function, as shown in Atg7‑deficient mice and B1a B cell studies.[9][16][7]

### 7.3. Subcellular compartments and localization

Subcellular compartments involved in SCAR31 pathophysiology include the **autophagosome**, **lysosome**, **mitochondria**, **endoplasmic reticulum**, and **cytoplasm**, where autophagy operates.[3][5][7][15][16] Gene Ontology Cellular Component terms relevant here are *Autophagosome* (GO:0005776), *Lysosome* (GO:0005764), *Mitochondrion* (GO:0005739), *Endoplasmic reticulum* (GO:0005783), and *Cytoplasm* (GO:0005737). ATG7 is localized primarily in the cytoplasm, where it interacts with ATG12, ATG10, ATG5, LC3, and ATG3 to form conjugation complexes.[15]

In ATG7‑deficient cells, autophagosomes are reduced or malformed, and cargo adaptors like p62/SQSTM1 accumulate as puncta, indicating stalled autophagy.[1][3][7] Mitochondria accumulate damage and may show altered morphology and function, contributing to oxidative stress and metabolic dysfunction.[16] Lipid droplets accumulate due to impaired lipophagy, altering cellular lipid homeostasis.[16] In neurons, axonal compartments show organelle accumulation and swelling due to impaired axonal autophagy.[5][7][9] These subcellular alterations underlie tissue‑level dysfunction and clinical phenotypes.

Localization of brain abnormalities is **bilateral and symmetric**, with cerebellar hypoplasia and corpus callosum thinning affecting both hemispheres, though severity may vary regionally.[3][7][13] Motor symptoms such as spasticity and ataxia reflect bilateral involvement of descending tracts and cerebellar circuits. Ocular and auditory deficits may be symmetric or asymmetric, but data are limited. Knowledge bases should represent localization as primarily **bilateral central nervous system involvement**, with multi‑organ systemic effects.

## 8. Temporal Development

### 8.1. Onset patterns

SCAR31 onset is typically **congenital or pediatric**, with signs evident in infancy and early childhood.[1][3][7][13][14] Global developmental delay and hypotonia manifest within the first year or two of life, with delayed motor milestones, poor head control, and late walking.[1][3][13] Cognitive and language delays become evident as children fail to acquire age‑appropriate skills, and ataxia, tremor, and dysarthria are observed as motor control demands increase.[1][3][7][13] These patterns correspond to **chronic, insidious onset**, rather than acute or subacute episodes. HPO terms such as *Congenital onset* (HP:0003577) and *Childhood onset* (HP:0011463) are applicable, depending on the precise timing.

### 8.2. Disease progression and course

Disease progression in SCAR31 is **chronic and generally progressive**, but with significant variability across patients.[3][7][13] Developmental deficits, once established, tend to be relatively stable, while motor symptoms such as ataxia, tremor, and spasticity may worsen over time, leading to increased disability and reliance on mobility aids.[3][7][13] Collier’s series included siblings who survived into adulthood with undetectable ATG7 and near absence of autophagic flux, yet with mild–moderate neurological impairments, suggesting that the disease can be **slowly progressive** and compatible with long‑term survival.[7] In more severe cases, patients develop spastic paraplegia and become wheelchair‑bound, and one patient died during childhood, indicating the potential for serious progression and mortality.[7][3]

The disease course can thus be characterized as **chronic, lifelong, and variably progressive**, with no known spontaneous remissions. There is no evidence of an episodic or relapsing‑remitting pattern; rather, deficits accrue or become more disabling over time. Early childhood appears to be a **critical period** during which neurodevelopmental anomalies and brain structural abnormalities emerge; interventions during this window may influence functional outcome, though they cannot correct structural defects.

### 8.3. Critical periods and windows of vulnerability

Autophagy plays critical roles during **neurodevelopment**, including neuronal differentiation, synaptic pruning, and removal of developmental debris.[7] ATG7 deficiency disrupts these processes, particularly during prenatal and early postnatal brain development, leading to cerebellar hypoplasia and corpus callosum thinning.[3][7] The prenatal and early neonatal periods likely constitute **critical windows of vulnerability** during which ATG7 deficiency has maximal impact on brain morphogenesis. After this period, autophagy continues to be important for maintenance, and ATG7 deficiency contributes to progressive neurodegeneration and axonal degeneration, but the foundational structural abnormalities are already established.

Similarly, muscle development and endocrine organ maturation may be particularly sensitive to autophagy during specific developmental windows. In mice, Atg7 deficiency in germ cells leads to primary ovarian insufficiency, demonstrating critical roles in reproductive development.[9] While SCAR31 data on reproductive endocrinology are limited, endocrine dysfunction reported in patients suggests developmental windows of vulnerability in endocrine organs as well.[7][13] Knowledge bases might annotate **prenatal and early childhood periods** as critical windows for SCAR31 pathogenesis.

## 9. Inheritance and Population

### 9.1. Inheritance pattern, penetrance, and expressivity

SCAR31 is unequivocally **autosomal recessive**.[1][3][12][13][14] OMIM and Malacards classify the disease as autosomal recessive spinocerebellar ataxia 31, and Collier’s familial data show transmission patterns consistent with autosomal recessive inheritance, with affected individuals harboring biallelic ATG7 variants and parents being heterozygous carriers.[1][3][12][13] Disease Ontology describes SCAR31 explicitly as an autosomal recessive cerebellar ataxia.[14]

Penetrance for SCAR31 appears to be **high or complete** among individuals with biallelic deleterious ATG7 variants, in the sense that all reported individuals with such variants exhibit some degree of neurodevelopmental and autophagic impairment.[3][7][13] There is no evidence of asymptomatic individuals with biallelic null ATG7 mutations; however, phenotypic severity is variable, and some patients have milder impairments despite severe molecular deficiency.[3][7] Expressivity is thus **variable**, with a spectrum from mild–moderate intellectual disability and ambulatory ataxia to severe spastic paraplegia, seizures, and multi‑system involvement.[1][3][7][13] OMIM notes that there was not a clear genotype–phenotype correlation among the families, indicating that expressivity is influenced by factors beyond the specific variant type.[1] 

Genetic anticipation is **not applicable**, as SCAR31 is not caused by repeat expansions but by point mutations and small indels. Germline mosaicism could theoretically occur, but there is no direct evidence in reported families. Founder effects may exist in specific populations where particular ATG7 variants are more common, but the current literature does not identify specific founder mutations; the Collier cohort included families from diverse backgrounds.[3] Consanguinity likely plays a role in some families, as autosomal recessive disorders are more prevalent in consanguineous populations, but the provided resources do not detail consanguinity status. Carrier frequency of pathogenic ATG7 variants is extremely low in general populations, as indicated by gnomAD and other datasets.[11][7][13]

### 9.2. Epidemiology, prevalence, and demographics

SCAR31 is an **ultra‑rare disease**, first described in 2021, with only a small number of families reported worldwide.[3][7][1][13] Precise prevalence and incidence estimates are not available, but given the rarity of biallelic ATG7 LoF variants and the small number of published cases, SCAR31 likely has a prevalence far below 1 in 100,000, perhaps in the range of a few families globally. Orphanet and Malacards classify SCAR31 as a rare disease but do not provide quantitative prevalence estimates, reflecting the lack of large epidemiologic data.[12][13]

Affected populations in the Collier cohort included families from multiple ethnic backgrounds, although specific demographic details are limited.[3] There is no evidence that SCAR31 is confined to any single geographic region or ethnic group, but autosomal recessive disorders may be more prevalent in communities with high consanguinity. Geographic distribution of specific variants may show clustering where founder mutations occur, but this has not yet been systematically mapped.

Sex ratio in SCAR31 appears to be approximately equal, with both male and female patients represented, and there is no indication of sex‑linked effects or significant sex differences in severity.[3][7][13] Age distribution of affected individuals spans childhood to adulthood, with some patients dying in childhood and others surviving into adulthood despite severe autophagy deficiency.[3][7] Knowledge bases should thus represent SCAR31 as a pediatric‑onset, lifelong disorder with no known sex predilection.

## 10. Diagnostics

### 10.1. Clinical evaluation and neuroimaging

Diagnostic evaluation of SCAR31 begins with **clinical assessment** of developmental, neurological, musculoskeletal, and systemic features. Clinicians should suspect SCAR31 in children with global developmental delay, hypotonia, ataxic gait, tremor, dysarthria, and neuroimaging showing cerebellar hypoplasia and thin posterior corpus callosum, especially when accompanied by optic atrophy, myopathy, and endocrine abnormalities.[1][3][7][13] A thorough neurological examination, developmental assessment, and physical evaluation for musculoskeletal and dysmorphic features are essential.

Brain MRI is a key diagnostic tool. Collier et al. reported that all assessed patients had cerebellar hypoplasia and a thin posterior corpus callosum, and Malacards and the Collier review emphasize these as hallmark imaging findings.[3][7][13] Radiological features include reduced cerebellar volume, particularly in the vermis and hemispheres, and a slender posterior corpus callosum, sometimes with enlarged ventricles.[3][13] Imaging databases and RadLex terms for cerebellar hypoplasia and corpus callosum abnormalities may be used to annotate these findings in knowledge bases.

Electrophysiologic tests such as EEG and EMG may be performed to evaluate seizures and neuromuscular function; EMG might reveal myopathic patterns in some patients, consistent with muscle biopsy findings.[3][7] Histopathology of muscle shows myopathic changes, p62 accumulation, and inflammation.[7] These findings support autophagy deficiency but are not specific to SCAR31; they must be interpreted in conjunction with genetic testing.

### 10.2. Genetic testing: exome sequencing and targeted analysis

The **definitive diagnosis** of SCAR31 requires identification of **biallelic pathogenic ATG7 variants** via genetic testing. Collier et al. used **exome sequencing** to discover ATG7 variants in affected individuals, highlighting the utility of genome‑wide sequencing approaches in diagnosing rare neurodevelopmental disorders.[3] Exome sequencing or genome sequencing is therefore recommended as a primary diagnostic modality for suspected SCAR31, especially in patients with complex neurodevelopmental phenotypes and nonspecific clinical features.

Once ATG7 variants are identified, confirmatory testing and segregation analysis in family members can establish autosomal recessive inheritance. Single‑gene sequencing of ATG7 may be used in families with known pathogenic variants, and targeted **gene panels** for hereditary ataxia or congenital autophagy disorders should include ATG7.[13][10] The Genetic Testing Registry (GTR) and ClinVar entries for ATG7 provide information on available tests and variant interpretation, although specific SCAR31‑focused panels may not yet exist.

Chromosomal microarray, karyotyping, and FISH are not typically useful for diagnosing SCAR31, as the disease is caused by point mutations and small indels rather than large copy number changes or structural rearrangements.[1][3][5][13] Mitochondrial DNA testing is also not directly relevant at present, though mitochondrial dysfunction is a downstream feature of autophagy deficiency.

### 10.3. Omics‑based diagnostics and biomarkers

Beyond DNA sequencing, functional assays of autophagy in patient cells can support diagnosis and mechanistic understanding. Collier et al. measured ATG7 protein levels and autophagy markers (LC3, p62) in fibroblasts and skeletal muscle, showing severely reduced ATG7, impaired LC3‑II formation, and p62 accumulation.[3][7] These **proteomics‑like assessments** provide evidence of autophagy deficiency and can serve as biomarkers of ATG7 dysfunction. However, they are research tools rather than routine clinical diagnostics.

No standardized blood, CSF, or urine biomarkers have been established for SCAR31. Circulating levels of autophagy markers, inflammatory cytokines, or metabolic indicators could potentially be informative, but this remains speculative. Omics‑based diagnostics such as RNA sequencing, metabolomics, or lipidomics could reveal signatures of autophagy deficiency, but these have not yet been applied systematically in SCAR31.

### 10.4. Clinical criteria and differential diagnosis

Formal diagnostic criteria for SCAR31 have not been published by professional societies, given the disease’s recent discovery and rarity. Diagnosis is based on **molecular confirmation** of biallelic ATG7 variants together with compatible clinical and imaging phenotypes.[3][7][1][13] In the absence of molecular data, SCAR31 cannot be reliably distinguished from other congenital ataxias and neurodevelopmental disorders.

The **differential diagnosis** includes other hereditary ataxias and neurodevelopmental syndromes, particularly those involving autophagy genes. The ATG5‑related congenital ataxia described by Kim et al. features congenital ataxia and mental retardation, similar to SCAR31, but is caused by ATG5 mutation.[4] WIPI2, WDR45, WDR45B, and ATG9B deficiency syndromes also present with neurodevelopmental defects and ataxia, and should be considered.[7][10] Non‑autophagy‑related congenital cerebellar hypoplasias, corpus callosum anomalies, and global developmental delay (e.g., PCH syndromes, intellectual disability syndromes) are also part of the differential.

The adult‑onset autosomal dominant SCA31 caused by BEAN1 repeat expansion must be distinguished from SCAR31. SCA31 presents with late‑onset progressive cerebellar ataxia, dysarthria, horizontal gaze nystagmus, and pure cerebellar involvement, whereas SCAR31 is pediatric‑onset with developmental delay, hypotonia, multi‑system involvement, and autosomal recessive inheritance.[8][13] Knowledge bases should provide clear **disambiguation** between these entities.

### 10.5. Screening and carrier testing

Population screening for SCAR31 is not currently feasible or recommended, given its ultra‑rarity and the lack of evidence‑based interventions. However, **carrier testing** and **cascade screening** in families with known ATG7 pathogenic variants are important for reproductive counseling and early detection in siblings. Genetic counseling should offer carrier testing for parents, siblings, and extended family members, as appropriate. Prenatal testing and preimplantation genetic diagnosis can be considered for carrier couples who wish to avoid having affected children, as discussed in the prevention section.

Newborn screening for SCAR31 is not currently available or practical, as no simple biochemical marker exists and genomic newborn screening for rare diseases is not yet standard practice. Knowledge bases should thus represent screening for SCAR31 primarily as **family‑based genetic carrier screening and prenatal diagnosis**.

## 11. Outcome and Prognosis

### 11.1. Survival, mortality, and life expectancy

Data on survival and mortality in SCAR31 are limited but suggest that **human life is compatible, in exceptional circumstances, with loss of a non‑redundant core autophagy protein**, albeit with morbidity.[3][7] Collier’s cohort included two siblings who survived into adulthood despite undetectable ATG7 protein and near absence of autophagic flux, and the review notes that **“ATG7 patients with dramatic reduction in autophagic activity are now approaching population life expectancy.”**[7] This remarkable finding indicates that, while ATG7 is essential for autophagy, compensatory mechanisms and tissue‑specific differences allow survival with severe autophagy deficiency.

However, not all patients have favourable survival. One patient in the Collier cohort died during childhood, and severe phenotypes with spastic paraplegia, seizures, and multi‑organ involvement likely increase mortality risk.[3][7] Comprehensive survival statistics (e.g., 5‑year, 10‑year survival rates) are not available due to the small number of cases and relatively recent description of the disease. Life expectancy is thus **variable**, with some patients reaching adulthood and potentially near normal life span, and others dying in childhood or adolescence.

Disease‑specific mortality arises from complications such as severe epilepsy, aspiration pneumonia, respiratory compromise due to neuromuscular weakness, endocrine crises, or infections, although detailed causes of death are not documented. Knowledge bases should reflect SCAR31 as a disease with potential for **long‑term survival**, but also risk for **early mortality** in severe cases, noting that more data are needed.

### 11.2. Morbidity, disability, and quality of life

Morbidity in SCAR31 is significant, encompassing intellectual disability, motor impairment, musculoskeletal weakness, visual and auditory deficits, and endocrine dysfunction.[1][3][7][13] Disability outcomes include limitations in mobility (ataxia, spastic paraplegia, inability to walk), communication (dysarthria, language impairment, hearing loss), self‑care, education, and employment. Many patients are likely to require lifelong assistance, specialized education, and supportive care.

Quality of life measures such as EQ‑5D or SF‑36 have not been systematically applied in SCAR31 cohorts, but extrapolation from hereditary ataxias and neurodevelopmental disorders suggests considerable impairment across physical, emotional, and social domains. Chronic motor impairment, cognitive deficits, visual and hearing loss, and endocrine issues contribute to reduced independence and social participation. Depression, anxiety, and caregiver burden may also be significant, although these aspects are not detailed in the literature.

Morbidity in SCAR31 should be catalogued in knowledge bases under International Classification of Functioning (ICF) domains, including impairments in neuromusculoskeletal functions, mental functions, and sensory functions, activity limitations in mobility and communication, and participation restrictions in education and employment.

### 11.3. Disease course, complications, and recovery potential

As discussed, SCAR31 follows a **chronic, progressive course** with variable severity. Complications include spastic paraplegia, seizures, musculoskeletal deformities, contractures, scoliosis, respiratory issues due to muscle weakness, visual and auditory disability, and endocrine crises or metabolic disturbances.[1][3][7][13] Inflammatory myopathy in muscle can cause pain and contribute to functional impairment.[7] Secondary complications such as infections, aspiration pneumonia, and pressure sores may arise in patients with severe disability.

Recovery potential is limited in terms of reversing structural brain anomalies or genetic defects; however, functional improvements can be achieved through early intervention, rehabilitation, and supportive therapies. Physical therapy can improve strength and coordination, occupational therapy can aid in adaptive strategies, and speech therapy can enhance communication despite dysarthria. Endocrine dysfunction may be managed with hormone replacement, and seizures can be controlled with anticonvulsant drugs. Thus, **partial functional recovery** and stabilization of symptoms are possible with appropriate management, though the underlying disease remains chronic.

Prognostic factors include **variant type and severity of ATG7 deficiency**, age of onset, severity of developmental delay and motor impairment, presence of seizures and endocrine complications, and access to multidisciplinary care.[3][7] Patients with undetectable ATG7 and near‑complete autophagy deficiency can still survive long term, but may have more severe phenotypes; conversely, hypomorphic variants might allow residual function and milder disease. Knowledge bases should categorize prognosis as **variable**, influenced by molecular severity and clinical management, and highlight the need for further longitudinal studies.

## 12. Treatment

### 12.1. Current pharmacotherapy and symptomatic management

At present, there is **no disease‑modifying pharmacotherapy** that directly corrects ATG7 deficiency or restores autophagic flux in SCAR31 patients. Treatment is therefore **symptomatic and supportive**, targeting specific manifestations such as seizures, spasticity, pain, and endocrine dysfunction. Anticonvulsant drugs (NCIT:C2946) are used to manage seizures, with choices based on seizure type and comorbidities. Muscle relaxants or antispasticity agents such as baclofen or tizanidine (NCIT:C80799, NCIT:C847) may alleviate spasticity, though care is required to avoid worsening weakness. Analgesics and anti‑inflammatory drugs can mitigate pain from myopathy or musculoskeletal complications.

Endocrine disorders are managed with hormone replacement therapies, such as thyroid hormone, cortisol, or sex hormones, depending on specific deficiencies. Nutritional support, including adequate caloric intake and management of vitamin and mineral deficiencies, is important for overall health. Gastrointestinal issues, if present, are managed with dietary modifications and medications.

Pharmacogenomics has not been specifically studied in SCAR31. However, given the multi‑system involvement and potential liver or kidney dysfunction, careful dose adjustment and monitoring of drug metabolism and toxicity are warranted. ATG7 deficiency may influence drug responses via altered autophagy, but data are lacking.

### 12.2. Advanced therapeutics: gene therapy and autophagy modulation

Conceptually, **gene therapy** or **gene editing** approaches that restore ATG7 expression could treat SCAR31 at its root cause. Viral vector‑mediated gene replacement, CRISPR‑based editing, or mRNA therapies targeting ATG7 could be envisioned. However, such approaches face significant challenges, including delivering the gene to the central nervous system, muscle, and endocrine tissues; dosing appropriately to avoid over‑activation of autophagy; and ensuring long‑term safety. As of the provided literature, no clinical trials have yet investigated gene therapy for SCAR31 or ATG7 deficiency.

Autophagy modulation via pharmacologic agents offers another theoretical avenue. mTOR inhibitors such as rapamycin, AMPK activators, or spermidine can enhance autophagy in some contexts, but in ATG7 deficiency, autophagy execution is impaired downstream, so upstream stimulation may not fully rescue function.[7] Agents that activate alternative degradation pathways or chaperone‑mediated autophagy might provide partial benefit. However, such strategies are speculative, and no clinical trials for SCAR31 have been reported.

Cell therapy approaches, such as stem cell transplantation or iPSC‑derived neuronal or muscle cell grafts, might ameliorate specific deficits, but they do not correct systemic autophagy deficiency. Immunotherapies are not directly relevant to SCAR31 at present.

### 12.3. Surgical, interventional, and rehabilitative therapies

Surgical interventions for SCAR31 are largely **supportive**, addressing complications such as scoliosis, contractures, or orthopedic deformities. Orthopedic surgery may correct severe scoliosis or limb deformities, improving posture and comfort. Neurosurgical interventions are rarely indicated, except potentially for refractory epilepsy (e.g., vagus nerve stimulation or epilepsy surgery) or severe spasticity (e.g., intrathecal baclofen pump).

Rehabilitation is a cornerstone of SCAR31 management. **Physical therapy** (NCIT:C15273) aims to improve strength, balance, coordination, and mobility, using exercises, assistive devices, and gait training. **Occupational therapy** (NCIT:C15294) focuses on maximizing independence in daily activities, adapting the environment, and providing assistive technologies. **Speech and language therapy** (NCIT:C15326) addresses dysarthria, language impairment, and swallowing difficulties. Early and ongoing rehabilitation can improve functional outcomes and quality of life.

### 12.4. Experimental treatments and personalized medicine

Because SCAR31 is newly recognized and ultra‑rare, **experimental treatments** have not yet reached clinical trial stages. Preclinical research in Atg7‑deficient mice and cellular models may inform future therapies. Personalized medicine approaches involve tailoring supportive and symptomatic management to individual needs, considering variant type, severity of autophagy deficiency, and co‑morbidities.

Genotype‑guided treatment is not yet established, but theoretical considerations include more aggressive supportive care in patients with complete ATG7 loss and careful monitoring of metabolic and endocrine functions. Pharmacogenomic considerations might involve avoiding drugs that are heavily dependent on autophagy for clearance or that exacerbate autophagy deficiency, although specific data are lacking.

Knowledge bases should represent SCAR31 treatment as primarily **supportive and rehabilitative**, with **no approved disease‑modifying therapies**, while highlighting gene therapy and autophagy modulation as potential future directions.

## 13. Prevention

### 13.1. Primary, secondary, and tertiary prevention

Primary prevention of SCAR31 involves **avoiding the occurrence of disease** in at‑risk families through genetic counseling and reproductive choices. For couples who are both ATG7 carriers, options include preimplantation genetic diagnosis (PGD) to select embryos without biallelic ATG7 mutations, targeted prenatal testing with chorionic villus sampling or amniocentesis, and consideration of donor gametes. ACMG and ACOG guidelines on carrier screening and reproductive counseling can inform these decisions.

Secondary prevention involves **early detection and intervention** in affected individuals. Early diagnosis via exome sequencing and clinical evaluation allows prompt initiation of rehabilitation, management of seizures and endocrine dysfunction, and planning for educational and supportive services. While early intervention does not cure SCAR31, it may improve developmental outcomes and quality of life.

Tertiary prevention focuses on **preventing complications** and optimizing function in those with established disease. This includes proactive management of spasticity, contractures, scoliosis, respiratory function, nutrition, vision and hearing, endocrine issues, and mental health. Regular multidisciplinary follow‑up and individualized care plans are essential.

### 13.2. Genetic counseling, screening, and public health considerations

Genetic counseling is central to SCAR31 prevention. Counselors should explain autosomal recessive inheritance, carrier risks, reproductive options, and implications for extended family members. Carrier screening in families with known ATG7 variants can identify at‑risk individuals and guide family planning.

Population‑wide carrier screening for ATG7 variants is not currently recommended, given the ultra‑rarity of SCAR31 and lack of cost‑effective screening strategies. Public health interventions for SCAR31 are limited, but general policies promoting access to genomic diagnostics and rare disease care can indirectly support prevention and management.

Behavioral interventions such as promoting healthy lifestyles may help manage general health but are unlikely to prevent SCAR31, which is genetically determined. Environmental interventions to reduce toxins or pollutants have no specific preventive role for SCAR31 at present.

Prophylactic medications or procedures are not available for SCAR31. Preventive strategies are thus focused on **genetic counseling and reproductive planning** (primary prevention) and **early diagnosis and structured care** (secondary and tertiary prevention).

## 14. Other Species and Natural Disease

### 14.1. Species affected and comparative pathology

No naturally occurring SCAR31‑like disease has been reported in companion animals or wildlife. However, **Atg7 deficiency in model organisms** provides insight into comparative pathology. In mice, conditional Atg7 knockout in neurons, muscle, hematopoietic cells, and germ cells causes phenotypes analogous to SCAR31, including ataxia, neurodegeneration, myopathy, hematopoietic defects, and ovarian insufficiency.[5][7][9][16] In yeast, Atg7 deletion severely attenuates autophagy and impairs survival under stress.[3][7][15] Zebrafish orthologs of ATG7 (*atg7*) are linked via ZFIN to the human disease DOID:0070412, indicating evolutionary conservation and potential for zebrafish disease modeling.[14]

These comparative models show that ATG7’s role in autophagy and tissue homeostasis is conserved across metazoans and fungi, and that loss of ATG7 leads to neurodegeneration and systemic pathology in multiple species. Comparative pathology thus supports the mechanistic understanding of SCAR31 and validates autophagy deficiency as the core mechanism.

### 14.2. Evolutionary conservation and transmission

ATG7 is highly conserved across eukaryotes, with homologs in yeast (*Atg7*), flies, zebrafish, and mammals.[7][15][14] The conservation of functional domains and catalytic mechanisms underscores the importance of ATG7 in autophagy and survival. Evolutionary analyses show strong purifying selection against disruptive ATG7 variants, consistent with gnomAD constraint data.[11][7] There is no zoonotic transmission or cross‑species susceptibility in the infectious sense, as SCAR31 is a genetic disorder, not an infection.

## 15. Model Organisms

### 15.1. Mouse models: Atg7 knockout and conditional mutants

Mouse models have been pivotal in elucidating ATG7’s role in autophagy and disease. Repositories such as RIKEN BioResource Center list **Atg7 floxed mice** (strain B6.Cg‑Atg7<tm1Tchi>), which enable tissue‑specific Atg7 deletion via Cre recombinase.[9] The strain description notes that Atg7 is essential for ATG conjugation, LC3 modification systems, and autophagosome formation, and that conditional Atg7‑deficient mice can be generated by crossing with tissue‑specific Cre mice.[9] Homozygous mutant mice are viable and fertile, but tissue‑specific knockouts reveal severe phenotypes in targeted organs.[9]

Komatsu et al. reported that loss of Atg7 in neurons leads to neurodegeneration, axon degeneration, and motor phenotypes including tremors and limb grasping.[1][5][7][9] Mammalian phenotype ontology annotations for Atg7‑deficient mice include abnormal autophagy, axon degeneration, absent cerebral cortex pyramidal cells, absent hippocampus pyramidal cells, abnormal nervous system physiology, tremors, limb grasping, weight loss, and liver abnormalities.[9] These phenotypes recapitulate key aspects of SCAR31, including ataxia, neurodegeneration, and systemic involvement, making Atg7 knockout mice valuable models.

Other tissue‑specific Atg7 knockouts include **uterine mesenchyme‑specific Atg7 knockout mice**, which exhibit repopulation of autophagy‑deficient stromal cells with autophagy‑intact cells after repeated breeding, demonstrating autophagy’s role in uterine physiology.[9] **Germ cell‑specific Atg7 knockout** results in primary ovarian insufficiency in female mice, highlighting reproductive consequences of autophagy deficiency.[9] These models illustrate ATG7’s roles beyond the nervous system.

More recently, Atg7 disruption in outer hair cells of mice causes electromotility disturbances, outer hair cell loss, and deafness, paralleling sensorineural hearing loss observed in SCAR31 patients.[7] Collectively, these models show that Atg7 deficiency in specific tissues replicates human disease features and confirm the mechanistic chain from ATG7 loss to tissue pathology.

### 15.2. Other model systems: yeast, zebrafish, and B cell models

Yeast *Atg7* mutants are classical autophagy models, demonstrating that ATG7 deletion severely impairs autophagy and survival under starvation.[3][7][15] These models established ATG7’s function in ubiquitin‑like conjugation and autophagosome biogenesis, laying groundwork for mammalian studies.

Zebrafish models, while not yet fully developed for ATG7 deficiency, are promising given ZFIN’s mapping of human ATG7 and SCAR31 to zebrafish *atg7* and DOID:0070412.[14] Zebrafish offer advantages for in vivo imaging of neurodevelopment and autophagy, and could be used to study ATG7 deficiency’s effects on brain and muscle development.

B1a B cell‑specific Atg7 deletion models, such as those studied by Clarke et al., illustrate ATG7’s role in immune cell metabolism and self‑renewal.[16] These models show that autophagy is differentially activated in B1a B cells and that Atg7 deletion leads to selective loss of B1a cells due to metabolic dysfunction and failure of self‑renewal.[16] While not directly modeling SCAR31, they provide insight into systemic implications of ATG7 deficiency.

### 15.3. Model characteristics, limitations, and applications

Atg7 knockout and conditional mouse models **recapitulate major features** of SCAR31, including neurodegeneration, ataxia, myopathy, reproductive issues, and immune cell abnormalities.[5][7][9][16] They allow detailed mechanistic studies of autophagy, tissue‑specific roles of ATG7, and the consequences of autophagy deficiency. However, there are limitations. Mice may exhibit more severe phenotypes than human SCAR31 patients, possibly due to differences in compensatory pathways or genetic background. Tissue‑specific knockouts cannot fully recapitulate the global germline ATG7 deficiency seen in SCAR31, although they can mimic organ‑specific manifestations.

Applications of these models include studying autophagy pathways, testing pharmacologic modulators of autophagy, investigating gene therapy approaches, and performing multi‑omics profiling. They provide preclinical platforms for potential SCAR31 therapies and mechanistic discovery.

Knowledge bases should link SCAR31 to Atg7 mouse models and yeast and zebrafish ATG7 models, annotating phenotypic overlaps and mechanistic insights with evidence type “model organism” (e.g., MGI, ZFIN, SGD references).

## Conclusion

Spinocerebellar ataxia, autosomal recessive 31 (SCAR31) is a paradigmatic **congenital disorder of autophagy** caused by biallelic loss‑of‑function variants in ATG7, a non‑redundant core autophagy effector enzyme.[1][3][5][7][13][14][15] Clinically, SCAR31 is characterized by early‑onset global developmental delay, hypotonia, variably impaired intellectual and language development, cerebellar ataxia, tremor, dysarthria, and, in severe cases, spastic paraplegia and inability to walk.[1][3][7][13] Neuroimaging reveals cerebellar hypoplasia and thin posterior corpus callosum, marking the disease as a neurodevelopmental rather than purely degenerative ataxia.[3][7][13] Additional features include myopathy, optic atrophy, retinitis pigmentosa, sensorineural deafness, facial dysmorphism, and endocrine dysfunction.[3][7][13] 

Mechanistically, ATG7 deficiency disrupts autophagy by impairing ATG12–ATG5 conjugation and LC3 lipidation, leading to severe autophagic flux reduction, accumulation of p62/SQSTM1, defective long‑lived protein degradation, and widespread cellular stress.[1][3][5][7][15][16] This autophagy failure compromises axonal homeostasis, neuronal development, muscle maintenance, endocrine function, and immune cell metabolism, generating the multi‑system SCAR31 phenotype. Model organism studies, particularly Atg7 knockout mice, validate these mechanisms and recapitulate key disease features, including neurodegeneration, ataxia, myopathy, and reproductive and immune abnormalities.[5][7][9][16]

SCAR31 is ultra‑rare, with only a small number of families described, but it has profound implications for understanding autophagy’s role in human health and disease. As Collier et al. emphasized, **“humans can survive with mild–moderate neurological impairments despite undetectable levels of ATG7 protein,”** showing that loss of a non‑redundant autophagy protein can be compatible with life, albeit at significant cost.[7] This challenges assumptions about gene essentiality and highlights the plasticity of human physiology.

Diagnostic confirmation of SCAR31 relies on exome or genome sequencing to identify biallelic ATG7 variants, coupled with clinical and imaging features.[3][1][13] There are no disease‑modifying therapies yet; management is supportive and rehabilitative, addressing seizures, spasticity, endocrine issues, and neurodevelopmental needs. Prevention focuses on genetic counseling and reproductive planning in affected families.

From a knowledge base perspective, SCAR31 should be represented as a Mondo:0030323 entity with cross‑links to OMIM:619422, DOID:0070412, ORPHA:88644, ATG7 (HGNC:ATG7; OMIM:608760; UniProt:O95352), and relevant HPO, GO, CL, UBERON, CHEBI, and NCIT terms. Evidence items should distinguish **human clinical data** (Collier et al., OMIM, Malacards), **model organism studies** (Komatsu et al., Atg7 knockout mice, Clarke et al.), **in vitro cellular assays** (patient fibroblasts and muscle), and **computational/population genetics analyses** (gnomAD LOEUF). Direct quotes from key abstracts and reviews, as incorporated above, support critical claims and provide authoritative phrasing.

Future research priorities include expanding patient cohorts to refine phenotype spectra and natural history, performing multi‑omics profiling to elucidate cell‑type specific mechanisms, exploring gene therapy and autophagy modulation strategies, and leveraging model organisms and iPSC systems to test interventions. SCAR31, as the first human ATG7 deficiency syndrome, will continue to illuminate the indispensable roles of autophagy in neurodevelopment, axonal maintenance, muscle and endocrine physiology, and systemic metabolic homeostasis.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.