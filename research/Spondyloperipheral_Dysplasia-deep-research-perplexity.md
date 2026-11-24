---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-06T13:13:15.718779'
end_time: '2026-11-06T13:19:11.152054'
duration_seconds: 355.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spondyloperipheral Dysplasia
  mondo_id: MONDO:0010078
  category: Mendelian
  causal_genes: COL2A1
  omim_id: OMIM:271700
  synonyms: spondyloperipheral dysplasia-short ulna syndrome
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 9
  verified: 8
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.111
  relevance_assessed: 8
  on_topic: 5
  unresolved_references:
  - DOI:10.1002/(SICI)1096-8628(19960503)63:1%3C123::AID-AJMG22%3E3.0.CO;2-P
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 29
  verified: 25
  not_found: 3
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.107
  labels_checked: 1
  labels_matching: 1
  unresolved_terms:
  - HP:0002658
  - HP:0004212
  - HP:0004270
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloperipheral Dysplasia
- **MONDO ID:** MONDO:0010078 (if available)
- **Causal gene(s):** COL2A1
- **OMIM:** OMIM:271700
- **Synonyms:** spondyloperipheral dysplasia-short ulna syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spondyloperipheral Dysplasia** covering all of the
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

# Spondyloperipheral Dysplasia (COL2A1-Related): An Integrated Review of Disease Characteristics

Spondyloperipheral dysplasia is an ultra‑rare Mendelian skeletal dysplasia caused by heterozygous pathogenic variants in the **COL2A1** gene, which encodes the alpha‑1 chain of type II collagen, a key structural protein of cartilage, vitreous body, and inner ear connective tissues.[1][5][6] The disorder is characterized clinically by disproportionate short stature, platyspondyly, epiphyseal dysplasia, and a distinctive peripheral skeletal involvement with brachydactyly type E and, in many individuals, short ulnae, hence the synonym “spondyloperipheral dysplasia‑short ulna syndrome.”[2][10][19] Molecular studies have shown that virtually all definitively associated variants cluster in the C‑propeptide domain of COL2A1 and are truncating (frameshift or nonsense) or closely related in‑frame alterations, leading to abnormal C‑terminal processing of type II procollagen.[6][7][11][12][17][18] This places spondyloperipheral dysplasia within the spectrum of type II collagenopathies, but with a uniquely prominent brachydactyly component that correlates with experimental data implicating the collagen II C‑propeptide (“chondrocalcin”) in growth plate calcification.[7][12] Clinically, SPD shows autosomal dominant inheritance with marked variable expressivity, ranging from mildly affected adults identified only after the birth of a severely affected child to prenatal lethal forms at the Torrance end of the SPD–PLSD‑T spectrum.[1][8][15] Because of its extreme rarity (estimated prevalence below 1 per 1,000,000), current knowledge is derived almost entirely from case reports, small families, curated databases (OMIM, Orphanet, MedlinePlus, ClinVar), and mechanistic inferences from broader type II collagen research, rather than from large cohorts or trials.[1][2][4][5][7][11][12][15] The following sections synthesize these scattered data into a structured disease knowledge base, integrating clinical phenotypes, genetics, pathophysiology, diagnostics, prognosis, treatment, and translational perspectives.

## 1. Disease Information: Nosology, Identifiers, and Data Sources

### 1.1 Definition and Clinical Concept

Spondyloperipheral dysplasia (SPD) is defined as a primary bone dysplasia characterized by the combination of axial skeletal changes typical of type II collagenopathies (platyspondyly, epiphyseal dysplasia, short trunk) and peripheral skeletal abnormalities, especially brachydactyly type E and short ulnae.[1][2][4][10] OMIM describes SPD as a distinct nosologic entity caused by heterozygous mutations in COL2A1 on chromosome 12q13.11, emphasizing platyspondyly and brachydactyly as hallmark features.[1] Orphanet’s disorder entry “spondyloperipheral dysplasia‑short ulna syndrome” similarly defines a rare genetic primary bone dysplasia with highly variable phenotype, typically including platyspondyly, brachydactyly type E, bilateral short ulnae, and mild short stature.[2] MedlinePlus Genetics frames the disease more broadly as “a disorder that impairs bone growth” and highlights disproportionate short stature, short torso, short limbs, and brachydactyly, often with clubfeet, myopia, and hearing loss.[5][19][20]

An early clinical description by Kelly and colleagues in 1977 referred to SPD as an unusual familial spondyloepiphyseal dysplasia and helped delineate the axial skeletal features before molecular genetics was available.[3] Subsequent case reports, notably Sorge et al. in 1995, expanded the phenotype to include facial features (“pugilistic face”), sensorineural deafness, and intellectual disability in some individuals.[4] With the discovery of COL2A1 C‑propeptide mutations in SPD by Zabel et al. in 1996 and Zankl et al. in 2004, SPD was firmly integrated into the type II collagenopathy group while retaining its distinctive peripheral skeletal signature.[7][12][13][17][18]

### 1.2 Key Identifiers and Classification

Multiple standardized identifiers and classification systems capture spondyloperipheral dysplasia as a Mendelian skeletal disorder. OMIM assigns SPD the phenotype number **271700**, linked to the COL2A1 gene (MIM 120140) on chromosome 12q13.11.[1] Orphanet lists SPD‑short ulna syndrome under **ORPHA:1856**, classifying it as a disorder of the skeletal system within the group of collagen type II‑related dysplasias.[2] The Monarch Initiative ontology maps SPD to **MONDO:0010078**, describing it as “a condition caused by truncating mutations in the C‑propeptide of COL2A1” and emphasizing brachydactyly with a prominent first toe as a distinguishing feature.[10]

