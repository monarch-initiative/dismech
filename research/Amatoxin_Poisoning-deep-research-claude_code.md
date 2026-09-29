---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-19T20:02:08.293971'
end_time: '2026-09-19T20:08:15.056604'
duration_seconds: 366.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Amatoxin Poisoning
  mondo_id: ''
  category: Environmental
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
  - claude-sonnet-5
  web_search_requests: 23
  num_turns: 23
  total_cost_usd: 1.7405002
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Amatoxin Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Amatoxin Poisoning** covering all of the
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

This is excellent, comprehensive material. Let me get the redirected molecular mechanisms article and a couple more targeted sources (HPO phenotypes, and the recent PMC review on kidney mitochondrial toxicity, plus genetics/gnomAD context on why there's no genetic susceptibility marker, and CHEBI/GO term confirmations).

# Amatoxin Poisoning — Comprehensive Research Report

## 1. Disease Information

**Overview.** Amatoxin poisoning is an acute, dose-dependent toxic hepatonephropathy caused by ingestion of amatoxin-containing mushrooms — most notably *Amanita phalloides* ("death cap"), but also *A. virosa*, *A. verna*, *A. exitialis*, *A. fuliginea*, *Galerina* spp., and some *Lepiota* spp. More than 35 mushroom species across the genera *Amanita*, *Galerina*, and *Lepiota* contain amatoxins ([StatPearls NBK431052](https://www.ncbi.nlm.nih.gov/books/NBK431052/)). It is the leading cause of fatal mushroom poisoning worldwide: "amatoxin-containing mushrooms cause 95% of worldwide mushroom ingestion deaths" (StatPearls). The disease is not a genetic/Mendelian disorder but an environmental/toxic-exposure disease entity — it has no OMIM phenotype number and, to my knowledge, no dedicated Orphanet ID (Orphanet is oriented to rare genetic disease and does not carry a specific entry for amatoxin poisoning). It is indexed in PubMed/MeSH and coded administratively via ICD-10-CM toxicology codes.

**Key identifiers:**
- **MeSH**: *Mushroom Poisoning*, Unique ID **D009145** ([MeSH Browser](https://meshb.nlm.nih.gov/record/ui?ui=D009145)) — the broader indexing term under which amatoxin-specific literature is filed; there is no separate amatoxin-specific MeSH descriptor, so curation should cite D009145 as the closest controlled heading.
- **ICD-10-CM**: **T62.0X1-** (Toxic effect of ingested mushrooms, accidental/unintentional), with `A`/`D`/`S` 7th-character extensions for initial encounter, subsequent encounter, and sequela ([ICD10Data](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T62-/T62.0X1A)). ICD-11 places it under Chapter 22 (Injury, poisoning or certain other consequences of external causes) without an amatoxin-specific leaf code identified in this search.
- **MONDO / OMIM / Orphanet**: no amatoxin-specific MONDO term or OMIM phenotype number was identified — as an acute environmental toxidrome rather than an inherited disease, this is expected; if a MONDO/HPO-style knowledge base entry is created, this would be modeled as an environmental/toxic exposure entity rather than a Mendelian disease.
- **Wikidata**: "mushroom poisoning" **Q852186**; the causal toxin class is described on Wikidata's "poisoning by drugs" superclass **Q387175**.
- **CHEBI** (toxin chemistry, see §4/§6): α-amanitin, β-amanitin, phalloidin are indexed compounds (structural details below).

**Synonyms / alternative names:** Amatoxin mushroom poisoning; amatoxin syndrome; *Amanita phalloides* poisoning; death-cap poisoning; phalloides syndrome; cyclopeptide mushroom poisoning; hepatotoxic mushroom poisoning.

**Data provenance.** The evidence base is almost entirely aggregated disease-level and cohort/case-series data — national poison-center registries, retrospective multi-center cohorts (e.g., a Slovak cohort of 698 patients; a Chinese cohort of 105 and another of 567 patients; a Turkish liver-transplant cohort of 26 patients), case reports/series, and animal/in-vitro mechanistic studies — rather than individual EHR-linked genomic data, consistent with an acute toxic-exposure disease rather than a genetically characterized disorder.

---

## 2. Etiology

**Disease causal factor:** ingestion of amatoxins — a family of bicyclic octapeptide toxins (α-amanitin, β-amanitin, γ-amanitin, ε-amanitin) — present in fruiting bodies of *Amanita phalloides* and related species. This is a purely **environmental/toxicological** etiology; there is no genetic cause of the disease itself.

**Risk factors:**
- **Environmental/behavioral**: wild-mushroom foraging, misidentification of *A. phalloides* for edible species (e.g., paddy-straw mushroom, *Volvariella volvacea*, in Asian contexts) (StatPearls); toxic species entering food-distribution/market chains through "misidentification during collection, unintentional mixing of edible and toxic species" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)); amatoxin is heat-stable and survives cooking, drying, and freezing, so no culinary preparation is protective (StatPearls).
- **Age**: children absorb proportionally higher toxin doses and have substantially higher morbidity/mortality than adults; "most unintentional mushroom exposures occur in children younger than 6 years," and historic mortality series report ~50% in adults vs ~33% in children in that era, though absolute pediatric case-fatality for hepatotoxic species has been reported >80% in some series ([PMC12488608](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488608/)).
- **Dose/quantity ingested**: the single most important determinant of severity — a single *A. phalloides* cap can contain a lethal dose (estimated human oral LD50 for α-amanitin ≈ 0.1 mg/kg) (StatPearls; veterinary sources).
- **Delay to treatment**: time from ingestion to initiation of decontamination/antidotal therapy is a major modifiable prognostic factor.
- **Putative genetic/transporter variation (not established as a validated risk factor)**: hepatic uptake of amatoxin is mediated by the OATP1B3 transporter, encoded by *SLCO1B3* (HGNC gene). Common *SLCO1B3* SNPs (rs4149117 c.334T>G; rs7311358 c.699G>A) alter transporter activity for other OATP1B3 substrates in pharmacogenomic studies, but a direct, validated association between *SLCO1B3* genotype and inter-individual amatoxin susceptibility was **not found** in the literature searched — this should be treated as a plausible but unproven gene–toxin interaction rather than a confirmed risk factor.
- **Familial clustering**: shared-meal ingestion produces simultaneous, sometimes markedly heterogeneous, outcomes within families/households ("Family and the Fungi" case series, family of eight, PMID search; a Vietnamese familial case series with "markedly heterogeneous outcomes," PMID 42523156).

**Protective factors:** none intrinsic (no known protective genetic variant or diet identified in the literature searched); the only true "protective factor" is avoidance of ingestion (education) or early decontamination/antidotal treatment after exposure.

**Gene–environment interaction:** the leading candidate is *SLCO1B3/OATP1B3* transporter expression level, which mechanistically determines cellular amatoxin influx (see §6) — cell lines with low OATP1B3 expression show markedly reduced amanitin cytotoxicity ([PubMed 38641045](https://pubmed.ncbi.nlm.nih.gov/38641045/), *Amanitin-induced variable cytotoxicity in various cell lines is mediated by the different expression levels of OATP1B3*). Whether inherited human *SLCO1B3* polymorphism modulates clinical severity in patients remains an open research question, not yet answered in a clinical cohort.

---

## 3. Phenotypes

Amatoxin poisoning produces a **time-staged, multi-organ phenotype set**, classically described in four (or, in condensed schemes, three) phases.

### Phase 1 — Latent phase
- **Type**: absence of symptoms (asymptomatic interval)
- **Onset**: 6–24 h post-ingestion (mean ~10–12.3 h; rarely up to 36–48 h) ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/); StatPearls)
- **Clinical significance**: this delay — longer than the near-immediate onset of most non-amatoxin mushroom toxidromes — is itself a diagnostic clue and the reason patients rarely link symptoms to the meal.
- **HPO**: no positive finding to bind (asymptomatic interval); could be modeled as a temporal qualifier rather than a phenotype node.

### Phase 2 — Gastrointestinal phase (~6–24 h onward, lasting 1–3 days)
| Phenotype | HPO term | Notes |
|---|---|---|
| Watery/profuse diarrhea | **HP:0002014** Diarrhea | Cholera-like, can be severe |
| Recurrent vomiting | **HP:0002013** Vomiting | |
| Abdominal pain / cramps | **HP:0002027** Abdominal pain | |
| Dehydration | **HP:0001944** Dehydration | Risk of hypovolemic shock |
| Hypotension / shock | **HP:0002615** Hypotension | Severe cases |
| Tachycardia | **HP:0001649** Tachycardia | Reflex to volume loss |

- **Severity**: variable, moderate to severe; can itself cause death from hypovolemic shock/electrolyte derangement in the most severe cases before hepatic phase manifests.
- **Progression**: transient, self-limited over 1–3 days, masking ongoing occult hepatic injury.

### Phase 3 — "Apparent convalescence" / latent hepatotoxic phase (day 2–3)
- Symptomatic relief with ongoing subclinical rise in transaminases; this is the most dangerous phase for missed diagnosis, described as "a significant diagnostic challenge" because of "the transient improvement phase preceding severe organ toxicity" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

### Phase 4 — Hepatic/multiorgan failure phase (day 3–7+)
| Phenotype | HPO term | Notes |
|---|---|---|
| Elevated hepatic transaminases | **HP:0002910** Elevated hepatic transaminase | AST/ALT frequently >1000–5000 U/L |
| Jaundice | **HP:0000952** Jaundice | |
| Coagulopathy | **HP:0001928** Abnormal bleeding (or **HP:0031956** Elevated prothrombin time / INR) | Loss of clotting factor synthesis |
| Hepatic encephalopathy | **HP:0002480** Hepatic encephalopathy | Graded I–IV |
| Hypoglycemia | **HP:0001943** Hypoglycemia | Loss of hepatic gluconeogenesis |
| Metabolic acidosis | **HP:0001942** Metabolic acidosis | |
| Acute liver failure | **HP:0006554** Acute hepatic failure | Fulminant hepatic failure |
| Acute kidney injury / hepatorenal syndrome | **HP:0001919** Acute kidney injury; consider **HP:0000083** Renal insufficiency | Acute tubular necrosis, proximal tubule injury |
| Elevated bilirubin | **HP:0002904** Hyperbilirubinemia | |
| Elevated LDH | (no dedicated HP term; lab finding) | |
| Elevated ammonia | (no dedicated HP term commonly used; correlates with encephalopathy) | Plasma ammonia >95.1 μmol/L independently associated with mortality ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)) |

**Additional / less common phenotypes reported in recent literature:**
- **Hematotoxicity** — unexpectedly reported in a retrospective cohort ("Unexpected Amanita phalloides-Induced Hematotoxicity," [PMC10891511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10891511/)); direct amanitin cytotoxicity to hematopoietic cell lines has been separately demonstrated in vitro (PMC10820516, *Unraveling Hematotoxicity of α-Amanitin in Cultured Hematopoietic Cells*).
- **Elevated CK-MB and impaired consciousness** — identified as independent mortality risk factors reflecting extrahepatic organ involvement, beyond conventional liver parameters ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/), citing a Chinese cohort study, PMID 40645529).
- **Ulcerating ileocolitis** — a distinct, less common GI manifestation described in a dedicated case report ([PMC4555452](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4555452/)).
- **Proximal tubular necrosis without recovery** — a nephrotoxic phenotype that can be irreversible even after hepatic recovery ([PMC8610939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8610939/)).

