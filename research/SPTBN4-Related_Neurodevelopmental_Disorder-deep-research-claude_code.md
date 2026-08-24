---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-03T00:24:18.886387'
end_time: '2026-08-03T00:30:14.926996'
duration_seconds: 356.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SPTBN4-Related Neurodevelopmental Disorder
  mondo_id: ''
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 15
  num_turns: 33
  total_cost_usd: 2.2604738999999996
  session_id: ccfe4e45-02a4-514e-bba5-3af1e8db647b
  stop_reason: end_turn
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SPTBN4-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SPTBN4-Related Neurodevelopmental Disorder** covering all of the
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

# SPTBN4-Related Neurodevelopmental Disorder: Comprehensive Research Report

## 1. Disease Information

**Overview:** SPTBN4-related neurodevelopmental disorder — officially designated **"Neurodevelopmental disorder with hypotonia, neuropathy, and deafness" (NEDHND)** — is an ultra-rare autosomal recessive disorder caused by biallelic loss-of-function or damaging variants in *SPTBN4*, the gene encoding βIV-spectrin. The condition is characterized by congenital hypotonia, profound global developmental delay/intellectual disability, axonal motor neuropathy, and — in a subset of patients — central (retrocochlear) deafness and epilepsy. Mechanistically, βIV-spectrin is a core cytoskeletal scaffold at the axon initial segment (AIS) and nodes of Ranvier, and its loss disrupts clustering of voltage-gated ion channels required for normal neuromuscular and auditory signal transmission (PMID:28540413; PMID:29861105).

**Key identifiers:**
- **OMIM:** #617519 (NEDHND, phenotype); *606214 (SPTBN4, gene)
- **MONDO:** MONDO:0060496
- **MedGen:** C4479603
- **Gene:** SPTBN4 (HGNC), chromosome 19q13.2 (GRCh38: chr19:40,466,241–40,576,464)
- **Orphanet:** listed under Orphanet gene-disease associations for SPTBN4 (Orphanet code for the rare-disease entity; see Orphanet SPTBN4 page)
- **ICD-10/ICD-11:** no disease-specific code exists; typically coded under nonspecific hereditary motor/sensory neuropathy or developmental disorder codes
- **MeSH:** no dedicated MeSH heading; indexed under "Muscular Hypotonia," "Peripheral Nervous System Diseases," "Intellectual Disability"

**Synonyms/alternative names:**
- NEDHND (official OMIM abbreviation)
- βIV-spectrinopathy / β-IV spectrinopathy
- SPTBN4 disorder (GeneReviews title, PMID:32672909)
- Congenital myopathy with neuropathy and central deafness (early descriptive name from the first reported case, PMID:28540413)

**Evidence base:** Information is derived almost entirely from **aggregated case reports/case series** (individual published families) rather than large-cohort epidemiological or EHR-derived resources, reflecting the disease's extreme rarity. As of the most recent natural history study (2025), only **38 patients** have been reported worldwide (PMC12335179).

Sources: [OMIM #617519](https://omim.org/entry/617519), [OMIM *606214](https://omim.org/entry/606214), [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/), [MalaCards SPTBN4](https://www.malacards.org/card/sptbn4_disorder)

---

## 2. Etiology

**Disease causal factors:** NEDHND is a monogenic, purely genetic disorder. It is caused by **biallelic (homozygous or compound heterozygous) pathogenic/loss-of-function variants in *SPTBN4*** — there is no known environmental, infectious, or acquired contribution. No multifactorial or polygenic component has been described.

**Genetic risk factors:**
- **Causal variants:** truncating (nonsense, frameshift, splice-site) and missense variants throughout *SPTBN4*, predominantly affecting the spectrin-repeat rod domain, the pleckstrin homology (PH) domain (which mediates phosphoinositide binding), and the ankyrin-binding domain.
- **Consanguinity** is a major risk factor: the natural history study found **66% of the 38 reported cases had documented parental consanguinity** (PMC12335179), consistent with the fully recessive inheritance and generally private (non-recurrent) nature of most variants.
- No modifier genes have been formally established, though partial functional compensation by paralogous cytoskeletal proteins (ankyrin-R, βI-spectrin) is documented mechanistically (see Mechanism section) and may modulate phenotype severity.
- No GWAS or susceptibility-locus data exist (disease is fully penetrant Mendelian, not complex).

**Environmental/lifestyle risk factors:** None established or plausible for this cytoskeletal structural-protein disorder.

**Protective factors:** None identified. Heterozygous carriers (parents/obligate carriers) are asymptomatic with no reported health effects (GeneReviews, PMID:32672909).

**Gene-environment interactions:** None described; the disorder behaves as a classic monogenic structural/cytoskeletal disease without documented environmental modulation.

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/), [Natural history study, PMC12335179](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335179/)

---

## 3. Phenotypes