International disease classification systems assign SPD to congenital skeletal dysplasias. Orphanet notes the ICD‑10 code **Q77.7** and ICD‑11 code **LD24.3** for spondyloperipheral dysplasia‑short ulna syndrome, aligning it with other spondylo‑epiphyseal dysplasias and osteochondrodysplasias.[2] MedGen at NCBI uses the concept ID **C0796173** for SPD, with the preferred name “spondyloperipheral dysplasia” and synonyms including “spondyloperipheral dysplasia with short ulna” and “spondyloperipheral dysplasia‑short ulna syndrome.”[20] The NIH Genetic Testing Registry (GTR) also lists SPD under the same concept, tied to COL2A1 and summarizing core clinical features.[19]

From a nosologic standpoint, SPD is categorized as a **Mendelian** monogenic disorder of connective tissue, specifically a **type II collagenopathy** in the subclass of chondrodysplasias, with autosomal dominant inheritance and extremely low prevalence (<1/1,000,000).[1][2][10]

### 1.3 Synonyms and Alternative Names

Across databases and publications, several synonyms are used, but they all refer to COL2A1‑related SPD. Common names include:

“Spondyloperipheral dysplasia” (primary term in OMIM, MedlinePlus, MedGen).[1][5][20]

“Spondyloperipheral dysplasia‑short ulna syndrome,” emphasizing the frequent presence of short ulnae.[2][10][18][19]

“Spondyloperipheral dysplasia with short ulna,” a synonym used in MedGen and ClinVar submissions.[18][20]

Occasionally, SPD has been described historically as “an unusual familial spondyloepiphyseal dysplasia” before its distinct identity was established.[3] Within the broader collagenopathy literature, SPD is sometimes discussed as part of the “SPD–Torrance spectrum,” referring to its close relationship to **platyspondylic lethal skeletal dysplasia, Torrance type (PLSD‑T)**, which is caused by dominant‑negative C‑propeptide mutations and shares many axial skeletal features but is typically perinatally lethal.[7][8][15]

### 1.4 Nature of Available Information

Because SPD is extremely rare, virtually all detailed knowledge derives from **aggregated disease‑level resources** (OMIM, Orphanet, MedlinePlus, MedGen, Monarch Initiative, GTR) and from a limited set of **individual case reports and small family studies** in the primary literature.[1][2][3][4][5][7][8][11][12][15] There are no published cohorts large enough to support robust epidemiological estimates, randomized trials, or standardized natural history models. Instead, data have been curated from a handful of well‑documented families with molecular confirmation of COL2A1 C‑propeptide mutations, including the index cases described by Zabel et al. (frameshift duplication, 1996), Zankl et al. (three truncating mutations, 2004), Bedeschi et al. (nonsense mutation in mother and child, 2011), Zhang et al. (novel frameshift in a Chinese family, 2013), and Désir et al. (somatic mosaicism for a PLSD‑T mutation in a mildly affected mother, 2012).[7][8][11][12][15]

These patient‑level data are then distilled into disease‑level summaries in OMIM and Orphanet, which provide concise descriptions of cardinal features, inheritance, prevalence, and causal gene. MedlinePlus Genetics and GTR offer patient‑oriented narratives and testing information, while MedGen and Monarch Initiative provide ontology‑bridged phenotypic and genetic annotations.[5][6][10][19][20] Thus, SPD knowledge is an archetype of a rare disease knowledge base built almost entirely from highly curated case‑based evidence rather than population‑scale analytics.

## 2. Etiology: Genetic Cause, Risk, and Modifiers

### 2.1 Primary Cause: COL2A1 C‑Propeptide Mutations

The primary and defining etiologic factor in spondyloperipheral dysplasia is heterozygous pathogenic variation in **COL2A1**, specifically affecting the C‑propeptide domain near the C‑terminus of the alpha‑1(II) collagen chain.[1][6][7][11][12] The COL2A1 gene, located on chromosome 12q13.11, encodes the procollagen type II alpha‑1 chain that self‑associates into homotrimeric type II procollagen molecules, which undergo extracellular processing to form mature collagen fibrils in cartilage, vitreous, and the inner ear.[6][20] 

MedlinePlus Genetics summarizes the etiologic mechanism succinctly:

> “Spondyloperipheral dysplasia is caused by variants (also called mutations) in the COL2A1 gene… The variants in the COL2A1 gene that cause spondyloperipheral dysplasia typically affect a region of the protein called the C‑propeptide domain.”[5]

This is supported by molecular studies showing that all definitively associated SPD mutations are truncating changes—frameshift duplications or nonsense variants—localized to exons encoding the C‑terminal C‑propeptide.[7][11][12][17][18] Zabel et al. reported the first such mutation in 1996: a 5‑bp duplication in exon 51 leading to a frameshift and premature stop codon, producing a truncated C‑propeptide region outside the helical domain.[12][14][17] Zankl et al. later ascertained two additional unrelated individuals with SPD and identified novel truncating mutations in the C‑propeptide, confirming truncating C‑propeptide variants as the shared molecular hallmark.[7][13][18]

