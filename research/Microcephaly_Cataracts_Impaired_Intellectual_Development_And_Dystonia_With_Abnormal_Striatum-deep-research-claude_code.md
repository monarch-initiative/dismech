---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T22:02:33.966324'
end_time: '2026-10-27T22:08:06.525088'
duration_seconds: 332.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Microcephaly, Cataracts, Impaired Intellectual Development, and Dystonia
    with Abnormal Striatum
  mondo_id: MONDO:0032656
  category: Mendelian
  causal_genes: KCNA4
  omim_id: OMIM:618284
  synonyms: MCIDDS; KCNA4-related neurodevelopmental disorder
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
  num_turns: 35
  total_cost_usd: 2.5007126
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 16
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 43
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - MGI
  - EXT_ID
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly, Cataracts, Impaired Intellectual Development, and Dystonia with Abnormal Striatum
- **MONDO ID:** MONDO:0032656 (if available)
- **Causal gene(s):** KCNA4
- **OMIM:** OMIM:618284
- **Synonyms:** MCIDDS; KCNA4-related neurodevelopmental disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Microcephaly, Cataracts, Impaired Intellectual Development, and Dystonia with Abnormal Striatum** covering all of the
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

The shell can't reach PubMed without approval, so I'm pulling the KCNA4 literature through web fetch instead.

I've got the core clinical and functional data from the 2016 paper. Next I'm checking ClinVar, GenCC and the mouse knockout literature, then I'll write the report.

I've confirmed the main ontology terms against the local cache. Now checking a few more labels (putamen and speech terms, the Kv channel GO term), then I'll write the report.

# Research Report: Microcephaly, Cataracts, Impaired Intellectual Development, and Dystonia with Abnormal Striatum (MCIDDS), caused by KCNA4

## Summary

