---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T04:14:01.067542'
end_time: '2026-10-30T04:16:45.669996'
duration_seconds: 164.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: RBBP7-Related X-linked Spermatogenic Maturation Arrest
  mondo_id: MONDO:0976123
  category: Mendelian
  causal_genes: RBBP7
  omim_id: OMIM:301137
  synonyms: SPGFX9; RBBP7-related maturation arrest
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
  web_search_requests: 3
  num_turns: 15
  total_cost_usd: 2.2790500000000007
  session_id: a41e7e10-190f-589a-8c9a-afe465c19827
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.4.0
term_validation:
  total_terms: 31
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 9
  labels_variant: 6
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RBBP7-Related X-linked Spermatogenic Maturation Arrest
- **MONDO ID:** MONDO:0976123 (if available)
- **Causal gene(s):** RBBP7
- **OMIM:** OMIM:301137
- **Synonyms:** SPGFX9; RBBP7-related maturation arrest
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **RBBP7-Related X-linked Spermatogenic Maturation Arrest** covering all of the
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

I'm checking the two cached primary papers and searching for any RBBP7 literature published since 2023.

# Research Report: RBBP7-Related X-linked Spermatogenic Maturation Arrest (SPGFX9)

**Gene:** RBBP7 (hgnc:9890, Xp22.2, gene MIM 300825) · **MONDO:** MONDO:0976123 · **OMIM:** 301137
**Report date:** 2026-10-30

> **Repository note:** dismech already has an entry for this disease, `kb/disorders/Spermatogenic_Failure_X-linked_9.yaml` (798 lines, created 2026-10-30). Both primary papers are cached in `references_cache/` as PMC full text: PMID:37843278 and PMID:35809576. Every quote below was copied from those cache files unless it is marked otherwise. PMIDs marked **[verify]** are not cached; run `just fetch-reference` on them before any curation use.

---

## 1. Disease Information

**Overview.** SPGFX9 is a monogenic form of male infertility caused by hemizygous loss-of-function variants in the X-linked gene **RBBP7** (retinoblastoma-binding protein 7, also called RbAp46). It presents as non-obstructive azoospermia (NOA). On histology it is *early* maturation arrest: Sertoli cells are present, spermatogonia are few, and there are no spermatocytes or sperm. In the founding family the proband also had a benign Leydig cell tumor.

