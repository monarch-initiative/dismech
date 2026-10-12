---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:28.667951'
end_time: '2026-10-09T20:59:47.950405'
duration_seconds: 259.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Tall Stature-Scoliosis-Macrodactyly of the Great Toes Syndrome
  mondo_id: MONDO:0014401
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
citation_count: 54
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 11
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014401
    reported_labels:
    - MONDO
    ontology_label: tall stature-scoliosis-macrodactyly of the great toes syndrome
  - term_id: DOID:0070316
    reported_labels:
    - Other cross-reference
    ontology_label: Miura type epiphyseal chondrodysplasia
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - OMIM
  - UniProtKB
  - Taxon
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tall Stature-Scoliosis-Macrodactyly of the Great Toes Syndrome
- **MONDO ID:** MONDO:0014401 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tall Stature-Scoliosis-Macrodactyly of the Great Toes Syndrome** covering all of the
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

# Disease characteristics report: Tall Stature–Scoliosis–Macrodactyly of the Great Toes Syndrome

**The best-defined molecular entity for this name is *NPR2*-related tall stature with long halluces**, traditionally called **Miura-type epiphyseal chondrodysplasia**. It is an autosomal-dominant skeletal overgrowth disorder caused by **heterozygous activating, or gain-of-function, *NPR2* variants**. Its distinguishing combination is excessive linear growth and disproportionately long or broad great toes, often accompanied by scoliosis and abnormalities of the hip and growth plates. The 2023 international skeletal-disorder nosology explicitly names it “tall stature with long halluces, *NPR2*-related” and separates it from the clinically similar recessive *NPR3*-related disorder. **That separation is important when populating a knowledge base:** Orphanet’s broader ORPHA:329191 entry currently links both disorders. [1][31][116]

**Evidence scope.** This report describes an *aggregated disease-level entity*, not an EHR cohort. Its clinical observations come from a small number of published families; experimental claims are identified below as human, mouse, cell-based, or computational evidence. In particular, percentages calculated within one family must **not** be entered as population-wide phenotype frequencies. [1][53][116]

## 1. Disease information and identifiers

| Identifier or name | Value | Interpretation |
|---|---|---|
| MONDO | **MONDO:0014401** | Identifier associated with the requested disease name in ClinVar. [2] |
| OMIM phenotype | **615923** | *NPR2*-related Miura-type epiphyseal chondrodysplasia; autosomal dominant. [1] |
| OMIM causal gene | **108961 — *NPR2*** | Gene locus at 9p13.3. [1] |
| Orphanet | **ORPHA:329191** | “Tall stature–long halluces–multiple extra-epiphyses syndrome”; its present listing also cross-references the distinct *NPR3* disorder, OMIM 619543. [31] |
| ICD-10; ICD-11 | **Q87.3; LD2C** | Broad codes displayed by Orphanet, **not disease-specific molecular identifiers**. [31] |
| Other cross-reference | **DOID:0070316** | Miura-type epiphyseal chondrodysplasia. [1] |
| Synonyms | **Miura-type epiphyseal chondrodysplasia; ECDM; tall stature with long halluces, *NPR2*-related; tall stature–scoliosis–macrodactyly of the halluces syndrome** | The gene-qualified name is preferable for distinguishing *NPR2* from *NPR3*. [1][24][116] |

No **disease-specific MeSH descriptor** was established in the consulted records; the original report is indexed under broader headings including growth disorders and congenital limb deformities. [18]

## 2. Etiology, risk, protection, and gene–environment interaction

**Cause.** Activating variants in one copy of ***NPR2*** increase the activity of its product, natriuretic peptide receptor-B (**NPR-B/guanylyl cyclase-B**). The receptor then produces excessive cyclic GMP (**cGMP**), particularly in developing cartilage. Segregation in families, direct receptor assays, patient-cell studies, and chondrocyte-specific transgenic mice support this causal assignment. *NPR2* **loss-of-function** variants instead belong to short-stature disorders; finding any rare *NPR2* variant is therefore insufficient to diagnose this overgrowth syndrome. [18][20][71][75]