MCIDDS (MONDO:0032656; OMIM #618284) is an ultra-rare autosomal recessive neurodevelopmental syndrome. Its causal gene is **KCNA4** (hgnc:6222), which encodes Kv1.4, a rapidly inactivating ("A-type") voltage-gated potassium channel of the Shaker family.

- **One family.** The whole evidence base for this disease is one consanguineous Saudi family with four affected siblings. They carry a homozygous missense variant, NM_002233 c.266G>A p.(Arg89Gln).
- **Two papers.** Al-Owain et al. 2013 (PMID:23181898) described the family and mapped the disease to chromosome 11. Kaya et al. 2016 (PMID:27582084) found the KCNA4 variant.
- **No second family.** I found no second family in PubMed/Europe PMC (182 hits screened), OMIM summaries, UniProt or GenCC as of October 2026.
- **Weak gene–disease validity.** All three GenCC submitters rate KCNA4–MCIDDS as **Limited**. UniProt files R89Q as of uncertain significance with "mildly decreased" K⁺ transport.
- **Different KCNA4 phenotype.** A 2025 report describes a *de novo heterozygous* loss-of-function KCNA4 variant (p.V558L) in a child with early-onset developmental and epileptic encephalopathy (PMID:40472070). That is a different, dominant phenotype and not MCIDDS.

These limits should shape the KB entry: every phenotype frequency is n = 4 from one sibship.

**How the facts were checked:**
- Abstracts and metadata were read through Europe PMC.
- Clinical details come from the Kaya 2016 full text (PMC13044907).
- GenCC, UniProt P22459 and MGI pages were read directly.
- OMIM and Orphanet blocked automated access. OMIM content is therefore reported only through secondary summaries, and no Orphanet code was confirmed.
- CURIEs marked ✔ below were checked against the repository's `cache/*/terms.csv`. Anything marked ⚠ was not and needs a lookup before binding.

---

## 1. Disease Information

**Overview.** MCIDDS is a congenital or early-childhood syndrome combining:
- growth retardation and microcephaly;
- bilateral early-onset ("congenital") cataract;
- mild intellectual disability (IQ 77–89) with ADHD;
- dystonia with pyramidal and extrapyramidal signs;
- a distinctive MRI pattern: **swollen caudate heads with thinned (atrophic) putamina**.

The neurological course was judged "very slowly progressive" (PMID:23181898).

| Identifier | Value | Status |
|---|---|---|
| MONDO | MONDO:0032656 "microcephaly, cataracts, impaired intellectual development, and dystonia with abnormal striatum" | ✔ cache |
| OMIM phenotype | #618284 | from template, UniProt, search summary |
| OMIM gene | *176266 (KCNA4) | search summary |
| Gene | KCNA4, hgnc:6222; locus 11p14.1 | ✔ stub/HGNC |
| UniProt | P22459 (KCNA4_HUMAN), 653 aa | ✔ fetched |
| Orphanet | Not confirmed (orpha.net blocked) | ⚠ |
| ICD-10/ICD-11, MeSH | No disease-specific code; falls under generic congenital cataract / basal-ganglia / ID codes | — |

**Synonyms:** MCIDDS; KCNA4-related neurodevelopmental disorder; "syndrome of abnormal striatum, congenital cataract and intellectual disability" (Kaya 2016 title); "Cataracts, Congenital, Intellectual Disability, Abnormal Striatum, and ADHD" (Arizona Hereditary Ocular Diseases database); "novel syndrome of abnormal striatum and congenital cataract" (Al-Owain 2013).

**Data provenance.** All data come from individual patients: four siblings described in two case reports. No registry, EHR or aggregate cohort data exist.

---

## 2. Etiology

**Cause.** The cause is genetic: a homozygous germline KCNA4 missense variant causing partial loss of Kv1.4 function.

**How the gene was found** (PMID:27582084):
- Linkage analysis gave a chromosome 11 interval with LOD 4.09, bounded by rs11602300 and rs7118193. The earlier 10K SNP scan had given a 45.9 Mb region with LOD 4.2353 (PMID:23181898).
- Autozygosity mapping narrowed this to a 12-gene block at chr11 29.1–31 Mb that contains KCNA4.
- Whole-exome sequencing found the variant.
- The variant segregated fully with disease and was absent from 747 ethnically matched in-house exomes and from a further cohort of 428.
- A 14-gene cataract panel (20 variants) found nothing that segregated.

Abstract quote (PMID:27582084): *"KCNA4 deficiency leads to a syndrome of abnormal striatum, congenital cataract and intellectual disability"* (title). The full text concludes: *"the mutation R89Q results in a loss of function in the Kv1.4 channel."*

**Risk factors:**
- **Genetic.** Biallelic KCNA4 variants. Parental consanguinity (first cousins) was the enabling factor in the only family.
- **Environmental.** None are known or expected.

**Protective factors:** None known.

**Modifier genes:** None reported.

**Gene–environment interactions:** None reported.

**Excluded candidates (PMID:23181898):** PAX6, B3GALTL and mtDNA were sequenced and were negative. Affymetrix SNP 6.0 showed no gross chromosomal abnormality.

---

## 3. Phenotypes

All four siblings (3 F, 1 M) come from Kaya 2016 Table 1 (PMC13044907) and Al-Owain 2013. Ages were not given in the material I could access.

| Phenotype | Freq (n=4) | Onset / course | Suggested HPO |
|---|---|---|---|
| Microcephaly | 4/4 | Early childhood | HP:0000252 Microcephaly ✔ |
| Growth retardation | 4/4 | Early childhood | HP:0001510 Growth delay ✔ |
| Early gross motor delay (mild) | 4/4 | Infancy | HP:0001270 Motor delay ✔ |
| Bilateral cataract, described as congenital but usually diagnosed in the first decade | 4/4 | Congenital or early childhood | HP:0000519 Developmental cataract ✔ (bilateral laterality as qualifier) |
| Glaucoma, left eye, with corneal opacity (eldest) | 1/4 | Secondary; childhood | HP:0000501 Glaucoma ✔; HP:0007957 Corneal opacity ✔ |
| Intellectual disability, mild (IQ 77–89, mean 83) | 4/4 | Childhood; stable or slowly progressive | HP:0001249 Intellectual disability ✔ (an IQ of 77–89 sits at the borderline-to-mild boundary, so consider the mild/borderline HPO children ⚠) |
| ADHD (moderate; severe in the youngest) | 4/4 | Childhood | HP:0007018 Attention deficit hyperactivity disorder ✔ |
| Severe language delay / dysarthria | 3/4 | Childhood | HP:0000750 Delayed speech and language development ✔; HP:0001260 Dysarthria ✔ |
| Dystonia / dystonic posturing | 4/4 | Childhood; very slowly progressive | HP:0001332 Dystonia ✔ |
| Cogwheel rigidity | reported on exam (frequency not split out) | — | HP:0002396 Cogwheel rigidity ✔ |
| Brisk reflexes, positive Babinski | reported | — | HP:0001347 Hyperreflexia ✔; HP:0003487 Babinski sign ✔ |
| Spastic gait | reported | — | HP:0002064 Spastic gait ✔ |
| Putaminal thinning / atrophy on MRI | 4/4 | — | HP:0031982 Abnormal putamen morphology ✔ |
| Caudate-head swelling on MRI | 4/4 | — | HP:0002134 Abnormal basal ganglia morphology ✔ (a caudate-specific HPO term was not in the cache ⚠) |
| Marked cerebral hypometabolism on FDG-PET | reported (Al-Owain 2013) | — | ⚠ HPO term to be looked up |
| Seizures | **not reported** in MCIDDS | — | Do not bind (contrast with the de novo KCNA4 DEE case) |

**Mode of inheritance:** HP:0000007 Autosomal recessive inheritance ✔.

**Quality of life.** No formal QoL instruments have been used. The likely burden is moderate:
- vision loss needing cataract surgery, plus glaucoma risk;
- ADHD and mild ID affecting schooling;
- a dystonic, spastic gait affecting mobility.

---

## 4. Genetic / Molecular Information

**Gene:** KCNA4 (hgnc:6222), Kv1.4. UniProt P22459, 653 aa.

**Protein features (UniProt):**
- Disordered N-terminal region 24–148, with a basic-residue stretch at 81–97.
- Six transmembrane segments: S1 305–326 through S6 539–567.
- S4 voltage sensor at 440–460.
- Pore helix at 512–523 and selectivity filter at 524–529.
- C-terminal PDZ-binding motif at 651–653.
- PKA phosphosite at Ser90, next to the disease residue.
- Kv1.4 can form heterotetramers with KCNA1, KCNA2 and KCNA5, and is modulated by KCNAB1/2.
- Expression is highest in brain and lower in testis, lung, kidney, colon and heart.

**The pathogenic variant:**

| Field | Value |
|---|---|
| HGVS | NM_002233: c.266G>A, p.(Arg89Gln) (R89Q); rs779101828 |
| Location | Disordered/low-complexity N-terminal region, basic stretch 81–97. It lies outside the N-terminal inactivation, T1/BTB, and ion-transport Pfam domains (Kaya 2016) and directly precedes the PKA site Ser90 (UniProt) |
| Type | Missense |
| Zygosity / origin | Homozygous, germline. Parents are heterozygous |
| Population frequency | 2 heterozygotes in ExAC (Kaya 2016). Absent from 747 + 428 Saudi exomes |
| Classification | UniProt: uncertain significance. ClinVar could not be accessed (NCBI blocked) ⚠ |
| Function | Partial loss of function (≈18% current reduction; §6) |

**Gene–disease validity (GenCC, thegencc.org/genes/HGNC:6222):**
- Ambry Genetics: Limited, AR (2018).
- Labcorp/Invitae: Limited, MOI unknown (2020).
- G2P: Limited, AR (2025).
- No ClinGen (CGGV) curation was found. Following repo rules, `gene_disease_validity` may copy these "Limited" tiers with `classified_by` set to the submitter, but the GenCC row would need to be cited as the source.

**Other KCNA4 phenotype (allelic, distinct):**
- Tsai et al. 2025 report a de novo heterozygous Kv1.4 **p.V558L** in the S6 hinge in one child with early-onset developmental and epileptic encephalopathy (PMID:40472070).
- Patch clamp showed *"severe loss-of-function"*, with trafficking preserved. The authors propose *"Kv1.4 as a novel epilepsy-related gene."*
- This should not be merged into MCIDDS: different inheritance, different phenotype, and n = 1.

**Not applicable or not reported:** modifier genes, epigenetic findings, chromosomal abnormalities, somatic variants.

---

## 5. Environmental Information

None known. MCIDDS is a monogenic Mendelian disorder with no reported environmental, lifestyle or infectious contributors.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Homozygous KCNA4 c.266G>A p.(Arg89Gln)** changes a conserved basic residue in the disordered N-terminus of Kv1.4. *Demonstrated genetically* (PMID:27582084).
2. This **leads to a modest loss of Kv1.4 channel function**. In *Xenopus* oocytes (two-electrode voltage clamp, +60 mV) peak current was WT 17 ± 0.7 µA vs R89Q 14 ± 0.9 µA (p < 0.05, n = 8). Co-expression of WT with R89Q gave 14 ± 0.9 µA, which indicates loss of function. A dominant-negative effect was not demonstrated, and rapid inactivation was preserved. *Demonstrated in vitro* (PMID:27582084).
   - *Inferred, untested:* R89Q might alter PKA phosphorylation at the adjacent Ser90 or binding of partners such as DLG1/DLG2/synaptotagmin I.
3. **Branch A: brain.** Less A-type K⁺ current (GO:0071805 potassium ion transmembrane transport ✔; GO:0005249 voltage-gated potassium channel activity ✔) **is inferred to cause** altered neuronal action-potential repolarization and excitability (GO:0019228 neuronal action potential ✔). Kv1.4 is concentrated in striatal and other CNS axonal and presynaptic compartments.
   - 3a. This **is inferred to result in** dysfunction and degeneration of striatal neurons, mainly medium spiny neurons (CL:1001474 ✔). The imaging correlate is **putaminal atrophy with caudate-head swelling** (UBERON:0001874 putamen ✔, UBERON:0001873 caudate nucleus ✔, UBERON:0002435 striatum ✔). FDG-PET hypometabolism shows the functional deficit (PMID:23181898).
     - The link from reduced Kv1.4 to striatal structural change is **speculative**, as the authors themselves say.
     - Indirect support: in mice, A-type current is up-regulated in ischemia-resistant striatal neurons, and Kv1.4/Kv4.2 loss increases vulnerability (PMID:21673715). This is model-organism evidence about ischemia, not MCIDDS.
   - 3b. Basal-ganglia circuit dysfunction **leads to** dystonia, cogwheel rigidity and dysarthria.
   - 3c. Cortical and global neuronal dysfunction during development **leads to** microcephaly, mild ID and ADHD. *Inferred.*
   - 3d. Pyramidal signs (hyperreflexia, Babinski sign, spastic gait) suggest corticospinal involvement. The mechanism is unknown.
4. **Branch B: lens.** KCNA4 mRNA is present in mouse lens and retina (RT-PCR, n = 2; PMID:27582084). Loss of lens K⁺ conductance **is inferred to disturb** lens-fibre ion homeostasis and membrane potential (CL:0011004 lens fiber cell ✔; GO:0002088 lens development in camera-type eye ✔). This **results in** bilateral cataract (UBERON:0000965 lens of camera-type eye ✔). *Speculative:* no lens functional data exist.
   - 4a. Cataract (and/or its surgery) is followed by secondary glaucoma and corneal opacity in one patient.
5. **Branch C: growth.** Growth retardation has no proposed mechanism.

### Checklist notes

- **Protein dysfunction.** This is partial loss of function, not complete. The modest effect size (~18%) set against a severe multisystem phenotype is the main reason the gene–disease link is rated "Limited."
- **Cellular location.** GO:0008076 voltage-gated potassium channel complex ✔. The protein sits at the plasma membrane and axon.
- **Cell types.** Medium spiny neuron (CL:1001474 ✔); neuron (CL:0000540 ✔); lens fiber cell (CL:0011004 ✔).
- **Not reported:** metabolic, immune and epigenetic changes, and any omics, single-cell or CRISPR-screen data.

---

## 7. Anatomical Structures Affected

- **Primary organs.** Brain: the striatum (caudate swelling, putaminal atrophy) and the cortex (microcephaly). Eye: the lens.
- **Secondary.** Anterior segment of the eye (glaucoma, corneal opacity, in 1 of 4) and somatic growth.
- **Body systems.** Nervous system, visual system, growth.
- **Lateralization.** Cataracts and MRI changes are bilateral. Glaucoma was unilateral (left) in one patient.
- **Cells.** Striatal neurons, lens fibre cells (inferred).
- **Subcellular.** Plasma membrane, voltage-gated K⁺ channel complex, axon.

---

## 8. Temporal Development

- **Onset.** Congenital or infantile: early motor delay, microcephaly and growth retardation. Cataracts are "congenital" but were usually diagnosed in the first decade.
- **Course.** Neurological phenotype *"very slowly progressive"* (PMID:23181898). Lifelong.
- **Stages, remission, critical periods.** None defined. Early cataract removal is the main time-sensitive intervention, because of the risk of amblyopia (general paediatric principle, not MCIDDS-specific data).

---

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007 ✔). Both parents of the index family are first cousins and heterozygous carriers.
- **Prevalence.** Unknown; only 4 patients have been described. Orphanet-style class: ultra-rare (<1/1,000,000), or cases-in-literature = 4 (1 family).
- **Penetrance and expressivity.** Complete in the family (4/4 homozygotes affected, heterozygous parents unaffected). Severity varied: ADHD was most severe in the youngest, language delay affected 3 of 4, and glaucoma 1 of 4.
- **Population.** One Saudi Arabian family. The R89Q allele is very rare in ExAC (2 heterozygotes). No founder effect has been established.
- **Sex ratio.** 3 F : 1 M; too few cases to interpret.
- **Not reported:** anticipation, germline mosaicism.