### Core phenotype frequencies (GeneReviews cohort, n=14 from 12 families; PMID:32672909)

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Congenital hypotonia | 14/14 (100%) | HP:0008936 (Hypotonia, congenital) |
| Neuromuscular weakness | 14/14 (100%) | HP:0003324 (Generalized muscle weakness) |
| Areflexia/axonal neuropathy | 13/14 (93%) | HP:0001284 (Areflexia); HP:0000762 (Axonal loss) |
| Developmental delay/intellectual disability | 13/14 (93%) | HP:0001263 (Global developmental delay); HP:0001249 (Intellectual disability) |
| Feeding difficulties | 9/14 (64%) | HP:0011968 (Feeding difficulties) |
| Respiratory difficulties | 8/14 (57%) | HP:0002093 (Respiratory insufficiency) |
| Visual impairment (cortical) | 6/14 (43%) | HP:0100704 (Cerebral visual impairment) |
| Joint contractures | 5/14 (36%) | HP:0001371 (Flexion contracture) |
| Seizures | 5/14 (36%) | HP:0001250 (Seizure); HP:0011097 (Epileptic spasms) |
| Hearing loss (auditory neuropathy, central) | 4/14 (29%) | HP:0000407 (Sensorineural hearing impairment); more precisely HP:0000375-adjacent central auditory processing deficit |

### Larger, multinational natural-history cohort (n=38; PMC12335179, 2025) — broader phenotype spectrum:
- Muscle weakness, motor disability, hypotonia, speech delay: near-universal
- Ocular abnormalities (nystagmus, visual impairment to complete blindness): **43%**
- Scoliosis, deafness, seizures: each **~21–25%**
- GI problems (feeding difficulties, dysphagia, gastrostomy dependence): **54%**
- Respiratory difficulties (recurrent pneumonia; 2 progressed to restrictive lung disease): **61%**
- **Ataxia**: newly reported in 2 Saudi patients — first human report of this feature, previously only seen in the mouse model (see Model Organisms section)
- Dysmorphic features/choreoathetosis reported in individual case reports (PMC8298470)

### Phenotype characteristics
- **Onset:** Congenital-to-early-infantile in most patients; among 29 patients with documented data, 15 presented at birth; overall range of presentation 13 months–15 years in some series (PMC12335179).
- **Severity:** Variable, from profound (non-ambulatory, non-verbal, ventilator-dependent) to a milder phenotype restricted to axonal neuropathy without intellectual disability (PMID:31857255 — two siblings with a homozygous splice variant had myopathic facies with ptosis and axonal neuropathy but **no** seizures, feeding difficulties, respiratory difficulties, or intellectual disability).
- **Progression:** Generally "static or slow progression" rather than a classically degenerative course, though hypotonia may evolve into appendicular hypertonia/spasticity with axial hypotonia persisting (GeneReviews).
- **Frequency variability:** Hearing loss and seizures are present in only a minority (~25–36%), making them "supportive" rather than obligate diagnostic features — an important point for differentiating milder from more severe presentations.

