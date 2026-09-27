---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-15T02:33:06.762440'
end_time: '2026-09-15T02:38:11.232640'
duration_seconds: 304.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ciguatera Fish Poisoning
  mondo_id: MONDO:0043230
  category: Environmental
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 16
  total_cost_usd: 1.2929635999999998
  session_id: edd440d3-b18f-53e7-aada-8026267dae7b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 46
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 38
  on_topic: 28
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 26
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001251
    reported_labels:
    - Peripheral neuropathy/paresis, ataxia
    ontology_label: Ataxia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ciguatera Fish Poisoning
- **MONDO ID:** MONDO:0043230 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Ciguatera Fish Poisoning** covering all of the
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

# Ciguatera Fish Poisoning — Comprehensive Research Report

## 1. Disease Information

**Overview.** Ciguatera fish poisoning (CFP, "ciguatera") is an acquired, foodborne marine-toxin illness caused by eating fish (rarely certain invertebrates) whose flesh has bioaccumulated ciguatoxins (CTXs) — heat-stable, lipophilic, polycyclic polyether neurotoxins produced by benthic dinoflagellates of the genera *Gambierdiscus* and *Fukuyoa*. It is not an infection and not a genetic disorder; it is an environmentally acquired toxicosis whose severity and phenotype depend on toxin dose, congener mixture, and host factors. CFP produces a characteristic triad of gastrointestinal, neurological, and cardiovascular manifestations that begins acutely (minutes to ~72 h post-ingestion) and, in a substantial minority of patients, evolves into a chronic, relapsing neurological syndrome lasting weeks to years (Friedman et al., *Marine Drugs* 2017, PMC5367029; PMID:19005579).

