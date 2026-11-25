---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T00:54:19.599797'
end_time: '2026-11-24T01:00:43.999482'
duration_seconds: 384.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SNUPN-Related Muscular Dystrophy
  mondo_id: MONDO:0100584
  category: Mendelian
  causal_genes: SNUPN
  omim_id: not recorded
  synonyms: not recorded
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
  web_search_requests: 4
  num_turns: 13
  total_cost_usd: 0.968976055
  session_id: 0d0b64ea-d690-4261-a3df-10d255f589e5
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 27
  retrieval_calls: 25
  assistant_text_blocks: 2
citation_count: 6
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  relevance_assessed: 12
  on_topic: 11
  validator_version: 0.8.0
term_validation:
  total_terms: 50
  verified: 50
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 20
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SNUPN-Related Muscular Dystrophy
- **MONDO ID:** MONDO:0100584 (if available)
- **Causal gene(s):** SNUPN
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SNUPN-Related Muscular Dystrophy** covering all of the
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

I'm still collecting abstracts for the main SNUPN papers. Shell access isn't approved, so I'm using web-fetch.

# SNUPN-Related Muscular Dystrophy (LGMDR29): Disease Characteristics Report

**How this report was built and what to check:**
- The target is the disease caused by biallelic variants in ***SNUPN*** (snurportin‑1, 15q24.2). It is published as SNUPN‑related muscular dystrophy, also called autosomal recessive limb‑girdle muscular dystrophy 29 (LGMDR29).
- **MONDO:0100584 could not be confirmed.** A web search found no page for this ID, so its label should be checked in OLS or Mondo.
- **OMIM is not confirmed directly.** OMIM returned HTTP 403. The phenotype MIM #620793 comes from secondary sources: OMIM‑derived tables found by search and the ACTN 2026 paper. SNUPN gene MIM 607902 likewise came from search results.
- **Quotes are short.** Full abstracts could not be reproduced. Quoted fragments are verbatim from the source, and longer passages are paraphrased.
- **Ontology IDs are unchecked.** The HPO, GO, CL and UBERON IDs are my suggestions and were not looked up in this session. Verify them before loading.
- **Evidence base.** There are four disease papers: [PMID 38366623](https://pubmed.ncbi.nlm.nih.gov/38366623/), [PMID 38413582](https://pubmed.ncbi.nlm.nih.gov/38413582/), [PMID 41054283](https://pubmed.ncbi.nlm.nih.gov/41054283/) and [PMID 41705730](https://pubmed.ncbi.nlm.nih.gov/41705730/). Together they cover about 27 patients.

---

## 1. Disease Information

**Overview.** SNUPN‑related muscular dystrophy is an autosomal recessive muscular dystrophy caused by biallelic hypomorphic variants in *SNUPN*. The gene encodes snurportin‑1 (SPN1), the adaptor that imports spliceosomal U‑snRNPs into the nucleus.
- **Clinical picture.** Patients have:
  - early proximal and axial weakness;
  - joint contractures and a rigid spine;
  - restrictive respiratory insufficiency;
  - raised creatine kinase (CK);
  - in some patients, features outside muscle: cerebellar atrophy, thin corpus callosum and congenital cataracts.
- **Biopsy and mechanism.** Muscle biopsy often shows myofibrillar‑like pathology. The mechanism is defective snRNP biogenesis with widespread mis‑splicing.

**Phenotypic range.** The 2026 cohort describes the entity as running "from a congenital or childhood onset pure muscular dystrophy to more complex phenotypes" with neurodevelopmental features, cataracts or spinocerebellar ataxia (Muelas et al., *Ann Clin Transl Neurol* 2026;13(2):285‑295, PMID 41054283, DOI 10.1002/acn3.70211; abstract paraphrased).

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| OMIM phenotype | #620793, LGMDR29 | From secondary sources; OMIM blocked |
| OMIM gene | SNUPN *607902 | From secondary sources |
| Disease Ontology | DOID:0061134 is the parent LGMD term; [disease-ontology.org](https://disease-ontology.org/term/DOID:0061134/owl) lists the LGMDR29 synonym | Partly retrieved |
| MONDO | MONDO:0100584, as supplied | Not verified |
| Orphanet, ICD‑10, ICD‑11, MeSH | No disease‑specific code retrieved. It probably falls under LGMD codes: ICD‑10 G71.0 / G71.03 and MeSH "Muscular Dystrophies, Limb‑Girdle". | Not retrieved |
| Gene/protein | SNUPN, ENSG00000169371; UniProt O95149; NP_001036046; 360 amino acids (per the Brain 2024 paper) | Retrieved |

**Synonyms:**
- SNUPN‑related muscular dystrophy
- LGMDR29
- autosomal recessive limb‑girdle muscular dystrophy 29
- SNUPN‑related LGMD with myofibrillar‑like features
- SNUPN‑related spinocerebellar atrophy (the neurological end of the spectrum, PMID 41705730)

**Source of data.** All data are aggregated case series of individual patients from four publications. No EHR or registry data exist.

---

## 2. Etiology

**Cause.** The disease is monogenic and autosomal recessive. It is caused by biallelic germline *SNUPN* variants, mostly hypomorphic.
- Nashabat et al. found that "Nine hypomorphic SNUPN biallelic variants, predominantly clustered in the last coding exon, are ascertained to segregate with the disease" (*Nat Commun* 2024;15:1758, PMID 38413582, DOI 10.1038/s41467-024-45933-5, PMCID PMC10899626).
- Iruzubieta et al. concluded that "variants in SNUPN are the cause of a new type of LGMD according to current definition" (*Brain* 2024;147(8):2867‑2883, PMID 38366623, DOI 10.1093/brain/awae046).

**Genetic risk factors:**
- **Homozygosity.** Consanguinity was present in 4/18 patients (22%) in the Nashabat cohort.
- **Founder haplotypes.** These were seen for c.926T>G (families F1 and F9), c.902_903delAT (F13/F14) and c.899_900delAC (F6, F7, F12) (PMID 38413582).
- **Variant class and severity.** Neurodegeneration and cataracts were more frequent with protein‑truncating variants than with missense variants. This comes from the Discussion of PMID 38413582, which was available only as a model summary, so treat it as provisional.

**Environmental risk factors.** None are known.

**Protective factors.** None are known, genetic or environmental.

**Gene–environment interactions.** None have been reported.

---

## 3. Phenotypes

Frequencies come from the Nashabat cohort (N=18, PMID 38413582) unless marked otherwise. "Iru" means the Iruzubieta cohort (N=5, PMID 38366623).

| Phenotype | Type | Frequency | Onset / course | Suggested HPO |
|---|---|---|---|---|
| Proximal upper‑ and lower‑limb weakness | Sign | 18/18 (100%); Iru 5/5 | Birth to 10 y; progressive | HP:0003701 Proximal muscle weakness |
| Distal lower‑limb weakness | Sign | 16/18 (89%) | Progressive | HP:0009053 Distal lower limb muscle weakness |
| Distal upper‑limb weakness | Sign | 12/16 (75%) | Progressive | HP:0008959 Distal upper limb muscle weakness |
| Axial weakness | Sign | 16/18 (89%) | Progressive | HP:0003327 Axial muscle weakness |
| Onset before walking or before age 2 | Onset | 12/18 (67%) | Congenital to infantile | HP:0003593 Infantile onset |
| Loss of ambulation | Function | 11/18 non‑ambulant (61%); Iru 2/5 in wheelchair | Childhood or adolescence (e.g., lost at 13 y) | HP:0002505 Progressive inability to walk |
| Elevated CK | Lab | 16/17 >500 U/L (94%), 1,500–8,000 U/L; Iru 290–5,750 IU/L | — | HP:0003236 Elevated circulating creatine kinase concentration |
| Myopathic EMG | Electrophysiology | 11/11 | — | HP:0003458 EMG: myopathic abnormalities |
| Joint contractures | Sign | 14/18 (78%); Iru 5/5, including neck and elbow | Early | HP:0001371 Flexion contracture; HP:0034392 Neck flexion contracture (verify) |
| Scoliosis, rigid spine, lordosis | Sign | 12/16 (75%); hyperlordosis Iru 5/5 | Progressive | HP:0002650 Scoliosis; HP:0003306 Spinal rigidity; HP:0003307 Hyperlordosis |
| Respiratory insufficiency needing support | Sign | 11/18 (61%); restrictive pattern Iru 5/5, with nocturnal NIV in 3 | Early, sometimes ahead of the weakness | HP:0002093 Respiratory insufficiency; HP:0002091 Restrictive ventilatory defect |
| Death from respiratory failure before age 15 | Outcome | 2/18 (11%) | Childhood | HP:0002878 Respiratory failure |
| Cerebellar atrophy | Imaging | 5/9 imaged (56%); asymptomatic in 1 adult (ACTN 2026) | — | HP:0001272 Cerebellar atrophy |
| Thin corpus callosum | Imaging | 3/7 (43%) | — | HP:0033725 Thin corpus callosum (verify) |
| White‑matter hyperintensities | Imaging | 1 patient | — | HP:0002500 Abnormality of the cerebral white matter |
| Congenital bilateral cataracts | Sign | 6/18 (33%), all operated | Congenital | HP:0000519 Congenital cataract |
| Spinocerebellar ataxia / atrophy | Sign | 2 families (Okubo 2026) | — | HP:0001251 Ataxia |
| Facial weakness | Sign | 0/5 (Iru) | Absent | Exclude: HP:0030319 |
| Cardiac conduction defect | Sign | Incomplete RBBB in 1/5 (Iru), otherwise no cardiac involvement reported | — | HP:0011712 Right bundle branch block |
| Myalgia, joint hyperlaxity | Symptom | 1/5 (Iru) | — | HP:0003326; HP:0001382 |

Alport syndrome was seen in all three sisters of Iruzubieta family 2. It is very likely a coincidental second diagnosis.

**Adult‑onset form.** Muelas et al. 2026 (PMID 41054283) describe two siblings who were compound heterozygous for p.Arg27Cys and p.Cys174Tyr.
- They had adult‑onset proximo‑distal and axial weakness with early respiratory involvement.
- Muscle MRI showed involvement of the paravertebral, triceps, sartorius and gracilis muscles.
- Some features resembled inclusion body myositis.

**Quality of life.** No EQ‑5D, SF‑36 or disease‑specific instrument has been reported. The main burdens are inferred from the clinical data:
- loss of walking in about 60%;
- dependence on night‑time ventilation;
- contractures and spinal deformity;
- vision problems from cataracts.

---

## 4. Genetic / Molecular Information

**Gene.**
- *SNUPN* (snurportin 1), 15q24.2, nine exons.
- The protein, SPN1 (O95149, 360 amino acids), has an N‑terminal importin‑β‑binding (IBB) domain, an m3G‑cap (TMG)‑binding domain and a C‑terminal region needed for self‑association (PMID 38413582).
- The HGNC ID and NCBI Gene ID were not retrieved.

**Reported pathogenic variants (germline, biallelic)**

| Variant | Protein | Class | Zygosity / families | Source |
|---|---|---|---|---|
| c.926T>G | p.Ile309Ser | Missense, exon 9 | Homozygous: Romanian and Macedonian families (Iru); Kosovar family F1 and F9 (founder), plus compound heterozygous | 38366623; 38413582 |
| c.760‑1G>A | — | Splice acceptor (intron 8 retention) | Compound heterozygous with c.958delA (F2) | 38413582 |
| c.958delA | p.Met320* | Nonsense / frameshift | Compound heterozygous | 38413582 |
| c.848C>G | p.Ser283* | Nonsense | Compound heterozygous | 38413582 |
| c.922C>T | p.Gln308* | Nonsense | Compound heterozygous | 38413582 |
| c.902_903delAT | p.Tyr301Cysfs*29 | Frameshift | Homozygous (F4, F13/F14) | 38413582 |
| c.899_900delAC | p.Asp300Valfs*30 | Frameshift | Homozygous in 4 families (founder) | 38413582 |
| c.787C>T | p.Gln263* | Nonsense | Compound heterozygous | 38413582 |
| c.164G>A | p.Arg55Gln | Missense, N‑terminal | Homozygous (F10) | 38413582 |
| p.Arg27Cys and p.Cys174Tyr | — | Missense | Compound heterozygous, adult onset | 41054283 |
| Compound heterozygous variants, details not retrieved | — | — | Spinocerebellar atrophy families | 41705730 |

Caveats on the table:
- The transcript is NM_001042581 per the Brain paper; it was printed as "NM_0011042581", so verify.
- "Eight out of nine variants cluster in the last coding exon," a 198‑nucleotide stretch. Because the variants cluster in this last exon, truncating changes would likely escape nonsense‑mediated decay and produce C‑terminally truncated protein. That is my inference, consistent with the authors calling the variants hypomorphic.
- In the Nashabat Results text, the list of compound‑heterozygous pairs is garbled, so check the supplement.

**Classification.**
- At discovery, c.926T>G was a VUS on exome sequencing. Its predictors were CADD 28.9 and AlphaMissense 0.9, and it was predicted damaging (PMID 38366623).
- ClinVar and ClinGen classifications were not retrieved.

**Allele frequencies:**
- c.926T>G: gnomAD v4 0.000005472 (PMID 38366623).
- c.902_903delAT: homozygous in 22 individuals in EVS, MAF ≤10⁻⁴, "clinical significance was unknown". This is an odd observation that should be checked.
- c.760‑1G>A, c.958delA, c.899_900delAC and c.787C>T: absent from gnomAD, BRAVO/TOPMed and EVS (PMID 38413582).

**Functional consequence.** Partial loss of function (hypomorphic):
- Truncating C‑terminal variants and Ile309Ser impair SPN1 oligomerization (truncations completely, Ile309Ser partly).
- The variants reduce importin‑β binding and impair folding (PMIDs 41054283, 41705730).
- Germline origin only; no somatic role in this disease.

**Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

---

## 5. Environmental Information

No environmental, lifestyle or infectious factors are known. Searches found no such reports.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. Biallelic hypomorphic *SNUPN* variants, mostly in exon 9 (the C‑terminus), lead to an SPN1 protein that misfolds, cannot oligomerize and binds importin‑β less well. Truncating variants abolish co‑immunoprecipitation with wild‑type SPN1, and Ile309Ser reduces it (PMID 38413582). Reduced importin‑β binding and impaired folding were also shown (PMID 41054283; PMID 41705730: "Mutated snurportin-1 displayed impaired nuclear transport and reduced binding to importin beta").
2. Defective SPN1 then fails to form or move the m3G‑capped U‑snRNP–SPN1–importin‑β import complex. Mutant SPN1 builds up around the nucleus in patient fibroblasts (PMID 38413582).
3. As a result, Sm‑core snRNPs are held in the cytoplasm and nuclear snRNP levels fall. This was demonstrated in patient fibroblasts and muscle (SmB/B′ aggregates) and in CRISPR HeLa lines. Iruzubieta et al. report "cytoplasmic accumulation of snRNP components" with unchanged total levels (PMID 38366623).
4. Next, nuclear spliceosome maturation is disrupted. COILIN moves into nucleoli, Cajal bodies are abnormal ("breakdown of Cajal bodies," abstract of PMID 38413582), and spliceosome‑component transcripts are themselves mis‑spliced (DDX39B, SF3A3, U2AF2, DDX5; PMID 38366623).
5. This leads to widespread mis‑splicing:
   - in mutant cells, 519 skipped exons and 88 retained introns;
   - in patient muscle, 714 events in 555 genes.

   It is not yet shown whether all of these events cause disease, and the authors note that some may be downstream of degeneration (PMID 38366623).
6. The pathway then branches:
   - **6a. Muscle sarcolemma and extracellular matrix (ECM).** Mis‑splicing and reduced levels of SGCA (exon 3 skipping), LAMA5, COL4A5/COL IV, COL6A1/2, COL12A1 and POSTN lead to reduced and abnormally cleaved β‑dystroglycan (DAG1) and destabilize the dystrophin‑glycoprotein complex. ITGB2 and SFRP2 go up (PMID 38413582).
   - **6b. Muscle calcium handling and cytoskeleton.** Mis‑splicing of PPP3CC, ANK2 and ATP2A1 (a shift to the neonatal SERCA1b isoform) is a probable contributor, which is inferred (PMID 38366623).
   - **6c. Cerebellum.** In Purkinje cells, global mis‑splicing lowers expression of neuronal development and synaptic genes, leaves the cytoskeleton immature and reduces sonic hedgehog secretion. That in turn disturbs granule‑cell migration and interneuron development, causing cerebellar atrophy and ataxia (knock‑in mouse, PMID 41705730).
   - **6d. Lens.** Cataracts are reported, but no mechanism has been studied.
7. Next, cytoskeletal disorganization and protein aggregation follow:
   - F‑actin and β‑tubulin are disorganized in mutant fibroblasts, and vimentin and vinculin increase;
   - desmin, αB‑crystallin and myotilin aggregate in patient muscle;
   - the Z‑disc streams, and p62/LC3 accumulate, implicating autophagy (PMIDs 38413582, 38366623).

   The authors' model is "(1) aberrant splicing, (2) disassembly of DGC (SGCA & DAG) complexes, and finally (3) cytoskeleton aggregation" (PMID 38413582).
8. This results in fibre degeneration and necrosis, endomysial fibrosis and fatty replacement. Clinically that appears as progressive proximal and axial weakness, contractures, restrictive respiratory failure and raised CK.

**Pathways and processes, with suggested GO terms:**
- snRNA import into nucleus (GO:0061015)
- spliceosomal snRNP assembly (GO:0000387)
- mRNA splicing via spliceosome (GO:0000398)
- protein import into nucleus (GO:0006606)
- extracellular matrix organization (GO:0030198)
- cytoskeleton organization (GO:0007010)
- autophagy (GO:0006914)
- cerebellar Purkinje cell layer development (GO:0021680)

**Cellular components, with suggested GO terms:**
- Cajal body (GO:0015030)
- cytoplasm (GO:0005737)
- nuclear envelope (GO:0005635)
- Z disc (GO:0030018)
- dystrophin‑associated glycoprotein complex (GO:0016010)
- extracellular matrix (GO:0031012)

**Cell types, with suggested CL terms:**
- skeletal muscle fibre (CL:0008002)
- fibroblast (CL:0000057)
- Purkinje cell (CL:0000121)
- cerebellar granule cell (CL:0001031)

**Molecular profiling:**
- **Muscle RNA‑seq** (2 patients): 511 genes up and 125 down. SPP1 was among the most increased, FOS and EGR1 among the most decreased, and STMN2 appeared only in patients (PMID 38366623).
- **Fibroblast cytosolic proteomics:** 102 proteins up and 28 down, enriched for mitochondrial, snRNP and spliceosome terms (PMID 38366623).
- **Single‑cell RNA‑seq** of mouse cerebellum (PMID 41705730).
- **Not reported:** metabolomics, lipidomics, epigenomics, immune studies or CRISPR screens. No inflammation was seen (STIR MRI was negative).

---

## 7. Anatomical Structures Affected

**Primary:** skeletal muscle (UBERON:0001134).
- **Thigh** (Iru MRI): gluteus medius, involved in all; vasti; adductor magnus; sartorius; gracilis. The posterior thigh is relatively spared.
- **Paravertebral muscles.**
- **Lower leg:** peroneus longus, medial gastrocnemius.
- **Arm (adult form):** triceps.

**Secondary:**
- respiratory muscles and diaphragm (UBERON:0001103), giving restrictive respiratory insufficiency;
- cerebellum (UBERON:0002037);
- corpus callosum (UBERON:0002336);
- lens (UBERON:0000965);
- joints and spine (contractures, rigid spine);
- possibly heart (RBBB in 1 patient).

**Body systems:** musculoskeletal, respiratory, nervous and visual.

**Tissue, cell and subcellular level:** see Section 6.

**Lateralization:** bilateral and symmetric. The cataracts were bilateral.

---

## 8. Temporal Development

**Onset:**
- usually congenital to childhood, from birth to 10 years;
- 67% before walking or before age 2 (PMID 38413582);
- Iruzubieta cohort: 1–9 years;
- a rarer adult‑onset form exists (PMID 41054283);
- the onset pattern is insidious and chronic.

**Progression.** The course is slowly to moderately progressive and lifelong:
- ambulation is often lost in childhood or adolescence;
- respiratory insufficiency can be early;
- two children died of respiratory failure before age 15.

No formal staging, remission or natural‑history study exists.

**Critical period.** The early respiratory decline is a window in which monitoring matters. This is inferred from the clinical data.

---

## 9. Inheritance and Population

**Inheritance and penetrance:**
- autosomal recessive;
- penetrance appears complete in biallelic carriers;
- heterozygous parents were unaffected;
- expressivity is variable, from pure LGMD to multisystem disease, and from congenital to adult onset;
- no anticipation or germline mosaicism has been reported.

**Patient count.** About 27 published patients:
- 18 from 15 families (PMID 38413582);
- 5 from 2 families, Romanian and Macedonian (PMID 38366623);
- 2 Spanish siblings (PMID 41054283);
- 2 families in Japan (PMID 41705730).

There is probably some overlap, because the Iruzubieta and Nashabat cohorts share c.926T>G.

**Geography and populations:**
- The Nashabat cohort spans three continents. Author institutions are in Turkey, Iran, Europe, the USA and Colombia, but the individual patients' origins were mostly not available to me.
- Founder haplotypes exist for c.926T>G (Balkan: Kosovo, Romania, North Macedonia) and for two exon‑9 frameshifts.

**Sex ratio:** 10 male to 8 female.

**Epidemiology:** prevalence, incidence and carrier frequency are unknown.

---

## 10. Diagnostics

**Laboratory:**
- CK is raised in most patients, usually 1,500–8,000 U/L, but can be only mildly raised (about 300 U/L).
- EMG is myopathic.
- Nerve conduction is usually normal; one patient had reduced CMAP amplitude.

**Muscle MRI:**
- gluteus medius;
- paravertebral muscles;
- anterior and medial thigh (vasti, adductor magnus, sartorius, gracilis), with the posterior thigh relatively spared;
- peroneus and medial gastrocnemius;
- no oedema on STIR.

**Brain MRI:** cerebellar atrophy and/or thin corpus callosum.

**Ophthalmology:** slit‑lamp examination for cataracts.

**Respiratory:** pulmonary function tests show a restrictive pattern.

**Muscle biopsy** (PMIDs 38366623, 38413582, 41054283):
- dystrophic changes with endomysial fibrosis;
- type I fibre predominance;
- internal nuclei and necrotic fibres;
- minicore‑like and whorled fibres;
- occasional rimmed vacuoles;
- myotilin, desmin, αB‑crystallin and p62/LC3 aggregates, with Z‑disc streaming on electron microscopy, i.e. myofibrillar‑like features ("Muscle biopsy showed myofibrillar-like features consisting of myotilin deposits and Z-disc disorganization," PMID 38366623);
- reduced α‑sarcoglycan and dystroglycan;
- cytoplasmic SmB/B′ aggregates, a possible tissue marker;
- in the adult form, granule and vesicle proliferation with remodelling of the nuclear envelope and sarcolemma.

**Genetic testing:**
- Exome or genome sequencing, or an LGMD/myopathy panel that includes *SNUPN*. The authors advise that SNUPN be included in genetic testing for myopathies (PMID 38366623).
- Muelas et al. advise testing in adults with late‑onset proximo‑distal and axial weakness with early respiratory impairment, especially when it mimics inclusion body myositis (PMID 41054283).
- RNA studies can confirm splice variants (for example, intron‑8 retention with c.760‑1G>A).
- Microarray, karyotype, FISH, mtDNA and repeat‑expansion tests have no direct role. They are useful only to exclude other diagnoses.

**Differential diagnosis** (by clinical reasoning; no cited source compares these):
- Rigid‑spine and contracture myopathies: SEPN1, COL6, LMNA, EMD/FHL1.
- Myofibrillar myopathies: DES, MYOT, CRYAB, FLNC, BAG3.
- Sarcoglycanopathies and dystroglycanopathies.
- Inclusion body myositis, for the adult form.
- Marinesco–Sjögren syndrome (SIL1): congenital cataracts, cerebellar atrophy and myopathy.
- Spinocerebellar ataxias, for the cerebellar form.

**Screening:** no newborn screening exists. Cascade carrier testing is possible once the familial variants are known.

---

## 11. Outcome / Prognosis

**Mortality:**
- 2/18 children (11%) died of respiratory failure before 15 years (PMID 38413582);
- the oldest reported patients are in their 20s to adulthood (Iru: 29 y);
- the adult‑onset family is described as well;
- survival curves and life expectancy are unavailable.

**Morbidity:**
- about 60% lose ambulation;
- about 60% develop respiratory insufficiency needing support;
- contractures and scoliosis are common;
- cataracts need surgery.

**Prognostic factors:**
- Truncating variants may be linked to more neurological and lens involvement (provisional, from the summarized Discussion of PMID 38413582).
- Early onset is linked to greater severity, which is inferred.
- No prognostic biomarkers are known, and no QoL data exist.

---

## 12. Treatment

**No disease‑specific therapy exists.** No drugs, gene therapy, ASO or cell therapy have been tested. No ClinicalTrials.gov entries were identified, though a dedicated search was not run.

Nashabat et al. speculate that "targeting SPN1 or other snRNP partners may hold promise" (from a summarized section of PMID 38413582).

**Supportive care.** This follows general LGMD and congenital myopathy practice; nothing SNUPN‑specific is published. Suggested NCIT terms are not verified.
- **Respiratory:** regular PFTs and nocturnal non‑invasive ventilation (NIV), which three Iruzubieta patients use. NCIT: Non‑Invasive Ventilation.
- **Physical therapy, stretching and orthoses** for contractures. NCIT: Physical Therapy.
- **Scoliosis surveillance and surgery** where needed.
- **Mobility aids.**
- **Cataract surgery,** done in all six affected children (NCIT: Cataract Extraction).
- **ECG and echocardiography** given the single RBBB case.
- **Genetic counselling.**

**Pharmacogenomics:** not applicable.

---

## 13. Prevention

- **Primary prevention:** none.
- **Genetic counselling:** 25% recurrence risk for sibs of an affected child.
- **Reproductive options:** carrier testing of relatives, prenatal diagnosis or preimplantation genetic testing once the familial variants are known.
- **Founder variants:** in founder populations (Balkans; families with exon‑9 frameshifts), targeted carrier testing may be informative.
- **Tertiary prevention:** respiratory surveillance with timely NIV, contracture prevention, scoliosis monitoring and early detection of cataracts.
- **Vaccines, prophylaxis, environmental measures:** not applicable.

---

## 14. Other Species / Natural Disease

- No naturally occurring SNUPN disease in animals has been reported, and OMIA was not searched.
- Orthologues have been studied: fly Snup (Natalizio et al., *Mol Biol Cell* 2013, PMID 23885126) and mouse Snupn (PMID 41705730).
- SPN1's role in snRNP import is evolutionarily conserved; Drosophila Snurportin was characterized in PMID 23885126.
- No zoonotic potential.
- Ortholog NCBI Gene IDs were not retrieved.

---

## 15. Model Organisms

| Model | Type | Phenotype | Recapitulation and limits | Source |
|---|---|---|---|---|
| *Drosophila* muscle‑specific Snup RNAi (Mhc‑GAL4 > UAS‑iSnup, VDRC #40997) | Invertebrate knockdown | Climbing on day 15: 49.3% vs 84.7% in controls. Day 25: 0.55% vs 56.6%. Median lifespan 67 vs 88 days (P<0.001). | Progressive motor decline. Knockdown, not the patient alleles, and the histology was limited. | PMID 38366623 |
| Snupn knock‑in mouse carrying the patients' compound heterozygous variants | Mammalian knock‑in | Cerebellar ataxia, cerebellar atrophy, Purkinje dendritic abnormalities, global Purkinje mis‑splicing, reduced SHH, secondary granule‑cell and interneuron defects | Models the neurological arm. Muscle phenotype not described in the abstract. | PMID 41705730 |
| CRISPR/Cas9 HeLa SPN1^sgEx2 and SPN1^sgEx9 | Cell line | Reduced SPN1 and nuclear Sm, more COILIN foci, reduced β‑dystroglycan | Non‑muscle cells | PMID 38413582 |
| Patient dermal fibroblasts (m1/m1, m2/m3, m6/m6, m9/m9) | Primary cells | Perinuclear SPN1 aggregates, cytoplasmic snRNP retention, mis‑splicing, ECM and cytoskeletal defects | Non‑muscle cells | PMIDs 38413582, 38366623 |
| HEK293T co‑IP and overexpression systems | In vitro | Loss of oligomerization | Biochemical only | PMID 38413582 |

- **Not yet available:** zebrafish, iPSC‑derived myotubes and organoids.
- **Resources:** MGI, FlyBase (Snup) and VDRC; MGI and IMPC were not queried.

---

## Key references

1. Iruzubieta P, et al. Biallelic variants in *SNUPN* cause a limb girdle muscular dystrophy with myofibrillar‑like features. *Brain* 2024;147(8):2867‑2883. PMID 38366623; DOI 10.1093/brain/awae046; https://pmc.ncbi.nlm.nih.gov/articles/PMC11292911/
2. Nashabat M, et al. SNUPN deficiency causes a recessive muscular dystrophy due to RNA mis‑splicing and ECM dysregulation. *Nat Commun* 2024;15:1758. PMID 38413582; DOI 10.1038/s41467-024-45933-5; PMC10899626.
3. Muelas N, et al. SNUPN‑Related Muscular Dystrophy: Novel Phenotypic, Pathological and Functional Protein Insights. *Ann Clin Transl Neurol* 2026;13(2):285‑295. PMID 41054283; DOI 10.1002/acn3.70211; PMC12883674.
4. Okubo M, et al. SNUPN variants cause spinocerebellar atrophy by disrupting global splicing in cerebellar Purkinje cells. *Brain* 2026;149(3):1007‑1022. PMID 41705730; DOI 10.1093/brain/awaf348.
5. Natalizio AH, et al. Identification and characterization of Drosophila Snurportin. *Mol Biol Cell* 2013. PMID 23885126 (title and authors only; not read).
6. Disease Ontology, DOID:0061134 (LGMD; LGMDR29 synonym): https://disease-ontology.org/term/DOID:0061134/owl

**Data gaps:**
- Exact MONDO, Orphanet, ICD and MeSH codes.
- ClinVar classifications.
- The full variant and pair list from the Nashabat supplement.
- Variant details for the Okubo families.
- Any natural history, QoL or therapeutic‑trial data; none exist in the literature found.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 23 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `DOID:0061134` (5 mentions) - the report calls it "LGMD; LGMDR29 synonym"; DOID calls it **autosomal recessive limb-girdle muscular dystrophy type 29**, and lists "LGMDR29" among its other names
- `CL:0008002` (1 mention) - the report calls it "skeletal muscle fibre"; CL calls it **skeletal muscle fiber**
- `UBERON:0001103` (1 mention) - the report calls it "respiratory muscles and diaphragm"; UBERON calls it **diaphragm**, and lists "thoracic diaphragm" among its other names

Every term resolved, and every label the report gave matched.