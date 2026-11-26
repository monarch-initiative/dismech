---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-20T13:56:48.745218'
end_time: '2026-11-20T14:01:36.664026'
duration_seconds: 287.92
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Congenital Nongoitrous Hypothyroidism 3
  mondo_id: MONDO:0012360
  category: Mendelian
  causal_genes: not recorded
  omim_id: OMIM:609893
  synonyms: CHNG3; hypothyroidism, congenital, nongoitrous, 3
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
  web_search_requests: 7
  num_turns: 15
  total_cost_usd: 0.951106915
  session_id: 14527bd7-bf70-47ed-9024-616d721b96da
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  tool_calls: 26
  retrieval_calls: 25
  assistant_text_blocks: 2
citation_count: 16
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 2
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:38714869
  relevance_assessed: 10
  on_topic: 6
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 3
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Nongoitrous Hypothyroidism 3
- **MONDO ID:** MONDO:0012360 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** OMIM:609893
- **Synonyms:** CHNG3; hypothyroidism, congenital, nongoitrous, 3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Nongoitrous Hypothyroidism 3** covering all of the
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

Fetching the key abstracts through Europe PMC, since PubMed blocked automated access.

I have enough sourced material now, so I'm writing the report.

# Congenital Nongoitrous Hypothyroidism 3 (CHNG3; OMIM 609893; MONDO:0012360)

