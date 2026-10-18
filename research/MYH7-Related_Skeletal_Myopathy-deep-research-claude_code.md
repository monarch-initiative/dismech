---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T23:30:47.051068'
end_time: '2026-10-15T23:32:00.847251'
duration_seconds: 73.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: MYH7-Related Skeletal Myopathy
  mondo_id: MONDO:0008050
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
  total_cost_usd: 0.8048261000000001
  session_id: 5094b216-d64b-5a31-b45d-f4070926f044
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 6
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.3.0
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
- **Disease Name:** MYH7-Related Skeletal Myopathy
- **MONDO ID:** MONDO:0008050 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MYH7-Related Skeletal Myopathy** covering all of the
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

# MYH7-Related Skeletal Myopathy: Research Report

**Provenance of this report.** I ran three web searches. They returned secondary sources and PMC links, but no abstracts and almost no PMIDs. Claims backed by a retrieved source carry a link. Everything else is background knowledge and is marked **[unverified]**. Per this repository's rules, run `just fetch-reference` on any PMID before using it, and look up every ontology CURIE with OAK or the term caches before binding it. The CURIEs below were not looked up. **I give no PMIDs and no exact-quote snippets, because I could not verify any.** The few paper citations that follow are PMC or journal links I did retrieve.

---

## 1. Disease Information