ClinVar classifies several of these variants as pathogenic for SPD. The NM_001844.5(COL2A1):c.4287_4291dup (p.Tyr1431fs) duplication corresponds to the Zabel 1996 patient and is annotated as pathogenic for spondyloperipheral dysplasia.[17] Similarly, NM_001844.5(COL2A1):c.4314C>A (p.Cys1438Ter) is a nonsense variant identified by Zankl et al. in an SPD patient and is also classified as pathogenic.[18] Zhang et al. described another truncating mutation, p.Lys1444AsnfsX27, in an affected Chinese individual, strengthening the pattern of C‑terminal truncation.[11] Collectively, these cases, together with OMIM’s aggregated analysis, establish that SPD is etiologically defined by **germline heterozygous truncating mutations in the COL2A1 C‑propeptide domain**.[1][6][7][11][12][17][18]

### 2.2 Genetic Risk Factors and Susceptibility

In the context of SPD, the primary genetic risk factor is simply **inheritance of a pathogenic C‑propeptide COL2A1 variant**. The disease is autosomal dominant, meaning that a single mutated allele is sufficient to cause the phenotype.[1][2][5][19] Penetrance appears high but expressivity is markedly variable: some heterozygous carriers manifest severe skeletal abnormalities, while others, including mosaic individuals, may show mild features or be diagnosed only after detailed evaluation following an affected pregnancy.[4][8][15] No common susceptibility alleles or polygenic risk factors have been described, reflecting the rarity and monogenic nature of the condition.

There is some evidence that specific **mutation type and position** within the C‑propeptide may modulate the severity and qualitative phenotype, particularly along the continuum between SPD and PLSD‑T. Zankl et al. proposed that truncating mutations close to the 3′ end of the COL2A1 mRNA might escape nonsense‑mediated decay, permitting translation of mutant chains that fail to trimerize but still accumulate in chondrocyte endoplasmic reticulum (ER), whereas certain missense or in‑frame deletions may exert a dominant‑negative effect by incorporating into abnormal trimers.[7][8][9] This mechanistic distinction correlates with clinical severity: classical SPD with survival into adulthood versus lethal PLSD‑T in the fetus or neonate, as illustrated in the mosaic mother‑fetus pair described by Désir et al.[8]

Modifier genes are not well characterized for SPD specifically. However, broader type II collagenopathies show phenotypic overlap with other connective tissue disorders, and it is plausible (though not demonstrated) that variants in ECM components, growth factor pathways, or cartilage regulatory genes could modify skeletal severity or joint degeneration. To date, no reproducible modifier loci have been reported in SPD cohorts, and the limited number of cases precludes formal genetic association studies.[1][7][11][12]

### 2.3 Environmental and Lifestyle Risk Factors

No specific environmental, occupational, or lifestyle risk factors have been implicated in the **primary** occurrence of spondyloperipheral dysplasia. Because SPD is driven by highly penetrant germline COL2A1 mutations, its incidence is governed almost entirely by de novo mutational events and autosomal dominant transmission, rather than modifiable exposures.[1][2][5] 

Environmental factors may influence **secondary manifestations** such as degenerative joint disease, pain, and mobility limitations. For example, high mechanical load, obesity, or joint trauma might exacerbate early osteoarthritis in individuals with structurally abnormal cartilage, as extrapolated from general orthopedic knowledge. However, such relationships have not been specifically studied in SPD patients, and any statements about lifestyle influences remain inferential. The available case reports rarely include detailed environmental histories, focusing instead on genetic findings and skeletal morphology.[4][7][11][12][15]

### 2.4 Protective Factors and Gene–Environment Interactions

There are no known genetic protective variants that reduce risk for SPD in carriers of COL2A1 C‑propeptide mutations. Penetrance appears high, and even mosaic carriage can manifest as mild SPD or related phenotypes.[8] Environmental protective factors likewise have not been identified, though general recommendations for skeletal health—such as maintaining normal weight, adequate vitamin D and calcium status, and avoiding high‑risk trauma—are reasonable for minimizing complications, rather than preventing the primary disease.

Gene–environment interactions have not been systematically explored in SPD. The conceptual possibility exists that environmental stressors (e.g., ER stressors, inflammatory insults, or mechanical overload) could exacerbate the consequences of mutant collagen II in chondrocytes, but there is no direct evidence for such interactions in SPD specifically. Mechanistic insights largely come from in vitro studies of collagen II biosynthesis and experimental models of ER stress, rather than SPD‑targeted experiments.[6][7][12][16] Given the rarity of SPD, prospective studies of gene–environment interplay are unlikely in the near term, and knowledge will probably continue to rely on extrapolation from common cartilage disorders.

## 3. Phenotypes: Clinical Spectrum, Severity, and Impact

### 3.1 Overview of Core Phenotypes

SPD’s phenotypic signature is a combination of **axial skeletal dysplasia** and **peripheral brachydactyly**, with variable extraskeletal involvement of the eyes, ears, and neurodevelopment.[1][2][4][5][10][19][20] MedlinePlus Genetics describes:

> “People with spondyloperipheral dysplasia typically have short stature, with a short torso, short arms and legs, and short fingers and toes (brachydactyly)… Affected individuals also tend to have flattened bones of the spine (platyspondyly) and inward‑ and upward‑turning feet (clubfoot). Some people… may also experience nearsightedness (myopia) or hearing loss.”[5][19][20]

