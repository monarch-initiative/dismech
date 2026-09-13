---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:15:43.184476'
end_time: '2026-09-05T17:26:35.987776'
duration_seconds: 652.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Xanthinuria
  mondo_id: MONDO:0018106
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hereditary_Xanthinuria-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Xanthinuria
- **MONDO ID:** MONDO:0018106 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hereditary Xanthinuria** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Hereditary Xanthinuria
- **MONDO ID:** MONDO:0018106 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hereditary Xanthinuria** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Hereditary Xanthinuria: Comprehensive Disease-Characteristics Report

## Executive summary

Hereditary (classical) xanthinuria is a rare, lifelong, autosomal-recessive disorder of terminal purine catabolism. **Type I** results from biallelic **XDH** loss-of-function variants and isolated xanthine oxidoreductase deficiency; **type II** results from biallelic **MOCOS** variants and failure to sulfurate the molybdenum cofactor required by both xanthine oxidoreductase and aldehyde oxidase. Both forms cause profound hypouricemia and hypouricosuria with accumulation and urinary excretion of hypoxanthine and poorly soluble xanthine. Most patients are asymptomatic, but xanthine crystalluria and stones may cause hematuria, renal colic, obstruction, infection, hydronephrosis, acute kidney injury, chronic kidney disease, or—rarely—kidney failure. In the largest well-characterized cohort, 7/20 patients (35%) were symptomatic; broader case literature suggests disease-attributable symptoms or xanthine stones in approximately 40%. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 18-19)

A compact subtype comparison follows.

| Domain | Type I | Type II | Evidence/notes |
|---|---|---|---|
| Causal gene | **XDH** | **MOCOS** | Biallelic loss-of-function variants cause classical hereditary xanthinuria (peretz2021classicalxanthinuriain pages 2-4, peretz2021classicalxanthinuriain pages 1-2) |
| OMIM disease ID | **278300** | **603592** | Current genetic-nephrolithiasis review confirms both subtype mappings (gefen2024reviewofchildhood pages 15-16) |
| Inheritance | Autosomal recessive | Autosomal recessive | Consanguinity, homozygosity, and founder effects are frequent in reported families (peretz2021classicalxanthinuriain pages 18-19) |
| Enzyme defect | Isolated xanthine dehydrogenase/xanthine oxidoreductase deficiency | Combined xanthine dehydrogenase/xanthine oxidoreductase and aldehyde oxidase deficiency | MOCOS normally sulfurates molybdenum cofactor required by both enzymes (peretz2021classicalxanthinuriain pages 2-4, ichida2012mutationsassociatedwith pages 1-3) |
| Core biomarkers | Profound hypouricemia and hypouricosuria; increased urinary xanthine and hypoxanthine | Same core biochemical profile | Fractional urate excretion is generally normal or low; one type I case had serum urate <5.95 µmol/L and combined urinary xanthine/hypoxanthine of 108.35 µmol/mmol creatinine (abal2021identificationofa pages 1-2) |
| Principal complications | Xanthine crystalluria and radiolucent urolithiasis; obstruction, hematuria, renal colic, urinary infection, hydronephrosis, and rarely kidney failure; occasional myopathy/arthropathy | Similar renal and extra-renal phenotype, plus potential toxicity from drugs dependent on aldehyde oxidase metabolism | Approximately 35% of a 20-patient cohort were symptomatic; historical series suggest stones or attributable symptoms in roughly 40% (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 18-19, cameron1993gouturicacid pages 6-8) |
| Diagnostic confirmation | Biallelic pathogenic/likely pathogenic **XDH** variants | Biallelic pathogenic/likely pathogenic **MOCOS** variants; aldehyde-oxidase functional/metabolite testing can distinguish type II | Confirm biochemical suspicion with sequencing that covers coding regions, splice boundaries, and copy-number changes; historical allopurinol loading is now secondary to molecular testing (grases2018xanthineurolithiasisinhibitors pages 1-2, peretz2021classicalxanthinuriain pages 2-4) |
| Management | High fluid intake; low-purine diet; reduce purine- and fructose-rich foods; monitor renal function and stone burden; remove obstructing stones when necessary | Same measures, with added medication review for aldehyde-oxidase-dependent drugs | No disease-specific pharmacotherapy is established. Urine alkalinization has uncertain or little benefit because xanthine solubility is relatively pH-independent; allopurinol is not routine therapy and may increase xanthine burden (grases2018xanthineurolithiasisinhibitors pages 1-2, peretz2021classicalxanthinuriain pages 2-4, cameron1993gouturicacid pages 1-2) |


*Table: Compact comparison of the genetic, biochemical, clinical, diagnostic, and management features of hereditary xanthinuria types I and II. Evidence notes identify established findings and important treatment cautions.*

**Evidence caveat.** Disease-specific 2023–2024 primary literature is sparse. The current picture therefore rests on a 2024 genetic-nephrolithiasis review, a 2023 NIH natural-history protocol, the largest molecular cohort published in 2021, functional studies, and individual case reports. Population incidence, penetrance, quality-of-life effects, and long-term survival have not been established prospectively.

---

## 1. Disease information

### Definition and classification

“Hereditary xanthinuria,” “classical xanthinuria,” “xanthine oxidoreductase deficiency,” and “xanthine dehydrogenase/oxidase deficiency” are commonly used names. The adjective **classical** generally covers types I and II and distinguishes them from generalized molybdenum-cofactor deficiency, sometimes historically called “type III.” The latter is a clinically distinct, usually severe neurodevelopmental disease caused by molybdenum-cofactor biosynthesis defects and should not be merged with XDH- or MOCOS-related classical xanthinuria. (abal2021identificationofa pages 1-2, gefen2024reviewofchildhood pages 15-16)

