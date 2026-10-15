---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T04:05:21.148429'
end_time: '2026-10-12T04:06:25.652431'
duration_seconds: 64.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glucocorticoid Resistance
  mondo_id: MONDO:0014421
  category: Mendelian
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
  num_turns: 5
  total_cost_usd: 0.7980847
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.3.0
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
- **Disease Name:** Glucocorticoid Resistance
- **MONDO ID:** MONDO:0014421 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glucocorticoid Resistance** covering all of the
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

# Glucocorticoid Resistance (primary generalized glucocorticoid resistance, Chrousos syndrome): research report

**Verification status.** I ran three web searches in this session. Claims with a PMID and a "verified" tag come from those results. Everything else is from background knowledge and carries "unverified". Before it goes into the KB, run `just fetch-reference` on every PMID and check each snippet. Check every CURIE against its ontology lookup. That includes the template's MONDO:0014421 and the ORPHA, OMIM and HGNC identifiers below. Do not bind any unverified CURIE from this report.

## 1. Disease information

**Overview.** Primary generalized glucocorticoid resistance (GGR) is also called Chrousos syndrome, familial or sporadic glucocorticoid resistance, or cortisol resistance. It is a rare condition with generalized, partial tissue insensitivity to glucocorticoids. The cause is usually an inactivating defect in the glucocorticoid receptor gene (NR3C1).
- The hypothalamic-pituitary-adrenal (HPA) axis is compensatorily activated to overcome the resistance, giving raised ACTH and cortisol.
- Raised ACTH also drives adrenal steroids with mineralocorticoid and androgen activity.
- Patients therefore show mineralocorticoid excess and hyperandrogenism, but no Cushingoid features.
- Verified: Charmandari et al. 2008 (PMID:18319312) report that the spectrum runs from asymptomatic to severe cases of hyperandrogenism, fatigue, and/or mineralocorticoid excess.
- Verified: compensatory HPA-axis activation drives ACTH hypersecretion because the reduced sensitivity of peripheral tissues is offset by increased HPA activity.

**Identifiers (all unverified, look up before use).**
- OMIM #615962 (glucocorticoid resistance, generalized). The older entry was OMIM 138040.
- The template gives MONDO:0014421.
- Orphanet, ICD-10/11 and MeSH ("Glucocorticoid resistance" or "Cortisol resistance") were not looked up.
- HGNC for NR3C1 is probably 7978. In this KB it would be written `hgnc:7978`.

**Synonyms.** Chrousos syndrome; familial glucocorticoid resistance; generalized glucocorticoid resistance; cortisol resistance; primary cortisol resistance.

**Data source.** The information is aggregated at disease level from case reports and kindreds, not from EHR. About 100 or fewer families have been reported (unverified).

**Scope note.** Acquired, tissue-specific glucocorticoid resistance is a separate matter. It occurs in asthma, rheumatoid arthritis, inflammatory bowel disease, and leukemia, and is mediated by GRβ, cytokines, and the like. This report covers the Mendelian entry. Other states belong in a mechanism module or a grouping, not here.