### Quality of life impact
No formal EQ-5D/SF-36/PROMIS studies exist for this ultra-rare disease. Qualitatively, the disorder carries very high care burden: most patients are non-ambulatory, non-verbal, require tube feeding and often ventilatory/BiPAP support, and need lifelong caregiver-dependent care (GeneReviews Management table; PMC12335179).

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/), [Natural history study (Orphanet J Rare Dis), PMC12335179](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335179/), [PMID:31857255 (axonal neuropathy without ID)](https://pubmed.ncbi.nlm.nih.gov/31857255/)

---

## 4. Genetic/Molecular Information

**Causal gene:** *SPTBN4* (HGNC symbol; OMIM *606214), encoding **spectrin beta, non-erythrocytic 4 (βIV-spectrin)**, chr19q13.2.

**Gene function/isoforms:** *SPTBN4* has multiple transcript variants producing distinct protein isoforms, notably a full-length **288 kDa isoform** (βIVΣ1, the AIS/nodal isoform) and a shorter **72 kDa isoform** expressed in other tissues (fibroblasts); loss of both was demonstrated in the index patient by Western blot (PMID:28540413).

**Pathogenic variant spectrum:**
- Across the largest natural-history cohort, **31 different SPTBN4 variants** have been identified among the 38 reported patients, spanning **missense, nonsense, splice-site, deletion, insertion, duplication, and even tandem-repeat/multi-exon deletion** variant classes (PMC12335179).
- Representative variants from the literature:
  - c.1597C>T; p.(Gln533*) — first reported homozygous nonsense variant, Kurdish consanguineous family (PMID:28540413)
  - c.3820G>T (p.Glu1274*), c.2709G>A (p.Trp903*), c.7453delG (p.Ala2485Leufs*31), c.1511G>A (p.Arg504Gln), c.1813C>T (p.Gln605*) — from the AJHG cohort (PMID:29861105)
  - c.1799_1800delGC (frameshift) — three affected siblings, consanguineous family, axonal neuropathy with intellectual disability (ScienceDirect 2024)
  - c.2265G>A (p.Trp755*) — novel nonsense variant reported in the 2025 natural history study (PMC12335179)
  - A multi-exon deletion (structural/CNV-type variant) reported among novel bi-allelic variants (PMC8298470, EJHG 2021)
- **Zygosity:** Homozygous variants predominate (consistent with high consanguinity rates); compound heterozygosity is less common (4/38 patients in the largest series; 2/6 in the AJHG cohort).
- **Variant classification (ACMG/AMP):** Most reported variants are classified pathogenic/likely pathogenic based on null-variant type, absence/rarity in gnomAD, and segregation with disease; several missense variants (e.g., p.Arg504Gln) required functional validation (AIS mislocalization, PIP-binding assays) to support pathogenicity (PMID:29861105).
- **Population frequency:** Individual pathogenic variants are typically **absent or exceedingly rare in gnomAD** — e.g., a pathogenic homozygous missense variant reported in one patient was entirely absent from gnomAD (EJHG 2021). Formal gene-level LOEUF/constraint statistics specific to *SPTBN4* were not identified in general search resources; direct gnomAD browser query would be needed for exact pLI/LOEUF values.
- **Origin:** All reported variants are **germline**; no somatic *SPTBN4* variants or associated malignancy have been described.

**Functional consequences (from AJHG functional studies, PMID:29861105):**
- Truncating variants (p.Gln605*, p.Trp903*, p.Glu1274*) **fail to localize to the AIS** when expressed in cultured neurons, unlike wild-type βIVΣ1, which is "highly enriched at AISs, where it co-localized with AnkG."
- The PH-domain frameshift variant p.Ala2485Leufs*31 **fails to bind any phosphoinositides** on PIP-strip assays (wild-type binds PI(3,5)P2, PI(4,5)P2, PI(3,4,5)P3 strongly), implicating loss of membrane-lipid anchoring as a distinct pathogenic mechanism.
- Some missense variants (p.Arg504Gln, p.Arg2435Cys) retain AIS localization, suggesting these act through a different (e.g., partial loss-of-function or altered channel-clustering capacity) mechanism than complete mislocalization.
- Overall mechanism: **loss of function** — reduced/absent βIV-spectrin protein or disrupted AIS/nodal targeting — is the predominant disease mechanism; no gain-of-function or dominant-negative variants have been reported (consistent with strictly recessive inheritance).

**Modifier genes:** None formally established in humans, though the paralogous **ankyrin-R (ANK1)** and **βI-spectrin (SPTBN1)** proteins partially compensate for loss of AnkG/βIV-spectrin at nodes for **sodium** channel clustering (but not potassium channel clustering) in mouse models — a mechanistic compensation pathway rather than a validated human modifier locus (PMID:29861105).

**Epigenetic information:** No epigenetic (DNA methylation, histone modification, chromatin) data specific to *SPTBN4*/NEDHND were identified in the literature search.

**Chromosomal abnormalities:** The disease is caused by point mutations/small indels and occasionally larger structural variants (multi-exon deletions) within *SPTBN4*; no recurrent aneuploidy, translocation, or contiguous-gene deletion syndrome mechanism has been reported.

Sources: [PMID:28540413 (Knierim et al. 2017, Hum Genet)](https://pubmed.ncbi.nlm.nih.gov/28540413/), [PMID:29861105 / PMC5992132 (Wang et al. 2018, AJHG)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5992132/), [PMC8298470 (EJHG 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8298470/), [PMC12335179 (2025 natural history)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335179/)

---

## 5. Environmental Information

No environmental toxins, occupational exposures, lifestyle factors, or infectious agents have been implicated in NEDHND causation or modification — this is a purely monogenic structural-cytoskeletal disorder. Not applicable.

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)

1. **Molecular trigger:** Biallelic loss-of-function (or damaging missense) variants in *SPTBN4* → absent or non-functional βIV-spectrin protein (loss of the 288 kDa AIS/nodal isoform and/or the 72 kDa isoform).
2. **Cytoskeletal scaffold failure:** βIV-spectrin normally forms, together with **ankyrin-G (AnkG)**, a periodic submembranous cytoskeletal lattice at the **axon initial segment (AIS)** and **nodes of Ranvier**, cross-linking actin filaments to the plasma membrane and anchoring ion channels and adhesion molecules (neurofascin-186, NrCAM) at these excitable domains (Wikipedia SPTBN4 summary; PMID:17548513).
3. **Loss of ion-channel clustering:** Without βIV-spectrin, **voltage-gated sodium channels (Nav)** fail to cluster properly at nodes/heminodes, and — critically — **KCNQ2/KCNQ3 potassium channels are essentially absent** from nodes, since the alternative ankyrin-R/βI-spectrin compensatory complex (which partially rescues Na+ channel clustering) **cannot rescue K+ channel clustering** (PMID:29861105). Human nerve biopsy from a p.Trp903* patient showed nearly undetectable nodal βIV-spectrin, weak Na+ channel labeling, and no detectable nodal KCNQ2.
4. **Impaired axonal conduction:** Disrupted saltatory conduction and impaired action-potential fidelity produce **axonal motor neuropathy** (clinically manifesting as areflexia/hyporeflexia and weakness) and, in the auditory brainstem, **impaired Nav clustering at auditory nerve heminodes** causes elevated action-potential threshold, increased conduction failures during high-frequency spike trains, and slowed central conduction — the basis of the **central (retrocochlear) deafness** phenotype, with normal cochlear function (PMID:35393465, PMC8991253).
5. **Downstream clinical manifestation:** The combination of impaired peripheral/axonal signaling (neuropathy, weakness, hypotonia), impaired central auditory processing (deafness without cochlear pathology), and disrupted AIS function in cortical/cerebellar neurons (contributing to intellectual disability, seizures, ataxia in some patients) together produce the multisystem neurodevelopmental phenotype.

### Molecular pathways / cellular processes
- **Cytoskeleton organization** (GO:0007010) — spectrin-actin membrane skeleton assembly
- **Voltage-gated sodium channel clustering** and **potassium channel clustering** at nodes of Ranvier/AIS (GO:1990138 axon guidance-adjacent; specific GO terms: "sodium channel regulator activity," "ankyrin binding")
- **Axonogenesis / axon guidance**
- No classical signaling cascade (Wnt/MAPK/mTOR/PI3K-AKT) is directly implicated; this is a **structural scaffold disorder**, not a signaling-pathway disorder.

### Protein dysfunction
- **Loss of function** is the dominant mechanism: complete absence of protein (nonsense/frameshift/large deletion variants), failure of AIS/nodal localization despite protein expression (some truncating variants), or failure of phosphoinositide-membrane binding via the PH domain (p.Ala2485Leufs*31) that likely secondarily disrupts membrane anchoring.
- Domains affected: spectrin-repeat rod domain (structural scaffolding/dimerization), ankyrin-binding domain (AnkG interaction), pleckstrin homology (PH) domain (phosphoinositide/membrane binding).

### Tissue damage mechanisms
- Not primarily an oxidative-stress/fibrotic/necrotic process; rather a **developmental/functional excitable-membrane-domain assembly defect**. Muscle biopsy findings (fiber-type disproportion, fiber atrophy predominantly type 1) likely reflect secondary/neurogenic changes from axonal motor neuropathy rather than primary muscle pathology (PMID:28540413; PMC12335179 — "muscle fiber atrophy...more than fiber atrophy type 2").

### Biochemical abnormalities
- Absent nodal/heminodal Nav channel clustering; **absent nodal KCNQ2/KCNQ3 K+ channel clustering** (the key differentiator vs. simple AnkG loss, since Na+ clustering can be partially rescued by AnkR/βI-spectrin but K+ clustering cannot) (PMID:29861105).

### Molecular profiling / advanced technologies
No transcriptomic (GEO/ArrayExpress), proteomic, metabolomic, or single-cell/spatial transcriptomic datasets specific to human NEDHND tissue were identified. Functional characterization has relied on: patient fibroblast/nerve/muscle biopsy immunohistochemistry and Western blot, heterologous expression in cultured neurons (AIS localization assays), PIP-strip lipid-binding assays, and mouse genetic models (see Model Organisms).

### Cell types and biological processes involved (suggested ontology terms)
- **Cell types (CL):** motor neuron (CL:0000100), Schwann cell (CL:0002573), skeletal muscle fiber (CL:0000188), spiral ganglion neuron / auditory brainstem neuron (bushy cell, CL:0000099-adjacent), Purkinje cell (for cerebellar/ataxia phenotype, CL:0000121)
- **Biological processes (GO):** GO:0007010 cytoskeleton organization; sodium channel clustering (part of "establishment of protein localization to plasma membrane," GO:0090150); axonogenesis (GO:0007409)
- **Anatomical localization (UBERON):** axon initial segment, node of Ranvier, peripheral nerve (UBERON:0001021), skeletal muscle organ (UBERON:0001134), auditory brainstem/cochlear nucleus (UBERON:0002047-adjacent), cerebellum (UBERON:0002037)

Sources: [PMID:29861105 / PMC5992132 (AJHG 2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5992132/), [PMID:35393465 (Sci Rep 2022, heminode Nav clustering)](https://pubmed.ncbi.nlm.nih.gov/35393465/), [PMID:11528393 (Parkinson et al. 2001, Nat Genet, quivering mouse)](https://pubmed.ncbi.nlm.nih.gov/11528393/), [PMID:17548513 (AnkG-dependent AIS/node assembly)](https://pubmed.ncbi.nlm.nih.gov/17548513/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** peripheral nervous system (motor axons), central nervous system (brain — cortex, cerebellum, auditory brainstem), skeletal muscle (secondary/neurogenic involvement).
- **Secondary:** respiratory system (restrictive lung disease/respiratory failure from neuromuscular weakness — leading cause of the 2 reported deaths), gastrointestinal system (dysphagia, feeding difficulties), musculoskeletal system (scoliosis, joint contractures), visual system (cortical visual impairment, nystagmus).
- **Body systems:** nervous, musculoskeletal, respiratory, digestive, and (in a subset) auditory/sensory systems.

**Tissue and cell level:**
- Peripheral motor axons and their Schwann cell-associated nodes of Ranvier
- Central auditory pathway axons/heminodes (auditory brainstem, e.g., endbulb of Held-type terminals studied in mouse models)
- Cerebral cortical and cerebellar (Purkinje) neurons — axon initial segments
- Skeletal muscle fibers (secondary neurogenic atrophy pattern, predominant type 1 fiber involvement)

**Subcellular level (GO Cellular Component):**
- Axon initial segment (GO:0043194)
- Node of Ranvier (GO:0033268)
- Plasma membrane / cytoskeleton-membrane interface (spectrin-actin membrane skeleton)
- Sarcolemma (βIV-spectrin localizes here in muscle per PMID:28540413)

**Localization (UBERON):** peripheral nerve, skeletal muscle, cerebellum, brainstem auditory nuclei, cerebral cortex. Involvement is generally **bilateral/symmetric**, consistent with a systemic structural-protein defect rather than a focal lesion.

Sources: [PMID:28540413](https://pubmed.ncbi.nlm.nih.gov/28540413/), [Wikipedia SPTBN4](https://en.wikipedia.org/wiki/SPTBN4)

---

## 8. Temporal Development

**Onset:** Congenital to early-infantile in the majority — hypotonia, facial weakness, and areflexia typically present **soon after birth**, with delayed motor milestones and feeding difficulties from infancy; many patients "often do not achieve head control." In the larger natural-history cohort, 15/29 patients with documented data presented **at birth**, with the remainder presenting later (up to 15 years in some individuals with milder splice/missense variants) (PMC12335179).

**Onset pattern:** Insidious/static congenital presentation rather than acute onset.

**Progression:**
- Overall course is best described as **"static or slow progression"** rather than classic neurodegeneration, though hypotonia may evolve into appendicular spasticity/contractures over time while axial hypotonia persists (GeneReviews).
- "Considerable variation among patients" in rate and pattern of progression (PMC12335179).
- No formal staging system exists (this is not a cancer- or infection-type disease with defined stages).

**Disease course pattern:** Chronic, lifelong, non-remitting; no spontaneous or treatment-induced remission has been reported. Some features (e.g., epilepsy) may be episodic within an overall stable/progressive baseline.

**Disease duration:** Chronic lifelong condition; not self-limited. Mortality has been documented in early childhood in a minority (2/17 patients with mortality data died at 14 months and 3 years, both from **respiratory failure**), indicating a subset with a severe/fatal early course, while others survive into later childhood/adolescence with severe disability (PMC12335179).

**Critical periods:** Early infancy/childhood is the critical period for diagnosis, respiratory/nutritional support initiation, and developmental intervention (early intervention programs ages 0–3 per GeneReviews management guidance); the postnatal period is also mechanistically critical for auditory brainstem heminode maturation, per mouse model data showing βIV-spectrin's essential role specifically during **postnatal development** of Nav clustering (PMID:35393465).

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/), [PMC12335179 (natural history)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335179/)

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence: unknown/not established.** GeneReviews states explicitly: "The prevalence of this condition is unknown." Only ~38 patients have been reported in the world literature as of the 2025 natural history study — this is an **ultra-rare disease**, likely under-ascertained given its recent (2017) first description and reliance on exome/genome sequencing for diagnosis.
- No incidence, birth-prevalence, or registry-based estimates exist.

**Inheritance pattern:** **Autosomal recessive.** Both parents of an affected individual are obligate heterozygous carriers (typically asymptomatic).

**Penetrance:** Appears fully penetrant for biallelic pathogenic variants (no reported unaffected homozygotes), though phenotypic severity varies (see Phenotypes section) — this is best characterized as **variable expressivity rather than incomplete penetrance**.

**Expressivity:** Markedly **variable** — ranging from profound multisystem disease (severe ID, seizures, deafness, respiratory failure) to a milder phenotype limited to axonal neuropathy and myopathic facies without intellectual disability (PMID:31857255). This variability appears to correlate partly with variant type/location (e.g., truncating variants causing complete AIS mislocalization vs. missense variants retaining partial function).

**Genetic anticipation:** Not described (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported in the literature reviewed, though standard recurrence-risk counseling (25% per pregnancy) applies as for other AR conditions; germline mosaicism cannot be excluded and would be discussed per standard genetic counseling practice.

**Founder effects:** No specific founder variant/population has been formally described, though the disproportionate representation of **consanguineous Middle Eastern/Arab families** (45% of reported cases are Arab, 13 Saudi patients specifically in the 2025 cohort) suggests regional enrichment from consanguinity-driven ascertainment rather than a confirmed single founder allele (PMC12335179).

**Consanguinity role:** Major — **66% of the 38 reported cases** had documented parental consanguinity, and most reported homozygous (rather than compound heterozygous) genotypes arise in consanguineous unions.

**Carrier frequency:** Not established in the literature (individual variants are typically private/family-specific and largely absent from gnomAD); no population-level carrier-frequency study has been performed.

**Population demographics (from PMC12335179, n=38):**
- **Sex distribution:** 45% female, 37% male, 18% unspecified — no strong sex bias apparent (consistent with autosomal, not X-linked, inheritance).
- **Ethnic/geographic distribution:** Arab/Middle Eastern patients comprise the largest reported subgroup (45%, including 13 Saudi patients from one 2025 cohort), reflecting both true regional consanguinity-driven enrichment and possible ascertainment bias from specific referral centers; cases have also been reported from German, Kurdish, and other European/international families (PMID:28540413; PMC8298470).
- **Age distribution:** Reported patients range from infancy through adolescence (up to 15 years at presentation in some cases); no adult-onset cases have been described, consistent with the congenital nature of the disorder.

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/), [PMC12335179 (natural history, 38 patients)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335179/)

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- No specific diagnostic biomarker or blood/urine test exists. Creatine kinase (CK) is typically **not markedly elevated** (helpful in distinguishing from dystroglycanopathies per GeneReviews differential diagnosis table).
- **Electromyography (EMG)/nerve conduction studies:** demonstrate axonal motor neuropathy/neuronopathy pattern.
- **Auditory brainstem response (ABR):** absent or abnormal in patients with central deafness, despite normal cochlear function/otoacoustic emissions — a key diagnostic clue pointing to **retrocochlear/central** rather than cochlear hearing loss (consistent with mouse model mechanism).
- **EEG:** performed in 12 patients in the natural history cohort; 5 abnormal, 7 normal — used to characterize seizure activity/epileptiform discharges (some patients show epileptiform discharges without clinical seizures, PMC8298470).
- **Neuroimaging (brain MRI):** abnormal in 14/22 patients with available imaging — findings include vermian atrophy, diffuse T2-hyperintensity, mildly enlarged CSF spaces, cerebral atrophy, and white matter abnormalities (PMC12335179).
- **Muscle biopsy:** performed in 8 patients; shows fiber atrophy (type 1 fiber atrophy more prominent than type 2), incomplete congenital fiber-type disproportion, and combined myopathic/neurogenic features — reflecting secondary muscle involvement from the primary axonal neuropathy plus intrinsic sarcolemmal βIV-spectrin loss (PMID:28540413; PMC12335179).
- **Nerve biopsy:** in select functionally characterized cases, shows reduced/absent nodal βIV-spectrin, weak Nav channel labeling, and absent nodal KCNQ2 channels (PMID:29861105).

**Genetic testing:**
- **Recommended approach (GeneReviews):** a **hypotonia, neuropathy, intellectual disability, and/or epilepsy multigene panel that includes SPTBN4**, or **exome/genome sequencing**. **Single-gene sequential testing is typically NOT recommended** given phenotypic overlap with many other congenital hypotonia/neuropathy genes.
- **Molecular findings in the GeneReviews cohort (n=14):** 8 truncating variants, 4 missense, 2 splice variants; 12/14 individuals homozygous.
- Chromosomal microarray, karyotyping, and mitochondrial DNA testing are not primary diagnostic tools for this disorder (it is a single-gene defect, not typically caused by CNV, though at least one multi-exon deletion has been reported and would be detectable by CMA/exome CNV calling) (PMC8298470).
- Repeat-expansion testing is not applicable.

**Omics-based diagnostics:** No RNA-seq, proteomic, or epigenomic diagnostic assay is in clinical use; research-level functional studies (AIS-localization assays, PIP-strip lipid binding) have been used to classify variants of uncertain significance in the research setting (PMID:29861105), but these are not standard clinical diagnostics.

**Clinical criteria/differential diagnosis (GeneReviews):**
| Condition to exclude | Distinguishing feature |
|---|---|
| Prader-Willi syndrome | Hyperphagia, obesity (absent in SPTBN4 disorder) |
| Muscular dystrophy-dystroglycanopathy | Elevated CK, brain malformations |
| Spinal muscular atrophy | Normal cognition and hearing |
| TBCK-related disorder | White matter changes; normal hearing |
| UNC80 deficiency | Dysmorphic features, skull deformities |

**Screening:** No population-based newborn or carrier screening program exists for this ultra-rare condition; family-specific carrier testing, prenatal testing, and preimplantation genetic testing become available once the familial pathogenic variant(s) are identified.

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/), [PMC12335179](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335179/)

---

## 11. Outcome/Prognosis

**Survival and mortality:**
- No formal 5-/10-year survival statistics exist given the small cohort size.
- In the 2025 natural history study, **2 of 17 patients with mortality data died** — at ages **14 months and 3 years**, both from **respiratory failure**, underscoring neuromuscular respiratory compromise as the principal life-threatening complication (PMC12335179).
- Most reported patients survive into childhood/adolescence with severe disability rather than early death, but data on long-term (adult) survival are essentially absent given the disease's recent discovery (2017) and young reported cohort.

**Morbidity and function:**
- The majority of affected individuals have **severe-to-profound developmental delay/intellectual disability**, are **non-ambulatory** (unable to sit, stand, or walk), and have **severely limited or absent speech/language**.
- Significant disability domains: motor (non-ambulatory), communication (non-verbal), respiratory (ventilator-dependence in some), nutritional (gastrostomy-tube dependence common), and sensory (visual/hearing impairment in a subset).
- No formal QOL instrument (EQ-5D, SF-36, PROMIS) data are published for this population.

**Disease course/complications:**
- Recurrent aspiration pneumonia (from dysphagia/sialorrhea) — reported in 61% respiratory-difficulty subgroup, with 2 patients progressing to restrictive lung disease.
- Scoliosis and joint contractures from chronic hypotonia/immobility.
- Drug-resistant epilepsy (including infantile spasms) in a subset.
- Recovery potential: no reports of functional recovery or improvement over time; course is static-to-slowly-progressive rather than remitting.

**Prognostic factors:** Variant type appears to correlate with severity — truncating variants causing complete loss of AIS localization are associated with more severe multisystem phenotypes, while certain missense/splice variants that partially preserve protein function are associated with milder, neuropathy-predominant phenotypes without intellectual disability (PMID:31857255 vs. PMID:29861105/PMC8298470). No validated prognostic biomarker exists.

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/), [PMC12335179 (natural history)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335179/)

---

## 12. Treatment

There is **no disease-modifying, curative, or gene-targeted therapy** for SPTBN4-related neurodevelopmental disorder. Management is entirely **supportive/symptomatic**, per GeneReviews consensus recommendations:

**Pharmacotherapy:**
- **Epilepsy:** "Standardized treatment with anti-seizure medication by an experienced neurologist"; a ketogenic diet has been used safely in at least one reported case. (NCIT: C15986 Pharmacotherapy; specific anti-seizure medications selected per standard epilepsy protocols)
- **Sialorrhea:** Consider medical management with glycopyrrolate (Robinul®) or **Botox® (botulinum toxin) injections** if severe. (NCIT:C1420 Botulinum Toxin; NCIT:C47646-adjacent anticholinergic pharmacotherapy)
- **Constipation:** Stool softeners, prokinetics, osmotic agents, or laxatives as needed. (NCIT:C15986 Pharmacotherapy — supportive)

**Advanced therapeutics:** None available or in development — no gene therapy, cell therapy, RNA-based therapy (ASO/siRNA), targeted therapy, or immunotherapy programs exist for SPTBN4 disorder; no registered ClinicalTrials.gov studies were identified.

**Surgical/interventional:**
- **Gastrostomy tube placement** for persistent feeding difficulties/dysphagia (NCIT:C15829-adjacent Enteral Feeding / Gastrostomy)
- Orthopedic management of scoliosis and joint contractures (surgical correction as clinically indicated) (NCIT:C16186 Orthopedic Surgical Procedure)

**Supportive and rehabilitative care:**
- **Hearing aids** for hearing loss (NCIT — Hearing Aid Fitting; no dedicated NCIT clinical-action term identified — device-based intervention)
- **Ventilator support (e.g., BiPAP)** for respiratory distress/nocturnal hypoventilation (NCIT:C50384-adjacent noninvasive ventilation)
- **Feeding therapy** (NCIT:C15302-adjacent rehabilitation therapy)
- **Physical/occupational therapy** with stretching protocols for spasticity/contractures (NCIT:C15302 Physical Therapy)
- **Early intervention services (ages 0–3), developmental preschool (ages 3–5), IEP/specialized educational instruction** for developmental delay/intellectual disability (NCIT:C15315 Rehabilitation)
- No specific treatment exists for cortical visual impairment beyond early intervention.

**Treatment strategy:** GeneReviews provides a structured multidisciplinary management framework (initial evaluations across neurology, developmental pediatrics, ophthalmology, audiology, sleep medicine, GI/feeding, orthopedics, and genetic counseling) plus a surveillance schedule (ophthalmology and sleep study every 1–2 years, audiology as indicated, seizure monitoring, growth/nutrition assessment).

**Treatment outcomes:** No systematic data on response rates or adverse events exist beyond individual case reports; management follows generic protocols for congenital hypotonia/neuromuscular disease rather than SPTBN4-specific evidence.

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/)

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable risk factor); the principal "primary prevention" avenue is **genetic counseling and reproductive risk reduction** in families with a known pathogenic variant — carrier testing of at-risk relatives, prenatal testing (chorionic villus sampling/amniocentesis) for at-risk pregnancies, and **preimplantation genetic testing (PGT)** once familial variants are identified (GeneReviews).