**Frequency/severity data**: In a Chinese cohort of 105 patients, INR > 3.6 (AUC 0.941) and plasma ammonia > 95.1 μmol/L (AUC 0.805) independently predicted mortality; a Chronic Liver Failure–Organ Failure (CLIF-OF) score >9 within 24 h "demonstrated excellent predictive performance and outperformed the other evaluated scoring systems" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Quality-of-life impact**: acute survivors without transplant generally recover full hepatic/renal function; those with irreversible proximal tubular necrosis or those requiring liver transplantation face long-term morbidity (immunosuppression, chronic kidney disease risk) — dedicated EQ-5D/SF-36 outcome studies specific to amatoxin poisoning were not identified in this search.

---

## 4. Genetic/Molecular Information

Amatoxin poisoning is **not a Mendelian/inherited disease** — there is no causal gene, no pathogenic germline variant, and no chromosomal abnormality that causes it. The relevant "genetic/molecular" information is instead about (a) the toxin's own molecular identity and target, and (b) transporter genetics that may modulate host susceptibility.

**Molecular target (host):**
- **POLR2A** (RNA polymerase II largest subunit) — the direct, non-covalent binding target of amanitins. α-Amanitin binds in the "bridge helix" region of RNAP II via hydrogen bonding, blocking translocation and transcription elongation ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)). HGNC: POLR2A.
- **SLCO1B3** (OATP1B3) — hepatic sinusoidal uptake transporter for amanitin; HGNC gene `SLCO1B3`. Knockdown of OATP1B3 in HepG2 cells abolishes α-amanitin cytotoxicity, and cell-line susceptibility correlates with OATP1B3 expression level ([PubMed 38641045](https://pubmed.ncbi.nlm.nih.gov/38641045/); [PubMed 16495352](https://pubmed.ncbi.nlm.nih.gov/16495352/), Letschert et al., *Molecular characterization and inhibition of amanitin uptake into human hepatocytes*, Toxicol Sci 2006).
- **SLC10A1** (NTCP, sodium-taurocholate cotransporting polypeptide) — contributes secondarily to hepatocyte amanitin uptake alongside OATP1B3.
- **STT3B** — a subunit of the oligosaccharyltransferase (N-glycan biosynthesis) complex, recently identified via CRISPR screening as required for cellular amanitin entry; STT3B depletion sharply reduces α-amanitin uptake, and indocyanine green was identified as a candidate STT3B inhibitor with in vivo protective effect ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)).
- **TP53 / BAK** — p53- and caspase-3-dependent apoptosis mediates hepatocyte death; p53/BAK-knockout mice show resistance to α-amanitin hepatotoxicity ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)).
- **TNF** (TNF-α) — amplifies hepatocyte apoptosis and lipid peroxidation after amanitin exposure; anti-TNF antibody pretreatment prevents liver injury in mice ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)).

**Toxin molecular identity (chemical entities):**
- **α-Amanitin** — CHEBI-indexed bicyclic octapeptide, Wikipedia/CHEBI entry ("α-Amanitin"); a highly modified bicyclic octapeptide with an outer peptide-bond loop and an inner loop closed by a tryptathionine (Trp–Cys) crossbridge between 6-hydroxytryptophan and cysteine; carries hydroxylated/modified residues including (2S,3R,4R)-4,5-dihydroxyisoleucine and trans-4-hydroxyproline, conferring high-affinity RNAP II binding.
- **β-Amanitin, γ-amanitin, ε-amanitin** — structural congeners differing at side-chain positions, all sharing the amatoxin bicyclic scaffold and RNAP II mechanism.
- **Phalloidin / phallacidin** — related bicyclic heptapeptide "phallotoxins," biosynthesized by the same *Amanita* gene cluster but acting on filamentous actin rather than RNAP II; contribute to the early GI-phase symptoms, though they are poorly absorbed orally and are not the lethal principle.
- **CHEBI suggestions**: CHEBI:2828 (α-amanitin) and related CHEBI entries for β-amanitin/phalloidin (exact CHEBI IDs should be confirmed via OAK/CHEBI lookup at curation time rather than asserted from memory).

