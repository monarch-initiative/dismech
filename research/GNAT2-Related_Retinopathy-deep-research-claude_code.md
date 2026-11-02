---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-02T00:04:33.514411'
end_time: '2026-11-02T00:08:10.751467'
duration_seconds: 217.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: GNAT2-Related Retinopathy
  mondo_id: MONDO:0800392
  category: Mendelian
  causal_genes: GNAT2
  omim_id: not recorded
  synonyms: achromatopsia 4; GNAT2-related achromatopsia; GNAT2-related cone dystrophy
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
  num_turns: 17
  total_cost_usd: 1.9770189000000002
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 30
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 3
  unresolvable_prefixes:
  - ORPHA
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GNAT2-Related Retinopathy
- **MONDO ID:** MONDO:0800392 (if available)
- **Causal gene(s):** GNAT2
- **OMIM:** not recorded
- **Synonyms:** achromatopsia 4; GNAT2-related achromatopsia; GNAT2-related cone dystrophy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **GNAT2-Related Retinopathy** covering all of the
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

Pulling abstracts for the main GNAT2 papers now, so the report can quote their exact wording.

# GNAT2-Related Retinopathy (MONDO:0800392): research report

**Scope.** This report covers the disease caused by biallelic variants in **GNAT2** (HGNC:4394, written `hgnc:4394` in dismech; OMIM gene \*139340). GNAT2 encodes the α-subunit of cone transducin, the G protein that couples activated cone opsin to the cone phosphodiesterase PDE6C/PDE6H. The MONDO concept GNAT2-related retinopathy (MONDO:0800392) is a gene-anchored umbrella. It covers **achromatopsia 4 (ACHM4)**, which is OMIM #613856 and MONDO:0013465. It also covers the related phenotypes reported with GNAT2 variants: infantile-onset cone dystrophy, incomplete achromatopsia and oligocone trichromacy.

**How the quotes were checked.** All quotes below were taken from PubMed abstracts in this session, using the E-utilities efetch text. They are short excerpts. Before using any of them as a dismech `snippet`, cache the reference with `just fetch-reference` and run `just count-verified-snippets`.

**Ontology terms.** The CURIEs given as candidates were not looked up in this session. Each one must be confirmed with `runoak` or the term caches before it is bound, as the project's term rules require.

---

## 1. Disease information

**Overview.** GNAT2-related retinopathy is an autosomal recessive cone photoreceptor disorder. It is usually congenital or infantile in onset, and it typically presents as achromatopsia:
- nystagmus from infancy
- photophobia (light sensitivity)
- reduced visual acuity
- absent or severely reduced colour discrimination
- absent or severely reduced cone ERG responses, with rod function largely preserved

GNAT2 was the third achromatopsia gene to be identified. Kohl et al. 2002 wrote: *"Our results demonstrate that GNAT2 is the third gene implicated in achromatopsia."* (PMID:12077706)

**Identifiers**