Orphanet’s disease definition adds brachydactyly type E changes (short metacarpals and metatarsals, short distal phalanges) and bilateral short ulnae, as well as possible midface hypoplasia, degenerative proximal femoral changes, limited elbow extension, sacralization of L5, and clubfeet.[2] OMIM aggregates similar features, listing brachydactyly, depressed nasal bridge, flat acetabular roof, flat capital femoral epiphyses, acetabular spurs, and platyspondyly among others.[1][10][20]

From a phenotype ontology perspective, important **HPO terms** include: disproportionate short stature (HP:0003521), platyspondyly (HP:0004322), epiphyseal dysplasia (HP:0002658), brachydactyly (HP:0001156), brachydactyly type E (HP:0005863), short ulna (HP:0003026), clubfoot (HP:0001762), hip dysplasia (HP:0001762), myopia (HP:0000545), sensorineural hearing impairment (HP:0000407), intellectual disability (HP:0001249), midface hypoplasia (HP:0000322), and sacralization of lumbar vertebra (HP:0004590).[1][2][10][20]

### 3.2 Axial Skeletal Phenotypes

The axial skeleton—spine, thorax, pelvis—is consistently involved in SPD, reflecting the central role of type II collagen in vertebral endplates and epiphyseal cartilage. Platyspondyly, defined as flattened vertebral bodies with reduced height and sometimes rounded or ovoid configuration on lateral radiographs, is nearly universal among reported SPD patients.[1][4][7][10][20] Vertebral endplates often show irregular indentations, and OMIM notes “irregular vertebral endplates” and “vertebral body abnormalities (platyspondyly, end‑plate indentations)” as characteristic features.[1][11][20]

Pelvic and proximal femoral changes are also prominent. OMIM and MedGen list flat acetabular roofs, flat capital femoral epiphyses, and acetabular spurs, reflecting abnormal development of the hip joint.[1][10][20] Sorge et al. described “hip dysplasia” in their 1995 case,[4] and Zhang et al. noted hip dysplasia and epiphyseal abnormalities in the Chinese SPD patient.[11] These features correspond to HPO terms such as flat acetabular roof (HP:0003298), flat capital femoral epiphysis (HP:0006607), and hip dysplasia (HP:0001762).[20]

Thoracic configuration may be affected, leading to barrel‑shaped chest or exaggerated anterior convexity of the thoracic spine, as catalogued in MedGen’s phenotype list.[20] Sacralization of L5, where the fifth lumbar vertebra is fused or partially fused to the sacrum, has been specifically mentioned in Orphanet’s description of SPD‑short ulna syndrome.[2] The combined axial changes contribute to disproportionate short trunk, altered spinal biomechanics, and potential predisposition to early degenerative changes and back pain.

### 3.3 Peripheral Skeletal Phenotypes: Brachydactyly and Short Ulna

The **peripheral skeletal** involvement—hence “peripheral” in the disease name—is dominated by brachydactyly type E and, in many cases, short ulnae. Brachydactyly type E refers to disproportionate shortening of the metacarpals and metatarsals, particularly the fourth and fifth rays, with relatively preserved phalanges.[2][7][11][12] Zankl et al. emphasized that SPD is defined by “platyspondyly and brachydactyly” and that the brachydactyly develops with age in children who initially present with a collagen II disorder phenotype.[7] OMIM and Monarch Initiative list brachydactyly and a prominent first toe among SPD’s distinguishing features.[1][10]

Radiographically, cone‑shaped epiphyses of the fingers, short distal phalanges, short fifth metacarpal, wide palms, and generalized short toes are catalogued in MedGen’s feature set for SPD.[20] These correspond to HPO terms such as brachydactyly (HP:0001156), short metacarpal (HP:0004026), short distal phalanx of finger (HP:0004212), cone‑shaped epiphyses (HP:0010580), broad palm (HP:0004270), and short toe (HP:0001831).[20] Sorge et al. described brachydactyly with “short fingers” clinically, and Zabel’s case had “brachydactyly E‑like changes” in the hands and feet.[4][12][14]

Short ulnae (HP:0003026) are particularly highlighted in Orphanet’s SPD‑short ulna syndrome entry, where bilateral short ulnae are part of the typical phenotype.[2] This may limit elbow extension and contribute to upper limb disproportion, with potential functional impact on reach and fine motor tasks. Limited elbow extension and mild short stature are mentioned by Orphanet as additional skeletal features.[2]

### 3.4 Extraskeletal Phenotypes: Eyes, Ears, Face, and Neurodevelopment

Type II collagen is expressed in the vitreous body of the eye and in the inner ear, so SPD, like other COL2A1 disorders, can include ocular and auditory manifestations. MedlinePlus Genetics notes that “some people with spondyloperipheral dysplasia may also experience nearsightedness (myopia) or hearing loss,” consistent with broader type II collagenopathy phenotypes.[5][19][20] Myopia (HP:0000545) and sensorineural hearing impairment (HP:0000407) have been reported in SPD case reports; Sorge et al. specifically described “sensorineural deafness” and “mental retardation” (intellectual disability) in their patient.[4] Intellectual disability (HP:0001249) appears to be variable and is not present in all cases, reflecting heterogeneous CNS involvement or secondary effects.