**Identifiers supported by the retrieved sources**

- Parent disease: **MONDO:0018106**, as specified in the target template.
- Xanthinuria type I: **OMIM/MIM 278300**.
- Xanthinuria type II: **OMIM/MIM 603592**.
- XDH gene entry cited in the NIH protocol: **OMIM *607633**.
- No disease-specific ICD-10-CM or ICD-11 code was established in the retrieved literature; coding generally falls under broader disorders of purine/pyrimidine metabolism. A specific MeSH identifier was likewise not verified and should not be inferred. (abal2021identificationofa pages 1-2, gefen2024reviewofchildhood pages 15-16, NCT06092346 chunk 1)

The evidence is principally **aggregated disease-level literature plus small patient cohorts and case reports**, not EHR-derived population data. The major 2021 study combined molecular, biochemical, clinical, and genealogical data from Israeli and German families. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 5-8)

---

## 2. Etiology, risk, protection, and environment

### Primary cause

The initiating cause is germline, biallelic loss of function in **XDH** or **MOCOS**. Type I is an isolated XDH/XOR defect. In type II, MOCOS deficiency leaves molybdenum cofactor in an inactive oxo form, disabling both XDH/XOR and aldehyde oxidase. These are monogenic disorders rather than infectious, toxic, occupational, or lifestyle-acquired diseases. (peretz2021classicalxanthinuriain pages 2-4, ichida2012mutationsassociatedwith pages 1-3)

### Genetic risk factors

The principal risk factors are parental carrier status, consanguinity, endogamy, and founder alleles. In one family series, 70% of 17 parental couples were consanguineous and 18% were endogamous; most affected offspring were homozygous. More than two-thirds of published cases have originated from Mediterranean or Middle Eastern populations, probably reflecting ascertainment, consanguinity, and founder effects rather than biological restriction to those populations. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 18-19)

A likely founder XDH variant, **c.2164A>T (p.Lys722Ter)**, was identified in Turkmen- and Arab-origin families. The estimated common ancestor was approximately 179 generations old, supporting broad dispersion across the Afro-Asian stone-forming belt. A Yemenite-Jewish MOCOS **c.1046C>T (p.Thr349Ile)** founder effect is also supported by affected families and carrier detection. (peretz2021classicalxanthinuriain pages 8-9)

No validated susceptibility loci, modifier genes, protective alleles, anticipation, or clinically important germline mosaicism have been established. The severe mouse–human difference implicates purine salvage and nucleobase transport—notably **HPRT** activity and species-specific **SLC23A4** status—as plausible mechanistic modifiers, but this has not been demonstrated as a human modifier association. (terada2025pseudogenizationofthe pages 2-3, terada2025pseudogenizationofthe pages 1-2)

### Environmental and protective factors

Diet does not cause the genetic defect, but purine intake, fructose-rich intake, low urine volume, and dehydration plausibly increase substrate delivery or urinary supersaturation and therefore modify stone risk. High fluid intake and reduction of purine-rich foods are the most consistently recommended protective measures; one cohort also recommends avoiding fructose-rich foods. Quantitative hydration or dietary targets have not been validated in trials. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 2-4, cameron1993gouturicacid pages 1-2)

There is no evidence that smoking, alcohol, pollution, radiation, occupational exposure, or infectious agents initiate classical xanthinuria. Alcohol may be discouraged as part of a low-purine stone-prevention diet, but this is management advice rather than evidence of causation. No vaccine or antimicrobial prevention applies.

---

## 3. Phenotypes

| Phenotype | Type and characteristics | Frequency/course | Suggested HPO term |
|---|---|---|---|
| Profound hypouricemia | Laboratory abnormality; congenital biochemical trait, usually persistent | Essentially defining; may be incidentally detected at any age | Hypouricemia (HP:0003537) |
| Hypouricosuria | Laboratory abnormality; very low/undetectable urinary urate, with normal or low fractional urate excretion | Defining | Decreased urinary urate excretion |
| Xanthinuria/hypoxanthinuria | Laboratory abnormality; increased urinary xanthine and hypoxanthine | Defining | Xanthinuria; abnormal urinary purines |
| Xanthine crystalluria/urolithiasis | Sign/manifestation; episodic, recurrent, variable severity; radiolucent stones | About 40% in historical literature; variable between cohorts | Nephrolithiasis (HP:0000787), Crystalluria |
| Hematuria and renal colic | Symptom/sign secondary to stones | Intermittent; subset of stone formers | Hematuria (HP:0000790), Renal colic |
| Obstruction/hydronephrosis | Structural complication | Uncommon; may be acute | Hydronephrosis (HP:0000126), Urinary-tract obstruction |
| Urinary infection | Secondary complication | Recurrent in some symptomatic patients | Recurrent urinary-tract infections |
| AKI/CKD/kidney failure | Organ complication from obstruction/crystal injury; severity highly variable | Rare but documented, including ESKD | Acute kidney injury, Renal insufficiency (HP:0000083) |
| Myalgia/myopathy | Symptom attributed to xanthine deposition | Minority/rare | Myalgia (HP:0003326), Myopathy |
| Arthropathy | Musculoskeletal manifestation | Rare | Arthropathy (HP:0003040) |