---

## 10. Diagnostics

- **Clinical recognition.** Suspect MCIDDS in a child with:
  - bilateral early cataract;
  - microcephaly and growth delay;
  - mild ID with ADHD;
  - dystonia with pyramidal signs;
  - the MRI pattern of swollen caudate heads with thin putamina.
- **Imaging.** Brain MRI is key. FDG-PET showed marked hypometabolism (PMID:23181898).
- **Genetic testing.** The recommended route is exome or genome sequencing, especially in consanguineous families, as done in the index family. Supporting steps:
  - SNP-array autozygosity mapping;
  - targeted confirmation of KCNA4 variants;
  - parental segregation testing.

  KCNA4 is not on most congenital-cataract panels, so a negative cataract panel does not exclude MCIDDS. CMA, karyotype, FISH, mtDNA and repeat-expansion testing have no specific role, apart from excluding differentials.
- **Functional confirmation.** For a novel variant, consider heterologous expression and electrophysiology (oocyte TEVC or patch clamp), as done for R89Q and V558L.
- **Biomarkers and laboratory tests.** None known.
- **Differential diagnosis:**
  - other syndromic congenital cataract with ID, such as Marinesco–Sjögren syndrome, cerebrotendinous xanthomatosis, Lowe syndrome, and congenital disorders of glycosylation;
  - striatal or basal-ganglia disorders with dystonia, such as mitochondrial and Leigh syndrome, glutaric aciduria type 1, Wilson disease, and NBIA (eye-of-the-tiger sign);
  - 11p chromosomal disorders, such as WAGR/PAX6 deletion. PAX6 lies in the original linkage interval and was excluded by sequencing;
  - KCNA4 de novo DEE (PMID:40472070), which has seizures and dominant inheritance.
