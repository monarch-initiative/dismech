---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-31T20:06:38.642080'
end_time: '2026-10-31T20:07:36.024698'
duration_seconds: 57.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypercalciuria, Absorptive, 2
  mondo_id: MONDO:0007748
  category: Mendelian
  causal_genes: ADCY10
  omim_id: OMIM:143870
  synonyms: hypercalciuria, absorptive, susceptibility to; hypercalciuria, absorptive,
    type 2
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.7085406000000001
  session_id: 89c9b5bb-a581-5af1-a5aa-767b76668861
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 2
  validator_version: 0.4.0
term_validation:
  total_terms: 12
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypercalciuria, Absorptive, 2
- **MONDO ID:** MONDO:0007748 (if available)
- **Causal gene(s):** ADCY10
- **OMIM:** OMIM:143870
- **Synonyms:** hypercalciuria, absorptive, susceptibility to; hypercalciuria, absorptive, type 2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypercalciuria, Absorptive, 2** covering all of the
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

# Hypercalciuria, Absorptive, 2 (HCA2; MONDO:0007748; OMIM 143870): ADCY10 (soluble adenylyl cyclase, sAC)

**Evidence caveat.** I ran three web searches, which returned database summaries and the abstract text KEGG and DrugBank cite for the original paper. I did not open or verify any primary paper in full. Identifiers marked **[unverified]** are from memory and need `just fetch-reference` before they go into the KB. Run `just preflight-dr` and `just validate-research-terms` before using anything here. Every ontology CURIE below is a lead, not a verified binding.

## 1. Disease information

HCA2 is the OMIM phenotype (143870) assigned to the causal gene **ADCY10** (HGNC symbol; gene OMIM 605205; 1q24.2). ADCY10 encodes soluble adenylyl cyclase, a bicarbonate-, calcium- and ATP-regulated cAMP generator that is insensitive to G proteins and forskolin.

- **Phenotype.** Absorptive hypercalciuria (AH) is defined by intestinal calcium hyperabsorption. It causes hypercalciuria with normal serum calcium and normal or suppressed PTH, and it is a recurrent calcium-nephrolithiasis phenotype often complicated by reduced bone density.
- **Synonyms.** Hypercalciuria, absorptive, susceptibility to; hypercalciuria, absorptive, type 2; familial idiopathic hypercalciuria (a MedGen/OMIM-linked name).
- **Source level.** The information is aggregated at disease level (OMIM, KEGG, PanelApp), not from EHR data. Underlying data are from small research cohorts.
- **Gene-disease validity is contested.**
  - Genomics England PanelApp rates ADCY10 **Amber** for this condition. The reviewer note says the association rests partly on a single study and that the authors acknowledge it is questionable.
  - An Australian PanelApp panel was reported to downgrade it to **Red** (association-study-only).
  - OMIM-derived resources list it as autosomal dominant.
  - Do not set `CAUSATIVE` or copy a ClinGen-style tier. If no external body has classified the pair (ClinGen is not confirmed here), leave `gene_disease_validity` absent. Say in the genetic-record `notes` that the evidence is a single candidate-gene study.

