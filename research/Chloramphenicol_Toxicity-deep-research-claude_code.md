---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-06T01:20:01.461514'
end_time: '2026-10-06T01:21:19.846441'
duration_seconds: 78.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chloramphenicol Toxicity
  mondo_id: MONDO:0010784
  category: Complex
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.7528386
  session_id: 68ee5478-082d-5a81-aae3-c2c1854f6b8b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chloramphenicol Toxicity
- **MONDO ID:** MONDO:0010784 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Chloramphenicol Toxicity** covering all of the
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

# Chloramphenicol Toxicity: Research Report for dismech Curation

**Scope and verification status.** I ran three web searches (standard mode) and read only the result summaries. I did not open any article or fetch any abstract. Two consequences follow:

- **PMIDs and snippets.** I give no PMIDs and no exact-quote snippets, because I could not verify them. Fetch each cited source with `just fetch-reference` and copy snippets from the cache, as CLAUDE.md requires.
- **Ontology terms.** I give no CURIEs. Terms are named in words only, and each needs an OAK or cache lookup before binding.

Claims marked **[general knowledge]** come from well-established pharmacology and were not confirmed in this session.

**Mondo ID.** The template gives MONDO:0010784. I did not check it, and I could not confirm it refers to chloramphenicol toxicity. Resolve it via OAK before use, because dismech guards against named-entity confusion.

---

## 1. Disease Information

**Overview.** Chloramphenicol toxicity is a group of adverse drug reactions to the broad-spectrum antibiotic chloramphenicol. It has three distinct clinical forms:

1. **Dose-dependent, reversible bone-marrow suppression.** This mainly affects the erythroid lineage and can cause sideroblastic anemia.
2. **Idiosyncratic aplastic anemia.** It is rare, usually irreversible, and can occur after any route of exposure.
3. **Gray baby syndrome.** It occurs in neonates and premature infants and causes cardiovascular collapse.

Other toxicities are optic and peripheral neuropathy and hemolysis in G6PD deficiency. These are **[general knowledge]**.

**Entry-level decision.** The toxicity is a pharmacologic or iatrogenic entity, and it has no heritable cause. The three forms have different mechanisms and time courses. The stub queue's `entry_type` decision is therefore live here:
- A single `DISEASE` entry would need pathophysiology nodes that hold for every case. That is hard, because the forms share no mechanism.
- A `GROUPING` of three entries, or a single entry with `has_subtypes`, is the more defensible option.
- Record the choice in notes either way.

**Synonyms (general knowledge).** Chloramphenicol-induced aplastic anemia, chloramphenicol-induced bone marrow depression, gray (grey) baby syndrome, gray syndrome.

**Identifiers.** I did not verify any. Check MeSH, ICD-10-CM (T36.2X-, adverse effect and poisoning by chloramphenicol group), and MONDO via OAK.

**Data origin.** The sources are aggregate: pharmacology reviews, StatPearls, case reports and case series, and population case-control studies of aplastic anemia. They are not EHR-derived.

---

## 2. Etiology

**Causal factor.** Exposure to chloramphenicol is the cause. Systemic routes (IV or oral) are the classic ones. Topical and ocular exposure is a minor, contested contributor to aplastic anemia (see below).