Facial features are variably reported. Sorge et al. described a “pugilistic face,” which likely refers to frontal bossing, midface hypoplasia, or coarse facial features.[4] Orphanet lists midface hypoplasia and depressed nasal bridge as occasional features.[2] OMIM and Monarch Initiative also include depressed nasal bridge (HP:0005280) in the SPD phenotype list.[1][10][20] These craniofacial changes may be subtle compared with the skeletal anomalies but can contribute to the gestalt that suggests a collagenopathy.

Neurodevelopmental concerns, when present, may stem from structural brain anomalies, sensory deficits, or other factors. However, the limited data do not support a consistent pattern of CNS malformation in SPD, and intellectual disability is best considered an occasional, possibly secondary phenotype.[4][2] Quality of life impact, therefore, is heavily contingent on the combination of skeletal, sensory, and cognitive involvement in each individual.

### 3.5 Age of Onset, Progression, and Severity

SPD is a **congenital** disorder in the sense that the underlying genetic lesion is present from conception and many skeletal abnormalities are detectable in infancy or even prenatally by ultrasound.[2][5][15] Orphanet lists infancy and neonatal periods as typical ages of onset.[2] Bedeschi et al. reported a mother with undiagnosed SPD whose fetus showed macrocephaly, narrow thorax, and shortened bowed limbs at 17–20 weeks’ gestation, illustrating prenatal manifestation along the SPD–PLSD‑T spectrum.[15] 

However, some phenotypic features are **age‑dependent**. Zankl et al. emphasized that brachydactyly type E “developed in childhood” in two infants originally presenting with type II collagenopathy features, and they proposed that precocious calcification and epiphyseal fusion might explain the delayed onset of peripheral skeletal changes.[7] Similarly, Orphanet notes that brachydactyly type E changes may become more apparent with growth.[2] This dynamic pattern underscores the importance of longitudinal follow‑up for diagnostic clarity.

Symptom severity ranges from mild short stature and limited joint involvement to severe skeletal disproportion with significant functional impairment. Sorge’s 1995 patient manifested marked skeletal dysplasia plus sensorineural deafness and intellectual disability, while some adults identified in familial studies have relatively mild features.[4][7][11][15] In the mosaic SPD–PLSD‑T case, the mother’s phenotype was “compatible with mild spondyloperipheral dysplasia,” whereas the fetus’s phenotype was lethal.[8] Thus, SPD spans a broad severity spectrum, influenced by mutation type, mosaicism, and possibly other factors.

Symptom progression appears largely **non‑episodic and chronic**, with skeletal architecture established early and degenerative changes (e.g., hip osteoarthritis, spinal stenosis) potentially worsening over time. There is no evidence of remitting–relapsing course; rather, SPD represents a lifelong structural disorder with stable skeletal anomalies and age‑related secondary complications.

### 3.6 Quality of Life Impact

The impact of SPD on quality of life depends on the combination and severity of skeletal and extraskeletal features. Disproportionate short stature, limb shortening, and brachydactyly can impair mobility, manual dexterity, and ability to perform tasks requiring reach or fine motor coordination, affecting activities of daily living and vocational opportunities.[2][4][5] Hip dysplasia and acetabular anomalies may predispose to pain and limited range of motion, complicating walking, stair climbing, and participation in physical activities.[1][20] Thoracic deformities and platyspondyly could potentially influence respiratory function or back pain, though specific data in SPD are limited.

Sensorineural hearing loss, when present, contributes to communication barriers and may affect educational attainment and social integration, while myopia requires ongoing ophthalmologic care and optical correction.[4][5] Intellectual disability, although not universal, has substantial impact on independence and psychosocial functioning in those affected.[4] 

Formal quality‑of‑life instruments such as SF‑36 or EQ‑5D have not been systematically applied in SPD cohorts, given the rarity of the condition. Nevertheless, extrapolating from related skeletal dysplasias, one can infer meaningful limitations in physical functioning domains, variable impact on emotional and social domains, and potential need for assistive devices and environmental adaptations. Comprehensive multidisciplinary care that addresses orthopedic, audiologic, ophthalmologic, and developmental needs is likely to improve quality of life, even in the absence of disease‑modifying therapies.

## 4. Genetic and Molecular Information

### 4.1 COL2A1 Gene: Structure and Function

The **COL2A1** gene encodes the collagen type II alpha‑1 chain, the principal component of type II collagen, which is predominantly expressed in hyaline cartilage, the vitreous of the eye, and parts of the inner ear.[6][20] MedlinePlus summarizes:

> “The COL2A1 gene provides instructions for making the basic component of type II collagen, called the alpha‑1(II) chain. Type II collagen adds structure and strength to connective tissues and plays an important role in the normal development of joints, eyes, and the inner ear.”[6]

At the protein level, the alpha‑1(II) chain consists of a large central triple‑helical domain characterized by repeating Gly‑X‑Y motifs, flanked by N‑terminal and C‑terminal propeptides. During collagen biosynthesis, three alpha‑1(II) chains assemble into a procollagen triple helix in the ER, guided by intra‑ and interchain disulfide bonds in the C‑propeptide region, and are then secreted into the extracellular space where N‑ and C‑propeptides are cleaved to form mature fibrils.[6][12][16] The C‑propeptide, sometimes referred to as “chondrocalcin,” is implicated in matrix mineralization and growth plate calcification.[7][12]

Disease‑causing COL2A1 mutations span numerous domains and cause a spectrum of type II collagenopathies, including spondyloepiphyseal dysplasia congenita, Stickler syndrome type I, Kniest dysplasia, achondrogenesis type II, and PLSD‑T, among others.[1][6][9][16] Glycine substitutions in the triple‑helical domain are common in these classical collagenopathies, whereas SPD is uniquely associated with truncating mutations in the C‑propeptide domain.[1][6][7][11][12][17][18]

