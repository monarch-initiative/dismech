---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-26T20:23:11.442356'
end_time: '2026-10-26T20:24:17.551104'
duration_seconds: 66.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Bilateral Parasagittal Parieto-occipital Polymicrogyria
  mondo_id: MONDO:0012986
  category: Mendelian
  causal_genes: FIG4
  omim_id: OMIM:612691
  synonyms: bilateral temporo-occipital polymicrogyria; FIG4-related polymicrogyria
    with seizures; polymicrogyria with seizures
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
  web_search_requests: 2
  num_turns: 4
  total_cost_usd: 0.7982825999999998
  session_id: 402da01d-554f-59a0-9730-4f6c8133551c
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 1
  validator_version: 0.4.0
term_validation:
  total_terms: 5
  verified: 5
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bilateral Parasagittal Parieto-occipital Polymicrogyria
- **MONDO ID:** MONDO:0012986 (if available)
- **Causal gene(s):** FIG4
- **OMIM:** OMIM:612691
- **Synonyms:** bilateral temporo-occipital polymicrogyria; FIG4-related polymicrogyria with seizures; polymicrogyria with seizures
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Bilateral Parasagittal Parieto-occipital Polymicrogyria** covering all of the
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

# Bilateral Parasagittal Parieto-occipital Polymicrogyria (BPPP; MONDO:0012986; OMIM 612691): causal gene FIG4

**Scope and provenance.** I ran only a limited web search this session: two standard searches that returned snippets and curation summaries. I did not open any primary paper in full text. Each claim below is labelled by source class.

- **Retrieved:** statements traced to a search result, with the URL given.
- **Background knowledge:** statements from my own recall. Treat these as unverified leads until checked against the primary source.
- **No PMIDs are asserted.** None was retrieved, and I will not write one from memory. The only paper identifier I have is the Baulac 2014 DOI.

The causal gene is **FIG4**, which encodes the phosphoinositide 5-phosphatase that converts PI(3,5)P2 to PI3P. Disease class: autosomal recessive Mendelian malformation of cortical development (a pediatric-onset cortical polymicrogyria with epilepsy).

## 1. Disease information

