---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T12:29:38.937969'
end_time: '2026-10-15T12:34:21.743564'
duration_seconds: 282.81
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Myopathy 21 With Early Respiratory Failure
  mondo_id: MONDO:0957224
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
citation_count: 55
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 27
  not_found: 0
  obsolete: 2
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 5
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0051085
    ontology_label: obsolete chaperone cofactor-dependent protein refolding
    replaced_by: GO:0006457
  - term_id: GO:0051082
    ontology_label: obsolete unfolded protein binding
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myopathy 21 With Early Respiratory Failure
- **MONDO ID:** MONDO:0957224 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Myopathy 21 With Early Respiratory Failure** covering all of the
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

# Congenital Myopathy 21 With Early Respiratory Failure  
**Disease knowledge-base research report — evidence reviewed through 15 October 2026**

## Executive summary

**Congenital myopathy 21 with early respiratory failure (CMYO21)** is an ultra-rare, autosomal-recessive protein-aggregate/myofibrillar myopathy caused by **biallelic pathogenic variants in *DNAJB4***. Its defining clinical combination is disproportionate **diaphragmatic/respiratory-muscle weakness**, often producing nocturnal hypoventilation or abrupt hypercapnic respiratory failure, together with **axial rigidity or rigid-spine syndrome**. Limb strength can remain nearly normal despite life-threatening respiratory disease. Onset ranges from infancy to the fifth decade, with J-domain missense variants associated in a small cohort with substantially earlier onset and higher mortality. [54][47]

The principal mechanism is failure of the DNAJB4 HSP40 co-chaperone at the myofibrillar Z-disc. This disrupts HSP70-assisted protein quality control, permits accumulation of myofibrillar/Z-disc proteins, and produces sarcomeric disorganization, protein inclusions, muscle-fiber atrophy and particularly severe diaphragm involvement. This causal interpretation is supported by human genetics, patient tissue, cultured cells, yeast complementation, CRISPR-knockout myotubes and knockout mice. [54]

No disease-modifying treatment is approved. Current practice is proactive respiratory surveillance, bilevel non-invasive ventilation, cough assistance and airway clearance, plus cardiac, swallowing, nutritional, orthopedic and rehabilitation care. Gene replacement is a plausible but preclinical concept, not a clinical intervention. [106][191]

**Evidence limitation:** CMYO21 was defined only in 2022–2023, and published cohorts remain very small. Frequencies and genotype–phenotype associations should therefore be treated as provisional rather than population estimates.

---

## Key evidence sources

| Publication | Date and evidence type | Key contribution | PMID / DOI / URL |
|---|---|---|---|
| Weihl et al., “Loss of function variants in DNAJB4 cause a myopathy with early respiratory failure” | Online 20 October 2022; issue January 2023; primary human, cellular, yeast and mouse study | Established recessive *DNAJB4* myopathy in four patients from three families and demonstrated loss of chaperone function | PMID **36264506**; DOI **10.1007/s00401-022-02510-8**; https://pmc.ncbi.nlm.nih.gov/articles/PMC9812937/ [54] |
| Inoue et al., “Genotype–phenotype correlation in recessive DNAJB4 myopathy” | 28 October 2024; peer-reviewed human cohort plus functional assays | Added seven affected persons/five families, five variants and preliminary genotype–phenotype statistics | PMID **39468638**; DOI **10.1186/s40478-024-01878-w**; https://pmc.ncbi.nlm.nih.gov/articles/PMC11514740/ [47] |
| Al-Kasbi et al., “The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 Middle Eastern families” | 7 November 2022; human WES cohort | First report of homozygous *DNAJB4* p.Arg61Gly in a ventilator-dependent child; subsequently incorporated into the disease spectrum | PMID **36344539**; DOI **10.1038/s41598-022-22036-z**; https://pmc.ncbi.nlm.nih.gov/articles/PMC9640568/ [88] |
| Schoser et al., adult neuromuscular NGS reassessment | Online 21 December 2023; human diagnostic cohort | Independent replication with homozygous c.308del, identified on exome reanalysis | https://pmc.ncbi.nlm.nih.gov/articles/PMC10972933/ [318] |
| Wang et al., congenital-myopathy standard-of-care consensus | 2012; expert consensus | Pulmonary, nutritional, orthopedic and rehabilitation management framework | PMID **22431881**; https://pmc.ncbi.nlm.nih.gov/articles/PMC5234865/ [106][109] |

Two particularly informative abstract statements are:

> “Affected patients presented with axial rigidity and early respiratory failure requiring ventilator support between the 1st and 4th decade of life.” [54]

> “Missense variants in the J-domain may predict a more severe phenotype.” [47]

---

# 1. Disease information

## 1.1 Definition

CMYO21 is a **Mendelian, autosomal-recessive skeletal-muscle chaperonopathy** due to biallelic *DNAJB4* variants. It is characterized primarily by:

- Diaphragmatic weakness and restrictive/hypercapnic respiratory failure;
- Nocturnal hypoventilation or sudden respiratory decompensation;
- Rigid spine, neck stiffness and axial weakness;
- Relatively mild or absent appendicular weakness in many patients;
- Myofibrillar disorganization, protein aggregates and sometimes rimmed vacuoles on biopsy.

The label “congenital” refers to its classification among congenital myopathies, but **symptoms are not necessarily present at birth**: documented onset extends from approximately three months to 45 years. [47][154]

## 1.2 Identifiers and synonyms

| Identifier system | Identifier / name |
|---|---|
| MONDO | **MONDO:0957224**, congenital myopathy 21 with early respiratory failure |
| OMIM phenotype | **620326** |
| MedGen | **C5830424**, UID 1841060 |
| Causal gene OMIM | ***DNAJB4*: 611327** |
| HGNC | ***DNAJB4*: HGNC:14886** |
| NCBI Gene | **11080** |
| Ensembl | **ENSG00000162616** |
| UniProt | **Q9UDY4** |
| Cytogenetic location | **1p31.1** |
| Common abbreviation | **CMYO21** |
| Common alternative descriptions | *DNAJB4*-related myopathy with early respiratory failure; recessive *DNAJB4* myopathy; *DNAJB4*-related rigid-spine myopathy; *DNAJB4* chaperonopathy |
| ICD-10 | No dedicated code; parent congenital-myopathy category **G71.2** is the closest disease-class code |
| ICD-11 | No dedicated code; congenital myopathies **8C72** |
| MeSH | No disease-specific descriptor identified; broader descriptors include congenital myopathies and muscle diseases |
| Orphanet | No clearly established disease-specific recessive CMYO21 record was located. **ORPHA:97245** is the parent “congenital myopathy” group. ORPHA:700170 refers instead to *DNAJB4*-related **dominant distal myopathy**, a distinct allelic disorder. |