### 4.2 Pathogenic Variants in SPD: Types, Locations, and Classification

All definitively reported SPD‑causing variants are **heterozygous, germline, truncating mutations** in the C‑propeptide coding region of COL2A1, or closely related variants that disrupt critical cysteine residues and trimerization motifs.[1][6][7][11][12][17][18] Variant types include frameshift insertions/duplications, nonsense substitutions, and occasionally in‑frame deletions or missense variants at key residues, especially in cases overlapping with PLSD‑T.[7][8][11][12][18]

Zabel et al. (1996; American Journal of Medical Genetics 63:123–128, PMID:8723097) reported a sporadic patient with short stature, spondylo‑epiphyseal involvement, and brachydactyly E‑like changes, in whom they identified “a frameshift as consequence of a 5 bp duplication in exon 51 [of COL2A1] that leads to a stop codon,” representing “the first [mutation] to be located at the C‑terminal outside the helical domain of COL2A1.”[12][14][17] ClinVar records this duplication as NM_001844.5(COL2A1):c.4287_4291dup (p.Tyr1431fs) and classifies it as pathogenic for spondyloperipheral dysplasia.[17]

Zankl et al. (2004; Am J Med Genet A 129A:144–148, PMID:15316962) described three unrelated individuals with SPD, each harboring a different truncating mutation in the C‑propeptide coding region: one nonsense (p.Cys1438Ter) and two frameshift mutations leading to premature termination.[7][13][18] ClinVar annotates NM_001844.5(COL2A1):c.4314C>A (p.Cys1438Ter) as pathogenic for SPD, citing Zankl’s case.[18] The authors emphasized that all three mutations predict premature termination close to the 3′ end of the mRNA, likely escaping nonsense‑mediated decay and allowing synthesis of mutant chains that cannot trimerize.[7]

Zhang et al. (2013; Gene 522:107–110, PMID:23545312) identified a novel truncating mutation, p.Lys1444AsnfsX27, in the C‑propeptide of COL2A1 in a Chinese patient with SPD, further reinforcing the phenotype–genotype correlation.[11] Bedeschi et al. (2011; Orphanet Journal of Rare Diseases 6:7, PMID:21356074) reported a previously undescribed nonsense mutation in the C‑propeptide in a mother–child pair with SPD, extending the mutation catalogue.[15] Désir et al. (2012; Am J Med Genet A 158A:1948–1952, PMID:22495950) described a novel in‑frame deletion c.4458_4460delCTT (p.Phe1486del) in the C‑propeptide in a fetus with PLSD‑T and somatic mosaicism for the same mutation in a mother with mild SPD.[8] 

From a classification standpoint, all these SPD‑associated truncating variants are **pathogenic** under ACMG/AMP guidelines, given the clear causal relationship with a well‑defined monogenic phenotype, segregation data in families, functional predictions (loss of essential cysteine residues and trimerization motifs), and absence from population databases.[7][11][12][17][18] They are **germline** variants, transmitted in an autosomal dominant fashion, with occasional cases of somatic mosaicism as in Désir et al.[8] No somatic mutations have been implicated in SPD as a neoplastic or acquired condition.

### 4.3 Functional Consequences: Loss of Function, Dominant Negative, ER Retention

The functional consequences of SPD‑causing COL2A1 mutations involve a complex combination of **loss of normal type II collagen function** and potentially **gain‑of‑function or dominant‑negative effects** mediated by the mutant C‑propeptide. Zankl et al. proposed that truncating mutations near the 3′ end of COL2A1 “probably protect [the transcripts] from nonsense‑mediated decay and allow for synthesis of mutant procollagen chains.”[7] However, loss of crucial cysteine residues or other sequences essential for trimerization “prevents these chains from associating and participating in procollagen helix formation, and thus leads to accumulation in the ER—consistent with EM findings.”[7] This ER accumulation suggests a **dominant‑negative intracellular effect**, where mutant chains interfere with normal collagen biosynthesis, coupled with a **haploinsufficiency** for secreted functional collagen.

MedlinePlus and the COL2A1 gene fact sheet similarly explain that variants affecting the C‑propeptide domain “lead to the production of an abnormal version of the alpha‑1(II) chain that interferes with the production of procollagen molecules,” resulting in reduced mature type II collagen.[5][6] This decrease disrupts normal bone and cartilage development, leading to SPD’s skeletal abnormalities.[5][6]

The specific role of the C‑propeptide in calcification introduces an additional layer of functional consequence. Zankl et al. note that the C‑propeptide of collagen II had previously been found to promote calcification (“chondrocalcin”) and hypothesize that SPD mutations may induce “precocious calcification and premature fusion of metacarpal and phalangeal growth plates,” explaining brachydactyly type E.[7] This suggests a **gain‑of‑aberrant‑function** component in growth plate mineralization, though the precise biochemical mechanism remains to be elucidated.

In PLSD‑T, related C‑propeptide mutations have been characterized as **dominant‑negative** due to incorporation of mutant chains into abnormal trimers, causing severe structural defects and perinatal lethality.[9][16] The mosaic mother–fetus pair described by Désir et al. underscores that the same mutation can produce lethal PLSD‑T in a non‑mosaic fetus and milder SPD in a mosaic adult, underlining the importance of dosage and cellular distribution of mutant chains.[8]

