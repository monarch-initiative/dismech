---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:28.541558'
end_time: '2026-10-09T21:00:10.895334'
duration_seconds: 282.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Split-Foot Malformation with Mesoaxial Polydactyly
  mondo_id: MONDO:0014816
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
citation_count: 52
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 1
  off_topic: 1
  off_topic_references:
  - PMC:PMC11805609
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 8
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - OMIM
  - Taxon
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Split-Foot Malformation with Mesoaxial Polydactyly
- **MONDO ID:** MONDO:0014816 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Split-Foot Malformation with Mesoaxial Polydactyly** covering all of the
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

# Split-Foot Malformation with Mesoaxial Polydactyly: disease-characteristics report

**Split-foot malformation with mesoaxial polydactyly (SFMMP) is an exceptionally rare, congenital, autosomal-recessive disorder caused by biallelic variants affecting the sterile alpha motif (SAM) domain of the long MAP3K20/ZAK protein isoform.** Its defining clinical combination is variable split-foot malformation, abnormal fingernails, and—in one reported family—bilateral sensorineural hearing loss. The original molecular study described **five affected people in two families**; consequently, most apparent phenotype percentages are descriptions of those five people, not reliable population estimates. **PMID: 26755636**.[46][101]

The original abstract states: “Here we describe an autosomal recessive human disease in two unrelated families characterized by a split-foot defect, nail abnormalities of the hands, and hearing loss, due to mutations disrupting the SAM domain of the protein kinase ZAK.” **PMID: 26755636; published online January 11, 2016.**[46]

## 1. Disease information and identifiers

SFMMP is a **developmental limb-patterning disorder**, not an acquired or progressive degeneration of an initially normal foot. “Split foot” describes a cleft appearance caused by deficiency of central foot structures; “mesoaxial polydactyly” refers to an extra, centrally positioned toe. Neither finding alone establishes this molecular diagnosis. The 2023 international skeletal-disorder nosology places SFMMP in its split-hand/foot group as **NOS 39-0100**, with recessive *ZAK* inheritance. **PMIDs: 26755636, 36779427.**[90][196][272][278]

| Identifier or name | Disease-level value |
|---|---|
| MONDO | **MONDO:0014816**.[1] |
| OMIM phenotype | **616890**; distinct from **609479**, the *MAP3K20* gene entry.[69] |
| Orphanet | **ORPHA:488232**.[2] |
| ICD-10 | **Q74.8**, a broad congenital-limb-malformation category rather than an SFMMP-specific code.[2] |
| ICD-11 / disease-specific MeSH descriptor | No specific identifier established in the reviewed disease records; do not substitute a gene/protein MeSH term for a disease descriptor.[2][94] |
| Other terminology | **SFMMP**; “split-foot malformation-mesoaxial polydactyly syndrome”; “split-foot malformation-mesoaxial polydactyly-nail abnormalities-sensorineural hearing loss syndrome”; sometimes **SHFM7**.[2][69] |
| Other identifiers | UMLS **C5567487**; SNOMED CT **1172635005**.[2][106] |

**Evidence provenance:** This is an **aggregated disease-level entry** derived principally from published, individually described patients and family studies, supplemented by curated OMIM, Orphanet, HPO, and ClinVar records. It is **not** an EHR-derived population cohort. ClinVar additionally contains submitted individual-variant observations and literature-derived assertions; those should not be mistaken for independent disease cohorts.[46][106][113][web:EX7zcFJZkZRVQY5N1HGJM6Hx]

## 2. Etiology, risks, protection, and gene–environment interaction

**Established cause:** Homozygosity for either *MAP3K20* **c.1103T>G, p.(Phe368Cys)** or an approximately **14.7-kb intragenic deletion removing exons 12–16** was identified in the two original families. Both lesions affect the **SAM-containing long isoform, ZAKα**. The missense allele segregated with disease in the Pakistani family, was absent from **180 Pakistani controls** and then-available public databases, and affected a structurally important SAM residue. The deletion was homozygous in an affected Tunisian boy and heterozygous in his unaffected first-cousin parents. **PMID: 26755636.**[46][web:64dmrzKYw3F8wQLZlMe7VIVX][web:hd5SRXfhsDlQUuWJemN2EHyg]