The MONDO, OMIM, MedGen and gene-location assignments are reported in MedGen and OMIM. [1][144] The parent Orphanet/ICD mappings are ORPHA:97245, ICD-10 G71.2 and ICD-11 8C72. [149]

## 1.3 Data provenance

This report is **aggregated disease-level evidence**, not an extraction from a single EHR. It synthesizes:

- Published individual-patient and pedigree data;
- Disease resources such as OMIM, MedGen, MONDO and ClinVar;
- Cohort-level functional experiments;
- General congenital-myopathy care guidance.

Because cohorts are tiny, much of the phenotype evidence ultimately traces to identifiable case-series participants rather than registry-scale epidemiology.

---

# 2. Etiology

## 2.1 Causal factor

The primary cause is **biallelic germline pathogenic or likely pathogenic variation in *DNAJB4***, encoding DNAJ/HSP40 family member B4. The disease mechanism is predominantly **loss of function**:

- Truncating variants produce absent or rapidly degraded protein;
- p.Leu262Ser destabilizes the protein;
- J-domain variants such as p.Arg25Gln, p.Lys35Asn and p.Arg61Gly can be stable but functionally defective in chaperone assays. [54][47]

No infectious, toxic, nutritional or environmental cause is established.

## 2.2 Risk factors

### Genetic

- Homozygosity or compound heterozygosity for deleterious *DNAJB4* alleles;
- Parental consanguinity, which increases the probability of homozygosity for rare recessive alleles;
- Positive family history of compatible respiratory/rigid-spine myopathy;
- Preliminary evidence suggests **J-domain missense variants** confer more severe disease than truncating or C-terminal variants: median onset 0.5 versus 28 years and mortality 75% versus 14% in the small comparison, respectively. [47]

### Environmental and acquired

No environmental exposure is known to cause CMYO21. Respiratory infections, aspiration, surgery, anesthesia or sedative medications may **precipitate decompensation in someone who already has respiratory-muscle weakness**, but they are complications or stressors, not proven etiologic factors.

Age is not a causal risk factor, although expression is age-dependent in adult-onset cases. No credible sex-specific biological risk has been established; the male predominance in one recent series—six males and one female—is likely vulnerable to ascertainment and family-size effects. [47]

## 2.3 Protective factors

No protective allele, modifier gene, diet or lifestyle exposure has been demonstrated. Potentially protective clinical practices include early detection of nocturnal hypoventilation, vaccination, infection avoidance, cough augmentation and timely ventilation, but these prevent complications rather than prevent the genotype or underlying myopathy.

## 2.4 Gene–environment interactions

No formal gene–environment interaction study exists. Heat-shock experiments showed that mutant DNAJB4 impaired clearance of TDP-43 aggregates and protection from heat-induced cell death, suggesting that cellular proteotoxic stress can expose deficient chaperone reserve. Extrapolation from this in-vitro result to environmental heat exposure in patients is **not established**. [54]

---

# 3. Phenotypes

## 3.1 Phenotype summary and suggested HPO annotations

Frequencies below refer where possible to the seven affected individuals in the 2024 cohort, not to a population registry. Patient ascertainment specifically for early respiratory disease inflates respiratory-feature frequencies.

| Phenotype type | Manifestation and suggested HPO term | Onset, severity and progression | Observed frequency/evidence | Functional and quality-of-life effect |
|---|---|---|---|---|
| Clinical sign | **Respiratory failure — HP:0002878** | Infancy to adulthood; often severe, progressive or abrupt; generally hypercapnic | 6/7 developed failure in the 2024 cohort; the seventh was lost to follow-up at age two. All four foundational patients developed failure. [47][54] | Hospitalization, syncope/arrest, long-term ventilation, tracheostomy and death |
| Clinical sign | **Diaphragmatic weakness — HP:0009113** | May be isolated or disproportionate to limb weakness; chronic/progressive | Defining feature in the original four cases; adult FVC was 38% and pCO₂ 70 mmHg in one patient. [54] | Orthopnea/dyspnea, impaired sleep, dependence on assisted ventilation |
| Physiologic abnormality | **Nocturnal hypoventilation — HP:0002877**; hypercapnia | Often precedes daytime or acute respiratory failure | Documented in an adult before syncope and respiratory failure; likely underdetected without CO₂ monitoring. [54] | Morning symptoms, sleep fragmentation, daytime fatigue and sudden decompensation risk |
| Symptom | **Dyspnea — HP:0002094** | Variable; may appear acutely in adults | Both Spanish adult cases presented with dyspnea/hypercapnic insufficiency. [54] | Exercise and sleep limitation |
| Musculoskeletal sign | **Spinal rigidity — HP:0003306** | Infancy or adulthood; persistent/progressive | 3/7 in the 2024 cohort and 3/4 foundational patients | Reduced neck/trunk flexion, dressing and mobility difficulties; worsens chest-wall restriction |
| Musculoskeletal sign | **Axial muscle weakness — HP:0003327** | Early or adult; often exceeds appendicular weakness | Common component of rigid-spine presentation | Impaired posture, head control and chest expansion |
| Musculoskeletal sign | Neck stiffness / limited cervical motion | Usually infancy in severe J-domain disease | 3/7 in 2024 series | Difficulty turning or bending the head |
| Musculoskeletal sign | **Scoliosis — HP:0002650** | Congenital or progressive childhood/adolescent | 3/7 in 2024 cohort | Further restrictive physiology, seating and pain burden |
| Musculoskeletal sign | Ankle/joint contractures — **HP:0001371** | Childhood, generally progressive | 3/7 in 2024 cohort | Reduced range of motion and walking efficiency |
| Symptom/sign | Limb weakness — **HP:0001324**; distal weakness HP:0002460 or proximal weakness HP:0003701 | Often absent or mild; can be adult progressive | Pronounced in only two of seven recent patients—one distal, one proximal | Gait and hand-function limitations when present |
| Feeding sign | **Dysphagia — HP:0002015** | Severe pediatric form; chronic | 3/7; all three required nasogastric or gastrostomy feeding. [47] | Aspiration, malnutrition and caregiver burden |
| Infectious complication | Recurrent lower respiratory infection — **HP:0002783** | Usually secondary to weak cough/dysphagia | 4/7 in 2024 cohort | Admissions, antibiotic use and accelerated respiratory decline |
| Cardiac sign | **Hypertrophic cardiomyopathy — HP:0001639** | Variable; not universal | Two recent patients plus one original patient; mitral insufficiency occurred in another | Arrhythmia/heart-failure surveillance and treatment burden |
| Laboratory abnormality | Elevated CK — **HP:0003236** | Normal to mildly/moderately elevated; nonspecific | Original range normal to 500–700 U/L; recent cohort mostly normal, one 1,226 U/L | Diagnostic clue only; not a severity biomarker |
| Electrophysiology | **Myopathic EMG — HP:0003458** | Short-duration, low-amplitude, polyphasic units and early recruitment | Present in most tested cases but not obligatory | Supports muscle rather than neuropathic localization |
| Pathology | **Rimmed vacuoles — HP:0003805**; fiber-size variation, angular fibers, inclusions | Variable between muscles and disease stages | Rimmed vacuoles and inclusions occurred in the foundational biopsies; inclusions were not evident in limited recent samples. [54][47] | Diagnostic tissue evidence; not directly patient-reported |
| Imaging | Selective hamstring involvement | Semitendinosus/biceps femoris in initial study; semimembranosus and adductor longus in later cases | Reproduced across small independent cohorts | Can direct biopsy and support differential diagnosis |
| Neurologic/imaging | Brain atrophy or thin corpus callosum | Rare; uncertain direct causality | Frontal atrophy in one patient; thin corpus callosum/mild atrophy in another | Potential neurodevelopmental burden, but cognition was generally normal |
| Developmental | Developmental/intellectual impairment | Rare and attribution uncertain | Reported in the original p.Arg61Gly candidate-gene family; not apparent in the 2024 cohort | May require developmental support, but is not a core phenotype |
| Other | Inguinal hernia, fetal growth restriction, lipoid pneumonia | Isolated reports | Seen in the p.Arg61Gly family | Case-specific burden; insufficient evidence for core annotation |