- **Naming discrepancy.** The target name ("parasagittal parieto-occipital") differs from the synonym list ("bilateral temporo-occipital polymicrogyria").
  - MalaCards titles the entry "Polymicrogyria, Bilateral Temporooccipital (BTOP)" ([MalaCards](https://malacards.org/card/polymicrogyria_bilateral_temporooccipital)).
  - A search-result summary of the OMIM entry (612691) describes "bilateral malformation of cortical development, centered around the parasagittal and mesial aspects of the parietooccipital cortex" (as relayed in the search results; the OMIM page itself was not opened).
  - Lump/split call for you: these appear to be one OMIM/MONDO concept with two descriptive spellings. I did not verify the MONDO label.
- **Overview (retrieved).**
  - Baulac et al. studied a consanguineous Moroccan family with temporo-occipital polymicrogyria, epilepsy and psychiatric features, previously mapped to 6q16-q22. They used exome sequencing and found a homozygous FIG4 missense variant in each affected sibling and absent in three unaffected siblings ([WUSTL profile of Baulac 2014, Neurology 82(12):1068-75, doi:10.1212/WNL.0000000000000241](https://profiles.wustl.edu/en/publications/role-of-the-phosphoinositide-phosphatase-fig4-gene-in-familial-ep/)).
  - The earlier clinical and mapping report is Ben Cheikh et al. 2009. It described autosomal recessive bilateral occipital polymicrogyria in a large consanguineous Moroccan family (as relayed in the search summary; I did not verify its details).
- **Other identifiers.** Orphanet, ICD-10/11 and MeSH identifiers were not retrieved; I give none.
- **Data origin.** The data are family-level, from published pedigrees. They are neither EHR-derived nor aggregated registry data.

## 2. Etiology

- **Causal factors.** Biallelic FIG4 variants: a homozygous missense variant in the index family. The ClinGen/GenCC-style evidence tier is only moderate.
  - The Genomics England PanelApp entry ([PanelApp, Malformations of cortical development](https://panelapp.genomicsengland.co.uk/panels/96/gene/FIG4/)) and a GenCC submission ([GenCC SGC-178381.1](https://thegencc.org/submissions/SGC-178381.1)) were returned.
  - A reviewer comment in the search results said only one family with one supporting mouse model is described.
  - I did not open these pages, so the exact classification wording is unverified.
  - **Do not record a ClinGen tier on this entry** unless a CGGV record is found. A GenCC "Moderate" is not a ClinGen assertion, and the KB rule is to copy tiers, never assign them.
- **Variant identity.** A search result reports the variant as D783V (p.Asp783Val) (via a secondary summary). Verify this against the primary paper before binding it.
- **Risk, protective and gene-environment factors.** None are reported. Consanguinity is the relevant population factor: the single family is consanguineous. No environmental exposure has been implicated; I found no supporting literature.

## 3. Phenotypes

Everything below is from the index family and is based on search-result summaries (retrieved); frequencies and onset ages were not retrieved.

| Phenotype | Suggested HP term (verify by lookup before binding) | Support |
|---|---|---|
| Polymicrogyria, bilateral, posterior (parieto-occipital / temporo-occipital) | HP:0002126 (Polymicrogyria) is my recollection; verify | Core feature |
| Epilepsy, including focal seizures with bilateral tonic-clonic evolution and status epilepticus | HPO annotations in the search results cite HP:0002133 (Status epilepticus) and HP:0007334 (Bilateral tonic-clonic seizure with focal onset) | [Glyco​smos DOID entry](https://glycosmos.org/diseases/DOID:0080923) |
| Psychiatric features | No term retrieved | Baulac abstract summary |

- **Not retrieved:** onset age, progression, severity range, cognitive and motor outcomes, and quality of life.
- The Ben Cheikh 2009 description would be the place to check onset in the pediatric context. This is a lead, not a statement.

## 4. Genetic and molecular information

- **Gene.** FIG4 (HGNC symbol; use the lowercase `hgnc:` CURIE after a lookup, since I did not retrieve the number). It lies at 6q21, inside the originally mapped 6q16-q22 interval.
- **Variant.** One homozygous missense variant is reported. Its functional class is unestablished.
  - The Baulac abstract summary says a rescue assay in Fig4-null mouse fibroblasts was performed.
  - The direction of its result was not retrieved, so I do not state it.
- **Allelic disorders (background knowledge, unverified here).** FIG4 loss of function is also linked to Charcot-Marie-Tooth type 4J (CMT4J), and a search result confirms this link ([secondary summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC5005439)). Further links I recall are Yunis-Varón syndrome (severe biallelic loss), ALS11 and a cerebral hypomyelination phenotype from biallelic variants. The hypomyelination paper appeared in a search result titled "Cerebral hypomyelination associated with biallelic variants of FIG4" ([Deep Blue](https://deepblue.lib.umich.edu/handle/2027.42/149294?show=full)).
  - The FIG4 allelic series is a lump/split decision: separate germline entries per phenotype, not one "FIG4 disease."
- **Modifier genes, epigenetics and chromosomal abnormalities:** none reported.

## 5. Environmental information

None. Neither toxins, infection nor lifestyle factors are reported. I found no data.

## 6. Mechanism / pathophysiology

Ordered causal chain. Steps 1 to 3 are established biochemistry in general; step 4 is demonstrated in mouse only; steps 5 to 7 are inferred for this disorder.

1. **Biallelic FIG4 missense variant (D783V in the index family)** leads to reduced Fig4 phosphatase function. The extent is not shown for this variant; this is inferred.
2. **Reduced Fig4 activity** disturbs PI(3,5)P2 turnover. In the Vac14/Fab1/Fig4 complex, Fig4 is part of the machinery for acute interconversion of PI3P and PI(3,5)P2 ([VAC14 complex paper, Deep Blue](https://deepblue.lib.umich.edu/handle/2027.42/102059?show=full)). The direction of the net PI(3,5)P2 change in humans is not established.
3. **Dysregulated endolysosomal PI(3,5)P2 signalling** leads to endolysosomal enlargement and vacuolization. In Fig4-null mice, PI(3,5)P2 is reduced and enlarged LAMP2-positive vesicles accumulate ([pale tremor mouse paper summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC4059992)). One review proposes osmotic swelling from impaired activation of lysosomal cation channels; this is a proposal, not settled.
4. **In mouse,** the vacuolization is largely neuronal. Neuron-specific Fig4 transgene expression rescues the lethal wasting phenotype, and neuron-specific knockout reproduces it (from the same search summaries).
5. **Link from endolysosomal dysfunction to polymicrogyria is inferred, not demonstrated.** The mechanism between lysosomal and vesicle-trafficking dysfunction and cortical lamination or sulcation defects is unknown. Baulac reported Fig4-null mouse brain changes described as "reminiscent of human cortical malformations", and these were not shown to be polymicrogyria itself.
6. **Why the posterior regional pattern?** Unknown. This is a genuine knowledge gap.
7. **Epilepsy** is presumed secondary to the dysplastic cortex. The mechanism is not demonstrated.

Suggested ontology anchors, to be looked up and not taken from this list:
- GO: phosphatidylinositol-3,5-bisphosphate 5-phosphatase activity; endosome/lysosome organization.
- CL: neuron; cortical neuron.
- UBERON: parietal lobe, occipital lobe, cerebral cortex.

No transcriptomic, proteomic, single-cell or screening data were retrieved.

## 7. Anatomical structures affected

- Primary: the cerebral cortex, bilateral, centred on the parieto-occipital and mesial parasagittal region.
- Alternative description in the literature: temporo-occipital. This is the naming discrepancy flagged in section 1.
- Subcellular: the endolysosomal compartment (a GO cellular component to look up). Non-CNS involvement was not described in the retrieved sources.

## 8. Temporal development

Not retrieved. Polymicrogyria is a prenatal cortical malformation, which is background knowledge rather than an established claim for this family. Seizure onset age and the course were not found. No remission or critical-period data were retrieved.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive. Source: Ben Cheikh 2009 as relayed in the search summary; consistent with the homozygous variant in a consanguineous family.
- **Penetrance and expressivity:** not established. The affected siblings were homozygous for the variant; no data on unaffected homozygotes were retrieved.
- **Founder effect or carrier frequency:** not assessed. The family is Moroccan. I did not check gnomAD.
- **Prevalence and incidence:** not available. One reported family; Orphanet prevalence data were not retrieved. Mark prevalence as `NOT_YET_DOCUMENTED` unless Orphanet says otherwise.
- **Sex ratio and geographic distribution:** no data.

## 10. Diagnostics

- **Imaging:** MRI showing bilateral posterior polymicrogyria is the diagnostic anchor (background knowledge).
- **EEG:** reasonable for seizure characterization (background knowledge).
- **Genetic testing:** FIG4 sequencing. FIG4 is on the PanelApp "Malformations of cortical development" panel and the Australian "Polymicrogyria and Schizencephaly" panel ([PanelApp Australia](https://panelapp-aus.org/panels/18/gene/FIG4/)). The PanelApp rating wording was not read.
- **Differential diagnosis:** other posterior polymicrogyria genes and syndromes, and CMT4J and Yunis-Varón syndrome as FIG4 allelic disorders. I did not retrieve distinguishing features.
- **Screening, biomarkers, GeneReviews baseline:** I did not check for a GeneReviews chapter, so that is a gap for `just check-genereviews`.

## 11. Outcome and prognosis

Not retrieved: survival, disability, long-term seizure control and quality of life. With one family, none may exist.

## 12. Treatment

No disease-specific treatment or trial was found. Management is presumably symptomatic, with antiseizure medication, but no source was retrieved. I did not search ClinicalTrials.gov or pharmacogenomic resources.

Generic NCIT terms to look up if the entry curates symptomatic care:
- Pharmacotherapy (a generic action term used with `therapeutic_agent`).
- Supportive care.
- Genetic counseling.

## 13. Prevention

Not studied specifically. Genetic counseling for recurrence risk is the standard general measure for autosomal recessive disease. Prenatal and preimplantation testing would require a known familial variant. This is inference, not sourced.

## 14. Other species

Not retrieved: OMIA records and naturally occurring disease. I do not know of any.

## 15. Model organisms

- **Mouse, Fig4-null (pale tremor, plt).** A spontaneous retroviral insertion gives a null allele ([PMC4059992 summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC4059992)).
  - Phenotype: neurodegeneration, diluted pigmentation and lethality by about six weeks.
  - Spongiform brain degeneration with extensive neuronal vacuolization, largely confined to brain and spleen.
  - Reduced PI(3,5)P2 and enlarged LAMP2-positive vesicles in fibroblasts.
  - Neuron-specific transgene rescue, and neuron-specific knockout reproducing the phenotype.
- **Mouse, Vac14 mutants.** Vac14-null mice show neonatal lethality with CNS and PNS neurodegeneration, similar to Fig4-null mice. The ingls (L156R) mutant disrupts the Vac14-Fab1 interaction.
- **Fidelity to the human disease.** This is a `HUMAN_MODEL_MISMATCH`-type question: the null mouse shows a severe neurodegenerative phenotype. The human disease is a missense, presumably hypomorphic, cortical malformation. The mouse paper's brain findings were described as "reminiscent of human cortical malformations", but no mouse polymicrogyria is established by what I retrieved.
- **Other databases** (MGI, ZFIN, IMPC) were not queried.

## Gaps and leads for curation

1. Fetch and read Baulac 2014 (doi:10.1212/WNL.0000000000000241) and Ben Cheikh 2009. I could not retrieve PMIDs here, so use the fetch tool and confirm the variant nomenclature, the rescue assay's direction and the HP-level phenotype frequencies.
2. Check for any second family. The sources I saw all indicate a single family. Run PubMed for newer FIG4 polymicrogyria reports.
3. Look up the HP, GO, CL and UBERON terms listed above with `runoak`, and the MONDO label for MONDO:0012986. Nothing here is verified.
4. Resolve the naming discrepancy (parieto-occipital versus temporo-occipital) against the OMIM entry text.
5. Do not infer a mechanism for the polymicrogyria from the mouse neurodegeneration. Record it as a knowledge gap.

Sources:
- [Baulac et al. 2014, WUSTL profile](https://profiles.wustl.edu/en/publications/role-of-the-phosphoinositide-phosphatase-fig4-gene-in-familial-ep/)
- [GenCC submission SGC-178381.1](https://thegencc.org/submissions/SGC-178381.1)
- [PanelApp, Malformations of cortical development](https://panelapp.genomicsengland.co.uk/panels/96/gene/FIG4/)
- [PanelApp Australia, Polymicrogyria and Schizencephaly](https://panelapp-aus.org/panels/18/gene/FIG4/)
- [MalaCards BTOP](https://malacards.org/card/polymicrogyria_bilateral_temporooccipital)
- [Glycosmos DOID:0080923](https://glycosmos.org/diseases/DOID:0080923)
- [PMC4059992](https://pmc.ncbi.nlm.nih.gov/articles/PMC4059992)
- [PMC5005439](https://pmc.ncbi.nlm.nih.gov/articles/PMC5005439)
- [VAC14 complex, Deep Blue](https://deepblue.lib.umich.edu/handle/2027.42/102059?show=full)
- [FIG4 hypomyelination, Deep Blue](https://deepblue.lib.umich.edu/handle/2027.42/149294?show=full)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.