**Variant classification / population frequency**: not applicable in the ClinVar/gnomAD sense, since this is a toxin-exposure disease. No ACMG/AMP pathogenicity classification, no somatic/germline distinction, and no allele-frequency data for a "causal variant" exist. The nearest genetic-variation data relevant to the entry are the *SLCO1B3* transporter SNPs discussed in §2, which are pharmacogenomic modifiers of a xenobiotic transporter, not disease-causing variants.

**Epigenetics / chromosomal abnormalities**: none identified as relevant; not applicable to this disease category.

---

## 5. Environmental Information

**Environmental/toxic factor**: amatoxins (α-, β-, γ-amanitin) synthesized by *Amanita phalloides* and related fungi — this is itself the disease's entire environmental etiology (see §2). CHEBI/ECTO exposure-term candidates: "exposure to Amanita phalloides toxin" / "dietary exposure to mushroom toxin" (exact ECTO CURIE should be confirmed at curation via OAK lookup).

**Lifestyle factors**: wild-mushroom foraging as a recreational/subsistence activity is the dominant behavioral risk factor; regional foraging culture explains most of the geographic difference in case burden — "this difference in frequency reflects the relative popularity of mushroom foraging in Europe and Asia rather than significant differences in intrinsic toxicity or prevalence of harmful mushroom species across the regions" (search synthesis from epidemiology sources above). Restaurant/market contamination (toxic species entering food-distribution chains) is a second, distinct lifestyle-adjacent exposure route, especially documented in China/Southeast Asia ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Infectious agents**: not applicable — amatoxin poisoning is a toxidrome, not an infection.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion** of amatoxin-containing mushroom material → amatoxins (heat-stable; survive cooking) are released and rapidly absorbed from the small-intestinal mucosa into the portal circulation. This step also directly injures enterocytes (high protein-synthesis-rate cells), contributing to the early diarrhea/vomiting phase (Phase 2, §3). *Inferred/demonstrated*: demonstrated in humans and animal models.
2. Absorbed amatoxin travels via the **portal vein to the liver**, where it is taken up across the hepatocyte sinusoidal membrane predominantly by the **organic anion-transporting polypeptide OATP1B3** (gene *SLCO1B3*), with a secondary contribution from the bile-salt transporter **NTCP** (*SLC10A1*) ([PubMed 16495352](https://pubmed.ncbi.nlm.nih.gov/16495352/); [PubMed 38641045](https://pubmed.ncbi.nlm.nih.gov/38641045/)). This leads to → hepatocyte-selective toxin accumulation, explaining the liver's role as principal target organ.
3. Within the hepatocyte, entry into the cytosol/nucleus additionally requires the **N-glycan biosynthesis machinery (STT3B)**, recently identified via CRISPR screening as necessary for α-amanitin uptake at the cellular level — depleting STT3B sharply reduces toxin entry ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)). This leads to →
4. **Non-covalent, high-affinity binding of α-amanitin to RNA polymerase II** at the bridge-helix region (hydrogen-bond interaction with RNAP II residues), which blocks the enzyme's translocation step during transcription elongation ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)). This leads to →
5. **Progressive, global inhibition of mRNA synthesis**, and consequently → **failure of new protein synthesis** in cells with the highest transcriptional/translational turnover (hepatocytes, enterocytes, and renal proximal tubular epithelial cells) — the mechanistic basis for the tissue tropism of the disease (StatPearls; [PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)). This leads to →
6. **Cellular stress response and mitochondrial dysfunction**: p53 accumulates in the cytosol and translocates to mitochondria (a process reported as Bcl-2–mediated), reducing TOM20 expression and triggering **mitochondrial reactive oxygen species (ROS) generation** ([PubMed 39967828](https://pubmed.ncbi.nlm.nih.gov/39967828/) / [PMC11835023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11835023/), *Is Amanita phalloides Nephrotoxicity due to Mitochondrial Toxicity?*). Branch: cytosolic ROS may also directly activate the caspase cascade independent of the mitochondrial route.
7. **p53- and caspase-3-dependent apoptosis** of hepatocytes ensues; this is genetically demonstrated — p53/BAK-knockout mice are resistant to α-amanitin hepatotoxicity ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)). In parallel, →
8. **TNF-α upregulation** amplifies hepatocyte apoptosis and lipid peroxidation; anti-TNF antibody pretreatment in mice prevents α-amanitin liver injury, establishing this as a mechanistically necessary (not merely correlated) amplification loop ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)).
9. At the tissue level, the combination of direct transcriptional shutdown, oxidative/mitochondrial injury, and apoptosis/necrosis produces **centrilobular (zone 3) hepatic necrosis** with nucleolar disintegration, corresponding clinically to the rapid rise in transaminases and progression toward fulminant hepatic failure (Phase 4).
10. In parallel to the hepatic branch, the same RNAP II-inhibition/oxidative-stress/mitochondrial-dysfunction cascade occurs in **renal proximal tubular epithelial cells**, producing acute tubular necrosis, cell vacuolization, tubular dilatation, and interstitial edema — this can occur independently of, and sometimes outlasts, hepatic recovery ([PubMed 39967828](https://pubmed.ncbi.nlm.nih.gov/39967828/); [PMC8610939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8610939/), a case of irreversible proximal tubular necrosis).
11. Systemic consequences of hepatic failure — loss of clotting-factor synthesis (coagulopathy), loss of gluconeogenesis (hypoglycemia), impaired ammonia clearance (hyperammonemia → hepatic encephalopathy), and metabolic acidosis — converge with renal failure to produce **multiorgan failure**, the terminal common pathway leading to death without liver transplantation.
12. A separately reported extrahepatic branch: **direct amanitin cytotoxicity to hematopoietic cells** ([PMC10820516]) and possible cardiac involvement (elevated CK-MB as an independent mortality predictor, [PMC13211627]) suggest the RNAP II-inhibition mechanism is not confined to the classic three target tissues, though the mechanistic detail of cardiac/hematologic injury is less well characterized than hepatic/renal injury — this is an area of ongoing investigation rather than an established branch.

### Molecular pathways / GO terms
- **RNA polymerase II transcription inhibition**: GO:0006366 (transcription by RNA polymerase II); target protein POLR2A.
- **Apoptotic process**: GO:0006915 (apoptotic process); GO:0097194 (execution phase of apoptosis); GO:0006919 (activation of cysteine-type endopeptidase activity involved in apoptotic process) for caspase-3 activation.
- **Response to oxidative stress**: GO:0006979 (response to oxidative stress); GO:0072593 (reactive oxygen species metabolic process).
- **Mitochondrial dysfunction/mitophagy**: GO:0000422 (mitophagy); GO:0007005 (mitochondrion organization).
- **TNF signaling**: GO:0033209 (tumor necrosis factor-mediated signaling pathway).
- **Necrosis**: GO:0070265 (necrotic cell death).

### Cell types (CL terms)
- **Hepatocyte** — CL:0000182
- **Enterocyte** — CL:0000584
- **Kidney proximal tubule epithelial cell** — CL:1001016 (or CL:0002306 epithelial cell of proximal tubule)
- **Hepatic stellate cell / Kupffer cell** — potential secondary responders in the inflammatory amplification loop (not directly evidenced above but biologically plausible; do not bind without a specific citation)

### Anatomical/tissue targets (UBERON, see also §7)
- Liver (UBERON:0002107), specifically the centrilobular/zone 3 hepatic lobule region
- Kidney proximal convoluted tubule (UBERON:0004134 / UBERON:0001225 renal tubule)
- Small intestine mucosa/enterocyte layer (UBERON:0002108/UBERON:0000160)

### Omics / advanced technologies
- **Metabolomics**: an untargeted metabolomics study of 61 amatoxin poisoning patients identified 33 differential metabolites, with 11-oxo-androsterone glucuronide, glucose-6-phosphate, and glycochenodeoxycholate-3-sulfate positively correlating with hepatic injury severity ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/), citing PMID-referenced study [34]).
- **Functional genomics/CRISPR screen**: identified STT3B/N-glycan biosynthesis as a novel amanitin-entry dependency, nominating indocyanine green as a candidate inhibitor ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)).
- **Proteomics**: comparative proteomic analysis in vitro identified decreased TRiC chaperonin proteins as a novel correlate of α-amanitin hepatotoxicity ([PMC7999322](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7999322/), *Identification of Decrease in TRiC Proteins as Novel Targets of Alpha-Amanitin-Derived Hepatotoxicity by Comparative Proteomic Analysis In Vitro*).
- **Machine learning models**: a retrospective ML study of 567 critically ill mushroom-poisoning patients found extreme gradient boosting achieved AUC 0.83 (cross-validation) / 0.90 (test set), sensitivity 0.93, specificity 0.79, outperforming physician gestalt for outcome prediction ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ**: liver (UBERON:0002107) — centrilobular/zone-3 hepatocellular necrosis, the dominant lethal lesion.
- **Secondary organs**: kidney (UBERON:0002113) — acute tubular necrosis/hepatorenal syndrome; gastrointestinal tract (small intestine, colon) — enterocyte injury, and in rare cases ulcerating ileocolitis ([PMC4555452](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4555452/)); central nervous system — secondary hepatic encephalopathy (not primary CNS toxicity); hematopoietic system — reported hematotoxicity ([PMC10891511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10891511/)); cardiovascular system — elevated CK-MB reported as prognostic ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)), of uncertain primary-vs-secondary mechanism.
- **Body systems**: digestive, hepatobiliary, renal/urinary, hematologic, and (secondarily) nervous system.

