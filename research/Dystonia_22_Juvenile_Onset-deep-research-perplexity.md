---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-11T20:05:42.094102'
end_time: '2026-10-11T20:09:11.006803'
duration_seconds: 208.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dystonia 22, Juvenile-Onset
  mondo_id: MONDO:0957539
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
citation_count: 51
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 28
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 9
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  - Gene
  - UniProt
  - Taxon
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dystonia 22, Juvenile-Onset
- **MONDO ID:** MONDO:0957539 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dystonia 22, Juvenile-Onset** covering all of the
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

# Dystonia 22, juvenile-onset: disease-characteristics research report

**Dystonia 22, juvenile-onset (DYT22JO) is an ultra-rare, autosomal-recessive disorder caused by biallelic loss-of-function variants in *TSPOAP1*.** It typically presents in the early teenage years with progressive, predominantly craniocervical dystonia that becomes generalized, cognitive deterioration, and cerebellar—especially vermian—atrophy. The most detailed clinical and experimental evidence remains the original study of **four affected people in two families**; later reports have added patients but have not established population rates or a standardized treatment response. *TSPOAP1* missense-associated **adult-onset focal dystonia** is a distinct DYT22 phenotype and should not be pooled with DYT22JO. [46][1][77]

**Evidence notation:** “Human” means observation in affected people; “mouse” and “in vitro” identify experimental evidence. Fractions below describe *reported individuals*, **not** population prevalence or reliable penetrance estimates.

## 1. Disease information and identifiers

| Identifier or name | Disease-specific information |
|---|---|
| Preferred name and synonyms | Dystonia 22, juvenile-onset; juvenile-onset dystonia-22; DYT22JO; juvenile-onset *TSPOAP1*-related dystonia. The broader label DYT-TSPOAP1/DYT-22 may also encompass the distinct adult-onset phenotype. [1][77] |
| OMIM phenotype | **620453**; causal-gene OMIM entry **610764** (*TSPOAP1*). Adult-onset dystonia-22 is separately **OMIM:620456**. [1] |
| Disease Ontology | **DOID:0060966**. [1] |
| MONDO | **MONDO:0957539 was supplied in the request but could not be independently verified against the retrieved disease records**; retain it as a provisional mapping pending ontology validation, rather than treating it as confirmed. [1][185] |
| Orphanet | A disease-specific ORPHA number was **not verified**. Do not substitute an ORPHA number for another juvenile dystonia. |
| ICD | **ICD-10 G24** describes dystonia; **G24.9** is an *unspecified-dystonia* code, **not a DYT22JO-specific code**. A disease-specific ICD-11 code was not verified. [152][154] |
| MeSH | **Dystonic Disorders: D020821**; **Dystonia: D004421**. “Juvenile-onset dystonia,” **C537704**, is a broader supplementary concept, not a unique identifier for *TSPOAP1* disease. [151][158][153] |
| Evidence provenance | This entry synthesizes published, **aggregated disease-level** descriptions derived primarily from individually examined research participants, pedigrees, imaging, and laboratory experiments. It is **not** an EHR-derived cohort or a patient-level clinical record. [46][1] |

