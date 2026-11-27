---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T18:23:05.625905'
end_time: '2026-11-26T18:31:20.594379'
duration_seconds: 494.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hepatic Tuberculosis
  mondo_id: MONDO:0005787
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: tuberculosis of liver
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
  web_search_requests: 16
  num_turns: 1
  total_cost_usd: 1.5891448700000002
  session_id: 48b1cd6c-e2ed-468b-b0f7-0c1823b15c88
  stop_reason: end_turn
  tool_calls: 62
  retrieval_calls: 62
  assistant_text_blocks: 6
citation_count: 33
reference_validation:
  total_references: 48
  verified: 48
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 9
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:25943103
  - PMID:26499189
  relevance_assessed: 48
  on_topic: 28
  off_topic: 1
  off_topic_references:
  - PMID:17553562
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 12
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 12
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - EXT_ID
  service_unreachable: 11
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hepatic Tuberculosis
- **MONDO ID:** MONDO:0005787 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** tuberculosis of liver
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hepatic Tuberculosis** covering all of the
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

Let me try PubMed E-utilities directly for abstracts.

Still researching: I'm pulling abstracts for the key hepatic TB case series, plus genetics, model-organism and treatment sources.

I've started a background lookup for abstracts of about ten hepatic TB case series and several supporting papers. While it runs, I'm checking the MONDO identifier and pharmacogenomics sources.

Waiting on the background abstract lookup. When it returns I'll write the full report.

## Part 1: PMID abstracts (Europe PMC)

Quotes are capped at 125 characters because these are non-preapproved sources, so each entry has short verbatim fragments. Anything outside quotation marks is paraphrase.

**1. PMID 7744492.** "Hepatic tuberculosis: comparison of miliary and local form." Chien RN, Lin PY, Liaw YF. *Infection*, 1995, 23(1):5-8. Cited 35 times.
- "Five patients had no evidence of extrahepatic tuberculosis (local form), and 17 had the miliary form." (22 patients in total.)
- "granuloma, caseation, acid-fast bacilli, fatty change and portal fibrosis as the main findings" (histology, both forms)

**2. PMID 3659266.** "A prospective study of hepatic tuberculosis in 41 black patients." Maharaj B, Leary WP, Pudifin DJ. *Q J Med*, 1987, 63(242):517-522. Cited 29 times.
- "Acid-fast bacilli, caseation and coexistent liver disease were detected in 59, 51 and 37 per cent of patients respectively." (AFB 59%, caseation 51%, coexistent liver disease 37%.)
- Paraphrase: abdominal symptoms were absent in 54%, weight loss in 39%, pyrexia in 37%, and anaemia in 27%. Splenomegaly was absent in 68%.
- "Twenty-two per cent of chest radiographs were normal."

**3. PMID 14600128.** "The nodular form of hepatic tuberculosis: a review with five additional new cases." Huang WT, Wang CC, Chen WJ, Cheng YF, Eng HL. *J Clin Pathol*, 2003, 56(11):835-839. Cited 37 times.
- "All of them were positive for M tuberculosis by PCR analysis of the liver tissue." (5/5 PCR-positive.)
- Paraphrase: all five were preoperatively thought to have a malignant liver lesion, and histology showed chronic granulomatous inflammation.

**4. PMID 24179582.** "Diagnosis and treatment of hepatic tuberculosis: report of five cases and review of literature." Wu Z, Wang WL, Zhu Y, et al. *Int J Clin Exp Med*, 2013, 6(9):845-850. Cited 41 times.
- "Image examination associated with image-guided fine needle aspiration biopsy is the best diagnostic method."
- "The renal post-transplantation patient with hepatic tuberculosis eventually died of multiple organ failure (MODS)."
- Paraphrase: 3 of 5 were confirmed by needle biopsy, and the other 4 had no recurrence over 48-120 months.

**5. PMID 29759945.** "Diagnosis of local hepatic tuberculosis through next-generation sequencing: Smarter, faster and better." Ai JW, Li Y, Cheng Q, et al. *Clin Res Hepatol Gastroenterol*, 2018, 42(3):178-181. Cited 34 times. Single case.
- "We identified a total of 299 sequencing reads of Mycobacterium tuberculosis" (from liver tissue, by NGS).
- "No specific Mycobacterial tuberculosis nucleotide sequence was detected in the sample of peripheral blood."
- "repeated Ziehl-Neelsen staining of the liver tissue finally identified small numbers of positive bacillus."

**6. PMID 15162540.** "Imaging diagnosis of 12 patients with hepatic tuberculosis." Yu RS, Zhang SZ, Wu JJ, Li RF. *World J Gastroenterol*, 2004, 10(11):1639-1642. Cited 74 times.
- "Parenchymal type was found in 10 cases" (of 12 CT cases).
- "Enhanced MR in 3 cases was slightly shown peripheral enhancement or with multilocular enhancement."
- "typical CT and MR findings can suggest the diagnosis." (Conclusion.)

**7. PMID 28148232.** "Hepatic tuberculosis in human immunodeficiency virus co-infected adults: a case series of South African adults." Gounder L, Moodley P, Drain PK, Hickey AJ, Moosa MS. *BMC Infect Dis*, 2017, 17:115. Cited 5 times.
- "The most frequent clinical finding was hepatomegaly (85%)."
- "Acid-fast bacilli were cultured from liver tissue in 30% (6/20) of patients; 25% (5/20) identified as TB."
- Paraphrase: 20 histology-confirmed cases, median CD4 47 cells/µl, 75% with pre-existing pulmonary TB, and six deaths within one year.