### 4.4 Allele Frequencies and Population Data

Because SPD mutations are highly deleterious and cause a rare dominant skeletal dysplasia, they are expected to be **extremely rare or absent** in population databases such as gnomAD, ExAC, or 1000 Genomes. Specific allele frequencies for SPD‑associated variants are generally not reported in public data, but their classification as pathogenic and their occurrence in single families support their rarity.[11][17][18] 

The overall **carrier frequency** of SPD‑causing COL2A1 variants in the general population is unknown but is likely far below 1 in 100,000, consistent with the estimated clinical prevalence <1/1,000,000.[2][10] There are no reported founder mutations with elevated frequencies in particular ethnic or geographic populations; SPD cases have been described in European and Chinese families, suggesting a global distribution of sporadic and familial mutations.[7][11][12][15]

### 4.5 Modifier Genes, Epigenetics, and Chromosomal Abnormalities

Modifier genes specific to SPD have not been identified. The limited number of cases and strong primary effect of COL2A1 C‑propeptide mutations make it difficult to discern secondary genetic influences. However, in broader type II collagenopathies, phenotypic variability may be influenced by polymorphisms in matrix proteins, metalloproteinases, or signaling pathways regulating chondrocyte activity, providing a conceptual framework for potential modifiers.[6][9][16] Future whole‑genome or exome analyses in SPD families could, in principle, identify such modifiers, but no such studies have been reported to date.

Epigenetic alterations (DNA methylation, histone modifications, chromatin state) have not been studied in SPD specifically. Given that COL2A1 expression is tightly regulated during chondrogenesis, cartilage development and growth plate maturation involve complex epigenetic programming, but SPD’s etiology is clearly dominated by structural gene mutation rather than an epigenetic primary defect.[6][16] There is no evidence for chromosomal structural abnormalities (aneuploidy, translocations, inversions) directly causing SPD; all reported cases involve sequence‑level changes in COL2A1 on a structurally normal chromosome 12.[1][11][12][18][20]

## 5. Environmental Information: Non‑Genetic Influences

### 5.1 Environmental Factors

No specific environmental factor has been demonstrated to cause or substantially modify spondyloperipheral dysplasia. The disease is essentially a monogenic, germline COL2A1 disorder, and cases arise either through de novo mutation or autosomal dominant inheritance.[1][2][5][7][11][12] Studies of environmental exposures in SPD are non‑existent due to the condition’s rarity and the strong genetic signal. 

From a conceptual standpoint, environmental influences on cartilage health and bone growth—such as nutrition, endocrine milieu, and mechanical loading—could, in theory, modulate the severity of secondary complications (e.g., joint pain, osteoarthritis), but they do not alter the underlying skeletal architecture established by mutant collagen II during development.[6][16] No publication has linked toxin exposure, radiation, pollution, or occupational stress specifically to SPD onset or progression.

### 5.2 Lifestyle Factors

Similarly, lifestyle factors such as smoking, diet, exercise, and alcohol consumption have not been studied in relation to SPD severity or outcomes. For individuals living with SPD, general recommendations for bone and joint health—regular low‑impact exercise, maintenance of normal weight, avoidance of smoking, and balanced nutrition—are sensible but not disease‑specific. SPD’s primary manifestation is structural and congenital, making lifestyle interventions more relevant to managing symptoms and preventing secondary degeneration than to altering the core skeletal dysplasia.

### 5.3 Infectious Agents

SPD is not associated with any infectious agent. There is no evidence that bacterial, viral, fungal, or parasitic infection plays a causal or triggering role in the disease. Infectious complications may occur postoperatively or in association with general health, but these are not part of the disease definition or mechanism.

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

To integrate the available mechanistic data, the pathophysiology of spondyloperipheral dysplasia can be conceptualized as the following ordered causal chain:

Step 1: A **heterozygous truncating or structurally disruptive mutation in the C‑propeptide domain of COL2A1** leads to production of abnormal alpha‑1(II) collagen chains in chondrocytes and other COL2A1‑expressing cells.[1][6][7][11][12][17][18]

Step 2: The mutant C‑propeptide disrupts **trimerization and procollagen assembly**, resulting in failure of mutant chains to participate in triple helix formation and their **accumulation in the endoplasmic reticulum**, while reducing secretion of mature type II procollagen; this step is inferred from EM and biochemical data in collagen II disorders.[7][12][16]

Step 3: ER accumulation of mutant chains and reduced functional collagen secretion lead to **extracellular matrix disorganization** in cartilage, including altered fibril structure, abnormal collagen network, and defective integration with other ECM components such as proteoglycans.[12][16]

Step 4: Disorganized cartilage matrix and impaired collagen II support result in **defective growth plate function and endochondral ossification**, particularly in vertebral bodies, epiphyses, and peripheral bones, causing platyspondyly, epiphyseal dysplasia, and disproportionate short stature.[1][4][7][10][20]

Step 5: Abnormal behavior of the collagen II C‑propeptide (“chondrocalcin”) in the context of mutation **promotes precocious calcification and premature fusion of metacarpal and phalangeal growth plates**, leading to brachydactyly type E and short fingers and toes; this step is inferred from clinical timing and experimental evidence on C‑propeptide function.[7][12]

