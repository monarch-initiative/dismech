---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T11:11:25.453498'
end_time: '2026-09-08T11:27:05.595644'
duration_seconds: 940.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 33
  mondo_id: MONDO:0032636
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_33-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 33
- **MONDO ID:** MONDO:0032636 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 33** covering all of the
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
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 33
- **MONDO ID:** MONDO:0032636 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 33** covering all of the
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


# Mitochondrial Complex I Deficiency, Nuclear Type 33: Disease-Characteristics Report

## Executive summary and evidence limits

Mitochondrial complex I deficiency, nuclear type 33 (MC1DN33) is an **ultra-rare autosomal-recessive mitochondrial encephalopathy caused by biallelic pathogenic variants in NDUFA6**, a nuclear-encoded accessory subunit of respiratory-chain complex I. The disease was established in 2018 from **four unrelated pediatric patients**; therefore, essentially all disease-specific frequencies below are proportions of these four cases, not population estimates. The phenotype ranges from lethal neonatal metabolic encephalopathy to childhood-onset progressive Leigh-spectrum disease. Patient fibroblasts show defective complex-I assembly, and restoration with wild-type NDUFA6 rescues complex-I abundance and activity, providing strong functional evidence of causality (PMID: **30245030**; published October 2018; DOI/URL: https://doi.org/10.1016/j.ajhg.2018.08.013). (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 8-9, alston2018biallelicmutationsin pages 5-6)

No new NDUFA6 patient cohort or disease-specific therapy was identified among the retrieved 2023–2024 literature. The principal recent mechanistic advance is a 2024 *Cell* study showing that a *C. elegans* NDUFA6 ortholog mutation can suppress selected complex-I defects through a mechanism resembling hypoxia; this is model-organism evidence, not a treatment recommendation (published February 2024; DOI: https://doi.org/10.1016/j.cell.2023.12.010). (meisel2024hypoxiaandintracomplex pages 14-16)

## 1. Disease information

**Definition.** MC1DN33 is a Mendelian oxidative-phosphorylation disorder in which defective NDUFA6 impairs assembly and function of mitochondrial NADH:ubiquinone oxidoreductase (complex I). Clinical presentations include severe neonatal mitochondrial encephalopathy and early-childhood Leigh or Leigh-like disease. (alston2018biallelicmutationsin pages 2-3, alston2018biallelicmutationsin pages 3-5, fernandez‐vizarra2021mitochondrialdisordersof pages 92-96)

**Identifiers and names**

- MONDO: **MONDO:0032636**.
- OMIM phenotype: **618253**; NDUFA6 gene entry: **602138**. (fernandez‐vizarra2021mitochondrialdisordersof pages 92-96)
- Causal gene: **NDUFA6**, approved name *NADH:ubiquinone oxidoreductase subunit A6*; Ensembl **ENSG00000184983**. Open Targets independently associates NDUFA6 with MONDO:0032636 and links the evidence to PMID 30245030. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 33)
- Synonyms: **mitochondrial complex I deficiency, nuclear type 33**, **MC1DN33**, **NDUFA6-related mitochondrial complex I deficiency**, **early-onset isolated mitochondrial complex I deficiency**, and **NDUFA6-related mitochondrial encephalopathy**. NDUFA6 has also been called **LYRM6** or the complex-I **14-kDa accessory subunit**. (alston2018biallelicmutationsin pages 3-5, fernandez‐vizarra2021mitochondrialdisordersof pages 92-96)
- ICD-10, ICD-11 and MeSH: no disease-specific code/heading was established in the retrieved evidence; broader mitochondrial-metabolism or Leigh-syndrome categories are ordinarily required. Orphanet disease-specific mapping was likewise not established.

**Data provenance.** The foundational evidence is patient-level clinical, genomic and fibroblast/muscle data from four unrelated families, subsequently aggregated by OMIM/MONDO/Open Targets and reviews. It is not an EHR-derived population dataset. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 33, alston2018biallelicmutationsin pages 3-5)

## 2. Etiology, risk and protective factors

### Causal factor

The primary cause is **germline biallelic loss or severe impairment of NDUFA6**. Reported alleles include initiation-codon, missense, nonsense and frameshift variants. Segregation and unaffected heterozygous relatives support autosomal-recessive inheritance. Wild-type complementation of patient cells restored the biochemical phenotype, arguing that NDUFA6 dysfunction—not an environmental exposure—is causal. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 5-6)

### Risk factors