**8. PMID 2157746.** "The nodular form of local hepatic tuberculosis. A review." Oliva A, Duarte B, Jonasson O, Nadimpalli V. *J Clin Gastroenterol*, 1990, 12(2):166-173. Cited 38 times.
- "Since 1950, 21 cases of isolated tuberculoma or tuberculous abscess of the liver have been reported in the world literature."
- Paraphrase: the authors add two cases. Laparotomy was needed in 19 of the 23 cases, and the diagnosis was usually unsuspected.

**9. PMID 10398910.** "Isolated hepatic tuberculosis: report of five cases and review of the literature." Kok KY, Yapp SK. *J Hepatobiliary Pancreat Surg*, 1999, 6(2):195-198. Cited 39 times.
- "It usually presents as a protracted illness frequently associated with jaundice and hepatomegaly."
- "We report five cases of isolated hepatic tuberculosis" (no frequency data in the abstract).

**10. PMID 16531964.** "Hepatic tuberculosis in absence of disseminated abdominal tuberculosis." Desai CS, Josh AG, Abraham P, et al. *Ann Hepatol*, 2006, 5(1):41-43. Cited 17 times.
- "Retrospective analysis of seven cases of hepatic tuberculosis without miliary abdominal tuberculosis"
- "Complete resolution of liver lesions on treatment with 4-drug anti-tuberculosis drug chemotherapy was seen."
- Paraphrase: all seven had fever and hepatomegaly, five had upper abdominal pain and vomiting, and mean ESR was 65. Mean LDH was 794 IU/L and mean albumin 2.4 g%.

## Part 2: Europe PMC searches (sort=CITED desc, pageSize=3)

**a) TYK2 / tuberculosis / P1104A.** 5 hits.
- Best hit: **PMID 30578352.** "Tuberculosis and impaired IL-23-dependent IFN-γ immunity in humans homozygous for a common TYK2 missense variant." Boisson-Dupuis S et al. *Sci Immunol*, 2018. Cited 185 times.
  - "We show that homozygosity for the common TYK2 P1104A allele, which is found in about 1/600 Europeans"
  - "is more frequent in a cohort of patients with tuberculosis from endemic areas than in ethnicity-adjusted controls"
- Hit 2: **PMID 31068474.** "Homozygosity for TYK2 P1104A underlies tuberculosis in about 1% of patients in a cohort of European ancestry." Kerner G et al. *PNAS*, 2019 (year taken from the extracted summary). Cited 9 times per the summary. Hit 2 is a PNAS study and was not part of the verbatim text.
- Hit 3 was cut off in the verbatim text. The extracted summary named a 2024 paper (PMID 38337161), but I could not verify that, so I have not reported it.

**b) Zebrafish / granuloma / M. marinum.** 10 hits.
- Best hit: **PMID 12479816.** "Real-time visualization of mycobacterium-macrophage interactions leading to initiation of granuloma formation in zebrafish embryos." Davis JM et al. *Immunity*, 2002. Cited 423 times.
  - "Here, we exploit the optical transparency of zebrafish embryos to image the events of M. marinum infection in vivo."
  - "Thus, Mycobacterium-macrophage interactions can initiate granuloma formation solely in the context of innate immunity."
- Other hits: PMID 17553562 (Meijer AH et al., *Dev Comp Immunol*, 2008, cited 120 times) and PMID 21372049 (Stoop EJ et al., *Dis Model Mech*, 2011, cited 93 times).

**c) Bovine tuberculosis / liver.** 4 hits.
- Best hit: **PMID 31012527.** "Liver fluke (Fasciola hepatica) co-infection with bovine tuberculosis in cattle: A prospective herd-level assessment of herd bTB risk in dairy enterprises." Byrne AW et al. *Transbound Emerg Dis*, 2019. Cited 8 times.
  - "Models predicting bTB risk were not improved with the inclusion of liver fluke exposure levels."
- These hits are about liver fluke co-infection in cattle, not liver involvement by bovine TB. The other hits are PMID 30484969 (Byrne AW et al., 2019, cited 6 times) and a 2017 Edinburgh thesis (Kelly RF, no PMID).

**d) Tuberculosis / liver transplant / review.** 21 hits.
- Best hit: **PMID 19642133.** "Tuberculosis in liver transplant recipients: a systematic review and meta-analysis of individual patient data." Holty JE et al. *Liver Transpl*, 2009. Cited 96 times.
  - "The short-term mortality rate was 31%."
  - "The prevalence of active MTB infection in transplant recipients was 1.3%."
- Hit 2: PMID 21384513 (Jafri SM et al., *Liver Transpl*, 2011, cited 47 times). Hit 3: PMID 10917220 (Verma A et al., *Pediatr Infect Dis J*, 2000, cited 18 times).

**e) Rifapentine / four-month / tuberculosis.** 4 hits.
- Best hit: **PMID 33951360.** "Four-Month Rifapentine Regimens with or without Moxifloxacin for Tuberculosis." Dorman SE et al. *N Engl J Med*, 2021, 384(18):1705-1718. Cited 456 times.
  - "The primary efficacy outcome was survival free of tuberculosis at 12 months."
  - "Rifapentine with moxifloxacin was noninferior to the control in the microbiologically eligible population"
- Hit 2: PMID 38634108 (Louie JK et al., *Open Forum Infect Dis*, 2024, cited 17 times). Hit 3: PMID 35294823 (Phillips PPJ et al., *N Engl J Med*, 2022, a letter with 0 citations).

