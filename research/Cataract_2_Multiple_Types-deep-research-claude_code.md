---
provider: claude_code
model: claude-opus-5-5
cached: false
start_time: '2026-10-23T01:55:26.111824'
end_time: '2026-10-23T01:58:59.499863'
duration_seconds: 213.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 2, Multiple Types
  mondo_id: MONDO:0100436
  category: Mendelian
  causal_genes: CRYGC
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
  - claude-opus-5-5
  num_turns: 21
  total_cost_usd: 2.0517308
  session_id: 21d3f92e-29ff-44d3-9eb2-80699e9e6513
  stop_reason: end_turn
  permission_denials: 9
  denied_tools:
  - Bash
  - mcp__ols-mcp__get_terms_from_ontology
  - mcp__ols-mcp__search_all_ontologies
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 5
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 2, Multiple Types
- **MONDO ID:** MONDO:0100436 (if available)
- **Causal gene(s):** CRYGC
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

Please provide a comprehensive research report on **Cataract 2, Multiple Types** covering all of the
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

I'm going through the locally cached CRYGC references, since PubMed access isn't granted.

Now pulling the variant-level details from the tables in those cohort papers.

I have what I need. The report is below.

# Cataract 2, Multiple Types (CTRCT2; CRYGC-related congenital cataract): Research Report

**Target:** Cataract 2, multiple types, MONDO:0100436. **Causal gene: *CRYGC*** (γC-crystallin, chromosome 2q33–q35, in the *CRYGA–CRYGD* cluster). This is not the *CRYGD* disease: Cataract 4, multiple types (MONDO:0007281) is curated separately in `kb/disorders/Cataract_4_Multiple_Types.yaml`.

## How this report was researched

- **PubMed and OLS access were denied in this session**, so I could not search live literature or ontologies. The report is built from two sources:
  1. **Verified:** 22 abstracts and full texts already in the repository's `references_cache/` that mention *CRYGC*, plus the repository's committed term caches (`cache/hp`, `cache/cl`, `cache/go`, `cache/uberon`, `cache/ncit`). Every quote in "Evidence Table A" was copied from those cached files and is fit to use as a dismech snippet.
  2. **Background knowledge (unverified):** earlier literature I know of but could not open, such as the Ren 2000 insertion family, Santhiya 2002 R168W, and mouse *Crygc* models. These are marked **[UNVERIFIED]**. Their PMIDs, if given, must be confirmed with `just fetch-reference` before use. No quote is given for any of them.
- **The HGNC ID for *CRYGC* is not in `cache/hgnc/terms.csv`.** Only `hgnc:2411` (CRYGD) is cached. I believe *CRYGC* is `hgnc:2410`, but that comes from memory and **must be looked up** before it is written into an entry.

---

## 1. Disease Information

**Overview.** CTRCT2 is a non-syndromic, usually autosomal dominant, congenital or early-childhood lens opacity caused by heterozygous variants in *CRYGC*. "Multiple types" refers to the range of shapes the opacity takes in different families: Coppock-like (embryonal nuclear), lamellar/zonular, zonular pulverulent, nuclear, and others. Some families also have microcornea.

**Identifiers**
| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0100436 "cataract 2, multiple types" | In the draft entry |
| OMIM phenotype | 604307 (CTRCT2) | One cached paper lists "CRYGC, OMIM 604307" (PMID:31842807) |
| OMIM gene | 123680 (*CRYGC*) | [UNVERIFIED] |
| HGNC | hgnc:2410 (CRYGC) | [UNVERIFIED — look up] |
| Orphanet | No disease-specific ORPHA. Covered by the general "early-onset non-syndromic cataract" group | [UNVERIFIED] |
| ICD-10 / ICD-11 | Q12.0 Congenital cataract / LA10 (no gene-specific code) | Standard classification |
| MeSH | Cataract/congenital (D002386) | General |