- **Genetic:** two pathogenic/likely pathogenic NDUFA6 alleles are the necessary established risk factor. Consanguinity was present in two families—second-cousin parents in one and first-cousin parents in another—raising the probability of homozygosity. (alston2018biallelicmutationsin pages 2-3)
- **Family history:** one family reported two related males who died with epilepsy, compatible with—but not molecularly proven to represent—the same recessive disorder. (alston2018biallelicmutationsin pages 2-3)
- **Environmental/lifestyle/sex:** no toxin, diet, occupation, smoking, alcohol, sex-specific or age-dependent susceptibility factor has been demonstrated.
- **Stress-triggered expression:** one child deteriorated sharply after fever at 25 months. Fever likely increased energetic demand and revealed limited mitochondrial reserve, but infection was a trigger of decompensation rather than the genetic cause. (alston2018biallelicmutationsin pages 2-3)

### Protective factors and gene–environment interaction

No human protective allele, diet, drug or lifestyle factor is established. A 2024 study found that hypoxia and an NDUFA6-ortholog suppressor allele rescued selected complex-I mutants in *C. elegans*, normalizing forward electron transfer and energetic measures. This is experimental genetic-interaction evidence and **must not be interpreted as support for clinical hypoxia**, which carries substantial risk. Candidate intra-complex modifiers included NDUFS2 and NDUFS7, but no modifier has been validated in patients with MC1DN33. (meisel2024hypoxiaandintracomplex pages 14-16)

## 3. Phenotypes

Across the four reported patients, onset was antenatal/neonatal in one, at 7 weeks in one, at 3 months in one, and around 2 years in one. Two of four died in early infancy, while two survived into childhood with severe progressive motor disability. Because n=4, percentages are descriptive only. (alston2018biallelicmutationsin pages 2-3)

| Subject/demographics | Genotype | Onset/triggers | Major phenotype and MRI | Biochemical findings | Outcome |
|---|---|---|---|---|---|
| **S1:** Hungarian female; term birth; intrauterine growth restriction | Compound heterozygous **NDUFA6** c.191G>C (p.Arg64Pro; likely pathogenic) and c.265G>T (p.Glu89*; pathogenic) | Antenatal ventriculomegaly and cerebellar hypoplasia; severe disease apparent at birth; no postnatal trigger reported | Severe neonatal hypotonia, absent primitive reflexes, hypoglycaemia, metabolic/lactic acidosis, hyperammonaemia, coagulopathy, and abnormal cerebral monitoring. MRI: extensive supratentorial white-matter, brainstem, and cerebellar abnormalities | Lactate **>20 mmol/L**; skeletal-muscle complex I activity **44% of control**; most severe fibroblast complex-I assembly and respiration defect; reduced fully assembled complex I and N/Q-module subunits | Died at approximately **51 hours** (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 2-3, alston2018biallelicmutationsin pages 5-6) |
| **S2:** Kurdish male; parents were second cousins | Homozygous **NDUFA6** c.331_332del (p.Glu111Serfs*35; pathogenic); unaffected sister heterozygous | Weakness at **2 years**; marked gait deterioration after fever at **25 months** | Progressive spasticity, dysphagia, severe motor regression, optic atrophy, and dysarthria; eventually lost voluntary limb movement, with relatively preserved cognition. Serial MRI: progressive disseminated lesions of cerebral white matter, corpus callosum, basal ganglia, brainstem, and cervical spinal cord, followed by atrophy and cystic degeneration; MRS showed elevated lactate | Blood and CSF lactate normal; skeletal-muscle complex I activity **46% of control**; fibroblasts showed reduced complex-I assembly | Alive at last reported follow-up; exact age and subsequent outcome **not reported in gathered evidence** (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 2-3) |
| **S3:** South Asian male; intrauterine growth restriction; parents were first cousins; sparse hair and minor dysmorphism | Homozygous **NDUFA6** c.3G>A (p.?; initiation-codon variant, pathogenic) | Explosive seizures at **3 months**, including status epilepticus; specific trigger not reported | Developmental regression, hypotonia, dystonia, impaired vision, severe developmental delay, feeding/aspiration complications, bronchiectasis, and neutropenia; unable to walk at **10 years**. MRI included basal-ganglia abnormalities; complete MRI description **not available in gathered evidence** | Elevated CSF lactate; muscle and fibroblast complex-I enzymatic activity reportedly normal, but fibroblasts had a marked complex-I assembly defect and impaired growth in galactose-rich/glucose-free medium | Alive at **10 years** with severe motor disability; later outcome **not reported**. Two related males reportedly died from epilepsy (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 2-3, alston2018biallelicmutationsin pages 6-8) |
| **S4:** British female; other demographic details not reported | Compound heterozygous **NDUFA6** c.309del (p.Met104Cysfs*35) and c.355del (p.Leu119Tyrfs*20), confirmed in trans; pathogenic | Seizures at **7 weeks**, progressing to status epilepticus and apnoea; trigger not reported | Severe early infantile encephalopathy. MRI: abnormalities of white matter/corticospinal tracts, brainstem, and thalami | Severe persistent blood and CSF lactic acidosis; tissue respiratory-chain activity and detailed fibroblast functional results **not reported in gathered evidence** | Died at **13 weeks** (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 2-3) |