**Established risk factor:** Having two disease-causing alleles. Consanguinity occurred in both reported families and increases the chance that relatives inherit the same rare allele; it is **not itself a separate molecular cause**. Family history is therefore clinically useful. Neither variant has an established founder prevalence, carrier frequency, or population-specific risk estimate. No sex-dependent susceptibility, environmental toxin, infection, parental-age effect, protective allele, protective diet, or demonstrated gene–environment interaction has been established **for SFMMP**. General knowledge about teratogens or ribotoxic stress should not be entered as an SFMMP-specific exposure association. **PMID: 26755636.**[46][web:64dmrzKYw3F8wQLZlMe7VIVX]

## 3. Phenotypes

**Denominators matter.** The initial report included **four affected relatives in family 1** and **one affected boy in family 2**. Three of four affected family-1 members had a split foot—two bilateral and one unilateral—while the fourth, despite being homozygous, did not. The Tunisian boy had bilateral involvement. All four affected family-1 members had bilateral sensorineural hearing impairment; the boy passed newborn hearing screening and had normal reported language development at age two, **not a documented comprehensive lifetime exclusion of hearing loss**. These yield descriptive counts of **4/5 with split foot** and **4/5 with reported hearing impairment**, without justifying precise penetrance estimates. **PMID: 26755636.**[46][web:64dmrzKYw3F8wQLZlMe7VIVX][web:dbKj8JkWy7gE7ebDykFfDuZX]

The table distinguishes **directly reported findings** from additional **Orphanet-curated HPO associations**. Curated frequency bands should not be converted into numerical percentages from five cases.[web:hwHbfWnxra0B7zX87KwzsLuY][web:pwBpm7Vg3MOVPYeEasOb1gKg]

| Phenotype type and characteristic | Onset, severity, course, and observed frequency | Functional or quality-of-life implications | Suggested HPO term |
|---|---|---|---|
| **Physical sign: split foot**, unilateral or bilateral; a homozygous affected relative can lack it | Congenital; anatomically variable; **4/5 described patients**, with bilateral, unilateral, and absent presentations; structural defect expected to persist without correction | Footwear fit, support, walking, and appearance may be affected; no SFMMP-specific functional score was reported | **Split foot — HP:0001839**.[46][web:64dmrzKYw3F8wQLZlMe7VIVX][web:hwHbfWnxra0B7zX87KwzsLuY] |
| **Physical sign: central/partial second-toe duplication**, described in individuals from both families | Congenital; variable; **at least two individually identified presentations**, not a validated prevalence | May complicate footwear or foot reconstruction; no quantified SFMMP-specific impact | **Mesoaxial foot polydactyly — HP:0010112**, when its precise anatomical definition is met; record “partial duplication of second toe” separately where appropriate.[46][196] |
| **Physical signs: first–second and/or fourth–fifth toe syndactyly** | Congenital; individually reported, including in the Tunisian boy; severity and total frequency insufficiently characterized | May affect toe configuration and surgical planning; specific functional effect unmeasured | **1–2 toe syndactyly — HP:0010711; 1–2 toe complete cutaneous syndactyly — HP:0005767; 4–5 toe syndactyly — HP:0004692**. Use “complete” only when documented.[web:dbKj8JkWy7gE7ebDykFfDuZX][web:hwHbfWnxra0B7zX87KwzsLuY] |
| **Physical sign: abnormal fingernails**, including duplicated nail beds of fourth fingers | Congenital; characteristic in both families; exact person-level frequency and severity not securely tabulated | Potential appearance or fine-manipulation implications; no measured nail-specific quality-of-life effect | **Abnormality of the nail — HP:0001597**; describe the documented duplicated nail bed in free text rather than equating it with all nail dysplasia.[46][web:64dmrzKYw3F8wQLZlMe7VIVX][web:hwHbfWnxra0B7zX87KwzsLuY] |
| **Clinical sign: bilateral sensorineural hearing impairment** | **4/4 in family 1; 4/5 across the initial report as recorded**. Age at diagnosis, audiometric severity, and progression were not established; family-2 newborn screening was normal | Potential effects on speech and language access; early assessment matters, but no SFMMP-specific outcome scale exists | **Bilateral sensorineural hearing impairment — HP:0008619**.[web:dbKj8JkWy7gE7ebDykFfDuZX][241] |
| **Additional curated structural signs: toe-phalangeal hypoplasia/aplasia and proximal second-toe symphalangism** | Congenital associations in Orphanet; **no independently verified person-by-person counts** for each feature | Depends on resultant foot anatomy; no phenotype-specific measurements | **HP:0010413** second-toe distal phalanx; **HP:0010076** hallux distal phalanx; **HP:0010359**, **HP:0010371**, **HP:0010383** third–fifth toe phalanges; **HP:0100483** second-toe proximal phalanx–metatarsal symphalangism.[web:hwHbfWnxra0B7zX87KwzsLuY] |