Established HPO identifiers for spinal rigidity, diaphragmatic weakness and respiratory failure are HP:0003306, HP:0009113 and HP:0002878. [284] Axial weakness is HP:0003327. [273]

## 3.2 Negative or uncommon findings

Several affected persons retained normal gait, limb strength, motor milestones, facial movement, ocular movement, bulbar function and cognition despite severe respiratory disease. Absence of conspicuous appendicular weakness therefore **does not exclude CMYO21**. [54]

No disease-specific EQ-5D, SF-36, PROMIS or other formal quality-of-life study has been published. Expected major burdens are ventilator dependence, restricted spine movement, repeated respiratory admission, feeding-tube dependence and caregiver requirements.

---

# 4. Genetic and molecular information

## 4.1 Causal gene

| Field | Information |
|---|---|
| Gene | ***DNAJB4*** |
| Full name | DnaJ heat shock protein family (Hsp40) member B4 |
| HGNC | HGNC:14886 |
| NCBI Gene | 11080 |
| OMIM gene | 611327 |
| Ensembl | ENSG00000162616 |
| UniProt | Q9UDY4 |
| Locus | 1p31.1; GRCh38 approximately chr1:77,979,175–78,017,964 |
| Disease inheritance | Autosomal recessive for CMYO21 |
| Protein role | HSP40/DNAJ co-chaperone; client recognition and recruitment to HSP70, stimulating HSP70 ATPase activity and protein folding/triage |
| Important localization | Cytosol and skeletal-muscle Z-disc |

NCBI lists ATPase-activator activity and Z-disc localization for DNAJB4. [91] OMIM places CMYO21 at 1p31.1 with recessive inheritance. [144]

## 4.2 Reported recessive disease variants

Reference transcript: **NM_007034.5**.

| Variant | Class/domain | Population evidence | Clinical/functional interpretation |
|---|---|---|---|
| c.74G>A, p.Arg25Gln | Missense, J-domain | Absent from gnomAD in foundational report | ClinVar pathogenic; stable and Z-disc-localized but failed yeast complementation, TDP-43 disaggregation and heat-stress protection |
| c.105G>C, p.Lys35Asn | Missense, J-domain | gnomAD v4 AF **0.000003181**, no homozygotes | Called pathogenic by 2024 authors; increased stability but loss of function in yeast/disaggregation assays |
| c.181A>G, p.Arg61Gly | Missense, J-domain | Absent from gnomAD | ClinVar pathogenic; segregated recessively; normal stability but defective functional assays |
| c.308del, p.Gly103GlufsTer25 | Frameshift | Rare; no population homozygotes reported | Pathogenic homozygous variant identified on exome reanalysis in an adult with diaphragmatic respiratory failure |
| c.547C>T, p.Arg183Ter | Nonsense | gnomAD v4 AF **0.000008893**, no homozygotes | Pathogenic in 2024 study; rapidly degraded |
| c.775C>T, p.Arg259Ter | Nonsense | gnomAD v4 AF **0.000002813**, no homozygotes | Pathogenic in 2024 study; rapidly degraded |
| c.785T>C, p.Leu262Ser | Missense, C-terminal substrate-binding region | Absent from gnomAD in foundational report | ClinVar pathogenic; unstable and rapidly degraded |
| c.856A>T, p.Lys286Ter | Nonsense, last exon/C-terminal region | Absent from gnomAD in foundational report | ClinVar pathogenic; truncated protein absent/rapidly degraded |
| Exon 2 deletion, hg38 chr1:78,013,051–78,013,619 | Exonic structural deletion | Absent from gnomAD; no homozygotes | Pathogenic loss-of-function allele in adult-onset disease |

Four variants—p.Lys286Ter, p.Leu262Ser, p.Arg25Gln and p.Arg61Gly—had disease-specific ClinVar pathogenic records in the retrieved dataset. [166] The 2024 cohort reported the remaining variants as pathogenic but did not give variant-specific formal ACMG evidence codes. Frequencies and functional results are from that peer-reviewed study. [47]

All disease-causing variants are **constitutional/germline**, not somatic.

### Important allelic distinction