The 2021 cohort found 7/20 affected persons symptomatic (35%). Among 11 adults, only 3 (27%) retrospectively reported urolithiasis symptoms, whereas 47% of children and young adults were symptomatic, suggesting ascertainment or age-related differences rather than a proven age-dependent penetrance model. Onset can be neonatal, pediatric, or adult, and many adults remain asymptomatic. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 18-19, peretz2021classicalxanthinuriain pages 19-20)

A quantitative type-I case had serum urate **<5.95 µmol/L**, urinary urate **12.15 µmol/mmol creatinine**, and combined urinary xanthine/hypoxanthine **108.35 µmol/mmol creatinine**; ultrasound showed 7- and 9-mm suspected renal calculi. (abal2021identificationofa pages 1-2)

There are no validated disease-specific EQ-5D, SF-36, PROMIS, behavioral, or psychiatric data. Quality-of-life impairment is expected mainly during renal colic, infection, repeated procedures, or kidney failure, but has not been quantified.

---

## 4. Genetic and molecular information

### Causal genes and proteins

- **XDH**, chromosome **2p23.1**, transcript **NM_000379.4**, protein **NP_000370.2**, encodes a 1,333-amino-acid xanthine dehydrogenase/oxidoreductase. Each approximately 150-kDa subunit contains two [2Fe–2S] centers, an FAD-binding region, and a C-terminal molybdenum-cofactor-binding catalytic domain. (peretz2021classicalxanthinuriain pages 2-4, ichida2012mutationsassociatedwith pages 1-3)
- **MOCOS**, chromosome **18q12.2**, transcript **NM_017947.1**, protein **NP_060417.4**, encodes an 888-amino-acid molybdenum-cofactor sulfurase. Its N-terminal NifS-like, pyridoxal-phosphate-dependent cysteine-desulfurase domain supplies sulfur; its C-terminal domain binds Moco and generates active sulfido-Moco. (peretz2021classicalxanthinuriain pages 2-4)

### Representative pathogenic variants

Reported **XDH** disease alleles include frameshift, nonsense, and missense variants: c.141insG p.Cys48LeufsTer12; c.449G>T p.Cys150Phe; c.641del p.Pro214GlnfsTer4; c.913del p.Leu305fsTer1; c.1434G>A p.Trp478Ter; c.1658insC p.Ala556SerfsTer67; c.1871C>G p.Ser624Ter; c.2164A>T p.Lys722Ter; and c.2473C>T p.Arg825Ter. Reported **MOCOS** alleles include c.1037insA p.Gln347AlafsTer33; c.1046C>T p.Thr349Ile; c.1088_1089del p.Leu363ProfsTer16 (ClinVar 1017655; rs761752580); c.1771C>T p.Pro591Ser; and c.2326C>T p.Arg776Cys. These are germline variants; somatic origin is not part of disease pathogenesis. Population allele frequencies were not available in the retrieved evidence and should be obtained directly from current gnomAD/ClinVar records before database ingestion. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 8-9)

Functional evidence is unusually strong for several missense alleles. XDH Cys150 lies in the Fe/S-I cluster-binding motif; the corresponding plant-protein substitution prevented detectable stable protein accumulation. MOCOS p.Thr349Ile markedly impaired protein stability, PLP binding, and cysteine-desulfurase activity; p.Pro591Ser and p.Arg776Cys reduced Moco/MPT binding to about **24%** and **6%** of wild type, respectively. These experiments used plant/yeast or bacterial heterologous systems rather than human renal cells. (peretz2021classicalxanthinuriain pages 14-16)

No recurrent chromosomal abnormality, disease-specific methylation signature, histone alteration, or validated epigenetic mechanism is known. Likewise, there are no established disease-specific single-cell, spatial-transcriptomic, proteomic, lipidomic, CRISPR-screen, or multi-omic patient datasets.

---

## 5–6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic XDH loss of function leads to** absent or markedly reduced XDH/XOR activity (**type I**).
2. **Alternatively, biallelic MOCOS loss of function leads to** deficient sulfur insertion into Moco, which **results in** combined loss of XDH/XOR and aldehyde-oxidase activity (**type II**).
3. **Loss of XDH/XOR catalysis leads to** failure of hypoxanthine → xanthine and xanthine → uric-acid oxidation.
4. **This block results in** profound hypouricemia/hypouricosuria and accumulation of xanthine and hypoxanthine; much hypoxanthine is salvaged to IMP, whereas xanthine is excreted.
5. **High urinary xanthine plus its poor solubility leads to** crystalluria and xanthine-stone nucleation.
6. **Crystal deposition or stones lead to** tubular obstruction, epithelial injury, hematuria, renal colic, hydronephrosis, and infection.
7. **Persistent or severe obstruction/crystal injury leads to** AKI, interstitial inflammation/fibrosis, CKD, and occasionally kidney failure; tubular apoptosis and fibrosis are demonstrated in mice but partly inferred in humans.
8. **Type-II aldehyde-oxidase deficiency additionally leads to** impaired metabolism of selected xenobiotics, which can result in drug toxicity.

This is a metabolic enzyme-deficiency pathway, not a canonical Wnt/MAPK/mTOR signaling disorder. Mammalian XOR normally transfers electrons from the molybdenum catalytic center through Fe–S clusters to FAD and NAD+ or oxygen. It can also generate reactive oxygen species and participate in nitric-oxide biology; however, the contribution of reduced XOR-derived ROS or reduced urate antioxidant capacity to human xanthinuria phenotypes remains uncertain. (ichida2012mutationsassociatedwith pages 1-3)