*Table: Patient-level summary of the four unrelated children reported by Alston et al. in 2018, including genotypes, clinical trajectories, biochemical evidence, and outcomes. Missing details are explicitly identified to prevent unsupported knowledge-base assertions.*

### Phenotype–ontology recommendations

- Intrauterine growth restriction — **HP:0001511**; 2/4 reported.
- Neonatal hypotonia — **HP:0001319**; generalized hypotonia **HP:0001290**.
- Seizures — **HP:0001250**; status epilepticus **HP:0002133**; clinically prominent in at least 2/4.
- Global developmental delay — **HP:0001263**; developmental regression **HP:0002376**.
- Progressive spasticity — **HP:0001257**; dystonia — **HP:0001332**.
- Dysphagia — **HP:0002015**; feeding difficulty — **HP:0011968**; aspiration — **HP:0002835**.
- Optic atrophy — **HP:0000648**; visual impairment — **HP:0000505**.
- Lactic acidosis — **HP:0003128**; elevated CSF lactate — **HP:0011976**.
- Hyperammonemia — **HP:0001987**; hypoglycemia — **HP:0001943**; coagulopathy — **HP:0003256**.
- Cerebral white-matter abnormality — **HP:0002500**; basal-ganglia abnormality — **HP:0002134**; brainstem abnormality — **HP:0002363**; cerebellar hypoplasia — **HP:0001321**; ventriculomegaly — **HP:0002119**.
- Failure to walk/loss of ambulation — **HP:0002540** or **HP:0002355**, depending on exact annotation.
- Bronchiectasis — **HP:0002110**; neutropenia — **HP:0001875**.

Reported manifestations profoundly impaired feeding, mobility, communication, vision and independent daily functioning. No EQ-5D, SF-36, PROMIS or disease-specific quality-of-life measurements have been published for this genotype. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 2-3)

## 4. Genetic and molecular information

**Gene/protein.** NDUFA6 encodes a nuclear-derived mitochondrial complex-I accessory subunit. The disease study supported a 154-residue protein and revision to transcript **NM_002490.5**; transcript ambiguity is clinically important when describing the start-codon allele. NDUFA6 contains a conserved LYR motif involved in binding the mitochondrial acyl-carrier protein NDUFAB1. (alston2018biallelicmutationsin pages 5-6, alston2018biallelicmutationsin pages 3-5)

**Reported germline variants**

1. c.191G>C, p.(Arg64Pro): compound heterozygous; classified likely pathogenic; absent from gnomAD, ClinVar and dbSNP in the 2018 analysis.
2. c.265G>T, p.(Glu89*): compound heterozygous; pathogenic; reported MAF approximately **0.0008%**.
3. c.331_332del, p.(Glu111Serfs*35): homozygous; pathogenic; absent from gnomAD, ClinVar and dbSNP in that analysis.
4. c.3G>A, p.(?): homozygous initiation-codon variant; pathogenic; reported MAF approximately **0.0004%**.
5. c.309del, p.(Met104Cysfs*35): compound heterozygous; pathogenic; reported frequency approximately **0.006%**.
6. c.355del, p.(Leu119Tyrfs*20): in trans with c.309del; pathogenic; reported MAF approximately **0.0004%**.

No allele was observed homozygously in gnomAD. Frequencies are historical values from the publication and should be rechecked against the current gnomAD release before clinical reporting. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 5-6)

All variants are **germline**; no somatic disease mechanism is reported. Functional consequences are loss of protein or defective assembly/stability rather than gain-of-function or dominant-negative action. The terminal-exon frameshift may escape nonsense-mediated decay and produce an abnormal C terminus. (alston2018biallelicmutationsin pages 5-6)

No pathogenic chromosomal rearrangement, recurrent copy-number variant, repeat expansion, disease-specific methylation signature, epigenetic lesion or validated human modifier gene has been reported. SMDT1 appears as a secondary Open Targets association linked to the same literature/ClinVar records, but the primary causal gene for MC1DN33 is NDUFA6; this database signal should not be interpreted as evidence that SMDT1 causes the disorder. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 33)

## 5. Environmental information

