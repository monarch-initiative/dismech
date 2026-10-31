---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T19:15:01.277659'
end_time: '2026-10-15T19:16:40.363898'
duration_seconds: 99.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lessel-Kreienkamp Syndrome
  mondo_id: MONDO:0030897
  category: Mendelian
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
  web_search_requests: 5
  num_turns: 12
  total_cost_usd: 0.8280181
  session_id: a4618dfa-d284-5dfb-b077-0a3b19b97962
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 7
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0030897
    reported_labels:
    - MONDO
    ontology_label: Lessel-Kreienkamp syndrome
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lessel-Kreienkamp Syndrome
- **MONDO ID:** MONDO:0030897 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lessel-Kreienkamp Syndrome** covering all of the
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

I'll load the search tools and verify the gene and identifiers first, since I don't want to assert them from memory.

Status: I've verified the gene and the main sources I could reach. PubMed and PMC blocked my fetches, so I'm writing the report now and marking what I couldn't check.

# Lessel-Kreienkamp Syndrome (LESKRES): research report

**Source classes used here:** structured databases (MedGen, GenCC, LOVD, via search summaries), primary literature (two papers, one reached only as a summary), and a preprint (title only).

**What I could not check:**
- PubMed and PMC returned cookie and browser-verification pages, so I never read the Lessel 2020 abstract or full text. For that paper I have only a Europe PMC excerpt (under 125 characters), a search-tool paraphrase, and the figures the 2025 Frontiers paper quotes from it.
- I found no Orphanet ORPHA code. That is a gap in what I searched, not evidence that none exists.
- I did not read OMIM, ClinGen, ClinVar, gnomAD, GeneReviews, MGI or ZFIN directly.
- The MONDO ID in your template is not confirmed from MONDO itself. Search summaries attributed it to MedGen, but I could not open that record. Treat it as a lead and run `just validate-terms` before binding.

## 1. Disease information

**Overview.** LESKRES is an autosomal dominant neurodevelopmental disorder caused by heterozygous *AGO2* variants. The disorder is characterized by global developmental delay, intellectual disability, and speech and language delay from infancy or early childhood, with a wide severity range.
- Source for the overview and range: NCBI MedGen (UID 1762595) via search summary.
- Severity range: some patients walk with mild delay and mild cognitive deficits, while others never walk or speak.
- Co-occurring features per the same summary: behavioral problems (most common), seizures, hypotonia, cardiac defects, subtle facial differences.

**Identifiers.**

| Identifier | Value | Source and status |
|---|---|---|
| OMIM phenotype | #619149 | MedGen, LOVD (disease #07272), GenCC listing; structured databases via search results |
| OMIM gene | *606229 (AGO2) | Search-result summary only; not checked in OMIM |
| MONDO | MONDO:0030897 | Lead only, per your template and a search summary of MedGen |
| Orphanet | not found | Gap |
| Gene | *AGO2*, 8q24.3 | MedGen via search summary |

**Pitfalls.**
- The JAX vocabulary page pairs "Lessel-Kreienkamp Syndrome" with OMIM:618681. That number is Lessel-Kubisch syndrome (*MDM2*) in other sources, so the JAX pairing looks like a source error.
- LOVD lists the gene as EIF2C2, an older symbol for *AGO2*. I inferred this is a naming difference and did not verify it.
- Do not confuse it with *AGO1*-related neurodevelopmental disorder (a separate gene; the AGO1 paper is bioRxiv 2020.12.23.424103 / PMID 34930816 per a search summary, not read).

**Synonyms.** LESKRES; AGO2-related neurodevelopmental disorder; Lessel-Kreienkamp neurodevelopmental syndrome (the title of the 2026 preprint).

**Data origin.** The data come from aggregated case series and database assertions. Individual-level EHR data are not described in anything I read.

## 2. Etiology

- **Cause.** Germline heterozygous *AGO2* variants. GenCC lists the *AGO2*–LESKRES relationship as Definitive and autosomal dominant (GenCC submission SGC-105696.2, via search summary; submitter not identified).
- **Origin.** The Frontiers 2025 paper states most reported variants are de novo. That paper also reports inheritance in one branch of its own family, where the proband's mother carries the variant, and its Discussion describes the variant as de novo. The two statements are internally inconsistent in that article.
- **Risk, protective, environmental and gene-environment factors.** None reported in anything I read. I did not search for them specifically.

## 3. Phenotypes

All figures below are from the Frontiers 2025 case report (Yang, Song & Yan, doi 10.3389/fgene.2025.1598462). They are that paper's pooled counts across 25 reported individuals, drawn mainly from Lessel 2020. They are secondary figures, not the original data.

