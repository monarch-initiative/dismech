---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T14:47:59.797179'
end_time: '2026-09-04T15:01:08.705606'
duration_seconds: 788.91
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: "Intellectual disability autosomal dominant 16, MRD16, OMIM 614609,\
    \ also called Coffin-Siris syndrome 4 or CSS4 \u2014 the SMARCA4-related BAFopathy.\
    \ Caused by heterozygous de novo non-truncating variants in SMARCA4, the BRG1\
    \ catalytic ATPase subunit of the BAF/SWI-SNF chromatin remodelling complex. This\
    \ is the germline neurodevelopmental SMARCA4 disorder, NOT SMARCA4-deficient rhabdoid\
    \ tumour predisposition syndrome type 2 and NOT SMARCA2 Nicolaides-Baraitser syndrome."
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 61
  verified: 61
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Intellectual_Disability_Autosomal_Dominant_16-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual disability autosomal dominant 16, MRD16, OMIM 614609, also called Coffin-Siris syndrome 4 or CSS4 — the SMARCA4-related BAFopathy. Caused by heterozygous de novo non-truncating variants in SMARCA4, the BRG1 catalytic ATPase subunit of the BAF/SWI-SNF chromatin remodelling complex. This is the germline neurodevelopmental SMARCA4 disorder, NOT SMARCA4-deficient rhabdoid tumour predisposition syndrome type 2 and NOT SMARCA2 Nicolaides-Baraitser syndrome.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual disability autosomal dominant 16, MRD16, OMIM 614609, also called Coffin-Siris syndrome 4 or CSS4 — the SMARCA4-related BAFopathy. Caused by heterozygous de novo non-truncating variants in SMARCA4, the BRG1 catalytic ATPase subunit of the BAF/SWI-SNF chromatin remodelling complex. This is the germline neurodevelopmental SMARCA4 disorder, NOT SMARCA4-deficient rhabdoid tumour predisposition syndrome type 2 and NOT SMARCA2 Nicolaides-Baraitser syndrome.** covering all of the
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
- **Disease Name:** Intellectual disability autosomal dominant 16, MRD16, OMIM 614609, also called Coffin-Siris syndrome 4 or CSS4 — the SMARCA4-related BAFopathy. Caused by heterozygous de novo non-truncating variants in SMARCA4, the BRG1 catalytic ATPase subunit of the BAF/SWI-SNF chromatin remodelling complex. This is the germline neurodevelopmental SMARCA4 disorder, NOT SMARCA4-deficient rhabdoid tumour predisposition syndrome type 2 and NOT SMARCA2 Nicolaides-Baraitser syndrome.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual disability autosomal dominant 16, MRD16, OMIM 614609, also called Coffin-Siris syndrome 4 or CSS4 — the SMARCA4-related BAFopathy. Caused by heterozygous de novo non-truncating variants in SMARCA4, the BRG1 catalytic ATPase subunit of the BAF/SWI-SNF chromatin remodelling complex. This is the germline neurodevelopmental SMARCA4 disorder, NOT SMARCA4-deficient rhabdoid tumour predisposition syndrome type 2 and NOT SMARCA2 Nicolaides-Baraitser syndrome.** covering all of the
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


# SMARCA4-related Coffin–Siris syndrome 4 (CSS4/MRD16): disease-characteristics report

**Scope.** This report concerns the germline neurodevelopmental disorder caused by heterozygous pathogenic **SMARCA4** variants—Coffin–Siris syndrome 4 (CSS4), also called intellectual developmental disorder, autosomal dominant 16 (MRD16). It does **not** treat SMARCA4-related rhabdoid tumor predisposition syndrome 2 (RTPS2), somatic SMARCA4-deficient cancers, or **SMARCA2**-related Nicolaides–Baraitser syndrome (NCBRS) as the same disease. Evidence is limited by very small cohorts, variable ascertainment, and frequent use of data aggregated across genetically heterogeneous Coffin–Siris syndromes.

## Executive summary

CSS4 is a congenital, lifelong, variably expressive BAFopathy. Developmental delay/intellectual disability, speech and behavioral differences, feeding problems, growth impairment, characteristic facial and hair findings, and variable fifth-digit/nail hypoplasia form the core phenotype. Cardiac, airway, hearing, ophthalmologic, skeletal, and CNS abnormalities can materially affect morbidity. In a 15-person SMARCA4 cohort, 12 variants were missense and 11/12 lay within residues 761–1,243 around the helicase/ATPase domains; most confirmed variants were de novo. A separate 12-person registry subset found fifth-digit anomalies in 58%, hypertrichosis in 50%, microcephaly in 42%, hearing loss in 33%, scoliosis in 42%, and seizures in 8%, although these parent-reported estimates are imprecise. (li2020thevariabilityof pages 2-3, mannino2018firstdatafrom pages 3-5, mannino2018firstdatafrom pages 5-6)

There is no curative or disease-modifying therapy. Current implementation is molecular diagnosis followed by multidisciplinary supportive care, early developmental intervention, and organ-directed surveillance. No SMARCA4-CSS4 interventional trial was identified. (vergano2025coffinsirissyndrome pages 15-17, vergano2025coffinsirissyndrome pages 17-19, vergano2025coffinsirissyndromec pages 1-4)