MC1DN33 is not infectious, toxic, radiation-induced or lifestyle-mediated. No pathogen has been shown to cause it, and it has no zoonotic transmission. Fever-associated regression in one child is consistent with metabolic decompensation under increased energy demand, but no specific organism was implicated. Avoidance of prolonged fasting, dehydration and catabolic illness is biologically reasonable general mitochondrial care, not proven NDUFA6-specific prevention. (alston2018biallelicmutationsin pages 2-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic NDUFA6 variants lead to** absent, unstable or structurally impaired NDUFA6 protein. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 5-6)
2. **Defective NDUFA6 leads to** impaired interaction with NDUFAB1/mitochondrial acyl-carrier protein, particularly for variants affecting the conserved LYR-domain interface; the precise effect of each allele is partly inferred from structure. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 5-6)
3. **Loss of this late assembly function leads to** reduced incorporation/stability of NDUFA7, NDUFA12 and NDUFAB1 and failure to complete the complex-I N module. (alston2018biallelicmutationsin pages 6-8, alston2018biallelicmutationsin pages 5-6)
4. **Incomplete assembly results in** reduced mature complex I and accumulation of an approximately **830-kDa** NDUFAF2-bound intermediate. This intermediate can associate with complexes III and IV but lacks NADH-dehydrogenase activity. (alston2018biallelicmutationsin pages 6-8)
5. **Reduced functional complex I leads to** impaired oxidation of NADH and electron transfer to ubiquinone, diminished proton pumping and reduced capacity to maintain membrane potential and ATP production; the latter energetic consequences are established complex-I biology and supported indirectly by patient-cell respiration/galactose-growth defects. (alston2018biallelicmutationsin pages 6-8, meisel2024hypoxiaandintracomplex pages 14-16, alston2018biallelicmutationsin pages 5-6)
6. **Energetic failure leads to** increased reliance on glycolysis, lactate accumulation and limited reserve during illness, particularly in energy-demanding neurons, glia, skeletal muscle and respiratory-control circuits. The cell-type attribution is inferred from affected anatomy and general mitochondrial physiology, not demonstrated by NDUFA6 single-cell data. (alston2018biallelicmutationsin pages 2-3)
7. **Brain energy failure results in** developmental regression, seizures, tone abnormalities, optic injury and progressive symmetric/diffuse white-matter, basal-ganglia, brainstem, thalamic and corticospinal-tract lesions; severe systemic failure can produce hypoglycemia, hyperammonemia, coagulopathy, apnea and early death. (alston2018biallelicmutationsin pages 2-3)

### Pathway and ontology annotations

- Reactome/KEGG concepts: respiratory electron transport; complex-I assembly; oxidative phosphorylation; NADH oxidation; proton-motive-force generation; ATP synthesis.
- Suggested GO biological processes: **mitochondrial respiratory chain complex I assembly (GO:0032981)**, **mitochondrial electron transport, NADH to ubiquinone (GO:0006120)**, **oxidative phosphorylation (GO:0006119)**, **ATP synthesis coupled electron transport (GO:0042773)** and **cellular response to hypoxia (GO:0071456)** for experimental modifier work.
- GO molecular function: **NADH dehydrogenase (ubiquinone) activity (GO:0008137)** applies to the complex rather than NDUFA6 catalysis itself.
- GO cellular components: **mitochondrial inner membrane (GO:0005743)**, **respiratory-chain complex I (GO:0005747)** and **mitochondrial respirasome (GO:0005746)**.
- Candidate Cell Ontology terms: neuron **CL:0000540**, oligodendrocyte **CL:0000128**, astrocyte **CL:0000127**, skeletal-muscle cell **CL:0000188**, cardiomyocyte **CL:0000746**. These are vulnerability candidates; NDUFA6-specific single-cell validation is unavailable.

There is no disease-specific transcriptomic, lipidomic, methylomic, spatial-transcriptomic or single-cell atlas. Complexome profiling and patient-fibroblast proteomic/assembly analyses constitute the most informative molecular profiling: they showed loss of mature complex I, depletion of N/Q-module components and a stalled assembly intermediate. (alston2018biallelicmutationsin pages 6-8, alston2018biallelicmutationsin pages 5-6)

## 7. Anatomical structures affected

The **central nervous system** is primary: cerebral white matter, corpus callosum, basal ganglia, thalami, brainstem, corticospinal tracts, cervical spinal cord and cerebellum were affected across patients. Optic pathways were involved through optic atrophy/visual impairment. Skeletal muscle showed biochemical complex-I deficiency in two patients, although overt primary myopathy was not uniformly documented. Respiratory and gastrointestinal systems were secondarily affected through apnea, dysphagia, aspiration and bronchiectasis. (alston2018biallelicmutationsin pages 2-3)

Suggested UBERON terms include brain **UBERON:0000955**, cerebral white matter **UBERON:0002437**, basal ganglion **UBERON:0002420**, brainstem **UBERON:0002298**, thalamus **UBERON:0001897**, cerebellum **UBERON:0002037**, corpus callosum **UBERON:0002336**, spinal cord **UBERON:0002240**, optic nerve **UBERON:0000962**, and skeletal muscle tissue **UBERON:0001134**. Lesions were multifocal and often bilateral/diffuse; no consistent unilateral lateralization was reported. Subcellular localization is the mitochondrial inner membrane/complex-I assembly environment.

## 8. Temporal development