**Suggested ontology annotations:** purine nucleobase catabolic process; xanthine catabolic process; hypoxanthine metabolic process; urate biosynthetic process; molybdenum-cofactor sulfuration; oxidoreductase activity; iron–sulfur cluster binding; FAD binding; molybdenum-ion binding. Relevant cells include renal tubular epithelial cells—especially proximal tubular epithelium—and hepatocytes, because liver is a major site of XDH and aldehyde-oxidase activity. Suggested CL labels are *kidney proximal tubule epithelial cell* and *hepatocyte*; suggested GO cellular components include cytosol, molybdenum-cofactor-containing enzyme complex, and iron–sulfur cluster-containing protein complex.

---

## 7. Anatomical structures affected

The primary clinically affected system is the **urinary system**: kidney, renal calyces/pelvis, ureters, and bladder can contain crystals or stones. Suggested UBERON labels are kidney, renal tubule, renal pelvis, ureter, and urinary bladder. Injury localizes principally to renal tubular lumina and epithelium, with downstream interstitium and whole-kidney involvement in severe disease. Stones may be unilateral or bilateral; no characteristic lateralization exists. (patil2025xanthinestonesin pages 2-4, piret2012amousemodel pages 4-8)

The liver is the major metabolic site of XDH/XOR and aldehyde oxidase but generally does not show a primary clinical lesion. Skeletal muscle and joints are rare secondary sites associated with myopathy or arthropathy. No consistent cardiovascular, respiratory, immune, endocrine, or nervous-system involvement characterizes classical types I/II. Neurologic disease should instead raise concern for generalized molybdenum-cofactor deficiency. (abal2021identificationofa pages 1-2, cameron1993gouturicacid pages 6-8)

---

## 8–9. Temporal development, inheritance, and population

The biochemical defect is congenital and lifelong. Clinical onset is highly variable—from neonatal stone disease to incidental adult hypouricemia—and the course may remain stable and asymptomatic or become episodic with recurrent stones. There is no accepted stage system, remission definition, anticipation, or predictable progression rate. Prevention before the first stone and rapid relief of obstruction are the main actionable windows. (peretz2021classicalxanthinuriain pages 18-19, peretz2021classicalxanthinuriain pages 19-20)

Inheritance is autosomal recessive. Penetrance of the **biochemical phenotype** appears high in biallelic loss of function, but penetrance of symptoms is incomplete and expressivity variable. For unrelated carrier parents, counseling uses the standard per-pregnancy probabilities: 25% affected, 50% carrier, and 25% unaffected/non-carrier. Carrier frequency and population incidence are unknown; published estimates vary too widely and are not supported by population screening. No reliable cases-per-100,000 prevalence or annual incidence can presently be supplied. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 18-19)

Both sexes are affected; no credible sex ratio has been established. Disease is worldwide, with apparent enrichment in Mediterranean, Middle Eastern, Arab, Jewish, and Turkmen families. That pattern is influenced by consanguinity, founder alleles, and publication bias. (peretz2021classicalxanthinuriain pages 1-2, peretz2021classicalxanthinuriain pages 8-9)

---

## 10. Diagnostics

### Recommended workflow

1. **Recognize persistent profound hypouricemia.** Repeat serum urate and exclude laboratory interference or urate-lowering medication.
2. **Determine underproduction versus renal wasting.** Hereditary xanthinuria shows very low urinary urate and normal/low fractional urate excretion; renal hypouricemia usually has increased fractional excretion (>10% in a recent review/case definition).
3. **Measure urine and preferably plasma xanthine/hypoxanthine** by HPLC or LC–MS/MS. Marked xanthinuria with hypouricosuria is the central biochemical signature.
4. **Analyze any stone** by infrared spectroscopy or X-ray diffraction. Xanthine stones are typically radiolucent on plain radiography but detectable by ultrasound or CT.
5. **Confirm genetically** with sequencing and deletion/duplication analysis of **XDH** and **MOCOS**. A monogenic nephrolithiasis/purine-metabolism panel is reasonable; WES/WGS is useful when targeted testing is negative or phenotype is atypical. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are not first-line tests.
6. **Distinguish type I from type II.** Genotype is preferred. Aldehyde-oxidase-dependent metabolite profiling can support type II. Historical liver biopsy and allopurinol-loading tests are now secondary and carry practical or safety disadvantages. (grases2018xanthineurolithiasisinhibitors pages 1-2, abal2021identificationofa pages 1-2, peretz2021classicalxanthinuriain pages 2-4)

A modern stone example illustrates imaging limitations: plain radiography was negative, whereas CT showed a 10-mm renal-pelvic stone and distal ureteral stones at approximately 352–427 HU; FT-IR/crystallography found 71% xanthine. This 2025 case is supportive but not a validated universal HU threshold. (patil2025xanthinestonesin pages 2-4)

### Differential diagnosis

- **Renal hypouricemia** due to SLC22A12/URAT1 or SLC2A9/GLUT9: low serum urate but high fractional urate excretion; exercise-induced AKI is characteristic.
- **Generalized molybdenum-cofactor deficiency** due to MOCS1, MOCS2, GPHN or related genes: sulfite-oxidase deficiency, neonatal/infantile encephalopathy, seizures, abnormal tone and developmental impairment, plus xanthinuria.
- **Purine nucleoside phosphorylase deficiency**, **APRT deficiency/2,8-dihydroxyadenine stones**, and other monogenic stone disorders.
- Acquired hypouricemia from urate-lowering drugs, severe liver disease, malnutrition, SIADH, or proximal tubular dysfunction.
- Iatrogenic xanthine stones during strong XOR inhibition, especially in high-purine-turnover states.