**Key identifiers.**
- **MONDO:** MONDO:0043230 (per curation target; MONDO models this as an acquired environmental disease, not a Mendelian disorder)
- **MeSH:** D036841, "Ciguatera Poisoning" (Tree Number C25.723.415.246) — https://meshb.nlm.nih.gov/record/ui?ui=D036841
- **ICD-10-CM:** T61.0- family — T61.01XA (accidental/unintentional, initial encounter), T61.02XA (intentional self-harm), T61.03XA (assault), T61.04XA (undetermined); ICD-11 should be searched under the poisoning-by-marine-animal/toxin chapter (NE61 exposure category)
- **OMIM:** none — CFP is not a Mendelian disease and has no OMIM phenotype entry, consistent with its purely acquired-toxicologic etiology
- **Orphanet:** not indexed as a distinct rare-disease entity in the searches performed here; CFP is more commonly catalogued in toxicology/food-safety resources (NORD does carry a consumer-oriented entry: https://rarediseases.org/rare-diseases/ciguatera-fish-poisoning/)
- **Synonyms:** ciguatera poisoning, ciguatera toxicosis, tropical fish poisoning, "ciguatera" (from Cuban Spanish *cigua*, referring to a marine snail once implicated); associated but distinct entities are scombroid poisoning, tetrodotoxin poisoning, and paralytic/neurotoxic/diarrhetic shellfish poisoning (PSP/NSP/DSP), which curators should not conflate with CFP despite overlapping "seafood poisoning" framing.

**Evidence base.** The bulk of the literature is aggregated disease-level clinical/epidemiological data (case series, outbreak investigations, retrospective cohort/registry analyses) rather than individual-patient EHR data — French Polynesia, Guadeloupe/Martinique, Hong Kong, Puerto Rico, Florida/CDC, and Pacific-island public-health datasets are the dominant sources (PMC4210881; PMC3339456; PMC5814543; PMC3236724; PMC9415704).

---

## 2. Etiology

**Disease causal factor.** CFP is caused exclusively by dietary ingestion of ciguatoxin-contaminated fish (occasionally other reef organisms) — it is a **toxin-mediated, environmental** disease with no infectious or Mendelian-genetic causal component. Ciguatoxins are secondary metabolites of epibenthic/epiphytic dinoflagellates in the genera *Gambierdiscus* (≥18 species, e.g., *G. polynesiensis*, *G. excentricus*, *G. australes*) and the sister genus *Fukuyoa*, which live on macroalgae and reef detritus in tropical/subtropical coral-reef ecosystems (PMC12854468; PMID:41610130). Herbivorous reef fish graze on toxin-laden algae; the biologically less-toxic precursor "gambiertoxins" are then oxidized by hepatic cytochrome P450 enzymes as they pass up the food chain into the far more potent ciguatoxins, which biomagnify in carnivorous apex reef predators (barracuda, grouper, snapper, moray eel, amberjack) (Mudge et al., *Chemosphere* 2023, PMID:37044143; Mudge et al., *Toxicon* 2024, PMID:38043714). Congeners differ by ocean basin: Pacific ciguatoxins (P-CTX-1, -2, -3), Caribbean ciguatoxins (C-CTX-1, -2), and Indian Ocean ciguatoxins (I-CTX) — a distinction relevant to potency and detection-assay cross-reactivity.

**Genetic risk factors.** No causal or susceptibility gene variants have been established for CFP; it is not modeled by ClinVar/GWAS as a genetic disease. There is no confirmed evidence of allelic variation in voltage-gated sodium channel genes (*SCN1A–SCN11A*) modulating human ciguatera susceptibility, although this is biologically plausible given the toxin's direct VGSC target and is an open research gap.

**Environmental risk factors:**
- Consumption of large, carnivorous, apex-predator reef fish (barracuda, grouper, snapper, moray eel, amberjack) from endemic tropical/subtropical reef waters (Caribbean, Pacific, and increasingly Macaronesia/East and Southeast Asia) (PMC5367029; PMID:31927300).
- Fish size/trophic position: larger, older predatory fish generally pose higher risk through biomagnification, though the size–toxicity relationship is site-specific and not a reliable universal predictor — fish weighing >2 kg accounted for >80% of Hong Kong CFP outbreak fish, but size was not predictive in French Polynesia (PMC9027493; ScienceDirect S0041010114000890).
- Consumption of fish liver, roe, or viscera, which concentrate CTX more than muscle.
- Sea-surface warming, coral-reef degradation, and habitat disturbance (storms, dredging, coastal construction) that promote *Gambierdiscus*/*Fukuyoa* proliferation on newly exposed algal substrate — climate-linked geographic range expansion of ciguatera risk zones is well documented (PMC12854468).
- Sex and age are not strong independent risk factors for exposure per se (risk tracks with who eats the implicated fish), though physiological factors (see below) modulate presentation.
- Repeated/sensitizing prior exposure: some evidence suggests prior ciguatera episodes lower the threshold for symptomatic recurrence on subsequent, even minor, toxin exposure ("sensitization") (PMC5367029).

**Protective factors.** No genetic protective alleles are established. The only well-supported "protective" factor is behavioral/environmental: avoidance of high-risk species/regions, avoidance of fish viscera, and (in some traditional Pacific practices) test-feeding to animals or ants before human consumption — none of which are validated, sensitive screening methods. There is no dietary or pharmacologic chemoprophylaxis with demonstrated efficacy.

**Gene–environment interactions.** None are established for CFP in the CTD/GxE literature; the dominant "interaction" reported is host-intrinsic pharmacodynamic variability (differential VGSC subtype expression/density in individual patients) rather than a documented allele-by-exposure interaction.

---

## 3. Phenotypes

CFP produces a multi-system, largely episodic/acute syndrome with a distinctive delayed-onset chronic neurological tail. Onset is typically 30 minutes–24 hours after ingestion (range 15 min–72 h) (PMC5367029; Louisiana DOH manual).

**Gastrointestinal (earliest, usually first 24 h, self-limited over 1–2 days):**
- Nausea (HP:0002018), Vomiting (HP:0002013), Diarrhea (HP:0002014), Abdominal pain/cramps (HP:0002027) — very frequent (>70–90% of cases)

**Neurological (may begin with or shortly after GI symptoms; can persist weeks–months–occasionally years):**
- Paresthesia (HP:0003401) — tingling of lips, tongue, extremities
- **Cold–hot temperature (thermal) allodynia/reversal** — the pathognomonic feature: cold objects feel burning-hot and hot objects feel cold; there is no single dedicated HPO term, but this is best mapped under abnormal thermal sensation (consider HP:0031000-type "sensory neuropathy" branches, or free-text with `Cold-induced dysesthesia`)
- Pruritus (HP:0000989), often severe and exacerbated by alcohol
- Myalgia (HP:0003326), Arthralgia (HP:0002829)
- Peripheral neuropathy/paresis, ataxia (HP:0001251) in severe cases
- Headache (HP:0002315)
- Blurred vision (HP:0000622), photophobia
- Dysgeusia/metallic or unusual taste sensations
- Dental pain or sensation of "loose teeth"
- Dysuria (painful urination)
- Sleep disturbance, nightmares, and rarely hallucinations
- Anxiety (HP:0000739) and Depression (HP:0000716) are reported, particularly with chronic ciguatera

**Cardiovascular (typically appear within the first day, can be life-threatening in severe cases):**
- Bradycardia (HP:0001662), Hypotension (HP:0002615), and cardiac arrhythmia — reviewed as an underappreciated but potentially serious complication (Cardiovascular Complications in Ciguatera Fish Poisoning, PMID:22574244)

**Constitutional:** fatigue (HP:0012378), diaphoresis/excessive sweating, chills

**Dermatological (less common, described in case reports):** chronic dermatitis with episodic erythema following ciguatoxin exposure (PMC10562083)

**Phenotype characteristics:**
- **Onset:** acute, hours after a single contaminated meal; no congenital or pediatric-specific onset pattern (any age can be affected, generally correlating with reef-fish consumption).
- **Severity:** dose-dependent, ranging from mild self-limited GI upset to severe, occasionally fatal, cardiovascular/respiratory compromise; case-fatality is low (<0.1% of reported cases) (PMC5367029).
- **Progression/course:** classically triphasic — acute GI phase (day 1–2) → acute-subacute neurological/cardiovascular phase (days–weeks) → chronic ciguatera phase in ~20% of patients, with fluctuating fatigue, myalgia, and pruritus persisting months to years (ScienceDirect S1080603223000030; PMC8472944).
- **Frequency among affected individuals:** GI symptoms in the large majority (>70–90%); neurological symptoms in most symptomatic patients; cold–hot reversal is frequently cited as characteristic but is not universal; cardiovascular signs are less common but clinically important.
- **Quality-of-life impact:** chronic ciguatera syndrome (fatigue, pruritus, dysesthesias, and psychiatric symptoms lasting months–years) can be markedly disabling; no validated disease-specific QoL instrument was identified, though generic instruments (EQ-5D, SF-36) have been used in adjacent seafood-toxin research.

Suggested HPO terms: HP:0002018, HP:0002013, HP:0002014, HP:0002027, HP:0003401, HP:0000989, HP:0003326, HP:0002829, HP:0001251, HP:0002315, HP:0000622, HP:0001662, HP:0002615, HP:0012378, HP:0000739, HP:0000716.

---

## 4. Genetic/Molecular Information

CFP has **no causal Mendelian gene** — this section is largely not applicable in the conventional sense used for inherited disease curation:
- **Causal genes:** none (environmental toxin exposure, not a germline or somatic mutation).
- **Pathogenic variants:** not applicable; there is no ClinVar/HGMD entry for "ciguatera."
- **Somatic vs. germline:** not applicable.
- **Modifier genes:** none confirmed in humans, though differential expression/density of voltage-gated sodium channel (VGSC) subtypes (*SCN1A*/Na_V1.1, *SCN9A*/Na_V1.7, *SCN10A*/Na_V1.8, *SCN11A*/Na_V1.9) across peripheral sensory neurons plausibly modulates individual symptom phenotype (see mechanism, below) but this is inferred from channel pharmacology, not from human genetic-association studies.
- **Epigenetics:** no disease-specific epigenetic studies identified.
- **Chromosomal abnormalities:** not applicable.