- **Onset:** congenital/neonatal to age 2 years; all known cases were pediatric.
- **Course:** severe neonatal presentations were rapidly fatal, whereas childhood cases were progressive, sometimes with acute regression during seizures or febrile illness.
- **Stages:** no validated staging system exists. A practical natural-history description is presymptomatic/antenatal abnormality → metabolic or neurologic onset → regression/progressive motor impairment → multisystem complications and, in severe cases, respiratory failure/death.
- **Remission:** no spontaneous or treatment-induced durable remission has been documented.
- **Critical period:** infancy and early childhood appear maximally vulnerable, and catabolic illness may precipitate deterioration; this inference is based on four cases. (alston2018biallelicmutationsin pages 2-3)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. The published families include affected males and females, with no evidence of sex bias. Penetrance appears high for individuals carrying two severe alleles, but it cannot be quantified. Expressivity is clearly variable: survival ranged from approximately 51 hours to at least 10 years. No anticipation, confirmed germline mosaicism or founder variant has been established. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 2-3)

Prevalence, incidence, carrier frequency, geographic distribution and sex ratio are unknown. Four unrelated index cases of Hungarian, Kurdish, South Asian and British backgrounds demonstrate that the disorder is not confined to one population, but these cases cannot support demographic rate estimates. Two consanguineous families illustrate recessive-risk enrichment rather than a quantified population effect. (alston2018biallelicmutationsin pages 2-3)

## 10. Diagnostics

### Recommended workflow

1. **Clinical suspicion:** neonatal metabolic encephalopathy, unexplained lactic acidosis, early seizures/regression, progressive spastic-dystonic disease, optic atrophy, or Leigh/white-matter MRI patterns.
2. **Biochemical testing:** blood and CSF lactate, pyruvate, glucose, ammonia, acid–base status, liver/coagulation studies, plasma amino acids, acylcarnitines and urine organic acids. A normal lactate does **not** exclude disease: one molecularly affected child had normal blood/CSF lactate. (alston2018biallelicmutationsin pages 2-3)
3. **Imaging:** brain MRI with diffusion and, where available, proton MRS. Relevant sites include white matter, basal ganglia, brainstem, thalami, cerebellum and corticospinal tracts; MRS may reveal lactate. (alston2018biallelicmutationsin pages 2-3)
4. **Molecular testing:** trio WES or WGS, or a comprehensive mitochondrial/Leigh/complex-I panel including **NDUFA6**. Confirm candidate variants by segregation and ensure annotation against the clinically appropriate NDUFA6 transcript, given the documented transcript revision. (alston2018biallelicmutationsin pages 5-6, alston2018biallelicmutationsin pages 8-9)
5. **Functional confirmation when needed:** respiratory-chain enzymology in muscle or fibroblasts; BN-PAGE/complexome profiling; oxygen-consumption studies; galactose-growth testing; and complementation. Muscle complex-I activity was only 44% and 46% of control in two cases, but another patient had normal muscle/fibroblast enzymatic activity despite a clear assembly defect—so normal single-tissue enzymology does not exclude MC1DN33. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 8-9, alston2018biallelicmutationsin pages 6-8)
6. **RNA/protein studies:** RNA sequencing may resolve splice or expression effects in unsolved mitochondrial disease, while complexome/proteomic analysis can demonstrate defective assembly. These are specialist second-line tests rather than population screening. (alston2020pathogenicbiallelicmutations pages 8-9, alston2018biallelicmutationsin pages 5-6)

CMA, karyotyping and FISH are not first-line for this single-gene recessive disorder unless syndromic features suggest a copy-number/chromosomal diagnosis. mtDNA sequencing remains important in a broad mitochondrial differential but will not detect nuclear NDUFA6 variants. Repeat-expansion testing is not indicated specifically.

**Differential diagnosis:** other nuclear or mtDNA complex-I deficiencies; Leigh syndrome due to NDUFS4, NDUFAF genes or other OXPHOS genes; pyruvate-dehydrogenase deficiency; POLG-related disease; mitochondrial translation disorders; organic acidemias; urea-cycle defects; hypoxic–ischemic injury; leukodystrophies; and epileptic encephalopathies. Molecular confirmation is decisive because clinical and MRI findings overlap extensively.

No population newborn screen exists. Cascade testing of relatives and reproductive carrier testing are appropriate after a familial variant is known.

## 11. Outcome and prognosis

Two of the four published patients died at approximately **51 hours** and **13 weeks**; one was alive with profound motor disability and inability to walk at age 10; another had progressive spasticity, dysphagia, optic atrophy and loss of voluntary limb movement. These observations indicate potentially high infant mortality and severe long-term neurologic morbidity, but 5- or 10-year survival, median life expectancy and disease-specific mortality rates cannot be calculated from four cases. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 2-3)

Likely adverse prognostic features include antenatal abnormalities, neonatal onset, severe persistent lactic acidosis, apnea, extensive brainstem involvement and severe complex-I assembly/respiration defects. The original study noted that biochemical severity broadly tracked clinical severity, but genotype–prognosis rules remain unvalidated. (alston2018biallelicmutationsin pages 2-3, alston2018biallelicmutationsin pages 5-6)