- **Screening.** No newborn screening. Cascade carrier testing is possible within the family.

---

## 11. Outcome / Prognosis

There are no survival or life-expectancy data. All four siblings survived childhood. The disability profile is:
- mild ID;
- ADHD;
- visual impairment from cataract, with secondary glaucoma risk;
- a progressive dystonic and spastic movement disorder.

Prognostic factors and biomarkers are unknown.

---

## 12. Treatment

There is no disease-specific or mechanism-targeted therapy. Arizona Hereditary Ocular Diseases database: *"No treatment is available for the general condition. Cataract surgery may be considered."* Management is supportive.

| Intervention | Notes | Suggested NCIT |
|---|---|---|
| Cataract extraction (± lens implant); glaucoma management | At least 1 patient underwent cataract surgery | NCIT:C15329 Surgical Procedure ✔ (a cataract-specific NCIT procedure term needs a lookup ⚠) |
| Pharmacotherapy for ADHD (stimulants) and for dystonia (e.g., anticholinergics, botulinum toxin) | Standard symptomatic care; **no MCIDDS-specific outcome data** | NCIT:C15986 Pharmacotherapy ✔ |
| Physical therapy | For spasticity and dystonia | NCIT:C15302 Physical Therapy ✔ |
| Occupational therapy | | NCIT:C121351 Occupational Therapy ✔ |
| Speech-language therapy | For language delay and dysarthria (3/4) | NCIT:C159273 Speech Language Therapy ✔ |
| Genetic counseling | Recurrence risk 25% for carrier parents | NCIT:C15240 Genetic Counseling ✔ |