**f) Tuberculous liver abscess.** 50 hits.
- Best hit: **PMID 21535224.** "Endoscopic ultrasonography-guided drainage for tuberculous liver abscess drainage." Itoi T et al. *Dig Endosc*, 2011. Cited 33 times. Single case report.
  - "Four weeks later, we found that cultured microorganism obtained using drainage catheter was Mycobacterium tuberculosis."
- Hit 2: PMID 6464195 (Spiegel CT, Tuazon CU, *Tubercle*, 1984, cited 26 times). Hit 3: PMID 10064416 (Jain R et al., *J Clin Ultrasound*, 1999, cited 26 times).

**g) VDR / tuberculosis / meta-analysis.** 5 hits.
- Best hit: **PMID 31649297.** "Association of Fok1 VDR polymorphism with Vitamin D and its associated molecules in pulmonary tuberculosis patients and their household contacts." Panda S et al. *Sci Rep*, 2019. Cited 26 times. This is a primary case-control study, not a meta-analysis.
  - "'f' allele was associated with increased susceptibility to TB."
- The meta-analysis is hit 2: **PMID 33901685.** "FokI polymorphism of the vitamin D receptor (VDR) gene and susceptibility to tuberculosis: Evidence through a meta-analysis." Yadav U et al. *Infect Genet Evol*, 2021. Cited 11 times.
  - "No statistically significant association was observed in the allele contrast model"
  - Its conclusion reports a significant association in the overall analysis and in the Asian subgroup.

**h) BCG / protection / meta-analysis / tuberculosis.** 1 hit.
- **PMID: none.** This is a preprint, Research Square (DOI 10.21203/rs.3.rs-97073/v1, PPR231548). "BCG vaccination provides protection against COVID 19: A Systematic review and meta-analysis." Khera D et al., 2020. Cited 0 times.
  - "From our results we can say that BCG vaccination causes a decrease in COVID-19 incidence and mortality."
- The hit is about COVID-19, not tuberculosis. No tuberculosis-protection meta-analysis matched the query.

## URLs read

- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7744492%20AND%20SRC:MED&resultType=core&format=json (the first attempt timed out, and the retry succeeded)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:3659266%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14600128%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24179582%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29759945%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15162540%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:28148232%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:2157746%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10398910%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16531964%20AND%20SRC:MED&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22TYK2%22%20AND%20TITLE%3A%22tuberculosis%22%20AND%20(P1104A%20OR%20homozygosity)&resultType=core&pageSize=3&sort=CITED%20desc&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22zebrafish%22%20AND%20TITLE%3A%22granuloma%22%20AND%20%22Mycobacterium%20marinum%22&resultType=core&pageSize=3&sort=CITED%20desc&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22bovine%20tuberculosis%22%20AND%20TITLE%3A%22liver%22&resultType=core&pageSize=3&sort=CITED%20desc&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22tuberculosis%22%20AND%20TITLE%3A%22liver%20transplant%22%20AND%20review&resultType=core&pageSize=3&sort=CITED%20desc&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22rifapentine%22%20AND%20TITLE%3A%22four-month%22%20AND%20tuberculosis&resultType=core&pageSize=3&sort=CITED%20desc&format=json (read in full, including a second read at offset 39786)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22tuberculous%20liver%20abscess%22&resultType=core&pageSize=3&sort=CITED%20desc&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22VDR%22%20AND%20TITLE%3A%22tuberculosis%22%20AND%20meta-analysis&resultType=core&pageSize=3&sort=CITED%20desc&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22BCG%22%20AND%20TITLE%3A%22protection%22%20AND%20TITLE%3A%22meta-analysis%22%20AND%20tuberculosis&resultType=core&pageSize=3&sort=CITED%20desc&format=json

# Hepatic Tuberculosis (MONDO:0005787): Disease Characteristics Report

**How I read the request:** Hepatic tuberculosis is an infectious disease. It is caused by *Mycobacterium tuberculosis* (and occasionally other members of the *M. tuberculosis* complex). **It has no causal human gene and no OMIM disease entry.** The template sections on Mendelian genetics therefore cover host *susceptibility* genes only, or are marked not applicable.

**About ontology identifiers:** Under this run's sourcing rules I can only give IDs I actually retrieved. Those are MONDO:0005787, DOID:407 (the parent, gastrointestinal tuberculosis), the ICD codes, the MeSH heading and SNOMED CT 186273003. HPO, GO, CL, UBERON, ChEBI, NCIT and NCBI Taxon terms are given **as labels only**. Map them to IDs in a separate curation step.

**Access limits:** PubMed and some PMC pages could not be fetched directly in this session. Abstracts were retrieved through Europe PMC and publisher pages instead. Quotes from abstracts are kept short.

---

## 1. Disease Information

**Overview.** Mondo defines hepatic TB as "infection of the liver with species of mycobacterium" (most often *M. tuberculosis*), "characterized by localized small tuberculous miliary lesions or tumor-like mass (tuberculoma)" with abnormal liver function tests (Mondo record via [SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0005787/)).

There are two forms:
- **Miliary (disseminated):** part of generalized haematogenous TB. This is about 79% of reported cases.
- **Local (isolated):** about 21% of reported cases. It includes nodular tuberculoma or abscess and the tubular/ductal (cholangitic) form.