**Secondary prevention:** Early diagnosis via multigene panel/exome sequencing in infants presenting with congenital hypotonia enables earlier initiation of supportive interventions (respiratory monitoring, feeding support, developmental services) that may reduce morbidity, though no formal screening program exists.

**Immunization:** No disease-specific vaccine strategy; standard immunization schedules apply, with attention to respiratory infection prevention (e.g., influenza, RSV prophylaxis, pneumococcal vaccination) given aspiration/respiratory vulnerability — a general supportive-care consideration rather than a published disease-specific guideline.

**Screening/early detection:** No population-based newborn screening exists (not detectable by standard metabolic newborn screening panels, as this is a structural-protein/cytoskeletal disorder, not a biochemical one). Family-specific carrier screening is the only applicable "screening" modality once an index case is identified.

**Genetic counseling:** Central to prevention in this disorder — given autosomal recessive inheritance, each subsequent pregnancy in a family with two carrier parents carries a 25% recurrence risk; consanguineous unions substantially elevate risk given the high rate of biallelic homozygosity observed in reported cohorts (66% consanguinity rate).

**Public health/environmental interventions:** Not applicable (no environmental risk factor to mitigate).

**Prophylaxis:** No disease-specific prophylactic medication exists; supportive prophylaxis against aspiration pneumonia (positioning, feeding modifications, possible gastrostomy) is a practical preventive measure against the leading cause of mortality (respiratory failure).