- Li et al. 2023 (PMID:37843278, *J Clin Invest*): *"we identified a deleterious hemizygous variant of X-linked retinoblastoma-binding protein 7 (RBBP7) as a potential key cause of MA, which was also found to be associated with the development of Leydig cell tumors."*
- Riera-Escamilla et al. 2022 (PMID:35809576, *Am J Hum Genet*): *"The most frequently affected prioritized gene, RBBP7, was found mutated in ten men across all cohorts, and our functional studies in Drosophila support its role in germ stem cell maintenance."*

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0976123 (*spermatogenic failure, X-linked, 9*) |
| OMIM | 301137 (phenotype); 300825 (RBBP7 gene) |
| DOID | DOID:0061177 ([Disease Ontology](https://disease-ontology.org/term/DOID:0061177/owl)) |
| Orphanet | No disorder-specific ORPHA code found. It falls under the general NOA/male infertility groupings. |
| ICD-10 / ICD-11 | No specific code. Nearest: N46.01 (azoospermia, organic) / GB04.0 (male infertility due to azoospermia). |
| MeSH | Azoospermia (D053713); Infertility, Male (D007248) |

**Synonyms:** spermatogenic failure, X-linked, 9; SPGFX9; RBBP7-related maturation arrest; X-linked RBBP7 maturation arrest.

**Data provenance:** all of the evidence comes from individual patients: one family, plus 10 men from aggregated sequencing cohorts. No registry or EHR-derived data exist.

---

## 2. Etiology

- **Cause:** germline, hemizygous, X-linked loss-of-function variants in RBBP7.
- **Genetic risk factors:**
  - **Family variant:** c.1200dupA, p.W401Mfs*5 (NM_002893.4; the paper also writes it as c.1201ins1, p.W401Mfs*4). It was found in two brothers.
  - **Cohort variants:** 10 men in a 2,354-man X-chromosome exome screen carried RBBP7 variants, three of them loss-of-function. Burden versus gnomAD gave an adjusted p = 5.07E−6 (PMID:35809576).
- **Environmental risk factors:** none described. The founding family had no mumps orchitis, trauma, toxins, radiation, STIs, anabolic steroids or chemotherapy (PMID:37843278).
- **Protective factors and gene–environment interactions:** none reported.
- **Possible modifiers (speculative):** Riera-Escamilla et al. suggest RBBP7 forms a CRL4B^RBBP7 complex with CUL4B, which degrades HUWE1. They note that both CUL4B and HUWE1 carried variants in infertile men. This is a hypothesis about a possible pathway interaction, not an established modifier effect: *"we speculate that RBBP7, CUL4B, or HUWE1 may lead to both spermatogenic failure and cancer predisposition."*

---

## 3. Phenotypes

| Phenotype | Suggested HPO | Type | Onset | Frequency / evidence |
|---|---|---|---|---|
| Male infertility | HP:0003251 *Male infertility* | Clinical sign | Recognized in adulthood (2–3 years of failure to conceive) | 2/2 brothers; 10/10 cohort carriers |
| Non-obstructive azoospermia | HP:0011961 *Non-obstructive azoospermia* | Laboratory / clinical | Adult presentation; congenital in nature | 2/2 (family); cohort = NOA/cryptozoospermia |
| Early maturation arrest (spermatogonial/meiotic) | No precise HPO term. Consider HP:0011961 plus a free-text descriptor; check HPO for a "spermatogenic maturation arrest" term. | Histopathology | — | 2/2 brothers (mTESE histology) |
| Decreased testicular size | HP:0008734 *Decreased testicular size* | Physical sign | Adult | 2/2 (3.6 mL and 4.5 mL) |
| Elevated FSH | HP:0008232 *Elevated circulating follicle stimulating hormone level* | Laboratory | Adult | 2/2 (45.5 and 18.76 IU/L) |
| Leydig cell tumor (benign) | HP:0100618 *Leydig cell neoplasia* | Neoplasm | Adult (27 y) | 1/2 (proband only) |
| Variable LH and testosterone | (HP:0040085 *Abnormal circulating testosterone* — **[verify]**) | Laboratory | Adult | Discordant between the brothers |
| Failed sperm retrieval at mTESE | — | Procedure outcome | — | 2/2 |

Supporting quotes (PMID:37843278):
- *"Sertoli cells were obvious, but with only a few spermatogonia and no spermatocytes or sperm present in patient samples"*
- *"the levels of FSH were higher than normal, with 45.5 IU/L in the proband (II:1) and 18.76 IU/L in his brother (II:2)"*
- *"the patients' mean testicle size was abnormally small, with 3.6 mL in the proband (II:1) and 4.5 mL in his brother (II:2)"*
- *"these results indicate that this neoplasm is a benign Leydig cell tumor (LCT)."*

**Severity and course:** spermatogenic failure is complete in the reported patients, and the condition appears stable rather than progressive. The disease is non-syndromic: general health was normal and erectile and ejaculatory function were preserved.

**Quality of life:** no disease-specific data. The general NOA literature describes the psychosocial burden of infertility. The Leydig cell tumor needed surgery (testis-sparing enucleation).

---

## 4. Genetic / Molecular Information

**Causal gene:** RBBP7, hgnc:9890, Xp22.2. It encodes a 425-aa WD40-repeat histone chaperone, a 7-bladed β-propeller with an N-terminal α-helix and a short C-terminal α-helix. It is a core subunit of CAF-1, NuRD, Sin3-HDAC and PRC2-type chromatin complexes, and is ubiquitously expressed.

**Variants**

| Variant | Type | Origin | Classification | Population frequency | Source |
|---|---|---|---|---|---|
| NM_002893.4: c.1200dupA, p.(Trp401Metfs*5) | Frameshift (1-bp insertion in the last 2 exons, sixth/last WD40 blade) | Germline; maternally inherited (heterozygous mother) | Predicted pathogenic (FATHMM-indel, CRAVAT, SIFT_indels2). No ClinVar classification was found. | Absent from 1000G, ESP6500, ExAC and gnomAD; absent from 103 further Chinese NOA men | PMID:37843278 |
| 10 rare variants in 10 men (3 LoF, others missense) | LoF + missense | Germline, hemizygous | Prioritized as a "strong candidate" (score ≥5) | Not in gnomAD | PMID:35809576 (variant details are in its Fig. 2 / Table S4) |

Supporting quotes:
- *"An identical hemizygous variant (NM_002893.4, c.1201ins1, p.W401M fs*4) was identified in the 2 brothers, occurring on chromosome Xp22.2 and affecting the last 2 exons of RBBP7."* (PMID:37843278)
- *"RBBP7 is the most frequently mutated gene in our four cohorts: nine NOA-affected men carry variants not reported in gnomAD, three of them LoF."* (PMID:35809576)
- *"the burden test showed that pathogenic variants in RBBP7 were significantly more common in infertile men than in gnomAD control individuals (adjusted p value = 5.07E−6)"* (PMID:35809576)

**Functional consequence:** loss of function. The truncated protein loses its C-terminal hydrophilic α-helix (in silico modelling: 23 hydrogen bonds fall to 8). Modelling also predicts weaker binding to histone H4 Arg35 and to the BRCA1 BRCT domain, and RBBP7 protein is reduced in patient testis. In the fly rescue experiment, the mutant human RBBP7 failed to rescue while the wild-type protein did. That points to a null or hypomorphic allele, not a dominant-negative one.

**Gene-disease validity:** no ClinGen or GenCC classification was found. The evidence is research-level: one family plus a cohort burden test.

**Modifier genes, epigenetics, chromosomal abnormalities:**
- No modifier genes have been established.
- RBBP7 is itself an epigenetic regulator (it chaperones histones and is part of HDAC complexes), but no patient methylome or histone-mark data exist.
- Patients had normal karyotypes and no AZF microdeletions, which is a prerequisite for this diagnosis.

---

## 5. Environmental Information

Not applicable. There are no known environmental, lifestyle or infectious contributors. In the founding family, the documented absence of acquired causes (varicocele, torsion, orchitis, gonadotoxins) is part of the diagnostic work-up.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Hemizygous germline RBBP7 LoF variant**, e.g. p.W401Mfs*5 in the sixth WD40 blade. There is no second X allele to compensate. *(Demonstrated genetically.)*
2. **→ results in** a truncated protein that has lost its C-terminal α-helix and has **reduced testicular RBBP7 protein**. *(The protein reduction was shown by immunostaining and western blot of patient tissue; the structural effect is in silico.)*
3. **→ leads to** **impaired binding of RBBP7 to histone H4** and to the **BRCA1 BRCT domain**. *(Binding to both was predicted by modelling. In patient tubules, weak RBBP7 signal with loosely distributed H4 was observed; the BRCA1 effect was inferred from docking energies of −9.5 vs −10.9 kcal/mol.)*
4. **→ results in** **reduced BRCA1 and defective double-strand-break repair**, with increased γH2AX in the seminiferous tubules. *(Observed in the proband only. The causal direction from step 3 is inferred. A proposed alternative route runs through CRL4B^RBBP7 → HUWE1 → BRCA1 degradation; this is speculative.)*
5. **→ leads to** **G2/M cell-cycle arrest and apoptosis of spermatogonia and spermatocytes**. *(Shown in mouse GC-1 and GC-2 cell lines after siRNA knockdown, in vitro.)*
   - **Parallel branch 5′:** **loss of germline stem cell maintenance**. In Drosophila, knocking down the ortholog Caf1-55 in germ cells (nos-GAL4) removed all GSCs and germ cells (model organism).
6. **→ results in** **germ cell depletion with early (spermatogonial/meiotic) maturation arrest**: few spermatogonia, no spermatocytes or spermatids. *(Human histology.)*
7. **→ leads to** **non-obstructive azoospermia, small testes and raised FSH** (loss of inhibin-B feedback is inferred), and therefore **male infertility**.
   - **Branch B (somatic):** RBBP7 loss in **somatic testicular cells**, together with a DSB-repair defect, may lead to **somatic hyperproliferation and a Leydig cell tumor**. *(The human evidence is one tumor with hardly detectable RBBP7 and low BRCA1. In Drosophila, cyst-cell knockdown with tj-GAL4 caused tumor-like cyst-cell accumulation. The causal link is hypothesized.)*

Key quotes (PMID:37843278):
- *"This mutation resulted in premature protein translation termination, affecting the sixth WD40 domain of the RBBP7 and the interaction of the mutated RBBP7 with histone H4. Decreased BRCA1 and increased γH2AX were observed in the proband. In mouse spermatogonial and pachytene spermatocyte-derived cells, deprivation of rbbp7 led to cell cycle arrest and apoptosis."*
- *"knockdown of RBBP7/Caf1-55 in germ cells resulted in complete absence of germ cells and reduced testis size, whereas knockdown of RBBP7/Caf1-55 in cyst cells resulted in hyperproliferative testicular cells."*

Quote from PMID:35809576:
- *"We observed a complete lack of dBigH1- and Vasa-expressing cells at the tip of nos > Caf1-p55RNAi testes, revealing that RBBP7/Caf1-p55 is necessary for GSCs maintenance"*

### Checklist detail

- **Pathways:** chromatin assembly (CAF-1 / histone H3-H4 deposition); HDAC complexes (NuRD, Sin3); PRC2; the BRCA1 DSB-repair / homologous recombination pathway; the CRL4B ubiquitin ligase and HUWE1 axis (hypothesized).
- **Cellular processes:** germline stem cell maintenance; mitotic G2/M transition; apoptosis; meiotic entry/progression (inferred). Mouse oocyte knockdown evidence also links Rbbp7 to histone deacetylation and to chromosome segregation during meiosis: Balboula et al., *Cell Cycle* 2014, PMID:24317350 **[verify]**.
- **Protein dysfunction:** C-terminal truncation of the WD40 β-propeller, giving loss of function.
- **Metabolic and immune involvement:** none reported.
- **Molecular profiling:** human testis scRNA-seq shows RBBP7 is highest in spermatogonia and spermatocytes and lower in spermatids. The protein is also present in Sertoli and Leydig cells (PMID:37843278). No disease-specific transcriptomic, proteomic or GEO datasets were found.

**Suggested GO terms** (the first four are already bound and validated in the KB entry):

| Term | Label |
|---|---|
| GO:0042393 | histone binding (DECREASED) |
| GO:0006302 | double-strand break repair |
| GO:0000086 | G2/M transition of mitotic cell cycle |
| GO:0006915 | apoptotic process |
| GO:0036098 | male germ-line stem cell population maintenance **[verify]** |
| GO:0007283 | spermatogenesis **[verify]** |
| GO:0006335 | DNA replication-dependent chromatin assembly **[verify]** |

**Suggested CL terms:**

| Term | Label |
|---|---|
| CL:0000020 | spermatogonium |
| CL:0000656 | primary spermatocyte |
| CL:0000216 | Sertoli cell |
| CL:0000178 | Leydig cell |
| CL:0000014 | germ line stem cell **[verify]** |

---

## 7. Anatomical Structures Affected

- **Organ:** testis (UBERON:0000473 **[verify]**). The disease is restricted to the male reproductive system, with no reported extragonadal involvement.
- **Tissue:** seminiferous tubule epithelium (UBERON:0001343 seminiferous tubule of testis **[verify]**); the testicular interstitium is the site of the Leydig cell tumor.
- **Cells:** spermatogonia (depleted), spermatocytes (absent), Sertoli cells (preserved), Leydig cells (tumor in the proband).
- **Subcellular:** nucleus / chromatin (GO:0005634 nucleus; GO:0000785 chromatin **[verify]**).
- **Lateralization:** testicular hypotrophy was bilateral; the Leydig tumor was unilateral (right upper pole, 0.6 × 0.5 cm).

---

## 8. Temporal Development

- **Onset:** the defect is presumed congenital or prepubertal (a germ-cell maintenance failure), but it is clinically recognized in adulthood (ages 26–27) through infertility.
- **Course:** stable and lifelong. There is no evidence of progression; post-pubertal germ-cell loss is plausible but unproven.
- **Remission:** none is expected.
- **Critical periods:** fertility preservation before germ-cell depletion is theoretical only, since the timing of germ-cell loss in humans is unknown. The Leydig tumor did not recur after one year of follow-up.

---

## 9. Inheritance and Population

- **Inheritance:** X-linked recessive (HP:0001419). Affected males are hemizygous and the carrier mother is unaffected: *"Their mother (I:2) had a heterozygous mutation with a double peak"* (PMID:37843278). Because affected men are infertile, transmission runs through carrier females.
- **Penetrance:** apparently complete in hemizygous males among reported cases (12/12), but ascertainment was through infertility. No unaffected hemizygous males have been reported.
- **Expressivity:** variable for the Leydig tumor (1/2 brothers) and for hormone profiles. Spermatogenic failure was consistent.
- **Anticipation, mosaicism, founder effects:** none reported.
- **Frequency:** RBBP7 variants were found in 10/2,354 men with idiopathic azoospermia or cryptozoospermia, about 0.42%. Li et al. noted this figure explicitly: *"Riera-Escamilla et al. identified RBBP7 mutations in 10 out of 2,354 men (0.42%)."* The family variant was absent from 103 Chinese NOA men.
- **Population prevalence:** not established; this is ultra-rare. Prevalence class: NOT_YET_DOCUMENTED, or CASES_IN_LITERATURE with about 12 cases.
- **Demographics:** males only. Cases come from a Chinese family and from European, US and Australian cohorts (the Barcelona, MERGE/Münster and GEMINI cohorts).

---

## 10. Diagnostics

- **Semen analysis:** azoospermia on repeated centrifuged samples.
- **Hormones:** raised FSH; variable LH and testosterone. Tumor markers (LDH, AFP, hCG) were normal in the proband.
- **Imaging:** scrotal ultrasound shows small testes and may show a hypoechoic, vascularized lesion (Leydig tumor). CT was used for staging.
- **Histology (mTESE or biopsy):** early maturation arrest. Immunohistochemistry: WT1 marks Sertoli cells; the tumor was inhibin+++, vimentin+, calretinin+, WT1−, with Ki67 <5%.
- **Genetic work-up:** first karyotype and Y-chromosome AZF microdeletion testing, both normal by definition here. Then whole-exome sequencing or an NOA gene panel that includes RBBP7. Sanger segregation testing (carrier mother) confirms the result. Li et al. suggest *"a panel of RBBP7 combined with other azoospermia-associated gene variants."* NCIT: C15709 *Genetic Testing* (in the entry).
- **Differential diagnosis:**
  - other X-linked NOA genes: TEX11, AR, USP26, GCNA, HUWE1, CUL4B, FANCB;
  - autosomal meiotic-arrest genes, e.g. SYCP3, TEX14, MEIOB;
  - Klinefelter syndrome (excluded by karyotype);
  - AZFa/b/c deletions;
  - acquired NOA (orchitis, chemotherapy, cryptorchidism);
  - Leydig cell hyperplasia (diffuse) as opposed to Leydig cell tumor (a solitary, well-defined nodule).
- **Screening:** none established. After an index case, cascade carrier testing of female relatives is reasonable.

---

## 11. Outcome / Prognosis

- **Survival:** normal life expectancy is expected; the disease is non-syndromic.
- **Fertility:** in both reported mTESEs, sperm retrieval failed (*"No mature spermatozoa were retrieved"*). The prognosis for biological paternity is therefore poor.
- **Complications:** Leydig cell tumor (benign; surgical enucleation; no recurrence at one year). After the tumor was removed, the proband's testosterone fell, and long-term hypogonadism is possible. Both Li and Riera-Escamilla raise a possible wider cancer predisposition through BRCA1 / DNA-repair biology; this is unproven.
- **Prognostic markers:** the early-arrest histology and genotype predict a poor mTESE outcome (inferred from two cases).

---

## 12. Treatment

No disease-specific therapy exists. Management:

| Intervention | NCIT suggestion | Notes |
|---|---|---|
| Microdissection TESE ± ICSI | NCIT:C15329 *Surgical Procedure* (bind and verify any more specific term) | Failed in both reported cases |
| Testis-sparing tumor enucleation | NCIT:C15329 *Surgical Procedure* | Used for the Leydig cell tumor |
| Genetic counseling | NCIT:C15240 *Genetic Counseling* | X-linked recessive; carrier mother |
| Testosterone replacement for hypogonadism | NCIT:C15986 *Pharmacotherapy* + CHEBI:17347 testosterone **[verify]** | Only if symptomatic hypogonadism; suppresses spermatogenesis |
| Donor sperm / adoption | — | Family-building alternatives |

- **Pharmacogenomics, gene therapy, cell therapy, RNA therapies:** none.
- **Clinical trials:** no RBBP7-specific trials were found.
- **Other:** hormonal stimulation (FSH, hCG, clomiphene) has no evidence base in this genotype.

---

## 13. Prevention

- **Primary prevention:** none.
- **Genetic counseling for carrier females:** each son has a 50% risk of being affected. Options include preimplantation genetic testing or prenatal diagnosis once the familial variant is known.
- **Cascade testing:** testing female relatives clarifies carrier status. Testing brothers of an index case allows early counseling and sperm-banking discussion, although sperm is unlikely to be present.
- **Tertiary prevention:** ultrasound surveillance for testicular tumors is suggested by the authors (*"special attention should be paid toward screening for possible RBBP7 mutation–related testicular tumors"*). This is expert opinion and has not been validated.

---

## 14. Other Species / Natural Disease

- No naturally occurring RBBP7-associated infertility has been reported in animals (no OMIA entry found).
- **Orthologs:** mouse *Rbbp7* (X-linked; 99% similarity to human), zebrafish *rbbp7*, Drosophila *Caf1-55* (96% similarity per Li et al.; 94% per Riera-Escamilla et al.). This is a highly conserved WD40 histone chaperone.
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Manipulation | Recapitulation | Limitations | Source |
|---|---|---|---|---|
| *D. melanogaster* (NCBITaxon:7227), germline knockdown nos>Caf1-55 RNAi | Germline RNAi | Testes very underdeveloped in 94% (n=36), about 74% smaller testes, loss of GSCs and Vasa+ germ cells, sterility. Recapitulates germ-cell depletion well. | Invertebrate testis architecture; Drosophila has no Leydig cells | PMID:35809576; PMID:37843278 |
| *D. melanogaster*, cyst-cell knockdown tj>Caf1-55 RNAi | Somatic RNAi | Cyst-cell (Sertoli analog) hyperproliferation, germ-cell overproliferation and accumulation of undifferentiated cells, reduced fertility. Partially models somatic tumorigenesis. | Cyst cells ≠ Leydig cells | PMID:37843278 |
| Drosophila Caf1-55 null | Null mutant | Small larval testis, γH2Av (DSB) elevation, tumor-like cyst cells | Lethal at L2 | PMID:37843278 |
| Drosophila rescue | Human WT vs mutant RBBP7 transgene | WT human RBBP7 rescues fertility; p.W401Mfs mutant does not | Supports pathogenicity of the specific allele | PMID:37843278 |
| Mouse GC-1 (spermatogonia) / GC-2 (spermatocyte) lines | siRNA knockdown | ↓ proliferation, ↑ apoptosis, G2/M arrest (S phase 43.9→31.2% in GC-1) | Immortalized lines; in vitro | PMID:37843278 |
| Mouse oocytes | siRNA/morpholino | Chromosome misalignment, spindle assembly checkpoint (SAC) failure, HDAC defects in female meiosis | Female germline only | PMID:24317350 **[verify]** |
| Mouse Rbbp7 conditional knockout | — | **No published male germline knockout phenotype was found.** A floxed line is commercially available ([Cyagen S-CKO-08695](https://www.cyagen.com/mouseatlas/S-CKO-08695)). | Knowledge gap | — |

**Main knowledge gap:** no mammalian in vivo model exists. A germ-cell-specific Rbbp7 knockout (Stra8-Cre or Ddx4-Cre) would test the mechanism, and a Leydig-specific deletion would test the tumor link. These are good candidates for a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion in the KB entry.

---

## Evidence Summary and Caveats

1. **The evidence base is thin.** It consists of one family (two brothers) and one cohort study (10 carriers plus a burden test). Nothing new on RBBP7 and male infertility turned up in searches for 2024–2026 work.
2. **The Leydig cell tumor association rests on a single patient.** Treat it as a hypothesis, not an established phenotype frequency.
3. **The BRCA1 and histone H4 mechanism** is supported by in silico modelling and immunostaining of one proband. It has not been shown biochemically with the mutant protein.
4. **No ClinGen classification exists.** `gene_disease_validity` should stay absent.
5. **The variant nomenclature is inconsistent within the source:** the paper uses both c.1200dupA p.W401Mfs*5 and c.1201ins1 p.W401Mfs*4. The HGVS-correct form appears to be c.1200dupA p.(Trp401Metfs*5).

## Sources

**Primary (cached in `references_cache/`):**
- Li J et al. *X-linked RBBP7 mutation causes maturation arrest and testicular tumors.* J Clin Invest 2023. PMID:37843278. doi:10.1172/JCI171541. [PMC10575721](https://pmc.ncbi.nlm.nih.gov/articles/PMC10575721/)
- Riera-Escamilla A et al. *Large-scale analyses of the X chromosome in 2,354 infertile men discover recurrently affected genes associated with spermatogenic failure.* Am J Hum Genet 2022. PMID:35809576. doi:10.1016/j.ajhg.2022.06.007

**Not cached; verify before use:**
- Balboula AZ et al. Mouse oocyte Rbbp7 knockdown, Cell Cycle 2014. PMID:24317350 ([Taylor & Francis](https://informahealthcare.com/doi/full/10.4161/cc.27410))

**Web resources consulted:**
- [MalaCards: SPGFX9](https://www.malacards.org/card/spermatogenic_failure_x_linked_9)
- [Disease Ontology DOID:0061177](https://disease-ontology.org/term/DOID:0061177/owl)
- [GeneCards: RBBP7](https://www.genecards.org/card/RBBP7)
- [LabMedica: X chromosome genes linked to male infertility](https://mobile.labmedica.com/molecular-diagnostics/articles/294793812/x-chromosome-genes-linked-to-male-infertility.html)
- [Münster CRIS record for PMID:35809576](https://cris-portal.uni-muenster.de/portal/en/publication/170112721)
- [MGI expression assay MGI:7266366](https://www.informatics.jax.org/assay/MGI:7266366)
- [Cyagen Rbbp7 cKO line](https://www.cyagen.com/mouseatlas/S-CKO-08695)
- [PMC8411525 (BRD7, a different gene; excluded as a name confusion)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8411525/)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 6 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0042393` (1 mention) - the report calls it "histone binding (DECREASED)"; GO calls it **histone binding**
- `GO:0036098` (1 mention) - the report calls it "male germ-line stem cell population maintenance **[verify]"; GO calls it **male germ-line stem cell population maintenance**
- `GO:0007283` (1 mention) - the report calls it "spermatogenesis **[verify]"; GO calls it **spermatogenesis**
- `GO:0006335` (1 mention) - the report calls it "DNA replication-dependent chromatin assembly **[verify]"; GO calls it **DNA replication-dependent chromatin assembly**
- `CL:0000014` (1 mention) - the report calls it "germ line stem cell **[verify]"; CL calls it **germ line stem cell**
- `NCBITaxon:7227` (1 mention) - the report calls it "D. melanogaster"; NCBITaxon calls it **Drosophila melanogaster**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

30 of 31 terms resolved to a current term; the rest could not be looked up either way.