The 2024 pediatric review confirms XDH and MOCOS as xanthinuria genes and distinguishes MOCS1/MOCS2 molybdenum-cofactor deficiency, in which neurologic/systemic disease is expected. (gefen2024reviewofchildhood pages 15-16)

Population newborn screening is not established. Cascade biochemical and genetic testing of siblings and reproductive partners is appropriate after a molecular diagnosis.

---

## 11. Outcome and prognosis

Most diagnosed individuals have normal general development and can remain asymptomatic for decades. No disease-specific survival curve, 5- or 10-year survival statistic, life-expectancy estimate, mortality rate, validated prognostic model, or quality-of-life instrument exists. Prognosis is mainly determined by stone burden, obstruction, recurrent infection, and renal function. Rare severe outcomes include nephrectomy, CKD, ESKD, uremia, and death. (peretz2021classicalxanthinuriain pages 1-2, cameron1993gouturicacid pages 6-8)

A recent 2024 nephrolithiasis review recognizes that both types can progress to ESKD. Conversely, the 2021 family cohort reported no stone recurrence under conservative advice during available follow-up, although cohort size and follow-up preclude efficacy estimates. (peretz2021classicalxanthinuriain pages 19-20, gefen2024reviewofchildhood pages 15-16)

---

## 12. Treatment and current implementation

### Conservative management

There is no approved enzyme replacement, substrate-reduction drug, gene therapy, RNA therapy, or disease-specific pharmacotherapy. Standard real-world care consists of:

- high fluid intake to maintain dilute urine;
- a low-purine diet and avoidance of excessive purine-rich food;
- reduction of fructose-rich foods where advised;
- periodic serum creatinine/eGFR, urinalysis, urinary metabolites, and renal imaging;
- prompt treatment of urinary infection and urgent decompression/removal of obstructing stones. (peretz2021classicalxanthinuriain pages 2-4, abal2021identificationofa pages 1-2)

Suggested NCIt intervention labels include **Dietary Modification**, **Fluid Therapy/Oral Hydration**, **Metabolic Monitoring**, **Ureteroscopy**, **Laser Lithotripsy**, **Percutaneous Nephrolithotomy**, **Ureteral Stent Placement**, and **Kidney Transplantation** where clinically necessary.

### Important therapeutic cautions

**Allopurinol is not routine treatment for hereditary xanthinuria.** It inhibits the already defective target and can increase xanthine burden in other clinical contexts. Its historical use as a diagnostic loading test should not be confused with chronic therapy. Type-II patients also lack aldehyde oxidase and may have altered handling/toxicity of AOX substrates; literature specifically flags allopurinol, azathioprine, cyclophosphamide, methotrexate, quinine, pyrazinamide, and related compounds, although the strength of clinical evidence differs by drug. Medication review with metabolic/pharmacology expertise is warranted. (cameron1993gouturicacid pages 6-8, cameron1993gouturicacid pages 1-2, salhen2013drosophilamelanogasteras pages 57-58)

Urinary alkalinization is **not established**: xanthine solubility is relatively pH-independent, and one experimental review states that alkalinization has no benefit, while some clinical reports call it controversial or possibly useful. It should not be represented as proven disease-modifying therapy. (grases2018xanthineurolithiasisinhibitors pages 1-2, policastro2018personalizedinterventionin pages 3-5)

Theobromine metabolites 3- and 7-methylxanthine inhibited xanthine crystallization in synthetic urine, but this is in-vitro evidence only; the authors explicitly called for clinical trials. It is not recommended therapy. (grases2018xanthineurolithiasisinhibitors pages 1-2)

### Research study

**NCT06092346**, initiated **19 December 2023**, is a recruiting NIH/NHGRI prospective observational natural-history study of purine and pyrimidine metabolism disorders, explicitly including XDH-associated xanthinuria type I. Planned enrollment is 999 participants aged ≥1 month, including affected people, family members, and healthy volunteers. It collects genomic, clinical, laboratory, pharmacological, imaging, microbiome, nutritional, quality-of-life, functional, hospitalization, and survival data at the NIH Clinical Center in Bethesda. It tests no treatment but is the most relevant current real-world research implementation. URL: https://clinicaltrials.gov/study/NCT06092346. (NCT06092346 chunk 1, NCT06092346 chunk 2)

---

## 13. Prevention

- **Primary prevention:** the disease itself cannot be prevented after conception except through reproductive options following familial variant identification—carrier testing, prenatal diagnosis, or preimplantation genetic testing. Genetic counseling is indicated.
- **Secondary prevention:** cascade testing and evaluation of unexplained persistent hypouricemia can identify presymptomatic relatives before stones occur.
- **Tertiary prevention:** hydration, purine restriction, avoidance of dehydration, medication review—especially in type II—and surveillance for stones and renal dysfunction aim to prevent obstruction and kidney damage.
- Vaccination, infectious prophylaxis, and population-wide screening have no disease-specific role. (abal2021identificationofa pages 1-2, peretz2021classicalxanthinuriain pages 2-4)

---

## 14. Natural disease in other species

