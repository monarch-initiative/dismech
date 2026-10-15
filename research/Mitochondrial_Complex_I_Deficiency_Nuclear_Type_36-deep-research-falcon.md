---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T17:37:30.243499'
end_time: '2026-09-03T17:52:22.211118'
duration_seconds: 891.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial complex I deficiency, nuclear type 36 (MC1DN36), caused
    by biallelic NDUFC2 variants (the rare Mendelian mitochondrial disease, NOT the
    NDUFC2 cardiovascular/hypertension GWAS locus and NOT the NDUFC2-KCTD14 readthrough)
  mondo_id: MONDO:0030902
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_36-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial complex I deficiency, nuclear type 36 (MC1DN36), caused by biallelic NDUFC2 variants (the rare Mendelian mitochondrial disease, NOT the NDUFC2 cardiovascular/hypertension GWAS locus and NOT the NDUFC2-KCTD14 readthrough)
- **MONDO ID:** MONDO:0030902 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex I deficiency, nuclear type 36 (MC1DN36), caused by biallelic NDUFC2 variants (the rare Mendelian mitochondrial disease, NOT the NDUFC2 cardiovascular/hypertension GWAS locus and NOT the NDUFC2-KCTD14 readthrough)** covering all of the
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
- **Disease Name:** Mitochondrial complex I deficiency, nuclear type 36 (MC1DN36), caused by biallelic NDUFC2 variants (the rare Mendelian mitochondrial disease, NOT the NDUFC2 cardiovascular/hypertension GWAS locus and NOT the NDUFC2-KCTD14 readthrough)
- **MONDO ID:** MONDO:0030902 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex I deficiency, nuclear type 36 (MC1DN36), caused by biallelic NDUFC2 variants (the rare Mendelian mitochondrial disease, NOT the NDUFC2 cardiovascular/hypertension GWAS locus and NOT the NDUFC2-KCTD14 readthrough)** covering all of the
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


# Mitochondrial complex I deficiency, nuclear type 36 (MC1DN36)

## Executive summary and evidence boundary

MC1DN36 is an ultra-rare, autosomal-recessive primary mitochondrial disorder caused by biallelic pathogenic variants in **NDUFC2**, a nuclear gene encoding an accessory subunit of mitochondrial respiratory-chain complex I. The established presentation is early-onset Leigh syndrome with developmental impairment or regression, lactic acidosis, symmetric deep-gray/brainstem MRI lesions, and severe isolated complex-I deficiency. The defining evidence remains one 2020 primary report of three children from two consanguineous families; consequently, every frequency below is a case-series proportion, not a population estimate. In 2023, the ClinGen Mitochondrial Disease Gene Curation Expert Panel classified the NDUFC2–Leigh syndrome spectrum relationship as **Moderate**, reflecting persuasive functional evidence but very few independent human cases. (alahmad2020bi‐allelicpathogenicvariants pages 1-2, mccormick2023expertpanelcuration pages 9-10)

No additional NDUFC2-MC1DN36 clinical series, disease-specific therapy, interventional trial, natural-history study, single-cell study, or faithful whole-animal disease model was identified through the searched literature and ClinicalTrials.gov records. The common NDUFC2 cardiovascular/hypertension variants and the **NDUFC2-KCTD14** readthrough are outside this report.

## 1. Disease information

### Definition

MC1DN36 is a Mendelian oxidative-phosphorylation disorder in which inadequate NDUFC2 function prevents normal assembly of the membrane arm of NADH:ubiquinone oxidoreductase (complex I). The resulting bioenergetic defect preferentially injures high-energy tissues, producing a Leigh syndrome spectrum phenotype. The primary paper’s exact abstract statement is: **“Bi-allelic pathogenic variants in NDUFC2 cause early-onset Leigh syndrome and stalled biogenesis of complex I.”** It described three affected children carrying homozygous c.346_*7del or c.173A>T, p.His58Leu variants. (alahmad2020bi‐allelicpathogenicvariants pages 1-2)

### Identifiers and synonyms

| Resource | Identifier/name | Interpretation |
|---|---|---|
| MONDO | **MONDO:0030902** | Mitochondrial complex I deficiency, nuclear type 36; identifier supplied in the target specification and consistent with the disease concept. |
| OMIM disease | Commonly indexed as **MC1DN36 / mitochondrial complex I deficiency, nuclear type 36** | The retrieved primary text directly gives the NDUFC2 gene entry but not the disease-entry number; the latter should be verified against the live OMIM record before database ingestion. |
| OMIM gene | **603845 — NDUFC2** | Explicitly cited by the primary report. (alahmad2020bi‐allelicpathogenicvariants pages 4-6, alahmad2020bi‐allelicpathogenicvariants pages 12-13) |
| Gene/transcript | **NDUFC2; NM_004549.6; NP_004540.1** | Transcript and protein accessions used in the defining study. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 10-11) |
| ClinVar submissions | **SCV001162791** for c.346_*7del; **SCV001162790** for c.173A>T | Submitter records quoted in the primary report, not assertions independently re-evaluated here. (alahmad2020bi‐allelicpathogenicvariants pages 4-6) |
| Orphanet | No disease-specific identifier established in retrieved evidence | It may be subsumed under Leigh syndrome or mitochondrial complex-I deficiency. |
| ICD-10/ICD-11 and MeSH | No MC1DN36-specific code/heading identified | Use a broader mitochondrial metabolism/Leigh syndrome code only with local coding guidance; do not represent it as disease-specific. |