**How I read the request:** The template says "causal gene: not recorded." My sources show the cause is not a protein-coding gene. It is a non-coding, thyroid-specific **(TTTG)4 short tandem repeat (STR)** on chromosome 15q, catalogued in OMIM as *620900, "SHORT TANDEM REPEAT, TTTG(4), THYROID-SPECIFIC; STRTS" ([OMIM 620900](https://omim.org/entry/620900)). The repeat lies between **DET1** and **MIR7-2**. Its mutant alleles turn up the bicistronic **MIR7-2/MIR1179** microRNA locus, which sits about 35 kb downstream ([Grasberger et al. 2024, PMID 38714869, PMC11472772](https://pmc.ncbi.nlm.nih.gov/articles/PMC11472772/)). So the effector "gene" is best given as MIR7-2/MIR1179, and the causal locus as STRTS.

**Limits on sources:**
- PubMed, OMIM (HTTP 403) and the Narumi full text (captcha) blocked automated retrieval.
- The 2024 Grasberger paper was read verbatim only for roughly its first 40,000 characters. Points I could not confirm are marked *unverified*.
- I did not retrieve any HPO, GO, CL, UBERON, NCIT, Orphanet or ICD identifiers. Ontology suggestions are given **as labels only** and need ID lookup before curation.

---

## 1. Disease information

- **What it is:**
  - Clinically, CHNG3 is **autosomal dominant resistance to thyrotropin (RTSH)**: TSH is raised from birth, the thyroid is not enlarged, and thyroid hormone is usually normal or near-normal.
  - The Disease Ontology defines it as congenital hypothyroidism with autosomal dominant inheritance of resistance to thyrotropin, caused by a heterozygous change in a thyroid-specific TTTG(4) intergenic non-coding STR ([DOID:0070127](https://disease-ontology.org/term/DOID:0070127/owl)).
  - The 2024 paper says: "Affected individuals present at birth with nongoitrous euthyroid hyperthyrotropinemia that persists into adulthood" (PMID 38714869).
- **Identifiers I retrieved:**
  - OMIM 609893 ([CISMeF](https://www.cismef.org/page/detail/en/MIM_PH_609893), which records it as "phenotype, molecular basis known")
  - MONDO:0012360 ([NORD/MONDO page](https://rarediseases.org/mondo-disease/congenital-nongoitrous-hypothryoidism-3/))
  - DOID:0070127
  - MedGen 482447
  - MGI disease page OMIM:609893 ([MGI](https://www.informatics.jax.org/disease/OMIM:609893))
  - I did not retrieve Orphanet, ICD-10/11 or MeSH codes. The closest broad category, congenital hypothyroidism, falls under ICD-10 E03.1, but I have not verified this.
- **Synonyms:** CHNG3; hypothyroidism, congenital, nongoitrous, 3; thyrotropin resistance; RTSH; resistance to thyrotropin ([CISMeF](https://www.cismef.org/page/detail/en/MIM_PH_609893)).
- **Data source type:** Aggregated disease-level resources (OMIM, MONDO, DOID) plus family-based research cohorts. No EHR data.

## 2. Etiology

- **Cause:**
  - The cause is germline, heterozygous, non-coding mutation of the (TTTG)4 STR. The STR lies inside a primate-specific AluSx1 retrotransposon that carries a "weak thyroid-specific enhancer-like chromatin signature" (PMID 38714869).
  - The 2024 abstract: "Non-coding mutations in a (TTTG)4 short tandem repeat (STR) underlie dominantly inherited RTSH in all 82 affected participants from 12 unrelated families."
- **History of the locus:**
  - Grasberger et al. 2005 (JCEM, PMID 15870119; DOI 10.1210/jc.2005-0572) described five multigenerational kindreds: 102 individuals, 56 affected.
    - They found "no evidence of incomplete penetrance but variable expressivity."
    - They excluded linkage to TSHR, PAX8, TITF1 (NKX2-1), GNAS and FOXE1.
  - Grasberger et al. 2005 (Hum Genet, PMID 16189712; DOI 10.1007/s00439-005-0036-6) mapped the locus to **15q25.3–26.1**.
    - Maximum multipoint LOD scores were 8.51 and 4.31.
    - Linkage was replicated in three further kindreds.
    - Fine mapping narrowed the locus to a 3 cM / 2.9 Mb interval.
- **Genetic risk factors:**
  - **STR 4/3:** deletion of one TTTG unit (10 of 12 families).
  - **STR 4/4\*:** a T>G substitution in the third repeat (TTGG instead of TTTG).
  - Details of both are in §4.
- **Allelic spectrum (Japan):**
  - Narumi et al. 2024 (PMID 38714868; DOI 10.1038/s41588-024-01735-5) found TTTG microsatellite variants in **137/989 congenital hypothyroidism (CH) patients, 3/33 multinodular goiter (MNG) patients and 3/38,722 controls**.
  - Their linkage study started from one family with both non-goitrous CH and MNG.
- **Environmental risk factors:** None reported. The disease is monogenic.
- **Protective factors:** None reported.
- **Gene–environment interaction:** None reported. Iodine status as a modifier has not been studied in the sources I retrieved.

## 3. Phenotypes

Sources are PMID 38714869 (12 families, 82 affected) and PMID 15870119 unless noted. HPO labels are suggestions only; the IDs need verification.

| Phenotype | Type | Onset / course | Frequency | Suggested HPO label |
|---|---|---|---|---|
| Raised serum TSH (hyperthyrotropinemia) | Lab | Neonatal, lifelong; highest in newborns, then the expected fall with age | 100%: "All participants with STRmut had serum TSH values above the upper limit of the reference range indicating complete penetrance" | Increased circulating thyroid-stimulating hormone level |
| Free T4 normal or slightly low | Lab | Lifelong | FT4 was "slightly lower… but, except for one individual, still within the population reference range"; no correlation with TSH | (euthyroid) / Decreased circulating free T4 (rare) |
| Raised serum thyroglobulin | Lab | Lifelong | "most participants"; "uncorrelated to the degree of hyperthyrotropinemia". Also seen in untreated affected subjects in 4 of the 5 families in 2005 | Increased circulating thyroglobulin level |
| Normal or small thyroid (non-goitrous) | Sign / imaging | Congenital | On ultrasound, 5 normal-sized and 4 hypoplastic | Thyroid hypoplasia |
| Low radionuclide uptake | Imaging / lab | — | Low in 6 of 7 tested, normal in 1 | Decreased radioactive iodine uptake |
| Enlarged nodular gland needing surgery | Sign | Adult (inferred) | 3/82 (3.66%) | Multinodular goiter |
| Positive newborn TSH screen / congenital hypothyroidism | Lab | Neonatal | Common (not quantified in the text I read) | Congenital hypothyroidism |
| Ectopic thyroid (Japanese 15q26.1 carriers) | Imaging | Congenital | All 5 carriers from 4 families in a 63-patient CH cohort ([ECE-ESPE 2025 abstract](https://www.endocrine-abstracts.org/ea/0110/ea0110oc11.2)) | Ectopic thyroid gland |

- **Severity:** Mild. The University of Miami describes the condition as "often misdiagnosed as hypothyroidism" ([UM news](https://news.med.miami.edu/?p=23569)).
- **Tissue specificity:** No phenotype outside the thyroid has been reported. The enhancer was not active in skin fibroblasts, "consistent with thyroid specific regulation" (PMID 38714869).
- **Quality of life:** No QoL data (EQ-5D, SF-36) were found.

## 4. Genetic and molecular information

- **Causal locus:**
  - STRTS (OMIM *620900), at 15q26.1 (2024 papers); earlier given as 15q25.3–26.1.
  - Note: DOID and ZFIN list 15q25.1. This conflicts with the other sources and should be treated as a discrepancy.
- **Variants** (Table 1 of PMID 38714869, GRCh38):
  - **STR3 (4→3 repeats):** `NC_000015.10:g.88569449_88569452del` (VCF GRCh38 15:88569433 CTTTG>C).
    - gnomAD v3.1.2 frequency: **1/151,588**.
    - The deletion is recurrent; it arose **de novo** in family 14.
    - Enrichment versus gnomAD: FDR = 2.8 × 10⁻⁴⁴.
  - **STR4\*:** GRCh38 15:88569444 T>G, giving TTGG in place of TTTG in the third repeat. It is "absent in gnomAD."
  - The second single-nucleotide change mentioned in the abstract ("a single nucleotide change within the STR (two families)") could not be verified verbatim.
- **Segregation:** STRwt was homozygous in all 66 unaffected relatives tested. All 76 genotyped affected participants were heterozygous for STR3 or STR4\*.
- **Classification:** I retrieved no ClinVar or ClinGen classification.
- **Variant class:** Non-coding regulatory, intergenic STR variants (contraction or substitution).
- **Origin:** Germline.
- **Functional consequence:**
  - **Gain of function** of a cis-regulatory element. The mutant STR switches on a thyroid enhancer cluster and increases MIR7-2/MIR1179 expression on the same haplotype.
  - Narumi et al. instead describe the microsatellite as part of a "thyroid-specific transcriptional repressor" whose activity the variants disrupt (PMID 38714868, abstract). The two framings agree: loss of repression is equivalent to gain of enhancer activity.
- **Modifier genes, epigenetics, chromosomal abnormalities:** No modifier genes have been reported. The epigenetic findings are chromatin-accessibility results, covered in §6. No chromosomal abnormality is involved.

## 5. Environmental information

There are no known environmental, lifestyle or infectious contributors. This section is not applicable.

## 6. Mechanism and pathophysiology

**Causal chain:**

1. A germline heterozygous contraction (TTTG)4→(TTTG)3 or a T>G substitution occurs in an intergenic STR inside a primate-specific AluSx1 element on chr15q26.1, between DET1 and MIR7-2 (demonstrated; PMID 38714869).
2. This **leads to** a new chromatin footprint at the STR in thyrocytes.
   - STR3 "was contained within a 30–60 bp footprint on 22 of 27 chromatin fibers."
   - Predicted FOXE1 binding sites lie there; that FOXE1 actually binds is *inferred*.
3. This **results in** activation of a codependent cluster of "five accessible elements" that forms a thyroid-specific enhancer. Element 2, which overlaps the STR, is central (Fiber-seq on thyroid tissue; demonstrated).
4. This **leads to** greater accessibility, on the same haplotype only, of the MIR7-2/MIR1179 promoter about 35 kb downstream.
   - Quote: "substantially and selectively enhanced on the STR3 haplotype."
   - The 13.5 kb region of interest showed 5.7-fold higher expression (P = 0.0003) on RNA-seq.
5. This **results in** overexpression of mature **miR-7-5p** and **miR-1179** in thyrocytes but not in fibroblasts (demonstrated).
   - Fold changes of about 10.9× and 2.6× are *unverified*.
6. This **leads to** imbalance in signaling pathways that miR-7-5p targets. This step is **working model / inferred**.
   - Candidate targets in the unverified summary: EGFR, IGF1R, PIK3CB/PIK3CD, giving PI3K–AKT–mTOR effects.
   - Also unverified: luciferase assays reportedly showed that TSHR is *not* substantially targeted.
7. This **results in** less thyrocyte proliferation and growth response to TSH, i.e. **TSH resistance** (inferred). Two branches follow:
   - **7a.** Weaker growth signaling leads to a normal-sized or hypoplastic gland and low radionuclide uptake.
   - **7b.** Compensatory pituitary TSH rise leads to near-normal FT4 and high thyroglobulin. Positive feedback then holds euthyroid hyperthyrotropinemia in place for life. In a minority of carriers, nodular growth leads to MNG (3.7%; Narumi links CH and MNG genetically).

**Checklist coverage:**
- **Pathways (suggested GO labels):**
  - miRNA-mediated post-transcriptional gene silencing
  - regulation of transcription by RNA polymerase II (enhancer activity)
  - thyroid-stimulating hormone signaling pathway
  - thyroid hormone generation
  - epidermal growth factor receptor signaling pathway / phosphatidylinositol 3-kinase signaling (inferred)
- **Cell type (suggested CL label):** thyroid follicular cell.
- **Not reported:** immune involvement, metabolic or lipidomic profiling, single-cell data and CRISPR screens.
- **Omics data:** RNA-seq and Fiber-seq data are deposited at SRA BioProject PRJNA972324.

## 7. Anatomy

- **Primary organ:** Thyroid gland (endocrine system). Suggested UBERON label: thyroid gland.
- **Secondary:** Pituitary thyrotrophs, as the physiological source of the compensatory TSH rise. This is inferred, not a lesion.
- **Cell:** Thyroid follicular epithelial cell (thyrocyte).
- **Subcellular:** Nucleus (chromatin, enhancer) and cytoplasmic miRNA–RISC machinery. Suggested GO CC labels: nucleus, chromatin, RISC complex.
- **Lateralization:** Bilateral (whole gland).

## 8. Temporal development

- **Onset:** Congenital or neonatal, often found on newborn TSH screening.
- **Course:** Stable and lifelong.
  - TSH and FT4 are highest in newborns, then fall in the expected age-related pattern (PMID 38714869).
  - A small proportion develop nodular glands in adulthood.
- **Remission:** None. The biochemical trait persists.
- **Critical period:** The neonatal period, when it must be told apart from true congenital hypothyroidism, which needs urgent treatment.

## 9. Inheritance and population

- **Inheritance:** Autosomal dominant.
- **Penetrance:** Complete for raised TSH (PMID 38714869). The 2005 study found no incomplete penetrance.
- **Expressivity:** Variable (PMID 15870119).
- **Segregation and sex ratio:** In fully phenotyped generations, 64% of offspring were affected. The male:female ratio was 1:1.4 (PMID 15870119).
- **De novo cases:** Documented (family 14), and the deletion is recurrent across families.
- **Frequency among RTSH families:** STR variants were found in "12 of 101 families with RTSH" (PMID 38714869).
- **Frequency in Japan (allelic):** 137/989 (≈13.9%) of CH patients carried TTTG variants, versus 3/38,722 controls (PMID 38714868). This suggests the locus is a common cause of CH in Japan.
- **Ethnicity:** The 2024 abstract describes families of "different ethnic origins"; I could not verify the specific countries.
- **Prevalence or incidence:** No disease-specific prevalence is available. CH overall affects about 1 in 2,000 newborns ([UChicago](https://biologicalsciences.uchicago.edu/news/new-genetic-mutation-identified-congenital-thyroid-condition)).
- **Anticipation:** The STR is short and contracted rather than expanded; no anticipation has been reported.
- **Consanguinity:** Not relevant, since inheritance is dominant.

## 10. Diagnostics

- **Laboratory:**
  - Serum TSH: raised.
  - FT4 and T3: normal or low-normal.
  - Serum thyroglobulin: often raised.
  - Thyroid autoantibodies: negative. "Nonautoimmune" is part of Narumi's title.
- **Imaging:**
  - Ultrasound: normal or hypoplastic gland; ectopy reported in Japanese carriers.
  - Radionuclide scan: uptake often low.
- **Genetic testing:**
  - The STR is non-coding and intergenic, so **standard exome and CH gene panels will miss it**.
  - Targeted Sanger sequencing or genome sequencing (WGS) is needed. Both 2024 studies used WGS plus Sanger.
  - Repeat-aware variant calling is advisable because the change is a 4 bp contraction within a repeat.
- **Differential diagnosis:**
  - CHNG1 (TSHR loss of function; OMIM 275200)
  - CHNG2 (PAX8; OMIM 218700)
  - Other dyshormonogenesis and dysgenesis genes
  - Subclinical autoimmune hypothyroidism
  - Transient neonatal hyperthyrotropinemia
  - Points that favour CHNG3: dominant family history, no goitre, high thyroglobulin and a negative TSHR/PAX8 result.
- **Screening:** Newborn TSH screening detects affected infants.

## 11. Prognosis

- **Survival:** Life expectancy is expected to be normal. No mortality data exist.
- **Long-term outcome:** Mostly euthyroid; morbidity appears low. About 3.7% need surgery for enlarged nodular glands (PMID 38714869).
- **Prognostic biomarkers:** None established. TSH and FT4 do not correlate with each other.

## 12. Treatment

- **No disease-specific therapy exists.**
- Levothyroxine (suggested NCIT label: Levothyroxine Sodium) is used for CH in general. Some participants in the 2024 study were on L-T4, which was stopped for at least 6 weeks before testing.
- No trials of whether levothyroxine is needed in euthyroid carriers were found.
- **Surgery:** Thyroidectomy for nodular goitre (NCIT label: Thyroidectomy).
- **Advanced therapies:** None. No ClinicalTrials.gov entries were found.
- **Personalized approach:** A genetic diagnosis may prevent unnecessary lifelong treatment of mild euthyroid hyperthyrotropinemia. This is my inference from the "misdiagnosed" framing; no trial tests it.

## 13. Prevention

- **Primary prevention:** None.
- **Secondary prevention:** Newborn TSH screening.
- **Cascade testing:** Testing relatives for the STR is feasible.
- **Counseling:** 50% recurrence risk to offspring; de novo cases occur.

## 14. Other species

- The STR appears to be **primate-specific**.
- Gorillas carry TCTG-variant alleles at the equivalent STR (11 gDNA samples), and "gorillas have significantly higher serum TSH levels than other great apes" (PMID 38714869).
- Some New World monkeys have the syntenic region without TTTG repeats.
- No OMIA entries were found.

## 15. Model organisms

- **No animal model exists.**
- The enhancer cluster is not fully conserved in rodents, so mouse models were reportedly judged unfeasible (*unverified* summary of PMID 38714869).
- **Experimental systems used so far:**
  - Primary human thyroid tissue (Fiber-seq, RNA-seq)
  - Patient skin fibroblasts (negative control tissue)
  - HEK293 and COS1 luciferase assays (*unverified*)
  - In vitro repressor assays (Narumi; details not retrieved)
- MGI lists OMIM:609893 but gives no specific model ([MGI](https://www.informatics.jax.org/disease/OMIM:609893)).

---

### Key references
- Grasberger H, et al. **2024**. *Nat Genet* 56:877–888. PMID 38714869; PMC11472772; doi:10.1038/s41588-024-01717-7.
- Narumi S, et al. **2024**. *Nat Genet* 56:869–876. PMID 38714868; PMC11096107; doi:10.1038/s41588-024-01735-5.
- Grasberger H, et al. **2005**. *J Clin Endocrinol Metab* 90:4025–4034. PMID 15870119.
- Grasberger H, et al. **2005**. *Hum Genet* 118:348–355. PMID 16189712.

### Sources
- [PMC11472772](https://pmc.ncbi.nlm.nih.gov/articles/PMC11472772/)
- [Nature Genetics s41588-024-01717-7](https://www.nature.com/articles/s41588-024-01717-7)
- [PubMed 38714869](https://pubmed.ncbi.nlm.nih.gov/38714869/)
- [Narumi PMC11096107](https://pmc.ncbi.nlm.nih.gov/articles/PMC11096107)
- [Nature s41588-024-01735-5](https://www.nature.com:443/articles/s41588-024-01735-5)
- [OMIM 620900](https://omim.org/entry/620900)
- [PubMed 15870119](https://pubmed.ncbi.nlm.nih.gov/15870119/)
- [Hum Genet 2005 record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_hal_primary_oai_HAL_hal_00174467v1)
- [DOID:0070127](https://disease-ontology.org/term/DOID:0070127/owl)
- [NORD/MONDO](https://rarediseases.org/mondo-disease/congenital-nongoitrous-hypothryoidism-3/)
- [CISMeF](https://www.cismef.org/page/detail/en/MIM_PH_609893)
- [MGI](https://www.informatics.jax.org/disease/OMIM:609893)
- [UChicago news](https://biologicalsciences.uchicago.edu/news/new-genetic-mutation-identified-congenital-thyroid-condition)
- [UMiami news](https://news.med.miami.edu/?p=23569)
- [ECE-ESPE 2025 abstract](https://www.endocrine-abstracts.org/ea/0110/ea0110oc11.2)
- [Wikipedia: Congenital hypothyroidism](https://Www.wikipedia.org/wiki/Congenital_hypothyroidism)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:38714869`: "Affected individuals present at birth with nongoitrous euthyroid hyperthyrotropinemia that persists into adulthood"
  - closest text in source: "The unaffected individuals in each family were homozygous for four repeats (STR 4/4), whereas all affected individuals were heterozygous for a deletion of one repeat (STR 4/3; Fig"
- `PMID:38714869`: "weak thyroid-specific enhancer-like chromatin signature"
  - closest text in source: "The STR maps to a predicted cis-regulatory element (SCREEN database; EH38E3153006) that exhibits a weak thyroid-specific enhancer-like signature and is located within a topologically associating domain (TAD) containing seven annotated genes, several of them being normally expressed in thyroid tissue (Extended Data Fig"
- `PMID:38714869`: "consistent with thyroid specific regulation"
  - closest text in source: "The STR is contained in a primate-specific Alu retrotransposon with thyroid-specific cis-regulatory chromatin features"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

2 of 3 terms resolved to a current term; the rest could not be looked up either way.