Heterozygous ***DNAJB4* c.270T>A, p.Phe90Leu** causes a separate **autosomal-dominant distal myopathy**, not recessive CMYO21. It produces late-onset hand/distal weakness with protein inclusions and later respiratory involvement. [90] It should not be merged into the CMYO21 variant set.

## 4.3 Functional consequence

The best-supported overarching mechanism is **loss of DNAJB4 co-chaperone function**. A purely haploinsufficient mechanism is unlikely for CMYO21 because heterozygous carriers are clinically unaffected. Stable J-domain mutants may also acquire abnormal interactions with HSP70, but a toxic component remains speculative. [47]

## 4.4 Modifier genes, epigenetics and chromosomal abnormalities

- **Modifier genes:** none established.
- **Protective alleles:** none established.
- **Disease-specific epigenetic signature:** none reported.
- **Large cytogenetic abnormality:** no recurrent aneuploidy, translocation or inversion is associated.
- A homozygous single-exon deletion is known, so exon-level CNV analysis is diagnostically relevant.
- No pathogenic repeat expansion or mitochondrial-DNA mechanism is known.

---

# 5. Environmental information

| Category | Current evidence |
|---|---|
| Toxins, radiation, pollution or occupational exposures | No causal association |
| Smoking or alcohol | No CMYO21-specific association; smoking would reasonably reduce respiratory reserve but has not been studied |
| Diet | No preventive or causal diet identified |
| Exercise | No evidence that exercise prevents disease. Individually prescribed submaximal activity may preserve function; exhaustive exercise has not been evaluated |
| Infection | No pathogen causes CMYO21. Respiratory infection can cause acute deterioration because cough and ventilation are weak |
| Aspiration | Secondary to dysphagia; contributes to pneumonia rather than primary disease |
| Heat/proteotoxic stress | Mutant cells perform poorly under experimental heat shock, but a clinical environmental interaction is unproven |

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Biallelic pathogenic *DNAJB4* variation leads to** absent, unstable or functionally defective DNAJB4 co-chaperone in skeletal myofibers.  
2. **Defective DNAJB4 leads to** impaired recognition/handling of unfolded or damaged client proteins and impaired recruitment of those clients to HSP70 at or near the myofibrillar Z-disc.  
3. **Impaired DNAJB4–HSP70 proteostasis leads to** deficient protein refolding/disaggregation and accumulation of client, Z-disc and stress-chaperone proteins; the exact disease-driving client proteins remain incompletely identified.  
4. **Protein accumulation leads to** desmin-, myotilin- and related protein-positive inclusions, insoluble aggregates, Z-disc streaming and sarcomeric/myofibrillar disorganization.  
5. **Myofibrillar disruption leads to** reduced muscle-fiber integrity, fiber-size variation, angular/atrophic fibers, core-like areas, occasional rimmed vacuoles and progressive loss of contractile capacity.  
6. **Preferential injury or limited reserve in diaphragm and axial muscles leads to** diaphragmatic weakness, reduced chest expansion, axial weakness, neck stiffness and rigid spine. Why the diaphragm is disproportionately affected is strongly demonstrated phenotypically but mechanistically **inferred**, not fully resolved.  
7. **Diaphragm/chest-wall weakness leads to** reduced tidal volume, restrictive ventilatory physiology and sleep-first alveolar hypoventilation.  
8. **Progressive hypoventilation leads to** hypercapnia, dyspnea, morning/sleep symptoms and eventually acute or chronic respiratory failure, ventilator dependence or death.  
9. **Branch A: axial weakness and contracture lead to** scoliosis and further mechanical restriction, which can compound respiratory failure.  
10. **Branch B: bulbar weakness/dysphagia leads to** aspiration, recurrent lower respiratory infection and feeding-tube dependence.  
11. **Branch C: cardiac-muscle involvement in a subset leads to** hypertrophic cardiomyopathy or valvular dysfunction; this branch is clinically observed, but the precise cardiomyocyte mechanism is not specifically demonstrated.

## 6.2 Molecular and cellular detail

DNAJB4 is a type-II DNAJ/HSP40 co-chaperone. DNAJ proteins bind selected clients and stimulate HSP70 ATP hydrolysis, thereby promoting folding, disaggregation or degradation. In muscle, wild-type DNAJB4 co-localizes with α-actinin at the Z-disc. [54][95]

### Human evidence

Patient muscle showed:

- Loss or marked reduction of DNAJB4;
- Z-disc streaming and sarcomeric disorganization;
- Dense granulofilamentous material;
- Desmin- and myotilin-positive inclusions;
- Fiber atrophy and occasional rimmed vacuoles.

The p.Lys286Ter and p.Leu262Ser proteins were rapidly degraded. p.Arg25Gln retained Z-disc localization but failed functional tests, separating **localization** from **chaperone competence**. [54]

### In-vitro evidence

CRISPR *Dnajb4*-knockout C2C12 cells differentiated into myotubes but showed:

- Increased myoblast fusion/myonuclei per myotube;
- Increased desmin and α-actinin;
- Insoluble DNAJB6, CRYAB and desmin;
- Desmin, actin and myotilin aggregates.

HeLa-cell heat-shock assays showed persistent nuclear TDP-43 aggregates with disease variants. TDP-43 was an experimental client/readout; it is **not yet proven to be the principal human muscle disease substrate**. [54][47]

### Model-organism evidence

*Dnajb4*-null mice developed kyphosis, reduced hanging-grid endurance, lower hindlimb muscle weights, diaphragm thinning and marked diaphragm-fiber atrophy. Knockout muscle accumulated desmin, myotilin, α-actinin, HSPA1 and CRYAB. [54]

### Pathways and processes

No canonical oncogenic-style pathway such as Wnt, MAPK or PI3K–AKT has been shown to drive CMYO21. The central pathway is the **DNAJ–HSP70 proteostasis network**.

Suggested ontology annotations:

| Category | Suggested ontology term |
|---|---|
| Biological process | GO:0006457 — protein folding |
| Biological process | GO:0051085 — chaperone cofactor-dependent protein refolding |
| Biological process | Response to unfolded protein |
| Biological process | Protein disaggregation |
| Biological process | Sarcomere organization / myofibril organization |
| Molecular function | GO:0031072 — heat-shock-protein binding |
| Molecular function | GO:0051082 — unfolded-protein binding |
| Molecular function | ATPase-activator activity |
| Cellular component | Z-disc |
| Cellular component | Myofibril / sarcomere |
| Cellular component | Cytosol |
| Cell type | CL:0000188 — cell of skeletal muscle |
| Cell type | CL:0000594 — skeletal muscle fiber |
| Experimental cell | CL:0000515 — skeletal muscle myoblast |
| Experimental cell | CL:0002372 — myotube |
| Probable secondary cell | Cardiomyocyte |