**What *is* molecularly characterized is the toxin itself**, which is the appropriate target of curation:
- Ciguatoxins are cyclic polyether compounds (13–14 fused ether rings), biosynthesized from precursor "gambiertoxins"/"gambierol"-type compounds by *Gambierdiscus*/*Fukuyoa*, and oxidatively activated in fish liver by cytochrome P450 enzymes (PMID:37044143; PMID:38043714).
- Major human-relevant congeners: P-CTX-1 (most potent, Pacific), P-CTX-2, P-CTX-3, C-CTX-1/-2 (Caribbean), I-CTX (Indian Ocean); related toxins from the same dinoflagellates include maitotoxin and gambierone.
- Molecular target: voltage-gated sodium channel (VGSC) **site 5** on the α-subunit (CHEBI/GO terms below); ciguatoxins act as **allosteric agonists**, not channel blockers.

---

## 5. Environmental Information

**Environmental factors (primary etiological axis for this disease):**
- Toxin-producing benthic dinoflagellates *Gambierdiscus* spp. and *Fukuyoa* spp. — taxonomically Dinophyta/Alveolata — colonizing dead coral, turf algae, and macroalgal surfaces in tropical/subtropical reef systems (PMC12854468; PMC8473099).
- Reef disturbance (storms, bleaching, dredging, construction) that increases algal substrate available for dinoflagellate colonization.
- Sea-surface temperature rise and broader climate change, associated with geographic range expansion of *Gambierdiscus*/*Fukuyoa* into temperate-adjacent waters (e.g., Macaronesia/Canary Islands, parts of East/Southeast Asia and even isolated temperate detections) (PMC12854468; PMC7761829; ScienceDirect topic review S1568988324001689).
- Regional/seasonal variation in toxin production tied to nutrient availability and pH (PMC7761829).

**Lifestyle factors:**
- Dietary reliance on reef fish (subsistence/artisanal fishing communities in the Pacific and Caribbean bear disproportionate risk).
- Recreational/tourist consumption of reef fish (grouper, barracuda, snapper) in endemic regions, including via imported/exported fish in non-endemic countries (documented urban outbreaks, e.g., New York City, CDC MMWR 2010–2011).
- Post-exposure dietary triggers of relapse: alcohol, caffeine, nuts/nut oils, chocolate, chicken, eggs, and reef fish/fish sauces are widely reported (though mechanistically unproven) to provoke recurrence of neurological symptoms for up to 6 months after the index poisoning; patients are counseled to avoid these for ~6 months (Poison Control; CDPH fact sheet; StatPearls NBK482511).

**Infectious agents:** none — CFP is not infectious and is not caused by bacteria, viruses, fungi, or parasites; it must be distinguished from bacterial seafood-associated illnesses (e.g., *Vibrio* spp.) and from scombroid (histamine) poisoning, which share an overlapping consumption context but a distinct toxin/mechanism.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered)

