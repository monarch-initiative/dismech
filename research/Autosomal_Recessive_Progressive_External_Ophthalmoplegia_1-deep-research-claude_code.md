---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T16:21:01.621461'
end_time: '2026-07-31T16:27:08.515492'
duration_seconds: 366.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Progressive External Ophthalmoplegia 1
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
  web_search_requests: 17
  num_turns: 25
  total_cost_usd: 1.8542326999999996
  session_id: 1ff1ab7e-d42a-5ad6-b222-89444922f8c7
  stop_reason: end_turn
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Progressive External Ophthalmoplegia 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Progressive External Ophthalmoplegia 1** covering all of the
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

# Autosomal Recessive Progressive External Ophthalmoplegia 1 (PEOB1) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Autosomal recessive progressive external ophthalmoplegia with mitochondrial DNA deletions, type 1 (PEOB1) is a mitochondrial DNA-maintenance disorder caused by biallelic (homozygous or compound heterozygous) pathogenic variants in **POLG**, the nuclear gene encoding the catalytic subunit of mitochondrial DNA polymerase gamma (Pol γA). It is a chronic, typically adult-onset (>40 years) disease defined by progressive weakness of the extraocular muscles (bilateral ptosis and diffuse, symmetric ophthalmoparesis), exercise intolerance, and the presence of multiple mitochondrial DNA (mtDNA) deletions in skeletal muscle. PEOB1 sits within the broader "POLG-related disorders" spectrum, which ranges from the fatal infantile Alpers-Huttenlocher syndrome to the comparatively benign late-onset autosomal recessive PEO described here (Van Goethem et al., *Nat Genet* 2001, PMID not directly retrieved but DOI 10.1038/90034; OMIM #258450).

**Key identifiers:**
- **OMIM:** #258450 — "Progressive External Ophthalmoplegia with Mitochondrial DNA Deletions, Autosomal Recessive 1; PEOB1" (gene-disease relationship: *POLG*, OMIM *174763, chromosome 15q26.1)
- **Gene:** POLG (HGNC:9179), also historically POLG1
- **Orphanet:** ORPHA:254886 — "Autosomal recessive progressive external ophthalmoplegia"
- **MONDO:** the umbrella MONDO term for this entity should be cross-checked against MONDO's POLG-PEO recessive class (searchable via OLS/MONDO as "progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 1")
- **MeSH:** Ophthalmoplegia, Chronic Progressive External (D029231); Mitochondrial Diseases (D028361)
- **ICD-10:** H49.4 (Progressive external ophthalmoplegia); G71.3 (Mitochondrial myopathy, NEC) is sometimes used for the systemic phenotype
- **GeneReviews:** "POLG-Related Disorders" (NCBI Bookshelf NBK26471)
- **GTR condition:** C1850303 (autosomal recessive PEO)

**Synonyms:** PEOB1; Ophthalmoplegia, progressive external, autosomal recessive, with mitochondrial DNA deletions; arPEO; CPEO (chronic progressive external ophthalmoplegia) — note CPEO is the broader clinical umbrella term, not gene-specific; POLG-related PEO (recessive form); mitochondrial DNA depletion syndrome 4 nomenclature overlaps in some databases with the more severe POLG spectrum entries (Alpers syndrome, MCHS, SANDO/MIRAS) which share the same causal gene but different allele combinations.

**Evidence base:** Predominantly derived from aggregated case series, multi-center cohort studies (e.g., the 155-patient Hikmat et al. 2020 cohort, *J Inherit Metab Dis*, PMID 32068908), disease-level curated resources (OMIM, Orphanet, GeneReviews), and individual case reports — not large-scale EHR-based epidemiology, reflecting the disease's rarity.

---

## 2. Etiology

**Disease causal factor:** PEOB1 is a **monogenic, purely genetic** disease. It requires **biallelic pathogenic variants in POLG** (chr15q26.1), which abolish or severely impair the catalytic and/or proofreading (3′→5′ exonuclease) activity of the mitochondrial DNA polymerase, the sole DNA polymerase responsible for replicating the mitochondrial genome. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause of this specific PEOB1 entity — although "environmental" or "gene-environment" stressors (below) can modulate disease severity or unmask latent POLG dysfunction.

**Genetic risk factors:**
- Two pathogenic POLG alleles are required (true autosomal recessive; heterozygous carriers are asymptomatic or rarely mildly symptomatic).
- **Founder/common pathogenic variants:**
  - **c.1399G>A (p.Ala467Thr)** — the single most common recessive POLG pathogenic allele; accounts for roughly 31–45% of mutant alleles in some European cohorts; gnomAD overall frequency ≈0.051% (143/282,888 alleles), rising to ≈0.098% in non-Finnish Europeans; population genetics studies (Chinnery et al./Rajakulendran, *EJHG* 2007) trace it to single ancient European founders.
  - **c.2243G>C (p.Trp748Ser)** — very common, frequently found *in cis/trans* with A467T as a compound "haplotype" allele; individually associated with more severe recessive phenotypes when combined with a second severe allele.
  - **c.2542G>A (p.Gly848Ser)** — a third recurrent founder variant, often reported in seizure-associated POLG phenotypes.
  - Combined carrier frequency for these founder alleles reaches ~1% in some European-descent populations (Rajakulendran et al., *Eur J Hum Genet* 2016).
- **Genotype-phenotype correlation:** Variants located in the **polymerase (Pol) domain** (including the classic Y955C originally identified by Van Goethem et al. 2001) tend to produce more severe phenotypes when biallelic; variants in the linker region are typically associated with milder, later-onset PEO. Homozygous or compound heterozygous combinations involving at least one "severe" allele generally shift phenotype toward the ataxia-neuropathy spectrum (MIRAS/SANDO) or earlier-onset Alpers-like disease, while combinations of milder proofreading-domain alleles (e.g., A467T with another mild allele) are more likely to present as isolated late-onset PEO.
- **Modifier/susceptibility genes:** No confirmed nuclear modifier genes for PEOB1 specifically; mtDNA haplogroup background has been proposed as a modifier of mitochondrial disease severity generally but is not established for POLG-PEO.
- **Digenic/oligogenic interaction:** Not established for PEOB1 — this is a single-locus recessive disorder (distinguish from the broader class of "multiple mtDNA deletion disorders," MDMDs, caused by ≥20 different nuclear genes including TWNK, RRM2B, DGUOK, SLC25A4/ANT1, OPA1, MGME1, RNASEH1, TK2, TOP3A, DNA2 — genetically heterogeneous phenocopies, not modifiers of POLG-PEO itself).

**Protective factors:** No established genetic or environmental protective factors specific to PEOB1. General mitochondrial-supportive measures (aerobic exercise, avoidance of mitochondrial toxins) are supportive/management-oriented rather than disease-preventive (see Treatment/Prevention).

