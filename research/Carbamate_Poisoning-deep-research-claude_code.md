---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-10-28T18:22:44.354225'
end_time: '2026-10-28T18:27:36.967133'
duration_seconds: 292.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Carbamate Poisoning
  mondo_id: ''
  category: Environmental
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: carbamate insecticide poisoning; carbamate intoxication; carbamate toxicity
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 6
  num_turns: 13
  total_cost_usd: 2.4545914
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 22
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 1
  validator_version: 0.4.0
term_validation:
  total_terms: 55
  verified: 52
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 9
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0005605
    ontology_label: GO_0005605
    replaced_by: GO:0005604
  unresolvable_prefixes:
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Carbamate Poisoning
- **MONDO ID:**  (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** carbamate insecticide poisoning; carbamate intoxication; carbamate toxicity
- **Category:** Environmental

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Carbamate Poisoning** covering all of the
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

This is a legitimate clinical toxicology research task — carbamate poisoning is a medical/pesticide-toxicology condition treated in emergency medicine. Let me proceed with clinical research framing.

Let me gather specific PMIDs, identifiers, and mechanistic detail.

# Research Report: Carbamate Poisoning

**Scope note:** This is an acquired, environmental/toxicological disease (acute poisoning by N-methyl carbamate anticholinesterase insecticides), not a Mendelian disorder. There is **no causal gene** — the template field "causal gene(s): not recorded" is correct, and the per-paragraph gene-naming instruction does not apply. The molecular target of the toxicant is the host enzyme **acetylcholinesterase (gene *ACHE*, hgnc:108)**, which is inhibited rather than mutated. I flag throughout where the task template's germline-genetics framing is not applicable.

A caveat on verification: PMIDs below are given where I am confident; where I could only confirm a PMC ID or DOI I say so explicitly rather than inventing a PMID. Per dismech evidence rules, every identifier should be re-fetched with `just fetch-reference` before it is written into an entry, and every quoted snippet re-verified against the cached source.

---

## 1. Disease Information

**Overview.** Carbamate poisoning is an acute cholinergic toxidrome caused by exposure (ingestion, inhalation, or dermal) to N-methyl carbamate insecticides. These compounds reversibly **carbamylate acetylcholinesterase (AChE)** at cholinergic synapses, causing acetylcholine to accumulate at muscarinic receptors, nicotinic receptors (neuromuscular junction and autonomic ganglia), and in the CNS. The clinical picture is essentially indistinguishable at the bedside from organophosphate (OP) poisoning, but the enzyme–inhibitor bond is spontaneously hydrolyzed (decarbamylation) and, critically, **does not "age,"** so recovery of enzyme function is generally faster and the classic delayed syndromes are much less prominent ([AJEM review](https://ajemjournal.com/article/S0735-67570900059-X/fulltext); [WikEM: Carbamates](https://wikem.org/wiki/Carbamates); [StatPearls](https://statpearls.com/sp/al/21/30316/)).

**Key identifiers.**
- **ICD-10-CM:** T60.0 — *Toxic effect of organophosphate and carbamate insecticides* (carbamates share the code with OPs) ([AAPC T60.0](https://www.aapc.com/codes/icd-10-codes/T60.0); [gesund.bund.de T60](https://gesund.bund.de/en/icd-code-search/t60)).
- **ICD-11:** NE61 *Harmful effects of or exposure to noxious substances, chemical category* / 9D00-range for organophosphate & carbamate — verify against the live ICD-11 browser; carbamates are coded with OPs there as well.
- **MeSH:** No single descriptor for "carbamate poisoning." Relevant descriptors are *Carbamates* (class) and specific agents, e.g., **Carbofuran D002235** (CAS 1563-66-2; UNII SKF77S6Y67; UMLS C0006995) ([NLM MeSH D002235](https://meshb.nlm.nih.gov/record/ui?ui=D002235); [CISMeF](https://www.cismef.org/page/detail/en/MSH_D_002235)). The umbrella descriptor *Cholinesterase Inhibitors* (D002800) is also relevant.
- **MONDO:** **No dedicated MONDO term for carbamate insecticide poisoning exists** at the time of writing — an OLS search of MONDO returns only unrelated carbamoyl/carbamazepine entries ([OLS MONDO query]). This is an `OUT_OF_SCOPE`-vs-curate consideration for the queue; if curated, it would likely anchor on a broad chemical-poisoning MONDO parent with `skos:narrowMatch`, or motivate a new-term request.
- **ECTO:** **ECTO:9000282** *exposure to carbamate* — the directly usable exposure term for the `environmental:` block.
- **Orphanet:** No specific ORPHA code (acute toxic exposure, not a rare disease).

**Data provenance.** Information is from **aggregated disease-level** clinical toxicology literature (prospective cohorts, reviews, poison-center references), not individual EHR records.

**Synonyms:** carbamate insecticide poisoning; carbamate intoxication; carbamate toxicosis; anticholinesterase carbamate poisoning; (agent-specific) aldicarb/carbofuran/carbaryl/methomyl/propoxur poisoning.

---

## 2. Etiology

**Primary cause — environmental/toxicological (not genetic).** Exposure to an N-methyl carbamate insecticide. Common agents and their approximate human relevance:
- **Aldicarb** (Temik; highly toxic, WHO Class Ia) — notorious in malicious/deliberate poisonings ("Tres Pasitos"), CHEBI:38511.
- **Carbofuran** (Furadan; WHO Ib) — a leading agent in South Asian self-poisoning; CHEBI:34611, CAS 1563-66-2.
- **Carbosulfan** (a carbofuran pro-insecticide, WHO II) — high human case fatality despite lower hazard class.
- **Fenobucarb (BPMC)** — liquid formulation, South/Southeast Asia.
- **Methomyl** (Lannate; WHO Ib) — CHEBI:34848.
- **Carbaryl** (Sevin; WHO II) — CHEBI:3390, the prototypical lower-toxicity carbamate.
- **Propoxur** (Baygon) — household insecticide; frequent in accidental/pediatric and some deliberate exposures ([Baygon case overview](https://cme30.eu/?p=49643)).
- **Methiocarb**, **bendiocarb**, **oxamyl**, **pirimicarb** — other agrochemical carbamates.

(Note: carbaryl CHEBI, methomyl CHEBI etc. should be re-verified in CHEBI before binding.)

**Routes of exposure / risk contexts (environmental risk factors).**
- **Deliberate self-poisoning (suicide)** — the dominant cause of severe cases and deaths in low- and middle-income agricultural regions (South Asia, Southeast Asia) ([Sri Lanka carbamate cohort, PMC4950420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4950420/)).
- **Occupational** — agricultural applicators, formulators, re-entry workers (dermal/inhalational).
- **Accidental** — children ingesting household products (e.g., propoxur baits); contaminated food.
- **Homicidal/malicious** — aldicarb in particular.

**Risk factors:** rural agricultural residence; ready access to concentrated liquid formulations; absence of regulatory bans; psychiatric illness/acute distress (for self-poisoning); occupational handling without PPE.

**Protective factors (population/policy level):** national **pesticide regulation and bans** on the most lethal agents — a well-documented structural intervention. Sri Lankan pesticide regulation markedly reduced acute poisoning deaths ([Influence of pesticide regulation on poisoning deaths, archive.cmb.ac.lk](https://archive.cmb.ac.lk/items/14377362-2b71-4b8c-bc10-9429a4b915f0); [Lancet Glob Health 2021](https://doaj.org/article/44f3b05b293a45f1976a60d1d06b2a67)). PPE, safe storage, and dilution of formulations are secondary protective measures.

**Gene–environment interaction.** The pharmacologically relevant host-variation axis is **not a disease-causing variant** but **detoxification enzyme polymorphism**: paraoxonase-1 (*PON1*) and butyrylcholinesterase (*BCHE*) variants modulate response to anticholinesterase pesticides. *PON1* is classically tied to OP (oxon) hydrolysis more than carbamates; *BCHE* activity affects scavenging capacity. These are **modifiers of susceptibility/severity**, not causal. (Evidence base is stronger for OPs than carbamates — flag as INDIRECT/uncertain for carbamate-specific claims.)

---

## 3. Phenotypes

The toxidrome is **acute-onset** (minutes to ~2 hours post-exposure), **generally transient** (hours to a few days as AChE spontaneously reactivates), and dominated by cholinergic excess. Mnemonics: muscarinic **DUMBELS** (Defecation, Urination, Miosis, Bronchorrhea/Bronchospasm/Bradycardia, Emesis, Lacrimation, Salivation) and **SLUDGE/BBB** ([Medscape](https://img.medscape.com/pi/iphone/medscapeapp/html/A816221-business.html); [StatPearls](https://statpearls.com/sp/al/21/30316/)).

**Muscarinic (clinical signs/autonomic):**
- Miosis — HP:0000545 (Myopia is different; pinpoint pupils → **HP:0030810 Miosis**)
- Hypersalivation — **HP:0002307** (Drooling) / sialorrhea
- Bronchorrhea & bronchospasm → respiratory distress — **HP:0002094 Dyspnea**, **HP:0002104 Apnea**; excessive airway secretions (no precise HP; coarse)
- Lacrimation — **HP:0009926 (Increased lacrimation / Epiphora)**
- Diarrhea — **HP:0002014**; vomiting — **HP:0002013**
- Urinary incontinence — **HP:0000020**
- Bradycardia — **HP:0001662**; hypotension — **HP:0002615**
- Sweating/diaphoresis — **HP:0000975 (Hyperhidrosis)**

**Nicotinic (neuromuscular / ganglionic):**
- Muscle fasciculations — **HP:0002380 (Fasciculations)**
- Muscle weakness — **HP:0001324**; progressing to flaccid paralysis and **respiratory muscle failure** (the main proximate cause of death)
- Tachycardia/hypertension (ganglionic, early) — **HP:0001649 / HP:0000822**

**CNS:**
- Altered consciousness, drowsiness, coma — **HP:0001259 (Coma)**, **HP:0001250 (Seizure)**
- Confusion/agitation — **HP:0001289**
- Seizures (especially severe/pediatric)
- *Note:* Carbamates cross the blood–brain barrier **less readily than many OPs** (e.g., carbaryl), so CNS effects may be relatively less prominent for some agents — but highly lipophilic/potent carbamates (aldicarb, carbofuran) produce profound CNS depression and seizures.

**Laboratory abnormalities:**
- **Depressed red-cell (true/AChE) and plasma (butyryl-/pseudo-) cholinesterase activity** — the key biomarker, but **spontaneous in-vitro reactivation of carbamylated enzyme can cause falsely normal or rapidly recovering levels**, making ChE a less reliable confirmatory test than in OP poisoning. LOINC: RBC acetylcholinesterase e.g. **LOINC:32460-1** (verify); serum/plasma cholinesterase **LOINC:2098-2** (Cholinesterase, verify exact code and Long Common Name before binding).
- Hyperglycemia, leukocytosis, metabolic/respiratory acidosis, hypokalemia (variable).

**Onset/severity/progression/frequency.** Onset acute (minutes–2 h). Severity ranges mild→fatal; dose- and agent-dependent. Course **episodic/self-limited** — most survivors recover within 24–48 h as enzyme reactivates, **shorter than OP poisoning**; carbamates "do not lead to chronic toxicity or delayed syndromes" in the classic teaching because the bond hydrolyzes spontaneously ([StatPearls](https://statpearls.com/sp/al/21/30316/)). Frequency of individual signs is not well-quantified per-agent in the literature; bronchorrhea/respiratory failure drives mortality.

**Quality-of-life impact.** For survivors, usually full recovery with no chronic sequelae (contrast OP, which can leave intermediate syndrome / OPIDN / chronic neuropsychiatric effects). The major burden is **acute mortality** in deliberate poisoning rather than chronic disability.

---

## 4. Genetic / Molecular Information

**Not applicable as a germline/causal-gene disorder.** There are no causal genes, pathogenic variants, inheritance, allele frequencies, somatic/germline distinctions, modifier-gene disease loci, chromosomal abnormalities, or disease-specific epigenetics — this is an acquired chemical intoxication. The template's sections 4 (causal genes/variants), 9 (inheritance/penetrance/consanguinity/founder effects), and the genetic parts of 10 (genetic testing) and 13 (carrier/prenatal screening) are **N/A** and should be recorded as such in the entry.

The only molecular genetics worth noting are **host pharmacogenetic modifiers** (§2): *BCHE* (butyrylcholinesterase, hgnc:983) and *PON1* (paraoxonase-1, hgnc:9204) variants may modify scavenging/detoxification. These are susceptibility/severity modifiers, not causes, and the carbamate-specific evidence is weaker than for OPs — curate as INDIRECT if at all.

---

## 5. Environmental Information

This is the **core etiology** of the disease (see §2).
- **Environmental/toxic factor:** N-methyl carbamate insecticide exposure. **ECTO:9000282 (exposure to carbamate)** is the directly bindable exposure term for an `environmental[].exposure_term` block. CTD contains extensive toxicogenomic data for carbofuran, aldicarb, carbaryl, methomyl (chemical–gene/phenotype interactions) — a good source for mechanism snippets.
- **Occupational/lifestyle:** agricultural work, pesticide application, formulation/packaging.
- **Infectious agents:** None — not applicable.

For the pathograph, the environmental node should link via `influences_mechanisms` with `environmental_effect: TRIGGERS` to a "Systemic carbamate exposure / AChE carbamylation" pathophysiology node (mirroring the `Arsenic_Poisoning` worked pattern in CLAUDE.md).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Exposure** (ingestion / dermal / inhalation) of an N-methyl carbamate **leads to** systemic absorption and distribution of the parent carbamate (and, for pro-insecticides like carbosulfan, bioactivation to the active carbamate).
2. Circulating carbamate **reaches cholinergic synapses and the neuromuscular junction** and **results in carbamylation of the catalytic serine hydroxyl of acetylcholinesterase** (and butyrylcholinesterase), forming a **carbamyl–enzyme conjugate** — a reversible covalent modification. *(Demonstrated biochemically.)*
3. Carbamylated AChE **cannot hydrolyze acetylcholine**, which **leads to accumulation of acetylcholine** in the synaptic cleft at muscarinic receptors, nicotinic receptors, and CNS synapses.
4. Excess ACh at **muscarinic receptors leads to** the parasympathetic/exocrine signs (miosis, bronchorrhea, bronchospasm, bradycardia, salivation, lacrimation, GI hypermotility, urinary signs).
5. Excess ACh at **nicotinic receptors (NMJ/ganglia) leads to** fasciculations → depolarizing blockade → muscle weakness → **flaccid paralysis of respiratory muscles**.
6. Excess ACh in the **CNS leads to** agitation, seizures, and central respiratory depression.
7. **Branch point — divergence from OP poisoning:** the carbamyl–enzyme bond **undergoes spontaneous hydrolysis (decarbamylation)** and, crucially, **does not undergo "aging"** (irreversible dealkylation). This **leads to** spontaneous reactivation of AChE over hours and **results in** a shorter, usually self-limited course, with the classic OP delayed syndromes (intermediate syndrome, OPIDN) being largely absent or rare. *(Aging is OP-specific: [USPTO patent background](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11492340); [toxicology study guide](https://open-exam-prep.com/study-guides/ct-pesticide-applicator/toxicology-health-ppe/organophosphates-cholinesterase).)* **Caveat/inferred:** the *speed* of spontaneous reactivation is disputed — lay sources say "rapid," but primary data (e.g., Reiner's reactivation-rate tabulations, [PMC2428035](https://pmc.ncbi.nlm.nih.gov/articles/PMC2428035); and a rivastigmine–enzyme study showing <10% Torpedo-enzyme reactivation at 48 h, [Proteopedia 1gqs](https://proteopedia.org/w/1gqs)) show it is enzyme- and compound-dependent and can be slow. This nuance underlies the **oxime controversy** (§12).
8. Proximate cause of death: **respiratory failure** (bronchorrhea + bronchospasm + respiratory-muscle paralysis + central depression), compounded by aspiration and, less commonly, early cardiac events ([Eddleston treatment protocol, PMC1065055](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1065055/)).

### Checklist detail
- **Molecular pathway / target:** cholinergic neurotransmission; target enzyme **acetylcholinesterase (*ACHE*)**, molecular function **GO:0003990 (acetylcholinesterase activity)**, inhibited (`modifier: DECREASED`); downstream **GO:0007271 (synaptic transmission, cholinergic)**, increased ACh at receptors (**GO:0095500 acetylcholine receptor signaling pathway**).
- **Cellular processes:** cholinergic over-stimulation of smooth muscle, exocrine glands, skeletal muscle (motor end-plate depolarization block), neurons. Cell types: **CL:0000100 (motor neuron)**, **CL:0000187 (muscle cell)** / skeletal muscle fiber, cholinergic neurons (**CL:0000108 cholinergic neuron**), exocrine gland cells, bronchial smooth muscle.
- **Protein dysfunction:** reversible covalent inhibition (carbamylation) of AChE/BChE — a loss of catalytic function of the enzyme (not misfolding/aggregation).
- **Receptors:** muscarinic ACh receptors (CHRM1-5) and nicotinic ACh receptors (CHRNA/B families) over-activated downstream.
- **Immune system:** not primary.
- **Tissue damage:** generally functional/reversible rather than structural; secondary injury from hypoxia, seizures, aspiration pneumonitis.
- **Metabolic:** secondary acidosis, hyperglycemia.
- **CHEBI anchors:** carbamate class **CHEBI:13941**; acetylcholine **CHEBI:15355**; atropine **CHEBI:16684**; pralidoxime **CHEBI:8352** (verify).

---

## 7. Anatomical Structures Affected

- **Body systems:** autonomic nervous system; respiratory; neuromuscular; cardiovascular; GI; CNS.
- **Primary organs:** nervous system / neuromuscular junction (functional target); lungs/airways (**UBERON:0002048 lung**, bronchi **UBERON:0002185**) — bronchorrhea/bronchospasm; eye (pupil, **UBERON:0001771 pupil** → miosis); exocrine glands (salivary **UBERON:0001044**, lacrimal **UBERON:0001817**).
- **Secondary:** heart (**UBERON:0000948**) — brady/tachyarrhythmia; brain (**UBERON:0000955**) — seizures, central respiratory depression; skeletal muscle (**UBERON:0001134**), diaphragm (**UBERON:0001103**) — paralysis.
- **Tissue/cell level:** neuromuscular junction (**UBERON:0002375 muscle tissue / GO:0031594 neuromuscular junction**); cholinergic synapses.
- **Subcellular:** synaptic cleft; AChE is anchored at the synaptic basal lamina / cell membrane (**GO:0045202 synapse**, **GO:0005605 basal lamina**).
- **Localization:** systemic/bilateral (miosis bilateral; weakness generalized).

---

## 8. Temporal Development

- **Onset:** acute, minutes to ~2 h after exposure (faster with ingestion of concentrated liquids).
- **Pattern:** acute toxidrome; **self-limited** in survivors.
- **Progression:** rapid peak; **recovery typically within 24 h and usually complete within 24–48 h** as AChE reactivates — notably **shorter than OP poisoning**.
- **Critical period / intervention window:** the first hours — airway protection and atropine titration are life-saving in this window; death is early (respiratory, occasionally cardiac).
- **Delayed syndromes:** classically **absent** — carbamates generally do not cause the OP **intermediate syndrome (24–96 h muscle paralysis)** or **OP-induced delayed polyneuropathy (OPIDN, 2–3 weeks)** ([CDC ATSDR intermediate syndrome material](https://archive.cdc.gov/www_atsdr_cdc_gov/csem/cholinesterase-inhibitors/intermediate_syndrome.html)). **Exceptions/uncertainty:** rare **suspected** intermediate-syndrome-like presentations are reported, chiefly in **veterinary** cases (methiocarb and aldicarb in dogs — [Tinson 2017 Aust Vet J](https://bioweb.supagro.inrae.fr/ESTHER/paper/Tinson_2017_Aust.Vet.J_95_201); Klainbart et al. anticholinesterase dog review) and isolated human reports; curate these as a `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP` discussion rather than an established feature.

---

## 9. Inheritance and Population

**Inheritance: not applicable** (acquired intoxication — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency).

**Epidemiology.**
- Carbamates are a major component of the global pesticide self-poisoning burden, concentrated in rural Asia. WHO-era estimates put **pesticide self-poisoning case fatality in the developing world at 10–20%, up to 50–70% for the most toxic agents** ([Eddleston protocol, PMC1065055](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1065055/)).
- **Prospective carbamate cohort (Sri Lanka, 6 hospitals; *Clinical Toxicology* 2016;54:624–631, DOI 10.1080/15563650.2016.1187735; PMC4950420):** **n = 1,288** carbamate self-poisonings (carbofuran powder n=719; carbosulfan EC25 n=389; fenobucarb EC50 n=127). **183 (14.2%) required intubation/ventilation; 71 (5.5%) died.** Case fatality by agent: **carbofuran ≈2.2%, fenobucarb ≈6.3% (OR ~3.0 vs carbofuran), carbosulfan ≈11.1% (OR ~5.5)** — higher mortality with the high-strength liquid formulations despite lower WHO hazard class ([PMC4950420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4950420/)). Reduced GCS at presentation predicted worse outcome.
- **Atropine safety cohort (Konickx, Eddleston et al.; OP + carbamate, n=1,957):** early atropine given before oxygen — **primary cardiac death within 3 h of atropine in only 4/1,957 (0.2%)**; most deaths were later respiratory ([search summary; confirm PMID before citing]).
- **Lancet Global Health 2021:** since 2013 the five deadliest agents in Sri Lanka (including fenobucarb and carbosulfan) had case fatality 7.2–8.6% ([DOAJ](https://doaj.org/article/44f3b05b293a45f1976a60d1d06b2a67)).

**Demographics:** predominantly working-age adults in deliberate self-poisoning (regional sex ratios vary); children in accidental household exposures. **Geographic:** South/Southeast Asia, sub-Saharan Africa, agricultural LMICs.

Prevalence/incidence as a formal disease rate is not well defined; occurrence tracks pesticide availability and regulation. For a `Prevalence` block, use `measure_type: CASES_IN_LITERATURE` or cohort-derived figures with explicit denominators rather than a population prevalence.

---

## 10. Diagnostics

- **Primarily clinical** — recognition of the cholinergic toxidrome (DUMBELS/SLUDGE + miosis + bronchorrhea + fasciculations/weakness) plus exposure history. **Treatment must not wait for labs** ([StatPearls](https://statpearls.com/sp/al/21/30316/)).
- **Cholinesterase assays:** depressed **RBC acetylcholinesterase** and **plasma/pseudocholinesterase**. **Important caveat:** carbamylated enzyme **spontaneously reactivates (including in the sample tube)**, so ChE levels may be only transiently low or falsely normal — **less reliable than for OPs**, and a normal level does not exclude carbamate poisoning. (LOINC codes to verify: Cholinesterase in serum/plasma; Acetylcholinesterase in RBC.)
- **Differentiation from OP:** clinically similar; the distinction matters mainly for oxime decision-making and prognosis (shorter course, no aging). History of the specific product is key.
- **Supportive labs/tests:** ABG (respiratory failure/acidosis), glucose, electrolytes (hypokalemia), ECG (brady/tachyarrhythmia, QT), chest imaging (aspiration). Specific **agent confirmation** by GC-MS/LC-MS on blood/urine/gastric contents is forensic/research, not routine.
- **Genetic testing, newborn/carrier screening, CMA, karyotype, repeat-expansion, mitochondrial testing:** **all N/A.**
- **Differential diagnosis:** OP poisoning (primary), nicotine/other cholinergic agents, nerve-agent exposure, other causes of coma with miosis (opioids — but opioids lack fasciculations/bronchorrhea), status epilepticus, severe pneumonia.

---

## 11. Outcome / Prognosis

- **Generally good with prompt supportive care** — most survivors recover fully within 24–48 h with **no chronic sequelae** (contrast OP). Overall cohort mortality ~5.5% but strongly agent/formulation-dependent (carbofuran ~2% vs carbosulfan ~11%) ([PMC4950420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4950420/)).
- **Proximate cause of death:** respiratory failure (secretions, bronchospasm, muscle paralysis, central depression), aspiration; occasionally early cardiac events.
- **Prognostic factors:** specific agent and formulation strength; **GCS at presentation** (lower = worse); dose; time to atropine/airway support; development of respiratory failure requiring ventilation (14.2% in the cohort).
- **Morbidity/disability:** low long-term disability in survivors; the burden is acute mortality. QoL instruments not disease-specific.
- **Chronic effects:** the chronic neuropsychiatric/neuropathic sequelae described for OPs are largely **not** features of carbamate poisoning (uncertainty noted in §8 for rare intermediate-syndrome-like reports).

---

## 12. Treatment

**Mainstay = airway + atropine; decontamination; oximes controversial.**

- **Resuscitation/airway (NCIT:C15247 / supportive):** "aggressive airway management is of utmost importance" ([WikEM](https://wikem.org/wiki/Carbamates)); oxygen, suction of secretions, intubation/ventilation for respiratory failure (14.2% of the cohort).
- **Atropine (antimuscarinic; CHEBI:16684; NCIT:C47485 Atropine):** the specific antidote — titrated to **drying of secretions / clear chest / adequate oxygenation**, not to pupils or heart rate alone; large cumulative doses (tens–hundreds of mg) may be needed ([Eddleston protocol, PMC1065055](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1065055/)). Treatment term: `NCIT:C15986 Pharmacotherapy` + `therapeutic_agent` atropine.
- **Oximes (pralidoxime, CHEBI:8352; obidoxime):** **controversial and generally not recommended for pure carbamate poisoning.** Rationale: carbamylated AChE reactivates spontaneously and does not age, so oximes add little; and **"unconfirmed reports suggest increased toxicity of carbamates when oximes are administered"** (notably historical carbaryl animal data) ([AJEM review](https://ajemjournal.com/article/S0735-67570900059-X/fulltext); [Baygon case review](https://cme30.eu/?p=49643)). However, **when OP co-exposure cannot be excluded, pralidoxime is still given** ([WikEM](https://wikem.org/wiki/Carbamates)); meta-analyses show no clear mortality benefit of adding oxime to atropine. Curate the oxime question as a `mechanistic_hypotheses`/`discussion` with conflicting evidence.
- **Benzodiazepines (NCIT:C205 Benzodiazepine):** for seizures/agitation (diazepam/lorazepam).
- **Decontamination:** remove and bag clothing, skin wash; staff PPE (gloves/gowns) ([WikEM](https://wikem.org/wiki/Carbamates)). Activated charcoal if early and airway protected (evidence limited).
- **Pharmacogenomics / targeted / gene / cell / RNA / immunotherapy:** **N/A** (no genotype-guided therapy; no advanced therapeutics).
- **Experimental:** none established; general pesticide-poisoning trials (e.g., magnesium, lipid emulsion, alkalinization) are investigational and mostly OP-focused.
- **Adverse events:** atropine toxicity (anticholinergic delirium, hyperthermia, tachycardia) from over-dosing — a real risk, with warnings against reflexive repeat atropine without indication (Uganda audit: 38.8% of atropine given without a clear indication).

---

## 13. Prevention

**Primary prevention (the highest-impact, best-evidenced lever):**
- **Regulatory bans / restriction of the most lethal carbamates** (aldicarb, carbofuran; carbosulfan bans tracked internationally) — population-level mortality reductions demonstrated in Sri Lanka ([Lancet Glob Health 2021](https://doaj.org/article/44f3b05b293a45f1976a60d1d06b2a67); [carbosulfan ban tracker](https://www.global-agriculture.com/crop-protection/carbosulfan-ban-tracker-where-the-insecticide-is-restricted-worldwide/)).
- Safer formulations/packaging, dilution, secure storage, means-restriction for suicide prevention.
- Occupational controls: PPE, training, re-entry intervals.
- **Public health / environmental:** central/community pesticide storage; mental-health and suicide-prevention services in agricultural communities.

**Secondary/tertiary:** rapid access to care and atropine; poison-center protocols. **Immunization, genetic/carrier screening, prenatal testing, genetic counseling:** **N/A.**

---

## 14. Other Species / Natural Disease

- **Veterinary relevance is high** — carbamate toxicosis is common in companion animals (malicious baiting with aldicarb/carbofuran; accidental ingestion) and wildlife (secondary poisoning of raptors/scavengers from carbofuran-laced carcasses — a major conservation issue).
- **Species (NCBITaxon):** dog (**NCBITaxon:9615**), cat (**NCBITaxon:9685**), and many wild birds/mammals; the molecular target AChE is conserved across vertebrates and insects (the intended target).
- **Natural/veterinary disease:** confirmed canine carbofuran/chlorpyrifos poisonings ([Czech Vet Med 2003](https://vetmed.agriculturejournals.cz/pdfs/vet/2003/06/05.pdf)); **suspected intermediate syndrome** after methiocarb (dog, [Tinson 2017](https://bioweb.supagro.inrae.fr/ESTHER/paper/Tinson_2017_Aust.Vet.J_95_201)) and aldicarb (dogs/cats, São Paulo thesis). These veterinary data are **MODEL_ORGANISM** evidence and are the main source of the "carbamate intermediate syndrome" signal — treat human extrapolation as a `HUMAN_MODEL_MISMATCH`.
- **Comparative biology:** mechanism (AChE carbamylation) is identical across species; the insecticidal action on insect AChE is the same mechanism exploited therapeutically.
- **Zoonotic/transmission:** N/A (toxicological, not infectious).

---

## 15. Model Organisms

- **In vivo mammalian:** rats and mice are standard for carbamate AChE-inhibition pharmacology/toxicology, antidote (atropine/oxime) studies, and the historical carbaryl+oxime interaction data. Guinea pigs are used for anticholinesterase/antidote work (AChE profile closer to human).
- **Ex vivo / in vitro:** purified AChE (human, *Torpedo*, electric eel) for carbamylation/decarbamylation kinetics (Reiner's reactivation studies, [PMC2428035](https://pmc.ncbi.nlm.nih.gov/articles/PMC2428035); rivastigmine–AChE crystallography, [Proteopedia 1gqs](https://proteopedia.org/w/1gqs)); erythrocyte/neuronal cell assays.
- **Invertebrate / computational:** insect AChE (target of action); molecular docking/QSAR of carbamate–AChE binding (COMPUTATIONAL evidence).
- **Model value/limitations:** animal models reproduce the acute cholinergic crisis and antidote response well; **species differences in spontaneous reactivation rate and BBB penetration** limit direct quantitative translation, and the human **oxime-harm** question is incompletely resolved by models.
- **Resources:** MGI (mouse AChE), CTD (carbofuran/aldicarb/carbaryl toxicogenomics), ESTHER database (cholinesterase/carbamate enzymology).

---

## Summary of key ontology anchors for curation

| Axis | Suggested term(s) |
|---|---|
| Exposure (ECTO) | **ECTO:9000282** exposure to carbamate |
| Chemical class (CHEBI) | carbamate **CHEBI:13941**; carbofuran CHEBI:34611; aldicarb CHEBI:38511; carbaryl CHEBI:3390; acetylcholine CHEBI:15355; atropine CHEBI:16684; pralidoxime CHEBI:8352 *(verify each)* |
| Target enzyme | AChE, *ACHE* hgnc:108; activity **GO:0003990** (DECREASED); BChE *BCHE* hgnc:983 |
| Biological process (GO) | GO:0007271 cholinergic synaptic transmission; GO:0095500 ACh receptor signaling |
| Cell types (CL) | CL:0000108 cholinergic neuron; CL:0000100 motor neuron; skeletal muscle fiber |
| Anatomy (UBERON) | lung 0002048, bronchus 0002185, pupil 0001771, salivary gland 0001044, diaphragm 0001103 |
| Phenotypes (HP) | HP:0030810 Miosis; HP:0002307 Drooling; HP:0002380 Fasciculations; HP:0001324 Muscle weakness; HP:0002094 Dyspnea; HP:0001662 Bradycardia; HP:0001250 Seizure; HP:0001259 Coma; HP:0002014 Diarrhea |
| Treatment (NCIT) | NCIT:C15986 Pharmacotherapy (+ atropine, pralidoxime, benzodiazepine agents); NCIT:C15247/supportive care; mechanical ventilation |
| ICD-10 | T60.0 |

**Principal citations to fetch/verify before curation:** Eddleston et al. early-management protocol, *Crit Care* 2004 ([PMC1065055](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1065055/)); Sri Lanka carbamate cohort, *Clin Toxicol* 2016, DOI 10.1080/15563650.2016.1187735 ([PMC4950420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4950420/)); AJEM carbamate review ([ajemjournal](https://ajemjournal.com/article/S0735-67570900059-X/fulltext)); StatPearls carbamate toxicity ([statpearls](https://statpearls.com/sp/al/21/30316/)); Reiner cholinesterase reactivation ([PMC2428035](https://pmc.ncbi.nlm.nih.gov/articles/PMC2428035)); Lancet Glob Health 2021 regulation study ([DOAJ](https://doaj.org/article/44f3b05b293a45f1976a60d1d06b2a67)); Tinson 2017 veterinary intermediate syndrome ([ESTHER](https://bioweb.supagro.inrae.fr/ESTHER/paper/Tinson_2017_Aust.Vet.J_95_201)); CDC/ATSDR cholinesterase-inhibitor material ([CDC archive](https://archive.cdc.gov/www_atsdr_cdc_gov/csem/cholinesterase-inhibitors/intermediate_syndrome.html)).

**Sources:**
- [AJEM carbamate toxicology review](https://ajemjournal.com/article/S0735-67570900059-X/fulltext)
- [WikEM: Carbamates](https://wikem.org/wiki/Carbamates) / [Carbamate toxicity](https://www.wikem.org/wiki/Carbamate_toxicity)
- [StatPearls: Carbamate Toxicity](https://statpearls.com/sp/al/21/30316/)
- [Medscape: Organophosphate and Carbamate Toxicity](https://img.medscape.com/pi/iphone/medscapeapp/html/A816221-business.html)
- [Baygon (propoxur) case report overview](https://cme30.eu/?p=49643)
- [Eddleston et al., early management protocol, PMC1065055](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1065055/)
- [Sri Lanka carbamate cohort, PMC4950420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4950420/)
- [Lancet Global Health 2021, pesticide regulation](https://doaj.org/article/44f3b05b293a45f1976a60d1d06b2a67)
- [Influence of pesticide regulation on poisoning deaths, Sri Lanka](https://archive.cmb.ac.lk/items/14377362-2b71-4b8c-bc10-9429a4b915f0)
- [Reiner, cholinesterase reactivation, PMC2428035](https://pmc.ncbi.nlm.nih.gov/articles/PMC2428035)
- [USPTO patent text on AChE aging](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11492340)
- [Pesticide toxicology study guide](https://open-exam-prep.com/study-guides/ct-pesticide-applicator/toxicology-health-ppe/organophosphates-cholinesterase)
- [Proteopedia: rivastigmine–AChE (1gqs)](https://proteopedia.org/w/1gqs)
- [NLM MeSH: Carbofuran D002235](https://meshb.nlm.nih.gov/record/ui?ui=D002235) / [CISMeF](https://www.cismef.org/page/detail/en/MSH_D_002235)
- [AAPC ICD-10 T60.0](https://www.aapc.com/codes/icd-10-codes/T60.0) / [gesund.bund.de T60](https://gesund.bund.de/en/icd-code-search/t60)
- [Tinson 2017, suspected intermediate syndrome, dog (ESTHER)](https://bioweb.supagro.inrae.fr/ESTHER/paper/Tinson_2017_Aust.Vet.J_95_201)
- [Czech Vet Med 2003, canine carbofuran](https://vetmed.agriculturejournals.cz/pdfs/vet/2003/06/05.pdf)
- [CDC/ATSDR: Intermediate Syndrome](https://archive.cdc.gov/www_atsdr_cdc_gov/csem/cholinesterase-inhibitors/intermediate_syndrome.html)
- [Carbosulfan ban tracker](https://www.global-agriculture.com/crop-protection/carbosulfan-ban-tracker-where-the-insecticide-is-restricted-worldwide/)

*(One note for the curation queue: the worktree is named `ache-module`, and this disease is a clean conformer for an acetylcholinesterase-inhibition mechanism module shared with organophosphate poisoning — the branch-point in §6 step 7 is exactly the OP-vs-carbamate divergence such a module should encode.)*

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005605` (GO_0005605) (1 mention) - replaced by `GO:0005604`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0009926` (1 mention) - the report calls it "Increased lacrimation / Epiphora"; HP calls it **Epiphora**, and lists "Increased lacrimation" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `LOINC`.

52 of 55 terms resolved to a current term; the rest could not be looked up either way.