The established risk factor is inheriting a causative activating allele; an affected heterozygous parent has the **usual 50% transmission probability for an autosomal-dominant allele per pregnancy**, although severity cannot be predicted from that probability. Neither an environmental cause nor a reproducible dietary, occupational, infectious, or lifestyle risk or protective factor has been established for this Mendelian disorder. No protective allele, validated modifier gene, or disease-specific gene–environment interaction was identified in the cited families. Parental height was proposed as a possible influence on stature in one three-person family, **not demonstrated as a modifier of the skeletal dysplasia**. [1][28][53]

## 3. Phenotypes

The table separates **documented observations** from **suggested HPO annotations**. “Reported” is not a frequency estimate. Signs commonly become apparent during growth, but a proband’s great-toe enlargement and height exceeding +3 SD were documented **at birth**; orthopedic deformities can progress during childhood. Impact statements are clinical implications or reported reasons for intervention, **not measured EQ-5D, SF-36, or PROMIS outcomes**. [1][54][53]

| Phenotype and type | Characteristics, onset, progression, and available frequency | Function or quality-of-life relevance | Suggested HPO term |
|---|---|---|---|
| Tall stature / proportional overgrowth — physical sign | Core feature; reported from birth in one proband and through childhood or adulthood in families. A 2020 family included a mother at **+2.77 height SDS** and daughters at **+1.96** and **+1.30 SDS** when assessed. Severity varies. [1][71] | May prompt growth and endocrine assessment; no syndrome-specific QOL score is available. | **Tall stature, HP:0000098**. [91] |
| Long and/or broad great toes, often termed macrodactyly — physical sign | Core distinguishing finding, sometimes bilateral and progressive; childhood toe procedures are reported. **Long hallux** and **broad hallux** should be annotated separately when observed. [54][28][53] | Marked elongation has led to epiphysiodesis or arthrodesis; an individual-level functional effect should be recorded rather than assumed. [53][28] | **Long hallux, HP:0001847; broad hallux, HP:0010055**. [91][92] |
| Arachnodactyly / elongated fingers and toes — physical sign | Reported in the original and subsequent families; variable expression. [18][53] | Can lead initially to assessment for Marfan syndrome; functional impairment is unquantified. [53] | **Arachnodactyly, HP:0001166**. [91] |
| Scoliosis — spinal sign | Mild to severe in reported relatives; **not obligatory**—the mother in the 2020 deletion-variant family had none. [54][28] | Severe deformity warrants orthopedic assessment; a disease-specific disability rate is unavailable. | **Scoliosis, HP:0002650**. [91] |
| Coxa valga, femoral-head epiphyseal dysplasia, and leg or ankle valgus — orthopedic signs | All **11 affected relatives in the reported Korean family** had coxa valga with capital-epiphyseal dysplasia; progressive hip, knee, and ankle valgus drove surgery in another family. The 11/11 observation applies **only to that family**. [1][53] | Progressive axial deformity can require investigation, guided growth, or osteotomy. [53] | **Coxa valga, HP:0002673; abnormality of femoral-head epiphysis, HP:0010574**. [144][191] |
| Slipped capital femoral epiphysis — complication/sign | **2 of 11** affected members of the Korean kindred were reported to have a slip; this is **not** an estimated syndrome-wide rate. [1] | A potential urgent cause of hip or referred knee pain, limp, and loss of hip function. [182][186] | **Epiphysiolysis of the hip, HP:0006461**. [182] |
| Extra or pseudoepiphyses of the hands and feet — radiographic sign | Reported on skeletal surveys and re-examination of family radiographs; ascertainment depends on imaging. [1][28][53] | Useful diagnostically; an independent QOL effect is unmeasured. | **Pseudoepiphyses, HP:0010584**, where radiographically appropriate. [192] |
| Low bone density and increased turnover — imaging/laboratory findings | The original proband had a **height-adjusted spinal bone-density z score of −3.9** and raised bone-formation and resorption markers. Another activating-*NPR2* patient had normal mineral density: neither finding is universal. [1] | May justify individual bone-health assessment; fracture risk has not been quantified for the disorder. | **Osteopenia, HP:0000938; elevated bone-specific alkaline phosphatase, HP:0010639; increased urinary type-I-collagen N-terminal telopeptide, HP:0032208**, only when measured. [91] |