GO:0006457 denotes protein folding and GO:0051085 cofactor-dependent protein refolding. [252][254] Relevant cell-ontology identifiers include skeletal-muscle myoblast CL:0000515 and myotube CL:0002372. [241]

## 6.3 Metabolism, immunity and tissue injury

- No reproducible metabolomic or lipidomic disease signature exists.
- Core-like regions and diminished oxidative-enzyme staining occur, but there is no established primary mitochondrial enzyme deficiency.
- No primary autoimmune or inflammatory mechanism has been demonstrated.
- Rare necrotic fibers, fibrosis and fatty replacement are downstream tissue injury, not the initiating lesion.
- Autophagic involvement is suggested by rimmed vacuoles/protein aggregates, but a disease-specific autophagy defect has not been proven.

## 6.4 Molecular profiling and advanced technologies

| Technology | Disease-specific findings |
|---|---|
| Exome sequencing | Main discovery and diagnostic technology |
| Genome sequencing | No published CMYO21-specific systematic cohort; useful for unresolved CNVs/intronic variants |
| RNA sequencing | No CMYO21-specific diagnostic series or transcriptomic signature |
| Proteomics | No unbiased human proteomic dataset; targeted immunoblotting showed changes in Z-disc and chaperone proteins |
| Metabolomics/lipidomics | No disease-specific data |
| Single-cell or spatial transcriptomics | None reported |
| CRISPR screen | No genome-wide screen; CRISPR was used to generate C2C12 knockout cells and knockout mice |
| Multi-omics | None reported |

In broader neuromuscular diagnostics, integrated genome/RNA/protein analysis increased family-level diagnostic yield from approximately 40% to over 60%, but this is general evidence rather than a CMYO21-specific validation. [301]

---

# 7. Anatomical structures affected

| Level | Structure and suggested ontology | Evidence |
|---|---|---|
| Primary organ | Skeletal muscle — UBERON:0001134 / general skeletal-muscle tissue UBERON:0002036 | Primary disease tissue |
| Primary muscle | **Diaphragm — UBERON:0001103** | Disproportionate clinical weakness and severe knockout-mouse atrophy [245] |
| Axial sites | Paraspinal, neck and chest-wall musculature | Rigid spine, neck stiffness and limited chest expansion |
| Limb muscles | Semitendinosus, biceps femoris; semimembranosus and adductor longus; sometimes soleus and gluteus maximus | Selective MRI/CT abnormalities [321] |
| Secondary respiratory organs | Lungs/airways | Structurally secondary; affected by hypoventilation, weak cough, pneumonia and aspiration |
| Secondary skeleton | Vertebral column | Rigidity, kyphosis and scoliosis |
| Secondary cardiac site | Myocardium and mitral valve apparatus | HCM or mitral insufficiency in a subset |
| Tissue | Striated skeletal-muscle tissue | Fiber atrophy, fibrosis, fatty replacement and aggregates |
| Cell | Multinucleated skeletal myofiber | Principal target |
| Subcellular | Z-disc, sarcomere, myofibril and cytosol | DNAJB4 localization and aggregate pathology |
| Lateralization | Generally bilateral/systemic | No consistent unilateral pattern; selective muscles can be asymmetrically affected, but this is not defining |

---

# 8. Temporal development

## 8.1 Onset patterns

Two provisional clinical patterns emerge:

1. **Infantile/childhood pattern:** neck stiffness or respiratory disease in the first year, followed by rigid spine, contractures, dysphagia and severe respiratory failure. This is enriched for J-domain missense variants.
2. **Adult pattern:** insidious weight loss or mild weakness followed by abrupt dyspnea, syncope, respiratory arrest or hypercapnic failure, sometimes with little limb weakness.

Reported first symptoms range from approximately **three months to 45 years**. [47]

## 8.2 Progression

- Chronic, lifelong and generally progressive;
- No established relapsing-remitting course;
- Respiratory symptoms may appear suddenly after a clinically silent period;
- Infantile J-domain disease can progress to death before adulthood;
- Adult cases may remain ambulant while requiring nocturnal ventilation;
- No spontaneous molecular remission is reported.

Practical stages are:

1. **Presymptomatic/genetic stage**;
2. **Early axial or sleep-related stage**—neck stiffness, reduced chest expansion or nocturnal symptoms;
3. **Established respiratory stage**—reduced FVC, nocturnal hypercapnia, recurrent infection;
4. **Advanced stage**—daytime hypercapnia, prolonged ventilation, tracheostomy, dysphagia and cardiopulmonary complications.

The key intervention window is **before daytime respiratory failure**, when sleep CO₂ abnormalities, supine FVC decline or weak cough may first be detectable.

---

# 9. Inheritance and population

## 9.1 Inheritance

- **Autosomal recessive**;
- Parents of affected persons are usually clinically unaffected heterozygotes;
- For two confirmed carrier parents, each pregnancy has a theoretical:
  - 25% affected risk;
  - 50% carrier risk;
  - 25% non-carrier/unaffected probability.
- Penetrance for clearly pathogenic **biallelic** genotypes appears high but has not been quantified.
- Expressivity is markedly variable, from infantile fatal respiratory disease to adult-onset respiratory failure.
- No genetic anticipation is established.
- Germline mosaicism has not been reported but cannot be excluded as a general counseling consideration.
- Consanguinity is prominent in severe pediatric families, although unrelated non-consanguineous Spanish patients demonstrate that it is not required. [54][47]

## 9.2 Epidemiology

No population prevalence, birth prevalence or annual incidence has been calculated for CMYO21. Published evidence through 2024 comprised only a small number of families, so it is appropriately considered **ultra-rare**.

For context—not a CMYO21 estimate—the pooled prevalence of all congenital myopathies was 1.62 per 100,000 overall and 2.76 per 100,000 children in a systematic review. [151]

No founder variant is established. Families have been reported from Spain, Saudi Arabia, Oman, Turkey, Colombia and an adult European diagnostic cohort, arguing for broad geographic distribution. [47][54]

Carrier frequency cannot be reliably computed from current data. All individually enumerated pathogenic alleles are absent or extremely rare in gnomAD and were not observed homozygously in population controls. [47]

