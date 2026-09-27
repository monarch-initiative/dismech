---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-08T14:25:33.460918'
end_time: '2026-08-08T14:30:56.134219'
duration_seconds: 322.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Atransferrinemia
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
  web_search_requests: 16
  num_turns: 28
  total_cost_usd: 2.0062390000000008
  session_id: 477ccf21-ede1-58d8-aaf7-6fd33d04ddf7
  stop_reason: end_turn
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Atransferrinemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Atransferrinemia** covering all of the
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

# Atransferrinemia (Congenital Hypotransferrinemia): Comprehensive Research Report

## 1. Disease Information

**Overview.** Atransferrinemia (also called congenital atransferrinemia, hereditary hypotransferrinemia, or familial hypotransferrinemia) is an extremely rare autosomal recessive metal-metabolism disorder caused by absent or severely reduced synthesis of transferrin, the principal plasma iron-transport glycoprotein. The disorder produces a paradoxical dual phenotype: severe microcytic, hypochromic anemia due to failure to deliver iron to erythroid precursors, together with progressive systemic (secondary) iron overload/hemosiderosis because absorbed dietary iron cannot be carried in a regulated, transferrin-bound form and instead accumulates as non-transferrin-bound iron (NTBI) in parenchymal tissues. It was first described by Heilmeyer et al. in 1961 (PMID:13906009) and remains one of the rarest inherited disorders of iron metabolism, with only ~16–20 genetically or clinically documented cases from ~14–16 families reported to date.

**Key identifiers:**
- **OMIM:** #209300 (Atransferrinemia) — phenotype entry; *190000 — TF (Transferrin), the causal gene
- **Orphanet:** ORPHA:1195 (Congenital atransferrinemia)
- **Gene:** TF; HGNC:11740; chromosome 3q22.1 (some sources cite 3q21); 24 exons
- **Mondo Disease Ontology:** integrates the OMIM/Orphanet records above (Mondo unifies OMIM:209300 and ORPHA:1195 into a single congenital-atransferrinemia disease concept)
- **MeSH/GTR:** listed as "Atransferrinemia," concept C0521802 in NCBI's Genetic Testing Registry
- **ICD-10-CM:** falls under E83.19 (Disorders of iron metabolism, other) — no dedicated code exists
- **Synonyms:** Congenital hypotransferrinemia; hereditary hypotransferrinemia; familial idiopathic hypotransferrinemia; transferrin deficiency

**Source of information.** Because the condition has been reported in fewer than 20 kindreds worldwide, essentially all available data derive from aggregated case reports and case series (individual-patient-level literature) rather than large disease registries or EHR-based cohorts — there is no population-level epidemiological database for this disease.

---

## 2. Etiology