Useful synonyms are **NDUFC2-related mitochondrial disease**, **NDUFC2-related Leigh syndrome**, **NDUFC2 deficiency**, and **autosomal-recessive complex I deficiency due to NDUFC2**. “Leigh syndrome spectrum” is a broader phenotype, not a synonym with identical extension.

The clinical evidence consists of individually described patients and laboratory investigations, subsequently aggregated into disease-level resources and the 2023 ClinGen expert curation. It is not derived from EHR-scale population data. (alahmad2020bi‐allelicpathogenicvariants pages 1-2, mccormick2023expertpanelcuration pages 9-10)

## 2. Etiology, risk, protective, and environmental factors

The necessary initiating cause is **biallelic germline NDUFC2 dysfunction**. Both reported families were consanguineous, and each informative parent was heterozygous, supporting autosomal-recessive inheritance. No dominant, somatic, mtDNA, chromosomal, infectious, toxic, dietary, occupational, or lifestyle cause has been demonstrated. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 4-6)

* **Genetic risk:** two reported homozygous alleles—NM_004549.6:c.346_*7del, predicted p.(His116_Arg119delins21), and c.173A>T, p.(His58Leu). Family history, parental relatedness, and carrier status increase reproductive risk but do not modify severity once an affected genotype is present.
* **Modifiers/protective alleles:** none established. No modifier gene, protective NDUFC2 allele, penetrance-reducing allele, or validated epigenetic modifier is known.
* **Environment:** intercurrent respiratory infection precipitated severe lactic decompensation/regression in Subject 2 and preceded terminal deterioration in Subject 3. Infection is therefore a plausible **trigger of metabolic crisis**, not a cause of the inherited disorder. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 4-6)
* **Gene–environment interaction:** the limited observations support the general mitochondrial concept that increased energy demand during illness can expose inadequate respiratory reserve. This downstream interaction is clinically plausible but has not been experimentally quantified in MC1DN36.
* **Protective lifestyle factors:** none disease-specifically validated. Avoidance of fasting and rapid treatment of illness are precautionary mitochondrial-care practices rather than proven prevention of MC1DN36.

## 3. Phenotypes

The complete patient-level evidence is summarized below. Frequencies must retain their tiny denominators.