| Phenotype | Frequency | Suggested HPO (not looked up; verify) |
|---|---|---|
| Intellectual disability | 25/25 | Intellectual disability |
| Motor developmental delay | 25/25 | Motor delay |
| Delayed independent walking (>15 months) | 22/22 | Delayed ability to walk |
| Impaired speech development | 25/25 | Delayed speech and language development |
| Impaired receptive language | 17/17 | Receptive language delay |
| Seizures | 8/22 (about 36%) | Seizure |
| Epicanthic folds | 16/25 | Epicanthus |
| ADHD | 12/19 | Attention deficit hyperactivity disorder |
| Gait abnormality | 9/18 | Abnormal gait |
| Brain morphology abnormality | 9/17 | Abnormal brain morphology |
| Open mouth appearance | 13/25 | Open mouth |

**Correction.** The source shows 8/22 for seizures, which is about 36%, not the 67% the fetch summary printed. Check the source before using that figure.

**Pediatric framing.**
- Onset is infancy or early childhood, with developmental delay as the presenting feature.
- Hypotonia, cardiac defects and behavioral problems are listed qualitatively in MedGen. I have no frequencies for them and no quality-of-life data.
- Progression and the adult phenotype are unknown from what I read.

## 4. Genetic and molecular information

- **Gene.** *AGO2*, which encodes Argonaute-2, the catalytic effector of the RNA-induced silencing complex (RISC). The HGNC CURIE should be read from HGNC or `cache/hgnc/terms.csv` before binding. I did not look it up.
- **Variant spectrum (Frontiers 2025).** Quoted: "With the exception of p.Phe182del, all identified variants are missense."
  - Lessel 2020 reported 13 variants in 21 patients (Nat Commun 2020, PMID 33199684 per GenCC, PMC7670403, doi 10.1038/s41467-020-19572-5).
  - The Frontiers paper counts 14 pathogenic variants including its own.
  - A chr8 deletion encompassing *AGO2* is also mentioned (chr8.hg19:g.(141,582,269–141,817,600)), set aside in that paper's analysis.
- **Hotspots.** The paper gives residues 182–203, 357–367 and 717–760, but its figure caption gives 340–367 and 714–760. Those boundaries conflict in the source.
- **Newer cohort (preprint, not peer-reviewed as far as I could confirm).** "The clinical and molecular spectrum of AGO2-associated Lessel-Kreienkamp neurodevelopmental syndrome" (Research Square rs-8378840). A search summary says it reports 45 new individuals with 33 variants (30 novel), pooled with 70 previously reported cases. I read only the title page, so the counts are unverified.
- **Mechanism class.** Lessel 2020 reports that, depending on the mutation, the defect either prevented RISC formation or caused tighter mRNA-target binding (paraphrase from a tool summary; only the quote "We identify 13 heterozygous mutations in AGO2 in 21 patients affected by disturbances in neurological development" was returned verbatim). Every tested change impaired shRNA-mediated silencing per the GenCC-linked search summary. I could not determine whether this is classed as loss of function, dominant negative or other.
- **Frontiers case.** AGO2 c.2149T>C (p.Cys717Arg), ACMG likely pathogenic (PM2_P, PP2, PS2_M, PP1, PP3). The authors say they lack functional data and that mechanism is unresolved.
- **ClinVar, gnomAD, epigenetic and chromosomal information:** not retrieved.

## 5. Environmental information

Not applicable or not reported in the sources I read.

## 6. Mechanism and pathophysiology

An ordered causal chain, with inferred steps marked.

1. A heterozygous germline *AGO2* variant arises, mostly de novo (Frontiers 2025).
2. The variant alters the Argonaute-2 protein. Variants cluster in domain hotspots, including the PIWI region around residues 717–760, which carries the catalytic DDE motif (Frontiers 2025).
3. The altered protein impairs RNA interference. In Lessel 2020, every tested variant reduced shRNA-mediated silencing.
4. Two branches are reported in Lessel 2020 (paraphrase of the abstract; source not read directly):
   - 4a. Some variants prevent RISC formation.
   - 4b. Others make AGO2 bind mRNA targets too tightly.
5. Impaired miRNA-guided regulation is inferred to disrupt neuronal gene regulation during development. This step is inference from the abstract's framing ("dynamic AGO2–RNA binding to normal human neuronal development"), not a demonstrated pathway to specific phenotypes.
6. Developmental delay, intellectual disability, speech delay and variable seizures and behavioral problems follow. The link from step 5 to these features is not demonstrated.

**Suggested GO terms (not looked up).** RNA interference; miRNA-mediated gene silencing; RISC complex. Bind only after a lookup.
**Cell type and anatomy.** Neurons and the CNS are plausible. I found no cell-type-resolved data.
**Omics, single-cell and screens:** a GEO record (GSE311030, dated 2026-07-27) appears linked to the preprint's AGO2-bound miRNA sequencing, but I did not open it, and per the CLAUDE.md dataset rules its relevance needs manual triage.