**Not established as SFMMP features:** behavioral or psychiatric changes, a characteristic blood/urine chemistry abnormality, and the broad skin, dental, craniosynostosis, and eye phenotype described in a **different, heterozygous MAP3K20-associated disorder**. A reported Tunisian child’s psychomotor and language development were normal at age two. **PMIDs: 26755636, 38451290.**[web:dbKj8JkWy7gE7ebDykFfDuZX][web:ZJvgk4cm9d9MxYGCAItMHt2j]

## 4. Genetic and molecular information

**Causal gene:** *MAP3K20* (**HGNC:17797; NCBI Gene:51776; OMIM:609479**), historically *ZAK*, at **2q31.1**. ZAKα contains an N-terminal kinase domain, leucine zipper, and C-terminal SAM domain; the shorter ZAKβ lacks that SAM domain. **PMIDs: 26755636, 27816943.**[95][91][46][web:Scoq7tGuP1xNmfWOudXb3Z3b]

| SFMMP-associated germline allele | Class, evidence, and molecular consequence | Frequency and interpretation |
|---|---|---|
| **NM_016653.3:c.1103T>G; NP_057737.2:p.Phe368Cys**; rs863225437; ClinVar **VCV000218144** | Homozygous missense SAM-domain allele. ClinVar aggregates **two pathogenic submissions**, but its review status is **“no assertion criteria provided”**—not an independently documented ACMG expert-panel classification. Structural tests found approximately **30% less SAM-domain α-helicity**, loss of cooperative unfolding, and aggregation propensity. **PMID: 26755636.**[web:EX7zcFJZkZRVQY5N1HGJM6Hx][web:EOAnxlclgg6vjWe7CeaEheqH] | Absent from **180 tested Pakistani controls**, EVS, and ExAC in the original investigation. The retrieved ClinVar record gives **no current numerical gnomAD allele frequency**; absence from those older datasets is not a measured zero frequency today.[web:EX7zcFJZkZRVQY5N1HGJM6Hx] |
| **NM_016653.2:c.988-4814_1359+60del**; approximately **14.7 kb**, exons **12–16**; ClinVar **RCV000210488** | Homozygous intragenic **structural deletion** affecting the SAM domain; ClinVar **pathogenic**, one literature-based submission without stated assertion criteria. A **31-bp insertion at the junction** was also reported; preserve the source’s breakpoint notation when recording this complex allele. **PMID: 26755636.**[web:hd5SRXfhsDlQUuWJemN2EHyg] | Absent from the investigators’ **more than 600** in-house samples and consulted CNV databases; **no validated numerical population allele frequency**. Unaffected parents were heterozygous.[web:hd5SRXfhsDlQUuWJemN2EHyg][web:dbKj8JkWy7gE7ebDykFfDuZX] |

