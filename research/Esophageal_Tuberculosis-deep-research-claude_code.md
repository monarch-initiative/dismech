---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T00:24:36.064271'
end_time: '2026-11-27T00:31:22.432284'
duration_seconds: 406.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Esophageal Tuberculosis
  mondo_id: MONDO:0004189
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: esophagus tuberculosis; oesophagus tuberculosis; tuberculosis of oesophagus
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
  - claude-opus-5-5
  web_search_requests: 10
  num_turns: 19
  total_cost_usd: 1.172366935
  session_id: ef8c6552-650e-4c66-900c-3fdb04fe8845
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 88
  retrieval_calls: 86
  assistant_text_blocks: 3
citation_count: 13
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 39
  on_topic: 28
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  service_unreachable: 2
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Esophageal Tuberculosis
- **MONDO ID:** MONDO:0004189 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** esophagus tuberculosis; oesophagus tuberculosis; tuberculosis of oesophagus
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Esophageal Tuberculosis** covering all of the
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

Let me try PubMed E-utilities directly for PMIDs and abstracts.

I'm gathering primary PubMed abstracts on esophageal TB, then a few broader TB sources for genetics, mechanism, treatment and models.

# Esophageal Tuberculosis (MONDO:0004189): Disease Characteristics Report

**How I scoped this report:** Esophageal tuberculosis (ETB) is an infectious disease caused by *Mycobacterium tuberculosis* complex. **No causal human gene is recorded, and none exists.** This matches the template ("Causal gene(s): not recorded"). The genetic sections therefore cover host susceptibility to TB in general, labelled as not specific to the esophagus.

The literature on ETB itself is small: case reports, case series and three reviews. Wherever a claim comes from general TB research rather than ETB research, I say so. I give ontology terms (HPO, GO, CL, UBERON, NCIT, CHEBI) as **labels only**. I did not retrieve their numeric IDs in this session, so they need to be mapped before use. The identifiers that were retrieved are listed in Section 1.

---

## 1. Disease Information

