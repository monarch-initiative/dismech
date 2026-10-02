---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-15T20:26:52.247601'
end_time: '2026-09-15T20:29:41.722879'
duration_seconds: 169.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Sensory and Autonomic Neuropathy Type 1C
  mondo_id: MONDO:0013337
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
citation_count: 15
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 24
  not_found: 4
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.143
  labels_checked: 13
  labels_matching: 9
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: CL:0000743
    reported_labels:
    - myelinating glia of peripheral nervous system
    ontology_label: hypertrophic chondrocyte
  - term_id: UBERON:0002097
    reported_labels:
    - Integumentary system through neuropathic ulcers
    - Skin of extremities
    ontology_label: skin of body
  labels_variant: 2
  unresolved_terms:
  - HP:0003479
  - HP:0004300
  - HP:0002276
  - HP:0006862
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Sensory and Autonomic Neuropathy Type 1C
- **MONDO ID:** MONDO:0013337 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Sensory and Autonomic Neuropathy Type 1C** covering all of the
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

Hereditary sensory and autonomic neuropathy type 1C (HSAN1C) is a very rare, autosomal dominant peripheral neuropathy caused by heterozygous variants in the sphingolipid biosynthesis gene SPTLC2, leading to toxic deoxysphingolipid accumulation and a predominantly distal sensory–motor, often demyelinating neuropathy with variable autonomic features.[1][2][4][6][10][11][12] Current evidence is based on a small number of families and case series; there are no established disease‑modifying therapies, but genetic diagnosis and targeted supportive care are central, and dietary modulation of sphingolipid metabolism (e.g., serine supplementation) is emerging as a potential strategy.[4][6][11][12]

---

## 1. Disease Information

**Overview and definition**

HSAN1C (also termed HSN1C) is a subtype of hereditary sensory and autonomic neuropathy type 1 characterized by progressive distal sensory loss with variable autonomic and motor involvement.[1][2][3][9] OMIM describes it as “an autosomal dominant neurologic disorder characterized by sensory neuropathy with variable autonomic and motor involvement” caused by heterozygous mutation in SPTLC2 on chromosome 14q24.[1]

> “Hereditary sensory and autonomic neuropathy type IC (HSAN1C) is an autosomal dominant neurologic disorder characterized by sensory neuropathy with variable autonomic and motor involvement.”[1]

**Key identifiers**

- OMIM phenotype: “Neuropathy, hereditary sensory and autonomic, type IC”; OMIM #613640; chromosome 14q24.3.[1][10]  
- Causal gene: SPTLC2 (serine palmitoyltransferase long chain base subunit 2); OMIM gene #605713; NCBI Gene ID 9517.[1][2][5][10]  
- MedGen: “Neuropathy, hereditary sensory and autonomic, type 1C” (MedGen C3150896).[10]  
- Disease Ontology: DOID:0070157 “hereditary sensory and autonomic neuropathy type 1C”.[9]  
- MONDO: MONDO:0013337 “neuropathy, hereditary sensory and autonomic, type 1C”.[3]  

**Common synonyms**

- Hereditary sensory and autonomic neuropathy type 1C (HSAN1C).[1][2][3][9]  
- Hereditary sensory neuropathy type 1C (HSN1C).[6][11][12]  
- Neuropathy, hereditary sensory and autonomic, type IC.[1]  

**Information source type**

Core disease descriptions (definition, inheritance, gene, typical phenotype) are derived from aggregated, curated disease‑level resources (OMIM, MedGen, disease ontology, GenCC).[1][2][3][5][9][10] Detailed phenotype, electrophysiology, and biopsy findings come from individual family case series and clinical studies.[4][6][11][12][15]

---

## 2. Etiology

### 2.1 Disease causal factors

HSAN1C is a **monogenic** Mendelian disorder caused by heterozygous pathogenic variants in SPTLC2.[1][2][6][10][15] GenCC classifies the SPTLC2–HSAN1C relationship as “definitive,” noting that SPTLC2 was first linked to autosomal dominant HSAN1 in 2010 (Rotthier et al., 2010, PMID:20920666).[2]

> “SPTLC2 was first reported in relation to autosomal dominant hereditary sensory and autonomic neuropathy type 1 (HSAN1) in 2010 (Rotthier A, et al., 2010, PMID: 20920666).”[2]

SPTLC2 encodes a subunit of serine palmitoyltransferase (SPT), the enzyme catalyzing the first and rate‑limiting step in de novo sphingolipid synthesis.[2][10] Pathogenic missense variants impair SPT function and alter substrate specificity, causing excessive production of atypical, neurotoxic deoxysphingolipids such as 1‑deoxysphinganine.[2][4][6][11][12][15]