| System | ID | Notes |
|---|---|---|
| MONDO | MONDO:0800392 (GNAT2-related retinopathy) | Gene-anchored umbrella term |
| MONDO | MONDO:0013465 (achromatopsia 4) | Narrower: the classic ACHM4 presentation |
| OMIM | #613856 ACHM4; \*139340 GNAT2 (gene) | The template listed OMIM as "not recorded". 613856 is the nearest phenotype entry. |
| Orphanet | ORPHA:49 (Achromatopsia) | Orphanet submits GNAT2 to GenCC under achromatopsia (MONDO:0018852) and cone dystrophy (MONDO:0000455), both "Supportive" |
| ICD-10 | H53.5x (colour vision deficiencies; achromatopsia sits in this block) | Exact code not verified |
| GenCC | ClinGen: **Definitive, autosomal recessive**, for MONDO:0800392. G2P: Definitive (ACHM4). Labcorp/Invitae and PanelApp Australia: Strong. Ambry: Moderate. | [GenCC HGNC:4394](https://thegencc.org/genes/HGNC:4394) |

**Synonyms.** Achromatopsia 4; ACHM4; GNAT2-related achromatopsia; GNAT2-associated achromatopsia (GNAT2-ACHM); GNAT2-related cone dystrophy; rod monochromacy (historical).

**Source of information.** All of it comes from aggregated case series and cohorts, plus disease-level resources (OMIM, Orphanet, GenCC). None of it comes from EHR data.

**Recommendation for the dismech entry.** The ClinGen GenCC submission names MONDO:0800392 directly. Its CGGV record could therefore be recorded in `gene_disease_validity` with `classified_by: CLINGEN`. The CGGV assertion ID was not retrieved here. Fetch it with `just clingen-list` or `just fetch-reference`; do not compose it.

---

## 2. Etiology

**Causal factor.** The disease is caused by biallelic loss-of-function variants in GNAT2 (1p13.3).
- Kohl et al. found protein-truncating mutations in *"five independent families with achromatopsia"* (PMID:12077706).
- Aligianis et al. independently mapped ACHM4 to 1p by autozygosity mapping in a consanguineous Pakistani family. They identified *"a frameshift mutation in exon 7 (c842_843insTCAG; M280fsX291)"* (PMID:12205108).

**Genetic risk factors.**
- **Consanguinity** is the main risk factor. Most reported families are consanguineous, for example in Pakistan (PMID:12205108) and Tunisia (PMID:21107338).
- **Founder alleles.** The Tunisian p.R313X allele is described as likely a founder mutation (PMID:21107338).

**Modifier genes.** None have been established. The phenotypic spread within families has been attributed to allele "leakiness" rather than to modifier genes. In two cousins, a leaky splice allele produced a milder oligocone-trichromacy picture (PMID:15557429).

**Environmental risk factors, protective factors and gene–environment interactions.** None are known for this monogenic disease. No protective variants have been reported.

---

## 3. Phenotypes

Two cohorts give the core picture. Georgiou et al. 2020 studied 9 patients: *"All nine subjects (3 women) presented with nystagmus, decreased visual acuity (VA), light sensitivity"* (PMID:32203983). In the Michaelides 2003 family: *"All five examined patients had a history of nystagmus from infancy, photophobia, defective colour vision"* (PMID:14609822).

| Phenotype | Type | Onset / course | Frequency | Candidate HPO term (verify) |
|---|---|---|---|---|
| Nystagmus (pendular, infantile) | Sign | Infancy; often improves with age | ~100% in case series | HP:0000639 Nystagmus |
| Photophobia / light sensitivity | Symptom | Infancy; lifelong | ~100% | HP:0000613 Photophobia |
| Reduced visual acuity (~20/120–20/200 typical) | Sign | Congenital; mostly stationary | ~100% | HP:0007663 Reduced visual acuity |
| Absent or severely impaired colour vision (complete achromatopsia, i.e. monochromacy) or residual colour vision (incomplete) | Sign | Congenital | Nearly all; incomplete forms and oligocone trichromacy occur (PMID:15557429) | HP:0011516 Rod monochromacy / HP:0000551 Abnormality of color vision |
| Absent or severely reduced photopic and 30-Hz flicker ERG; scotopic ERG normal or near-normal | Lab / electrophysiology | Present from early life | ~100% | HP:0012268 Abnormal cone ERG? (needs term lookup) |
| Hemeralopia (day blindness) | Symptom | Congenital | Common | HP:0012047 Hemeralopia |
| Myopia | Sign | Childhood | Possibly over-represented with GNAT2 (Danish cohort, PMID:36980963) | HP:0000545 Myopia |
| Foveal hypoplasia or mild ellipsoid-zone disruption on OCT | Imaging | Variable | Subset | HP:0007750 Hypoplasia of the fovea |
| Progressive decline in visual acuity (cone dystrophy phenotype) | Sign | Childhood–adulthood | Minority (PMID:14609822) | HP:0000529 Progressive visual loss |

**Quality of life.** Photophobia and low acuity limit reading, driving eligibility, outdoor function and education. No GNAT2-specific EQ-5D or SF-36 data exist. Patients typically use tinted lenses and low-vision aids.

---

## 4. Genetic and molecular information

- **Gene and protein.** GNAT2 (`hgnc:4394`; OMIM \*139340; chromosome 1p13.3) encodes the guanine nucleotide-binding protein G(t) subunit α-2, cone transducin α (Gαt2).
- **Mutation spectrum.** Felden et al. 2019 screened 1,116 families with achromatopsia and identified *"23 patients with ACHM from 19 independent families with likely causative mutations in GNAT2"*. They describe this as *"representing 1.7% of our large ACHM cohort"*. The 22 variants include 12 novel ones and a novel exon 4 duplication (PMID:31058429). Kohl 2002 also estimated the GNAT2 share of achromatopsia at under 2% (PMID:12077706).
- **Variant classes.** Most variants are truncating: nonsense, frameshift, splice and small indels. Examples:
  - c.235C>T, p.Gln79\* (OMIM)
  - c.285_291del7insCTGTAT
  - c.842_843insTCAG, p.Met280Ilefs\*12 (M280fsX291), from the Pakistani family and the British 3-generation family (PMID:12205108, PMID:14609822)
  - p.Tyr95fs (PMID:15557429)
  - c.937C>T, p.Arg313\* (Tunisian founder; ClinVar Pathogenic) (PMID:21107338)
  - c.730_743del, homozygous, in a Japanese patient (PMID:27718025)
  - a coding exon 4 duplication (PMID:31058429)

  Missense variants are rare and need careful interpretation. A K270 deletion did **not** co-segregate with disease and is considered non-causal (PMID:15094710).
- **Functional consequence.** Loss of function (null or hypomorphic). Leaky splice alleles give milder phenotypes. No gain-of-function or dominant-negative mechanism is known.
- **Origin.** Germline.
- **Allele frequency.** Pathogenic alleles are individually rare in gnomAD. No common pathogenic allele is known.
- **Other categories.** No epigenetic contribution, chromosomal abnormalities or modifier genes are known.

---

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious contributors are known. Bright light worsens symptoms (photophobia), but it does not cause the disease.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic truncating or hypomorphic GNAT2 variants lead to** absent or markedly reduced functional cone transducin α in cone outer segments. For truncating alleles this is inferred from the variant class. In mice it has been shown directly (PMID:17065522, PMID:29518352).
2. **Loss of Gαt2 means that** light-activated cone opsins (S-, M- and L-opsin) cannot activate cone PDE6 (PDE6C/PDE6H). The amplification step of cone phototransduction fails. In the Gnat2^cpfl3 mouse, *"The decreased sensitivity and amplification rate of cones is not explained by a reduction in GNAT2 protein"* alone, which points to defective transducin signalling (PMID:32315379).
3. **Without PDE6 activation, cGMP in cones does not fall, CNG channels stay open and the cone does not hyperpolarise.** The result is absent or severely reduced cone photoresponses, while rod phototransduction through GNAT1 is spared.
4. **No cone signal reaches the cone bipolar cells, which results in** an absent photopic ERG, loss of daylight vision and loss of colour discrimination (achromatopsia).
5. **Vision under photopic conditions therefore relies on saturated rods, which results in** photophobia, hemeralopia and low acuity. Congenital loss of foveal cone input during visual development is thought to produce infantile nystagmus. This step is inferred: it is the general sensory-nystagmus mechanism, not one demonstrated specifically for GNAT2.
6. **Branch: what happens to the cones themselves.**
   - **6a.** In most GNAT2 patients the cone structure is relatively preserved: *"The cone mosaic in GNAT2-ACHM is relatively well preserved, potentially allowing for a wide therapeutic window"* (PMID:32203983). Cone density was reduced by only 15–30% in a Japanese patient (PMID:27718025). In mice, Gnat2 knockout causes *"loss of cone function without degeneration"* (PMID:29518352).
   - **6b.** In a subset of patients, and in misfolding missense mouse models, progressive cone degeneration follows. Examples are the human cone dystrophy phenotype with declining acuity (PMID:14609822) and the Gnat2^c.518A>G mouse, which shows cone loss, opsin mislocalisation and retinal remodelling (PMID:23580486). The mouse findings suggest that misfolded transducin, rather than mere absence, may drive degeneration. Progressive ellipsoid-zone disruption is reported in mixed-gene achromatopsia cohorts (PMID:39287548), but it is not GNAT2-specific.

### Checklist detail

- **Pathways.** Cone phototransduction: KEGG hsa04744 (Phototransduction); Reactome "Activation of the phototransduction cascade".
- **Candidate GO terms (verify):**
  - GO:0007602 phototransduction
  - GO:0007603 phototransduction, visible light
  - GO:0050908 detection of light stimulus involved in visual perception
  - GO:0003924 GTPase activity, as a molecular function, modifier DECREASED or loss
  - GO:0001750 photoreceptor outer segment, as a cellular component
  - GO:0042670 retinal cone cell differentiation? Do not use this one: the evidence does not support a differentiation defect.
- **Candidate CL terms:** CL:0000573 retinal cone cell; CL:0000604 retinal rod cell (spared); cone bipolar cell (downstream).
- **Protein dysfunction.** Truncating alleles cause loss of the GTPase/Ras-like domain and the effector (PDE6γ-binding) interface. Some missense alleles cause misfolding (mouse c.518A>G).
- **Immune, metabolic and epigenetic changes.** None are characterised for GNAT2. A related report: UNC119, a transducin-binding trafficking protein, produces cone-rod dystrophy with JAK-STAT and NF-κB inflammatory activation (PMID:41107067). That is a different gene and must not be transferred to GNAT2.
- **Omics.** No GNAT2-specific transcriptomic, proteomic or single-cell datasets were identified.

---

## 7. Anatomical structures affected

- **Organ and system.** The retina (UBERON:0000966), bilaterally, especially the fovea and macula (UBERON:0000054 / macula lutea; verify IDs). The nervous and visual system is involved; there is no systemic disease.
- **Cells and subcellular compartments.** Retinal cone cells (CL:0000573), specifically the cone outer segment, which is the site of phototransduction. Candidate GO terms: GO:0120200 rod photoreceptor outer segment, or a cone-specific term if one exists (verify).
- **Lateralisation.** Bilateral and symmetric.

---

## 8. Temporal development

- **Onset.** Congenital or early infancy. Nystagmus and photophobia are noticed in the first months of life.
- **Course.**
  - In most patients the disease is largely stationary in function. Danish cohort: *"support the evidence that achromatopsia is a predominantly stationary condition with respect to BCVA"* (PMID:36980963). Visual acuity *"remained stable despite changing foveal structure"* (PMID:38348755).
  - A minority have a progressive infantile-onset cone dystrophy with declining acuity (PMID:14609822).
  - In mixed-gene cohorts, some authors argue that achromatopsia is progressive (PMID:33562422; PMID:19592100).
- **Duration.** Lifelong. There is no remission.
- **Critical window.** Preserved cone structure suggests a wide window for gene therapy (PMID:32203983). Early childhood is likely optimal for cortical plasticity, but this is inferred.

---

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (candidate term HP:0000007). Penetrance is complete for biallelic null alleles.
- **Expressivity.** Variable: complete achromatopsia, incomplete achromatopsia, oligocone trichromacy, or progressive cone dystrophy (PMID:15557429; PMID:14609822).
- **Anticipation and germline mosaicism.** None reported.
- **Prevalence.** Achromatopsia overall affects about 1 in 30,000–50,000 people. GNAT2 accounts for about 1.7–2% of cases (PMID:31058429; PMID:12077706). That gives a rough GNAT2-ACHM prevalence on the order of 1 per 1.5–3 million. This is an extrapolation, not a directly measured figure.
- **Founder effects and populations.**
  - Tunisian p.R313X founder (PMID:21107338).
  - Consanguineous Pakistani families (PMID:12205108).
  - In Korea, GNAT2 caused 2 of 21 cases (9.5%) (PMID:36833446).
  - In Japan, 2 families out of a PDE6C- and CNGA3-dominated cohort (PMID:39287548).
  - In the Dutch cohort, none (PMID:19592100).
- **Sex ratio.** About 1:1, as expected for an autosomal recessive disease.

---

## 10. Diagnostics

- **Electrophysiology.** Full-field ERG under ISCEV standards shows absent or near-absent light-adapted single-flash and 30-Hz flicker responses, with normal or near-normal dark-adapted rod responses.
- **Colour vision testing.** Anomaloscope, Hardy–Rand–Rittler plates and Farnsworth tests.
- **Imaging.**
  - OCT: preserved or mildly disrupted foveal ellipsoid zone; foveal hypoplasia in some patients.
  - Adaptive optics (AOSLO): a contiguous, relatively preserved cone mosaic compared with CNGA3 or CNGB3 disease (PMID:32203983; PMID:27718025).
  - Fundus autofluorescence: usually normal or showing mild changes.
- **Genetic testing.** Use an inherited retinal disease or achromatopsia panel covering CNGA3, CNGB3, GNAT2, PDE6C, PDE6H and ATF6. RPGRIP1 should now be included as well, because of the Japanese structural variant (PMID:39669618; PMID:41666299). Exome or genome sequencing with CNV calling is useful because exon-level duplications occur (PMID:31058429). There is no role for CMA, karyotype, FISH, mtDNA or repeat-expansion testing.
- **Differential diagnosis:**
  - other achromatopsia genes (CNGA3, CNGB3, PDE6C, PDE6H, ATF6)
  - blue-cone monochromacy (OPN1LW/OPN1MW; X-linked; S-cone function preserved)
  - early-onset cone or cone-rod dystrophies
  - Leber congenital amaurosis (rod ERG also abnormal)
  - albinism and idiopathic infantile nystagmus
  - oligocone trichromacy
- **Screening.** No newborn screening. Carrier and cascade testing applies in consanguineous families.

---

## 11. Outcome and prognosis

- **Survival and mortality.** Normal life expectancy. There is no disease-specific mortality.
- **Morbidity.** Lifelong low vision, usually in the legal-blindness or severe-impairment range. Patients are usually ineligible to drive and face educational and occupational limitations.
- **Prognosis.** Visual function is mostly stable. A minority have progressive acuity loss (PMID:14609822). No prognostic biomarkers have been validated. Cone mosaic preservation on AOSLO is a candidate stratifier for therapy eligibility.

---

## 12. Treatment

**Current care** is supportive only. Candidate NCIT terms need lookup; the ones below are from the CLAUDE.md list.

| Intervention | Candidate NCIT term | Modality |
|---|---|---|
| Red or brown filtered tinted lenses and sunglasses for photophobia | Device. The device term cannot sit in the `TreatmentTerm` slot, so bind the action and carry the device as a qualifier. | DEVICE |
| Low-vision aids and visual rehabilitation | NCIT:C15315 Rehabilitation | BEHAVIORAL |
| Refractive correction (myopia is common) | — | DEVICE |
| Genetic counselling | NCIT:C15240 Genetic Counseling | — |
| Educational support | NCIT:C15747 Supportive Care | — |

**Gene therapy.**
- **Preclinical.** AAV gene replacement rescued cone function in Gnat2^cpfl3 mice. The authors report the ability to *"rescue both the cone-mediated electroretinogram response and visual acuity"* (PMID:17515894). A cone-specific promoter for this purpose was developed (PMID:24664760).
- **Clinical.** No GNAT2-specific human trial was identified. Human achromatopsia AAV trials have targeted CNGA3 and CNGB3, for example NCT02599922, NCT02610582, NCT02935517 and NCT03001310. These are not applicable to GNAT2, but they inform how feasible the approach is (reviewed in PMID:39273686). The candidate NCIT action term is NCIT:C15238 Gene Therapy (GENE_THERAPY).
- **Pharmacotherapy and pharmacogenomics.** None.

---

## 13. Prevention

- **Primary prevention.** Not applicable. Reproductive options in known carrier families include preimplantation genetic testing and prenatal diagnosis.
- **Secondary prevention.** Early genetic diagnosis allows timely low-vision intervention and possible trial eligibility.
- **Tertiary prevention.** Photoprotection improves comfort. There is no evidence that it changes the course of the disease.
- **Other prevention categories.** Genetic counselling for autosomal recessive recurrence risk (25% per pregnancy) and cascade carrier testing. No vaccines or public-health measures apply.

---

## 14. Other species and natural disease

- **Mouse (NCBITaxon:10090):** the spontaneous Gnat2^cpfl3 and Gnat2^c.518A>G strains (see section 15).
- **Dogs:** no naturally occurring GNAT2 disease is reported in OMIA. Canine day blindness or achromatopsia maps to CNGB3 (Alaskan Malamute, German Shorthaired Pointer) and CNGA3. GNAT2 was examined as a candidate gene in wire-haired dachshund day blindness, and no causal variant was reported (PMID:18593457).
- **Sheep:** day blindness is caused by CNGA3 (PMID:19874885), not GNAT2.
- **Conservation.** Gαt2 is highly conserved across vertebrates. Rod and cone transducin α-subunits are functionally largely interchangeable in mice (PMID:19815523; PMID:20603337).
- **Zoonotic potential.** None.

---

## 15. Model organisms

| Model | Genetics | Phenotype recapitulation | Limitations | PMID |
|---|---|---|---|---|
| Gnat2^cpfl3 mouse | Spontaneous missense in exon 6 | *"poor cone-mediated responses on ERG at 3 weeks that became undetectable by 9 months"*; progressive loss of cone α-transducin labelling; cones structurally intact at 14 weeks | Hypomorph, not a null: it *"cannot be assumed to be a Gnat2 null"* (PMID:32315379). Rod responses also decline with age. The mouse lacks a fovea. | 17065522, 32315379 |
| Gnat2^c.518A>G mouse | Spontaneous missense (misfolding) | No cone response; cone loss, opsin mislocalisation and remodelling by 12 months | Degeneration is more severe than in typical human GNAT2-ACHM | 23580486 |
| Gnat2^−/− knockout | Targeted null | *"complete loss of cone-driven a-waves"*; *"no loss of cones"* | Closest to the human null genotype; no fovea | 29518352 |
| Gnat1/Gnat2 double knockout and VEP studies | Targeted | Probe residual non-transducin pathways | Tool model | 36605613 |
| AAV rescue in cpfl3 | Gene therapy | Restored cone ERG and acuity | Mouse vs human cone density and fovea | 17515894 |

- **Databases.** MGI (Gnat2), IMPC, JAX (cpfl3 strain).
- **Other systems.** No zebrafish GNAT2 disease model or human iPSC/organoid model specific to GNAT2 was identified in this search. That is a knowledge gap.
- **Translational note.** Mouse knockouts show function loss without degeneration, which matches the relatively preserved cone mosaic in humans. The misfolding missense model degenerates. Whether human missense alleles behave the same way is unknown, and would be a candidate `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion in the entry.

---

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 12077706 | Kohl S et al. *Am J Hum Genet* 2002 — GNAT2 mutations in achromatopsia | Human clinical |
| 12205108 | Aligianis IA et al. *J Med Genet* 2002 — ACHM4 mapping, M280fsX291 | Human clinical |
| 14609822 | Michaelides M et al. 2003 — cone dystrophy phenotype with M280fsX291 | Human clinical |
| 15557429 | Rosenberg T et al. 2004 — incomplete achromatopsia / oligocone trichromacy | Human clinical |
| 15094710 | Piña AL et al. 2004 — K270del, not causal | Human clinical / computational |
| 21107338 | Ouechtati F et al. 2011 — Tunisian p.R313X | Human clinical |
| 27718025 | Ueno S et al. 2017 — AOSLO, c.730_743del | Human clinical |
| 31058429 | Felden J et al. *Hum Mutat* 2019 — mutation spectrum (19 of 1,116 families) | Human clinical |
| 32203983 | Georgiou M et al. 2020 — photoreceptor structure in GNAT2-ACHM | Human clinical |
| 36980963 | Andersen MKG et al. 2023 — Danish cohort | Human clinical |
| 38348755 | Andersen MKG et al. 2024 — Danish cohort phenotypes | Human clinical |
| 36833446 | Choi YJ et al. 2023 — Korean cohort | Human clinical |
| 39287548 | Inooka T et al. 2024 — Japanese cohort | Human clinical |
| 17065522 | Chang B et al. 2006 — cpfl3 mouse | Model organism |
| 23580486 | Jobling AI et al. 2013 — Gnat2 c.518A>G mouse | Model organism |
| 29518352 | Ronning KE et al. 2018 — Gnat2 knockout | Model organism |
| 32315379 | Chen NS et al. 2020 — cpfl3 transducin signalling | Model organism |
| 17515894 | Alexander JJ et al. *Nat Med* 2007 — AAV rescue | Model organism |
| 39273686 | Baxter MF et al. 2024 — gene therapy for achromatopsia, review | Review |

**Web sources consulted:**
- [GenCC HGNC:4394](https://thegencc.org/genes/HGNC:4394)
- [OMIM #613856 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/613856)
- [OMIM \*139340 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/139340)
- [Felden 2019 (Region H)](https://research.regionh.dk/da/publications/mutation-spectrum-and-clinical-investigation-of-achromatopsia-pat/)
- [Chen 2020 cpfl3 (PMC7401474)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7401474/)
- [Ronning 2018 (PMC5987249)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5987249)
- [ClinVar Miner p.Arg313Ter](https://clinvarminer.genetics.utah.edu/submissions-by-variant/NM_001377295.2%28GNAT2%29%3Ac.937C%3ET%20%28p.Arg313Ter%29)
- [JAX gene therapy news](https://cm.sc.jax.org/news-and-insights/2007/october/gene-therapy-restores-vision-to-blind-mice)
- [MedlinePlus GNAT2](https://medlineplus.gov/genetics/gene/gnat2)
- [PubMed search](https://pubmed.ncbi.nlm.nih.gov/?term=GNAT2+achromatopsia+OR+GNAT2+cone+dystrophy)

**Information not found:**
- GNAT2-specific prevalence, quality-of-life instruments, omics datasets, iPSC or organoid models, and human clinical trials
- ICD-11 code (not verified)
- the ClinGen CGGV assertion ID for MONDO:0800392

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 30 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

31 of 33 terms resolved to a current term; the rest could not be looked up either way.