**Primary abstract, exact quotation:** “Subjects carrying loss-of-function variants presented with juvenile-onset progressive generalized dystonia, associated with intellectual disability and cerebellar atrophy.” — Mencacci *et al.*, *Journal of Clinical Investigation*, **1 April 2021**, PMID **33539324**, DOI **10.1172/JCI140625**; [article URL](https://pmc.ncbi.nlm.nih.gov/articles/PMC8011894/). [46]

## 2. Etiology: causal, risk, protective, and environmental factors

The established cause is **homozygous truncating *TSPOAP1* variation**, predicted to remove functional RIM-binding protein 1 (**RIMBP1**) through early truncation or nonsense-mediated decay. The original families were of Gujarati Indian and Estonian origin. First-cousin parentage in the Gujarati family increased the opportunity for homozygosity; consanguinity is **not required**, as it was not reported for the Estonian family. These are *germline inherited* findings, not somatic mutations. [46][1]

| Factor | DYT22JO-specific conclusion |
|---|---|
| Causal genetic risk | Biallelic loss-of-function *TSPOAP1* variants; see Section 4. [46] |
| Family history and consanguinity | An affected sibling or known carrier parents raise individual risk under autosomal-recessive inheritance. Consanguinity occurred in one original family; its population-attributable contribution is unknown. [46] |
| Age and sex | Age in the early teenage years describes **observed onset**, not a demonstrated exposure-related risk. No sex-specific risk estimate is available. [46] |
| Toxins, occupation, diet, smoking, alcohol, infection, radiation | **No DYT22JO-specific causal association established** in the cited clinical series. |
| Protective alleles, modifier genes, diet, lifestyle | **None established.** Absence of disease in a carrier is consistent with recessive inheritance, not evidence of a protective allele. [46] |
| Gene–environment interaction | **Not demonstrated in humans.** Oxotremorine provoked more dystonia-like events in *Tspoap1*-knockout mice; this is an **experimental pharmacological challenge**, not evidence that environmental oxotremorine exposure causes human DYT22JO. [46] |

## 3. Phenotypes and effects on functioning

The following frequencies are **original-series observations, at most four people**, and should be stored with that denominator and source rather than as generalizable disease frequencies. Onset of dystonia was in the early teenage years; school-age learning difficulties could precede it. “All four” applies only where explicitly reported. [46][1]

| Phenotype and type | Onset, course, severity, frequency in original series | Functional or quality-of-life implication | Suggested HPO term |
|---|---|---|---|
| Generalized dystonia; clinical sign | Early teenage onset; progressive, severe, craniocervical-predominant; **4/4**. [46] | Increasing difficulty with movement and independence; no DYT22JO-specific EQ-5D or SF-36 score reported. | **HP:0007325** generalized dystonia; **HP:0001332** dystonia. [166][107] |
| Craniocervical dystonia and abnormal voice; sign/symptom | Prominent cranial involvement, including dysphonia; described across the four loss-of-function cases, without a separately published per-feature percentage. [46] | Impaired spoken communication. | **HP:0001618** dysphonia; **HP:0001332** dystonia. [106] |
| Dysarthria; sign | Prominent and progressive; separate numerical frequency unavailable. [46] | Reduced speech intelligibility. | **HP:0001260** dysarthria. [109] |
| Dysphagia; symptom/sign | Progressive swallowing difficulty; separate numerical frequency unavailable. [46] | Eating and swallowing become harder; aspiration risk warrants clinical assessment, but a DYT22JO-specific aspiration rate has **not** been measured. | **HP:0002015** dysphagia. [46][113] |
| Upper-limb dystonic posturing, overflow, writhing; signs | Ongoing and progressive; separate numerical frequency unavailable. [46] | Impaired dexterity and severe handwriting difficulty. | **HP:0001332** dystonia; **HP:0007010** poor fine motor coordination is a *functional descriptor*, not proof of primary coordination disease. [168] |
| Abnormal gait and lower-limb dystonic posturing; signs | Progressive inward foot turning, tiptoeing and leg stiffening; reported in the original juvenile group. [46] | Progressive loss of independent walking was described. | **HP:0001332** dystonia; document observed gait pattern individually rather than automatically coding gait ataxia. |
| School-age learning difficulty, then cognitive deterioration; behavioral/cognitive findings | Early motor and language development initially normal; mild primary-school learning difficulty followed by deterioration in **4/4**. Formal assessments documented worsening in two individuals. [46] | Educational and later daily-living support needs; no disease-specific patient-reported outcome score. | **HP:0001249** intellectual disability when clinically established; **HP:0001256** mild intellectual disability where assessed. [175][167] |
| Cerebellar, predominantly vermian, atrophy; imaging sign | **4/4** on MRI; progressive on serial imaging in reported individuals. Classic nystagmus, limb dysmetria and gait ataxia were **not prominent** in the original group. [46] | An important diagnostic clue; an independent contribution to disability is unproven. | **HP:0001272** cerebellar atrophy; **HP:0006855** cerebellar vermis atrophy. [106][169] |
| Generalized tonic–clonic seizures and interictal EEG activity; signs/test finding | **1/4** for seizures in the original series. [46] | Potential episodic safety and treatment burden. | **HP:0001250** seizure; describe EEG finding separately. [175] |
| Movement-triggered painful episodic limb/truncal dystonia; symptom/sign | Reported in **one** original individual, superimposed on progressive dystonia. [46] | Episodic pain and interruption of activity. | **HP:0001332** dystonia; document the trigger and episodic pattern in free text. |
| Lower-limb spasticity and brisk reflexes; signs | Reported in **one** original individual. [46] | May further impair walking. | Use clinically verified spasticity/brisk-reflex HPO terms in that patient; do not assign to all DYT22JO cases. |

**Later phenotype evidence:** A **2025 report of two unrelated patients** described adolescent-onset generalized dystonia with craniocaudal progression and noted eye-movement abnormalities within the broader reported spectrum. A **2026 case report** identifies childhood-onset generalized dystonia with cerebellar atrophy; its PubMed record has **no abstract**, so an exact variant or further phenotype cannot responsibly be extracted from that record. Holla *et al.*, *Parkinsonism & Related Disorders*, online **2 December 2025**, PMID **41371074**, DOI **10.1016/j.parkreldis.2025.108139**, [URL](https://pubmed.ncbi.nlm.nih.gov/41371074/); Dutta *et al.*, *Movement Disorders Clinical Practice*, **24 April 2026**, PMID **42027086**, DOI **10.1002/mdc3.70622**, [URL](https://pubmed.ncbi.nlm.nih.gov/42027086/). [77][78]

## 4. Genetic and molecular information

***TSPOAP1***, formerly **BZRAP1**, is at **17q22**: **HGNC:16831; NCBI Gene:9256; Ensembl:ENSG00000005379; UniProt:O95153; OMIM:610764**. It encodes the presynaptic active-zone scaffolding protein **RIMBP1**. Transcript versions must be preserved when recording variants: the original study used **NM_004758.3**, while a later ClinVar representation of the second variant uses **NM_004758.4** and the equivalent inversion description. [72][65][46][131]

| Variant and original transcript | Class, original evidence, and population observation | Interpretation for this entry |
|---|---|---|
| **NM_004758.3:c.538delG; p.(Ala180Profs*8)** | Homozygous frameshift in **three affected siblings**; each parent heterozygous; unaffected sibling reference homozygous. Absent among **>120,000** gnomAD individuals examined in the original analysis, including **>15,000** South Asian individuals. **Human segregation and computationally predicted loss of function**; no patient-cell functional test reported. [46] | Original authors identified it as pathogenic/causal for **DYT22JO**. An observed database absence is not a measured carrier frequency. [46] |
| **NM_004758.3:c.2449_2450delinsTG; p.(Gln817Ter)** | Homozygous stop-gain in **one affected Estonian individual**; mother heterozygous; father unavailable. Absent from the gnomAD data examined, which included **2,418 Estonian individuals**. Also recorded as **NM_004758.4:c.2449_2450inv** in ClinVar. [46][131] | ClinVar records a **germline pathogenic** submission for juvenile-onset dystonia-22; ClinVar notes **no variant-specific functional evidence**. [131] |
| **NM_004758.3:c.5422G>A; p.(Gly1808Ser)** | Homozygous missense in three relatives with **adult-onset focal dystonia**, not the juvenile loss-of-function syndrome. In neuronal rescue assays it increased calcium transients and evoked transmission. [46] | **Exclude from DYT22JO-specific pathogenic-variant counts.** It illustrates a different variant class and phenotype, OMIM:620456. [1][46] |
| **Additional truncating variants reported in 2025; novel homozygous variant reported in 2026** | The retrieved 2025 abstract does not give HGVS nomenclature; the retrieved 2026 record has no abstract. [77][78] | Record the case reports as supporting evidence, but **do not invent variant strings, allele frequencies, or ACMG classifications**. |

The original study found no additional confirmed biallelic cases among approximately **700** other dystonia exomes it screened. No DYT22JO-specific **modifier gene, protective variant, repeat expansion, pathogenic structural chromosome rearrangement, or epigenetic signature** was established. The Estonian case’s chromosomal microarray found no explanatory copy-number variant. [46]

## 5. Environmental information

No infectious agent, toxin, radiation exposure, occupation, smoking pattern, diet, or exercise pattern has been established as a cause or preventive factor for this **Mendelian** syndrome. In particular, the mouse **oxotremorine** result concerns experimentally induced sensitivity after gene knockout, not a documented human exposure pathway. **CHEBI annotation:** enter chemical identifiers only after verifying a specific compound and its context; do not enter oxotremorine as a human disease cause. [46]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic truncating *TSPOAP1* variants lead to** predicted loss of functional presynaptic **RIMBP1**. **Human genetic evidence** supports the initiating lesion; the exact effect of each patient allele on patient-neuron protein abundance was **not directly measured**. [46]
2. **RIMBP1 deficiency leads to** impaired presynaptic active-zone organization and less effectively coupled calcium-channel activity and vesicle release. This step draws on established RIMBP1 biology and knockout experiments; its precise magnitude **in affected human neurons is inferred**. [46]
3. **Altered synaptic transmission leads to**, or accompanies, **reduced excitatory synaptic markers and shortened Purkinje-cell dendritic arbors** in older knockout mice. Whether one abnormality causes the other has **not been demonstrated**. [46]
4. **Abnormal cerebellar development or maintenance is consistent with** progressive human cerebellar atrophy. A direct mouse-to-human structural causal link, and the extent to which cerebellar changes themselves **cause** dystonia, remain **inferred rather than established**. [46]
5. **Disrupted motor-network signaling plausibly leads to** progressive dystonia and impaired movement, speech, swallowing, and gait; **a possible parallel branch** through other RIMBP1-expressing motor circuits may contribute. Circuit-specific necessity in patients has **not been demonstrated**. [46]

**Experimental detail.** At about six months, knockout mice showed approximately **30% less distal Purkinje dendritic calbindin-covered area**, roughly **20% less vGluT1 signal**, and approximately **15–30% fewer vGluT2-labelled clusters**, depending on dendritic region. These changes were not evident at two months. Purkinje-cell **number** and gross cerebellar **volume** were not significantly reduced in that mouse analysis; therefore, do not equate the mouse histology with proven Purkinje-cell death in patients. After muscarinic challenge, knockout mice had approximately **300% greater motor-dysfunction scores** than controls. These are **mouse experimental measurements**, not human disease biomarkers. [46]

**Mechanistic boundary:** the original paper explicitly cautions that it **does not establish a causal link** between cerebellar structural changes and dystonia. The adult-onset p.Gly1808Ser **in-vitro** findings—larger spike-evoked calcium transients and enhanced release—must not be described as the demonstrated effect of juvenile truncating alleles. No DYT22JO-specific Wnt, MAPK, mTOR, immune, apoptosis, metabolic, methylation, patient single-cell, spatial-transcriptomic, proteomic, lipidomic, or metabolomic disease signature was established by these studies. A mitochondrial-suspected Estonian case later attributed to *TSPOAP1* does **not** establish primary mitochondrial DYT22JO. [46][48][234][238]

| Suggested mechanistic annotation | Term and evidence boundary |
|---|---|
| Biological process | **GO:0007269**, neurotransmitter secretion; annotate as relevant **protein/pathway biology**, not as an experimentally quantified process in patient neurons. [243][46] |
| Cellular component | **GO:0048786**, presynaptic active zone; **GO:0045202**, synapse. [239][240] |
| Cell type | **CL:0000121**, Purkinje cell, for the mouse morphological findings; presynaptic neurons supplying excitatory Purkinje inputs were assessed through markers, not conclusively assigned a single affected human cell type. [246][46] |
| Pathway description | Calcium-dependent, action-potential-evoked synaptic-vesicle release and excitatory synapse maintenance are supported descriptions; a DYT22JO-specific KEGG signaling cascade has not been established. [46] |

## 7. Anatomical structures affected

**The nervous system is primary.** MRI directly implicates the **cerebellum**, predominantly its **vermis**. Mouse findings locate abnormalities in **cerebellar Purkinje dendrites and their excitatory synaptic inputs**, with the presynaptic active zone as the relevant subcellular site. Speech, swallowing, upper-limb and gait effects involve muscles as **downstream effectors**; primary muscle disease has not been shown. The original MRIs did not show characteristic basal-ganglia volume loss or signal abnormality, despite the potential involvement of wider motor circuits. [46]

Suggested anatomy: **UBERON:0002037, cerebellum**; use **HP:0006855** for the directly observed *vermian atrophy*. Suggested cells/components: **CL:0000121**, Purkinje cell, and **GO:0048786**, presynaptic active zone. Disease-defining unilateral or bilateral anatomical lateralization has not been established; lower-limb gait posturing could be bilateral. [248][169][246][239][46]

## 8. Temporal development

Early motor and language milestones were generally normal in the original four patients; mild learning problems emerged at primary-school age, followed by **insidious early-teenage motor onset and progressive generalization**. Serial MRI showed increasing cerebellar atrophy in individuals scanned at **ages 5, 8 and 14**, and **15 and 17**, respectively. The course appears chronic, but there is **no validated stage system, median progression rate, remission rate, or established intervention window**. The published movement-triggered paroxysms in one person should not be mistaken for remission of the underlying progressive disorder. [46]

## 9. Inheritance, epidemiology, and population

Inheritance is **autosomal recessive**, supported by homozygous affected individuals and segregation in the reported families. If **both parents are confirmed heterozygous carriers of the same pathogenic allele**, the standard Mendelian risk for each pregnancy is **25% affected, 50% carrier, 25% inheriting neither parental variant**; that calculation is a genetic expectation, **not** a measured DYT22JO penetrance. Neither penetrance nor carrier frequency has been estimated. There is no evidence establishing anticipation or germline mosaicism as characteristic. [46][1]

The original four juvenile cases came from **two families**; a later 2025 report added **two unrelated adolescent-onset patients**, and a 2026 publication reports **one childhood-onset case**. These are publication counts, **not an exhaustive worldwide case registry**: overlapping earlier reports must not be double-counted. No defensible prevalence per 100,000, annual incidence, sex ratio, founder-variant frequency, ethnic risk ratio, or geographic distribution estimate is available. The 2018 Estonian exome study reported the individual later included in the 2021 genetic characterization; its cohort’s **57% WES diagnostic yield** is **not a DYT22JO prevalence statistic**. [46][77][78][228][238]

## 10. Diagnostics

**Clinical suspicion** should rise with adolescent progressive, upper-segment-predominant generalized dystonia **plus cognitive deterioration and vermis-predominant cerebellar atrophy**. A movement-disorder examination, developmental and family history, cognitive assessment, swallowing assessment when indicated, and **brain MRI** establish the phenotype and identify competing explanations; MRI is **supportive, not molecular confirmation**. EEG is indicated by seizures, not an obligatory disease biomarker. No specific blood, urine, enzyme, biopsy, PET, EMG, or circulating assay diagnoses DYT22JO. [46][1]

| Test or diagnostic approach | DYT22JO-specific use and limitation |
|---|---|
| Early-onset dystonia/movement-disorder gene panel | Include ***TSPOAP1*** alongside genes for clinically overlapping dystonias; Genomics England lists *TSPOAP1* as a **green/high-evidence** childhood-onset movement-disorder gene. A panel’s actual coverage and deletion/duplication detection must be checked. [65] |
| **WES** with segregation testing | **Directly demonstrated**: homozygosity mapping and WES identified the original causal variants; Sanger sequencing confirmed segregation. Assess both alleles and transcript-specific HGVS nomenclature. [46] |
| **WGS** | Reasonable escalation if panel/WES is unrevealing or structural/noncoding variation is suspected, but **a disease-specific incremental diagnostic yield has not been established**. |
| Single-gene *TSPOAP1* testing | Efficient when a familial pathogenic variant is known; consider targeted testing of relatives with appropriate counseling. [46] |
| CMA; karyotype; FISH | Not first-line confirmation of the reported sequence-variant mechanism. CMA excluded a copy-number explanation in one original patient; use cytogenetic tests when findings independently suggest a chromosome disorder. [46] |
| mtDNA, repeat-expansion, or omics testing | **Not tests for known DYT22JO alleles**; pursue only for a broader differential. The historically mitochondrial-suspected Estonian patient was diagnosed through a nuclear-gene finding. [238][46] |

**Differential diagnosis:** other genetically determined generalized or combined dystonias, particularly when there is developmental or cognitive involvement, and **treatable causes of childhood dystonia** should be assessed through phenotype-guided evaluation. A structurally normal basal ganglia does not exclude DYT22JO. Do **not** use the adult-onset *TSPOAP1* p.Gly1808Ser phenotype as the expected course for juvenile truncating variants. No validated DYT22JO-specific clinical diagnostic criteria or population/newborn screening program was identified. [46][1][65]

## 11. Outcomes and prognosis

The best-supported prognosis is **progressive motor and cognitive morbidity**, with reported deterioration in walking, speech, swallowing and independent functioning; progressive cerebellar atrophy can accompany it. **Five- or ten-year survival, life expectancy, disease-specific mortality, recovery probability, quantitative quality-of-life scores, and validated molecular prognostic biomarkers have not been established.** Swallowing and mobility complications merit assessment, but their DYT22JO-specific incidence cannot be calculated from these reports. [46][1]

## 12. Treatment and implementation

**No treatment has been shown to correct the *TSPOAP1* lesion or halt DYT22JO progression.** Care is individualized and symptomatic; evidence for general dystonia treatments must not be reported as a DYT22JO response rate. A **2023 *TSPOAP1*-biallelic DBS case report exists**, but its accessible PubMed record supplies **no abstract or quantitative outcome**. Hasani *et al.*, *Movement Disorders*, **18 October 2023** online, PMID **37850637**, DOI **10.1002/mds.29618**, [URL](https://pubmed.ncbi.nlm.nih.gov/37850637/). [76][46]

| Treatment or intervention | Role, evidence and important qualification | Suggested NCIT intervention annotation |
|---|---|---|
| **Botulinum neurotoxin injections** | An established **focal-dystonia** intervention that may be considered for selected troublesome neck or other focal components. This is **extrapolation**, not a measured DYT22JO outcome; localized weakness or worsened swallowing requires particular consideration when bulbar symptoms exist. [253][46] | Botulinum toxin injection—**candidate NCIT label; code not verified**. |
| **Trihexyphenidyl or other symptom-directed oral therapy** | Anticholinergic therapy is used in broader dystonia practice; benefit, tolerability, and dose for DYT22JO are **unestablished**. Cognitive vulnerability makes adverse-effect review important. [253][46] | Drug therapy—**candidate label; code not verified**. |
| **Baclofen or clonazepam** | Possible symptom-directed choices based on clinical presentation, **without DYT22JO-specific trial evidence**. Assess sedation and functional trade-offs. [253] | Drug therapy—**candidate label; code not verified**. |
| **Levodopa trial during evaluation** | May help evaluate an alternative *treatable* dystonia diagnosis; **no demonstrated disease-modifying effect for confirmed DYT22JO**. [253][46] | Drug therapy—**candidate label; code not verified**. |
| **Phenytoin for superimposed paroxysms** | Movement-triggered painful dystonic episodes were **controlled in one original patient**. This is a single-person symptomatic observation, **not** a generalized-DYT22JO treatment response. [46] | Anticonvulsant drug therapy—**candidate label; code not verified**. |
| **Deep brain stimulation, considered for severe refractory dystonia** | One *TSPOAP1*-biallelic case report documents its use, but a reliable **genotype-specific percentage benefit and long-term safety estimate are unavailable** from the retrieved report. Broader dystonia DBS outcomes must not be imputed to DYT22JO. [76][253] | Deep brain stimulation—**candidate label; code not verified**. |
| **Physical, occupational, speech and swallowing rehabilitation** | Individualized support for mobility, hand use, communication, nutrition and safety; broadly supported as multidisciplinary dystonia care, **not proven to stop DYT22JO neurodegeneration**. [253][46] | Physical therapy; occupational therapy; speech-language therapy—**candidate labels; codes not verified**. |
| **Gene, RNA, cell, targeted molecular or immunotherapy** | **No DYT22JO-specific approved therapy or identified interventional trial** in the retrieved evidence. These should be marked **investigational/not established**, not offered as existing treatments. [253] | No disease-specific NCIT intervention assignment warranted. |

No **NCT identifier**, *TSPOAP1*-specific pharmacogenomic rule, comparative treatment-response rate, or verified NCIT **code** was found; the suggested labels above require terminology-service validation before knowledge-base ingestion.

## 13. Prevention and counseling

**Primary prevention of the inherited mutation through lifestyle, vaccination, or environmental control is not established.** **Secondary prevention** centers on timely recognition, molecular diagnosis, testing of at-risk relatives for a *known family variant*, and counseling before reproductive decisions. Where a pathogenic familial variant is known, prenatal or preimplantation genetic testing can be discussed according to patient preferences and applicable clinical practice. **Tertiary prevention** means monitoring and treating swallowing difficulty, falls, communication limitations and other functional consequences. There is no DYT22JO-specific newborn screening, vaccine, chemoprophylaxis, or public-health exposure-control program. [46][1]

## 14. Other species and naturally occurring disease

The genetically characterized **natural disease is human** (*Homo sapiens*, **NCBI Taxon:9606**). Mouse (*Mus musculus*, **Taxon:10090**) *Tspoap1* is an experimental ortholog and model, **not evidence of an established naturally occurring veterinary DYT22JO syndrome**. Zebrafish (*Danio rerio*, **Taxon:7955**) has an annotated *tspoap1* ortholog, but that annotation alone does not demonstrate natural disease or phenotype recapitulation. No affected breed, OMIA-defined natural counterpart, zoonotic transmission, or cross-species infectious susceptibility applies to the established Mendelian condition. [266][254][67][46]

## 15. Model organisms and experimental systems

| Model and resource | Demonstrated phenotype or application | Limitation |
|---|---|---|
| ***Tspoap1*/RIMBP1 knockout mouse**; *Mus musculus*, **Taxon:10090**, mouse-gene resource **MGI:2450877** | Increased open-field activity (~**30%**), nearly doubled beam-walk slips, limb clasping, and heightened dystonia-like postures after oxotremorine; progressively abnormal Purkinje dendrites and reduced excitatory synaptic markers. Tests motor-network and cerebellar consequences of complete loss. **Mouse evidence.** [46][130][254] | Provoked mouse movements are **not** identical to spontaneous progressive human dystonia; gross mouse cerebellar volume and Purkinje-cell counts were not significantly reduced in the reported analysis. [46] |
| **Mouse-derived cultured hippocampal autaptic neurons** with conditional presynaptic-protein deletion and RIMBP1 rescue | Patch clamp and synaptic calcium imaging test active-zone function; the **adult-associated p.Gly1808Ser**, not a juvenile allele, produced nearly **100% larger** evoked EPSCs and **>100% larger** calcium transients than wild-type RIMBP1 rescue. **In-vitro evidence.** [46] | Demonstrates a possible **adult-variant** functional mechanism; **not** a patient-derived DYT22JO neuron or direct measurement of juvenile truncating variants. |
| **HEK293T interaction assay** | Adult-associated mutant RIMBP1 co-immunoprecipitated **>3-fold** more CaV2.1 than wild type in the reported experiment. **In-vitro evidence.** [46] | Overexpression/interaction assay, not proof of increased calcium-channel recruitment in juvenile patients. |
| **Other organisms and advanced models** | A zebrafish *tspoap1* ortholog is catalogued. [67] | No disease-recapitulating zebrafish, naturally affected animal, patient iPSC/organoid, single-cell, spatial-transcriptomic, or CRISPR-screen result was established in the retrieved DYT22JO evidence. |

**Knowledge-base interpretation:** attach **PMID:33539324** to the original human phenotypes, two named juvenile variants, mouse findings, and their explicitly qualified mechanistic connection. Attach **PMID:41371074** and **PMID:42027086** to later case observations without inferring unpublished HGVS strings; attach **PMID:37850637** to the existence of a DBS case report **without inventing its outcome**. [46][77][78][76]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 9 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`, `UniProt`, `Taxon`, `MGI`.

19 of 28 terms resolved to a current term; the rest could not be looked up either way.