**Synonyms (OMIM-style, unverified):** CTRCT2; Coppock-like cataract; cataract, congenital, Coppock-like; cataract, zonular pulverulent, CRYGC-related; CRYGC-related congenital cataract.

**Data source type.** Everything here comes from disease-level resources: family linkage and segregation studies, and next-generation-sequencing (NGS) panel or exome cohorts. No electronic-health-record or registry data are specific to this disease.

## 2. Etiology

- **Cause:** a heterozygous germline *CRYGC* variant. Most are inherited dominantly; a few have arisen de novo.
- **Gene–disease validity:** a 2026 ClinGen-protocol curation of 13 crystallin genes found *CRYGC* **Definitive** for autosomal dominant pediatric cataract (PMID:42091610). This is a published curation that used ClinGen methods. It is **not** a ClinGen `CGGV:` record, so it must not go into `gene_disease_validity` with `classified_by: CLINGEN` unless an actual CGGV assertion is found.
- **Historical correction:** the first human cataract mutation, the Coppock-like cataract, was originally assigned to the pseudogene *CRYGE*. Héon et al. (1999) showed that the *CRYGE* change was a polymorphism found in 23% of controls, and that the true cause in the original family was a missense variant in *CRYGC* exon 2 (PMID:10521291). This variant is usually given as p.Thr5Pro.
- **Environmental risk, protective factors, gene–environment interaction:** none reported. It is a monogenic developmental cataract. Clinical environmental modifiers apply to every infantile cataract, not to this disease: amblyopia is driven by how long the visual axis is deprived of a clear image, and aphakic glaucoma risk rises with surgery in early infancy.

## 3. Phenotypes

| Phenotype | HPO (cached) | Onset | Frequency / notes | Source |
|---|---|---|---|---|
| Cataract (bilateral, congenital) | HP:0000518 Cataract | Congenital | Defining (100%) | All cohort papers |
| Nuclear cataract | HP:0100018 | Congenital | The most common reported form: S78F (PMID:29914532), W157X (PMID:40868138) | Verified |
| Coppock-like (embryonal nuclear) cataract | No specific HPO term; use HP:0100018 with a note | Congenital | Original family, T5P | PMID:10521291 |
| Lamellar / zonular cataract | HP:0007971 / HP:0010920 | Congenital/infantile | R168W families [UNVERIFIED, Santhiya 2002] | — |
| Zonular pulverulent cataract | HP:0010693 Pulverulent cataract | Congenital | 5-bp insertion family [UNVERIFIED, Ren 2000] | — |
| Microcornea | HP:0000482 | Congenital | Seen with truncating variants: E135* (PMID:27878435); W157X [Guo 2012, UNVERIFIED] | Verified (E135*) |
| Nystagmus | HP:0000639 | Infancy | Secondary to dense early opacity; frequency not reported | General |
| Strabismus, amblyopia | HP:0000486, HP:0000646 | Childhood | Sequelae of visual deprivation | General |
| Visual impairment | HP:0000505 | Congenital | Severity depends on how dense and central the opacity is, and how early surgery is done | General |
| Aphakic glaucoma (post-surgical) | HP:0000501 Glaucoma | After surgery | A complication of lensectomy, not a primary feature | PMID:35307324 (management review) |

- **Inheritance term:** HP:0000006 Autosomal dominant inheritance.
- **Onset terms:** HP:0003577 Congenital onset; HP:0003593 Infantile onset.
- **Expressivity:** severity and morphology vary between families and within them.
- **Quality of life:** the main burden is lifelong reduced vision and amblyopia. No QoL instrument has been studied in this specific disease.

## 4. Genetic / Molecular Information

**Gene.** *CRYGC* has 3 exons and encodes a 174-amino-acid protein made of two domains, each containing two Greek-key motifs. The protein is a major structural protein of fiber cells in the embryonic and fetal lens nucleus. Its RefSeq transcript is NM_020989.3/.4 (protein NP_066269.1, from PMID:24968223).

