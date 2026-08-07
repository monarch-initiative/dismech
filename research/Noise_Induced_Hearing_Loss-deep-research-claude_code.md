---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-20T16:27:27.052231'
end_time: '2026-07-20T16:35:19.026308'
duration_seconds: 471.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Noise Induced Hearing Loss
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
  - claude-opus-4-8
  web_search_requests: 6
  num_turns: 10
  total_cost_usd: 2.4188
  session_id: 406ef896-4bdc-446e-978b-e2caf8616b78
  stop_reason: end_turn
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Noise Induced Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Noise Induced Hearing Loss** covering all of the
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

Alright, I've got a solid evidence base. Here's the full report.

---

# Research Report: Noise-Induced Hearing Loss (NIHL)

*A quick orienting note before we dive in, since this one behaves differently from most dismech entries: NIHL isn't a broken gene you're born with — it's an environmental injury to a gorgeous, non-renewable piece of tissue. Your cochlea's hair cells are like the enamel on your teeth: once ground down, they don't grow back. So the whole story here is about a mechanical/chemical assault on cells that can't regenerate, plus a genetic lottery that decides how tough your particular set of hair cells happens to be. Keep that framing in your back pocket — it explains why "prevention" is the loudest section and "cure" is basically empty.*

Wherever I couldn't nail an ontology ID down cold, I've flagged it **[verify]** rather than invent one — same anti-hallucination discipline the repo lives by.

---

## 1. Disease Information

