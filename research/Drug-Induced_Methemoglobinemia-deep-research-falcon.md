---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T14:09:54.724101'
end_time: '2026-09-02T14:20:12.264567'
duration_seconds: 617.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Drug-Induced Methemoglobinemia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 48
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Drug-Induced_Methemoglobinemia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Drug-Induced Methemoglobinemia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Drug-Induced Methemoglobinemia** covering all of the
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
- **Disease Name:** Drug-Induced Methemoglobinemia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Drug-Induced Methemoglobinemia** covering all of the
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


# Drug-Induced Methemoglobinemia: Disease-Characteristics Research Report

**Scope.** This report treats drug-induced methemoglobinemia as an **acquired toxic/iatrogenic dyshemoglobinemia**, not as congenital CYB5R3 deficiency or hemoglobin-M disease. Evidence is principally aggregated disease-level literature, hospital cohorts, trials, and case series; the 2024 Iowa study used de-identified individual medical-record data aggregated at cohort level. No patient-specific EHR data were supplied for this report. (iolascon2021recommendationsfordiagnosis pages 1-3, belzer2024causesofacquired pages 1-2)

## Executive summary

Drug-induced methemoglobinemia occurs when a medication or reactive metabolite oxidizes hemoglobin iron from oxygen-binding ferrous Fe²⁺ to ferric Fe³⁺ faster than erythrocyte reduction systems can restore it. Ferric heme cannot bind oxygen, while oxidation also increases oxygen affinity at the remaining ferrous hemes, producing functional anemia and impaired tissue unloading despite a normal arterial oxygen tension. It is usually acute, reversible, and exposure-dependent, but dapsone and lipophilic agents can produce delayed or recurrent toxicity. (iolascon2021recommendationsfordiagnosis pages 1-3, belzer2024causesofacquired pages 1-2, iolascon2021recommendationsfordiagnosis pages 9-10)

The strongest recent epidemiologic evidence is a 2024 single-center retrospective study: among 21,449 measurements from 2,502 patients during 2009–2023, 546 measurements (2.5%) were ≥3.1% MetHb and 33 (0.15%) were ≥10%. Dapsone caused 67.0% of pediatric and 63.6% of adult elevated-MetHb encounters; inhaled nitric oxide caused 16.5% and 12.8%, respectively. These are proportions among tested hospital patients, **not population incidence estimates**. (belzer2024causesofacquired pages 1-2, belzer2024causesofacquired pages 3-4, belzer2024causesofacquired pages 2-3)

The operational clinical summary is provided below.

| Domain | High-value finding | Quantitative threshold/data | Ontology suggestion |
|---|---|---|---|
| Normal physiology | Methemoglobin (MetHb) is continuously generated but normally reduced within erythrocytes | Usually **<1%–2% of total hemoglobin** | GO:0019825 oxygen binding; CL:0000232 erythrocyte |
| Severity: minimal | Low pulse-oximeter readings or pale, gray, or blue skin may occur; patients are generally asymptomatic | **MetHb <10%** | HP:0012418 hypoxemia; HP:0032239 abnormal blood oxygen level |
| Severity: mild | Cyanosis and dark-brown or chocolate-colored blood; asymptomatic status or confusion is possible | **MetHb 10%–30%** | HP:0000961 cyanosis; HP:0001289 confusion |
| Severity: moderate | Functional anemia causes dyspnea, dizziness, syncope, chest pain, palpitations, headache, and fatigue | **MetHb 30%–50%** | HP:0002094 dyspnea; HP:0002321 vertigo; HP:0001279 syncope; HP:0001695 palpitations; HP:0002315 headache; HP:0012378 fatigue |
| Severity: severe | Tachypnea, metabolic acidosis, dysrhythmia, seizure, delirium, or coma may develop | **MetHb 50%–70%** | HP:0002789 tachypnea; HP:0001942 metabolic acidosis; HP:0011675 arrhythmia; HP:0001250 seizure; HP:0001259 coma |
| Severity: potentially fatal | Profound tissue hypoxia and death; urgent rescue treatment is required | **MetHb >70%** | HP:0012418 hypoxemia; GO:0070482 response to oxygen levels |
| Diagnostic clue | Suspect when cyanosis or low SpO₂ fails to correct with supplemental oxygen despite a normal or high PaO₂ | SpO₂ often trends toward **~85%**; a **saturation gap >5%** is suggestive | HP:0000961 cyanosis; HP:0012418 hypoxemia |
| Confirmatory test | Multiwavelength blood co-oximetry directly quantifies MetHb and is preferred over conventional pulse oximetry | Report MetHb as **percentage of total hemoglobin**; arterial or venous blood may be used | LOINC: methemoglobin/total hemoglobin in blood; NCIT: C111159 Co-Oximetry |
| Visual finding | Blood remains chocolate-brown rather than becoming red after oxygen exposure | Commonly apparent with clinically important MetHb, often **>10%–20%** | HP:0031816 abnormal blood color |
| Key drug triggers | Dapsone, benzocaine, prilocaine, lidocaine, phenazopyridine, primaquine/chloroquine, sulfonamides, rasburicase, metoclopramide, nitroglycerin, nitroprusside, and inhaled nitric oxide | Risk is exposure- and dose-dependent; dapsone and inhaled nitric oxide predominate in monitored hospital populations | CHEBI terms for individual oxidants; NCIT: Pharmacologic Substance |
| Other triggers | Sodium/amyl/isobutyl nitrite, nitrate-contaminated food or water, aniline/nitrobenzene, chlorates, pesticides, smoke inhalation, and some recreational-drug adulterants | Intentional nitrite ingestion can produce **MetHb >30%** and fatal poisoning | CHEBI:16301 nitrite; CHEBI:17632 nitrate; NCIT: Environmental Exposure |
| Initial management | Stop or remove the oxidant, administer oxygen, obtain IV access, correct acidosis/hypoglycemia, and provide cardiopulmonary or seizure support as required | Treat the patient immediately when unstable; do not delay care while distinguishing acquired from hereditary disease | NCIT: C71943 Supportive Care; NCIT: Oxygen Therapy |
| Treatment threshold | Methylene blue is indicated for symptomatic acquired disease and for high levels even without symptoms; lower thresholds apply when oxygen delivery is already compromised | Common thresholds: **≥20% if symptomatic** or **≥30% if asymptomatic**; consider treatment near **10%** with severe anemia or cardiac/pulmonary disease | NCIT: Methylene Blue Treatment; CHEBI:6872 methylene blue |
| First-line antidote | IV methylene blue accepts electrons from NADPH; leukomethylene blue reduces ferric Fe³⁺ back to ferrous Fe²⁺ in erythrocytes | **1–2 mg/kg IV over 3–5 min** | CHEBI:6872 methylene blue; GO:0055114 oxidation-reduction process |
| Repeat and maximum dosing | Repeat only if clinical findings or MetHb fail to improve; excessive dosing can worsen MetHb and cause hemolysis | Repeat **1 mg/kg after 30–60 min**; avoid cumulative doses **>5.5–7 mg/kg** | NCIT: Repeat Dose; HP:0001878 hemolytic anemia |
| G6PD caution | Methylene blue may be ineffective and can provoke oxidative hemolysis because NADPH generation is impaired | Avoid when G6PD deficiency is known; rapidly weigh risk versus benefit in life-threatening poisoning | HP:0001878 hemolytic anemia; GO:0004345 glucose-6-phosphate dehydrogenase activity; CL:0000232 erythrocyte |
| Serotonergic-drug caution | Methylene blue inhibits monoamine oxidase A and may precipitate serotonin syndrome with serotonergic medicines | Review SSRIs, SNRIs, MAO inhibitors, and other serotonergic agents before administration when feasible | HP:0011447 serotonin syndrome; GO:0004491 monoamine oxidase activity |
| Alternative or adjunctive therapy | Ascorbic acid reduces MetHb nonenzymatically but acts more slowly; dosing is not standardized | Often requires **≥24 h**; reported adult regimens vary from **0.5 g every 12 h** to larger IV doses | CHEBI:29073 L-ascorbic acid; GO:0016209 antioxidant activity |
| Refractory disease | Exchange transfusion, red-cell transfusion, or hyperbaric oxygen may be used when methylene blue is contraindicated or ineffective | Therapeutic whole-blood exchange has reported **81.6% survival** in methylene-blue-refractory cases | NCIT: C15283 Exchange Transfusion; NCIT: C135060 Hyperbaric Oxygen Therapy |
| Rebound monitoring | Long-acting or lipophilic oxidants can cause recurrent MetHb after an initial response; dapsone is especially important because of active metabolites and enterohepatic recirculation | Rebound may occur for **up to 18 h**; dapsone cases may require repeat treatment every **6–8 h for 2–3 days** | NCIT: Therapeutic Drug Monitoring; HP:0031796 recurrent symptom |
| Clinical course | Most recognized and promptly treated episodes resolve completely after withdrawal of the trigger and restoration of functional hemoglobin | MetHb should decline substantially within **30–60 min** after effective methylene blue | MONDO: acquired methemoglobinemia; GO:0036293 response to decreased oxygen levels |