**Speculative, untested:** Kv channel openers would in principle oppose loss of function. No KCNA4-selective opener is in clinical use, and a 2025 review of K⁺-channel openers (PMID:41155561) does not establish one.

**Not available:** gene therapy, ASO and clinical trials. No NCT registrations were found.

---

## 13. Prevention

- **Primary.** Genetic counseling for consanguineous couples and carrier testing of relatives. Prenatal diagnosis or PGT-M is possible once familial variants are known.
- **Secondary.** Early ophthalmological examination of at-risk siblings, so cataract is found and treated early.
- **Tertiary.** Glaucoma surveillance after cataract surgery, plus orthopaedic and physiotherapy care to limit contractures.
- **Not applicable:** vaccines, public-health or environmental measures.

---

## 14. Other Species / Natural Disease

- **Animal disease.** No naturally occurring KCNA4 disease is reported. OMIA was not checked ⚠.
- **Orthologs.** Mouse *Kcna4* (MGI:96661); rat, zebrafish and Drosophila Shaker-family homologues exist.
- **Conservation.** Kv1 channels are highly conserved.
- **Transmission.** Not applicable (not zoonotic).

---

## 15. Model Organisms

- **Mouse *Kcna4* knockout** (Kcna4^tm1Lndn; London et al. 1998, PMID:9547391):
  - Homozygotes are viable, fertile and grossly normal.
  - MGI: *"a small subset of mutants exhibit spontaneous seizure activity."*
  - The original paper studied the cardiac transient outward current (Ito). It concluded that Kv1.4 is *"not the molecular basis of Ito in adult murine ventricular myocytes"*.
  - **No cataract, microcephaly or striatal phenotype has been reported.** In a KB `animal_models` link this would be `FAILS_TO_RECAPITULATE` / `PARTIALLY_RECAPITULATES` with LOW fidelity. A `HUMAN_MODEL_MISMATCH` discussion is warranted.