**Environmental/gene-environment interaction — the critical clinical interaction:**
- **Valproic acid (sodium valproate) is an absolute contraindication** in any POLG-related disorder, including PEOB1. Valproate is metabolized via mitochondrial β-oxidation and can precipitate acute, sometimes fatal, hepatic failure in POLG-mutant patients — a well-documented gene-drug interaction (Stewart et al., *Lancet Neurol* 2010, and cautionary statements throughout GeneReviews). This is the single most important gene-environment interaction to flag clinically.
- Other mitochondrial toxins (e.g., certain antiretrovirals affecting mtDNA polymerase, aminoglycosides affecting mitochondrial translation) are theoretically relevant to worsening mitochondrial reserve but are not disease-causal.
- Physiologic stress (fasting, intercurrent infection, surgery) is reported anecdotally to unmask or worsen symptoms in POLG disease broadly, consistent with reduced mitochondrial energetic reserve, though this is best documented in the early-onset/Alpers phenotypes rather than isolated arPEO.

---

## 3. Phenotypes

### Core/defining phenotypes
| Phenotype | Type | Suggested HPO term |
|---|---|---|
| Bilateral ptosis | Clinical sign | HP:0000508 (Ptosis) |
| Progressive external ophthalmoplegia / ophthalmoparesis | Clinical sign | HP:0000590 (Ophthalmoplegia) / HP:0000602 (Ophthalmoparesis) |
| Exercise intolerance | Symptom | HP:0003546 (Exercise intolerance) |
| Proximal/generalized skeletal muscle weakness | Clinical sign | HP:0003701 (Proximal muscle weakness) / HP:0001324 (Muscle weakness) |
| Muscle atrophy | Clinical sign | HP:0003202 (Skeletal muscle atrophy) |

### Additional/variable manifestations (PEO-"plus" features)
| Phenotype | Type | Suggested HPO term |
|---|---|---|
| Sensory axonal peripheral neuropathy | Clinical sign | HP:0003390 (Aplasia/Hypoplasia... ) — better: HP:0007141 (Axonal (sensory) neuropathy) |
| Cerebellar ataxia | Clinical sign | HP:0001251 (Ataxia) |
| Dysarthria | Clinical sign | HP:0001260 (Dysarthria) |
| Sensorineural hearing loss | Clinical sign | HP:0000407 (Sensorineural hearing loss) |
| Cataracts | Clinical sign | HP:0000518 (Cataract) |
| Depression / psychiatric symptoms | Behavioral | HP:0000716 (Depression) |
| Hypogonadism | Clinical sign | HP:0000135 (Hypogonadism) |
| Parkinsonism | Clinical sign | HP:0001300 (Parkinsonism) |
| Mitral valve prolapse | Clinical sign | HP:0001634 (Mitral valve prolapse) |
| Cardiomyopathy | Clinical sign | HP:0001638 (Cardiomyopathy) |
| Gastrointestinal dysmotility | Clinical sign | HP:0002015 (Dysphagia) / HP:0002251 (Aganglionic megacolon) not exact — general GI dysmotility phenotype |
| Elevated CSF/serum lactate | Laboratory abnormality | HP:0002151 (Increased serum lactate) |
| Ragged red fibers on biopsy | Laboratory/histopathology | HP:0003200 (Ragged-red muscle fibers) |
| COX-negative (cytochrome c oxidase-deficient) fibers | Laboratory/histopathology | HP:0033279 or related mitochondrial myopathy histology term (verify via OAK) |

**Onset:** Classic PEOB1/arPEO manifests typically **after age 40** (late-onset category in the POLG age-of-onset classification), though earlier presentations occur, especially with more severe allele combinations that push the phenotype toward the juvenile/adult ataxia-neuropathy spectrum (12–40 years) or, rarely, earlier.

**Severity/progression:** Progressive and generally slow. In the Hikmat et al. 2020 cohort (*J Inherit Metab Dis*, PMID 32068908) analyzing 155 POLG-disease patients stratified by age of onset:
- **Late-onset disease (>40 y):** ptosis (95%), PEO (89%), ataxia (58%), peripheral neuropathy (65%) — **this group has the best overall prognosis** among the three age strata.
- **Juvenile/adult-onset (12–40 y):** ataxia (90%), peripheral neuropathy (84%), seizures (71%), stroke-like episodes (54%).
- **Early-onset (<12 y):** hepatopathy (87%), seizures (84%), feeding difficulties (84%), hypotonia (79%) — worst prognosis.
- Across the whole POLG spectrum: neurological (90%), ophthalmological (74%), and gastrointestinal (63%) features predominate overall.

Many patients initially diagnosed with "isolated" arPEO develop additional systemic/neurological features (ataxia, neuropathy) over years to decades — GeneReviews explicitly cautions that "progressive PEO without systemic involvement" as a static label requires caution, since longitudinal follow-up frequently reveals evolution toward the ataxia-neuropathy spectrum (MIRAS/SANDO).

**Frequency of PEO/ptosis in the general POLG-mutant population:** Ptosis in ~34% (51/149) and PEO in ~38% (56/146) of a broader all-ages POLG cohort, rising to >90% when restricted to the late-onset stratum — illustrating strong age-dependence of the phenotype-frequency relationship (cite Hikmat 2020 stratified data above).

**Quality of life impact:** Ptosis and ophthalmoparesis cause functional visual impairment (chin-up head posture to see under ptotic lids, diplopia less common than in myasthenia because weakness is typically symmetric), corneal exposure risk after ptosis surgery, and exercise intolerance limits activities of daily living; neuropathy and ataxia (when present) contribute to gait disability and falls risk. No disease-specific validated QOL instrument was identified in this search; general neuromuscular-disease QOL tools (SF-36, individualized) are used in the small POLG literature.

---

## 4. Genetic/Molecular Information

**Causal gene:** **POLG** (OMIM *174763; HGNC:9179; chromosome 15q26.1), encoding the 140-kDa catalytic α-subunit of the heterotrimeric mitochondrial DNA polymerase γ holoenzyme (Pol γA + a dimeric Pol γB accessory subunit encoded by **POLG2**). POLG is the sole DNA polymerase responsible for mtDNA replication and repair.

**Variant classification and type:**
- Pathogenic variants span **missense** (majority, especially the recurrent founder alleles), **nonsense**, **frameshift**, **splice-site**, and rare small in-frame indels; large deletions/duplications are uncommon (~5% detection by dosage analysis per GeneReviews).
- Structurally, POLG has three key functional domains: the N-terminal **exonuclease (proofreading) domain**, a **linker region** (contains the "spacer" and thumb subdomains, binds POLG2), and the C-terminal **polymerase domain**. Mutation location correlates loosely with mechanism and severity:
  - Exonuclease-domain mutations impair 3′→5′ proofreading, increasing point-mutation rate and promoting deletion formation.
  - Polymerase-domain mutations (e.g., the original Y955C) impair nucleotide incorporation/catalysis directly.
  - Linker-domain mutations (where A467T and W748S lie) can impair holoenzyme processivity/stability and POLG2 interaction.