**Reported variants**
| Variant (NM_020989) | Protein | Class | Phenotype | Source |
|---|---|---|---|---|
| c.13A>C [nomenclature unverified] | p.Thr5Pro (T5P) | Missense, Greek key 1 | Coppock-like | PMID:10521291 (abstract names "a missense mutation in a highly conserved segment of exon 2") |
| c.233C>T | p.(Ser78Phe) | Missense, Greek key 2 | Nuclear; classed LP (likely pathogenic) | PMID:29914532 |
| c.328_329delinsT | p.Pro110Serfs*37 | Frameshift, Greek key 3 | Classed P (pathogenic); segregates | PMID:26694549 |
| c.403G>T | p.(Glu135*) | Nonsense | Pediatric cataract with microcornea; gnomAD 0.0000577 | PMID:27878435 |
| c.432C>A | p.Tyr144* | Nonsense | Classed P | PMID:37337769 |
| c.471G>A | p.Trp157Ter (W157X) | Nonsense, ex3 | Nuclear; de novo; surgery at 1 month | PMID:40868138; PMID:18421082 |
| c.497C>T | p.Ser166Phe | Missense, Greek key 4 | Segregates; classed P | PMID:26694549 (originally Prokudin 2014) |
| p.Arg168Trp | — | Missense | Lamellar | [UNVERIFIED, Santhiya 2002] |
| c.119_123dup (5-bp insertion) | Frameshift | — | Variable zonular pulverulent | [UNVERIFIED, Ren 2000] |

- **Origin:** germline in every case, and no somatic variants are reported. One de novo case is documented (PMID:40868138). HP:0001442 (somatic mosaicism) does not apply.
- **Functional class:** most variants likely act by dominant negative / toxic gain of aggregation. The `functional_impact_category` closest to the evidence is probably `DOMINANT_NEGATIVE` or `NEOMORPHIC`; choose one only if a source states it.
  - Many truncating alleles fall in the last exon or near the 3′ end (Y144*, W157X), where nonsense-mediated decay would not be expected to remove the transcript. This is my inference, not a cited finding. The resulting truncated protein self-aggregates (PMID:18421082).
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported.

## 5. Environmental Information

Not applicable. There are no toxin, lifestyle or infectious causes. For an infantile cataract, the main things to rule out are congenital infections (rubella, TORCH) and metabolic causes (galactosemia); these are part of the differential diagnosis, not causes of this disease.

## 6. Mechanism / Pathophysiology

**Causal chain**
1. A heterozygous *CRYGC* missense or truncating variant (germline) **results in** a γC-crystallin with a change in a conserved Greek-key region, or loss of the C-terminal domain (Greek keys 3–4) (PMID:10521291; PMID:26694549).
2. The altered protein **leads to** exposed hydrophobic surface, lower solubility and self-aggregation (shown for W157X, PMID:18421082). For T5P, altered folding and protein–protein interactions are reported [UNVERIFIED, Fu & Liang 2002–2003]. For missense variants in general this is partly inferred, by analogy to *CRYGD* P23T and R58H, which lose solubility without unfolding.
3. Aggregates form inside the cytoplasm of lens fiber cells (CL:0011004). They form in the embryonic and fetal nucleus because γC is expressed early and is concentrated in the central fibers. The location is inferred from expression pattern and from morphology (nuclear and Coppock-like opacities).
4. The resulting high-molecular-weight aggregates and particle formation **lead to** light scattering. This disrupts the short-range order of densely packed crystallin needed for transparency (the GO term GO:0005212 *structural constituent of eye lens* describes that normal function).
5. Light scattering **results in** a congenital lens opacity. Its morphology depends on the variant and on when, during lens development, the affected fiber layer was laid down: nuclear, lamellar or pulverulent.
6. Opacity of the visual axis during the critical period of visual development **leads to** form-deprivation amblyopia, nystagmus and strabismus.
   - **Branch, surgery:** lensectomy **leads to** an aphakic or pseudophakic eye, which carries a risk of glaucoma.