**Important 2025 mechanistic refinement:** The original protein-folding findings do **not** prove simple loss of kinase activity. In a later **cell-based, in-vitro/structural study**, disease-associated **p.Phe368Cys showed constitutive ZAK activation even without induced ribosome collisions or normal ribosome interaction**. The authors did **not** show that this activity causes the human limb phenotype in vivo. Thus, annotate **“disrupted SAM structure; constitutive kinase activation demonstrated in an experimental cellular system; developmental consequence unresolved,”** rather than an unqualified “kinase loss of function.” The abstract describes “a known pathogenic variant of the SAM domain” among mutants that can bypass the ribosome requirement. **PMID: 41261136; online November 19, 2025.**[web:q7a1jL9GGAgGvNRUfGEUIrwd]

**Do not conflate MAP3K20 disorders.** A 2024 primary report found **five people with *de novo* heterozygous linker-region variants** and a different spectrum involving craniosynostosis, ectodermal findings, hearing loss, and limb anomalies. Its abstract specifies “five individuals” with “heterozygous *de novo* variants in the linker region between the kinase domain and leucine zipper domain.” Separately, biallelic truncating, kinase-domain alleles cause **MAP3K20-related centronuclear myopathy**, with muscle weakness rather than the characteristic SFMMP foot defect. **PMIDs: 38451290, 27816943.**[web:ZJvgk4cm9d9MxYGCAItMHt2j][web:Scoq7tGuP1xNmfWOudXb3Z3b]

**Modifiers and other genomic findings:** The original linkage analysis found a **9.1-Mb chromosome-2 interval, maximum LOD 3.5**. A later patient with split-hand/foot malformation had homozygous *ZAK* p.Ala505Ser **and** an approximately **2.01-Mb 7q21.3–q22.1 deletion** encompassing established SHFM-related genes; its authors favored the deletion as the principal cause and proposed p.Ala505Ser only as a possible modifier. **Do not register that deletion or p.Ala505Ser as established SFMMP-causing alleles or an established SFMMP modifier.** No SFMMP-specific methylation signature, pathogenic aneuploidy, translocation, or inversion has been established. **PMIDs: 26755636, 32266845.**[web:EOAnxlclgg6vjWe7CeaEheqH][web:jQuU0ZAeiLluYP1hDlcbWWz7]

## 5. Environmental information

No specific toxin, radiation exposure, pollution, occupation, smoking pattern, diet, exercise pattern, alcohol exposure, or infectious agent is implicated **as a cause or reproducible modifier of this Mendelian syndrome**. Chemical induction of ribosome collisions in a laboratory is an experimental tool, **not evidence that an exposed pregnancy will develop SFMMP**. There is no infectious transmission or zoonotic risk. **PMIDs: 26755636, 41261136.**[46][web:q7a1jL9GGAgGvNRUfGEUIrwd]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Inherited biallelic SAM-region *MAP3K20* lesions lead to** an altered long ZAKα isoform during embryonic development; the observed missense variant and exon deletion perturb this domain in different ways. **Human genetics and protein assays demonstrated; PMID: 26755636.**[web:EOAnxlclgg6vjWe7CeaEheqH]
2. **SAM disruption leads to** impaired normal SAM structural behavior: p.Phe368Cys destabilizes the isolated domain, while exon 12–16 deletion removes its encoded region. **Demonstrated or predicted according to allele; PMID: 26755636.**[web:EOAnxlclgg6vjWe7CeaEheqH]
3. **The missense branch: p.Phe368Cys leads to** constitutive ZAK activation in transfected experimental cells, bypassing the usual requirement for ribosome-collision sensing. **Demonstrated *in vitro*; whether this occurs in affected embryonic limb cells is inferred, not shown. PMID: 41261136.**[web:q7a1jL9GGAgGvNRUfGEUIrwd]
4. **The deletion-model branch: mouse SAM-domain deletion leads to** abnormal hindlimb patterning and approximately **60% lower *Trp63* transcript abundance** in homozygous hindlimbs. **Demonstrated in the model; whether reduced TP63 is the obligatory mediator in human SFMMP remains inferred. PMID: 26755636.**[web:dbKj8JkWy7gE7ebDykFfDuZX]
5. **Altered developmental ZAK–TP63-associated signaling is proposed to lead to** disturbed distal limb-bud organization and digit specification, **resulting in** split foot, variable toe duplication/syndactyly, and nail anomalies. The proposed intermediate tissue and signaling links **have not been directly demonstrated in affected human embryos**. **PMID: 26755636.**[web:EOAnxlclgg6vjWe7CeaEheqH]
6. **In a separate, unresolved branch, altered ZAK function is associated with** sensorineural hearing impairment in one human family; **the precise auditory cell injury or developmental mechanism is unproven**. Mouse *Zak* expression in cochlear hair cells provides context, but the original SAM-deletion mice did not have a detectable abnormal Preyer reflex. **PMID: 26755636.**[web:dbKj8JkWy7gE7ebDykFfDuZX]