- ACMG classification: A467T, W748S, and G848S are all classified **pathogenic** in ClinVar for POLG-related spectrum disorders (multiple submitters); many rarer POLG variants remain VUS pending functional/segregation data.

**Population/allele frequency:**
- p.Ala467Thr (c.1399G>A): gnomAD ~0.051% overall, ~0.098% in non-Finnish Europeans; the most common recessive pathogenic POLG allele (reported in at least 52 patients in aggregate case literature, 15 homozygous, 37 compound heterozygous, per ClinVar aggregation).
- These founder mutations are traced to ancient single European founder haplotypes (Rajakulendran et al., *Eur J Hum Genet* 2007/2016 lineage of studies), explaining their spread across Europe, Australia, New Zealand, and the US in populations of European descent.
- Carrier frequency for POLG pathogenic variants collectively approaches ~1% in some European-ancestry cohorts (relevant to ACMG carrier-screening panel design, per the 2024 gnomAD carrier-frequency estimation study, PMID 38459613).

**Somatic vs. germline:** PEOB1 pathogenic variants are **germline**. However, the disease mechanism itself operates through **secondary somatic mtDNA mutagenesis**: the germline nuclear POLG defect causes accumulation of somatic, clonally expanded mtDNA deletions in postmitotic tissues (especially skeletal and extraocular muscle) over the patient's lifetime — a form of accelerated somatic mitochondrial genome instability driven by a germline nuclear lesion.

**Functional consequence:** **Loss of function / hypomorphic** — reduced polymerase fidelity and/or reduced exonuclease proofreading activity, and/or reduced holoenzyme processivity, leading to (a) increased point mutation rate in mtDNA, (b) stalling of replication forks, and (c) accumulation of large-scale mtDNA deletions, ultimately (d) mtDNA depletion in severe cases. Nature Communications work (Basu et al., *Nat Commun* 2018, PMID 30089853 area) demonstrated that POLG's exonuclease activity is required for rapid degradation of linear mtDNA fragments generated during replication/repair; loss of this activity allows persistence of fragments and increases formation of deletions via non-homologous end joining or microhomology-mediated repair of stalled/broken replication intermediates.

**Modifier genes:** None firmly established for POLG-PEO specifically. POLG2 (the accessory subunit gene) causes a phenotypically overlapping but genetically and functionally distinct autosomal dominant PEO (PEOA5) and is mechanistically linked (holoenzyme partner) but is not a modifier of POLG1-driven PEOB1.

**Epigenetic information:** No POLG-PEO-specific DNA methylation, histone modification, or chromatin signature has been established in the literature surveyed; this is not a primary disease mechanism for a structural/catalytic enzyme defect of this kind. Not applicable/not identified.

**Chromosomal abnormalities:** Not applicable — PEOB1 is caused by point mutations/small indels in POLG, not by large chromosomal rearrangements. (Contrast with the mtDNA-deletion disorder Kearns-Sayre syndrome, which involves a single large mtDNA deletion, not nuclear chromosomal abnormality.)

---

## 5. Environmental Information

- **Environmental factors:** No toxin, radiation, or pollutant exposure is established as disease-causal for PEOB1 (it is monogenic). The dominant environmentally-modifiable risk is iatrogenic: **valproic acid exposure**, which can precipitate acute liver failure in POLG-mutant individuals (see Etiology/Gene-Environment above) — this is the most clinically actionable environmental factor for the entire POLG-disease spectrum, including arPEO.
- **Lifestyle factors:** Aerobic exercise has evidence (in the *Polg* "mutator" mouse model) of attenuating the progeroid/mitochondrial-dysfunction phenotype, and is used clinically as a supportive, not preventive, intervention in human mitochondrial myopathy generally; specific human PEOB1 exercise-outcome trial data were not identified in this search.
- **Infectious agents:** Not applicable — PEOB1 is not an infectious disease. Intercurrent infections/febrile illness may act as nonspecific metabolic stressors that unmask or worsen symptoms in POLG disease broadly (most documented in early-onset phenotypes), analogous to metabolic decompensation patterns in other mitochondrial diseases, but this is not a primary causal factor.

---

## 6. Mechanism / Pathophysiology

**Causal chain (initial trigger → clinical manifestation):**

1. **Molecular trigger:** Biallelic POLG pathogenic variants reduce the catalytic fidelity, proofreading (exonuclease) activity, and/or processivity of the Pol γ holoenzyme (GO:0006261, DNA-templated DNA replication; GO:0004674 or more precisely GO:0003887 DNA-directed DNA polymerase activity; GO:0008310, single-stranded DNA 3'-5' exodeoxyribonuclease activity for the exonuclease domain).
2. **Replication stalling and mtDNA instability:** Defective Pol γ causes replication fork stalling and generates persistent linear mtDNA fragments; because the exonuclease activity that normally degrades these fragments is impaired, they persist and are aberrantly repaired, generating **large-scale mtDNA deletions** (somatic, clonally expanded within individual cells/fibers over years). In some genotypes, replication failure instead causes **mtDNA depletion** (reduced copy number) rather than deletions — genotype-dependent branch point (relevant to the broader POLG spectrum, e.g., Alpers phenotype is depletion-dominant while adult PEO is deletion-dominant).
3. **Cellular consequence:** Clonal expansion of deleted mtDNA molecules within individual postmitotic muscle fibers over decades reaches a pathogenic threshold, causing **focal cytochrome c oxidase (Complex IV) deficiency** (mtDNA-encoded subunits of Complexes I, III, IV, and ATP synthase are lost from deleted genomes) — the classic "COX-negative, SDH-hyperreactive (ragged-red/ragged-blue) fiber" seen on histochemistry (GO cellular component: GO:0005739 mitochondrion; GO:0005743 mitochondrial inner membrane; relevant biological process GO:0006123, mitochondrial electron transport, cytochrome c to oxygen).
4. **Tissue-level consequence:** Oxidative phosphorylation (OXPHOS) failure in a mosaic pattern of affected fibers leads to a bioenergetic deficit that is most clinically apparent in tissues with high, continuous energy/mtDNA-turnover demand and long-lived postmitotic cells — **extraocular muscle** is exquisitely susceptible (thought to reflect its very high mitochondrial content, tonic/high-frequency firing pattern, and high mtDNA turnover), explaining the near-universal, early involvement of eyelid levator and extraocular muscles.
5. **Organism-level manifestation:** Progressive extraocular and skeletal myopathy (ptosis, ophthalmoparesis, exercise intolerance, proximal weakness), and — as the somatic mutation burden and clinical spectrum expand — peripheral nerve (axonal sensory neuropathy), cerebellar (ataxia), auditory (sensorineural hearing loss), lens (cataract), cardiac conduction/muscle, gonadal, and CNS (depression, parkinsonism) involvement in a subset of patients, reflecting variably penetrant multi-organ mosaic mtDNA deletion burden.