## 9.3 Demographics

- Both sexes are affected.
- No valid male:female ratio can be inferred.
- Age distribution spans infancy through at least the seventh decade.
- No ethnicity-specific susceptibility is established beyond ascertainment in consanguineous populations.

---

# 10. Diagnostics

## 10.1 When to suspect CMYO21

Strong diagnostic clues are:

- Unexplained hypercapnic or restrictive respiratory failure;
- Diaphragm weakness out of proportion to limb weakness;
- Infantile neck stiffness or rigid-spine syndrome;
- Preserved ambulation despite severe respiratory impairment;
- Normal or mildly increased CK;
- Selective hamstring abnormalities on muscle MRI;
- Myofibrillar protein inclusions, Z-disc streaming or rimmed vacuoles;
- Recessive family history or consanguinity.

The 2024 authors specifically recommend considering *DNAJB4* when an infant has neck stiffness or an adult develops respiratory failure without prominent limb weakness. [188]

## 10.2 Clinical investigations

| Investigation | Expected/useful finding |
|---|---|
| Upright and supine spirometry | Reduced FVC; a disproportionate supine decline supports diaphragm weakness |
| Maximal inspiratory/expiratory pressures | Reduced respiratory-muscle strength |
| Peak cough flow | Detects inadequate cough and need for cough assistance |
| Overnight oximetry **with CO₂ measurement** | Sleep-related hypoventilation; oximetry alone may miss hypercapnia |
| Polysomnography | Distinguishes hypoventilation from obstructive apnea |
| Arterial/capillary blood gas | Elevated pCO₂; one index adult had pCO₂ 70 mmHg |
| Serum bicarbonate | Chronic CO₂-retention clue |
| CK | Often normal or mildly elevated; occasionally about 1,200 U/L |
| ECG and echocardiogram | HCM, valvular disease or rhythm complications |
| Swallow study | Dysphagia and aspiration |
| EMG/NCS | Myopathic motor units; nerve conduction usually not the primary abnormality |
| Muscle MRI | Selective posterior-thigh/hamstring involvement |
| Muscle biopsy | Fiber-size variation, angular fibers, fibrosis, fatty replacement, rubbed-out/core-like regions, aggregates, Z-disc disruption and occasional rimmed vacuoles |
| Electron microscopy | Z-disc streaming and granulofilamentous material |

## 10.3 Genetic-testing strategy

1. **First line:** a comprehensive congenital-myopathy, rigid-spine or neuromuscular panel that includes *DNAJB4* and exon-level deletion/duplication analysis.
2. **Alternative first line:** trio WES or genome sequencing, especially with atypical, multisystem or nonspecific respiratory presentations.
3. **Confirmatory testing:** Sanger confirmation and parental segregation for SNVs/indels; orthogonal CNV confirmation for exon deletion.
4. **If negative:** reanalyse exome data as gene–disease knowledge evolves. The c.308del diagnosis was found through reanalysis after the *DNAJB4* association became known. [318]
5. **If still unresolved:** WGS for structural/deep-intronic variants and muscle/fibroblast RNA studies for aberrant splicing or expression.
6. **Single-gene testing:** reasonable in a highly specific phenotype or known familial variant.
7. **CMA/karyotype/FISH:** low yield for isolated CMYO21; CMA may identify broad CNVs but is not the preferred test for small *DNAJB4* variants.
8. **Mitochondrial DNA and repeat-expansion testing:** not CMYO21 tests; use only when the differential suggests another disease.

*DNAJB4* is a green/high-evidence gene on the NHS congenital-myopathy panel, which uses WES or medium-panel testing with exon-level CNV analysis. [288][296]

## 10.4 Diagnostic criteria

No validated scoring system or formal society criteria exist. A molecular diagnosis requires:

- A compatible phenotype;
- Two pathogenic/likely pathogenic *DNAJB4* alleles in trans or a confirmed homozygous allele;
- Appropriate segregation;
- Exclusion of the separate dominant p.Phe90Leu distal-myopathy phenotype.

A VUS should not be considered diagnostic without segregation, population, functional and phenotype evidence.

## 10.5 Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| *SELENON*-related rigid-spine muscular dystrophy/multiminicore disease | Similar axial rigidity and disproportionate respiratory weakness; test *SELENON* and assess characteristic pathology |
| *TTN*-related hereditary myopathy with early respiratory failure | Usually dominant/adult, often distal weakness; cytoplasmic bodies and *TTN* A-band variants |
| Late-onset Pompe disease | Acid α-glucosidase deficiency; elevated biomarkers and enzyme assay; treatable |
| Nemaline myopathy, including *NEB*, *ACTA1*, *TNNT1* | Nemaline rods and gene-specific pattern |
| Myofibrillar myopathies—*DES*, *CRYAB*, *FLNC*, *BAG3*, *FHL1* | Overlapping aggregates and hamstring MRI; often different inheritance and cardiac/neuropathic patterns |
| Congenital muscular dystrophy due to *LMNA* or *LAMA2* | Dystrophic biopsy, contractures and gene-specific imaging |
| Spinal muscular atrophy | Neurogenic EMG, areflexia and *SMN1* testing |
| Congenital myasthenic syndrome | Fatigability, decrement and neuromuscular-junction gene findings |
| Congenital myotonic dystrophy | Maternal myotonia and DMPK expansion |
| Mitochondrial myopathy | Multisystem features, lactate/respiratory-chain or mtDNA findings |
| Dominant *DNAJB4* distal myopathy | Heterozygous p.Phe90Leu, distal hand onset, later respiratory disease |

These pediatric and adult differentials are explicitly discussed in the 2023 and 2024 primary studies. [316][321]

## 10.6 Screening

- No population or newborn screening program exists.
- **Cascade genetic testing** is appropriate for adult relatives after a familial variant is identified.
- Test symptomatic relatives promptly even when limb strength is normal.
- Asymptomatic biallelic relatives should receive baseline pulmonary, sleep, cardiac and swallowing assessment.
- Carrier testing is appropriate for reproductive partners in families where the familial allele is known.

---

# 11. Outcome and prognosis

## 11.1 Survival and mortality

No valid five-year, ten-year or median-survival estimate exists. Outcomes range from preserved ambulation into adulthood to death in infancy or childhood from respiratory disease.

In the small genotype comparison:

- J-domain variants: **75% mortality**;
- Other variants: **14% mortality**;
- *P* = 0.046.

The corresponding onset ages were 0.5 versus 28 years, *P* = 0.035. These are hypothesis-generating results from very small groups, not stable prognostic percentages. [47]

Documented severe outcomes include:

- Death at 11 months;
- Death at ages seven, nine and 11 years;
- Tracheostomy and near-continuous ventilation;
- Adult respiratory arrest and syncope;
- Long-term nocturnal non-invasive ventilation.

## 11.2 Morbidity

Major morbidity arises from:

- Chronic ventilatory insufficiency;
- Recurrent pneumonia and weak secretion clearance;
- Dysphagia, aspiration and feeding-tube dependence;
- Rigid spine, scoliosis and contractures;
- Cardiomyopathy in a subset;
- Reduced independence and caregiver burden.

No standardized disease-specific quality-of-life instrument has been validated.

## 11.3 Prognostic factors

Probable adverse factors are:

- J-domain missense genotype;
- Infantile onset;
- Early neck stiffness or rigid spine;
- Declining FVC, especially supine;
- Sleep or daytime hypercapnia;
- Recurrent lower respiratory infection;
- Dysphagia/aspiration;
- Cardiac involvement.

No molecular or circulating prognostic biomarker has been validated. CK does not reliably track severity.

Recovery of lost muscle function is not documented. Ventilation can correct hypoventilation and substantially improve safety and symptoms, but it does not reverse the underlying chaperonopathy.

---

# 12. Treatment

## 12.1 Current strategy

There is **no approved disease-modifying pharmacotherapy, gene therapy, RNA therapy or cell therapy for CMYO21**. Treatment is supportive and should be coordinated by neuromuscular, respiratory, cardiology, nutrition/swallowing, rehabilitation and orthopedic teams. A 2025 mechanistic review confirmed that no mechanism-based therapy is approved for any J-domain-protein myopathy. [191]

## 12.2 Interventions

| Intervention | Indication and practical role | Suggested NCIT-style intervention term |
|---|---|---|
| Bilevel non-invasive positive-pressure ventilation with backup rate | Nocturnal hypoventilation, hypercapnia or respiratory-muscle failure; preferred to CPAP because CPAP does not provide ventilation | Noninvasive Positive Pressure Ventilation |
| Invasive mechanical ventilation/tracheostomy | Severe acute failure, inability to protect airway or inadequate NIV | Mechanical Ventilation; Tracheostomy |
| Mechanical insufflation–exsufflation and assisted cough | Low peak cough flow, secretion retention or respiratory infection | Cough Assist Therapy; Airway Clearance Therapy |
| Chest physiotherapy/suction | Mobilization and removal of secretions | Respiratory Therapy |
| Prompt antibiotics for bacterial infection | Pneumonia or other bacterial respiratory infection; not chronic disease modification | Antibiotic Therapy |
| Swallow evaluation and feeding modification | Dysphagia or aspiration risk | Swallowing Therapy; Nutritional Support |
| Nasogastric or gastrostomy feeding | Unsafe swallow, aspiration or inadequate nutrition | Enteral Nutrition; Gastrostomy |
| Physical and occupational therapy | Preserve range, function and participation; prevent secondary contractures | Physical Therapy; Occupational Therapy |
| Stretching, orthoses and seating support | Contracture and scoliosis management | Orthopedic Device; Rehabilitation Therapy |
| Scoliosis surgery | Selected progressive deformity after respiratory/anesthetic planning | Spinal Fusion |
| Cardiomyopathy-directed medication | HCM, mitral disease, arrhythmia or heart failure according to cardiology standards | Cardiovascular Therapy |
| Vaccination | Reduce respiratory infectious complications | Vaccination |

Congenital-myopathy consensus guidance recommends at least annual spirometry, inspiratory/expiratory pressures, peak cough flow and oximetry in low-risk patients, with more frequent testing in high-risk patients. Bilevel ventilation is recommended for hypoventilation, while CPAP alone is insufficient. [106]

### Practical respiratory algorithm

1. Obtain sitting and supine spirometry, inspiratory/expiratory pressures and peak cough flow.
2. Perform overnight oximetry with transcutaneous or end-tidal CO₂, or full polysomnography.
3. Start nocturnal bilevel ventilation when hypoventilation/hypercapnia or clinically significant respiratory-muscle weakness appears.
4. Add cough augmentation and secretion clearance early.
5. During infection, increase airway clearance and ventilation and avoid treating hypoventilation with oxygen alone.
6. Escalate to invasive support for severe failure or when NIV cannot maintain ventilation/airway protection.

## 12.3 Pharmacotherapy and pharmacogenomics

No drug has demonstrated a CMYO21-specific response rate. Bronchodilators, antibiotics, analgesics and cardiology medications should be used for standard indications, not as treatment of DNAJB4 deficiency.

No CMYO21-specific CPIC, PharmGKB or FDA pharmacogenomic guidance exists.

## 12.4 Experimental treatment

Conceptual strategies include:

- AAV-mediated **DNAJB4 gene replacement** for recessive loss of function;
- Enhancement of HSP70/proteostasis capacity;
- Substrate reduction for aggregation-prone clients;
- Manipulation of DNAJ–HSP70 interactions.

Gene replacement remains preclinical and faces skeletal-muscle/diaphragm delivery, immune and durability challenges. [191] No CMYO21-specific interventional ClinicalTrials.gov study or NCT identifier was found.

---

# 13. Prevention

## 13.1 Primary prevention

The genotype cannot be prevented by lifestyle change or vaccination. Reproductive options after identifying familial variants include:

- Preconception carrier testing;
- Partner testing;
- Prenatal diagnosis by chorionic-villus sampling or amniocentesis;
- IVF with preimplantation genetic testing for monogenic disease;
- Donor gametes or other family-planning options.

## 13.2 Secondary prevention

- Cascade testing of siblings and relatives;
- Pulmonary and sleep evaluation before symptoms;
- Early echocardiography and swallow assessment;
- Periodic reanalysis of negative genomic results in strongly suggestive families;
- Early institution of ventilation before daytime respiratory failure.

## 13.3 Tertiary prevention

- NIV and cough assistance to reduce hypoventilation and secretion retention;
- Vaccination against influenza, COVID-19 and pneumococcal disease according to age/risk schedules;
- Aspiration precautions and enteral feeding where required;
- Contracture prevention, orthopedic surveillance and bone-health support;
- Cardiac surveillance;
- Respiratory/anesthetic planning before surgery;
- Avoid unnecessary respiratory depressants and carefully monitor opioids, sedatives and anesthesia.