**Pathway detail and evidence boundaries:** ZAK is a **MAP kinase kinase kinase**. A 2025 primary biochemical/cryo-electron-microscopy study showed that ribosome collisions position ZAK on neighboring **RACK1** proteins, promote **SAM-domain dimerization** and activation, and engage downstream **p38/JNK** stress signaling; **SERBP1** opposes inappropriate activation. That work explains how p.Phe368Cys can be hyperactive experimentally, **not** whether ordinary embryonic ribosome collisions cause SFMMP. The 2016 mouse experiments found normal *Fgf8*, *Shh*, and *Trp63* **spatial staining patterns** in a tested context, whereas quantitative testing found reduced *Trp63* **amount** in SAM-mutant hindlimbs. A WNT, FGF8, or SHH defect should therefore **not** be recorded as a directly established SFMMP molecular abnormality. **PMIDs: 26755636, 41261136.**[web:dbKj8JkWy7gE7ebDykFfDuZX][web:q7a1jL9GGAgGvNRUfGEUIrwd]

**Ontology-ready mechanism annotations:** Suggested biological-process terms are **protein phosphorylation (GO:0006468)**, **embryonic limb morphogenesis (GO:0030326)**, and **limb development (GO:0060173)**; these are annotation suggestions, not claims that each process was individually measured in patients. The experimental subcellular context includes **cytoplasm and ribosome**; the structural target is a protein SAM domain, not a demonstrated mitochondrial, lysosomal, or metabolic defect. Suggested relevant cells are **mesenchymal cell (CL:0000134)**, **chondrocyte (CL:0000138)**, and **keratinocyte (CL:0000312)**, with limb-bud ectoderm and auditory hair cells named anatomically; involvement of each particular cell class **in human SFMMP has not been independently proven**. No disease-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or validated epigenomic signature was identified in the reviewed evidence. The decisive functional-genomics application was **CRISPR/Cas editing of mouse *Zak***. **PMIDs: 26755636, 41261136.**[46][web:q7a1jL9GGAgGvNRUfGEUIrwd][210][227]

## 7. Anatomical structures affected

**Primary sites:** distal lower limbs, especially the **foot (UBERON:0002387)**, toes, phalanges/metatarsals and their developmental precursors; fingernail units are also affected. An **apical ectodermal ridge (UBERON:0004356)** is a useful *developmental-context* annotation, **not a directly sampled lesion in a patient**. **Secondary/associated site:** the auditory system and **ear (UBERON:0001690)**; a cochlear cellular mechanism remains unconfirmed. Relevant tissue classes include developing ectoderm/epithelium, mesenchyme, and developing connective/skeletal tissues. Involvement may be **unilateral or bilateral and asymmetric**; one genetically affected person had **no split foot**. Do not assign the mouse knockout’s severe embryonic cardiac phenotype as an established organ manifestation of surviving humans with SFMMP. **PMID: 26755636.**[46][202][280]

**Suggested cellular-component annotation:** cytoplasm and ribosome for the experimentally studied ZAK stress-response machinery; **not** a patient-specific subcellular pathology diagnosis. **PMID: 41261136.**[web:q7a1jL9GGAgGvNRUfGEUIrwd]

## 8. Temporal development

The malformations are **congenital**; Orphanet specifies **neonatal onset**. The defensible natural-history description is **persistent structural differences with variable severity**, rather than an acute, episodic, staged, or relapsing disease. Neither a progression rate nor formal early/intermediate/end stages, spontaneous anatomical remission, or long-term audiometric trajectory has been established. Embryonic limb patterning is the biologically relevant vulnerability period; after birth, the clinically actionable period is early assessment of hearing and function. The Tunisian child’s normal hearing screen and development at two years must not be extrapolated to lifelong outcome. **PMID: 26755636.**[2][web:dbKj8JkWy7gE7ebDykFfDuZX]