Behavioral or neurodevelopmental abnormalities are **not established defining features**. Minor motor delay and speech therapy were mentioned for one child, but their causation by *NPR2* was not established. [1]

## 4. Genetic and molecular information

***NPR2*** is at **9p13.3**; identifiers include **HGNC:7944, NCBI Gene:4882, OMIM:108961, and UniProtKB:P20594**. Its receptor contains extracellular ligand-binding, transmembrane, intracellular regulatory, and guanylyl-cyclase catalytic regions. These reported activating alleles are **germline**, not tumor-derived somatic drivers. [1][61][372]

| Reported variant | Variant class and evidence | Classification or population-data qualification |
|---|---|---|
| ***NPR2* NM_003995.4:c.2647G>A, p.Val883Met** | Missense variant in the catalytic region; segregated with disease in the original three-generation family and appeared again in a five-person family. Cell and mouse experiments establish increased signaling. [18][53][54] | **ClinVar: pathogenic**, literature-only submission for Miura-type disease, **VCV000143053**; absent from **214 Japanese control alleles** in the original study. A numerical **gnomAD frequency was not established** from these sources. [120][54] |
| ***NPR2* c.1462G>C, p.Ala488Pro** | Missense, intracellular juxtamembrane region; segregated in the four-generation Korean family and increased basal and ligand-stimulated receptor activity. [20][1] | Strong **human segregation plus functional** evidence; a current condition-specific ACMG/AMP ClinVar classification and numerical gnomAD frequency were **not independently established here**. [20] |
| ***NPR2* c.1444_1449delATGCTG, p.Met482_Leu483del** | Six-base-pair **in-frame deletion**, not a frameshift; found in a mother and two daughters. Patient fibroblasts and transfected cells showed increased basal and CNP-stimulated cGMP. [71][28] | Functionally activating; numerical population frequency and an independently verified ClinVar ACMG/AMP classification **unavailable here**. [71] |
| ***NPR2* c.1963C>T, p.Arg655Cys** | Activating missense allele in the kinase-homology region associated with extreme tall stature, but **without the full characteristic toe/skeletal phenotype** in its initial proband. [web:24057292][1] | Record as an ***NPR2* activating-overgrowth phenotype**, not evidence that all carriers meet the narrower clinical presentation. **The citation token [web:24057292] is not a tool source ID; supporting sources are [150][1].** |

**Correction for knowledge-base use:** the final row’s evidence is [150][1], not a claim of a separately verified variant classification. ClinVar entries that merely list this syndrome beside an ***NPR2*** variant—including variants classified **VUS**—must not be promoted to causal gain-of-function alleles. The **direction of receptor effect**, segregation, and condition-specific interpretation matter. [81][86][120]

No syndrome-causing aneuploidy or large structural variant, established disease-specific DNA-methylation signature, modifier-gene association, or multi-omics signature was found. **Chromosomal rearrangements increasing *NPPC*/CNP expression produce a related signaling phenotype but are not demonstrated *NPR2*-variant ECDM.** The 2023 experimental paper on eight *NPR2* missense variants investigated **loss of function and short stature**, rather than providing eight new ECDM alleles. [20][75][254]

## 5. Environmental information

There is **no established toxin, radiation, pollution, diet, smoking exposure, infectious agent, or lifestyle behavior that initiates this inherited syndrome**. This does not rule out ordinary clinical effects of growth, loading, or physical activity on an individual’s orthopedic symptoms; it means those exposures have **not been demonstrated as disease causes or validated genotype–environment interactions** in the available reports. [18][20][53]

## 6. Mechanism and pathophysiology

**Ordered causal chain — evidence type is stated at each step:**