**Tissue/cell level:**
- Hepatic parenchyma — hepatocytes (CL:0000182), predominantly centrilobular (zone 3) distribution.
- Renal proximal convoluted tubule epithelium (CL:1001016) — acute tubular necrosis, vacuolization, tubular dilatation, interstitial edema.
- Intestinal epithelium — enterocytes (CL:0000584).

**Subcellular level (GO Cellular Component):**
- Nucleus (GO:0005634) — site of RNAP II inhibition.
- Mitochondrion (GO:0005739) — site of ROS generation, TOM20 downregulation, p53 translocation.
- Endoplasmic reticulum (GO:0005783) — site of N-glycosylation machinery (STT3B/oligosaccharyltransferase complex, GO:0008250 oligosaccharyltransferase complex).

**Localization**: bilateral/systemic — liver and both kidneys are affected diffusely rather than laterally, consistent with a hematogenously/portally delivered toxin rather than a focal lesion.

---

## 8. Temporal Development

**Onset**: acute, toxin-exposure onset, staged over hours to days rather than an "age of onset" in the developmental sense; any age can be affected upon ingestion, with children disproportionately severely affected (§2, §3).

**Onset pattern**: acute, with a characteristic **delayed** symptom onset (6–24 h latent phase) — a diagnostically important feature distinguishing amatoxin poisoning from the near-immediate-onset mushroom toxidromes (e.g., muscarinic, ibotenic-acid) that are typically benign.

**Progression / staging** (see §3 for full phenotype detail):
1. Latent phase (0–24 h, mean ~10–12 h)
2. Gastrointestinal phase (~6–48 h onward; lasts 1–3 days)
3. Apparent convalescence (day 2–3) — false clinical improvement masking ongoing hepatic injury
4. Hepatic/multiorgan-failure phase (day 3–7+) — culminates in death (days 5–12 without treatment, per synthesis of epidemiologic sources) or, with treatment, recovery or need for liver transplantation.

**Progression rate**: variable but generally rapid once the hepatic phase begins; without treatment most fatal cases progress to death within 5–12 days of ingestion.

**Disease course pattern**: monophasic/self-limited if diagnosed and treated early (full recovery with supportive care/antidotal therapy); can be fulminant/lethal if untreated or if a large dose was ingested, irrespective of treatment.

**Remission**: treatment-induced (supportive care + antidotal therapy + possible extracorporeal support); no spontaneous remission is described once hepatic failure is established, other than in mild-dose exposures that never progress past the GI phase.

**Critical period for intervention**: the latent and early GI phase (first 24–48 h) is the critical therapeutic window — early decontamination (activated charcoal within 2–4 h) and early silibinin/NAC initiation (ideally within 24 h of ingestion) are associated with markedly better outcomes; "early therapeutic plasma exchange (within the first 24 h) improved treatment outcomes by reducing circulating toxin concentrations" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)). Recent literature explicitly recommends treating **asymptomatic** patients with a credible exposure history pre-emptively, since "the absence of early symptoms does not exclude significant toxin absorption" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

---

## 9. Inheritance and Population

**Inheritance pattern**: not applicable — amatoxin poisoning is an acquired toxic exposure, not a heritable trait. (Familial clusters occur because family members eat the same contaminated meal, not because of shared genetic susceptibility per se, though as noted in §2 shared *SLCO1B3* genotype within families is a plausible but unproven contributor to intra-family variability in severity — e.g., a Vietnamese case series describing "markedly heterogeneous outcomes" within one family exposed to the same meal.)

**Epidemiology:**
- Amatoxin-containing mushrooms cause **~50–100 fatal poisonings per year in Western Europe**, are less common in the U.S. (roughly 1–2 deaths/year), with additional cases reported from Africa, Asia, Australia, and Central/South America (search synthesis, epidemiology section above).
- Amatoxin-containing mushrooms account for **>90% of fatal mushroom-related food-poisoning deaths in the U.S.**
- **Mortality rate**: overall ~10–20% for *A. phalloides* poisoning in older series; more recent series with modern intensive care and antidotal therapy report 1.8–22% depending on treatment cohort; StatPearls reports **<5% mortality in developed countries with early intensive-care access**; historical mortality (pre-modern-treatment era) reported as ~50% in adults and ~33% in children.
- A meta-analysis of 33 studies reported a **pooled mortality estimate of ~2.87%** across all mushroom-poisoning cases and found that of 16 patients undergoing liver transplantation, 14 survived ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- A large systematic review of 506 NAC-treated patients found an **11.26% mortality rate** (including transplant cases) and a **4.35% liver-transplantation rate** ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- A Turkish liver-transplant cohort (2008–2023, n=26) reported **69.2% overall post-transplant survival**, with higher MELD scores and need for retransplantation associated with increased mortality ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Population demographics:**
- **Geographic distribution**: global, but case burden concentrated in regions with strong mushroom-foraging culture — Western/Southern Europe, and China/Southeast Asia (where *A. exitialis*, *A. fuliginea*, *Galerina sulciceps*, and *Russula subnigricans* are additionally implicated, [PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)); lower incidence in the U.S., attributed to foraging-culture prevalence rather than mushroom-species distribution differences.
- **Age distribution**: bimodal risk emphasis — young children (accidental ingestion, higher per-kg dose) and adult foragers (intentional but mistaken ingestion); pediatric poisoning is a distinct epidemiologic and clinical subgroup with its own recent 15-year retrospective analysis ([PMC12488608](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488608/)).
- **Sex ratio**: not clearly established as skewed in the sources reviewed; foraging-related exposure may somewhat favor adult recreational foragers of either sex depending on region — no robust sex-ratio statistic was identified in this search.
- **Ethnic/consanguinity/founder effects/carrier frequency**: not applicable (non-genetic disease).

---

## 10. Diagnostics