| Subject / family | Genotype and confirmation caveat | Onset and major clinical features | MRI and laboratory findings | Functional evidence | Outcome |
|---|---|---|---|---|---|
| **Subject 1 — Family 1**; Saudi female; consanguineous first-cousin parents | Homozygous **NDUFC2 NM_004549.6:c.346_*7del**, predicted **p.(His116_Arg119delins21)** stop-loss variant; confirmed by WGS and Sanger sequencing. Both parents and one healthy brother were heterozygous. | Born at 37 weeks; birthweight 2.0 kg. Developmental delay recognized at 2 years when unable to walk. At 6 years: height and weight below 5th centile, inability to stand unsupported or speak, facial dysmorphism, spasticity, brisk reflexes, and bilateral optic-disc pallor. No seizures or recognized cardiac, renal, or hepatic abnormality. | MRI at 21 months: bilateral corticospinal-tract and corona-radiata T2 hyperintensity, local white-matter volume loss, ventricular-outline irregularity suggestive of periventricular leukomalacia, and symmetric thalamic, substantia-nigral, and posterior medullary lesions. Serum lactate 3.6–7.6 mmol/L; alanine 724 μmol/L; proline 366 μmol/L; urinary fumarate 151 mM/M creatinine. | Fibroblast complex-I activity **16% of control**; severely decreased oxygen consumption; NDUFC2 mRNA **43% of control**; no detectable NDUFC2 protein; fully assembled complex I undetectable, with deficient complex-I-containing supercomplexes. Wild-type NDUFC2 lentiviral expression partially restored subunit levels and complex-I assembly. | Alive at last reported examination at age 6 years, with severe motor and speech disability. |
| **Subject 2 — Family 1**; younger Saudi brother of Subject 1 | **Presumed homozygous c.346_*7del**, inferred from the affected-sibling phenotype and family segregation. **DNA was unavailable, so his genotype was not directly confirmed.** | Prenatal cardiomegaly, dilated superior vena cava, small VSD, cisterna-magna dilation, and ventriculomegaly. Born at 36 weeks; birthweight 2.020 kg. Global developmental delay and growth below 3rd centile. Acute hydrocephalus at 5 months required a ventriculoperitoneal shunt. At 19 months, respiratory infection precipitated seizures and complete developmental regression; subsequent spasticity, muscle atrophy, unsafe swallow with aspiration, recurrent chest infections, tube feeding, hydronephrosis, and persistent lactic acidosis. | MRI at 10 days: bilateral frontal periventricular and caudothalamic-groove T2 abnormalities, lentiform-nucleus lesions, paucity and edema of periventricular white matter, Dandy–Walker malformation, and partial corpus-callosum agenesis. Serum lactate persistently 4.0–10.0 mmol/L after birth and above 20.0 mmol/L during severe infection. Ammonia, CK, liver and thyroid tests, plasma amino acids, urinary organic acids, and newborn screening were unremarkable. | No patient sample was available for respiratory-chain, protein, complexome, or rescue studies. Similar biochemical dysfunction was inferred by the authors from the shared phenotype and presumed familial genotype. | Died at **3 years** from pneumonia with severe metabolic acidosis. |
| **Subject 3 — Family 2**; Moroccan male; consanguineous first-cousin parents | Homozygous **NDUFC2 NM_004549.6:c.173A&gt;T, p.(His58Leu)**; identified by a mitochondrial-disease gene panel and confirmed by Sanger sequencing. Both parents were heterozygous; healthy siblings were not tested. | Vomiting, failure to thrive, psychomotor delay, and poor eye contact from the first months. At 5 months: weight, length, and head circumference below 3rd centile; strabismus; truncal hypotonia with limb hypertonia; paucity of spontaneous movement; and absent postural control. Severe central auditory and visual conduction abnormalities; intermittent clonic seizures occurred under anesthesia. | MRI: bilateral symmetric T2 hyperintensity in the thalami, basal ganglia, and brainstem; spinal MRI normal. Serum lactate 3.2 mmol/L and pyruvate 194 μmol/L; routine tests and plasma amino acids normal. EEG and peripheral nerve-conduction studies unremarkable. | Complex-I activity **19% of control in fibroblasts** and **48% in skeletal muscle**; severely decreased fibroblast oxygen consumption; NDUFC2 mRNA comparable to control but only scant NDUFC2 protein; greatly reduced assembled complex I and supercomplexes. Wild-type NDUFC2 lentiviral expression partially restored protein levels and assembly. | Died at **8 months** after severe respiratory deterioration. |
| **Reported cohort summary** | **3 affected children from 2 unrelated consanguineous families; 2 distinct homozygous variants.** Molecular confirmation in 2/3 subjects; Subject 2’s genotype was inferred but untested. | Developmental delay or psychomotor impairment **3/3**; poor growth or failure to thrive **3/3**; abnormal tone or spasticity **3/3**; seizures **2/3**; major feeding or aspiration problems **1/3**. | Elevated lactate **3/3**; bilateral brain MRI abnormalities **3/3**, involving deep gray nuclei and/or brainstem in all three. | Severe isolated complex-I deficiency demonstrated in available fibroblasts **2/2** and muscle **1/1**; impaired respiration **2/2**; assembly defect and partial lentiviral rescue **2/2**. | Death in infancy or early childhood **2/3**; one survivor had severe disability at age 6. These descriptive frequencies derive from only three cases and are not population estimates. |


*Table: Patient-level clinical, genetic, biochemical, and outcome data from the three children reported by Alahmad et al. on September 24, 2020. The table highlights Subject 2’s inferred, unconfirmed genotype and the very small denominators underlying all frequencies. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 1-2, alahmad2020bi‐allelicpathogenicvariants pages 4-6, alahmad2020bi‐allelicpathogenicvariants pages 6-9)*

### Suggested HPO annotations

* **Neurodevelopment:** global developmental delay (HP:0001263), delayed motor development (HP:0001270), absent speech (HP:0001344), developmental regression (HP:0002376), psychomotor regression (HP:0002376 or the most current HPO child term).
* **Motor/neurologic:** muscular hypotonia (HP:0001252), truncal hypotonia, limb hypertonia (HP:0001276), spasticity (HP:0001257), hyperreflexia (HP:0001347), muscle atrophy (HP:0003202), paucity of movement, seizures (HP:0001250).
* **Growth/feeding:** failure to thrive (HP:0001508), short stature (HP:0004322), low weight (HP:0004325), microcephaly (HP:0000252), vomiting (HP:0002013), dysphagia (HP:0002015), aspiration (HP:0002835), feeding difficulties (HP:0011968).
* **Eye/sensory:** poor eye contact, strabismus (HP:0000486), optic-disc pallor/optic atrophy (HP:0000648), abnormal visual evoked potentials and abnormal brainstem auditory evoked potentials.
* **Metabolic/laboratory:** lactic acidosis (HP:0003128), elevated circulating lactate (HP:0002151), elevated pyruvate, hyperalaninemia (HP:0003348), hyperprolinemia (HP:0008358), fumaric aciduria, isolated mitochondrial complex-I deficiency (HP:0003201).
* **Imaging/anatomy:** bilateral basal-ganglia lesions (HP:0002134), thalamic lesions, brainstem lesions, abnormal cerebral white matter, ventriculomegaly (HP:0002119), hydrocephalus (HP:0000238), Dandy–Walker malformation (HP:0001305), partial agenesis of corpus callosum (HP:0001338).
* **Other reported findings:** ventricular septal defect (HP:0001629), cardiomegaly (HP:0001640), pulmonary-artery stenosis (HP:0001642), hydronephrosis (HP:0000126), recurrent respiratory infections (HP:0002205).