7. **Branch, microcornea:** for some truncating alleles (E135*, W157X), microcornea is reported alongside the cataract. Its mechanism is unknown and may involve abnormal lens growth acting on anterior-segment size. This is a knowledge gap.

**Ontology suggestions (all in the committed caches)**
- **GO:** GO:0005212 structural constituent of eye lens (its MF function is lost or disturbed); GO:0070306 lens fiber cell differentiation; GO:0002088 lens development in camera-type eye; GO:0006457 protein folding; GO:0007601 visual perception (DECREASED).
- **CL:** CL:0011004 lens fiber cell; CL:0002224 lens epithelial cell, which is the cell type used in the transfection model (PMID:18421082).
- **UBERON:** UBERON:0000965 lens of camera-type eye; UBERON:0000970 eye. No cached term exists for the lens nucleus; check UBERON for "nucleus of lens" before binding one.
- **Suggested `biological_scale` tags:** steps 1–2 MOLECULAR, step 3 CELLULAR, steps 4–5 TISSUE, step 6 ORGANISM.

**Molecular profiling, single-cell, omics:** no CTRCT2-specific datasets were found or checked.

## 7. Anatomical Structures Affected

- **Primary:** the crystalline lens (UBERON:0000965), mainly the embryonic and fetal nucleus and the lamellar zones. Usually bilateral.
- **Secondary:** cornea when microcornea is present; visual cortex and the visual system in general through amblyopia.
- **Cell and subcellular level:** cytoplasm of lens fiber cells (CL:0011004), with cytoplasmic protein aggregates.

## 8. Temporal Development

- **Onset:** congenital, or detected in infancy. A juvenile presentation (HP:0001118) is possible for milder opacities.
- **Progression:** generally stationary. Some lamellar or pulverulent forms may become denser over time. There are no natural-history studies.
- **Critical period:** the first weeks to months of life. Dense bilateral cataract is usually operated on at about 6–10 weeks of age to avoid irreversible amblyopia (PMID:35307324, an infantile-cataract management review). The W157X proband was operated on at 1 month (PMID:40868138).

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006), with full or near-full penetrance in the reported pedigrees. De novo cases occur.
- **Expressivity:** variable.
- **Not reported:** anticipation, founder effects, a role for consanguinity.
- **Prevalence of congenital cataract overall:** roughly 1–6 per 10,000 births [general literature, UNVERIFIED].
- **Share caused by *CRYGC*:** crystallin genes account for about half of inherited non-syndromic pediatric cataract (PMID:42091610). *CRYGC* is one of the most frequent among them, but there is no gene-specific prevalence figure. In cohorts:
  - 1 of 23 solved cases in a Chinese cohort (PMID:29914532)
  - 2 of 33 solved families in a UK NGS cohort (PMID:26694549)
  - 1 of 10 solved families in a Swiss cohort (PMID:40868138)
- **Population, sex, geography:** reported in European, Chinese, Indian [UNVERIFIED] and Swiss families. There is no sex bias.

## 10. Diagnostics

- **Clinical:** slit-lamp biomicroscopy to classify morphology; red-reflex screening in newborns; corneal diameter measurement (microcornea); assessment for nystagmus and amblyopia.
- **Genetic:** multigene congenital-cataract NGS panels or exome sequencing are first-line. They give diagnostic yields of more than 70% in familial cohorts (PMID:26694549), 75% familial and 47.8% sporadic (PMID:29914532), and 50% in the Swiss cohort (PMID:40868138). *CRYGC* is on standard panels.
- **Variant interpretation:** use ACMG/AMP criteria. Last-exon truncating variants should be read as likely gain of aggregation, not loss of function.
- **Other tests:** CMA, karyotype and metabolic tests only to rule out syndromic causes.
- **Differential diagnosis:** other crystallin genes (*CRYGD* — the clinically closest; *CRYBB2*, *CRYAA*), connexins (*GJA8*, *GJA3*), *MIP*, *BFSP1/2*, *HSF4*, *MAF*; Nance–Horan syndrome (*NHS*; X-linked, often missed in carrier females — PMID:40868138); galactosemia; congenital rubella.
- **Biomarkers:** none.