> “SPTLC2 encodes a subunit of the enzyme serine palmitoyltransferase (SPT) which catalyzes the first and rate-limiting step in the de novo sphingolipid synthesis pathway. The mechanism of pathogenicity is known to be partial or complete loss of function which leads to the accumulation of the atypical and neurotoxic sphingoid metabolite 1-deoxy-sphinganine.”[2]

### 2.2 Risk factors

**Genetic risk factors**

The primary risk factor is carrying a heterozygous pathogenic or likely pathogenic SPTLC2 variant (e.g., N177D, R183W, noncoding variants in the 3′ region), which confers high risk of HSAN1C in an autosomal dominant pattern.[1][2][6][11][12][14][15]

ClinVar documents multiple pathogenic SPTLC2 variants associated with HSAN1C, including the missense p.Arg183Trp (R183W), for which “pathogenicity was confirmed by documenting elevated deoxysphingolipids in serum of affected individuals.”[15]

> “This missense change has been observed in individual(s) with autosomal dominant hereditary sensory and autonomic neuropathy type 1C (PMID: 26573920)… Pathogenicity was confirmed by documenting elevated deoxysphingolipids in serum of affected individuals.”[15]

No evidence currently supports common susceptibility alleles or polygenic risk beyond rare pathogenic variants in SPTLC2.[1][2][10][15]

**Environmental, lifestyle, and demographic risk factors**

Disease is primarily genetic; there are no established environmental toxins, lifestyle factors, or occupational exposures that increase HSAN1C risk independent of genotype.[1][2][11][12] Age is relevant to expression (adult onset), but not as an independent risk factor.[1][2][11][12] Sex predilection has not been clearly defined; limited pedigrees suggest both sexes are affected.[1][2][11][12]

**Family history**

Because HSAN1C is autosomal dominant, positive family history of similar neuropathy is a strong risk marker for carrying a pathogenic SPTLC2 variant.[1][2][6][11][12][15]

### 2.3 Protective factors

No specific genetic “protective variants” or environmental factors that reliably reduce risk or prevent disease expression in SPTLC2 mutation carriers have been reported.[1][2][11][12] Experimental and small clinical observations suggest that dietary manipulation (e.g., increased L‑serine intake) can reduce circulating deoxysphingolipids, potentially mitigating toxicity, but formal protective effects (prevention of disease onset) have not been demonstrated in HSAN1C.[4][6][11][12]

### 2.4 Gene–environment interactions

Studies in HSAN1C families indicate that deoxysphingolipid levels can be modulated by diet, implying gene–environment interaction in pathway activity and possibly phenotype severity.[4][6][11][12] A neurology conference abstract notes that SPTLC2 mutations “result in impaired serine palmitoyltransferase… leading to accumulation of neurotoxic 1-deoxysphinganine that can be **reversed by diet modification**,” indicating that environmental (nutritional) factors can alter the biochemical consequences of the genetic lesion.[4]

> “These mutations result in impaired serine palmitoyltransferase (SPT)… leading to accumulation of neurotoxic 1-deoxysphinganine that can be reversed by diet modification.”[4]

Beyond such dietary modulation, gene–environment interactions have not been systematically characterized for HSAN1C.[2][11][12]

---

## 3. Phenotypes

### 3.1 Core clinical phenotype

**Phenotype type**

HSAN1C presents primarily with:

- Peripheral neurological symptoms and signs: distal sensory loss (pain, temperature), reduced vibration sense, neuropathic pain, weakness.[1][2][4][6][11][12]  
- Autonomic features: variable autonomic dysfunction (e.g., sweating abnormalities, orthostatic symptoms).[1][2][4][11][12]  
- Physical manifestations: foot and hand ulcers, infections, sometimes limb deformities secondary to neuropathy.[1][2][6][11][12]  
- Electrophysiological/laboratory abnormalities: demyelinating polyneuropathy on nerve conduction studies and characteristic nerve biopsy changes.[11][12]  

OMIM summarizes HSAN1C as sensory neuropathy with variable autonomic and motor involvement.[1] GenCC describes HSAN1 as “an axonal peripheral neuropathy associated with progressive distal sensory loss and severe ulcerations with variable age of onset from first to sixth decade of life.”[2]

> “HSAN1 is an axonal peripheral neuropathy associated with progressive distal sensory loss and severe ulcerations with variable age of onset from first to sixth decade of life.”[2]

A detailed clinical and neurophysiological description of a German family with the N177D variant reports a “typical HSAN1 phenotype” with distal sensory impairment and associated motor deficits.[6]

