---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-26T20:29:15.711752'
end_time: '2026-10-26T20:30:53.712075'
duration_seconds: 98.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Recessive Spinocerebellar Ataxia 17
  mondo_id: MONDO:0014503
  category: Mendelian
  causal_genes: CWF19L1
  omim_id: OMIM:616127
  synonyms: CWF19L1 autosomal recessive congenital cerebellar ataxia; SCAR17; autosomal
    recessive congenital cerebellar ataxia caused by mutation in CWF19L1; autosomal
    recessive spinocerebellar ataxia type 17; spinocerebellar ataxia autosomal recessive
    type 17; spinocerebellar ataxia, autosomal recessive type 17
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
  num_turns: 9
  total_cost_usd: 0.7847518
  session_id: 402da01d-554f-59a0-9730-4f6c8133551c
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 3
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 16
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMID:41422678
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 3
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Spinocerebellar Ataxia 17
- **MONDO ID:** MONDO:0014503 (if available)
- **Causal gene(s):** CWF19L1
- **OMIM:** OMIM:616127
- **Synonyms:** CWF19L1 autosomal recessive congenital cerebellar ataxia; SCAR17; autosomal recessive congenital cerebellar ataxia caused by mutation in CWF19L1; autosomal recessive spinocerebellar ataxia type 17; spinocerebellar ataxia autosomal recessive type 17; spinocerebellar ataxia, autosomal recessive type 17
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Spinocerebellar Ataxia 17** covering all of the
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

Now abstracts of key papers.

# Autosomal Recessive Spinocerebellar Ataxia 17 (SCAR17; CWF19L1-related ataxia): research report

**Source classes:** I read PubMed titles and abstract summaries through E-utilities, plus GenCC, MalaCards and PanelApp search snippets. I did not read full texts. The fetch tool would not return abstracts verbatim, so the only quotes below are the short excerpts it returned. Every other statement is a paraphrase of an abstract summary.

**Gaps in this report:**
- Frequencies, per-patient tables, imaging details and the zebrafish phenotype details were not checked against full text.
- I did not search for mouse or other-species models beyond the 2014 zebrafish work.
- Ontology identifiers were not looked up. Suggested HPO, GO, CL and UBERON entries are given as term names only, and each is a lead to be resolved with a lookup before binding.
- The Section 6 steps marked "inferred" are my reasoning, not source statements.

---

## 1. Disease information