**Cell types involved:** Skeletal/extraocular myocyte (CL:0000192 smooth muscle cell is wrong — correct: CL:0000188 skeletal muscle myoblast / mature skeletal muscle fiber; extraocular myocyte has no distinct CL term but can be annotated as CL:0008002 skeletal muscle fiber, UBERON-localized to extraocular muscle), peripheral sensory neuron (CL:0000101 sensory neuron), Purkinje/cerebellar neurons (CL:0000121 Purkinje cell) in ataxia-affected patients, cochlear hair cells (CL:0000201/CL:0000202) in hearing-loss-affected patients, lens epithelial cells in cataract.

**Biochemical abnormality:** Impaired mitochondrial DNA polymerase (POLG) fidelity/processivity → downstream OXPHOS enzyme complex deficiency (particularly Complex I and IV, whose subunits are partly mtDNA-encoded) → impaired ATP synthesis and elevated lactate/pyruvate (common but not universal laboratory finding).

**Molecular/cellular process ontology suggestions:**
- GO:0006264 mitochondrial DNA replication
- GO:0032042 mitochondrial DNA metabolic process
- GO:0006281 DNA repair
- GO:0007005 mitochondrion organization
- GO:0006123 mitochondrial electron transport, cytochrome c to oxygen (Complex IV deficiency downstream effect)

**Omics/advanced technologies:** No large-scale transcriptomic, proteomic, or single-cell datasets specific to PEOB1 human tissue were identified in this search (reflecting rarity of biobanked tissue); most molecular characterization comes from muscle biopsy histochemistry/EM plus targeted biochemical/enzymatic assays of respiratory chain complexes, and from model-system (mouse, zebrafish, yeast) omics rather than direct human multi-omics profiling.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Extraocular muscles (levator palpebrae superioris, medial/lateral/superior/inferior recti, obliques) — UBERON:0002031 (extraocular muscle) / more general UBERON:0001772 (obturator... not relevant) — extraocular muscle is the primary UBERON target; specifically the levator palpebrae superioris (UBERON:0011343-adjacent structures should be verified via OAK).
- **Secondary:** Skeletal (limb-girdle/proximal) muscle (UBERON:0001134, skeletal muscle tissue); peripheral nervous system (peripheral nerve, UBERON:0000010); cerebellum (UBERON:0002037) in ataxia-affected patients; inner ear/cochlea (UBERON:0001846) in hearing loss; lens (UBERON:0000965) in cataract; heart (UBERON:0000948) in the subset with cardiomyopathy/mitral valve prolapse; gonads (testis UBERON:0000473 / ovary UBERON:0000992) in hypogonadism; gastrointestinal tract (UBERON:0005409) in dysmotility.
- **Body systems:** Neuromuscular (primary), nervous system (peripheral and central), special senses (visual — via extraocular myopathy and via cataract; auditory), cardiovascular, endocrine (gonadal), digestive.

**Tissue/cell level:** Skeletal/extraocular muscle fibers (mosaic COX-deficient, ragged-red fibers); peripheral sensory axons (axonal, not demyelinating, sensory neuropathy predominant); cerebellar Purkinje and granule cell circuitry.

**Subcellular level:** Mitochondria broadly (GO:0005739); specifically the mitochondrial matrix (GO:0005759, site of mtDNA and the replisome) and mitochondrial nucleoid (GO:0042645, mitochondrial nucleoid — the mtDNA-protein complex where Pol γ operates).

**Localization/laterality:** Ophthalmoplegia is characteristically **bilateral and symmetric** (a key distinguishing feature from myasthenia gravis, which is often asymmetric/fluctuating) — ptosis and ocular motility restriction affect both eyes in a diffuse, non-fatigable pattern.

---

## 8. Temporal Development

- **Onset:** Classic PEOB1 = **late-onset**, typically **after age 40 years** (GeneReviews). Earlier presentations (juvenile/adult-onset, 12–40 y) occur with more severe allele combinations and blend into the ataxia-neuropathy spectrum (MIRAS/SANDO); onset before age 12 is atypical for "pure" arPEO and instead characterizes the more severe POLG phenotypes (Alpers-Huttenlocher, MCHS).
- **Onset pattern:** Insidious/gradual — patients frequently do not notice the earliest, mild ptosis/ophthalmoparesis and are often diagnosed years after first symptoms, sometimes after being misdiagnosed with myasthenia gravis.
- **Progression:** Slowly progressive over years to decades. Ptosis and ophthalmoparesis worsen gradually; additional features (neuropathy, ataxia, hearing loss, cataract) may accrue over the disease course, particularly in patients followed longitudinally rather than assessed cross-sectionally.
- **Disease course:** Chronic, lifelong, non-remitting — no spontaneous remission is described. Unlike myasthenia gravis, there is no fluctuation or fatigability pattern.
- **Prognosis by age-of-onset stratum:** Late-onset (arPEO) disease has the **best prognosis** of the three POLG age strata; overall survival is far more favorable than early-onset (infantile hepatocerebral/Alpers) or juvenile/adult-onset (epilepsy/stroke-like-episode-dominant) POLG disease, where survival correlates strongly with age at onset of seizures/liver disease (median survival 0.7 years when epilepsy onset is in the first 3 years of life vs. median 18.0 years when epilepsy onset is after age 16; liver involvement is an independent poor-prognostic marker) (Hikmat et al., 2020; Cohen/Naviaux natural history studies).
- **Critical periods:** None specifically described for the adult-onset arPEO phenotype; by contrast, early recognition and valproate avoidance is critical at any age given the risk of fulminant hepatic failure if a POLG-mutant patient (of any phenotype) is inadvertently exposed.

---

## 9. Inheritance and Population

**Epidemiology:** PEO as a clinical syndrome overall has no precisely established population prevalence (Orphanet notes "prevalence unknown"). It is grouped among ultra-rare Mendelian mitochondrial disorders; a closely related entity (childhood-onset autosomal recessive myopathy with external ophthalmoplegia) is documented at <1/1,000,000. POLG-related disorders overall are estimated (from carrier-frequency modeling) to have a combined genetic prevalence on the order of ~1 in several thousand to ~1 in 10,000+ depending on population and specific phenotype, but PEOB1 specifically (the late-onset, comparatively mild recessive PEO subset) has no dedicated incidence/prevalence figure identified in this search.