Clinical severity ranged from severe childhood disability to fatal infantile disease. Developmental impairment, poor growth, abnormal tone, elevated lactate, and bilateral MRI abnormalities occurred in all three reported children. Two died by age three; one was alive but unable to stand unsupported or speak at age six. No validated EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life measurements exist. Functional impact was nevertheless profound: loss or failure of milestones, tube feeding, aspiration, intensive-care admission, shunt surgery, and severe mobility/communication limitation. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 1-2, alahmad2020bi‐allelicpathogenicvariants pages 4-6)

## 4. Genetic and molecular information

**NDUFC2** encodes a small nuclear-encoded complex-I membrane-arm accessory subunit. The defining study used NM_004549.6 and identified:

1. **c.346_*7del**, a 22-nucleotide last-exon deletion and stop-loss allele predicted to produce p.(His116_Arg119delins21). It was absent from the population databases examined in 2020. Subject 1 was homozygous; both parents and a healthy brother were heterozygous. The similarly affected brother was presumed homozygous, but DNA was unavailable. Fibroblast NDUFC2 mRNA was 43% of control and protein was undetectable. (alahmad2020bi‐allelicpathogenicvariants pages 4-6, alahmad2020bi‐allelicpathogenicvariants pages 6-9)
2. **c.173A>T, p.(His58Leu)**, a missense substitution at a highly conserved residue. Subject 3 was homozygous and both parents were carriers. Predictors reported were PolyPhen-2 1.000, SIFT 0.000, PROVEAN −6.733, and scaled CADD 27.9. The exact allele frequency was not supplied, but it was treated as rare; a different substitution at the same codon, p.His58Tyr, had gnomAD MAF 1.21×10⁻⁵. NDUFC2 transcript abundance was normal, whereas protein was scant, consistent with protein/complex instability. (alahmad2020bi‐allelicpathogenicvariants pages 4-6, alahmad2020bi‐allelicpathogenicvariants pages 6-9)

The alleles are constitutional **germline** variants. Functional consequence is loss of normal complex-I assembly/function, not gain-of-function or dominant-negative activity. Wild-type cDNA partially restored complex-I subunits and holoenzyme assembly in both available patient fibroblast lines—strong variant-level functional evidence. (alahmad2020bi‐allelicpathogenicvariants pages 9-10, alahmad2020bi‐allelicpathogenicvariants pages 11-12)

In the 2020 gnomAD release used by the authors, no healthy person was homozygous for an NDUFC2 loss-of-function allele. Two homozygous coding variants were observed—p.Leu46Val (4,270 homozygotes; MAF 0.197) and p.Arg119His (one homozygote; MAF 2.77×10⁻⁴)—and were not predicted to materially alter residue chemistry. These historical values should be refreshed against current gnomAD before clinical interpretation. (alahmad2020bi‐allelicpathogenicvariants pages 6-9)

No disease-associated copy-number variant, aneuploidy, translocation, repeat expansion, somatic mosaicism, germline mosaicism, anticipation, methylation signature, or modifier locus has been reported. The 2023 expert panel placed NDUFC2 in the autosomal-recessive complex-I group and assigned Moderate validity. (mccormick2023expertpanelcuration pages 9-10, mccormick2023expertpanelcuration pages 15-20)

## 5. Environmental, lifestyle, and infectious information

There is no evidence that smoking, alcohol, exercise pattern, diet, radiation, pollution, toxin exposure, occupation, or a specific pathogen causes MC1DN36. Pneumonia/respiratory infection acted as an acute stressor in the two fatal cases; aspiration and unsafe swallowing probably increased infection risk in Subject 2. No organism was identified, and the disease is neither infectious nor transmissible. (alahmad2020bi‐allelicpathogenicvariants pages 2-4)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic NDUFC2 variants lead to** absent, reduced, or unstable NDUFC2 protein in the mitochondrial inner membrane.
2. **Loss of functional NDUFC2 leads to** failure to stabilize/incorporate the proximal membrane-arm **ND2 module**, with associated disruption of the neighboring ND1 module.
3. **Failed ND1/ND2-module incorporation results in** accumulation of Q-module/TIMMDC1/NDUFA13 and larger MCIA-containing assembly intermediates and independent ND4-module intermediates—directly demonstrated by patient complexome profiling.
4. **Stalled membrane-arm biogenesis leads to** marked depletion of fully assembled complex I and complex-I-containing respiratory supercomplexes, while complexes II–V remain comparatively preserved.
5. **Loss of holo-complex I results in** deficient NADH oxidation, ubiquinone reduction, proton pumping, membrane-potential support, and oxygen consumption; impaired ATP production and altered redox balance are mechanistically expected, although ATP and ROS were not directly quantified in these three patients.
6. **Insufficient respiratory reserve leads to** chronic lactate elevation and vulnerability to metabolic acidosis during infection or other increased-energy-demand states.
7. **Energy failure in high-demand developing tissues results in**—by strong Leigh-syndrome inference—bilateral basal-ganglia, thalamic, substantia-nigral, brainstem, corticospinal/white-matter injury and neuromuscular dysfunction.
8. These lesions **lead to** developmental delay/regression, tone abnormalities, seizures, visual pathway dysfunction, feeding/respiratory compromise, severe disability, and, in the most severe cases, early death. (alahmad2020bi‐allelicpathogenicvariants pages 10-11, alahmad2020bi‐allelicpathogenicvariants pages 9-10, alahmad2020bi‐allelicpathogenicvariants pages 4-6, alahmad2020bi‐allelicpathogenicvariants pages 6-9)