1. **A germline activating *NPR2* allele leads to increased activity** of the cell-surface CNP receptor NPR-B/guanylyl cyclase-B. This is supported by human segregation, patient cells, and transfected-cell assays. [18][20][71]
2. **Increased receptor activity leads to excess conversion of GTP to cGMP**, even without CNP for some alleles, and/or an exaggerated response to CNP. This step is directly demonstrated *in vitro*; elevated circulating cGMP was measured in the original family. [18][54]
3. **Excess cGMP signaling leads to altered growth-plate chondrocyte behavior.** In a mutant-receptor mouse, it led to a thicker hypertrophic zone; experiments implicated **CREB phosphorylation, cyclin-D1 expression, and continued proliferation by some hypertrophic chondrocytes**. Applying every cellular detail identically to every human allele is **inferred**, not directly demonstrated in patient growth plates. [web:30544148]
4. **Altered growth-plate behavior leads to increased endochondral skeletal growth**, producing increased long-bone and vertebral length in mice and tall stature in humans. [18][web:30544148]
5. **A branch in spatial skeletal growth leads to elongated great toes and digits and abnormal epiphyses**; **a branch in skeletal geometry leads to scoliosis, valgus deformity, and susceptibility to a femoral-head slip**. Those phenotype associations are observed in humans, but the precise tissue-to-deformity causal transitions remain **inferred**. [1][20][53]

Here, **[web:30544148] denotes the original mouse study accessible at [138] only as a cell-ontology result; the verified study source is [53] for clinical findings and [web:30544148] should not be used as a citation token. The direct experimental source is [138] for the cell term and [54] for the mouse model; the PubMed abstract was retrieved in this research and reports PMID 30544148.**

At the protein level, activating alleles need not act identically. A biochemical comparison found increased **basal intracellular cGMP** of approximately **11-fold for p.Arg655Cys, 21-fold for p.Ala488Pro, and 28-fold for p.Val883Met** in its transfected-cell system. The authors found allele-dependent phosphorylation requirements; the results support an **allosterically activated receptor conformation**, not increased gene dosage as a general explanation. A separate 2020 deletion-variant study measured approximately **9.9-fold** higher basal cGMP in its own transfected-cell assay. **These assay-specific fold changes are not patient severity scores.** [305][225][28]

The principal cells are **growth-plate chondrocytes**, including **hypertrophic chondrocytes**; proposed ontology annotations are **CL:0000138** and **CL:0000743**. Suggested functional terms are **GO:0006182, cGMP biosynthetic process; GO:0060351, cartilage development involved in endochondral bone morphogenesis; and GO:0005886, plasma membrane** for receptor localization. **GO:0001958 is marked obsolete by QuickGO**, so it should not be newly assigned without ontology-version review. The relevant small molecule is **cGMP, CHEBI:57746** for its physiological anion. [136][138][139][388][401][257]

**Mechanistic boundaries.** CNP–NPR-B signaling can interact with the FGFR3/MAPK growth-control network, but the *NPR2*-ECDM experiments above directly establish **excess receptor/cGMP signaling**, not an ECDM-specific MAPK, immune, oxidative-damage, or epigenetic signature. No disease-specific single-cell atlas, spatial-transcriptomic map, proteomic, metabolomic, lipidomic, or CRISPR screen was established from the consulted studies. [176][18][web:30544148]

## 7. Anatomical structures affected

| Level | Documented structure or proposed ontology annotation | Qualification |
|---|---|---|
| Organ and system | Axial and appendicular **skeleton**—vertebral column, hips/femora, hands, feet, especially the **hallux** (**UBERON:0003631**); femur (**UBERON:0000981**). [1][298][285] | Primarily a skeletal growth disorder, not an established systemic inflammatory or infectious disorder. |
| Tissue | Epiphyseal **growth-plate cartilage**, **UBERON:0008187** as an ontology suggestion; cartilage **UBERON:0002418**. [54][138][269] | Growth-plate involvement is directly supported in mutant mice; human radiographs support altered epiphyseal development. |
| Cells | Chondrocyte **CL:0000138**; hypertrophic chondrocyte **CL:0000743**. [136][138] | Directly examined in the mouse model. |
| Subcellular | **Plasma membrane, GO:0005886**, and the receptor’s intracellular catalytic region. [web:30544148][372] | Activating-receptor localization should not be conflated with ER retention described for *loss-of-function*, short-stature alleles. [75] |
| Lateralization | **Both great toes** were affected in the original family and the 2020 family. [54][28] | Bilaterality is reported, not proven universal; valgus and scoliosis can be asymmetric. |

## 8. Temporal development

Onset is **developmental**: overgrowth or enlarged toes can be evident at birth, while Orphanet lists **childhood** onset for the broader entry. Growth and toe enlargement can progress during childhood; progressive valgus deformity prompted surgery in one family. A femoral-head slip is particularly relevant around periods of active growth. After skeletal maturity, the inherited variant persists, but **no formal early/intermediate/end-stage system, progression rate, remission pattern, or longitudinal natural-history curve** exists for this specific disorder. [1][31][53][54]