**Clinical diagnosis**: the classic pattern — asymptomatic-to-GI-symptom interval of 6–24 h after wild-mushroom ingestion, followed by rising transaminases within 2–3 days — is itself strongly diagnostic (StatPearls). Differential diagnosis must exclude acetaminophen overdose, viral/infectious hepatitis, and autoimmune hepatitis.

**Laboratory tests:**
- Complete metabolic panel, liver function tests (AST/ALT/bilirubin), coagulation studies (PT/INR), renal function (creatinine, BUN), ammonia, lactate, glucose.
- "It takes about 24 hours before any signs or laboratory indicators of liver injury begin to appear" (StatPearls) — meaning a normal initial LFT panel does not exclude poisoning.

**Toxin-specific detection (biomarkers):**
- **Urinary amatoxin quantification** is the diagnostic modality of choice; a Slovak cohort of 698 patients found "urinary amanitin examination correlated with the severity of poisoning in the range of 6–47 h after mushroom ingestion without any false negativity, while the serum assay showed no diagnostic value" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)) — establishing urine, not serum, as the correct matrix.
- Detection methods: radioimmunoassay (RIA), ELISA (detection limit ~0.2 ng/mL for α-/γ-amanitin), lateral flow immunoassay (LFIA, point-of-care, detection to ~10 ng/mL in urine but requiring LC-MS/MS confirmation given false-positive/negative risk), and liquid chromatography–high-resolution tandem mass spectrometry (LC-HRMS/MS), including magnetic-bead affinity-column extraction methods for α-, β-, γ-amanitin (multiple 2023–2024 method-development papers identified in search).
- Molecular species-identification tools: loop-mediated isothermal amplification (LAMP) assays can identify toxic mushroom species in processed/mixed food samples ("detect as low as 1% of the target species," turnaround 40–90 min) ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Imaging/other studies**: no amatoxin-specific imaging modality; abdominal imaging and cross-sectional imaging are used to assess liver morphology/complications non-specifically in fulminant hepatic failure.

**Genetic testing**: not applicable — no genetic test exists or is indicated for this toxic-exposure disease.

**Prognostic/risk-stratification scoring systems** (critical for transplant-listing decisions):
- **CLIF-OF (Chronic Liver Failure–Organ Failure) score** — a score >9 within 24 h "demonstrated excellent predictive performance and outperformed the other evaluated scoring systems" in a Chinese cohort ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- **INR > 3.6** (AUC 0.941) and **plasma ammonia > 95.1 μmol/L** (AUC 0.805) independently predict mortality ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- **King's College Hospital Criteria (KCC)** for non-acetaminophen acute liver failure — used as a general predictor of poor outcome, adapted for amatoxin-induced ALF.
- **Ganzert criteria** (amatoxin-specific): prothrombin index ≤25% combined with serum creatinine ≥106 μmol/L between days 3–10 post-ingestion ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- **Escudié criteria** (amatoxin-specific, more stringent): prothrombin index <10% (roughly INR >6) from day 4 post-ingestion, reported with "100% accuracy in predicting fatal outcome" in the deriving cohort ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- Machine-learning mortality-prediction model (XGBoost): AUC 0.83 (cross-validation)/0.90 (test), sensitivity 0.93, specificity 0.79, in 567 critically ill patients ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Screening**: no population/newborn/carrier screening applicable; the relevant "screening" analog is species-identification education and rapid toxin/species testing at point of suspected exposure (poison-control/mycologist consultation).

---

## 11. Outcome/Prognosis

**Mortality**: historically 10–20% for *A. phalloides* poisoning overall; contemporary developed-country mortality with early ICU access is **<5%** (StatPearls); a broad meta-analysis across all mushroom poisonings gives a pooled ~2.87% mortality; NAC-treated cohorts (n=506) show 11.26% mortality (including transplant cases). Untreated/late-presenting fulminant cases can approach much higher fatality, and pediatric-specific hepatotoxic-species series report case-fatality >80% in some cohorts ([PMC12488608](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488608/)).

**Time course to death (untreated)**: typically 5–12 days post-ingestion.

**Liver transplantation outcomes**: a Turkish cohort (n=26, 2008–2023) reported 69.2% overall post-transplant survival, with higher MELD score and need for retransplantation predicting worse outcome; a broader meta-analysis found 14/16 transplant recipients survived (~87.5%) ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Morbidity/complications**: hepatic encephalopathy, coagulopathy, hepatorenal syndrome, and — notably — **irreversible proximal tubular necrosis with permanent renal impairment even after hepatic recovery** ([PMC8610939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8610939/)); rare ulcerating ileocolitis ([PMC4555452](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4555452/)); reported hematotoxicity ([PMC10891511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10891511/)).

**Prognostic factors** (see §10 for the formal scoring systems): amount ingested, species ingested, time to treatment initiation, INR/prothrombin index trajectory, plasma ammonia, CLIF-OF score, elevated CK-MB and impaired consciousness (markers of extrahepatic organ involvement) ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Recovery potential**: full hepatic and renal recovery is common when treatment (decontamination + silibinin/NAC ± extracorporeal support) is started early; recovery is markedly less likely once grade ≥2 hepatic encephalopathy, INR >3.6–6, or CLIF-OF >9 are reached without transplantation.

---

## 12. Treatment

**Decontamination:**
- **Activated charcoal**, 1 g/kg, repeated every 2–4 h, ideally started within 2–4 h of ingestion to reduce absorption and interrupt enterohepatic recirculation of amatoxin (StatPearls). NCIT: **NCIT:C1687** (Activated Charcoal) or a general decontamination procedure term.

**Antidotal pharmacotherapy:**
- **Silibinin (silymarin/Legalon-SIL)** — first-line antidote; competitively inhibits **OATP1B3**-mediated hepatocyte uptake of amatoxin and interrupts enterohepatic recirculation; also has anti-TNF/anti-apoptotic action. Dosing: IV silibinin 5 mg/kg over 1 h, then 20 mg/kg/day continuous infusion (or oral silymarin 1 g four times daily) (StatPearls; [PMC3414726](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3414726/), *Legalon SIL: The Antidote of Choice*). NCIT candidate: therapeutic_agent CHEBI silibinin, treatment_term NCIT:C15986 (Pharmacotherapy).
- **N-acetylcysteine (NAC)** — IV, using acetaminophen-poisoning-style dosing regimens; acts as a glutathione precursor/free-radical scavenger, targeting the oxidative-stress arm of the mechanism (§6). A Thai cohort of 74 NAC-treated patients: "70 (94.59%) were successfully treated at a low cost" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- **Benzylpenicillin G (high-dose)** — historically used, "four million units every four hours," proposed to competitively inhibit hepatic amatoxin uptake, but comparative evidence shows it is inferior to silibinin: "In nearly 1,500 documented cases, overall mortality in patients treated with silibinin is <10% compared to >20% when using penicillin or a combination of silibinin and penicillin" (search synthesis, treatment section). A Slovak comparative study (2004–2020, n=141) found silibinin **monotherapy** had significantly *higher* treatment failure than **combined** penicillin G + silibinin (41.67% vs 1.57%; p=0.00058) — an apparent discrepancy across studies that should be flagged in curation as reflecting differing cohorts/eras/outcome definitions rather than a settled consensus ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- **Cyclosporine** — an OATP transporter inhibitor with only limited case-report-level support (StatPearls).