**Disease causal factors.** Atransferrinemia is a monogenic, purely genetic disorder — there is no known infectious or primarily environmental cause of the *congenital* form. It results from **homozygous or compound heterozygous loss-of-function mutations in the TF gene** (OMIM *190000), which encodes the 679-amino-acid transferrin glycoprotein synthesized predominantly in hepatocytes. Loss of functional transferrin protein removes the principal iron chaperone from plasma, producing the combined anemia/iron-overload phenotype (OMIM #209300; PMID:11110675, PMID:15466165, PMID:18097132).

**Genetic risk factors.**
- **Causal variants (biallelic, TF gene):**
  - c.[10bp del + 9bp dup ins] / c.1429G>C (p.Ala477Pro) — compound heterozygous, first reported U.S. case (PMID:11110675)
  - c.229G>A (p.Asp77Asn, D77N) — homozygous, third reported case (PMID:15466165)
  - c.410G>A (p.Cys137Tyr) — homozygous, first Turkish case, 11th reported patient (PMID:18097132)
  - c.1765C>T (p.Pro589Ser) — listed pathogenic in ClinVar for Atransferrinemia
  - c.-117G>A (5′ regulatory region variant) — reported in ClinVar associated with Atransferrinemia
  - More than 30 TF structural polymorphisms exist in the general population (the common TF C, especially TF C1, variant), but these are population variants distinct from the rare disease-causing null/hypomorphic alleles.
- **Susceptibility/modifier genes:** none well established; disease severity appears to correlate with residual transferrin synthesis (complete absence vs. detectable low levels) rather than with variation at a second locus.
- **Consanguinity:** several reported kindreds (e.g., the Turkish and other homozygous cases) involve consanguineous parents, consistent with autosomal recessive inheritance and founder-type homozygosity in small/isolated populations.

**Environmental risk factors.** Not applicable to the congenital form (purely genetic). However, an **acquired ("secondary") atransferrinemia** phenocopy can occur in adults from severe chronic undernutrition, systemic inflammation, protein-losing enteropathy, and liver failure, which suppress hepatic transferrin synthesis or increase its loss/consumption (PMC9807235). This acquired form is reversible with correction of the underlying nutritional/inflammatory/hepatic disease and — notably — a case report found that even with undetectable serum transferrin, a patient maintained near-normal hemoglobin, suggesting compensatory non-transferrin iron-delivery pathways can partially substitute in adults (see Mechanism section).

**Protective factors.** None specific to the germline disease are described in the literature; heterozygous (carrier) TF mutation carriers are asymptomatic, indicating that a single functional TF allele is sufficient for normal iron transport and provides protection against clinical disease.

**Gene-environment interactions.** No formal GxE data exist for congenital atransferrinemia given its rarity. The clearest interaction in the literature is disease-modifying: iron **supplementation is contraindicated** in congenital atransferrinemia because it does not correct the anemia (erythroid precursors cannot use free/NTBI iron efficiently for hemoglobin synthesis) and instead worsens secondary hemosiderosis — i.e., a therapeutic environmental exposure (dietary/parenteral iron) interacts adversely with the genetic lesion.

---

## 3. Phenotypes

Onset is typically in **infancy to early childhood** (some case series document presentation from birth to ~7–20 years, with most patients recognized before age 10). The clinical picture combines anemia-related symptoms with iron-overload-related organ dysfunction.

| Phenotype | Type | HPO suggestion | Frequency/Notes |
|---|---|---|---|
| Pallor | Sign | HP:0000980 (Pallor) | Nearly universal presenting sign |
| Fatigue/lethargy | Symptom | HP:0012378 (Fatigue) | Common presenting complaint |
| Failure to thrive / growth retardation | Sign | HP:0001508 (Failure to thrive) / HP:0001510 (Growth delay) | Frequently reported |
| Microcytic anemia | Lab abnormality | HP:0001935 (Microcytic anemia) | Defining feature; Hb as low as 5–6 g/dL reported |
| Hypochromic anemia | Lab abnormality | HP:0001931 (Hypochromic microcytic anemia — combined term) | Co-occurs with microcytosis |
| Elevated serum ferritin | Lab abnormality | HP:0003281 (Elevated serum ferritin) | Markedly elevated (e.g., 1413–2072 µg/L in one case series vs. normal 45–160) despite low serum iron in some reports, or elevated serum iron/transferrin saturation in others depending on tissue iron redistribution |
| Low/absent serum transferrin | Lab abnormality | (suggest verifying exact HPO term, e.g., "Decreased circulating transferrin concentration") | Diagnostic hallmark; typically <35 mg/dL (severely reduced total iron-binding capacity) |
| Elevated transferrin saturation | Lab abnormality | HP:0032120 (Increased transferrin saturation) — verify | Despite low/absent transferrin, % saturation is paradoxically elevated because the small pool present is fully iron-loaded |
| Hepatomegaly | Sign | HP:0002240 (Hepatomegaly) | Common |
| Hepatic fibrosis/cirrhosis | Complication | HP:0001395 (Hepatic fibrosis) / HP:0001394 (Cirrhosis) | Late complication of iron overload |
| Splenomegaly | Sign | HP:0001744 (Splenomegaly) | Reported in some cases |
| Cardiomyopathy / heart failure | Complication | HP:0001638 (Cardiomyopathy) | From cardiac iron deposition; can be fatal if untreated |
| Tachycardia / systolic ejection murmur | Sign | HP:0001649 (Tachycardia) / HP:0031650 (Systolic murmur) | Attributed to chronic anemia (high-output state) |
| Recurrent infections | Symptom | HP:0002719 (Recurrent infections) | Reported, possibly related to iron's effect on immune function |
| Anorexia / irritability | Symptom | HP:0002039 (Anorexia) / HP:0000737 (Irritability) | Infantile presentation |
| Arthritis / joint involvement | Sign | HP:0001369 (Arthritis) | Reported in a subset (iron-related arthropathy, akin to hemochromatotic arthropathy) |
| Hypothyroidism | Complication | HP:0000821 (Hypothyroidism) | Endocrine iron-overload complication |
| Diabetes mellitus | Complication | HP:0000819 (Diabetes mellitus) | Endocrine (pancreatic) iron-overload complication |
| Pancreatic iron deposition | Sign | (suggest UBERON/GO annotation rather than HPO) | Iron accumulates preferentially in liver, heart, pancreas, thyroid, kidney |
| Hypospadias | Congenital anomaly | HP:0000047 (Hypospadias) | Reported in one case, hypothesized secondary to fetal hypoxia from severe anemia rather than a direct TF effect |
| Intrauterine growth retardation, lactic acidosis, aminoaciduria (severe neonatal form) | Sign cluster | HP:0001511 / HP:0003128 / HP:0003355 | Described in a severe neonatal presentation treated with apotransferrin/exchange transfusion (PMID:10654962); both infants ultimately died at 8–10 weeks |

**Severity/progression:** Variable but generally progressive if untreated — from mild anemia recognized incidentally to life-threatening cardiac and hepatic iron deposition. Disease course is chronic/lifelong, punctuated by episodes requiring transfusion or plasma/transferrin infusion.

**Quality of life impact:** Chronic transfusion dependence, recurrent infusion visits, growth impairment, and risk of endocrine and cardiac complications substantially affect pediatric development and long-term quality of life; no disease-specific QOL instrument data were identified in the literature (consistent with its ultra-rarity).

---

## 4. Genetic/Molecular Information

**Causal gene:** TF (Transferrin), OMIM *190000, HGNC:11740, chromosome 3q22.1 (GRCh38: 3:133,661,998–133,796,641), 24 exons, encoding a bilobed 679-amino-acid iron-binding glycoprotein with two homologous iron-binding domains (N-lobe and C-lobe), each coordinating one Fe³⁺ ion together with a synergistic carbonate anion.

**Pathogenic variants identified in confirmed atransferrinemia cases:**
| Variant (cDNA/protein) | Zygosity | Location | Case | Reference |
|---|---|---|---|---|
| 10-bp deletion + 9-bp duplicated-sequence insertion / c.1429G>C (p.Ala477Pro) | Compound heterozygous | — | First U.S. case | Beutler et al. 2000, Blood 96:4071–4074, PMID:11110675 |
| c.229G>A (p.Asp77Asn, D77N), exon 3 | Homozygous | Exon 3 | Third reported case (parents/sibling heterozygous carriers) | Knisely, Gelbart, Beutler 2004, Blood 104:2607, PMID:15466165 |
| c.410G>A (p.Cys137Tyr), exon 4 | Homozygous | Exon 4 | First Turkish case, 11th reported patient | PMID:18097132 |
| c.1765C>T (p.Pro589Ser) | — | — | Listed in ClinVar under "Atransferrinemia" | ClinVar RCV000376325 |
| c.-117G>A | — | 5′ regulatory | Listed in ClinVar under "Atransferrinemia" | ClinVar RCV000338348 |

**Variant classification:** Per ACMG/AMP framework as reflected in ClinVar, the confirmed causal alleles above are classified Pathogenic/Likely pathogenic for Atransferrinemia; numerous additional TF missense variants in ClinVar/dbSNP are classified as benign population polymorphisms (the >30 known TF structural variants, e.g., the common TF C1/C2/C3/B/D variant system used historically in population genetics/paternity testing) and are not disease-causing.

**Allele frequency:** No dedicated population allele frequency has been established for the rare pathogenic null alleles (consistent with an ultra-rare recessive disease); gnomAD/ExAC would be the appropriate resource to query per-variant frequencies, but published case reports do not cite population frequency data, reflecting the extreme rarity of biallelic loss-of-function TF genotypes.

**Somatic vs. germline:** Congenital atransferrinemia is strictly germline. Somatic/COSMIC-type data are not applicable (TF is not classically an oncogene/tumor suppressor in this context, though transferrin/transferrin receptor biology intersects with some cancer iron-dependency research unrelated to this Mendelian disease).

**Functional consequences:** The known variants produce **loss of function** — either through frameshift/deletion-insertion events that likely abolish protein production, or through missense substitutions (D77N, C137Y, A477P, P589S) that are presumed to destabilize the folded iron-binding lobes or impair secretion, resulting in absent-to-trace circulating transferrin. No gain-of-function or dominant-negative TF alleles have been reported for this disease.

**Modifier genes:** None specifically validated; clinical variability across cases (severity of anemia, degree of iron overload, response to therapy) likely reflects the amount of residual transferrin synthesized (complete absence vs. very low but detectable levels) rather than a distinct modifier locus.

**Epigenetic information:** No disease-specific DNA methylation or histone-modification studies of TF in atransferrinemia were identified; TF hepatic transcription is known generally to be regulated by inflammatory cytokines (as an acute-phase reactant that is *down*-regulated in inflammation) and by iron status via HNF and STAT pathways, which is relevant to the *acquired* form (see below) but has not been studied epigenetically in the congenital disease.

**Chromosomal abnormalities:** Not applicable — atransferrinemia is caused by point mutations/small indels within TF, not by large structural chromosomal rearrangements, aneuploidy, or copy-number changes.

---

## 5. Environmental Information

- **Environmental factors:** None cause the congenital genetic disease; however, exogenous iron (dietary or parenteral) is a clinically important **modifying** exposure — iron supplementation is explicitly contraindicated because unbound iron cannot be used for erythropoiesis and instead exacerbates secondary hemosiderosis/hemochromatosis in liver, heart, pancreas, thyroid, and kidney.
- **Lifestyle factors:** No specific dietary, smoking, exercise, or alcohol association data exist for this ultra-rare Mendelian disease.
- **Infectious agents:** Not causal for the congenital form. Recurrent infections are a downstream *consequence* of the disease (possibly related to iron dysregulation impairing innate immune function, and/or to general debility), not a trigger of it.
- **Acquired ("secondary") atransferrinemia** — a clinically distinct, non-genetic phenocopy — is triggered environmentally by severe chronic malnutrition, systemic inflammation, protein-losing/short-bowel enteropathy, and hepatic failure suppressing hepatic transferrin synthesis; it is reversible with treatment of the underlying condition (PMC9807235).

---

## 6. Mechanism / Pathophysiology

**Causal chain (congenital form):**
1. **Trigger:** Biallelic TF loss-of-function mutation → absent or near-absent hepatocyte-synthesized, secreted transferrin protein.
2. **Molecular consequence:** Failure of the normal transferrin–transferrin receptor 1 (TFRC/TfR1, OMIM *190010) cycle: without transferrin, iron cannot be delivered in its physiological, receptor-mediated, endocytosed form to erythroid precursors in the bone marrow.
3. **Cellular consequence (erythroid):** Erythroblasts are starved of iron for heme/hemoglobin synthesis despite whole-body iron sufficiency or excess → ineffective erythropoiesis → **microcytic, hypochromic anemia**.
4. **Systemic consequence (iron handling):** Dietary iron absorbed via duodenal enterocytes (via DMT1/ferroportin) has no transferrin "sink" to bind to in plasma; unbound iron circulates as **non-transferrin-bound iron (NTBI)**. Intestinal DMT1 expression is paradoxically *upregulated* at the villus brush border in hypotransferrinemic states (mouse data), further increasing iron absorption despite tissue iron excess — an inappropriate absorption response driven by low circulating (rather than tissue) iron sensing and low hepcidin.
5. **Tissue uptake of NTBI:** NTBI is taken up avidly by parenchymal cells via **ZIP14 (SLC39A14)** in hepatocytes and pancreatic acinar cells, and via other transporters (e.g., L-type/T-type calcium channels in cardiomyocytes), producing **secondary iron overload/hemosiderosis** concentrated in liver, heart, pancreas, thyroid, and kidney — clinically the mirror image of primary hereditary hemochromatosis but occurring *with* concurrent severe anemia rather than normal hemoglobin.
6. **Regulatory consequence:** Transferrin is itself a major *positive* determinant of hepatic hepcidin expression (via holo-transferrin–driven TfR1/TfR2/HFE signaling); in its absence, hepcidin is inappropriately low, further permitting unchecked intestinal iron absorption and cellular iron efflux via ferroportin — a feed-forward loop that worsens tissue iron loading (PMID cluster on "Transferrin is a major determinant of hepcidin expression in hypotransferrinemic mice").
7. **End-organ damage:** Chronic iron deposition in liver → fibrosis/cirrhosis; in heart → cardiomyopathy, arrhythmia, high-output failure (compounded by chronic anemia); in pancreas/thyroid → diabetes mellitus and hypothyroidism (a hemochromatosis-like endocrinopathy pattern).
8. **Compensatory/alternative iron-delivery pathways** (relevant especially to milder/acquired cases): erythroid precursors and other cells can partially acquire iron independent of classical transferrin–TfR1 via ferritin-receptor pathways (TIM-1/HAVCR1, SCARA5, CXCR4), NTBI transporters (ZIP14, CD44), and direct macrophage-to-erythroblast iron transfer through the erythroblastic island "nurse macrophage" ferroportin-mediated route — explaining why some acquired-atransferrinemia patients maintain near-normal hemoglobin despite undetectable serum transferrin (PMC9807235).

**Molecular pathways:** Transferrin/transferrin receptor cycling (clathrin-mediated endocytosis pathway); hepcidin–ferroportin axis (systemic iron regulation, KEGG "Mineral absorption"/Reactome "Iron uptake and transport"); erythropoiesis and heme biosynthesis pathways (impaired due to iron-restricted erythropoiesis); NTBI uptake pathways (ZIP14/SLC39A14, L-type calcium channels).

**Cellular processes:** Ineffective erythropoiesis; iron-restricted heme synthesis; cellular iron overload–induced oxidative stress (Fenton-chemistry-driven reactive oxygen species) in hepatocytes, cardiomyocytes, and pancreatic acinar cells, leading to organelle damage, fibrogenesis, and eventual cell death/fibrosis (feeding into a fibrotic-response-type cascade in liver and heart).

**Protein dysfunction:** Loss of transferrin protein function — either failure of synthesis/secretion (frameshift/deletion-insertion alleles) or structural destabilization of the iron-binding lobes (missense alleles such as D77N, C137Y, A477P) impairing iron coordination or folding/secretion competence.

**Metabolic changes:** Iron metabolism is the central axis — low/absent plasma iron-transport capacity paired with tissue iron accumulation; secondary metabolic derangements can include impaired mitochondrial function in iron-overloaded hepatocytes and cardiomyocytes and, in the most severe neonatal-onset cases, associated lactic acidosis and aminoaciduria (PMID:10654962), suggesting broader mitochondrial/metabolic stress in profound neonatal presentations.

**Immune system involvement:** Recurrent infections are reported clinically; iron overload is known generally to impair neutrophil and lymphocyte function and to favor growth of siderophilic pathogens, though disease-specific immunology studies in atransferrinemia are lacking.

**Tissue damage mechanisms:** Oxidative stress from labile/catalytic tissue iron (Fenton chemistry generating hydroxyl radicals) driving hepatic fibrosis/cirrhosis and cardiomyopathy; anemia-driven tissue hypoxia (proposed mechanism for the hypospadias reported in one case, via fetal hypoxic insult to genital tubercle development).

**Biochemical abnormalities:** Absent/markedly reduced serum transferrin (<35 mg/dL vs. normal ~200–360 mg/dL), reduced total iron-binding capacity (TIBC), variably low serum iron in classic pediatric presentations (with markedly elevated ferritin reflecting tissue stores) or elevated serum iron with high transferrin saturation in others — the precise lab pattern differing somewhat across reported cases but always featuring a markedly abnormal iron/ferritin/transferrin triad.

**Molecular profiling / advanced technologies:** No transcriptomic, proteomic, metabolomic, single-cell, or spatial-transcriptomic studies specific to human atransferrinemia patient tissue were identified in the literature search — consistent with the extreme rarity of the disease and paucity of available biosamples. Model-organism work (mouse hpx, zebrafish gav) has substituted for human -omics data (see Model Organisms section).

**Suggested GO terms:** GO:0006826 (iron ion transport), GO:0033212 (iron assimilation), GO:0006879 (cellular iron ion homeostasis), GO:0055072 (iron ion homeostasis), GO:0034755 (iron ion transmembrane transport), GO:0033212 (iron uptake); GO Cellular Component: GO:0005576 (extracellular region, for secreted transferrin), GO:0031252 (cell leading edge, for TfR endocytosis machinery — verify applicability).
**Suggested CL terms:** CL:0000765 (erythroblast), CL:0000037 (hematopoietic stem cell), CL:0000182 (hepatocyte), CL:0000138 (chondrocyte — n/a here), CL:0002496 (pancreatic acinar cell), CL:0000746 (cardiac muscle cell / cardiomyocyte).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Bone marrow (erythropoiesis failure) and liver (site of transferrin synthesis and major iron-overload target)
- **Secondary (iron deposition/complications):** heart (cardiomyopathy, arrhythmia), pancreas (endocrine — diabetes), thyroid (hypothyroidism), kidney, joints (arthritis)
- **Body systems involved:** hematologic/immune, hepatic/digestive, cardiovascular, endocrine, musculoskeletal

**Tissue and cell level:**
- Erythroid precursor cells in bone marrow (CL:0000765 erythroblast) — primary site of the functional iron-deficiency lesion
- Hepatocytes (CL:0000182) — site of transferrin synthesis (loss of function) and iron accumulation (hemosiderosis, fibrosis)
- Pancreatic acinar/islet cells — NTBI uptake via ZIP14, leading to islet iron deposition and diabetes
- Cardiomyocytes (CL:0000746) — NTBI uptake causing iron-overload cardiomyopathy
- Reticuloendothelial (macrophage) system — normally receives senescent-RBC iron via transferrin-independent routes; may partially buffer NTBI

**Subcellular level:** Mitochondria (site of heme synthesis, impaired by iron-restricted erythropoiesis, and site of oxidative damage in iron-overloaded cells); lysosomes/endosomes (site of the normal transferrin–TfR1 endocytic iron-release cycle, which is absent given no transferrin cargo); cytosol/ferritin stores (site of accumulated iron in overloaded tissues).

**Localization:** Systemic/multi-organ rather than lateralized; no laterality pattern described.

**Suggested UBERON terms:** UBERON:0002106 (spleen), UBERON:0002107 (liver), UBERON:0000948 (heart), UBERON:0001264 (pancreas), UBERON:0002046 (thyroid gland), UBERON:0002371 (bone marrow), UBERON:0001021 (bone/joint — for arthritis).

---

## 8. Temporal Development

- **Onset:** Typically infancy to early childhood; some cases present as early as birth (severe neonatal form with IUGR, lactic acidosis) and others are recognized incidentally later in childhood or even in the second decade (a 2021 report describes management "in the second decade" — PMID:34792309). Onset pattern is generally insidious (gradual anemia/pallor) rather than acute, though severe neonatal presentations can be fulminant.
- **Progression:** Chronic and, without treatment, progressive — worsening anemia and accumulating tissue iron burden over years, with eventual hepatic fibrosis/cirrhosis and cardiac decompensation. With regular plasma/transferrin replacement therapy, disease course can be stabilized long-term (cases followed into the second decade of life under a "dynamic" fresh-frozen-plasma-plus-chelation approach).
- **Disease course pattern:** Chronic and relapsing (dependent on regularity of plasma/transferrin infusions); if infusions lapse, anemia and iron indices worsen again. In the most severe neonatal cases, the course has been rapidly fatal (death at 8–10 weeks despite apotransferrin/exchange-transfusion therapy).
- **Critical periods:** Early infancy appears to be the highest-risk window for mortality in the most severe genotypes; early diagnosis and initiation of plasma/apotransferrin therapy is critical to prevent irreversible cardiac and hepatic iron deposition.
- **Remission:** No spontaneous remission described for the congenital form (it is a fixed genetic lesion); the reversible *acquired* form can fully normalize once the precipitating nutritional/inflammatory/hepatic condition resolves (PMC9807235).

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (OMIM #209300); disease requires homozygous or compound heterozygous TF mutations. Heterozygous carriers are clinically asymptomatic.
- **Penetrance:** Appears complete for biallelic loss-of-function genotypes, though severity varies (see below).
- **Expressivity:** Variable — ranging from mild, incidentally discovered hypotransferrinemia with manageable anemia, to severe neonatal disease with multi-organ involvement and early death; likely correlates with residual transferrin synthetic capacity of the specific allele combination.
- **Genetic anticipation:** Not described (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported in the literature reviewed.
- **Founder effects:** Plausible given reported consanguineous kindreds (e.g., Turkish case) but no specific founder haplotype has been characterized in the literature surveyed.
- **Consanguinity:** Documented in at least some reported families, consistent with autosomal recessive inheritance in an ultra-rare disease.
- **Carrier frequency:** Not established; given fewer than ~20 kindreds reported worldwide, the disease is far rarer than can support a meaningful population carrier-frequency estimate from current data.

**Epidemiology:**
- **Prevalence:** Unknown/not calculable; Orphanet lists prevalence as unknown. Cumulative literature reports approximately **16–20 cases from ~14–16 families** worldwide since the first 1961 description, making this one of the rarest known inherited disorders of iron metabolism.
- **Incidence:** Not established.
- **Affected populations:** Cases reported across diverse populations/geographies, including the United States, Japan, Turkey, and other countries — no clear ethnic predilection has been established, though consanguinity in some reported families suggests regional clustering tied to specific consanguineous kindreds rather than a broad ethnic association.
- **Geographic distribution:** Sporadic, worldwide case reports rather than an endemic pattern.
- **Sex ratio:** No clear sex predilection reported (autosomal recessive, both male and female cases documented, e.g., hypospadias case is male, other reported cases are female).
- **Age distribution:** Predominantly diagnosed in infancy/childhood, though later presentations (up to the second decade and beyond) have been documented.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Serum transferrin level:** hallmark test; diagnostic threshold cited as serum TF <35 mg/dL (vs. normal ~200–360 mg/dL)
- **Complete blood count:** severe microcytic, hypochromic anemia (hemoglobin as low as 5–6 g/dL in reported cases; MCV markedly reduced, e.g., 58–61 fL)
- **Serum iron:** variably low or normal/elevated depending on case and disease stage
- **Total iron-binding capacity (TIBC):** markedly reduced (reflecting absent transferrin) in most reports, though paradoxically some case series show TIBC within/near normal range with very low transferrin — likely reflecting assay/methodology differences and residual iron-binding proteins
- **Transferrin saturation (%):** elevated/near-100% despite low absolute transferrin, because the small circulating pool is fully iron-saturated
- **Serum ferritin:** markedly elevated (reported values of 1413–2072 µg/L against a normal range of ~45–160 µg/L), reflecting tissue iron stores
- **Imaging:** liver/cardiac MRI (T2*) can quantify tissue iron burden, analogous to its use in other iron-overload disorders (e.g., thalassemia, hemochromatosis) — not specifically detailed in the atransferrinemia literature reviewed but standard practice by extrapolation
- **Biopsy findings:** hepatic biopsy in affected patients would be expected to show iron deposition (hemosiderosis) with variable fibrosis; specific histopathology descriptions were not detailed in the sources reviewed here beyond general hemosiderosis references

**Genetic testing:**
- **Recommended approach:** TF gene sequencing (single-gene test) is the diagnostic confirmatory test once biochemical findings (undetectable/very low transferrin with anemia and iron overload) raise suspicion; also available via targeted gene panels for inherited anemias/iron-overload disorders and via NCBI GTR-listed laboratory tests (GTR gene ID for TF: 7018)
- **Orphanet-listed diagnostic test:** "Molecular diagnosis of atransferrinemia (TF gene)" (Orphanet test ID 367407)
- **WES/WGS:** would be expected to detect TF variants but are not specifically required given the well-defined single-gene etiology; useful when initial targeted testing is uninformative or phenotype is atypical
- **Chromosomal microarray/karyotyping/FISH:** not indicated — disease is due to intragenic point mutations/small indels, not large structural variants

**Clinical criteria:** No formal consensus diagnostic criteria/society guideline exists given the disease's rarity; diagnosis is based on the combination of (1) microcytic hypochromic anemia, (2) markedly low/absent serum transferrin with low TIBC, (3) elevated ferritin/tissue iron overload, and (4) confirmatory TF gene sequencing.

**Differential diagnosis:** Iron-deficiency anemia (distinguished by low, not high, ferritin); hemolytic anemias; congenital dyserythropoietic anemia; aceruloplasminemia (a differential also involving iron-transport dysfunction, but due to CP gene mutations affecting ferroxidase activity rather than transferrin itself); G6PD deficiency; hereditary hemochromatosis (distinguished by normal-to-high hemoglobin rather than severe anemia); acquired/secondary hypotransferrinemia from malnutrition, inflammation, or liver/enteric protein loss.

**Screening:** No newborn screening or population carrier-screening program exists for this ultra-rare disease; case-finding is via clinical recognition of the unusual anemia + iron-overload biochemical pattern, followed by targeted genetic confirmation and cascade testing of relatives.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal survival statistics (5-year/10-year) exist given the extreme rarity of the disease; individual case outcomes vary widely. Severe neonatal-onset disease has been fatal within weeks (two infants died at 8 and 10 weeks of age despite apotransferrin and exchange-transfusion therapy in one report — PMID:10654962), whereas milder/later-onset cases treated with regular plasma or transferrin replacement have been followed successfully into the second decade of life and beyond (PMID:34792309).
- **Life expectancy:** Historically, untreated disease "can be fatal" from cardiac and hepatic iron-overload complications; with modern plasma-infusion/chelation management, long-term survival into adulthood appears achievable, though comprehensive long-term outcome data are lacking.
- **Morbidity/functional outcomes:** Chronic anemia-related fatigue and growth impairment in childhood; risk of hepatic fibrosis/cirrhosis, cardiomyopathy/arrhythmia, diabetes mellitus, and hypothyroidism as iron-overload sequelae if inadequately treated.
- **Complications:** Secondary hemochromatosis-type organ damage (liver, heart, pancreas, thyroid); recurrent infections; possible developmental anomalies from fetal hypoxia in severe prenatal-onset disease (hypospadias case).
- **Recovery potential:** With treatment (regular plasma/transferrin infusion ± chelation/phlebotomy), anemia and iron overload can be substantially improved (e.g., hemoglobin rising from 6.4 g/dL to >10 g/dL after apotransferrin dosing; ferritin declining from 1413 to 903 µg/L over 12 months of FFP therapy in one case). Without treatment, the disease is progressive and can be fatal.
- **Prognostic factors:** Genotype/residual transferrin synthetic capacity, age at diagnosis/treatment initiation, adherence to regular infusion therapy, and degree of cardiac/hepatic iron deposition at the time treatment begins.

---

## 12. Treatment

**Pharmacotherapy / plasma-based replacement (mainstay of treatment):**
- **Fresh frozen plasma (FFP) infusion:** Standard, most widely used therapy; provides exogenous transferrin. In one case series, monthly FFP produced reticulocytosis (6% at 2 weeks), hemoglobin rise to 12.4 g/dL at 1 month, and ferritin decline to 903 µg/L by 12 months (PMC5544637).
- **Apotransferrin (purified/iron-free transferrin) infusion:** Used in several reported cases; an 8-year-old boy given 2 g apotransferrin (9.8% protein in normal saline) over three doses across 16 days had hemoglobin rise from 6.4 g/dL to >10 g/dL. Intravenous apotransferrin combined with exchange transfusion has also been trialed in severe neonatal-onset disease to normalize transferrin saturation, and was reported as "safe" though not lifesaving in that specific severe cohort (PMID:10654962).
- **Recombinant human transferrin:** Mentioned in the literature as a treatment modality alongside plasma-derived transferrin, though clinical experience is limited given disease rarity.
- **Iron chelation therapy:** Used adjunctively to manage secondary iron overload (e.g., deferoxamine/deferasirox-class agents), particularly in a "dynamic approach" combining FFP with iron-directed therapy described for maintaining hematologic stability into the second decade of life (PMID:34792309).
- **Phlebotomy:** Mentioned as an adjunct to reduce iron burden in some management approaches, analogous to hemochromatosis management, though must be balanced against the patient's underlying anemia.

**Contraindicated therapy:** Direct **iron supplementation is contraindicated** — it does not correct the anemia (because erythroid iron utilization requires transferrin-mediated delivery) and instead worsens secondary hemosiderosis.

**Surgical/interventional:** No disease-specific surgical intervention beyond standard management of iron-overload complications (e.g., addressing hypospadias surgically if present as a congenital anomaly, unrelated to the core iron pathway).

**Supportive/rehabilitative care:** Management of growth, nutrition, and infection risk in affected children; endocrine management (thyroid hormone replacement, diabetes management) if hypothyroidism/diabetes develop from iron overload.

**Experimental/investigational:** No registered clinical trials specific to atransferrinemia were identified (consistent with its ultra-rarity precluding formal trial recruitment); management is based on case-report-level evidence and extrapolation from broader iron-overload/transfusion-dependent anemia management principles.

**Treatment outcomes:** Response to plasma/apotransferrin infusion is generally favorable for correcting anemia acutely, but the very severe neonatal genotype cohort described above did not survive despite treatment, indicating that genotype/disease severity and timing of intervention are critical determinants of outcome.

**Suggested NCIT terms for treatment annotation:**
- NCIT:C15986 (Pharmacotherapy) — generic parent for plasma/transferrin/chelator administration
- NCIT:C15747 (Supportive Care)
- Blood product/plasma infusion does not have a precise dedicated NCIT clinical-action term in the standard set used here; would need specific lookup (e.g., "Fresh Frozen Plasma Transfusion" or "Plasma Exchange" terms) via NCIT search
- Iron chelation therapy would be annotated under NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to the specific chelator (e.g., CHEBI term for deferoxamine/deferasirox)

**Treatment strategy:** No formal treatment algorithm/guideline exists; management follows individualized case-based protocols combining regular transferrin/plasma replacement with iron-overload monitoring and adjunctive chelation, titrated to hemoglobin and ferritin/iron-saturation response.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (a fixed germline genetic disease); the only "primary prevention" avenue is genetic counseling and reproductive options (see below) for known carrier couples.
- **Secondary prevention:** Early recognition of the anemia + iron-overload biochemical pattern to initiate transferrin/plasma replacement before irreversible cardiac/hepatic damage accrues; regular monitoring of ferritin, transferrin saturation, and cardiac/hepatic iron burden (e.g., T2* MRI) in known patients.
- **Tertiary prevention:** Chelation therapy and dose-titrated plasma/transferrin replacement to prevent progression of established organ iron overload to fibrosis/cirrhosis and cardiomyopathy; endocrine surveillance (thyroid function, glucose tolerance) to catch and treat iron-overload endocrinopathy early.
- **Immunization:** No disease-specific vaccine strategy; standard-of-care immunizations remain appropriate, and given the reported susceptibility to recurrent infections, timely routine vaccination and prompt treatment of infections are reasonable general measures (not disease-specific literature-supported recommendations).
- **Screening/early detection:** No population or newborn screening program exists; case detection currently relies on clinical suspicion triggered by unexplained microcytic anemia with a disproportionately elevated ferritin/undetectable transferrin.
- **Genetic screening/counseling:** For families with a known affected child or confirmed carrier status, genetic counseling regarding autosomal recessive recurrence risk (25% for future pregnancies of two carrier parents), carrier testing of at-risk relatives, and prenatal or preimplantation genetic testing options (where a familial pathogenic variant has been identified) are the standard reproductive-risk-management tools, by extrapolation from general recessive-disease practice (no atransferrinemia-specific prenatal testing literature was identified).
- **Risk stratification:** Not formally developed for this disease.
- **Public health / environmental / prophylactic interventions:** Not applicable to the congenital genetic form; for the *acquired* form, addressing underlying malnutrition, inflammatory disease, and hepatic dysfunction is itself the "preventive" strategy, since correcting those drivers reverses the acquired hypotransferrinemia.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Mouse (*Mus musculus*, NCBITaxon:10090) and zebrafish (*Danio rerio*, NCBITaxon:7955) are the two species with well-characterized naturally occurring or induced Tf-deficiency models; no confirmed spontaneously occurring veterinary (companion animal/livestock) cases of atransferrinemia were identified in this search.
- **Gene orthologs:** Mouse *Trf* (ortholog of human TF); zebrafish *tfa* (transferrin-a; zebrafish carry a teleost-specific duplicate, tfa/tfb, arising from genome duplication).
- **Natural disease:**
  - **Mouse hpx (hypotransferrinemic) strain:** A spontaneous mutation originating in the BALB/cJ strain decades ago; *Trf^hpx/hpx* mice have <1% of normal plasma transferrin. The molecular defect is a point mutation at the exon 16 splice-donor site, abolishing normal Trf mRNA splicing (with only low-level aberrant transcripts produced via cryptic splice sites, including a predominant 27-bp in-frame deletion transcript) (PMID:10910930; original strain description PMID:3681112, "Hereditary hypotransferrinemia with hemosiderosis, a murine disorder resembling human atransferrinemia").
  - **Zebrafish gavi (gav) mutant:** Identified in a large-scale forward-genetic screen for hypochromic-anemia phenotypes; caused by mutations (alleles gav^IT029 and gav^HE067) producing aberrant splicing of the transferrin-a (tfa) transcript, closely phenocopying human congenital hypotransferrinemia including hypochromic anemia and, in the fish, embryonic lethality by ~14 days post-fertilization if untreated (PMID:19047682).
- **Veterinary relevance:** No specific reports of naturally occurring atransferrinemia in companion animals or livestock were found in this search; the disease's veterinary significance is therefore primarily as a research model concept (mouse, zebrafish) rather than a recognized spontaneous veterinary disease entity.
- **Comparative biology/evolutionary conservation:** The transferrin–TfR1 iron-delivery mechanism and the hepcidin–ferroportin regulatory axis are highly conserved across vertebrates, which is why both mouse and zebrafish models recapitulate the core human phenotype (anemia + iron mismanagement) faithfully, supporting cross-species mechanistic inference.
- **Transmission/zoonotic potential:** Not applicable — a non-communicable, monogenic disorder.

---

## 15. Model Organisms

| Model | Type | Genetic lesion | Phenotype recapitulation | Limitations | Key reference |
|---|---|---|---|---|---|
| **Mouse hpx (Trf^hpx/hpx), BALB/cJ background** | Spontaneous point mutation (induced/naturally arising model organism) | Splice-donor site mutation after exon 16 of Trf, abolishing normal splicing; residual mRNA via cryptic splicing (27-bp in-frame deletion transcript) | Severe anemia and tissue iron overload; mice die before weaning unless treated with exogenous transferrin or RBC transfusion — closely mirrors human disease severity and dual anemia/iron-overload phenotype; also shows compensatory intestinal DMT1 upregulation, informative for the human NTBI-absorption mechanism | Neonatal lethality without intervention makes long-term/adult study harder without rescue treatment; species differences in iron physiology (e.g., placental iron transfer, dietary patterns) may limit some translational inferences | PMID:3681112 (original description); PMID:10910930 (molecular defect); additional hepcidin/DMT1 mechanistic studies in hpx mice |
| **Zebrafish gavi (gav) mutant, alleles gav^IT029/gav^HE067** | Induced/naturally arising mutant (forward genetic screen) | Mutations causing aberrant splicing of transferrin-a (tfa) | Hypochromic anemia and (if untreated) embryonic/larval lethality by ~14 dpf; morpholino knockdown of tfa reproduces the anemia and reduced tissue iron staining phenotype, and this is rescued by tfa cRNA co-injection — a strong causality/rescue demonstration | Zebrafish possess a duplicated transferrin gene (tfa/tfb) from teleost genome duplication, an evolutionary difference from the single human TF gene; external embryonic development and high fecundity make it excellent for early-development and high-throughput screening studies but less suited to modeling adult-onset organ complications (cardiomyopathy, cirrhosis, endocrinopathy) seen in human patients | PMID:19047682 |

**Applications:** Both models have been used to dissect (1) the erythropoiesis defect caused by iron-restricted heme synthesis, (2) the compensatory/dysregulated intestinal iron absorption response (DMT1 upregulation in mouse), and (3) the hepcidin-suppression mechanism that drives secondary iron overload — directly informing the pathophysiological model described in Section 6. The zebrafish model in particular has been leveraged for genetic and morpholino-based mechanistic dissection given the ease of embryonic manipulation and imaging.

**Resources:** Mouse Genome Informatics (MGI) for the *Trf^hpx* allele; ZFIN for the zebrafish *gav* mutant allele records.

---

## Summary for Knowledge-Base Curation

Atransferrinemia is a well-bounded, single-gene (TF, chromosome 3q22.1), autosomal recessive disorder (OMIM #209300 / ORPHA:1195) with a clear, well-documented causal chain: TF loss-of-function mutation → absent/low plasma transferrin → failure of transferrin-receptor–mediated iron delivery to erythroid precursors (microcytic/hypochromic anemia) in parallel with unregulated NTBI uptake via ZIP14 and low hepcidin → secondary iron overload in liver, heart, pancreas, thyroid, and kidney. It has strong, cross-species mechanistic validation from both the classical mouse *hpx* strain and the zebrafish *gavi* mutant, several molecularly characterized human cases with specific pathogenic TF variants (D77N, C137Y, A477P, and a deletion-insertion allele), and an established (if evidence-limited, given disease rarity) treatment paradigm centered on plasma/apotransferrin replacement plus iron chelation, with iron supplementation specifically contraindicated. A distinct, environmentally triggered and reversible "acquired atransferrinemia" phenocopy (malnutrition/inflammation/liver failure) should be modeled or annotated separately from the congenital genetic disease, and its physiology (near-normal hemoglobin despite absent transferrin) offers useful mechanistic contrast highlighting non-canonical/compensatory iron-delivery pathways.

---

**Sources:**
- [Entry - #209300 - ATRANSFERRINEMIA - OMIM](https://omim.org/entry/209300)
- [Entry - *190000 - TRANSFERRIN; TF - OMIM](https://omim.org/entry/190000)
- [Orphanet: Congenital atransferrinemia (ORPHA:1195)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=1195)
- [Orphanet: TF-transferrin](https://www.orpha.net/en/disease/gene/TF)
- [Atransferrinemia - Symptoms, Causes, Treatment | NORD](https://rarediseases.org/rare-diseases/atransferrinemia/)
- [Atransferrinemia | About the Disease | GARD](https://rarediseases.info.nih.gov/diseases/9595/atransferrinemia)
- [Atransferrinemia - Wikipedia](https://en.wikipedia.org/wiki/Atransferrinemia)
- [Atransferrinemia - an overview | ScienceDirect Topics](https://www.sciencedirect.com/topics/medicine-and-dentistry/atransferrinemia)
- [Congenital Hypotransferrinemia, an Unusual Cause of Iron Deficiency Anemia: Report of Two Cases - PMC (PMID:28824244)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5544637/)
- [A Rare Case of Congenital Atransferrinemia: International Collaboration for Genetic Diagnosis | Blood](https://ashpublications.org/blood/article/124/21/4883/94110/A-Rare-Case-of-Congenital-Atransferrinemia)
- [Molecular characterization of a case of atransferrinemia | Blood (PMID:11110675)](https://ashpublications.org/blood/article/96/13/4071/176175/Molecular-characterization-of-a-case-of)
- [Molecular characterization of a third case of human atransferrinemia | Blood (PMID:15466165)](https://ashpublications.org/blood/article/104/8/2607/19095/Molecular-characterization-of-a-third-case-of)
- [A new case of human atransferrinemia with a previously undescribed mutation in the transferrin gene - PubMed (PMID:18097132)](https://pubmed.ncbi.nlm.nih.gov/18097132/)
- [Exogenous apotransferrin and exchange transfusions in hereditary iron overload disease - PubMed (PMID:10654962)](https://pubmed.ncbi.nlm.nih.gov/10654962/)
- [Fresh Frozen Plasma Plus Iron Therapy in Congenital Hypotransferrinemia in the Second Decade - PubMed (PMID:34792309)](https://pubmed.ncbi.nlm.nih.gov/34792309/)
- [Reversible atransferrinemia in a patient with chronic enteropathy: is transferrin mandatory for iron transport? - PMC (PMID:9807235 article)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9807235/)
- [Transferrin-a modulates hepcidin expression in zebrafish embryos - PubMed (PMID:19047682)](https://pubmed.ncbi.nlm.nih.gov/19047682/)
- [The molecular defect in hypotransferrinemic mice - PubMed (PMID:10910930)](https://pubmed.ncbi.nlm.nih.gov/10910930/)
- [Hereditary hypotransferrinemia with hemosiderosis, a murine disorder resembling human atransferrinemia - PubMed (PMID:3681112)](https://pubmed.ncbi.nlm.nih.gov/3681112/)
- [Transferrin is a major determinant of hepcidin expression in hypotransferrinemic mice | Blood](https://ashpublications.org/blood/article/117/2/630/28165/Transferrin-is-a-major-determinant-of-hepcidin)
- [Zip14 (Slc39a14) mediates non-transferrin-bound iron uptake into cells | PNAS](https://www.pnas.org/doi/10.1073/pnas.0606424103)
- [TF transferrin - NIH Genetic Testing Registry (GTR) - NCBI](https://www.ncbi.nlm.nih.gov/gtr/genes/7018/)
- [NM_001063.4(TF):c.1765C>T (p.Pro589Ser) AND Atransferrinemia - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000376325/)
- [NM_001063.3(TF):c.-117G>A AND Atransferrinemia - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000338348/)
- [NM_001063.4(TF):c.229G>A (p.Asp77Asn) AND Atransferrinemia - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000013456/)