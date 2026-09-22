---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-01T10:43:16.703054'
end_time: '2026-09-01T10:47:19.742763'
duration_seconds: 243.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infantile-Onset Pompe Disease
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 19
  num_turns: 21
  total_cost_usd: 1.3501074
  session_id: f6b940e1-15b7-538d-b954-76b625bf5c27
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile-Onset Pompe Disease** covering all of the
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

I'll research this systematically across multiple searches, then compile the full report.

Good foundational data. Let me dig deeper into gene therapy, phenotypes/HPO, cardiac mechanism, diagnostics, animal models, and immune tolerance induction.

I now have comprehensive data across all major domains. Let me compile the full research report.

# Infantile-Onset Pompe Disease (IOPD): Comprehensive Research Report

## 1. Disease Information

**Overview.** Infantile-onset Pompe disease (IOPD; classic infantile glycogen storage disease type II) is the most severe form of a spectrum of autosomal recessive lysosomal storage disorders caused by biallelic pathogenic variants in *GAA*, encoding acid α-glucosidase (acid maltase). Deficient GAA activity (typically <1% of normal in classic IOPD) causes progressive lysosomal glycogen accumulation, most critically in cardiac and skeletal muscle, producing hypertrophic cardiomyopathy, profound hypotonia, and respiratory failure with death, if untreated, typically within the first year to two years of life from cardiorespiratory insufficiency ([OMIM 232300](https://www.omim.org/entry/232300); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1261/)).

**Key identifiers:**
- **OMIM (phenotype):** #232300 — Pompe Disease, Infantile-Onset (IOPD); related entries #606800 (GAA gene) and #621314 (late-onset Pompe disease, LOPD)
- **Orphanet:** ORPHA:79258 (glycogen storage disease type II, infantile onset)
- **MONDO:** MONDO:0009291 (glycogen storage disease II, infantile onset) — parent disease group MONDO:0008608 (glycogen storage disease II / Pompe disease)
- **ICD-10-CM:** E74.02 (Pompe disease); **ICD-11:** 5C51.0 (glycogen storage disease type II)
- **MeSH:** D006008 (Glycogen Storage Disease Type II)
- **Gene:** GAA (HGNC:4065), locus 17q25.3 ([OMIM *606800](https://www.omim.org/entry/606800))

**Synonyms:** Glycogen storage disease type II (GSD II); acid maltase deficiency (AMD); acid α-1,4-glucosidase deficiency; glycogenosis type II.

**Evidence base composition.** Knowledge derives from a mixture of (a) individual case reports and small case series (predominant in the pre-newborn-screening era and for rare genotypes); (b) larger aggregated multicenter cohorts and disease registries, notably the **Pompe Registry** (Sanofi/Genzyme-sponsored, international, >1,000 patients) and national newborn-screening (NBS) cohorts (Taiwan, Illinois, Missouri, Pennsylvania, California); and (c) mechanistic/biochemical studies using patient fibroblasts, iPSC-derived cardiomyocytes, and murine/canine models. A 2024 aggregated biochemical/genetic study screened >30,000 samples from 57 countries, identifying 723 confirmed Pompe cases and 283 distinct *GAA* alterations (98 novel) ([Balendran-Braun et al., 2024, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11918499/)).

---

## 2. Etiology

**Primary cause — genetic.** IOPD is caused by **biallelic pathogenic (predominantly loss-of-function) variants in *GAA*** that reduce residual GAA enzymatic activity to <1% of normal. Autosomal recessive inheritance; both parents are typically obligate heterozygous carriers.

**Genotype-severity correlation.** Residual GAA activity roughly correlates with age of onset and severity: null/null genotypes (two alleles producing no functional protein, e.g., large deletions, frameshift, nonsense variants) generally produce the most severe classic IOPD phenotype, whereas genotypes retaining even a small amount of residual activity (e.g., one allele with a leaky splice variant) tend toward later-onset, milder disease ([Peruzzo et al., Ann Transl Med](https://atm.amegroups.org/article/view/25187/html)).

**Risk factors:**
- *Genetic:* Homozygosity or compound heterozygosity for null/severe *GAA* variants. Recurrence risk 25% per pregnancy for carrier couples; prenatal and carrier testing available.
- *Population/ethnic:* Certain pathogenic variants show founder/ethnic enrichment — e.g., **c.2560C>T (p.Arg854Ter)** is common in African American patients and frequently produces the CRIM-negative (cross-reactive immunologic material–negative) phenotype; the splice variant **c.-32-13T>G** is the most common pathogenic allele overall (especially in individuals of Caucasian/European ancestry) but, because it retains partial residual activity, is typically associated with **late-onset** rather than infantile disease when paired with a milder second allele ([Rare Disease Advisor — Etiology](https://www.rarediseaseadvisor.com/disease-info-pages/pompe-disease-etiology/); [PMC7467391](https://pmc.ncbi.nlm.nih.gov/articles/PMC7467391/)).
- *Environmental:* No established environmental, infectious, or lifestyle causal factors; this is a purely monogenic Mendelian disorder. There is no known gene-environment interaction modifying IOPD risk, though nutritional/caloric status and intercurrent respiratory infections influence clinical course and survival once disease is present.

**Protective factors:** None specific to genetic susceptibility (no known protective alleles). The major modifiable "protective" factor in outcome (not causation) is **early diagnosis via newborn screening and prompt initiation of enzyme replacement therapy (ERT)**, which is strongly associated with improved survival and motor outcomes ([PMC7422965](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422965/)).

**Pseudodeficiency alleles.** Common *GAA* pseudodeficiency variants (notably c.1726G>A and c.2065G>A, enriched in Asian populations) reduce measured enzyme activity in screening assays without causing disease, creating a diagnostic pitfall in NBS programs that must be resolved by second-tier molecular testing.

---

## 3. Phenotypes

IOPD is defined operationally by **onset before 12 months of age with hypertrophic cardiomyopathy** ("classic" IOPD) versus a **"non-classic" infantile** subtype with onset in the first year but without (or with minimal) cardiomyopathy ([PMC7422965](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422965/)).

| Phenotype | Frequency (untreated classic IOPD cohorts) | Suggested HPO term |
|---|---|---|
| Generalized hypotonia ("floppy baby") | ~96% (motor delay) | HP:0001252 Hypotonia |
| Hypertrophic cardiomyopathy / cardiomegaly | ~92% | HP:0001639 Hypertrophic cardiomyopathy; HP:0001640 Cardiomegaly |
| Hepatomegaly | ~90% | HP:0002240 Hepatomegaly |
| Macroglossia | ~62% | HP:0000158 Macroglossia |
| Feeding difficulties / poor suck | common | HP:0011968 Feeding difficulties |
| Failure to thrive / poor growth | common | HP:0001508 Failure to thrive |
| Respiratory distress / weakness | progressive, near-universal untreated | HP:0002098 Respiratory distress; HP:0002747 Recurrent respiratory infections |
| Short PR interval / WPW pattern | frequent in infancy | HP:0005165 Short PR interval; HP:0001712 Wolff-Parkinson-White syndrome pattern |
| Motor developmental delay | ~96% | HP:0001270 Motor delay |
| Muscle weakness (proximal) | universal, progressive | HP:0003324 Generalized muscle weakness |
| Areflexia/hyporeflexia | common | HP:0001265 Hyporeflexia |
| Sensorineural hearing loss (subset) | reported in survivors | HP:0000407 |
| White-matter abnormalities / cognitive decline (long-term survivors) | emerging in ERT-treated survivors | HP:0002500 (leukoencephalopathy pattern); HP:0001249 Intellectual disability |

**Characteristics:**
- **Onset:** Classic IOPD presents within days to a few months of birth (median ~2 months); non-classic infantile onset is later in the first year.
- **Severity/progression:** Rapidly progressive without treatment — cardiac hypertrophy with left ventricular outflow obstruction, worsening hypotonia, and cardiorespiratory failure culminate in death, historically at a median age of ~6–8.7 months, with essentially universal mortality by 1–2 years untreated.
- **Quality of life impact:** Even in ERT-treated long-term survivors, cumulative burden includes ventilator dependence (invasive or non-invasive), wheelchair use, hearing loss, and — increasingly recognized as survival extends — progressive CNS white-matter disease and cognitive decline, since ERT does not cross the blood–brain barrier ([Ebbink et al. 2018](https://onlinelibrary.wiley.com/doi/10.1111/dmcn.13740); [Dorpel et al. 2024, JIMD](https://onlinelibrary.wiley.com/doi/10.1002/jimd.12736)).

---

## 4. Genetic/Molecular Information

**Causal gene:** *GAA* (acid alpha-glucosidase; HGNC:4065), 17q25.3, OMIM *606800. Encodes a lysosomal glycoside hydrolase (EC 3.2.1.20) that hydrolyzes the α-1,4 and α-1,6 glucosidic linkages of glycogen to free glucose within the lysosome.

**Pathogenic variant spectrum:** Approximately 400+ pathogenic *GAA* variants reported (missense, nonsense, frameshift, splice-site, small indels, and rare large deletions/duplications). Classic IOPD is typically caused by variants abolishing essentially all enzyme activity/protein production (null alleles) in trans on both chromosomes.

- Example pathogenic variants: **c.2560C>T (p.Arg854Ter)** — nonsense, frequent in African-descent CRIM-negative patients; **c.525delT** and **c.2481+102_2646+31del (exon 18 deletion)** — common "Dutch" founder null alleles; **c.1935C>A (p.Asp645Glu)** — used to generate a knock-in mouse model recapitulating IOPD.
- The **c.-32-13T>G (IVS1)** splice variant is the most prevalent pathogenic allele population-wide (allele frequency 40–70% among Caucasian late-onset patients) but produces only partial (10–20%) residual normal splicing/enzyme, so it is generally associated with LOPD rather than IOPD unless paired with an unusually severe modifying context.
- **Variant classification** follows ACMG/AMP criteria via ClinVar; e.g., c.2237G>C (p.Trp746Ser) classified pathogenic, c.266G>A (p.Arg89His) likely pathogenic ([PMC10433214](https://pmc.ncbi.nlm.nih.gov/articles/PMC10433214/)).
- **Population frequency:** gnomAD/ExAC/TOPMed catalog carrier frequencies; pathogenic and pseudodeficiency allele frequencies both vary substantially by ancestry, complicating NBS.

**Functional consequence:** Predominantly **loss of function** — absent, truncated, misfolded, or catalytically dead GAA protein. Missense variants can cause misfolding with ER retention/degradation or reduced catalytic efficiency.

**CRIM status.** A major molecular/immunologic axis specific to treatment: **CRIM-negative** patients (no detectable endogenous GAA protein, typically due to null/null genotypes such as homozygous c.2560C>T) mount high-titer neutralizing antibody responses against recombinant GAA (rhGAA) ERT that abolish efficacy unless immune tolerance induction is used; **CRIM-positive** patients (some residual, even non-functional, immunoreactive protein) generally respond better and sustain lower antibody titers ([PubMed 26693141](https://pubmed.ncbi.nlm.nih.gov/26693141/)).

**Modifier genes / epigenetics:** No well-established modifier genes for IOPD severity are established beyond *GAA* genotype itself; epigenetic contributions are not well characterized for this disorder.

**Chromosomal abnormalities:** Not a chromosomal disorder; no aneuploidy/translocation etiology.

---

## 5. Environmental Information

IOPD is a monogenic disorder with **no causal environmental, infectious, toxic, or lifestyle contributors**. Relevant environmental/lifestyle considerations are limited to disease-course modifiers rather than causes:
- Intercurrent respiratory infections accelerate respiratory decompensation in a child with compromised diaphragmatic/intercostal muscle strength.
- Nutritional management (caloric and protein intake, feeding route) affects growth and secondary morbidity but does not cause the disease.
- No infectious agent is implicated in pathogenesis.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function *GAA* variants → **near-complete loss of lysosomal acid α-glucosidase enzymatic activity** (<1% of normal in classic IOPD) — demonstrated directly (enzyme assay).
2. Loss of GAA activity → **failure of lysosomal glycogen hydrolysis**; glycogen continuously delivered to the lysosome via macroautophagy cannot be degraded to glucose — demonstrated.
3. Undegraded glycogen → **progressive lysosomal glycogen accumulation** (lysosomal glycogenosis) in cardiac myocytes, skeletal myofibers, smooth muscle, and to a lesser extent hepatocytes and CNS neurons/motor neurons — demonstrated (muscle biopsy, autopsy).
4. Lysosomal glycogen overload → **lysosomal enlargement/rupture and "autophagic buildup"**: increased autophagosome formation coupled with **impaired autophagosome–lysosome fusion** ("autophagic block"), producing massive accumulation of undigested autophagic debris in the myofiber — demonstrated in muscle and iPSC-cardiomyocyte models ([PMC11118179](https://pmc.ncbi.nlm.nih.gov/articles/PMC11118179/)).
5. Autophagic/lysosomal dysfunction → **secondary organelle damage**: mitochondrial fragmentation, decreased mitochondrial number, impaired oxidative phosphorylation/ATP production, and elevated reactive oxygen species from depolarized mitochondria — demonstrated in Pompe iPSC-cardiomyocytes ([PMC10984102](https://pmc.ncbi.nlm.nih.gov/articles/PMC10984102/); [PMC5442755](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5442755/)).
6. Concurrently, disrupted lysosomal/Golgi trafficking → **Golgi-based protein glycosylation deficits**, contributing to impaired sarcomeric/membrane protein maturation (inferred mechanistic contributor, demonstrated in iPSC-cardiomyocytes) ([PMC study, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0021925820492786)).
7. Combined mitochondrial dysfunction, oxidative stress, and disrupted autophagy → **myofiber ultrastructural disruption** — vacuolization, disorganized sarcomeres/contractile elements, and progressive **replacement of contractile tissue by glycogen-laden vacuoles and lysosomal/autophagic debris** — demonstrated (PAS-positive, acid phosphatase–positive vacuolar myopathy on biopsy).
8. In cardiac muscle specifically → **massive interstitial and intracellular glycogen deposition drives concentric hypertrophic cardiomyopathy**, progressing to left ventricular outflow tract obstruction, diastolic dysfunction, and eventually systolic heart failure — demonstrated (echocardiography, autopsy).
9. Glycogen infiltration of the **cardiac conduction system** → shortened PR interval and, in a subset, a true anatomic AV accessory pathway producing Wolff-Parkinson-White pattern/syndrome with risk of supraventricular tachyarrhythmia — demonstrated (ECG studies) ([Rare Disease Advisor — Cardiac Findings](https://www.rarediseaseadvisor.com/news/cardiac-findings-pediatric-patients-pompe-disease/)).
10. In skeletal muscle (predominantly type I and type II fiber atrophy) and diaphragm/intercostal muscle → progressive **weakness, hypotonia, and impaired ventilatory mechanics** — demonstrated.
11. Diaphragmatic and bulbar (oral-motor/tongue) muscle involvement → **feeding difficulty, macroglossia, and respiratory insufficiency**, culminating without treatment in **cardiorespiratory failure and death** — demonstrated (natural history studies).
12. **Branch — CNS pathway (increasingly recognized in long-term ERT survivors):** because rhGAA does not cross the blood–brain barrier, glycogen continues to accumulate in CNS structures (motor neurons, periventricular/subcortical white matter) → progressive **white-matter hyperintensities**, in a subset **seizures/encephalopathy**, and declining processing speed/fluid reasoning/IQ over years — demonstrated in long-term survivor cohorts, and understood as an emergent consequence of extended survival unmasking a previously fatal-before-onset CNS phenotype ([Ebbink 2018](https://onlinelibrary.wiley.com/doi/10.1111/dmcn.13740); [van der Dorpel 2024](https://onlinelibrary.wiley.com/doi/10.1002/jimd.12736); [ScienceDirect — Severe CNS involvement](https://www.sciencedirect.com/science/article/abs/pii/S1096719223007497)).
13. **Branch — immunologic (ERT-treated CRIM-negative patients only):** absence of endogenous GAA protein (null/null genotype) → host immune system recognizes infused rhGAA as fully foreign → high-titer neutralizing IgG antibody formation → **loss of ERT efficacy and accelerated clinical decline** unless immune tolerance induction is applied — demonstrated (CRIM-negative cohort studies).

**Molecular pathways / cellular processes:** Autophagy (GO:0006914 autophagy; GO:0000422 autophagy of mitochondrion — mitophagy), lysosomal glycogen catabolic process (GO:0005980 glycogen catabolic process; GO:0005764 lysosome as cellular component), oxidative stress/ROS generation, mitochondrial dysfunction (GO:0007005 mitochondrion organization), impaired autophagosome-lysosome fusion (GO:0061909).

**Biochemical abnormality:** Acid α-glucosidase (EC 3.2.1.20) enzymatic deficiency — the core lysosomal enzyme defect.

**Suggested ontology terms:**
- **GO (biological process):** GO:0005980 (glycogen catabolic process), GO:0006914 (autophagy), GO:0061909 (autophagosome-lysosome fusion), GO:0007005 (mitochondrion organization)
- **GO (cellular component):** GO:0005764 (lysosome), GO:0005776 (autophagosome), GO:0005739 (mitochondrion)
- **CL (cell types):** CL:0000746 (cardiac muscle myoblast/cardiomyocyte), CL:0000188 (skeletal muscle myoblast/myocyte), CL:0000187 (muscle cell), CL:0000540 (neuron; relevant for motor neuron/CNS involvement)
- **CHEBI:** CHEBI:28087 (glycogen)
- **UBERON:** UBERON:0000948 (heart), UBERON:0001134 (skeletal muscle tissue), UBERON:0002037 (cerebellum, if relevant), UBERON:0002240 (spinal cord — phrenic motoneurons)

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Heart (concentric hypertrophic cardiomyopathy), skeletal muscle (generalized), diaphragm and intercostal/accessory respiratory muscles, tongue (macroglossia), liver (mild-moderate hepatomegaly, largely from glycogen rather than functional hepatic disease).

**Secondary/complication-level:** Lower motor neurons/spinal cord (phrenic motoneuron glycogen accumulation contributing to diaphragmatic weakness — shown in mouse models and increasingly in human autopsy/imaging); CNS white matter (periventricular, centrum semiovale, later corpus callosum, internal/external capsule, brainstem — in long-term survivors); cardiac conduction system (AV node/accessory pathways); inner ear (sensorineural hearing loss reported in survivors); vascular smooth muscle.

**Body systems:** Cardiovascular, musculoskeletal/neuromuscular, respiratory, and (in long-term survivors) central/peripheral nervous system.

**Tissue/cell level:** Cardiac and skeletal myofibers (both type I and type II fibers show atrophy/vacuolization, with vacuole burden nearly universal across fibers in classic IOPD versus patchy in later-onset forms); hepatocytes; smooth muscle cells; anterior horn motor neurons.

**Subcellular level:** Lysosome (primary site of pathology; GO:0005764); autophagosome (GO:0005776); mitochondria (secondary dysfunction); Golgi apparatus (secondary glycosylation defect).

**Localization:** Bilateral/systemic — not lateralized. Cardiac hypertrophy is typically concentric/biventricular, with LV outflow tract obstruction a specific concern.

---

## 8. Temporal Development

**Onset:** Classic IOPD manifests within the first weeks to few months of life (median onset ~2 months of age); hypertrophic cardiomyopathy is often detectable in the first weeks. Non-classic infantile onset occurs later in the first year, generally without the severe early cardiomyopathy.

**Onset pattern:** Subacute-to-rapidly progressive from birth (in classic form) rather than acute or episodic.

**Progression (untreated):** Continuous, rapid deterioration — motor decline, worsening hypotonia, progressive cardiomegaly/heart failure, feeding failure, and respiratory insufficiency — with death typically by 6–12 months, essentially universal mortality by age 2 in untreated classic IOPD ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1261/)).

**Progression (ERT-treated):** Highly variable; cardiac response to ERT is often robust (regression of hypertrophy), while skeletal muscle/respiratory response is more variable and CRIM-status-dependent. Long-term survivors (now reaching adolescence/adulthood on ERT, as reported in a 2025 25-year follow-up cohort) show a shifting phenotype dominated by residual skeletal myopathy, ventilator dependence in a substantial subset, and emerging CNS disease ([ScienceDirect, 2025](https://www.sciencedirect.com/science/article/abs/pii/S1098360025002370)).

**Disease course pattern:** Progressive, not relapsing-remitting; no spontaneous remission described.

**Critical periods for intervention:** Pre-symptomatic treatment initiation (via newborn screening, ideally within the first weeks of life, before irreversible cardiac/muscle damage and before CRIM-negative patients mount antibody responses) is repeatedly shown to be the single strongest predictor of outcome — sibling comparisons show markedly better outcomes for the presymptomatically treated sibling versus the symptomatically treated sibling ([PMC5121151](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5121151/)).

---

## 9. Inheritance and Population

**Inheritance pattern:** Autosomal recessive (both *GAA* alleles pathogenic); HP:0000007.

**Penetrance:** Complete for classic biallelic null genotypes (essentially 100% penetrant for the IOPD phenotype given null/null genotype); genotype-phenotype correlation is strong enough that specific variant combinations are used clinically to predict severity, although modifiers of exact age of onset/severity exist.

**Expressivity:** Variable across the wider *GAA*-related disease spectrum (IOPD → non-classic infantile → childhood/juvenile → late adult onset), governed largely by residual enzyme activity; within classic IOPD itself expressivity of the core cardiomyopathy/hypotonia phenotype is relatively consistent.

**Genetic anticipation:** Not described (not a repeat-expansion disorder).

**Founder effects / ethnic variant enrichment:** c.2560C>T enriched in patients of African ancestry (frequently CRIM-negative); c.-32-13T>G broadly prevalent, especially in those of European ancestry (associated with LOPD); specific exon-18 deletion and c.525delT common "Dutch"/European null alleles; pseudodeficiency alleles (c.1726G>A, c.2065G>A) enriched in East/Southeast Asian populations, complicating NBS interpretation in these groups.

**Carrier frequency:** Estimated overall Pompe disease carrier frequency on the order of 1:100 in general populations (varies by ancestry); precise IOPD-specific carrier frequency not separately well established given genotype heterogeneity.

**Epidemiology:**
- Overall Pompe disease (all forms) incidence estimated ~1:40,000 (Netherlands data), broken down as **~1:138,000 for IOPD** and ~1:57,000 for LOPD.
- Pennsylvania NBS data reported a combined IOPD+LOPD incidence of ~1:16,095 in that screened population (higher than historical estimates, reflecting ascertainment of previously undiagnosed LOPD as well as an inclusive definition) ([PMC7712483](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7712483/); [PMC11943203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11943203/)).
- NBS programs (Taiwan, Illinois, California, Missouri, Pennsylvania, Oregon) have each identified small numbers of IOPD cases per screened cohort (e.g., 10 IOPD cases identified in one Illinois cohort of 684,290 infants, split "classical"/"nonclassical" by presence of cardiomyopathy).

**Sex ratio:** No significant sex predilection reported (autosomal, not X-linked).

**Geographic distribution:** Pan-ethnic; higher incidence reported in some populations (e.g., relatively higher Pompe disease incidence historically noted in African American and Chinese populations for specific severe genotypes), but the disease occurs worldwide.

---

## 10. Diagnostics

**Newborn screening (NBS):** Pompe disease was added to the U.S. **Recommended Uniform Screening Panel (RUSP)** in **March 2015** (Advisory Committee vote May 2013), and as of recent years is screened by the great majority (nearly universal, though not all) U.S. state NBS programs, using a first-tier fluorometric or tandem mass spectrometry GAA enzyme activity assay on dried blood spot (DBS), followed by second-tier molecular (*GAA* sequencing) or biomarker testing to resolve pseudodeficiency and false positives ([EveryLife Foundation](https://everylifefoundation.org/newborn-screening-take-action/pompe-disease/); [HRSA RUSP](https://www.hrsa.gov/advisory-committees/heritable-disorders/rusp)).

**Biochemical testing:**
- **GAA enzyme activity assay** in DBS, leukocytes, or cultured skin fibroblasts (gold standard confirmatory test); acarbose is used to inhibit interfering neutral glucosidase activity in leukocyte/DBS assays.
- **Urine Hex4 (glucotetrasaccharide, Glc4)** biomarker — elevated in Pompe disease, useful for diagnostic support and for monitoring treatment response, though not disease-specific (also elevated with liver disease or dietary carbohydrate intake) ([Mayo Clinic Labs](https://www.mayocliniclabs.com/test-catalog/download-setup?format=pdf&unit_code=64174)).
- Creatine kinase (CK) is typically markedly elevated in IOPD; a "creatine/creatinine-to-GAA activity ratio" has been proposed as a screening-adjunct biomarker.

**Genetic testing:** *GAA* full gene sequencing plus deletion/duplication analysis is standard confirmatory and CRIM-status-informative testing (e.g., Mayo Clinic GAAN panel); essential for genotype-based CRIM prediction, prognosis, and family/carrier counseling.

**CRIM testing:** Determination of cross-reactive immunologic material status (via Western blot/immunohistochemistry of GAA protein in cultured fibroblasts or lymphocytes, increasingly supplemented/predicted by genotype) is a required step prior to ERT initiation, as CRIM-negative status mandates consideration of prophylactic immune tolerance induction.

**Muscle biopsy:** Historically used before biochemical/genetic assays became routine; shows PAS-positive, diastase-sensitive, acid phosphatase-positive vacuolar myopathy with near-universal fiber involvement in classic IOPD (in contrast to patchy involvement in LOPD, where biopsy can be falsely negative in 20–30% of cases) ([SciELO](https://www.scielo.br/j/anp/a/n396bYxpb76cMyjpBFRD3HS/)).

**Imaging/functional tests:** Echocardiography (left ventricular mass index, wall thickness, LVOT obstruction) is central to diagnosis and monitoring; ECG (short PR interval, high QRS voltage, WPW pattern); pulmonary function testing/polysomnography for respiratory status; brain MRI in long-term survivors to monitor white matter disease.

**Clinical criteria/differential diagnosis:** Distinguished from other causes of infantile hypotonia and hypertrophic cardiomyopathy, including other glycogen storage diseases, mitochondrial cardiomyopathies, RASopathies (Noonan syndrome), Danon disease, and congenital myopathies — GAA enzyme assay is definitive.

**Screening extension:** Carrier screening and prenatal/preimplantation genetic testing are available once familial variants are known; cascade family testing recommended after proband diagnosis.

---

## 11. Outcome/Prognosis

**Untreated:** Uniformly fatal; median survival historically ~6–8.7 months, with death from cardiorespiratory failure by age 1–2 years in essentially all untreated classic IOPD infants.

**ERT-treated:** Enzyme replacement therapy (commercially available since 2006) has transformed prognosis — landmark trials and real-world cohorts show significantly prolonged overall and ventilator-free survival, with many CRIM-positive, early-treated infants now surviving into adolescence and adulthood. However:
- Cardiac response to ERT is generally favorable (hypertrophy regression).
- Skeletal muscle/motor response is more variable; a substantial proportion of long-term survivors remain wheelchair- and/or ventilator-dependent.
- CRIM-negative, ERT-treated-without-tolerance-induction patients have markedly worse outcomes due to antibody-mediated ERT failure.
- Emerging **CNS involvement** (white matter disease, cognitive decline in a subset, occasional seizures/encephalopathy) is now recognized as a significant morbidity in long-term survivors, since ERT cannot cross the blood-brain barrier — an outcome effectively "unmasked" by improved somatic survival ([Ebbink 2018](https://onlinelibrary.wiley.com/doi/10.1111/dmcn.13740); [2024 severe CNS involvement report](https://pubmed.ncbi.nlm.nih.gov/38184429/)).
- Sensorineural hearing loss is a recognized long-term complication.

**Prognostic factors:** CRIM status, genotype (null/null vs. some residual activity), age at ERT initiation (earlier/pre-symptomatic markedly better), ERT dose, and presence/absence of successful immune tolerance induction in CRIM-negative patients are the dominant prognostic determinants.

---

## 12. Treatment

**Enzyme Replacement Therapy (ERT) — mainstay of care:**
- **Alglucosidase alfa** (Myozyme/Lumizyme) — first FDA-approved rhGAA (2006); standard dose 20 mg/kg IV every other week (EOW); higher-dose regimens (up to 40 mg/kg/week, divided) increasingly used ("high-dose"/"dose-intensive therapy") to improve outcomes, given evidence that the standard dose is insufficient to halt long-term myopathy progression ([PMC systematic review](https://www.sciencedirect.com/science/article/pii/S2214426924001320); [PubMed 31904026](https://pubmed.ncbi.nlm.nih.gov/31904026/)).
- **Avalglucosidase alfa-ngpt** (Nexviazyme) — a next-generation rhGAA with enhanced mannose-6-phosphate targeting, FDA-approved for patients ≥1 year including IOPD; single-center cohort data (2025) support efficacy and safety when transitioning IOPD patients from alglucosidase alfa ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1098360025000206)).
- **Cipaglucosidase alfa-atga + miglustat (Pombiliti/Opfolda)** — approved combination ERT/chaperone regimen, currently indicated for adults with LOPD; the **ROSSELLA trial** is evaluating this combination in pediatric IOPD (ages 0 to <18 years).

NCIT term: **NCIT:C15238** (Gene Therapy) for gene therapy approaches below; **NCIT:C15986** (Pharmacotherapy) for ERT with `therapeutic_agent` bound to the specific rhGAA product.

**Immune tolerance induction (ITI) — critical for CRIM-negative patients:**
- Prophylactic short-course ITI with **rituximab + methotrexate + IVIG** (typically ~5 weeks, given ERT-naive) is now considered standard of care for CRIM-negative IOPD, preventing formation of neutralizing anti-rhGAA IgG antibodies. In one cohort of 19 CRIM-negative patients receiving ITI, 74% were alive at median follow-up of 44.2 months, in contrast to rapid deterioration historically seen in non-tolerized CRIM-negative infants ([JCI Insight](https://insight.jci.org/articles/view/94328); [PMC7424004](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7424004/)).

**Gene therapy (advanced/experimental):**
- **AAV9-hGAA gene therapy** — first-in-human case report (published 2022/2023) of a single IV AAV9-hGAA infusion in an infant with IOPD showed normalized GAA activity, improved cardiac function, and Hammersmith Infant Neurological Examination gains within 8 weeks ([NEJM 2024](https://www.nejm.org/doi/full/10.1056/NEJMoa2407766)).
- **GC301** — an AAV9 vector with ubiquitous promoter, in Phase 1/2 trial (NCT05793307) for IOPD, active as of 2025.
- Other AAV vector programs (e.g., AAV8-mediated liver-targeted secretable GAA approaches) are in earlier-phase/preclinical-to-clinical transition; an in-utero ERT feasibility trial (UCSF) is also underway for lysosomal storage diseases including IOPD, targeting completion ~2027.
- As of February 2025, ~41 active/recruiting Pompe disease clinical trials span ERT, gene therapy, and substrate reduction approaches ([Rare Disease Advisor — Clinical Trials](https://www.rarediseaseadvisor.com/hcp-resource/pompe-disease-clinical-trials/)).

**Supportive/multidisciplinary care:**
- Respiratory support (mechanical ventilation, non-invasive ventilation, cough-assist devices) — NCIT:C50384-type respiratory support terms.
- Physical, occupational, and speech/feeding therapy (NCIT:C15302 Physical Therapy).
- Nutritional support/feeding management, including gastrostomy tube feeding in severe bulbar involvement (NCIT:C15447 Dietary Intervention).
- Cardiology monitoring/management of arrhythmias (including WPW-associated tachyarrhythmia).
- Audiology monitoring for sensorineural hearing loss.
- Genetic counseling for families (NCIT:C15240 Genetic Counseling).

**Treatment outcomes/adverse events:** Infusion-associated reactions are common with rhGAA, especially at higher doses/faster infusion rates; anaphylaxis risk requires premedication protocols and monitoring. Antibody development (especially in CRIM-negative, non-tolerized patients) is the principal cause of ERT failure.

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (no environmental exposure to avoid); prevention operates through reproductive/genetic pathways — carrier screening, genetic counseling for at-risk couples (both known carriers or from high-prevalence populations), and prenatal diagnosis or preimplantation genetic testing (PGT) for known familial variants.

**Secondary prevention (early detection):** **Newborn screening** is the dominant secondary-prevention strategy, enabling pre-symptomatic diagnosis and treatment initiation before irreversible cardiac and muscle damage occurs — repeatedly shown to be the single most important modifiable determinant of outcome.

**Tertiary prevention:** Immune tolerance induction in CRIM-negative patients prevents antibody-mediated treatment failure; proactive respiratory, cardiac, nutritional, and rehabilitative management reduces complication burden in diagnosed patients.

**Screening/genetic counseling:** Cascade carrier testing of at-risk family members after proband identification; reproductive counseling per autosomal recessive 25% recurrence risk.

**Public health:** State-level RUSP alignment legislation (14 states as of recent tallies) to ensure timely adoption of Pompe NBS; ongoing advocacy (e.g., EveryLife Foundation, AMDA Pompe) to close remaining gaps in state NBS coverage.

---

## 14. Other Species / Natural Disease

Pompe disease occurs naturally in several non-human species, providing valuable comparative and translational models (OMIA:000419 across species):

- **Dogs (Canis lupus familiaris):** Naturally occurring GAA deficiency in **Finnish and Swedish Lapphunds**, caused by a nonsense mutation (c.2237G>A, producing a premature stop at residue 746); this canine model closely mimics human IOPD both genetically and clinico-pathologically, and is used as a valuable large-animal model for gene therapy development ([PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0056825); OMIA:000419-9615).
- **Cattle (Bos taurus):** Naturally occurring disease in **Brahman and Beef Shorthorn cattle**, with three distinct breed-specific *GAA* mutations, each producing a premature stop codon (OMIA:000419-9913).
- **Cats (Felis catus):** Documented Pompe-like disease (OMIA:000419-9685); underlying mutation not fully characterized in the reviewed literature.
- **Sheep and Japanese quail:** Naturally occurring Pompe-like disease also reported, without a confirmed causal mutation identified to date (OMIA:000419-9940).

**Veterinary relevance:** These natural animal models — particularly the Lapphund dog model — recapitulate cardiac and skeletal muscle pathology and are used preclinically to evaluate AAV gene therapy and next-generation ERT approaches before human trials.

**Comparative pathology:** Across species, the core lysosomal glycogen-storage mechanism and resultant cardiac/skeletal myopathy are conserved, supporting cross-species translational relevance; GAA is highly conserved evolutionarily.

---

## 15. Model Organisms

**Genetically engineered murine models (Mus musculus):**
- **Bijvoet model** (exon 13 disruption) — near-complete GAA absence in all tissues; progressive lysosomal glycogen accumulation in cardiomyocytes, hepatocytes, skeletal muscle; notably, this model does **not** show significant muscle weakness up to 9 months of age, limiting its ability to model the severe early weakness of human IOPD.
- **Raben model** (exon 6 disruption) — progressive glycogen accumulation in muscle and motor neurons; muscle wasting/weakness not obvious until 8–9 months, again a milder-than-human phenotype.
- **Genetic background effects:** Gaa−/− mice backcrossed to pure 129SVE background show less severe respiratory deficits than on mixed B6/129 background, an important confound for phenotyping studies.
- **Newer knock-in models** using CRISPR-Cas9 to introduce patient-derived point mutations (e.g., **c.1935C>A / p.Asp645Glu** knock-in) better recapitulate **early-onset hypertrophic cardiomyopathy and skeletal muscle weakness**, more faithfully modeling classic human IOPD than the original knockout lines ([Scientific Reports 2020](https://www.nature.com/articles/s41598-020-65259-8); [Scientific Reports 2022](https://www.nature.com/articles/s41598-022-25914-8)).
- **Respiratory phenotype:** Gaa−/− mice show reduced ventilation, elevated cervical spinal cord glycogen with prominent inclusions in phrenic motoneurons, and attenuated phrenic nerve output relative to wild-type — a model for the neuromuscular respiratory component of human disease ([PMC7139647](https://pmc.ncbi.nlm.nih.gov/articles/PMC7139647/)).
- Gene therapy proof-of-concept: hepatic expression of secretable GAA rescues advanced disease in mouse models, supporting the biological rationale for liver-directed AAV vectors.

**Cellular/in vitro models:**
- **Patient-derived iPSC cardiomyocytes** — used extensively to study mitochondrial dysfunction, oxidative stress, and Golgi glycosylation deficits underlying Pompe cardiomyopathy; a key platform since it captures human-specific cardiomyocyte biology unavailable in mouse models.
- Patient fibroblast cultures — standard for GAA enzyme activity confirmatory testing and CRIM status determination.

**Applications:** These models are used to study glycogen accumulation kinetics, autophagic dysfunction, evaluate ERT/gene therapy biodistribution and efficacy, and screen novel therapeutics (e.g., chaperone/substrate-reduction compounds).

**Model limitations:** Standard knockout mice underrepresent the severity and early onset of skeletal myopathy/weakness seen in human classic IOPD, motivating the shift toward patient-variant knock-in models and the continued value of the canine (Lapphund) natural model, which more faithfully reproduces human disease severity and timing.

**Resources:** MGI (Mouse Genome Informatics) for murine allele records; OMIA for animal (dog, cattle, cat, sheep) natural disease models.

---

## Summary for Knowledge-Base Curation

IOPD is a well-characterized, single-gene (*GAA*, 17q25.3) autosomal recessive lysosomal storage disease with a clear, richly evidenced causal chain from enzyme deficiency → lysosomal glycogen accumulation → autophagic/mitochondrial dysfunction → cardiac and skeletal myofiber damage → cardiorespiratory failure, now substantially modified by ERT, immune tolerance induction (for CRIM-negative patients), and emerging gene therapy. Strong primary-literature support exists (PMID-citable) across genetics (OMIM, GeneReviews, ClinVar-referenced variant studies), mechanism (iPSC and murine model studies), epidemiology/NBS (multi-state cohort publications), treatment (COMET/mini-COMET/ROSSELLA trial literature, AAV9-hGAA NEJM case report), and comparative/animal-model biology (canine and bovine natural models). Key curation considerations for a dismech entry include: distinguishing CRIM-positive/negative subtypes with modifier-gene-style typing on the immune response; modeling the ERT→gene-therapy treatment progression with `therapeutic_modality` (PROTEIN_REPLACEMENT for ERT, GENE_THERAPY for AAV9-hGAA); and capturing the emerging CNS/HUMAN_MODEL_MISMATCH angle, since mouse knockout models substantially underrepresent human skeletal myopathy severity while the Lapphund dog model is a higher-fidelity comparator.

---

### Sources

- [OMIM #232300 — Pompe Disease, Infantile-Onset](https://www.omim.org/entry/232300)
- [OMIM *606800 — GAA gene](https://www.omim.org/entry/606800)
- [OMIM #621314 — Pompe Disease, Late-Onset](https://www.omim.org/entry/621314)
- [Pompe Disease — GeneReviews®, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1261/)
- [Molecular genetics of Pompe disease: a comprehensive overview — Ann Transl Med](https://atm.amegroups.org/article/view/25187/html)
- [Biochemical and Genetic Testing of GAA in Over 30,000 Symptomatic Patients (2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11918499/)
- [Pompe Disease: Pathogenesis, Molecular Mechanisms — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13116368/)
- [Failure of Autophagy in Pompe Disease — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11118179/)
- [Pompe disease: from pathophysiology to therapy and back again](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4135233/)
- [Lysosomal glycogen accumulation disturbs cytoplasmic glycogen metabolism — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10092494/)
- [Mitochondrial dysfunction in Pompe iPSC-cardiomyocytes — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10984102/)
- [Metabolomic profiling of Pompe iPSC-cardiomyocytes — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5442755/)
- [Golgi-based glycosylation deficit in Pompe iPSC-cardiomyocytes — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0021925820492786)
- [Lessons Learned from Pompe Disease Newborn Screening and Follow-up — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422965/)
- [Newborn Screening for Pompe Disease: Pennsylvania Experience — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7712483/)
- [Five-Year Outcomes of Pompe Patients Identified by PA Newborn Screen — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11943203/)
- [Newborn Screening for Pompe Disease in Illinois — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7422983/)
- [Clinical Laboratory Experience of Blood CRIM Testing — PubMed](https://pubmed.ncbi.nlm.nih.gov/26693141/)
- [EveryLife Foundation — Pompe Disease Newborn Screening](https://everylifefoundation.org/newborn-screening-take-action/pompe-disease/)
- [HRSA Recommended Uniform Screening Panel](https://www.hrsa.gov/advisory-committees/heritable-disorders/rusp)
- [Sustained immune tolerance induction in CRIM-negative IOPD — JCI Insight](https://insight.jci.org/articles/view/94328)
- [Benefits of Prophylactic Short-Course ITI — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7424004/)
- [AAV9-Mediated Gene Therapy for Infantile-Onset Pompe Disease — NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2407766)
- [First-in-human AAV9-hGAA gene therapy case report — medRxiv](https://www.medrxiv.org/content/10.1101/2022.12.22.22283398.full.pdf)
- [Pompe Disease Clinical Trials — Rare Disease Advisor](https://www.rarediseaseadvisor.com/hcp-resource/pompe-disease-clinical-trials/)
- [Dose-intensive therapy (DIT) for infantile Pompe disease — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2214426924001320)
- [Higher dosing of alglucosidase alfa improves outcomes — PubMed](https://pubmed.ncbi.nlm.nih.gov/31904026/)
- [Transitioning from alglucosidase alfa to avalglucosidase alfa in IOPD — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1098360025000206)
- [Infantile-onset Pompe disease entering adulthood — ScienceDirect (2025)](https://www.sciencedirect.com/science/article/abs/pii/S1098360025002370)
- [Classic infantile Pompe patients approaching adulthood: consequences for the brain — DMCN](https://onlinelibrary.wiley.com/doi/10.1111/dmcn.13740)
- [Severe CNS involvement in long-term treated children with IOPD — PubMed](https://pubmed.ncbi.nlm.nih.gov/38184429/)
- [Long term survival in classic infantile Pompe disease: brain/cognitive spectrum — JIMD 2024](https://onlinelibrary.wiley.com/doi/10.1002/jimd.12736)
- [Divergent outcomes in siblings with IOPD treated presymptomatically vs symptomatically — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5121151/)
- [A Nonsense Mutation in GAA Causes Pompe Disease in Finnish and Swedish Lapphunds — PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0056825)
- [OMIA:000419 — Glycogen storage disease II (multiple species)](https://omia.org/OMIA000419/9615/)
- [Longitudinal characterization of Gaa knock-in mice — Disease Models & Mechanisms](https://journals.biologists.com/dmm/article/19/3/dmm052611/371074/Longitudinal-characterization-of-Gaac-1826dupA)
- [The Respiratory Phenotype of Pompe Disease Mouse Models — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7139647/)
- [CRISPR-Cas9 generated Pompe knock-in murine model — Scientific Reports (2020)](https://www.nature.com/articles/s41598-020-65259-8)
- [Gaa c.1935C>A knock-in mouse model — Scientific Reports (2022)](https://www.nature.com/articles/s41598-022-25914-8)
- [Muscle biopsy in Pompe disease — SciELO](https://www.scielo.br/j/anp/a/n396bYxpb76cMyjpBFRD3HS/)
- [Rare Disease Advisor — Pompe Disease Etiology](https://www.rarediseaseadvisor.com/disease-info-pages/pompe-disease-etiology/)
- [Rare Disease Advisor — Cardiac Findings in Pediatric Pompe Disease](https://www.rarediseaseadvisor.com/news/cardiac-findings-pediatric-patients-pompe-disease/)
- [Ambulatory ECG analysis in infants on rhGAA ERT — Genetics in Medicine](https://www.nature.com/articles/gim200655)
- [Arrhythmias in patients receiving ERT for infantile Pompe disease — Genetics in Medicine](https://www.nature.com/articles/gim2008116)
- [GAA variants with reduced activity but no symptoms, exome sequencing — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10433214/)
- [Pompe disease: pathogenesis, molecular genetics and diagnosis — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7467391/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 18 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008608` (1 mention) - the report calls it "glycogen storage disease II / Pompe disease"; MONDO calls it **Down syndrome**
- `CL:0000540` (1 mention) - the report calls it "neuron; relevant for motor neuron/CNS involvement"; CL calls it **neuron**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0009291` (1 mention) - the report calls it "glycogen storage disease II, infantile onset"; MONDO calls it **glycogen storage disease III**
- `CL:0000746` (1 mention) - the report calls it "cardiac muscle myoblast/cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiac muscle fiber" among its other names
- `CL:0000188` (1 mention) - the report calls it "skeletal muscle myoblast/myocyte"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0002037` (1 mention) - the report calls it "cerebellum, if relevant"; UBERON calls it **cerebellum**
- `UBERON:0002240` (1 mention) - the report calls it "spinal cord — phrenic motoneurons"; UBERON calls it **spinal cord**, and lists "spinal cord structure" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`.