**Extracorporeal / blood-purification therapy:**
- **Therapeutic plasma exchange (TPE)** — increasingly supported as adjunctive therapy: in patients with hepatic encephalopathy grade ≥2, adjunctive TPE was "associated with improved liver transplant-free survival at 28 days" and "independently associated with reduced risk of death or liver transplantation" (multi-center Amanita-PEX study, [PMC12573913](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12573913/)); a Turkish cohort found early TPE (within 24 h) improved outcomes by reducing circulating toxin ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)); recommended replacement fluid: 5% albumin and fresh frozen plasma.
- **Combined plasma exchange + double plasma molecular adsorption system (DPMAS)** — used successfully as a bridge to transplantation/recovery in a Chinese pediatric series ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- **Molecular Adsorbent Recirculating System (MARS)** and hemoperfusion — additional extracorporeal modalities reported in case series (e.g., a Vietnamese familial case series using haemoperfusion and plasma exchange, PMID 42523156).
- **Standard hemodialysis** — used for renal failure but does not itself remove circulating amatoxin (StatPearls).

**Liver transplantation:** definitive therapy for established/progressing fulminant hepatic failure; timing guided by the transplant-specific prognostic criteria in §10 (King's College, Ganzert, Escudié criteria). Reported outcomes: 69.2% overall survival in a 26-patient Turkish cohort; 14/16 survival in a broader meta-analytic sample ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)). NCIT: **NCIT:C15289** (Organ Transplantation).

**Supportive care:** aggressive IV fluid resuscitation (the "Santa Cruz protocol" AMP regimen's first pillar — "aggressive intravenous fluid replacement to completely reverse prerenal azotemia and protect kidneys"), electrolyte correction, glucose monitoring/correction, correction of coagulopathy, and ICU-level monitoring. NCIT: **NCIT:C15747** (Supportive Care).

**Emerging/experimental therapeutics:**
- **Indocyanine green** as a candidate STT3B inhibitor blocking cellular amanitin entry — shown protective in cellular and animal models ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)); not yet a clinical standard.
- **Resveratrol** — experimental anti-inflammatory agent reducing hepatic mononuclear infiltration, necrosis, and caspase-3 positivity in animal models ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).
- ***Ganoderma lucidum* supplementation** — a retrospective Chinese study (n=61) found statistically significantly shorter hospital stay (6.69±3.98 vs 9.27±5.30 days; p=0.034) and lower cost associated with adjunct use ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)) — hypothesis-generating rather than confirmatory.

**Notable unrelated biomedical repurposing (not a treatment for the disease, but relevant molecular context)**: α-amanitin itself is being repurposed as a cytotoxic payload for **antibody-drug conjugates (ADCs)** in oncology — e.g., PSMA-targeted amanitin-ADCs for prostate cancer (HDP-103) and TROP2-targeted amanitin-ADCs for pancreatic cancer, exploiting RNAP II inhibition's cell-cycle-independent cytotoxicity against slowly dividing/dormant tumor cells (AACR abstracts, 2024–2026 search results). This is a translational application of the toxin, not a treatment of amatoxin poisoning itself, but is directly relevant to the toxin's molecular mechanism narrative and to `therapeutic_modality`/mechanism cross-references if the KB models amanitin as a chemical entity.

**Treatment algorithm summary** (as codified in "Santa Cruz"/AMP-style protocols): (1) aggressive fluid resuscitation, (2) early activated charcoal if within the decontamination window, (3) IV silibinin ± NAC ± penicillin G started as early as possible (even in asymptomatic exposed patients), (4) escalation to plasma exchange/DPMAS/MARS for progressive coagulopathy or encephalopathy, (5) transplant evaluation using amatoxin-specific (Ganzert/Escudié) or general (King's College) criteria once transplant-threshold criteria are met.

---

## 13. Prevention

**Primary prevention:**
- **Public education** is repeatedly emphasized as the single most important preventive measure: "the key to preventing mushroom poisoning is education of the public" ([PMC12488608](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488608/); StatPearls). StatPearls explicitly recommends: "do not eat wild mushrooms but instead buy them from a grocery store," and to wash commercially purchased mushrooms to remove pesticide residue.
- Physician education/training: "there is a need to enhance training for primary care physicians so that they can recognize the characteristics of amatoxin poisoning and be equipped with the relevant treatment methods" ([PMC12488608](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488608/)).
- Molecular/rapid species-identification tools (LAMP assays, point-of-care LFIA urine tests) support both prevention (screening food-chain samples/markets) and early diagnosis.

**Secondary prevention (early detection):** low threshold for urinary amatoxin testing and treatment initiation in any patient with a credible wild-mushroom exposure history, even while still asymptomatic — because "the absence of early symptoms does not exclude significant toxin absorption" ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)); regional poison-control-center and mycologist consultation networks for rapid species identification (StatPearls).

**Tertiary prevention:** early antidotal therapy and extracorporeal support to prevent progression to irreversible hepatic/renal failure and the need for transplantation (§12).

**Immunization**: not applicable (no vaccine exists or is relevant).

**Genetic/prenatal screening, counseling**: not applicable — non-genetic disease.

**Public health / environmental interventions:** regulation and inspection of wild-foraged mushrooms entering commercial food-distribution and market/catering chains, particularly in regions (China, Southeast Asia) where this route of exposure is documented ([PMC13211627](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)).

**Prophylaxis**: no pre-exposure prophylactic medication exists; "prophylaxis" in practice means avoiding wild-mushroom consumption and, once exposure is suspected, immediate presentation for antidotal therapy within the critical early treatment window (§8).

---

## 14. Other Species / Natural Disease