## 7. Anatomical structures affected

The central nervous system is the primary system affected (neurodevelopment, with brain morphology abnormalities in 9/17 per Frontiers 2025). Secondary involvement listed qualitatively in MedGen: heart (cardiac defects) and face. I have no laterality or subcellular data.

## 8. Temporal development

- Onset is in infancy or early childhood.
- Natural history, progression and disease stages are not described in anything I read.
- No remission pattern is reported.

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant (MedGen, GenCC).
- **De novo.** Most variants are de novo (Frontiers 2025).
- **Penetrance and expressivity.** Expressivity is variable (severity range above). I have no penetrance estimate. Apparent inheritance in the Frontiers family means familial transmission occurs, but the paper is internally inconsistent about which variants were de novo.
- **Prevalence, incidence, sex ratio, founder effects, geographic distribution:** not found.
- **Germline mosaicism:** not assessed in the sources read.
- **Cohort size.** At least 21 patients in 2020, plus the later case reports, plus the 2026 preprint's claimed 45 additional individuals (unverified).

## 10. Diagnostics

- **Genetic testing.** Variants were found by whole-exome sequencing or array CGH in the original cohort (via search summary of the 2026 preprint's background). Exome or genome sequencing, or a gene panel containing *AGO2*, is the route. Genomics England PanelApp lists *AGO2* on its Intellectual disability panel (panel 285); the gene's rating there was not retrieved.
- **Chromosomal microarray.** The chr8 deletion encompassing *AGO2* means CMA can detect deletion cases, but I have no data on how often.
- **Biomarkers, imaging, diagnostic criteria and screening:** no disease-specific marker, criteria or screening program found. Brain imaging abnormalities occur in about half of those assessed.
- **Differential diagnosis.** Other Argonaute and miRNA-pathway disorders (e.g. *AGO1*) and other genetic causes of syndromic intellectual disability.

## 11. Outcome and prognosis

No survival or longevity data found. Functional outcome ranges from mild delay with independent walking to non-ambulatory and nonverbal (MedGen). Prognostic factors by variant or domain are the main purpose of the 2026 preprint, but I could not read its results.

## 12. Treatment

No disease-specific therapy was found. No clinical trial (NCT) was searched for. Management would be supportive: developmental, speech and physical therapy, and anti-seizure treatment where seizures occur. This is inference from the phenotype, not a source-backed recommendation.

## 13. Prevention

Genetic counseling is the main measure. Recurrence risk is low where the variant is de novo, but at least one family shows transmission, so parental testing is relevant. No sources were retrieved on prenatal or preimplantation options.

## 14. Other species and natural disease

Nothing found, and I did not search OMIA. *AGO2* is highly conserved across species.

## 15. Model organisms

I found no AGO2 model organism data for this phenotype. The functional evidence I found is in cell systems (shRNA silencing assays in Lessel 2020 and the 2026 preprint's co-IP, localization and miRNA sequencing, per a search summary). Evidence source for those is `IN_VITRO`. MGI, ZFIN and IMPC were not searched, so this is a gap, not an absence.

## Suggested next steps for curation

1. Fetch and read Lessel 2020 (PMID 33199684) via `just fetch-reference PMID:33199684` before quoting any snippet. The search-tool paraphrase that mutations were "inherited" conflicts with the de novo statement in Frontiers 2025, so verify it against the paper itself.
2. Check ClinGen, ClinVar and the AGO2 OMIM entry directly, and quote the ClinGen assertion as `CGGV:` rather than relying on the GenCC search summary.
3. Resolve MONDO:0030897 and the ORPHA code with `just validate-terms` and an Orphadata lookup.
4. Decide lump/split. Variant-level genotype-phenotype claims should wait for the 2026 cohort to be published.

## Sources

- [NCBI MedGen 1762595](https://ncbi.nlm.nih.gov/medgen/1762595) (search snippet only)
- [LOVD disease #07272](https://databases.lovd.nl/shared/diseases/07272)
- [GenCC submission SGC-105696.2](https://thegencc.org/submissions/SGC-105696.2) (search snippet only)
- [Lessel et al. 2020, Nat Commun, PMC7670403](https://pmc.ncbi.nlm.nih.gov/articles/PMC7670403) (not read directly)
- [Yang, Song & Yan 2025, Front Genet](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2025.1598462/full)
- [Research Square preprint rs-8378840](https://www.researchsquare.com/article/rs-8378840/v1) (title only)
- [Genomics England PanelApp, AGO2](https://panelapp.genomicsengland.co.uk/panels/285/gene/AGO2/) (search snippet only)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030897` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Lessel-Kreienkamp syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.