**Overview.** ETB is tuberculosis of the esophagus. The Disease Ontology defines its counterpart (DOID:7332) as *"A gastrointestinal tuberculosis that involves formation of tuberculous ulcers located_in esophagus"* ([MGI/DO](https://www.informatics.jax.org/disease/DOID:7332)).

It is one of the rarest forms of extrapulmonary TB:
- *"Esophageal TB accounts for less than 0.2% of total TB cases"* and about 2.8% of GI TB cases (Chaudhary et al. 2022, PMID 36742928, [PMC9895252](https://pmc.ncbi.nlm.nih.gov/articles/PMC9895252/)).
- *"Esophageal tuberculosis is rare, constituting about 0.3% of gastrointestinal tuberculosis"* (Jain SS et al. 2013, PMID 24255751).

Most cases are **secondary**, spreading from nearby mediastinal lymph nodes or the lungs: *"Secondary esophageal tuberculosis is much more common than primary TB. The most common source of secondary esophageal involvement is tuberculous mediastinal lymphadenitis"* (PMID 36742928).

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| MONDO | MONDO:0004189 (leaf term; parents are esophageal disorder and gastrointestinal tuberculosis) | [SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0004189/) |
| Disease Ontology | DOID:7332 | [MGI](https://www.informatics.jax.org/disease/DOID:7332) |
| UMLS / MedGen | C0152902 | [MedGen](https://ncbi.nlm.nih.gov/medgen/C0152902) |
| MeSH | No esophagus-specific descriptor. The parent is **Tuberculosis, Gastrointestinal, D014385** | [MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D014385) |
| ICD-10-CM | Probably A18.83, "Tuberculosis of digestive tract organs, not elsewhere classified". I could not confirm that the esophagus is coded here, so check the official tabular. | [AAPC](https://aapc.com/codes/icd-10-codes/A18.83) |
| OMIM / Orphanet | None (not a Mendelian disease) | — |
| ICD-11 | Not retrieved | — |

**Synonyms:** esophagus tuberculosis; oesophageal tuberculosis; tuberculosis of (o)esophagus; esophageal TB; ET/ETB. "Primary ETB" (no other TB focus) and "secondary ETB" are clinical subtypes.

**Source of information:** Aggregated disease-level resources, mainly case reports and case series pooled in reviews. There are no EHR or registry cohorts specific to ETB.

---

## 2. Etiology

**Cause.** The cause is infection with *M. tuberculosis* complex (*M. tuberculosis* in essentially all reported cases). *M. bovis* causes zoonotic TB, but I found no ETB case attributed to it.

There are three routes of spread (PMID 36742928; Ye et al. 2022, PMID 36498584):
1. **Spread from contiguous structures.** This is the most common route, usually from mediastinal and subcarinal nodes, less often from lung, larynx or the spine (Pott's disease). *"In most cases, ET is caused by the rupture of infected mediastinal lymph nodes to the esophagus"* (PMID 36498584). Devarbhavi et al. found that *"Esophageal tuberculosis was always associated with spread from adjacent structures"* (PMID 12665778).
2. **Hematogenous or miliary spread.** This is rare.
3. **Primary infection.** *"Primary ET occurs when patients swallow sputum or food contaminated with tubercle bacilli"*, but it *"very rarely occurs"* (PMID 36498584).

**Risk factors.** None of these were studied in ETB cohorts. They are inferred from TB in general.
- **TB endemicity.** Most series come from India, China and Pakistan. In Indian patients with persistent dysphagia, ETB made up *"0.5% of all patients with persistent dysphagia"* (Jain SK et al. 2002, PMID 11866263).
- **Male sex:** *"male to female ratio of 3.2:1"* (PMID 36742928). However, the 311-patient systematic review found 50.5% were male (Birda et al. 2022, PMID 34482490).
- **HIV.** In ETB, *"less than 1% of cases of esophageal TB have been found to be HIV positive"* (PMID 36742928). Case reports describe ETB in AIDS ([Endoscopy 2006](https://www.thieme-connect.com/products/ejournals/html/10.1055/s-2006-944643)). In the four-patient series of Ye et al., *"None of them had AIDS ... or other diseases that led to being immunocompromised"* (PMID 36498584).
- **TNF-α blockade** (general TB risk): *"There were 70 reported cases of tuberculosis after treatment with infliximab, for a median of 12 weeks"* (Keane et al. 2001, PMID 11596589).

**Genetic risk factors** (general TB, not ETB-specific):
- **TYK2 P1104A homozygosity:** *"may account for ∼1% of TB cases in Europeans"*. Frequency was *"6/620, 1%"* in TB patients versus *"228/114,473, 0.2%"* in controls (Kerner et al. 2019, PMID 31068474). Homozygosity impairs IL-23-dependent IFN-γ immunity, with an odds ratio of about 89 in endemic-area cohorts (Boisson-Dupuis et al. 2018, PMID 30578352).
- **Mendelian susceptibility to mycobacterial disease (MSMD).** *"299 unique mutations in 21 genes"* have been reported. *"61% ... had mutations of IL12RB1 (41%) or IFNGR1 (20%)"* (Khavandegar et al. 2024, PMID 38341181).
- In general, *"human genetic factors contribute significantly to this interindividual variability"* (Abel et al. 2014, PMID 24821915).

**Protective factors.**
- **BCG vaccination** protects mainly against severe childhood forms. A systematic review of 18 trials found that absence of prior infection *"is associated with higher efficacy of BCG"* (Mangtani et al. 2014, PMID 24336911). Protection against infection *"is inconsistent across different groups"* (Pelzer et al. 2025, PMID 39709975).
- No protective variants have been identified for ETB.

**Gene–environment interaction.** None has been studied for ETB. In general TB, defects in the IL-12/IL-23–IFN-γ axis interact with the level of exposure (PMID 30578352).

---

## 3. Phenotypes

**Pooled frequencies across 311 patients from 22 studies** (Birda et al. 2022, PMID 34482490): *"Dysphagia (72.3%), odynophagia (22.4%) and chest pain (31.3%) were predominant symptoms."* Chaudhary et al. reported that *"Progressive dysphagia is the most common presenting symptom reported in more than 90% of patients"* and that constitutional symptoms are *"present in up to 65% of cases"*. They called anaemia *"the most consistent physical finding"* (PMID 36742928).

| Phenotype | Type | Frequency / notes | Suggested HPO label (ID not retrieved) |
|---|---|---|---|
| Dysphagia, progressive | Symptom | 72.3% (34482490); >90% (36742928) | Dysphagia |
| Odynophagia | Symptom | 22.4% | Odynophagia |
| Chest pain / retrosternal pain | Symptom | 31.3% | Chest pain |
| Weight loss | Constitutional | Up to 65% | Weight loss |
| Fever, night sweats, anorexia, fatigue | Constitutional | Common (36498584) | Fever; Night sweats; Anorexia; Fatigue |
| Cough on eating / cough after swallowing (fistula) | Sign | Predominant in fistula cases (12665778) | Cough |
| Hematemesis / upper GI bleeding | Sign | Table 2 of 36742928 lists 8 cases. The narrative review calls bleeding a "most common symptom" (36498584). | Hematemesis; Gastrointestinal hemorrhage |
| Anemia | Laboratory | "Most consistent physical finding" | Anemia |
| Esophageal ulcer | Endoscopic | 59.9% | Esophageal ulceration |
| Submucosal bulge / extrinsic compression | Endoscopic | 31.7% / 24.8% | — |
| Pseudotumour | Endoscopic | 5.8% | — |
| Esophageal stricture | Complication | 7 cases (36742928) | Esophageal stricture |
| Tracheo-/broncho-esophageal fistula | Complication | About 50% in one 10-patient series (12665778) | Tracheoesophageal fistula |
| Mediastinal lymphadenopathy (CT) | Imaging | 76.5% | Mediastinal lymphadenopathy |
| Abnormal chest radiograph | Imaging | 65% (Nagi et al. 2003, PMID 12752007) | — |

- **Onset:** Adults; *"The average age at diagnosis is 39 years"*, range 15 to 85 (PMID 36742928). Paediatric cases have been reported, for example a 14-year-old (PMID 15163882) and a 15-year-old with hematemesis (PMID 24255751).
- **Course:** Subacute to chronic and progressive. Symptoms typically last weeks to months.
- **Quality of life:** No EQ-5D or SF-36 data exist. The main burdens are dysphagia-related malnutrition and aspiration through fistulas: *"Tracheoesophageal fistula can increase the risk of aspiration pneumonia"* (PMID 36498584).

---

## 4. Genetic / Molecular Information

- **Causal genes:** Not applicable, since this is an infection. There are no pathogenic germline variants, ClinVar entries, chromosomal abnormalities or epigenetic signatures specific to ETB.
- **Host susceptibility and modifier genes** (general TB or mycobacterial disease):
  - TYK2 P1104A (PMIDs 31068474, 30578352).
  - MSMD genes, chiefly IL12RB1 and IFNGR1, mostly loss-of-function and usually autosomal recessive (PMID 38341181).
- **Allele frequency:** Using ancient DNA, Boisson-Dupuis et al. estimate that *"the frequency of P1104A in Europeans has decreased, from about 9% to 4.2%, over the past 4000 years"* (PMID 30578352).
- **Pathogen genetics:** The ESX-1/RD1 locus drives macrophage recruitment and granuloma expansion (Davis & Ramakrishnan 2009, PMID 19135887; zebrafish/*M. marinum* model). Drug-resistance mutations are relevant to treatment. PMID 36498584 mentions rolling-circle amplification for resistance detection (96.6% sensitivity, 89.5% specificity).
- **Epigenetics:** No data for ETB.

---

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* complex. I did not retrieve the NCBI Taxonomy ID. Transmission is by airborne droplets. Secondary ETB arises from established thoracic infection, and swallowing infected sputum or food is proposed as the route for primary ETB (PMID 36498584).
- **Environmental and lifestyle factors:** None specific to ETB. General TB drivers such as crowding, undernutrition and immunosuppression (HIV, TNF inhibitors) apply by inference. The esophagus is thought to be relatively protected by its stratified squamous epithelium and saliva, but I did not retrieve a source for this in this session.
- **Zoonotic *M. bovis*:** Its burden in humans *"might be underestimated"* (Olea-Popelka et al. 2017, PMID 27697390). No esophageal cases were identified.

---

## 6. Mechanism / Pathophysiology

**Causal chain (most common, secondary route):**

1. Inhaled *M. tuberculosis* infects alveolar macrophages and spreads by lymphatics to hilar, mediastinal and subcarinal lymph nodes. This step is established general TB biology.
2. Within the nodes, ESX-1/RD1-dependent recruitment of macrophages **leads to** granuloma formation and expansion. Infected macrophages leave the granuloma and seed new ones (PMID 19135887, zebrafish model; for humans this is inferred).
3. Granulomas fail to eradicate the bacteria (PMID 22517424). The result is caseous necrosis and matted, enlarged nodes, typically subcarinal (EUS: *"enlarged lymph nodes adjacent to esophageal wall lesions in 18 cases"* of 32; Puri et al., PMID 21777339).
4. Enlarged nodes **cause** extrinsic compression of the mid-esophagus. Clinically this is a submucosal bulge with dysphagia.
5. Caseating nodes infiltrate and rupture into the esophageal wall, which **results in** transmural granulomatous inflammation and mucosal ulceration (PMID 36498584; Baijal et al. via [Semantic Scholar](https://www.semanticscholar.org/paper/Esophageal-Tuberculosis-:-An-Analysis-of-Fourteen-Baijal-Agal/aa209a897000705c7f663957f7ea8dd762273f88)).
6. The process then branches:
   - **6a.** Penetration into the airway or mediastinum **leads to** a tracheo- or broncho-esophageal fistula or esophagomediastinal sinus, which leads to coughing on swallowing and aspiration pneumonia (PMID 12665778).
   - **6b.** Erosion into the aorta **leads to** an aortoesophageal fistula and massive hematemesis (PMID 36498584).
   - **6c.** Healing by fibrosis, or traction by fibrotic nodes, **leads to** stricture or traction diverticulum (PMID 36742928).
   - **6d.** Systemic cytokine release (inferred) **leads to** fever, weight loss and anaemia.

**Alternative initiating routes.** Primary ETB begins with swallowed bacilli seeding the mucosa, then mucosal ulceration and granuloma. Hematogenous/miliary spread is rare. In both cases the chain continues from step 5.

**Mechanism checklist**

| Category | What is known |
|---|---|
| **Immune and cellular** | Granulomas show *"central caseous necrosis, surrounded by a radial arrangement of epithelioid cells, with scattered Langhans giant cells"* (PMID 36498584). Control of infection depends on IFN-γ and TNF signalling (PMIDs 30578352, 11596589). Adalimumab and infliximab *"suppressed phagosome maturation"* in macrophages (PMID 18954258, in vitro). |
| **Suggested GO labels** | granuloma formation; response to bacterium; macrophage activation; interferon-gamma–mediated signaling pathway; tumor necrosis factor–mediated signaling pathway; phagosome maturation; inflammatory response; necrotic cell death |
| **Suggested CL labels** | macrophage (alveolar macrophage upstream); epithelioid cell; multinucleated (Langhans) giant cell; CD4-positive alpha-beta T cell; esophageal squamous epithelial cell |
| **Tissue damage** | Caseous necrosis, ulceration, fibrosis/stricture, fistulisation |
| **Molecular profiling** (transcriptomics, proteomics, single-cell, spatial) | None found for ETB |

---

## 7. Anatomical Structures Affected

- **Primary site:** Esophagus, predominantly the middle third (UBERON label: "middle third of esophagus"; I did not retrieve the ID). *"Mid-oesophagus was the commonest site of involvement (88%)"* (PMID 34482490). Lower-third involvement is rare. Chaudhary et al. state that the upper third has not been reported (PMID 36742928). Abid et al., however, described *"deep and large proximal esophageal ulcers"* (PMID 12739552), so this point is disputed.
- **Secondary sites:** mediastinal and subcarinal lymph nodes (76.5% on CT), lungs, trachea and bronchi (fistula), aorta (fistula), pleura, spine.
- **Body systems:** digestive, respiratory, lymphatic/immune.
- **Tissue level:** stratified squamous mucosa, submucosa, muscularis and adventitia. On EUS the lesion is *"heterogeneous and hypoechoic ... with interrupted adventitia"* (Yang et al. 2025, PMID 41244781).
- **Subcellular level:** the bacteria live inside macrophage phagosomes (GO cellular component label: "phagocytic vesicle").
- **Laterality:** Not applicable; this is a midline organ.

---

## 8. Temporal Development

- **Onset:** Mostly adults (mean 39 years; most series report means of 31 to 51). Onset is insidious or subacute.
- **Stages:** No formal staging. EUS describes three nodal phases, from Phase I *"homogeneous and hypoechoic"* to later *"heterogeneous, predominantly hypoechoic mass with local hyperechoic foci or strands, indistinct adventitia, and occasionally partial matting"* (PMID 36498584). Endoscopic morphologies run roughly in order: bulge, then ulcer, then fistula or stricture.
- **Course:** Without treatment it progresses, with complications such as fistula, bleeding or dissemination. With treatment, remission follows: *"His dysphagia subsided within two weeks of starting therapy"* (Paudel et al. 2021, PMID 34367833). Fistulas can close on medical therapy alone, as in *"A follow-up endoscopy after two months revealed that the fistula was closed"* (Salad et al. 2022, PMID 35298984). Endoscopic healing is usually documented by about 1 year (PMID 36498584).
- **Critical window:** Diagnosing it before unnecessary esophagectomy, which can happen when ETB is mistaken for carcinoma (PMID 16252203).

---

## 9. Inheritance and Population

- **Inheritance:** Not applicable (acquired infection). Penetrance, anticipation, founder effects and carrier frequency are not applicable.
- **Epidemiology:**
  - About 0.15–0.2% of TB cases or TB-related deaths, and 0.07–3% of GI TB (PMIDs 36742928, 36498584).
  - 0.30% prevalence in one Chinese surgical cohort (Ni et al. 2013, PMID 23991308).
  - 0.5–0.55% of patients with persistent dysphagia in endemic India (PMID 11866263).
  - Context: WHO estimated about 10.7 million people fell ill with TB in 2024, and 16% of notified cases were extrapulmonary ([WHO Global TB Report 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-disease-burden/1-1-tb-incidence)).
  - No population incidence rate exists for ETB itself.
- **Geography:** Mostly TB-endemic South and East Asia, Africa and Latin America. One South African review found only 11 patients over 18 years ([PMC2399217](https://pmc.ncbi.nlm.nih.gov/articles/PMC2399217)).
- **Sex ratio:** Reported anywhere from about 1:1 (50.5% male, PMID 34482490) to 3.2:1 male (PMID 36742928).
- **Age distribution:** 15 to 85 years.

---

## 10. Diagnostics

**Endoscopy.** Findings include *"ulcers (59.9%), submucosal bulge (31.7%), extrinsic compression (24.8%) and pseudotumour (5.8%)"* (PMID 34482490). The typical lesion is a *"mid-esophageal linear ulceration with irregular infiltrated margins and grayish membranous necrotic base"*. Fistulas may show a *"double-barreled appearance"* (PMID 36498584).

**Biopsy and histopathology.**
- Granuloma was found in 72.3% and AFB in 32.5% (PMID 34482490).
- Mucosal biopsy sensitivity was 22% to 60.8% (PMID 36742928).
- Ziehl–Neelsen staining is *"positive in <25%"*. Culture has *"80% and 98%"* sensitivity and specificity but takes 6 to 8 weeks (PMID 36498584).
- PCR on paraffin-embedded biopsies can establish the diagnosis (Fujiwara et al. 2003, PMID 12560925).
- Cytology was *"a very useful diagnostic parameter"* (PMID 11866263).

**Endoscopic ultrasound (EUS) and EUS-guided sampling.**
- Puri et al. found ulcers in 56.25%, extrinsic bulge in 62.5%, and a definitive diagnosis in 27/32 (PMID 21777339).
- Tang et al. reported an EUS-established diagnosis in 33/35 (94.3%) (PMID 28575247).
- EUS helps when repeated biopsies fail: *"All 9 patients failed to be diagnosed by at least two repeated biopsies"* (Zhu et al. 2020, PMID 32859167).
- EUS-guided fine-needle biopsy was diagnostic in 4 of 6 (PMID 41244781). EUS-guided fine-needle aspiration plus T-SPOT worked in a single case (PMID 38311428).

**Imaging.**
- CT shows *"mediastinal lymphadenopathy (76.5%) and oesophageal thickening (52.1%)"* (PMID 34482490). Necrotic nodes are suggestive.
- Chest radiograph is abnormal in 65% (PMID 12752007).
- Barium swallow shows strictures, fistulas or traction diverticula.

**Molecular tests.** For extrapulmonary TB, Xpert MTB/RIF and Xpert Ultra *"may be helpful"*, but *"Sensitivity varies across different extrapulmonary specimens"* (Kohli et al. Cochrane 2021, PMID 33448348). Neither has been validated specifically on esophageal tissue.

**Immunological tests.** IGRA/T-SPOT and TST are supportive only.

**Genetic testing.** Not indicated, except for MSMD work-up when mycobacterial disease is unusually severe or recurrent (PMID 38341181).

**Differential diagnosis:**
- Esophageal carcinoma (*"Esophageal TB can mimic esophageal carcinoma on computed tomography scan"*, PMID 31572563; can lead to *"unnecessary surgical therapy such as esophagectomy"*, PMID 16252203)
- Crohn's disease of the esophagus (PMID 31572563)
- CMV, HSV, candida and HIV-related idiopathic ulcers
- Sarcoidosis
- Lymphoma
- Submucosal tumours (leiomyoma, GIST)
- Mediastinal malignancy with fistula

**Diagnostic criteria:** There are no formal criteria. Diagnosis rests on histology (caseating granuloma) and/or microbiology (AFB, culture, PCR), with response to anti-TB therapy as supportive evidence.

**Screening:** Not applicable to ETB. Latent TB screening before TNF inhibitors is recommended (PMID 11596589).

---

## 11. Outcome / Prognosis

- **Survival:**
  - *"Response to antitubercular therapy was excellent; 97.7% patients recovered and 2.3% patients died"* (PMID 34482490).
  - Devarbhavi et al.: 9 of 10 patients recovered on drugs alone, and 1 died of disseminated disease (PMID 12665778).
  - South African series: 9 of 11 had good outcomes and 2 died (PMC2399217).
  - Chaudhary et al.: 1 of 4 local cases died of septicaemia within 6 days of starting therapy (PMID 36742928).
  - Ye et al.: *"The prognosis is generally good if patients are diagnosed properly and receive anti-tubercular treatment promptly"* (PMID 36498584).
- **Complications:** hematemesis (8), stricture (7), traction diverticulum (4), esophagobronchial fistula (4), esophagoarterial/aortic fistula (4), esophagopleural fistula (2) (PMID 36742928, Table 2). Others include aspiration pneumonia, perforation and dissemination.
- **Poor prognostic factors** (inferred from case series):
  - Disseminated or miliary disease
  - Aortoesophageal fistula
  - Delayed diagnosis
  - HIV co-infection: one cited series of 6 HIV-positive men with TB fistulas found that none improved on anti-TB therapy alone (cited secondarily via [Redalyc](https://www.redalyc.org/journal/3377/337766864017/337766864017.pdf); primary source not retrieved).
- **Prognostic biomarkers:** None established.
- **Quality-of-life measures:** No data.

---

## 12. Treatment

**Drug therapy** (NCIT labels: Antitubercular Agent; Isoniazid; Rifampin; Pyrazinamide; Ethambutol).
- **Standard regimen:** 2 months of isoniazid, rifampicin, pyrazinamide and ethambutol (HRZE), then 4 months of isoniazid and rifampicin (HR). This is the general ATS/CDC/IDSA approach (Sotgiu et al. 2016, PMID 27587550; no abstract retrieved).
- **Duration:** Ye et al. describe a 9-month course (2 months HRZE + 7 months HR) (PMID 36498584). Chaudhary et al. suggest 6 months for isolated disease and 12 months for disseminated disease, but that figure comes from an unverified part of the full text. Paediatric cases were treated for 6 months (PMID 24255751).
- **Shorter regimen:** A 4-month rifapentine–moxifloxacin regimen was *"noninferior to the standard 6-month regimen"* for pulmonary TB (Dorman et al. 2021, PMID 33951360). It has not been studied in ETB.
- **Pharmacogenomics:** NAT2 acetylator status affects isoniazid toxicity. This was not retrieved this session and is not ETB-specific.

**Endoscopic and interventional treatment:**
- Esophageal stenting (11.4% of patients, PMID 34482490)
- Over-the-scope clip closure of fistulas (success 33–77%) and argon plasma coagulation for bleeding (PMID 36498584)
- Dilation of strictures

**Surgery** (NCIT labels: Esophagectomy; Video-Assisted Thoracoscopic Surgery). Surgery was needed in 14.5% (PMID 34482490). It is *"indicated for failed medical therapy and complications"* (PMID 36742928). VATS *"is useful in improving rate of confirmative diagnosis, and relieving symptom of dysphagia"* (PMID 23991308). The historic first report was esophagectomy for primary ETB (Fahmy et al. 1969, PMID 5821628).

**Supportive care:** nutritional support (enteral feeding when dysphagia or fistula is severe), proton-pump inhibitors, and treatment of aspiration pneumonia. These are general practice; no ETB-specific trials were retrieved.

**Gene, cell, RNA, targeted or immunotherapies:** Not applicable. No ETB clinical trials were identified.

**Adverse events:** Standard first-line TB drug toxicities apply (hepatotoxicity, optic neuritis with ethambutol). These are general knowledge, not retrieved this session.

**Treatment algorithm:**
1. Suspicion: mid-esophageal ulcer or bulge, mediastinal nodes, endemic exposure.
2. Endoscopic biopsy for histology, AFB, culture and PCR/Xpert.
3. If non-diagnostic, EUS-guided FNA or FNB.
4. Anti-TB therapy.
5. Endoscopic or surgical management for persistent fistula, bleeding or stricture.

---

## 13. Prevention

- **Primary prevention:**
  - BCG vaccination; its protection against pulmonary disease varies (PMIDs 24336911, 39709975).
  - Airborne infection control and contact tracing.
- **Secondary prevention:**
  - Treat latent TB infection, especially before TNF-inhibitor therapy (PMID 11596589).
  - Prompt treatment of mediastinal TB lymphadenitis, which removes the main source of secondary ETB (inferred).
- **Tertiary prevention:** Early diagnosis prevents fistulas and unnecessary esophagectomy (PMIDs 16252203, 36742928). Endoscopic follow-up confirms healing.
- **Genetic counselling:** Only relevant for MSMD families.
- **Public health:** The WHO End TB programmes apply. Screening for ETB itself is not indicated.

---

## 14. Other Species / Natural Disease

- No naturally occurring esophageal TB in animals was identified in this session.
- *M. bovis* causes bovine TB and zoonotic human TB (PMID 27697390), but no esophageal disease was reported.
- Cynomolgus macaques develop active and latent TB resembling human disease (*"The data underscore the similarities between human and nonhuman primate M. tuberculosis infection"*; Lin et al. 2009, PMID 19620341). Esophageal involvement is not described.
- Not retrieved this session: NCBI Taxon IDs, VBO breeds, and orthologue gene IDs.

---

## 15. Model Organisms

There is **no specific model of esophageal TB.** The general TB models are:

| Model | Use | Recapitulation and limits |
|---|---|---|
| Zebrafish / *M. marinum* | Granuloma formation, ESX-1/RD1 virulence, macrophage dissemination (PMID 19135887) | Captures early granuloma biology; not mediastinal-to-esophageal spread |
| Cynomolgus macaque / *M. tuberculosis* | Spectrum of latent and active TB; *"the only established model of latent infection"* (PMID 19620341) | Closest to human pathology, including caseous granulomas and thoracic lymph nodes; costly |
| Mouse (knockouts in IFN-γ/IL-12/TNF pathways) | Host susceptibility; parallels human MSMD and TNF-inhibitor biology | Not retrieved this session; mice lack classic caseating granulomas |
| Human macrophages in vitro | Effect of TNF blockers on phagosome maturation (PMID 18954258) | Cellular only |

Model databases such as MGI and ZFIN have no ETB-specific entries (MGI DOID:7332 page shows no models, [MGI](https://www.informatics.jax.org/disease/DOID:7332)).

---

## Key Evidence Summary

| PMID | Study | Evidence type |
|---|---|---|
| 34482490 | Birda 2022, systematic review, 311 patients | Human clinical |
| 36742928 | Chaudhary 2022, review of 133 cases plus 4 local cases | Human clinical |
| 36498584 | Ye 2022, endoscopy narrative review | Human clinical |
| 21777339 | Puri 2012, EUS in 32 cases | Human clinical |
| 28575247 | Tang 2017, EUS in 35 cases | Human clinical |
| 12665778 | Devarbhavi 2003, 10 fistula cases | Human clinical |
| 11866263 | Jain 2002, 12 cases, 0.5% of persistent dysphagia | Human clinical |
| 12752007 | Nagi 2003, imaging in 23 cases | Human clinical |
| 23991308 | Ni 2013, surgical cohort in China | Human clinical |
| 31068474, 30578352, 38341181 | Host genetics (TYK2, MSMD) | Human genetic |
| 19135887, 22517424 | Granuloma biology | Model organism / review |
| 11596589 | Infliximab-associated TB | Human pharmacovigilance |

**Gaps and caveats:**
- There are no ETB-specific genetic, omics, QoL, incidence-registry, animal-model or clinical-trial data.
- Treatment-duration recommendations differ between sources (6, 9 or 12 months).
- Ontology numeric IDs other than MONDO, DOID, MedGen and MeSH were not retrieved and need to be mapped.

Sources: [PMC9895252](https://pmc.ncbi.nlm.nih.gov/articles/PMC9895252/) · [PMC9740747](https://pmc.ncbi.nlm.nih.gov/articles/PMC9740747/) · [Birda, Dysphagia (SpringerMedizin)](https://www.springermedizin.de/oesophageal-tuberculosis-a-systematic-review-focusing-on-clinica/19632794) · [MedGen C0152902](https://ncbi.nlm.nih.gov/medgen/C0152902) · [MONDO node](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0004189/) · [MGI DOID:7332](https://www.informatics.jax.org/disease/DOID:7332) · [MeSH D014385](https://meshb.nlm.nih.gov/record/ui?ui=D014385) · [AAPC A18.83](https://aapc.com/codes/icd-10-codes/A18.83) · [WHO Global TB Report 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-disease-burden/1-1-tb-incidence) · [PMC2399217](https://pmc.ncbi.nlm.nih.gov/articles/PMC2399217) · [Baijal et al.](https://www.semanticscholar.org/paper/Esophageal-Tuberculosis-:-An-Analysis-of-Fourteen-Baijal-Agal/aa209a897000705c7f663957f7ea8dd762273f88) · [Endoscopy 2006 AIDS case](https://www.thieme-connect.com/products/ejournals/html/10.1055/s-2006-944643) · [Redalyc HIV case](https://www.redalyc.org/journal/3377/337766864017/337766864017.pdf) · PubMed abstracts retrieved via NCBI E-utilities (efetch) for every PMID cited above.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 39 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Terms the ontology service could not be reached for

2 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0004189` (5 mentions)
- `DOID:7332` (9 mentions)

No term could be looked up either way, so nothing here was confirmed or contradicted.