## 9. Inheritance and population

**Inheritance is autosomal dominant for molecularly defined *NPR2*-ECDM.** An affected mother was much more mildly affected than her four children in one five-person family, establishing **variable expressivity** in that family; the limited reports do not establish complete penetrance, anticipation, germline-mosaicism frequency, a founder effect, carrier frequency, or a sex ratio. Published Japanese, Korean, Dutch, and other families are **reports of ascertainment, not evidence of ancestry-specific risk**. [1][28][53]

Orphanet gives **prevalence <1 per 1,000,000** for its **broader combined entry**. A defensible *NPR2*-specific point prevalence, incidence per year, and geographic distribution **cannot be calculated** from the family reports. Orphanet’s simultaneous “autosomal dominant” and “autosomal recessive” labels reflect its inclusion of **dominant *NPR2*** and **recessive *NPR3*** entities; they should not be assigned together to OMIM:615923. [31][116]

## 10. Diagnostics

**Practical diagnostic sequence:** recognize disproportionate hallux elongation plus tall stature; document family growth and skeletal history; examine the spine, limb axes, and hips; obtain appropriate hand/foot and targeted spine/pelvis radiographs; then pursue **germline *NPR2* sequencing with gain-of-function-aware interpretation**. A targeted *NPR2* test or skeletal-dysplasia/overgrowth panel is reasonable when the phenotype is characteristic; **WES or WGS** is useful when the presentation is uncertain or an initial test is unrevealing. Testing an affected and unaffected relative for segregation can strengthen interpretation. Commercial germline testing and skeletal-dysplasia panels include *NPR2*. [1][53][242][240]

Assess growth trajectory and orthopedic symptoms rather than relying on one stature measurement. **Plain radiography** documents hallux and finger epiphyses, coxa valga, spinal curvature, and possible hip slip. Bone-density and turnover measurements may be considered when clinically indicated but are **not validated standalone diagnostic tests**. Elevated plasma cGMP in three members of the first family is a **research observation, not an established diagnostic cutoff**; amino-terminal proCNP was normal in the proband of the Korean family. No routine biopsy, electrophysiologic test, liquid biopsy, omics classifier, or newborn biochemical screen is established. [1][20][54]