Step 6: Similar matrix and growth plate defects in the **ulnae and other long bones** lead to short ulnae, limited elbow extension, bowed long bones, and limb disproportion.[2][15][20]

Step 7: In cartilage of the **hip joint, thoracic spine, and pelvis**, defective collagen II causes flat acetabular roofs, flat capital femoral epiphyses, acetabular spurs, barrel‑shaped chest, and exaggerated thoracic curvature.[1][4][20]

Step 8: In the **vitreous body of the eye and inner ear structures**, reduced or abnormal type II collagen leads to altered structural integrity and refractive properties, resulting in myopia and sensorineural hearing impairment in some patients.[4][5][6]

Step 9: Over time, structural skeletal anomalies and cartilage matrix defects **predispose to early degenerative changes**, pain, and functional limitations, shaping the long‑term clinical course.[4][7][11][15]

Step 10: In cases where C‑propeptide mutations are more structurally disruptive or present at higher mutant dosage (e.g., non‑mosaic), the same mechanisms **extend to severe generalized skeletal dysplasia**, causing platyspondylic lethal skeletal dysplasia, Torrance type, on the SPD–PLSD‑T spectrum.[8][9][15]

### 6.2 Molecular Pathways and Biological Processes

At the molecular level, SPD implicates several key **biological processes** and **pathways**:

Collagen biosynthesis and processing (GO:0032964), including transcription of COL2A1, translation of alpha‑1(II) chains, post‑translational modifications, trimerization mediated by C‑propeptide disulfide bonds, and intracellular trafficking.[6][12][16]

Extracellular matrix organization (GO:0030198), involving assembly of collagen fibrils, crosslinking, interaction with proteoglycans (e.g., aggrecan), and maintenance of cartilage structural integrity.[6][12][16]

Cartilage development and chondrocyte differentiation (GO:0061036), covering growth plate dynamics, proliferation, hypertrophy, and matrix mineralization.[6][7][12][16]

Ossification and bone morphogenesis (GO:0001503), particularly endochondral ossification in the vertebral bodies, long bones, and epiphyses.[4][7][11][20]

Response to ER stress and unfolded protein response (GO:0030968), inferred from accumulation of mutant collagen chains in the ER and EM findings.[7][12][16]

While specific signaling cascades (e.g., Wnt, FGFR, BMP, MAPK) are crucial to cartilage and bone development, SPD’s pathophysiology is dominated by structural ECM disruption rather than primary signaling pathway defects. Nevertheless, altered ECM can modulate signaling microenvironments, influencing chondrocyte behavior indirectly.

### 6.3 Protein Dysfunction: C‑Propeptide and Chondrocalcin

The **C‑propeptide** of collagen II plays two major roles: mediating trimerization via disulfide bonds and facilitating matrix mineralization as “chondrocalcin.”[7][12] SPD mutations truncate or structurally alter this domain, thereby:

Removing critical cysteine residues required for correct interchain disulfide bonding and trimerization, leading to assembly failure and ER retention.[7][12]

Potentially altering the C‑propeptide’s interaction with calcium ions (CHEBI:29108) and other mineralization factors, which may change the timing or pattern of growth plate calcification.[7][12]

Zabel’s 1996 case showed, at the histological level, changes in chondrocyte morphology, collagen II fibril structure, and cartilage matrix composition, consistent with profound C‑propeptide dysfunction.[12][14][17] The authors concluded that the truncated C‑propeptide “seems to affect helix formation and produces changes of chondrocyte morphology, collagen type II fibril structure and cartilage matrix composition,” highlighting both intracellular and extracellular consequences.[12]

Zankl et al. built on prior knowledge that the C‑propeptide promotes calcification, suggesting that mutant C‑propeptide could cause premature epiphyseal fusion, a hallmark of brachydactyly type E in SPD.[7] While direct biochemical assays of these specific mutant C‑propeptides are limited, the consistency of clinical patterns across unrelated families supports this mechanistic inference.

### 6.4 Cellular Processes: Chondrocytes, Growth Plates, and ER Stress

The main **cell type** involved in SPD pathophysiology is the **chondrocyte** (CL:0000138), which resides in articular cartilage, growth plates, and vertebral endplates. Mutant collagen II disrupts chondrocyte ECM interactions, leading to altered proliferation, hypertrophy, and matrix deposition. Electron microscopy in type II collagenopathies shows dilated ER cisternae with accumulated mutant collagen, indicative of ER stress and potentially activation of the unfolded protein response.[7][12][16] Chronic ER stress can influence chondrocyte survival, apoptosis, and differentiation, further shaping cartilage architecture.

Growth plate chondrocytes in the metacarpals, metatarsals, ulnae, and vertebral bodies are particularly affected, resulting in abnormal patterns of longitudinal bone growth, premature epiphyseal closure, and skeletal dysplasia. Endochondral ossification, in which a cartilage template is replaced by bone, depends critically on a well‑organized collagen II matrix. SPD disrupts this template, leading to short bones, epiphyseal flattening, and platyspondyly.[4][7][11][20]

In the eye, specialized cells in the vitreous body depend on collagen II fibrils to maintain transparency and structural integrity; mutant collagen may alter vitreous consistency and refractive properties

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1002/(SICI)1096-8628(19960503)63:1%3C123::AID-AJMG22%3E3.0.CO;2-P` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002658` (1 mention) - HP does not contain this term
- `HP:0004212` (1 mention) - HP does not contain this term
- `HP:0004270` (1 mention) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.