| Domain | Best quantitative finding | Evidence type/source/date | Interpretation/limitation |
|---|---|---|---|
| Clinical and variant spectrum | **15 unrelated individuals; 14 different SMARCA4 variants; 12 missense variants, of which 11/12 mapped to residues 761–1,243 in or near the helicase/ATPase domains.** Ten of 12 missense variants were confirmed de novo; parental data were unavailable for two. | Human CSS4 registry cohort; Li et al., July 2020; DOI: [10.1002/ajmg.a.61732](https://doi.org/10.1002/ajmg.a.61732) (li2020thevariabilityof pages 2-3, li2020thevariabilityof pages 5-7) | Supports enrichment of pathogenic non-truncating variants in critical BRG1 domains and marked clinical variability. The small, clinically ascertained cohort cannot establish population penetrance or precise genotype–phenotype rules. |
| Development and classic morphology | In the **12-person SMARCA4 subset**, fifth-digit anomalies occurred in **7/12 (58%)**, sparse scalp hair in **4/12 (33%)**, hypertrichosis or hirsutism in **6/12 (50%)**, high or cleft palate in **6/12 (50%)**, and microcephaly in **5/12 (42%)**. | Parent-reported human CSS/BAF registry; Mannino et al., October 2018; DOI: [10.1002/ajmg.a.40471](https://doi.org/10.1002/ajmg.a.40471) (mannino2018firstdatafrom pages 3-5) | Absence of fifth-digit hypoplasia or other classic findings does not exclude CSS4. Parent reporting, missing observations, age-dependent ascertainment, and the small denominator limit precision. |
| Developmental milestones | Median ages in the SMARCA4 subset were **rolling 8 months, sitting 12 months, crawling 15 months, walking 26 months, and first words 15.5 months**. | Parent-reported human registry, n=12; Mannino et al., October 2018 (mannino2018firstdatafrom pages 3-5) | Demonstrates early developmental delay, particularly gross-motor delay. Medians do not describe the full range, intellectual-disability severity, or adult adaptive outcome. |
| Neurologic, musculoskeletal, and feeding findings | Seizures **1/12 (8%)**, hypotonia **2/12 (17%)**, corpus-callosum abnormalities **2/12 (17%)**, scoliosis **5/12 (42%)**, kyphosis **4/12 (33%)**, feeding-tube use **2/12 (17%)**, and constipation **5/12 (42%)**. | Parent-reported human registry, n=12; Mannino et al., October 2018 (mannino2018firstdatafrom pages 3-5, mannino2018firstdatafrom pages 5-6) | Indicates multisystem morbidity but may underestimate findings requiring formal examination, imaging, or age-dependent diagnosis. The reported autism or intellectual-delay value of 4/12 should not be interpreted as the true frequency of developmental impairment. |
| Cardiopulmonary involvement | Registry findings included heart murmur **2/12 (17%)**, PFO or PDA **1/12 (8%)**, VSD **1/12 (8%)**, valve stenosis **1/12 (8%)**, coarctation **1/12 (8%)**, airway malacia **4/12 (33%)**, and obstructive sleep apnea **3/12 (25%)**. A separate 15-person cohort reported congenital heart disease in approximately **50%**, ranging from PFO or PDA to tetralogy of Fallot. | Human registries and cohort; Mannino et al., October 2018; Li et al., July 2020 (mannino2018firstdatafrom pages 5-6, li2020thevariabilityof pages 8-9) | Cardiac disease may be clinically important and occasionally severe, supporting baseline cardiac assessment. Differences between estimates probably reflect cohort composition, definitions, and ascertainment. |
| Hearing and vision | Hearing loss **4/12 (33%)**, myopia **3/12 (25%)**, strabismus **3/12 (25%)**, astigmatism **2/12 (17%)**, and retinal abnormality, nystagmus, ptosis, or cortical visual impairment each **1/12 (8%)**. | Parent-reported human registry, n=12; Mannino et al., October 2018 (mannino2018firstdatafrom pages 5-6) | Supports formal audiology and ophthalmology surveillance. Small counts and lack of standardized examination limit phenotype-frequency estimates. |
| Epigenomic biomarker | A peripheral-blood BAFopathy DNA-methylation classifier used probes with **at least 5% methylation difference**, retained probes with **AUC greater than 0.85**, used a radial-basis-function support-vector machine with **10-fold cross-validation**, and classified at a **0.5** probability threshold. | Human CSS/NCBRS methylation study; Aref-Eshghi et al., November 2018; DOI: [10.1038/s41467-018-07193-y](https://doi.org/10.1038/s41467-018-07193-y) (arefeshghi2018bafopathies’dnamethylation pages 6-7, arefeshghi2018bafopathies’dnamethylation pages 14-15) | Potential adjunct for ambiguous BAFopathy cases and SMARCA4 VUS assessment, not a stand-alone diagnostic test. The retrieved evidence does not provide SMARCA4-only sensitivity or specificity, and the signature overlaps other BAFopathies. |
| Current management and trials | **No cure** is available. Care is multidisciplinary and supportive: early developmental intervention, PT/OT, speech and feeding therapy, AAC when needed, and standard treatment of seizures and behavioral, cardiac, orthopedic, hearing, vision, sleep, and nutritional problems. No SMARCA4-CSS4 disease-modifying interventional trial was identified in the search. | Current expert synthesis; GeneReviews comprehensive update, **15 May 2025** (vergano2025coffinsirissyndrome pages 15-17, vergano2025coffinsirissyndrome pages 17-19, vergano2025coffinsirissyndromec pages 1-4) | Recommendations are largely general CSS guidance rather than evidence from SMARCA4-specific controlled trials. Treatment-response rates and genotype-directed pharmacotherapy are unavailable. |
| Allele context versus RTPS2 | Typical CSS4 alleles are predominantly **de novo missense or in-frame variants** affecting ATPase/helicase regions and are interpreted as dominant-negative or gain-of-function; RTPS2 is associated predominantly with **truncating loss-of-function variants**. Rare CSS-like phenotypes from nonsense variants or whole-gene deletions demonstrate biological overlap. | Human CSS4 cohort, deletion case, structural synthesis, and expert review; 2020–2025 (mitrakos2020coffinsirissyndrome4related pages 4-4, li2020thevariabilityof pages 5-7, vergano2025coffinsirissyndrome pages 22-25) | CSS4 and RTPS2 must not be conflated. Cancer risk for canonical non-truncating CSS4 variants is unquantified; individualized cancer-genetics review is reasonable for truncating or deletion alleles, but routine RTPS2 surveillance cannot automatically be extrapolated to all CSS4 patients. |


*Table: Compact evidence summary of the principal human cohorts, phenotype frequencies, molecular diagnostic findings, management status, and allele-specific distinction between SMARCA4-related CSS4 and RTPS2. Small cohorts and overlapping BAFopathy signatures require cautious interpretation.*

## 1. Disease information

### Definition and identifiers

CSS4 is an autosomal-dominant congenital malformation/neurodevelopmental syndrome caused by a heterozygous germline pathogenic or likely pathogenic variant in **SMARCA4**, which encodes BRG1, the catalytic ATPase of mammalian SWI/SNF—also called BRG1/BRM-associated factor (BAF)—chromatin-remodeling complexes. The disease results from disordered developmental gene regulation rather than an enzyme deficiency, infection, toxic exposure, or degenerative process. The current GeneReviews molecular framework assigns dominant-negative or gain-of-function effects to typical SMARCA4 CSS alleles, while primary reports show that selected truncating variants and deletions can produce a milder CSS-like phenotype through haploinsufficiency. (mitrakos2020coffinsirissyndrome4related pages 4-4, li2020thevariabilityof pages 5-7, vergano2025coffinsirissyndrome pages 22-25)

* **OMIM disease:** 614609, CSS4/MRD16.
* **OMIM gene:** 603254, **SMARCA4**. (vergano2025coffinsirissyndrome pages 22-25)
* **HGNC symbol:** SMARCA4; protein aliases include BRG1 and BAF190A.
* **Inheritance:** autosomal dominant, usually de novo.
* **Synonyms:** Coffin–Siris syndrome 4; CSS4; intellectual disability/developmental disorder, autosomal dominant 16; MRD16; SMARCA4-related Coffin–Siris syndrome; SMARCA4-related BAFopathy.
* **MONDO/Orphanet/MeSH:** A CSS4-specific MONDO identifier, Orphanet identifier, and MeSH heading were not verified in the retrieved evidence. A knowledge base should not substitute the broad “Coffin–Siris syndrome” identifier without recording the SMARCA4 molecular subtype.
* **ICD:** no verified CSS4-specific ICD-10 or ICD-11 code was found; implementations commonly require broader congenital-malformation, developmental-disability, or rare-disease coding plus the molecular diagnosis.

The principal evidence is **aggregated disease-level research**: international registries, published case series, GeneReviews, and molecular studies. The 2018 registry was parent-reported rather than an EHR-derived population cohort; individual case reports supply additional patient-level evidence. (mannino2018firstdatafrom pages 3-5, mannino2018firstdatafrom pages 6-8)

### Essential exclusion

Canonical CSS4 generally involves de novo missense or in-frame variants in functionally constrained ATPase/helicase regions. RTPS2 is an allelic but clinically different cancer-predisposition syndrome, classically associated with germline loss-of-function alleles. Rare nonsense variants, deletions, and patients with both developmental and neoplastic findings create a genuine boundary zone, so allele-specific cancer-genetics review is preferable to automatically assigning either diagnosis. SMARCA2-related NCBRS is caused by a different ATPase paralog and remains a differential diagnosis, despite overlapping BAFopathy methylation profiles. (mitrakos2020coffinsirissyndrome4related pages 4-4, li2020thevariabilityof pages 5-7, arefeshghi2018bafopathies’dnamethylation pages 6-7, vergano2025coffinsirissyndrome pages 22-25)

## 2. Etiology, risk, protection, and environment

The initiating cause is a heterozygous germline **SMARCA4** pathogenic variant, usually arising de novo. In the 15-person series, 10/12 missense variants with available parental testing were confirmed de novo; parental samples were unavailable for two. These rare variants were absent from the population databases used by the investigators and were classified as pathogenic or likely pathogenic using ACMG evidence. (li2020thevariabilityof pages 2-3)

No validated susceptibility loci, modifier genes, protective alleles, environmental risk factors, infectious triggers, lifestyle causes, or gene–environment interactions have been demonstrated for CSS4. Maternal diet, smoking, alcohol, occupation, pollutants, and common infections should therefore not be described as causes. Family history is commonly negative because most cases are de novo. Parental age effects, sex-specific penetrance, and ancestry-specific risk have not been established.

No disease-specific protective diet, supplement, medication, or behavior is known. General measures—safe feeding, vaccination, physical activity adapted to ability, and prevention of aspiration or orthopedic complications—protect health but do not prevent the molecular disorder.

## 3. Phenotypes

The best gene-specific frequencies come from only 12 parent-reported individuals; denominators and ascertainment must accompany every percentage. The absence of fifth-digit or other “classic” findings does not exclude the diagnosis. (mannino2018firstdatafrom pages 3-5, mannino2018firstdatafrom pages 6-8)

* **Neurodevelopment:** congenital/early-childhood global developmental delay, variable intellectual disability, expressive-language impairment, and behavioral differences. Suggested terms: **HP:0001263 Global developmental delay**, **HP:0001249 Intellectual disability**, **HP:0000750 Delayed speech and language development**, **HP:0000717 Autism**, and **HP:0007018 Attention-deficit/hyperactivity disorder**. Median milestones in the SMARCA4 subset were rolling 8 months, sitting 12 months, crawling 15 months, walking 26 months, and first words 15.5 months. Speech acquisition in another cohort was broadly reported between approximately 18 months and three years. (li2020thevariabilityof pages 8-9, mannino2018firstdatafrom pages 3-5)
* **Motor/neurologic:** hypotonia (**HP:0001252**) occurred in 2/12 (17%) and seizures (**HP:0001250**) in 1/12 (8%). Corpus-callosum abnormalities (**HP:0001274 Agenesis of corpus callosum**, where anatomically applicable) occurred in 2/12 (17%); no ventricular, cerebellar, or posterior-fossa abnormalities were reported in that small subset. These zero counts do not establish absence from CSS4. (mannino2018firstdatafrom pages 3-5, mannino2018firstdatafrom pages 5-6)
* **Growth/head size:** prenatal growth impairment is generally mild and postnatal impairment mild to moderate; microcephaly (**HP:0000252**) was reported in 5/12 (42%). Suggested terms include **HP:0001510 Growth delay**, **HP:0004322 Short stature**, and **HP:0004325 Decreased body weight**. (mannino2018firstdatafrom pages 3-5, vergano2025coffinsirissyndromec pages 9-11)
* **Feeding/GI:** feeding or sucking difficulty (**HP:0011968 Feeding difficulties**) is prominent; feeding-tube use occurred in 2/12 (17%), constipation (**HP:0002019**) in 5/12 (42%), and abnormal dentition in 7/12 (58%). Feeding dysfunction impairs nutrition and can create aspiration risk and caregiver burden. (mannino2018firstdatafrom pages 3-5, vergano2025coffinsirissyndromec pages 9-11)
* **Digits/nails:** fifth-digit anomalies occurred in 7/12 (58%). Use **HP:0009237 Hypoplasia of the fifth finger**, **HP:0004220 Hypoplasia of the fifth toe**, **HP:0001798 Anonychia**, or **HP:0001800 Hypoplastic toenails** only when the specific feature is documented. Variable frequency and truncating/deletion cases without digital anomalies make this supportive, not obligatory. (mitrakos2020coffinsirissyndrome4related pages 4-4, mannino2018firstdatafrom pages 3-5)
* **Hair/face/palate:** hypertrichosis or hirsutism (**HP:0000998 Hypertrichosis**) occurred in 6/12 (50%), sparse scalp hair (**HP:0002209**) in 4/12 (33%), and high or cleft palate (**HP:0000218 High palate; HP:0000175 Cleft palate**) in 6/12 (50%). Facial coarseness is variable and may be less marked than in other CSS genotypes. (mannino2018firstdatafrom pages 3-5, vergano2025coffinsirissyndromec pages 9-11)
* **Cardiac:** one series estimated congenital heart disease in approximately 50%, ranging from PFO/PDA to tetralogy of Fallot. In the 12-person registry: murmur 17%, PFO/PDA 8%, VSD 8%, valve stenosis 8%, and coarctation 8%. Suggested HPO terms include **HP:0001627 Abnormality of the cardiovascular system**, **HP:0001643 Patent ductus arteriosus**, **HP:0001629 Ventricular septal defect**, and lesion-specific terms. (mannino2018firstdatafrom pages 5-6, li2020thevariabilityof pages 8-9)
* **Airway/sleep:** tracheo-/broncho-/laryngomalacia occurred in 4/12 (33%) and obstructive sleep apnea in 3/12 (25%). Suggested terms: **HP:0002786 Tracheomalacia**, **HP:0001601 Laryngomalacia**, and **HP:0002870 Obstructive sleep apnea**. These can affect feeding, sleep, respiratory safety, and surgical risk. (mannino2018firstdatafrom pages 5-6)
* **Musculoskeletal:** scoliosis (**HP:0002650**) occurred in 5/12 (42%) and kyphosis (**HP:0002808**) in 4/12 (33%). Mobility and self-care may be affected by hypotonia, joint laxity, spinal curvature, or delayed motor development. (mannino2018firstdatafrom pages 3-5, mannino2018firstdatafrom pages 5-6)
* **Hearing/vision:** hearing loss (**HP:0000365**) occurred in 4/12 (33%); myopia and strabismus each in 25%, astigmatism in 17%, and retinal abnormality, nystagmus, ptosis, or cortical visual impairment each in 8%. Suggested terms include **HP:0000407 Sensorineural hearing impairment**, **HP:0000545 Myopia**, **HP:0000486 Strabismus**, and finding-specific retinal terms. (mannino2018firstdatafrom pages 5-6)

No CSS4-specific EQ-5D, SF-36, PROMIS, or validated disease-specific quality-of-life dataset was found. Functional burden follows from communication limitations, feeding and mobility needs, sensory impairment, behavioral challenges, medical appointments, and dependence in activities of daily living.

## 4. Genetic and molecular information

**SMARCA4** is located at 19p13.2 and encodes the nuclear BRG1 ATPase. Typical CSS4 variants are heterozygous germline missense or short in-frame changes, especially in ATPase/helicase functional regions. In Li et al., 15 individuals carried 14 variants; 12 were missense and 11/12 mapped to residues 761–1,243 in or around the helicase ATP-binding and C-terminal domains. (li2020thevariabilityof pages 2-3, li2020thevariabilityof pages 5-7)

Truncating alleles are uncommon but cannot be excluded from the CSS4 spectrum. Reported examples include c.3310C>T, p.Gln1104* and c.4590C>G, p.Tyr1530*, both predicted to undergo nonsense-mediated decay. For c.1452_1453delGGinsA, p.(Asp485Ilefs*16), however, RNA sequencing found 15% mutant-allele reads, demonstrating incomplete NMD. A 428-kb deletion including SMARCA4 was associated with moderate intellectual disability, speech delay, feeding difficulty, sensorineural hearing loss, and psychiatric symptoms but no classic fifth-digit abnormality, supporting a milder haploinsufficiency phenotype. (mitrakos2020coffinsirissyndrome4related pages 4-4, li2020thevariabilityof pages 5-7)

Population allele frequencies for specific variants should be retrieved directly from the current gnomAD release during variant curation; the cohort report states that its missense variants were absent from the population resources examined. Pathogenicity should be assigned per ACMG/AMP criteria using de novo status, population absence, domain constraint, computational evidence, phenotype, and—where available—functional or episignature data. A VUS is not diagnostic. (li2020thevariabilityof pages 2-3, vergano2025coffinsirissyndromec pages 1-4)

No validated CSS4 modifier gene is known. A peripheral-blood BAFopathy DNA-methylation signature overlaps ARID1B-, SMARCB1-, SMARCA4-CSS and SMARCA2-NCBRS, supporting a functional continuum. It can help adjudicate ambiguous variants but is neither fully SMARCA4-specific nor a replacement for sequence diagnosis. (arefeshghi2018bafopathies’dnamethylation pages 6-7, arefeshghi2018bafopathies’dnamethylation pages 14-15)

Large whole-gene deletions can cause a CSS4-like phenotype, but routine karyotype/FISH is not an efficient first-line assay. No recurrent aneuploidy, translocation, repeat expansion, mitochondrial mutation, or founder chromosome rearrangement defines CSS4.

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupational agent, lifestyle factor, or pathogen is known to cause or trigger CSS4. Infectious-agent taxonomy and CHEBI environmental-agent annotations are therefore not applicable. Environmental and educational context can modify functional outcome—through access to therapy, communication aids, nutrition, and medical care—but not the presence of the causal germline variant.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous germline pathogenic **SMARCA4** variant **leads to** altered structure, dosage, ATP engagement, DNA/nucleosome interaction, or catalytic function of BRG1.
2. Altered BRG1 **results in** deficient or mistargeted ATP-dependent BAF/PBAF nucleosome remodeling; dominant interference with assembled complexes is likely for many ATPase-region missense/in-frame alleles, whereas selected truncating/deletion alleles result in haploinsufficiency. (li2020thevariabilityof pages 5-7, valencia2023landscapeofmswisnf pages 7-8, vergano2025coffinsirissyndrome pages 22-25)
3. Defective remodeling **leads to** abnormal chromatin accessibility and transcriptional regulation during development. The genome-wide blood DNA-methylation episignature demonstrates a persistent downstream epigenomic consequence, although blood methylation is a biomarker rather than direct proof of fetal-brain events. (arefeshghi2018bafopathies’dnamethylation pages 6-7, arefeshghi2018bafopathies’dnamethylation pages 14-15)
4. In developing neural and other embryonic progenitors, dysregulated developmental programs are **inferred to result in** altered proliferation, fate specification, differentiation, synapse development, and tissue morphogenesis. This step is supported mainly by general SMARCA4/BAF structural, cellular, and animal evidence rather than patient brain tissue.
5. Neural-development disruption **results in** developmental delay, intellectual disability, speech/behavioral differences, hypotonia, seizures in a minority, and variable structural CNS findings.
6. A developmental branch affecting craniofacial, ectodermal, limb, cardiac, airway, auditory, ocular, and skeletal morphogenesis **results in** the characteristic but variably present multisystem phenotype.

### Mechanistic detail and evidence level

BAF complexes possess DNA-stimulated ATPase activity that destabilizes histone–DNA interactions and repositions nucleosomes. Structural mapping places recurrent neurodevelopmental SMARCA4 variants at the nucleosome interface and ATP-binding pocket. Variants R973W and R1243W diminished PBAF nucleosome-remodeling activity in vitro; effects of nearby CSS/NDD variants are structurally inferred rather than individually demonstrated. (valencia2023landscapeofmswisnf pages 7-8, vergano2025coffinsirissyndrome pages 22-25)

The 2023 structural synthesis found that non-truncating NDD variants predominantly disrupt cBAF and cluster in key structural regions, providing expert support for variant grouping by molecular interface rather than simply by “missense” class. The authors nevertheless caution that static structures cannot by themselves prove effects on ATP engagement. (valencia2023landscapeofmswisnf pages 7-8, valencia2023landscapeofmswisnf pages 13-14)

Suggested ontology annotations are **GO:0006338 chromatin remodeling**, **GO:0006355 regulation of DNA-templated transcription**, **GO:0045893 positive regulation of DNA-templated transcription**, **GO:0007399 nervous system development**, **GO:0030182 neuron differentiation**, **GO:0007417 central nervous system development**, and **GO:0007420 brain development**. Proposed cell annotations, reflecting inference from developmental biology rather than CSS4 patient histology, include **CL:0000047 neuronal stem cell**, **CL:0000031 neuroblast/neural progenitor**, **CL:0000540 neuron**, **CL:0000128 oligodendrocyte**, and cranial neural-crest derivatives. Subcellular annotation: **GO:0005634 nucleus**, **GO:0000785 chromatin**, and **GO:0000786 nucleosome**.

No reproducible CSS4-specific metabolomic, lipidomic, proteomic, immune-inflammatory, oxidative-stress, apoptosis, fibrosis, or necrosis signature was found. These should not be added merely because SMARCA4 participates in those processes in cancer.

## 7. Anatomical structures affected

The primary system is the developing nervous system, particularly brain/cerebral development and neural circuits supporting cognition, language, behavior, motor control, and vision. Suggested sites include **UBERON:0000955 brain**, **UBERON:0001950 neocortex**, **UBERON:0002336 corpus callosum**, and **UBERON:0001017 central nervous system**. Evidence supports variable corpus-callosum involvement but not a single CSS4-specific neuroanatomic lesion. (mannino2018firstdatafrom pages 3-5)

Other affected structures include fifth digits and nails; craniofacial structures, palate and teeth; scalp hair and skin appendages; heart and great vessels; larynx, trachea and bronchi; spine and joints; eye/retina/visual pathways; ear and auditory system; and gastrointestinal/nutritional systems. Suggested annotations include **UBERON:0000948 heart**, **UBERON:0003129 skull**, **UBERON:0001716 secondary palate**, **UBERON:0002102 forelimb**, **UBERON:0002103 hindlimb**, **UBERON:0001474 bone element**, **UBERON:0002384 connective tissue**, **UBERON:0000970 eye**, and **UBERON:0001690 ear**.

At the subcellular level, disease initiation is nuclear/chromatin based. Lateralization is not characteristic; digital, hearing, ocular, and skeletal findings may be bilateral or asymmetric depending on the individual.

## 8. Temporal development

The molecular lesion is present from conception and acts during embryonic/fetal development. Growth restriction and structural malformations may be prenatal or congenital; feeding difficulty, hypotonia, dysmorphism, airway problems, or heart disease may be evident neonatally. Developmental and language differences become clearer during infancy and early childhood. (mannino2018firstdatafrom pages 3-5, vergano2025coffinsirissyndromec pages 9-11)

CSS4 is chronic and lifelong, not episodic or relapsing-remitting. Congenital malformations are structurally stable unless treated, while their consequences and behavioral phenotype evolve with age. Scoliosis, contractures, sleep disturbance, obesity, or adaptive limitations may emerge later. There are no validated disease stages, remission criteria, or end-stage designation. Early childhood is the principal intervention window for feeding safety, communication, sensory access, and developmental therapy, although benefit from rehabilitation and accommodations can continue across life.

## 9. Inheritance and population

Inheritance is autosomal dominant and predominantly de novo. Penetrance among molecularly defined canonical pathogenic variants appears high for some neurodevelopmental phenotype, but numerical penetrance has not been established. Expressivity is broad, ranging from mild learning/behavioral differences without organ disease to substantial multisystem congenital abnormalities. (li2020thevariabilityof pages 2-3, vergano2025coffinsirissyndrome pages 17-19)

An affected person has a theoretical 50% chance of transmitting the variant at each conception. When parental blood testing is negative, recurrence risk is low but not zero because gonadal mosaicism cannot be excluded. Rare inherited cases and mosaic variants warrant individualized counseling. No anticipation, founder effect, consanguinity association, carrier frequency, geographic enrichment, ancestry predisposition, or established sex-ratio distortion is known.

Population prevalence and annual incidence have not been reliably measured. Published cohorts represent tens of molecularly confirmed SMARCA4-CSS4 cases rather than population surveillance, precluding cases-per-100,000 estimates.

## 10. Diagnostics

### Molecular diagnosis

Diagnosis requires a compatible phenotype and a heterozygous pathogenic or likely pathogenic variant in SMARCA4. A VUS neither confirms nor excludes CSS4. Because the phenotype overlaps many neurodevelopmental disorders, trio exome/genome sequencing or a broad neurodevelopmental/BAFopathy panel is generally more efficient than phenotype-driven SMARCA4-only sequencing. Parental testing establishes de novo status and assesses mosaicism. Exome/genome analysis should include copy-number calling; chromosomal microarray remains useful for deletions such as the reported 428-kb SMARCA4-containing deletion. (mitrakos2020coffinsirissyndrome4related pages 4-4, vergano2025coffinsirissyndromec pages 1-4, vergano2025coffinsirissyndromea pages 1-4)

WGS can identify coding and noncoding sequence variants, structural variants, and copy-number changes missed by some panels or exomes. RNA analysis can assess splice effects or NMD, as illustrated by residual mutant transcript reads. Peripheral-blood methylation episignature testing may supply functional evidence for a disputed variant, but its overlap with other BAFopathies prevents gene-specific interpretation in isolation. (li2020thevariabilityof pages 5-7, arefeshghi2018bafopathies’dnamethylation pages 6-7, arefeshghi2018bafopathies’dnamethylation pages 14-15)

Karyotype, FISH, mitochondrial sequencing, repeat-expansion testing, metabolomics, proteomics, liquid biopsy, and tissue biopsy are not routine CSS4 tests unless another diagnosis is suspected. No biochemical enzyme assay or circulating protein biomarker is diagnostic.

### Clinical evaluation

After molecular diagnosis, baseline assessment should include growth and nutrition; feeding/aspiration evaluation; neurologic and developmental assessment; hearing and ophthalmology examinations; echocardiography; renal/genitourinary assessment; musculoskeletal examination; dental review; respiratory/sleep review; and evaluation for recurrent infections. Brain MRI, EEG, swallow study, and sleep study are indication-driven rather than mandatory in every patient. (vergano2025coffinsirissyndromeb pages 13-15, vergano2025coffinsirissyndromec pages 13-15)

Important differentials include other molecular CSS subtypes, **SMARCA2**-NCBRS, Cornelia de Lange syndrome, DOORS syndrome, 4q deletion syndrome, BOD syndrome, fetal alcohol spectrum disorder, and fetal hydantoin embryopathy. The causal gene and variant—not fifth-digit morphology alone—resolve many cases. (vergano2025coffinsirissyndromea pages 13-15)

There is no population newborn screening, biochemical carrier screening, or routine cascade screening program. Testing relatives is appropriate when inheritance or mosaicism is possible. Prenatal diagnosis and preimplantation genetic testing are possible after identification of the familial variant. (vergano2025coffinsirissyndromec pages 1-4)

## 11. Outcome and prognosis

No reliable CSS4-specific survival curve, five- or ten-year survival statistic, mortality rate, or life-expectancy estimate is available. Published cohorts are too small and young for valid inference. CSS4 is not inherently described as a relentlessly progressive or fatal disorder; prognosis is instead driven by the severity of developmental disability and organ complications such as congenital heart disease, airway obstruction, aspiration, epilepsy, sensory impairment, and orthopedic disease.

Developmental gains occur, but most affected individuals have persistent language, learning, behavioral, or adaptive needs. Recovery to an unaffected state is not expected because the causal developmental chromatin disorder is lifelong. Prognostic biomarkers and validated genotype-based outcome calculators do not exist. ATPase-domain clustering is useful for pathogenicity assessment but does not yet provide reliable individual prognostication. Small subgroup sizes and age-dependent ascertainment make apparent genotype–phenotype correlations provisional. (li2020thevariabilityof pages 8-9, mannino2018firstdatafrom pages 6-8)

## 12. Treatment and real-world implementation

There is no cure and no approved SMARCA4-directed pharmacotherapy, gene therapy, RNA therapy, cell therapy, or epigenome-editing treatment. Current care is multidisciplinary and supportive. (vergano2025coffinsirissyndrome pages 15-17)

* **Development:** early intervention, special education, PT, OT, speech-language therapy, feeding therapy, and infant mental-health/developmental services. Suggested NCIT concepts: **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Rehabilitation Therapy**, and **Supportive Care**.
* **Communication:** augmentative and alternative communication evaluation; AAC supports rather than prevents speech development. (vergano2025coffinsirissyndrome pages 17-19)
* **Feeding/nutrition:** clinical feeding assessment, swallow study when dysphagia or aspiration is suspected, texture modification, feeding therapy, and nasogastric or gastrostomy feeding for severe dysfunction. Suggested NCIT terms: **Nutritional Support**, **Enteral Nutrition**, and **Gastrostomy**. (vergano2025coffinsirissyndrome pages 15-17, vergano2025coffinsirissyndrome pages 17-19)
* **Neurology/behavior:** standard antiseizure medication selected by an experienced neurologist; no agent is CSS4-specific. Standard evidence-based management of ADHD, anxiety, aggression, sleep disturbance, autism-related needs, or tics is individualized. (vergano2025coffinsirissyndrome pages 15-17, vergano2025coffinsirissyndrome pages 17-19)
* **Organ-directed treatment:** cardiology/surgery for congenital heart disease; ENT/audiology and hearing aids for hearing loss; ophthalmologic correction of refractive error or strabismus; orthopedic/rehabilitation management of scoliosis, joint laxity, or mobility limitations; sleep-medicine treatment of apnea; dental care; and immunology referral for unusual recurrent infections. (vergano2025coffinsirissyndrome pages 15-17)

Surveillance at each visit should address growth, nutritional and oral-feeding safety, neurologic symptoms, development and education, behavior, sleep, mobility, infections, and family support. Ophthalmology and audiology are recommended annually or as clinically indicated; dental review is advised at least every six months once teeth are present. (vergano2025coffinsirissyndrome pages 17-19)

No CSS4-specific treatment response rates, adverse-event series, pharmacogenomic recommendation, CPIC guidance, or combination-treatment algorithm exists. The retrieved ClinicalTrials.gov search found no relevant SMARCA4-CSS4 interventional study. A clonazepam study discussed in GeneReviews concerned ARID1B-related CSS and did not establish benefit; it should not be extrapolated to CSS4. (vergano2025coffinsirissyndrome pages 17-19)

### Tumor surveillance caveat

Routine RTPS2 surveillance should not automatically be applied to every person with a canonical non-truncating CSS4 allele. However, rare truncating/deletion alleles and developmental–cancer overlap justify consultation with cancer genetics. Published authors have recommended surveillance for loss-of-function carriers, and one deletion case was advised pelvic ultrasonography every six months, but CSS4-specific cancer penetrance and the benefit of such surveillance remain unquantified. Decisions should be allele- and family-history-specific. (mitrakos2020coffinsirissyndrome4related pages 4-4, li2020thevariabilityof pages 5-7)

## 13. Prevention

There is no environmental primary prevention because most cases arise from a spontaneous de novo variant. Vaccination, diet, or exposure avoidance does not prevent CSS4.

* **Primary/reproductive prevention:** nondirective genetic counseling; parental testing; prenatal diagnosis or preimplantation genetic testing when the causal variant is known.
* **Secondary prevention:** prompt genomic testing in children with unexplained developmental delay plus dysmorphism, feeding problems, fifth-digit/nail changes, or multisystem congenital anomalies; early hearing, vision, cardiac, feeding, and developmental assessment.
* **Tertiary prevention:** aspiration precautions, nutrition support, seizure safety, treatment of sleep apnea, hearing/vision correction, PT/OT to reduce contractures and mobility complications, scoliosis monitoring, AAC, educational accommodations, and coordinated psychosocial support. (vergano2025coffinsirissyndrome pages 15-17, vergano2025coffinsirissyndrome pages 17-19, vergano2025coffinsirissyndromec pages 1-4)

No public-health sanitation measure, antimicrobial prophylaxis, chemoprevention regimen, or population screening program applies.

## 14. Other species and natural disease

No well-established naturally occurring veterinary CSS4 homolog caused by a spontaneous heterozygous non-truncating SMARCA4 variant was found. Accordingly, breed-specific VBO terms, veterinary prevalence, zoonotic transmission, and cross-species transmission are not applicable. The condition is genetic and noncommunicable.

Relevant orthologs include mouse **Smarca4** (*Mus musculus*, NCBI Taxonomy 10090), zebrafish *smarca4* orthologs (*Danio rerio*, Taxonomy 7955), and Drosophila *brm* (*Drosophila melanogaster*, Taxonomy 7227). Exact current NCBI Gene IDs should be retrieved from NCBI rather than inferred here. Strong conservation of the ATPase machinery supports comparative mechanistic studies, but ortholog disruption often represents complete or tissue-specific loss, not the dominant missense mechanism typical of human CSS4.

## 15. Model organisms and experimental systems

Available models are predominantly induced genetic systems rather than natural disease models:

* **Mouse conditional Smarca4/Brg1 loss:** tissue- or stage-specific deletion demonstrates essential roles in neural stem/progenitor maintenance, cortical development, brain and eye development, oligodendrocyte differentiation, synapse development, and ventricular/brain morphogenesis. These models support the affected developmental processes but may be embryonic lethal or more severe than heterozygous human CSS4.
* **Neuronal/cell models:** BRG1 perturbation alters nucleosome remodeling and chromatin accessibility; selected recurrent variants diminish remodeling in vitro. These are useful for variant-function assays and testing dominant interference. (valencia2023landscapeofmswisnf pages 7-8)
* **BAFopathy methylation models:** patient blood and machine-learning classifiers provide a human functional biomarker. The reported pipeline selected probes with at least 5% methylation difference and AUC >0.85 and used a radial-basis-function SVM with tenfold cross-validation, but retrieved evidence did not supply SMARCA4-only sensitivity or specificity. (arefeshghi2018bafopathies’dnamethylation pages 14-15)
* **Structural/computational models:** cryo-EM-based mapping places NDD variants at ATP, nucleosome, Arp-module, and core-module interfaces. These models prioritize functional testing but cannot prove pathogenic mechanism alone. (valencia2023landscapeofmswisnf pages 7-8, valencia2023landscapeofmswisnf pages 13-14)

A major unmet need is a heterozygous knock-in model carrying a recurrent human CSS4 missense/in-frame allele, evaluated longitudinally for cognition, speech-relevant communication, behavior, heart/airway development, digits, hearing, and vision. Patient-derived iPSCs, neural progenitors, cortical organoids, CRISPR isogenic controls, single-cell multi-omics, and chromatin-accessibility profiling would better model allele-specific dominant effects. No mature CSS4-specific organoid, spatial-transcriptomic, metabolomic, lipidomic, or therapeutic-screening platform was identified in the retrieved evidence.

## Key source quotations and recent developments

* Li et al. (published July 2020) summarized the disease biology as: **“SMARCA4 encodes a central ATPase subunit in the BRG1-/BRM-associated factors (BAF) or polybromo-associated BAF (PBAF) complex in humans, which is responsible in part for chromatin remodeling and transcriptional regulation.”** The same abstract reports **“a cohort of 15 unrelated individuals”** and emphasizes variability in learning impairment and health issues. DOI: https://doi.org/10.1002/ajmg.a.61732. (li2020thevariabilityof pages 2-3)
* Aref-Eshghi et al. (published November 2018) reported overlapping peripheral-blood episignatures and showed that a machine-learning model could resolve ambiguous cases and reclassify variants of uncertain significance. DOI: https://doi.org/10.1038/s41467-018-07193-y. (arefeshghi2018bafopathies’dnamethylation pages 6-7, arefeshghi2018bafopathies’dnamethylation pages 14-15)
* Valencia et al. (published August 2023) integrated NDD variant and structural data; their direct functional summary notes that SMARCA4 brace-helix variants R973W and R1243W **“diminish[ed] nucleosome remodeling activity of PBAF complexes in vitro.”** DOI: https://doi.org/10.1038/s41588-023-01451-6. (valencia2023landscapeofmswisnf pages 7-8)
* The comprehensive GeneReviews update posted **15 May 2025** states: **“There is no cure for CSS. Supportive care to improve quality of life, maximize function, and reduce complications is recommended.”** It remains the most current authoritative management synthesis, although most recommendations are CSS-wide rather than tested specifically in SMARCA4 cohorts. (vergano2025coffinsirissyndrome pages 15-17, vergano2025coffinsirissyndrome pages 22-25)

PMIDs were not present in the retrieved full-text metadata for several central sources; DOI URLs are therefore supplied rather than risking incorrect PMID assignment.

References

1. (li2020thevariabilityof pages 2-3): Dong Li, Rebecca C. Ahrens‐Nicklas, Janice Baker, Vikas Bhambhani, Amy Calhoun, Julie S. Cohen, Matthew A. Deardorff, Alberto Fernández‐Jaén, Benjamin Kamien, Mahim Jain, Fiona Mckenzie, Mark Mintz, Constance Motter, Kirsten Niles, Alyssa Ritter, Curtis Rogers, Maian Roifman, Sharron Townshend, Catherine Ward‐Melver, and Samantha A. Schrier Vergano. The variability of smarca4‐related coffin–siris syndrome: do nonsense candidate variants add to milder phenotypes? American Journal of Medical Genetics Part A, 182:2058-2067, Jul 2020. URL: https://doi.org/10.1002/ajmg.a.61732, doi:10.1002/ajmg.a.61732. This article has 34 citations.

2. (mannino2018firstdatafrom pages 3-5): Elizabeth A. Mannino, Hanae Miyawaki, Gijs Santen, and Samantha A. Schrier Vergano. First data from a parent‐reported registry of 81 individuals with coffin–siris syndrome: natural history and management recommendations. American Journal of Medical Genetics Part A, 176:2250-2258, Oct 2018. URL: https://doi.org/10.1002/ajmg.a.40471, doi:10.1002/ajmg.a.40471. This article has 51 citations.

3. (mannino2018firstdatafrom pages 5-6): Elizabeth A. Mannino, Hanae Miyawaki, Gijs Santen, and Samantha A. Schrier Vergano. First data from a parent‐reported registry of 81 individuals with coffin–siris syndrome: natural history and management recommendations. American Journal of Medical Genetics Part A, 176:2250-2258, Oct 2018. URL: https://doi.org/10.1002/ajmg.a.40471, doi:10.1002/ajmg.a.40471. This article has 51 citations.

4. (vergano2025coffinsirissyndrome pages 15-17): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

5. (vergano2025coffinsirissyndrome pages 17-19): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

6. (vergano2025coffinsirissyndromec pages 1-4): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

7. (li2020thevariabilityof pages 5-7): Dong Li, Rebecca C. Ahrens‐Nicklas, Janice Baker, Vikas Bhambhani, Amy Calhoun, Julie S. Cohen, Matthew A. Deardorff, Alberto Fernández‐Jaén, Benjamin Kamien, Mahim Jain, Fiona Mckenzie, Mark Mintz, Constance Motter, Kirsten Niles, Alyssa Ritter, Curtis Rogers, Maian Roifman, Sharron Townshend, Catherine Ward‐Melver, and Samantha A. Schrier Vergano. The variability of smarca4‐related coffin–siris syndrome: do nonsense candidate variants add to milder phenotypes? American Journal of Medical Genetics Part A, 182:2058-2067, Jul 2020. URL: https://doi.org/10.1002/ajmg.a.61732, doi:10.1002/ajmg.a.61732. This article has 34 citations.

8. (li2020thevariabilityof pages 8-9): Dong Li, Rebecca C. Ahrens‐Nicklas, Janice Baker, Vikas Bhambhani, Amy Calhoun, Julie S. Cohen, Matthew A. Deardorff, Alberto Fernández‐Jaén, Benjamin Kamien, Mahim Jain, Fiona Mckenzie, Mark Mintz, Constance Motter, Kirsten Niles, Alyssa Ritter, Curtis Rogers, Maian Roifman, Sharron Townshend, Catherine Ward‐Melver, and Samantha A. Schrier Vergano. The variability of smarca4‐related coffin–siris syndrome: do nonsense candidate variants add to milder phenotypes? American Journal of Medical Genetics Part A, 182:2058-2067, Jul 2020. URL: https://doi.org/10.1002/ajmg.a.61732, doi:10.1002/ajmg.a.61732. This article has 34 citations.

9. (arefeshghi2018bafopathies’dnamethylation pages 6-7): Erfan Aref-Eshghi, Eric G. Bend, Rebecca L. Hood, Laila C. Schenkel, Deanna Alexis Carere, Rana Chakrabarti, Sandesh C. S. Nagamani, Sau Wai Cheung, Philippe M. Campeau, Chitra Prasad, Victoria Mok Siu, Lauren Brady, Mark A. Tarnopolsky, David J. Callen, A. Micheil Innes, Susan M. White, Wendy S. Meschino, Andrew Y. Shuen, Guillaume Paré, Dennis E. Bulman, Peter J. Ainsworth, Hanxin Lin, David I. Rodenhiser, Raoul C. Hennekam, Kym M. Boycott, Charles E. Schwartz, and Bekim Sadikovic. Bafopathies’ dna methylation epi-signatures demonstrate diagnostic utility and functional continuum of coffin–siris and nicolaides–baraitser syndromes. Nature Communications, Nov 2018. URL: https://doi.org/10.1038/s41467-018-07193-y, doi:10.1038/s41467-018-07193-y. This article has 169 citations and is from a highest quality peer-reviewed journal.

10. (arefeshghi2018bafopathies’dnamethylation pages 14-15): Erfan Aref-Eshghi, Eric G. Bend, Rebecca L. Hood, Laila C. Schenkel, Deanna Alexis Carere, Rana Chakrabarti, Sandesh C. S. Nagamani, Sau Wai Cheung, Philippe M. Campeau, Chitra Prasad, Victoria Mok Siu, Lauren Brady, Mark A. Tarnopolsky, David J. Callen, A. Micheil Innes, Susan M. White, Wendy S. Meschino, Andrew Y. Shuen, Guillaume Paré, Dennis E. Bulman, Peter J. Ainsworth, Hanxin Lin, David I. Rodenhiser, Raoul C. Hennekam, Kym M. Boycott, Charles E. Schwartz, and Bekim Sadikovic. Bafopathies’ dna methylation epi-signatures demonstrate diagnostic utility and functional continuum of coffin–siris and nicolaides–baraitser syndromes. Nature Communications, Nov 2018. URL: https://doi.org/10.1038/s41467-018-07193-y, doi:10.1038/s41467-018-07193-y. This article has 169 citations and is from a highest quality peer-reviewed journal.

11. (mitrakos2020coffinsirissyndrome4related pages 4-4): Anastasios Mitrakos, Leandros Lazaros, Amelia Pantou, Ariadni Mavrou, Emmanuel Kanavakis, and Maria Tzetis. Coffin-siris syndrome 4-related spectrum in a young woman caused by a heterozygous smarca4 deletion detected by high-resolution acgh. Molecular Syndromology, 11:141-145, Jun 2020. URL: https://doi.org/10.1159/000508563, doi:10.1159/000508563. This article has 11 citations and is from a peer-reviewed journal.

12. (vergano2025coffinsirissyndrome pages 22-25): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

13. (mannino2018firstdatafrom pages 6-8): Elizabeth A. Mannino, Hanae Miyawaki, Gijs Santen, and Samantha A. Schrier Vergano. First data from a parent‐reported registry of 81 individuals with coffin–siris syndrome: natural history and management recommendations. American Journal of Medical Genetics Part A, 176:2250-2258, Oct 2018. URL: https://doi.org/10.1002/ajmg.a.40471, doi:10.1002/ajmg.a.40471. This article has 51 citations.

14. (vergano2025coffinsirissyndromec pages 9-11): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

15. (valencia2023landscapeofmswisnf pages 7-8): Alfredo M. Valencia, Akshay Sankar, Pleuntje J. van der Sluijs, F. Kyle Satterstrom, Jack Fu, Michael E. Talkowski, Samantha A. Schrier Vergano, Gijs W. E. Santen, and Cigall Kadoch. Landscape of mswi/snf chromatin remodeling complex perturbations in neurodevelopmental disorders. Nature Genetics, 55:1400-1412, Jul 2023. URL: https://doi.org/10.1038/s41588-023-01451-6, doi:10.1038/s41588-023-01451-6. This article has 84 citations and is from a highest quality peer-reviewed journal.

16. (valencia2023landscapeofmswisnf pages 13-14): Alfredo M. Valencia, Akshay Sankar, Pleuntje J. van der Sluijs, F. Kyle Satterstrom, Jack Fu, Michael E. Talkowski, Samantha A. Schrier Vergano, Gijs W. E. Santen, and Cigall Kadoch. Landscape of mswi/snf chromatin remodeling complex perturbations in neurodevelopmental disorders. Nature Genetics, 55:1400-1412, Jul 2023. URL: https://doi.org/10.1038/s41588-023-01451-6, doi:10.1038/s41588-023-01451-6. This article has 84 citations and is from a highest quality peer-reviewed journal.

17. (vergano2025coffinsirissyndromea pages 1-4): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

18. (vergano2025coffinsirissyndromeb pages 13-15): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

19. (vergano2025coffinsirissyndromec pages 13-15): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

20. (vergano2025coffinsirissyndromea pages 13-15): SS Vergano, G Santen, and D Wieczorek. Coffin-siris syndrome. Unknown journal, 2025.

## Artifacts

- [Edison artifact artifact-00](Intellectual_Disability_Autosomal_Dominant_16-deep-research-falcon_artifacts/artifact-00.md)

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
| Terms checked | 61 |
| Resolved | 61 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.