**Overview.** Noise-induced hearing loss is an acquired, typically bilateral **sensorineural** hearing loss caused by exposure to hazardous sound — either a single intense blast (**acoustic trauma**) or, far more commonly, chronic repeated exposure (occupational/recreational). The damage lands on the sensory cells and synapses of the inner ear (cochlea), producing a characteristic high-frequency loss with a notch around 3–6 kHz (classically **4 kHz**). It is one of the most common causes of sensorineural hearing loss worldwide (second to age-related presbycusis) and is generally cited as **the most prevalent occupational disease on the planet** ([Chen et al., 2020, *Environ Health Prev Med*, PMC7603754](https://pmc.ncbi.nlm.nih.gov/articles/PMC7603754/)).

**Key identifiers:**
- **MeSH:** D006311 — "Hearing Loss, Noise-Induced" (high confidence)
- **ICD-10:** **H83.3** "Noise effects on inner ear" (occupational sensorineural loss is often additionally coded under H90.3–H90.5)
- **ICD-11:** block for effects of noise on the inner ear (foundation code should be **[verify]** against the current ICD-11 browser)
- **MONDO:** a "noise-induced hearing loss" term exists in MONDO but I could not confirm the exact CURIE from the sources retrieved — **[verify]** by searching `sqlite:obo:mondo` for "noise-induced hearing loss" before curating the `disease_term`
- **OMIM:** none as a Mendelian disease (this is a complex/multifactorial trait; OMIM covers *susceptibility loci* only, e.g. some hereditary deafness genes)
- **Orphanet:** not a rare disease — no primary ORPHA entry expected
- **SNOMED CT / Category:** Complex (environmental injury with genetic susceptibility)

**Synonyms:** acoustic trauma (acute form), occupational hearing loss, noise-induced deafness, sociacusis (societal/recreational noise), boilermaker's ear/"boilermaker's deafness" (historical), industrial hearing loss, sensorineural hearing loss due to noise.

**Data provenance.** Information is **aggregated / disease-level** — drawn from occupational epidemiology, audiometric surveillance cohorts, animal mechanistic studies, and clinical review literature — rather than a single-patient EHR resource. Individual-level data exist in occupational surveillance registries (OSHA/NIOSH standard-threshold-shift records).

---

## 2. Etiology

**Primary cause.** Excessive acoustic energy delivered to the cochlea. Two exposure archetypes:
1. **Acoustic trauma** — a single or brief exposure to extremely intense sound (impulse/blast, typically **>120–140 dB SPL**: gunfire, explosions, industrial blasts). Can cause immediate, permanent mechanical destruction of the organ of Corti.
2. **Chronic occupational/recreational NIHL** — cumulative repeated exposure above ~**85 dBA** (8-hour time-weighted average), building damage over months to years. "Occupational NIHL may occur with sustained exposure to noise levels of 85 dB or higher for eight hours per day or 40 hours per week" ([Chen et al., 2020, PMC7603754](https://pmc.ncbi.nlm.nih.gov/articles/PMC7603754/)).

Damage depends on **intensity, duration, frequency spectrum, and temporal pattern** (impulse noise is more damaging than continuous energy-equivalent noise).

**Risk factors — environmental/exposure:**
- Occupational noise (mining, construction, manufacturing, agriculture, military, aviation, music industry)
- Recreational noise (firearms/hunting, concerts, personal listening devices, power tools, motorsports)
- **Ototoxic co-exposures that synergize with noise:** organic **solvents** (toluene, styrene, xylene), **heavy metals** (lead, mercury), **carbon monoxide** and asphyxiants, and ototoxic drugs (aminoglycosides, cisplatin, loop diuretics). These are more than additive — think of noise and solvents as two people leaning on the same rotten floorboard.
- Whole-body/hand-arm **vibration** (co-exposure amplifies risk)

**Risk factors — host/demographic:**
- **Age** (older cochleae more vulnerable; NIHL and presbycusis compound)
- **Male sex** — largely an *exposure* effect (more high-noise occupations); "being female serving as a protective factor" in occupational cohorts ([Frontiers Public Health 2024, PMC11557527](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11557527/))
- **Cardiovascular risk** — hypertension, hyperlipidemia, diabetes (compromised cochlear microcirculation); an active area of study ([Frontiers Cell Neurosci 2025, "Interplay between NIHL and hypertension," PMC12009814](https://pmc.ncbi.nlm.nih.gov/articles/PMC12009814/))
- **Smoking** and heavy alcohol use
- **Lighter pigmentation** (see protective factors — melanin)
- **Genetic susceptibility** (see §4)

**Protective factors:**
- **Environmental/behavioral:** hearing protection (earplugs/earmuffs), reduced exposure time/intensity, distance from source, dietary **antioxidants and magnesium**, and the intriguing **"conditioning"/"toughening"** phenomenon — sub-damaging low-level sound pre-exposure renders the cochlea more resistant to a subsequent traumatic exposure.
- **Melanin/pigmentation:** strial melanocytes appear otoprotective; darker-pigmented individuals show relatively lower NIHL susceptibility.
- **Female sex** (partly exposure, possibly partly estrogen-related protection).
- **Genetic:** favorable antioxidant-enzyme alleles (e.g. certain CAT, GST genotypes) associate with lower threshold shifts.

**Gene–environment interaction.** NIHL is a textbook **GxE trait**: identical noise doses yield very different outcomes across individuals, and susceptibility genes only manifest *in the presence of* the noise insult. A mouse study explicitly framed it this way — "Genetic Architecture of Noise-Induced Hearing Loss: Evidence for a Gene-by-Environment Interaction" ([Lavinsky et al., 2016, *G3*](https://academic.oup.com/g3journal/article/6/10/3219/6032507)). The GWAS-nominated **Nox3** locus is a prime example of a gene whose effect is only "unmasked" by noise ([Lavinsky et al., 2015, *PLoS Genet*, PMC4399881](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4399881/)).

---

## 3. Phenotypes

Core clinical picture: **bilateral, high-frequency, sensorineural** hearing loss, usually symmetric (asymmetry is a red flag for firearm exposure — "shooter's ear," worse in the ear opposite the shouldered rifle — or for a non-NIHL cause).

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| Sensorineural hearing impairment | Clinical sign | High-frequency, bilateral; notch at 3–6 kHz (classically 4 kHz) with relative recovery at 8 kHz | **HP:0000407** Sensorineural hearing impairment |
| High-frequency hearing loss | Clinical sign | Earliest and most prominent; notch pattern | **HP:0008542** high-frequency hearing impairment **[verify label/ID]** |
| Tinnitus | Symptom | Very common, often first/most bothersome symptom; frequently chronic | **HP:0000360** Tinnitus |
| Difficulty hearing in noise (speech-in-noise deficit) | Symptom | Hallmark of "hidden hearing loss"/synaptopathy; may precede audiometric threshold change | HPO term for impaired speech discrimination **[verify]** |
| Hyperacusis | Symptom | Reduced sound tolerance | hyperacusis HPO term **[verify]** |
| Temporary threshold shift (TTS) | Lab/functional | Transient loss recovering over ~hours–day post-exposure; a warning sign | (functional, not a standing HP term) |
| Permanent threshold shift (PTS) | Lab/functional | Irreversible audiometric loss | maps to HP:0000407 |
| Diplacusis | Symptom | Same tone perceived at different pitches between ears | **[verify]** |

**Characteristics:**
- **Age of onset:** any age with sufficient exposure; occupational cases typically manifest after **years of cumulative exposure** in adulthood; acoustic trauma can strike instantly at any age.
- **Severity:** variable — mild high-frequency notch to moderate-severe SNHL; WHO grades: slight (20–40 dB), moderate (41–60 dB), severe (61–80 dB), profound (≥81 dB) ([Chen et al., 2020, PMC7603754](https://pmc.ncbi.nlm.nih.gov/articles/PMC7603754/)).
- **Progression:** progressive *while exposure continues*, then **stabilizes once exposure stops** (a key distinction from presbycusis, which keeps advancing). The notch typically deepens and widens over the first ~10–15 years of continuous exposure.
- **Frequency among affected:** tinnitus accompanies a large share of NIHL cases; speech-in-noise complaints are near-universal in significant loss.

**Quality-of-life impact:** communication difficulty, social withdrawal, occupational limitation, chronic tinnitus-related distress/insomnia, depression/anxiety, and an association with **accelerated cognitive decline and dementia risk** in the broader hearing-loss literature. Tinnitus is often the single most QoL-degrading feature.

---

## 4. Genetic / Molecular Information

**No single causal gene** — NIHL is polygenic susceptibility layered on an environmental trigger. Candidate/associated genes cluster into functional pathways ([Zhang et al., 2022, *Front Cell Neurosci*, "The Role of Genetic Variants in the Susceptibility of NIHL," PMC9315435](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9315435/)):

- **Oxidative-stress / antioxidant defense:** **CAT** (catalase), **SOD2**, **GSTM1**, **GSTT1**, **PON2**, **NQO1**, **NOX3** (NADPH oxidase 3). The 2022 review: *"Mutations of oxidative stress related genes would disturb the balance of the oxidative and antioxidative system in the cochlea… ultimately result in hearing loss."*
- **Potassium ion recycling / channels:** **KCNQ4**, **KCNE1**, **GJB2** (connexin 26). KCNQ4 and KCNE1 were among the most reproducible across Polish, Swedish, and Chinese cohorts ([PMC9315435](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9315435/)).
- **Hair-cell structure / stereocilia & monogenic-deafness genes:** **PCDH15**, **CDH23**, **MYH14**, **GRHL2**, **EYA4** — variants that already cause hereditary deafness also modulate noise vulnerability.
- **Heat-shock / stress response:** **HSPA1A / HSPA1L (HSP70)**.

**GWAS.** A genome-wide association study in the Hybrid Mouse Diversity Panel identified **Nox3** on chromosome 17 as a critical susceptibility gene, with the top functional cluster enriched for **mitochondrial** genes ([Lavinsky et al., 2015, PMC4399881](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4399881/)). Human GWAS have been comparatively underpowered given exposure heterogeneity.

**Suggested HGNC/gene annotations:** KCNQ4, KCNE1, CAT, SOD2, GSTM1, GSTT1, PON2, NOX3, HSPA1A, HSPA1L, PCDH15, MYH14, GRHL2, EYA4, GJB2, CDH23 (bind with lowercase `hgnc:` per repo convention).

**Variant classification:** these are **germline susceptibility polymorphisms** (risk-modifying, not "pathogenic" in the ACMG Mendelian sense) — appropriately typed with `relationship_type: SUSCEPTIBILITY` and, given the strong GxE, `HP:0010982` polygenic inheritance framing is a reasonable model note. Somatic variation is not relevant.

**Epigenetics:** an emerging area — noise exposure is associated with **DNA methylation changes** and altered **miRNA** expression in cochlear tissue in animal models; human epigenomic data are still thin. Flag as a knowledge gap.

**Chromosomal abnormalities:** none — not applicable.

---

## 5. Environmental Information

- **Environmental factors (the whole ballgame):** occupational noise (manufacturing, mining, construction, agriculture, military, transportation, entertainment) and recreational noise (firearms, amplified music/concerts, personal audio devices, power tools, motorsports). Impulse/blast noise > continuous noise for equivalent energy.
- **Co-toxicant exposures (synergistic ototoxicity):** organic solvents (**toluene, styrene, xylene, trichloroethylene**), heavy metals (**lead, mercury**), **carbon monoxide**, and pesticides — these potentiate noise damage (relevant CTD/TOXNET territory).
- **Lifestyle factors:** **smoking** (vascular/oxidative), heavy **alcohol**, and possibly poor cardiovascular/metabolic health as effect modifiers.
- **Infectious agents:** not applicable — NIHL is a physical/chemical injury, not infectious.

---

## 6. Mechanism / Pathophysiology

The best current synthesis recognizes **three overlapping injury mechanisms** ([Kurabi et al., 2017, "Cellular mechanisms of noise-induced hearing loss," *Hear Res*, PMID: 27916698, PMC6750278](https://pmc.ncbi.nlm.nih.gov/articles/PMC6750278/); [encyclopedia synthesis](https://encyclopedia.pub/entry/45066)):

**(1) Mechanical destruction (acoustic trauma).** Extreme intensity directly shears the organ of Corti. *"Sufficiently intense overstimulation of the cochlea… will produce mechanical damage… includes direct mechanical disruption of HC stereociliary arrays"* (Kurabi et al.). Includes stereocilia fracture, uncoupling from the tectorial membrane, reticular-lamina rupture, and hair-cell death. **Uncoupling of outer-hair-cell stereocilia from the tectorial membrane** is the primary morphological correlate of reversible **temporary threshold shift**.

**(2) Metabolic / oxidative decompensation (chronic moderate-intense noise).** Overstimulation drives excess metabolic demand → mitochondrial overproduction of **reactive oxygen and nitrogen species (ROS/RNS)**. *"Damaging levels of noise lead to metabolic overstimulation and subsequent generation of free radical species… reactive oxygen species are observed in hair cells after acoustic overexposure and exist there for about 10 days"* — a lingering chemical fire, not a one-and-done. ROS drive **lipid peroxidation** (toxic 4-HNE), DNA damage, and activation of stress pathways (**MAPK/JNK**), tipping hair cells into **apoptosis and/or necroptosis** (*"Apoptosis occurs through the sequential actions of caspases"* — Kurabi et al.). **Outer hair cells of the basal (high-frequency) turn** are the most vulnerable population. Reduced **cochlear blood flow / ischemia-reperfusion** and **stria vascularis** dysfunction (endocochlear potential drop) contribute.

**(3) Glutamate excitotoxicity & cochlear synaptopathy.** Overstimulated inner hair cells dump excess **glutamate** at the ribbon synapse → afferent dendrite swelling → loss of **IHC–spiral-ganglion-neuron ribbon synapses**. This "cochlear synaptopathy" / **hidden hearing loss** can occur *with normal audiometric thresholds*, producing speech-in-noise and temporal-processing deficits, and is followed by delayed spiral-ganglion-neuron loss. The classic demonstration: excess glutamate release with afferent swelling, and strong protection by the glutamate antagonist kynurenate ([Puel et al., 1998, *Neuroreport*, PMID: 9674603](https://pubmed.ncbi.nlm.nih.gov/9674603/)). Note the field is actively debating **partial synaptic self-repair** (2025 reviews: [Wang et al., *Adv Sci*, PMC12362826](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12362826/)).

**Inflammation:** resident cochlear **macrophages** are recruited and pro-inflammatory cytokines rise, amplifying injury — a downstream/modulating arm.

**Causal chain (upstream → downstream):**
`Hazardous sound energy` → (mechanical stress on organ of Corti) → **[branch A: mechanical stereocilia/hair-cell disruption]** and/or **[branch B: metabolic overdrive → mitochondrial ROS/RNS → lipid peroxidation + JNK/MAPK → OHC apoptosis/necroptosis]** and/or **[branch C: glutamate excitotoxicity → ribbon-synapse loss → SGN degeneration]** → cochlear neuroinflammation → **permanent sensorineural threshold shift + tinnitus + speech-in-noise deficit**.

**Suggested ontology terms:**
- **Cell types (CL):** cochlear outer hair cell **CL:0000601**; cochlear inner hair cell **CL:0000589**; spiral ganglion neuron **[verify — CL:0000103 neuron as fallback]**; cochlear macrophage; strial marginal cell / cochlear fibrocyte **[verify]**.
- **Biological processes (GO):** response to oxidative stress **GO:0006979**; cellular response to oxidative stress **GO:0034599**; reactive oxygen species metabolic process **GO:0072593**; apoptotic process **GO:0006915**; glutamate receptor signaling pathway **GO:0007215**; sensory perception of sound **GO:0007605**; lipid peroxidation **[verify]**; inflammatory response **GO:0006954**.
- **Subcellular (GO CC):** mitochondrion **GO:0005739** (ROS source); stereocilium / stereocilium bundle **[verify]**; ribbon synapse **[verify]**.
- **CHEBI:** reactive oxygen species **CHEBI:26523**; hydrogen peroxide **CHEBI:16240**; L-glutamate **CHEBI:29985** **[verify]**; glutathione **CHEBI:16856**.

**Molecular profiling:** transcriptomic (GEO) and proteomic studies of noise-exposed cochlea show upregulation of oxidative-stress, apoptosis, and inflammatory programs; single-cell/spatial cochlear atlases are emerging but human tissue is scarce (post-mortem/temporal-bone limited). Treat any single-cell claims as **HUMAN_MODEL_MISMATCH** candidates — most mechanistic data are rodent.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** the **cochlea** (inner ear), specifically the **organ of Corti**. Body system: **auditory / nervous / special sense**.
- **Secondary:** **spiral ganglion / cochlear nerve (CN VIII)** with retrograde degeneration; central auditory pathway plasticity implicated in tinnitus.

**Tissue / cell level:**
- Sensory epithelium of the organ of Corti — **outer hair cells** (first and hardest hit, basal turn), then **inner hair cells**; **spiral ganglion neurons**; **stria vascularis** (marginal/intermediate/basal cells) and its melanocytes; supporting cells and cochlear fibrocytes.

**Subcellular level:**
- **Mitochondria** (ROS generation), **stereocilia bundles** (mechanical target), **ribbon synapses** (excitotoxic target), plasma membrane/lipid bilayer (peroxidation).

**Localization (UBERON):**
- inner ear **UBERON:0001846**; cochlea **UBERON:0001844**; organ of Corti / spiral organ **UBERON:0002227**; stria vascularis **UBERON:0002542** **[verify]**; spiral ganglion **UBERON:0001691** **[verify]**; cochlear (auditory) nerve **UBERON:0001648** **[verify]**.
- **Tonotopic pattern:** high-frequency (basal-turn) region damaged first → the 3–6 kHz audiometric notch.
- **Lateralization:** usually **bilateral and symmetric**; **asymmetric** in firearm/impulse exposure (shooter's ear).

---

## 8. Temporal Development

- **Onset:** any age with adequate exposure. Chronic occupational NIHL usually manifests after **years** of cumulative exposure; **acoustic trauma** is instantaneous.
- **Onset pattern:** insidious/chronic (occupational) vs. acute (acoustic trauma/blast).
- **Progression stages:** early = transient **TTS** and a subtle 4 kHz notch → intermediate = fixed notch (**PTS**) that deepens/widens → advanced = broader high- and mid-frequency SNHL affecting speech frequencies.
- **Rate:** for continuous occupational exposure, threshold shift is fastest in the **first 10–15 years**, then plateaus; the disease **stops progressing once exposure ceases** (contrast presbycusis).
- **Course pattern:** progressive-then-stable; **TTS is the reversible warning phase**, PTS is permanent.
- **Remission:** none for established PTS — mammalian hair cells don't regenerate. TTS "remits" spontaneously within ~24 h.
- **Critical window:** the hours-to-days after acute exposure (TTS phase) is the only realistic **therapeutic window** — the rationale behind acute-trauma steroid trials and experimental otoprotectants.

---

## 9. Inheritance and Population

**Epidemiology:**
- WHO: ~**16%** of adult disabling hearing loss is attributable to occupational noise (regional range **7–21%**); ~**5.3%** of the global population exhibits NIHL, with ~10% exposed to hazardous noise ([Chen et al., 2020, PMC7603754](https://pmc.ncbi.nlm.nih.gov/articles/PMC7603754/)).
- **Occupational NIHL is the most prevalent occupational disease globally**; higher burden in less-developed regions; occupational-attributable burden ranges from ~11% (South Africa) to ~58% (USA) in the reviewed literature.
- In the US, tens of millions of workers are exposed to hazardous noise (NIOSH); WHO also flags **~1.1 billion young people** at risk from recreational/leisure noise.

**Genetic/inheritance parameters:** **not Mendelian** — **multifactorial / polygenic susceptibility** with a strong **gene-by-environment** structure. No classic inheritance pattern, penetrance, expressivity, anticipation, founder effect, or carrier frequency in the single-gene sense. Model susceptibility with `HP:0010982` (polygenic) plus `SUSCEPTIBILITY`-typed candidate genes.

**Population demographics:**
- **Sex:** male predominance, mostly **exposure-driven** (female sex is protective in occupational cohorts).
- **Ethnicity/pigmentation:** lighter-pigmented individuals show somewhat greater susceptibility (melanin hypothesis).
- **Geographic:** tracks industrial and military noise exposure; higher measured prevalence in lower-income/less-regulated settings.
- **Age:** compounds with presbycusis; older workers show greater cumulative loss.

---

## 10. Diagnostics

**Clinical/functional tests:**
- **Pure-tone audiometry** — the cornerstone: bilateral high-frequency SNHL with a **3–6 kHz notch** (classically 4 kHz) and recovery at 8 kHz; *"hearing thresholds at 2 and 8 kHz are both at least 10 dB HL better than the threshold at 4 kHz"* is a common notch definition ([Indian J Otol / notch screening literature](https://journals.lww.com/ijoo/fulltext/2015/21040/audiometric_notching_at_4_khz__good_screening_test.9.aspx)).
- **Otoscopy & tympanometry** — normal (confirms sensorineural, not conductive).
- **Otoacoustic emissions (DPOAE)** — sensitive early marker of outer-hair-cell dysfunction, can flag damage before threshold change.
- **ABR / electrocochleography** — reduced **wave I amplitude** is the emerging biomarker of cochlear **synaptopathy / hidden hearing loss**.
- **Speech-in-noise & extended high-frequency audiometry** — catch functional deficits missed by standard audiometry.
- **Occupational surveillance:** serial audiograms tracking **Standard Threshold Shift (STS)** (OSHA: ≥10 dB average shift at 2, 3, 4 kHz).

**Genetic testing:** not routine clinically; research-only susceptibility panels (oxidative-stress, K⁺-channel, HSP genes). WES/WGS not indicated for diagnosis (rule out hereditary deafness only if the picture is atypical).

**Omics diagnostics:** none clinically validated; research transcriptomic/proteomic signatures exist in animal cochlea.

**Diagnostic criteria & differential:** diagnosis is clinical — **hazardous-exposure history + compatible audiometric notch + normal otoscopy/middle ear**. Differential: **presbycusis** (symmetric, progressive, no plateau, less notch), **ototoxic drug/chemical loss**, **sudden SNHL** (acute, often unilateral), **Ménière disease** (fluctuating low-frequency, vertigo), **vestibular schwannoma / retrocochlear** (asymmetric — image if so), hereditary/genetic SNHL, autoimmune inner-ear disease.

**Screening:** workplace **hearing conservation program** audiometric surveillance (OSHA 29 CFR 1910.95) — baseline + annual audiograms for noise-exposed workers.

---

## 11. Outcome / Prognosis

- **Reversibility:** established **PTS is permanent and irreversible** (no mammalian hair-cell regeneration). **TTS fully recovers** within ~24 h if exposure stops.
- **Progression:** halts once exposure ceases — so prognosis hinges on **removing the exposure**.
- **Mortality:** NIHL is **not directly fatal**; morbidity is the story.
- **Morbidity / disability:** communication disability, occupational limitation, chronic **tinnitus** (frequent, often the dominant QoL burden), social isolation, depression, elevated injury risk (impaired hazard awareness), and the population-level association of hearing loss with **cognitive decline/dementia**. Measured with EQ-5D, SF-36, and hearing-specific PROMs (e.g. HHIE, THI for tinnitus).
- **Prognostic factors:** cumulative noise dose, peak intensity, impulse component, co-exposure to ototoxicants, age, cardiovascular/metabolic comorbidity, and genetic susceptibility. For **acute acoustic trauma**, earlier intervention (steroids) and lower initial threshold shift predict better recovery.

---

## 12. Treatment

**Bluntly: there is no cure for established NIHL.** Management is rehabilitative + (for acute trauma) a narrow rescue window + a large experimental pipeline.

**Established management (chronic/permanent loss):**
- **Hearing aids** — first-line amplification for symptomatic loss. *Suggested MAXO: hearing-aid device / auditory assistive technology* **[verify MAXO ID]**.
- **Cochlear implantation** — for severe-to-profound loss not aided adequately. *MAXO cochlear implantation* **[verify]**.
- **Aural rehabilitation / auditory training**, assistive listening devices, communication strategies. *MAXO: rehabilitation MAXO:0000015 / supportive care MAXO:0000950* **[verify].**
- **Tinnitus management:** cognitive behavioral therapy, sound/masking therapy, tinnitus retraining. *MAXO: psychotherapy / behavioral intervention* **[verify].**

**Acute acoustic trauma (rescue, within days):**
- **Corticosteroids** (systemic and/or intratympanic) — borrowed from sudden-SNHL protocols; evidence moderate. *treatment_term NCIT:C15986 Pharmacotherapy + therapeutic_agent corticosteroid (CHEBI/NCIT).*
- **Hyperbaric oxygen** — used in some centers, evidence controversial.

**Experimental otoprotectants (mostly antioxidant/anti-apoptotic; strong in animals, unproven in humans):**
- **N-acetylcysteine (NAC)** — reliably protective in the lab but **clinically unproven**: a large military RCT (277 NAC vs 289 placebo after weapons training) did **not** reject the null for standard threshold shift ([Kopke et al., 2015, *Hear Res*, PMID: 25620313](https://pubmed.ncbi.nlm.nih.gov/25620313/)). *"NAC has consistently reduced permanent NIHL in the laboratory, but its clinical efficacy is still controversial."*
- **D-methionine** — Phase 3 military trial ([NCT02903355](https://cdn.clinicaltrials.gov/large-docs/55/NCT02903355/Prot_SAP_000.pdf)).
- **Ebselen (SPI-1005)** — glutathione-peroxidase mimetic, clinical trials.
- **Magnesium, ACEMg (vitamins A/C/E + Mg), coenzyme Q10, resveratrol, sodium thiosulfate, zinc** (tinnitus) — mixed/early data ([NCT02951715](https://clinicaltrials.gov/study/NCT02951715), [NCT00808470](https://clinicaltrials.gov/study/NCT00808470)).
- **Neurotrophin therapy (NT-3, BDNF)** — to regrow ribbon synapses in synaptopathy (preclinical).
- **Hair-cell regeneration** (Atoh1 gene therapy, Notch/γ-secretase inhibitors) — experimental, not clinical.

**Pharmacogenomics:** minimal established guidance; susceptibility genotyping is research-only.

---

## 13. Prevention

**This is the section that actually saves ears — NIHL is almost entirely preventable.**

**Primary prevention — hierarchy of controls (occupational):**
1. **Elimination/substitution & engineering controls** — quieter machinery, enclosures, damping (most effective).
2. **Administrative controls** — limit exposure time, rotate workers, distance.
3. **Hearing Protection Devices (HPDs)** — earplugs/earmuffs (rated by NRR) as last line.
4. **Regulatory limits:** OSHA PEL **90 dBA** (8-h TWA) with a **85 dBA action level** (29 CFR 1910.95); **NIOSH REL 85 dBA** with a 3-dB exchange rate; EU limits similar. **Hearing Conservation Programs** are mandated above the action level.
5. **Public-health education:** WHO **"Make Listening Safe"** for recreational noise; safe-listening standards for personal audio and venues.

**Secondary prevention:** **audiometric surveillance** to catch STS early and intervene (remove from exposure, refit HPDs). Baseline + annual audiograms.

**Tertiary prevention:** prevent further loss (rigorous exposure avoidance once loss is detected) and mitigate disability (hearing aids, rehab).

**Behavioral interventions:** turn down volume, take listening breaks, increase distance from sources, wear HPDs at concerts/ranges/power-tool use.

**Pharmacoprevention:** experimental (see §12) — no approved pharmacologic prophylaxis yet.

**Counseling:** occupational-health counseling on HPD use; not a genetic-counseling disease.

**Immunization / prophylactic drugs:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy affected:** any mammal with a cochlea is susceptible. Well-documented experimentally in **mouse (NCBITaxon:10090), rat (10116), guinea pig (10141), chinchilla (34682), gerbil (10047)**; also relevant to **marine mammals** (cetaceans — sonar/blast) and captive/working animals exposed to loud environments.
- **Breed:** no classic breed-specific NIHL (unlike congenital pigment-associated deafness in dogs/cats, which is a different mechanism). Working/military dogs are a practical exposure concern. **VBO:** not applicable.
- **Orthologous genes:** the candidate genes are conserved (mouse *Kcnq4, Cat, Sod2, Nox3, Hspa1a/b, Pcdh15, Cdh23*, etc.) — the **Nox3** susceptibility signal was itself discovered in mice ([PMC4399881](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4399881/)).
- **Natural disease / veterinary relevance:** primarily a concern for **marine mammals** (anthropogenic ocean noise) and working animals; OMIA does not treat it as a Mendelian animal disorder.
- **Comparative biology:** cochlear injury mechanisms (OHC loss, oxidative stress, excitotoxic synaptopathy) are **highly conserved across mammals** — which is exactly why rodent models translate mechanistically (even as pharmacology stubbornly fails to translate to human protection).
- **Transmission / zoonosis:** not applicable (non-infectious).

---

## 15. Model Organisms

- **Mouse** (*Mus musculus*, MGI): the workhorse. **CBA/CaJ** is preferred for auditory work (good hearing into old age); **C57BL/6** is common but carries the **Cdh23^ahl** age-related-hearing-loss allele that confounds noise studies (recent synaptopathy work in **C57BL/6N**: [PMC11473312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11473312/)). Knockouts/transgenics test candidate genes; the **Hybrid Mouse Diversity Panel** enabled the Nox3 GWAS.
- **Chinchilla** (*Chinchilla lanigera*): the **gold standard for behavioral audiometry** — audible range overlaps humans, large cochlea for histology; classic excitotoxicity/synaptopathy and otoprotection studies.
- **Guinea pig** (*Cavia porcellus*): accessible cochlea, standard for pharmacologic otoprotection and cochlear physiology.
- **Rat** (*Rattus norvegicus*, RGD): common for noise-exposure + antioxidant studies.
- **Zebrafish** (*Danio rerio*, ZFIN): lateral-line **neuromast** hair cells for high-throughput ototoxicity/otoprotection screening and **hair-cell regeneration** biology (fish *do* regenerate hair cells — the tantalizing contrast with mammals).

**Model design:** almost all are **induced** (controlled noise exposure at defined SPL/duration/spectrum), sometimes layered on genetic backgrounds to probe susceptibility genes.

**Recapitulation & limitations:** rodent models faithfully reproduce OHC loss, the metabolic/oxidative cascade, excitotoxic synaptopathy, and threshold shifts — mechanistically excellent. **The persistent gap:** protective compounds that work beautifully in these models (NAC, D-methionine, ACEMg) have **repeatedly underperformed in human trials** — a textbook **HUMAN_MODEL_MISMATCH** worth flagging in the KB entry. Human cochlear tissue is nearly inaccessible in life, so mechanistic human confirmation lags animal data by design.

**Resources:** MGI, IMPC/KOMP (mouse), RGD (rat), ZFIN (zebrafish), plus the auditory-neuroscience literature (Liberman/Kujawa synaptopathy work, Puel excitotoxicity work).

---

## Curation notes for the dismech entry

- **Category "Complex" is exactly right** — model this as an **environmental injury with polygenic susceptibility**, not a gene-disease entry. Use `SUSCEPTIBILITY`-typed genes and an `HP:0010982` polygenic inheritance note; don't force a Mendelian frame.
- **Strong module-conformance candidates:** this is a clean fit for **`sensorineural_hair_cell_loss`** (`#Hair Cell Mechanotransduction Failure and Death` — the conserved SNHL final common pathway). The oxidative-stress/apoptosis arm also touches generic ROS→apoptosis logic; worth a `conforms_to` on the hair-cell-loss module at minimum.
- **Best-verified PMIDs to anchor evidence** (all fetched/confirmed live, but re-run `just fetch-reference` before quoting — snippets above are paraphrase-safe summaries, *not* guaranteed exact abstract substrings):
  - **27916698** — Kurabi et al., cellular mechanisms (mechanism backbone)
  - **9674603** — Puel et al., excitotoxicity & synapse repair
  - **25620313** — Kopke et al., NAC RCT (negative — good REFUTE/PARTIAL evidence for otoprotection)
  - Nox3 GWAS (Lavinsky 2015, PMC4399881) and the 2022 genetic-susceptibility review (PMC9315435) for the genetics block
- **Anti-hallucination reminder:** every ontology ID I marked **[verify]** (spiral ganglion CL, several UBERON inner-ear terms, high-frequency-hearing-loss HP, MAXO device terms, the MONDO CURIE) needs an OAK check (`runoak … info`) before it goes in a `term:` — I deliberately didn't guess IDs I couldn't stand behind.

**Sources:**
- [Cellular mechanisms of noise-induced hearing loss (Kurabi et al., PMC6750278 / PMID 27916698)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6750278/)
- [An overview of occupational NIHL: epidemiology, pathogenesis, prevention (Chen et al., PMC7603754)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7603754/)
- [The Role of Genetic Variants in the Susceptibility of NIHL (PMC9315435)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9315435/)
- [GWAS identifies Nox3 for NIHL susceptibility (Lavinsky et al., PMC4399881)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4399881/)
- [Genetic architecture of NIHL: gene-by-environment (Lavinsky et al., G3 2016)](https://academic.oup.com/g3journal/article/6/10/3219/6032507)
- [NIHL: molecular targets and interventions (PMC8279877)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8279877/)
- [Excitotoxicity and repair of cochlear synapses (Puel et al., PMID 9674603)](https://pubmed.ncbi.nlm.nih.gov/9674603/)
- [NAC prevention RCT (Kopke et al., PMID 25620313)](https://pubmed.ncbi.nlm.nih.gov/25620313/)
- [Consequences and mechanisms of noise-induced cochlear synaptopathy (Wang et al., 2025, PMC12362826)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12362826/)
- [Noise-induced synaptopathy in C57BL/6N mice (PMC11473312)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11473312/)
- [NIHL & hypertension interplay (PMC12009814)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12009814/)
- [Occupational epidemiology of NIHL (PMC11557527)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11557527/)
- [Audiometric notching at 4 kHz screening](https://journals.lww.com/ijoo/fulltext/2015/21040/audiometric_notching_at_4_khz__good_screening_test.9.aspx)
- [D-methionine Phase 3 trial (NCT02903355)](https://cdn.clinicaltrials.gov/large-docs/55/NCT02903355/Prot_SAP_000.pdf)

*And that's the whole cochlea's sad little saga — a sensory organ that gives you one set of hair cells for the whole ride, no refills, no do-overs. Which is why the entire clinical playbook boils down to "please, for the love of Podunk, wear the earplugs." Happy curating.*