## 11. Outcome / Prognosis

- **Life expectancy:** normal. No mortality is attributable to the disease.
- **Visual outcome:** depends mainly on density of the opacity, timing of surgery, and how well amblyopia therapy is followed.
- **Long-term complications:** aphakic glaucoma, visual-axis opacification, strabismus, persistent nystagmus.
- **Prognostic factors:** dense central (nuclear) opacity and late surgery predict poorer acuity. There are no CTRCT2-specific outcome data.

## 12. Treatment

| Treatment | NCIT (cached) | Modality | Notes |
|---|---|---|---|
| Cataract surgery (lensectomy ± intraocular lens) | NCIT:C157809 Cataract Surgery | SURGERY | Early surgery for visually significant opacity; IOL implantation is usually deferred in young infants |
| Optical correction (aphakic contact lens or spectacles) | Not cached; look up | DEVICE | Bind the clinical action, not the device (see CLAUDE.md "Devices are not clinical actions") |
| Amblyopia occlusion therapy | Not cached; look up | BEHAVIORAL | |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — | 50% recurrence risk for offspring of an affected parent |
| Glaucoma surveillance and management | — | — | Lifelong after surgery |

- **Pharmacotherapy:** none disease-modifying.
- **Pharmacogenomics, gene therapy, RNA therapy:** none.
- **Clinical trials:** none for this disease. The lanosterol and 25-hydroxycholesterol "aggregate-dissolving" approaches were tested in animal crystallin cataract models but are not a clinical option [UNVERIFIED].

## 13. Prevention

- **Primary:** none.
- **Secondary:** newborn red-reflex screening; cascade examination of relatives in affected families.
- **Tertiary:** timely surgery, refractive rehabilitation, amblyopia treatment, glaucoma surveillance.
- **Reproductive:** genetic counseling; prenatal or preimplantation testing is possible once the familial variant is known.

## 14. Other Species

- *CRYGC* orthologs are conserved across mammals and fish; the mouse ortholog is *Crygc*.
- No naturally occurring animal *CRYGC* cataract is confirmed. Check OMIA before asserting one [UNVERIFIED].

## 15. Model Organisms

- **In vitro (verified):** EGFP-tagged W157X γC expressed in COS-7 and human lens epithelial cells forms intracellular aggregates; wild-type protein does not (PMID:18421082; `evidence_source: IN_VITRO`). This model recapitulates step 2 of the causal chain at CELLULAR scale. Its limitation: it is a non-lens or epithelial context with overexpression, so no fiber-cell differentiation is involved.
- **Mouse [UNVERIFIED]:** several ENU-induced dominant *Crygc* and γ-crystallin cluster mutants with nuclear and zonular cataract are described by Graw and colleagues. Confirm the allele names in MGI before curating an `animal_models` record.

---

## Evidence Table A — quotes verified against `references_cache/`