- **Kv1.4/Kv4.2 double-deficient mice:** increased striatal neuronal vulnerability to ischemia (PMID:21673715). This is indirect evidence for a protective role of A-type current in striatum.
- **In vitro:** *Xenopus* oocyte expression of R89Q (PMID:27582084); patch clamp of V558L (PMID:40472070). The 2025 study's Drosophila model concerned the KCNA3 variant, not KCNA4.
- **Not reported:** knock-in models of R89Q, zebrafish, iPSC-derived striatal neurons, lens organoids, and IMPC phenotyping.

---

## Evidence gaps and curation cautions

1. **A single family, with linkage to a 45.9 Mb interval.** Autozygosity reduced it to 12 genes, but this is still a single-family, single-variant gene–disease claim. GenCC rates it "Limited" three times over.
2. **A modest functional effect.** The ~18% current reduction is hard to reconcile with a severe multisystem phenotype. Any pathophysiology edges beyond "KCNA4 loss of function" should be marked inferred or hypothetical (EMERGING hypothesis status).
3. **Allelic de novo DEE.** The case of PMID:40472070 is a separate entity, or at most a `has_subtypes`-level note. It should not add seizures to MCIDDS.
4. **Unchecked sources.** OMIM, Orphanet and ClinVar could not be accessed automatically and should be checked by a curator.

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 23181898 | Al-Owain M et al. A novel syndrome of abnormal striatum and congenital cataract: evidence for linkage to chromosomes 11. *Clin Genet* 2013;84(3):258-264 | Human clinical |
| 27582084 | Kaya N et al. KCNA4 deficiency leads to a syndrome of abnormal striatum, congenital cataract and intellectual disability. *J Med Genet* 2016;53(11):786-792. doi:10.1136/jmedgenet-2015-103637; PMC13044907 | Human clinical + in vitro |
| 40472070 | Tsai MH et al. De novo missense variants of KCNA3, KCNA4, and KCNA6 cause early onset developmental epileptic encephalopathy. *Hum Mol Genet* 2025;34(16):1392-1404 | Human clinical + in vitro |
| 9547391 | London B et al. The transient outward current in mice lacking the potassium channel gene Kv1.4. *J Physiol* 1998;509:171-182 | Model organism |
| 21673715 | Up-regulation of A-type potassium currents protects neurons against cerebral ischemia. *J Cereb Blood Flow Metab* 2011 | Model organism |