*Table: This table consolidates severity strata, diagnostic clues, common oxidant triggers, antidotal treatment, contraindications, rescue options, and rebound monitoring for drug-induced methemoglobinemia. It is based on expert recommendations, recent hospital data, and clinical reviews (iolascon2021recommendationsfordiagnosis pages 3-5, belzer2024causesofacquired pages 1-2, iolascon2021recommendationsfordiagnosis pages 9-10, iolascon2021recommendationsfordiagnosis pages 10-11, iolascon2021recommendationsfordiagnosis pages 8-9, cefalu2020methemoglobinemiainthe pages 6-8).*

## 1. Disease information

### Definition and names

Methemoglobinemia is an excess of hemoglobin containing ferric iron. Healthy blood generally contains <1%–2% MetHb. “Drug-induced methemoglobinemia” denotes an acquired form attributable to a medicine, medical gas, or its metabolite; overlapping labels include **acquired methemoglobinemia**, **toxic methemoglobinemia**, **toxin-induced methemoglobinemia**, **iatrogenic methemoglobinemia**, and British spellings *methaemoglobinaemia/methaemoglobinaemia*. (iolascon2021recommendationsfordiagnosis pages 5-6, belzer2024causesofacquired pages 1-2)

A concise authoritative abstract statement is: “Acquired forms are the most common, mainly due to the exposure to substances that cause oxidation of the Hb both directly or indirectly.” This comes from the European Hematology Association/EuroBloodNet consensus review, published September 2021 (DOI: [10.1002/ajh.26340](https://doi.org/10.1002/ajh.26340)). (iolascon2021recommendationsfordiagnosis pages 1-3)

### Identifiers

* **MeSH:** Methemoglobinemia, **D008708**. (NCT03542760 chunk 2)
* **ICD-10-CM:** D74.8, “Other methemoglobinemias,” is commonly applicable to acquired/drug-induced disease; D74.9 is unspecified methemoglobinemia. External terminology validation is advisable before production use.
* **ICD-11:** classified under methemoglobinaemias/blood disorders, but an exact drug-induced leaf code was not established from the retrieved evidence.
* **MONDO:** no confidently verified dedicated MONDO identifier for the drug-induced subtype was recovered. Map provisionally to the acquired-methemoglobinemia concept rather than congenital methemoglobinemia.
* **OMIM/Orphanet:** not generally appropriate as primary identifiers for this acquired adverse-drug reaction. OMIM entries for CYB5R3-related disease and HbM describe hereditary differentials, not the target entity.
* **Suggested ontology label:** “drug-induced methemoglobinemia,” parent “acquired methemoglobinemia”; add causal relations to the implicated CHEBI/RxNorm substance.

## 2. Etiology

### Causal agents

Prominent drug causes include **dapsone**, benzocaine, prilocaine, lidocaine, phenazopyridine, primaquine/chloroquine, sulfonamides including trimethoprim-sulfamethoxazole, rasburicase, metoclopramide, nitroglycerin, sodium nitroprusside, and inhaled nitric oxide. Less frequent reports involve acetaminophen overdose, phenacetin, nitrofurantoin, cyclophosphamide, flutamide, and even excessive methylene blue. Non-drug oxidants include sodium/amyl/isobutyl nitrite, nitrate-contaminated food or water, aniline/nitrobenzene, chlorates, pesticides, and smoke. (cefalu2020methemoglobinemiainthe pages 4-6, belzer2024causesofacquired pages 2-3, iolascon2021recommendationsfordiagnosis pages 11-12, cefalu2020methemoglobinemiainthe pages 8-10)

Dapsone is bioactivated to **dapsone hydroxylamine**, which oxidizes hemoglobin; enterohepatic recirculation and persistent metabolites explain prolonged or recurrent disease. Cimetidine can inhibit CYP-mediated hydroxylamine formation, but evidence supports neither routine acute use nor a universally accepted preventive regimen. (bai2024dapsoneinducedmethemoglobinemiain pages 3-4, barclay2011dapsoneinducedmethemoglobinemiaa pages 5-5, cefalu2020methemoglobinemiainthe pages 6-8)

### Risk factors

Risk reflects oxidant potency, dose, route, duration, and absorption. Topical benzocaine on mucosa and high-dose prilocaine are particularly recognized procedural risks. Infants have only approximately 50%–60% of adult erythrocyte CYB5R activity and more readily oxidized HbF. Older age, anemia, acidosis, sepsis, pregnancy, and cardiac, pulmonary, coronary, peripheral vascular, or cerebrovascular disease lower tolerance by reducing oxygen-delivery reserve. (belzer2024causesofacquired pages 2-3, cefalu2020methemoglobinemiainthe pages 3-4, iolascon2021recommendationsfordiagnosis pages 8-9)

**Genetic susceptibility** is not equivalent to genetic causation. G6PD deficiency impairs NADPH generation, increases oxidative-hemolysis risk, and can make methylene blue ineffective or harmful. Unrecognized CYB5R3 deficiency, HbM, or unstable globin variants may amplify or mimic an acquired episode. No validated GWAS susceptibility loci, penetrance estimate, polygenic score, or clinically established pharmacogenomic dosing algorithm was identified. (iolascon2021recommendationsfordiagnosis pages 3-5, iolascon2021recommendationsfordiagnosis pages 9-10)

### Protective factors and gene–environment interaction

Avoidance or dose limitation of oxidants, alternative local anesthetics, monitoring during dapsone or inhaled-NO therapy, and preservation of glucose/NADPH availability are practical protective factors. The clearest gene–environment interaction is oxidant exposure superimposed on G6PD or erythrocyte reductase deficiency. A CYB5R3 Thr117Ser polymorphism has been discussed in malaria/sickle-cell contexts, but it is not an established protective allele for drug-induced methemoglobinemia. No protective diet or lifestyle intervention has proven efficacy. (iolascon2021recommendationsfordiagnosis pages 3-5, iolascon2021recommendationsfordiagnosis pages 9-10, iolascon2021recommendationsfordiagnosis pages 11-12)

## 3. Phenotypes

Severity varies with MetHb percentage, rate of rise, hemoglobin concentration, comorbidity, and chronic adaptation. The consensus ranges are: <10%, usually asymptomatic with low oximeter readings or gray/blue color; 10%–30%, cyanosis and dark-brown blood, sometimes confusion; 30%–50%, dyspnea, dizziness, syncope, chest pain, palpitations, headache, and fatigue; 50%–70%, tachypnea, acidosis, dysrhythmia, seizure, delirium, or coma; >70%, profound hypoxia and high mortality. (iolascon2021recommendationsfordiagnosis pages 3-5, belzer2024causesofacquired pages 2-3)

Suggested HPO mappings include **Cyanosis HP:0000961**, Dyspnea HP:0002094, Headache HP:0002315, Fatigue HP:0012378, Syncope HP:0001279, Palpitations HP:0001695, Metabolic acidosis HP:0001942, Seizure HP:0001250, Coma HP:0001259, Hemolytic anemia HP:0001878, and hypoxemia/abnormal blood oxygenation. Chocolate-brown blood is best represented as an abnormal blood-color finding if the local terminology supports it.

Onset is possible at any age and is ordinarily abrupt after exposure. Manifestations are episodic and exposure-linked, rather than developmentally progressive. Quality-of-life instruments specific to this condition have not been validated; acute dyspnea, fatigue, confusion, intensive-care admission, and interruption of necessary dapsone therapy are the principal functional burdens. In the 2024 cohort, 68.7% of pediatric and 37.4% of adult elevated-MetHb encounters were asymptomatic, reflecting surveillance of treated patients. (belzer2024causesofacquired pages 4-5)

## 4. Genetic and molecular information

There is **no single causal gene** for the acquired target disease and no characteristic germline, somatic, chromosomal, or epigenetic lesion. Accordingly, pathogenic-variant classification, allele frequency, anticipation, mosaicism, and founder effects are not applicable to uncomplicated drug-induced disease.

Genes relevant to susceptibility and differential diagnosis are:

* **G6PD**: reduced NADPH supply and increased oxidative hemolysis; X-linked deficiency modifies treatment safety.
* **CYB5R3**: biallelic loss-of-function causes autosomal-recessive congenital methemoglobinemia, with >80 disease-causing variants reported by 2020; it is a differential, not the usual cause of an acquired event.
* **CYB5A** and globin genes **HBA1, HBA2, HBB, HBG1, HBG2**: rare hereditary methemoglobinemias/HbM differentials. (iolascon2021recommendationsfordiagnosis pages 1-3, iolascon2021recommendationsfordiagnosis pages 3-5)

Routine WES, WGS, CMA, karyotyping, FISH, mtDNA, or repeat-expansion testing has no role after a clear exposure-linked, resolving episode. Consider CYB5R activity and targeted CYB5R3/globin sequencing when cyanosis predates exposure, persists after drug withdrawal, recurs without oxidants, or clusters in a family. (iolascon2021recommendationsfordiagnosis pages 5-6, iolascon2021recommendationsfordiagnosis pages 8-9)

## 5. Environmental information

Relevant environments include endoscopy/anesthesia and dental settings using topical/local anesthetics; ICUs using inhaled nitric oxide or nitroprusside; oncology/transplant settings using dapsone or rasburicase; recreational “poppers” or adulterated cocaine; and occupational/agricultural exposure to anilines, nitrobenzene, chlorates, pesticides, and nitrate-contaminated water. Tobacco, alcohol, exercise, and ordinary diet are not established independent causes, although smoking-related cardiorespiratory disease may reduce physiologic reserve. (belzer2024causesofacquired pages 2-3, iolascon2021recommendationsfordiagnosis pages 11-12)

Infections do not generally act as transmissible causes. Sepsis and infant gastroenteritis may increase endogenous nitric oxide/nitrite production or acidosis and thereby trigger MetHb formation. These are physiologic cofactors, not evidence of a pathogen-specific methemoglobinemia. (belzer2024causesofacquired pages 2-3, iolascon2021recommendationsfordiagnosis pages 8-9)

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Drug or reactive metabolite exposure leads to** oxidant delivery to circulating erythrocytes.
2. **Oxidant stress leads to** conversion of heme Fe²⁺ to Fe³⁺ faster than endogenous reduction can compensate.
3. **Fe³⁺ formation results in** heme sites that cannot bind oxygen.
4. **Oxidation of part of the hemoglobin tetramer also leads to** increased oxygen affinity at remaining Fe²⁺ sites—the Darling–Roughton effect—and a left-shifted dissociation curve.
5. **Both effects result in** reduced arterial oxygen-carrying capacity and impaired tissue oxygen unloading despite preserved dissolved oxygen and often normal/high PaO₂.
6. **Functional anemia leads to** compensatory tachycardia and tachypnea and then tissue hypoxia, headache, fatigue, dyspnea, and cyanosis.
7. **If oxidation continues or oxygen reserve is poor, tissue hypoxia leads to** lactate/metabolic acidosis, ischemia, dysrhythmia, seizures, coma, organ injury, and death.
8. **Branch—normal recovery:** erythrocyte NADH–cytochrome-b5 reductase and subsidiary NADPH-dependent pathways lead to reduction of Fe³⁺ back to Fe²⁺.
9. **Branch—treatment:** NADPH reduces methylene blue to leukomethylene blue, which leads to accelerated reduction of MetHb.
10. **Branch—susceptibility:** low CYB5R activity, G6PD deficiency, anemia, acidosis, or cardiorespiratory disease leads to faster accumulation or greater clinical severity; for some comorbid effects the magnitude is observational rather than experimentally demonstrated. (belzer2024causesofacquired pages 1-2, cefalu2020methemoglobinemiainthe pages 3-4, iolascon2021recommendationsfordiagnosis pages 9-10)

This is a redox/oxygen-transport disorder, not primarily a Wnt, MAPK, PI3K–AKT, mTOR, immune, apoptotic, or fibrotic disease. The initiating molecular lesion is oxidation within erythrocyte hemoglobin; downstream organ damage is hypoxic/ischemic. Suggested GO terms include oxidation–reduction process, oxygen binding, response to decreased oxygen levels, cellular response to hypoxia, and methemoglobin reductase activity. The principal Cell Ontology entity is **erythrocyte CL:0000232**. (belzer2024causesofacquired pages 1-2, mcnulty2022foodinducedmethemoglobinemiaa pages 1-1)

No reproducible disease-specific transcriptomic, proteomic, lipidomic, metabolomic, epigenomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics signature was identified. MetHb percentage itself is the direct biochemical phenotype.

## 7. Anatomical structures affected

The primary affected tissue is circulating blood, specifically hemoglobin in mature erythrocytes. The relevant subcellular context is erythrocyte cytosol and the heme prosthetic groups of hemoglobin; mature erythrocytes lack nuclei and mitochondria. Suggested terms include **UBERON:0000178 blood**, erythrocyte CL:0000232, hemoglobin complex, cytosol, and heme-binding site.

Secondary injury is systemic and proportional to oxygen demand: brain (confusion, seizure, coma), heart (angina, dysrhythmia, ischemia), skeletal muscle, kidney, and other organs may be affected by hypoxia. Lungs are not necessarily structurally diseased, explaining a normal PaO₂ despite cyanosis. There is no lateralization. (iolascon2021recommendationsfordiagnosis pages 3-5, cefalu2020methemoglobinemiainthe pages 1-3)

## 8. Temporal development

Onset is usually acute or subacute after exposure, with abrupt neurologic or cardiac symptoms distinguishing acquired disease from lifelong congenital cyanosis. Endogenous MetHb half-life has been estimated at approximately 55 minutes once oxidant input ceases. Effective methylene blue ordinarily lowers MetHb substantially within 30–60 minutes. (belzer2024causesofacquired pages 1-2, iolascon2021recommendationsfordiagnosis pages 9-10, iolascon2021recommendationsfordiagnosis pages 11-12)

The course is commonly self-limited after drug withdrawal, but dapsone can require treatment every 6–8 hours for 2–3 days. Rebound has been reported up to 18 hours after methylene blue, particularly with long-acting or lipophilic oxidants; one dapsone case fell from 25% to 7% and rebounded to 13.6% within six hours before a second dose. Serial co-oximetry is therefore important. (barclay2011dapsoneinducedmethemoglobinemiaa pages 5-6, iolascon2021recommendationsfordiagnosis pages 9-10, cefalu2020methemoglobinemiainthe pages 6-8)

## 9. Inheritance and population

Drug-induced methemoglobinemia is **not inherited**. Population prevalence and annual incidence are unknown because cases are sporadic, exposure-dependent, and under-recognized; no valid cases-per-100,000 estimate was found. There is no established sex ratio or ethnicity-specific incidence independent of exposure patterns and G6PD prevalence.

In the 2024 Iowa cohort, 303 unique patients had at least one result ≥3.1%, while only 27 had ≥10% during 2009–2023. Among ≥10% episodes across the longer dataset, causes included dapsone (40), benzocaine (10), recreational alkyl nitrites (3), sodium-nitrite suicide attempts (3, one fatal), nitrate-contaminated food (2), and sepsis (2). Severe intentional nitrite poisonings appear to be increasing with online availability, but this remains surveillance evidence rather than population incidence. (belzer2024causesofacquired pages 1-2, belzer2024causesofacquired pages 3-4, belzer2024causesofacquired pages 5-6)

## 10. Diagnostics

Diagnosis rests on exposure history, cyanosis or hypoxia refractory to oxygen, an SpO₂–SaO₂ “saturation gap,” chocolate-brown blood, and **multiwavelength co-oximetry**. Conventional two-wavelength pulse oximeters cannot quantify MetHb and tend toward approximately 85%; PaO₂ measures dissolved oxygen and can remain normal or high. A saturation gap >5% is suggestive but not diagnostic. Arterial or venous blood co-oximetry directly reports MetHb as a percentage of total hemoglobin. (cefalu2020methemoglobinemiainthe pages 1-3, rathod2024shadesofblue pages 2-3, bai2024dapsoneinducedmethemoglobinemiain pages 3-4)

Additional tests should include CBC/hemoglobin, blood gas and lactate, renal/hepatic function where relevant, ECG for severe disease, and hemolysis studies—reticulocytes, bilirubin, LDH, haptoglobin, smear/Heinz bodies—when dapsone, rasburicase, sulfonamides, or G6PD deficiency are plausible. Imaging, biopsy, EEG, and pulmonary-function testing are not diagnostic unless needed to evaluate competing pathology.

Differentials include cardiopulmonary hypoxemia/right-to-left shunt, carboxyhemoglobinemia, sulfhemoglobinemia, cyanide toxicity, peripheral vasoconstriction/artifact, congenital CYB5R3 deficiency, HbM, and unstable hemoglobin. Sulfhemoglobin is not reducible by methylene blue and can interfere with some measurements. Persistent lifelong/familial cyanosis favors hereditary disease. (iolascon2021recommendationsfordiagnosis pages 5-6, gehle2013atsdrcasestudies pages 81-87, bai2024dapsoneinducedmethemoglobinemiain pages 3-4)

There is no general-population or newborn screening program for the acquired disease. Targeted surveillance is used during dapsone and inhaled-NO treatment and in high-risk anesthesia settings. A completed prospective liposuction study followed 133 patients over 24 hours, and a pediatric dental study randomized 91 children to prilocaine, lidocaine, or no local anesthetic with continuous pulse co-oximetry. (NCT01766999 chunk 1, NCT01402869 chunk 1)

## 11. Outcome and prognosis

Promptly recognized disease generally resolves completely without chronic disability. A 2024 five-patient series reported peak MetHb of 16.6%–41%; four received methylene blue and all recovered. (rathod2024shadesofblue pages 3-5, rathod2024shadesofblue pages 2-3)

Risk rises sharply at 50%–70%, and >70% is potentially fatal, but level alone is imperfect because rate of rise, anemia, and cardiopulmonary reserve matter. In the food/nitrate systematic review, 97 articles described 568 cases, median MetHb 30%; 35 deaths occurred, 32 after accidental ingestion. Most patients survived even at levels up to 89% when methylene blue was administered, and methylene blue alone produced a mean 39.1-percentage-point fall among 22 evaluable cases. These data concern acquired food/nitrite poisoning and are supportive rather than drug-specific efficacy estimates. (mcnulty2022foodinducedmethemoglobinemiaa pages 1-1)

The Iowa cohort found no therapeutic-dose dapsone-attributed fatalities, whereas one of three sodium-nitrite suicide attempts was fatal. Death recorded during an encounter often reflected severe underlying illness rather than MetHb itself. No 5- or 10-year survival metric, chronic disability index, EQ-5D, SF-36, or validated prognostic model is applicable. (belzer2024causesofacquired pages 4-5, belzer2024causesofacquired pages 5-6)

## 12. Treatment

1. **Immediately stop/remove the oxidant.** Decontaminate safely when dermal/occupational exposure is continuing.
2. **Support oxygen delivery:** high-flow oxygen, IV access, glucose and correction of acidosis, fluids/pressors, ventilation, seizure treatment, and toxicology consultation as needed.
3. **Treat symptomatic patients** and generally asymptomatic patients with MetHb ≥30%; commonly cited thresholds are ≥20% when symptomatic and ≥30% when asymptomatic. Treat at approximately 10%–20% when severe anemia, cardiac/pulmonary disease, CO poisoning, infancy, or other limited reserve is present. (iolascon2021recommendationsfordiagnosis pages 10-11, iolascon2021recommendationsfordiagnosis pages 8-9)
4. **Methylene blue/methylthioninium chloride:** 1–2 mg/kg of 1% solution IV over 3–5 minutes; repeat approximately 1 mg/kg after 30–60 minutes if symptoms or MetHb persist. Avoid cumulative exposure above approximately 5.5–7 mg/kg because methylene blue itself becomes oxidizing and may worsen MetHb/hemolysis. Suggested annotations: CHEBI:6872; NCIT methylene-blue treatment/antidote therapy. (iolascon2021recommendationsfordiagnosis pages 9-10, iolascon2021recommendationsfordiagnosis pages 10-11, cefalu2020methemoglobinemiainthe pages 6-8)
5. **Major cautions:** known G6PD deficiency because of inadequate NADPH response and hemolysis; serotonergic medicines because methylene blue inhibits MAO-A and can precipitate serotonin syndrome; pregnancy because of reported teratogenicity; renal failure and certain anesthetic settings warrant caution. In immediately life-threatening toxicity, expert risk–benefit judgment is necessary rather than delaying all therapy for a G6PD result. (bai2024dapsoneinducedmethemoglobinemiain pages 3-4, iolascon2021recommendationsfordiagnosis pages 9-10, iolascon2021recommendationsfordiagnosis pages 8-9)
6. **Alternatives:** ascorbic acid directly reduces MetHb but is slower—often ≥24 hours—and dosing is not standardized. It is used when methylene blue is unavailable/contraindicated. Exchange transfusion, red-cell transfusion, or hyperbaric oxygen are rescue options; expert review cites 81.6% survival after therapeutic whole-blood exchange in methylene-blue-refractory cases. (mcnulty2022foodinducedmethemoglobinemiaa pages 3-3, iolascon2021recommendationsfordiagnosis pages 9-10, iolascon2021recommendationsfordiagnosis pages 10-11)
7. **Dapsone overdose:** serial MetHb/hemolysis monitoring and repeated treatment may be necessary. Multiple-dose activated charcoal shortened reported dapsone half-life from 77±23 to 12.7±0.7 hours, but requires toxicology guidance and airway safety. (barclay2011dapsoneinducedmethemoglobinemiaa pages 5-5)

There is no role for surgery, gene therapy, cell therapy, RNA therapy, or immunotherapy. Completed real-world implementation studies include the 24-person acquired-MetHb registry **NCT03542760** and the seven-person open-label Phase 4 ProvayBlue study **NCT03395223**, which used 1 mg/kg IV and permitted one repeat dose after an hour. Small enrollment underscores the rarity and limited prospective evidence base. (NCT03542760 chunk 1, NCT03395223 chunk 1)

## 13. Prevention

**Primary prevention:** maintain electronic medication alerts; avoid benzocaine/prilocaine or excessive doses in susceptible patients; calculate weight-based local-anesthetic exposure; review concurrent oxidants; use safer PCP-prophylaxis alternatives when appropriate; prevent nitrate/nitrite ingestion; regulate access and clearly label sodium nitrite; and use occupational controls/PPE for anilines and pesticides. (belzer2024causesofacquired pages 2-3, iolascon2021recommendationsfordiagnosis pages 11-12)

**Secondary prevention:** recognize the saturation gap early, obtain co-oximetry, and monitor MetHb during dapsone, inhaled nitric oxide, nitroprusside, and high-risk anesthesia. Routine dapsone monitoring in the Iowa center detected many asymptomatic cases and allowed dose reduction or discontinuation; only three dapsone patients required methylene blue. (belzer2024causesofacquired pages 3-4, belzer2024causesofacquired pages 5-6)

**Tertiary prevention:** document the culprit as a serious adverse drug reaction, avoid re-exposure, monitor for rebound for at least the expected pharmacologic window, and assess hemolysis where relevant. Vaccination and antimicrobial prophylaxis do not prevent the dyshemoglobinemia itself. Genetic counseling is unnecessary for an isolated acquired episode, but is appropriate if persistent/familial findings suggest hereditary disease.

## 14. Other species/natural disease

The conserved vertebrate mechanism—heme Fe²⁺ oxidation to Fe³⁺—occurs in mammals and birds. Veterinary cases can follow acetaminophen, local anesthetics, nitrates/nitrites, PAPP bait, and other oxidants; cats and dogs are especially relevant non-target species. This is not infectious and has no zoonotic transmission.

An in-vitro comparative study used blood from coyote (*Canis latrans*), California vole (*Microtus californicus*), feral swine (*Sus scrofa*), European starling (*Sturnus vulgaris*), and mallard (*Anas platyrhynchos*). Mammalian blood reached 100% MetHb at 15 mM sodium nitrite versus 200 mM for avian blood, while color values at a given MetHb fraction were similar enough to support a cross-species blood-spot diagnostic card. (patton2016detectingmethemoglobinemiain pages 1-2)

Acetaminophen studies indicate metabolic activation to p-aminophenol is important: at 500 µM p-aminophenol, canine and feline erythrocytes generated more MetHb than rat or mouse cells, plausibly reflecting lower NADH-methemoglobin-reductase and N-acetyltransferase detoxification. This makes species extrapolation imperfect. (mcconkey2007themechanismof pages 132-137)

## 15. Model organisms

Available models are chiefly **induced toxicology models**, not genetic replicas of the heterogeneous human exposure syndrome:

* **Ex-vivo blood oxidation:** sodium nitrite in mammalian and avian blood enables spectrophotometric/colorimetric assay development at the 635-nm MetHb absorption peak. Strength: direct and cross-species. Limitation: lacks metabolism, circulation, organ hypoxia, and treatment pharmacokinetics. (patton2016detectingmethemoglobinemiain pages 1-2)
* **Rat and Beagle-dog nitrite models:** single IM doses ≥100 mg/kg in rats and 60 mg/kg in dogs caused death/moribundity; repeated doses ≤30 and ≤10 mg/kg/day, respectively, were tolerated, with transient dose-dependent methemoglobinemia. These models characterize dose, time course, and systemic toxicity but involve nitrite rather than most human medicines. (miller2021safetyandtoxicology pages 1-2)
* **Canine/feline acetaminophen/p-aminophenol systems:** useful for metabolic activation, erythrocyte susceptibility, and veterinary toxicology; they do not reproduce dapsone or local-anesthetic pharmacology. (mcconkey2007themechanismof pages 132-137)
* **Naturally CYB5R-deficient dogs:** useful for hemoglobin-redox and methylene-blue studies, but model hereditary rather than drug-induced disease.

Suggested resources are MGI, RGD, ZFIN, OMIA, and NCBI Taxonomy. No standardized knockout, organoid, iPSC, or humanized model is required to diagnose or treat the acquired disease.

## Evidence appraisal and recent developments

The most consequential 2023–2024 development is improved quantitative description of real-world causes: the March/June 2024 Iowa study shows dapsone and iatrogenic nitric oxide dominate mild monitored cases, while intentional nitrite exposure and historical benzocaine use disproportionately contribute to severe episodes. It also documents institutional reduction in benzocaine-associated severe disease, consistent with prevention through changed procedural practice. (belzer2024causesofacquired pages 1-2, belzer2024causesofacquired pages 5-6)

Prospective evidence remains sparse. The FDA-requested Phase 4 study enrolled only seven patients, and the multicenter registry enrolled 24. Thus, expert recommendations appropriately rely on mechanism, observational cohorts, case series, and long clinical experience rather than randomized antidote trials. (NCT03542760 chunk 1, NCT03395223 chunk 1)

### Key sources and dates

* Belzer A, Krasowski MD. *Causes of acquired methemoglobinemia—a retrospective study at a large academic hospital.* **Available March 16, 2024; Toxicology Reports 2024.** DOI: [10.1016/j.toxrep.2024.03.004](https://doi.org/10.1016/j.toxrep.2024.03.004). Human retrospective cohort. (belzer2024causesofacquired pages 1-2)
* Rathod et al. *Shades of Blue: A Case Series of Acquired Methemoglobinemia.* **April 2024.** DOI: [10.7759/cureus.58312](https://doi.org/10.7759/cureus.58312). Human case series. (rathod2024shadesofblue pages 2-3)
* Iolascon et al. *Recommendations for diagnosis and treatment of methemoglobinemia.* **September 2021.** DOI: [10.1002/ajh.26340](https://doi.org/10.1002/ajh.26340). Systematic search plus >75% Delphi-like expert consensus. (iolascon2021recommendationsfordiagnosis pages 1-3)
* Cefalu et al. *Methemoglobinemia in the Operating Room and Intensive Care Unit.* **March 19, 2020.** DOI: [10.1007/s12325-020-01282-5](https://doi.org/10.1007/s12325-020-01282-5). Clinical review. (cefalu2020methemoglobinemiainthe pages 1-3)
* McNulty et al. *Food-induced methemoglobinemia: a systematic review.* **March 2022.** DOI: [10.1111/1750-3841.16090](https://doi.org/10.1111/1750-3841.16090). Systematic review of 568 human cases. (mcnulty2022foodinducedmethemoglobinemiaa pages 1-1)
* Historical primary clinical references with PMIDs include Wright et al., **PMID 10533013**; Ash-Bernal et al., 138-case series, **PMID 15342970**; Umbreit, **PMID 16986127**; Guay, 242 local-anesthetic episodes, **PMID 19224791**; and Vasters et al. on prilocaine risk factors, **PMID 16723054**. These PMIDs are supplied in the ClinicalTrials.gov bibliography and should be linked through `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`. (NCT01402869 chunk 1, NCT01402869 chunk 2)

**Knowledge gaps:** no reliable population prevalence/incidence, validated patient-reported outcome instrument, disease-specific omics signature, GWAS architecture, or adequately powered randomized antidote trial is available. Exact ontology identifiers for a dedicated drug-induced MONDO/ICD-11 subtype should be terminology-validated before database release.

References

1. (iolascon2021recommendationsfordiagnosis pages 1-3): Achille Iolascon, Paola Bianchi, Immacolata Andolfo, Roberta Russo, Wilma Barcellini, Elisa Fermo, Gergely Toldi, Stefano Ghirardello, David Rees, Richard Van Wijk, Antonis Kattamis, Patrick G. Gallagher, Noemi Roy, Ali Taher, Razan Mohty, Andreas Kulozik, Lucia De Franceschi, Antonella Gambale, Mariane De Montalembert, Gian Luca Forni, Cornelis L. Harteveld, and Josef Prchal. Recommendations for diagnosis and treatment of methemoglobinemia. Sep 2021. URL: https://doi.org/10.1002/ajh.26340, doi:10.1002/ajh.26340. This article has 319 citations and is from a domain leading peer-reviewed journal.

2. (belzer2024causesofacquired pages 1-2): Alex Belzer and Matthew D. Krasowski. Causes of acquired methemoglobinemia – a retrospective study at a large academic hospital. Jun 2024. URL: https://doi.org/10.1016/j.toxrep.2024.03.004, doi:10.1016/j.toxrep.2024.03.004. This article has 38 citations and is from a peer-reviewed journal.

3. (iolascon2021recommendationsfordiagnosis pages 9-10): Achille Iolascon, Paola Bianchi, Immacolata Andolfo, Roberta Russo, Wilma Barcellini, Elisa Fermo, Gergely Toldi, Stefano Ghirardello, David Rees, Richard Van Wijk, Antonis Kattamis, Patrick G. Gallagher, Noemi Roy, Ali Taher, Razan Mohty, Andreas Kulozik, Lucia De Franceschi, Antonella Gambale, Mariane De Montalembert, Gian Luca Forni, Cornelis L. Harteveld, and Josef Prchal. Recommendations for diagnosis and treatment of methemoglobinemia. Sep 2021. URL: https://doi.org/10.1002/ajh.26340, doi:10.1002/ajh.26340. This article has 319 citations and is from a domain leading peer-reviewed journal.

4. (belzer2024causesofacquired pages 3-4): Alex Belzer and Matthew D. Krasowski. Causes of acquired methemoglobinemia – a retrospective study at a large academic hospital. Jun 2024. URL: https://doi.org/10.1016/j.toxrep.2024.03.004, doi:10.1016/j.toxrep.2024.03.004. This article has 38 citations and is from a peer-reviewed journal.

5. (belzer2024causesofacquired pages 2-3): Alex Belzer and Matthew D. Krasowski. Causes of acquired methemoglobinemia – a retrospective study at a large academic hospital. Jun 2024. URL: https://doi.org/10.1016/j.toxrep.2024.03.004, doi:10.1016/j.toxrep.2024.03.004. This article has 38 citations and is from a peer-reviewed journal.

6. (iolascon2021recommendationsfordiagnosis pages 3-5): Achille Iolascon, Paola Bianchi, Immacolata Andolfo, Roberta Russo, Wilma Barcellini, Elisa Fermo, Gergely Toldi, Stefano Ghirardello, David Rees, Richard Van Wijk, Antonis Kattamis, Patrick G. Gallagher, Noemi Roy, Ali Taher, Razan Mohty, Andreas Kulozik, Lucia De Franceschi, Antonella Gambale, Mariane De Montalembert, Gian Luca Forni, Cornelis L. Harteveld, and Josef Prchal. Recommendations for diagnosis and treatment of methemoglobinemia. Sep 2021. URL: https://doi.org/10.1002/ajh.26340, doi:10.1002/ajh.26340. This article has 319 citations and is from a domain leading peer-reviewed journal.

7. (iolascon2021recommendationsfordiagnosis pages 10-11): Achille Iolascon, Paola Bianchi, Immacolata Andolfo, Roberta Russo, Wilma Barcellini, Elisa Fermo, Gergely Toldi, Stefano Ghirardello, David Rees, Richard Van Wijk, Antonis Kattamis, Patrick G. Gallagher, Noemi Roy, Ali Taher, Razan Mohty, Andreas Kulozik, Lucia De Franceschi, Antonella Gambale, Mariane De Montalembert, Gian Luca Forni, Cornelis L. Harteveld, and Josef Prchal. Recommendations for diagnosis and treatment of methemoglobinemia. Sep 2021. URL: https://doi.org/10.1002/ajh.26340, doi:10.1002/ajh.26340. This article has 319 citations and is from a domain leading peer-reviewed journal.

8. (iolascon2021recommendationsfordiagnosis pages 8-9): Achille Iolascon, Paola Bianchi, Immacolata Andolfo, Roberta Russo, Wilma Barcellini, Elisa Fermo, Gergely Toldi, Stefano Ghirardello, David Rees, Richard Van Wijk, Antonis Kattamis, Patrick G. Gallagher, Noemi Roy, Ali Taher, Razan Mohty, Andreas Kulozik, Lucia De Franceschi, Antonella Gambale, Mariane De Montalembert, Gian Luca Forni, Cornelis L. Harteveld, and Josef Prchal. Recommendations for diagnosis and treatment of methemoglobinemia. Sep 2021. URL: https://doi.org/10.1002/ajh.26340, doi:10.1002/ajh.26340. This article has 319 citations and is from a domain leading peer-reviewed journal.

9. (cefalu2020methemoglobinemiainthe pages 6-8): John N. Cefalu, Tejas V. Joshi, Matthew J. Spalitta, Carson J. Kadi, James H. Diaz, Jonathan P. Eskander, Elyse M. Cornett, and Alan D. Kaye. Methemoglobinemia in the operating room and intensive care unit: early recognition, pathophysiology, and management. Advances in Therapy, 37:1714-1723, Mar 2020. URL: https://doi.org/10.1007/s12325-020-01282-5, doi:10.1007/s12325-020-01282-5. This article has 104 citations and is from a peer-reviewed journal.

10. (iolascon2021recommendationsfordiagnosis pages 5-6): Achille Iolascon, Paola Bianchi, Immacolata Andolfo, Roberta Russo, Wilma Barcellini, Elisa Fermo, Gergely Toldi, Stefano Ghirardello, David Rees, Richard Van Wijk, Antonis Kattamis, Patrick G. Gallagher, Noemi Roy, Ali Taher, Razan Mohty, Andreas Kulozik, Lucia De Franceschi, Antonella Gambale, Mariane De Montalembert, Gian Luca Forni, Cornelis L. Harteveld, and Josef Prchal. Recommendations for diagnosis and treatment of methemoglobinemia. Sep 2021. URL: https://doi.org/10.1002/ajh.26340, doi:10.1002/ajh.26340. This article has 319 citations and is from a domain leading peer-reviewed journal.

11. (NCT03542760 chunk 2):  Acquired Methemoglobinemia Observational Registry. Hospital Quality Foundation. 2018. ClinicalTrials.gov Identifier: NCT03542760

12. (cefalu2020methemoglobinemiainthe pages 4-6): John N. Cefalu, Tejas V. Joshi, Matthew J. Spalitta, Carson J. Kadi, James H. Diaz, Jonathan P. Eskander, Elyse M. Cornett, and Alan D. Kaye. Methemoglobinemia in the operating room and intensive care unit: early recognition, pathophysiology, and management. Advances in Therapy, 37:1714-1723, Mar 2020. URL: https://doi.org/10.1007/s12325-020-01282-5, doi:10.1007/s12325-020-01282-5. This article has 104 citations and is from a peer-reviewed journal.

13. (iolascon2021recommendationsfordiagnosis pages 11-12): Achille Iolascon, Paola Bianchi, Immacolata Andolfo, Roberta Russo, Wilma Barcellini, Elisa Fermo, Gergely Toldi, Stefano Ghirardello, David Rees, Richard Van Wijk, Antonis Kattamis, Patrick G. Gallagher, Noemi Roy, Ali Taher, Razan Mohty, Andreas Kulozik, Lucia De Franceschi, Antonella Gambale, Mariane De Montalembert, Gian Luca Forni, Cornelis L. Harteveld, and Josef Prchal. Recommendations for diagnosis and treatment of methemoglobinemia. Sep 2021. URL: https://doi.org/10.1002/ajh.26340, doi:10.1002/ajh.26340. This article has 319 citations and is from a domain leading peer-reviewed journal.

14. (cefalu2020methemoglobinemiainthe pages 8-10): John N. Cefalu, Tejas V. Joshi, Matthew J. Spalitta, Carson J. Kadi, James H. Diaz, Jonathan P. Eskander, Elyse M. Cornett, and Alan D. Kaye. Methemoglobinemia in the operating room and intensive care unit: early recognition, pathophysiology, and management. Advances in Therapy, 37:1714-1723, Mar 2020. URL: https://doi.org/10.1007/s12325-020-01282-5, doi:10.1007/s12325-020-01282-5. This article has 104 citations and is from a peer-reviewed journal.

15. (bai2024dapsoneinducedmethemoglobinemiain pages 3-4): Sakshi Bai, Abraham Kisule, Bipneet Singh, Kavita Luthra, and Danesh Kumar. Dapsone-induced methemoglobinemia in a woman with multiple myeloma without glucose-6-phosphate dehydrogenase (g6pd) deficiency. Jun 2024. URL: https://doi.org/10.7759/cureus.63249, doi:10.7759/cureus.63249. This article has 3 citations.

16. (barclay2011dapsoneinducedmethemoglobinemiaa pages 5-5): James A Barclay, Stamatina E Ziemba, and Rami B Ibrahim. Dapsone-induced methemoglobinemia: a primer for clinicians. Annals of Pharmacotherapy, 45:1103-1115, Sep 2011. URL: https://doi.org/10.1345/aph.1q139, doi:10.1345/aph.1q139. This article has 101 citations and is from a peer-reviewed journal.

17. (cefalu2020methemoglobinemiainthe pages 3-4): John N. Cefalu, Tejas V. Joshi, Matthew J. Spalitta, Carson J. Kadi, James H. Diaz, Jonathan P. Eskander, Elyse M. Cornett, and Alan D. Kaye. Methemoglobinemia in the operating room and intensive care unit: early recognition, pathophysiology, and management. Advances in Therapy, 37:1714-1723, Mar 2020. URL: https://doi.org/10.1007/s12325-020-01282-5, doi:10.1007/s12325-020-01282-5. This article has 104 citations and is from a peer-reviewed journal.

18. (belzer2024causesofacquired pages 4-5): Alex Belzer and Matthew D. Krasowski. Causes of acquired methemoglobinemia – a retrospective study at a large academic hospital. Jun 2024. URL: https://doi.org/10.1016/j.toxrep.2024.03.004, doi:10.1016/j.toxrep.2024.03.004. This article has 38 citations and is from a peer-reviewed journal.

19. (mcnulty2022foodinducedmethemoglobinemiaa pages 1-1): Richard McNulty, Nikhil Kuchi, Elena Xu, and Naren Gunja. Food-induced methemoglobinemia: a systematic review. Journal of food science, 87 4:1423-1448, Mar 2022. URL: https://doi.org/10.1111/1750-3841.16090, doi:10.1111/1750-3841.16090. This article has 64 citations and is from a peer-reviewed journal.

20. (cefalu2020methemoglobinemiainthe pages 1-3): John N. Cefalu, Tejas V. Joshi, Matthew J. Spalitta, Carson J. Kadi, James H. Diaz, Jonathan P. Eskander, Elyse M. Cornett, and Alan D. Kaye. Methemoglobinemia in the operating room and intensive care unit: early recognition, pathophysiology, and management. Advances in Therapy, 37:1714-1723, Mar 2020. URL: https://doi.org/10.1007/s12325-020-01282-5, doi:10.1007/s12325-020-01282-5. This article has 104 citations and is from a peer-reviewed journal.

21. (barclay2011dapsoneinducedmethemoglobinemiaa pages 5-6): James A Barclay, Stamatina E Ziemba, and Rami B Ibrahim. Dapsone-induced methemoglobinemia: a primer for clinicians. Annals of Pharmacotherapy, 45:1103-1115, Sep 2011. URL: https://doi.org/10.1345/aph.1q139, doi:10.1345/aph.1q139. This article has 101 citations and is from a peer-reviewed journal.

22. (belzer2024causesofacquired pages 5-6): Alex Belzer and Matthew D. Krasowski. Causes of acquired methemoglobinemia – a retrospective study at a large academic hospital. Jun 2024. URL: https://doi.org/10.1016/j.toxrep.2024.03.004, doi:10.1016/j.toxrep.2024.03.004. This article has 38 citations and is from a peer-reviewed journal.

23. (rathod2024shadesofblue pages 2-3): Bharatsing D Rathod, Nilesh Kamble, Onkar Awadhiya, Udit Narang, Rajashree S Khot, and Sunita Kumbhalkar. Shades of blue: a case series of acquired methemoglobinemia. Apr 2024. URL: https://doi.org/10.7759/cureus.58312, doi:10.7759/cureus.58312. This article has 3 citations.

24. (gehle2013atsdrcasestudies pages 81-87): K Gehle. Atsdr case studies in environmental medicine: nitrate/nitrite toxicity. Unknown journal, 2013.

25. (NCT01766999 chunk 1): Hartmut Gehring. Methemoglobinemia After Liposuction - Diagnostic by Pulse Oximetry and Blood Gas Analysis.. University Hospital Schleswig-Holstein. 2008. ClinicalTrials.gov Identifier: NCT01766999

26. (NCT01402869 chunk 1): Lauren GutenBerg. Methemoglobin Levels in Generally Anesthetized Pediatric Dental Patients Receiving Local Anesthetics. Loma Linda University. 2011. ClinicalTrials.gov Identifier: NCT01402869

27. (rathod2024shadesofblue pages 3-5): Bharatsing D Rathod, Nilesh Kamble, Onkar Awadhiya, Udit Narang, Rajashree S Khot, and Sunita Kumbhalkar. Shades of blue: a case series of acquired methemoglobinemia. Apr 2024. URL: https://doi.org/10.7759/cureus.58312, doi:10.7759/cureus.58312. This article has 3 citations.

28. (mcnulty2022foodinducedmethemoglobinemiaa pages 3-3): Richard McNulty, Nikhil Kuchi, Elena Xu, and Naren Gunja. Food-induced methemoglobinemia: a systematic review. Journal of food science, 87 4:1423-1448, Mar 2022. URL: https://doi.org/10.1111/1750-3841.16090, doi:10.1111/1750-3841.16090. This article has 64 citations and is from a peer-reviewed journal.

29. (NCT03542760 chunk 1):  Acquired Methemoglobinemia Observational Registry. Hospital Quality Foundation. 2018. ClinicalTrials.gov Identifier: NCT03542760

30. (NCT03395223 chunk 1):  MEthylene Blue In Patients With Acquired Methemoglobinemia. Provepharm SAS. 2018. ClinicalTrials.gov Identifier: NCT03395223

31. (patton2016detectingmethemoglobinemiain pages 1-2): Toni G. Patton, Stephen L. Blamer, and Katherine E. Horak. Detecting methemoglobinemia in animals with a drop of blood. PLoS ONE, 11:e0167942, Dec 2016. URL: https://doi.org/10.1371/journal.pone.0167942, doi:10.1371/journal.pone.0167942. This article has 17 citations and is from a peer-reviewed journal.

32. (mcconkey2007themechanismof pages 132-137): SE McConkey. The mechanism of acetaminophen-induced methemoglobinemia in dogs and cats. Unknown journal, 2007.

33. (miller2021safetyandtoxicology pages 1-2): Lutfiya Miller, Charles D. Hébert, Sheila D. Grimes, James S. Toomey, Joo-Yeun Oh, Jason J. Rose, and Rakesh P. Patel. Safety and toxicology assessment of sodium nitrite administered by intramuscular injection. Oct 2021. URL: https://doi.org/10.1016/j.taap.2021.115702, doi:10.1016/j.taap.2021.115702. This article has 2 citations and is from a highest quality peer-reviewed journal.

34. (NCT01402869 chunk 2): Lauren GutenBerg. Methemoglobin Levels in Generally Anesthetized Pediatric Dental Patients Receiving Local Anesthetics. Loma Linda University. 2011. ClinicalTrials.gov Identifier: NCT01402869

## Artifacts

- [Edison artifact artifact-00](Drug-Induced_Methemoglobinemia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.