Sources: [GeneReviews SPTBN4 Disorder](https://www.ncbi.nlm.nih.gov/books/NBK559435/)

---

## 14. Other Species / Natural Disease

No naturally occurring SPTBN4-related disease has been reported in companion animals, livestock, or wildlife (e.g., no OMIA entry identified). The relevant "natural disease" model is a **spontaneous mouse mutant** (see Model Organisms, below) rather than a veterinary clinical disease. Orthologous *Sptbn4* genes exist across mammals (high conservation of the spectrin/ankyrin cytoskeletal system), but no cross-species zoonotic or comparative veterinary disease relevance applies — this is a purely genetic, non-transmissible condition.

---

## 15. Model Organisms

### Mouse models — the primary and best-characterized model system

**1. Quivering (qv) spontaneous mutant mouse** (NCBITaxon:10090, *Mus musculus*)
- A **spontaneous autosomal recessive mutation** that arose in 1953, with **seven distinct alleles** identified over time (e.g., *qv*, *qv-3J*, *qv-4J*).
- Phenotype: **progressive ataxia with hind-limb paralysis, deafness, and tremor** — closely recapitulating the human triad of neuropathy/motor dysfunction and central deafness.
- Molecular basis: **loss-of-function mutations in mouse *Sptbn4* (Spnb4)** causing "alterations in ion channel localization in myelinated nerves," providing the original mechanistic rationale for human SPTBN4 disease (PMID:11528393, Parkinson et al., *Nature Genetics* 2001).
- Auditory pathology: **central, not cochlear**, deafness — absent Preyer's reflex (ear-twitch to sound) despite normal cochlear morphology and normal cochlear microphonic potentials, but abnormal brainstem auditory nuclei responses — directly mirroring the human central/retrocochlear hearing loss mechanism.
- Available strain: **B6ByJ;D2-Sptbn4^qv-4J/J** (Jackson Laboratory stock #002996).

**2. Sptbn4^geo (β4-spectrin null) mice**
- Complete knockout model used to study postnatal auditory brainstem development.
- Findings: β4-spectrin is critical for **Nav channel clustering at the heminode** along auditory nerve terminals during postnatal development, but is **not required for formation of nodal/AIS structures per se**. Presynaptic terminal recordings showed elevated action-potential threshold and increased conduction failures during high-frequency spike trains; mice showed slower central conduction and **no startle responses** despite normal cochlear function (PMID:35393465, Sci Rep 2022).

**3. AnkyrinG conditional knockout (AnkG cKO) and *Sptbn4^qv-3J* comparison mice**
- Used in the AJHG functional study (PMID:29861105) to demonstrate that **ankyrin-R and βI-spectrin can partially compensate for AnkG/βIV-spectrin loss to rescue Nav channel clustering at nodes, but cannot rescue KCNQ2/KCNQ3 potassium channel clustering** — establishing the differential channel-specific compensation mechanism central to disease pathophysiology.

**4. Double βI/β4-spectrin knockout mice**
- Mice lacking both β1- and β4-spectrin show **severe motor impairment and epileptic activity**, indicating synergistic/compensatory roles between spectrin paralogs at the AIS in different neuron populations (e.g., parvalbumin-positive interneurons, where β1-spectrin substitutes at the AIS in the absence of β4-spectrin) (ResearchGate/PMID references from related spectrin-compensation literature).

### Model characteristics
- **Phenotype recapitulation:** The mouse models reproduce the **core triad** of the human disease remarkably well — motor/axonal neuropathy, ataxia, and central (not cochlear) deafness — and the 2025 natural history study explicitly notes that ataxia, previously seen only in mice, has now also been documented in human patients, strengthening cross-species concordance (PMC12335179).
- **Model limitations:** Human intellectual disability/developmental delay — the most disabling feature in most patients — is difficult to directly model/quantify in mice; cognitive-behavioral correlates in mouse models were not detailed in the sources reviewed. Respiratory failure (the leading human mortality cause) and gastrointestinal/feeding phenotypes are also less emphasized in the mouse literature reviewed here.
- **Research applications:** Mouse models have been essential for (a) establishing the causal gene and loss-of-function mechanism prior to human gene discovery, (b) dissecting the differential Na+ vs. K+ channel-clustering compensation mechanism, (c) studying postnatal auditory brainstem heminode maturation, and (d) informing timelines for potential future node-of-Ranvier "restoration" therapeutic strategies (a related paper, PMID:29907663, "Reorganization of Destabilized Nodes of Ranvier in βIV Spectrin Mutants Uncovers Critical Timelines for Nodal Restoration and Prevention of Motor Paresis," suggests a window for intervention, though this remains preclinical).

### Non-mammalian/cellular models
No zebrafish, *Drosophila*, *C. elegans*, or yeast *SPTBN4* disease models were identified in this search; functional characterization of human variants has primarily used **heterologous expression in cultured rodent neurons** (AIS-localization assays) and **in vitro PIP-strip lipid-binding assays** (PMID:29861105) rather than whole-organism non-mammalian models.

### Resources
- Jackson Laboratory strain repository (quivering alleles): [JAX Strain 002996](https://www.jax.org/strain/002996)
- MGI (Mouse Genome Informatics) — *Sptbn4* gene records
- No dedicated IMPC/KOMP conditional-knockout program specific to *Sptbn4* was identified in this search, though such resources may exist and warrant a direct IMPC database query for full confirmation.

Sources: [PMID:11528393 (Parkinson et al. 2001, Nat Genet)](https://pubmed.ncbi.nlm.nih.gov/11528393/), [PMID:35393465 (Sci Rep 2022)](https://pubmed.ncbi.nlm.nih.gov/35393465/), [PMID:29861105 (AJHG 2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5992132/), [JAX Strain 002996](https://www.jax.org/strain/002996), [PMID:29907663 (nodal restoration timelines)](https://pubmed.ncbi.nlm.nih.gov/29907663/)

---

## Summary of Key Primary Literature (PMID index)

| PMID | Citation | Contribution |
|---|---|---|
| 11528393 | Parkinson et al. 2001, *Nat Genet* | Original quivering mouse *Sptbn4* mechanism paper |
| 28540413 | Knierim et al. 2017, *Hum Genet* | First human SPTBN4 disease report (congenital myopathy, neuropathy, central deafness) |
| 29861105 | Wang, Ortiz-González, Yum et al. 2018, *AJHG* | Defines βIV spectrinopathy as distinct entity; Na+/K+ channel clustering mechanism |
| 31857255 | 2019, *Eur J Med Genet* (or similar) | Milder phenotype — axonal neuropathy without intellectual disability |
| 32672909 | Yang et al., GeneReviews *SPTBN4* Disorder | Consensus clinical/management reference |
| 35393465 | 2022, *Sci Rep* | Heminode Nav clustering and central auditory processing mechanism |
| PMC8298470 (EJHG 2021) | Novel bi-allelic variants expand SPTBN4 spectrum | Genotype-phenotype expansion, multi-exon deletion |
| PMC12335179 (2025) | Natural history of SPTBN4-related NEDHND | Largest cohort (38 patients), ataxia first reported in humans, mortality data |

---

**Note on evidence gaps:** No OMIM clinical synopsis full-text could be directly retrieved (403 error) — clinical synopsis details above are triangulated from GeneReviews, the AJHG/EJHG primary literature, and the 2025 natural-history study, which together provide equivalent or more current phenotype-frequency data. Direct confirmation of gnomAD gene-constraint metrics (LOEUF/pLI) for *SPTBN4* was not obtained in this search and would require a direct gnomAD browser query if precise values are needed for curation.