1. **Dinoflagellate toxin production** — *Gambierdiscus*/*Fukuyoa* spp. biosynthesize gambiertoxin/CTX precursors on reef algal substrate → these enter the marine food web via herbivorous grazing.
2. **Trophic biotransformation and biomagnification** — hepatic cytochrome P450 oxidation in herbivorous and omnivorous fish converts precursor toxins into more potent ciguatoxins, which accumulate preferentially in the liver, viscera, and (to a lesser but still hazardous degree) muscle of predatory reef fish → **leads to** highly concentrated CTX burden in apex-predator fish flesh consumed by humans.
3. **Ingestion and absorption** — human consumption of contaminated fish → CTX is absorbed across the gastrointestinal epithelium (lipophilic, heat-stable — cooking does **not** inactivate it) → **leads to** systemic distribution to excitable tissue (enteric neurons, peripheral sensory/autonomic neurons, cardiac conduction tissue, CNS).
4. **Molecular target engagement** — CTX binds with picomolar–nanomolar affinity as an allosteric agonist at **neurotoxin receptor site 5** on the α-subunit of voltage-gated sodium channels (VGSCs), across multiple Na_V subtypes (Na_V1.1, Na_V1.6, Na_V1.7, Na_V1.8, Na_V1.9) with differential subtype selectivity (PMC5320492; PMC5618408) → **causes** a hyperpolarizing shift in the voltage-dependence of channel activation, slowed/incomplete inactivation, and increased channel open-probability at (or near) resting membrane potential.
5. **Neuronal/cardiac hyperexcitability** — this shift **results in** spontaneous, repetitive firing of peripheral sensory afferents, enteric neurons, autonomic fibers, and cardiac pacemaker/conduction cells, together with **sodium- and secondary calcium-influx-driven depolarization** and axonal swelling (PMC7602189; ScienceDirect chapter S2468748021000059).
6. **Downstream cellular consequences** — sustained Na⁺/Ca²⁺ influx **activates** intracellular calcium-dependent signaling cascades → **leads to** oxidative stress, mitochondrial dysfunction, and (in sustained/high-dose exposure) neuroinflammatory signaling and neuronal injury; CTX also inhibits delayed-rectifier and A-type K⁺ currents in dorsal root ganglion (DRG) neurons, **further amplifying** excitability (PMC4744673).
7. **Neuropeptide release / neurogenic inflammation** — calcium-influx-dependent release of **CGRP (calcitonin gene-related peptide)** from sensory afferents (via Na_V1.9/Na_V1.7/Na_V1.1 activation) **triggers** local neurogenic vasodilation and can propagate systemic autonomic effects, in part via a nitroxyl/TRPA1-linked pathway (PMC5618408).
8. **Organ-level manifestations (branching):**
   - **Enteric nervous system branch:** hyperexcitability of enteric/autonomic neurons → **produces** the early gastrointestinal phase (nausea, vomiting, diarrhea, cramping).
   - **Peripheral sensory neuron branch:** DRG/peripheral nerve hyperexcitability and altered cold-thermoreceptor (likely TRPM8/TRPA1-modulated) signaling → **produces** paresthesia, pruritus, myalgia, and the pathognomonic cold–hot temperature-reversal sensation, an effect experimentally reproduced as **ionic cold-hypersensitivity of spinal neurons** in ciguatera models (PMC4744673).
   - **Cardiac conduction branch:** VGSC-mediated hyperexcitability and altered autonomic tone acting on cardiac pacemaker/conduction tissue and vascular smooth muscle → **produces** bradycardia, hypotension, and arrhythmia (PMID:22574244).
   - **CNS branch (higher-dose/prolonged exposure):** CNS penetration and neuroinflammatory/neuroprotective transcriptional responses have been demonstrated in a murine brain gene-expression model after CTX-1 exposure, showing an acute anti-inflammatory, neuroprotective transcriptional signature superimposed on the excitotoxic insult (*BMC Neuroscience* 2010, "Gene expression profiling in brain of mice exposed to the marine neurotoxin ciguatoxin reveals an acute anti-inflammatory, neuroprotective response") — this is a **model-organism (mouse)** finding and its direct translational fidelity to the human chronic syndrome is not established (flagged as a human–model mismatch candidate).
9. **Chronic phase (inferred, mechanistically less well characterized)** — persistent low-level channel dysregulation, sensitized nociceptive circuitry, and/or ongoing neuroinflammation are hypothesized to underlie the **chronic ciguatera syndrome** (fatigue, relapsing dysesthesia/pruritus, psychiatric symptoms lasting months–years), but the mechanistic basis of chronicity itself is **inferred rather than directly demonstrated** in humans (PMC8472944).

### Category detail

- **Molecular pathways:** VGSC site-5 allosteric agonism (GO:0005248 voltage-gated sodium channel activity; consider GO:0086006 for cardiac-specific VGSC activity in cardiac myocytes); downstream calcium-signal transduction (GO:0006816 calcium ion transport); CGRP-mediated neurogenic inflammation pathway.
- **Cellular processes:** neuronal hyperexcitability/repetitive firing, calcium-dependent neuropeptide exocytosis, oxidative stress response (relevant GO: GO:0006979 response to oxidative stress), and (in model systems) an acute neuroinflammatory/neuroprotective transcriptional program (GO:0006954 inflammatory response).
- **Protein dysfunction:** not a structural protein-misfolding disease; the relevant "dysfunction" is pharmacological/functional gain-of-activity at the wild-type VGSC protein (allosteric agonism), not a mutation-driven loss/gain of function — i.e., this is analogous to the dismech convention of `modifier: GAIN_OF_FUNCTION` applied to a **non-genetic**, toxin-driven activity state of ion-channel function, since there is no host variant to anchor a `functional_impact_category`.
- **Metabolic changes:** hepatic cytochrome P450–mediated oxidative bioactivation occurs in the **fish**, not the human host; in the poisoned human, no distinct primary metabolic disease process has been characterized beyond the downstream oxidative-stress cascade above.
- **Immune system involvement:** neuroinflammatory signaling is implicated as a downstream amplifier (see above); CFP is not an autoimmune or immunodeficiency-related disease.
- **Tissue damage mechanisms:** oxidative stress and calcium-overload-mediated neuronal/axonal injury in peripheral sensory neurons; no established necrotic/fibrotic end-organ damage pattern in survivors, consistent with the largely functional/reversible nature of the toxicosis.
- **Biochemical abnormality:** functional ion-channel dysregulation (VGSC gain-of-activity) rather than an enzyme deficiency or receptor structural defect.
- **Molecular profiling:** disease-specific human transcriptomic/proteomic/metabolomic datasets were not identified in this search; the only omics-level data found is the murine brain transcriptomic study cited above (model-organism, not human).
- **Single-cell/spatial/multi-omics:** none identified for CFP specifically.

**Suggested GO terms:** GO:0005248 (voltage-gated sodium channel activity), GO:0086006 (voltage-gated sodium channel activity involved in cardiac muscle cell action potential), GO:0006816 (calcium ion transport), GO:0006979 (response to oxidative stress), GO:0006954 (inflammatory response), GO:0019233 (sensory perception of pain).
**Suggested CL terms:** CL:0000101 (sensory neuron), a dorsal root ganglion sensory neuron term, CL:0000540 (neuron, generic), CL:0000746 (cardiac muscle cell), CL:0000192 (smooth muscle cell) for vascular effects. *(Exact CL CURIEs should be re-verified against the current Cell Ontology before binding — not confirmed via direct ontology lookup in this research pass.)*

---

## 7. Anatomical Structures Affected

- **Organ level:**
  - Primary: gastrointestinal tract (stomach, intestine), peripheral nervous system, cardiovascular system (heart, vasculature)
  - Secondary/complication-level: skin (pruritus, rare chronic dermatitis, PMC10562083), genitourinary system (dysuria), CNS (headache, sleep disturbance, rare hallucinations), musculoskeletal system (myalgia/arthralgia)
  - Body systems involved: digestive, peripheral/autonomic nervous, cardiovascular, integumentary, and (in chronic disease) psychiatric/behavioral
- **Tissue/cell level:** enteric neurons and gut epithelium; peripheral sensory (dorsal root ganglion) neurons and unmyelinated/thinly myelinated afferent fibers; cardiac conduction-system and pacemaker cells; vascular smooth muscle
- **Subcellular level:** plasma-membrane voltage-gated sodium channel complexes (site 5); relevant GO Cellular Component: GO:0005886 (plasma membrane), GO:0034706 (sodium channel complex); downstream mitochondrial oxidative-stress involvement (GO:0005739 mitochondrion)
- **Localization:** diffuse/systemic rather than focal — bilateral, symmetric sensory disturbances are typical (no reported lateralization pattern)

**Suggested UBERON terms:** UBERON:0001555 (digestive tract), UBERON:0000010 (peripheral nervous system), UBERON:0002240 (spinal cord, for DRG-adjacent structures), UBERON:0000948 (heart), UBERON:0001981 (blood vessel), UBERON:0002097 (skin of body).

---

## 8. Temporal Development

- **Onset:** acute, dose- and toxin-load-dependent, typically 30 min–24 h (range 15 min–72 h) after ingestion of contaminated fish; no congenital, pediatric-specific, or age-restricted onset — onset timing is exposure-anchored, not developmental (PMC5367029; Louisiana DOH).
- **Progression:**
  - **Stage 1 — Acute gastrointestinal phase:** hours 0–24–48; nausea/vomiting/diarrhea/cramping, typically self-limited.
  - **Stage 2 — Acute neurological/cardiovascular phase:** overlapping with or shortly following Stage 1, lasting days to a few weeks; paresthesia, thermal reversal, pruritus, myalgia, bradycardia/hypotension.
  - **Stage 3 — Chronic ciguatera phase:** in an estimated ~20% of patients, fluctuating fatigue, myalgia, pruritus and neuropsychiatric symptoms persisting months to occasionally years (ScienceDirect S1080603223000030; PMC8472944).
- **Progression rate:** variable — most cases resolve fully within 3–6 weeks; a substantial minority progress to the chronic phase.
- **Disease course pattern:** predominantly self-limited/acute with a recognized relapsing-remitting chronic tail; recurrences can be re-triggered by re-exposure to trigger foods/beverages (alcohol, caffeine, nuts, fish) even long after the index poisoning.
- **Disease duration:** self-limited in the majority; chronic/lifelong-feeling course (though generally not permanently disabling) in a minority; rare reports describe permanent nerve damage.
- **Remission:** spontaneous in most cases; symptomatic treatment (mannitol acutely; amitriptyline/gabapentinoids for chronic neuropathic symptoms) may shorten or ameliorate — but not clearly cure — the course.
- **Critical periods/windows for intervention:** early administration of IV mannitol (within the first 24–48 h) is reported anecdotally to produce the most dramatic neurological improvement, though rigorous trial evidence is lacking (see Diagnostics/Treatment sections).

---

## 9. Inheritance and Population

**Inheritance pattern:** none — CFP is an acquired environmental toxicosis, not a heritable disease. Penetrance, expressivity, anticipation, germline mosaicism, founder effects, consanguinity, and carrier frequency are **not applicable**.

**Epidemiology:**
- CFP is considered the most prevalent phycotoxin-related seafood poisoning worldwide, with global burden estimates commonly cited at **~20,000–50,000 cases/year** (PMID:31927300; PMC5367029; NORD).
- Regional incidence:
  - French Polynesia: annual incidence ~18/10,000 population (2016)
  - Guadeloupe (French West Indies), 2013–2016: mean annual incidence 1.47/10,000 — roughly 5-fold higher than the 1996–2006 baseline for the same territory (PMC5814543)
  - Hong Kong: distinct, well-documented urban import-related outbreaks tied to specific high-risk reef fish species (PMC4210881)
  - Puerto Rico (Culebra): incidence surveys in 2005–2006 (PMC3339456)
  - Pacific Islands overall: substantial burden documented over 1998–2008 (PMC3236724)
- True prevalence/incidence is widely regarded as **significantly underestimated** due to under-recognition of symptoms, absence of routine surveillance in many endemic regions, and reporting reluctance (tourism-economy concerns) (PMC5367029).
- Case-fatality is low, <0.1% of reported cases.

**Population demographics:**
- Affected populations are geographically rather than ethnically defined — coastal/island communities dependent on reef fishing (Pacific Islands, Caribbean) bear the highest burden; travelers/tourists to endemic regions and consumers of imported reef fish in non-endemic countries (documented US mainland and European outbreaks) are also affected.
- **Geographic distribution:** historically endemic in the tropical/subtropical Pacific and Caribbean; documented range expansion since ~2000 into Macaronesia (Canary Islands, Madeira/Selvagens) and East/Southeast Asian waters, plausibly climate-change-linked (PMC12854468; PMC8402339; PMC3367630 [Canary Islands]).
- **Sex ratio:** no strong, consistently reported sex-based susceptibility differential was identified; risk tracks with consumption patterns of implicated fish rather than intrinsic sex-linked biology.
- **Age distribution:** all ages affected; severity in some reports is greater in young children and elderly patients, plausibly reflecting body-weight-normalized dose and comorbidity burden, though this was not rigorously quantified across the sources reviewed here.

---

## 10. Diagnostics

**Clinical diagnosis** is predominantly based on the characteristic symptom triad (GI → neurological → cardiovascular) with a temporally plausible exposure history to a high-risk reef fish species; no single confirmatory bedside clinical test exists.

**Laboratory/biomarker and toxin-detection tests (mainly applied to the *fish*, not the patient, for outbreak confirmation/regulatory screening):**
- **Mouse bioassay (MBA):** historically the reference method for detecting CTX-group toxins in fish tissue but increasingly disfavored on animal-welfare grounds and for poor specificity/limited sensitivity; the EU CONTAM Panel has explicitly called for validated alternatives.
- **Receptor-binding assay (RBA):** competition binding between CTX and radiolabeled or fluorescently labeled brevetoxin-2 for VGSC site 5; a fluorescence-based RBA (RBA_F) was developed as a non-radioisotope alternative (PMC4830512; PMC10818520); a chemiluminescent acridinium-brevetoxin ligand assay has also been evaluated (PMC6833909).
- **Cell-based assays (CBA):** neuroblastoma (N2a) and other neuronal cell lines exploit CTX's VGSC-agonist cytotoxicity; a human SH-SY5Y neuronal cell assay has been used as an in-vitro toxicity model (ScienceDirect S1382668917301011).
- **ELISA/immunoassay:** sandwich ELISA and the Hokama "stick test" enzyme immunoassay have been used for fish-tissue screening, with newer fluorescence-based sandwich ELISA formats reaching detection limits compatible with the FDA guidance level of 0.01 ppb (10 ppt) for CTX1B in fish (PMID:18623118; PMC4830512).
- **Analytical chemistry:** LC-MS/MS is increasingly used as a specific, quantitative confirmatory method for CTX congeners in fish tissue in reference laboratories.
- There is **no validated, widely available clinical (human-serum/urine) biomarker assay** for confirming ciguatera in a patient; diagnosis in clinical practice remains syndromic.

**Imaging/functional/electrophysiology:** not disease-specific; nerve conduction studies may show findings consistent with a sensory neuropathy in patients with prolonged neurological symptoms, but no CFP-specific electrophysiologic signature was identified in this search.

**Genetic testing:** not applicable — there is no genetic test for CFP.

**Clinical criteria/differential diagnosis:** CFP must be differentiated from scombroid (histamine) poisoning, paralytic/neurotoxic/diarrhetic/amnesic shellfish poisoning, tetrodotoxin poisoning, and Guillain-Barré syndrome or other acute peripheral neuropathies when the ingestion history is unclear.

**Screening:** no population-level screening program exists for asymptomatic individuals; the primary "screening" that occurs is regulatory/food-safety testing of harvested reef fish (see Prevention).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** generally excellent; case-fatality <0.1% of reported cases (PMC5367029). Death, when it occurs, is typically attributable to severe cardiovascular collapse or respiratory compromise in high-dose exposures.
- **Morbidity:** acute morbidity from the GI/neurological/cardiovascular triad is usually self-limited (resolution in 3–6 weeks); chronic ciguatera syndrome (fatigue, myalgia, pruritus, dysesthesia, anxiety/depression) affects up to ~20% of symptomatic patients and can persist for months to years, with meaningful impact on daily functioning (ScienceDirect S1080603223000030; PMC8472944).
- **Predictors of chronicity:** an exploratory hospital-based analysis from French Polynesia sought predictors of chronic ciguatera among hospitalized cases (PMC8472944); specific predictive factors identified there should be reviewed directly for detailed curation, but broadly, higher initial symptom severity and possibly repeated prior exposure are implicated as risk factors for chronic evolution.
- **Recovery potential:** most patients recover fully; a minority experience prolonged/relapsing dysesthesia, and rare reports describe permanent peripheral nerve injury.
- **Complications:** dehydration (from GI losses), cardiovascular instability requiring monitoring/support in severe cases, and psychosocial/occupational impact from chronic symptoms.
- **Prognostic factors:** initial toxin dose, congener/toxin mixture, individual sensitization from prior episodes, and possibly timing of treatment (early mannitol administration is anecdotally associated with more rapid neurological improvement, though this is not established by rigorous trial evidence — see below).

---

## 12. Treatment

**No specific antidote exists.** Management is supportive and symptomatic.

**Pharmacotherapy:**
- **Intravenous mannitol** (osmotic diuretic, NCIT treatment-term candidate: dietary/osmotic agent category) — the most extensively reported specific intervention: supported by four uncontrolled case series, one unblinded comparative trial, and multiple case reports describing rapid (within minutes to days) reduction in neurological symptoms when given early; however, the only randomized, double-blind controlled trial found **no significant benefit over normal saline**, and mannitol carries its own adverse-effect profile. Net evidence is therefore mixed/inconclusive, and mannitol is **not established as clearly superior** to supportive care (Clinical Toxicology 2017, tandfonline 10.1080/15563650.2017.1327664; PMC2579736).
- **Amitriptyline** (tricyclic antidepressant) — reported in case series/reports to relieve pruritus, dysesthesia, and chronic neuropathic pain; considered most useful for the **chronic** neurological phase, generally requiring prolonged treatment to sustain benefit.
- Other agents used with variable, case-report-level success for chronic neuropathic symptoms: **gabapentin, pregabalin, fluoxetine, duloxetine, tocainide** (a sodium-channel-blocking antiarrhythmic) (emedicine.medscape.com/article/813869-medication).
- Symptomatic supportive medications: antiemetics and antidiarrheals for GI symptoms; antihistamines for pruritus; NSAIDs/analgesics for myalgia/arthralgia; atropine for symptomatic bradycardia; IV fluids for volume support/hypotension.
- No approved pharmacogenomic guidance exists (not a PharmGKB/CPIC-covered condition).

**Advanced therapeutics:** gene therapy, cell therapy, RNA-based therapies, targeted therapies, and immunotherapies are **not applicable** to CFP; investigational small-molecule work includes rosmarinic acid and derivatives, patented for potential ciguatera treatment (US Patent 9060985), though clinical efficacy data were not identified in this search.

**Surgical/interventional:** none indicated; management is medical/supportive.

**Supportive/rehabilitative care:** hydration, symptom-targeted medication, and — for patients with prolonged neuropathic symptoms — potential benefit from standard chronic-pain rehabilitative approaches (physical therapy for myalgia/weakness), although disease-specific rehabilitation protocols were not identified.

**Experimental/clinical trials:** no active, disease-specific registered clinical trials with NCT identifiers were identified in this search; the one randomized controlled trial identified addressed mannitol vs. saline (cited above) but a specific NCT number was not surfaced by the search tools used.

**Treatment outcomes:** none of the pharmacologic agents studied (mannitol, TCAs, gabapentinoids, tocainide) has demonstrated clear superiority over another in controlled comparison; evidence quality across the board is low (predominantly case reports/series).

**Treatment strategy:** no formal clinical-practice-guideline algorithm was identified; management is empirical/symptom-driven, generally: supportive care first line → consider early mannitol for significant neurological symptoms (with informed acknowledgment of equivocal trial evidence) → TCA/gabapentinoid for persistent/chronic neuropathic symptoms → dietary trigger avoidance (fish, alcohol, caffeine, nuts) for up to 6 months post-episode to reduce relapse risk.

**Suggested NCIT terms:** NCIT:C15747 (Supportive Care), NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bindings for mannitol, amitriptyline, gabapentin, pregabalin, duloxetine, and tocainide (each should be verified against CHEBI/NCIT before binding).

---

## 13. Prevention

- **Primary prevention:** avoidance of high-risk reef-fish species (barracuda, grouper, snapper, moray eel, amberjack, and in some regions parrotfish/triggerfish) sourced from known or suspected ciguatera-endemic waters; avoidance of fish liver, viscera, and roe. The **FAO/WHO Codex Alimentarius Code of Practice for the Prevention or Reduction of Ciguatera Poisoning (CXC 83-2024)** provides the current international framework for producer/processor-level risk reduction. In the US, the **FDA has issued guidance for primary seafood processors** to obtain harvest-location information for reef fish (grouper, amberjack, snapper, lionfish, king mackerel, barracuda) to assess ciguatoxin risk before distribution.
- **No reliable field test exists for consumers** — ciguatoxin is odorless, tasteless, and heat-stable, so neither sensory inspection nor cooking prevents intoxication. Traditional folk tests (ant/animal test-feeding) are not validated and are not recommended as safety measures.
- **Secondary prevention/screening:** regulatory-level fish testing using receptor-binding assays, ELISA, or LC-MS/MS in processing/export facilities in some jurisdictions; no population-based human screening program exists.
- **Tertiary prevention:** post-episode dietary counseling to avoid known relapse-triggering foods/beverages (fish, alcohol, caffeine, nuts, chocolate, chicken, eggs) for approximately 6 months to reduce symptom recurrence.
- **Immunization:** not applicable — no vaccine exists or is biologically relevant to a small-molecule toxin exposure of this kind.
- **Genetic counseling/screening:** not applicable.
- **Public health interventions:** harmful-algal-bloom (*Gambierdiscus*/*Fukuyoa*) monitoring programs in some endemic regions; public health education campaigns in endemic Pacific/Caribbean territories; import controls and species-specific fishing advisories/bans in some high-risk locales.
- **Environmental interventions:** reef conservation to limit the coral/algal disturbance that promotes toxin-producing dinoflagellate proliferation is a plausible upstream intervention, though not a formal "prevention program" in the clinical sense.
- **Prophylaxis:** no drug or procedure is established for chemoprophylaxis before consumption of at-risk fish.