**Risk factors**
- **Prematurity and neonatal age.**
  - Gray baby syndrome is described in premature neonates given chloramphenicol IV or orally within two days of birth. The immature liver cannot glucuronidate the drug efficiently, and the neonatal kidney cannot excrete it and its metabolites well ([PMC case report and review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12833000/); [StatPearls](https://www.statpearls.com/point-of-care/22420)).
  - Another summary states that immature neonatal liver cannot synthesize and recycle UDP-glucuronyltransferase efficiently.
- **High dose or prolonged therapy.** Marrow suppression is dose-dependent and reversible **[general knowledge, consistent with the JCI-era literature below]**.
- **Hepatic or renal impairment.** These reduce clearance **[general knowledge]**.
- **Aplastic anemia.** It is idiosyncratic. Genetic susceptibility has been proposed but is not established. I found no verified susceptibility locus.

**Aplastic anemia risk figures (from search summaries, not verified at source)**
- A commonly quoted risk of fatal aplastic anemia after chloramphenicol is about 1 in 20,000 to 1 in 30,000 courses, roughly 13 times the background incidence (reported in the [NTP Report on Carcinogens profile](https://ntp.Niehs.Nih.Gov/ntp/roc/content/profiles/chloramphenicol.pdf) results; confirm in the document).
- Case-control data are weaker than the headline figure:
  - One study reported an adjusted OR of 8.7 (95% CI 0.87–87.93) for exposure in the previous year.
  - An ocular-chloramphenicol analysis found 3 cases (2.1%) and 5 controls (0.4%) exposed, with an adjusted OR of 3.77 (95% CI 0.84–16.90).
  - The search summary said more than 400 cases across two large population-based studies had no chloramphenicol eye-drop use.
  - See the [Haematologica article](https://haematologica.org/article/view/5343/23532), [PMC1873671](https://pmc.ncbi.nlm.nih.gov/articles/PMC1873671/), and [PMC28472](https://pmc.ncbi.nlm.nih.gov/articles/PMC28472). I do not know which paper reports which number, so attribute them only after reading.
- **Curation note.** The ocular-exposure OR confidence intervals include 1, so that data does not establish risk.

**Protective factors.** None established. Avoiding the drug and using alternative antibiotics in neonates is prevention, not a protective factor.

**Gene–environment interactions.** I found no verified data. G6PD deficiency with hemolysis is a recognized pharmacogenetic interaction **[general knowledge, unverified]**. It would need a source before being curated.

---

## 3. Phenotypes

Frequencies are not verified. Do not enter them without a source.

| Form | Phenotype | Onset and course | HPO term (to look up) |
|---|---|---|---|
| Marrow suppression | Anemia (often with reticulocytopenia) | Dose-related, during therapy, reversible on withdrawal | Anemia; Reticulocytopenia |
| Marrow suppression | Sideroblastic anemia | During therapy | Sideroblastic anemia |
| Marrow suppression | Leukopenia, thrombocytopenia | During therapy | Leukopenia; Thrombocytopenia |
| Aplastic anemia | Pancytopenia, bone marrow aplasia | Idiosyncratic, can be delayed after exposure, often irreversible | Pancytopenia; Aplastic anemia |
| Gray baby syndrome | Abdominal distention, vomiting | Days after drug start | Abdominal distention; Vomiting |
| Gray baby syndrome | Hypothermia, cyanosis | Same | Hypothermia; Cyanosis |
| Gray baby syndrome | Cardiovascular instability, vasomotor collapse, mottled and then ashen-gray skin | Same | Hypotension or shock-type terms; Mottled skin |

- The gray-baby clinical picture comes from the [PMC case report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12833000/) and [StatPearls](https://www.statpearls.com/point-of-care/22420) summaries.
- That case report reviews 19 additional published cases. Mine it for outcomes and frequencies.
- Quality-of-life data: none found.
- Optic neuritis and peripheral neuropathy occur with prolonged use **[general knowledge, unverified]**.

---

## 4. Genetic/Molecular Information

- **Causal genes.** None. This is not a Mendelian disease.
- **Relevant pharmacogenes (general knowledge, needs sources):**
  - UGT2B7 mediates chloramphenicol glucuronidation. UGT1A6 and UGT1A9 involvement is less certain.
  - Developmental immaturity of UGT activity is the neonatal mechanism.
- **Molecular target.** The mitochondrial ribosome (mtDNA-encoded protein synthesis). The sources say chloramphenicol targets the 39S large subunit of the mitoribosome ([T3DB](https://sendgrid.t3db.ca/toxins/T3D3954) summary; verify against a primary source).
- **Epigenetic and chromosomal data.** None found.
- **Genetic susceptibility to aplastic anemia.** Unresolved. State this as a knowledge gap, not as a gene association.

---

## 5. Environmental Information

- **Exposure.** Systemic chloramphenicol by IV or oral route. Topical or ocular use is controversial (see Section 2).
- **Lifestyle factors.** None.
- **Infectious agents.** None cause the toxicity. The drug is used for severe infections such as meningitis and typhoid, where alternatives are limited **[general knowledge]**.
- **ECTO term to look up.** An exposure term for chloramphenicol. Run `l~chloramphenicol` against ECTO, and try both "anaesthetic"-style spelling variants where relevant. Re-run every search a note claims, as CLAUDE.md requires.

---

## 6. Mechanism / Pathophysiology

### Causal chains

**Chain A: Dose-dependent marrow suppression**
1. Systemic chloramphenicol reaches hematopoietic progenitors. This is inferred from the drug's distribution **[general knowledge]**.
2. The drug binds the mitochondrial ribosome (39S subunit) and inhibits mitochondrial protein synthesis ([T3DB summary](https://sendgrid.t3db.ca/toxins/T3D3954); [JCI article](https://jci.org/articles/view/107015)).
3. This depletes mtDNA-encoded respiratory-chain subunits, including cytochrome components. The JCI summary says the inhibitory effect can be explained by the drug's action on cytochrome formation by the mitochondrial protein-synthesizing system.
4. Metabolically active, rapidly dividing cells, notably the erythroid lineage, lose oxidative capacity and become cytotoxically affected. Iron utilization is impaired, which gives sideroblastic changes. The sideroblastic link is stated in the search summary as thought to be related to mitochondrial dysfunction; the detailed iron-handling steps are inferred.
5. The result is reversible erythroid-predominant marrow suppression and anemia. The reviewed source says ample evidence ties the reversible suppression to inhibition of mitochondrial protein synthesis, while the aplastic form is a separate rare complication.

**Chain B: Idiosyncratic aplastic anemia (mechanism unresolved)**
1. Chloramphenicol exposure occurs.
2. A susceptible host develops stem-cell injury. The mechanism is **not established**. Proposed routes (a toxic nitroso or nitro-reduction metabolite, or genetic susceptibility) are hypotheses, not demonstrated here.
3. Marrow aplasia and pancytopenia follow.

Do not link Chain A's mitochondrial inhibition to aplastic anemia as if causal. The sources frame them as separate complications.

**Chain C: Gray baby syndrome**
1. A neonate, usually premature, receives chloramphenicol.
2. Immature hepatic UDP-glucuronyltransferase activity means glucuronidation is deficient. Renal excretion is also immature ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12833000/)).
3. Unconjugated drug accumulates to high serum concentrations.
4. Accumulated drug inhibits mitochondrial function in cardiac and other tissues. This step is the **commonly proposed but not directly demonstrated** link, and it needs a source before curation.
5. Cardiovascular collapse follows, with mottling, then ashen-gray skin, hypothermia, and cyanosis.

### Suggested ontology terms (lookup required)
- **GO.** Mitochondrial translation. Also consider a mitochondrial ribosome-related term for the molecular function (peptidyl transferase activity, inhibited by drug). Check the exact labels.
- **CL.** Erythroid progenitor cell, hematopoietic stem cell, hepatocyte (glucuronidation).
- **CHEBI.** Chloramphenicol. Look it up, and also look up chloramphenicol glucuronide if a metabolite node is wanted.
- **GO Cellular Component.** Mitochondrion, mitochondrial large ribosomal subunit.
- **Modifier.** Use `DECREASED` for mitochondrial translation (a quantitative state). Do not use `LOSS_OF_FUNCTION` unless you can justify it qualitatively.
- **Biological scale tags.** MOLECULAR for ribosome inhibition, CELLULAR for erythroid suppression, ORGANISM for circulatory collapse.

### Mechanism module candidates
`kb/modules/` already has antimicrobial drug mechanism modules and a "treatment toxicity / side effect as mechanism" family. Run `just list-modules ribosom` and `just list-modules mitochond` and use `rg -il "mitochondrial translation" kb/modules` before writing new nodes.

### Molecular profiling, single-cell, and screens
No data found for chloramphenicol toxicity. State "not available".

---

## 7. Anatomical Structures Affected

- **Primary.** Bone marrow, especially the erythroid compartment. Also the circulatory system in neonates.
- **Secondary.** Liver (site of drug metabolism). Optic nerve and peripheral nerves with chronic use **[general knowledge, unverified]**.
- **Cells.** Erythroid progenitors, hematopoietic stem cells, hepatocytes, cardiomyocytes (proposed).
- **Subcellular.** Mitochondria and the mitoribosome.
- **Laterality.** Not applicable, since the effects are systemic.
- **UBERON terms.** Look up bone marrow, liver, and optic nerve.

---

## 8. Temporal Development

- **Marrow suppression.** It develops during therapy, is dose-related, and is generally reversible after withdrawal.
- **Aplastic anemia.** It can appear weeks to months after exposure, is idiosyncratic, and is often irreversible. The delay is **[general knowledge]**; confirm it.
- **Gray baby syndrome.** It typically appears within the first days of therapy in neonates.
- **Critical period.** The neonatal and premature period, when glucuronidation is immature.
- **Remission.** Marrow suppression reverses on withdrawal. For aplastic anemia I have no verified remission data.

---

## 9. Inheritance and Population

- **Inheritance.** None.
- **Incidence figures.**
  - Aplastic anemia risk after chloramphenicol was quoted at about 1 in 20,000 to 1 in 30,000, as above.
  - A separate figure for background aplastic anemia incidence in Latin American countries was 1.6 per million per year, from a search summary. This is background incidence, not toxicity incidence.
  - If you encode `Prevalence`, use `measure_type: UNKNOWN` or a literature-based measure, not a rate you cannot quote. Gray baby syndrome today is rare, but I have no verified figure.
- **Demographics.** Neonates and premature infants for gray baby syndrome. No verified sex ratio or geography.
- **Consanguinity, founder effects, anticipation, carrier frequency.** Not applicable.

---

## 10. Diagnostics

All of this section is **[general knowledge]** unless stated. Verify with StatPearls (Gray baby syndrome and chloramphenicol chapters) and clinical guidelines.

- **Clinical diagnosis.** Temporal association with drug exposure plus compatible findings.
- **Laboratory tests.**
  - CBC with reticulocyte count. Suppression usually shows reticulocytopenia and anemia.
  - Marrow examination for vacuolated precursors, or aplasia in the idiosyncratic form.
  - Serum drug concentration monitoring. Therapeutic ranges exist, and high levels predict toxicity. Get the numbers from a guideline, not memory.
- **Genetic testing.** Not applicable.
- **Differential.** Neonatal sepsis and shock, other drug-induced marrow failure, and other causes of aplastic anemia.
- **Screening.** Monitoring blood counts during therapy. Therapeutic drug monitoring in neonates.

---

## 11. Outcome/Prognosis

- **Marrow suppression.** Reversible on drug withdrawal.
- **Aplastic anemia.** Mortality is high. The risk is much rarer than the older literature implied, as the case-control summaries above suggest.
- **Gray baby syndrome.** It is potentially fatal. The [PMC case report with 19 reviewed cases](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12833000/) is the best lead for mortality figures. I could not read them.
- **Prognostic factors.** Early recognition and drug cessation, serum level, and gestational age **[general knowledge]**.

---

## 12. Treatment

All of this is **[general knowledge]**. Confirm each item against a cited source before entering a `treatments:` block.

- **Stop chloramphenicol.** This is the primary treatment.
- **Supportive care.** Circulatory and respiratory support for gray baby syndrome. Transfusion for marrow suppression.
- **Removal of the drug.** Exchange transfusion, charcoal hemoperfusion, and hemodialysis have been reported in gray baby syndrome. Check the case-report literature for the actual evidence level.
- **Aplastic anemia.** Standard management is immunosuppressive therapy or hematopoietic stem cell transplantation. This is not specific to chloramphenicol, so reference the general aplastic anemia entry if one exists.
- **Experimental or trial data.** None found. Run a ClinicalTrials.gov search before writing "none".
- **NCIT terms to look up.** Supportive care, blood transfusion, hematopoietic cell transplantation, and discontinuation of therapy if NCIT has it. Apply the modality rules in CLAUDE.md. For example, `NCIT:C15431` maps to `CELL_THERAPY` in the mechanical backfill table, and I have not checked that mapping against the ontology in this session.

---

## 13. Prevention

- **Primary prevention.** Avoid chloramphenicol in neonates, or where alternatives exist. This is the key lesson from gray baby syndrome.
- **Dose control.** Use serum level monitoring and dose adjustment in neonates and in hepatic or renal impairment **[general knowledge]**.
- **Secondary prevention.** Serial blood counts.
- **Public health.** Regulatory restrictions and label warnings. I did not verify jurisdiction-specific policy.
- **Vaccines and genetic counseling.** Not applicable.

---

## 14. Other Species / Natural Disease

- **Veterinary use and toxicity.** One search result was a veterinary journal PDF ([Eurasian J Vet Sci](https://www.eurasianjvetsci.org/pdf.php3?id=676)). I did not read it. It suggests animal-toxicity literature exists.
- **Cats.** They are known for deficient glucuronidation and are sensitive to some drugs **[general knowledge]**. Whether chloramphenicol toxicity is documented in cats is unverified.
- **Food-producing animals.** Chloramphenicol is banned in food animals in many jurisdictions. This is a regulatory point, not a verified toxicity statement.
- **NCBI Taxon, breed, and OMIA entries.** None applicable (not heritable).
- **Zoonosis.** Not applicable.

---

## 15. Model Organisms

- **Mitochondrial translation inhibition.** The mechanism has been demonstrated in mammalian systems in the JCI-era literature ([JCI](https://jci.org/articles/view/107015)). The search summary does not say which species. Read it before assigning `evidence_source`.
- **Cell models.** Bone marrow cell and cell-line studies of mitochondrial protein synthesis inhibition are plausible leads. I have no verified citation.
- **Genetic models.** None. Mouse and zebrafish models of chloramphenicol-induced marrow suppression or gray baby syndrome: not found.
- **Limitations.** Reversible suppression is modeled by mitochondrial translation inhibition, but idiosyncratic aplastic anemia has no known model.
- **Databases.** MGI, ZFIN and IMPC are not applicable because the cause is non-genetic.

---

## Curation Next Steps

1. **Resolve the MONDO ID and the lump/split decision** (Section 1).
2. **Fetch references.** Run `just fetch-reference` on the PMC articles (PMC12833000, PMC1873671, PMC28472), the JCI article, and the Haematologica article. Get PMIDs from the fetched cache files, not from memory.
3. **Look up every ontology term.** Use OAK or the caches, in the same step as writing the CURIE. The `dismech-terms` skill governs this.
4. **Assign `evidence_source` correctly.**
   - Human case series: `HUMAN_CLINICAL`.
   - Mitochondrial ribosome studies in cells or isolated mitochondria: `IN_VITRO`.
   - Studies in animals: `MODEL_ORGANISM`.
5. **Mark unverified links as gaps.** Use `KNOWLEDGE_GAP` discussions for the aplastic anemia mechanism and for the cardiac step of gray baby syndrome. Do not state them as causal edges.
6. **Add a `history/` record** with `just new-history`.

## Sources

- [Chloramphenicol-induced gray baby syndrome: case report and review (PMC12833000)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12833000/)
- [StatPearls: Gray baby syndrome](https://www.statpearls.com/point-of-care/22420)
- [Frontiers in Pediatrics 2025 article (10.3389/fped.2025.1733059)](https://public-pages-files-2025.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2025.1733059/pdf)
- [JCI article 107015](https://jci.org/articles/view/107015)
- [T3DB chloramphenicol record](https://sendgrid.t3db.ca/toxins/T3D3954)
- [NTP Report on Carcinogens: chloramphenicol profile](https://ntp.Niehs.Nih.Gov/ntp/roc/content/profiles/chloramphenicol.pdf)
- [Haematologica article 5343](https://haematologica.org/article/view/5343/23532)
- [PMC1873671](https://pmc.ncbi.nlm.nih.gov/articles/PMC1873671/)
- [PMC28472](https://pmc.ncbi.nlm.nih.gov/articles/PMC28472)
- [Eurasian J Vet Sci PDF](https://www.eurasianjvetsci.org/pdf.php3?id=676)