SCAR17 is caused by biallelic loss-of-function variants in **CWF19L1** (HGNC:25613; 10q24.31; OMIM disease 616127). The identifiers given in the template are MONDO:0014503 and OMIM:616127. I did not independently verify the MONDO ID or any ORPHA or ICD mapping. The clinical picture is an early-onset cerebellar ataxia with cerebellar atrophy, often with intellectual disability. The course runs from non-progressive congenital ataxia to slowly progressive atrophy (MalaCards, a structured-database aggregator: https://malacards.org/card/spinocerebellar_ataxia_autosomal_recessive_17).

GenCC rates the gene-disease relationship as **definitive** for autosomal recessive cerebellar ataxia (https://thegencc.org/submissions/SGC-106813.2, via search snippet). I did not open the ClinGen record, so there is no CGGV citation. PanelApp also lists the gene on an intellectual disability panel (https://panelapp.genomicsengland.co.uk/panels/285/gene/CWF19L1/).

Synonyms are as given in the template. The data come from published family and cohort reports, not from EHR. This is a germline Mendelian disorder with no somatic counterpart.

---

## 2. Etiology

- **Cause:** Homozygous or compound heterozygous CWF19L1 variants. The first reports described loss-of-function alleles: a splice-donor variant (c.964+1G>A; PMID:25361784) and a frameshift (PMID:27016154).
- **Risk factors:** I found no environmental or protective factors and no gene-environment interactions.
- **Modifiers:** None reported in what I read. A variant-type genotype-phenotype pattern is suggested (Section 4).
- **Unrelated GWAS hits:** PubMed also returns liver-fat and NAFLD association papers for the *ERLIN1–CHUK–CWF19L1* locus (PMID:23477746, PMID:24785259, PMID:34558842). These are not relevant to SCAR17.

---

## 3. Phenotypes

Evidence is limited to small family reports and one small cohort.

| Phenotype | Notes and source | Suggested HPO term (name only) |
|---|---|---|
| Cerebellar ataxia, gait unsteadiness | Core feature in all reports (PMID:25361784, 26197978, 27016154). Onset is usually early childhood. | Gait ataxia; Truncal ataxia |
| Cerebellar atrophy | Mildly progressive on serial MRI in one boy (PMID:27016154). Atrophy is also reported in PMID:26197978 and in the Eastern-Spain/Brazil series. | Cerebellar atrophy |
| Intellectual disability, mild | PMID:27016154; PMID:36357319 (progressive ataxia plus intellectual disability). | Intellectual disability, mild |
| Developmental delay | Reported (PMID:36453471; MalaCards). | Global developmental delay |
| Dysarthria, nystagmus, intention tremor | Listed as common cerebellar signs by MalaCards. I did not verify these in primary papers. | Dysarthria; Nystagmus; Intention tremor |
| Dystonia | A 2020 compound heterozygous family abstract noted it as recurrent. I did not locate the primary source. | Dystonia |
| Epilepsy | Two Saudi sisters with late-onset ataxia and seizures, a novel homozygous missense c.395A>G, p.(Asp132Gly) (PMID:33012273). Epilepsy is also described in the series in PMID:36453471. | Seizure |

- **Severity:** The 2020 abstract's authors judged the missense plus nonsense compound heterozygous genotype milder than homozygous truncating alleles. This is a single-family observation.
- **Quality-of-life data:** None found.

---

## 4. Genetic and molecular information

- **Gene:** CWF19L1 (HGNC:25613), 14 exons, 10q24.31 (MalaCards).
- **Reported families, all from PubMed abstract summaries:**
  - Turkish consanguineous family, homozygous splice-donor c.964+1G>A (PMID:25361784). Burns et al. also knocked the gene down in zebrafish.
  - Dutch girl, compound heterozygous variants. The authors wrote "Our data confirm CWF19L1 as a novel but rare gene causing ARCA" (PMID:26197978).
  - Turkish boy with a homozygous frameshift. A related fetus carried the same variant (PMID:27016154).
  - Saudi sisters, homozygous missense (PMID:33012273).
  - Chinese family, two novel variants. The abstract says "heterozygous", but the title says SCAR17, which is recessive, so these are presumably compound heterozygous. I did not confirm this (PMID:36357319).
  - Two Indian families with novel homozygous variants, including a splice-acceptor variant with aberrant transcripts (PMID:37752213).
  - Four new patients plus a literature review (PMID:36453471).
  - A congenital ataxia cohort in which CWF19L1 was one of 18 genes found (PMID:38681507).
- **Variant classes:** Splice, frameshift, nonsense and missense. ClinVar reportedly holds 29 variations (MalaCards, aggregator). I did not query ClinVar, ClinGen or gnomAD directly.
- **Functional consequence:** Loss of function. Absent protein was reported in patient cells for the frameshift family, according to a search-result summary of PMID:27016154. I could not confirm this in the abstract.
- **Not found:** No epigenetic or chromosomal abnormality data, and no somatic involvement.

---

## 5. Environmental information

No environmental, lifestyle or infectious factors are known.

---

## 6. Mechanism and pathophysiology

**Causal chain** (steps 1–3 are demonstrated, steps 4–6 are inferred):
1. Biallelic loss-of-function CWF19L1 variants cause loss or truncation of the protein (demonstrated at the genetic level; protein loss in cells was reported for one family).
2. This leads to defective function of a protein that interacts with the lariat-debranching enzyme hDbr1 and shuttles between nucleus and cytoplasm (PMID:25671812). Masaki et al. report "hDrn1 directly interacts with hDbr1 through protein-protein interaction." hDrn1 is the CWF19L1 protein.
3. CWF19L1 is a splicing regulator. It interacts with U5 snRNP components and the PRPF19 complex, and its loss disrupts alternative splicing of immune-related genes in T cells (PMID:39542248). **This is a T-cell, not neuronal, system.**
4. *Inferred:* Splicing or lariat-processing dysfunction, with intron-turnover and cell-type-specific splicing defects, impairs cerebellar neuron development or survival. No neuronal splicing data were found in this search.
5. *Inferred:* Cerebellar atrophy follows, with onset in early childhood.
6. This produces ataxia and intellectual disability.

- **Branching:** The report in PMID:33012273 of epilepsy and later onset, and the dystonia seen in a compound heterozygous family, suggest involvement beyond the cerebellum. The authors say this may implicate multiple levels of the nervous system.
- **Not supported:**
  - The cell-cycle link in the gene name comes from yeast homology. In glioma cells, increased CWF19L1 was reported to drive G1 arrest through CDK4/6 (PMID:32508030). This is a cancer-cell finding with no established role in SCAR17.
  - A related paralog paper (PMID:41422678) concerns CWF19L2 and lariat debranching.
- **Suggested GO terms (names only):** mRNA splicing via spliceosome; RNA lariat debranching enzyme activator activity (the latter is a predicted annotation).
- **Cell types:** Cerebellar Purkinje cell and cerebellar granule cell are the likely targets, but this is inferred.
- **Not found:** Omics data, single-cell data and CRISPR screens.

---

## 7. Anatomical structures affected

- The cerebellum is the primary site, with atrophy on MRI (PMID:27016154). Suggested UBERON term: cerebellum.
- Other CNS involvement is suggested by epilepsy and intellectual disability (PMID:33012273).
- Subcellular compartments: nucleus and cytoplasm (shuttling, PMID:25671812); spliceosome (GO cellular component).
- I found no data on lateralization.

---

## 8. Temporal development

- **Onset:** Usually early childhood. One late-onset family is reported (PMID:33012273). The 9-year-old boy in PMID:27016154 had early-onset ataxia.
- **Course:** Variable. It ranges from non-progressive congenital ataxia to slowly progressive atrophy (MalaCards). Serial MRI showed mild progression in one patient (PMID:27016154).
- **Not found:** Staging, remission patterns and critical periods.

---

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive. The consanguineous Turkish and Saudi families are consistent with homozygosity by descent. Consanguinity is a documented factor in these families.
- **Geography:** Reported in Turkish, Dutch, Saudi, Chinese, Indian, Spanish and Brazilian patients. I found no founder effects.
- **Prevalence and incidence:** Not found. Orphanet and gnomAD carrier data were not queried.
- **Penetrance, anticipation, mosaicism:** No data. Anticipation and germline mosaicism are not expected for an autosomal recessive loss-of-function disorder (my inference).

---

## 10. Diagnostics

- **Genetic testing:** The gene is found by exome sequencing or ataxia panels. CWF19L1 was diagnostic in a congenital ataxia cohort of 30 Brazilian patients, where 46.7% had a genetic diagnosis (PMID:38681507). In an Eastern-Spain ataxia series (130 families), 39% had a pathogenic or likely pathogenic variant, rising to 47% with SCA36 screening (PMID:36530930). That paper's abstract summary did not mention CWF19L1.
- **Imaging:** MRI shows cerebellar atrophy or hypoplasia.
- **Functional confirmation:** RNA studies can confirm aberrant splicing of splice variants (PMID:37752213).
- **Differential diagnosis:** Other recessive cerebellar ataxias and congenital ataxias, and any early-onset ataxia with intellectual disability. I did not pull GeneReviews, since I could not confirm a SCAR17 chapter; it can be checked offline with `just check-genereviews`.
- **Not found:** Biomarkers, newborn screening and diagnostic criteria.

---

## 11. Outcome and prognosis

- **Survival:** No data found.
- **Function:** Variable. Some patients have non-progressive ataxia and others slowly progressive atrophy.
- **Prognostic factors:** The 2020 abstract suggests milder disease with compound missense/nonsense genotypes. This is not confirmed.

---

## 12. Treatment

- No disease-specific therapy was found.
- **Supportive care** (my inference, not from a source): physical, occupational and speech therapy, and antiseizure treatment where epilepsy occurs. NCIT candidates: Physical Therapy, Occupational Therapy, Speech Language Therapy, Supportive Care. The identifiers still need a lookup.
- No clinical trials or pharmacogenomic data were found. ClinicalTrials.gov was not searched.

---

## 13. Prevention

- Genetic counseling (autosomal recessive risk, 25% per pregnancy), carrier testing of relatives, and prenatal or preimplantation testing once the familial variants are known.
- A fetus carrying the familial variant was identified in PMID:27016154.

---

## 14. Other species and natural disease

I did not search OMIA or VBO. I found no naturally occurring disease in other species. Orthologs are annotated in zebrafish (ZFIN ZDB-GENE-031204-5), mouse and rat; this is from search snippets only.

---

## 15. Model organisms

- **Zebrafish:** Morpholino knockdown of cwf19l1 altered cerebellar morphology and caused movement abnormalities (PMID:25361784). This is MODEL_ORGANISM evidence.
- **Mouse:** Not searched (MGI/IMPC). A Cwf19l1 gene summary exists, but I read no phenotype data.
- **T-cell loss-of-function studies** (PMID:39542248) address splicing biology, not the ataxia phenotype.
- **Limits:** A knockdown is not a stable knockout, and a morpholino carries off-target risk. Human neuronal relevance is unconfirmed.

---

## Curation leads, labelled as leads

- Resolve all HPO, GO, CL, UBERON and NCIT candidates above by lookup before binding any of them.
- Retrieve full abstracts through `just fetch-reference` and quote exact snippets from the cache. I did not have them verbatim.
- Check the ClinGen gene-disease validity record for the CGGV citation, and check whether the MONDO term is the correct one for SCAR17.
- The zebrafish phenotype and the paralog paper (PMID:41422678) need full-text review before use.

**Sources:**
- https://malacards.org/card/spinocerebellar_ataxia_autosomal_recessive_17
- https://thegencc.org/submissions/SGC-106813.2
- https://panelapp.genomicsengland.co.uk/panels/285/gene/CWF19L1/
- PubMed via NCBI E-utilities, for PMIDs 25361784, 26197978, 27016154, 25671812, 32508030, 33012273, 36357319, 36453471, 36530930, 37752213, 38681507, 39542248, 41422678, 23477746, 24785259 and 34558842.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:41422678` (2 mentions) - NVL2-interacting protein CWF19L2 is required for debranching of intron-derived lariat RNAs.
  - shared terms: cwf19l1

Weighed against this report's own most characteristic terms: `found`, `ataxia`, `abstract`, `atrophy`, `scar17`, `cwf19l1`, `variant`, `recessive`, `cerebellar`, `family`, `gene`, `disability`, `intellectual`, `compound`, `malacard`, `patient`, `zebrafish`, `loss-of-function`, `heterozygous`, `phenotype`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

1 of 3 terms resolved to a current term; the rest could not be looked up either way.