Natural or inherited xanthinuria has comparative relevance in animals. A bovine MOCOS/MCS deletion, **c.769_771delTAC (p.Tyr257del)**, causes type-II-like xanthinuria, urinary xanthine accumulation, growth arrest, and death at approximately six months. Drosophila **rosy** mutants disrupt the XDH ortholog and are useful for enzyme-domain and stress studies, but their prominent eye-pigment phenotype poorly models human renal stone disease. (salhen2013drosophilamelanogasteras pages 57-58)

Recent feline and canine reports exist in the search record, including familial Munchkin-cat xanthinuria and multiple canine XDH/MOCOS variants, but full text suitable for evidence extraction was unavailable; breed, VBO, exact variant, and frequency annotations should therefore be curated directly from those veterinary primary papers rather than inferred here. There is no zoonotic potential or cross-species transmission: these are inherited metabolic defects.

---

## 15. Model organisms and experimental systems

The ENU-derived **RENF mouse** carries homozygous **Xdh p.Glu26Ter**. By four weeks, mice have growth impairment, elevated urea/creatinine, small irregular kidneys, intratubular casts, interstitial inflammation and fibrosis, and extensive tubular apoptosis. The model reproduces biochemical xanthinuria and renal injury but is substantially more severe than typical human disease. (piret2012amousemodel pages 1-2, piret2012amousemodel pages 4-8)

A major translational advance published in 2025 showed why. Mice retain intestinal **Slc23a4**, whereas the human gene is pseudogenized. Combining high Hprt activity, Xdh knockout, and Slc23a4 knockout extended median survival to **191.8 days**, versus **64.05** and **83.3 days** on heterozygous and wild-type Slc23a4 backgrounds. Nevertheless, rescued mice had renal impairment, anemia, reproductive abnormalities, and urinary xanthine excretion approximately 20-fold greater than human type-I patients. A low-purine diet reduced urinary xanthine from **3.761 ± 0.299** to **1.520 ± 0.260 mol/mol creatinine**. This is a useful adult model but not a faithful quantitative replica of human disease. (terada2025pseudogenizationofthe pages 2-3, terada2025pseudogenizationofthe pages 1-2)

Additional systems include Arabidopsis XDH expressed in *Pichia pastoris* and recombinant human MOCOS domains expressed in *E. coli*. They are valuable for variant-function classification but cannot model human stone formation, renal physiology, penetrance, or quality of life. (peretz2021classicalxanthinuriain pages 14-16)

---

## Current expert assessment and research priorities

The strongest current interpretation is that hereditary xanthinuria is underdiagnosed because profound hypouricemia is often ignored and many affected people are asymptomatic. Persistent low serum urate combined with low urinary urate should prompt direct xanthine/hypoxanthine measurement and XDH/MOCOS testing. The major unmet needs are prospective natural-history data, population prevalence, standardized biochemical thresholds, systematic ClinVar/gnomAD variant curation, genotype–phenotype analysis, validated hydration/diet targets, type-II pharmacokinetic studies, and human-relevant renal organoid or cellular models. The NIH natural-history protocol is positioned to address several of these gaps. (abal2021identificationofa pages 1-2, NCT06092346 chunk 1, NCT06092346 chunk 2)

### Representative abstract language

- Peretz et al. (published **7 July 2021**) reported: **“Seven out of 20 affected individuals (35%) presented with xanthinuria-related symptoms of varied severity.”** DOI/URL: https://doi.org/10.3390/biomedicines9070788. (peretz2021classicalxanthinuriain pages 1-2)
- Abal et al. (published online **21 July 2021**) concluded that hereditary xanthinuria is **“an underdiagnosed pathology, often found in a routine analysis that shows hypouricemia.”** DOI/URL: https://doi.org/10.1515/almed-2021-0018. (abal2021identificationofa pages 1-2)
- The 2024 childhood-nephrolithiasis review identifies **XDH** and **MOCOS** as the genetic causes of autosomal-recessive xanthinuria types I and II and recognizes xanthine nephrolithiasis and possible ESKD. Published **March 2024**; DOI/URL: https://doi.org/10.3389/fgene.2024.1381174. (gefen2024reviewofchildhood pages 15-16)

PMIDs were not present in the retrieved full-text metadata for the principal sources and are therefore not fabricated here; DOI URLs provide persistent source resolution.

References

1. (peretz2021classicalxanthinuriain pages 1-2): Hava Peretz, Ayala Lagziel, Florian Bittner, Mustafa Kabha, Meirav Shtauber-Naamati, Vicki Zhuravel, Sali Usher, Steffen Rump, Silke Wollers, Bettina Bork, Hanna Mandel, Tzipora Falik-Zaccai, Limor Kalfon, Juergen Graessler, Avraham Zeharia, Nasser Heib, Hannah Shalev, Daniel Landau, and David Levartovsky. Classical xanthinuria in nine israeli families and two isolated cases from germany: molecular, biochemical and population genetics aspects. Jul 2021. URL: https://doi.org/10.3390/biomedicines9070788, doi:10.3390/biomedicines9070788. This article has 12 citations.

2. (peretz2021classicalxanthinuriain pages 18-19): Hava Peretz, Ayala Lagziel, Florian Bittner, Mustafa Kabha, Meirav Shtauber-Naamati, Vicki Zhuravel, Sali Usher, Steffen Rump, Silke Wollers, Bettina Bork, Hanna Mandel, Tzipora Falik-Zaccai, Limor Kalfon, Juergen Graessler, Avraham Zeharia, Nasser Heib, Hannah Shalev, Daniel Landau, and David Levartovsky. Classical xanthinuria in nine israeli families and two isolated cases from germany: molecular, biochemical and population genetics aspects. Jul 2021. URL: https://doi.org/10.3390/biomedicines9070788, doi:10.3390/biomedicines9070788. This article has 12 citations.