### Molecular detail and evidence level

NDUFC2 resides in the ND2 proton-pumping module and contacts multiple ND1-, ND2-, and ND4-module subunits. Patient complexomes retained Q-module formation but accumulated approximately 300-kDa Q–TIMMDC1–NDUFA13 and 715–800-kDa MCIA-containing intermediates; N, ND2, and ND5 intermediates were not detected. This supports a scaffolding/stabilizing role at an early membrane-arm assembly step rather than direct catalysis of NADH oxidation. (alahmad2020bi‐allelicpathogenicvariants pages 10-11, alahmad2020bi‐allelicpathogenicvariants pages 9-10, alahmad2020bi‐allelicpathogenicvariants pages 6-9, fernandez‐vizarra2021mitochondrialdisordersof pages 96-99)

Direct human evidence comprises respiratory-chain enzymology, respirometry, immunoblotting, BN-PAGE, proteomics/complexome profiling, and lentiviral complementation in patient fibroblasts, plus muscle enzymology in Subject 3. Residual complex-I activity was 16% and 19% in available fibroblasts and 48% in Subject 3 muscle. Fully assembled complex I was undetectable in Subject 1 and greatly reduced in Subject 3. (alahmad2020bi‐allelicpathogenicvariants pages 4-6)

Suggested ontology terms are **mitochondrial respiratory-chain complex-I assembly** (GO:0032981), **mitochondrial electron-transport, NADH to ubiquinone** (GO:0006120), **oxidative phosphorylation** (GO:0006119), **ATP synthesis coupled electron transport** (GO:0042773), **proton transmembrane transport** (GO:1902600), **mitochondrial inner membrane** (GO:0005743), **respiratory-chain complex I** (GO:0005747), and **mitochondrial respiratory-chain supercomplex** (GO:0098803). Relevant suggested cell classes include neuron (CL:0000540), CNS neuron, skeletal muscle cell/myocyte (CL:0000188), cardiomyocyte (CL:0000746), retinal/optic-pathway neuron, astrocyte (CL:0000127), oligodendrocyte (CL:0000128), and fibroblast (CL:0000057). Only fibroblasts and skeletal muscle were directly assayed; injury to specific neural cell classes remains inferred.

No MC1DN36-specific transcriptome, single-cell, spatial-transcriptomic, lipidomic, epigenomic, or integrated multi-omic study exists. The available complexome dataset is deposited as **ProteomeXchange/PRIDE PXD014936**. (alahmad2020bi‐allelicpathogenicvariants pages 11-12)

## 7. Anatomical structures affected

The principal system is the **central nervous system**, particularly bilateral basal ganglia/lentiform nuclei, thalami, substantia nigra, brainstem/medulla, corticospinal tracts, corona radiata, and periventricular white matter. Corpus callosum, cerebellar/posterior-fossa development, and ventricular/CSF pathways were abnormal in Subject 2. Skeletal muscle, optic discs/visual pathways, auditory brainstem pathways, swallowing/respiratory apparatus, and growth are also involved. Cardiac and renal findings occurred in one child each, but their causal relationship to NDUFC2 deficiency is uncertain. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 1-2)

Suggested UBERON concepts include brain (UBERON:0000955), basal ganglion, thalamus (UBERON:0001897), substantia nigra (UBERON:0002038), brainstem (UBERON:0002298), medulla oblongata (UBERON:0001896), cerebral white matter, corpus callosum (UBERON:0002336), spinal cord (normal in Subject 3), skeletal muscle tissue (UBERON:0001134), optic nerve (UBERON:0000941), heart (UBERON:0000948), kidney (UBERON:0002113), and lung (UBERON:0002048). Lesions were characteristically bilateral/symmetric rather than lateralized. Subcellular localization is the mitochondrial inner membrane and respiratory complex-I membrane arm. (alahmad2020bi‐allelicpathogenicvariants pages 1-2, alahmad2020bi‐allelicpathogenicvariants pages 9-10)

## 8. Temporal development

Onset was congenital/antenatal in Subject 2, within the first months in Subject 3, and recognized at two years in Subject 1. Thus, known MC1DN36 is a pediatric, usually infantile/early-childhood disorder, but three cases cannot exclude milder or adult presentations. The course is chronic and progressive, with episodic acute decompensation: Subject 2 underwent rapid regression during infection at 19 months; Subject 3 died after respiratory deterioration at eight months; Subject 1 had severe static/progressive disability at six years. No remission was reported. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 1-2, alahmad2020bi‐allelicpathogenicvariants pages 4-6)