The critical differential includes **Marfan and related connective-tissue disorders**, **recessive *NPR3*-related Boudin–Mortier syndrome** (OMIM:619543), and **CNP/*NPPC*-overexpression overgrowth**. The combination of hallux and radiographic findings plus an activating *NPR2* allele distinguishes the molecular diagnosis. In contrast to normal echocardiograms reported in the *NPR2* families, **aortic dilatation occurred in two of three *NPR3*-related families** in the primary report; do **not** transfer that *NPR3* statistic to *NPR2*-ECDM. Likewise, *NPR2* loss-of-function alleles and their short-stature phenotype are not molecular confirmation of this disorder. [1][20][59][web:30032985][75]

## 11. Outcome and prognosis

Available observations chiefly establish **skeletal morbidity**: potentially progressive spinal or lower-limb deformity, toe procedures, and a documented risk of slipped capital femoral epiphysis. The five-person family report states: **“Progressive valgus deformities (at the hips, knees, and ankles) were the main complaints and necessitated orthopedic investigations and surgery.”** Adult affected individuals have been described, but there are **no reliable syndrome-specific survival rates, life-expectancy estimates, mortality rates, disability prevalence, validated prognostic biomarker, or standardized quality-of-life scores**. Severity within a family is not reliably predicted by identifying its allele alone. [53][1][28]

## 12. Treatment and real-world implementation

**Management is individualized orthopedic and supportive care; no drug, gene therapy, RNA therapy, cell therapy, or molecularly targeted treatment has established clinical efficacy for *NPR2* activating-overgrowth ECDM.** These are reports of treatment in individuals, **not comparative efficacy trials**. [53][28][225]

| Intervention | Disease-specific use and evidence | Suggested NCIT clinical-intervention annotation |
|---|---|---|
| Orthopedic surveillance, imaging, and individualized rehabilitation | Follow symptomatic scoliosis, hip position, limb axes, and function during growth; supportive therapy may be tailored to impairment. No syndrome-specific response rate is reported. [1][53] | Use an appropriate verified orthopedic-assessment or physical-therapy term in the local NCIT release; **specific code not verified here**. |
| Great-toe **epiphysiodesis** | Reported at age **8** in the 2020 mother and age **5** in her older daughter; the original family also describes toe-shortening surgery. These observations do not establish an optimal age or success rate. [28][54] | **Epiphysiodesis**—term suggestion; **specific NCIT code not verified**. |
| Guided growth, **osteotomy**, or toe **arthrodesis** | In a five-person family, the two older brothers underwent osteotomies and guided growth for axial deformities and arthrodesis for elongated halluces. [53] | **Osteotomy, NCIT:C51903**; verify release-specific terms for guided growth and arthrodesis. [357] |
| Prompt assessment and stabilization of a **suspected slipped capital femoral epiphysis** | Hip or knee pain or limp merits prompt hip assessment. Stabilization is standard care for an actual slip; it has **not** been evaluated as a syndrome-specific preventive procedure. [1][186] | **Surgical stabilization of slipped femoral epiphysis**—term suggestion; **specific NCIT code not verified**. |
| High-dose estrogen/progestogen for predicted tall adult stature | **Historical individual treatment**, not a recommended syndrome regimen: one affected mother received it at 14–16 years; the report states that it had **little effect on growth**. [225] | **Hormonal therapy**—historical annotation only; **specific NCIT code not verified**. |
| Mutant-receptor inhibition with **TNP-ATP** | **Experimental, cell-based only**: an ATP analogue inhibited several activating mutant receptors in biochemical assays. No patient response or clinical safety data were reported. [305] | **Experimental guanylyl-cyclase inhibition**—no established disease intervention code. |

**Avoid a direction-of-effect error:** vosoritide is a **CNP receptor agonist** studied or used for conditions of **inadequate growth**, including achondroplasia or some *NPR2* **deficiency** trials. Such studies are **not ECDM treatment trials** and do not establish an indication for a receptor that is already overactive. No ECDM-specific NCT efficacy trial was established from the consulted evidence. [176][241]

## 13. Prevention

**Primary prevention by lifestyle change, vaccination, environmental control, or prophylactic medication is not established** for this inherited disorder. Once a familial causal allele is characterized, **genetic counseling and targeted familial testing** can support reproductive decisions and earlier recognition; prenatal or preimplantation testing is technically conditional on knowing the family’s variant and appropriate specialist counseling. **Secondary and tertiary prevention** means recognizing potentially progressive deformity and evaluating new hip/leg pain or limping promptly, then treating complications on their own clinical merits. No population newborn-screening program or validated asymptomatic-population risk score is established. [1][53][186][242]

## 14. Other species and natural disease

The documented naturally affected species is **human, *Homo sapiens* (NCBI Taxon:9606)**. The experimental ortholog is mouse ***Npr2*** (**NCBI Gene:230103; MGI:97372**) in ***Mus musculus* (NCBI Taxon:10090)**. No naturally occurring companion-animal breed or wildlife syndrome equivalent, VBO breed identifier, veterinary prevalence, zoonotic transmission, or infectious cross-species susceptibility was established in the cited material. Similar skeletal responses in humans and engineered mice provide the relevant **comparative biology**, not evidence of animal-to-human transmission. [330][332][270][18]

## 15. Model organisms and research applications

| Model and evidence type | Phenotype recapitulated or finding | Principal limitation and application |
|---|---|---|
| **Col11a2-directed p.Val883Met *Npr2* transgenic mouse** — engineered organism | Increased cartilage cGMP, elongated bones, digits, and vertebrae, enlarged growth plates, and kyphosis; severity differed among founders. [18][54] | **Kyphosis in mice is not identical to human scoliosis.** Useful for testing skeletal causality and growth-plate mechanisms, not a measured human treatment response. [54] |
| **p.Val883Met mutant mouse growth-plate/chondrocyte experiments** — organism plus cellular assays | Thickened hypertrophic zone, BrdU evidence that some hypertrophic cells kept proliferating, and increased CREB phosphorylation and cyclin-D1 expression in experimental cells. The primary study is **PMID:30544148**. [54][73] | Identifies a plausible downstream mechanism; its exact contribution in each human allele has not been directly measured in patient growth plates. |
| **Patient skin fibroblasts** — human ex-vivo model | The 2020 deletion variant showed raised basal and CNP-stimulated cGMP; p.Arg655Cys was also studied in patient fibroblasts. [71][web:24057292] | Fibroblasts can test native receptor function but are **not growth-plate cartilage**. |
| **Transfected HEK-293/293T cells and receptor biochemistry** — in-vitro model | Reproduced ligand-independent and ligand-stimulated activation, enabled variant comparisons, and supported allosteric-mechanism and inhibitor experiments. [18][20][71][305] | Expression and drug effects in a heterologous cell system do not establish clinical efficacy or safety. |

### Selected primary evidence and recent authoritative classification

| Publication date | Source, URL, and PMID | Exact abstract excerpt or principal evidentiary contribution |
|---|---|---|
| **3 August 2012** | Miura *et al.*, *PLoS ONE*. **PMID:22870295**; https://pubmed.ncbi.nlm.nih.gov/22870295/ | “elevated levels of cGMP in growth plates lead to the elongation of long bones.” Foundational family, cell, and mouse evidence. [18] |
| **20 November 2013 online; January 2014 issue** | Miura *et al.*, *American Journal of Medical Genetics A*. **PMID:24259409**; https://pubmed.ncbi.nlm.nih.gov/24259409/ | “A novel missense mutation of NPR2, c.1462G>C (p.Ala488Pro) was found to co-segregate with the phenotype”. [20] |
| **1 April 2019** | Yamamoto *et al.*, *Human Molecular Genetics*. **PMID:30544148**; https://pubmed.ncbi.nlm.nih.gov/?term=CREB+activation+hypertrophic+chondrocytes+Miura+NPR2+Yamamoto | Mutant-mouse and cell study of hypertrophic-zone expansion and CREB/cyclin-D1 signaling. [73] |
| **1 July 2020** | Lauffer *et al.*, *Journal of Clinical Endocrinology & Metabolism*. **PMID:32282051**; https://pubmed.ncbi.nlm.nih.gov/32282051/ | “basal cGMP levels and CNP-stimulated cGMP production were markedly increased compared with controls.” [71] |
| **19 October 2020 online; January 2021 issue** | Kenis *et al.*, *American Journal of Medical Genetics A*. **PMID:33073519**; https://pubmed.ncbi.nlm.nih.gov/33073519/ | Five affected relatives, substantial intrafamilial variability, and documented orthopedic operations. [53] |
| **13 February 2023 online; May 2023 issue** | Unger *et al.*, **2023 skeletal-disorder nosology**, **PMID:36779427**; https://pubmed.ncbi.nlm.nih.gov/36779427/ | Classifies **“Tall stature with long halluces, NPR2-related”** separately from the *NPR3*-related condition. This is authoritative **classification**, not a new patient series. [116][201] |
| **23 November 2023** | Original functional research on *NPR2* **loss-of-function** variants, DOI **10.3389/fcell.2023.1294748**; https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2023.1294748/full | Relevant to interpreting variant **direction of effect**, but **not** primary evidence for new activating ECDM variants. [75] |

**Knowledge-base conclusion:** curate **monoallelic activating *NPR2* → excessive receptor-generated cGMP → abnormal growth-plate activity → skeletal overgrowth** as the supported disease chain. Keep ***NPR3*-related recessive tall stature**, *NPPC*-overexpression phenocopies, and ***NPR2* loss-of-function short stature** as **separate molecular entities**; leave unsupported frequencies, modifiers, molecular therapies, and prognosis fields explicitly **unknown**. [18][20][53][116][web:30032985]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 11 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014401` (1 mention) - the report calls it "MONDO"; MONDO calls it **tall stature-scoliosis-macrodactyly of the great toes syndrome**
- `DOID:0070316` (2 mentions) - the report calls it "Other cross-reference"; DOID calls it **Miura type epiphyseal chondrodysplasia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `OMIM`, `UniProtKB`, `Taxon`, `MGI`.