Rolleston and McNee first described this miliary/local split in 1905 (Hickey et al. 2015, PMID 25943103, [PMC4425874](https://pmc.ncbi.nlm.nih.gov/articles/PMC4425874/)). Hepatic TB accounts for under 1% of all TB infections and is "likely underreported" (PMID 25943103).

**Identifiers**

| System | Identifier |
|---|---|
| MONDO | MONDO:0005787. Cross-referenced to DOID:407, gastrointestinal tuberculosis ([MGI DOID:407](https://www.informatics.jax.org/disease/DOID:407)) |
| MeSH | "Tuberculosis, Hepatic" ([MeSH tuberculosis tree](https://meshb.nlm.nih.gov/record/ui?ui=D014386)) |
| SNOMED CT | 186273003 "Tuberculosis of liver (disorder)" ([ART-DECOR](https://art-decor.org/terminology/snomed/viewConcept/186273003)) |
| ICD-10 (WHO) | A18.8 "Tuberculosis of other specified organs" with K77.0* "Liver disorders in infectious and parasitic diseases classified elsewhere" (dagger-asterisk pair) ([NHS ICD-10 browser](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-a15-a19.htm)) |
| ICD-10-CM (US) | A18.83 "Tuberculosis of digestive tract organs, NEC", with the K77 note ([AAPC](https://aapc.com/codes/icd-10-codes/A18.83)) |
| ICD-11 | Not retrieved |
| OMIM / Orphanet | None. This is an infectious disease, not a Mendelian disorder, and no Orphanet entry was found. |

**Synonyms:** tuberculosis of liver; hepatic TB; tuberculous hepatitis (Essop 1984 title); hepatobiliary tuberculosis (broader term); primary or isolated or local hepatic TB; hepatic tuberculoma; tuberculous liver abscess; nodular or macronodular hepatic TB.

**Evidence base:** The data come almost entirely from aggregated case series and case reports, which are individual-patient clinical data. Hickey 2015 pooled 618 patients from 14 series (1960–2013). There are no registries or EHR-scale studies.

---

## 2. Etiology

**Cause.** The cause is infection of the liver by *M. tuberculosis*. Most cases arise from haematogenous dissemination: "Approximately 79% of all reported hepatic TB cases were due to systemic dissemination of bacilli" (PMID 25943103). Local disease is thought to follow portal-venous spread from a gut focus. This is a mechanistic inference repeated in reviews (Chaudhary 2014, PMID 24976240, [PMC4073015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4073015/)).

**Risk factors (human clinical evidence)**
- **HIV and severe immunosuppression:**
  - Hepatic involvement occurred in 17.4% of HIV-infected vs 4.3% of HIV-uninfected people with disseminated TB (summarised in PMID 25943103).
  - A South African series of 20 HIV-positive adults with hepatic TB had a median CD4 count of 47 cells/µL. In that series "hepatic TB occurred in patients with severe immunosuppression" (Gounder 2017, PMID 28148232).
  - "Hepatic TB has become more prevalent, likely as a result of the… HIV/AIDS epidemic" (PMID 25943103).
- **Solid-organ transplantation:**
  - The prevalence of active TB in liver-transplant recipients was 1.3% (Holty 2009, PMID 19642133).
  - Hepatic TB after renal transplant has ended in fatal multi-organ failure (Wu 2013, PMID 24179582).
  - Isolated hepatic TB has been reported in a transplanted liver (PMID 15522111).
- **Population-level drivers of TB in general (WHO Global TB Report 2024, 2023 data):** estimated attributable incident TB cases were undernutrition 0.96 M, alcohol use disorders 0.75 M, smoking 0.70 M, HIV 0.61 M and diabetes 0.38 M ([WHO GTB 2024](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024)). These figures apply to TB overall, not specifically to hepatic TB.
- **Co-existing liver disease:** found in 37% of patients in one prospective series (Maharaj 1987, PMID 3659266).

**Host genetic susceptibility (TB in general; nothing hepatic-specific was found)**
- **Mendelian susceptibility to mycobacterial disease (MSMD):** "caused by inborn errors of IFN-γ immunity" (Rosain/Bustamante 2018, PMID 30264912). The genes involved include *IL12RB1*, *IL12B*, *IFNGR1/2*, *STAT1*, *TYK2*, *ISG15* and *SPPL2A*, among others.
- **TYK2 P1104A homozygosity:**
  - This common allele "found in about 1/600 Europeans" impairs IL-23-dependent IFN-γ immunity and is enriched in TB patients (Boisson-Dupuis 2018, PMID 30578352).
  - In the UK Biobank, 6 of 620 TB patients (1%) were homozygous vs 0.2% of controls, an odds ratio of about 5.0 (95% CI 1.96–10.31) (Kerner 2019, PMID 31068474).
  - Penetrance is incomplete.
- **VDR FokI polymorphism:** a meta-analysis reported an association overall and in Asian subgroups, but not in the allele-contrast model (Yadav 2021, PMID 33901685). Evidence is modest.

**Protective factors:**
- Treating HIV with antiretroviral therapy (ART) to restore immunity.
- Avoiding immunosuppression where possible.
- TB preventive therapy (see §13).

No hepatic-specific protective variants have been reported. No BCG meta-analysis for hepatic TB was retrieved; the only hit was an irrelevant COVID-19 preprint.

**Gene–environment interactions:** Host IFN-γ/IL-12/IL-23 pathway defects matter only when there is exposure to mycobacteria. NAT2 acetylator genotype interacts with isoniazid to cause drug-induced liver injury (see §12). No hepatic-TB-specific interaction data were found.

---

## 3. Phenotypes

The table pools data from the systematic review (PMID 25943103; medians across series) and individual series.

| Phenotype | Type | Frequency | Suggested HPO label |
|---|---|---|---|
| Hepatomegaly | sign | median 80% (10–100); 85% in HIV+ (PMID 28148232); 70–96% (PMID 24976240) | Hepatomegaly |
| Fever | symptom/sign | median 67% (30–100) | Fever |
| Respiratory symptoms | symptom | median 66% (32–78); 74% (Essop 1984) | Cough / Dyspnea |
| Abdominal pain (RUQ) | symptom | median 59.5% (40–83); 65–87% (PMID 24976240) | Abdominal pain / Right upper quadrant pain |
| Weight loss | symptom | median 57.5% (20–100) | Weight loss |
| Splenomegaly | sign | median 30% (0–40); 25–55% | Splenomegaly |
| Ascites | sign | median 23% (5–25) | Ascites |
| Jaundice | sign | median 20% (0–60); 20–35% | Jaundice |
| Liver tenderness | sign | 36% (PMID 24976240) | Hepatic tenderness (curator to confirm term) |
| Raised ALP and GGT | lab | most common lab abnormality; ALP about 200–750 U/L, GGT about 100–400 U/L (PMID 25943103) | Elevated circulating alkaline phosphatase concentration; Elevated gamma-glutamyltransferase level |
| Raised transaminases | lab | 78% (Essop 1984) | Elevated hepatic transaminase |
| Hyperbilirubinemia | lab | mild, both forms | Hyperbilirubinemia |
| Hypoalbuminemia | lab | mean albumin 2.4 g/dL (Desai 2006, PMID 16531964) | Hypoalbuminemia |
| Raised ESR | lab | mean 65 mm/h (PMID 16531964) | Elevated erythrocyte sedimentation rate |
| Anemia | lab | 27% (PMID 3659266) | Anemia |
| Hepatic calcification | imaging | 49% (58/119) on plain film in one series (PMID 25943103) | Hepatic calcification |
| Obstructive jaundice / biliary stricture | sign | rare; can mimic Klatskin tumour (PMID 3421231; PMID 18723964) | Cholestasis |
| Fever of unknown origin | presentation | case-level (PMID 17293928) | Fever of unknown origin |

- **Onset:** mainly in adults, with a subacute to chronic, insidious course. Kok 1999 describes it as "usually presents as a protracted illness frequently associated with jaundice and hepatomegaly" (PMID 10398910).
- **Severity:** varies, and is severe in disseminated or HIV-associated disease.
- **Comparison of forms:** miliary and local forms had similar clinical and pathological features (Chien 1995, PMID 7744492).
- **Quality of life:** no EQ-5D, SF-36 or disease-specific quality-of-life data were found for hepatic TB.

---

## 4. Genetic / Molecular Information

- **Causal genes, pathogenic variants, allele frequencies, somatic origin, chromosomal abnormalities, epigenetics:** not applicable. The disease is infectious.
- **Host susceptibility genes:** see §2 (MSMD genes; *TYK2* P1104A, a germline missense variant that causes partial loss of IL-23 signalling).
- **Pharmacogenetic modifier:** *NAT2*. "Genetic variants of NAT2 gene have significant role in isoniazid induced hepatotoxicity" (Khan 2019 meta-analysis, PMID 30509962).
- **Pathogen genetics:** next-generation sequencing of liver tissue found 299 *M. tuberculosis* reads in local hepatic TB, with none in blood (Ai 2018, PMID 29759945).

---

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* (NCBI Taxonomy label "Mycobacterium tuberculosis"; *M. tuberculosis* complex). It is airborne and spreads person to person.
- **Lifestyle and environmental factors:** undernutrition, alcohol use disorder, smoking and diabetes are the leading attributable drivers of TB in general (WHO 2024; figures in §2).
- **Other exposures:** no CTD or toxicant data are specific to hepatic TB.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain**

1. Inhaled *M. tuberculosis* infects alveolar macrophages. This leads to a primary pulmonary focus and bacteraemia (established TB biology; not retrieved in this session for the liver specifically).
2. **Branch A (miliary, about 79%):** haematogenous dissemination through the hepatic artery leads to bacilli reaching the liver sinusoids (PMID 25943103).
   **Branch B (local):** portal-venous seeding from a gut or abdominal focus leads to focal disease. This route is *inferred* in reviews (PMID 24976240).
3. **Kupffer cell capture (demonstrated in mice with BCG):** "Kupffer cells directly capture blood-borne bacteria and subsequently nucleate formation of a nascent granuloma" (Egen 2008, PMID 18261937).
4. Growth is restricted to professional phagocytes. This results in a low bacillary burden: "Among sites of extrapulmonary growth of Mycobacterium tuberculosis, the liver is the least infected," which the authors attribute to "complete restriction of mycobacterial growth to liver macrophages" (Seiler 2001, PMID 11705978, mouse). This may explain why acid-fast bacilli (AFB) are rarely seen in human liver tissue, though that link is an inference.
5. Recruited monocytes and macrophages, together with effector T cells (IL-12/IL-23 → IFN-γ axis), lead to an organised epithelioid granuloma with Langhans giant cells.
   - TNF signalling maintains the granuloma structure (PMID 18261937).
   - Inborn errors of this axis predispose to disseminated disease (PMID 30264912; PMID 30578352).
   - Innate macrophage–mycobacterium interactions alone can *initiate* granulomas (zebrafish/*M. marinum*, Davis 2002, PMID 12479816).
6. Central caseous necrosis develops, and granulomas coalesce. This results in macronodules (tuberculoma, 1–4 cm) or tuberculous abscess.
   - In the ductal form, caseous material erodes into bile ducts, causing cholangitis and stricture. This step is inferred from imaging and case reports (PMID 26499189; PMID 3421231).
7. The consequences then branch:
   - Diffuse granulomatous infiltration leads to hepatomegaly and a cholestatic enzyme pattern (disproportionately high ALP).
   - Biliary or hilar node compression leads to obstructive jaundice.
   - Healed lesions lead to calcification.
   - Rarely, portal vein thrombosis leads to portal hypertension (PMID 16026440).
8. Severe immunosuppression (HIV) results in poorly formed granulomas, greater dissemination and high mortality (PMID 28148232; this mechanism is inferred).

**Checklist summary**
- **Pathways:** IL-12/IFN-γ; IL-23/TYK2; TNF signalling.
- **Suggested GO process labels:** granuloma formation; macrophage activation; response to interferon-gamma; tumor necrosis factor-mediated signaling pathway; phagocytosis.
- **Suggested CL labels:** Kupffer cell; macrophage; epithelioid cell; multinucleate giant cell (Langhans); T cell (CD4-positive, alpha-beta); monocyte; hepatocyte (bystander).
- **Tissue damage:** caseous necrosis, fibrosis, fatty change and portal fibrosis (PMID 7744492).
- **Omics:** no hepatic-TB transcriptomic, proteomic, single-cell or CRISPR-screen data were found.

---

## 7. Anatomical Structures Affected

- **Primary organ:** liver (UBERON label "liver"). Within the liver: the hepatic sinusoids and parenchyma (Yu 2004 found the parenchymal type in 10 of 12 cases, PMID 15162540), and the biliary tree ("intrahepatic bile duct").
- **Other sites:** hilar or porta hepatis lymph nodes, spleen, peritoneum (ascites), lung (concomitant disease in about 66–75%), and portal vein.
- **Systems:** digestive (hepatobiliary), respiratory, immune.
- **Subcellular level:** bacilli sit in macrophage phagosomes. Suggested GO cellular component label: "phagocytic vesicle".
- **Laterality:** not applicable. Distribution is diffuse (miliary) or focal (often the right lobe in case reports; not quantified).

---

## 8. Temporal Development

- **Onset:** adults; subacute or insidious. Diagnosis was suspected clinically in only 47% of cases (Essop 1984).
- **Course:** progressive if untreated. Lesions resolve with therapy: "Complete resolution of liver lesions on treatment with 4-drug anti-tuberculosis drug chemotherapy" (Desai 2006, PMID 16531964). There was no recurrence over 48–120 months in 4 of 5 patients (PMID 24179582).
- **Staging:** there is no formal staging system and "no standard classification system" (Kakkar 2015, PMID 26499189). Morphologic patterns are miliary, macronodular/tuberculoma, abscess, serohepatic and tubular/cholangitic.
- **Remission:** treatment-induced only. Spontaneous remission was not documented.

---

## 9. Inheritance and Population

- **Inheritance:** not applicable, because the disease is infectious. Rare host-susceptibility conditions in the MSMD group are mostly autosomal recessive or dominant with incomplete penetrance (PMID 30264912).
- **Frequency within TB:**
  - Hepatic TB was found in 1.2% (96/8,342) of active-TB inpatients in a South African hospital, 1978–1984 (Essop 1984, Q J Med 53:465; summarised in PMID 25943103).
  - Liver TB histology was found in 37.3% of HIV/TB deaths in a Nigerian autopsy series (PMID 25943103).
  - True incidence "remains unknown".
- **Background TB burden (WHO 2024, 2023 data):**
  - 10.8 million incident cases (95% UI 10.1–11.7 M), or 134 per 100,000.
  - 1.25 million deaths.
  - 6.1% of cases in people living with HIV.
  - 30 countries carry 87% of the burden ([WHO GTB 2024](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024); [CIDRAP](https://www.cidrap.umn.edu/tuberculosis/who-report-shows-global-tuberculosis-cases-are-rising)).
  - WHO notes the 2024 estimates have been superseded by the 2025 report.
- **Geography:** cases are reported from endemic regions, including South Africa, India, the Philippines and East Asia (PMID 25943103).
- **Sex ratio and age distribution:** not available in the retrieved abstracts.

---

## 10. Diagnostics

**Laboratory:**
- The pattern is cholestatic: ALP and GGT are raised more than transaminases. A disproportionately raised ALP suggests infiltration (PMID 24976240).
- ESR is raised; albumin may be low.

**Histopathology** (the most specific test):
- Caseating granulomas: median sensitivity 68% (PMID 25943103); 51% in Maharaj 1987; 83% in Essop 1984.
- Epithelioid granulomas: 80–100% (PMID 24976240).
- Liver biopsy was "the most useful aid to correct diagnosis" (Essop 1984).

**Microbiology:**
- AFB smear: median sensitivity 25% (0–59). Maharaj 1987 found AFB in 59%.
- Liver-tissue culture: 30% (6/20) in HIV-positive patients (PMID 28148232).
- PCR on liver tissue: median sensitivity 86% (30–100) (PMID 25943103). PCR was positive in 5 of 5 nodular cases (Huang 2003, PMID 14600128).
- Metagenomic NGS: shown in a single case (PMID 29759945).

**Imaging:**
- Abnormality rates: ultrasound 76%, CT 88%, chest radiograph 42.5% (medians, PMID 25943103).
- CT is the most sensitive modality. Lesions appear as hypodense nodules with rim enhancement and a "cluster" sign (PMID 8419431).
- Biopsy combined with nucleic acid testing is the most specific approach (PMID 25943103).
- Image-guided fine-needle aspiration is "the best diagnostic method" (PMID 24179582).
- FDG-PET can show a hepatic "superscan" (PMID 24347039).
- Local hepatic TB often mimics cancer, including hepatocellular carcinoma (HCC) and cholangiocarcinoma (PMID 33031307; 26236700; 34687434). All 5 nodular cases in Huang 2003 were first thought to be malignant.

**Differential diagnosis:**
- Sarcoidosis and other granulomatous hepatitis (drug-induced, fungal, brucellosis, Q fever, PBC).
- HCC, cholangiocarcinoma or Klatskin tumour, and metastases.
- Pyogenic or amoebic abscess.
- Lymphoma.

**Genetic and omics testing:** not applicable to diagnosis. Consider MSMD gene panel or exome testing for unusually severe or familial disseminated mycobacterial disease (PMID 30264912).

**Screening:** no hepatic-specific screening exists. Standard TB/LTBI screening is used, for example in transplant candidates.

---

## 11. Outcome / Prognosis

- **Mortality:**
  - HIV-uninfected patients: case fatality 12–42% (PMID 25943103).
  - Untreated patients: 95% (35/37) died in one series.
  - HIV-positive patients: 30% (6/20) died within one year, and "the 12-month mortality remained high" (PMID 28148232).
  - Liver-transplant recipients with TB: short-term mortality 31% (PMID 19642133).
- **Prognostic factors:** HIV and immunosuppression, delayed diagnosis, and regimens without rifampicin (Essop: 0% mortality with rifampicin vs 17–50% without; PMID 24976240). Miliary and local forms have similar presentations (PMID 7744492).
- **Complications:** obstructive jaundice, portal hypertension or portal vein thrombosis, abscess rupture, multi-organ failure, and drug-induced liver injury.
- **Recovery:** good with therapy in drug-susceptible disease. Standard 4-drug therapy for 6–12 months gave "positive outcomes" in nearly all drug-susceptible patients (PMID 25943103).
- **Quality of life and disability data:** none found.

---

## 12. Treatment

**First-line drugs** (suggested NCIT labels: Isoniazid, Rifampin, Pyrazinamide, Ethambutol; ChEBI labels likewise):
- Intensive phase: isoniazid, rifampicin, pyrazinamide and ethambutol. Typical doses are 5, 10, 30 and 20 mg/kg/day for 2 months.
- Continuation phase: isoniazid and rifampicin, totalling 6–12 months (PMID 24976240; PMID 25943103).

**Short regimen:**
- WHO conditionally recommends 2HPMZ/2HPM (rifapentine, isoniazid, moxifloxacin, pyrazinamide) for people aged 12 and over. The recommendation "also applies to extrapulmonary TB – except TB of the central nervous system, bone or joint" ([WHO Module 4](https://www.ncbi.nlm.nih.gov/books/NBK613096/)).
- The supporting trial is Dorman 2021, NEJM, PMID 33951360: "Rifapentine with moxifloxacin was noninferior to the control."
- The operational handbook may exclude disseminated or abdominal TB, so check the handbook before applying this regimen to hepatic TB.

**Interventional:**
- Abscesses: percutaneous or EUS-guided drainage (Itoi 2011, PMID 21535224).
- Obstructive jaundice: biliary decompression (endoscopic stenting).
- Uncertain masses: surgical resection or laparotomy. Laparotomy was needed in 19 of 23 nodular cases historically (Oliva 1990, PMID 2157746).

**Adverse effects:** drug-induced liver injury is the main concern and is especially hard to separate from hepatic TB itself. The ATS statement gives a monitoring and rechallenge framework (Saukkonen 2006, PMID 17021358).

**Pharmacogenomics:**
- NAT2 slow acetylators have higher isoniazid hepatotoxicity risk (PMID 30509962).
- A CPIC NAT2–isoniazid guideline was still in development as of 2024–2025 ([CPIC minutes Dec 2024](https://cpicpgx.org/wp-content/uploads/2024/12/CPIC-Minutes_Dec-2024.docx)).

**HIV co-infection:** give ART alongside TB therapy and watch for IRIS. No hepatic-specific IRIS figures were verified.

**Gene, cell and RNA therapies:** not applicable. Recombinant IFN-γ is used in some MSMD patients, but this is not specific to hepatic TB and was not retrieved here.

**Hepatic-specific clinical trials:** none identified.

---

## 13. Prevention

- **Primary prevention:**
  - BCG vaccination. A hepatic-specific efficacy meta-analysis was not retrieved.
  - Infection control.
  - Addressing undernutrition, alcohol, smoking, diabetes and HIV (WHO 2024).
- **Secondary prevention:**
  - LTBI testing and preventive therapy in high-risk groups: people living with HIV, transplant candidates, and people starting TNF inhibitors.
  - A high index of suspicion in endemic areas for hepatomegaly, fever or raised liver enzymes (PMID 25943103).
- **Tertiary prevention:**
  - Prompt rifampicin-containing therapy.
  - Liver-function monitoring during treatment (PMID 17021358).
  - Biliary decompression where needed.
- **Genetic counselling:** relevant only for MSMD families.

---

## 14. Other Species / Natural Disease

- **Cattle:** *M. bovis* (bovine TB) can involve the liver in cattle and is zoonotic. The retrieved literature covered liver fluke co-infection as a herd-risk factor rather than hepatic lesions: liver fluke "were not improved" bTB risk models (Byrne 2019, PMID 31012527).
- **Orthologs:** *TYK2* and *IL12RB1* orthologs exist in mouse and zebrafish. NCBI Gene IDs were not retrieved.
- **OMIA:** no entry applies, because the disease is not Mendelian.

---

## 15. Model Organisms

| Model | Findings | Recapitulation and limits |
|---|---|---|
| Mouse, *M. tuberculosis* IV/aerosol | Liver least infected; growth limited to macrophages (PMID 11705978) | Reproduces hepatic granulomas. Mice do not form caseating granulomas the way humans do. |
| Mouse, BCG intravital imaging | Kupffer cells nucleate granulomas; immobile myeloid core with mobile T cells; TNF-dependent maintenance (PMID 18261937) | Excellent for granuloma dynamics. Uses BCG rather than virulent *M. tuberculosis*. |
| Zebrafish embryo, *M. marinum* | Innate macrophages alone initiate granulomas (Davis 2002, PMID 12479816); further work in PMID 17553562 and PMID 21372049 | Optically transparent; useful for genetic screens. Different pathogen, and not hepatic. |
| Knockout mice (e.g., IFN-γ, TNF pathway) | Disseminated disease | Not retrieved specifically for liver in this session. |

**Resources:** MGI and ZFIN. No hepatic-TB-specific model was identified.

---

## Key References (PMIDs retrieved in this session)

25943103 (Hickey 2015 systematic review) · 24976240 (Chaudhary 2014) · 28148232 (Gounder 2017) · 26499189 (Kakkar 2015 imaging) · 7744492 (Chien 1995) · 3659266 (Maharaj 1987) · 14600128 (Huang 2003) · 24179582 (Wu 2013) · 29759945 (Ai 2018 NGS) · 15162540 (Yu 2004) · 2157746 (Oliva 1990) · 10398910 (Kok 1999) · 16531964 (Desai 2006) · 19642133 (Holty 2009) · 18261937 (Egen 2008) · 11705978 (Seiler 2001) · 12479816 (Davis 2002) · 30264912 (Rosain 2018 MSMD) · 30578352 (Boisson-Dupuis 2018) · 31068474 (Kerner 2019) · 33901685 (Yadav 2021 VDR) · 30509962 (Khan 2019 NAT2) · 17021358 (Saukkonen 2006 ATS) · 33951360 (Dorman 2021) · 21535224 (Itoi 2011) · 31012527 (Byrne 2019). Essop 1984, Q J Med 53:465–77, is cited by journal reference; its PMID was not retrieved.

**Sources:** [PMC4425874](https://pmc.ncbi.nlm.nih.gov/articles/PMC4425874/) · [PMC4073015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4073015/) · [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search) · [WHO GTB Report 2024](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024) · [WHO Module 4](https://www.ncbi.nlm.nih.gov/books/NBK613096/) · [Mondo via SAIL](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0005787/) · [SNOMED 186273003](https://art-decor.org/terminology/snomed/viewConcept/186273003) · [AAPC A18.83](https://aapc.com/codes/icd-10-codes/A18.83) · [NHS ICD-10](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-a15-a19.htm) · [Kerner 2019 (Pasteur record)](https://research.pasteur.fr/en/b/a5Q) · [ATS hepatotoxicity statement](https://www.thoracic.org/statements/resources/mtpi/hepatotoxicity-of-antituberculosis-therapy.pdf) · [CPIC](https://cpicpgx.org/wp-content/uploads/2024/12/CPIC-Minutes_Dec-2024.docx) · [CIDRAP](https://www.cidrap.umn.edu/tuberculosis/who-report-shows-global-tuberculosis-cases-are-rising) · [MGI DOID:407](https://www.informatics.jax.org/disease/DOID:407)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 48 |
| On topic | 28 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25943103` *(abstract only)*: "likely underreported"
  - Text part not found as substring: 'likely underreported' (note: only abstract available for PMID:25943103, full text may contain this excerpt)
- `PMID:25943103` *(abstract only)*: "Approximately 79% of all reported hepatic TB cases were due to systemic dissemination of bacilli"
  - closest text in source: "We sought to review case series to characterize the epidemiology, pathophysiology, clinical features, diagnosis, and treatment of hepatic TB and to comment on the impact of HIV co-infection on these characteristics"
- `PMID:25943103` *(abstract only)*: "Hepatic TB has become more prevalent, likely as a result of the… HIV/AIDS epidemic"
  - closest text in source: "Hepatic TB has become more prevalent, likely as a result of the human immunodeficiency virus/acquired immunodeficiency syndrome (HIV/AIDS) epidemic"
- `PMID:26499189` *(abstract only)*: "no standard classification system"
  - Text part not found as substring: 'no standard classification system' (note: only abstract available for PMID:26499189, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:17553562` (2 mentions) - Identification and real-time imaging of a myc-expressing neutrophil population involved in inflammation and mycobacterial granuloma formation in zebrafish.
  - shared terms: gene, mycobacterium

Weighed against this report's own most characteristic terms: `liver`, `hepatic`, `disease`, `tuberculosis`, `found`, `patient`, `local`, `abscess`, `disseminated`, `serie`, `gene`, `hiv`, `miliary`, `essop`, `genetic`, `msmd`, `form`, `label`, `lesion`, `mycobacterium`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 12 |

### Terms the ontology service could not be reached for

11 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `EXT_ID:7744492` (2 mentions)
- `EXT_ID:14600128` (2 mentions)
- `EXT_ID:24179582` (2 mentions)
- `EXT_ID:29759945` (2 mentions)
- `EXT_ID:15162540` (2 mentions)
- `EXT_ID:28148232` (2 mentions)
- `EXT_ID:2157746` (2 mentions)
- `EXT_ID:10398910` (2 mentions)
- `EXT_ID:16531964` (2 mentions)
- `MONDO:0005787` (6 mentions)
- `DOID:407` (7 mentions)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `EXT_ID`.

No term could be looked up either way, so nothing here was confirmed or contradicted.