| PMID | Supports | Source type | Exact snippet |
|---|---|---|---|
| 10521291 | CRYGC is causal in the Coppock-like family | HUMAN_CLINICAL | "Further analysis of the original Coppock-like-cataract family identified a missense mutation in a highly conserved segment of exon 2 of CRYGC." |
| 10521291 | First evidence for CRYGC | HUMAN_CLINICAL | "To our knowledge, these findings are the first evidence of an involvement of CRYGC and support the role of CRYGD in human cataract formation." |
| 10521291 | CRYGE was a polymorphism | HUMAN_CLINICAL | "the previously reported Coppock-like-cataract mutation, the first human cataract mutation, in the pseudogene CRYGE represented a polymorphism seen in 23% of our control population." |
| 18421082 | Truncation causes self-aggregation | IN_VITRO | "The deletion of C-terminal 18 residues of human gammaC- and gammaD-crystallins exposes the side chains of several hydrophobic residues in the sequence to the solvent, causing the molecule to self-aggregate." |
| 18421082 | Aggregates seen in cells | IN_VITRO | "Transfection of the EGFP-tagged mutant cDNAs into several cell lines led to the visualization of aggregates, whereas that of wild-type cDNAs did not." |
| 42091610 | Definitive gene–disease relationship | OTHER (gene curation; `quote_role: PRIMARY_RESULT`) | "Seven genes (CRYAA, CRYAB, CRYBA1, CRYBB1, CRYBB2, CRYGC, CRYGD) scored as Definitively associated with autosomal dominant (AD) inherited pediatric cataracts." |
| 26694549 | Frameshift alleles predict loss of Greek keys 3–4 | HUMAN_CLINICAL | "with both mutations predicting loss of the third and fourth Greek Key domains of CRYGC." |
| 26694549 | Crystallins dominate NGS yield | HUMAN_CLINICAL | "Two novel heterozygous frameshift mutations in crystallins were identified, one in CRYGC and the other in CRYGD." |
| 40868138 | De novo W157X with nuclear cataract | HUMAN_CLINICAL | "F5 (CRYGC; c.471G>A): index subject (2-3), had nuclear cataracts and underwent surgery at 1 month. He is the only carrier of the variant thus it being de novo." |
| 29914532 | S78F nuclear cataract (table row) | HUMAN_CLINICAL | "F#4 \| M \| 5 years \| Nuclear cataract \| - \| AD \| CRYGC NM_020989.3 \| c.233C>T \| p.(Ser78Phe)" |
| 27878435 | E135* with microcornea (table row) | HUMAN_CLINICAL | "Pediatric cataract with microcornea \| No \| AD \| 7 \| Variant found in a known gene \| CRYGC" |
| 42091610 | Crystallins cause about half of cases | HUMAN_CLINICAL (`quote_role: BACKGROUND`) | "variants in crystallin genes are believed to cause about half of all non-syndromic inherited pediatric cataracts" |

**Notes on the table**
- **Table-row snippets** (PMID:29914532, PMID:27878435): check with `just count-verified-snippets` after placing them. Table pipes normalize, but the row text must match exactly.
- **Missing quote:** I did not see a sentence in the cached W157X/Swiss text stating microcornea, so do not attach microcornea to W157X from these files.

## Evidence Table B — leads to fetch and verify before use [UNVERIFIED]

- **Ren Z et al. 2000, *Hum Genet*:** CRYGC 5-bp insertion, variable zonular pulverulent cataract.
- **Santhiya ST et al. 2002, *J Med Genet*** (PMID:12011157, to confirm): CRYGC R168W, lamellar cataract.
- **Guo Y et al. 2012, *Mol Vis*:** CRYGC W157X, nuclear cataract with microcornea, Chinese pedigree (cited in PMID:40868138).
- **Prokudin I et al. 2014:** CRYGC S166F (cited in PMID:26694549).
- **Fu L & Liang JJ (2002–2003):** biophysics of the T5P conformation and its protein interactions.
- **Mouse *Crygc* ENU alleles:** MGI.

## Curation caveats

1. **Name-collision risk:** "Cataract 2" is not *CRYGD*-related Cataract 4. Do not copy that entry's *CRYGD* P23T/R58H biophysics as CRYGC evidence. PMID:18421082 is the one source that legitimately covers both genes.
2. **HGNC binding:** look up the *CRYGC* CURIE before writing it. It is absent from the cache.
3. **Coppock-like morphology:** HPO has no specific term. Bind HP:0100018 Nuclear cataract and keep the more specific wording in `preferred_term`.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001442` (1 mention) - the report calls it "somatic mosaicism"; HP calls it **Typified by somatic mosaicism**, and lists "Somatic mosaicism" among its other names
- `UBERON:0000965` (2 mentions) - the report calls it "Primary:** the crystalline lens"; UBERON calls it **lens of camera-type eye**, and lists "crystalline lens" among its other names

Every term resolved, and every label the report gave matched.