The principal vulnerability windows appear to be early neurodevelopment and catabolic illness. This is descriptive, not a validated staging system. There are no defined early/intermediate/end-stage criteria or quantitative progression rate.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed carrier parents, each conception has a theoretical 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele. The two families were Saudi and Moroccan and both involved first-cousin parents. This supports consanguinity as an ascertainment/reproductive-risk factor but does not establish founder effects or ethnic enrichment. (alahmad2020bi‐allelicpathogenicvariants pages 1-2, alahmad2020bi‐allelicpathogenicvariants pages 4-6)

Known sex distribution is two males and one female. Penetrance appears high for the reported homozygous genotypes, but cannot be estimated formally; expressivity was variable in onset and severity. Carrier frequency, birth prevalence, incidence, geographic distribution, founder status, and population sex ratio are unknown. Reporting only three patients precludes a defensible cases-per-100,000 estimate.

## 10. Diagnostics

### Recommended approach

1. Suspect Leigh spectrum disease in an infant/child with developmental delay or regression, abnormal tone, failure to thrive, seizures or visual/feeding abnormalities, especially with lactate elevation and bilateral deep-gray/brainstem MRI lesions.
2. Obtain blood lactate and pyruvate with careful collection; consider plasma amino acids, urine organic acids, blood gas, glucose, ammonia, CK, liver/renal studies, and CSF lactate when clinically justified. Normal ancillary metabolites do not exclude MC1DN36.
3. Perform brain MRI, including diffusion and spectroscopy when available. Typical LSS evidence includes bilateral symmetric basal-ganglia/brainstem T2 abnormalities; isolated thalamic lesions are nonspecific and can reflect hypoxic-ischemic injury. (mccormick2023expertpanelcuration pages 20-23)
4. Use a comprehensive mitochondrial disease/Leigh panel including **NDUFC2**, or preferably trio WES/WGS with nuclear and mtDNA analysis. The first family’s prioritization-limited WES was negative, whereas unbiased WGS found the terminal-exon deletion—an important warning about pipeline filters and coverage. (alahmad2020bi‐allelicpathogenicvariants pages 10-11, alahmad2020bi‐allelicpathogenicvariants pages 11-12)
5. Confirm candidate variants and segregation by Sanger sequencing or an orthogonal method. Evaluate exon-level CNVs and noncoding/splice variants when sequencing is unrevealing.
6. For novel or uncertain NDUFC2 variants, pursue functional confirmation in fibroblasts or muscle: spectrophotometric respiratory-chain activities, high-resolution respirometry, NDUFC2/complex-I immunoblotting, BN-PAGE/in-gel activity, or complexome profiling. Demonstration of isolated complex-I deficiency and rescue by wild-type NDUFC2 is particularly strong, although complementation is a research-level test. (alahmad2020bi‐allelicpathogenicvariants pages 4-6, alahmad2020bi‐allelicpathogenicvariants pages 11-12)

CMA, karyotyping, FISH, and repeat-expansion testing are not first-line tests for this single-gene disorder. CMA was normal in Subject 1. mtDNA sequencing is important in the broader differential but cannot detect a nuclear NDUFC2 variant. RNA-seq could identify occult splice effects; proteomics can reveal complex-I assembly failure, but neither is validated as routine MC1DN36 diagnostics.

Differential diagnoses include other nuclear/mtDNA complex-I deficiencies, pyruvate-dehydrogenase deficiency, other Leigh-spectrum genes, organic acidemias, biotin/thiamine-responsive disorders, POLG-related disease, hypoxic-ischemic encephalopathy, leukodystrophies, and congenital brain malformations. Molecular diagnosis is essential because imaging and lactate are not gene-specific. The 2023 ClinGen framework accepts characteristic imaging plus neurologic and biochemical/mitochondrial evidence, including OXPHOS activity below 30%, an MRS lactate peak, or diminished respiration. (mccormick2023expertpanelcuration pages 20-23, mccormick2023expertpanelcuration pages 5-7)

## 11. Outcome and prognosis

Among the three reported children, two died—at eight months and three years—while the surviving child had severe motor and language disability at age six. This observed 2/3 mortality must not be interpreted as a survival rate. Pneumonia, respiratory deterioration, aspiration, and severe metabolic acidosis were major complications. Poor growth, loss of mobility/communication, feeding dependence, seizures, spasticity, and respiratory vulnerability indicate high morbidity. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 4-6)

No 5- or 10-year survival estimate, life expectancy, standardized disability outcome, quality-of-life score, prognostic biomarker, or genotype–prognosis model exists. Earlier onset, profound residual complex-I deficiency, brainstem/bulbar disease, and recurrent metabolic crises are plausible adverse factors, but they are not validated specifically for NDUFC2.

## 12. Treatment and current applications