Sources:
- [Kaya et al. 2016, J Med Genet (PMC full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13044907/)
- [JMG article page](https://jmg.bmj.com/content/53/11/786)
- [JMG blog summary](https://blogs.bmj.com/jmg/2016/08/31/kcna4-deficiency-leads-to-a-syndrome-of-abnormal-striatum-congenital-cataract-and-intellectual-disability/)
- [OAR@UM record](https://www.um.edu.mt/library/oar/handle/123456789/28242)
- [Europe PMC REST: PMID 27582084](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:27582084&resultType=core&format=json)
- [Europe PMC REST: PMID 23181898](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23181898&resultType=core&format=json)
- [Europe PMC REST: PMID 40472070](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40472070&resultType=core&format=json)
- [Arizona Hereditary Ocular Diseases entry](https://disorders.eyes.arizona.edu/node/3149)
- [MalaCards MCIDDS](https://www.malacards.org/card/microcephaly_cataracts_impaired_intellectual_development_and_dystonia_with_abnormal_striatum)
- [OMIM #618284](https://omim.org/entry/618284)
- [OMIM *176266](https://www.ncbi.nlm.nih.gov/omim/176266)
- [GenCC KCNA4](https://thegencc.org/genes/HGNC:6222)
- [UniProt P22459](https://rest.uniprot.org/uniprotkb/P22459.txt)
- [MGI Kcna4](https://www.informatics.jax.org/marker/MGI:96661)
- [MGI Kcna4 targeted allele](https://informatics.jax.org/allele/MGI:2386331)
- [humandiseasegenes.nl KCNA4](https://humandiseasegenes.nl/kcna4/parents)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `EXT_ID`.

37 of 43 terms resolved to a current term; the rest could not be looked up either way.