**Inheritance pattern:** **Autosomal recessive** (biallelic POLG pathogenic variants required). Note that POLG is also independently a cause of **autosomal dominant** PEO (PEOA1, heterozygous variant sufficient) — the same gene causes phenotypically similar disease under different zygosity/allele-severity combinations, and recessive disease is generally more severe than the dominant form (per Orphanet/OMIM).
- **Penetrance:** Complete for biallelic pathogenic genotypes, though age-dependent (symptoms emerge progressively rather than being present from birth) — effectively full penetrance by later adulthood for the classic late-onset genotype combinations.
- **Expressivity:** Highly **variable**, both between and within families with the same genotype — even patients homozygous for the same founder allele can show a spectrum from isolated PEO to full ataxia-neuropathy-spectrum disease, indicating stochastic somatic mtDNA deletion accumulation contributes to phenotypic variability beyond genotype alone.
- **Anticipation:** Not described — POLG disease does not follow a repeat-expansion anticipation mechanism.
- **Germline mosaicism:** Not specifically documented for POLG in the literature surveyed.
- **Founder effects:** Strong — A467T, W748S, and G848S are all traceable European founder alleles (see Etiology/Genetic risk factors), giving PEOB1/POLG-spectrum disease its comparatively higher (for a "rare disease") carrier frequency in European-ancestry populations relative to many other ultra-rare recessive mitochondrial disorders.
- **Consanguinity:** As with any autosomal recessive disorder, consanguineous unions increase risk, particularly for rarer non-founder POLG alleles; not specifically quantified for PEOB1 in this search.
- **Carrier frequency:** Combined POLG pathogenic-variant carrier frequency approaches ~1% in some European-ancestry cohorts (dominated by A467T); this is unusually high for a recessive disease of this severity and is explained entirely by founder effects rather than heterozygote advantage.

**Population demographics:** Predominantly reported in populations of **European ancestry** (consistent with founder-allele geography — Europe, Australia, New Zealand, US populations of European descent per Rajakulendran et al.). No confirmed sex predilection (autosomal, so ~1:1 male:female expected and generally observed). Age distribution of affected/diagnosed individuals for the arPEO subtype skews toward middle-aged to older adults (40s onward) at symptom onset, with diagnosis often delayed further due to the insidious onset and diagnostic overlap with myasthenia gravis and other CPEO causes.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Serum/CSF lactate and pyruvate (may be elevated, not universally diagnostic).
- Creatine kinase (CK) — often normal or mildly elevated in mitochondrial myopathy (helps distinguish from primary myopathies with higher CK).