---

## 14. Other Species / Natural Disease

- **Taxonomy of susceptible hosts:** any vertebrate consuming ciguatoxic fish is potentially susceptible; documented naturally occurring CFP has been best characterized in **companion animals** — dogs (*Canis lupus familiaris*, NCBITaxon:9615) and cats (*Felis catus*, NCBITaxon:9685) — in the Cook Islands, where a three-part descriptive series (2011–2017 clinic records; 246 cases, 165 dogs and 81 cats) characterized demographic/temporal/spatial distribution, exposure history and case definition, and treatment/outcome (PMC7020132 / PMID:32158145; PMC7096299; PMC7429383 / PMID:32848300).
- **Natural disease and veterinary relevance:** in dogs and cats, CFP presented as a multisystem toxicosis dominated by **motor dysfunction** (ataxia, paresis/paralysis, recumbency being common), with respiratory and gastrointestinal involvement especially prominent in dogs; reef/lagoon fish and moray eels were the most commonly implicated exposure sources. Treatment was primarily supportive (fluid therapy, muscle relaxants); survival exceeded 90%, with most fatalities occurring in the first week and average hospitalization of ~12.9 days.
- **Comparative pathology:** the canine/feline presentation — dominated by motor/ataxic signs rather than the human-predominant sensory/GI triad — illustrates a **species-dependent phenotype divergence** attributable to differences in diet (scavenging fish carcasses/viscera, higher relative dose), body size/dose-normalization, and possibly differential VGSC subtype distribution across species; this is a notable point for any comparative-pathology or cross-species pathograph annotation.
- **Zoonotic potential/transmission:** CFP is not transmissible between animals or from animal to human by contact — both human and animal cases arise independently from ingestion of toxin-contaminated fish, so this is a **shared environmental exposure**, not zoonotic transmission in the classical sense.
- **Orthologous genes:** the molecular target (VGSC α-subunits) is highly conserved across vertebrates (fish, mammals), which is why fish themselves, along with mammals, are susceptible to CTX pharmacodynamics — this cross-species conservation underlies the utility of animal/cell models (see below).