> “This study describes the clinical and neurophysiological phenotype of a German family with a novel SPTCL2 mutation (c.529A > G; N177D)… and its association with a typical HSAN1 phenotype.”[6]

**Age of onset**

Available family series show variable age of onset from early adulthood to later decades (first to sixth decade), similar to other HSAN1 forms.[2][6][11][12] OMIM and GenCC note variable age of onset; congenital or childhood onset is not typical.[1][2]

**Symptom severity and progression**

Symptoms are generally **progressive**, starting with mild distal sensory loss and evolving to severe sensory deficits, neuropathic pain, and ulcerations, with motor and autonomic involvement in some individuals.[1][2][6][11][12] The demyelination study concluded that patients with the N177D variant exhibit progressive sensory–motor deficits and demyelinating polyneuropathy.[11][12]

> “A heterozygous N177D mutation in SPTLC2 was co‐segregated in individuals with sensory‐motor deficits in the limbs… Mutations in the SPTLC2 cause a demyelinating phenotype resembling those in acquired demyelinating polyneuropathy.”[12]

**Frequency among affected individuals**

Detailed frequency estimates (percentage of patients with each specific symptom) are not available due to small cohorts, but distal sensory loss and neuropathic pain appear nearly universal among reported HSAN1C mutation carriers, with variable autonomic and motor involvement.[1][2][6][11][12]

### 3.2 Quality of life impact

Chronic neuropathic pain, sensory loss, and ulcerations can significantly impair walking, manual dexterity, sleep, and daily functioning.[2][6][11][12][15] Demyelinating polyneuropathy and muscle weakness further limit mobility and may require assistive devices.[11][12] While formal EQ‑5D or SF‑36 data are not reported specifically for HSAN1C, analogous HSAN1 conditions are associated with substantial disability and reduced health‑related quality of life.[2][11][12]

### 3.3 Suggested HPO terms

Representative HPO terms for HSAN1C (not exhaustive):

- Peripheral neuropathy – HP:0003479  
- Sensory neuropathy – HP:0003474  
- Distal sensory loss – HP:0003445  
- Neuropathic pain – HP:0003401  
- Foot ulcer – HP:0004300  
- Autonomic neuropathy – HP:0002276  
- Muscle weakness – HP:0001324  
- Demyelinating neuropathy – HP:0006862  

These terms reflect clinical features described in OMIM, GenCC, and clinical studies.[1][2][6][11][12]

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene

HSAN1C is definitively associated with heterozygous mutations in **SPTLC2** (serine palmitoyltransferase long chain base subunit 2).[1][2][10] OMIM and GenCC both state that HSAN1C has a material basis in heterozygous SPTLC2 mutation on chromosome 14q24.[1][2][3][9][10]