3. (peretz2021classicalxanthinuriain pages 2-4): Hava Peretz, Ayala Lagziel, Florian Bittner, Mustafa Kabha, Meirav Shtauber-Naamati, Vicki Zhuravel, Sali Usher, Steffen Rump, Silke Wollers, Bettina Bork, Hanna Mandel, Tzipora Falik-Zaccai, Limor Kalfon, Juergen Graessler, Avraham Zeharia, Nasser Heib, Hannah Shalev, Daniel Landau, and David Levartovsky. Classical xanthinuria in nine israeli families and two isolated cases from germany: molecular, biochemical and population genetics aspects. Jul 2021. URL: https://doi.org/10.3390/biomedicines9070788, doi:10.3390/biomedicines9070788. This article has 12 citations.

4. (gefen2024reviewofchildhood pages 15-16): Ashley M. Gefen and Joshua J. Zaritsky. Review of childhood genetic nephrolithiasis and nephrocalcinosis. Frontiers in Genetics, Mar 2024. URL: https://doi.org/10.3389/fgene.2024.1381174, doi:10.3389/fgene.2024.1381174. This article has 14 citations and is from a peer-reviewed journal.

5. (ichida2012mutationsassociatedwith pages 1-3): Kimiyoshi Ichida, Yoshihiro Amaya, Ken Okamoto, and Takeshi Nishino. Mutations associated with functional disorder of xanthine oxidoreductase and hereditary xanthinuria in humans. International Journal of Molecular Sciences, 13:15475-15495, Nov 2012. URL: https://doi.org/10.3390/ijms131115475, doi:10.3390/ijms131115475. This article has 145 citations.

6. (abal2021identificationofa pages 1-2): Cristina Collazo Abal, Susana Romero Santos, Carmen González Mao, Emilio C. Pazos Lago, Francisco Barros Angueira, and Daisy Castiñeiras Ramos. Identification of a new mutation in the human xanthine dehydrogenase responsible for xanthinuria type i. Advances in Laboratory Medicine, 2:567-570, Jul 2021. URL: https://doi.org/10.1515/almed-2021-0018, doi:10.1515/almed-2021-0018. This article has 4 citations.

7. (cameron1993gouturicacid pages 6-8): J. S. Cameron, F. Moro, and H. A. Simmonds. Gout, uric acid and purine metabolism in paediatric nephrology. Pediatric Nephrology, 7:105-118, Feb 1993. URL: https://doi.org/10.1007/bf00861588, doi:10.1007/bf00861588. This article has 271 citations and is from a domain leading peer-reviewed journal.

8. (grases2018xanthineurolithiasisinhibitors pages 1-2): Felix Grases, Antonia Costa-Bauza, Joan Roig, and Adrian Rodriguez. Xanthine urolithiasis: inhibitors of xanthine crystallization. Aug 2018. URL: https://doi.org/10.1371/journal.pone.0198881, doi:10.1371/journal.pone.0198881. This article has 21 citations and is from a peer-reviewed journal.

9. (cameron1993gouturicacid pages 1-2): J. S. Cameron, F. Moro, and H. A. Simmonds. Gout, uric acid and purine metabolism in paediatric nephrology. Pediatric Nephrology, 7:105-118, Feb 1993. URL: https://doi.org/10.1007/bf00861588, doi:10.1007/bf00861588. This article has 271 citations and is from a domain leading peer-reviewed journal.

10. (NCT06092346 chunk 1):  A Natural History Study Seeks to Understand the Clinical, Genomic, Pharmacological, Laboratory, and Dietary Determinates of Pyrimidine and Purine Metabolism Disorders. National Human Genome Research Institute (NHGRI). 2023. ClinicalTrials.gov Identifier: NCT06092346

11. (peretz2021classicalxanthinuriain pages 5-8): Hava Peretz, Ayala Lagziel, Florian Bittner, Mustafa Kabha, Meirav Shtauber-Naamati, Vicki Zhuravel, Sali Usher, Steffen Rump, Silke Wollers, Bettina Bork, Hanna Mandel, Tzipora Falik-Zaccai, Limor Kalfon, Juergen Graessler, Avraham Zeharia, Nasser Heib, Hannah Shalev, Daniel Landau, and David Levartovsky. Classical xanthinuria in nine israeli families and two isolated cases from germany: molecular, biochemical and population genetics aspects. Jul 2021. URL: https://doi.org/10.3390/biomedicines9070788, doi:10.3390/biomedicines9070788. This article has 12 citations.

12. (peretz2021classicalxanthinuriain pages 8-9): Hava Peretz, Ayala Lagziel, Florian Bittner, Mustafa Kabha, Meirav Shtauber-Naamati, Vicki Zhuravel, Sali Usher, Steffen Rump, Silke Wollers, Bettina Bork, Hanna Mandel, Tzipora Falik-Zaccai, Limor Kalfon, Juergen Graessler, Avraham Zeharia, Nasser Heib, Hannah Shalev, Daniel Landau, and David Levartovsky. Classical xanthinuria in nine israeli families and two isolated cases from germany: molecular, biochemical and population genetics aspects. Jul 2021. URL: https://doi.org/10.3390/biomedicines9070788, doi:10.3390/biomedicines9070788. This article has 12 citations.