## 12. Treatment and current applications

There is **no approved NDUFA6-targeted or disease-modifying treatment**, no published genotype-specific response rate, and no demonstrated gene, RNA or cell therapy. Current real-world care is multidisciplinary and supportive:

- acute management of hypoglycemia, acidosis, seizures, apnea and hyperammonemia;
- avoidance of fasting and prompt provision of calories/fluids during illness;
- antiseizure therapy selected with mitochondrial safety in mind;
- nutritional assessment and enteral feeding when aspiration or dysphagia threatens safety;
- respiratory support and treatment of aspiration-related infection;
- physical, occupational, speech/feeding and assistive-mobility therapy;
- ophthalmology, audiology, neurology, metabolic, cardiac and respiratory surveillance.

These recommendations are extrapolated from mitochondrial/Leigh care, not tested specifically in MC1DN33. Vitamins, cofactors, antioxidants and amino-acid supplements are used empirically in Leigh syndrome, but they have not cured the disorder and are not established definitive therapies. (hord2025thecurrentstate pages 5-6)

Broader Leigh/nuclear-primary-mitochondrial-disease development programs have evaluated redox modulators such as vatiquinone/EPI-743 and sonlicromanol/KH176, complex-I bypass concepts such as succinate prodrugs, mTOR inhibition/sirolimus and mitochondrial membrane-targeted agents. None has demonstrated NDUFA6-specific efficacy. Model data for KH176 and hypoxia/suppressor biology remain preclinical and incompletely correct pathology or survival. (hord2025thecurrentstate pages 5-6, meisel2024hypoxiaandintracomplex pages 14-16)

Suggested NCIt intervention concepts include **Supportive Care**, **Anticonvulsant Therapy**, **Enteral Nutrition**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Respiratory Support**, **Genetic Counseling**, **Gene Therapy** and **Genome Editing**; the last two are research concepts only. Exact NCIt codes should be terminology-server validated before ingestion.

## 13. Prevention

Primary prevention through lifestyle change or vaccination is not possible for a germline recessive disorder. Reproductive prevention options after familial variants are established include carrier testing, partner testing, preimplantation genetic testing for monogenic disease, chorionic-villus sampling, amniocentesis and use of donor gametes. Each pregnancy of two confirmed carriers has the standard autosomal-recessive probabilities: 25% affected, 50% heterozygous carrier and 25% unaffected/non-carrier.

Secondary prevention consists of early molecular diagnosis, cascade testing and anticipatory monitoring. Tertiary prevention aims to reduce metabolic decompensation, aspiration, malnutrition, contractures, immobility and respiratory complications. No prophylactic medication or NDUFA6-specific newborn screening program exists.

## 14. Other species and natural disease

No naturally occurring veterinary NDUFA6 disease, breed predisposition or cross-species transmission was identified. NDUFA6/LYRM-family biology is evolutionarily conserved, particularly the LYR-domain interaction with acyl-carrier protein. Relevant comparative taxa include *Homo sapiens* (**NCBI Taxon 9606**), *Mus musculus* (**10090**) and *Caenorhabditis elegans* (**6239**). The disorder is inherited, not infectious or zoonotic. (alston2018biallelicmutationsin pages 3-5, meisel2024hypoxiaandintracomplex pages 14-16)

## 15. Model organisms and experimental systems

**Human patient fibroblasts** are the disease-defining model. BN-PAGE, complexome profiling, respirometry and galactose-growth assays reproduced the complex-I defect. Lentiviral expression of wild-type NDUFA6 restored mature complex-I abundance and in-gel activity, providing the strongest functional validation. Limitations include tissue-specificity and inability of fibroblasts to reproduce brain development or neuronal circuitry. (alston2018biallelicmutationsin pages 8-9, alston2018biallelicmutationsin pages 6-8, alston2018biallelicmutationsin pages 5-6)

In **C. elegans**, NDUFA6 ortholog **nuo-3(G60D)** acted as an intra-complex suppressor of selected matrix-arm complex-I mutants. It restored forward NADH-to-ubiquinone transfer without necessarily restoring complex-I abundance and improved oxygen consumption, ATP, membrane potential and NADH/NAD+ balance. This model is valuable for structural epistasis and suppressor discovery but does not reproduce the human biallelic loss-of-function phenotype or establish therapeutic safety. (meisel2024hypoxiaandintracomplex pages 14-16)

No disease-specific Ndufa6 knockout/knock-in mouse, zebrafish, Drosophila, patient-derived iPSC-neuron or brain-organoid model was documented in the retrieved evidence. Ndufs4-null Leigh mice are useful for general complex-I pathophysiology and intervention development but are not NDUFA6 models.

## Current interpretation and key knowledge gaps