**Muscle biopsy (a cornerstone diagnostic test):**
- **Histochemistry:** Modified Gomori trichrome stain shows **ragged-red fibers (RRF)** (subsarcolemmal/intermyofibrillar mitochondrial proliferation); succinate dehydrogenase (SDH) staining shows corresponding "ragged-blue" fibers; combined **COX/SDH** staining reveals **COX-deficient fibers** (blue, SDH-positive but COX-negative) — the single most sensitive histochemical marker of mtDNA-deletion disease, often more sensitive than RRF alone.
- **Electron microscopy:** Paracrystalline mitochondrial inclusions, abnormal mitochondrial morphology/proliferation.
- **Molecular studies on muscle:** Southern blot or long-range PCR demonstrating **multiple mtDNA deletions** (distinguishing this "multiple deletion" disorder from Kearns-Sayre syndrome's single large deletion); quantitative PCR may show reduced mtDNA copy number in more severe genotypes.
- **Biochemical respiratory chain enzymology** on muscle homogenate: reduced Complex I and Complex IV activities characteristic (mtDNA-encoded subunit-dependent complexes).

**Imaging:** Not primary for diagnosis; orbital MRI may show extraocular muscle atrophy in advanced disease but is non-specific. Brain MRI may be used to evaluate cerebellar atrophy or white matter change in patients with ataxia/CNS features, again nonspecific.

**Electrophysiology:**
- Nerve conduction studies/EMG to characterize the sensory axonal peripheral neuropathy when present (reduced sensory nerve action potential amplitudes with relatively preserved conduction velocities, consistent with axonal loss).
- Repetitive nerve stimulation and single-fiber EMG are used to **exclude myasthenia gravis** (a key differential) — should be normal in PEOB1.
- Audiometry to characterize sensorineural hearing loss when present.

**Genetic testing (definitive diagnosis):**
- **First-line:** POLG sequence analysis (single-gene or targeted mitochondrial-disease gene panel), which detects the pathogenic variant in ~95% of cases; gene-targeted deletion/duplication analysis accounts for the remaining ~5%.
- **Broader approach:** Given genetic heterogeneity of multiple-mtDNA-deletion disorders (POLG, POLG2, TWNK, RRM2B, DGUOK, SLC25A4, OPA1, MGME1, RNASEH1, TK2, TOP3A, DNA2, and others), a **multigene mitochondrial-disease/PEO panel** or exome sequencing is often used clinically, particularly when the phenotype is atypical or POLG sequencing is negative.
- **Whole-exome/whole-genome sequencing** utility: increasingly used as first-tier or reflex testing given phenotypic overlap across the >20 known "multiple mtDNA deletion" genes; the specific yield data for PEOB1 alone were not separately quantified in this search.
- **Mitochondrial genome sequencing** of muscle (not blood — mtDNA deletion mosaicism is tissue-specific and typically not detectable in blood in adult-onset PEO) is essential to demonstrate the pathognomonic multiple-deletion picture, but does not identify the causal *nuclear* gene.
- **Chromosomal microarray/karyotype/FISH:** Not applicable/not indicated — PEOB1 is a nuclear point-mutation disorder, not a copy-number or cytogenetic disorder.

**Clinical diagnostic criteria:** No formal consensus scoring system specific to PEOB1 was identified; diagnosis rests on the clinical triad of (bilateral ptosis + symmetric ophthalmoparesis + exercise intolerance/myopathy), muscle biopsy evidence of mtDNA-deletion-type mitochondrial myopathy, demonstration of multiple mtDNA deletions in muscle, and confirmation of biallelic POLG pathogenic variants.

**Differential diagnosis:**
- **Ocular myasthenia gravis** — key distinguishing features: MG is typically fatigable/fluctuating and often asymmetric, with positive acetylcholine receptor or MuSK antibodies and abnormal repetitive nerve stimulation/single-fiber EMG; PEOB1 is static-progressive, symmetric, antibody-negative.
- **Kearns-Sayre syndrome** — single large mtDNA deletion (usually sporadic, not inherited in Mendelian fashion), onset before age 20, plus pigmentary retinopathy and cardiac conduction defects (triad required for KSS diagnosis) — PEOB1 lacks the KSS triad and shows *multiple* rather than single mtDNA deletions.
- **Oculopharyngeal muscular dystrophy (OPMD)** — caused by GCN-repeat expansion in PABPN1; presents with ptosis/dysphagia, distinguished by dysphagia prominence and specific molecular test.
- **Myotonic dystrophy type 1**, **congenital fibrosis of the extraocular muscles**, **thyroid eye disease/orbitopathy**, **chronic orbital myositis**, **abetalipoproteinemia**, **Refsum disease** — all in the broader CPEO differential.
- **Other genetic multiple-mtDNA-deletion disorders** (TWNK-recessive, RRM2B, DGUOK, SLC25A4, MGME1, RNASEH1, TK2, TOP3A, DNA2, OPA1) — clinically similar/indistinguishable without molecular testing; distinguished only by causal gene on sequencing.

**Screening:** No population-based newborn or general screening program exists for this adult-onset recessive disorder. **Carrier screening** (e.g., expanded carrier screening panels, ACMG-aligned) for POLG founder variants (notably A467T) is available and relevant given the ~1% carrier frequency in European-ancestry populations; **cascade testing** of at-risk relatives (siblings: 25% recurrence risk) and **genetic counseling** (including reproductive options such as prenatal or preimplantation genetic testing) are appropriate once a proband's biallelic genotype is established.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** The late-onset arPEO phenotype (PEOB1) carries the **best prognosis** within the POLG-disease spectrum; life expectancy is not dramatically shortened relative to the general population in isolated PEO without major systemic (hepatic, cardiac) involvement, though precise actuarial life-expectancy figures specific to PEOB1 were not identified in this search. This contrasts sharply with early-onset POLG phenotypes, where survival is markedly reduced and correlates with age at seizure onset and presence of liver disease (median survival as low as 0.7 years for epilepsy onset before age 3; liver involvement independently predicts worse survival) (Hikmat et al. 2020 and related natural-history literature).
- **Morbidity/function:** Chronic visual disability from ptosis/ophthalmoparesis (compensatory head-tilt, risk of exposure keratopathy, especially post-surgical); progressive proximal myopathy can impair mobility and activities of daily living; when ataxia/neuropathy develop, gait and fine-motor disability increase; hearing loss and cataract contribute to sensory disability in affected patients.
- **Complications:** Corneal exposure after ptosis surgery is a specific, well-documented iatrogenic complication in this population (due to poor Bell's phenomenon/orbicularis function accompanying the myopathy) — requires careful pre-op counseling and often conservative (under-)correction. Systemic complications (when present) include cardiac conduction disease/cardiomyopathy, endocrinopathy (hypogonadism), and GI dysmotility.
- **Recovery potential:** No disease-modifying therapy exists; the underlying mitochondrial myopathy and neuropathy are not reversible, though supportive interventions (ptosis surgery, physical therapy, hearing aids, cataract surgery) meaningfully improve function and quality of life for the specific affected organ system.
- **Prognostic factors:** Age at onset (later onset = better prognosis), genotype severity (allele combination — polymerase-domain/severe alleles trend toward worse, more systemic phenotype), presence/absence of liver involvement and early-onset seizures (poor prognostic markers, mainly relevant to the more severe ends of the POLG spectrum rather than classic arPEO), and degree of eventual systemic (ataxia-neuropathy-spectrum) evolution.
- **Prognostic biomarkers:** No validated molecular biomarker specific to PEOB1 progression was identified; general markers under study across POLG disease include serum/CSF lactate, GDF15/FGF21 (used more broadly as mitochondrial-disease biomarkers in other conditions), and mtDNA deletion burden on repeat muscle biopsy — the latter research-grade rather than clinically validated for prognosis specifically in this entity.

---

## 12. Treatment

**No disease-modifying or curative therapy exists.** Management is supportive, multidisciplinary, and focused on symptom management and monitoring for multisystem involvement, mirroring general mitochondrial-disease care.

**Pharmacotherapy:**
- **Coenzyme Q10 (ubiquinone/ubidecarenone)** supplementation (100–600 mg/day in small studies) — general mitochondrial-supportive therapy with reported (limited-evidence) benefits including reduced serum lactate/pyruvate and possible partial functional improvement; not POLG-PEO-specific, extrapolated from broader mitochondrial-disease "mitochondrial cocktail" practice. **NCIT term:** treatment_term NCIT:C15986 (Pharmacotherapy); therapeutic_agent CHEBI (ubidecarenone/coenzyme Q10, CHEBI:46245).
- Other components of the empiric "mitochondrial cocktail" (L-carnitine, riboflavin, alpha-lipoic acid, creatine) are used in general mitochondrial-myopathy practice with weak evidence; specific PEOB1 trial data were not identified.
- **Critical avoidance:** **Valproic acid / sodium divalproate are contraindicated** across the POLG spectrum, including PEOB1, due to hepatotoxicity risk — this should be flagged as a therapeutic *counter-indication* rather than a treatment.

**Pharmacogenomics:** The principal pharmacogenomic relevance is the valproate-hepatotoxicity gene-drug interaction described above; POLG genotype should be checked (or at minimum strongly suspected clinically) before initiating valproate in any patient with unexplained epilepsy, ataxia, or PEO-like features.

**Advanced therapeutics:** No approved gene therapy, cell therapy, RNA-based therapy, or targeted molecular therapy exists specifically for POLG-PEO at the time of this research; deoxynucleoside-substrate replacement therapies under investigation for other mtDNA-maintenance disorders (e.g., TK2 deficiency) are not established for POLG-PEO. No relevant ClinicalTrials.gov interventional trials specific to PEOB1 were identified in this search (searches for POLG-PEO-specific trials did not surface active NCT-registered studies beyond general mitochondrial-disease natural-history/biomarker studies).

**Surgical/interventional:**
- **Ptosis surgery** (levator resection, frontalis/brow suspension sling) — mainstay surgical intervention for functionally significant ptosis, but with meaningful risk of postoperative exposure keratopathy due to poor Bell's phenomenon/blink mechanics in this myopathic population; conservative under-correction is often favored. **NCIT:** procedure best captured under NCIT:C15329 (Surgical Procedure) or a more specific ophthalmic surgical term if available.
- **Strabismus surgery** is used more cautiously and less frequently than in comitant strabismus, given the progressive, restrictive nature of the myopathy.
- **Cataract surgery** for visually significant cataracts.
- **Cochlear implantation/hearing aids** for sensorineural hearing loss (device-based, not curative of the underlying disease).

**Supportive/rehabilitative:**
- Nonsurgical ptosis aids: **ptosis crutches/props**, **Fresnel prisms** for symptomatic misalignment/diplopia.
- **Scleral contact lenses** for ocular surface protection/rehabilitation in advanced disease.
- **Physical therapy** (resistance/aerobic exercise) to preserve muscle function, address proximal weakness, and (by analogy with mouse-model data showing exercise attenuates the *Polg* mutator progeroid phenotype) potentially support mitochondrial biogenesis, though direct human PEOB1 exercise-trial evidence was not identified.
- **Occupational therapy, speech-language therapy** (for dysarthria/dysphagia when present in the ataxia-neuropathy-spectrum-evolved phenotype).
- **Genetic counseling** (NCIT:C15240) for the patient and at-risk relatives given the 25%/50%/25% recessive recurrence-risk pattern.

**Treatment strategy/monitoring:** Regular multidisciplinary follow-up including periodic **liver function testing** (e.g., every 3 months per GeneReviews guidance, reflecting vigilance for hepatotoxic drug exposures and any evolving hepatic involvement), cardiac evaluation (ECG/echocardiogram) for conduction disease/cardiomyopathy surveillance, audiometry, ophthalmologic exam (cataract, corneal surface), and neurologic assessment for evolving ataxia/neuropathy — consistent with the "PEO-plus" surveillance philosophy given the phenotype's tendency to expand over time.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (this is a fixed germline genetic disease); the closest analog is **avoidance of valproate exposure** in genetically at-risk or POLG-confirmed individuals to prevent iatrogenic hepatic catastrophe — arguably the single most important "preventive" clinical action in this disease.
- **Secondary prevention:** Early diagnosis (via genetic testing once PEO is clinically suspected) enables anticipatory monitoring (liver, cardiac, audiologic, ophthalmologic) before complications become symptomatic/advanced.
- **Tertiary prevention:** Conservative surgical planning (ptosis under-correction) to prevent exposure keratopathy; proactive management of ataxia/neuropathy-related fall risk; cardiac monitoring to catch conduction disease before syncope/sudden events.
- **Genetic screening:**
  - **Carrier screening** for POLG founder pathogenic variants (notably A467T) is commercially available (e.g., expanded carrier screening panels referenced by Myriad/Foresight) and increasingly incorporated given the relatively high (~1%) carrier frequency in European-ancestry populations.
  - **Prenatal testing/preimplantation genetic testing (PGT-M)** is an option for couples where both partners are known carriers or where a proband's biallelic genotype has been characterized.
  - **Cascade family testing** of siblings/relatives of an affected proband, given 25% recurrence risk for full siblings.
- **Genetic counseling:** Central to prevention strategy — informing reproductive decision-making, clarifying that arPEO is generally the mildest end of the POLG spectrum (important reassurance context) while noting variable expressivity means the same genotype can theoretically manifest more severely in a given individual.
- **Public health/behavioral/immunization/prophylaxis:** Not applicable — this is not an infectious, environmentally-driven, or vaccine-preventable disease.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal disease caused by POLG mutations was identified in this search (searches for OMIA POLG entries were not directly performed but no evidence of natural veterinary POLG-PEO disease surfaced in the broader literature reviewed). This appears to be a human-specific documented clinical entity at present, though POLG orthologs exist broadly across mammals (used experimentally, see Model Organisms below).
- **Orthologous gene:** Mouse *Polg* (MGI:1338062; NCBI Gene ortholog), highly conserved catalytic and exonuclease domains — the basis for the mouse model described below.
- **Comparative biology:** The core biochemical mechanism (Pol γ proofreading/catalytic function in mtDNA replication) is deeply evolutionarily conserved from yeast (MIP1, the yeast Pol γ ortholog) through zebrafish (polg1/polg2) to mammals, which is precisely why yeast, zebrafish, and mouse models (below) are informative surrogates for human POLG disease mechanism, even though naturally occurring animal disease has not been documented.
- **Zoonotic potential/transmission:** Not applicable — non-infectious, non-transmissible monogenic disease.

---

## 15. Model Organisms

**Yeast:** *Saccharomyces cerevisiae* MIP1 (Pol γ ortholog) mutants have been used to model POLG catalytic and exonuclease domain mutations, informative for basic replication-fidelity mechanism studies (per the 2025 *Cell Death & Disease* review "Model organisms in POLG-related disorders: insights from yeast to multicellular systems").

**Zebrafish:**
- A stable CRISPR/Cas9-generated **polg2 knockout zebrafish line** (allele *polg2^ia304^*) recapitulates human POLG-disorder phenotypes: homozygous mutants show slower development, decreased viability, remarkable **mtDNA depletion**, altered mitochondrial network/dynamics, and reduced mitochondrial respiration (PMC11032366). While this specific model targets *polg2* (the accessory-subunit ortholog) rather than *polg1* directly, it is used as a platform for **drug-treatment screening** relevant to the broader POLG-disorder mechanism.
- Zebrafish models more broadly are highlighted as useful for probing the **neurological manifestations** of POLG disease (encephalopathy, epilepsy, ataxia) given their amenability to behavioral and imaging assays.

**Mouse — the "mtDNA mutator" model (most extensively characterized):**
- The classic **Polg^D257A/D257A "mutator" mouse** carries a proofreading-domain (exonuclease-dead) knock-in mutation, causing an ~2,500-fold increase in mtDNA point-mutation rate and marked linear-fragment/deletion accumulation (an 11-kb linear mtDNA fragment corresponding to most of the mtDNA major arc has been specifically characterized, mechanistically linking loss of exonuclease-mediated fragment degradation to deletion formation — directly relevant to the human PEOB1 deletion mechanism).
- **Phenotype recapitulation:** This model reproduces a **systemic premature-aging (progeroid) phenotype** — accelerated sarcopenia, hearing loss, osteoporosis, hair graying/alopecia, thymic involution, testicular atrophy, cardiac hypertrophy, anemia, weight loss, and markedly shortened lifespan — overlapping substantially with several "PEO-plus" features seen in human POLG disease (hearing loss, cardiomyopathy, hypogonadism), though the mouse model's dominant aging-phenotype framing is broader than isolated human arPEO.
- **Mechanistic insight from the model:** Muscle from mutator mice shows increased mitochondrial fission (elevated Fis1) and heightened autophagy, proposed to contribute to the sarcopenic phenotype — a plausible parallel to human myopathic muscle wasting.
- **Intervention data:** Endurance exercise is the only reported intervention shown to attenuate the progeroid phenotype and extend healthspan/lifespan in this model — informing (by extrapolation, not direct trial) the rationale for exercise as supportive therapy in human patients.
- **Newer, refined mouse models (2025):** A study titled "Modelling POLG mutations in mice unravels a critical role of POLγB in regulating phenotypic severity" (*Nat Commun* 2025) specifically dissects how the POLG2 (Pol γB) accessory subunit modulates phenotypic severity of POLG catalytic mutations — directly relevant to understanding genotype-phenotype variability in human disease. A separate 2025 bioRxiv-reported "inducible mtDNA mutator mouse model" adds temporal/spatial control, addressing the limitation that constitutive mutator mice can show embryonic lethality or phenotypes that are difficult to dissect tissue-specifically.

**Model limitations:** Existing constitutive POLG mouse mutants can present either embryonic lethality (very severe alleles) or comparatively mild/non-specific phenotypes, limiting fidelity to the specific adult-onset, tissue-restricted (extraocular-muscle-predominant) human PEOB1 phenotype and limiting utility for high-throughput drug screening — a limitation explicitly motivating development of the newer inducible and zebrafish models.

**Research applications:** These models collectively enable study of (a) the exonuclease-fragment-degradation mechanism of deletion formation, (b) POLG2/Pol γB modulation of severity, (c) tissue-specific bioenergetic failure and its downstream cellular consequences (mitochondrial fission/autophagy), and (d) candidate interventions (exercise; pharmacologic screening in zebrafish).

**Resources:** MGI (Mouse Genome Informatics) for *Polg* knock-in/flox alleles (e.g., the C57BL/6JCya-Polg^em1flox^ conditional model cataloged commercially); ZFIN for zebrafish *polg1/polg2* alleles.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Domain | Suggested terms |
|---|---|
| Disease | OMIM:258450; ORPHA:254886; MONDO (verify exact PEOB1-specific term via OLS) |
| Gene | HGNC:9179 (POLG), lowercase `hgnc:9179` per repo convention |
| Phenotypes (HP) | HP:0000508 Ptosis; HP:0000590 Ophthalmoplegia; HP:0000602 Ophthalmoparesis; HP:0003546 Exercise intolerance; HP:0001324 Muscle weakness; HP:0003202 Skeletal muscle atrophy; HP:0007141 Axonal sensory neuropathy; HP:0001251 Ataxia; HP:0001260 Dysarthria; HP:0000407 Sensorineural hearing loss; HP:0000518 Cataract; HP:0001634 Mitral valve prolapse; HP:0001638 Cardiomyopathy; HP:0002151 Increased serum lactate; HP:0003200 Ragged-red muscle fibers |
| Biological processes (GO) | GO:0006264 mitochondrial DNA replication; GO:0032042 mitochondrial DNA metabolic process; GO:0006281 DNA repair; GO:0006123 mitochondrial electron transport, cytochrome c to oxygen |
| Molecular function (GO) | GO:0003887 DNA-directed DNA polymerase activity; GO:0008310 single-stranded DNA 3'-5' exodeoxyribonuclease activity |
| Cell types (CL) | Skeletal/extraocular muscle fiber; CL:0000101 sensory neuron; CL:0000121 Purkinje cell (ataxia-affected patients) |
| Anatomy (UBERON) | UBERON:0002031 extraocular muscle; UBERON:0001134 skeletal muscle tissue; UBERON:0002037 cerebellum; UBERON:0001846 cochlea; UBERON:0000965 lens |
| Treatment (NCIT) | NCIT:C15986 Pharmacotherapy (CoQ10, avoid valproate); NCIT:C15329 Surgical Procedure (ptosis repair); NCIT:C15240 Genetic Counseling; NCIT:C15315 Rehabilitation |
| Chemicals (CHEBI) | CHEBI:46245 ubidecarenone (coenzyme Q10); note valproate/valproic acid as a **contraindicated** agent, not a treatment |

---

## Notes on Evidence Gaps

- Precise population **prevalence/incidence** figures specific to PEOB1 (as opposed to POLG-disease overall, or CPEO as a clinical umbrella) were **not found** — flag as "prevalence unknown" per Orphanet, consistent with rare-disease reporting limits.
- No dedicated **QOL instrument data**, **omics (transcriptomic/proteomic) human-tissue datasets**, or **active interventional clinical trials** specific to PEOB1 were identified in this search — likely reflects genuine absence of such studies for this specific rare recessive subtype rather than a search limitation, though a targeted ClinicalTrials.gov/GEO query would be a reasonable follow-up before concluding definitively.
- Exact PMIDs for several foundational papers (Van Goethem et al. 2001 Nat Genet; the Hikmat et al. 2020 JIMD cohort, PMID 32068908; Basu et al. 2018 Nat Commun on exonuclease/fragment degradation) should be independently re-verified against PubMed/cached abstracts before use as curated evidence snippets, per standard dismech verification SOP — this report should be treated as a **lead-generation document**, not pre-verified evidence.

**Sources:**
- [OMIM #258450 — PEOB1](https://omim.org/entry/258450)
- [OMIM *174763 — POLG](https://omim.org/entry/174763)
- [OMIM #616479 — PEOB2 (RNASEH1)](https://omim.org/entry/616479)
- [OMIM #617070 — PEOB4 (DGUOK)](https://www.omim.org/entry/617070)
- [Orphanet — Autosomal recessive PEO (ORPHA:254886)](https://www.orpha.net/en/disease/detail/254886)
- [GeneReviews — POLG-Related Disorders (NBK26471)](https://www.ncbi.nlm.nih.gov/books/NBK26471/)
- [MalaCards — PEOB1](https://www.malacards.org/card/progressive_external_ophthalmoplegia_with_mitochondrial_dna_deletions_autosomal_recessive_1)
- [MedlinePlus — Progressive external ophthalmoplegia](https://medlineplus.gov/genetics/condition/progressive-external-ophthalmoplegia/)
- [MedlinePlus — POLG gene](https://medlineplus.gov/download/genetics/gene/polg.pdf)
- [Nature Genetics — Van Goethem et al., Mutation of POLG associated with PEO](https://www.nature.com/articles/ng0701_211)
- [Nature Communications — POLG exonuclease degrades linear DNA fragments precluding deletions](https://www.nature.com/articles/s41467-018-04895-1)
- [Nature Communications — POLγB regulates phenotypic severity in mouse POLG models (2025)](https://www.nature.com/articles/s41467-025-60059-y)
- [Cell Death & Disease — Model organisms in POLG-related disorders](https://www.nature.com/articles/s41419-025-08366-6)
- [PMC — Zebrafish polg2 knockout recapitulates POLG-disorders](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11032366/)
- [Journal of Inherited Metabolic Disease — Hikmat et al. 2020, simplifying POLG clinical classification](https://onlinelibrary.wiley.com/doi/full/10.1002/jimd.12211)
- [Genetics in Medicine — natural history of early-onset POLG disease](https://www.nature.com/articles/gim201735)
- [ClinVar — POLG c.1399G>A (p.Ala467Thr)](https://www.ncbi.nlm.nih.gov/clinvar/variation/13496/)
- [European Journal of Human Genetics — Abundance of POLG mutations from single ancient founders](https://www.nature.com/articles/5201831)
- [PubMed — Estimation of carrier frequencies via gnomAD for carrier screening](https://pubmed.ncbi.nlm.nih.gov/38459613/)
- [PMC — RNASEH1 mutations and PEO with multiple mtDNA deletions](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6588129/)
- [MedLink Neurology — Chronic progressive external ophthalmoplegia](https://www.medlink.com/articles/progressive-external-ophthalmoplegia)
- [Medscape — CPEO Treatment & Management](https://emedicine.medscape.com/article/1215103-treatment)
- [PMC — Treatment of ptosis in chronic progressive external ophthalmoplegia](https://pmc.ncbi.nlm.nih.gov/articles/PMC1041145/)