13. (terada2025pseudogenizationofthe pages 2-3): Kazuki Terada, Tamaki Watanabe, Nobuhiro Yasuno, Toshio Ohtsubo, Shigeru Shibata, Kimiyoshi Ichida, and Makoto Hosoyamada. Pseudogenization of the slc23a4 gene is necessary for the survival of xdh-deficient mice. Scientific Reports, Jan 2025. URL: https://doi.org/10.1038/s41598-025-87751-9, doi:10.1038/s41598-025-87751-9. This article has 4 citations and is from a peer-reviewed journal.

14. (terada2025pseudogenizationofthe pages 1-2): Kazuki Terada, Tamaki Watanabe, Nobuhiro Yasuno, Toshio Ohtsubo, Shigeru Shibata, Kimiyoshi Ichida, and Makoto Hosoyamada. Pseudogenization of the slc23a4 gene is necessary for the survival of xdh-deficient mice. Scientific Reports, Jan 2025. URL: https://doi.org/10.1038/s41598-025-87751-9, doi:10.1038/s41598-025-87751-9. This article has 4 citations and is from a peer-reviewed journal.

15. (peretz2021classicalxanthinuriain pages 19-20): Hava Peretz, Ayala Lagziel, Florian Bittner, Mustafa Kabha, Meirav Shtauber-Naamati, Vicki Zhuravel, Sali Usher, Steffen Rump, Silke Wollers, Bettina Bork, Hanna Mandel, Tzipora Falik-Zaccai, Limor Kalfon, Juergen Graessler, Avraham Zeharia, Nasser Heib, Hannah Shalev, Daniel Landau, and David Levartovsky. Classical xanthinuria in nine israeli families and two isolated cases from germany: molecular, biochemical and population genetics aspects. Jul 2021. URL: https://doi.org/10.3390/biomedicines9070788, doi:10.3390/biomedicines9070788. This article has 12 citations.

16. (peretz2021classicalxanthinuriain pages 14-16): Hava Peretz, Ayala Lagziel, Florian Bittner, Mustafa Kabha, Meirav Shtauber-Naamati, Vicki Zhuravel, Sali Usher, Steffen Rump, Silke Wollers, Bettina Bork, Hanna Mandel, Tzipora Falik-Zaccai, Limor Kalfon, Juergen Graessler, Avraham Zeharia, Nasser Heib, Hannah Shalev, Daniel Landau, and David Levartovsky. Classical xanthinuria in nine israeli families and two isolated cases from germany: molecular, biochemical and population genetics aspects. Jul 2021. URL: https://doi.org/10.3390/biomedicines9070788, doi:10.3390/biomedicines9070788. This article has 12 citations.

17. (patil2025xanthinestonesin pages 2-4): Siddanagouda B. Patil, Vinay S. Kundargi, Santosh Patil, Basavesh S. Patil, Manoj K. Vaidya, and Gurushantappa S. Kadakol. Xanthine stones in an infant: a case report and clinical insights. Journal of Urological Surgery, Apr 2025. URL: https://doi.org/10.4274/jus.galenos.2024.2024-8-9, doi:10.4274/jus.galenos.2024.2024-8-9. This article has 0 citations.

18. (piret2012amousemodel pages 4-8): Sian E. Piret, Christopher T. Esapa, Caroline M. Gorvin, Rosie Head, Nellie Y. Loh, Olivier Devuyst, Gethin Thomas, Steve D. M. Brown, Matthew Brown, Peter Croucher, Roger Cox, and Rajesh V. Thakker. A mouse model of early-onset renal failure due to a xanthine dehydrogenase nonsense mutation. PLoS ONE, 7:e45217, Sep 2012. URL: https://doi.org/10.1371/journal.pone.0045217, doi:10.1371/journal.pone.0045217. This article has 15 citations and is from a peer-reviewed journal.

19. (salhen2013drosophilamelanogasteras pages 57-58): KS Al Salhen. Drosophila melanogaster as a model for molybdo-flavoenzyme mediated protection against chemical and physical stress. Unknown journal, 2013.

20. (policastro2018personalizedinterventionin pages 3-5): Lucas J. Policastro, Subodh J. Saggi, David S. Goldfarb, and Jeffrey P. Weiss. Personalized intervention in monogenic stone formers. Mar 2018. URL: https://doi.org/10.1016/j.juro.2017.09.143, doi:10.1016/j.juro.2017.09.143. This article has 38 citations and is from a domain leading peer-reviewed journal.

21. (NCT06092346 chunk 2):  A Natural History Study Seeks to Understand the Clinical, Genomic, Pharmacological, Laboratory, and Dietary Determinates of Pyrimidine and Purine Metabolism Disorders. National Human Genome Research Institute (NHGRI). 2023. ClinicalTrials.gov Identifier: NCT06092346

22. (piret2012amousemodel pages 1-2): Sian E. Piret, Christopher T. Esapa, Caroline M. Gorvin, Rosie Head, Nellie Y. Loh, Olivier Devuyst, Gethin Thomas, Steve D. M. Brown, Matthew Brown, Peter Croucher, Roger Cox, and Rajesh V. Thakker. A mouse model of early-onset renal failure due to a xanthine dehydrogenase nonsense mutation. PLoS ONE, 7:e45217, Sep 2012. URL: https://doi.org/10.1371/journal.pone.0045217, doi:10.1371/journal.pone.0045217. This article has 15 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hereditary_Xanthinuria-deep-research-falcon_artifacts/artifact-00.md)