**Reviews.**
- Charmandari 2008, PMID:18319312, verified.
- Nicolaides & Charmandari, Eur J Clin Invest 2015, from the search result, PMID not retrieved.
- "Glucocorticoid Resistance", Exp Suppl 2019, [PMID:31588529](https://pubmed.ncbi.nlm.nih.gov/31588529/), verified.
- Hormones (Athens) 2017, [PMID:28742501](https://pubmed.ncbi.nlm.nih.gov/28742501/). It also covers patients with similar features but no detectable NR3C1 mutation.
- Endotext chapter by Chrousos and Charmandari: [primary generalized glucocorticoid resistance syndrome](https://www.endotext.org/wp-content/uploads/pdfs/primary-generalized-glucocorticoid-resistance-syndrome.pdf).
- [Q&A: Primary generalized glucocorticoid resistance (PMC3086527)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3086527/).

## 2. Etiology

**Causal factors.**
- Germline NR3C1 variants (chromosome 5q31.3) reduce the receptor's function.
- Verified: the first familial defect was an abnormal receptor with decreased affinity for cortisol, in Chrousos 1982 ([PMID:6282933](https://pmc.ncbi.nlm.nih.gov/articles/PMC370198)). The father had mineralocorticoid excess with hypertension and hypokalemia. He and his son had high cortisol without Cushing's stigmata.
- Verified: Vingerhoeds 1976 (J Clin Endocrinol Metab 43:1128–1133) was the earlier "Spontaneous hypercortisolism without Cushing's syndrome" report. I did not find its PMID.
- Verified: Hurley 1991 ([PMID:1704018](https://pmc.ncbi.nlm.nih.gov/articles/PMC296359)) found a point mutation in the hormone-binding domain, with a Val 641 mutant receptor. It reports a two- to threefold reduction in receptor-ligand binding affinity in the propositus, and threefold lower dexamethasone binding for the mutant. The D641V shorthand was not confirmed in the retrieved text.
- Verified: Karl et al. 1993 described the first family with glucocorticoid receptor haploinsufficiency, a different mechanism from the affinity defect.
- Genetic heterogeneity: some patients with a similar phenotype have no NR3C1 mutation (PMID:28742501). Other glucocorticoid-signaling factors are suspected, such as co-chaperones and coregulators.

**Risk factors.** Genetic factors are the dominant ones. Environmental risk factors are not established. Related polymorphisms (BclI, N363S, ER22/23EK) modulate sensitivity in the general population and are not causal for this disease (unverified).

**Protective factors.** None known.

**Gene-environment interactions.** Not established for the Mendelian disease. Stress and illness may unmask or worsen it, but I have no source.

## 3. Phenotypes

Presentation depends on the degree of resistance and on the excess of ACTH-driven adrenal steroids. All frequencies below are qualitative and from background knowledge unless tagged. Suggested HPO terms are unverified, so look each up.

| Phenotype | Type | Notes | Suggested HPO (verify) |
|---|---|---|---|
| Hypertension | sign | From mineralocorticoid excess (deoxycorticosterone, corticosterone, cortisol spillover on MR) | Hypertension |
| Hypokalemia, metabolic alkalosis | laboratory | Mineralocorticoid excess | Hypokalemia; Metabolic alkalosis |
| Hyperandrogenism | sign | Acne, hirsutism, male-pattern hair loss, oligo/amenorrhea and anovulation, infertility in women | Hirsutism; Acne; Oligomenorrhea; Infertility |
| Precocious puberty | sign | Children, adrenal androgen excess | Precocious puberty |
| Fatigue | symptom | Reported | Fatigue |
| Elevated ACTH, cortisol, and urinary free cortisol | laboratory | Loss of normal diurnal rhythm preserved, but with high levels and resistance to dexamethasone suppression | Elevated circulating cortisol level; Elevated circulating ACTH level |
| Adrenal hyperplasia / adrenal rest tumors | sign | Chronic ACTH drive; incidentaloma on imaging | Adrenal hyperplasia |
| Male oligospermia | sign | Reported | Oligospermia |
| Hypoglycemia, failure to thrive | sign | Rare, neonatal or severe (unverified) | Hypoglycemia |
| Asymptomatic | | Common in heterozygous relatives | |

**Characteristics.**
- Onset is any age, from neonatal to adult. Severity is variable, even within a family.
- The course is chronic. The disease does not progress in the usual sense, though signs may emerge with age.
- Quality of life: no dedicated instrument studies were found. Hyperandrogenism and infertility have the largest effect.

## 4. Genetic and molecular information

**Causal gene.** NR3C1 (glucocorticoid receptor, GR). Alternative-splicing isoforms are GRα (the active one) and GRβ.

**Variants.**
- The spectrum includes missense variants in the ligand-binding domain (e.g., Val641, as in Hurley 1991), nonsense and frameshift variants causing haploinsufficiency (Karl 1993), splice-site variants, and deletions.
- The Endotext chapter lists the consequences as:
  - reduced affinity to glucocorticoids or to target DNA;
  - inability to transactivate glucocorticoid-responsive genes;
  - slowed cytoplasmic-to-nuclear translocation.
- Dominant-negative effects are described for some missense variants (unverified).
- Classification per ACMG/AMP, population frequencies from gnomAD, and ClinGen validity were not checked. Run `just list-gene-validity` and look for a CGGV record. Do not assign a validity tier yourself.
- Germline origin throughout.

**Modifiers and epigenetics.** Not established. Common GR polymorphisms may modulate expression, and I have no source. No chromosomal abnormality is known as a cause.

## 5. Environmental information

None established as a cause.
- Environmental factors, lifestyle factors, and infectious agents: none.
- Exogenous glucocorticoids and illness-related stress affect the HPA axis and can confound testing.
- The pharmacological dexamethasone suppression test is itself the diagnostic perturbation.

## 6. Mechanism and pathophysiology

**Causal chain.**
1. A germline NR3C1 variant reduces functional GRα. The mechanisms are reduced ligand affinity, reduced DNA binding or transactivation, slowed nuclear translocation, or haploinsufficiency. (Demonstrated: Hurley 1991 and others.)
2. Tissues become partially insensitive to cortisol. Negative feedback at the hypothalamus and pituitary is blunted. (Demonstrated: dexamethasone-suppression resistance.)
3. The result is raised CRH and ACTH, which in turn raise adrenal output. Cortisol rises until it partially overcomes the resistance. (Charmandari 2008, PMID:18319312.)
4. The branch, driven by the raised ACTH, goes two ways:
   - **Branch A, mineralocorticoid.** Excess cortisol, deoxycorticosterone, and corticosterone act at the mineralocorticoid receptor. Hypertension, hypokalemia, and alkalosis follow. Part of this is inferred. Cortisol is normally inactivated in kidney by 11β-HSD2, so saturation of that enzyme is a proposed contributor.
   - **Branch B, androgen.** Adrenal androgens (DHEA, DHEA-S, androstenedione) rise. Hyperandrogenism follows, with acne, hirsutism, oligo-anovulation, and precocious puberty. Androgen excess may also suppress the gonadotropin axis.
5. Chronic ACTH drive causes adrenal hyperplasia. Compensation maintains cortisol-dependent functions in most tissues, so Cushingoid features are absent. (Inferred.)

**Cell types and processes (suggested terms, verify).**
- Cell types: corticotroph (CL), adrenal cortex cell (zona fasciculata, zona reticularis), hypothalamic neurosecretory cell, renal collecting-duct principal cell.
- GO processes: glucocorticoid receptor signaling pathway; glucocorticoid metabolic process; negative regulation of hormone secretion; nuclear translocation of the receptor.
- Cellular components: cytoplasm and nucleus (GR shuttling).

Metabolic, immune, and molecular profiling information is not available; I did not search. Single-cell, spatial, and multi-omics data are not available.

## 7. Anatomical structures affected

- **Primary:** hypothalamus, pituitary, adrenal cortex, and the glucocorticoid-responsive peripheral tissues.
- **Secondary:** kidney (mineralocorticoid effect), skin and pilosebaceous unit, ovary and testis.
- UBERON ids were not checked.
- Lateralization is not applicable.

## 8. Temporal development

- Onset is variable, from infancy to adulthood. Many carriers are asymptomatic and found by family screening.
- Chronic and lifelong. No staging system exists. Spontaneous remission is not described.
- Critical periods: pubertal timing and fertility. I have no source on this.

## 9. Inheritance and population

- **Inheritance.** Both autosomal dominant (haploinsufficiency or dominant-negative variants) and autosomal recessive or homozygous forms (more severe) are described. Both are unverified here. Bind the mode-of-inheritance HPO term after lookup.
- **Penetrance and expressivity.** Incomplete penetrance and variable expressivity are well described.
- **Prevalence.** Very rare. I found no figure, so use `prevalence_class: NOT_YET_DOCUMENTED` or `CASES_IN_LITERATURE` rather than inventing a rate.
- **Population data.** Founder effects, sex ratio, consanguinity, and geographic distribution were not researched. Note that women are often detected earlier because of hyperandrogenism.

## 10. Diagnostics

- **Laboratory.** Elevated 24-hour urinary free cortisol, plasma cortisol, and ACTH, with preserved circadian rhythm. The 1 mg overnight dexamethasone suppression test is abnormal. Elevated adrenal androgens. Hypokalemia. LOINC codes were not checked and must be sourced through `just loinc-seed-cache`.
- **Imaging.** Adrenal CT or MRI shows hyperplasia or adrenal masses.
- **Genetic testing.** Single-gene or panel testing of NR3C1. Exome and genome sequencing are alternatives. Deletion/duplication analysis is a reasonable adjunct.
- **Functional.** Glucocorticoid receptor binding assays in lymphocytes or fibroblasts, and reporter assays, can show reduced function (these are what the original studies used).
- **Differential.** Cushing's syndrome (distinguished by absent Cushingoid features), apparent mineralocorticoid excess, congenital adrenal hyperplasia, PCOS, primary aldosteronism, pseudo-Cushing states, and depression. Hyperandrogenism with high cortisol and no Cushingoid features is the key clue.
- **Screening.** No population screening. Cascade testing of relatives is appropriate.

## 11. Outcome and prognosis

- Life expectancy is probably normal. No survival data were found.
- Complications are hypertension and hypokalemia, infertility, and the effects of long-standing hyperandrogenism. Adrenal incidentalomas occur.
- Treatment-related risk matters: over-treatment with glucocorticoids can produce iatrogenic Cushing's.
- Prognostic factors and biomarkers: not studied.

## 12. Treatment

All of this is unverified; check against the Endotext chapter.

- **Principle.** Suppress the excess ACTH drive with a high dose of a synthetic glucocorticoid with little mineralocorticoid activity, usually dexamethasone. The dose is titrated to the hormone and blood-pressure response, and cortisol alone is not the target.
- **Pharmacotherapy.**
  - Dexamethasone (CHEBI/NCIT agent). NCIT treatment term: Pharmacotherapy `NCIT:C15986`, with `therapeutic_agent`.
  - Mineralocorticoid receptor antagonists (spironolactone, eplerenone) for hypertension and hypokalemia. Spironolactone also has antiandrogen activity.
  - Antiandrogens or combined oral contraceptives for hyperandrogenism in women.
- **Advanced therapeutics.** None. Gene therapy and cell therapy are not applicable.
- **Surgery.** Not indicated except for an adrenal mass.
- **Supportive care.** Fertility counseling and management.
- **Clinical trials.** None identified. I did not search ClinicalTrials.gov.
- **Pharmacogenomics.** Not established.

## 13. Prevention

- Primary prevention is not possible. Genetic counseling and cascade testing of relatives are the main measures.
- Prenatal diagnosis and preimplantation testing are options where the variant is known.
- Prophylaxis: none.
- Tertiary prevention is blood-pressure and potassium monitoring, and avoiding glucocorticoid over-treatment.

## 14. Other species and natural disease

- NR3C1 is conserved across mammals (human NCBITaxon:9606).
- Spontaneous glucocorticoid resistance has been described in New World primates (e.g., squirrel monkey, cotton-top tamarin) with naturally high cortisol and low receptor affinity (unverified, from background knowledge).
- OMIA, breed, and zoonosis data were not searched. They are likely not applicable.

## 15. Model organisms

- All of this is unverified, from background knowledge, and needs a literature search before use.
- The Nr3c1 knockout mouse is lethal at birth from lung failure, so it is not a model of this disease. Heterozygous mice and tissue-specific conditional knockouts, and GR-dimerization-deficient (GR-dim) knock-in mice, are used instead.
- Heterozygous Nr3c1 mice show HPA-axis hyperactivity. Fidelity to the human phenotype (hypertension, hyperandrogenism) is unknown.
- Cell models: patient fibroblasts and lymphocytes, and transfection systems for variant functional assays.
- Resources: MGI, IMPC, ZFIN, and the Alliance of Genome Resources.
- If the entry carries a model, record `modeled_mechanisms` with `fidelity` and `limitations`, and use `HUMAN_MODEL_MISMATCH` if the knockout lethality is relevant.

## Gaps

- Not retrieved: the 2015 Nicolaides PMID, the Vingerhoeds PMID, the Karl 1993 PMID, any quantitative frequencies, treatment evidence, and all ontology identifiers.
- Before curation, run the GeneReviews check (`just check-genereviews`) to see whether a chapter exists. Also check whether a ClinGen assertion exists for NR3C1.

## Sources

- [Glucocorticoid Resistance, PMID 31588529](https://pubmed.ncbi.nlm.nih.gov/31588529/)
- [Hormones (Athens) review, PMID 28742501](https://pubmed.ncbi.nlm.nih.gov/28742501/)
- [Chrousos 1982, PMC370198](https://pmc.ncbi.nlm.nih.gov/articles/PMC370198)
- [Hurley 1991, PMC296359](https://pmc.ncbi.nlm.nih.gov/articles/PMC296359)
- [Q&A: Primary generalized glucocorticoid resistance, PMC3086527](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3086527/)
- [Endotext: primary generalized glucocorticoid resistance syndrome](https://www.endotext.org/wp-content/uploads/pdfs/primary-generalized-glucocorticoid-resistance-syndrome.pdf)
- [Endotext: glucocorticoid resistance syndromes and states](https://www.endotext.org/wp-content/uploads/pdfs/glucocorticoid-resistance-syndromes-and-states.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

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