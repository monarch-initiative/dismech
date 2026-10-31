---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-31T20:14:01.125882'
end_time: '2026-10-31T20:14:56.734301'
duration_seconds: 55.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Combined Factor V and Factor VIII Deficiency
  mondo_id: MONDO:0018175
  category: Mendelian
  causal_genes: LMAN1, MCFD2
  omim_id: not recorded
  synonyms: combined deficiency of factor V and factor type VIII; F5F8D; FV and FVIII
    combined deficiency; familial multiple coagulation factor deficiency
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
  total_cost_usd: 0.6910026
  session_id: 8c6626a0-6fa6-5ad6-8fa7-2f4c04f432c1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 6
reference_validation:
  total_references: 5
  verified: 3
  not_found: 0
  unverifiable: 2
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 1
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:23852824
  - PMID:19183188
  relevance_assessed: 3
  on_topic: 3
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Factor V and Factor VIII Deficiency
- **MONDO ID:** MONDO:0018175 (if available)
- **Causal gene(s):** LMAN1, MCFD2
- **OMIM:** not recorded
- **Synonyms:** combined deficiency of factor V and factor type VIII; F5F8D; FV and FVIII combined deficiency; familial multiple coagulation factor deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Combined Factor V and Factor VIII Deficiency** covering all of the
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

# Combined Factor V and Factor VIII Deficiency (F5F8D): research report

**Verification status.** I ran two web searches. Only the PMIDs and quotes marked **[verified]** appeared in those results. Everything marked **[from memory]** is not source-checked, including any PMID I give for it. Verify those with `just fetch-reference` before using them as evidence. I could not retrieve the GeneReviews chapter, OMIM, Orphanet or the MONDO record. The OMIM number is left blank, as in your template, and I did not confirm MONDO:0018175 against the MONDO record.

**Causal genes.** The disease is caused by recessive loss of function in **LMAN1** (the gene for ERGIC-53, on 18q21) or **MCFD2** (on 2p21–p16). Your template's identifiers (LMAN1, MCFD2) match this. I did not look up the HGNC IDs. Look them up and use the lowercase `hgnc:` form.

## 1. Disease information
- F5F8D is a rare autosomal recessive bleeding disorder. Plasma FV and FVIII are low together (see section 3).
- It is not a defect in the F5 or F8 genes. It is a defect in the cell's secretory transport of both proteins.
- **Synonyms:** those listed in your template.
- **Source type:** this is an aggregated, disease-level description from reviews, not individual patient (EHR) data.

