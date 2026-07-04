---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-01T02:06:46.631712'
end_time: '2026-07-01T02:12:36.578553'
duration_seconds: 349.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autoimmune Gastritis
  mondo_id: ''
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 26
  total_cost_usd: 2.4650833
  session_id: 5c58c42e-aa53-5307-a59b-32bd2414492b
  stop_reason: end_turn
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoimmune Gastritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Gastritis** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Autoimmune Gastritis (AIG) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Autoimmune gastritis (AIG) — also termed Type A gastritis, autoimmune metaplastic atrophic gastritis (AMAG), or chronic autoimmune atrophic gastritis — is a chronic, organ-specific autoimmune disease of the stomach in which autoreactive CD4+ T cells and autoantibodies destroy the acid-secreting parietal cells and intrinsic-factor-producing cells of the oxyntic (corpus/fundic) mucosa, sparing the antrum ([Lenti et al., 2019, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8414617/); [Ku PMC10378041](https://pmc.ncbi.nlm.nih.gov/articles/PMC10378041/)). Progressive parietal cell loss produces achlorhydria, hypergastrinemia, oxyntic atrophy, intestinal/pseudopyloric metaplasia, and — via loss of intrinsic factor — vitamin B12 malabsorption culminating in pernicious anemia. Compensatory hypergastrinemia drives enterochromaffin-like (ECL) cell hyperplasia and predisposes to type 1 gastric neuroendocrine tumors (gNETs) as well as gastric adenocarcinoma ([Frontiers 2026](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1878128/full); [Naples review, PMC12563516](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/)).

**Identifiers.**
- No single dedicated MONDO/OMIM/Orphanet term captures "autoimmune gastritis" as its own top-level rare-disease entity; instead the entity is most often indexed through its end-organ consequence, **pernicious anemia**: **Orphanet ORPHA:120** — "Pernicious anemia," explicitly flagged by Orphanet as **"NON RARE IN EUROPE"** and listed with synonyms "Addison-Biermer anemia," "Biermer disease," "acquired pernicious anemia," "juvenile onset pernicious anemia" (Orphanet, ORPHA:120).
- Juvenile/early-onset pernicious anemia forms are catalogued in **OMIM** under the 261xxx congenital vitamin-B12-malabsorption/pernicious-anemia series (e.g., an entry around **OMIM:261100**); because these OMIM entries emphasize monogenic juvenile pernicious anemia rather than the adult autoimmune-mediated form, they should be treated as adjacent/partially-overlapping identifiers rather than a direct MONDO-equivalent for adult AIG — this should be independently verified against the live OMIM/MONDO record before being used as a KB `mappings` value.
- **MeSH**: "Gastritis, Atrophic" (D005704) is the closest controlled MeSH heading; "Anemia, Pernicious" (D000752) covers the hematologic sequela.
- **ICD-10/11**: ICD-10 K29.4 "Chronic atrophic gastritis"; ICD-11 DA42.2/related autoimmune-gastritis coding under digestive-system chronic gastritis; pernicious anemia is coded separately (ICD-10 D51.0).
- **Synonyms**: Type A gastritis, autoimmune metaplastic atrophic gastritis (AMAG), autoimmune corpus-restricted (chronic) atrophic gastritis, autoimmune atrophic gastritis (AAG).

**Data source type.** Most of the literature synthesized below is aggregated disease-level evidence (cohort studies, systematic/position-paper reviews, GWAS meta-analyses of population biobanks — Estonian Biobank, UK Biobank, FinnGen) rather than individual EHR-level curation; a few large single/multi-institution retrospective cohorts (e.g., Italian, Japanese, Chinese series) are cited explicitly below.

---

## 2. Etiology

**Primary causal mechanism.** AIG is caused by a breakdown of self-tolerance to the gastric H⁺/K⁺-ATPase proton pump (the α- and β-subunits) on parietal cells and, in a subset, to intrinsic factor. Autoreactive CD4+ T cells (Th1, and Th17) recognize H⁺/K⁺-ATPase-derived peptides, secrete IFN-γ/IL-17, and mediate parietal cell apoptosis via Fas-FasL and perforin/granzyme B pathways; B cells produce complement-fixing anti-parietal-cell antibodies (PCA) and anti-intrinsic-factor antibodies (IFA) ([Unraveling the Mysteries of AIG, PMC11899966](https://pmc.ncbi.nlm.nih.gov/articles/PMC11899966/); [Immunological mechanisms of AIG, PMC12909420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12909420/)).

**Genetic risk factors.**
- A 2021 genome-wide association meta-analysis (2,166 pernicious-anemia cases vs. 659,516 European controls pooled from the Estonian Biobank, UK Biobank, and FinnGen) identified five genome-wide-significant risk loci ([Lahtela et al. 2021, *Nature Communications*, PMC8213695](https://pmc.ncbi.nlm.nih.gov/articles/PMC8213695/); PMID not directly retrieved but paper is Nat Commun 2021;12:3811):
  | Locus | Lead SNP | Gene | P-value | OR (95% CI) |
  |---|---|---|---|---|
  | 1p13.2 | rs6679677 | **PTPN22** | 1.91×10⁻²⁴ | 1.63 (1.48–1.79) |
  | 2p16.1 | rs12616502 | **PNPT1** | 3.14×10⁻⁸ | 1.70 (1.41–2.05) |
  | 6p21.32 | rs28414666 | **HLA-DQB1** | 1.40×10⁻¹⁶ | 1.38 (1.28–1.49) |
  | 10p15.1 | rs2476491 | **IL2RA** | 1.90×10⁻⁸ | 1.22 (1.14–1.30) |
  | 21q22.3 | rs74203920 | **AIRE** (missense) | 2.33×10⁻⁹ | 1.83 (1.50–2.29) |

  Direct quote: *"We conduct a genome-wide association study meta-analysis in 2166 cases and 659,516 European controls from population-based biobanks and identify genome-wide significant signals."* The PTPN22 lead SNP (rs6679677) is in strong LD with the well-known autoimmunity nonsynonymous variant rs2476601 in exon 12 of PTPN22, also implicated in rheumatoid arthritis, SLE, type 1 diabetes, vitiligo, and autoimmune thyroid disease.
- **HLA class II** susceptibility alleles **HLA-DRB1\*03 and HLA-DRB1\*04** are consistently reported as increasing risk, and the HLA-DR15 haplotype has been implicated by GWAS as well ([Frontiers 2026](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1878128/full); medRxiv preprint on HLA-DR15).
- **AIRE** missense variants link AIG/pernicious anemia to the broader monogenic autoimmune polyendocrine syndrome type 1 (APS-1/APECED) spectrum, where recurrent AIRE loss-of-function alleles (R139X, R257X, W78R, C322fsX372, T16M, R203X, A21V in an Italian APS-1 cohort, n=158) predispose to AIG among other organ-specific autoimmunities.
- Candidate/proton-pump genes: **ATP4A**, **ATP4B** (the antigen itself), plus **SLC26A7**, **SLC26A9**, **SLC4A2** (acid-base transporters) and **BACH2** (a broad autoimmunity susceptibility transcription factor) have emerging GWAS/candidate-gene support ([Kalkan et al. 2023, PMC10378041](https://pmc.ncbi.nlm.nih.gov/articles/PMC10378041/); PMID: 37504250).

**Environmental/infectious risk factors.**
- ***Helicobacter pylori*** is the leading environmental trigger hypothesis via **molecular mimicry**: the β-subunit of *H. pylori* urease shares high sequence homology with the β-subunit of gastric H⁺/K⁺-ATPase, generating cross-reactive T- and B-cell responses in genetically susceptible hosts ([MDPI review PMID unlisted](https://www.mdpi.com/1422-0067/26/16/7737)). Paradoxically, the relationship between active *H. pylori* infection and established AIG is complex/inverse in some cohorts — chronic *H. pylori* infection may itself trigger AIG onset, but established AIG is often *H. pylori*-negative at diagnosis, and some evidence suggests *H. pylori*-driven Th2 responses may suppress ongoing AIG in certain contexts.
- **Murine roseolovirus** neonatal infection triggers CD4+ T-cell-dependent gastritis in mouse models, suggesting viral triggers merit further study in humans.
- **Smoking**: not established as a direct AIG-specific trigger but is a well-documented independent and interactive risk factor for gastric atrophy, intestinal metaplasia, dysplasia, and gastric cancer, relevant to AIG's malignant-transformation risk.
- **Age and sex**: female sex and age >50–60 are strong epidemiological risk correlates (see Section 9).
- **Family history / other autoimmunity**: family clustering with autoimmune thyroid disease, type 1 diabetes, vitiligo strongly increases risk (see Section 9).

**Protective factors.** No validated protective genetic variant is established specifically for AIG; broadly, non-risk HLA haplotypes and, per emerging microbiome data, an intact butyrate-producing gut microbiota (e.g., *Faecalibacterium prausnitzii*) that sustains regulatory T cell (Treg) differentiation via short-chain fatty acids is hypothesized to be protective against Th17-driven progression ([Frontiers 2026](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1878128/full)).

**Gene-environment interaction.** The PTPN22/HLA-DQB1/AIRE genetic background is proposed to lower the threshold for *H. pylori*-triggered molecular mimicry and epitope spreading to become self-perpetuating autoimmunity — i.e., infection acts as an environmental "second hit" in a genetically primed host, though this remains a mechanistic hypothesis rather than a proven causal chain in humans (a `KNOWLEDGE_GAP`/`HUMAN_MODEL_MISMATCH` candidate for KB curation).

---

## 3. Phenotypes

Most AIG is asymptomatic/subclinical for years; phenotypes span GI, hematologic, neurologic, and — indirectly — endocrine/dermatologic domains via associated autoimmunity.

| Phenotype | Type | Onset/course | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Dyspepsia / early satiety / postprandial fullness | Symptom | Adult, chronic/fluctuating | ~47–60% (more common in young women, non-smokers) | HP:0002018 (Dyspepsia) |
| Iron-deficiency anemia | Laboratory abnormality | Often precedes B12 deficiency by years | ~20–50% | HP:0011870 (Iron deficiency anemia) |
| Vitamin B12 deficiency / megaloblastic (pernicious) anemia | Laboratory/clinical sign | Insidious, adult (often 60s), progressive if untreated | Defining late feature | HP:0008163 (Decreased vitamin B12), HP:0001887 (Megaloblastic anemia) |
| Achlorhydria / hypochlorhydria | Laboratory abnormality | Progressive with atrophy | Near-universal in advanced disease | HP:0003204 (Achlorhydria, if modeled) |
| Hypergastrinemia | Laboratory abnormality | Compensatory, progressive | Near-universal in advanced disease | HP:0500152 (Abnormal circulating gastrin concentration) or similar |
| Gastric mucosal atrophy (oxyntic) | Histopathologic sign | Chronic, progressive (early→florid→end-stage over ~3 years per prospective cohorts) | Defining lesion | HP:0002608 (Atrophic gastritis, if present) / MONDO cross-ref |
| Glossitis | Physical sign | Secondary to B12/iron deficiency | Variable | HP:0000216 (Glossitis) |
| Peripheral neuropathy / paresthesia | Symptom/sign | Subacute, progressive if untreated | Occurs with B12 deficiency | HP:0003676 (Progressive; use with HP:0003390 Paresthesia) |
| Subacute combined degeneration of the spinal cord | Clinical sign | Late, progressive, potentially irreversible | Uncommon but serious | HP:0002314 (Subacute combined degeneration) |
| Ataxia | Sign | Progressive, B12-deficiency-related | Uncommon | HP:0001251 (Ataxia) |
| Type 1 gastric neuroendocrine tumor (ECL-cell carcinoid) | Neoplastic complication | Late, indolent | ~2.8–11% cumulative (up to ~37% in some Chinese cohorts using sensitive detection) | HP:0100633 (Neuroendocrine neoplasm) |
| Gastric adenocarcinoma | Neoplastic complication | Late, age >60 highest risk | ~0.1–0.5%/year incidence; 3–5x general population risk | HP:0012126 (Gastric adenocarcinoma, if available) / MONDO |
| Infertility / recurrent miscarriage | Reproductive phenotype | Adult women | Reported in case series (n=168) | HP:0000789 (Infertility) |
| Weight loss | Symptom | Variable | Minority | HP:0001824 (Weight loss) |
| Diarrhea | Symptom | Variable | Minority, malabsorption-related | HP:0002014 (Diarrhea) |

**Age of onset**: Classically adult-onset (median age at diagnosis 61–67 years, range 18–94), but pediatric AIG is increasingly recognized — pediatric prevalence ~0.15% among children undergoing gastric biopsy, mean diagnosis age 10.9 years, with striking **68.2% female predominance** and **59.1%** presenting with a concurrent extragastric autoimmune disorder ([Kalkan et al., PMC10378041](https://pmc.ncbi.nlm.nih.gov/articles/PMC10378041/)).

**Severity/progression**: A prospective cohort of 270 patients found histopathology in *all* patients progressed over time (generally within 3 years) from mild to severe/end-stage, with **no observed spontaneous regression** — supporting a monotonically progressive natural history once autoimmunity is established ([PMC8414617](https://pmc.ncbi.nlm.nih.gov/articles/PMC8414617/)). A separate prospective study reported an annual progression rate of 10.9% from "potential" (seropositive, histologically normal) to "overt" AAG (PMID: 38050966).

**Quality of life**: Neurological B12-deficiency sequelae, if diagnosis is delayed, are described as "inexorably progressive," while early diagnosis and lifelong B12 replacement largely normalizes hematologic and neurologic function; dyspeptic symptoms in early disease modestly affect quality of life but are frequently under-recognized because most patients are asymptomatic.

---

## 4. Genetic/Molecular Information

AIG is a **complex/polygenic** autoimmune disease, not a single-gene Mendelian disorder (contrast with monogenic APS-1/AIRE, which is a Mendelian cause of *syndromic* AIG).

- **Causal antigen genes** (autoantigen targets, not classically "causal mutations"): **ATP4A** (HGNC:816, H⁺/K⁺-ATPase α-subunit) and **ATP4B** (HGNC:817, β-subunit) encode the gastric proton pump targeted by PCA; intrinsic factor is encoded by **GIF** (HGNC:4256).
- **Susceptibility loci** (GWAS-confirmed, see Section 2): **PTPN22** (HGNC:9646), **PNPT1** (HGNC:23349), **HLA-DQB1** (HGNC:4944), **IL2RA** (HGNC:6008), **AIRE** (HGNC:360).
- **Variant classification**: The PTPN22 signal tags the well-characterized rs2476601 (R620W) gain-of-function/loss-of-inhibitory-function missense variant recurrent across autoimmune disease (not AIG-specific, pleiotropic risk allele — not a Mendelian pathogenic variant in the ACMG sense). The AIRE signal (rs74203920) is annotated as missense in the GWAS meta-analysis; distinct, more severe AIRE loss-of-function alleles (R139X, W78R, R257X, C322fsX372, etc.) cause monogenic APS-1/APECED, of which AIG is one of several organ-specific autoimmune components.
- **Allele frequency**: The PTPN22 rs2476601 minor allele frequency is well characterized in European populations (~10–12% in gnomAD/1000 Genomes; enriched across multiple autoimmune GWAS) — population-level data should be pulled from gnomAD directly for KB curation rather than assumed here.
- **Somatic vs. germline**: All described genetic risk variants (PTPN22, HLA-DQB1, IL2RA, AIRE, PNPT1) are **germline** susceptibility alleles; there is no described somatic-mutation mechanism for AIG itself (somatic events become relevant only in the neoplastic complications — gNETs and gastric adenocarcinoma — as separate downstream processes).
- **Functional consequences**: PTPN22 R620W disrupts a phosphatase involved in T-cell receptor signaling attenuation, lowering the threshold for autoreactive T-cell activation (loss of inhibitory function); AIRE variants impair thymic promiscuous gene expression and central tolerance induction, permitting escape of autoreactive T-cell clones (loss of function).
- **Modifier genes**: BACH2 (broad Treg/Th differentiation modifier across autoimmune diseases) and SLC26A7/SLC26A9/SLC4A2 (ion transporters co-expressed with the H⁺/K⁺-ATPase, potentially modifying antigen exposure/epithelial stress) are proposed modifiers rather than primary drivers.
- **Epigenetics**: Emerging but sparse data — aberrant DNA methylation patterns and altered microRNA profiles (**miR-21** elevated, **miR-223** reduced in gastric mucosa) are reported in AIG and associated with progression toward dysplasia/carcinoma, but comprehensive methylome/histone studies specific to AIG are lacking (a documented knowledge gap).
- **Chromosomal abnormalities**: None described as causal for typical AIG; trisomy 21 (Down syndrome) carries a recognized comorbid association with autoimmune (including gastric) disease and pernicious anemia (case reports), reflecting broader autoimmune susceptibility rather than a specific gastric mechanism.

---

## 5. Environmental Information

- **Infectious trigger**: *Helicobacter pylori* — proposed via molecular mimicry between its urease β-subunit and the gastric H⁺/K⁺-ATPase β-subunit; also implicated via chronic inflammation, polyclonal lymphocyte activation, epitope spreading, and bystander activation ([MDPI 2025](https://www.mdpi.com/1422-0067/26/16/7737)). Murine roseolovirus neonatal infection is a model-organism-demonstrated viral trigger (mouse), of uncertain human relevance.
- **Lifestyle**: Smoking is an established independent/synergistic risk factor for gastric mucosal atrophy, intestinal metaplasia, and gastric cancer generally, relevant to AIG's malignant potential, though not shown to specifically initiate the autoimmune process. Diet/alcohol have not been robustly linked to AIG initiation specifically (as opposed to gastric cancer risk broadly).
- **Microbiome**: Hypochlorhydria from parietal cell loss reshapes the gastric niche, permitting overgrowth of non-*Helicobacter* taxa (*Streptococcus*, *Lactobacillus*, *Veillonella*); dysbiosis-associated loss of short-chain-fatty-acid-producing species (e.g., *Faecalibacterium prausnitzii*) is hypothesized to impair Treg differentiation and worsen Th17-driven inflammation, and *Bacillus cereus* has been reported enriched specifically in AIG-related gastric cancer.
- **Occupational/toxin exposures**: No specific validated occupational or toxin exposure is established for AIG.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Genetic susceptibility** (HLA-DRB1\*03/\*04, HLA-DQB1, PTPN22 R620W, AIRE variants, IL2RA, PNPT1) lowers central/peripheral tolerance thresholds →
2. **Antigen exposure/trigger** — possible *H. pylori* molecular mimicry of gastric H⁺/K⁺-ATPase β-subunit, or other unidentified triggers →
3. **Autoreactive CD4+ T-cell activation**: dendritic cells process H⁺/K⁺-ATPase peptides and, via IL-12/IL-23, drive differentiation into **Th1** (IFN-γ, TNF-α) and **Th17** (IL-17A/E/F, IL-21, IL-22) effector subsets; innate lymphoid cells (ILC3) reinforce IL-17/IL-22 output →
4. **Cytotoxic effector mechanisms against parietal cells**: (a) Fas upregulation on parietal cells + FasL-expressing T/NK cells assembling the death-inducing signaling complex (DISC) → caspase-8 activation; (b) perforin/granzyme B cytotoxicity from NK cells (~20% of gastric mucosal lymphocytes) and cytotoxic T cells; (c) B-cell-derived **anti-parietal cell antibodies (PCA)** targeting H⁺/K⁺-ATPase α/β-subunits and **anti-intrinsic factor antibodies (IFA)**, mediating complement-dependent cytotoxicity and antibody-dependent cellular cytotoxicity →
5. **Epithelial stress amplification**: inflammatory cytokines (IL-1β, TNF-α) trigger ER stress/unfolded protein response via the **PERK–eIF2α–ATF4–CHOP axis**, downregulating Bcl-2 and activating Bax, driving mitochondrial-pathway apoptosis; impaired autophagic flux further sensitizes parietal cells to apoptosis ([PMC12563516](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/)) →
6. **Parietal cell loss → oxyntic (corpus/fundic) mucosal atrophy**, with tissue remodeling sustained by gastric myofibroblasts and eosinophil infiltration; pseudopyloric and intestinal metaplasia develop as replacement phenotypes →
7. **Loss of gastric acid (achlorhydria)** removes the normal negative-feedback on antral G cells → **chronic hypergastrinemia** →
8. **Gastrin–CCK2R signaling on ECL cells**: activates **ERK/MAPK** (Ras-Raf-MEK-ERK → cyclin D1, c-Myc), **PI3K/Akt** (→ Bad inactivation, mTOR survival signaling), and **STAT3** (→ Bcl-xL, VEGF) cascades, driving **ECL cell hyperplasia**, which can progress to dysplasia and **type 1 gastric neuroendocrine tumors** →
9. **Loss of intrinsic factor** (from parietal/IF-producing cell destruction, compounded by anti-IF antibodies blocking IF-B12 binding or the IF-B12-cubilin receptor interaction in the terminal ileum) → **vitamin B12 malabsorption** → megaloblastic **pernicious anemia** and, if prolonged, **subacute combined degeneration** of the spinal cord and peripheral neuropathy →
10. **Chronic atrophic/metaplastic mucosa** is an independent field of increased **gastric adenocarcinoma** risk (3–5× general population), compounding the ECL/gNET pathway.

**Cell types involved** (Cell Ontology candidates): parietal cell (**CL:0000160**), chief/zymogenic cell (**CL:0000155**), enterochromaffin-like cell (**CL:0000502** or closest ECL-cell term), gastric mucous neck/foveolar cell, gastric G cell (gastrin-producing enteroendocrine cell), Th1 CD4+ T cell (**CL:0000545**-derived Th1 subset), Th17 CD4+ T cell, cytotoxic CD8+ T cell (**CL:0000625**), NK cell (**CL:0000623**), plasma/B cell (**CL:0000786**), dendritic cell (**CL:0000451**), ILC3 (**CL:0001071**), gastric myofibroblast, eosinophil (**CL:0000771**).

**Biological processes** (GO candidates): T-cell mediated cytotoxicity (**GO:0001913**), Fas signaling pathway (**GO:0036337**/apoptotic signaling via death domain receptors, **GO:0008625**), complement-dependent cytotoxicity, endoplasmic reticulum unfolded protein response (**GO:0030968**), regulation of apoptotic process (**GO:0042981**), autophagy (**GO:0006914**), positive regulation of interleukin-17 production (**GO:0032740**), cellular response to interferon-gamma (**GO:0071346**), response to gastrin (if modeled), MAPK cascade (**GO:0000165**), PI3K signaling (**GO:0014065**), regulation of vitamin B12 transport/intrinsic factor binding.

**Molecular profiling**: microRNA dysregulation (miR-21↑, miR-223↓) is reported in gastric mucosa; transcriptomic/proteomic/metabolomic single-cell or spatial datasets specific to AIG are not yet well established in public repositories (GEO/HCA) — an area flagged as an evidence gap in recent reviews.

**Single-cell/advanced technologies**: No mature single-cell atlas of human AIG gastric mucosa was identified in this search; this is an emerging-technology gap consistent with the "Human studies validating ER stress and autophagy dysfunction remain limited" caveat explicitly raised in the cellular-crosstalk review ([PMC12563516](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/)).

---

## 7. Anatomical Structures Affected

- **Primary organ**: Stomach, specifically the **oxyntic mucosa of the corpus/fundus** (UBERON:0001162 body of stomach / UBERON:0001156 gastric fundus), sparing the antrum (contrast with *H. pylori*-associated multifocal/antral-predominant gastritis).
- **Secondary organ involvement**: 
  - Hematologic system (bone marrow megaloblastic changes from B12 deficiency)
  - Nervous system (peripheral nerves, dorsal columns/lateral corticospinal tracts of the spinal cord — subacute combined degeneration)
  - Small intestine (terminal ileum, site of intrinsic-factor-mediated B12 absorption, secondarily affected functionally though not structurally)
  - Reproductive system (infertility/miscarriage reported)
  - Thyroid, pancreatic islets, skin/melanocytes (via associated autoimmune comorbidities, not direct AIG pathology)
- **Body systems**: digestive, hematologic/immune, nervous, and (via comorbidity) endocrine and integumentary systems.
- **Tissue/cell level**: gastric oxyntic (fundic) glands — parietal cells, chief cells, ECL cells, mucous neck cells; lamina propria immune infiltrate (T cells, B/plasma cells, eosinophils, mast cells); antral G cells (indirectly, via hypergastrinemia feedback, though G-cell hyperplasia itself can occur).
- **Subcellular level**: mitochondria (apoptosis via Bax/Bcl-2, cytochrome c release), endoplasmic reticulum (UPR/PERK-eIF2α-ATF4-CHOP stress pathway), apical canalicular membrane of parietal cells (H⁺/K⁺-ATPase proton pump localization — GO Cellular Component: apical plasma membrane, **GO:0016324**).
- **Localization/laterality**: Gastric involvement is typically diffuse within the corpus/fundus (not lateralized); neurological B12-deficiency manifestations can be bilateral and symmetric (peripheral neuropathy, subacute combined degeneration).

---

## 8. Temporal Development

- **Onset**: Predominantly adult-onset, insidious; median diagnosis age 61–67 years (range 18–94). A distinct **pediatric-onset** phenotype exists (mean age 10.9 years, prevalence ~0.15% among biopsied children), often with strong concurrent extragastric autoimmunity.
- **Onset pattern**: Chronic/insidious rather than acute; disease may be "silent" for years before serologic (PCA/IFA) positivity converts to histologic and clinical disease.
- **Progression/staging** (histopathologic 3–5 stage models):
  - **Stage 0 / "potential" AIG**: seropositive (PCA/IFA+) but histologically normal or minimally abnormal.
  - **Early phase**: mild-to-moderate oxyntic atrophy, CD4+ lymphocytic infiltration, pseudopyloric metaplasia; parietal cells may show compensatory hypertrophy.
  - **Florid phase**: moderate-to-severe oxyntic gland atrophy, dense lymphoplasmacytic inflammation, ECL cell hyperplasia, intestinal metaplasia.
  - **End-stage**: severe gland loss, extensive intestinal metaplasia/dysplasia, ECL hyperplasia, paradoxically reduced active inflammation.
- **Progression rate**: A prospective study of "potential" to "overt" AAG reported an annual progression rate of **10.9%**; a separate 270-patient prospective cohort found histology progressed in essentially all patients within ~3 years with **no spontaneous regression** observed.
- **Disease course pattern**: Monotonically progressive (not relapsing-remitting) at the histologic/immunologic level, though symptom burden can fluctuate.
- **Duration**: Chronic, lifelong once established; the underlying autoimmune/atrophic process does not resolve spontaneously, though its hematologic and neurologic *consequences* (B12/iron deficiency) are effectively controlled with lifelong replacement therapy.
- **Critical periods**: The seropositive "potential" phase represents a clinically important window for early detection before irreversible gland atrophy and before neurologic B12-deficiency sequelae become established; the pediatric-onset subgroup's long-term natural history remains largely unstudied (explicit knowledge gap).

---

## 9. Inheritance and Population

**Epidemiology.**
- **Prevalence**: Estimated ~0.1–2% in the general population, rising to **2–3% in adults over 60**. Endoscopic-biopsy cohort studies: USA (1988–2008, n=41,245 biopsies) ~1.1%; Japan (asymptomatic screening) ~0.49%; European multicenter gastritis cohorts ~2% among biopsied gastritis cases; lower prevalence reported in a large Chinese cohort (n=97,341) ([Lenti et al., PMC8414617](https://pmc.ncbi.nlm.nih.gov/articles/PMC8414617/)).
- **Ethnic/geographic variation**: Non-white Hispanic populations show higher prevalence (**~2.7%**) versus ~1% in white, Asian, and African-American populations in some U.S. cohort data; earlier age of onset reported in non-white groups in some studies.
- **Sex ratio**: Consistent **female predominance**, roughly **2–3:1 (F:M)** across adult cohorts; the pediatric cohort shows an even more pronounced **68.2% female** skew.
- **Age distribution**: Bimodal-ish — a small pediatric-onset group (mean ~10.9 years) and the dominant adult/elderly-onset group (median 61–67 years).

**Inheritance pattern**: AIG is a **complex/polygenic (multifactorial)** trait, not Mendelian, driven by additive/interacting common variants (PTPN22, HLA-DQB1, IL2RA, PNPT1) plus environmental triggers. The exception is syndromic AIG occurring as one manifestation of **monogenic autosomal recessive APS-1/APECED** (biallelic **AIRE** loss-of-function), which follows classic Mendelian AR inheritance with high penetrance for the syndrome overall but variable penetrance/expressivity for the gastric component specifically.

**Penetrance/expressivity**: For the common polygenic form, individual risk-allele penetrance is low (as expected for GWAS-identified common variants, ORs 1.2–1.8); for AIRE-driven APS-1, the AIRE genotype has high penetrance for autoimmune polyendocrinopathy overall, but expressivity across specific component diseases (including AIG) is variable between AIRE-mutation carriers.

**Genetic anticipation / mosaicism / founder effects**: Not described for AIG's common polygenic form. AIRE founder mutations are known in specific populations (e.g., Finnish, Iranian Jewish, Sardinian founder alleles for APS-1), relevant to any AIG occurring in that syndromic context, but this is a population feature of APS-1 rather than of idiopathic AIG.

**Consanguinity**: Relevant only to the rare AR-AIRE/APS-1 syndromic route, not to typical polygenic AIG.

**Carrier frequency**: Not meaningfully defined for a polygenic trait; APS-1/AIRE carrier frequencies are population-specific and available via GeneReviews/GTR for that distinct monogenic condition.

**Associated autoimmune comorbidity (polyautoimmunity)**:
- **Autoimmune thyroid disease**: reported concurrently in **36–44%** of AIG patients in some series (other sources cite ~2.8% in specific cohorts — figures vary substantially by study design/population, underscoring heterogeneity).
- **Type 1 diabetes**: AIG/pernicious anemia risk in T1D patients is **~3–5× the general population**; conversely, among T1D patients, 5–10% have AIG/pernicious anemia, 15–30% have autoimmune thyroid disease, 2–10% have vitiligo, and up to one-third develop a broader autoimmune polyglandular syndrome.
- **Vitiligo, rheumatoid arthritis, psoriasis, autoimmune hepatitis, myasthenia gravis, Sjögren syndrome, autoimmune hemolytic anemia** are also reported comorbid associations, consistent with a "multiple autoimmune syndrome" (MAS) pattern (Autoimmune Institute review; PMC6146093 editorial).
- Case reports also document AIG co-occurring with primary biliary cholangitis, non-nodal mantle cell lymphoma progression, and Down syndrome-associated pernicious anemia.

---

## 10. Diagnostics

**Serologic tests** (first-line, "serological biopsy" panel):
- **Anti-parietal cell antibodies (PCA)**: sensitivity ~81–90%, specificity ~88–90% (varies by assay/cohort).
- **Anti-intrinsic factor antibodies (IFA)**: lower sensitivity (~27–32%) but very high specificity (95–100%).
- **Newer ATP4A/ATP4B luciferase immunoprecipitation assays**: ATP4A sensitivity ~75%/specificity ~88%; ATP4B sensitivity ~77%/specificity ~88% — proposed as improved, more standardized alternatives to conventional immunofluorescence PCA testing ([Lenti/Massironi review, PMC11354099](https://pmc.ncbi.nlm.nih.gov/articles/PMC11354099/)).
- **Serum pepsinogen I (PGI)** and **PGI/PGII ratio**: low PGI (<70 µg/L, cutoffs vary by study) or low ratio (<2.1, <1.8, <3 depending on study/population) indicates oxyntic atrophy; sensitivity/specificity in the 67–100% range depending on cutoff and cohort.
- **Serum gastrin-17**: elevated (>355 pg/mL in one study; various pmol/L cutoffs elsewhere) reflects loss of acid-mediated negative feedback and is a reliable marker of oxyntic atrophy; combined PGI/II + gastrin-17 panels reach ~88.9% accuracy for identifying NET-bearing patients.
- **Commercial panel**: GastroPanel® (PGI, PGII, gastrin-17, *H. pylori* IgG) used for non-invasive screening.
- **Chromogranin A**: elevated with ECL hyperplasia/NET development; used to monitor NET burden and treatment response (e.g., to netazepide/somatostatin analogs).
- **Novel immune marker**: antral CD8+/CD4+ T-lymphocyte ratio >4.0 (sensitivity 71.4%, specificity 93.3%) proposed to distinguish AIG from *H. pylori*-associated gastritis histologically.

**Endoscopy/histology (gold standard)**:
- Endoscopic findings: sticky adherent mucus, scattered whitish protrusions, remnant oxyntic mucosal islands, patchy redness, hyperplastic polyps (in a 245-patient Japanese cohort).
- Biopsy protocol: Updated Sydney System — minimum 5 biopsies (2 antrum, 1 incisura, 2 corpus) to allow topographic (corpus vs. antrum) comparison, essential to distinguish corpus-restricted AIG atrophy from antral-predominant *H. pylori* gastritis.
- **OLGA/OLGIM staging**: combines topography with atrophy (OLGA) or intestinal metaplasia (OLGIM) severity into stages 0–IV; stage 0–II = lower cancer risk (surveillance every 3–5 years), stage III–IV = higher risk (surveillance every 1–2 years).
- Histologic 3–5 stage model of disease progression as described in Section 8.

**Differential diagnosis**: *H. pylori*-associated (multifocal/antral-predominant) chronic gastritis; NSAID/chemical (reactive) gastropathy; other causes of iron/B12 deficiency (celiac disease, dietary deficiency, small intestinal bacterial overgrowth, pancreatic exocrine insufficiency, terminal ileal disease/resection); lymphocytic gastritis; Zollinger-Ellison syndrome (also causes hypergastrinemia, but via a gastrinoma rather than achlorhydria-driven feedback loss — distinguished by gastric pH/secretin stimulation testing).

**Genetic testing**: No first-line clinical genetic test is used for typical polygenic AIG (unlike Mendelian disorders); AIRE sequencing is indicated only when syndromic APS-1/APECED is clinically suspected (mucocutaneous candidiasis, hypoparathyroidism, adrenal insufficiency plus AIG).

**Screening**: No population-wide screening program exists for sporadic AIG; targeted serologic screening (PCA/IFA, pepsinogens) is reasonable in patients with unexplained iron or B12 deficiency, first-degree relatives of AIG patients, or patients with another organ-specific autoimmune disease (thyroid, T1D, vitiligo) given comorbidity rates.

---

## 11. Outcome/Prognosis

- **Mortality/survival**: AIG itself is not directly fatal; prognosis is driven by (a) adequacy of B12/iron replacement and (b) surveillance for malignant complications. With appropriate lifelong vitamin replacement, hematologic and most neurologic manifestations are controlled or reversed if caught early.
- **Neurologic morbidity**: Untreated/delayed B12 deficiency produces "inexorably progressive" neurologic injury (peripheral neuropathy → subacute combined degeneration → ataxia/weakness), which can become irreversible if replacement is delayed — underscoring the importance of early diagnosis.
- **Neoplastic risk/complications**:
  - **Type 1 gastric neuroendocrine tumors (gNETs)**: cumulative incidence ~2.8%/person-year in some cohorts, ~4.7% at 2 years in others; up to 10–37% prevalence in various case series depending on detection sensitivity and population; generally indolent — tumors <1 cm and Ki-67 ≤2% managed with surveillance; favorable prognosis overall, with <10% metastasis rate for lesions <2 cm.
  - **Gastric adenocarcinoma**: risk estimated at **3–5× (some sources: 7×)** the general population; annual incidence ~0.1–0.5%/person-year; risk factors within the AIG population include age >60 (HR ~4.7), intestinal metaplasia without pseudopyloric metaplasia (HR ~4.3), and pernicious anemia (HR ~4.3). Notably, recent prospective cohorts restricted to *H. pylori*-negative AAG patients reported **no gastric adenocarcinoma cases**, suggesting that much of the historically reported cancer risk in AIG populations may be attributable to prior/concurrent *H. pylori* infection rather than the autoimmune process alone — an important nuance for risk stratification and a candidate `HUMAN_MODEL_MISMATCH`/knowledge-gap note.
- **Prognostic factors**: age at diagnosis, degree of atrophy/OLGA-OLGIM stage, *H. pylori* status (past or present), presence of dysplasia, and B12-deficiency neurologic involvement at diagnosis.
- **Quality of life**: Largely normalized with treatment in early-detected disease; unaddressed B12 deficiency and neuroendocrine tumor development are the main drivers of long-term morbidity.

---

## 12. Treatment

**Pharmacotherapy (replacement/supportive)**:
- **Vitamin B12**: lifelong **intramuscular** (or high-dose sublingual/oral) cyanocobalamin/hydroxocobalamin supplementation — first-line, definitive management of the pernicious-anemia component. MAXO candidate: pharmacotherapy generically, or a dietary/vitamin-supplementation MAXO term if available; NCIT:C15986 (Pharmacotherapy) with a CHEBI therapeutic_agent (e.g., CHEBI cyanocobalamin) is the dismech-pattern annotation.
- **Iron**: oral iron (often with vitamin C to enhance absorption in the achlorhydric stomach) or, if oral therapy fails (due to hypochlorhydria-impaired absorption), **intravenous iron infusion**. Iron status should be checked in all AIG patients regardless of overt anemia, given corpus-predominant atrophy's impact on non-heme iron absorption.
- **Acid-suppressive therapy caution**: **PPIs are generally NOT recommended** in AIG, since patients already have hypochlorhydria/achlorhydria and PPIs would exacerbate hypergastrinemia and ECL hyperplasia risk; **H2-receptor antagonists** (e.g., famotidine) are preferred if short-term acid-related symptom control is needed, and PPIs are reserved for short-term severe reflux esophagitis only.

**Management of neoplastic complications**:
- **Type 1 gNETs**: small (<1 cm, Ki-67 ≤2%) lesions managed by endoscopic surveillance; larger (>1 cm) or higher-grade lesions undergo endoscopic resection (surveillance every 6–12 months post-resection per ESGE guidelines); refractory/recurrent cases may proceed to antrectomy (removes the gastrin-secreting antral mucosa, normalizing gastrin levels) or medical gastrin-pathway blockade.
- **Netazepide** (a gastrin/CCK2-receptor antagonist): reduces chromogranin A and can shrink/eradicate type 1 gNETs in patients with autoimmune chronic atrophic gastritis, though continuous treatment is needed to prevent recurrence ([PMC5306499](https://pmc.ncbi.nlm.nih.gov/articles/PMC5306499/)).
- **Somatostatin analogs** (e.g., octreotide, lanreotide): reported response rates ~25–100% for type 1 NETs across small studies.
- **Gastric adenocarcinoma**: managed per standard gastric cancer oncologic pathways (endoscopic resection for early lesions, surgery/chemotherapy for advanced disease) — not AIG-specific.

**Endoscopic surveillance**: Regular high-definition upper endoscopy with systematic biopsy (per Sydney System protocol), frequency tailored to OLGA/OLGIM risk stage — every **3–5 years** for low-risk (stage 0–II) and every **1–2 years** for high-risk (stage III–IV) or NET-bearing patients.

**Emerging/experimental**:
- **Immunomodulatory therapy**: limited evidence suggests corticosteroids or other immunosuppressants might help in early, highly inflammatory disease stages, though no targeted immunotherapy is currently approved.
- **Th17/IL-17-axis-targeted biologics** (e.g., anti-IL-17 monoclonal antibodies like secukinumab/ixekizumab, approved in psoriasis/spondyloarthropathy) are mechanistically plausible given the Th17 contribution to AIG pathogenesis, but are not yet studied/approved specifically for AIG (an explicit translational gap).
- **Microbiota-targeted approaches**: probiotic supplementation (e.g., *Faecalibacterium prausnitzii*) or fecal microbiota transplantation are proposed research directions to restore Treg-supportive short-chain-fatty-acid production, but remain preclinical/conceptual for AIG.
- **AI-assisted endoscopy**: deep-learning-based image analysis reported to achieve diagnostic accuracy for atrophic changes comparable to or exceeding experienced endoscopists — an emerging diagnostic-support tool rather than a treatment.

**Treatment algorithm summary**: (1) confirm diagnosis serologically + histologically → (2) lifelong B12 replacement (parenteral) + iron repletion as needed → (3) OLGA/OLGIM-stratified endoscopic surveillance → (4) targeted intervention (endoscopic resection, antrectomy, netazepide/somatostatin analog) if type 1 gNET or dysplasia/adenocarcinoma develops → (5) screen for/monitor associated autoimmune comorbidities (thyroid, T1D, vitiligo).

---

## 13. Prevention

- **Primary prevention**: No established primary prevention exists for the autoimmune initiation of AIG itself (unlike infectious or vaccine-preventable disease); *H. pylori* eradication in infected individuals is standard gastritis/gastric-cancer prevention practice generally, though its specific effect on preventing AIG onset is unproven and the relationship is complex (see Section 5).
- **Secondary prevention (early detection)**: Targeted serologic screening (PCA/IFA, pepsinogen, gastrin-17) in high-risk groups — first-degree relatives of AIG patients, patients with unexplained iron/B12 deficiency, and patients with another organ-specific autoimmune disease (autoimmune thyroiditis, type 1 diabetes, vitiligo) — enables detection at the "potential"/seropositive stage before irreversible atrophy or neurologic injury.
- **Tertiary prevention**: Structured endoscopic surveillance (OLGA/OLGIM-stratified) prevents progression from dysplasia to invasive gastric adenocarcinoma and enables early resection of type 1 gNETs before they enlarge or (rarely) metastasize; lifelong B12/iron replacement prevents irreversible hematologic and neurologic complications.
- **Genetic counseling**: Relevant primarily in the rare monogenic APS-1/AIRE-driven syndromic context (recurrence risk counseling for autosomal recessive AIRE variants), not for typical sporadic polygenic AIG.
- **Public health**: No population-level public health intervention (vaccination, sanitation) is applicable; the closest public-health-relevant lever is *H. pylori* screening/eradication programs in high-gastric-cancer-incidence regions, which have ancillary relevance to the atrophic-gastritis-to-cancer pathway generally.

---

## 14. Other Species / Natural Disease

- **Taxonomy**: Naturally occurring/experimentally induced autoimmune gastritis has been most extensively studied in **mouse** (*Mus musculus*, NCBITaxon:10090).
- **Natural/spontaneous disease in animals**: **C3H/He mice** develop **spontaneous autoimmune gastritis** without experimental manipulation, serving as a natural-disease model for gastric autoimmunity (PMID: 9777963).
- **Veterinary relevance**: No major companion-animal or livestock natural-disease correlate of human AIG was identified in this search; the mouse models above are laboratory rather than veterinary-clinical observations.
- **Orthologous genes**: Mouse *Atp4a*/*Atp4b* (orthologs of human ATP4A/ATP4B) are the principal autoantigens in murine models, directly paralleling the human disease target.
- **Comparative pathology**: Murine neonatal-thymectomy-induced gastritis is histologically and immunologically similar to human pernicious-anemia-associated atrophic gastritis — chronic mononuclear infiltrate, destruction of parietal and zymogenic (chief) cells, and autoantibodies to H⁺/K⁺-ATPase α- and β-subunits (PMID: 1648525; PMID: 9272282).
- **Zoonotic potential**: Not applicable — AIG is a non-infectious autoimmune process, not a transmissible disease.

---

## 15. Model Organisms

- **Neonatal thymectomy mouse model**: ~60% of neonatally thymectomized **BALB/c** mice spontaneously develop autoimmune gastritis, driven by depletion of CD4+CD25+ regulatory T cells; histologically and serologically similar to human pernicious-anemia-associated gastritis, with autoantibodies against H⁺/K⁺-ATPase α- and β-subunits ([Clinical and Experimental Immunology](https://academic.oup.com/cei/article/89/1/63/6488118); PMID: 1648525, PMID: 9272282). The thymic (rather than purely gastric) expression pattern of the α-subunit in BALB/c thymus is proposed to explain the dominant pathogenic role of the β-subunit.
- **Spontaneous C3H/He mouse model**: A genetically distinct strain (C3H/He) develops autoimmune gastritis spontaneously without thymectomy, offering a complementary "new mouse model for gastric autoimmunity" (PMID: 9777963).
- **Immunization-induced model**: Immunization of mice with purified gastric H⁺/K⁺-ATPase induces a **reversible** autoimmune gastritis, useful for dissecting antigen-specific initiation and potential resolution/tolerance mechanisms (PMC1363986).
- **TxA23 TCR-transgenic / polyclonal effector T-cell transfer models**: Adoptive transfer of H⁺/K⁺-ATPase-specific effector T cells (including Th1, Th2, and Th17 subsets) produces autoimmune gastritis with distinct histopathologic patterns and differential susceptibility to suppression by regulatory T cells depending on the transferred effector subset (PMC2561289) — this system has been particularly informative for dissecting how Th1 vs. Th17-driven disease differs mechanistically and in Treg-responsiveness, directly informing the Th17/Treg-axis therapeutic hypotheses discussed in Section 12.
- **Model characteristics/limitations**: Mouse models robustly recapitulate the core autoantigen (H⁺/K⁺-ATPase), the T-cell-mediated destructive mechanism, and downstream atrophic/metaplastic histology, but do not fully model the human-specific downstream consequences — chronic ECL hyperplasia progressing to type 1 gastric NETs and long-term gastric adenocarcinoma risk are less consistently reproduced in short-lived rodent models, and human-specific comorbid polyautoimmunity (thyroid, T1D, vitiligo clustering) is not intrinsically modeled by single-antigen mouse systems. This human-model translational gap (mouse captures initiation/parietal-cell-destruction biology well, but not the full human neoplastic-complication trajectory) is a strong candidate for a `HUMAN_MODEL_MISMATCH` discussion in a dismech KB entry.
- **Research applications**: These models have been used to define the H⁺/K⁺-ATPase α/β-subunit antigenic hierarchy, the CD4+CD25+ Treg-dependent tolerance mechanism, and differential Th1/Th2/Th17 pathogenicity and Treg-suppressibility — directly supporting current human therapeutic hypotheses around Treg restoration and Th17-cytokine blockade.
- **Resources**: MGI (Mouse Genome Informatics) for *Atp4a*/*Atp4b* strain and allele records; no dedicated ZFIN/FlyBase/WormBase model of autoimmune gastritis was identified (unsurprising, as gastric parietal cell autoimmunity is a mammalian-immune-system-dependent phenomenon without a clear invertebrate correlate).

---

## Summary of Key Ontology Term Suggestions for KB Curation

- **Genes (HGNC)**: ATP4A (hgnc:816), ATP4B (hgnc:817), GIF (hgnc:4256), PTPN22 (hgnc:9646), PNPT1 (hgnc:23349), HLA-DQB1 (hgnc:4944), IL2RA (hgnc:6008), AIRE (hgnc:360), BACH2 (hgnc:939)
- **Cell types (CL)**: parietal cell, chief cell, enterochromaffin-like cell, gastric G cell, Th1/Th17 CD4+ T cell, NK cell, plasma cell, dendritic cell
- **Biological processes (GO)**: T-cell mediated cytotoxicity, Fas-mediated apoptosis, ER stress/UPR, autophagy, IL-17 production, MAPK cascade, PI3K-Akt signaling
- **Phenotypes (HP)**: megaloblastic anemia, iron deficiency anemia, subacute combined degeneration, ataxia, glossitis, dyspepsia, neuroendocrine neoplasm
- **Anatomy (UBERON)**: body of stomach/gastric fundus (oxyntic mucosa), antrum, spinal cord dorsal columns
- **Chemicals (CHEBI)**: cyanocobalamin/hydroxocobalamin, ferrous sulfate, netazepide
- **Treatments (MAXO/NCIT)**: NCIT:C15986 (Pharmacotherapy) + therapeutic_agent for B12/iron; endoscopic resection/surveillance (MAXO surgical/procedural terms)

**Important caveat for curation**: I was unable to definitively confirm a dedicated MONDO/OMIM identifier specifically for "autoimmune gastritis" as distinct from pernicious anemia (ORPHA:120) during this search — recommend an explicit OAK/MONDO-browser lookup (`runoak -i sqlite:obo:mondo search "autoimmune gastritis"`) before committing any `mappings:` block to a disorder YAML, per the project's anti-hallucination ontology-verification SOP.

---

## Sources

- [Frontiers | Autoimmune gastritis: a comprehensive review of pathophysiology, risk stratification, and management (2026)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1878128/full)
- [Update in Molecular Aspects and Diagnosis of Autoimmune Gastritis — PMC10378041](https://pmc.ncbi.nlm.nih.gov/articles/PMC10378041/) (PMID: 37504250)
- [Unraveling the Mysteries of Autoimmune Gastritis — PMC11899966](https://pmc.ncbi.nlm.nih.gov/articles/PMC11899966/) (PMID: 39632655)
- [The Autoimmune Gastritis Puzzle: Emerging Cellular Crosstalk and Molecular Pathways Driving Parietal Cell Loss and ECL Cell Hyperplasia — PMC12563516](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/)
- [Immunological mechanisms of autoimmune gastritis — PMC12909420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12909420/)
- [Pro- and anti-inflammatory cytokines: the hidden keys to autoimmune gastritis therapy — PMC11347309](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11347309/)
- [Improving the Diagnosis of Autoimmune Gastritis: From Parietal Cell Antibodies to H+/K+ ATPase Antibodies — PMC11354099](https://pmc.ncbi.nlm.nih.gov/articles/PMC11354099/)
- [Genome-wide association study identifies five risk loci for pernicious anemia — PMC8213695 / Nature Communications 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8213695/)
- [Autoimmune gastritis, with or without pernicious anemia: epidemiology, risk factors, and clinical management — PMC8414617](https://pmc.ncbi.nlm.nih.gov/articles/PMC8414617/)
- [Autoimmune Atrophic Gastritis: A Clinical Review — PMC11010983](https://pmc.ncbi.nlm.nih.gov/articles/PMC11010983/) (PMID: 28072728 cited within; PMID: 38050966 cited within)
- [Autoimmune Gastritis and Helicobacter pylori Infection: Molecular Mechanisms of Relationship — MDPI](https://www.mdpi.com/1422-0067/26/16/7737)
- [Netazepide, a gastrin/cholecystokinin‑2 receptor antagonist, can eradicate gastric neuroendocrine tumours — PMC5306499](https://pmc.ncbi.nlm.nih.gov/articles/PMC5306499/)
- [Autoimmune Gastritis: Update and New Perspectives in Therapeutic Management — Current Treatment Options in Gastroenterology](https://link.springer.com/article/10.1007/s11938-023-00406-4)
- [The morphologic spectrum of gastric type 1 enterochromaffin-like cell neuroendocrine tumors — PMC10121960](https://pmc.ncbi.nlm.nih.gov/articles/PMC10121960/)
- [Progression From Antral G-Cell Hyperplasia to Gastric Neuroendocrine Tumor in a Patient With Autoimmune Gastritis — PMC8386912](https://pmc.ncbi.nlm.nih.gov/articles/PMC8386912/) (PMID: 34476276)
- [Orphanet: Pernicious anemia (ORPHA:120)](https://www.orpha.net/en/disease)
- [OMIM entry 261100](https://omim.org/entry/261100)
- [Involvement of the H+/K+-ATPase α subunit as a major antigenic protein in autoimmune gastritis induced by neonatal thymectomy in mice — Clin Exp Immunol](https://academic.oup.com/cei/article/89/1/63/6488118)
- [Experimental autoimmune gastritis: mouse models of human organ-specific autoimmune disease — PubMed 15763991](https://pubmed.ncbi.nlm.nih.gov/15763991/)
- [The parietal cell autoantigens recognized in neonatal thymectomy-induced murine gastritis — PubMed 1648525](https://pubmed.ncbi.nlm.nih.gov/1648525/)
- [Spontaneous Autoimmune Gastritis in C3H/He Mice — PubMed 9777963](https://pubmed.ncbi.nlm.nih.gov/9777963/)
- [Immunization with gastric H+/K(+)-ATPase induces a reversible autoimmune gastritis — PMC1363986](https://pmc.ncbi.nlm.nih.gov/articles/PMC1363986/)
- [Th1, Th2 and Th17 Effector T Cell-Induced Autoimmune Gastritis Differs in Pathological Pattern and Susceptibility to Suppression by Regulatory T Cells — PMC2561289](https://pmc.ncbi.nlm.nih.gov/articles/PMC2561289/)
- [Expression of the gastric H/K-ATPase alpha-subunit in the thymus — PubMed 9272282](https://pubmed.ncbi.nlm.nih.gov/9272282/)
- [Type 1 Diabetes Mellitus and Autoimmune Diseases: A Critical Review — MDPI](https://www.mdpi.com/2075-4426/13/3/422)
- [Editorial: The Association of Other Autoimmune Diseases in Patients With Thyroid Autoimmunity — PMC6146093](https://pmc.ncbi.nlm.nih.gov/articles/PMC6146093/)
- [Comorbidities in Autoimmune Disease & Multiple Autoimmune Syndrome — Autoimmune Institute](https://www.autoimmuneinstitute.org/articles/comorbidities-in-autoimmune-disease-multiple-autoimmune-syndrome/)