There is **no curative, approved, or NDUFC2-targeted treatment** and no NDUFC2-specific clinical trial was found. Care should be coordinated through a specialist mitochondrial/metabolic center and remains supportive:

* individualized emergency plans; prompt treatment of fever/infection, dehydration, hypoglycemia, and acidosis; avoidance of prolonged fasting;
* nutritional assessment, swallowing evaluation, aspiration precautions, and nasogastric/gastrostomy support when needed;
* antiseizure treatment selected with mitochondrial expertise; rehabilitation including physical, occupational, speech/communication, and respiratory therapy;
* management of spasticity/dystonia, vision/hearing impairment, hydrocephalus, orthopedic complications, and pain;
* periodic cardiac, respiratory, renal, ophthalmologic, audiologic, neurologic, growth, and nutritional surveillance based on manifestations;
* careful peri-anesthetic planning, since Subject 3 experienced clonic seizures during anesthesia, although causality is uncertain. (alahmad2020bi‐allelicpathogenicvariants pages 2-4, alahmad2020bi‐allelicpathogenicvariants pages 4-6)

Empirical “mitochondrial cocktails” such as thiamine, riboflavin, coenzyme Q10, antioxidants, or carnitine have not been tested in MC1DN36 and should not be described as effective. Ketogenic diet and coenzyme Q10 are targeted to particular other Leigh etiologies, not automatically to NDUFC2 deficiency. The expert panel emphasized that genotype matters because some LSS causes have specific treatments; none was identified for NDUFC2. (mccormick2023expertpanelcuration pages 12-14)

The lentiviral wild-type-NDUFC2 rescue is proof of mechanism, not a clinical gene therapy: transduced fibroblasts showed partial restoration, but no delivery, safety, CNS targeting, or in-vivo efficacy study exists. No NDUFC2-specific CRISPR, mRNA, ASO, siRNA, cell therapy, transplantation, surgery beyond complication management, or pharmacogenomic strategy is established. Suggested broad NCIT intervention concepts include Genetic Counseling, Physical Therapy, Occupational Therapy, Speech Therapy, Enteral Nutrition, Anticonvulsant Therapy, and Supportive Care; exact current NCIT codes should be resolved against the live thesaurus.

## 13. Prevention

The inherited biochemical defect cannot currently be prevented through lifestyle or immunization. Primary reproductive prevention options after identifying familial variants include genetic counseling, carrier/cascade testing, preimplantation genetic testing for monogenic disease (PGT-M), chorionic-villus or amniotic-fluid prenatal diagnosis, and use of donor gametes. The defining authors specifically noted that molecular diagnosis enables prenatal testing in subsequent pregnancies. (alahmad2020bi‐allelicpathogenicvariants pages 12-13)

There is no population or newborn screening program for MC1DN36. Targeted testing of siblings and relatives is appropriate once a familial allele is known. Secondary/tertiary prevention consists of early diagnosis, anticipatory feeding/respiratory care, vaccination according to routine schedules, prompt infection treatment, avoidance of fasting, and emergency metabolic planning. These measures may reduce complications but have no MC1DN36-specific efficacy estimates.

## 14. Other species and natural disease

No naturally occurring NDUFC2-associated Leigh-like disease was identified in a companion animal, livestock species, or wildlife; therefore no breed/VBO annotation is justified. NDUFC2 orthologs and the complex-I membrane-arm function are evolutionarily conserved, but species-specific NCBI Gene identifiers should be imported directly from NCBI/Alliance rather than inferred here. The condition has no zoonotic potential and no cross-species transmission.

## 15. Model organisms and experimental systems

The strongest disease model is **patient-derived skin fibroblasts** from Subjects 1 and 3. They reproduce the molecular phenotype—16–19% residual complex-I activity, reduced respiration, loss of subunits/holoenzyme/supercomplexes, stalled assembly intermediates—and show partial rescue after wild-type NDUFC2 expression. Their limitation is that fibroblasts cannot model regional brain necrosis, neural development, behavior, feeding, or survival. (alahmad2020bi‐allelicpathogenicvariants pages 4-6, alahmad2020bi‐allelicpathogenicvariants pages 6-9, alahmad2020bi‐allelicpathogenicvariants pages 11-12)

NDUFC2-knockout HEK293T and other NDUFC2-reduction systems support a general requirement for complex-I integrity, but they are not models of either reported human allele or the full MC1DN36 phenotype. The patient paper notes that its complexome findings provide in-vivo cellular support for earlier NDUFC2-knockout assembly results. (alahmad2020bi‐allelicpathogenicvariants pages 10-11)

No validated Ndufc2 knock-in mouse, zebrafish, Drosophila, C. elegans, yeast, patient-derived iPSC neuron, brain organoid, or humanized model of MC1DN36 was identified. Ndufs4 knockout mice are widely used for complex-I Leigh syndrome, but they model a different gene and should be annotated only as **mechanistically analogous**, not as an NDUFC2 disease model.

## Recent developments and expert interpretation