The expert interpretation supported by the available evidence is that MC1DN33 is a **complex-I assembly disorder with extreme allelic and clinical severity**, rather than a uniform classic Leigh syndrome. The decisive diagnostic lesson is that neither normal circulating lactate nor normal muscle complex-I activity excludes it: assembly analysis and genomic testing may be required. (alston2018biallelicmutationsin pages 8-9, alston2018biallelicmutationsin pages 6-8, alston2018biallelicmutationsin pages 2-3)

Priority research needs are: additional natural-history cases; updated ClinVar/gnomAD curation; standardized transcript annotation; neuronal and organoid models; quantitative ATP, membrane-potential, ROS and metabolomic studies; genotype–phenotype analysis; and evaluation of whether complex-I bypass, redox or intra-complex suppressor strategies are relevant to NDUFA6 deficiency. At present, proposed modifier and treatment mechanisms remain preclinical, and clinical management should not extend beyond established mitochondrial-disease practice without trial oversight. (hord2025thecurrentstate pages 5-6, meisel2024hypoxiaandintracomplex pages 14-16)

### Key primary and recent sources

1. Alston CL et al. “Bi-allelic Mutations in NDUFA6 Establish Its Role in Early-Onset Isolated Mitochondrial Complex I Deficiency.” *American Journal of Human Genetics*. Published October 2018. PMID **30245030**. https://doi.org/10.1016/j.ajhg.2018.08.013. The study’s central conclusion was that biallelic NDUFA6 variants were identified in four pediatric subjects and that complex-I assembly defects plus lentiviral rescue established causality. (alston2018biallelicmutationsin pages 3-5, alston2018biallelicmutationsin pages 8-9)
2. Meisel JD et al. “Hypoxia and intra-complex genetic suppressors rescue complex I mutants by a shared mechanism.” *Cell*. Published February 2024. https://doi.org/10.1016/j.cell.2023.12.010. This provides recent model-organism evidence for NDUFA6-related structural suppression, not human therapeutic evidence. (meisel2024hypoxiaandintracomplex pages 14-16)
3. Fernandez-Vizarra E, Zeviani M. “Mitochondrial disorders of the OXPHOS system.” *FEBS Letters*. 2021. https://doi.org/10.1002/1873-3468.13995. The review lists NDUFA6/OMIM 602138 and the associated phenotype OMIM 618253 as early-onset complex-I deficiency/mitochondrial encephalopathy. (fernandez‐vizarra2021mitochondrialdisordersof pages 92-96)

References

1. (alston2018biallelicmutationsin pages 3-5): Charlotte L. Alston, Juliana Heidler, Marris G. Dibley, Laura S. Kremer, Lucie S. Taylor, Carl Fratter, Courtney E. French, Ruth I.C. Glasgow, René G. Feichtinger, Isabelle Delon, Alistair T. Pagnamenta, Helen Dolling, Hugh Lemonde, Neil Aiton, Alf Bjørnstad, Lisa Henneke, Jutta Gärtner, Holger Thiele, Katerina Tauchmannova, Gerardine Quaghebeur, Josef Houstek, Wolfgang Sperl, F. Lucy Raymond, Holger Prokisch, Johannes A. Mayr, Robert McFarland, Joanna Poulton, Michael T. Ryan, Ilka Wittig, Marco Henneke, and Robert W. Taylor. Bi-allelic mutations in ndufa6 establish its role in early-onset isolated mitochondrial complex i deficiency. Oct 2018. URL: https://doi.org/10.1016/j.ajhg.2018.08.013, doi:10.1016/j.ajhg.2018.08.013. This article has 81 citations.

2. (alston2018biallelicmutationsin pages 8-9): Charlotte L. Alston, Juliana Heidler, Marris G. Dibley, Laura S. Kremer, Lucie S. Taylor, Carl Fratter, Courtney E. French, Ruth I.C. Glasgow, René G. Feichtinger, Isabelle Delon, Alistair T. Pagnamenta, Helen Dolling, Hugh Lemonde, Neil Aiton, Alf Bjørnstad, Lisa Henneke, Jutta Gärtner, Holger Thiele, Katerina Tauchmannova, Gerardine Quaghebeur, Josef Houstek, Wolfgang Sperl, F. Lucy Raymond, Holger Prokisch, Johannes A. Mayr, Robert McFarland, Joanna Poulton, Michael T. Ryan, Ilka Wittig, Marco Henneke, and Robert W. Taylor. Bi-allelic mutations in ndufa6 establish its role in early-onset isolated mitochondrial complex i deficiency. Oct 2018. URL: https://doi.org/10.1016/j.ajhg.2018.08.013, doi:10.1016/j.ajhg.2018.08.013. This article has 81 citations.