---

## 15. Model Organisms

- **Mouse (in vivo):** the traditional **mouse bioassay (MBA)** has been the historical reference method for detecting CTX-class toxins in fish extract, based on lethality/toxicity scoring, but is increasingly disfavored for animal-welfare and specificity/sensitivity reasons (EU CONTAM Panel). Separately, **murine brain gene-expression profiling after CTX-1 exposure** demonstrated an acute anti-inflammatory, neuroprotective transcriptional response superimposed on the excitotoxic insult (*BMC Neuroscience*, 2010) — a mechanistic (not diagnostic) mouse model.
- **Rodent dorsal root ganglion (DRG)/spinal neuron electrophysiology models:** ex vivo/in vitro rodent sensory-neuron preparations have been used to demonstrate CTX-induced ionic mechanisms of **cold hypersensitivity**, directly modeling the human thermal-reversal phenotype (PMC4744673), and to show multiple Na_V-subtype involvement in CTX pathophysiology (PMC5320492) and CGRP release (PMC5618408).
- **Cell-based (in vitro) models:**
  - Mouse **neuroblastoma (N2a) cell-based assay (CBA)** — the most widely used in vitro surrogate for CTX potency/toxicity screening.
  - **Human SH-SY5Y neuronal cell line** — used to demonstrate potent cytotoxic effects of P-CTX-3C, providing a human-cell in vitro toxicity model (ScienceDirect S1382668917301011).
  - Heterologous expression systems (e.g., Xenopus oocytes or mammalian cell lines expressing individual cloned Na_V subtypes) underlie the subtype-selectivity electrophysiology studies cited above (PMC5320492).
