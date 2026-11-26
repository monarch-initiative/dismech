# Citations for Research Query

**Query:** # Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Histiocytic Sarcoma
- **MONDO ID:** MONDO:0019479 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** sarcoma, histiocytic, malignant
- **Category:** Neoplasm. Scope rules for this report - rely on series that apply the modern definition (immunophenotyped, with lymphoma and other mimics excluded); leave out ALK-positive histiocytosis (name it only as a separate disease), ALK staining, anaplastic large cell lymphoma and any ALK-directed treatment or trial; state any NF1 or NF2 change at gene level only; do not name or discuss chromosome-arm changes (in particular 1p36, 11q or 17q) or chromothripsis. It is mostly an adult disease; do not describe it as a childhood tumour unless a source says so.

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Histiocytic Sarcoma** covering all of the
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

**Provider:** claude_code
**Generated:** 2026-11-21T00:25:20.420183

1. https://rarediseases.org/mondo-disease/histiocytic-sarcoma/
2. https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86896
3. https://pubmed.ncbi.nlm.nih.gov/30626916/
4. https://academic.oup.com/oncolo/article/26/7/e1263/6510483
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC12429796/
6. https://doi.org/10.3390/ijms26178554
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9252913/
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11076448/
9. https://pubmed.ncbi.nlm.nih.gov/41915766/
10. https://doi.org/10.1182/blood.2026033049
11. https://seer.cancer.gov/icd-o-3/sitetype.icdo3.20220429.pdf
12. https://www.pathologyoutlines.com/topic/lymphnodeshistiocyticsarcoma.html
13. https://icdlist.com/icd-10/C96.A
14. https://www.icd10data.com/ICD10CM/Codes/C00-D49/C81-C96/C96-
15. https://seer.cancer.gov/seertools/hemelymph/51f6cf59e3e27c3994bd5471/
16. https://en.wikipedia.org/wiki/Malignant_histiocytosis
17. https://www.researchgate.net/publication/321353983_Histiocytic_sarcoma_A_population-based_analysis_of_incidence_demographic_disparities_and_long-term_outcomes
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC9271260/
19. https://ashpublications.org/bloodadvances/article/9/10/2530/535782/Characterization-and-treatment-outcomes-of
20. https://haematologica.org/article/view/9331
21. https://www.modernpathology.org/article/S0893-3952(23
22. https://www.nature.com/articles/s41379-020-00673-x
23. https://www.nature.com/articles/s41408-025-01335-4
24. https://www.modernpathology.org/article/S0893-3952(22
25. https://doi.org/10.1093/ajcp/aqac087
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC12270463/
27. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12310312/
28. https://pubmed.ncbi.nlm.nih.gov/16086090/
29. https://pubmed.ncbi.nlm.nih.gov/36051154/
30. https://pubmed.ncbi.nlm.nih.gov/33786289/
31. https://pubmed.ncbi.nlm.nih.gov/18987551/
32. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10546704/
33. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5066022/
34. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4544561/
35. https://ashpublications.org/blood/article/128/20/2475/35616/Histiocytic-sarcoma-secondary-neoplasm-or
36. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400417/
37. https://pubmed.ncbi.nlm.nih.gov/41135521/
38. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1505737/xml
39. https://monarchinitiative.org/HP:0002716
40. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12400779/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC9124500/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC6170302/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC13478121/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC11452572/
45. https://doi.org/10.3390/diagnostics16162623
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC11413427/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC12279446/
48. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7481156/
49. https://ashpublications.org/bloodadvances/article/9/6/1376/534302/Anxiety-and-depression-in-patients-with
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC10481619
51. https://bloodcancerunited.org/research/award/patient-reported-outcomes-and-survivorship-histiocytic-neoplasms
52. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9124500/
53. https://link.springer.com/article/10.1007/s00795-024-00393-0
54. https://pubmed.ncbi.nlm.nih.gov/32238464/
55. https://pmc.ncbi.nlm.nih.gov/articles/PMC12616613/
56. https://academic.oup.com/ajcp/article/164/Supplement_1/aqaf121.281/8321081
57. https://pmc.ncbi.nlm.nih.gov/articles/PMC6190545/
58. https://dx.doi.org/10.1093/ajcp/aqz056
59. https://onlinelibrary.wiley.com/doi/full/10.1002/ajh.26983
60. https://pmc.ncbi.nlm.nih.gov/articles/PMC13472141/
61. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12067900/
62. https://pmc.ncbi.nlm.nih.gov/articles/PMC13432202/
63. https://www.nature.com/articles/s41572-021-00307-9
64. https://doi.org/10.1182/bloodadvances.2024015275
65. https://www.medrxiv.org/content/10.64898/2026.07.02.26356825v1.full
66. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11794134/
67. https://ashpublications.org/blood/article/142/Supplement%201/1161/505458/Deciphering-the-Epigenetic-Landscape-in
68. https://doi.org/10.3390/ijms27114949
69. https://amigo.geneontology.org/amigo/term/GO:0000165
70. https://pubmed.ncbi.nlm.nih.gov/30867592/
71. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10212919/
72. https://pmc.ncbi.nlm.nih.gov/articles/PMC11940154/
73. https://www.nature.com/articles/3800346
74. https://pubmed.ncbi.nlm.nih.gov/34330800/
75. https://dx.doi.org/10.1080/10428194.2025.2561114
76. https://pubmed.ncbi.nlm.nih.gov/38098600/
77. https://www.ebi.ac.uk/ols4/ontologies/cl/entities/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0000235
78. https://cellxgene.cziscience.com/cellguide/CL:0000235
79. https://pubmed.ncbi.nlm.nih.gov/39048487
80. https://diagnosticpathology.biomedcentral.com/articles/10.1186/1746-1596-2-7
81. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11149727/
82. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10918721/
83. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12920180/
84. https://pubmed.ncbi.nlm.nih.gov/42405293/
85. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7888511/
86. https://pubmed.ncbi.nlm.nih.gov/35884764/
87. https://m.bioportal.bioontology.org/ontologies/OBI_BCGO?conceptid=http://purl.obolibrary.org/obo/UBERON_0000029&p=classes
88. https://www.uptodate.com/contents/histiocytic-sarcoma/abstract/2
89. https://pmc.ncbi.nlm.nih.gov/articles/PMC12144458/
90. https://pubmed.ncbi.nlm.nih.gov/41049224/
91. https://pubmed.ncbi.nlm.nih.gov/40260333/
92. https://pmc.ncbi.nlm.nih.gov/articles/PMC9297408/
93. https://doi.org/10.6004/jnccn.2022.7001
94. https://www.sciencedirect.com/science/article/abs/pii/S2666636725002908
95. https://www.sciencedirect.com/topics/medicine-and-dentistry/histiocytic-sarcoma
96. https://meridian.allenpress.com/aplm/article/142/11/1322/103148/Histiocytic-Sarcoma-Review-Discussion-of
97. https://jcdr.net/articles/PDF/19763/70351_CE%5BRa1%5D_F(IS
98. https://pmc.ncbi.nlm.nih.gov/articles/PMC4349012/
99. https://pubmed.ncbi.nlm.nih.gov/29676378
100. https://tech.snmjournals.org/content/49/4/358
101. https://pubmed.ncbi.nlm.nih.gov/34781268/
102. https://pubmed.ncbi.nlm.nih.gov/25324352/?dopt=Abstract
103. https://pmc.ncbi.nlm.nih.gov/articles/PMC5705028/
104. https://ashpublications.org/blood/article/142/Supplement%201/6332/506171/Molecular-Findings-on-Plasma-Cell-Free-DNA
105. https://meridian.allenpress.com/aplm/article/144/5/650/427448/Histiocytic-Sarcoma
106. https://pubmed.ncbi.nlm.nih.gov/42264920/
107. https://www.erdheim-chester.org/wp-content/uploads/2022/08/NCCN-Guidelines-for-Histiocytic-Neoplasms.pdf
108. https://www.mskcc.org/news-releases/fda-approves-oral-mek-inhibitor-cobimetinib-histiocytic-neoplasms-research-led-msk-cancer
109. https://ascopost.com/issues/december-10-2022/fda-approves-oral-mek-inhibitor-cobimetinib-for-histiocytic-neoplasms/
110. https://ashpublications.org/blood/article/142/Supplement%201/1812/505051/Phase-2-Trial-of-Single-Agent-Cobimetinib-for
111. https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C77908
112. https://www.researchgate.net/publication/325191894_Trametinib_in_Histiocytic_Sarcoma_with_an_Activating_MAP2K1_MEK1_Mutation
113. https://haematologica.org/article/view/8337
114. https://www.thejh.org/index.php/jh/article/view/1030/678
115. https://pmc.ncbi.nlm.nih.gov/articles/PMC12481021/
116. https://aacrjournals.org/cancerdiscovery/article-abstract/16/1/OF1/771345/RAF-independent-MEK1-mutant-Histiocytoses-Respond?redirectedFrom=fulltext
117. https://ascopubs.org/doi/10.1200/PO-24-00471
118. https://pubmed.ncbi.nlm.nih.gov/41798885/
119. https://pmc.ncbi.nlm.nih.gov/articles/PMC10718375/
120. https://pmc.ncbi.nlm.nih.gov/articles/PMC11366101/
121. https://onlinelibrary.wiley.com/doi/10.1111/crj.13741
122. https://www.mdpi.com/1422-0067/25/13/7293
123. https://pmc.ncbi.nlm.nih.gov/articles/PMC12853904/
124. https://doi.org/10.1182/blood-2024-208929
125. https://doi.org/10.3390/hematolrep18010002
126. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4718299/
127. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9162887/
128. https://www.researchgate.net/publication/276347560_Palliative_care_in_the_home_a_case_study_of_secondary_histiocytic_sarcoma_in_a_3-year-old_child
129. https://clinicaltrials.gov/study/NCT02649972
130. https://clinicaltrials.gov/study/NCT04079179
131. https://clinicaltrials.gov/study/NCT04007848
132. https://clinicaltrials.gov/study/NCT04437381
133. https://omia.org/OMIA000620/9615/
134. https://pmc.ncbi.nlm.nih.gov/articles/PMC3658424/
135. https://pubmed.ncbi.nlm.nih.gov/19531730/
136. https://www.histiocytosis.ucdavis.edu/
137. https://hospital.cvm.ncsu.edu/services/small-animals/cancer-oncology/oncology/canine-histiocytic-sarcoma/
138. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9504151/
139. https://cebp.aacrjournals.org/content/21/7/1019
140. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8016107/
141. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6678586/
142. https://www.researchgate.net/publication/340167279_PTPN11_mutations_in_canine_and_human_disseminated_histiocytic_sarcoma
143. https://en.wikipedia.org/wiki/Canine_histiocytic_diseases
144. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5644619/
145. https://pubmed.ncbi.nlm.nih.gov/17338159/
146. https://doi.org/10.1111/j.1939-1676.2007.tb02937.x
147. https://www.researchgate.net/publication/274402918_Evaluation_of_a_combination_chemotherapy_protocol_including_lomustine_and_doxorubicin_in_canine_histiocytic_sarcoma
148. https://doi.org/10.1111/jvim.13964
149. https://pmc.ncbi.nlm.nih.gov/articles/PMC11144536/
150. https://pmc.ncbi.nlm.nih.gov/articles/PMC11442397/
151. https://journals.sagepub.com/doi/10.1177/03009858231166658
152. https://pmc.ncbi.nlm.nih.gov/articles/PMC11219191/
153. https://pmc.ncbi.nlm.nih.gov/articles/PMC12906819/
154. https://pubmed.ncbi.nlm.nih.gov/40783184/
155. https://journals.sagepub.com/doi/10.1177/0300985811430696
156. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0097280
157. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4020815/
158. https://www.biorxiv.org/content/10.1101/2025.03.12.642796v2.full
159. https://pmc.ncbi.nlm.nih.gov/articles/PMC13627489
160. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3432091/
161. https://www.cellosaurus.org/CVCL_0007
162. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5831740/
163. https://www.cellosaurus.org/CVCL_L315
164. https://www.cellosaurus.org/CVCL_IU62
165. https://www.cellosaurus.org/CVCL_3997
166. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7718904/
167. https://www.mdpi.com/1422-0067/26/17/8554
168. https://www.malacards.org/card/histiocytic_sarcoma
169. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11232355/
170. https://ashpublications.org/blood/article/148/3/275/567492/Consensus-recommendations-for-malignant
171. https://www.nature.com/articles/s41379-018-0200-x
172. https://pmc.ncbi.nlm.nih.gov/articles/PMC9161669/
173. https://dx.doi.org/10.1002/onco.13801
174. https://pmc.ncbi.nlm.nih.gov/articles/PMC4276966/
175. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891036/
176. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7918796/
177. https://pmc.ncbi.nlm.nih.gov/articles/PMC9882698/
178. https://pubmed.ncbi.nlm.nih.gov/41835761/
179. https://pmc.ncbi.nlm.nih.gov/articles/PMC5124769/
180. https://www.cellosaurus.org/CVCL_W472
181. https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C69145