The most important post-discovery development is the **2023 ClinGen expert-panel curation**. Among 114 Leigh-spectrum gene–disease relationships, 31 were Definitive, 38 Moderate, and 43 Limited; NDUFC2 was assigned **Moderate**, near the borderline but upgraded through expert review because the functional evidence was unusually strong. The panel’s classification appropriately balances compelling patient-cell rescue/complexome data against only two independently ascertained families. Recuration is warranted as new cases appear. (mccormick2023expertpanelcuration pages 9-10, mccormick2023expertpanelcuration pages 7-9, mccormick2023expertpanelcuration pages 4-5)

No disease-specific 2023–2024 therapeutic or clinical-natural-history advance was found. Accordingly, the current expert interpretation is conservative: **the gene–disease relationship is credible, the assembly mechanism is unusually well demonstrated, but clinical spectrum, penetrance, epidemiology, prognosis, and treatment responsiveness remain largely unknown.**

## Key primary and authoritative sources

1. **Alahmad A, et al.** “Bi-allelic pathogenic variants in NDUFC2 cause early-onset Leigh syndrome and stalled biogenesis of complex I.” *EMBO Molecular Medicine*. Published online **24 September 2020**;12:e12619. DOI/URL: https://doi.org/10.15252/emmm.202012619. Exact abstract conclusion: **“Complexome profiling confirmed a loss of NDUFC2 and defective complex I assembly,”** with aberrant intermediates indicating a crucial role in the membrane arm, particularly the ND2 module. (alahmad2020bi‐allelicpathogenicvariants pages 1-2)
2. **McCormick E, et al.** “Expert Panel Curation of 113 Primary Mitochondrial Disease Genes for the Leigh Syndrome Spectrum.” *Annals of Neurology*. **August 2023**;94:696–712. DOI/URL: https://doi.org/10.1002/ana.26716. This is the principal recent authoritative gene-validity assessment. (mccormick2023expertpanelcuration pages 9-10, mccormick2023expertpanelcuration pages 7-9)
3. **Fernandez-Vizarra E, Zeviani M.** “Mitochondrial disorders of the OXPHOS system.” *FEBS Letters*. 2021;595:1062–1106. DOI/URL: https://doi.org/10.1002/1873-3468.13995. It places NDUFC2 in the complex-I membrane-arm ND2 module and associates it with complex-I deficiency/Leigh syndrome. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99)

**PMID note:** PMID values were not present in the retrieved full-text metadata and are therefore not supplied rather than risk an incorrect identifier. DOI links above are stable primary identifiers.

References

1. (alahmad2020bi‐allelicpathogenicvariants pages 1-2): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

2. (mccormick2023expertpanelcuration pages 9-10): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 72 citations and is from a highest quality peer-reviewed journal.

3. (alahmad2020bi‐allelicpathogenicvariants pages 4-6): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

4. (alahmad2020bi‐allelicpathogenicvariants pages 12-13): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

5. (alahmad2020bi‐allelicpathogenicvariants pages 2-4): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

6. (alahmad2020bi‐allelicpathogenicvariants pages 10-11): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

7. (alahmad2020bi‐allelicpathogenicvariants pages 6-9): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

8. (alahmad2020bi‐allelicpathogenicvariants pages 9-10): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

9. (alahmad2020bi‐allelicpathogenicvariants pages 11-12): Ahmad Alahmad, Alessia Nasca, Juliana Heidler, Kyle Thompson, Monika Oláhová, Andrea Legati, Eleonora Lamantea, Jana Meisterknecht, Manuela Spagnolo, Langping He, Seham Alameer, Fahad Hakami, Abeer Almehdar, Anna Ardissone, Charlotte L Alston, Robert McFarland, Ilka Wittig, Daniele Ghezzi, and Robert W Taylor. Bi‐allelic pathogenic variants in ndufc2 cause early‐onset leigh syndrome and stalled biogenesis of complex i. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012619, doi:10.15252/emmm.202012619. This article has 34 citations and is from a highest quality peer-reviewed journal.

10. (mccormick2023expertpanelcuration pages 15-20): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 72 citations and is from a highest quality peer-reviewed journal.

11. (fernandez‐vizarra2021mitochondrialdisordersof pages 96-99): Erika Fernandez‐Vizarra and Massimo Zeviani. Mitochondrial disorders of the oxphos system. FEBS Letters, 595:1062-1106, Dec 2021. URL: https://doi.org/10.1002/1873-3468.13995, doi:10.1002/1873-3468.13995. This article has 410 citations and is from a peer-reviewed journal.

12. (mccormick2023expertpanelcuration pages 20-23): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 72 citations and is from a highest quality peer-reviewed journal.

13. (mccormick2023expertpanelcuration pages 5-7): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 72 citations and is from a highest quality peer-reviewed journal.

14. (mccormick2023expertpanelcuration pages 12-14): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 72 citations and is from a highest quality peer-reviewed journal.

15. (mccormick2023expertpanelcuration pages 7-9): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 72 citations and is from a highest quality peer-reviewed journal.

16. (mccormick2023expertpanelcuration pages 4-5): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 72 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_36-deep-research-falcon_artifacts/artifact-00.md)