- **Zebrafish:** no CFP/ciguatoxin-specific zebrafish study was identified in this search, though zebrafish are an established general platform for neurotoxin/venom screening and represent a plausible, currently underexploited model for ciguatoxin research given their genetic tractability and high-throughput behavioral assays.
- **Model limitations:** the mouse bioassay's poor specificity/sensitivity and animal-welfare concerns are explicitly noted as drivers for developing alternative (receptor-binding, cell-based, immunoassay) methods. No model fully recapitulates the human **chronic ciguatera syndrome** — chronicity itself has not been modeled in any organism identified in this search, representing a clear translational/human-model-mismatch gap worth flagging in any dismech `discussions` block (`kind: HUMAN_MODEL_MISMATCH`) if this disease is curated.
- **Applications:** current models are used almost exclusively for (a) toxin detection/potency quantification in fish (regulatory/food-safety use) and (b) acute electrophysiological/mechanistic dissection of VGSC-subtype pharmacology and peripheral sensory hyperexcitability — not for therapeutic drug screening or for modeling the chronic human syndrome.

---

## Summary of Key Evidence Gaps for Curation

1. No confirmed human genetic-susceptibility literature exists — any curated `genetic` block should record this as an absence rather than infer VGSC-gene involvement from toxin pharmacology alone.
2. Chronic ciguatera syndrome pathophysiology is mechanistically under-characterized in humans and has no established animal model — a strong `HUMAN_MODEL_MISMATCH` candidate.
3. Mannitol's efficacy remains genuinely contested (RCT-negative vs. case-series-positive) — evidence should be curated with explicit `SUPPORT`/`REFUTE` items from both the RCT and the case-series literature rather than presenting mannitol as established therapy.
4. Exact CHEBI/GO/CL/UBERON CURIEs proposed above are suggestions based on general biology and were **not individually confirmed via a live ontology lookup** in this research pass — per standard curation practice, each should be re-verified (e.g., via OAK/`runoak`) before being written into a KB entry, rather than bound from this report directly.

---

### Sources