## 9. Inheritance and population

**Autosomal recessive.** When both biological parents carry the same established pathogenic allele, the standard Mendelian **risk per pregnancy is 25% affected, 50% carrier, and 25% inheriting neither familial allele**; counseling should confirm the actual familial genotypes. Variable expressivity is directly observed: one homozygous affected relative lacked a split foot, while another had unilateral involvement. That observation alone cannot yield a population penetrance percentage. No anticipation, germline mosaicism rate, founder effect, or carrier frequency has been established. **PMID: 26755636.**[46][web:64dmrzKYw3F8wQLZlMe7VIVX]

Orphanet’s estimate is **prevalence <1 per 1,000,000**, not a measured national incidence. **Annual incidence, population age distribution, geographic prevalence, and population sex ratio are unknown.** The original cases were from families in Pakistan and Tunisia; their locations do not establish ethnic restriction or an endemic region. A later comparison table records **three males and one female** in the original Pakistani family and **one male** in the Tunisian family, but **4:1 is a five-person report count, not a disease sex ratio**. **PMIDs: 26755636, 38451290.**[2][web:ZJvgk4cm9d9MxYGCAItMHt2j]

## 10. Diagnostics and screening

**Clinical suspicion:** congenital split/atypical feet, central toe duplication or syndactyly, characteristic fingernails, and potentially bilateral sensorineural hearing loss, especially with similarly affected relatives or consanguinity. Examine all four limbs and nails, obtain a pedigree, and arrange **foot radiographs** to define skeletal anatomy when management requires it. Obtain **age-appropriate formal audiology even if an initial newborn screen was passed**, because the molecular syndrome can include hearing loss and a normal screen is not a complete lifelong audiological evaluation. Foot imaging and audiology are **phenotype-directed clinical recommendations**, not validated SFMMP-specific diagnostic criteria. **PMID: 26755636.**[46][web:dbKj8JkWy7gE7ebDykFfDuZX][76]

**Molecular confirmation:** seek **biallelic pathogenic/likely pathogenic *MAP3K20* variants**, considering **SNVs and intragenic exon deletions**. An appropriate **limb-malformation/SHFM panel with deletion–duplication analysis**, **exome sequencing plus reliable CNV calling**, or **genome sequencing** can be selected according to the phenotype and laboratory capabilities. Single-gene sequencing is reasonable when a familial allele is known, but **sequencing alone may miss the documented exon 12–16 deletion**; use validated copy-number or breakpoint assessment. The original study used linkage, exome sequencing, array-CGH, qPCR, breakpoint PCR, and segregation analysis; GTR lists tests associated with *MAP3K20* and this condition. **PMID: 26755636.**[web:EOAnxlclgg6vjWe7CeaEheqH][web:RjRxYfl6gV7WymF9gF9gk2y6]