3. (alston2018biallelicmutationsin pages 5-6): Charlotte L. Alston, Juliana Heidler, Marris G. Dibley, Laura S. Kremer, Lucie S. Taylor, Carl Fratter, Courtney E. French, Ruth I.C. Glasgow, René G. Feichtinger, Isabelle Delon, Alistair T. Pagnamenta, Helen Dolling, Hugh Lemonde, Neil Aiton, Alf Bjørnstad, Lisa Henneke, Jutta Gärtner, Holger Thiele, Katerina Tauchmannova, Gerardine Quaghebeur, Josef Houstek, Wolfgang Sperl, F. Lucy Raymond, Holger Prokisch, Johannes A. Mayr, Robert McFarland, Joanna Poulton, Michael T. Ryan, Ilka Wittig, Marco Henneke, and Robert W. Taylor. Bi-allelic mutations in ndufa6 establish its role in early-onset isolated mitochondrial complex i deficiency. Oct 2018. URL: https://doi.org/10.1016/j.ajhg.2018.08.013, doi:10.1016/j.ajhg.2018.08.013. This article has 81 citations.

4. (meisel2024hypoxiaandintracomplex pages 14-16): Joshua D. Meisel, Maria Miranda, Owen S. Skinner, Presli P. Wiesenthal, Sandra M. Wellner, Alexis A. Jourdain, Gary Ruvkun, and Vamsi K. Mootha. Hypoxia and intra-complex genetic suppressors rescue complex i mutants by a shared mechanism. Feb 2024. URL: https://doi.org/10.1016/j.cell.2023.12.010, doi:10.1016/j.cell.2023.12.010. This article has 9 citations and is from a highest quality peer-reviewed journal.

5. (alston2018biallelicmutationsin pages 2-3): Charlotte L. Alston, Juliana Heidler, Marris G. Dibley, Laura S. Kremer, Lucie S. Taylor, Carl Fratter, Courtney E. French, Ruth I.C. Glasgow, René G. Feichtinger, Isabelle Delon, Alistair T. Pagnamenta, Helen Dolling, Hugh Lemonde, Neil Aiton, Alf Bjørnstad, Lisa Henneke, Jutta Gärtner, Holger Thiele, Katerina Tauchmannova, Gerardine Quaghebeur, Josef Houstek, Wolfgang Sperl, F. Lucy Raymond, Holger Prokisch, Johannes A. Mayr, Robert McFarland, Joanna Poulton, Michael T. Ryan, Ilka Wittig, Marco Henneke, and Robert W. Taylor. Bi-allelic mutations in ndufa6 establish its role in early-onset isolated mitochondrial complex i deficiency. Oct 2018. URL: https://doi.org/10.1016/j.ajhg.2018.08.013, doi:10.1016/j.ajhg.2018.08.013. This article has 81 citations.

6. (fernandez‐vizarra2021mitochondrialdisordersof pages 92-96): Erika Fernandez‐Vizarra and Massimo Zeviani. Mitochondrial disorders of the oxphos system. Dec 2021. URL: https://doi.org/10.1002/1873-3468.13995, doi:10.1002/1873-3468.13995. This article has 412 citations and is from a peer-reviewed journal.

7. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 33): Open Targets Query (Mitochondrial complex I deficiency, nuclear type 33, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (alston2018biallelicmutationsin pages 6-8): Charlotte L. Alston, Juliana Heidler, Marris G. Dibley, Laura S. Kremer, Lucie S. Taylor, Carl Fratter, Courtney E. French, Ruth I.C. Glasgow, René G. Feichtinger, Isabelle Delon, Alistair T. Pagnamenta, Helen Dolling, Hugh Lemonde, Neil Aiton, Alf Bjørnstad, Lisa Henneke, Jutta Gärtner, Holger Thiele, Katerina Tauchmannova, Gerardine Quaghebeur, Josef Houstek, Wolfgang Sperl, F. Lucy Raymond, Holger Prokisch, Johannes A. Mayr, Robert McFarland, Joanna Poulton, Michael T. Ryan, Ilka Wittig, Marco Henneke, and Robert W. Taylor. Bi-allelic mutations in ndufa6 establish its role in early-onset isolated mitochondrial complex i deficiency. Oct 2018. URL: https://doi.org/10.1016/j.ajhg.2018.08.013, doi:10.1016/j.ajhg.2018.08.013. This article has 81 citations.

9. (alston2020pathogenicbiallelicmutations pages 8-9): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

10. (hord2025thecurrentstate pages 5-6): C Hord, A Dinchman, and P Kang. The current state of the mitochondrial diseases lhon, melas and leigh syndrome and their treatments: a review. Unknown journal, 2025.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_33-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032636` (4 mentions) - the report calls it "if available"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 33**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (1 mention) - replaced by `HP:0001288`
- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`
- `GO:0005746` (obsolete mitochondrial respirasome) (1 mention) - replaced by `GO:0098803`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005743` (1 mention) - the report calls it "GO cellular components: **mitochondrial inner membrane"; GO calls it **mitochondrial inner membrane**