No public-health sanitation or vector-control intervention is applicable because the disorder is neither infectious nor environmentally transmitted.

---

# 14. Other species and naturally occurring disease

## 14.1 Orthologs and taxonomy

| Species | Taxonomy identifier | Ortholog / identifier | Natural disease evidence |
|---|---:|---|---|
| Human, *Homo sapiens* | NCBI Taxon 9606 | *DNAJB4*, NCBI Gene 11080 | CMYO21 |
| House mouse, *Mus musculus* | NCBI Taxon 10090 | *Dnajb4*, NCBI Gene **67035**, MGI:1914285 | Engineered models; no established analogous spontaneous breed disease |
| Rat, *Rattus norvegicus* | NCBI Taxon 10116 | *Dnajb4*, NCBI Gene **295549** | No natural homologous disease established |
| Zebrafish, *Danio rerio* | NCBI Taxon 7955 | *dnajb4*, NCBI Gene **445061** | No published CMYO21-like natural disease |
| Budding yeast, *Saccharomyces cerevisiae* | NCBI Taxon 4932 | *SIS1* is a functional class-B DNAJ homolog, not a one-to-one vertebrate ortholog | Used for complementation assays |

Mouse, rat and zebrafish stringent orthology is listed by MGI, and the zebrafish Gene ID is 445061. [196][197]

## 14.2 Natural veterinary disease and transmission

No naturally occurring *DNAJB4*-related myopathy was identified in OMIA or veterinary case literature, and no breed-specific VBO annotation is established. Consequently:

- Veterinary prevalence and breed risk are unknown;
- There is no zoonotic potential;
- There is no horizontal or cross-species transmission;
- Conservation is relevant to comparative muscle proteostasis, not infectious susceptibility.

---

# 15. Model organisms and experimental systems

| Model | Type/resource | Recapitulated findings | Applications | Limitations |
|---|---|---|---|---|
| *Dnajb4* knockout mouse | Mammalian CRISPR knockout; C57BL/6NJ-*Dnajb4*^em1(IMPC)J/Mmjax; **MMRRC_046155-JAX** | Kyphosis by four to eight months, reduced hanging-grid endurance, lower muscle mass, marked diaphragm thinning/atrophy, core-like fibers and accumulation of Z-disc/chaperone proteins | Causal proof of loss of function; diaphragm biology; pathology; preclinical gene replacement | Did not reproduce acute lethal respiratory failure within the reported period; forelimb grip was preserved through eight months |
| *Dnajb4* p.Phe90Leu knock-in mouse | Mammalian knock-in model of dominant allelic disease | Weakness and type-1-fiber protein inclusions | Distinguishes dominant toxic/dominant-negative disease from recessive CMYO21 | Models a separate dominant distal myopathy, not CMYO21 |
| C2C12 *Dnajb4*-knockout cells | CRISPR skeletal-myoblast/myotube model | Normal differentiation but excess fusion, larger myotubes, insoluble desmin/DNAJB6/CRYAB and myofibrillar aggregates | Cell-autonomous proteostasis and rescue assays | Murine immortalized cells do not model ventilation or systemic progression |
| Patient fibroblasts | Human primary in-vitro model | Reduced/absent DNAJB4 for destabilizing variants | Protein stability and variant validation | Fibroblasts are not mature skeletal myofibers |
| HEK293/Flp-In expression systems | Human-cell overexpression model | Variant-specific degradation kinetics | Protein half-life and rescue experiments | Artificial expression and non-muscle context |
| HeLa TDP-43 heat-shock assay | Human-cell stress model | Persistent TDP-43 aggregates with mutant DNAJB4 | Functional classification of missense variants | TDP-43’s role as the decisive disease client remains unproven |
| *S. cerevisiae* *sis1* complementation | Invertebrate/fungal functional system | J-domain-equivalent variants failed to rescue essential Sis1 function | Tests conserved DNAJ activity | Yeast lacks vertebrate sarcomeres, diaphragm and clinical phenotype |

The knockout mouse was viable at Mendelian ratios but developed kyphosis, weakness and particularly severe diaphragm atrophy, closely matching the anatomical selectivity of human disease. [230] MGI identifies mouse *Dnajb4* as MGI:1914285/NCBI Gene 67035. [227]

---

# Knowledge-base conclusions

1. **Definitive disease–gene relationship:** CMYO21 is caused by biallelic ***DNAJB4*** variants and follows autosomal-recessive inheritance.
2. **Core phenotype:** early or disproportionate respiratory failure plus axial rigidity/rigid spine, often with preserved limb strength.
3. **Mechanistic class:** HSP40/HSP70-associated chaperonopathy and protein-aggregate myopathy centered on Z-disc/myofibrillar proteostasis.
4. **Most useful diagnostic test:** genomic testing that includes *DNAJB4* sequence and exon-level CNV analysis, followed by segregation; WES/WGS reanalysis is important.
5. **Best-supported management:** proactive sleep/CO₂ and pulmonary surveillance, bilevel ventilation, assisted cough and multidisciplinary complication management.
6. **Major evidence gaps:** true prevalence, natural history, penetrance, disease-specific patient-reported outcomes, definitive client proteins, modifiers, biomarkers and clinical therapeutic trials.
7. **Most important recent development:** the October 2024 cohort broadened the variant and phenotype spectrum and provided preliminary evidence that J-domain missense variants predict earlier onset and greater mortality. [47]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 5 |
| Terms whose name was checked | 8 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051085` (obsolete chaperone cofactor-dependent protein refolding) (2 mentions) - replaced by `GO:0006457`
- `GO:0051082` (obsolete unfolded protein binding) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0051085` (2 mentions) - the report calls it "chaperone cofactor-dependent protein refolding"; GO calls it **obsolete chaperone cofactor-dependent protein refolding**, and lists "chaperone co-factor-dependent protein refolding" among its other names
- `GO:0051082` (1 mention) - the report calls it "unfolded-protein binding"; GO calls it **obsolete unfolded protein binding**
- `CL:0000594` (1 mention) - the report calls it "skeletal muscle fiber"; CL calls it **skeletal muscle satellite cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.

27 of 34 terms resolved to a current term; the rest could not be looked up either way.