**Differential diagnosis:** other molecular forms of split-hand/foot malformation, including **7q21/*DLX5–DLX6*** abnormalities and other SHFM loci; **heterozygous MAP3K20 linker-associated disease**, particularly if craniosynostosis or broad ectodermal findings predominate; and **biallelic kinase-domain MAP3K20 myopathy**, if generalized weakness, hypotonia, or abnormal muscle biopsy dominates. These are distinct molecular diagnoses despite overlap in gene or limb appearance. **PMIDs: 32266845, 38451290, 27816943.**[web:jQuU0ZAeiLluYP1hDlcbWWz7][web:ZJvgk4cm9d9MxYGCAItMHt2j][web:Scoq7tGuP1xNmfWOudXb3Z3b]

**Tests without an established routine SFMMP role:** characteristic blood/urine biomarkers, enzyme assays, biopsy, ECG/EEG/EMG, mitochondrial sequencing, repeat-expansion testing, liquid biopsy, and clinical metabolomic/proteomic/epigenomic assays. Chromosomal microarray or cytogenetic testing can be useful **for a broader unresolved differential diagnosis**, not because the two established SFMMP alleles are aneuploidies. There are **no demonstrated SFMMP-specific formal diagnostic-score criteria or population newborn molecular-screening program**. **PMIDs: 26755636, 32266845.**[web:EOAnxlclgg6vjWe7CeaEheqH][web:jQuU0ZAeiLluYP1hDlcbWWz7]

## 11. Outcome and prognosis

**Life expectancy, 5-/10-year survival, mortality rates, disease-specific deaths, EQ-5D/SF-36 scores, and validated prognostic biomarkers are unavailable for SFMMP.** No progressive multiorgan failure has been established. The main plausible long-term burdens are those of **persistent foot anatomy and potentially hearing impairment**; their individual severity, footwear needs, and hearing trajectory require assessment, not prediction from genotype alone. **The single reported two-year-old Tunisian child had normal psychomotor and language development at that examination.** There are no reliable genotype-specific response rates or natural-history cohorts. **PMID: 26755636.**[46][web:dbKj8JkWy7gE7ebDykFfDuZX]

## 12. Treatment and implementation

**There is no established medication or molecular treatment that reverses the congenital SFMMP lesion.** Management is individualized and function-oriented; the table separates **general clinical practice or evidence from other cleft-foot cases** from outcomes demonstrated in genetically confirmed SFMMP.[46][76][256]

| Intervention and suggested NCIt term | Practical role and evidence boundary |
|---|---|
| **Orthopedic/foot assessment; footwear adaptation, orthoses, and rehabilitation**. Suggested broad intervention vocabulary: **Physical Therapy** where applicable; verify any more specific local NCIt code before loading it. | Assess balance, walking, pressure, pain, and shoe fit; treat observed problems. **No SFMMP-specific treatment-response percentage** exists. This is supportive care, not alteration of embryonic anatomy.[46][256] |
| **Individualized foot reconstruction**, potentially including cleft closure, correction of selected duplicated structures, or syndactyly procedures; broad **Surgical Procedure — NCIT:C15329**. | Consider only after imaging and assessment of expected function and patient/family goals. A **2020 cleft-foot case without an established SFMMP genotype** reported improved support and appearance maintained two years after surgery; it **does not demonstrate efficacy or risk rates in SFMMP**. **PMID: 32190557.**[256][211] |
| **Audiological assessment, hearing technology when indicated, and early communication/language intervention**; use appropriately verified device-specific NCIt terms, rather than a generic surgery code for every hearing intervention. | Follow general pediatric hearing-loss practice: screen by **1 month**, diagnose identified loss by **3 months**, and initiate intervention by **6 months**; hearing aids or cochlear implants depend on measured hearing and clinical assessment. These are **general hearing-care benchmarks, not SFMMP trial results**.[76][77] |
| **Genetic counseling — NCIT:C15240**. | Explain recessive recurrence risk, variable foot expression, carrier testing of relatives when appropriate, and reproductive options after familial variants are confirmed.[46][211] |

**Not established for this disorder:** disease-modifying pharmacotherapy or pharmacogenomic dosing rules; gene, cell, RNA, immune, or targeted therapy; a validated genotype-guided treatment algorithm; an SFMMP-specific interventional trial or NCT identifier; treatment response rates or disease-specific adverse-event rates. In particular, **experimental ZAK inhibition used to interrogate a cellular p.Phe368Cys mechanism is not an indicated treatment for a congenital limb malformation**. **PMID: 41261136.**[web:q7a1jL9GGAgGvNRUfGEUIrwd]

## 13. Prevention

**Primary prevention of the underlying allele is not possible through vaccination, diet, or avoidance of a known SFMMP-specific exposure.** For a family with established variants, genetic counseling, targeted carrier testing, and discussion of **prenatal or preimplantation genetic testing** can support reproductive decisions; these are **options**, not evidence of environmental prevention or a population screening recommendation. **Secondary prevention** means identifying an affected child’s hearing or functional needs early; **tertiary prevention** means managing footwear, mobility, and communication-related consequences. Routine immunizations remain appropriate but **do not prevent SFMMP**. **PMID: 26755636.**[46][76]

## 14. Other species and naturally occurring disease

**Human:** *Homo sapiens*, **NCBI Taxon:9606**; **mouse:** *Mus musculus*, **NCBI Taxon:10090**, ortholog *Map3k20*, **NCBI Gene:65964; MGI:2443258**. Other species have *MAP3K20* orthologs, but **an authenticated, naturally occurring veterinary equivalent caused by the human SFMMP SAM-domain alleles was not established** in the reviewed evidence. Naturally occurring polydactyly in an animal should **not** be equated with this molecular syndrome. Cross-species conservation supports experimental comparison; there is **no zoonotic transmission**. **PMID: 26755636.**[121][126][128][130][134]

## 15. Model organisms and experimental systems

| Model or system | What it reproduces or demonstrates | Principal limitation and research application |
|---|---|---|
| **Mouse *Zak* disruption of both isoforms**, produced with CRISPR/Cas-edited embryonic stem cells | Homozygous knockout caused **fully penetrant embryonic lethality around E9.5**, with severe cardiac edema and growth retardation; heterozygotes appeared morphologically normal. **PMID: 26755636.**[web:EOAnxlclgg6vjWe7CeaEheqH] | Models an extreme **whole-gene loss**, **not** the viable, SAM-region-specific human SFMMP phenotype; demonstrates why variant domain/isoform matters. |
| **Mouse SAM-region deletion**, generated using a roughly **12-kb engineered deletion** | **4/64 animals** had variable hindlimb duplication/polydactyly phenotypes; homozygous mutant hindlimbs showed approximately **60% less *Trp63* expression** by qRT-PCR. **PMID: 26755636.**[web:EOAnxlclgg6vjWe7CeaEheqH][web:dbKj8JkWy7gE7ebDykFfDuZX] | **Low penetrance**; phenotypes can include substantial hindlimb/pelvic duplication rather than a close copy of a human cleft foot. No obvious ear abnormality or Preyer-reflex difference was found. Useful for developmental mechanism, not for estimating human penetrance or hearing outcomes. |
| **Purified wild-type and p.Phe368Cys SAM domains**, structural/biophysical assays | Demonstrated missense-domain destabilization, reduced helicity, altered unfolding, and aggregation propensity. **PMID: 26755636.**[web:EOAnxlclgg6vjWe7CeaEheqH] | Isolated protein cannot establish the full embryonic phenotype or net cellular kinase output. |
| **Human ZAK-knockout HEK293T cells re-expressing ZAK variants; cryo-EM/biochemistry of ribosome complexes** | Demonstrated RACK1-associated collision sensing and **constitutive, ribosome-interaction-independent activation of p.Phe368Cys** in the tested cellular system. **PMID: 41261136.**[web:q7a1jL9GGAgGvNRUfGEUIrwd] | These are **not developing human limb or auditory cells**; no p.Phe368Cys human-limb rescue experiment or corresponding knock-in developmental outcome was established in that study. |

**Knowledge-base interpretation:** Record the **human biallelic genotype–phenotype association as established**; record the mouse SAM-deletion/*Trp63* result and cellular p.Phe368Cys hyperactivity as **different, complementary mechanistic evidence types**. The exact link between those results—and the cause of hearing impairment—remains unresolved. **PMIDs: 26755636, 41261136.**[46][web:q7a1jL9GGAgGvNRUfGEUIrwd]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 1 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC11805609` (1 mention) - Fun in the sun: ribosomes defend against UV irradiation.
  - shared terms: none

Weighed against this report's own most characteristic terms: `web`, `established`, `sfmmp`, `hearing`, `foot`, `zak`, `affected`, `family`, `molecular`, `normal`, `variant`, `allele`, `phenotype`, `dbkj8jkwy7ge7ebdykffduzx`, `loss`, `map3k20`, `limb`, `sfmmp-specific`, `disease`, `variable`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 8 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `OMIM`, `Taxon`, `MGI`.

25 of 33 terms resolved to a current term; the rest could not be looked up either way.