**Taxonomy of causal organism**: *Amanita phalloides* (NCBITaxon:33397), *Amanita virosa*, *Amanita verna*, *Amanita exitialis*, *Amanita fuliginea*, *Galerina marginata*/*sulciceps*, various *Lepiota* spp. — the fungal source organisms, not the affected host species.

**Naturally occurring disease in other species:**
- **Dogs** are the most extensively documented non-human natural host, with numerous veterinary case reports and case series of accidental *Amanita* ingestion. "*Amanita phalloides*, the death cap mushroom, is the most common cause of potentially fatal mushroom poisoning in people and dogs" (search synthesis). A case series of 5 dogs treated with an adapted human "Santa Cruz protocol" reported **100% survival to discharge** ([PubMed 33458945](https://pubmed.ncbi.nlm.nih.gov/33458945/); Goupil et al., *J Vet Emerg Crit Care* 2021). A separate case report documents fatal Amanita toxicosis with acute hepatic necrosis in a dog (Puschner et al., *J Vet Diagn Invest* 2007, PMID referenced via sagepub 104063870701900317).
- **Cats** are also affected, per veterinary toxicology reviews (North American Mycological Association resource).
- **Beagle dogs** have been used as a deliberate experimental model for *Amanita exitialis* toxicokinetics (ScienceDirect, *Toxicity and toxicokinetics of Amanita exitialis in beagle dogs*).

**Comparative pathology / cross-species susceptibility (mechanistic, see also §15):**
- **Species-dependent oral absorption and lethality** is well documented: "the rate of absorption of amanitins from the gastrointestinal tract varies with the animal species and is estimated to be much greater in dogs than in mice and rabbits; rats appear relatively resistant to the toxic effects of amanitins" (Merck Veterinary Manual / search synthesis). Mice are essentially unaffected by *oral* Amanita ingestion (unlike humans and dogs) but succumb rapidly (8–10 h) to a lethal **intraperitoneal** dose — a key reason mice are a poor natural-exposure model despite being used for parenteral mechanistic studies.
- Estimated oral LD50: α-amanitin ≈0.1 mg/kg in humans; methyl-γ-amanitin LD50 ≈0.5 mg/kg in dogs (similar order of magnitude).
- In dogs, 80–90% of ingested amatoxin is rapidly renally excreted, with the remaining 10–20% undergoing enterohepatic recirculation back to the liver — directly paralleling the human mechanism that silibinin therapeutically interrupts.

**Zoonotic potential**: not applicable — this is direct environmental toxin exposure common to multiple species independently ingesting the same fungal source, not a transmissible disease between species.

---

## 15. Model Organisms

**In vivo models:**
- **Dogs** — the preferred large-animal natural/experimental model, given (a) documented spontaneous natural poisoning closely paralleling human disease course and (b) high oral bioavailability of amatoxins comparable to humans, in contrast to mice/rats. Used both for observational veterinary case data and deliberate toxicokinetic study (beagle *A. exitialis* model).
- **Mice** — used extensively for **mechanistic** (not natural-exposure) studies via intraperitoneal α-amanitin dosing; the basis for the p53/BAK-knockout apoptosis-resistance experiments and the anti-TNF-antibody hepatoprotection experiments underlying the pathophysiology model in §6 ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)). **Limitation**: mice are resistant to *oral* Amanita ingestion and die rapidly (8–10 h) after IP dosing, so the mouse IP model recapitulates the *molecular* mechanism but not the *natural exposure route or the human multi-phase clinical timeline*.
- **Rats** — relatively resistant to amanitin toxicity compared to dogs/mice/rabbits by the oral route; used in some nephrotoxicity mechanistic studies (e.g., β-carotene protection against α-amanitin nephrotoxicity via modulation of oxidative/autophagic/nitric-oxide/polyol pathways in rat kidney, ScienceDirect 2024).
- **Rabbits** — mentioned comparatively in absorption-kinetics literature but with less detailed primary data identified in this search.

**In vitro / cellular models:**
- **HepG2 cells** — the principal human hepatocyte-line model for OATP1B3-dependent amanitin cytotoxicity studies, including the OATP1B3-knockdown protection experiments ([PubMed 38641045](https://pubmed.ncbi.nlm.nih.gov/38641045/)) and comparative proteomic (TRiC-protein) studies ([PMC7999322](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7999322/)).
- **Primary/cultured human hepatocytes** — used in the original OATP1B3/NTCP transporter-characterization work and in silibinin/NAC/penicillin G antidote-efficacy comparisons in vitro ("Benzylpenicillin, acetylcysteine and silibinin as antidotes in human hepatocytes intoxicated with α-amanitin," ScienceDirect).
- **Cultured hematopoietic cell lines** — used to demonstrate direct amanitin hematotoxicity independent of hepatic mechanisms ([PMC10820516]).
- **CRISPR knockout cell-line screens** — used to identify STT3B/N-glycan biosynthesis as a novel amanitin cellular-entry dependency ([PMC11640968](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)).
- **3D liver spheroid / iPSC-derived hepatocyte organoid models** — general hepatotoxicology platforms (HepG2 spheroids, iPSC-hepatocyte spheroids, HepaRG) exist and are increasingly used for hepatotoxicant screening broadly, but **no amatoxin-specific organoid/iPSC study was identified** in this search — this is a plausible near-term research gap (an experimental-model limitation worth flagging in a KB entry rather than asserting a positive finding).

**Model characteristics — phenotype recapitulation and limitations:**
- The **canine model most faithfully recapitulates human natural-exposure disease** (oral route, similar absorption kinetics, similar hepatorenal clinical course, and demonstrated response to a human-derived treatment protocol).
- The **mouse IP model faithfully recapitulates the molecular mechanism** (RNAP II inhibition → p53/caspase-3 apoptosis → TNF-amplified hepatocyte injury) but **does not recapitulate** the natural oral-exposure route, the multi-day staged clinical course, or the renal proximal-tubule injury pattern as well as the hepatic injury pattern.
- **HepG2/primary hepatocyte in vitro models** faithfully recapitulate OATP1B3-dependent uptake and antidote pharmacology (silibinin, NAC, penicillin G competition) but cannot model the whole-organism multi-organ (renal, GI, hematologic) phenotype or the enterohepatic recirculation dynamics that silibinin's therapeutic rationale depends on in vivo.

**Model databases/resources**: MGI (mouse *Tp53*, *Bak1* knockout strains used in the apoptosis experiments), general toxicology repositories; no dedicated amatoxin-poisoning model registry was identified.

---

## Summary of Suggested Ontology Term Bindings for KB Curation

| Category | Suggested term(s) | Notes |
|---|---|---|
| Disease/MeSH | MeSH:D009145 (Mushroom Poisoning) | No dedicated amatoxin MeSH heading; no MONDO/OMIM/Orphanet ID found |
| ICD-10-CM | T62.0X1- (+ 7th character) | Toxic effect of ingested mushrooms |
| Causal chemical entities | CHEBI (α-amanitin, β-amanitin, phalloidin) | Confirm exact CHEBI CURIEs via OAK lookup, not from memory |
| Host target gene | HGNC: POLR2A | RNA polymerase II, direct binding target |
| Uptake transporter genes | HGNC: SLCO1B3 (OATP1B3), SLC10A1 (NTCP) | Hepatocyte uptake |
| Novel entry factor | STT3B (N-glycan biosynthesis) | CRISPR-screen-identified |
| Apoptosis genes | TP53, BAK1 (BAK), caspase-3 (CASP3) | Mouse knockout evidence |
| Amplifier | TNF | Anti-TNF antibody prevents injury in mice |
| GO biological processes | GO:0006366 (RNAP II transcription), GO:0006915 (apoptosis), GO:0006979 (oxidative stress response), GO:0000422 (mitophagy), GO:0033209 (TNF signaling), GO:0070265 (necrotic cell death) | |
| Cell types (CL) | CL:0000182 (hepatocyte), CL:0000584 (enterocyte), proximal tubule epithelial cell | |
| Anatomy (UBERON) | UBERON:0002107 (liver), renal proximal tubule, small intestine | |
| Phenotypes (HP) | HP:0002014 (diarrhea), HP:0002013 (vomiting), HP:0002910 (elevated transaminases), HP:0000952 (jaundice), HP:0002480 (hepatic encephalopathy), HP:0006554 (acute hepatic failure), HP:0001919 (acute kidney injury), HP:0001943 (hypoglycemia), HP:0001942 (metabolic acidosis) | Verify exact IDs at curation time |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent silibinin/NAC; NCIT:C15289 (Organ Transplantation); NCIT:C15747 (Supportive Care) | |

---

## Sources

- [Amatoxin Mushroom Toxicity — StatPearls (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK431052/)
- [Amatoxin Intoxication and Wild Mushroom Poisoning: Current Advances in Diagnosis, Risk Stratification, and Clinical Management (PMC13211627 / Toxins 2026, 18(5):216)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211627/)
- [Amanita phalloides-Associated Liver Failure: Molecular Mechanisms and Management (PMC11640968)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11640968/)
- [Review of present knowledge on the pathogenesis and pathophysiology of Amanita phalloides poisoning (PMID 8370055)](https://pubmed.ncbi.nlm.nih.gov/8370055/)
- [Amanita phalloides poisoning: Mechanisms of toxicity and treatment (PMID 26375431)](https://pubmed.ncbi.nlm.nih.gov/26375431/)
- [Acute Liver Failure Caused by Amanita phalloides Poisoning (PMC3395149)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3395149/)
- [Toxic Effects of Amanitins: Repurposing Toxicities toward New Therapeutics (PMC8230822)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8230822/)
- [Identification of Decrease in TRiC Proteins as Novel Targets of Alpha-Amanitin-Derived Hepatotoxicity (PMC7999322)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7999322/)
- [Potential value of urinary amatoxin quantification (PMID 30565383)](https://pubmed.ncbi.nlm.nih.gov/30565383/)
- [From liver injury to failure: predictive biomarkers (PMID 40645529)](https://pubmed.ncbi.nlm.nih.gov/40645529/)
- [Comprehensive Clinical Profile of Amanita exitialis Poisoning (PMC12737360)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12737360/)
- [Amanita phalloides Mushroom Poisonings — Northern California, 2016 (PMC5657817)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5657817/)
- [Legalon SIL: The Antidote of Choice (PMC3414726)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3414726/)
- [Molecular characterization and inhibition of amanitin uptake into human hepatocytes (PMID 16495352)](https://pubmed.ncbi.nlm.nih.gov/16495352/)
- [Amanitin-induced variable cytotoxicity mediated by OATP1B3 expression (PMID 38641045)](https://pubmed.ncbi.nlm.nih.gov/38641045/)
- [Unexpected Amanita phalloides-Induced Hematotoxicity (PMC10891511)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10891511/)
- [Amanitin intoxication: effects of therapies on clinical outcomes – 40 years review](https://www.tandfonline.com/doi/full/10.1080/15563650.2022.2098139)
- [Treatment of amatoxin poisoning: 20-year retrospective analysis (PMID 12475187)](https://pubmed.ncbi.nlm.nih.gov/12475187/)
- [Extensive proximal tubular necrosis following Amanita phalloides ingestion (PMC8610939)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8610939/)
- [Is Amanita phalloides Nephrotoxicity due to Mitochondrial Toxicity? (PMC11835023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11835023/)
- [Clinical recovery of 5 dogs from amatoxin mushroom poisoning using an adapted Santa Cruz protocol (PMID 33458945)](https://pubmed.ncbi.nlm.nih.gov/33458945/)
- [Toxicity and toxicokinetics of Amanita exitialis in beagle dogs](https://www.sciencedirect.com/science/article/abs/pii/S0041010118300199)
- [Diagnosis of Amanita Toxicosis in a Dog with Acute Hepatic Necrosis](https://journals.sagepub.com/doi/10.1177/104063870701900317)
- [Epidemiology and clinical aspect of pediatric mushroom poisonings: 15-year retrospective analysis (PMC12488608)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488608/)
- [MeSH Browser: Mushroom Poisoning (D009145)](https://meshb.nlm.nih.gov/record/ui?ui=D009145)
- [ICD-10-CM T62.0X1A](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T62-/T62.0X1A)
- [Ulcerating Ileocolitis in Severe Amatoxin Poisoning (PMC4555452)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4555452/)
- [Unraveling Hematotoxicity of α-Amanitin in Cultured Hematopoietic Cells (PMC10820516)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10820516/)
- [Abstract: Amanitin-based antibody-drug conjugates targeting PSMA](https://aacrjournals.org/cancerres/article/74/19_Supplement/664/598047/Abstract-664-Amanitin-based-antibody-drug)
- [Novel Amanitin-Based Antibody–Drug Conjugates Targeting TROP2 for Pancreatic Cancer](https://aacrjournals.org/mct/article/24/4/485/754278/Novel-Amanitin-Based-Antibody-Drug-Conjugates)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 11 |
| References weighed for topical relevance | 27 |
| On topic | 21 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC13211627` *(abstract only)*: "misidentification during collection, unintentional mixing of edible and toxic species"
  - closest text in source: "Liquid chromatography, mass spectrometry, immunoassays, and the molecular identification of fungal species have improved diagnostic precision, particularly in cases with uncertain exposure history or delayed presentation"
- `PMC:PMC13211627` *(abstract only)*: "the transient improvement phase preceding severe organ toxicity"
  - closest text in source: "Future research should prioritize standardized diagnostic pathways, validated prognostic models, and clinically applicable treatment algorithms that support earlier escalation of care in severe mushroom intoxication."
- `PMC:PMC13211627` *(abstract only)*: "demonstrated excellent predictive performance and outperformed the other evaluated scoring systems"
  - Text part not found as substring: 'demonstrated excellent predictive performance and outperformed the other evaluated scoring systems' (note: only abstract available for PMID:42188618, full text may contain this excerpt)
- `PMC:PMC13211627` *(abstract only)*: "early therapeutic plasma exchange (within the first 24 h) improved treatment outcomes by reducing circulating toxin concentrations"
  - closest text in source: "Overall, clinical outcome depends not only on toxin profile, but also on timely diagnosis, accurate early risk stratification, and prompt coordinated treatment"
- `PMC:PMC13211627` *(abstract only)*: "the absence of early symptoms does not exclude significant toxin absorption"
  - closest text in source: "Overall, clinical outcome depends not only on toxin profile, but also on timely diagnosis, accurate early risk stratification, and prompt coordinated treatment"
- `PMC:PMC13211627` *(abstract only)*: "urinary amanitin examination correlated with the severity of poisoning in the range of 6–47 h after mushroom ingestion without any false negativity, while the serum assay showed no diagnostic value"
  - closest text in source: "This review examines recent advances in the diagnosis, risk stratification, and therapeutic management of wild mushroom poisoning, with amatoxin intoxication serving as the principal clinical focus"
- `PMC:PMC13211627` *(abstract only)*: "70 (94.59%) were successfully treated at a low cost"
  - Text part not found as substring: '70 (94.59%) were successfully treated at a low cost' (note: only abstract available for PMID:42188618, full text may contain this excerpt)
- `PMC:PMC12573913` *(abstract only)*: "independently associated with reduced risk of death or liver transplantation"
  - closest text in source: "PEX was independently associated with reduced risk of the combined endpoint death or liver transplantation within 28 days from inclusion in patients with HE grade ≥ 2 (HR 0.37, 95%-CI 0.19-0.73, p = 0.004)"
- `PMC:PMC12488608` *(abstract only)*: "the key to preventing mushroom poisoning is education of the public"
  - closest text in source: "BACKGROUND: Mushroom poisoning is a significant public health concern, particularly in pediatric populations, where developmental differences in toxin metabolism and organ vulnerability pose unique clinical challenges"
- `PMC:PMC12488608` *(abstract only)*: "there is a need to enhance training for primary care physicians so that they can recognize the characteristics of amatoxin poisoning and be equipped with the relevant treatment methods"
  - closest text in source: "Despite its geographic and seasonal patterns, pediatric mushroom poisoning remains underrepresented in the literature, necessitating further investigation into its epidemiological and clinical characteristics"
- `PMC:PMC13211627` *(abstract only)*: "the absence of early symptoms does not exclude significant toxin absorption"
  - closest text in source: "Overall, clinical outcome depends not only on toxin profile, but also on timely diagnosis, accurate early risk stratification, and prompt coordinated treatment"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CHEBI:2828` (1 mention) - the report calls it "α-amanitin"; CHEBI calls it **Arnebinone**
- `CL:1001016` (2 mentions) - the report calls it "Renal proximal convoluted tubule epithelium"; CL calls it **kidney loop of Henle ascending limb epithelial cell**
- `UBERON:0002107` (3 mentions) - the report calls it "Liver", "Primary organ**: liver", "liver"; UBERON calls it **liver**
- `NCBITaxon:33397` (1 mention) - the report calls it "Amanita phalloides"; NCBITaxon calls it **Chironomus plumosus**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006919` (obsolete activation of cysteine-type endopeptidase activity involved in apoptotic process) (1 mention)
- `GO:0070265` (obsolete necrotic cell death) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006919` (1 mention) - the report calls it "activation of cysteine-type endopeptidase activity involved in apoptotic process"; GO calls it **obsolete activation of cysteine-type endopeptidase activity involved in apoptotic process**
- `GO:0000422` (2 mentions) - the report calls it "mitophagy"; GO calls it **autophagy of mitochondrion**, and lists "mitophagy" among its other names
- `GO:0070265` (2 mentions) - the report calls it "necrotic cell death"; GO calls it **obsolete necrotic cell death**
- `CL:0000182` (3 mentions) - the report calls it "Hepatic parenchyma — hepatocytes"; CL calls it **hepatocyte**
- `CL:0000584` (3 mentions) - the report calls it "Intestinal epithelium — enterocytes"; CL calls it **enterocyte**, and lists "mature enterocyte" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Secondary organs**: kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002107` - called "Liver", "Primary organ**: liver", "liver"