## 2. Etiology
- **Cause:** biallelic mutations in LMAN1 or MCFD2.
  - **Share of families:** "Together, mutations in LMAN1 and MCFD2 account for nearly all cases of F5F8D, with c. 70% of F5F8D families attributable to LMAN1 mutations and c. 30% to MCFD2 mutations." [verified, [PMID:23852824](https://www.pubmed.gov/23852824/)]
- **Environmental risk and protective factors:** none known. This is a monogenic disorder.
- **Gene-environment interaction:** none known. Consanguinity raises the chance of homozygosity (see section 9).
- **Modifiers:** I found no established modifier genes.

## 3. Phenotypes
All HPO terms below are suggestions. Look up each CURIE and label before binding.

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Reduced FV and FVIII activity | Decreased factor V activity; Decreased factor VIII activity (HPO has terms for both, so search for them) | Laboratory abnormality. "F5F8D is characterized by concomitantly low levels (usually between 5% and 20%) of both FV and FVIII and is associated with a mild to moderate bleeding tendency." [verified, [PMID:23852824](https://www.pubmed.gov/23852824/)] |
| Prolonged PT and aPTT | Prolonged prothrombin time; Prolonged partial thromboplastin time | Laboratory abnormality. Frequency not checked. |
| Mild to moderate bleeding tendency | Abnormal bleeding | Verified as stated above. |
| Epistaxis, easy bruising, menorrhagia, postpartum, post-surgical and post-dental-extraction bleeding | Epistaxis; Easy bruising; Menorrhagia | [from memory] Frequencies not checked. |

- **Onset:** usually childhood or later, when a bleed or surgery draws attention. [from memory]
- **Course:** lifelong and stable. Bleeding is provoked, not progressive. [from memory]
- **Quality-of-life data:** none checked.
- **Genotype and phenotype:** "the mean levels of plasma FV and FVIII in patients with MCFD2 mutations are significantly lower than the corresponding levels in patients with LMAN1 mutations." [verified, [PMID:19183188](https://www.qxmd.com/r/23852824); the review is cited in my search results, but I did not open its page]
  - The two groups overlap considerably, and they cannot be told apart clinically.

## 4. Genetic and molecular information
- **LMAN1** and **MCFD2** are the two causal genes.
- **Variant spectrum:** LMAN1 variants are mostly null (nonsense, frameshift, splice and start-codon changes). MCFD2 variants are mostly missense or small deletions that disrupt EF-hand calcium-binding structure. [from memory] Population allele frequencies and ClinGen classifications were not checked. Look up ClinGen gene-disease validity before recording any tier, and copy the tier from the source.
- **Origin:** germline. There are no somatic, epigenetic or chromosomal abnormalities that I know of.
- **Functional consequence:** loss of function.
  - **Molecular defect:** "Disrupting the LMAN1-MCFD2 receptor complex formation is the primary molecular defect of missense mutations leading to F5F8D" [verified, [PMID:23852824](https://www.pubmed.gov/23852824/)].

## 5. Environmental information
None known: no toxin, lifestyle or infectious cause.

## 6. Mechanism and pathophysiology

**Causal chain**
1. Biallelic loss of function in LMAN1 or MCFD2 abolishes the LMAN1–MCFD2 complex, or removes one of its two members.
2. "The LMAN1-MCFD2 protein complex functions as a cargo receptor that facilitates the transport of FV and FVIII from the ER to the Golgi apparatus." [verified, [PMID:23852824](https://www.pubmed.gov/23852824/)]
3. Without the receptor, FV and FVIII secretion falls. I did not verify the reported mechanistic detail that the proteins are retained in the ER.
4. Plasma FV and FVIII fall to about 5–20% of normal (step 3 is the inferred link).
5. Two cofactors of coagulation are deficient together, and a mild to moderate bleeding tendency follows.

- **Why only FV and FVIII are affected** is not established in what I retrieved. The suggestion that other cargo is carried by additional receptors is inference on my part.
- **Suggested ontology terms.** Look up each CURIE before use.
  - **Biological process:** ER-to-Golgi vesicle-mediated transport (GO), a protein-export-from-ER term, and a blood coagulation term.
  - **Cell type:** hepatocyte (CL). FV and FVIII are made in the liver. FVIII is also made by liver sinusoidal endothelial cells. [from memory]
  - **Subcellular compartments:** endoplasmic reticulum, ER–Golgi intermediate compartment, and Golgi apparatus (GO CC).
  - **Calcium:** the complex needs calcium. MCFD2 binds LMAN1 in a calcium-dependent way. [verified in the retrieved snippet as "Ca2+-dependent"]
- **Omics, immune, metabolic and single-cell data:** none retrieved, and I do not expect any.

## 7. Anatomical structures affected
- **Primary:** none show structural change. The defect is in secretion by liver cells and other factor-producing cells.
- **Clinical effect:** bleeding from mucosa, skin, the uterus and surgical sites.
- **Localization:** bilateral and systemic. Suggested UBERON term: liver.

## 8. Temporal development
- Congenital, present from birth. It is often diagnosed late.
- Stable throughout life. There is no remission. The risk is highest around surgery, trauma, dental work and childbirth. [from memory, no citation]

## 9. Inheritance and population
- **Inheritance:** autosomal recessive.
  - Suggested HPO term: autosomal recessive inheritance. Verify the CURIE.
- **Prevalence:** "F5F8D is estimated to be extremely rare (1:1,000,000) in the general population, but an increased frequency is observed in regions where consanguineous marriages are practiced." [verified in a search snippet from a [rarecoagulationdisorders.org](https://rarecoagulationdisorders.org/disorder/combined-fv-and-fviii-deficiency/) or review page; I could not tell which page the snippet came from]
  - For the KB, use `measure_type: UNKNOWN` unless the measure is stated, and put `rate_per_100000: 0.0001`. Check the source's measure type first.
- **Populations:** the disorder is concentrated in Middle Eastern Jewish groups, Iranians, Arabs and Turks. [from memory]
  - **Founder variants:** examples exist in Middle Eastern Jewish groups. I did not retrieve the specific variants.
- **Sex ratio:** equal, by autosomal inheritance.
- **Penetrance, expressivity and carriers:** I did not retrieve penetrance data. Heterozygous carriers are generally reported as asymptomatic. [from memory] Genetic anticipation and germline mosaicism: not applicable.

## 10. Diagnostics
- **Laboratory:** low FV and FVIII activity, with prolonged PT and aPTT.
  - LOINC codes for the factor assays should be looked up with `just loinc-seed-cache`, not typed from memory.
- **Genetic testing:** sequencing of LMAN1 and MCFD2 (a two-gene panel, single genes, or exome) confirms the diagnosis. [from memory]
- **Differential diagnosis:** hemophilia A (distinguished by normal FV), isolated FV deficiency, combined deficiency of vitamin K-dependent factors, liver disease, and acquired inhibitors or disseminated intravascular coagulation.
  - These differential diagnoses come from general knowledge, not retrieved sources.
- **Screening:** none is routine. Cascade testing of relatives is reasonable.

## 11. Outcome and prognosis
- **Life expectancy:** I did not retrieve survival or mortality data. The bleeding is described as mild to moderate, so I would expect a near-normal life with appropriate cover for procedures. That is an inference and needs a citation.
- **Complications:** prolonged bleeding after surgery or childbirth. The data I could retrieve do not say how common this is.

## 12. Treatment
My searches returned no treatment information. The following is general knowledge that needs checking against a source before use. Candidate sources are the GeneReviews chapter, the 2009 review ([PMID:19598067](https://read.qxmd.com/read/19598067/combined-factor-v-and-factor-viii-deficiency), title only retrieved), and the [rarecoagulationdisorders.org page](https://rarecoagulationdisorders.org/disorder/combined-fv-and-fviii-deficiency/).

- **FV replacement:** fresh frozen plasma. No FV concentrate is available, as far as I know. [from memory]
- **FVIII replacement:** factor VIII concentrate or recombinant FVIII. [from memory]
- **Desmopressin:** reported to raise FVIII. [from memory]
- **Antifibrinolytics:** tranexamic acid for mucosal bleeding. [from memory]
- **Gene therapy and cell therapy:** none approved. I did not search clinical trials.
- **NCIT terms:** `NCIT:C15986` (Pharmacotherapy) and `NCIT:C15747` (Supportive Care) appear in the project's CLAUDE.md. Look up specific agent terms (plasma, desmopressin, tranexamic acid) and do not bind them from memory.

## 13. Prevention
- Genetic counseling for consanguineous families and carrier testing of relatives.
- Planned replacement or prophylaxis cover before surgery, dental work and delivery. [general knowledge, uncited]

## 14. Other species / natural disease
I did not search OMIA. I do not know of a naturally occurring animal form. Treat that as unchecked.

## 15. Model organisms
- I recall a Lman1 knockout mouse, but I did not check it, so I cannot say whether it reproduces the human factor deficiency.
- The cargo-receptor function of LMAN1 and MCFD2 is conserved in model systems, but I did not verify this. Check MGI and the literature before curating an `animal_models` entry. Do not write one from this report.

## Primary-literature leads (unverified, from memory)
Do not cite these until `just fetch-reference` confirms the title and abstract.
- **Nichols et al. 1997, J Clin Invest:** the 18q linkage paper. The Soff review cites it, but I did not confirm a PMID.
- **Nichols et al. 1998, Cell:** the LMAN1 (ERGIC-53) gene discovery.
- **Zhang et al. 2003, Cell:** MCFD2 discovery.

## Sources
- [Zheng & Zhang 2013 update, PMID 23852824](https://www.pubmed.gov/23852824/)
- [Combined FV and FVIII deficiency (rarecoagulationdisorders.org)](https://rarecoagulationdisorders.org/disorder/combined-fv-and-fviii-deficiency/)
- [Combined factor V and factor VIII deficiency, PMID 19598067](https://read.qxmd.com/read/19598067/combined-factor-v-and-factor-viii-deficiency)
- [PMC2777536](https://pmc.ncbi.nlm.nih.gov/articles/PMC2777536) and [PMC3563766](https://pmc.ncbi.nlm.nih.gov/articles/PMC3563766): appeared in search results, and I did not open or use them.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 2 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23852824`: "Together, mutations in LMAN1 and MCFD2 account for nearly all cases of F5F8D, with c. 70% of F5F8D families attributable to LMAN1 mutations and c. 30% to MCFD2 mutations."
  - closest text in source: "Mutations in LMAN1 and MCFD2 account for nearly all cases of F5F8D.20,21 LMAN1 is a 13-exon gene localized to chromosome 18q21"
- `PMID:23852824`: "F5F8D is characterized by concomitantly low levels (usually between 5% and 20%) of both FV and FVIII and is associated with a mild to moderate bleeding tendency."
  - closest text in source: "F5F8D is characterized by simultaneous decreases of plasma FV and FVIII to 5 to 30% of normal and mild-to-moderate bleeding symptoms"
- `PMID:19183188` *(abstract only)*: "the mean levels of plasma FV and FVIII in patients with MCFD2 mutations are significantly lower than the corresponding levels in patients with LMAN1 mutations."
  - closest text in source: "Though clinically indistinguishable, MCFD2 mutations generally exhibit lower levels of FV and FVIII than LMAN1 mutations"
- `PMID:23852824`: "The LMAN1-MCFD2 protein complex functions as a cargo receptor that facilitates the transport of FV and FVIII from the ER to the Golgi apparatus."
  - closest text in source: "LMAN1 and MCFD2 form a Ca2+-dependent cargo receptor complex that functions in the transport of FV/FVIII from the endoplasmic reticulum (ER) to the Golgi"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.