- [Ciguatoxins Evoke Potent CGRP Release by Activation of Voltage-Gated Sodium Channel Subtypes NaV1.9, NaV1.7 and NaV1.1 (PMC5618408)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5618408/)
- [Multiple sodium channel isoforms mediate the pathological effects of Pacific ciguatoxin-1 (PMC5320492)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5320492/)
- [Algal ciguatoxin identified as source of ciguatera poisoning in the Caribbean (PMC10201850, PMID:37044143)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10201850/)
- [3-Epimers of Caribbean ciguatoxins in fish and algae (PMID:38043714)](https://pubmed.ncbi.nlm.nih.gov/38043714/)
- [Clinical Characteristics of Ciguatera Poisoning in Martinique, French West Indies (PMC9415704)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9415704/)
- [An Updated Review of Ciguatera Fish Poisoning (PMC5367029)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5367029/)
- [Neurological Disturbances of Ciguatera Poisoning: Clinical Features and Pathophysiological Basis (PMC7602189)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7602189/)
- [Global impact of ciguatoxins and ciguatera fish poisoning on fish, fisheries and consumers (PMID:31927300)](https://pubmed.ncbi.nlm.nih.gov/31927300/)
- [Ciguatera poisonings: A global review of occurrences and trends (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1568988320301529)
- [Epidemiology and Clinical Features of Ciguatera Fish Poisoning in Hong Kong (PMC4210881)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4210881/)
- [Incidence of Ciguatera Fish Poisoning in Culebra, Puerto Rico (PMC3339456)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3339456/)
- [Incidence and clinical characteristics of CFP in Guadeloupe 2013–2016 (PMC5814543)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5814543/)
- [Ciguatera Fish Poisoning in the Pacific Islands (1998 to 2008) (PMC3236724)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3236724/)
- [Screening for Predictors of Chronic Ciguatera Poisoning, French Polynesia (PMC8472944)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8472944/)
- [Cardiovascular Complications in Ciguatera Fish Poisoning (PMID:22574244)](https://pubmed.ncbi.nlm.nih.gov/22574244/)
- [Ciguatera Toxin Syndrome from Amberjack Ingestion — Chronic Dermatitis (PMC10562083)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10562083/)
- [MeSH Browser: Ciguatera Poisoning (D036841)](https://meshb.nlm.nih.gov/record/ui?ui=D036841)
- [Ciguatera Fish Poisoning — NORD](https://rarediseases.org/rare-diseases/ciguatera-fish-poisoning/)
- [ICD-10-CM T61.01XA](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T61-/T61.01XA)
- [Risk of ciguatoxins is shaped by Gambierdiscus community structure (PMC12854468, PMID:41610130)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12854468/)
- [Effects of pH and Nutrients on Growth and Toxin Profile of Gambierdiscus polynesiensis (PMC7761829)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7761829/)
- [Ciguatoxin-Producing Dinoflagellate Gambierdiscus in the Beibu Gulf (PMC8473099)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8473099/)
- [Is mannitol the treatment of choice for patients with ciguatera fish poisoning? (Clinical Toxicology)](https://www.tandfonline.com/doi/abs/10.1080/15563650.2017.1327664)
- [Ciguatera Toxicity Medication — Medscape](https://emedicine.medscape.com/article/813869-medication)
- [Ciguatera Fish Poisoning: Treatment, Prevention and Management (PMC2579736)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2579736/)
- [Fluorescent Receptor Binding Assay for Detecting Ciguatoxins in Fish (PMC4830512)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4830512/)
- [Establishing a Receptor Binding Assay for Ciguatoxins (PMC10818520)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10818520/)
- [Detection of ciguatoxin using sandwich ELISA and neuroblastoma cell bioassay (PMID:18623118)](https://pubmed.ncbi.nlm.nih.gov/18623118/)
- [Chemiluminescent Receptor Binding Assay for Ciguatoxins and Brevetoxins (PMC6833909)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6833909/)
- [Chronic Ciguatera Poisoning: A Case Report (ScienceDirect S1080603223000030)](https://www.sciencedirect.com/science/article/abs/pii/S1080603223000030)
- [Ciguatera: What It Is, Symptoms, Treatment & Long-term Effects — Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/ciguatera)
- [FDA Issues Final Guidance for Seafood Processors On How to Avoid Ciguatera Fish Poisoning](https://www.food-safety.com/articles/3365-fda-issues-final-guidance-for-seafood-processors-on-how-to-avoid-ciguatera-fish-poisoning)
- [CODE OF PRACTICE FOR THE PREVENTION OR REDUCTION OF CIGUATERA POISONING — Codex Alimentarius CXC 83-2024](https://www.fao.org/fao-who-codexalimentarius/sh-proxy/zh/?lnk=1&url=https://workspace.fao.org/sites/codex/Standards/CXC+83-2024/CXC_083e.pdf)
- [Ciguatera fish toxicity in French Polynesia: Size does not always matter (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0041010114000890)
- [Evaluating Age and Growth Relationship to Ciguatoxicity in Coral Reef Fish (PMC9027493)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9027493/)
- [Food poisoning from fish: Ciguatera — Poison Control](https://www.poison.org/articles/food-poisoning-from-ciguatera)
- [A descriptive study of ciguatera fish poisoning in Cook Islands dogs and cats: Demographic, temporal, and spatial distribution (PMC7020132, PMID:32158145)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7020132/)
- [A descriptive study of CFP in Cook Islands dogs and cats: Exposure history, clinical signs, case definition (PMC7096299)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7096299/)
- [A descriptive study of CFP in Cook Islands dogs and cats: Treatment and outcome (PMC7429383, PMID:32848300)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7429383/)
- [Ionic mechanisms of spinal neuronal cold hypersensitivity in ciguatera (PMC4744673)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4744673/)
- [Gene expression profiling in brain of mice exposed to ciguatoxin — BMC Neuroscience](https://link.springer.com/article/10.1186/1471-2202-11-107)
- [Human neuronal cell based assay: A new in vitro model for toxicity evaluation of ciguatoxin (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1382668917301011)
- [Ciguatera Fish Poisoning, Canary Islands (PMC3367630)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3367630/)
- [Ciguatera Toxicity — StatPearls (NBK482511)](https://www.ncbi.nlm.nih.gov/books/NBK482511/)
- [Ciguatera poisoning: an unwelcome vacation experience (PMC2666861)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2666861/)
- [Ciguatera fish poisoning — Wikipedia](https://en.wikipedia.org/wiki/Ciguatera_fish_poisoning)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 38 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 29 |
| Terms named correctly | 26 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001251` (2 mentions) - the report calls it "Peripheral neuropathy/paresis, ataxia"; HP calls it **Ataxia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000540` (1 mention) - the report calls it "neuron, generic"; CL calls it **neuron**
- `UBERON:0002240` (1 mention) - the report calls it "spinal cord, for DRG-adjacent structures"; UBERON calls it **spinal cord**, and lists "spinal cord structure" among its other names