Sources: [KEGG H02340](https://www.kegg.jp/entry/H02340), [MedGen C0342639](https://https.ncbi.nlm.nih.gov/medgen/C0342639), [PanelApp UK](https://panelapp.genomicsengland.co.uk/panels/878/gene/ADCY10/), [PanelApp AU](https://panelapp-aus.org/panels/192/gene/ADCY10), [GeneCards](https://www.genecards.org/card/ADCY10).

## 2. Etiology

- **Primary cause.** Genetic. The proposed lesion is ADCY10 variation in a locus on 1q23.3-q24.
  - Reed et al. 2002 (J Clin Endocrinol Metab 87:1476-85; **PMID:11932268 [unverified]**) sequenced a candidate gene in 12 unrelated Caucasian AH patients. They found 18 base substitutions in the human soluble adenylate cyclase gene.
  - Per the KEGG/DrugBank-cited abstract, one or more of these changes was associated with lower L2-L4 vertebral bone density.
  - The abstract wording is "eighteen base substitutions in the soluble adenylate cyclase human homolog gene; one or more base changes was associated with a lower L2-L4 vertebral bone density." Confirm the exact text against the cached abstract before using it as a snippet.
- **Linkage.** Reed et al. 1999 (J Clin Endocrinol Metab 84:3907-13; **PMID:10566627 [unverified]**) mapped the AH locus to chromosome 1q23.3-q24 by genome-wide linkage in three kindreds.
- **Risk factors.**
  - Genetic: the ADCY10 variants above. The only other bone association found was a modest ADCY10 polymorphism association with spinal areal BMD in premenopausal white women. This came from a 2010-era study in healthy adults, and I did not retrieve its citation.
  - Environmental: AH phenotype expression is modulated by dietary calcium, sodium, protein and oxalate, and by vitamin D status. I found no gene-specific data for these.
  - No gene-environment interaction data were found for ADCY10 and hypercalciuria.
- **Protective factors.** None specific to HCA2 found.

## 3. Phenotypes (HPO leads, all to be verified)

| Phenotype | HPO lead | Frequency / notes |
|---|---|---|
| Hypercalciuria | HP:0002150 | Defining feature; intestinal calcium hyperabsorption |
| Nephrolithiasis (calcium stones) | HP:0000787 | The recurrent-stone phenotype; frequency not quantified in what I retrieved |
| Reduced spine bone density / osteopenia | HP:0000938 (osteopenia) | Association with lower L2-L4 density reported in the Reed 2002 cohort; not firmly replicated |
| Normal serum calcium | none (normal finding) | Normal or suppressed PTH |

- **Onset and course.** Onset is typically in adulthood with recurrent episodic stones. I did not find a source for onset age or progression in HCA2 specifically.
- **Quality of life.** No data found.
- HP term IDs are from memory. Look each up in OLS or the term cache before binding.

## 4. Genetic and molecular information

- **Causal gene.** ADCY10 (hgnc ID not retrieved; look up in the cache; the KB uses lowercase `hgnc:`). Locus 1q24.2.
- **Variants.**
  - The 2002 study reported 18 substitutions in 12 patients. I could not confirm which were coding or splice versus intronic or promoter.
  - Variant classification (ACMG), gnomAD frequencies and functional consequence are not established from what I retrieved. I found no functional studies showing LOF or GOF.
  - Origin is presumably germline. I did not find any statement to the contrary.
- **Modifiers, epigenetics, chromosomal abnormalities.** Not available.
- **Naming trap.** Do not confuse ADCY10 with ADCY1-9 (transmembrane adenylyl cyclases) or with VDR/CLDN14/CASR/SLC34A1 genes, which are implicated in other hypercalciuria or stone phenotypes.

## 5. Environmental information

No gene-specific environmental, lifestyle or infectious factors were found. General hypercalciuria dietary modulators (sodium, protein, calcium intake) apply but should not be attached to HCA2 without a source.

## 6. Mechanism / pathophysiology

**Proposed causal chain (largely inferred, not demonstrated for ADCY10):**

1. A germline ADCY10 variant is hypothesized to alter sAC expression or activity (inferred; no functional study identified).
2. sAC generates cAMP in response to bicarbonate, calcium and ATP in tissues where it is expressed, including kidney and bone (osteoblasts), per the searched gene summaries.
3. Altered cAMP signaling is hypothesized to increase intestinal calcium absorption and/or renal calcium handling (unproven link).
4. Intestinal hyperabsorption leads to hypercalciuria.
5. Hypercalciuria leads to calcium stone formation.
6. In parallel, altered sAC signaling in bone is hypothesized to reduce bone density (low L2-L4 density was seen in the 2002 cohort; mechanism unknown).

**Gap statement.** Steps 1-3 and 6 have no demonstrated mechanism. The KB entry should record them as hypotheses. A `KNOWLEDGE_GAP` discussion is suitable, covering whether ADCY10 variants change sAC function and whether the intestine is the site of action.

- **Biology of sAC (background).** The enzyme belongs to a distinct class that is soluble and not regulated by G proteins or forskolin (NCBI summary via the searched pages). Lead GO terms: adenylate cyclase activity (GO:0004016), cAMP biosynthetic process (GO:0006171), bicarbonate-regulated signaling (look up). Lead CL terms: osteoblast (CL:0000062), renal tubular epithelial cell (look up).
- **Molecular profiling, single-cell, CRISPR screens.** Nothing relevant found.

## 7. Anatomical structures affected

- **Primary.** Intestine (calcium absorption), kidney (stone formation; urinary calcium excretion), and bone (reduced density).
- **UBERON leads:** kidney UBERON:0002113, small intestine UBERON:0002108, vertebral column/lumbar vertebra (look up).
- **Lateralization.** Not applicable (systemic, bilateral).

## 8. Temporal development

Adult-onset recurrent stone disease is typical for AH generally. No HCA2-specific natural-history data were found. Disease course is presumably chronic and lifelong with episodic stone events (inferred).

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant per OMIM-derived listings (HP:0000006). Penetrance, expressivity, founder effects, consanguinity and carrier frequency are not documented in what I found.
- **Epidemiology.**
  - No Orphanet or registry prevalence found for HCA2.
  - The 2002 cohort was Caucasian; no broader ancestry data were found.

## 10. Diagnostics

- **Laboratory.**
  - 24-hour urine calcium elevated, with normal serum calcium and PTH.
  - A calcium-load or fast/load test distinguishes absorptive from renal-leak hypercalciuria. This is the standard AH method (Pak's classification); no HCA2-specific paper retrieved.
- **Genetic testing.** ADCY10 appears on some PanelApp renal tubulopathy and calcium/phosphate panels. Because of the Amber/Red rating, a finding should be interpreted cautiously.
- **Imaging.** Renal ultrasound/CT for stones; DXA for bone density.
- **Differential.** Other causes of hypercalciuria, including primary hyperparathyroidism, renal-leak hypercalciuria, hypercalcemia of other causes, distal renal tubular acidosis, and monogenic stone disorders.

## 11. Outcome and prognosis

No HCA2-specific data. Complications are recurrent stones and possible bone loss.

## 12. Treatment

No HCA2-specific trials were found. General AH management (standard practice, not sourced here):

- Thiazide diuretics to reduce urinary calcium (NCIT:C15986 Pharmacotherapy; thiazide agent via `therapeutic_agent`).
- Potassium citrate; dietary sodium restriction and adequate (not restricted) calcium intake.
- Hydration.
- Stone procedures (NCIT:C15329 Surgical Procedure) as needed.

Pharmacogenomics, gene therapy and trials: none found.

## 13. Prevention

Tertiary prevention of stone recurrence through hydration, diet and thiazides. Genetic counseling is relevant for dominant inheritance, but the weak gene-disease evidence limits the interpretation of test results.

## 14. Other species

Not identified. The OMIA lookup was not run.

## 15. Model organisms

- A commercial conventional Adcy10 knockout mouse (C57BL/6J) exists (Cyagen). The vendor page gave no urinary calcium, bone or stone data.
- The best-known knockout phenotype in the literature is male infertility, because sAC is required for sperm motility (**[unverified]**, from memory). I found no mouse study of hypercalciuria, bone or stones.
- Do not cite a model as recapitulating HCA2 without a source. If the knockout is entered, use `FAILS_TO_RECAPITULATE` or `UNKNOWN`-fidelity wording only with evidence.

## Curation recommendations

1. Cache the Reed 2002 abstract with `just fetch-reference PMID:11932268`, then quote only the sentences it actually contains.
2. Record the ADCY10-HCA2 relationship as `SUSCEPTIBILITY`/uncertain, not `CAUSATIVE`. Note the Amber PanelApp rating and the single-study basis.
3. Search for a gnomAD constraint score, independent replication, a ClinVar assessment and sAC functional data before adding any mechanism node beyond the hypothesis group.
4. Fill the unsourced sections (epidemiology, treatment outcomes, models) only after verification.

Sources: [KEGG H02340](https://www.kegg.jp/entry/H02340), [DrugBank article A142174](https://go.drugbank.com/articles/A142174), [PanelApp UK ADCY10](https://panelapp.genomicsengland.co.uk/panels/878/gene/ADCY10/), [PanelApp AU](https://panelapp-aus.org/panels/192/gene/ADCY10), [MedGen C0342639](https://https.ncbi.nlm.nih.gov/medgen/C0342639), [GeneCards ADCY10](https://www.genecards.org/card/ADCY10), [Cyagen Adcy10 KO](https://www.cyagen.com/mouseatlas/S-KO-18917), [Wikipedia ADCY10](https://en.wikipedia.org/wiki/ADCY10).

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000787` (1 mention) - the report calls it "Nephrolithiasis (calcium stones)"; HP calls it **Kidney stone**, and lists "Nephrolithiasis" among its other names

Every term resolved, and every label the report gave matched.