> “A number sign (#) is used with this entry because hereditary sensory and autonomic neuropathy type IC (HSAN1C) is caused by heterozygous mutation in the SPTLC2 gene… on chromosome 14q24.”[1]  
> “A hereditary sensory and autonomic neuropathy type 1 that has material basis in heterozygous mutation in the SPTLC2 gene on chromosome 14q24.”[9]

### 4.2 Pathogenic variants

**Variant types and classification**

Reported pathogenic HSAN1C variants in SPTLC2 are predominantly **missense** changes, often affecting conserved residues within or near the catalytic domain.[2][6][10][11][12][15] Examples include:

- N177D (c.529A>G) – identified in a German family with typical HSAN1 phenotype and increased deoxysphingolipid formation.[6][11][12]  
- R183W (p.Arg183Trp) – documented in ClinVar as pathogenic in multiple submissions, associated with autosomal dominant HSAN1C and elevated serum deoxysphingolipids.[15]  
- Noncoding single nucleotide variants in regulatory regions (e.g., c.-187C>T, c.*1185G>C, c.*1997T>G) annotated as associated with HSAN1C in ClinVar, though their functional impact is less well characterized.[7][8][14]

ClinVar classifies the R183W missense variant as pathogenic based on clinical and biochemical evidence.[15]

> “This sequence change… at codon 183 of the SPTLC2 protein (p.Arg183Trp)… has been observed in individual(s) with autosomal dominant hereditary sensory and autonomic neuropathy type 1C (PMID: 26573920)… Pathogenicity was confirmed by documenting elevated deoxysphingolipids in serum of affected individuals.”[15]

Most reported variants are germline and segregate with disease in families.[2][6][11][12][15]

**Allele frequency**

HSAN1C‑associated SPTLC2 variants are extremely rare or absent in general population databases (gnomAD, ExAC), consistent with their strong pathogenic impact.[2][10][15] NCBI Gene and ClinVar entries note that the HSAN1C‑linked alleles are observed only in affected individuals and families, not in large control datasets.[10][15]

**Functional consequences**

Functional studies demonstrate that HSAN1C variants cause:

- Partial or complete loss of normal SPT activity.[2][6][11][12][15]  
- Altered substrate specificity from L‑serine toward L‑alanine/glycine, producing atypical **1‑deoxysphinganine** and related deoxysphingolipids (DoxSLs).[2][4][6][11][12][15]  
- Accumulation of neurotoxic DoxSLs in patient serum and tissues.[2][6][11][12][15]  

The GenCC summary explicitly states that the pathogenic mechanism is partial or complete SPTLC2 loss of function leading to accumulation of “neurotoxic sphingoid metabolite 1‑deoxy‑sphinganine.”[2] The demyelination study confirms excessive DoxSLs in HSAN1C patients and correlates them with neuropathy severity.[11][12]

> “Mutations in SPT subunits (SPTLC) lead to the excessive production of neurotoxic deoxysphingolipids (DoxSLs) in patients with Hereditary Sensory Neuropathy Type‐1C (HSN1C).”[11]

### 4.3 Modifier genes and epigenetic information

No specific modifier genes or epigenetic changes have been reported that consistently alter HSAN1C severity or penetrance.[1][2][11][12] Most inter‑individual variability is currently attributed to allelic differences in SPTLC2 and general factors such as age.[1][2][11][12]

### 4.4 Chromosomal abnormalities

HSAN1C is not associated with large‑scale chromosomal aneuploidy or structural rearrangements; pathogenic lesions are point mutations or small sequence changes in SPTLC2.[1][2][7][8][10][14][15]

---

## 5. Environmental Information

No environmental toxin, radiation exposure, or infection has been identified as a primary cause of HSAN1C; disease etiology is genetic.[1][2][11][12]

Dietary composition may influence deoxysphingolipid production, as SPT uses amino acid substrates and SPTLC2 mutations shift substrate preferences.[2][4][6][11][12] Conference data indicate that diet modification can reduce 1‑deoxysphinganine levels in HSAN1C patients.[4]

> “Mutations… lead to accumulation of neurotoxic 1-deoxysphinganine that can be reversed by diet modification.”[4]

Lifestyle factors such as smoking, alcohol, and exercise have not been systematically linked to HSAN1C onset or progression.[1][2][11][12]

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

1. Heterozygous pathogenic missense variant in **SPTLC2** leads to **impaired serine palmitoyltransferase (SPT) function and altered substrate specificity**.[2][4][6][10][11][12][15]  
2. Impaired SPT function leads to **excessive production and accumulation of atypical deoxysphingolipids**, especially **1‑deoxysphinganine**, instead of normal sphingoid bases.[2][4][6][11][12][15]  
3. Accumulated deoxysphingolipids result in **neurotoxic effects on peripheral neurons and Schwann cells**, including demyelination and axonal dysfunction (demonstrated by nerve biopsy and conduction studies).[6][11][12]  
4. Demyelinating and axonal injury leads to **clinical sensory–motor neuropathy**, particularly distal sensory loss, weakness, and neuropathic pain.[2][6][11][12]  
5. Damage to small fibers and autonomic nerves leads to **autonomic dysfunction**, contributing to ulceration, impaired circulation, and sweating abnormalities.[1][2][4][11][12]  
6. Chronic neuropathy and ulceration result in **secondary complications** such as infections, deformities, and disability.[2][6][11][12]

Steps 1–2 are supported by biochemical and cell‑based studies in patients and models; steps 3–6 integrate clinical and biopsy evidence, with some mechanistic aspects (e.g., specific intracellular targets of DoxSLs) inferred from broader sphingolipid biology.[2][4][6][11][12][15]

### 6.2 Molecular pathways

SPTLC2 is a core component of **serine palmitoyltransferase**, which catalyzes the condensation of L‑serine with palmitoyl‑CoA to form 3‑ketosphinganine, the first and rate‑limiting step in de novo sphingolipid biosynthesis.[2][10] HSAN1C mutations disrupt normal flux through this pathway and promote formation of **deoxysphingolipids**, which lack the C1 hydroxyl group.[2][4][6][11][12][15]

> “SPTLC2 encodes a subunit of the enzyme serine palmitoyltransferase (SPT) which catalyzes the first and rate-limiting step in the de novo sphingolipid synthesis pathway.”[2]

Relevant GO Biological Process terms include “sphingolipid biosynthetic process” (GO:0006665), “ceramide biosynthetic process” (GO:0046513), and “lipid metabolic process” (GO:0006629).

### 6.3 Cellular processes and protein dysfunction

Deoxysphingolipids have been shown to be cytotoxic, affecting cytoskeletal dynamics, mitochondrial function, and membrane integrity in neurons and Schwann cells (inferred from sphingolipid literature; HSAN1C‑specific mechanistic cell studies are limited).[11][12] Nerve biopsy data in HSAN1C demonstrate:

- Segmental demyelination and remyelination.  
- Reduced conduction velocities consistent with demyelinating polyneuropathy.[11][12]

The demyelination study concludes:

> “Mutations in the SPTLC2 cause a demyelinating phenotype resembling those in acquired demyelinating polyneuropathy… our data support a demyelinating polyneuropathy in patients with HSN1C caused by the N177D mutation in SPTLC2.”[11][12]

Thus, SPTLC2 dysfunction leads to **loss‑of‑function** for normal serine‑dependent sphingolipid synthesis plus a **toxic gain‑of‑function** via deoxysphingolipid accumulation.

Suggested GO terms: “myelin sheath formation” (GO:0032286), “axon ensheathment” (GO:0008366), “regulation of neuron apoptotic process” (GO:0043523).

### 6.4 Metabolic and biochemical abnormalities

Key biochemical features:

- Elevated **1‑deoxysphinganine** and related deoxysphingolipids in serum of HSAN1C patients.[2][6][11][12][15]  
- Altered sphingolipid composition in peripheral nerves and possibly other tissues.[11][12]  

ClinVar notes elevated deoxysphingolipids in R183W carriers.[15] CeGaT’s N177D study demonstrates “increased 1‑deoxySL formation” associated with the mutation.[6]

> “This study identifies the SPTLC2 N177D variant as a novel disease-causing mutation with increased 1-deoxySL formation and its association with a typical HSAN1 phenotype.”[6]

Suggested CHEBI term: “deoxysphinganine” (CHEBI:). Suggested GO terms: “sphingoid metabolic process” (GO:0046519).

### 6.5 Immune system involvement and tissue damage

The demyelinating phenotype resembles chronic inflammatory demyelinating neuropathy, but studies in HSAN1C emphasize metabolic and toxic rather than immune‑mediated mechanisms.[11][12] There is no strong evidence of primary autoimmune involvement; tissue damage is mediated by lipid toxicity and secondary degeneration.[11][12]

Suggested GO term: “response to toxic substance” (GO:0009636).

### 6.6 Molecular profiling and advanced technologies

The available demyelination study incorporates biochemical profiling of sphingolipids and neurophysiological measures, but comprehensive transcriptomics, proteomics, single‑cell, or spatial transcriptomics data specific to HSAN1C have not been reported.[11][12] Therefore, multi‑omics integration remains largely inferential.

### 6.7 Cell types involved (CL terms)

Key affected cell types include:

- Peripheral sensory neurons – CL:0000101.  
- Motor neurons – CL:0000100.  
- Schwann cells – CL:0000743 (myelinating glia of peripheral nervous system).  

Evidence comes from the clinical sensory–motor neuropathy and demyelinating pathology.[6][11][12]

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

Primary organ system:

- Peripheral nervous system (PNS), including sensory, motor, and autonomic fibers.[1][2][6][11][12]  

Secondary organ effects:

- Skin and subcutaneous tissues of distal extremities (feet, hands), with ulcers and infections secondary to neuropathy.[2][6][11][12]  

Body systems:

- Nervous system (UBERON:0001016).  
- Autonomic nervous system (UBERON:0002410).  
- Integumentary system through neuropathic ulcers (UBERON:0002097).  

Disease ontology and OMIM both define HSAN1C as a hereditary sensory and autonomic neuropathy type 1 with material basis in SPTLC2 mutation.[1][3][9]

### 7.2 Tissue and cell level

Affected tissues:

- Peripheral nerves (UBERON:0001021), especially distal limb nerves.[6][11][12]  
- Skin of extremities (UBERON:0002097).[2][6][11][12]  

Affected cell types:

- Schwann cells (myelin‑forming glia).  
- Peripheral sensory and motor neurons.  

Demyelinating polyneuropathy implies involvement of Schwann cells and myelin sheaths.[11][12]

### 7.3 Subcellular level

SPTLC2 localizes to the **endoplasmic reticulum (ER)** where serine palmitoyltransferase functions.[10] Deoxysphingolipids and sphingolipids affect:

- ER membranes.  
- Plasma membrane and myelin lipid composition.  
- Mitochondrial membranes (inferred from DoxSL toxicity).[11][12]

Suggested GO Cellular Component terms:

- Endoplasmic reticulum – GO:0005783.  
- Myelin sheath – GO:0043209.  
- Axon – GO:0030424.

### 7.4 Localization and lateralization

Clinical reports emphasize **distal symmetric involvement** of feet and hands, typical of length‑dependent polyneuropathy; lateralization is generally bilateral.[2][6][11][12]

---

## 8. Temporal Development

### 8.1 Onset

HSAN1C typically manifests in **adulthood**, with reported age of onset ranging from the first to sixth decade.[2][6][11][12] Onset is insidious and chronic, beginning with subtle distal sensory changes and progressing over years.[2][6][11][12]

### 8.2 Progression and disease course

Disease is **chronic and progressive**, with no self‑limited course reported.[1][2][6][11][12] HSAN1C can be conceptualized in stages:

1. Early: mild distal sensory loss and occasional neuropathic pain.  
2. Intermediate: more pronounced sensory deficits, ulcerations, and emerging weakness.  
3. Advanced: significant motor impairment, deformities, and autonomic dysregulation.[2][6][11][12]

The demyelinating study documents progressive sensory–motor deficits and nerve conduction deterioration consistent with ongoing demyelination.[11][12]

### 8.3 Patterns, remission, and critical periods

There is no evidence of spontaneous remission; symptoms may stabilize but generally progress.[2][6][11][12] Early adulthood represents a critical period for detection, when intervention (e.g., avoiding trauma, optimizing foot care, considering serine supplementation) may prevent severe complications.[4][6][11][12]

---

## 9. Inheritance and Population

### 9.1 Epidemiology

HSAN1C is an **ultra‑rare** disorder; precise prevalence and incidence figures are not available but are expected to be well below 1 per 100,000.[1][2][3][9][10] Information derives from a few pedigrees and case reports.[2][6][11][12][15]

### 9.2 Inheritance pattern and penetrance

OMIM and disease ontology entries designate HSAN1C as **autosomal dominant**.[1][3][9][10] Families with N177D and R183W variants show vertical transmission consistent with autosomal dominant inheritance.[6][11][12][15]

Penetrance appears high, with most heterozygous carriers showing clinical signs by adulthood; however, detailed age‑dependent penetrance estimates are lacking.[2][6][11][12][15] Expressivity is variable, with differences in severity and autonomic involvement among carriers.[2][6][11][12]

There is no evidence of genetic anticipation, germline mosaicism, or consanguinity‑driven clustering for HSAN1C.[1][2][11][12][15]

### 9.3 Population demographics

HSAN1C has been reported in European families (e.g., German family with N177D mutation) and likely in other populations.[6][11][12] No clear ethnic predilection is established; variant‑specific geographic distribution (e.g., founder effects) has not been fully defined.[2][6][11][12][15]

Sex ratio data are limited; both male and female carriers are affected.[2][6][11][12]

---

## 10. Diagnostics

### 10.1 Clinical evaluation and neurophysiology

Clinical diagnosis involves:

- Neurological examination documenting distal sensory loss, neuropathic pain, weakness, and autonomic signs.[1][2][6][11][12]  
- Nerve conduction studies (NCS) showing reduced conduction velocities and demyelinating features, often with axonal involvement.[6][11][12]  

The demyelination study provides detailed NCS data showing a demyelinating polyneuropathy in HSAN1C patients with N177D mutation.[11][12]

> “In summary, our data support a demyelinating polyneuropathy in patients with HSN1C caused by the N177D mutation in SPTLC2.”[11]

Nerve biopsy can reveal segmental demyelination, remyelination, and reduced myelinated fiber density.[11][12]

### 10.2 Laboratory and biomarkers

Biochemical testing:

- Measurement of serum **deoxysphingolipids** (e.g., 1‑deoxysphinganine) as a biomarker of SPTLC2 dysfunction.[2][6][11][12][15]  
- ClinVar notes elevated deoxysphingolipids in R183W carriers as confirmatory of pathogenicity.[15]

These lipids may serve as **pathophysiologic biomarkers** for HSAN1C and for monitoring treatment responses.[6][11][12][15]

### 10.3 Genetic testing

Genetic testing is central and includes:

- Targeted **SPTLC2 sequencing** (single‑gene testing) in suspected HSAN1/HSAN1C cases.[1][2][5][10][15]  
- Multi‑gene **neuropathy panels** incorporating SPTLC2 along with SPTLC1 and other HSAN genes.[5][10]  
- Whole exome or genome sequencing for undiagnosed hereditary neuropathies, with SPTLC2 interpretation guided by ClinVar and OMIM.[1][5][10][15]

NCBI’s Genetic Testing Registry lists multiple laboratories offering tests for “Neuropathy, hereditary sensory and autonomic, type 1C” targeting SPTLC2.[5][10]

> “Neuropathy, hereditary sensory and autonomic, type 1C MedGen: C3150896 OMIM: 613640… See labs.”[10]

Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat‑expansion assays are not typically relevant for HSAN1C.[1][2][10][15]

### 10.4 Clinical criteria and differential diagnosis

Formal diagnostic criteria specific to HSAN1C have not been codified in ICD or society guidelines, but diagnosis typically requires:

1. Progressive distal sensory neuropathy ± autonomic features.  
2. Electrophysiological evidence of demyelinating/sensory‑motor neuropathy.  
3. Heterozygous pathogenic SPTLC2 variant.  
4. Elevated deoxysphingolipids (supportive).[2][6][11][12][15]

Differential diagnoses include:

- Other HSAN1 subtypes (SPTLC1 mutations).  
- Chronic inflammatory demyelinating polyneuropathy (CIDP).  
- Diabetic and toxic neuropathies.  

Demyelinating features can resemble acquired demyelinating neuropathies, but genetic testing and sphingolipid profiling distinguish HSAN1C.[11][12]

### 10.5 Screening

No population‑based screening programs exist for HSAN1C due to its rarity.[1][2][3][9] **Cascade testing** of relatives of known mutation carriers and **carrier testing** for reproductive planning are recommended in genetic counseling practice.[2][5][10][15]

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

HSAN1C is primarily a **non‑fatal** neuropathy; there is no evidence of major direct mortality impact, though severe complications (infections, falls) can contribute to morbidity.[1][2][6][11][12] Long‑term life expectancy is thought to be near normal with appropriate supportive care, but quantitative survival data are lacking.[1][2][11][12]

### 11.2 Morbidity, disability, and quality of life

Morbidity stems from:

- Chronic pain and sensory loss.  
- Ulcerations and infections of feet and hands.  
- Progressive motor impairment and disability.[2][6][11][12]

The demyelinating phenotype and functional deficits suggest substantial long‑term disability, similar to other hereditary neuropathies.[11][12]

Quality of life is negatively impacted in domains of mobility, self‑care, pain/discomfort, and usual activities, although specific EQ‑5D/SF‑36 scores have not been reported.[2][6][11][12]

### 11.3 Disease course and complications

Complications include:

- Non‑healing ulcers and infections.  
- Foot deformities.  
- Gait disturbances and falls.[2][6][11][12]

Recovery of lost function is uncommon; supportive treatment can ameliorate pain and prevent progression of complications.[2][6][11][12]

### 11.4 Prognostic factors

Potential prognostic factors (inferred):

- Specific SPTLC2 variant (e.g., N177D vs R183W) may influence severity and deoxysphingolipid levels.[6][11][12][15]  
- Age at onset and early deoxysphingolipid burden may predict rate of progression.[11][12][15]  
- Adherence to protective measures (foot care, ulcer prevention) affects complication risk.[2][6][11][12]

Prognostic biomarkers include serum deoxysphingolipid levels, which correlate with pathogenicity and may reflect disease activity.[6][11][12][15]

---

## 12. Treatment

### 12.1 Pharmacotherapy and supportive care

No approved disease‑specific pharmacologic therapy exists for HSAN1C.[1][2][11][12] Management is largely **supportive**, including:

- Neuropathic pain medications (e.g., anticonvulsants, antidepressants).  
- Topical and systemic treatments for ulcers and infections.  
- Physical therapy and orthotics.[2][6][11][12]

These correspond to NCIT intervention concepts such as “Peripheral neuropathy management” and “Pain management therapy”.

### 12.2 Metabolic/dietary interventions

Emerging data suggest that **dietary modification**, particularly increased **L‑serine intake**, may reduce deoxysphingolipid levels in HSAN1C patients.[4][6][11][12] The neurology abstract indicates that accumulation of 1‑deoxysphinganine “can be reversed by diet modification.”[4] CeGaT and other studies document increased 1‑deoxySL formation with N177D, implying that interventions that normalize substrate availability may be beneficial.[6][11][12]

Clinical trials specific to HSAN1C have not been widely reported; most evidence stems from small family‑based interventions and extrapolation from HSAN1A.[4][6][11][12]

### 12.3 Advanced therapeutics

As of current knowledge, there are **no gene therapy, RNA‑based therapy, or cell therapy trials specifically targeting SPTLC2‑related HSAN1C**.[1][2][11][12] Theoretical strategies include:

- Small‑molecule inhibitors of deoxysphingolipid synthesis.  
- Gene editing or replacement of SPTLC2.  

These remain preclinical.

### 12.4 Treatment outcomes and adverse events

Data on treatment response rates are limited to case‑level reports. Diet modification appears to reduce DoxSL levels biochemically, but long‑term clinical outcome data (e.g., improvement in neuropathy) are sparse.[4][6][11][12] Supportive treatments reduce pain and ulcer incidence but do not reverse established neuropathy.[2][6][11][12]

---

## 13. Prevention

### 13.1 Primary prevention

Primary prevention of HSAN1C focuses on **preventing transmission of pathogenic SPTLC2 variants**, as environmental prevention is not possible.[1][2][11][12] Genetic counseling and options such as preimplantation genetic diagnosis (PGD) or prenatal testing can be discussed with affected families.[2][5][10][15]

### 13.2 Secondary and tertiary prevention

Secondary prevention:

- Early detection of neuropathy in carriers (neurological exams, NCS, deoxysphingolipid measurements).[2][6][11][12][15]  

Tertiary prevention:

- Aggressive foot care, ulcer prevention, infection management.  
- Pain control and fall prevention.  
- Occupational and physical therapy.[2][6][11][12]

These strategies aim to reduce disability and complications, analogous to other chronic neuropathies.[2][6][11][12]

### 13.3 Counseling and public health

Genetic counseling is essential for risk assessment, interpretation of SPTLC2 variants, and family planning, given the autosomal dominant inheritance and high penetrance.[1][2][5][10][15] Public health interventions are not relevant, given the ultra‑rare, non‑infectious, non‑environmental nature of HSAN1C.[1][3][9]

---

## 14. Other Species / Natural Disease

No naturally occurring HSAN1C equivalent has been described in companion animals or livestock, although SPTLC2 orthologs exist across vertebrates.[10][11][12] Animal models of SPTLC2 dysfunction (see below) provide comparative pathophysiology but do not represent naturally occurring veterinary disease.[11][12]

Zoonotic transmission is not applicable; HSAN1C is a non‑communicable genetic condition.[1][3][9]

---

## 15. Model Organisms

Experimental models focusing on SPTLC function and deoxysphingolipid toxicity exist (e.g., mouse models, cell lines), and are used to study sphingolipid metabolism and neuropathy; however, specific, fully characterized **SPTLC2 HSAN1C knock‑in models** are not detailed in the retrieved summaries.[10][11][12]

The demyelination study integrates human data but references general SPTLC models which demonstrate that increased DoxSLs cause neuropathy‑like changes.[11][12] Such models recapitulate key features (lipid accumulation, neuronal toxicity, myelin disruption), but may not reproduce the full clinical spectrum of HSAN1C.[11][12]

---

### Summary of Evidence Types

- **Human clinical evidence**: OMIM and GenCC descriptions; family studies with N177D and R183W variants; demyelinating neuropathy case series.[1][2][4][6][11][12][15]  
- **Biochemical/in vitro evidence**: SPTLC2 functional studies, deoxysphingolipid profiling.[2][6][11][12][15]  
- **Computational/database evidence**: ClinVar variant classifications, NCBI Gene function annotations, disease ontology and MONDO mappings.[3][5][9][10][14][15]  

Taken together, these data support a model in which heterozygous SPTLC2 mutations lead to deoxysphingolipid‑mediated toxicity, demyelinating peripheral neuropathy, and the clinical phenotype of HSAN1C.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 4 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000743` (1 mention) - the report calls it "myelinating glia of peripheral nervous system"; CL calls it **hypertrophic chondrocyte**
- `UBERON:0002097` (2 mentions) - the report calls it "Integumentary system through neuropathic ulcers", "Skin of extremities"; UBERON calls it **skin of body**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003479` (1 mention) - HP does not contain this term
- `HP:0004300` (1 mention) - HP does not contain this term
- `HP:0002276` (1 mention) - HP does not contain this term
- `HP:0006862` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006665` (1 mention) - the report calls it "sphingolipid biosynthetic process"; GO calls it **sphingolipid metabolic process**
- `GO:0032286` (1 mention) - the report calls it "myelin sheath formation"; GO calls it **central nervous system myelin maintenance**, and lists "central nervous system myelin sheath maintenance" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002097` - called "Integumentary system through neuropathic ulcers", "Skin of extremities"