**Overview.** MYH7-related skeletal myopathy is an umbrella for autosomal dominant (rarely recessive) skeletal muscle disease caused by variants in *MYH7*. This gene encodes β-cardiac/slow myosin heavy chain (MyHC-I), which is expressed in the heart and in type I skeletal muscle fibres. The GeneReviews chapter of this name (authors Lamont and Laing) lists these related phenotypes ([GTR/MedGen C4552004](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004); [NORD](https://rarediseases.org/mondo-disease/myh7-related-skeletal-myopathy/)):
- Laing distal myopathy (MPD1)
- Myosin storage myopathy (hyaline body myopathy)
- Scapuloperoneal myopathy
- Limb-girdle-type presentations, and congenital/axial forms with neck rigidity

**Identifiers.**
- MONDO:0008050, as supplied in the template. I did not verify it.
- OMIM MPD1 is 160500 **[unverified]**.
- Orphanet and ICD codes were not retrieved.
- HGNC symbol: MYH7. The repository form for the HGNC CURIE is lowercase `hgnc:`. The ID was not looked up.

**Synonyms.** Laing distal myopathy and myopathy, distal, type 1 (MPD1) are listed in MedGen/GTR. Myosin storage myopathy is also listed there as a related name ([GTR](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004)).

**Data provenance.** The information comes from aggregated disease-level resources and family and cohort series, not from EHR data.

**Lumping and splitting (for the curator).** MYH7 disease also includes cardiomyopathy: hypertrophic, dilated and LVNC. Skeletal myopathy and cardiomyopathy usually segregate by variant region but sometimes overlap. The decision-register granularity rules should be checked before choosing between a single entry and `has_subtypes`. Candidate subtypes are Laing distal myopathy, myosin storage myopathy, scapuloperoneal myopathy, and the recessive form.

---

## 2. Etiology

- **Cause.** The cause is a heterozygous germline *MYH7* missense or in-frame variant, mostly in the rod (tail) domain, with a few in the head or other regions. The GeneReviews testing strategy centres on exons 30–40, which catches most Laing cases ([search summary of GeneReviews](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004)). One exon 14 variant has been linked to a Laing-like phenotype with cardiomyopathy, per the same summary.
- **Overlap with cardiac disease.** MYH7 variants causing familial hypertrophic cardiomyopathy are spread across nearly the whole molecule. They overlap the regions associated with Laing distal myopathy and myosin storage myopathy (same source).
- **Risk and protective factors.** No environmental or lifestyle risk factors are established. No protective or modifier alleles are established. Gene–environment interactions are not applicable or not described.
- **Mosaicism and de novo variants.** De novo variants are common in sporadic cases. Germline mosaicism is possible **[unverified]**.

---

## 3. Phenotypes

Ontology suggestions below are HPO labels from memory and need lookup before use.

| Phenotype | Notes | HPO suggestion |
|---|---|---|
| Distal limb weakness | The most common pattern. In Laing myopathy it starts in the ankle dorsiflexors and great toes, then reaches the finger extensors. Onset is usually before age 5. Life expectancy is normal ([GeneReviews summary](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004)). | Distal muscle weakness (HP:0002460) |
| Foot drop / steppage gait | Follows from tibialis anterior weakness | Foot dorsiflexor weakness; Steppage gait |
| Scapuloperoneal weakness | Shoulder-girdle and peroneal involvement | Scapuloperoneal weakness |
| Neck flexor weakness and neck extensor contracture, axial weakness | Cervical rigidity is a recognised axial form ([2016 report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982306/)). | Neck flexor weakness; Limited neck range of motion |
| Congenital or early infantile weakness | Half of 21 Italian cases had congenital or early infantile weakness, mostly distal. Later-onset cases were mostly proximal (2016 Italian cohort, as summarised in search results). | Neonatal hypotonia |
| Cardiomyopathy | 14% of a 57-patient French cohort had dilated, hypertrophic or LVNC cardiomyopathy ([French cohort](https://integ04-cnspfv.archimed.fr/doc/OAI_1/oai-HAL-hal-04761813v1)). | Cardiomyopathy |
| Elevated CK | Typically normal or mildly raised **[unverified]**. | Elevated serum creatine kinase |

**Phenotype distribution.** In the French multicentre cohort of 57 patients, distal myopathy accounted for 70%, scapuloperoneal for 23%, and axial with cervical rigidity for 7% ([French cohort](https://integ04-cnspfv.archimed.fr/doc/OAI_1/oai-HAL-hal-04761813v1)). The cohort's publication date and journal were not confirmed.

**Penetrance and expressivity.** These are variable, even within families ([2016 report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982306/)).

**Quality-of-life data.** I did not find any.

---

## 4. Genetic/Molecular Information

- **Gene and protein.** *MYH7*, at chromosome 14q11.2 **[unverified]**, encodes β-myosin heavy chain.
- **Variant class.** Variants are mostly missense and in-frame deletions or insertions in the rod domain, including:
  - Proline substitutions in the coiled-coil rod, such as p.Leu1793Pro, p.Arg1500Pro, p.Arg1434Pro and p.Ala1437Pro. The last two are from the [2016 report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982306/). The R1500P variant appears in the [2024 mouse study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11060730/). The others are from memory **[unverified]**.
  - The recurrent p.Lys1729del, studied in flies (see the Model Organisms section).
  - Myosin storage myopathy variants, notably p.Arg1845Trp and p.Leu1793Pro, in the distal rod and "assembly competence domain" **[unverified]**.
- **Functional consequence.** The mutant protein is expressed and incorporated. This is dominant-negative or altered-function, not simple loss of function (see Mechanism).
- **Modifier genes and epigenetics.** None established.
- **Recessive form.** PanelApp lists both dominant and recessive myosin storage myopathy under MYH7 ([PanelApp AU](https://panelapp-aus.org/panels/3071/gene/MYH7/)).
- **Allele frequency and ACMG classification.** I did not retrieve these. Check ClinVar, ClinGen and gnomAD.
- **Chromosomal abnormalities.** None are described.

---

## 5. Environmental Information

No environmental, lifestyle or infectious factors are established for this disease.

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. A heterozygous rod-domain *MYH7* variant, often a proline substitution that disrupts the coiled-coil, arises in the germline.
2. The mutant β-myosin rod has altered coiled-coil stability and thick-filament assembly properties. In transfected non-muscle cells, proline substitutions impaired myosin self-assembly but did not stop the mutant molecules entering sarcomeres ([2016 report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982306/)).
3. The mutant protein is expressed in slow type I fibres, including the tibialis anterior. This tissue pattern probably explains the selective distal weakness; the link is inferred, not demonstrated **[unverified]**.
4. Mutant myosin changes motor and thick-filament function. In a Laing R1500P mouse model, the mutation **impaired motor activity despite lying in the structural rod domain**. Muscles showed fatigue and weakness, faster actin–myosin detachment, and a shift of heads toward the disordered relaxed state. This implies hypercontractility and higher ATP use ([JCI 2024, Laing distal myopathy–associated proline substitution](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11060730/)).
5. Chronic energetic and structural stress leads to type I fibre atrophy and myopathic change. Some forms show hyaline or myosin storage bodies. This step is **inferred** from the general MYH7 literature **[unverified]**.
6. The result is progressive, selective distal weakness. Many patients stay ambulant and have a normal lifespan.

**Branches.** Variants in the head or other regions drive cardiomyopathy through sarcomere hypercontractility. Some variants affect both heart and skeletal muscle.

**Open question.** Assembly defect versus altered cross-bridge activity as the primary driver is unresolved. A fly model of the recurrent K1729del variant found structural and functional phenotypes and a modifier mechanism, but the data were confounded and no consensus has emerged on mechanism (search summary; fly paper not retrieved).

### Suggested ontology terms (not verified, look up before binding)
- **GO terms.** Candidates are myosin filament assembly; sarcomere organization; striated muscle contraction; and muscle myosin complex.
- **Cell types.** Candidates are type I skeletal muscle fibre ("slow muscle cell"), skeletal muscle satellite cell, and cardiac muscle cell.
- **Anatomy.** Tibialis anterior, anterior compartment of the leg, and neck muscles.
- **Subcellular.** A band, sarcomere, thick filament.

### Molecular profiling
I found no transcriptomic, proteomic or other omics data in my searches.

---

## 7. Anatomical Structures Affected

- **Primary.** Skeletal muscle, especially distal lower-limb muscles (anterior compartment, great toe extensors), then finger extensors ([GeneReviews summary](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004)).
- **Secondary.**
  - Scapuloperoneal and axial neck muscles ([French cohort](https://integ04-cnspfv.archimed.fr/doc/OAI_1/oai-HAL-hal-04761813v1)).
  - Heart, in a minority of patients (14% in the French cohort).
- **Tissue.** Muscle with a type I fibre predominance of involvement.
- **Subcellular.** The sarcomeric thick filament.
- **Lateralisation.** Usually symmetric **[unverified]**.

---

## 8. Temporal Development

- **Onset.** Laing distal myopathy usually begins before age 5. Myosin storage myopathy and scapuloperoneal forms range from congenital to adult onset. Italian cohort data show half of patients with congenital or early infantile weakness.
- **Progression.** Slow. Many patients remain ambulant, and life expectancy is normal in Laing distal myopathy (GeneReviews summary). Proximal and axial involvement can appear later **[unverified]**.
- **Remission.** None is known.
- **Critical windows.** None are described.

---

## 9. Inheritance and Population

- **Inheritance.** Autosomal dominant is the usual pattern. Autosomal recessive myosin storage myopathy is also listed ([PanelApp AU](https://panelapp-aus.org/panels/3071/gene/MYH7/)).
- **Penetrance and expressivity.** Variable ([2016 report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982306/)).
- **De novo cases.** These occur frequently **[unverified]**.
- **Prevalence.** I did not find a reliable figure. Check the Orphanet epidemiology table for Laing distal myopathy.
- **Founder effects, sex ratio and geographic distribution.** Not retrieved.
- **Anticipation.** Not applicable.

---

## 10. Diagnostics

- **Genetic testing.** The GeneReviews strategy is to sequence *MYH7* exons 30–40 first (covers most Laing cases), then broaden to the full gene or to a myopathy gene panel or exome ([GeneReviews summary](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004)).
- **Muscle biopsy.** Findings are typically mild myopathic change with type I fibre abnormalities, and in myosin storage myopathy subsarcolemmal hyaline bodies reactive for slow myosin **[unverified]**.
- **Imaging.** Muscle MRI shows a selective pattern, with tibialis anterior involvement early **[unverified]**.
- **EMG and CK.** Myopathic changes; CK normal to mildly raised **[unverified]**.
- **Cardiac evaluation.** ECG and echocardiography are recommended because of cardiomyopathy risk ([French cohort](https://integ04-cnspfv.archimed.fr/doc/OAI_1/oai-HAL-hal-04761813v1)).
- **Differential diagnosis.** Distal myopathies such as GNE, DYSF and MATR3 disease, Charcot–Marie–Tooth disease and other hereditary neuropathies (neurophysiology distinguishes these), FSHD, and other causes of scapuloperoneal syndromes.
- **Screening.** Cascade testing of relatives is appropriate.

---

## 11. Outcome / Prognosis

- Laing distal myopathy usually has a normal life expectancy ([GeneReviews summary](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004)).
- Disability is generally slowly progressive. Severe early-onset forms are described.
- Cardiac involvement is the main risk to prognosis. Population-scale MYH7 cardiomyopathy data show 5-year adverse event rates of about 11.6% in DCM (JACC 2022 international cohort, via search summary). These are cardiomyopathy data, not skeletal myopathy data.
- Quality-of-life instruments and survival statistics for skeletal myopathy were not found.

---

## 12. Treatment

- **No disease-modifying therapy exists.** Care is supportive.
  - Physiotherapy and rehabilitation. Candidate NCIT terms, to be looked up: Physical Therapy (NCIT:C15302, per this repository's own list), and Rehabilitation (NCIT:C15315, same list).
  - Orthoses, such as ankle-foot orthoses, for foot drop.
  - Orthopaedic surgery for contractures or deformities. NCIT:C16186 is listed in the repository's guide.
  - Cardiac surveillance and standard cardiomyopathy therapy.
- **Experimental approaches.** Allele-specific silencing and gene editing for MYH7 are in preclinical development **[unverified]**. I found no registered trials, so no NCT IDs are given.
- **Pharmacogenomics.** Not applicable.
- **Myosin modulators.** Cardiac myosin inhibitors such as mavacamten are used in obstructive HCM. They have no established role in skeletal myopathy. The 2024 finding of altered motor function in a Laing model suggests the idea is worth testing; this is my inference, not a published claim.

---

## 13. Prevention

- Genetic counselling covers dominant inheritance with a 50% recurrence risk, variable expressivity, and de novo possibility **[unverified]**.
- Prenatal and preimplantation testing are options for families with a known variant.
- Cascade testing and cardiac surveillance of carriers.
- No primary prevention exists.

---

## 14. Other Species / Natural Disease

- *MYH7* is conserved. The ortholog in other species has not been checked against NCBI Gene.
- I did not search OMIA, so I cannot state whether natural disease is recorded in other species.
- Zoonotic potential: not applicable.

---

## 15. Model Organisms

| Model | Details | Source |
|---|---|---|
| Mouse, R1500P knock-in | Described as the first mouse model of Laing distal myopathy. Motor activity impaired; fatigue and weakness; faster actin–myosin detachment; shift to the disordered relaxed head state; hypercontractility and higher ATP use. | [JCI 2024, J Clin Invest 134(9)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11060730/). The search result suggested PMID 38690726 but did not state it, so confirm before use. |
| *Drosophila*, K1729del | Structural and functional phenotypes plus a modifier mechanism. The authors note confounds, and no consensus on mechanism. | Search summary only. The paper was not retrieved. |
| Transfected non-muscle cells | Rod proline substitutions impair myosin self-assembly but are still incorporated into sarcomeres. | [2016 report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982306/) |

**Fidelity and limits.** The mouse model reproduces fatigue, weakness and altered myosin function. Whether it reproduces the selective distal pattern of the human disease was not established in the material I retrieved. For `evidence_source`, grade the mouse paper `MODEL_ORGANISM` and the cell-culture work `IN_VITRO`.

---

## Gaps and recommended next steps

1. Fetch the primary papers for the cited cohorts (French multicentre, Italian 2016, JACC 2022) and obtain verified PMIDs.
2. Read the full GeneReviews chapter, since my access was only through search summaries. It is the mandatory phenotype baseline. Run `just check-genereviews` on the entry.
3. Check Orphanet and ClinGen records for MYH7, which I did not reach. They are needed for gene-disease validity, prevalence and frequency data.
4. Verify every HPO, GO, CL, UBERON, NCIT and HGNC identifier, because all were suggested without lookup.

## Sources

- [MYH7-related skeletal myopathy, GTR/MedGen](https://https.ncbi.nlm.nih.gov/gtr/conditions/C4552004)
- [MYH7-related skeletal myopathy, NORD](https://rarediseases.org/mondo-disease/myh7-related-skeletal-myopathy/)
- [PanelApp Australia: MYH7](https://panelapp-aus.org/panels/3071/gene/MYH7/)
- [Laing distal myopathy–associated proline substitution in the β-myosin rod perturbs myosin cross-bridging activity (JCI 2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11060730/)
- [Two novel MYH7 proline substitutions cause Laing distal myopathy-like phenotypes (2016)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982306/)
- [MYH7-related myopathies: French multicentre cohort](https://integ04-cnspfv.archimed.fr/doc/OAI_1/oai-HAL-hal-04761813v1)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
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